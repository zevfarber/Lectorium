#!/usr/bin/env python3
"""Reviewer's edits to aeneid-077 units.json (pass 1). Each edit: (unit index or 'about', field, old, new);
old must occur exactly once in that field. Only l, i, n (and the part's 'about') are touched; t never. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # M 439-440: 438 is the poet's statement, not Jupiter's; Lausus and Pallas face each other but are kept apart (433-438)
 (0, 'n', "Lausus is fighting Pallas (last part).", "Lausus faces Pallas across the battle (433–434)."),
 (0, 'n', "Jupiter has just said that Pallas and Lausus will fall to greater enemies (438):",
          "The poet has just said that Pallas and Lausus will fall to a greater enemy (438):"),
 # L 441-443: 'vidit' is 'saw'; 'ut' + perfect 'as soon as'
 (1, 'i', "When he reached his comrades, he cried,", "As soon as he saw his comrades, he cried,"),
 # L 445-448: 'tyranni' is the narrator's word, seen from Pallas's side, not spoken by him
 (3, 'n', "with a hostile edge in Pallas's mouth.", "with a hostile edge here, the narrator seeing Turnus as Pallas sees him."),
 # L 449-451a: i dropped 'iam'
 (4, 'i', "“I shall be praised either for winning the richest spoils",
          "“Now I shall be praised either for winning the richest spoils"),
 # L 451b: 'Fatus' is 'having spoken'; 'present sense' contradicted the gloss
 (5, 'n', "the perfect participle of the deponent 'for', used with present sense.",
          "the perfect participle of the deponent 'for', active in meaning like all deponents."),
 # L 453-454a: biiugis was at 399 in the last part, not 400; add the quantity (scan-fixes 10.453)
 (7, 'n', "three syllables with the second 'i' a consonant, as at 400 in the last part.",
          "three syllables with the second 'i' a consonant and 'bi-' short, as at 399 in the last part."),
 # L 457-459: 'qua' is the adverb, long, as the metre shows
 (9, 'n', "'siqua' = 'si qua', 'if in any way',", "'siqua' = 'si qua', 'if in any way' ('qua' the adverb, with a long 'a'),"),
 # M 462-463: wrong nominative given for semineci
 (11, 'n', "'semineci' is from 'semineci-s', 'half-dead'.", "'semineci' is the dative of 'seminex' (genitive 'seminecis'), 'half-dead'."),
 # L 464-465: magnum... gemitum encloses 'sub imo corde premit', not 'the next line and a half'; Zeus's 'tears of blood' are bloody raindrops
 (12, 'n', "'magnum… gemitum', 'a great groan', framing the next line and a half.",
           "'magnum… gemitum', 'a great groan', enclosing 'sub imo corde premit'."),
 (12, 'n', "sheds tears of blood (Iliad 16.459–461);", "lets fall drops of bloody rain on the earth (Iliad 16.459–461);"),
 # L 467-469a: i recast away from familiar published wording ('Every man has his appointed day', 'to lengthen fame')
 (14, 'i', "“Every man has his appointed day; for all men the span of life is short, and once gone it can never be restored; but to make one's name outlast one by what one does, that is what courage is for.",
           "“For every man his own day stands fixed; for all, life's time is short and cannot be made good once spent; but to stretch one's renown further by deeds is the work that courage has to do."),
 # L 469b-471a: l line 1 lost the genitive
 (15, 'l', "Troy beneath the walls high", "Of Troy beneath the walls high"),
 # MAJOR 471b-472: pervenit is the perfect (pervēnit), as the metre shows, not the present
 (16, 'n', "'pervenit ad', 'arrives at', present tense: he is already near it.",
           "'pervenit ad', 'has arrived at', perfect: the metre needs the long 'e' of 'pervēnit' (the present is 'pervĕnit'). His end is as good as come."),
 # M 473: the doubtful 'reicit arvis' stated honestly; 'fits his grief' was not grounded
 (17, 'n', "'oculos… reicit arvis', 'turns his eyes away from the fields', 'arvis' taken as an ablative of separation: Jupiter will not watch what follows. Some take 'arvis' as dative and the line to mean that he turns his eyes back to the battlefield; the sense of turning away fits his grief better.",
           "'oculos… reicit arvis' is read two ways. Here 'arvis' is taken as an ablative of separation, 'turns his eyes away from the fields': Jupiter will not watch what follows, as Zeus at the start of Iliad 13 turns his eyes away from the fighting at Troy. Others take 'arvis' as dative, 'turns his eyes back onto the fields', to the battle he must let run its course. The Latin allows both."),
 # L 474-475: the line echoed is 414, 'fulgenti deripit ense'
 (18, 'n', "'deripit', 'snatches off', the same verb Halaesus used of a hand at 415.",
           "'deripit', 'snatches off'; 'fulgentem deripit ensem' echoes 'fulgenti deripit ense' at 414, where Halaesus lops off a hand."),
 # L 486: calidum... telum does not frame the line (Ille rapit before it)
 (23, 'n', "'calidum… telum', 'the warm weapon', framing the line,", "'calidum… telum', 'the warm weapon', enclosing 'frustra de volnere',"),
 # L 487: sanguis with its last syllable long (the scansion shows it)
 (24, 'n', "'sanguis animusque', 'blood and life',", "'sanguis animusque', 'blood and life' ('sanguis' with its last syllable long, an old quantity),"),
 # L 495b-499: one Danaid, Hypermestra, spared her husband
 (30, 'n', "killed their husbands on the wedding night.", "all but one of them killed their husbands on the wedding night."),
 # L 501-502: i recast away from familiar published wording ('blind', 'the minds of men ... fate')
 (32, 'i', "How blind the minds of men are to fate and to what lies ahead, and how unable to keep within bounds when good fortune raises them high!",
           "How little the human mind knows of fate and of the lot that is coming, or of holding to the mean when prosperity has carried it aloft!"),
 # L 503-505a: i recast ('to have left Pallas untouched' is stock)
 (33, 'i', "A time will come for Turnus when he would give a great price to have left Pallas untouched, when he will hate those spoils and this day.",
           "For Turnus a time will come when he would pay a great price to buy back Pallas unharmed, and will loathe those spoils and this day."),
 # M 507-509: dolor and decus are in apposition to the vocative, not 'nominatives in exclamation'; i recast away from 'grief and glory'
 (35, 'n', "'grief and great glory', in alliteration, nominatives in exclamation;",
           "'grief and great glory', in alliteration, in apposition to the vocative (for these nouns the two cases look alike);"),
 (35, 'i', "O you who will go home to your father, his great grief and his great glory! This day, your first, gave you to war, and this same day takes you away, though you leave behind you great heaps of Rutulian dead.",
           "O you who go home to your father to be his great sorrow and his great pride! This first day of yours gave you to the war, and this same day carries you off, though you leave great heaps of Rutulian dead behind you."),
 # L about: rephrase two stock phrasings; 'home' and 'taken by war' corrected
 ('about', None, "every man's day is fixed, and the work of courage is to lengthen one's name by deeds.",
                 "each man's day stands fixed, and courage's task is to carry one's name further by deeds."),
 ('about', None, "The Arcadians carry Pallas home on his shield, a great grief to his father and a great glory, given to war and taken by it on the same first day.",
                 "The Arcadians carry Pallas back on his shield, a great sorrow to his father and a great pride, given to the war and carried off by the same day, his first."),
]
for k, f, old, new in E:
    s = D['about'] if k == 'about' else U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    if k == 'about': D['about'] = s.replace(old, new)
    else: U[k][f] = s.replace(old, new)
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
A.jdump(D, p)
print('applied', len(E), 'edits')
