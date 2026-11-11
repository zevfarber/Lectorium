# Review — aeneid-044 (Aeneid VI.398–508), adversarial reviewer

I reviewed this part in two passes. In pass 1, I checked each of the 60 units word by word: `l`, `i` and `n` against the Latin, every grammatical label, every citation and memory claim, the speech marks and misprint notes, and every `i` for remembered English. The passages the brief flagged got the closest check: 426–429, 450–455, 460 and 469–474. Pass 2 re-read every edited unit in full and fixed three problems that pass 1 had introduced (items P2-1 to P2-3).

I then hand-scanned all 111 lines by quantities and compared each with the scanner's output. The scanner was run in-process, the way `build_aeneid.py` calls `SL.scan_story`. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule and of the validator's six-foot rule. With the fixes applied, all 111 lines pass. One COSTLY flag remains, at 6.448, and there the scanner is right (see below).

`t` is untouched. The cut tuples in `make_units.py` are unchanged. The regenerated `units.json` has the same `t`, `ln` and `p` in all 60 units (checked by script). `title`, `titleEn`, `part` and `about` are unchanged. Edits were made to the strings in `make_units.py` by a Python replace script, with each old string asserted to occur once, and `units.json` was regenerated with `make_units.py` (`A.jdump`). `build_aeneid.py` was not run.

**Speech marks**: `t`, `l` and `i` each have 4 “ and 4 ”.
- In `t`, the Sibyl's speech opens at 399. Aeneas's two speeches open at 456 and 500 and close at 466 and 508.
- The printed marks at 406–407 count as one ” and one “ in `t`.
- `l` and `i` open and close the Sibyl's speech at 399 and 407. They mark the parenthesis at 406 by closing and reopening the speech, so their extra pair stands in for the printed ”…“.

**Severity counts: major 9, medium 16, low 33 (30 in pass 1, 3 in pass 2). Refused findings: 12 (listed at the end).**

## Changes — pass 1

### Major
1. **Note 447 (unit 28), "'Laodamia' ends with '-mia' read as one syllable (-mya)"**: this is false. *Lāŏdămīa* has five syllables with a long -mī- (Greek -μεια), and the line closes Lā-ŏ-dă | mī-ă. The note now says so, and adds that *Pasiphaën* has four syllables (Pā-sĭ-phă-ē, as Ecl. 6.46 and Aen. 6.25).
2. **Note 500 (unit 54), "'Deiphobe'… with 'Dei-' read as one syllable"**: this is false. With a one-syllable Dei-, neither 495 nor 500 can open: at 495 *-bum* is long by position, which would give –⏑– in the first foot. *Dēĭphŏbe* has four syllables, and the note now says so.
3. **Note 507 (unit 59), "'te, amice' elides"**: this is false. The line needs *te* kept and shortened in hiatus: vānt tĕ ă | mī-cĕ nĕ | quī-vī. This is the well-known licence of the *qui amant* type. The note was corrected.
4. **6.408 scan wrong** (unflagged, cost 0). The scanner gave *plura* and *his* short and *venerabile* long ve-, ne-. Hand scansion: Nec plū | (ra) hīs Il | (le) ad-mī | rāns vĕ-nĕ | rā-bĭ-lĕ | dō-num.
5. **6.436 scan wrong** (unflagged). The scanner gave *proiecere* short -ie-, -ce- and *animas* long a-, -ni-. Hand scansion: prō-iē | cē(re) ă-nĭ | mās quam | vel-lent | ae-thĕ-r(e) ĭn | al-tō. The perfect stem is iēc- and the ending is -ēre.
6. **6.494 scan wrong** (unflagged). The scanner contracted *Pria-* and made -mi- long. Hand scansion: At(que) hic | Prī-ă-mĭ | dēn lă-nĭ | ā-tum | cor-pŏ-rĕ | tō-tō, with the first syllable lengthened as at 3.295.
7. **6.495 scan wrong** (unflagged). The scanner gave Dei- one syllable and -pho- long. Hand scansion: Dē-ĭ-phŏ | bum vĭ-dĕt | et lă-cĕ | rum crū | dē-lĭ-tĕr | ō-ra.
8. **6.505 scan wrong** (unflagged). The scanner gave *tumulum* long tu-, mu- and *Rhoeteo* short -te-, -o. Hand scansion: Tunc ĕ-gŏ | met tŭ-mŭ | lum Rhoe | tē-ō | lī-tŏ-r(e) ĭ | nā-nem.
9. **6.507 scan wrong** (unflagged). The scanner elided *te* and gave a long a- in *amice*. Hand scansion as in item 3.

### Medium
10–19. **Scansion, the known blind spots and the packet's flags**:
   - **6.403** (flag): *Troius* has three syllables (as at 1.596), and Ae- is one syllable.
   - **6.413, 424, 467 and 475**: *Aenean* and *Aeneas* were split into A-e, with -ne- short.
   - **6.447** (flag): see item 1.
   - **6.473**: *coniunx* was read as co-ni-unx.
   - **6.479**: *Tydeus* was read as three syllables with short Ty-. It is Tȳ-deus, as at 2.164.
   - **6.489**: *Danaum* was read with synizesis and a long Da-. It has three syllables, Dă-nă-um, as at 1.30.
   - **6.500** (flag): *Deiphobe* has four syllables, and Teu- is one syllable.
20. **Note 407 (unit 6)**: the note read "'Tumida ex ira' is 'swollen from anger', 'ex' giving the cause". `Ex` here marks the state being left ("out of swelling anger"), not the cause. The note now also says that, because the -a is elided, *tumida* can be taken with *corda*. `l` was changed from "Swollen with anger then his heart settles" to "From swelling anger then his heart settles".
21. **Note 436 (unit 22)**: the note said "the imperfect subjunctive of an unreal wish". *Quam vellent* is not a wish subjunctive. It is the unreal present, a conditional whose "if" is left unspoken. Corrected.
22. **Note 474 (unit 40)**: the note said "'Illi' is a dative with 'respondet', 'answers her cares'". In fact `curis` is the dative governed by *respondet*, and *illi* is a dative of reference. Corrected.
23. **Note 481–485 (unit 45)**: the note said "'Ingemuit' takes the names as its objects". *Ingemuit* is intransitive here. The names are in apposition to *quos… omnes*, the object of *cernens*, which is how `i` already reads them. Corrected.
24. **i 458–460 (VI.460)**: "it was against my will, my queen, that I went from your shores" carried "against my will, my queen", a distinctive run from the best-known versions. It is now "it was not by my own choice, my queen, that I parted from your shore". `new-renderings.md` was updated.
25. **i 472–474**: "tore herself away and fled, still his enemy … answers her sorrows and gives her love for love" ran almost word for word with a well-known version. It is now "In the end she wrenched herself free and rushed away, hostile to him, back into the shade-giving grove, where Sychaeus, once her husband, meets her griefs with his own and returns her love in equal measure".

### Low
26. **Note 405–407 (unit 5)**:
    - "'Nulla' is used as an adverb" was not accurate, because *nulla* agrees with *imago*. The note now says it does the work of an emphatic *non*.
    - "subjunctive … of confident expectation" is not a standard category. It is now "a potential subjunctive shading into a mild command".
27. **Note 408 (unit 7)**: "Charon's silence makes its own point" read more into *nec plura his* than the Latin says. It is now "Nothing more is said on either side".
28. **Note 417 (unit 13)**: "'trifaux' is a word coined for him" is now "a rare word, perhaps coined for him".
29. **Note 419–421 (unit 14)**: "'Melle soporatam' is 'made sleepy with honey'" did not say what the participle agrees with. The note now says it goes with *offam*, "made sleep-bringing with honey".
30. **Note 430 (unit 18)**: "genitive of the penalty … the regular legal construction" was stated flatly. The note now gives *capitis damnare* as the pattern and the alternative "false capital charge" (*crimine mortis*).
31. **Note 431 (unit 19)**: "'Hae… sedes' frames the line" is wrong, because *hae* is the fourth word. It is now "spans the line".
32. **Note 445 (unit 27)**: "'His… locis'… framing the line" is now "with the first two names set between them".
33. **Note 450 (unit 29)**: "she has been dead only a few weeks" was an unsupported figure. It is now "she has not long been dead".
34. **Note 451–455 (unit 30)**:
    - "the relative 'qui' (the man) is put before its clause" was muddled. The note now says that *qualem… lunam* wraps round the relative clause, whose subject *qui* has no antecedent.
    - "Argonautica 4.1477–1480" could not be verified to the line and was softened to "near the end of Argonautica 4".
35. **Note 466 (unit 37)**: the relative reading of *quod* ("this word that I speak to you") was added beside "the fact that".
36. **Note 489–491 (unit 49)**: "the living Trojan they once routed" was ambiguous: it read as if the Greeks had routed Aeneas. It is now "The Greek dead, who once sacked his city, now panic at a living Trojan".
37. **Note 505–506 (unit 57)**: "each comrade lost on the shore" is not Homer's wording. The men were killed by the Cicones on the plain (Od. 9.64–66). The note now says that Odysseus will not let his ships sail until each comrade killed by the Cicones has been called three times. The citation 9.65 is kept.
38. **l 449 (unit 28)**: the *et* of *rursus et* had been dropped. The line now begins "and again into her old…".
39. **i 400–402**: "frighten the bloodless shades … keep to her uncle's house" was close to a known version. It is now "the monstrous porter may go on barking in his cave to all eternity and scaring the bloodless dead, and Proserpina may stay chaste within her uncle's doors".
40. **i 403–404**: "among the deepest shades of Erebus" echoed a known version. It is now "is coming down to his father, to the lowest shadows of Erebus".
41. **i 426–429** (flagged): "babes whom a black day stole away, torn from the breast … plunged into untimely death" was rephrased to "little ones shut out from the sweetness of life and snatched from the breast, whom a black day carried off and sank in death before their time".
42. **i 434–436**: "hating the light, flung away their lives" was close to a known version. It is now "loathing the daylight, cast their lives away".
43. **i 442–444**: "consumed with its cruel wasting … secluded paths … encircling grove of myrtle" was close to a known version. It is now "eaten away with its cruel sickness are kept out of sight on hidden tracks, sheltered all round by a wood of myrtle".
44. **i 447–449**: "turned back by fate into her first shape" echoed a known version. It is now "whom fate has returned once more to the shape she was born with".
45. **i 450–451**: "Phoenician Dido, her wound still fresh, was wandering" is now "Among these women, the wound still new upon her, Dido of Phoenicia was roaming through the wide wood".
46. **i 451–455** (the new-moon simile, flagged): the stock shape "as a man sees … or thinks he has seen" was broken up. It is now "like the young moon early in the month that a man glimpses rising among the clouds, or believes he glimpsed … with all the tenderness of love".
47. **i 456–457**: "you had sought your end with the sword" is now "you had taken the sword and gone to meet your end".
48. **i 461–464**: "I could not believe that by going I would bring such grief upon you" was close to a known version. It is now "nor did I ever think my going would cause you sorrow as great as this".
49. **i 466**: "This is the last time fate will let me speak to you" is the stock rendering. It is now "Fate allows me no word with you beyond this one."
50. **i 469–471** (flagged): "kept her eyes fixed on the ground, and her face was no more moved … hard flint" ran close to a known version. It is now "She stood turned away from him, her gaze held on the earth, and the speech he had begun changed her look no more than if she were unyielding flint, or a standing crag of Marpessian stone".
51. **i 475–476**: "pitied her as she went" is now "Yet Aeneas, stricken no less by the injustice of her fate, sent his tears after her far into the distance, and grieved for her going".
52. **i 492–493**: "the war-shout they began died away in their gaping mouths" echoed a known version. It is now "came to nothing in their open mouths".
53. **i 494–497**: "his face cruelly torn, his face and both his hands" was close to a known version. It is now "his features savagely slashed, the features and both hands … sliced away by a degrading wound".
54. **i 500–501, 502–504, 505–506 and 507–508** were lightly rephrased away from known versions:
    - "mighty in battle, sprung from Teucer's high blood, who had the will to punish you so savagely?"
    - "spent with the great slaughter you made of the Greeks"
    - "three times lifted my voice to summon your spirit"
    - "I could not set eyes on, or lay you in your native earth before I sailed away", which is also closer to *conspicere* and *decedens*.
55. **Note 481–485 (unit 45)**: the last sentence, on the names strung on -que, was dropped. It repeated the Iliad 17.216 point, and without the cut item 23 would have pushed the note further past the 140-word warning.

## Changes — pass 2
- **P2-1 (low)**: in the note at 451–455, the pass-1 edit had left "'qualem… lunam'" twice in a row. The second is now "The pair wraps round…".
- **P2-2 (low)**: the note at 474 read "…and 'illi'…, and 'aequat'…" with a doubled "and". It is now punctuated as two clauses.
- **P2-3 (low)**: i 498 "Aeneas could scarcely make him out" blurred *adgnovit*. It is now "Aeneas scarcely recognised him".

## Scan-fixes lines added (16)
These 16 entries were appended at the end of `scan-fixes.json`, each with its reason. The existing entries are unchanged: the diff only appends.
- 6.403
- 6.408
- 6.413
- 6.424
- 6.436
- 6.447
- 6.467
- 6.473
- 6.475
- 6.479
- 6.489
- 6.494
- 6.495
- 6.500
- 6.505
- 6.507

Each entry matches its line's words under `WORD_RE`. Each has six feet (five dactyls or spondees, then –×), 13–17 syllables, one × and one ‖.

## Hand-scan notes on the special lines (scanner right, no entry)
- **6.448** (packet flag, COSTLY 2.5): the scanner's quantities are right: īt cŏ-mĕs | ēt iŭ-vĕ | nīs quon | dām nunc | fē-mĭ-nă | Cae-neus. Caeneus is two syllables with the Greek -eus. The cost is the scanner's diphthong penalty, so no entry was added and the flag will still print.
- **Synizesis**:
  - *alveo* (412) is right as two syllables.
  - *deinde* (434) is right.
  - *Laodamia* (447) and *Deiphobe* (500) are **not** synizesis (items 1, 2).
- **Greek eu**:
  - *Teucri* (500): the scanner had Teu- right; the line was wrong for Dei-.
  - *Tydeus* (479) is fixed.
  - *Caeneus* (448) is right.
  - *ceu* (492) is right.
  - *euntem* (476) is right as e-un-tem (not a diphthong).
  - *Parthenopaeus* (480) is right as -pae-us.
  - *Sychaeus* (474) is right as Sy-chae-us.
- **Initial Ae-**:
  - *Aeneas* and *Aenean* are fixed at 403, 413, 424, 467 and 475.
  - *aeternum* (401), *aethere* (436) and *aequat* (474) are right.
- **Consonantal i after a prefix**:
  - *coniunx* (473) is fixed.
  - *proiecere* (436) is fixed.
  - *obicit* (421) and *obiectam* (422) are divided o-bi-cit and o-biec by the scanner, but the marks (–⏑⏑, ––) are the same as ob-ji-cit and ob-jec. No entry was added, as for *inice* in 043 (see Questions).
- **Hiatus**: 507 *te, amice* (fixed). There is no other hiatus in the part.
- **Elision checked**:
  - *fata est* (398), *Nullae hic* (399), *pietate insignis*, *genitorem imas*, *Tumida ex*, *plura his*, *Ille admirans*, *Inde alias* and *ingentem Aenean*.
  - *glaucaque exponit*, *obiectam atque immania* and *Continuo auditae*.
  - *ipsa in morte*, *maestamque Eriphylen*, *Evadnenque et*, *silva in magna* and *te adloquor*.
  - *sese atque inimica*, *longe et*, *illi occurrit*, *ille omnes longo ordine*, *Idaeumque etiam … etiam arma* and *Atque hic*.
  - *adeo adgnovit*, *supplicia et*, *Deiphobe armipotens*, *alto a*, *litore inanem*, *constitui et* and *conspicere et*.

## Doubtful quantities left as scanned, or entered on the only fit
- **6.479 Tȳdeus** with a long Ty- rests on 2.164 *Tydides* and on the metre. A three-syllable Ty-de-us cannot be made to fit, because "-us hic" would have to be long.
- **6.494 Prīamiden**: the long first syllable is the only fit, as at 3.295, which is unconfirmed (QUESTIONS 19).
- **6.505 Rhoetēo** with a long -tē- is the only fit given the short syllables of *tumulum*.
- **6.466 *adloquor***: the scanner divides it a-dlo. The marks are right (long first syllable by position).

## Refused findings
- **R1 — 6.406–407 marks**: these are handled per rule 5b, and correctly. `t` is as printed. The second ” heads the next unit's `t`, as at 6.155 and 6.197. `l` and `i` close the speech after *adgnoscas.* and mark the parenthesis. Both notes open with "The print has …, a misprint for …, corrected here". Kept.
- **R2 — 6.472 *tandem* and 6.486 *circumstant* lowercase after a full stop**: handled per rule 5b, as for 5.481 *sternitur* and 5.556 *omnibus*. Each note opens in house form. Kept.
- **R3 — Citations verified and kept**:
  - Iliad: 5.838–839 (the axle groans under Athena), 11.59–60 (τρεῖς τ' Ἀντηνορίδας), 17.216 (Glaucus, Medon, Thersilochus) and 8.368.
  - Odyssey: 9.65 (the threefold call), 11.623, 11.568–571 (Minos), 11.489–491 (Achilles), 11.543–564 (Ajax), 11.225–332 and 321–326, 24.5–9 and 8.517–520.
  - Hesiod, *Theogony* 311–312 and 790–791.
  - Catullus 66.39.
  - Georgics 4.479–480.
  - Aeneid: 11.28, 3.303–305, 4.314, 4.441–449, 4.366–367, 4.24–29, 1.343–356, 6.653–655, 6.540, 6.381, 6.388, 6.396–397 and 6.260/290.
- **R4 — 6.400 note, Apollo's year with Admetus**: "for a year" is a standard version (some say longer). Kept.
- **R5 — 6.412 *ingentem***: the note's point about heroic size is a standard commentary remark. Kept.
- **R6 — 6.415 *incolumis* as accusative plural**: this is Conington's reading. The nominative singular (Charon) is possible, but the note's reading is the usual one. Kept.
- **R7 — 6.428 *in limine primo*, 6.441 *Fields of Mourning***: these are standard names and literal phrases, not echoes. Kept.
- **R8 — i 460 `l`**: "unwilling, queen, from your shore I departed" is the literal order required of `l`. Kept.
- **R9 — Note lengths**: units 405 (155 words), 445 (171) and 494 (152) exceed the validator's 140-word warning. The overrun is mostly the drafter's, and every sentence earns its place: the misprint statement, the catalogue of heroines and the mutilation. This is a warning, not a failure, so they are kept.
- **R10 — 6.468 *lacrimasque ciebat***: the note takes the tears as his own, with hers as the alternative. `i` follows the note. Kept.
- **R11 — 6.477 *tenebant***: "were reaching" for the imperfect is defensible ("were making for"). Kept.
- **R12 — 6.505 the variant *in***: the note reports it without overstating. Kept.

## For the owner (QUESTIONS.md)
- **6.507 *te, amice***: this is entered as hiatus with a shortened *te* (vānt tĕ ă | mī-cĕ…). If the audio reads elision from `sc`, check that it does not elide here.
- **Unconfirmed lengthenings**: 6.479 Tȳdeus and 6.494 Prīamiden rest on the only fit, as at 3.295.
- **Prefix + consonantal i where the marks already coincide** (6.421 *obicit*, 6.422 *obiectam*, 6.466 *adloquor* divided a-dlo): no entries were added, the same open question as in 043.
- **6.448 Caeneus**: the scanner is right. The COSTLY flag will still print at build time, and no entry was added.
