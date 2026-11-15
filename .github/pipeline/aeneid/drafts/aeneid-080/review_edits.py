#!/usr/bin/env python3
"""Reviewer's edits to aeneid-080 units.json (pass 1). Each edit: (unit index, field, old, new); old must occur
exactly once in that field (old=None replaces the whole field, which must start with the given 'new' check
prefix in NOTE_START). Only l, i, n are touched; t never. Run once."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

N19 = ("The print has 'viderit. ”Hoc', the closing speech mark joined to the next word, a misprint for "
       "'viderit.” Hoc', corrected here: the speech ends with 'viderit'. 'Ad quae', 'at which (words)', a connecting "
       "relative; the Latin Library has 'ad quem', 'to whom'. The verb of speaking is again left out. 'subridens "
       "mixta… ira', 'smiling, with anger mixed in', ablative absolute. 'Ast', an old and poetic form of 'at', 'but'. "
       "'divom', old genitive plural; 'divom pater atque hominum rex' is Homer's 'father of men and gods'. 'de me… "
       "viderit', 'about me he will see': the idiom 'viderit' (perfect subjunctive or future perfect), 'let him look "
       "to it, that is his affair'. Mezentius echoes Achilles' reply to the dying Hector (Iliad 22.365–366), but with "
       "a sneer. Elisions 'morer(e) ast', 'atqu(e) hominum'.")
N31 = ("The print has 'Aeneae. ”Dixit', the closing speech mark joined to the next word, a misprint for "
       "'Aeneae.” Dixit', corrected here: the speech ends with 'Aeneae'. 'oculis spatium emensus', 'having measured "
       "the space with his eyes', the deponent 'emetior'. 'quantum satis hastae', 'as much as (is) enough for a "
       "spear'. The verb of speaking is left out. 'Dextra mihi deus', 'my right hand (is) my god': the scorner of gods "
       "prays to his own hand and spear; 'adsint', 'may they be present', is the word of prayers to gods. 'libro', "
       "'I poise, balance'. 'Voveo… te… tropaeum', 'I vow you as a trophy': a trophy was a post dressed in captured "
       "armour, and Lausus himself, in Aeneas's armour, will be one. 'praedonis', 'the robber's', Aeneas, the foreign "
       "raider. 'Aeneae', genitive, 'of (victory over) Aeneas'. Elisions 'atqu(e) oculis', 'spati(um) emensus'.")
CLOSE = "The closing speech mark printed at the head of this unit belongs to Mezentius's speech (see the note before)."

E = [
 # L1 703: saxo atque... is not hendiadys; atque adds the fuller description of the one weapon
 (3, 'n', "'a stone, a huge fragment of mountain', hendiadys;", "'a stone, a huge fragment of mountain', 'atque' adding the fuller description;"),
 # L2 706: ignarum... Mimanta do not frame the line (occubat first)
 (5, 'n', "the adjective and the name frame the line.", "the adjective and the name far apart, holding the rest of the line between them."),
 # D1 709-710: l made 'harundinea' the boar's food; it is the reedy forest (silva... harundinea)
 (6, 'l', "in the forest\nfed on reeds,", "in a forest\nof reeds having fed,"),
 # L3 718 (drafter's open point a): say which lighter stop the English reads
 (7, 'n', "a misprint for a lighter stop, corrected here:", "a misprint for a lighter stop (read here as a semicolon), corrected here:"),
 # L4 721: l put 'longe' with miscentem; note and i take it with vidit
 (10, 'l', "Him when, throwing into confusion from afar the middle ranks, he saw,", "Him when, far off, throwing into confusion the middle ranks, he saw,"),
 # D2 727-728: l attached 'taeter' (foul) to the jaws; it agrees with cruor
 (12, 'l', "; there bathes his cruel, foul,\njaws the gore,", "; washes his ruthless\njaws the foul gore,"),
 # L5 726-729: 'Hunc ubi... vidit' is line 721, not 722
 (12, 'n', "'Hunc ubi… vidit' of 722.", "'Hunc ubi… vidit' of 721."),
 # D3 736: 'nixus' governs both ablatives (posito pede ... et hasta); not an ablative absolute
 (16, 'n', "'posito pede', ablative absolute, 'foot set', on the body, as a warrior plants his foot to draw out his spear (compare Patroclus at Iliad 16.503, perhaps). 'nixus et hasta', 'and leaning on his spear', the 'et' placed late.",
           "'posito pede nixus et hasta', 'resting on his planted foot and on his spear', 'nixus' (from 'nitor') with two ablatives, the 'et' placed late; the foot is set on the body, as a warrior plants his foot to draw out his spear (compare Patroclus at Iliad 16.503, perhaps)."),
 (16, 'l', "Then over the fallen man, with foot planted, leaning on his spear too:", "Then over the fallen man, on his planted foot leaning and on his spear:"),
 # D3 + E1 737 (echo: 'no small part of this war')
 (16, 'i', "Then, setting his foot on the fallen man and leaning on his spear, he said: “There lies tall Orodes, my men, no small part of this war.”",
           "Then, standing over the fallen man, his weight on the foot he had planted on him and on his spear, he said: “Look, men: tall Orodes lies here, and he counted for much in this war.”"),
 # L6 + rule 5b placement as 077/078 (print's reading opens the note of the unit where the speech closes); viderit both ways
 (19, 'n', None, N19),
 (20, 'n', "The print has 'viderit. ”Hoc', with the closing speech mark joined to the next word, a misprint for 'viderit.” Hoc', corrected here: the speech ends with 'viderit'.", CLOSE),
 # E2 743-744 (echo)
 (19, 'i', "“Die now. As for me, the father of gods and king of men will see to that.”",
           "“Now die. What becomes of me is for the father of gods and king of men to see to.”"),
 # E3 744-746 (echo)
 (20, 'i', "With these words he drew the spear from the body. Hard rest and iron sleep pressed down upon his eyes, and their light closed in everlasting night.",
           "So saying, he pulled the spear out of the body. A hard stillness, an iron sleep, weighed on the dying man's eyes, and their light was shut away into a night without end."),
 # L7 749: l 'Lycaonian' vs note/i 'son of Lycaon'
 (21, 'l', "Messapus Cronius and Lycaonian Erichaetes,", "Messapus Cronius and Lycaon's son Erichaetes,"),
 # D4 753: Thronium Salius Saliumque Nealces is acc-nom-acc-nom, parallel, not chiasmus
 (23, 'n', "the name repeated in chiasmus, 'Thronium Salius Saliumque Nealces'.",
           "the name set twice side by side, nominative then accusative, 'Thronium Salius Saliumque Nealces' (object, subject, object, subject)."),
 # L8 762: ingentem... hastam do not frame the line (At vero first)
 (26, 'n', "the adjective and noun framing the line.", "the adjective and noun far apart, enclosing the participle and the name."),
 # D5 764: Nerei is the Latin second-declension genitive of Nereus (Greek would be Nereos), scanned in two syllables
 (27, 'n', "'Nerei', a Greek genitive in two syllables.", "'Nerei', genitive of 'Nereus', scanned as two syllables, the '-ei' run together."),
 # E4 763-767 Orion simile (echo)
 (27, 'i', "He was as huge as Orion when he strides on foot through the vast pools of the midmost sea, cleaving his way, his shoulders rising clear of the waves, or when, carrying home an ancient ash-tree from the mountain heights, he walks upon the ground and hides his head among the clouds:",
           "He was huge as Orion is when he wades through the deepest waters of mid-ocean, breaking a path, his shoulder towering above the waves, or when, bringing back an aged ash from the mountain-tops, he treads the ground with his head lost in the clouds:"),
 # L9 770: imperterritus is not before the line-end ('ille' is)
 (30, 'n', "a long compound filling the space before the line-end.", "a long compound filling the space before 'ille'."),
 # L10 + rule 5b placement (as 19/20)
 (31, 'n', None, N31),
 (32, 'n', "The print has 'Aeneae. ”Dixit', with the closing speech mark joined to the next word, a misprint for 'Aeneae.” Dixit', corrected here: the speech ends with 'Aeneae'.", CLOSE),
 # L11 772: i begins lower case after the semicolon that ends 771 (house practice in this part); E5 773 (echo)
 (31, 'i', "Measuring with his eye the distance a spear could carry, he said: “My right hand, which is my god, and the weapon I poise to throw, be with me now!",
           "measuring with his eye the distance a spear could carry, he said: “Let my right hand, the only god I own, and the spear I balance for the throw, stand by me now!"),
 # E6 781-782 (echo, 'remembered his sweet Argos') + drafter's open point b: the restored mark is a semicolon
 (34, 'i', "The unhappy man fell, by a wound meant for another, and looked up at the sky, and as he died remembered his sweet Argos.",
           "The unhappy man fell, struck by a wound meant for another; he looked up at the sky, and dying, his thoughts went home to the Argos he loved;"),
 # L12 783 (open point b): after 'Argos;' the next unit begins lower case, as t does
 (35, 'l', "Then dutiful Aeneas", "then dutiful Aeneas"),
 (35, 'i', "Then dutiful Aeneas", "then dutiful Aeneas"),
 # D6 785: metre needs transit with long final i, so the contracted perfect; l tense follows
 (35, 'n', "'transit', perhaps the contracted perfect of 'transeo' for 'transiit' (the Latin Library's reading), or a present.",
           "'transit', the contracted perfect of 'transeo', for 'transiit' (the Latin Library's reading): the metre needs a long final 'i', which the present 'transit' does not have."),
 (35, 'l', "bulls' woven work passes,", "bulls' woven work passed,"),
]
NOTE_START = {19: "'Ad quae', 'at which (words)'", 31: "'oculis spatium emensus'"}
for k, f, old, new in E:
    s = U[k][f]
    if old is None:
        assert s.startswith(NOTE_START[k]) and s.endswith("On the closing speech mark, see the next unit. " + s.split("next unit. ")[-1]), (k, s[:60])
        U[k][f] = new; continue
    c = s.count(old); assert c == 1, (k, f, c, old)
    U[k][f] = s.replace(old, new)
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert top == {k: D[k] for k in top}
for u in U:
    assert u['l'].count('\n') == u['t'].count('\n') and '\n' not in u['i'], u['ln']
    assert 15 <= len(u['n'].split()) <= 139, (u['ln'], len(u['n'].split()))
    assert 'sc' not in u
A.jdump(D, p)
print('applied', len(E), 'edits')
