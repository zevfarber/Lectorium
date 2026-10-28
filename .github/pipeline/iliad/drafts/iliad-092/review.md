# iliad-092 — review (Iliad 15.92–183)

Two passes. Pass 1: notes against the lines, Greek → `l`, `l` ↔ `i`, remembered English and house table, quotation marks and `mark`s, the neighbouring part (iliad-091 ends on Themis's closed speech, so unit 1 correctly has no opening mark carried over; Poseidon's reply at 15.184 opens the next part). Pass 2: `gloss.json`, every parse against its line. `t` was not touched (checked: the unit `t`s still concatenate to 15.92–183 exactly, `ln` and line counts of `t`/`l` agree, `p` stands on all seven ¶ lines, `“`/`”`/`mark` are right on all seven speeches).

Severity: high = wrong sense or broken structure; medium = false statement in a note, or a departure from the house table or from a published unit; low = wording or precision.

## Changes — units.json

| line | field | sev | what was wrong | what was done |
|---|---|---|---|---|
| 92 | n | low | "Themis, whose welcome ended the last part": it is her question that ends 091 | "whose question" |
| 97 | n | medium | κεχαρησέμεν called a "future-perfect infinitive … 'will have rejoiced'"; it is the reduplicated future infinitive | relabelled "reduplicated future infinitive of χαίρω, 'will be glad'" |
| 97 | i | low | "whether mortals or gods" turned οὔτε … οὔτε into a disjunction | "neither mortals nor gods" |
| 103 | n | low | μετηύδα called "unaugmented"; the augment is there (μετ- + ηὔδα) | "the imperfect … (μετά + ηὔδα)" |
| 104 | n | low | νήπιοι "vocative-like": it is a nominative of exclamation | reworded |
| 106 | l, i, n | medium | ὄθεται "takes no thought / has regard"; the table fixes ὄθομαι "heed" (1.181, 5.403) and the draft's new-renderings row contradicted it | "takes no heed" in `l`, `i`, note |
| 115 | n | medium | μὴ νεμεσήσετ' called "a future used as a command"; it is the short-vowel aorist subjunctive in a prohibition | corrected |
| 115 | n | low | "the standing way to say 'gods'" overstated | "the usual way" |
| 119 | l | low | "his horses": no possessive in ἵππους | "the horses" |
| 119 | n | medium | scansion flag real, not noted (see "Scansion" below) | one sentence added |
| 123 | l, i, n | medium | πρόθυρον: note said "forecourt", `l`/`i` said "doorway"; the table fixes "forecourt" and lists "doorway" as avoided (3.493, 11.777) | `l`, `i` now "forecourt"; note kept "forecourt", gloss unchanged |
| 128 | l, i, n | low | μαινόμενε "raving"; the table's μαίνομαι is "rage / go mad" (5.185, 6.132) | "Raging one" / "You are raging" |
| 138 | n | low | ἑῆος glossed only as "own" with no hint of the ancient doubt | added "sometimes taken as the genitive of ἐΰς 'good'; 'own' is followed" (the glossary entry already says so) |
| 140 | l, i, n | medium | "the stock and the offspring": the same words γενεήν τε τόκον τε are published at 7.128 (iliad-042) as "the lineage and the birth", and the table lists "stock" and "offspring" as rejected | `l`, `i`, note follow iliad-042 |
| 140 | n | medium | "The sentence-end falls in the middle of line 140": it is this unit's beginning that does, the sentence ends at 141 | "This unit begins in the middle of line 140." |
| 142 | n | medium | "the seat Athena found at 124": 124 is Athena's own seat she left; Ares's seat is not mentioned | "(the seat is not named; presumably it is his own)" |
| 147 | n | low | "-τε serves for the dual and the plural alike": the plural form is used for two addressees | reworded |
| 151 | n | low | ἵκανον and εὗρον both called "unaugmented aorists"; ἵκανον is an imperfect and εὗρον carries its augment | corrected |
| 158 | l, i, n | medium | βάσκ' ἴθι given as "Go, be off"; published 7.8, 11.186 and 8.399 (iliad-007, -050, -065) have "Go, set out" / "Be off with you" | `l` "Go, set out, swift Iris"; `i` "Be off with you, swift Iris, and announce …"; note "go, set out" |
| 162 | l, i, n | low | φραζέσθω "consider"; table's φράζομαι is "take heed / take care" (5.410); `i` also dropped the "even" of μή … οὐδέ | "take heed" (`l`), "take care … lest … he fail even to bring himself" (`i`), note |
| 166 | l, i, n | medium | ὄθεται "takes no thought" (as 106); στυγέουσι "dread", but the same half-line τόν τε στυγέουσι καὶ ἄλλοι is published at 7.111 (iliad-042) as "whom others too hate" and the table lists "dread" as avoided; note called Zeus "clearly" the antecedent | "takes no heed … whom others too hate"; note says "most naturally Zeus himself" |
| 170 | l, i, n | medium | κραιπνῶς μεμαυῖα διέπτατο given as "so rushing, eager, flew through the air"; the same half-line stands in iliad-091 (15.83) as "so at a rush, eager, flew across" and the table fixes κραιπνῶς "at a rush" (8.247) | "so at a rush, eager, flew across swift Iris" / "so, at a rush and in her eagerness, swift Iris flew across"; note points to 15.83 |
| 182 | l, i, n | medium | as 166 (heed; "dread"); note said τόν "plainly" means Zeus | "takes no heed … whom others too hate"; "most naturally" |

## Changes — gloss.json (second pass)

| form | field | sev | what was wrong | what was done |
|---|---|---|---|---|
| κέλετ | entry | medium | glossed as imperfect κέλετο "bade"; at 146 the line, `l` and note all have the present, "bids" | "pres. 3 sg. mid., elided (κέλετ' = κέλεται): 'bids'" |
| νεμεσήσετ | entry | medium | "fut. 2 pl." (same error as the note at 115) | "aor. subj. 2 pl. act., short vowel … prohibition" |
| κεχαρησέμεν | entry | low | "mid." and "= Attic κεχαρήσεσθαι": -έμεν is an active infinitive ending | "fut. inf. act. … (= Attic κεχαρήσειν)" |
| καθάπτετο | entry | low | "(+ dat.)"; at 127 the person is accusative (Ἄρηα), the dative is of means | "(+ acc.)" |
| θαλερὼ | entry | low | meaning "blooming, sturdy, stout" and "both sturdy (thighs)"; house word is "flourishing" | "flourishing, blooming, sturdy" |
| ἔλθητε, ἴδησθε | entry | low | "the ending serves the dual too": false | "plural form, though two are addressed" |
| ὄθεται | entry | low | "care for, take thought of (+ gen.)"; the form here takes an infinitive and the house word is "heed" | "heed, care about (+ gen. or inf.) … 'heeds, takes care'" |
| ἀλεγίζει | entry | low | "heed, care for … 'heeds, cares'" overlaps ὄθομαι "heed" | "care for, take account of … 'cares'" |
| μαινόμενε | entry | low | "'raving one!'" | "'raging one!'" (follows the unit) |
| ἶσόν (`__broaden__`) | entry | low | "neut. acc. sg." for 183, where the accusative agrees with the unexpressed subject of φάσθαι (masc. or neut. have the same form) | "acc. sg. (masc. or neut.), agreeing with the unexpressed subject of φάσθαι …"; the old entry is still contained whole |

Checked and left: all other 78 novel entries (parse, lemma, "unaugmented/elided/epic" claims, ’ only, under 230 characters, no line numbers); the novel-forms list is covered exactly; every `__broaden__` value still contains the existing glossary entry whole; the new readings of αὐτή (you yourself), δαιτός (object of ἄρχε), εἶσι (+ future participle), ἔχεθ' (imperative), παραί (+ gen.), τοῦ (gen. of comparison), μή (εἰ μὴ + aorist; infinitive as command) fit the lines. Known-form entries spot-checked against their uses (τώ/τὼ "therefore" at 109 and 138, ἣ, ὃν possessive at 112, ἀνά + dat. at 152, εἰς ὦπα, ὑπὸ + gen. at 171, σέο, πὰρ + gen., σὸν): all covered.

## Also edited (outside units.json)

new-renderings.md, two rows brought in line with the above so that step 4 does not copy stale rows into the table: ἀφήμενος · ὄθεται now "takes no heed" (table's ὄθομαι "heed"); κραιπνῶς μεμαυῖα now "so at a rush, eager" / "at a rush and in her eagerness".

## Scansion (line 119)

Flag: UNRESOLVED; metrical lengthening of κέλετο. By hand: ὣς φά|το καὶ ῥ’ ἵπ|πους κέ|λε το Δεῖ|μον τε Φό|βον τε (the packet's reading). Feet 1–3 and 5–6 are regular (ῥ’ before ἵππους gives position in foot 2; μόν before τε, and βον before τε, are long by position). Foot 4 needs a long at the final syllable of κέλετο, which is short by nature before a single consonant Δ. So the irregularity is real as transmitted; the usual reason is that Δεῖμος began with an old double consonant. Sentence added to the note of the unit at 119: "The line is metrically irregular as transmitted: the last syllable of κέλετο, short by nature, has to stand in the long place of the fourth foot, as if Δεῖμον still began with a double consonant (the old digamma)."

## Findings considered and refused

- **ἔχεθ' (109)**: kept as imperative "bear". ἔχετε elided before ὅττι (rough breathing) gives ἔχεθ'; the middle ἔχεσθε is another way to the same sense, so no change; the gloss and the broadened ἔχεθ' agree. (Drafter's range "105–106/109/139–141": 105–106 ἆσσον ἰόντες / ἔπει ἠὲ βίῃ, and 139–141 ἤδη … τις … ἀμείνων / ἔπειτα / γενεήν, were read word by word; no further error beyond those listed above.)
- **"many-fountained" vs "many-springed" Ida (151)**: kept "many-fountained" / "of many springs" as in iliad-046 (8.47, the same accusative phrase, and the table row at 8.47). The later table rows (11.183 iliad-065, 14.157 iliad-087/088) have "many-springed" in `l`, and the 14.157 row lists "many-fountained" as rejected, but that row is for the genitive. The table is thus inconsistent for `l`; left for the owner (the `i` is "of many springs" everywhere, so only `l` differs).
- **αἰθρηγενέος (171)**: kept "born of the clear sky", note and gloss already say the sense is not certain; no better-attested alternative.
- **προτέρην (157)**: kept "first": accusative agreeing with Ἶριν, "Iris first (before Apollo)"; the alternative "the former Iris" has no support. The note's "i.e. before Apollo" is an inference from 143–145 and is flagged as such by "i.e.".
- **δαιτὸς ἐΐσης (95)**: kept; `l` "the equal feast", `i` "the equally shared feast" are the table's rows (1.468, 4.48).
- **Antecedent of τόν τε στυγέουσι καὶ ἄλλοι (167/183)**: kept Zeus (the speaker's own boast in 167; the reported boast in 183 where οἱ = Zeus). Poseidon as antecedent would make "others also hate" a threat the speech gives no ground for. Note now hedged ("most naturally").
- **ἑῆος (138)**: "own" kept; matches the glossary entry, with the ἐΰς doubt noted.
- **110 `i` omits "already"** for ἤδη: "by now" covers it.
- **139 `i` "in hand" for χεῖρας**: idiomatic; sense unchanged.
- **132 `i` "the measure of"** added to ἀναπλήσας: the note explains the image and the Iliad's other uses are "fill up"; the `l` is literal.
- **101 `i` "lips alone"**: "alone" is carried by οὐδὲ … ἰάνθη; kept.
- **100 `i` "troubled" vs `l` "vexed"**: the table's ὀχθέω row gives exactly this pair.
- **121 `i` "stirred up" for ἐτύχθη**: a free but faithful rendering of the aorist passive of τεύχω with a verbless "anger and wrath"; kept.
- **115–118 `i` rearranged** (πληγέντι … κεῖσθαι as two coordinate infinitives): sense and force kept; the construction is explained in the note.
- **130 `i` "just now"** for δὴ νῦν: acceptable.
- **137 `i` "seize us"**: object supplied from ἡμέας in the previous clause; kept.
- **ἀργαλέος 121 "grievous" vs 140 "hard"**: both follow the table (4.470 "grievous", 1.589 "hard"); the table is itself unsettled here, not the draft.
- **Units 47–48 (168, 169)**: `l` and `i` identical to iliad-065's units; correct. 114 `l`/`i` consistent with odyssey-063.
- **Quotation marks**: no change needed; seven speeches (93–99, 104–112, 115–118, 128–141, 146–148, 158–167, 174–183), each “ on the first unit with its `mark`, ” on the last; Hera's three, Ares's, Athena's, Zeus's, Iris's.

## Counts

| severity | units.json | gloss.json | new-renderings.md | total |
|---|---|---|---|---|
| high | 0 | 0 | 0 | 0 |
| medium | 12 | 2 | 0 | 14 |
| low | 11 | 9 | 2 | 22 |

Scansion flags: 1 (line 119), real, noted. Not built or validated (reviewer does not run the build).
