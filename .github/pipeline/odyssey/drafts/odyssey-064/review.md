# Review of odyssey-064 (Odyssey 13.217–328)

Files read: runbook.md (Reviewer paragraph and the glosser sentence), conventions.md (rules and house-rendering table), packet.md, units.json, new-renderings.md, gloss.json (second pass), known-forms.json, novel-forms.json, drafts/odyssey-001/units.json (model), drafts/odyssey-063/units.json (last unit), root odyssey-063.json, root odyssey-glossary.json, and the published parts named in the packet. No translation other than the house wording was consulted. The build was not run.

Severity scale: **major** = a false statement of grammar, position or cross-reference, or an `l`/`i` that misstates the Greek; **moderate** = a mislabel, an imprecision or a force mismatch; **minor** = consistency, tidiness, overstatement.

Mechanical checks (all pass): `t` joined equals the packet text (112 lines) and was never touched; every `ln` is the line on which the unit begins; `l` keeps the line division of `t`; `i` has no newline; `p` is on exactly the units opening Murray's paragraphs (217, 228, 236, 250, 256, 287, 291, 311); keys are only `t l i n ln v p mark`; apostrophes are U+2019 throughout.

Quotation marks: the last unit of odyssey-063 (ln 215) ends ” and the root odyssey-063.json agrees, so no speech runs into this part and none runs out of it. Five speeches, each with “ on the first unit and ” on the last, in both `l` and `i`, and `mark` on the first unit: Odysseus 228–235 (mark “Odysseus speaks”), Athena 237–249 (“Athena answers”), Odysseus 256–286 (“Odysseus answers”), Athena 291–310 (“Athena speaks”), Odysseus 312–328 (“Odysseus answers”). The introductory units (226–227, 236, 253, 290, 311) carry no marks.

Reused published lines (13.227, 237, 250, 253, 264, 282, 290, 311, 316, 317) were compared line by line with the packet: identical except where the sentence forces a change (237 opens a speech here, so “ for ‘; 250 has “she” because Athena speaks).

Scansion flags: none in the packet, so no line needed a hand scan and no scansion sentence was added.

## Pass 1 — units.json (labels in notes, Greek to `l`, `l` to `i`, remembered English, quotation marks)

Changes: 16 (major 5, moderate 7, minor 4).

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| (top) · about | minor | “laughs at his tricks”: the Greek says μείδησεν, “smiled”; she gently reproaches him, she does not laugh | “teases him for his tricks” |
| 226 · l | moderate | “At her Odysseus rejoiced, seeing her”: τήν is the object of ἰδών only; “At her” translates a pronoun twice | “Odysseus rejoiced, seeing her,” (the note already says τήν is the object of ἰδών) |
| 230 · n | major | “γε stresses σοί”: γε stands after ἐγώ (σοὶ γὰρ ἐγώ γε) and the unit’s own `l` has “I, at least” | “γε follows ἐγώ and stresses it, ‘I at least’.” |
| 232 · n | moderate | εἰδῶ called an “aorist subjunctive”; it is the subjunctive of οἶδα (the shipped glossary has “perf. subj.”) | “takes the subjunctive εἰδῶ ‘I may know’ (of οἶδα)” |
| 246 (unit beginning ἔστι μὲν ὕλη) · n | moderate | “ἔστι ‘there is’ opens the line”: ἔστι stands mid-line 246, after the ano teleia; it opens the unit, not the line | “opens the unit” |
| 258 · n | major | κατέκτανον called “an aorist without augment”; the ε- of κατ-έ-κτανον is the augment (the unaugmented form is κτάνον) | “an aorist with its augment (κατ- + ἔκτανον)” |
| 271 · n | major | same error: “κατακτείνω without augment, as at 259” | “…of κατακτείνω, with its augment, as at 259” |
| 265 · i | moderate | “I would not serve his father”: “would not” means refusal; the Greek is an imperfect “I was not serving” (and `l` says “I was not serving”) | “I did not serve his father” |
| 269 · l | major | “and not any of us / of men noticed”: reads as though ἡμέας were partitive; the Greek is “not any of men noticed us” | “and not any / of men noticed us,” (line division kept) |
| 287 · n | minor | “‘so he spoke’, masculine”: φάτο has no gender | “said of Odysseus” |
| 287 · n | minor | κατέρεξε assigned to “καταρέζω”; the shipped glossary lemma (4.610 κατέρεξεν) is καταρρέζω, and the gloss.json entry uses it | “καταρρέζω” |
| 288 · l | minor | ἰδυίῃ rendered “skilled” in `l`; the house table keeps “knowing” for ἰδυῖα in `l` (7.92, 11.432), with “skilled” allowed in `i` | “knowing splendid works” in `l`; `i` unchanged (“skilled in splendid handiwork”) |
| 306 · n | major | “under ἵνα (305)”: ἵνα stands in line 303; also “the third aorist subjunctive” could be read as “third aorist” | “the third of the aorist subjunctives under ἵνα (303)” |
| 307 · n | moderate | ἐκφάσθαι called “the aorist middle infinitive”; it is the middle infinitive of the φημί stem (shipped glossary: “mid. inf.”) | “the middle infinitive of ἐκφημί” |
| 307 · i | moderate | “that you have come home from wandering”: ἦλθες ἀλώμενος has no “home”, and `l` has “that you came wandering” | “that you came wandering” |
| 313 · l | moderate | “for you yourself to everyone liken yourself”: σὲ … αὐτήν (“yourself”) is rendered twice | “for yourself to everyone you liken.” (`i` unchanged, “liken yourself to everyone”, the house wording) |

## Pass 2 — gloss.json, and a second reading of the edited units

Every `gloss.json` entry was checked against the line(s) it parses. Key set equals novel-forms.json; no novel key is already in the shipped glossary; all new entries are under 230 characters, use only ’, and carry no line numbers; every `__broaden__` entry begins with the old entry whole and its new reading is true of the line (αὐτὴν 313, βάλον 267, κρήτῃ 256/260, μή 229, μηδέ 308, πατρὶ 265, πρίν 322, πρὸς 324, τῆς 262, τί 319, ἀντιβολήσαις 229). Every word form of the units is covered by the shipped glossary or by gloss.json.

Changes: 15 (major 3, moderate 5, minor 7). The second reading of the units (all notes, `l`, `i`, quotation marks, and the edits of pass 1) found nothing further.

| key · field | severity | what was wrong | what was done |
|---|---|---|---|
| κατέκτανον · entry | major | “epic κτάνον with κατά- prefixed”: the form is augmented (ε- of ἔκτανον); contradicted by the (corrected) notes | “augmented epic ἔκτανον with κατά- prefixed (= Attic κατέκτεινα)” |
| ἀνασχέσθαι · entry | major | “ἀνασχέσθαι = ἀνασχεῖν”: ἀνασχεῖν is the active infinitive, not an equivalent | “aor. inf. mid. (second aorist, ἀν- + ἔσχον)” |
| ἀλφηστὰς · entry | major | “grain-eating, bread-eating … epithet of mortals”: omits that the sense is disputed (convention; the unit note says it is uncertain and the translation takes “earn”) and departs from the shipped ἀλφηστάων entry | rewritten on the shipped entry: “’bread-eating’ (epithet of men); sense disputed, some derive it from ἀλφεῖν ’earn’ (’gain-winning’); masc. acc. pl.” |
| νίκα (flagged) · entry | moderate | “unaugmented, uncontracted”: νίκα is the contracted form of νικάω; the parse (impf. 3 sg., = ἐνίκα, + acc.) is right, matching the shipped ἐνίκα entry | “uncontracted” removed |
| πόθει (flagged) · entry | moderate | “unaugmented, uncontracted (= ἐπόθει)”: πόθει is contracted from πόθεε (the note says so) | “unaugmented, contracted from πόθεε (= ἐπόθει)” |
| ἠρίθμει · entry | moderate | “uncontracted -εε → -ει” contradicts itself (-εε → -ει is contraction) | “contracted -εε → -ει” |
| ἐπηετανοὶ · entry | moderate | “ever-flowing, abundant, unfailing”: “ever-flowing” is a guess the house table turns down for ἐπηετανός (it is “never-failing”; ἀενάων has “ever-flowing”); shipped entry is “abundant, never-failing” | “abundant, never-failing (sense only approximate)” |
| ποικιλομῆτα · entry | moderate | lemma “ποικιλόμητις”; the word is ποικιλομήτης (shipped entry for ποικιλομήτην, house table 7.168) | lemma corrected |
| παντὶ (flagged) · entry | minor | “masc. dat. sg.” only; παντί is masc. and neut., and an entry is general to the form | “masc./neut. dat. sg.: ’to everyone’ (or ’to everything’)”; the unit’s “everyone” stays |
| ἱκάνομεν · entry | minor | “impf. 1 pl.” only; the form is also present (the note says so) | added that the same form is also pres. |
| πολεμίζομεν (flagged) · entry | minor | same: “impf. 1 pl., unaugmented” only | added that the same form is also pres.; the imperfect reading (ἧος … πολεμίζομεν) stands |
| κιχάνω · entry | minor | “poetic by-form of κιχάνομαι/κιχάνω” is a tautology | “poetic verb; middle by-form κιχάνομαι” |
| κατέρεξε · entry | minor | “= κατήρεξε”: no such Attic form is known to me, and “ρ doubled” was unexplained; shipped κατέρεξεν has plain “aor. 3 sg.” | “καταρρέζω — stroke, caress (with the hand); aor. 3 sg., epic” |
| ἆτ (flagged) · entry | minor | “masc. voc. sg.” of an -ος adjective hid the unusual -α vocative; “unceasing” was unsupported | “insatiable; masc. voc. sg., elided (ἆτ’ = ἆτα, an unusual -α vocative)…” |
| νώνυμός · entry | minor | lemma νώνυμνος with a double ν beside a printed form with one ν, unexplained | “νώνυμνος … printed νώνυμος” |

## Findings considered and refused

- **Flagged parses kept as they stand.** πόθει (impf. 3 sg. of ποθέω, + gen.), θάρσυνάς (aor. 2 sg., unaugmented, accent from the enclitic τε), νίκα (impf. 3 sg. of νικάω, + acc.), πολεμίζομεν (impf. 1 pl.), παντὶ (dative of πᾶς), ἆτ’ (vocative, “insatiate”) are all right in substance; only the wording of the entries was corrected, as above.
- **“Odysseus answers” at 256** (the introducing formula at 253 is the non-reply καί μιν φωνήσας προσηύδα, like 228, which has “speaks”): marks are free text in the published parts, and he is answering Athena’s account of the land. Kept.
- **φίλα in φίλα γούναθ’ (231) missing from `i`:** the published parts render γούναθ’ ἱκάνω with “your knees” and no “dear” (odyssey-009, -016, -026, -031); `l` has “dear”. Kept.
- **ἐπίκλοπος glossed “thievish, sly” in the note at 291:** that is the wording of the house table (11.364); the avoided “sly” in new-renderings.md is about the English rendering, which is “thievish” / “a trickster”. Kept.
- **“Priam’s” (typographic) against “Priam's” in odyssey-010 for 316–317:** the line reuse rule binds whole units only, and the parts from odyssey-025 on use ’. Kept.
- **Note 296 “best of mortals and best of gods at the same skill”:** κλέομαι ἐν πᾶσι θεοῖσι is “famed among all the gods”; the note’s reading is the usual one and the `i` says “famed”. Kept.
- **Note 311 προσέφη “the aorist of πρόσφημι”:** the same label is used in published notes; kept.
- **ᾧ πατρί at 265 as “Orsilochus’s own father”:** the possessive ὅς may refer to a person other than the subject; the note’s reading is the natural one. Kept.
- **φασὶν gloss “accented from the enclitic”:** unclear wording, but I could not establish what Murray’s accent there reflects without a source; left, not a demonstrable error.
- **ἐπιβώτορι gloss “herdsman, shepherd”:** a dictionary meaning, not a rendering; the avoided words in new-renderings.md concern `l`/`i` only. Kept.
- **βούβοτος, εὐδείελος glossed “fem. nom. sg.”:** true of the line, though the form is also masculine; not an error (παντὶ and the two verbs were changed because their other readings are also live in the poem).
- **Unit lengths:** the cut at the comma after 261 (and at 264, 301, 305) is justified, since the sentences run 9–12 lines.

## Unresolved

None that blocks the build. Two points rest on a judgment, not on a source I could check: the lemma νώνυμνος beside printed νώνυμος (the entry now says so), and φασὶν’s accent wording (left).
