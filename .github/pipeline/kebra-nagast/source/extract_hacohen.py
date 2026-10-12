#!/usr/bin/env python3
"""Turn Ran HaCohen's per-chapter HTML (raw/KN-NNN.html, fetched 2026-10-12 by the Run 3 fetcher from
tau.ac.il/~hacohen/KN/) into source/kebra-nagast-bezold1905.json. Run once; the output is the pinned source.
Chapter = HaCohen's file (KN 1..117 = Bezold's chapters 1-117; KN 118 = the colophon).
Each chapter: list of paragraphs, each a single-spaced string of Geʿez exactly as in the file
(numeric character references decoded; figure-spaces and nbsp removed; whitespace runs -> one space)."""
import re, html, json, os, hashlib, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
def paras(n):
    s = open(os.path.join(HERE, 'raw', f'KN-{n:03d}.html'), encoding='utf-8').read()
    s = re.sub(r'(?is)<(script|style|form|head|table).*?</\1>', '', s)
    s = re.sub(r'(?is)<a [^>]*>.*?</a>', '', s)           # the chapter number link
    out = []
    for m in re.finditer(r'(?is)<p\b[^>]*>(.*?)</p>', s):
        t = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
        t = t.replace(' ', ' ').replace('\xa0', ' ')
        t = re.sub(r'\s+', ' ', t).strip()
        if t:
            out.append(unicodedata.normalize('NFC', t))
    return out
chapters = []
for n in range(1, 119):
    ps = paras(n)
    bad = sorted({c for p in ps for c in p if not (0x1200 <= ord(c) <= 0x139F or c == ' ')})
    chapters.append({'n': n, 'label': str(n) if n <= 117 else 'Colophon', 'paragraphs': ps,
                     'words': sum(len(re.findall(r'[ሀ-ፚ፩-፼]+', p)) for p in ps),
                     'nonGeez': bad})
doc = {'work': 'Kebra Nagast', 'edition': 'Carl Bezold, Kebra Nagast: Die Herrlichkeit der Könige (Abh. K. Bayer. Akad. Wiss. XXIII/1, Munich 1905) — public domain',
       'digital': "Ran HaCohen's Unicode text of Bezold (tau.ac.il/~hacohen/KN/KN <n>.html), from Michal Jerabek's 1995 Library of Ethiopic Texts; fetched 2026-10-12",
       'chapters': chapters}
json.dump(doc, open(os.path.join(HERE, 'kebra-nagast-bezold1905.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(c['words'] for c in chapters), 'words;', [c['n'] for c in chapters if c['nonGeez']])
