# aeneid-022 review (III.506–612) — adversarial reviewer

Two passes. Pass 1: every one of the 62 units read against the Latin word by word (grammar labels, cross-references, `l`, `i`,
`n`, `about`, speech marks); all 107 lines scanned by hand against the scanner's output (syllable by syllable, with natural
quantities checked and a brute-force fit tried on every doubtful line), including the packet's five flagged lines (527, 533,
549, 553, 588), Greek `eu` (Euroo 533, Teucri 601; Eoo 588), initial `Ae-` (Aetna 554/571/579, aestu 557, aethera 572, aethra
585 — all correctly one syllable; `aera` 514 is ā-ĕ-ra, correct), consonantal `i` after a prefix or a hiatus (obiectae 534,
iniuria 604, Graiugenum 550, iussi 561, Iunoni 547, Iliacos 603, periisse 606, Troia 596) and hiatus/elision chains. Pass 2: the
edited units were re-read for `l` <-> `i` agreement, remembered English and note length, which led to a further six small edits
(U6, U15, U20, U40, U60 and a stale claim "A new paragraph" at 3.610); the three-line unit 525–527 was found to lose its
scansion in the build (below).
`t` was not touched: checked by script against the original `units.json` after every edit (the 62 `t` strings, `ln`, `p`, `v` are
identical). `units.json` was regenerated from `draft.py` by `make_units.py` (draft.py edited by script; only `l`, `i`, `n` and the
part `about` changed). Nothing built, validated against a built file, committed or pushed (`gloss.json` does not exist yet).
Reference works only (Lewis & Short, Allen & Greenough, Conington); no modern translation consulted.

## Counts

| | major | medium | low | total |
|---|---|---|---|---|
| text (`l`, `i`, `n`, `about`) | 9 | 19 | 44 | 72 |
| scansion (`scan-fixes.json`, 11 entries) | 2 | 8 | 0 | 10 |
| **all changes** | **11** | **27** | **44** | **82** |

Severity: major = a false grammatical label or a false statement of the construction, a wrong reading of the Latin in `l`, or a
line/unit the build cannot scan; medium = a mislabel that does not mislead the reading, an invented or misplaced word that moves the
sense, an unverifiable cross-reference, a possible echo of a known version, a wrong scanner quantity/syllable count; low = wording,
unverifiable asides, wrong cites. Refused findings: 22 (below).

## Cross-references checked against the source text

- Helenus 3.403–407 (veil the head at the altars on the shore "ne qua inter sanctos ignis … hostilis facies occurrat et omina turbet"): true,
  but the drafter attached it to the Juno sacrifice only; reworded (Medium 11).
- Helenus 3.410–413 ("laeva tibi tellus et longo laeva petantur aequora circuitu; dextrum fuge litus"): true; now quoted at 561–562.
- Helenus 3.435–440 (the one precept above all: win Juno's favour with prayer and gifts, 437–439): the drafter's "437–440" was too narrow
  for "dederat quae maxima" (435 "unum illud … proque omnibus unum"); now 435–440. Helenus on Scylla/Charybdis 3.418–432: "3.410–432" kept.
- Helenus 3.396–398 (avoid the Greek-settled coast): added to the `suspecta arva` note; true.
- Odyssey 12: Charybdis is Homer's; kept, with the surplus words ("her whirlpool") trimmed.
- Juno Lacinia, temple on the Lacinian headland near Croton: true, kept. Tarentum a Spartan colony, a tradition tying it to Hercules: kept,
  reworded "legend made Hercules its founder" to "a tradition connected it with Hercules".
- Minerva temple "traditionally near Hydruntum (Otranto) on the Calabrian shore": not in the Latin and not verifiable from the reference
  works; removed. The note now says Virgil names no place, and that Minerva is the Pallas of 544.
- 1.203 (`forsan et haec olim meminisse iuvabit`) for the construction at 606: true.

## Major (11)

1. U12 (3.529) note: `secundi` "a nominative plural adjective used as an adverb". False: it is an adjective agreeing with the gods
   addressed ("be favourable as you blow"). Rewritten; `l` "breathe favourably" -> "breathe, favourable" (low).
2. U14 (3.532) note: "the two actions are listed without a link (asyndeton)". False: the line is `Vela legunt socii et proras … torquent`;
   `et` links them. Removed.
3. U20 (3.541–543) note: `idem` "neuter plural" (false: nominative masculine plural, the older form of `iidem`, agreeing with
   `quadrupedes`); `sueti` "a contracted perfect passive participle" (false: the ordinary perfect participle of `suesco`, `sunt`
   understood); `concordia` "a neuter plural predicate" (false: it agrees with `frena`). All three corrected.
4. U22 (3.546) note: `Heleni` "a Greek genitive in -i". False: the ordinary Latin genitive of `Helenus`. Corrected.
5. U24 (3.551–552) note: `cernitur` "agrees with the nearest subject, `sinus`". False: there is one subject. Corrected.
6. U26 (3.554–556) note: "the preposition `ad` is between its adjective phrase and noun". False: `fractasque ad litora voces` is ordinary
   order, `ad litora`. Removed.
7. U30 (3.561–562) `l` and note: `rudentem` taken as the noun "rope" ("the creaking rope wrenched to the left prow"), and `laevas`
   taken with `proram`. False: `rudentem` is the present participle of `rudo` agreeing with `proram` ("the groaning prow"), and
   `laevas` agrees with `undas` (`ad undas`). `l` rebuilt ("and first the groaning / wrenched the prow Palinurus towards the waves on
   the left"); note rewritten, with the noun `rudens` ("rope") mentioned and set aside. The `i` was already right.
8. U33 (3.566) note: `inter` "stands after its noun phrase's first word". False: `inter` governs `cava saxa`. Corrected.
9. U59 (3.609) note: "puts the relative adjective before the subject". False: `quae` is the interrogative adjective of an
   indirect question. Corrected.
10. 3.527 `stans celsa in puppi:` (packet: UNRESOLVED) is one of Virgil's half-lines (scanner finds no hexameter). Hand entry added
    (reason begins "Half-line"; validator form: feet 1–3, one ×).
11. 3.525–526 (entries added): the scanner drops the scansion of the whole unit 525–527 because 527 is UNRESOLVED, so these two perfectly
    good lines would reach the built file with blank `sc` and the validator would fail. Hand entries added (the scanner's own fit,
    checked by hand: 525 cratera = crā-tē-ră, as `crateras` 1.724; 526 implevitque, divosque), with that reason stated. (One finding, two entries.)

## Medium (27) — text (19)

1. U2: "(the lots decided who would watch)" invented; removed.
2. U4: "the hours being pictured as driving her chariot" invented; now "Night is carried onward as they pass".
3. U6 `i`: "Orion, armed with gold, which he surveys" -> "whom he scans" (a person, not a thing).
4. U9 `i` (521–522): "And now Dawn was reddening, the stars driven off, when from far away we see dim hills and Italy lying low" kept the shape of
   well-known versions; now "Already the stars were put to flight and Dawn was turning red, when from far away we see dim hills, and
   Italy lying low."
5. U10 `l`, `i` (523–524): `l` had the closing marks spaced from the word ("Italy ”") and no exclamation; `i` "“Italy!” cries Achates
   first of all; “Italy!” the comrades hail it" is a close echo of familiar versions. Both rewritten ("“Italy!” Achates is the first to
   call out; “Italy!” his comrades answer, hailing it with glad shouting").
6. U12 note: `potentes` "a nominative (vocative) adjective" (vocative plural agreeing with `Di`) and `facilem` "a predicate adjective"
   (agrees with `viam`). Corrected.
7. U13 note: Otranto/Hydruntum and "the Calabrian shore" removed as unverifiable (see above); `Minervae` may go with `templum` or `arce`, said now.
8. U14 `l`: "The sails gather in the comrades" reads `vela` as the subject. Now "The sails they gather in, the comrades, and the prows to
   the shores they turn."
9. U19 note: `bello` "an ablative of purpose" is not a standard label; now "a dative of purpose or an ablative of cause".
10. U20 `i`: "bear the harness" for `frena` ("bridles") and "used of old" for `olim`; now "have long been used to come under the chariot
    and to bear bridles in step beneath the yoke" (the note adds `olim` "long since").
11. U21 note: "The covered head belongs to the sacrifice to Juno" — the veiling at 545 comes before the Juno rite (546–547) and
    Helenus's rule (403–407) is for the altars on the shore generally. Reworded; also removed "the Trojans treat her as the power of the place".
12. U23 note: `antemarum` described as "a spelling of `antemna`". The line cannot scan with the printed `antemarum` (te would be short in
    the second half of a spondee); it scans only as `antemnarum`, so an `n` looks dropped in the edition. The note now says so and the
    printed text is kept (`t` is cut from the source; an `n` added would be a change to the edition of record, not this reviewer's call;
    see Refused 9).
13. U25 `i`: "the goddess of Lacinium lifts her temple" adds a temple not in `attollit se diva Lacinia`; "Caulon's citadel" for `arces` (plural).
    Rewritten; note's "the Greek town of that name stood on a rocky coast" -> "the epithet marks a dangerous shore".
14. U30 note: `iussi` "a perfect participle used as a predicate, `obedient`". Not what the form is; corrected (nominative plural participle,
    "having been ordered").
15. U45 note: `supplex` "a predicate nominative" -> "a predicative adjective, `as a suppliant`".
16. U55 note: `spargite me in fluctus` "tear him limb from limb" invented; `ponto` "dative or ablative with the compound verb" hedged.
17. U56 `i` (606): "it will be a joy to have died at the hands of men" is a close echo of familiar versions; now "If I am to die, it will
    content me to have died by human hands."
18. U60 note: "A new paragraph." is false (610 is not a paragraph start in the packet); removed. (The `p` flag was already correct.)
19. `about`: "the ships are lifted to heaven and dropped to the shades below, three times" is wrong (it is the rocks that roar and the spray
    that flies up three times, 566–567). Rewritten.

## Medium (27) — scansion (8)

All in `scan-fixes.json` with reasons. In each the scanner returned a valid hexameter with wrong vowel lengths or syllable count
(the scanner assigns lengths by fit, with cost 0.0 on all of these).

- 3.506: scanner `vĭcĭ | nā Cē`; right `vī | cī-nă Cĕ` (vicus has long i; Cĕraunia has short e).
- 3.517: scanner had `circumspicit` with long spi/cit and `Oriona` with short O/ri; right `cūm spĭ-cĭt | Ō-rī | ō-nă`.
- 3.533: `Euroo` split into E-u; right one syllable Eu (sc: Eu-ro-o all long, the only fit; doubtful ro, o).
- 3.552: scanner `se` short, `diva` as di-vā, `La` long; right `līt sē | dī-vă Lă | cī-nĭ-ă`.
- 3.566: scanner `clamorem` as short-short and `cava` long-long; right `clā-mōrem`, `că-vă`.
- 3.579: `urgueri` as four syllables with short gu, e; right three (ur-guē-rī; gu consonantal, as urguet in 002).
- 3.601: `Teucri` split into Te-u; right Teu-cri.
- 3.604: `iniuria` as five syllables (i-ni-u-ri-a); right four (in-iū-ri-a), as in 001, 004, 019.

## Low (44) — text only

U0: `Provehimur` "active in sense", "the narrowest crossing", `undis` "dative of reference" (now "or interest") (3); U1 stray ",;" (1);
U5 "feeling it" invented (1); U6 Orion's belt and sword described as fact, weather aside (2); U7 `Postquam` note, `l` "clear sky" duplicating
`clarum` (-> "serene") (2); U8 garbled "-que… et" sentence (1); U9 "first sight in the poem" (-> "the Trojans' first sight") (1); U11
"a libation to the gods of the sea" (1); U12 `l` adverb for adjective (1); U15 `Euroo` sentence, `spumant` filler (2); U16 wording (1); U17 `i`
"twin walls" plural for `gemino muro` (1); U18 apposition hedged, "White horses are frequent in omens" removed (2); U19 "a harsh joke" (1);
U21 Pallas/Minerva sentence (1); U22 cite 437–440 -> 435–440, "Argivae… ironic edge" removed (2); U23 cite 396–398 added (1); U24 Hercules
"legend" (1); U29 "rowers lean back with the full weight of the body" (1); U31 "a quirk of Greenough's print" (-> "of the source text") (1);
U33 "flagged in the first part" (1); U34 Odyssey 12 phrasing (1); U37 invented parenthesis (1); U40 "a smithy of the gods", `urgueri` "old passive
infinitive" (2); U42 `l` "what the cause gives the sound" (1); U44 `umentem` "Greenough's spelling of `umidam`" (1); U45 note on `suprema` (1); U50 `i`
"flung himself down" (1); U52 "hyperbaton" claim (1); U53 `i` "that" -> "this" (agrees with `l`), `hoc` reference (1); U55 `pro quo` "connecting
relative (flagged in the first part)" (1); U56 "sea and monsters" (1); U58 "a series of clauses without links" (1); U60 `ipse` "without waiting for
Aeneas" (1); `about` "They pass Tarentum…" -> "They sight…" (1). Also trimmed three notes to under the 140-word limit (U6, U20, U15; no content lost).

## Hand scansions (11 entries added to `scan-fixes.json`)

3.506, 3.517, 3.525, 3.526, 3.527 (half-line), 3.533, 3.552, 3.566, 3.579, 3.601, 3.604. Tested without building: the scanner plus
all entries leaves no UNRESOLVED line, every word of every line has an `sc` token, every entry matches the words of its line, every hexameter
has six numbered feet, one × and only –⏑⏑ / –– feet (sixth –×), and 527 has feet 1–3 and one ×.

## Doubtful quantities (scanner's only fit; no entry, or entered with the doubt stated)

3.533 `Euroo` (ro, o long; entered); 3.549 `antemarum` (te long only if read `antemnarum`; scanner's fit kept, note says so); 3.551
`Herculei` (le short, i long; the only fit); 3.558 `Nimirum` (ni and mi both long; only fit); 3.606 `hominum` (scanner lengthens ho, mi;
in the poem it is ho⏑mi⏑ elsewhere, and the alternative fit lengthens pe, re of `pereo`; neither is natural; kept); 3.564–565 `imos`
(long i, as published 006, 013, 015, 017); 3.588 `Eoo` (Ĕ-ō-ō; packet flag checked, scanner right); 3.554 `Trinacria` (na lengthened
before cr; elsewhere short, 582 and 3.440; either way valid); 3.569 `Cyclopum` (Cy long by position); 3.575 `avolsa`
(long first a); 3.576 `liquefacta` (short li, que; only fit); 3.596 `Troia` (Tro-i-a with short i, as published 002, 003, 016);
3.568 `Interea` (final a lengthened, as published 002, 019, 021).

## Speech marks

- Anchises, prayer 3.528–529: “ opens unit 12, ” closes it (529). Checked.
- Achates and the crew, 3.523–524: two one-word cries; the print has “Italiam ”primus; `t` stays as printed; `l` and `i` mark each cry
  “Italy!”.
- Anchises, omen 3.539–543: “ opens unit 19 (539), ” closes unit 20 inside `spes et pacis ”ait` (543); `l` and `i` close it before the tag.
- Anchises, 3.558–560: “ opens unit 28, ” closes unit 29 (560).
- Castaway, 3.599–606: “ opens unit 51, ” closes unit 56 (606); no marks between. Checked.
- Counts: `t` 6 opening, 6 closing; `l` and `i` 6 and 6. No validator warning expected.

## Refused findings (22) — considered and not changed

1. Drafter's cross-references 3.403–407, 3.410–413, 3.410–432 (strait): correct; kept (the 437–440 and the veiling use refined, above).
2. Juno Lacinia, Croton, Tarentum a Spartan colony: true; kept.
3. Charybdis from Odyssey 12: true; kept (trimmed).
4. 3.563 `laevam` begins lowercase after a full stop. The source has a lowercase letter; this is not missing punctuation, so Rule 5
   (adding a mark to the source) does not apply and `t` is left as cut; the note says it is a quirk of the text. A capital in the edition would
   be a source correction for the owner to decide.
5. 3.549 `cornua velatarum obvertimus antemarum` flagged COSTLY: scanner's fit is the only one and is the line `antemnarum` scans as; no entry; see Medium 12.
6. 3.553 `Caulonisque arces et navifragum Scylaceum` (COSTLY): hand-scanned, scanner right (cau-lō-nis-que ar-cēs et | nā-vĭ-frăgum Scȳ-lă-cē-um); no entry.
7. 3.588 `Postera iamque dies primo surgebat Eoo` (COSTLY): hand-scanned, scanner right (Ĕōō in the sixth foot's long syllables); no entry.
8. 3.521 `Iamque`, 3.561 `ac iussi`, 3.547 `Iunoni Argivae`, 3.598/3.607 `iuveni`, `iuvabit`, 3.602 `Scio`: consonantal i handled correctly by the scanner.
9. The edition's `antemarum` (and `Eu-`, `urgueri` spellings): kept as printed; `t` is cut from the source and a correction would be the
   owner's call. A QUESTIONS.md line is not needed: the line scans and the note states the problem.
10. 3.514 `aera` (ā-ĕ-ra), `Hyadas`, `Triones` (trĭ-ō-nes): right.
11. 3.534 `obiectae`: scanner's syllabification (o-biec-tae) gives the right weights; no entry.
12. 3.570–571 `iuxta` (final a long) and `ruinis` (rŭ-ī-nis): right.
13. Initial `Ae-` and `Au-`: Aetna, aestu, aethera, aethra, `Aurora`, `Au-` forms: right, no split.
14. U19 `hospita` "a bitter edge": kept as a hedged reading of the apostrophe.
15. U21 `numina sancta` plural for one goddess; `velamur`/`capita` Greek-style accusative: defensible; kept.
16. U32 `idem` "we, the very same people" with `Tollimur … et idem desedimus`: defensible; kept.
17. U35 `adlabimur oris`: dative of the place to which; defensible; kept.
18. U41 `quotiens mutet` subjunctive in reported speech: right; kept.
19. U48 line 595 bracketed as spurious: note kept (61 such lines, per `conventions.md`).
20. U57 `volutans` reflexive sense: kept.
21. Notes over 140 words: none left (three trimmed).
22. `l` forms such as "The sun rushes down" (`ruit`), "Night, driven by the hours" (`acta`), "having drawn lots" (`sortiti`): word by word right; kept.

## Notes for the build

`gloss.json` does not exist yet, so `python3 build_aeneid.py aeneid-022` cannot finish in the real tree. With the eleven entries the
scansion gate should pass: no UNRESOLVED line; 527 is a half-line entered as such. The unit 525–527 receives `sc` from the hand
entries. Expected validator WARNs: none for note length; none for quotation counts (6 and 6). The new-renderings file is unchanged
(none).
