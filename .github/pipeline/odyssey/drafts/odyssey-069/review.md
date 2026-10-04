# odyssey-069 (14.321–417) — review

## Pass 1

Reviewer: adversarial, pass 1 only (glossary `gloss.json` ignored, being written elsewhere). `units.json` and `new-renderings.md` were edited in place by script (`review069_apply.py`, with a pre-review copy kept in the scratchpad); no character of any `t` was touched. The one structural change is three re-cuts (findings 3–5), which move unit boundaries over the same text: the units’ `t`, joined in order, still reproduce the archive character for character (checked against the pre-review copy, and with a read-only copy of the tiling checks in `build_odyssey.py`). The part now has 51 units (was 54).

**Totals: 38 findings — 5 major, 12 moderate, 21 minor.** Scale: *major* = a false grammatical label about the form in the line, an English layer that reverses or changes the Greek, or a defect that makes the build refuse; *moderate* = a false cross-reference or structural claim, a departure from a shipped rendering or a table row, a label that is inexact, or an English word that misplaces the sense; *minor* = an overclaim, an invented detail, a hedge that was missing, a wording nudge.

### What was read

Read in full, in chunks: `conventions.md` (rules sections and every row of the house-renderings table, through the 14.x rows), `packet.md`, `units.json`, `new-renderings.md`, the pilot `drafts/odyssey-001/units.json` and `review.md`, the last three units of odyssey-068, the last units of odyssey-067 around 14.191 (the speech’s opening, and the precedent for a formula line that has no stop), `validate_odyssey.py` and `build_odyssey.py` (to know what the build refuses), and the Murray source JSON for the lines where a stop is missing. odyssey-070 does not exist yet. Published English was looked up by script for μαψιδίως, κατὰ κόσμον, νήποινον, ὀϊζύς, ἠνώγει, προσεφώνεε, ἐνδυκέως, ξείνια, κειμήλια, σταθμός, ἔφασκε and the repeated lines. No modern translation was opened or recalled; Murray’s English was not opened.

Checks run (read-only): tiling, `ln`, `p`, line counts, five-line limit and terminal punctuation (the build’s own tests); the validator’s rule 6 (whole-unit repeats); quotation-mark counts; note length (every note now 25–130 words, none contains `?`, a backtick or an ASCII apostrophe). Not run: `build_odyssey.py` itself (no dry-run; it writes files) and the validator’s glossary-coverage check (the glossary is being written elsewhere; the merged units contain exactly the same forms as before, so coverage is unchanged).

### Neighbouring part, quotation marks, paragraphs

odyssey-068’s last unit (14.317–320) has no closing ” in either layer: the Cretan’s speech, opened with “ at 14.191 (odyssey-067), runs on. So 14.321 correctly opens with no “ and no `mark`, and its note says so. The closing ” stands on 14.359 (“for it was still my lot to live.”) and the note there now says where the speech was opened (two parts back, not “the last part”). Eumaeus: “ on 361 (`mark`), ” on 389; Odysseus: “ in the second line of the merged 390 unit (`mark`), ” on 400; Eumaeus: “ on 402 (`mark`), ” on 408; Eumaeus to the herdsmen: “ on 414 (`mark`), ” on 417. No nested speech. Counts per layer: 4 openings, 5 closings, so the validator will WARN (rule 5), correctly: say so in LOG.md. `p` is on 321, 360, 390, 401, 409, 414, the six ¶ of Murray. The formula lines 360 and 401 carry no `mark`; the speech after each starts the next unit.

## Changes (line · field · severity · what was wrong · what was done)

1. **382 · n · major** — False label: “μιν is Odysseus, the subject of the infinitive ἰδέσθαι”. μιν is the *object* of ἰδέσθαι (the Aetolian is its unexpressed subject, as of φῆ), and ἀκειόμενον agrees with μιν; `l` and `i` already had it right (“he said he had seen him … mending ships”), so the note contradicted its own `l`. Note rewritten (object; ἀκειόμενον agrees with μιν; “present participle” added).
2. **401 · l (and new-renderings row) · major** — `l` “Him answering spoke to the heavenly swineherd:” reverses the roles: it reads as if the swineherd were the one addressed, and `i` (“the heavenly swineherd spoke to him”) says the opposite. δῖος ὑφορβός is the subject. Now “To him answering spoke the heavenly swineherd:”, the order of the shipped line in odyssey-036 (unit at line 381: “Then indeed to Alcinous spoke heavenly Odysseus”). New-renderings row corrected and the withdrawn wording recorded in its avoided column.
3. **369–371 · structure (t, l, i, n) · major** — The unit 369–370 ends at ὀπίσσω, where the source prints no stop, and `build_odyssey.py` refuses a unit that does not end at `. ; · ,`. Re-cut: merged with 371 (one unit, three lines, ends at the full stop after ἀνηρείψαντο). English kept line by line from the shipped 1.239–241 (published l and i reused verbatim; the final punctuation is now a full stop in both layers, since the Greek ends with one, where the shipped line ended `;` for a raised dot). Rule 6 no longer applies to these lines as a unit (different Greek), so the wording is fixed by this note and by the packet. Note rewritten (says the stop is missing, and that the English is that of 1.239–241).
4. **390 · structure (t, l, i, n, mark) · major** — The formula line 390 ends at Ὀδυσσεύς with no stop in the source: same build refusal. Re-cut as at 14.191 in odyssey-067 (“The source prints no colon at the end of 191; the two lines are one unit here”): 390 is merged with 391–392. The formula keeps its shipped English (l “Him answering addressed many-wiled Odysseus:”, i “In answer Odysseus of many wiles said to him:”); “ now opens the second line of `l` and follows “to him:” in `i`; `p` and `mark` “Odysseus answers” (formerly on 391) sit on the merged unit. Note merged and trimmed, with the missing-stop sentence.
5. **411–413 · structure (t, l, i, n) · major** — Line 412 ends at αὐλιζομενάων with no stop: same refusal. Merged 411–412 with 413 (three lines; ends at the raised dot after ὑφορβός). `l` line 2 now ends `;` and line 3 opens “and he …” (no stop in the Greek between them); `i` is the two former `i` joined, with a full stop between the sentences. The note, which said “the unit is cut there by the sense”, now says the unit runs on to 413, and its κοιμηθῆναι gloss was corrected at the same time (see 29 below).
6. **334 (ἀλλ’ ἐμὲ πρὶν ἀπέπεμψε) · n · moderate** — “πρίν … meaning before that sailing” is false or empty: the ship the Cretan was put on *is* that sailing. What is meant is the sailing the king had promised Odysseus. Rewritten.
7. **336 · l, i, n · moderate** — ἠνώγει rendered “urged” in `l`, “urged” in `i`; every shipped ἠνώγει (odyssey-010, -023, -058) is “bade” in `l`, with “told”/“ordered” in `i`. `l` now “bade (them) send me”, `i` “told them to send me”, note “‘bade’”, and “those he urged” → “those he bade”.
8. **349 · i · moderate** — ἀμφικαλύψας given “wrapped”; the table row for ἀμφικαλύπτω fixes “enfold(ed)” in both layers and lists “cover”, “shroud”, “close over” as avoided (the echo is the point). `i` now “I enfolded the rag down about my head”. Tmesis gloss in the note brought into line.
9. **349 · n · moderate** — ἐφόλκαιον: the note said the meaning is unknown and in the next breath that “it names some part or fitting of the ship”. That is a claim about the unknown. Now: “From the line it is something smooth … that a man can go down to reach the water”; guesses listed as before.
10. **359 · n · moderate** — False cross-reference: “since it began in the last part”. The speech was opened at 14.191 in odyssey-067, two parts back (odyssey-068 contains no opening mark). Also the νυ gloss “you see” contradicted `l` “then”. Both corrected.
11. **364 · l, i, n (and new-renderings row) · moderate** — **μαψιδίως** (the flagged inconsistency). Draft: “to no purpose”, a fourth English word for one Greek adverb. Shipped: “heedlessly” (2.56, of feasting), “at random” (3.72 and 9.253, of wandering) and “without cause” (7.309, odyssey-032, μαψιδίως + infinitive of anger; the draft’s note and row omitted this one). Decision: this line stands exactly like 7.309 (adverb beside an infinitive of a wrongful act, said to the person doing it), so it takes “without cause” in both layers; “to no purpose” withdrawn; no fourth word. The older “heedlessly”/“at random” divergence belongs to published parts and is not touched; it stays flagged in the new-renderings row for the owner. Note cites 7.309.
12. **375 · l · moderate** — “both those who grieve, for long, for the lord who has gone”: the commas attach δήν to ἄχνυνται, but the note and `i` take δὴν οἰχομένοιο together (“for the lord long gone”). Now “both those who grieve for the lord long gone”.
13. **375 · n · moderate** — False structural claim: μέν “answered by the two groups of ἠμέν … ἠδέ”. The contrast with οἱ μέν comes at 378 (ἀλλ’ ἐμοί); the two groups stand in apposition to οἱ. Rewritten.
14. **384 · n · moderate** — φάτ’ called “aorist middle”; the house glossary parses φάτο as imperfect middle. Now “imperfect middle”.
15. **401 · n · moderate** — “ὑφορβός … the same noun as συβώτης”: false, they are two nouns with the same sense (the table says so). Now “a second word for the swineherd beside συβώτης”.
16. **402 · n · moderate** — “ἀπὸ … ἑλοίμην is tmesis for ἀφέλοιμι”: the printed form is middle (ἑλοίμην), so the compound is ἀφελοίμην, middle optative of ἀφαιρέομαι. Corrected.
17. **321b · n · moderate** — ἰόντ’ was called “the accusative ‘him, as he went’, the object of both”; it is a participle agreeing with an unexpressed ‘him’, which is the object. Corrected (and ἔφασκε given as “iterative (-σκ-) imperfect”, to match the glossary).
18. **321b · n · minor** — πολύκμητον “said of iron because it is hard to work”: a stated cause for a word’s use. Now “which suits iron, a metal hard to work”.
19. **327 · i · minor** — “after being so long away”: “so” is not in ἤδη δὴν ἀπεών (`l` “already long away”). Now “after being long away already”.
20. **331 · n · minor** — “the offering that sealed an oath”: the lines say he swore while pouring; the ritual function is a gloss. Now “the pouring that went with an oath”.
21. **341 · i · minor** — “threw about me another, a vile rag”: “another” with no head noun, and `l` has “another evil rag”. Now “threw another vile rag about me”.
22. **341 · n · minor** — English “me” where the Greek με is meant; “a different, worse garment” asserts “worse”. Now με, and “a different one, and a poor one”.
23. **353 · n · minor** — “out of the sea and up the bank”: no bank in the lines. Now “out of the sea”.
24. **354 · n · minor** — “the pronoun ‘they’ is easy to confuse with the article, as always in Homer”: muddled (οἱ is the pronoun; there is no article to confuse it with). Now “οἱ δέ is ‘and they’ … the old demonstrative pronoun, not the article of later Greek”.
25. **363 · i · minor** — “I do not think those things are as they should be” moves the negative from the predicate to the verb (weaker than οὐ κατὰ κόσμον ὀΐομαι). Now “I think those things are not as they should be”.
26. **363 · n · minor** — “a tale that does not hang together”: an interpretation of κατὰ κόσμον presented as the sense. Now “the stranger’s story”.
27. **365 · l · minor** — “or in the arms of friends”: the shipped line (1.235, 4.487) and the new-renderings row both have “his friends”. Restored.
28. **365 · i · minor** — “know well how my lord’s homecoming went”: invents a clause the Greek does not have (νόστον is the object of οἶδα, ὅ τ’ … explains it). Now “know well of my lord’s homecoming, that he was utterly hateful …”.
29. **365 · n · minor** — “the object is what happened about it”: vague. Now “νόστον is the object of οἶδα, and ὅ τ’ (ὅ τε) works as ‘that’ and explains it”. (At 411 the κοιμηθῆναι note said “to be put to sleep” against `l` “to sleep”; corrected inside the re-cut note: “aorist passive infinitive with an active sense, ‘to go to sleep’”.)
30. **372b · i · minor** — “happens to urge me” turns εἰ μή πού τι into chance; `l` has “perhaps”. Now “unless perhaps circumspect Penelope urges me”.
31. **381 · n · minor** — “its brevity carries the hurt”: an unverifiable literary claim. Cut; the factual half kept.
32. **384 · i · minor** — “bringing great stores of goods”: “great stores” for πολλά; `l` “many goods”. Now “bringing many goods”.
33. **393a · n · minor** — ποιησόμεθ’ stated flatly as an aorist subjunctive; the spelling is that of the future, as odyssey-067’s ἀγορεύσω note hedges. Now “a short-vowel aorist subjunctive … spelled like the future, which would give much the same sense”.
34. **395 · i · minor** — “where my heart wishes to be” for ὅθι μοι φίλον ἔπλετο θυμῷ: turns “has become dear” into a wish. Now “where it has grown dear to my heart”.
35. **395 · n · minor** — “the stranger has just said (341–343)”: fifty lines back. Now “described”.
36. **402 · i · minor** — “that would indeed win me a good name” (“win” invented; οὕτω … εἴη μοι is “so … would be for me”) and “both now” for ἅμα τ’ αὐτίκα (`l` “at once”). Now “in that way I should indeed have a good name and excellence among men, both at once and hereafter”.
37. **402 · n · minor** — “οὕτω γάρ is ‘so, for’” while `l` and `i` have “so, indeed”. Now “‘so, indeed’, the γάρ confirming”.
38. **406 · n · minor** — Κρονίων “here a name for Zeus himself”: it stands in apposition to Δία. Corrected.

## Quote marks, repeated lines, stock epithets — checked, no change

- **14.360** = published (odyssey-066, 14.55): `l` and `i` identical, checked by script (rule 6 clear). **14.390** formula: published wording kept inside the merged unit. **14.409**: first line reuses the published `l` and `i` of odyssey-019 verbatim. **14.369–371**: wording of 1.239–241 reused, see 3. **14.368** (1.235 = 4.487): `l` and `i` now both match the shipped lines.
- Stock epithets against the table: δῖος ὑφορβός “the heavenly swineherd” (✓ both), πολύμητις “many-wiled”/“of many wiles” (✓), περίφρων Πηνελόπεια “circumspect” (✓), ἀντίθεος “godlike” (✓), ἀργιόδοντες “white-toothed” (✓), εὐδείελος “clear-seen” (✓), ποντοπόρος “sea-crossing” (✓), ἐύσσελμος “well-benched” (✓), ὀπώρη “late summer” (✓), πρόφρων “ready-minded”/“with a ready mind” (✓), ξείνιος Ζεύς “guest-god”/“god of guests” (✓), δαίμων “a power”/“some power” (✓), ἄπιστος “unbelieving” (as odyssey-067), ἐκέκλετο “called out”/“gave orders to” (as odyssey-027).
- The Greek ends with no stop at 370, 390 and 412 (checked in the source JSON); the other cuts all fall at `.`, `;` or `·`.

## Considered and refused

- **326 ἄνακτος** (Pheidon, as the note says, versus Odysseus): the note commits to Pheidon, the usual reading, and `i` keeps the Greek’s ambiguity (“the halls of the lord”); no change.
- **328 θεοῖο** (with δρυός, or with ἐπακούσαι ‘hear from the god’): `l` keeps the Greek order, `i` takes it with the oak; the note makes no claim about it; left.
- **325** “the heap of goods” as subject of βόσκοι: a harmless gloss; left.
- **364 `l` “why you is it needful”**: awkward, but within the Greek-order licence the shipped `l` layer uses; left.
- **386–387 `i`** drops the second τι (“in any way”): natural English, same force; left.
- **391 `i`** turns the result clause οἷον … into a second sentence and drops ἦ μάλα as a separate word: the exclamation carries both; left.
- **402 `l`** “so, indeed” renders γάρ rather than κεν: consistent with the corrected note; left.
- **414 `i`** “the stranger” against `l` “a stranger”: the definite reading is the natural one for ξείνῳ here; left.
- **366 ἤχθετο** (ἔχθομαι ‘be hateful’ or ἄχθομαι ‘be vexed’): both layers say “hateful”, as the shipped ἀπεχθάνομαι does; the note names the verb; left.
- **415 ὀϊζύς “distress”**: three different English words are shipped for ὀϊζύς (“woe”, “suffering”, “misery”, odyssey-010 and -014). “Distress” is a fourth, but the new-renderings row records it, and “woe” is reserved for πῆμα (used two lines apart in this part’s 338) and “misery” for δύη; left, flagged for the owner.
- **363 κατὰ κόσμον `i`**: shipped renderings vary (“out of due order”, “improperly”, “in very good order”); no table row fixes the sense used here (“as things ought to be”); left.
- **344 ἑσπέριοι, 337 δύης ἐπὶ πῆμα, 345 ἐϋσσέλμῳ/ὅπλῳ, 398 ἀλεύεται (short-vowel subjunctive, not named), 414 ἄξεθ’ (aorist imperative, no house parse)**: labels checked and true of the form; left.
- **No metrical remarks** were added (no scansion flags in the packet, none of the notes depends on metre).
- `conventions.md` not edited.

## For a person or the next pass

1. Run `build_odyssey.py odyssey-069` and the validator once `gloss.json` lands; expect one WARN (rule 5: 4 openings, 5 closings, correct); add a line to LOG.md that the Cretan’s speech opened at 14.191.
2. Ratify the μαψιδίως decision (“without cause” at 14.365) and decide whether to reopen 2.56 “heedlessly” and 3.72/9.253 “at random”.
3. Table rows to add: προσεφώνεε reply-formula (14.401), μαψιδίως, and the ἠνώγει rendering “bade” (already the shipped practice, not yet a row).

## Pass 2

Reviewer: adversarial, pass 2, from scratch on the revised file (pass 1’s fixes can introduce errors). Read in full, in chunks: `conventions.md` (rules, every table row through 14.x, the glossary and note rules), `packet.md`, `units.json` as revised, `review.md` (pass 1), `new-renderings.md`, `gloss.json`, the pilot `drafts/odyssey-001/{units.json,review.md}` (for the shape of a review and of the notes), and the shipped odyssey-065 to -068 around the neighbouring marks and the speech opened at 14.191. No modern translation was opened or recalled, and Murray’s English was not opened. `units.json`, `gloss.json` and `new-renderings.md` were edited by script (`review069_pass2.py`, with pre-pass copies kept in the scratchpad); every `t` was asserted equal to its pre-pass value, and the build’s own tiling check passes.

Re-done checks: notes against the form and the line (every note read against its unit); Greek to `l` word by word; `l` against `i`; remembered English in `i`; quotation marks, `p` and `mark` (4 openings and 5 closings per layer, as pass 1 found; `p` on 321, 360, 390, 401, 409, 414; marks on 361, 390, 402, 414; the closing ” at 359 ends the speech opened at 14.191); repeated lines against the published English (14.360, 14.369–371, 14.390, 14.409 first line, 14.368 = 1.235 and 4.487: all identical to what ships; νήποινον as 1.159, ξείνια as 13.490, ἠνώγει as 10.173/23.112, προσεφώνεε as 36.381, κειμήλια, ἐνδυκέως); stock epithets against the table (all as pass 1 found); every unit ends at `. ; · ,`. Every parse in `gloss.json` was checked against the line it occurs in, and every old glossary entry that the line leans on was checked against the repo’s `odyssey-glossary.json` (an old entry that gave the wrong parse for this occurrence needed a `__broaden__`).

**Totals: 20 findings — 1 major, 7 moderate, 12 minor** (9 in the glossary, 10 in the units, 1 in new-renderings). Scale as in pass 1. (Pass 1’s fixes were all re-checked and stand; none introduced an error in the units. The one major finding is in the glossary, which pass 1 did not read.)

### Changes (line · field · severity · what was wrong · what was done)

1. **329 · gloss.json (`__broaden__` νοστήσει) · major** — The repo entry for νοστήσει is “fut. 3 sg. act.: ‘will return’”. In νοστήσει’ (ἰθάκης … ὅππως νοστήσει’) the form is the elided optative νοστήσειε, as the unit’s own note says, so the glossary would have told the reader the wrong tense and mood. Entry kept whole, then ` · also aor. opt. 3 sg., elided (νοστήσει’ = νοστήσειε), in an indirect question after a past verb: ‘how he might return’`.
2. **329 · gloss.json (`__broaden__` ὅππως) · minor** — The entry gave only “with κε + subj. (or fut.)”; the line has it with an optative in an indirect question after a past verb. Broadened.
3. **341 · gloss.json (`__broaden__` τὰ) · moderate** — The relative use in the repo entry is “neut. nom. pl.”; in ῥωγαλέα, τὰ … ὅρηαι the relative is the accusative object of ὅρηαι. Broadened (old entry whole, then ` · also relative, neut. acc. pl.: ‘which’ …`).
4. **341 · gloss.json (ὅρηαι) · moderate** — Parsed “pres. subj. 2 sg. mid. … ‘you can see’”, against the note’s “looks like a middle subjunctive, but the sense is plain present”. Now “pres. 2 sg. mid., epic ὅρηαι (a subjunctive-looking form used as a plain present; = Attic ὁρᾷ): ‘you see’”, which agrees with the note and with `l` and `i`.
5. **349 · gloss.json (θύρηθ) and n · moderate** — The glossary had θύρηθε(ν) while the note (and new-renderings row) said θύρηθι with “-θι marks place where”: two different forms asserted for one elided word, and the printed θύρηθ’ does not decide. Gloss now “θύρηθι (θύρηθε) — outside, out of doors; epic adv., elided (θύρηθ’), the ending -θι (place where) or -θε”; the note says “an elided adverb … ending in -θι (place where) or -θε”; the new-renderings row likewise.
6. **364 · gloss.json (`__broaden__` μαψιδίως) · minor** — The glossary glosses “idly, heedlessly, to no purpose” and not the “without cause” that both layers use here (as at 7.309). Broadened with the reading and the construction.
7. **378 · gloss.json (ἐξήπαφε) · minor** — “augmented” is unsupported for a reduplicated aorist whose η may be the reduplication itself. Now “epic reduplicated aor. (ἤπαφε)”, no claim about an augment.
8. **375 · gloss.json (ἐξερέουσιν) · minor** — Parsed “pres.” while the note says “could be read as present or future”. Now “pres. or fut.”, with the uncontracted ending named.
9. **398 · gloss.json (ἀλεύεται) · minor** — “pres. or short-vowel aor. subj.”: a present subjunctive of ἀλέομαι would not be spelled so. Now “aor. subj. 3 sg. mid., short vowel (= ἀλεύηται), perhaps a fut.”.
10. **409 · n · moderate** — “ὣς, with a circumflex”: the accent printed is the grave (varia) that the acute becomes in running text, not a circumflex. Now “ὣς, the accented form, is the adverb ‘so’ (unaccented ὡς is ‘as’)”.
11. **365 · n · moderate** — “had the gods not hated him, he would have died at Troy”: makes the gods the subject of δάμασσαν, which the Greek does not state (the `i` rightly keeps “they”). Now “δάμασσαν has no stated subject; the next lines say what he thinks a death at Troy would have brought, a mound and fame”.
12. **`about` · moderate** — “whose crew meant to sell him as a slave”: the lines say only that they planned “a day of slavery” (δούλιον ἦμαρ); “sell” is not in them. Now “meant to make a slave of him”.
13. **`about` · moderate** — “Odysseus proposes a bargain, clothes and a passage if Odysseus comes home”: the same name for the speaker and for the man whose return is in question, and the destination (Dulichium) missing. Now “The disguised Odysseus proposes a bargain, clothes and a passage to Dulichium if Eumaeus’s master comes home …”.
14. **348 · n · minor** — “the Cretan’s claim that no human hand freed him”: the Greek says only that the gods did it; and “the knot is pictured as being bent open” stated a picture as the sense. Now “the Cretan’s claim that the gods themselves freed him”; the picture cut, the gloss “‘unbent’, undid” kept.
15. **336 · n · minor** — ἠνώγει called “the pluperfect … used as a past tense”, while the glossary entry reads “impf.”. Now “the past tense of ἄνωγα (pluperfect in form, imperfect in sense), ‘bade’”.
16. **364 · n · minor** — “pointing at the stranger’s wretched condition, a man with nothing to gain”: an interpretation of τοῖον ἐόντα stated as the sense, with an invented motive. Now “pointing at the stranger as he sits there in his rags” (341–343 give the rags).
17. **381 · n · minor** — “he did everything a host could”: invented; the imperfect gives only “went on welcoming”. Cut.
18. **395 · i · minor** — the same phrase in the same speaker’s earlier line (14.132, odyssey-067) ships “a cloak and a tunic as clothes”; `i` had “as clothing”. Now “a cloak and a tunic as clothes, and send me …”.
19. **415 · n · minor** — “with περ stressing the contrast”: a claim about force the line does not need. Now “‘we who indeed’”.
20. **new-renderings.md · θύρηθι row · minor** — brought into line with finding 5.

### Considered and refused

- **363 κατὰ κόσμον `i`** (“as they should be”): row 911 fixes “in very good order” for 8.489, where the “very” is λίην’s; no row fixes the negated use, and the shipped renderings vary; left as pass 1 left it.
- **326 ἄνακτος / 328 θεοῖο / 325 “the heap of goods” / 386–387 / 391 / 402 `l` γάρ**: as pass 1 refused them; re-read, no new reason to move.
- **364 `l` “why you is it needful”**: ugly, within the Greek-order licence; left.
- **396 “send me to go”**: follows πέμψαι … ἰέναι; the Greek has both infinitives.
- **414 `i` “the stranger” against `l` “a stranger”**: left (as pass 1).
- **415 ὀϊζύς “distress”** and **μαψιδίως** against older shipped words: as pass 1; the μαψιδίως row stands, to be ratified by the owner.
- **369–370 full stop at the end of `l` line 2 and `i` “in time to come.”** though the Greek prints no stop at 370: the English is the shipped 1.239–241 wording, and the unit’s note says why the unit runs on; left.
- **ἔδυσαν glossed under ἐκδύω with the tmesis named**: the glossary lemmatises compounds in tmesis this way (cf. ἀνέγναμψαν); left.
- **ἔβαινον (existing entry only illustrates the tmesis use)**: its first reading (“go, step; impf. 3 pl.”) already covers the plain use here; no broadening needed.
- **Existing entry φοίτων, “uncontracted”**: looks wrong (φοίτων is the contracted imperfect of φοιτάω), but an old entry can only be broadened, never replaced; flagged for the owner, not touched.
- **ἄελλαι “storm, squall, gust” (existing entry) against `l` “blasts”**: the entry is a gloss list, not a rendering; left.
- `conventions.md` not edited.

### Build and validator (run from the odyssey folder)

`python3 build_odyssey.py odyssey-069` → `BUILT odyssey-069: 51 units, 97 lines, 121 new glossary forms (12573 total), 18 broadened`; `scansion lines needing a person or the reviewer: none`.
`python3 validate_odyssey.py odyssey-069` → two WARN (rule 5, 4 openings and 5 closings in `l` and in `i`: correct, the Cretan’s speech opened at 14.191 in odyssey-067 and closes at 14.359; say so in LOG.md) and `PASS — odyssey-069: 51 units, 97 lines, glossary 12573`. No failures.
