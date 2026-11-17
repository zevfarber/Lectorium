#!/usr/bin/env python3
"""Reviewer helper (aeneid-097; adapted from 090): make_units.py's checks run against the edited units.json (make_units.py itself is
not rerun: it would overwrite units.json with the drafter's strings), plus a replica of build_aeneid.py's per-unit
checks (tiling, ln, p, line counts, five-line limit, ending at punctuation)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A
EXEMPT = set(); NOSTOP = set(); NOTE_MARKS = set()
P = A.part('aeneid-097'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
D = A.jload(os.path.join(HERE, 'units.json')); U = D['sentences']
prev_end_line = None
for u in U:
    t, ln, l, i, n = u['t'], u['ln'], u['l'], u['i'], u['n']
    if bool(u.get('p')) != (prev_end_line != ln and ln in paras): print('P FLAG', ln)
    prev_end_line = ln + t.count('\n')
    if t.count('\n') != l.count('\n'): print('LINE COUNT', ln)
    if t.count('\n') > 4: print('TOO LONG', ln)
    if '\n' in i: print('NEWLINE IN i', ln)
    if t.rstrip('”]')[-1] not in A.TERMINAL + ',' and ln not in NOSTOP: print('ENDING', ln, repr(t[-12:]))
    nw = len(n.split())
    if nw > 139 or nw < 15: print('NOTE LENGTH', ln, nw)
    for mk in '“”[]':
        if t.count(mk) != l.count(mk) and ln not in EXEMPT: print('MARK l', ln, mk)
        if mk in '“”' and t.count(mk) != i.count(mk) and ln not in EXEMPT: print('MARK i', ln, mk)
    if ('“' in n or '”' in n) and ln not in NOTE_MARKS: print('DOUBLE MARK IN n', ln)
covered = sorted({u['ln'] + k for u in U for k in range(u['t'].count('\n') + 1)})
if covered != [l['n'] for l in L]: print('COVERAGE', covered)
if A.sha(L) != P['sha256']: print('SHA MISMATCH')
for lay in ('t', 'l', 'i'):
    print(lay, 'marks', sum(u[lay].count('“') for u in U), '/', sum(u[lay].count('”') for u in U))
print('notes', min(len(u['n'].split()) for u in U), '-', max(len(u['n'].split()) for u in U), 'words;', len(U), 'units;', len(covered), 'lines')
# ---- replica of build_aeneid.py's unit checks (lines 21-44)
S = '\n'.join(l['t'] for l in L); nums = [l['n'] for l in L]; paras2 = paras | {L[0]['n']}
pos = 0; li = 0; atStart = True; errs = []
for k, u in enumerate(U):
    t = u['t']
    if not S.startswith(t, pos): errs.append(f'unit {k}: t does not match'); break
    if u['ln'] != nums[li]: errs.append(f'unit {k}: ln')
    if bool(u.get('p')) != (atStart and nums[li] in paras2): errs.append(f'unit {k}: p')
    if t.count('\n') + 1 > 5: errs.append(f'unit {k} (line {nums[li]}): spans more than five lines')
    if t.rstrip('”—]')[-1:] not in A.TERMINAL + ',' and not t.endswith('—'): errs.append(f'unit {k} (line {nums[li]}): does not end at punctuation')
    pos += len(t); li += t.count('\n')
    if pos < len(S):
        if S[pos] not in ' \n':
            if S[pos-1] not in A.TERMINAL: errs.append(f'unit {k}: ends mid-word')
            atStart = False
        else:
            atStart = S[pos] == '\n'; li += 1 if atStart else 0; pos += 1
if pos != len(S): errs.append('not fully covered')
print('BUILD REPLICA:', errs or 'OK')
# ---- t, ln, p, v unchanged against the drafter's file (copy kept outside the repo before review_edits.py ran)
import json
B = '/tmp/claude-0/-home-user-Lectorium/b0556cfd-434d-57f0-9c80-564604a6c0cc/scratchpad/units.orig.json'
if os.path.exists(B):
    O = A.jload(B)['sentences']
    print('t/ln/p/v vs drafter:', 'OK' if [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in O] == [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] else 'CHANGED')
    print('fields changed:', sum(o[f] != u[f] for o, u in zip(O, U) for f in ('l', 'i', 'n')))
