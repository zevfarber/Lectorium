# odyssey-089 (Odyssey 18.108–214) — Review

## Pass 1

Reviewer, pass 1 of 2 (`units.json` only; `gloss.json` was being written concurrently and is left for pass 2). Method: runbook section 2 order. (1) Every grammatical label, word-position claim and cross-reference in every note against the form and the line; the cross-references were looked up in `source/odyssey-murray1919.json` (13.437–438, 17.197–198, 17.466, 4.793–795, 8.18–20, 1.332–334, 16.414–416, 1.366, 2.382, 2.393, 18.44–45, 18.85, 18.172, 5.215–217, 8.169). (2) Greek to `l` word by word. (3) `l` against `i` in sense and force. (4) Remembered English in `i`. (5) Quotation marks and `mark`. (6) The whole of `conventions.md` read (house table to its last row, including the rows appended after the Scansion header), then every row whose Greek shares a word with a unit looked up, with its "avoided" column set against the unit's `l` and `i` by script; every repeated line or half-line compared with the published English in odyssey-001 to 088 (identical-`t` units compared by script: units 108, 109, 124, 169, 177, 208–210 and 211 agree with the published `l` and `i` word for word). `new-renderings.md` checked against the English in `units.json`. `t` was never touched: all 64 `t` strings are byte-identical before and after (checked by script) and still join to the packet's 107 lines. No modern translation was opened or recalled; the aids were the house table, the published parts, the source text and LSJ/Autenrieth/Cunliffe/Monro/Smyth-level knowledge.

Checks that passed with no change: `ln` of every unit; `p` on the first unit of each of Murray's 14 paragraphs (108, 112, 117, 122, 124, 151, 158, 164, 169, 177, 185, 187, 201, 206) and on no other unit; `v` on every unit; one `\n` in `l` for each `\n` in `t`; no `\n` in `i`; no ASCII quotes or backticks in any `l`, `i` or `n`; unit boundaries (every unit ends at a full stop, question mark or ano teleia, except unit 32, which ends at a comma because the sentence 158–162 is five lines long, and the note says so); `title`, `titleEn` and `part` with the cite exactly as in `parts.json` (18.108–214).

Speech marks. Checked against `drafts/odyssey-088/units.json`: its last unit (18.105–107, Odysseus to Irus) closes its speech with ” and the next source line, 18.108, is narrator (ἦ ῥα καὶ ἀμφ’ ὤμοισιν …), so no speech runs into this part. Here there are seven speeches: units 4–5 (the suitors, 112–116), 9–10 (Amphinomus, 122–123), 12–25 (Odysseus, 125–150), 35–36 (Penelope, 164–168), 38–41 (Eurynome, 170–176), 43–47 (Penelope, 178–184) and 56–57 (Penelope, 201–205). Each has “ on its first unit and ” on its last unit in both `l` and `i` (no stray mark inside any speech), and a `mark` on its first unit and on no other unit, in the wording odyssey-088 uses (“The suitors speak”, “Odysseus answers”, “Penelope speaks”). The part ends at 18.214, the introduction of Telemachus’s address (ἡ δ’ αὖ Τηλέμαχον προσεφώνεεν); the speech begins at 18.215 in the next part, so unit 63 correctly carries no “.

Scansion flags: none in the packet, so no line was scanned by hand and no metrical sentence was added to any note.

Repeated lines. Whole-unit repeats (108, 109, 124, 169, 177, 208–210, 211) agree with the published English in both layers. Line 189 agrees with odyssey-021.794, 207 with odyssey-004.330, 213 with odyssey-004.365, 116 with odyssey-088.83, 159 with odyssey-087.561, 110a with odyssey-086.466; 112 was brought into line with odyssey-066.53 (change 6 below).

### Changes

Line is the unit's `ln`; where two units share a line the first words are given.

| # | Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 132 | n | high | ὄφρα … παρέχωσι called an aorist subjunctive. παρέχωσι is the present subjunctive of παρέχω (the aorist would be παράσχωσι). | ‘takes the present subjunctive παρέχωσι ‘furnish’ (παρέχω) with no ἄν’. |
| 2 | 175 | n | high | ἠρῶ called the contracted aorist middle of ἀράομαι. It is the imperfect 2 sg. (ἠράου → ἠρῶ); the aorist is ἠρησάμην (cf. ἠρήσαντο at 213, which the note at 212 labels correctly). | ‘the contracted imperfect middle of ἀράομαι ‘pray’ (ἠράου, 2 sg.)’. |
| 3 | 170 | n | high | ἔειπες said to have ‘the epic reduplication’. It is the augmented aorist of εἶπον with the augment left unfused (root Ϝειπ-), as the notes of earlier parts say; there is no reduplication. | ‘the aorist of εἶπον with the augment left unfused with the root’s first vowel (Attic εἶπες)’. |
| 4 | 188 (κούρῃ Ἰκαρίοιο) | n | high | Cross-reference false: ‘4.794, where Athena also lays Penelope in sleep’. At 4.793–794 sleep comes on Penelope of itself (ἐπήλυθε νήδυμος ὕπνος); Athena acts at 4.795 by sending a phantom. | Now: sleep falls on Penelope as she lies thinking of her son, it is not Athena who sends it there, and the Athena formula ἔνθ’ αὖτ’ ἄλλ’ ἐνόησε follows at 4.795. |
| 5 | 130 | l, i, n | medium | ἀκιδνότερον rendered ‘frailer’. The same word already ships as ‘slighter’ in both layers at 5.217 (odyssey-024, ἀκιδνοτέρη) and 8.169 (odyssey-034, ἀκιδνότερος); the new-renderings row presented ‘frailer’ as a new choice without noticing this (the shipped note there glosses the word ‘slight, feeble, of little account’). One Greek word, one English. | l ‘Nothing slighter does the earth nourish than man’; i ‘The earth nourishes nothing slighter than man’; the note says ‘slighter’ is the rendering already used at 5.217 and 8.169. The `new-renderings.md` row was rewritten to match (see Other findings). |
| 6 | 112 | i, n | medium | Line 112 and the first half of 113 (ὅττι μάλιστ’ ἐθέλεις) already ship (odyssey-066.51–53) as ‘what you most wish’; the draft’s `i` had ‘whatever you most wish, and whatever is dear to your heart’, departing from the packet’s English where the sentence allows the published wording. | i ‘… what you most wish, and what is dear to your heart’; the note now glosses ὅττι as ‘what’ (‘whatever’). `l` already matched. |
| 7 | 195 | n | medium | ‘The first line has the same words as 8.20’: it does not. 8.20 has the masculine μακρότερον, here the feminine μακροτέρην. Also ‘makes Odysseus greater’ is not what 8.19–20 says (taller and stouter), and the comparatives were all called ‘feminine’, though πάσσονα is not a feminine form. | ‘is 8.20 … except that the adjective there is the masculine μακρότερον’, ‘taller and stouter’; the comparatives are said to agree with μιν, the first and third being feminine forms. |
| 8 | 182 | n | medium | Note attached μοι to ἐλθέμεν (‘to me’), `i` agrees (‘come to me’), but `l` has ‘But for me … bid’; the note contradicted its own `l`. The Greek allows both. | Note now says μοι can go with the bidding, ‘for me’, as in `l`, or with ‘come’, ‘to me’, as in `i`. |
| 9 | 202 (αἴθε μοι ὣς …) | n | medium | ‘ποθέουσα … takes the genitive πόσιος ‘husband’ and the accusative of respect παντοίην ἀρετήν’ states one construction as the only one; ποθέω takes the accusative and πόσιος … φίλοιο can depend on ἀρετήν (‘every excellence of my dear husband’). `l`/`i` follow the first reading. | Note now gives both readings and says which one `l` and `i` take. |
| 10 | 146 (ἀλλά σε δαίμων) | l | low | δαίμων: the house row (6.172) fixes `l` ‘a power’, `i` ‘some power’; `l` had ‘some power’. | l ‘But may a power you’. |
| 11 | 201 | l, n | low | μάλ’ in ἦ με μάλ’ αἰνοπαθῆ not rendered in `l` and not mentioned in the note (it goes with αἰνοπαθῆ). | l ‘Truly, me, very fearsomely suffering, …’; note adds ‘μάλα ‘very’ goes with αἰνοπαθῆ’. |
| 12 | 143 | i | low | οὐκέτι δηρόν ‘no longer for long’ (l) became ‘will not be long away’, dropping οὐκέτι. | ‘… will not be away from his dear ones and his fatherland much longer’. |
| 13 | 143 | n | low | οἷ’ glossed ‘as, how’ where `l` has ‘Such things’. | ‘οἷα, ‘such things as’’. |
| 14 | 149 | i | low | γάρ at the head of οὐ γὰρ ἀναιμωτί … dropped from `i` (`l` has ‘For’). | i ‘For I do not think the suitors and he will part …’. |
| 15 | 155 (ἀλλ’ οὐδ’ ὣς φύγε κῆρα) | n | low | ‘the next line says why he could not escape’: the reason begins in the same line, after the ano teleia (πέδησε δὲ καὶ τὸν Ἀθήνη). | ‘the rest of the sentence says why he could not escape’. |
| 16 | 155 (πέδησε δὲ καὶ τὸν) | l | low | `l` ‘for Athena bound him too’ renders δέ as ‘for’; `l` keeps the Greek connective (the explanatory force is left to `i`, which has ‘for’). | l ‘and Athena bound him too’. |
| 17 | 138 (πατρί τ’ ἐμῷ) | l | low | ‘to my own father’: ἐμῷ is plain ‘my’ and `i` has ‘my father’. | l ‘to my father trusting, and to my brothers’. |
| 18 | 171 | l | low | σῷ παιδί rendered ‘your own son’; σός is plain ‘your’ (the note says ‘your’; the previous unit’s παιδί is ‘my son’). | l ‘and to your son speak the word’. |
| 19 | 171 | n | low | ‘washed off her skin’ in a note on a verb addressed to ‘you’ (`l` ‘your skin’). | ‘washed off your skin’. |
| 20 | 187 | n | low | ‘also at 2.382 and 2.393’ left out the nearest parallel, 4.795 (the same line, in the part that also has Athena and Penelope asleep). | ‘also at 2.382, 2.393 and 4.795’. |
| 21 | 110 (τοὶ δ’ ἴσαν εἴσω) | n | low | ‘the colon that opens their speech’: the printed mark is an ano teleia (the English has the colon). | ‘the ano teleia that opens their speech’. |
| 22 | 214 | n | low | ‘The speech itself comes after the colon, in the next line’: the speech is not in the next line but in the next part (18.215), and the mark is an ano teleia. | ‘The speech itself begins in the next part, at 18.215, after the ano teleia.’ |
| 23 | 206 | n | low | ὑπερώϊα explained only as a plural noun; `l` ‘came down the upper rooms’ and `i` ‘came down from’ differ, and the note did not say why. | Added: an accusative of the place she comes down from (English needs ‘from’). |
| 24 | 166 | n | low | ὁμιλεῖν glossed ‘not to consort’ against `l` ‘mingle’, `i` ‘keep company’; κέρδιον described as ‘the comparative of the adjective of κέρδος’ (garbled). | ‘not to mingle’; ‘κέρδιον being a comparative from κέρδος ‘gain’, ‘better, more profitable’’. |
| 25 | 153 | n | low | φίλον ‘dear’ left without saying what it agrees with (it agrees with ἦτορ, not δῶμα, across τετιημένος). | ‘with φίλον ‘dear’ agreeing with ἦτορ across the word between’. |
| 26 | 192 | n | low | προσώπατα καλά glossed ‘fair face’; the house `l` for καλός of a face is ‘fine’ (row 15.332), as `l` has it. | ‘fine face’. |
| 27 | 212 | l | low | γούνατα … λύτο: house row (5.297) has `l` ‘knees were loosed’; `l` had ‘loosened’ (the note says ‘loosed’). | l ‘their knees were loosed’. |
| 28 | — | about | low | Four ASCII apostrophes in `about` (heart's, Telemachus's, Eurynome's, Penelope's); the house rule is the typographic ’. | Replaced by ’. |

Totals: 4 high, 5 medium, 19 low (28 entries; entries 5, 6, 11 touch more than one field).


### Findings considered and refused

1. **ἀμφίπολοι: ‘attendants’ at 198 (unit 54) against ‘handmaids’ at 207 and 211.** The house table (rows 6.18 etc., 7.290) fixes ‘attendants’ and lists ‘handmaidens’ among the avoided words; but 207 and 211 are repeated lines that ship as ‘two handmaids’ and ‘a trusty handmaid’ (odyssey-004.330, .335), the table itself keeps ‘handmaids’ as shipped in the identical 2.136 unit (row 10.349), and the packet requires the published wording for repeated lines. Both usages are correct under the rules; the divergence is an old one in the table, not this part’s. Left; recorded for the owner under Other findings.
2. **Unit 2 (110a), `l` ‘And back, then, he, to the threshold going, sat down’ puts ‘then’ (ἄρα) after ‘back’, though the note puts ἄρα inside the tmesis.** The wording is the shipped `l` of 17.466 (odyssey-086.466) word for word; the note’s statement about where ἄρα stands is true of the Greek. Left.
3. **Unit 13 (126–127), `i` ‘since I used to hear a good name given to Nisus of Dulichium, that he was both a good man and a rich one’ — the ‘name … that’ construction is heavy.** The table fixes κλέος ἐσθλόν as ‘a good name’ and the construction is accusative with infinitive after ἄκουον; the English is grammatical and follows the Greek. Left.
4. **Unit 44 (180–181), ‘my splendour, for me at least’ / ‘my beauty, for me at least’ renders ἐμοί twice.** The idiomatic possessive for a dative of interest, with ἐμοί γε kept as the emphasis; `l` and `i` agree and the note explains ἐμοί γε. Left.
5. **Units 46–47, `i` ‘for I will not go in … alone;’ followed by ‘for I am ashamed.’** The first ‘for’ renders δέ, which can be explanatory after the request at 183, and the second renders γάρ. Two ‘for’s in neighbouring clauses read acceptably; `l` keeps ‘and’ and ‘for’. Left.
6. **Unit 30, `l` ‘bound’ and `i` ‘fettered’ for πέδησε.** Both ship: odyssey-011.269 (ἐπέδησε) has ‘bound’ / ‘bound’, odyssey-053.292 (κατὰ … πέδησε) has ‘fettered (him) fast’ / ‘fettered’; the table has no row for πεδάω. The note says ‘bind, fetter’. Left.
7. **Unit 56, `i` drops ἦ ‘truly’ (`l` has it).** A mild assertion; `i` carries the force with ‘so terribly afflicted’. Left.
8. **Unit 21, `i` drops πάμπαν ‘at all’.** `i` says ‘let no man ever be lawless’; `l` has ‘ever at all’. Left.
9. **Unit 36, `i` ‘think ill behind one’s back’ for ὄπιθεν.** `l` has ‘behind’; the English idiom has the same sense and the note says ‘behind’. Left.
10. **Unit 41, `i` ‘of an age’ for τηλίκος (`l` ‘of such an age’).** An idiomatic English rendering of the same meaning. Left.
11. **ἄναλτον (112), ‘insatiable’, not flagged as uncertain.** It matches the shipped rendering at 17.228 (odyssey-084.226, ‘insatiable belly’ in both layers); the meaning is the traditional one and no earlier note called it unknown. Left.
12. **ἐπητῇ (128), ‘ready of speech’.** Matches the table row (13.332) and odyssey-065.331; the note says the sense is only approximately known. Left.
13. **κοσμήτορι λαῶν (152), ‘marshaller’ / ‘marshal’; κλεηδόνι ‘omen’; ἀθεμίστιος ‘lawless’; ἀχρεῖον ‘idly’; αἰνοπαθῆ; κῶμ’ ‘slumber’; κλιντῆρι ‘couch’; τέκος ‘child’; ἔξοχος Ἀχαιῶν; χορὸν ἱμερόεντα; ἀγλαΐην ‘splendour’ / ‘beauty’.** Each looked up in the table and the published parts: no earlier shipped rendering and no conflicting row (ἀγλαΐη plural ‘splendours’, 17.244, is the table’s separate row and `l` keeps its root-sense; κλιντήρ ‘couch’ shares its English with εὐνή as the new-renderings row says; ἱμερόεις keeps ‘full of longing’ as at 10.398 and 17.519). Left.
14. **Fixed formulas.** ἦ ῥα καί ‘He spoke, and / So he said, and’ (row 8.416), πάτερ ὦ ξεῖνε ‘father, O stranger’ / ‘stranger, my father’ (row 8.408), χαῖρε ‘Welcome’, αἴθε ‘Would that / If only’ (row 14.440), κατὰ μοῖραν ‘according to what is fitting’ / ‘as is fitting’, ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν, ἀπονίπτεσθαι, παραύδα ‘speak / talk soothingly’ (row 11.488), ἀεκαζόμενος ‘much against his will’ (row 13.277), κῆρα ‘death-fate’ / ‘death’ (row 15.235), ὄσσετο ‘foresaw’, δεινός etc. all agree with the table. Left.
15. **Remembered English.** No phrase in `i` arrived whole; the four- and five-word overlaps with published `i` fall in fixed formulas or repeated lines.

### Other findings for the next pass or the drafter (not changed here, because the reviewer edits `units.json`; the one exception is stated)

- **new-renderings.md, row for ἀκιδνότερον (18.130):** the row proposed ‘frailer’ as a new choice, but the word already ships as ‘slighter’ (5.217, 8.169). Because the rows of this file are copied into the table in `conventions.md` at publication and ‘frailer’ would have contradicted the shipped parts, the row was edited in place to say ‘slighter’ in both layers, with ‘frailer’ moved to the avoided column and a remark that the word is not new. This is the only change made outside `units.json`; the drafter or the owner may prefer to delete the row altogether.
- **For pass 2 (`gloss.json`):** check that the entries for ἀκιδνότερον (meaning ‘slight, feeble’, not ‘frail’), ἠρῶ (imperfect, not aorist), παρέχωσι (present subjunctive), ἔειπες (augmented aorist, augment unfused), πέδησε, δεικανόωντ’ (elided -ντο, imperfect middle 3 pl.), ἔχεαι (= ἔχῃ, pres. mid./pass. 2 sg.), παρστήετον (dual), θησαίατ’ (θηέομαι), φάο and ἀπεβήσετο agree with the notes as now corrected.
- **Table divergence, ἀμφίπολοι:** ‘attendants’ (rows 6.18, 7.290) against ‘handmaids’ shipped in odyssey-004 (18.207, 18.211 repeat 1.330 and 1.335) and in the identical 2.136 unit (row 10.349 accepts it). This part uses both, each where its rule requires; the owner may wish to settle the table.
- **new-renderings.md, all other rows:** checked against the English in `units.json` and against the table; the English in both layers matches every row (ὣς ἄρ’ ἔφαν; κλεηδών; κοσμήτωρ λαῶν; ἀθεμίστιος; ἀχρεῖον ἐγέλασσεν; αἰνοπαθής, now with ‘very’ in `l` before it, which the row’s ‘fearsomely suffering’ still covers; κῶμα; ἀγλαΐη; κλιντήρ; τέκος; ἔξοχος Ἀχαιῶν; χορὸν ἱμερόεντα; ἡ δ’ αὖ Τηλέμαχον προσεφώνεεν). No row conflicts with the house table.


## Pass 2

Reviewer, pass 2 of 2 (`units.json` re-read from scratch, and `gloss.json` checked entry by entry). Method: runbook section 2 order again. (1) Every grammatical label, word-position claim and cross-reference in all 64 notes against the form and the line; cross-references re-looked up in `source/odyssey-murray1919.json` (18.84–85, 16.414–416, 13.437–438, 4.793–795, 8.19–20, 5.217, 8.169, 1.330–334, 1.366, 2.382, 2.393, 17.197–198, 17.466, 18.44–45, 9.106). (2) Greek to `l` word by word. (3) `l` against `i`. (4) Remembered English. (5) Quotation marks by script: “ on the first unit and ” on the last of each of the seven speeches in both `l` and `i`, `mark` on exactly units 4, 9, 12, 35, 38, 43, 56, no speech left open at the end of the part; unit 63 correctly has no “. (6) `gloss.json`: all 106 keys in `novel-forms.json` present and no extra; every parse set against the line(s) where the form occurs; format by script (no ASCII `'` or backtick in any entry, no "here", no line numbers, all novel entries under 230 characters, no novel article-form, none needed for the possessive ὅς); each of the 16 `__broaden__` entries checked as "old entry whole (compared with `known-forms.json`) plus new reading" and each new reading checked against its line; then every known form of the part read against its `known-forms.json` entry to see whether the use here is covered. Pass 1's four corrections (ἠρῶ imperfect, παρέχωσι present subjunctive, ἔειπες unfused augment, ἀκιδνότερον ‘slighter’) are now in agreement across `units.json`, `gloss.json` and `new-renderings.md`. `t` untouched: all 64 `t` strings byte-identical before and after (checked by script). Scansion flags: none in the packet.

### Changes — units.json

| # | Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 177 | n | high | προσέειπε called ‘the uncontracted aorist of πρόσφημι’. It is the aorist of προσεῖπον (πρός + εἶπον) with the augment unfused (προσέ-ειπε); πρόσφημι has προσέφη (unit 11). The known-forms entry already says προσεῖπον. | ‘the aorist of προσεῖπον ‘address’ with the augment left unfused (Attic προσεῖπε)’. |
| 2 | 184 (οἴη δ’ οὐκ εἴσειμι) | n | medium | εἴσειμι called ‘the future of εἰσέρχομαι’; it is a present form (εἰς + εἶμι) with future sense, as the glossary entry says; the note and the gloss disagreed. | ‘the present of εἴσειμι (εἰς + εἶμι) with future sense’. |
| 3 | 202 (αἴθε μοι ὣς) | n | low | πόροι said to be from ‘πόρω’, which is not a lemma; the defective aorist is πόρον (known-forms entry: πόρον (πορεῖν)). | ‘the aorist optative of the defective aorist πόρον’. |
| 4 | 126 (τοίου γὰρ καὶ πατρός) | n | low | ‘with σε understood’: the missing word is the verb (‘you are’), not a pronoun; `l` ‘you are’ is already the verb. | ‘with ‘you are’ understood’. |
| 5 | 136 (τοῖος γὰρ νόος) | n | low | ‘tmesis for ἐπάγῃσι … the subjunctive (Attic ἄγῃ)’: the Attic form of the compound is ἐπάγῃ. | ‘(Attic ἐπάγῃ)’. |
| 6 | 175 (ἤδη μὲν γάρ τοι) | n | low | τοι (‘your’, ‘to you’) is translated in `l` and `i` but not mentioned. | Added: τοι ‘your’ (Attic σοι), a dative of the person concerned. |
| 7 | 171 (ἀλλ’ ἴθι) | l | low | ἔπος has no article; `l` ‘speak the word’. | l ‘speak a word’ (`i` keeps ‘the word’ as English prose). |
| 8 | 180 (ἀγλαΐην γάρ) | i | low | ‘in their hollow ships’: no ‘their’ in κοίλῃς ἐνὶ νηυσίν. | ‘in hollow ships’. |
| 9 | 199 (τὴν δὲ γλυκὺς) | n | low | ‘where she wipes away tears’: tears are not in the Greek. | ‘as one does on waking’. |
| 10 | 212 (τῶν δ’ αὐτοῦ) | n | low | λύτο quoted as ‘were loosed’ with no parse. | Added: the unaugmented aorist passive of λύω. |

Totals for `units.json`: 1 high, 1 medium, 8 low.

### Changes — gloss.json

| # | Key | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 11 | ἠρῶ | high | ‘past 2 sg.’ is vague and Pass 1 had fixed the label: imperfect of ἀράομαι (ἠράου > ἠρῶ). | ‘impf. 2 sg. mid./dep.’ |
| 12 | ἀκιδνότερον | medium | meaning ‘weak, insignificant’ and gloss ‘frailer’ contradict the shipped ‘slighter’ (5.217, 8.169) and the corrected note. | ‘slight, feeble, of little account … ’slighter’’. |
| 13 | οὐδὲν (`__broaden__`) | medium | new reading described as ‘object or subject’ though the form is only the object of τρέφει here, and quoted ‘frailer’ / ‘nourishes nothing frailer’. | ‘neut. acc. sg. as object of a verb, with a comparative: ’nothing (slighter)’ (οὐδὲν ἀκιδνότερον … γαῖα τρέφει)’. Old part unchanged. |
| 14 | φθινύθω | medium | parsed ‘pres. 1 sg.’; in ἵνα … φθινύθω it is the subjunctive (the note says so). | ‘pres. subj. 1 sg. (same form as the indic.)’. |
| 15 | ὀρώρῃ | low | ‘perf. subj. 3 sg. mid.’: ὄρωρα is the active-form intransitive perfect; there is no middle here. | ‘perf. subj. 3 sg. (of ὄρωρα …), intrans.’ |
| 16 | ἐπητῇ | low | ‘after ἔοικα + dat.’ pins the entry to one construction (it agrees with ἀνδρί). | ‘masc. dat. sg.’ |
| 17 | ὄφρ (new `__broaden__`) | medium | ὄφρ’ ἀρετὴν παρέχωσι (132) is temporal ‘so long as’ + subjunctive without ἄν; the entry has ‘as long as’ only with the indicative and ‘while/until’ with ἄν. | Old entry whole + ‘also temporal + subj. without ἄν or κε, ’so long as’ …’. |
| 18 | μὴ (new `__broaden__`) | medium | μὴ πάντα … ὁμιλεῖν (166) is μή with an infinitive of advice; this key's entry has no infinitive use. | Old entry whole + ‘also + inf., negating an infinitive of advice …’. |
| 19 | πρὸς (new `__broaden__`) | low | πρὸς πόσιός τε καὶ υἱέος (162), ‘in the eyes of’, is not among the genitive uses. | Old entry whole + ‘also + gen., ’in the eyes of, with’’. |
| 20 | ἔς (new `__broaden__`) | low | ἔς περ ὀπίσσω (122): the preposition with an adverb, no noun; the entry has only ‘+ acc.’ and tmesis. | Old entry whole + the idiom. |
| 21 | πέδησε (new `__broaden__`) | low | entry says ‘tmesis with κατά (= κατέπεδησε)’; in 155 the verb stands simple, with no preverb. | Old entry whole + ‘simple aor. with no preverb: ’bound, fettered’’. |

Totals for `gloss.json`: 1 high, 5 medium, 5 low (11 entries). Combined with `units.json`: 2 high, 6 medium, 13 low (21 changes).

Checked and left: the other 100 novel entries (parse true in each line they occur in, Attic equivalent named where Homeric, article-forms none); the broadenings εἴη, οἷον, οἵῳ, τό, τρέφει, πείσεσθαι, πηνελοπείῃ, ἀνῆκε, ἐγώ, ἐπ, ἔπι, ἴῃ, ἱμερόεντα, ὁππότε, ὄπιθεν (each new reading is true of a line in the part, and the old entry is carried whole, verified by script against `known-forms.json`). In `ἐπ` the old entry itself uses the ‘ ’ quotes of an earlier part; it is old text and is not rewritten.

### Findings considered and refused (pass 2)

1. **Unit 18 (134), `i` ‘bring grievous things to pass as well’ for καὶ λυγρά (`l` ‘even’).** καί is ‘also’ or ‘even’; ‘as well’ is within the range and the note says ‘but when even’. Left.
2. **Unit 38 (170), `l`/`i` ‘have spoken’/‘have said’ for the aorist ἔειπες.** An aorist of what has just been said; English perfect is the natural rendering and the table has no row against it. Left.
3. **Unit 9 (122), `l` ‘even hereafter’ against `i` ‘at least in the time ahead’ for ἔς περ ὀπίσσω.** περ is a weak intensifier; both layers carry it, in different words. Left.
4. **ἐπὶ φρεσὶ θῆκε (158), ‘put in her mind’ not named in the ἐπὶ entry.** ‘on, upon’ with the dative covers ‘upon the mind’; no separate reading needed. Left.
5. **Unit 55, φώνησέν τε ‘the accent moving onto the verb’.** The acute is the extra accent a proparoxytone takes before an enclitic; the note's wording is loose but not false. Left.
6. **ἐπ broadening ‘ἐπ’ ἦμαρ ‘for a day’’ (136).** Not the reading `l` and `i` take (tmesis, covered by the old entry), but the note itself offers it as the alternative and the entry is general. Left.
7. **πηνελοπείῃ broadening uses ‘prudent’ where the house epithet is ‘circumspect’.** The old part of the entry already says ‘prudent’; the glossary gloss is not an English-layer rendering. Left.
8. **Unit 59 (207), ‘The half-line ends at a full stop’.** The unit is the second half of line 207 (it begins mid-line 207, after the ano teleia that ends the previous unit); the wording is clumsy but true. Left.
9. **Pass 1's refused findings (ἀμφίπολοι ‘attendants’ against ‘handmaids’, etc.)** re-examined; the same reasons hold. Left.
10. **Remembered English.** Nothing new beyond the formulas and repeated lines already agreed in Pass 1.
