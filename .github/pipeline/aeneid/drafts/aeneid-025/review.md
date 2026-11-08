# aeneid-025 (IV.105–205) — adversarial review

Two passes. Pass 1: every unit read against the Latin word by word (labels, `l`, `i`, speech marks), and all 101 lines scanned by hand against the scanner's fit. Pass 2: the patched `units.json` re-read; `t`, `ln`, `p` compared with the pre-review file (identical in all 55 units); `l`/`t` line counts, single-line `i`, note lengths and speech marks re-checked; the new `scan-fixes.json` entries run through the validator's own foot/syllable test (all 101 lines pass); one further echo found and fixed (unit 46). No modern translation was opened. Edits were made to `draft.py` (the 34 changed units' `l`/`i`/`n` strings) and `units.json` regenerated with `make_units.py`; `t` was never touched.

Severity: High = a false grammatical label, or an `l` that mis-attaches or changes the Latin; Medium = imprecise or unsupported label, `l` not word-for-word, `l`/`i` disagreement, remembered English; Low = wording, over-claim, style.

## Totals (text layers): 8 High, 13 Medium, 20 Low (41 findings, counted per finding: a bullet below may carry two, e.g. the tense in unit 1, the anastrophe in unit 21, the two layers in units 22 and 28; all fixed except as listed under "Refused or kept")

Scansion: 13 lines added to `scan-fixes.json` (4.110, 113, 117, 126, 128, 137, 140, 142, 150, 168, 172, 191, 196); 12 are corrections, 4.128 is a record-only confirmation of the scanner's fit.

## Changes (unit numbers are 0-based positions in `units.json`; line in brackets)

### High
- **25 (150)** `n` called `tantum` a neuter accusative used as an adverb. False: it is neuter nominative singular agreeing with `decus` ("so great a glory"). `n`, `l` ("so great a glory") and `i` ("such beauty") fixed.
- **36 (169–170)** `n` said `primus` is predicative with `causa`. False: `primus` is masculine and agrees with `dies`; `causa` is the predicate noun, understood again after `malorum`. `l` ("the first of death and the first cause of evils") garbled the genitives; now "That day, first of death and first of evils, / the cause was"; `i` says first cause of death and first cause of evils.
- **31 (162–164)** `l` rendered `diversa` as "scattered", attached to the grandson; `diversa` agrees with `tecta` ("different shelters"). `l` now keeps it with `tecta`; `i` says each ran a different way.
- **27 (153–155)** `l` put "dusty" on `fuga` ("in dusty flight"), contradicting its own note (`pulverulenta` agrees with `agmina`). Fixed: "bunch their dusty columns in flight".
- **15 (131–132)** `n` called `canum` an "old genitive plural". It is the ordinary genitive plural of `canis` (an -um stem). Fixed.
- **16 (133–135)** `n` called `Poenorum` an "old genitive plural". It is the regular -orum genitive. Fixed.
- **41 (174)** `n` called `non aliud… ullum` a "double negation". It is a pleonastic negative (a double negative would cancel). Fixed.
- **45 (184–185)** `n` said `somno` is a dative of the goal, `l` said "close her eyes in sweet sleep", `i` said "to sweet sleep": three readings. `declinat` is "lowers", not "closes". Now one reading (ablative of means, dative noted as an alternative) in all three layers.

### Medium
- **1 (107–109)** `l` "Who so mad" smuggled in a `tam` that is not in the Latin; `demens` (agreeing with `quis`) was unlabelled. `l` "Who, being mad"; `n` labels it. `i` tense harmonised ("fortune follows") with `sequatur` as a proviso.
- **2 (110–112)** `miscerive` was described as if an active infinitive; it is passive `misceri` + `-ve`, and both infinitives are passive. `n` fixed; `i` "the joining of a treaty" now plural (`foedera`).
- **12 (127–128)** `l`/`i` reduced `dolis` (plural) to "the trick" and `l` rearranged the clause. Now "the wiles discovered" in both; `l` keeps "Not having opposed her as she asked".
- **18 (138–139)** `n` called the repeated "gold" an anaphora. It is a repetition in three cases (polyptoton), not repetition at clause openings. Reworded neutrally.
- **20 (141–142)** `l` "before the others most beautiful of all" mixed `ante alios omnis` with the superlative; `i` made the superlative a comparative. Both fixed; `n` now says `pulcherrimus` agrees with `Aeneas`.
- **21 (143–146)** `i` ("Like Apollo when he leaves wintry Lycia and the streams of the Xanthus…") followed a well-known English version too closely; rephrased. `n` also names the anastrophe `altaria circum`.
- **28 (156–159)** `l` omitted `cursu` ("now these at a run"); `i` flattened `praeterit` to "rides past". `n` called `votis` an ablative; it goes with `dari` and may be dative or ablative. All three fixed.
- **34 (166)** `n` said `prima` "agrees with `Tellus` and `Iuno` as an adverb". It is nominative feminine agreeing with the nearer subject; only English takes it as an adverb. Fixed.
- **42 (175–177)** `i` "gathers strength as she goes" echoes a well-known version; rephrased ("wins strength from her going").
- **43 (178–180)** `i` "Mother Earth… bore her (so they say) as the last sister of Coeus and Enceladus" echoed a known version; rephrased.
- **49 (191–192)** `l` "whom the fair Dido deigns to join to herself as husband" treats `cui` as an accusative; it is dative with `viro` in apposition. `l` now "to whom, as husband, the fair Dido deigns to join herself".
- **53 (198–202)** `pingue solum` and `florentia limina` are further accusative objects of `sacraverat`; `i` had made them new clauses ("the ground was rich…"). `l` "born of a ravished… nymph" turned an ablative absolute into a genitive-like phrase and added a possible sexual-violence sense not in `rapta` as used here; `i` "huge for his broad realm" mis-took `latis regnis`. All fixed; the Latin Library mention for `divom` (an orthographic variant the conventions say to ignore) removed from the note.

### Low
- 0 (105–107): `l` "she sensed that she had spoken" was ambiguous (she/she): now "sensed her to have spoken". `n` "relative purpose clause" reworded to "purpose clause introduced by `quo`".
- 3 (113): `n` "she alone may approach him" over-claims; now "it is for her to approach him".
- 7 (117–119): `i` "Aeneas is preparing" disagreed with plural `parant`/`l` "are preparing"; also "first dawn" for `primos ortus`. Reworded.
- 14 (130): `l` "Out of the gates" for `portis` ("through").
- 17 (136–137): `i` "coloured border" for `picto limbo`; now "embroidered border".
- 22 (147–148): `i` "binds" for `implicat`, and `fingens` was lost; `n` "ties up" → "entwines".
- 32 (164): note was 14 words (below the validator's 15-word floor); expanded.
- 35 (167–168): `l` "a witness… of the marriage" read as a genitive; `conscius` takes the dative: "to the marriage".
- 38 (172): `n` for `coniugium vocat` was garbled ("the thing she names her love"); now says it is the predicate accusative with `amorem` understood.
- 41: `i` "than which no evil is quicker" echoed a common phrasing; now "an evil swifter than any other".
- 42: `n` "(she is timid)" asserted one reading of `metu`; now notes the reading is debated.
- 44 (181–183): `i` "wonderful to tell" is a common English tag; now "a marvel to relate".
- 46 (186–187): `i` "sits as a watcher on a rooftop" echoed a known version (found in pass 2); now "sits on guard at the peak of a roof… and frightens great cities".
- 47 (188): `i` "a clinger to the false" is not real English; now "She clings to what is false and twisted as firmly as she carries word of what is true."
- 50 (193–194): `n` named only `captos`; `immemores` is also accusative plural, and the subject accusative of `fovere` is stated.
- 51 (195): `n` "as in `in ora virum`" was circular (this is that phrase); removed.
- 54 (203–205): `i` "the very powers of the gods" added an intensifier; `n` Latin Library `divom` mention removed (orthographic variant).

## Speech marks
Checked and correct, none changed: Venus opens at 107 (unit 1) and closes at 113 (unit 3); “Perge; sequar”. (unit 4, Greenough's own pair, full stop outside the mark; speaker Venus, so Juno's `excepit` is a reply); Juno opens at 115 (unit 6) and closes at 125/127 (unit 11, `hic hymenaeus erit.”`). Iarbas's prayer opens in the next part, so unit 54 ends with its colon and no mark. Opening/closing counts balance in `t`, `l` and `i`.

## Paragraph marks
`p` is on units at 105, 129, 160, 173, 189, 198, matching Greenough's six paragraphs in the packet.

## Scansion (hand-scanned: all 101 lines; the three flagged, and every line with Ae-, consonantal i, initial Iu-/Ia-, hiatus; no Greek eu occurs in the part)
Added to `scan-fixes.json` (each with its reason there):
- **4.110** `fātīs` long-long, `incerta`/`feror` with short -ta, fe-: the scanner's cost-0.0 fit had fa-, -tis short and ta, fe long.
- **4.113, 4.172** consonantal i after a prefix: `con-iunx`, `con-iugium` (scanner read co-ni-).
- **4.117, 4.142, 4.150, 4.191** `Aeneas`/`Aenean`: Ae- one syllable, -nē- long (scanner split Ae-).
- **4.126, 4.168** `cōnūbium`: long cō- and nū- (from nūbo) with synizesis of -bio-/-biis (scanner gave nu- short).
- **4.128** (flagged) confirmed: the scanner's fit is right; entered as a record.
- **4.137** `Sīdōniam`: long -dō- and synizesis -niam (scanner gave do- short).
- **4.140** (flagged) `Ĭūlus` trisyllabic, so the fifth foot is a dactyl (laetus I | ūlus) instead of the scanner's spondee.
- **4.196** (flagged) `Ĭarbas` with a vowel I (same reasoning); fifth foot a dactyl (quet I | ar ban).

## Doubtful quantities (for the owner, or a second reviewer)
1. **cōnūbium nū long** (4.126, 4.168): I am fairly sure (nūbo, Lewis & Short headword), but the published lines 1.73 (aeneid-001) and 3.136 (aeneid-018) were left with the scanner's short nu-, while 3.319 (aeneid-020) has it long. Not touched (outside this part); worth a sweep.
2. **Iarbas with vowel I**: with the vowel I, both 4.36 and 4.196 are ordinary lines; with consonantal I each has a spondaic fifth foot. 4.36 (published in aeneid-024, entered in `scan-fixes.json` with the consonantal I) is probably wrong. Not touched.
3. **Sīdōnia**: published Sidonia (1.446, 1.613) has do- long; published 1.677 `Sidoniam` (aeneid-008) has it short. Metre forces synizesis on 4.137 if do- is long.
4. **4.172 praetexit**: the line only scans with the final -it long in the fourth foot; the scanner's fit has the same lengthening. Accepted, flagged.
5. **4.174 velocius**: the scanner's fit (cost 0.3) needs ve- long; ve- is short in `velox`. No alternative scansion exists, so left; a licence of Virgil's or a quantity I cannot confirm.
6. **4.132 Massyli** needs the y long (forced by metre); **4.136 stīpante** needs long i (Lewis & Short has stīpo); **4.146 Crētēs, Dryopēs** with long final -es (Greek -es lengthened); **4.166 pronuba** short nu- (Lewis & Short prōnŭba); **4.120 nigrantem, 4.152 caprae, 4.163 agros** with the first syllable lengthened before muta cum liquida (ordinary licence).

## Refused or kept findings
- `quod instat` as "subject of `confieri`" (unit 6): strictly the subject of `possit`/`confieri`; kept as written (true enough).
- `portis` as "ablative of the way out" (unit 14) and `acri equo` / `culmine` labels: kept.
- Unit 9 `l` "dark" for `opaca` at the end (transparent, if awkward): kept. Unit 10 `l` order differs from unit 33; kept as harmless.
- `sequar` labelled "future" (unit 4): it is also a possible hortatory subjunctive; the sense is the same. Kept.
- `l` "stamping horse" for `sonipes` (unit 16): kept (a gloss of the compound).
- The Latin Library note on `viresque/virisque` (unit 42): kept, since it affects the construction; the `divom/diuum` notes were removed as orthography.
- The "evils" in unit 36 glossed as Dido's suicide and the long enmity with Rome: an interpretation, hedged in the note; kept.
- Unit 11 handling of the bracketed line 126 and its note: correct per the conventions; kept.
