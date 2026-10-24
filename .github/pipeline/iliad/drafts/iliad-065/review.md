# iliad-065 (Iliad 11.122–220) — reviewer, pass 1

Method: runbook section 2, "Reviewer", pass 1 only. Every grammatical label in every note checked against the form in its
line; every cross-reference looked up in the pinned source and in the published parts (`iliad-NNN.json`, `odyssey-NNN.json`
in the repository root); Greek to `l` word by word; `l` against `i`; remembered English; house table (Iliad and Odyssey)
for every stock word; quotation marks and `mark` against speech boundaries; every unit compared by `letters_only` with every
published Iliad and Odyssey unit (the validator's rule). The pinned source for 11.218 already ends in the raised dot (re-pinned
in commit e6f3c8253; sha of lines 122–220 matches `parts.json`), and the concatenation of the units' `t` equals lines 122–220
of the source (whitespace-normalised); `t` is untouched, byte for byte. No translation was opened or recalled.
`gloss.json` is being written elsewhere and was not read or touched. Scansion: none flagged, so none done.

Counts: 17 changes — 2 high, 7 medium, 8 low.

Severity: high = would fail the gate or mistranslates; medium = a false label or cross-reference, a house rendering not
honoured, an unsupported claim; low = polish, tightened wording, a missing cross-reference.

Unit positions below are by `ln` (the part has several units that share an `ln`; where that matters the first words of the unit are given).

## Changes

| # | line | field | sev | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 214 | l, i, n | high | The Greek (letters) equals the published unit at 6.106 (iliad-036, `οἳ δ’ ἐλελίχθησαν καὶ ἐναντίοι ἔσταν Ἀχαιῶν·`, a one-line unit), which the packet's list did not show (it gave only 5.497). The validator demands the same English, final stop included: that unit ends `Achaeans;` in both layers, the draft ended `Achaeans,` (gate would fail: "same Greek as iliad-036 line 106 but different English"). | Final stop changed to `;` in `l` and `i`; note now says the line is also 6.106 and that the English is kept with that stop. The `new-renderings.md` row rewritten to match. |
| 2 | 218 | l | high | The Greek equals the published unit at 2.484 (iliad-012 line 484; the source now ends the line with the raised dot). `i` already agreed (`…of Olympus:`), but `l` ended `Olympian halls` with no stop where the published `l` ends `Olympian halls;` (gate would fail). | `;` added to `l`. The `new-renderings.md` row (which still said "no stop printed" and gave a comma) rewritten. |
| 3 | 164 | l, i, n | med | κυδοιμοῦ rendered "tumult". The table fixes κυδοιμός as "uproar" (5.593, personified "Uproar"), and the shipped common-noun uses are "uproar" (10.523, iliad-063, both layers; 11.52, iliad-064, both layers). "Tumult" is on the table's avoided list for this word. | "uproar" in `l` and `i`; note says it is the same word and English as 10.523 and 11.52. `new-renderings.md` row rewritten. |
| 4 | 153 | l, i, n | med | δηϊόωντες rendered "ravaging" / "wreaking havoc". The table row for δηϊόω (4.416) fixes "cut down" in both layers, the same in active and passive, and lists "ravage" as avoided. The drafter's row had set "cutting down" aside as if it were kept for ἐναίρω/κτείνω, which the table does not say. | "cutting down with bronze" in `l` and `i`; note says "cut down" is the house rendering (4.416). `new-renderings.md` row rewritten. |
| 5 | 173 | l, i, n | med | νυκτὸς ἀμολγῷ rendered "in the dark of night" in both layers. The same words are published at Odyssey 4.841 (odyssey-021): `l` "in the dead of night", `i` "in the depths of the night", and the Odyssey glossary entry says "in the dead of night". The Iliad context (a lion at night) does not forbid it, and the departure was not recorded as one. | `l` "in the dead of night", `i` "in the depths of the night"; note says the English is the Odyssey's and the sense is a guess. `new-renderings.md` row rewritten. |
| 6 | 168 | l, n | med | κεκλήγων rendered "shouting" in `l`. The table (5.591) fixes `l` "shrieking" (`i` "with a shrill cry", which the draft has) and lists "shouting" as avoided (kept for ἄϋσε). | `l` "and he, shrieking, followed always,"; note adjusted and cites 5.591. |
| 7 | 161 | n | med | "the dative of the one they are dear to is understood from γύπεσσιν for the second half" is false of the line: ἀλόχοισιν is itself a dative in the line, set against γύπεσσιν; nothing is understood. | Note says both datives stand in the line (γύπεσσιν ‘to vultures’, ἀλόχοισιν ‘to wives’) with ἢ ‘than’. |
| 8 | 156 (second unit, `οἳ δέ τε θάμνοι`) | n | med | "the same noun as at 11.118": ὁρμῆς stands in 11.119 (11.118 is `καρπαλίμως δ’ ἤϊξε διὰ δρυμὰ πυκνὰ καὶ ὕλην`; the published unit iliad-064 starts at 118 but the word is in the second line). | `11.118` to `11.119`. |
| 9 | 211 | n | med | τεύχεσιν called "the dative plural of τεύχεα"; τεύχεα is the plural of τεῦχος, and τεύχεσιν is the dative plural of τεῦχος. | "the dative plural of τεῦχος (plural τεύχεα) ‘armour’". |
| 10 | 132 | n | low | "found in the Odyssey in the accusative": the very same line (nominative) stands at Odyssey 21.10 (odyssey-102), with the English the draft has; the accusative is 14.324 (odyssey-069). Half the truth. | "the same line stands at Odyssey 21.10, and the three nouns in the accusative at Odyssey 14.324". |
| 11 | 139 | n | low | ἀγγελίην called an "accusative of purpose"; it is the accusative of the errand (‘on a message’), with ἐλθόντα. | Label corrected. |
| 12 | 158 | n | low | Ἀτρεΐδῃ called "the epic dative"; it is the ordinary dative of Ἀτρεΐδης (Attic has the same form). Same kind of label as iliad-064 review no. 29. | "the dative of Ἀτρεΐδης (the same form in Attic)". |
| 13 | 179 | n | low | χερσί called "the epic dative plural"; χερσί is the ordinary dative plural of χείρ (the epic form would be χείρεσσι). | "with χερσί, the dative plural of χείρ". |
| 14 | 170 | n | low | The note said φηγόν is "an oak" while `l` and `i` say "the oak" (the published English at 6.237 and 9.354, iliad-038 and iliad-055). | "φηγόν is ‘oak’, and the English keeps ‘the oak’, the landmark by the gates, as at 6.237 and 9.354." |
| 15 | 187 | n | low | τόφρα glossed "for so long"; the units say "for that long". | "for that long". |
| 16 | 189 (first unit, `τόφρ’ ἀναχωρείτω`) | n | low | ἀναχωρείτω glossed "let him withdraw"; the table (4.305) gives "let him step back" and keeps "withdraw" out. | "let him step back". |
| 17 | 215 | n | low | "under the second of its three names": ambiguous and wrong against the convention (the order is Achaeans, Danaans, Argives, so Argives is the third; and Ἀχαιῶν stands in the line before). | "under the name Argives, after Ἀχαιῶν in the line before". |

`new-renderings.md` was edited only where it contradicted the shipped units (rows for 11.153, 11.164, 11.173, 11.214, 11.218), as iliad-064's review did for its οὔλιος row; the table must not receive the withdrawn wordings.

## Findings considered and refused

1. **11.122–123, topic accusatives (drafter's note).** Πείσανδρον τε καὶ Ἱππόλοχον and υἱέας are accusatives with no verb until 126, where τοῦ περ δὴ δύο παῖδε λάβε takes them up (the same two). `l` "But he — Peisander…" and `i` "As for Peisander and Hippolochus" say exactly this, and the note says so and why the unit stops mid-line. Kept. (μενεχάρμην is singular and goes with the nearer name, checked.)
2. **11.131 split into two units.** Whole-line identity with 6.46 (iliad-036 line 46) would force "Take me alive, … and you accept worthy ransom"; the speakers are two brothers (duals 129–130, νῶϊ 135), so `i` needs "us". The split at the comma leaves the second half with exactly the published English of 6.46 (checked: `l` and `i` identical, and the note says so) and the first half a recorded departure. Marks and quotes are right (“ on 131a, ” on 134/135; `mark` on the first unit). Kept.
3. **11.218 source ends with '·' and `i` ends with ':' like iliad-012.** Source and sha checked; the unit's `t` ends with the raised dot and matches the source. The only fault was `l` (no. 2 above). The LOG.md record of the rule-5 correction is not yet there (the run's job at the end).
4. **ἀμείλικτον "unsoftened" / "unyielding".** No published rendering of this word; the drafter's refusal of "ungentle/unrelenting" (the table's ἀμείλιχος 9.158, 9.572) is a fair separation of two different adjectives, and the contrast with μειλιχίοις in the same line is stated. Kept.
5. **ἐσσευε "sent … rolling" (not "made rush").** The table's ἔσσευα (5.208) has blood as object; here ἔσσευε governs an infinitive and the object is a man, so "made rush to be rolled" would be ungainly in `l`. Kept, recorded in `new-renderings.md`.
6. **ὅλμος "round block", ἀξύλῳ "dense", περὶ πρό "far ahead", γεφύρας "bridges", ἀάπτους.** Each is flagged in its note as not understood and as a guess; the γεφύρας and ἀάπτους renderings are the table's (8.378; "untouchable"/"irresistible"). The ὅλμος note says both "something round that rolls" and "not known": left, because the note then says "round block" is a guess. Kept.
7. **πεζοὶ … ἱππῆες "men on foot … horsemen".** Agrees with the table (2.810, 4.297–301); the avoided list (infantry, cavalry, charioteers) is right. Kept.
8. **σφεδανόν "furiously", ἀμολγῷ guess.** No published rendering of σφεδανός; "furiously" fits "impetuous" and the note says so. (ἀμολγῷ: see no. 5.)
9. **ἀπόρουσε "leapt down".** iliad-029 (5.297) ships "leapt down" in both layers for the same verb of a man leaving his chariot; the note states that the Greek does not say off the chariot. iliad-027 and iliad-035 have "away" for a different movement. Kept.
10. **πιδηέσσης "many-springed" / "with its many springs".** The table's πολυπίδακα (8.47) is a different word ("many-fountained" in `l`); no published rendering of πιδήεις. The drafter's note claims the table gives "of many springs" (true only for `i`); harmless, and the `l` literal of a different compound is a judgement call. Kept.
11. **ἐρινεόν "wild fig tree".** The table itself has both "wild fig-tree" (6.433) and "wild fig tree" (12.103); no rule to enforce. Kept.
12. **τεΐν in the note at 11.200** (the line prints τεῒν). Citation-form accent of the pronoun, not a misquotation. Kept.
13. **Quotation marks and `mark`.** Speeches: 131–135 (“ on 131a, ” at the end of 134/135), 138–142, 186–194, 200–209; every `mark` is on the first unit of a speech, no speech runs in from 11.121 or out of 11.220 (checked against iliad-064's end and the opening of 11.221). No change.
14. **Same-Greek checks.** Besides nos. 1 and 2: 11.199 equals the units at 2.790 (iliad-015) and 3.129 (iliad-017), English identical; 11.191–192 and 11.206–207 are one pair of identical units with identical English; 11.210–213 and 11.185 are parts of longer published units, so no rule applies and their English is kept as the notes say.
15. **Cross-references checked and found true:** 3.263 (ἔχον ὠκέας ἵππους); 8.378 (ἀνὰ πτολέμοιο γεφύρας); 2.790; 8.398; 8.425; 5.494–497; 2.484; Antenor's account of the embassy (3.205–207); 126/129–130 for Agamemnon (αὐτὰρ ὃ); 138 / 142; 143 / 145; 187–188 / 202–203; 189–190 / 204–205; 191–192 / 206–207; 194 / 209; ὁρμῆς (11.119, fixed); ἀνδροκτασίαι in the Odyssey (odyssey-056).

## For the glosser (second pass)

`gloss.json` was not read. When the second pass checks it, the renderings changed here matter for any gloss text that quotes the English: κυδοιμοῦ ‘uproar’ (not ‘tumult’), δηϊόωντες ‘cut down’ (not ‘ravage’), ἀμολγῷ ‘dead of night’ (the Odyssey's glossary entry already says so), κεκλήγων ‘shriek’.


# Pass 2 (gloss)

Scope: every novel entry and every `__broaden__` entry of `gloss.json` checked against the Greek of `units.json` (form by form, every place it occurs), against `known-forms.json` (old text must open each broadened entry) and `odyssey-forms.json`; all 481 distinct tokens of the units checked for coverage, and every known entry for a form used here read for a reading it lacks. `units.json` not touched. Entry format taken from runbook section 2 (conventions.md has no separate entry-format section): general to the form, no line numbers or ‘here’, typographic ’ only, under 230 characters (broadened entries only longer where the old entry already was), Attic equivalent for Homeric forms, homographs joined by ' · '.

Counts: 35 changes — 3 high, 10 medium, 22 low.

| # | key | sev | what was wrong / done |
|---|---|---|---|
| 1 | κυδοιμοῦ | high | ’tumult’ contradicts house rendering ’uproar’ (review pass 1 no. 3) |
| 2 | __broaden__ ὄχεα | high | FALSE: said neut. nom. pl. subject; ὄχεα is the accusative object of κροτάλιζον (horses rattled chariots) |
| 3 | __broaden__ ἕπετ (new) | high | MISSING: ἕπετ’ stands as the imperfect ἕπετο (followed), not the present ἕπεται, in two places |
| 4 | δύῃ | medium | parse kept (aor. subj. of δύω, true in both places); dropped the line-pinned "with τε and ἠέλιος as subject"; homograph with noun δύη named |
| 5 | μολὼν | medium | lemma was the infinitive μολεῖν; headword is βλώσκω; ’epic’ label dropped (μολών is also Attic poetic) |
| 6 | τυπεὶς | medium | false label ’epic’: τυπείς is the ordinary Attic aor. pass. participle |
| 7 | ἀμολγῷ | medium | English made to agree with units (depths of the night) and Odyssey entry; ’milking-time’ marked uncertain |
| 8 | ἀξύλῳ | medium | asserted etymology stated as fact; unit note calls it a guess |
| 9 | ἐφόβησε | medium | tense force: the aorist is gnomic and the unit says ’puts to flight’, not ’scared’ |
| 10 | ἱππεῖς | medium | dropped ’chariot-fighter’ (not the house sense; units say horsemen); added the epic form |
| 11 | ὅλμον | medium | ’boulder’ asserted a sense the unit note calls unknown |
| 12 | __broaden__ ἁπάντων | medium | new entry was 245 chars (>230 for an old entry under 230); shortened |
| 13 | __broaden__ δεδεγμένος (new) | medium | MISSING: old only gave ’waiting for’; here ’having accepted’ |
| 14 | αἰπὺς | low | example rendered ’sheer destruction’; units say ’steep’ |
| 15 | εἰλυφόων | low | gloss ’swirling’ to match unit English |
| 16 | εἴασχ | low | iterative force in the rendering |
| 17 | κόψας | low | gloss to match unit English ’striking off’ |
| 18 | μενεχάρμην | low | removed name-pinning (general to the form) |
| 19 | πεζοὶ | low | unit English ’men on foot’ (table avoids infantry-type words) |
| 20 | σφεδανὸν | low | unit English ’furiously’ (was ’hotly, headlong’) |
| 21 | ἀμείλικτον | low | gloss ’unrelenting, pitiless’ replaced by ’unyielding’ of the unit; kept apart from ἀμείλιχος |
| 22 | ἀνώχθω | low | unit English ’let him tell’ |
| 23 | ἐπειγόμενοι | low | unit English ’hard pressed’ (was ’driven on’) |
| 24 | ἐρίγδουποι | low | unit English ’loud-crashing’ |
| 25 | ἐριαύχενες | low | unit English ’strong-necked’ |
| 26 | ἐρινεὸν | low | unit English |
| 27 | ἔκπεσον | low | homograph form 1 sg. noted |
| 28 | ἔφεπε | low | unit English ’pursued’ |
| 29 | ὁρᾷ | low | noted identical indicative spelling; parse as subj. confirmed by ὄφρ’ ἂν … κεν |
| 30 | ὁρᾷς | low | same |
| 31 | ὑπόεικε | low | unit English ’give way from’ |
| 32 | __broaden__ παῖδε | low | example English to unit ’caught two sons’ |
| 33 | __broaden__ ἀεικέα | low | example to unit English ’unseemly insult’ |
| 34 | __broaden__ οἳ (new) | low | MISSING: οἳ … θάμνοι, article-like use |
| 35 | __broaden__ λώβην (new) | low | MISSING: object of τίσετε (paying), not giving |

## Glosser parsing choices scrutinised — all confirmed unless listed above

- ὁρᾷ / ὁρᾷς as pres. subj.: right (ὄφρ’ ἂν … κεν + subj.); the indicative has the same spelling, now said. The `κεν` broadening for ὄφρ’ ἂν … κεν is right.
- ἐστόν 2 dual: right (υἱέες ἐστόν, ‘you two are’); the entry already says 3 dual has the same spelling.
- ἐξέμεν aor. inf. of ἐξίημι (= Attic ἐξεῖναι): right (ἕμεν is the aorist infinitive; the pres. is ἱέμεναι).
- κείν’ = κενός (κεινά): right; the acute on the elided syllable excludes κεῖνα ‘those’.
- μολών: parse right; lemma changed to βλώσκω (see above).
- δύῃ verb: right (aor. subj. of δύω coordinated with ἀφίκηται/ἀφίκηαι). The Odyssey has δύῃ as the dative of δύη ‘woe’ (odyssey-forms.json), a different word not occurring in this part; the entry names it in parentheses rather than carrying a reading that does not occur here.

## Findings considered and refused

1. **Adding the Odyssey noun reading δύῃ (δύη ‘woe’, dat.) as a joined homograph.** The reading does not occur in this part; entries parse the form where it occurs. Named in parentheses only.
2. **δόμοις (132), old entry.** Its two readings speak of ἐν after or before the noun in ways that do not fit ἐν Ἀντιμάχοιο δόμοις exactly, but the first reading (plural for one dwelling) is true of the word; not rewritten (the runbook forbids rewriting old entries; the form is covered).
3. **Examples with Greek quotations in entries (αἰπὺς, νυκτὸς, παῖδε …).** These are usage examples, not line numbers or ‘here’; kept.
4. **ἀνδροκτασίης, ἀντιμάχοιο, πείσανδρον ‘a son of Antimachus’, κεκλήγων, πεζοὺς ‘foot-soldiers’ (old entry).** Parse true; the old πεζοὺς gloss is left as it stands (never rewrite an existing entry).
5. **ἐνίσπες, ἐγγυαλίξω, ἐλθόντα, ἐφέβοντο, ἔγκατα, ἔλθῃ, ὄλεκον, ὦρσαν, θῦεν, κείατο.** Compared with the Odyssey entries; this part's use fits each; kept as written.
6. **κεκλήγων / ὄπα / σιγαλόεντα / ἀάπτους (old entries).** Cover this part's use and the units' English (‘shrieking’ in the old entry, ‘shriek’ in the unit is the same word); no change.
7. **ἁπάντων, ὥς, κεν, μηδ.** Broadened entries parse true in every place; only ἁπάντων and λώβην needed shortening (under 230).
