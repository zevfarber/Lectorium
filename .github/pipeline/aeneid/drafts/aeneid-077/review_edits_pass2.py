#!/usr/bin/env python3
"""Reviewer's pass-2 edits to aeneid-077 units.json (run after review_edits.py). Same rules: (unit, field, old, new),
old must occur exactly once; only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E2 = [
 # P2-1 439-440: pass 1 made 'enemy' singular, which no longer fits 'the first of those enemies'
 (0, 'n', "will fall to a greater enemy (438): here the first of those enemies arrives.",
          "will each fall to a greater enemy (438): here the first of those enemies arrives."),
 # P2-2 464-465: pass-1 wording repeated 'sub imo corde premit'
 (12, 'n', "enclosing 'sub imo corde premit'. 'sub imo corde premit', 'presses down",
           "enclosing 'sub imo corde premit', 'presses down"),
 # P2-3 495b-499: pass-1 wording broke the sentence
 (30, 'n', "the fifty daughters of Danaus, married against their will to their cousins the sons of Aegyptus, all but one of them killed",
           "of the fifty daughters of Danaus, married against their will to their cousins the sons of Aegyptus, all but one killed"),
 # P2-4 503-505a: 'buy back' added a 're-' the Latin lacks ('emptum', 'bought')
 (33, 'i', "when he would pay a great price to buy back Pallas unharmed,",
           "when he will wish he could buy Pallas's safety at a great price,"),
 # P2-5 507-509: 'rediture' is future, 'who are to go home'
 (35, 'i', "O you who go home to your father to be his great sorrow and his great pride!",
           "O you who are to go home to your father, his great sorrow and his great pride!"),
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
