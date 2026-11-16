# Review — aeneid-084 (Aeneid XI.225–335), adversarial reviewer

**Severity counts: major 5 (scansion, 13 wrong lines), medium 8, low 23. Refused or upheld without change: 15. Scan-fixes entries added: 14 (11.232, 11.247, 11.251, 11.254, 11.262, 11.279, 11.282, 11.289, 11.292, 11.300, 11.302, 11.308 carrier, 11.309, 11.321).**

As in 083, all the majors are scansion. Of the two packet flags, 11.309 (UNRESOLVED) needed a fix and 11.260 (COSTLY 3.0) is right as the scanner has it. Twelve wrong lines were not flagged.

## How the review was done

**Pass 1** went through all 56 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference;
- the speech marks, the misprint at 236, the possibly dropped punctuation (291, 326, 328), the Latin Library variants, `about`, `title`, `part`, `titleEn` and the `p` flags (225, 243, 296: right).

**Sources.** I used the Latin, the pinned source and memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). No translation was opened.

**Pass 2:**
- I re-read every field that pass 1 changed.
- I re-read all `l` for misattached words, which gave the fix at 265 (L13).
- I re-read all `i` for distinctive remembered phrasing, which gave the recast at 309 (L23).
- I restored the drafter's file and ran `review_edits.py` once from it, with all edits in one script: 40 replacements, each old string asserted to occur exactly once.

**Checks in the script and against a copy taken before any edit:**
- `t`, `ln`, `p`, `v` and the top-level fields are unchanged.
- Only `l`, `i` and `n` changed, in 39 fields.
- `l` has as many lines as `t`, and no `i` has a line break.
- Notes run 15–139 words.
- `l` and `i` each have 2 “, 2 ”, 1 ‘ and 1 ’ (see D8).

**Files:**
- **`units.json`** was edited only by `drafts/aeneid-084/review_edits.py`, written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically first.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` and do not rerun `make_units.py`.
- **`scan-fixes.json`** was appended to by `drafts/aeneid-084/add_scan_fixes.py` (083's script with this part's `NEW` table). Each entry is checked against:
  - the build's word-match rule;
  - the validator's metre rule;
  - the syllable count stated in its `why`.

  The 1002 earlier entries are unchanged and in order, and there are now 1016.
- **`drafts/aeneid-084/scan_check.py`** (083's replica, part id changed). With the fixes applied, the build's scansion step and the validator's metre check give:
  - `sc` on all 56 units;
  - no metre failures;
  - no misaligned units;
  - one report line left: the 11.260 COSTLY note, for a fit that is correct.
- **Build not run**, as instructed.

## Scansion

I hand-scanned all 111 lines and compared each one syllable by syllable with the scanner. There are no half-lines and no hypermetric lines.

**Packet flags:**
- **11.309 UNRESOLVED: fixed.** The monosyllable *quam* is elided: *pōnĭtĕ | spēs sĭbĭ | quīsquĕ sĕd | hāec qu(am) ān | gūstă vĭ | dētīs* (16). Because a unit with an unresolved line gets no `sc` at all, 308 (same unit 308–309) needs a **carrier entry**. The scanner's own fit for 308 is right (*Aetolum*, Ae- one syllable).
- **11.260 COSTLY 3.0: right, no entry.** *sīdŭs ĕt | Eūbŏĭ | cāe cāu | tēs ūl | tōrquĕ Că | phāreūs*: *Euboicae* with Eu- long and -bo-i- short, and *Caphareus* with -eus one syllable. This matches the drafter's scansion syllable for syllable. House practice leaves a correct COSTLY fit alone (10.473).

**Unflagged lines that are wrong (12):**
- **Initial Ae- split:** 232 *Aenean* and 282 *Aenean* (cost 1.2), and 289 *Aeneaeque*.
- **Greek eu split:** 279 *Teucris* and 321 *Teucrorum*.
- **Wrong quantities with the right count (cost 0.0 / 1.0):**
  - 251: *Audītīs… plăcĭdō*. The scanner had *Audĭtĭs… plācīdo*.
  - 300: *plācātī ănĭmī*. The scanner had *plăcăti ānīmi*.
  - 302: *Ant(e) ĕquĭdem summā dē rē*, as in 083's 11.111. The scanner had *ēquīdem summă dĕ*.
- **Wrong syllable count or division:**
  - 247: *Ĭāpўgis* has four syllables with a vowel I, as *Iapyge* at 8.710. The scanner read *Ia-* as consonantal and *-bat* as long, and counted 13.
  - 254: *suādet* has two syllables, as at 2.9, 4.81 and 9.340. The scanner read *su-a-det*.
  - 262: *Prōtei* (Πρωτεύς) has a long *Prō-* and *-ei* by synizesis, and *Mĕnĕlāŭs* has four syllables, as at 6.525. The scanner had *Prŏ-tĕ-ī* and *-laus* as one syllable. The count came out the same by accident.
  - 292: *cŏĕant* has its ordinary three syllables (*ōr cŏĕ | ānt īn*), as at 7.317, 7.546 and 8.385. The scanner preferred synizesis (the blind spot noted in conventions), and so did the drafter's note (D4).

**Hand-checked and right:**
- **Names and quantities:**
  - 243 *Dĭŏmēdem* and 226 *Dĭŏmēdis*: no eu here.
  - 265 *Īdŏmĕnei*, with -ei as one syllable. Cost 1.5, but right.
  - 263 *Cȳclōpăs*, Greek accusative plural with short -as. Cost 1.0, right.
  - 326 *Ĭtălō*.
  - 286 *Īnăchias*.
  - 266 *My̆cēnaeus*.
  - 246 *Argy̆rĭpam*.
  - 331 *ōrātōrēs*.
- **Initial Ae- read right by the scanner:** 239 *Aetola*, 263 *Aetnaeos*, 308 *Aetolum*.
- **Consonantal i after a prefix, all right:** 267 *coniugis* and 270 *coniugium* (cost 1.5, right), 230 *Troiano*, 288 *Troiae*, 310 *iaceant*, 327 *iacet*.
- **eu and au:** 297 *ceu*, 273 *heu*, 318 *Aurunci*: all one syllable, right.
- **Elision:** 233 *dĕum* has two syllables (no synizesis). 278 *m(e) ad* gives 13 syllables, right. 275 *ade(o) ex* is right. 288 *cessat(um) est* and 313 *certat(um) est* are prodelision, which the scanner renders as elision with the same count (house practice, 7.263).
- **Hiatus:** none in the part.
- **Cosmetic only:** the caesura placement at 265. No entry.

| key | reason (short) |
|---|---|
| 11.232 | Ae- one syllable, *Aenēān*; 14 |
| 11.247 | *Ĭāpўgis*, four syllables, *-băt* short; 14 |
| 11.251 | *Audītīs*, *plăcĭdō*; 14 |
| 11.254 | *suādet* two syllables; 15 |
| 11.262 | *Prōtei* (-ei synizesis), *Mĕnĕlāŭs*; 15 |
| 11.279 | *Teu-*; 14 |
| 11.282 | Ae-; 15 |
| 11.289 | Ae-, *Grāium*; 15 |
| 11.292 | *cŏĕant* three syllables; 16 |
| 11.300 | *plācātī ănĭmī*; 15 |
| 11.302 | *ĕquĭdem*, *summā dē*; 15 |
| 11.308 | carrier for 309; scanner right; 14 |
| 11.309 | flagged UNRESOLVED; elided *qu(am)*; 16 |
| 11.321 | *Teu-*; 15 |

## Changes

**Major (scansion, scan-fixes.json only)**
- **M1.** Initial Ae- was split at 232, 282 and 289. None was flagged.
- **M2.** *Teucris/Teucrorum* had the eu split at 279 and 321. Neither was flagged.
- **M3.** Wrong quantities with the right count at 251, 300 and 302. None was flagged.
- **M4.** Wrong syllable count or division at 247 (*Iapygis*), 254 (*suadet*), 262 (*Protei Menelaus*) and 292 (*coeant*). None was flagged.
- **M5.** 309 was unresolved (flagged). It is now fixed, with a carrier entry for 308.

**Medium**
- **D1. Unit 232–233, `l`.** "and of the mound before his eyes the fresh ones" made *tumuli* a genitive. It is nominative plural, the second subject of *admonet*, as the note says. Now "and the mounds before his eyes, fresh ones."
- **D2. Unit 268, `l` and note.**
  - `l` "conquered Asia lay in wait for the adulterer" reversed subject and object (*adulter* is the subject). Now "for conquered Asia lay in wait the adulterer."
  - The note's "the adulterer… took the victory from it [Asia]" is now "lay in wait for its conqueror".
  - "Some editors read 'possedit'" (unchecked, from memory) is now "Some texts are said to read".
- **D3. Unit 296–297, note, `l` and `i`.**
  - The note said "'turbata'… agrees with 'fremor'". *turbata* is neuter plural and goes with *ora* (*fremor* is masculine; the metre has short final -ă). Corrected.
  - `l` "troubled, roaring" is now "troubled ones, a roar".
  - `i` "a confused murmur of alarm ran from mouth to mouth" is now "a confused murmur passed from one troubled mouth to the next".
  - *Ausonidum* is now glossed as the old -um for -arum.
- **D4. Unit 292–293, note.** "'Coeant' is two syllables in the verse, 'coe-' read as one" was wrong: it has its ordinary three syllables (see M4). Corrected.
- **D5. Unit 264–265, note.** Neoptolemus was "killed by Orestes at Delphi" with the citation III.325–336. Virgil has Orestes cut him down *patrias… ad aras* (III.332, checked in the source). Delphi is another version. Now cites III.330–332 and III.333–336.
- **D6. Unit 275–277, note.** "'caelestia corpora'… the poetic plural for Venus alone" is not safe, because in Iliad 5 Diomedes wounds Ares too. Now "a generalising plural: in Iliad 5 he wounded Ares as well, though only Venus is named here."
- **D7. Unit 243–245, note.** "'Diomedem', Greek accusative" was a false label. *Diomedem* is the Latin third-declension form. Corrected.
- **D8. Speech marks, units 252–254, 293 and 294–295 (`l`, `i`, notes).**
  - Greenough prints a second “ at 252 inside Venulus's speech, and one ” at 295. Diomedes' words end at 293 (*cavete*): *rex optime, regis… audisti* is Venulus to Latinus. The drafter's claim is right.
  - The drafter followed the print (“ “ ” in `l` and `i`). I applied the house handling of the soothsayer inside Evander's speech (8.499–503, aeneid-061, QUESTIONS item 55). In `l` and `i`, Diomedes' words now stand in single marks, ‘ at 252 and ’ after *cavete* at 293.
  - The notes at 252, 293 and 294 say so. This is not a 5b misprint (no "The print has…" opening): `t` stays as printed, and the validator will still warn 3 “ / 2 ” for `t` only.
  - `l` and `i` now balance.

**Low: notes**
- **L1. 225.** *medio in flagrante tumultu* is now "in the middle of the blazing tumult", all ablative. It had been "the blazing middle".
- **L2. 227.** The note read *nil… valuisse* as "that nothing had availed" and also called *nil* adverbial, which contradicted itself. Now "had availed nothing", with *dona, aurum, preces* as subjects.
- **L3. 241.** *infit* "always introducing speech" is now "regularly".
- **L4. 261–263.** The note said "No elisions". The lines have *Militi(a) ex* and *divers(um) ad*, now listed. Added: *Cyclopas*, Greek accusative plural with short -as (which the metre needs).
- **L5. 271–274.** *petierunt*, "the full perfect", is now "= petiverunt, the perfect in -erunt (not -ere), its e long".
- **L6. 279–280.** Added that *laetor* with the genitive is a poetic extension; it usually takes the ablative.
- **L7. 291.** "most editions put a semicolon there" was unverifiable. Now "editions generally punctuate there".
- **L8. 294–295.** *magno… bello*, "dative… or ablative, 'on the war'": a bare ablative "on" is not a construction. Now "dative of reference, 'regarding the great war'".
- **L9. 297–299.** "Homer's river similes, but no single model" (an assertion) is now "Homer has similes of roaring water like this one, but no single model is certain".
- **L10. 316–317.** *finis super usque Sicanos* had been glossed as "past the boundaries of the Sicanians", which is muddled. Now "beyond the borders, right on to the Sicanians". The note gives *super* after its noun, and the alternative of *Sicanos* taken with *finis*. The matching `i` is L22.
- **L11. 326–329.** "no stops after 'navis' or 'materies'": *materies* has a comma. Now "no mark after 'navis' and only a comma after 'materies'".

**Low: `l` construal and layout**
- **L12. 251.** "with calm thus returned from mouth" read as if *ab ore*. Now "with calm, thus gave back, mouth".
- **L13. 265.** "Of Libya on the shore" read *Libycone* as a genitive. Now "On the Libyan, living, shore, the Locrians?"
- **L14. 266.** "of the great leader of the Achaeans" gave *magnorum* to the leader. Now "of the great, the leader, Achaeans".
- **L15. 270.** `l` ended "!" where `t` and the note have a question. Now "?".
- **L16. 279.** "any after the overthrown war" is now "any, after overthrown, war".
- **L17. 301.** "the king begins high" is now "the king begins, high".
- **L18. 306.** "whom no weary / battles" read *weary* as an adjective. Now "whom no wear out / battles".

**Low: `i` accuracy and echo recasts**
- **L19. 279–280.** "I take no pleasure in remembering the evils of the past" dropped *memini* as a verb of its own. Now "the evils of the past I neither dwell on nor delight in".
- **L20. 288–290.** "victory was held fast" could read as "held firm". *haesit* means it stuck. Now "was held up".
- **L21. 305.** *importunum*, "ill-starred" (unlucky), is now "ill-timed", matching the note.
- **L22. 316–317.** "beyond the borders of the Sicanians" is now "past the borders and on as far as the Sicanians" (with L10).
- **L23. 309.** "Each man must be his own hope" is a remembered stock phrasing. Now "Each of you has only himself to hope in".

## Refused or upheld without change

1. **236 `olli`, lowercase after a stop.** Upheld as a rule-5b misprint (the note opens "The print has…"), as at 11.220 in 083, under open QUESTIONS item 43.
2. **291, 326 and 328: possibly dropped punctuation.** Not fixed under rule 5. The printed Greenough cannot be seen here (the Perseus TEI is the only copy), and the variants file records only word differences. `t` is as printed, `l` and `i` punctuate by sense, and the notes say so (softened in L7 and L11). Goes to QUESTIONS.
3. **268 `subsedit`.** Kept. It construes, and the Latin Library agrees. The note's variant claim is softened (D2).
4. **260 COSTLY.** No entry: the scanner is right.
5. **The drafter's proposed scansion of 292 (*coe-* as one syllable).** Overruled (M4, D4).
6. **243–245 `Diomedem`, scansion.** No entry: the scanner is right.
7. **251 *Auditis* as an ablative absolute with the noun understood.** Upheld.
8. **261 *abacti*, plural with the singular verbs, the Greeks distributed.** Upheld.
9. **264 *referam* as a deliberative subjunctive.** Upheld. The future indicative is possible, but the question favours the subjunctive.
10. **310–311 construal (*cetera… omnia* with the indirect question).** Upheld. The note says how it is taken.
11. **241 *linguis* as a dative.** Upheld.
12. **283–284 *quantus… adsurgat* as an indirect question or exclamation.** Upheld.
13. **`i` at 283 "believe me, who have tried it".** Kept. It is the Latin itself (*experto credite*), not a borrowed phrasing.
14. **New house renderings: none.** Upheld. *experto credite* is proverbial, but it is not a set piece.
15. **`about` "Ajax drowned off Caphareus".** Loose. Virgil (I.44–45) has Minerva strike Ajax with lightning and impale him on a rock, and the text here names no one. The reviewer may edit only `l`, `i` and `n`. If the orchestrator wants it tightened: "the fleet wrecked on the Euboean rocks and Caphareus".

## Cross-references

**Checked in the pinned source:**
- VIII.9: Venulus sent to Diomedes.
- VII.591–600: Latinus gives up the reins.
- VIII.319–325: Saturn.
- I.39–45: Ajax son of Oileus.
- I.99–101: Simois.
- III.121–122: Idomeneus.
- III.330–336: Neoptolemus (D5).
- III.588ff: the Cyclopes.
- I.10: *insignem pietate*.
- I.37: *haec secum*.
- I.5: *dum conderet urbem*.
- XI.100–101: *oratores*, olive branches.
- XI.215–219.

All right after D5.

**Unchecked, from memory, and plausible (kept, stated plainly):**
- Iliad 5: Diomedes fights Aeneas with the stone, and wounds Aphrodite and Ares.
- Iliad 6: Hector and Aeneas as the best of the Trojans.
- Odyssey 4, 9 and 11; Aeschylus's Agamemnon.
- Ovid, Metamorphoses 14 (the birds of Diomedes).
- Nauplius and the false beacons; Idomeneus's vow; the Locrians in Libya; Aegiale.
- Argyripa as Argos Hippion, later Arpi.
- The Sicani in early Latium.
- *pacem petendum* as a Lucretian construction.

## For the owner / QUESTIONS.md

- **Rule-5b misprint.** 11.236 `olli`, lowercase after the full stop ending 235 (item 43 pattern). The publishing run should add the entry.
- **Possibly dropped punctuation, not fixed.** 11.291 (after `armis`), 11.326 (after `navis`) and 11.328 (`materies,`). If the printed Greenough has the marks, rule 5 applies: add them to the source and re-pin aeneid-084. The notes at 291 and 326 would then need their "the print has no…" sentences removed.
- **Nested speech, 252–295.** The print has two “ and one ”. `l` and `i` give Diomedes' words in single marks closed at 293 (the 8.499–503 handling), and the validator warns 3 “ / 2 ” for `t` only. If you prefer the drafter's handling (follow the print), only units 252, 293 and 294 change.
- **Doubtful reading kept.** 11.268 `subsedit` (variant `possedit`, unchecked).
- **`about`.** "Ajax drowned off Caphareus" is loose (refused item 15). The orchestrator may tighten it.
- **Build.** Not run. Build from `units.json` as it stands, and do not rerun `make_units.py`.
