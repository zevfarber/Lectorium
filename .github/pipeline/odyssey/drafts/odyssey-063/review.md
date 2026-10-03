# odyssey-063 (13.113–216) — review

## Pass 1

Scope: grammar and position claims in every note, cross-references, Greek → `l` word by word, `l` ↔ `i`, remembered English in `i`, quotation marks and speech `mark`s, the packet's flagged line (13.213), and the rows of `new-renderings.md` against the table in `conventions.md`. `units.json` was edited in place by script; the `t` of all 64 units was asserted unchanged before and after (the unit tiling, `ln`, `p`, `v` and line counts of `l` were re-checked after the edits). Not touched in this pass: `gloss.json` (not yet written), `new-renderings.md`, `conventions.md`.

Severity: high = fails the validator, or a note states something false about this line (a wrong label, position or cross-reference); medium = a wrong form or label of lesser weight, or a conflict with the house table; low = polish, an addition not in the Greek, or an `l`/`i` mismatch of force.

Totals: 20 findings, all fixed in the file — **6 high, 5 medium, 9 low**. One consequence is left open for the caller (the stray ” at 13.178, below).

### Changes made

| Line · unit | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 13.178 (first half, "ὣς ἀγόρευ’ ὁ γέρων·") | `l` | high | Same Greek as the shipped unit at odyssey-038 line 570, whose `l` is "So the old man spoke;" (the validator, check 6, refuses a different English). The draft had "So spoke the old man;". The packet did not list it because it only matches whole lines. | `l` set to the shipped "So the old man spoke;". `i` already matched. |
| 13.178 (second half, "τὰ δὲ δὴ νῦν πάντα τελεῖται.") | `l`, `i`, `n` | high | Same Greek as the shipped unit at odyssey-006 line 176; draft English differed in both layers (validator check 6 would fail). | `l` = "and now indeed all these things are being fulfilled.”" and `i` = "and now, indeed, all of it is coming to pass.”", exactly as shipped, closing ” included. One sentence added to the note saying the English is kept as shipped at 2.176 and that its closing mark closes nothing here. **Open**: see below. |
| 13.120 · unit "ἐκ δὲ κτήματ’ ἄειραν" | `n` | high | "The unit begins mid-line, after the comma." False: the unit begins at the start of line 120 (line 119 ends with the comma). | Replaced by "It continues the sentence of the last unit, after the comma at the end of line 119." |
| 13.155 · unit "ὁππότε κεν …" | `n` | high | "The last line is word for word Poseidon’s line 152." False cross-reference: 152 opens ἀνθρώπων, 158 opens ἄνθρωποι; only the rest of the line is identical. | Now "The last line, from μέγα δέ on, is word for word Poseidon’s line 152 (which opens with ἀνθρώπων where this has ἄνθρωποι)". |
| 13.192 · unit "μή μιν πρὶν …" | `n` | high | Said ἄλοχος, ἀστοί and φίλοι are all "joined by τε … τε". Only ἀστοί τε φίλοι τε is; ἄλοχος stands without a connective. | Reworded: ἄλοχος, and ἀστοί τε φίλοι τε "the last two joined by τε … τε". |
| 13.209 · unit "ὢ πόποι, οὐκ ἄρα …" | `n` | high | μ’ ἔφαντο … ἄξειν was labelled "an accusative with the future infinitive" (as if accusative-and-infinitive of indirect speech). μ’ is με, the object of ἄξειν; the infinitive's subject is the same as the subject of ἔφαντο. | Label corrected to say exactly that. |
| 13.120 · same unit as above | `n` | medium | "tmesis for ἐξήειραν": ἄειραν is unaugmented, so the compound would be ἐξάειραν, not the augmented form. | Replaced by a statement of the tmesis without naming a form: "the preverb ἐκ standing apart from the verb". |
| 13.189 · unit "περὶ γὰρ θεὸς …" | `n` | medium | "tmesis for περιέχευε" beside "χεῦε is the unaugmented aorist": the two statements disagree; the unaugmented compound is περίχευε. | Now "tmesis for περίχευε". |
| 13.122 · unit "καὶ τὰ μὲν οὖν …" | `n` | medium | μή πώς … δηλήσαιτο called "a clause of fear". There is no verb of fearing; it is a precaution, a negative purpose clause ("lest"). | Now "a negative purpose clause after a past verb". |
| 13.213 · unit "Ζεὺς σφέας τίσαιτο …" | `l`, `i`, `n` | medium | τίσαιτο and τίνυται are the same verb (τίνυμαι). Table row 1453 (12.378) fixes it as "take vengeance on" in both layers and lists "punish" as avoided; the draft had "punish(es)" in `l` for both, and in `i` "punish" for the first and "takes vengeance on" for the second (one verb, two English words in one sentence). | `l`: "may take vengeance on them … and takes vengeance on whoever errs"; `i`: "take vengeance on them … takes vengeance on whoever does wrong". Note gloss reordered to "take vengeance on, punish". The `new-renderings.md` row for ἐφορᾷ … τίνυται now needs its `l` amended (see below). |
| `about` | `about` | medium | Said Zeus advises turning the ship into a stone "instead" (of the mountain). Zeus keeps the mountain (154–158 end with μέγα δέ σφιν ὄρος πόλει ἀμφικαλύψαι, which unit 13.155's note itself says). Also "gifts hidden under an olive tree" (Greek: put beside the trunk, out of the road) and "blaming the Phaeacians for deceiving him" (Greek: they said they would bring him to Ithaca and did not). | Rewritten to: gifts set down beside an olive tree off the road; Zeus advises turning the ship into a stone within sight of the whole city, keeping the mountain in the plan; Poseidon goes to Scheria and turns the ship to stone as she comes in; Odysseus blames the Phaeacians for not keeping their word to bring him to Ithaca. |
| 13.116 · unit "οἱ δ’ ἐκ νηὸς …" | `l`, `i`, `n` | low | The cloth is λίνον, shipped in the previous part (13.73) as "a linen cloth" beside "a blanket"; here "the linen" (`l`) and "the linen sheet" (`i`) named the same object differently. | `l` "the linen cloth", `i` "the linen cloth"; note adds that these are the ῥῆγος and linen cloth spread for him on the ship at 73. (`rug` kept, see refused findings.) |
| 13.125 · unit "οὐδ’ ἐνοσίχθων …" | `i` | low | "but went to find out the plan of Zeus": ἐξείρετο is "inquired into"; "went" is not in the Greek. | "but inquired into the plan of Zeus:". |
| 13.128 · unit "Ζεῦ πάτερ …" | `l`, `i` | low | "from my own stock" / "of my own stock": ἐμῆς is plain "my"; "own" is the sense of the possessive ὅς, which the course teaches to keep apart. | "own" dropped in both layers. |
| 13.154 · unit "ὢ πέπον …" | `l`, `i` | low | "my own heart": ἐμῷ θυμῷ, same point. | "own" dropped in both layers. |
| 13.143 · unit "ἀνδρῶν δ’ εἴ πέρ τις …" | `l` | low | `l` ended with a full stop, while the note says the English carries on with a comma and the next `l` begins in lower case. | `l` now ends with a comma, as `i` does. |
| 13.147 · unit "αἶψά κ’ ἐγὼν …" | `i` | low | "at once" for αἶψα; the table (row for καρπαλίμως) keeps "quickly" for αἶψα and "at once" for αὐτίκα; `l` already had "Quickly". | `i`: "I would do it quickly". |
| 13.149 · unit "νῦν αὖ Φαιήκων …" | `i` | low | `i` "Now, for my part" against `l` "Now in turn": αὖ is "in turn, again", not a contrast with Zeus. | `i`: "Now, in my turn,". |
| 13.169 · unit "καὶ δὴ προὐφαίνετο πᾶσα." | `n` | low | "close to the harbour": the Greek says near the land (ἐγγύθι γαίης, 156), not near a harbour. | "close to the land". |
| 13.215 · unit "ἀλλ’ ἄγε δὴ τὰ χρήματ’ …" | `n` | low | ἀριθμήσω called a subjunctive flatly; the form is a short-vowel subjunctive or a future (the note hedges the parallel ἱερεύσομεν at 13.181 and should do the same). | Now "ἀριθμήσω (a short-vowel subjunctive, though it could be read as a future) and ἴδωμαι (an aorist subjunctive)". |

### Hand-scan of the flagged line

- **13.213** (`Ζεὺς σφέας τίσαιτο ἱκετήσιος, ὅς τε καὶ ἄλλους`; scanner: UNRESOLVED; synizesis, lengthening, correption). Scanned by hand, fifteen syllables: Ζεὺς σφέας (σφέας as one long syllable) | τῑ σαι | το (short, lengthened as the longum of foot 3 at the main caesura) ἱ κε | τή σι ος | ὅς τε καὶ (καὶ shortened before ἄλλους) | ἄλ λους. Iota of τίσαιτο is long (τίσις, ἀποτῖσαι at 193), so no other fit exists. The irregularity is real; the note at that unit already carries the one plain sentence ("As transmitted, line 213 is metrically irregular at τίσαιτο, whose short final syllable has to count as long at the main caesura, and σφέας must be read as one syllable.") and it is correct; left as drafted.

### Quotation marks and speech marks (checked, no change except the stray ” below)

Seven speeches, each with `mark` on its first unit and “ on that unit, ” on its last: Poseidon 128–138; Zeus 140–145; Poseidon 147–152; Zeus 154–158; an anonymous Phaeacian 168–169; Alcinous 172–183; Odysseus 200–216. Nothing inside a speech is quoted (the old man's prophecy at 175–177 is indirect). Paragraph flags `p` fall on the eleven ¶ lines (113, 128, 139, 146, 153, 159, 168, 170, 172, 184, 200). The last unit of odyssey-062 (13.111) is narration, so no speech runs on into this part, and Odysseus's speech closes at 216 (the next paragraph is narration). Counts in `l` and `i` are 7 “ and 8 ” because of the closing mark carried by the shipped English at 13.178 (below); the validator will print its expected quotation-mark WARN.

### Repeated lines (checked)

13.137, 139, 153, 166, 167, 170, 172, 174, 177, 200, 201, 202 (packet list) all reuse the shipped English as far as the sentence allows. The packet missed 13.178 (both halves are shipped whole units; found by comparing every unit with the published units, as the validator does); fixed above. After the edits no unit of this part has the same Greek as a shipped unit with different English.

### Findings considered and refused

1. **ἄρα, ῥα, γε, περ untranslated in `l`** (e.g. κὰδ δ’ ἄρ’ ἐπὶ ψαμάθῳ, ἦ ῥ’ οἵ γ’, οὐκέτ’ ἐγώ γε). House practice leaves these weak particles out of `l` unless they carry sense; none here changes the meaning. Left.
2. **Rendering ῥῆγος as "blanket" and ῥῆγος … σιγαλόεντι as "glossy blanket"** (row 1105 lists "rugs" as avoided for ῥήγεα πορφύρεα; odyssey-062 has "a blanket" at 13.73). The Greek phrase ῥήγεα σιγαλόεντα is already shipped as "glossy rugs" (odyssey-027 and odyssey-052); the unit keeps that and its note now ties the cloth to 13.73. Flagged for the owner as a standing inconsistency, not edited.
3. **"the flat of his hand" / "the flats of his hands" for χειρὶ/χερσὶ καταπρηνέσσι** (13.164, 13.199) as possibly remembered English. I did not consult any translation to test it. The sense is the LSJ gloss of καταπρηνής ("with the flat of the hand") and `l` carries the literal "downturned", so it passes the "rebuild from the grammar" test. Kept; the caller may wish to know the phrase is an unusual one.
4. **Joining the two halves of 13.178 into one unit** (the odyssey-025 precedent in QUESTIONS.md, which avoids carrying a closing ” into the middle of a speech). Refused only because this pass may not touch `t`. See open item.
5. **13.182 `i` "in the hope that he will take pity" for αἴ κ’ ἐλεήσῃ** (`l` and the note: "if he may/should take pity"). An idiomatic rendering of "in case", same sense; kept.
6. **13.131 `i` "Why, even now:"** for καὶ γὰρ νῦν. English idiom for "for even now"; kept.
7. **Notes outside the 25–110-word band** (over: the units at 116, 122, 128, 136, 149, 172, 189, 209, 213; under: the repeated formula at 153, 17 words). Each long one is a hard spot with several forms to parse; the short one is a repeat of 139. Validator WARNs only; left.
8. **13.139 / 153 note "τὸν δ’ ‘to him’"** for an accusative: a gloss of the formula, not a parse; left.
9. **13.198 ὣ as dual of possessive ὅς**: stated as "taken as", already hedged; left. (The glossary entry should carry the same hedge; to be checked in pass 2.)
10. **ἴσαν "old pluperfect of οἶδα"** and **κίον "the past tense of κίω"**: acceptable labels (the second deliberately non-committal); left.

### Open item for the caller

- **Stray ” at 13.178.** To satisfy the validator the second half-line must carry the shipped English with its closing ” (it ended a speech at 2.176). Here it sits in the middle of Alcinous's speech, which ends at 183. The odyssey-025 precedent avoided this by joining the neighbouring units; that would mean replacing units 13.178a and 13.178b by one unit with `t` = "ὣς ἀγόρευ’ ὁ γέρων· τὰ δὲ δὴ νῦν πάντα τελεῖται." (`l` "So the old man spoke, and now indeed all these things are being fulfilled."; `i` "So the old man spoke, and now all of it is being fulfilled."), with no closing mark. I have left the two units as they were cut, because the brief forbids touching `t`. If the join is made, the notes of the two units should be merged and the quote-mark count returns to 7 and 7.

### Rows of `new-renderings.md` against the table (not edited; for the caller to amend before the rows are copied into `conventions.md`)

1. **ἐφορᾷ … τίνυται** — `l` should now read "oversees … takes vengeance on" (the unit follows row 1453 for τίνυμαι, which lists "punish" as avoided); the row's `l` "punishes" is stale, and "avenges" should stay in the avoided list. Add τίσαιτο (13.213) to the row.
2. **νοήμων "discerning"** collides with the existing row for πινυτός (11.445), which is also "discerning" in both layers; the row does not acknowledge it. Either say the two words are told apart by context (as the table does for δύσμορος / κάμμορος) or choose another English. The unit keeps "discerning".
3. **ἐννοσίγαιος alone** repeats an existing row (bare ἐννοσίγαιος at 11.102, "the earth-shaker"); merge with it.
4. **ἔπεα πτερόεντ’ ἀγόρευον** repeats the existing row for 9.409 (plural, with ἀπαμειβόμενοι). Merge, or cite it.
5. **ὑπερβασίη** — the row lists "outrage" as avoided, but odyssey-010 (3.206) ships `i` "grievous outrage" for the same word (its `l` "transgression" agrees with this row). The row should say so or the earlier unit is left as an acknowledged divergence.
6. **ᾤμωξεν** — the row avoids "wailed" and "groaned", but odyssey-043 (9.395) ships `l` "wailed" for the same verb and the table (οἰμώξας, 9.506) has "groaning/groaned"; the row should note that the finite aorist here is "cried out" and that the others stand as shipped. The avoided gloss "wailed (reserved for ὀλοφύρομαι)" is also wrong: ὀλοφυρόμενος is "lamenting" in the same part.
7. **ἄστυ "town"** with "city" listed as avoided (reserved for πόλις): shipped parts use "city" for ἄστυ (odyssey-028, -029, -030, -033, -034 and others) and "town" in others (odyssey-005, -038, -046); the reservation is not true of what is shipped.
8. **ῥῆγος / ῥήγεα** — no row, though the unit uses "rug" against table row 1105 (see refused finding 2). A row stating the choice would close it.
9. **χρήματα / κτήματα** both "goods": acknowledged in the row; fine.
10. The remaining rows (ἐΰζυγος, δεδμημένον ὕπνῳ, ἀθρόα, ὁδίτης, εὐρυσθενής, κελαινεφές, ὢ πέπον, ἀλλοειδής, ἀτραπιτοί, λιμένες πάνορμοι, ἀναΐξας, ὣ … μηρώ, καταπρηνής, ὀλοφυρόμενος, πατρώϊος, βωμός, ὑπερμενής, ἀπήμων of escorts, ἱκετήσιος, ἕλωρ, ἄγνωστος) match what the units use in both layers and do not conflict with a table row; the shipped-at claims for δεδμημένον ὕπνῳ (7.318), ἔπεα πτερόεντ’ ἀγόρευον (odyssey-015 line 189, odyssey-043) and ἀπήμων (8.565) were checked and are true.

### Left for pass 2

`gloss.json` (parses against the line, including ὣ at 13.198, ἔξ at 13.130, ἀριθμήσω at 13.215, ἱερεύσομεν at 13.181, and the broadened entries) and a second full read of `l`/`i` after this pass's edits.

### Resolution of the open item (caller)
13.178a and 13.178b joined into one unit (the odyssey-025 precedent), notes merged, no closing ” — quotation marks back to 7 and 7. The unit has new Greek, so no shipped unit conflicts.

## Pass 2

Scope: a second full read of every unit's `note`, `l` and `i` after pass 1's edits and the 178a/b join (63 units), against the Greek line by line (case, tense, mood, position claims, cross-references, quotation marks, `p` and `mark`); every entry of `gloss.json` checked against each line where the form stands (all 104 novel entries and the 13 `__broaden__` entries), and the 384 known-form entries of `known-forms.json` checked for uses the old entry does not cover. Greek, LSJ, Autenrieth, Cunliffe, Monro and Smyth only; no translation consulted. `units.json` and `gloss.json` edited in place by script (indent kept); the `t` of all 63 units asserted unchanged before and after (sha256 of the list of `t` strings identical). Line counts of `l` against `t`, absence of ASCII apostrophes and backticks, entry length under 230 (novel entries), and the rule that each `__broaden__` entry contains the old entry whole were re-checked after the edits. Nothing from pass 1 was reverted; no pass-1 edit was found to be wrong. The join at 13.178 was checked: one unit, no closing ”, quotation marks 7 and 7, note merged correctly.

Totals: 31 findings, all fixed in the file — **0 high, 7 medium, 24 low**.

### Changes made — `units.json`

| Line · unit | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 13.134 · "οἱ δ’ εὕδοντ’ …" | `n` | medium | "Ἰθάκῃ has the Ionic -η" set up a contrast that does not exist: Attic also has η after κ (ᾱ only after ε, ι, ρ), so Ἰθάκη is the same in Attic. | "Ἰθάκῃ is the dative of Ἰθάκη." (The corresponding claims for Τροίης, Σχερίην, Ἀθηναίη, ὑπερβασίην are true, because ι precedes.) |
| 13.168 · "ὤ μοι, τίς δὴ νῆα …" | `n` (and gloss `ἐπέδησ`) | medium | The note derived ἐπέδησ’ from πεδάω; the glossary entry derived it from ἐπιδέω. Two lemmas for one form. ἐπ-έδησε from ἐπιδέω and ἐ-πεδ-ησε from πεδάω are spelled alike, so neither can be asserted alone. | Note now "the aorist of ἐπιδέω ‘bind on’ (or of πεδάω ‘fetter’, from πέδη ‘fetter’, which is spelled the same)"; gloss entry hedged the same way (see below). |
| 13.213 · "Ζεὺς σφέας τίσαιτο …" | `n` | low | "σφέας must be read as one syllable" is too strong: Ζεὺς σφέ|ας as a dactyl (σφέας disyllabic, both short) fits the line as well as the spondaic fifteen-syllable scan. What is certain in both scans is the longum at τίσαιτο (the metrical lengthening at the penthemimeral caesura), which the note already states. | "and σφέας is read as one syllable, as usual in Homer." |
| 13.139 · "τὸν δ’ ἀπαμειβόμενος …" | `n` | low | "τὸν δ’ ‘to him’": τόν is the accusative object of προσέφη, not a dative; a learner would take it for a dative. | "τὸν δ’ ‘and him’ (the article as a pronoun, accusative)". |
| 13.132 · "νόστον δέ οἱ …" | `n` | low | "the negative οὔ ποτε goes with πάγχυ": οὔ negates the verb; πάγχυ limits the negation. Loose, and wrong as a label. | "the negative οὔ ποτε ‘never’ is limited by πάγχυ ‘altogether’, so the claim is that …". |
| `about` | `about` | low | "the Phaeacians, seeing it, recall the old prophecy and decide to stop giving escorts and to sacrifice twelve bulls": the Phaeacians in 168–170 do not understand; Alcinous recalls the prophecy and proposes both measures (172–183), and they obey (184). | "Alcinous, seeing it, recalls the old prophecy and bids the Phaeacians stop giving escorts and sacrifice twelve bulls, which they set about doing." |
| `about` | `about` | low | "and goes to count his goods": the part ends with Odysseus saying "let me count" (215); he has not yet done it. | "and resolves to count his goods." |

### Changes made — `gloss.json` (novel entries)

| Form · line | Sev. | What was wrong | What was done |
|---|---|---|---|
| κάρτεϊ · 143 | medium | "dat. of means: ‘by might’". In βίῃ καὶ κάρτεϊ εἴκων the dative is the thing yielded to (εἴκω + dat.), as the unit's `l`, `i` and note all have it ("to force and might yielding"). The parse contradicted the unit. | "neut. dat. sg., epic, with εἴκων: ’(yielding) to might’". |
| ἔξ · 130 | medium | "accented ἔξ when placed after its noun (anastrophe)". False: ἔξ stands after the adjective ἐμῆς and before its noun γενέθλης, and anastrophe is not what accents it; a proclitic takes an acute before an enclitic, and εἰσι (3 pl. of εἰμί) is enclitic. The unit note ("ἔξ is ἐξ before εἰσι") was right and the entry was not. | "accented ἔξ because the enclitic εἰσι follows it: ’of (my stock)’". |
| ἀπολλήξωσι · 151 | medium | "short-vowel" is false: -ωσι is the ordinary long-vowel subjunctive ending of a sigmatic aorist (a short-vowel subjunctive would be ἀπολλήξουσι). | "short-vowel" removed; Attic form named: "aor. subj. 3 pl., in a purpose clause after ἵνα (= Attic ἀπολήγω)". |
| ἐπέδησ · 168 | medium | Lemma ἐπιδέω against the note's πεδάω (see above). | "ἐπιδέω — bind on, fetter (or aor. of πεδάω ’fetter’, spelled the same); aor. 3 sg., elided (ἐπέδησ’ = ἐπέδησε)". |
| γνοίη · 192 | low | "in a fear clause after μή" while the unit note (and pass 1's note at 13.122) call the construction a negative purpose clause continuing ὄφρα; and "’lest she recognise’" fits only one of the three subjects (ἄλοχος, ἀστοί, φίλοι). | "in a negative purpose clause after μή: ’lest he or she recognise’". |
| δηλήσαιτο · 124 | low | Same: "fear clause" against the note's "negative purpose clause after a past verb". | "in a negative purpose clause after μή". |
| δεδμημένον · 119 | low | Homeric form, no Attic equivalent named. | "epic δεδμημένος (= Attic δεδαμασμένος)". |
| καταπρηνέσσ · 199 | low | Epic ending, Attic not named. | "epic -έσσι (= Attic -έσι), elided". |
| πεπλήγετο · 198 | low | "reduplicated aor." asserts a tense the form does not show (it has been read as an epic reduplicated imperfect or aorist). | "epic reduplicated past 3 sg. mid." |
| πρεσβύτατον · 142 | low | The superlative is written "πρέσβυτατος" (wrong accent). | "πρεσβύτατος". |
| τεύξειεν · 191 | low | "-ειεν ending (= Attic -ειε)" presents the movable ν as a dialect difference; -ειε(ν) is as common in Attic. | "with movable ν (τεύξειε)". |
| τιμήεις · 129 | low | Poetic adjective, Attic equivalent not named. | "poetic (Attic ἔντιμος)". |
| ἀριθμήσω · 215 | low | Parse stated flatly as a short-vowel subjunctive; the unit note (pass 1) hedges it with "could be read as a future"; pass 1 asked for the same hedge here. | "fut. indic. or short-vowel aor. subj. 1 sg., hortatory if subj.: ’I shall count / let me count’". |
| ἐϋζύγου · 116 | low | Meaning "well-benched" contradicts `l`/`i` "well-yoked" and the new-renderings row (which reserves "well-benched" for ἐύσσελμος). | "well-yoked, with good cross-benches (exact sense uncertain)". |
| ἴκελον · 157 | low | Epic adjective, Attic equivalent not named. | "(= Attic ὅμοιος)". |
| ὀδυσῆϊ · 126 | low | Attic form not named (only the double-σ epic variant). | "= Ὀδυσσῆϊ, Attic Ὀδυσσεῖ". |
| ὣ · 198 | low | Dual of the possessive stated without the hedge the unit note has ("taken as"). | "masc. acc. dual, taken so with μηρώ". |
| ῥαῖσαι · 151 | low | "(= Attic ῥαῖσαι)" names an equivalent identical to the form; empty. | Removed; "aor. inf. act., after ἐθέλω: ’to smash’". |
| θεῖναι · 156 | low | "used as an imperative/proposal": the infinitive depends on ἄριστα (note: "rest on δοκεῖ … ἄριστα"), it is not an imperative. | "explaining ἄριστα: ’(best) to make, to set up (a stone)’". |
| φαινέσκετο · 194 | low | Epic iterative, no Attic equivalent named. | "(= Attic ἐφαίνετο)". |
| ἔγρεσθαι · 124 | low | Epic 2nd aorist, Attic equivalent not named. | "epic (Attic ἐγερθῆναι)". |

### Changes made — `gloss.json` (`__broaden__`)

| Form · line | Sev. | What was wrong | What was done |
|---|---|---|---|
| χεῦε · 189 | medium | The added clause read "περὶ … χεῦε = περιέχευε" (augmented), while the unit note (pass 1) says tmesis for περίχευε; χεῦε is the unaugmented aorist, so the compound is unaugmented. | "= περίχευε ’poured round’". Old entry still contained whole. |
| λίνῳ · 118 (missing broadening) | medium | Existing entry: "flax, linen thread; … instrumental: ‘with thread’". Here λίνῳ is the linen cloth after σύν (dative of accompaniment), a sense the entry does not cover. | Broadened: old entry whole + " · also linen cloth, a sheet; dat. sg. after σύν: ’together with the linen cloth’". |
| βίῃ · 143 (missing broadening) | low | Existing entry: "dat. sg. used adverbially: ‘by force’". Here it is the thing yielded to after εἴκων. | Broadened with " · also dat. sg. with εἴκων, the thing yielded to: ’yielding to force’ (βίῃ καὶ κάρτεϊ εἴκων)". |
| τέ · 211 (missing broadening) | low | Existing entries cover ἦ τ’ (elided) and ὅ τε but not ἦ τέ before the enclitic μ’: "truly" (the note at 13.209 glosses it so). | Broadened with " · also in ἦ τέ, a strengthened affirmation: ’truly’ (ἦ τέ μ’ ἔφαντο ’who truly said’)". |

Checked and found correct (no change): all other novel entries (lemma, meaning, parse, Attic equivalent where one exists, ’ only, no line numbers, under 230 characters) and the remaining twelve original `__broaden__` additions (βάντες, τὰς, ὅπως, κελαινεφές, πομπῆς, ἔμεν, ἀμφικαλύψῃ, μεῖναι, γένηται, πάντα, ἔφαντο, σφέας), each of which contains the old entry whole. Pass 1's open question on ὣ, ἔξ, ἀριθμήσω and ἱερεύσομεν: ὣ and ἔξ and ἀριθμήσω answered above; ἱερεύσομεν already reads "fut. or short-vowel aor. subj." and is correct.

### Second read of `l` and `i` (no change needed)

Every unit's `l` was read against the Greek word by word and `i` against `l`; no error pass 1 introduced was found, and none it missed. Specific re-checks that stand: the shipped repeats (13.137, 139, 153, 166, 167, 170, 172, 174, 177, 200–202) are identical in `l` as the packet requires; 13.140–145 and 13.154–158 keep "earth-shaker", "cloud-gatherer", "dark-clouded one" and "of wide strength" as in the table and new-renderings; "take vengeance on" is kept for both τίσαιτο and τίνυται (row 1453); ἄστυ "town" and πόλις "city" are used consistently; the quotation marks (“ at 13.128, 140, 147, 154, 168, 172, 200 and ” at 138, 145, 152, 158, 169, 183, 216) and the seven `mark`s are right, and the eleven `p` flags fall on the eleven ¶ lines. The hand-scan of 13.213 is confirmed (see the finding above for the one overstatement in the note).

### Findings considered and refused (pass 2)

1. **κάτθεσαν (known entry "syncopated and unaugmented") against the unit note ("κατέθεσαν with the vowel of the middle syllable lost")**: both describe the same surface form (κατ’ + unaugmented θέσαν, or κατέθεσαν with ε lost); neither is false, and an existing entry may not be rewritten. Left.
2. **βάντες broadening "with ἐκ + gen., no tmesis"** (13.116): ἐκ νηὸς βάντες can also be read as tmesis ἐκ … βάντες = ἐκβάντες with νηός governed by the compound; the two readings give the same sense and the entry is a defensible choice. Left.
3. **τί at 13.216** ("μή τί μοι οἴχωνται … ἄγοντες"): the known entry lists the indefinite as an adjective after μή; here it is the substantive object of ἄγοντες ("anything"). Covered closely enough by the entry's general "neut. acc. sg." and not worth a broadening.
4. **ἄρ before πῃ at 13.207** (the known entry speaks of ἄρ’ elided and of ἄρ τε): ἄρ is the plain short form; no new reading.
5. **ἠλίβατοι, πάνορμοι, ἐΰζυγος, ὑπερμενής, ἀλλοειδής as dictionary meanings** that differ in wording from the house renderings ("towering", "all-mooring", "well-yoked", "of surpassing strength", "other-looking"): glossary entries are lexical, the unit carries the house rendering; only ἐΰζυγος contradicted it outright and was fixed.
6. **Length of the notes at 13.116, 122, 128, 136, 149, 172, 189, 209, 213** (above 110 words) and **13.153** (17 words): validator WARNs only, as in pass 1; each long note parses several forms, the short one repeats 13.139.
7. **ἕλωρ "prey, booty" in the glossary against "booty" avoided in the table**: the entry is lexical, `l`/`i` say "prey"; left.
8. **"flat of his hand" at 13.164 and 13.199**: pass-1 refused finding 3 re-examined; LSJ gives "with the flat of the hand" for χειρὶ καταπρηνεῖ, `l` is the literal "downturned"; kept.

### Still for the caller (unchanged from pass 1, not touched here)

The nine rows of `new-renderings.md` that pass 1 listed (ἐφορᾷ … τίνυται and τίσαιτο, νοήμων / πινυτός, bare ἐννοσίγαιος, ἔπεα πτερόεντ’ ἀγόρευον, ὑπερβασίη, ᾤμωξεν, ἄστυ, ῥῆγος) still need amending before the rows are copied into `conventions.md`; pass 2 found one further point: the ἐϋζύγου row ("well-yoked", "well-benched" avoided) now agrees with its glossary entry.
