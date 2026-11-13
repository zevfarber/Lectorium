# Review — aeneid-062 (Aeneid VIII.520–607), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 41 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every mythological claim. I also checked the drafter's rule-5b calls (8.556 `vota`, 8.558 `tum`, 8.583 `volneret. ”Haec`, and the unclosed bracket opened at 8.561), the reading of `urbem` at 571, the Latin Library variants, the echo of 1.101 at 539, every "(from memory)" attribution, and the `about`.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.100–101, 1.257, 4.173, 7.560, 8.102, 8.359–368, 8.404, 8.443, 8.479, 8.481–488, 8.506 and 11.875, and the internal pointers 556, 561, 565, 567 and 568. All are right.

**Pass 2** re-read every edited field in full and made one more change (P2-1).

**Scansion.** I hand-scanned all 88 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with my scansion syllable by syllable.
- **The scanner was wrong on 10 lines**: 521, 523, 536 (half-line, UNRESOLVED), 551, 552, 563, 586, 598, 602 and 606.
  - Only 536 was flagged. The other nine were wrong with no flag.
  - Each now has a hand entry.
- **Two carrier lines**: 534 and 535 share unit 5 with the half-line 536. The scanner is right on both (checked by scanning them alone in-process), but without entries the unit would get no `sc`, so both are entered as carrier lines.

Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule:
- full lines: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×
- the half-line 536: feet numbered 1..k with k < 6, one ×, and a reason beginning "Half-line"

Each `why` gives a syllable count, and a script checked that count against its entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 12 entries apply
- **all 41 units get `sc`**. Without the 534–536 entries, unit 5 got none, and the build would refuse.
- all 88 lines pass the validator's metre check
- the scanner report is empty after the fixes

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 41 units, checked by script against a copy of the drafter's file taken before any edit. `title`, `titleEn` and `part` are unchanged. `about` has one change (item 27).
- 17 units changed. `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Note lengths.** None was over 140 words before or after; every note is now 35–138 words.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 131 insertions, 0 deletions, trailing newline kept, formatting as before (`indent=1`, no ASCII escaping). The new keys come after 8.517, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Speech marks.** These were checked in `t`, `l` and `i`. There are two speeches, and each layer has 2 “ and 2 ”:
- **Aeneas, 532–540**: “ on unit 4, ” on unit 9.
- **Evander, 560–583**: “ on unit 20, ” on unit 29. The print's closing mark is joined to *Haec* (rule-5b item R3), so unit 29 also carries *Haec genitor… fundebat*.

**Severity counts: major 10, medium 2, low 25 (24 in pass 1, 1 in pass 2). Refused findings: 16. Scan-fixes entries added: 12 (10 corrections, 2 carrier lines).**

## Changes — pass 1

### Major
1–10. **Scansions the scanner got wrong.** Each line now has a hand entry with its reason.
   - **Initial Ae- split in two**:
     - **8.521 *Aeneas***: Ae-nē | ās An | chī-sĭ-ă | dēs et | fī-dŭs Ă | chā-tēs (14 syllables). The scanner had 15.
     - **8.552 *Aeneae***: dū-cunt | ex-sor | t(em) Ae-nē | ae quem | ful-vă lĕ | ō-nis (13). The scanner had 14.
     - **8.586 *Aeneas***: Ae-nē | ās in | ter prī | mōs et | fī-dŭs Ă | chā-tēs (13). The scanner had 14.
     - **8.606 *Aeneas***: Hūc pă-tĕr | Ae-nē | ās et | bel-lō | lec-tă iŭ | ven-tus (14). The scanner had 15.
   - **Greek eu split — 8.551 *Teucris***: Dan-tŭr ĕ | quī Teu | crīs Tyr | rhē-nă pĕ | ten-tĭ-bŭs | ar-va (15). The scanner split Te-u and had 16.
   - **Synizesis preferred — 8.523 *Cytherea***: nī sig | num cae | lō Cy-thĕ | rē-ă dĕ | dis-sĕt ă | per-tō (15). The scanner made *rea* one syllable and *de-* of *dedisset* long, a fit with 14. The precedent is 1.257.
   - **Wrong quantities with the right syllable count**:
     - **8.563 *regem hac Erulum***: et rē | g(em) hāc Ĕ-rŭ | lum dex | trā sub | Tar-tă-ră | mī-sī (14). The scanner made *rē-* and *hāc* short and *E-*, *-ru-* long. With *rē-* and *hāc* long by nature, the only dactyl available in the first four feet is *hāc Ĕ-rŭ*.
     - **8.598 *religione… late sacer***: rē-lĭ-gĭ | ō-nĕ pă | trum lā | tē să-cĕr | un-dĭ-quĕ | col-lēs (16). The scanner made *late* two shorts and *sa-* long.
     - **8.602 *finis aliquando***: quī prī | mī fī | nīs ă-lĭ | quand(o) hă-bŭ | ē-rĕ Lă | tī-nōs (15). The scanner made *fi-nis* two shorts and *a-li* two longs.
   - **Half-line — 8.536 *laturam auxilio.*** (UNRESOLVED): lā-tū | r(am) au-xĭ-lĭ | ō (– – | – ⏑ ⏑ | ×), 6 syllables. It is entered as at 7.760, 8.41 and 8.469, with a reason beginning "Half-line".
     - Without this entry, and the carrier entries for 534 and 535, unit 5 gets no `sc` and the build refuses.

### Medium
11. **Unit 23 (566–567) and unit 20 (560–563), the bracket opened at 561: downgraded from "misprint, corrected" to "kept as printed, doubtful".**
    - The print opens `(qualis eram` at 561 and never closes it. The bracket in 565 is a separate, closed pair.
    - The drafter called it a misprint for `armis):` at 567. That is the likeliest place, since the main sentence resumes at *non ego* (568). But it is not the only possible reading:
      - the print's comma after *eram* allows a close there, with the *cum*-clause then hanging on *annos* ("the years when…");
      - or the opening bracket itself may be the stray.
    - So rule 5b's "only one way to read" is not met. The note in unit 23 now opens with the print's reading, says "Kept as printed, doubtful", gives the three possibilities, says the sense is the same, and says `l` and `i` close the bracket after *armis* as the likeliest place. The unit 20 note now says the print "opens a bracket here and never closes it (see 567)", replacing "the clause it encloses runs to 567".
12. **Note 548–550, a false label.** It called *nuntia ventura* "neuter plural agreeing loosely with 'pars'". Both words are feminine singular agreeing with *pars* directly: "the remaining part… (being) about to come as bearer of the news". The note now says so. `l` changes from "as messengers to come" to "as bearer of news to come".

### Low
13. **Unit 0 (520–523)**:
    - **`l`**: "and fixed their faces they kept" read *defixi* as agreeing with *ora*. It now reads "and, fixed, their faces they kept".
    - **Note**: "'they kept their faces fixed'… the participle predicative" now reads "'fixed, they held their faces', kept them downcast: 'defixi' is nominative plural, agreeing with the two men, not with 'ora'".
    - **Note**: "'caelo… aperto'… framing the line" was wrong, since *caelo* is the line's third word. It now reads "enclosing 'Cytherea dedisset'".
    - **Note**: it added "'Aeneas', three syllables, Ae-nē-ās" and "'Cytherea' (four syllables, Cy-the-rē-a)", which agree with the 521 and 523 entries.
14. **Note 532–533**: "'Olympo' ablative (or dative) of the source of the summons" used a non-standard label. It now reads "'by Olympus', dative of the agent with a passive, a poetic use (it can also be taken as ablative)".
15. **`l` 541**: "from the seat he raises himself high" made *alto* an adverb with the verb. It now reads "from the seat he raises himself, the lofty one".
16. **`i` and note 543**: `i` had "the household god *he* had worshipped the day before" (Aeneas), and the note had "the household god *Evander* honoured the day before". Neither is stated by *hesternum larem*. Both now read "the household god honoured the day before".
17. **`l` 544**: "chosen in the custom" now reads "chosen by custom".
18. **Note 544–545**: "'Euandrus'… three syllables, E-van-drus" implied a consonantal *v*. It now reads "three syllables, Eu-an-drus, the Greek 'eu' one long syllable", which agrees with the scanner's correct fit of 545.
19. **Note 552–553**: it added "'Aeneae'… three syllables, Ae-nē-ae", which agrees with the 552 entry.
20. **Note 560–563**: it added "(Ĕ-rŭ-lus)", which agrees with the 563 entry.
21. **`l` 569**: "nor on *his* neighbouring" added a possessive. It now reads "nor upon neighbouring… / this head insulting".
22. **Note 568–571, *urbem***: "some take it as Mezentius's own city" was an unchecked, unhedged attribution. It now reads "it could also be Mezentius's own Agylla, which his cruelty emptied (8.481–488)". The drafter's primary reading, Pallanteum, stands (R4).
23. **Note 580–584**: "'volneret', Greenough's 'vulneret'" reversed the relation. It now reads "Greenough's spelling of 'vulneret'".
24. **Note 585–588**: it added "'Aeneas' (586) is three syllables, Ae-nē-ās", which agrees with the 586 entry.
25. **Unit 32 (589–591)**:
    - **`l` 591**: "and the darkness dissolved" could be read with *darkness* as subject. It now reads "and has dissolved the darkness".
    - **`i`**: a precautionary rephrase of the Lucifer simile. "the star Venus loves above all the other fires of heaven lifts his holy face into the sky and scatters the darkness" now reads "like Lucifer, the Morning Star, when he comes up dripping from the waves of Ocean, the one of all heaven's fires that Venus prizes most, and raises his hallowed face to the sky and melts the dark away". *Melts* now matches `l`'s "dissolved" for *resolvit*.
26. **Note 592–593, a missing elision.** *nub(em) et* (593) is added.
27. **Unit 35 (595–596)**:
    - **`i`**: a precautionary rephrase of 596. "the gallop of hooves hammers the loose, dry earth" now reads "and hoof after hoof, in a galloping beat, shakes the powdery plain".
    - **Note**: "at 11.875 (from memory)" was checked against the source and is right. The hedge is replaced by the line itself, *quadrupedumque putrem cursu quatit ungula campum*. The Ennius attribution stays hedged.
28. **Unit 36 (597–598)**:
    - **`i`**: "by the religion of our forefathers" drew the narrator into *patrum*. It now reads "by the piety of men of old".
    - **Note**: it added "'re-' is long in verse, as if 'rel-ligione'", which agrees with the 598 entry.
29. **Note 606–607**: it added "(Ae-nē-ās, three syllables)", which agrees with the 606 entry.
30. **`about`**: "an ancient grove… where Tarchon and the Etruscans are camped" now reads "near which", since the camp is *haud procul hinc* (603).

Items 13–30 make 18 numbered low items, several with more than one change. Counted change by change, there are 24 pass-1 lows: item 13 counts 4, items 25, 27 and 28 count 2 each, and every other item counts 1.

## Changes — pass 2
- **P2-1 (low), `i` 571**: "robbed this city" committed the English to Pallanteum, against the note's open reading of *urbem* (item 22). It now reads "robbed the city".

## Scan-fixes entries added (12)
These are appended after 8.517 in line order:
- **Initial Ae- (4)**: 8.521, 8.552, 8.586 and 8.606
- **Greek eu (1)**: 8.551
- **Synizesis preferred (1)**: 8.523
- **Wrong quantities, same count (3)**: 8.563, 8.598 and 8.602
- **Half-line (1)**: 8.536 (UNRESOLVED)
- **Carrier lines (2)**: 8.534 and 8.535. The scanner is right on both; they are needed only because they share unit 5 with 536.

Each entry matches its line's words under `WORD_RE`. Each full line has six feet, five –⏑⏑/–– feet then –×/⏑×, 13–16 syllables and one ×. The half-line has feet 1–3 and one ×, with a reason beginning "Half-line".

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *Euandrus* (545) is right: Eu-ān | drūs pă-rĭ | tēr pă-rĭ | tēr Trō | iā-nă iŭ | ven-tus. *Heu* (537) is right. *Teucris* (551) is fixed.
- **Initial Ae-**: *aethere* (524), *aethera* (526), *aere* (593) are right. Fixed: 521, 552, 586 and 606.
- **Synizesis**: *aureis* (553) is right as *au-reis*, two syllables. *cui* (564, 566) is right as one syllable. *abiete* (599) is right as three syllables, *ab-ie-te* with consonantal *i*: īn-clū | sē-rĕ că | v(i) et nī | grā nĕ-mŭs | ab-yĕ-tĕ | cin-gunt. *Cytherea* (523) is fixed.
- **Consonantal i**: *maior* (557, mai-ior), *Troiana* (545) and *Troiae* (587) are right. There is no consonantal *i* after a prefix in this part.
- **Hiatus**: none. *O* is not elided at 560, 572 and 579, as always.
- **Cosmetic division**: at 579 the scanner divides *a–brum-pe-re* (prefix *ab-*). The quantities are right, as with *co–niunx* (QUESTIONS item 37).
- **Other quantities checked**: *Anchīsiădēs* (521), *inprōvīsō* (524), *Hercŭlĕīs* (542), *Fērōnia* (564), *dictū* (565), *Thȳbri* long by position before *br* (540), *săcrum* and *săcrasse* lengthened before *cr* (591, 600), *chlămy̆de* (588), *Ōcĕăni* (589), *Lūcĭfĕr* (589), *pulvĕrĕam* (593), *ungula* three syllables (596).

## Refused findings
- **R1 — 8.556 `vota`**: **upheld** as a rule-5b misprint for *Vota* (lowercase after the stop ending 555). This is consistent with 8.9, 8.79, 8.285, 8.310, 8.366, 8.489, 8.496, 8.510 and 8.514. The general ruling asked in QUESTIONS item 43 is still open.
- **R2 — 8.558 `tum`**: **upheld** as a misprint for *Tum*, on the same grounds.
- **R3 — 8.583 `volneret. ”Haec`**: **upheld**. `t` stays as printed, `l`/`i` close Evander's speech after *volneret*, and the note opens with the print's reading. The mark cannot be split from *Haec*, so unit 29 carries *Haec genitor… fundebat*. This follows 7.560, 8.404 and 8.443.
- **R4 — 8.571 *urbem***: the drafter's primary reading, Pallanteum, is kept. *finitimo huic capiti* makes Evander's own town the natural object. The alternative is now stated without an unchecked attribution (item 22).
- **R5 — 8.588 Latin Library `it` for `in`**: the note is kept. The variant can only be the first *in* (*it medio*), since *conspectus it armis* makes no sense. It supplies a verb but leaves the picture the same, and the note says "most likely".
- **R6 — 8.539, the echo of 1.101**: verified against the source. 1.101 reads *scuta virum galeasque et fortia corpora volvit*, the same line with *volvit* for *volves*. In 1.100 the Simois is the river. The note is right.
- **R7 — Other Latin Library variants**: 528 *caeli in regione* (LL adds *in*), 579 and 581 (word order) and 594/596 (spelling) do not change the sense and are not noted. The drafter's brief mention of the order at 579 is harmless and is kept. 544 *mactat* and 555 *limina* are noted, which is defensible.
- **R8 — Attributions kept, hedged "from memory" and unchecked against a text**:
  - Iliad 21 (Achilles choking the Scamander)
  - Iliad 7 and 11 (Nestor wishing for his youth)
  - Iliad 22 and 5 (Achilles' spear as the evening star; Diomedes' armour like the star bathed in Ocean)
  - Ennius (the hoof line)

  All are right as far as I remember. None was cut.
- **R9 — Unhedged background claims, kept as standard**: Venus coming ashore at Cythera (Hesiod); Feronia's groves at Soracte and Tarracina; the Etruscan trumpet; the Pelasgians in Italy; *Praeneste* feminine here.
- **R10 — Note 527–529, "the cloud that carries the gods' gifts"**: kept. It is an interpretation, but a harmless one.
- **R11 — Note 534–536, *si… ingrueret* "subjunctive in reported speech"**: kept. It is true (indirect discourse after *cecinit*).
- **R12 — Note 532–533, *ne… quaere* as a poetic prohibition**: kept. A&G list *ne* with the imperative as poetic.
- **R13 — `i` 560, "the years that are gone"**: kept. It is literal and not distinctive.
- **R14 — `i` 532–540**: I found no distinctive echo of a published version in Aeneas's speech. The two set lines, 596 and 589–591, were rephrased as a precaution (items 25 and 27).
- **R15 — `title`, `titleEn` and `part`**: accurate and our own, and left unchanged.
- **R16 — Note 556–557, *periclo* dative with *propius***: kept. It is the usual construction.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading.
  - 8.556 `vota` and 8.558 `tum`, lowercase after a stop. **The ruling in item 43 is still open.**
  - 8.583 `volneret. ”Haec`, closing mark joined to the next word, as 8.404 and 8.443.
- **Kept as printed, doubtful**: 8.561 `(qualis eram` opens a bracket that is never closed.
  - The likeliest close is after *armis* at 567, but after *eram* at 561 is also possible, or the opening bracket may be the stray.
  - `l`/`i` close it at 567, and the note says so.
  - If the owner rules it a clear misprint, only the note's opening needs to change.
- **Doubtful quantities on the chosen fit**: 8.563 *Ĕrŭlum*, both short, forced by the metre (the name occurs only here); 8.598 *rēligione*, long by the usual verse licence.
- **Build report**: it should be empty, since all 12 entries apply.
- **Unchecked attributions** are as listed in R8.
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
