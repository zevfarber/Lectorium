# odyssey-023 (Odyssey 5.97–191) — review, pass 1

**Blocking issues: none.** No `t` boundary looks wrong. The paragraph (`p`) flags match Murray's ¶ at 97, 116, 145, 148, 160, 171 and 180, and every unit ends at a `.`, `;` or `·` as the rules require.

## Mechanical checks (all pass)

- **`t` untouched.** All 49 `t` fields are byte-identical to the draft at HEAD.
- **Line breaks.** Every unit has the same number of `\n` in `l` as in `t`, and no `i` contains `\n`.
- **Quotation marks.** There are 6 “ and 6 ” in `l`, and the same in `i`. They open at units 0, 13, 26, 34, 41 and 45 and close at units 11, 24, 26, 39, 43 and 48. The last speech closes inside the part at 5.191, which is correct: 5.192 begins with the narrator's ὣς ἄρα φωνήσασ’.
- **`mark` tags.** "Hermes answers" (0, 26), "Calypso answers" (13, 45), "Calypso speaks" (34, where she opens the exchange), "Odysseus answers" (41). All are accurate, and all use the house verbs ("speaks" / "answers"), which are the two most common in shipped parts.
- **Whole-unit repeats (validator rule 6).** No unit's whole Greek matches a published unit. Rule 6 compares whole units only, so it does not police the single repeated lines listed in packet.md; those are held by the convention "a repeated line gets the same English every time". I checked each one by hand (below).
- **Internal repeat.** 5.110–111 (unit 9) and 5.133–134 (unit 19) have identical `l` and `i`. Rule 6 also covers repeats within this part, and it passes.

## Changes made

| Line · field | Severity | What was wrong | What I did |
|---|---|---|---|
| 5.112 · `i` | MAJOR | The `l` ("he bade you") and the note ("serves as a simple past, ‘he bade’") read ἠνώγειν as past, but `i` had the present: "Now he bids you send the man away". So `l` and `i` disagreed on tense. | `i` → "He bade you send this man away now, with all speed;" |
| 5.99 · `n` | MINOR | "ἐμέ γε is emphatic, ‘me, of all gods’" reads more into γε than it carries. | → "γε stresses ἐμέ, ‘me’: Hermes is the one sent, and not by his own choice." This agrees with the note's last sentence and with `i`. |
| 5.123 · `n` | MINOR | "ἧος is Attic ἕως" is false: ἧος is the epic form, and ἕως is the Attic one. | → "ἧος is the epic form of Attic ἕως". |
| 5.157 (unit at 156) · `n` | MINOR | The note said the reused lines changed only by a lowered capital. In fact `l` also turns the published full stop after "pains" into a comma, so the note misdescribed its own unit. The adjustment itself is faithful. | The note now says both punctuation changes happen. |
| 5.163 · `n` | MINOR | πῆξαι was labelled only as an aorist infinitive used as an imperative. The aorist middle imperative 2 sg. is the identical form, and it pairs with the middle ἁρμόζεο in the line before. | The note keeps the infinitive reading as the simpler one and adds the middle-imperative alternative. |
| 5.166 · `l`, `i` | MINOR | μενοεικέ’ was rendered "to your heart's content" (`l`) and "all your heart could want" (`i`). These are ready-made English idioms, and they bring in "heart" where the Greek has no θυμός, κῆρ or ἦτορ. The table's row at 3.342 already turns down "to their hearts' content" as a stock idiom. The note's own gloss is "suited to the desire". | `l` → "all you could desire", `i` → "all you could desire". |
| 5.177 · `n` | MINOR | The alternative sense given for ἀέκητι σέθεν, "in spite of you, however you urge me", was muddled and nearly reversed the point. | → the phrase is hard because Calypso is urging him to go, and it seems to mean "without your true goodwill", that is, unless he can be sure she wishes him well. The `l`/`i` "against your will" stays; it matches the shipped 3.213. |
| 5.188–189 · `l`, `i`, `n` | MINOR | Verbs were mixed up across the part. Odysseus's μήδεαι (5.173) is "devising". Here φράσσομαι was "will devise" in `l` but "will take thought" in `i` and the note, and μηδοίμην was "plan". "Plan" is also the part's word for βουλευσέμεν (5.179, 5.187). | `l`: "will take thought for … I would devise". `i`: "just what I would devise". The note now gives the aorist-subjunctive possibility for φράσσομαι (the drafter's flag) and ties μηδοίμην to μήδεαι at 5.173. |
| 5.135 · `n` | MINOR | "The line reports" referred to a two-line unit. | → "The two lines report". |
| new-renderings.md · κάμμορε row | NOTE | δύσμορος already shipped as "ill-fated" in both layers (1.49, 2.351). The new κάμμορε "Ill-fated one" therefore gives two different μόρος-compounds the same English. | Added a flag to that row. I did not change the rendering; see below. |

## Findings considered and refused

- **θυμός = "heart" (the drafter's flag). RESOLVED: keep "heart".** Row 278 (θυμὸς ἀγήνωρ) claims θυμός is "kept 'spirit' throughout". Shipped text and the table itself contradict that:
  - the pilot's ὃν κατὰ θυμόν "in his own heart" (1.4)
  - the fixed κατὰ φρένα καὶ κατὰ θυμόν "in mind and in heart"
  - ὅσον ἤθελε θυμός "as much as their heart wished" (3.342)
  - τετληότι θυμῷ "with enduring heart" (4.447)
  - odyssey-022's ἑῷ θυμῷ "in his own heart" (5.76), θυμὸς ἄνωγεν "my heart bids me" (5.89), ἤραρε θυμόν "fitted his heart" (5.95), and "racking his heart" (5.83 = this part's 5.157)

  5.157 must reproduce 5.83's English under the repeated-line convention.

  One correction to the brief: rule 6 would **not** hard-fail on this. It compares only whole units, and unit 156 is a new three-line unit. The convention still binds.

  So the outlier is row 278's parenthesis, not this draft. **Orchestrator action:** amend row 278 at fold-in so that it no longer claims "spirit throughout". For example: "θυμός is usually 'heart'; 'spirit' is kept in the fixed θυμὸς ἀγήνωρ".
- **ἀέκητι σέθεν "against your will".** The rendering is kept, since it matches the shipped 3.213. Only the note was fixed (above).
- **φράσσομαι as future.** Accepted as the main reading; the alternative is now in the note.
- **ἠνώγειν as the 3 sg. pluperfect in -ειν.** Correct. Monro lists ἠνώγειν as a 3 sg. pluperfect, and some editors print ἠνώγει. The 5.139 ἀνώγει, labelled a present built on the perfect, is also correct. Only the `i` tense needed fixing (above).
- **πολύτλας "much-enduring".** Accepted. It is the literal compound (πολυ- + τλα-). It is first attested in the poem here: no published part contains it. It is distinct from ταλασίφρων "enduring-minded"/"steadfast" and ταλαεργοί "labour-enduring" while showing the shared root, and the rejected alternatives are well argued. "much-enduring, heavenly Odysseus" keeps δῖος as the table's "heavenly".
- **ὣς φάτο, ῥίγησεν δὲ [Name] "So he spoke, and shuddered, [Name],".** Accepted. It follows the shipped 4.609 μείδησεν frame exactly, and "shuddered" keeps ῥῖγος. No existing row claims "shuddered".
- **5.181 "her hand" for the fixed "his hand".** Accepted as a faithful gender adjustment, since χειρί has no possessive. It follows the same principle as "So he/she spoke", and rule 6 is not touched.
- **Differing shipped `i` wordings of καί μιν φωνήσας(’) ἔπεα πτερόεντα προσηύδα** ("raising her voice" at 2.269 vs "lifting his voice" at 1.122). Both are reproduced as shipped at 5.117 and 5.172, which is correct under the repeat rule. The inconsistency between the earlier parts is theirs and is noted for the table.
- **κάμμορε "Ill-fated one".** Not changed. κατα- and δυσ-μορος are near-synonyms, and every root-faithful alternative ("doomed", "ill-doomed") overstates or sounds archaic. It is flagged in new-renderings.md for the table owner.
- **ἀργῆτι κεραυνῷ "bright".** Not changed. "bright" is not reserved; it is already shipped for λευκός at 5.70 (ὕδατι λευκῷ "bright water"), a close colour-word. Note, though, that the new-renderings row reserves "shining" for φαεινός, while 5.86 shipped φαεινῷ as "shining" in `l` but "bright" in `i`. That is harmless, but worth knowing at fold-in.
- **5.99 `l` "Zeus bade me, me, come here".** The doubled "me" is odd but deliberate: it renders ἐμέ γε. I left it, and the note now explains the emphasis. Pass 2 may prefer "me — me —".
- **5.182 `i` "nothing you know is empty".** Slightly stiff, but built from οὐκ ἀποφώλια εἰδώς rather than recalled. Kept.
- **Remembered-English sweep.** Apart from 5.166, nothing in `i` reads as recalled from a modern version. "What a rogue you are", "his sweet life was ebbing away" and "he unwilling and she willing" all follow the Greek construction directly.
- **Cross-references verified against the text.** These all check out:
  - 5.14 ἀνάγκῃ; 5.33 σχεδίη; 5.42 and 5.26 (the repeated lines); 5.82 κλαῖε καθήμενος; 1.14 πότνια
  - 3.280 ἀγανοῖς βελέεσσιν (the shipped wording is followed); 4.805 θεοὶ ῥεῖα ζώοντες; 4.504 μέγα λαῖτμα θαλάσσης; 4.707 ὠκυπόρων "swift-faring"; 4.25 ἀγχοῦ δ’ ἱστάμενος; 2.230 πρόφρων "ready-minded"; 4.511 ἁλμυρὸν ὕδωρ "briny water"
  - all in-part line numbers (99, 105, 108, 112, 113, 119, 122, 124, 131, 143, 152, 171, 173, 179, 182, 185, 187)
- **House-renderings compliance.** Checked every occurrence of δῖα θεάων, ἔπεα πτερόεντα προσηύδα, τὴν δ’ αὖτε προσέειπε, διάκτορος, ἀργεϊφόντης, κρατὺς ἀργεϊφόντης, μεγαλήτορα, ἐπ’ ἠεροειδέα πόντον, οἴνοπι πόντῳ, πόντον ἐπ’ ἀτρύγετον, ἐν σπέσσι γλαφυροῖσι, ἤματα πάντα, αἰγιόχοιο, νῆες ἐῖσαι, νῆα θοήν, ὣς φάτο, the masculine ὣς ἄρα φωνήσας ἀπέβη, δῖος, ἐυπλόκαμος and ῥοδοδάκτυλος Ἠώς. All use the table's exact wording.
- **Published repeated lines.** 5.115, 5.117, 5.142, 5.144, 5.157, 5.158, 5.172 and 5.181 are reproduced verbatim. The only changes are the ones each sentence forces:
  - 5.157/158: punctuation and a lowered capital.
  - 5.141: μοι for οἱ, so "I have" for "he has". This is 5.141, not 5.142, and it is not itself a repeat.
  - 5.181: "her hand".
  - 5.168: ἵκηαι for ἵκηται, so "you" for "he".

  Each adjustment is faithful to the Greek.

## Review pass 2

**Blocking issues: none.** I did not touch `units.json` in this pass, so every `t` is byte-identical to HEAD. I found no problem with `t` or unit boundaries. I also ran the build's glossary checks against the edited `gloss.json` without writing anything. Nothing redefines an existing form, nothing lies outside this part, every broadening keeps its old entry whole, and no form is missing.

### Glossary: corrections to new entries (10)

| Form | Severity | What was wrong | What I did |
|---|---|---|---|
| τοσσόνδε | MINOR | The lemma was given as τόσος. LSJ lemmatises the -δε compound as τοσόσδε. | Lemma → "τοσόσδε (epic τοσσόσδε, …)". The rest is unchanged. |
| παρεξελθεῖν | MINOR | "(Attic παρελθεῖν with extra preverb)" wrongly implies that παρεξέρχομαι is a non-Attic stand-in. The compound exists in Attic as well. | → "(παρα- + ἐξ- + ἐλθεῖν)". |
| δακρυόφιν | MINOR | It was parsed as "pl.". The -φι(ν) suffix does not mark number. | → "neut. gen./abl. with the epic suffix -φιν (number not marked)". |
| πῆξαι | MINOR | The entry gave only the infinitive-as-imperative reading. The unit's note, as fixed in pass 1, also allows the identical aor. mid. imper. 2 sg. | Added "(or aor. mid. imper. 2 sg., the same form)", so the entry and the note agree. |
| πέλασσε | MINOR | The parse left out that the form is unaugmented and has epic σσ. The house practice, as with μάχοντο and μίγη, is to flag both. | → "aor. 3 sg., unaugmented, epic σσ (= Attic ἐπέλασε)". |
| ἀλίτοντο | MINOR | The augment is missing, but this was not flagged. | → "aor. mid. 3 pl., unaugmented (= ἠλίτοντο)". |
| ῥίγησεν (5.116, 5.171) | MINOR | The augment is missing, but this was not flagged. | Added "unaugmented (= ἐρρίγησεν)". |
| ἀποπέμψω | MINOR | The gloss "’I will send you away’" pinned the entry to line 161, which breaks the rule that an entry is general to its form. | → "’I will send away’". |
| ἱερά | MINOR | The lemma was given as ἱερόν. LSJ lemmatises the word as ἱερός. | → "ἱερός (neut. as noun ἱερόν)". |
| ἠνώγειν | NOTE | This entry says plupf. The existing published ἠνώγει entry says impf. for the same tense. | Added "(= ἠνώγει, often labelled impf.)" so that a reader comparing the two is not confused. |

### Glossary: broadenings (10 new, and 1 extended)

The glosser checked only the forms it could see needed a new sense. I checked every known form in the part against its actual line or lines. Each of the entries below is a published entry that fails a real use in this part. In each case the old text is kept whole and the new reading is appended after " · ".

- **ἀκτῆς (5.151). MAJOR.** The only published entry is ἀκτή "grain, meal", and it explicitly calls that "a homonym of ἀκτή ’shore’". Here ἐπ’ ἀκτῆς is "on the shore". I added the ‘shore’ reading. The same gap already shipped at 5.82 in odyssey-022.
- **ἐθελούσῃ (5.155). MAJOR.** The published gloss is "’unwilling’ (οὐκ ἐθελούσῃ)". Here the word is un-negated and means the opposite, "she willing" (οὐκ ἐθέλων ἐθελούσῃ). I added "without a negative: ’willing’".
- **ἀνώγει (5.139). MAJOR.** The published entry says "impf. 3 sg. ’was bidding’". Here the verb is paired with the present ἐποτρύνει and is itself a present, as the unit's note says. I added "pres. 3 sg. … ’bids’".
- **ἄπυστος (5.127). MAJOR.** The published entry gives only the passive sense, "unheard of". Here the sense is active, "without tidings": Zeus was not long uninformed. LSJ cites this very line for the active sense, and the `l` and the note both use it. I added the active reading.
- **ἀργαλέον (5.175). MINOR.** The published parse is "neut. nom. sg., impersonal predicate governing an inf.". Here the word is a neuter accusative agreeing with λαῖτμα, as the note says. I added that reading.
- **θεά (5.173, 5.178). MINOR.** The published entry says "nom. sg.". Both uses here are vocative. I added "voc. sg. (same form)". The glossary already marks vocatives elsewhere (φίλε, τέκνον).
- **θεοί (5.118, 5.129). MINOR.** The published entry says "nom. pl.". Both uses here are vocative. I added "voc. pl.". I left θεὰ (5.97) and θεοὶ (5.122) alone, because a nominative reading is defensible there.
- **ὅττι (5.112). MINOR.** The published entry is "whoever, whatever". It does not cover the superlative idiom ὅττι τάχιστα, "as quickly as possible", which appears here for the first time. I added the idiom.
- **ἐποιχομένη (5.124). MINOR.** The published sense is "go to and fro at, ply (the loom)". Here the word means "come upon, assail", with her shafts; the `l` has "assailing" and the `i` has "came upon him". I added that sense.
- **αὐτῇ (5.189, 5.190). MINOR.** The published entry gives "’for herself’" and "’in it’". Here the word reinforces a first-person pronoun (ἐμοί περ αὐτῇ, μοι αὐτῇ), so the sense is "myself". I added that reading.
- **μή (5.147), extending the glosser's broadening. MINOR.** The glosser correctly added μή + fut. inf. for 5.179/187. But the fear clause at 5.147, μή πώς … χαλεπήνῃ, takes the subjunctive after a primary verb, and the old entry covers only "the optative in secondary sequence". I appended "’lest’ with the subj. after a primary verb".

**The glosser's own 6 broadenings are confirmed as warranted and correct.**
- **αὐτῆς:** ἐπ’ αὐτῆς 5.163 is governed by a preposition, and the old entry says "governed by a noun".
- **τὸν:** τὸν μῦθον 5.98 and 5.183 is adjectival.
- **ἧος:** at 5.123 it means "until" with an indicative past terminus.
- **ὅτε:** 5.189 has the optative, "if ever".
- **μή:** 5.179 and 5.187 have μή + fut. inf. after swearing.
- **πέρι:** ἄστυ πέρι 5.106 is a preposition in anastrophe with the accusative.

### Glossary: checked and confirmed (NOTE)

- **All 152 new entries.** I checked each against every occurrence in the 49 units. Apart from the rows above, every lemma, parse, meaning and Attic equivalent is correct, including the forms that occur twice (κεραυνῷ, ἀργῆτι, βουλευσέμεν, παρεῖναι, κατειβ-). The entry shape is correct. No entry has an ASCII apostrophe, a backtick or a straight quote, and none is longer than 230 characters.
- **Other known forms.** These cover their uses here and were left alone:
  - τὸ at 5.175 and 5.185; ὅς at 5.128 and 5.185
  - ᾧ, οἷς and ἣν as possessives; οἶον and οἷον
  - ἐπὶ at 5.175, as an adverb or in tmesis; πάρα; ἔνι; περὶ + gen. at 5.130
  - ὅτ’ and ὁπότ’; τις, τι and τί; τοι as both pronoun and particle
  - ἤματα; ὕδωρ as nom. and acc.; κακὸν
- **Left as they stand (not wrong enough to broaden):**
  - ὥς at 5.164 is a purpose clause without κε, but the entry's ‘so that’ still conveys it.
  - μευ at 5.170 is a gen. of comparison, but "gen. sg." is still true.
  - ἐυπλόκαμος has a parenthesis "(Calypso’s standing epithet)" though it is used of Demeter at 5.125, and its gloss "fair-tressed" differs from the table's "fine-plaited". That is harmless to this part and flagged for fold-in.

### Translation

**No translation corrections were needed.** I re-verified each of pass 1's changes against the Greek and all ten are correct:

- **5.112 `i` (the MAJOR fix).** ἠνώγειν is a pluperfect used as a simple past, so "He bade" is correct, and `l`, `i` and the note now agree.
- **5.99 note.** Correct.
- **5.123 note.** "ἧος is the epic form of Attic ἕως" is correct.
- **5.157 note.** Correct.
- **5.163 note.** Correct, and now matched by the πῆξαι entry.
- **5.166.** "all you could desire" is correct. No published repeat is involved.
- **5.177 note.** Correct.
- **5.188–189.** The verbs are now consistent across the part. No published repeat is involved.
- **5.135 note.** Correct.
- **new-renderings.md flag.** Correct.

I also checked the following, and all of it holds:
- **Line breaks.** Every unit has the same number of `\n` in `l` as in `t`, and no `i` contains `\n`.
- **Quotation marks.** There are 6 “ and 6 ” in `l`, and the same in `i`. They open at units 0, 13, 26, 34, 41 and 45 and close at 11, 24, 26, 39, 43 and 48. The `mark` tags sit on the opening units.
- **Internal repeat.** 5.110–111 (unit 9) and 5.133–134 (unit 19) have identical `l` and `i`.
- **The 8 published repeated lines.** 5.115, 5.117, 5.142, 5.144, 5.157, 5.158, 5.172 and 5.181 still reproduce the shipped wording line for line. The only changes are the forced punctuation, pronoun and gender adjustments pass 1 recorded.
- **House-renderings table.** Every fixed formula still matches its row, re-checked against the table:
  - δῖα θεάων, ἔπεα πτερόεντα προσηύδα, τὴν δ’ αὖτε προσέειπε
  - διάκτορος and ἀργεϊφόντης, the masculine ὣς ἄρα φωνήσας ἀπέβη, ὣς φάτο (he and she)
  - οἶνοψ πόντος, ἀτρύγετος, νηῦς θοή, νηῦς ἐίση
  - ἐπ’ ἠεροειδέα πόντον, ἐν σπέσσι γλαφυροῖσι, ἤματα πάντα, μεγαλήτωρ
  - δῖος, and the κατέρεξεν gesture formula
- **Grammatical labels in the notes.** All are true of the form in its line, and no note contradicts its own `l` or `i`. A few cosmetic differences remain, and each is within the note's own scope: 5.152 note "flowing away" against `l` "ebbing away"; 5.129 note "is at my side" against `l` "be beside me"; the 5.97 note allows either case for θεά.
- **5.141 `i` (NOTE).** The `i` contains an ASCII apostrophe ("the sea's broad back"). It reproduces the shipped wording of 5.142's repeat verbatim, and the same string has already shipped in four parts, so it stays. It is flagged for a global typographic sweep.

**Build readiness: clean.** Run `python3 build_odyssey.py odyssey-023`, then `python3 validate_odyssey.py odyssey-023`.
