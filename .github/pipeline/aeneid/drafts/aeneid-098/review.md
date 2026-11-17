# Review — aeneid-098 (Aeneid XII.746–842), adversarial reviewer

**Severity counts:**
- **Major: 13.** All 13 are wrong scansions. They are 746, 760, 762, 770, 772, 783, 793, 794, 808, 816, 824, 827 and 836. The packet flagged only 772 and 824. Six had a cost of 0.0 (762, 770, 793, 816, 827 and 836). Two were false fits with the right syllable count (762 and 827).
- **Medium: 5** findings (24 edits).
  - Seven elisions were missing (756, 763, 804, 814 twice, 832, 834).
  - 758 `l` made *Rutulos* the object of *fugiens*.
  - 823 `l` attached *indigenas* to *nomen*.
  - The simile's `i` slipped into the past tense at 752–755.
  - Fourteen `i` renderings were rephrased as a precaution against remembered modern versions, mostly in Juno's plea and Jupiter's reply.
- **Low: 20** findings (20 edits plus 6 scan-fixes).
- **Refused or upheld without change: 24.**
- **Scan-fixes added: 19.** They were written straight into `scan-fixes.json` by `drafts/aeneid-098/add_scan_fixes.py --write` and appended after 12.744 in line order. The keys are 12.746, 12.760, 12.762, 12.770, 12.772, 12.783, 12.788, 12.792, 12.793, 12.794, 12.803, 12.808, 12.812, 12.816, 12.824, 12.827, 12.829, 12.836 and 12.837.
  - 13 fix wrong scans (Major).
  - 5 change only the syllable division (Low: 788, 792, 803, 829, 837). 803 also moves the caesura to the full stop.
  - 1 is a confirmation entered to clear the packet's COSTLY flag (Low: 812, as 12.704).
  - The git diff of `scan-fixes.json` is 214 insertions and 0 deletions.

Nothing blocks the build. The `scan_check.py` replica gives sc for 46 of 46 units, applies all 19 entries, and has no report left, no metre failures and no line-up failures. `build_aeneid.py` itself was not run.

## How the review was done

**Pass 1** went through all 46 units word by word:
- `l`, `i` and `n` against the Latin, every grammatical label, and every elision list line by line. The elision lists were also checked mechanically against the scanner's elided syllables, which agreed with the hand scansion on every line.
- The speech marks. There are four speeches: Turnus 777–779, Jupiter 793–806, Juno 808–828 and Jupiter 830–840. `t` has 4/4 and `l` and `i` have 5/5 each. The difference is the 777 *inquit*, where `l` and `i` close and reopen round "he says". 806 moves the closing mark from the head of the 806 unit to the end of the 803 unit. Both are deliberate (see below).
- The `p` flags at 746 and 766. Both are right.
- The bracketed lines 801–802, in `[ ]` in `t` and `l`, and in `[ ]` in `i`, with the note saying so.
- Cross-references checked in `source/aeneid-greenough.json`:
  - 12.319–320 (the arrow, *incertum qua pulsa manu*);
  - 12.134 (Juno on the hill now called Alban);
  - 12.468–472 (Juturna takes Metiscus's shape);
  - 12.90–91 (Daunus's sword) and 12.735–737 (Metiscus's sword taken in haste);
  - 12.745 (*vasta palus*);
  - 7.47–49 (Faunus, Picus, Saturn);
  - 1.254 (*Olli subridens hominum sator atque deorum*);
  - 5.432 and 12.905 (*genua labant*).

  All are right.

All 97 lines were hand-scanned by quantity and compared with the scanner's fit. `scan_check.py`, `review_check.py`, `review_edits.py` and `add_scan_fixes.py` are 097's, pointed at 098. Precedent entries:
- *Aeneas* 12.311, *Aenean* 12.63 and 11.910, *Teucros* 12.506, *Teucri* 12.744;
- *coniunx* 12.80 and 12.272, *adiungit* 12.244, *subiciunt* 12.288, *inicit* 9.553;
- *quia* 2.84, 5.231 and 8.650;
- lengthening at the pause before h: *erat hoc* 7.174;
- division only: *sublatis* 12.26, *sublapsa* 12.686, *adloquitur* 4.8, 8.372 and 10.228, *suprema* 12.653;
- confirmation: 12.704.

Sources: the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2** re-read every changed field (41 fields) against `t`, checked each `l` for words on the wrong line, and checked each `i` for drift, tense and remembered phrasing. Nothing further was found.

**Script runs.**
- A copy of the drafter's `units.json` and of `scan-fixes.json` was kept before editing, at `/tmp/claude-0/-home-user-Lectorium/41c8822a-fe7b-500a-9eeb-2865cf372c95/scratchpad/units.orig.json` and `scan-fixes.orig.json`.
- `review_edits.py` runs once from the drafter's file and makes 44 edits to 41 fields. Each old string is asserted to occur exactly once. Its guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` are unchanged;
  - `l` line counts equal those of `t`;
  - no `i` contains a line break;
  - every note is 15–139 words.
- `review_check.py` prints no faults:
  - it exempts the mark counts at 776, 803 and 806 and the quoted mark in the 803 note, for the reasons below;
  - marks are t 4/4, l 5/5, i 5/5;
  - notes run 37–105 words;
  - 46 units, 97 lines;
  - `BUILD REPLICA: OK`;
  - `t/ln/p/v vs drafter: OK`.
- `make_units.py` was not rerun and still holds the drafter's strings. Build from `units.json`, and do not rerun `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 746 | 1.2 | *Aeneas*: Nēc mĭ-nŭs \| Ae-nē \| ās quām \| quām tār \| dā-tă să \| gīt-ta (14). The scanner split Ae-. |
| 760 | 1.2 | *Aeneas*: Ae-nē \| ās mōr \| tēm cōn \| trā prae \| sēns-quĕ mĭ \| nā-tur (13). The scanner split Ae-. |
| 762 | **0.0** | *excīsūrum* (from *excīdo*) has -cī- and -sū- long, and *mĭnĭtans* is short-short: ēx-cī \| sū-r(um) ūr \| bēm mĭ-nĭ \| tāns ēt \| saū-cĭ-ŭs \| īns-tat (14). The scanner made ci, su short and mi, ni long. This is a false fit with the same count. |
| 770 | **0.0** | *Teucri* is Teu-crī: sēd stīr \| pēm Teū \| crī nūl \| lō dīs \| crī-mĭ-nĕ \| sāc-rum (13). The scanner split Te-u (14). *sacrum* is divided sac-rum, as 12.653. |
| 772 | 2.1 (flagged) | *Aeneae*, with *hasta* elided into it. The -bat of *stabat* is lengthened in the arsis at the pause, and h makes no position (as 7.174): Hīc hās \| t(a) Ae-nē \| ae stā \| bāt hūc \| īm-pĕ-tŭs \| īl-lam (13), four spondees. The scanner split Ae- (14). |
| 783 | 1.2 | *Aeneas*: rō-bŏ-rĭs \| Ae-nē \| ās Dūm \| nī-tĭ-tŭr \| ā-cĕr ĕt \| īns-tat (15). The scanner split Ae- (16). |
| 793 | **0.0** | *coniunx* is con-iunx: Quā iām \| fī-nĭs ĕ \| rīt cōn \| iūnx Quīd \| dē-nĭ-quĕ \| rēs-tat (14). The scanner read co-ni-unx (15). |
| 794 | 1.2 | *Aenean*, with *Indigetem* elided into it: Īn-dĭ-gĕ \| t(em) Ae-nē \| ān scīs \| īps(a) ēt \| scī-rĕ fă \| tē-ris (14). The scanner split Ae- (15). |
| 808 | 0.6 | *quia* is quĭ-ă, two shorts: Īs-tă quĭ \| dēm quĭ-ă \| nō-tă mĭ \| hī tŭ-ă \| māg-nĕ vŏ \| lūn-tas (17, five dactyls). The scanner used synizesis (16). |
| 816 | **0.0** | *adiuro* is ad-iū-rō, with a consonantal i: ād-iū \| rō Stў-gĭ \| ī că-pŭt \| īm-plā \| cā-bĭ-lĕ \| fōn-tis (15). The scanner read a-di-u-ro (16). |
| 824 | 2.0 (flagged) | *Teucrosque* is Teu-crōs-que. *Trōăs* has its -ăs long by position before *fieri*, and *fĭĕrī* is short-short-long: neū Trō \| ās fĭ-ĕ \| rī iŭ-bĕ \| ās Teū \| crōs-quĕ vŏ \| cā-ri (15). The scanner split Te-u (16). |
| 827 | **0.0** | *Rōmānă* has long Rō- and -mā-, and *Ĭtălā* a short I-: sīt Rō \| mā-nă pŏ \| tēns Ĭ-tă \| lā vīr \| tū-tĕ prŏ \| pā-go (15). The scanner made Ro, ma short and na, po long. This is a false fit with the same count. |
| 836 | **0.0** | *Teucri* is Teu-crī: sūb-sī \| dēnt Teū \| crī Mō \| rēm rī \| tūs-quĕ să \| crō-rum (13). The scanner split Te-u (14). |

### Low (scan-fixes)

- **Division only**, with the same feet and quantities as the scanner's fit. Each scanner division put an open long mark on a short vowel, which the audio would voice long. This follows Book XII practice (12.26, 12.288, 12.686, 12.687, 12.729).
  - **788** *sublimes* is now sub-lī-mes.
  - **792** *adloquitur* is now ad-lŏ-quĭ-tur, as 4.8, 8.372 and 10.228.
  - **803** *supremum* is now sup-rē-mum, as 12.653. The caesura moves to the full stop after *est*, the penthemimeral.
  - **829** *subridens* is now sub-rī-dens.
  - **837** *adiciam* is now ad-ĭ-cĭ-am, as 12.288 and 9.553.
- **812** was flagged COSTLY 2.0. It is confirmed by hand: stār(em) ă-cĭ \| ē tră-hĕ \| rēm-qu(e) ĭ-nĭ \| mīc(a) īn \| proe-lĭ-ă \| Teu-cros (16). The flag comes from the penthemimeral caesura falling on an elision. The entry only clears the flag, as at 12.704.

### Checked by hand and found right, so no entry

- **747** *genua* is ge-nu-(a), with the a elided into *impediunt*: īn-tēr \| dūm gĕ-nŭ \| (a) īm-pĕ-dĭ \| ūnt cūr \| sūm-quĕ rĕ \| cū-sant (15). The consonantal-u reading (gen-va, 14) also scans, but nothing requires it here, unlike *genua labant* at 5.432 and 12.905. House practice prefers the ordinary reading to synizesis, so the scanner's fit stands. The note now says so.
- **779** *Aeneadae*, with *contra* elided into Ae-: the scanner has Ae- as one syllable here, Ae-nĕ-ă-dae.
- **810** *aeria* is ā-ĕ-rĭ-ā (Greek ἀέριος, as 8.221), with *me* elided. This is not the diphthong ae. The scanner is right at cost 1.2.
- **749** *siquandō* needs a long -dō in the fourth foot. **764** *lĕvia* means "light", and *lūdĭcra* is short before cr. **778** *tĕnē*, *cŏlŭī*. **789** *hīc*. **805** *miscēr(e) hymĕnaeos*, an elision before h. **814** *suās(i) ēt*. **821** *cōnūbīs*. **830** *Iŏvĭs*, and *ēs* long by position. **832** *Vēr(um) ăg(e) ĕt*. **839** *sūprā*, long by nature.
- **814** *ma-iora* and **820** *ma-iestate* keep the scanner's division, as 12.244 kept *ma-ius*.
- Every other line has the quantities and elisions the scanner gives it.

There is no hiatus in the part.

## Medium

- **M1 (missing elisions, 6 edits):**
  - 756 *ver(o) exoritur*;
  - 763 *Quinqu(e) orbis*;
  - 804 *infand(um) adcendere*;
  - 814 *suas(i) et* and *maior(a) audere*;
  - 832 *Ver(um) ag(e) et*;
  - 834 *Sermon(em) Ausonii*.
- **M2 (758 `l`).** "He, at once fleeing the Rutulians, at once rebukes all" made *Rutulos* the object of *fugiens*. It is the object of *increpat*. It now reads "He, at once fleeing, the Rutulians at once rebukes, all", which matches `i` and the note.
- **M3 (823 `l`).** "not the old, native, name to change the Latins" attached *indigenas* (accusative plural) to *nomen*. It now reads "not the old name the native Latins to change", which matches the note's "'indigenas… Latinos', framing the line".
- **M4 (simile tense, 752–755 `i`).** The simile opens in the present at 749 ("has come upon… presses"), but 752–755 went into the past ("ran", "clung", "was mocked"). Both units are now in the present ("runs", "clings… has him, snaps… and is cheated by a bite on empty air"), as in 097.
- **M5 (`i`, precautionary rephrasings, 14 edits).** Each was rebuilt from the Latin. `l` was not touched in these edits.
  - **764–765.** "no trifling prize of the games they were after" is now "no slight reward, no prize of the games, that they strove for: the contest was for Turnus's life and blood".
  - **808–809.** "It is because I knew that this was your will… though against my wish" is now "It is only because I knew this to be your will… that I have left Turnus and the earth behind, little as I wished it".
  - **819–820.** "One thing, which no law of fate forbids, I beg of you…" is now "This one thing, which no law of fate holds bound, I implore of you for Latium, and for the dignity of your own blood". "Forbids" also misread *tenetur*.
  - **821–825.** "do not command the native Latins to change their ancient name, or to become Trojans and be called Teucrians" is close to stock. It is now "do not bid the Latins, born of this soil, give up the name they have always borne, nor become Trojans and take the Teucrian name, nor have the men change their speech or alter their dress".
  - **826–827.** "Let Latium stand; let there be Alban kings…; let the Roman stock grow mighty on Italian courage" is now "Let Latium live on; let Alban kings reign age after age; let the line of Rome draw its might from the manhood of Italy".
  - **828.** "Troy has fallen: then let it be gone for good…" is now "Troy has perished; grant that she stay perished, and her name with her".
  - **830.** "You are truly Jove's sister, Saturn's other child" is now "Sister of Jove you are indeed, the other offspring of Saturn".
  - **831.** "such great waves of anger you churn in your breast" is now "so huge is the swell of anger that you roll beneath your breast".
  - **832–833.** "I grant you your wish, and yield, beaten and willing both" is now "what you want I give, and I give way, overcome and yet of my own will".
  - **834–835.** "The Ausonians will hold on to the tongue their fathers spoke…" is now "The men of Ausonia will hold to the speech of their fathers and to their ways, and the name they bear now they will bear still".
  - **835–836.** "merged with them in blood alone, and sink from view" is now "mixed with them in body only, and settle out of sight among them". *corpore* is "body", not "blood".
  - **836–837.** "I will make them all Latins of one tongue" is now "make them, every one, Latins speaking with a single voice".
  - **838–840.** "you will see outstrip men and outstrip the gods themselves in devotion, and no nation will keep your festivals…" is now "From here will rise a people mingled with Ausonian blood, and you will see it pass beyond men, beyond the very gods, in devotion; nor will any nation pay you honour with equal zeal".

## Low

- **L1 (746 note).** *tardata* agrees with *genua* (neuter plural). *genua* is ge-nu-(a) here, with no consonantal u, unlike 5.432 and 12.905.
- **L2 (749 note).** *veluti siquando* is "just as when", and only literally "as if ever". "As if" alone suggests a comparative condition.
- **L3 (752 note).** The elision list now uses the house form: "Elisions 'ill(e) autem', 'aut(em) insidiis'."
- **L4 (762 note).** Added *excīsūrum* (long -cī-, -sū-) and *mĭnĭtans*, the gloss for the scan-fix.
- **L5 (764–765 `l`).** "for not light or game-prizes are sought, / prizes" rendered *praemia* twice. It is now "for not light or sporting are sought / prizes, but about Turnus's life and blood they contend".
- **L6 (772 note).** Added that *stabat* has -at lengthened at the pause before *huc*, and that there are four spondees.
- **L7 (777 `l` and note).**
  - The Latin vocative "Faune" is now "Faunus".
  - `l` "he said" is now "he says", as the house `l` for *inquit* in every published part.
  - The note now gives the precedents (7.594, 8.439, 11.42).
- **L8 (780 `i`).** "the god's help he called on was not called in vain" is now "called on the god for help with prayers that were not to be in vain".
- **L9 (797 `l`).** "By a mortal was it fitting to be violated, with a wound, a god" split *mortali… volnere* as if *mortali* were a person. It is now "Was it fitting by a mortal wound to be violated, a god". The note already reads "by a mortal wound".
- **L10 (806–807 note).** "*Saturnia*… held to the end" was wrong, since *voltu* ends the line. So was "*submisso… voltu*… framing the line", since *sic dea* opens it. Both are now "split round" or "round" the words they enclose. The stray-mark sentence now says "t keeps it, and l and i carry none here", as in 070.
- **L11 (808 note).** Added *quia*, two short syllables (scan-fix gloss).
- **L12 (810 note).** Added *aeria*, four syllables ā-ĕ-rĭ-ā, not the diphthong.
- **L13 (818 note).** *exosa* is the participle of *exodi*, not of *odi*.
- **L14 (824 note).** *Troas* is now described as long by position here. "the Trojan's Phrygian clothes" is now "Trojans'".
- **L15 (827 note).** Added *Ĭtălā* short I- and *Rōmāna* (scan-fix gloss).
- **L16 (832, rule 5b form).** The note now reads: "The print has no mark after 'furorem' (832), a misprint for a stop (a colon is read here), corrected here: 'do quod vis' begins a new statement." This follows 12.743 *orbes* in 097. `l` and `i` already had the colon.
- **L17 (837 note).** *adiciam* is now explained as ad-ĭ-cĭ-am, the single written i standing for consonantal and vowel i together. The draft's "the i a consonant" was half the story.
- **L18 (838 note).** "the antecedent drawn into the relative clause" was not right. *genus* is the object of *videbis*, set before its relative. The note now says that.
- **L19** is the division-only scan-fixes 788, 792, 803, 829 and 837, listed above.
- **L20** is the 812 confirmation entry, listed above.

## Refused or upheld (no change)

1. **777 *inquit* inside the marks** is upheld as Greenough's habit, not a misprint. This matches 7.594 (aeneid-054), 8.351 and 8.362 (060), 8.439 (061), 9.355 (067), 10.490 (077) and 11.42 (082). Only 12.258 (aeneid-093) treated the same thing as a rule-5b misprint. `t` keeps the print, and `l` and `i` close and reopen round "he says" or "he cried". `review_check.py` exempts 776 from the mark count for this.
2. **806 `veto. ”Sic`** under rule 5b is upheld: `t` as printed, with the stray ” at the head of the 806 unit, and `l` and `i` closing the speech at the end of the 803 unit, as at 9.644, 9.656, 10.298 and 10.335. The note wording is the house formula. Exempted in `review_check.py` (803, 806, and the quoted mark in the 803 note).
3. **832 rule 5 (adding the colon to the source)** was not applied, because the print could not be checked. It is handled under 5b as 12.743 was.
4. **801–802 bracketed lines** are upheld. `l` "lest" and the note's "and let not" are both defensible for *ni* (purpose after *inflectere*, or prohibition).
5. **747 *genua*** keeps the scanner's ordinary reading (see Scansion).
6. **779, 810, 812** and the other lines listed above: the scanner is right.
7. **814 *maiora*, 820 *maiestate*** keep the division ma-io and ma-ies, as house practice at 12.244.
8. **793 *Qua*** as an adverb, with the Latin Library's *quae* noted as a slight difference of sense, is upheld.
9. **786 *Quod* as connecting relative and subject of *licere*** is upheld.
10. **790 *certamina* "an accusative of what they face"** is upheld (after *adsistunt contra*).
11. **752 *mille… vias*, "accusative of the path run (cognate)"** is upheld. It is loose but defensible.
12. **813 *Iuturnam… suasi*, "suadeo usually takes a dative"** is upheld, and is correct.
13. **815 *contenderet*… "a zeugma"** is upheld.
14. **841 *mentem*, both readings given** is upheld.
15. **797 *divom* as an accusative singular, subject of *violari*** is upheld.
16. **842 `i` "Then" for *Interea*** is upheld. It is a scene change, and "Meanwhile" would jar after 841.
17. **Narrative `i` tense** is past throughout outside the simile and the speeches.
18. **Unchanged `i` in Jupiter's first speech (793–806) and Juno's 810–818** was checked for echo and kept, as close to the Latin and not distinctive. This includes "I forbid you to try anything more" and "the one oath that holds the gods above in awe".
19. **"From memory" attributions** all keep their markers. Each was checked for plausibility:
    - Iliad XXII hound and fawn (about 22.189–192);
    - Achilles waving the Greeks back (22.205–207);
    - three circuits (22.165);
    - no ox-hide or beast as prize (22.159–161);
    - Athena returning the spear (22.276–277);
    - Zeus with Athena (22.167–185);
    - Hera swearing by Styx (15.36–38);
    - Livy 1.2.6 on Jupiter Indiges;
    - the Capitoline triad.
    All are plausible.
20. **Cross-references** were checked in the source (listed above) and are right.
21. **Variants.** The drafter notes 773 *in* and 793 *quae*, which is enough. The rest are orthography.
22. **`p` flags** at 746 and 766 are upheld. **`new-renderings.md` "None."** is upheld, since no set piece falls in the part.
23. **No advisory.** The part is chase and dialogue.
24. **`about`** ("let Troy stay fallen, name and all") is not a field the reviewer edits. It is plain and was left alone.

## For the run lead

- **`scan-fixes.json`** now holds 19 new keys, 12.746 to 12.837 as listed, appended after 12.744. Nothing else in the file changed.
- **Rule 5b, for `QUESTIONS.md`/`LOG.md`:** two corrections in the reading text, with `t` as printed:
  - 12.806 `veto. ”Sic` → `veto.” Sic`;
  - 12.832 no mark after *furorem* → a colon.
- **Decisions for the owner:**
  1. The *inquit*-inside-marks practice is inconsistent across published parts: aeneid-093 (12.258) calls it a misprint, and the others call it Greenough's habit. 098 follows the majority.
  2. Many earlier lines keep the scanner's open-long divisions *su-bli-*, *su-bri-*, *a-dlo-*, *a-di-ci-*, *su-pre-* without a fix. Examples are 1.229, 1.254, 1.259, 4.222, 9.740, 10.742, 8.304, 10.182, 11.354 and 6.513. Book XII parts now fix them as they come. A one-time sweep would make the audio consistent.
- **Unchecked, from memory:**
  - the Homeric line numbers above;
  - *excīsūrum* (long ī, from *excīdo*);
  - *Ĭtălā* with a short I in 827 (forced by the metre);
  - the lengthening of *stabāt* at 772 (forced by the metre and parallel to 7.174).
