#!/usr/bin/env python3
"""Reviewer's edits to aeneid-080 units.json (pass 2), after re-reading every field pass 1 changed."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
E = [
 # P2-1 781-782: pass-1 i left 'dying' dangling on 'his thoughts'
 (34, 'i', "he looked up at the sky, and dying, his thoughts went home to the Argos he loved;",
           "he looked up at the sky, and as he died his thoughts went home to the Argos he loved;"),
 # P2-2 744-746: checked in the pinned source, XII.310 has 'conduntur', not 'clauduntur'
 (20, 'n', "Virgil uses these two lines again in XII.309–310.",
           "Virgil repeats these two lines at XII.309–310, with 'conduntur', 'are hidden', for 'clauduntur'."),
 # P2-3 689: checked in the pinned source, VII.648 prints 'contemptor divom'
 (0, 'n', "'contemptor divum'", "'contemptor divom'"),
]
for k, f, old, new in E:
    s = U[k][f]; assert s.count(old) == 1, (k, f, old); U[k][f] = s.replace(old, new)
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
# speech marks: t carries the print (stray ” at the head of 744 and 776); l and i close each speech in its own unit
PAIRS = {742: 744, 772: 776}
marks = {f: [(u['ln'], u[f].count('“'), u[f].count('”')) for u in U if '“' in u[f] or '”' in u[f]] for f in 'tli'}
assert marks['l'] == marks['i'] == [(736, 1, 1), (739, 1, 1), (742, 1, 1), (772, 1, 1)], marks
assert marks['t'] == [(736, 1, 1), (739, 1, 1), (742, 1, 0), (744, 0, 1), (772, 1, 0), (776, 0, 1)], marks['t']
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
    assert 'sc' not in u
A.jdump(D, p)
print('applied', len(E), 'edits; marks', marks['t'])
