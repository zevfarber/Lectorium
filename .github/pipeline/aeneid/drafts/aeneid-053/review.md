# Review — aeneid-053 (Aeneid VII.373–474), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 51 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the speech marks, the rule-5b question at 7.401 (*Siqua*), the Latin Library variants that matter (7.430 *arma*/*arva*; the rest are spelling), and every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched. Every in-poem cross-reference was checked against the pinned source:
- 2.150 and 5.28 (capital after a mid-speech colon, added here), 2.314 (*arma amens capio*), 2.325 (*fuimus Troes*)
- 4.173–197 (Fama), 4.381 (*I, sequere Italiam*), 4.693 (*Iuno omnipotens*, for the note on *omnipotens*), 5.618–620 (Iris as *Beroë*)
- 7.98 (*externi venient generi*), 7.321–322 (*funestae… taedae*), 7.371–372 (*Inachus Acrisiusque patres*), 7.409 (*Rutuli*), and the internal back-references 378, 380, 384, 385, 425, 428, 440–442, 444, 452–453
- 10.720 (*profugus hymenaeos*, added here), 1.85 (*Notusque*, cited in a scan-fixes reason)

**Pass 2** re-read every edited field in full and made one more change (P2-1).

**Scansion.** I hand-scanned all 102 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_line`/`SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑× (half-lines: feet 1..k, fewer than six, one ×, with a `why` that starts "Half-line"). Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step with all fixes applied gives an **empty scanner report**: the three COSTLY flags and the three UNRESOLVED lines are all cleared. All 102 lines pass the validator's check, and **all 51 units get `sc`**. The UNRESOLVED lines needed two carrier entries (7.438 and 7.454), because the half-lines 439 and 455 share a unit with the second half of the line before them. The hypermetric 470 is a unit of its own, so it needed no carrier.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 51 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 22 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words. The longest are 401 (134), 385 (132) and 389 (128).
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 176 insertions, 0 deletions, trailing newline kept. The new keys come after 7.358, in line order.
- The build was not run (it writes the published files and the manifest). Its scansion step and the validator's scansion check were replicated instead.

**Speech marks.** Amata, 400–403: “ on *Io matres*, ” after *mecum.* Allecto as Calybe, 421–434: “ on *Turne*, ” after *armis.* Turnus, 436–444: “ on *Classis*, ” after *gerenda.* Allecto, 452–455: “ on *En ego*, ” after *gero.* Each of the three layers has 4 “ and 4 ”. Nothing was changed.

**Severity counts: major 8, medium 9, low 20 (19 in pass 1, 1 in pass 2). Refused findings: 18. Scan-fixes entries added: 16.**

## Changes — pass 1

### Major
1–8. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities were wrong. Each line now has a hand entry.
   - **7.382 *mirata volubile***: the scanner made *mĭ-ră-* short-short and *-tā vō-* long-long. *Mīror* has a long i, and *vŏlūbilis* has a short first syllable. Hand scansion: īn-pū | bēs-quĕ mă | nūs mī | rā-tă vŏ | lū-bĭ-lĕ | bu-xum.
   - **7.388 *Teucris***: the scanner split Teu-. Hand scansion: quō thă-lă | m(um) ē-rĭ-pĭ | āt Teu | crīs tae | dās-quĕ mŏ | rē-tur.
   - **7.400 *Io***: the scanner read *Io* as one syllable with a consonantal I, which made *clāmāt* a spondee. The cry is ĭ-ō, two syllables (so Horace, *io Triumphe*, Odes 4.2.49). Hand scansion: clā-măt Ĭ | ō mā | trēs au | dī-t(e) ŭ-bĭ | quae-quĕ Lă | tī-nae. Both readings fit the meter, so this one is also on the doubtful list.
   - **7.411 *delata noto***: the scanner made *dē-lā-* short-short and *-tă nŏ-* long-long. *Dēlāta* is a nominative with a short final a, and *Notus* has a short o (1.85). Hand scansion: prae-cĭ-pĭ | tī dē | lā-tă nŏ | tō Lŏ-cŭs | Ar-dĕ-ă | quon-dam.
   - **7.419 *Calybe Iunonis***: the scanner made *Cā-lȳ-* long and *-bĕ Iŭ-* short. *Călўbē* is short-short-long (Greek Καλύβη), and *Iūno* has a long u. Hand scansion: fit Că-lў | bē Iū | nō-nĭs ă | nūs tem | plī-quĕ să | cer-dos.
   - **7.443 *Cura tibi divom***: the scanner made *cūrā* a spondee (a nominative cannot have a long final a) and *tī-bĭ dĭ-* long-short-short (*dīvus* has a long i). Hand scansion: Cū-ră tĭ | bī dī | v(om) ef-fĭ-gĭ | ēs et | tem-plă tŭ | ē-ri, with *tibī* long at the beat (the only fit).
   - **7.456 *coniecit***: the scanner read co-ni-e-cit, four syllables. It is *con-iē-cit*, with a consonantal i after the prefix. Hand scansion: Sīc ef | fā-tă fă | cem iŭ-vĕ | nī con | iē-cĭt ĕt | ā-tro.
   - **7.472 *sese Rutuli***: the scanner made *sĕ-sĕ* short-short and *Rū-tū-* long-long (the same error as at 7.286). Hand scansion: cer-tā | tim sē | sē Rŭ-tŭ | l(i) ex-hor | tan-tŭr ĭn | ar-ma.

### Medium
9. **7.410** (COSTLY 2.0), **wrong as flagged**: the scanner read *Danae* as two syllables. It is *Dă-nă-ē*, three syllables (Horace scans *Dănăēn*, Odes 3.16.1). Hand scansion: Ā-crĭ-sĭ | ō-nē | īs Dă-nă | ē fun | das-sĕ cŏ | lō-nis. *Acrisioneis* has six syllables, with Ā- long by position before cr.
10. **7.389** (COSTLY 2.1): I confirmed the scanner's parse by hand and entered it to clear the flag: Eu-hoe | Bac-chĕ frĕ | mēns sō | lum tē | vir-gĭ-nĕ | dig-num.
11. **7.464** (COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag: ex-sul | tant-qu(e) aes | tū lă-tĭ | cēs fŭ-rĭt | in-tŭs ă | quā-ī. *Aquāī* has three syllables.
12. **7.439, a half-line** (UNRESOLVED): in-mĕ-mŏr | est nos | trī.
13. **7.455, a half-line** (UNRESOLVED): bel-lă mă | nū lē | tum-quĕ gĕ | rō.
14. **7.470, a hypermetric line** (UNRESOLVED): sē să-tĭs | am-bō | bus Teu | crīs-quĕ vĕ | nī-rĕ Lă | tī-nīs(que). The *-que* elides into *Haec* (471). *Teucris* has two syllables.
15. **Carriers 7.438 and 7.454**: the scanner's fits are right (checked by hand). Each line shares a unit with the half-line after it, and without the entry the build would give that unit no `sc`.
16. **Notes 439, 455 and 470 talked about "the scanner"**: this is pipeline jargon in a reader's note, and no published Aeneid note uses it. Each sentence now says what the line is: "(two feet and a syllable)"; "three and a half feet"; the hypermetric explanation without "that is why the scanner cannot close it".
17. **Unit 389, who takes up the thyrsus**: `i` read "since it is for him she takes up…", right after "she shrieks", so "she" read as Amata. The subject of *sumere… lustrare… pascere* is the maiden. `i` now reads "since it is for him that the girl takes up the supple thyrsus…", and the note reads "'that she (the maiden) takes up… circles… grows'". "Leafy" (not in *mollis*) is now "supple".

### Low
18. **Note 378, Homer**: "The seed is in Homer, Iliad 14.413" claimed a source. It now reads "Homer has the top in a single line (Iliad 14.413), where Ajax's stone sends Hector spinning 'like a top'". The line number is from memory and is on the list below.
19. **Note 411, Ovid**: "(Met. 14.573–580)" was a line reference from memory that I cannot vouch for. It now reads "Ovid, at the end of his Aeneas story (Metamorphoses 14), tells how a heron…".
20. **Note 423, an inference stated as fact**: "earned in his battles for Latinus" now reads "presumably earned in battles for Latinus" (as 421 and 426 already hedge it).
21. **Note 467, an inference stated as fact**: "the friendship Latinus has just made with the Trojans' envoys is broken by this act" now reads "most naturally the peace Latinus has just made with the Trojans' envoys, which this act breaks".
22. **Note 404, a wrong word-order claim**: "'Talem… reginam'… frames the two lines, with Allecto set inside" was wrong. *Talem* and *reginam* each begin a line, and *Allecto* follows *reginam*. It now reads "the adjective held a line apart from its noun, each word leading its line".
23. **Note 408**: "'Fuscis… alis'… goes round 'tristis dea'" now reads "goes round 'tristis dea tollitur'".
24. **Note 425**: "'Ingratis… periclis'… frames the line" was wrong (*I nunc* comes first). It now reads "goes round 'offer te, inrise'".
25. **Note 432**: "'Caelestum'… of a piece with 'divom'" was loose. *Caelestum* is a third-declension *-um* for *-ium*, and *divom* is the old second-declension *-om*. It now reads "a poetic form".
26. **Note 401, *Siqua***: "it may be a slip, but it is doubtful and harmless" now records the ruling. The capital is Greenough's habit where a colon opens what is said (2.150 *roganti: Quo molem*, 5.28 *contra: Flecte viam*), so it is not a misprint (see R1).
27. **`i` 461, an echo precaution**: "the lust for the sword rages in him, and the accursed madness of war" now reads "a craving for the sword rages in him, and war's wicked madness, and over all of it, anger:".
28–36. **Scansion pointers added to notes**, to go with the fixes and with lines a reader will stumble on:
   - *mīrāta* and *vŏlū-* (381)
   - *Teucris* two syllables (385, 470)
   - *canit* lengthened at the beat before *hymenaeos*, as *profugus hymenaeos* 10.720 (397)
   - *Io* two syllables, ĭ-ō (400)
   - *Danae* three syllables and *notus* with a short o (408)
   - *Calybe* Că-lў-bē (419)
   - *cura* with a short final a, so *tibī* (443)
   - *coniecit* three syllables (456)
   - *sēsē* long-long and *Rŭtŭli* short-short (471)

## Changes — pass 2
- **P2-1 (low)**: in note 470, the new sentence on *Teucris* had landed between the hypermetric explanation and "Virgil allows such lines rarely…". It was moved to the end of the note.

## Scan-fixes entries added (16)
Appended after 7.358 in line order, each with its reason:
- 7.389, 7.410, 7.464 (packet COSTLY flags; 410 was wrong)
- 7.438, 7.454 (carriers), 7.439, 7.455 (half-lines), 7.470 (hypermetric)
- 7.382, 7.388, 7.400, 7.411, 7.419, 7.443, 7.456, 7.472 (no flag, wrong quantities)

Each matches its line's words under `WORD_RE`. The full lines have six feet, five –⏑⏑/–– feet then –×, 14–16 syllables and one ×. The half-lines have 3 and 4 numbered feet and one ×, and their `why` starts "Half-line". In the replicated build all 16 apply, the scanner report is empty, and all 102 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: none in this part (*aestu* 464 and *aethera* 395 are ordinary diphthongs, and right).
- **Greek eu**: *Ceu* (378) and *Euhoe* (389) are right. *Teucris* at 388 and 470 is fixed.
- **Consonantal i after a prefix**: *coniugium* at 423 and 433 is right as `con–iu⏑gi⏑um`. *coniecit* (456) is fixed. *Iunonis* at 419 is fixed for quantity, not division. Also right: *iuris* (402), *iuveni* (420, 446, 456), *iaceres* (427), *iubet* (432, 468), *iam* (414, 466), *maius*/*maiorem* (386; `ma–ius` is a cosmetic division), *Iuno* (438), *iuventae* (473).
- **Hiatus**: none in this part. *audite ubi* (400), *Respice ad* (454) and *ingens rumpit… ossaque et* (458) are ordinary elisions. *Rabidoque haec* (451) and *ad haec* (454, *ad* short before h) are right.
- **Others checked and right**: *gȳro* (379), *ātria* (379), *Ītaliam* (469), *Thȳbridis* (436), *Ĕrīnys* (447), *hydris* (447, long by position at the line's end), *aëni* as ă-ē-nī (463), *exūberat* (465), *ăvīs* (412), *effūgit* perfect (437), *pārēre* (433), *īdem* masculine (393), *dēsĕrŭēre* (394), *ŭlŭlātibus* (395), *sacrum* (391), *flagrantem* (397) and *nigrā* (414), each long by position before a stop and liquid on the only fit.

## Doubtful quantities and readings entered on the only fit
- **7.400 *Io***: both readings fit. The entry takes ĭ-ō (two syllables), the normal quantity of the interjection. The scanner's monosyllable would need a consonantal I.
- **7.443 *tibī*** with a long final i at the beat: the only fit once *cūră* is short.
- **7.398 *canit hymenaeos***: *-nit* is lengthened at the beat before *hy-*. This is the scanner's fit and the only one; no entry (compare 10.720).
- **7.410 *Ā-crisioneis***: the A is long by position before cr, on the only fit.
- **7.391 *sā-crum*, 7.397 *flā-grantem*, 7.414 *nī-grā***: each is long by position before a stop and liquid, on the only fit. These are the scanner's fits; no entry.
- **7.376 *excĭta***: short i, from *excio*, on the only fit.

## Refused findings
- **R1 — 7.401 `Siqua`, the capital after a colon**: kept as printed, **not a misprint**. Greenough capitalises after a mid-speech colon where it opens what is said: 2.150 *roganti: Quo molem*, 5.28 *contra: Flecte viam*, 1.328 *sonat: O, dea certe*, 2.670 *proelia: Numquam*, 5.637 *faces: Hic quaerite*. *Siqua* as one word is also his spelling (7.4, 9.406 and some twenty more *siqua*/*siquis*). The note says so.
- **R2 — other rule-5b misprints**: none. A script found no lowercase after a stop, no space before a mark and no misplaced quote mark in 373–474.
- **R3 — 7.430 *arma*/*arva***: the note's handling is kept. It gives both readings, and both make sense.
- **R4 — 7.384 *feroces*/*ferocis*, 7.382 *inpubes*, 7.439 *inmemor*, 7.443 *divom*, 7.463/464 diaeresis**: orthography only, as the conventions say. The notes already explain Greenough's spellings.
- **R5 — Iliad 2.20–21 (the Dream as Nestor), 6.490–493 (Hector to Andromache), 21.362–365 (the boiling river)**: kept. I recall the Greek of each and the line numbers fit, but they are not checked against a text (see below).
- **R6 — note 383, *cursu… illo***: kept. Taking *illo* as the ablative of comparison and *cursu* as respect is one of the two standard readings, and `l`/`i` follow it.
- **R7 — note 373, *Latinum* as object of *experta***: kept. Taking it with *experta* as well as with *stare* is a defensible reading.
- **R8 — note 392, *omnis* as accusative plural with *matres***: kept. This is the usual construction, and `l` shows it.
- **R9 — `l` 401 "If" with a capital**: kept. `l` follows the print, and `i` runs on in lower case.
- **R10 — note 389, *Euhoe* "without speech marks"**: true of the pinned source. Kept.
- **R11 — `i` 373 omits *ingentibus***: kept. "Monstrous visions" carries the sense, and `l` has "huge".
- **R12 — "The model is…" for Iliad 6 at 444 and Iliad 21 at 462–466**: kept. These are the standard Homeric parallels, and the wording claims imitation, not quotation.
- **R13 — note 474, *atavus* "great-great-great-grandfather"**: correct (*avus, proavus, abavus, atavus*). Kept.
- **R14 — note 419, Calybe's temple "at Ardea presumably"**: already framed as inference. Kept.
- **R15 — cosmetic syllable divisions** (*ma–ius* 386, *con–iu⏑gi⏑um* 423/433, *E⏑4ri–nys* 447): the quantities are right, so there are no entries (as aeneid-052 R18).
- **R16 — note 439, "left incomplete when he died with the Aeneid unrevised"**: kept, in line with the published notes (aeneid-006).
- **R17 — `i` echoes elsewhere**: nothing further found. "Rumour flies", "War and peace will be the concern of men" and "I carry war and death" are plain renderings, not a translator's turns.
- **R18 — `title`, `titleEn`, `part`, `about`**: our own, and the summary is accurate. Unchanged.

## For the owner (QUESTIONS.md)
- **Misprints**: none decided in this part. 7.401 `Siqua` (a capital after a colon) is recorded as Greenough's habit, not a misprint (R1). If the owner wants a ruling on capitals after mid-speech colons generally, the list in R1 is the evidence.
- **Doubtful quantities**: 7.400 *Io* scanned ĭ-ō (the entry's choice of two fits); 7.443 *tibī*; 7.398 *canit* lengthened at the beat; 7.410 *Ā-* by position. None was checked against an edition.
- **`make_units.py` is stale**: `drafts/aeneid-053/make_units.py` still holds the drafter's strings; re-running it would discard this review.
- **Unchecked attributions, from memory**: Iliad 14.413 (Hector spun "like a top"); Iliad 2.20–21; Iliad 6.490–493; Iliad 21.362–365; Ovid's heron at Ardea (Metamorphoses 14, line numbers cut); Horace Odes 3.16.1 *Danaen* and Odes 4.2.49 *io Triumphe* (cited in scan-fixes reasons); the Danae–Ardea foundation legend; *olli* "after Ennius"; *lymphatus* from *lymphae*/nymphs. None was checked against a text in this run.
