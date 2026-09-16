#!/usr/bin/env python3
"""
diff_passes.py — list every disagreement between two independent transcriptions of a page run.

    python3 diff_passes.py <run_dir> <first_page> <last_page>

Reads <run_dir>/p<NNN>/pass1.json and pass2.json (lists of {"line", "t", ...}) and writes
<run_dir>/disputes.json:
    {"<page>": [[i1, i2, kind, pass1_text, pass2_text], ...]}
where i1/i2 are 0-based indices into pass1/pass2 (None when a line exists in only one pass),
kind is "word" (a differing word span) or "MISSING LINE". Prints a summary. The adjudicator
agent (prompts/adjudicate.md) decides each entry from the images.
"""
import json, re, sys, difflib

def norm(s):
    return re.sub(r'\s+', ' ', s.replace('—', ' — ')).strip()

def main():
    run, p0, p1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    disputes, total = {}, 0
    for p in range(p0, p1 + 1):
        a = json.load(open(f'{run}/p{p:03d}/pass1.json', encoding='utf-8'))
        b = json.load(open(f'{run}/p{p:03d}/pass2.json', encoding='utf-8'))
        A = [norm(x['t']) for x in a]; B = [norm(x['t']) for x in b]
        sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
        pairs = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                pairs += [(i1 + k, j1 + k) for k in range(i2 - i1)]
            else:
                for k in range(max(i2 - i1, j2 - j1)):
                    pairs.append((i1 + k if i1 + k < i2 else None, j1 + k if j1 + k < j2 else None))
        dl = []
        for i, j in pairs:
            if i is None or j is None:
                dl.append([i, j, 'MISSING LINE', A[i] if i is not None else '', B[j] if j is not None else ''])
                continue
            if A[i] == B[j]: continue
            wa, wb = A[i].split(), B[j].split()
            for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes():
                if op != 'equal':
                    dl.append([i, j, 'word', ' '.join(wa[a1:a2]), ' '.join(wb[b1:b2])])
        disputes[str(p)] = dl; total += len(dl)
        print(f'page {p}: pass1 {len(a)} lines, pass2 {len(b)} lines, {len(dl)} disagreement(s)')
    json.dump(disputes, open(f'{run}/disputes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('total disagreements:', total)

if __name__ == '__main__':
    main()
