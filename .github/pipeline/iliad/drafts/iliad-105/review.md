# iliad-105 — review (Iliad 16.569–675, 60 units, 107 lines)

Reviewer pass 1 (notes, cross-references, Greek → `l` → `i`, house tables, quotation marks) and pass 2 (re-read every edited unit, re-ran the validator's same-Greek rule against all published Iliad parts and the Odyssey, re-checked marks and `p`/`mark` flags). `t` untouched (verified identical before and after). `gloss.json` not touched. No scansion flags in the packet; all 107 lines were also run through `scan_line` and scan.

## Changes (unit index · line · field · severity · what was wrong · what was done)

| unit · ln | field | sev | wrong | done |
|---|---|---|---|---|
| 19 · 606 | `i` | HIGH (gate, unresolved) | The Greek is letter-for-letter the published iliad-084 unit (13.671), whose `i` is "Paris hit him…". `validate_iliad.py` check 6 FAILS on same Greek with different English. "Paris" is true there and false here (Meriones). | Left "Meriones hit him…". Needs the lead's decision before the build (see Open item). |
| 17 · 602 | `l`,`i`,`n` | MEDIUM | μένος rendered "strength"; the Iliad table fixes μένος as "might" (2.387, 3.294, 5.125, 5.296, 6.265, 7.457, 10.366, 12.18), "strength" being kept for κράτος/σθένος. Row 6.265 has μένος and ἀλκή side by side, both "might", with a note saying so. | "their might … their might"; note says both words are "might". |
| 30 · 621 | `l`,`i`,`n` | MEDIUM | σβέσσαι μένος "quench the strength", same table violation (and new-renderings.md wrongly claimed the table's μένος was "strength"). | "quench the might". |
| 18 · 603 | `l`,`i`,`n` | MEDIUM | κορυστήν "armed man"; the table (4.457, 13.201) fixes κορυστής as "helmeted (warrior)" and lists "armed man" as avoided. | "helmeted warrior"; note says "armed" is the other reading. |
| 2 · 573 | `i`,`n` | MEDIUM | ἐξεναρίξας given "killed" only, with a note claiming the verb "tells only of the killing" of a kinsman; unsupported, and the table (4.488, 5.703, etc.) fixes ἐξεναρίζω as "kill and strip" (the 6.417 departure applies only where the killing is already told). | `i` "having killed a good cousin and stripped him of his armour"; note now says the English gives both. `l` "despoiled" unchanged. |
| 24 · 611–613 | `l`,`i`,`n` | MEDIUM | οὐρίαχος "butt-spike"; the published iliad-081 (13.443, same word) has "butt-end", and the glossary has "spear-butt". πελεμίχθη "quivered" clashed with κραδαινομένη "quivering" two lines on and with the published "shook" for πελεμίζω. | "butt-end"; `i` "shook"; note cites 13.443. |
| 47 · 652 | `n` | MEDIUM | Cross-reference "formula of 10.153" is wrong (10.153 is a different line). The formula is at 13.458 and 14.23. | Corrected; also removed "here with οἱ" (the formula already has it). |
| 26 · 614 | `n` | MEDIUM | "Idomeneus’ escape from this same cast" is false: Idomeneus escapes an earlier cast of Aeneas, at 13.503–505. | Reworded with the line numbers. |
| 51 · 659 | `n` | MEDIUM | "harmed by the spear in his side" — Patroclus hit Sarpedon where the midriff closes round the heart (16.481). | Corrected, with the citation. |
| 49 · 657 | `n` | MEDIUM | ἔτραπε called "unaugmented"; it has the augment. κέκλετο called "unaugmented aorist": it is the reduplicated aorist. | Both labels fixed. |
| 22 · 609 | `l`,`i` | LOW | ὑπασπίδια: `l` "under-the-shield" and `i` "under the cover of" depart from the table (13.158: `l` "under the shield", "under cover of" avoided; προβιβάς "striding forward"). | `l` "under the shield striding forward"; `i` "as he strode forward under his shield". |
| 23 · 610 | `n` | LOW | "elsewhere in Book 13" vague (and the line is 13.184, 13.404, 13.503). | Line numbers given. |
| 42 · 641 | `n` | LOW | "The last half-line is that of 2.471": 643 is the whole of 2.471. | "last line". |
| 32 · 623 | `n` | LOW | "is the pair of 5.654": 5.654 has the infinitive δώσειν, not δοίης. | "echoes the pair of 5.654", with the Greek quoted. |
| 8 · 584 | `n` | LOW | "you had been angered" for the pluperfect κεχόλωσο while `l` says "were angered". | Note says it stands for "you were angry". |
| 28 · 617 | `n` | LOW | καὶ … περ ('even though') not accounted for; note glossed only "dancer though you are". | Note says καὶ … περ marks the concession. |
| 57 · 671 | `n` | LOW | πομποῖσι κραιπνοῖσι quoted in a form that is not in `t`. | πομποῖσιν κραιπνοῖσιν. |
| 25 · 613 | `n` | LOW | "‘its’ strength" (μένος is "might" here). | "‘its’ might". |

Also edited `new-renderings.md` (so the rows copied into conventions.md are right): removed the ἐξεναρίξας row (no longer a departure); rewrote the οὐρίαχος, σβέσσαι μένος, κορυστής rows; removed the "reviewer should note the clash" aside from the ἀφίει μένος row.

Counts: HIGH 1 (open), MEDIUM 9, LOW 8. Units changed: 2, 8, 17, 18, 22, 23, 24, 25, 26, 28, 30, 32, 42, 47, 49, 51, 57.

## The drafter's flagged points

1. **606a English vs iliad-084.** Published `i` is "Paris hit him…", correct for 13.671 where Paris shoots Euchenor and wrong for 16.606 where Meriones throws. The sense does not allow conforming, so "Meriones" stays; `l` is identical to the published one. The validator nevertheless fails (rule keyed on letters only). Open item below.
2. **613 ἀφίει μένος "might" vs 602 "strength".** 613 is right (identical to published iliad-081, 13.444, and to the table's μένος "might"); 602 and 621 were wrong and are now "might". No clash remains. Note that 9.706 in the table (τὸ γὰρ μένος ἐστὶ καὶ ἀλκή → "strength and might", "follows the table's μένος 'strength'") contradicts 2.387 and 6.265; it looks like a table error and should be corrected when the table is next touched, not followed.
3. **573 ἐξεναρίξας.** Conformed to the table ("killed and stripped"), see above. The drafter's reasoning was a fair judgment call but the table's own exception (6.417) does not cover it, and the note asserted something about the verb that cannot be shown.
4. **Ilios vs Ilium.** "Ilios" is right: the table's Ἴλιον rows (5.204, 8.561, 13.724, 15.71) and published iliad-079/096 use "Ilios"; "Ilium" is kept for Ἴλιος ἱρή (4.46, 7.413, 11.196). The 5.551 row of the table (l/i "Ilium of the fine foals") contradicts its own avoided-list and the Odyssey; flagged for correction, not followed.
5. **Notes citing Book 13.** Checked against the source text and published parts: 13.444 (iliad-081) ✓, 13.671–672 (iliad-084) ✓, 13.544 ✓, 13.158 (iliad-078) ✓, 13.184/13.404/13.503–505 ✓ (iliad-079, -082). All correct except the faulty 10.153 (fixed). Other references checked against the source and correct: 16.412–414 (iliad-103), 4.505, 5.78, 2.471, 2.683, 5.654, 16.126, 16.454–457, 16.490, 4.140, 8.69.

## Considered and refused

- Unit 1 `i` "well-peopled" against `l` "well-inhabited": matches the Odyssey/Iliad pairing (Od. 13.285, Il. 13.815). Kept.
- Unit 12 "a home" for the plural οἰκία: collective sense, no better English; kept.
- Unit 18 `l` "of Ida" for Ἰδαίου (adjective agreeing with Διός): the note says it is an epithet of Zeus and `i` has "Idaean Zeus". Kept.
- Unit 28 `l`/`i` omit "even" for καί: concessive καὶ … περ; now explained in the note rather than forced into the English.
- Unit 28 διαμπερές "completely / for good": the table's "right through" (5.284, 7.171) is for the spatial sense; 16.640 keeps "right through". Documented in new-renderings; kept.
- Unit 47 ὄφρα with optative rendered "that": defensible as the clause giving what seemed better; kept.
- Unit 55 `i` "go out from the missiles" with the note that the direction is open: `i` follows ἐκ βελέων literally and the note does not say otherwise. Kept.
- Unit 4 νέκυος taken as Sarpedon's body without naming it: the note says so and the part's opening note names the fight. Kept.
- Units 10, 5, 14, 20, 25, 39, 54, 58, 59: whole-unit repeats; `l` and `i` identical to the published ones (checked by script). Unit 59 differs from odyssey-117 (warning only; Iliad's own 16.457 / iliad-103 is followed).
- Remembered English: nothing found that arrives fully formed; "wide-wayed", "double-pointed", "man-breaker", "dark as a cloud", "my good fellow" are all table renderings.
- Quotation marks: speeches at 617–618 (Aeneas), 620–625 (Meriones), 627–631 (Patroclus), 667–675 (Zeus) each open with “ on the `mark` unit and close with ” on the last, in both layers; no speech runs on from iliad-104 (its last unit is narrative) or into the next part (Zeus's speech ends at 675). `p` is on units 0, 29, 33, 39 = ¶ at 569, 619, 626, 632.
- Nothing in `n` names a modern translator; all notes within the validator's word band (units 11 at 130 words, 32 and 40 near it, are pre-existing lengths; no failure).

## Open item for the lead (blocks the gate)

Unit 19 (16.606, `τὸν βάλ’ ὑπὸ γναθμοῖο καὶ οὔατος·`) cannot pass `validate_iliad.py` with a true English. Options: (a) change the published iliad-084 unit (13.671) `i` to a subject-free "He hit him beneath the jaw and the ear;" (true in both places; `n` already names Meriones here) and set unit 19's `i` to the same; (b) accept "Paris hit him…" here (false, not recommended); (c) merge units 19 and 20 into one unit (changes unit boundaries, `t` stays). I recommend (a).

Also for later parts: 16.610–613 recurs at 17.526–529 (and 17.305), so the οὐρίαχος / ἠλεύατο / ἀφίει μένος renderings above will bind Book 17.

## Pass 2 (second reviewer: glossary parses, broadenings, merged unit)

Checked every one of the 89 new `gloss.json` entries against the line in `t` (case, tense, mood, voice, lemma), the 23 `__broaden__` entries (old entry from `git show HEAD:iliad-glossary.json` kept whole, then ` · ` and the new reading, and each new reading matched to its line), the entry rules (under 230 characters for new entries, ’ only, no line numbers, no "here"), and the merged unit 19 (606–607). `gloss.json` and the root `iliad-glossary.json` were found identical for this part's keys and were kept identical after the fixes.

Fixes (gloss.json and iliad-glossary.json, identical):

| form | wrong | done |
|---|---|---|
| ταναοῖο | the word "here" in the entry | removed |
| κεχάροντο | "unaugmented" on a reduplicated aorist middle (misleading; the form has no augment to lack) | "redupl. aor. 3 pl. mid., epic" |
| ἐξεναρίξας | gloss ’having slain’ disagrees with the part's `i` and the table (kill and strip) | ’having killed and stripped’ |
| οὐρίαχος | "butt-spike", but the unit and iliad-081 (13.443) say "butt-end" | "butt-end of a spear, the spike at the butt" |
| κεχόλωσο | ’you were enraged’; `l` and `i` say "angered" | ’you were angered’ |

Also fixed `n` (units.json and iliad-105.json, identical) at 16.613: "Whose strength Ares lets go" now "Whose might" (the unit renders μένος "might").

Result: 5 entries fixed, 1 note fixed, 0 parse errors found otherwise (all 89 case/tense/mood/voice/lemma checks agree with `t`). All 23 broadenings keep the old entry whole, add one ` · also …` reading, and each reading matches its line. Length: the 89 new entries are all under 230; 12 broadened entries are over 230, which the build allows and which is unavoidable under the additions-only rule. No ASCII apostrophes, no line numbers.

Merged unit 19 (606–607): the note reads sensibly for two lines ("The two lines are those of 13.671–672"), the subject and the weapon are handled, and `l`/`i` cover both lines. `t`, `tr`, `sc` untouched.

Quotation mark: the only warning, 675 against odyssey-117 296, differs solely in the closing ” (Odyssey has none); `t`, `l` and `i` are otherwise identical. `python3 validate_iliad.py iliad-105`: PASS (59 units, 107 lines).

No edits are needed to `t`, `tr`, `sc` or unit boundaries. Nothing committed.
