#!/usr/bin/env python3
"""Build source/hesiod-evelyn-white1914.json and parts.json from the Perseus TEI of Evelyn-White's Hesiod
(Loeb, 1914; the TEI files are kept in source/). Run once, in setup (2026-11-20), modelled on ../iliad/archive_iliad.py.
Books: 'Th' = Theogony (tlg001), 'WD' = Works and Days (tlg002).
Normalised, and nothing else: elision mark -> U+2019; NFC; tags stripped; lines the edition brackets (<del>) kept inside
[ ]; Theogony 929a-t, the passage Evelyn-White prints from Chrysippus (via Galen) after 929 (TEI <add>), kept inside
⟨ ⟩ with their labels, numbered 929; the ellipsis (<gap>) inside it recorded, not printed. Paragraphs: rend="align(indent)"."""
import re, json, hashlib, unicodedata, os
HERE = os.path.dirname(os.path.abspath(__file__))
TARGET, MAXLEN, MINLEN = 100, 135, 55
books, shas, odd = {}, {}, []
for key, f in (('Th', 'tlg001'), ('WD', 'tlg002')):
    x = open(os.path.join(HERE, 'source', f'tlg0020.{f}.perseus-grc2.xml'), encoding='utf8').read()
    shas[key] = hashlib.sha256(x.encode('utf8')).hexdigest()
    body = x[x.find('<body'):]
    lines = []
    for m in re.finditer(r'<gap\b[^>]*/>|<l\b([^>]*)>(.*?)</l>', body, re.S):
        if m.group(0).startswith('<gap'):
            odd.append(f'{key}: ellipsis after {lines[-1].get("label", lines[-1]["n"])} (not printed)'); continue
        attrs, raw = m.group(1), m.group(2)
        n = re.search(r'\bn="([^"]+)"', attrs).group(1)
        bracket = '<del>' in raw; added = '<add>' in raw
        t = re.sub(r'<[^>]+>', '', raw); t = re.sub(r'\s+', ' ', t).strip()
        t = unicodedata.normalize('NFC', t.replace('ʼ', '’').replace('᾽', '’').replace("'", '’'))
        if bracket: t = '[' + t + ']'
        if added: t = '⟨' + t + '⟩'
        rec = {'n': int(re.match(r'\d+', n).group(0)), 't': t, 'p': 'align(indent)' in attrs or not lines}
        if not n.isdigit(): rec['label'] = n
        lines.append(rec)
    for a, b in zip(lines, lines[1:]):
        if b['n'] != a['n'] + 1 and not b.get('label') and not a.get('label'): odd.append(f'{key}: numbering jumps {a["n"]} -> {b["n"]}')
    books[key] = lines
src = {'edition': 'H. G. Evelyn-White, Hesiod, the Homeric Hymns and Homerica (Loeb Classical Library; London: Heinemann / New York: Macmillan, 1914), Greek text',
       'tei': {'Th': 'PerseusDL/canonical-greekLit data/tlg0020/tlg001/tlg0020.tlg001.perseus-grc2.xml',
               'WD': 'PerseusDL/canonical-greekLit data/tlg0020/tlg002/tlg0020.tlg002.perseus-grc2.xml'},
       'teiSha256': shas,
       'normalised': 'elision mark -> U+2019; NFC; tags stripped; <del> lines in [ ]; Th. 929a-t (<add>) in ⟨ ⟩ with labels; nothing else',
       'books': books}
json.dump(src, open(os.path.join(HERE, 'source', 'hesiod-evelyn-white1914.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
def sha(ls): return hashlib.sha256('\n'.join(l['t'] for l in ls).encode('utf8')).hexdigest()
parts = []; pid = 0
for key in ('Th', 'WD'):
    L = books[key]; idx = list(range(len(L)))
    # cut points are line INDEXES (labelled lines share numbers); a part ends before a paragraph start
    starts = [i for i in idx if L[i]['p']]
    ends = sorted({s - 1 for s in starts if s > 0} | {len(L) - 1})
    ends = [e for e in ends if not (L[e].get('label') and e + 1 < len(L) and L[e + 1].get('label'))]
    INF = 1e18; best = {-1: (0, None)}
    for e in ends:
        cand = (INF, None)
        for s in sorted(best):
            if s >= e: continue
            Ln = e - s
            pen = (Ln - TARGET) ** 2 * 50 if (Ln > MAXLEN and any(s < q < e for q in ends)) else (Ln - TARGET) ** 2 * (4 if Ln < MINLEN else 1)
            if best[s][0] + pen < cand[0]: cand = (best[s][0] + pen, s)
        best[e] = cand
    cuts = []; e = len(L) - 1
    while e is not None and e >= 0: cuts.append(e); e = best[e][1]
    s = 0
    for e in sorted(c for c in cuts if c >= 0):
        pid += 1; seg = L[s:e + 1]
        lab = lambda r: r.get('label', str(r['n']))
        parts.append({'id': f'hesiod-{pid:03d}', 'seq': pid, 'book': key, 'work': 'Theogony' if key == 'Th' else 'Works and Days',
                      'from': seg[0]['n'], 'to': seg[-1]['n'], 'fromIdx': s, 'toIdx': e, 'lines': len(seg),
                      'cite': f'{"Th." if key == "Th" else "WD"} {lab(seg[0])}–{lab(seg[-1])}', 'file': f'hesiod-{pid:03d}.json',
                      'sha256': sha(seg), 'status': 'todo'})
        s = e + 1
json.dump({'work': 'Hesiod', 'source': 'source/hesiod-evelyn-white1914.json',
           'cutRule': "parts end only where Evelyn-White begins a paragraph; target ~100 lines; the Theogony, then the Works and Days",
           'parts': parts}, open(os.path.join(HERE, 'parts.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
import statistics as st
Ls = [p['lines'] for p in parts]
print('parts', len(parts), 'min/median/max', min(Ls), st.median(Ls), max(Ls)); [print(p['id'], p['cite'], p['lines']) for p in parts]
print('oddities', odd); print({k: len(v) for k, v in books.items()})
