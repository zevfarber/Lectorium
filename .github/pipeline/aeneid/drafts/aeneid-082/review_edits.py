#!/usr/bin/env python3
"""Reviewer's edits to aeneid-082 units.json (passes 1 and 2; the script was re-run from the drafter's file after pass 2). Each edit: (unit index, field, old, new); old must occur
exactly once in that field. Only l, i, n are touched; t, ln, p, v and the top-level fields never. Run once
(it refuses if the file has already been edited: the first old string must still be present)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

def PRINT(a, b):
    return (f"The print has '{a} ”{b}', the closing speech mark joined to the next word, a misprint for "
            f"'{a}” {b}', corrected here: the speech ends with '{a[:-1]}'. ")
def CLOSE(who):
    return f"The closing speech mark printed at the head of this unit belongs to {who} speech (see the note before)."

E = [
 # ---- rule-5b placement at 97/98, made the same as 077, 078, 080 and 081 (081 review D5): the print's reading
 #      opens the note of the unit where the speech closes; the next unit (whose t begins with the stray mark)
 #      points back to it.  (medium)
 (44, 'n', "'salve… vale', the two", PRINT('vale.', 'Nec') + "'salve… vale', the two"),
 (44, 'n', " The closing speech mark is printed joined to the next word; see the next unit.", ""),
 (45, 'n', "The print has 'vale. ”Nec', with the closing speech mark joined to the next word, a misprint for 'vale.” Nec', corrected here: the speech ends with 'vale'.", CLOSE("Aeneas's")),

 # ---- speech marks in i at 24: the speech has been open since 14, so i must not reopen it before 'Go' (medium)
 (11, 'i', "“Go,” he said, “and honour", "Go,” he said, “and honour"),

 # ---- elision list (medium)
 (28, 'n', "No elisions.", "Elision 'iuven(em) agresti'."),

 # ---- l construal (medium): 'sospite… nato' is an ablative absolute, not a dative
 (24, 'l', "wounds routed will you look on him, nor, safe, a dread\nwill you pray for, for your son, death, as a father.",
           "wounds routed will you look on him, nor, with safe, a dread\nwill you pray for, your son, death, as a father."),

 # ---- labels, wording, layout (low)
 (1, 'n', "with the infinitive 'dare', 'to give'.",
          "with the infinitive 'dare', 'to give'. 'et… -que', 'both… and', join 'praecipitant curae' and 'turbata… mens est'."),
 (2, 'n', "'Mezenti', Greenough's genitive in single '-i' for 'Mezentii'.",
          "'Mezenti', genitive, with the single '-i' that Virgil regularly uses for names in '-ius' (for 'Mezentii')."),
 (4, 'l', "thus beginning he urges, exulting:", "thus beginning he urges them, exulting as they were:"),
 (9, 'n', "'adnuerint', future perfect, 'shall have nodded':",
          "'adnuerint', 'shall have nodded', perfect subjunctive standing for a future perfect inside the purpose clause (the forms are the same):"),
 (13, 'n', "not elided before 'Evandro': a hiatus.",
           "not elided before 'Evandro': a hiatus, with a spondee in the fifth foot (Par-rha-si | ō Ē | van-dro), a Greek rhythm for two Greek names."),
 (14, 'l', "and, the grieving Trojan women, as to their hair according to custom loosed.",
           "and the Trojan women, as to their grieving hair according to custom loosed."),
 (15, 'n', "ablative absolute framing the line-end,", "ablative absolute split across the line-end,"),
 (15, 'n', "'regia', 'the royal dwelling', the hall where the king's son lies.",
           "'regia', 'the royal dwelling', Aeneas's quarters in the camp, where Pallas lies."),
 (23, 'n', "The third short exclamation in a row, each starting with a demonstrative ('Hi… Haec').",
           "The third short exclamation in a row, the last two starting with a demonstrative ('Hi… Haec')."),
 (28, 'l', "like, by a girl's reaped thumb, a flower,", "like, by a girl's thumb reaped, a flower,"),
 (37, 'n', "the marks after the full stop are not Latin, and the line is complete in sense and metre; the owner may know what they stand for.",
           "the marks after the full stop are not Latin (probably a slip of the electronic text rather than of Greenough's page), and the line is complete in sense and metre."),

 # ---- pass 2: l attachments (low)
 (16, 'l', "and on the smooth gaping breast the wound", "and, gaping on the smooth breast, the wound"),
 (32, 'l', "and many besides of the Laurentine prizes of the battle", "and many besides, of the Laurentine, prizes, of the battle,"),
 (45, 'n', "'to the high walls', the Trojan camp, framing the line-end.", "'to the high walls', the Trojan camp, split across the line-end."),

 # ---- i: echo recasts and register (low)
 (2, 'i', "a trophy to you, great lord of war:", "a trophy for you, great god, mighty in war:"),
 (17, 'i', "“Poor boy,” he said, “was it you that Fortune grudged me, just when she came to me smiling,",
           "“Pitiable boy,” he said, “was it you that Fortune, coming to me in gladness, begrudged me,"),
 (23, 'i', "So much for my solemn pledge!", "This is what my great pledge has come to!"),
 (44, 'i', "and for all time I say goodbye.”", "and for all time I bid you farewell.”"),
]

for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part', 'about')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    n = len(u['n'].split()); assert 15 <= n <= 139, (k, n)
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    assert o == c == 5, (lay, o, c)
A.jdump(D, p)
print('applied', len(E), 'edits')
