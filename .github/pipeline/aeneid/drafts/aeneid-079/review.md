# Review — aeneid-079 (Aeneid X.606–688), adversarial reviewer

**Severity counts: major 4, medium 2, low 19 (17 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 14. Scan-fixes entries added: 10 (all wrong full lines; no half-lines, no carriers).**

All four majors are scansion findings, and the packet flagged none of them:
- M1: initial Ae- split at 637, 647, 656, 661.
- M2: Greek eu split at 617 and 684.
- M3: the i in *coniuncta* 653 read as a vowel.
- M4: wrong quantities with the right count at 623, 628, 649.

## How the review was done

**Pass 1** covered all 38 units word by word. I checked:
- `l`, `i` and `n` against the Latin
- every grammatical label, every "framing" claim and every elision list
- every cross-reference, and every attribution made from memory
- the speech marks, the Latin Library variants, `about`, `title`, `part` and `titleEn`

**Elision lists.** All 38 are right. I checked each line for a vowel or -m before a vowel or h; *Iuno adlacrimans* 628 and *ago? Aut* 675 are both listed, and the elision at 675 is correctly said to run across the question mark.

**Speech marks.** There are six “ and six ” in each of `t`, `l` and `i`, each on the right unit:

| speech | opens | closes |
|---|---|---|
| Jupiter | 607 | 607 (one unit) |
| Juno | 611 | 618 |
| Jupiter | 622 | 625 |
| Juno | 628 | 631 |
| Turnus | 647 | 649 |
| Turnus | 668 | 676 |

The speech opening at 649 opens inside the unit that begins at 647. No speech runs across a part boundary.

**Other checks:**
- **Half-lines and hiatus.** There are none. All 83 lines are full hexameters, and the replica metre check passes on every line.
- **Echoes.** I read every `i` for echoes of the well-known English versions and recast six (E1–E6).
- **Sources.** The Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

**Cross-references checked in the pinned source:**
- IV.24 *Sed mihi vel tellus optem prius ima dehiscat* (Dido): right.
- I.76 *Aeolus haec contra*: right.
- VII.409–412: Ardea, Turnus's city. *Dauni… urbem* (688) is Ardea.
- X.166–167: Massicus leads the men *qui moenia Clusi…* (added at 653–655, L6).
- **X.76 *cui Pilumnus avus*.** In the council, Juno calls Pilumnus Turnus's *grandfather*. Here (619) he is *quartus pater*, so the note now records the inconsistency (D2).
- IX.4 *Pilumni Turnus sacrata valle sedebat*; *Osinius* occurs only at X.655 in the edition, so "perhaps named only here" holds; *tanton* occurs only at X.668.
- **praelia/proelia.** The edition has *proelia* 40 times and *praelia* only at X.661 (D1).
- The scan-fix precedents cited in the new entries: 10.44 *Teucris*, 10.81 *Aenean*, 1.343 and 2.597 *coniunx*.

**Pass 2** re-read every field pass 1 edited, in full. It re-checked:
- the speech marks: 6/6 in each layer, on the same units in `t`, `l` and `i`, asserted by script
- the line counts: `l` has as many lines as `t` in every unit, and no `i` has a line break
- note lengths: 49–104 words, all inside 15–139
- that no unit carries `sc`

It made changes P2-1 and P2-2.

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by `review_edits.py` (pass 1, 21 edits) and `review_edits_pass2.py` (pass 2, 2 edits). Each old string was asserted to occur exactly once in its field, and the file was written with `aeneid_lib.jdump`. The drafter's file round-tripped byte-identically before any edit.
- **Untouched fields.** A copy taken before any edit shows that `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` are unchanged in every unit.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` as it stands and do not rerun `make_units.py`.
- **Build and validator not run** (left to the run).

## Scansion

I hand-scanned all 83 lines and compared them syllable by syllable with the scanner, run in-process the way the build calls it. The helper is `drafts/aeneid-079/scan_check.py` (078's, with the part id changed).

**Packet flags:** none. The scanner gave every line a fit, and no line was flagged COSTLY or UNRESOLVED. Ten of those fits are wrong.

**Unflagged lines that are wrong (10):**
- **Initial Ae- split:**
  - 637 *Aeneae* (cost 1.2)
  - 647 *Aenean* (cost 1.5)
  - 656 *Aeneae* (cost 1.2); the scanner also made *sese* two shorts
  - 661 *Aeneas* (cost 1.2)
- **Greek eu split (cost 0.0 and 0.6):** 617 *Teucris* and 684 *Teucrum*. The scanner wrote *at Te-u* and *tat Te-u* as dactyls.
- **Consonantal i read as a vowel (cost 0.0):** 653 *coniuncta*. It is con-iunc-ta, three syllables; the scanner read co-ni-unc-ta and made the third foot a dactyl, which gave 16 syllables.
- **Wrong quantities with the right count:**
  - **623 (cost 0.0).** The scanner made *mē* and *hōc* short and *ĭtă* long-long. The line is ō-rā | tur iŭ-vĕ | nī mē | (que) hōc ĭ-tă | pō-nĕ-rĕ | sen-tis.
  - **628 (cost 0.0).** The scanner made *Iū-* short and *ad-* short, and *-lă-crĭ-* long-long. The line is Et Iū | n(o) ad-lă-crĭ | māns Quid | sī quae | vō-cĕ gră | vā-ris.
  - **649 (cost 0.6).** Here the scanner kept *Ae* whole, but read the vocative as *Aenĕă* and *thalamos* as long-long. The vocative is *Aenēā* and *thălămōs* is short-short-long. The line is Quō fŭ-gĭs | Ae-nē | ā Thă-lă | mōs nē | dē-sĕ-rĕ | pac-tos.

**Checked and right as the scanner reads them:**
- ***coniunx* 607, 611 (cost 1.5).** The feet and quantities are right. Only the syllable division is off: the scanner writes *co–niunx* where the hand fixes write *con–iunx*. The latest Book X entry, 10.44, keeps *co–niunx*, so no entry was added (R1).
- ***conicit* 646, 657.** The scanner's cō-nĭ-cĭt is right: three syllables, the first long through the hidden consonantal i.
- ***euntis* 640.** Its e-u is not a Greek diphthong (ĕ-un-tis). *aetherii* 621, *aequora* 660, *aequore* 665 and *aestu* 687 carry the ordinary diphthong *ae*.
- **Lines with small costs, each the right fit:** 608 *rēbāre*, 614, 615, 625, 633, 667, 668, 670, 672, 676 *mihī*, 679 and 681.
- **Line 619 *tua larga*.** *tua* is short: it is the neuter plural with *limina*, and *larga* is the ablative with *manu*. The note already reads it so.
- **Line 655 *Osinius*.** Its only fit is Ŏ-sī-nĭ-ŭs.
- **Lines 674 and 683.** *vĭdĕō* has a long final o; in *iăcĭat* the initial i is consonantal.

**How the entries were checked.** Every entry was checked by `drafts/aeneid-079/add_scan_fixes.py` (078's, with the part id and entries changed; dry run, then `--write`):
- against the build's word-match rule
- against the validator's metre rule
- against the syllable count stated in its own `why`

The 661 entry follows the printed *praelia*, since `t` is as printed. A replica of the build's scansion step, reading `scan-fixes.json`, gives these results:
- all 10 entries apply
- **all 38 units get `sc`**
- no unit's `sc` is out of line with its words
- no line fails the metre check
- no report is left

The change to `scan-fixes.json` only appends: 119 insertions, 0 deletions, with the new keys after 10.599 in line order. The file still round-trips through `json.dumps(…, ensure_ascii=False, indent=1)+'\n'`.

## Changes — pass 1

### Major
- **M1. Initial Ae- split, unflagged: 10.637, 647, 656, 661.** See Scansion.
- **M2. Greek eu split, unflagged: 10.617, 684.** See Scansion.
- **M3. *coniuncta*, unflagged: 10.653.** See Scansion.
- **M4. Wrong quantities with the right count, unflagged: 10.623, 628, 649.** See Scansion.

### Medium
- **D1. 661 *praelia*: rule 5b applied (the drafter's open point).**
  - **The evidence.** The edition prints *proelia* 40 times and *praelia* only here.
  - **Why rule 5b covers it.** One stray letter is not one of the edition's consistent spelling habits, which the rule excludes. There is no word *praelium* for the sense to choose instead, so the sense allows only one reading. That makes it a clear misprint.
  - **What changed.** The note now opens: "The print has 'praelia', a misprint for 'proelia', corrected here: 'in proelia', 'to battle'; the edition prints 'proelia' everywhere else." The drafter's clause "'in praelia', Greenough's spelling of 'proelia'" was removed. `t` stays as printed; `l` and `i` ("to battle", "to fight") needed no change.
  - **For the glosser.** The form *praelia* should be glossed as *proelia*, as at 5.215 *ana*/*arva*.
- **D2. Note 618–620.** The note explains *quartus pater* rightly (great-great-grandfather: pater, avus, proavus, abavus), but it missed that Juno herself calls Pilumnus *avus* at X.76 (verified). Added: "at X.76 Juno called Pilumnus his grandfather ('avus'), a small inconsistency."

### Low
- **L1. Note 607–610.** The note called *rebare* "Greenough's form of 'rebaris', 'you used to think'". It is Virgil's ordinary verse ending, not a spelling of the edition's. It now reads "'rebare' = 'rebaris', imperfect indicative of 'reor', 'as you supposed'".
- **L2. Note 613–616.** "Daunus… king of Ardea" overstated the text: Turnus is the king, Daunus the aged father. It now reads "Turnus's aged father, at Ardea (688)".
- **L3. Note 621.** *aetherii… Olympi* does not frame the line, since *Cui rex* comes first. It now reads "far apart, 'Olympi' held to the end of the line".
- **L4. Note 641–642.** *qualis* may be the accusative plural (= *quales*) with *figuras*; the alternative is now given (wording finished in P2-1).
- **L5. Note 647–649a.** "Greenough keeps both" (*Aenean*, *Aenea*) suggested an edition's spelling; these are Virgil's own Greek forms. It now reads "the Greek vocative, with a long final 'a'", which is the quantity the scan needs.
- **L6. Note 653–655.** Cross-reference added: Clusium's men came with Massicus (X.166–167).
- **L7. Note 656.** "'Huc', 'here'" is now "'hither'", as in `l`.
- **L8. Note 668–669.** "Greenough's shortened form" of *tantone* is now "the shortened form".
- **L9. 670.** In the note, "'quem' standing in apposition to 'me'" is now "'quem' predicative with 'me'". In `i`, "Where have I come from?" misread *Unde abii?* ("from where have I gone?") and is now "What place have I left?"
- **L10. Note 673 (the drafter's open point).** The Latin Library's *quosque* changes the construction (a relative instead of an exclamatory question), and the drafter's own words admit "much the same sense". That is below the bar of "note a variant only where it changes the sense", so the clause was cut.
- **L11. Note 687.** *secundo* agrees with both *fluctu* and *aestu*, both masculine ablative singular, not with "the nearer noun". It now reads "going with both nouns".
- **E1. `i` 607 (echo).** "My sister, and my dearest wife as well, you were right in what you thought" is close to stock versions. It is now "Sister of mine, and no less my most dear wife, it is just as you supposed".
- **E2. `i` 625–627 (echo).** "you are feeding on empty hopes" is now "the hopes you nourish are empty".
- **E3. `i` 636–640 (echo).** "a marvel to behold" is now "a wondrous thing to see".
- **E4. `i` 647–649a (echo).** "Where are you running, Aeneas?" is now "Where do you flee, Aeneas?". `l` keeps the literal wording.
- **E5. `i` 651–652 (echo).** "the winds were carrying his triumph away" is now "the winds were bearing off the joy he thought was his".
- **E6. `i` 685–686 (echo).** "Three times he tried each course" is now "Each course he attempted three times".

## Changes — pass 2
- **P2-1. Note 641–642.** The pass-1 insertion repeated *qualis*; it is now "(or it is accusative plural, = 'quales', with 'figuras', 'such shapes as': the sense is the same)".
- **P2-2. `i` 670.** "what sort of man will it bring me home as?" is now "What flight is this, and as what kind of man will it bring me home?"

## Refused or upheld without change
1. **R1. *coniunx* 607 and 611 (cost 1.5).** The scanner's feet and quantities are right; only its syllable division (*co–niunx*) differs. The latest Book X entry, 10.44, keeps the same division, so no entry was added.
2. **The other small costs (608, 614, 615, 625, 633, 667, 668, 670, 672, 676, 679, 681).** The scanner is right on each; no entries.
3. **The unit ending at the comma at 640 (the drafter's open point). Upheld.** The period 636–642 has only commas inside it and is seven lines long. conventions.md says "at most five lines; split long periods at internal punctuation". Splitting at *euntis,* before the simile is the natural break, and the note says the unit ends at a comma.
4. **The five-line unit 680–684.** Upheld: there is no internal stop, and it is within the limit.
5. **The order of 661–662.** Upheld: Greenough's order is kept, and the note states the Latin Library order in one clause. This is a placement that changes how the passage reads, so it is worth the clause.
6. **The other Latin Library variants.** 660 *avolsamque*/*auulsamque* (orthography) and 679 *neque*/*nec* (no change of sense) are rightly not noted.
7. **Doubtful readings left both ways or as drafted.**
   - 608: Jupiter's irony.
   - 625: *hactenus indulsisse vacat*, the perfect infinitive in present sense.
   - 630–631: *veri vana feror* ("go astray", with "perhaps 'I am said to be'").
   - 660: *revoluta per aequora* (perhaps the ebb tide). The `i` "ebbing waters" takes one of the note's two readings, which is legitimate.
   - 678: *Syrtis* as genitive singular.
   - 686: *animi*, with its origin given as "perhaps".
8. **650 "enough for a grave".** Upheld: this is the traditional reading of the taunt.
9. **631 *Quod* as "a connecting relative, 'as to which'".** Upheld: *quod* used as a connective before *utinam*/*ut* (A&G).
10. **619 *tua… limina*.** Upheld: the note is right, and the metre confirms the short *tua*.
11. **Echo check, kept.** "What earth could open deep enough to swallow me now?" (plain English for the Latin), "On he glides, cutting through the deep" and the 668–669 and 676–679 renderings are the drafter's own turns.
12. **Attributions from memory, kept as written.**
    - I am confident of these: Iliad 16.431–461 (Zeus and Hera over Sarpedon); 5.449–453 (Apollo's image of Aeneas); 4.182 (Agamemnon: may the earth gape for me); 1.188–194 (Achilles deliberating); 16.702–705 (Patroclus three times at the wall).
    - These already carry "perhaps", which is right: 21.595–605 (Agenor) and 6.281–282 (Hector of Paris).
13. **Advisory: none. Upheld, with a flag for the owner.** 680–682 is Turnus considering falling on his sword: two lines, a thought only, checked by Juno. The note states it plainly. This matches the drafter's judgement, and I judge it below the bar, but see the owner list.
14. **Half-lines and hiatus: none in X.606–688.** Checked.

## Scan-fixes entries added (10)
| key | reason | syllables |
|---|---|---|
| 10.617 | *Teucris*, Greek eu (cost 0.0, unflagged) | 15 |
| 10.623 | *mē*, *hōc*, *ĭtă* (cost 0.0, unflagged) | 15 |
| 10.628 | *Iūno*, *ad-lă-crĭ-māns* (cost 0.0, unflagged) | 14 |
| 10.637 | *Aenēae*, initial Ae- (cost 1.2, unflagged) | 14 |
| 10.647 | *Aenēān*, initial Ae- (cost 1.5, unflagged) | 13 |
| 10.649 | *Aenēā* vocative, *thălămōs* (cost 0.6, unflagged) | 15 |
| 10.653 | *coniuncta*, consonantal i (cost 0.0, unflagged) | 15 |
| 10.656 | *Aenēae*, *sēsē* (cost 1.2, unflagged) | 15 |
| 10.661 | *Aenēās*, initial Ae- (cost 1.2, unflagged); words as printed (*praelia*) | 13 |
| 10.684 | *Teucrum*, Greek eu (cost 0.6, unflagged) | 15 |

## For the owner (QUESTIONS.md)
- **Rule-5b misprint 10.661 `praelia` for `proelia`.** It is corrected in the note and should be corrected in the gloss; `t` stays as printed. The publishing run should add the QUESTIONS.md entry that rule 5b asks for, as for 5.215 and 6.684. The reviewer may not touch QUESTIONS.md.
- **The Pilumnus inconsistency.** X.76 calls him *avus*; X.619 calls him *quartus pater*. This is now noted in the reading; no decision is needed.
- **Doubtful readings, given both ways in the notes:**
  - 630–631: *veri vana feror*
  - 641: *qualis*, nominative or accusative plural
  - 660: *revoluta per aequora*
  - 670: *quemve*, predicative
- **Advisory.** Turnus contemplates suicide (680–682) and is restrained. If the owner rules on suicide advisories (the Dido question), say whether a contemplated, unperformed suicide counts. The reviewer judges that it does not.
