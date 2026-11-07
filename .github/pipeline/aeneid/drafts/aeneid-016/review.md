# aeneid-016 review (Aeneid II.689-804), two passes

Findings: **major 6, medium 23, low 29** (58 in all). Changes made by script to `units.json` (39 `l`/`i`/`n` fields in 33 units, plus `about`; `t`, `ln`, `p`, `v` and the `l` line counts checked unchanged against the original, `i` is one line everywhere) and 21 entries added to `scan-fixes.json` (2.698, 710, 711, 718 carrier, 719 carrier, 720 half-line, 721, 723, 725, 726, 738, 745, 746 carrier, 747, 751, 766 carrier, 767 half-line, 777, 783, 787 half-line, 799). Speech marks (opening “ in the unit with the first word, closing ” in the unit with the last, in `t`, `l` and `i`): 689-691 (u0-u1), 701-704 (u6-u9), 707-720 (u12-u20), 733 (u26), 734 (u27), 776-789 (u51-u59). Counts of “ are 6 in `t` and `l` and 7 in `i` (the `i` of u26 splits the cry round "he cries": two pairs), of ” 6, 6 and 7; checked after the edits. Line 775 is in `[ ]` in all three layers.

`draft.py` still holds the pre-review text: do not re-run `make_units.py`, it would overwrite these edits.

## Changes to units.json
Major
1. u26 (733) n: "cf. 'ait' at 640" is a wrong line cite. Greenough (`source/aeneid-greenough.json`) has `sanguis, ait solidaeque…` at 639 (640 is `vos agitate fugam`). Now 639.
2. u29 (736-740) n: "`substitit` is the perfect of 'substo'". The verb is `subsisto` (perfect `substiti`), "halted". Fixed.
3. u33 (745) n: "a rhetorical question expecting the answer 'yes'" is false: `Quem… non incusavi` is a question word question, not a yes/no one. Now "whom did I not blame?", answer "everyone".
4. u39 (756) `l`: "if by chance my foot" gives the foot to Aeneas. `pedem… tulisset` is Creusa's foot (the `i` and the note had it right). Now "the foot".
5. u61 (792) `l`: "to my neck" is the reverse of the Latin (`collo`, her neck; the `i` had "her neck"). Now "to her neck".
6. u25 (730-733) n: "`creber` is a predicate adjective with `sonitus`". It is an attributive adjective, held apart from its noun by `ad auris`. Fixed.

Medium
7. u3 (695-697) n: "the star's track points the road the Trojans are to take" is not in the Latin and nothing in the lines says it. Cut; now "leaves a mark of light across the sky". `signantem vias` glossed "marking out its ways".
8. u15 (710-711) n: the reason given for keeping Creusa at a distance ("so that, if they are seen, she is not caught with them") is not in the text. Cut.
9. u21 (721-723) n: "`fatus`… the perfect participle of the deponent `for` with present sense" contradicts "having said" (the same slip was fixed in aeneid-015, item 16). Now "active in sense".
10. u47 (768-770) n: `Ausus` "(present sense)", same slip. Now "(active in sense)".
11. u42 (759) `l`, `i`, n: `l` "tower above the flames" reads `flammae` as an object, but it is the subject (`exsuperant flammae`); now "rise up, the flames". `i` "climb over everything" adds an object the Latin does not have; now "mount higher". Note says `flammae` is the subject.
12. u59 (789) `l`: "keep the love common" puts `communis` on `amorem`; it goes with `nati`. Now "of the son common keep the love".
13. u60 (790) `l`: "These things when having spoken she had given" doubles the sense (`Haec ubi dicta dedit`, `dicta` is the object). Now "These sayings when she had given".
14. u53 (778) n: (a) "`fas (est)`: 'it is right that you carry off'" drops the `nec`: "it is not right". (b) The Latin Library variant was misreported ("`portare Creusam`, without `comitem`"). The packet gives two entries for 778: `comitem` printed by the Latin Library where Greenough has nothing, and Greenough's `comitem asportare Creüsam` against `portare Creusam`; that is a different order and `portare` for `asportare`, not an omission. Note now says the line is printed a little differently, `portare` for `asportare`, `comitem` placed elsewhere; same sense. Variant left in the note because `asportare`/`portare` is a real difference of form.
15. u57 (785) n: "`Graiis` is the old form `Graiis`" says nothing. Now: the poetic adjective `Graius` for `Graecus`, dative plural with `matribus`; the Latin Library's `Grais` is the same word contracted.
16. u58 (788) n: "she keeps Creusa among the gods' lands instead of among the living" is the drafter's invention. Now "on these shores of Troy, and Virgil says no more of how".
17. u62 (793-794) n: the cross-reference to VI.700-702 was verified in Greenough (`source/aeneid-greenough.json`): 6.700-702 are these three lines, but the note said "the two lines… nearly word for word". It is all three lines, Greenough spells `brachia` there, and 6.702 (`par levibus ventis…`) is printed in `[ ]` (it is in his `bracketed` list). Note now says so. The gloss "the dream-sleep that slips from the mind" is unsupported and cut.
18. u65 (800) n: "`velim`… in a general relative clause" is wrong (a general relative takes the indicative). Now a present subjunctive, the clause saying what they stand ready for.
19. u11 (705-706) `i`: "the blazing houses roll their heat nearer" adds houses (`incendia`, "fires"). Now "the blazes"; also "through the city walls" for `per moenia`.
20. u50 (775) n: "one of the reasons the line is doubtful" asserts editors' reasons we cannot cite. Now says the infinitives could only be read as historical, "an awkward construction that may be why the line is bracketed". The bracket itself is correct: 2.775 is in `bracketed`; Greenough prints it in `[ ]`; `l` and `i` keep the brackets (item 7 of the brief).
Scansion (medium; see Scansion below)
21. 2.745 UNRESOLVED (hand-scanned, one reading only).
22. 2.787 (scanner fit at cost 3.8 by splitting `divae`, all spondees): a half-line.
23. 2.720 `abluero` UNRESOLVED: half-line.
24. 2.767 `stant circum` UNRESOLVED: half-line.
25. 2.747 Teucros split in two (Greek eu).
26. 2.698 `late` wrong quantities at cost 0.0.
27. 2.799 `convenere` wrong quantities at cost 0.0.
28. 2.710 Ĭūlus (COSTLY 2.8).
29. 2.723 `succedo` ē and Ĭūlus (COSTLY 2.6).

Low
30. 2.711 coniunx (COSTLY 3.1; synizesis route, same feet; con | iunx).
31. 2.725 coniunx (seventeen syllables for sixteen).
32. 2.738 coniunx (fifteen for fourteen).
33. 2.777 coniunx (fifteen for fourteen).
34. 2.783 coniunx (synizesis route, cost 1.5).
35. 2.721 subiecta: sub | iec | ta; the scanner's vowel reading made the fourth foot a dactyl.
36. 2.726 iniecta: in | iec | ta (thirteen syllables, not fourteen).
37. 2.751 obiectare: ob | iec | ta | re (the scanner had o | biec).
38. 2.718 carrier (the unit also holds the half-line 720).
39. 2.719 carrier (same unit).
40. 2.746 carrier (the unit also holds 745).
41. 2.766 carrier (the unit also holds the half-line 767).
42. `about`: "finding her home" is "their house"; "not his fault" is not in Creusa's words (she says only that these things do not happen without the gods' will). Both fixed.
43. u7 (702) n: "these are the Penates and the family's gods" asserted an identification; now "the ancestral gods of the house (the Penates are named separately at 717)".
44. u19 (717) n: "the heart of Aeneas' mission" overstated; now "part of Aeneas' task". The cross-reference I.6 `inferretque deos Latio` verified: in `drafts/aeneid-001/units.json` it is the second line of the unit at ln 5, so line 6.
45. u22 (723-724) n and `i`: "the same narrative present-and-perfect mix" refers to nothing (reworded); `i` "steps that cannot match his" added a modal; now "steps unequal to his".
46. u23 (725) `i`: "the darkest places" is a superlative the Latin lacks (`opaca locorum`). Now "shadowy places".
47. u24 (727) n: "the old nominative plural of `Graius`" now "the contracted nominative plural".
48. u26 `i` (echo): "fly, my son; they are upon us" to "flee, my son; they are drawing near".
49. u28 `i` (echo of the "unfriendly power… bewildered mind" shape): now "some power, I could not tell which, no friend to me, took my shaken wits from me in my terror".
50. u34 (747) n: `Teucros` named as an adjective agreeing with `Penatis`.
51. u44 (761) n: "(Achilles' old tutor in the Iliad)" stated as fact; now "presumably".
52. u45 (763) n: "`auro solidi` is 'solid with gold'" suggested plating; now "solid in gold, that is, of solid gold".
53. u48 (771) n: "the dead appear taller than the living" is a general claim; now "so she looks larger than the Creusa he knew".
54. u49 (774) `i` (echo): "my hair stood on end, and my voice stuck in my throat" to "the hair rose on my head, and my voice clung to my throat"; n `steterunt` "stood up" to "stood on end".
55. u62 (793-794) `i` (echo): "like the light breeze, most like a flitting dream" to "as light as the breezes and most like a sleep that flies" (`somno` is sleep).
56. u20 (718-720) n: added that 720 `abluero` is a half-line (as aeneid-015 did for 614, 623, 640).
57. u46 (766-767) n: added that 767 `stant circum` is a half-line.
58. u57 (785-787) n: added that 787 is a half-line; also "Achilles' and Pyrrhus' country" to "Achilles' home country" (the Myrmidons are Achilles' people; Pyrrhus is not tied to Thessaly by the text).

## The drafter's flagged cross-references
- **792-794 / VI.700-702**: verified against Greenough's Book VI (see 17), kept and corrected. **Odyssey 11**: the scene (Odysseus and the shade of his mother, three attempts) is kept without a line cite; reworded so the subject of "slips" is clear (u61).
- **717 / I.6**: verified (44), kept.
- **703 / "line 638"**: the only citation of 638 in the part is u5 (699-700) "his refusal to leave (638-649)". Greenough has `exsiliumque pati. “Vos O…` at 638 and the speech closing `contigit igni.”` at 649: verified, kept. The same check showed the 640 cite in u26 was wrong (1).
- Also verified in the source: "(688)" in u0 (`caelo palmas cum voce tetendit`); "713-715" in u31; "760" in u63; "704" in u67.

## Refused / checked and kept
- u1 `pietate` as ablative of cause, u2 `senior` as the elder man and the left-hand thunder, u12 `imponere` as a passive imperative, u14 `quo… cumque` as tmesis, u16 `animis… advertite`, u17 `urbe egressis`, u30 `nec post`, u36 `reverti` as the infinitive of the deponent `revertor`, u54 `Thybris`, `Lydius` and the ploughing metaphor, u55 Lavinia, u56 `Creüsae` as an objective genitive, u64 `exsilio` as a dative of purpose: labels checked against the forms and left.
- u45 `gaza` as a Persian loan word and u34 Teucer as the Trojans' early king: standard (Lewis & Short); left. u49 "a formula for terror that the poet uses again elsewhere": true (the line recurs), no line cites given, left.
- u29 `i` "taken from wretched me by fate" puts `fatone` inside the "whether" clause as the Latin does: left. u32 `i` "had slipped away" for the perfect `fefellit`: left, the sense is kept (low).
- `i` echoes checked and left: u12 "Come then, dear father" (generic for `Ergo age, care pater`), u54 "a vast plain of sea to plough" (the metaphor is in `arandum`), u67 "lifting up my father". No remembered wording was found beyond items 48, 49, 54, 55.
- Latin Library disagreements: 727 `examine` (noted, u24), 739 `lassa`/`lapsa` (noted, u29, "changes the sense a little"; Greenough's `lassa` is in `l` and `i`), 771 `furenti`/`ruenti` (noted, u48; `i` takes Greenough), 778 (14), 786 `Graiis`/`Grais` (15), 798 `volgus` (noted), 804 `montes`/`montis` (noted: same case). 738/769/772/784 `Creüsa`/`Creusa`, 741 `animumque`/`animumue`, 777 `divom`/`diuum` are spellings: the notes on 738 (diaeresis) and 777 (old genitive in -om) say what the form is; the rest ignored.
- No modern translator is named in any layer (checked), no Servius or Homer line cites remain, and the A&G cites (jussive, partitive genitive with a neuter adjective, `nescio quis`, middle voice) are all general headings.
- Two passes: the first read every note against its form and line, `l` against `t` word by word and `l` against `i`; the second took the scansion (every line, natural quantities) and re-checked the edited fields, speech marks, line counts and paragraph flags by script, and ran the validator's foot rules over all 116 lines with the 21 new entries (0 failures).

## Scansion
Every line scanned by hand with natural quantities of every open syllable (the scanner leaves them to the metre, so can return a valid fit with wrong quantities; this found 2.698 and 2.799 at cost 0.0). Letters of every entry equal the words; six feet, dactyl/spondee patterns, sixth foot –×; half-lines numbered 1..k with one ×.

Entries added:
- 2.698 lātē (long -tē, as at 1.21): dat lū(cem) | et lā | tē cir | cum lŏ-că | sul-phŭ-rĕ | fū-mant (scanner: la- and -te short, dactyl in the second foot).
- 2.710 ū-nă să | lūs am | bō-bŭs ĕ | rit Mĭ-hĭ | par-vŭs Ĭ | ū-lus (Ĭūlus three syllables, as 1.556, 2.674, 2.677).
- 2.711 sit cŏ-mĕs | et lon | ge ser | vet ves | tī-gĭ-a | con-iunx.
- 2.721 Haec fa | tus la | tos u-me | ros sub | iec-tă-quĕ | col-la.
- 2.723 suc-cē | do (que) ŏ-nĕ | rī dex | trae sē | par-vŭs Ĭ | ū-lus (cēdo has long ē; the scanner shortened it and read Iu- as one syllable).
- 2.725 pō-nĕ sŭ | bit con | iunx fĕ-rĭ | mur per ŏ | pā-că lŏ | cō-rum.
- 2.726 et me | quem dū | dum non | ul(la) in | iēc-tă mŏ | vē-bant (iniecta = in | iec | ta).
- 2.738 heu mĭ-sĕ | ro con | iunx fā | to(ne) ē | rep-tă Crĕ | ü-sa.
- 2.745 quem non | in-cū | sā-v(ī) ā | mens hŏ-mĭ | num-quĕ dĕ(o) | rum-que: fourteen syllables, `deo` one short syllable by synizesis. With `deorum` in three syllables (fifteen) there is no fit at all (checked by enumerating the quantities); the line is the only one in the part resting on this. **Unconfirmed.**
- 2.747 Ās-că-nĭ(um) | An-chī | sēn-quĕ pă | trem Teu | cros-quĕ Pĕ | nā-tis (Teu- one long syllable, as 1.304).
- 2.751 per Tro | (iam) et rur | sus că-pŭt | ob-iec | tā-rĕ pĕ | rī-clis.
- 2.777 Ō dul | cis con | iunx Non | haec sĭ-nĕ | nū-mĭ-nĕ | dī-vom.
- 2.783 il-lic | res lae | tae reg | num(que) et | rē-gĭ-a | con-iunx (same feet as the scanner; syllabification only).
- 2.799 Un-dĭ-quĕ | con-vē | nē ă-nĭ | mis ŏ-pĭ | bus-quĕ pă | rā-ti (convenēre is the perfect of convēnī: both ē long; the scanner had them short and a different foot pattern).
- Carriers 2.718, 2.719, 2.746, 2.766: the scanner's own fit for the whole line (cost 1.2, 0.5, 0.0, 0.0), applied because the half-line or unresolved line in the same unit leaves the scanner no whole line to scan. 2.718 needs `e` of `e tanto` long (ē, as ā for ab); 2.719 `donec` with long do-.
- Half-lines: 2.720 ab-lŭ-ĕ | rō (– ⏑ ⏑ | ×); 2.767 stant cir | cum (– – | ×); 2.787 Dār-dă-nĭs | et dī | vae Vĕ-nĕ | ris nŭ-rŭs (eleven syllables, four feet, last syllable ×). 2.787 is one of the ten unfinished lines of Book II (66, 233, 346, 468, 614, 623, 640, 720, 767, 787); it is not in the scanner's report as unresolved because the scanner found a fit by splitting `divae` into di-va-e and making every syllable long (cost 3.8), which is why the packet only called it COSTLY. If the owner disagrees that 787 is a hemistich, the entry's reason is the place to revisit.

Hand-scanned, scanner right, no entry (notable): 2.704 tibi with long -bi (cost 1.6; the only fit; cf. 2.784 parta tibi, -bi long again); 2.727 (COSTLY 2.0): te-la ne(que) | ad ver | so glo-me | ra ex | ag-mi-ne | Grā-i (Grai two syllables, the fit is the right one); 2.734 aera as ae-ra (diphthong, not three syllables) and clipeos as cli-pe-os (three, short pe); 2.735 nescio (short o), mihi; 2.744 dēfuit; 2.746 vīdī, crūdēlius; 2.761 asylo with long sy- (the only fit); 2.774 stĕtĕrunt (short -ĕrunt, the only fit); 2.775 (bracketed line scans as a full hexameter, cost 0.3); 2.781 Lȳdius with long Ly- (only fit); 2.792 ibi with long -bi (cost 0.6, only fit); 2.714 iuxtā with long -a (only fit); 2.755 ubīque (long -bi); 2.772 ipsĭus with short -si-; 2.801 Lūcĭfer. Greek eu: Teucros 747 (fixed). Initial Ae-: aestus 706 (acc. pl., long -tus), 759 (nom. sg., short -tus), aequor 780, aequis 724, aera 734; all diphthongs, scanner right. Consonantal i after a prefix: coniunx (711, 725, 738, 777, 783), subiecta 721, iniecta 726, obiectare 751. Hiatus: none (Creüsa has the diaeresis, 738, 769, 772, 778, 784).

## Unresolved / left open
- 2.745: `deo` as one short syllable (above).
- 2.787 as a half-line (above): from the syllable count and the standard list of Virgil's hemistichs, not from a source in the pipeline.
- Long final -i of `tibi` (704, 784) and `ibi` (792), long Ly- of `Lydius` (781), long sy- of `asylo` (761), long do- of `donec` (719), long `e` of `e tanto` (718), long -a of `iuxta` (714): each is the only fit; left, unconfirmed.
- 2.763 `gaza` with long ga- (cost 1.3): only fit, left.

## Counts
major 6, medium 23, low 29.
