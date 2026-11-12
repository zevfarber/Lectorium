# Review — aeneid-052 (Aeneid VII.286–372), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 38 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the speech marks, every rule-5b misprint decision (7.294, 296, 300, 360, 364 spacing; 7.320 no mark after *iugalis*; 7.323 capital *Horrenda*; 7.340 *inventus*), the Latin Library variants that matter (7.307 *Lapithis*/*Lapithas*, 7.358 *nata*/*natae*, 7.363 *An*/*at*), and every `i` for remembered English. I paid most attention to 7.312 *flectere si nequeo superos, Acheronta movebo* and to 317–319. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched. Every in-poem cross-reference was checked against the pinned source:
- 1.2 (*fato profugus*), 1.9, 1.24 (*caris… Argis*), 1.25, 1.28 (*genus invisum*), 1.37 (*haec secum*), 1.46–47 (quoted word for word), 1.50–52 (Aeolia), 1.70 (*disiice*), 1.111 (*Syrtis*)
- 2.312 (*Sigea igni freta*), 3.420–432 (Helenus on Scylla and Charybdis), 3.558–560, 3.699 (Pachynus), 4.166 (*pronuba Iuno*), 4.305, 4.366 (*perfide*), 5.606 (Iris sent), 5.781 (*nec exsaturabile pectus*)
- 6.571 (Tisiphone), 6.830–831 (*socer*, *gener*), 7.47–48, 7.52, 7.56–58, 7.96–98 (*externi venient generi*, 98), 7.266, 7.409–411 (Danae, *Acrisioneis… colonis*, Ardea)
- 10.76 (Venilia), 10.704–705 (*face praegnans / Cisseis*), 12.845–847 (the Dirae, Megaera, Night their mother)

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 87 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step with all fixes applied gives an empty scanner report (both COSTLY flags cleared). All 87 lines pass the validator's check, and all 38 units get `sc`. There were no UNRESOLVED lines, so no carrier entries were needed.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 38 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words. The longest are units 4 and 32 at 137 words each, then unit 24 at 136.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 152 insertions, 0 deletions, trailing newline kept.
- The build was not run. `build_aeneid.py` has no dry-run option: `--help` is read as a part id and refused at once with "no such part", before anything is read or written.

**Speech marks.** Juno's soliloquy, 293–322: “ on the first unit (*Heu*), ” after *taedae.* Juno to Allecto, 331–340: “ on *Hunc*, ” after *inventus.* Amata, 359–372: “ on *Exsulibusne*, ” after *Mycenae.* Each of the three layers has 3 “ and 3 ”. Nothing was changed.

**Severity counts: major 11, medium 5, low 23 (21 in pass 1, 2 in pass 2). Refused findings: 18. Scan-fixes entries added: 13.**

## Changes — pass 1

### Major
1–11. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities were wrong. Each line now has a hand entry.
   - **7.286 *sese referebat***: the scanner made *sĕsĕ* short-short and *rē-fē-* long-long. The syllable count is the same and the quantities are wrong. Hand scansion: Ec-c(e) au | t(em) Ī-nă-chĭ | īs sē | sē rĕ-fĕ | rē-băt ăb | Ar-gis.
   - **7.287 *coniunx***: the scanner read co-ni-unx as three syllables. Hand scansion: sae-vă Iŏ | vīs con | iunx au | rās-qu(e) in | vec-tă tĕ | nē-bat.
   - **7.288 *Aenean***: the scanner split Ae-. Hand scansion: et lae | t(um) Aē-nē | ān clas | sem-qu(e) ex | ae-thĕ-rĕ | lon-ge.
   - **7.294 *Phrygum… Sigeis***: the scanner made *Phry-* long and *Si-ge-* short. *Phrўges* has a short y, and *Sīgēus* is long throughout (2.312 scans Ū-că-lĕ | gōn Sī | gē(a) īg…). Hand scansion: fā-tă Phrў | gum Num | Sī-gē | īs oc | cum-bĕ-rĕ | cam-pis.
   - **7.301 *Teucros***: the scanner split Teu-. Hand scansion: Ab-sump | t(ae) in Teu | crōs vī | rēs cae | lī-quĕ mă | rīs-que.
   - **7.308 *coniunx***: the scanner read three syllables. Hand scansion: Ast ĕ-gŏ | mag-nă Iŏ | vīs con | iunx nīl | lin-quĕ-r(e) ĭ | nau-sum.
   - **7.310 *Aenea***: the scanner split Ae- and made *-ne-* short. Hand scansion: vin-cŏr ăb | Aē-nē | ā quod | sī mĕ-ă | nū-mĭ-nă | nōn sunt.
   - **7.317 *coeant***: the scanner read *coe-* as a diphthong (two syllables). *Coeo* is *co-* + *eo*. Hand scansion: Hāc gĕ-nĕr | āt-quĕ sŏ | cēr cŏ-ĕ | ānt mer | cē-dĕ sŭ | ō-rum. Both readings fit the meter, so this one is also on the doubtful list.
   - **7.319 *te pronuba***: the scanner made *tē* and *prō-* short (nēt tĕ prŏ | nū-bā). *Prōnuba* is long as at 4.166. Hand scansion: ēt Bel | lō-nă mă | nēt tē | prō-nŭ-bă | Nēc fă-cĕ | tan-tum.
   - **7.344 *Teucrum***: the scanner split Teu-. Hand scansion: quam sŭ-pĕr | ad-ven | tū Teu | crum Tur | nī-qu(e) hў-mĕ | nae-is.
   - **7.358 *nata lacrimans***: the scanner made *nătă* short-short and *lā-crī-* long-long. *Nātā* is an ablative, and *natus* has a long a. Hand scansion: mul-tă sŭ | pēr nā | tā lă-crĭ | māns Phrў-gĭ | īs-qu(e) hў-mĕ | nae-is.

### Medium
12. **7.320** (COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag: Cis-sē | īs prae | gnāns īg | nīs ē | nī-xă iŭ | gā-lis. *Cisseis* has three syllables, and *iugalis* begins with a consonantal i, so *enixa* is not elided.
13. **7.340** (COSTLY 2.0): the scanner scanned the misprint *inventus*. It elided *rapiatque* into it, which gave a spondaic fifth foot. The line is now scanned as *iuventus*, with the i consonantal and no elision, on the printed word (`in⏑6ven–tus×`, as the 5.181 and 7.254 entries do): ar-mă vĕ | līt pos | cāt-quĕ sĭ | mūl ră-pĭ | āt-quĕ iŭ | ven-tus.
14. **Unit 290, a missed misprint (rule 5b)**: *moliri* is lowercase after the full stop that ends 289. The aeneid-049 reviewer had already listed 7.290 among the lowercase-after-a-stop cases (QUESTIONS #43). The note now opens with the print's reading, as 7.259, 7.267 and 7.274 did in aeneid-051, and `l` begins "Building".
15. **`l` 319–320**: `l` read "Nor with a torch only / Cisseus's daughter…", which attaches "only" to the torch. The note (rightly) puts *tantum* with *Cisseis*, and so does `i`. `l` now reads "Nor with a torch did only / Cisseus's daughter, pregnant, give birth to marriage fires;".
16. **`i` 318–319**: "Bellona waits to attend you as bride" could be read as Bellona being the bride. It was also close to the familiar "awaits thee as bridesmaid" turn. It now reads "Your dowry, girl, will be the blood of Trojans and Rutulians, and it is Bellona who will stand beside you at your wedding."

### Low
17. **Note 319–322, misprint wording**: "a misprint for 'iugalis;'" claimed more than can be known, since the print may simply have no mark there. It now reads "the sense needs a stop before 'quin', so it is read here as 'iugalis;' (probably a dropped mark)". It still opens with the print's reading.
18. **Note 294–296, Ennius**: "as Macrobius reports the lines" now reads "Macrobius cites as the model a line of Ennius's Annales…". The attribution is unverified and is on the list below.
19. **Note 313–314**: "'regnis… Latinis'… frames the clause" was wrong: *Non dabitur* stands outside the phrase. It now reads "goes round 'esto, prohibere'".
20. **Note 331–334**: "(12.846)" for Night as the Furies' mother now reads "(12.845–847)". *Nox… tulit* runs over 846–847.
21. **Note 338–340**: "'Disice' is Greenough's spelling of 'disiice'" was wrong: Greenough prints *disiice* at 1.70 and *disice* here. It now reads "'Disice' (Greenough prints 'disiice' at 1.70) is the imperative of 'disicio'…; its first syllable is long, 'dis-yi-ce'."
22. **Note 338–340, *concute***: "as one shakes out a fold of a garment for what it holds" was an image with no source. It is softened to "'shake', 'rouse', as if to shake out all it holds."
23. **Note 371–372, a wrong label**: "has the present subjunctive of a 'should… would' condition". The main clause is an indicative (*sunt* understood), so the condition is mixed. It now reads "puts the condition as an imagined case (present subjunctive), though the main statement is plain fact."
24. **`i` 317, an echo precaution**: "Let son-in-law and father-in-law join hands, then, at this price, paid by their own people" now reads "Then let the son-in-law and his bride's father come together on these terms, and let their own people pay for it:".
25–37. **Scansion pointers added to notes**, to go with the fixes and with lines a reader will stumble on:
   - *Aenean* three syllables and *coniunx* two (286–289; one sentence was cut to make room: "Virgil does not explain how she sees Latium from so far")
   - *Sigeis* Sī-gē-īs (294–296)
   - *Teucros* two syllables (301)
   - *alveo* two syllables, by synizesis (303–304)
   - *Aenea* Aē-nē-ā and *coniunx* two syllables (308–310)
   - *coeant* three syllables (317)
   - *te* long and *prō-* long (318–319)
   - *obsidere* from *obsīdo* (331–334; this is what makes the line scan, with Ĭtalos)
   - the line scanned with *iuventus* (338–340)
   - *Teucrum* two syllables (341–345)
   - *conicit* with a long first syllable (346–348)
   - *nata* with a long final a (354–358)
   - the first a of *Lavinia* short here, long at 314 (359–360)

## Changes — pass 2
- **P2-1 (low)**: note 294–296 cited 2.312 twice, once for the place and once for the scansion. The second citation was cut, so it now reads "'Sigeis' scans Sī-gē-īs."
- **P2-2 (low)**: note 354–358 had "'super' with the ablative (long final a)", which reads as if *super* had the long a. It now reads "'super' with the ablative 'nata' (long final a)".

## Scan-fixes entries added (13)
Appended at the end of `scan-fixes.json`, each with its reason:
- 7.320, 7.340 (packet COSTLY flags; 340 is scanned on the corrected reading)
- 7.286, 7.287, 7.288, 7.294, 7.301, 7.308, 7.310, 7.317, 7.319, 7.344, 7.358 (no flag, wrong quantities)

Each matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 13–16 syllables and one ×. In the replicated build all 13 apply, the scanner report is empty, and all 87 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: *Aeneadae* (334) is right, as Aē-nĕ-ă-dae. *Aenean* (288) and *Aenea* (310) are fixed.
- **Greek eu**: *Teucris* (359) is right, and so is *Heu* (293). *Teucros* (301) and *Teucrum* (344) are fixed.
- **Consonantal i after a prefix**: *coniunx* at 314 is right in quantity (`co–niunx`, so the division is cosmetic). *disice* (339) is right as `di–si⏑ce⏑`: the first syllable is long and the division cosmetic. *conicit* (347) is right as `co–ni⏑cit⏑`. *coniunx* at 287 and 308 is fixed. Also right: *Iovis* (287, 308), *Troia*/*Troiano*/*Troianas* (296, 318, 364), *Iuno* (330), *iugalis* (320), *iussa* (368), *iam* (290), *iacent* (298), *Huic* (346), *cui* (325).
- **Synizesis**: *alveo* (303) is two syllables, which is right; the note now says so. *coeant* (317) is fixed (no synizesis).
- **Hiatus**: none in this part. Every vowel meeting is an ordinary elision, including over h (*Iuno his* 330, *Turnique hymenaeis* 344, *Phrygiisque hymenaeis* 358, *Ledaeamque Helenam* 364). *usquam est* (311) and *locuta est* (357) are prodelision.
- **Others checked and right**: *Ī-nă-chus* (372, line-initial, so Ī is certain), *Pă-chȳ-no* (289), *prō-spexit* (289), *pŏ-tŭ-ē-re* (295), *in-vē-nē-re* (297), *prŏ-fŭ-gis* (300), *prō-fuit* (303), *Thȳ-bri-dis* (303), *Că-lў-dō-na* (306, 307), *prŏ-hĭ-bē-re* (313), *rĕ-cĭ-dī-va* (322, as 10.58), *Al-lēc-tō* (324), *tĕ-nĕ-bris* with -ne- short (325), *Plū-tōn*, *ō-dē-re* (327), *prŏ-prĭ-um* (331), *ŭ-nă-nĭ-mos* (335), *fū-nĕ-rĕ-as* (337), *fē-cun-dum* (338), *Gor-gŏ-nĕ-is* (341), *ob-sē-dit* (343), *lē-vi-a* (349), *lū-bri-cus* (353), *lŭ-ēs* (354), *Lē-dae-am* (364), *Lă-ce-dae-mo-na* (363), *con-san-guĭ-nĕ-o* (366), *rĕ-or* (370), *My-cē-nae* (372). The syllable divisions *su–blap* (354), *exs–cin* (316), *E–xin* (341) and *praeg–nans* (320) are cosmetic: the quantities are right, so there is no entry (as *sublimes* in aeneid-051).

## Doubtful quantities and readings entered on the only fit
- **7.359 *Lăvinia*** with a short first a: forced by the meter (*ducenda* ends in a short syllable). Elsewhere it is *Lā-* (7.314, 7.72, 6.764). This is the scanner's fit and the only one; no entry.
- **7.333 *conubiis***: the scanner reads *cōnŭbĭīs* (short u). A three-syllable *cōnūbyīs* also fits. This is the same handbook question as 7.253 in aeneid-051. The scanner's fit is kept, with no entry.
- **7.334 *Ĭtalos*** with a short I, together with *obsīdere* (from *obsīdo*): the only fit (as the short *Ĭtalus* at 7.178). No entry.
- **7.317 *coeant***: both fit. The entry takes *cŏ-ĕ-ant* (three syllables), the normal reading of *coeo*.
- **7.294 *fata Phrygum***: *-ta* is not lengthened before *Phr-*, which is the only fit once *Sī-gē-* is long.
- **7.340**: the scansion follows the corrected *iuventus* on the printed *inventus*. If the owner prefers `sc` to scan the print, drop the entry (the scanner's own fit has a spondaic fifth foot with *que* elided into *in-*).
- **Long by position before stop and liquid, on the only fit**: *ā-* of *acri* (291), *Ā-* of *Acrisius* (372).

## Refused findings
- **R1 — spacing misprints 7.294 `Phrygum !`, 7.296 `viros ?`, 7.300 `ponto !`, 7.360 `tuique ?`, 7.364 `urbes ?`**: kept as rule-5b notes, following 7.116 and 7.197. Only the spacing is affected, and each note opens with the print's reading.
- **R2 — 7.323 `Horrenda`**: kept as a misprint. A capital in mid-sentence after *terras* has no sense, and *horrenda* as an epithet is plain.
- **R3 — 7.340 `inventus`**: kept as a misprint for *iuventus*. *Inventus* gives no sense, the Latin Library has *iuuentus*, and only *iuventus* gives the normal dactylic fifth foot.
- **R4 — 7.307 *Lapithis***: the note's handling is kept: Greenough's dative is construed loosely, and the *Lapithas* reading is given. The sense does not change.
- **R5 — Servius on Mars and Pirithous's wedding** (unit 304–307): kept as attributed. I believe it is right, but I could not check it (see below).
- **R6 — Servius on Venilia as Amata's sister** (unit 365–366): kept as attributed and worded as Servius's claim, not as fact. Unchecked.
- **R7 — Freud's motto** (unit 312): kept. *Flectere si nequeo superos, Acheronta movebo* is the epigraph of *Die Traumdeutung* (dated 1900).
- **R8 — `i` 312 and `l` 312, for echoes**: no change. "If I can bring no god above round to my side, I shall rouse the world of the dead" avoids the familiar "If I cannot bend heaven, I will move hell" turns, and `l`'s "to sway… Acheron I shall set moving" is the crib.
- **R9 — other `i` for echoes**: nothing further found. "Haec ubi dicta dedit" as "When she had said this", and "a thousand names, a thousand ways of doing harm", are plain renderings.
- **R10 — "girl" for *virgo* in `i` 318**: kept. Juno speaks with contempt, and "girl" is not modern-casual.
- **R11 — note 351–353, "'ingens' agrees with it [coluber]"**: kept. *Ingens* could also go with *aurum*, but the note's reading is the natural one and is the one `l` and `i` follow.
- **R12 — "(in her chariot)" for *invecta*** (unit 286): kept as a parenthetical gloss of what "borne along" implies.
- **R13 — `i` 311 "will not shrink" for the potential *dubitem haud***: kept. `l` has "would not hesitate", and the note explains the mood.
- **R14 — 7.363 *An*/*at* and 7.358 *nata*/*natae***: the notes' handling is kept; the sense barely changes.
- **R15 — Hecuba as "Cisseis"**: kept. This is Virgil's (Euripidean) genealogy, and the note does not contrast it with Homer's Dymas.
- **R16 — `title`, `titleEn`, `part`, `about`**: our own, and the summary is accurate. Unchanged.
- **R17 — `l` 290 "having deserted their ships"**: kept; it shows the perfect infinitive.
- **R18 — cosmetic syllable divisions** (*co–niunx* 314, *su–blap* 354, *exs–cin* 316, *E–xin* 341): no entries, as in aeneid-051 R20.

## For the owner (QUESTIONS.md)
- **Misprints to record**: 7.290 `moliri` → `Moliri` (lowercase after a stop; the ruling asked for in item 43 is still open); 7.294 `Phrygum !`, 7.296 `viros ?`, 7.300 `ponto !`, 7.360 `tuique ?`, 7.364 `urbes ?` (space before the mark); 7.320 no mark after `iugalis` (read as `iugalis;`, probably a dropped mark); 7.323 `Horrenda` → `horrenda`; 7.340 `inventus` → `iuventus`. In each case `t` is as printed and `l`/`i` give the reading.
- **Scansion on the corrected reading**: the 7.340 entry scans *iuventus* on the printed word, following 5.181 and 7.254.
- **Doubtful quantities on the only fit**: 7.359 *Lăvinia*; 7.333 *cōnŭbiis* (the scanner's choice of two fits); 7.334 *Ĭtalos* with *obsīdere*; 7.317 *coeant* trisyllabic (the entry's choice of two fits). None was checked against an edition.
- **`make_units.py` is stale**: `drafts/aeneid-052/make_units.py` still holds the drafter's strings; re-running it would discard this review.
- **Unchecked attributions, from memory**: Macrobius citing Ennius's Annales *nec cum capta capi nec cum combusta cremari* (294–296); Servius on Mars, left out of Pirithous's wedding, stirring the Lapith–Centaur fight (304–307); Servius making Venilia Amata's sister (365–366); Oeneus neglecting Diana at Calydon (the Iliad 9 story; not cited by line); Hecuba's dream of the firebrand (319–322; the note cites only 10.704–705, which has *face praegnans* but not the dream); Freud's epigraph (312); Allecto's name as "the unresting" (324–326). None was checked against a text in this run.
