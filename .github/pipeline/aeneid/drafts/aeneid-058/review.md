# Review — aeneid-058 (Aeneid VIII.102–218), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 49 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's flagged calls:
- the rule-5b misprints 8.113 `tenditis? ”inquit`, 8.124 `excepitque`, 8.137 `orbes` with no stop, 8.214 `Amphytrioniades` and 8.217 `reddidit`
- 8.122 `ait` printed without marks
- the drafter's doubts on 130 (the Atridae kinship), 159 (Priam's visit to Arcadia), the Servius items, Ennius *accipe daque fidem*, Livy 1.7, Propertius 4.9, the Homeric Hymn to Hermes, Iliad 6, 7 and 20, and Odyssey 1

I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 8.1, 8.9, 8.51–56, 8.73, 8.86–89, 8.99–100, 8.269–272, 8.336, 8.351, 8.581, 7.68, 7.152–155, 7.206–209, 7.320, 7.594, 1.216, 2.722, 3.163, 3.167, 9.427 and 10.479–489. All of them say what the notes say they say. Two needed rewording:
- **8.351 and 7.594** both print *inquit* with commas, which the drafter's note itself admitted (item 24).
- **8.55–56** is now cited for the Tiber's instruction to ally with the Arcadians (item 21).

**Pass 2** re-read every edited field in full. It made four more changes (P2-1 to P2-4).

**Scansion.** I hand-scanned all 117 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with my scansion syllable by syllable.
- The scanner was **wrong with no flag on 16 lines**, and **wrong as flagged on 1 (8.194)**.
- The other two flagged lines, **8.154 and 8.167, are right**, so they get no entry (R8).

Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and a script checked that count against its entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 17 entries apply
- all 117 lines pass the validator's check
- **all 49 units get `sc`**
- the scanner report keeps only the COSTLY flags at 154 and 167, both confirmed right

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written in `aeneid_lib.jdump` format.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 49 units. I checked this by script against a fresh run of `make_units.py` into the scratchpad, whose output was identical to the drafter's `units.json` before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 27 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- Every note is 15–140 words; the longest is 140. Five draft notes were over the limit: 102 (159 words), 121 (144), 127 (157), 136 (197) and 201 (150). All are now within it.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 189 insertions, 0 deletions, trailing newline kept. The new keys come after 8.100, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Speech marks.** These were checked in `t`, `l` and `i`:
- **Pallas, 112–113**: unit 3 opens and closes the speech. In `t` the close is the misplaced `”inquit` (R1).
- **Pallas, 114**: unit 4 opens and closes it again, as printed.
- **Aeneas, 117–120**: units 6 and 7.
- **Pallas, 122–123**: unit 8. In `l` and `i` the speech is broken round *ait* (2 “ and 2 ”). In `t` it is as printed (1 and 1).
- **Aeneas, 127–151**: units 12 and 22.
- **Evander, 154–174**: units 24 and 32.
- **Evander, from 185**: opens in unit 36 and runs on into the next part, so no closing mark falls here.

**Severity counts: major 16, medium 6, low 29 (25 in pass 1, 4 in pass 2). Refused findings: 20. Scan-fixes entries added: 17.**

## Changes — pass 1

### Major
1–16. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities or the syllable count were wrong. Each line now has a hand entry with its reason.
   - ***Aeneas*/*Aenean*, Ae- split in two:**
     - **8.115**: Tum pă-tĕr | Ae-nē | ās pup | pī sīc | fā-tŭr ăb | al-ta (14 syllables). The scanner had 15.
     - **8.126**: Tum rē | (gem) Ae-nē | ās dic | tīs ad | fā-tŭr ă | mī-cis (13). The scanner had 14.
     - **8.178**: ac-cĭ-pĭt | Ae-nē | ān sŏ-lĭ | ō(que) in | vī-tăt ă | cer-no (15). The scanner had 16.
     - **8.182**: Ves-cĭ-tŭr | Ae-nē | ās sĭ-mŭl | et Trō | iā-nă iŭ | ven-tus (15). The scanner had 16.
   - **8.152 *Dixerat Aeneas. Ille os oculosque***: Dī-xĕ-răt | Ae-nē | ās il | l(e) ōs ŏ-cŭ | lōs-quĕ lŏ | quen-tis. The scanner made -nē- and -ās short and ŏ-cŭ- long.
   - **Greek eu split in two:**
     - **8.136 *Teucros***: ad-vĕ-hĭ | tur Teu | crōs Ē | lec-tram | max-ŭ-mŭs | At-las.
     - **8.161 *Teucros***: mī-rā | bar-quĕ dŭ | cēs Teu | crōs mī | rā-băr ĕt | ip-sum.
     - **8.185 *Euandrus***: rēx Eu | an-drŭs ă | it nōn | haec sol | lem-nĭ-ă | nō-bis.
   - **8.129 *Danaum***: Dă-nă-um is three syllables, as at 1.754 and 2.14: nōn ĕ-quĭ | (dem) ex-tĭ-mŭ | ī Dă-nă | um quod | duc-tŏr ĕt | Ar-cas (16). The scanner used synizesis with a long Da-.
   - **Consonantal i after a prefix:**
     - **8.130 *coniunctus***: … rēs gĕ-mĭ | nīs con | iunc-tŭs Ă | trī-dis.
     - **8.145 *obieci***: ob-iē | cī că-pŭt | et sup | plex ad | lī-mĭ-nă | vē-ni (14). The scanner had o-bi-e- with a short ē.
     - **8.164 *coniungere***: … trae con | iun-gĕ-rĕ | dex-tram.
   - **8.135 *Grai perhibent***: Ē-lec | (tra) ut Grā | ī pĕ-rhĭ | bent At | lan-tĭ-dĕ | crē-tus. *Grāī* has two long syllables, as at 3.163. The *per-* of *perhibent* is short, because h makes no position. The scanner had Gră-ĭ and pē-rhī-, which gave the same syllable count but four wrong quantities.
   - ***Laomedontiaden* (seven syllables, as 8.18 and 7.105):**
     - **8.158**: Lā-ŏ-mĕ | dōn-tĭ-ă | dēn Prĭ-ă | mum Să-lă | mī-nă pĕ | ten-tem, five dactyls.
     - **8.162**: Lā-ŏ-mĕ | dōn-tĭ-ă | dēn sed | cunc-tīs | al-tĭ-ŏr | ī-bat.
     
     In both lines the scanner ran Lao- into one syllable and made -me- long.
   - **8.200 *nobis aliquando***: At-tŭ-lĭt | et nō | bīs ă-lĭ | quan(do) op | tan-tĭ-bŭs | ae-tas. The scanner made nŏ-bĭs and ā-lī-.

### Medium
17. **8.194** (COSTLY 2.3), **wrong as flagged**. *sēmihominis* is four syllables, with its i said as a consonant (sēm-yŏ-mĭ-nis). *Cācī* is long-long and *făcĭēs* has three syllables: sēm-yŏ-mĭ | nīs Cā | cī fă-cĭ | ēs quam | dī-ră tĕ | nē-bat. The scanner kept a vowel i, made -mi- long and -ci short, and ran *fa-cies* into two syllables.
18. **Note 121–123 (*ait*), self-contradictory.** The note said Greenough prints *ait* "with no marks or commas around it, his habit… (compare *inquit* at 7.594 and 8.351, where he does give commas)". The examples show the habit is only to leave the verb inside the marks. Elsewhere he sets it off with commas, and here the commas are missing. Rewritten: "Greenough leaves 'ait' inside the speech marks, his habit… ('inquit' at 7.594 and 8.351); there he sets it off with commas, here the print has none." The note also went from 144 to 133 words.
19. **Note 142, a false label.** "with 'ab' set after its adjective" is wrong: in *sanguine ab uno* the preposition stands between the noun and its adjective. Corrected.
20. **Note 169, a false label.** "the antecedent placed inside the relative clause" is wrong: *dextra* is outside *quam petitis*, the subject of *iuncta est*, and it comes last. The note now reads "the relative clause set before its antecedent, which comes last".
21. **Note 131–133, an unsupported claim.** "Helenus and the Tiber both sent him here" was wrong for Helenus, who never sent Aeneas to Evander. The note now reads: "the prophecies that have guided him, last of all the Tiber's, which bade him make the Arcadians his allies (8.55–56)". I checked this against 8.56, *hos castris adhibe socios et foedera iunge*.
22. **`l` and note 147–149, *teneant*.** The `l` line "and the sea which above they hold, and which washes below" made *quod* the object of *teneant*. In fact *teneant* is the second verb of the *quin* clause, with *mare* as its object, and *quod supra* (understand *adluit*) is a relative clause. The `l` now reads "and the sea, the one above, they hold, and the one that washes below". In the note, "'teneant', 'they may hold'" now reads "a second verb of the 'quin' clause, 'and hold'". The `i` was already right.

### Low
23. **Note 102–104**: "'sollemnem… honorem'… framing the line" was wrong, since *Forte die* comes before it. It now reads "split across the line".
24. **Note 102–104**: I cut "Servius (from memory) says the Trojans arrived on the very day of the yearly rite, which the Romans kept in August". The first half only repeats Virgil, and the August date is an attribution I cannot check. This also brought the note from 159 words to 140.
25. **Note 102–104**: the elisions now read *sollemn(em) illo* and *ant(e) urb(em) in*. The *ante urbem* elision had been missed.
26. **Note 107–110**: I cut the Latin Library's *tacitos*. The note itself called it "no real change", and conventions say to note a variant only where the sense changes.
27. **Note 114**: added the elision *Pacemn(e) huc*.
28. **Note 126**: added *reg(em) Aeneas*, with *Aeneas* three syllables.
29. **Note 127–130**: the following edits took the note from 157 words to 140.
    - Cut "(esses)", which was misleading: the verb to supply is *fores*.
    - Cut the unverified "(Allen & Greenough on 'quod' with the subjunctive, from memory)". The rejected-reason label itself is right (R13).
    - Cut "a thought he might have had and did not".
    - Added that *Danaum* has three syllables.
30. **Note 134–136**: added that *Grai* has two syllables and that *Teucros* has *eu* as one. To stay within 140 words I cut "a poetic use" and "the point of the Trojans' homecoming", and shortened the Teucer sentence.
31. **Note 136–139**: rewritten from 197 words to 138, with no change to the misprint call (R5).
    - Cut the Latin Library's *orbis* for *orbes*. It is morphology, and conventions say to ignore it.
    - Cut the muddled remark that "'gelido' takes the adjective into the middle of the phrase".
    - "In this version of the story" became "in Virgil".
32. **Note 140–141**: the elisions now read *Mai(am) auditis* and *id(em) Atlas*. The first had been missed.
33. **Note 155–156**: added the elision *voc(em) Anchisae*.
34. **Note 157–159**: cut "and the commentators know no other source (from memory)", a claim about scholarship I cannot check. "The visit to Arcadia is not in Homer" stays, and it is true. "Line 158 is all dactyls" now reads "runs five dactyls", with *Laomedontiaden* seven syllables.
35. **Note 163–164**: "'iuvenali… amore'… framing the rest of the clause" was wrong. It frames only *ardebat*, and now reads "framing the verb".
36. **Note 165**: Pheneus as "Evander's old home" now reads "where the young Evander then lived". This is what *Phenei sub moenia duxi* implies, and no more.
37. **Note 169–171**: added the elision *Erg(o) et*.
38. **Note 172–174**: added the elision *quand(o) huc*.
39. **Note 175–178**: added the elision *solioqu(e) invitat*, and *Aenean* as three syllables.
40. **Note 179–181**: "Elision 'certatim araeque'" now reads *certat(im) araeque*. Added *tauror(um) onerantque*.
41. **Note 190–192**: added the elision *suspens(am) hanc*.
42. **Note 193–195**: "'vasto… recessu'… ablative of description" was wrong. With *summota* it is an ablative of place.
43. **Note 195–197**: "'tristi… tabo'… framing the line" was wrong. It frames *pendebant pallida*.
44. **Note 201–204**: trimmed from 150 words to 135. I cut the route home through Spain, Gaul and Italy and shortened the Geryon gloss. Added the elision *taurosqu(e) hac*.
45. **Note 205–208**: cut "a reading many editors prefer (from memory)" on *furis*, a claim about scholarship. The variant itself stays, since it changes the sense.
46. **Note 209–211**: added the elisions *atqu(e) hos* and *sax(o) occultabat*.
47. **Note 212**: added the elision *null(a) ad*.
The scansion pointers added in items 28, 29, 30, 34 and 39 (*Aeneas*/*Aenean*, *Danaum*, *Grai*, *Teucros*, *Laomedontiaden*) agree with the hand entries.

Items 23–47 are the 25 pass-1 lows.

## Changes — pass 2
- **P2-1 (low)**: in note 134–136, the cut in item 30 left a comma splice: "…(3.167, 7.206–209), to Evander what matters is Atlas". The comma is now a colon.
- **P2-2 (low)**: in note 126, the new scansion sentence sat between the *dictis… amicis* gloss and the *adfatur* gloss. It now comes after *adfatur*.
- **P2-3 (low)**: in note 201–204, "'descendant of Alceus'" was a misspelling. It now reads Alcaeus.
- **P2-4 (low)**: in note 136–139, "(as at 7.320)" was ambiguous about what was alike. It now reads "(compare 7.320)", which also keeps the note within 140 words.

## Scan-fixes entries added (17)
These are appended after 8.100 in line order, each with its reason:
- **Unflagged, wrong quantities or syllable count (16)**: 8.115, 8.126, 8.129, 8.130, 8.135, 8.136, 8.145, 8.152, 8.158, 8.161, 8.162, 8.164, 8.178, 8.182, 8.185 and 8.200
- **COSTLY, wrong as flagged (1)**: 8.194

Each entry matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 13–17 syllables and one ×, and its `why` gives a syllable count that matches.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *Euandrum* (119) and *Teucrum* (154) are one syllable, which is right. *Teucros* (136, 161) and *Euandrus* (185) are fixed.
- **Initial Ae-**: *aetherios* (137), *aetas* (200) and the *-ae* endings are right as the scanner reads them. Every *Aeneas*/*Aenean* in the part is fixed: 115, 126, 152, 178 and 182.
- **Consonantal i**:
  - Right as read: *coniunxere* (133, co–niun– with both syllables long; the division is cosmetic), *disiectae* (191, di–siec–), *Troiugenas* (117), *Graiugenum* (127), *Troiana* (182), *Troiane* (188), *iuvenum*/*iuvenes*/*iuventus*, *Maia* (138) and *Maiam* (140, elided into *auditis*).
  - Fixed: *coniunctus* (130), *obieci* (145), *coniungere* (164) and *semihominis* (194).
- **Hiatus**: there is none in the part. Every vowel meeting is an ordinary elision or a prodelision, for example *quicumque es* (122), *iuncta est* (169), *ante urbem in* (104), *Maiam auditis* (140) and *saxo occultabat* (211).
- **Other words named in the brief, scanner right**:
  - *Phenei* (165): Phĕ-nĕ-ī
  - *Geryonae* (202): Gē-rў-ŏ-nae, in an all-dactyl line
  - *boum* (217): bŏ-um
  - *mugiit* (218): mū-gĭ-ĭt
  - *Amphytrioniades* (214): scanned as Amphitryoniades, Am-phĭ-trў-ō-nĭ-ă-dēs
- **8.154 (COSTLY 2.1), right**: Tum sīc | pau-că rĕ | fert ut | tē for | tis-sĭ-mĕ | Teu-crum (14).
- **8.167 (COSTLY 2.0), right**: dis-cē | dens chlă-mў | dem(que) au | rō dĕ-dĭt | in-ter | tex-tam, a spondaic line (14). The drafter's note says so.

## Refused findings
- **R1 — 8.113 `tenditis? ”inquit`**: the misprint call is **upheld**. It is the same slip as 7.68 and 5.741, both treated under rule 5b. `t` stays as printed, `l`/`i` close the speech after the question mark, and the note opens with the print's reading. It may be an artefact of the Perseus encoding rather than of the print, but the treatment is the same either way.
- **R2 — 8.124 `excepitque`**, lowercase after `hospes.”`: **upheld** as a misprint. This is consistent with 8.9, 8.79 and 7.290. The general ruling asked in QUESTIONS item 43 is still open.
- **R3 — 8.217 `reddidit`**, lowercase after the stop ending 216: **upheld**, on the same grounds as R2.
- **R4 — 8.214 `Amphytrioniades`**: **upheld** as a clear misprint (y and i transposed). Line 103 prints *Amphitryoniadae*, and the Latin Library has *Amphitryoniades*. The scanner reads the printed letters with the right quantities, so no entry is needed.
- **R5 — 8.137 `orbes` with no stop**: **upheld**, as at 7.320. *vobis* in 138 begins a new sentence, and any modern text has a stop here. This is arguably a rule-5 case (missing punctuation), which would mean correcting the source and re-pinning; that is outside the reviewer's remit. Listed for the owner.
- **R6 — 8.122 `ait` without marks**: **kept as printed, not a misprint**. Leaving a verb of saying inside the speech marks is Greenough's habit: 1.754, 7.594 and 8.351. The missing commas are a rule-5 punctuation case, as 5.474 was (QUESTIONS item 30), and are not applied here. The note now tells the reader to supply them (item 18).
- **R7 — 8.122 *quicumque es***: **no entry**. The scanner's tokens (`qui–3cum–que`, `es⏑`, with *-que* unmarked) are exactly the house notation for prodelision: compare 7.263 `cu⏑6pi–do`, `est×` and 8.169 `iunc–ta`, `4est–`. The quantities are right (… cum-quĕ s'ă | it cō …), and the drafter's note ("scanned with prodelision") is consistent with this.
- **R8 — 8.154 and 8.167 (COSTLY)**: the scanner's fits are **right**, so there are no entries, as the brief says. Both stay in the build's scanner report.
- **R9 — Cosmetic syllable divisions with right quantities**: these get no entries. Examples: *a–dla–bi* (108), *co–niun–xe–re* (133), *di–siec–tae* (191), *su–bla–ta* (175), *Ma–iam* (140) and *A–tlas* (136, 140, 141).
- **R10 — 8.205 *furiis***: kept as Greenough prints it. It is a possible reading (ablative of cause with *effera*), not a clear misprint. The Latin Library's *furis* is noted because it changes the sense.
- **R11 — 8.211 *raptos*** (Latin Library *raptor*): the note on it is right, since this variant also changes the sense. Kept.
- **R12 — 8.130, the Atridae kinship**: "How Evander was kin to them Virgil does not say; the old commentators offered family trees (from memory)" is true and hedged. Kept. From memory, one ancient tree runs through Hippodamia, granddaughter of the Pleiad Sterope. I did not add it, because I cannot check it.
- **R13 — 8.130 *fores***: the subjunctive of a rejected reason is the right label (*non quod*). Kept.
- **R14 — 8.104 *huic***: "dative of reference" was kept. Possession is also possible, but the sense is the same.
- **R15 — 8.104 Pallas "Evander's only son"**: kept. It is supported by 8.581, *mea sera et sola voluptas*.
- **R16 — 8.159, Priam's visit to Arcadia**: "not in Homer" is true and kept. The unverifiable rest was cut (item 34).
- **R17 — Attributions kept, hedged or standard**:
  - Servius on *tanto nomine* (121) and on *viscera* (180)
  - Ennius *accipe daque fidem* (150), which I recall as the start of an Annales line
  - Livy 1.7, Cacus as a shepherd *ferox viribus*
  - Propertius 4.9 and Ovid Fasti 1, the Cacus story
  - the Homeric Hymn to Hermes: the birth on Cyllene (139) and the cattle driven backwards (210)
  - Iliad 6, Glaucus and Diomedes
  - Iliad 7, the long chine for Ajax
  - Iliad 20, Aeneas's genealogy
  - Odyssey 1, Telemachus's questions
  - the Homeric end-of-meal formula
  - *Cacus*/*kakos*
  
  All are right as far as I remember. None could be checked against a text.
- **R18 — The `i` echo check**: I found no distinctive echo of a published version. The `i` lines are plain renderings built on the `l`.
- **R19 — 8.118 "The words overstate"**: kept. It is an interpretation, and it is labelled as one.
- **R20 — `title`, `titleEn`, `part` and `about`**: these are accurate and our own, and were left unchanged. The claim that Dardanus and Mercury are both grandsons of Atlas is right.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: 8.113 `tenditis? ”inquit`, 8.124 `excepitque`, 8.214 `Amphytrioniades` and 8.217 `reddidit`. `t` is as printed, and `l`/`i` carry the corrected reading. The ruling on lowercase after a stop (item 43) is still open.
- **Punctuation that is arguably rule 5** (a source fix plus a re-pin, not a 5b note):
  - 8.137 `orbes`, with no stop before *vobis*. It is treated as a 5b misprint, as at 7.320.
  - 8.122 `ait`, with no commas, as at 5.474. It is kept as printed, and the note tells the reader to supply the commas.
- **8.205 *furiis***: Greenough's reading is kept. *furis* is given in the note.
- **Build report**: COSTLY flags at 8.154 and 8.167 will still show in the report. Both fits were checked by hand and are right, and no entry was made, per the brief.
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
- **Unchecked attributions, from memory**: listed in R17. The Servius date for the rite and the Allen & Greenough pointer were cut, not kept.
