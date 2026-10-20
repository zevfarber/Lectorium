# iliad-030 (5.318–415) — reviewer report

Two passes. Pass 1 was over `units.json` (grammatical labels, positions, cross-references, Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks, hand scansion, the drafter's departure and every row of `new-renderings.md`). Pass 2 was over `gloss.json` (every parse against its line, the 19 `__broaden__` entries, and the known forms for uses the old entries do not cover). No modern translation was opened or recalled. `t` was not touched (checked by script: all 52 `t` are identical before and after, and joined they reproduce the 98 lines of the packet). `ln` is right on every unit, `l` has the same number of `\n` as `t`, no `i` has a `\n`. Nothing built, committed or pushed.

Speech marks checked. 5.317 (iliad-029, last unit) is narration, so 5.318 opens with no mark. Five speeches: 348–351 (units at 348, 350), 359–362 (359, 361), 373–374 (373, one unit), 376–380 (376, 379), 382–415 (382 … 412). Each opens with “ on its first unit, which carries `mark`, and closes with ” on its last; opens and closes balance in both `l` and `i`, and no unit between 382 and 412 closes early. 5.416 (source) is narration with a ¶, so Dione's speech really does end at 415. `p` sits exactly on the five ¶ lines (318, 352, 363, 375, 381). The two published lines (5.346, 5.366) are identical in `l` and `i` to iliad-029 and odyssey-013. Cross-references checked against the lines: 1.586 (iliad-006 has "Endure, my mother, and hold out, grieved though you are" / "Endure it, my mother, and bear up, worried as you are"; unit 382 matches with "child"), 331 (ἄναλκις, yes), 336 (οὔτασε, yes), 396 (υἱὸς Διὸς αἰγιόχοιο, yes), 402 (ἠκέσατ’, yes), 404 (ἔκηδε, yes), 318, 352, 358, 375, 392, 5.346 repeat: all true. Half-line repeats compared against published parts: 322 and 324 against iliad-029 (262, 264), 326 against odyssey-094, 378 against odyssey-081, 388 against iliad-029 (311), 367 against odyssey-073, 347 against iliad-027/029.

## Hand scan of the packet-flagged lines

359 φίλε κασίγνητε κόμισαί τέ με δός τέ μοι ἵππους: 16 syllables, φῖ-λε-κα | σίγ-νη | τε-κό-μι | σαῖ-τε-με | δὸς-τε-μοι | ἵπ-πους. It needs the short ι of φίλε long in the first foot, the final -τε of κασίγνητε long at the opening of the third foot (this is also the caesura), and μοι short before ἵππους. The irregularity is real; the sentence was missing and is added (finding 13).

371 ἣ δ’ ἀγκὰς ἐλάζετο θυγατέρα ἥν: ἣ | δ’ἀγ-κὰς | ἐ-λά-ζε-το | θυ-γα-τέ-ρα | ἥν = 12 syllables, the least a hexameter can have, which fits only as six spondees; ἐλάζετο and θυγατέρα are full of short syllables, so several must be counted long. The irregularity is real; the sentence was missing and is added (finding 19).

## Changes (line · field · severity · wrong · done)

| # | line | field | severity | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 318 | `n` | minor | "μέν looks ahead to the other chariot in the next line": there is no other chariot; the next line brings in Sthenelus, and it is he who is set against Aphrodite. | "μέν sets her against Sthenelus, who comes in the next line". |
| 2 | 319 | `n` | minor | Cross-reference: Diomedes' orders were given "at the end of the last part"; they are 5.260–273, in the middle of iliad-029 (the part ends with the rescue of Aeneas). | "in the last part (5.260–273)". |
| 3 | 321–324 | `l`, `i`, `n` | minor | Same Greek half-line as 5.264 (ἐξ… Τρώων μετ’ ἐϋκνήμιδας Ἀχαιούς), which iliad-029 renders "among the well-greaved Achaeans" in both layers; here "to". Undeclared difference. | `l` and `i` "among"; note "‘among the Achaeans’". |
| 4 | 326 | `l`, `i`, `n`, new-renderings | minor | ὅτι οἱ φρεσὶν ἄρτια ᾔδη stands in odyssey-094 ("because his mind was fitted to his own", both layers). The unit used new wording ("he knew fitting things" / "his thoughts were fitting to his own") with no departure declared and no Iliad reason to depart. | Reused the published clause in `l` and `i`; note says so and keeps the word-for-word explanation; the row now records a reuse (the literal wording is listed as turned down). |
| 5 | 331 | `n` | major | "θεός is used for a goddess, with no feminine form": false, θεά exists and the unit itself uses it at 405 (and the glossary has it). | "θεός, which is common in gender, is used here of a goddess (the feminine θεά also occurs, as at 405)". |
| 6 | 338 | `n` | minor | οἱ called "the article’s old pronoun": οἱ is the enclitic dative of the personal pronoun, not the article. | "the enclitic dative pronoun". |
| 7 | 339 | `n` | minor | Claim about where a word stands: "ὕπερ standing after its noun"; in πρυμνὸν ὕπερ θέναρος it stands before θέναρος. | "ὕπερ ‘above’ governing the genitive θέναρος". |
| 8 | 341 | `n` | minor | ἔδουσ’ labelled "the epic third plural of ἐσθίω": the form is the third plural of ἔδω, the epic verb that does the work of ἐσθίω. | Label corrected. |
| 9 | 347 | `n` | minor | Two false statements: τῇ is said to stand "between" ἐπί and the verb (it stands in front of ἐπί; μακρόν is between), and the diaeresis "marks two syllables" (ἄϋσε has three; it keeps α and υ apart). | Both corrected. |
| 10 | 352 | `l`, `i`, `n`, new-renderings | major | αἰνῶς rendered "terribly"; the Iliad table (αἰνῶς … ἔοικεν, 3.158) fixes "dreadfully" and turns "terribly" down. | "dreadfully" in `l`, `i`, note; τείρω row updated and cites 3.158. |
| 11 | 353 | `n` | minor | χρόα καλόν labelled an accusative of respect, while `l` and `i` make "her fair skin" the subject; the note did not say so. | Added "which the English turns into a subject". |
| 12 | 357 | `i`, new-renderings | minor | ἐριποῦσα rendered "fell"; the table renders the stem ἐρείπω "crashed down" in both layers (γνὺξ δ’ ἔριπ’, ἔστη γνὺξ ἐριπών) and `l` here already had it. | `i` "crashed down on her knees"; row updated, "fell" listed as turned down. |
| 13 | 359 | `n` | minor | Flagged line, real irregularity, no scansion sentence. | Sentence added (φίλε long in foot 1, -τε of κασίγνητε long at the start of foot 3, μοι short before ἵππους). |
| 14 | 367 | `l` | minor | ἵκοντο "came to" in `l` but "reached" in `i`, and "reached" is the shipped rendering of the same half-line at odyssey-073 (αἶψα δ’ ἔπειθ’ ἵκοντο). | `l` "reached". |
| 15 | 368 | `l` | major | "There the horses wind-footed, swift Iris made stand": the epithets stand next to "horses" and read as describing them; the Greek has them on Iris (nominative). | "There the horses made stand wind-footed, swift Iris," (the row's phrase "wind-footed, swift Iris" is intact). |
| 16 | 370–371 | `l` | major | "…the knees of Dione, heavenly Aphrodite, / her own mother": as punctuated the English makes "heavenly Aphrodite" an apposition to Dione (and reads Dione as Aphrodite), but δῖ’ Ἀφροδίτη is the subject. `i` was right; `l` disagreed in sense. | "And she, heavenly Aphrodite, fell on the knees of Dione, / her own mother;". |
| 17 | 370 | `n` | minor | "Dione, named only here in this part": she is named again at 381. | "named here for the first time in this part". |
| 18 | 372 | `n` | minor | κατέρεξεν said to be the aorist of "κατερέζω": the verb is καταρρέζω (the glossary entry for κατέρεξεν already has it). | Corrected. |
| 19 | 371 | `n` | minor | Flagged line, real irregularity, no scansion sentence. | Sentence added (twelve syllables, only six spondees possible, short syllables of ἐλάζετο and θυγατέρα counted long). |
| 20 | 379 | `n` | minor | "Δαναοί, the third of the poem’s names for the army": on the Iliad convention's order (Achaeans, Danaans, Argives) it is the second, and nothing here counts them. | "one of the poem’s three names for the army". |
| 21 | 381 | `l`, new-renderings | major | δῖα θεάων rendered "heavenly one among goddesses", while the note says it keeps the Odyssey wording; the Odyssey table (and the Iliad rows for δῖα γυναικῶν, 3.171) has `l` "heavenly-one of goddesses". | `l` "heavenly-one of goddesses"; row updated (`i` was already right). |
| 22 | 386 | `n` | minor | Position claim: "ἐνί after its noun" in κρατερῷ ἐνὶ δεσμῷ; it stands between adjective and noun. | Corrected. |
| 23 | 388 | `n` | minor | "a hard tag on the war-god" is unclear and unhelpful about a doubtful word. | "an old tag for the war-god whose traditional sense is ‘insatiable’". |
| 24 | 391 | `n` | minor | "the imperfect of the verb that gives δαμάζω ‘subdue’": garbled. | "the imperfect of δαμνάω, a by-form of δαμάζω ‘subdue’". |
| 25 | 400 | `l`, `i`, new-renderings, gloss κῆδε | minor | κῆδε rendered "troubled" at 400 but ἔκηδε "distressed" at 404, for the same transitive verb in the same tense, while the note itself glosses κήδω as ‘distress’. | "distressed" at both; row and gloss entry brought into line. |
| 26 | 401 | `l`, `i`, `n`, `about`, new-renderings, gloss παιήων | major | Παιήων rendered "Paeon"; the Odyssey table (binding) has Παιήονος γενέθλης as "of the race of Paieon" and turns "Paean" down. The new row called "Paeon" the familiar form without noting the clash. | "Paieon" throughout (unit, note, `about`, row, gloss entry). |
| 27 | 410 | `n` | minor | "καρτερός being the Attic κρατερός": κρατερός is not Attic prose; the two are the same word with the letters transposed. | Reworded. |
| 28 | 412 | `n` | minor | "it could also mean ‘lest before long’": δήν means ‘long’; the alternative is not supported. | "the construction of the phrase is not certain, but the point … is the same". |
| 29 | new-renderings | ὤμῳ ἔνι στιβαρῷ row | minor | Row `l` "in his stout shoulder", unit `l` "into". | Row matched to the unit. |
| 30 | gloss | ἔκηδε | major | Parsed "aor. 3 sg."; it is the imperfect of κήδω (the unit note says imperfect, and κῆδε is parsed impf.). | "impf. 3 sg. act., augmented". |
| 31 | gloss | ἀβληχρήν | major | Entry gave "weak, soft, gentle" as the meaning; the unit note and the convention say the word's meaning is not known. | "meaning unknown (guessed ’weak’, ’mild’, ’tender’)". |
| 32 | gloss | ἔξαγ | minor | Parsed as aorist; ἔξαγε is the unaugmented imperfect of ἐξάγω (an aorist would be ἐξήγαγε / ἐξάγαγε). | "impf. 3 sg., unaugmented … Attic ἐξῆγε". |
| 33 | gloss | κόμισαί | minor | Meaning given as "take up, carry off, rescue"; κομίζω here is ‘tend, convey’ (`l` "convey"). | "tend, carry, convey … ’convey!’". |
| 34 | gloss | ἆτος | minor | Stated ‘insatiable’ flatly for a word whose sense is only traditional. | "(the traditional sense; formation uncertain)". |
| 35 | gloss | ὀδυνήφατα | minor | "that slays pain (… cf. ἔπεφνον)" stated as fact; the unit note says the explanation is usual but not certain. | Hedged to match. |
| 36 | gloss | ἐκίχανε | minor | "= Attic κατέλαβε" equated an imperfect with an aorist of another verb. | "(poetic; Attic καταλαμβάνω)". |
| 37 | gloss `__broaden__` | ἄναλκις (new) | minor | Known entry parses only "masc. nom. sg."; at 331 it agrees with Aphrodite (θεός, a goddess). | Old entry whole, then " · also fem. nom. sg., of Aphrodite: ’without might’". |
| 38 | gloss `__broaden__` | ὡς (new) | minor | Known entry has no ‘as if’ use; 374 has ὡς εἴ τι κακὸν ῥέζουσαν. | Old entry whole, then " · also ὡς εἴ, ’as if’ (…)". |

Counts: major 8 (5, 10, 15, 16, 21, 26, 30, 31), minor 30, total 38. `t` untouched.

## Verification of the drafter's departure and of `new-renderings.md`

- συνθεσίαι "arrangements" (5.319) against the table's συνθεσίαι "covenants" (2.339): upheld. The table row is about sworn pacts between sides, and its avoided list ("agreements", "treaties", "pacts") does not contain "arrangements"; at 319 one man lays the orders on another and the other keeps them, so "covenants" would be wrong. The row records the reason. The gloss entry agrees.
- All other rows were read against the units and the table. Rows that follow the table were checked against it: φλοῖσβος, κυανέῃ νεφέλῃ, 347 (identical to the iliad-016/027/029 pattern μακρὸν ἄϋσε), πολλὰ λισσομένη, γυναῖκας ἀνάλκιδας (Odyssey ἀνάλκις "without might"), φύλοπις αἰνή, τλάω, ἀμβρόσιον εἶδαρ, θεῶν ἕδος, ἀνίημι, στιβαρός, ὠκὺν ὀϊστόν, ἰφθίμη ἄλοχος, ἐνωπῇ, μακρὸν Ὄλυμπον "tall" (unit uses it), πελώριος "huge" (Iliad row 3.166, a word of wonder), σχέτλιος "cruel one". Corrected rows: ἄρτια, τείρω, γνὺξ ἐριποῦσα, 381, κῆδε, Παιήων, ὤμῳ ἔνι. The remaining quoted strings in the rows occur in the units' `l`/`i`.

## Findings considered and refused

- 319 `i` "had laid upon him" for ἐπέτελλε against iliad-027's 5.198 "gave instructions": refused; the object here is "arrangements", the verb is the one of 1.25 ("laid a strong charge on him"), and `l` "enjoined" matches the table's "enjoined".
- 331 `l` "a god" for θεός (`i` "goddess"): refused; `l` keeps the grammatical gender-neutral word as it does at 340 "of the god", and the note now says so.
- 342 `n` "ἀναίμονες … means without human blood": refused; it is the poem's own explanation (gods have ichor), and the row records it.
- 335 `l` "the hand at its end" / `n` "the part beyond the wrist": refused; ἄκρην χεῖρα is not certain in detail, but the note gives the exact spot as 339 does and `i` agrees.
- 339 `i` "above the palm, at its base" against `l` "at the base, above the palm": refused; the order differs but the sense is the same and the row records both.
- 358 `i` "his horses" and 357 `l` "the" horses (no possessive or article in the Greek): refused; 355–356 make them Ares' horses.
- 367 `i` omits ἔπειτα (`l` has "then"): refused; a weak sequencing particle after αἶψα, and the shipped Odyssey `i` drops it too.
- 391 `i` "for the hard bond was overcoming him" for δέ: refused; paratactic δέ here is explanatory, as the Odyssey `i` practice allows.
- 405 `i` "it is the goddess … who has urged": refused as a cleft that follows the Greek's final-position subject; no sense added.
- 408 `i` "come home from war" (`home` not in the Greek): refused; the picture is the father at home at his knees, stated in the note.
- 361 `n` the alternative ὅ = ὅτι: refused as an error; the note presents it as a possible second reading with nearly the same sense, which is true.
- 351 `n` πωλήσεαι as future middle: refused; right as labelled.
- 412 `l` "her wedded husband, the best of the Achaeans, the mighty wife of Diomedes": refused; the Greek has the same stacking, case marks the apposition to Aegialeia, and `i` is clear.
- 412 `i` "servants" against `l` "household servants": refused; the Odyssey row allows "servants" in `i`.
- 345 `i` "rescued him, holding him in his hands": refused; μετὰ χερσίν ‘in the hands’ and the note says so.
- Remembered-English check: no phrase in either layer read as an imported modern translation; nothing changed on that ground.

## Pass 2 — gloss.json

All 184 novel forms are present, none extra, and every word of the 52 units is covered by the novel list, the known list or the existing glossary. No entry is 230 characters or longer (the `__broaden__` values are the old entry plus the new reading and are exempt), none has an ASCII apostrophe, a backtick or a line number. The 21 `__broaden__` values (19 from the glosser, 2 added) each begin with the existing entry from `known-forms.json` whole, then " · " and the new reading, and every new reading is true of a form in this part: κάτα 332, μάχης 355, μὴ 388–390, οὐχ 349, πάσης 326, πέρ 340, πελώριος 395, πολέμου 348, πολὺν 334, ποτὶ 408, πτολίπορθος 333, σύ 350, τάων 319/332, τέ 350, χ 351, ἔπι 327, ἕο 343, ἥν 371, ὅττι 349/407.

The forms the glosser was least sure of:

- πετέσθην: kept. The form is the thematic secondary dual middle (πετέ-σθην, unaugmented imperfect) of πέτομαι; "impf. 3 dual, unaugmented" is right.
- ἠρύκακε: kept. Reduplicated second aorist of ἐρύκω, 3 sg.; the Attic comparison is fair.
- ἐκίχανε: changed (finding 36); parse impf. 3 sg. stands.
- ἐλήθετο: kept. Imperfect middle of λήθομαι with the genitive, as the unit note says; the Attic comparison is only a gloss.
- ἀκηχεμένη: kept. Perfect passive participle (ἀκαχίζω family), agrees with Aphrodite, and the Odyssey table's ἀκαχήμενος ἦτορ is the same word.
- ὀδυνήφατα: hedged (finding 35).
- πίνουσ’ / ἔδουσ’: kept as elided 3 pl. present indicatives of πίνω and ἔδω (with οὐ, so not participles); "= Attic ἐσθίουσι" for ἔδουσ’ is correct.

Other changes to the gloss are findings 25 (κῆδε), 26 (παιήων), 30–38 above.
