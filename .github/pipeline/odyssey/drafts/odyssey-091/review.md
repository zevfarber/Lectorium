# Review — odyssey-091 (Odyssey 18.320–428), pass 1

Reviewer pass 1 of 2 (units.json only; gloss.json is checked in pass 2). Files read: conventions.md in full, runbook.md section 2, packet.md, units.json, new-renderings.md. `t` was not touched (the check script confirms every `t` is byte-identical before and after, and that the `t` pieces joined reproduce the packet lines, including the added · at 18.405). No `tr` or `sc` written. Edits were made by script (`json.dumps(..., ensure_ascii=False, indent=1)`, which reproduces the original file layout exactly); each replacement asserted a single match.

Method: (1) every grammatical label and every claim about position or cross-reference in every note checked against the line; (2) Greek to `l` word by word; (3) `l` against `i`; (4) remembered English; (5) quotation marks, `mark`, `p`, `ln`; (6) the table in conventions.md, row by row for every rendering in the part; (7) repeated lines against the packet.

Totals: 21 findings, 27 field edits. High 0 · Medium 5 · Low 16. Refused: 14.

Severity scale: High = wrong Greek, wrong sense, or a quotation/structure error that would ship. Medium = a false or contradictory note, a table violation, or an `i` that misleads. Low = precision, house style, or a small drift between `l`, `i` and the note.

## Changes made

| Line · field | Sev. | What was wrong | What was done |
|---|---|---|---|
| 351 · n | Medium | Note called κέκλυτε "a perfect imperative with present sense". It is the reduplicated aorist imperative of κλύω (as the published notes at odyssey-005, -031, -033, -047, -086 say). | Now "a reduplicated aorist imperative of κλύω, 'hear'". |
| 353 · n | Medium | Note glossed ἀθεεί as "'not without a god'" and then said οὐκ ἀθεεί was a double negative. If ἀθεεί already meant "not without", οὐκ ἀθεεί would be a triple negative; the note contradicted itself. | ἀθεεί is "'without a god' (ἀ- 'without' …)", οὐκ ἀθεεί "a double negative, 'not without a god', that is 'with a god’s help'". |
| 343 · n | Medium | The note's lead said Odysseus stands "with every eye on him", which is the passive reading of ὁρώμενος, but `l` ("toward all looking") and `i` ("looked at them all") take the active reading, and the note's own last sentence adopts the active one. The note contradicted its own `l`/`i`. Also "gives the hall its light" claimed more than φαείνων says. | Lead rewritten to "Odysseus stays where he is, in the light, and looks at them all." The closing sentence, which leaves the passive reading open, stands. |
| 368 · l, i, n | Medium | Table: κνέφας (9.168) is "darkness" in both layers, "dusk" is listed as avoided. `l` had "until very dusk", `i` "until deep dusk", the note "'right up until dusk' (κνέφας, 'darkness')". | `l` "fasting, right up to darkness,"; `i` "fasting until deep darkness,"; note "'right up until darkness' (κνέφας)". |
| 406 · i | Medium | "you can no longer keep eating and drinking in your hearts" reads as "continue to eat and drink", the opposite of `l` ("no longer keep hidden in your heart eating or drinking"). | "and can no longer keep food and drink hidden in your hearts", matching `l` and the note's "stays close to the words". |
| 406 · l, n | Low | Table row δαιμόνιε (10.472) fixes "Strange man" in both layers; the plural vocative in `l` was "Strange ones" (and so in the note), while `i` had "Strange men". | `l` and note now "Strange men", agreeing with `i` and with the singular row. |
| 321 · n | Low | "Melantho, the first to abuse Odysseus" can be read as a claim about the whole poem (Irus and Antinous have already abused him); the part shows only that she is first in this scene. | "who is the first in this scene to abuse Odysseus". |
| 327 · i | Low | "you must be someone knocked out of his wits": "must be" adds an inference that σύ γέ τις … ἐσσί (a flat assertion) does not carry, and `l` says "you, indeed, are". "here you stay and speak" added "stay", which ἐνθάδε … ἀγορεύεις does not say. | "you are someone knocked out of his wits … but here you speak at length". |
| 330 · n | Low | "Eurymachus will say these words again, almost exactly, at 390–393": lines 390–393 are word for word 330–333, and the note at 389 says so. | "word for word". |
| 331 · i and 391 · i | Low | `l` "Surely wine has hold of your wits, or else …" but `i` "Either wine has hold …" dropped the force of ἦ ῥά. The two units are the same Greek, so both were changed alike. | Both `i` now "Surely wine has hold of your wits, or else your mind is always like this;". |
| 338 · l | Low | οἷ’ ἀγορεύεις is the same half-line at 338 and 389; `l` had "what things you say" at 338 and "such things as you say" at 389, and the note at 389 says "the same words as at 338". | 338 `l` now "such things as you say" (as at 389 and as in both notes). `i` stays different in the two places because the clauses differ (object of "tell" against cause of the threat). |
| 338 · mark | Low | House form for a reply is "X answers" (Athena answers, Odysseus answers, Eurymachus answers); "Odysseus replies" is not used anywhere in the shipped parts. | "Odysseus answers". |
| 344 · i | Low | "did not remain unfulfilled" implies they stayed unfulfilled for a time; οὐκ ἀτέλεστα γένοντο is "did not turn out unfulfilled". | "did not go unfulfilled". |
| 350 · i | Low | "trying to raise a laugh": ἔτευχε is a plain imperfect, not conative. | "and raising a laugh among his companions." |
| 357 · n | Low | "making it a courteous proposal" sits oddly beside the note's own first sentence (the offer is a taunt). | "a polite-sounding proposal". |
| 371 · l, i, n | Low | οὐκ ἀλαπαδνόν: `l` "weak" and `i` "feeble" both collide with the table ("weak" reserved for ἠπεδανός / ἀνάλκις in the ἄκικυς row; "feeble" is the ἄκικυς rendering and is listed as avoided for ἠπεδανός and ἀβληχρός). "Frail" appears nowhere in the table. | `l` and `i` "not frail", note "'not frail'". Not entered in new-renderings.md (see refusals). |
| 381 · i | Low | "But in truth you are very insolent": "in truth" translates nothing; `l` has "But", the note says ἀλλά is "but as it is". | "But as it is, you are very insolent". |
| 381 · n | Low | The note glossed ἀπηνής "'unkind, unfeeling'"; "unfeeling" is a rendering the table turned down (ἀναιδής row), and new-renderings.md lists it as avoided for ἀπηνής. | "'unkind'". |
| 382 · i | Low | "with a few men, and none of them good": "a few" is "some", but παύροισι is "few" in the sense of scant; "none of them good" is stronger than οὐκ ἀγαθοῖσιν. | "with few men, and those not good". |
| 414 · i | Low | ῥηθέντι δικαίῳ: `l` "a just thing said", the table keeps "just"/"unjust" for δίκαιος (ἄγριοι οὐδὲ δίκαιοι row), `i` had "fair remark". | "a just remark". |
| 420 · n | Low | Note's first gloss "'for Telemachus to care for'" made Telemachus the agent, against its own second clause ("be a care, with the dative of the person who has the care") and against `l` / `i` ("to be a care", "to be Telemachus’ concern"). | "'to be a care to Telemachus'". |

## Second pass over my own edits

Re-read every edited field after the script ran. Checks: `t` unchanged in all 68 units; `\n` count of `l` equals that of `t` in every unit; no `\n` in any `i`; no backtick; no ASCII apostrophe in `l`/`i`; every note has an even count of single quotes; “ and ” balance (each speech opens on its first unit and closes on its last: 327–336, 338–339, 351–355, 357–364, 366–386, 389–393, 401–404, 406–409, 414–421, with “ only in the first unit and ” only in the last); 331/391 `l` and `i` identical, 332/392 identical, 333/393 identical except the closing ”; 338 and 389 now share "such things as you say". One polish found and made in the second pass: the new lead of the 343 note repeated its own φαείνων clause, so the sentence "φαείνων says that he is the one giving light" was dropped (the gloss that follows already says it). Nothing else needed changing.

## Checked and found sound (no change)

- Quotation marks and `mark`: every speech has `mark` on its first unit (327, 338, 351, 357, 366, 389, 401, 406, 414). Part 090 ends at 18.319 with the closing ” on Odysseus' speech, so no opening mark is owed at 320. No speech runs past 428 (the last one closes at 421).
- `p`: true on exactly the fifteen ¶ lines of the packet (320, 327, 337, 340, 346, 351, 356, 365, 387, 389, 394, 401, 410, 414, 422); `ln` of every unit, including the mid-line starts (344, 394, 425), matches the packet lines.
- Repeated lines against the packet: 18.351/352 (`l` and `i` identical to the published pieces), 365 (identical, whole unit), 384 (first `l` line and `i` identical), 388 (identical with Eurymachus for Antinous), 399 and 400 (published wording reused as far as the sentence allows), 405 (whole unit identical), 410 (identical), 412/413 (reused), 417 (second `l` line and the tail of `i` identical), 427 (first `l` line and the start of `i` identical), 349 (reused). 18.349's own unit runs on into 350, so exact identity is not required there; the reused wording is in place.
- Scansion: the packet flags no line; nothing to scan and no note sentence added.
- Table: ὣς ἔφαθ’, ἐνένιπε/ἐνένιπεν, ὑπόδρα (new row), μεταμώνια, θυμαλγής, εὐκαμπής, αἴθων, οἰνοχόος, Μούλιος ἥρως, ἑαδότα μῦθον ἔειπε, βάν ῥ’ ἴμεναι κείοντες ἑὰ πρὸς δώμαθ’ ἕκαστος all match new-renderings.md. Also checked against existing rows: ἀγήνορες, ἀγακλειτῆς βασιλείης, πολύμητις, ἀπαμειβόμενος προσέφη, ὣς ἄρα φωνήσας, ἦ ῥα, πτολίπορθος, ἐπηετανός, ἀθύρματα, λαμπτῆρες, ἀπηνής, ὕβρις, κραταιός, πρόθυρον, ἐπισταδόν, μελιηδής, δέπας, ἐπαρξάμενοι, δεῖπνον / δόρπον (not used), κρητήρ, δμῶες, στυφελίζω, καθαπτόμενος.
- Remembered English: no phrase in `i` arrives as a stock of any modern translation that I could trace to a rebuilt-from-grammar failure; "you must be" (327) was removed on grammatical grounds above.
- Cross-references in notes verified: 330 → 390–393; 338 → 389; 366–386 chain (366–370 reaping, 371–374 ploughing, 376–378 war, 375/379–380 results); 364 (belly); 394 stool in the 396 note; 389 → 330–333; 393 → 333; 401 wish in the 402 note; 337 scowl in the 387 note.

## Findings considered and refused

1. **18.327 `l`/`i`, "Stranger, sorry soul" / "you sorry creature"**: it is the logged new rendering; the note's "pitying or contemptuous 'wretch', here the second" is consistent with it. Kept.
2. **18.331 / 391, ἦ ῥά as a question**: the edition prints · (not ;), unlike 333 where the note explains ἦ as a question. Treating 331 as a statement ("Surely … or else") is right; kept.
3. **18.334 `i`, "Take care that … does not soon rise up"**: a free but faithful rendering of μή + subjunctive as warning (the note says "fear or a warning"). Kept.
4. **18.354 αὐτοῦ**: `l` "his own", `i` "his very", note "'his'". All three are within the sense of αὐτοῦ κὰκ κεφαλῆς; kept.
5. **18.357 `i` "you would be sure of a wage"** for μισθὸς … ἄρκιος ἔσται (future indicative in a parenthesis): the conditional is natural in the surrounding "would you be willing … if I took you on"; `l` keeps the future. Kept.
6. **18.368 `i` "with a finely curved sickle for me, and one just like it for you"**: free for ἔχοιμι / ἔχοις, but the sense is exact and the table row for εὐκαμπής is respected. Kept.
7. **18.371 ἰσοφόροι**, `l` "equally-bearing" / `i` "evenly matched in pulling": the sense of the compound is explained in the note; kept.
8. **18.384–386 `l`, "for you" twice (τοι … φεύγοντι)**: deliberate, mirrors both datives; the published first line and the `i` are reused as required. Kept.
9. **18.397 `l` "clanged" against the note's "'resound, boom'"**: `l` chooses a rendering within the gloss; no contradiction. Kept.
10. **18.407 `i` "must be stirring you up"** for νύ τις: the note glosses νύ "'then, I suppose'" and `l` has "I think"; "must be" is an acceptable inference-marker in English. Kept.
11. **Descriptive `mark` verbs ("Melantho abuses Odysseus", "Eurymachus taunts Odysseus", "Eurymachus threatens Odysseus", "A suitor complains", "Telemachus rebukes the suitors")**: the convention gives "X speaks" / "X answers" as examples; shipped parts already use "Eumaeus prays", "Odysseus cries out to the gods", "Odysseus asks". Kept (only "replies" was normalised).
12. **18.422 note, ἔειπε "with the ε doubled for the metre"**: a simplification (the double ε is the augment with the old digamma) but not false in what the reader sees; kept, as a harmless school-gloss.
13. **οὐκ ἀλαπαδνόν, λέσχη, αἱμασιά, χαλκήϊος, ἄρκιος and other once-only words**: none is a formula or epithet that will recur, so none needs a row in new-renderings.md; "frail" (371) is a plain word chosen only to stay clear of the table's reservations. If the owner wants a row, the entry would be οὐκ ἀλαπαδνόν "not frail" / "not frail", avoided "weak", "feeble".
14. **18.326 note, ῥ’ "a particle of emphasis"**: ῥα (= ἄρα) is rendered "then" in `l` and the same note at 337 glosses ἄρ’ as "then"; the vaguer word "emphasis" does no harm. Kept.

## Left for pass 2

gloss.json (not touched; the glosser is writing it concurrently). In pass 2: every parse against the line, including whether κέκλυτε, ἀθεεί, ἀλαπαδνόν, ἠβαιαί, κνέφαος, σφέλας, μεταμώνια are entered as the notes now say, and the `__broaden__` entries against the readings in this part.

---

# Pass 2 — gloss.json against units.json

Checked: all 129 novel entries and the 12 glosser `__broaden__` entries against the line(s) where each form stands; every known form of the part (416 in known-forms.json, including the long ones — αὐτοῦ, κέ, μή, τι, τις, τοι, ὁ/τό forms, ἐπί, κατά, πρός, εἰ, ἄν, ὄφρα, ὅτε — and the elided ones: δ’, θ’, κ’, τ’, ἐπ’, μετ’, ἄρ’, ῥ’, ἀλλ’, οὐδ’, δώμαθ’/δώματ’, μάλ’, σ’, μ’, γ’, κεῖσ’, πόλλ’, κάκ’, δείλ’, οἷ’, ἄγετ’, ἄλλοθ’, ὄφρ’) for whether the existing entry covers the reading used. The 12 glosser broadenings were each confirmed to be the old shipped entry whole, then " · " and one new reading, and each new reading is correct for its line (εὐρέα, δώματος, καλλιπάρῃος, λέγων, γένοιτο, ποίῃ, χαλεπαίνοι, ἄν, ἄρ, ἐπ, ἐπὶ, ὁππότε). The novel key set equals novel-forms.json. All novel entries are under 230 characters, use only ’ and contain no line numbers or "here". Items from my "Left for pass 2" list: κέκλυτε and ἀθεεί are glossed as the notes now say (the shipped κέκλυτέ entry says reduplicated aorist imperative; ἀθεεί "without a god"); ἀλαπαδνόν, ἠβαιαί, κνέφαος, σφέλας are sound as they stand (ἀλαπαδνόν "feeble, weak" is a dictionary sense, not a rendering, so the "frail" change in the notes does not touch it; κνέφαος "darkness, dusk, evening gloom" is a gloss). Totals for pass 2: 2 medium, 13 low (15 findings); 16 gloss.json entries changed (10 novel, 6 new broadenings); 1 units.json unit changed (3 fields); 4 findings refused.

## Changes

| Where | Sev. | What was wrong | What was done |
|---|---|---|---|
| 375 · l, i, n (units.json) | Medium | Missed in pass 1. ὦλκα is the accusative singular of ὦλξ "furrow" (glosser had it right), and διηνεκέα agrees with it as an accusative singular (epic -έα). My pass-1 reading, and the draft, took both as plurals ("unbroken furrows"). The glosser's διηνεκέα entry ("neut. acc. pl.") disagreed with its own ὦλκα entry. | `l` "an unbroken furrow", `i` "an unbroken furrow from one end to the other", note "ὦλκα is the accusative singular of ὦλξ 'furrow', and διηνεκέα, agreeing with it, means …". The διηνεκέα entry corrected to "masc./fem. acc. sg., epic -έα (= Attic -ῆ)". |
| δύη · `__broaden__` | Medium (a missing reading) | Shipped δύη is only the noun "woe". At the line it is the aorist subjunctive of δύω (ὄφρ’ … δύη ἄχος κραδίην); the note says so. | Added · "also δύω — sink into, enter; aor. subj. 3 sg., with acc.: …". |
| ἐόντα · `__broaden__` | Low | Shipped entry is accusative singular; here ἐόντα is neuter nominative plural agreeing with θύρετρα. | Added the nominative-plural reading. |
| ὃ · `__broaden__` | Low | Neither of the shipped readings covers ὃ καὶ μεταμώνια βάζεις (neuter relative as a connective, "which is why"). | Added. |
| μή · `__broaden__` | Low | Shipped entry has "lest" only after a primary verb; μή τίς τοι … ἀναστῇ stands alone as a warning. | Added. |
| εἶεν · `__broaden__` | Low | Only a concessive condition was listed; here a plain condition (εἰ … βόες εἶεν). | Added. |
| πὰρ · `__broaden__` | Low | Dative sense listed only as "beside" of place; οὕνεκα πὰρ παύροισι is "among". | Added. |
| διεπτοίησε | Low | Entry garbled its own parse ("= διαπτοιεῖν, aor. διεπτόησε"). | "augment inside the compound (δι-ε-πτοίησε)". |
| δολίος | Low | "a servant of Penelope’s household" claims what the part does not show. | "Dolius, father of Melantho". |
| κεύθετε | Low | "’keep down in the heart’, i.e. contain" chose one reading the note leaves open. | General: "hide, keep hidden, hold within; pres. 2 pl." |
| μετέθηκε | Low | "set in motion" is not a sense of μετατίθημι. | "place among, transfer; aor. 3 sg., augmented". |
| ἀντιβίοις, ὀνειδείοις | Low | "epic -οις (= Attic -οις)" says nothing; the forms are not epic variants. | Remark removed. |
| ἐκπέμψῃσι | Low | Entry tied the form to a μή clause; it stands in a relative clause (ὅς τίς … ἐκπέμψῃσι). | "in a general relative clause: ’who may send out’". |
| ἑαδότα | Low | "(= Attic ᾑδηκότα)" is not an attested Attic form. | "epic (perf. ἕαδα)". |
| ῥηθέντι | Low | Repeated the headword inside the parse; "a thing said" is thinner than the note's "what was said". | "aor. part. pass. neut. dat. sg.: ’what was said’, with δικαίῳ". |

`t` unchanged again (checked against the pre-pass-2 file). Pass 1 + pass 2 together: High 0, Medium 7, Low 29.

## Refused in pass 2

1. **Known entry ἑκάστης ("agreeing with νηός")**: the pinned example is odd but the parse (fem. gen. sg.) is right for γυῖα ἑκάστης; existing entries are not rewritten.
2. **αὐτοῦ**: the shipped entry already has the plain possessive reading "his" with a noun (ὀστέα δ’ αὐτοῦ) and "his own"; no broadening needed.
3. **κέ, τι, τοι, τις, ἐπί/ἐπ’ (other uses), κατά, πρός, εἰ, ὄφρα, ὅτε**: every use in this part falls under a shipped reading (κέ with potential optative; τι adverbial with negatives; τοι dative and particle; ἐπὶ + dat. "on" at ἐπὶ κροτάφοις; κατὰ δῆμον / κατὰ δώματ’ "throughout"; εἰ in wishes, protases and "whether"; ὄφρα + subj. purpose; ὅτε general with epic τε).
4. **ἀλαπαδνόν "feeble, weak" and ἀπηνής "harsh, rough, unfeeling"**: dictionary glosses in a glossary entry, not renderings; the table's reservations govern `l`/`i`, not the gloss. Kept.
