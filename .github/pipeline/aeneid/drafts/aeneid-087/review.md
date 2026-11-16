# Review — aeneid-087 (Aeneid XI.532–647), adversarial reviewer

**Severity counts: major 7 (scansion: 11 wrong lines, among them the hypermetric 609 that would have stopped the build), medium 6, low 17. Refused or upheld without change: 24. Scan-fixes entries added: 13 (11.540, 11.550, 11.583, 11.585, 11.608, 11.609, 11.610, 11.619, 11.620, 11.640, 11.642, 11.643, 11.644).**

**Decision for the owner (D1):** I did not uphold the drafter's reading of the marks at 537 and 584 as rule-5b misprints. They are the print's own division of the passage, which is doubtful, so the print's marks are kept (see D1). This changes `l`/`i` marks in units 535, 557, 559 and 584, and the notes of eight units.

## How the review was done

**Pass 1** went through all 57 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference;
- the speech marks;
- the Latin Library variants;
- the `p` flags (532 and 597 only, which is right).

**Sources.** I used the Latin, the pinned source and memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). No translation was opened.

**Pass 2:**
- I re-read every field that pass 1 changed (37 fields and `about`). Four of my own wordings were fixed: 625's note said 'with its wave' twice; 644's `l`/`i` said "driven" twice; 640's note had an apposition that did not parse.
- I re-read every `l` for misattached words, which gave L14–L18.
- I re-read every `i` for distinctive remembered phrasing. None needed a recast. The simile (624–628), the prayer and the closing 647 are plain and built from the Latin.
- I restored the drafter's file and ran `review_edits.py` once from it: 46 replacements in `l`/`i`/`n` plus one in `about`, each old string asserted to occur exactly once.

**Files and checks:**
- **`units.json`** was edited only by `drafts/aeneid-087/review_edits.py`, written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically first.
  - `t`, `ln`, `p`, `v`, `title`, `titleEn` and `part` are unchanged, which the script asserts.
  - `about` changed in one sentence, "She tells the story." → "Then comes Camilla's story." (D1).
- **`make_units.py` was not touched or rerun.** It still holds the drafter's strings and EXEMPT {537, 557, 559, 584}, so build from `units.json` as it stands.
- **`drafts/aeneid-087/review_check.py`** (086's, adapted) runs `make_units.py`'s checks against the edited file. The settings are now EXEMPT {535, 537} and NOTE_MARKS {535}.
  - It also holds a replica of the build's per-unit checks (tiling, `ln`, `p`, five lines, ending). Result: **BUILD REPLICA: OK**.
  - Notes run 38–130 words.
  - `t`, `l` and `i` each have 3 “ and 3 ”, so the validator should not warn on marks.
- **`scan-fixes.json`** was appended to by `drafts/aeneid-087/add_scan_fixes.py` (086's script with this part's `NEW` table). Each entry is checked against:
  - the build's word-match rule;
  - the validator's metre rule;
  - the syllable count in its `why`.

  The earlier 1034 entries are unchanged and in order, and there are now 1047.
- **`drafts/aeneid-087/scan_check.py`** (086's replica). With the fixes applied it gives:
  - `sc` on all 57 units;
  - no metre failures;
  - no misaligned units;
  - no report lines left.
- **Build not run.**

## Scansion

I hand-scanned all 116 lines and compared each one syllable by syllable with the scanner's fit. The scanner returned a fit for 115 lines; 609 was UNRESOLVED.

**Wrong, not flagged (8):**
- **540** *Prīverno antīquā Mĕtăbus*: the scanner had *an-tĭ-quă* and *Mē-tā*. The true scansion is *Prī-ver | n(o) an-tī | quā Mĕ-tă | bus c(um) ex | cē-dĕ-rĕt | ur-be* (564 *At Mĕtăbus* the scanner gets right).
- **550** *cārōque ŏnĕrī*: the scanner had *că-rŏ* and *ō-nē*.
- **583** *aeternum tēlōrum… virgĭnĭtātis*: the scanner made *te-lo* short and *-gi-ni-* long. *aeternum* is not elided before *t-*.
- **585** *Teucros*: the eu was split (16 syllables for 15), and to fit, *tālī* was made short-short and *la-* long.
- **620** *Trōĕs*: the scanner ran it into one syllable and lengthened *ă-gunt* (13 syllables for 14).
- **642** *dē-ĭ-cĭt*: the scanner read *dei-* as one syllable and made *-cit* long before a vowel (as 8.428, 10.753).
- **643** *nūdīque ŭmĕrī*: the scanner had the quantities reversed.
- **644** *huic*: the scanner split it into *hŭ-ĭc* (16 syllables for 15). In Virgil huic is one syllable (5.849, 8.631, and 554 here).

**Flagged:**
- **609 (UNRESOLVED), hypermetric.** The *-que* of *furentisque* elides into *exhortantur*: *sub-stĭ-tĕ | rat sŭ-bĭ | t(o) ē-rum | punt clā | mō-rĕ fŭ | ren-tīs(que)*. The entry follows the 4.558/8.228/9.650/10.895 format (`6ren–tis×que`).
  - **Carriers.** 608 and 610 share units with 609 (608–609 *substiterat:*; 609–610 *exhortantur equos;*). Both are correct on the scanner's own fit, and both are entered so those units receive `sc`.
  - **Without these entries the build would have refused the part.**
- **619 COSTLY, right.** The scansion is *rē-ĭ-cĭ | unt par | mās ĕt ĕ | quōs ad | moe-nĭ-ă | ver-tunt*. *reiciunt* has four syllables with a long *re-* (as *reice*, Ecl. 3.96; *proicis*, 11.361). It is entered only to clear the flag, as 7.208 and 9.811 were.
- **640 COSTLY, wrong.** *Iollan* has three syllables, with a vowel I (Iollas at Eclogues 2.57, 3.76, from memory). *Cātillus* has a long first syllable: it opens VII.672 *Catillusque acerque Coras* (checked). The true scansion is *vol-vĭ-tŭr | il-l(e) ex | cus-sŭs hŭ | mī Cā | tĭl-lŭs Ĭ | ol-lan*. The scanner made *Iol-* one syllable.

**Hand-checked and right:**
- **Greek and unusual names:**
  - 532 *Opim*;
  - 534, 557 *Lātōnia*;
  - 543 *Casmillae*;
  - 547 *Ămăsēnus*;
  - 564 *Mĕtăbus*;
  - 566 *Trĭviae* (*grā-mĭ-nĕ-ō* four syllables);
  - 580 *Strymŏniamque*;
  - 581 *Tyrrhēna*;
  - 582 *Dĭāna* (*sōlā* is ablative, long, which confirms the note);
  - 592 *Trōs Ĭtălusque* (the short I is forced);
  - 603 *Messāpus*;
  - 604 *Cŏrās*;
  - 612 *Tyrrhēnus*;
  - 612 and 615 *Aconteus*, with the final *-eus* one syllable at line end (the scanner is right);
  - 620 *Ăsīlas* (as X.175, checked);
  - 636 *Orsĭlŏchus Rĕmŭli*;
  - 642 *Herminium*.
- **Consonantal i after a prefix:**
  - 580 *dē-iē-cit*;
  - 625 *sŭ-pĕr-iă-cit* (*per* long by position);
  - 630 *rē-iec-ti*.

  *conixi* (613) is *cō-nī-xi*, from *cōnītor*, with no prefix-i; the scanner is right.
- **Synizesis:** 635 *sēm-yă-nĭ-mēs*, four syllables (the scanner and the note agree).
- **Others:**
  - No hiatus in the part.
  - 538 *vēnit* is perfect: the first foot needs the long syllable (this fed D2).
  - 563 *fŭgit* present.
  - 586 *mihī*.
  - 611 *ob-tēx-* (long by position).
  - 627 *rē-tr(o)*.
  - 632 *lēgit* perfect (forced).
  - 588 *abere* is scanned as printed (*ā-bĕ-rĕ*) with *lābere*'s quantities, so no entry is needed.

| key | reason (short) |
|---|---|
| 11.540 | *antīquā*, *Mĕtăbus*; 14 |
| 11.550 | *cārō*, *ŏnĕrī*; 15 |
| 11.583 | *tēlōrum*, *virgĭnĭtātis*; 14 |
| 11.585 | *Teu-*; 15 |
| 11.608 | carrier for 609 (scanner's fit); 13 |
| 11.609 | hypermetric *furentisque*; 15 counted |
| 11.610 | carrier for 609 (scanner's fit); 15 |
| 11.619 | COSTLY confirmed, *rē-ĭ-cĭ-unt*; 15 |
| 11.620 | *Trō-ĕs*, *ăgunt*; 14 |
| 11.640 | *Ĭ-ol-lan*, *Cātillus*; 15 |
| 11.642 | *dē-ĭ-cĭt*; 15 |
| 11.643 | *nūdī*, *ŭmĕrī*; 15 |
| 11.644 | *huic* one syllable; 15 |

## Changes

**Major (scansion, scan-fixes.json only)**
- **M1.** Wrong quantities with the right count at 540, 550, 583 and 643 (not flagged).
- **M2.** *Teucros* had the eu split at 585 (not flagged).
- **M3.** *Troes* was one syllable at 620 (not flagged).
- **M4.** *deicit* was two syllables at 642 (not flagged).
- **M5.** *huic* was two syllables at 644 (not flagged).
- **M6.** The hypermetric 609, with carriers 608 and 610. Unresolved, it would have stopped the build.
- **M7.** *Iollan*/*Catillus* at 640.

(The 619 entry only clears the flag.)

**Medium**
- **D1. Speech marks at 537 and 584: not misprints, but the print's division (doubtful, kept).** The drafter read 535–594 as one unbroken speech. He treated `alias. ”Neque` (537) and `colit. “Vellem` (584) as stray marks under rule 5b and gave Metabus's prayer single marks.
  - **Why the marks are not stray.** `archive_aeneid.py` writes ” before the rest of the line wherever a TEI `</q>` closes mid-line. That is exactly the `vale. ”Nec` pattern of 11.98 and the others in QUESTIONS 55–64. So the source does close Diana's speech after *alias* and reopen it before *Vellem*: two coordinated marks, not one stray one. On that pointing, 537–584 is the poet's own account of Camilla's childhood, and the prayer is an ordinary speech.
  - **The print construes.** *Dianae* in the third person suits the narrator, and *Dixit* (561) is the narrator's usual close. *Vellem* resuming Diana's words is abrupt but clear.
  - **The usual reading is also good.** *enim* and *iste* sound like speech, gods name themselves, and 586 *cara mihi* picks up 537.
  - **What rule 5b allows.** It excludes doubtful readings ("where more than one reading is possible… keep the print and say so"), and QUESTIONS 59 kept 9.146's mark as doubtful on the same grounds.
  - **What changed.** Only the spacing of `”Neque` is corrected, as at 11.98. `l`/`i` now:
    - close Diana's words after "others.” (535–537);
    - leave 537–584 unmarked;
    - give the prayer “ ” (557, 559);
    - reopen at “I would/could wish (584).

    The notes were rewritten accordingly:
    - 535 opens "The print has 'alias. ”Neque'… corrected here" and gives both readings;
    - 537 says the mark belongs to the previous unit and sets out the case for Diana speaking throughout;
    - 556, 557, 559, 562 ("Diana's pity" → "pity"), 582 and 584 were adjusted.

    In 537 `l`/`i`, "my heart" became "her heart". `about` was adjusted as above.
  - **If the owner prefers the drafter's reading,** these notes' openings and the marks in units 535, 537, 557, 559 and 584 revert. Every other change stands.
- **D2. 537, `n` and `l`.** *venit* is perfect: the metre needs the long *vē-* of the first foot. The note now says so, and `l` "comes love" is now "has come love".
- **D3. 644–645, `n`, `l`, `i`.** "'transfixa', 'having transfixed'" gave an active sense to a perfect passive participle. The note now reads "perfect passive participle agreeing with 'hasta', 'driven right through' him":
  - `l`: "piercing him" → "thrust through";
  - `i`: "having pierced him through" → "passing clean through".
- **D4. 640–643, `n`.** "the repetition with change of reference" was false: both *ingentem* are Herminius. The note now says "both of Herminius, the adjective repeated at the head of each phrase".
- **D5. 612–615, `i`.** "were the first to fall with a mighty crash" rendered the Latin Library's *ruinam dant* ('make a fall'), not the print's *ruina… dant sonitum ingenti*. `i` now reads "were the first to raise a din, crashing down mightily". The note already keeps the print and gives the variant.
- **D6. 552–555, `n`.** "the object is put first… then resumed" mislabelled *Telum*. It is the antecedent drawn into the relative clause as the object of *gerebat*, then picked up by *huic… hastae*. The note is now corrected.

**Low: notes**
- **L1. 532.** "'Opim', Greek-style accusative" is now "accusative… in '-im' as Latin often gives Greek names in '-is'" (the Greek would be *-in*).
- **L2. 532.** "imperfects: she was speaking when the battle began below" is now "imperfects that set the scene, 'interea', while Turnus lies in wait". The battle begins only at 597.
- **L3. 534.** *tristis* could also be nominative with *Latonia*. The note now says so.
- **L4. 547.** "'abundans', literally 'over-wave-ing'" is now "from 'ab' and 'unda', 'streaming off in waves'".
- **L5. 569.** "the 'et' postponed" was wrong: *et* joins *pastorum* and *solis* in place.
- **L6. 569.** "keeping the early '-om' after 'v' as in… 'volnus'" is now "the early 'o'".
- **L7. 603.** "the Etruscan-born horse-tamer of VII.691" is now "the horse-tamer, son of Neptune" (VII.691 *Neptunia proles*, checked).
- **L8. 640.** "one of the twin founders of Tibur" is now "twin brother of Coras (Argive warriors from Tibur, VII.670–672)", as 086 corrected. Added: *Cātillus* has a long first syllable (VII.672).
- **L9. 640–642.** Added the syllable counts *I-ol-lan* (three) and *dē-i-cit* (three).
- **L10. 633.** "the verb for the groans is supplied from 'surgit'" is now "'gemitus' shares 'volvuntur'… a bold zeugma; some supply 'rise' instead". *surgit* is singular with *pugna*.
- **L11. 632.** Added *lēgit*, perfect, forced by the metre.
- **L12. 620.** Added *Trō-es*, two syllables. "in Book X" is now "(X.175)" (checked).
- **L13. 624.** The rule-5b note now adds the Latin Library's reading. It also says why the nominative cannot stand: there would be no object for *superiacit*, and the crag would be the thrower.

**Low: `l`**
- **L14. 539.** "from his kingdom and his proud strength" attached *vires* to *regno*. Now "from his kingdom, and of his proud strength" (both governed by *ob*).
- **L15. 609.** "and frenzied / they urge on their horses" attached *furentis* to the riders. Now "and the raging / they urge on, horses".
- **L16. 615–617.** "hurls headlong" read *praecipitat* as transitive. Now "plunges headlong".
- **L17. 625, 631.**
  - 625: "over the rocks throws its wave" made *unda* the object. Now "the rocks overtops with its wave".
  - 631: "into battles whole" attached *totas* to *proelia*. Now "into battles, the whole / … lines".

## Refused or upheld without change

1. **588 `abere` → `labere` (rule 5b).** Upheld. *abere* is no Latin form, *abeo*'s imperative being *abi*. *lābere* is the only reading the sense and metre allow, it is answered by *delapsa* (595), and the Latin Library has it.
2. **625 `scopulusque` → `scopulosque` (rule 5b), judged strictly.** Upheld.
   - *superiacio* is transitive ('throw over, overtop') and needs an object.
   - *unda* cannot be the object. If nominative, it would be a third subject beside *pontus*, with *spumeus* masculine.
   - A nominative *scopulus* would have to be a second subject with *pontus*: "and the crag, foaming, throws [nothing] over with the wave". That does not construe, and a rock does not throw the sea.
   - No reading of the printed form gives sense. The correction is one letter, and the Latin Library has *scopulosque*.
   - Note strengthened (L13).
3. **613–614 *ruina… dant sonitum ingenti*, kept as printed.** Upheld: "with a huge crash they make a sound" construes, and the variant is mentioned. The `i` fix is D5.
4. **630 subject of *bis reiecti*: the Etruscans.** Upheld.
   - The two *bis* clauses answer the simile's flow and ebb.
   - 621–623 has the Trojan side fleeing after the Latins rally.
   - *respectant terga tegentes* describes the fleeing side.
   - Taking it of the Rutulians would repeat 629.

   The note gives the alternative. *armis* is taken with *tegentes*; a link with *reiecti* ('thrown back by arms') is also possible and is left unstated.
5. **612 *Tyrrhenus* as a proper name.** Upheld.
6. **641–643 *cui* with a supplied 'had'.** Upheld.
7. **535–537 *cingitur*, middle.** Upheld.
8. **539 *viresque* / *uirisque*, 569 *aevom*, 591 *volnere*, 614 *quadrupedantum*, 626 *arenam*.** Orthography or morphology, and the treatment is right.
9. **552–555 described as a loose but vivid order.** Kept; only the label changed (D6).
10. **Scanner right, no correction needed:** 612 and 615 *Aconteus*; 613 *conixi*; 580 *deiecit*; 625 *superiacit*; 630 *reiecti*; 635 *semianimes*; 592 *Ĭtalus*; 611 *obtexitur*; 627 *retro*. (619 *reiciunt* is right too, but it has an entry only to clear its COSTLY flag.)
11. **588 sc.** The scanner's fit of the printed *abere* already has *lābere*'s quantities.
12. **590 'Diana hands Opis her bow and quiver' for *Haec cape*.** Plausible (*haec* is neuter plural, 'these things'). Kept.
13. **591 *violarit* as future perfect.** Kept. A perfect subjunctive is also possible after *quicumque*, and the sense is the same.
14. **586 *foret* as "the apodosis of the wish".** Loose, but defensible. Kept.
15. **609 note, "This 'hypermetric' line is rare in Virgil".** Kept (about twenty instances).
16. **Attributions from memory, all kept and all plausible:**
    - Servius on *Casmilla*/*camilla*;
    - Sarpedon carried home by Sleep and Death (Iliad XVI, "a scene Virgil may have in mind");
    - missiles like snow in the Iliad (no line cited);
    - the she-wolf parallel;
    - Strymonian cranes.
17. **Cross-references checked in the source:**
    - VII.670–672;
    - VII.691;
    - X.175;
    - XI.836 *Opis*;
    - XI.690 (Orsilochus later killed by Camilla, so on the Trojan side, as the note says).
18. **`i` echoes.** None distinctive enough to recast.
19. **Advisory: none.** Upheld; ordinary battle killing.
20. **New renderings: none.** Upheld.
21. **`p` flags at 532 and 597.** Right.
22. **Elision lists.** All 57 were checked against the hand scansion and all are complete. Two examples: 583 *aeternum telorum* is rightly not elided, and 554 *natam, libro* rightly not either.
23. **Note on 586 "she is dear now and will soon be lost".** Kept.
24. **The 588 rule-5b note's opening formula.** Kept as written.

## For the owner / QUESTIONS.md

- **D1, speech marks 11.537/584.**
  - The print (TEI `</q>` after *alias*, `<q>` before *Vellem*) gives 537–584 to the narrator. The drafter treated both marks as rule-5b misprints so that Diana speaks without a break to 594.
  - The reviewer ruled the print a doubtful but construable division. Under rule 5b it is kept: `l`/`i` follow the print's marks, only the `”Neque` spacing is corrected (as 11.98), and the notes give both readings.
  - **Please rule.** If the owner wants Diana's unbroken speech, revert the mark changes in units 535, 537, 557, 559 and 584 and their note openings.
- **Rule-5b misprints:**
  - 11.588 `abere` (read *labere*);
  - 11.625 `scopulusque` (read *scopulosque*);
  - 11.537 `alias. ”Neque` (spacing).
- **Kept as printed, variant noted for sense:** 11.613–614 *ruina… sonitum* (LL *ruinam… sonitu*).
- **Scansion:**
  - 11.609 is hypermetric (*furentisque* elides into *exhortantur*). Check that the audio elides it.
  - 11.640 rests on two points: *Iollan* as three syllables (from Eclogues 2.57 and 3.76, from memory) and *Cātillus* long (VII.672, checked).
  - 11.619 is entered only to clear a COSTLY flag.
- **Build.** Build from `units.json` as it stands. `make_units.py` still has the drafter's strings and EXEMPT and must not be rerun.
