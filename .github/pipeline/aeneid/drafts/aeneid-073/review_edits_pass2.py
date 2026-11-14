#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-073 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E2 = [
 # P2-1 135b-137a: 'set into dark wood' contradicts the pass-1 correction (boxwood is pale)
 (20, 'n', "'inlaid', ivory set into dark wood.", "'inlaid', ivory set into wood."),
 # P2-2 135b-137a: name the place of the hiatus exactly (scan-fixes 10.136: at the main caesura)
 (20, 'n', "stays long at the pause in mid-line.", "stays long at the main caesura."),
]
for k, f, old, new in E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E2), 'pass-2 edits')
