# Review — aeneid-086 (Aeneid XI.445–531), adversarial reviewer

**Severity counts: major 6 (scansion: 7 wrong lines in 5 groups; plus the unit 492–493 that the build will refuse), medium 3, low 14. Refused or upheld without change: 18. Scan-fixes entries added: 7 (11.446, 11.449, 11.472, 11.480, 11.487, 11.511, 11.512).**

**Blocking, needs a decision before the build (M6):** `build_aeneid.py` line 35 refuses any unit whose `t` does not end at `. ; : ? ! ,` (or a dash). Unit 18 (492–493, ending `aperto`) does not, so **the build will refuse this draft as it stands** ("unit 18 (line 492): does not end at punctuation"). The brief's premise that the build does not forbid this is mistaken. My replica of the build's unit checks (`review_check.py`) reports that one error and nothing else. See "The horse simile" below.

## How the review was done

**Pass 1** went through all 33 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference;
- the speech marks, including the rule-5b units 459 and 463, the Latin Library variants and the `p` flag (445 only: right).

**Sources.** I used the Latin, the pinned source and memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). No translation was opened.

**Pass 2:**
- I re-read every field that pass 1 changed.
- I re-read all `l` for misattached words, which gave L13 and L14.
- I re-read all `i` for distinctive remembered phrasing and found none that needed a recast. The renderings of the horse simile, the prayer and Turnus's arming are plain and literal.
- I restored the drafter's file and ran `review_edits.py` once from it: 20 replacements, each old string asserted to occur exactly once.

**Checks in the script and against the drafter's copy:**
- `t`, `ln`, `p`, `v` and the top-level fields are unchanged.
- Only `l`, `i` and `n` changed, in 16 fields.
- `l` has as many lines as `t`, and no `i` has a line break.
- Notes run 50–122 words.
- `l` and `i` each have 7 “ and 7 ”. `t` has 7 “ and 6 ”, so the validator will warn for `t` only. That is expected: the print's stray reopening mark is at 464.
- `review_check.py` runs `make_units.py`'s checks on the edited file: line counts, five-line limit, endings, note length, speech marks with EXEMPT {459, 463} and NOSTOP {492}, and coverage of 445–531. All pass. The double marks in the notes of 459 and 463 are allowed: they quote the print in the rule-5b opening, as published notes do at 11.24 and 11.98.
- The same script holds a replica of the build's per-unit checks (tiling, `ln`, `p`, five lines, ending). Its only failure is unit 18.

**Files:**
- **`units.json`** was edited only by `drafts/aeneid-086/review_edits.py`, written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically first.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` and do not rerun `make_units.py`.
- **`scan-fixes.json`** was appended to by `drafts/aeneid-086/add_scan_fixes.py` (085's script with this part's `NEW` table). Each entry is checked against:
  - the build's word-match rule;
  - the validator's metre rule;
  - the syllable count stated in its `why`.

  The earlier entries are unchanged and in order. There were 1027 keys and there are now 1034.
- **`drafts/aeneid-086/scan_check.py`** (085's replica, part id changed). With the fixes applied, the build's scansion step and the validator's metre check give:
  - `sc` on all 33 units;
  - no metre failures;
  - no misaligned units;
  - no report lines.
- **Build not run.** `build_aeneid.py` has no dry run and no `--help`: it takes the argument as a part id and exits "no such part: --help".

## Scansion

I hand-scanned all 87 lines and compared each one syllable by syllable with the scanner. The packet flagged none. There are no half-lines and no hypermetric lines.

**Unflagged lines that are wrong (7):**
- **Initial Ae- split:**
  - 446 *Aenēās* (cost 1.2, 15 syllables for 14).
  - 472 *Aenēān* (cost 1.2, 16 for 15).
- **Greek eu split:** 449 *Teucros* (cost 0.6). The scanner counted 16 syllables and, to fit, made *flū-* short and *-mi-* long.
- **Hiatus:** 480 *causa mali tanti, oculos deiecta decoros*. The scanner (cost 0.0) elided *tanti* and made *ŏcŭ-* long-long. True scansion: *cau-să mă | lī tan | tī ŏ-cŭ | lōs dē | iec-tă dĕ | cō-ros*, with hiatus at the pause and the main caesura, as at 1.16. With the elision there is no fit with natural quantities. *dēiecta* has consonantal i.
- **aenis as a diphthong:** 487. *ă-ē-nis* has three syllables, as at 1.295, 1.449 and 8.22. The scanner (cost 0.0) counted 14 syllables and made *rŭtĭlum* long-long.
- **Wrong quantities with the right count:**
  - 511: the scanner had *Ae-nĕ-ăs* and *fāmā fī-*. The true scansion is *Ae-nē | ās ut | fā-mă fĭ | dem…* (cost 1.0).
  - 512: the scanner had *ex-plŏ-ră-tō-rēs* and *ē-quī-tum*. All of *explōrātōrēs* is long, and *ĕquĭtum* is short-short (cost 0.0).

**Hand-checked and right:**
- **The groups the brief names:**
  - **Initial Ae-:** 503 *Aeneadum*: *au-dĕ(o) ĕt | Ae-nĕ-ă | dum…*. The scanner kept Ae- as one syllable here and is right. 487 *aenis* is the opposite case, fixed above.
  - **Greek and unusual names:**
    - 457 *Pădūsae*.
    - 463 *Vŏlŭse*.
    - 465 *Cŏrās*.
    - 483 *Trītōnĭa*.
    - 484 *Phrўgĭī*.
    - 464 and 518 *Messāpus*.
    - 479 *Lāvīnĭa*. It has four syllables with a vowel i (*Lā-vī-nĭ | ă vir-go*), not consonantal; the scanner agrees.
    - 498 *Camilla*.
    - 450, 504 and 517 *Tyrrhēn-*.
  - **Consonantal i after a prefix:** 480 *dēiecta* (dē-iec-ta). The scanner is right on that word; the line was wrong for the hiatus. No other prefix-i word occurs in the part.
  - **Synizesis:** 495 *adsuētus*, with *sue* as one syllable (*ad-sue-tŭs ă-quae*). The scanner is right (cost 1.5, not flagged; no entry).
  - **Elision, not hiatus:** 456 *haud secus atqu(e) alt(o) in luco*. Both vowels elide (*haud sĕ-cŭs | at-qu(e) al | t(o) in lū | cō cum…*), there is no hiatus, and the scanner is right.
- **Others:**
  - 492 *fūgit*, perfect, forced by the metre: *tīs fū | gīt prae*, the -it long before *pr-*. The scanner is right. The note and `l` are now corrected (D3).
  - 469 *pătēr* lengthened in the third arsis before *et*. Scanner right. The note now says so (L10).
  - 459 *Imm(o) ăĭt*.
  - 471 *s(e) incusat*.
  - 502 *siqu(a) est*.
  - 508 *Ītaliae*.
  - 510 *sūprā*.
  - 516 *obsīdam* (from *obsīdo*).
  - 518 *ācer*.
  - 519 *Tībur-*.
  - 524 *tĕnŭīs*, three syllables.
  - 527 *plānĭtĭēs*.
  - 531 *insēdit ĭnīquis*.

| key | reason (short) |
|---|---|
| 11.446 | Ae-, *Aenēās*; 14 |
| 11.449 | *Teu-*; 15 |
| 11.472 | Ae-, *Aenēān*; 15 |
| 11.480 | hiatus *tantī, ŏculos*; 15 |
| 11.487 | *ă-ē-nis*, *rŭtĭlum*; 15 |
| 11.511 | *Aenēās*, *fāmă*, *fĭdem*; 14 |
| 11.512 | *explōrātōrēs*, *ĕquĭtum*; 15 |

## The horse simile (492–497): the unit ending without a stop

Greenough prints 492–497 as one period. Its only marks are the commas after *luxurians* and *colla* in 497. Any unit that reaches one of those commas from 492 spans six lines. So no tiling of these lines meets both of the build's rules, the five-line limit (line 34) and the ending at punctuation (line 35).

I would **keep the drafter's split after 493 *aperto***. It is the one real joint in the period. The *ubi*-clause (the horse bolts, free, master of the plain) ends there, and the two *aut… aut* alternatives with their main verbs begin. The conventions make five lines a hard limit for the reader's tap-units. They already accept a comma end inside a long period (2.166 and 2.462 in 010 and 013). A six-line unit would break the five-line rule outright.

But the build refuses the split as it stands, so one of these is needed, and it is the run's or the owner's call, not the reviewer's:
1. **A narrow allowance in `build_aeneid.py`** for an unpunctuated unit end at a line end, recorded per unit. This is my recommendation.
2. **Rule 5.** Add a comma after *aperto* in the source and re-pin aeneid-086. This is allowed only if Greenough's page prints it, and I cannot check the page; many editions punctuate there, but that is not evidence for Greenough.
3. **One six-line unit 492–497.** This needs the five-line check relaxed instead.

Under option 2 the note's first sentence ("divided here, without a mark") would change. Under option 3, units 18 and 19 would merge and their `l`, `i` and `n` would need joining.

## Changes

**Major (scansion, scan-fixes.json only)**
- **M1.** Initial Ae- was split at 446 and 472 (not flagged).
- **M2.** *Teucros* had the eu split at 449 (not flagged).
- **M3.** The hiatus at 480 *tanti, oculos* was scanned as an elision with wrong quantities (not flagged).
- **M4.** 487 *aenis* was read as a diphthong (not flagged).
- **M5.** Wrong quantities with the right count at 511 and 512 (not flagged).
- **M6.** Unit 492–493 will be refused by the build (above). Not fixed: it needs a decision.

**Medium**
- **D1. Unit 505–506, `n`, `l`, `i`.** The note said "'prima', feminine again, 'the first'". That is impossible: the subject of *temptare* is the accusative *Me*, so a feminine would have to be *primam*. *prima* is neuter plural with *pericula*, "the first dangers of war". All three fields are corrected:
  - the note now explains why;
  - `l` is now "Me allow with my hand to try the first dangers of war;";
  - `i` is now "Let me put my hand to the first hazards of war, while…".
- **D2. Unit 477–480, `n`.** The elision list gave 'tant(i) oculos'. It is hiatus (M3). The note now says "'tanti, oculos' is not elided: 'tanti' keeps its long -i in hiatus at the pause and the main caesura (as 'Samo hic', I.16)".
- **D3. Unit 492–493, `n` and `l`.** *fugit* is perfect *fūgit*, forced by the metre, but `l` had the present "flees". `l` is now "has fled the stalls". The note adds that *fugit* is the perfect of the instant of breaking loose, followed by the presents *tendit… emicat*.

**Low: rule-5b notes (house formula "The print has…")**
- **L1. Unit 459–462.** The note now opens "The print has '“Immo, ait, O cives adrepto tempore, Turnus,”', with 'ait' and 'Turnus' inside the marks, a second opening mark before 'cogite', and 'ruunt. ”Nec' at 461 (as 'vale. ”Nec', 11.98): misprints for a speech … corrected here."
- **L2. Unit 463–464.** The note now opens "The print has '“duc, ait, et Rutulos' at the start of 464, a misprint (as '“Ite, ait,' at 11.24) for 'duc,” ait, “et Rutulos', corrected here: …".

**Low: other notes**
- **L3. 463:** added the elision *Volscor(um) edice*.
- **L4. 526:** added the elision *summoqu(e) in*.
- **L5. 460:** added that *cogite concilium* throws back Latinus's own *cogere concilium* (304, checked).
- **L6. 465.** "Coras and his brother Catillus, Argive founders of Tibur… (from memory, about 670–677)" is now "Coras and his twin Catillus, Argive warriors from Tibur, the town named after their brother Tiburtus… (670–677)". That is what VII.670–672 says (checked).
- **L7. 519.** "Tiburtus, founder of Tibur" is now "the brother of Coras and Catillus after whom Tibur is named (VII.671)".
- **L8. 453:** VII.460 *arma amens fremit* checked in the source; "from memory" dropped.
- **L9. 480:** VI.93 *Causa mali tanti* checked; "from memory" dropped.
- **L10. 469:** added that the last syllable of *pater* is lengthened in the third arsis.
- **L11. 487:** added that *aenis* has three syllables, a-e-nis.
- **L12. 487–491.** "The tenses move from pluperfect to imperfect" was wrong, because *horrebat* (imperfect) comes first. Now "Imperfects ('horrebat', 'fulgebat') and pluperfects ('incluserat', 'adcinxerat') give way to the vivid present".

**Low: `l`**
- **L13. 475.** "with a varied ringed garland" read *cinxere* as an adjective. Now "Then the walls, with a varied garland, ringed".
- **L14. 488.** "he bristled scales" made *squamis* the object of *horrebat*. Now "he bristled, scales," (*with bronze… scales*).

## Refused or upheld without change

1. **459–461 as rule-5b misprints.** Upheld:
   - `t` is as printed. `l`/`i` set *ait… Turnus* outside the marks and close after *ruunt.*
   - The unit carries 'Nec plura locutus… altis' so the misplaced closing mark stays inside one unit. That is a 4-line unit, which is fine.
   - Only the note's opening changed (L1).
2. **463–464, the reopening mark before *duc*.** Upheld, as 11.24 (L2).
3. **The split after 493.** Kept and recommended, but blocked by the build (M6).
4. **469 *Consilium* / Latin Library *concilium*.** The note is right to give it: the sense changes, and *differt* suits a plan. Kept.
5. **463 *maniplos* / *maniplis*.** Right: the construction changes, not the sense.
6. **466 *firmet… capessat* / plurals.** Right, one clause.
7. **The orthographic variants** (*adrectae*, *adrepto*, *adceperit*, *adsciverit*, *adcinxerat*, *praesaepia*, *adrectisque*, *siqua*, *adcommoda*). Rightly treated as Greenough's spellings, not as variants.
8. **492 *fūgit*.** The scanner is right, so no entry. The `l`/`n` fix is D3.
9. **503 *Aeneadum*.** The scanner is right, so no entry.
10. **456 *atque alto in luco*.** Elision, not hiatus. The scanner is right.
11. **479 *Lāvīnia*.** Four syllables with a vocalic i. The scanner is right.
12. **495 *aquae* "probably dative".** The hedge is upheld; a genitive with *flumine* is possible.
13. **498 *quam… imitata* called a connecting relative.** Loose but defensible: the clause carries the next main action. Kept.
14. **453 *fremit arma* as an internal accusative.** Defensible ("roars 'arms!'"); "roars for arms" with a plain object is the other reading. Kept.
15. **486 *certatim* of one man.** Kept as "with all eagerness".
16. **Homeric references:**
    - Iliad II.459–466 (birds by the Cayster);
    - Iliad VI.286–311 and 305–310 (Theano's prayer, refused by Athena), which matches my memory of 311;
    - Iliad VI.506–511 and XV.263–268 (the horse simile).

    All kept with "from memory", plausible. The others kept from memory are *Ilicet* < *ire licet*, and Padusa and its swans.
17. **`i` echoes.** None distinctive enough to recast.
18. **New house renderings and advisory:** none. Upheld.

## Cross-references

**Checked in the pinned source:**
- VII.460;
- VI.93;
- I.159;
- VII.670–677;
- VII.803 (Camilla closing the catalogue);
- XI.302–335 (Latinus's proposal and embassy; *cogere concilium*, 304);
- XI.24 and XI.98 (rule-5b precedents).

All right after L6–L9.

## For the owner / QUESTIONS.md

- **Blocking (M6): unit 492–493 ends without punctuation.** The build will refuse it. Greenough's six-line simile 492–497 has no internal mark before 497, so the five-line rule and the punctuation-ending rule cannot both be met. My recommendation is to keep the split after *aperto* and give the build a recorded per-unit allowance. The alternatives are rule 5 (only if Greenough prints a comma after *aperto*, which I cannot check) or a six-line unit.
- **Rule-5b misprints:**
  - 11.459–461: `“Immo, ait, O cives adrepto tempore, Turnus,” “cogite… ruunt. ”Nec`.
  - 11.464: `“duc, ait,`.

  `t` is as printed, `l`/`i` are corrected and the notes open "The print has…". The validator will warn for `t` (7 “ / 6 ”).
- **Variant noted for sense:** 469 *Consilium* (Latin Library *concilium*), print kept.
- **Build:** not run. Build from `units.json` as it stands, and do not rerun `make_units.py`.
