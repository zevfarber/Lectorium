# odyssey-101 (20.299–394) — review, pass 1 (translation)

Method: notes checked label by label, position by position and cross-reference by cross-reference against the line and against the published parts named in the packet (054 = 11.321–434, 077 = 16.1–111, 035 = 8.195–291, 091 = 18.320–428, 004 = 1.325–444, 083 = 17.101–203, 080 = 16.308–392, 074 = 15.260–350, 008 = 2.321–434, and the last unit of odyssey-100, which closes Ctesippus’ speech with ” at 298, so 299 opens plain narration). Greek read word by word against `l`; `l` against `i`; `i` for remembered English; house table consulted for every epithet and formula. Mechanical checks run by script: `t` joined reproduces the packet lines exactly; `ln` and `p` agree with the lines and with Murray’s paragraph marks (299, 304, 320, 322, 338, 345, 351, 358, 360, 363, 371, 376, 384, 387); `l` line count equals `t` line count; `i` has no line breaks; every Greek word quoted in a note is found in the part with the same accents (one exception, fixed below); “ and ” balance in `l` and `i` and sit on the first and last unit of each of the seven speeches (304–319, 322–337, 339–344, 351–357, 360–362, 364–370, 376–383); `mark` is on the first unit of each. `t` was not touched.

## Open finding for the controller (not edited: it needs a change of `t`)

**BLOCKER · unit 14 (318–319) · l, i · high** — The Greek of 318–319 is, letter for letter, the whole published unit at odyssey-077 line 108, so `validate_odyssey.py` check 6 (which compares `letters_only(t)`, ignoring punctuation) requires `l` and `i` identical to the published ones. Those end in a comma (speech still running); here Murray closes the sentence and Telemachus’ speech with a full stop, so the English must end `.”`. The two requirements cannot both be met inside this unit, and the draft as it stands will FAIL check 6. I left the English correct for the Greek as cut (full stop, closing ”) and did not edit `t`. Recommended fix, which needs the drafter or controller to re-cut `t` and which keeps every build rule (unit ≤ 5 lines; cut at a comma only where the sentence would pass four lines; and the comma after χαλκῷ is the syntactic pause between protasis and apodosis): split units 13 and 14 as **315** | **316–319** instead of 315–317 | 318–319.
- Unit A (315, ends with comma): `l` “But if now me myself to kill you are eager with bronze,” · `i` “But if you are already set on killing me myself with bronze,” · note: the existing first sentence of unit 13’s note down to “with a weapon.”
- Unit B (316–319, ends full stop): `l` “even that I should wish, and much better it would be\nto be dead than these always unseemly deeds to look upon,\nstrangers roughly handled, and the maidservant women\n(the men) dragging about in unseemly ways through the fine house.”” · `i` “I should wish even that, and it would be far better to be dead than to keep seeing these unseemly deeds, strangers roughly handled, and the suitors dragging the maidservants about in unseemly ways through the fine house.”” · note: the rest of the current notes of units 13 and 14 combined (κε with optatives; τεθνάμεν; accusatives continuing ὁράασθαι; ῥυστάζοντας masculine; the two borrowings from 11.358 and 16.107–109; speech ends here). Neither unit then repeats a published unit as a whole, and 316 and 317 keep the published wording. Units 20 and 21 (328–329 | 330–332) are already cut the same way and need nothing.

Not a defect, only recorded: the same check passes for 320 (units agree with 035 including the full stop, because the published line also ends in a full stop in `l`/`i`), 322–323, 324–325, 338, 350, 359, 363, 375 — all identical to the published English, verified by script.

## Changes made to units.json

| line · field | severity | what was wrong | what done |
|---|---|---|---|
| 302 (unit 3) · n | low | “The throw has missed by the width of a head.” A measure the Greek does not give (Odysseus bends his head ἦκα, slightly). | Replaced by “The throw misses.” |
| 303 (unit 4) · n | low | “a reduplicated aorist with the augment on top” asserts an analysis of ἠνίπαπε that cannot be checked against the dictionaries to hand. | Now “an aorist with a reduplicated stem (beside ἐνένιπε)”, which is what the forms show (ἐνένιπε is in the house table, 16.417). |
| 308 (unit 8) · n | medium | Cross-reference wrong: “ἀεικής and ἀεικέα, which return in 317 and 319”. 317 has ἀεικέα but 319 has ἀεικελίως; ἀεικής is not in 317–319 (it is at 366). | Now “ἀεικέα and ἀεικελίως, which return in 317 and 319” (agrees with the note on 394, which already lists 308, 317, 319 correctly). |
| 309 (unit 9) · n | low | χέρηα called “the epic neuter plural of χείρων (Attic χείρω)”: χέρηα belongs to the epic adjective χέρης, not to χείρων itself. | Now “the neuter plural of the epic adjective χέρης (Attic χείρων, neuter plural χείρω)”. |
| 309 (unit 9) · i | low | ἕκαστα (“each thing”) rendered “it all”; the table fixes `i` for ἕκαστα as “every detail” / “everything”. | “know it all” → “know everything”. |
| 313 (unit 11) · n | low | ἐρυκακέειν called “a reduplicated infinitive”; it is a reduplicated aorist infinitive (the present is ἐρύκω). | Added “aorist”. |
| 330 (unit 21) · n | low | “the cut at 329 was made to keep the sentence from running over five lines”: the sentence 328–332 is exactly five lines, and the convention’s limit is four. | Reworded: the sentence would otherwise fill five lines, so it is cut at the comma after 329. |
| 345 (unit 28) · n | low | ἄσβεστος “said of fire” claims a usage; only the formation from σβέννυμι is shown. | Dropped “and said of fire”; the fire-image stays, as the table’s ἄσβεστος γέλως (8.326) has it. |
| 371 (unit 45) · n | medium | “Peiraeus, a companion of Telemachus”: the note asserts something about the rest of the poem that this part cannot show. | Replaced by what the line shows: a man, not the port, who receives (ὑπέδεκτο) a guest as host, so ἐς Πείραιον is to his house. |
| 382 (unit 52) · i | medium | ὅθεν (“from where, whence”, a place) rendered “from whom”, which changes the relation to the Sicels; `l` has “whence”. | “from whom you would get” → “from where you would get”. |
| 382 (unit 52) · n | low | πολυκληΐδι quoted with a different accent from the line (πολυκληῗδι). | Quoted as printed. |
| 384 (unit 53) · i | low | “So the suitors spoke;” — the table fixes ὣς φάτο with a name filled in as “So spoke Athena …” in both layers (and ὣς φάσαν as “So they spoke”); `l` already had the same order. | “So spoke the suitors;” (now matches `l` and the unit at 345, “So spoke Telemachus;”). |
| 390 (unit 56) · n | medium | τετύκοντο labelled “imperfect middle of τεύχω”; it is the reduplicated (second) aorist middle. | Label corrected; the note adds that the English “were preparing” gives it the progressive sense the context asks for. |
| 392 (unit 57) · n | low | δόρπου labelled flatly as “the genitive, ‘as for a supper’”; with the comparative ἀχαρίστερον the genitive of comparison (“than a supper”) is an equally good parse and the line is ambiguous. | Both readings stated; the English is compatible with either. |
| 394 (unit 58) · l | low | μηχανόωντο is an imperfect; `l` had the pluperfect “had devised”. | “for earlier they were devising unseemly things.” (`i` “were the first to devise” already agrees). |

Counts: high 1 (open, above) · medium 4 · low 11 changes made (15 field edits in 13 units).

## Flagged items checked

- **318–319 repeated-line terminal punctuation** — see the blocker above. Every other repeated unit is word for word the published English; inside unit 13 the published wording for 316 and 317 is reused exactly.
- **σαρδάνιον** (301–302) — fine as drafted. The note says the meaning is not known and gives “bitter, mocking” only as the traditional guess; `l` “bitterly, so very much so” and `i` “a very bitter smile” follow the new-renderings row. “Adverbial accusative” is right for the neuter accusative. Kept.
- **ὅνδε δόμονδε** (329) — ὅνδε is the accusative of ὅδε (ὅν + δε) agreeing with the accusative δόμον that the suffix -δε has fused into δόμονδε; “to this house” is right and “to his own house” correctly avoided. Note’s statement is true.
- **κακοξεινώτερος** (376) — note states the sense is disputed and gives both readings; `l` “worse-in-strangers” is literal and `i` “worse … where strangers are concerned” leaves it open. Kept.
- **ἐπίμαστον** (377) — note says the meaning is not known and “sought-out” is only a literal guess; `l` and `i` agree. Kept.
- **ἐπιδέδρομεν** (357) — perfect of ἐπιτρέχω (δέδρομα, stem δραμ-), 3 sg with movable ν before the vowel of ἀχλύς; note “has no object in the Greek” is true. Kept.
- **Scansion flags** — packet lists none. I ran the scanner over all 96 lines: every line fits; 325, 360 and 380 carry “spondaic fifth”, an ordinary licence that the build does not treat as unresolved, so no note sentence added.

## Findings considered and refused

- Unit 0, 299: the note on Murray’s full stop at 299 (participle phrase continues in 300) is correct; no change.
- Unit 5, 304: θυμῷ “in your heart” as a dative of respect is a defensible label for this line; kept.
- Unit 10, 311: “three genitives are a genitive absolute” is loose, since σίτου has no participle, but the note says so in the next sentences; kept.
- Unit 17: “optative with ἄν as a mild prohibition” for οὐκ ἂν … χαλεπαίνοι is the published reading of this line (091); kept. “ῥηθέντι … of λέγω” is right (ἐρρήθην is the Attic aorist passive of λέγω).
- Unit 20, 329: ὑμῖν called “dative of possession” — arguable (dative of interest), but the note’s paraphrase “the heart is theirs” is what the line says; kept. ἐώλπει “past of ἔλπομαι” is vague, not false.
- Unit 21: ὑπότροπος glossed “turning back, returning” in the note while the English is “returning”/“arrived back”; the note’s gloss is lexical, the new-renderings row records the avoidance; kept.
- Unit 25: `i` drops “at all” of οὔ τι διατρίβω; οὔ τι is already carried by “not holding up”; kept.
- Unit 28: `l` “among the suitors” for the dative μνηστῆρσι and `i` “among the suitors” agree; kept.
- Unit 31 / 38 / 41 / 47: identical to the published English (enforced by the validator); cross-references 17.151, 16.345, 15.271, 2.324 checked against the packet’s unit positions in 083, 080, 074, 008.
- Unit 13 note: “316 is also said by Odysseus at 11.358, and 317 is Telemachus’ own at 16.107” — checked: 054 unit at 358 carries Odysseus’ answer to Alcinous (mark “Odysseus answers” at 355); 077 unit at 105 is lines 105–107, so 317 = 16.107; and 318–319 = 16.108–109. True.
- Unit 17 / 18 notes: 18.414–415 is Amphinomus (mark “Amphinomus speaks” in 091), and 324–325 = 18.416–417; true.
- Unit 29 and 46 notes on γελοίων / γελόωντες / γελοίωντες: forms are as printed; the note on 390 says it is “the same word in another form”, which is right. Kept.
- Unit 33: `i` “wrapped in night” — the natural rendering of εἰλύαται νυκτί, rebuilt from the verb and the dative; not a remembered phrase. Kept.
- Unit 35: `i` “hastening down to Erebus, beneath the gloom” follows the Greek order and the table’s ζόφος “gloom”; any translation of these words will be close, but nothing here is a recalled sentence. Kept.
- Unit 37: the note’s “untroubled, not forced” for ἡδύ is interpretation, but it is marked by the contrast with ἀλλοτρίοισιν at 347 that the note itself draws; kept.
- Unit 40: “The implied joke is that outside, in the open, he will find it is day.” Interpretation, not a grammatical claim; consistent with νυκτὶ ἐΐσκει and with the “sent out to the assembly” sense; kept.
- Unit 50: `i` “And now this other one” for αὖτε (l “again”); acceptable, the table reserves αὖτε “in turn” for the reply-formulas; kept.
- Unit 54: `l` “he would lay” for the future ἐφήσει after ὁππότε in a past context; fine in English sequence of tenses; kept.
- Unit 55: “ἐν μεγάροισιν goes with ἀνδρῶν” — checked: “the speech of each of the men in the halls” is the natural parse; `l` and `i` agree; kept.
- Unit 57: identification of θεά with Athena and καρτερὸς ἀνήρ with Odysseus is given as inference from 345 and 385 in the note, not as a grammatical claim; kept.
- Remembered English: no phrase in `i` arrived whole; the renderings that coincide with the Loeb prose of Murray (a meaning-check only) are literal one-word equivalents (“Erebus”, “gloom”, “phantoms”), not constructions. No modern translator named in any note.

## Pass 2

**Step A: re-cut (blocker of pass 1 closed).** Units 13–14 (315–317 | 318–319) re-cut by script as 315 | 316–319; `t` cut fresh from the packet lines (concatenation of old 13+14 equals the packet's 315–319 exactly). Unit 13 (315): `l` “But if now me myself to kill you are eager with bronze,” · `i` “But if you are already set on killing me myself with bronze,”, ends with comma, note = first half of the old note plus “the main clause comes in the next two lines”. Unit 14 (316–319, four lines, ends `.`): `l` and `i` as proposed, checked against the Greek (316 `καί κε τὸ βουλοίμην … εἴη`, 317 `τεθνάμεν … ὁράασθαι`, 318–319 accusatives continuing ὁράασθαι, ῥυστάζοντας masculine) and keeping the house wording of 054 (316) and 077 (317, 318–319) word for word except the final `.”`; neither new unit repeats a published unit whole (check 6 passes). `ln` 315 and 316, no `p`/`mark`; “ only on 304, ” only at the end of 319; quotes balance.

**Step B: second read of all 59 units against the Greek, and of every `gloss.json` parse.**

| unit/entry | severity | what was wrong | what done |
|---|---|---|---|
| 29 (347) · n | low | note called γελοίων “an uncontracted imperfect of γελάω”; gloss.json (and the form) make it γελοιάω, a by-form | note now “an imperfect of γελοιάω, a by-form of γελάω” |
| 33 (351) · n | low | “three kinds of nouns in τε … τε … τε”: νέρθε is an adverb | “The three τε … τε … τε give …” |
| 44 (367) · n | low | ἔξειμι called “the future of ἐξέρχομαι”; it is a present form (ἐκ + εἶμι) with future sense, as the gloss says | note reworded to agree with the gloss |
| 57 (392) · n | low | validator WARN: 132 words (band ≤110); the sentence “the supper is the slaughter …” was interpretation | trimmed to 104 words, interpretive sentence dropped, nothing else changed |
| gloss ἐώλπει | low | “epic augment (ἐώλπει = ἐόλπει)” invents an analysis; the form is the pluperfect of ἔολπα | “plpf. 3 sg. of the perf. ἔολπα (present sense), with imperfect force” |
| gloss ἀχαρίστερον | low | “epic for ἀχαριστότερος” asserts a form relation that cannot be checked | clause removed; entry is now lemma, comparative, case, agreement |
| gloss __broaden__ κέ | medium | new reading “from whom you would” for ὅθεν (place, “whence”); contradicts `l` and the pass-1 fix of unit 52 | “from where you would” |
| gloss __broaden__ μέσον | low | label “through the middle” but its own gloss of the example is “in the middle” | “in the middle” |

Counts, pass 2: high 0 · medium 1 · low 7 (8 changes: 3 notes, 1 note trim, 4 gloss entries). Pass 1 plus pass 2: high 1 (closed by the re-cut) · medium 5 · low 18.

Parses checked against the line and found right (no change): τετύκοντο (reduplicated aorist middle of τεύχω, 3 pl.), ἐρυκακέειν (aorist infinitive of ἐρύκω, reduplicated, and the note agrees), χέρηα (broadened: neuter plural of χέρης beside the old masc. acc. sg., both true of the line; τὰ χέρηα is the object-apposition to ἕκαστα), ἀλάληται (perfect indicative of ἀλάομαι, present sense, parallel to ἔφθιται), γελοίων (3 pl. imperfect, finite verb of οἱ in 347; participle γελοίωντες at 390 is the same verb), εἰλύαται (perf. 3 pl. mid./pass. of εἰλύω, -αται for -νται), τοῖς ἔξειμι (dative plural demonstrative “with these”, instrument; ἔξειμι present of ἐκ + εἶμι with future sense), πλέον (new reading πλέος “full”, neuter nominative agreeing with πρόθυρον, + gen. εἰδώλων; the πλέω and πλείων readings stay for other places), ζῆν (acc. of Ζεύς after μά; elided Ζῆν’), πολυκληῗδι (dat. sg. of πολυκλήϊς agreeing with νηΐ, quoted with the line’s accent), plus every other novel form and each `__broaden__` addition (βαλόντες, βίης, γήμασθ’, κατ’, νέοι, πάσχετε, περικαλλέα, τ’, ἄξιον, ἄσπετα, ἤπιον, ὁππότε) against its line. Formatting: all new entries under 230 characters, typographic ’ only, no ASCII apostrophe, no line numbers, no “here”; every `__broaden__` entry contains the old entry whole (build enforces).

Considered and refused in pass 2: lemma spelling ἀεικείη (gloss) against ἀείκεια (note, new-renderings): two spellings of one noun, no false claim, left; αἱμοφόρυκτα lemma φορύσσω (gloss) against “root of φύρω” (note, new-renderings): related roots, left; ἀλεύομαι in the note against ἀλέομαι in the glossary: LSJ variants, left; the colon in the English of 304 and 381 where Murray prints an ano teleia: ordinary English punctuation for it, left; unit 55 note’s “where she can hear” (inference, not grammar), left; unit 43 `i` “well wrought” for τετυγμένος (the participle is used of well-made things; matches the note), left.

Step C: `build_odyssey.py odyssey-101` and `validate_odyssey.py odyssey-101` run (the build was re-run after the unit 57 trim, after reverting the first build’s glossary/manifest output): PASS, no WARN. No source correction needed; `source/` and `parts.json` untouched.
