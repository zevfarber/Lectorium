#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-074 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E2 = [
 # P2-1 260-262a: the pass-1 i put 'habet' into the past; keep Virgil's present in both clauses, as l does
 (33, 'i', "he had the Trojans and his own camp in sight, when he raised the blazing shield high in his left hand.",
           "he has the Trojans and his own camp in sight, when he lifts the blazing shield high in his left hand."),
 # P2-2 224-228a: ignarum's long a (scan-fixes 10.228)
 (13, 'n', "'ignarum', 'unknowing':", "'ignarum' (long 'a', from 'gnarus'), 'unknowing':"),
 # P2-3 262b-264a: Dardanidae's short -da-ni- (scan-fixes 10.263)
 (34, 'n', "'Dardanidae', 'the Dardanians',", "'Dardanidae', 'the Dardanians' (Dar-da-ni-dae, the middle syllables short),"),
]
for k, f, old, new in E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E2), 'pass-2 edits')
