#!/usr/bin/env python3
"""Reviewer's edits to aeneid-079 units.json (pass 2), after re-reading every field pass 1 changed."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
E = [
 # P2-1 641: pass-1 insertion repeated 'qualis'; tightened
 (14, 'n', "the ghosts of the dead; 'qualis' may instead be accusative plural (= 'quales') with 'figuras', 'such shapes as', with the same sense.",
           "the ghosts of the dead (or it is accusative plural, = 'quales', with 'figuras', 'such shapes as': the sense is the same)."),
 # P2-2 670: i word order clumsy
 (29, 'i', "What is this flight, and what sort of man will it bring me home as?",
           "What flight is this, and as what kind of man will it bring me home?"),
]
for k, f, old, new in E:
    s = U[k][f]; assert s.count(old) == 1, (k, f, old); U[k][f] = s.replace(old, new)
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
marks = {f: [(u['ln'], u[f].count('“'), u[f].count('”')) for u in U if '“' in u[f] or '”' in u[f]] for f in 'tli'}
assert marks['t'] == marks['l'] == marks['i'], marks
assert sum(x[1] for x in marks['t']) == sum(x[2] for x in marks['t']) == 6
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
    assert 'sc' not in u
A.jdump(D, p)
print('applied', len(E), 'edits; marks', marks['t'])
