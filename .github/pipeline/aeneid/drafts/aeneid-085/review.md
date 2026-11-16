# Review — aeneid-085 (Aeneid XI.336–444), adversarial reviewer

**Severity counts: major 5 (scansion: 7 wrong lines and 2 half-lines), medium 4, low 30. Refused or upheld without change: 16. Scan-fixes entries added: 11 (11.361, 11.373 carrier, 11.374 carrier, 11.375, 11.383, 11.389 carrier, 11.390 carrier, 11.391, 11.434, 11.440, 11.442).**

As in 083 and 084, all the majors are scansion. Of the three packet flags, 375 and 391 (UNRESOLVED) are half-lines and needed entries with carriers. 354 (COSTLY 2.0) is right as the scanner has it. Five wrong lines were not flagged.

## How the review was done

**Pass 1** went through all 45 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference;
- the speech marks, the stray marks at 399 and 442, the punctuation at 413, the reading at 425, the Latin Library variants and the `p` flags (336 and 376: right).

**Sources.** I used the Latin, the pinned source and memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). No translation was opened.

**Pass 2:**
- I re-read every field that pass 1 changed.
- I re-read all `l` for misattached words, which gave the fixes at 340–342 (D3) and 419–423 (L27).
- I re-read all `i` for distinctive remembered phrasing. I found none that needed a recast.
- I restored the drafter's file and ran `review_edits.py` once from it, with all edits in one script: 34 replacements, each old string asserted to occur exactly once.

**Checks in the script and against the drafter's copy:**
- `t`, `ln`, `p`, `v` and the top-level fields are unchanged.
- Only `l`, `i` and `n` changed, in 31 fields.
- `l` has as many lines as `t`, and no `i` has a line break.
- Notes run 15–139 words (51–91 here).
- `l` and `i` each have 2 “, 2 ”, 1 ‘ and 1 ’. `t` has 4 “ and 2 ”, so the validator will warn for `t` only (see L1, L2).
- I re-ran the checks from `make_units.py` against the edited file: line counts, five-line limit, endings, note length, speech marks with EXEMPT {399, 440}, and coverage of 336–444. All pass. The one message is "double mark in n" at 440, where the rule-5b note quotes the printed '“devovi'. Published notes do the same (078).

**Files:**
- **`units.json`** was edited only by `drafts/aeneid-085/review_edits.py`, written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically first. The copy of the drafter's file (`units.drafter.json`) was deleted afterwards.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` and do not rerun `make_units.py`.
- **`scan-fixes.json`** was appended to by `drafts/aeneid-085/add_scan_fixes.py` (084's script with this part's `NEW` table). Each entry is checked against:
  - the build's word-match rule;
  - the validator's metre rule (the half-line rule for 375 and 391);
  - the syllable count stated in its `why`.

  The 1016 earlier entries are unchanged and in order, and there are now 1027.
- **`drafts/aeneid-085/scan_check.py`** (084's replica, part id changed). With the fixes applied, the build's scansion step and the validator's metre check give:
  - `sc` on all 45 units;
  - no metre failures;
  - no misaligned units;
  - one report line left: the 11.354 COSTLY note, for a fit that is correct.
- **Build not run**, as instructed. `build_aeneid.py` has no `--help`: it takes the argument as a part id ("no such part: --help").

## Scansion

I hand-scanned all 109 lines and compared each one syllable by syllable with the scanner. The half-lines are 375 and 391. There are no hypermetric lines.

**Packet flags:**
- **11.375 UNRESOLVED (*qui vocat.”*): half-line.** *quī vŏcăt*, entered like 10.580 (*Cui Liger*). It shares unit 373–375, so 373 and 374 are entered as **carriers**. The scanner's fits for both are right.
- **11.391 UNRESOLVED (*semper erit?*): half-line.** *sēmpĕr ĕ | rĭt*, entered like 2.346. It shares unit 389–391 (*An tibi Mavors… semper erit?*), so 389 and 390 are entered as **carriers**. The scanner's fits for both are right.
- **11.354 COSTLY 2.0: right, no entry.** *ādĭcĭ | ās nēc | t(e) ūllī | ūs vĭŏ | lēntĭă | vīncat*: *ad-* is long because *adicias* = *adiicias* (consonantal i), and *ullīus* has its normal long -ī-. The drafter's note says so. House practice leaves a correct COSTLY fit alone (10.473, 11.260).

**Unflagged lines that are wrong (5):**
- **Initial Ae- split:** 442 *Aeneas* (cost 1.2).
- **Greek eu split:** 434 *Teucri* (cost 0.6).
- **Wrong quantities with the right count:**
  - 440: *vōbīs* (both long) and *ănĭmam* (both short). The scanner had *Vŏbĭs ānīmam* (cost 0.0).
  - 383: *ēlŏquĭō* has four syllables and a short *-lo-*. The scanner made *-lo-* long and ran *-quio* into one syllable (cost 0.0). The count came out the same by accident.
- **Wrong syllable count:** 361 *prōĭcĭs* has three syllables, with the root's i a vowel after the prefix (as *rēĭce*, Ecl. 3.96). The scanner took *proi-* as one syllable and lengthened *-cis* before the vowel of *O* (cost 1.5).

**Hand-checked and right:**
- **The groups the brief names:**
  - **Greek eu:** 385 *Teucrorum* (scanner right).
  - **Initial Ae-:** 428 *Aetolus* (scanner right).
  - **Consonantal i after a prefix:** 354 *adicias*; 371 *coniunx*. 361 *proicis* is the opposite case, a vowel i (fixed above).
  - **Greek names:**
    - 404 *Tȳdīdēs*.
    - 404 *Lārissaeus*. Its long first syllable is forced by the metre, as in the same pair at II.197.
    - 403 *Mȳrmĭdŏnum*, and *Phrўgia* with a short y.
    - 405 *Hādriacas*, long by position before dr. *rētrō* is lengthened before tr.
    - 395 *Arcadăs*, Greek accusative.
    - 396 *Bitiās*.
    - 393 *Īliaco*.
    - 394 *Ēvandri*.
- **Others:**
  - 336 *īdem* (masculine).
  - 341 *pătre*, lengthened before tr.
  - 348 *mihī* and 373 *tibī*, long final i.
  - 350 *Trōĭa*, three syllables (the adjective).
  - 355 *hymenaeis*, four syllables.
  - 360 *totiens*, three syllables.
  - 378 and 384 *Drancē*, Greek vocative, long.
  - 383 and 400 *Proinde*, two syllables.
  - 397 *diē*.
  - 413 *occĭdimus*.
  - 420 *Ĭtălae*, short I, as 9.133 and 11.326.
  - 421 *Troianis*.
  - 429 *Messāpus*.
  - 430 *misēre*.
  - 436 *exōsa*.
- **Elision:** 415 *Quamqu(am) O* is the only fit, so O takes the elision and there is no hiatus.
- **Hiatus:** none in the part.

| key | reason (short) |
|---|---|
| 11.361 | *prōĭcĭs* three syllables; 16 |
| 11.373 | carrier for 375; scanner right; 14 |
| 11.374 | carrier for 375; scanner right; 15 |
| 11.375 | half-line *quī vŏcăt*; 3 |
| 11.383 | *ēlŏquĭō* four syllables, short *-lo-*; 17 |
| 11.389 | carrier for 391; scanner right; 14 |
| 11.390 | carrier for 391; scanner right; 15 |
| 11.391 | half-line *sēmpĕr ĕrĭt*; 4 |
| 11.434 | *Teu-*; 13 |
| 11.440 | *vōbīs*, *ănĭmam*; 16 |
| 11.442 | Ae-, *Aenēās*; 14 |

## Changes

**Major (scansion, scan-fixes.json only)**
- **M1.** Initial Ae- was split at 442 (not flagged).
- **M2.** *Teucri* had the eu split at 434 (not flagged).
- **M3.** Wrong quantities with the right count at 440 and 383 (neither flagged).
- **M4.** Wrong syllable count at 361 *proicis* (not flagged).
- **M5.** The half-lines 375 and 391 were unresolved (flagged). Both are now entered, with carriers 373, 374, 389 and 390.

**Medium**
- **D1. Unit 434–437, note.** "'exosa', perfect participle of the deponent 'exosus'" was a false label: there is no deponent *exosus*. Now "'exosa', 'hating', the participle of the defective verb 'exodi', active in sense".
- **D2. Unit 425–427, note.** "'dies', feminine here" is not shown by anything in the line: the note itself makes *multa* the neuter object. Now "'dies', 'time, the passing of days', the subject".
- **D3. Unit 340–342, `l`.** "with these weighs down words" made *dictis* the object. *his… dictis* is the instrument and *iras* the object of both verbs. Now "rises, and with these loads, words, and heaps up angers:".
- **D4. Unit 425–427, note (425 *variisque*).** The note opened "The print has 'variisque'…". That is the rule-5b formula, but the reading is kept as doubtful. The note now opens "'variisque', as printed, is hard to construe". It names both other readings: the Latin Library's *variique*, and *variusque*, which some texts are said to read (from memory, unchecked). The print is kept, as the drafter had it.

**Low: speech marks and the rule-5b note**
- **L1. Unit 399a, note.** *“Nulla salus bello.* is Turnus quoting Drances (362). I upheld the drafter's handling: single marks around the three words in `l` and `i`, `t` as printed. That matches the nested speech at 11.252–293 in 084. The note opened "The print has…", the rule-5b formula, as if this were a misprint. Now it begins "Drances' words of 362, thrown back at him by Turnus. The print sets an opening double mark before 'Nulla' and closes nothing here; l and i give just these three words in single marks… as at XI.252–293".
- **L2. Unit 440–442, note (442 *“devovi.*).** I upheld this as a rule-5b misprint, a stray opening mark omitted in `l` and `i`, as 6.629 and 6.46. The note now opens with the house formula: "The print has '“devovi', a misprint for 'devovi', corrected here: …".
- **L3. Unit 411–414, note (413 *regressum?* before lowercase *oremus*).** Upheld as printed, not a misprint. Lowercase after a question mark is Greenough's habit: LOG records 6.845 kept on that ground, citing 1.583, and I checked both in the source. The note now cites I.583 and VI.845 instead of asserting what Greenough intends.

**Low: elision lists**
- **L4. 336–339:** added *stimulisqu(e) agitabat*.
- **L5. 346–350:** added *consediss(e) urbem*.
- **L6. 357–359:** added *ips(um) obtestemur*.
- **L7. 408–409:** added *tec(um) et*.
- **L8. 411–414:** added *pac(em) et*.
- **L9. 415:** "No elisions" is now "Elision 'Quamqu(am) O'".
- **L10. 432–433:** "No elisions" is now *Volscor(um) egregia*, *equit(um) et*. Also added that 433 repeats VII.804 word for word (checked).
- **L11. 438–440:** added *pari(a) induat*.

**Low: other notes**
- **L12. 336.** "*stimulis… amaris*… framing the line-end" is now "framing the verb".
- **L13. 341.** "(Servius takes it either way)" was unchecked and from memory. Now "the words allow either".
- **L14. 354.** "*adicias*, potential or jussive" is now "jussive subjunctive, a polite command".
- **L15. 351.** *fugae fidens* as an allusion to the Tiber leap (IX.815–818) was asserted. It is now "perhaps glancing at".
- **L16. 366.** "'Sat'… with the genitive understood or simply adverbial" is now "standing as an indeclinable adjective with 'funera'".
- **L17. 370.** *adversum* was given only with *hostem*. It can equally go with *pectus*, and the note now gives both.
- **L18. 372.** The Latins' burials were cited as "(182–224)". In the source they are 203–212: 184–202 are the Trojans' pyres, 213–224 the mourning in the city.
- **L19. 375.** "Aeneas, who said he would rather have met Turnus in single combat (115–118)" is now "who said Turnus should have fought it out with him alone". That is what 115–117 say.
- **L20. 402.** Added the cross-reference for the twice-taken Trojans: Numanus's *bis capti Phryges*, IX.599 (checked).
- **L21. 404.** Added that the pair echoes II.197, *Tydides, nec Larisaeus Achilles* (checked; Greenough spells it *Larisaeus* there).

**Low: `l` construal and layout**
- **L22. 337.** "with goads was driving bitter" read *bitter* as a result. Now "was driving, bitter ones,".
- **L23. 345.** *dicere mussant*, "to say they mutter", is now "to say it they hesitate, muttering". With an infinitive, *musso* means hesitate to speak (L&S).
- **L24. 363.** "together with peace's… pledge" made *simul* a preposition, but *pignus* is accusative. Now "and at the same time peace's sole inviolable pledge".
- **L25. 390.** "in feet fleeing those" is now "in those runaway feet of yours".
- **L26. 400.** "of the Dardanian" read *Dardanio* as a genitive. It agrees with *Capiti*. Now "the Dardanian, and to your own affairs".
- **L27. (pass 2) 421.** "with much glory has come / blood" gave *multo* to *gloria*. *cum multo… sanguine* frames *gloria venit*. Now "with much, glory has come, / blood".

**Low: `i`**
- **L28. 336–339.** The `i` began "Then Drances rose", taking *surgit* from 342, and unit 340–342's `i` also has "he rose". Now "Then Drances, hostile as ever, …".
- **L29. 370.** "against the enemy who faces you" took one side of the ambiguity (L17). Now "bear your breast confidently to face the enemy".
- **L30. 406.** "Or then, when…" was unidiomatic. Now "Or take the times when…".

## Refused or upheld without change

1. **399, the reading as a nested quotation.** Upheld (L1). I considered the 9.146 handling, a mid-speech “ read as the printer's mark for a new paragraph, and rejected it here: 399 is not indented in the source, and the three words are Drances' own.
2. **442 as a rule-5b misprint.** Upheld (L2).
3. **413, kept as printed.** Upheld (L3).
4. **425 *variisque*, kept as printed.** Upheld (D4). Two different corrections are possible, so it is doubtful, not a clear misprint.
5. **354 COSTLY.** No entry: the scanner is right.
6. **367 *ingentis* with *agros*.** Upheld. The -is accusative plural cannot go with neuter *funera*.
7. **378 *semper*, the Latin Library's word order.** Upheld as a note with no change of sense.
8. **The other Latin Library variants** (*futtilis*, *ciuis*, *si qua*, *uiris*, *Larisaeus*, *ne quid*, *Volcani*). Orthographic and rightly not discussed. *siqua* and *nequid* are glossed as one word, which is harmless.
9. **418, Iliad II.418 (biting the earth).** Kept with "from memory". It matches my memory (ὀδὰξ λαζοίατο γαῖαν, Agamemnon's prayer).
10. **440, Iliad XVIII (Hephaestus's armour).** Kept with "from memory".
11. **343, *consulo* with the accusative of the thing.** Upheld.
12. **416–417, *fortunatus laborum* (genitive of respect, Greek model) and *egregius animi* (locative-genitive).** Upheld. Both are Allen & Greenough doctrine.
13. **354–356, *quin* after the idea of prevention in *nec… vincat*.** Upheld.
14. **402 *arma Latini* as the king's side.** Upheld. "The Latin's" is also possible, but nothing turns on it.
15. **New house renderings: none.** Upheld. *Nulla salus bello* is quotable but not a set piece.
16. **`about`.** The comparison with Thersites and Polydamas is interpretive but fair, and is hedged ("while being neither"). It is outside the reviewer's fields anyway.

## Cross-references

**Checked in the pinned source:**
- 122–131 (Drances' earlier speech).
- 115–118 (L19).
- 333–334 and 316–334 (Latinus's offer).
- 203–212 (L18).
- VI.325–330.
- IX.672–676, 703–705, 749–755, 815–818 (Pandarus, Bitias, the leap).
- X.479–489 (Pallas).
- XI.5–11 (the trophy).
- XII.9 and XII.45 (*violentia Turni*).
- VII.691–705 (Messapus).
- XII.258 (Tolumnius).
- VII.803–817 (Camilla, with 804 = 433).
- VIII.608–616 and 729 (*Volcani*).
- 239 (*Aetola*).
- 225–295.
- II.197.
- IX.599.
- I.583 and VI.845.

All right after L18 and L19.

**Unchecked, from memory, and plausible (kept, stated plainly or softened):**
- Iliad II.418; Iliad XVIII.
- Daunus as a fighter.
- Troy taken by Hercules in Laomedon's time.
- The Decii and the *devotio*.
- Homer's "winged words".
- The general's auspices.
- *curia* as an anachronism.
- Servius on 341 (softened away, L13).
- *variusque* as a reading in other texts (D4).

## For the owner / QUESTIONS.md

- **Rule-5b misprint.** 11.442 `“devovi.`: a stray opening mark, omitted in `l` and `i`, `t` as printed, note opening "The print has…". The publishing run should add the QUESTIONS entry.
- **Nested quotation, 399.** `“Nulla salus bello.`: the print opens a mark and never closes it. `l` and `i` give the three words in single marks, as for Diomedes' words at 11.252–293. `t` has 4 “ and 2 ”, so the validator warns for `t` only. If you rule the mark a misprint instead, only the note of unit 399a changes.
- **Doubtful reading kept.** 11.425 `variisque`: Latin Library `variique`; *variusque* is from memory, unchecked. If you rule it a misprint, say for which reading. Only the note's opening and the `l` phrase "with varied (turns)" change.
- **Kept as printed (Greenough's habit, not a question).** 11.413 `regressum?` before lowercase `oremus`.
- **Build.** Not run. Build from `units.json` as it stands, and do not rerun `make_units.py`.
