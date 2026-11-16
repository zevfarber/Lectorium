# Review — aeneid-091 (Aeneid XII.1–106), adversarial reviewer

**Severity counts:**
- **Major: 14.** Scansion errors on 14 lines: 26, 28, 31, 48, 54, 58, 63, 65, 66, 72, 78, 80, 83 and 88. The scanner flagged none of them; nine had a cost of 0.0 to 0.3.
- **Medium: 2.**
- **Low: 29.** That is 28 text edits (one of them to `about`) and 1 syllable-division scan-fix (17).
- **Refused or upheld without change: 24.**
- **Scan-fixes added: 15.** They were written directly into `scan-fixes.json` by `drafts/aeneid-091/add_scan_fixes.py`, with keys 12.17, 12.26, 12.28, 12.31, 12.48, 12.54, 12.58, 12.63, 12.65, 12.66, 12.72, 12.78, 12.80, 12.83 and 12.88. They are appended after 11.910 in the existing `{"sc": [...], "why": "..."}` format. The git diff shows additions only.

Nothing blocks the build. For QUESTIONS.md, see "For the orchestrator".

## How the review was done

**Pass 1** went through all 55 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- the cross-references that can be checked in the pinned source: XI.434–444, XI.115–118, VII.96–101, XI.845, X.76, IX.3–4, IV.215 and XII.595–603;
- the speech marks: six speeches, at 11–17, 19–45, 48–53, 56–63, 72–80 and 95–100;
- the misprint decisions;
- the `p` flags at 1, 18, 54 and 81, which are all right.

I hand-scanned all 106 lines by quantity and compared each with the scanner's fit. `scan_check.py` is 090's, pointed at 091, and runs the scanner the way `build_aeneid.py` does. Sources were the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2:**
- I re-read every changed field.
- I re-read all `l` for words carried into the wrong line, which turned up the 57–58 duplication.
- I re-read all `i` for subject/object reversals, tense drift and remembered phrasing.
- I re-checked the rule-5b note form, which turned up 81.

**Script runs.**
- The drafter's file round-trips byte-identically through `aeneid_lib.jdump`.
- `review_edits.py` runs once from the drafter's file and applies 30 edits. Each old string is asserted to occur exactly once.
- The guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn` and `part` are unchanged;
  - `l` has as many lines as `t`;
  - no `i` contains a line break;
  - notes run 40–134 words;
  - `t`, `l` and `i` each have 6 “ and 6 ”.
- `review_check.py` is 090's, with `EXEMPT = NOTE_MARKS = {43, 45}`. It prints no faults and `BUILD REPLICA: OK`.
- `scan_check.py` applies all 15 entries. It reports no metre failures, and every unit's `sc` lines up.
- `make_units.py` was not touched and still holds the drafter's strings. Build from `units.json`; do not re-run `make_units.py`.

## Scansion (major, one per line; plus one low)

| line | scanner (cost) | right reading |
|---|---|---|
| 26 | 0.3 | *sublātis* has a long *-lā-* and *-tīs*, and *ăpĕrīre* has a short *a-pe-*: sub-lā \| tī-să-pĕ \| rī-rĕ-dŏ \| lī-sĭ-mŭl \| hōc ă-nĭ \| m(o) hau-rī (16). The scanner had *la-* and *-tis* short and *a-pe-* long. |
| 28 | **0.0** | It should be *dīvīque hŏmĭnesque*: fās ĕ-răt \| id-qu(e) om \| nēs dī \| vī-qu(e) hŏ-mĭ \| nēs-quĕ că \| nē-bant (15). The scanner had *di-vi* short and *ho-mi* long. |
| 31 | **0.0** | **Hiatus** at *genero, arma*: the long dative *-ō* does not elide at the pause, and *gĕnĕrō* is short-short. The line is prō-mis \| s(am) ē-rĭ-pŭ \| ī gĕ-nĕ \| rō ar \| m(a) im-pĭ-ă \| sump-sī (15). The scanner elided the *-o* and made *ge-ne* long. This is the only fit with standard quantities: 14 syllables would need three dactyls. |
| 48 | 0.6 | *prō mē* are long and *gĕrĭs* is short: Quam prō \| mē cū \| ram gĕ-rĭs \| hanc prĕ-cŏr \| op-tĭ-mĕ \| prō mē (15). |
| 54 | **0.0** | It should be *rēgīnă* and *nŏvā*, as in 1.522: At rē \| gī-nă nŏ \| vā pug \| nae con \| ter-rĭ-tă \| sor-te (14). |
| 58 | **0.0** | *requiēs* has three syllables, rĕ-quĭ-ēs, as *requiem* at 4.433: tū rĕ-quĭ \| ēs mĭ-sĕ \| rae dĕ-cŭs \| im-pĕ-rĭ \| um-quĕ Lă \| tī-nī (17). The scanner ran *requ-ies* together. |
| 63 | 1.2 | The *Ae-* split: *gener(um) Aenēān*, read nec gĕ-nĕ \| r(um) Ae-nē \| ān cap… (15). |
| 65 | 0.8 | *quoi* (= *cui*) is one long syllable, as at 7.692 and 10.530: …gĕ \| nās quoi \| plū-rĭ-mŭs… (14). The scanner read *quŏ-ĭ*. Both readings fit the metre, but disyllabic *cui* is not Virgilian, and its *-ī* would be long anyway. |
| 66 | **0.0** | *subiēcit* has a consonantal *i*: sub-iē \| cit rŭ-bŏr \| et că-lĕ \| fac-tă pĕr \| ō-ră cŭ \| cur-rit (16). The scanner read *su-bi-e-cit* and counted 17. |
| 72 | 0.6 | *nē mē* are long, *lăcrĭmis* has two short syllables, and *ōmine* has a long *o*: Nē quae \| sō nē \| mē lă-crĭ \| mīs nē \| v(e) ō-mĭ-nĕ \| tan-tō (14). |
| 78 | 1.0 | *Teucros* and *Teucrum* each have one *eu*: nōn Teu \| crōs ă-găt \| in Rŭ-tŭ \| lōs Teu \| cr(um) ar-mă quĭ \| ēs-cant (15). |
| 80 | **0.0** | *coniunx* is *con \| iunx*: il-lō \| quae-rā \| tur con \| iunx Lā \| vī-nĭ-ă \| cam-pō (13). The scanner read *co-ni-unx*. |
| 83 | 0.3 | *Ōrīthyia* has four syllables, Ō-rī-thyi-a (Greek Ōreithyia), and *dĕdĭt* is short: Pī-lum \| nō quōs \| ip-să dĕ \| cus dĕ-dĭt \| Ō-rī \| thyi-a (14). The fifth foot is a spondee. The scanner had *de-dit* long and *O-ri* short. |
| 88 | **0.0** | It should be *lōrīcam* and *ŭmĕrīs*: cir-cum \| dat lō \| rī-c(am) ŭ-mĕ \| rīs sĭ-mŭl \| ap-tăt hă \| ben-dō (15). |

**17 (low): syllable division only.** The scanner wrote *co-niunx*. The quantities are right, and the division is now *con-iunx*, as at 2.519 and 2.673.

**Checked by hand and found right, so no entry.** These include the drafter's list:
- **12** *ignāv(i) Aenĕădae*: *Ae-* is one syllable and *-nĕ-ă-* is short, as at I.157. The scanner is right.
- **60** *Teucris*: one *eu*.
- **30** *con-iu-gis*: a consonantal *i*, correctly divided.
- **40** *consanguinei*: five syllables, *-nĕ-ī*.
- **84** *anteirent*: *-tei-* is one syllable.
- **87** *dehinc*: two syllables; one does not fit (Ip-sĕ dĕ \| hinc au…). *ŏrĭchalco* has a short *ri*.
- **93** *aedibus*.
- **59** *in t(e) omnis*.
- **17, 64, 80** *Lā-*.
- **13**: *pater* lengthened on the beat before the pause (fourth foot *ter et*). This is the only fit.
- **68**: *ebur* lengthened in the same way (second foot *bur aut*). This is the only fit.
- **89**: *ensemquē clipeumque*, with the first *-que* lengthened (Homeric licence, as III.91). This is the only fit.
- **35**: *spēs Ĭtălās*, with short *I* (forced).
- **42**: *cōnūbia*.
- Costs of 1.5–1.6 at 17, 30, 59, 60 and 84 are all right.

The 13/68/89 lengthenings are now pointed out in the notes (L14–L16).

## Medium

- **M1 (60, `l`).** "cease to join hands with the Teucrians" reads in English as making an alliance. *manum committere* is to engage in fight, and the note and `i` already say so. It now reads "cease to engage your hand in combat with the Teucrians".
- **M2 (46, `i`).** "it mounts the higher and grows worse for being treated". "Mounts the more" is a phrase I remember from a published prose version of this line. It now reads "it only surges further, and every attempt to treat it makes the sickness worse". "The cure" is still avoided, as the drafter intended.

## Low

**Elision lists and the rule-5b form** (L1–L4):
- **L1 (19–21).** The list was "e.g." and incomplete. It now gives all seven elisions, adding *virtut(e) exsuperas*, *aequ(um) est* and *atqu(e) omnis*.
- **L2 (38).** Added *s(um) adscire*.
- **L3 (31).** The hiatus *genero, arma* is now stated (see the scansion of 31).
- **L4 (81).** The note opened "A new paragraph in Greenough." before the print's reading. Rule 5b requires the note to open with the print's reading, so the order is swapped.

**Labels and facts** (L5–L13):
- **L5 (29).** *Victus… victus* frames the line, so it is not anaphora.
- **L6 (5).** *ille* "the hunters' famous quarry" was embroidery. It now reads "that lion, pointing at the beast as if it stood before us".
- **L7 (36).** "the fighting has lasted only days" was an unverifiable claim. It now reads "an exaggeration of how long the war has lasted".
- **L8 (40).** *consanguinei* "kinsmen through Amata" now gives both senses: Turnus's tie to Amata, or simply a kindred people of Latium.
- **L9 (88).** *umeris* was called "Greenough's spelling". It is now "also spelled *humeris*", as 090's L10.
- **L10 (83).** Pilumnus is "Turnus's grandfather (X.76)", checked in the source: *cui Pilumnus avus*.
- **L11 (83).** Added a note on Orithyia's four syllables and the spondaic fifth foot.
- **L12 (65).** Added that *flagrantis* is the *-is* accusative plural with *genas*.
- **L13 (65).** Added that *quoi* is one long syllable.

**Scansion pointers** (L14–L16): the scanner's own fits are kept. The notes now point out *pater* lengthened at 13, the first *-que* lengthened at 89 and *ebur* lengthened at 68.

**`l`:**
- **L17 (57–58).** "you are the rest, my wretched age" repeated the noun already given. It now reads "you are the rest, wretched as it is".

**`i`**, mostly precautions against phrasing remembered from published versions (L18–L27):
- **L18 (1–4).** "war's reverses", "blazes up unbidden": recast.
- **L19 (4–8).** "glories in tossing the shaggy mane" is now "exults as he shakes out the thick mane".
- **L20 (45).** "not swayed by his words in the least" is now "Words do nothing at all to bend Turnus's violence", which also matches *flectitur*.
- **L21 (62–63).** "quit this hateful daylight" is now "leave this light I have come to hate".
- **L22 (68–69).** "white lilies blush" is now "white lilies glow red".
- **L23 (69).** "came and went" is not in *dabat ore colores*. It now reads "the colours the maiden's face showed".
- **L24 (74).** "Turnus is not free to put off his death" is now "it is not in Turnus's power to put off his death".
- **L25 (81–84).** Two changes:
  - the past tense is now historic present, matching the units on either side;
  - *decus* "as a prize" is now "as a mark of honour".
- **L26 (87–88).** "stiff with gold and pale orichalc" is now "rough with gold and white orichalc", which follows the note's *squalentem* and *albo*.
- **L27 (97–100).** "Grant me to lay low the body" is now "Grant that I may bring down the body".

**`about`:**
- **L28.** "begging Turnus to … go home to his old father" was wrong: Latinus asks only for pity for Daunus (*miserere parentis*). It now reads "and to pity his old father far away in Ardea".

## Refused or upheld (no change)

1. **12.45 `dividit. ”Haudquaquam`: upheld as a rule-5b misprint.** This is the fifth case of the Perseus spacing pattern after 10.451, 11.98, 11.827 and 11.849. `t` is as printed, `l` and `i` close Latinus's speech after *dividit.*, and both notes (43 and 45) open with the print's reading in the 849 form.
2. **12.52 lower-case `longe`: upheld as a misprint for *Longe*** (item 43 practice). The stop itself is right, because the boast ends and the sneer begins.
3. **12.60, 12.81 and 12.89, full stop plus lower case: upheld as misprints for a comma.** The syntax allows only the run-on reading:
   - at 60, the *per… per…* oath needs *oro*;
   - at 81, *ubi… recessit* needs *poscit*;
   - at 89, *ensem* takes up *ensemque*.

   The units run across the stop, as in 019, 020 and 063, so no boundary sits at a misplaced stop.
4. **12.55 *monitura* kept as printed: upheld.** It construes ("meaning to counsel him"), so it is a doubtful reading, not one with a single possible correction, and rule 5b says to keep the print. The note gives the Latin Library's *moritura*. Greenough himself prints *moritura* at 12.602 (checked), of Amata's death, which is a point for the owner but not grounds to emend.
5. **12.104 *atque* (LL *aut*): upheld**, noted briefly.
6. **53 *sese occulat*, the goddess hiding herself: upheld.** *sese* refers to the subject of its clause, *quae*.
7. **46 `l` "sickens with the healing": upheld.** Only `i` was changed (M2).
8. **25 *genus* as accusative of respect: upheld.**
9. **79 *et Rutuli* as a loose second subject of *quiescant*: upheld.**
10. **72 *Ne… prosequere* as *ne* plus the present imperative of the deponent: upheld.**
11. **44 *nostro sanguine* "his and Aeneas's": upheld.**
12. **68 *multa* with *rosa*: upheld.** It cannot be settled by metre, because it is the line's last syllable. *rosā* is long in 69, so the ablative stands. The `l`, `i` and note agree.
13. **31 *genero* as a dative of separation: upheld.**
14. **41 *prodiderim* as perfect subjunctive: upheld.** The future perfect would be *prodidero*.
15. **96 *gerit*, with *gerebat* understood for Actor: upheld.**
16. **Unit 35's "the one moment in the poem where Lavinia shows any feeling": upheld** as a fair critical commonplace.
17. **Cross-references checked in the source, all right:**
    - XI.434–444 (Turnus's promise);
    - XI.115–118: Aeneas says Turnus should have met him in arms. Kept as "offered single combat", which is a fair reading;
    - VII.96–101 (Faunus's oracle);
    - XI.845 *indecorem*;
    - IV.215 *semiviro comitatu*;
    - 45 = 9 *violentia*.
18. **Homeric and Georgics references from memory: upheld** as marked. They are Iliad XX.164–175, V.311–345, IV.141–147, VI.487–489, XIX.400–403 and XVIII.205–214, and Georgics III (the bull, close to III.232–234).
19. **"by tradition her sister's son" (Turnus and Amata): upheld** as marked from memory. Venilia is Turnus's mother (X.76). Her being Amata's sister is Servius's, and is unchecked.
20. **The drafter's elision lists at the other 51 units: checked line by line, all right.** No elision runs across a line-end, at 73/74 or elsewhere.
21. **The `i` at 14–17 "take Lavinia as his bride"**, where the Latin has Lavinia as subject: upheld. The sense is the same.
22. **11–12 *Aeneadae* "sons of Aeneas" with contempt: upheld.**
23. **No advisory: upheld.** The threat to foul Aeneas's hair is talk, and Amata's death is only foreshadowed.
24. **No set piece and no new house rendering: upheld.**

## For the orchestrator

- **`scan-fixes.json`** now holds 15 new keys, 12.17–12.88 as listed above, appended after 11.910. Nothing else in the file changed.
- **QUESTIONS.md (rule-5b record, as items 81 and 82):**
  - 12.45 `dividit. ”Haudquaquam` should read `dividit.” Haudquaquam`. This is the fifth case of the pattern, which supports item 82's suggestion to fix the spacing in `archive_aeneid.py`.
  - 12.52 lower-case `longe` should be *Longe*.
  - At 12.60 `recumbit). unum`, 12.81 `recessit. poscit` and 12.89 `cristae. ensem`, the stop should be a comma.
  - `t` is as printed throughout, with `l` and `i` corrected.
- **Readings for the owner:**
  - 12.55 *monitura* is kept, with LL *moritura* noted. Greenough prints *moritura* at 12.602.
  - 12.104 *atque* is kept (LL *aut*).
- **Scansions resting on judgement:**
  - 12.31 hiatus *genero, arma*, which is the only fit;
  - 12.83 *Ōrīthyia* with four syllables and a spondaic fifth foot, which rests on the long *-rī-* from Greek *ei*. The five-syllable alternative *Ō-rĭ-thy-ī-a* would need a short *ri*;
  - 12.65 *quoi* as one syllable. Both readings scan, so this is a judgement.
  - The scanner's lengthenings at 12.13 *pater*, 12.68 *ebur* and 12.89 *-que* were confirmed and left without entries.
- **Unchecked from memory:** the references listed in item 18 above, and Venilia as Amata's sister (Servius).
- **No new house renderings, no set pieces, no advisory.**
