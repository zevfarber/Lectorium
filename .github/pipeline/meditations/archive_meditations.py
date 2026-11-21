#!/usr/bin/env python3
"""Build source/meditations-leopold1908.json and parts.json from the Perseus TEI of Leopold's Marcus Aurelius
(1908; the TEI file is kept in source/). Run once, in setup (2026-11-21), modelled on ../hesiod/archive_hesiod.py.

The archive is a list of chapters {b, c, blocks:[{t, v?, sub?}]}. A block is a stretch the drafter's units must
tile without crossing: the chapter's prose (Perseus's sections joined by a space), a verse quotation Leopold sets
as verse (v: true; its lines joined by \n), or a book's closing subscription (sub: true).
Normalised, and nothing else: elision marks (ʼ ᾽ ' and the combining comma above after a consonant) -> U+2019;
Leopold's quotation marks ʽ…ʼ -> ‘…’; NFC; tags stripped; <add> (editor's supplement) in ⟨ ⟩; <del> (editor's
deletion) in [ ]; † kept; at 7.51 the colon from Euripides divided mid-word 'τ|λῆναι' is moved to fall between words."""
import re, json, hashlib, unicodedata, os
HERE = os.path.dirname(os.path.abspath(__file__))
TEI = os.path.join(HERE, 'source', 'tlg0562.tlg001.perseus-grc2.xml')
TARGET, MAXW, MINW = 800, 1150, 450
x = open(TEI, encoding='utf8').read()
teisha = hashlib.sha256(x.encode('utf8')).hexdigest()
body = x[x.find('<body'):]
odd = []

def norm(s):
    s = s.replace('τ<lb/>λῆναι', '<lb/>τλῆναι')
    s = re.sub(r'<add>(.*?)</add>', r'⟨\1⟩', s, flags=re.S)
    s = re.sub(r'<del>(.*?)</del>', r'[\1]', s, flags=re.S)
    s = s.replace('<lb/>', '\x01')
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('ʽ', '‘').replace('ʼ', '’').replace('᾽', '’').replace("'", '’')
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'(?<=[^\W\d_])̓', '’', s)      # φ̓ -> φ’ (combining comma above used as an elision mark)
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[ \t\r\n]+', ' ', s)
    return s

chapters = []
for bm in re.finditer(r'<div type="textpart" subtype="book"[^>]*n="(\d+)">(.*?)(?=<div type="textpart" subtype="book"|</body>)', body, re.S):
    b = int(bm.group(1))
    for cm in re.finditer(r'<div type="textpart" subtype="chapter"[^>]*n="(\d+)">(.*?)(?=<div type="textpart" subtype="chapter"|$)', bm.group(2), re.S):
        c = int(cm.group(1)); blocks = []; prose = []
        def flush():
            if prose:
                t = ' '.join(p.strip() for p in prose if p.strip()).strip()
                if t: blocks.append({'t': t})
                prose.clear()
        for pm in re.finditer(r'<p\b([^>]*)>(.*?)</p>', cm.group(2), re.S):
            attrs, raw = pm.group(1), pm.group(2)
            if 'rend="center"' in attrs:
                flush(); blocks.append({'t': norm(raw).strip(), 'sub': True}); continue
            # verse quotations: <quote rend="blockquote"> inside the paragraph, or a whole paragraph set in lines
            pieces = re.split(r'(<quote\b[^>]*>.*?</quote>)', raw, flags=re.S)
            if len(pieces) == 1 and '<lb/>' in raw: pieces = ['', '<quote>' + raw + '</quote>', '']
            for k, piece in enumerate(pieces):
                if piece.startswith('<quote'):
                    flush()
                    t = norm(re.sub(r'^<quote\b[^>]*>|</quote>$', '', piece))
                    t = '\n'.join(l.strip() for l in t.split('\x01'))
                    blocks.append({'t': t.strip(), 'v': True})
                else:
                    t = norm(piece).replace('\x01', ' ')
                    if t.strip(): prose.append(t)
        flush()
        chapters.append({'b': b, 'c': c, 'blocks': blocks})

def words(ch): return sum(len(re.findall(r'[A-Za-zΆΈ-Ͽἀ-῿]+', bl['t'])) for bl in ch['blocks'])
for ch in chapters:
    ch['w'] = words(ch)
    for bl in ch['blocks']:
        if re.search(r'[<>&]|\x01', bl['t']): odd.append(f'{ch["b"]}.{ch["c"]}: leftover markup {bl["t"][:40]!r}')
    if not ch['blocks']: odd.append(f'{ch["b"]}.{ch["c"]}: empty')
src = {'edition': 'J. H. Leopold, M. Antoninus Imperator Ad se ipsum (1908), Greek text',
       'tei': 'PerseusDL/canonical-greekLit data/tlg0562/tlg001/tlg0562.tlg001.perseus-grc2.xml', 'teiSha256': teisha,
       'normalised': "elision marks -> U+2019; Leopold's ʽ…ʼ -> ‘…’; NFC; tags stripped; <add> in ⟨ ⟩; <del> in [ ]; † kept; verse quotations as lines; the colon break inside τλῆναι moved to fall before the word; nothing else",
       'chapters': [{k: v for k, v in ch.items() if k != 'w'} for ch in chapters]}
json.dump(src, open(os.path.join(HERE, 'source', 'meditations-leopold1908.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))

def sha(chs): return hashlib.sha256(json.dumps([ch['blocks'] for ch in chs], ensure_ascii=False).encode('utf8')).hexdigest()
parts = []; pid = 0
for b in range(1, 13):
    C = [i for i, ch in enumerate(chapters) if ch['b'] == b]
    W = [chapters[i]['w'] for i in C]; n = len(C)
    INF = 1e18; best = {0: (0, None)}     # best[k]: cost of cutting the first k chapters of the book
    for e in range(1, n + 1):
        cand = (INF, None)
        for s in range(0, e):
            if s not in best: continue
            w = sum(W[s:e])
            pen = (w - TARGET) ** 2 * (40 if (w > MAXW and e - s > 1) else (4 if w < MINW else 1))
            if best[s][0] + pen < cand[0]: cand = (best[s][0] + pen, s)
        best[e] = cand
    cuts = []; e = n
    while e: cuts.append(e); e = best[e][1]
    s = 0
    for e in sorted(cuts):
        seg = [chapters[i] for i in C[s:e]]; pid += 1
        a, z = seg[0]['c'], seg[-1]['c']
        parts.append({'id': f'meditations-{pid:03d}', 'seq': pid, 'book': b, 'fromCh': a, 'toCh': z,
                      'chapters': len(seg), 'words': sum(ch['w'] for ch in seg),
                      'cite': f'{b}.{a}' + (f'–{z}' if z != a else ''), 'file': f'meditations-{pid:03d}.json',
                      'sha256': sha(seg), 'status': 'todo'})
        s = e
json.dump({'work': 'Marcus Aurelius, Meditations', 'source': 'source/meditations-leopold1908.json',
           'cutRule': 'parts end only at the end of a chapter and never cross a book; target ~800 Greek words',
           'parts': parts}, open(os.path.join(HERE, 'parts.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
import statistics as st
ws = [p['words'] for p in parts]
print('chapters', len(chapters), 'words', sum(ch['w'] for ch in chapters))
print('parts', len(parts), 'min/median/max words', min(ws), st.median(ws), max(ws))
for p in parts: print(p['id'], p['cite'], p['chapters'], p['words'])
print('verse blocks', sum(1 for ch in chapters for bl in ch['blocks'] if bl.get('v')), 'subscriptions', sum(1 for ch in chapters for bl in ch['blocks'] if bl.get('sub')))
print('oddities', odd)
