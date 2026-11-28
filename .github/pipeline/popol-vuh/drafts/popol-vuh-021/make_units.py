#!/usr/bin/env python3
"""Assemble units.json from cut.json (t, never retyped) + groups.py + units_src.py, and check it."""
import json, re, sys
sys.path.insert(0, '/home/user/Lectorium/.github/scripts'); sys.path.insert(0, '.')
from wordre import WORD_RE
from groups import GROUPS
from units_src import U, ABOUT
from cut import paragraphs

cut = json.load(open('cut.json', encoding='utf-8'))
assert [i for g in GROUPS for i in g] == list(range(len(cut))), 'groups must take every piece once, in order'
assert len(GROUPS) == len(U), (len(GROUPS), len(U))
sents, errs = [], []
for k, (g, u) in enumerate(zip(GROUPS, U), 1):
    if len({cut[i]['para'] for i in g}) != 1:
        errs.append(f'U{k} straddles paragraphs')
    t = ' '.join(cut[i]['t'] for i in g)
    toks = WORD_RE.findall(t)
    mt = u['mt'].split()
    if len(mt) != len(toks):
        errs.append(f'U{k}: {len(mt)} mt for {len(toks)} tokens')
        for a, b in zip(toks, mt): print('   ', a, b)
    else:  # first-letter case follows the manuscript token
        mt = [(m[0].upper() + m[1:]) if w[0].isupper() else (m[0].lower() + m[1:]) for w, m in zip(toks, mt)]
    sents.append({'t': t, 'mt': mt, 'l': u['l'], 'i': u['i'], 'n': u['n']})

# checks: tiling, paragraph starts, mt lengths
paras = paragraphs()
starts, acc = set(), 0
for p in paras:
    starts.add(acc); acc += len(re.sub(r'\s', '', p))
pos, nstart = 0, 0
for k, s in enumerate(sents, 1):
    if pos in starts: nstart += 1
    pos += len(re.sub(r'\s', '', s['t']))
want = re.sub(r'\s+', ' ', ' '.join(paras)).strip()
got = re.sub(r'\s+', ' ', ' '.join(s['t'] for s in sents)).strip()
if want != got: errs.append('units do not tile the paragraphs')
if nstart != len(paras): errs.append(f'{nstart} paragraph starts for {len(paras)} paragraphs')
for k, s in enumerate(sents, 1):
    if len(s['mt']) != len(WORD_RE.findall(s['t'])): errs.append(f'U{k} mt length')
# every paragraph's first piece begins a unit
firsts = [g[0] for g in GROUPS]
for i, c in enumerate(cut):
    if c['first_in_para'] and i not in firsts: errs.append(f'piece {i} starts paragraph {c["para"]} mid-unit')
if errs:
    print('\n'.join(errs)); sys.exit(1)
json.dump({'about': ABOUT, 'sentences': sents}, open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.load(open('units.json', encoding='utf-8'))
nw = [len(WORD_RE.findall(s['t'])) for s in sents]
print(f'OK: {len(sents)} units, {len(paras)} paragraphs, {sum(nw)} words, longest {max(nw)} (U{nw.index(max(nw))+1}); '
      f'paragraph starts at U' + ', '.join(str(firsts.index(i) + 1) for i, c in enumerate(cut) if c['first_in_para']))
