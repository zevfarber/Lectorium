#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-076 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E2 = [
 # P2-1 394: pass-1 wording stacked two appositions
 (16, 'n', "'the Evandrian sword', the sword of Evander's house, wielded by his son, the adjective from the name used as with 'Daucia proles' just before.",
           "'the Evandrian sword', the sword of Evander's house in his son's hand; the adjective from the name is used as with 'Daucia proles' just before."),
 # P2-2 418-420a: the play canens/canentia rests on different verbs with different quantities (cf. sc 10.417, 10.418)
 (27, 'n', "'canentia lumina', 'whitening eyes', from 'caneo', 'to be grey or white':",
           "'canentia lumina', 'whitening eyes', from 'caneo' (long 'a', as in 'canus'), 'to be grey or white':"),
 (27, 'n', "a play on 'canens', 'singing', in the line before.",
           "a play on 'canens', 'singing' (short 'a', from 'cano'), in the line before."),
]
for k, f, old, new in E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
A.jdump(D, p)
print('applied', len(E2), 'edits')
