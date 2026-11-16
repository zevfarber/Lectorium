#!/usr/bin/env python3
"""Reviewer's edits to aeneid-084 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n are
touched; t, ln, p, v and the top-level fields never. Run once (it refuses if the file has already been
edited: every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

E = [
 # ---------------- medium ----------------
 # D1 'tumuli... recentes' is nominative plural, a second subject; l made it a genitive 'of the mound'
 (3, 'l', "warns him the anger of the gods, and of the mound before his eyes the fresh ones.",
          "warns him the anger of the gods, and the mounds before his eyes, fresh ones."),
 # D2 l reversed subject and object; note muddled who took what from whom; 'possedit' claim softened
 (20, 'l', "conquered Asia lay in wait for the adulterer.", "for conquered Asia lay in wait the adulterer."),
 (20, 'n', "Asia was defeated, and the adulterer, Aegisthus, took the victory from it. Some editors read 'possedit', 'took possession of', which changes the sense: 'the adulterer won what Agamemnon had conquered'. Greenough's reading is kept.",
           "Asia was conquered, and the adulterer, Aegisthus, lay in wait for its conqueror. Some texts are said to read 'possedit', 'took possession of', which changes the sense: 'the adulterer won what Agamemnon had conquered'. Greenough's reading is kept."),
 # D3 'turbata' (neuter plural) agrees with 'ora', not with masculine 'fremor'
 (35, 'n', "a noise of many voices saying different things; the adjective and noun stand at either end, 'turbata', 'troubled', agrees with 'fremor'. 'per ora cucurrit', 'ran through the mouths'. 'Ausonidum', genitive plural of 'Ausonides', 'the sons of Ausonia', with the short '-um' ending.",
           "a noise of many voices saying different things; the adjective and noun stand at either end. 'per ora cucurrit… turbata', 'ran through the troubled mouths': 'turbata' is neuter plural with 'ora', not with 'fremor'. 'Ausonidum', genitive plural of 'Ausonides', 'the sons of Ausonia', the old '-um' for '-arum'."),
 (35, 'l', "of the Ausonians, troubled, roaring:", "of the Ausonians, troubled ones, a roar:"),
 (35, 'i', "a confused murmur of alarm ran from mouth to mouth among the Ausonians:",
           "a confused murmur passed from one troubled mouth to the next among the Ausonians:"),
 # D4 'coeant' has its ordinary three syllables here (dactyl or co-e); the drafter's synizesis is the scanner's error
 (32, 'n', "'Coeant' is two syllables in the verse, 'coe-' read as one.",
           "'Coeant' has its ordinary three syllables, 'co-e-ant'."),
 # D5 in Virgil Orestes kills Neoptolemus at his father's altars (III.332), not at Delphi
 (17, 'n', "he was killed by Orestes at Delphi, and part of his realm passed to Helenus (III.325–336).",
           "he was cut down by Orestes 'at his father's altars' (III.330–332), and part of his realm passed to Helenus (III.333–336)."),
 # D6 Diomedes wounded Ares as well as Aphrodite in Iliad 5; 'for Venus alone' is not safe
 (23, 'n', "'caelestia corpora', 'heavenly bodies', the poetic plural for Venus alone.",
           "'caelestia corpora', 'heavenly bodies', a generalising plural: in Iliad 5 he wounded Ares as well, though only Venus is named here."),
 # D7 'Diomedem' is the Latin third-declension accusative, not a Greek one
 (9, 'n', "'Diomedem', Greek accusative.", "'Diomedem', accusative of 'Diomedes', declined as a Latin third-declension noun."),
 # D8 nested speech: Diomedes' words in single marks in l/i, closed at 'cavete' (house handling of VIII.499-503)
 (13, 'l', "“O fortunate peoples, Saturnian kingdoms,", "‘O fortunate peoples, Saturnian kingdoms,"),
 (13, 'i', "“O happy peoples,", "‘O happy peoples,"),
 (13, 'n', "Diomedes' words, quoted by Venulus; the print opens them with a second opening mark inside Venulus's speech and closes both with a single mark at 295.",
           "Diomedes' words, quoted by Venulus. The print opens them with a second opening mark inside Venulus's speech and prints none where they end (293); l and i give them in single marks, closed at 'cavete', as for the soothsayer inside Evander's speech (VIII.499–503)."),
 (33, 'l', "but that with arms clash arms, beware.", "but that with arms clash arms, beware.’"),
 (33, 'i', "but beware of letting arms clash with arms.", "but beware of letting arms clash with arms.’"),
 (33, 'n', "'armis… arma', the same noun twice, side by side with the verb between, the clash shown in the words. This is the last of Diomedes' words; the print marks no close, and 294–295 return to Venulus.",
           "'armis… arma', the same noun in two cases with the verb between them, the clash shown in the words. This is the last of Diomedes' words; the print marks no close here, l and i do, and 294–295 return to Venulus."),
 (34, 'n', "The print puts a single closing mark here for both speeches, Diomedes' and Venulus's: Diomedes' words end at 293.",
           "The print's single closing mark here ends Venulus's speech; Diomedes' words, quoted inside it, ended at 293."),

 # ---------------- low: notes ----------------
 (0, 'n', "'medio in flagrante tumultu', 'in the blazing middle of the tumult'.",
          "'medio in flagrante tumultu', 'in the middle of the blazing tumult', all three words ablative."),
 (1, 'n', "'nil… valuisse', 'that nothing… had availed', with 'nil' as an adverbial 'not at all'.",
          "'nil… valuisse', 'had availed nothing', with 'dona', 'aurum' and 'preces' as subjects and 'nil' adverbial, 'not at all'."),
 (8, 'n', "always introducing speech.", "regularly introducing speech."),
 (16, 'n', "met by Ulysses in Odyssey 9 and by Aeneas in III.588–681. No elisions.",
           "met by Ulysses in Odyssey 9 and by Aeneas in III.588–681; 'Cyclopas', Greek accusative plural, its '-as' short. Elisions 'Militi(a) ex', 'divers(um) ad'."),
 (22, 'n', "'petierunt', the full perfect, with '-erunt'.",
           "'petierunt' = 'petiverunt', the perfect in '-erunt' (not '-ere'), its e long."),
 (25, 'n', "both verbs taking the genitive 'veterum… malorum'.",
           "both verbs taking the genitive 'veterum… malorum' (with 'laetor', which usually has the ablative, a poetic extension)."),
 (31, 'n', "most editions put a semicolon there, and the reading text marks the pause.",
           "editions generally punctuate there, and the reading text marks the pause."),
 (34, 'n', "'magno… bello', dative, 'for the great war', or ablative, 'on the war'.",
           "'magno… bello', dative of reference, 'regarding the great war'."),
 (36, 'n', "the simile has its ancestors in Homer's river similes, but no single model.",
           "Homer has similes of roaring water like this one, but no single model is certain."),
 (48, 'n', "'finis super usque Sicanos', 'beyond, all the way past the boundaries of the Sicanians', 'finis' accusative plural;",
           "'finis super usque Sicanos', 'beyond the borders, right on to the Sicanians', 'super' after its noun, 'finis' accusative plural (some take 'Sicanos' with 'finis', 'beyond the Sicanian borders');"),
 (53, 'n', "The print sets no stops after 'navis' or 'materies', so the lines run on;",
           "The print has no mark after 'navis' and only a comma after 'materies', so the lines run on;"),

 # ---------------- low: l construal and layout ----------------
 (12, 'l', "Having heard, he these things with calm thus returned from mouth:",
           "Having heard, he these things, with calm, thus gave back, mouth:"),
 (18, 'l', "Of Libya on the shore living the Locrians?", "On the Libyan, living, shore, the Locrians?"),
 (19, 'l', "Himself the Mycenaean, of the great leader of the Achaeans,",
           "Himself the Mycenaean, of the great, the leader, Achaeans,"),
 (21, 'l', "my longed-for wife and fair Calydon I should see!", "my longed-for wife and fair Calydon I should see?"),
 (25, 'l', "nor for me with the Teucrians any after the overthrown war", "nor for me with the Teucrians any, after overthrown, war"),
 (37, 'l', "from the throne the king begins high:", "from the throne the king begins, high:"),
 (39, 'l', "whom no weary\nbattles:", "whom no wear out\nbattles:"),

 # ---------------- low: i accuracy and echo recasts ----------------
 (25, 'i', "and I take no pleasure in remembering the evils of the past.",
           "and the evils of the past I neither dwell on nor delight in."),
 (30, 'i', "that the Greeks' victory was held fast", "that the Greeks' victory was held up"),
 (39, 'i', "We are waging an ill-starred war,", "We are waging an ill-timed war,"),
 (42, 'i', "Each man must be his own hope; but you see how slender a hope that is;",
           "Each of you has only himself to hope in; but you see how slender a hope that is;"),
 (48, 'i', "stretching far to the west beyond the borders of the Sicanians;",
           "stretching far to the west, past the borders and on as far as the Sicanians;"),
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
    so = sum(u[lay].count('‘') for u in U); sc = sum(u[lay].count('’') for u in U)
    assert o == c == 2 and so == sc == 1, (lay, o, c, so, sc)
A.jdump(D, p)
print('applied', len(E), 'edits')
