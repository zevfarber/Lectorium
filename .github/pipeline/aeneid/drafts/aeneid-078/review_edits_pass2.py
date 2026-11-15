#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-078 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
E2 = [
 # P2-1 517-520: the pass-1 insertion left the tense clause dangling
 (3, 'n', "not here the leader Ufens of VII.745, the present tense for their home country.",
          "not here the leader Ufens of VII.745; the present tense is for their home country."),
 # P2-2 510-512 (echo): 'surer messenger who speeds to Aeneas' is close to stock versions; recast
 (0, 'i', "No longer is it only rumour of the disaster, but a surer messenger who speeds to Aeneas: his men are a hair's breadth from death, and it is time to help the routed Trojans.",
          "It is no longer mere rumour of the disaster: a more certain informant speeds to Aeneas with word that his men are within a hair of death, and that it is time to help the routed Trojans."),
 # P2-3 557 (echo): 'Lie there now' is the stock rendering of the Homeric line too; recast
 (24, 'i', "“Lie there now, you terror of the field.", "“Lie where you are now, you dreaded warrior."),
 # P2-4 559-560 (echo): 'hungry fish will lick your wounds' is stock; recast
 (26, 'i', "and hungry fish will lick your wounds.”", "and fish that have gone unfed will lap at your wounds.”"),
 # P2-5 569-570a (echo): 'raged in victory over the whole field, once his blade had grown warm' is close to stock; recast
 (29, 'i', "so Aeneas raged in victory over the whole field, once his blade had grown warm with blood.",
           "so, once his sword-point had grown warm, Aeneas raged his fill across the whole plain, a conqueror."),
]
for k, f, old, new in E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
A.jdump(D, p)
print('applied', len(E2), 'edits')
