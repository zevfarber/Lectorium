#!/usr/bin/env python3
"""Reviewer's edits to aeneid-074 units.json (pass 1). Each edit: (unit index, field, old, new);
old must occur exactly once in that field. Only l, i, n (and the part's 'about') are touched; t never. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # MED 185-188: vocative Cinyre points to Cinyrus, not Cinyras (vocative Cinyra), the Cyprian king's name;
 # i made Ligurum partitive; framing; vestrum softened
 (0, 'l', "Cinyras, nor you, with few companions, Cupavo,", "Cinyrus, nor you, with few companions, Cupavo,"),
 (0, 'i', "Nor would I pass you by, Cinyras, bravest in war of the Ligurian chiefs,",
          "Nor would I pass you by, Cinyrus, leader of the Ligurians and bravest in war,"),
 (0, 'n', "'Cinyre', vocative; the Latin Library prints 'Cunare', and the name differs between editions.",
          "'Cinyre', vocative, pointing to a nominative 'Cinyrus'; the Latin Library prints 'Cunare', and the name differs between editions."),
 (0, 'n', "'olorinae… pennae', 'swan's feathers', framing the line.", "'olorinae… pennae', 'swan's feathers', enclosing 'surgunt de vertice'."),
 (0, 'n', "'vestrum' plural, as if Love and his fellow love-gods were addressed:",
          "'vestrum' plural, as if Love were addressed together with his mother Venus, or with the other powers of love:"),
 # MED 189-193: canentem agrees with senectam (n and i), not with Cycnus (l)
 (1, 'l', "whitening, in soft plumage, drew on old age,", "in soft plumage drew on a whitening old age,"),
 (1, 'n', "'canentem', 'growing white' (from 'caneo'), plays on 'canit', 'sings'.",
          "'canentem… senectam', 'a whitening old age', 'canentem' from 'caneo', 'be white' (the metre makes 'ca-' long), playing on 'canit', 'sings'."),
 # L 198-201a: Manto's identity softened; dives + ablative
 (4, 'n', "in Greek legend the daughter of the Theban seer Tiresias.", "commonly identified with the daughter of the Theban seer Tiresias."),
 (4, 'n', "'dives avis', 'rich in ancestors', ablative of respect.", "'dives avis', 'rich in ancestors', ablative with an adjective of plenty."),
 # L 207-208: Aulestes is named at XII.290 and killed by 296
 (7, 'n', "Aulestes will die in Book XII (290).", "Aulestes will die in Book XII (289–296)."),
 # MAJOR 209-212: caerula goes with freta (the metre makes its -a short), not with the ablative concha
 (8, 'l', "Him carries a monstrous Triton, with his blue conch\nterrifying the straits,",
          "Him carries a monstrous Triton, with his conch the sea-blue\nstraits terrifying,"),
 (8, 'i', "who terrifies the seas with his blue conch;", "who terrifies the blue seas with his conch;"),
 (8, 'n', "'caerula concha', 'with sea-blue conch', ablative of means.",
          "'caerula… freta', 'the sea-blue straits', object of 'exterrens'; the metre makes the -a of 'caerula' short, so it cannot agree with the ablative 'concha', 'with his conch'."),
 # L 213-214: i followed the Latin Library's 'aere', not the print's 'aera' (n and l)
 (9, 'i', ", cutting the plains of salt with their bronze-clad prows.", ", and their bronze prows were cutting the plains of salt."),
 # L 217-218: Aeneas (scan-fixes 10.217)
 (11, 'n', "'cura', 'care',", "'Aeneas', 'Ae-' one syllable. 'cura', 'care',"),
 # L 224-228a: Cymodocea (scan-fixes 10.225)
 (13, 'n', "the name coming last.", "the name coming last; 'Cymodocea' is five syllables, Cy-mo-do-ce-a."),
 # L 228b-229a: the Servius/Vestals attribution was from memory and unchecked: softened; Aenea (scan-fixes 10.229)
 (14, 'n', "Servius says the words recall a ritual formula with which the Vestal Virgins roused the king of sacrifices, 'vigilasne, rex? vigila'.",
           "Ancient commentators heard in the words a ritual call used to rouse a priest, 'vigilasne, rex? vigila'. 'Aenea' is three syllables, the last long."),
 # L 230-231a: framing
 (16, 'n', "'Idaeae… pinus', 'Idaean pines', framing the line:", "'Idaeae… pinus', 'Idaean pines', enclosing 'sacro de vertice':"),
 # L 236-237: elision list
 (19, 'n', "Elisions 'tel(a) inter', 'medi(a) atque'.", "Elisions 'tel(a) inter', 'medi(a) atque', 'atqu(e) horrentis'."),
 # L 244-245: l took ingentis with caedis; n and i take it with acervos
 (23, 'l', "of huge Rutulian slaughter will look upon the heaps.”", "will look upon huge heaps of Rutulian slaughter.”"),
 # L 252-255: Idaea is an adjective; urbis wording; biiugi (scan-fixes 10.253)
 (29, 'l', "“Kindly mother of Ida, of the gods,", "“Kindly Idaean mother of the gods,"),
 (29, 'n', "'urbis' is nominative here, an old plural form; the Latin Library prints 'urbes'.",
           "'urbis' must be nominative plural here, an old spelling of 'urbes' (which the Latin Library prints), not Greenough's usual accusative '-is'."),
 (29, 'n', "'biiugi… leones', 'lions yoked in pairs',", "'biiugi… leones', 'lions yoked in pairs' ('biiugi' is bi-iu-gi, the second i a consonant),"),
 # L 260-262a: i mixed tenses and lost the inverted cum; Teucros (scan-fixes 10.260)
 (33, 'i', "And now he has the Trojans and his own camp in sight as he stands on the lofty stern, and then he raised the blazing shield high in his left hand.",
           "And now, standing on the lofty stern, he had the Trojans and his own camp in sight, when he raised the blazing shield high in his left hand."),
 (33, 'n', "'deinde', two syllables here.", "'deinde', two syllables here, and 'Teu-' in 'Teucros' one."),
]
for k, f, old, new in E:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
assert D['about'].count("Cinyras leads the Ligurians") == 1
D['about'] = D['about'].replace("Cinyras leads the Ligurians", "Cinyrus leads the Ligurians")
A.jdump(D, p)
print('applied', len(E) + 1, 'edits')
