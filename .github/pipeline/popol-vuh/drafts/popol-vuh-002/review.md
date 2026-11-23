# Review — popol-vuh-002

## Pass 1

Reviewer pass 1, 2026-11-23. Read conventions.md, packet.md (text + establishment log), popol-vuh-001.json,
popol-vuh-glossary.json and the draft units.json. The meaning checks used only Brasseur 1861 (OCR lines 18440–19000,
K'iche' and French). No modern translation was opened. All edits were made by script; no `t` was changed and no unit
was added, removed or moved. Afterwards len(mt) == len(WORD_RE.findall(t)) holds for all 35 units.

Counts: **major 2 · minor 22 · style 5** (29 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 17 | l | major | xrah was glossed as a passive ("it-was-wanted"). It is x- + r- (3sg ergative) + ah 'want', an active singular verb. | Now "it-wanted" three times. |
| 17 | n, i | major | The note said "the animals are the subject", but the verb is singular and only qui tih 'their trying' is plural. The i ("to keep the creators' day") read qui ꜫih 'their day' as the creators' day, which the possessive does not support. | The note now gives the form and says the subject is not stated: it may be the creators spoken of as one, or impersonal. It reports Brasseur's reading. qui ꜫih is 'their day, their lot', marked inferred. The i is rebuilt: "Then a new trial of their day was wanted: that they should make another attempt, that they should set in order a new way of honouring." |
| 1 | i | minor | vxe che, caam 'the foot of the trees and vines' was dropped, and the question was recast as "that there are trees and vines". cate was dropped. | "Is the foot of the trees and vines to be only calm, only silent? It is good, then, that there should be guardians for them," |
| 1 | n | minor | The note said the singular creator "is answered by a plural". xeꜭha closes the same speech; it does not answer it. | Now says the speech is brought in with singular cacha and closed with plural xeꜭha. |
| 3 | i | minor | Chuxic stands outside the quotation in t, but the i put "So be it" inside quotes as speech. chuxic is not chuxoc. | "So it shall be, they were told." |
| 3 | l | minor | "Let-it-be" for chuxic (no -oc). The guessed senses (yaa, zacal, ychacabal) carried no mark. | "It-shall-be"; added (?) to water, brush and standing. |
| 3 | n | minor | qui poco vi ivib had no note, so a reader would take qui as 'their'. It is c- + i- 'you (all)'. chuxic was glossed 'let it be'. The letter choice in ychacabal (log) was not mentioned. | Added a sentence on qui = c- + i-. chuxic is now 'it shall be' (ch- + ux), set against chuxoc. Added the plain-c-for-Brasseur-k note on ychacabal and said that quechelah is a spelling of quichelah. |
| 3 | mt | minor | quechelah → k'iche'laj changed the vowel e to i, so the word was not respelled. | k'echelaj: the letters respelled, with the ejective supplied because the word 'forest' is certain. |
| 13 | mt | minor | Same as unit 3. | k'echelaj. |
| 0 | n | minor | Two letter decisions from the log were not mentioned: canti (plain c, B. qanti) and quichelah (qu kept where B. reads g). | Both are now said. |
| 8 | n | minor | The log's letter decision for icaharizah (plain c, B. gaharizah) was not mentioned. | Added. |
| 10 | n | minor | The log's MS/Brasseur difference xuꜩinic / x-utzitic was not mentioned. | Added. |
| 34 | n | minor | The log's looped-t reading for catit was not mentioned. | Added ("as in Ratit"). |
| 4 | l | minor | quiritah 'spread out' is said in the note to be inferred, but l stated it as fact. | Now "spread-out(?)". |
| 5 | i | minor | "its place to lie" contradicted l and n (vyacalibal 'standing-place', from yacal 'standing, raised'). | "its place to rest". |
| 7 | l | minor | hutac 'each' was glossed "each-kind". 'kind' was added to both lines of l. | "according-to each division, by each gathering". |
| 11 | l, n | minor | rumal is 3sg 'by it', but l had "by-them" (the pilot's note sets rumal against cumal). | l is now "by-it"; the note adds that rumal is singular, the animals taken together. |
| 14 | i | minor | chi ca ban (chi optative + ca- 'we') is 'let us make', but i had "we shall make them". | "let us make them now." |
| 20 | i | minor | tiha has no person prefix and is a bare command, but i had "Let us try again!" (that is ca tiha, unit 24). | "Try once more!"; the note now says there is no person prefix and compares ca tiha. |
| 21 | l, i | minor | que 'for us' is called uncertain in the note, but l had no mark. In i, "the dawn is near" was not in the K'iche' (both nouns are subjects of yopih 'has arrived'). | Added (?) twice in l; i is now "Now the sowing has come, the dawning has come". |
| 26 | l, n | minor | xqui lo 'they saw it' was stated as fact. lo is not otherwise known as a verb of seeing; the sense comes from Brasseur's French. | Now "saw(?)" in l, and the note says inferred. |
| 28 | mt | minor | chi was respelled chi, although units 4 and 7 respell the same shared-letter chi (cut) as chik, and l, n and Brasseur's French ('encore') all read chic. | chik, for consistency with 4 and 7. |
| 30 | mt, i | minor | Same chi → chik. The i dropped 'again'. | chik; "And they spoke again". |
| about | — | minor | "will keep the canyons and forests" misread the text (the canyons and forests become their home). "to be hunted" was not in the text, which says killed and eaten. | "will have the canyons and forests for their home … to be killed and eaten." |
| 12 | n | style | "-atah, the passive of xbanatah" was unclear. | "the same passive ending as in xbanatah". |
| 22 | n | style | "coh 'we'" did not separate the c- from the oh. | "coh (c- + oh 'we')". |
| 28 | i, n | style | i dropped chic 'again'. The note did not say what the toggle shows. | "spoke again"; the note now says the toggle shows chik. |
| 30 | i | style | "Count the days again, try out the shaping" broke up the single verb qui tiha, which governs both nouns of the couplet. | "Try once more to reckon its days, to find its shaping." |
| 33 | n | style | "-tah" was presented as a suffix. | "with tah, the particle of wishing, joined on". |


### Considered and refused

- **ꜭoh → koj (unit 0).** By the letter rule ꜭ would become k'. But the word 'puma' is certain as koj, Brasseur reads plain c, and the note explains the conflict. Kept.
- **Huzu → Jusuk, chi → chik (units 2, 4, 7).** These supply a letter that is shared across a word boundary. They do not restore an ejective. The log says the drafter should note huzuc / chic, and the notes do. Kept, and units 28 and 30 were brought into line with them (above).
- **que → qe 'for us' (unit 21).** If the word is uncertain, letter-for-letter would give ke. But qu→k or q is a choice the per-word mt is there to make, and the gloss 'for us' (ca-/qa- set) is what the note and l give, both marked uncertain. Kept. The glossary's `que` entry ('thus') will need a second sense.
- **Cate → K'ate (units 1, 32).** The ejective is supplied, but k'ate 'then, only then' is a certain word (B. qate). Kept.
- **"Grandmother of the Day, Grandmother of the Light" (unit 32, about).** It may echo a modern translation, but it is the literal sense of Ratit Ꜫih, Ratit Zac (r- + atit + ꜫih / zac). Brasseur has the same ('l'aïeule du soleil, l'aïeule de la lumière'). Rebuilding from the K'iche' gives the same English, so it was kept. The conventions' "avoided: Grandmother of Day" applies to Iyom, not to this title.
- **"Now that you can cry, now that you can call" (unit 7).** 'can' is interpretive, and mix is 3sg 'it has just …'. But l and n say plainly what the form is, and no more literal English reads naturally. Kept. Pass 2 may want to look again.
- **"each after its kind" (unit 7).** It has a biblical ring, but it is not a Popol Vuh translation and it renders chu hutac chobil well. Kept.
- **Ahꜯac, Ahbit as "the Builder and the Shaper" in i (units 28, 31).** These are different titles from Ꜯacol, Bitol, but they name the same pair. The l and n keep the distinction. Kept.
- **poco / poc / pocotahic (units 3, 4, 28).** Brasseur reads g (ꜫ) in all three (pogo, pog, pogotahic), and the MS is printed with plain c. This is not in the establishment log, so it is a question for the establisher, not the notes. The mt respells letter for letter (pok-), which is right while the reading stands. Flagged here only.
- **Chi byih (unit 8) as chi + y- 'you (pl.)' + bih** (Brasseur Ch'y biyh). This is possible, but the same byih follows ca- 'we' in unit 30, so y cannot be a person marker there. The note's account (a doubtful spelling of bih) was kept.
- **Paragraph flags (`p`).** None of the units has `p`. Pass 1 was not asked to set them, and they come from the packet's paragraph blocks. Left for the pipeline. Note that ¶ breaks fall before units 0, 1, 4, 7, 10, 11, 12, 17, 20, 25, 28, 32, 33 if they are set by hand.

## Pass 2

Reviewer pass 2, 2026-11-23. Read conventions.md, packet.md, popol-vuh-001.json, popol-vuh-glossary.json, units.json
(after pass 1), gloss.json and the pass 1 record. Meaning checks used only Brasseur 1861 (OCR lines 18540–18900); no
modern translation was opened. Edits by script; no `t` changed, no unit added, removed or moved, no `p` added;
len(mt) == len(WORD_RE.findall(t)) holds for all 35 units. Glossary keys are unchanged (the 203 novel forms); only
`__broaden__` gained two keys (`chi`, `rico`), and every broadened value is the old entry whole + " · " + the new reading.

Glossary form check (script: each unit's WORD_RE tokens, lowercased, zipped with mt): every entry's modern form equals
the draft's mt for that form, except `quechelah` (fixed below). `ca` (qa/ka) and `que` (ke/qe) have two mt values and
now carry both readings. Known forms whose mt differs from the published glossary: `chi` (chik in units 4, 7, 28, 30)
and `que` (qe in unit 21) — both broadened.

Counts: **major 1 · minor 17 · style 20** (38 rows).

### Changes

| unit / gloss key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| gloss `xrah` | value | major | "it was wanted, (they) wanted": the passive and the plural that pass 1 removed from the units (a major there). xrah is x- + r- 3sg ergative + aj, active singular. | "xraj — wanted; x- completive + r- 'he, it' (3sg ergative before a vowel) + aj 'want', the wanted action following as a noun". |
| gloss `quechelah` | value | minor | Modern form k'iche'laj; the draft's mt (after pass 1) is k'echelaj. | "k'echelaj — forest; a second spelling of quichelah (k'iche'laj) …". |
| gloss `ꜭohe` | value | minor | Invented morphology (k'o + "-je") and pinned to one line ("after chi of wishing"); the form is also used in kat k'oje wi (unit 3). | "be, be there, dwell; intransitive verb, the verb of k'o 'there is'", both uses cited. |
| gloss `chuxic` | value | minor | "let it be; ch- optative": pass 1 made it 'it shall be' and set it against chuxoc. | "it shall be; ch- + ux + -ik, said after a speech, beside chuxoq 'let it be'". |
| gloss `bano` | value | minor | "doing, did": it is the verb (xki b'ano 'they made it', chi qa b'ano), not a noun. | "do, make; b'an + -o, the ending of a transitive verb". |
| gloss `chu` | value | minor | "(uncertain)" with no morphology: chu is two plain things, chi + u- 'its' (unit 7) and ch- + u- 'it' (unit 33). | Both analyses given; hedge dropped. |
| gloss `hutac` | value | minor | "each, each kind": pass 1 removed 'kind' from the l because hutac is 'each'. | "each; quantifier, ju- 'one' + -taq". |
| gloss `quibil` | value | minor | "reciprocal ending" is invented. | "ki- 'their' + ib' 'self' + -il". |
| gloss `ivecha` | value | minor | "i- + wecha 'food'": the w is the prefix (iw- before a vowel), as the entry for xivech says. | "iw- 'your (pl.)' (i- before a vowel) + echa 'food'". |
| gloss `lo` | value | minor | Only 'perhaps'; the same form is the verb in xqui lo 'they saw(?)' (unit 26). | Second reading added, marked uncertain and inferred from Brasseur. |
| gloss `ꜫih` | value | minor | 'day, sun' only; unit 17 reads qui ꜫih 'their day, their lot (inferred)'. | Added "in ki q'ij perhaps 'their lot, fortune' (uncertain)". |
| gloss `nabaxtah`, `canabaxic` | value | minor | Stated as certain, though nabax 'remember' is inferred (unit 22 note, gloss `nabax`). | "(uncertain)", "sense inferred". |
| `__broaden__` `que` | value | minor | The 'for us' reading is mt qe, not ke, but sat under the ke heading. | Three readings: ke 'thus' · ke k- + e 'they' · qe 'for us' (uncertain). |
| `__broaden__` `chi` (new) | value | minor | Units 4, 7, 28, 30 show chi as chik (shared c); the published entry gives only chi. | Broadened with "chik — again: chic with its final c shared with the next word". |
| 13 | i | minor | "you shall have, but they shall be the canyons" is future (Brasseur's reading); the K'iche' and l are completive/perfect (xivech 'became yours', mixe vuxic 'have become'). "lairs and dens" broke the rendering of unit 5. | "your food and your fodder, your places to sleep and your places to rest, are yours there; they have become the canyons and the forests, …". |
| 31 | l, n | minor | chire is singular ('to him, to her', so the note), but l had "to-them". | l "to-him/her"; note says the pair is spoken to as one, as with catoc. |
| 33 | l, n | minor | Same with chirech: l "to-them". | l "to-him/her"; note adds that chirech is singular. |
| 33, 34 | l | minor | nabaxtah, canabaxic 'remembered' unhedged, though unit 22 says the sense is inferred. | "remembered(?)", "our-being-remembered(?)". |
| gloss `cacha` | value | style | "k- 'ongoing'" against the note's ca-. | "ka- 'ongoing action'". |
| gloss `ychacabal` | value | style | Morphology skipped the root. | "+ a root chak not otherwise known + -ab'al". |
| gloss `camo`, `yao` | value | style | Pinned to xu ("after xu"), meaning given as past. | "take" / "give"; -o transitive ending, with the phrase as example. |
| gloss `ꜭhavahe` | value | style | "(let)" belongs to tah, not to this word. | "speak (uncertain form) … (kix ch'awaje taj 'speak, you all')". |
| gloss `coh` | value | style | "pronoun before a verb" contradicted its own "k- 'shall' + oj". | "we, us (shall); k- + oj, before a verb". |
| gloss `icaharizah` | value | style | "us" comes from coh, not from this word. | "you (all) praise, honour (uncertain)". |
| gloss `xcoꜫibeh` | value | style | "it cried out": the subject is each of the animals (l "they-cried(?)"); no morphology. | "cried out (uncertain); x- completive + a verb not otherwise known". |
| gloss `vbixic` | value | style | Root given as b'i 'say' (that is b'i' 'name'). | b'ij 'say'. |
| gloss `xꜭha` | value | style | "(they) said": the form is singular (subject Alom, Ꜭaholom taken as one). | "said; … the singular of xech'a". |
| gloss `tihtobeh` | value | style | "with verb ending". | "+ -ej, transitive verb ending". |
| gloss `tiyic` | value | style | No morphology; doubtful reading not said. | "doubtful reading, perhaps ti' 'eat' + -ik". |
| gloss `yoh` | value | style | "(uncertain)": the units treat yoh 'undo' as known (unit 26 note; l unhedged); the inferred sense in unit 29's note is yoc's. | Hedge removed. |
| gloss `mucun` | value | style | "(uncertain)" while l and n are unhedged; Brasseur reads 'could not see behind' here and the verb recurs later in his text (x-e mucunic). | "look, see; verb". |
| gloss `vꜭhan` | value | style | "its speech" only; it is used in xe vꜭhan qui quib 'they spoke among themselves'. | "speech, speaking", with the phrase. |
| `__broaden__` `ta` | value | style | New reading lacked a modern form and the format of the others. | "· ta — hear, understand; transitive verb (xki ta 'they heard')". |
| `__broaden__` `rico` (new) | value | style | Published 'they found'; here chu rico 'let it find'. | "· riqo — find, in chu riqo 'let it find' (ch- + u- 'it')". |
| 8 | l | style | "Let-you-say": no 'you' prefix (pass 1 refused y as a person marker). | "Let-(you)-say", as unit 15's "let-(you)-take". |
| 15 | i | style | "now" is not in the K'iche' (it is Brasseur's 'Maintenant'); xa 'only' dropped. | "Take up your service, and only that: your flesh shall be eaten." |
| 30 | i | style | "to reckon its days, to find its shaping": 'find' is invented; the K'iche' has two passive nouns, 'its being day-counted, its being shaped'. | "Try once more: let its days be counted, let it be shaped." |
| 32 | i | style | "the word was given" for vbixic 'its being said'. | "Then it was told to the diviners". |

### Considered and refused

- **Unit 7 "Now that you can cry, now that you can call" and "each after its kind"** (pass 1 left both for pass 2). Both come straight from Brasseur's French ("puisque la puissance de bramer et de gazouiller (vous est donnée)"; "chacun suivant son espèce, chacun suivant son genre"), the permitted check, not from a modern translation; l and n state the forms. Kept.
- **Unit 13 future tense as Brasseur's** — Brasseur has "vous les aurez; (mais) ce seront les ravines", but the K'iche' verbs are completive/perfect and l follows them; i was brought into line with l (above), not with Brasseur.
- **gloss `nuc` = nuk' (ejective supplied).** nuk' 'arrange' is a certain word; the mt and gloss agree, and the note gives Brasseur nuq. Kept.
- **gloss `chau` = ch'aw, `iziquih` = isik'ij (ejectives supplied).** Certain words (ch'aw 'speak', sik'ij 'call'); within the mt rule. Kept.
- **gloss `xivech` (x- on a possessed noun).** Odd, but it is the note's own analysis, and the gloss agrees with it. Kept; a question for a later pass on Classical K'iche' grammar.
- **known `chauaxoc` "root chaw 'sow'"** against `ravaxic` "awax 'sow'" here (ch- + awax would be consistent). The published entry is outside this part's keys and was not broadened. Flagged for the glossary owner.
- **l "let we make" (units 14, 30) against "let-us make" (unit 21).** chi ca ban(o) has a separate chi 'let' and ca- 'we'; ca bana has no chi. The difference is in the K'iche'. Kept.
- **Ahꜯac, Ahbit as "the Builder and the Shaper" in i; ahbit "the shaper" in unit 33.** As pass 1. Kept.
