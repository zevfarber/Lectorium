# aeneid-005 — review (I.387–465)

Adversarial review in two passes, from the Latin and the public-domain references only (Lewis & Short, Allen & Greenough, Conington's general
sense). No modern translation was opened and no English wording was recalled as a source.
Pass 1: every unit field by field (every grammatical label in every `n` against the form in its line; Latin to `l` word by word, including
the line division; `l` against `i`; remembered English in `i` and `l`; speech marks; factual and cross-reference claims in `n` and `about`,
the latter checked against the source text of Book I where they cite it: I.3, I.15–18, I.113–117, I.170, I.188, I.302, I.320, I.381),
then a hand scansion of all 79 lines, syllable by syllable, against the quantities themselves (not merely "is it a valid hexameter").
Pass 2: re-read of the edited file (three more items, listed under "Pass 2" below), and a script that runs the build's own scansion
code (`scan_latin.scan_story` plus `scan-fixes.json`, as `build_aeneid.py` does) and the validator's hexameter test over all 79 lines:
79 lines, 0 bad, no UNRESOLVED or COSTLY report left. The full build was not run (there is no `gloss.json` yet; the glosser comes next).
All edits to `units.json` were made by changing `draft.py` and re-running `make_units.py`. **`draft.py` and `units.json` agree**; `units.json` is
what the build reads. `t` was never edited; it is identical, unit for unit, to the draft's.

**Counts:** Major 8 · Medium 13 · Low 27 · scan fixes added 9 (8 lines the scanner had wrong or could not fit, 1 carrier line) ·
refused / verified and kept 22. Changed: 32 of 40 units (0 `t` cuts, 4 `l`, 10 `i`, 30 `n`) and `about`.

Remembered English: checked from memory of the well-known verse and prose versions, not by collation. Four lines were rephrased because
they sat close to a stock rendering (I.437 *O fortunati*, I.439 *mirabile dictu*, I.462, and a phrase in I.405); none of the others is a
distinctive echo.

**Process note for the owner.** `runbook.md` says a set piece listed in `conventions.md` that has not been decided stops the run. The drafter
did not stop at I.462 (*sunt lacrimae rerum*) but proposed a rendering in `new-renderings.md`. The reviewer has kept that route (reworded,
see Medium 20) and left the rendering as a proposal for the owner to confirm; the table in `conventions.md` is not touched here.

## Major (false label or false statement of fact in a note)

1. **#0 `n` (387)** — "`invisus` is a perfect participle used as an adjective, 'unseen' becoming 'hateful'." Wrong: `invisus` 'hated' is the
   adjective belonging to `invideo`; `invisus` 'unseen' is a different word (`in` + `video`). Also "the subjunctive" made specific: perfect subjunctive.
2. **#4 `n` (399)** — "`tuorum` is the old genitive plural of `tui`." Wrong on both counts: it is the ordinary genitive plural masculine of
   the adjective `tuus` used as a noun, not the contracted `-um` type, and not from `tui` (genitive of `tu`). The note had also sent the reader to
   "391" for `reduces`; it is 390 (Low 3).
3. **#6 `n` (402)** — `rosea cervice` "ablative absolute-like": it is an ablative of respect or manner ("with her rosy neck"), not any kind of absolute.
4. **#12 `n` (416–417)** — "`est` is understood, as `sunt` also is for the altars." The altars have their own verb, `calent`; nothing is understood for them.
5. **#24 `n` (436)** — "`fervet` — the third-conjugation form of `ferveo`." `fervet` is the ordinary second-conjugation form (the third would be `fervit`). Removed.
6. **#32 `n` (453–455)** — "The verb `miratur` serves both `dum` clauses." The first `dum` has `lustrat`, the second `miratur` (the note's own opening line says so). Rewritten.
7. **#39 `n` (464)** — "`inani` is placed after the verb, enclosing `animum pascit`." `pictura… inani` enclose `pascit` only; `animum` stands outside.
8. **#34 `n` (459–460)** — "`nostri` the possessive adjective, a genitive with `plena`." `nostri` is the possessive adjective agreeing with `laboris`;
   it is `laboris` that `plena` governs in the genitive. Rewritten.

## Medium

9. **#34 `n`** — "the `fidus Achates` of later books": the phrase is already at I.188 (checked in the source). Now cites it.
10. **#1 `n` (390–391)** — "`nuntio` governs an accusative with a participle": it is an accusative and infinitive with `esse` omitted; `reduces` agrees with `socios`,
    the participles with `classem`. Rewritten; `limina` (plural) glossed.
11. **#2 `n` (394–395)** — "`aperto… caelo` frames the line": the words stand on either side of `turbabat` and are split across two lines (394/395). Rewritten.
12. **#2 `n`** — "The usual reading is that they stand for the twelve ships": the reading is not verifiable from the Latin as "usual"; and "a bird of ill omen
    for the swans here (the storm, Juno's work)" was an unsupported equation. Kept only what the text gives: twenty ships (I.381), seven in harbour
    with Aeneas (I.170), one seen to sink (I.113–117), twelve unaccounted for; and Venus's own swans-to-ships comparison at 397–400.
13. **#23 and #24 `n` (434–436)** — "repeated almost word for word from Georgics 4.168 … 4.169": not checkable here (the Georgics are not in `source/`) and
    quoted by number from memory. Deleted from both notes.
14. **#23 `l` and `n` (435)** — `ignavom` agrees with `pecus`, not `fucos`; `l` ("the lazy drones, a herd") attached it to the drones. `l` now
    "the drones, a lazy herd"; the note says what it agrees with.
15. **#20 `n` (430)** — "bees at Iliad 2.87–93" and "Virgil used much of this passage in his own bee-book (Georgics 4)": line numbers and the Georgics
    claim not verifiable here. Kept only that bees as a simile for a busy crowd are Homeric (the Achaeans gathering, Iliad 2).
16. **#18 `n` (427)** — "a second `alii` in 428 for the clause's subject" read as if one `alii` served both clauses; each `hic` clause has its own `alii`.
17. **#28 `i` (442)** — "newly landed" is not in the Latin (`primum` goes with `effodere`, "where first… dug up"); removed. `n` on `Poeni`:
    "the Phoenicians, i.e. the Carthaginians" → "the Punic people, the Carthaginians (of Phoenician stock)", with the I.302 and I.3 cross-references checked.
18. **#25 `i` (437)** — "How fortunate they are, whose walls…" turned the vocative into the third person, and sat near the stock English for *O fortunati*.
    Now "How fortunate you are, you whose walls are rising even now!"; `l` has "O fortunate ones".
19. **#27 `l`, `i`, `n` (439)** — *mirabile dictu* was rendered "wonderful to tell" (`l`) and "strange to tell" (`i`), both the stock phrases. `l` "marvellous in the telling",
    `i` "a marvel even to speak of". The note now also says `se` is understood with `miscet viris`.
20. **#37 `i`, `n`, `about` (462)** — the drafter's `i` "Misfortune has its tears, and the mind is stirred by the lot of mortals" has a first half too close to the
    familiar "tears for misfortune" type; replaced by **"There are tears for what befalls, and the mind is stirred by the lot of mortals."** The note's claim that the line was
    "checked against the well-known English versions" (the drafter cannot have done so) was replaced by a plain statement; `about` ("tears for misfortune… mortal fortunes touch
    the mind") rewritten to match. `l` ("are tears of happenings, and the mind the mortal things touch") is a word-for-word gloss and stays. `new-renderings.md` updated.
    Checked from memory (not by collation) against "tears of things", "tears for things", "tears at the heart of things", "tears in the nature of things",
    "tears for misfortune", "touch the heart", "mortal things touch the mind", "mortal sorrows": no verbatim overlap. An undetected overlap cannot be excluded; the owner confirms.
21. **#30 `n` (446–449)** — "three forms of bronze in three lines": three words (`aerea`, `aere`, `aenis`) in two lines. "`cui` — dative of possession": a dative of reference
    with `surgebant`, which English renders "whose". Both fixed; `aere` as the ablative of `aes` added.

## Low

1. **#1 `l`** — `limina` is plural; "threshold" → "thresholds".
2. **#1 `n`** — "`frustra… vani`, a deliberate play" asserted the poet's intention; now says only that the word-stem recurs and what `vani` means here.
3. **#4 `n`** — "compare 391" → 390 (`reduces socios`).
4. **#6 `n`** — "Iliad 3.396 ff." not verifiable by number; now "the Iliad (Book 3)", substance unchanged (Helen knows the disguised Aphrodite by neck, breast, eyes).
5. **#6 `i`** — "she was revealed a true goddess" is a stock turn; now "the way she moved showed her a true goddess".
6. **#6 `n`** — "in epic a god is known by the way they walk": a generalisation; now limited to this line. Also clarified `ad… pedes… imos` and, in pass 2 (pass-2 #3), the I.320 description to
   "gathered in a knot… leaving the knee bare" (the line says `nuda genu nodoque sinus collecta`).
7. **#7 `n`** — "`est` split from the participle": it is simply placed before it.
8. **#8 `n`** — "(the huntress's form, the stranger's greeting)": the second example is not in the Latin; trimmed.
9. **#11 `n`** — "a Greek meaning of `aer`": rephrased; the note now separates `aer` (411) from `aes` 'bronze' (448–449), which the scansion also depends on.
10. **#11 `n`** — "Odyssey 7.14–17": line numbers not verifiable; "Odyssey 7".
11. **#12 `n`** — "Odyssey 8.362–363" and "Virgil adds the hundred altars": numbers dropped; "the song of Ares and Aphrodite"; the case of `Paphum` stated.
12. **#12 `i`** — "soars away", "breathe with fresh garlands": now "goes off on high", "are fragrant with fresh garlands".
13. **#13 `n`** — "`monstrat` … with the vivid present of the road itself": garbled; replaced.
14. **#13 `i`** — present "hurry on" for the perfect `corripuere`: now past, "hurried on".
15. **#14 `n`** — `plurimus` agrees with `qui` (the hill); a double space.
16. **#15 `n`** — "partitive genitive" for `strata viarum` and "the noise of the building" for `strepitum`: neither is in the Latin; trimmed.
17. **#16 `n`** — the list of infinitives under `instant` left out `optare`, `concludere`; the `sulco` rite stated as "the Roman rite for a city's or a plot's boundary", now "a Roman way of marking out a town's line".
18. **#17 `n`** — "laws before houses, a Roman thought rather than the real Carthage": unverifiable aside; deleted.
19. **#19 `n`** — "Virgil's Carthage is partly an imagined Rome…": opinion; deleted.
20. **#19 `i`** — "a theatre" for `theatris` (plural): "theatres".
21. **#21 `n`** — "so that the line has a bee-like cluster of words" (fluff) and "as at 431" (the cut before is at 430/431); both fixed.
22. **#24 `n`** — "the `talis` of `qualis` (431)": the `qualis` is at 430.
23. **#26 `n`** — "Aeneas has climbed to a point from which he looks to the city's heights": not in the Latin; deleted.
24. **#32 `i`** — "wonders what fortune the city enjoys, and at the craftsmen's skill" was a zeugma on `miratur`; now "he marvels at the fortune the city has, at the craftsmen's skill…".
25. **#29 `i`** — "she had said" for `monstrarat` (shown): "she had shown".
26. **#36 `n`** — "draws comfort from the fact that Troy's story is honoured even in a foreign city": inference; softened to what the scene shows.
27. **#38 `n`** — "if even Carthage honours it, the Carthaginians will not be hostile": inference beyond the Latin; softened.

## Pass 2 (additional edits found on re-reading the edited file)

1. **#4 `n`** — the first rewrite left "it is not the contracted `-um` type;" running into the next sentence, and "the verbs… the verbs" twice; tidied.
2. **#6 `n`** — see Low 6 (I.320 wording).
3. **Scansion carrier 446** — see below: the build discards the scanner's output for a whole unit if one of its lines is UNRESOLVED (448), so 446 had to be
   carried in `scan-fixes.json` as well, or the validator would have found it empty.

## Scansion

All 79 lines were scanned by hand, syllable by syllable, with the quantities checked (a valid hexameter is not enough: the scanner returns
valid lines with wrong quantities). The scanner flagged one line (448); hand checking found it wrong or only apparently right in nine more.

**Added to `scan-fixes.json` (9):**

| line | why |
|---|---|
| 1.415 | `sublimis`: sub- long, -lī- long, -mis short, then short `abit`; the scanner had su-bli short-short, mis long, a long. |
| 1.421 | Initial `Ae-` split (A-e-ne); `Ae-nē-ās` three long; `ma-ga-` long-long is forced once Ae- is one syllable. |
| 1.424 | `mōlīrī` all long (scanner: li, ri short); `mănĭbus` short-short (scanner: ma, ni long); -que and -cem elided. |
| 1.438 | Initial `Ae-` split; `Ae-nē-ās`; `ait` a-it (a monosyllabic `ait` would also scan, same other quantities). |
| 1.446 | Carrier line only (scanner right); in the same unit as the unresolved 448. |
| 1.447 | `dōnis` long-long (dōnum), `ŏpŭlentum` short-short (scanner: reversed). |
| 1.448 | **The UNRESOLVED line**: hypermetric. 15 syllables plus the -que of `nexaeque`, elided into the initial `ae-` of 449 (synaphea); the scanner cannot elide across a line end. `aerea` ae-re-a, `cui` one syllable, `surgēbant`. |
| 1.449 | `fŏrĭbus` short-short-short (scanner: all long), `strīdēbat` with long -dē-, `aenis` three syllables ă-ē-nis (ahēnus contracted) so that -bat is short before a vowel; the scanner took ae-nis as two. |
| 1.451 | Initial `Ae-` split; `Ae-nē-ās`; -mum elided. |

**Checked by hand and left to the scanner (the lines the runbook lists, and the others of the same kind):**
- Greek `eu`: none in this part (`neu` 413 is the diphthong, scanned correctly).
- Initial `Ae-`: Aeneas 421, 438, 451 (fixed above); `aetheria` 394, `aestate` 430, `aerea` 448, `aere` 449 (diphthong, fixed/checked); **411 `aere` is `aer` 'air', a-ĕ-re, and the scanner's split is right.**
- Consonantal `i` after a prefix or after a vowel: `adgnovit` (406, not 405: ad-gno-vit, scanner right), `iactati` 442, `iungere` 408 (no elision of `dextrae` before it),
  `iam` 396, 437, 457, 459, `Iamque` 419, `Iovis` 394, `Iunoni`/`Iuno` 446, 443, `Iura` 426 (a line the packet's own advice named): all consonantal, scanner right.
- Hiatus: none; elisions (`-que`, `-um`, `-am`) checked line by line.
- Lines whose result depends on a licence, all accepted: 404 `imos` with long first syllable (the only way the line scans), 405 `dea` as one syllable by synizesis (cost 1.5; scanner's
  reading is the only one that scans), 436 `fragrantia` with `fra-` long before `gr`, 450 `oblata` with `ob-` long, 458 `Atridas` with `A-` long before `tr`, 451 `leniit` as three syllables
  (le-ni-it; a contracted `le-nit` would also fit, same other quantities).

Total after the fixes: 79 of 79 lines pass the validator's hexameter test (script, as above).

## Refused / verified and kept (22)

1. #0 `qui adveneris` read as causal ("since you have arrived") — kept; the note gives both "who" and "since".
2. #3 (395–396) whole unit — every label (`videntur`, `despectare` as frequentative, `captas` agreeing with `terras`) true.
3. #5 `qua`, `gressum` singular for plural — kept (ablative of the relative as adverb; collective singular).
4. #8 `Quid` as an accusative of respect (adverbial "why"), `crudelis tu quoque` "too" referring to the other gods' cruelty — kept.
5. #9, #10 — true as written (`datur` impersonal, `dextrae` dative, `gressum tendit`).
6. #14 `adspectat` as frequentative of `aspicio`; `urbi imminet` dative — kept.
7. #15 `magalia` as the Punic word for huts (Lewis & Short) — kept.
8. #17 Greenough's brackets and the statement that the passage runs without the line — kept; true (423–425, 427).
9. #19 `immanis` (acc. pl. in -is), `decora alta` in apposition, `scaenis futuris` dative with `futuris` — kept.
10. #22 `liquentia` from `liqueo` as an adjective; `distendunt` with the ablative — kept.
11. #23 `venientum` as the old `-um` genitive plural (correct here, unlike `tuorum`) — kept.
12. #28 `acris` as the genitive singular of `acer`; `monstrarat` contracted pluperfect; `loco` ablative of place — kept.
13. #30 "Juno… is Carthage's patron goddess (I.15–18)" — verified in the source.
14. #31 `leniit` as the contracted perfect of `lenio`; `ausus` with `est` understood; `confidere` with the ablative — kept.
15. #33 `Atridas` as a Greek accusative plural; `ambobus` as a dative of reference; the Shield of Achilles (Iliad 18) as the ecphrasis model — kept.
16. #35 "Pyrrhus will kill Priam in Book II" — kept.
17. #0, #11 "Odyssey 7" for Athena's disguise and mist — kept in substance (numbers dropped; Low 10).
18. #12 Paphos, Saba (Sheba) — kept.
19. `vitalis`, `laetantis`, `omnis`, `montis` as Greenough's `-is` accusative plurals — verified in the packet text.
20. Speech marks — all correct: “ on #0, #8, #25, #34 and ” on #5, #9, #25, #38; 4 and 4 in `t`, `l` and `i`; #34 opens mid-line before `Quis`, as printed.
21. `l` line divisions of all 40 units against `t` (the count test passes; content aligned by eye for 446–449 and 453–456, the only places where a word crosses lines).
22. `about` — checked against the text; only the I.462 sentence changed.
