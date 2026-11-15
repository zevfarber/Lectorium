# Review — aeneid-080 (Aeneid X.689–790), adversarial reviewer

**Severity counts: major 5, medium 6, low 21 (18 in pass 1, 3 in pass 2). Refused or upheld-without-change findings: 18. Scan-fixes entries added: 17 (11 wrong full lines, 1 half-line, 1 hypermetric line, 4 carriers).**

All five majors are scansion findings. Four of them are lines the packet did not flag:
- M1: initial Ae- split at 769, 776, 783 and 787.
- M2: Greek eu split at 690.
- M3: wrong syllable count at 705 (*Cisseis*), 712 (*cuiquam*), 745 (*quies*) and 753 (*deicit*).
- M4: wrong quantities with the right count at 724 and 743.

The fifth, M5, covers the two flagged UNRESOLVED lines: the half-line 728 and the hypermetric 781, each entered with carriers for its unit.

## How the review was done

**Pass 1** covered all 38 units word by word. I checked:
- `l`, `i` and `n` against the Latin
- every grammatical label, every "framing" claim and every elision list
- every cross-reference, and every attribution made from memory
- the speech marks, the Latin Library variants, `about`, `title`, `part` and `titleEn`

**Elision lists.** All 38 are right. I checked each line for a vowel or -m before a vowel or h. *Teucrosqu(e) invadit* 690, *ventum (e)st* 710, *nequ(e) his* 757, *morer(e) ast* 743 (across the stop) and *caelumqu(e) aspicit* 781–782 (across the line-end) are all listed.

**Speech marks.** In `t` there are four “ and four ”. Two of the ” are the rule-5b strays at the head of 744 and 776. In `l` and `i` there are four “ and four ”, each speech closed in its own unit. A script asserts this layout.

| speech | opens | closes (`l`, `i`) | `t` closing mark |
|---|---|---|---|
| Mezentius | 737 (unit 736) | 737 | 737 |
| Orodes | 739 | 741 | 741 |
| Mezentius | 743 (unit 742) | 744 *viderit.* | head of unit 744 (misprint) |
| Mezentius | 773 (unit 772) | 776 *Aeneae.* | head of unit 776 (misprint) |

No speech runs across a part boundary.

**Other checks:**
- **About, title, part, titleEn.** All right. *Orodis* is the right genitive of the third-declension *Orodes*.
- **Hiatus.** None.
- **Half-lines and the hypermetric line.** 728 *ora cruor,* is a half-line and 781 is hypermetric; see Scansion.
- **Echoes.** I read every `i` for echoes of the well-known English versions and recast six (E1–E6). These include the four famous places named in the brief: 737, 743–746, the Orion simile and 782.
- **Sources.** The Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

**Cross-references checked in the pinned source:**
- VII.586 *Ille velut pelagi rupes immota resistit*: right.
- **VII.648.** The source prints *contemptor divom*, not *divum*. The note is corrected (P2-3).
- VIII.481–495: Mezentius expelled; right.
- VII.649–654: Lausus; right.
- III.170 *Corythum*: right.
- IV.41 *Numidae infreni*: right.
- VIII.185–275: Evander's story of Hercules and Cacus; right.
- IV.177: the same line as 767, apart from Greenough's comma; right.
- **XII.309–310.** This has *conduntur*, not *clauduntur*, so the two lines are not repeated word for word. The note now says so (P2-2).
- The quantity and scan-fix precedents cited:
  - 1.535 *nimbosus Ŏrīōn*
  - 7.320 *Cisseis* (three syllables)
  - 7.692 *cuiquam*
  - 1.723, 3.495 and 7.598 *quies*
  - 8.428 *deicit*
  - 9.340 *suadet enim vesana fames*, the same half-line as 724
  - 4.558, 5.753, 6.602 and 8.228 (hypermetric)
  - 10.490 and 10.580 (half-lines with carriers)

**Pass 2** re-read every field pass 1 edited, in full, and made P2-1. It then made the two cross-reference corrections, P2-2 and P2-3. It re-checked:
- the speech-mark layout above, asserted by script
- that `l` has as many lines as `t` in every unit, and that no `i` has a line break
- note lengths: 41–138 words, all inside 15–139
- that no unit carries `sc`

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by `review_edits.py` (pass 1, 28 edits) and `review_edits_pass2.py` (pass 2, 3 edits). Each old string was asserted to occur exactly once in its field. Two whole-note replacements (units 742 and 772) are guarded by their opening words. The file was written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically before any edit.
- **Untouched fields.** A copy taken before any edit shows that `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` are unchanged in every unit.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` as it stands and do not rerun `make_units.py`.
- **Build and validator not run** (left to the run).

## Scansion

I hand-scanned all 102 lines and compared them syllable by syllable with the scanner, run in-process the way the build calls it. The helper is `drafts/aeneid-080/scan_check.py` (079's, with the part id changed).

**Packet flags:**
- **696 (COSTLY 2.0): right.** *Hē-brum* is long by position before *br*.
- **749 (COSTLY 2.0): right.** *Lȳ-cā-ŏ-nĭ-um*, with *-que* elided into *Erichaeten*.
- **763 (COSTLY 2.0): right.** *Ŏ-rī-ōn*, as 1.535.
- **764 (COSTLY 2.5): right.** *Nerei* is two syllables, and *mĕdĭī* has a long final i.
- **728 (UNRESOLVED): half-line**, entered with carriers 726, 727 and 729.
- **781 (UNRESOLVED): hypermetric**, entered with carrier 782.

As in 078, no entries were made for the four right COSTLY fits; they stay in the build's printed report.

**Unflagged lines that are wrong (11):**
- **Initial Ae- split (cost 1.2):**
  - 769 *Aeneas*
  - 776 *Aeneae*
  - 783 *Aeneas*
  - 787 *Aeneas*
- **Greek eu split (cost 0.0):** 690 *Teucros*. The scanner made *nae Te-u* a dactyl.
- **Wrong syllable count:**
  - **705 *Cisseis* (cost 1.5).** It is three syllables, Κισσηΐς, as 7.320. The scanner also made *-na* and *Pa-* long. The line is Cis-sē | īs rē | gī-nă Pă | rīn crĕ-ăt | ur-bĕ pă | ter-na.
  - **712 *cuiquam* (cost 0.0).** *cui* is one syllable (as 7.692). The scanner split it into cŭ-ĭ.
  - **745 *quies* (cost 0.0).** *quies* is two syllables, quĭ-ēs, and *dura* has a short final a. The scanner read *quies* as one syllable and made *-ra* long.
  - **753 *deicit* (cost 1.8).** It is dē-ĭ-cĭt, as 8.428. The scanner read *dei-* as one syllable and made *-cit* long before *at*.
- **Wrong quantities with the right count:**
  - **724 (cost 1.5).** This is the same half-line as 9.340: *vēsāna*, *fămēs*.
  - **743 (cost 0.3).** The scanner made *dē* and *mē* short and *pater* long-long. The line is Nunc mŏ-rĕ | r(e) āst dē | mē dī | vōm pă-tĕr | āt-qu(e) hŏ-mĭ | nūm rex.

**Checked and right as the scanner reads them:**
- 702 *Euanthen* and 780 *Euandro*: Greek eu kept whole.
- **722 *coniugis*:** the division *con–iu* is right.
- **736 *abiectum*:** the division *a–biec* is off, but the quantities are right, as 079's R1. No entry.
- **720 *profugus hymenaeos*:** *-gūs* is lengthened in the arsis, the standard account.
- **751 *pĕdĕs*.**
- **755 *luctūs*:** accusative plural.
- **761 *Tīsiphonē*.**
- **780 *Ĭtălā… urbe*:** ablative. This is the only fit; a long Ī leaves none.
- **785 *trānsīt*:** the contracted perfect, which settles D6.
- **Small costs, each the right fit:** 707, 715, 719, 721, 730, 739, 740, 754, 768, 773 and 775.

**How the entries were checked.** Every entry was checked by `drafts/aeneid-080/add_scan_fixes.py` (079's, with the part id and entries changed, and carrier support added: `sc` None takes the scanner's own fit). It ran as a dry run, then `--write`. Each entry was checked:
- against the build's word-match rule
- against the validator's metre rule, or the half-line rule for 728
- against the syllable count stated in its own `why`. For 781 the count is fifteen marked syllables, with the elided *-que* unmarked, as 4.558 and 5.422.

A replica of the build's scansion step, reading `scan-fixes.json`, gives these results:
- all 17 entries apply
- **all 38 units get `sc`**
- no unit's `sc` is out of line with its words
- no line fails the metre check
- the only report left is the four right COSTLY fits

The change to `scan-fixes.json` only appends: 190 insertions, 0 deletions, with the new keys after 10.684 in line order. The file still round-trips through `json.dumps(…, ensure_ascii=False, indent=1)+'\n'`.

## Changes — pass 1

### Major
- **M1. Initial Ae- split, unflagged: 10.769, 776, 783, 787.** See Scansion.
- **M2. Greek eu split, unflagged: 10.690.** See Scansion.
- **M3. Wrong syllable count, unflagged: 10.705, 712, 745, 753.** See Scansion.
- **M4. Wrong quantities with the right count, unflagged: 10.724, 743.** See Scansion.
- **M5. Half-line 10.728 and hypermetric 10.781 (flagged UNRESOLVED).** Both were entered, with carriers 726, 727, 729 and 782; the build would refuse otherwise.

### Medium
- **D1. `l` 707–711.** "in the forest / fed on reeds" made *harundinea* the boar's food. It agrees with *silva*, the reed forest. `l` now reads "in a forest / of reeds having fed".
- **D2. `l` 726–729.** "his cruel, foul, / jaws" put *taeter* on the jaws; it agrees with *cruor*. `l` now reads "washes his ruthless / jaws the foul gore".
- **D3. 736.** *posito pede nixus et hasta*: *nixus* governs both ablatives ("resting on his planted foot and on his spear"). It is not an ablative absolute plus a separate *hasta*. The note, `l` and `i` are all changed.
- **D4. Note 753.** *Thronium Salius Saliumque Nealces* runs object, subject, object, subject. That is parallel order, not chiasmus. The note now describes the name set twice side by side, nominative then accusative.
- **D5. Note 763–767.** *Nerei* is not a Greek genitive; the Greek would be *Nereos*. It is the genitive of *Nereus*, scanned as two syllables. The note is corrected.
- **D6. Note 783–786.** The metre needs *trānsīt* with a long i (*tran–sit–* | *in–tex–*), so the drafter's "or a present" is ruled out. The note now gives the contracted perfect and the reason, and `l` "passes" is now "passed".

### Low
- **L1. Note 698–701.** *saxo atque ingenti fragmine* is not hendiadys. It is one weapon, *atque* adding the fuller description, and the note now says so.
- **L2. Note 705–706.** *ignarum… Mimanta* does not frame the line, since *occubat* comes first. It now reads "far apart".
- **L3. Note 712 (the drafter's open point a, upheld).** The note keeps its rule-5b opening and now says which lighter stop the English reads ("read here as a semicolon").
- **L4. `l` 721.** *longe* now goes with *vidit*, as in the note and `i`.
- **L5. Note 726–729.** *Hunc ubi… vidit* is line 721, not 722.
- **L6. Note 742–744.** *viderit* is now given both ways, as perfect subjunctive or future perfect ("let him look to it"). The drafter's note called it jussive while `l` and `i` said "will see".
- **L7. `l` 749.** "Lycaonian Erichaetes" is now "Lycaon's son Erichaetes", as in the note and `i`.
- **L8. Note 762.** *ingentem… hastam* does not frame the line, since *At vero* comes first. It now reads "far apart, enclosing the participle and the name".
- **L9. Note 770.** *imperterritus* does not stand before the line-end; *ille* does. It now reads "before 'ille'".
- **L10. Rule-5b placement at 742/744 and 772/776, made consistent with 077 (449/451, 494/495) and 078 (580/583, 592/594).**
  - The note of the unit where the speech closes now opens "The print has 'viderit. ”Hoc' … corrected here" (likewise 'Aeneae. ”Dixit').
  - The next unit's note now opens "The closing speech mark printed at the head of this unit belongs to Mezentius's speech (see the note before)."
  - The drafter had the two the other way round.
  - Two notes were rewritten whole to fit the 139-word limit. The only content dropped is "the language of a vow to a god" at 772.
- **L11. `i` 772.** It now begins in lower case ("measuring"), after the semicolon that ends 771, as every other semicolon break in this part does.
- **L12. 781–783 (the drafter's open point b).** `l` already ended "remembers;". `i` now also ends with ";", and `l` and `i` of 783 begin with lower-case "then", as `t` does after the run's restored *Argos;*.
- **E1. `i` 737 (echo).** "no small part of this war" is now "Look, men: tall Orodes lies here, and he counted for much in this war."
- **E2. `i` 743–744 (echo).** "As for me, the father of gods and king of men will see to that" is now "What becomes of me is for the father of gods and king of men to see to."
- **E3. `i` 744–746 (echo).** "Hard rest and iron sleep pressed down upon his eyes, and their light closed in everlasting night" is now "A hard stillness, an iron sleep, weighed on the dying man's eyes, and their light was shut away into a night without end."
- **E4. `i` 763–767, the Orion simile (echo).** The new version reads "…wades through the deepest waters of mid-ocean, breaking a path, his shoulder towering above the waves… he treads the ground with his head lost in the clouds".
- **E5. `i` 773 (echo).** "My right hand, which is my god… be with me now!" is now "Let my right hand, the only god I own, and the spear I balance for the throw, stand by me now!"
- **E6. `i` 781–782 (echo).** "remembered his sweet Argos" is now "as he died his thoughts went home to the Argos he loved" (wording finished in P2-1). `l` keeps the literal "his sweet Argos remembers".

## Changes — pass 2
- **P2-1. `i` 781–782.** The pass-1 wording "and dying, his thoughts went…" left *dying* dangling. It now reads "and as he died his thoughts went home…".
- **P2-2. Note 744–746.** "Virgil uses these two lines again in XII.309–310" was not exact. It now reads "Virgil repeats these two lines at XII.309–310, with 'conduntur', 'are hidden', for 'clauduntur'."
- **P2-3. Note 689–690.** *'contemptor divum'* is now *'contemptor divom'*, as the source prints it at VII.648.

## Refused or upheld without change
1. **Open point (a): 718 *hastas.* before lower-case *haud* (714). Upheld as rule 5b.**
   - The sense allows only one reading: the simile runs on into *haud aliter*.
   - The edition's precedent treats a lower-case word after a full stop as a misprint. Examples: 3.286 (aeneid-019), 3.391 (aeneid-020), 5.481, 6.472 and 8.285.
   - Which lighter stop Greenough printed cannot be checked, so the note says only "a lighter stop", and the English reads a semicolon.
   - QUESTIONS item 43 (the general ruling on lower case after a stop) is still open.
2. **716 *lacessunt:* before capital *Venerat*. Kept, not a misprint.**
   - A colon before a capital occurs 24 times in the edition, among them 10.544 and 10.549, so it is within the print's habits.
   - **Observation for the owner.** The stops at 713 (;), 716 (:) and 718 (.) are exactly the ones these lines carry in the usual order (714–716, then 717–718). That suggests the punctuation stayed with the lines when they were transposed, in Greenough or in the Perseus encoding.
3. **Open point (b): the run's restored *Argos;* (782).** Confirmed. The draft is now consistent: `l` and `i` end with ";", and 783 begins in lower case (L12).
4. **The four right COSTLY fits (696, 749, 763, 764).** No entries, as 078's 528.
5. **The other small costs and the divisions at 722 and 736.** The scanner is right on each; no entries.
6. **Latin Library variants.** The drafter's choices are upheld: 705, 710, 727 and 742 are noted; 704, 709, 712 and 749 and the orthographic ones are not.
7. **Segmentation.** Upheld:
   - the units ending at commas (697, 711, 725)
   - the single unit 726–729 holding the half-line and *sic ruit*
   - the five-line unit 772–776
8. **742 *mixta… ira* as an ablative absolute.** Upheld: noun and participle are in the ablative. The manner reading gives the same English.
9. **747 *illum… hunc* = Cronius… Erichaetes.** Upheld.
10. **754 the javelin/arrow split.** Upheld; the note already says "perhaps".
11. **714 *iustae quibus est Mezentius irae* as a double dative; 706 *ignarum*; 776 *tropaeum Aeneae*.** Upheld.
12. **727 *inproba*.** The note says "shameless", while `l` and `i` say "ruthless". Kept: both are within the word's range.
13. **Echo check, kept.** These are plain renderings, not distinctive:
    - 757 "neither side knew what it was to run"
    - 758 "the useless anger of both sides"
    - 768
    - 789–790 "the tears rolled down his face"
    - the rock, boar and lion similes
14. **Attributions from memory, kept as written.**
    - I am confident of these:
      - Iliad 15.618–621 (the rock), 3.23–28 (the lion and Menelaus), 16.851–854 and 22.358–360 (dying prophecies), 22.365–366 (Achilles' reply), 4.443 (Strife)
      - Odysseus as a boar at bay in Iliad 11
      - Hecuba as daughter of Cisseus in Euripides (Hecuba, the opening)
    - These already carry "perhaps", which is right: 11.414–420, 11.221–247 and 11.241 (Iphidamas, bronze sleep), 16.503, 22.391–394, 7.245–248, 16.718, and Odyssey 11.572–575.
    - Monte Viso, Cortona and the Valerii are standard.
15. **Advisory: none.** Upheld: this is ordinary battle killing.
16. **The about.** Upheld. "A bridegroom who never married" is a fair summary of *infectos… hymenaeos*.
17. **`make_units.py` / `drafter-notes.md`.** These still say 722 for *Hunc ubi… vidit*. They are left as they are, since they are the drafter's record.
18. **Hiatus: none in X.689–790.** Checked.

## Scan-fixes entries added (17)
| key | reason | syllables |
|---|---|---|
| 10.690 | *Teucros*, Greek eu (cost 0.0, unflagged) | 13 |
| 10.705 | *Cisseis* three syllables; *regină*, *Păris* (cost 1.5, unflagged) | 15 |
| 10.712 | *cuiquam*, cui one syllable (cost 0.0, unflagged) | 14 |
| 10.724 | *vēsānă fămēs*, as 9.340 (cost 1.5, unflagged) | 15 |
| 10.726 | carrier for half-line 728 (scanner's fit) | 15 |
| 10.727 | carrier for half-line 728 (scanner's fit) | 16 |
| 10.728 | half-line *ora cruor* (UNRESOLVED) | 4 |
| 10.729 | carrier for half-line 728 (scanner's fit) | 15 |
| 10.743 | *dē*, *mē*, *pătĕr* (cost 0.3, unflagged) | 15 |
| 10.745 | *quĭēs*, *dūră* (cost 0.0, unflagged) | 15 |
| 10.753 | *dē-ĭ-cĭt* (cost 1.8, unflagged) | 17 |
| 10.769 | *Aenēās*, initial Ae- (cost 1.2, unflagged) | 15 |
| 10.776 | *Aenēae*, initial Ae- (cost 1.2, unflagged) | 13 |
| 10.781 | hypermetric, *-que* elided into 782 (UNRESOLVED) | 15 (+que) |
| 10.782 | carrier for 781 (scanner's fit) | 16 |
| 10.783 | *Aenēās*, initial Ae- (cost 1.2, unflagged) | 15 |
| 10.787 | *Aenēās*, initial Ae- (cost 1.2, unflagged) | 13 |

## For the owner (QUESTIONS.md)
- **Rule-5b misprints 10.744 `viderit. ”Hoc` and 10.776 `Aeneae. ”Dixit`.** In each, the closing mark is joined to the next word. The publishing run should add the QUESTIONS.md entry that rule 5b asks for. The reviewer may not touch QUESTIONS.md.
- **10.718 `hastas.` before lower-case `haud`, treated as a rule-5b misprint.** It falls under the still-open item 43 (lower case after a stop). The stops round the transposed 717–718 look like those of the usual order, carried with the lines; whether that happened in Greenough or in Perseus could not be checked.
- **10.782 restored mark.** The run restored it as `;` (rule 5); which mark Greenough printed could not be checked. The reading is the same either way.
- **Rule-5b note placement.** It is now the same as 077 and 078 (L10). Say if you prefer the drafter's placement, with the print's reading on the unit whose `t` holds the stray mark.
- **Doubtful readings, given both ways in the notes:** 744 *viderit* (perfect subjunctive or future perfect) and 754 the javelin/arrow split.
- **Doubtful quantities resting on the only fit:** 780 *Ĭtălā*, 720 *profugūs* lengthened before *hymenaeos*, and 778–779 *Antōren*.
