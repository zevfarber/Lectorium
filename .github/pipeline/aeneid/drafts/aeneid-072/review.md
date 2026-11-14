# Review — aeneid-072 (Aeneid X.1–95), adversarial reviewer

**Severity counts: major 17, medium 2, low 22 (20 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 21. Scan-fixes entries added: 20 (14 wrong full lines, 3 half-lines, 3 carriers).**

I reviewed this part in two passes.

**Pass 1** covered all 59 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked:
- the drafter's two misprint calls (10.20, 10.36), and looked for others
- the Latin Library variants
- the speech marks
- the bracketed lines 20–21 and 27
- the half-lines 17, 62 and 62b
- the no-advisory decision
- `about`, the title and the part names

I read every `i` for echoes of the well-known English versions.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

I checked the in-poem cross-references against the pinned source, and all are right:
- 1.26–28 (*iudicium Paridis*)
- 1.279 (*imperium sine fine*)
- 2.325 (*fuimus Troes*)
- 3.183–187 (Cassandra foretold Italy)
- 5.606 (Iris sent to the fleet)
- 7.153–155 (envoys with olive branches)
- 7.312 (*Acheronta movebo*)
- 7.323–325 (Allecto)
- 8.9 (Venulus sent to Diomedes)
- 9.2 (Iris sent to Turnus)
- 9.4 (Pilumnus)
- 9.77–122 (the ships turned into nymphs by the Mother of the Gods)
- the in-part references to 10.12, 25, 27, 38, 44–45, 51, 85 and 86

**Pass 2** re-read every edited field in full, re-checked speech marks, line counts and note lengths, and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 96 source lines (95 numbers plus 62b). I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story` (with each unit's `ln`), and compared its output with mine syllable by syllable. The helper is `drafts/aeneid-072/scan_check.py`, adapted from 071 to key lines by `label` as the build now does.
- **The packet's flags.** 17, 62 and 62b are half-lines (M2, M11, M12). 20 is the misprint *Rutulli* (M4). 89 (COSTLY 2.8) is wrong: the count is right but the quantities are not (M16).
- **`scan_story` joins 62 and 62b.** Both units carry `ln` 62, so `scan_story` scans them as one hexameter (it reports 95 lines, not 96). The validator, however, checks 62 and 62b separately, so both need half-line entries.
- **Twelve more lines are wrong without a packet flag:** 6, 18, 25, 26, 28, 44, 48, 58, 65, 81, 85, 90.
  - Initial *Ae-*: *Aeneas* ×3, *Aenean* ×2.
  - Greek *eu*: *Teucros* 28, *Teucris* 44, *Teucri* 58.
  - Consonantal *i* after a prefix: *obiecit* 90.
  - *quianam* run together: 6.
  - The hiatus of *O* elided away: 18.
  - Wrong quantities with no special feature: 26.
- **16, 21 and 22 are carriers.** They share units 9 and 12 with the unresolved lines 17 and 20, and a unit with an unresolved line gets no `sc` at all (L-S1–3).

Every new `scan-fixes.json` entry was checked by script (`drafts/aeneid-072/add_scan_fixes.py`):
- against the build's word-match rule (`strip(sc) == WORD_RE.findall(line)` for the line as printed)
- against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet, then –×/⏑×. For a `why` beginning "Half-line", the validator's half-line rule applies instead: numbered feet 1..k with k<6 and exactly one ×.
- against its own `why`: each `why` gives a syllable count, and the script checked it.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 20 entries apply (keys `10.n`, and `10.62b` for the label)
- **all 59 units get `sc`**
- every unit's `sc` lines up with its words
- all 96 lines pass the validator's metre check (half-line rule for 17, 62 and 62b)
- the scanner report is empty (no UNRESOLVED, MISMATCH or COSTLY left)

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by Python scripts: `review_edits.py` for pass 1 and `review_edits_pass2.py` for pass 2. Each old string was asserted to occur exactly once in its field. The file is written with `aeneid_lib.jdump`; a round-trip of the drafter's file through `jdump` was byte-identical before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` are as the drafter left them in all 59 units (checked by script against a copy taken before any edit). `title`, `titleEn`, `part` and `about` are unchanged. No unit boundary was changed.
- **16 units changed:** 0, 2, 4, 6, 15, 20, 21, 23, 28, 30, 35, 39, 43, 48, 50, 56.
- **Layout checks.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks.** `t`, `l` and `i` each have 3 “ and 3 ”, on the same units: Jupiter 2/8, Venus 10/36, Juno 38/58. The bracket counts in `t` and `l` agree.
- **Note lengths.** The notes run 41–129 words, under the validator's 140.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- **`scan-fixes.json`.** The diff only appends: 220 insertions, 0 deletions, trailing newline kept, formatting unchanged (`json.dumps(indent=1, ensure_ascii=False)`; a round-trip of the old file was byte-identical before appending). There were no 10.* keys before, so the new keys follow 9.811, in line order (… 10.62, 10.62b, 10.65 …).
- **Build and validator not run.** `build_aeneid.py` has no dry-run mode, so its scansion step and the validator's metre and `sc`-alignment checks were replicated instead.

## Changes — pass 1

### Major (scanner wrong; each now has a scan-fixes entry)
- **M1. 10.6, *quianam* (unflagged).** The scanner ran *qui-a* into one long syllable (14). Right, as *Heu quianam* 5.13: Cae-lĭ-cŏ | lae mag | nī quĭ-ă | nam sen | ten-tĭ-ă | vō-bis (15).
- **M2. 10.17, half-line (UNRESOLVED).** pau-că rĕ | fert: a dactyl and one syllable (4).
- **M3. 10.18, *O… O* (unflagged).** The scanner elided the second *O* and lengthened *ho-mi* (14). The interjection is never elided. Right: Ō pă-tĕr | Ō hŏ-mĭ | num rē | rum-qu(e) ae | ter-nă pŏ | tes-tas (15). This agrees with the drafter's note.
- **M4. 10.20, *Rutulli* (UNRESOLVED).** With the misprint's double *l*, *-tul-* is long and no hexameter fits. The entry's tokens spell `Rutulli` as printed, because the build matches the words of the printed line. The line is scanned as *Rutuli*, with the stray *l* carried on the last syllable (`Ru⏑tu⏑4lli–`). The entry's `why` says so. Cer-nĭs ŭt | in-sul | tent Rŭ-tŭ | lī Tur | nus-quĕ fĕ | rā-tur (15).
- **M5. 10.25, *Aeneas* (COSTLY 1.2, under the threshold).** The scanner split *Ae-* (15). Right: Ae-nē | ās ig | nā-rŭs ă | best Num | quam-nĕ lĕ | vā-ri (14).
- **M6. 10.26, *muris iterum* (unflagged).** The count is right but the quantities are wrong: the scanner made *mū-rīs* short-short and *ĭ-tĕ-* long-long. Right: ob-sĭ-dĭ | ō-nĕ sĭ | nēs mū | rīs ĭ-tĕ | r(um) im-mĭ-nĕt | hos-tis (16).
- **M7. 10.28, *Teucros* (unflagged).** The scanner split Te-u (15). Right: at-qu(e) ĭ-tĕ | r(um) in Teu | crōs Ae | tō-līs | sur-gĭt ăb | Ar-pis (14).
- **M8. 10.44, *Teucris* (COSTLY 1.5).** The scanner split Te-u (15). Right: sī nūl | l(a) est rĕ-gĭ | ō Teu | crīs quam | dēt tŭ-ă | con-iunx (14). *coniunx* has consonantal *i*, and the scanner already had that right.
- **M9. 10.48, *Aeneas* (COSTLY 1.2).** The scanner split *Ae-* and shortened *-nē-* (14). Right: Ae-nē | ās sā | n(e) ig-nō | tīs iac | tē-tŭr ĭn | un-dis (13).
- **M10. 10.58, *Teucri* (unflagged).** The scanner split Te-u (17). Right: dum Lă-tĭ | um Teu | crī rĕ-cĭ | dī-vă-quĕ | Per-gă-mă | quae-runt (16). *rĕcĭdīva* is scanned as at 4.344.
- **M11. 10.62, half-line (UNRESOLVED).** dā pă-tĕr | Ī-lĭ-ă | cōs Teu | crīs: two dactyls, a spondee and one syllable (9).
- **M12. 10.62b, half-line (UNRESOLVED).** Tum | rē-gĭ-ă | Iū-nō (6). The feet are numbered 1–3 from the half-line's own start, as the validator requires. The `why` explains that in the shared verse they are the fourth to sixth feet (crīs Tum | rē-gĭ-ă | Iū-nō).
- **M13. 10.65, *Aenean* (unflagged).** The count is right but the quantities are wrong: the scanner made *-ne-an* short and *ho-mi* long. Right: Ae-nē | ān hŏ-mĭ | num quis | quam dī | vom-quĕ sŭ | bē-git (14).
- **M14. 10.81, *Aenean* (COSTLY 1.2).** The scanner split *Ae-* (16). Right: Tū pŏ-tĕs | Ae-nē | ān mă-nĭ | bus sub | dū-cĕ-rĕ | Grā-ium (15).
- **M15. 10.85, *Aeneas* (COSTLY 1.2).** The scanner split *Ae-* (15). Right: Ae-nē | ās ig | nā-rŭs ă | best ig | nā-rŭs ĕt | ab-sit (14).
- **M16. 10.89 (flagged COSTLY 2.8).** The scanner had 14 syllables but made *qui* and *Trō-* short and *-ăs* and *Ă-* long. Right, as the drafter has it: cō-nā | mur nōs | an mĭ-sĕ | rōs quī | Trō-ăs Ă | chī-vis (14).
- **M17. 10.90, *obiecit* (unflagged).** The scanner read *o-bi-e-cit* (15). Right: ob-iē | cīt quae | cau-să fŭ | it con | sur-gĕ-r(e) ĭn | ar-ma (14).

### Medium
1. **Note 1–4, Iliad 4.** The note said that at the start of Iliad 4 and 8 "Zeus calls the gods together and forbids them to join the fighting". Only Book 8 has the ban. The Book 4 council is the one where Zeus taunts Hera and the gods decide to break the truce. The note now reads "as the Iliad does at the start of Books 4 and 8; in Book 8 Zeus calls the gods together and forbids them to join the fighting."
2. **Note 81–83, Iliad 5.** The note said Aphrodite "carried the wounded Aeneas out of Diomedes' reach". She did not: Diomedes wounded her and she let Aeneas fall. Apollo then hid him in a dark cloud and left a phantom of him on the field, which is the point of *proque viro… nebulam*. The note now says so and adds "Juno gives Venus all the credit." Note 29–30 ("as she carried Aeneas out of the fight") is accurate and was left alone.

### Low
- **L-S1. 10.16: carrier entry.** The scanner's fit is right (15). The line is entered only because unit 9 also holds the half-line 17.
- **L-S2. 10.21: carrier entry.** The scanner's fit is right (16). Unit 12 holds line 20.
- **L-S3. 10.22: carrier entry.** The scanner's fit is right (15). Its first words, *Marte ruat?*, are in unit 12 with line 20.
- **L1. Note 6–7.** It now says *quianam* is "three syllables, qui-a-nam", to match M1.
- **L2. Note 9a.** *Quae contra vetitum discordia?* is not "half a line long". The note now says "less than a line long".
- **L3. `l` 11–13.** "do not summon it early" added a word the Latin does not have. It is now "do not summon it".
- **L4. Note 11–13.** *iustum… tempus* does not frame the line, because *Adveniet* comes first. The note now says the pair is "enclosing 'pugnae, ne arcessite'".
- **L5. Note 11–13.** The elision list left out *n(e) arcessite*. Added.
- **L6. `i` 25a and 85a.** The two notes stress that Juno repeats Venus's words exactly, but the `i` lines differed ("And Aeneas is far away and knows nothing of it." / "Aeneas is away and knows nothing:"). Both now read "Aeneas is away and knows nothing of it", with the original stops.
- **L7. Note 31–33a.** The elision list left out *nequ(e) illos*. Added.
- **L8. Note 33b–35.** "'but if (they came) having followed', 'sunt' left out" contradicted itself. It now reads "'but if (they have) followed', 'sunt' left out".
- **L9. Note 39–41.** The drafter flagged *movet*'s subject as an interpretation, but the note gave it flat. It is now "best taken as Juno, unnamed, as her own words in Book VII suggest (some make it Allecto)". The wording was revised in P2-2.
- **L10. Note 48–49.** The note said "No elisions", but *san(e) ignotis* is elided. Corrected.
- **L11. Note 48–49.** *dederit* was called a future perfect, flat. The same form is a perfect subjunctive, drawn into the mood of *sequatur*. Both readings are now given.
- **L12. `l` and note 51–52a.** The note glossed *Idaliae* as a genitive ("the house of Idalium"), while `l` made it an adjective ("the Idalian home"). If *Idaliae* were an adjective, *domus* would have to be plural. `l` is now "and Idalia's house", and the note explains that Idalia is another name for Idalium.
- **L13. Note 59–60a.** *cineres… supremos* does not frame the line. The note now says the pair is "enclosing 'patriae insedisse'".
- **L14. Note 65–66.** The elision list left out *s(e) inferre*. Added.
- **L15. Note 72–73a.** "(line 44–45)" is now "(lines 44–45)".
- **L16. Note 81–83.** The elision list left out *obtender(e) inanis*. Added.
- **L17. Note 92–93.** *Dardanius… adulter* does not frame the line, because *Me duce* comes first. The note now says "the sneering noun held back to the end of the line".

## Changes — pass 2
- **P2-1. Note 51–52a.** The pass-1 gloss was reworded: "'the house of Idalia', genitive; Idalia is another name for Idalium, and the house is her temple there."
- **P2-2. Note 39–41.** The pass-1 hedge quoted *Acheronta movebo* a second time in the same note. It now says "as her own words in Book VII suggest".

## Scan-fixes entries added (20)
| key | reason | syllables |
|---|---|---|
| 10.6 | *quĭănam* three syllables | 15 |
| 10.16 | carrier for half-line 17 (scanner right) | 15 |
| 10.17 | half-line (UNRESOLVED) | 4 |
| 10.18 | *O* in hiatus, not elided | 15 |
| 10.20 | misprint *Rutulli* scanned as *Rutuli* (UNRESOLVED) | 15 |
| 10.21 | carrier for line 20 (scanner right) | 16 |
| 10.22 | carrier for line 20 (scanner right) | 15 |
| 10.25 | *Aeneas*, initial Ae- | 14 |
| 10.26 | *mūrīs*, *ĭtĕrum* | 16 |
| 10.28 | *Teucros*, Greek eu | 14 |
| 10.44 | *Teucris*, Greek eu | 14 |
| 10.48 | *Aeneas*, initial Ae- | 13 |
| 10.58 | *Teucri*, Greek eu | 16 |
| 10.62 | half-line, first half of the shared line (UNRESOLVED) | 9 |
| 10.62b | half-line *Tum regia Iuno* (UNRESOLVED) | 6 |
| 10.65 | *Aenēān*, initial Ae- | 14 |
| 10.81 | *Aenēān*, initial Ae- | 15 |
| 10.85 | *Aeneas*, initial Ae- | 14 |
| 10.89 | *quī*, *Trōăs*, *Ăchīvis* (COSTLY 2.8) | 14 |
| 10.90 | *obiecit*, consonantal i after a prefix | 14 |

## Hand-scan notes on the special lines (scanner right, no entry)
- **38 *Aeolia***: Ae-ŏ-lĭ-(a) ex-cī-tōs, with *Ae-* as one syllable. Right. **28 *Aetolis*** is right inside the 10.28 entry.
- ***Teucris* 8 and *Teucros* 22**: eu is one syllable. Right. (22 is entered only as a carrier.)
- **73 *Ubi hic***: ē-gĭt ŭ | b(i) hīc Iū | nō dē | mis-să-vĕ | nū-bĭ-bŭs | Ī-ris. Right, and it agrees with the drafter's note.
- **91 *Europamque Asiamque et***: Eū-rō | pam-qu(e) Ă-sĭ | am-qu(e) et | foe-dĕ-ră | sol-vĕ-rĕ | fur-to (13). Right.
- **31 *Troes***, at the end of the line, is two syllables. Right. **60 *fuit Xanthum et Simoenta***: right.
- **41 *Italum*** is short *Ĭ-* here, the only fit. **10 *suasit*** has consonantal *u*. **66 *s(e) inferre***: right.
- **44 *coniunx*** and **71 *Tyrrhenamque fidem aut***: right (44 is entered for *Teucris*).
- **54 *Ausoniam: nihil***: no elision, because *nihil* begins with *n*. …Au-sŏ-nĭ | am nĭ-hĭ | lur-bĭ-bŭs | in-de: right.

## Refused or upheld findings
1. **10.20 *Rutulli* (misprint, upheld).** The Latin Library has *Rutuli*, and the metre needs it. `t` keeps the print, and `l`/`i` read "Rutulians". The note opens in the rule-5b form.
2. **10.36 *repetem* (misprint, upheld).** It should be the deliberative subjunctive *repetam*, which the Latin Library has. The note opens in the rule-5b form.
3. **No other misprints.** I checked:
   - the capital *O* twice at 18 (the interjection)
   - *Fortuna* at 49 (personification)
   - no commas inside the brackets at 20–21
   - *conamur, nos, an* at 89 (an editorial choice)
   - every capital after a stop
   - Greenough's spellings (*moerorum*, *volnera*, *volgare*, *inpulsus*, *adspectat*, *exscidia*, *adsurgis*, *inrita*, and the *-is* accusatives)

   Upheld.
4. **Bracketed lines 20–21 and 27** are kept inside [ ] in `t` and `l` and explained in the notes. Upheld.
5. **62 / 62b** are cut as two units and explained in the note to the 62b unit. Upheld.
6. **Latin Library variants.** *fossas/fossae* (24) and *tu/et* (83) are noted because they change the sense or the rhetoric. *quamcumque/quacumque* (49) is not noted because it does not. The orthographic variants are ignored. Upheld.
7. **84 *contra*** as an adverb, with *Rutulos* the object of *iuvisse*. Upheld; it is the usual construal.
8. **57 *exhausta (esse)*** as the third infinitive. Upheld.
9. **71 *agitare*** governing both *fidem* and *gentis*. Upheld; it is defensible.
10. **87 *urbem*** as the Latin state. Upheld.
11. **44 *null(a) est*** listed as elision, not prodelision. Upheld; either is acceptable.
12. **18 hiatus of *O***, stated in the note. Upheld; the scan now agrees (M3).
13. **Note 6–7, "the poem shows no such scene"**, about Jupiter's earlier ban. Upheld.
14. **Note 88–90a, *qui… obiecit* = Paris.** Upheld. The masculine *qui* supports it, though some see a veiled thrust at Venus.
15. **Note 76, *Pilumnus avus*.** At 9.4 Pilumnus is *parentis*, "ancestor". *avus* can be loose, and the note follows the text. Upheld.
16. **Note 29–30, Iliad 5 (Aphrodite wounded as she carried Aeneas out).** Accurate. Upheld.
17. **Attributions from memory, confirmed:**
    - Ennius as the source of the *divom pater atque hominum rex* formula, and *quianam* as an Ennian archaism
    - Homer's χρυσέη for Aphrodite
    - Diomedes at Arpi
    - Iliad 8's ban on the gods

    Kept as written.
18. **Echo check.** No distinctive echo of a known English version was found. "father of the gods and king of men" is the stock rendering of a formula, and the other `i` lines are the plain sense of the Latin. Upheld.
19. **Speech marks** (“ 6 / ” 15; “ 18 / ” 62; “ 63 mid-line / ” 95). They agree in `t`, `l` and `i`. Upheld.
20. **Advisory: none (upheld).** It is a council of the gods with no violence on stage.
21. **`about`, title, part names.** They are accurate and contain no echo. Unchanged.

## For the owner (QUESTIONS.md)
- **Misprints (rule 5b: `t` as printed, `l`/`i` corrected, the note opens with the print's reading):** 10.20 *Rutulli* (for *Rutuli*) and 10.36 *repetem* (for *repetam*).
  - The 10.20 scan-fix spells *Rutulli* to match the printed words but scans *Rutuli*. If rule 5 is ever applied to the source, that entry must change to `Ru⏑tu⏑4li–`.
- **Half-line 62b numbering.** The validator needs feet numbered from 1, so 10.62b is `1Tum– 2re–gi⏑a⏑ 3Iu–no×`. In the verse these are feet 4b–6.
- **Unchecked attributions from memory:** Iliad 4 and 8 openings; Iliad 5 (Aphrodite wounded, Apollo's cloud and phantom); Ennius for the formula and for *quianam*.
- **Advisory:** none taken.
