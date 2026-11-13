# Review — aeneid-060 (Aeneid VIII.306–406), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 46 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's rule-5b calls (8.310 `miratur`, 8.336 missing ”, 8.366 `dixit`, 8.404 `tuis. ”Ea`) and every attribution marked "(from memory)".

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.131, 6.684 (QUESTIONS item 40), 6.792–794, 7.315, 7.560, 7.594, 7.599, 8.51–54, 8.104, 8.122, and the internal pointers 315, 317, 325, 343, 346, 357, 364–365, 370, 374, 378, 380, 389 and 397. Three needed changing:
- **8.122** was cited as a case of `inquit` set inside a speech. It prints `ait`, not `inquit` (item 21).
- **357** was quoted as *pater Ianus*. The text has *Ianus pater* (item 31).
- **378 and 380** were called "two successive lines". They are not, because 379 comes between them (item 28).

**Pass 2** re-read every edited field in full and made three more changes (P2-1 to P2-3).

**Scansion.** I hand-scanned all 101 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with my scansion syllable by syllable.
- **The scanner was wrong on 9 lines**: 308, 311, 355, 356, 367, 372, 380, 385 and 397. Only 372 was flagged (COSTLY 3.0); the other eight were wrong with no flag. Each now has a hand entry.
- **The other six flagged lines are right**: 341, 345, 377, 383, 384 and 402 get no entry (R5).
- **8.323 `tutis` cannot scan as printed**, because the ablative plural has a long *-īs*. This is treated as a rule-5b misprint for *tutus* (item 10). The scanner's own fit already gives the quantities of *tutus* (tū-tŭs ĭn), so no entry is needed (R7).

Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and a script checked that count against its entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 9 entries apply
- **all 46 units get `sc`**
- all 101 lines pass the validator's metre check
- the scanner report keeps only the COSTLY flags on 341, 345, 377, 383, 384 and 402, which are confirmed right

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 46 units. I checked this by script against a fresh run of `make_units.py` into the scratchpad, whose output was identical to the drafter's `units.json` before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 24 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Note lengths.** Eight drafter notes were over 140 words: units 4, 11, 13, 14, 29, 44 and 45, plus unit 6 after the misprint was added. All are now trimmed (item 32). Every note is now 15–140 words; the longest is 140.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 99 insertions, 0 deletions, trailing newline kept, formatting as before (`indent=1`, no ASCII escaping). The new keys come after 8.301, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Speech marks.** These were checked in `t`, `l` and `i`. There are five speeches: Evander at 314–336, 351–358 and 362–365, Venus at 374–386, and Vulcan at 395–404.
- In `l` and `i`, each speech has “ on its first unit (4, 18, 24, 29, 40) and ” on its last (11, 22, 25, 34, 45).
- `l` has 5 “ and 5 ”.
- `i` has 6 and 6, because unit 18's `i` puts "he said" outside the marks (R11).
- `t` has 5 “ and 4 ”, because the print has no closing mark at 336. **The validator will warn about this, which is expected.**

**Severity counts: major 10, medium 4, low 25 (22 in pass 1, 3 in pass 2). Refused findings: 16. Scan-fixes entries added: 9.**

## Changes — pass 1

### Major
1–9. **Scansions the scanner got wrong.** Each line now has a hand entry with its reason.
   - **Initial Ae- split in two**:
     - **8.308 *Aenean***: et cŏ-mĭ | t(em) Ae-nē | ān iux | tā nā | tum-quĕ tĕ | nē-bat (14 syllables). The scanner had 15.
     - **8.311 *Aeneas***: Ae-nē | ās că-pĭ | tur-quĕ lŏ | cīs et | sin-gŭ-lă | lae-tus (15). The scanner had 16.
     - **8.367 *Aenean***: in-gen | t(em) Ae-nē | ān dū | xit strā | tīs-quĕ lŏ | cā-vit (13). The scanner had 14.
     - **8.380 *Aeneae***: et dū | r(um) Ae-nē | ae flē | vis-sem | sae-pĕ lă | bō-rem (13). The scanner had 14.
   - **Consonantal i after a prefix — 8.355 *disiectis***: Haec dŭ-ŏ | prae-tĕ-rĕ | ā dis | iec-tīs | op-pĭ-dă | mū-rīs (15). The scanner read di-si-ec- and had 16.
   - **Synizesis preferred — 8.356 *reliquias***: rē-lĭ-quĭ | ās vĕ-tĕ | rum-quĕ vĭ | dēs mŏ-nĭ | men-tă vĭ | rō-rum (17, five dactyls). The scanner read *re-liqu-ias* and had 16. The precedent is 7.244.
   - **8.372 (COSTLY 3.0) *Volcanum adloquitur***: Vol-cā | n(um) ad-lŏ-quĭ | tur thă-lă | mō-qu(e) haec | con-iŭ-gĭs | au-reō (15).
     - *Volcānus* has a long ā, *ad-* is long by position, and *lŏquĭtur* has two short syllables.
     - The scanner's fit had the same syllable count with four wrong quantities.
   - **8.385 *coeant***: As-pĭ-cĕ | quī cŏ-ĕ | ant pŏ-pŭ | lī quae | moe-nĭ-ă | clau-sīs (16). The scanner read *coe-* as a diphthong and had 15. The precedent is 7.317.
   - **8.397 *Teucros***: tum quŏ-quĕ | fās nō | bīs Teu | crōs ar | mā-rĕ fŭ | is-set (14). The scanner split Te-u and had 15.

10. **8.323 `tutis`: a misprint the draft missed (rule 5b).**
    - The ablative plural *tūtīs* has a long *-īs*, and the fifth foot cannot take it. The line scans only as *tū-tŭs ĭn | ō-rīs*.
    - *tutus* is also the Latin Library's reading. The drafter had translated *tutis* and said "the sense comes to much the same".
    - The note now opens with the house formula, "The print has 'tutis', a misprint for 'tutus', corrected here; t keeps the print…". It adds that the line is scanned with *tutus*, as with *vidit* for the print's *videt* at 6.684 (QUESTIONS item 40).
    - The Latin Library paragraph was replaced by "'tutus', 'safe', goes with Saturn".
    - `l` "since in these he had lain hid, safe, shores" now reads "since he had lain hid, safe, in these shores".
    - `i` already read *tutus* ("he had lain hidden safe"), so it is unchanged.

### Medium
11. **Note 324–325, a false label.** It said "'quae perhibent'… the antecedent drawn into the relative clause". *saecula* stands outside the clause. It now reads "a relative clause set between 'Aurea' and its noun; 'aurea' can also be taken inside it, 'the ages they call golden'."
12. **Note 337–341, a false label.** It said "the antecedent drawn into the relative clause and the words framing it". *portam* precedes *quam*; it is *Romani* and *nomine* that belong to the relative clause and stand before *quam*. The note now says so.
13. **Note 342–344, a wrong construction.** It took "'Parrhasio… Lycaei', 'Parrhasian (= Arcadian) Lycaean', framing the line around 'Panos'" as one phrase. *Parrhasio* goes with *de more*, and *Lycaei* goes with *Panos*.
    - The note now reads "'Parrhasio… de more', 'after the Parrhasian (= Arcadian) custom', interlaced with 'Panos… Lycaei', 'of Lycaean Pan'".
    - "'dictum… de more', 'named after the custom (of)'" now reads "'dictum', 'named', agrees with 'Lupercal'".
14. **Note 351–352, a false claim.** It said Seneca quotes the line "to describe the awe of a deep grove (Letter 41)". In Letter 41 Seneca applies *quis deus incertum est, habitat deus* to the god dwelling in every good man; the grove passage is separate. It now reads "Seneca quotes 'quis deus incertum est, habitat deus' of the god who dwells in every good man (Letter 41, from memory)."

### Low
15. **Note 306–307**: "framing the clause across the line" now reads "split across the line around 'ad urbem'".
16. **Note 313**: "Readers have often noticed the irony…", an unverifiable claim about readers, now reads "There is a point in it: …".
17. **Note 319–320**: "'aetherio… Olympo'… framing the line" was wrong, since *Primus ab* comes first. It now reads "enclosing 'venit Saturnus'".
18. **Note 330–332**: "the Greek accusative ending '-im'" now reads "the accusative in '-im', as in 'Tiberim'". The Greek ending would be -ιν; *-im* is the Latin i-stem accusative.
19. **`l` 344**: "from Parrhasian named, of Pan, after the custom, Lycaean" was opaque and misconstrued (see item 13). It now reads "named after the Parrhasian custom of Lycaean Pan", falling back on the sense.
20. **Note 345–346**: "'sacri… nemus Argileti'… framing the line" now reads "enclosing 'monstrat nemus'". **`l` 345**: "Also and of sacred he shows the grove, Argiletum," read *Argileti* as apposition. It now reads "And also of the sacred he shows the grove, of Argiletum,".
21. **Note 351–352**: "(as at 7.594 and 8.122)" now reads "(7.594 'inquit', 8.122 'ait')", because 8.122 prints *ait*.
22. **Note 359–361**: "'pauperis Euandri'… framing the line's beginning" now reads "at the head of the line".
23. **`l` 361**: "in the Roman Forum and in the elegant lowing Carinae" made the Carinae low. It now reads "lowing in the Roman Forum and in the elegant Carinae", with the infinitive moved to make sense.
24. **Note 364–365**: "'rebus… egenis'… dative with 'veni'" now reads "dative with 'non asper' (or with 'veni', 'come to')". *asper* + dative is the more natural construction.
25. **Note 369**: cut "as in the south", an unsupported gloss.
26. **Note 370–373**: added that *Volcanum* has a long *a*, *Vol-cā-num*. This agrees with the 372 entry.
27. **Note 374–378**: "'Argolici… reges'… framing the line" now reads "enclosing 'vastabant Pergama'".
28. **Note 379–380**: "ending two successive lines" now reads "ending 378 and 380".
29. **Note 387–388**: "'niveis… lacertis'… framing the clause" now reads "enclosing 'hinc atque hinc diva'".
30. **`i` 391–392**: "when the thunder breaks, a fiery fissure splits the storm-clouds with its quivering light" detached *rupta* from *rima* and turned *percurrit* into "splits". It now reads "a fiery rift, torn open by the flashing thunder, runs gleaming through the storm-clouds with its light", which matches `l`.
31. **Note 394**: "as 'pater Ianus' at 357" now reads "as 'Ianus pater' at 357".
32. **Note lengths and wording, in eight notes**:
    - **Over the 140-word limit** (the validator warns): units 4 (166 words), 11 (168), 13 (164), 14 (165), 29 (151), 44 (153) and 45 (169), and unit 6 after item 10. All were trimmed to 140 or fewer.
    - **Restatements and glosses cut**: unit 44's closing sentence restated its first one, and unit 45 had "the body relaxing into sleep after love". Repeated glosses were shortened.
    - **Unchanged**: no claim, label or scansion pointer was altered by the trimming.
    - **Unit 14's *rettulit* note**: "as though the grove had already been a refuge in Evander's day" was cut. The "restored" reading is still given.
33. **Note 395–396**: "'quo'… placed second in its clause, after the verb" was wrong, since *quo* is third. It now reads "held back until after the subject and verb".
34. **Note 400–402**: "a spondaic fifth foot, 'po-test ē-lec-trō'" now reads "'-test ē-', before 'lec-trō'". This matches the scansion.

Items 15–34 make the 20 numbered low items. Items 20 and 32 each count twice (two separate corrections each), which gives the 22 pass-1 lows.

## Changes — pass 2
- **P2-1 (low), note 333–336**: the trim had left "corrected here: Evander's speech (from 314) ends here", with "here" twice. It now reads "the speech begun at 314 ends at 336". The quoted *pelagi extrema* was restored to the printed *pelagique extrema*.
- **P2-2 (low), note 321–323**: "(as 'vidit' at 6.684)" was unclear. It now reads "(as 'vidit' for the print's 'videt' at 6.684)".
- **P2-3 (low), note 351–352**: item 21 had produced "his habit with a verb of speaking set into a speech (…)", which repeats the sentence. It is now "his habit (7.594 'inquit', 8.122 'ait')".

## Scan-fixes entries added (9)
These are appended after 8.301 in line order:
- **Initial Ae- (4)**: 8.308, 8.311, 8.367 and 8.380
- **Consonantal i (1)**: 8.355
- **Synizesis (1)**: 8.356
- **Wrong quantities, flagged COSTLY (1)**: 8.372
- **coeant (1)**: 8.385
- **Greek eu (1)**: 8.397

Each entry matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 13–17 syllables and one ×.

## Hand-scan notes on the special lines (scanner right, no entry)
- **8.341 (COSTLY 4.0), right**: Ae-nĕ-ă | dās mag | nōs et | nō-bĭ-lĕ | Pal-lan | tē-um (14 syllables). *Aenĕădas* has a short *nĕ* and *ă*. *Pallantēum* is four syllables, so the line is spondaic.
- **8.345 (COSTLY 2.3), right**: Nec nōn | et sā | crī mons | trat nĕ-mŭs | Ar-gī | lē-tī. *sācri* is long by position before *cr*; the alternative *et să-crī* is not a dactyl, because *-crī* is long. The fifth foot is spondaic (*Argīlētum*).
- **8.377, 8.384 (COSTLY 2.1), right**: *coniunx* is divided *co–niunx*. This is a cosmetic division with the right quantities, as at 393, which has no flag. It is the open question in QUESTIONS item 37 (R6).
- **8.383 (COSTLY 2.1), right**: … fī-lĭ-ă | Nē-rei, with *Nerei* two syllables by synizesis.
- **8.402 (COSTLY 2.0), right**: quod fĭ-ĕ | rī fer | rō lĭ-quĭ | dō-vĕ pŏ | test ē | lec-trō. The fifth foot is spondaic.
- **Greek eu**:
  - *Euandrus* (313) and *Euandri* (360) are right.
  - *Teucros* (397) is fixed.
- **Initial Ae-**:
  - *Aeneadas* (341) is right, as are *aevo* (307), *aetherio* (319), *aetas* (326), *aegida* (354), *aeterno* (394) and *Aeneae*'s final *-ae*.
  - Fixed: 308, 311, 367 and 380.
- **Consonantal i**:
  - *coniugis* (372, 406), *coniunx* (377, 384, 393), *iungere* (316), *Iovis*/*Iovem*, *Ianus*/*Ianiculum*, *iam*, *iuxta*, *Troiam* and *Tarpeiam* (347, Tar-pē-iam) are right.
  - *disiectis* (355) is fixed.
- **Synizesis**:
  - *aureo* (372), *Nerei* (383) and *huic* (358, one syllable) are right.
  - *reliquias* (356) is fixed.
  - *dehinc* (337) is two syllables here, dic-tă dĕ | hinc. With one syllable, the second foot would be dic-tă-dehinc (– ⏑ –), which does not scan (1.131 is the monosyllabic case).
- **Hiatus**: there is none in the part. *subiit haec* (363) is not hiatus: *-īt* is long in the third-foot arsis, as the drafter's note says.
- **Other quantities checked**:
  - *vēnit*, the perfect (319)
  - *Ĭtali*, short (331); with a long I the line cannot be fitted
  - *Asȳlum* (342)
  - *Pānos* (344)
  - *rēligio* (349)
  - *Sĭcānae* (328)
  - *ēgere* (335)
  - *ineluctabile* with long *ē* (334)
  - *excĭdium* with short *ĭ* (386), as at 1.22 and 2.643
  - *placidā* (325), *patriā* (333), *gelidā* (343) and *meā* (401), ablatives with a long *-ā*
  - *tonitrū* (391)
  - *amplexū* (388)

## Refused findings
- **R1 — 8.310 `miratur`**, lowercase after the stop ending 309: **upheld** as a rule-5b misprint. This is consistent with 8.9, 8.79, 8.124, 8.217, 8.285 and 7.290. The general ruling asked in QUESTIONS item 43 is still open.
- **R2 — 8.336, no closing mark after `Apollo.`**: **upheld** as handled. `t` stays as printed, `l`/`i` close the speech, and the note opens with the print's reading. This follows 8.137 `orbes` and 7.320 `iugalis` (a dropped mark recorded as a note).
  - It could instead be a rule-5 source correction (add ” and re-pin), but prior parts have not done that for a dropped mark.
  - *Vix ea dicta* (337) shows the speech is over, so the reading is not doubtful.
- **R3 — 8.366 `dixit`**, lowercase after the closing mark ending 365: **upheld**, as R1.
- **R4 — 8.404 `tuis. ”Ea`**: **upheld**. The mark cannot be split from *Ea* in `t`, so the last unit carries 404–406. This follows 7.560, 7.599 and 5.400. Unit 44 ends at a comma, which the build allows.
- **R5 — 8.341, 345, 377, 383, 384 and 402 (COSTLY)**: all fits are right, so there are no entries. They stay in the build's scanner report.
- **R6 — *co–niunx*** division (377, 384, 393): cosmetic, with the right quantities, so there is no entry (058 R9, QUESTIONS item 37).
- **R7 — 8.323**: no scan-fixes entry. The scanner's fit (tū–tĭs⏑ ĭn⏑) already has the quantities of the corrected *tutus*, on the printed word.
- **R8 — Note 337**: the remark on *dehinc*, which stands in the next unit, is kept. It is true, and it is harmless where it is.
- **R9 — Note 366–368**: *stratis* is kept with *foliis*. It could also be the noun "bedding", with *foliis et pelle* going with *effultum*. The sense is the same.
- **R10 — `i` 394, "the fire-god" for *pater***: kept. It identifies the speaker, and `l` keeps "the father".
- **R11 — `i` 351**: "“This grove,” he said, “this hill…" adds a pair of marks round "he said". The marks balance, and this is the house practice for *inquit* inside a speech.
- **R12 — Attributions kept, hedged "from memory" and unchecked against a text**:
  - Odyssey 19 (Penelope's "oak or rock")
  - Hesiod, Works and Days (the golden race under Kronos)
  - Georgics 2 (*Saturnia tellus*)
  - Livy 1 (Tiberinus drowned in the Albula; Romulus's asylum)
  - Servius on Argus and the Argiletum
  - Iliad 17 (Zeus shaking the aegis)
  - Seneca, Letters 18 and 31 (*Aude, hospes*) and 41 (*quis deus*; corrected, item 14)
  - Iliad 18 (Thetis), the lost cyclic epic for Memnon's arms, and Iliad 14 (Hera and Zeus)
  - L&S on *indubitare*

  All are right as far as I remember. "Night 'swift' in Homer" (θοὴ νύξ) is a standard epithet and is kept unhedged.
- **R13 — The `i` echo check**: I found no distinctive echo of a published version. Units 25 and 27 were checked with care (*Aude, hospes*; *Nox ruit*), and their wording is our own.
- **R14 — `title`, `titleEn`, `part` and `about`**: these are accurate and our own, and were left unchanged.
- **R15 — `t` marks**: `t` has 5 “ and 4 ”, which is correct for this print (R2). The validator's WARN is expected.
- **R16 — Note 362–363, *subiit* "the old long '-īt' of the perfect"**: kept. Lengthening in arsis at the caesura is the other account, and the quantity is the same either way.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading.
  - 8.310 `miratur` and 8.366 `dixit`, lowercase after a stop (the ruling in item 43 is still open)
  - 8.336 no closing mark after `Apollo.` (a rule-5 source correction is possible instead)
  - 8.404 `tuis. ”Ea`
  - **8.323 `tutis` for `tutus`, new in review.** It is unmetrical as printed, and *tutus* is the Latin Library's reading. Whether Greenough's 1881 page prints *tutis*, or the TEI does, could not be checked.
- **Doubtful quantities on the chosen fit**:
  - 8.328 *Sĭcānae*, short Si-
  - 8.331 *Ĭtali*, short I-
  - 8.342 *Asȳlum*, long -sy-
  - 8.344 *Pānos*
  - 8.337 *dehinc* as two syllables
  - 8.363 *subiīt*, long
  - 8.372 *aureo* and 8.383 *Nerei* by synizesis
  - 8.345 *sācri*, long by position
- **Build report**: COSTLY flags on 341, 345, 377, 383, 384 and 402 will still show. Each was checked by hand and is right, and no entry was made.
- **Unchecked attributions** are as listed in R12.
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
