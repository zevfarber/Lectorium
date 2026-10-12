#!/usr/bin/env python3
"""One-off: cut the Kebra Nagast (chapters 2-117 + colophon; chapter 1 is the published pilot) into parts of
roughly 300-600 words. Consecutive short chapters are grouped; a chapter over 650 words is cut at the
sentence end (።) nearest an equal division. Writes ../parts.json (statuses todo; sha256 of each slice)."""
import json, os, re, hashlib, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import hooks as H
src = json.load(open(os.path.join(HERE, 'kebra-nagast-bezold1905.json'), encoding='utf-8'))
W = lambda s: len(re.findall(r'[ሀ-ፚ፩-፼]+', s))
groups = []; cur = []; cw = 0
for c in src['chapters'][1:]:
    w = c['words']
    if w > 650:
        if cur: groups.append(cur); cur = []; cw = 0
        txt = '\n'.join(c['paragraphs'])
        k = max(2, round(w / 450))
        ends = [m.end() for m in re.finditer('።', txt)]
        cuts = []
        for j in range(1, k):
            goal = len(txt) * j / k
            cuts.append(min(ends, key=lambda e: abs(e - goal)))
        bounds = [0] + cuts + [len(txt)]
        for j in range(k):
            a, b = bounds[j], bounds[j + 1]
            while b < len(txt) and txt[b] in ' \n': b += 1      # the space after the cut belongs to neither
            groups.append([{'n': c['n'], 'span': [a, bounds[j + 1]], 'piece': j + 1, 'of': k}])
        continue
    if cur and (cw + w > 560 or (w >= 200 and cw >= 300)):
        groups.append(cur); cur = []; cw = 0
    cur.append({'n': c['n']}); cw += w
if cur: groups.append(cur)
# fold a lone short chapter (< 200 words) into the previous group of whole chapters
out = []
for g in groups:
    gw = sum(src['chapters'][x['n'] - 1]['words'] for x in g) if 'span' not in g[0] else None
    if out and gw is not None and gw < 200 and 'span' not in out[-1][0] and \
            sum(src['chapters'][x['n'] - 1]['words'] for x in out[-1]) + gw <= 650:
        out[-1] += g
    else:
        out.append(g)
parts = []
for i, g in enumerate(out):
    if 'span' in g[0]:
        n = g[0]['n']; pid = f'kebra-nagast-ch{n}{"abcd"[g[0]["piece"] - 1]}'
        cite = f'ch. {n}, part {g[0]["piece"]} of {g[0]["of"]}'
        chs = [{'n': n, 'span': g[0]['span']}]
    else:
        ns = [x['n'] for x in g]
        lab = lambda n: 'colophon' if n == 118 else str(n)
        pid = 'kebra-nagast-' + ('colophon' if ns == [118] else f'ch{ns[0]}' + (f'-{ns[-1]}' if len(ns) > 1 else ''))
        cite = ('the colophon' if ns == [118] else f'ch. {ns[0]}' + (f'–{ns[-1]}' if len(ns) > 1 else ''))
        chs = [{'n': n} for n in ns]
    p = {'id': pid, 'seq': i + 2, 'chapters': chs, 'cite': cite, 'name': '', 'file': pid + '.json', 'status': 'todo'}
    p['words'] = W(H.slice_source(p))
    p['sha256'] = hashlib.sha256(H.slice_source(p).encode()).hexdigest()
    parts.append(p)
doc = {'work': 'Kebra Nagast', 'source': 'source/kebra-nagast-bezold1905.json',
       'cutRule': 'chapters 2–117 and the colophon; short chapters grouped to ~300–600 words; a chapter over 650 words cut at the ። nearest an equal division. Chapter 1 is the published pilot (kebra-nagast-ch1).',
       'parts': parts}
json.dump(doc, open(os.path.join(os.path.dirname(HERE), 'parts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(parts), 'parts;', min(p['words'] for p in parts), '-', max(p['words'] for p in parts), 'words')
