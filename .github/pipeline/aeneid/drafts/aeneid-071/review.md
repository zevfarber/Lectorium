# Review — aeneid-071 (Aeneid IX.717–818), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 51 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked the drafter's misprint call (9.781), looked for misprints the drafter might have missed, checked the Latin Library variants, the speech marks, the bracketed line 777, the no-advisory decision, and the `about`, title and part names. I read every `i` for echoes of the well-known English versions, most closely the lion simile (792–798) and the Tiber ending (815–818).

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source and are all right: 9.2, 9.171–173, 9.423, 9.632, 9.708, 9.709, 1.221, 1.254, 2.547–548, 6.89, 6.164–165, 7.31, 8.62–64. The wording about 8.62–64 was loosened (L12).

**Pass 2** re-read every edited field in full, re-checked speech marks, line counts and note lengths, and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 102 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story` (with each unit's `ln`, so lines split between units are joined), and compared its output with mine syllable by syllable. The helper is `drafts/aeneid-071/scan_check.py`.
- **The packet's three flags**: 721 and 761 are half-lines and need entries (M2, M5). 811 (COSTLY 2.2) is right as the scanner gives it; it is entered only to clear the flag, as earlier parts did (L-S2).
- **Nine more lines are wrong without a packet flag**: 719, 725, 756, 767, 772, 779, 787, 791, 805 (M1, M3, M4, M6–M11). Four of them are Greek *eu* (*Teucris*, *Teucri* ×2, *Teucrorum*). The drafter's list of *eu* lines left out 805 *Teucrorum*. One is initial *Ae-* (787 *Aeneae*). The other four have wrong quantities with no special feature (725, 756, 767, 772).
- **760** is a carrier for the half-line 761 (L-S1).
- The drafter's other worries turn out to be cases where the scanner is right (see "Hand-scan notes" below).

Every new `scan-fixes.json` entry was checked by script (`drafts/aeneid-071/add_scan_fixes.py`) against the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet, then –×/⏑×. For a `why` beginning "Half-line", the rule is the validator's half-line rule instead. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 13 entries apply
- **all 51 units get `sc`**
- all 102 lines pass the validator's metre check (half-line rule for 721 and 761)
- the scanner report is empty.

**What was edited, and how.**
- `units.json` was edited only by Python scripts: `drafts/aeneid-071/review_edits.py` for pass 1 and `review_edits_pass2.py` for pass 2. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`, and a round-trip of the drafter's file through `jdump` was byte-identical before any edit.
- `t`, `ln`, `p` and `v` are as the drafter left them in all 51 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged. No unit boundary was changed.
- **10 units changed** (4, 8, 13, 17, 23, 26, 27, 39, 41, 50). `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks**: `t`, `l` and `i` each have 5 “ and 5 ”, on the same units (7, 8, 10, 11, 16, 17, 32, 33, 35).
- **Note lengths**: the longest note is 121 words, under the validator's 140.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 133 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.716, in line order.
- The build and the validator were not run (`build_aeneid.py` has no dry-run mode). Their scansion and layer steps were replicated instead.

**Severity counts: major 11, medium 1, low 16 (14 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 20. Scan-fixes entries added: 13 (11 wrong lines, of which 2 are half-lines; 1 carrier; 1 confirmation).**

## Changes — pass 1

### Major (scanner wrong; each now has a scan-fixes entry)
M1. **9.719, *Teucris* (unflagged).** The scanner split Te-u (15). Right: im-mī | sit-quĕ Fŭ | gam Teu | crīs ā | trum-quĕ Tĭ | mō-rem (14).
M2. **9.721, half-line (flagged COSTLY 8.4).** The scanner forced a hexameter by lengthening *a-ni* and *de-us*. Right: bel-lā | tōr-qu(e) ă-nĭ | mō dĕ-ŭs | in-cĭ-dit, a spondee and three dactyls (11). The last syllable is marked ×, as 5.815 and 2.787 (half-lines ending in a full dactyl).
M3. **9.725, *latis umeris* (unflagged).** Right count, wrong quantities: the scanner made *lātīs* short-short and *ŭmĕ-* long-long. Right: ob-nī | xus lā | tīs ŭ-mĕ | rīs mul | tōs-quĕ sŭ | ō-rum (14).
M4. **9.756, *trepida… Troes* (unflagged).** The scanner read *Troes* as one syllable and made *trĕ-pĭ-* long-long and *-ne* long (14). Right: Dif-fŭ-gĭ | unt ver | sī trĕ-pĭ | dā for | mī-dĭ-nĕ | Trō-ĕs (15). This matches the note's "two syllables".
M5. **9.761, half-line (UNRESOLVED).** ē-gĭt ĭn | ad-ver | sōs, a dactyl, a spondee and one syllable (6).
M6. **9.767, *Noemona… Prytanim* (unflagged).** The scanner read *Noe-* as a diphthong and lengthened the wrong *-que* (15). Right: Al-can | drum-qu(e) Hă-lĭ | um-quĕ Nŏ | ē-mŏ-nă | quē Prў-tă | nim-que (16). The *-que* before *Pr-* is long, as Homer's τε is before Πρύτανιν. This confirms the drafter's query.
M7. **9.772, *vastatorem Amycum* (unflagged).** Right count, wrong quantities: the scanner made *-tā-tō-* short-short and *Ă-mў-* long-long. Right: vas-tā | tō-r(em) Ă-mў | cum quō | nōn fē | lī-cĭ-ŏr | al-ter (14). Compare *nunc Amyci casum*, 1.221.
M8. **9.779, *Teucri* (COSTLY 1.5, under the flag threshold).** The scanner split Te-u (15). Right: con-vĕ-nĭ | unt Teu | crī Mnes | theus ā | cer-quĕ Sĕ | res-tus (14).
M9. **9.787, *Aeneae* (COSTLY 1.2, under the threshold).** The scanner split *Ae-* and shortened *-nē-* (15). Right, as 1.92: et mag | n(i) Ae-nē | ae seg | nēs mĭ-sĕ | ret-quĕ pŭ | det-que (14).
M10. **9.791, *Teucri* (unflagged).** The scanner split Te-u (15). Right: ā-crĭ-ŭs | hōc Teu | crī clā | mō-r(e) in | cum-bĕ-rĕ | mag-no (14).
M11. **9.805, *Teucrorum* (unflagged; missing from the drafter's eu list).** The scanner split Te-u (14). Right: nī Tur | nus cē | dat Teu | crō-rum | moe-nĭ-bŭs | al-tis (13).

### Medium
1. **Note 731–733, "The subject is Turnus throughout."** This is false: *nova lux* is the subject of *effulsit*, *arma* of *sonuere*, and *cristae* of *tremunt*. Only *mittit* has Turnus as its subject. The note now opens "Everything here is Turnus's (his eyes, his armour, his crest), though only 'mittit' has him as its subject." In the same note I also dropped "ablative of separation" from *oculis*: "from" or "in his eyes" are both defended, and the gloss stands without the label.

### Low
- **L-S1. 9.760: carrier entry.** The scanner's fit is right (14 syllables). The line is entered only because it shares a unit with the unresolved half-line 761, as 9.466/9.519 were.
- **L-S2. 9.811: confirmation entry.** It is flagged COSTLY 2.2, but the scanner's parse is right: ic-tĭ-bŭs | in-gĕ-mĭ | nant has | tīs et | Trō-ĕs ĕt | ip-se (15). The line is entered only to clear the flag, as with the 2.x Laocoön lines.
- **L1. Note 739.** The elision list left out *null(a) hinc*. Added.
- **L2. Note 743–744.** *nodis et cortice crudo* are not ablatives of description: they go with the adjective *rudem*, "rough with". Corrected.
- **L3. `l` 748b.** "for not is this man…" misread *is*, which here means "such a one", as the note says. It is now "for not such is of weapon or of wound the author.”"
- **L4. `l` 760–761.** "but fury, blazing, …" made *ardentem* agree with *furor*. *ardentem* is the object (Turnus). It is now "but fury the blazing man, and of slaughter mad desire, / drove against those facing him."
- **L5. Note 760.** The note quoted *furor… et… insana cupido*, but the Latin has *caedisque*. It now quotes "'furor… caedisque insana cupido'".
- **L6. Note 765–767.** Added "'Noemona' four, No-e-mo-na, and the '-que' before 'Prytanim' is long, as Homer's 'te' is before 'Prytanin'", to match M6.
- **L7. Note 768–770a.** *dexter* is now hedged: "probably 'on the right' (some take it 'with his right hand')". The drafter flagged it as an interpretation, but the note gave it flat.
- **L8. `i` 792b–796 (lion simile).** "a crowd of men… crowds in upon" repeated itself, and the sentence kept the order and wording most English versions of this simile share; it was recast. It now reads: "As when a throng of men bears hard with hostile weapons on a savage lion, and he, shaken yet still fierce, with a baleful glare, gives ground slowly; anger and courage forbid him to turn tail, yet, much as he longs to, he cannot drive at them through the spears and the men:"
- **L9. Note 792b–796.** *Ceu* alone is "as". The note now glosses "'Ceu… cum', 'as when'".
- **L10. Note 799–800.** The first *bis* does not stand at the head of its clause (*Quin etiam bis tum*). The note now says "one in each clause".
- **L11. `i` 816b–818 (Tiber ending).** "returned him, washed clean of the slaughter, rejoicing to his comrades" followed the order and key words of well-known modern versions too closely; it was recast. It now reads "the river, with its yellow flood, received him as he came, held him up on gentle waves, and sent him back glad to his comrades, the slaughter rinsed away."
- **L12. Note 816b–818.** "in Book VIII the same river had welcomed Aeneas as his friend (8.62–64)" overstated what those lines do: there Tiberinus names himself to Aeneas in a dream. The note now says "the river god had shown himself to Aeneas as his helper (8.62–64)".

## Changes — pass 2
- **P2-1. Note 731–733.** The new opening's comma chain is now bracketed: "Everything here is Turnus's (his eyes, his armour, his crest), though only…".
- **P2-2. `i` 768–770a.** "lunging with flashing sword" is now "lunging with his flashing sword".

## Scan-fixes entries added (13)
| key | reason | syllables |
|---|---|---|
| 9.719 | *Teucris*, Greek eu | 14 |
| 9.721 | half-line; scanner forced a hexameter (flagged COSTLY 8.4) | 11 |
| 9.725 | *lātīs*, *ŭmĕrīs* | 14 |
| 9.756 | *Trōĕs* two syllables, *trĕpĭdā* | 15 |
| 9.760 | carrier for half-line 761 (scanner right) | 14 |
| 9.761 | half-line (UNRESOLVED) | 6 |
| 9.767 | *Nŏēmŏnă* four syllables; -que long before *Pr-* | 16 |
| 9.772 | *vāstātōrem*, *Ămўcum* | 14 |
| 9.779 | *Teucri*, Greek eu | 14 |
| 9.787 | *Aenēae*, initial Ae- (as 1.92) | 14 |
| 9.791 | *Teucri*, Greek eu | 14 |
| 9.805 | *Teucrorum*, Greek eu | 13 |
| 9.811 | confirmation, clears COSTLY 2.2 (scanner right) | 15 |

## Hand-scan notes on the special lines (scanner right, no entry)
- **800 *fugā***: bīs cōn | fū-să fŭ | gā pēr | mū-rōs | āg-mĭ-nă | vēr-tit. Right, and it is the only fit: the third foot needs a long *-ā*, and *confūsā* cannot also be long, because the fourth syllable *fŭ-* cannot begin a foot. The drafter's reading (*confusa* with *agmina*) stands.
- **748 *neque enim is***: ēf-fŭ-gĭ | ēs nĕ-qu(e) ĕ | n(im) īs tē | lī nēc | vōl-nĕ-rĭs | auc-tor (15). There are two elisions, and *is* is long by position. Right.
- **752 *concussa est***: the scanner treats it as prodelision (`cus–sa est–`). Right.
- **735 *Aeneadae***, **774 *Aeoliden***: *Ae-* one syllable. Right. **803 *aëriam***: four syllables. Right.
- **781**, **812 *Mnestheus***: eu one syllable. Right.
- **807 *iniectis***: the count and quantities are right (in- long before the consonantal i); only the division is `i–niec`. No entry, consistent with 070's refusal for *coniecto* (070 review, item 14).
- **794 / 797 *retro***: *re-* is lengthened before *tr*. This is the only fit in both lines. Right.
- **753 *cerebro*** (*-rē-* long before *br*), **755 *utroque*** (*ū-* before *tr*), **730 *tigrim***: right.
- **720**: the scanner's fit is right (17 syllables). No carrier is needed, because 721 is COSTLY, not UNRESOLVED, so the unit keeps its `sc`.
- **739 *null(a) hinc***, **804 *german(ae) haud***, **782 *moeni(a) habetis***: elision across h. Right.

## Refused or upheld findings
1. **9.781 `tenditis? ”inquit` (misprint, upheld).** This is a closing mark joined to the next word, as 9.377, 9.392 and 9.423 (all checked in the source). The note opens in the rule-5b form. `t` keeps the print, and `l`/`i` close the quotation after *tenditis?*. The mark stays inside one unit, so the per-unit counts agree in all three layers.
2. **No other misprints.** Punctuation and capitals after stops are regular through 717–818. The Latin Library differences are editorial readings, not errors: 724 `magna`/`multa`, 764 `tergum`/`tergus`, 770 `desectum`/`deiectum` and 782 `quae iam`/`quaeve`. None changes the sense, so none is noted (upheld). The orthographic variants are ignored per conventions.
3. **746 *veniens*** taken with an understood *volnus*, with the Juno alternative given. Upheld.
4. **800 *fugā*** ablative, *confusa* with *agmina*. Upheld; the metre proves it.
5. **748** elision list (*nequ(e) enim*, *en(im) is*). Upheld.
6. **752** prodelision note. Upheld.
7. **811** drafter's scan. Upheld; it is entered only as a confirmation.
8. **783–785 *ediderit… miserit*** called perfect subjunctive in an indignant question. Upheld. Some take them as future perfect indicative, but the note's label is the usual one and the sense is the same.
9. **762 *Phalerim*** called a Greek accusative. It is the Latinised form of Greek -ιν. Upheld.
10. **778 *Teucri*** as an adjective with *ductores*. Upheld; it is a defensible construal.
11. **730 *non* with *viderit***, **773** the understood verb, and **805** *ni Turnus cedat* as the reported threat: all are hedged. Upheld.
12. **798 *improperata* "a rare word"**: as far as I know, Lewis & Short cite only this passage. Kept as "a rare word", which is safe either way.
13. **777 bracketed line** kept inside [ ] in the 774–777 unit and noted. Upheld.
14. **Attributions from memory, confirmed:**
    - Iliad 4.440 and 15.119 (Deimos and Phobos)
    - Iliad 19.365–366 (Achilles' eyes)
    - Iliad 5.4–7 (fire from Diomedes' helmet and shield)
    - Iliad 5.678 (the four names, Odysseus)
    - Iliad 11.548–555 (Ajax as a retreating lion)
    - Iliad 16.102–111 and 16.109–110 (Ajax worn down at the ships)
    - Iliad 8.397–408 (Iris sent to Hera and Athena)

    Kept as written. The drafter left Ennius's tribune (Macrobius 6.3) uncited, and I agree with that.
15. **Echo check.** Apart from L8 and L11, no distinctive echo of a known English version was found. "Have you no pity… and no shame" (786–787) and "his gasping breath shook his weary limbs" (814) are the plain sense of the Latin. Upheld.
16. **Unit cuts.** 771b–773 ends at a comma because 771b–776 has no stronger stop and would be six lines. 722–726, 792b–796 and 801–805 are five lines each. Upheld; no boundary is wrong.
17. **Advisory: none (upheld).** Pandarus's head split in two (750–755) is battle killing, consistent with 067–070. QUESTIONS item 61 is still open, and the drafter's ready lede is there if the owner rules otherwise.
18. **Note 737–738 "promised to you as a dowry" (`i`).** The palace is the dowry Turnus expects with Lavinia, not one formally promised to him. This is a loose but fair paraphrase of *dotalis regia*. Upheld.
19. **`l` 727–730 and 791–792a** keep Virgil's order at some cost to English ("…press on, great,"). This follows the conventions' "show the hyperbaton when it teaches something", and the notes explain the frames. Upheld.
20. **`about`, title, part names.** They are accurate and contain no echo. Unchanged.

## For the owner (QUESTIONS.md)
- **Misprint (rule 5b, t as printed, l/i corrected, note opens with the print's reading):** 9.781 `tenditis? ”inquit` (closing mark joined to the next word).
- **Doubtful quantities on the only fit:**
  - 9.767: the *-que* before *Prytanim* is lengthened, following Homer's τε Πρύτανιν.
  - 9.794 and 9.797: *rē-trō*.
- **Unchecked attributions from memory:** Iliad 4.440, 15.119, 19.365–366, 5.4–7, 5.678, 11.548–555, 16.102–111, 8.397–408.
- **Advisory:** none taken (item 61 open).
