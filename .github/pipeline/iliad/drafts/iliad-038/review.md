# iliad-038 review (6.232–331), pass 1

Scope of pass 1: every grammatical label and cross-reference in every note against the line; Greek to `l` word by word; `l` and `i` agreement; remembered English; quotation marks (marks at 254, 264, 305, 326 present; closing marks at 262, 285, 310, 331 present; 331 ends Hector’s speech, so nothing runs into the next part); reuse of published English (6.253, 6.274–276, 6.278, 6.294, 6.295, 6.310, 6.325 compared with iliad-036, iliad-016, odyssey-072, odyssey-076: units at 274, 295 and 325 are identical in `t`, `l`, `i` to the published ones). No packet-flagged lines (none flagged). `t` untouched (checked byte for byte). Gloss.json is for pass 2.

## Changes (line · field · severity · what was wrong · what done)

1. 6.234 · n · medium · called ἑκατόμβοι’ ἐννεαβοίων "two neuter adjectives"; ἐννεαβοίων is a genitive plural, not neuter · rewrote: neuter plural ἑκατόμβοι(α) against genitive plural ἐννεαβοίων.
2. 6.264 · i · low · "and I forget my might" turned the subjunctive of fear (λάθωμαι, under "or you may …") into an indicative · now "and I may forget my might". Row for ἀπογυιώσῃς in new-renderings.md updated to match.
3. 6.267 · i · low · `i` "right" against `l` and note "possible" (ἔστι with infinitive) · `i` now "nor is it in any way possible …".
4. 6.271 · l · low · "that lay on the knees" reads as a past relative clause; Greek is imperative τὸν θές · `l` now "that one lay on the knees" (matches the note).
5. 6.277 · n · low · cross-reference "fixed at 6.96" · the shared line is 6.97, in the published unit 6.96–97; now "6.96–97".
6. 6.279 · i · low · "in case he will listen" (a fear/precaution sense) for αἴ κ’ ἐθέλῃσ’ "if he is willing" (and `l` "if") · now "if he will listen when I speak".
7. 6.284 · n · medium · called ἐκλελαθέσθαι a "perfect infinitive"; it is the reduplicated aorist infinitive · corrected.
8. 6.289 · n · low · said ἀνήγαγεν is "led up" while `l` and the row give "led away" · note now "‘led away’ (ἀνάγω ‘lead up’ is the verb for taking someone out to sea)".
9. 6.305 · i · low · ἠδὲ καὶ αὐτόν "and himself too" lost its "too" in `i` · "and grant that he himself also fall headlong".
10. 6.326 · l · medium · `l` "not at all fair" against the house rule that plain καλά is "fine" in both layers (Odyssey table; and the new-renderings row itself says "fine", not "fair") · `l` now "not at all fine"; row updated.
11. 6.329 · i · low · optative ἴδοις rendered "saw" while `l` says "might see" · `i` now "whomever you might see".

Severity count: high 0, medium 3, low 8.

## Considered and refused

- 6.250/6.246 μνηστῇς "wedded" in `l`: μνηστός is "wooed" (note says so); "wedded wives" is the table row (new-renderings) and fits the sense. Kept.
- 6.261 `i` turns dative ἀνδρὶ κεκμηῶτι into the possessive "a weary man’s great might": same sense, natural English. Kept.
- 6.255 note "opens her answer to her own question": Hecuba does answer her question at once (ἦ μάλα δή); label true. Kept.
- 6.291 περ glossed "also": acceptable for the emphatic "the very voyage on which he also …". Kept.
- 6.268 `i` "spattered with blood and gore" vs Greek πεπαλαγμένον with the datives: agrees with the row and the note. Kept.
- 6.230s ἵππων "horses" in `l`, "chariots" in `i`: the note says so. Kept.
- 6.297 note `ἐν πόλει ἄκρῃ` "citadel": standard sense, kept.
- 6.282 ἐκ τοῖο "his": note’s "old genitive of the article used as ‘his’" is true of τοῖο here. Kept.
- 6.305 `l` and `i` omit δή ("now") in `i`: particle with no English force here. Kept.
- 6.308 `i` omits νῦν ("now"): αὐτίκα νῦν is "at once now", an intensive pair; `i` "at once" carries it. Kept.
- 6.293 note "a robe of Helen’s" for the Odyssey line: true (Od. 15.105–108). Kept.
- Remembered English: no phrase in `i` arrived whole from a known translation; "lady mother", "Strange man", "city-guarding" etc. are house renderings.

# Pass 2 (glosser and parses)

Scope: every parse in gloss.json (161 entries: case, number, tense, mood, voice, lemma, meaning, Attic equivalent) read against its line; the 19 `__broaden__` entries checked as old entry whole (from iliad-glossary.json) + ` · ` + a new reading that occurs in 6.232–331; entry length, ’ only, no line numbers, no ‘here’; a second look at units.json (labels in notes, `l` against `i`). `t` untouched. The six flagged conjectures: θέρηται (pres. subj. mid., fear clause, 6.331, LSJ θέρομαι ‘be heated, burnt’) confirmed; ἀτέρπου (LSJ ἄτερπος = ἀτερπής, cited for 6.285, agrees with ὀϊζύος) confirmed; ἐπιπλὼς (root-aorist participle of ἐπιπλέω, Attic ἐπιπλεύσας) confirmed; ἐξέλετο (= Attic ἐξείλετο, dative of the person deprived) confirmed; ἕν (elided ἕν’ = ἕνα, 6.293) confirmed; ἀμφιδέδηε lemma and sense confirmed, Attic equivalent wrongly given (below); δεδμημένοι homograph resolved (below).

## Changes

1. δεδμημένοι · gloss · medium · second reading ‘also δάμνημι … overpowered’ does not occur in this part (both uses, 6.244 and 6.248, are ‘built’, δέμω) · entry now the δέμω reading only. The Odyssey entry for the form is the other verb; this glossary is separate.
2. κατεβήσετο · gloss · medium · called ‘unaugmented (= κατέβη)’; the form has the augment (κατ-ε-βήσετο), it is the epic sigmatic middle aorist · corrected.
3. ἀμφιδέδηε · gloss · low · ‘epic δέδηε (= Attic δέδηεν)’ is only movable ν, not an Attic equivalent · now ‘perf. 3 sg. act., present sense (perf. of δαίω)’.
4. χαλκείων · gloss · low · ‘Ionic -είων (= Attic χαλκῶν)’: χάλκειος is ordinary Greek and the form needs no equivalent · removed.
5. δῖα (broaden) · gloss · low · new reading said ‘nom. sg., in apposition to the one addressed’; at 6.305 it is a vocative · now ‘fem. voc. sg., in address’.
6. 6.300 · n · low · ‘explains why Theano holds the keys’: keys are not in this part · now ‘is the one who opens the doors’.

Severity count: high 0, medium 2, low 4.

## Checked and left

- All other 155 parses and the other 18 broaden entries agree with their lines (new readings occur at 6.327, 247, 291, 302, 264, 321, 328, 305, 256, 292, 277, 253, 267, 329, 258/281).
- κατελθόντ, ἐκλελαθέσθαι, εἰρόμεναι (pres., Ep. of ἐρωτάω/ἔρομαι), ἱερεύσομεν (subj. or fut.), ὅς at 6.293 (relative, antecedent πέπλος): correct.
- 6.287 ‘the verb of the order at 270’ for the participle ἀολλίσσασα: same verb, kept.
- Article-forms (αἱ, τῇσι, θὲς) are glossed as pronouns; no possessive ὅς occurs in this part.
- Notes all under ~110 words, no backticks, no unit-note line-number or mid-line claims found wrong; `l` and `i` agree throughout (pass-1 fixes confirmed).
