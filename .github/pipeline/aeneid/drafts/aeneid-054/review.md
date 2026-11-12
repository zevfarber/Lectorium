# Review — aeneid-054 (Aeneid VII.475–600), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 54 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the speech marks, the drafter's six rule-5b calls (7.551, 7.552, 7.560, 7.594, 7.596, 7.599), the Latin Library variants that matter (7.543 *convexa*/*conversa*, 7.551 *veniunt*/*veniant*; the rest are spelling), and every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched. Every in-poem cross-reference was checked against the pinned source:
- 1.76 (*Aeolus haec contra*), 1.150 (*furor arma ministrat*), 1.159 and 1.530 (*Est… locus*)
- 2.426–427 (*iustissimus unus qui fuit in Teucris*, Rhipeus), 2.733 (*prospiciens; “Nate*, added here)
- 4.169–170 (*ille dies primus leti primusque malorum causa fuit*), 6.468 (*lenibat*)
- 7.59–80 (the bees and Lavinia's hair), 7.96–101 (Faunus), 7.317 (*coeant*, added here in scansion notes), 7.318 (*sanguine Troiano et Rutulo dotabere, virgo*), 7.327 (*odere sorores*), 7.385–405 (Amata in the woods), 7.456–457 (the torch), and the internal back-references 491, 493, 505–508, 506, 533, 541–542
- 1.754 and 8.351 (*inquit* printed inside a speech without marks, added here)

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 126 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself, gives an **empty scanner report**: the four COSTLY flags and the UNRESOLVED line are all cleared. All 126 lines pass the validator's check, and **all 54 units get `sc`**. The UNRESOLVED line (566) needed two carrier entries (565 and 567), because the unit 565b–567 would otherwise get no `sc`.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 54 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 21 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words. The drafter's 540 (177 words) and 475 (147) were trimmed to 136 and 138.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 214 insertions, 0 deletions, trailing newline kept. The new keys come after 7.472, in line order.
- The build was not run (it writes the published files and the manifest). Its scansion step and the validator's scansion check were replicated instead.

**Speech marks.** Allecto, 545–551: “ on *En*, ” after *agros.* Juno, 552–560: “ on *Terrorum*, ” after *regam.* (the print's ” stands at the head of the next unit, see R1). Latinus, 594–599: “ on *Frangimur*, ” after *spolior.* (likewise). `t` has 3 “ and 3 ”; `l` and `i` each have 4 and 4, because they break the speech round *inquit* at 594 (R4). Nothing was changed.

**Severity counts: major 12, medium 8, low 25 (23 in pass 1, 2 in pass 2). Refused findings: 17. Scan-fixes entries added: 19.**

## Changes — pass 1

### Major
1–12. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the syllables or quantities were wrong. Each line now has a hand entry.
   - **7.476 *Teucros***: the scanner split Teu- into Te-u. Hand scansion: Al-lēc | t(o) in Teu | crōs Stў-gĭ | īs sē | con-cĭ-tăt | ā-lis.
   - **7.487 *Adsuetum***: the scanner read ad-su-e-tum with a short su. The u of *suē-* is a consonant (as 7.33 *adsuetae*). Hand scansion: ad-suē | t(um) im-pĕ-rĭ | īs sŏ-rŏr | om-nī | Sil-vĭ-ă | cū-rā.
   - **7.495 *ripaque… viridante***: the scanner made *rī-pā* short-short and *vĭ-rĭ-* long-long. *Ripā* is an ablative. Hand scansion: dē-flŭ-ĕ | rēt rī | pā(que) aes | tūs vĭ-rĭ | dan-tĕ lĕ | vā-ret.
   - **7.508 *telum ira facit***: the scanner made *tē-* and *ī-* short and *-ră fă-* long. Hand scansion: rī-mān | tī tē | l(um) ī-ră fă | cit vŏ-căt | ag-mĭ-nă | Tyr-rhus.
   - **7.529 *sese… mare***: the scanner made *sē-sē* short-short and *mă-* long (as at 7.286 and 7.472). Hand scansion: pau-lā | tim sē | sē tol | lit mă-r(e) ĕt | al-tĭ-ŭs | un-das.
   - **7.546 *coeant***: the scanner read *coe-* as one syllable by synizesis. It is *cŏ-ĕ-ant*, as in the entry at 7.317. Hand scansion: dīc ĭn ă | mī-cĭ-tĭ | am cŏ-ĕ | ant et | foe-dĕ-ră | iun-gant.
   - **7.564 *fama… memoratus***: the scanner made *fā-mā* short-short and *mĕ-mŏ-* long-long. *Fama* is ablative. Hand scansion: nō-bĭ-lĭs | et fā | mā mul | tīs mĕ-mŏ | rā-tŭs ĭn | ō-ris.
   - **7.573 *regina manum***: the scanner made *rē-gī-* short-short and *-nă mă-* long-long. Hand scansion: im-pō | nit rē | gī-nă mă | num rŭ-ĭt | om-nĭs ĭn | ur-bem.
   - **7.578 *Teucros***: Te-u split again. Hand scansion: ter-rō | r(em) in-gĕ-mĭ | nāt Teu | crōs in | rēg-nă vŏ | cā-ri.
   - **7.582 *coeunt***: synizesis again. Hand scansion: un-dĭ-quĕ | col-lec | tī cŏ-ĕ | unt Mar | tem-quĕ fă | tī-gant.
   - **7.594 *fatis… ferimur***: the scanner made *fā-tīs* short-short and *fĕ-rĭ-* long-long. Hand scansion: fran-gĭ-mŭr | heu fā | tīs in | quit fĕ-rĭ | mur-quĕ prŏ | cel-la.
   - **7.598 *parta quies***: the scanner read *quies* as one syllable and lengthened *-ta* (as 3.495, the same words). Hand scansion: Nam mĭ-hĭ | par-tă quĭ | ēs om | nis(que) in | lī-mĭ-nĕ | por-tus.

### Medium
13. **7.478** (COSTLY 2.0), **wrong as flagged**: *Iulus* is Ĭ-ū-lus, three syllables (house practice since 1.556). Hand scansion: in-sĭ-dĭ | īs cur | sū-quĕ fĕ | rās ă-gĭ | tā-băt Ĭ | ū-lus.
14. **7.493** (COSTLY 2.0), **wrong as flagged**: *Iuli* likewise. Hand scansion: Hunc prŏ-cŭl | er-ran | tem ră-bĭ | dae vē | nan-tĭs Ĭ | ū-li.
15. **7.524** (COSTLY 3.2), **wrong as flagged**: the scanner made *dū-rīs* short-short, split *prae* into pra-e and read *eus* as a diphthong. *Praeustis* is prae-us-tis with *prae* shortened before the vowel (the 5.186 entry already cites this line). Hand scansion: stī-pĭ-tĭ | būs dū | rīs ă-gĭ | tur sŭ-dĭ | būs-vĕ prae | us-tis.
16. **7.566** (UNRESOLVED): *urguet* is two syllables, ur-guĕt, as in the entry at 7.241. Hand scansion, five dactyls: ur-guĕt ŭ | trim-quĕ lă | tus nĕ-mŏ | rīs mĕ-dĭ | ō-quĕ fră | gō-sus.
17. **Carriers 7.565 and 7.567**: the scanner's fits are right (checked by hand). Without them the unit *densis… torrens* would get no `sc`.
18. **7.547** (COSTLY 2.1): I confirmed the scanner's parse by hand and entered it to clear the flag: Quan-dŏ quĭ | d(em) Au-sŏ-nĭ | ō rēs | per-sī | san-guĭ-nĕ | Teu-cros.
19. **Note 552, the semicolon called a misprint**: reversed. *Tum contra Iuno; “Terrorum* reads the same with a colon or a semicolon, so the print is not something the sense allows only one way to read (rule 5b). Greenough prints the same semicolon before a speech at 2.733 (*prospiciens; “Nate*), and that part kept it without comment. The note now says the semicolon is kept as printed and is not treated as a misprint. `l` keeps "Juno:" as English punctuation.
20. **Note 553, a false label**: "the antecedent is drawn into the relative clause and stands at its end" was wrong. *Arma* stands outside the relative clause, as the object of *imbuit*. The note now reads "the relative clause comes first, and its antecedent 'arma' waits for the end of the main clause, as the object of 'imbuit'".

### Low
21. **Note 479**: "'Subitam… rabiem' framing the line" was wrong (*Hic* comes first and *Cocytia virgo* last). It now reads "the adjective held apart from its noun by 'canibus'".
22. **Note 511**: "'Saeva… dea' framing the line" was wrong (*At* comes first and *nocendi* last). It now reads "the adjective set well apart from its noun".
23. **Note 516, geography**: "far apart and far from the Latin coast" was not true of Lake Nemi, which is near the coast. It now reads "Both lie far inland", of the Nar and the Velinus.
24. **Note 516, Apollonius**: "Argonautica 4.136–138" was a line reference from memory that I cannot vouch for. It now reads "Apollonius's Argonautica (Book 4)".
25. **Note 498, "another sacred deer"**: Silvia's stag is a pet, not sacred. It now reads "another deer whose killing cost dear: the stag of Artemis that Agamemnon shot…".
26. **Note 490**: "'Ad limina nota' and 'domum', accusative of place to which" called a prepositional phrase a bare accusative. It now gives the label to *domum* only.
27. **Note 563, *valles***: the note said "valleys", while `l` and `i` said "valley". The note now says *valles* is probably the by-form of *vallis*, though it may be plural.
28. **Note 586, an unverified claim about editors**: "some editors have suspected 586" now reads "Some take the two lines for alternative drafts left in the unrevised poem; Greenough prints both."
29. **Note 594, *inquit***: the note now says that leaving the marks out round *inquit* is Greenough's habit (1.754, 8.351), not a misprint (see R4).
30. **`l` 577**: "the terror redoubles" read as intransitive. It now reads "the terror he redoubles".
31. **`i` 523, an echo precaution**: "a dark harvest of drawn swords bristles far and wide" now reads "far and wide the drawn swords bristle like a dark field of grain".
32. **Notes 540 and 475, length**: 540 dropped "The capital after the colon, where a speech opens, is Greenough's habit". The capital is on *En*, the first word of the speech, so it says nothing. Both notes were trimmed to under 140 words, and the substance is kept.
33–43. **Scansion pointers added to notes**, to go with the fixes:
   - *Teucros* two syllables and *Iulus* three (475)
   - *adsuetum* three syllables (487)
   - *rīpā* and *Iuli* (493)
   - *praeustis* (523)
   - *sēsē* and *măre* (528)
   - *coeant* (546)
   - *fāmā* (563)
   - *urguet* two syllables (565)
   - *coeunt* (580)
   - *fātis* and *fĕrĭmur* (594)
   - *quies* and *parta* (598)

## Changes — pass 2
- **P2-1 (low)**: in note 516, the new sentence repeated "in Sabine country" from the sentence before it. It now reads "Both lie far inland".
- **P2-2 (low)**: in note 586, two clauses were run together with semicolons. The sentence is now split.

## Scan-fixes entries added (19)
Appended after 7.472 in line order, each with its reason:
- 7.478, 7.493, 7.524 (packet COSTLY flags, all three wrong), 7.547 (COSTLY, confirmed)
- 7.566 (UNRESOLVED), 7.565 and 7.567 (carriers)
- 7.476, 7.487, 7.495, 7.508, 7.529, 7.546, 7.564, 7.573, 7.578, 7.582, 7.594, 7.598 (no flag, wrong syllables or quantities)

Each matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 13–17 syllables and one ×. In the replicated build all 19 apply, the scanner report is empty, and all 126 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *Teucros* at 547 (line end) and *heu* (594) are right. 476 and 578 are fixed.
- **Initial Ae-**: none in this part. *aestus* (495), *aera* (526), *aethera* (530), *aequo* (540) and *aetherias* (557) are ordinary diphthongs, and right.
- **Consonantal i after a prefix**: *obicit* (480, ō-bĭ-cĭt) and *coniugia* (555, con-iŭ-gĭ-a) are right. *Iulus/Iuli* (478, 493) are fixed. Also right: *iuvenis* (531), *iustissimus* (536), *iungant* (546), *Iunonem*/*Iuno*/*Iunonis* (544, 552, 592), *iam* (523), *iactant* (527).
- **Hiatus**: none in this part. Every vowel meeting is an ordinary elision (e.g. *Allecto in* 476, *dextrae erranti* 498, *neque enim* 581, *Ipsi has* 595).
- **Other lines checked and right**: *Tyrrhīdae* (484), *ērĭlī* (490), *āfuit* (498), *vēnit* perfect (499), *rĕfūgit* (500), *quă-drŭ-pēs* (500), *lăcessīta* (527), *Nār* (517), *Trō-ĭ-a* (521), *Ĕrīnys* (570), *quīs* (570), the 13-syllable spondaic 561 *Illa autem attollit*, and *ĕ-ūnt rēs* (592).

## Doubtful quantities and readings entered or left on the only fit
- **7.546 *coeant* and 7.582 *coeunt***: both readings fit the meter. The entries take cŏ-ĕ-, three syllables, following the entry at 7.317, instead of the scanner's synizesis.
- **7.545 *tibī***: the final i is long at the beat before *bello*. This is the scanner's fit and the only one; no entry.
- **7.484 *Tyrrhīdae***: the long ī is needed by the meter, although a patronymic from a second-declension name would usually have a short i. Scanner's fit; no entry.
- **7.521 *āgricolae*, 7.551 *āgros*, 7.595 *sācrilego***: each is long by position before a stop and liquid, on the only fit. Scanner's fits; no entry.
- **7.524 *prae***: shortened before a vowel (entry).
- **7.499 *vēnit***: the perfect, on the only fit. `l` and `i` say "came" and "went".

## Refused findings
- **R1 — 7.560 *regam. ”Talis* and 7.599 *spolior. ”Nec***: the drafter's misprint calls are **upheld**. The closing mark set after a space and joined to the next word is a slip that recurs some 85 times in the pinned text. Parts 035 and 040–044 treat it as a misprint, `t` as printed and `l`/`i` closing the speech. Kept.
- **R2 — 7.551 *veniunt***: the drafter's misprint call is **upheld**. *Ut* here can only introduce purpose or result, both of which need the subjunctive, and no indicative sense ("as they come") fits a future plan. The Latin Library reads *veniant*. The sense allows only one reading. `t` is as printed, and `l`/`i` read *veniant*. Kept.
- **R3 — 7.596 *O miseri***: the capital O is Greenough's habit, not a misprint. He prints a capital O mid-sentence about forty times (1.76 *Tuus, O regina*, 2.281, 3.103, 3.560). Lower-case *o* also occurs, about twenty times, mostly in Books 4 and 8–11. The note says so. Kept.
- **R4 — 7.594 *inquit* without marks**: Greenough's habit, not a misprint (1.321, 1.754, 2.78, 2.387, 8.351, 8.362, 10.491, 11.42, 12.259 and more). `l`/`i` add the marks, as aeneid-043 did at 6.318. Kept.
- **R5 — Iliad 11.3–14 (Strife on Odysseus' ship), 13.339 (*ἔφριξεν δὲ μάχη*), 2.455–458 (the gleam reaching heaven), 4.422–428 (the wave simile), 15.618–621 (the rock)**: kept. I recall the Greek of each and the line numbers fit, but they were not checked against a text (see below).
- **R6 — Almo, a stream just south of Rome; Amsanctus among the Hirpini; Lake Nemi below Diana's grove at Aricia; the Nar white with sulphur and fed by the Velinus**: kept. These are the standard facts, from memory.
- **R7 — Agamemnon's stag at Aulis**: the story is right, from memory (the stag of Artemis that held the fleet). Only the "sacred deer" framing was changed (item 25).
- **R8 — note 493, *aestus* "accusative plural"**: correct. The accusative singular would be *aestum*. Kept.
- **R9 — note 540, *convexa*/*conversa***: kept, shortened. Both readings are given, and `l`/`i` follow Greenough.
- **R10 — the wording "corrected here; t keeps the print" in the notes at 549, 559 and 599**: the house wording since aeneid-035. Kept.
- **R11 — note 577, *igni* as the heat of the crowd's passion**: one standard reading. Kept.
- **R12 — note 481, *quae* agreeing with *causa***: right (attraction to the predicate noun). Kept.
- **R13 — note 481, the quotation of 4.169 starts "ille" in lower case where the print has *Ille***: a quotation set inside a sentence. Kept.
- **R14 — cosmetic syllable divisions** (*in–te–3xens* 488, *cir–4cums–tant* 585): the quantities are right, so there are no entries (as aeneid-053 R15).
- **R15 — `i` echoes elsewhere**: nothing further found. "We are shattered, alas, by fate", "my rest is won" and "let fall the reins of state" are plain renderings, not a translator's turns.
- **R16 — `title`, `titleEn`, `part`, `about`**: our own, and the summary is accurate. Unchanged.
- **R17 — note 594 and the other notes that say "l and i"**: pipeline shorthand, but the house uses it in published notes (aeneid-030 onward). Kept.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: three upheld and one reversed. Upheld, with `t` as printed and `l`/`i` corrected:
  - 7.551 *veniunt* for *veniant*
  - 7.560 *regam. ”Talis* and 7.599 *spolior. ”Nec* (closing marks joined to the next word)

  Reversed: 7.552 *Iuno;*, a semicolon before a speech, is kept as printed and not treated as a misprint. The sense is the same, and 2.733 has the same thing. Not misprints, and recorded as Greenough's habits: 7.594 *inquit* inside a speech with no marks, and 7.596 a capital *O* mid-sentence.
- **Doubtful quantities**:
  - 7.546 *coeant* and 7.582 *coeunt*, entered as three syllables. Both fit, and the scanner chose synizesis.
  - 7.545 *tibī*
  - 7.484 *Tyrrhīdae* with a long ī
  - 7.521 *āgricolae*, 7.551 *āgros* and 7.595 *sācrilego*, long by position
  - 7.524 *prae* shortened

  None was checked against an edition.
- **`make_units.py` is stale**: `drafts/aeneid-054/make_units.py` still holds the drafter's strings. Re-running it would discard this review.
- **Unchecked attributions, from memory**:
  - Iliad 11.3–14, 13.339, 2.455–458, 4.422–428, 15.618–621
  - Apollonius, Argonautica Book 4 (the dragon's hiss and the mothers; line numbers cut)
  - the Almo as a stream just south of Rome, and Amsanctus in Hirpine country
  - Agamemnon's stag and Aulis
  - the view that 586–587 are alternative drafts
  - *olli* "with an Ennian ring"
  - *ilicet* as the formula of dismissal

  None was checked against a text in this run.

## After review (orchestrator)
- The build refused units 34/35 and 52/53, which split the print's tokens `regam. ”Talis` (7.560) and `spolior. ”Nec` (7.599) mid-word. Following aeneid-050 (7.116 `consumimus, ”inquit`), each pair was merged into one unit (`t` re-joined from the cut text, `l`/`i`/`n` concatenated). 52 units.
- Unit at 7.599: one sentence cut from the note to bring it under 140 words.
