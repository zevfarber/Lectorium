# odyssey-119 (24.438–548) — review

## Pass 1

Scope: `units.json` against `packet.md`, `conventions.md` (rules read in full, tables grepped), `new-renderings.md`, the pilot `drafts/odyssey-001/units.json`, the published parts (for repeated Greek) and `odyssey-118.json` (neighbouring part). `gloss.json` belongs to pass 2. `units.json` was edited in place by script; `t` is byte-identical before and after (checked by hash and unit-by-unit comparison). 76 units, 111 lines.

Severity scale used here. **high**: the unit would fail the gate (validator check 6, a repeated published unit must repeat its English exactly) or breaks a house rendering outright. **major**: a note says something false about the Greek or the text (grammatical label, cross-reference). **minor**: `l`/`i` fault in sense or force, house-rendering slip, repeated-line inconsistency, note gap or misleading wording. **nit**: polish.

### Changes

| Line · unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 449 · u8 | l, i | high | Same Greek as the published unit at odyssey-107 and odyssey-116 (`τοὶ δ’ ἀγχιστῖνοι ἔπιπτον.`). `l` was "and they fell one close upon another." against the table row ἀγχιστῖνοι (`l` "in close succession"), and a closing ” had been added, so the English differed from the shipped unit. The validator would fail it. | Set `l` = "and they, in close succession, fell." and `i` = "and they fell one close upon another." exactly as published. The closing ” is therefore not there. See "Open conflict" below. |
| 481 · u34 | l, i | high | Same Greek as the published unit at odyssey-077 (`ἔρξον ὅπως ἐθέλεις·`), whose English is lower-case "do as you wish;". The draft had "Do as you wish;", which the validator rejects. | Set both layers to "do as you wish;". |
| 502–503 · u49 | l | high | Same letters as the published unit at odyssey-108 (the validator ignores punctuation, so the missing comma after Ἀθήνη does not make it a new unit). `l` was "And near at hand to them came …"; published is "And to them near at hand came …". | `l` set to the published wording. `i` was already identical. |
| 441 · u2 | n | major | "τάφος, with the accent on the first syllable, is ‘amazement’, not τάφος ‘grave’". The accent does not distinguish the two words; both are accented τάφος. The false mark of difference is the error. | Rewritten: τάφος is ‘amazement’, a neuter noun unrelated to τάφος ‘grave’, though spelled alike (the table row τάφος 21.122 says the same without the accent claim). |
| 449 · u8 | n | major | "ἔπιπτον is an unaugmented imperfect". It has the augment (ἔ-); unaugmented would be πίπτον. | Now "the imperfect of πίπτω, with its augment (compare the unaugmented πῖπτε at 535)". |
| 472 · u28 | n | major | "προσηύδα is an unaugmented imperfect". The η- is the augment (unaugmented would be αὔδα). | "an imperfect, ‘spoke to’, with the augment η-". |
| 494 · u43 | n | major | Same false claim: "προσηύδα is the unaugmented ‘spoke to’". | "the imperfect ‘spoke to’, with the augment η-". |
| 533 · u67 | n | major | "εἷλεν is the unaugmented aorist of αἱρέω". εἷλεν is augmented; the unaugmented form is ἕλε (438, 441). | "the aorist of αἱρέω ‘seize’, with its augment (the unaugmented form is ἕλε, as at 438)". |
| 520 · u61 | n | major | "ὣς φάτο … is feminine here". φάτο has one form for either sex; the verb is not feminine. | "the verb has the same form whoever speaks, and here the speaker is Athena." |
| 546–548 · u75 | n | major | Cross-reference wrong: "the final lines repeat 502–503". Only 548 repeats a line (503); 547 is not 502, and 546 repeats nothing. (u49's note says it correctly.) | "the last line repeats 503, so that the poem ends …". |
| 475 · u30 | l | minor | "war, both evil, and fearsome battle-din": the "both" of τε … καὶ was attached to "evil", which misreads the Greek (πόλεμόν τε κακὸν καὶ φύλοπιν αἰνήν = both evil war and fearsome din). | "Will you farther both evil war and fearsome battle-din / work, …". |
| 462 · u20 | l | minor | `l` "lest anywhere someone …" while the note glosses μή πού τις as "lest perhaps someone" (πού here is ‘perhaps’); `l` and note disagreed. | `l` now "lest perhaps someone an evil drawn on himself find." |
| 460 · u17 | i | minor | "since they said he would never come back": "since" is not in the Greek (δέ) and "never" overstates οὐκέτι ‘no longer’. | "and they said he would never again come back." |
| 481 · u35 | i | minor | "what is fitting" for ὡς ἐπέοικεν; the force is ‘as is fitting’, and the table row for the same stem (ἐπιεικές, ὡς ἐπιεικές) fixes "as is fitting" and refuses variants. | "and I will tell you as is fitting." |
| 495 · u45 | i | minor | "at once" for θᾶσσον. The table row θᾶσσον fixes `i` "quickly" for the imperative use and names "at once" as refused (20.154). | "but let us arm ourselves quickly.” |
| 500 · u48 | i | minor | Line 500 = 467 (the note says "the same English"), but `i` began "And when" where u25 has "But when". | "But when they had put the flashing bronze about their bodies, …". |
| 500 · u48 | l | minor | "and went out, and led Odysseus" reads as Odysseus being led; Ὀδυσσεύς is the subject. | "… and went out, and Odysseus led." |
| 543 · u73 | l | minor | "cease from the quarrel": the note (correctly) has παῦε transitive with accusative νεῖκος, `i` "put an end to the quarrel"; "cease from" is intransitive and disagrees. | "hold yourself back, and stop the quarrel of even-handed war,". |
| 546 · u75 | l | minor | "between both sides" for μετ’ ἀμφοτέροισιν, where the same words at 476 (u30) are "among both sides" in `l`. | "among both sides set". |
| 546–548 · u75 | i | minor | "who had taken the shape of Mentor": the published wording for 503/548 is the participle "having taken the shape of Mentor, in body and in voice alike" (odyssey-007, -108). | "having taken the shape of Mentor". |
| 482 · u36 | n | minor | The note did not say who ταμόντες (nominative plural) refers to; a reader sees plural agents and a singular ὁ μέν. | Added: "ταμόντες is nominative plural, with the two sides as its unstated subject." The scansion sentence already in the note was kept (see below). |
| 454 · u13 | n | minor | "This line opens Medon’s speech too": this line opens Halitherses’ speech; it is 443 that opens Medon’s. | "Medon’s speech began with these same words (443), so that …". |
| 539 · u71 | n | minor | "κὰδ … ἔπεσε is κατέπεσε, with the preverb shortened and joined to the next word": κάδ is apocope with the τ assimilated to the following δ’, not "joined to the next word". | "with the preverb shortened (κατά becomes κάδ before the δ’ that follows)". |
| 467 · u25 | n | nit | "‘flashing, gleaming’ is the traditional guess": "gleaming" is reserved for γλαυκῶπις and refused for νώροπα in new-renderings.md. | "‘flashing’ is the traditional guess". |
| 469 · u26 | n | nit | "(literally ‘not speaking’, an infant)" states an uncertain etymology as fact. | "(traditionally explained as ‘not speaking’, that is an infant)". |

### Open conflict (for the caller)

Unit 8 (449) ends Medon’s speech, which opens with “ at u4. The Greek unit is identical to a published unit that has no ”, and validator check 6 requires identical `l` and `i`. I kept the gate-safe published English, so Medon’s speech has no closing ” in either layer. After the build the validator will print the WARN "12 opening and 11 closing quotation marks"; that is this unit, not a missed mark elsewhere (all other 11 speeches are opened and closed, in `l` and `i` alike). Options for the owner: accept the WARN and note it in LOG.md, or add ” and change the check so quote marks are ignored when comparing repeated units. I did not do either.

### Checks that found nothing to change

- **Note labels.** Every grammatical label was checked against its form and line, including every "unaugmented" (ἕλε, ἕλεν, ὅρα, γένοντο, πείθοντ’, φῆ, βῆ, κίεν, στῆ, πῖπτε, χαῖρε: all true), every "begins/ends mid-line after the ano teleia/question mark at X" (441, 481, 495, 514: true), and every cross-reference (466, 467, 450, 519, 443, 503/548, 535, 438: true after the fixes above).
- **Greek → `l`, case relations, tense, mood, particles.** All units read word by word; the only misreading was u30 (above). ἀπαμειβόμενος/προσέφη, ἔπεα πτερόεντα, δὴ τότ’ … προσέφη, ὃν φίλον υἱόν, πολύτλας δῖος Ὀδυσσεύς, γλαυκῶπις, ὀβριμοπάτρη, ψολόεις κεραυνός, ὁμοίιος πόλεμος, εὐρύχορος, εὐρύοπα, δολιχόσκιον, χλωρὸν δέος, ἐϋφρονέων ἀγορήσατο, κέκλυτε δὴ νῦν μευ and the new renderings (νώροπα, χαλκοπαρῄου, ὑψιπετήεις, σίτοιο μελίφρονος, ἀφροσύναι, ἀναγκαῖοι, ἀριστῆος) all agree with the table and new-renderings.md in both layers.
- **Repeated lines.** 451, 454, 477, 479–480, 510 are identical to the published units; 473, 490, 504, 542, 547, 548 appear inside longer units with the published wording (u49 and u75 now follow it too); 467 = 500 and 519 = 522 are consistent in both layers after the u48 fix.
- **Quotation marks and `mark`.** Twelve speeches (443, 454, 473, 478, 491, 495, 506, 511, 514, 517, 531, 542), each with `mark` on its first unit, “ on its first unit, ” on its last (except 449, above); `l` and `i` carry the same marks in every unit. Nothing runs on from odyssey-118, whose last unit (437) closes Eupeithes’ speech; nothing runs into a next part (the poem ends).
- **`p`, `ln`, `v`.** `p` is on exactly the units that start a Murray paragraph (20 paragraphs); `ln` is the line each unit starts on; `v` is true throughout; `l` has one `\n` per `\n` in `t`; `i` has none.
- **Scansion of 482** (`ἐπεὶ δὴ μνηστῆρας ἐτίσατο δῖος Ὀδυσσεύς`), scanned by hand: 15 syllables, so three dactyls. Feet: 1 ἐπεὶ (– –), 2 δὴ μνη- (– –), 3 -στῆ-ρας ἐ (– ⏑ ⏑), 4 τί-σα-το (– ⏑ ⏑; ι of τίνω/τίσις is long by nature), 5 δῖ-ος Ὀ- (– ⏑ ⏑), 6 -δυσ-σεύς (– ×). By nature ἐπεί is ⏑ – (ε short, ει long), which cannot fill the first foot; it fits only if the first syllable is lengthened. The line has no other irregularity, so the drafter’s note ("metrically irregular as transmitted: the first syllable of ἐπεί must be scanned long by metrical lengthening") is correct, is one plain sentence, and was left as it is. `scan_hexameter.py` gives the same scansion with the same single licence; its UNRESOLVED flag comes only from the unmarked quantity of the ι in ἐτίσατο. 483 (the other line of the unit) scans cleanly (correption in βασιλευέτω is the ordinary kind).
- **Remembered English.** Nothing found that is demonstrably recalled. Checked with suspicion and left: "clattered upon him" (literal ἐπ’ αὐτῷ + ἀράβησε), "fell upon the front-line fighters" (ἐν … ἔπεσον προμάχοις, the plain grammar; "front fighters" in `l` is the same calque), "are contending over excellence" (δῆριν ἔχουσιν), "pity took hold of" (οἶκτος … ἕλε). No source consulted; each rebuilds from the case relations and none is a house-table violation.

### Findings considered and refused

| Finding | Reason refused |
|---|---|
| u1 `i` "Close to them came" against table row ἀγχίμολον (14.410) `i` "close by" | The same word is already shipped at 24.502 with `i` "close to them" (odyssey-108), and the 14.410 row is for the unaccompanied adverb; the row also refuses "at hand", yet the published 24.502 `l` is "near at hand" and u49 must repeat it. Left; the two shipped usages are consistent with each other. |
| u7 `l` "an immortal god" against `i` "the immortal god" | Greek has no article; `i` uses "the" because the god is the one just named (ἄμβροτον … θεόν). Sense is the same. |
| u53 note "the fourth of the reply-formulas" as an unverifiable claim | The table row for τὴν/τὸν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα itself calls it "the fourth reply-formula"; the note follows the house numbering. |
| u10 note "the same formula introduces speakers elsewhere" as a claim beyond the part | Backed by the published 2.157 and 7.155/11.342 rows; the claim is true and is only the formula itself. |
| u60 `i` drops μάλα ("very") of αἶψα μάλ’ | "at once" carries αἶψα μάλα in the same way as the shipped parallel `i` for 522 in this unit; `l` keeps "very swiftly". Not a loss of force worth a change. |
| u52 `i` "you will learn" for εἴσεαι (‘you will know’) | After ἐπελθών the future of οἶδα is ‘you will come to know’; "learn … now that you have come to it" is the sense. |
| u27 `l` "but he was not then destined … but there his doom" (two "but") | οὐδ’ ἄρ’ is ‘and not then’; `l` is stiff but not wrong, and `i` is correct. |
| u46 `i` "four with Odysseus" for ἀμφ’ Ὀδυσῆ’ | "with" is a fair reading of ἀμφί here; `l` keeps "around". |
| u46 note calls οἱ the "article-form" (not "pronoun") | The conventions say the "article" is a pronoun, but the note says "article-form" for ἓξ δ’ υἱεῖς οἱ Δολίοιο, where the word is the article in its later use; no reader is misled. |
| u73 `i` "hold yourself back" against table row ἴσχεο (24.323) "keep yourself from" | That row has a genitive object ("from weeping"); here ἴσχεο stands alone, and the ἴσχεο row at 11.251 ("restrain yourself") shows the stem is rendered by context. |
| u64 ἀμφιγύοισι "double-pointed" not in new-renderings.md | The note already says the meaning is not well understood. This is the last part of the poem, so the rendering cannot recur; a table row would serve no later part. |
| u36 `i` "let faithful oaths be sworn" (passive for the plural agent ταμόντες) | The agent is unstated in the Greek too and is now named in the note; the English is clear. |
| u18 note that the wish of γένοιτο is for the Ithacans to do what Halitherses asks | A plausible reading, not a claim about the poem beyond this part; the alternative (‘so may it be’ with the speech’s whole thrust) points the same way. |
| u40 `l` "whether" against note "lest" | `l` follows the surface word order; the note explains the construction. They do not contradict. |
| u58 note "The Greek does not say who the rivals are" against `i` "My son and my grandson" | The Greek says only ‘son and grandson’; the possessives are English, and the note says so. |
| u14 κακότητι "wickedness" against table row κακότητα φυγόντες (23.238, "misfortune") | The note states the moral sense here and the other senses; the row’s refusal of "wickedness" is for the other sense. |
| new-renderings.md rows | All seven agree with `units.json` in both layers and with the neighbouring table rows; the νώροπα "gleaming" refusal is now also followed in the note (u25). |

### Counts (pass 1)

| Severity | Count |
|---|---|
| high | 3 |
| major | 7 |
| minor | 13 |
| nit | 2 |
| **total changes** | **25** |

Findings considered and refused: 17. One open conflict (u8 closing ”, above).

## Pass 2

Scope: a fresh full read of `units.json` (all 76 units: `t` against the packet, `l` word by word, `l` ↔ `i`, notes, quotation marks, `mark`, `p`, `ln`, line counts, ASCII quotes), then every entry of `gloss.json` (93 new forms, 19 broadened keys before this pass) checked against each line where the form occurs, and the 427 known-form entries read against this part’s uses. `t` is untouched (hash of all `t` identical before and after). Afterwards a scratch copy of the repository was built and validated: `BUILT`, then `PASS` with only the expected quotation WARN (12 opening, 11 closing; unit at 449, left as instructed). Nothing was built in the real tree.

### Changes

| Line · field | Severity | What was wrong | What was done |
|---|---|---|---|
| gloss `ἔδυνον` (498) | major | Parse said "unaugmented". ἔδυνον has the augment ἐ-. | Now "impf. 3 pl. act., augmented". |
| 528 · n | major | "ἤϋσεν is the aorist of ἀϋτέω". ἤϋσεν belongs to ἀΰω (gloss lemma); ἀϋτέω would give ἀΰτησε. | Lemma corrected to ἀΰω. |
| gloss `προΐει` (broaden) | major | Entry covered only the impf. 3 sg. (522). At 519 προΐει is the present imperative 2 sg. (‘let fly!’), as the note of that unit says, so the reader was given a false parse there. | Broadened: old entry whole, plus the imperative reading. |
| 460 · n | minor | "φάντο is the aorist middle of φημί": the glossary (φάτο, ἔφαντο) and gloss.json give the impf. mid.; note and gloss disagreed. | Note now "unaugmented imperfect middle of φημί (= ἔφαντο)". Gloss kept. |
| 524 · n and gloss `ἔρυτο` | minor | Both said "aorist middle … (= ἐρρύσατο)". The glossary’s house parse for the same stem (εἴρυτο) is impf. mid. of ἐρύομαι (Attic ἐρρύετο). | Gloss: "impf. 3 sg. mid., epic (= Attic ἐρρύετο); an aorist sense (= ἐρρύσατο) is possible". Note: "epic past middle … (an imperfect in form, with an aorist sense)". |
| gloss `ἀλεὶς` (538) | minor | "(ἀλίζω)" is a different verb; the Attic equivalent was missing (ἁλείς). | "εἴλω (εἰλέω) — press together, huddle; aor. 2 pass. part. …, epic ἀλείς (= Attic ἁλείς)". |
| gloss `νώροπα` | minor | Meaning "flashing, gleaming": "gleaming" is refused for νώροψ in new-renderings.md. | "flashing (meaning not known; traditional gloss)". |
| gloss `μελίφρονος` | minor | "heart-warming" against the house rendering "heart-sweetening" (new-renderings.md; note of 489). | "honey-hearted, heart-sweetening (sense uncertain)". |
| gloss `χαλκοπαρῄου` | minor | "epic -ου": the genitive in -ου is the ordinary one, not an epic form (the epic would be -οιο). | "fem. gen. sg. (two-ending adj.), agreeing with κόρυθος". |
| 521 · n | minor | "The second line repeats 519, and has the same English": the English differs (519 imperative "let fly your", 522 past "he let fly the"). | Says the wording is the same except that προΐει is an imperative there and a past tense here. |
| 456 · i | minor | "you would not obey me" makes a refusal of will; οὐ … πείθεσθ’ is a plain imperfect, as the note and `l` say. | "for you did not obey me". |
| gloss `οὐ` (broaden) | minor | 479 οὐ γὰρ δὴ … ; is a question expecting ‘yes’ (the note says so); the existing entry for the unaccented key is only "not". | Broadened with that reading. |
| gloss `ἔθηκαν` (broaden) | minor | The gloss for ἀνόστους says "predicate after ἔθηκαν", but ἔθηκαν had only "put, place, set". | Broadened with "made (them so), + predicate acc.". |
| 542 · n | nit | κεχολώσεται called "a future indicative"; the form is the future perfect (the glossary says fut. perf.). | "the future perfect κεχολώσεται". |
| gloss `φίλταθ` | nit | "syncopated φίλταθε" is not what the form is. | "epic φίλταθε (= Attic φίλτατε), elided". |
| gloss `ἅδε` | nit | "aor. 2" alone is opaque, and the augment question is the reader’s first. | "aor. 3 sg. act. (stem ἁδ-), unaugmented". |
| gloss `οἴμησεν` | nit | Voice missing. | "aor. 3 sg. act." |
| 517 · n | nit | Note "swing back" against gloss "swing up" for ἀμπεπαλών. | Note aligned to "swing up, brandish". |
| 498 · n | nit | "ἐν δ’ ἄρα is ‘and in addition’" against `l` "And among them". | "‘and among them’". |

### The glosser’s flagged forms

- οἴμησεν (οἰμάω): kept. A rare epic aorist ‘darted, swooped’, 3 sg. with ν-movable before δέ; the note and `l`/`i` agree with it. Only the voice was added.
- ἅδε: kept as aorist of ἁνδάνω (stem ἁδ-), unaugmented, with the dative σφιν; the glossary has only the augmented impf. ἥνδανε, so there is no clash.
- ἔρυτο: corrected to the house parse (see above); the Attic equivalent given is ἐρρύετο, with ἐρρύσατο as the alternative.
- ἀλεὶς: parse true (aor. 2 pass. part. of εἴλω); lemma and Attic form fixed (above).
- ἕσσαντο = Attic ἡμφιέσαντο: true (ἀμφιέννυμι, mid. ἡμφιεσάμην). Kept.
- ἔσχεθε: kept as "aor. 3 sg. … epic by-form", the same convention as the glossary’s ἔσχεθεν and ἔσχεθον.

### Checks that found nothing to change (pass 2)

- All 93 novel forms were read against every occurrence; every other parse is true of the form in its line (cases, tense, mood, voice, agreement, Attic equivalents). The remaining 19 broadened entries each begin with the old entry whole and add readings that occur in this part (checked by script); the build’s containment, length (<230), ASCII-quote and "no extra form" tests pass.
- The known-form entries were read against this part. Covered as they stand: ὅ σφιν (453), μή in all four constructions, κεν (454, 528), τὸ πάρος, περὶ χροῒ, ὅπως ἐθέλεις, τί (473, 478), διὰ + gen., βάλεν ‘struck’, ἐν δ’ ἄρα, οἱ Δολίοιο (497), ἦ τοι, ἦ … ἦ, ἐπὶ + acc./dat.
- `units.json`: every `l` has the same number of lines as its `t`; no ASCII quotes; `l` and `i` carry the same “ ” in every unit; 12 speeches, `mark` on the first unit of each, ” on the last of eleven. Repeated lines (451, 454, 473, 477, 479–480, 490, 502–503, 504, 510, 542, 547–548) follow the published wording; 467 = 500 and 519 = 522 consistent.

### Findings considered and refused (pass 2)

| Finding | Reason refused |
|---|---|
| Missing closing ” at 449 | Intentional (identical to a published unit; validator requires identical English). The WARN is expected. |
| Notes that start mid-line (443, 452, 485, 514…) do not say so | Only a claim about where a word stands must be checked; none is made. Adding it is not required by the conventions. |
| πείθεσθ’ (456) could be present indicative, not imperfect | The context is past (γένοντο, the aorist) and the wish to stop the sons is over; imperfect is right. |
| ἡμεῖς (484) = the gods | Zeus and Athena; supported by the shape of the speech. The note says it. |
| ταμόντες with "the two sides" as subject | An interpretation, flagged as unstated in the Greek; leave. |
| u1 "ἕλε", 441 "ἕλεν", 533 "εἷλεν" augment labels | All true (ἕλε/ἕλεν unaugmented; εἷλεν augmented). |
| 497 οἱ as "article-form" | Correct for ‘the sons of Dolius’; known entry covers it. |
| 454, 510, 542 repeated lines | Equal to the published wording. |
| 6 `i` "it was not against the will … that Odysseus devised" | A cleft that keeps the negation on ἀέκητι θεῶν, as the Greek does. |
| 55 `i` "I do nothing to shame your line" for οὔ τι καταισχύνοντα | Fair rendering of the participle after ὄψεαι; `l` keeps the literal. |
| ἔσχεθε as impf. of σχέθω | The glossary’s existing ἔσχεθεν/ἔσχεθον use "aor.… by-form", and a differing label for one form would be inconsistent. |

### Counts (pass 2)

| Severity | Count |
|---|---|
| high | 0 |
| major | 3 |
| minor | 10 |
| nit | 6 |
| **total changes** | **19** (12 in `gloss.json`, of which 3 are new `__broaden__` keys, now 22 in all; 7 in `units.json`) |

Findings considered and refused: 11. Open item unchanged: the missing ” at 449 and the resulting WARN.
