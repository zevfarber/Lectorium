#!/usr/bin/env python3
"""Reviewer's edits to aeneid-078 units.json (pass 1). Each edit: (unit index or 'about', field, old, new);
old must occur exactly once in that field. Only l, i, n (and the part's 'about') are touched; t never. Run once."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]

# MAJOR M1: 'Mago' (521) is the dative of Magus, -i; the man is Magus. Every English mention is renamed
# (l, i, n, about); the Latin form stays quoted as 'Mago' only where the note parses it (unit 4).
n_mago = 0
for k, u in [('about', None)] + list(enumerate(U)):
    for f in (['about'] if k == 'about' else ['l', 'i', 'n']):
        s = D['about'] if k == 'about' else u[f]
        new = re.sub(r"\bMago\b", 'Magus', s)
        n_mago += len(re.findall(r"\bMago\b", s))
        if k == 'about': D['about'] = new
        else: u[f] = new

E = [
 # M1 (cont.) 521: the note parses the form
 (4, 'n', "'Magus', dative, 'at Magus', with 'contenderat'",
          "'Mago', dative of 'Magus' (second declension), 'at Magus', with 'contenderat'"),
 # L 510-512: l 'And now no' blurred 'Nec iam' ('no longer')
 (0, 'l', "And now no rumour of so great a disaster,", "And no longer a rumour of so great a disaster,"),
 # L 510-512: 'ablative of measure' is not the construction; it describes their situation
 (0, 'n', "'tenui discrimine leti', 'by a thin margin of death', ablative of measure: a 'discrimen' is the dividing line.",
          "'tenui discrimine leti', 'by a thin margin of death', an ablative describing their situation: a 'discrimen' is the dividing line, here between life and death."),
 # L 517-520: the Sulmo of IX.412 is one of Volcens' Latin horsemen, not called Rutulian; line refs added
 (3, 'n', "(a Rutulian Sulmo dies in Book IX)", "(a Sulmo is killed in Book IX, IX.412)"),
 (3, 'n', "the sacrifice is carried out in Book XI.", "the sacrifice is carried out in Book XI (XI.81–82)."),
 (3, 'n', "'whom the Ufens rears', a river of Latium,", "'whom the Ufens rears', a river of Latium (VII.802), not here the leader Ufens of VII.745,"),
 # L 535-536: 'present sense' contradicts the gloss 'having so spoken' (as 077 L4)
 (14, 'n', "'Sic fatus', 'having so spoken', the deponent participle with present sense.",
           "'Sic fatus', 'having so spoken', the perfect participle of the deponent 'for', active in meaning like all deponents."),
 # M 537-539: Greenough's archaic 'redimibat' unexplained; 'sacra' is ablative with 'vitta' (the metre needs crā; scan-fixes 10.538)
 (15, 'n', "'cui… tempora', 'whose temples', dative of reference.",
           "'cui… tempora', 'whose temples', dative of reference. 'redimibat' = 'redimiebat', the old imperfect of a fourth-conjugation verb. 'sacra… vitta', ablative, 'with the sacred ribbon': the metre shows the long final 'a'."),
 # L 541-542: the trophy words recur at XI.7-8
 (17, 'n', "as Aeneas does with Mezentius's at the start of Book XI.",
           "as Aeneas does with Mezentius's at the start of Book XI, where the words come back: 'tibi, magne, tropaeum, bellipotens' (XI.7–8)."),
 # L 545-546: totum... orbem does not frame the line ('et' first)
 (19, 'n', "'totum clipei… orbem', 'the whole circle of the shield', framing the line.",
           "'totum clipei… orbem', 'the whole circle of the shield', enclosing 'clipei ferro deiecerat'."),
 # M 547-549 (drafter's open point): the 'spell or vow' suggestion is unsupported; give the plain sense
 (20, 'n', "Perhaps a spell or a vow is meant, a word with power in it.",
           "That is, he trusted that what he boasted would come true."),
 # L 552-553: 'reducta' is drawn back for the stroke; thrust or throw is not said
 (22, 'n', "he draws it back to throw.", "he draws it back for the stroke."),
 # L 554-556: 'deturbat caput' with 'truncum' is a beheading
 (23, 'i', "Aeneas struck his head to the ground,", "Aeneas struck his head off to the ground,"),
 # L 557: the sc will show the last syllable of 'iace' long, at the pause under the beat
 (24, 'n', "'iace', imperative, 'lie'.", "'iace', imperative, 'lie', its final 'e' counting long here, at the pause where the beat falls."),
 # L 557-558: 'optima mater' is 'your excellent mother' (the note's irony), not 'no loving mother'
 (25, 'i', "No loving mother will lay you in the earth", "Your fine mother will not lay you in the earth"),
 # L 561-564: the Camers inconsistency stated exactly (XII.224 is Juturna taking his form); Numa killed at IX.454; Amyclae story attributed vaguely
 (27, 'n', "A Camers appears alive again in Book XII; Virgil left such details unrevised at his death.",
           "In Book XII Juturna takes the form of a Camers as if he were still living (XII.224), and a Numa was already killed in Book IX (IX.454): small inconsistencies in a poem left unrevised at Virgil's death."),
 (27, 'n', "the old story is that,", "an old story told by the ancient commentators is that,"),
 # L 565-568: l made 'breasts' a subject of 'blazed'; 'pectoribusque' goes with 'oribus'
 (28, 'l', "and breasts blazed,", "and from breasts blazed,"),
 # M 570-571: 'consonantal i written double' is false: quadri- + iugum, a vowel i then a consonantal i
 (30, 'n', "'quadriiugis' has the consonantal 'i' written double, as 'biiugis' (575).",
           "'quadriiugis' is 'quadri-' + 'iugum': the first 'i' a vowel, the second a consonant, so qua-dri-iu-gis, four syllables; so too 'biiugis' (575)."),
 # M 572-574: n reads 'longe gradientem' as long strides (Homer's 'striding long'), l/i read 'from afar'; aligned to n
 (31, 'n', "'longe gradientem', 'striding long', with great steps.",
           "'longe gradientem', 'striding long', with great steps, like a Homeric hero coming on 'with long strides'."),
 (31, 'l', "And they, him from afar striding and dreadful things roaring,",
           "And they, him with long strides advancing and dreadful things roaring,"),
 (31, 'i', "when they saw him striding at them from far off with a terrible roar,",
           "when they saw him coming on with long strides and roaring terribly,"),
 # M 575-576: same false label; biiugis... albis does not frame the line ('Interea' first)
 (32, 'n', "ablative, framing the line; 'biiugis' has the doubled consonantal 'i', as at 571.",
           "ablative, enclosing 'infert se Lucagus'; 'biiugis' is 'bi-' + 'iugum', bi-iu-gis, three syllables, 'bi-' short and the second 'i' a consonant, as at 571 and at 399 two parts back."),
 # L 580-583: in Iliad 5 Sthenelus drives off the horses at Diomedes' order
 (36, 'n', "Diomedes wounded him and took his horses,", "Diomedes wounded him and his horses were taken,"),
 # L 586-589: 'telo' softened (drafter's doubt)
 (39, 'n', "'telo', 'with his weapon': he has no whip and uses his sword.",
           "'telo', 'with his weapon', probably the sword he was whirling (577), used in place of a whip."),
 # L 594-595: Liger is not 'left helpless in it': he slips down from the chariot (596)
 (43, 'n', "and Liger, the driver, is left helpless in it.", "and Liger, the driver, cannot escape."),
 # L about: Liger both boasts and begs; Lucagus does neither
 ('about', None, "who charge him in a chariot, the one boasting, the other begging.",
                 "who charge him in one chariot, Liger first boasting, then begging."),
]
for k, f, old, new in E:
    s = D['about'] if k == 'about' else U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    if k == 'about': D['about'] = s.replace(old, new)
    else: U[k][f] = s.replace(old, new)
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
    for f in ('l', 'i'): assert 'Mago' not in u[f], (u['ln'], f)
    assert u['n'].count('Mago') == (1 if k == 4 else 0) and (k != 4 or "'Mago', dative of 'Magus'" in u['n']), u['ln']
assert 'Mago' not in D['about']
A.jdump(D, p)
print('renamed Mago -> Magus', n_mago, 'times; applied', len(E), 'edits')
