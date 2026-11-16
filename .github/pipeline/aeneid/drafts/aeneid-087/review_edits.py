#!/usr/bin/env python3
"""Reviewer's edits to aeneid-087 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n (and the
top-level 'about', one sentence) are touched; t, ln, p, v and title/titleEn/part never. Run once (it refuses if
the file has already been edited: every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part')}

E = [
 # ---------------- medium: speech marks 537 / 584 are not misprints but the print's division (doubtful, kept) ----------------
 (1, 'n', "Diana's speech begins, and it runs on to 594.",
          "The print has 'alias. ”Neque', the closing mark joined to the next word, a misprint for 'alias.” Neque', corrected here (as 'vale. ”Nec', 11.98). In the print Diana's first words end here and resume at 'Vellem' (584–594); between, the poet tells Camilla's story. Many editors give all of 535–594 to Diana; either reading is possible, so the print's marks are kept."),
 (1, 'l', "dear to me before others.", "dear to me before others.”"),
 (1, 'i', "she is dear to me above all others.", "she is dear to me above all others.”"),
 (2, 'n', "The print has a closing double mark joined to 'Neque', as if Diana's speech ended at 'alias'; it does not, and the reading text leaves the mark out. Diana speaks of herself by name, 'Dianae', as gods often do (compare 'sola contenta Diana', 582), and the speech plainly goes on to 594.",
          "The closing speech mark printed at the head of this unit belongs to Diana's words before it (see the note there). With the print's marks the poet now speaks, naming the goddess, 'Dianae'. Others keep Diana speaking: 'enim' and 'iste' sound like speech, gods name themselves (compare 582), and 'Vellem' (584) needs no verb of speaking."),
 (2, 'n', "'venit', 'has come'.", "'venit', perfect, 'has come': the metre needs the long 'vē-'."),
 (2, 'n', "'animum', understood as hers.", "'animum', hers."),
 (2, 'l', "comes love, nor with a sudden sweetness has it moved my heart.",
          "has come love, nor with a sudden sweetness has it moved her heart."),
 (2, 'i', "nor has it stirred my heart with a sudden sweetness.", "nor has it stirred her heart with a sudden sweetness."),
 (11, 'n', "Metabus's prayer, which follows, is a speech within Diana's speech.",
           "Metabus's prayer follows, in speech marks of its own."),
 (12, 'n', "The print sets Metabus's prayer in double marks inside Diana's speech; the reading text gives the nested speech single marks.",
           "Metabus's prayer begins. (On the reading that gives the whole story to Diana, see 537, it would be a speech within her speech.)"),
 (12, 'l', "‘Kindly one,", "“Kindly one,"),
 (12, 'i', "‘Kind goddess,", "“Kind goddess,"),
 (13, 'n', "The print closes Metabus's prayer with a double mark; in the reading text it closes with a single one, since Diana is still speaking.",
           "Metabus's prayer ends."),
 (13, 'l', "doubtful breezes.’", "doubtful breezes.”"),
 (13, 'i', "uncertain winds.’", "uncertain winds.”"),
 (15, 'n', "Diana's pity for a child", "pity for a child"),
 (24, 'n', "Diana again names herself, as at 537.", "The goddess is named again, as at 537."),
 (25, 'n', "The print has an opening double mark before 'Vellem', as if a new speech began; Diana has been speaking since 535 and goes on, so the reading text leaves the mark out.",
           "Diana speaks again, with the print's opening mark before 'Vellem', and goes on to 594 (on the marks, see 537)."),
 (25, 'l', "I would wish she had not been seized", "“I would wish she had not been seized"),
 (25, 'i', "I could wish she had never", "“I could wish she had never"),

 # ---------------- medium: wrong labels / wrong English ----------------
 # 644-645 'transfixa' is a perfect passive participle with 'hasta', not active 'having transfixed'
 (54, 'n', "'transfixa', 'having transfixed', of the spear.",
           "'transfixa', perfect passive participle agreeing with 'hasta', 'driven right through' him."),
 (54, 'l', "doubles the man up, piercing him, with pain.", "doubles the man up, thrust through, with pain."),
 (54, 'i', "quivered there, and, having pierced him through, doubled him up with pain.", "quivered in the wound and, passing clean through, doubled him up with pain."),
 # 641 both 'ingentem' are Herminius: no change of reference
 (52, 'n', "'ingentem animis, ingentem corpore', the repetition with change of reference.",
           "'ingentem animis, ingentem corpore', both of Herminius, the adjective repeated at the head of each phrase."),
 # 613-614 the print says 'make a sound', not 'fall' (that is the Latin Library's 'ruinam dant')
 (39, 'i', "and were the first to fall with a mighty crash,", "and were the first to raise a din, crashing down mightily,"),
 # 552 'Telum' is the antecedent drawn into the relative clause, not an object of the main verb
 (10, 'n', "and picks it up again with 'huic' and 'hastae': the object is put first to fix attention, then resumed, a loose but vivid order.",
           "drawn into the relative clause as the object of 'gerebat' ('a huge spear, which…'), and picks it up again with 'huic' and 'hastae', a loose but vivid order."),
 # 609 'frenzied' attached to the riders in l
 (37, 'l', "suddenly they burst out with a shout, and frenzied\nthey urge on their horses;",
           "suddenly they burst out with a shout, and the raging\nthey urge on, horses;"),
 # 539 l attached 'vires superbas' to 'regno'
 (3, 'l', "Driven, on account of hatred, from his kingdom and his proud strength,",
          "Driven, on account of hatred, from his kingdom, and of his proud strength,"),

 # ---------------- low: notes ----------------
 (0, 'n', "'Opim', Greek-style accusative of 'Opis',", "'Opim', accusative of 'Opis', in '-im' as Latin often gives Greek names in '-is',"),
 (0, 'n', "'compellabat… dabat', imperfects: she was speaking when the battle began below.",
          "'compellabat… dabat', imperfects that set the scene, 'interea', while Turnus lies in wait."),
 (0, 'n', "'-is' accusative plural, 'sad words';", "'-is' accusative plural, 'sad words' ('tristis' could also be nominative, 'the sorrowing goddess');"),
 (6, 'n', "'abundans', literally 'over-wave-ing', overflowing.", "'abundans', from 'ab' and 'unda', 'streaming off in waves', overflowing."),
 (18, 'n', "'on the mountains of shepherds and lonely', the 'et' postponed:", "'on the mountains of shepherds and lonely', 'et' joining a genitive and an adjective:"),
 (18, 'n', "keeping the early '-om' after 'v' as in 'divom' and 'volnus'.", "keeping the early 'o' after 'v', as in 'divom' and 'volnus'."),
 # VII.691 Messapus is son of Neptune; nothing says Etruscan-born (checked)
 (35, 'n', "Messapus is the Etruscan-born horse-tamer of VII.691;", "Messapus is the horse-tamer, son of Neptune, of VII.691;"),
 # VII.670-672: Argive twins from Tibur, not its founders (as corrected in 086)
 (52, 'n', "Catillus, brother of Coras, one of the twin founders of Tibur, now kills two men.",
           "Catillus, twin brother of Coras (Argive warriors from Tibur, VII.670–672), now kills two men; 'Cātillus' has a long first syllable, as VII.672 shows."),
 (52, 'n', "'Iollan', Greek accusative of 'Iollas'.", "'Iollan', Greek accusative of 'Iollas', three syllables, I-ol-lan."),
 (52, 'n', "'deicit', 'casts down', present.", "'deicit', 'casts down', present, three syllables, dē-i-cit."),
 (48, 'n', "the verb for the groans is supplied from 'surgit' at the end.",
           "'gemitus' shares 'volvuntur' with the arms, bodies and horses, a bold zeugma (the groans 'roll' out); some supply 'rise' instead."),
 (47, 'n', "'legit… virum vir', 'man chose man',", "'legit… virum vir', 'man chose man', 'lēgit' perfect (the metre needs the long e),"),
 (42, 'n', "'Troes', Greek nominative plural, 'Trojans',", "'Troes', Greek nominative plural, two syllables, Trō-es, 'Trojans',"),
 (42, 'n', "named in the catalogue of Aeneas's allies in Book X.", "named in the catalogue of Aeneas's allies (X.175)."),
 (45, 'n', "corrected here: 'superiacit', 'throws over', needs an object, and 'spumeus' goes with 'pontus'.",
           "corrected here (the Latin Library has 'scopulosque'): 'superiacit', 'throws over', needs an object, and 'spumeus' goes with 'pontus'; a nominative 'scopulus' would leave the verb with no object and make the crag the thrower."),

 # ---------------- low: l ----------------
 (40, 'l', "hurls headlong far", "plunges headlong far"),
 (45, 'l', "and over the rocks throws its wave,", "and the rocks overtops with its wave,"),
 (47, 'l', "into battles whole", "into battles, the whole"),
]

for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)
old_about = "She tells the story. "
assert D['about'].count(old_about) == 1
D['about'] = D['about'].replace(old_about, "Then comes Camilla's story. ")

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    n = len(u['n'].split()); assert 15 <= n <= 139, (k, n)
    assert ('“' not in u['n'] and '”' not in u['n']) or k == 1, k
    assert '‘' not in u['l'] + u['i'] and '’' not in u['l'] + u['i'], k
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    assert o == c == 3, (lay, o, c)
A.jdump(D, p)
print('applied', len(E) + 1, 'edits')
