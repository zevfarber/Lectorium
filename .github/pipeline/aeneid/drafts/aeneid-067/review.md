# Review — aeneid-067 (Aeneid IX.314–445), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 61 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked the drafter's five rule-5b calls (9.353 `Nisus. sensit`, 9.377 `iter? ”Nihil`, 9.392 `silvae? ”Simul`, 9.423 `amborum, ”inquit`, 9.427 `Me me` with no opening mark), the decision to keep 9.355 `“Absistamus, ait, nam` and the bracketed 9.363, the no-advisory decision, the Latin Library variants, the `about`, the title and part names. I read every `i` for echoes of the well-known English versions, most closely 9.390, 9.427–430, 9.433–437 and 9.444–445.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington, Servius). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.267–271, 2.317, 3.80, 6.844, 7.68, 7.691, 8.113, 9.59–64, 9.159–161, 9.234, 9.236–237, 9.291, 9.312–313, 9.446–449 and 10.495–500, plus the in-part references (323, 327, 333, 363, 374, 378, 400, 403, 414). All say what the notes say. One claim about the poem as a whole was false (item 6): Euryalus is not the poem's first young man undone by spoils, because Coroebus dies in captured Greek arms at 2.386–412.

**Pass 2** re-read every edited field in full and made three more changes (P2-1 to P2-3).

**Scansion.** I hand-scanned all 132 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with mine syllable by syllable.
- **The scanner was wrong on 2 lines**, 340 and 384. Neither was flagged. Both have the right syllable count with wrong quantities. Each now has a hand entry.
- **The one flagged line, 390 (COSTLY 2.1), is right**: Eu-rў-ă | l(e) in-fē | līx quā | tē rĕ-gĭ | ō-nĕ rĕ | lī-quī (14 syllables), with *Eu-* one syllable. It gets no entry, as 9.281 in aeneid-066. The drafter's note says it "needs one"; refused (R9).
- **No half-lines, no hiatus and no Greek initial *Ae-*** in this stretch.

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- both entries apply
- **all 61 units get `sc`**
- all 132 lines pass the validator's metre check
- after the fixes, the scanner report holds only COSTLY 390, which is hand-checked right and does not block the build.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump` (`indent=1`, `ensure_ascii=False`, no trailing newline, as the drafter's file).
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 61 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- **23 units changed.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks.**
  - `t` has 6 “ and 7 ”, because the print has no “ at 427. The validator will warn about this, as it did for 9.146 in aeneid-065.
  - `l` and `i` have 8 “ and 8 ” each, on the same units: speeches open at 320, 355, 375, 390, 404, 422 and 427 and close at 321–323, 355–356, 375–377, 391–392, 409, 422–423 and 428–430.
  - 355 has two “ in `l`/`i` because "he says" is set outside the marks.
- **Note lengths.** Every note is now 34–135 words. Unit 360–364 was 193 words, over the validator's 140, and was cut to 135 (item 6).
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 21 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.310, in line order.
- The build and the validator were not run (`build_aeneid.py` has no dry-run mode). Their scansion steps were replicated instead.
- **`drafts/aeneid-067/` has no `gloss.json`.** The build needs one. That belongs to the glosser's step, not this review.

**Severity counts: major 2, medium 12, low 21 (18 in pass 1, 3 in pass 2). Refused or upheld-without-change findings: 24. Scan-fixes entries added: 2 (9.340, 9.384).**

## Changes — pass 1

### Major
1. **9.340, wrong quantities (unflagged).** *vēsāna* has a long first and second syllable (*vē-* + *sānus*), and *fămēs* a short first syllable. The scanner had *vĕ-să-nā fā-mēs*, the right count with the wrong feet. The line is now suā-dĕt ĕ | nĭm vē | sā-nă fă | mēs man | dit-quĕ tră | hit-que (15 syllables), with the caesura after *fames*. *suādet* is two syllables, as the scanner also reads it.
2. **9.384, wrong quantities (unflagged).** *rāmōrum* has a long ā and the long ō of the genitive plural, and *ŏnĕrōsa* is short-short-long. The scanner had *ră-mŏ* and *ō-nē*. The line is now Eu-rў-ă | lum tĕ-nĕ | brae rā | mō-r(um) ŏ-nĕ | rō-să-quĕ | prae-da (16 syllables).

### Medium
3. **Note 9.316–319, a wrong construction.** The note said *vident* takes plain accusatives *corpora, currus, viros* and then the accusative and infinitive *arma iacere, vina*. But *viros* has no verb unless *iacere* serves it too: "men among the reins and wheels" needs "lying", and the drafter's own `i` says "men lying". The note now says *iacere* serves *viros*, *arma* and *vina* alike.
4. **Note 9.333, a false agreement.** "*tepefacta*… agrees with both subjects" is wrong: *tepefacta* is feminine singular, and *tori* is masculine plural. It now says the participle agrees with the nearer subject, *terra*, and goes in sense with both.
5. **Note 9.359, a wrong label.** "*bullis* ablative of description" is wrong. An ablative of description needs an adjective with it and describes a noun. *aurea bullis* is "golden in its studs": an ablative of respect (or of means). The note now says so.
6. **Note 9.360–364, a false claim and an overlong note.**
   - "Euryalus is the first of the poem's young men undone by spoils" is false. Coroebus puts on Androgeos's Greek arms and dies because of them (2.386–412). The claim is cut. The Turnus–Pallas parallel is kept: "as the belt Turnus strips from Pallas (10.495–500) will kill Turnus".
   - The note was 193 words, over the validator's 140. It is now 135. The cuts were Tibur's position, "summing up the whole description", "a history told in passing" and the bracket explanation, shortened.
7. **Note 9.329–331, a miscount.** "*premit*… with all four objects" was wrong: there are three (*famulos*, *armigerum*, *aurigam*). It now names them.
8. **Note 9.422–423, a wrong label.** "*amborum*… the genitive of the charge" is wrong. That genitive goes with judicial verbs (accuse, condemn). Here *amborum* depends on *poenas*, "the penalty for both". It now says so.
9. **Note 9.427–428, a wrong construction.** "*Me me*, accusatives, the object of *convertite*" is wrong: the object of *convertite* is *ferrum*, and *me* stands in *in me*. *Me me* hangs without a verb (anacoluthon), and *in me convertite ferrum* takes it up. The note now says so.
10. **`i` 9.427–428, a remembered echo.** "Me, me! Here I am, I did it, turn your swords on me, Rutulians!" is close to a well-known modern version. It now reads "Me, it is me! Here I stand, the man who did it: turn your blades against me, men of the Rutuli! All of the trickery was mine;". *convertite ferrum* still has to be "turn… against me"; the rest is rebuilt.
11. **`i` 9.428–430, a remembered echo.** "his only fault was to love his unlucky friend too well" and "the stars that saw it all" echo the familiar versions (and Dryden's "too much love to his unhappy friend"). It now reads "he dared nothing and had the power to do nothing — this sky and the stars that know the truth are my witnesses — his only offence was to love his ill-starred friend beyond measure."
12. **`i` 9.433–434, a remembered echo.** "Euryalus rolled over in death; blood ran over his lovely limbs, and his neck gave way…" is too close to a known version. It now reads "Down went Euryalus, rolling in death; blood streamed over his handsome limbs, and his neck, its strength gone, sank back upon his shoulders:". It keeps "rolling", which the note ties to *Volvitur* at 414, and has "shoulders" for *umeros*.
13. **`i` 9.435–437, a remembered echo.** In the flower simile, "cut through by the plough, droops as it dies, or poppies bow their heads on tired stems" follows the shape and words of the familiar versions. It now reads "as a red flower, sheared off at the root by the plough, wilts away in dying, or as poppies, their stems grown weary, let their heads sink when a chance shower weighs them down." *forte* is now "chance", and *succisus* is "cut from below".
14. **`i` 9.444–445, a remembered echo.** "and there at last found rest in a quiet death" is very close to a known closing cadence. It now reads "Then, his body pierced again and again, he threw himself on his lifeless friend, and there at last a calm death brought him rest."

### Low
15. **Note 9.316–319**: "resting on their raised poles" contradicted itself; a raised pole is not something a chariot rests on. It now reads "tipped back with their poles in the air once the horses are unyoked". *litore* "the bank of the river" is now "probably the river-bank" (shore or bank cannot be settled).
16. **`i` 9.321–322**: "look out all around" did not render *longe*. It now reads "look out far afield".
17. **Note 9.332–333**: "the long word fills most of the line" was false: *singultantem* is four syllables of a 15-syllable line. It now reads "the two words take up the first half of the line".
18. **Note 9.334–337**: *premit* was glossed "he falls on" here and "overpowers" at 329. It is now "overpowers" in both places.
19. **Note 9.334–337**: "the god is Bacchus, named for his gift" put it backwards: the god's name stands for the gift. It now reads "his name standing for his gift".
20. **Note 9.339–341**: "A lion simile, set before what it illustrates" was wrong. The simile follows Nisus's killings, and the drafter's own next note says "Nisus has been the lion". It now reads "closing Nisus's killings; the next words turn it on Euryalus".
21. **Note 9.339–341**: "'Impastus… leo'… framing the line" was false; *leo* stands mid-line. It now reads "the adjective first and emphatic, the noun held back".
22. **Note 9.339–341**: added the quantities (vē-sā-na, fă-mēs), which agree with the 9.340 entry.
23. **Note 9.342–346**: "a line of nothing but names" was false, because 344 has *subit*. It now reads "fill the line round its one verb".
24. **`i` 9.347–348**: "As he rose, Euryalus closed with him" read as if Euryalus were rising. *adsurgenti* is Rhoetus. It now reads "As Rhoetus rose".
25. **Note 9.384–385**: added the quantities (rā-mō-rum, ŏ-nĕ-rō-sa), which agree with the 9.384 entry.
26. **`i` 9.390**: "Poor Euryalus, where have I left you behind?" leaned on a familiar wording. It now reads "Euryalus, my ill-starred friend, where was it I left you?". "ill-starred" matches the note's gloss of *infelix*.
27. **Note 9.395–398**: added that *pervenit* is present (pervĕnit, as the metre shows: pervēnit would not scan), like *videt*.
28. **Note 9.395–398**: "the wood and the dark he had trusted (378)" now reads "they had trusted". At 378 the subject is *illi*, both men.
29. **Note 9.400–401**: "'pulchram… mortem'… framing the clause" was wrong: the two words frame *properet per volnera*, not *inferat et*. It now says so.
30. **Note 9.416–417**: "'circumspiciunt'… fills most of the half-line" was wrong, because 416 is a full line. It now reads "fills the line up to the main pause in the fourth foot" (see P2-2).
31. **`i` 9.438–439**: "and would be held by none but Volcens" read oddly for *in solo Volcente moratur*. It now reads "and had no thought for anyone but Volcens".
32. **Note 9.444–445**: "'super exanimum… amicum'… framing the line" was wrong, because *Tum* opens the line. It now reads "framing 'sese proiecit'".

## Changes — pass 2
- **P2-1 (low), `l` 9.348**: "he buried as he rose" had the same ambiguity as item 24. It now reads "he buried, (him) rising", word for word with *adsurgenti*.
- **P2-2 (low), note 9.416**: item 30 left "'circumspiciunt'… fills the line up to the main pause", but the line opens with *Diversi*. It now reads "with 'Diversi' fills the line up to the main pause in the fourth foot".
- **P2-3 (low), note 9.334–337**: "'luserat', 'had played', at dice" stated an inference as fact. It now reads "probably at dice".

Pass 2 also re-checked:
- **Every "framing" claim in the part**, against the line as printed. After items 21, 29 and 32, all are right.
- **Every elision list against the scanner's elisions**, line by line. All 61 notes were already right, including the cross-unit elisions *singultant(em) atro*, *eriper(e) An* and *ambor(um) inquit*.

## Scan-fixes entries added (2)
These are appended after 9.310 in line order:
- **9.340**: *vēsāna fămēs*, wrong quantities with the right count (15 syllables)
- **9.384**: *rāmōrum ŏnĕrōsa*, wrong quantities with the right count (16 syllables)

Each entry matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, and one ×. Each `why` states the count, and the script checked it.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek *eu*, one long syllable, right everywhere else**:
  - 320 *Euryal(e) audendum*
  - 342 *Euryali*
  - 359 *Euryalus*
  - 373 *gale(a) Euryalum*
  - 390 (flagged, see above)
  - 396 *videt Euryalum*: per-vĕ-nĭt | ac vĭ-dĕt | Eu-ry-ă | lum quem | iam mă-nŭs | om-nis
  - 424 *in Euryalum*
  - 433 *Volvitur Euryalus*
  - In 384 it is also right; that line's error is elsewhere.
- **Consonantal i after a prefix.** The scanner's count and quantities are right in all of these:
  - 379 *obiciunt*: ŏb-(j)ĭ-cĭ-unt, four syllables. The scanner divides it O-bi-ci-unt, the same quantities, –⏑⏑–.
  - 410 *conixus*: cō-nī-xus.
  - 411 *conicit*: three syllables, long-short-short.
  - 419 *traiecto*: trā-iec-tō.
  - 444 *proiecit*: prō-iē-cit.

  The syllable division is display only. That is the same open question as QUESTIONS item 37/38 (*obicit* at 6.421), so there are no entries.
- **Other consonantal i and u**: *iacere* (318), *iacentis* (329), *iuxta* (329), *iuvenem* (335, 399), *iacebat* (336), *iungeret* (361), *Iamque* (351, 371), *iam* (386, 396), *suadet* (340, two syllables) and *sanguine*/*singultantem* (*gu* before a vowel) are all right.
- ***Ae-*/*ae-***: only Latin *ae* (*aequasset* 338, *Caedicus* 362, *praemissi* 367), all right. There is no Greek *Ae-* in this part.
- **Hiatus**: none. **Half-lines**: none.
- **Quantities checked and right**:
  - *exitio* (316); *lītore* and *lōra* (317–318); *Hyrtacĭdēs* (319); *tăpētibus* and *Rhamnētem* (325); *īdem* (327); *aurīga* (330); *ātro* (333); *tŏri* (334); *lūserat* and *făciē* (336); *lūdum* (338)
  - *ŏvīlia* and *leō* (339); *mūtum* and *metū* (341); *ignārōs* (345); *crātēra* (346); *multā morte* (348); *cŭpīdine* and *nimiā* (354); *crātēras*, *tapētas* (358); *phălĕrās* (359); *Tīburtī* and *dītissimus* (360)
  - *nēquīquam* and *umerīs* (364); *ĕquĭtēs* (367); *flectentīs* (372); *sublustrī* (373); *Nĭhĭl* (377); *fīdere* (378); *īlice* (381); *imprūdens* (386); *infēlix*, *quā* and *relīquī* (390); *vestīgia* (392); *strepitūs* (394); *pervĕnit* (396)
  - *hastīle* (402); *Lātōnia* (405); *ăris* (406); *ibīque* (412); *īlia* (415); *ācrior* (416); *lībrābat* (417); *Tăgō* (418); *ătrōx* (420); *ēnsis* and *vīribus* (431); *trāns-ă-bĭ-it* (432); *succīsus* (435); *papāvera* (436); *dēmīsēre* and *pluviā* (437); *sētius* (441); *placidā* and *quĭēvit* (445)

## Refused or upheld findings
- **R1 — 9.353 `Nisus. sensit`**: **upheld** as a rule-5b misprint (stop for comma, lower-case *sensit*), as at 6.472, 7.290 and 8.9. *cum talia Nisus* needs *ait* (355), and 354 is a parenthesis. The general ruling on lower-case after a stop (QUESTIONS item 43) is still open; a full stop misprinted for a comma reads the same either way.
- **R2 — 9.377 `iter? ”Nihil`**: **upheld**, as 7.68 and 8.113 (both checked in the source). The unit rightly runs on to *nocti.*
- **R3 — 9.392 `silvae? ”Simul`**: **upheld** on the same grounds. The unit runs on to *errat.*
- **R4 — 9.423 `amborum, ”inquit`**: **upheld**, as 7.68 and 9.52.
- **R5 — 9.427 `Me me`, no opening mark**: **upheld** in substance. Greenough closes the speech at 430, so it must open here. This is the same case as 3.315 (QUESTIONS item 20), which was handled the same way. As there, it could instead be a rule-5 source correction (add “ to 9.427 and re-pin aeneid-067), but the printed page could not be checked.
- **R6 — 9.355 `“Absistamus, ait, nam`**: **upheld as kept**. It is Greenough's habit (*ait*/*inquit* inside one pair of marks, set off by commas, as 8.351, 8.362 and 8.439), not a misprint. `l`/`i` set English marks round "he says".
- **R7 — 9.363 bracketed**: **upheld**. It is kept in [ ] in `t`, `l` and `i`, and the note says so. The note states both readings (Rhamnes the grandson without it; the belt won by war with it).
- **R8 — No advisory**: **upheld**. The killings are each a line or two of Homeric idiom: the beheading at 332–333, blood and wine at 349–350, the spear through the brain at 418–419. The conventions say "ordinary killing earns nothing" for the battle books, and "graphic detail rarely". 061 (Mezentius) got none. 063's advisory rested on sexual violence. The drafter's drop-in text is sound if the owner wants a different line for IX–XII.
- **R9 — The drafter's "390 needs one"**: **refused**. The scanner's fit is right; COSTLY is a cost flag, not an error.
- **R10 — *obiciunt*, *conicit*, *proiecit***: no entries (see the hand-scan notes).
- **R11 — Note 9.400, *moriturus* "meaning to die… future participle of purpose"**: kept. The poets use the future participle for purpose (A&G), and "bound to die" would also fit; the note is defensible.
- **R12 — Note 9.346, *magnum* adverbial**: kept. The note gives the other construction (with *cratera*), and `i` avoids "great".
- **R13 — Note 9.350–351, *hic* = Euryalus, *tendebat* still Euryalus**: kept. This is the usual reading, and the note does not overstate it.
- **R14 — Note 9.362, *ille* = Remulus**: kept. This is the natural reading, since *dat* has Remulus as the giver to his own grandson.
- **R15 — Note 9.371, *castris* the Rutulian camp, *muros* the Trojan walls**: kept, a defensible reading.
- **R16 — `i` 9.375 "The sight was not lost on them"**: kept. I know no version that uses it here.
- **R17 — Note 9.342, "'est' is left out"**: kept. *erat* or *fuit* would be more exact in narrative, but the historic presents around it make *est* harmless.
- **R18 — Note 9.329, *Tris… iacentis* framing the line**: kept. It is true: first and last words.
- **R19 — Latin Library variants**:
  - 380 *aditum*, 402–403 *torquet… et* and 432 *transadigit* change the sense and are noted.
  - 331, 370 and 406–407 are orthographic, mentioned once as a reader's aid, which is harmless.
  - 383, 401 and 421 are rightly ignored.
- **R20 — Attributions from memory, all kept; I can stand behind each**:
  - Iliad 10.471–475 (the Thracians' arms in order, a pair of horses by each man)
  - Iliad 10.494–497 (Rhesus breathing hard, the evil dream over his head)
  - Iliad 10.485–486 (Diomedes like a lion on unguarded goats or sheep)
  - Iliad 10 (Odysseus drags the dead aside and drives off the horses)
  - Iliad 2.858–859 (Ennomus the augur)
  - Iliad 1.39–41 (Chryses: "if ever I roofed a temple")
  - Iliad 6 (Glaucus and Diomedes)
  - Iliad 8.306–308 (Gorgythion and the poppy)
  - Catullus 11.22–24 (the flower at the meadow's edge, touched by the passing plough)
- **R21 — Note 9.353–354, "many editors set it in brackets"**: kept. It is unspecific, and true of the familiar texts.
- **R22 — Note 9.316, "Nisus's report (9.236–237)"**: kept. It is checked, and also true of 9.189.
- **R23 — `about`, `title`, `titleEn`, `part`**: unchanged. The `about` agrees with the text throughout. `part` and `titleEn` carry IX.314–445.
- **R24 — `i` elsewhere** (320, 337, 355–356, 365–366, 381–383, 410–413, 424–426, 431–432): read for echoes. None is distinctive enough to change.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading:
  - 9.353 `Nisus. sensit`: stop for comma, lower-case after a stop. The item-43 ruling is still open.
  - 9.377 `iter? ”Nihil`, 9.392 `silvae? ”Simul` and 9.423 `amborum, ”inquit`: closing marks joined to the next word.
  - 9.427 `Me me` with no opening mark: as 3.315. It could instead be a rule-5 source correction (add “ and re-pin aeneid-067). With the print as it stands, the validator warns: `t` 6 “ / 7 ”.
- **Kept as printed**: 9.355 `ait` inside the marks (Greenough's habit); 9.363 bracketed, kept in [ ].
- **Advisory**: none. Upheld; see R8. The owner may want to set the line for Books IX–XII once.
- **Scansion**: the build report should list only COSTLY 390, which is hand-checked right. There are 2 entries: 9.340 (*vēsāna fămēs*) and 9.384 (*rāmōrum ŏnĕrōsa*).
- **Unchecked attributions, all from memory**: Iliad 10 (several places), 2.858–859, 1.39–41, 6, 8.306–308; Catullus 11.22–24; "many editors bracket 354"; Serranus as a surname of the Atilii.
- **Stale files**:
  - `make_units.py` still holds the drafter's strings, so re-running it would discard this review.
  - `drafts/aeneid-067/` has no `gloss.json` yet, and the build needs one.
