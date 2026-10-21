# Review — iliad-041 (7.1–91), two passes

Edits were made to `units.json` by script; `t` was never touched (checked: the units' `t`, joined, equal lines 1–91 of the archive; every `ln` is the line the unit starts on). Unit numbers below are by `ln` (line the unit starts on).

## Open problem for the caller (not fixable without touching `t`)

- **7.43 · `l`/`i` · HIGH (validator).** The unit `ὣς ἔφατ’, οὐδ’ ἀπίθησε θεὰ γλαυκῶπις Ἀθήνη.` has the same Greek as the whole unit at 5.719 (iliad-034, line 719), whose published English is `l` "So she spoke, and did not disobey, the goddess, gleaming-eyed Athena." and `i` "So Hera spoke, and the goddess, gleaming-eyed Athena, did not disobey." `validate_iliad.py` check 6 will FAIL the draft's (correct) "So he spoke … " because the English must be identical. The published `i` is wrong here (Apollo spoke, not Hera; the 5.719 `i` names Hera although the Greek does not). Left as drafted. Ways out, for the caller to choose: (a) join this unit with the next (7.43 + 7.44–45) so the Greek differs, as iliad-008 did for 2.166–167; ready text would be `l` "So he spoke, and did not disobey, the goddess, gleaming-eyed Athena.\nAnd of them Helenus, Priam’s dear son, put together in spirit\nthe plan, which pleased the gods as they were devising;" and `i` "So he spoke, and the goddess, gleaming-eyed Athena, did not disobey. Helenus, Priam’s dear son, grasped in his spirit the plan that pleased the gods in their devising;" with the two notes joined; (b) copy the published English and accept "Hera" (false in context); (c) QUESTIONS.md. I recommend (a). Every other whole-unit repeat checks out identical (7.28 = odyssey-101; 7.33 = iliad-003 and three Odyssey units; 7.66b = iliad-017; 7.91a = iliad-040).

## Pass 1 — notes, then Greek → `l` → `i`, remembered English, quotation marks

### Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 7.47 | `l`, `i`, `n` | HIGH | μῆτιν rendered "counsel". The house table (Διὶ μῆτιν ἀτάλαντον, 2.169) fixes μῆτις as "cunning" and expressly turns down "peer of Zeus in counsel". | `l` "to Zeus in cunning equal", `i` "the equal of Zeus in cunning"; note says μῆτις is "cunning" throughout. |
| 7.70 | `l`, `i`, `n` | HIGH | τεκμαίρεται rendered "ordains". The table (τεκμήραντο 6.349; τεκμαίρομαι 7.317) gives "fix" and turns down "ordained", "decreed". | `l` "he fixes matters for both", `i` "he fixes matters for both sides"; note cites 6.349. |
| 7.91 | `l`, `i`, `n` | MEDIUM | κλέος οὔ ποτ’ ὀλεῖται is a repeated formula (2.325, iliad-010, "fame will never perish"); the draft gave "glory". | "my fame never will perish" / "my fame will never perish"; note says the phrase is that of 2.325 and keeps its English. |
| 7.26 | `l`, `i` | MEDIUM | ἦ ἵνα δή … δῷς is purpose ("is it in order that …"); "Is it so that …" loses the purpose and can read as a plain "is it the case that". The note itself says "in order that". | `l` "Is it, then, in order that to the Danaans …", `i` "Is it in order that you may give the Danaans …". |
| 7.24 | `i`, `n` | MEDIUM | `i` moved αὖ onto ἦλθες ("come again from Olympus"), which says she has come before; αὖ goes with σύ. Also the table (1.202 τίπτ’ αὖτ’ …) turns down "have you come again" for this construction. | `i` "Why, you again, daughter of great Zeus, so eager, have you come from Olympus?"; note says αὖ goes with σύ. |
| 7.44 | `i`, `n` | LOW | `i` "had pleased" shifts the imperfect ἐφήνδανε to a pluperfect (`l` and note say "pleased"). The note also left τῶν without a construction. | `i` "the plan that pleased the gods in their devising"; note: τῶν δ’ "and of them" means the two gods, whose plan it is. |
| 7.90 | `i` | LOW | "in the fight" is not in the Greek (ἀριστεύοντα only). | "once killed while he was excelling". |
| 7.66 | `n` | MEDIUM | Note said the unit "is word for word 3.85". 3.85 is `ἐσσυμένως· Ἕκτωρ δὲ μετ’ ἀμφοτέροισιν ἔειπε·`; only the second half matches. | Note now says "word for word the second half of 3.85 (which begins with ἐσσυμένως)". |
| 7.54 | `n` | LOW | "The three lines are nearly word for word 3.76–78": the unit is 7.54–56a (two lines and a half) against 3.76, 3.77, 3.78a, and the differences were not named. | Reworded: "These lines … (χάρη for ἐχάρη, οἳ for τοὶ)". |
| 7.49 | `n` | LOW | "the English is the same" as 3.68 — the `l` line is, but `i` has "make the others" where iliad-016 has "make all the others" (the Greek has no πάντας there). | "nearly the same (‘all’ is not in the Greek here)". Wording of `i` kept (it is the more exact). |
| 7.49 | `n` | LOW | προκαλέω / προκαλέομαι used inconsistently across notes 7.38 and 7.49. | Both now "προκαλέω (middle)", as the existing glossary entry for προκάλεσσαι has it. |
| 7.87 | `n` | LOW | 6.459 is printed `εἴπῃσιν` (with ν); the note called it "the form of words" with -σι. | Added "(there with a final ν)". |
| 7.30 | `n` | LOW | `l` renders the dative ὑμῖν as "of you"; the note did not say the dative names whose spirit it is. | Note adds: ὑμῖν names whose spirit it is (‘to your spirit’). |
| 7.41 | `n` | LOW | ἀγασσάμενοι: "the second sense fits better" stated as if settled. | Note adds that the choice is a judgment from the context (see refused findings). |
| 7.11 | `n` | LOW | λύντο called an "aorist passive" (the glossary calls it middle with passive sense). | "an unaugmented aorist of λύω with passive sense (middle in form)". |
| 7.58 | `n` | LOW | ἑζέσθην called a "dual aorist"; it is the dual of the imperfect (cf. ἕζετο). | "a dual past tense (imperfect)". |
| 7.36 | `n` | LOW | καταπαυσέμεν described only as "-έμεν"; it is the future infinitive (after μέμονας). | "an epic future infinitive in -σέμεν". |
| new-renderings.md | rows | — | Rows for μῆτιν, τεκμαίρεται, κλέος, ἀριστεύοντα were out of step with the edits above. | The four rows were rewritten to match. |

### Cross-references (all verified against `source/iliad-monro-allen1920.json` and the published parts)

- **3.20** = 7.40 = 7.51, `ἀντίβιον μαχέσασθαι ἐν αἰνῇ δηϊοτῆτι` — true; iliad-016 unit at 3.18 has the same line, English reused exactly. "where Alexander made the same challenge" is true (3.19–20 narrate his προκαλίζετο).
- **3.68** = 7.49 `ἄλλους μὲν κάθισον Τρῶας καὶ πάντας Ἀχαιούς` — true; spoken by Alexander to Hector at 3.67–68.
- **3.76–78** — true with the differences now named (3.76 αὖτ’ ἐχάρη, 3.78 τοὶ).
- **3.85** — half-line only (fixed above). **3.86** `κέκλυτέ μευ Τρῶες καὶ ἐϋκνήμιδες Ἀχαιοὶ` — true, word for word.
- **5.711–712** — 5.711 is `… θεὰ λευκώλενος Ἥρη`, 7.17 has `γλαυκῶπις Ἀθήνη`; 5.712 identical. True as stated.
- **1.526** `τέκμωρ` — a "sign" in iliad-006 (unit at 1.525); true.
- **6.459** — true (see the ν remark). Also checked: `ὥς ποτέ τις ἐρέει·` is 6.462, and 7.91a is identical to the published unit.
- **Odyssey 7.187** — `ὄφρ’ εἴπω τά με θυμὸς ἐνὶ στήθεσσι κελεύει` is the second line of odyssey-031's unit at 7.186; true. Also 8.26.
- **1.206** (formula note at 7.33) — true; iliad-003.
- Internal: "returns at 16" (λύντο), "λύντο at 12 and 16", "the line already used at 40" (7.51), "as in line 23", "as at 20", "as at 87", "the oak (60)", "answered by Ἕκτωρ δ’ in line 11", "εἰ μέν of line 77", "as in line 48" — all true. Positions: the unit-ends "in the middle of line 20 / line 30 / line 27 / line 56" are true; "δῷς at the start of the next line" true.

### Considered and refused

- **ἀγασσάμενοι 7.41 "feeling indignation".** Kept. ἀγάομαι/ἀγαίομαι has both senses; the Odyssey table already fixes ἀγαιόμενος "indignant" and ἀγάασθαι "resent" apart from "wonder", and after a challenge to the whole host "indignant" suits the sentence. Only the note's wording was loosened (judgment from context). `l` and `i` agree.
- **Δεξιάδην 7.15 kept as a name.** Kept: iliad-027 already ships Ἁρμονίδεω as "Harmonides" without naming the father, and every shipped "son of X" has X in the line. The note says why.
- **ἄμμ’ 7.76 ambiguity.** Kept. The elided form is dative ἄμμι or accusative ἄμμε; "for us / our witness" fits a dative of interest and the note says the form does not decide it. The glossary entry now records both readings joined by " · ".
- **ἑλέτην "the two took" / "killed"**; follows iliad-032. **κορυνήτης "club-wielder"**, **τέκμωρ "an end for Ilios"**, **ὣς φίλον ἔπλετο**, **ἑκάεργε "far-working"** (table), **ὑψίζυγος**, **αἰειγενετάων**, **πεφρικυῖαι** (iliad-024 "bristling"): all in line with shipped English.
- **λύντο δὲ γυῖα "gave way" in `i` / "were loosened" in `l`.** Kept (the table has no row; λέλυνται is "loosened" in `l` at odyssey-090, and the unit uses the same pair at 12 and 16).
- **οὖρον "a fair wind".** Kept; the Odyssey ships "a fair wind" for bare οὖρον (19.585 etc.); "favouring" is reserved for ἴκμενον.
- **Quotation marks.** “ on 24, 34, 38, 47, 67; ” on 30, 36, 41, 53, 91b; nested ‘ ’ on 89 (the later sailor), as iliad-040 does at 6.460; `mark` on each speech's first unit; Hector's speech (7.67–91) closes at 91 and the next part opens with ὣς ἔφαθ’ (7.92), so nothing runs on. Opening/closing counts match (5/5).
- **Paragraph flags.** `p` on 1, 8, 17, 33, 37, 43, 54 — matches the ¶ marks.
- **Unit lengths.** 7.38–40 ends at a comma and 7.81–83 at a comma; each sentence would run past four lines (5 and 6), so the comma cut is permitted.
- **Remembered English.** Nothing suspect: no unit's English looked ready-made; the renderings follow the table or the grammar.
- **Scansion flags.** The packet flags none; no line was hand-scanned, no irregularity note added.

## Pass 2 — `gloss.json` (existed at the start of pass 2; 101 novel forms + `__broaden__`)

Every novel form was checked against its line(s); all 101 forms are present; no entry reaches 230 characters; no ASCII apostrophe or backtick. `__broaden__` entries all begin with the existing entry whole followed by " · " (verified by script), and each added reading was checked against its line. The known-forms list (349) was read for uses the existing entries do not cover.

Fixes made directly in `gloss.json`:

| Form | Problem | Fix |
|---|---|---|
| ἀγασσάμενοι | lemma ἄγαμαι alone; the existing entry for ἀγασσάμεθ’ lemmatises `ἀγάομαι (ἄγαμαι)` | lemma made `ἀγάομαι (ἄγαμαι)` |
| ἄμμ | committed to the dative only; the elided form is a genuine homograph of ἄμμι/ἄμμε (the note says so) | both readings given, joined by " · " |
| ἀτάλαντε | example said "equal to Zeus in counsel" | "in cunning" (house rendering) |
| κορυνήτης | meaning "club-bearer, club-man" (both turned down in new-renderings.md); "epithet of Areithous" pins it to a line | "club-wielder (κορύνη ’club’); masc. nom. sg." |
| στεφάνης | "ridge-rim of a helmet" asserts a part the renderings deliberately do not decide | "rim, ring; of a helmet, its rim (exact part uncertain)" |
| τεκμαίρεται | "devises, ordains" conflicts with the table ("fix") | "fix, appoint …: ’fixes’" |
| ἑκάεργε | "far-working, far-darter" mixes the table's two epithets (far-darter is ἕκατος) | "far-working … sense disputed, ’far-shooting’ another guess" |
| φρὶξ | gloss ’ruffling’ (a word the renderings avoid) | ’ripple’ |
| φυλομέδουσα | "Phylomedousa" (not the English name used) | "Phylomedusa" |
| αἰγυπιοῖσι | "agreeing with ὄρνισιν" pinned to the line | dropped |
| `__broaden__` εἵατ | existing entry has only present εἵαται; 7.65 εἵατ’ is the imperfect εἵατο (as 7.61) | broadened: old entry + " · also impf. 3 pl., elided (εἵατ’ = εἵατο, = Attic ἧντο): ’sat’" |
| `__broaden__` ἀμφοτέροισιν | existing entry only "after μετά, ’among both’"; 7.70 is "for both" | broadened with " · also dat. of interest: ’for both’" |

Checked and left: every other parse (αὐχέν, βούλετο, δαμείετε, δῷς, εἴπῃσι, εὔπυργον, εὕρωσιν, κάμωσιν, κί, καταπαυσέμεν "fut. inf.", κατατεθνηῶτος, κρεμόω, λελάχωσι, λύντο, μέμονας, μελάνει, μητιόωσι, ναιετάοντα, οἰόθεν, ὄρσωμεν, πολυκλήϊδι, προκαλέσσεται, πυλέων, σύνθετο, συναντέσθην, ταναήκεϊ, ταρχύσωσι, φανήτην, χεύωσιν, ἐξέσσυτο, ἐπιάλμενον, ἐπόρσειαν, ἐφήνδανε, ἑζέσθην "impf." (the unit note was corrected to match), ἑτεραλκέα, ἠϊονῆα, ἰφίνοον, …). The broadened τῷ, ὑπὸ, γυῖα, ἀντίος, μάχης, πίθοιο, τέκμωρ, τοί, μοῖρα, ἐχεύατο, ἔπι, αὐτῆς, δόμεναι, δώῃ, σῆμα each fit the line cited.

Not broadened, judged covered by the existing entry: τι (εἴ μοί τι πίθοιο — "adverbial acc. after εἰ"), πρὸς (πρὸς … ἔειπεν — tmesis already there), μῆτιν ("counsel" in the old entry is a lexical sense; the rendering is fixed in the units), ἥ (relative, already there).
