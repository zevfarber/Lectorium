# Review — aeneid-093 (Aeneid XII.216–310), adversarial reviewer

**Severity counts:**
- **Major: 8.** Wrong scansions on 8 lines: 231, 241, 244, 247, 272, 281, 308 and 309. The packet flagged none ("Scanner flags: none"); five of the eight had a cost of 0.0 to 0.3.
- **Medium: 1** finding (3 edits): the notes at 246, 251 and 297 said *Italas/Itali* has a long first syllable. It is short in all three lines (the scanner had it right).
- **Low: 20.** That is 16 text findings (31 field edits in all, counting the medium) and 4 syllable-division scan-fixes (230, 232, 251, 288).
- **Refused or upheld without change: 21.**
- **Scan-fixes added: 12.** Written straight into `scan-fixes.json` by `drafts/aeneid-093/add_scan_fixes.py --write`, keys 12.230, 12.231, 12.232, 12.241, 12.244, 12.247, 12.251, 12.272, 12.281, 12.288, 12.308, 12.309, appended after 12.211 in the existing `{"sc": [...], "why": "..."}` format. The git diff of `scan-fixes.json` is 141 insertions, 0 deletions.

Nothing blocks the build.

## How the review was done

**Pass 1** went through all 46 units word by word: `l`, `i` and `n` against the Latin; every grammatical label and elision list line by line; the speech marks (Juturna 229–237, Tolumnius 259–265, Messapus 296); the 259 rule-5b handling; the `p` flag (216 only, right); every cross-reference, checked in `source/aeneid-greenough.json` (6.46, 6.228, 8.478–479, 8.492–493, 8.499–503, 9.571, 10.207, 10.562–564, 10.745–746, 11.429, 11.464, 12.118, 12.158 — all found, two corrected in wording, see L2 and L11). All 95 lines were hand-scanned by quantity and compared with the scanner's fit (`scan_check.py` is 092's, pointed at 093), and the existing `scan-fixes.json` entries were used as precedent. Sources: the Latin, the pinned source and memory of the public-domain references only; no translation was opened.

**Pass 2** re-read every changed field (28 fields), every `l` for words on the wrong line, and every `i` for drift from `l`/`n`, for tense, and for remembered phrasing.

**Script runs.**
- The drafter's `units.json` round-trips byte-identically through `aeneid_lib.jdump`; a copy was kept outside the repo before editing.
- `review_edits.py` runs once from the drafter's file: 31 edits, each old string asserted to occur exactly once; guards confirm `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part`, `about` unchanged, `l` line counts equal `t`'s, no line break in `i`, notes 15–139 words.
- `review_check.py` (092's, with `EXEMPT = {258}`, `NOTE_MARKS = {258}`, the unit holding 259) prints no faults: marks t 3/3, l 4/4, i 4/4 (the extra pair is the 259 correction); notes 36–106 words; 46 units, 95 lines; `BUILD REPLICA: OK`; `t/ln/p/v vs drafter: OK`.
- `scan_check.py` applies all 12 entries: sc for 46 of 46 units, no metre failures, no line-up failures, no report left.
- `make_units.py` was not touched and still holds the drafter's strings. Build from `units.json`; do not re-run `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 231 | 1.6 | *Trōĕs* two syllables: nōn sŭ-mŭs \| ēn ōm \| nēs ēt \| Trō-ĕs ĕt \| Ār-că-dĕs \| hī sūnt (15). Scanner ran Troes into one syllable (14). |
| 241 | **0.0** | *requiem* is rĕ-quĭ-ĕm (as 4.433): Quī sĭ-bĭ \| iām rĕ-quĭ \| ēm pūg \| nae rē \| būs-quĕ să \| lū-tēm (15). Scanner read requ-iem with a long re- (14). |
| 244 | **0.0** | *adiungit* is ad-iun-git, consonantal i (as 7.238, 8.13): Hīs ă-lĭ \| ūd mā \| iūs Iū \| tūr-n(a) ād \| iūn-gĭt ĕt \| āl-tō (14). Scanner read a-di-un-git (15). |
| 247 | 1.0 | *rubrā* is ablative with *aethrā* (long -a), *Iŏvĭs* short-short: Nām-quĕ vŏ \| lāns rūb \| rā fūl \| vūs Iŏ-vĭs \| ā-lĕs ĭn \| aeth-rā (15). Scanner had rubra short-short and Iovis long-long. Divided rub-ra so the audio keeps the u short. |
| 272 | **0.0** | *coniunx* is con-iunx (as 12.17, 12.178): ū-nă tŏt \| Ār-că-dĭ \| ō cōn \| iūnx Tȳr \| rhē-nă Gy̆ \| līp-pō (15). Scanner read co-ni-unx (16). |
| 281 | 1.0 | *Trōĕs* two syllables, *Ăgyllini* short A-: Trō-ĕs Ă \| gȳl-lī \| nī-qu(e) ēt \| pīc-tīs \| Ār-că-dĕs \| ār-mīs (14). Scanner had Troes one syllable and A- long. |
| 308 | 0.3 | *lātē* long-long, *rĭgat* short-short, *disicit* dis-i-cit: dīs-ĭ-cĭt \| ēt spār \| sō lā \| tē rĭ-găt \| ār-mă crŭ \| ō-rĕ (15). Scanner had la-te short-short and ri-gat long-long. |
| 309 | **0.0** | = 10.745, scanned as its entry: *quĭēs* two syllables, *dūră* short -a: Ōl-lī \| dū-ră quĭ \| ēs ŏ-cŭ \| lōs ēt \| fēr-rĕ-ŭs \| ūr-gēt (15). Scanner read quies as one syllable and made -ra long. |

### Low (syllable division only; same feet and quantities as the scanner's)

These were wrong only in the syllable split. Each split left an open syllable marked long over a vowel that is short by nature, which `latin_verse.py` would voice as a long vowel.
- **230** *obiectare*: ob-iec, not o-biec (as 2.444, 4.549).
- **232** *Etruria*: Et-ru-ri-a, not an open long E-. The E is short and long only by position before *tr*.
- **251** *Adrexere*: Ad-re, not an open long A-. *volucres* is vo-luc-res.
- **288** *subiciunt*: sub-i-ci-unt, not su-bi- (as 2.444, 9.553).

### Checked by hand and found right, so no entry

- 219 *Ad-iu-vat* (closed Ad-).
- 221 *iuvenali* and *et iu-* (et long by position).
- 225 *cui* as one syllable.
- 226 *ācerrimus*, with a long ā.
- 236 *pārēre*, with a long ā.
- 238 *incensa est*, prodelision, in the scanner's usual form.
- 246, 251 and 297 *Ĭtali/Ĭtalas*, with a short I-, as 3.440, 5.703 and 9.133. Only the notes were wrong (Medium).
- 253 *aethera* and 310 *aeternam*: the scanner has Ae- as one syllable.
- 256 *prōiēcit*: pro- is long by nature, so the open long syllable is right.
- 260 *Adcipio adgnoscoque*.
- 269 *cŭnĕī*, three syllables.
- 274 *balteus*, three syllables. The scanner fit (0.0) agrees with the note; two syllables would also scan, but 12.942 needs three.
- 284 *ferreus*, three syllables.
- 285 present *fŭgit*.
- 299 *venient(i) Ĕbŭsō*.
- 305 *prīmāqu(e) ăciē*.

There is no hiatus and no half-line in the part.

## Medium (text)

- **M1 (246, 251, 297 notes).** The notes said that *Italas* has "its first syllable lengthened, as 'Italia' does in verse", that *Itali* is "Ī-ta-li", and (at 297) "with the first syllable long, as at 251". All three are false. Each line scans only with a short I- (for example, *mentēs Ĭtălās* gives a dactyl, and a long Ī gives no fit). This agrees with the house entries at 3.440, 5.703 and 9.133.

  The notes now say the first syllable is short, and the 246 note adds that only *Italia* lengthens its I-.

## Low

**Notes:**
- **L1 (219).** "a-dju-vat" is now "ad-ju-vat, the first syllable long by position".
- **L2 (225).** "Camers appears at 10.562–563 as the son of great-hearted Volcens, the richest landowner of the Ausonians" has been cut back to what is certain. At 10.563–564, *ditissimus agri qui fuit Ausonidum* may refer to Camers, not to Volcens. The note now reads "Camers appears at 10.562–564, 'magnanimo Volcente satum', son of great-hearted Volcens."
- **L3 (241).** *Qui* was glossed as "the antecedent left out". It is now a connecting relative picking up the Laurentines and Latins of 240. The `i` now reads "They, who had been hoping…" instead of "Men who…". *requiem pugnae* is now an objective genitive, not a "genitive of separation".
- **L4 (247).** Added a scansion pointer: *rubra* is ablative with *aethra*, so its -a is long (scan-fix 12.247).
- **L5 (259).** "as at 6.46 and 11.464" is now "as 'ait' does at 6.46 and 11.464". Those lines have *ait*, not *inquit*.
- **L6 (278).** "Greenough's comma after the first 'pars'" is now "The comma printed after the first 'pars', kept here". See Refused 3 for the decision.
- **L7 (280).** *Laurentum* had been called "the old '-um' genitive plural", which suggests the *superum/divom* pattern. It is now "the genitive plural of 'Laurens', '-um' for '-ium'". Added "'Troes', two syllables, as at 231" (scan-fix 12.281).
- **L8 (285).** "*focos*, the braziers set up at 118" is now "the hearths for the sacrificial fire set up at 118", and `i` "fire-pans" is now "hearths". This keeps it in line with 092's review of 118, which dropped "portable braziers".
- **L9 (288).** "su-bji-ci-unt" is now "sub-ji-ci-unt".
- **L10 (294).** *telo… trabali* "framing the line" is now "framing 'orantem multa'". *Messapus* stands first in the line, outside the frame.
- **L11 (298).** "one buries Misenus at 6.228" is now "one gathers Misenus's bones into an urn at 6.228" (*ossaque lecta cado texit Corynaeus aëno*).
- **L12 (304).** "told in four plain words" is now "five". *sic rigido latus ense ferit* has five words.
- **L13 (309–310).**
  - `l` "are closed" for *conduntur* contradicted the note, which contrasts *conduntur* with 10.746 *clauduntur*, "are closed". It is now "are laid away".
  - Added "'quies', two, qui-es" (scan-fix 12.309).
  - `i` "weighs down his eyes; his eyes are shut in everlasting night" repeated *eyes* and drifted from *conduntur*. It now follows the published 10.745–746 (aeneid-080): "A hard stillness, an iron sleep, pressed on his eyes, and their light was laid away in a night without end."

**`i`:**
- **L14 (tense).** The `i` layer wavered between past and present from unit to unit, while the narrative around it is told in the past. The present-tense ones were put into the past: 216 "had long been seeming" → "had long seemed"; 218 "see… do not meet"; 219 "adds… do"; 225 "plunges… is… speaks"; 241 "want… pray… pity"; 244 "adds… gives"; 267 "whistles… flies… cuts". Speeches keep their own tenses.

  The second clause of 244 was recast at the same time: "none ever did more to confound… or deceived them more" is now "no sign ever threw Italian minds into deeper confusion, or deceived them more surely with its marvel".
- **L15 (260).** "poor people" for *O miseri* was too casual for the register. It is now "you wretched men".
- **L16 (235).** "his name will live on men's lips" is a stock phrase in English versions. As a precaution it is now "and pass, a living man, from mouth to mouth", which stays closer to *vivus per ora feretur*.

**Scan-fixes:** L17–L20 are 230, 232, 251 and 288, listed above.

## Refused or upheld (no change)

1. **259 rule-5b handling: upheld.** The source has `“Hoc erat, hoc, votis, inquit, quod saepe petivi.`, with both inner marks missing. This is the Perseus pattern seen at 6.46 and 11.464. `t` is as printed. `l` and `i` close before *inquit* and reopen after it, and the note opens "The print has…". `make_units.py` exempts it. See "For the run lead" on whether rule 5 is the better route.
2. **Speech marks: correct.** In `t` they are 3 “ / 3 ” (229–237, 259–265, 296). `l` and `i` each have 4/4, the extra pair being the 259 correction. The first and last units of each speech carry the marks, and notes 229/236 and 264 say where the speeches open and end.
3. **278 `pars, gladios`: the comma is kept as printed, and the note is upheld in substance.**
   - The comma does not change the sense.
   - Rule 5 covers only *missing* punctuation.
   - Rule 5b covers clear misprints of letters and words, and a doubtful case is kept as printed with a note.
   - Whether Greenough's 1881 page has the comma cannot be checked; only the Perseus-derived source is local.

   So `t` keeps it. `l` reproduces it ("part, swords they draw"), and the note now says that the comma is printed, is kept, and is not needed for the sense. Its earlier wording called it "Greenough's", an attribution that cannot be checked (changed in L6).
4. **216 *iamdudum* "since the oath began": kept** as an interpretive gloss. The ceremony has been going on since 161.
5. **222 *Quem* as a connecting relative agreeing with the following *sermonem*: upheld.**
6. **218 *non viribus aequis* as an ablative of manner or description, with *eos pugnare* understood: upheld.** The note on the Latin Library's *aequos* is right and changes the construction, not the sense.
7. **221 *tabentes* / LL *pubentes*: the note is upheld.** It is a variant that changes the picture.
8. **231–232 *fatales manus* as "probably the Etruscans", with the prophecy at 8.499–503: upheld.** Turnus's shelter of Mezentius at 8.492–493 is checked.
9. **234 *devotio* (the Decii): upheld.**
10. **247–250 Iliad XII eagle omen** (the eagle drops the snake it carries): **upheld**, and so is the `about`'s "model in the Iliad".
11. **254 *ipso pondere* as the swan's weight: upheld.** 256 *fluvio* as a dative of direction: upheld.
12. **266 Pandarus and Athena in Iliad IV: upheld.**
13. **270 *ut forte* as "where by chance": upheld.** It is a standard reading (*ut* = *ubi*).
14. **274 *balteus* "best read in three syllables, though two would also scan": upheld.** Both are true for this line.
15. **276 *transadigit* with two accusatives: upheld.**
16. **283 "Who carries them off and why is not said": upheld.**
17. **289 Messapus, Neptune's son and tamer of horses (7.691), and 290 Aulestes at 10.207: upheld.**
18. **296 *Hoc habet*, the cry of the arena: upheld.** "He has it!" is the plain sense, not a distinctive echo.
19. **Elision lists: checked line by line in all 46 units, all right.**
20. **The `about`: no change.** It is accurate, including that Alsus kills Podalirius.
21. **`p` flags (216 only) and `new-renderings.md` ("none"): upheld.** No set piece falls in the part.

## For the run lead

- **`scan-fixes.json`** now holds 12 new keys, 12.230 to 12.309 as listed, appended after 12.211. Nothing else in the file changed.
- **QUESTIONS.md / rule record:**
  - **12.259** `votis, inquit, quod` should read `votis,” inquit, “quod`. The two inner speech marks are missing, the same Perseus pattern as 6.46 and 11.464. It is handled as rule 5b, as the drafter set it up. Since only punctuation is missing, rule 5 (add the marks to the source and re-pin) would also apply; I left the source alone.
  - **12.278** `pars, gladios`: a comma that is probably stray, kept as printed with a note. It is unverifiable against Greenough's page.
- **Scansion resting on judgement:**
  - **Split syllables.** 232 *Et-ru-ri-a*, 247 *rub-ra* and 251 *vo-luc-res* are split after the mute, so that the audio does not lengthen a short vowel.

    Earlier entries (2.157 *sa-cra-ta*, 6.685 *u-tras-que*) kept the open long syllable instead. If you want one practice for mute-plus-liquid, these three are the ones to change.
  - **Open long syllables on short vowels (unchanged).** The scanner's `ma–ius` (244, kept unchanged in the 244 entry) puts a long mark on an open *ma-*, which the audio will read *mā-ius*. The same holds for every *maius/maior/eius/cuius* in the corpus. Fixing it is a `latin_verse.py` question, not a per-line one.
- **Unchecked from memory:**
  - Iliad XII (the eagle and the snake);
  - Iliad IV (Pandarus, Athena disguised);
  - the Decii's *devotio*;
  - *hoc habet* as the arena cry;
  - Podalirius as a Greek healer of the Iliad;
  - Agylla = Caere.

  The cross-references to Virgil's own lines were all checked in the source.
- **No new house renderings, no set pieces, no advisory** (battle narrative only).
