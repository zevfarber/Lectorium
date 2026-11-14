#!/usr/bin/env python3
"""Reviewer's edits to aeneid-075 units.json (pass 1). Each edit: (unit index, field, old, new);
old must occur exactly once in that field. Only l, i, n (and the part's 'about') are touched; t never. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # MED 276-277: IX.126 comes after the ships have become nymphs (IX.77-122), not before; dative label; elision typo
 (0, 'n', "where Turnus faced the Trojan ships before they became nymphs.",
          "where Turnus kept his nerve after the Trojan ships had turned into nymphs."),
 (0, 'n', "'audaci Turno' a dative of possession:", "'audaci Turno' a dative of reference, where English uses a possessive:"),
 (0, 'n', "Elision 'praecipir(e) et'.", "Elision 'praeciper(e) et'."),
 # L 279: votis (scan-fixes 10.279)
 (1, 'n', "'Quod votis optastis', 'what you have longed for in your prayers';",
          "'Quod votis optastis', 'what you have longed for in your prayers' ('votis' with long 'o', from 'voveo');"),
 # L 280-282a: quisque is the subject of referto too (third person)
 (3, 'l', "each man, his own, and of his home mindful; now the great call back\ndeeds, the glories of your fathers.",
          "each man, his own, and of his home mindful; now the great let him recall\ndeeds, the glories of the fathers."),
 (3, 'i', "now call to mind the great deeds and glories of your fathers.",
          "now let him call to mind the great deeds, the glories of his fathers."),
 (3, 'n', "'esto' and 'referto' are future imperatives, the solemn form of command used in laws and formal orders: 'let each man be…', 'call back'.",
          "'esto' and 'referto' are third-person future imperatives, both with 'quisque' as subject, the solemn form of command used in laws and formal orders: 'let each man be…', 'let him recall'."),
 # L 287: Aeneas (scan-fixes 10.287) already in the note. 309: Teucros already noted.
 # L 310b-313a: Aeneas/Aenean (scan-fixes 10.311, 10.313)
 (14, 'n', "'Aenean', Greek accusative;", "'Aenean', Greek accusative ('Ae-' one syllable here and in 'Aeneas' above);"),
 # MED 313b-314: i made Aeneas, not the sword, 'drink'; l word order
 (15, 'i', "he drove his sword through the bronze-linked mail and the tunic stiff with gold, and drank from the side he laid open.",
           "he drove his sword through the bronze-linked mail, through the tunic stiff with gold, and drained the blood from his side, laid open."),
 (15, 'l', "through the tunic rough with gold, in the side he drains, laid open.",
           "through the tunic rough with gold, the side he drains, laid open."),
 # L 315-317a: casus accusative plural; Phoebe short e (scan-fixes 10.316)
 (16, 'n', "'casus… ferri', 'the hazards of the steel', the surgeon's blade.",
           "'casus… ferri', 'the hazards of the steel', the surgeon's blade, 'casus' accusative plural, object of 'evadere'."),
 # L 333-335a: wording of the relative
 (24, 'n', "'steterunt quae', 'which stood (fixed)', the relative clause after its sense;",
           "'steterunt quae', 'which stood (fixed)', the relative 'quae' placed after its verb, its antecedent the spears understood from 'ullum';"),
 # L 336b-337: thoraca (scan-fixes 10.337)
 (26, 'n', "'thoraca', Greek accusative of 'thorax', 'breastplate'.",
           "'thoraca', Greek accusative of 'thorax', 'breastplate' (tho-ra-ca, the first two syllables long)."),
 # L 342-344: Achatae is an ordinary first-declension genitive of a Greek name in -es; Aenean (scan-fixes 10.343)
 (29, 'n', "'magni… Achatae', 'of great Achates', the Greek genitive in '-ae';",
           "'magni… Achatae', 'of great Achates', genitive in '-ae', the Greek name in '-es' declined in the first declension;"),
 (29, 'n', "'Aenean', Greek accusative;", "'Aenean', Greek accusative, 'Ae-' one syllable;"),
 # L 352b-354a: Halaesus as Book VII has him (VII.723 'Agamemnonius, Troiani nominis hostis')
 (32, 'n', "Halaesus appears in the catalogue of Book VII as a follower of Agamemnon's line who settled in Italy;",
           "Halaesus appears in the catalogue of Book VII as 'Agamemnonius', of Agamemnon's house or following, an enemy of the Trojan name;"),
 # L 356b-359: magno... aethere encloses only discordes; i rephrased (less stock wording, no 'locked' repeated in 361)
 (34, 'n', "'magno… aethere', 'in the great upper air', framing 'discordes… venti', 'warring winds'.",
           "'magno… aethere', 'in the great upper air', enclosing 'discordes', with 'venti', 'the winds', after it: 'winds at strife'."),
 (34, 'i', "As when, in the vast sky, warring winds raise battle against one another with equal spirit and equal strength, and neither they themselves nor the clouds nor the sea will give ground, the fight hangs long in doubt, and everything stands locked in resistance:",
           "As when, in the great sky, winds at odds with one another stir up battle, matched in spirit and in strength, and neither the winds themselves nor the clouds nor the sea give way, and the struggle stays long undecided, everything braced and straining against everything:"),
 # L 360-361: i rephrased away from stock phrasing
 (35, 'i', "foot is locked against foot, and man pressed close on man.",
           "foot holds fast against foot, and man is crowded hard on man."),
]
for k, f, old, new in E:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
old = "Aeneas calls for the spears he once threw at the Greeks and kills two of the brothers, while a third only grazes Achates."
assert D['about'].count(old) == 1
D['about'] = D['about'].replace(old, "Aeneas calls for the spears that once stood in Greek bodies at Troy, kills one brother and cripples another's arm, while a third, aiming back, only grazes Achates.")
A.jdump(D, p)
print('applied', len(E) + 1, 'edits')
