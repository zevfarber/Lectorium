#!/usr/bin/env python3
"""
apply_verdicts.py — build the page archive from pass 1 plus the adjudicator's verdicts.

    python3 apply_verdicts.py <run_dir> <first_page> <last_page> <out_archive.json>

Takes <run_dir>/p<NNN>/pass1.json as the base text, applies every entry of
<run_dir>/verdicts.json whose verdict differs from pass 1 (word replacement inside the line;
"MISSING LINE" verdicts that say a line exists are inserted from pass 2; verdicts that say a
pass-1 line does not exist are dropped), and writes the archive:

    {"edition": ..., "scan": ..., "pages": "printed pp. A-B (PDF pages A+18 .. B+18)",
     "method": ..., "lines": [{"ref": "P<pp>L<ll>", "t": "...", "v": true?, "h": true?}, ...]}

Printed page = PDF page - 18 for Calcutta II vol. 1 (Arabic text begins at PDF page 19).
Refs use the PRINTED page number, as the pilot's archive does. Prints what it applied and
every low-confidence verdict, for the LOG.
"""
import json, sys

PDF_TO_PRINTED = -18

def main():
    run, p0, p1, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    V = json.load(open(f'{run}/verdicts.json', encoding='utf-8'))
    pages = {p: json.load(open(f'{run}/p{p:03d}/pass1.json', encoding='utf-8')) for p in range(p0, p1 + 1)}
    pass2 = {p: json.load(open(f'{run}/p{p:03d}/pass2.json', encoding='utf-8')) for p in range(p0, p1 + 1)}
    applied, low, drops, inserts = 0, [], [], []
    for v in V:
        if v.get('join'):
            print(f'JOIN NOTE (PDF p{v["p"]}): {v.get("note","")}'); continue
        p = int(v['p']); i1, i2 = v.get('i1'), v.get('i2'); verdict = (v.get('verdict') or '').strip()
        if v.get('confidence') == 'low': low.append((p, i1 if i1 is not None else i2, verdict, v.get('note', '')))
        if i1 is None:                                   # line only in pass 2
            if verdict and verdict.upper() != 'NO SUCH LINE':
                inserts.append((p, i2, {'line': 0, 't': verdict}))
            continue
        L = pages[p][i1]
        if i2 is None:                                   # line only in pass 1
            if verdict.upper() == 'NO SUCH LINE': drops.append((p, i1))
            continue
        if v['pass1'] and v['pass1'] in L['t'] and verdict != v['pass1']:
            L['t'] = L['t'].replace(v['pass1'], verdict, 1); applied += 1
        elif v['pass1'] and v['pass1'] not in L['t']:
            print(f'WARNING: could not locate pass-1 text on page {p} line {i1 + 1}: {v["pass1"]!r}')
    for p, i1 in sorted(drops, reverse=True): pages[p].pop(i1)
    for p, i2, L in sorted(inserts, key=lambda x: (x[0], x[1]), reverse=True):
        # insert after the pass-1 line that matches the pass-2 line preceding i2
        prev = pass2[p][i2 - 1]['t'] if i2 > 0 else None
        k = next((n for n, x in enumerate(pages[p]) if prev and x['t'].strip() == prev.strip()), None)
        pages[p].insert(0 if k is None else k + 1, L)
    lines = []
    for p in range(p0, p1 + 1):
        pp = p + PDF_TO_PRINTED
        for n, L in enumerate(pages[p], 1):
            e = {'ref': f'P{pp:02d}L{n:02d}', 't': L['t']}
            for k in ('v', 'h'):
                if L.get(k): e[k] = True
            lines.append(e)
    arch = {'edition': 'Macnaghten, Alif Laila vol. 1, Calcutta 1839 (Calcutta II)',
            'scan': 'archive.org aliflailaorbooko01macn, 300 ppi',
            'pages': f'printed pp. {p0 + PDF_TO_PRINTED}-{p1 + PDF_TO_PRINTED} (PDF pages {p0}-{p1})',
            'method': 'Tesseract draft (tools/td/calc.traineddata) corrected against 2x line crops and page bands by one agent; independent second full transcription; disagreements adjudicated by a third agent against the images. Prose is the bare rasm as printed; verse carries the edition\'s vowel marks, hemistichs separated by " * " (v); headings and night labels marked h; trailing filler written "—".',
            'lines': lines}
    json.dump(arch, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'applied {applied} verdict(s), dropped {len(drops)} line(s), inserted {len(inserts)}; {len(lines)} lines -> {out}')
    if low:
        print('LOW-CONFIDENCE verdicts (record in LOG):')
        for p, i, t, note in low: print(f'  PDF p{p} line {i + 1}: {t}  — {note[:120]}')

if __name__ == '__main__':
    main()
