# Review — aeneid-046 (Aeneid VI.608–702), adversarial reviewer

I reviewed this part in two passes. In pass 1, I checked each of the 51 units word by word: `l`, `i` and `n` against the Latin, every grammatical label, every citation and mythological claim, the speech marks, the misprints (README rule 5b), the bracketed line 702, and every `i` (and `l` where avoidable) for remembered English. I worked from the Latin and from memory of the reference works only; no translation was opened. Pass 2 re-read every edited unit in full and made one further change (P2-1).

I then hand-scanned all 95 lines by quantity and compared each with the scanner's output. The scanner was run in-process, the way `build_aeneid.py` calls `SL.scan_story`. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and of the validator's six-foot rule (feet 1–6, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×). I then ran a replica of the build's scansion step with the fixes applied: all 9 entries applied, the scanner report is empty (the packet's COSTLY flag at 645 is cleared), and all 95 lines pass the six-foot rule.

`t` is untouched. The cut tuples in `make_units.py` are unchanged. The regenerated `units.json` has the same `t`, `ln`, `p` and `v` in all 51 units (checked by script against a copy taken before any edit). `title`, `titleEn`, `part` and `about` are unchanged. Edits were made to the strings in `make_units.py` by a Python replace script, with each old string asserted to occur once, and `units.json` was regenerated with `make_units.py`. `build_aeneid.py` was not run. The diff to `scan-fixes.json` only appends.

**Speech marks**: `l` and `i` each have 6 “ and 7 ”, plus one ‘ ’ pair for Phlegyas. The extra ” closes the Sibyl's speech that opened at 562 in aeneid-045. `t` has 7 “ and 6 ” because of the misprinted “ at 630 and the unclosed “ at 620. The validator will print warnings for both, and they are expected.
- The Sibyl: carried over from 562 and closes at 627. Phlegyas's cry is 620 only, in single marks (see R1).
- The Sibyl: 629 → 632. The speech is broken by *ait* at 630 (a misprint, see item 22).
- The Sibyl to the souls: 669 → 671.
- Musaeus: 673 → 676.
- Anchises: 687 → 694.
- Aeneas: 695 → 698.

**Severity counts: major 5, medium 16, low 25 (24 in pass 1, 1 in pass 2). Refused findings: 16 (listed at the end).**

## Changes — pass 1

### Major
1. **6.684 *videt* is a misprint (rule 5b)**: the note called *videt* "a historic present" and treated the Latin Library's *vidit* as a variant tense. But the present *vĭdet* has a short first syllable and cannot stand in the sixth foot. Only the perfect *vīdit* scans. The note now opens: "The print has 'videt', a misprint for 'vidit'… t keeps the print, because t must match the pinned source; l and i give the reading." `l` was changed from "he sees" to "he saw". `i` already had "saw" and was also rephrased (item 41). No scan entry is needed, because the scanner already reads the word as *vī-dit*, with a long first syllable (R5).
2–5. **Scansions the scanner got wrong without a flag.** Each now has a hand entry.
   - **6.639**: the scanner made the -tu- and -na- of *fortunatorum* short and the ne- and -mo- of *nemorum* long. Hand scansion: for-tū | nā-tō | rum nĕ-mŏ | rum sē | des-quĕ bĕ | ā-tas.
   - **6.649**: the scanner made the -na- and -ni- of *magnanimi* long and read *heroes* as two syllables. Hand scansion: mag-nă-nĭ(mi) | hē-rō | ēs nā | tī mĕ-lĭ | ō-rĭ-bŭs | an-nis.
   - **6.673**: the scanner made both syllables of *lūcīs* short and the ha- and -bi- of *habitamus* long. Hand scansion: nul-lī | cer-tă dŏ | mus lū | cīs hă-bĭ | tā-mŭs ŏ | pā-cis.
   - **6.690**: the scanner made the du- and -ce- of *ducebam* short and the a- and -ni- of *animo* long. Hand scansion: sīc ĕ-quĭ | dem dū | cē(bam) ă-nĭ | mō rē | bar-quĕ fŭ | tū-rum.

### Medium
6–10. **Scansion: the known blind spots and the packet's flag**:
   - **6.618 *Theseus***: the scanner split the Greek *eu* and made The- short (Thĕ-sĕ-ūs). It is Thē-seus, two syllables. Hand scansion: īn-fē | līx Thē | seus Phlĕ-gў | ās-quĕ mĭ | ser-rĭ-mŭs | om-nis.
   - **6.635 *Aeneas***: the scanner made -ne- and -as short and the ă- and -dĭ- of *aditum* long. Hand scansion: oc-cŭ-păt | Aē-nē | ās ă-dĭ | tum cor | pus-quĕ rĕ | cen-ti.
   - **6.648 *Teucri***: the scanner split Te-u. Hand scansion: hīc gĕ-nŭs | an-tī | quum Teu | crī pul | cher-rĭ-mă | prō-les.
   - **6.685 *Aenean***: the scanner made -ne- and -an short and the a- and -la- of *alacris* long. Hand scansion: Aē-nē | ān ă-lă | crīs pal | mās ū | tras-quĕ tĕ | ten-dit. The ū of *utrasque* is lengthened before *tr* (see the doubtful list).
   - **6.645** (packet flag, COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag. Hand scansion: Nēc nōn | Thrē-ĭ-cĭ | us lon | gā cum | ves-tĕ să | cer-dos. *Threïcius* has four syllables (Θρηΐκιος).
11. **Note 666, *Sybilla***: the note said "corrected here", but `t` still shows *Sybilla*. The note is now in the house form used since aeneid-040: "The print has 'Sybilla', a misprint for 'Sibylla' (… eleven times with its other cases); t keeps the print, because t must match the pinned source; l and i give the reading." I verified the count of eleven by script: Sibyllae ×6, Sibylla ×3, Sibyllam ×2.
12. **Note, `l` and `i` 640**: the note said "The '-et' after 'campos aether' joins 'vestit' to the next clause". That is wrong on two counts: *et* is not an enclitic, and it does not join *vestit* to the next clause. *Largior* is a predicate with *est* understood, and *et* joins it to *vestit*. The note now says "the air here is ampler, and clothes the fields with light". `l` now reads "More bountiful here the air is, and the plains it clothes with light". `i` was rephrased to match. The old ending, "and stars of their own", was also a known version's wording.
13. **Note, `l` and `i` 632, *haec ubi***: the note said "'Haec ubi' is 'where', the relative placed after 'haec'". In fact *haec* agrees with *dona* ("these gifts"), and *ubi* refers back to *portas*. The note now says so. `l` now reads "lay down these gifts", and `i` reads "this gift". `i` was also moved away from "the walls raised in the forges of the Cyclopes".
14. **Note 618, Phlegyas**: the note stated as fact that he was "king of the Lapiths and father of Ixion and of Coronis". That genealogy varies between sources. The note now reads: "In the story Servius tells, Phlegyas, father of Coronis (and in some accounts of Ixion), set fire to Apollo's temple…".
15. **Note 617, Theseus**: the note said Proserpina was "named at 393 and, with Pirithous, in the bracketed line 601". Line 601 names Pirithous, not Theseus or Proserpina. The note now reads "Charon recalls the attempt at 392–397". It also flags the conflict with 6.122, where Aeneas counts Theseus among those who made the journey, and it adds the scansion Thē-seus.
16. **i 620**: "learn not to slight the gods" is a known version's wording. It now reads "learn not to hold the gods in contempt". `new-renderings.md` was updated.
17. **i 645–647**: "striking them now with his fingers, now with an ivory quill" matched a known version almost word for word. It now reads "Nor is the Thracian priest missing: in his long robe he answers their rhythms with the seven distinct notes of his lyre, sounding them sometimes with his fingers, sometimes with a plectrum of ivory."
18. **i 642–643**: "grapple on the yellow sand" is a known version's phrase. It now reads "Some train their bodies on wrestling-floors of grass, vie with one another in sport, and wrestle on the tawny sand".
19. **i 648–650**: "born in happier years" is a known version's phrase. It now reads "born in a better age".
20. **i 697–698**: "Let me clasp your hand, father, let me, and do not draw back from my embrace" was very close to a known version. It now reads "Give me your right hand to hold, father, give it, and do not slip away from my arms."
21. **i 673–675**: "we live in shady groves… the cushioned riverbanks" was close to a known version. It now reads "we haunt the shadowy woods, and keep to the soft couches of the riverbanks and the meadows kept fresh by running streams" (see also P2-1).

### Low
22. **Note 628–630**: the misprint sentence is now in the house form and opens the note: "The print has 'munus; / “adceleremus ait; Cyclopum', a misprint for 'munus; / adceleremus” ait; “Cyclopum': … (the same slip as at 6.46 and 6.52). t keeps the print…; l and i give the reading." The precedent is aeneid-040's 6.45–46 and 6.52 (`“Tros`).
23. **l 610**: "or who over riches alone brooded" let *soli* be read as "riches alone". It now reads "over riches, alone, brooded".
24. **i 623**: "a union the gods forbid" could be read as the exclamation "God forbid". It was also close to a known version ("forced his daughter's bed"). It now reads "this one broke into his own daughter's bedchamber, into a marriage that was forbidden".
25. **Note 652**: "The verbs stand first in each clause, 'stant… pascuntur'" was false, because *pascuntur* does not open its clause. It now reads "'Stant' opens the line: a still picture."
26. **Note 679–683**: the note quoted the line as "'fata fortunasque…", dropping the first -que of *fataque*. Fixed. It now also glosses *virum* as the old genitive plural.
27. **Note 700–702**: the note gave Greenough's reason for the bracket ("since it may have been copied in from Book II") as fact, but he gives none. It is softened to "presumably as a repetition carried over from Book II", and the note now names line 702 explicitly. It still says the line is bracketed as spurious and printed plainly in Book II, consistent with aeneid-016's II.792–794.
28. **Note 630–632**: "the smiths who work for Vulcan under Etna (they appear in Book VIII)" is now "the smiths who work Vulcan's forges (they are seen at work in Book VIII)". In Book VIII the forge is on Vulcania.
29. **Note 635**: "after seeing the place of the guilty" is now "after passing so near the place of the guilty". Aeneas only heard Tartarus and saw its walls.
30. **Note 656**: on *superne*, "most take it as 'upward'" is now "many take it as 'upward'". The commentators divide.
31. **Note 620**: the reason for ending Phlegyas's words at 620 is now stated from the Latin: "the 'Non… possim' of 625–627 is plainly her own voice, answering her 'Ne quaere doceri' of 614". "the usual reading" is now "as most editors do".
32–45. **Remembered English and small accuracy fixes in `i`**:
   - **617**: "unhappy Theseus sits, and will sit to all eternity" is now "luckless Theseus sits there, and will go on sitting for all time". The old wording ran close to a known version.
   - **618–619**: "most wretched of all" made *miserrimus* look like it took *omnis*. It now reads "in his utter misery".
   - **624**: "dared some monstrous wrong, and carried through what he had dared" is now "dared some unspeakable outrage, and saw his daring through".
   - **628–630**: "the aged priestess… But come now, take to the road" is now "the long-lived priestess… But now, come, be on your way… let us hurry".
   - **644**: "tread out the measures of a dance and chant their songs" is now "beat out a dance with their feet and recite their verses".
   - **653–655**: "the care they gave to keeping their horses sleek" is now "their concern to feed glossy horses".
   - **656–659**: "feasting on the grass… a fragrant laurel grove… the full river… rolls" ran close to a known version as a whole. It now reads "eating on the grass and singing a glad paean as one choir, amid a sweet-scented grove of laurel, from where the Eridanus pours its full stream up through the woods toward the world above".
   - **676**: "I will soon set you on your way down by an easy track" is now "I will soon set you down by an easy track where you wish to be".
   - **679–683**: "deep in a green valley… that were to pass up to the light above" is now "far down in a green hollow… shut away there, who were destined to rise to the daylight of the world above".
   - **684–686**: "coming towards him over the grass, he eagerly stretched out both his hands" is now "caught sight of Aeneas making his way across the grass to meet him, he reached out both hands in his eagerness; tears poured down his cheeks, and his voice burst from his lips".
   - **687–688**: "Has the devotion your father counted on mastered that cruel road?" is now "Has your loyalty, so long awaited by your father, won through the hardships of the road?"
   - **693**: "and buffeted, my son, by what dangers!" is now "and what dangers, my son, have tossed you about!"
   - **694**: "How afraid I was that the kingdom of Libya would do you some harm!" is now "How I dreaded that the realm of Libya might somehow injure you!"
   - **699**: "So he spoke, and all the while his face was wet with streaming tears" was close to a known version. It now reads "As he said this, a flood of tears kept running down his face."

## Changes — pass 2
- **P2-1 (low)**: in i 673–675, the pass-1 wording "None of us has a settled home; our homes are…" repeated "home". It now reads "we haunt the shadowy woods, and keep to…".

## Scan-fixes lines added (9)
These 9 entries were appended at the end of `scan-fixes.json`, each with its reason. The existing entries are unchanged: the diff only appends.
- 6.618
- 6.635
- 6.639
- 6.645
- 6.648
- 6.649
- 6.673
- 6.685
- 6.690

Each entry matches its line's words under `WORD_RE` and has six feet. Each has five dactyls or spondees, then –×, 14–15 syllables, one × and one ‖. In the replicated build with all fixes applied, the scanner report is empty and all 95 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *Theseus* (618) and *Teucri* (648) are fixed. *hymenaeos* (623) has no eu: hў-mĕ-nae-ōs, with -que elided into it. That is right.
- **Initial Ae-**: *Aeneas* (635) and *Aenean* (685) are fixed. The scanner has *aeternum* (617), *aether* (640), *aequora* (692) and *Aeneas* elsewhere right. Line 650 has no Ae- word (*Assaracus*, *auctor*).
- **Consonantal i after a prefix**: none in this part. *iugum* (676), *iam*, *iungere* (697), *iactatum* (693), *iubent* (632) and *iustitiam* (620) are all word-initial and right.
- **Hiatus**: none. *facili iam* (676) has a consonantal i, so there is no elision. The elisions at *magnanimi heroes* (649, fixed), *defixae hastae* (652) and *vetitosque hymenaeos* (623) are ordinary elisions before h-.
- **Synizesis**: the scanner has *dehinc* (678) right as one long syllable: dē-sŭ-pĕr | os-ten | tat dehinc | sum-mă că | cū-mĭ-nă | lin-quunt.
- **Others checked and right**: *Phlegyas* (618, Phlĕ-gў-ās, inside the fix); *Cyclopum* (630, Cȳ- long before cl, the only fit); *Musaeum* (667); *Anchisen* and *Illĭus* (670, short i as often in verse); *Eridani* (659, Ē-); *paeana* (657, -ā-); *Tyrrheno* (697); *Libyae* (694, three syllables); *Troiae* (650, two syllables); *periclis* (693); *comprendere* (626); *ibī* (700, the final i common). Lines 700–702 match aeneid-016's sc for II.792–794 apart from *brachia* for *bracchia*.

## Doubtful quantities entered on the only fit
- **6.685 ūtrasque**: the u is lengthened before *tr*. With a short ŭ, the line has no fit.
- **6.630 Cȳclōpum** (scanner's fit, no entry): Cy- is long before *cl*, which is the only fit.
- **6.640 aethēr** (scanner's fit, no entry): the -ēr is long, keeping the Greek η. With a short -ĕr, the 14-syllable line does not fit.

## Refused findings
- **R1 — Extent of Phlegyas's cry (620 only)**: kept. Greenough prints “ at 620 and only one ” (627), so the print does not decide the question. The Latin does: 625–627 *Non, mihi si linguae…* is the Sibyl's own disclaimer, picking up her *Ne quaere doceri* (614). The *hic… hic* of 621–623 is her pointing at the sinners. I could not consult Conington's text in this run (Perseus is blocked by the proxy), so the note no longer leans on "the usual reading". It now says "as most editors do" and gives the Latin reason (item 31). Single marks for the nested cry follow aeneid-037 (5.637).
- **R2 — 629–630 as a misprint**: I agree with the drafter. It is the same pattern as 6.45–46 and 6.52 in aeneid-040 (an opening mark printed for the closing mark after the first words, and no opening mark after *ait*). Treated identically: `t` as printed, `l` and `i` giving the reading.
- **R3 — i 700–702**: "to throw his arms around his father's neck" is the common shape for *collo dare brachia circum*. It is kept, because the brief and the house require consistency with the published II.792–794 (aeneid-016), which this rendering reproduces.
- **R4 — Note lengths over 140 words**: 608 (200), 620 (156), 628 (156), 679 (142), 684 (146) and 700 (157). These are warnings, not failures. Each sentence carries a construction or a required notice (the misprint, the speech extent, the bracket).
- **R5 — 6.684 scan entry**: not added. The scanner already gives `6vi–det×`, with a long first syllable, which is the quantity of the corrected *vīdit*. An entry would change nothing.
- **R6 — Rule 5b, other candidates**: none. *adceleremus*, *volnera*, *brachia*, *repostos*, *comprendere* and *Threïcius* are Greenough's spellings, not misprints.
- **R7 — Latin Library variants**: *inanis*, *artis*, *omnis*, *tranavimus*, *bracchia* and *acceleremus* are orthography, already noted where useful. *aliquos* (664) and *lauris* (658) are noted in `n`. *vidit* (684) is now handled as the misprint (item 1).
- **R8 — Citations verified and kept**:
  - Odyssey: 11.593–600 (Sisyphus), 4.563–568 (the Elysian plain), 11.204–208 (Anticleia, three times, "like a shadow or a dream"), and Book 11 for Orion hunting (572–575) and Achilles asking after his son (492ff).
  - Iliad 2.488–490 (ten tongues, ten mouths). Georgics 2.43–44.
  - Pindar, *Pythian* 2.21–24 (Ixion on the wheel). Pindar's dirge fragment on the sun below.
  - The Twelve Tables' *patronus si clienti fraudem fecerit, sacer esto*, which Servius cites here.
  - Aeneid: 1.3, 1.422, 3.167, 4.351–353, 5.722–740, 6.119–120, 6.122, 6.136–148 and 6.392–397.
- **R9 — Note 612, "Roman law let a husband or father kill an adulterer caught in the act"**: this is broadly true (custom, and the father's right under the Julian law). Kept.
- **R10 — Servius's identifications (Curio at 621, Antony at 622)**: these are attributed to Servius, not asserted. Kept.
- **R11 — Note 612, "slaves who deserted their masters… for Sextus Pompeius"**: this is the traditional explanation and is introduced with "usually taken". Kept.
- **R12 — 6.629 sc has no ‖**: the quantities are right, and neither the build nor the validator needs a caesura mark (aeneid-045 R13). No entry.
- **R13 — i 625–627, "a voice of iron"**: this is the literal *ferrea vox* and cannot be avoided. The rest already steers clear of the well-known openings. Kept.
- **R14 — i 695–696, "your image, father, your sorrowful image"**: this is the literal repetition of *tua… tua*. The clause shape differs from the known versions. Kept.
- **R15 — Note 686, "'utrasque' is plural because each hand is one of a pair"**: the label is loose (*uterque* is plural with a noun that is itself plural), but it is not false. Kept.
- **R16 — 6.635 caesura**: I put ‖ after *Aeneas* (penthemimeral), following the scanner's own ranking. The sense-pause after *aditum* would favour the hephthemimeral. Either is defensible, and neither gate checks it.

## For the owner (QUESTIONS.md)
- **6.684 `videt`**: a new rule-5b misprint. It cannot scan, and only *vidit* fits. Published as printed in `t`, with `l`/`i` reading *vidit* and the note opening with the print's reading, as for #23 and #36.
- **6.666 `Sybilla`** (for *Sibylla*) and **6.629–630 `“adceleremus ait;`** (as 6.46): published as printed in `t`, with the notes in the house form.
- **Phlegyas (6.620)**: the cry ends at 620, in single marks inside the Sibyl's speech. I could not reach Conington's note to confirm his view.
- **Doubtful quantities on the only fit**: 6.685 ūtrasque, 6.630 Cȳclopum and 6.640 aethēr.
