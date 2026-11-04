# iliad-153 (Iliad 24.93–199) — review

Two passes. `units.json` edited in place by script; `t` untouched (checked: every unit's `t` is still a
contiguous stretch of the edition's lines 93–199, and the units' `t` are byte-identical to before).
`new-renderings.md` updated for every rendering changed. No `gloss.json` exists yet, so no parses were checked.

Totals: 47 edit operations (23 medium, 24 low, 0 high) and **1 unresolved high-severity blocker** (unit at 144, below).

## Unresolved blocker (not changed: it needs `t`)

| line | field | severity | problem | done |
|---|---|---|---|---|
| 144 | `t` (segmentation) | **high** | The unit 144–145 ends at `εἴσω`, with no punctuation. `build_iliad.py` refuses: "unit 34 (line 144): does not end at punctuation" (confirmed by running the build, which changed nothing). It is the only build failure found. | Not fixed, because the fix changes the unit boundary and so `t`. Recommended: merge units 144 and 146 into one unit at ln 144 (5 lines, within the five-line limit, ending `ἴτω ἀνήρ.`); `t` is the two `t` joined by `\n`, `l` likewise, `i` = "…and bring word to great-spirited Priam inside Ilium, to ransom his dear son, as he goes to the ships of the Achaeans, and to bring Achilles gifts that will cheer his heart, himself alone; let no other man of the Trojans go with him.", keep `mark`, join the notes. Alternatively the drafter re-cuts after `οἶον,` (148). |

## Changes

Order of the checks: (1) notes true of the form and line, cross-references; (2) Greek → `l`; (3) `l` ↔ `i`; (4) remembered English; (5) quotation marks; (6) table conformity.

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 93 | n | medium | "Thetis, named at the end of the last part (92)": she is named at 89; 92 is the end of her speech. | "who has just finished speaking in the last part (24.90–92)". |
| 95 | n | medium | "sent from Olympus at 24.74": 24.74–76 is Zeus wishing someone would call Thetis; Iris sets out at 24.77. | 24.77. |
| 97 | n | medium | "ἐξαναβᾶσαι and ἀϊχθήτην are duals": ἐξαναβᾶσαι is a nominative plural participle (a dual would be -σα). | ἀϊχθήτην the dual; ἐξαναβᾶσαι a plural participle agreeing in sense. |
| 100 | n | low | Said Athena gave way "because the seat beside Zeus was hers", then said the Greek does not say whose seat. | "presumably yielding the seat beside Zeus". |
| 103 | n | medium | "the Greek is the same line as 1.544": 1.544 is τὴν δ’ ἠμείβετ’ …; the line is 22.167 (the unit published in iliad-139). | 22.167. |
| 104 | i | medium | Table: κηδομένη περ (1.586, 5.382) has `i` "worried as you are"; the draft said it followed 5.382 but wrote "grieved as you are". | "worried as you are". |
| 110 | n | medium | `l` "your regard and love" became `i` "my regard and love for you" with no word on the change of possessor (τεήν can be "toward you" or "that you feel"). | Sentence added: ‘your’ is taken as ‘toward you’ (Zeus's regard), and the Greek could also mean hers for him. |
| 113 | l, i | medium | Table: σκύζομαι is "sullen" (σκυζομένη 4.23, 8.483, 9.198; "angry" reserved for χόλος); χολόω is "angered/angry" (6.205, 16.320, 24.65). Draft had "angry" for σκύζεσθαι and "enraged" (kept for the speech-introduction χολωσαμένη, 3.413) for κεχολῶσθαι. | `l` "sullen at him … am angered"; `i` "sullen toward him … am angry at him". |
| 113 | n | medium | Glosses ("are angry", "am enraged", "‘be angry’", "‘enrage’", "made angry") followed the old English. | Glosses brought into line (two edits; the second found on the second pass). |
| 134 | l, i | medium | Same as 113 (second-person version). | `l` "sullen at you … is angered"; `i` "sullen toward you … is angry at you". |
| 134 | n | low | "in the second person" was loose (the persons are changed, only σοί is second person); ἑέ for the printed ἑὲ; "emphatic form" unsupported; glosses old. | Reworded; ἑὲ; glosses "be sullen", "be angered". |
| 117 | i | low | "to ransom his dear son, going to the ships": reads as if the son goes; the note itself says ἰόντ’ is Priam's. | "as he goes to the ships". Same at 146 and (first person, "as I go") at 194, which repeat the Greek. |
| 119 | i, n | medium | Table: ἰαίνω has `i` "cheered" (23.598, 23.600) and that row turns down "soothed"; draft had "soothe". | "cheer" in `i`, and the same word in the note. Same change in `i` at 146, 175, 194. |
| 123 | n | medium | "ἐπένοντο is the imperfect of ἐπιπένομαι": there is no such verb here; it is augmented πένοντο. | "imperfect of πένομαι ‘busy oneself’, with the augment". |
| 126 | n | medium | "a formula for a gentle address by a woman to a man": line 127 is also Dione to Aphrodite (5.372) and Hector to Andromache (6.485). | "a formula for a gentle address, found at 1.361 (Thetis to Achilles) and elsewhere". |
| 128 | n | low | "asks the question that Achilles is not eating or sleeping" (garbled). | "asks how long Achilles will go on without food or sleep". |
| 130 | i, n | medium | Table: μίσγομαι ἐν φιλότητι (2.232) is "mingle" in `l` and "lie … in love" in `i` (and the Odyssey row 5.126); draft had "mingle" in `i`. | `i` "it is good to lie in love even with a woman"; the note says μίσγεσθαι is the verb for sexual union. |
| 131 | l, n | low | Line 132 is 16.853 (iliad-107), whose published `l` is "near has taken its stand death and strong fate" and whose first line is "but to you already"; the part's `l` was freshly worded ("near stands …"). | Published wording reused; note says line 132 is 16.853 with the published English; ‘to you’. |
| 133 | l, n | low | Same clause as 2.26 and 2.63 (published "a messenger I am"); draft "a messenger am I". | "a messenger I am"; note cites 2.26 and 2.63. The same in `l` at 172. |
| 139 | n | low | "a real condition, since Achilles knows he has no means of checking Zeus's will except through his mother": reasoning the Greek does not give. | "a plain condition with the indicative, ‘if he really does bid it’". |
| 141 | i, n | low | Table: ἀγύρις is "gathering" in `l` and "throng" in `i` (16.661). | `i` "in the throng of the ships"; note says so. |
| 163 | l | low | `l` "heaped together", `i` "scraped together", note "scrape together". | `l` "scraped together". |
| 166 | n | low | Hand scan of the flagged line (see below): the note named the lengthening before νυοί but not the spondaic fifth foot. | Clause added to the existing sentence: the line "ends in a spondaic fifth foot, with the υ of ὠδύροντο counted long". |
| 172 | n | low | "the same phrase as in the Greek of 1.105": 1.105 has plural κάκ’ and masculine ὀσσόμενος. | "the verb of 1.105 (κάκ’ ὀσσόμενος), here singular and feminine". |
| 174 | l, i | low | Line 174 is 2.27/2.64 (only σεῦ/σευ differs); the published English is "who, though far from you, greatly cares for and pities you" / "who, though he is far from you, cares greatly for you and pities you". Draft reworded both. | Published `l` and `i` reused. |
| 174 | n | medium | "κήδεται … and ἐλεαίρει … both on the object σευ": σευ is governed by ἄνευθεν; κήδεται takes the genitive and ἐλεαίρει the accusative. | "with ‘you’ understood for both"; notes the line is also 2.27. |
| 189 | i | medium | Table: ἠνώγει is "bade" in `i` (7.386, 7.394), "told" turned down; draft "told his sons to make ready … and to bind". | "bade his sons make ready … and bind a basket on it". |

Hand scan of line 166 (θυγατέρες δ’ ἀνὰ δώματ’ ἰδὲ νυοὶ ὠδύροντο): 16 syllables, four dactyls then two spondees:
θῡ-γα-τέ | ρες δ’ ἀ-νὰ (the second foot's longum is ρες) | δώ-ματ’ ἰ- | δὲ νυ-οὶ | ὠ-δῡ | ρον-το.
Real irregularities: (a) the foot-4 longum δὲ is long only because νυός began with σν- (the note's existing sentence); (b) the fifth foot is a spondee, which needs the υ of ὠδύροντο long (the added clause); (c) θυγατέρες' lengthening and the shortening of νυοί before ὠ are ordinary epic licences and were not added to the note.

## Findings considered and refused

| line | finding | reason refused |
|---|---|---|
| 97–98, 113–116, 117–119, 120–122, 130–131, 134–135, 149–150, 161–162, 172–174, 178–179, 188–189 | Units cut at commas where the whole sentence is four lines or fewer (conventions: "never at a comma unless …"). | This needs `t` changed. The same pattern stands in published parts (10–17 per part in iliad-139, -149, -152), and the build accepts a comma. Reported, not changed. |
| 110 | "regard" for αἰδώς (the table's αἰδώς is "shame"). | Kept. "Shame and love" is not a sense the Greek can bear here; the table's own αἰδέομαι "respect" (4.402) and the 24.44 row ("the note says it can also mean respect") allow the sense; "respect" itself was kept free as the row's avoided word. The note says "ordinarily ‘shame’". Possessor question fixed above. |
| 97 | `l`/`i` "up to heaven": ἐς οὐρανόν has no "up". | Heaven is above and ἐξαναβᾶσαι already carries "up"; the sense is not changed. Harmless. |
| 107 | `l` "about the corpse of Hector and Achilles" could read as one corpse of both. | The note says ἀμφί governs both datives; `i` repeats "about". |
| 198 | `i` "my very own might and heart" for αὐτόν γε (accusative "me myself"). | Same sense in English; `l` is literal and the note says "me myself". |
| 197 | `i` "what does it seem to you … to be?" is stiff. | Drafter's avoided "what do you think" is the sense-shift the table prefers to stay clear of; the Greek is literal. |
| 144 | `i` "Be off with you" and `l` "Go, set out" | Match the 2.8 / 11.186 rows exactly. |
| 133 | `l` "and of Zeus" against published "but of Zeus" (2.26) | Δέ after a clause already opening "But give heed" would read "But … but"; "and" is the coherent choice and the word order now matches. |
| 108 | `l` "the city-sacking" after "Achilles," | Matches 2.728 (the dative epithet in `l` is "city-sacking"). |
| 106 | note: τοῦ as "relative" while `l` says "for what reason" | Both readings give the same sense; the note says "for the sake of which". |
| 11, 15 | notes' statements ("Zeus is saying that he will not let Hector's body be stolen", "which the following lines then make unnecessary") | Fair reading of the context, and flagged as the note's own gloss; kept. |
| 45 | `l` uses a verb for the dung ("scraped") where the note says "heaps on his own head" | Different verbs, different actions (καταμήσατο vs the custom of heaping on the head); both are true. |
| 191 | `l` and `i` against odyssey-072 | First line and its `i` match the published Odyssey wording; checked. |
| 103, 138 | whole-unit identity with published | Checked: `l` and `i` identical to iliad-139 (22.167) and iliad-003 (1.215). The line-level repeats at 121, 127, 159, 168, 188 were checked against the packet and agree. |
| 90–92 (iliad-152, last unit) | The neighbouring part's note begins mid-word ("ς is ‘a vain word’"). | Not this part; reported to the caller. Continuity of speech marks is fine: iliad-152's last unit closes Thetis's speech with ” and this part opens with narration. |

## Checks that passed (both passes)

- Quotation marks: six speeches, each opened with “ on its first unit (`l` and `i`) and `mark` set there (104, 128, 139, 144, 171, 194), closed with ” on its last unit (119, 137, 139, 157, 186, 198); no stray marks in between.
- "Unit begins/ends in the middle of line N" claims in the notes (113/114, 122/123, 128/130/131, 134/135, 149/150, 161/162/163, 178/179): all true.
- `l` has the line count of `t` in every unit; no line breaks in `i`; `p` on 93, 120, 138, 141, 159, 188 (the edition's paragraphs).
- Stock epithets by house rendering: δῖα θεάων, ποδήνεμος ὠκέα Ἶρις, εὐρύοπα Κρονίδης, ἀργεϊφόντης, ἐΰσκοπος, πτολίπορθος, πόδας ὠκύς, ἀργυρόπεζα, ἀελλόπος, δῖος Ἀχιλλεύς, μεγαλήτωρ, ἄμαξα ἐύτροχος, Διὸς ἄγγελος, νηυσὶ κορωνίσιν, Ἴλιον ἱρήν.
- Remembered English: none found; the phrasings are the house's.
