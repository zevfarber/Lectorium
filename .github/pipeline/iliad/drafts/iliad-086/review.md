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


# Pass 2 (units re-read, gloss.json checked against the lines)

Scope: every note label and cross-reference re-checked against the line (stop marks, "begins/ends in mid-line" claims checked by script against `t`, line numbers cited in notes checked); Greek to `l` to `i` re-read for all 61 units; speech marks (6 speeches, `mark` and “/” present on the right units in both layers; the previous part, iliad-085, ends in narration, so nothing runs on); paragraph marks `p` against the packet (1, 9, 27, 52, 64, 82, 103). `t` untouched (list of all 61 `t` compared before and after the script). `gloss.json`: all 109 new entries read against the line they stand in (every form occurs in the part; none is already in the glossary; shape, ’ only, length under 230 all hold); all 25 `__broaden__` entries read against the lines (each keeps the old entry whole, each new reading is true of its line); and, because the glosser's task includes known forms, all 427 forms in `known-forms.json` read for whether the old entry covers the use here.

`__broaden__` shape: build_iliad.py reads `add.pop('__broaden__',{})` as `{form: new entry}` and dies unless `g[form] in new entry`; the file has exactly that shape (a dict at the top level of gloss.json, values the old entry whole plus ` · ` plus the new reading). No shape change was needed. It now holds 31 entries.

Counts: 0 high, 5 medium, 8 low changes (13 rows below); 5 findings refused; 2 notes for the caller.

## Changes

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 9, 66 | gloss (broaden τετυγμένον) | medium | Old entry parses only "masc. acc. sg., + dat. of material"; here the form is neut. acc. sg. (σάκος, 9) and neut. nom. sg. (τεῖχος, 66). | Added " · also neut. acc. sg., agreeing with σάκος: ’wrought’ · also neut. nom. sg., agreeing with τεῖχος: ’wrought, well-made’". |
| 10 | gloss (broaden κείμενον) | medium | Old entry "masc. acc. sg., agreeing with λίθον"; here neut. acc. sg. with σάκος. | Added the neut. acc. sg. reading. |
| 53 | gloss (broaden ἑτοῖμα) | medium | Old entry "neut. acc. pl."; here it is the predicate of the subject ταῦτα, so nominative. | Added " · also neut. nom. pl., predicate with ταῦτα: ’ready’". |
| 107 | gloss (broaden ἀμείνονα) | medium | Old entry "masc. acc. sg."; here fem. acc. sg. agreeing with μῆτιν. | Added the fem. acc. sg. reading. |
| 75 | gloss (broaden εἰρύαται) | medium | Old entry is ἐρύομαι "guard, protect… ’they guard’"; here it is ἐρύω "draw", ships "are drawn up" (the table row for 4.247–248 has "are drawn up"). The meaning was not covered. | Added " · also perf. pass. 3 pl. of ἐρύω ’draw’, epic -αται (for -νται): ’are drawn up’". |
| 75 | n | low | "νῆες ὅσαι stands first as a nominative that ἕλκωμεν … then takes as object": a nominative is not an object; it is a nominative left hanging, taken up by πάσας. | Note now says so ("left standing at the head of the sentence … takes them as its object in sense, and πάσας ‘all of them’ picks them up in the accusative"). |
| 108 | n | low | "ἀσμένῳ is the dative of ἅσμενος": the word is ἄσμενος, smooth breathing (the gloss entry has it right). | ἄσμενος. |
| 83 | n | low | "φύγεν is ἔφυγε, an unaugmented aorist": reads as if the augmented form were the unaugmented one. | "φύγεν is the aorist of φεύγω ‘escape’ without its augment (= ἔφυγε)". |
| 79 | l | low | The δέ of ἔπειτα δέ κεν was dropped in `l` ("then we could drag"); `i` has "and then". `l` renders δέ as "and" elsewhere. | "and then we could drag all the ships." |
| 13 | gloss (broaden κλισίης) | low | Old entry covers κλισίης after ἐκ, ἀπό, ἐγγύς, not after ἐκτός (ἐκτὸς κλισίης). | Added " · also fem. gen. sg. after ἐκτός: ’outside the hut’". |
| 107 | gloss (broaden μῆτιν) | low | The new reading glossed μῆτιν as ’a plan’, but this part's English (and the table) is "cunning"; ’plan’ is kept for βουλή. | ’cunning, counsel’. |
| 104 | gloss (broaden πώς), 62 (broaden τι) | low | Example translations not true to the lines: ’quite, I think, me’ (nothing in the Greek says "I think"); ’if … can do anything’ (ῥέξει is future, `l` "will do"). | ’very much, somehow, me’; ’if … will do anything’. |
| 101 | gloss ἀποπαπτανέουσιν | low | The note and new-renderings say the sense is not certain, but the glossary entry asserted it flatly. | Entry now has "(sense traditional)" as ἀλίαστον's does. |

## Gloss.json: checked and left as is

All 109 new entries: lemma, tense/mood/voice, number and the quoted English true of the line they stand in (spot points that might have been wrong and were not: εἰρύατο "plpf." with the alternative "were guarded"; ξύμβλητο/ξύμβληντο unaugmented; πῖνε kept as a homograph with the imperative second; ἀσκληπιάδην/μαχᾶον/θρασυμήδεος as printed forms; νυσσομένων as a loose genitive absolute, as the note says; κεκριμένον masc. acc. with οὖρον; ἐπικρατέουσί dat. pl. with Τρωσί). Of the 25 original broadens, each new reading is true of its line (αὐτούς/αὐτῶν 47, 56, 68; γένηται 98; γῆρας 86; εἴη 93, 107; κακόν 80; μάχεσθαι 51, 63; μάχην 57; μεθ’ 21; μὴ 46; νύκτα 80; οἷσιν 85; παλαιός 108; υἷος 9; ἀτειρὴς 25; ἀϋτῆς 37, 96; ἄγοιτο 91; ἐπ’ 77; ᾗ 67; ᾧ 55; πρώτας 31; πρῶται 75). Known forms whose old entry covers the use although it names another noun (θερμά, λαιψηρά, μακρόν, ἡμέτερον, σὴ, ἀέκοντας, with the same parse) were not broadened.

## Pass 2 findings considered and refused

1. 33 `l` "was able all / the beach to hold the ships" can be read "all the beach": already considered in pass 1 (Greek order and line division kept, the note says πάσας agrees with νῆας); refused again.
2. 107 μῆτιν `i` "who can tell of a better cunning": stiff, but bound by the table (pass 1, refused 4 and 107); unchanged.
3. 96 `i` "you who bid us drag" supplies "us" (the Greek has no pronoun with κέλεαι … ἑλκέμεν): the sense requires an understood subject for the infinitive and `l` leaves it out; refused as a change.
4. 24, 44 `l` renders the infinitives of the reported threat with "would he go back"/"he should set ablaze": a necessary finite frame in English for indirect speech after ἐπηπείλησεν; the pass-1 repair is accepted.
5. Known-form entries whose parse is right and whose "agreeing with X" example names another noun (see above): not broadened.

## For the caller (not changed by the reviewer)

- `new-renderings.md` has no row for ὄρχαμε λαῶν (14.102), a vocative that recurs and is not in the table ("chief of the people" in `l` and `i`, no avoided list given); consider adding one before step 4 copies the rows. The "Uses of existing table rows" paragraph still says ἅλα δῖαν "heavenly sea" (see pass 1, row 75–76: the shipped English is "heavenly brine"); not a row, nothing to copy.
- `packet.md` still shows the old `·` at 14.83 (derived file; pass 1 said so).
