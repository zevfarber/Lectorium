# aeneid-020 review (III.306–409) — adversarial reviewer

Two passes. Pass 1: every unit read against the Latin word by word (grammar labels, `l`, `i`, notes, speech marks);
every one of the 104 lines scanned by hand against the scanner's output, with the packet's flagged lines
(316, 317, 335, 340, 354, 398), Greek `eu`, initial `Ae-`, consonantal `i` after a prefix, hiatus and diaeresis words
done first. Pass 2: re-read of the edited units for `l` ↔ `i` agreement and remembered English in `i`.
`t` was not touched (checked by script: the 52 `t` strings, `ln`, `p`, `v` are identical before and after).
`units.json` was edited by script only. `parts.json` and `LOG.md` untouched; nothing committed.

## Counts

| | major | medium | low | total |
|---|---|---|---|---|
| text (`l`, `i`, `n`) | 6 | 20 | 35 | 61 |
| scansion (`scan-fixes.json`) | 2 | 7 | 5 | 14 |
| **all changes** | **8** | **27** | **40** | **75** |

Pass 1: 59 text changes and the 14 scansion entries; pass 2: 2 text changes (one echo rephrased in `i`, one `i` brought
into line with a corrected `l`). Refused findings: 17 (below).

Severity: major = a false grammatical label, or a line the build cannot scan; medium = a mislabel that does not
mislead the reading, an omitted or invented word that moves the sense, an echo of a known version, a wrong scanner
quantity; low = wording, unverifiable asides, pipeline mechanics, confirmations that only clear a flag.

## Major (8)

1. Unit 0 (3.306) note: `circum` "stands after its noun (anastrophe)". False: `arma` is the noun; `Troïa` is the
   adjective and stands before the preposition. Rewritten.
2. Unit 6 (3.315) note: `extrema` "a neuter plural used as a noun" and `per` "follows its noun". False: `extrema` is
   the adjective of `omnia`, and `per` stands between them. Rewritten.
3. Unit 11 (3.321) note: `Priameïa` "four syllables". It is five (Pri-a-me-ï-a), and the scansion needs five.
4. Unit 12 (3.325) note: `per` "placed after its noun" in `diversa per aequora`. False: it stands between adjective
   and noun.
5. Unit 24 (3.352) note: Greek `eu` of `Teucri` "pronounced as two syllables, Te-u-cri". False: `eu` is one diphthong,
   Teu-cri.
6. Unit 45 (3.396) note: "`Italique` and `litoris` frame `hanc… oram`". False: `hanc` goes with `oram`, and `Italique`
   (genitive) is only separated from `litoris` by it. Rewritten.
7. 3.316 `ne dubita, nam vera vides.` (half-line) — scanner UNRESOLVED; hand entry added (reason starts "Half-line").
8. 3.340 `quem tibi iam Troia—` (half-line) — scanner UNRESOLVED; hand entry added (reason starts "Half-line").

## Medium (27) — text (20)

- Unit 0 `i` said she "stared at me"; the Latin has her seeing the arms (`arma amens vidit`). Rewritten.
- Unit 4 note: "two perfects with only one `et`" — there are three perfects joined by `-que` and `et`.
- Unit 6 note: opened with a pipeline remark ("We add “ in `l` and `i`") instead of the rule-5b formula; rewritten
  (see Speech marks).
- Unit 8 `i`: "worthy of you at last" for `digna satis` ("worthy enough"); "taken you in" rephrased.
- Unit 13 note: "a crossed arrangement… frames" — the order `me famulo famulamque Heleno` alternates accusative and
  dative, it does not frame. Rewritten.
- Unit 14 note: asserted the killing at Delphi as if Virgil said it, and tied `patrias` to it; now the tradition
  is labelled as such and `patrias` glossed "of his fathers, ancestral"; `i` brought into line.
- Unit 15 note: `hanc… arcem` "which Aeneas has just entered" — he has not; the citadel is the one before their eyes.
- Unit 16 `i`: "have given you your voyage" kept the shape of a known version; rephrased.
- Unit 19 note (3.340 completion): the "perhaps she means… Creusa bore you" guess is removed; the note now says
  the line is a half-line, is not completed here, and that ancient commentators mention a supplied ending that is
  not Virgil's (hedged, no Latin quoted).
- Unit 23 `i`: "I walk in… I see" for `procedo… adgnosco` ("I go forward… I recognise").
- Unit 24 `l`: "in the friendly city" — `fruuntur` takes the ablative as object; no `in`.
- Unit 25 note: wrong description of `in` between noun and adjective; rewritten.
- Unit 27 `l`: "had advanced" for the perfect `processit`.
- Unit 30 `i`: "all the sacred signs have told me" — `religio` is singular, and `l` has "sign"; aligned.
- Unit 33 note: `ex` "between its noun and adjective" — it stands between adjective and noun.
- Unit 36 `l`: "this is the order that is turned" made `is` a copula; it is the demonstrative. Now "this order is turned".
- Unit 42 note: opening brought to the rule-5b formula (see Misprint).
- Unit 49 note (3.405): `velare… adopertus` hedged (below); `i` "come between you and the holy fires" for `inter sanctos
  ignis` ("among the holy fires").
- Unit 11 `i` (pass 2): "O happy above all the rest" rephrased ("O blessed, alone beyond all others").

## Medium (27) — scansion (7)

All in `scan-fixes.json` with reasons. The scanner returned valid hexameters with wrong quantities.

- 3.326: `Achilleae` read as three syllables with synizesis, forcing both syllables of `iuvenem` long. Now
  A-chil-lē-ae, `-tus` long before the consonantal i, `ju-ve-` short-short.
- 3.334: `Helenus` has two short syllables (cf. 3.295); the scanner made He- and le- long. Now
  pars Hĕ-lĕ | nō quī | Chā-ŏ-nĭ | ŏs cog | nō-mĭ-nĕ | cam-pos.
- 3.343: initial `Ae-` split into A-e; `Aeneas` is Ae-nē-ās (diphthong, long ē).
- 3.352: `Teucri` split Te-u-cri; Teu-cri with the diphthong.
- 3.363: `suaserunt` read su-a-se-runt with short a; suadeo has consonantal u and long ā (suā-), as in the published
  suadet/suasit/suadentque. Now sua-se-runt.
- 3.388: `dicam` read with short di and lengthened ti-; `dīcam` is long, so `tibi` is ti-bī.
- 3.391: `capitum` read long-long-long and `enixa`'s e short; now trī-gin | tā că-pĭ | tum fē | tūs ē | nī-xă iă | cē-bit
  (`fetus` accusative plural, fētūs).

## Low (40)

35 text changes: pipeline remarks removed from notes (units 30, 31, 34, 36: "the dash… cannot be cut"; unit 5);
unverifiable or speculative asides removed (unit 0 "the dead are walking"; unit 8 "this sounds like Aeneas"; unit 22
"ghost-image"; unit 27 Auster as "a general word for a good wind" and "weeks of waiting"; unit 35 "scroll or wheel…
Virgil's own view"; unit 38; unit 39; unit 40; unit 43 "mocking fate"; unit 44); wording (units 5, 9, 11, 12, 14, 15,
17, 22, 23, 31, 46, 48, 50; "Achilles's" → "Achilles'" and a better cite for Priam's death, 2.526–558); `l`/`i` agreement
(unit 17 "indeed/truly" for `-nam` → "pray"; unit 46 "hostile" → "wicked" to match `malis`).
5 scansion entries that only confirm the scanner or clear a flag/unit: 3.317, 3.335, 3.354, 3.398 (COSTLY flags),
3.339 (its unit also holds the half-line 340 and so gets no sc from the scanner; the line begins in the previous unit).

## Hand scansions (14 entries added)

3.316 and 3.340 (half-lines); 3.317, 3.335, 3.354, 3.398 (scanner right, flags cleared); 3.326, 3.334, 3.343, 3.352, 3.363,
3.388, 3.391 (scanner wrong); 3.339 (unit mechanics).

## Misprint and missing mark (rule 5b)

- 3.391: Greenough prints `iacebit.` followed by lower-case `alba`, which is in apposition to `sus`, and `is locus` needs
  the whole sentence. A full stop where a comma is meant is clearly a misprint (the sense allows only one way to read
  it, though which mark is meant — comma — is not guessed: any pause mark gives the same reading). Decided: treat as
  5b. `t` stays as printed (checks require it), the unit runs 389–393 across the stop (five lines), the translation
  reads the comma, and the note opens with the print's reading.
- 3.315: the print has no opening “ before Aeneas's reply (315–319) but does close it with ” at 319, and Andromache's
  first speech is closed at 312 and her second opened at 321, so the reply is unambiguous. The drafter put “ on `l` and
  `i` of unit 6 and ” on unit 9. **Accepted**: a dropped mark, corrected in the reading text; `t` left as printed; note
  opens with the print's reading. Rule 5 (add the mark to the source and re-pin) was not applied because it covers a
  mark "that the printed edition has", and we cannot see Greenough's page; for the owner.

## Speech marks

Andromache 310–312: “ opens `t` of unit 2, ” heads `t` of unit 4 and is carried at the end of `l` and `i` of unit 3.
Aeneas 315–319: “ added to `l`/`i` of unit 6 only; ” closes `t` of unit 9. Andromache 321–343: “ opens `t` of unit 11,
” closes `t` of unit 21. Aeneas 359–368: “ opens unit 29, ” closes unit 32. Helenus 374–: “ opens unit 34, no close (goes on
into the next part). `l` and `i` carry the same marks as `t` except where noted. The validator WARNs 5 opening vs
4 closing in `l` and `i` for the unclosed Helenus speech (expected). The ” at 312 heading the next unit's `t` follows
004/007/019.

## Particular worries

- 3.340 completion note: hedged as above; no completion is offered, no Latin supplied.
- 3.405 `velare comas adopertus`: the label "passive/middle imperative" is the usual reading but not the only one; note
  now says "best taken as" and mentions the infinitive-for-imperative alternative. `comas` as accusative of respect and
  `adopertus` as a repeating participle kept.
- 3.391 `iacebit.`: see Misprint.
- Chaon (in the tradition, killed by Helenus by accident while hunting), Orestes at Delphi, Hermione promised to Orestes, Polyxena's
  sacrifice and Molossus are not in these lines; each is now labelled "in the tradition" in the notes (sources: Servius,
  Euripides; no modern work used).

## Refused findings (17) — considered and not changed

1. 3.306 `conspexit`: the long final -it at the caesura is lengthening in arsis; scanner right.
2. 3.308 `deriguit`: the second foot opens on the short -it, long in arsis; the scanner's fit is the only one. Doubtful.
3. 3.311 `si lux`: `si` has to be long (lengthened); the scanner's fit is the single-change fit. Doubtful.
4. 3.380 `Saturnia`: Sa- long, as in the published 001 and 007; no entry.
5. 3.365 `Harpyia`: py- long before consonantal i is the only fit (019 used Har-pў-ĭ-ae at 3.212 etc.); no entry.
6. 3.371 `sacrati`: sa- long before cr, as in the published 008, 010, 011, 016; no entry.
7. 3.386 `Aeaeaeque`: scanner's Ae-ae-ae-que keeps the diphthongs; right.
8. 3.393 `requies`: scanner's requ-ies (long re-, as relliquiae); alternative re-quĭ-ēs also fits. Left; doubtful.
9. 3.396 `Italique`: short I, 3.364 has long I; both usages occur; left.
10. 3.346 `Priamides`: only fits with Pria- as one syllable; scanner right.
11. 3.351 `Scaeaeque`, 3.320 `Deiecit`, 3.331 `coniugis`, 3.333 `Neoptolemi`, 3.314 `subicio`: consonantal i / Greek / diphthong
    handled correctly by the scanner.
12. 3.399 `Locri`: Lo- lengthened before cr (final foot); kept.
13. 3.402 `Petelia`: te- long (Greek η) is needed for the only fit; kept.
14. 3.335: Cha- long both times and ā long in the elided n'a — brute-forced, no other fit; entered as confirmed, doubtful.
15. 3.317 `te` long in the arsis of foot 2 is the only fit (13 syllables, one dactyl); entered as confirmed, doubtful.
16. Note word counts: seven notes exceed 140 words (units 0, 11, 29, 33, 40, 42, 49); the validator WARNs (019 had five).
    Left; the content is needed.
17. Unit 7 note ("about 58 hemistichs"), unit 24 (litotes), unit 31 (`dictu` supine), unit 41 (future imperative): labels true; kept.

## Notes for the build

`gloss.json` does not exist yet, so `python3 build_aeneid.py aeneid-020` cannot finish in the real tree: it passes the
scansion gate (all 104 lines fit, 14 hand scansions applied, no UNRESOLVED/COSTLY) and then stops at the missing file,
changing nothing. To test the gates, a scratch copy of the pipeline (outside the repository) was built with a
placeholder `gloss.json` for the 224 novel forms: `BUILT aeneid-020: 52 units, 104 lines, scansion on 50 units`, then
`validate_aeneid.py` printed **PASS** with only the WARNs above (7 long notes; 5 vs 4 quotation marks in `l` and `i`).
The scanner alone leaves the half-line units (7 and 19) without sc; the hand entries for 316, 339 and 340 supply it.
