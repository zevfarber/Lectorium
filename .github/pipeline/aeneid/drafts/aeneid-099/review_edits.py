#!/usr/bin/env python3
"""Reviewer's edits to aeneid-099 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n are touched;
t, ln, p, v, title, titleEn, part, about and advisory never. Run once (it refuses if the file has already been edited:
every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about', 'advisory')}

E = [
 # ---------------- medium M1: missing elision (947) ----------------
 (50, 'n', "a present subjunctive in an indignant question. No elisions.",
           "a present subjunctive in an indignant question. Elision 'Tun(e) hinc'."),

 # ---------------- medium M2: l attaches fratris to the verb rather than to armis (844) ----------------
 (0, 'l', "and Juturna prepares from her brother to send away, from the arms.",
          "and Juturna prepares, of her brother, to send away from the arms."),

 # ---------------- medium M3: i, precautionary rephrasings against remembered modern versions ----------------
 (10, 'i', "But when unhappy Juturna, far off, knew the whirr of the Dira's wings, she tore her loosened hair, and as a sister will, she marred her face with her nails and beat her breast with her fists:",
           "But when Juturna, far off, knew the shrill whirr and the wings of the Dira, the unhappy sister tore at her loosened hair and disfigured her face with her nails, her breast with her fists:"),
 (11, 'i', "“What help can your sister give you now, Turnus?",
           "“Turnus, what is there now that your sister has the power to do for you?"),
 (13, 'i', "By what craft can I keep you in the daylight? Can I stand against such a monster as this?",
           "By what art am I to keep you in the light of day? Am I one to set myself against a portent such as this?"),
 (15, 'i', "Do not terrify me, ill-omened birds; I am frightened already. I know the beat of your wings and the deadly sound, and I do not mistake the haughty orders of great-hearted Jove.",
           "Do not try to frighten me, ill-omened birds: I am afraid already. I know that beating of wings and that deadly sound, and I read aright the proud commands of great-hearted Jove."),
 (16, 'i', "Is this what he pays me for my maidenhood?",
           "Is this what he gives me back in exchange for my maidenhood?"),
 (17, 'i', "Why did he give me a life without end?",
           "To what end did he make my life endless?"),
 (18, 'i', "Why has the lot of death been taken from me? Then at least I could put an end to this great grief now, and go with my poor brother through the shades!",
           "Why am I denied the lot of death? Then surely I could put an end to all this grief now, and keep my poor brother company on his way through the shades!"),
 (20, 'i', "Or will anything of mine be sweet to me without you, brother? Oh, what earth will gape deep enough for me, and send a goddess down to the Shades below?”",
           "Or can anything that is mine be sweet to me, brother, without you? Oh, where is the earth that will open deep enough for me, and carry a goddess down to the lowest of the Shades?”"),
 (21, 'i', "So much she said, and covered her head with her sea-grey mantle, and with many a groan the goddess hid herself in the depths of her river.",
           "She said no more, but drew her grey-green mantle over her head and, groaning deeply, the goddess hid herself in the depths of her river."),
 (23, 'i', "“What is the delay now? Why are you still holding back, Turnus?",
           "“What is it that keeps us waiting now? Turnus, why do you still shrink back?"),
 (26, 'i', "Turnus shook his head: “Your hot words do not frighten me, savage: it is the gods that frighten me, and Jupiter my enemy.”",
           "Turnus shook his head: “Your hot words do not frighten me, fierce as you are; the gods are what frighten me, and Jupiter, who is now my enemy.”"),
 (30, 'i', "But he did not know himself as he ran or as he went, as he raised his hands or moved the enormous stone: his knees gave way, and his blood thickened, frozen with cold.",
           "But running or walking, lifting his hands or heaving the enormous stone, he did not know himself; his knees buckled, and his blood went cold and thick."),
 (32, 'i', "And as in dreams, when the drowsy quiet of night has weighed down our eyes, we seem to strain in vain to run on and on, and in the middle of the effort we sink down helpless; the tongue will not work, the body's familiar strength fails, and neither voice nor words will come:",
           "And just as in sleep, when at night a heavy rest has pressed our eyes shut, we seem to want, and want in vain, to lengthen our eager running, and halfway through the struggle we slump, spent; the tongue has no power, the strength we know gives out in the body, and no voice comes, no words:"),
 (40, 'i', "Struck, huge Turnus fell to the ground, his knee bent double under him.",
           "Hit, the huge Turnus came down to the ground, his knee folding under him."),
 (42, 'i', "Humbled, a suppliant, he raised his eyes and stretched out his right hand in entreaty. “I have earned this, truly, and I make no plea against it,” he said:",
           "Brought low, a suppliant, he lifted his eyes and held out his right hand to plead. “I have deserved it, I grant, and I ask no reprieve,” he said:"),
 (43, 'i', "“Make use of your fortune.",
           "“Take what your fortune gives."),
 (44, 'i', "If any thought for an unhappy parent can touch you (you too had such a father in Anchises), I beg you, have pity on Daunus in his old age, and give me back to my people, or, if you would rather, my body robbed of the light.",
           "If care for a father in his misery can move you at all (and Anchises was such a father to you), I pray you, take pity on the old age of Daunus, and give me back to my own, or, if you choose, my body, stripped of the light."),
 (45, 'i', "You have won, and the Italians have seen me beaten and holding out my hands; Lavinia is yours to marry:",
           "The victory is yours, and the men of Ausonia have watched me, beaten, stretch out my hands; Lavinia is yours for a wife:"),
 (46, 'i', "do not carry your hatred any further.”",
           "let your hatred stretch no further.”"),
 (48, 'i', "and Turnus's words were beginning to sway him more and more as he hesitated, when high on Turnus's shoulder there came into view the ill-fated baldric, and the belt of young Pallas flashed with its familiar studs; Turnus had overcome the boy and struck him down with a wound, and now wore on his shoulders the badge he had taken from his enemy.",
           "and already the words were bending Aeneas, who wavered more and more, when high on Turnus's shoulder the ill-starred baldric caught his eye, and the belt of the boy Pallas glinted with the studs he knew so well: Turnus had overcome the boy and laid him low with a wound, and now wore the trophy of an enemy on his shoulders."),
 (50, 'i', "“You, dressed in the spoils of one of mine, are you to be snatched out of my hands?",
           "“Are you to be torn from my grasp here, you, decked out in the spoils of one of mine?"),
 (51, 'i', "It is Pallas who deals you this wound, Pallas who offers you up as a victim and takes the penalty out of your guilty blood,”",
           "This wound is the wound of Pallas; Pallas makes an offering of you, and takes his payment out of your guilty blood,”"),
 (52, 'i', "and as he said it he buried his sword deep in the breast that faced him, in a blaze of fury.",
           "and as he spoke he drove the sword deep into the breast that faced him, burning with rage."),
 (53, 'i', "But Turnus's limbs went slack and cold, and life,",
           "But the cold undid Turnus's limbs, and life,"),

 # ---------------- low ----------------
 # L1 863 spondaic fifth foot (scan-fix gloss)
 (7, 'n', "'bustis', 'tombs', places where the dead were burned.",
          "'bustis', 'tombs', places where the dead were burned. Line 863 has a spondee in the fifth foot, 'culminibus desertis', a rare, heavy close."),
 # L2 'Juturna's immortality' not named at 139-141
 (17, 'n', "her immortality, the other part of Jupiter's payment with her rule over pools and rivers (12.139–141).",
           "her immortality, which she counts as Jupiter's payment along with the rule over pools and rivers that the poem named (12.139–141)."),
 # L3 881 fratri (scan-fix gloss)
 (18, 'n', "'comes', 'as companion'.", "'comes', 'as companion', two short syllables, while 'frātrī' has a long a."),
 # L4 25 l: opta is 'wish', as the note and i
 (25, 'l', "choose the steep, with wings,", "wish the steep, with wings,"),
 # L5 895 'me terrent' is not turned round
 (26, 'n', "'terrent' and 'me' turned round from the first clause.",
           "the 'me… terrent' of the first clause repeated, with the real subject now named."),
 # L6 905 genua (precedent)
 (30, 'n', "'genua', here two syllables, 'gen-wa', the u a consonant,",
           "'genua', here two syllables, 'gen-wa', the u a consonant (as in the same words at 5.432),"),
 # L7 909 quies, nequiquam (scan-fix gloss)
 (32, 'n', "'nequiquam', 'in vain'.", "'quies', two syllables, quĭ-ēs. 'nequiquam', 'in vain', its first two syllables long."),
 # L8 929 late (scan-fix gloss)
 (41, 'n', "'late', 'far and wide'.", "'late', 'far and wide', both syllables long."),
 # L9 935 seu (scan-fix gloss)
 (44, 'n', "'me seu corpus… mavis', 'me, or, if you prefer, my body'.",
           "'me seu corpus… mavis', 'me, or, if you prefer, my body', 'seu' one syllable."),
 # L10 937 four words, not five; coniunx
 (45, 'n', "given up in five words.", "given up in four words; 'coniunx' is con-iunx, the i a consonant after the prefix."),
 # L11 938 rule-5b formula as 098 (803 / 806)
 (46, 'n', "corrected here: Turnus's speech ends at 'odiis', so l and i close it there while t keeps the print.",
           "corrected here: Turnus's speech ends at 'odiis'."),
 (47, 'n', "The print has 'odiis. ”Stetit', a misprint for 'odiis.” Stetit'; the mark at the head of t belongs to the speech just ended, so l and i carry none.",
           "The closing speech mark the print sets before 'Stetit' belongs to the end of the previous unit; t keeps it, and l and i carry none here."),
 # L12 X.501-505: Turnus will wish Pallas untouched, not the belt
 (48, 'n', "and the poet said then that the day would come when he wished it untouched (X.495–505, from memory).",
           "and the poet said then that a time would come when Turnus would wish Pallas untouched and hate those spoils and that day (X.495–505)."),
 # L13 cross-references checked in the pinned source: 'from memory' dropped
 (9, 'n', "(2.774, from memory)", "(2.774)"),
 (51, 'n', "(10.517–520, from memory)", "(10.517–520)"),
 (53, 'n', "(I.92, from memory)", "(I.92)"),
]
for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part', 'about', 'advisory')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    assert 15 <= len(u['n'].split()) <= 139, (k, len(u['n'].split()))
# 952 house rendering untouched (conventions.md, XI.831 = XII.952)
assert U[53]['l'].endswith("and life with a groan takes flight, chafing, down under the shades.")
assert U[53]['i'].endswith("and life, bitter at its going, took flight with a groan down among the shades.")
A.jdump(D, p)
print(len(E), 'edits applied')
