# aeneid-006 — review (I.466–560)

Adversarial review in two passes, from the Latin and public-domain references only (Lewis & Short, Allen & Greenough, Conington's general
sense, Servius for the Rhesus oracle). No modern translation was opened and no English wording was recalled as a source.

- **Pass 1:** every unit, field by field. I checked every grammatical label in every `n` against the form in its line, the Latin against
  `l` word by word (line division included), `l` against `i`, remembered English in `i`, speech marks, and the factual and
  cross-reference claims in `n` and `about`. Then I hand-scanned all 95 lines, syllable by syllable, against the quantities themselves (not
  merely "is it a valid hexameter").
- **Pass 2:** a re-read of the edited file. It caught 16 more items (marked *P2* below; three of them corrected my own pass-1 wording).
  A script then applied `scan-fixes.json` over `scan_latin.scan_story` exactly as `build_aeneid.py` does, and ran the validator's
  hexameter test over all 95 lines: **93 pass**, the two half-lines (534, 560) cannot pass by design (see "Blocking for the build/validator").
  No UNRESOLVED report is left. COSTLY reports remain for 474, 530 and 555: I hand-checked them and the scanner is right.
- **The full build was not run** (per instructions).

All edits were made to `units.json` by script (json load / modify / dump, `ensure_ascii=False`, `indent=1`). **`t`, `ln`, `p` and `v` are
untouched** (asserted by the script, unit for unit). `draft.py` was **not** updated and now disagrees with `units.json`. **Do not re-run
`make_units.py`**: it would overwrite the review.

**Counts:** Major 9 · Medium 18 · Low 32 · scan fixes added 15 (12 lines the scanner had wrong or could not fit, 2 half-lines,
1 carrier line) · refused / verified and kept 17. Changed: 40 of 45 units (0 `t`, 22 `l`, 16 `i`, 38 `n`) and `about`.

Speech marks: “ opens unit 22 (522) and ” closes unit 42 (558) in `t`, `l` and `i`. There is one of each per layer.

Remembered English: checked from memory of the well-known versions, not by collation. I.530 `i` ("There is a place the Greeks call
Hesperia, an ancient land…") was close to the stock shape of the familiar versions. It is rephrased ("There is a region, Hesperia to the
Greeks…"). No other line is a distinctive echo.

## Blocking for the build/validator (for the orchestrator / owner)

**Half-lines 534 (`Hic cursus fuit:`) and 560 (`Dardanidae.`).** These are the first hemistichs in the pipeline. The build accepts them:
`scan-fixes.json` now has hand entries, and the build checks only that the words match. **`validate_aeneid.py` will not pass them.**
Section 4 requires six feet on every line. Worse, `feetpat[5]` raises an **IndexError**, because these lines have only 2 feet. So the
validator crashes at line 534 rather than failing cleanly. It needs a rule for hemistichs, for example:
- a `"half": true` key on the scan-fixes entry, or a list of half-lines in `conventions.md`;
- the validator skipping the six-foot test for those lines, and checking only feet in order 1…k with one final ×.

There are ~58 such lines in the poem, so this will recur. I did not touch the validator (outside the reviewer's role). This belongs in
`QUESTIONS.md` / `conventions.md`. The hand entries use the ordinary format, with the last syllable marked ×.

## Major (false label or false statement of fact)

1. **#1 `n` (469)** — "'Rhesi' — Greek genitive." It is the ordinary Latin second-declension genitive of `Rhesus`. Fixed.
2. **#1 `n` (473)** — "'gustassent' and 'bibissent' are the contracted pluperfects for 'gustavissent', 'bibissent'." Only `gustassent` is
   contracted. `bibissent` is the regular pluperfect subjunctive of `bibo` (perfect `bibi`). Fixed.
3. **#3 `n` (477)** — "'cervixque comaeque' — the first '-que' marks the pair, with 'et' on the second element". There is no `et`. It is the
   double `-que … -que`. Fixed.
4. **#6 `n` (483)** — "Two events of the Iliad (22 and 24)". Achilles does not drag Hector round the walls in Homer. He chases the living
   Hector three times round them, drags the body to the ships (22), and later drags it three times round Patroclus' tomb (24). The
   dragging round the walls is a later version. Fixed (wording settled in P2).
5. **#7 `n` (487)** — "'inermis' is the accusative plural masculine in -is". It agrees with `manus` (feminine), "unarmed hands". As
   written, the note implied agreement with Priam, which is impossible (`Priamum`, accusative singular). Fixed.
6. **#9 `n` (490)** — "'Amazonidum' — a Greek genitive plural in -um (for -arum, as in 'Danaum')". `Amazonis, -idis` is third
   declension, so `-um` is its regular ending, not the contracted type. Fixed.
7. **#15 `n` (511)** — "'Teucrorum' — the old genitive plural in -um." `Teucrorum` is the regular `-orum`. Replaced with a gloss of `Teucri`.
8. **#15 `n` (512)** — "'dispulerat ... avexerat' — pluperfects (-erat for -verat …)". Neither is syncopated: perfects `dispuli` and
   `avexi`. Fixed.
9. **#41 `n` (554)** — "The Trojans name Italy and Latium without having been told that Italy is where they are going". This is false:
   Aeneas has told them *tendimus in Latium* (I.205, checked in the source). Replaced.

## Medium

10. **#0 `n`** — "'Graii' is the old form of 'Graeci'." `Graius` is a separate, poetic word beside the prose `Graecus`. Also "'Phryges' is
    the usual poet's word" became "a poets' name". Fixed.
11. **#1 `l`** — The line division was broken: "he recognises, weeping" (`adgnoscit lacrimans`, line 470) sat in line 469. Restored. Also
    `avertit … in castra` → "drives off … into the camp", and `pabula` → "fodder".
12. **#1 `n`** — The Rhesus oracle was stated without qualification. It is a later story (Servius), not in Homer: now said so. "The
    historical present ('adgnoscit', 'avertit')" was also wrong, since `avertit` may equally be perfect. Now said.
13. **#2 `n` (474)** — "Troilus, the youngest son of Priam" and "Troy could not fall if he lived to twenty" are not verifiable from the
    references, and are deleted. "The story is not in the Iliad, but was a favourite in later art" was also imprecise. It now reads:
    Homer only names him (Iliad 24.257); the ambush was told in the Cypria and was a favourite of Greek vase-painters.
14. **#7 `n` and `l` (485–487)** — "three 'as' clauses" was wrong: it is one temporal `ut` repeated before each object of the single verb
    `conspexit`. In `l`, "as he sees" stood in line 486, though `conspexit` is in 487. The line division is restored ("…he beheld").
15. **#8 `n` (489)** — "Memnon … he is in the Epic Cycle, not Homer." Homer names him (Odyssey 4.188, 11.522); his story was in the
    Aethiopis. Fixed; the three syllables of `Eoas` are noted.
16. **#9 `l` and `n` (490–493)** — `l` put Penthesilea in line 490 and "raging" in 491; the line division is restored. `mammae` was given as
    genitive with `cingula`. It is dative with the compound `subnectens`; `cingula` is a poetic plural. The unverifiable "right" breast and
    "inspired" (of `furens`) are deleted.
17. **#10 `n`, `l`, `i` (494–497)** — Several problems:
    - The note called `dum` + present "the historical present of a continuous action". It is the regular idiom, `dum` + present
      indicative with a past main verb.
    - "Dido is named here … for the first time" is false: she is named at I.299, 340 and 446. Now "appears in person for the first time".
    - `incessit` was "went in"; it is `incedo`, to advance in state.
    - `l` had "seemed" for `videntur`.
    - *P2*: the tenses in `i` were made consistent.
18. **#12 `n` (502)** — The line was called "chiastic". Genitive–adjective–verb–subject–noun is interlaced, not chiastic. Fixed.
19. **#21 `n` (520)** — `Postquam introgressi` was explained as a perfect participle construction, and `data copia` as "having been given".
    Both are finite verbs with `sunt` / `est` left out. Fixed. "Ilioneus is the Trojan spokesman, also at I.611" was also wrong (at 611
    Aeneas greets him). It is replaced by I.120 (his ship) and VII.212 ff. (his speech to Latinus).
20. **#29 `n` (534)** — "only seven syllables?" is false: `Hic cursus fuit` has five syllables, two and a half feet. Pipeline talk ("the
    tap-unit and the scansion") is removed. The Life's account is stated soberly.
21. **#32 `i` and `n` (539–540)** — `i` contained a line break. It is now one line. `barbara` was called "a predicate adjective"; it is
    attributive with `patria` ("what country so barbarous").
22. **#35 `n` and `l` (542–543)** — "'fandi' / 'nefandi' are the genitives of the gerund and its negative". They are `fandum` / `nefandum`,
    gerundive forms used as nouns, in the genitive with `memores`. Also, `sperate` here means "expect", not "hope". `l` "yet hope that
    there are gods" became "yet expect gods". The note says so.
23. **#36 `n` and `l` (544–545)** — The note glossed "nor was there anyone greater in piety (nor) in war". `pietate` goes with `iustior`
    and `bello … armis` with `maior`; `quo` is the comparison for both. `l` line 2, "nor in piety, nor greater…", was not English that
    matched the Latin. Both are rewritten, and `i` is aligned.
24. **#37 `n` (546)** — "'virum' in apposition … if the fates preserve (him) as a man". `quem … virum` is a connecting relative used as an
    adjective: "and if the fates preserve this man". Fixed, with `l` to match.
25. **#38 `n`, `i` (548–549)** — "the Latin Library prints 'poeniteat', the older form". That is not an older form, and conventions say
    orthographic variants are not noted. Deleted. `i` "you will not regret" disagreed with `l` and with the subjunctive. Both are now
    "nor should you regret". *P2*: the `l` line division is restored (`officio` is in 548).
26. **#42 `n` and `l` (555–558)** — "'unde huc advecti' is a participial clause". It is finite with `sumus` left out. In `l`, "let us seek"
    stood in line 557, though `petamus` is in 558. Restored.
27. **#44 `i` (559–560)** — `i` contained a line break. It is now one line.

## Low

28. **`about`** — "Troilus dragged from his chariot": he clings to it. Now "dragged behind his chariot".
29. **#0 `l`** — "high-crested" → "crested" (`cristatus`). In `n`, "the shield-scenes of the Iliad" is now named for what it is: an
    ecphrasis in the manner of the Shield of Achilles (Iliad 18).
30. **#1 `i`** — "in the first sleep" → "in their first sleep".
31. **#2 `i`** — "weapons thrown away" → "weapons lost" (`amissis`). In `n`, "'Achilli' is the old dative" (*P2*) became simply
    "dative of 'Achilles'".
32. **#3 `n`/`i`** — "its end draws a line" is now just that the reversed spear trails a line. *P2*: the unverifiable "still in his grip"
    is dropped, and `i` is now "his reversed spear".
33. **#4 `n`/`l`** — The prayer in Iliad 6 is to break Diomedes' spear and pity the city, not "keep him out of the city". A gloss of
    `suppliciter` is added, and `l` line 3 now matches the participle (`tunsae`, "beaten").
34. **#6** — The wording of the Homeric facts was refined in P2 (see Major 4).
35. **#7 `i`** — "truly lets out" → "indeed gives". "See I.462 … which this scene is meant to enforce" is deleted (interpretive).
36. **#11 `n`/`l` (498–501)** — "Virgil replaces the Greek mountain with the Eurotas" is muddled, since both are Greek. Now: Homer's
    Taygetus and Erymanthus become the Eurotas and Cynthus. In `l`, `oreades` is moved into line 500, where it stands. The quantities
    Ŏrēădes (four syllables) and Dīāna are noted.
37. **#12 `l`/`i`/`n`** — "among the midst" → "through their midst". `i` "touches" → "thrills" (`pertemptant`). "The kingdoms to come …
    long irony" is tightened, with a reference to I.12–22. *P2*: `talis … talem` is explained ("talem" agrees with "se").
38. **#13 `n`** — "'subnixa' being a deponent-looking form" is wrong, since it is a deponent participle. "'resedit' — she sat down again,
    after her walk" was speculative. Both are fixed.
39. **#14 `l`/`n`** — The imperfects `dabat … aequabat … trahebat` are rendered as such.
40. **#15 `n`** — "Antheus, Antheus (I.181)" was a duplication; the list is now Antheus, Sergestus and Cloanthus. `alias … oras` is
    identified as an accusative of goal. *P2*: my pass-1 `l` rearrangement of 509–510 was ambiguous ("Aeneas, coming up…"), so I reverted
    to the drafter's order.
41. **#16 `l`/`n`** — "Both he was stunned at the same time" → "He was stunned at once himself, at once struck was Achates". `obstipuit`
    is identified as the perfect of `obstipesco`.
42. **#17 `n`** — "the type of word that fools a scanner" (pipeline talk) is removed. The note now says that `coniungere` has four
    syllables with a consonantal i.
43. **#18 `i`** — "holds them back" is not `turbat`; now "troubles their minds".
44. **#19 `n`** — The gloss on `linquant` is clarified, and `quid` = "why" is noted.
45. **#20 `l`/`i`/`n`** — `veniam`: "pardon" / "mercy" → "favour" / "a kind hearing", to match the note. The postponed `nam` is noted.
    *P2*: a duplicated gloss is removed.
46. **#22 `n`** — "the infinitive for the result" is a mislabel; now "a poetic construction". "It echoes … VI.853" is anachronistic and
    became "compare". *P2*: "frames the construction … encloses 'condere Iuppiter'" → "frames 'cui condere Iuppiter'".
47. **#23 `n`** — "the queen's name second": `te` is a pronoun. The note now says that `Troes` has two syllables.
48. **#25 `l`/`n`** — `venimus` stands in 528, and `l` now has it there (*P2* wording). The note adds that `populare` is the active form of
    the usually deponent `populor`.
49. **#26 `n`** — "The claim is true of Aeneas' people" is a value judgement, and is trimmed.
50. **#27 `n`/`i`** — "'Grai' — the old form for 'Graii'" → "contracted". The asyndetic relative is noted. The note now says that 530–533
    return word for word at III.163–166 (a certain repetition). `i` is rephrased (echo caution, see above).
51. **#28 `i`** — "called the people Italian" → "called the nation Italy" (`Italiam … gentem`), to agree with `l`.
52. **#30 `n`** — The quantity Ŏrīōn (three syllables, short O) is noted.
53. **#33 `n`** — "'harenae' is a genitive (or dative)": the dative is implausible and is deleted.
54. **#35 `n`** — "'temno', rare" → "the poets' word for 'contemno'".
55. **#39 `n`/`l`/`i`** — The Latin Library variant `armaque` is restated plainly. Acestes is placed in context: he already gave the
    Trojans wine at I.195–196, and the duplicated "Book V" is removed. `i` "who is famous and of Trojan blood" → "a king of illustrious
    Trojan blood", and `l` is aligned (*P2*).
56. **#40 `i`/`n`/`l`** — `i` dropped `liceat` and is now "Let us be allowed…". `silvis` is "in the woods" (ablative of place), not
    "from the forests".
57. **#41 `l`** — `tendere` stands in 554, and `l` now has it there.
58. **#44 `n`** — "'ore' … ablative of manner" → "of means". The half-line status is noted, with a cross-reference to 534.
59. **#1, #9, #10, #42 (*P2*)** — I trimmed notes that had grown past the validator's 140-word warning (largest now 138).

## Hand scansions added to `scan-fixes.json` (15)

| line | scanner had | correct |
|---|---|---|
| 1.489 | `Eo-` one syllable, `a-ci` long (COSTLY) | Ē-ō-ās three syllables, ăcĭēs |
| 1.491 | `-lea` by synizesis, `fu-` long (no flag) | Penthĕsĭlēă five syllables, fŭrens |
| 1.494 | `A-e-ne` dactyl | Ae-nē-ae, Dardani(o) elided |
| 1.499 | `Di-a` short-short, `cho-` long (no flag) | Dīāna, chŏrōs |
| 1.500 | `-rea-` by synizesis, `-des` long (no flag) | Ŏrēădĕs four syllables |
| 1.509 | `A-e-ne` dactyl | Ae-nē-ās, subit(o) elided |
| 1.514 | `co-ni-un-ge-re` | con-iun-ge-re, consonantal i |
| 1.522 | `re-gi` short, `na`, `no` long (no flag) | Ō rē-gī-nă nŏ-vam |
| 1.524 | `Troes` one syllable, `mi-se` long (no flag) | Trō-ēs (long by position), mĭsĕrī |
| 1.534 | UNRESOLVED | half-line: Hīc cur-sus fŭ-ĭt |
| 1.535 | `su-bi` long, `Orion` two syllables (no flag) | sŭbĭt(o), Ŏrīōn three syllables |
| 1.544 | `A-e-ne` dactyl | Ae-nē-ās |
| 1.556 | `Iuli` two syllables, spondaic fifth (COSTLY) | Ĭūlī three syllables |
| 1.559 | (second unit had no sc: carrier for 560) | checked; Ilioneus with Greek eu |
| 1.560 | UNRESOLVED | half-line: Dar-dă-nĭ-dae |

Six of these lines were not flagged by the scanner at all (491, 499, 500, 522, 524, 535). The scanner found a cheap but wrong fit.

## Refused, or verified and kept

1. **1.474 (COSTLY 2.0)** — The scanner is right: Part(e) ălĭ | ā fŭgĭ | ēns ā | mīs sīs | Trōĭlŭs | ar-mis. No entry.
2. **1.530 (COSTLY 2.0)** — The scanner is right: `Grai` is two syllables (Grā-ī), cōgnōmine. No entry.
3. **1.555 (COSTLY 3.2)** — The scanner is right: sīn ab | sūmp-tă să | lūs et | tē pă-tĕr | op-tŭ-mĕ | Teu-crum. No entry.
4. **Hiatus** — There is none in this part. 1.469 `procul hinc Rhesi` and 1.527 involve consonant endings only. The `eu` lines
   498 (`Eurotae`), 511 (`Teucrorumque`), 521 (`Ilioneus`) and 555 (`Teucrum`) are already right in the scanner. No other prefix + i
   lines.
5. **1.542/543** — Greenough prints no comma after `arma`. The source is left alone, and the note's remark stays.
6. **Latin Library variants** — `maxumus/maximus`, `optume/optime`, `Lybiae/Libyae` and `paeniteat/poeniteat` are orthography. Only
   Greenough's spellings are glossed, and the `poeniteat` remark is deleted. `arvaque/armaque` changes the sense and stays in the note.
7. **#0 "'Namque' explains why he is weeping"** — Kept: it picks up the tears of 465.
8. **#9 "Virgil is preparing Dido"** — Kept. The juxtaposition is in the text (493 → 496).
9. **#8 "Aeneas fought Achilles, Iliad 20"** — Kept (true).
10. **#15 "Sergestus and Cloanthus … Roman families (V.121–123)"** — Kept (Sergii, Cluentii).
11. **#2 "'curru' dative/ablative"** — Kept. Both analyses are standard.
12. **#4 `tunsae pectora`, accusative of respect** — Kept.
13. **#36 `l` "A king we had, Aeneas"** — Kept literal. The shape is forced by the Latin and is not a distinctive echo.
14. **I.462 cross-reference in #7** — Deleted as interpretive, not refused (listed under Low 35).
15. **Caesura marks the scanner placed** (e.g. 521 after `placido`) — Not changed. Not a quantity error.
16. **No "confirmation" entries for scanner-correct COSTLY lines** — None added. The brief asks for entries only where the scanner is
    wrong; 559 is the only carrier.
17. **`draft.py`** — Not mirrored (`units.json` is authoritative, per the brief).
