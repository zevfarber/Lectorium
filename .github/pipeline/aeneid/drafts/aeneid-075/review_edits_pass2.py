#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-075 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E2 = [
 # P2-1 342-344: 'strike him in return' left 'him' ambiguous (Numitor or Aeneas)
 (29, 'i', "but he was not allowed to strike him in return, and only grazed",
           "but he was not granted a hit on Aeneas in return, and only grazed"),
 # P2-2 315-317a: Phoebe's short final -e (scan-fixes 10.316)
 (16, 'n', "('Phoebe', vocative: the poet turns to address the god)",
           "('Phoebe', vocative, with short final '-e': the poet turns to address the god)"),
]
for k, f, old, new in E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E2), 'edits')
