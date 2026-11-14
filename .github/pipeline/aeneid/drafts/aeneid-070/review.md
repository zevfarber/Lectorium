# Review — aeneid-070 (Aeneid IX.621–716), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 43 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked the drafter's five misprint calls (9.635, 9.644, 9.654, 9.656, 9.683), the readings kept as printed (9.676 `animis`, 9.686 `at`), the Latin Library variants, the speech marks, the no-advisory decision, the `about`, the title and part names. I read every `i` for echoes of the well-known English versions, most closely Apollo's *Macte nova virtute* (641–644), the oak simile (679–682) and the Baiae simile (710–716).

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 9.40–43, 9.593, 9.598–620, 9.599, 1.267, 2.693, 4.558–559, 5.372, 11.690. One was off: Numanus's speech is 23 lines (598–620), not 22 (item L3).

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 96 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story` (with each unit's `ln`, so lines split between units are joined), and compared its output with mine syllable by syllable.
- **The packet's five flags**: 640, 647, 650, 652 and 673 are all wrong as the scanner gives them (M3, M4, M5, M7, M9).
- **Eight more lines are wrong without a flag**: 634, 636, 651, 653, 680, 689, 697, 707 (M1, M2, M6, M8, M10–M13).
- **716 *Typhoeo***: right count and quantities, wrong syllable division (`phoe–o`, an oe diphthong). Entered as 8.298 *Typhoeus* (L-S1).
- **649** has no error, but its second half sits in the same unit as hypermetric 650, so the scanner gives that unit nothing; it is entered as a carrier line, as 4.559, 5.752, 5.754, 6.603 and 8.229 were. 651 and 652 are carriers too, but are also wrong in their own right.
- The drafter's other worries are cases where the scanner is right (see "Hand-scan notes" below).

**Hypermetric 650.** Handled exactly as 4.558 (whose second half it repeats), 5.753, 6.602 and 8.228: the elided `-que` follows the `×` as an unmarked syllable (`'co⏑6lo–rem×que'`). The validator's metre rule strips letters before reading the feet, so the line passes as six feet of 15 counted syllables. Its `why` does not begin "Half-line", so it gets the full hexameter check, which it passes.

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet, then –×/⏑×. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 15 entries apply
- **all 43 units get `sc`**
- all 96 lines pass the validator's metre check
- the scanner report is empty (the UNRESOLVED and four COSTLY lines are all cleared by matching entries).

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`, as the drafter's file was.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 43 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- **13 units changed** (1, 2, 7, 9, 10, 12, 13, 15, 16, 19, 26, 36, 42). `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Note lengths.** Every note is 29–109 words; none was over the validator's 140 before or after.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 168 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.618, in line order.
- The build and the validator were not run (`build_aeneid.py` has no dry-run mode). Their scansion and layer steps were replicated instead.

**Severity counts: major 13, medium 1, low 15 (13 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 17. Scan-fixes entries added: 15 (13 wrong lines, 1 syllable division, 1 carrier).**

## Changes — pass 1

### Major (scanner wrong; each now has a scan-fixes entry)
M1. **9.634, *traicit* (unflagged).** The scanner read *trai-* as a diphthong and made *-cit* long before the vowel of *I* (13). Right, with the consonantal i written once after the prefix, as *inicit* 9.553: trā-ĭ-cĭt | ī vēr | bīs vīr | tū-t(em) īn | lū-dĕ sŭ | pēr-bis (14).
M2. **9.636, *Teucri* (unflagged).** The scanner split Te-u (15). Right: hōc tān | t(um) Ās-că-nĭ | ūs Teū | crī clā | mō-rĕ sĕ | quūn-tur (14).
M3. **9.640, *Iulum* (flagged COSTLY 2.0).** The scanner took Iu- as consonantal and made a spondaic fifth foot (13). *Iulum* is Ĭ-ū-lum, as the published entries for Iulus: nū-bĕ sĕ | dēns āt | (que) hīs vīc | tō-r(em) ād | fā-tŭr Ĭ | ū-lum (14).
M4. **9.647, hiatus (flagged COSTLY 3.5).** The scanner elided *Dardanio* and split *Anchisae* into four syllables. Right, with hiatus and a spondaic fifth foot: ān-tī | qu(um) īn Bū | tēn hīc | Dār-dă-nĭ | ō Ān | chī-sae (13).
M5. **9.650, hypermetric (UNRESOLVED).** As 4.558: ōm-nĭ-ă | lōn-gae | vō sĭ-mĭ | līs vō | cēm-quĕ cŏ | lō-rēm(que), the -que eliding into *et* (651) (15 counted).
M6. **9.651 (unflagged; also a carrier for 650).** Right count, wrong quantities: the scanner made *crīnīs* short-short, *saevă* long and *sŏ-* long. Right: ēt crī | nīs āl | bōs ēt | sae-vă sŏ | nō-rĭ-bŭs | ār-ma (14).
M7. **9.652, *Iulum* (flagged COSTLY 2.0).** As M3: āt-(que) hīs | ār-dēn | tēm dīc | tīs ād | fā-tŭr Ĭ | ū-lum (13).
M8. **9.653, *satis, Aenide* (unflagged).** Right count, wrong quantities: the scanner made *sa-* and *-tis* long and *tē-* short. *sătĭs* forces a first-foot dactyl, and then *Aenīdē* must be long-long-long: sīt să-tĭs | Āe-nī | dē tē | līs īm | pū-nĕ Nŭ | mā-num (14).
M9. **9.673, *Iaera* (flagged COSTLY 2.0).** The scanner read *Iae-* as consonantal I plus diphthong, with a spondaic fifth foot (13). *Iaera* (Ἴαιρα) is three syllables, as the drafter's note says: quōs Iŏ-vĭs | ē-dū | xīt lū | cō sīl | vēs-trĭs Ĭ | ae-ra (14).
M10. **9.680, *ripis Athesim* (unflagged).** Right count, wrong quantities: the scanner made *rīpīs* short-short and *Ăthĕ-* long-long. Right: sī-vĕ Pă | dī rī | pīs Ă-thĕ | sīm seu | prōp-tĕr ă | moe-num (15).
M11. **9.689, *Troes glomerantur* (unflagged).** The scanner read *Troes* as one syllable and *glŏmĕ-* as long-long (13). Right, with *Trō-ĕs* two syllables as the note says: ēt iām | cōl-lēc | tī Trō | ēs glŏ-mĕ | rān-tŭr ĕ | ō-dem (14).
M12. **9.697, *Thebana de matre nothum* (unflagged).** Right count, wrong quantities: the scanner made *dē* and *mā-* short, and *-trĕ* and *nŏ-* long. Right: Thē-bā | nā dē | mā-trĕ nŏ | thūm Sār | pē-dŏ-nĭs | āl-ti (14).
M13. **9.707, *squama lorica fidelis* (unflagged).** Right count, wrong quantities: the scanner made *squāmā* short-short, nominative *lōrīcă* long-final and *fĭ-* long. Right: nēc dŭ-plĭ | cī squā | mā lō | rī-că fĭ | dē-lĭs ĕt | āu-ro (15).

### Medium
1. **Note, `l` and `i` 646–647a, *Forma tum vertitur oris*.** The draft made *Forma* the subject of *vertitur* ("His shape then is turned"). The metre rules this out: in *pĕ-tīt Fōr | mā tūm* the fourth foot needs a long *-ā*, so *formā* is ablative of respect and Apollo is the subject ("he is turned, in the shape of his face, into old Butes"). Changes:
   - `n` now says *formā* is ablative of respect, as the metre shows, with Apollo the subject.
   - `l` now reads "In shape then he is turned, of his face, / into old Butes;".
   - `i` now reads "Then he was changed, in the look of his face, into old Butes;".

### Low
- **L-S1. 9.716 *Typhoeo*: scan-fixes entry.** The quantities are the scanner's, but the syllables are now `Ty⏑6pho–eo×` (no oe diphthong; -eo by synizesis) instead of `phoe–o`, following the 8.298 *Typhoeus* entry. The note now says so (L12).
- **L-S2. 9.649: carrier entry.** The scanner's own fit (17 syllables), entered only because the line shares a unit with 650.
- **L1. `l` 625.** "to my daring give your nod, my undertaking" added "my" twice and blurred the dative. It now reads "to bold give your nod, beginnings", showing the *audacibus… coeptis* frame that the note describes.
- **L2. Note 626–629.** Eclogue 3.87 is not a bull "promised": *pascite taurum* is a bull to be reared for Pollio. It now says "of a bull to be reared for Pollio".
- **L3. Note 636a.** Ascanius speaks a line and a half (634b–635), and Numanus's speech runs 598–620, which is 23 lines. It now reads "The boy's line and a half answer Numanus's twenty-three (598–620)".
- **L4. Note 638–640.** *Aetheria… plaga* frames *tum forte*, not the line. Added "'Iulum' has three syllables, I-u-lum", which matches M3/M7.
- **L5. `i` and `l` 641–642a.** "Glory to your young courage, boy! This is the road to the stars" was close to the stock English of this famous line. It is now "Honour to you, boy, for courage newly shown! This is how one travels to the stars". `l` "Be blessed" is now "Be honoured", matching the note's gloss of *macte*.
- **L6. Note 644b–646a.** "(see the last unit)" could be read as the part's last unit. It now says "(see the previous unit)".
- **L7. Note 649b–652.** Added "Lines 650–651 echo the description of Mercury at 4.558–559" (*omnia Mercurio similis, vocemque coloremque / et crinis flavos*), which was checked in the source.
- **L8. Note 653–654a.** Added that the metre makes the i of *Aenīdē* long (M8).
- **L9. Note 659–660.** "'proceres… Dardanidae'… framing;" named no object. It now reads "framing 'divinaque tela'".
- **L10. Note 679–682.** "'propter' after 'amoenum (Athesim)'" was wrong: *propter* stands after *Athesim* but before *amoenum*. It now reads "as 'propter' after 'Athesim': 'propter amoenum Athesim'".
- **L11. Note 702–704.** *Meropem* has the ordinary Latin accusative ending; only *Erymanta* and *Bitian* are Greek. Corrected.
- **L12. Note 715–716.** "'Typhoeo', a Greek dative" is now "dative of the Greek name, Ty-pho-eo… the 'oe' is not a diphthong", which matches L-S1.

## Changes — pass 2
- **P2-1. `l` 641.** "Be honoured in your new valour" is now "Be honoured for your new valour".
- **P2-2. Note 638–640.** "'victorem… Iulum'… framing;" is now "framing 'adfatur'".

## Scan-fixes entries added (15)
| key | reason | syllables |
|---|---|---|
| 9.634 | *trāĭcit*, consonantal i after prefix; -cit short before a vowel | 14 |
| 9.636 | *Teucri*, Greek eu | 14 |
| 9.640 | *Ĭūlum* three syllables (flagged) | 14 |
| 9.647 | hiatus *Dardaniō \| Anchīsae*, spondaic fifth (flagged) | 13 |
| 9.649 | carrier for 650 (scanner right) | 17 |
| 9.650 | hypermetric, -que elides into 651 *et* (UNRESOLVED) | 15 |
| 9.651 | *crīnīs*, *saevă*, *sŏnōribus*; carrier for 650 | 14 |
| 9.652 | *Ĭūlum* (flagged); carrier for 650 | 13 |
| 9.653 | *sătĭs*, *Aenīdē*, *tēlīs* | 14 |
| 9.673 | *Ĭaera* three syllables (flagged) | 14 |
| 9.680 | *rīpīs*, *Ăthĕsim* | 15 |
| 9.689 | *Trōĕs* two syllables, *glŏmĕrantur* | 14 |
| 9.697 | *dē*, *mātrĕ*, *nŏthum* | 14 |
| 9.707 | *squāmā*, *lōrīcă*, *fĭdēlis* | 15 |
| 9.716 | *Typhōeō*: syllable division only (as 8.298) | 16 |

## Hand-scan notes on the special lines (scanner right, no entry)
- **638** *Aetheria*, **645** *aethere*: Ae- one syllable. Right.
- **646** Ās-că-nĭ | ūm-quĕ pĕ | tīt fōr | mā tūm | vēr-tĭ-tŭr | ō-ris: right, and it is what proves *formā* ablative (Medium 1).
- **642** *Iure*, **624/716** *Iovem/Iovis*, **621** *iactantem*, **698/704** *iaculo*, **712** *iaciunt*: consonantal i. Right.
- **674** *abietibus*: āb-yĕ-tĭ | būs iŭ-vĕ | nēs pă-trĭ | īs ēt | mōn-tĭ-bŭs | ae-quos (`ab–ie⏑ti⏑`, as published `ab–ie⏑te⏑`). Right.
- **698** *coniecto*: cōn-iēc | tō stēr | nīt iă-cŭ | lō vŏ-lăt | Ī-tă-lă | cōr-nus (15). Count and quantities right; the scanner divides `co–niec` (see refused item 14).
- **710** *Euboico*: eu one syllable; *Baiarum* `Ba–ia–rum`, count and quantities right. Right.
- **679** *aëriae*, **699** *aëra*: a-e two syllables. **679** *līquentia* has long ī (from *līquor*). Right.
- **643** *resīdent*: the metre confirms the long ī of *resīdo*, so the note's "future of 'resido'" is right (*resĭdeo* would not scan).
- **644** *Troia*: `Tro–ia⏑`, as in the published parts. Right.
- **690** *eodem* three syllables; **676** *fret(i) animis*; **715** *Prochyt(a) alta*; **682** *sublimi* (`su–bli`, quantity right, ad-/sub- division left as published). Right.

## Refused or upheld findings
1. **9.635 `His` → `Bis` (misprint, upheld).** It is a wrong letter. Ascanius throws back Numanus's own *bis capti Phryges* (599, checked), and *His capti* gives no sense. The Latin Library has *bis*, and the scansion is the same. The note opens in the rule-5b form.
2. **9.644 `capit. ”Simul` and 9.656 `bello. ”Sic` (misprints, upheld).** Each is a closing mark joined to the next word, as 9.392, 9.561 and 5.400. The handling (`t` carries the stray ” at the head of the next unit, and `l`/`i` close the speech on the earlier unit, which then carries no mark) is coherent. It is also forced: the source has no space between ” and the next word, so a cut after ” would end mid-word, which `build_aeneid.py` refuses. Running the units on would make six-line units. Counts: `t`, `l` and `i` each have 4 “ and 4 ”. In `t` the closing marks are on units 2, 6, 12 and 18; in `l`/`i` they are on units 2, 6, 11 and 17. The validator compares totals per layer only, so it gives no warning. This is the 042 / 6.155 handling.
3. **9.654 `magnus, Apollo` (misprint, upheld).** The drafter asked whether a stray comma is too slight for rule 5b. I judge it a clear misprint, not a doubtful reading. *magnus Apollo* is subject of *concedit*. The comma separates nothing: it has no partner after *Apollo*, there is no vocative, and *magnus* cannot stand alone as a substantive here. Only one reading of the words is possible. Punctuation misprints have been treated this way before (6.844 `sulco Serrane,`, 7.170 `ingens. centum`). The note's opening stands.
4. **9.683 lowercase `inrumpunt` after `nutant.` (misprint, upheld).** This is the standing interim practice (QUESTIONS 43: treated as misprints until the owner rules). The drafter's reading of Greenough's unpunctuated 683 (the *ut* clause parenthetic, the four named men the subjects) construes and is upheld.
5. **9.676 `animis` (kept, upheld).** The Latin Library has *armis*. Both give sense and both scan, so this is a doubtful reading, kept and noted.
6. **9.686 `at` (kept, upheld).** The Latin Library has *aut*. The sense is the same, so the reading is kept and noted. The note's account (*aut* in 687 alone carries the alternative) is right.
7. **9.645 `misit`** (Latin Library *mittit*): tense only, so not noted. Upheld. The orthographic variants (677, 679, 699, 700) are ignored per conventions.
8. **Advisory: none (upheld).** This is ordinary battle killing, consistent with 067–069.
9. **Attributions from memory, confirmed:**
   - Iliad 1.528 (Zeus's nod)
   - Georgics 1.40 (*audacibus adnue coeptis*, to Caesar)
   - Eclogue 3.87 (wording corrected in L2)
   - Iliad 17.322–325 (Apollo as Periphas)
   - Iliad 1.46 (the arrows rattle on his shoulders)
   - Iliad 12.131–134 (the two Lapiths like oaks)
   - Iliad 12.156–158 (stones like snow)
   - Iliad 4.504 (*arabēse de teuche' ep' autōi*)
   - Iliad 2.783 (*ein Arimois*)
   - Sarpedon killed by Patroclus in Iliad 16
   - Assaracus as Anchises's grandfather
   - the Haedi as stormy stars
   - Cumae from Chalcis
   - Baiae piers
   - Inarime and Typhoeus

   Kept as written.
10. **Note 657, *mortalis aspectus* as "mortal sight", with the alternative given.** Upheld.
11. **Note 668, *ab occasu* "from the west", with the alternative given.** Upheld.
12. **Note 709, the subject of *intonat* taken as Bitias.** Upheld, since it is hedged.
13. **Note 697, *Thebana* "probably" Thebe in the Troad.** Upheld.
14. **9.698 *coniecto*: no entry.** The scanner's count and quantities are right, and only the division `co–niec` is off. The published parts carry `co–niunx×` eight times as the scanner gave it, and 069 refused the same kind of entry for *adripit*/*adlapsa*. Refused for consistency. The same applies to 710 `Ba–ia–rum` and 644 `Tro–ia`.
15. **`i` 641 "This is the road to the stars" as a set piece.** *sic itur ad astra* is not on the conventions' set-piece list. The rewording in L5 avoids the stock phrasing; no house rendering is proposed.
16. **Echo check.** No other distinctive echo of a known English version was found. "into thin air" (658) is ordinary English for *in tenuem auram*. Upheld.
17. **Unit cuts.** The 642b–644a / 644b–646a and 654b–656a / 656b–658 divisions are forced by the stray marks (item 2), and the 702–704 / 705–708a split at a comma is within the five-line limit. Upheld.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b, t as printed, l/i corrected, note opens with the print's reading):**
  - 9.635 `His` for *Bis*
  - 9.644 `capit. ”Simul` and 9.656 `bello. ”Sic` (closing mark joined to the next word)
  - 9.654 `magnus, Apollo` (stray comma)
  - 9.683 lowercase `inrumpunt` (item 43 still open).
- **Kept as printed:** 9.676 `animis` (Latin Library *armis*) and 9.686 `at` (Latin Library *aut*).
- **Doubtful quantities on the only fit:**
  - 9.653 *Aenīdē*, long i
  - 9.680 *Ăthĕsim*, short-short, forced by *rīpīs*
  - 9.673 *Ĭaera*, three syllables, from the Greek
- **9.646 *formā*:** the reviewer's change rests on the metre; *forma* nominative cannot scan.
- **Unchecked attributions from memory:** Iliad 1.528, 17.322–325, 1.46, 12.131–134, 12.156–158, 4.504, 2.783; Georgics 1.40; Eclogue 3.87; Thebe in the Troad; Roman piers at Baiae.
