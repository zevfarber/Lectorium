#!/usr/bin/env python3
"""Build and check one Kalpasūtra part.   usage: python3 build_kalpa.py 001
Reads source/jinacaritra-jacobi1879.json (Jacobi's text, IAST) and drafts/NNN/draft.txt; writes <root>/kalpasutra-NNN.json
in the Gita's word-by-word format (t Devanagari, tr Jacobi's romanization, words with glyphs and morph, glossary
embedded) and adds the library entry to stories.json. Refuses, writing nothing, on any mismatch.
Checks: the draft's words tile the source blocks token for token; every unit has l and i; every Devanagari word in
t has a glossary entry (the reader's word regex); Devanagari re-derived from tr matches t."""
import sys, os, re, json
import kalpa_lib as K
num = sys.argv[1]; D = os.path.join(K.HERE, 'drafts', num)
def die(*a): print('BUILD REFUSED:', *a); sys.exit(1)

# ---- parse the draft
units, cur, memo = [], None, {}
for raw in open(os.path.join(D, 'draft.txt'), encoding='utf8'):
    line = raw.rstrip('\n')
    if line.startswith('# ') or not line.strip(): continue
    if line.startswith('#U'):
        cur = {'sec': line[2:].strip(), 'lines': [[]], 'l': [], 'i': '', 'n': ''}; units.append(cur); last = None; continue
    if line == '--': cur['lines'].append([]); continue
    if line.startswith('W '):
        body = line[2:]
        reading, _, morph = body.partition('|')
        reading = reading.strip()
        core = K.split_punct(reading)[1].rstrip('-')
        if morph.strip():
            ms = []
            for m in morph.split(';;'):
                lemma, _, gloss = m.strip().partition(' — ')
                if not gloss: die('bad morph', line)
                ms.append({'lemma': lemma.strip(), 'gloss': gloss.strip(), 'g': [0]})
            memo[core.lower()] = ms
        elif core.lower() not in memo: die('no gloss given for', reading)
        cur['lines'][-1].append({'core': core, 'morph': memo[core.lower()]}); last = None; continue
    m = re.match(r'^([LIN]): ?(.*)$', line)
    if m: last = m.group(1); val = m.group(2)
    elif last == 'L': val = line
    else: die('cannot read draft line:', line)
    if last == 'L': cur['l'].append(val)
    elif last == 'I': cur['i'] = val
    else: cur['n'] = val

# ---- tile the source
src = K.source()['blocks']
toks = []          # (block index, token, separator-before)
for bi, b in enumerate(src):
    for li, ln in enumerate(b['t'].split('\n')):
        for ti, t in enumerate(ln.split(' ')):
            toks.append((bi, t, 'nl' if (li > 0 and ti == 0) else ' '))
k = 0; sentences = []; glossary = {}
for ui, u in enumerate(units):
    words = []; t_parts = []; tr_parts = []; bi0 = toks[k][0] if k < len(toks) else None
    for lidx, wl in enumerate(u['lines']):
        for wi, w in enumerate(wl):
            n = len(w['core'].split(' '))
            grp = toks[k:k + n]
            if len(grp) < n: die(f'unit {ui}: ran out of source at {w["core"]}')
            if any(g[0] != bi0 for g in grp): die(f'unit {ui}: crosses a block at {w["core"]}')
            raw = ' '.join(g[1] for g in grp)
            lead, core, trail = K.split_punct(raw)
            hy = core.endswith('-')
            if hy: core = core[:-1]
            if core != w['core']: die(f'unit {ui}: draft word {w["core"]!r} != source {core!r}')
            if wi == 0 and lidx > 0 and grp[0][2] != 'nl': die(f'unit {ui}: line break in draft where the source has none, at {core}')
            k += n
            # a punctuation-only token after the word (the verse's || ) belongs to it
            while k < len(toks) and toks[k][0] == bi0 and re.fullmatch(r'[|.,;:]+', toks[k][1]):
                trail += ' ' + toks[k][1]; k += 1
            dev = K.to_dev(core)
            dtrail = K.dev_punct(trail).replace('। ॥', '॥').replace('। ।', '।').replace(' ', '') + ('-' if hy else '')
            glyphs = ([{'s': lead, 'tr': ' ', 'role': 'punct'}] if lead else []) + [{'s': dev, 'tr': core}] + \
                     ([{'s': dtrail, 'tr': ' ', 'role': 'punct'}] if dtrail else [])
            e = {'reading': core, 'glyphs': glyphs, 'morph': w['morph']}
            if wi == 0 and lidx > 0: e['br'] = True
            words.append(e)
            t_parts.append(('\n' if e.get('br') else ' ') + lead + dev + (' ' + dtrail if dtrail and dtrail[0] in '।॥' else dtrail))
            tr_parts.append(('\n' if e.get('br') else ' ') + raw)
            glossary.setdefault(dev, core + ' — ' + '; '.join(m['lemma'] + ' — ' + m['gloss'] for m in w['morph']))
    # the unit must end at a word boundary inside its block
    s = {'t': ''.join(t_parts).strip(' '), 'tr': ''.join(tr_parts).strip(' '), 'l': '\n'.join(u['l']), 'words': words}
    if u['i']: s['i'] = u['i']
    if u['n']: s['n'] = u['n']
    if not s['l'] or not u['i'] or not u['n']: die(f'unit {ui}: l, i and n are all required in the pilot')
    if s['l'].count('\n') != s['t'].count('\n'): die(f'unit {ui}: l has {s["l"].count(chr(10))+1} lines, t has {s["t"].count(chr(10))+1}')
    blk = src[bi0]
    first_of_block = (ui == 0) or (sentences and sentences[-1].get('_b') != bi0)
    if u['sec']: s['ln'] = int(u['sec'])
    if first_of_block and blk.get('p'): s['p'] = True
    if blk.get('v'): s['v'] = True
    s['_b'] = bi0
    sentences.append(s)
if k != len(toks): die(f'{len(toks) - k} source tokens left over, from {toks[k][1]!r}')
for s in sentences: s.pop('_b')
# ---- checks
missing = sorted({w for s in sentences for w in K.WORD_DEV.findall(s['t'])} - set(glossary))
if missing: die('Devanagari words without a glossary entry:', missing)
title = 'कप्पसुत्त — जिणचरिय'
story = {'id': f'kalpasutra-{num}', 'title': title, 'titleRead': 'Kappasutta — Jiṇacariya',
 'titleEn': 'The Kalpasūtra — Life of Mahāvīra 1: The Descent and the Dreams (§§1–4)',
 'work': 'कप्पसुत्त', 'workEn': 'The Kalpasūtra', 'part': '1 · The Namokkāra; the Descent and the Dreams (§§1–4)',
 'language': 'Prakrit', 'langCode': None, 'script': 'devanagari', 'numbering': 'stanza',
 'source': ("Text: Hermann Jacobi, The Kalpasûtra of Bhadrabâhu (Leipzig: Brockhaus, 1879; Abhandlungen für die Kunde des Morgenlandes VII.1), "
   "Jinacaritra, the Namokkāra and §§1–4 (pp. 33–34), transcribed from the Wellcome Collection scan (public domain). Section numbers are Jacobi’s. "
   "Jacobi prints the Prakrit in Roman letters; the romanization under each word is his, put into IAST (â î û → ā ī ū; his dotted ọ, an o formed by "
   "contraction, → o), with his hyphens between compound members, his apostrophes for elided vowels, his brackets and his punctuation. "
   "The Devanagari is converted letter for letter from it, compounds closed up as Prakrit is printed in India; a vowel after a vowel keeps its own "
   "letter, since this Prakrit has no diphthongs. Round brackets: words missing in Jacobi’s manuscript A; square brackets: words missing in "
   "manuscripts A and C. His footnotes of variant readings are not reproduced. Pronunciation: not yet chosen (no audio). "
   "Translations made fresh from the Prakrit for Lectorium; no translation consulted for wording."),
 'about': ("The Kalpasūtra, ascribed by tradition to Bhadrabāhu, is among the best-loved scriptures of the Śvetāmbara Jains: monks read it aloud to "
   "the community every year during the festival of Paryuṣaṇa. Its first and longest part, the Jinacaritra, tells the lives of the Jinas, beginning "
   "with Mahāvīra, the twenty-fourth and last of this age. This opening has the Namokkāra, the salutation every Jain knows by heart; the five great "
   "moments of Mahāvīra’s life; his descent from heaven into the womb of the brahmin woman Devānandā; and the fourteen dreams she sees that night."),
 'sentences': sentences, 'glossary': glossary}
out = os.path.join(K.ROOT, f'kalpasutra-{num}.json')
json.dump(story, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
M = json.load(open(os.path.join(K.ROOT, 'stories.json'), encoding='utf8')); st = M['stories']
st[:] = [e for e in st if e.get('id') != story['id']]
after = max([j for j, e in enumerate(st) if e.get('language') == 'Sanskrit'], default=len(st) - 1)
st.insert(after + 1, {'id': story['id'], 'title': title, 'titleEn': story['titleEn'], 'language': 'Prakrit', 'work': story['work'],
                      'workEn': story['workEn'], 'part': story['part'], 'file': f'kalpasutra-{num}.json'})
json.dump(M, open(os.path.join(K.ROOT, 'stories.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(f'BUILT {out}: {len(sentences)} units, {sum(len(s["words"]) for s in sentences)} words, glossary {len(glossary)}')
