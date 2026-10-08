# Review — odyssey-103 (Odyssey 21.101–206), pass one

Edited `units.json` in place by script; `t` untouched (checked: all 60 `t` identical before and after). Lines are cited by `ln` of the unit. Severity: high = a wrong claim of fact about the Greek or a layer contradicting the Greek or the other layer; medium = a false grammatical label, false location claim, or a note contradicting `l`/`i`; low = wording, force or consistency.

## Changes

| line | field | sev | what was wrong | what was done |
|---|---|---|---|---|
| 131 | `l` | high | `l` read as a statement ("Truly even hereafter … shall I be"), `i` as a double question, and the note itself says ἦ … ἠέ is a double question; the layers disagreed in force. | `l` now a question ("Is it that even hereafter …?"), keeping the line division; note adds that both layers end with a question mark. |
| 203 | `n` | high | Note called ὅνδε "the accusative of ὅδε ‘this’", "to this house, the house where they stand": a false label (the accusative of ὅδε is τόνδε; ὅνδε is possessive ὅς + -δε, as the glossary already has it) and it contradicted the `l`/`i` "his own house". | Note now: possessive ὅν ‘his own’ + -δε, "to his own house", second line shipped. |
| 128 | `n` | medium | ἐτάνυσσε called an imperfect ("an imperfect with κε"); it is an aorist (glossary: aor.). | Reworded to aorist with κε. |
| 167 | `n` | medium | ἐνένιπεν called an imperfect; it is the reduplicated second aorist (glossary and 21.84’s note say aorist). | "reduplicated second aorist". |
| 159 | `n` | medium | πειρήσεται called "a future" beside the subjunctive ἴδηται after ἐπήν; a future indicative does not stand after ἐπήν. | "has the form of a future; after ἐπήν best taken as a short-vowel aorist subjunctive". Glosser: the existing entry for πειρήσεται says "fut. mid. 3 sg."; broaden with "· also short-vowel aor. subj." if gloss.json is made. |
| 134 | `n` | medium | ἐκτελέωμεν called an aorist subjunctive; the form is from the present stem of ἐκτελέω (aorist would be ἐκτελέσωμεν). | "a subjunctive of exhortation" (tense not asserted). |
| 122 | `n` | medium | "στῆσε … same verb as στῆσεν two lines before": στῆσεν is at 120, στῆσε at 123, three lines. | "three lines before, at 120". |
| 140 | `n` | medium | Claimed the patronymic is "the fixed way of naming Antinous when he speaks"; 21.167 in this very part has none, and a note may not generalise beyond what the part shows. | "a stock addition to his name in this introduction". |
| 150 | `l`, `n` | medium | `l` "he wearied his hands" (direct object) against the note’s "accusative of respect: he tired in the hands" and `i` "his hands grew weary". | `l` "he grew weary in his hands"; note wording matched. |
| 153 | `n` | medium | "ἁμαρτεῖν … with the genitive οὗ in οὗθ’ ἕνεκ’": οὗ is the relative governed by ἕνεκα, not a genitive after ἁμαρτεῖν. | Rewritten: οὗθ’ ἕνεκ’ stands for οὗ ἕνεκα, relative clause with the thing missed unstated. |
| 102 | `n` | medium | "ὢ πόποι, with the circumflex": the printed ὢ is grave (an acute before another word), not circumflex. | Corrected; still says it is not the circumflex ὦ of address. |
| 168 | `mark` | low | "Antinous speaks" repeated the mark of 141 and was not distinguished from his order at 176. | "Antinous answers Leiodes" (176 keeps "Antinous speaks again"). |
| 203 | `l` | low | "And so in the same way": the table (20.238) has "So in the same way"; the δέ is not carried there. | "So in the same way Eumaeus prayed …" (new-renderings.md row corrected too). |
| 111 | `i` | low | δηρόν "for long" lost ("any longer" translates only ἔτι). | "for much longer" (covers μηδ’ ἔτι δηρόν); note adds the phrase. |
| 111 | `n` | low | "τανύω, which in turn takes τόξου": it is the noun τανυστύς that has τόξου depending on it. | Reworded. |
| 113 | `n` | low | "τοῦ is … ‘that bow there’" against `l`/`i` "the bow". | "close to its old demonstrative force, ‘the bow in question’". |
| 136 | `n` | low | "datives in -ῃσιν and -εσσιν": ἐϋξέστῃς has the short ending -ῃς. | Added. |
| 153 | `i` | low | "many of our best men" adds "our" and a partitive the Greek does not have. | "many of the best men". |
| 175 | `n` | low | "Homer’s fixed way of naming the man": a claim beyond the part. | "a stock way". |
| 176 | `n` | low | στέατος called a partitive genitive although it is governed by ἐκ in tmesis; ἐόντος’ agreement (with στέατος, not τροχόν) left unsaid and `l` "wheel, that is within" is ambiguous. | "genitive of source"; note says ἐόντος agrees with στέατος. |
| 194 | `n` | low | ἀνώγει called "a perfect"; it is the present-sense form built on the perfect (glossary says so). | Reworded. |
| 200 | `n` | low | "‘that he may come … and lead him’" gives δαίμων’s clause the wrong subject. | "and that a power may lead him". |
| 205 | `n` | low | "here ‘true’" while `l`/`i` and the table keep "unerring". | Removed. |

Counts (table rows): high 2, medium 9, low 12.

## Open points resolved

1. **21.167 "rebuked them"**: kept. The validator forces the 21.84 English for a whole-unit repeat; the note already says the Greek has no object and that only Leiodes is rebuked. Recorded in new-renderings.md note 1. If the owner wants "him", 21.84 (odyssey-102) and its table row must change together.
2. **21.204 "to his own house" / "his own home"**: kept (follows the shipped 1.82 and 20.239 and the glossary entry for ὅνδε). The 20.329 table row ("to this house", "to his own house" avoided) conflicts with that and, in the draft’s note, was the source of a false label; the unit’s note was corrected, and new-renderings.md note 2 records the conflict for the owner. The 20.329 row is not touched here.

## Considered and refused

- Unit at 110 `i` omits καὶ δέ "and indeed": force is carried by "well enough"; no change.
- 21.171 (unit at 168) `l`/`i` "you yourself" for σύ: emphatic pronoun, "yourself" slightly over-reads αὐτός but is idiomatic and consistent in both layers; no change.
- Unit at 187 note "close to those used of the same two men elsewhere": the packet shows this half-line is shipped (odyssey-019), so the claim is demonstrable; no change.
- Unit at 106 note "line Penelope used at 21.73": checked against odyssey-102 (ln 73, Penelope speaking); true.
- Unit at 131 reading ἦ … ἠέ as double question although Murray ends with a full stop: kept, now in `l` too (see above).
- Unit at 153 οὗθ’ form (not obtainable from οὗ + ἕνεκα by elision): transmitted as printed; not mentioned in the note beyond "stands for".
- Unit at 198 κελεύει "order" (l) / "urge" (i): intentional, per the new-renderings row.
- Unit at 184 (first) `i` "warmed the bow": supplied object is stated in the note.
- Table rows checked against the units: ἕρκος ὀδόντων, πότνια μήτηρ, θεοειδής, δῖος, θεῖος, πολύφρων, μνηστῆρες ἀγαυοί, ἀκάματον πῦρ, μειλιχίοισι, αἰπόλος αἰγῶν, ὣς φάτο, ἐπιβουκόλος, δαίμων, ἀνώγει, νημερτής, ἔπεσσιν ἀμειβόμενος προσέειπεν: all agree.
- Quotation marks: “ in `l` and `i` on the units at 102, 131, 141, 152, 168, 176, 193, 200 (first unit of each speech, each with `mark`) and ” on the units at 114, 134, 141, 161, 174, 179, 198, 202; no speech is open at the end of the part (205 introduces a speech that opens the next part, as its note says). Checked.
- Scansion: no flags in the packet; rescanned all 106 lines, only "spondaic fifth" (113, 121, 124, 147, 149, 160, 189, 193), an ordinary hexameter licence; no note needed.
- gloss.json does not yet exist; the parse check of pass two should include the πειρήσεται, ἐνένιπεν, ἐτάνυσσε, ἀνώγει and ὅνδε points above.

---

# Pass two (units.json re-read against the Greek; every gloss.json entry parsed against its lines)

Edited `units.json` and `gloss.json` in place by script; `t` untouched (all 60 `t` identical before and after). Severity scale as in pass one.

## Changes

| line / form | field | sev | what was wrong | what was done |
|---|---|---|---|---|
| νημερτέ’ (205) | gloss.json | medium | Parsed "neut. acc. pl. (= νημερτέα), adverbial: truly, unerringly", but it agrees with the masc. sg. νόον (νημερτέα is the masc. acc. sg. of the -ής adjective); the unit's own note and `i` ("their unerring minds") take it as an adjective. | Entry now: masc. acc. sg., elided (νημερτέ’ = νημερτέα): ’unerring’. |
| ὅνδε (204) | gloss.json `__broaden__` | medium | The broadening added "’this his own’; the sense ’to’ lies in δόμονδε", a second reading that contradicts the unit's note and `l`/`i` ("his own house"); the existing entry already covers ὅνδε δόμονδε exactly, so no broadening was needed. | Removed the `__broaden__` entry for ὅνδε. |
| ἔνεικε (178, 183) | gloss.json `__broaden__` | medium | Missing broadening: the known entry gives only "aor. 3 sg." (indicative), but at 178 ἔνεικε is the aorist imperative (the note at 181 says so). | Added: old entry whole + " · also aor. imper. 2 sg.: ’bring!’ (ἐκ … ἔνεικε ’bring out!’)". |
| αἴνου (110) | gloss.json | low | Gave "tale, story, talk" only; the unit's note and `l`/`i` use the sense ’praise’. | "αἶνος — tale, story, praise; masc. gen. sg." |
| οἴνοπος (144) | gloss.json | low | "epic Οἴνοπος" implied a Homeric by-form; Οἴνοπος is simply the regular genitive of Οἴνοψ. | "masc. gen. sg. (Οἴνοπος)". |
| 134 | `n` | low | "comparative of πρόφερος": no such adjective; the lemma (and the gloss) is προφερής. | "comparative of προφερής". |
| 172 | `n` | low | "the sense is ‘archer’" stated flatly, while the glossary (rightly) records the sense of ῥυτήρ as disputed (‘protector’ elsewhere). | "the sense is taken here as ‘archer’". |
| 190 | `n` | low | "μετά with the accusative means ‘in pursuit of’": over-reads μετὰ τοὺς … ἤλυθε (the glossary has ‘after’). | "means ‘after’ here". |
| new-renderings.md, Ζεῦ πάτερ row | `l` column | low | Row said "Zeus father, would that …"; the unit (and shipped 'Father Zeus') has "Father Zeus, would that …". Would have entered the table wrong. | Row corrected to "Father Zeus, …". |
| new-renderings.md, νεμεσσάω row | `i` column | low | Row said "I resent"; the unit's `i` at 169 is "I am resentful". | Row corrected. |

Counts of pass-two changes: high 0, medium 3, low 7.

## Checked and found correct (no change)

- Every other novel entry (about 95) parsed against each line where the form occurs: lemma, meaning, case, number, tense, mood, voice, person. All under 230 characters, typographic ’ only, no line numbers, no "here", none pinned to a line. Digits in entries are person numbers (1 sg. etc.), not line numbers.
- The other 12 broadenings: each is the known entry whole (checked by string prefix against known-forms.json) + " · " + one new reading, and each new reading is true of the line cited (αὐτὸν 196, βίης 185, θέτ’ 119, κε 162, οἴῳ 146, οἷόν 173, πειρήσεται 159, τίθει 177, τανύσσαι 171, χώρου 142, ἀνέγνω 205, ἄρ 166, ὅτ’ 116, ῥυτῆρα 173). The pass-one point on πειρήσεται is carried out.
- Known forms read against the part (411 keys; all 411 tokens covered, no form missing from novel or known): the only gap found was ἔνεικε. In particular the existing entries already cover πρὶν (150 ’before that, sooner’), αὐτῆς (109 ’Ithaca itself’), τῷ (184 ’therefore, and so’), τοί (172 particle), ἔλθοι (162 relative with κε), ἦ (194, 197 ’or’), ὅτε (133 subj., general), τὸ τέταρτον (128), τοῦ (113, 142 article-like).
- Units: re-read all 60 against the Greek. Labels in notes, l/i, speech marks (“ on the first unit and ” on the last of each of the 8 speeches, in both `l` and `i`; `mark` on each first unit), `p` flags (all 15 ¶ lines), whole-unit and part-line repeats against the packet (101, 106, 130, 133, 139, 140, 143, 162, 166, 167, 187, 199, 201, 202, 204: wording identical or consistently reused), cross-references (21.73, 21.84 "two men", 21.96–97, 133 from odyssey-077, 138, 203) all verified against the published parts. No further errors.

## Findings considered and refused

- ἷζε (145) is recorded as "aor. 3 sg., ’sat down’"; here the sense is a habitual ’sat’ and the form could equally be taken as imperfect. The headword and the form-class are not wrong, only the gloss ’sat down’ is a little narrow; not broadened.
- βίης (126, after μεθῆκε): the existing "gen. of separation with σχέσθαι" covers it; no extra reading added.
- ὅπως (198, + pres. indic., indirect question): the existing entry (’how’ after a verb of telling; + pres. indic. ’in whatever way’) covers it closely enough.
- ὤμοιϊν (118): the glossary calls it dual, the unit's note says only "epic form … old ending -οιϊν"; not contradictory, so left.
- Unit at 198, `l` "Tell me how …" adds "me" that the Greek lacks: the supplied indirect object is natural and the new-renderings row records it on purpose; no change.
- Unit at 131: ἦ … ἠέ as a double question although Murray has a full stop: stays as pass one decided.
- Unit at 125 note "repeat those of 21.96–97": checked, true (odyssey-102 ln 96).
- ὁμαρτήσαντες, θυοσκόος and the other "rare word" entries: meanings are glossed as the lexica give them, and the uncertain ones say so; no change.
