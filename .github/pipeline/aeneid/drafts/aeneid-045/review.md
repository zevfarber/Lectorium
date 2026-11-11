# Review — aeneid-045 (Aeneid VI.509–607), adversarial reviewer

I reviewed this part in two passes. In pass 1, I checked each of the 50 units word by word: `l`, `i` and `n` against the Latin, every grammatical label, every citation and mythological claim, the speech marks, the misprint question (README rule 5b), and every `i` for remembered English. The drafter's unverified citations got the closest check, and so did the lines the brief flagged (539, 546, 562, 601–603). Pass 2 re-read every edited unit in full and made one further fix (P2-1).

I then hand-scanned all 99 lines by quantities and compared each with the scanner's output. The scanner was run in-process, the way `build_aeneid.py` calls `SL.scan_story`. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and of the validator's six-foot rule (feet 1–6, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×). With the 18 new entries applied, all 99 lines pass. The packet's COSTLY flag at 544 and its UNRESOLVED flag at 602 are both covered by entries, so the build will drop them from its report.

`t` is untouched. The cut tuples in `make_units.py` are unchanged. The regenerated `units.json` has the same `t`, `ln`, `p` and `v` in all 50 units (checked by script against a copy taken before any edit). `title`, `titleEn`, `part` and `about` are unchanged. Edits were made to the strings in `make_units.py` by a Python replace script, with each old string asserted to occur once, and `units.json` was regenerated with `make_units.py`. `build_aeneid.py` was not run.

**Speech marks**: `t`, `l` and `i` each have 5 “ and 4 ”. The extra “ belongs to the Sibyl's speech that opens at 562 and runs on into the next part. The validator will print a warning for it, and the warning is expected.
- Deiphobus: 509 → 534.
- The Sibyl: 539 → 543.
- Deiphobus: 544 → 546.
- Aeneas: 560 → 561.
- The Sibyl: opens at 562 and is still open at 607. The last note says that her account continues.

**Severity counts: major 11, medium 11, low 24 (23 in pass 1, 1 in pass 2). Refused findings: 13 (listed at the end).**

## Changes — pass 1

### Major
All 11 major changes are scansions the scanner got wrong with no flag. Each now has a hand entry in `scan-fixes.json`.
1. **6.509**: the scanner contracted *Pria-* to one syllable and made *-mi-* long. Hand scansion: Ād quae | Prī-ă-mĭ | dēs nĭ-hĭl | Ō tĭb(i) ă | mī-cĕ rĕ | lic-tum. The first syllable is lengthened as at 3.295 and 6.494.
2. **6.510**: the scanner gave *Deiphobo* a one-syllable Dei- and a long -pho-. Hand scansion: om-nĭ-ă | Dē-ĭ-phŏ | bō sol | vīs-t(i) et | fū-nĕ-rĭs | um-brīs.
3. **6.515**: the scanner made both a's of *fātālis* short, and *-lis* and the e- of *equus* long. Hand scansion: Cum fā | tā-lĭs ĕ | quus sal | tū sŭ-pĕr | ar-dŭ-ă | vē-nit.
4. **6.522**: the scanner read *quies* as one syllable and made *alta*'s -a long. The line is five dactyls: dul-cĭs ĕt | al-tă quĭ | ēs plă-cĭ | dae-quĕ sĭ | mil-lĭ-mă | mor-tī.
5. **6.525**: the scanner made the Me- and -ne- of *Menelaum* long and contracted -laum. Hand scansion: in-trā | tec-tă vŏ | cat Mĕ-nĕ | lā(um) et | lī-mĭ-nă | pan-dit.
6. **6.529**: the scanner had the -o- and -li- of *Aeolides* long, the tā- of *tālia* short, and *Grais* as one syllable. Hand scansion: hor-tā | tor scĕ-lĕ | r(um) Ae-ŏ-lĭ | dēs Dī | tā-lĭ-ă | Grā-īs.
7. **6.531**: the scanner made the ā of *cāsūs* and its -ūs short, and the a- and -ge of *age* long. Hand scansion: Sed tē | quī vī | vum cā | sūs ă-gĕ | fā-rĕ vĭ | cis-sim.
8. **6.564**: the scanner made *lūcīs* short in both syllables and the He- and -ca- of *Hecate* long. Hand scansion: sed mē | cum lū | cīs Hĕ-că | tē prae | fē-cĭt Ă | ver-nīs, as at 6.118.
9. **6.582**: the scanner made *et* and the A- of *Aloidas* long, and its -lō- and -ī- short. Hand scansion: Hīc ĕt Ă | lō-ī | dās gĕ-mĭ | nōs im | mā-nĭ-ă | vī-dī. The Greek has ω and -ει-.
10. **6.600**: the scanner read *requies* as two long syllables. Hand scansion: pec-tŏ-rĕ | nec fī | brīs rĕ-quĭ | ēs dă-tŭr | ul-lă rĕ | nā-tīs.
11. **6.601**: the scanner contracted the *-xio-* of *Ixiona* to one syllable and made its -na long. Hand scansion: Quid mĕ-mŏ | rem Lă-pĭ | thās Ix | ī-ŏ-nă | Pī-rĭ-thŏ | um-que.

### Medium
12–17. **Scansion: the known blind spots and the packet's flags**:
   - **6.523**: *coniunx* was read as co-ni-unx. It is con | iunx, as at 6.473.
   - **6.539**: *Aenea* was split into A-e, with -ne- short. Ae- is one syllable, -nē- is long and the vocative -ā is long (as at 6.52).
   - **6.548 and 6.559**: *Aeneas* was split into A-e, with -ne- short.
   - **6.544** (packet flag, COSTLY): Dē-ĭ-phŏ | bus con | trā nē | sae-vī | mag-nă să | cer-dōs. The scanner made -i- and -pho- long, and the adverb *contrā* and the prohibitive *nē* short.
   - **6.602–603** (packet flag, UNRESOLVED): this is a hypermetric line. The -que of *cadentique* elides into *imminet*: quōs sŭ-pĕr | ā-tră sĭ | lex iam | iam lāp | sū-ră că | den-tī(que). The entries follow 1.448 and 4.558: -que is left unmarked after ×. Line 603 needs its own entry because it shares unit 47 with 602, and a unit with an unresolved line receives no sc.
18. **Note 577 (unit 37)**: the note said "Virgil doubles the depth" of Homer's Tartarus. That does not follow. Homer's Tartarus lies as far below Hades as heaven is above earth (Iliad 8.13–16), which already makes it about twice the height of heaven below the surface. It is Hesiod's measure (Theogony 720) that Virgil doubles. The note now says both.
19. **Note 585 (unit 40)**: the note said "the punishment is for what he did while he was doing it, his blasphemy caught in the act". This muddled the grammar. The note now says that *dum* takes the present as its regular tense, even of past time: "while he was imitating". The fact that he was struck down in the act (592–594) is now a separate sentence.
20. **i 539**: the drafter had "Night is hurrying down… using up the hours in tears". It now reads "Night is sweeping down, Aeneas, and we are passing the hours in tears." The old version was too close to the stock "night comes on apace… we waste the hours in weeping".
21. **i 546**: the drafter had "Go on, glory of our nation, go on". That ran close to a well-known version. It now reads "On your way, pride of our people, on your way; and may you have the use of kinder fates than mine!" `new-renderings.md` was updated to match.
22. **i 562–563**: the drafter had "no one who is pure may set foot on that threshold of guilt". That was close to a known version. It now reads "no one who is pure is permitted to step upon that criminal threshold", which is also closer to *sceleratum*.

### Low
23. **Note 513 (unit 2)**: "'Supremam… noctem' frames the line" was wrong, because *supremam* is the third word. It now reads "spans the line" (as in 044).
24. **Note 515 (unit 3)**: the note glossed "'orgia'… is its accusative, 'crying euhoe over the rites'". It now calls *orgia* the object, "celebrating the rites with the cry of euhoe". `i` was changed to match: "raising the Bacchic cry in the rites".
25. **Note 531 (unit 11)**: the prose order was given as "(quis) casus". The text has the interrogative adjective *qui*, so it now reads "qui casus".
26. **Note 537 (unit 15)**: "'Fors' is short for 'forsitan'" was not accurate. *Fors* is the noun "chance" used as an adverb. The note now says so.
27. **Note 548 (unit 23)**: "'rapidus… amnis' frames the line" was wrong, because *rapidus* is the second word. It now reads "spans the line".
28. **Note 566 (unit 32)**: the note spoke of "the double '-que' runs on to 'subigit'". There are three -que's. It now says the "-que… -que" pattern runs on to a third -que.
29. **Note 601 (unit 46)**: "'Ixiona' and 'Pirithoum' are Greek accusatives" was half wrong. *Pirithoum* is the ordinary Latin -um, so the note now says that.
30. **Note 603 (unit 48)**: "'Genialibus altis… toris' frames the line" was wrong, because the phrase crosses the line-end. It now reads "runs over the line-end".
31. **l 510**: "to the shade of the dead man" is now "to the shades of the corpse", which keeps the plural *umbris* and the note's sense of *funeris*.
32. **l 524**: "from his head" is now "from my head", because Deiphobus is speaking. `i` already had "my".
33. **l 530**: "a penalty" is now "penalties", for the plural *poenas*.
34. **l 550**: "encircles torrent a river" used "torrent" as an adjective, which English cannot do. It is now "encircles rushing a river".
35. **l 602**: the -que of *cadentique* had been dropped. The line now reads "and to one falling".
36. **i 509–510**: "you have left nothing undone" was a stock phrase from a known version. It now reads "you have neglected nothing; every due to Deiphobus and to the shade of his body you have paid in full".
37. **i 511–512**: "the murderous guilt" is now "the deadly wickedness", away from a known "murderous crime".
38. **i 513–514**: the line is now "For you know how we passed that final night in a gladness that deceived us; and you have reason enough, and more, to remember it."
39. **i 528**: "Why do I linger over it?" is now "Why should I draw this out?"
40. **i 533–534**: "joyless sunless dwellings, this place of turmoil" is now "gloomy homes where no sun shines, this troubled place".
41. **i 547**: "He said no more, and with the word he turned away" is now "That was all he said, and with the word still on his lips he turned his steps away". This keeps *in verbo* and *vestigia*.
42. **i 557–558**: "the clank of dragging chains" was close to a known version. It now reads "the screech of iron and the rattle of chains hauled along".
43. **i 573–574**: "grating on their hinges… the accursed gates are thrown open" was close to a known version. It now reads "Then, and not till then, the accursed gates swing wide, their hinges shrieking with a hideous noise", which also brings out *tum demum*.
44. **i 595–597**: "spread out over nine full acres" is now "covering nine whole acres as it lies".
45. **i 602–603**: "Over them hangs a black crag that seems on the very point of slipping and falling" was close to a known version. It now reads "Above them a dark rock hangs, forever on the point of sliding down, and looks as if it were already falling".

## Changes — pass 2
- **P2-1 (low)**: in note 585, the pass-1 sentence "The cruel penalty fell on him in the very act" blurred the fact that he is paying *now*, in Tartarus. It now reads "He was struck down in the very act (592–594), and pays for it here."

## Scan-fixes lines added (18)
These 18 entries were appended at the end of `scan-fixes.json`, each with its reason. The existing entries are unchanged: the diff only appends.
- 6.509
- 6.510
- 6.515
- 6.522
- 6.523
- 6.525
- 6.529
- 6.531
- 6.539
- 6.544
- 6.548
- 6.559
- 6.564
- 6.582
- 6.600
- 6.601
- 6.602
- 6.603

Each entry matches its line's words under `WORD_RE` and has six feet. Each has five dactyls or spondees, then –× (602 is –× with -que unmarked), 13–17 syllables, one × and one ‖.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**:
  - *Teucrum* (562) is right as one diphthong.
  - *evantes* (517) is right as ē-van-tēs, Greenough's spelling with consonantal v.
  - *Salmonea* (585) is right as Sal-mō-nĕ-ă, the Greek accusative of -eus with no diphthong.
  - *Tartareus* (551) is right: it is adjectival -e-us, four syllables.
- **Initial Ae-**:
  - *Aenea*, *Aeneas* and *Aeolides* are fixed (529, 539, 548, 559).
  - *aetherio* (536), *aetherium* (579) and *aere* (591) are right.
- **Consonantal i after a prefix**:
  - *coniunx* (523) is fixed.
  - *traiecerat* (536: trā-iē-cĕ-rat) and *deiecti* (581: dē-iec-tī) are right.
  - *iacentem*, *iecur*, *Iovem*, *Iovis* and *iugera* are right.
- **Hiatus**: there is none in this part. *Nihil O* (509) is a consonant before the vowel, and *O virgo* (560) follows -es.
- **Greek names**:
  - These were checked and are right: Phlegethon (551), Tisiphone (555, 571, Tī-sĭ-phŏ-nē), Rhadamanthus and Gnosius (566), Hydra (576), Titania (580), Tityon (595), Elidis (588) and Graium (588, two syllables, Grāi-um).
  - Deiphobus (510, 544), Hecate (564), Aloidas (582), Menelaum (525), Priamides (509) and Ixiona/Pirithoum (601) are fixed.
- **555 *palla… cruenta***: these are ablatives with long -ā. The scanner has them right.
- **589 *sibi***: the scanner has the final -ī long, which is the only fit (the final i of *sibi* is common).
- **545 *tenebris***: the -nē- in the sixth foot is long by mute and liquid. Right.

## Doubtful quantities entered on the only fit
- **6.509 Prīamidēs**: the lengthened first syllable is entered as at 3.295 and 6.494. This is unconfirmed (QUESTIONS 19).
- **6.529 Grāīs**: entered as two syllables (as at 2.786). Read as one syllable, the line cannot fit with the correct *tālia*.
- **6.582 Ălōīdās**: the long -ī- rests on the Greek -ει- form. A short -ĭ- would leave the second foot –⏑ before the long *-dās*.

## Refused findings
- **R1 — rule 5b, no misprints**: I agree with the drafter's finding.
  - 509 *Nihil O tibi amice* has no commas round the vocative. That is Greenough's punctuation, not an error the sense forces, and the note already says how he prints it.
  - 602 *quos* in lowercase after the bracketed 601 is deliberate: the relative continues the sentence across the bracketed line. The note at 602 explains it.
  - 535 *roseïs* (a diaeresis) and 589 *honorem,—* are his print habits.
  - `t` is unchanged.
- **R2 — Citations verified and kept**:
  - Odyssey: 13.80 (θανάτῳ ἄγχιστα ἐοικώς), 8.517–520 (Odysseus and Menelaus at Deiphobus's house), 11.236 (Tyro, daughter of Salmoneus), 11.305–320 (Otus and Ephialtes, Ossa and Pelion, killed by Apollo), 11.576–581 (Tityos, nine plethra, two vultures), 11.582–592 (Tantalus), 10.513 (Pyriphlegethon into Acheron), 4.564 (Rhadamanthus in the Elysian plain) and 4.271–289 (Helen at the horse).
  - Iliad 8.13–16 (the passage is right; only the claim drawn from it was changed, item 18).
  - Plato, *Gorgias* 524a (the meeting of the roads, and Rhadamanthus as judge).
  - Pindar, *Olympian* 1 (the stone hung over Tantalus, around 1.55–58).
  - Aeneid: 2.234, 2.248–249, 2.256–257, 6.52, 6.118, 6.287, 6.397, 6.630–636 and 6.637–639.
- **R3 — Note lengths**: units 509 (163 words), 515 (170) and 566 (156) exceed the validator's 140-word warning. This is a warning, not a failure, and each sentence carries its own construction, so they are kept.
- **R4 — Speech-mark imbalance (5 “, 4 ”)**: this is correct, because the Sibyl's speech runs into aeneid-046. Kept.
- **R5 — Note 533, imperfect *adires* after the present *fatigat***: the note's explanation ("looks back on the coming as already done") is Conington's line. Kept.
- **R6 — l 535 "with rosy Aurora her four-horse car"**: this reads slightly loosely against *roseis… quadrigis*, but the note gives the construction. Kept.
- **R7 — Note 576, "ablative of description" for *hiatibus* with *immanis***: this is defensible. One could also call it an ablative of respect. Kept.
- **R8 — Note 528, *thalamo* as a dative of direction**: this is the standard poetic dative. Kept.
- **R9 — Note 535, "the visit seems to have a time allotted to it"**: this is supported by *omne datum… tempus* in 537. Kept.
- **R10 — Note 562, "frames the line-end"** for *sceleratum… limen*: this is imprecise but not false, because the pair does enclose *insistere* at the line-end. Kept.
- **R11 — i 601, "Why should I speak of the Lapiths, of Ixion and Pirithous?"**: this is the literal rendering of a praeteritio formula, not a distinctive echo. Kept.
- **R12 — i 520–522, "the very likeness of quiet death"**: this is not a known version's wording. Kept.
- **R13 — 6.594 sc has no ‖ mark**: the scanner's quantities are right, and the build and validator do not require a caesura mark. No entry was added.

## For the owner (QUESTIONS.md)
- **6.602–603 hypermetric *cadentique***: this is entered with the -que unmarked and elided into *imminet*. The audio should elide it across the line-end, not read it as a sixth-foot syllable.
- **Lengthenings and syllable counts on the only fit**: 6.509 Prīamidēs (with 3.295 and 6.494), 6.529 Grāīs as two syllables, and 6.582 Ălōīdās.
- **Note 577, Theogony 720**: the line is cited from memory (Hesiod's "as far beneath the earth as heaven is above it", around 720–721). Check the exact line number if a copy is at hand.
