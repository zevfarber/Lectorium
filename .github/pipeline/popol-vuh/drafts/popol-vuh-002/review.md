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
