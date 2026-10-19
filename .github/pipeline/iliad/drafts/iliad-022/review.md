# iliad-022 review (Iliad 4.85–182)

Reviewer, two passes. Pass 1: every grammatical label, where-a-word-stands claim and cross-reference in the notes checked against the line and against the published parts (iliad-015, -019, -021, odyssey-014, -073); no note left contradicting its own `l`/`i`. Pass 2: Greek to `l` word by word (case, tense, mood, particles), `l` to `i`, remembered English, quotation marks and `mark` fields, the two scansion flags by hand, and `gloss.json` (it existed at the start of pass 2: 224 entries, 223 novel forms plus `__broaden__`; every parse checked against its lines). `t` was not touched (verified by script: every `t` identical before and after, the joined `t` equals packet lines 85–182, key order of every unit unchanged). Line division of `l` equals that of `t` in all 64 units; no `\n` in any `i`; every note is at most 108 words; `p` stands on exactly the five units the edition opens a paragraph at (85, 104, 127, 141, 148).

## Changes to units.json

| line · unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| about | about | medium | "the bow he made from the horns": the text (110) says a horn-working craftsman (τέκτων) made it; Pandarus only strings it. | "the bow made from the horns of a wild goat he once shot himself". |
| 4.88 | n | medium | "an archer whose name appears here for the first time": Πάνδαρος is already named in the Catalogue, 2.827 (iliad-015, unit at 2.824, with Zeleia and the bow from Apollo). | "the archer from Zeleia already named in the Catalogue (2.827)". |
| 4.93 | n | medium | Note said "the sense is a polite ‘would you …?’" while `l`/`i` render a statement ("you might obey me"): the note contradicted its own `l`/`i`. | Note now says the English keeps the statement the edition's full stop gives, the proposal follows in 94–96, and ἦ ῥά νύ … could also open a question (see adjudication 1). `l`/`i` unchanged. |
| 4.97 | i | low | "above all" for πάμπρωτα (note says "first of all"; `l` "before all others"): "above all" is "most of all", which 96 has already said of Alexander. | "first of all". |
| 4.97 | n | low | Asserted that παρ’ "belongs with" τοῦ; it may as well be in tmesis with φέροιο. | Both named; "either way ‘carry off from him’". |
| 4.108 | n | low | "the rock it was climbing down": ἐκβαίνοντα πέτρης (107) says "coming out from a rock"; nothing says the same rock or a climb. | "falls back upon the rock". |
| 4.112 | l, n | low | `l` and note gave ποτὶ γαίῃ as "toward the ground"; ποτί here takes the dative (at, against), not the accusative of motion, and `i` already had "against the ground". | `l` "against the ground"; note "with the dative, is ‘against the ground’". |
| 4.113 | i, n | low | "might not spring up before Menelaus … was hit" reads as "before Menelaus" the person; μὴ πρίν … πρὶν βλῆσθαι is "not until … was struck". | `i` "until Menelaus … was hit"; note says ‘until’ in the English. |
| 4.125 | l | low | `l` "sharp-pointed" for ὀξυβελής collided with the house `l` "sharp-pointed" for ἐχεπευκής (see 4.128). | `l` "sharp-shafted" (ὀξύς + βέλος); `i` "sharp-pointed" kept. |
| 4.125 | n | low | "ἐπιπτέσθαι … ‘fly at’" while `l` says "fly onward". | Note gives ἐπιπέτομαι "fly at, fly on", here "fly onward"; also names ὀξυβελής "sharp-shafted". |
| 4.127 | n | medium | "its second adjective is held back to the end of the line … before the one god who matters is brought in at the start of 128": ἀθάνατοι stands at the start of 128, not at the end of a line, and Athena is brought in later in 128. | "carried over into the first word of 128, with a comma, before the one god who matters is brought in". |
| 4.128 | l, n | medium | `l` "the sharp shaft" for βέλος ἐχεπευκές; the table row ἐχεπευκής (1.51) is `l` "sharp-pointed", `i` "sharp", and iliad-001 shipped "sharp-pointed" at 1.51. The departure was not recorded in `new-renderings.md` (row 30 said "follows 1.51"). | `l` "the sharp-pointed shaft" (`i` "sharp shaft" was right); note says so; `new-renderings.md` rows 28 and 30 corrected. |
| 4.132 | n | low | "the broad belt that holds the breastplate in place": more than the line says. | "the broad belt worn at the waist". |
| 4.136 | l, n | low | `l` "… it was driven / and the belly-guard, which …" has no construction: μίτρης θ’ is a genitive after the διά of the first line. | `l` "and (through) the belly-guard" (parenthesis as elsewhere in `l`, e.g. "wondrous (power)"); note says "after the same διά". |
| 4.140 | n | low | "ὠτειλή is a wound that is open" (vague, not a lexical fact). | "a wound, here the cut the arrow made". |
| 4.144 | n | low | "the Odyssey ships ‘a glory’ for it": workshop jargon in a reader's note. | "the Odyssey renders it ‘a glory’". |
| 4.146 | n | low | μιάνθην left without number; τοι "to you" while `l` says "your". | "third-person plural aorist passive"; τοι "to you, turned into ‘your’ in the English". |
| 4.155 | n | low (scansion flag, real) | Flag UNRESOLVED had no metrical remark. Hand scan: φῖ-λε κα | σῖγ-νη | τε θά-να | τὸν νυ τοι | ὅρ-κι ε | ταμ-νον. It scans only if the first syllable of φίλε is lengthened for the long of foot 1 and the short final syllable of κασίγνητε counts long in foot 3 (τοι before ὅρκι’ is ordinary correption). The scanner reports the same. | One sentence added to the note (108 words). |
| 4.157 | n | medium | "ὥς, with its accent, is ‘so, thus’": the accent proves nothing; ὥς σ’ may be ὡς + enclitic σε, and a proclitic takes an acute before an enclitic (the glossary's own ὥς entry says so). "Could also be read ‘since’" was then unexplained. | Note says ὥς σ’ may be ὡς + σε with the accent from the enclitic; read "so, thus", could be "since". `l`/`i` unchanged. |
| 4.158 | n | low | "ἐπέπιθμεν … a perfect of πείθομαι": it is the augmented epic pluperfect of πέποιθα (imperfect sense); ᾗς left unparsed. | "ᾗς is the epic dative plural of the relative, and ἐπέπιθμεν is the pluperfect of πέποιθα (πείθομαι) used for ‘we trusted’". |
| 4.166 | n | medium | "ἐπισσείῃσιν is an aorist subjunctive": no σ before the ending, so it is the present subjunctive of ἐπισείω (aorist would be -σείσῃ-). | "a present subjunctive with the old ending -σιν" (the glossary entry already says pres. subj.). |
| 4.166 | n | low | "the fearful cover Zeus shakes": the aegis is not shown to be a cover; ὑψίζυγος "built on ὕψι and ζυγόν" stated as fact. | "The aegis is what Zeus shakes to bring terror"; ὑψίζυγος "is explained from ὕψι … and ζυγόν …, but its exact sense is not certain". |
| 4.171 | n | low | "Odysseus used it of Agamemnon at 2.284": the word ἐλέγχιστον is in 2.285 (iliad-010, the unit begins at 284 but the word is in its second line); "the word for disgrace" was vague. | "2.285"; "the superlative of ἐλεγχής ‘shameful’". |
| 4.173 | n | low | "κὰδ with the δ taken from the next consonant" garbled; "her full name". | "κὰδ because the τ of κατά becomes δ before the δ of δέ"; "her usual title". |
| 4.178 | n | low | "χόλον τελέσαι": that infinitive is not in the line; the text has τελέσει’. | "χόλον τελέσει’". |
| 4.85 | n | low | "closes the onlookers’ speech" (the speech closed at 84); "the story moves from the gods to the field" (it moved at 78–79). | "the narrator’s tag on the onlookers’ speech"; "turns from the onlookers to what Athena does next". |

Counts: medium 7, low 19, high 0 (one row per finding; a finding that touched two fields is counted once).

## Changes to gloss.json

`gloss.json` existed at pass 2. All 223 novel forms present, none extra, none already in the glossary, all under 230 characters, typographic ’ only, no line numbers. All 18 `__broaden__` entries the glosser wrote start with the old entry whole plus " · " and each new reading is true of its line in this part. Fixes:

| form · line | severity | what was wrong | what was done |
|---|---|---|---|
| λέξεται · 131 | medium | "fut. mid. 3 sg.: ‘she will lie down’": the one lying down is the child (παιδός), not a woman; the line also reads as a general clause. | Subject dropped; "fut. mid. 3 sg., or short-vowel subj. in a general clause: ‘will lie down’". |
| τελεῖ · 161 | low | "fut. 3 sg." while the note and `l`/`i` read a present ("fulfils"); the contracted form is the same in both tenses. | "3 sg. contracted from τελέει, pres. or fut." |
| ἄμυνεν · 129 | low | "aor." while the note says imperfect; ἤμυνε is the same form in both. | "impf. or aor. 3 sg., unaugmented". |
| κυκλοτερὲς · 124 | low | "predicative with τόξον" while the note takes it as an adverb ("into a circle"). | "used adverbially: ‘into a circle’". |
| ἐπεστενάχοντο · 154 | low | gloss "groan in answer" is the reading `new-renderings.md` avoids (decides a response). | "groan in addition, groan along with". |
| κῦδος (broaden) · 145 | low | old entry "neut. acc. sg."; in 145 κῦδος is the nominative in apposition to ἄγαλμα. | Added `__broaden__` entry (19 now): old entry whole + " · also neut. nom. sg., in apposition: ‘glory’". |

Noted, not changed (existing glossary, outside this part's gloss): the published entry for ἕποντο says "impf. 3 pl. mid., augmented (ἕποντο = εἵποντο)"; the form is unaugmented (as the note at 90 says). Existing entries are not to be rewritten here; flag for a later cleanup.

## Adjudication of the drafter's doubtful points

1. **4.93–96, statement or question.** Kept as statements (the edition prints full stops at 93 and 96; the three optatives τλαίης κεν … ἄροιο run on as one proposal; same course as iliad-021 at 4.82–83). The note now names the question reading. `i` "Surely" kept for ἦ ῥά νύ (the free layer; `l` has "Truly now").
2. **μίτρη.** "belly-guard" kept: the usual explanation (metal guard for the lower belly under the belt); the note says "the usual explanation".
3. **ὑψίζυγος.** "sitting on high" kept; "high-throned" would use θρόνος. Note hedged.
4. **Λυκηγενής.** "Lycia-born" kept; the note (101, 119) says the sense is not certain and names "wolf-born" and "light-born".
5. **ἴξαλος.** "bounding" kept; note says it is the usual explanation and not certain.
6. **ἕρμα … ὀδυνάων.** "the prop of black pains" kept; the note says the figure and exact sense are uncertain. ἕρμα "prop" matches 1.486.
7. **κορώνη.** "tip" kept; note says literally "crow", a curved end-piece by the usual explanation.
8. **νεῦρον / ὄγκοι (151).** "the sinew", "the barbs" kept; note says "probably the binding … and hooks of the head". Not the bowstring of 122 (νεῦρα βόεια), which the note at 122 keeps apart.
9. **ὥς 157.** "so" kept; note corrected (see above).
10. **ἀπέτισαν 161.** Gnomic aorist, "they pay" in `i`, `l` "paid back"; kept: the sentence is a general truth (εἴ περ … τελεῖ), and "paid" would make it past narrative.
11. **ἐπισσείῃσιν 167.** `l`/`i` "shall shake" kept (the subjunctive depends on ὅτ’ ἄν in 164); label corrected.
12. **μιάνθην 146.** Third plural aorist passive, "were stained", agrees with μηροί; kept.
13. **Zeleia.** Kept as a name; Pandarus' home town, as the Catalogue (2.824) places it.

## The flagged lines

- **4.135** (`διὰ μὲν ἂρ ζωστῆρος ἐλήλατο δαιδαλέοιο`): hand scan δῑ-ὰ μὲ | νἀρ ζῶ | στῆ-ρος ἐ | λή-λα-το | δαι-δα-λέ | οι-ο. Regular hexameter; the only licence is the ordinary lengthening of διά in foot 1. The scanner's UNRESOLVED comes from the unmarked quantities of the α in ἐλήλατο and δαιδαλέοιο, not from an irregularity. **Not real; no sentence added.**
- **4.155**: real; sentence added (see table).

## Quotation marks

Neighbouring part: iliad-021's last unit (4.82–84) closes the onlookers' speech with ” and carries `mark` "Someone in the crowd speaks"; no speech runs into 4.85 and unit 1 here (85) correctly has no opening mark. In this part: Athena (as Laodocus) 93–103: “ on 93, ” on 103, `mark` on 93. Agamemnon 155–182: “ on 155 (`mark`), ” on 182. The inner Trojan speech 178–181: ‘ on 178 (`mark` "A Trojan speaks, as Agamemnon imagines it"), ’ on 180–181; the end of Agamemnon's speech at 182 (ὥς ποτέ τις ἐρέει· τότε μοι χάνοι …) is outside the inner quotation, as the Greek has it, and carries ”. Same marks in `l` and `i`. Checked by script: no stray quotation mark anywhere else. All correct; no change.

## Reused lines

4.136 (first line): `l` "and through the much-wrought breastplate it was driven" and `i` "was driven … through the richly wrought breastplate as well" follow iliad-019 (3.358); only the sentence frame differs. 4.163: whole unit, `l` and `i` identical to odyssey-073. 4.165: `l` wording and `i` "Ilium … and Priam, and the people of Priam of the good ash-spear" follow iliad-021 (4.46–47). 101–103 = 119–121: identical except the person, as the note says.

## Findings considered and refused

- **4.105 `i` "bared" for ἐσύλα (`l` "stripped").** The object is the bow and the note says why ("taking the bow out of its covering"); same verb as σύλα at 116 ("took the lid off"). Refused.
- **4.106 `i` word order ("beneath the breast" after "from a rock").** Reads as the place of the shot, which is what ὑπὸ στέρνοιο is; `l` has the Greek order. Refused.
- **4.112 `i` "strung" for τανυσσάμενος.** The usual sense of τανύω with a bow; the note and `l` ("having stretched it") show the word. Refused.
- **4.122 `l` "ox-sinews" vs `i` "string".** Plural for one string, said in the note. Refused.
- **4.124 κυκλοτερές as adverb vs predicate adjective.** Same form either way; `l`/`i` ("into a circle") serve both. Refused.
- **4.158 `l` "Not at all in any way" omits the asseverative of οὐ μέν πως.** The note gives "surely not in any way"; `i` "No," carries the force. Refused.
- **4.160 `i` "has not fulfilled" for aorist οὐκ ἐτέλεσσεν (`l` "did not fulfil").** English present perfect for a general protasis; sense identical. Refused.
- **4.161 τελεῖ as present or future.** Same contracted form; `l`/`i` present, note present, gloss now "pres. or fut." Refused as a change to `l`/`i`.
- **4.164 `i` drops "at some time" (ποτ’).** `l` has it; note explains ὅτ’ ἄν ποτ’. Refused.
- **4.172, 4.171 `i` "very thirsty" vs `l` "much-thirsty" for πολυδίψιον.** Table row, recorded in `new-renderings.md`. Refused.
- **4.176 `l` "over-bold" / `i` "overbearing".** The Odyssey table's pair for ὑπερηνορέοντες (6.5). Refused.
- **4.178 ἐπὶ πᾶσι "on all" ambiguous (all the Achaeans or all men).** The note already says so. Refused.
- **4.182 note "swallowed alive".** Inference about the wish, and Agamemnon is alive when the Trojan would speak; kept as a reading of the image. Refused.
- **`i` "dark as a cloud", "winged words", "lord of men", "blessed gods", "dear to Ares", "the driver of spoil", "in the bright upper air", "sweet sleep", "bulwark against javelins".** All the table's renderings; no English phrase in `i` arrived fully formed that the grammar does not give. "fill up the doom of your life" and "the plough-land will rot your bones" are built from πότμος / ἄρουρα as the table has them. Refused.
- **Every other note label, cross-reference (εἴπεσκεν at 81; Athena's descent at 78; ἀνεδύσετο 1.496; ἅλιον 4.26; ἀτέλεστα 4.26 and 4.57; 4.46–47; εὐχωλήν 2.160; κυδάλιμος of Menelaus in the Odyssey; σύλα 105/116; ὀϊστός/ἰός 116/118; 3.358; κελαινεφές 140) and Greek-to-`l`-to-`i` correspondence** checked and found true.
