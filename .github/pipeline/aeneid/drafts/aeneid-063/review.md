# Review — aeneid-063 (Aeneid VIII.608–731), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 50 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every cross-reference and every historical or mythological claim. I also checked the drafter's rule-5b calls (8.629 `ab Ascanio. pugnataque`, 8.691 `alta`, 8.694 `stuppea`, 8.698 `omnigenumque`), the Latin Library variants, the `advisory`, the `about`, and every "(from memory)" attribution.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington, Servius). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.402–409, 1.713, 2.682–684, 2.707–708, 2.721–723, 3.12, 8.343, 8.370, 8.424 and 8.534–536, and the internal pointers 627, 628/710 and 720. All are right except the Book 1 claim in item 8. The hedge on 3.12 is now replaced by the line itself (item 21). For the scansion entries I also checked 11.247, 11.678 and 12.391 (*Iapyx*).

**Pass 2** re-read every edited field in full and made four more changes (P2-1 to P2-4).

**Scansion.** I hand-scanned all 124 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with my scansion syllable by syllable.
- **The scanner was wrong on 6 lines**: 631, 650, 671, 710, 726 and 727.
  - None of the six was flagged. The two flagged lines, 615 and 679 (COSTLY 2.0), are right.
  - Each of the six now has a hand entry.
- **No half-lines** fall in this part, so no carrier entries are needed.

Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). This caught one mistake of mine: 727 *extremique* was first split into two tokens; it is now one. Each entry was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and a script checked that count against its entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 6 entries apply
- **all 50 units get `sc`**
- all 124 lines pass the validator's metre check
- the scanner report after the fixes holds only the two COSTLY flags, 615 and 679. Both are hand-checked right. As with 8.292, 8.341 and 8.515 in 059–061, they get no entry. They do not block the build.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump` (`indent=1`, `ensure_ascii=False`, no trailing newline, as the drafter's file).
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 50 units, checked by script against a copy of the drafter's file taken before any edit. `title`, `titleEn` and `part` are unchanged. `about` has one change (item 25) and `advisory` has one (item 24).
- 19 units changed. `l` still has the same number of lines as `t` in every unit, and no `i` has a line break. Speech marks: 1 “ and 1 ” in each of `t`, `l` and `i`.
- **Note lengths.** Every note is 27–140 words. Four notes went over 140 with additions and were trimmed back:
  - unit 8 dropped "'procubuisse', perfect infinitive"
  - unit 14 dropped "'innaret fluvium'… with the accusative"
  - units 19 and 24 were reworded more tightly
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 66 insertions, 0 deletions, trailing newline kept, formatting as before (`indent=1`, no ASCII escaping). The new keys come after 8.606, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Severity counts: major 6, medium 2, low 27 (23 in pass 1, 4 in pass 2). Refused findings: 20. Scan-fixes entries added: 6.**

## Changes — pass 1

### Major
1–6. **Scansions the scanner got wrong, none flagged.** Each line now has a hand entry with its reason.
   - **8.631 *huic* read as two syllables**: prō-cŭ-bŭ | is-sĕ lŭ | pām gĕ-mĭ | nōs huic | ū-bĕ-ră | cir-cum (16 syllables). The scanner had hŭ-ĭc and 17. *huic* is one long syllable, as always in Virgil and as at 5.849.
   - **8.650 *quia* contracted**: as-pĭ-cĕ | rēs pon | t(em) au-dē | rēt quĭ-ă | vel-lĕ-rĕ | Cō-clēs (15). The scanner made *quia* one long syllable and the fourth foot a spondee, 14. The precedents are 2.84 and 5.231.
   - **8.671 *late maris***: Haec in | tēr tŭ-mĭ | dī lā | tē mă-rĭs | ī-băt ĭ | mā-gō (15). The scanner made *lātē* two shorts and *mă-rĭs* two longs: the right count, but the wrong quantities. The same error was fixed at 8.598.
   - **8.710 *Iapyge* read with consonantal I**: fē-cĕ-rat | Ig-nĭ-pŏ | tēns un | dīs ĕt Ĭ | ā-py̆-gĕ | fer-rī (16). The scanner made the I consonantal (Jā-), which lengthened *et*, and had 15.
     - The I of *Iapyx* is a short vowel everywhere I can check. The verse requires it at 11.247 (*condebat Iapygis*: dē-bă-tĭ | ā-py̆-gĭ | sā-grīs), at 11.678 (*venator Iapyge*) and at 12.391 (*dilectus Iapyx*), and Horace scans it the same way (Odes 1.3.4, *praeter Iapyga*, from memory).
   - **8.726 *Euphrates* (Greek eu split) and more**: fin-xĕ-răt | Eu-phrā | tēs ī | bāt iam | mol-lĭ-ŏr | un-dīs (14). The scanner split E-u, and it also made *-xe-* long and *-tēs* and *ī-* short, a fit with 15.
   - **8.727 *extremique hominum***: ex-trē | mī-qu(e) hŏ-mĭ | num Mŏ-rĭ | nī Rhē | nus-quĕ bĭ | cor-nis (15). The scanner made *-trē-* short and *hŏ-mĭ-* long: the right count, but the wrong quantities.

### Medium
7. **Unit 10 (639–641), a false label.** The note had "'Iovis ante aram'… 'ante' after its noun". *ante* stands before *aram*. It is the genitive *Iovis* that is set ahead of the preposition, and the note now says so.
8. **Unit 1 (609–611), a false claim about Book 1.** The note said that in Book 1 Venus "was gone before he knew her". In fact Aeneas recognises her as she leaves: *ille ubi matrem / adgnovit, tali fugientem est voce secutus* (1.405–406). The note now reads "and he knew her only as she turned to go (1.402–406)".

### Low
9. **Note 609–611**: the missing elision *sequ(e) obtulit* (611) is added.
10. **Note 612–614**: "the whole of it in two and a half lines" now reads "in three lines". The speech fills 612–614.
11. **Note 615–616**: "'sub adversa… quercu'… framing the line" was wrong, since *arma* comes first. It now reads "enclosing 'posuit radiantia'".
12. **`l` 630**: "in the green of Mavors cave" read *viridi* as a noun with *Mavortis*. It now reads "in the green, of Mavors, cave".
13. **Note 630–634**: it added "'huic' (one syllable) dative", which agrees with the 631 entry. "'procubuisse', perfect infinitive" was dropped to keep the note under 140 words; *procubuisse* is still named in the accusative-and-infinitive remark.
14. **Note 642–645**: "'citae… quadrigae'… framing the line" was wrong, since *citae* is the fourth word. It now reads "enclosing 'Mettum in diversa'".
15. **Note 649–651**: it added "'quia' is two short syllables, quĭ-ă", which agrees with the 650 entry. "'innaret fluvium'… with the accusative" was dropped for length.
16. **Note 663–666, the pilentum.** "their gift of gold to the state" was vague. It now reads "said to reward the gold they gave for the offering to Apollo vowed at Veii (Livy 5, from memory)", which is Livy 5.25 as I remember it.
17. **Unit 20 (666–670)**:
    - **`l` 667**: "the deep mouth of Dis" now reads "the deep doorways of Dis", keeping the plural *ostia*.
    - **`i` 668–669**: "a beetling crag", a stock phrase with a literary ring, is replaced by "a menacing crag", closer to *minaci* and as a precaution.
18. **Note 671–672**: it added "'lātē' is long in both syllables, 'măris' short in both", which agrees with the 671 entry.
19. **`i` 688, a precautionary rephrase.** "and in his train — the shame of it! — comes his Egyptian wife" now reads "and after him — an outrage! — follows his Egyptian wife".
20. **`l` 689**: "and all foams" could be read as "everything foams". It now reads "and the whole foams", for *totum… aequor*.
21. **Note 678–681, *penatibus et magnis dis***: "the same words end 3.12… (from memory)" was checked against the source and is right. The hedge is replaced by the line itself, *cum sociis natoque Penatibus et magnis dis*.
22. **Note 691–693**: "'pelago' dative" now reads "dative with the compound verb (or ablative of place)", since both are possible.
23. **`i` 700–701**: "the grim Furies swoop from the sky" added a verb the Latin does not have; *Dirae* is a second subject of *saevit*. It now reads "and with him the grim Furies from the sky above".
24. **`advisory`**: "Mettus's punishment takes two and a half lines" was wrong. The picture runs from 642 to 645, three lines and a word plus the apostrophe. It now reads "about three lines". See R5 for the advisory as a whole.
25. **`about`**: "the grove near Caere where the Etruscans are camped" now reads "close to where". The camp is *haud procul hinc* (8.603–604), not in the grove. This is the same correction 062's reviewer made to that part's `about`.
26. **`i` 705**: "at the terror of it all Egypt…" could be misread as "it all". A comma is added: "at the terror of it, all Egypt…".
27. **Unit 48 (726–728)**:
    - **`i` 728, a precautionary rephrase**: "the Araxes, chafing at its bridge" now reads "the Araxes, resentful of the bridge laid over it".
    - **Note**: it added "Eu-phrā-tēs" and "(ex-trē-mī, hŏ-mĭ-num)", which agree with the 726 and 727 entries.
28. **`i` 729–731, a rephrase of the book's last line as a precaution**, as the brief asks. The old `i` was "These were the things he wondered at… as he raised to his shoulder the glory and the destiny of all his line to come". It now reads: "Such are the scenes he marvels at across the shield of Vulcan, his mother's gift; he knows nothing of what they show, yet takes delight in the pictures, and he lifts onto his shoulder, with the shield, the renown and the destiny of the generations to come." This also puts `i` in the present, matching *miratur… gaudet* and `l`.
    - "the fame and fortune(s)" and "children's children" are avoided on purpose.
29. **Note 709–710**: "four syllables, I-a-py-ge, the first short" now reads "Ĭ-ā-py̆-gĕ, the I a short vowel, so 'et' before it stays short", which agrees with the 710 entry.

Items 9–29 make 21 numbered low items. Counted change by change, there are 23 pass-1 lows: items 17 and 27 count 2 each, and every other item counts 1.

## Changes — pass 2
- **P2-1 (low), `i` 710**: "the north-west wind" now reads "the west-north-west wind", to agree with the note's Iapyx.
- **P2-2 (low), note 649**: "the repeated word framing the line" was wrong. *similem similemque* stand in the middle of the line. It now reads "the two participles enclosing the repeated 'similem'".
- **P2-3 (low), note 678**: "'Augustus… Caesar', framing the line" now reads "spanning the line", since *Hinc* comes first.
- **P2-4 (low), note 689–690**: "'totum… aequor'… framing the two lines" now reads "spanning the two lines", since *totum* stands mid-line.

## Scan-fixes entries added (6)
These are appended after 8.606 in line order:
- **huic as one syllable (1)**: 8.631
- **quia as two syllables (1)**: 8.650
- **Wrong quantities, same count (2)**: 8.671 and 8.727
- **Iapyge with vocalic I (1)**: 8.710
- **Greek eu split, with wrong quantities (1)**: 8.726

Each entry matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 14–16 syllables and one ×. Each `why` states the count, and each count was checked by script.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Flagged COSTLY, right**:
  - **615** Dī-xĭt ĕt | am-plē | xūs nā | tī Cy-thĕ | rē-ă pĕ | tī-vit (15). *Cytherea* has four syllables, as at 1.257 and 8.523.
  - **679** cum pă-trĭ | bus pŏ-pŭ | lō-quĕ pĕ | nā-tĭ-bŭs | et mag | nīs dīs. This is a spondaic fifth foot with a monosyllabic ending, as at 3.12.
- **Greek eu**: *Leucaten* (677) is right: fer-vĕ-rĕ | Leu-cā | tēn au | rō-qu(e) ef | ful-gĕ-rĕ | fluc-tus. *Euphrates* (726) is fixed.
- **Initial Ae-**: *Aeneadae* (648), *Aegyptum* and *Aegyptia* (687, 688), *Aegyptus* (705), *aere*, *aevi*, *aequor*, *aethere* and *aequora* are all right.
- **Consonantal i**:
  - after a prefix: *coniugis* (612: con-jŭ-gis), *eiectum* (646: ē-jec-tum, three long syllables) and *coniunx* (688) are right. At 688 the scanner divides it *co–niunx*, which is cosmetic, as in QUESTIONS item 37.
  - at the start of a word: *iuvenci* (719), *Iovis* (640), *iungebant* (641) and *iura* (670) are right.
  - between vowels: *Tarpeiae* (652) is right.
  - *Iapyge* (710) is fixed.
- **Synizesis**: *cui* (680, 683) is one syllable and right. *deum* (698) has two syllables and is right. *quia* (650) and *huic* (631) are fixed.
- **Hiatus**: none in this part.
- **Cloelia** (651): *Cloe-* is one syllable (oe diphthong): Cloe-lĭ-ă. Right.
- **Other quantities checked**:
  - *mĕī* (612), *ācrem* (614), *lēvis* (624), *ēlectro* (624), *clĭpĕī* (625)
  - *īdem*, nominative plural, long (639); *cĭtae*, *dīversa* and *quădrīgae* (642); *Albāne* (643); *Rōmŭlĕo* (654)
  - *extŭderat*, from *extundo*, perfect *extŭdi* (665); *pīlentis* (666); *Cătĭlīna* (668)
  - *delphīnĕs*, the Greek -ĕs short (673); *Ĭtălos* and *Ĭtălis*, short I as in *Itali* at 1.109 (678, 715); *aperītur* (681); *Āgrippa*, long by position (682); *rostrată*, neuter plural with *tempora* (684)
  - *Ăntōnius* (685); *Ărabs* (706); *Cŭrēs* (638); *Lĕlĕgăs*, *Cāras* and *sagittĭfĕros* (725); *Nŏmădum* (724); *Ărāxēs* (728)

## Refused findings
- **R1 — 8.629 `ab Ascanio. pugnataque`**: **upheld** as a rule-5b misprint.
  - The *-que* of *pugnataque* adds *bella* to the list under *fecerat*, and the lowercase *p* agrees, so the sense allows only one reading: no sentence break.
  - The note calls it "a misprint for a comma". Whether the print meant a comma or no stop at all makes no difference to the sense, and `l`/`i` use a comma. The note is kept.
- **R2 — 8.691 `alta`**: **upheld** as a misprint for *Alta* (lowercase after the full stop ending 690). This is consistent with 8.556, 8.558, 8.489, 8.496, 8.510 and 8.514. The ruling asked in QUESTIONS item 43 is still open.
- **R3 — 8.694 `stuppea`**: **upheld** on the same grounds.
- **R4 — 8.698 `omnigenumque`**: **upheld** on the same grounds.
- **R5 — The `advisory`**: **kept, right in shape and in substance**, apart from item 24.
  - **Shape**: it is the `{lede, more}` object of the published Ovid parts (ovid-met-007, -008, -022), and the build copies a top-level `advisory` to the story.
  - **Substance, the Sabine women**: the abduction of the Sabine women to be wives is forced marriage, which falls under "sexual violence always". The Ovid parts flag such things even when they take half a line (008, 022, 032). The lede and the more say plainly what happened and that the poem gives it one phrase.
  - **Substance, Mettus**: his dismemberment, with the entrails dragged and the brambles dripping blood, alone sits on the "graphic detail rarely" line. Aeneid-061 gave no advisory for Mezentius (8.485–488). It is reasonable to include it in an advisory the part needs anyway.
  - **The rendering of *raptas sine more***: the advisory has "'seized against all custom'" and the note "'seized without custom'". Both are fair.
  - `claude/content-advisory.md` is still not in the repository (QUESTIONS item 36), so this was judged against conventions and the published Ovid advisories.
  - **This would be the first Aeneid part with an advisory.** See "For the owner".
- **R6 — The COSTLY flags at 615 and 679**: both are hand-checked right, so no entries were made, as at 8.292, 8.515 and others.
- **R7 — 8.688 *co–niunx* and 8.612 *con–iu-gis***: these are cosmetic divisions with the right quantities, so no entries were made (QUESTIONS item 37).
- **R8 — Note 683–684, *rostrata* "agrees in grammar with 'tempora'"**: **checked and right**. The final *-a* is short (fifth foot *trā-tă cŏ*), so *rostrata* is neuter plural with *tempora*, not the ablative with *corona*. It is a transferred epithet, as the note says.
- **R9 — `i` 625, "past all telling"**: kept. It is an ordinary idiom for *non enarrabile*, not a distinctive echo.
- **R10 — Note 635–638, *consessu caveae* "ablative of separation"**: kept. It goes with *raptas* ("seized from the seated crowd"). A place reading is also possible, but the label is defensible.
- **R11 — Note 652–654, Romulus's hut on the Capitol**: kept. It is hedged "said to be", and a *casa Romuli* on the Capitol is attested besides the Palatine one.
- **R12 — Note 652, "Marcus Manlius, afterwards called Capitolinus"**: kept. It matches Livy's "cui Capitolino postea fuit cognomen" (Livy 5.31, from memory).
- **R13 — Note 671–672, "the sea forms a band about the central scene"**: kept. It is interpretive but standard, and the `about` agrees.
- **R14 — Unit 30, the two-word unit *alta petunt:***: kept. It ends at a colon, and splitting there is within the conventions.
- **R15 — Latin Library variants** (687 *virisque*, 690–691 *-vulsum*/*-vulsas*, 704 *intendebat*, 708 and 715 *imm-*, 716 *maxima ter centum*): these are orthography, morphology or a simplex/compound verb pair with no change of sense, and correctly not noted. The notes give Greenough's spellings as his.
- **R16 — Rule 5 and rule 5b, anything else missed**: none found.
  - No punctuation looks dropped by the print.
  - 710 *Ignipotens* with a capital (lowercase at 628) and 679 *penatibus* lowercase (*Penatibus* at 3.12) are the print's inconsistencies, not misprints. The 628/710 difference is already noted.
- **R17 — Note 626–629, *haud* negating both adjectives**: kept. This is the usual reading (Servius).
- **R18 — Note 657, *tenebant* "on the point of taking it"**: kept. It is the conative imperfect, and `i` "all but held" agrees.
- **R19 — `i` elsewhere**: I found no distinctive echo of a published version beyond items 17, 19, 27 and 28, which were rephrased as a precaution.
- **R20 — Attributions kept, hedged "from memory" and unchecked against a text**: all are right as far as I remember. None was cut.
  - Iliad 19 (Thetis brings the armour) and Iliad 18 (the shield of Achilles)
  - Livy 1 (the Sabines, the treaty, Mettus), Livy 2 (Porsenna, Cocles, Cloelia), Livy 5 (Manlius and the geese, the matrons' gold)
  - Ovid, Fasti 3 (the ancilia)
  - Sallust (Cato against the Catilinarians)
  - Plutarch (Antony's great ships, Cleopatra's flight, the image with the snake in the triumph)
  - Agrippa's naval crown for Naulochus
  - Res Gestae (82 temples restored)
  - Servius (the Araxes bridge)
  - L&S on *egelidus*
  - Horace Odes 1.3 (only in this review, for *Iapyx*)

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading.
  - 8.629 `ab Ascanio. pugnataque`: a stray full stop inside the list governed by *fecerat*.
  - 8.691 `alta`, 8.694 `stuppea` and 8.698 `omnigenumque`: lowercase after a full stop. **The ruling in item 43 is still open.**
- **Advisory**: this is the first Aeneid part to carry one. It covers the Sabine abduction (635–638, under "sexual violence always") and Mettus's dismemberment (642–645). Remove the Mettus half if you want "graphic detail rarely" read strictly, as at 8.485–488 (aeneid-061, none given).
- **Scansion**: the build report should list only COSTLY 615 and 679, both hand-checked right.
  - 6 entries: 8.631 *huic* (one syllable), 8.650 *quia* (two), 8.671 *lātē măris*, 8.710 *Ĭāpy̆ge*, 8.726 *Euphrātēs*/*finxĕrat*/*ībat*, 8.727 *extrēmī hŏmĭnum*.
  - No doubtful quantities remain on the chosen fits.
- **Unchecked attributions** are as listed in R20.
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
