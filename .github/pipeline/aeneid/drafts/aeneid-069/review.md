# Review — aeneid-069 (Aeneid IX.530–620), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 36 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked the drafter's four misprint calls (9.561, 9.567, 9.601, 9.620), the two doubtful readings kept as printed (9.579 `manus`, 9.584 `Matris`), the Latin Library variants, the no-advisory decision, the `about`, the title and part names. I read every `i` for echoes of the well-known English versions, most closely Numanus's taunt (598–620) and the two similes (551–555, 563–566).

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.183, 6.228, 6.448, 6.644, 7.496–499, 9.43, 9.465, 9.506, 9.509–511, 9.521–522, 9.769, 10.145, 10.576 and 12.298. One was off: the historic infinitive *effundere* is at 9.509, not 511 (item L4). *aggere* occurs 16 times elsewhere in the print, as the drafter says; *agere* only at 9.567.

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 91 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with mine syllable by syllable. The packet flagged nothing, and the scanner reported nothing.
- **The scanner was wrong on 6 lines, none flagged**: 535, 552, 555, 585, 615 and 618. Each now has a hand entry (items M1–M6).
- **553 *inicit***: the scanner's quantities are right but its syllable division (`i–ni⏑cit⏑`, an open long i-) is not; entry added as for *obicis* at 4.549 (item L1).
- The drafter's other worries are cases where the scanner is right (see "Hand-scan notes" below): 569 *Ilioneus* (`neus` already one syllable), 584 *Symaethia*, 600 *conubia*, 609 *versaque iuvencum*, 571 *Corynaeum*, 546 *Maeonio*, 573 *Caeneus*.
- **567 *agere***: no entry. The scanner already marks the printed word `a–ge⏑re⏑`, long-short-short, which is the scansion of *aggere*, and any entry would hold exactly the same string. This follows 8.323 *tutis*, which has no entry for the same reason.

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet, then –×/⏑×. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 7 entries apply
- **all 36 units get `sc`**
- all 91 lines pass the validator's metre check
- the scanner report is empty.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`, as the drafter's file was.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 36 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn` and `part` are unchanged. `about` has two small corrections (L21, L22).
- **16 units changed** (0, 1, 2, 3, 4, 6, 9, 12, 16, 20, 21, 22, 24, 26, 33, 34). `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks.** `t`, `l` and `i` each have 2 “ and 2 ”, on the same units:
  - Turnus to Lycus opens and closes in the 560b–562 unit.
  - Numanus opens in the 598–599 unit and closes at the end of the 619–620 unit (`ferro.”`).
  - This is right.
- **Note lengths.** Every note is 21–126 words; none was over the validator's 140 before or after.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 79 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.520, in line order.
- The build and the validator were not run (`build_aeneid.py` has no dry-run mode). Their scansion steps were replicated instead.
- **`drafts/aeneid-069/` has no `gloss.json`.** The build needs one. That belongs to the glosser's step, not this review.

**Severity counts: major 6, medium 2, low 24 (22 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 24. Scan-fixes entries added: 7 (6 wrong lines, 1 syllable division).**

## Changes — pass 1

### Major (scanner wrong; each now has a scan-fixes entry)
M1. **9.535, *coniecit* (unflagged).** The scanner read co-ni-e-cit, four syllables with a short co- (14). Right, as the entries at 2.545 and 7.456: Prīn-cēps | ār-dēn | tēm cōn | iē-cīt | lām-pă-dă | Tūr-nus (13).
M2. **9.552, *contra tela furit* (unflagged).** The count was right but the quantities wrong. The scanner made *contră* and *tĕ-* short, and *-lā* and *fū-* long. Right: cōn-trā | tē-lă fŭ | rīt sē | sē-qu(e) haud | nēs-cĭ-ă | mōr-tī (14).
M3. **9.555, *qua tela videt* (unflagged).** The count was right but the quantities wrong. The scanner made *quă* and *tĕ-* short, and *-lā* and *vī-* long. Right: īn-rŭ-ĭt | ēt quā | tē-lă vĭ | dēt dēn | sīs-sĭ-mă | tēn-dit (15).
M4. **9.585, *placabilis* (unflagged).** The count was right but the quantities wrong. The scanner made *plă-că-* short and *-bī-līs* long. Right: flū-mĭ-nă | pīn-guĭs ŭ | b(i) ēt plā | cā-bĭ-lĭs | ā-ră Pă | lī-cī (16).
M5. **9.615, *indulgere choreis* (unflagged).** The scanner made *-reis* one syllable, *iū-* long and *indulgĕre* short (14). Right: *chŏrēīs* is three syllables (as *choreas*, 6.644), and *indulgēre* has the long ē of the second conjugation: dē-sĭ-dĭ | ae cōr | dī iŭ-văt | īn-dūl | gē-rĕ chŏ | rē-īs (15).
M6. **9.618, *adsuetis* (unflagged).** The scanner read ad-su-e-tis as four syllables with a short ē (16). This is the same error as the 9.511 entry. Right, with the u consonantal and both *Dindyma* and *ubi* elided: Dīn-dў-m(a) ŭ | b(i) ad-suē | tīs bĭ-fŏ | rēm dāt | tī-bĭ-ă | cān-tum (15).

### Medium
1. **Note, `l` and `i` 578b–580, *abditaque intus spiramenta animae*.** The draft took *abdita* as the arrow ("the arrowhead, buried inside"). The natural reading, and the usual one, has *abdita* (neuter plural) agreeing with *spiramenta*: "the hidden breathing-passages of life". The arrow, understood, is the subject of *rupit*. Changes:
   - `n` now explains the agreement.
   - `l` now reads "and the hidden within / breathing-ways of life with a deadly wound it burst".
   - `i` now reads "and the shaft tore open with a deadly wound the hidden passages of his breath deep inside him".
2. **`l` ↔ `i` and note 556–558, *muros tenet*.** `l` and the note said "makes for the walls"; `i` said "reached the wall". He does reach it, since he is hanging from it at 562 (*pendentem*), and L&S gives *teneo* "reach, gain (a place)". Both `l` and the note now say "gains", so `l` and `i` agree.

### Low
- **L1. 9.553 *inicit*: scan-fixes entry.** The quantities are the scanner's, but the syllables are now `in–i⏑cit⏑` (consonantal i written once after the prefix) instead of an open long `i–`. This follows the entries for *obicis* (4.549) and *subiciunt*. The note already explained *in-yicit*.
- **L2. Note 530–534.** "The storming of a wall goes back to Iliad 12" is now "The assault recalls Iliad 12". The note names a general model, not a source.
- **L3. Note 535–537.** Added: "'coniecit', 'hurled', three syllables, 'con-iecit', the i a consonant." This matches M1 and the 553 note's treatment of *inicit*.
- **L4. Note 538–539a.** The historic infinitive *effundere* is at 509, not 511. Corrected.
- **L5. `i` 539b–541.** *subito* goes with *procubuit*, not with the weight. "under that sudden weight, came crashing down" is now "suddenly came crashing down under their weight".
- **L6. Note 542–544a.** The note said *pectora* was "framed with *duro… ligno*". In fact *duro… ligno* frames *transfossi*, and the note now says so.
- **L7. `i` 542–544a.** "splintered beams" added something not in *duro ligno*. It now reads "the hard timber", matching `l`.
- **L8. Note 545b–548.** *vetitis… armis* frames *ad Troiam miserat*, not the line.
- **L9. Note 556–558.** *alta… tecta* frames *certat prendere*, not just *certat*.
- **L10. Note 563–566a.** *pedibus… uncis* frames *Iovis armiger*, not the line.
- **L11. Note 569–572.** Added the missing elision *subeunt(em) ignisque* (570).
- **L12. Note 578b–580.** Added the missing elision *erg(o) alis* (578).
- **L13. Note 581–585.** *egregiis… armis* frames *Arcentis filius*, not the line.
- **L14. Note 581–585.** *pictus… chlamydem* was called "the accusative of the thing", while the same note compared it with *pectora* (543), which that note calls an accusative of respect. Both are now called accusative of respect.
- **L15. Note 586–589.** Two framing claims were wrong.
  - *stridentem fundam* stands at the head of the line and frames nothing. It is now "object of *egit*", and the framing claim moves to *positis… hastis*, which frames *Mezentius*.
  - *media… tempora* frames *adversi liquefacto*, not the line.
- **L16. Note 595–597.** Added the missing elision *ant(e) aciem* (595).
- **L17. Note 600.** *nostra… conubia* frames *sibi bello*, not the line.
- **L18. Note 614–616.** Added "'choreis' has three syllables, 'cho-re-is'", which matches M5.
- **L19. Note 617–618.** *biforem… cantum* frames *dat tibia*, not "the clause".
- **L20. Note 617–618.** Added the missing elision *ub(i) adsuetis*, and "'adsuetis' has three syllables, the u a consonant", which matches M6.
- **L21. `about`.** "splits with a sling-stone" is now "with a lead sling-bullet". The text says *liquefacto plumbo*, and the note says lead.
- **L22. `about`.** "sleeves and bonneted caps" is now "their sleeved tunics and ribboned bonnets" (*tunicae manicas… redimicula mitrae*).

## Changes — pass 2
- **P2-1. `i` 578b–580.** After the medium change, "an arrow… the arrow" repeated the word. It is now "the shaft".
- **P2-2. Note 586–589.** Punctuation: "framing 'adversi liquefacto'; 'adversi', 'of him facing'."

## Scan-fixes entries added (7)
| key | reason | syllables |
|---|---|---|
| 9.535 | *coniecit* con-iē-cit, consonantal i after prefix | 13 |
| 9.552 | *contrā*, *tēlă*, *fŭrit*: wrong quantities, same count | 14 |
| 9.553 | *inicit* in-ĭ-cĭt: syllable division only (as 4.549 *obicis*) | 14 |
| 9.555 | *quā*, *tēlă*, *vĭdet*: wrong quantities, same count | 15 |
| 9.585 | *plācābilis*: wrong quantities, same count | 16 |
| 9.615 | *chorēīs* three syllables, *indulgēre* | 15 |
| 9.618 | *adsuētis* three syllables (as 9.511) | 15 |

## Hand-scan notes on the special lines (scanner right, no entry)
- **532** *Ĭtălī*, short I: ēx-pūg | nār(e) Ĭ-tă | lī sūm | māqu(e) ē | vērtĕr(e) ŏ | pūm vī, with a monosyllabic ending. Right.
- **539** *retroque*: rē- is long by muta cum liquida (glŏmĕ | rānt rē | trōquĕ rĕ | sīdunt). Right.
- **561** *adripit* and **578** *adlapsa*: the scanner divides these a-dri-, a-dlap-, with the a marked long. The quantities are right, and only the syllable boundary is off. Not entered: the published parts carry *a–dla–bi⏑mur⏑* and *a–dla–bi⏑tur⏑* as the scanner gave them. Refused for consistency.
- **567** *agere* (printed for *aggere*): the scanner gives `a–ge⏑re⏑`, the scansion of *aggere*: tōl-lĭ-tŭr | īn-vā | dūnt ēt | fōs-sās | āg-gĕ-rĕ | cōm-plent (14). No entry needed (precedent 8.323).
- **569** *Ilioneus*: the scanner already takes *-neus* as one syllable: Ī-lĭ-ŏ | neūs sāx | (o) āt-qu(e) īn | gēn-tī | frāg-mĭ-nĕ | mōn-tīs (14). Right.
- **571** Ē-mă-thĭ | ō-nă Lĭ | gēr Cŏ-rў | naē-ūm | stēr-nĭt Ă | sī-lās (16). Right.
- **573** *Caeneus* has -eus as one syllable; *Caenĕă* is the Greek accusative (14). Right.
- **574** Tūr-nŭs Ĭ | tўn Clŏ-nĭ | ūm-quĕ Dĭ | ō-xīp | pūm Prŏ-mŏ | lūm-que (16). Right.
- **584** *Symaethia*: Sȳ- has to be long (ē-dūc | tūm Mā | trīs lū | cō Sȳ | maē-thĭ-ă | cīr-cum, 13). This is the only fit; the quantity is doubtful (cf. the doubtful-quantity lists in QUESTIONS.md items 49–56).
- **600** *conubia*: cō-nū-bĭ-ă, with the u long and the bi a vowel, the only fit at the line end (14). Right.
- **609** *versaque iuvencum*: no elision before consonantal i, *versā* ablative: Ōmn(e) aē | vūm fēr | rō tĕ-rĭ | tūr vēr | sā-quĕ iŭ | vēn-cum (14). Right.

## Refused or upheld findings
1. **9.561 `manus? ”Simul` (misprint, upheld).** This is the closing mark joined to the next word, as at 9.392 `silvae? ”Simul` (QUESTIONS 61), 7.560, 8.404 and 9.22. The note opens in the rule-5b form. The unit carries the narrative to the stop.
2. **9.567 `agere` → `aggere` (misprint, upheld).** It is a dropped letter. *agere* gives no construction with *fossas… complent* and scans only with a false long a. Greenough prints *aggere* 16 times elsewhere, and the Latin Library has *aggere*. Only one reading is possible, so rule 5b applies. The note's opening is correct.
3. **9.601 no mark after `adegit` (misprint, upheld, note only).** The question *Quis deus… quae… dementia adegit* can only end in `?`, and the capital *Non* confirms a stop. Handled as 8.137 and 9.289 (QUESTIONS 52, 60): note only, because the printed page could not be checked for a rule-5 source fix.
4. **9.620 no mark after `Idaeae` (misprint, upheld, note only).** A break is certain, but whether it is `;` or `:` is not. Handled the same way as item 3. The note's wording ("a misprint for a stop (a semicolon is read here)") is accepted as the rule-5b form for a missing mark, as at 9.289.
5. **9.579 `manus` (doubtful reading, kept).** *infixa est lateri manus* is a genuine reading; the Latin Library's *alte* (no *manus*) is a rival reading, not a correction. Both scan. Rule 5b says to keep the print and give the variant, which the note does.
6. **9.584 `Matris` (doubtful reading, kept; not a misprint).** The Latin Library's *Martis* differs from *Matris* by a transposed letter, which could suggest a misprint. But *Matris luco* gives good sense, Greenough capitalises it deliberately (as *Matris Idaeae*, 619), and it is not a case where the sense allows only one reading. So rule 5b's "doubtful readings: keep the print and say so" applies. The note, which does not identify the Mother, is upheld.
7. **Latin Library orthographic variants** (550, 561, 578, 580, 591, 611): ignored per conventions. The note's passing mention of *vires*/*viris* (611) is harmless.
8. **Advisory: none (upheld).** This is ordinary battle killing, consistent with 067 and 068. The general ruling asked in QUESTIONS 61 is still open.
9. **Attributions from memory, confirmed:**
   - Iliad 12.41–48 (Hector like a boar or lion whose courage kills it)
   - Iliad 22.308–310 (Hector like an eagle swooping on a lamb or hare)
   - Iliad 2.235 (Thersites, "Achaean women, no longer Achaean men")
   - Troy taken by Hercules after Laomedon's fraud
   - the Palici
   - the belief that sling-bullets melt in flight (no author named)
   - Cybele's eunuch priests
   - Dindymus and Berecyntus
   - *ferrugo* as a dark red dye
   - *manicae* as effeminate

   Kept as written, apart from the softening of Iliad 12 in L2.
10. **Note 569–572: the sides of Liger and Asilas, and Corynaeus alive at 12.298.** The facts are checked (10.576, 6.228, 12.298) and the "loose end" remark is fair. Upheld.
11. **Note 573–576a: Caeneus "born a woman and made a man", 6.448.** Correct, since 6.448 shows him a woman again among the dead. Upheld.
12. **Note 544b: *Vix unus Helenor et Lycus*.** Upheld.
13. **Note 538: *malorum… fugam*, objective genitive.** Upheld.
14. **Note 548: anacoluthon resumed by *isque*.** Upheld.
15. **Note 586–589: *diffidit* as the perfect of *diffindo*.** Upheld; the present would be *diffindit*.
16. **Note 590–594: personal *dicitur* with Ascanius as subject.** Upheld.
17. **Note 603–606: *venatu* as the old dative.** Upheld (Servius, Conington).
18. **`i` 603–606, "as boys they are up all night for the hunt".** Considered and refused. *invigilo* is "stay awake over, lose sleep for" (L&S), so the rendering is fair.
19. **Note 607–608, "farming and war, the two Roman virtues".** Loose, but a reasonable gloss of the *aut… aut*. Kept.
20. **Note 612–613: raiding honourable in early Italy and Homeric Greece.** General background (cf. Thucydides 1.5). Kept.
21. **Note 609–610a, "framing the line and a half" for *versa… hasta*.** Correct as written. Upheld.
22. **Echo check.** No distinctive echo of a known English version was found in any `i`. *leave weapons to men*, *twice-captured*, *hard race from the root* and *Phrygian women… not Phrygian men* are literal from the Latin. Upheld.
23. **Unit 569–576 split at the comma after *sagitta* (572), into two four-line units.** Upheld.
24. **9.567 scan-fixes entry.** Not added (see Hand-scan notes): the scanner's output on the printed word is already the *aggere* scansion.

## For the owner (QUESTIONS.md)
- **9.601 and 9.620 (missing marks):** handled as note-only misprints, like 8.137, 8.336 and 9.289. If the printed page shows `?` after *adegit* and a stop after *Idaeae*, add them to the source under rule 5 and re-pin aeneid-069; only the notes' openings change.
- **9.584 `Matris` vs *Martis*:** kept as a doubtful reading. If you rule it a misprint, the 581–585 note should open "The print has 'Matris', a misprint for 'Martis', corrected here", and `l`/`i` should read "grove of Mars".
- **Doubtful quantity on the only fit:** 9.584 *Sȳmaethia*.
- **Scanner syllable division *a-dl-*/*a-dr-*** (561, 578; published *adlabimur*/*adlabitur*): left as the scanner gives them. Say if you want ad- compounds entered as the ob-/sub- compounds were.
- **Unchecked attributions from memory:** Iliad 12 as a general model; Iliad 12.41–48, 22.308–310, 2.235; the melting sling-bullet; raiding honourable in early Italy.
