#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-071 units.json (after review_edits.py). Same rules: l/i/n only, old once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 (4, 'n', "Everything here is Turnus's, his eyes, his armour, his crest, though only",
          "Everything here is Turnus's (his eyes, his armour, his crest), though only"),
 (27, 'i', "lunging with flashing sword from the rampart", "lunging with his flashing sword from the rampart"),
]
for k, f, old, new in E:
    assert U[k][f].count(old) == 1, (k, f, old)
    U[k][f] = U[k][f].replace(old, new)
A.jdump(D, p); print('applied', len(E), 'edits')
