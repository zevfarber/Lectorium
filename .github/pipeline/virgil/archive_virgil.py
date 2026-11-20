#!/usr/bin/env python3
"""Build source/virgil-greenough.json and parts.json for the Eclogues and Georgics from the Perseus TEI of
Greenough's Virgil (the TEI files are kept in source/). Run once, in setup (2026-11-20); a run never needs it.

Edition: J. B. Greenough, The Bucolics, Aeneid, and Georgics of Virgil (Boston: Ginn & Company, 1881) — the
edition the Aeneid uses. Public domain everywhere.

Normalised, and nothing else: tags stripped; whitespace collapsed. The Perseus TEI of these two works carries
no paragraph marks and no speech marks (the Aeneid's does), so:
  - Eclogues: the TEI's <sp>/<speaker> turns (Greenough prints the speaker's name) are kept: the first line of
    each turn records `speaker`, and a turn begins a paragraph. The two inscription lines of Ecl. 5.43-44
    (<quote>) are kept as printed, in capitals.
  - Georgics: Perseus's `card` milestones (its sense sections) stand in for paragraphs.
Books are keyed E1..E10 (Eclogues) and G1..G4 (Georgics)."""
import re, json, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROMAN = 'I II III IV V VI VII VIII IX X'.split()
TARGET, MAXLEN, MINLEN = 100, 135, 55
def tei(n): return open(os.path.join(HERE, 'source', f'phi0690.{n}.perseus-lat2.xml'), encoding='utf8').read()
def clean(t): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t)).strip()
books, shas = {}, {}
x = tei('phi001'); shas['phi001'] = hashlib.sha256(x.encode()).hexdigest()
body = x[x.find('<body'):]
for k, ch in enumerate(re.split(r'<div type="textpart" subtype="poem" n="\d+">', body)[1:], 1):
    lines = []
    head = clean(re.search(r'<head>(.*?)</head>', ch, re.S).group(1))
    for m in re.finditer(r'(<speaker>(.*?)</speaker>)|<l\b[^>]*n="(\d+)"[^>]*>(.*?)</l>', ch, re.S):
        if m.group(1):
            pending = clean(m.group(2)); continue
        rec = {'n': int(m.group(3)), 't': clean(m.group(4)), 'p': not lines}
        if 'pending' in dir() and pending:
            rec['speaker'] = pending; rec['p'] = True; pending = None
        lines.append(rec)
    pending = None
    books[f'E{k}'] = {'head': head, 'lines': lines}
y = tei('phi002'); shas['phi002'] = hashlib.sha256(y.encode()).hexdigest()
body = y[y.find('<body'):]
for k, ch in enumerate(re.split(r'<div type="textpart" subtype="book" n="\d+">', body)[1:], 1):
    lines = []; card = False
    for m in re.finditer(r'(<milestone[^>]*unit="card"[^>]*/>)|<l\b([^>]*)>(.*?)</l>', ch, re.S):
        if m.group(1): card = True; continue
        n = int(re.search(r'n="(\d+)"', m.group(2)).group(1)); t = m.group(3)
        dele = '<del' in t
        s = clean(t)
        if dele: s = '[' + s + ']'
        lines.append({'n': n, 't': s, 'p': card or not lines}); card = False
    books[f'G{k}'] = {'head': f'GEORGICON LIBER {ROMAN[k-1]}', 'lines': lines}
odd = []
for b, d in books.items():
    L = d['lines']
    for a, c in zip(L, L[1:]):
        if c['n'] != a['n'] + 1: odd.append(f'{b}: numbering jumps {a["n"]} -> {c["n"]}')
src = {'edition': 'J. B. Greenough, ed., The Bucolics, Aeneid, and Georgics of Virgil (Boston: Ginn & Company, 1881)',
       'tei': {'Eclogues': 'PerseusDL/canonical-latinLit data/phi0690/phi001/phi0690.phi001.perseus-lat2.xml',
               'Georgics': 'PerseusDL/canonical-latinLit data/phi0690/phi002/phi0690.phi002.perseus-lat2.xml'},
       'teiSha256': shas,
       'normalised': 'tags stripped, whitespace collapsed; Eclogue speakers kept as `speaker` on the first line of each turn; Georgics paragraphs = Perseus card milestones; <del> lines in [ ]; nothing else',
       'books': {b: d['lines'] for b, d in books.items()}, 'heads': {b: d['head'] for b, d in books.items()}}
json.dump(src, open(os.path.join(HERE, 'source', 'virgil-greenough.json'), 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
def sha(ls): return hashlib.sha256('\n'.join(l['t'] for l in ls).encode('utf8')).hexdigest()
parts = []; pid = 0
for b, d in books.items():
    L = d['lines']; first, last = L[0]['n'], L[-1]['n']
    if b.startswith('E'):
        cuts = [last]
    else:
        ends = sorted({l['n'] - 1 for l in L if l['p'] and l['n'] > first} | {last})
        INF = 1e18; best = {first - 1: (0, None)}
        for e in ends:
            cand = (INF, None)
            for s in sorted(best):
                if s >= e: continue
                Ln = e - s
                pen = (Ln - TARGET) ** 2 * 50 if (Ln > MAXLEN and any(s < q < e for q in ends)) else (Ln - TARGET) ** 2 * (4 if Ln < MINLEN else 1)
                if best[s][0] + pen < cand[0]: cand = (best[s][0] + pen, s)
            best[e] = cand
        cuts = []; e = last
        while e is not None and e >= first: cuts.append(e); e = best[e][1]
    s = first
    for e in sorted(c for c in cuts if c >= first):
        pid += 1; seg = [l for l in L if s <= l['n'] <= e]
        work = 'Eclogues' if b.startswith('E') else 'Georgics'
        num = ROMAN[int(b[1:]) - 1]
        parts.append({'id': f'virgil-{pid:03d}', 'seq': pid, 'book': b, 'work': work, 'from': s, 'to': e, 'lines': len(seg),
                      'cite': (f'Ecl. {num}' if work == 'Eclogues' and (s, e) == (first, last) else f'{"Ecl." if work == "Eclogues" else "G."} {num}.{s}–{e}'),
                      'group': f'Eclogue {num}' if work == 'Eclogues' else f'Book {num}',
                      'file': f'virgil-{pid:03d}.json', 'sha256': sha(seg), 'status': 'todo'})
        s = e + 1
json.dump({'work': 'Eclogues and Georgics (Virgil)', 'source': 'source/virgil-greenough.json',
           'cutRule': 'each Eclogue is one part; the Georgics are cut only at Perseus card milestones, target ~100 lines',
           'parts': parts}, open(os.path.join(HERE, 'parts.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
import statistics as st
Ls = [p['lines'] for p in parts]
print('parts', len(parts), 'min/median/max', min(Ls), st.median(Ls), max(Ls)); print('oddities', odd)
print({b: len(d['lines']) for b, d in books.items()})
print('speakers', sum(1 for d in books.values() for l in d['lines'] if l.get('speaker')))
