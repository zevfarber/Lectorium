# Review — aeneid-049 (Aeneid VII.1–106), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 42 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference, and every historical or mythological claim. I also checked the speech marks and the rule-5b misprint notes (7.35, 7.41, 7.45, 7.50, 7.68), the bracketed line 7.74, the one Latin Library variant that changes the sense (7.66 *ex*/*et*), and every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened. Every in-poem cross-reference was checked against the pinned source:
- 2.512–514, 2.682–686 and 2.782
- 4.173–188
- 5.732 and 5.779–815
- 6.86–87, 6.234, 6.381, 6.764 and 6.900
- 7.189–191
- 8.319–325

**Pass 2** re-read every edited field in full and made one more change (P2-1).

**Scansion.** I hand-scanned all 106 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's six-foot rule: feet 1–6, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` also states its syllable count, and a script checked that count against the entry. A replica of the build's scansion step, with all fixes applied, gives an empty scanner report (the 7.5 COSTLY flag is cleared), and all 106 lines pass the six-foot check.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 42 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words. Five draft notes were over: units 4, 19, 25, 26 and 27, at 149, 145, 162, 147 and 163 words.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands, or port the changes first.
- The diff to `scan-fixes.json` only appends: 139 insertions, 0 deletions, trailing newline kept.

**Speech marks.** `t`, `l` and `i` each have 3 “ and 3 ”.
- The seer, 68–70: one unit. “ at *Externum*, ” after *cernimus,*, “ at *adventare*, ” after *arce.*
- Faunus, 96–101: “ on the first unit (*Ne pete*), ” on the last (after *videbunt.*).

All marks agree across the layers, unit for unit.

**Severity counts: major 9, medium 12, low 27 (26 in pass 1, 1 in pass 2). Refused findings: 22. Scan-fixes entries added: 12.**

## Changes — pass 1

### Major
1–9. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities were wrong. Each line now has a hand entry.
   - **7.15**: the scanner had *gēmītŭs ĭrae*. Hand scansion: Hinc ex | au-dī | rī gĕ-mĭ | tūs ī | rae-quĕ lĕ | ō-num.
   - **7.21**: the scanner read *Troes* as one syllable, made *pā-tē-* long and made *tă-* short. Hand scansion: Quae nē | mons-tră pĭ | ī pă-tĕ | ren-tur | tā-lĭ-ă | Trō-ĕs.
   - **7.41**: the scanner had *dīvā mō-nĕ Dĭcam*. Hand scansion: tū vā | tem tū | dī-vă mŏ | nē dī | c(am) hor-rĭ-dă | bel-la.
   - **7.53**: the scanner had *mă-tŭ-rā vī-rō*. Hand scansion: iam mā | tū-ră vĭ | rō iam | plē-nīs | nū-bĭ-lĭs | an-nīs.
   - **7.66**: the scanner had *ob-sĕ-dĕ-re ā-pī-cem*. Hand scansion: ob-sē | dēr(e) ă-pĭ | c(em) ex pĕ-dĭ | bus per | mū-tŭ-ă | nē-xīs.
   - **7.91**: the scanner made *conloquio* two syllables with a long *lo*, made *ĭmĭs* short and made *Ā-chē-* long. Hand scansion: con-lŏ-quĭ(o) | at-qu(e) ī | mīs Ă-chĕ | ron-t(a) ad | fā-tŭr Ă | ver-nīs.
   - **7.100**: the scanner had *pē-dī-bus* and a short *Sŏl*. Hand scansion: om-nĭ-ă | sub pĕ-dĭ | bus quā | Sōl ŭt | rum-quĕ rĕ | cur-rens. The ŭ of *utrumque* is lengthened before *tr*. That is the only fit (see the doubtful list).
   - **7.104**: the scanner had *lă-tĕ vō-lī-tans*. Hand scansion: sed cir | cum lā | tē vŏ-lĭ | tans iam | Fā-mă pĕr | ur-bēs.
   - **7.105**: the scanner ran *Lao-* into one syllable and made *-mē-* long. Hand scansion: Au-sŏ-nĭ | ās tŭ-lĕ | rat cum | Lā-ŏ-mĕ | dōn-tĭ-ă | pū-bēs. This matches the published *Laomedontiadae* at 3.248.

### Medium
10–12. **Scansion: the packet's flag and the known blind spots.**
   - **7.5** (packet flag, COSTLY 2.0): the scanner read *exsequiis* as three syllables, ex-sequ-iis, with *se* long. It is ex-sĕ-quĭ-īs. Hand scansion: At pĭ-ŭs | ex-sĕ-quĭ | īs Aē | nē-ās | rī-tĕ sŏ | lū-tīs. *Aeneas* in this line was already right.
   - **7.29 *Aeneas***: the scanner split Ae- into two short syllables (A-ĕ-nĕ-ās). Hand scansion: At-qu(e) hīc | Aē-nē | ās in | gent(em) ex | ae-quŏ-rĕ | lū-cum.
   - **7.33 *adsuetae***: the scanner read four syllables, ad-sŭ-ē-tae. The u is consonantal, as in *suesco*, so the word is ad-suē-tae. That is the reading of the 6.16 (*insuetum*), 6.814 (*desueta*) and 6.832 (*adsuescite*) entries. Hand scansion: ad-suē | tae rī | pīs vŏ-lŭ | crēs et | flū-mĭ-nĭs | al-veo. Both readings fit the line, so this is listed with the doubtful quantities. A sentence was added to the unit note (item 26).
13. **Note 3–4, a wrong label**: "Note the order in 'sedem tuus' and 'ossaque nomen', words of two clauses interleaved." Both pairs belong to one clause each: *sedem* and *tuus* are both in the first clause, *ossa* and *nomen* both in the second. The note now reads: "Note the order: 'tuus' is held apart from 'honos' by 'sedem', and in the second clause the object 'ossa' comes before its subject 'nomen'."
14. **l 38–39**: "when the stranger fleet / first the army brought" made *advena* agree with *classem*. It goes with *exercitus*, as the note itself says. It now reads "when, a stranger, its fleet / first the army brought".
15. **l and note 56, *atavis***: "great-great-grandfathers" is wrong. An *atavus* is a great-great-great-grandfather (*avus, proavus, abavus, atavus*). In `l` the word is now "forefathers". The note now reads "'powerful in grandfathers and forefathers'… ('atavus' is strictly the great-great-great-grandfather)".
16. **l and i 66–67, Greenough's *ex***: both layers translated the Latin Library's *et* ("and by their feet…", "and with their feet locked…"), though the note rightly says that with Greenough's *ex* the two clauses stand with no connective.
    - `l` now reads "settled on the crest; from their feet, through each other linked,".
    - `i` now reads "and settled on the crest; hanging by their feet, locked each to each, a sudden swarm dangled from the leafy bough."
    - The variant sentence in the note was tightened.
17. **Note 71–73, a false claim**: "Lavinia is named here for the first time." Anchises names her at 6.764 (*Lavinia coniunx*). The note now reads "Lavinia, foretold as Aeneas's wife by Anchises (6.764), now appears in the story."
18. **l, i and note 74, *omnem ornatum***: the draft treated *ornatum* as the subject of *cremari* ("[and all her adornment… to be burned]"). After the personal *visa (est)*, Lavinia stays the subject, so *omnem ornatum* is an accusative of respect, like *comas* in 75.
    - `l` now reads "[and in all her adornment with crackling flame to be burned]".
    - `i` now reads "[and to burn in crackling flame in all her finery,]".
    - The note says so.
19. **Note 81–84, a wrong label**: "'Mephitim', with the Greek-style accusative in '-im'". The *-im* is the old Latin i-stem accusative (*turrim*, *vim*), not Greek. The note now reads "with the old accusative in '-im' (as 'turrim')".
20. **Note 89–91, a wrong cross-reference**: "the plural 'Averni'… as at 5.732". At 5.732 the form is the neuter *Averna per alta*. The note now reads "the plural standing for the lower world, as 'Averna per alta' at 5.732". The form *Avernis* fits either gender.
21. **i 32–34, `l` and `i` disagreed**: `i` said "filling the air… with their sweet song", which drops *mulcebant*. `l` has "were soothing". `i` now reads "were charming the air with their song, round about and overhead, and flitting through the grove."

### Low
22. **i 1–2**: "You too, Caieta, nurse of Aeneas, gave our shores a fame that will never die" had the shape of the familiar versions. It is now "Caieta, Aeneas's nurse, you also, in your death, won for our coast a fame that will not fade;".
23. **Note 1–2**: "the harbour where Aeneas landed" is now "the harbour Aeneas made for at the very end of Book VI (6.900)". The source says only *fert… portum*.
24. **l, i and note 8–9**:
    - In `l`, "nor the shining his course" is now "their course". *Cursus* is the Trojans' voyage.
    - In `i`, "does not refuse its light to their course; under its quivering beams the sea gleams" was close to the old prose versions. It is now "The breezes freshen behind them as night comes on, and the white moon is generous to their voyage; the sea sparkles in her shimmering light."
    - In the note, "bright and full" is now "bright". *Candida* does not say the moon is full.
25. **Note 10–14 (trim, 149 → under 140)**: "in Virgil's day it was joined to the mainland, but it had been thought an island" is now "it had once been thought an island". The gloss on *inaccessos* was dropped, since `l` shows it.
26. **Note 32–34**: added that *adsuetae* is three syllables, ad-suē-tae, to go with the scan fix.
27. **i 15–16**: "straining against their chains and roaring late into the night" was close to the known renderings. It is now "From there came the groaning and the rage of lions that would not bear their chains, roaring in the dead of night,".
28. **Note 15–16**: added that *recusantum* and *rudentum* have the shorter genitive *-um* for *-ium*.
29. **i 17–20**: "all once men, whom the cruel goddess Circe with her potent herbs had stripped of human form" is now "creatures that had been men, until the pitiless goddess Circe, with her herbs of power, took away their human looks and clothed them in the features and hides of beasts."
30. **i 25–26**: "Dawn shone yellow as saffron in her rosy chariot" is now "Already the sea was reddening under the first rays, and high in the heavens saffron Dawn glowed in her rose-coloured car,".
31. **i 35–36**: "He orders his comrades to change course and turn their prows to land, and joyfully he enters the shady river" was the plain shape found in several versions. It is now "He bids his crews alter course and swing their bows towards the shore, and glad at heart he passes into the shadowed river."
32. **Note 44–45**: dropped the closing sentence about *moveo.Rex*. It repeated the misprint note on the next unit, and rule 5b puts that note on one unit only.
33. **Note 45–46**: "corrected here; t keeps the print…, and so this unit begins in the middle of line 45" is a non sequitur, since the unit begins mid-line because the sentence does. It now reads "a misprint for 'moveo. Rex'; only the spacing is affected, and t keeps the print, because t must match the pinned source."
34. **i 45–46**: "had governed the countryside and its towns in a long, unbroken peace" lost *placidas* and added "unbroken". It is now "was ruling over fields and cities that lay quiet in a long peace."
35. **Note 47–49 (trim, 145 → under 140)**: dropped the gloss "'Refert' is 'names'", since `l` shows it.
36. **l 50–51**: "in its early growth, rising, was snatched away in youth" rendered *iuventa* twice. It is now "in its first youth, as it rose, it was snatched away."
37. **i 52–53**: "ripe for a husband" is the stock rendering. It is now "already fit for a husband, her years full, of an age to be wed." (see P2-1).
38. **Note 54–55**: "Ausonia is an old name of a people of central Italy" is now "the land of the Ausones, an old people of south-central Italy".
39. **Note 59–63 (trim, 162 → under 140)**: the *quam… inventam* gloss was shortened, and the *cum conderet* gloss and "The laurel is sacred to Phoebus Apollo" were dropped. "(you'll see it often with parts of the body…)" was shortened to "(again 'accensa comas', 75)".
40. **Note 64–67 (trim, 147 → under 140)**: dropped the *stridore ingenti* gloss, which `l` shows. The variant wording was also tightened (item 16).
41. **Note 68–70 (trim, 163 → 130)**: the misprint sentence now uses the house wording of 5.670 and 5.741 ("the closing mark set after the space and joined to 'inquit'"). Dropped "'Isdem' is 'eisdem'" and the *continuo vates* gloss. *Dominarier* is now "the old form of the infinitive 'dominari', with the archaic ending '-ier'".
42. **Note 71–73 (trim)**: the *iuxta genitorem* gloss was dropped (keeping "'Adstat' is Greenough's spelling of 'astat'") to make room for item 17.
43. **Note 74**: "it reads like an addition meant to fill out the picture, and the sentence runs well without it" was the drafter's guess about authenticity. It is now "the sentence is complete without it".
44. **Note 81–84**: "Horace places an Albunea at Tibur" now cites the poem: Odes 1.7, *domus Albuneae resonantis*.
45. **Note 85–86**: "Oenotria, 'the land of wine'" stated a popular etymology as fact. It now reads "(from a king Oenotrus; it was also linked with the Greek word for wine)".
46. **Note 96–97**: "'conubiis'… frames the line with 'Latinis'" was not accurate, since *conubiis* is the third word. It is now "is held apart from its adjective 'Latinis' at the line-end".
47. **l 100–101**: "where the Sun, at either running back, / looks on the Ocean" was garbled. It is now "where the Sun, on his returning course, either / looks on Ocean".

## Changes — pass 2
- **P2-1 (low)**: in `i` 52–53, the pass-1 wording "a girl now grown to womanhood" lost *viro*. It now reads "already fit for a husband, her years full, of an age to be wed."

## Scan-fixes entries added (12)
These were appended at the end of `scan-fixes.json`, each with its reason:
- 7.5
- 7.15
- 7.21
- 7.29
- 7.33
- 7.41
- 7.53
- 7.66
- 7.91
- 7.100
- 7.104
- 7.105

Each matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 13–16 syllables and one ×. In the replicated build, all 12 apply, the scanner report is empty, and all 106 lines pass the validator's check.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: these are right: *Aeneia* (1, Aē-nē-ĭ-ă), *aeternam* (2), *aequora* (7), *aethere* (25), *aequore* (29), *aethera* (34, 65), and *Aeneas* in 5 (inside the 7.5 entry). Only *Aeneas* in 29 was split (item 11).
- **Greek names**: *Circaeae* (10), *Circe* (20), *Erato* (37, Ĕ-ră-tō), *Tiberinus* (30), *Tyrrhenam* (43), *Phoebo* (62), *Oenotria* (85), *Oceanum* (101, Ō-cĕ-ă-num) and *mephitim* (84, mĕ-phī-tim) are right. *Troes* (21), *Acheronta* (91) and *Laomedontia* (105) are fixed.
- **Greek eu**: there is none in this part.
- **Consonantal i after a prefix**: *adiungi* (57) is ad-iun-gī, three syllables with a- long by position. The division *a–diun* is cosmetic, the same as *subiectis* at 6.853. *coniunx* (56) is con-iunx, two syllables. Both are right. *Caieta* (2) is Cā-iē-ta, right. *Huius* (64), *maior*/*maius* (44–45) and *iuxta* (72) are right.
- **Hiatus**: there is none. Every vowel meeting is an ordinary elision: *Hesperia in*, *mare et aethere ab*, *magno e*, *subita ex*, *Circe in*, *nocturna in*, among others. *iuventa est* (51) and *luco est* (95) are prodelision.
- **Others checked and right**:
  - quantities and syllable counts: *tenuīs* three syllables (14), *Lāvīnia* (72), *alveo* by synizesis (33, inside the entry), *conubiis* cō-nŭ-bĭ-īs (96)
  - long by nature: *quierunt* (6), *Pīcus* (48), *Marīca* (47), *Sāturne* (49), *Albuneā* (83), *sērā* (16), *multā… arenā* (31), *totā* (54), *iuxtā* (72), *flammā* (74), *visū* (78), *fāmā fātīs* (79), *hārum* (94), *monitūs* (102)
  - short syllables: *Ĭtalae* (85)
  - long by position before a stop and liquid: *sacrasse* sā- (62), *cedrum* cē- (13), *sacra* sā- (60), *sacro* (83)

## Doubtful quantities entered on the only fit
- **7.100 *utrumque***: the ŭ is lengthened by position before *tr*. Without that, no hexameter fits (Sōl and quā are long by nature). Elsewhere the ŭ is short, as published at 2.61 (*in utrumque*, aeneid-009).
- **7.33 *adsuetae***: the line scans both as ad-sŭ-ē-tae and as ad-suē-tae. The entry follows the consonantal-u convention of the 6.16, 6.814 and 6.832 entries.
- **Scanner's fits, no entry**: *cēdrum* (13), *sācrasse* (62), *sācra* (60) and *sācro* (83) are long by position before a stop and liquid, the only fit in each place.

## Refused findings
- **R1 — Circe in Odyssey 10** (unit 10–14): kept. In Od. 10 the men hear Circe singing at her great loom, and lions and wolves she has drugged are round her house. Book 10 is right, and the note gives no line numbers.
- **R2 — Erato in Apollonius 3** (unit 37–40): kept. *Argonautica* 3 opens by invoking Erato (εἰ δ' ἄγε νῦν, Ἐρατώ…), before Medea's love. Virgil's *Nunc age* answers εἰ δ' ἄγε νῦν.
- **R3 — Albunea in Horace** (unit 81–84): kept, and the cite was added (item 44). Odes 1.7.12 puts *domus Albuneae resonantis* at Tibur. "Virgil seems to set it near Laurentum" is hedged.
- **R4 — Lucretius 1.123, *modis miris*** (unit 89–91): kept. The line is *sed quaedam simulacra modis pallentia miris*, in the passage on Ennius and the *Acherusia templa* (1.120–126). Virgil reuses it at Georgics 1.477.
- **R5 — 7.35 *flectere*, 7.41 *tu*, 7.50 *filius* as rule-5b misprints**: kept. The precedent is 5.481 (*sternitur*), 5.556 (*omnibus*), 6.472 (*tandem*) and 6.486 (*circumstant*), all published as misprints in this form. See the owner question below.
- **R6 — 7.68 *cernimus, ”inquit***: kept as a misprint, as at 5.670 and 5.741 (published). The wording was brought into line (item 41).
- **R7 — 7.45 *moveo.Rex***: kept as a spacing misprint with one note (items 32–33). The precedent 2.13 *incipiam.Fracti* was given a plain note.
- **R8 — 7.66 *ex pedibus***: not a misprint. *Ex* gives sense ("hung from their own linked feet"), so rule 5b does not apply. It stays as a variant note.
- **R9 — 7.74 bracket**: Greenough's `<del>` is printed inside [ ] as the conventions require, and the note says so.
- **R10 — historic infinitives 15–18** (*exaudiri*, *saevire*, *ululare*): kept. The nominatives *sues*, *ursi* and *formae* show the construction.
- **R11 — *Quae* as a connecting relative (21)**: kept. It is a connecting relative used adjectivally with *monstra… talia*.
- **R12 — *ferri* (78) as a historic infinitive**: kept.
- **R13 — *cum inversum* (27, 105)** and **generalising *cum* + perfect (87)**: kept.
- **R14 — *Laurentis* (63) in apposition to *nomen***: kept. *Laurentis* cannot be a dative, so the dative reading "to his Laurentine settlers" is ruled out.
- **R15 — Turnus "named here for the first time" (56)**: verified. There is no *Turnus* in Books I–VI of the source.
- **R16 — the other cross-references in the notes**: verified in the source:
  - Misenus 6.234 and Palinurus 6.381
  - Neptune and Venus 5.779–815
  - the Tiber in 2.782 and 6.87
  - *bella, horrida bella* 6.86
  - Priam's laurel 2.512–514
  - Iulus's flame 2.682–686
  - Picus 7.189–191
  - Saturn 8.319–325
  - Fama 4.173–188
- **R17 — Marica at Minturnae; Picus in Ovid, Met. 14; Horace's *flavum Tiberim***: kept. All are standard. Horace's *flavum Tiberim* is Odes 1.2.13; the note names Horace without a cite.
- **R18 — i 44–45 "A grander sequence of events is opening before me"**: kept. It is not a known version's wording.
- **R19 — i 79–80 and 98–101**: kept. Neither is a known version's full clause.
- **R20 — "Iliadic half" (1, 44)**: kept. It is the usual description.
- **R21 — Latin Library variants**: only 7.66 changes the sense. The rest are orthography (*adspirant*, *praesaepibus*, *voltus*, *arena*, *divom*, *adstat*, *siqua*) and are rightly noted as Greenough's spellings or ignored.
- **R22 — `title`, `titleEn`, `part`, `about`**: these are our own and borrow no translation's heading. Unchanged.

## For the owner (QUESTIONS.md)
- **Lower-case after a full stop in Books VII–VIII.** This part treats three cases (7.35, 7.41, 7.50) as rule-5b misprints, following 5.481, 5.556, 6.472 and 6.486. The pinned source has many more ahead: 7.259, 7.267, 7.274 and 7.290, and about fifteen in Book VIII (8.9, 8.79, 8.124, 8.217, 8.285, 8.310, 8.366, 8.489, 8.496, 8.510, 8.514, 8.556, 8.558, 8.691, 8.694, 8.698). That frequency makes it look like a habit of the encoding, or of Greenough's print in these books, rather than scattered misprints. Rule 5b excludes an edition's habits, so the owner may want to rule once for all of them, before the Book VIII parts.
- **5.301 *adsueti* (aeneid-034, published)**: it was published with the scanner's ad-sŭ-ē-tī (four syllables). The entries at 6.16, 6.814 and 6.832, and now 7.33, read the u as consonantal (ad-suē-tī). The line fits both ways (ad-suē | tī sil | vīs cŏ-mĭ | tēs sĕ-nĭ | ō-rĭs Ă | ces-tae). A `scan-fixes.json` entry for 5.301 and a rebuild of aeneid-034 would make it consistent. This is the same kind of item as 2.509 *desueta* in the 048 review.
- **`make_units.py` is stale**: `drafts/aeneid-049/make_units.py` still holds the drafter's strings. Building from `units.json` is fine. Re-running `make_units.py` would discard this review.
- **Misprints to record (no emend list for the Aeneid)**: 7.35 `flectere` → `Flectere`; 7.41 `tu` → `Tu`; 7.50 `filius` → `Filius`; 7.45 `moveo.Rex` → `moveo. Rex`; 7.68 `cernimus, ”inquit` → `cernimus,” inquit`. In each case `t` is as printed, and `l`/`i` give the reading.
- **From memory, worded as attributions**: Odes 1.7 (Albunea), Lucretius 1.123, *Argonautica* 3 (Erato). None was checked against a text in this run.
- **Doubtful quantities on the only fit**: 7.100 *ŭt-* lengthened before *tr*; 7.33 *adsuetae* read ad-suē-tae.
