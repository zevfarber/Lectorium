#!/usr/bin/env python3
"""Reviewer's edits to aeneid-072 units.json (pass 1). Each edit: (unit index, field, old, new);
old must occur exactly once in that field. Only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # MED 1-4: Iliad 4 has a council but no ban on fighting; only Iliad 8 has the ban
 (0, 'n', "as the Iliad does at the start of Books 4 and 8, where Zeus calls the gods together and forbids them to join the fighting.",
          "as the Iliad does at the start of Books 4 and 8; in Book 8 Zeus calls the gods together and forbids them to join the fighting."),
 # L 6: quianam's syllables (scan-fixes 10.6)
 (2, 'n', "'quianam', an archaic word for 'why',", "'quianam', three syllables, qui-a-nam, an archaic word for 'why',"),
 # L 9: the question is not half a line
 (4, 'n', "The short question, half a line long,", "The short question, less than a line long,"),
 # L 11-13: 'early' is not in the Latin; elision list; framing claim
 (6, 'l', "There will come the right time for battle — do not summon it early —", "There will come the right time for battle — do not summon it —"),
 (6, 'n', "'iustum… tempus', 'the right time', framing the line, with 'pugnae' as genitive.",
          "'iustum… tempus', 'the right time', enclosing 'pugnae, ne arcessite', with 'pugnae' as genitive."),
 (6, 'n', "Elisions 'magn(um) atque', 'atqu(e) Alpes'.", "Elisions 'n(e) arcessite', 'magn(um) atque', 'atqu(e) Alpes'."),
 # L 25 / 85: Juno repeats Venus's words exactly; let i show it
 (15, 'i', "And Aeneas is far away and knows nothing of it.", "Aeneas is away and knows nothing of it."),
 (50, 'i', "Aeneas is away and knows nothing:", "Aeneas is away and knows nothing of it:"),
 # L 31-33: elision list
 (20, 'n', "Elisions 'tu(a) atque', 'atqu(e) invito'.", "Elisions 'tu(a) atque', 'atqu(e) invito', 'nequ(e) illos'."),
 # L 33-35: '(they came)' and "'sunt' left out" contradicted each other
 (21, 'n', "'sin… secuti', 'but if (they came) having followed', 'sunt' left out, and the sentence breaks off",
           "'sin… secuti', 'but if (they have) followed', 'sunt' left out, and the sentence breaks off"),
 # L 39-41: movet's subject hedged
 (23, 'n', "'movet', the subject is Juno, unnamed.",
           "'movet', the subject is best taken as Juno, unnamed, as her own 'Acheronta movebo' suggests (some make it Allecto)."),
 # L 48-49: elision list; dederit hedged
 (28, 'n', "No elisions.", "Elision 'san(e) ignotis'."),
 (28, 'n', "'whatever way (Fortune) shall have given', future perfect.",
           "'whatever way (Fortune) shall have given', future perfect in sense (the same form is the perfect subjunctive, drawn into the mood of 'sequatur')."),
 # L 51-52a: Idaliae is genitive in the note; l made it an adjective
 (30, 'l', "and the Idalian home:", "and Idalia's house:"),
 (30, 'n', "'Idaliae… domus', 'the house of Idalium', her temple there.",
           "'Idaliae… domus', 'the house of Idalia', genitive of Idalia, another name for Idalium: her temple there."),
 # L 59-60a: framing claim
 (35, 'n', "'supremos', 'last', framing the line with 'cineres': the final embers of the city.",
           "'cineres… supremos', 'the last ashes', noun and adjective enclosing 'patriae insedisse': the final embers of the city."),
 # L 65-66: elision list
 (39, 'n', "Elision 'sequ(i) aut'.", "Elisions 'sequ(i) aut', 's(e) inferre'."),
 # L 72-73a: lines
 (43, 'n', "(line 44–45)", "(lines 44–45)"),
 # MED 81-83: Iliad 5 -- Aphrodite did not get Aeneas away; Apollo hid him and left a phantom
 (48, 'n', "In Iliad 5 Aphrodite carried the wounded Aeneas out of Diomedes' reach, and he was then hidden in a cloud.",
           "In Iliad 5 Aphrodite tried to carry the wounded Aeneas out of the fight, but Diomedes wounded her and she let him fall; Apollo then hid him in a dark cloud and left a phantom of him on the field. Juno gives Venus all the credit."),
 (48, 'n', "Elision 'nebul(am) et'.", "Elisions 'nebul(am) et', 'obtender(e) inanis'."),
 # L 92-93: framing claim
 (56, 'n', "'Dardanius… adulter', 'the Dardan adulterer', Paris, framing the line.",
           "'Dardanius… adulter', 'the Dardan adulterer', Paris, the sneering noun held back to the end of the line."),
]
E2 = []  # pass 2 lives in review_edits_pass2.py
for k, f, old, new in E + E2:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E) + len(E2), 'edits')
