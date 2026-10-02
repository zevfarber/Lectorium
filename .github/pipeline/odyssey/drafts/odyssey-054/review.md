# odyssey-054 review (two passes) — Odyssey 11.321–434

Reviewer, adversarial, two full passes over `units.json` (60 units) and `new-renderings.md`; `gloss.json` does not exist yet and was not read. `units.json` was edited in place by script (`l`, `i`, `n` only); a before/after comparison shows every unit's `t` identical, the same 60 units, and `title`, `titleEn`, `part`, `about` unchanged. No unit boundary was moved.

Checked and clean: `t` joined reproduces the packet's 114 lines (whitespace aside); every `ln` is the line the unit starts on; the 12 `p` flags equal Murray's paragraph starts (321, 326, 333, 336, 342, 347, 354, 362, 377, 385, 395, 404); `l` has the line division of `t` in all 60 units and no `i` has a `\n`; no ASCII apostrophe, backtick or double quote in `l`, `i` or `n`; no translator named; the seven units whose Greek is identical to a published unit (11.335, 347, 354, 362, 377, 395–396) repeat the published `l` and `i` exactly (the validator's check 6 emulated, 0 mismatches), and the repeated lines inside larger units (333, 343, 355 = 378, 370, 398, 405, 411) carry the published wording; the part cites no other part or line by number, so there was no cross-reference to a published part to verify, and the internal ones (332/352 μελήσει, 341/384 ἰότης, 372/389 πότμον ἐπέσπον, 372/388 …, 399–400/406–407, 409/324 ἔκτα, 424/427 κυνῶπις/κύντερον, 386/434 θηλυτερ-, 350/376 τλ-) were each looked up in the line. Scansion: the packet flags none; running `scan_hexameter.py` over the 114 lines gives only "spondaic fifth" at 327, 347, 361, 362, 365, 376, 417, 419, all ordinary, none UNRESOLVED, so no note needs a metre sentence.

## Quotation marks

- odyssey-053's last unit (11.318–320) is narration; no speech of any kind is open across the 053/054 boundary. This part opens (units 0–5) inside the outer speech of Odysseus that odyssey-039 opened at 9.2 (“, `mark` "Odysseus speaks") and that 040–053 leave unclosed; units 0–5 therefore carry no marks, correctly.
- Unit 6 (11.332) closes that outer speech with ” on the last unit of the speech, because 11.333–377 is the poet's own voice, not Odysseus's. The drafter then gives Arete (336–341), Echeneus (344–346), Alcinous (348–353, 363–376) and Odysseus (355–361) double marks, the marks of frame-level speech as in 031–038, and reopens the outer speech with “ at 11.378 (unit 35, `mark` "Odysseus answers again"), leaving it unclosed because it runs on into the tale. Inner speeches inside the reopened speech are single (‘ at 397 closed ’ at 403; ‘ at 405 left open at 434). I checked this against how the rest of the poem treats the same situation: there is no earlier frame interruption of the tale (040–053 have none; the Book 7 tale in 031–032 is uninterrupted), so this is new practice, but it is the only consistent one. Leaving the outer speech open through 333–377 would put narrator lines and frame speeches inside Odysseus's quotation, and single-quoting them would mark Arete, Echeneus and Alcinous as speaking inside his story. Accepted unchanged.
- Parity: 6 “ and 6 ” in each layer (opens at 336, 344, 348, 355, 363, 378; closes at 332, 341, 346, 353, 361, 376), so the validator's check 5 gives no WARN; the ” at 332 pairs with the “ of odyssey-039 and the “ at 378 is the one left open. `mark` stands on the first unit of every speech opened here (units 9, 14, 18, 23, 27, 35, 44, 48). For LOG.md: outer speech (opened 9.2) closed at 11.332 and reopened at 11.378, runs on into odyssey-055, as does Agamemnon's speech (opened 11.405, single marks).

Counts: 5 high, 7 medium, 18 low (30 findings acted on; every one is listed below).

## Changes

| Line · unit | Field | Severity | What was wrong | What done |
|---|---|---|---|---|
| 11.373 · units 31–32 | l, i, n (both units) | high | Unit 31's `t` is only νὺξ δ’ ἥδε μάλα μακρή, but its `l`, `i` and note all translated and discussed ἀθέσφατος, which is the first word of unit 32's `t`; unit 32's English then had no word for it. A reader tapping either unit saw a word translated in the wrong place (see the refused finding below for the cause) | The English follows the `t` as it stands: unit 31 is "And this night is very long," / "This night is very long," with a note on ἥδε, μάλα, μακρή and a pointer to the next word; unit 32 now opens "immense; and not yet is it time" / "immense, and it is not yet time to sleep in the hall; so tell me of marvellous deeds." and carries the ἀθέσφατος note (sense uncertain) with the θέσκελος note. **If the owner moves ἀθέσφατος· into unit 31's `t`, restore the old English to 31 and drop the first word of 32's `l` and `i`** |
| 11.324 · unit 1 | n | high | "ἔκτα … in its short athematic form, without augment": ἔκτα is ἔ-κτα and has the augment (the unaugmented form is κτᾶ; the thematic ἔκτανε is the longer form, as odyssey-005's note says) | "with the augment (the longer form is ἔκτανε)" |
| 11.354 · unit 22 | n | high | "προσέφη is ‘addressed’, an aorist without augment": προσέφη is πρός + ἔφη and carries the augment | "the aorist of πρόσφημι" (as in odyssey-031's note) |
| 11.382 · unit 37 | n | high | "κήδε’ … in apposition to τούτων": κήδεα is accusative and τούτων genitive; the apposition is to οἰκτρότερ’ ἄλλ’ (οἰκτρότερα ἄλλα), the object of ἀγορεύειν | "in apposition to οἰκτρότερ’ ἄλλ’" |
| 11.385 · unit 38 | n | high | "ἁγνή is ‘pure’ (the same word that describes Artemis)": Artemis appears at 324 with no epithet, so the cross-reference is false in this part and a claim about the rest of the poem that this part cannot show | parenthesis cut |
| 11.338 · unit 10 | l, i, n | medium | ξεῖνος … ἐμός rendered "a stranger … mine" / "my stranger". The table gives "guest-friend" for ξεῖνος of the host–guest bond (row 688), and the identical construction is shipped as "guest-friend" at 1.417 (ξεῖνος δ’ οὗτος ἐμός) and 8.208 (ξεῖνος γάρ μοι ὅδ’ ἐστί). Here the speaker is the host | `l` "And a guest-friend, moreover, mine he is, …"; `i` "Moreover he is my guest-friend, …"; note rewritten ("the guest-friend, the man bound to a host") |
| 11.353 · unit 21 | l, i, n | medium | δήμῳ rendered "among the people". The table fixes δῆμος as "land" in both layers (row 636, "people" being λαός); and `i` "it is I who hold power" added a cleft emphasis the Greek does not have | `l` "for of him the power is in the land"; `i` "for the power in the land is mine"; note says δῆμος is "land" in both layers and that the first person is the translation's |
| 11.409 · unit 49 | l, i, n | medium | θάνατόν τε μόρον τε rendered "death and portion" / "death and an allotted end". The same two nouns are table-fixed (row 675, 9.61) as "both death and doom" / "death and doom", and shipped so at 9.61 | `l` "having contrived for me both death and doom"; `i` "contrived death and doom for me"; note says μόρος is properly "portion" |
| 11.410 · unit 49 | l, i, n | medium | οὐλομένῃ ἀλόχῳ rendered "accursed". The table's φάρμακον οὐλόμενον is "the ruinous drug" (row 1027, shipped 10.394) and lists "accursed" among the avoided renderings of this participle | "ruinous" in both layers; note says the Greek has no "my" and that the word is a curse-word, "ruinous, accursed" |
| 11.324–325 · unit 1 | i | medium | Δίῃ ἐν ἀμφιρύτῃ: `i` "washed on every side by the sea", but the same adjective is shipped in `i` as "with the sea running all round it" at 1.50 and 1.198 (and the note at 1.198 says the phrase repeats 1.50) | "in Dia, with the sea running all round it" |
| 11.415 · unit 51 | l, i, n | medium | (a) εἰλαπίνῃ τεθαλυίῃ rendered "an abundant banquet": the participle τεθαλυῖα is shipped "flourishing" in both layers at 6.293 and 11.192 (the table notes it at row 549); "abundant" belongs to θάλεια / θαλερός. (b) ἔρανος rendered "contribution-feast" / "a shared feast": 1.226 ships "a meal of shared contributions" / "a meal where each man brings his share" | (a) "a flourishing banquet" in both layers; (b) the 3.226 wording in `l` and `i`; note rewritten |
| 11.375 · unit 33 | n | medium | Note gave ὅτε … τλαίης as "‘whenever you could bring yourself’" while `l` and `i` both say "if you …": the note contradicted its own translation | note now: "‘when you could bring yourself’ … ὅτε with the optative has here the force ‘if ever’", which is the `l`/`i` reading |
| 11.321 · unit 0 | l, i, n | low | "had no joy of her" is a stock English phrase that may be remembered rather than built from ἀπονίναμαι "have profit or enjoyment of" (LSJ) | "had no enjoyment of her" in `l`, `i`, `n`; note also trimmed from 122 to under 110 words |
| 11.328 · unit 3 | n | low | "μυθήσομαι and ὀνομήνω, which look like futures": only μυθήσομαι does | "μυθήσομαι, which looks like a future, and ὀνομήνω" |
| 11.330 · unit 4 | i | low | `l` "even the night", `i` "the night itself": force of καί lost | "for even the night, deathless though it is, would be spent …" |
| 11.332 · unit 6 | n | low | Did not say which speech the ” closes | "(opened at 9.2)" added |
| 11.335 · unit 8 | n | low | "her stock epithet": the part shows λευκώλενος once; "stock" claims recurrence | "her epithet here" |
| 11.344 · unit 14 | i | low | ἧμιν ("to us") is in `l` but dropped in `i` | "does not speak to us wide of the mark" |
| 11.346 · unit 16 | n | low | "would make the sentence a plain ‘both deed and word hang from Alcinous here’": "plain" is idle and confusing | "would give ‘both deed and word hang from Alcinous here’" |
| 11.350 · unit 19 | i | low | μάλα περ νόστοιο χατίζων ("much though in need of homecoming" in `l`) became "eager as he is for his homecoming": χατίζω is need/want, not eagerness | "much as he wants his homecoming" |
| 11.357 · unit 23 | n | low | "between the condition and what he would say to it": the clause after the pause is the main clause (καί κε τὸ βουλοίμην), not something he says | "between the condition and the clause that answers it" |
| 11.361 · unit 25 | i | low | ὅσοι … ἰδοίατο is an optative ("as many as might see me"); `i` had "who saw" | "who might see me come home" |
| 11.378 · unit 35 | n | low | Did not say that this unit's opening mark reopens the long speech | "its opening mark begins Odysseus’s long speech afresh" |
| 11.390 · unit 40 | n | low | "The order of the clauses shows that he knows Odysseus only after drinking": the order shows nothing; ἐπεί gives the cause | "The ἐπεί clause gives the cause: it is the blood that lets him know Odysseus." |
| 11.399 · unit 45 | n | low | "Ποσειδάων is the Ionic form": it is the epic form (Ionic is Ποσειδέων) | "the epic form" |
| 11.423 · unit 54 | n | low | Did not say which verb ποτὶ γαίῃ goes with, and `l` leaves it before ἀείρων | "ποτί … most likely goes with βάλλον" |
| 11.425 · unit 55 | i | low | "would not bring herself" (a volitional shift; ἔτλη is an aorist "did not bring herself") and "went down to the house of Hades" (a "down" the Greek does not have) | "did not bring herself, even as I went to the house of Hades" |
| 11.424 · unit 55 | n | low | "the standing reproach of shamelessness": "standing" claims recurrence beyond this part | "a reproach of shamelessness" |
| nine notes | n | low | Notes over the 110-word band (units 0, 27, 30, 37, 39, 49, 51, 55, 59: 114–123 words) | trimmed to 110 or under without losing a label (duplicated Greek-with-gloss pairs and the repeated line in `l` cut; units 37, 49, 51 also corrected as above) |
| `new-renderings.md` | rows | low | The rows were out of step with the units: ἀμφιρύτῃ, ξεῖνος, κράτος/δῆμος, ἔρανος/τεθαλυῖα, θάνατόν τε μόρον τε, οὐλομένῃ, μέλαινα (said "night" is "dark"; the table's `l` is "black night"), πομπή (332 is "my escort"; the two lines are not equal), ἔτλη, πρὶν γάρ | each row rewritten to the final wording and, where it clashed with the table, the draft's wording is recorded as avoided; one row added for ἀπόνητο; the οἰκτρός row notes that ἐλεεινός is also "pitiable" |

## Considered and refused

- **Move ἀθέσφατος· into unit 31's `t`.** The Greek is νὺξ δ’ ἥδε μάλα μακρή, ἀθέσφατος· (ano teleia after ἀθέσφατος); the drafter cut at the comma and left ἀθέσφατος· opening unit 32, so the cut breaks the punctuated-unit rule. Refused because the task forbids touching `t`; the English and notes were made faithful to the `t` as it stands (first row above). Recommendation: the owner moves the one word; the concatenation check is unaffected (non-space characters of `t` unchanged, as in the boundary moves logged for odyssey-051).
- **Reworking the quotation scheme** (leave the outer speech open and single-quote the frame speeches, or double-quote Odysseus's resumed speech without a `mark`). Refused; see the section above.
- **ὀλοφύραο "lamented"** against the shipped "pitied" for ὀλοφύρατο (4.364, 10.157): that is the construction with a person as object; with a thing as object (κεῖνα) "lament" is the sense. Kept.
- **γναμπτοῖσι μέλεσσι "pliant / supple limbs"** against the shipped "bent hooks" (4.369): "bent limbs" would read as crooked. Kept, noted here only.
- **οἰκτρός and ἐλεεινός both "pitiable".** Two Greek words, one English; "piteous" and "pitiful" are taken. Kept, with the table's cross-note added to the `new-renderings.md` row.
- **ἀμέγαρτον "a dreadful blast".** Picks a guess in `i`, but the note says the word is of uncertain sense and gives "unenviable" as the literal gloss, which is the house pattern for such words. Kept.
- **τοῦ γὰρ κράτος: a third-person reading** ("for he has power") in `i`. The drafter's reading of τοῦ as pointing back to ἐμοί is defensible and stated in the note; the first-person `i` stays, in the plainer form above.
- **ἐκ τοῦδε (346) "from here on"** against "from this man". Both readings are given in the note; `l` is neutral. Kept.
- **ἀλλά "so" (345 `i`).** "so do as she says" for ἀλλὰ πίθεσθε: the note gives "all the same, then". Kept.
- **ἔφην "I had supposed" (430).** A tense shift from "I said" in `l`, but the new-renderings row records the reason and "suppose" is allowed in `i`. Kept.
- **11.352 line reuse** of 1.358 ("all of them, and mine above all"): a different construction (the thing belongs to them, not is the care of them); the part's own wording stands.
- **κύδιστε "superlative of κυδρός", πρίν "the adverb", αὐτοῦ "the adverb", ἀπόνητο "aorist middle of ἀπονίναμαι", ἐκ … ἔχεται with the genitive, ἀγηγέραθ’ "pluperfect passive", ὀλοφύραο "optative"**: each checked against LSJ and Cunliffe and found true as labelled. Kept.
- **Ποσειδάων "the Ionic form" (unit 45).** The form is the epic one (Ionic is Ποσειδέων); the note's word was a label, so it is corrected in the table as a low finding rather than left.
- **Remembered English in `i`.** Scanned every `i`; the only phrase that arrived ready-made was "had no joy of her" (changed). "there is a time for many tales, and a time also for sleep" is forced by ὥρη μὲν … ὥρη δὲ, with "tales" built from μύθων; kept. "a time" vs "an hour" fixed in new-renderings.
- **Spondaic fifth feet** at eight lines: not irregular, no note.
- **Unit 5 "my companions", unit 6 "my escort"**: possessives supplied; the context is Odysseus's own, as the table does elsewhere; kept (new-renderings aligned).
- **Unit 27 `i` drops τὸ μέν "in this at least"**: the force is carried by the sentence; low, kept.

## Second pass

Re-read every edited unit against its `t`, then every unchanged unit once more for labels, then ran the mechanical checks again on the edited file (t identity, repeats, line counts, ASCII, quote parity 6/6 in both layers, note lengths all between 25 and 110 words). Nothing further found. Open for the glosser: ἀθέσφατος now sits in the unit that carries the translation; forms new in the edited English need no new gloss.

## Gloss pass

Reviewer second pass over `gloss.json`: every novel-form parse and the seven `__broaden__` entries checked against the Greek of the line where each occurs. Nine corrections to novel-form entries; the broadened entries are sound (each is the old entry whole plus ` · ` and a reading that this part shows; they run past 230 characters only because they carry the earlier readings).

| key | what was wrong | now |
|---|---|---|
| δόξης | "Ionic -ης (= Attic -ας)": δόξης is the ordinary Attic genitive too, so no dialect note applies | note dropped; ἀπὸ δόξης ’contrary to expectation’ added |
| εἰλαπίνῃ | "Ionic -ῃ (= Attic -ᾳ)": εἰλαπίνη is an η-stem in Attic as well | note dropped |
| ὑσμίνῃ | same error (ὑσμίνη is an η-stem) | note dropped |
| μαχεούμενον | called "uncontracted" with Attic equivalent μαχούμενον (that is the Attic future); the form is a contracted epic present participle | "epic -εούμενον (= Attic μαχόμενον)" |
| διδοῖτε | "you would give": the optative continues the εἰ-clause begun by ἀνώγοιτ’ | "you were to give" |
| ὀτρύνοιτε | "you would speed": same | "you were to speed" |
| τελέσω | "I shall complete" misses the construction (subjunctive after εἰς ὅ κε) | "until I have paid in full" |
| κρατερῇ | no Attic equivalent for the Ionic η after ρ | "Ionic -ῃ (= Attic -ᾳ)" |
| στυγερήν | same | "Ionic -ην (= Attic -άν)" |

Left unchanged after checking: all other case, tense, mood, person and number parses; the article-forms and possessive ὅς do not occur among the novel forms; the broadened ὅτ’, σέο, αὐτοῦ, λέγε, νόστοιο, ἐίσας, περίφρων entries cover the uses in this part (ὡς ὅτ’ ἀοιδός; σέο τ’ αὐτοῦ; both αὐτοῦ adverbs; λέγε θέσκελα; νόστοιο χατίζων; φρένας ἐίσας; Arete as περίφρων).

Note for the build: the working-tree `odyssey-glossary.json` already holds the nine old entries (the build ran before this pass); the corrected `gloss.json` needs a rebuild or the same nine entries patched there.
