# aeneid-037 (V.580–679): adversarial review

Two passes over all 53 units. Pass 1: every grammatical label in every note; Latin to `l` word by word; `l` against `i`; speech marks; echoes of known versions. Pass 2: a re-read of every changed field (diffed against the draft), then a hand scansion of the four flagged lines and every line with Greek eu, initial Ae-, consonantal i, a Greek name with separate vowels, or a hiatus. After the scansion pass, every remaining line was checked by hand as well, because three wrong fits (588, 610, 668) came back from the scanner at cost 0.0–0.3 and so were never flagged.

`t`, the source and the `parts.json` sha are untouched: every `t`, `ln` and `p` is identical before and after (checked by script). Edits were made to the `U` data in `make_units.py` by an exact-match replacement script, and `units.json` was regenerated from it. Scansion fixes were added to `scan-fixes.json` (additions only; no existing entry changed). The build's scansion step and the validator's metre checks were simulated with the new entries, without running the build: all 53 units get `sc`, no UNRESOLVED remains, every line is six valid feet, and the half-line passes the hemistich check.

Counts: **13 major, 7 medium, 18 low** (38 findings).

## Major (13)

Scansion (11). An entry was added for each.
1. 5.588: the scanner gave `Creta` two shorts and `Labyrinthus` a long La- and a long by-. Crēta has a long ē and the ablative -ā is long, while Lăbyrinthus has La- and by- short: Ut quon | dam Crē | tā fer | tur Lă-bў | rin-thŭs ĭn | al-tā. The scanner reported this at cost 0.0, so the packet did not flag it.
2. 5.592: the scanner split `Teucrum` into Te-u (cost 0.0). Teu- is one long syllable.
3. 5.610: the scanner made `visa` a spondee, `ci-` long, and `-to` and `de-` short (cost 0.0). The right reading is vīsă cĭ | tō dē | cur-rit.
4. 5.620: `coniunx` was read co-ni-unx with a short co-. It is con | iunx, and the feet change: fit Bĕ-rŏ | ē Tmă-rĭ | ī con | iunx lon | gae-vă Dŏ | rў-clī.
5. 5.634: the scanner read `Simoenta` with the diphthong oe and made Si- long (cost 0.0). The word is Sĭ-mŏ-en-ta, so the fourth foot is th(um) et Sĭ-mŏ and the fifth en-tă vĭ.
6. 5.647: `coniunx` was again read co-ni-unx. It is con | iunx: est Dŏ-rў | clī con | iunx dī | ….
7. 5.650: the scanner read `Beroen` as Be-roen, with oe as a diphthong and Be- long (cost 0.0). The word is Bĕ-rŏ-ēn, as Beroë is at 620 and 646: dum Bĕ-rŏ | ēn dī.
8. 5.653: the half-line `Haec effata.` came back UNRESOLVED, which would have stopped the build. A hand scansion was entered: Haec ef | fā-ta. The line is a unit by itself, so it needs no carrier entry.
9. 5.665: `Eumelus` was split into E-u (cost 0.0). Eu- is one long syllable: vēs Eu | mē-lŭs ĕt | ip-si.
10. 5.668: the scanner made `sic` and `a-` short, and `-cer` and `e-` long (cost 0.3). The right reading is bat sīc | ā-cĕr ĕ | quō tur.
11. 5.675 (flagged COSTLY 2.7): `Aeneas` was split into A-e with a short -ne-. It is Aē-nē-ās.

Grammar (2).
12. Unit 643 (`Iliadum`): the note called it "the Greek first-declension form in '-um'". That is false. `Ilias, Iliadis` is third declension, and -um is its ordinary genitive plural. The note was corrected.
13. Unit 650 (`inferet`): the note called it "Greenough's future indicative". The future `inferet` has a short second syllable, and the line does not scan with it: with Anchisae elided, the fifth foot would be three shorts. The metre needs `inferret`, the Latin Library's reading, and so does the sense, which runs parallel with `careret`. The note now opens "The print has 'inferet', a misprint for 'inferret', corrected here…" and says that `t` keeps the print. `l` ("would not bring") and `i` ("could not pay") already read `inferret`. The scanner's fit for 652 already treats fe- as long, which is right for the line as Virgil wrote it, so 652 gets no entry.

## Medium (7)

14. Unit 583: the note said "they entangle circles with alternating circles". That attaches `alternos` to `orbibus`, but it agrees with the accusative `orbes`. The note now says "alternating circles with circles, 'alternos' agreeing with 'orbes'". `l` became "alternating with circles, circles".
15. Unit 588: `l` read "with walls a woven blind path", which attaches `caecis` to the path. The note and the grammar have it with `parietibus`. `l` now reads "with blind walls a woven path", and the note adds "agreeing with 'parietibus'".
16. Unit 592: the note said that without `luduntque per undas`, "the relative 'qui… nando' has no verb". That is false, because `secant` remains. The note now says this happens only if the whole bracketed line is dropped.
17–20. Units 613, 623, 653 and 675: the reader-facing notes mentioned the scanner ("The scanner flags … for hand-checking", "the scanner marks it UNRESOLVED"). These were deleted, following the 036 precedent. The half-line note at 653 now opens the way the published 020 note does.

## Low (18)

21. Unit 580: `l` had "the columns, the three", which makes `terni` look as if it agreed with the neuter `agmina`. `l` now reads "their columns, in threes", and the note says that `terni` agrees with the riders.
22. Unit 588: one clause was added on `parietibus` scanning par-ie-ti-bus, with a consonantal i, as the 663 note already does for `abiete`. The reader would otherwise meet that `sc` unexplained.
23. Unit 596: "Longam… Albam… split across the line by 'muris'" was inaccurate. Both words are in one line, split by `muris cum cingeret`.
24. Unit 602: the note had `dicitur` doing duty for both clauses and also "'dicuntur' understood", which contradicts itself. It now says the one `dicitur` stays singular in the second clause, agreeing with the predicate `agmen`.
25. Unit 605: `l` had "not yet having glutted", which is active, for the passive `saturata`. The note has "sated". `l` now reads "not yet sated as to her ancient pain".
26. Unit 620: "the name frames the line" was false, because `fit Beroë` comes first. The note now says that `Tmarii… Dorycli` enclose `coniunx longaeva`.
27. Unit 637: `l` had "here is the home" for `domus` without an article. The note has "a home". `l` now reads "here is a home".
28. Unit 654: `l` had "the goddess herself … raised", which reads `se` as intensive. `l` now reads "the goddess raised herself on balanced wings through the sky".
29. Unit 659: `i` had "hearths within the houses", but the note puts them in the shelters of the camp on the shore. `i` now reads "within their shelters".
30. Unit 673: the note said "'Galeam… inanem'… framing the line", but `Galeam` stands mid-line. It now says "framing the clause".
31. Unit 676: `l` read "But they, scattered in fear over the shores", which makes `diversa` look as if it agreed with "they". `l` now reads "But they, in fear, over the scattered shores".
32–38. Units 583 (`orbis`), 626 (`omnis`), 633 (`amnis`), 635 (`puppis`), 636 (`ardentis`), 647 (`ardentis`) and 667 (`equestris`): the notes reported Latin Library -is/-es differences, which conventions.md says to ignore as morphology. These were deleted. The variants that give the familiar spelling once (`adspirat`, `Septuma`, `exscidium`, `adgnoscunt`, `voltus`, `Troïa`, `Beroë`) and the variants that change the sense (`frangeret`, `Hinc`, `inferret`) were kept.

## Refused or left as drafted (no change)

- 5.613 (COSTLY 3.0) and 5.623 (COSTLY 2.0): both fits were checked by hand and are correct. 613 is At prŏ-cŭl | in sō | lā sē | crē-tae | Trō-ă-dĕs | ac-tā, with sōlā and actā long ablatives and Troadĕs a Greek nominative with short -es. 623 is Ō mĭ-sĕ | rae quās | nōn mă-nŭs | in-quĭt Ă | chā-ĭ-că | bel-lo. No entries were made, following the practice that entries override the scanner. The build will still list both lines as COSTLY in its report, and the reviewer has confirmed them.
- 5.589 `parietibus`: the scanner's consonantal-i reading (par-ie-ti-bus, cost 1.5) is right. 5.663 `abiete` (ab-ie-te) is right too.
- 5.619 `conicit` and 5.662 `coniciunt`: the quantities (cō-nĭ-cĭt) are right. Only the syllabification (co-ni) is loose, which is the same treatment as `obicitur` in 036. No entry.
- 5.673 `proiecit` (prō-iē-cit, three syllables), 5.602 `Troiaque` / `Troianum`, 5.631 `iacere` and 5.643 `iacit`: all right.
- 5.599 `Troïa`, 5.646 `Rhoeteïa` (COSTLY 1.9 in the scanner's own run, below the flag threshold in the packet) and 5.607 `Iliacam`: right.
- 5.644 `Iliadum. Hic`: -um elides across the full stop, which is right. No hiatus is needed.
- 5.671 `heu` is one syllable. 5.679 `Iuno est` is prodelision, shown the scanner's way as in published 001, 002 and 004. Both are right.
- 5.652: the scanner's long fe- is right for the true reading (see item 13). No entry.
- Unit 646 `l` "this Rhoetean woman": the note explains the agreement with `coniunx`, and `i` follows it. Left.
- Unit 670 `i` "What is this strange madness?" drops `iste` ("of yours"), and the note covers it. This is not a distinctive echo. Left.
- Unit 605 `i` "favouring winds": `adspirare` regularly carries this sense. Left.
- Unit 610 `decurrit` rendered as past: the form could be present or perfect, and the past suits the narrative. Left.
- Unit 639 `tantis… prodigiis` as dative: defensible (an ablative is also possible). Left.
- Echo check of every `i`, from memory only and without opening any translation: no distinctive echo of a known version was found. The phrases checked were `Italiam sequimur fugientem` ("an Italy that flees before us"), `haud ignara nocendi` ("no stranger to the art of doing harm"), `vox omnibus una`, `Quis furor iste novus`, `Furit immissis Volcanus habenis` and `excussaque pectore Iuno est`. Nothing was rephrased.
- Speech marks were checked across `t`, `l` and `i`. The women's cry runs 615–616 and Beroë/Iris 623–640, with Cassandra's dream words in single marks at 637–638. Pyrgo runs 646–652 and Ascanius 670–673, broken at `inquit`. All open on their first unit and close on their last. The misprints in `t` (616 `”vox`, 637 `“ardentes`, 638 `“hic`, 671 `”inquit`, 673 `”Galeam`) are left in `t`, as required, and the notes say so.
- Misprint in `t` at 652 (`inferet`): `t` was not changed.

## scan-fixes.json entries added (11)

5.588, 5.592, 5.610, 5.620, 5.634, 5.647, 5.650, 5.653 (half-line), 5.665, 5.668, 5.675.

## Unconfirmed (for QUESTIONS if wanted)

- `inferet` at 652: the metre proves it is wrong for the line, but whether Greenough's 1881 print has `inferret`, so that the slip is the Perseus transcription's, could not be checked against the printed page.
- `Dorycli`: rў is taken long before cl at 620 (sixth foot) and short at 647 (first foot), as a common syllable. Both are the only fits.
- `Tmarii` with a short a (Greek Τμάρος), and `Lăbyrinthus` with short La- and by-: these are the standard quantities, but they were not checked against a dictionary entry in the pipeline.
