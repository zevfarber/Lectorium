#!/usr/bin/env python3
"""Reviewer's edits to aeneid-094 units.json (passes 1 and 2; run once from the drafter's file).
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
 # ---------------- medium: Iasides note contradicted the house scansion (5.843 Ia-si-de, scanner kept at 392) -------
 (29, 'n', "'Iasides', 'son of Iasus', a Greek patronymic, likewise beginning with a vowel.",
           "'Iasides', 'son of Iasus', a Greek patronymic, read here as three long syllables, Ia-si-des, as 'Iaside' at 5.843."),

 # ---------------- medium: distinctive echoes of modern versions in the farewell (435-440) ----------------
 (44, 'i', "“Learn from me, my boy, what manhood is, and what real labour is; learn about good fortune from others.",
           "“Learn from me, my boy, what it is to be a man and to labour in earnest; for good fortune, look to others."),
 (45, 'i', "For now my right hand will keep you safe in war and lead you to great rewards.",
           "For now my own hand will keep you from harm in battle and bring you among great prizes."),
 (46, 'i', "And you, when before long your years have ripened, make sure that you remember; and as you call to mind the examples of your own people, let your father Aeneas and your uncle Hector stir you on.”",
           "And you, when before long your years have ripened, see to it that you keep this in mind; and as your thoughts go back to the examples of your kin, may your father Aeneas and your uncle Hector wake your courage.”"),

 # ---------------- low: notes ----------------
 # 311: dextram ... inermem frames the verb, not the line (At pius Aeneas come first)
 (0, 'n', "'dextram… inermem', 'his unarmed right hand', framing the line, a sign of peace.",
          "'dextram… inermem', 'his unarmed right hand', framing 'tendebat', a sign of peace."),
 # 330: raptas ... hastas frames fugientibus ingerit, not the line (proterit aut come first)
 (8, 'n', "perhaps lying on the field, framing the line.", "perhaps lying on the field, framing 'fugientibus ingerit'."),
 # 336: Insidiae is 'Ambush' in l and i; the note said 'Treachery'
 (10, 'n', "with Wrath and Treachery as persons,", "with Wrath and Ambush as persons,"),
 # 336: comma splice in i
 (10, 'i', "than the South Winds and the West, the farthest reaches", "than the South Winds and the West; the farthest reaches"),
 # 349: scansion pointer (scan-fix 12.349)
 (13, 'n', "'Danaum', old genitive plural.", "'Danaum', old genitive plural, three syllables, Da-na-um."),
 # 363: the lengthened -que of Chloreaque is not mentioned
 (19, 'n', "'sternacis', 'apt to throw its rider', from 'sterno'.",
           "'sternacis', 'apt to throw its rider', from 'sterno'. The '-que' of 'Chloreaque' is lengthened in the strong place of the foot, a Homeric licence in lists (as 3.91 'liminaque laurusque')."),
 # 370: l made the crest the subject of 'shakes'
 (21, 'l', "and his crest, against the chariot, shakes the breeze, flying.",
           "and his crest, as the chariot meets it, the breeze shakes, flying."),
 # 371: scansion pointer (scan-fix 12.371)
 (22, 'n', "'eu' is one syllable, the Greek diphthong, Phe-geus.", "'eu' is one syllable, the Greek diphthong, Phē-geus, with a long first syllable, as at 5.263."),
 # 386: the accusative gressus is not explained
 (27, 'n', "'nitentem', 'leaning', with the ablative 'cuspide': the spear serves as a staff.",
           "'nitentem', 'leaning', with the ablative 'cuspide' and 'gressus' as its object, 'propping his steps': the spear serves as a staff."),
 # 395: elision list missed Ill(e) ut
 (30, 'n', "Elisions 'herbar(um) usumque', 'agitar(e) inglorius'.", "Elisions 'Ill(e) ut', 'herbar(um) usumque', 'agitar(e) inglorius'."),
 # 406: saevus ... horror sits inside one line
 (33, 'n', "'saevus… horror', 'savage dread', split across the line:", "'saevus… horror', 'savage dread', framing 'campis magis ac magis':"),
 # 417: the basin is labrum (from lavo), not the lip
 (37, 'n', "'labrum' a basin with a lip;", "'labrum' here 'basin, tub' (lābrum, from 'lavo'), not 'lip';"),
 # 422: the long final syllable of dolor
 (38, 'n', "'stetit', 'stood still', stopped.",
           "'stetit', 'stood still', stopped. 'dolor' has its last syllable lengthened at the pause, in the strong place of the foot, dŏ-lōr | ōm-nis."),
 # 427: scansion pointer (scan-fix 12.427)
 (41, 'n', "'humanis opibus', 'by human resources'.", "'humanis opibus', 'by human resources', hū-mā-nis ŏ-pi-bus."),
 # 440: the last line repeats 3.343
 (46, 'n', "The singular verb agrees with the nearer subject.",
           "The singular verb agrees with the nearer subject. The line repeats 3.343, Andromache's question about the boy, with 'excitet' for 'excitat'."),

 # ---------------- low: i in the narrative tense (past), as aeneid-093 ----------------
 (7, 'i', "He calls at once for his horses and his armour, leaps proudly up into his chariot and takes the reins in his hands.",
          "He called at once for his horses and his armour, leapt proudly up into his chariot and took the reins in his hands."),
 (8, 'i', "Racing over the field he gives many brave men's bodies to Death; many he sends rolling half-dead, or he crushes whole files beneath his chariot, or snatches up spears and hurls them at those who run.",
          "Racing over the field he gave many brave men's bodies to Death; many he sent rolling half-dead, or he crushed whole files beneath his chariot, or snatched up spears and hurled them at those who ran."),
 (11, 'i', "so Turnus, eager, drives his horses, steaming with sweat, through the thick of the fighting, trampling cruelly on the enemies he has killed; the flying hooves spatter a bloody dew, and the gore is trodden into the sand.",
           "so Turnus, eager, drove his horses, steaming with sweat, through the thick of the fighting, trampling, a piteous sight, on the enemies he had killed; the flying hooves spattered a bloody dew, and the gore was trodden into the sand."),
 (13, 'i', "Elsewhere Eumedes charges into the thick of the battle,", "Elsewhere Eumedes charged into the thick of the battle,"),
 (19, 'i', "He sends Asbytes to keep him company,", "He sent Asbytes to keep him company,"),
 (21, 'i', "so, wherever Turnus cuts his way, the ranks give before him and the lines turn and run; his own momentum carries him on, and the wind that meets the chariot shakes his streaming crest.",
           "so, wherever Turnus cut his way, the ranks gave before him and the lines turned and ran; his own momentum carried him on, and the wind that met the chariot shook his streaming crest."),
 (24, 'i', "While he is dragged along, hanging from the yoke with his body exposed, Turnus's broad lance catches him, drives in and bursts his corselet of double mail, and with a wound just grazes the surface of his flesh.",
           "While he was dragged along, hanging from the yoke with his body exposed, Turnus's broad lance caught him, drove in and burst his corselet of double mail, and with a wound just grazed the surface of his flesh."),
 (28, 'i', "He rages, and struggles to pull out the weapon whose shaft has snapped, and calls for the nearest way to help:",
           "He raged, and struggled to pull out the weapon whose shaft had snapped, and called for the nearest way to help:"),
 (32, 'i', "tries one thing after another, all in vain, with his skilled hand and the potent herbs of Phoebus; in vain he works at the arrowhead with his right hand and grips the iron with clinging forceps.",
           "tried one thing after another, all in vain, with his skilled hand and the potent herbs of Phoebus; in vain he worked at the arrowhead with his right hand and gripped the iron with clinging forceps."),
 (33, 'i', "No good fortune shows the way, and Apollo, the author of the art, gives no help at all; and out on the plain the savage terror swells more and more, and the danger draws nearer.",
           "No good fortune showed the way, and Apollo, the author of the art, gave no help at all; and out on the plain the savage terror swelled more and more, and the danger drew nearer."),
 (34, 'i', "Already they see the sky stand thick with dust; the horsemen are coming up, and darts are falling thick",
           "Already they saw the sky stand thick with dust; the horsemen were coming up, and darts were falling thick"),
 (35, 'i', "A grim cry rises to the sky", "A grim cry rose to the sky"),
 (36, 'i', "plucks dittany from Ida in Crete,", "plucked dittany from Ida in Crete,"),
 (40, 'i', "shouts Iapyx, and he is the first to fire their courage", "shouted Iapyx, and he was the first to fire their courage"),
 (42, 'i', "he hates delay, and makes his spear flash.", "he hated delay, and made his spear flash."),
 (43, 'i', "Once the shield is fitted to his side and the corselet to his back, he folds Ascanius in his armoured embrace and, kissing him lightly through the helmet, says:",
           "Once the shield was fitted to his side and the corselet to his back, he folded Ascanius in his armoured embrace and, kissing him lightly through the helmet, said:"),
]
for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# the 'about': Aeneas kisses the boy through the helmet; he does not embrace him through it
ab_old, ab_new = "embraces Ascanius through his helmet:", "embraces Ascanius and kisses him through his helmet:"
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
