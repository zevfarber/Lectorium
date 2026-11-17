# Review — aeneid-095 (Aeneid XII.441–553), adversarial reviewer

**Severity counts:**
- **Major: 14.** Wrong scansions on 14 lines: 481, 482, 483, 491, 505, 506, 507, 515, 526, 528, 529, 535, 540 and 553. The packet flagged 3 lines (443, 515, 538); only 515 is among the 14. Eight of the other 13 had a cost of 0.0: 482, 483, 506, 507, 528, 529, 535 and 553.
- **Medium: 2** findings (3 edits). The 535 elision list elided *Hyllo*, which stands in hiatus (1 edit). Two `i` renderings came close to well-known modern versions (503–504, 546–547; 2 edits).
- **Low: 14.** That is 11 note findings, 1 in the `about`, 1 finding covering the tense of `i` (30 edits), and 1 scan-fix that changes only the syllable division (451).
- **Refused or upheld without change: 20.**
- **Scan-fixes added: 17.** Written straight into `scan-fixes.json` by `drafts/aeneid-095/add_scan_fixes.py --write`, appended after 12.440 in line order. The keys are 12.443, 12.451, 12.481, 12.482, 12.483, 12.491, 12.505, 12.506, 12.507, 12.515, 12.526, 12.528, 12.529, 12.535, 12.538, 12.540 and 12.553. Of these, 14 are Major, 1 is Low (division only: 451), and 2 are "Confirmed", entered only to clear the COSTLY flag (443, 538). The git diff of `scan-fixes.json` is 198 insertions, 0 deletions.

Nothing blocks the build.

## How the review was done

**Pass 1** went through all 52 units word by word:
- `l`, `i` and `n` against the Latin.
- Every grammatical label, and every elision list line by line.
- The speech marks: there are none in this part. `t`, `l` and `i` are all 0/0. 500–504, the poet's own question, is rightly unmarked.
- Who is who at 513, 516, 529 and 535 (see Refused 1).
- The `p` flags (441 and 500, both right).
- Cross-references to Virgil's own lines, checked in `source/aeneid-greenough.json`: 4.532, 5.297, 7.691, 7.744–749, 8.19, 9.465, 9.772–775, 12.139–141, 12.258–266, 12.328, 12.334–335 and 12.338.

All 113 lines were hand-scanned by quantity and compared with the scanner's fit. `scan_check.py` is 094's, pointed at 095. The existing `scan-fixes.json` entries were used as precedent: Aeneas at 12.311, Teucros at 1.304, coniecit at 2.545 and 7.456, disiectas at 2.608, quies at 12.309, Graium at 10.81 and 11.289, Troius at 1.596, ācer at 9.779, and Mnestheus at 12.384. Sources: the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2** re-read every changed field (43 fields plus the `about`), every `l` for words on the wrong line, and every `i` for drift from `l`/`n`, for tense and for remembered phrasing. It found one slip from pass 1: at 548–552 the `i` still had "the strength he has". This was folded into `review_edits.py`, which was rerun from the drafter's copy.

**Script runs.**
- The drafter's `units.json` round-trips byte-identically through `aeneid_lib.jdump`. A copy was kept in the scratchpad (`units.orig.json`) before editing.
- `review_edits.py` runs once from the drafter's file. It makes 45 edits (44 field edits plus 1 to the `about`), each old string asserted to occur exactly once. Its guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn` and `part` are unchanged;
  - `l` line counts equal those of `t`;
  - no `i` contains a line break;
  - every note is 15–139 words.
- `review_check.py` (094's, with `NOTE_MARKS` empty) prints no faults:
  - marks are t 0/0, l 0/0, i 0/0;
  - notes run 44–114 words;
  - 52 units, 113 lines;
  - `BUILD REPLICA: OK`;
  - `t/ln/p/v vs drafter: OK`.
- `scan_check.py` applies all 17 entries: sc for 52 of 52 units, no metre failures, no line-up failures, and no COSTLY report left.
- `make_units.py` was not rerun and still holds the drafter's strings. Build from `units.json`, and do not rerun `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 481 | 1.2 | *Aeneas* Ae-nē-ās: Haud mĭ-nŭs \| Ae-nē \| ās tōr \| tōs lĕ-gĭt \| ōb-vĭ-ŭs \| ōr-bes (15). The scanner split Ae- (16). |
| 482 | **0.0** | *disiecta* dis-iec-ta, consonantal i: vēs-tī \| gāt-quĕ vĭ \| r(um) ēt dīs \| iēc-tă pĕr \| āg-mĭ-nă \| māg-na (15). The scanner read di-si-ec-ta (16). |
| 483 | **0.0** | *coniecit* con-iē-cit: vō-cĕ vŏ \| cāt quŏ-tĭ \| ēns ŏ-cŭ \| lōs cōn \| iē-cĭt ĭn \| hos-tem (16). The scanner read co-ni-e-cit (17). |
| 491 | 1.8 | *Aeneas*: Sub-stĭ-tĭt \| Ae-nē \| ās ēt \| sē cōl \| lē-gĭt ĭn \| ar-ma (14). The scanner split Ae- (15). |
| 505 | 1.2 | *Aeneas*, with *Sucronem* elided into *ea* (nominative, short): Ae-nē \| ās Rŭ-tŭ \| lūm Sū \| crō-n(em) ĕ-ă \| prī-mă rŭ \| en-tis (15). The scanner split Ae- (16). |
| 506 | **0.0** | *Teucros* Teu-crōs, Greek eu: pūg-nă lŏ \| cō stă-tŭ \| īt Teu \| crōs haud \| mūl-tă mŏ \| ran-tem (15). The scanner split Te-u (16). |
| 507 | **0.0** | *quā* and *fāta* long, *cĕlerrima* short: ēx-cĭ-pĭt \| īn lă-tŭs \| ēt quā \| fā-tă cĕ \| lēr-rĭ-mă \| crū-dum (16). The scanner had qua and fa- short and ce- long, a false fit with the same count. |
| 515 | 3.8 (flagged) | *Echionium* Ĕ-chī-ŏ-nĭ-ŭm, five syllables (Echīon, as Ovid, *Met.* 3.126), with *nomen*'s -en short before the vowel; *Peridiae* has a long ī by the metre: nō-mĕn Ĕ \| chī-ŏ-nĭ \| ūm mā \| trīs-quĕ gĕ \| nūs Pĕ-rĭ \| dī-ae (16). The scanner made E- long and chi short, and ran -nium into one syllable (15). |
| 526 | 1.2 | *Aeneas*: Ae-nē \| ās Tūr \| nūs-quĕ rŭ \| ūnt pēr \| proē-lĭ-ă \| nūnc nunc (14). The scanner split Ae- (15). |
| 528 | **0.0** | *tōtīs* long-long, *vŏlnĕră* short: pēc-tŏ-ră \| nūnc tō \| tīs īn \| vōl-nĕ-ră \| vī-rĭ-bŭs \| ī-tur (15). The scanner had to-tis short and -ne-ra long, a false fit with the same count. |
| 529 | **0.0** | *ătăvos* has both a's short, so *Murrā-* is long and *hic* counts long: Mūr-rā \| n(um) hīc ă-tă \| vōs ĕt ă \| vō-r(um) ān \| tī-quă sŏ \| nan-tem (15). The scanner made Mur-ra-hic a dactyl and a-ta- long, a false fit with the same count. |
| 535 | **0.0** | Hiatus after *Hyllo* (its -ō long in the arsis, not elided); *ănĭmis* short-short: Īl-lĕ rŭ \| ēn-t(i) Hȳl \| lō ă-nĭ \| mīs-qu(e) īm \| mā-nĕ frĕ \| men-ti (15). The scanner elided Hyllo and made a-ni- long, a false fit with the same count. |
| 540 | 1.2 | *Aenea* (ablative, -ā): Ae-nē \| ā vĕ-nĭ \| ēn-tĕ sŭ \| ī dĕ-dĭt \| ōb-vĭ-ă \| fer-ro (16). The scanner split Ae- (17). |
| 553 | **0.0** | *requies* rĕ-quĭ-ēs, three syllables (as quies at 12.309): nēc mŏ-ră \| nēc rĕ-quĭ \| ēs vās \| tō cēr \| tā-mĭ-nĕ \| ten-dunt (15). The scanner read requ-ies as two syllables with a long first (14). |

### Low (syllable division only; same feet and quantities as the scanner's)

- **451** *abrupto* is ab-rup-tō, not a-brup-tō. The open long a- would be voiced as a long vowel. This follows 094's 12.319 and 093's prefix practice.

### Confirmed (entered only to clear the flag)

- **443** (flagged, 3.0). *Antheus* and *Mnestheus* each have two syllables, with the Greek eu. The first -que is long before Mn-: Ān-theus \| quē Mnēs \| theus-quĕ rŭ \| ūnt ōm \| nīs-quĕ rĕ \| līc-tis (14).
- **538** (flagged, 2.0). *Graium* has two syllables (as 10.81 and 11.289), and so does *Cretheu*, the Greek vocative: Dēx-tĕ-ră \| nēc tŭ-ă \| tē Grā \| ium fōr \| tīs-sĭ-mĕ \| Crē-theu (15). The run lead's comma after *Cretheu* does not affect the scan.

### Checked by hand and found right, so no entry

- **549** *Mnestheus ācerque*: ācer has a long ā (as 5.507 *Post acer Mnestheus*, 9.176 *acerrimus*, and the house entry 9.779). The scanner's fit is right (cost 1.5).
- **541** *clipei* has three syllables and *aerei* is two by synizesis (cost 1.5). The note says so.
- **502** *Troius* has three syllables, Trō-ĭ-ŭs, as at 1.596 (cost 1.0).
- **509** *deiectum*: the scanner rightly read de-iec-tum. **511** *abscisa* (ab-scī-sa) is right.
- **456** *Rhoeteius*, Rhoe-tē-ĭ-ŭs (1.0). **459** *Archetium/Mnestheus* (1.5). **510** *pedes*, pĕdĕs (1.0). **542** *Aeole*, Ae- one syllable (0.6).
- **458** *Osirim*, Ŏ-sī-rim. **460** *Gyās*, long, as at 5.118. **488** *Huic* is one syllable. **518** *cui* is one syllable.
- **479** *iamqu(e) hic* twice, eliding before h. **532** *sol(o) hunc*.
- **447**, **494**, **497**, **524**, **531**, **536**, **548** and **550–552**: the elisions and quantities are as the scanner has them.

There is no half-line in the part. The only hiatus is at 535.

### Left as scanned (house practice, QUESTIONS item 31)

These divisions put an open long mark on a vowel that is short by nature, but the feet and quantities are right:
- before a mute and a liquid: 450 *a-trum*, 453 *a-gri-*, 463 *a-gros*, 492 *po-pli-*;
- before x: 489 *prae-fi-xa*, 517 *e-xo-sum*, 531 *sa-xi*, 537 *fi-xo*.

## Medium (text)

- **M1 (535 note).** The elision list included *Hyll(o) animisque*. The line scans only with hiatus there: *ănĭmis* cannot fill a spondee. The list now drops it and adds that *Hyllo animisque* is a hiatus, with the long -o kept in the strong place of the foot (scan-fix 12.535).
- **M2 (`i`, echoes of modern versions).**
  - **503–504.** "Was it your will, Jupiter, that nations destined to live in everlasting peace should clash in so great an upheaval?" This came close to well-known versions. It is now "Jupiter, did it please you that peoples who were to live together in lasting peace should crash against each other in such an upheaval?"
  - **546–547.** "your lofty home was beneath Ida, your lofty home at Lyrnesus; your tomb is in Laurentine soil." It is now "beneath Ida stood your lofty house, at Lyrnesus your lofty house; your grave lies in Laurentine earth."

  `l` was not touched in either place.

## Low

**Notes:**
- **L1 (446).** *gelidus… tremor* was said to frame "two lines". It is now "split across the line round 'per ima cucurrit ossa'".
- **L2 (458).** "Ufens led the Aequi" is now "the Aequiculi … (7.744–749)". The source has *Aequicula* at 7.747.
- **L3 (460).** *in adversos… hostis* was said to frame "the line" (*primus* comes first). It now frames *telum qui torserat*, "as it frames 'ductor Rhoeteius' at 456".
- **L4 (468).** Athena and Sthenelus in Iliad V is now marked "from memory".
- **L5 (473).** "The simile is Virgil's own" was an unchecked claim of originality. It is now "No Homeric model comes to mind for it (from memory)".
- **L6 (513).** Added the scansion of *Echionium* (five syllables, long ī) and *Peridiae* (Pe-ri-dī-ae, the long ī required by the metre). This goes with scan-fix 12.515.
- **L7 (529).** Added *ătăvos*, and that *Murranum* therefore has a long second syllable and *hic* counts long (scan-fix 12.529).
- **L8 (538).** "Cretheus is one of Evander's Arcadians" was stated as fact. It is now "presumably one of Evander's Arcadians, not the Trojan Cretheus, the Muses' friend, whom Turnus killed at 9.774–775", which was checked in the source.
- **L9 (539).** "Cupencus is a priest" rests only on Servius' gloss. It is now "was apparently a priest, since Servius, from memory, says…".
- **L10 (542).** "this Aeolus is a Trojan" is now "a man of the Troad (his home was Lyrnesus, 547)". 547 makes his home Lyrnesus, not Troy.
- **L11 (553).** Added *requies*, three syllables (scan-fix 12.553).

**`about`:**
- **L12.** "he gives his anger free rein" is now "he lets his anger loose". This keeps it clear of the phrase dropped from the `i` at 499.

**`i` tense:**
- **L13 (as 094's L17).** The narrative `i` wavered between past and present: 441 was in the past, 442 in the present. It is now in the past at 442, 444, 450, 456, 458, 460, 462, 464, 466, 468, 471, 477, 481, 486 (twice), 488, 494, 496, 505, 509, 513, 516, 525, 526, 529, 532, 535, 548 and 553: 30 edits.
  - Similes keep the present: 451–455, 473–477 and 521–525.
  - So do the poet's own questions (500–504) and the apostrophe *Occidis* at 544.
  - At 499, "and gives his anger free rein" is now "and slackened every rein that held his anger". This is closer to *irarum omnis effundit habenas*, and avoids a stock phrase of the modern versions.
  - At 527, "hearts that cannot learn defeat" is now "hearts that had never learned to be beaten". The first was close to a remembered phrasing.
  - At 505, "since he holds him only briefly" is now "since Sucro held him up only briefly", to make the subject clear.

**Scan-fixes:**
- **L14** is 451, listed above.

## Refused or upheld (no change)

1. **Who is who: the drafter is right on all four.**
   - **513 *Ille* = Aeneas and 516 *hic* = Turnus.** *ille* takes the more distant of the two last named (Aeneas, 505), and *hic* the nearer (Turnus, 509). The victims settle it. Talos, Tanais, Cethegus (a Roman family name) and Onites are Italians, so Aeneas kills them. The Lycian brothers and Menoetes the Arcadian are on the Trojan side, so Turnus kills them.
   - **529 *hic* = Aeneas.** Murranus boasts of a line of Latin kings. Turnus later says that he saw Murranus fall (12.639).
   - **535 *Ille* = Turnus.** *hic* at 529 is Aeneas, so *ille* is the other man. Hyllus is a Trojan, and 538–539 goes straight on to Turnus' next kill (*eripuit Turno*).
2. **544 `i` "You fall" kept in the present.** *Occidis* is the vivid present of the apostrophe, and the poet addresses the dead man directly.
3. **500–504 `i` in the present** ("whom Turnus and the Trojan hero drive"): this is the poet's *nunc*.
4. **Similes in the present**, as in 094.
5. **549 *ācer*: the scanner is right.** There is no entry (see above).
6. **541, 502, 509, 456, 459, 510 and 542: the scanner is right.**
7. **Mute + liquid and x divisions: no entries**, following QUESTIONS item 31.
8. **Speech marks: none in the part**, and correctly none in `l` and `i`. 500–504 is narrative, not a speech.
9. **Variants: none changes the sense enough for a note.**
   - *relinquit* / *reliquit* is a present against a perfect, inside a run of historic presents.
   - *Archetium/Arcetium*, *orbes/orbis*, *dirigit/derigit*, *adgnovit*, *volnera* and *sepulchrum* are orthography or morphology.
10. **12.538 comma: not re-raised**, as instructed.
11. **509 *congressus pedes*, "Turnus fights them dismounted": upheld.** *pedes* is nominative with *Turnus*.
12. **509 *Dioren*, "perhaps the Diores of the foot-race in Book V" (5.297): upheld as "perhaps".** The *Amycus* here is evidently not the Amycus Turnus killed at 9.772. The name recurs in the poem, and the note does not identify him, which is right.
13. **451 Iliad IV goatherd, 500 Iliad XII, 521 Iliad XI, 539 Servius on *cupencus*, 552 Ennius:** each is already marked "from memory". Upheld.
14. **505 `l` puts "that fight" in line 1, though *pugna* is in 506:** *ea* is in 505, so the gloss is placed by the first word of the phrase. Left as it is.
15. **548 `l` "Wholly indeed turned are the lines" for *Totae*:** loose for an adjective, but clear. Left as it is.
16. **488 *uti*, "since he was carrying": upheld** (explanatory *ut*).
17. **505 *haud multa morantem*, Sucro "not delaying (Aeneas) much": upheld.** The `i` now names Sucro.
18. **445 *excĭta* and 492 *incĭta*, both short ĭ: upheld.** The drafter's notes give no quantity, and the scanner's is right.
19. **`p` flags (441 and 500) and `new-renderings.md` ("None"): upheld.** No set piece falls in the part.
20. **441 *ingens* "with the force of an adverb": upheld.**

## For the run lead

- **`scan-fixes.json`** now holds 17 new keys, 12.443 to 12.553 as listed, appended after 12.440. Nothing else in the file changed.
- **No misprint found.** The only source change in the part is the run lead's comma at 12.538.
- **Doubtful quantity, for the record:**
  - **12.515 *Peridiae*.** The name is known only from this line, and the metre requires Pe-ri-dī-ae. The entry and the note both say that the metre is the authority.
  - ***Echionium*** is entered with Ĕ-chī-, after Ovid's Echīon. That is from memory of Ovid, *Met.* 3.126 (*quorum fuit unus Echion*).
- **12.535 hiatus.** This is the first hiatus I have entered in Book XII. The entry's `sc` marks *Hyllo* as a full long syllable. If `latin_verse.py` elides any vowel before a vowel regardless of `sc`, the audio would run *Hyll' animisque*. It is worth checking how the audio treats an `sc` syllable that is marked long rather than left unmarked.
- **Unchecked from memory:**
  - Iliad IV (the goatherd and the cloud);
  - Iliad V (Athena and Sthenelus);
  - Iliad XI (fire and river similes);
  - Iliad XII (hard to tell it all as a god);
  - Homer's apostrophes to Patroclus and Menelaus;
  - Servius on *cupencus*;
  - Ennius as the source of 552;
  - Ovid *Met.* 3.126 for Echīon;
  - Lycian Patara as Apollo's oracle.

  The cross-references to Virgil's own lines were checked in the source.
- **No new house renderings, no set pieces, no advisory.** It is battle narrative only. The severed heads at 511–512 are ordinary epic killing.
