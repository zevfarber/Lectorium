# Review — aeneid-076 (Aeneid X.362–438), adversarial reviewer

**Severity counts: major 10, medium 0, low 22 (20 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 11. Scan-fixes entries added: 12 (8 wrong full lines, the misprint line 371, 3 carriers).**

## How the review was done

**Pass 1** covered all 42 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list (all 42 are right, including Hisbo/ille at 384–385, which is not an elision because the line ends between them), every "framing" claim, every cross-reference and every attribution made from memory. I also checked:
- the speech marks (369–378, 421–423): “ opens unit 369a and unit 421, ” closes unit 377 and unit 423, in `t`, `l` and `i` alike
- the rule-5b handling of 371 `Opemque`
- the Latin Library variants (363, 366, 371, 378, 390, 401, 412)
- `about`, `title`, `part` and `titleEn`

I read every `i` for echoes of the well-known English versions, especially the fire simile (405–409) and 435–438, and recast those three.

Sources: the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

**Cross-references checked in the pinned source:** VII.649–650 (Lausus second in beauty only to Turnus), VII.723 (Halaesus *Agamemnonius, Troiani nominis hostis*, Low 13), VIII.514–519 (Pallas and the Arcadian horsemen), X.170 (*torvus Abas*), X.352 (Halaesus enters), X.460–473 (the prayer to Hercules, refused), X.495–500 (Turnus takes the belt), and X.253 and 5.144 (the quantities of *biiugi*).

**Pass 2** re-read every edited field in full and re-checked the speech marks (two openings and two closings in each layer), line counts (`l` has the same number of lines as `t` in every unit, and no `i` has a line break) and note lengths (40–120 words). It made the changes P2-1 and P2-2.

**Scansion.** I hand-scanned all 77 lines and compared them syllable by syllable with the scanner, run in-process the way the build calls it. The helper is `drafts/aeneid-076/scan_check.py` (075's, with the part id changed).
- **Packet flags:**
  - 371 (UNRESOLVED) is the misprint; it gets an entry scanned as *spemque*.
  - 402 (COSTLY 3.0) is **right**: quam mĕ-dĭ | us Rhoē | teus in | ter-cĭ-pĭt | op-tĭ-mĕ | Teu-thra. Both *Rhoe-teus* and *Teu-thra* have eu as one syllable. The cost is only the Greek eu.
  - 424 (COSTLY 2.0) is **right**: Au-dĭ-ĭt | il-lă dĕ | us dum | tex-ĭt Ĭ | mā-ŏ-n(a) Hă | lae-sus.
- **Eight full lines are wrong with no packet flag:**
  - wrong quantities with the right count: 366 (*nātūra*, *lŏci*), 376 (*nōbīs*, *ănĭmae*), 391 (*Lārīdē*, short *-que* and *si-*), 413 (*Lādōna*, *Phĕrēta*)
  - consonantal i after a prefix: *biiugis* 399 (run together into one syllable), *traicit* 400 (read as two syllables), *iniecere* 419 (read with a vowel i)
  - *Grāīs* 430 (made short-short, which forced *imperdita* to be long-long)
- **Carriers.** 369, 370 and 372 are entered because they share unit 369b–372a with 371. Without them that unit would get no `sc`.
- **Right as the scanner reads them:**
  - *Teucri* 430 and *Rhoeteus* 402 (eu one syllable), *Rhoetea* 399 and *Rhoeti* 388
  - *semianimes* 396 and *semianimis* 404 (four syllables, consonantal i)
  - *Laride* 395 (Lā-rī-dē; this is what fixes 391)
  - *insuetos* 364 (four syllables), *suasit* 367 (two), *huic* 380 (one), *deest* 378 (one, synizesis), *Troiamne* 378, *maiore* 438
  - *obice* 377 (long first syllable), *canens* 417 and *canentia* 418 (short and long a), *Palla* 411
  - There is no initial *Ae-* in this part, and no hiatus.

Every entry was checked by `drafts/aeneid-076/add_scan_fixes.py` (075's, with the part id and entries changed; dry run, then `--write`):
- against the build's word-match rule
- against the validator's metre rule
- against the syllable count stated in its own `why`

A replica of the build's scansion step, reading `scan-fixes.json`, gives these results:
- all 12 entries apply
- **all 42 units get `sc`**
- no unit's `sc` is out of line with its words
- no line fails the metre check
- the only reports left are the correct COSTLY fits at 402 and 424

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by `review_edits.py` (pass 1: 22 field edits) and `review_edits_pass2.py` (pass 2: 3 field edits). Each old string was asserted to occur exactly once in its field. The file was written with `aeneid_lib.jdump`; the drafter's file round-tripped byte-identically before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` were checked by script against a copy taken before any edit, and are unchanged in all 42 units. `title`, `titleEn`, `part` and `about` are unchanged.
- **Units changed:** 0, 3, 5, 6, 8, 9, 14, 15, 16, 19, 22, 24, 25, 27, 30, 32, 35, 39, 40.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so build from `units.json` as it stands.
- **`scan-fixes.json`.** The change only appends (135 insertions, 0 deletions), with new keys after 10.343 in line order.
- **Build and validator not run.**

## Changes — pass 1

### Major
- **M1. Note and `l` 424b–425, *dum texit*.** The note called *texit* the "present of 'tego'". It is the perfect (the present is *tegit*). The note now reads "'while he shielded', perfect of 'tego' (the present is 'tegit'): 'dum' normally takes the present, and the perfect here is unusual". `l` "while he shields" is now "while he shielded".
- **M2. 10.366** (cost 0.0, unflagged). The scanner had *na-tu* short-short and *lo-* long. Right: ās-pĕ-ră | quīs nā | tū-ră lŏ | cī dī | mit-tĕ-rĕ | quan-do (15).
- **M3. 10.371**, the misprint (UNRESOLVED). It is scanned as *spemque*, marked on the printed word: spem-quĕ mĕ | ām pă-trĭ | ae quae | nunc sŭ-bĭt | ae-mŭ-lă | lau-di (16). **Carriers 10.369, 10.370 and 10.372** are entered; the scanner is right on all three.
- **M4. 10.376** (cost 0.0, unflagged). The scanner had *no-bis* short-short and *a-ni-* long-long. Right: mor-tā | lēs tŏ-tĭ | dem nō | bīs ă-nĭ | mae-quĕ mă | nus-que (15).
- **M5. 10.391** (COSTLY 0.6, unflagged). The scanner had *Lăridĕ*, which forced it to lengthen both *-que* and the *si-* of *simillima*. Right, with *Lārīdē* as at 395: Dau-cĭ-ă | Lā-rī | dē Thym | ber-quĕ sĭ | mil-lĭ-mă | prō-les (15).
- **M6. 10.399** *biiugis*. The scanner ran *bi-iu* into one syllable (14). Right, as at 5.144 and 10.253: Tum Pal | las bĭ-jŭ | gīs fŭ-gĭ | en-tem | Rhoē-tĕ-ă | prae-ter (15).
- **M7. 10.400** *traicit*. The scanner read two syllables, with *-cit* long (15). Right, as at 9.634: trā-ĭ-cĭt | Hōc spă-tĭ | um tan | tum-quĕ mŏ | rae fŭ-ĭt | Ī-lo (16).
- **M8. 10.413** (cost 0.0, unflagged). The scanner had *La-do* short-short, *-na* long and *Phe-* long. Right: Hīc mac | tāt Lā | dō-nă Phĕ | rē-tă-quĕ | Dē-mŏ-dŏ | cum-que (15).
- **M9. 10.419** *iniecere*. The scanner read the i as a vowel (15). Right, as *iniecit* at 2.408: in-jē | cē-rĕ mă | num Par | cae tē | lis-quĕ să | crā-runt (14).
- **M10. 10.430** *Grais*. The scanner had *Gra-is* short-short and *-di-ta* long-long. Right: et vōs | Ō Grā | īs im | per-dĭ-tă | cor-pŏ-ră | Teu-cri (14).

### Low
- **L1. `l` 362–363.** "the other side" is now "another side" (*parte ex alia*, as `i` has it).
- **L2. Note 369b–372a.** "'pedibus' is dative with 'fido'" is now "dative (or ablative)". *fido* takes either.
- **L3. `i` 373–374.** "our proud homeland" lost *alta*, which the note explains as Pallanteum on its hill. It now reads "that is the road by which our homeland, high on its hill, demands you back, you and Pallas your leader".
- **L4. Note 375–376.** *urget* is at 373, two lines before *urgemur*, not "in the line before". It now reads "two lines before (373)".
- **L5. `l` 379.** "into the dense bursts the enemy" read as a noun phrase. It now reads "into the packed enemy bursts".
- **L6. Note 380–381a.** With the passive participle *adductus*, *fatis iniquis* is an "ablative of means", not "of cause".
- **L7. `l` 390.** In "on the Rutulian fell fields", *fell* read as an adjective. It now reads "fell on the Rutulian fields".
- **L8. Note 390–392.** Added "all three syllables long here and at 395" to *Laride*, to match M5.
- **L9. Note 393.** *dura… discrimina* does not frame the line, because *at nunc* stands before it and *Pallas* after. It now reads "enclosing 'dedit vobis'".
- **L10. Note 394.** "Evander's own sword in his son's hand" went beyond the text. It now reads "the sword of Evander's house" (wording finished in P2-1).
- **L11. Note 399–400a.** Added "and 'bi-' short" to *biiugis*, to match M6.
- **L12. Note 399–400a.** Dropped "= 'transicit'", which is not a form I can vouch for. Added "three syllables, tra-i-cit", to match M7.
- **L13. Note 411b–412, Halaesus.** "a follower of Agamemnon's line who settled in Italy" went beyond VII.723. This is the same correction 075 made (its L12). It now reads "'Agamemnonius', of Agamemnon's house or following, an enemy of the Trojan name (VII.723)".
- **L14. Note 413–416.** Added the quantities of *Ladona* and *Phereta*, to match M8.
- **L15. `i` 405–409, the fire simile.** Recast from the Latin to move away from stock prose wording ("the winds he hoped for", "the gaps between catch", "looking down like a victor on the exulting flames"). It now reads: "And as in summer, once the winds he has waited for spring up, a shepherd sets fire to the woods at scattered points; all at once the spaces between are caught, and Vulcan's battle-line spreads out in one bristling front across the broad plains, while he sits, a victor, gazing down on the flames as they exult:". This also restores *acies Volcania*.
- **L16. `i` 423.** The old wording dropped *Haec*. It now reads "Your oak shall have these arms and this man's spoils."
- **L17. Note 429–430.** The *Etrusci* are not "Tarchon's allies". They are "Tarchon's Etruscans, Aeneas's allies".
- **L18. Note 429–430.** Added "(two long syllables, Gra-is)" to *Grais*, to match M10.
- **L19. `i` 435–436a.** Recast away from familiar wording ("had denied them any return to their homeland"). It now reads "both of them strikingly fair, but Fortune had refused them any homecoming."
- **L20. `i` 436b–437.** "did not let the two of them meet each other in combat" is now "would not allow the two to clash with one another".

## Changes — pass 2
- **P2-1. Note 394.** The pass-1 wording stacked two appositions. It now reads "the sword of Evander's house in his son's hand; the adjective from the name is used as with 'Daucia proles' just before."
- **P2-2. Note 418–420a.** The play *canens* / *canentia* rests on two verbs with different quantities, as the `sc` shows. The note now says "from 'caneo' (long 'a', as in 'canus')" and "'canens', 'singing' (short 'a', from 'cano')". This is two field edits.

## Refused or upheld without change
1. **Rule 5b at 371, `Opemque` → `spemque`. Upheld.**
   - **Why it is a misprint.** The reading is unmetrical. *ops* has a short o (ŏpis), so *ŏpēmquĕ mĕām* cannot open a hexameter, and the scanner finds no fit. *spēmque* gives a normal line. *Opem meam* is grammatical ("my aid"), but the metre allows only one reading, which meets rule 5b's test.
   - **The capital O.** It is a supporting sign. Whether the slip is Greenough's compositor's or the Perseus transcription's, the reader sees the same error.
   - **How it is handled.** It follows the established Aeneid practice (QUESTIONS #19, #23; scan-fixes 5.181, 7.254, 10.20): `t` as printed, `l`/`i` corrected ("my hope"), and the note opens with the required sentence. The scan-fix scans *spemque* on the printed word.
2. **402 and 424, flagged COSTLY.** The scanner is right, and no entry was added (see Scansion above).
3. **Note 431, "ablative of manner"** for *ducibusque et viribus aequis*. Kept. It could be called an ablative absolute, but "manner" is defensible (A&G's *aequo animo* type) and the gloss is right either way.
4. **Note 384–385, connecting relative *Quem* with *non super occupat*.** Upheld; *super* as an adverb ("standing over the body") is the usual reading.
5. **Note 377–378, *Troiam* as probably the Trojan camp.** Upheld, as hedged.
6. **Note 426–427a, *perterrita* with *agmina*, predicative with *sinit*.** Upheld.
7. **Note 395–396, *semianimes* four syllables, and the Ennius fragment** (*semianimesque micant oculi*, on a severed head, quoted by Macrobius). Upheld.
8. **Attributions from memory, kept as written.** I am confident of each:
   - Iliad 15.733–741 (Ajax at the ships)
   - Iliad 21.568–570 (Agenor)
   - Iliad 11.155–157 and 20.490–492 (fire)
   - Iliad 2.831–834 and 11.329–332 (Merops)
   - Servius's Anchemolus story, unnamed in the note
   - *manus iniectio*
9. **Variant notes at 363, 366, 378, 390, 401 and 412.** Upheld; each is brief and correct.
10. **Misprints.** No others found. The speech marks sit correctly, and *vellit* 381 is the same word as the Latin Library's *uellit*.
11. **Advisory: none (upheld).** This is ordinary battle killing. Anchemolus's offence is a passing mention of consensual incest, not sexual violence.

## Scan-fixes entries added (12)
| key | reason | syllables |
|---|---|---|
| 10.366 | *nātūra*, *lŏci* (quantities) | 15 |
| 10.369 | Carrier for 371 (scanner right) | 15 |
| 10.370 | Carrier for 371 (scanner right) | 14 |
| 10.371 | Misprint *Opemque*, scanned as *spemque* (UNRESOLVED) | 16 |
| 10.372 | Carrier for 371 (scanner right) | 15 |
| 10.376 | *nōbīs*, *ănĭmae* (quantities) | 15 |
| 10.391 | *Lārīdē* (quantities) | 15 |
| 10.399 | *biiugis*, consonantal i, *bi-* short | 15 |
| 10.400 | *traicit*, three syllables | 16 |
| 10.413 | *Lādōna*, *Phĕrēta* (quantities) | 15 |
| 10.419 | *iniecere*, consonantal i after the prefix | 14 |
| 10.430 | *Grāīs* (quantities) | 14 |

## For the owner (QUESTIONS.md)
- **10.371 `Opemque` → `spemque` (rule 5b).** Rule 5b asks for a QUESTIONS.md entry where the work has no emendation list. The publishing run should add one: "aeneid-076, 10.371: print `Opemque`, read `spemque` (metre; Latin Library agrees); `t` as printed, `l`/`i`/note corrected, scan-fix scans `spemque`." The reviewer may not touch QUESTIONS.md.
- **10.413 *Lādōna*.** The long first syllable rests on memory of Ovid's *Lādōnis* (Met. I.702). The long *-dō-* (Greek ω) and the short *Phĕ-* are certain. The scanner's fit is wrong on *-dō-* and *Phĕ-* whichever way the first syllable goes.
- **Unchecked attributions from memory.** These are kept and believed right:
  - Iliad 15.733–741, 21.568–570, 11.155–157, 20.490–492, 2.831–834, 11.329–332
  - the Ennius fragment
  - Servius on Anchemolus
- **Advisory:** none taken.
