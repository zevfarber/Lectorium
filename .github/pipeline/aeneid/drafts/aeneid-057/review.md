# Review — aeneid-057 (Aeneid VIII.1–101), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 40 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the drafter's flagged calls: the misprints 8.9 *mittitur* and 8.79 *sic*, the adjective 8.77 *hesperidum*, the bracketed lines 42–49 and the half-line 41, 8.65 *caput*, 8.40 *terrere*, 8.90 *rumore secundo*, 8.85 hysteron proteron and 8.18 *Laomedontius*. The Latin Library variants were checked too: 25 *laquearia*, 75 *tenent* and 84 *maxima*. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened and nothing was searched. In-poem cross-references were checked against the pinned source:
- 7.607–622: the gates of war, opened by Juno at 620–622
- 7.615: *cornua rauco*
- 7.647–648: *contemptor divom Mezentius*
- 7.691: Messapus; 7.744–747: Ufens and the Aequi
- 11.246–247: Argyripa
- 1.68: *victosque Penates*
- 4.285–286, and 4.532 *magnoque irarum fluctuat aestu*
- 4.522: *Nox erat*
- 7.205–211: Dardanus
- 3.389–393 and 3.437–439: Helenus
- 1.269–271: Alba
- 2.782: *Thybris*
- 8.330–332: the king Thybris

**Pass 2** re-read every edited field in full and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 101 lines by quantity, the bracketed 42–49 included. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. The scanner was wrong, **with no flag**, on 22 lines, and wrong as flagged on 54. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and against the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. For the half-line, the check was the validator's half-line rule (feet 1..k with k < 6, one ×, a `why` that begins "Half-line"). Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself, gives an **empty scanner report**: the COSTLY flag at 54 and the UNRESOLVED half-line 41 are both cleared. All 101 lines pass the validator's check, and **all 40 units get `sc`**. The half-line 41 closes the unit 40–41, so 40 needed a carrier entry, as at 7.759.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 40 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged. 19 units changed.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- Every note is 15–140 words. The longest is 137.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 282 insertions, 0 deletions, trailing newline kept. The new keys come after 7.815, in line order.
- `gloss.json` was not touched.
- The build and the validator were not run. Their scansion steps were replicated instead.

**Speech marks.** There are two speeches. The Tiber speaks 36–65 (units 13 and 24) and Aeneas prays 71–78 (units 27 and 29). In each of `t`, `l` and `i` there are 2 “ and 2 ”, all as printed.

**Severity counts: major 22, medium 5, low 27 (25 in pass 1, 2 in pass 2). Refused findings: 20. Scan-fixes entries added: 25.**

## Changes — pass 1

### Major
1–22. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities or the syllable count were wrong. Each line now has a hand entry.
   - **8.5 *coniurat***: the i is consonantal after the prefix: cōn-iū | rāt trĕ-pĭ | dō Lă-tĭ | ūm sae | vīt-quĕ iŭ | ven-tus. The scanner had co-ni-u-rat with a short iū.
   - **8.11, 8.67, 8.73 *Aenean*** and **8.29, 8.84 *Aeneas***: these are Ae-nē-ān and Ae-nē-ās. The scanner split Ae- in two each time. At 73 it also made *accĭpĭte* long in -ci-.
   - **8.13 *adiungere***: the i is consonantal (ad-iun-), with *se* elided: …rō (se) ad | iun-gĕ-rĕ | gen-tis.
   - **8.18 *Laomedontius***: Lā-ŏ-mĕ | dōn-tĭ-ŭs | hē-rōs. The scanner read Lao as one syllable and made -me- long.
   - **8.22 *aenis***: three syllables, a-ē-nis (= *ahenis*). The line reads …brīs ŭ-bĭ | lū-mĕn ă | ē-nis. The scanner made *ubi* long-long and *lū-* short, and read *ae* as a diphthong.
   - **8.24 *late loca***: lā-tē lŏ-că. The scanner made it short-short long-long.
   - **8.28 *ripa gelidique***: rī-pā gĕ-lĭ-. The scanner made it short-short long-long.
   - **8.34 *crinis umbrosa tegebat***: crī-nīs um-brō-să tĕ-gē-. The scanner made *cri-* and *-nis* short and *-sa* and *te-* long.
   - **8.42 (bracketed) *tibi ne vana putes***: Iam-quĕ tĭ | bī nē | vā-nă pŭ | tēs haec. *nē* and *vā-* are long, so *tibī* takes a long final i.
   - **8.44 (bracketed) *capitum fetus enixa***: tā că-pĭ | tum fē | tūs ē | nī-xă iă. The scanner made *ca-* and *-pi-* long and *-tus* and *e-* short.
   - **8.46 (bracketed) *requies***: three syllables, rĕ-quĭ-ēs (17 syllables in the line). The scanner had requ-ies.
   - **8.51 *Arcades his oris***: Ar-că-dĕs | hīs ō | rīs… The scanner had Ar-cā-dēs, his short and o- short.
   - **8.52 *regem Euandrum comites***: quī rē | (gem) Eu-an | drum cŏ-mĭ | tēs quī… The scanner made *re-* short, split E-u, and made *co-* and *-mi-* long.
   - **8.57 *Ipse ego te ripis***: Ips(e) ĕ-gŏ | tē rī | pīs et. The scanner had ē-gō and tĕ rĭ-.
   - **8.63 *pinguia***: three syllables, pin-guĭ-ă, a dactyl. The scanner read the i as a consonant, giving pingu-ia, a spondee.
   - **8.92 *insuetum***: in-suē-tum, three syllables with a consonantal u, as *adsueta* 7.746 and *desueta* 1.722. The scanner had four syllables with a short ē.
   - **8.99 *Romana potentia***: Rō-mā-nă pŏ-. The scanner made *Ro-* and *-ma-* short and *-na* and *po-* long.
   - **8.100 *Euandrus***: eu is one long syllable, rēs ĭ-nŏ | pēs Eu | an-drŭs hă | bē-bat. The scanner split E-u into two short syllables.

### Medium
23. **8.54** (COSTLY 4.6), **wrong as flagged**: Pal-lan | tis prŏ-ă | vī dē | nō-mĭ-nĕ | Pal-lan | tē-um, a spondaic line. The scanner made *dē* and *nō-* short and *-mi-* and *-ne* long.
24. **8.41** (UNRESOLVED), the half-line *concessere deum.*: con-cēs | sē-rĕ dĕ | ūm, entered as a half-line as at 7.702 and 7.760.
25. **Carrier 8.40**: the scanner's fit is right (checked by hand: *neu* one syllable, *terrēre*). Without it, the unit 40–41 would get no `sc`.
26. **Note 18–20, a wrong cross-reference**: "This line and the next one and a half repeat word for word … (4.285–286)" pointed at 19–20. In fact 20–21 repeat 4.285–286, and 19 only echoes Dido's *magnoque irarum fluctuat aestu* at 4.532. Both are now stated, checked against the pinned text. A scansion pointer for *Laomedontius* was added.
27. **Note 62–64, a wrong and an unverifiable claim**:
   - "'Thybris' is the Greek form of the Tiber's name" was wrong. Evander derives the name from a king Thybris (8.330–332). It now reads "the poetic name… Evander will derive it from an old king Thybris (330–332)".
   - "Scamander does the same to Achilles in Iliad 21": I cannot vouch that Scamander names himself last. It was cut, and the note now says "holding the name back for effect". The separate Scamander and Achilles parallel in note 31 (a river-god speaking to a hero) is true and was kept.

### Low
28. **Note 1–3**: "when the gates of Janus were opened (7.607–615)" now reads "when Juno herself flung open the gates of war (7.607–622)". 607–615 only describe the gates, and Juno opens them at 620–622.
29. **Note 4–6**: added *con-iū-rat*, with the i a consonant.
30. **Note 10–14**: added *Aenean* Ae-nē-ān, and *adiungere* with a consonantal i.
31. **`i` 15–17**: "must be plainer to Diomedes" now reads "is plainer". The Latin *apparere* has no "must".
32. **`l` 21–25 (line 22)**: "in basins when light of bronze" attached *aenis* to the light. It now reads "just as when, of water, the trembling light in bronze basins". Coherence wins the tie here.
33. **Note 21–25**: added *aenis*, three syllables, a-ē-nis (= *ahenis*).
34. **`l` 28–30 (line 30)**: "and late gave through his limbs rest" read *seram* as an adverb. It now reads "and gave through his limbs a late rest".
35. **Note 28–30**: added *Aeneas*, three syllables.
36. **`l` 31–33 (line 32)**: "among the poplar, aged, himself to raise leaves" read as if he raised leaves. It now reads "among the poplar leaves, aged, himself to raise".
37. **Note 31–33**: "the two words framing the line" was said of *fluvio… amoeno* / *se attollere*, which do not frame a line. "Framing the line" now goes with *populeas… frondes*, which do frame line 32.
38. **Note 40–41**: "The scanner cannot resolve it as a hexameter for that reason" was pipeline talk, not for the reader. It is replaced by the scansion of the half-line.
39. **Note 42–45**: "These four lines repeat… 3.390–392" was wrong, because line 42 is not in Book III. It now reads "Lines 43–45 repeat…", and "why they have been suspected" became "why the passage has been suspected".
40. **Note 42–45**: added the long final i of *tibi* and *fētūs* as an accusative plural. The note stays within 140 words because I cut "you will see".
41. **Note 46–49**: "it is the line editors most often doubt (from memory)" was a claim about scholarship I cannot check. It was cut.
42. **Note 46–49**: "'ex quo', 'from which (sign)'" now reads "'from which (time)', or 'in consequence of which'". I also added *requies* as three syllables.
43. **Note 55–56**: "the anaphora" for *Hi… hos* was wrong, since these are different cases. It now reads "the pronoun repeated at the head of each clause".
44. **`i` 62–64, an echo precaution**: "the river dearest to heaven" now reads "of all rivers the most pleasing to heaven".
45. **Note 62–64**: added *pinguia* as three syllables.
46. **Note 65 (*caput*)**: added that Greenough's commas, which set *celsis caput urbibus* off beside *domus*, seem to support the "capital" reading the translation takes. The drafter's call is upheld (R5).
47. **Note 74–77**: the Latin Library's *tenent* was cut. The note itself said it made no real change of sense, and conventions say to note a variant only where the sense changes.
48. **Note 74–77, *hesperidum***: added "the waters of Hesperia, the western land, Italy". This is the point of the adjective.
49. **`i` 81, an echo precaution**: "a portent, wonderful to behold" is a stock phrasing. It now reads "But look — a sudden portent, a marvel to the eye".
50. **`l` 86–89 (line 87)**: "and with silent flowing back so stood still wave" was garbled. It now reads "and, flowing back with silent wave, so stood still".
51. **Note 91–93**: added *insuetum*, in-suē-tum, with a consonantal u.
52. **Note 97–100**: added *Rōmāna*, with both vowels long.

Items 28–52 are the 25 pass-1 lows.

## Changes — pass 2
- **P2-1 (low)**: note 1–3 now said "the war that Juno let loose… when Juno herself flung open". The repeated Juno was cut: "the war let loose at the end of Book VII, when Juno herself…".
- **P2-2 (low)**: note 74–77 said "the waters of the west" right after "'of the western waters'". This now reads "the waters of Hesperia, the western land, Italy".

## Scan-fixes entries added (25)
Appended after 7.815 in line order, each with its reason:
- **Unflagged, wrong quantities or syllable count (22)**: 8.5, 8.11, 8.13, 8.18, 8.22, 8.24, 8.28, 8.29, 8.34, 8.42, 8.44, 8.46, 8.51, 8.52, 8.57, 8.63, 8.67, 8.73, 8.84, 8.92, 8.99 and 8.100
- **COSTLY, wrong (1)**: 8.54
- **Carrier (1)**: 8.40
- **Half-line, UNRESOLVED (1)**: 8.41

Each matches its line's words under `WORD_RE`. The 24 full lines each have six feet, five –⏑⏑/–– feet then –×, 13–17 syllables and one ×. 8.41 passes the validator's half-line rule (feet 1–3, one ×, a `why` that begins "Half-line"). In the replicated build all 25 apply, the scanner report is empty, all 101 lines pass, and 40 of 40 units get `sc`.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Greek eu**: *Teucros* (10) is one syllable, which is right. *neu* (40) is one syllable, which is right. *Euandrum* and *Euandrus* are fixed.
- **Initial Ae-**: these are right as the scanner reads them: *aetheris* (28), *aeternaque* (37), *aetherii* (68), *aethera* (70), *aequor* (89), *aequore* (96) and *aequavit* (100). *Aeneas* and *Aenean* are fixed, as is *aenis* (22), which is not a diphthong.
- **Consonantal i/u**: right as read: *iuventus* (5), *Troianam* (36), *Iunoni* (60), *iacebit* (44), *iunge* (56), *Iamque*, *iamque* and *adsidue* (55). *coniurat* (5), *adiungere* (13), *insuetum* (92) and *pinguia* (63) are fixed.
- **Hiatus**: none. Every vowel meeting is an ordinary elision, for example *sole repercussum aut* (23), *regi aut regi apparere* (17), *placido aequore* (96) and *unde est* (71).
- **Words named in the brief, scanner right**:
  - *tenuis* (33): three syllables, tĕ-nŭ-ĭs. The -is is long by position before *gl-*: vī-sŭs ĕ | ūm tĕ-nŭ | īs glau | cō vē | lā-băt ă | mic-tu.
  - *abies* (91): see R11.
  - *lacuaria* (25): lă-cŭ-ā-rĭ-ă, five syllables.
  - *deinde* (66): synizesis.
  - *hesperidum* (77): Hes-pĕ-rĭ-dum.
  - *leniit* (87): lē-nĭ-ĭt.
  - *alituum* (27): ā-lĭ-tŭ-um.
- **Other lines checked and right**:
  - *Ūfens* (6); *Mēssāpus* (6); *Vĕnŭlus* and *Dĭŏmēdis* (9)
  - *adhibe* (56), with *ad-* short before h
  - *Thybris* (64, 86), with the y long
  - *sacra* (85), long before *cr*
  - *eā… nocte* (86)
  - *rēliquit* (67), *lī* long
  - *apparēre* (17)

## Doubtful quantities and readings entered or left on the only fit
- **8.42 *tibī***: the long final i rests on the metre, since *nē* and *vā-* are long. The same doubt has come up before (7.443, 7.545).
- **8.91 *abies***: left on the scanner's trisyllabic *ăbĭēs*. A disyllabic *ab-yes* with a consonantal i also scans, because -es is long by position before *m*. See R11.
- **8.33 *tenuis***: left on the scanner's trisyllable. A disyllabic *ten-vis* also scans, but nothing calls for it.
- **8.54 *Pallantēum***: a spondaic fifth foot, as the drafter's note says.

## Refused findings
- **R1 — 8.9 *mittitur***, lowercase after the stop ending 8: the drafter's misprint call is **upheld**. Greenough capitalises sentence openings, so this is treated as a misprint under rule 5b. That is consistent with 7.290 *moliri* (aeneid-052) and 7.35/41/50 (aeneid-049). `t` stays as printed and `l`/`i` are capitalised. The note opens with the print's reading.
- **R2 — 8.79 *sic***, after *firmes.”*: the misprint call is **upheld**, on the same grounds as R1.
- **R3 — 8.77 *hesperidum***: **upheld as an adjective**, not a misprint. *Hesperis*, *-idis* is the adjective "western", and its genitive plural agrees with *aquarum*. The lowercase is right for an adjective, so it is not a misprint for *Hesperidum*. The note was improved (item 48).
- **R4 — the brackets 42–49 and the half-line 41**: handled per conventions. Every bracketed line is in [ ]. Units 15–17 say so in their notes. Unit 17's note explains why the second half of 49 belongs with 50. The `i` carries the brackets in step with `t`. I checked the metrical observation in note 49–50 and it is true: *concessere deum* + *Nunc qua ratione quod instat* make a complete hexameter (con-cēs | sē-rĕ dĕ | ūm nunc | quā ră-tĭ | ō-nĕ quŏd | in-stat). It is labelled as an observation, so it was kept.
- **R5 — 8.65 *caput***: the "capital" reading in `l` and `i` is **upheld**. The note gives both readings fairly. Greenough's commas favour apposition to *domus* (item 46).
- **R6 — 8.40 *terrere***: **upheld**. It is the present passive imperative, *terrēre*, "be frightened", continued by *neu*. An infinitive has nothing to depend on here.
- **R7 — 8.90 *rumore secundo***: **upheld**. The note gives three readings without choosing, and the `i` "cheered on their way" takes one of them. "Ennius used it, from memory" is hedged, so it was kept.
- **R8 — 8.85 hysteron proteron**: **upheld**. *mactat* comes before *sistit ad aram*, though the setting at the altar must come first.
- **R9 — 8.18 *Laomedontius***: the note's genealogy is right. Laomedon is son of Ilus. Assaracus is Ilus's brother and Aeneas's great-grandfather. "Means simply 'Trojan'" is fair. Only the scansion needed a fix.
- **R10 — 8.33 *tenuis***: the scanner is right, so there is no entry (see the hand-scan notes).
- **R11 — 8.91 *abies***: the brief suggested a consonantal i (ab-yes). Both readings scan, so I made no entry and left the scanner's trisyllable. Virgil turns to a consonantal i in this word only where the metre forces it (*abiete* 2.16), and the drafter's note already says "three syllables here". This is listed for the owner.
- **R12 — 8.4 *animi***: kept as the drafter's "minds", with *sunt* supplied. It is not the locative/genitive "in mind".
- **R13 — 8.12 *fatis***: "ablative without 'a'" was kept. A dative of agent is also possible, but the sense is the same.
- **R14 — note 91–93 "anaphora"** for *mirantur… miratur*: the verb heads both clauses, so the label holds, loosely. Kept.
- **R15 — Latin Library 8.25 *laquearia*, 8.84 *maxima***: spelling only. The note's mention at 25 is a gloss of Greenough's spelling, not a variant note. Kept.
- **R16 — Unit 11's Scamander parallel** (a river-god speaking to a hero, Iliad 21): this is true, and it is hedged "from memory". Kept.
- **R17 — Attributions kept from memory, hedged or standard**:
  - Servius on the *coniuratio* (4–6)
  - Iliad 5, Diomedes against Aeneas (9)
  - Apollonius, Argonautica 3 (21)
  - Iliad 10 and Iliad 2 (26, 31)
  - the ancient Life on the half-lines (41)
  - "many editors" on 43–45
  - Ennius, *rumore secundo* (90)
  - Lewis & Short on *vasto* (8) and on *enim* (84)
- **R18 — The `i` echo check**: nothing more found beyond items 44 and 49. "It was night, and over all the earth deep sleep held…", "Son of the race of gods" and "On they row, wearing out the night and the day" are plain renderings. `title`, `titleEn` and `part` are our own and unchanged.
- **R19 — The "about"**: accurate. It says the sow lines are bracketed, and it gives noon and the Palatine. Unchanged.
- **R20 — Cosmetic syllable divisions in the scanner's fits** where the quantities are right (e.g. *Tro–ia–nam* at 36): no entries.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b)**: 8.9 *mittitur* and 8.79 *sic*, lowercase after a full stop. They are treated as misprints, as at 7.290, and `t` is as printed. This is the Book VIII batch that the aeneid-049 question (item 43) foresaw. A general ruling is still wanted.
- **Doubtful quantities on the chosen fit**:
  - 8.42 *tibī*
  - 8.91 *abies*: trisyllable kept; ab-yes also scans
  - 8.33 *tenuis*: trisyllable kept
- **`make_units.py` is stale**: `drafts/aeneid-057/make_units.py` still holds the drafter's strings. Re-running it would discard this review.
- **Unchecked attributions, from memory**: Servius (4–6); Iliad 2, 5, 10, 21; Apollonius, Argonautica 3; the Donatus Life on the half-lines; Ennius, *rumore secundo*; Lewis & Short on *vasto* and *enim*.
