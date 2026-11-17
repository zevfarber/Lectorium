#!/usr/bin/env python3
"""Reviewer's edits to aeneid-095 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n (and one phrase of
'about') are touched; t, ln, p, v, title, titleEn and part never. Run once (it refuses if the file has already been
edited: every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part')}

E = [
 # ---------------- medium: 535 elision list wrong (hiatus at Hyllo, scan-fix 12.535) ----------------
 (42, 'n', "Elisions 'ruent(i) Hyllo', 'Hyll(o) animisque', 'animisqu(e) immane', 'telumqu(e) aurata', 'aurat(a) ad'.",
           "Elisions 'ruent(i) Hyllo', 'animisqu(e) immane', 'telumqu(e) aurata', 'aurat(a) ad'; but 'Hyllo animisque' is a hiatus: the long -o stands in the strong place of the foot and is not elided."),

 # ---------------- medium: distinctive echoes of modern versions ----------------
 (30, 'i', "Was it your will, Jupiter, that nations destined to live in everlasting peace should clash in so great an upheaval?",
           "Jupiter, did it please you that peoples who were to live together in lasting peace should crash against each other in such an upheaval?"),
 (49, 'i', "your lofty home was beneath Ida, your lofty home at Lyrnesus; your tomb is in Laurentine soil.",
           "beneath Ida stood your lofty house, at Lyrnesus your lofty house; your grave lies in Laurentine earth."),

 # ---------------- low: notes ----------------
 (3, 'n', "'gelidus… tremor', 'a cold trembling', framing two lines;",
          "'gelidus… tremor', 'a cold trembling', split across the line round 'per ima cucurrit ossa';"),
 (10, 'n', "Ufens led the Aequi in the catalogue of Book VII.",
           "Ufens led the Aequiculi in the catalogue of Book VII (7.744–749)."),
 (11, 'n', "'in adversos… hostis', -is accusative, framing the line as at 456.",
           "'in adversos… hostis', -is accusative, framing 'telum qui torserat', as it frames 'ductor Rhoeteius' at 456."),
 (15, 'n', "The model is Athena thrusting Sthenelus",
           "The model, from memory, is Athena thrusting Sthenelus"),
 (17, 'n', "The simile is Virgil's own, small and domestic against the din of battle.",
           "No Homeric model comes to mind for it (from memory); it is small and domestic against the din of battle."),
 (33, 'n', "Elision 'congress(u) et'.",
           "'Echionium' has five syllables, E-chī-o-ni-um, and 'Peridiae' four, Pe-ri-dī-ae, the metre requiring a long ī. Elision 'congress(u) et'."),
 (40, 'n', "'avorum', 'of grandfathers', the full genitive.",
           "'avorum', 'of grandfathers', the full genitive. 'atavos' is ă-tă-vos, so 'Murranum' has a long second syllable and 'hic' counts long."),
 (44, 'n', "Cretheus is one of Evander's Arcadians, Greeks by descent.",
           "this Cretheus, a Greek, is presumably one of Evander's Arcadians, not the Trojan Cretheus, the Muses' friend, whom Turnus killed at 9.774–775."),
 (45, 'n', "Cupencus is a priest, and Servius, from memory, says",
           "Cupencus was apparently a priest, since Servius, from memory, says"),
 (47, 'n', "this Aeolus is a Trojan, not the king of the winds in Book I.",
           "this Aeolus is a man of the Troad (his home was Lyrnesus, 547), not the king of the winds in Book I."),
 (51, 'n', "'tendunt', 'they strain, strive',",
           "'requies' has three syllables, re-qui-es. 'tendunt', 'they strain, strive',"),

 # ---------------- low: i tense (narrative in the past, as 094; similes, the poet's questions and the apostrophe keep the present) ----
 (1, 'i', "Antheus and Mnestheus rush out, and the whole host leaves the camp and streams after them:",
          "Antheus and Mnestheus rushed out, and the whole host left the camp and streamed after them:"),
 (2, 'i', "then the plain is lost in a blinding cloud of dust, and the ground, roused by the tramp of feet, quakes.",
          "then the plain was lost in a blinding cloud of dust, and the ground, roused by the tramp of feet, quaked."),
 (5, 'i', "Aeneas flies on,", "Aeneas flew on,"),
 (9, 'i', "Just so the Trojan captain drives his column against the enemy before him, and each man packs close",
          "Just so the Trojan captain drove his column against the enemy before him, and each man packed close"),
 (10, 'i', "Thymbraeus strikes down the massive Osiris with his sword, Mnestheus kills Archetius, Achates cuts down Epulo,",
           "Thymbraeus struck down the massive Osiris with his sword, Mnestheus killed Archetius, Achates cut down Epulo,"),
 (11, 'i', "Tolumnius the augur himself falls,", "Tolumnius the augur himself fell,"),
 (12, 'i', "A shout rises to the sky, and now it is the Rutulians who turn and run,",
           "A shout rose to the sky, and now it was the Rutulians who turned and ran,"),
 (13, 'i', "Aeneas himself does not stoop to lay low the men who turn and run, nor does he go after those who stand to meet him on equal terms or who carry spears against him:",
           "Aeneas himself did not stoop to lay low the men who turned and ran, nor did he go after those who stood to meet him on equal terms or who carried spears against him:"),
 (14, 'i', "Turnus alone he searches for through the thick gloom, scanning every side; Turnus alone he challenges to fight.",
           "Turnus alone he searched for through the thick gloom, scanning every side; Turnus alone he challenged to fight."),
 (15, 'i', "tips Turnus's charioteer Metiscus out from among the reins and leaves him",
           "tipped Turnus's charioteer Metiscus out from among the reins and left him"),
 (16, 'i', "She takes his place herself and guides the rippling reins", "She took his place herself and guided the rippling reins"),
 (19, 'i', "just so Juturna is carried by the horses through the thick of the enemy, flying everywhere in the swift chariot; now here, now there she shows her brother in triumph, but never lets him close with the foe, and wheels away far off the track.",
           "just so Juturna was carried by the horses through the thick of the enemy, flying everywhere in the swift chariot; now here, now there she showed her brother in triumph, but never let him close with the foe, and wheeled away far off the track."),
 (20, 'i', "No less does Aeneas follow", "No less did Aeneas follow"),
 (22, 'i', "Alas, what can he do?", "Alas, what was he to do?"),
 (23, 'i', "In vain he is tossed on a shifting tide, as conflicting cares pull his mind",
           "In vain he was tossed on a shifting tide, as conflicting cares pulled his mind"),
 (24, 'i', "whirls one of them and aims it at him with a sure throw.", "whirled one of them and aimed it at him with a sure throw."),
 (26, 'i', "Then at last his anger rises;", "Then at last his anger rose;"),
 (28, 'i', "he calls again and again on Jupiter and on the altars of the violated treaty to bear witness, and now at last he charges into the thick of them and, terrible with the war-god on his side, stirs up savage slaughter that spares no one, and gives his anger free rein.",
           "he called again and again on Jupiter and on the altars of the violated treaty to bear witness, and now at last he charged into the thick of them and, terrible with the war-god on his side, stirred up savage slaughter that spared no one, and slackened every rein that held his anger."),
 (31, 'i', "Aeneas meets the Rutulian Sucro (his was the first fight that brought the Trojans' charge to a stand) and, since he holds him only briefly, catches him in the side and, where death comes quickest, drives his cruel sword",
           "Aeneas met the Rutulian Sucro (his was the first fight that brought the Trojans' charge to a stand) and, since Sucro held him up only briefly, caught him in the side and, where death comes quickest, drove his cruel sword"),
 (32, 'i', "Turnus, on foot, meets Amycus, thrown from his horse, and his brother Diores; one he strikes with his long spear as he comes on, the other with his sword, then cuts off both their heads, hangs them from his chariot and carries them, dripping with blood.",
           "Turnus, on foot, met Amycus, thrown from his horse, and his brother Diores; one he struck with his long spear as he came on, the other with his sword, then cut off both their heads, hung them from his chariot and carried them, dripping with blood."),
 (33, 'i', "Aeneas sends Talos", "Aeneas sent Talos"),
 (34, 'i', "Turnus kills two brothers", "Turnus killed two brothers"),
 (38, 'i', "with no less fury do the two of them, Aeneas and Turnus, sweep through the battle;",
           "with no less fury did the two of them, Aeneas and Turnus, sweep through the battle;"),
 (39, 'i', "now, now anger surges within them, hearts that cannot learn defeat are near to bursting, now with all their might they go about the work of wounding.",
           "now, now anger surged within them, hearts that had never learned to be beaten were near to bursting, now with all their might they went about the work of wounding."),
 (40, 'i', "Aeneas hurls headlong from his chariot with a rock, the whirling blow of a huge stone, and stretches him on the ground:",
           "Aeneas hurled headlong from his chariot with a rock, the whirling blow of a huge stone, and stretched him on the ground:"),
 (41, 'i', "and the wheels roll him under the reins and yokes, while the hooves of his own horses, forgetting their master, trample him",
           "and the wheels rolled him under the reins and yokes, while the hooves of his own horses, forgetting their master, trampled him"),
 (42, 'i', "Turnus goes to meet Hyllus as he charges in, raging with monstrous fury, and hurls his spear",
           "Turnus went to meet Hyllus as he charged in, raging with monstrous fury, and hurled his spear"),
 (50, 'i', "The whole battle-lines are now turned on each other,", "The whole battle-lines were now turned on each other,"),
 (50, 'i', "every man of them strives for himself with all the strength he has:", "every man of them strove for himself with all the strength he had:"),
 (51, 'i', "there is no pause and no rest; they strain against each other", "there was no pause and no rest; they strained against each other"),
]
for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# the 'about': keep its wording clear of the phrase replaced in the 499 i
ab_old, ab_new = "he gives his anger free rein.", "he lets his anger loose."
assert D['about'].count(ab_old) == 1; D['about'] = D['about'].replace(ab_old, ab_new)

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    assert 15 <= len(u['n'].split()) <= 139, (k, len(u['n'].split()))
A.jdump(D, p)
print(len(E) + 1, 'edits applied')
