# aeneid-034 review (V.286–386) — adversarial reviewer, two passes

Method: pass 1 read every unit's `t`, `l`, `i`, `n` against the Latin and the grammar; hand-scanned every line flagged by the packet and every line with Greek eu, initial Ae-, consonantal i after a prefix or hiatus, then all other lines against the scanner's output. Pass 2 re-read every edited unit, re-checked line counts (`l` has the same line count as `t` in all 53 units), speech marks, `p` flags, and simulated the build's scansion step (scanner + scan-fixes + the validator's foot checks: all 101 lines pass, none left without `sc`).

`t` is untouched (checked: every `t`, `ln` and `p` equals the drafter's). Edits to `l`/`i`/`n` were made by `review_patch.py` (exact-substring replacements with asserts) run after `make_units.py`; `draft.py` was not edited, so if `make_units.py` is re-run, run `review_patch.py` after it.

## Severity counts

Definition: major = a false grammatical label, or Latin mistranslated in `l`, or a scanner fit that is wrong; medium = misleading or unsupported claim, `l`/`i` disagreement, remembered echo, or a line the build cannot take without a hand entry; low = polish.

- Major: 12 (6 text, 6 scansion)
- Medium: 14 (12 text, 2 scansion)
- Low: 20 (17 text, 3 scansion)

## Changes: text

Major
1. U1 (289–290) note: `medium` was said to agree with the subject `heros`; it is accusative and agrees with `se` (the subject would be `medius`). Fixed.
2. U1 `l`: `se` rendered twice ("the hero himself … carried himself"). Now "himself … the hero … carried".
3. U2 (291–292): `animos` rendered "in spirit" in `l`, and the note invented an antecedent `eos`. The relative clause `qui… velint` stands before its antecedent `animos` ("he invites with prizes the spirits that may wish…"). `l`, `i` and note fixed.
4. U23 (327–330) note: `levi cum sanguine… labitur` was called an "inverse cum". `cum` is a preposition; there is no conjunction. `l` had "when". Note and `l` fixed (the `i` keeps "when", natural English for imperfect + vivid present).
5. U23 note: `viridisque super herbas` was said to put the preposition after its noun; `super` precedes the verb and `herbas` ends the line. Now: `super` an adverb (or a preposition cut off by the verb). `humum` made accusative of the place to which, and `i` made consistent ("poured on the ground… soaked the green grass over it").
6. U15 (311–313): note said `que` joins `pharetram` and `plenam`; it joins the adjectives `Amazoniam` and `plenam`. `l` "and one full of arrows" had an invented "one". Fixed.

Medium
7. U0 `l` "To this" for `Hoc` (not a dative or goal); now "After this", and the note says the case is unsettled.
8. U4 note: `egregia` was said to be "put between"; it is `Priami` that sits inside `egregia… de stirpe`. Fixed.
9. U15 note: `Threïciis` has four syllables (Thre-i-ci-is), not three. Fixed.
10. U17 note: the claim that the Homeric runners "pour" from the line is not in Iliad XXIII as remembered; removed (now "modelled on the foot race in the funeral games of Iliad XXIII").
11. U18 note: `Nisus` is held to the end of the first line of the unit, not the second. Fixed.
12. U22 (323–326) hedged `ambiguumque`: note said "a neuter noun… perhaps 'or at least'". Now: neuter adjective as noun, `que` joins the verbs, sense nearly "or", and the "at least" is stated to be the English version's, not the Latin's. `i` kept.
13. U24 (331–333): `l` invented "filth" for `in ipso`; the note asserted that `ipso` agrees with `fimo`. `l` now "in the very / fell, in unclean dung and in sacred blood"; note says the grammar is loose.
14. U30 `i` "bank of seats" for `consessum`, which is the assembly (the bank is `caveae`); now "the whole assembly of the vast theatre".
15. U31 `i`: "a courage all the more welcome for coming in a form so fair" is a distinctive echo of the familiar maxim in English versions; rephrased.
16. U35 note: `sic fatus` was said to have `est` omitted; it is a participial phrase, nothing omitted. Fixed.
17. U11 note: "iron-workers" is unsupported (removed); `Cnosia`/`Gnosia` is orthography (removed per conventions); `spicula` hedged (arrow-heads, dart-heads or spear-points); `levato ferro` said to be an ablative of quality, now an ablative with `lucida`; `i` "spearheads with burnished iron" tautology fixed.
18. U23 `i` (see 5): the ground and the grass were both said to be soaked, against `l` and the note.

Low
19. U3 note: "zeugma" for `Nisus amore pio` -> `insignis` understood.
20. U5 note: `Simul et` and `Acarnan ('Acarnas')` wording.
21. U8 `i`: "spoke, and spoke thus" padding.
22. U12 `i`: `erit` is future ("This shall be the one honour").
23. U16 note: "Aeneas is holding it up" is an inference; now "evidently showing it".
24. U17 `l` "the farthest marks they eye" -> "the farthest points they mark"; `i` "streaming… rain-cloud" slightly reworded.
25. U18 `i` "than the wings of the lightning" reworded (near-verbatim echo risk).
26. U19 note: "only just in order" was muddled; "next in order, yes, but far behind".
27. U22 note: `umero` as ablative also noted (hedge of `incumbens umero` widened, kept).
28. U35 `i` "mane" -> "hair" (`villis`).
29. U36 `i` "by his running" -> "by his merit" (`laude`); note: "irony" softened to "dark humour" (hedge kept).
30. U37 `l` garbled "with wet foul limbs with dung" -> "and wet foul limbs with dung".
31. U38 `i` "torn" -> "taken down" (`refixum`).
32. U41 note: orthographic `brachia`/`bracchia` remark removed (conventions: ignore orthography).
33. U51 note: "Greenough prints… misprint" -> "the text as printed… misplacement" (the placement comes through the archive; `t` kept as printed, `l`/`i` close the speech at `iube` by sense, as already done).
34. U0 note: `collibus… curvis` hedged (place or means).
35. Hedged flags kept as hedged, checked: `palmae` (U32, "probably the dative": kept, a reading "who came up for the palm" is the one used in `l`/`i`), `Danais refixum` (U38, "probably of the agent": kept), 5.360 shield history ("not told": kept, true), `incumbens umero` (see 27).

## Changes: scansion (scan-fixes.json, 11 entries added, all validated with the validator's own foot checks)

Scanner wrong (major):
- 5.286, 5.303, 5.348, 5.381: `Aeneas`/`Aeneae` split Ae- in two (A-e-ne-as), with a spurious extra syllable; corrected to Ae-nē-ās (house practice, as 5.282).
- 5.293: Teucri split Te-u-cri (cost 0.0, not flagged); Greek eu is one long syllable (as 1.38, 1.299 etc.).
- 5.345: Adiuvat read a-di-u-vat and the ablative magnā scanned short (cost 0.3, not flagged); corrected to Ad-iŭ-vat (consonantal i after the prefix) and long -nā.

Hemistichs (medium, UNRESOLVED otherwise): 5.294 (Nisus et Euryalus primi, 3 feet + 1 syllable) and 5.322 (tertius Euryalus, 2 feet + 1 syllable), "Half-line" entries.

Carriers (low): 5.295, 5.296, 5.321 share units with the half-lines, so would lose their `sc`; entered with the scanner's own (correct) fit.

Hand-scanned and found correct, no entry (refused): 5.312 (Threïciis, 4 syllables, dactyl-first), 5.320 (proximus/proxumus, both short -xi-, -xu-), 5.337 (see below), 5.359 (iussit with consonantal initial i; Didymaonis as Di-dy-mā-o-nis). All other lines with Eu-, Ae-, consonantal i (iuventa 295, iuvencis 329, iuvenis 331, iubebant etc.) or elision/hiatus were checked and are correct as scanned.

## Doubtful quantities left as scanned (for QUESTIONS.md)

5.337 `Euryalus` ends with a lengthened -lus before `et` at the penthemimeral pause (scanner fit; the only fit, precedent 1.314); 5.311 `Amāzoniam` (ā forced); 5.334 `oblitus` with long ŏb- before bl- (forced); 5.298 `Patron` with Pā- (forced); 5.343 `făvor` with short fa- (forced; the lexicon may give long); 5.371 `ī-dem` (forced); 5.299 `Tegeaeae` as Te-ge-ae-ae. Audio quantities may be off there; none checkable against public-domain sources.

## Refused findings

- Scanner's COSTLY flags at 5.312, 5.320, 5.337, 5.359: hand-scan agrees with the scanner; no entries added.
- Not changed: `Hoc… tendit` parse; `pater optimus` "kindest of men"; the speech-mark layout (t has the closing mark at the head of unit 52 as printed; `l` and `i` close at `iube.`; opening/closing marks balance 15/15 across t, l, i); the 5.350 variant note (`miserari` would change the construction, so it stays); the 5.359 `artes` note; the `proxumus` spelling note.
- No other remembered echoes found in `i` beyond those rephrased (checked the speeches at 304–314, 348–350, 353–356, 383–385 and the set pieces: none of the pilot's set-piece lines occurs here).
