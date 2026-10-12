#!/usr/bin/env python3
"""Assemble one Aeneid part from its draft.   usage: python3 build_aeneid.py aeneid-NNN

Reads   drafts/aeneid-NNN/units.json   {title, titleEn, part, about, sentences:[{t,l,i,n,ln,v,p?,advisory?}]}
        drafts/aeneid-NNN/gloss.json   {form: "lemma — meaning (parse)"} for every form not yet in aeneid-glossary.json
                                       optional key "__broaden__": {form: new entry} — the new entry must CONTAIN the old one
Writes  <root>/aeneid-NNN.json, <root>/aeneid-glossary.json (new keys added, sorted), and the manifest entry in
        <root>/stories.json after the previous part. Refuses, changing nothing, on any failure.
sc (scansion) is made here by the shared Latin scanner (.github/scripts/scan_latin.py, the one Ovid uses);
a drafter never writes it."""
import sys, os, re, json
import aeneid_lib as A
import scan_latin as SL
pid = sys.argv[1]; P = A.part(pid); L = A.lines_of(P)
def die(*a): print('BUILD REFUSED:', *a); sys.exit(1)
if A.sha(L) != P['sha256']: die('source text does not match parts.json sha256')
D = A.jload(os.path.join(A.HERE, 'drafts', pid, 'units.json'))
for k in ('title', 'titleEn', 'part', 'about'):
    if not D.get(k): die('units.json missing', k)
if P['cite'] not in D['part'] or P['cite'] not in D['titleEn']: die('part/titleEn must carry the citation', P['cite'])
# ---- tiling: the units' t, joined in order, reproduce the edition character for character
S = '\n'.join(l['t'] for l in L); nums = [l['n'] for l in L]; paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
pos = 0; li = 0; atStart = True; errs = []
for k, u in enumerate(D['sentences']):
    t = u.get('t', '')
    if not t or not S.startswith(t, pos): die(f'unit {k}: t does not match the edition at line {nums[li]}: expected {S[pos:pos+50]!r}')
    if u.get('ln') != nums[li]: errs.append(f'unit {k}: ln={u.get("ln")} but it starts on line {nums[li]}')
    if bool(u.get('p')) != (atStart and nums[li] in paras): errs.append(f'unit {k} (line {nums[li]}): p should be {atStart and nums[li] in paras}')
    if not u.get('v'): errs.append(f'unit {k}: v must be true')
    for f in ('l', 'i', 'n'):
        if not (u.get(f) or '').strip(): errs.append(f'unit {k} (line {nums[li]}): missing {f}')
    if (u.get('l') or '').count('\n') != t.count('\n'): errs.append(f'unit {k} (line {nums[li]}): l must have the same number of lines as t')
    if '\n' in (u.get('i') or ''): errs.append(f'unit {k}: i must not contain line breaks')
    if t.count('\n') + 1 > 5: errs.append(f'unit {k} (line {nums[li]}): spans more than five lines')
    if t.rstrip('”—')[-1:] not in A.TERMINAL + ',' and not t.endswith('—'): errs.append(f'unit {k} (line {nums[li]}): does not end at punctuation')
    pos += len(t); li += t.count('\n')
    if pos < len(S):
        if S[pos] not in ' \n': die(f'unit {k}: ends mid-word at line {nums[li]}')
        atStart = S[pos] == '\n'; li += 1 if atStart else 0; pos += 1
if pos != len(S): die(f'edition not fully covered: stopped at line {nums[li]}')
if errs: die('\n  ' + '\n  '.join(errs))
# ---- story
first = (A.published_stories() or [None])[0]
SOURCE = ("P. Vergilius Maro, Aeneid, ed. J. B. Greenough, The Bucolics, Aeneid, and Georgics of Virgil (Boston: Ginn & Company, 1881), "
          "public domain; TEI from PerseusDL/canonical-latinLit phi0690.phi003.perseus-lat2, sha256 %s. Collated against The Latin Library "
          "(cltk mirror) as a disagreement detector only. Greenough's spelling kept (volnus, divom, Karthago, -is accusatives); his quotation "
          "marks printed as “ ”. Pronunciation convention: reconstructed Classical (restored) Latin, applied consistently. All translations "
          "were made fresh from the Latin for Lectorium." % A.source()['teiSha256'][:16])
units = []
for u in D['sentences']:
    nu = {'t': u['t'], 'l': u['l'], 'i': u['i'], 'n': u['n']}
    if u.get('p'): nu['p'] = True
    nu['v'] = True; nu['ln'] = u['ln']; units.append(nu)
story = {'id': pid, 'sourceId': pid, 'title': D['title'], 'titleEn': D['titleEn'], 'language': 'Latin', 'langCode': None,
         'source': first['source'] if first and first['id'] != pid else SOURCE, 'about': D['about'],
         'work': 'Aeneid', 'workEn': 'Aeneid (Virgil)', 'part': D['part'], 'glossaryFile': 'aeneid-glossary.json'}
if D.get('advisory'): story['advisory'] = D['advisory']
story['sentences'] = units
# ---- scansion (shared scanner); every line must fit, or the part goes to QUESTIONS.md
n_ok, n_lines, rep = SL.scan_story(story)
# hand fixes (scan-fixes.json) override the scanner line by line
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
lt = [len(A.WORD_RE.findall(l['t'])) for l in L]
flat = [x for u in units for x in u.get('sc', [''] * len(A.WORD_RE.findall(u['t'])))]
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
applied = []
for i, l in enumerate(L):
    k = f"{P['book']}.{l['n']}"
    if k in fx:
        a = sum(lt[:i]); new = fx[k]['sc']
        if [strip(x) for x in new] != A.WORD_RE.findall(l['t']): die('scan-fixes.json', k, 'does not match the words of the line')
        flat[a:a + lt[i]] = new; applied.append(k)
        rep = [r for r in rep if not (r.startswith(('COSTLY', 'UNRESOLVED')) and strip(r.split(': ', 1)[1]).split() == [strip(x) for x in A.WORD_RE.findall(l['t'])])]
if applied:
    pos = 0
    for u in units:
        n = len(A.WORD_RE.findall(u['t'])); u['sc'] = flat[pos:pos + n]; pos += n
    print('hand scansions applied:', applied)
unres = [r for r in rep if r.startswith(('UNRESOLVED', 'MISMATCH'))]
if unres and not os.environ.get('ALLOW_UNSCANNED'): die('lines the scanner cannot fit (hand-check, then QUESTIONS.md):', unres)
# ---- glossary: additions only; an existing entry may be broadened, never replaced
gp = A.glossary_path()
G = A.jload(gp) if os.path.exists(gp) else {'work': 'Aeneid', 'workEn': 'Aeneid (Virgil)', 'language': 'Latin',
     'note': "Shared glossary for every part of Virgil's Aeneid. Entries keyed by word form as printed in Greenough (Boston: Ginn & Company, 1881), lowercased, exactly as the reader's word splitter cuts it (enclitic -que/-ne/-ve stay on the word). Lemma — meaning (grammatical info); the lemma may carry macrons for vowel length, the text never does.",
     'glossary': {}}
g = G['glossary']
add = A.jload(os.path.join(A.HERE, 'drafts', pid, 'gloss.json')); broaden = add.pop('__broaden__', {})
need = {f for u in units for f in A.forms(u['t'])}
for f, e in add.items():
    if f in g and g[f] != e: die('gloss.json redefines an existing form (use __broaden__):', f)
    if f not in need: die('gloss.json has a form that is not in this part:', f)
    if not re.match(r'^\S.* — \S', e) or '`' in e or len(e) > 230: die('bad glossary entry shape:', f, '=>', e)
for f, e in broaden.items():
    if f not in g or g[f] not in e: die('__broaden__ must keep the old entry whole inside the new one:', f)
missing = sorted(need - set(g) - set(add))
if missing: die(f'{len(missing)} forms have no glossary entry:', missing[:25])
for f in add: g[f] = add[f]
for f, e in broaden.items(): g[f] = e
G['glossary'] = dict(sorted(g.items()))
# ---- manifest: grouped by book, after the previous part, like the Odyssey; library shows Latin → Aeneid (Virgil)
ROMAN = 'I II III IV V VI VII VIII IX X XI XII'.split()
M = A.jload(os.path.join(A.ROOT, 'stories.json')); st = M['stories']
st[:] = [e for e in st if e.get('id') != pid]
mine = [k for k, e in enumerate(st) if e.get('work') == 'Aeneid']
before = [k for k in mine if st[k].get('seq', 0) < P['seq']]
if before: at = max(before) + 1
elif mine: at = min(mine)
else:   # first Aeneid entry: right after the Metamorphoses, so Latin works sit together
    ov = [k for k, e in enumerate(st) if e.get('language') == 'Latin']
    at = (max(ov) + 1) if ov else len(st)
st.insert(at, {'id': pid, 'title': D['title'], 'titleEn': D['titleEn'], 'language': 'Latin', 'work': 'Aeneid', 'workEn': 'Aeneid (Virgil)',
               'part': D['part'], 'group': f'Book {ROMAN[P["book"]-1]}', 'file': P['file'], 'seq': P['seq']})
A.jdump(story, os.path.join(A.ROOT, P['file'])); A.jdump(G, gp); A.jdump(M, os.path.join(A.ROOT, 'stories.json'))
print(f'BUILT {pid}: {len(units)} units, {len(L)} lines, scansion on {n_ok} units, {len(add)} glossary forms ({len(g)} total), {len(broaden)} broadened')
print('scanner report (COSTLY fits are for the reviewer to hand-check):'); [print('  ', r) for r in rep] or print('   none')
