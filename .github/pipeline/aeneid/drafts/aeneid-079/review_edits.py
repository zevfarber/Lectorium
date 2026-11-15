#!/usr/bin/env python3
"""Reviewer's edits to aeneid-079 units.json (pass 1). Each edit: (unit index or 'about', field, old, new);
old must occur exactly once in that field. Only l, i, n are touched; t never. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
E = [
 # L1 607: 'rebare' is Virgil's form (not Greenough's spelling), imperfect indicative of reor
 (1, 'n', "'rebare', Greenough's form of 'rebaris', 'you used to think', from 'reor';",
          "'rebare' = 'rebaris', imperfect indicative of 'reor', 'as you supposed';"),
 # echo 607
 (1, 'i', "“My sister, and my dearest wife as well, you were right in what you thought, and your judgement does not mislead you:",
          "“Sister of mine, and no less my most dear wife, it is just as you supposed, and your judgement does not mislead you:"),
 # L2 616: Daunus is not called king; Turnus rules
 (3, 'n', "'Dauno… parenti', Daunus, Turnus's father, king of Ardea.",
          "'Dauno… parenti', Daunus, Turnus's aged father, at Ardea (688)."),
 # M 619: X.76 makes Pilumnus his grandfather
 (5, 'n', "('pater, avus, proavus, abavus').",
          "('pater, avus, proavus, abavus'); at X.76 Juno called Pilumnus his grandfather ('avus'), a small inconsistency."),
 # L3 621: not framing the line ('Cui rex' first)
 (6, 'n', "the adjective and its noun framing the line;",
          "the adjective and its noun far apart, 'Olympi' held to the end of the line;"),
 # echo 627
 (8, 'i', "you are feeding on empty hopes.”", "the hopes you nourish are empty.”"),
 # echo 637
 (13, 'i', "a marvel to behold,", "a wondrous thing to see,"),
 # L4 641: qualis may be acc. pl. with figuras
 (14, 'n', "looks back to the phantom, which is like the ghosts of the dead.",
           "looks back to the phantom, which is like the ghosts of the dead; 'qualis' may instead be accusative plural (= 'quales') with 'figuras', 'such shapes as', with the same sense."),
 # L5 647: Virgil's own Greek forms, not an edition's spelling
 (17, 'n', "'Aenea', the Greek vocative; Greenough keeps both.",
           "'Aenea', the Greek vocative, with a long final 'a'."),
 # echo 649
 (17, 'i', "he cried: “Where are you running, Aeneas?", "he cried: “Where do you flee, Aeneas?"),
 # echo 652
 (19, 'i', "and did not see that the winds were carrying his triumph away.",
           "and never saw that the winds were bearing off the joy he thought was his."),
 # L6 655: cross-reference, Clusium's men under Massicus
 (20, 'n', "and 'ora' can mean any region.",
           "and 'ora' can mean any region; its men came with Massicus (X.166–167)."),
 # L7 656: huc is 'hither'
 (21, 'n', "'Huc', 'here', into the ship.", "'Huc', 'hither', into the ship."),
 # D1 661: rule 5b, praelia a misprint for proelia (proelia 40 times elsewhere in the edition)
 (24, 'n', "Greenough prints these two lines after 660;",
           "The print has 'praelia', a misprint for 'proelia', corrected here: 'in proelia', 'to battle'; the edition prints 'proelia' everywhere else. Greenough prints these two lines after 660;"),
 (24, 'n', " 'in praelia', Greenough's spelling of 'proelia'.", ""),
 # L8 668: 'tanton' is the ordinary shortened form, not Greenough's
 (28, 'n', "'tanton', Greenough's shortened form of 'tantone',", "'tanton', the shortened form of 'tantone',"),
 # L9 670: quem is predicative, not in apposition; i 'Where have I come from?' misread unde abii
 (29, 'n', "'quem' standing in apposition to 'me':", "'quem' predicative with 'me':"),
 (29, 'i', "Where have I come from?", "What place have I left?"),
 # L10 673: LL 'quosque' does not change the sense (drafter's open point): cut
 (32, 'n', "; The Latin Library prints 'quosque', 'and whom', a plain relative running on from 672, with much the same sense", ""),
 # echo 685
 (36, 'i', "Three times he tried each course, and three times", "Each course he attempted three times, and three times"),
 # L11 687: secundo goes with both nouns (both masculine ablative singular)
 (37, 'n', "with 'secundo' agreeing with the nearer noun.", "with 'secundo' going with both nouns."),
]
for k, f, old, new in E:
    s = D['about'] if k == 'about' else U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    if k == 'about': D['about'] = s.replace(old, new)
    else: U[k][f] = s.replace(old, new)
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
    assert 'sc' not in u
A.jdump(D, p)
print('applied', len(E), 'edits')
