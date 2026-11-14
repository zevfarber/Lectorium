#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-072 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E2 = [
 # P2-1 51-52a: smoother wording of the pass-1 Idaliae gloss
 (30, 'n', "'Idaliae… domus', 'the house of Idalia', genitive of Idalia, another name for Idalium: her temple there.",
           "'Idaliae… domus', 'the house of Idalia', genitive; Idalia is another name for Idalium, and the house is her temple there."),
 # P2-2 39-41: the pass-1 hedge quoted 'Acheronta movebo' a second time in the same note
 (23, 'n', "as her own 'Acheronta movebo' suggests (some make it Allecto).", "as her own words in Book VII suggest (some make it Allecto)."),
]
for k, f, old, new in E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E2), 'pass-2 edits')
