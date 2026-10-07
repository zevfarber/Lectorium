# odyssey-090 (Odyssey 18.215–319) — review

## Pass 1

Scope: units.json (63 units), new-renderings.md, packet.md, against conventions.md (read in full, including the house table to its last row) and the shape of odyssey-001. No gloss.json yet (pass 2 will check parses). No lines flagged by the scanner; `build_odyssey.py` was run once as a read-only probe and refuses only at unit 52 (see "Line 303" below). `t` was not touched in any unit (checked: every `t` is byte-identical to the draft as received).

Order followed: every grammatical label in every note against the form and line; word-position claims; cross-references (all line numbers cited in notes were checked: 215/220, 219, 221, 237, 244, 256/274, 217/274, 292–301, 295); notes against their own `l`/`i`; Greek to `l` word by word; `l` against `i`; remembered English; quotation marks; whole-line and half-line repeats against the 89 published parts (by script, line by line); house renderings against the table; new-renderings.md against the table.

Counts: **5 high, 14 medium, 13 low** changes in units.json, plus 4 housekeeping edits to new-renderings.md.

### Changes in units.json

Line = the unit's `ln`.

**High**

| Line | Field | What was wrong | What was done |
|---|---|---|---|
| 217 | n | Called νῦν δ’ ὅτε … ἱκάνεις a "condition" with "its result" in the last line. There is no conditional here: ὅτε δή gives a temporal/concessive clause, the κέν + optative is a separate remark, and the main statement is the last line. The note also ran 146 words (over the validator's 130 cap). | Rewrote the structural sentence accurately; note now 129 words. |
| 261 | n | Cited "οἵ κε ... ἔκρινον" (an imperfect) but the line has ἔκριναν, an aorist indicative. A form that is not in the line. | "οἵ κε ... ἔκριναν is κε with the aorist indicative of κρίνω, a general statement". |
| 272 | n | ἀπαυράω "with the double accusative of person and thing". The person is τῆς, a genitive; only ὄλβον is accusative. | "with ὄλβον as its object and τῆς, in the genitive, the person deprived". |
| 304 | n | "ἕσπερον is 'evening', accusative, object of ἐλθεῖν". ἐλθεῖν is intransitive; the line is tmesis ἐπὶ … ἐλθεῖν (ἐπελθεῖν) with ἕσπερον as accusative subject of the infinitive, as the note at 306 already says of ἐπὶ … ἦλθεν. | Corrected: tmesis, ἕσπερον the accusative subject of the infinitive. |
| 306 | n | Called τοῖσι … τερπομένοισι a "dative absolute". The dative depends on ἐπὶ … ἦλθεν ("came on them"), as the unit's own `i` says. | "the dative of the persons the evening came upon, with the participle of τέρπω". |

**Medium**

| Line | Field | What was wrong | What was done |
|---|---|---|---|
| 215 | n | "the first of three in a row built on the same words": there are two (215, 220); the note at 217 itself says 220 repeats 215. | "the first of two built on the same words (220 repeats it)". |
| 216 | l, i, n | κέρδεα rendered "shrewd things" / "shrewd thoughts". The noun is already shipped "cunning-ways" / "cunning ways" (odyssey-005 at 2.87, odyssey-006 at 2.115, odyssey-064 at 296; table row κέρδεα οἶδεν / εἰδώς). | `l` "cunning-ways", `i` "cunning ways", note says it is the house rendering. |
| 231 | l, i | κακὰ φρονέοντες rendered "with evil in mind" / "with evil in their thoughts". Shipped for the same participle: "evil thinking" / "meaning evil" (odyssey-048, table row 10.317) and "think evil things" / "mean evil" (odyssey-087). | `l` "thinking evil", `i` "meaning evil". |
| 233 | i, n | ἰότητι given as "wish". The table fixes ἰότης as "will", "one word throughout" (θεῶν ἰότητι, κακῆς ἰότητι). | `i` "by the suitors' will"; note says 'will' is the house word. |
| 247 | l, i, n | Line 249 is word for word 11.337 (odyssey-054, unit at 336), shipped "in looks and in stature and in the wits within, well-balanced" / "in looks and stature, and in the well-balanced mind within" (and table row 11.337). The draft had "form" and "balanced wits within". The packet did not list the line (packet.py's half-line-repeat gap, noted in QUESTIONS.md). "A repeated line gets the same English every time." | Both layers set to the shipped wording for that line; note names εἶδος as "looks, form" and says the line stands in an earlier part (11.337). |
| 251 | l | "my excellence, both form and body, / destroyed the immortals": in English the immortals read as the object; in Greek ἀθάνατοι is the subject of ὤλεσαν. A misleading `l`. | "the immortals destroyed" (subject unambiguous; the verb is no longer first). |
| 251 | n | "the 'up' is the going aboard of the ships, which the line does not say": an unsupported claim that also contradicts itself. | "the Argives 'going up' to Ilium, the line not saying from where". |
| 261 | l, n | ἀκοντιστάς "spear-throwers". The table keeps "javelin" for ἄκων (13.225) and reserves "spear" for ἔγχος / δόρυ; the unit's own `i` already said "javelin-throwers". | `l` "javelin-throwers"; note "men who hurl the ἄκων 'javelin'". |
| 280 | l, i, n | νήποινον rendered "without repayment" in `l`, and "eat up" for ἔδουσιν. The line stands in odyssey-002 at 1.159 as "unpunished" / "pay nothing for it" and "devour" (table row νήποινον ἔδοντες / ἔδουσιν, 14.377 and 14.417, which follows 1.159). | `l` "but not another's living unpunished do they devour.”", `i` "but they do not devour another's living and pay nothing for it.”"; note rewritten (no backticks: the validator fails on them). |
| 285 | n | δέξασθ’ called "the aorist imperative δέξασθε", a plural imperative addressed to one person. The neighbouring γήμασθ’ (270) and μεμνῆσθαι are taken as infinitives used as imperatives. | "most simply the aorist middle infinitive δέξασθαι, elided and used as an imperative … a plural imperative δέξασθε is unlikely". |
| 288 | l | Line 288 is word for word odyssey-006 (2.127 unit), published `l` "But we will not go, before then, to our own work, nor anywhere else,". The draft reordered it; the packet says to reuse the published wording for a repeated line as far as the sentence allows (it allows it here). `i` already matched. | `l` set to the published wording. |
| 295 | i | πολυδαίδαλον given in `i` as "of elaborate work", against the table's row for θάλαμον πολυδαίδαλον (6.15): "much-wrought" / "richly wrought". The new row 17 contradicted a table row without saying so. | `i` "For Eurymachus his herald at once brought a richly wrought necklace."; conflicting row removed from new-renderings.md. |
| 310 | i | ταλασίφρων given as "enduring-minded" in `i`. Table row and every shipped `i` I checked (odyssey-002, -009, -016) have "steadfast"; "-minded" is `l`-only. | `i` "the maids of steadfast Odysseus". |
| 315 | i | `i` moved ἥμεναι to the front ("sit with her and spin … beside her, and please her in the hall"): "sit with her" is not in the Greek, and "in the hall" was attached to the wrong verb (in Greek ἐν μεγάρῳ belongs to ἥμεναι, as `l` has it). | "spin your yarn beside her, and please her as you sit in the hall, or comb wool with your hands;". |

**Low**

| Line | Field | What was wrong | What was done |
|---|---|---|---|
| 229 | n | Last sentence ("cuts off the clause begun before the raised point") said nothing true. | "The raised point stands in the middle of line 229, so this unit is the second half of the line." |
| 233 | i | "the stranger was simply the stronger": "simply" is not in the Greek. | Dropped. |
| 239 | n | Quoted ὅπῃ; the line prints ὅπη. | Quoted as printed. |
| 256 | n | "imperfect" for ἐπέσσευεν. The doubled σ is that of the epic aorist ἔσσευα of σεύω; the tense was asserted without need. | "a past tense (the aorist) of ἐπισεύω". Pass 2: the glossary parse must agree (aorist). |
| 265 | n | ἀνέσει asserted as "the future … with κε". The form is read as a future or as a short-vowel subjunctive; the label was stated more firmly than the grammar allows. | Both readings named; sense unchanged. |
| 284 | n | "Murray prints a comma where the sense wants a raised point": a claim about the print the pinned source cannot show. The source has a comma; other published parts print the same formula with a raised point. | Reworded to what the text shows (comma here, raised point in the same formula elsewhere; unit ends here all the same). `t` untouched; the build accepts a comma. |
| 296 | n | Stray ". and ἐερμένον the perfect passive participle" (lower-case sentence start, no verb). | "; ἐερμένον is the perfect passive participle". |
| 302 | l | `l` ended without a stop while `i` ended with one. | `l` ends with a full stop (see "Line 303"). |
| 302 | i | "to the upper rooms", against new-renderings row ὑπερώϊα ("her upper rooms"). | "to her upper rooms". |
| 302 | n | "Murray prints no stop at the end of line 303": would be false once the stop is restored, and unprovable from the source. | Sentence removed. |
| 310 | n | "Murray prints both Ὀδυσσῆος and Ὀδυσῆος, as the metre needs": this part does not show the second form. | "(Attic Ὀδυσσέως)". |
| 313 | l | δμῳαί as "Maids"; the table's `l` is "maidservants" (`i` "maids"), as unit 310 correctly has. | “Maidservants of Odysseus, …. |
| 315 | n | "The maids' tasks are the same as those of the women of the house everywhere": a claim about the rest of the world, not shown by this part. | Removed. |

### Changes in new-renderings.md (housekeeping, not units)

- Removed ἀλλότριος φώς (18.219): already in the table (16.102) with the same renderings; it would copy as a duplicate row.
- Removed ἥβης μέτρον ἱκάνεις (18.217): already in the table (11.317) with the same renderings.
- Removed πολυδαίδαλος (18.295): contradicted the table's θάλαμον πολυδαίδαλον row (6.15, "richly wrought" in `i`); the unit now follows the table.
- Added οὐλομένης ἐμέθεν (18.273): the passive sense of ὄλλυμι, of Penelope herself ("me, the ruined" / "ruined as I am"), with "ruinous" kept for οὐλόμενος of what destroys others (φάρμακον οὐλόμενον, οὐλομένη γαστήρ). "Ruinous me" would be wrong in English; the table had no row for this sense.

The other 20 rows were checked against the table and stand (Εὐρύμαχος δ’ ἐπέεσσι προσηύδα consistent with the 12.36 row; the two reply-formulas, the feminine Antinous formula, μετέφη formula, 18.281 with "she", ὠκύποδες, τρίγληνα μορόεντα, ὁμοίιος, λαμπτῆρες / δαΐδες, ὑπερώϊα, ἠλάκατα, αἰδοίη βασίλεια, ἀγλαά, ἄλλο … ἄλλος, πολυτλήμων, ποικίλος, κληῒς, φρένες ἔμπεδοι · ἐναίσιμοι). Note: ἀγλαὰ δῶρα, δαΐδες and a few others are instances of existing rows rather than new fixes; harmless, left in.

### Checked and found correct

- Quotation marks: 6 speeches, each “ on its first unit and ” on its last, in both layers (215–225, 227–242, 245–249, 251–280, 285–289, 313–319); the nested ‘ … ’ for Odysseus' words inside Penelope's speech (259–270) opens and closes correctly, in `l` and `i` and in the note; `mark` is on the first unit of each of the seven speeches (including the quoted one); `p` is on exactly the twelve ¶ lines. Seam with the previous part: odyssey-089's last unit is the introduction at 18.214 and its note says the speech begins in the next part, so 215 correctly opens with “ and no closing mark is missing there. The part's last speech (Odysseus, 313–319) closes within the part, so nothing runs on into the next one.
- Whole-line repeats equal to the published English: 226 (odyssey-003), 243 line (odyssey-019), 245/285 first line (odyssey-081), 235 first line (odyssey-017), 281 first line (odyssey-032, with "she"), 290 (odyssey-088), 291 line (odyssey-037), 304–305 (odyssey-004). Unit 290 has a raised point where the published unit has a full stop; the validator keys on letters only, so the English must be and is identical.
- Every cross-reference line number in the notes; every claim about where a word stands (σοί first at 225, ἐστίν last at 287, ἕκαστος last at 291, πολλή last at 298, ἀθάνατοι after its verb at 252).
- Greek to `l` word by word for every unit (cases, tenses, moods, particles) after the corrections above. Points that are fine and were checked: ἀπονέεσθαι present infinitive with future sense; ἐθέλῃσθα / ἴδηαι epic endings; κέ + subjunctive/optative uses at 218, 225, 247, 254, 286; γήμασθ’ as imperative; ὅς … ἔασας (relative with a second-person antecedent); τῷ … γήμασθαι with σε; ᾖεν / ᾖε from εἶμι; ἦεν; the two datives in -οισι/-ῃσι claims.
- Remembered English in `i`: nothing found that arrives formed; the nearest suspects ("grace shone from them", "a different fine gift", "ruined as I am") were rebuilt from the grammar and stand.

### Findings considered and refused

- 227 `i` "I do not blame you for being angry at this": drops "at least" and moves τὸ μέν to the anger, but τὸ is an accusative of respect either way and the contrast with αὐτὰρ ἐγώ survives. Shipped νεμεσσάω renderings vary by context; no table row. Kept.
- 216 `i` "and more than now": καὶ μᾶλλον has its second half supplied by νῦν, as the note says; the doubled "more" is the draft's way of making that explicit. Kept.
- 235 `i` has no "thus" for οὕτω: the correlation οὕτω … ὡς is carried by "just as" in the next unit. Kept.
- 259 `i` drops "for" (γάρ): the explanatory chain γὰρ (259) – καὶ γὰρ (261) – τῷ (265) still reads in English. Kept.
- 261 `l` "for indeed the Trojans, they say," vs `i` "the Trojans too": both are legitimate readings of καὶ γάρ; the note says "for indeed". Kept.
- 229 χέρεια "the worse": the table's "the lesser" belongs to the persons χέρηες (15.324); for neuter things "the worse" is the right sense and the note says χερείων is the comparative of κακός. Kept.
- 273 `l` "the ruined" instead of the table's "ruinous": see the new row; "ruinous" would be wrong of oneself.
- 279 "for the girl a feast": table row κούρη (8.468) avoids "girl" for the vocative only; shipped odyssey-036 has "girl" in `l` for the noun. Kept.
- 296 `i` "bright as the sun" for ἠέλιον ὥς: a clarifying gloss of the simile, harmless; "beads" matches the shipped 076 "beads of amber". Kept.
- 299 ἴσθμιον: `l` "neck-band", `i` "collar". Not a recurring word; no row needed. Kept.
- 271 `i` "and now all of it is being fulfilled": adds "and" where the Greek has asyndeton. English flow; kept.
- 306 "dark evening": the table's `l` for μέλας of night is "black"; this is evening, and the new row says so. Kept.
- 292 `l` "For Antinous brought he …": "for" is the dative, μέν is not "for". Brief ambiguity only; kept (i is clear).
- 251 note: ἀρετή explained by the two following nouns taken in apposition (the other reading takes all three as objects); `l` and `i` both read it as apposition and the note says so; kept.
- 239 `i` "wherever his homecoming lies": slightly indefinite; kept.
- 250 / 284 new rows are instances of existing table rows (reply-formula, Antinous formula with a feminine object); kept as sensible and consistent.
- 244 `i` drops "with words": agrees with the table's 12.36 row. Kept.
- Unit 38 (284) ends at a comma: the build accepts commas and the unit break is right (speech in the next unit). Left as the source has it.

### Line 303 (the drafter's punctuation question, rule 5 of `.github/pipeline/README.md`)

My view: **this is a rule-5 case; the stop should be added.** Evidence, none of it from memory of the poem:

1. A scan of the pinned source found 1,186 lines that end a paragraph or a book. Every one ends in punctuation except 18.303 (`περικαλλέα δῶρα`, no mark). 16.185 and 17.146, the two earlier cases, were already corrected on the owner's approval, so 18.303 is the only remaining paragraph-final line without a stop in the whole source.
2. The source's own origin (Perseus TEI, fetched for comparison) also has no mark there, the same pattern as the two corrected lines: the conversion dropped the stop at the paragraph end.
3. The sentence is complete (ἡ μὲν … ἀνέβαιν’ … τῇ δ’ … ἔφερον … δῶρα) and the next paragraph begins a new sentence with οἱ δ’ …; a missing stop is not a feature of the print.
4. No published part prints that line: I searched the `t` of all 89 published parts for the line and for its distinctive half (`ἀμφίπολοι ἔφερον`, `ἔφερον περικαλλέα`) and found no occurrence, so there is no published precedent either way. The only files that contain the line are this draft and the source.

Recommended action (for the building run, not done here): add `.` after `δῶρα` in 18.303 of `source/odyssey-murray1919.json`, re-pin the `sha256` of odyssey-090 only (no other part contains the line), let unit 52's `t` end with `.`, rebuild, and record the correction in LOG.md. Until then `build_odyssey.py` refuses ("unit 52 (line 302): does not end at punctuation"), which I confirmed. I already made `l` end with a full stop to match `i` (which already did), and removed the note's claim that Murray prints no stop. The note needs no other change when the stop is restored.

### For pass 2 (after the glosser)

- Check that the glossary parses agree with the notes as corrected: ἔκριναν (aorist indicative of κρίνω, with κε), ἐπέσσευεν (aorist), ἀνέσει (future or subjunctive: whichever the entry says, it must not contradict "from ἀνίημι"), δέξασθ’ (infinitive δέξασθαι, elided; the novel-forms list has "δέξασθ"), γήμασθ’, ἕσπερον (accusative singular, subject of the infinitive), τοῖσι/τερπομένοισι (dative), ἀπηύρα (aorist of ἀπαυράω), δαινύατ’ (optative, 3 pl.), λελῦτο (perfect optative middle), ἐΐσας.
- Known forms: check that existing entries cover this part's uses (notably κεῖνος, τόν/τήν as pronouns, the relative ὅς at 222 and 286, and φώς 'man' at 219, which must not be read as φῶς 'light'; 317 has φάος).

### Notable

- The packet missed one repeated line (249 = 11.337, odyssey-054), which the half-line-repeat gap in packet.py explains; found by a line-level scan of all published parts.
- Five notes carried a false grammatical label or a form not in the line (217, 261, 272, 304, 306); the `l`/`i` layers were sound on those lines.
- Unit 217's note is at 129 words, one under the validator's cap.

## Pass 2 (gloss.json, and a second reading of units.json)

Scope: all 90 novel entries and 9 broadened entries of gloss.json against the line and against the notes as corrected in Pass 1; every one of the 450 known forms read against its use in this part to see whether the existing entry covers it; entry format (`—` shape, under 230 characters, typographic ’ only, no backtick, no line numbers, no "here"); every `__broaden__` entry checked as old entry whole + ` · ` + new reading. A coverage script finds no form of the part without an entry, no novel entry that is not in the part, no redefinition of an existing form. units.json was read once more in full; nothing further needed changing (no pass-2 edits to units.json, `t` untouched).

Counts: **0 high, 4 medium, 10 low** changes in gloss.json (5 new broadenings among them).

### Changes in gloss.json

**Medium**

| Form | What was wrong | What was done |
|---|---|---|
| ἴασον | "obscure epithet of Ἄργος (Peloponnesian Argos)": states as fact an identification the note (rightly) calls uncertain ("the Peloponnese or Greece in general"). | "obscure epithet of Ἄργος (meaning not certain)". |
| κληῗσιν (broadened) | Existing entry covers only thwart/rowing-bench (also thole-pin, key, bar); this part uses it for the hook or clasp of a brooch. | Old entry whole + " · also hook, clasp of a brooch: ’hooks’ (κληῗσιν ἐϋγνάμπτοις ’well-bent hooks’)". |
| πάροιθε (broadened) | Existing entry is "adv. of place" only; the part uses it of time (τὸ πάροιθε, "formerly") — and the new τὸ broadening points at it. | Old entry whole + " · also of time: ’formerly, before’ (τὸ πάροιθε)". |
| νοῆσαι (broadened) | Existing entry: "to glimpse, to notice"; this part has it as "think of, think out" (πεπνυμένα πάντα νοῆσαι). | Old entry whole + " · also ’think out, think of’ (πεπνυμένα πάντα νοῆσαι ’to think of all prudent things’)". |

**Low**

| Form | What was wrong | What was done |
|---|---|---|
| ἐϋγνάμπτοις | "epic -οις": -οις is the ordinary dative ending (Attic too). | Dropped the claim. |
| ἐνώμας | "iterative": the form is a plain contracted imperfect (the note says "a repeated action", not an iterative formation). | Dropped "iterative". |
| ἐπέσσευεν | "(= ἐπέσευεν)": not an Attic form of anything; the doubled σ is that of the aorist ἔσσευα. | "epic form with doubled σ (aor. ἔσσευα of σεύω)". Agrees with the note's "aorist". |
| εὐρυδάμαντι | "one of Penelope’s suitors": the part shows him among the Achaeans who send gifts, which is what the note says. | "one of the suitors". |
| μορόεντα, τρίγληνα | ", of earrings": pins a context into an entry that must be general to the form. | Removed from both. |
| μέγεθος | "’to your stature’": pins the possessive of one line. | "’to stature’". |
| ἐθέλωσιν | "ἤν = εἰ + ἄν" where the known-forms entry for ἤν says ἐάν. | "ἤν = ἐάν". |
| νεμεσσῶμαι (broadened) | Existing entry says "+ dat."; the part has the person in the accusative with an infinitive. | Old entry whole + " · also + acc. of the person and an infinitive: ’resent (you) for …’ (οὔ σε νεμεσσῶμαι κεχολῶσθαι)". |
| δέμας (broadened) | Existing entry: "accusative of respect"; at this line it is a direct object (or in apposition) after εἶδός τε. | Old entry whole + " · also neut. acc. sg., direct object or in apposition: ’body’ (εἶδός τε δέμας τε ’form and body’)". |
| τὸ (broadening by the drafter) | The new reading was glossed "’formerly’ (τὸ πάροιθε ’as before’)", two renderings at once. | Example now reads ’in former times’; old entry still whole. |

### Checked and correct (no change)

- Parses against the corrected notes: ἔκριναν (aor. 3 pl., with κε, general relative; the κε broadening says so), ἐπέσσευεν (aor.), ἀνέσει (future, or short-vowel subjunctive; the note and entry both say so), δέξασθ’ and γήμασθ’ (infinitives δέξασθαι, γήμασθαι, elided, used as imperatives; the entry for δέξασθ’ also says "not a plural δέξασθε"), ἕσπερον (known entry: masc. acc. sg.; the note makes it the accusative subject of the infinitive in tmesis), ἀπηύρα (known entry "aor. 3 sg., unaugmented", consistent with the note's person-in-genitive), δαινύατ’ (opt. 3 pl. mid.), λελῦτο (perf. opt. 3 sg. pass., "usual view"), ἐερμένον (masc. acc. sg., agreeing with ὅρμον, which the known entry gives as masc.), μορόεντα and τρίγληνα (neut. acc. pl., sense uncertain, said to be so), ἴδοιεν, πάθοι, φαίη, πέλοιτο, νεύοιεν, φαείνοιεν, ἀμφιπολεύοι (moods and tenses all match the notes).
- Εὐρυδάμας and Πείσανδρος "a suitor": supportable from the part (the Achaeans who send gifts after Antinous' proposal are the suitors, 18.290–301), and both entries say no more.
- The other 9 broadened entries are all old entry whole + " · " + a new reading, and each new reading is true of its use: γυναικῶν (περίεσσι γυναικῶν), κε (οἵ κε … ἔκριναν), μίμνειν (transitive "wait for"), τὰ (τὰ χέρεια), τὸ (τὸ πάροιθε), βίῃ (dative of respect), θέλγε (impf. 3 sg., unaugmented), ἐθέλωσι (general relative without κε), χρύσεον (masc. acc., with ὅρμον).
- Format: all entries under 230 characters, typographic ’ only, no backtick, no line numbers, no "here". Entries that give an example phrase (αἰνὸν ἄχος, ὅπῃ οἱ νόστος, κρίνω … οἵ κε) quote it as an illustration of the form, not as a pin to a line, as the existing glossary does.
- Known forms read against their use in the part (450): existing entries cover the use in every other case (checked especially: ἐπί/ἐπὶ in tmesis, ὄφρα + opt., ἵνα "where", κάτα/κατά in tmesis, ὅς κ’, τῷ "therefore" and "him", τοι, φώς "man", ἠῶ as object of "wait for", βασίλεια nom., οὐλομένης, ἀπηύρα).

### Refused

- λελῦτο "perf. opt." and ἀνέσει "fut., or short-vowel subjunctive": both are the usual views with the doubt stated; nothing firmer can be said from LSJ/Monro alone. Kept.
- ὁμοιΐου "(= ὅμοιος)": the equation is the lexicon's, and the entry says "sense disputed". Kept.
- ἴσθμιον "neck-band, necklace": the note says "something worn at the neck"; consistent. Kept.
- δαινύατ’ lemma δαίνυμαι (not δαίνυμι): the middle is the form used; the note names δαίνυμι as a heading. Kept.
- οὐλομένης (known entry "accursed, destructive, ruinous"): the unit renders "ruined"; the entry's gloss list allows it and the new-renderings row explains the choice. Not broadened.
