# odyssey-102 (Odyssey 21.1–100) — reviewer, pass one

Method: every note label and every position/cross-reference claim checked against the line; Greek to `l` word by word; `l` to `i`; table rows in `conventions.md` (rules, all rows for the words of this part, including the rows appended after the Scansion section); published odyssey-*.json for the words the drafter marked unknown; quotation marks; the last unit of odyssey-101; reused lines against the published units (units 31, 32, 38, 39 are identical in `l` and `i` to the published ones; reused single lines 21.1, 21.2, 21.44, 21.57 agree). `t` was not touched (checked: all 52 `t` are byte-identical before and after, and they join to the packet's 100 lines). Severity: HIGH = wrong or table-violating English in `l`/`i`; MEDIUM = false or unsupported claim, or wrong grammatical label, in a note; LOW = polish, clarity, small inaccuracy.

## Changes made (units.json, by script)

| line · field | sev | what was wrong | what was done |
|---|---|---|---|
| 46 · l, i, n | HIGH | κορώνη rendered "ring". The table fixes κορώνη of a door (7.90) as "handle" and lists "door-ring" among the renderings turned down. | `l` "loosed from the handle", `i` "slipped the strap from the handle", note now says "here the handle of the door" (the note already gave the 'crow' sense). |
| 98 · l, i, n | HIGH | ἔμελλεν rendered "was destined" / "was to be". The table row for ἔμελλεν + future infinitive is "was about" / "was about to" and lists "was destined to" as turned down. | `l` "he was about", `i` "was in fact about to be the first to taste", note now says "'was about to', the house rendering". |
| 25 (unit at 24) · n | MEDIUM (flag) | Scansion flag, line 25 (see below). The note was silent. | Added one sentence: "Line 25 is metrically irregular as transmitted: the first syllable of ἐπεί, naturally short, must be scanned long to open the line, an unresolved metrical lengthening at foot 1." Same wording as the published precedent. |
| 68 · n | MEDIUM | "κέκλυτε is a perfect imperative of κλύω". It is the reduplicated aorist imperative (published notes and the glossary say so). | Corrected to "a reduplicated aorist imperative". |
| 9 · n | MEDIUM | "The iron is the first mention of the metal that matters to the contest." False: σίδηρον is already in line 3 ("grey iron", the very thing Penelope is to set out). | Replaced: "Iron has already been named in line 3, as the 'grey iron' that Penelope is to set out; here it is part of the stored treasure." |
| 5 · n | MEDIUM | "a bent bronze bar that she will push through the door" is not in the Greek (the key is "well-bent", and it is sent in, ἧκε, at 47; nothing says it is pushed through). | Replaced by "a key, a bronze one of bent shape (εὐκαμπέα below); she uses it in line 47." |
| 48 · n | LOW | "wood and bronze" made up the material of the doors and the sound's character; the Greek says only that the noise is like a bull's. | Replaced by "The comparison is of sound only: the noise of the bolts and doors is likened to a bull's bellowing." |
| 18 · n | LOW | "the ships were large because they carried so many animals": inference, not in the text. | Clause removed. |
| 16 · l | LOW | πᾶς δῆμος that owes a debt is the folk, not the territory; the table gives "land" for δῆμος in the territorial sense but "the people" where the folk is meant (16.425 row); `i` already said "people". | `l` "the whole people owed" (was "the whole land"). |
| 16 · n | LOW | Clumsy sentence on ὄφελλε / ὀφέλλω. | Reworded: "here a by-form of ὀφείλω 'owe'; it is not the different verb ὀφέλλω 'increase'." |
| 24 · n | LOW | "(Ionic καρτερός beside κρατερός)": both are Homeric spellings; "Ionic" is a claim the note cannot back. | "(καρτερός and κρατερός are two forms of one word)". |
| 27 · n | LOW | τὴν ἥν οἱ παρέθηκεν stated flatly; the phrase is a known difficulty. | Now says it is "a difficult phrase", and that ἥν "is read as" the possessive. Translation unchanged. |
| 42 · n | LOW | "the carpenter is the same figure of skill" implies the same carpenter; the σταθμούς / στάθμη sentence contradicted itself ("not related … although connected"); no word on why the unit stops at a comma. | Reworded both; added "The unit is cut at the comma after line 45 because the sentence runs on to line 48." |
| 15 · n | LOW | τώ written with an acute; the text has τὼ. | Corrected to τὼ. |
| 67 · n | LOW | "the English adds them [quotation marks]" in a unit that has none. | Now says the speech begins in the Greek only from the verbs "and the English opens its quotation marks on the next unit". |
| 89 · n | LOW | ἀάατον: the note listed three guesses but not "ruinous", which the drafter's own new-renderings row lists as a rival reading. | Added "and so has the opposite, 'ruinous'". Translation unchanged ("harmless", unknown meaning said). |
| about | LOW | "an old guest-friend, Iphitus": nothing in the Greek makes Iphitus old. | "a guest-friend, Iphitus". |

Counts: 17 changes in all: HIGH 2, MEDIUM 4 (including the scansion sentence), LOW 11. Refused findings: 14.

## Scansion flag, line 25 (hand-scanned)

ἐπεὶ δὴ Διὸς υἱὸν ἀφίκετο καρτερόθυμον: ἐ-πεὶ | δὴ Δι-ὸς | υἱ-ὸν ἀ- | -φῑ-κε-το | καρ-τε-ρο | -θῡ-μον. Fourteen syllables, so two dactyls: foot 2 (δὴ Δι-ὸς, ὸς short before the vowel of υἱ-), foot 3 (υἱὸν ἀ-, with υἱ- as one long syllable), foot 4 (ἀφῑκετο: φῑ long, as it must be in ἵκω-compounds), foot 5 (καρ-τε-ρο, the omicron short), foot 6 θῡ-μον. Everything resolves except foot 1: ἐπεί is short-long and cannot fill a spondee unless its ε- is read long. The irregularity is real; the scanner's "UNRESOLVED / metrical lengthening at foot 1" is right. A note sentence was added to the unit at 24 (above).

## Unknown or doubtful words: consistency with conventions and published parts

- ἀμύμων (21.99): the note says the meaning is not known and keeps "blameless"; same as the table and odyssey-001/003. Consistent.
- ὄπις (21.28): "retribution", sense not certain; same as odyssey-066 and odyssey-100 and the table row (14.82). Consistent.
- δαΐφρων (21.16): "wise-minded" / "wise-hearted", doubt stated; same as the table row and odyssey-001/002/004. Consistent.
- ἀέθλια: 21.4 "a contest" follows the table row. 21.62 "contest-prizes" / "prizes from contests" departs from that row (which turns "prize(s)" down) but odyssey-034 already says the word can mean the prizes, and "contests of that lord" is not sense. Kept; see open items for the row's wording.
- ἀάατον, ὄγκιον, προσκηδής, ἐχράετ’, παλίντονος: not in any published part or in the table (checked by grep of conventions and of every odyssey-*.json `t`); each note says the meaning is unknown or provisional, in the manner of the table's ἠλίβατος / ἠνοπι χαλκῷ rows. Consistent.

## Quotation marks and neighbouring part

Speech 1: Penelope, 21.68–79: “ on the first unit (68, `mark` "Penelope speaks", both layers), ” on the last (79, both layers); no stray marks between. Speech 2: Antinous, 21.85–95: “ on 85 (`mark` "Antinous speaks"), ” on 94–95. No other marks. `p` on the units at 1, 42, 68, 80, 85, 96 matches the six ¶ in the packet. The last unit of odyssey-101 (20.394, narrator's verdict) opens and closes no speech, so nothing runs into this part. `i` has no newline; `l` line count equals `t` line count in all 52 units; no `tr`/`sc`.

## Findings considered and refused

1. ἀμφίπολος "handmaid" (21.66) against the table's "attendant(s)": the unit repeats a published unit (odyssey-004/089) and the validator requires identical `l`/`i`; the table itself (10.349 row) keeps "handmaids" for the shipped unit. 21.8 "attendant women" and 21.61 "attendants" follow the table. Refused as a change.
2. κώπη "handle" (of a key): the table's κώπη rows are for a sword ("hilt"); a key has a handle. Correct as drafted.
3. ὄγκιον "chest" and χηλοί "chests" are one English for two Greek words. The table accepts this elsewhere (δύσμορος / κάμμορος); both words are uncertain/rare. Refused as a change; see open items.
4. "recurved" in `i` for παλίντονον: close to the turned-down "back-bent", but the note says the shape is not known and `l` keeps "back-stretched"; no better English. Kept.
5. ἐπιείκελος ἀθανάτοισι(ν), κρατερώνυχας, ταλαεργοί, κειμήλια, λιγέως, κουρίδιον, ἄλκιμον ἔγχος, ξίφος ὀξύ, ἐΰξοον, πολύκμητος, ὑφορβός, νήπιος (child), πάϊς: each checked against its table row; all agree with it.
6. ἐνένιπεν "rebuked them" with the object supplied: matches the 16.417 and 19.90 rows; the note says the Greek states none. Correct.
7. ἆ δειλώ "oh, you two miserable ones / men": follows the ἆ δειλοί row; the dual shown by "you two". Correct.
8. ASCII ' in `i` possessives ("lord's", "woman's", "gods'"): the published parts mix ASCII and ’ (166 vs 98 occurrences) and neither the build nor the validator checks it. Not changed.
9. ὄγκιον / ἀέθλια / ἐπίστωρ in notes ("whether 'witness' is also meant is not certain"; "whether they were won or set is not told"): honest hedges, true to the Greek. Kept.
10. οἱ at 21.66 note ("'her' or 'beside her'"): vague but not false. Kept.
11. Unit 12 "αὖθ’ … 'on his side'", the "usually taken" remark on ὑπό in unit 11 (mule foals): recorded tradition, hedged in the note ("the Greek says only 'under'"). Kept.
12. Unit at 36 note "ἐπιείκελον ἀθανάτοισιν is the accusative of the phrase in line 14": line 14 has the nominative ἐπιείκελος; the note says the accusative of it, which is what line 37 has. Correct.
13. i drops "But" of ἀλλ’ ἄγετε (21.73) and "τότε" is kept at 21.100: force preserved; no change.
14. Title, `about`, `part`, cite match parts.json ("21.1–100"); no Murray line-number irregularity falls in this part, so no numbering remark is owed.

## Open items for pass two / the caller (not done here: not in units.json)

- new-renderings.md, ἀέθλια row: should say outright that 21.62 is a deliberate exception to the table's ἀέθλια "contest(s)" row (the row says "passim" and turns "prize(s)" down), citing the odyssey-034 note.
- new-renderings.md, ὄγκιον row: add that "chest" is also the English of χηλοί (21.51), two Greek words, one English; consider adding a χηλός "chest(s)" row, since it is not in the table.
- new-renderings.md: κορώνη of the door-strap (21.46) now follows the table's 7.90 row ("handle"); no new row needed.
- Pass two: check gloss.json parses against these edited notes (κέκλυτε, κορώνη, ἐχράετ’) and that `l`/`i` for 21.46 and 21.98 still pass the validator's repeated-line check (neither line repeats elsewhere).

# odyssey-102 — reviewer, pass two

Method: every note, label, position claim and cross-reference of the (pass-one-edited) `units.json` re-read against the Greek; Greek to `l` word by word, `l` to `i`, quotation marks recounted (only “ at 68 and 85, ” at 79 and 94, in both layers); then `gloss.json` read entry by entry against the line where each form stands (all 102 novel entries and all 13 `__broaden__` entries), and the 387 known forms read against their uses in this part for readings the existing entry does not cover. Mechanical checks on `gloss.json`: every key occurs in the part; no novel key is already in `odyssey-glossary.json`; every `__broaden__` key exists there and its entry starts with the old entry whole; all novel entries under 230 characters; no ASCII ' or backtick; no "here"; no line numbers. Every form in the 52 `t` has an entry in the glossary or in `gloss.json`. `t` was not touched (all 52 `t` byte-identical before and after; `l`, `i`, `ln` also unchanged: pass one's `l`/`i` edits at 21.46 and 21.98 were re-read and are right; neither line repeats elsewhere, so the validator's repeated-line check does not reach them). `units.json` was re-dumped by script and its formatting is unchanged. Pass one introduced no new error in `l`, `i` or the notes it rewrote.

## Changes made

### units.json (by script)

| line · field | sev | what was wrong | what was done |
|---|---|---|---|
| 22 · n | MEDIUM | "There is no finite verb in this sentence" is false: ὄλοντο is a finite verb in the relative clause. | "The main clause has no finite verb (the only finite verb is ὄλοντο, in the relative clause)". |
| 27 · n | MEDIUM | "Killing a guest at his own table broke the strongest rule of hospitality … all one offence": the Greek says the killing was in his (Heracles') house, after the table was set (ἔπειτα); "strongest rule" and "all one offence" are not in the text. | "Killing a guest in the host's own house, after setting a table before him, was a grave breach of hospitality, and the three charges … all point at that one act." |
| 53 · n | MEDIUM | "οἱ is 'around it'": οἱ is a dative pronoun ("to it", the bow); περί gives "around". Wrong label. | "οἱ is 'to it' (the bow); περίκειτο is 'lay around'". |
| 84 · n | MEDIUM | ἐνένιπεν called "the imperfect of ἐνίπτω"; the published notes (odyssey-081, -088, -091, -092) and the glossary call it the aorist. | "the aorist of ἐνίπτω 'rebuke', with movable ν". |
| 96 · n | MEDIUM | "Antinous's speech has just said that no one there could string the bow": he said he does not think it will be strung easily (οὐ γὰρ ὀΐω ῥηϊδίως … ἐντανύεσθαι). Overstated. | Now says exactly that, and "hoped to string it". |
| 5 · n | LOW | "(εὐκαμπέα below)": the word is the very next word in the same line, not below. | "(see εὐκαμπέα, the next word)". |
| 49 · n | LOW | "as the noise carries across": unsupported gloss. | Clause removed. |
| 55 · n | LOW | θεῖσα "with the case as its understood object": what is set on the knees is the bow in its case. | "with the bow in its case as its understood object". |
| 60 · n | LOW | "which is how Homer ties a later scene to an earlier one": a claim about Homer's practice that this part cannot show (conventions, Notes). | "The repetition ties this scene to the first." |
| 70 · n | LOW | "μύθου is a genitive, 'in speech'": vague; the genitive depends on ἐπισχεσίην ("pretext of speech", as `l` has it). | Now says so. |

Counts, units.json: 10 changes, MEDIUM 5, LOW 5, HIGH 0.

### gloss.json (edited in place; still valid JSON)

| key · field | sev | what was wrong | what was done |
|---|---|---|---|
| κορώνης | MEDIUM | "door-ring": the table (7.90 row) fixes κορώνη of a door as "handle" and turns "door-ring" down; the entry also contradicted the unit's note (21.46). | "curved door-handle or ring (the same word as κορώνη ’crow’); fem. gen. sg.; exact sense uncertain", in the manner of the published κορώνη entry. |
| ἐχράετ | MEDIUM | Meaning is disputed (note says "make use of" was also proposed), but the entry stated "attack, assail" flatly (rule: a word of disputed meaning says so). | "press upon, assail (+ acc.; sense disputed)". Parse (impf. 2 pl., epic uncontracted, elided) re-checked: right. |
| ὄγκιον | MEDIUM | "box or basket for implements": "for implements" is a claim nothing in the line supports. | "a container, perhaps a chest or basket (sense inferred, uncertain)". |
| ᾑρεῖτ | MEDIUM | "‘used to take’": the line has οὔ ποτε … ᾑρεῖτο, "never took"; the gloss pinned an iterative sense the unit does not have. | "’was taking, took’". |
| πινέμεν (new `__broaden__`) | MEDIUM | Line 69 has πινέμεν as the complementary infinitive after ἐχράετ’, beside ἐσθιέμεν (which glosser broadened); existing entry covers only the imperative and the infinitive after κέλεται. | Old entry whole + " · also complementary inf. after a verb of pressing or attacking: …". |
| ἀέθλια (new `__broaden__`) | MEDIUM | At 21.62 ἀέθλια τοῖο ἄνακτος is nominative (apposition to the subject σίδηρος … χαλκός); the entry says only "neut. acc. pl." | Old entry whole + " · also neut. nom. pl. (same form), in apposition to the subject". |
| τὸ (new `__broaden__`) | MEDIUM | 21.32 τὸ πρὶν μέν ῥ’ ἐφόρει: τὸ is the relative ("which", object of ἐφόρει, antecedent τόξον); the entry has no relative neut. acc. sg. | Old entry whole + " · also relative ὅς, ἥ, ὅ: which; neut. acc. sg., object of its clause (…)". |
| ᾐδέσατ | LOW | "aor. 3 sg. dep." is not a parse a reader can use. | "aor. 3 sg. mid." |
| ὄπιν | LOW | The sense is uncertain (the unit's note says so); the entry did not. | "(esp. of the gods’ retribution; sense uncertain)". |
| γωρυτῷ | LOW | "‘with the case and all’ after αὐτῷ" pins the entry to the line. | "masc. dat. sg." only. |
| ὀϊστοῦ | LOW | "partitive after γεύσεσθαι ‘taste of’" named the line's verb form. | "(partitive with γεύομαι ’taste of’)". |
| μέτα (`__broaden__`) | LOW | Example printed ἀνήρ; the line has ἀνὴρ. | Corrected. |
| all novel and `__broaden__` entries | LOW | 42 entries used ‘ … ’ for English glosses; the glossary is overwhelmingly ’ … ’ (7445 to 201) and the conventions show ’ … ’. | Every ‘ replaced by ’ (no old entry contained ‘, so no old entry was altered). |

Counts, gloss.json: 13 changes, MEDIUM 7, LOW 6, HIGH 0. All other novel entries were parsed against their lines and are right in lemma, case, number, gender, tense, voice and mood (including the duals δειλώ, κατείβετον, ὀρίνετον, κλαίετον, ἐξελθόντε, λιπόντε; the syncopated ξυμβλήτην; κέσκετ, ἐώλπει-type forms in known-forms; ἀρχήν/ἀρχὴν both fem. acc.).

### new-renderings.md

- ἀέθλια row (LOW): now states outright that 21.62 is a deliberate exception to the table's ἄεθλον "contest(s)" row (which says passim and turns "prize(s)" down), with the reason and the odyssey-034 precedent.
- ὄγκιον row (LOW): notes that χηλοί (21.51) has the same English "chest"; new row added for χηλός ("chests", fem. nom. pl.; turned down: "coffers", "boxes", "caskets") since the table has none.

Totals this pass: 26 changes (units 10, gloss 13, renderings 3): HIGH 0, MEDIUM 12, LOW 14. With pass one (HIGH 2, MEDIUM 4, LOW 11) the part's review total is HIGH 2, MEDIUM 16, LOW 25.

## Correction to pass one's record

Pass one's scansion paragraph says line 25 has "fourteen syllables, so two dactyls". Counting its own division, the line has sixteen syllables (ἐ-πεὶ | δὴ Δι-ὸς | υἱ-ὸν ἀ- | -φῑ-κε-το | καρ-τε-ρο | -θῡ-μον), which is four dactyls and two spondees. The conclusion stands: the irregularity is at foot 1 (ἐπεί, short-long, must be scanned long to fill the spondee), and the sentence added to the note at 24 says only that, so `units.json` needed no change.

## Findings considered and refused (pass two)

1. Unit 32 note, "ἑκάτερθε points to one attendant on each side": a reading, but it is the one `l` and `i` (identical to the published unit) already carry, and the validator pins them. Kept.
2. `ἐρέων` (21.31) as "asking after" (present participle of ἐρέω, a different verb) rather than the future "to tell": the standard reading for τὰς ἐρέων Ὀδυσῆϊ συνήντετο, and the broadened entry keeps the old reading whole. Kept.
3. `ἐχράετ’` from χράω (attack, assail) rather than the middle χράομαι: the elided -ετ’ can only be -ετε, so a middle (ἐχράεσθε) cannot be elided to this form; the entry now says the sense is disputed. Lemma kept.
4. `ἐφημέρια` "as a cognate object" (entry): an accusative of content with φρονέοντες; acceptable label. Kept.
5. Known-form τὰς (21.31, the mares): the entry lists "them" of other animals; the form and gender are covered, and the entry is not to be rewritten. No broadening.
6. Known-form σχέτλιος ("applied here to Zeus") and κρατερώνυχας ("of mules"): existing entries whose parenthetical names another use; the parse (masc. nom. sg.; masc. acc. pl.) covers this part. Additions only, so no change.
7. Known-form κατ’ at 21.55 and 21.90 (κατ’ αὖθι, κατ’ αὐτόθι): a fixed adverbial phrase; the entry for κατά plus the entries for αὖθι and αὐτόθι explain it, and the unit notes say "a form of κατ’ αὐτόθι 'right there'". No broadening.
8. Unit 24 note "because it would run past four lines" (unit of three lines, sentence of five): true of the whole sentence, if terse. Kept.
9. Unit 62 `l` "contest-prizes" / `i` "prizes from contests" against the table's "prize(s) turned down": kept as pass one decided; the new-renderings row now records the exception.
10. ἆ δειλώ gloss "you two wretches" beside `l` "you two miserable ones": a gloss, not the rendering; entries are not bound to the house rendering. Kept.
11. The unit-7 contrast "wise-minded" in `l` and "wise-hearted" in `i` (δαΐφρων): both are the table's accepted pair (pass one). Kept.
12. No modern translation was opened or recalled in this pass; no build was run; nothing was committed.
