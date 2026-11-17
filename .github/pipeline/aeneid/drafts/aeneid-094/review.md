# Review — aeneid-094 (Aeneid XII.311–440), adversarial reviewer

**Severity counts:**
- **Major: 17.** Wrong scansions on 17 lines: 311, 323, 324, 349, 355, 362, 371, 372, 384, 391, 399, 420, 425, 427, 428, 438 and 440. The packet flagged 6 lines; 5 of them (384, 391, 399, 420, 425) are among the 17. The other 12 were not flagged, and 4 of those (349, 362, 372, 438) had a cost of 0.0.
- **Medium: 2** findings (4 edits). The 391 note on *Iasides* contradicted the house scansion. The `i` of the farewell (435–440) echoed modern versions (3 edits).
- **Low: 19.** That is 15 note or `l` findings, 1 in the `about`, 1 finding covering the tense of `i` (17 edits), and 2 scan-fixes that change only the syllable division (319, 377).
- **Refused or upheld without change: 22.**
- **Scan-fixes added: 20.** Written straight into `scan-fixes.json` by `drafts/aeneid-094/add_scan_fixes.py --write`, appended after 12.309 in line order. The keys are 12.311, 12.319, 12.323, 12.324, 12.349, 12.355, 12.362, 12.371, 12.372, 12.377, 12.384, 12.391, 12.399, 12.419, 12.420, 12.425, 12.427, 12.428, 12.438 and 12.440. Of these, 17 are Major, 2 are Low (division only), and 12.419 is "Confirmed", entered only to clear the COSTLY flag. The git diff of `scan-fixes.json` is 231 insertions, 0 deletions.

Nothing blocks the build.

## How the review was done

**Pass 1** went through all 47 units word by word:
- `l`, `i` and `n` against the Latin.
- Every grammatical label, and every elision list line by line.
- The speech marks: 313–317, 359–361, 425, 427–429 and 435–440. They are 5/5 in `t`, `l` and `i`, each on the first and last unit of its speech.
- The rule-5b handling at 322–323, 362 and 425.
- The `p` flags (311 and 383, both right).
- Cross-references to Virgil's own lines, checked in `source/aeneid-greenough.json`: 3.91, 3.343, 5.263, 5.843, 8.710, 10.575–595, 11.247 and 11.678.

All 130 lines were hand-scanned by quantity and compared with the scanner's fit. `scan_check.py` is 093's, pointed at 094. The existing `scan-fixes.json` entries were used as precedent: Aeneas at 1.305 and 3.343, biiugos at 10.575/587/595, Phegeus at 5.263, and Iapyx/Iapyge at 8.710, 11.247 and 11.678. Sources: the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2** re-read every changed field (35 fields plus the `about`), every `l` for words on the wrong line, and every `i` for drift from `l`/`n`, for tense and for remembered phrasing.

**Script runs.**
- The drafter's `units.json` round-trips byte-identically through `aeneid_lib.jdump`. A copy was kept in the scratchpad before editing.
- `review_edits.py` runs once from the drafter's file. It makes 36 edits (35 field edits plus 1 to the `about`), each old string asserted to occur exactly once. Its guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn` and `part` are unchanged;
  - `l` line counts equal those of `t`;
  - no `i` contains a line break;
  - every note is 15–139 words.
- `review_check.py` (093's, with `NOTE_MARKS = {425}`) prints no faults:
  - marks are t 5/5, l 5/5, i 5/5;
  - notes run 58–137 words;
  - 47 units, 130 lines;
  - `BUILD REPLICA: OK`;
  - `t/ln/p/v vs drafter: OK`.
- `scan_check.py` applies all 20 entries: sc for 47 of 47 units, no metre failures, no line-up failures, and no COSTLY report left.
- `make_units.py` was not rerun and still holds the drafter's strings. Build from `units.json`, and do not rerun `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 311 | 1.2 | *Aeneas* Ae-nē-ās (as 1.305): Āt pĭ-ŭs \| Ae-nē \| ās dex \| trām tēn \| dē-băt ĭ \| ner-mem (14). The scanner split Ae- (15). |
| 323 | 1.2 | *Aeneae* Ae-nē-ae, with *sese* elided: nēc sē \| s(e) Ae-nē \| ae iac \| tā-vīt \| vŭl-nĕ-rĕ \| quis-quam (13). |
| 324 | 1.2 | *Aenean*: Tūr-nŭs ŭt \| Ae-nē \| ān cē \| dēn-t(em) ēx \| āg-mĭ-nĕ \| vī-dit (14). |
| 349 | **0.0** | *Danaum* Dă-nă-ūm, three syllables: quī quōn \| dām cās \| tr(a) ūt Dă-nă \| ūm spĕ-cŭ \| lā-tŏr ă \| dī-ret (15). The scanner read Dā-naum with synizesis (14). |
| 355 | 1.5 | *biiugis* bĭ-jŭ-gīs (as 10.575): sīs-tĭt ĕ \| quōs bĭ-jŭ \| gīs ēt \| cūr-rū \| dē-sĭ-lĭt \| at-que (15). The scanner made bi-iu one long syllable (14). |
| 362 | **0.0** | *coniecta* con-iec-tā, consonantal i: Huic cŏ-mĭ \| t(em) Ās-by \| tēn cōn \| iēc-tā \| cūs-pĭ-dĕ \| mit-tit (14). The scanner read co-ni-ec-ta (15). |
| 371 | 0.8 | *Phegeus* Phē-geus (as 5.263): Nōn tŭ-lĭt \| īn-stān \| tēm Phē \| geus ă-nĭ \| mīs-quĕ frĕ \| mēn-tem (15). The scanner split eu and made Phe- short (16). |
| 372 | **0.0** | *obiecit* ob-iē-cit: ōb-iē \| cīt sē \| s(e) ād cūr \| r(um) ēt spū \| mān-tĭ-ă \| frē-nis (13). The scanner read o-bi-e-cit (14). |
| 384 | 2.7 (flagged) | *Aenean*, with *Mnestheus* as two syllables: īn-tĕ-rĕ \| (a) Ae-nē \| ān Mnēs \| theus ēt \| fī-dŭs Ă \| chā-tes (14). |
| 391 | 2.0 (flagged) | *Iapyx* Ĭ-ā-pyx, vowel I (house: 8.710, 11.247, 11.678): Iām-qu(e) ă-dĕ \| rāt Phoe \| b(o) ānt(e) ă-lĭ \| ōs dī \| lēc-tŭs Ĭ \| ā-pyx (15). |
| 399 | 3.2 (flagged) | *Aeneas*, and *Iuli* as Ĭ-ū-lī: Ae-nē \| ās māg \| nō iŭ-vĕ \| n(um) ēt mae \| rēn-tĭs Ĭ \| ū-lī (14). |
| 420 | 2.0 (flagged) | *Iapyx*, and *eā* ablative: Fō-vĭt ĕ \| ā vōl \| nūs lym \| phā lōn \| gae-vŭs Ĭ \| ā-pyx (14). |
| 425 | 2.0 (flagged) | *Iapyx*: Ār-mă cĭ \| tī prŏ-pĕ \| rā-tĕ vĭ \| rō quĭd \| stā-tĭs Ĭ \| ā-pyx (16). |
| 427 | 0.6 | *hūmānis* and *ŏpĭbus*: Nōn haec \| hū-mā \| nīs ŏ-pĭ \| būs nōn \| ār-tĕ mă \| gis-trā (14). The scanner had -mă- and ō-pī-, a false fit with the same count. |
| 428 | 1.2 | *Aenea* (vocative, -ā), with *te* elided: prō-vĕ-nĭ \| ūnt nĕ-quĕ \| (te) Ae-nē \| ā mĕ-ă \| dēx-tĕ-ră \| ser-vat (16). |
| 438 | **0.0** | *mātūra* and *ădŏlēverit*: Tū fă-cĭ \| tō mōx \| cūm mā \| tū-r(a) ă-dŏ \| lē-vĕ-rĭt \| ae-tās (15). The scanner had ma-tu- short and a-do- long, a false fit with the same count. |
| 440 | 1.2 | The line is 3.343 with *excitet* for *excitat*, scanned as that entry: ēt pă-tĕr \| Ae-nē \| ās ĕt ă \| vūn-cŭ-lŭs \| ēx-cĭ-tĕt \| Hec-tor (16). |

### Low (syllable division only; same feet and quantities as the scanner's)

Each of these splits left an open syllable marked long over a vowel that is short by nature, which `latin_verse.py` would voice as a long vowel. This follows 093's practice for prefix plus consonant (12.230, 12.251, 12.288).
- **319** *adlapsa* is ad-lap-sa, not a-dlap-sa.
- **377** *obiecto* is ob-iec-tō, not o-biec-tō.

### Confirmed (entered only to clear the flag)

- **419** (flagged, 2.0). The scanner's parse is right. *ambrosiae* has four syllables with a short o. *panaceam* has four, from Greek πανάκεια, with a long ē: ām-brŏ-sĭ | ae sū | cōs ĕt ŏ | dō-rĭ-fĕ | rām pă-nă | cē-am (16).

### Checked by hand and found right, so no entry

- **346** *Eumedes*: Eu- is one syllable and the ē is long, despite the cost of 1.5.
- **356** *semianimi*: four syllables, sem-ja-ni-mi (cost 1.5).
- **363** *Chloreāquē Sybarimque…*: the lengthened -que in the arsis is right, and the note now says so. *Chlō-* is long, as at 11.768.
- **365** *Boreae*: three syllables. **366** *Aegaeo*, **401** *Paeonium* (with a short o, as at 7.769) and **409** *aethera*.
- **392** *Iasides*: Ia-si-des, three long syllables, kept as at 5.843. See QUESTIONS.
- **422** *dolŏr* lengthened at the pause (0.3). The note now says so.
- **429** *maior/maiora*.
- **421** *fūgit* perfect.
- **343** *Lăden*.
- **341** *Sthenelum/Thamyrum*.
- **335** *Thrāca*, *ātrae*.
- **352** *adfēcit*.
- **359** *Troiane*.
- **374** and **354**: *iugis* and *iaculo*, with consonantal i, so there is no elision before them.

There is no hiatus and no half-line in the part.

### Left as scanned (house practice, QUESTIONS item 31)

These divisions put an open long mark on a vowel that is short by nature, but feet and quantities are right:
- before a mute and a liquid: 317 *sa-cra*, 331 *He-bri*, 359 *a-gros*, 389 *late-bram*, 414 *ca-pris*;
- before x: 316 *fa-xo*, 353 *pros-pe-xit*, 379 *a-xis*, 388 *pro-xi-ma*, 439 *e-xem-pla*.

## Medium (text)

- **M1 (391 note).** The note said that *Iasides* is "likewise beginning with a vowel", that is, I-a-si-des. The house scansion (5.843, *Iaside*, entered as Ia-si-de, all long) and the scanner's fit kept here read a consonantal I. The note now says "read here as three long syllables, Ia-si-des, as 'Iaside' at 5.843". The Greek points the other way, and both lines would scan either way; see QUESTIONS.
- **M2 (435–440 `i`).** Three renderings came close to well-known modern versions:
  - "what real labour is; learn about good fortune from others". It is now "what it is to be a man and to labour in earnest; for good fortune, look to others".
  - "keep you safe in war and lead you to great rewards". It is now "keep you from harm in battle and bring you among great prizes".
  - "make sure that you remember … let your father Aeneas and your uncle Hector stir you on". It is now "see to it that you keep this in mind … may your father Aeneas and your uncle Hector wake your courage".

  `l` was not touched; it is literal.

## Low

**Notes and `l`:**
- **L1 (311).** *dextram… inermem* was said to frame "the line". It frames *tendebat*.
- **L2 (330).** *raptas… hastas* was said to frame "the line". It frames *fugientibus ingerit*.
- **L3 (336).** The note said "Treachery" while `l` and `i` say Ambush. It now says "Ambush".
- **L4 (336 `i`).** A comma splice: "…and the West, the farthest reaches…" is now "…West; the farthest…".
- **L5 (349).** Added "three syllables, Da-na-um" (scan-fix 12.349).
- **L6 (363).** Added that the -que of *Chloreaque* is lengthened in the strong place of the foot, a Homeric licence in lists (as 3.91 *liminaque laurusque*).
- **L7 (370 `l`).** "and his crest, against the chariot, shakes the breeze, flying" made the crest the subject. It is now "and his crest, as the chariot meets it, the breeze shakes, flying."
- **L8 (371).** Added "Phē-geus, with a long first syllable, as at 5.263".
- **L9 (386).** *gressus* was unexplained. The note now says it is the object of *nitentem*, "propping his steps".
- **L10 (395).** The elision list missed *Ill(e) ut*. Added.
- **L11 (406).** *saevus… horror* "split across the line" is wrong, since both words are in 406. It now reads "framing 'campis magis ac magis'".
- **L12 (417).** "'labrum' a basin with a lip" confused *lăbrum* (lip) and *lābrum* (basin, from *lavo*). Corrected.
- **L13 (422).** Added the lengthened final syllable of *dolor* at the pause.
- **L14 (427).** Added "hū-mā-nis ŏ-pi-bus" (scan-fix 12.427).
- **L15 (440).** Added that the line repeats 3.343, Andromache's question about the boy, with *excitet* for *excitat*. Checked in the source.

**`about`:**
- **L16.** "embraces Ascanius through his helmet" is now "embraces Ascanius and kisses him through his helmet". Line 434 has *per galeam delibans oscula*.

**`i` tense:**
- **L17 (as 093's L14).** The narrative `i` wavered between past and present. It is now in the past at 326, 328, 337, 346, 362, 368, 374, 387, 400, 405, 407, 409, 411, 425, 430 and 432. Similes (331–336, 365–367), speeches and gnomic statements (414–415) keep the present.

  At 337, "trampling cruelly" for *miserabile* is now "trampling, a piteous sight".

**Scan-fixes:**
- **L18–L19** are 319 and 377, listed above.

## Refused or upheld (no change)

1. **322–323 `facti. nec`: rule 5b upheld.** A full stop followed by a small letter is a clear misprint, and the sense allows only a comma (or at most a semicolon): one sentence. `t` is as printed (it is cut from the source). `l` and `i` read the comma, the unit runs across it, and the note opens "The print has…", as at 093's 12.259.
2. **425 `statis? ”Iapyx`: upheld.** It is a closing mark set after the space. Both counts still match, `l` and `i` print `statis?” Iapyx`, and the note opens "The print has…". It is probably an archive normalisation artefact rather than Greenough's; see QUESTIONS.
3. **362 `mittit.` kept as printed: upheld.**
   - The capital on *Chloreaque* proves nothing, because it is a name.
   - A stop with *mittit* carried over to the accusatives of 363–364 is possible, if harsh. So the reading is doubtful, and rule 5b says to keep the print with a note.
   - The note says exactly that. The unit runs 362–364 so that the accusatives stay with their verb.
   - `l` keeps the stop, and `i` keeps the verbless sentence.
4. **No other misprint found.** *adlapsa*, *adtulerit*, *adfecit*, *adspirat*, *tinguit*, *arundine*, *volnus/volnere* and *adcendit* are Greenough's spellings. *Achillis* (Latin Library *Achilli*) does not change the sense, so it needs no note.
5. **Speech marks: correct**, 5/5 in every layer.
6. **Elision lists: all right except 395** (see L10). Checked line by line, including the non-elisions before consonantal *iam*, *iugis*, *iaculo* and *iacens*.
7. **392 *Iasides*: the scanner's fit (consonantal I, all long) is kept** to match 5.843. Only the note was changed (M1).
8. **346, 356, 363, 401 and 422: the scanner is right** (see above).
9. **317, 331, 359, 389 and 414 (mute + liquid) and the x divisions: no entries**, following QUESTIONS item 31.
10. **311 *nudato capite*, "to be recognised": upheld.**
11. **316 *faxo* as an old future: upheld.**
12. **318–322 Pandarus in Iliad IV as the model: upheld.**
13. **331–336 Ares and Phobos in Iliad XIII; Deimos and Phobos as Ares' sons: upheld.**
14. **346–352 Dolon, son of Eumedes, in Iliad X, and his reward: upheld.**
15. **361 Patroclus mocking Cebriones in Iliad XVI: upheld.**
16. **379 inverted *cum*; *praecipitem* proleptic: upheld.**
17. **414 dittany and the wild goats in Aristotle and Theophrastus: upheld.**
18. **424 Glaucus healed by Apollo in Iliad XVI, and Aeneas healed in Apollo's temple in Iliad V: upheld.**
19. **433 "some take 'arma' loosely of his arms": left.** It is loose but not wrong.
20. **435 Sophocles, *Ajax* 550–551, and Hector in Iliad VI: upheld.** The Sophocles quotation is the drafter's own rendering, not a published one.
21. **351 `l` "rewarded, a price" is awkward but keeps the line division: left.**
22. **`p` flags (311, 383) and `new-renderings.md` ("None"): upheld.** No set piece falls in the part.

## For the run lead

- **`scan-fixes.json`** now holds 20 new keys, 12.311 to 12.440 as listed, appended after 12.309. Nothing else in the file changed.
- **QUESTIONS.md / rule record:**
  - **12.322** `gloria facti.` / `nec`: a full stop for a comma (small *nec*). Handled as rule 5b, with `t` as printed and `l`/`i` reading the comma. This is a wrong mark, not a missing one, so rule 5 (correcting the source) does not strictly apply.
  - **12.425** `statis? ”Iapyx`: the closing mark is placed after the space. This probably comes from how `archive_aeneid.py` places ” at a mid-line `</q>`. Worth checking the archive for other mid-line closings.
  - **12.362** `mittit.`: a doubtful stop (most texts have a comma), kept as printed with a note.
  - **12.392 / 5.843 *Iasides/Iaside*.** The house reads Ia-si-de(s), consonantal and all long. Homer's Ἰασίδης (Od. 11.283, line-end Ἀμφίονος Ἰασίδαο) scans Ῑ-ᾰ-σῐ-, which gives Latin Ī-ă-sĭ-dēs with a vowel I. Both lines scan either way. The house reading was kept for consistency; the owner may want to rule on both together. (3.168 *Iasiusque* needs a licence on either reading.)
  - **Audio.** Open long marks on short vowels before a mute and a liquid or before x are left as scanned (item 31). This is a `latin_verse.py` question, not a per-line one.
- **Unchecked from memory:**
  - Iliad XIII (Ares and Phobos);
  - Iliad XVI (Cebriones; Glaucus healed);
  - Iliad V (Aeneas healed);
  - Iliad VI (Hector and the helmet);
  - Iliad X (Dolon);
  - Iliad XX (the horses trampling the dead);
  - Aristotle and Theophrastus on dittany;
  - *Ajax* 550–551;
  - the -que licence as a grammarians' example.

  The cross-references to Virgil's own lines were checked in the source.
- **No new house renderings, no set pieces, no advisory** (battle narrative only).
