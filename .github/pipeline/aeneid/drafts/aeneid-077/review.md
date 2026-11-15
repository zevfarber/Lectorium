# Review — aeneid-077 (Aeneid X.439–509), adversarial reviewer

**Severity counts: major 4, medium 4, low 22 (17 in pass 1, 5 in pass 2). Refused or upheld-without-change findings: 11. Scan-fixes entries added: 5 (2 wrong full lines, 1 half-line, 2 carriers).**

Majors: 1 note error (472 *pervenit*) and 3 scansion entries (453, 486, 490).

## How the review was done

**Pass 1** covered all 36 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. All 36 elision lists are right. I also checked:
- the speech marks (441–443, 449–451, 460–463, 467–472, 481, 491–495): six openings and six closings in `t`, `l` and `i` alike. Two of the closings are the rule-5b pairs 449/451 and 494/495.
- the Latin Library variants (458, 470, 481, 486, 488). All are orthographic, and none needs a note beyond the ones already there.
- `about`, `title`, `part` and `titleEn`

I read every `i` for echoes of the well-known English versions and recast four: 467–469a, 501–502, 503–505a and 507–509.

Sources: the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

**Cross-references checked in the pinned source:**
- X.399 (*biiugis*)
- X.411 (the apostrophe *Palla*)
- X.414 (*fulgenti deripit ense*)
- X.433–438 (Pallas and Lausus kept apart; 438 is the poet speaking)
- Greenough's spelling of the name: he prints both *Euandr-* and *Evandr-*, so "Greenough's spelling here" at 492 is accurate.

**Pass 2** re-read every edited field in full and re-checked:
- the speech marks: six “ and six ” in each of `t`, `l` and `i`
- line counts: `l` has the same number of lines as `t` in every unit, and no `i` has a line break
- note lengths: 41–114 words

It made changes P2-1 to P2-5.

**Scansion.** I hand-scanned all 71 lines and compared them syllable by syllable with the scanner, run in-process the way the build calls it. The helper is `drafts/aeneid-077/scan_check.py` (076's, with the part id changed).
- **Packet flags:**
  - **453 (COSTLY 2.5) is wrong.** The scanner ran *bi-iu* into one syllable (15). Right: Dē-sĭ-lŭ | ĭt Tūr | nūs bĭ-jŭ | gīs pĕ-dĕs | ap-pă-răt | ī-re (16), with *pedes* the nominative *pĕdĕs*.
  - **473 (COSTLY 2.3) is right**, and no entry was added. *reicit* has three syllables with the first long: Sīc ă-ĭt | āt-qu(e) ŏ-cŭ | lōs Rŭ-tŭ | lō-rūm | rē-ĭ-cĭt | ar-vis. Two syllables cannot work: *rei-cit ar-* would put the long *tar* in the fifth foot. The cost comes only from the long *rē* before a vowel.
  - **490 (UNRESOLVED) is a half-line.** It is handled as 075 handled 284: Quēm Tūr | nūs sŭ-pĕr | ād-sīs | tēns (8 syllables), with the half-line rule.
- **Carriers.** 491 and 492 share unit 490–492a with the half-line, and the scanner is right on both. 491 has 16 syllables, with *Arcadĕs*. 492 has 14, with *Euandro* (Greek eu as one long syllable). As at 284–286, the unit would otherwise get no `sc`. Unit 492b–492 got `sc` even without the entries, but the 492 entry is needed for unit 490–492a.
- **One unflagged line is wrong:** 486 (cost 0.0). The scanner had *cā-lī-* long-long and *-tră dĕ* short-short. Right: Il-lĕ ră | pĭt că-lĭ | dūm frūs | trā dē | vol-nĕ-rĕ | tē-lum (15).
- **Checked and right as the scanner reads them:**
  - *Euandro* 492 and *Eurytides* 499 (Eu- one syllable; *Eu-ry-tī-dēs* is –⏑⏑–, with the short patronymic *-ĭ-*)
  - *Aeneia* 494 (*Ae-nē-ĭ-ă*, four syllables) and *aethera* 459
  - *adiuvet* 458 (consonantal i after the prefix) and *iugali* 497
  - *Alcide* 461 and *Alcides* 464 (*Al-cī-dē(s)*), *Sarpedon* 471 (*Sar-pē-dōn*), *Clonus* 499 (*Clŏ-*)
  - *Pallanta* (short final -ă, five times) and *semineci* 462 (*sē-mĭ-nĕ-cī*)
  - *siqua* 458: *quā* is the long adverb, which the metre requires. This is the scanner's 1.5 cost.
  - *cuique* 467 (*cui* one syllable)
  - *baltei* 496 (synizesis)
  - *sanguis* 487: the last syllable is long, which the metre requires in the fourth foot
  - *pervēnit* 472 (long ē). This is the basis of M1.
  - *vāgīnā* 475, *Troiae* 469
  - *leō* 454, *contrā* 448, *frūstrā* 486
  - There is no hiatus in the part.

Every entry was checked by `drafts/aeneid-077/add_scan_fixes.py` (076's, with the part id and entries changed; dry run, then `--write`):
- against the build's word-match rule
- against the validator's metre rule (the half-line rule for 490)
- against the syllable count stated in its own `why`

A replica of the build's scansion step, reading `scan-fixes.json`, gives these results:
- all 5 entries apply
- **all 36 units get `sc`**
- no unit's `sc` is out of line with its words
- no line fails the metre check
- the only report left is the correct COSTLY fit at 473

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by `review_edits.py` (pass 1: 25 edits, two of them to `about`) and `review_edits_pass2.py` (pass 2: 5 edits). Each old string was asserted to occur exactly once in its field. The file was written with `aeneid_lib.jdump`; the drafter's file round-tripped byte-identically before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` were checked by script against a copy taken before any edit, and are unchanged in all 36 units. `title`, `titleEn` and `part` are unchanged.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` as it stands and do not rerun `make_units.py`.
- **`scan-fixes.json`.** The change only appends (54 insertions, 0 deletions), with new keys after 10.430 in line order.
- **Build and validator not run.** `build_aeneid.py` has no dry-run or `--help`.

## Changes — pass 1

### Major
- **M1. Note 471b–472, *pervenit*.** The note called it the present ("arrives at… he is already near it"). The metre needs the long *ē* in the fifth foot (*tī pēr | vē-nĭt ăd | ae-vi*), so it is the perfect *pervēnit*. The note now reads "'has arrived at', perfect: the metre needs the long 'e' of 'pervēnit' (the present is 'pervĕnit'). His end is as good as come." `l` ("he has reached") and `i` ("has come to") were already right.
- **M2. 10.453** *biiugis*, the packet flag. See Scansion.
- **M3. 10.486** (unflagged). *călĭdum*, *frūstrā*, *dē*. See Scansion.
- **M4. 10.490**, the half-line, with **carriers 10.491 and 10.492**. See Scansion.

### Medium
- **D1. Note 439–440.** The note said "Jupiter has just said that Pallas and Lausus will fall to greater enemies (438)". 438 is the poet's own forecast (*mox illos sua fata manent maiore sub hoste*), as note 471b–472 itself says. The note also said "Lausus is fighting Pallas", but at 433–438 the two face each other and Jupiter does not let them meet. It now reads "Lausus faces Pallas across the battle (433–434)" and "The poet has just said…" (wording finished in P2-1).
- **D2. Note 462–463.** "'semineci' is from 'semineci-s'" gave a non-existent nominative. It now reads "the dative of 'seminex' (genitive 'seminecis')".
- **D3. Note 473, *reicit arvis* (doubtful reading).** The note argued for "away" because it "fits his grief better", but the grief belongs to Hercules, not Jupiter. The note now says the phrase is read two ways:
  - ablative of separation, "turns away from the fields" (kept in `l`/`i`), like Zeus turning his eyes away at the start of Iliad 13
  - dative, "back onto the fields"

  It ends "The Latin allows both." `l` and `i` are unchanged.
- **D4. Note 507–509.** *dolor atque decus* were called "nominatives in exclamation". They stand in apposition to the vocative *rediture*, and for these nouns the two cases look alike. Corrected. The `i` was also recast (see L16).

### Low
- **L1. `i` 441–443.** *vidit* is "saw", not "reached". It now reads "As soon as he saw his comrades" (*ut* + perfect).
- **L2. Note 445–448.** *tyranni* is the narrator's word, not one "in Pallas's mouth". It now reads "the narrator seeing Turnus as Pallas sees him".
- **L3. `i` 449–451a.** Restored *iam*: "Now I shall be praised…".
- **L4. Note 451b.** "*Fatus*… used with present sense" contradicted its own gloss "having spoken". It now reads "active in meaning like all deponents".
- **L5. Note 453–454a.** *biiugis* was at 399 in the last part, not 400. Added "'bi-' short", to match M2.
- **L6. Note 457–459.** Added "('qua' the adverb, with a long 'a')", which the metre confirms.
- **L7. Note 464–465.** *magnum… gemitum* does not frame "the next line and a half". It now reads "enclosing 'sub imo corde premit'" (merged in P2-2). In Iliad 16.459–461 Zeus lets fall bloody raindrops, not "tears of blood"; corrected.
- **L8. `i` 467–469a (echo).** The old wording opened "Every man has his appointed day", which is close to a familiar published opening. It now reads "For every man his own day stands fixed; for all, life's time is short and cannot be made good once spent; but to stretch one's renown further by deeds is the work that courage has to do." This avoids "lengthen fame by deeds" and "valour's work".
- **L9. `l` 469b–471a.** "Troy beneath the walls high" lost the genitive. It now reads "Of Troy beneath the walls high".
- **L10. Note 474–475.** The *deripit* echo is at 414, not 415. It now quotes *fulgenti deripit ense*, because the whole phrase is echoed.
- **L11. Note 486.** *calidum… telum* does not frame the line, because *Ille rapit* comes first. It now reads "enclosing 'frustra de volnere'".
- **L12. Note 487.** Added that the last syllable of *sanguis* is long here, as the `sc` will show.
- **L13. Note 495b–499.** Hypermestra spared Lynceus, so not all the Danaids killed their husbands. It now reads "all but one" (wording finished in P2-3).
- **L14. `i` 501–502 (echo).** The old wording ("How blind the minds of men are to fate") was close to stock versions, including Dryden's "blind in fate". It now reads "How little the human mind knows of fate and of the lot that is coming, or of holding to the mean when prosperity has carried it aloft!"
- **L15. `i` 503–505a (echo).** "to have left Pallas untouched" is stock. Recast; the wording was finished in P2-4.
- **L16. `i` 507–509 (echo).** The old wording had "his great grief and his great glory… This day, your first, gave you to war… takes you away". It now reads "…his great sorrow and his great pride! This first day of yours gave you to the war, and this same day carries you off, though you leave great heaps of Rutulian dead behind you." The opening was finished in P2-5.
- **L17. `about`.** Two changes:
  - The Jupiter clause was recast away from stock wording ("every man's day is fixed… lengthen one's name").
  - "carry Pallas home" became "carry Pallas back" (*referunt*: they carry him back to the camp, and Book XI takes him home). "taken by it [war]" became "carried off by the same day, his first" (*haec eadem aufert*).

## Changes — pass 2
- **P2-1. Note 439–440.** The pass-1 singular "a greater enemy" no longer agreed with "the first of those enemies". It now reads "will each fall to a greater enemy".
- **P2-2. Note 464–465.** Pass 1 had repeated *sub imo corde premit*; the two glosses are merged.
- **P2-3. Note 495b–499.** The pass-1 wording broke the sentence. It now reads "of the fifty daughters of Danaus, … all but one killed their husbands".
- **P2-4. `i` 503–505a.** "buy back" added a *re-* the Latin lacks (*emptum*). It now reads "when he will wish he could buy Pallas's safety at a great price, and will loathe those spoils and this day."
- **P2-5. `i` 507–509.** *rediture* is future. It now reads "O you who are to go home to your father, his great sorrow and his great pride!"

## Refused or upheld without change
1. **Rule 5b at 451 and 495 (`minas. ”Fatus`, `hospitia. ”Et`). Upheld.**
   - Each first note opens with the required sentence.
   - The stray ” begins the next unit's `t`.
   - `l` and `i` close the speech on the unit ending *minas.* / *hospitia.*
   - The pair balance holds, exactly as in 075 (297/298, 333/335).
2. **473 flagged COSTLY.** The scanner is right, and no entry was added (see Scansion).
3. **`l`/`i` 473 "turns away".** Kept. It is the drafter's choice, and it is now flagged as one of two readings (D3).
4. **Note 444 *aequore iusso*, "ablative of separation… the ground they were ordered to leave".** Upheld. This is the usual reading, and the note gives the literal phrase.
5. **Note 441–443, *pugnae* "dative with 'desisto', a poetic construction".** Upheld.
6. **Note 482–485, *quem… obeat* "the subjunctive giving the clause the force of 'though'".** Upheld; it is a concessive relative.
7. **Note 503–505a, *Turno tempus erit* "dative of possession".** Upheld.
8. **Note 500, *quo… spolio* "the relative attracted into agreement".** Upheld. The antecedent is drawn into the relative clause, and the gloss is right.
9. **Note 490–492a, "more than fifty" half-lines and *inquit* inside the marks.** Upheld, as in 075.
10. **`i` 481, "whether my spear is not the better at piercing".** Kept. The "not" gives the taunt, and *num* in an indirect question is neutral "whether"; the note already gives the literal sense.
11. **Attributions from memory, kept as written.** I am confident of each:
    - Iliad 16.487–489 (lion and bull), 16.431–461, 16.503–504
    - Iliad 7.245–248, 4.504, 2.418, 11.749, 17.198–208
    - Iliad 13.3–4 (added in D3)
    - I.209 and XII.940–952

## Scan-fixes entries added (5)
| key | reason | syllables |
|---|---|---|
| 10.453 | *biiugis*, consonantal i, *bi-* short (COSTLY 2.5) | 16 |
| 10.486 | *călĭdum*, *frūstrā*, *dē* (quantities; cost 0.0, unflagged) | 15 |
| 10.490 | Half-line (UNRESOLVED) | 8 |
| 10.491 | Carrier for 490 (scanner right) | 16 |
| 10.492 | Carrier for 490 (scanner right) | 14 |

## For the owner (QUESTIONS.md)
- **Rule-5b misprints 10.451 and 10.495.** In each the closing ” is printed joined to the next word. The publishing run should add the QUESTIONS.md entry that rule 5b asks for, as for 075's 298 and 335. The reviewer may not touch QUESTIONS.md.
- **10.473 *reicit arvis*.** This is a doubtful reading, not a misprint. The note now gives both readings, and `l`/`i` take "away".
- **Advisory:** none taken. Pallas's death is ordinary battle killing. The Danaid scene on the belt is a killing, told in one line.
