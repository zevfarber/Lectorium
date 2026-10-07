# odyssey-093 — review (Odyssey 19.104–202)

Reviewer: adversarial, two passes. Read in full before starting: `conventions.md` (every row of the house table, the glossary and notes sections), `runbook.md` section 2, `packet.md`, `new-renderings.md`, `units.json`, the last units of `drafts/odyssey-092/units.json`. No next part exists yet. No modern translation was opened or recalled. `t` was never touched (checked after each pass: every `t` byte-identical to the draft, tiling and `p`/`ln`/`v` unchanged). `gloss.json` was not touched.

Severity scale used here: **major** = wrong sense, false note, or a structural failure; **moderate** = a rendering or note that misleads, or that breaks a fixed rule / shipped repetition; **minor** = house-table consistency or polish with no change of sense.

Context checks that passed without change:
- Speech marks. 092's last unit ends Penelope's line “ἐθέλω δέ μιν ἐξερέεσθαι.”” (closed) and then ¶ τοῖσι δὲ μύθων ἦρχε Πηνελόπεια, so 093 opens a new speech at 19.104 (“ and `mark`), closes it at 19.105 (”). Odysseus 107–122 (“ … ”), Penelope 124–163 (“ … ”), with her quoted words to the suitors 141–147 in single marks (‘ … ’), the opening ‘ on 141 and the closing ’ on 147. Odysseus 165 opens “ and runs on into the next part with no closing mark (as it must; unit 54's note says so). Counts: “ 4, ” 3 in both layers; the validator will WARN once (open > close), which is correct and should be mentioned in LOG.md.
- `mark` is on the first unit of each of the five speeches (104, 107, 124, 141, 165); `p` on the first unit of each of Murray's six ¶ (104, 106, 123, 141, 148, 164).
- Whole-unit repeats (19.104, 106, 123, 129, 148, 164) are identical in `l` and `i` to every published unit with the same Greek (checked against all 92 published stories, not only the packet's list).
- Scansion: the packet flags none. The scanner fits all 99 lines with no UNRESOLVED/AMBIGUOUS flag; it prints an informational "spondaic fifth" on 19.173, 188, 191, 194. Scanned by hand: 173 (… ἐν δ’ ἄνθρωποι), 188 (… Εἰλειθυίης), 191 (… αἰδοῖόν τε), 194 (… ἐξείνισσα) are ordinary hexameters with a spondaic fifth foot (a regular licence, 4 lines in 99); no irregularity, so no sentence added to any note.

## Pass 1 — changes (line · field · severity · what was wrong · what was done)

1. 19.108 · `i` · minor · θεουδής rendered "fearing the gods", but the house table fixes "god-fearing" in both layers. · "like the fame of some blameless king who, fearing the gods and ruling over many mighty men, upholds" → "… who, god-fearing and ruling over many mighty men, upholds".
2. 19.118 · `i` · moderate · The second half of line 120, ἐπεὶ κάκιον πενθήμεναι ἄκριτον αἰεί, is a repeated half-line (odyssey-089, unit at line 173: l "since worse it is to mourn without end, always", i "since it is worse to grieve endlessly, always"). `l` already matched; `i` ("keep mourning without end") varied the wording and dropped αἰεί altogether, so `l` and `i` disagreed in force. · `i` → "since it is worse to grieve endlessly, always;".
3. 19.121 · `n` · moderate · Label asserted "the future indicative after μή" for νεμεσήσεται; with the coordinate subjunctive φῇ following, the form is as likely a short-vowel subjunctive, so the label was not safe. · Rewritten: "μή … νεμεσήσεται (future in form, though it may be read as a short-vowel subjunctive) is ‘lest … feel indignation at me’" (the final wording came in pass 2, see below). Sense unchanged; the glossary's "fut. 3 sg. mid." entry stays compatible.
4. 19.137 · `i` · moderate · τολυπεύω rendered "spin out my tricks": in English "spin out" means prolong, which is not the verb (wind off, work up, carry through) and contradicted the unit's own note. · "while I spin out my tricks" → "while I work out my tricks".
5. 19.138 · `l`, `i`, `n` · moderate · λεπτὸν καὶ περίμετρον is a repeated half-line (odyssey-005, 2.95: l and i both "fine and very large"). The draft had "fine and of surpassing measure" (l) and "fine and of ample size" (i), neither the shipped wording nor each other. · Both layers → "fine and very large;"; note rewritten to "περίμετρον ‘very large’ (περί- ‘very’, μέτρον ‘measure’), a rare word".
6. 19.149 · `l`, `i`, `n` · minor · The line is the first-person form of 2.104–105 (odyssey-006: "There by day she would weave the great web, / but by nights she would unravel it, when she had set torches beside her"). The draft varied it ("There also … used to weave … undo … whenever" / i "So by day …"), and `l` "There" against `i` "So" for ἔνθα. · `l` → "There by day I would weave the great web, / but by nights I would unravel it, when I had set torches beside me."; `i` → "There by day I would weave my great web, and by night unravel it again, once I had placed torches beside me."; note "used to" → "would". (ἱστόν stays "loom" at 138 and "web" at 149, as shipped at 2.94 / 2.104.)
7. 19.152 · `i` · minor · μηνῶν φθινόντων, περὶ δ’ ἤματα … ἐτελέσθη parallels odyssey-049 (unit at line 469: "as the months waned, … had run their course"); the draft's "wore away … were completed" did not match `l` "waning" or the shipped wording. · "as the months wore away and many days were completed," → "as the months waned and many days had run their course,".
8. 19.156 · `i` · minor · Shipped odyssey-006 (2.110, same words): "against her will, under compulsion". · "though unwilling" → "against my will".
9. 19.167 (ἀλλ’ ἔκ τοι ἐρέω) · `l`, `i`, `n` · moderate · This half-line is shipped three times (odyssey-006 187, -084 229, -088 82): l "But I will speak out plainly to you", i "But I will tell you plainly". The draft had l "But out to you I will say;" (tmesis forced into English) and i "But I will tell you;". · l → "But I will speak out plainly to you;", i → "But I will tell you plainly;", note "I will tell out" → "I will speak out".
10. 19.168–170 · `l`, `i`, `n` · minor · πολλὰ βροτῶν ἐπὶ ἄστε’ ἀλώμενος is shipped (odyssey-076, unit at line 491: "over many cities of mortals wandering" / "wandered over many cities of mortals"); draft had "to many towns of men". · l → "over many cities of mortals wandering, suffering pains;", i → "wandering over many cities of mortals and suffering pains;", note ‘town’ → ‘town, city’.
11. 19.171 · `i` · minor · μεταλλάω is "inquire after" (shipped 3 times: "what you ask me and inquire after"); draft's "and want to know" drifted. · "and want to know." → "and inquire after.".
12. 19.172 · `l`, `i`, `n` · minor · μέσῳ ἐνὶ οἴνοπι πόντῳ is shipped (odyssey-023, -032, -061) as "in the middle of the wine-faced open-sea" / "in the middle of the sea that has the look of wine"; draft had "in the midst of". · Changed in both layers and in the note.
13. 19.186 · `l`, `i` · minor · Μαλειῶν is "Malea" everywhere else (odyssey-011, -018: "Malea"); draft had "Maleae" (l) and "Cape Malea" (i). The note already said "Malea". · Both → "Malea".
14. `about` · moderate · "… younger brother of Idomeneus, who once entertained Odysseus, kept twelve days by the North Wind" reads as if Idomeneus entertained Odysseus; it is Aethon (Odysseus in disguise) who entertains, and Odysseus who is kept by the wind. · "… younger brother of Idomeneus, and he once entertained Odysseus, whom the North Wind kept in Crete for twelve days."

Pass 1 totals: **major 0, moderate 6 (items 2, 3, 4, 5, 9, 14), minor 8 (items 1, 6, 7, 8, 10, 11, 12, 13)**; 14 changes.

## Pass 1 — findings considered and refused

- 19.107 νεικέοι "find fault with you". Considered as possible remembered English; rebuilt from νεικέω "quarrel with, blame" with a potential optative, which gives exactly this; the house rows reserve "rebuke/revile" for the verb of abuse in aorists and imperatives, and "no one could rebuke you" would be wrong for a compliment. Kept.
- 19.108–114 "upholds just judgements", "the peoples prosper under him", "from good leadership", "the flocks bear without fail". Each rebuilt from case relations (ἀνέχω "hold up", εὐδικία "good judgement", ἀρετάω "thrive", ἔμπεδα "steadily/without fail", ἡγέομαι) and none matches a table row or shipped line; kept.
- 19.107 ὦ γύναι "O woman" against 19.165 "O wife of Odysseus": the first is the unmarked address (table row at 11.248), the second is shipped and fixed by the genitive depending on γύναι. Kept.
- 19.124–128, five lines with no stop at the end of 126. A cut at 126 is impossible (no punctuation in `t`), and cutting at the comma after 127 would strand the apodosis. The unit is at the five-line limit, not over it. Kept; the note says the semicolon is ours.
- 19.136 note "Ὀδυσῆ(α), elided here": the form stands before a consonant, so "elided" is loose, but the existing glossary entry for ὀδυσῆ uses the same words and the note agrees with it. Not touched; flagged for the owner.
- 19.152 ἐπήλυθον ὧραι "the seasons passed by / had passed": ἐπ- suggests "came on, came round", but this is a repeated line shipped in odyssey-006 (and the packet requires its wording), so kept.
- 19.121–122 i "because my wits are weighed down" — first pass kept; reconsidered and changed in pass 2.
- 19.165 mark "Odysseus begins his tale" — first pass kept; reconsidered and changed in pass 2.
- 19.174–177 "Dorians in their three tribes": the note says τριχάϊκες is unknown and that `l`/`i` follow one guess; kept.
- 19.179 "nine-year terms", "confidant": rebuilt from ἐννέωρος and ὀαρίζω, both flagged in the note; kept. Not added to `new-renderings.md` (not formulaic).
- 19.180 i "father of my father, great-hearted Deucalion" could be misread; the note states the apposition. Kept.
- 19.151 "the Achaeans" for the suitors: shipped usage (Penelope's account of the web in odyssey-006); kept.
- `new-renderings.md`: the two rows (νηυσὶ κορωνίσιν, δῖοι Ἀχαιοί) are the only phrases of this part that will plainly recur and have no row; both layers are used consistently (curved ships ×2; heavenly Achaeans ×1 plus δῖοί Πελασγοί). Complete.

## Structural check of build_odyssey.py (read, not run)

Emulated line for line with a separate script (`odyssey_lib` helpers only; `build_odyssey.py` was not run and nothing was written outside `units.json` and this file):
- title/titleEn/part/about present; cite `19.104–202` in `part` and `titleEn`; sha256 of the source matches `parts.json`.
- Tiling: every `t` is a prefix match of the edition at the running position; units end at a space or newline; the edition is fully covered.
- Per unit: `ln` equals the line the unit starts on (55 of 55); `p` true exactly where a unit begins on a Murray ¶ line; `v: true`; `l`/`i`/`n` non-empty; `l` has as many `\n` as `t`; no `\n` in `i`; no unit over five lines (max 5 at 19.124); every `t` ends in `.;·` or `,` (the em-dash line 143 is mid-unit).
- Scansion: all 99 lines scan, no UNRESOLVED/AMBIGUOUS; the validator's hexameter test (six feet, 12–17 syllables, one final ×, one caesura) holds for every line; token stream aligns with the words (716 of 716).
- `gloss.json` (read only): 104 keys, all in `novel-forms.json`, none already in the glossary, all occurring in this part; every entry matches `^\S.* — \S`, under 230 characters, no ASCII apostrophe or backtick; the 13 `__broaden__` entries each contain the old entry whole; no form of the part is left without an entry. (The 230-character limit is only checked for new entries; broadened `αὐτοῖς`, `μή`, `ὅσσον`, `εἰς`, `ἄλλη` exceed it and the build does not mind.)
- Validator-side: no ASCII `'`, backtick or koronis in `t`/`n`; notes are between 37 and 93 words (band 20–130 holds, no WARN); no modern translator named; the same-Greek-same-English rule holds for units 0, 2, 9, 11, 21, 31; one expected WARN for the unmatched “ at 19.165.
Expectation: `python3 build_odyssey.py odyssey-093` hits no structural error on the current `units.json` and `gloss.json`.

## Pass 2 — fresh complete read of the revised units.json (and gloss.json read-only)

Re-read all 55 units again from the Greek (line by line against `l`, then `l` against `i`, then every note against the line), and `gloss.json` against the lines. Nothing in pass 1's edits introduced a new error; the shipped-wording alignments were re-checked against odyssey-005/006/011/018/023/032/049/061/076/084/088/089.

Changes (line · field · severity · wrong · done):
1. 19.121–122 · `i` · minor · "and say that I am swimming in tears because my wits are weighed down with wine": the participle βεβαρηότα is circumstantial; "because" adds a causal link the Greek does not state. · → "and say that I am swimming in tears, my wits weighed down with wine.”".
2. 19.121 · `n` · minor · My own pass-1 hedge on νεμεσήσεται was clumsy ("which may also be read … either way after μή"). · → "μή … νεμεσήσεται (future in form, though it may be read as a short-vowel subjunctive) is ‘lest … feel indignation at me’".
3. 19.165 · `mark` · minor · "Odysseus begins his tale" is premature: the unit is the protest "will you never stop asking about my family?"; the tale of Crete begins at 172. · → "Odysseus answers again".

Pass 2 totals for units.json: **major 0, moderate 0, minor 3**.

Findings on `gloss.json` (not edited; for the glosser or the owner):
- moderate: `δμῳῶν` is parsed "δμώς … masc. gen. pl." but the unit translates "one of the maids" (fem., cf. δμῳάς at 19.154); the lemma should be δμῳή "female slave, maid", fem. gen. pl. (the ending is the same for both genders).
- moderate (gap): known form `ἱέμενον` (19.187) keeps the old entry "ἵεμαι … + gen.: ‘(you) eager for (your return)’", which does not cover "ἱέμενον Τροίηνδε" "making for / bound for Troy" (+ directional adverb); it needs a `__broaden__` reading.
- minor: `ἐνιπλήσῃς` is glossed "(prohibition) ‘do not fill’" but in 19.117 it is read in `l`/`i`/`n` as "lest you fill" (negative clause after imperatives); align one or the other.
- minor: `κατεδόντων` is called a "gen. absolute"; the unit note takes it as the genitive participle after ἀσχαλάᾳ ("vexed at those who eat up …"); say "gen. participle with ἀσχαλάω (cause)" or leave both.
- minor: `τίκτε` gloss "’bore’" for a father's act in the line (translated "begot"); give "’begot’".
- minor: `θυμόν` broadening "’appetite’" for πλησαίατο θυμόν, while the units say "fill their heart(s)" (house: θυμός = heart); consider "’desire, heart’".
- minor: `περίρρυτος` "sea-girt": "sea-girt" is reserved in the table for ἀμφίαλος; the same entry's "flowed round by water" is right, and could stand alone.
Everything else in `gloss.json` was checked against its line and is correct (parse, case, tense, mood, voice; Ionic and epic equivalents named; homographs `αὐτοῖς`, `καρπῷ`, `κύνας`, `μή`, `οἷός`, `ὅσσον`, `εἰς`, `ἄλλη`, `ἐμοί` broadened with readings that occur here).

Pass 2 total for `gloss.json`: **moderate 2, minor 5** (reported, not edited).

## Counts

| | major | moderate | minor |
|---|---|---|---|
| Pass 1, units.json (14 changes) | 0 | 6 | 8 |
| Pass 2, units.json (3 changes) | 0 | 0 | 3 |
| Pass 2, gloss.json (reported only) | 0 | 2 | 5 |

Note for LOG.md: the validator will print one WARN (4 “ against 3 ”) because Odysseus' speech from 19.165 runs on into odyssey-094.
