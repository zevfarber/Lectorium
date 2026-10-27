# iliad-086 — Iliad 14.1–108 — review, pass 1 (units)

Scope: every note label and cross-reference checked against the line and the repository (cross-references verified in the source and in the published parts: 10.135, 10.87, 13.458, 4.14, 4.317, 4.349–350, 9.114, 2.116, 2.153, 2.330, 12.70, 1.172, 1.482, 3.241, Odyssey 8.240, Odyssey 14.131); Greek to `l` word by word; `l` to `i`; remembered English (none found; the one phrase that arrived fully formed, none); speech marks (6 “ / 6 ” in each layer, `mark` on the first unit of each of the six speeches); scansion (the packet flags none; the scanner reports only a spondaic fifth at 4 and 54, see refused); sub-line and whole-unit repeats against all published Iliad and Odyssey units. `t` was not touched except as stated at 83. Gloss.json is for pass 2.

Counts: 2 high, 8 medium, 15 low changes (25 rows below); 15 findings refused.

## Changes

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 1 | l | high | “And Nestor did not escape the cry” says the opposite of the Greek: Νέστορα is the object of ἔλαθεν, ἰαχή the subject (the note said so, the `l` contradicted it). | `l` now “And Nestor the cry did not escape, drinking though he was, all the same,”. |
| 48 (τὰ δὴ νῦν πάντα τελεῖται) | l | high | Same Greek as the published unit at 2.330 (iliad-010) but `l` differed (“and those things now are all being fulfilled”); the validator's hard rule (letters-only key) would have failed the build. | `l` = the published “these things now all are being fulfilled.” (`i` already matched). Note: ‘those things’ → ‘these things’, and says the line stands at 2.330. |
| 31 | n | medium | Two false labels: εἴρυσαν called “unaugmented” (it is augmented: εἰ- = ἐ-ἐ-) and ἔδειμαν called “unaugmented” (ἔ- is the augment). | Note now says both are augmented aorists. (The unaugmented ἔρυσαν is at 35, where the note was right.) |
| 41 | n | medium | “προσέφη … unaugmented aorist of πρόσφημι”: προσέφη contains the augmented ἔφη. | “the past tense of πρόσφημι, with its augment”. |
| 44 | l | medium | The three infinitives (ἀπονέεσθαι, ἐνιπρῆσαι, κτεῖναι) were turned into indicatives in the last line of `l` (“he set on fire, and killed”). | “before with fire the ships he should set ablaze, and kill the men themselves.” |
| 63 | n | medium | “ἐστί, accented on its first syllable” — the edition prints ἐστὶ, accent on the last syllable; the claim was false of the printed form. | Accent claim removed; “ἐστί with the infinitive means ‘it is possible’.” |
| 65 | n | medium | “ἔχραισμε is the unaugmented aorist” — ἔχραισμε has the augment ἐ-. | “the aorist of χραισμέω ‘avail, help’”. |
| 75–76 | l, i, n | medium | ἅλα δῖαν rendered “heavenly sea”; the Iliad has shipped “heavenly brine” in both layers at 2.140 and 2.151 (and the Odyssey's from 3.153 on in `l`). Same words, same English. | `l`, `i` and note now “heavenly brine”. (new-renderings.md still lists ἅλα δῖαν as “heavenly sea” among the unchanged rows; that line is wrong, not a new row, and nothing needs copying.) |
| 83 | t, n | medium | Source drops the Greek question mark: 14.83 is printed with an ano teleia where the same line at 4.350 (iliad-024, published) has `;`. README rule 5 applies (punctuation only, one mark, already-published part prints the same line). | Done as reported below. `t` ends `;` now; note's last sentence replaced by “The line stands also at 4.350, and its English is kept.” |
| 95 | n | medium | The note cited “the Odyssey line at 92, in the optative ὄνοιτο”; ὄνοιτο is in 8.239, not in the line that stands at 92, and the note should assert nothing this part cannot show. | Parenthetical removed. |
| 1 | n | low | “ἔπεα πτερόεντα προσηύδα is the stock line”: it is half a line. | “stock phrase”. |
| 9 | n | low | “the next clause shows it, since he is carrying his own father's shield” confused which shield the son carries. | “The son is Thrasymedes, in whose hut the shield lay; the next line shows him carrying Nestor's own shield.” |
| 16 | n | low | 131 words (validator WARN, band 25–110). | Trimmed to 108 (dropped the κωφός gloss, the “house” sentence on λιγέων ἀνέμων, the “not roll” paraphrase); nothing asserted was changed. |
| 20 | n | low | “put as optatives, ἴοι … ἦε …”: only ἴοι is an optative. | Reworded: first course an optative, “go” understood after ἦε. |
| 24 | n | low | ἐναρίζω “in Homer is used simply for ‘kill’” overstates; the verb is also used of stripping. | “properly means to strip … and in Homer it often stands simply for ‘kill’”. |
| 33 | n | low | πάσας (agrees with νῆας) stood so that `l` can be read “all the beach”. | Note adds “πάσας agrees with νῆας, ‘all the ships’”; `l` left in Greek order. |
| 35 | n | low | “ὅσον … is answered by συνεέργαθον”: ὅσον goes with the verb, nothing answers it. | “goes with”. |
| 39 | n | low | “third singular of the aorist of 27” garbled (27 has the plural). | “the same aorist as ξύμβληντο in 27”. |
| 58 | n | low | “the phrase of 2.153”: 2.153 has ἷκεν (past), here ἵκει. | “echoes 2.153, ἀϋτὴ δ’ οὐρανὸν ἷκεν”. |
| 61 | i | low | “our wits” for νόος; the table has νόος “mind”, φρένες “wits”. | “and whether our minds can do anything;” |
| 77 | n | low | The reading of ὕψι ἐπ’ εὐνάων (afloat) was asserted flatly; it is the ancient interpretation. | “probably means”. |
| 88 | i | low | “the city of the Trojans of the wide streets” attaches the streets to the Trojans; εὐρυάγυιαν agrees with πόλιν. | “the city of the Trojans, with its wide streets,”. |
| 90 | n | low | “The line is also Odyssey 8.240” — which line was ambiguous (it is 92). | “Line 92 is also Odyssey 8.240”. |
| 95 | i | low | “for the thing you have said” turns the exclamatory οἷον ἔειπες into a plain causal. | “… altogether, what a thing you have said;” |
| 104 | n | low | “the vocative … with a single σ and the contracted ending”: -εῦ is the ordinary vocative of -εύς, not contracted. | “and a single σ” only. |

## Source correction (README rule 5), exactly

- Work and line: Iliad 14.83, `source/iliad-monro-allen1920.json`, book "14", `n` 83.
- Before: `Ἀτρεΐδη ποῖόν σε ἔπος φύγεν ἕρκος ὀδόντων·` After: `… ὀδόντων;` (U+00B7 replaced by U+003B, the same character the source uses for the question mark at 4.350 and 14.89). One mark, no letter or accent touched.
- Why: the sentence is a direct question (ποῖον), and the published part iliad-024 prints this line (4.350) with `;`; the English layers already ask a question. Confidence: high on the sense and on the published line; I did not have the printed page, so the evidence for the edition is the same line at 4.350 in the same source, which is what rule 5 names.
- Re-pinned: `parts.json`, only iliad-086 contains 14.83: sha256 `142a6608598032e0dc6571f8f49d28656543e14655ee40017c18cf6b8f0125dc` → `86b021872a38dbba23e9d0277b0830c7cbf77f4ad481aebe24f80bff0cb1e2e7`. Checked: `O.sha(lines_of(iliad-086))` equals the new pin; the units' `t` concatenate to the source exactly (validator's own test, reproduced by script).
- Draft: unit 83's `t` made to match. The validator keys repeats on letters only, so the unit already carried 4.350's English; it now has 4.350's Greek exactly, and `l` and `i` are identical to the published ones.
- To log (LOG.md, not written by me): “source correction (rule 5): 14.83 pinned source had `·` where published 4.350 has `;`; replaced, iliad-086 re-pinned”. `packet.md` still shows the old `·`; it is a derived file.
- `archive_iliad.py` would regenerate `·` if re-run; previous rule-5 fixes (7.139, 11.218) have the same property.

## Drafter's flagged doubts — decisions

- **14.83** ano teleia v. question mark: fixed in the source, above.
- **40 πτῆξε δὲ θυμὸν**: kept. Transitive “made cower” is the reading LSJ gives for this passage; the note already states that πτήσσω is usually intransitive, offers the alternative “cowered in heart”, and calls Ἀχαιῶν “probably” the whole army. The note's “Nestor's coming away from the fighting dismays the army” is an interpretation but is presented as what the unit takes. Left as is.
- **107 μῆτιν**: kept as “cunning”: the table fixes μῆτις “cunning” (2.169, 7.447 “his mind and his cunning”, 10.497 “the cunning of Athena”) and reserves “plan” for βουλή. The English is stiff but binding; the note says the word means skill in devising. Not changed.
- **101 ἀποπαπτανέουσιν** and **35 προκρόσσας**: the meanings are not known; each note says “not certain”, and `l`/`i` commit to one gloss each (“look about in alarm”, “in tiers”). “In tiers” is the LSJ-type gloss and the note describes the picture; the first is hedged by “probably” in the note. Accepted; the new-renderings rows say the sense is a guess.
- **77 ὕψι δ’ ἐπ’ εὐνάων**: accepted (εὐναί as anchor-stones, Il. 1.436 and the grammar of ὁρμίζω); “probably” added to the note's “means … afloat”, because `i` says “afloat”.
- **75 πρῶται**: accepted. “first” in `l`, “foremost” in `i`, and the note gives the place sense from ἄγχι θαλάσσης; 31's τὰς πρώτας (“the first ones”, first drawn up) is a different sense and `l` “first ones” there is fine.
- **53 παρατεκτήναιτο**: accepted, “rework / alter”; the note hedges and cites Odyssey 14.131 (checked: odyssey-067 line 131 has ἔπος παρατεκτήναιο).
- **71 ὅτε … ὅτε**: accepted. “when” the first time and “that” the second is the best reading of ᾔδεα … οἶδα; the note says the Greek leaves it open.

## Findings considered and refused

1. 4 and 54, spondaic fifth foot (scanner flag, not in the packet's list): refused. A spondaic fifth is a regular, if rare, variant; the Odyssey rules mention metre only where it explains a form, and the line scans as a hexameter.
2. Units that begin with a lower-case word after a full stop in `i` (e.g. 55 “for the wall…”, 63ff): refused; the published Iliad does this where the Greek continues with a connective (iliad-001 has seven cases).
3. 97 ἅλαδ’ `l` “to drag seaward” where iliad-057 has “to the sea” for the one-word ἅλαδ’: refused; the sentences differ, the sub-line reuse rule is “as far as your sentence allows”, and 100, 106 (ἅλα δ’) match the published “seaward”.
4. 59ff `i` “who can tell of a better cunning”: stiff English but the table binds μῆτις; refused (see 107).
5. 14.15 Τρῶας ὑπερθύμους in new-renderings.md: the row is not new (ὑπέρθυμος “high-spirited”, 4.365 in conventions); nothing to copy. The rendering itself is right.
6. 23–24 `l` “And they slew one another”: the imperfect could be “were slaying”; refused, the Iliad's `l` layer commonly gives imperfects as simple pasts (cf. “pondered” at 20), and `i` has “were killing”.
7. 5 `i` “wine that has the look of fire”: matches the table row (4.259).
8. 21 `l` “(them)” in parentheses: house style for supplied words (cf. “(past)” at 83, published).
9. 78 νὺξ ἀβρότη “immortal”: kept; the new row says why not “ambrosial” (that is ἀμβρόσιος, 2.19/2.57). The note's derivation is right.
10. 29 (14.53) “not even Zeus … could alter” for οὐδέ κεν ἄλλως … αὐτός: refused as a change; οὐδέ + αὐτός is “not even”, and the note keeps the literal “nor … in any other way” in `l`.
11. 62–63 `l` “into war I do not bid us to go” — correct case relations (πόλεμον accusative of goal, ἄμμε subject of the infinitive); refused.
12. 72–73 `i` “gives glory to these men on a level with the blessed gods” — τοὺς μέν are the Trojans (note says so); refused.
13. 88 `l` “So indeed are you set the city … to leave behind” — faithful to the order, line division kept.
14. 90–93 split at the comma after σκηπτοῦχός τ’ εἴη: legitimate, the sentence runs five lines (rule: break at the comma where the syntax pauses most).
15. 31–32 `i` “who thunders on high”: matches the table (12.68) and iliad-072; refused.

Not done: no change to `new-renderings.md` (reported above), `packet.md`, or `LOG.md`.
