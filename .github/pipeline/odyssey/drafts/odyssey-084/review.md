# odyssey-084 — review (Odyssey 17.204–305)

Reviewer, two passes. `units.json` was edited in place by script; `t` is byte-identical to the drafter's (checked after each pass: the `t` of all 58 units, and title, titleEn, part and about, unchanged). Severity scale used: **high** = the draft would fail the gate or misstate the text; **medium** = a false grammatical or positional claim in a note, or an `l`/`i` rendering that breaks a house rendering; **low** = imprecise wording, a slip of force, a hedge or length trim.

Method, pass 1: every grammatical label and every "at NNN" in every note checked against the line; cross-references checked in the source text (2.187, 1.139, 14.55, 15.344, 17.166, 17.193, 1.9, 5.223/224, 6.293, 8.363 all exist and say what the notes say); Greek → `l` word by word; `l` ↔ `i`; remembered English; quotation marks; the neighbouring parts; every table row of the drafter's `new-renderings.md` set against the existing table in `conventions.md` and against the shipped parts; every unit's Greek set against every shipped unit and line (the validator's rule 6 and the line-level repeats); note length against the validator's band; backticks. Neighbouring parts: the last unit of odyssey-083 (17.201–203, narrative, no speech open) leaves nothing running on; odyssey-085 does not exist yet. Odysseus's question at 17.305 opens a speech that begins in the next part, so the last unit correctly carries no “. Quotation marks inside the part: six speeches, 6 “ and 6 ” in each layer, “ on the first unit of each speech, ” on its last, `mark` on the first unit of each (217, 240, 248, 264, 273, 281); `p` flags agree with Murray's ¶ at 204, 217, 233, 240, 247, 254, 264, 272, 281.

Scansion: the packet flags nothing. I also ran `scan_hexameter.py`: it flags `spondaic fifth` (a spondee in the fifth foot) at 208, 217, 220, 230, 268, 288, 299 and nothing unresolved. A spondaic fifth foot is an ordinary licence of the hexameter, not an irregularity of the transmitted text, so no note was changed (see the refused list).

## Pass 1 — changes

| # | line · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | 204 · n | low | "Ἴθακος has the same name as the island" overstates: Ἴθακος and Ἰθάκη are one stem with different endings. | "Ἴθακος is a man's name built on the same stem as the island's, Ἰθάκη." |
| 2 | 208 · n | medium | "both genitives have uncontracted endings (Attic -ῶν)" is false of αἰγείρων, which is the ordinary form (only ὑδατοτρεφέων is uncontracted, -έων). | Claim restricted to ὑδατοτρεφέων. (Re-tidied in pass 2, #27.) |
| 3 | 210 · n | medium | τυκτήν stands at 206, so "two lines earlier" is wrong. | "four lines earlier". |
| 4 | 217 · n | low | τὸν ὁμοῖον called "the article used as a pronoun"; it is an ordinary article with a substantivised adjective. | "an adjective used as a noun with the article". |
| 5 | 223 · n | low | "εἰ with the optative and κε(ν) makes it remote": the κε(ν) that governs the apodosis is the one at 225 (καί κεν θεῖτο); the κ’ at 223 is not what makes the protasis remote. Note also 134 words (validator WARN above 130). | Claim reworded to εἰ + optative, with the κε(ν) of 225 named; "The condition runs over three lines" and the glosses of σταθμῶν and ὀρός dropped (the glossary carries them). Now 127 words. |
| 6 | 226 · i | medium | κάκ’ ἔργα rendered "base deeds" in `i` against "evil deeds" in `l`; the shipped rendering of κακὰ ἔργα is "evil deeds" in both layers every time (odyssey-005, 036, 044, 068, 080). "Base" is kept for κακός of a person. | `i`: "evil deeds". |
| 7 | 230 · n | low | A genitive participle (βαλλομένοιο) cannot "agree with" the dative οἱ. | "naming the same man as οἱ". |
| 8 | 234 · i | low | The Greek is οὐδέ … ἀλλά ('not … but', which the note itself says); `i` made the second clause a flat "and". | "and he did not shove him off the footpath, but stood firm;". |
| 9 | 240 · l | low | "this for me fulfil, this desire": τόδε agrees with ἐέλδωρ, so one "this" has been added; shipped `l` for κρηήνατ’ ἐέλδωρ (odyssey-013) is "fulfil my wish". | "this wish for me fulfil,". |
| 10 | 240 · n | low | 138 words (validator WARN). "the usual shape" asserts something about the rest of the poem. | Prayer-shape sentence shortened and made descriptive of this prayer; "the Greek does not remark on it" dropped. Now 125 words. |
| 11 | 243 · i | low | "that that man may come, and may some power lead him" — the second clause lacks its "that" and is not natural English. | "that that man may come, and that some power may lead him;". |
| 12 | 258 · n | medium | "τῷ is 'him', Eurymachus". τῷ is the man who has just sat down, Melanthius, the subject of the last two sentences: the servants set the portion before him; Eurymachus is only the object of φιλέεσκε. The note named the wrong man. | "τῷ is 'him', Melanthius, who has just sat down (the Greek does not name him again)". `l`/`i` ("beside him") were already neutral and unchanged. |
| 13 | 260 · l | medium | ἀγχίμολον given "close behind"; the table already fixes ἀγχίμολον (14.410) as "close by" in both layers (shipped at odyssey-069), avoiding "nearby" and "soon"; the drafter's own new row contradicts the existing row. | "And close by, Odysseus …". See "For the orchestrator" below on the row. |
| 14 | 260 · i | medium | Same: "Close behind him". | "Close by, Odysseus and the heavenly swineherd came up and halted, …". |
| 15 | 260 · n | medium | "ἤλυθ’ is ἤλυθε … an unaugmented past": ἤλυθε is the augmented form (the unaugmented stem is ἐλυθ-). | "a past of ἔρχομαι with its final vowel elided". |
| 16 | 263 · n | low | "a short exchange … on the threshold": nothing in these lines puts them on a threshold. | "on the threshold" removed. |
| 17 | 268 · n | medium | "The unit ends mid-line, at the full stop": it ends at the end of line 268; it is the unit before (δικλίδες· at 268) that ends mid-line, and this one begins mid-line. | "The unit begins mid-line, after the stop at δικλίδες, and ends at the full stop that closes the line." |
| 18 | 275 · n | low | "αὐτοῦ is the adverb 'right here', as at 255": the αὐτοῦ in the earlier unit is in line 254 (λίπεν αὐτοῦ). | "as at 254". |
| 19 | 282 · n | low | "ἔρχευ … in its uncontracted Ionic form": ἔρχευ is the Ionic contraction εο → ευ of ἔρχεο; the uncontracted form is ἔρχεο. | "the Ionic form of the imperative ἔρχεο (Attic ἔρχου)". |
| 20 | 284 · n | medium | "πέπονθα … with present sense": the perfect here means 'I have suffered' (as `l` and `i` both say); the note contradicts its own unit. | "the perfect of πάσχω 'suffer': he has suffered, and it still stands." (reworded in pass 2, #28). |
| 21 | 285 · l | high | The Greek μετὰ καὶ τόδε τοῖσι γενέσθω· is the same unit as odyssey-024 (5.224), and the validator (rule 6) fails a unit whose Greek repeats a shipped unit with different English. `l` was "among these let this too come to be;". | `l` now the shipped wording, "among them let this too come to pass;" — **but see the unresolved residual under the table**. |
| 22 | 285 · i | high | Same; `i` was "let this be added to them as well;". | `i` now the shipped wording, "let this too come to pass along with them;". |
| 23 | 285 · n | low | The note said nothing of the repeat. | One sentence added: the same words close Odysseus's speech to Calypso at 5.224 and the English repeats that wording. |
| 24 | 286 · n | low | "οὐλομένη γαστήρ is also found at 15.344": the words at 15.344 are οὐλομένης γαστρός (genitive), not those. | "οὐλομένης γαστρός, the same words in the genitive, is found at 15.344". |
| 25 | 294 · n | low | πρόξ asserted as "here 'roe-deer'". The kind of deer is not known; "roe-deer" is the traditional guess (the table's rendering is kept). | "a kind of deer; 'roe-deer' is the traditional guess". |
| 26 | 296 · n | high | The note contains backticks (`l`, `i`); the validator fails a note with a backtick, and conventions say Greek and glosses are bare/quoted. 127 words, and the τέμενος sentence ("the usual sense of a plot") said nothing clear. | Rewritten without backticks: τέμενος is land marked off for a chief or a god; the Greek-order line keeps "precinct" as shipped at 6.293 and 8.363, the English line "estate" because this is a chief's own farmland. "ἅλις is 'in abundance'" and "poured out," dropped. Now 129 words. |

Pass 1 counts (rows): **high 3** (#21, #22, #26), **medium 9** (#2, #3, #6, #12, #13, #14, #15, #17, #20), **low 14** (#1, #4, #5, #7, #8, #9, #10, #11, #16, #18, #19, #23, #24, #25). Total 26 field edits in 22 units.

### Unresolved residual from pass 1 (needs the orchestrator; I cannot fix it without touching `t`)

**285 (unit "μετὰ καὶ τόδε τοῖσι γενέσθω·") will still FAIL validator rule 6.** The shipped unit at 5.224 ends a speech, so its `l` and `i` close with ” ("…come to pass.”"). Here the speech continues for four more lines, so a ” would be wrong, and I refused to add a stray one. With the ” left out, the strings are one character short of identical and the validator will print `line 285: same Greek as odyssey-024 line 224 but different English`. The only clean way out that does not touch the Greek of any word is to merge units 48 and 49 (the `t` becomes "τολμήεις μοι θυμός, ἐπεὶ κακὰ πολλὰ πέπονθα\nκύμασι καὶ πολέμῳ· μετὰ καὶ τόδε τοῖσι γενέσθω·", `ln` 284, two lines), so that no unit is a whole repeat. Suggested merged English, built from the two units as they now stand: `l` "enduring is my heart, since many evils I have suffered\nin waves and in war; among them let this too come to pass;" and `i` "my heart is an enduring one, since I have suffered many evils on the waves and in war; let this too come to pass along with them;". The merged note would be the two notes joined, keeping the 5.224 sentence. Since the reviewer may not change `t`, this is left to the next step; if it is not done, the build will go through and the validator will not PASS.

## Pass 1 — findings considered and refused

| line · field | finding considered | why refused |
|---|---|---|
| 212, 3 · n/l/i; names row | Dolius against shipped "Dolios" (odyssey-020, 4.735 'old Dolios', the only shipped use). | The table's rule for names is the familiar Latinised form (Eurymachus, Phemius, Arcesius, Ktesios→Ctesius, Dulichium …). "Dolios" is the lone shipped exception, in a part I may not touch; changing this part to match it would make the shipped Greek-ending form the model for a name that recurs at 24.222 ff. and is a well-known Latin form (Dolius). Kept "Dolius"; the new names row already records the choice. Recommend a one-word correction of odyssey-020 at some later point, logged in QUESTIONS.md. |
| 215, 238 · l/i | νείκεσσεν/νείκεσ’ "reviled" against the shipped imperative νείκεε "rebuke" (odyssey-032) and the table's ὁμοκλή row (17.189, "rebukes … follows 'rebuke' for νεικέω"). | The finite verb is "reviled" at 8.158 (the table row and odyssey-034), νείκεσεν at odyssey-035 and νείκεον at odyssey-061; the one "rebuke" is an imperative (032) and a noun (ὁμοκλή). Four against two, the four being the same forms as here. Renderings kept. The drafter's row records this. (The ὁμοκλή row's "follows 'rebuke' for νεικέω" is the odd one out and could be softened later.) |
| 296 · i | τέμενος: `i` "estate" against the shipped "precinct" (6.293, 8.363). | The table's γέρας row (11.175) already reserves "estate" for τέμενος, so the drafter's `i` follows the table; `l` keeps the shipped "precinct". Note: 11.185 τεμένεα ("domains") is a third rendering; the table is not consistent here. Kept; the note now says why the layers differ. |
| 228 · l/i, n | ἄναλτος "insatiable": guess? | The note already says the derivation is unclear and "insatiable" is the ancient gloss; the word is not of unknown meaning, only of unknown formation. Kept. |
| 295 · l/i | πρόκας "roe-deer". | Table keeps "roe-deer" for πρόξ; the sense is a traditional guess, now said in the note (#25). Rendering kept. |
| 235 · i | μερμήριξεν: `i` "debated" where shipped `i` varies ("pondered", "wavered", "thought up"). | No table row fixes the `i`, `l` is "pondered" as shipped each time, and "debated whether" fits the ἠέ … ἦ clause. Kept. |
| 285 · n | "tmesis for μεταγενέσθω" against the shipped note at 5.224 ("μετά is an adverb here"). | The two notes describe one thing in two ways (a preverb standing apart is an adverb); neither is false. Kept. |
| 260 · n | "φόρμιγγος γλαφυρῆς … the usual epithet" asserts something about the rest of the poem. | The table already carries φόρμιγξ γλαφυρή (8.257) and the epithet is shipped; the claim is supported. Kept. |
| 275 · n | "δόμους εὖ ναιετάοντας is the usual line-end phrase". | The table has the phrase at 17.28 and 17.85. Kept. |
| 208, 217, 220, 230, 268, 288, 299 · n | `spondaic fifth` flag from the scanner; add the sentence "metrically irregular as transmitted"? | Scanned by hand against the scanner's pattern: each has a spondee in the fifth foot, a normal licence with a full sixth foot; none needs a licence in the text. The runbook asks for the sentence only where the irregularity is real, and conventions mention metre only where it explains a form. None added. |
| 248 · i | Spaced em dash "baneful tricks — whom". | Both spaced and unspaced dashes are shipped. Kept. |
| 262 · l | "for for them he was striking up": reads like a typo. | It is the literal order γάρ σφισι; `l` is the word-by-word line. Kept. |
| 257 · i | "dearer than all the rest" for superlative μάλιστα. | Same sense and force; kept. |
| 285 · l/i (adding ”) | Add the ” so the English is identical to the shipped unit and the validator passes. | It would close a speech that continues for four lines, and the reader would see a wrong quotation mark. Refused; the residual is stated above. |
| 233 · l | "in his follies" for ἀφραδίῃσιν. | Follows the table row (10.27) "follies" / `i` "folly". Kept. |

## For the orchestrator (outside `units.json`)

- `new-renderings.md`: the ἀγχίμολον row ("close behind" / "close behind", avoiding "nearby") contradicts the existing table row ἀγχίμολον (14.410, "close by"); drop it, the units now follow the existing row. The ἀγχίμολον change would otherwise put two conflicting rows in the table.
- `new-renderings.md`: the ἀφραδίη, κύμασι καὶ πολέμῳ and ὀλοφώϊα εἰδώς rows are correct as written; the κακὰ ἔργα rendering ("evil deeds") needs no new row.
- Any glossary entry for ἀγχίμολον, ἤλυθ’ etc. is for the glosser; `gloss.json` does not exist yet, so pass 2 could not check parses against the lines (the runbook's second pass reads it).
- Housekeeping candidates for `QUESTIONS.md`: odyssey-020 "Dolios"; the table's τέμενος / τεμένεα / "estate" rows; the ὁμοκλή row's remark about νεικέω.

## Pass 2 — the corrected file read again from the top

Read all 58 units again after the pass-1 edits: Greek → `l`, `l` ↔ `i`, `i` alone as English, every note against its own unit and against the edited layers (a note edited in pass 1 must still agree with the `l`/`i` it sits beside: 260 "close by", 240 "wish", 243 "some power", 296 "precinct"/"estate" all agree), lines numbers named in notes, quotation marks, `p` and `mark`, repeats against shipped units, note lengths (all between 20 and 130 words), no backtick in any note, `l` line counts equal to `t`, no `\n` in `i`. Scansion lines unchanged. Results of the lint script: every whole-unit repeat (229, 272, 280, 281 ×2, 290) matches its shipped English exactly; 285 differs only by the closing ” (the residual above); quotation marks 6/6 in both layers.

| # | line · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 27 | 208 · n | low | My pass-1 edit left a redundant sentence ("ὑδατοτρεφέων … agrees with it; ὑδατοτρεφέων has …"). | Joined: "ὑδατοτρεφέων 'nourished by water' agrees with it, with the uncontracted ending -έων (Attic -ῶν)." |
| 28 | 284 · n | low | My pass-1 wording "and it still stands" is cryptic. | "he has suffered, and that stays with him." |
| 29 | 296 · i | low | `i` "Now, with his lord gone away" for δὴ τότε in a past narrative; `l` has "Then indeed", and 301 (same words) has "Then" in `i`. | "Then, with his lord gone away, …". |
| 30 | 277 · i | low | "wait here": ἐπίμεινον says 'wait, stay on'; "here" is not in the Greek (the contrast with going ahead is already in the unit). | "or, if you prefer, wait, and I will go ahead;". |

Pass 2 counts: **high 0, medium 0, low 4** (4 rows). The pass-1 residual at 285 stands unchanged (still high, needs the orchestrator). No new errors were found in the Greek → `l` reading, the `l` ↔ `i` agreement, the quotation marks or the `p`/`mark` flags on this pass.

Findings considered and refused in pass 2: none new beyond the pass-1 list (the second reading re-checked each refused item and kept the decision).

## Counts

| | high | medium | low | rows |
|---|---|---|---|---|
| Pass 1 | 3 | 9 | 14 | 26 |
| Pass 2 | 0 | 0 | 4 | 4 |
| Total | 3 | 9 | 18 | 30 |

Unresolved after pass 2: 1 (the 285 repeat/closing-quote conflict, high, needs units 48+49 merged or a decision to accept the validator FAIL).
