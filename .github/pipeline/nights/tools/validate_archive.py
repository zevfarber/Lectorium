#!/usr/bin/env python3
"""
validate_archive.py — the gate a Nights page archive must pass before it is pushed.

    python3 validate_archive.py <archive.json> [--prev <previous_archive.json>]

Checks: JSON parses; every line has a non-empty "t" and a ref P<pp>L<ll>; refs are in order and
line numbers are contiguous within a page; pages are contiguous and follow the previous archive
(--prev); no Latin letters or digits inside Arabic lines (a common agent slip); no vowel marks in
a prose line (only lines marked v may carry tashkil); no precomposed alif-hamza/madda in a verse
line that has none in the print is NOT checkable here — that is the adjudicator's job; the
page joins (last words of page N + first words of N+1) are printed for the adjudicator to read.
Exit 0 and RESULT PASS, or exit 1 with the failures listed.
"""
import json, re, sys, unicodedata

MARKS = set('ًٌٍَُِّْٰ')

def main():
    path = sys.argv[1]; prev = sys.argv[sys.argv.index('--prev') + 1] if '--prev' in sys.argv else None
    fails = []
    try:
        d = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('RESULT FAIL: does not parse:', e); sys.exit(1)
    lines = d.get('lines', [])
    if not lines: fails.append('no lines')
    last_pp, last_ll, pages = None, 0, []
    for L in lines:
        ref, t = L.get('ref', ''), L.get('t', '')
        m = re.fullmatch(r'P(-?\d{2,3})L(\d{2})', ref)
        if not m: fails.append(f'bad ref {ref!r}'); continue
        pp, ll = int(m.group(1)), int(m.group(2))
        if pp != last_pp:
            if last_pp is not None and pp != last_pp + 1: fails.append(f'page jump {last_pp}->{pp}')
            if ll != 1: fails.append(f'{ref}: page does not start at L01')
            pages.append(pp); last_pp, last_ll = pp, 0
        if ll != last_ll + 1: fails.append(f'{ref}: line numbering gap')
        last_ll = ll
        if not t.strip(): fails.append(f'{ref}: empty text')
        if re.search(r'[A-Za-z0-9]', t): fails.append(f'{ref}: Latin letters/digits in text')
        if not L.get('v') and not L.get('h') and any(c in MARKS for c in t):
            fails.append(f'{ref}: vowel marks in a prose line (only v lines carry tashkil)')
    if prev:
        pd = json.load(open(prev, encoding='utf-8'))
        pprev = max(int(re.match(r'P(-?\d+)', L['ref']).group(1)) for L in pd['lines'])
        if pages and pages[0] != pprev + 1:
            fails.append(f'archive starts at printed p. {pages[0]}, previous archive ends at p. {pprev}')
    # page joins, for the eye
    byp = {}
    for L in lines: byp.setdefault(int(re.match(r'P(-?\d+)', L['ref']).group(1)), []).append(L['t'])
    print('page joins (read each as one sentence):')
    ps = sorted(byp)
    for a, b in zip(ps, ps[1:]):
        print(f'  p{a}->p{b}: {" ".join(byp[a][-1].split()[-4:])}  ||  {" ".join(byp[b][0].split()[:4])}')
    if fails:
        print('RESULT FAIL'); [print('  -', f) for f in fails]; sys.exit(1)
    print(f'RESULT PASS  ({len(lines)} lines, printed pp. {ps[0]}-{ps[-1]})')

if __name__ == '__main__':
    main()
