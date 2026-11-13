# Review — aeneid-061 (Aeneid VIII.407–519), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 56 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's rule-5b calls (8.443 `moras. ”Nec`, 8.447 `Ingentum`, 8.512 `indulgent`, lowercase after a stop at 489, 496, 510 and 514, 8.498 capital `Signaque`, 8.499 the opening mark), every attribution marked "(from memory)", and the `about`.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.1, 1.52, 6.46, 6.52, 7.98, 7.121, 7.648, 7.649–654, 8.169–171, 8.351, 8.359–368, 8.404, 8.405–406, and the internal pointers 421, 425, 446, 466, 470, 477, 480, 502 and 503. All are right.

**Pass 2** re-read every edited field in full and made four more changes (P2-1 to P2-4).

**Scansion.** I hand-scanned all 113 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with my scansion syllable by syllable.
- **The scanner was wrong on 14 lines**: 407, 413, 415, 428, 440, 456, 463, 465, 469 (half-line, UNRESOLVED), 484, 496, 502, 513 and 517.
  - Only 469 (UNRESOLVED) and 517 (COSTLY 2.0) were flagged. The other twelve were wrong with no flag.
  - Each now has a hand entry.
- **The other flagged line is right**: 515 (COSTLY 2.1) gets no entry (R7).

Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule:
- full lines: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×
- the half-line 469: feet numbered 1..k with k < 6, one ×, and a reason beginning "Half-line"

Each `why` gives a syllable count, and a script checked that count against its entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 14 entries apply
- **all 56 units get `sc`**. Without the 469 entry, unit 30 (`Rex prior haec:`) got none, and the build would refuse.
- all 113 lines pass the validator's metre check
- the scanner report keeps only the COSTLY flag on 515, which is confirmed right

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump`.
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 56 units. I checked this by script against a fresh run of `make_units.py` into the scratchpad, whose output was identical to the drafter's `units.json` before any edit.
- `title`, `titleEn` and `part` are unchanged. `about` has one change (item 50). 27 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- The tiling of `t` against the pinned source was re-checked, and the sha256 matches `parts.json`.
- **Note lengths.** Three drafter notes were over 140 words: unit 0 (187), unit 39 (152) and unit 46 (187). All are now trimmed. Every note is now 28–140 words.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 157 insertions, 0 deletions, trailing newline kept, formatting as before (`indent=1`, no ASCII escaping). The new keys come after 8.397, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Speech marks.** These were checked in `t`, `l` and `i`. There are two speeches, plus a quotation inside the second:
- **Vulcan, 439–443**: “ on unit 12, ” on unit 15.
- **Evander, 470–519**: “ on unit 31, ” on unit 55.
- **The soothsayer, 499–503**, quoted inside Evander's speech: `l` and `i` use single marks ‘ ’, opened in unit 46 and closed in unit 47.
- `l` and `i` each have 3 “ and 3 ”, because unit 12 puts "he says"/"he said" outside the marks.
- `t` has 3 “ and 2 ”. The print opens the soothsayer's words at 499 and never closes them. **The validator will warn about this, which is expected.**

**Severity counts: major 14, medium 3, low 36 (32 in pass 1, 4 in pass 2). Refused findings: 23. Scan-fixes entries added: 14.**

## Changes — pass 1

### Major
1–14. **Scansions the scanner got wrong.** Each line now has a hand entry with its reason.
   - **Initial Ae- split in two**:
     - **8.463 *Aeneae***: Hos-pĭ-tĭs | Ae-nē | ae sē | d(em) et sē | crē-tă pĕ | tē-bat (14 syllables). The scanner had 15.
     - **8.465 *Aeneas***: Nec mĭ-nŭs | Ae-nē | ās sē | mā-tū | tī-nŭs ă | gē-bat (14). The scanner had 15.
     - **8.496 *Aenea***: hīs ĕ-gŏ | t(e) Ae-nē | ā duc | tō-rem | mī-lĭ-bŭs | ad-dam (14). The scanner had 15.
   - **Greek eu split — 8.513 *Teucrum***: in-grĕ-dĕ | r(e) ō Teu | cr(um) at-qu(e) Ĭ-tă | lum for | tis-sĭ-mĕ | duc-tor (15). The scanner split Te-u and had 16.
   - **Consonantal i or u after a prefix**:
     - **8.413 *coniugis***: con-iŭ-gĭs | et pos | sit par | vōs ē | dū-cĕ-rĕ | nā-tōs (14). The scanner read co-ni-u-gis and also made *parvōs* and *ē-* short, a fit with 15.
     - **8.502 *subiungere***: nul-lī | fās Ĭ-tă | lō tan | tam sub | iun-gĕ-rĕ | gen-tem (14). The scanner read su-bi-un-ge-re, a fit with 15.
     - **8.517 *adsuescat*** (COSTLY 2.0): ad-suēs | cat prī | mīs et | tē mī | rē-tŭr ăb | an-nis (13). The scanner read ad-su-es-cat and made *te* and *mi-* short, a fit with 14. The precedents are 6.832 and 7.33.
     - **8.428 *deicit***: dē-ĭ-cĭt | in ter | rās pars | in per | fec-tă mă | nē-bat (14). The scanner read *dei-* as one syllable and made *-cit* long before *in*, a fit with 13.
   - **Synizesis preferred to the ordinary reading**:
     - **8.407 *quies***: Ind(e) ŭ-bĭ | prī-mă quĭ | ēs mĕ-dĭ | ō iam | noc-tĭs ă | bāc-tae (16). The scanner read *quies* as one syllable and *prima* with a long *-a*, a fit with 15.
     - **8.484 *ipsius***: ef-fĕ-ră | dī că-pĭ | t(i) ip-sī | us gĕ-nĕ | rī-quĕ rĕ | ser-vent (16). The scanner read *ip-sius* as two syllables and made *ge-* and *ne-* long, a fit with 15.
   - **Wrong quantities with the right syllable count**:
     - **8.415**: mol-lĭ-bŭs | ē strā | tīs ŏ-pĕ | r(a) ad fā | brī-lĭ-ă | sur-git (15). The scanner made *strā-* and *-tīs* short and *ŏ-*, *pĕ-* long.
     - **8.440 *Cyclopes***: Aet-nae | ī Cȳ | clō-pĕs ĕt | hūc ad | ver-tĭ-tĕ | men-tem (14). The scanner made *Cy-* and *clō-* short and *-pĕs* and *ĕt* long. The precedents are 3.644 and 8.424.
     - **8.456 *matutini***: et mā | tū-tī | nī vŏ-lŭ | crum sub | cul-mĭ-nĕ | can-tus (14). The scanner made *mā-* and *tū-* short and *vŏ-* and *lŭ-* long.
   - **Half-line — 8.469 *Rex prior haec:*** (UNRESOLVED): Rēx prĭ-ŏr | haec (– ⏑ ⏑ | ×), 4 syllables. It is entered as at 7.760 and 8.41, with a reason beginning "Half-line".
     - Without this entry, unit 30 gets no `sc` and the build refuses.
     - The unit holds only this line, so no carrier entries are needed.

### Medium
15. **Note 447–449, a false label.** It said "'contra' after its noun". In *omnia contra tela* the noun *tela* follows *contra*. It now reads "'contra' between 'omnia' and its noun 'tela'".
16. **Note 515–517, a false count.** It said *adsuescat* governs "three infinitives" and then listed *tolerare militiam*, *grave Martis opus* and *tua cernere facta*. *grave Martis opus* is a second object of *tolerare*, not an infinitive. The note now says two infinitives: *tolerare*, with the objects *militiam* and *grave Martis opus*, and *cernere*.
17. **`i` 431–432, a reversed sense.** It read "and wrath that follows in the track of the flames". In *flammisque sequacibus iras* it is the flames that pursue. It now reads "and wrath with its pursuing flames", which matches `l`.

### Low
18. **`i` 407–410**: "when the first sleep has done its work and banished sleep" had "sleep" twice, and a present perfect against the main verb "rose" (unit 2). It now reads "when the first rest of the night had driven sleep away, … at the hour when a woman…".
19. **Note 407–410**:
    - It was trimmed from 187 to 140 words (P2-1).
    - It added "'quies' is two syllables, qui-ēs", which agrees with the 407 entry.
    - Repeated glosses were cut. No claim was altered.
20. **`l` 417**: "with smoking steep rocks" made "steep" qualify the rocks. It now reads "steep with smoking rocks".
21. **Note 416–417**: "'ardua'… with 'fumantibus… saxis'… ablative of description" was wrong. An ablative of description qualifies a noun, not an adjective. It now reads "ablative of respect with 'ardua'".
22. **Note 418–422**: "'Cyclopum exesa caminis'… framing the line" was wrong, since the phrase fills only the second half of 418. It now reads "'Cyclopum… caminis' enclosing 'exesa'".
23. **Note 418–422, missing elisions.** The elision list left out *validiqu(e) incudibus* (419) and *Chalyb(um) et* (421); both are added. To make room, two glosses were cut: "Virgil keeps the name for the caverns here" and "breathing like a living thing under the bellows".
24. **`l` 423**: "from heaven descends on high" attached *ab alto* to the verb. It now reads "from high heaven descends".
25. **`l` 424**: "in the vast Cyclopes cave" read as a possessive. It now reads "Iron were working, in a vast cave, the Cyclopes,".
26. **Note 424–425**:
    - "Virgil's third is his own" is an unverifiable claim of invention. It now reads "Virgil's third, Pyragmon, takes the place of Arges".
    - It added "the first '-que' scanned long before 'St-'", which the scanner's correct fit has.
27. **Note 426–428**:
    - "'informatum erat'… split by 'manibus iam parte polita'" left out *fulmen*, which also stands between. It now reads "split across the line".
    - It added "'deicit'… three syllables, dē-i-cit", which agrees with the 428 entry.
28. **Note 429–430**: "(so the ancient commentators explain it)" was an unchecked attribution. It is now hedged "(…, from memory)".
29. **Note 435–438, a missing elision.** *serpent(um) auroque* (436) is added. To stay within 140 words, "(Minerva)" and "'bringing horror'" were cut.
30. **Unit 12 (439–440)**:
    - **`i`**: "take off the work you have begun" now reads "carry off the work you have begun" (P2-2).
    - **Note**: it added "'Cy-clō-pĕs', the Greek plural '-es' short", which agrees with the 440 entry.
31. **`l` 442**: "now of all art your master" made art the master *of you*. It now reads "now of all masterly art", which matches the note ("'magistra' used as an adjective").
32. **Note 449–451**: "No elisions" was false, since 450 has *redduntqu(e) alii*. It now reads "Elision 'redduntqu(e) alii'".
33. **Note 454–456**: "'Aeoliis… oris'… framing the clause" was wrong, since *Haec pater* comes first. It now reads "enclosing 'properat dum Lemnius'".
34. **`l` 465**: "Aeneas himself… was stirring" read *se* as intensive. It now reads "No less Aeneas, in the morning, was bestirring himself."
35. **Note 470–473**: "'victas' with both nouns" was wrong for agreement: *victas* is feminine and agrees with *res*. It now reads "'victas' agreeing with 'res' and understood with 'regna'".
36. **`l` 474**: "and the wall echoes round with arms" made *murum* the subject. It now reads "and the wall makes ring round with arms" (the Rutulian is the subject).
37. **Note 478–480**: "'Lydia… gens'… framing the next clause" now reads "split across the line-end".
38. **Unit 38 (484)**:
    - **`l`**: "for his head itself" misconstrued *ipsius*, which is a genitive. It now reads "for the head of himself and for his race".
    - **Note**: it added "'ipsius' has three syllables, ip-sī-us", which agrees with the 484 entry (placed per P2-3).
39. **Note 485–488**: it was trimmed from 152 to 135 words. Only restatements were cut ("a step up from 'quid memorem': this is what he did" now reads "going a step further"), and no claim was altered.
40. **`i` 487**: "a torture of his own devising" added an idea not in *tormenti genus*. It now reads "a form of torture".
41. **`l` 489**: it began "but", lowercase, against the note's "l and i begin with a capital". It now reads "But".
42. **`l` 493**: "by Turnus was defended, his host's, arms" made *Turni* an agent. It now reads "of Turnus was defended, his host, by the arms".
43. **Note 494**: "'furiis… iustis'… framing the line" was wrong, since *Ergo omnis* comes first. It now reads "enclosing 'surrexit Etruria'".
44. **Note 498–502**:
    - It was trimmed from 187 to 139 words.
    - The corrected reading was given as "'fata canens: “O Maeoniae'", which silently changed the print's comma to a colon. It now reads "'fata canens, “O Maeoniae'".
45. **`l` 501**: "and with deserved fires Mezentius with wrath" had *ira* translated twice ("fires… with wrath"). It now reads "and with deserved kindles Mezentius wrath".
46. **Note 505–507**: "'Ipse… Tarchon'… framing the sentence" was wrong, since the sentence runs on to 507. It now reads "framing 505–506".
47. **Note 511–513**:
    - The elision list left out *ingreder(e) o*; it is added.
    - It added "'Teu-' is one syllable", which agrees with the 513 entry.
48. **Note 515–517**: "'sub te… magistro'… ablative absolute in effect" was a false label: with *sub* it is a prepositional phrase. It now reads "'magistro' in apposition to 'te'".
49. **Note-length bookkeeping**: units 0, 39 and 46 were brought within 140 words (items 19, 39 and 44). This is counted once, as the validator WARN cleared.
50. **`about`**: "their king Tarchon" is not supported by the passage, which never calls him *rex*. It now reads "their leader Tarchon".

Items 18–50 make 33 numbered low items. Item 49 is bookkeeping only and is not counted separately. Items 30 and 38 each count once. That gives the 32 pass-1 lows.

## Changes — pass 2
- **P2-1 (low), note 407–410**: it was still 141 words after the trim. "'on whom it has been laid'" now reads "'on whom it is laid'" (140).
- **P2-2 (low), `i` 439–440**: item 30's "Put everything away… clear away the work" said "away" twice. It now reads "carry off the work".
- **P2-3 (low), note 484**: the inserted scansion remark had broken the sentence on *capiti ipsius*. It was moved to its own sentence before the elision.
- **P2-4 (low), note 498–502**: after the trim, "l and i give his words in single marks" was ambiguous (Evander's or the soothsayer's). It now reads "give the prophecy in single marks".

## Scan-fixes entries added (14)
These are appended after 8.397 in line order:
- **Initial Ae- (3)**: 8.463, 8.465 and 8.496
- **Greek eu (1)**: 8.513
- **Consonantal i/u after a prefix (4)**: 8.413, 8.428, 8.502 and 8.517 (8.517 was flagged COSTLY)
- **Synizesis preferred (2)**: 8.407 and 8.484
- **Wrong quantities, same count (3)**: 8.415, 8.440 and 8.456
- **Half-line (1)**: 8.469 (UNRESOLVED)

Each entry matches its line's words under `WORD_RE`. Each full line has six feet, five –⏑⏑/–– feet then –×/⏑×, 13–16 syllables and one ×. The half-line has feet 1–2 and one ×, with a reason beginning "Half-line".

## Hand-scan notes on the special lines (scanner right, no entry)
- **8.515 (COSTLY 2.1), right**: Pal-lan | t(a) ad-iun | gam sub | tē tŏ-lĕ | rā-rĕ mă | gis-tro (14 syllables). The scanner divides *a–diun*, a cosmetic division with the right quantities, as with *co–niunx* (060 R6, QUESTIONS item 37).
- **Greek eu**:
  - *Euandrum* (455) and *Teucrorum* (470) are right.
  - *Teucrum* (513) is fixed.
- **Initial Ae-**:
  - *Aeoliam* (416), *Aetnaea* (419), *Aetnaei* (440) and *Aeoliis* (454) are right, each with long Ae- and a short following vowel (Ae-ŏ-lĭ-, Aet-naē-).
  - *Maeoniae* (499) is right, and so are *aegida* (435), *aes* (445), *aera* (451), *aedibus* (468) and *longaevus* (498).
  - Fixed: 463, 465 and 496.
- **Consonantal i**:
  - *iuxta* (416), *iam*, *iungunt* (467), *Troiae* (471), *iugis* (480), *iungebat* (485), *iustis* (494), *iuventus* (499), *iustus* (500), *cuius* (511, cuj-jŭs) and *adiungam* (515) are right.
  - Fixed: *coniugis* (413), *deicit* (428), *subiungere* (502).
- **Synizesis**:
  - *cui* (409), *huic* (466, 518) and *deinde* (481, two syllables) are right.
  - Fixed: *quies* (407) and *ipsius* (484).
  - *coeptos* (439) is right with *coe-* as one syllable (as *coeptis*, Georgics 1.40).
- **Hiatus**: none in the part. *O Maeoniae* (499) is not elided; the interjection *O* is never elided, and the scanner keeps it.
- **Other quantities checked**:
  - *Sīcănium* (416), *Lĭpărēn* (417), *Chălybum* (421)
  - *Cy-* long by position before *cl* (418, 424, 440)
  - *exēsa* (418), *strīdunt* (420), *fornācibus* (421)
  - *-quĕ* lengthened before *St-* (425)
  - *cōnexos* (437), *ōcius* (444)
  - *volnĭfĭcus* and *chălybs* closed (446)
  - *lacū* (451), *Tegĕaeum* (459), *panthērae* (460), *ērilem* (462), *resīdunt* (467)
  - *Agyllīnae* (479), *insēdit* (480)
  - *sănĭē*, *tābō* (487)
  - *ăgros* long by position in the sixth foot (492)
  - *Ĕtrūria* with a short E (494), but *Ētrusca* long by position before *tr* (503)
  - *praetereā* (514), *mīlitiam* (516)
  - *Arcădăs* (518), *suō* (519)
  - *merĭtā* elided (501)

## Refused findings
- **R1 — 8.443 `moras. ”Nec`**: **upheld**. `t` stays as printed, `l`/`i` close Vulcan's speech after *moras*, and the note opens with the print's reading. The mark cannot be split from *Nec*, so unit 15 carries *Nec plura effatus*. This follows 7.560, 7.599 and 8.404.
- **R2 — 8.447 `Ingentum`**: **upheld** as a rule-5b misprint for *Ingentem*. No form *ingentum* agrees with *clipeum*, and the Latin Library has *ingentem*. The scansion is the same, so no entry is needed.
- **R3 — 8.512 `indulgent`**: **upheld** as a misprint for *indulget*. A plural verb cannot take the singular *fatum*, and the Latin Library has *indulget*. The scansion is the same.
- **R4 — Lowercase after a stop** at 489 `at`, 496 `his`, 510 `natum` and 514 `hunc`: **upheld**. This is consistent with 8.9, 8.79, 8.124, 8.217, 8.285, 8.310 and 8.366. The general ruling asked in QUESTIONS item 43 is still open.
- **R5 — 8.498 capital `Signaque` mid-sentence**: **upheld** as a rule-5b note, consistent with 7.323 *Horrenda* (item 46). The sense is unaffected, so the owner may prefer to keep such capitals silently, as for *Siqua* after a colon (item 47).
- **R6 — 8.499 opening mark before `fata canens`**: **upheld** as misplaced. The soothsayer's words begin at *O*, and *fata canens* is Evander's narrative.
  - This is the same pattern as 6.46, 6.52 and 7.121: a mark set at the head of the line holding the verb of speaking (the pattern ruling asked in item 44).
  - The corrected reading was adjusted (item 44 of this review).
- **R7 — 8.515 (COSTLY 2.1)**: the fit is right, with a cosmetic *a–diun* division, so there is no entry. It stays in the build's scanner report.
- **R8 — `t` marks**: `t` has 3 “ and 2 ”, which is correct for this print. The soothsayer's quotation is never closed. The validator's WARN is expected.
- **R9 — Note 423, *Hoc* = *huc***: kept. L&S lists *hoc* as the old form of *huc* with this passage (from memory).
- **R10 — Note 429–430, "Twelve rays in all"**: kept. The Latin gives *tris* only once for *ignis et alitis austri*. The reading three-each (twelve) is the usual one, and `i` follows it.
- **R11 — Note 411–413, "The colon closes the simile"**: kept. Strictly, the comparison is the time-clause, but the statement is not false.
- **R12 — Note 426, "these men's hands" for *his… manibus***: kept as a translation, not a label. *His* agrees with *manibus*.
- **R13 — Note 457, "you have seen this with 'nudus membra'"**: kept. It is the related accusative of the part concerned (A&G 397), although the construction there is with an adjective.
- **R14 — Note 481–482, "'superbo imperio' framing the line-break"**: kept. It is true, since the words stand on either side of it.
- **R15 — Note 416, "home of Aeolus… (1.52)"**: kept. 1.52 names *Aeoliam*, and Lipari as its chief island is the usual identification.
- **R16 — `i` 443, "Make haste, no delay!"**: kept. It is plain and our own.
- **R17 — `i` 495, "with war on the spot"**: kept. It is awkward, but it is accurate to *praesenti Marte*.
- **R18 — Note 407, *noctis abactae* as "driven on"**: kept. "Driven off", i.e. half spent, is the other account, and the time, midnight, is the same.
- **R19 — Note 510, "'Sabellus' an Oscan people's name used for Sabine"**: kept. It is defensible, and L&S treats *Sabellus* as poetic for Sabine.
- **R20 — The `i` echo check**: I found no distinctive echo of a published version. Units 13, 14, 39, 42 and 53 were checked with care, and their wording is literal or our own.
- **R21 — `title`, `titleEn` and `part`**: accurate and our own, and left unchanged.
- **R22 — Attributions kept, hedged "from memory" and unchecked against a text**:
  - Iliad 12 (the honest spinning woman's wage)
  - Hesiod, Theogony (Brontes, Steropes, Arges)
  - Iliad 5 (the aegis with the Gorgon)
  - Iliad 18 (bronze, tin, gold and silver; twenty bellows)
  - Iliad 7 (Ajax's sevenfold shield); Iliad 18 and 20 (five layers)
  - Georgics 4 (the Cyclopes simile for the bees)
  - Iliad 1 (Hephaestus falling on Lemnos)
  - Odyssey 2 (Telemachus's two dogs)
  - Herodotus 1 (the Lydian origin of the Etruscans)
  - Cicero's lost work quoted by Augustine (the Etruscan pirates' torture)
  - the ancient commentators on *imbris torti* as hail

  All are right as far as I remember.
- **R23 — Note 499 cross-references to 6.46, 6.52 and 7.121**: kept. They are the same kind of misplaced opening mark.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading.
  - 8.443 `moras. ”Nec`
  - 8.447 `Ingentum` and 8.512 `indulgent`; the Latin Library has the correct forms
  - 8.489 `at`, 8.496 `his`, 8.510 `natum` and 8.514 `hunc`, lowercase after a stop. **The ruling in item 43 is still open.**
  - 8.498 capital `Signaque`. Do you want mid-sentence capitals noted at all?
  - 8.499 opening mark before `fata canens`. **This is the item-44 pattern again.**
- **Doubtful quantities on the chosen fit**:
  - 8.428 *deicit* as three syllables, dē-ĭ-cit. The line will not fit with two, although *reice* is two syllables at Eclogues 3.96.
  - 8.416 *Sīcănium* with a long Si-, against *Sĭcānae* at 8.328
  - 8.425 *-quĕ* lengthened before *St-*
  - 8.503 *Ē-trusca* long by position, against *Ĕtrūria* at 494
  - 8.492 *āgros* by position
  - 8.415 *fā-brīlia* by position
  - 8.418, 424 and 440 *Cȳ-* by position
- **Build report**: the COSTLY flag on 515 will still show. It was checked by hand and is right, and no entry was made.
- **Validator**: it will WARN about `t` marks (3 “, 2 ”), which is expected.
- **Unchecked attributions** are as listed in R22.
- **`make_units.py` is stale**: it still holds the drafter's strings, so re-running it would discard this review.
