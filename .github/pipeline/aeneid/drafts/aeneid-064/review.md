# Review — aeneid-064 (Aeneid IX.1–106), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 53 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every cross-reference and every historical or mythological claim. I also checked the drafter's four rule-5b calls (9.22 `vocas. ”Et`, 9.38 `heia! ”Ingenti`, 9.52 `En, ”ait`, 9.77 `musae`), the two bracketed lines (29, 85), the Latin Library variants, the `about` and every attribution made from memory.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington, Servius). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.183, 1.269, 1.402–406, 3.5–6, 3.170, 3.354, 4.569, 4.576–577, 5.657–658, 6.747, 6.800, 7.157–159, 7.209, 7.464, 7.483–486, 7.691, 7.784, 8.100, 8.185, 8.523–529, 9.774–775, 10.76, 10.191, 10.113–115 and 10.619. Three were wrong: 10.76/10.619 (item 13), 8.524–529 (item 14) and 10.113–115 (item 17). For the 9.77 decision I also checked how the print capitalises *Penates* (2.293, 2.717, 8.679) and *nympha*.

**Pass 2** re-read every edited field in full, plus every "framing" claim in the part, and made four more changes (P2-1 to P2-4).

**Scansion.** I hand-scanned all 106 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with mine syllable by syllable.
- **The scanner was wrong on 12 lines**: 8, 9, 26, 34, 39, 41, 55, 68, 69, 81, 97 and 103. None of the twelve was flagged. Each now has a hand entry.
- The one flagged line, **32** (COSTLY 2.1, *alveo*), is right.
- **No half-lines** fall in this part.

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 12 entries apply
- **all 53 units get `sc`**
- all 106 lines pass the validator's metre check
- after the fixes, the scanner report holds only COSTLY 9.32. It is hand-checked right and gets no entry, as at 8.615 and 8.679. It does not block the build.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump` (`indent=1`, `ensure_ascii=False`, no trailing newline, as the drafter's file).
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 53 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- **23 units changed.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break. Speech marks: 6 “ and 6 ” in each of `t`, `l` and `i`, on the same units.
- **Note lengths.** Every note is now 39–140 words. Three notes the drafter left over 140 were trimmed with no loss of substance:
  - unit 13 (9.21–24): 169 words
  - unit 20 (9.37–39): 148 words
  - unit 26 (9.51–53): 150 words

  They lost repeated glosses ('Sequor omina tanta', 'mecum… set off by commas', 'hostis adest… the enemy is here') and the second half of the stock "because t must match the pinned source" clause.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 134 insertions, 0 deletions, trailing newline kept, formatting as before. The new keys follow 8.727, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Severity counts: major 12, medium 6, low 22 (18 in pass 1, 4 in pass 2). Refused or upheld-without-change findings: 18. Scan-fixes entries added: 12.**

## Changes — pass 1

### Major
1–12. **Scansions the scanner got wrong, none flagged.** Each line now has a hand entry with its reason.
- **Initial *Ae-* split (4 lines)**: 9.8, 9.41, 9.81 and 9.97. *Aeneas* is Ae-nē-ās, three syllables. The scanner split A-e each time and got 15, 15, 16 and 15 syllables where the right counts are 14, 14, 15 and 14.
  - 9.8: Ae-nē | ās ur | b(e) et sŏ-cĭ | īs et | clās-sĕ rĕ | lic-ta
  - 9.41: Ae-nē | ās sī | qu(a) in-tĕ-rĕ | ā fōr | tū-nă fŭ | is-set
  - 9.81: Ae-nē | ās clas | s(em) et pĕ-lă | gī pĕ-tĕ | r(e) al-tă pă | rā-bat
  - 9.97: Ae-nē | ās cui | tan-tă dĕ | ō per | mis-să pŏ | tes-tas, with *cui* one syllable
- **Greek *eu* in *Teucri* split (4 lines)**: 9.34, 9.39, 9.55 and 9.68. *Teu-* is one long syllable, as in the entries at 8.136 and 8.161. The right counts are 15, 13, 15 and 14; the scanner had one more each time.
  - 9.34: prō-spĭ-cĭ | unt Teu | cr(i) ac tĕ-nĕ | brās in | sur-gĕ-rĕ | cam-pis
  - 9.39: con-dunt | sē Teu | crī pōr | tās et | moe-nĭ-ă | com-plent
  - 9.55: hor-rĭ-sŏ | nō Teu | crum mī | rān-tŭr ĭ | ner-tĭ-ă | cor-da
  - 9.68: ex-cŭ-tĭ | āt Teu | crōs val | l(o) at-qu(e) ef | fun-dăt ĭn | ae-quum
- **9.9 *Euandri***: scēp-tră Pă | lā-tī | nī sē | dem-quĕ pĕ | tīt Eu | an-drī (14 syllables).
  - *Eu-* is one long syllable, as in the entries at 8.52, 8.100 and 8.185, so this is a spondaic line. *petīt* is the contracted perfect, *petiit*.
  - The scanner split E-u into two short syllables, a dactylic fit with 15.
  - **The drafter's note was also wrong.** It said "scan it E-van-dri, the u as a consonant", and `l` had the present "seeks". See item 18.
- **9.26 *dives… pictaï***: dī-vĕs ĕ | quum dī | vēs pic | tā-ī | ves-tĭs ĕt | au-rī (14 syllables).
  - The scanner had the right count but the wrong quantities. It made the first *-ves* and the *e-* of *equum* long, and the *-tā-ī* of the old genitive short.
  - *-āī* is long-long, as *aulāī* at 3.354 (au-lā | ī mĕ-dĭ…).
- **9.69 *adiuncta***: the i after the prefix is consonantal (ad-iunc-ta, three syllables), as *adiungere* at 8.13. The line is clas-sem | quae lă-tĕ | rī cas | trōr(um) ad | iunc-tă lă | tē-bat (14 syllables). The scanner read a-di-unc-ta, a fit with 15.
- **9.103 *Galatea***: four syllables, Gă-lă-tē-ă (Greek -εια), with *sĕcant* short in its first syllable. The line is et Gă-lă | tē-ă sĕ | cant spū | man-tem | pec-tŏ-rĕ | pon-tum (15 syllables). The scanner ran *-tea* together by synizesis and made *se-* long, a fit with 14.

### Medium
13. **Unit 1 (9.3–4), Pilumnus.** The note said Pilumnus was Turnus's "great-grandfather", citing 10.76 and 10.619. The two lines disagree with that and with each other: 10.76 has *avus* ("grandfather") and 10.619 has *quartus pater* ("father in the fourth degree"). The note now gives both and says the generation is left loose.
14. **Unit 12 (9.20–21), a false cross-reference.** "As at Jupiter's thunder in 8.524–529" was wrong. That sign is Venus's: *ni signum caelo Cytherea dedisset aperto* (8.523). It is lightning and thunder from a clear sky, not a parting sky. The note now reads "like the lightning and thunder from a clear sky that Venus sends as her sign at 8.523–529".
15. **Unit 22 (9.41–43), a false label.** The note had "'neu… auderent… neu (crederent)'", which makes *credere* stand for a finite verb. Both *struere* and *credere* are infinitives depending on *auderent*, as `l` already showed ("neither to draw up should they dare… nor to trust"). The note now says so, with *neu… neu* (= *neve… neve*) doing the work of *ne*.
16. **Unit 37 (9.77–78), rule 5b refused for *musae*.** See R4. The note no longer opens "The print has 'musae', a misprint for 'Musae', corrected here". It now says the print has a small letter here, against *Musa* at 1.8 and 10.191 and *Musis*/*Musarum* at 9.774–775. It explains that the print's capitals for collective divine names vary (*penatis* 2.293 beside *Penatis* 2.717, *penatibus* 8.679) and that the sense is the same either way, so the print is kept. `l` and `i` already wrote "Muses", which is ordinary English and needs no change.
17. **Unit 52 (9.104–106), a false cross-reference.** "The three lines return word for word at 10.113–115" was wrong. 10.113 begins *Fata viam invenient.* Only 104b–106, from *Stygii* to *Olympum*, recur there, after Jupiter's speech to the council. The note now says so.
18. **Unit 4 (9.8–9), *petit* and *Euandri*.**
    - **`l`**: "seeks" now reads "has sought". The metre needs *petīt* long, so it is the contracted perfect, and `i` already had "has… gone to seek".
    - **Note**: the false "E-van-dri, the u as a consonant" is replaced by "with 'eu' one long syllable, Eu-an-dri (as at 8.100 and 8.185)". It adds the perfect *petīt* and the spondaic fifth foot. This agrees with the 9.9 entry.

### Low
19. **Note 9.10–11**: "Corythus… (later Cortona)" now reads "(usually identified with the later Cortona)". This is a hedge, because the identification is traditional rather than certain.
20. **Note 9.16–17**: added "The second line all but repeats 1.406, Aeneas calling after the departing Venus". This was checked against the source: *adgnovit, tali fugientem est voce secutus*.
21. **Note 9.25–26**: "'campis… apertis'… framing the line" was wrong, since *campis* is the third word. See P2-1 for the final wording.
22. **Note 9.25–26**: "pic-ta-ī" now reads "pic-tā-ī, both the a and the i long", which agrees with the 9.26 entry.
23. **`i` 9.27–29**: "in the middle of the column rode Turnus" added a verb the Latin does not have. It now reads "was Turnus".
24. **`i` 9.30–32**: "So the deep Ganges moves in silence…" read as if the river were the thing compared, with "So" meaning "in this way". It now reads "It was as the deep Ganges moves in silence…".
25. **Note 9.30–32**: the unhedged "seven streams belong more properly to the Nile… and Virgil lends the number to the Ganges" now reads "seven streams sound more like the Nile, whose seven mouths were proverbial ('septemgemini… Nili', 6.800); the usual view is that Virgil lends the number to the Ganges".
26. **Note 9.33–34**: "'campis'… dative with 'insurgere'" now adds "(or ablative of place)", since both readings are possible.
27. **`l` 9.48**: "also at the city" now reads "and at the city". The note glosses *et* as "and (so)", and "also" misread it.
28. **Note 9.49–50**: "'maculis… albis'… framing the clause" was wrong, since *albis* is not last. It now reads "enclosing 'quem Thracius'".
29. **Note 9.51–53, the fetial spear**: added "(Livy 1, from memory)". The claim is Livy 1.32 as I remember it, and it is kept.
30. **Note 9.59–60, the Iliad 12 model**: "on the model of Homer's lion… (Iliad 12, of Sarpedon at the Greek wall)" now reads "commentators compare Homer's hungry lion going for the sheepfold (Iliad 12, of Sarpedon attacking the Greek wall, from memory)". The Sarpedon simile is real (Iliad 12.299 ff. as I remember it), but calling it *the* model is too strong. The wolf at the fold has other Homeric and Apollonian parallels.
31. **Note 9.59–60**: "'pleno… ovili'… framing 'lupus'" now reads "enclosing 'lupus insidiatus'".
32. **`l` 9.67**: "an approach" now reads "approaches", because the note rightly takes *aditus* as accusative plural.
33. **Note 9.73–74**: "'facibus… atris'… framing the line" was wrong, since *facibus* is the third word. It now reads "enclosing 'pubes accingitur'".
34. **Note 9.85–87**: "Without it the sentence still stands, 'lucus… fuit'…, though 'mihi' goes with it" was confusing, because *mihi* is in the bracketed line itself. It now reads "though it loses 'mihi', which makes the wood hers".
35. **Note 9.101–103, the Iliad 18 list**: added "from memory" to "(Iliad 18)". As I remember it, Doto is at 18.43 and Galateia at 18.45.
36. **Note 9.101–103**: added "'Galatea' is four syllables, Gă-lă-tē-ă", which agrees with the 9.103 entry.

These are 18 numbered low items. Items 21 and 22 touch the same note but are counted separately.

## Changes — pass 2
- **P2-1 (low), note 9.25–26**: my own "spanning the line" (item 21) was still inexact. It now reads "set wide apart in the line".
- **P2-2 (low), note 9.49–50**: "'cristaque… rubra'… framing the rest of the line" was wrong, since *crista* is the third word. It now reads "enclosing 'tegit galea aurea'".
- **P2-3 (low), note 9.67–68**: "'Qua… ratione'… framing 'temptet aditus'" was wrong, since *aditus* follows *ratione*. It now reads "enclosing 'temptet'; 'temptet aditus', 'is he to try approaches'", which also agrees with item 32.
- **P2-4 (low), note 9.78**: "'Tantos… ignes'… framing the line" was wrong, since *avertit?* opens line 78. It now reads "enclosing 'ratibus quis depulit'".

Pass 2 also re-checked every other "framing" claim in the part (9.5, 9.14–15, 9.16–17, 9.33, 9.36, 9.47, 9.65–66, 9.67, 9.75–76, 9.80–83, 9.91–92, 9.95, 9.101–103, 9.104–105). All are right.

## Scan-fixes entries added (12)
These are appended after 8.727 in line order:
- **Initial *Ae-* (4)**: 9.8, 9.41, 9.81 and 9.97
- **Greek *eu* in *Teucri* (4)**: 9.34, 9.39, 9.55 and 9.68
- **Greek *eu* in *Euandri*, a spondaic line (1)**: 9.9
- **Wrong quantities, same count (1)**: 9.26 (*dīvĕs ĕquum*, *pictāī*)
- **Consonantal i after a prefix (1)**: 9.69 *adiuncta*
- ***Galatēa*, no synizesis (1)**: 9.103

Each entry matches its line's words under `WORD_RE`. Each has six feet, five –⏑⏑/–– feet then –×, 13–15 syllables and one ×. Each `why` states the count, and each count was checked by script.

## Hand-scan notes on the special lines (scanner right, no entry)
- **9.32, flagged COSTLY 2.1, right**: cum rĕ-flŭ | it cam | pīs et | iam sē | con-dĭ-dĭt | al-veo (14 syllables). *alveo* has two syllables by synizesis, as the note says.
- **9.45 *obiciunt***: the scanner divides it o-bi-ci-unt, with the same quantities as the right ob-ji-ci-unt (– ⏑ ⏑ –). This is cosmetic only, so there is no entry (QUESTIONS item 37; 063 R7). The note's "ob-yi-ci-unt" is right.
- **9.50 *galea aurea***: this is elision, not synizesis. pōr-tăt ĕ | quūs crīs | tā-quĕ tĕ | gīt gă-lĕ | (a) au-rĕ-ă | rū-bra (16 syllables). The scanner agrees, and the note's "gale(a) aurea" is right.
- **9.38 *heia***: hōs-tĭs ă | dēst hē | (ja) In-gen | tī clā | mō-rĕ pĕr | om-nis. The final -a elides across the speech mark. The scanner agrees, and the note is right.
- **9.97 *cui***: one syllable, given in the entry.
- **9.77 *Teucris***: Teu- is one syllable, and the scanner is right here.
- **Hiatus**: none in this part.
- **Other quantities checked**:
  - *Īrim* (2); *Pīlumnī* (4); *Thaumantiăs* (5); *Cŏrўthī* (10); *Lȳdorum* (11); *Messāpus* and *cŏercent* (27); *Tyrrhīdae* (28, the metre's)
  - *nĭgro* lengthened before *gr* (33); *Căīcus*, three syllables (35); *cālīgine* (36); *intĕrĕā* with a long final (41)
  - *iăculum*, with initial consonantal i and *et* long before it (52); *bālātum* (62); *Rŭtŭlo* (65); *pīnū* (72); *Volcānus* (76)
  - *Iŏvem* (83); *ōlim* (99); *vēxerit* (100); *ēripiam* (101); *Nērēĭă* (102); *vŏrāgine* (105)

## Refused or upheld findings
- **R1 — 9.22 `vocas. ”Et`**: **upheld** as a rule-5b misprint. The pattern is the same as 7.560, 7.599, 8.404, 8.443 and 8.583 (QUESTIONS items 52–56). The unit correctly runs on to the end of the narrative sentence.
- **R2 — 9.38 `heia! ”Ingenti`**: **upheld** on the same grounds.
- **R3 — 9.52 `En, ”ait`**: **upheld** on the same grounds, the slip of 7.68 and 8.113 (closing mark joined to *ait*/*inquit*).
- **R4 — 9.77 lowercase `musae`**: **not upheld as a misprint.** The print is kept with no misprint opening, and the note flags it (item 16). My reasons:
  - **Rule 5b needs a clear error.** A capital on a divine name is not a sense matter. The reading is the same, and *musa* is also a common noun in Latin.
  - **The print's capitals here are loose.** It has *penatis* (2.293) beside *Penatis* (2.717), *penatibus* at 8.679, and *nympha*/*Nympha*. The 063 review already treated 8.679 *penatibus* as "the print's inconsistency, not a misprint" (063 R16).
  - **Item 49 points the same way.** It kept the doubtful capital at 7.623 as printed, because a slip could not be told from the print's habit. That is the case here too.
  - **This is unlike the lowercase-after-a-full-stop calls of item 43**, where the stop itself demands the capital.
  - If the owner rules otherwise, only the opening of the note changes.
- **R5 — COSTLY 9.32**: hand-checked right, so no entry was made.
- **R6 — 9.45 *obiciunt***: a cosmetic division with the right quantities, so no entry was made (item 37).
- **R7 — Brackets**: both bracketed lines are noted. 9.29 is noted in unit 15 (the Latin Library omits it, and it repeats 7.784, checked). 9.85 is noted in unit 42 (the Latin Library prints it). Both are kept inside [ ] in `t`, `l` and `i`.
- **R8 — Latin Library variants**: 6 *divom*, 16 *Adgnovit*, 26 *pictaï*, 40 *optumus*, 41 *siqua* and 46 *expectant* are orthography. The notes name Greenough's spelling as his, which is harmless.
  - 54 *clamorem* changes the picture slightly and is rightly noted.
  - 78 *ignis* is morphology and need not have been noted. "The same word" is harmless, and the note is kept.
- **R9 — Note 9.1–3, "Saturnia… the title used when her old grudge is at work"**: kept. It is interpretive but standard (cf. 1.23).
- **R10 — Note 9.59–61, *nocte super media* "'super' as a preposition after its noun"**: kept. It is Conington's way of taking it, as I remember, and the sense "past midnight" is not in doubt.
- **R11 — Note 9.38 *heia* "its i is a consonant, he-ya"**: kept. It is right, and it agrees with the scanner's *he–ia*.
- **R12 — Note 9.13 "Iris's speech ends, and Greenough closes the mark"**: kept. The mark is in the print at 13.
- **R13 — `i` echoes.** I read every `i` for distinctive echoes of the well-known published versions and found none that needed changing.
  - "loaded/burdened heaven with his vows", "now is the time to call for horses", "cut a vast bow beneath the clouds" and "made all Olympus quake" are literal renderings of the Latin, not borrowed turns, and are kept.
  - The only `i` changes (items 23 and 24) were for accuracy.
- **R14 — Note 9.10–11, Etruscans from Lydia**: kept. "Were believed to have come from Lydia" is hedged and right. It is Herodotus 1.94 as I remember it.
- **R15 — Note 9.5, Hesiod's Theogony (Thaumas and Electra as Iris's parents)**: kept. It is right as I remember it (Theogony 265–266), and it is listed under unchecked attributions.
- **R16 — Note 9.80–83, Cybele = Rhea, named from Berecyntus**: kept.
  - Berecyntus as a Phrygian mountain sacred to Cybele is in L&S.
  - The identification with Rhea, Jupiter's mother, is ancient, and the poem itself makes her Jupiter's mother (*Filius huic*, *genetrix*).
- **R17 — Note 9.49–50, Thracian horses and Rhesus**: kept. Rhesus's horses are the famous Thracian ones of Iliad 10.
- **R18 — Note 9.104–106, Zeus's nod shaking Olympus (Iliad 1)**: kept. It is Iliad 1.528–530 as I remember it.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading. All three are closing marks joined to the next word, as in items 52–56:
  - 9.22 `vocas. ”Et`
  - 9.38 `heia! ”Ingenti`
  - 9.52 `En, ”ait`
- **Kept as printed, not a misprint**: 9.77 lowercase `musae`. The print capitalises the Muses elsewhere, but its capitals for collective divine names vary (*penatis*/*Penatis*, 8.679 *penatibus*), and the sense is the same either way. This follows item 49 and 063 R16. If you rule capitals on proper names to be misprints, only the opening of the note on 9.77 changes.
- **Scansion**: the build report should list only COSTLY 9.32, which is hand-checked right.
  - 12 entries: 9.8, 9.41, 9.81 and 9.97 (*Aeneas*); 9.34, 9.39, 9.55 and 9.68 (*Teucri*); 9.9 (*Euandri*, a spondaic line with *petīt*); 9.26 (*dīvĕs ĕquum*, *pictāī*); 9.69 (*adiuncta*); 9.103 (*Galatēa*).
  - The one choice that could be argued is 9.9. Like the scanner's E-u split, the 14-syllable spondaic reading needs *petīt*. I chose it for consistency with *Eu-* as one syllable at 8.52, 8.100 and 8.185.
- **Unchecked attributions, all from memory**:
  - Hesiod, Theogony (Iris's parents)
  - Herodotus 1 (Lydians), which the note does not name
  - Iliad 12 (Sarpedon's lion), Iliad 18 (Doto, Galateia), Iliad 1 (the nod) and Iliad 10 (Rhesus's horses)
  - Livy 1 (the fetial spear)
  - Servius and Conington on the Ganges's seven streams
  - Cortona for Corythus
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
