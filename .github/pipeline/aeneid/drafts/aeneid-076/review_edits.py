#!/usr/bin/env python3
"""Reviewer's edits to aeneid-076 units.json (pass 1). Each edit: (unit index, field, old, new);
old must occur exactly once in that field. Only l, i, n are touched; t never. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
E = [
 # L 362-363: 'parte ex alia' is 'another side', as i has it
 (0, 'l', "But on the other side, where", "But on another side, where"),
 # L 369b-372a: fido takes the dative or the ablative
 (3, 'n', "'pedibus' is dative with 'fido'.", "'pedibus' is dative (or ablative) with 'fido'."),
 # L 373-374: 'alta' is 'lofty' (the note: Pallanteum on its hill), not 'proud'
 (5, 'i', "that is the way our proud homeland calls you back, and Pallas your leader with you.",
          "that is the road by which our homeland, high on its hill, demands you back, you and Pallas your leader."),
 # L 375-376: urget is at 373, two lines before 375
 (6, 'n', "'urgemur' picks up 'urget' in the line before.", "'urgemur' picks up 'urget' two lines before (373)."),
 # L 379: l read 'the dense bursts' as a noun phrase
 (8, 'l', "This he says, and in their midst into the dense bursts the enemy.",
          "This he says, and in their midst into the packed enemy bursts."),
 # L 380-381a: with the passive participle the ablative is of means
 (9, 'n', "'fatis… iniquis', 'by unkind fates', ablative of cause.",
          "'fatis… iniquis', 'by unkind fates', ablative of means with 'adductus'."),
 # L 390-392: 'the Rutulian fell fields' (fell read as an adjective); Laride's quantities (scan-fixes 10.391)
 (14, 'l', "You too, twins, on the Rutulian fell fields,", "You too, twins, fell on the Rutulian fields,"),
 (14, 'n', "'Laride', vocative of 'Larides';", "'Laride', vocative of 'Larides', all three syllables long here and at 395;"),
 # L 393: dura... discrimina does not frame the line (at nunc before, Pallas after)
 (15, 'n', "'dura… discrimina', 'harsh distinctions', framing the line:",
           "'dura… discrimina', 'harsh distinctions', enclosing 'dedit vobis':"),
 # L 394: 'Evander's own sword' goes beyond the text
 (16, 'n', "Evander's own sword in his son's hand,", "the sword of Evander's house, wielded by his son,"),
 # L 399-400a: biiugis and traicit quantities (scan-fixes 10.399, 10.400); 'transicit' dropped
 (19, 'n', "three syllables, the second 'i' a consonant.", "three syllables, the second 'i' a consonant and 'bi-' short."),
 (19, 'n', "'traicit' (= 'transicit', from 'trans' and 'iacio'), 'pierces through',",
           "'traicit' (from 'trans' and 'iacio'), three syllables, tra-i-cit, 'pierces through',"),
 # L 405-409: i recast from the Latin, away from stock prose wording of the simile
 (22, 'i', "And as in summer, when the winds he hoped for have risen, a shepherd sets fires at scattered points in the woods, and suddenly the gaps between catch, and a single bristling line of fire stretches across the wide plains, while he sits looking down like a victor on the exulting flames:",
           "And as in summer, once the winds he has waited for spring up, a shepherd sets fire to the woods at scattered points; all at once the spaces between are caught, and Vulcan's battle-line spreads out in one bristling front across the broad plains, while he sits, a victor, gazing down on the flames as they exult:"),
 # L 411b-412: Halaesus as VII.723 has him (as corrected in 075, L12)
 (24, 'n', "in the catalogue of Book VII he is a follower of Agamemnon's line who settled in Italy.",
           "in the catalogue of Book VII he is 'Agamemnonius', of Agamemnon's house or following, an enemy of the Trojan name (VII.723)."),
 # L 413-416: Ladona, Phereta quantities (scan-fixes 10.413)
 (25, 'n', "'Ladona', 'Phereta', Greek accusatives;",
           "'Ladona', 'Phereta', Greek accusatives (La-do-na with its first two syllables long, Phe-re-ta with its first short);"),
 # L 423: i dropped 'Haec'
 (30, 'i', "Your oak shall bear the arms and spoils of the man.”", "Your oak shall have these arms and this man's spoils.”"),
 # MAJOR 424b-425: texit is the perfect of tego, not the present
 (32, 'n', "'dum texit', 'while he shields', present of 'tego'.",
           "'dum texit', 'while he shielded', perfect of 'tego' (the present is 'tegit'): 'dum' normally takes the present, and the perfect here is unusual."),
 (32, 'l', "while he shields Imaon, Halaesus", "while he shielded Imaon, Halaesus"),
 # L 429-430: the Etruscans are Tarchon's own men; Grais quantities (scan-fixes 10.430)
 (35, 'n', "'Etrusci', Tarchon's allies.", "'Etrusci', Tarchon's Etruscans, Aeneas's allies."),
 (35, 'n', "'Grais' a dative of agent", "'Grais' (two long syllables, Gra-is) a dative of agent"),
 # L 435-436a and 436b-437: i recast away from familiar wording
 (39, 'i', "both of outstanding beauty, but Fortune had denied them any return to their homeland.",
           "both of them strikingly fair, but Fortune had refused them any homecoming."),
 (40, 'i', "Yet the ruler of great Olympus did not let the two of them meet each other in combat:",
           "Yet the ruler of great Olympus would not allow the two to clash with one another:"),
]
for k, f, old, new in E:
    s = U[k][f]; c = s.count(old)
    assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
A.jdump(D, p)
print('applied', len(E), 'edits')
