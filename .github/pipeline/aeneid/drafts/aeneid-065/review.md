# Review — aeneid-065 (Aeneid IX.107–223), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 57 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every cross-reference and every historical or mythological claim. I also checked the drafter's three rule-5b misprint calls (9.117 `iubet. ”Et`, 9.218 `Acestae,”`, 9.221 `adceleremus, ”ait`), the two places kept as doubtful (9.146 extra opening mark, 9.147 `castra.`), the Latin Library variants, the `about`, the title and part names, and every attribution made from memory. I read every `i` for echoes of the well-known English versions, with 9.182 and 9.184–185 read most closely.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington, Servius). No translation was opened and nothing was searched.

In-poem cross-references were checked against the pinned source: 1.71, 2.163–168, 2.195–198, 2.624, 3.185, 5.36–41, 5.114–118, 5.292–300, 5.315–361, 5.711–718, 7.55–58, 7.268–273, 7.421–424, 7.641–648, 7.691, 7.812–817, 8.404, 9.3, 9.22, 9.38, 9.52, 9.94–106, 9.224–245 and 10.219–224, 10.276. Two were wrong:
- 9.102–103 for Jupiter's *magni… aequoris esse deas* (item 18). The words are at 9.101–102.
- "151 repeats 2.166" (item 25). 2.166 has *Palladium*, not *Palladii*.

For the 9.146 decision I also listed every place where the print opens a speech mark while one is still open (21 in the poem; R4).

**Pass 2** re-read every edited field in full and made three more changes (P2-1 to P2-3).

**Scansion.** I hand-scanned all 117 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared its output with mine syllable by syllable.
- **The scanner was wrong on 12 lines**: 108, 113, 114, 133, 149, 165, 172, 177, 190, 192, 199 and 204. Only 165 was flagged. Each now has a hand entry.
- **167 is a half-line**, which the scanner returns as UNRESOLVED. It now has a half-line entry. 166 shares its unit, so it gets a carrier entry; without one, unit 166–167 gets no `sc` at all.
- **The other six flagged lines are right**: 156, 168, 179, 185, 196 and 201. They get no entry (see the hand-scan notes).

Every new `scan-fixes.json` entry was checked by script against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`). Each was also checked against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. For the half-line, the check was numbered feet 1..k with k < 6 and one ×. Each `why` gives a syllable count, and the script checked that count against the entry.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 14 entries apply
- **all 57 units get `sc`**
- all 117 lines pass the validator's metre check (116 hexameters and one half-line)
- after the fixes, the scanner report holds only COSTLY 156, 168, 179, 185, 196 and 201. All six are hand-checked right, and none blocks the build.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field. The file is written with `aeneid_lib.jdump` (`indent=1`, `ensure_ascii=False`, no trailing newline, as the drafter's file).
- `t`, `ln`, `p` and `v` are byte-for-byte as the drafter left them in all 57 units. A script checked this against a copy of the drafter's file taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- **26 units changed.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks**: 7 “ and 6 ” in each of `t`, `l` and `i`, on the same units. The extra “ is the doubtful one at 9.146 (R4).
- **Note lengths.** Every note is now 52–137 words. Unit 9.146–147 reached 141 words after item 22 and was trimmed (P2-3).
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- **`new-renderings.md` is stale.** It still quotes the drafter's `i` for 9.182 and 9.185, which items 37 and 38 replaced.
- The diff to `scan-fixes.json` only appends: 151 insertions, 0 deletions, trailing newline kept, formatting as before (a round-trip of the old file through `json.dumps(indent=1, ensure_ascii=False)` was byte-identical before appending). The new keys follow 9.103, in line order.
- The build and the validator were not run. Their scansion steps were replicated instead.
- **`drafts/aeneid-065/` has no `gloss.json`.** 064 had one, and the build needs it. That belongs to a later step, not this review.

**Severity counts: major 13, medium 4, low 29 (26 in pass 1, 3 in pass 2). Refused or upheld-without-change findings: 20. Scan-fixes entries added: 14.**

## Changes — pass 1

### Major
1–12. **Scansions the scanner got wrong.** Each line now has a hand entry with its reason.
- **Initial *Ae-* split (4 lines)**: 9.172, 9.177, 9.192 and 9.204.
  - 9.172 *Aeneas*: quōs pă-tĕr | Ae-nē | ās sī | quan-d(o) ad | ver-să vŏ | cā-rent (14 syllables; the scanner had 15).
  - 9.177 *Aeneae*, with *mīserat* long: Hyr-tă-cĭ | dēs cŏ-mĭ | t(em) Ae-nē | ae quem | mī-sĕ-răt | Ī-da (15 syllables; the scanner had 16).
  - 9.192 *Aenean*: Ae-nē | ān ac | cī-r(i) om | nēs pŏ-pŭ | lus-quĕ pă | tres-que (14 syllables). The scanner had the right count but read Ae-ne-an as a dactyl and made *pō-pū-* long.
  - 9.204 *magnanimum Aenean*, the same words as 1.260: mag-nă-nĭ | m(um) Ae-nē | ān et | fā-t(a) ex | trē-mă sĕ | cū-tus (14 syllables). The scanner made *-nā-* long and ran *Aenean* into two syllables, a fit with 13.
- **Greek *eu* in *Teucri* split (2 lines)**: 9.114 (Nē trĕ-pĭ | dā-tĕ mĕ | ās Teu | crī dē | fen-dĕ-rĕ | nā-vis, 15) and 9.149 (est ŏ-pŭs | īn Teu | crōs ad | dant sē | prō-tĭ-nŭs | om-nes, 14). The scanner had one syllable more each time.
- **Consonantal i after a prefix (2 lines)**:
  - 9.108 *iniuria*: dē-bĭ-tă | com-plē | rant cum | Tur-n(i) in | iū-rĭ-ă | Mā-trem (14 syllables; the scanner read i-ni-u-ri-a, 15), as at 1.27.
  - 9.199 *adiungere*: Mēn(e) ĭ-gĭ | tūr sŏ-cĭ | um sum | mīs ad | iun-gĕ-rĕ | rē-bus (15 syllables; the scanner had 16), as at 8.13.
- **9.113 *Troum***: two syllables, Trō-ŭm. ex-cĭ-dĭt | ēt Trō | ŭm Rŭ-tŭ | lō-rum-qu(e) | ag-mĭ-nă | com-plet (15 syllables). The scanner ran *Troum* into one syllable and made *Rū-tū-* long (14). The drafter's note ("two syllables") was right.
- **9.133 *Italae***: a short first I, as *Ĭtalos* at 3.440 and *Ĭtalas* at 5.703. ar-mă fĕ | runt Ĭ-tă | lae nīl | mē fā | tā-lĭ-ă | ter-rent (15 syllables). The scanner had the same count but made *Ī-tā-* long and *me* and *fa-* short.
- **9.165 *crateras aenos***, the one flagged line among these (COSTLY 2.0): *aēnos* is three syllables (ă-ē-nōs, never a diphthong) and *crātēras* has the short Greek *-ăs*, as at 7.633. in-dul | gent vī | n(o) et ver | tunt crā | tē-ră-s(ă) | ē-nōs (13 syllables). The scanner had 12 syllables and a spondaic fifth foot.
- **9.190 *late loca***: prō-cŭ-bŭ | ē-rĕ sĭ | lent lā | tē lŏ-că | per-cĭ-pĕ | por-ro (16 syllables). The scanner had the right count but made *lātē* short and *lŏca* long.

13. **9.166–167, the half-line.** 167 *insomnem ludo.* is a half-line: in-som | nem lū | dō (5 syllables). It is entered as a half-line, so the validator applies its hemistich rule. 166 gets a carrier entry: the scanner's own fit, con-lū | cent ig | nēs noc | tem cus | tō-dĭ-ă | dū-cit, checked by hand. Without these two entries the unit gets no `sc` and the build stops on UNRESOLVED.

### Medium
14. **Unit 9.140–142, `i` misread *perosos*.** "it ought to have been enough for them to have sinned once before, and now to hate almost every woman alive" made *perosos* a second infinitive of the "enough" clause. It is a participle: they should have come out of the first sin all but hating womankind, as the note rightly says. `i` now reads "one sin before ought to have been enough for them, and should have left them all but loathing the whole race of women."
15. **Unit 9.192–193, `i` got *reportent* the wrong way round.** "men be sent to bring him sure news" has the news going to Aeneas. *qui certa reportent* is men who will bring sure news back to the camp. It now reads "to bring back sure word".
16. **Unit 9.136–138, Lavinia.** The note said "promised to Turnus before Aeneas came, given to Aeneas by her father (Book 7)". Turnus was the suitor Amata favoured (7.55–57), not a promised husband. Latinus offers Lavinia to Aeneas (7.268–273) but has not given her. It now reads "whom Turnus had courted with her mother's backing before Aeneas came, and whom her father offered to Aeneas (7.55–57, 7.268–273)".
17. **Unit 9.222–223, a false claim.** *statione relicta* was glossed "a breach a Roman would notice". The relief has just taken over (*illi succedunt servantque vices*, 221–222), so no post is deserted. It now reads "now that the relief has taken it over".

### Low
18. **Note 9.116–117**: "(9.102–103)" now reads "(9.101–102)". *magni… iubebo / aequoris esse deas* is at 101–102.
19. **Note 9.107–109**: added "'iniuria' has a consonantal second i (in-yū-ri-a, four syllables)", which agrees with the 9.108 entry.
20. **Note 9.110–113**: "a short genitive plural of 'Tros'" was misleading, since *Trōum* is the regular third-declension form. It now reads "the genitive plural of 'Tros' (beside 'Troianorum'), two syllables, Trō-um".
21. **`l` 9.119–120**: "with plunged into the water beaks, / the depths they seek" put *aequora* with *demersis* as well as rendering *ima* as "the depths", and invented "into". It now reads "with plunged beaks, the waters / lowest they seek", which matches the note's *aequora… ima*.
22. **Note 9.120–122**: *virgineae… facies* is "set two lines apart" (120 and 122), not three.
23. **`i` 9.123–125**: "as his horses bolted in panic" added the bolting. *turbatis equis* now reads "as his horses took fright".
24. **Note 9.132–133**: added "'Italae' has a short first I here (Ĭ-ta-lae), as the metre shows, against the long I of 'Itala' at 3.185", which agrees with the 9.133 entry.
25. **Note 9.149–152**: "151 repeats 2.166" now reads "151 all but repeats 2.166 ('Palladium, caesis summae custodibus arcis')".
26. **Note 9.149–152**: *ne timeant* had no subject. It now reads "'let them (the Trojans) not fear' such tricks from us". The Trojans need not fear night raids, because Turnus will attack by daylight (153).
27. **Note 9.146–147**: "as English printing does when one speech runs into a new paragraph" implied a paragraph break that the print does not show at 146. It now says no break shows here, and that the mark is doubtful and kept (R4).
28. **Note 9.146–147**: the reason for keeping `castra.` was "an appeal ('you who…') is not impossible". That cannot stand, because *vos… qui apparat* has a singular verb, so *qui* must be the interrogative. The reason is now that pointing a question which is also a call to arms is the editor's choice, not a slip of the type (R5).
29. **Note 9.164–165**: added "(short '-ăs')" for *crateras*, which agrees with the 9.165 entry. See P2-1 for the final wording.
30. **Note 9.166–167**: "gaming with dice" was more than *ludo* says. It now reads "at games".
31. **Note 9.179–181**: "'it' could be the Latin Library's 'et'" was garbled. It now reads "For Greenough's 'it', 'goes', the Latin Library prints 'et'…".
32. **`i` 9.179–181**: "nor did a fairer put on Trojan armour" now reads "nor did any fairer man put on Trojan armour".
33. **Note 9.192–193**: added "(three syllables, Ae-nē-ān)" for *Aenean*, which agrees with the 9.192 entry.
34. **Note 9.194–196**: added that the line ends with a spondaic fifth foot, moe-ni-a | Pal-lan | tē-a, as again at 241 (checked). This explains the COSTLY flag on 196.
35. **Note 9.199–200**: "'adiungere' begins with a consonantal i after the prefix" now reads "has a consonantal i after the prefix".
36. **`l` 9.188**: "You see what the Rutulians holds, confidence in affairs." was not English. It now reads "You see what confidence in their affairs possesses the Rutulians."
37. **`i` 9.182 (*His amor unus erat*)**:
    - "One love bound the two, and they charged into battle" now reads "The two had one love between them, and side by side they would rush into battle".
    - "bound" was not in the Latin, and "charged" lost the habitual imperfect that the note points out.
    - The new wording is literal and, as far as I know, close to no published version.
38. **`i` 9.185**: "or does every man make a god of his own fierce longing?" now reads "or does each man's own dread craving grow into a god for him?"
    - The drafter's turn reversed the Latin's agency. In the Latin the desire becomes (*fit*) a god; the man does not make it one.
    - "make a god of" is also close to a familiar older English turn.
    - The new wording keeps *fit* and *dira* and avoids both "becomes his god" and "make a god of".
    - The first half, "do the gods set this ardour in our minds", is kept (R11).
39. **`l` 9.190–191**: "what now in my mind the thought rising" had no verb. It now reads "what thought is now rising in my mind".
40. **`i` 9.201–204**: "his fortunes to the last" suggested "to the end". *fata extrema* now reads "his fortunes at their worst", which agrees with the note.
41. **`i` 9.213–215**: "if Fortune forbids it as she does" now reads "if Fortune, as she so often does, forbids it" (*solita*).
42. **Note 9.216–218**: "the Trojan-born king in Sicily" was wrong. Acestes was born in Sicily to a Trojan mother and the river Crinisus (5.38, checked). See P2-2 for the final wording.
43. **`i` 9.219–221**: "But Euryalus said: … he said" now reads "But Euryalus answered: … he said".

These are 26 numbered low items. Items 27 and 28 touch the same note but are counted separately, as are items 31 and 32.

## Changes — pass 2
- **P2-1 (low), note 9.164–165**: item 29 left "with a short '-ăs', the bowl in which…", which hung the bowl on the ending. It now reads "the Greek accusative plural (short '-ăs') of 'crater', the bowl in which wine was mixed with water".
- **P2-2 (low), note 9.216–218**: item 42 left "(his mother was Trojan, 5.38), where in Book 5…", where "where" no longer pointed at Sicily. It now reads "the Sicilian king of Trojan blood (his mother was Trojan, 5.38); in Book 5 the weary and the women stayed behind in Sicily in a city named for him (5.715–718)".
- **P2-3 (low), note 9.146–147**: after items 27 and 28 the note was 141 words. It was trimmed to 137 ("The print ends with a full stop; a question wants a question mark…") with no loss of substance.

Pass 2 also re-checked every "enclosing"/"framing" claim in the part: 110–111, 114, 123–124, 138–139, 144–145, 154–155, 183, 185, 194–195, 197–198, 205–206, 208–209, 212, 216–217 and 219–220. All are right.

## Scan-fixes entries added (14)
These are appended after 9.103 in line order:
- **Initial *Ae-* (4)**: 9.172, 9.177, 9.192 and 9.204
- **Greek *eu* in *Teucri* (2)**: 9.114 and 9.149
- **Consonantal i after a prefix (2)**: 9.108 *iniuria* and 9.199 *adiungere*
- ***Troum*, two syllables (1)**: 9.113
- ***Ĭtalae*, short I (1)**: 9.133
- ***crātēras aēnos* (1)**: 9.165, the flagged COSTLY 2.0
- **Wrong quantities, same count (1)**: 9.190 *lātē lŏca*
- **Carrier (1)**: 9.166
- **Half-line (1)**: 9.167

Each entry matches its line's words under `WORD_RE`. Each hexameter entry has six feet, five –⏑⏑/–– feet then –×, 13–16 syllables and one ×. The half-line has feet 1–3 and one ×. Each `why` states the count, and each count was checked by script.

## Hand-scan notes on the special lines (scanner right, no entry)
- **9.156, flagged COSTLY 2.0, right**: Nunc ă-dĕ | ō mĕ-lĭ | ōr quŏ-nĭ | ām pars | ac-tă dĭ | ē-ī (16 syllables). *-or* is long by position before *qu-*, and *diēī* has a long ē.
- **9.168, flagged COSTLY 2.8, right**: Haec sŭ-pĕr | ē val | lō prō | spec-tant | Trō-ĕs ĕt | ar-mis (14 syllables). *Troes* has a short *-ĕs* before a vowel here. At 136 it is long by position before *Sunt*.
- **9.179, flagged COSTLY 2.5, right**: it iux | tā cŏ-mĕs | Eu-rў-ă | lūs quō | pul-chrĭ-ŏr | al-ter (15 syllables). *Eu-* is one syllable, and *it* is long by position.
- **9.185, flagged COSTLY 3.0, right**: Eu-rў-ă | l(e) an sŭ-ă | cui-quĕ dĕ | ūs fit | dī-ră cŭ | pī-do (16 syllables).
- **9.196, flagged COSTLY 4.0, right**: pos-sĕ vĭ | (am) ad mū | rōs et | moe-nĭ-ă | Pal-lan | tē-a (14 syllables), a spondaic fifth foot (item 34).
- **9.201, flagged COSTLY 2.4, right**: Nōn ĭ-tă | mē gĕ-nĭ | tōr bel | līs ad | suē-tŭs Ŏ | phel-tes (15 syllables). The *u* of *adsuetus* is consonantal.
- **Other *Teucri*/*eu* lines are right**: 9.130 *Teucris* and 9.171 *Mnestheus* (one syllable, before *ācer* with long ā; that is how the line scans). *Euryalus* at 9.179, 185 and 198 is right too.
- **9.180 *Aeneadum***: Ae-nĕ-ă-dum, the diphthong right.
- **9.138 *coniuge***: con-iŭ-gĕ, the i consonantal, right.
- **9.134 *iactant***: the i is consonantal, so *se* is long and unelided. Right.
- **Hiatus**: none in this part.
- **Elision of a monosyllable**: 9.200 *t(e) in*, right.
- **9.214 *solita***: elided, so the metre cannot decide between *humo solitā* and *solita… Fortuna*. The note gives both readings.
- **9.203 *sublatum***: the scanner divides it su-bla-, with the same quantities as the right sub-lā-. This is cosmetic only, so there is no entry (as 064 R6 and QUESTIONS item 37).
- **Other quantities checked**:
  - *Aurōrā* abl. (111); *Īdaeī* (112); *genetrīx iŭbĕt* (117); *abrumpunt* with *ab-* long (118); *delphīnum* (119); *Tiberīnus* (125)
  - *Trōiānos* (128); *ēripuit* (129); *mihī* (137); *Ētrusci*, long by position (150); *condēmur* (152)
  - *obsīdere* from *obsīdo*, which the metre requires (159); *ācer* (171) and *ācerrimus* (176); *prōpugnacula* (170); *Trōiae* (202)
  - *ērudiit* (203); *vītā* (206, 212); *quiētest* by prodelision (187); *pugnā* (213)

## Refused or upheld findings
- **R1 — 9.117 `iubet. ”Et`**: **upheld** as a rule-5b misprint. It is the pattern of 8.404, 9.22 and 9.38 (QUESTIONS items 52–56). The note opens with the print's reading, and the unit rightly runs on to the end of the narrative sentence.
- **R2 — 9.218 `Acestae,”`**: **upheld** as a misprint.
  - The speech is complete and the next word, *Ille*, has a capital and begins an independent sentence (*Ille autem:*). A comma cannot stand there.
  - This is the same kind of stop/comma slip already treated under rule 5b at 3.286, 3.391 and 6.251 (QUESTIONS items 19, 20 and 36).
  - `t` keeps the print, `l`/`i` end with a full stop, and the note opens with the print's reading.
- **R3 — 9.221 `adceleremus, ”ait`**: **upheld** on the same grounds, the slip of 7.68, 8.113 and 9.52 (closing mark joined to *ait*/*inquit*).
- **R4 — 9.146 extra opening mark, kept as doubtful**: **upheld**, with the note's reasoning corrected (item 27). My reasons:
  - **Elsewhere the print reopens a mark inside an open speech in 21 places.** Almost all are lines where *ait*/*inquit* interrupts (6.46, 6.52, 7.121 and others, item 44) or where a speech is quoted inside a speech (2.116, 11.252, 11.399).
  - **9.146 is neither.** It looks like the English convention for a speech that goes on into a new paragraph, with the paragraph indent missing here. Many editions do begin a paragraph at *Sed vos*, as I remember.
  - That makes it a doubt about Greenough's layout, not a clear error of type, so rule 5b says keep the print and say so. That is what the unit does. `t`, `l` and `i` all carry the mark, so the validator will WARN 7 “ / 6 ” in each layer. That is a warning, not a failure.
- **R5 — 9.147 `castra.` as a question, kept as doubtful**: **upheld**, with the reasoning corrected (item 28). The singular *apparat* makes *qui* interrogative, so the sense is certainly a question. But a full stop after a question that is also a summons is an editor's pointing choice, so the print stays and `l`/`i` give "?".
- **R6 — COSTLY 156, 168, 179, 185, 196 and 201**: hand-checked right, so no entries were made.
- **R7 — Latin Library variants**:
  - 134, 172, 187, 210, 211, 214, 215 and 221 are orthography. The notes name Greenough's spelling as his, which is harmless.
  - 121 (line omitted), 129 *ignis exspectant*, 151 *late* and 179 *et* change the sense and are rightly noted.
  - 155 *decimum* is orthography and is noted harmlessly.
- **R8 — Note 9.123–125 *ab alto* "from the sea at his mouth"**: kept. It is the usual way of taking it (the river checks its flow from the sea).
- **R9 — Note 9.176–178 *Ida venatrix*, mountain or nymph**: kept. Both views are ancient (Servius, from memory), and the note does not choose.
- **R10 — Note 9.200 "a thing Virgil allows with pronouns like 'me' and 'te'"**: kept. It is right (cf. *se adiungere*, 8.13).
- **R11 — `i` 9.184 "do the gods set this ardour in our minds"**: kept. It is literal (*addunt*), and it avoids the familiar "put this fire in our hearts".
- **R12 — `i` 9.110–113 "and in it the dancing bands of Ida"**: kept. Seeing the *chori* in the cloud is the natural reading, and the note says "also seen".
- **R13 — `i` 9.154–155 "Pelasgian boys"**: kept. *pubes* is "youth", and "boys" carries Turnus's contempt without inventing it.
- **R14 — Note 9.154 *faxo* "an old future perfect of 'facio' (= 'fecero')"**: kept. It is the school-grammar label (A&G).
- **R15 — Note 9.144–145, Neptune and Apollo built Troy's walls for Laomedon**: kept. The poem's own *Neptunia Troia* (2.625) supports Neptune. Apollo's share is Homeric (Iliad 7 and 21, from memory).
- **R16 — Note 9.201 "Opheltes is named only here"**: kept. The pinned source has *Opheltes* only at 9.201.
- **R17 — Note 9.221 *excitat* "Euryalus or Nisus, the subject left loose"**: kept. Euryalus is the grammatical subject carried on from *Ille*, but the hedge is harmless.
- **R18 — Note 9.166–167 "more than fifty" half-lines**: kept. It is true, and it is deliberately unspecific.
- **R19 — Note 9.110–113, Corybantes**: kept. The identification of Ida's *chori* with Cybele's dancers is the standard one.
- **R20 — `about`, `title`, `titleEn`, `part`**: unchanged. The `about` agrees with the text throughout (checked line by line, including "alone of the Trojan mothers", 217). `part` and `titleEn` carry IX.107–223.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: `t` is as printed and `l`/`i` are corrected, with each note opening with the print's reading:
  - 9.117 `iubet. ”Et`, a closing mark joined to the next word, as items 52–56
  - 9.218 `Acestae,”`, a comma for a full stop before a new sentence, as 3.286, 3.391 and 6.251
  - 9.221 `adceleremus, ”ait`, a closing mark joined to *ait*, as 9.52
- **Kept as printed, doubtful**:
  - 9.146 has an opening mark inside Turnus's open speech, with no paragraph break shown. It is probably a lost paragraph indent, and it is the only reopen in the poem not explained by *ait* or an inner quotation. The validator will WARN 7 “ / 6 ” in `t`, `l` and `i`.
  - 9.147 `castra.` is a question (*qui* interrogative) printed with a full stop. `l`/`i` give "?".
- **Scansion**: the build report should list only COSTLY 156, 168, 179, 185, 196 and 201, all hand-checked right.
  - 14 entries: 9.172, 9.177, 9.192 and 9.204 (*Ae-*); 9.114 and 9.149 (*Teucri*); 9.108 (*iniuria*); 9.199 (*adiungere*); 9.113 (*Trōum*); 9.133 (*Ĭtalae*); 9.165 (*crātēras aēnos*); 9.190 (*lātē lŏca*); 9.166 (carrier); 9.167 (half-line).
  - The only choice that could be argued is 9.133. Short *Ĭtalae* against *Ītala* at 3.185 rests on the metre alone, as at 3.440, 5.703 and 6.92.
- **Unchecked attributions, all from memory**:
  - Ovid, Metamorphoses 14 (the ships become nymphs)
  - Iliad 18 (Vulcan's arms for Achilles); Iliad 7 and 21 (Neptune and Apollo and Troy's walls)
  - Servius on *Ida venatrix* (mountain or nymph)
  - "most take *regem* of Ascanius" (Servius and Conington)
  - the Corybantes as the *Idaei chori*
  - that many editions begin a paragraph at 9.146
- **Stale files**:
  - `make_units.py` still holds the drafter's strings, so re-running it would discard this review.
  - `new-renderings.md` still quotes the replaced `i` for 9.182 and 9.185.
  - `drafts/aeneid-065/` has no `gloss.json` yet, and the build needs one.
