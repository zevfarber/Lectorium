# aeneid-021 review (III.410–505) — adversarial reviewer

Two passes. Pass 1: every unit read against the Latin word by word (grammar labels, `l`, `i`, notes, speech marks);
all 96 lines scanned by hand against the scanner's output (checked syllable by syllable, with a brute-force fit of
every doubtful line), the packet's flagged line (470), Greek `eu` (none in this part), initial `Ae-` (aequora, aevi,
aestu, aethera, aequali, aevo, aequor), consonantal `i` (coniugio, coniugis, iam, iubebat, iungere, ianua, Iunonis,
Troiam, Graiis) and hiatus/elision chains (Vade age et, Vade ait, Epiro Hesperia) done first. Pass 2: re-read of the
edited units for `l` <-> `i` agreement and remembered English; one note range corrected.
`t` was not touched (checked by script, twice: the 51 `t` strings, `ln`, `p`, `v` are identical before and after).
`units.json` was edited by script only. `parts.json`, `LOG.md` and the glossary untouched; nothing built, validated or
committed. Reference works only (Lewis & Short, Allen & Greenough, Conington); no modern translation consulted.

## Counts

| | major | medium | low | total |
|---|---|---|---|---|
| text (`l`, `i`, `n`, `about`) | 7 | 12 | 20 | 39 |
| scansion (`scan-fixes.json`) | 1 | 4 | 0 | 5 |
| **all changes** | **8** | **16** | **20** | **44** |

Severity: major = a false grammatical label (or a wrong speech mark in the reading layers), or a line the build cannot
scan; medium = a mislabel that does not mislead the reading, an invented or misplaced word that moves the sense, a
possible echo of a known version, a wrong scanner quantity; low = wording, unverifiable asides, wrong line cites.
Refused findings: 17 (below).

## Major (8)

1. Unit 37 (3.484) note: `chlamydem` "a Greek accusative". False: `chlamydem` is the ordinary Latin third-declension
   accusative of `chlamys` (the Greek form would be `chlamyda`). Now "accusative of 'chlamys', a Greek word for a cloak".
2. Unit 39 (3.488) note: `tuorum` "the genitive plural of 'tui'". False: `tui` is the pronoun's genitive; `tuorum` is the
   genitive plural masculine of the possessive `tuus`. Rewritten.
3. Unit 41 (3.491) note: `pubesceret` "a past-contrary statement… (if he had lived)". False: an imperfect subjunctive with
   `nunc` is present contrary-to-fact ("he would be growing up now"). Rewritten.
4. Unit 15 (3.448) note and `i`: `eadem` "the same ones, i.e. the leaves" and `i` "those same leaves". False: `eadem` is neuter
   plural (the verses, `carmina`, as `illa` in the previous unit); the leaves, `frondes`, are feminine. Note and `i`
   rewritten ("those same verses"; the note says the leaves are `frondes`, feminine).
5. Unit 22 (3.462) note: `ingentem` "a predicate use: 'raise Troy as a great thing'". False: it is the ordinary attributive
   adjective of `Troiam`, set early in the line. Rewritten.
6. Unit 48 (3.500) `l` and `i`: an opening “ at "If ever…" although Aeneas's speech opened at 3.493 (unit 43) and is closed
   at 3.505. A second opening mark with no close. Removed from both layers.
7. Units 34–35 (3.479–481), speech marks and note: the drafter's attribution is right (see Speech marks), but the
   notes asserted "the print has no other marks" (the archive has ” at 481) and that Greenough "broke the speech in two",
   which we cannot see; and `l`/`i` closed the speech at 479 and then ran “Go, says he, O…” with the tag unmarked. Both notes
   rewritten; `l`/`i` now read one speech with the tag inside it (below).
8. 3.470 `Addit equos, additque duces;` (half-line) — scanner UNRESOLVED; hand entry added (reason begins "Half-line").

## Medium (16) — text (12)

- Unit 2 (3.415): `tantum aevi… mutare` stated flatly ("'tantum' the object… 'aevi' a genitive of the whole"); the exact
  construction of `aevi` is not settled, so the note now says "taken as… though the exact construction is not certain";
  `l` "so great a part of age" for `tantum aevi` -> "so much of age".
- Unit 4 (3.421–423) `l`: `vastos` (agreeing with `fluctus`) was printed as "in the whirlpool vast", i.e. attached to
  `gurgite`; an invented "deep" ("steep deep waves") and a displaced `fluctus`. Rebuilt line by line ("the vast / sucks into the
  sheer drop the waves"); note adds that `vastos` agrees with `fluctus` on the next line.
- Unit 12 (3.443) `i`: "at the very bottom of her cave" — `rupe sub ima` ("beneath the lowest rock") says nothing of a cave
  or bottom. Now "beneath the deepest rock".
- Unit 22 `i`: "raise great Troy to the sky" kept the shape of well-known versions; now "let your deeds bear mighty Troy up to the
  skies" (the quotation in `about` follows).
- Unit 24 (3.469) note: "his arms now go to the man he fought against". Not in the Latin and false to Book II (Neoptolemus
  and Aeneas do not fight). Now "his arms are now given to the Trojans".
- Unit 31 (3.475) `l`: "In wedlock, Anchises…" — `coniugio… dignate` is "deemed worthy of the wedlock"; the ablative follows
  `dignor`. Now "Of wedlock, Anchises, of Venus proud, deemed worthy".
- Unit 31 `i`: "darling of the gods" (a stock rendering of `cura deum`) -> "the gods' own care".
- Unit 34 (3.479) note: speculation about what Greenough's print did (see Major 7).
- Unit 38 (3.486–488) `l`: "of hands to you which memorials of mine" made `mearum` modify `monumenta`; it goes with `manuum`.
  And `longum… amorem` had lost its verb's object ("of long love of Andromache may bear witness"). Rewritten:
  "of hands (my own) to you which memorials / may be, boy, and the long love of Andromache may attest".
- Unit 43 (3.493) `i`: "Live happy, you whose own fortune is already accomplished" — near-verbatim of a familiar version; now
  "Live on in happiness, you whose own fortune has already run its course".
- Unit 44 (3.494) `i`: "we are called from one fate to another" -> "we are summoned onward to fate after fate".
- Unit 46 (3.495–497) `i`: "no stretch of sea… to plough" (echo of known versions) -> "no expanse of sea is left for you to
  furrow, and no Ausonian fields, ever slipping backward, for you to hunt".

## Medium (16) — scansion (4)

All in `scan-fixes.json` with reasons. The scanner returned valid hexameters with wrong quantities.

- 3.440 `Trinacria finis Italos mittere relicta`: scanner had fi, nis short, Ita long, te long. Right: finis is accusative
  plural, fīnīs; Italos has short I and short ta (as Italis in 003); with those quantities the only fit (brute-forced over every
  one-syllable change) lengthens the te of `mittere` in the arsis of the fifth foot: Trī-nă-crĭ | ā fī | nīs Ĭ-tă | lōs mīt | tē-rĕ rĕ | līc-tă.
  Doubtful quantity.
- 3.475 `Coniugio, Anchise, Veneris…`: scanner (cost 1.5) read Anchise with short chi and se and Veneris long-long. Right:
  con-iŭ-gi(o) | Ăn-chī | sē Vĕ-nĕ | rĭs dig | nā-tĕ sŭ | pēr-bō. Matches the published 473 (An–chi–2ses–).
- 3.482 `Nec minus Andromache…`: scanner read Ān-drō-mā-chĕ; right Ăn-drŏ-mă-chē (as published 013, 019).
- 3.495 `Vobis parta quies…`: scanner made `quies` one long syllable and lengthened the -a of `parta`; right: quĭ-ēs (two
  syllables), parta short.

## Low (20)

Text: unit 1 (3.413) the claim "the Italian side of the strait, is Scylla's" is not in the Latin (now "Scylla holds the
right-hand side"); unit 4 the Odyssey line cite "12.103–106" removed (now "Book 12"); unit 5 `i` "heads" -> "faces" to match `l`/`ora`;
unit 6 "Scylla's dog-heads and wolf-belly are late additions to the Homeric woman" removed (unverifiable); unit 8 the cite "311 and 375"
for `nate dea` is 311 and 374; unit 10 `Iunoni` "dative of the person addressed" -> indirect object; unit 11 "a hint of the
conquest of Italy" removed; unit 14 "so long as the cave is closed" (not in the Latin) -> "so long as nothing disturbs them";
unit 15 `l` "when turned on its hinge a thin wind" -> "when, the hinge turned, a thin wind"; unit 16 "who have come a long way" removed;
unit 19 `l` "willingly" was displaced -> "and, willing, her voice and lips set free"; unit 22 "began at 375" -> 374; unit 24 "Dodona… famous for its
bronze" removed (only "oracle of Zeus"); unit 25 "separate from those for the fleet" (the gifts are not for the fleet) -> "listed apart from the
gifts just named"; unit 27 "Helenus is making the whole fleet ready" removed; unit 31 note range "475–479" -> "475–481";
unit 35 `nati pietate` "ablative of respect" -> "of cause or respect"; unit 42 "where the Latin Library has 'affabar'" removed (not in
`variants-latinlibrary.json`; unverifiable); unit 50 "(as at the end of the last part)" removed; `about` quotation of 3.462 brought into line with the new `i`.
Also unit 22 `l`/`i` and unit 36 unchanged after check. (Scansion: none at this level.)

## Hand scansions (5 entries added to `scan-fixes.json`)

- 3.470 (half-line; reason begins "Half-line"; validator form: feet 1–4, one ×): ăd-dĭt ĕ | quōs ăd | dĭt-quĕ dŭ | cēs.
- 3.440, 3.475, 3.482, 3.495 (scanner wrong, valid hexameters with wrong quantities).

Tested without building: `scan_story` on the edited units leaves exactly one UNRESOLVED line (3.470), which the entry supplies;
every new entry matches the words of its line (build's own check), has six numbered feet and one × (470: four feet, one ×),
and every foot is –⏑⏑ or –– (sixth –×). `gloss.json` does not exist yet, so the build cannot run.

## Doubtful quantities (scanner's only fit; no entry, or entered with the doubt stated)

3.412 `tibi` (bi long, lengthened in arsis; the only fit); 3.416 `utraque` (u long, by `tr`; the only fit); 3.421, 3.443 `imo`, `ima`
(long i, as in published 006, 013, 015, 017); 3.422 `rursus` (second syllable long, as 013, 015); 3.429 `Pachyni` (chy long, only fit);
3.433, 3.434, 3.500 `si` (long in arsis, as everywhere in the poem); 3.440 `mittere` (te lengthened, entered); 3.464 `gravia`
(final a lengthened at the caesura, only fit); 3.504 `casus` (sus lengthened at the caesura); 3.496 `retro` (re long by `tr`).

## Speech marks

- Helenus 374–462: ” heads nothing here; it is in `t`, `l` and `i` of unit 22 (3.462). The speech opened in the last part.
- Helenus to Anchises 475–481: **verified against the Latin: the speaker of 3.480 `Vade ait O felix nati pietate. Quid ultra provehor…`
  is Helenus**, not Anchises or Aeneas. `Vade` is an order to Anchises (`felix` is his vocative), `ait` is Aeneas the narrator's
  tag, and `Quid ultra provehor, et fando… demoror austros?` is Helenus checking himself, as the wind is waiting (472–473).
  The archived `t` has “ at 475 and “ at 480 and ” at 481 (no close at 479). `t` stays as printed. In `l` and `i`: “ opens unit 31
  (475); unit 34 is left open; unit 35 reads `Go,” says he, “O fortunate…` / `Go,” he says, “O happy…`; ” closes unit 36 (481).
- Andromache 486–491: “ opens unit 38, ” closes unit 41 (491); no marks in between (units 39, 40). Checked.
- Aeneas 493–505: “ opens unit 43 (493); ” closes unit 50 (505). The extra “ at unit 48 (500) removed (Major 6).
- Counts: `t` 4 opening, 4 closing. `l` and `i`: 4 opening, 5 closing (the ” of unit 22 closes the speech opened at 374, in the last
  part; and the interrupted speech of 475–481 has two openings and two closings in English against two openings and one closing
  in the print). The validator will WARN "l: 4 opening and 5 closing" and the same for `i`; expected, as in 020 for the opposite case.

## Refused findings (17) — considered and not changed

1. Drafter's attribution of 3.480 to Helenus: right (above); kept, notes corrected.
2. 3.412 `tibi`, 3.416 `utraque`, 3.421/443 `imo`/`ima`, 3.422 `rursus`, 3.429 `Pachyni`, 3.433/434/500 `si`: scanner's fit is the only one and
   matches published usage; no entry (listed as doubtful).
3. 3.453 `ne qua`: `ne` is long (nē); no entry.
4. 3.464 `gravia sectoque`: final a long at the caesura is the only fit; no entry.
5. 3.504 `casus`: sus long at the caesura, only fit; no entry.
6. 3.449 `ianua`: scanner reads consonantal i correctly (iā-nu-a), making `vit` long; no entry.
7. 3.488 `coniugis` (cost 1.5), 3.472 `iubebat`, 3.451 `iungere`, 3.494 `iam`, 3.437–438 `Iunoni(s)`, 3.462/505 `Troiam`: consonantal i handled correctly.
8. 3.473 `Anchises` (chi long) and 3.499 `Graiis` (Grā-iis): right.
9. 3.480 `Vade ait O` and 3.462 `Vade age et`: elisions right; `ait` is two syllables; no hiatus.
10. 3.428 `delphinum`, 3.476 `deum`, 3.452 `abeunt`, 3.454 `socii`, 3.460 `expediet`: no wrong synizesis (only `quies` was wrong).
11. Unit 15 `ianua`: the note's two readings (subject of `turbavit`, or "through the door") are both defensible; kept, hedged.
12. Unit 20 `venerata` "a passive sense": defensible (Conington); kept.
13. Unit 33 `praeterlabare` present subjunctive after `necesse est` (not an imperative); kept.
14. Unit 11 `mittere`: the note already hedges the construction; kept.
15. Unit 48 `olim` "some day": defensible; kept.
16. Unit 31 `bis` "explained in different ways": true and hedged; kept.
17. Notes over 140 words (units 0, 2, 4, 6, 8, 15, 24 and others): the validator will WARN; the content is needed. Labels confirmed true and
    kept: unit 7 `cessantem` and the postponed `et`; unit 14 `locis`; unit 16 `odere`; unit 26 hemistich count; unit 29 `ne qua mora`;
    unit 49 `quibus` dative of possession and the Penates cite (3.163–168, checked in the source); unit 33 cite 396–402 (checked).

## Notes for the build

`gloss.json` does not exist yet, so `python3 build_aeneid.py aeneid-021` cannot finish in the real tree. The scansion gate
should pass: all 96 lines fit with the five hand entries (470 half-line; 440, 475, 482, 495 wrong quantities). Expected validator
WARNs: long notes; 4 vs 5 quotation marks in `l` and `i` (above). The new-renderings file is unchanged: none.
