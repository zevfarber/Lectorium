#!/usr/bin/env python3
"""Reviewer's edits to aeneid-098 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n are touched;
t, ln, p, v, title, titleEn, part and about never. Run once (it refuses if the file has already been edited:
every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

E = [
 # ---------------- medium M1: missing elisions ----------------
 (4, 'n', "Elision 'circ(a) et'.", "Elisions 'ver(o) exoritur', 'circ(a) et'."),
 (7, 'n', "No elisions.", "Elision 'Quinqu(e) orbis'."),
 (26, 'n', "'potuist(i) infandum', 'dom(um) et'", "'potuist(i) infandum', 'infand(um) adcendere', 'dom(um) et'"),
 (30, 'n', "No elisions.", "Elisions 'suas(i) et', 'maior(a) audere'."),
 (39, 'n', "Elision 'ag(e) et'.", "Elisions 'Ver(um) ag(e) et'."),
 (40, 'n', "Elision 'utqu(e) est'.", "Elisions 'Sermon(em) Ausonii', 'utqu(e) est'."),

 # ---------------- medium M2: l makes Rutulos the object of fugiens (758) ----------------
 (5, 'l', "He, at once fleeing the Rutulians, at once rebukes all,", "He, at once fleeing, the Rutulians at once rebukes, all,"),

 # ---------------- medium M3: l attaches indigenas to nomen (823) ----------------
 (34, 'l', "not the old, native, name to change the Latins", "not the old name the native Latins to change"),

 # ---------------- medium M4: simile tense in i (752-755), as unit 749 ----------------
 (2, 'i', "the stag, terrified by the snares and the steep bank, ran a thousand ways forward and back;",
          "the stag, terrified by the snares and the steep bank, runs a thousand ways, forward and back;"),
 (3, 'i', "but the eager Umbrian hound clung close with gaping mouth, all but had him, snapped his jaws as if he held him, and was mocked by a bite on empty air.",
          "but the eager Umbrian hound clings close with gaping mouth, all but has him, snaps his jaws as though he held him, and is cheated by a bite on empty air."),

 # ---------------- medium M5: i, precautionary rephrasings against remembered modern versions ----------------
 (8, 'i', "it was no trifling prize of the games they were after: they were fighting for the life and blood of Turnus.",
          "for this was no slight reward, no prize of the games, that they strove for: the contest was for Turnus's life and blood."),
 (28, 'i', "“It is because I knew that this was your will, great Jupiter, that I have left Turnus and the earth, though against my wish;",
           "“It is only because I knew this to be your will, great Jupiter, that I have left Turnus and the earth behind, little as I wished it;"),
 (33, 'i', "One thing, which no law of fate forbids, I beg of you for Latium's sake and for the honour of your own kin:",
           "This one thing, which no law of fate holds bound, I implore of you for Latium, and for the dignity of your own blood:"),
 (34, 'i', "when they make peace through happy marriages (so be it), and when they join in laws and treaties, do not command the native Latins to change their ancient name, or to become Trojans and be called Teucrians, or to change their speech or their dress.",
           "when they come to settle peace with happy marriages (let it be so), when they come to join in laws and covenants, do not bid the Latins, born of this soil, give up the name they have always borne, nor become Trojans and take the Teucrian name, nor have the men change their speech or alter their dress."),
 (35, 'i', "Let Latium stand; let there be Alban kings through the long ages; let the Roman stock grow mighty on Italian courage:",
           "Let Latium live on; let Alban kings reign age after age; let the line of Rome draw its might from the manhood of Italy:"),
 (36, 'i', "Troy has fallen: then let it be gone for good, and let its name go down with it.”",
           "Troy has perished; grant that she stay perished, and her name with her.”"),
 (37, 'i', "“You are truly Jove's sister, Saturn's other child:",
           "“Sister of Jove you are indeed, the other offspring of Saturn:"),
 (38, 'i', "such great waves of anger you churn in your breast.",
           "so huge is the swell of anger that you roll beneath your breast."),
 (39, 'i', "But come, let go of this rage that you began for nothing: I grant you your wish, and yield, beaten and willing both.",
           "But come now, lay down this fury you took up to no purpose: what you want I give, and I give way, overcome and yet of my own will."),
 (40, 'i', "The Ausonians will hold on to the tongue their fathers spoke and to their own ways, and their name will remain what it is;",
           "The men of Ausonia will hold to the speech of their fathers and to their ways, and the name they bear now they will bear still;"),
 (41, 'i', "the Trojans will be merged with them in blood alone, and sink from view among them.",
           "the Trojans will be mixed with them in body only, and settle out of sight among them."),
 (42, 'i', "Their custom and the rites of their worship I will add, and I will make them all Latins of one tongue.",
           "Their manner of worship and its rites I shall add, and make them, every one, Latins speaking with a single voice."),
 (43, 'i', "The race that will spring from here, blended with Ausonian blood, you will see outstrip men and outstrip the gods themselves in devotion, and no nation will keep your festivals with equal zeal.”",
           "From here will rise a people mingled with Ausonian blood, and you will see it pass beyond men, beyond the very gods, in devotion; nor will any nation pay you honour with equal zeal.”"),

 # ---------------- low ----------------
 # L1 746 genua: agreement and scansion
 (0, 'n', "'genua', subject of 'impediunt' and 'recusant', here three syllables with the final a elided.",
          "'genua', subject of 'impediunt' and 'recusant', with 'tardata' agreeing with it (neuter plural); here it is ge-nu-a with its final a elided, so it needs no consonantal u, unlike 'genua labant' (5.432, 12.905)."),
 # L2 749 veluti siquando
 (1, 'n', "'veluti siquando', 'as if ever',", "'veluti siquando', 'just as when' (literally 'as if ever'),"),
 # L3 752 elision list form
 (2, 'n', "Elision 'ill(e) autem' and 'aut(em) insidiis'.", "Elisions 'ill(e) autem', 'aut(em) insidiis'."),
 # L4 762 excisurum quantities (scan-fix gloss)
 (6, 'n', "with 'se' left out.", "with 'se' left out; 'excīsūrum', from 'excīdo' (ex + caedo), has long -cī- and -sū-, and 'minitans' two short syllables."),
 # L5 764-765 l: 'prizes' twice
 (8, 'l', "for not light or game-prizes are sought,\nprizes, but of Turnus's life and blood they contend.",
          "for not light or sporting are sought\nprizes, but about Turnus's life and blood they contend."),
 # L6 772 stabat lengthened (scan-fix gloss)
 (11, 'n', "'stabat', 'stood', upright where it had struck.",
           "'stabat', 'stood', upright where it had struck; its -at is lengthened at the pause before 'huc' (h makes no position), and the first four feet are all spondees."),
 # L7 777 l: English name, house 'he says'
 (13, 'l', "“Faune, I pray, have pity,” he said, “and you, best, the iron,", "“Faunus, I pray, have pity,” he says, “and you, best, the iron,"),
 (13, 'n', "and l and i set 'he said' apart.", "and l and i set 'he says' apart (as 7.594, 8.439, 11.42)."),
 # L8 780 i: 'called on was not called'
 (14, 'i', "So he spoke, and the god's help he called on was not called in vain.",
           "He spoke, and called on the god for help with prayers that were not to be in vain."),
 # L9 797 l: mortali... volnere is one phrase
 (24, 'l', "By a mortal was it fitting to be violated, with a wound, a god,", "Was it fitting by a mortal wound to be violated, a god,"),
 # L10 806-807 note: placement words, mark wording
 (27, 'n', "belongs to the end of the previous unit, and is dropped here.", "belongs to the end of the previous unit; t keeps it, and l and i carry none here."),
 (27, 'n', "'Saturnia', 'daughter of Saturn', Juno's regular title, held to the end. 'submisso… voltu', 'with lowered face', framing the line;",
           "'dea… Saturnia', 'the Saturnian goddess', 'daughter of Saturn', Juno's regular title, split round 'submisso contra'. 'submisso… voltu', 'with lowered face', round 'contra Saturnia';"),
 # L11 808 quia (scan-fix gloss)
 (28, 'n', "'quia' is postponed.", "'quia' is postponed, and is two short syllables, quĭ-ă."),
 # L12 810 aeria
 (29, 'n', "'me aeria', 'me' elided before 'aeria'.", "'me aeria', 'me' elided before 'aeria', which is four syllables, ā-ĕ-rĭ-ā (Greek 'aerios'), not the diphthong ae."),
 # L13 818 exosa
 (32, 'n', "a participle of 'odi' with active sense,", "the participle of 'exodi', a compound of 'odi', with active sense,"),
 # L14 824 Troas; apostrophe
 (34, 'n', "'Troas', a Greek accusative plural, Trō-ăs, two syllables.", "'Troas', a Greek accusative plural, Trō-ăs, two syllables, the second long here by position before 'fieri'."),
 (34, 'n', "the Trojan's Phrygian clothes", "the Trojans' Phrygian clothes"),
 # L15 827 quantities (scan-fix gloss)
 (35, 'n', "'Itala virtute', ablative, 'by Italian valour'.", "'Itala virtute', ablative, 'by Italian valour', with a short I- (Ĭtălā), while 'Rōmāna' has two long syllables."),
 # L16 832 rule 5b form
 (39, 'n', "The print has no mark after 'furorem' (832); 'do quod vis' begins a new statement, so it is read as after a colon here.",
           "The print has no mark after 'furorem' (832), a misprint for a stop (a colon is read here), corrected here: 'do quod vis' begins a new statement."),
 # L17 837 adiciam
 (42, 'n', "'adiciam', 'I will add', ad- long, from 'ad-iacio' with the i a consonant.",
           "'adiciam', 'I will add', from 'ad' + 'iacio': the single i written stands for a consonantal i and a vowel i together (ad-ji-), so ad- is long by position and the word is ad-ĭ-cĭ-am."),
 # L18 838 genus... quod
 (43, 'n', "'the race which will rise from here', the antecedent drawn into the relative clause.",
           "'the race which will rise from here', 'genus', object of 'videbis', set before its relative 'quod'."),
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
    assert 15 <= len(u['n'].split()) <= 139, (k, len(u['n'].split()))
A.jdump(D, p)
print(len(E), 'edits applied')
