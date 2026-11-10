# aeneid-040 (VI.1-97) review, two passes

Severity counts: **major 24, medium 9, low 17** (50 findings: 36 text findings in units.json and make_units.py, 14 scansion entries in scan-fixes.json; findings refused or left are listed at the end and are not counted).
Text: major 10, medium 9, low 17. Scansion: major 14 (the scanner knows no vowel quantities, so cost 0.0 does not mean right).

Build: `python3 build_aeneid.py aeneid-040` now passes the tiling stage and the scansion stage (14 hand scansions applied; nothing UNRESOLVED; COSTLY 2.0 at 6.36 cleared) and stops only because `drafts/aeneid-040/gloss.json` does not exist yet. Nothing was written to the manifest. Expect the validator to WARN `t: 7 opening and 5 closing quotation marks` (misprints, below).
`units.json` was edited by script; `l` has the same line count as `t` in every unit; every `i` is one line; marks: l 7/7, i 7/7. `make_units.py` was regenerated from the final `units.json` and reproduces it (run, then diffed). Two passes: pass 1 was the full read of all 63 units against the Latin plus a hand scan of all 97 lines; pass 2 was a re-read of every changed unit, the mark count per layer, and a trial build (which found the tiling failure, M10).

## Text changes (units.json)

Major (10):
- M1 unit 25 (6.45): `l` carried the print's misplaced marks (`“tempus` at the head of line 46, a full stop after "maiden"); `i` gave "cried" and "she says" (two verbs for `ait`); the note called the mark after `virgo` "a comma or nothing" without saying that the misprint is the print's, and opened with a long hedge. `l` now `They had come to the threshold, when the maiden: “To demand the fates / is time,” she says;`, `i` `... when the maiden: “It is time to ask the fates,” she says;` (verb held back, as in the Latin); note rewritten to open with the print's reading and the correction (rule 5b).
- M2 unit 30 (6.51-52): the drafter's note put the closing mark after `precesque` and read `Cessas… Tros ait Aenea` as one utterance; `Tros… Aenea` is one vocative with `ait` dropped into it, so the closing mark belongs after `Tros` and a fresh opening mark before `Aenea`. `l` carried the print's `“Tros`; `i` closed the speech after "she says" and so did not match `l`. Now `l`: `“Do you hesitate over vows and prayers, / Trojan,” she says, “Aeneas?`; `i`: `“Do you hang back from vows and prayers, Trojan Aeneas?” she says.`; note opens with the print's reading.
- M3 unit 31 (6.52): `i` was `Do you hang back?”`, closing the speech, which runs to 53. Now `“Do you hang back?` (reopened, since `i` 30 closes); closed at 32.
- M4 unit 32 (6.52-53): `i` opened a spurious `“` at "For" in the middle of the speech. Removed.
- M5 unit 34 (6.54): label false: "per dura… ossa… with the preposition between adjective and noun". The preposition stands before the adjective; the verb (`cucurrit`) comes between adjective and noun. Fixed.
- M6 unit 36 (6.58-60): `l` line division did not follow `t` (`maria`, on t line 59, sat on `l` line 1; `Massylum gentes` ended up on the wrong line). Now: `circling great lands, / so many seas I entered, you as my guide, and far withdrawn / the Massylian peoples, and the fields stretched before the Syrtes,`.
- M7 unit 55 (6.87): `i` "the Tiber whitened with froth from the flow of blood": "whitened" is not in `spumantem sanguine`. Now "the Tiber foaming with streams of blood".
- M8 unit 59 (6.92): `i` dropped the `non` of `quas non oraveris urbes` (what cities will you NOT have begged), turning a rhetorical question into a statement. Now "what peoples of Italy, what cities, will you not have begged for help!".
- M9 unit 60 (6.93-94): note read `externi… thalami` as a genitive ("of a foreign marriage-chamber"); it is nominative plural, the second thing named as the cause. `hospita` label was vague. Half-line 94 (unfinished verse) was not mentioned. Rewritten; half-line stated.
- M10 tiling (found in pass 2 by the trial build): units 26, 32 and 45 ended on a closing `”` set against the next word (`deus! ”Cui`, `domus. ”Et`, `oro. ”Finem`), so the build refused ("ends mid-word"). Re-cut with `aeneid_lib.cut` through `make_units.py` (closers now `deus!`, `domus.`, `oro.`); the `”` stands at the head of units 27, 33 and 46, as in aeneid-037. This moves three unit boundaries in `t` (the text is still cut from the source by script, never retyped; the build's tiling now passes). Notes of 26, 32, 45 say the mark stands at the head of the next unit; notes of 27, 33, 46 gain a sentence pointing back to the misprint.

Medium (9):
- unit 10 (6.20-22) `i`: "and the pity of it" echoes a stock English phrase and left `miserum!` dangling. Now "- a pitiable thing -" with seven bodies of their sons every year.
- unit 16 (6.31) note: "if grief were allowing it" did not match its own "you would have had". Now: condition with `si` left out, imperfect subjunctive doing the work of the pluperfect (poetic), "if grief had allowed it".
- unit 26 (6.46), unit 32 (6.53), unit 45 (6.76): notes did not open with the print's reading in the house form ("The print has X, … a misprint for Y; t keeps the print, because t must match the pinned source"). Rewritten (26 also says the opening mark before the second `deus` is missing).
- unit 38 (6.62) `i`: "So far, and no further" adds a clause not in the Latin and is a stock phrase. Now "May the ill fortune of Troy have followed us only to this point."
- unit 39 (6.63-65) `i`: "offended" mistranslates `obstitit` (stood in the way of); "proud" for `ingens`. Now "in whose way Ilium and the great glory of Dardania stood".
- unit 43 (6.72-74) `i`: added "to guard them", not in the Latin. Removed.
- unit 62 (6.96-97) `i`: "which you least expect… will open from a Greek city" is close to the stock English rendering. Now "Your first road to safety, though you could never guess it, will lie open from a city of the Greeks."

Low (17):
- unit 0 n: `oris` "goes with it" -> dative of the place reached.
- unit 8 `i`: "at last" for `primum` (with "first" later); removed.
- unit 15 n: `reginae` queen (l) vs princess (i): note now says Ariadne, Minos's daughter, "the princess" in `i`.
- unit 19 n: tense gloss of `perlegerent… adforet` (imperfect subjunctive for pluperfect), as at 31.
- unit 27 `i`: "braided hair" is not in `comptae` (combed, dressed) -> "carefully dressed hair".
- unit 31 n: says the speech is still open and runs to the end of 53.
- unit 35 n: `Aeacidae` called a "Greek genitive" -> genitive of the patronymic `Aeacides`.
- unit 39 n: `dique` "being dei-que" -> `diique`, nominative plural of `deus` + `-que`.
- unit 48 `i`: `os` "lips" -> "mouth" (l has mouth).
- unit 51 `i`: "But heavier trials await you on land" is close to a stock version -> "But on the land there are still heavier things in store."
- unit 55 n: `Bella, horrida bella` "an anaphora" -> repetition with an adjective between.
- unit 58 (pass 2) `i`: "set on the Trojans" ambiguous -> "fastened upon the Trojans".
- unit 59 n: `oraveris` future perfect preferred (perfect subjunctive possible).
- unit 26 (pass 2) `l`: lost its opening `“` when `l` 25 closed the first quotation; restored (`“the god, look, the god!”`).
- notes of units 27, 33, 46: one sentence each pointing to the misprinted closing mark now at their head (part of M10).
- echo scan: no other distinctive echo found in `i` or `about`; kept as they are: "so the story goes" (6.14), "Wars I see, grim wars" (6.86-87), "Do not give way before your misfortunes" (6.95).
- `about`: checked against the Latin, nothing wrong.

## Misprints (rule 5b; t as printed; reading in l and i; entry in questions-entry.md)
Drafter's list (6.45, 52, 53, 76) confirmed and extended: 6.45 `virgo.` (full stop for comma) and `“tempus` at 46 (opening mark for closing mark after `tempus`; no opening mark before the second `deus`; `deus! ”Cui`); 6.52 `“Tros` (opening mark for the closing mark after `Tros`, and a fresh one before `Aenea`); 6.53 `domus. ”Et`; 6.76 `oro. ”Finem`. Notes now open with the print's reading in every unit that holds one (25, 26, 30, 32, 45), and 27, 33, 46 point back. Marks in l/i: l 7 open / 7 close, i 7 / 7; speeches: 37-39 (units 20-21), 45-46 (25-26), 51-53 (30-32), 56-76 (35-45), 83-97 (50-62) all open on the first unit and close on the last.

## Scansion (14 entries added to scan-fixes.json)
Hand-scanned every line, not only the flagged ones; all lines with Greek eu (2, 41, 42, 54, 67, 90, 93), initial Ae- (9, 40, 52, 58), consonantal i after a prefix or hiatus (14, 21, 33, 34, 51, 56, 58, 61-64, 81, 89, 91, 93) and the flagged 36 and 94.
Major (14): 6.9 and 6.40 Aeneas/Aenean split A-e by the scanner (recurring Ae- blind spot); 6.41 and 6.54 Teucros/Teucris split Te-u; 6.42 Eu- of Euboicae split E-u and excisum with long -ci-; 6.36 (COSTLY 2.0) Deiphobe is Dē-ĭ-phŏ-bē, four syllables; 6.94 UNRESOLVED -> half-line entry (externique iterum thalami); 6.93 coniunx with consonantal i (con-iunx), as 4.48 and the published parts; and six lines the scanner fitted without flagging (cost under 2.0) with wrong quantities: 6.16 insuetum (sue one long syllable, as suetus/sueti in published parts), 6.23 `elata mari` (ē-lā-tă mă-rī, not ĕ-lă-tā mā-rī), 6.24 crudelis (long cru- and -de-, as everywhere else), 6.92 `quas gentes Italum aut quas non oraveris urbes` (non, ō-rā long; Ĭtalum short I-), 6.95 `Tu ne cede` (nē and cēde long), 6.97 `quod minime reris` (mĭ-nĭ-mē, rē-ris).
Checked by hand and left as the scanner has them: 6.1, 3-8, 10-13, 15, 17-22, 25-35, 37-39, 43-53, 55-91, 96. Of those the following rest on one licence or an unconfirmed quantity (doubtful, left on the only fit found):
- 6.2 `Euboïcis` four syllables Eu-bo-ï-cis (diaeresis printed); 6.42 `Euboicae` entered with four syllables too (Eu-boi-cae with three also fits).
- 6.14 `Minoïa` Mī-nō-ĭ-ă; 6.58 `Aeacidae` Ae-a-ci-dae.
- 6.21 `Cecropidae` Cē- long before cr (muta cum liquida); 6.25 `Pasiphaë` with long Pā-; 6.60 `Massylum` with long sy- (the only fit; 4.132 Massyli is also in QUESTIONS); 6.87 `Thybrim` with long Thy- before br.
- 6.33 `omnia` with synizesis (om-nia, the only way the line fits); 6.37 `sibi` with long -bi- at the caesura; 6.52 `Neque enim` with long Ne- and e- (nĕ-qu'ĕ lengthened in arsis), and `Aenea` read Ae-nĕ-ă; 6.66 `da` long; 6.67 `meis` as two syllables (mĕ-īs); 6.75 `ludibria` with long di- before br; 6.79 `fatigat` with long -ti- (fatīgo).
- 6.61 `Italiae` with long I- vs short I- in 6.92 `Italum` (both occur in Virgil; the published parts differ too).

## Refused or left findings
- Left as drafted: unit 3 note's "stern-first" (consistent with `obvertunt… proras`); unit 6 note "Aurea tecta is Apollo's golden temple, which the next lines say Daedalus built" (it is Apollo's temple at 18-19; fine); unit 17 `levis` "predicative nominative" (acceptable label); unit 22 `Cecropidae` "nominative plural, Greek in form" (defensible); unit 29 `maior videri` "infinitive of respect (a Greek construction)" (acceptable); unit 53 note `hanc curam` "the worry about reaching Italy" (commentators differ; not a grammatical label, left).
- Refused: correcting the reading text in `t` for the misprints (the build requires `t` to match the pinned source; rule 5b allows the note-only route when the checks do not allow the correction; see questions-entry.md). Refused: changing 6.52 `Neque enim` to a short-Ne fit (no all-natural fit found; entered as doubtful above).
- Refused: adding scan-fixes entries for lines where the scanner's fit differs from mine only by free open syllables I cannot confirm (6.37, 6.52, 6.60, 6.66, 6.75, 6.79 above).
