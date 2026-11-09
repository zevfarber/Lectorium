# aeneid-030 (Aeneid IV.607–705) — reviewer's record

Two passes (grammar and Latin→`l`/`l`↔`i`/echoes/speech marks; then scansion of all 99 lines by hand against the scanner's fits). `t` untouched; `draft.py` edited by script and `make_units.py` rerun (65 units, no line-count errors). `scan-fixes.json` extended by script. Nothing built, published or added to `parts.json`; `build_aeneid.py aeneid-030` was run and stops, as expected, at the missing `gloss.json` after the scansion stage passed (no unresolved lines, 8 hand scansions applied, no files written).

Severity counts: **major 6, medium 15, low 17.** (Major = a false grammatical label, a mistranslation in `l`, or a scansion with wrong quantities / that stops the build.)

## Major

1. **4.683 `lymphis` mislabelled and mistranslated.** Note called it "a dative, 'to the waters'" and `l` read "Give the wounds to waters". `lymphis` is an ablative of means with `abluam`; `volnera` is the object of `abluam`. `l` now "Give: the wounds with waters / let me wash,"; `i` "Grant it: let me bathe her wounds with water,"; note rewritten (`mihi`/`veniam` understood, `volnera` object, `lymphis` ablative of means).
2. **4.629 UNRESOLVED (packet flag).** A hypermetric line: `-que` of `nepotesque` elides into `Haec` (630), as 4.558. Hand scansion ĭm-prĕ-cŏr | ar(ma) ar | mis pug | nent ip | sī-quĕ nĕ | pō-tes(que). Entry 4.629, plus a carrier entry 4.628 (the scanner's own correct fit; the unit would otherwise get no `sc`).
3. **4.633** scanner fit (cost 0.0) has wrong quantities: `antiqua` ti, qua short and `cinis` ci, nis long. Correct: nam-quĕ sŭ | am pă-trĭ(a) | an-tī | quā cĭ-nĭs | ā-tĕr hă | bē-bat (`antiqua` ablative with `patria`, long -ā; `cinis` short; matches the published `an–ti–qua–` fits).
4. **4.682** scanner fit (cost 0.6) made `te`, `me` short and `que`, `so` long. Correct: Exs-tinx | ti te | mē-quĕ sŏ | rŏr pŏ-pŭ | lum-quĕ pă | tres-que.
5. **4.685** scanner fit (cost 0.0): `gra` long, `dus` short, `e` short. Correct: ō-rĕ lĕ | gam Sic | fā-tă gră | dūs ē | vā-sĕ-răt | al-tos (`gradus` accusative plural, long -ūs; `ēvādo` long ē-).
6. **4.694** (the `Irim` line) scanner fit (cost 0.0): `o`, `bi` long, `tus`, `I` short. Correct: dif-fĭ-cĭ | lis (que) ŏ-bĭ | tūs Ī | rim dē | mī-sĭt Ŏ | lym-po (`obitus` accusative plural with long -ūs; `Īris` long Ī, as 4.700; `dēmīsit`).

## Medium

7. 4.618 `l` "of kingdom or of longed-for light may he enjoy" gives a genitive; `fruor` takes the ablative. Now "in kingdom or in longed-for light may he take joy,".
8. 4.618 note called `tradiderit` a perfect subjunctive. The form is either a future perfect indicative or a perfect subjunctive (identical in the 3rd person); note now says so.
9. 4.622–623 `l` put "my" after "send" ("this send my gifts") and `haec` as "this". Now "and to our ashes these send / gifts.".
10. 4.625 `i` "born from my ashes" for `ossibus`. Now "From my own bones let some avenger spring…".
11. 4.663 note: "`media inter talia` has the preposition after its adjective and noun". The preposition stands between adjective and noun. Fixed.
12. 4.671 note on `perque hominum… perque deorum` was garbled ("per separated from culmina… with culmina to be supplied"). `culmina` is stated once, with `per` set after it and repeated for `deorum`. Rewritten.
13. 4.675 note: Anna's speech "runs to 685". It ends at 684 (the print's ” sits at 685). Fixed.
14. 4.659–662 note: "The mark ” ends the speech (651–662)". The 651–658 speech closes at 658; this one runs 659–662. Fixed.
15. 4.644 note cited the Greek accusative "at 511"; the model is 4.518 `exuta pedem` (029, unit at 517). Also `maculis` was not labelled (ablative of means). Both fixed.
16. 4.693 `l` "long pitying the grief" read `longum` as an adverb. Now "having pitied the long grief". Note on `obitus`: `l`/`i` have singular "death" but note said "deaths"; note now says "a poetic plural for the singular".
17. 4.699 `l` "…had condemned the head Orcus" made Orcus a nominative. Now "and to Stygian had she condemned the head, to Orcus."
18. 4.659–660 speech marks, README 5b (see "Speech marks" below): notes of units 659, 660 (`ait.`), 660 (`umbras:`) rewritten to the 5b form.
19. 4.685 speech mark, README 5b (see below): notes of the `legam.` and `Sic fata` units rewritten.
20. 4.616 (packet flag, cost 2.0): scanner took `Iu-` as one syllable and made the fifth foot a spondee. House practice (1.556, 1.690, 4.274): Ĭūlī, three syllables. Hand scansion fī-nĭ-bŭs | ex-tōr | ris com | plex (u)ā | vul-sŭs Ĭ | ū-li.
21. 4.696 `quia` was fitted as one long syllable by synizesis. It is two short syllables (as aeneid-009): Nam quĭ-ă | nec fā | tō mĕ-rĭ | tā nec | mōr-tĕ pĕ | rī-bat.

## Low

22. About: "pitying her long agony and hard dying" and "she has lived, run her course" were close to remembered English; rephrased.
23. 4.622 `i` "send that to my ashes as my due" lost `munera`; now "let that be the offering you send to my ashes."
24. 4.624 `i` echoed the usual English ("no love… no treaties"); now "Let no affection pass between our nations, and no compact bind them."
25. 4.651–652 `i` "take in this soul of mine" echoed the usual English; now "take this spirit of mine into your keeping and loose me from these troubles."
26. 4.655 `i` "I saw my walls rise" (usual English) → "I lived to see my own walls stand;".
27. 4.657–658 `i` "Blessed, alas, over-blessed" kept the pattern of the famous line; now "How blest I might have been, alas, beyond all measure, had Trojan ships never once touched our coast!”".
28. 4.659–660 `i` echo of "I shall die unavenged, yet let me die": now "Unavenged I go to my death," / "yet die I will," she says.
29. 4.693–695 `i` "almighty Juno, pitying her long agony and difficult dying" → "all-powerful, moved by the length of her suffering and the hardness of her going…".
30. 4.702 `i` "I take this lock, hallowed to Dis" → "On orders I take this lock away, hallowed to Dis, and loose you from that body."
31. 4.705 `i` "passed off into the winds" → "drew back and was gone into the winds."
32. 4.682 `i` made `populum patresque Sidonios` an apposition; now "your people and the Sidonian elders".
33. 4.684 note: `super` "above, besides"; now "above, so 'still hovering over her'".
34. 4.697 `i` "wretchedly" for the adjective `misera`; now "a wretched woman before her time".
35. 4.641 note "compare 631 and 704" → 630.
36. 4.641 note on `anili`: "an eagerness that is still old" (obscure) → "the nurse's age set against the speed her mistress wants".
37. 4.663 note on `Dixerat`: unclear last clause; reworded.
38. 4.607 note was 152 words (WARN above 140); trimmed to 138.

## Speech marks (the drafter's question) and README 5b

What the checks require: `build_aeneid.py` checks only that `t` tiles the source; `validate_aeneid.py` only counts “ against ” **per layer** and WARNs (never fails) on a mismatch. Nothing compares `l`/`i` with `t`. The 026/029 precedent is exactly the drafter's 685 treatment (in 029 at 570 and 579, in 026 at 276: `l`/`i` close the speech at the end of the speech's last unit; the next unit's `t` keeps the print's ” at its head, and its `l`/`i` carry none). So:

- **685**: kept as drafted (precedent). Per 5b only one reading is possible, so the note of the `Sic fata` unit now opens "The print has ” at the head of 'Sic fata', a misprint for a ” after 'legam.'…, corrected here in the English layers (the Latin keeps the print…)". The `legam.` unit's note points to it.
- **659–660**: no precedent; the checks accept the drafter's variant, and the sense allows one reading (Dido's one sentence "Moriemur inultae, sed moriamur", broken by `ait`, then a new quotation at `Sic, sic`). Kept: `l`/`i` read “…,” / “…,” she says. / “Sic, sic… The note of the `ait.` unit opens with the 5b sentence (“ before `sed` with nothing closing it, a misprint for a closing ” after `moriamur`); the `umbras:` unit's note opens with the missing “ before `Sic, sic`; the first unit's note now only points to them. `t` stays as printed everywhere.
- Counts after edits: `l` 8 open / 8 close, `i` 8 / 8, `t` 6 / 7 (the 7th is the ” at 629 closing the speech opened in 029, plus the print's misplaced marks). Expect one validator WARN for `t`; it is not a failure.

## Advisory (QUESTIONS.md item 5)

No `advisory` written. QUESTIONS.md says: no advisory unless a trigger fires. `claude/content-advisory.md` is not in the repository, so the only guide is conventions ("sexual violence always; graphic detail rarely") and the advisories already on published parts (Lycaon's cooking, the Niobids, Marsyas' flaying, the plague, Pentheus: all long, anatomical dwelling on bodies). Dido's death is a suicide by sword told in about four lines (`ensem cruore spumantem`, `sparsas manus`, `stridit sub pectore vulnus`, the blood wiped with a robe); there is no sexual violence and no sustained anatomical description. No trigger applies. Left for the owner's ruling in QUESTIONS.md item 5.

## Variants and the drafter's other doubts (checked; refused as changes)

- **4.641 `celerabat` / `celebrabat`**: note kept. The variant changes the sense (`celebro`, "throng, frequent") and the note says so correctly.
- **4.651 `sinebant` / `sinebat`**: note kept. Changes the verb's subject (`fata deusque` plural vs `deus` alone); the note is accurate.
- 4.648 `vestes`/`uestis`, 4.688 `graves`/`grauis` (accusative plural either way), 4.683, 4.702: orthographic or morphological; notes adequate (683, 688, 702 already mention them; 648 correctly silent).
- **4.647 `quaesitum`**: participle with `munus` kept; the supine reading does not fit `non hos… in usus`.
- **4.692 `reperta`**: kept with `lucem`, as the note says; the alternative (agreeing with Dido) is possible but the note does not claim more than "most naturally" — stands.
- **4.696 `merita… morte`**, **4.612/623/625/662 `nostras…` for `meas`**: notes kept; correct.
- 4.675 `Me fraude petebas?`, 4.656 `inimico a fratre`, 4.632 `Barcen` (Greek accusative, long -ēn), 4.693 `Irim`, 4.700 `Iris`: labels true.
- Drafter's guess that Homeric parallels were absent: agreed; none added.

## Scansion: every line scanned by hand (99 lines)

Scanner fit confirmed correct, natural quantities, on all other lines, including the lines named in the brief: 4.617 `videatque` (vi-de-at-que, de short), 4.621, 4.625 `Exoriare` (Ex-ŏ-rĭ | ā-r(e) ă-lĭ, no synizesis), 4.630 `partis` (acc. pl. -īs long), 4.632 `Barcen` (long -ēn), 4.646 `ensemque`, 4.664, 4.668 `aether` (ae one syllable; the unit-level scan agrees with the line-level one), 4.700 `Iris` (Ergo `go` elided, Īris), 4.702 `adstitit`, 4.704. No line has Greek eu or initial Ae-. A check that the unit-level scan (as `build_aeneid.py` makes it) equals the line-level scan on every unfixed line: no differences.

**Hand scansions added to `scan-fixes.json`:** 4.616, 4.628 (carrier for 4.629's unit), 4.629 (hypermetric), 4.633, 4.682, 4.685, 4.694, 4.696. All pass the validator's foot, syllable-count and × checks, and the build's alignment checks.

**Doubtful quantities left as the scanner or precedent gives them (for QUESTIONS.md):**
- **4.667 `femineo ululatu`**: the scanner's fit (cost 1.5) reads `femineo` by synizesis and makes `mi` long. A natural-quantity parse exists with hiatus after `femineo` (fē-mĭ-nĕ | ō ŭ-lŭ | lā-tū); neither could be confirmed. Left as scanned.
- 4.615 `audacis` (genitive, -is short by nature) long in arsis at the caesura; 4.645 `inrumpit` `pit` long before `l-` and `domus` `mus` long in arsis; 4.619 `tradiderit` `rit` long before `reg-`; 4.686 `semianimem` by synizesis (sem-ya-ni-mem); 4.672 `exanimis` `mis` long in arsis; 4.670 `Tyros` `ros` long in arsis.
- Precedent kept: 4.627 long `o` of `olim` (as 1.203 and others), 4.679 `idem` with long first syllable (as 017, 018, 021, 022), 4.702 `supra` long `su-` (as 018, 026), 4.683 `Sidonios` short `do` (as 4.75), 4.641 `Sic ait` with long `sic` (QUESTIONS item 25).
