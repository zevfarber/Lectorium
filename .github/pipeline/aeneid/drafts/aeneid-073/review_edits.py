#!/usr/bin/env python3
"""Reviewer's edits to aeneid-073 units.json (pass 1). Each edit: (unit index, field, old, new);
old must occur exactly once in that field. Only l, i, n are touched. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # L 101b-103: 'tremefacta' is passive; the other construal of 'tellus'; 'eo dicente' is 'as he speaks', not 'before'
 (2, 'l', "and trembling from its base the earth;", "and, made to tremble from its base, the earth;"),
 (2, 'n', "supply 'est'.", "supply 'est', or take 'tellus' as a second subject of 'silescit'."),
 (2, 'n', "All nature hushed before the king of the gods speaks", "All nature hushed as the king of the gods speaks"),
 # L 104: the line repeats III.250 (checked in the edition)
 (3, 'n', "Elisions 'Accipit(e) ergo',", "The whole line repeats III.250, where the Harpy Celaeno begins her prophecy. Elisions 'Accipit(e) ergo',"),
 # L 107-108: cuique two syllables (scan-fixes 10.107)
 (5, 'n', "'secat spem',", "'cuique' is two syllables, 'cui-' one, as at 111. 'secat spem',"),
 # L 109-110: i committed to one reading ('misread') that l and n leave open
 (6, 'i', "and warnings misread.", "and ill-starred warnings."),
 # L 111a: muddled phrase
 (7, 'n', "and will get no special favour from the consequences of their acts.", "and are not released from the consequences of their acts."),
 # L 113-115: Stygii agrees with fratris; misprint note in the 071 form
 (10, 'l', "By the Stygian streams of his brother,", "By the streams of his Stygian brother,"),
 (10, 'n', "a misprint for 'invenient.” Stygii', corrected here; t keeps the print.",
           "a misprint for 'invenient.” Stygii', corrected here: the closing mark is joined to the next word (as at IX.781); t keeps the print."),
 # L 116a: not a half-line
 (11, 'n', "A half-line formula closing the scene;", "A brief formula closing the speech, filling the first half of the line;"),
 # L 116b-117: 'aureo' goes with 'solio'; the pair does not frame the line
 (12, 'l', "From his throne then Jupiter golden", "From his golden throne then Jupiter"),
 (12, 'n', "ablative of separation with 'surgit', framing the line;", "ablative of separation with 'surgit', enclosing 'tum Iuppiter';"),
 # L 118-119: 'omnibus' goes with 'portis'
 (13, 'l', "at the gates around, all of them, press on", "at the gates around, at all of them, press on"),
 # L 121b-125a: 'named after' is an inference; syllables of Hicetaonius (scan-fixes 10.123)
 (15, 'n', "'Assaraci duo', two men named after Assaracus, an ancestor of Aeneas.",
           "'Assaraci duo', 'the two Assaraci', two men who bear the name of Assaracus, an ancestor of Aeneas."),
 (15, 'n', "Greek patronymics;", "Greek patronymics ('Hicetaonius' is Hi-ce-ta-o-ni-us, six syllables);"),
 # L 132-135a: l repeated 'head'
 (19, 'l', "the Dardan boy, look, his head uncovered, his handsome head,", "the Dardan boy, look, his handsome head uncovered,"),
 # MED 135b-137a: boxwood is pale, not dark; Oricum softened; 'buxo aut' is a hiatus, not an elision (scan-fixes 10.136)
 (20, 'n', "both are dark, close-grained woods, so the white ivory shows bright against them,",
           "both close-grained woods, boxwood pale yellow and terebinth dark, against which the white ivory shows bright,"),
 (20, 'n', "'Oricia', 'of Oricum', a port in Epirus, known for the terebinth.", "'Oricia', 'of Oricum', a port on the coast of Epirus."),
 (20, 'n', "The line ends in a four-syllable Greek word, a Greek rhythm. Elision 'bux(o) aut'.",
           "The line ends in a four-syllable Greek word, a Greek rhythm, and 'buxo aut' is a hiatus: the -o is not cut off but stays long at the pause in mid-line. No elisions."),
 # L 137b-138: 'cui' unrendered in l; MED: the second subject receives the hair, not the neck the band
 (21, 'l', "and his flowing locks his milk-white neck", "whose flowing locks the milk-white neck"),
 (21, 'l', "receives, and, clasping them beneath,", "receives, and, binding them beneath,"),
 (21, 'n', "'crinis' accusative plural in '-is', framing the rest of the line.", "'crinis' accusative plural in '-is', enclosing 'cervix cui lactea'."),
 (21, 'n', "a second subject of 'accipit' by a slight stretch: the neck takes both the hair and the band.",
           "a second subject of 'accipit': the neck and the circlet both receive the hair, the circlet binding it up."),
 # L 139-142: framing; 'both armies' softened; MED: 'domo, ubi' is a hiatus (scan-fixes 10.141)
 (22, 'n', "framing the line: both armies saw him.", "enclosing 'viderunt, Ismare': the peoples who watched him fight."),
 (22, 'n', "Elisions 'diriger(e) et', 'dom(o) ubi', 'Pactolusqu(e) inrigat'.",
           "Elisions 'diriger(e) et', 'Pactolusqu(e) inrigat'; 'domo, ubi' is a hiatus, the -o not cut off but kept long at the pause."),
 # L 148-150a: '-ve' is 'or' (the note says so)
 (27, 'l', "and what he seeks, and what he himself brings,", "or what he seeks, or what he himself brings,"),
 # L 153b-154a: tense
 (29, 'i', "there was no delay;", "there is no delay;"),
 # MED 156b-158: 'duci. Aeneia' is a hiatus across the stop (scan-fixes 10.156); subiuncta (scan-fixes 10.157)
 (31, 'n', "Elision across the start of the unit, 'duc(i) Aeneia'.",
           "'subiuncta' is sub-iuncta, the i a consonant. No elision: 'duci. Aeneia', across the full stop, is a hiatus, the -i of 'duci' kept long."),
 # L 166: the pair does not frame the line
 (34, 'n', "and adjective and noun frame the line.", "and adjective and noun enclose 'princeps secat aequora'."),
 # L 172-174: garbled gloss
 (38, 'n', "so 'Chalybum metallis', 'mines like the Chalybes'', mines of iron.", "so 'Chalybum metallis', 'with the Chalybes' metals', iron mines like theirs."),
 # L 175-178: elision list
 (39, 'n', "'aci(e) atque'.", "'aci(e) atque', 'atqu(e) horrentibus'."),
 # L 179-180a: quantity of Etrusca (the metre's only fit)
 (40, 'n', "Greek by descent, Etruscan by ground.", "Greek by descent, Etruscan by ground. 'Etrusca' has a long first syllable here, as at VIII.503 (short at 148)."),
]
for k, f, old, new in E:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
A.jdump(D, p)
print('applied', len(E), 'edits')
