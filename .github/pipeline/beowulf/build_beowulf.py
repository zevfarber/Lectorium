#!/usr/bin/env python3
"""Assemble one Beowulf part from its draft.   usage: python3 build_beowulf.py beowulf-fitt-NN

Reads   drafts/<id>/units.json   {sentences:[{t, l, i, n, ln, v:true, p?}]}
        drafts/<id>/gloss.json   {form: "lemma — meaning (parse)"} for every form not yet in beowulf-glossary.json
                                 optional key "__broaden__": {form: new entry} — the new entry must CONTAIN the old one
Writes  <repo root>/<id>.json, <repo root>/beowulf-glossary.json (new keys appended), and the manifest entry in
        <repo root>/stories.json after the previous Beowulf part. Refuses, changing nothing, on any failure.
title, titleEn, part, source and about come from parts.json and the published parts — never from a drafter."""
import sys, os, re
import beowulf_lib as B
pid = sys.argv[1]; P = B.part(pid); L = B.lines_of(P)
def die(*a): print('BUILD REFUSED:', *a); sys.exit(1)
if B.sha(L) != P['sha256']: die('source text does not match parts.json sha256')
D = B.jload(os.path.join(B.HERE, 'drafts', pid, 'units.json'))
# ---- tiling: the units' t, joined in order, must reproduce the edition character for character
S = '\n'.join(l['t'] for l in L); nums = [l['n'] for l in L]
pos = 0; li = 0; errs = []
for k, u in enumerate(D['sentences']):
    t = u.get('t', '')
    if not t or not S.startswith(t, pos): die(f'unit {k}: t does not match the edition at line {nums[li]}: expected {S[pos:pos+60]!r}')
    if u.get('ln') != nums[li]: errs.append(f'unit {k}: ln={u.get("ln")} but it starts on line {nums[li]}')
    if not u.get('v'): errs.append(f'unit {k}: v must be true')
    for f in ('l', 'i', 'n'):
        if not (u.get(f) or '').strip(): errs.append(f'unit {k} (line {nums[li]}): missing {f}')
    if '\n' in (u.get('l') or '') + (u.get('i') or ''): errs.append(f'unit {k}: l and i are single paragraphs, no line breaks')
    if t.count('\n') + 1 > 8: errs.append(f'unit {k} (line {nums[li]}): spans more than eight lines')
    if t.rstrip()[-1] not in B.TERMINAL: errs.append(f'unit {k} (line {nums[li]}): does not end at punctuation')
    pos += len(t); li += t.count('\n')
    if pos < len(S):
        if S[pos] not in ' \n': die(f'unit {k}: ends mid-word at line {nums[li]}')
        li += 1 if S[pos] == '\n' else 0; pos += 1
if pos != len(S): die(f'edition not fully covered: stopped at line {nums[li]}')
if errs: die('\n  ' + '\n  '.join(errs))
units = []
for k, u in enumerate(D['sentences']):
    nu = {}
    if k == 0 or u.get('p'): nu['p'] = True
    nu.update({'v': True, 'ln': u['ln'], 't': u['t'], 'l': u['l'], 'i': u['i'], 'n': u['n']})
    units.append(nu)
# ---- glossary: additions only; an existing entry may be broadened, never replaced
G = B.glossary(); g = G['glossary']
add = B.jload(os.path.join(B.HERE, 'drafts', pid, 'gloss.json')); broaden = add.pop('__broaden__', {})
need = {f for u in units for f in B.forms(u['t'])}
for f, e in add.items():
    if f in g: die('gloss.json redefines an existing form (use __broaden__):', f)
    if f not in need: die('gloss.json has a form that is not in this part:', f)
    if not re.match(r'^\S.* — \S', e) or '`' in e or len(e) > 260: die('bad glossary entry shape:', f, '=>', e)
for f, e in broaden.items():
    if f not in g or g[f] not in e: die('__broaden__ must keep the old entry whole inside the new one:', f)
missing = sorted(need - set(g) - set(add))
if missing: die(f'{len(missing)} forms have no glossary entry:', missing[:25])
for f in add: g[f] = add[f]
for f, e in broaden.items(): g[f] = e
# ---- story, manifest
first = B.jload(os.path.join(B.ROOT, 'beowulf-fitt-02.json'))
story = {'id': pid, 'title': first['title'], 'titleEn': P['titleEn'], 'language': 'Old English', 'langCode': None,
         'work': first['work'], 'workEn': first['workEn'], 'part': P['part'], 'source': B.source_statement(P),
         'about': first['about'], 'glossaryFile': 'beowulf-glossary.json', 'sentences': units}
M = B.jload(os.path.join(B.ROOT, 'stories.json')); st = M['stories']
st[:] = [e for e in st if e.get('id') != pid]
order = [p['id'] for p in B.parts()['parts']]
before = set(order[:order.index(pid)])
prev = max([k for k, e in enumerate(st) if e.get('id') in before], default=len(st) - 1)
st.insert(prev + 1, {'id': pid, 'title': first['title'], 'titleEn': P['titleEn'], 'language': 'Old English',
                     'work': first['work'], 'workEn': first['workEn'], 'part': P['part'], 'file': P['file']})
B.jdump(story, os.path.join(B.ROOT, P['file'])); B.jdump(G, B.glossary_path()); B.jdump(M, os.path.join(B.ROOT, 'stories.json'))
print(f'BUILT {pid}: {len(units)} units, {len(L)} lines, {len(add)} new glossary forms ({len(g)} total), {len(broaden)} broadened')
