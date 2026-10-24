# iliad-060 (Iliad 10.194–294) — review

Two passes, run by script on `units.json`; `t` was not touched (the three merges below join existing `t` strings with the line break the edition prints between them; the tiling check against the edition still passes). Unit count 98 -> 95. Every change is listed as: line · field · severity · what was wrong · what was done. Lines are the line the unit starts on.

Checks run: tiling against the edition (as `build_iliad.py` does it), end-of-unit punctuation, `p` against the edition's paragraph marks (194, 218, 227, 240, 248, 254, 272, 283: all correct), `l` line counts, quotation marks (7 openings and 7 closings in each layer; `mark` on the first unit of each of the seven speeches; Nestor's speech from the previous part closes at 10.192 in iliad-059 and this part opens with the narrative), note length band, and the validator's repeat rule (see "Validator and repeated lines").

## Cross-references (all checked against the published JSON files in the repository root)

| Reference in a note | Result |
|---|---|
| 8.489 (note on 199) | Exists (iliad-051, unit at 489). The line is the same, but the drafter's English did NOT follow it, and the note's gloss contradicted it: see 199 below. |
| 3.95 (note on 218) | Exists (iliad-017, unit at 95); English identical. The note's "and in the Odyssey" was loose: the Odyssey has οἱ, not οἳ (odyssey-035 234 etc.). Fixed. |
| 3.96 (note on 219) | Correct (iliad-017 96, same shape with Menelaus). |
| 3.455 (note on 233) | Correct (iliad-020 455, English identical). |
| 9.676 (note on 248) | Correct (iliad-057 676, English identical). |
| Odyssey 1.65 (note on 243) | Correct (odyssey-001 65: the line is the first line of that unit, spoken by Zeus). |
| 4.372 ff. (note on 285) | Correct: Agamemnon's tale of Tydeus at Thebes, iliad-025, 4.372–399 (Asopus at 4.383). |
| Odyssey 3.382–384 (note on 292) | Correct (odyssey-012, units at 382 and 384; English identical in both layers). |
| Odyssey 3.442 (note on 255) | Correct (odyssey-013, unit at 440 contains 442: μενεπτόλεμος Θρασυμήδης, "steadfast in battle"). |
| "line 261 = 257", "272 repeats 254", "196", "255", "220", "204–210", "235/236" | Internal, all true. |

## Validator and repeated lines (the drafter's note on 10.218)

`validate_iliad.py` (rule 6) keys a unit by `letters_only(t)` (Greek letters only, so punctuation and accent-free differences in stops do not matter) and, if the same letters stand in an earlier published Iliad unit, requires `l` and `i` to be EXACTLY the published strings, punctuation of the English included. So 10.218 (t ends with a full stop; 3.95 ends with a raised dot) must carry the English of 3.95 as published, `;` at the end of both layers, though `t` ends with `.`. The draft already does; nothing to change. The same rule, run by hand over all units, found one failure the drafter had missed (251, below). The Odyssey comparison (rule 6b, warning only) shows no differences. `build_iliad.py` separately requires every unit's `t` to end in `. ; · ,`.

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 199 | `i`, `n` | major | The line is word for word 8.489, and the note said the English follows it, but the English read the other way: 8.489 has "the ground showed through, free of the dead" (νεκύων = separation), while this unit had "the place of the dead as they fell", and the note glossed it "the open ground lay where the dead had fallen". Same Greek, opposite sense. | `i` -> "where the ground showed through, free of the fallen dead;"; note now states the genitive of separation and what πιπτόντων adds. `l` was already the published `l`. |
| 222 (222–223) | `t` join, `l`, `i`, `n` | major | The unit ended at line 222 with no punctuation (ἀλλ’ εἴ τίς μοι … ἄλλος); the build refuses ("does not end at punctuation"). The note also said μοι goes "after ἅμα"; it goes with ἕποιτο, ἅμα being an adverb. `i` had "would be" against `l` "will be" (ἔσται). | Merged with the next unit (223) into one two-line unit; `l` two lines; `i` "will be"; note rewritten with the μοι construction corrected and the reason for the merge. |
| 225 (225–226) | `t` join, `l`, `i`, `n` | major | Same fault: unit ended at line 225 with no stop (… εἴ πέρ τε νοήσῃ). | Merged with 226 into one two-line unit; the speech's closing ” stays on the merged unit; note joined. |
| 289 (289–290) | `t` join, `l`, `i`, `n` | major | Same fault: unit ended at line 289 with no stop (… μήσατο ἔργα). | Merged with 290 into one two-line unit; note joined with the reason. |
| 251 | `i` | major | Same Greek as iliad-040 (unit at 526, ἀλλ’ ἴομεν·), published `i` "But come, let us go;". The draft's "But let us go;" would FAIL validator rule 6. | `i` -> "But come, let us go;". |
| 266 | `l`, `i`, `n` | major | πυκινὸν δόμον rendered "a close-built house" (`l`) and "his strong house" (`i`). The Odyssey table fixes πυκινὸς δόμος as "the solid house" and turns down "close-built" and "strong-built"; the Iliad table keeps "solid" for πυκινός (4.392, 5.751). The `l` and `i` also disagreed with each other. | `l` "a solid house having broken through"; `i` "breaking into his solid house"; note says "solid". (new-renderings.md still carries the wrong row: see follow-ups.) |
| 220 | `l`, `n` | major | θυμὸς ἀγήνωρ given "proud spirit" in `l`. Odyssey table (4.548) and the Iliad ἀγήνωρ row: `l` "manly spirit", `i` "proud spirit". The same phrase at 244 already had "manly spirit" in `l`, so the part contradicted itself. | `l` -> "my manly spirit"; note says which layer has which word. |
| 207 | `n` | moderate | "The same optative begins the next two lines' purposes" is false: the next lines are indirect questions (ἅσσα …, ἢ μεμάασιν …), not further purposes, and the optative does not "begin" them. | Replaced with: πύθοιτο also governs the two indirect questions that follow. |
| 247 | `n` | moderate | "περίοιδε is the perfect of περιοίδα": there is no such verb. | Now: περί + οἶδε, perfect of οἶδα (present in sense). |
| 259 | `n` | moderate | "The lines explain why a plain cap is worn by the young": nothing in the Greek says so; the note also never named the subject of ῥύεται. | Replaced with the subject (the καταῖτυξ). |
| 265 | `n` | moderate | Note said ἀρήρει is "had been fitted" while `l` and `i` say "was fitted" (and the table's 3.338 row has "was fitted"); "the felt sits between the straps and the head" is not in the Greek. | Note now "was fitted" (a pluperfect used for a state, as at 3.338); the unsupported sentence removed. |
| 268 | `i`, `n` | moderate | `i` "he gave it at Scandeia" against `l` "to Scandeia he gave it"; the note called the accusative a place of giving. Σκάνδειαν is accusative, i.e. direction. | `i` -> "he took it to Scandeia and gave it to Amphidamas of Cythera;" (the going is understood from the accusative); note says so. `l` left (it is the literal order). |
| 281 | `n` | moderate | The scansion sentence misdescribed the scanner's result. The chosen scansion needs BOTH lengthenings (πάλιν + ἐπί in foot 2; ἐϋκλεῖας + ἀφικέσθαι in foot 5), not "one or the other"; and the alternative scansion is a second one of equal cost, not a different place for the same licence. I scanned the line by hand: pattern – ⏑⏑ | – ⏑⏑ | – ⏑ ‖ ⏑ | – – | – ⏑⏑ | – ×; the irregularity is real, one sentence kept. Note was also 132 words (band warns above 130). | Sentence rewritten to say what the scanner found; note shortened to 129 words. |
| 285 | `n` | moderate | ἕσπεο called "the imperfect"; it is the aorist (ἑσπόμην), and new-renderings.md already glosses it "you went with". | "aorist second person, ‘you went with’". |
| 206 | `l`, `i` | moderate | τινά is singular; `l`/`i` had "some of the enemy" (a plural partitive), against the note's own "someone". | `l` "some one of the enemy"; `i` "one of the enemy". |
| about | `about` | moderate | "where the dead lie thin" (contradicts 199, now fixed); "not to spare Menelaus" (Menelaus is not named in Agamemnon's speech; the narrator says Agamemnon feared for him); "helmet lined with boar's tusks" (ἔκτοσθε: the tusks are on the OUTSIDE). | Reworded on all three points. |
| 276 | `l`, `i`, `n` | minor | κλάζω rendered "scream"; the Iliad table fixes κλάζω as "shriek". | "shrieked" / "shriek" / note. |
| 275 | `i`, `n` | minor | `i` "could not see" against `l` "did not see" (ἴδον, aorist); note called δι’ ὀρφναίην "an accusative of extent with διά" (διά governs the accusative). | `i` "did not see"; note reworded. |
| 208 (ἢ μεμάασιν) | `l` | minor | ἀπόπροθεν rendered "far from the city" in `l`; the Greek says only "far off" (the city is supplied from the next line). | `l` "far off"; `i` keeps the sense. |
| 214 | `n` | minor | "a ewe that is still suckling": the picture the new-renderings row refuses to decide. | "a ewe with a lamb". |
| 217 | `n` | minor | Claimed the sheep "will be spoken of or shared at every feast": not in the Greek. | Subject named plainly (the ewe, the gift). |
| 218 | `n` | minor | "the same line … in the Odyssey" (Odyssey has οἱ); "because the task is dangerous" is the drafter's guess. | Corrected; "No one answers at once." |
| 237 | `l` | minor | σῇσι φρεσί given "in your mind"; the part's own 232 and the Odyssey table use "wits". | "in your wits". |
| 253 | `i` | minor | ἔτι (still) dropped: "is all that is left". | "is still left". |
| 254 | `n` | minor | "The second half of the line … is the same as in 272": it is the line from ὅπλοισιν on, i.e. more than the second half. | "From ὅπλοισιν on, the line is the same as in 272." |
| 271 | `l`, `n` | minor | `l` began "and it then" (no καί/δέ in the Greek); note "now at last" for δὴ τότ’. | `l` "then indeed it covered …"; note "then indeed". |
| 278 | `n` | minor | Said ἐν πάντεσσι πόνοισι "ends the unit"; the unit ends after παρίστασαι. | Corrected. |
| 210 | `n` | minor | "ἐπεὶ … γ’ ‘since at least’": γε is emphatic, not limiting. | "since indeed (γε stresses the reason)". |

Counts: major 7, moderate 9, minor 12 (28 changed items; three of the majors are merges). 

## Findings considered and refused

- **ἀργιόδοντος ὑός (263) rendered "white-toothed boar".** The Odyssey table fixes ἀργιόδων ὗς (8.476) and ἀργιόδοντας ὕας (8.60) as "pig(s)", though it uses "boar" for σῦς and for wild animals (19.393). Here the tusks on a helmet can only be a wild boar's, and "pig" would mislead; the new-renderings row records "white-toothed" but not "boar" against "pig". Left as drafted. Owner may want one line in the table.
- **τολμήεις "enduring" (204), πρόφρων "ready-minded" (244, 290), μενεπτόλεμος, ξανθός, μειλίχιος "gentle", ἐϋκλεής "well-famed" / "of good name", κυνέη "helmet", ἀσκηθής "unscathed", θαλπωρή "comfort", μέρμερα "baneful", Ἀτρυτώνη, φῖλαι**: each checked against the tables and found to follow them. No change.
- **ὀλλύς (200) "destroying".** Some would write "from destroying". The participle agrees with Hector and the word is kept literal; the note already says the Argives are its object. Left.
- **οὗ πέρι (244).** Could be read "about whom"; the drafter's "whose heart beyond others" is a defensible reading and agrees with `i`. Left.
- **10.218 punctuation.** `l`/`i` end in `;` although `t` ends in `.`: required by the validator (see above). Left.
- **The speaker of 194.** The note says Nestor; iliad-059's last unit confirms it (Nestor to the guards). Left.
- **Scansion flag at 281.** Real (see table); the single-sentence note kept.
- **Speech boundaries.** All seven speeches open and close in this part; the neighbouring part iliad-061 is still `todo`, and Diomedes' prayer closes at 294 with ” (as in the Odyssey's published unit for the same two lines).

## Second pass

Greek -> `l` word by word (case relations, tense, mood, particles) on all 95 units after the edits; `l` <-> `i` agreement; remembered English in `i`; quotation marks. The second pass found no further errors beyond the table of changes above (the 266, 276 and 220 items were found on the second read against the tables). The `gloss.json` for this part does not yet exist in `drafts/iliad-060/`, so the parse check of the glossary (runbook: reviewer's second pass reads `gloss.json`) could NOT be done and must be repeated once the glosser has run. Note that the merges change which units contain 222–223, 225–226 and 289–290 for the glosser's "every place it occurs"; the forms are unchanged.

## Follow-ups (not mine to edit)

- `new-renderings.md`: the row for πυκινὸν δόμον (10.267) lists "close-built" in `l` and "strong" in `i`; it must read "solid house" in both (the table row for πυκινὸς δόμος, 7.81). The 10.208–210 and 10.252–253 rows describe the units as drafted and need no change; the row for ἀργιόδοντος ὑός should say "boar" against the table's "pig" (see refused finding).
- LOG.md should record: 3 units merged to satisfy the build's end-of-unit rule (222–223, 225–226, 289–290).

## Second pass (gloss)

`gloss.json` read against `units.json`: 140 novel entries (all of `novel-forms.json`, none missing, none extra) and 18 `__broaden__` entries. Every key occurs in the units; every `__broaden__` entry begins with the old entry whole. Format checked by script: all novel entries under 230 characters, typographic ’ only (no ASCII apostrophe, no U+02BC), no line numbers, no "here". Each parse was read against the line(s) it occurs in. Known forms were spot-checked for uses the old entry does not cover (ἢ, ἤ, ἥ, ὅ, ἐπ’, ἐπὶ, μετὰ, παρὰ, τῇ, τίς, δῖα, δῦναι and the like); all are covered.

### Changes

| Form | Severity | What was wrong | Done |
|---|---|---|---|
| σπεῖό | moderate | Called a "root aorist"; ἐσπόμην is a thematic 2nd aorist, and the Attic imperative was not named. | "2nd aor. imper. 2 sg. mid., epic σπεῖο (= Attic σποῦ)". |
| πύθοιτο | moderate | "In a wish-clause": neither use (240 hoped-for result after εἰ … ἤ; 204 potential with κε) is a wish. | Both uses stated. |
| αἰδοῖ | moderate | "Dative of motive, out of respect" gave the sense of αἰδόμενος; the word is the dative object of εἴκων ("yielding to respect", as `i` has it). | "with εἴκων (+ dat.): ’to respect, to deference’". |
| ὀλλὺς | moderate | "= ὀλλύων" names a form that is not the Attic equivalent; ὀλλύς is the athematic participle. | "athematic ὄλλυμι (Attic ἀπολλύς)". |
| πέρι (broaden) | moderate | Described οὗ πέρι as "after a relative genitive of comparison"; οὗ is the possessive genitive of Odysseus and πέρι the adverb "beyond others". | Reworded; example "οὗ πέρι … κραδίη ’whose heart beyond others’". |
| ἑσπομένοιο | minor | Tense of the participle not given. | "pres. part." |
| ἄνεται | minor | Sense uncertain (the unit's note says so) but the entry did not. | "sense not certain". |
| ὑὸς | minor | "epic ὑός" is also the Attic genitive of ὗς. | "gen. sg. ὑός". |
| πλέων (broaden) | minor | Example "the night further on" was a loose gloss. | "πλέων … τῶν δύο μοιράων ’more than the two parts’". |

Counts: major 0, moderate 5, minor 4 (9 entries changed).

### Considered and refused

- **δύ’, αὐτοῦ, νοήσῃ, ἕλοι, ἔλθοι, ἕποιτο, ὃ, τοῦ, ἑὸν, ἐδύτην, μηδ’, μηδὲ, τι, περὶ, πέρ (broadens)**: each new reading fits its line; left.
- **τίς (εἴ τίς μοι … ἕποιτο, 223)**: no broaden asked for; the old entry's "indefinite, written τίς: ’someone, one’" covers it.
- **θαμέες lemma**: LSJ gives θαμέες as the plural of θαμύς; the entry keeps the plural as its own head and names the Attic form. Left.
- **κεκλήατο "summoned" against `l` "called"**: both senses are in the entry. Left.
- **ἀργιόδοντος / ὑὸς "boar, pig"**: the entry gives both; the "boar" against "pig" question is the owner's (see the first pass and `new-renderings.md`).

### new-renderings.md

The πυκινὸν δόμον row now reads "solid house" in both layers (table row πυκινὸς δόμος, 7.81); the ἀργιόδοντος ὑός row notes "boar" against the Odyssey table's "pig", kept and flagged for the owner. Seven rows that only restated existing table entries were dropped: Ἀτρεΐδης δουρικλειτὸς Μενέλαος, ἐμῷ κεχαρισμένε θυμῷ, ἀσκηθής, ἐσχατόωντα, μειλίχιον μῦθον, μάλα μέρμερα … ἔργα, ξεινήϊον εἶναι.
