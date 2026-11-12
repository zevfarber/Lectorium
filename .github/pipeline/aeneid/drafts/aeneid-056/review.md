# Review — aeneid-056 (Aeneid VII.706–817), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 39 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's flagged items: the dative readings at 724 *curru*, 731 *flagello* and 761 *bello*; 787 *tam magis… quam magis*; 811 *celeris*; the doubtful pointing at 7.751 *oliva.* + *Archippi*; and the Latin Library variants. Those variants are 716 *Hortinae*/*Ortinae*, 757 *volnera*, 776 *aevom*, 798 *colles*/*collis* and 811 *tingueret*/*tingeret*. All five are spelling or morphology, and none changes the sense. I also checked every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched. In-poem cross-references were checked against the pinned source:
- I.522 and I.535: Ilioneus's speech, *nimbosus Orion*
- 7.371–372: *Inachus Acrisiusque patres*
- 7.409–410: Danae's founding of Ardea
- VI.288: *flammisque armata Chimaera*
- IX.612–613: *semperque recentis / comportare iuvat praedas et vivere rapto*, cited in note 748
- 7.647–648: *contemptor divom Mezentius*
- 7.10ff.: the Circaean shore
- 7.150 and 7.242: Numicus
- 7.804: *agmen agens*, again

**Pass 2** re-read every edited field in full and made one more change (P2-1).

**Scansion.** I hand-scanned all 112 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. For the half-line, the check was the validator's half-line rule (feet 1..k with k < 6, one ×, a `why` that begins "Half-line"). Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself, gives an **empty scanner report**: the two COSTLY flags (746, 789) and the UNRESOLVED half-line (760) are all cleared. All 112 lines pass the validator's check, and **all 39 units get `sc`**. The half-line 760 closes the unit 759–760, so 759 needed a carrier entry.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 39 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 21 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- Every note is 15–140 words. The drafter's 706 (172 words) was trimmed to 140.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 102 insertions, 0 deletions, trailing newline kept. The new keys come after 7.705, in line order.
- `gloss.json` was not touched (the glosser is working on it in parallel).
- The build was not run (it writes the published files and the manifest). Its scansion step and the validator's scansion check were replicated instead.

**Speech marks.** There are none in this stretch: `t`, `l` and `i` each have 0 “ and 0 ”.

**Severity counts: major 5, medium 5, low 28 (27 in pass 1, 1 in pass 2). Refused findings: 17. Scan-fixes entries added: 9.**

## Changes — pass 1

### Major
1–5. **Scansions the scanner got wrong with no flag.** Each line fit six feet with the right syllable count, so nothing warned, but the quantities were wrong. Each line now has a hand entry.
   - **7.719 *ubi Orion***: the scanner made *-vus* and *u-* long and *O-* and *-ri-* short. Hand scansion: sae-vŭs ŭ | b(i) Ō-rī | ōn hī | ber-nīs | con-dĭ-tŭr | un-dīs. With *ubi* elided, only the long Ō fits. It is short at I.535.
   - **7.764 *placabilis***: the scanner made *plā-cā-* short-short and *-bĭ-lĭs* long-long. Hand scansion: lī-tŏ-ră | pin-guĭs ŭ | b(i) et plā | cā-bĭ-lĭs | ā-ră Dĭ | ā-nae.
   - **7.785 *crinita iuba***: the scanner made *crī-nī-* short and *-tă iŭ-* long. Hand scansion: cui trĭ-plĭ | cī crī | nī-tă iŭ | bā gă-lĕ | (a) al-tă Chĭ | mae-ram. *Cui* is one syllable (a drafter flag), as the scanner also has it.
   - **7.803 *Hos super advenit Volsca de***: the scanner made *sŭ-* and *-pĕr* long and *Volscā* and *dē* short. Hand scansion: Hōs sŭ-pĕr | ad-vē | nit Vols | cā dē | gen-tĕ Că | mil-la, with *advēnit* as the perfect.
   - **7.815 *levis umeros***: the scanner made *lē-vīs* short-short and *ŭ-mĕ-* long-long. Hand scansion: vē-lĕt hŏ | nōs lē | vīs ŭ-mĕ | rōs ut | fī-bŭ-lă | crī-nem.

### Medium
6. **7.789** (COSTLY 2.0), **wrong as flagged**: the scanner read *Io* as one syllable and made *cornibus* a spondee with *-bus* long, giving 13 syllables. Hand scansion: At lē | vem clĭ-pĕ | um sub | lā-tīs | cor-nĭ-bŭs | Ī-ō, 14 syllables. *Lēvem* is long, as the drafter said; *levem* cannot scan with a short e.
7. **7.746** (COSTLY 2.1): I confirmed the scanner's parse by hand and entered it to clear the flag: hor-rĭ-dă | prae-cĭ-pŭ | ē cui | gens ad | suē-tă-quĕ | mul-tō. *Cui* is one syllable and *adsueta* has a consonantal u.
8. **7.760** (UNRESOLVED), the half-line *te liquidi flevere lacus.*: tē lĭ-quĭ | dī flē | vē-rĕ lă | cūs, three and a half feet, entered as at 7.702.
9. **Carrier 7.759**: the scanner's fit is right (checked by hand: *Angĭtĭae*, *vitreā*, *Fūcinus*). Without it, the unit 759–760 would get no `sc`.
10. **Note 783, a wrong Homeric attribution**: "Homer says much the same of Ajax and of Agamemnon (Iliad 3)". In Iliad 3 Agamemnon is *not* the tallest; Priam says others are taller by a head. The note now gives Ajax only, "taller than the Greeks by head and shoulders".

### Low
11. **Note 706, Livy**: "an Attus Clausus" now reads "Attius Clausus, at Rome Appius Claudius". "Livia's first husband and her son Tiberius" is simplified to "Tiberius, Livia's son and Augustus's stepson".
12. **Note 706, length**: 172 words, trimmed to 140. Cut: the gloss of *a quo*, the doubled rendering of *postquam…*, and the closing sentence on *nunc*.
13. **Note 712**: "All are Sabine places" now reads "All lie in or near the Sabine country". Nomentum is often counted Latin.
14. **Note 715**: the Latin Library's *Ortinae* was cut. It is spelling only, and conventions say to note a variant only where the sense changes.
15. **Note 718, *marmor***: "the Greek 'marmaros' meant 'glittering'" was wrong, since μάρμαρος is a stone. It now reads "is a gleaming stone, a word felt to go with 'marmairo', 'glitter'".
16. **`l` 727 (line 729)**: "of the river shallow / the neighbour, Volturnus," made *Volturni* an apposition to *accola*. It now reads "the neighbour, of Volturnus", since *Volturni* is genitive with *amnis*.
17. **Note 730**: "'aclydes' is a Greek word" now reads "a rare word, Greek in form". The etymology is uncertain.
18. **`i` 733, an echo precaution**: "Nor shall you go unsung in my verses" now reads "Nor shall my verses pass you by in silence".
19. **Note 736**: the claim "Lewis & Short derives 'avellana'…" was an attribution I cannot check. It now reads "the hazelnut was called 'nux Abellana' after the town".
20. **Note 748**: "almost the same line again in Book IX" now gives IX.613, with *comportare*, checked against the pinned text.
21. **`i` 759, an echo precaution**: "For you the grove of Angitia wept, for you the Fucine lake with its glassy water…" now reads "Angitia's grove wept for you, Fucinus wept for you with its glass-clear water, the bright lakes wept for you."
22. **Note 761, *bello***: the dative of goal is kept (the `l` follows it). The note now adds "(it may also go with 'pulcherrima', 'most splendid in war')".
23. **Note 761, *circum***: "placed after its adjective" now reads "set between adjective and noun".
24. **Note 797, Numicus**: "Aeneas was said to have vanished in it at his death (a story Livy… tells)" overstated Livy, who puts the grave by the river. It now reads "passed from the earth beside it (Livy, from memory, puts his resting-place there)".
25. **Note 797**: the Latin Library's *collis* was cut (morphology only).
26. **`i` 803**: "Last of all comes Camilla" does not render *Hos super*, and it was a stock phrasing. It now reads "Over and above these came Camilla", which also matches the perfect *advēnit*.
27. **Note 808, *celeris***: "most naturally goes with 'plantas'" claimed a preference I cannot vouch for. The note now gives both constructions and says the metre does not decide. The Latin Library's *tingeret* was dropped from the spelling note.
28. **`i` 812**: the draft gave the marvelling to the young men and the gazing to the mothers, but both verbs have both subjects. It now reads "All the young folk, streaming out of houses and fields, and the crowding mothers marvel at her and gaze after her as she passes,".
29–37. **Scansion pointers added to notes**, to go with the fixes and the doubtful quantities:
   - the long Ō of *Orion*, with *ubi* elided (718)
   - *adsueta* three syllables (746)
   - the half-line's scansion (759)
   - *plācābilis* (761)
   - *ardentis* lengthened at the pause before *haud* (781)
   - *crīnīta*, *iŭbā* and *cui* (785)
   - *lēvis*/*lĕvis* in macrons, and *Io* as Ī-ō (789)
   - *advēnit* as the perfect (803)
   - *lēvīs ŭmĕrōs* (814)

Items 11–37 are the 27 pass-1 lows. Item 22 hedges a reading that is otherwise kept (R4).

## Changes — pass 2
- **P2-1 (low)**: note 808's new clause "'celeris nec' is long either way" was loose. It now reads "'-ris' is long by position before 'nec' either way".

## Scan-fixes entries added (9)
Appended after 7.705 in line order, each with its reason:
- 7.719, 7.764, 7.785, 7.803 and 7.815 (no flag, wrong quantities)
- 7.746 (COSTLY, confirmed) and 7.789 (COSTLY, wrong)
- 7.759 (carrier) and 7.760 (UNRESOLVED half-line)

Each matches its line's words under `WORD_RE`. The eight full lines each have six feet, five –⏑⏑/–– feet then –×, 14–16 syllables and one ×. 760 passes the validator's half-line rule (feet 1–4, one ×, a `why` that begins "Half-line"). In the replicated build all 9 apply, the scanner report is empty, all 112 lines pass, and 39 of 39 units get `sc`.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *Teutonico* (741) is one syllable, which is right. *euntem* (813) is ĕ-un-, not the diphthong, and is right. There is no *Teucri*, *Eurus* or *Orpheus* in this part.
- **Initial Ae-**: these are right as the scanner reads them:
  - *Aequicula* (747), Ae-quī-cŭ-la, with the long ī needed by the fifth foot
  - *aetheria* (768), ae-thĕ-rĭ-(a), elided
  - *Aetnaeos* (786), Aet-nae-ōs
  - *aeratae*, *aereus* (743)
  - *aequora* (728, 738) and *aequore* (781, 811)
- **Consonantal i/u**: no prefixed *-iicio/coniunx* forms in this part. Right: *adsueta* (746, 806); *Troiani* (723); *cateias* (741), ending tē-iās; *tingueret* (811), gu consonantal; *iungit*, *iuxta*, *iuvat*, *iuvere*, *iuvenem*, *Iuppiter*, *iugum* and *iuventus*. *iuba* (785) is fixed for its quantity.
- **Hiatus**: none. Every vowel meeting is an ordinary elision, for example *nymphae Egeriae* (775), *Trivia Hippolytum* (774), *Nursia, et* (716) and *galea alta* (785).
- **Other lines checked and right**:
  - *Rōsea* (712), *Tĕtrica* (713), *Ērēti* (711), *Ămĭterna* (710) and *Sătīculus* (729)
  - *Tĕlōn* and *Sēbēthide* (734); *Tēlĕbŏum* (735)
  - *Rŭfras*, *Bătŭlum* and *Cĕlemnae* (739); *mālĭferae* (740); *sūbere* (742)
  - *Marrŭvia* with *vēnit* as the perfect (750)
  - *Paeŏniis* (769), short o as at XII.401; *Īnachus* (792)
  - *Săcrānae* and *sacrum* (796–797), long by position before *cr*
  - *Fērōnia* (800); *vallīs* (802)
  - *celeris nec* (811), and *ardentīs haud* (781), which is lengthened at the caesura

## Doubtful quantities and readings entered or left on the only fit
- **7.719 *Ōrīōn***: entered with long Ō. It is short at I.535 and IV.52, so the long O here rests on the metre with *ubi* elided.
- **7.789 *Ī-ō***: entered as two long syllables in the sixth foot. The long Ī rests on the metre.
- **7.781 *ardentis haud***: the final *-is* is lengthened at the penthemimeral caesura before h. This is the scanner's fit and the only fit, so no entry.
- **7.746 and 7.785 *cui***: one syllable, Virgil's usage, and the only fit in both lines.
- **No entry, the scanner's fit and the only fit**: *Rōsea* (712), *Rŭfras* (739), *Tĕlōn* (734), *Marrŭvia* (750) and *Fērōnia* (800).

## Refused findings
- **R1 — 7.751 *oliva.* + *Archippi***: the drafter's "doubtful, keep" call is **upheld**. The stop leaves 752–755 without a main verb, and the sense would run more easily on a comma, with *missu* and *Umbro* hanging on *venit* (750). But the capital *Archippi* agrees with the stop, so this is a consistent (if harsh) editorial pointing and not an obvious slip of type. It is the same case as 7.695 *Faliscos.* + *Hi* in aeneid-055. A verbless sentence with *venit* understood also reads. Rule 5b's "doubtful → keep and say so" applies, and the note already says so. Kept.
- **R2 — 724 *curru* as dative** (= *currui*, "yokes the horses to the chariot"): this is the usual construction with *iungo*, and it agrees with the `l`. The ablative is possible, but there is no reason to change. Kept.
- **R3 — 731 *flagello* as dative with *aptare*** ("fit these to a thong"): *apto* takes the dative. Kept.
- **R4 — 761 *bello* as dative of goal**: kept as the reading the `l` and `i` follow. The alternative, *pulcherrima bello*, was added to the note only (item 22).
- **R5 — 787 *tam magis… quam magis***: "an old correlative pair in place of the usual 'quo magis… eo magis'" is right, since the pair is archaic (Plautus, Lucretius). Kept.
- **R6 — Latin Library variants**: 716, 757, 776, 798 and 811 are all orthography or morphology, and none changes the sense. No note is needed. Two such mentions were cut (items 14 and 25).
- **R7 — Homer**: these are kept, and they fit my recollection of the Greek, but none was checked against a text:
  - leaves and flowers (Iliad 2), note 718
  - the earth groaning under the host (Iliad 2), note 722
  - the cloud of infantry (Iliad 4), note 793
  - the mares of Erichthonius (Iliad 20), note 808
  - Ajax (Iliad 3), note 783
- **R8 — Other attributions kept from memory**:
  - Servius on Halaesus (723) and on *Virbius* = *vir bis* (774)
  - Pindar, Pythian 3 (770)
  - Horace, Satires 1.5, on Feronia (797)
  - Livy on Attius Clausus (706)
  - Lewis & Short on *classes* (715) and *caetra* (732)
  - Euripides's *Hippolytus* (765)
  - the Allia in 390 BC and the *dies Alliensis* (715)
  - Marius and the Teutones (741)

  All are hedged or standard. Kept.
- **R9 — 7.781 *ardentis haud***: the scanner's fit is right, so there is no entry (see the doubtful list).
- **R10 — cosmetic syllable divisions in the scanner's fits** (*Sa–cra–* 796, *sa–crum* 797, *a–gris* 812): the quantities are right, so there are no entries (as aeneid-055 R17).
- **R11 — the place-name quantities in the list above**: the scanner is right on the only fit, so there are no entries.
- **R12 — `l` 774 present *recondit* against past "hid" in `i`**: the historic present is rendered as past in real English. Kept.
- **R13 — note 759 "address the dead man"**: the landscape's weeping implies Umbro's death, and the note already calls these lines his epitaph. Kept.
- **R14 — note 814 "Book VIII turns to Aeneas"**: Book VIII opens on Turnus's war-signal and turns to Aeneas at 8.18. That is close enough for an end-of-book pointer. Kept.
- **R15 — note 785 "Turnus is the fire of this war"**: interpretive, but it is offered as such. Kept.
- **R16 — further `i` echoes**: nothing more found. "Shields ring", "taller than all the rest by a full head" and "She could have flown over the tips of a field of standing corn" are plain renderings, not a translator's turns. `title`, `titleEn` and `part` are our own and unchanged.
- **R17 — speech marks**: none expected and none present. Confirmed.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: none called. Kept as doubtful: 7.751 *oliva.* + capital *Archippi*. The sense wants a comma, but the capital agrees with the stop (as 7.695).
- **Doubtful quantities on the chosen fit**:
  - 7.719 *Ōrīōn*, long O (short at I.535 and IV.52)
  - 7.789 *Ī-ō*
  - 7.781 *ardentis* lengthened before *haud*
  - 7.712 *Rōsea*, 7.739 *Rŭfras*, 7.734 *Tĕlōn*, 7.750 *Marrŭvia*, 7.800 *Fērōnia*

  None was checked against an edition or dictionary.
- **`make_units.py` is stale**: `drafts/aeneid-056/make_units.py` still holds the drafter's strings. Re-running it would discard this review.
- **Unchecked attributions, from memory**:
  - Iliad 2 (twice), 3, 4 and 20
  - Servius on Halaesus and on *vir bis*
  - Pindar, Pythian 3
  - Horace, Satires 1.5
  - Livy 1 (Aeneas by the Numicus) and Livy 2 (Attius Clausus)
  - Euripides's *Hippolytus*
