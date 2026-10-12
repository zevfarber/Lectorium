#!/usr/bin/env python3
"""Build source/aeneid-greenough.json and parts.json from the Perseus TEI of Greenough's Virgil.
usage: python3 -I archive_aeneid.py path/to/phi0690.phi003.perseus-lat2.xml [path/to/latin-library-dir]
Run once (2026-10-12, pilot). Kept so the archive can be re-derived and checked; a run never needs it.

Edition: P. Vergili Maronis Aeneis, in J. B. Greenough, The Bucolics, Aeneid, and Georgics of Virgil
(Boston: Ginn & Company, 1881 — the date both the TEI header and the CTS catalogue give).
Public domain everywhere. Hirtzel (Oxford 1900), the plan's first choice, has no reachable machine-readable copy.

What is normalised, and nothing else:
  - tags stripped; whitespace collapsed;
  - speech: Perseus encodes Greenough's printed quotation marks as <q> (a speech's first line is <q>,
    its continuation lines <q rend="merge">). We print “ before the first <q> of a speech and ” after
    the last line of it (the line whose successor does not continue it with a merge <q>), so the text
    shows the speech marks the printed page shows, as Magnus's Ovid does.
  - <del> lines (lines Greenough brackets as spurious) are kept, wrapped in [ ], and listed in
    `bracketed`; none falls in the pilot.
  - the Perseus <note> at 3.250 is dropped (it is Perseus's, not Greenough's).
Paragraphs: a line with rend="indent" begins a printed paragraph (Perseus's `card` milestones are
display chunks, not the edition's paragraphs; they are recorded but not used).
"""
import re, json, sys, hashlib, os, difflib
TARGET, MAXLEN, MINLEN = 100, 135, 55
PIN = {1: [101]}                       # the pilot is 1.1-101; never re-cut it
ROMAN = 'I II III IV V VI VII VIII IX X XI XII'.split()
x = open(sys.argv[1], encoding='utf8').read()
teisha = hashlib.sha256(x.encode('utf8')).hexdigest()
body = x[x.find('<body'):]
chunks = re.split(r'<div n="\d+" type="textpart" subtype="book">', body)[1:]
assert len(chunks) == 12, len(chunks)
books, odd, bracketed = [], [], []
for bi, ch in enumerate(chunks, 1):
    raw = [(m.group(1), m.group(2)) for m in re.finditer(r'<l\b([^>]*)>(.*?)</l>', ch, re.S)]
    lines = []
    for k, (attrs, t) in enumerate(raw):
        n = re.search(r'n="([^"]+)"', attrs).group(1)
        t = re.sub(r'<note\b.*?</note>', '', t, flags=re.S)
        opens = bool(re.search(r'<q(?![^>]*merge)[^>]*>', t))
        has_q = '<q' in t
        nxt = raw[k + 1][1] if k + 1 < len(raw) else ''
        cont_next = bool(re.match(r'\s*(<del>)?\s*<q rend="merge">', nxt))
        dele = '<del>' in t
        s = re.sub(r'<[^>]+>', '', t)
        s = re.sub(r'\s+', ' ', s).strip()
        if has_q and opens:
            # the opening mark goes where the <q> opens
            pre = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t[:t.find('<q')])).lstrip()
            s = pre + '“' + s[len(pre):].lstrip() if pre and s.startswith(pre) else ('“' + s if not pre else s)
            if pre and not s.startswith(pre): odd.append(f'{bi}.{n}: could not place opening quote')
        if has_q and not cont_next:
            m = re.search(r'</q>([^<]*)$', t)          # punctuation printed after the </q>
            tail = re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''
            if tail and s.endswith(tail): s = s[:len(s) - len(tail)] + '”' + tail
            else: s = s + '”'
        if dele: s = '[' + s + ']'; bracketed.append(f'{bi}.{n}')
        rec = {'n': int(re.match(r'\d+', n).group(0)), 't': s, 'p': 'rend="indent"' in attrs or not lines}
        if not n.isdigit(): rec['label'] = n; odd.append(f'{bi}: line {n!r} kept, numbered {rec["n"]} with label {n!r}')
        lines.append(rec)
    for a, b in zip(lines, lines[1:]):
        if b['n'] != a['n'] + 1 and not b.get('label'): odd.append(f'{bi}: numbering jumps {a["n"]} -> {b["n"]}')
    books.append(lines)
src = {'edition': 'P. Vergili Maronis Aeneis, ed. J. B. Greenough, The Bucolics, Aeneid, and Georgics of Virgil (Boston: Ginn & Company, 1881; TEI header date)',
       'tei': 'PerseusDL/canonical-latinLit data/phi0690/phi003/phi0690.phi003.perseus-lat2.xml', 'teiSha256': teisha,
       'normalised': 'tags stripped, whitespace collapsed; <q> speech markup printed as “ ”; <del> lines kept in [ ]; Perseus note at 3.250 dropped; nothing else',
       'bracketed': bracketed, 'books': {str(i + 1): b for i, b in enumerate(books)}}
here = os.path.dirname(os.path.abspath(__file__))
json.dump(src, open(os.path.join(here, 'source', 'aeneid-greenough.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
def sha(ls): return hashlib.sha256('\n'.join(l['t'] for l in ls).encode('utf8')).hexdigest()
parts = []; pid = 0
for bi, lines in enumerate(books, 1):
    first, last = lines[0]['n'], lines[-1]['n']
    ends = sorted({l['n'] - 1 for l in lines if l['p'] and l['n'] > first} | {last})
    pins = PIN.get(bi, [])
    for e in pins: assert e in ends, (bi, e)
    INF = 1e18; best = {first - 1: (0, None)}
    for e in ends:
        cand = (INF, None)
        for s in sorted(best):
            if s >= e or any(s < p < e for p in pins): continue
            L = e - s
            pen = (L - TARGET) ** 2 * 50 if (L > MAXLEN and any(s < q < e for q in ends)) else (L - TARGET) ** 2 * (4 if L < MINLEN else 1)
            if best[s][0] + pen < cand[0]: cand = (best[s][0] + pen, s)
        best[e] = cand
    cuts = []; e = last
    while e is not None and e >= first: cuts.append(e); e = best[e][1]
    s = first
    for e in sorted(c for c in cuts if c >= first):
        pid += 1; seg = [l for l in lines if s <= l['n'] <= e]
        parts.append({'id': f'aeneid-{pid:03d}', 'seq': pid, 'book': bi, 'from': s, 'to': e, 'lines': len(seg),
                      'cite': f'{ROMAN[bi-1]}.{s}–{e}', 'file': f'aeneid-{pid:03d}.json', 'sha256': sha(seg), 'status': 'todo'})
        s = e + 1
parts[0]['status'] = 'published'
json.dump({'work': 'Aeneid', 'source': 'source/aeneid-greenough.json',
           'cutRule': 'parts end only where Greenough begins a paragraph (indented line); target ~100 lines; aeneid-001 (I.1-101) pinned',
           'parts': parts}, open(os.path.join(here, 'parts.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
import statistics as st
L = [p['lines'] for p in parts]
print('lines', sum(len(b) for b in books), 'paragraphs', sum(l['p'] for b in books for l in b), 'parts', len(parts), 'min/median/max', min(L), st.median(L), max(L))
print('bracketed', len(bracketed)); print('oddities', len(odd)); [print('  ', o) for o in odd[:30]]
# witness B: The Latin Library (cltk mirror), a disagreement detector only; never contributes a character
if len(sys.argv) > 2:
    W = re.compile(r"[A-Za-zëïöü]+"); out = {}
    for bi, lines in enumerate(books, 1):
        fn = os.path.join(sys.argv[2], f'aen{bi}.txt')
        if not os.path.exists(fn): continue
        tl = [w for ln in open(fn, encoding='utf8', errors='replace').read().split('\n')[1:]
              if re.search(r'[a-z]{2}', ln) and 'Latin Library' not in ln and 'Classics Page' not in ln and 'AENEIDOS' not in ln and not ln.strip().startswith('Vergil:')
              for w in W.findall(ln)]
        pw, pl = [], []
        for l in lines:
            for w in W.findall(l['t']): pw.append(w); pl.append(l['n'])
        uv = lambda w: w.lower().replace('v', 'u').replace('j', 'i')   # witness B prints u for v in Books 2-12: orthography, not a reading
        tl = [w for w in tl if w not in ('Vergil', 'The', 'Latin', 'Library', 'Classics', 'Page')]
        sm = difflib.SequenceMatcher(None, [uv(w) for w in pw], [uv(w) for w in tl], autojunk=False)
        out[str(bi)] = [{'line': pl[min(i1, len(pl) - 1)], 'greenough': ' '.join(pw[i1:i2]), 'latinLibrary': ' '.join(tl[j1:j2])}
                        for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != 'equal']
    json.dump(out, open(os.path.join(here, 'source', 'variants-latinlibrary.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
    print('variants', {k: len(v) for k, v in out.items()})
