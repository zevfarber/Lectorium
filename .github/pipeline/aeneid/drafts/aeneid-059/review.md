# Review — aeneid-059 (Aeneid VIII.219–305), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 36 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's flagged calls:
- the rule-5b misprint 8.285 `tum` (lowercase after the stop ending 284)
- the missing comma after `aether` at 8.239–240
- the hypermetric line 8.228
- every attribution marked "(from memory)"

I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 8.104, 8.106, 8.107, 8.116, 8.136, 8.185, 8.188–189, 8.193–195, 8.198–199, 8.203, 8.207–208, 8.217–218, 2.792, 7.662 and 10.255. All of them say what the notes now say they say. One needed changing:
- **8.190** was cited to show Evander as an eyewitness. It only says "look at this crag". The note now cites **8.188–189** instead (*saevis… periclis servati*), where the Arcadians say they were saved (item 17).

**Pass 2** re-read every edited field in full. It made two more changes (P2-1 and P2-2).

**Scansion.** I hand-scanned all 87 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with my scansion syllable by syllable.
- **8.228 is UNRESOLVED.** It is a true hypermetric line and gets a hand entry. Its unit-mates 229 and 230 need entries too, and 229's own fit was also wrong.
- **The scanner was wrong with no flag on 6 more lines**: 221, 243, 263, 290, 298 and 301.
- **8.292 (COSTLY 3.0) is right**, so it gets no entry (R3).

Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and a script checked that count against its entry. For 228 the count is the sixteen that scan; the elided *-que* is not counted.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 9 entries apply
- the UNRESOLVED report for 228 is removed, so nothing is left that would make the build refuse
- all 87 lines pass the validator's check
- **all 36 units get `sc`**
- the scanner report keeps only the COSTLY flag at 292, which is confirmed right

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 36 units. I checked this by script against a fresh run of `make_units.py` into the scratchpad, whose output was identical to the drafter's `units.json` before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 18 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- Every note is 15–140 words; the longest is 135. No draft note was over the limit.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 104 insertions, 0 deletions, trailing newline kept. The new keys come after 8.200, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Speech marks.** These were checked in `t`, `l` and `i`, and each layer has 1 “ and 2 ”:
- **Evander, from 185**: his speech runs on from part 058, with no opening mark in unit 0, and closes at 275 in unit 21.
- **The Salii's hymn, 293–302**: it opens in unit 30 and closes in unit 33.

The validator will warn that the opening and closing marks are unequal. That is expected, because the speech opened in 058.

**Severity counts: major 7, medium 7, low 20 (18 in pass 1, 2 in pass 2). Refused findings: 16. Scan-fixes entries added: 9.**

## Changes — pass 1

### Major
1–7. **Scansions the scanner could not fit or got wrong with no flag.** Each line now has a hand entry with its reason.
   - **8.228, hypermetric (UNRESOLVED)**: ec-cĕ fŭ | rens ă-nĭ | mīs ă-dĕ | răt Tī | ryn-thĭ-ŭs | om-nem(que). The line has seventeen syllables, and sixteen count. The final *-que* elides into *accessum* at the start of 229 (synapheia).
     - The entry uses the house notation for earlier hypermetric lines (4.558, 5.753, 6.602): `"6om–nem×que"`, with *-que* unmarked.
     - *Tīrynthius* has long Tī, as 7.662 shows.
     - The build drops a COSTLY or UNRESOLVED report once a fix for that line is applied, so the UNRESOLVED goes and the build no longer refuses.
   - **8.229**: ac-ces | sum lus | trans hūc | ō-ră fĕ | rē-băt ĕt | il-lūc (14 syllables). The entry was needed anyway because 229 shares a unit with 228. The scanner's own fit was also wrong: it made *huc* and *ŏ-* short, and *-ra* and *fē-* long.
   - **8.221 *aerii***: rō-bŭr ĕt | ā-ĕ-rĭ | ī cur | sū pĕ-tĭt | ar-dŭ-ă | mon-tis (16 syllables). *āĕrius* has four syllables, as at Ecl. 1.58 *aeria*. The scanner read *ae* as a diphthong and made *pē-tīt* long.
   - **8.243 *siqua penitus***: nōn sĕ-cŭs | ac sī | quā pĕ-nĭ | tus vī | ter-ră dĕ | his-cens. The scanner made *si* and *qua* short and *pē-nī-* long. That fit has the same syllable count and four wrong quantities.
   - **Consonantal i after a prefix:**
     - **8.263 *abiuratae***: abs-trac | tae-quĕ bŏ | vēs ab | iū-rā | tae-quĕ ră | pī-nae (14). The scanner read ă-bĭ-ū- and had 15.
     - **8.290 *disiecerit***: ut bel | l(o) ē-grĕ-gĭ | ās ī | dem dis | iē-cĕ-rĭt | ur-bes (14). The scanner read di-si-e-ce-rit and had 15. *īdem* is the masculine.
   - **8.301 *Salve, vera Iovis***: Sal-vē | vē-ră Iŏ | vīs prō | lēs dĕ-cŭs | ad-dĭ-tĕ | dī-vīs. The scanner made *salvĕ* and *vĕ-* short, and *-rā* and *Iō-* long. That fit has the same syllable count and four wrong quantities.

### Medium
8. **8.298 *Typhoeus***, scansion. The scanner had the right quantities but divided the word Ty-phoe-us, with *oe* as a diphthong. The word is Ty-phō-eus (Τυφωεύς), with Greek *eu* as one syllable, and the audio reads vowels from `sc`. A hand entry was added. This is not the cosmetic consonant-division case of 058 R9, because here the vowel grouping changes.
9. **Note 228, a false label.** It said "'aderat', 'was there', the pluperfect sense of speed again", but *aderat* is imperfect. It now reads "'aderat', imperfect, 'was there', already, the moment the door was blocked."
10. **Note 228, a false claim.** It said Tiryns was "the city in the Argolid where Hercules grew up", but Hercules was reared at Thebes. It now reads "the city in the Argolid from which Amphitryon's family came; its 'Ti-' is long."
11. **Note 262–265, a false claim.** It said *boves* was "feminine because most of them are cows", but Cacus took four bulls and four heifers (8.207–208, checked). It now reads "feminine for the whole herd, bulls and heifers alike (8.207–208)."
12. **Note 298–300, a false label.** It called *turba capitum* "in apposition". The metre needs a long *turbā* in the third foot (bā că pĭ), so it is ablative. The `l` ("with its throng of heads") and the `i` already read it that way. It now reads "'with its crowd of heads', ablative: the metre needs the long 'a'."
13. **Note 293–295, a wrong cross-reference.** It said "Virgil makes both fall to the hero, as at Georgics 2.456–457". In the Georgics, Rhoetus, Pholus and Hylaeus fall in the Lapith brawl, which is laid to Bacchus, not Hercules. It now reads "Virgil makes both fall to the hero, though in the Georgics (2.455–457, from memory) they die in the Lapiths' drunken brawl."
14. **Note 271–272, an unsupported claim.** It said "the subject is most naturally Potitius… though some took it of Hercules himself (from memory: Servius discusses the question)". The Hercules reading is at least as natural, since Hercules founds his own altar in Ovid. Neutralised: "the subject is not stated, and may be Potitius, just named, or Hercules himself, who in Ovid sets up his own altar (Fasti 1.581, from memory)". The unverifiable Servius pointer is cut.

### Low
15. **8.230**: this line gets a scan-fixes entry with the scanner's own fit, which is correct (den-tĭ-bŭs | in-fren | dens Ter | tō-tum | fer-vĭ-dŭs | ī-ră). The entry is needed only because *dentibus infrendens* sits in the unit with 228, and a unit with an unresolved line gets no `sc`. 4.559 and 6.603 are the precedent.
16. **Note 220–221**: "'aerii… montis'… framing the line" was wrong, since *robur et* comes before it. It now reads "enclosing 'cursu petit ardua'". Also added that *aerii* has four syllables, with *ae* no diphthong.
17. **Note 222–223**: the 8.190 cross-reference was replaced by 8.188–189, as described at the top.
18. **Note 236–238**: cut the Latin Library's *ad amnem*. The note itself said "no change of sense", and conventions say to note a variant only where the sense changes.
19. **Note 238–240**: the comma sentence was reworded (see R2). "Most texts punctuate there and start a new clause" was an unverifiable claim about editions. It was also misleading, because *quo* governs all three verbs with or without a comma.
20. **Note 241–242**: *specus* "here masculine" now reads "usually masculine". Nothing in 241–242 shows its gender.
21. **Note 243–246**: "'qua' an adverb" now gives both readings: the adverb, or the indefinite with *vi*. Either way it is ablative, with a long *a*, which is what the metre needs. The `l` is kept (R8).
22. **`i` 243–246**: "as the light streamed in" now reads "streams in", to match "should split… cower" (present subjunctives).
23. **Note 247–250**: "'insperata… luce'… framing the line with 'deprensum… repente' between" was wrong, since *Ergo* comes first and *repente* last. It now reads "enclosing 'deprensum'".
24. **`l` 256**: *ipse* was missing. "and himself through the fire" now reads "and himself, he himself, through the fire".
25. **Note 262–265**: added that *abiuratae* is *ab-yu-*, with a consonant i. Cut "a monster in death as in life", which adds nothing to the Latin.
26. **`i` 262–265**: the tenses were present ("are wrenched… are shown… is dragged"). They are now past, to match the `i` of 259–261 and 265–267, which are both in the past.
27. **Note 268–270**: "'domus… Pinaria', framing the line" was wrong, since *et* comes first and *sacri* last. It now reads "'the Pinarian house', enclosing 'Herculei custos'".
28. **Note 276–278**: "'sacer… scyphus'… framing the line" was wrong. It frames *implevit dextram*.
29. **Note 288–289**: cut the Latin Library's *anguis*. It is morphology, which conventions say to ignore.
30. **Note 290–293**: the following edits were made.
    - Added that *idem* is the masculine, with long *ī*.
    - Added that *disiecerit* has a consonant i after the prefix.
    - "(told in Iliad 5, from memory)" now reads "(the sack is told in Iliad 5…)". Iliad 5 (Tlepolemus to Sarpedon) tells the sack for Laomedon's horses, but the Hesione rescue is not in it.
31. **Note 293–295**: added that *Hylaeeum* scans in three syllables, *Hy-lae-um* (see R4).
32. **Note 301–302**: added that *Salve* has a long final *e*, and that *vera* is vocative, with a short *a*.

The scansion pointers added in items 16, 21, 25, 30, 31 and 32, and the one already in note 228 (now with long Tī), agree with the hand entries.

Items 15–32 are the 18 pass-1 lows. Items 16, 25 and 30 each made more than one edit in the same note.

## Changes — pass 2
- **P2-1 (low)**: in note 293–295, item 13 left two semicolons in a row ("…foot (from memory); Virgil makes both fall to the hero; in the Georgics…"). These are now a full stop and "though".
- **P2-2 (low)**: in note 238–240, item 19's "though a new clause begins" sat awkwardly next to "'quo' governs all three verbs". It now reads "between the first two clauses".

## Scan-fixes entries added (9)
These are appended after 8.200 in line order, each with its reason:
- **UNRESOLVED, hypermetric (1)**: 8.228
- **Unit-mates of 228 (2)**: 8.229, where the scanner's own fit was also wrong, and 8.230, where the scanner's fit was right
- **Unflagged, wrong quantities or syllable count (5)**: 8.221, 8.243, 8.263, 8.290 and 8.301
- **Unflagged, wrong vowel grouping (1)**: 8.298

Each entry matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 14–16 syllables and one ×.

## Hand-scan notes on the special lines (scanner right, no entry)
- **8.292 (COSTLY 3.0), right**: rē-gĕ sŭb | Eu-rys | theō fā | tīs Iū | nō-nĭs ĭ | nī-quae (14 syllables). *Eu* is one syllable, and *-eō* of *Eurystheō* is one syllable by synizesis. Without synizesis the third foot would begin with a short (thĕ-ō), so no other fit exists. *sŭb* is short before the vowel.
- **Greek eu**:
  - *Euro* (223): one syllable, right. The line is right at COSTLY 1.5: tur-bā | tum(que) ŏ-cŭ | līs fŭ-gĭt | ī-lĭ-cĕt | ō-cĭ-ŏr | Eū-rō.
  - *Eurystheo* (292): right.
  - *Typhoeus* (298): fixed.
- **Initial Ae-**: there is no *Aeneas* in this part. *aether* (239) and *aestuat* (258) are right as diphthongs. *aerii* (221) is not a diphthong, and is fixed.
- **Consonantal i**:
  - Right as read: *deiecit* (226, dē-iē-), *iecit* (257), *iugo*, *iam*, *iuvenum*/*iuvenes*, *Iunonis*, *Troiamque* and *ianitor*.
  - Fixed: *abiuratae* (263), *disiecerit* (290) and *Iovis* (301, quantity).
  - *adiciunt* (304): the scanner divides it a–di–ci–unt instead of ad–(i)i–ci–unt, but the quantities (– ⏑ ⏑ –) are right. This is the cosmetic case of 058 R9 (*co–niun–xe–re*, *di–siec–tae*), so there is no entry (R5).
- **Hiatus**: there is none in the part. Every vowel meeting is an ordinary elision: *Quar(e) agite, o* (273), *de(um) et* (275), *t(e) ullae* (298), *Sali(i) ad* (285) and *bell(o) egregias* (290).
- **Other lines with a nonzero cost, checked and right**:
  - **221**: cost 1.1, but the fit is wrong and is fixed.
  - **248 (1.5)**: in-clū | sum-quĕ că | vō sax(o) | at(que) in | suē-tă rŭ | den-tem. *insueta* has *su* as a consonant, as at 6.16 *insuetum*.
  - **285 (0.8)**: tum Să-lĭ | (i) ad can | tus in | cen(sa) al | tā-rĭ-ă | cir-cum.
  - **294 (1.5)**: Hȳ-lae | (e)um-quĕ Phŏ | lum-quĕ mă | nū tū | Crē-sĭ-ă | mac-tas. Hȳ- is long, as Georg. 2.457 *magno Hylaeum* requires. See R4 on the spelling.
  - **296 (0.6)**: Tē Stў-gĭ | ī trĕ-mŭ | ē-rĕ lă | cūs tē | iā-nĭ-tŏr | Or-ci.
  - **299 (0.6)**: ar-dŭ-ŭs | ar-mă tĕ | nens nōn | tē ră-tĭ | ō-nĭs ĕ | gen-tem.
- **Other points checked**:
  - *obice* (227) has ō- long, as at 10.377.
  - *Aventini* (231) has short Ă-.
  - *Potitius* (269, 281) is Pŏ-tī-tĭ-ŭs.
  - *nequeunt* (265) has three syllables.
  - *propior fit* (280): *-or* and *fit* are long by position.
  - *turbā* (300) is long; see item 12.

## Refused findings
- **R1 — 8.285 `tum`**, lowercase after the stop ending 284: **upheld** as a rule-5b misprint. This is consistent with 058 R2/R3 (8.124, 8.217) and 8.9, 8.79 and 7.290. `t` stays as printed, `l`/`i` read "Then", and the note opens with the print's reading. The general ruling asked in QUESTIONS item 43 is still open.
- **R2 — 8.239–240, no comma after `aether`**: **reasonable as printed, not missing punctuation**. *quo* governs all three verbs (*intonat*, *dissultant*, *refluit*), and the first two stand in asyndeton. The construction reads correctly without a mark, and nothing is misrepresented. A modern editor would probably print a comma, but its absence is not a misprint. It is not clearly a rule-5 case either. The note now says simply that Greenough prints none, and that *quo* governs all three.
- **R3 — 8.292 (COSTLY)**: the scanner's fit is **right**, so there is no entry. It stays in the build's scanner report.
- **R4 — 8.294 `Hylaeeumque`**: the scanner's fit is **right** for the metre, with *-eum* run together. However, the name is Hylaeus (Ὑλαῖος), the Latin Library prints *Hylaeumque*, and I know no form *Hylaeeus*. The doubled *e* may be a slip of the print or of the TEI. The note now says the word scans in three syllables, *Hy-lae-um*, and does not call it a misprint. **For the owner.**
- **R5 — 8.304 *adiciunt***: the division *a–di* is cosmetic and the quantities are right, so there is no entry (058 R9). The drafter's note (*ad-yi-ci-unt*, *ad* long) is right.
- **R6 — 8.223, 248, 285, 296 and 299 (nonzero cost)**: all are right, so there are no entries.
- **R7 — Note 219, *Alcidae* "dative of reference"**: kept. The genitive is equally possible, but the label is true of one natural reading and the sense is the same.
- **R8 — `l` 243, "if somehow"**: kept. The adverb reading of *siqua* is possible, and the note now gives both.
- **R9 — Note 236, "on the left as Hercules faces it"**: kept as a reasonable interpretation of *laevum*.
- **R10 — `i` 239, "the whole vast sky"**: kept. "whole" is a slight addition that the register can bear.
- **R11 — Note 228, the hypermetric explanation**: kept, because it is right, synapheia and all.
- **R12 — Attributions kept, hedged or standard**:
  - Iliad 20: Achilles thrice lunging at Hector in the mist (230), and Hades' fear that the earth will be split open (243)
  - the Homeric Hymn to Hermes oath (263)
  - Livy 1.7 (the Pinarii late to the feast) and 9.29 (Appius Claudius, 312 BC, the Potitii extinct within a year)
  - Servius on the poplar crown from the underworld (276) and on Salii of Hercules at Tibur (285)
  - Pindar Nemean 1 and Theocritus 24 (the snakes)
  - Iliad 5 (the sack of Troy)
  - Sophocles' Trachiniae (Oechalia)
  - Pholus and the poisoned arrow
  - Typhoeus and the Gigantomachy

  All are right as far as I remember. None could be checked against a text, so each keeps "(from memory)". Two were corrected: Georgics 2 (item 13) and Servius on *statuit* (item 14, cut).
- **R13 — The `i` echo check**: I found no distinctive echo of a published version. "fear put wings on his feet" and "glory added to the gods" are the plain sense of the Latin.
- **R14 — Note 219 "atro felle"**: kept, because "split across the line" is right.
- **R15 — `title`, `titleEn`, `part` and `about`**: these are accurate and our own, and were left unchanged.
- **R16 — Speech-mark counts (1 “, 2 ”)**: these are correct for this part, as explained at the top.

## For the owner (QUESTIONS.md)
- **Misprint (rule 5b)**: 8.285 `tum`. `t` is as printed, and `l`/`i` read "Then". The ruling on lowercase after a stop (item 43) is still open.
- **8.239–240, no comma after `aether`**: I judge it reasonable as printed and not a rule-5 case. The decision is yours.
- **8.294 `Hylaeeumque`**: this is possibly a misprint for *Hylaeumque*. It is left as printed, and the note gives the three-syllable scansion.
- **Build report**: the COSTLY flag at 8.292 will still show in the report. The fit was checked by hand and is right, and no entry was made.
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
