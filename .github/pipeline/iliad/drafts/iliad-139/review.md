# Review, iliad-139 (Iliad 22.90–187)

Two passes. First pass: notes (grammar, positions, cross-references), Greek to `l`, `l` to `i`, remembered English
(against the conventions tables and every published unit with the same Greek), quotation marks, neighbouring parts.
Second pass: `gloss.json` against the lines and against `known-forms.json`. `units.json` and `gloss.json` were
edited in place by script; `t` was not touched (checked: the `t` fields joined equal the packet's 98 lines).
Unit = the `sentences` entry, named by its first line number `ln` (two units share 108, 131, 136, 141, 147, 183).
Backups of the pre-review files are in the scratchpad (`units.before.json`, `gloss.before.json`).

Cross-references checked and found true: 6.442 (= 22.105), 9.403 (= 22.156), 11.403 (= 22.98), 11.407 (= 22.122),
16.441–442 (= 22.179–180), 16.443 (= 22.181), 8.39 (= 22.183–184), Odyssey 1.28 (= 22.167). Part boundaries:
iliad-138 ends on a closed speech (`”` at 22.89), so 22.90 opens in narration; no speech runs out of this part at 187.
Scanner flagged nothing; no line was hand-scanned for that reason (no irregularity claimed in any note).

## Changes

| line · field | severity | wrong | done |
|---|---|---|---|
| 136 (οὐδ’ ἄρ’ ἔτ’ ἔτλη) · `l`, `i`, `n` | major | "dared" for ἔτλη: the table fixes τλάω as "bring oneself to" ("dared" is reserved for θαρσέω; rows 7.151, 7.480, 17.733) and iliad-131 (ln 421, same Greek οὐδ’ ἄρ’ ἔτ’ ἔτλη, Iliad 21) ships "no longer then did he bring himself" / "could no longer bring himself" | `l` "and he no longer brought himself / to stay there…", `i` "and he could no longer bring himself to stay where he was…"; note gloss "endure, dare" → "endure, bring oneself to", "no longer did he dare" → "bring himself" |
| 111 (καὶ κόρυθα βριαρήν) · `l`, `i`, `n` | major | "stout helmet" for βριαρήν: the table fixes βριαρός as "weighty" (`l`) / "heavy" (`i`) (11.375, 16.413) and iliad-067 ships "the weighty helmet" / "his heavy helmet" for this very phrase; "stout" is reserved for στιβαρός/παχύς. new-renderings.md wrongly says "heavy" is avoided | `l` "my weighty helmet", `i` "my heavy helmet", note "stout, heavy" → "weighty, heavy". (new-renderings.md row not edited, see below) |
| 175–176 (δαμάσσομεν) · `l` | major | Zeus's speech (168–176) is closed with `”` in `i` but not in `l` | `”` added at the end of `l` |
| 107 · `mark` | medium | an imagined speech inside a speech has a `mark` in the published parts (iliad-022 ln 178 "A Trojan speaks, as Agamemnon imagines it", iliad-040 ln 460 "The onlooker says"); this unit had none | `mark` "A Trojan speaks, as Hector imagines it" |
| 107 · `n` | medium | note contradicts `i`: says the English "gives the sense, relying on it" while `i` says "trusting"; also calls ἧφι βίηφι "by his own might" (instrumental) and then makes it the object of πιθήσας; also "aorist participle of πείθομαι" where the glossary has πιθέω | note now: ἧφι βίηφι "his own might", old ending -φι "doing the work of a dative after πιθήσας"; πιθήσας "aorist participle of πιθέω, the epic form of πείθομαι"; "trusting in it" |
| 131 (ὣς ὅρμαινε μένων) · `l`, `i`, `n` | medium | same Greek as iliad-132 ln 64 ("So he pondered, waiting;" / "So he pondered, standing there;"); the draft invented "remaining where he was" / "as he stood his ground" without a reason (rule: same Greek, same English) | `l` "So he pondered, waiting,", `i` "So he pondered, standing there,"; note "stay, remain" → "stay, wait" |
| 130 (εἴδομεν) · `n` | medium | note calls εἴδομεν the "aorist subjunctive of εἶδον (= εἴδωμεν)"; the aorist subjunctive of εἶδον would be ἴδωμεν, the glossary's existing entry (and the gloss.json broadening) treats the form as the short-vowel subjunctive of οἶδα; note and gloss disagreed | note: "the short-vowel subjunctive of οἶδα (= εἰδῶμεν), ‘let us see, find out’" |
| 104 (ἀτασθαλίῃσιν) · `l` | minor | "wanton follies"; the table's `l` is "wanton-follies" (hyphen; 1.7, 4.409) | "wanton-follies" |
| 169–170 (ἔκηεν) · `n` | minor | "epic imperfect of καίω": ἔκηα/ἔκηε(ν) is the aorist (cf. 1.40 ἔκηα); gloss.json already had "aor." | "the epic aorist of καίω (ἔκηα)" |
| 119–121 · `n` | minor | last sentence a bare list of glosses with no verb, no syntax | "κτῆσιν ‘property’ is the object of δάσασθαι, with ὅσην ‘as much as’; πτολίεθρον ‘citadel’ is the subject of ἐντὸς ἐέργει …, and ἐπήρατον means ‘lovely’" |
| 117–118 (ἀποδάσσεσθαι) · `n` | minor | "the infinitive of ἀποδατέομαι": the -εσθαι form is the future infinitive, like δωσέμεν; the unlabelled infinitive invited the aorist reading | "the future infinitive of ἀποδατέομαι" |
| 103 · `n` | minor | "the second a wish turned round" is not a description of an unreal-past remark | "the second a regret" |

## Changes in gloss.json

| form · field | severity | wrong | done |
|---|---|---|---|
| ἀποδάσσεσθαι | medium | "aor. inf. mid. … (= Attic ἀποδάσασθαι)": an aorist middle infinitive would be -ασθαι (δάσασθαι at 120 is that); this is the future | "fut. inf. mid., epic -σσ- (= Attic ἀποδάσεσθαι)" |
| ἐλάμπετο | medium | garbled: "mid. impf. 3 sg. (λάμπομαι), with pass. form of the gleaming" | "impf. 3 sg. mid. (λάμπομαι, the middle has the active sense): ’shone’" |
| __broaden__ μίμν | medium | known entry says "pres. imper. 2 sg." but the line has μίμν’ = imperfect 3 sg. (ἀλλ’ ὅ γε μίμν’ Ἀχιλῆα); not broadened | old entry whole + " · also impf. 3 sg. act., unaugmented, elided (μίμν’ = μίμνε), + acc.: ’kept waiting for’ …" |
| κορυθάϊκι | minor | lemma spelt κορυθαίξ (αι) but the form and the note have -άϊ- | lemma κορυθάϊξ |
| βεβρωκὼς | minor | "(+ gen.)", copied from the Odyssey entry; here the object φάρμακα is accusative | "+ acc." |
| __broaden__ σαώσομεν | minor | known entry gives only the hortative "let us save"; the line is an indirect deliberative alternative (ἠέ μιν … σαώσομεν) | " · also in an indirect deliberative alternative: ’whether we shall save’" |
| __broaden__ κεν | minor | ἐπεί κ’ ἀπὸ τεύχεα δύω (125): ἐπεί κεν + aorist subjunctive not covered (only ἐπεί κεν + future) | " · also ἐπεί κεν + aor. subj., in a temporal clause: ’once’ …" |

All other gloss entries checked against the line and found right (case, number, tense, voice, lemma); novel list and gloss keys
match exactly (no key missing, none extra); all novel entries under 230 characters; only ’ used; JSON parses (it did before; no parse error found).
Known forms checked for coverage of their use here and found adequate: ἔτλη, τῷ (22.127, "with him"), ἤ (22.122), ἠέ, ἦέ, ἢ,
ἔπλετο, ὕπο, ὕπαιθα, ἰθύς, ἐρινεόν, ἀνώγει, ἐπεί, πρίν, ὥς and the rest of the 445.

## Refused findings (considered, not changed)

- **ἀεθλοφόροι (22.162) "prize-bearing" vs iliad-138's "prize-winning" (22.22).** Kept. The same-Greek rule does not bind two different forms
  (ἀεθλοφόρος ἵππος / ἀεθλοφόροι ἵπποι) in different contexts; 22.162 is the plural phrase of 11.699 (ἀθλοφόροι ἵπποι, "prize-bearing", with a
  conventions row saying "prize-winning" is wrong where the prize is not yet won), and these horses are racing for the prize. 22.22 is a shipped part.
  Standing inconsistency inside Book 22, already flagged by the drafter; the cure, if wanted, is in iliad-138 (22.22 to "prize-bearing"),
  not here. conventions row 6649 (ἀεθλοφόρος 22.22) and row 3907 now disagree and should say so.
- **Capital letter in `i` after a semicolon** (165 "So the two of them circled…", 143 "So Achilles flew…"). Published parts do this constantly
  (403 of 970 checked cases); `i` is allowed its own sentence division.
- **Τρωσίν (119) "loose dative".** The note's label is right (dative of the persons from whom the oath is taken; `l` "for the Trojans", `i` "from the Trojans"); no change.
- **ἐμμεμαώς (143) `i` "eager"** against the 17.735 row's "full of eagerness": the row is a dual with a different sentence; "eager" is the table's `l` and the shipped μεμαυῖαν `i` ("already eager") is in the same part. Kept.
- **ὁπποτέρῳ (130) `i` "of us two"**: the row 3.309 has "of the two"; "of us two" is the same word made clear by the first person plural of εἴδομεν. Kept.
- **22.167 `l`/`i` ending in a colon where Odyssey 1.28 has a semicolon**: the drafter's reason (a speech follows) is right; only the final mark differs; kept.
- **οἴμησε (139) "darted" in `l`, "darts" in `i`** with the gnomic aorist: `l` literal, `i` idiomatic; the note says so. Kept.
- **ἀπὸ δρυὸς οὐδ’ ἀπὸ πέτρης (126)**: the note rightly says the sense is not known and `i` decides nothing. Kept.
- **22.98, 103, 105, 122, 156, 177, 179–182, 184, 186–187** reuse published English correctly (differences only at the punctuation and the added `”`/`“`);
  22.103 `l` has "; truly …" for the published ", — truly … , —" because the unit ends there; kept.
- **ὀχθήσας / ὄρνυμι / ἔειπες / μεμαυῖαν** notes: checked, true.
- **τρήρωνα "timorous"**, **ἠνεμόεντα "windy"**, **σιγαλόεντα "glossy"**, **πελώριον "huge"**, **κραιπνοῖσι "rushing"**, **Πηλιάδα μελίην**, **ἐρινεόν "wild fig-tree"** all agree with the tables.

## For the caller (not done by the reviewer)

- `new-renderings.md` still says βριαρήν is "stout" and that "heavy" is avoided (wrong, see above); it also has "remaining where he was" / "as he stood his ground"
  for 22.131 and no row for ἔτλη. If `make139.py` regenerates `units.json`, do not rerun it, or the corrections above are lost (the generator was not edited).
- `known-forms.json` / `gloss.json`: the `μίμν`, `σαώσομεν`, `κεν` broadenings were added by the reviewer; they begin with the old entry whole.

## Counts

`units.json`: 3 major, 4 medium, 5 minor (12 findings). `gloss.json`: 0 major, 3 medium, 4 minor (7 findings).
Total 19 findings: 3 major, 7 medium, 9 minor. Refused: 10.
