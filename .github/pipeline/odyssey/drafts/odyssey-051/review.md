# odyssey-051 (11.1–99) — review, pass 1

Scope: units.json, packet.md, new-renderings.md, checked against conventions.md, odyssey-001, the published parts, and the build and validator code. `t` untouched (checked: every `t` identical before and after; every `l` keeps its line count). gloss.json not read or touched. Notes that exceed 110 words after editing: lines 6, 38, 44, 62, 74 (all under the validator's 130 hard line; 6, 38, 44 and 62 were already 110–115 before).

## Changes (line · field · severity · what was wrong · what was done)

| line | field | severity | wrong | done |
|---|---|---|---|---|
| 57 | l | moderate | Odysseus's speech opens here (`mark` on this unit) but `l` lacked the opening ‘ that `i` has; published parts carry the marks in both layers | added ‘ |
| 58 | l | moderate | last unit of the speech: `l` lacked the closing ’ that `i` has | added ’ |
| 58 | i | low | “have got here” renders the aorist ἔφθης as a perfect | “On foot you got here before I did in my black ship.’” |
| 6 | n | moderate | said νεὸς κυανοπρῴροιο is “the Ionic genitive of νηῦς with the epic ending -οιο”; -οιο belongs to the adjective only, νεός is the plain Ionic genitive | split the two statements |
| 9 | n | moderate | said the singular ἴθυνε is natural “when the first subject is the nearer”; in ἄνεμός τε κυβερνήτης τ’ ἴθυνε the first subject is the farther | now says only that it agrees with one of the two subjects |
| 13 | n | low | “imperfect or aorist” for ἵκανε; ἱκάνω has the imperfect only | “imperfect” |
| 12 | n | low | “wherever it is used” asserts the line's use across the poem, which this part cannot show (conventions, Notes) | trimmed |
| 42 | n | low | “as with sounds elsewhere in the poem”, same rule | trimmed |
| 44 | n | low | note had ἑτάροισιν as “the object of ἐκέλευσα” and then spoke of an “unexpressed ‘them’” as subject of the infinitives, contradicting itself | now: ἑτάροισιν is the dative; the doers of the infinitives are unexpressed and δείραντας agrees with them; one redundant clause cut for length |
| 74 | n | moderate | κακκῆαι explained as “κατακῆαι with the κ assimilated”; what assimilates is the τ (κατὰ κῆαι) | corrected |
| 74 | n | low | ἀνδρὸς δυστήνοιο called “in apposition to the owner of the mound”; it is a genitive with σῆμα | corrected |
| 74 | i | low | “all that I have” after “my armour” reads as all possessions; ἅσσα μοι ἔστιν is relative to the armour | “with whatever armour I have” |
| 38 | n | low | οὐτάμενοι called “aorist passive participle”; the form is aorist middle, passive in sense | now says both |
| 62 | i | low | “by the long ladder” for ἰὼν ἐς κλίμακα μακρήν; the same words are shipped at odyssey-050 as “making for the long ladder” and the packet asks for the shipped wording as far as the sentence allows | “to go back down, making for the long ladder” |
| 62 | n | low | scansion flag, line 64 (see below) | added one sentence; also cut the first sentence (“a man drunk and asleep on the roof”), which no line of this part states, and which kept the note under 130 words |
| 32 | i | moderate | “and, apart from the rest, to sacrifice to Tiresias…” leaves a bare infinitive after the previous unit's “I would sacrifice…”, losing the future-infinitive promise (ἱερευσέμεν) | “and that, apart from the rest, I would sacrifice to Tiresias alone a sheep…” |
| 69 | l, i, n | moderate | “well-wrought ship” for ἐυεργέα νῆα; the table (ἐυεργής, 9.279) and odyssey-038/041 ship “well-made ship”, and the table keeps “well-wrought” for τετυγμένος | “well-made” in all three |
| 84 | l, i, n | moderate | “holy Ilios” for Ἴλιον ἱρήν; ἱρός is the Ionic ἱερός, shipped “sacred” (odyssey-011 “sacred Sounion”, -029, -013), and the table reserves “holy” for ἠγάθεος | “sacred Ilios” in all three |
| 88 | i | low | “before I had inquired” for πρίν…πυθέσθαι; the same clause at 50 and 89 is shipped “until … inquired of Tiresias” and the note says the English is the same | “until” |
| 88 | n | low | προτέρην explained as “she is the first to be kept off”, which is not what the word says (“first, ahead of Tiresias”) | corrected |
| 79 | n | high | note said μιν is “here Elpenor” while `l`/`i` say “she … her”; it never told the reader the English was wrong | rewritten (see issue (a)) |

Also changed outside units.json: new-renderings.md. Deleted two rows: ἐυεργὴς νηῦς “well-wrought ship” (contradicts the existing table row, which fixes “well-made”; see line 69) and εὐρυόδειος χθών (an identical row already exists: χθὼν εὐρυόδεια, 3.453, “the wide-wayed earth”). Without this, the publish step would copy a contradicting row and a duplicate into the table.

## The three flagged issues

**(a) Line 79, “she / her” for Elpenor.** Truly enforced, with no exemption. `validate_odyssey.py` check 6 compares, for every unit of this part, `letters_only(t)` with each earlier published unit; on a match it fails unless `l` and `i` are identical (`seen` is filled from published parts only; there is no allow-list or flag). The build does not touch it. The only ways round it would be to cut the units differently so the Greek no longer matches (folding line 79 into the speech unit at 80), which breaks the model's structure (a narration unit, then a `mark` unit) and would be publishing around a gate, so refused. Precedent: odyssey-044 (line 522, the Cyclops) and odyssey-047 (line 270, Eurylochus) shipped this same English with a note saying so. Done: kept the English; note rewritten the same way (Greek is gender-neutral; μιν is “him” or “her”; the English is the published wording, wrong here, read “he/him”). Suggest the caller add a QUESTIONS.md entry that lines 17.375-type formula units cannot take the speaker's gender; a gendered variant formula or a validator exemption needs an owner decision.

**(b) Line 64 scansion (καταντικρύ).** Scanned by hand: ἀλ|λὰ κα (dactyl) · ταν τι (spondee) · κρὺ τέ γε (dactyl) · ος πέ σον (dactyl) · ἐκ δέ μοι (dactyl) · αὐ χήν. καταντικρύ is ⏑–⏑– and cannot sit in a hexameter as it stands: the ι of τι must be read long (and κρὺ then falls as the longum of foot 3). The published line 10.559 (same words, πέσεν) scans the same way. The irregularity is real; one sentence added to the note of the unit that carries it (line 62 unit; the second half of the line, ἐκ δέ μοι αὐχήν, is regular but for the ordinary correption of μοι, which needs no comment).

**(c) Line 56 vs the house table.** The line's English is shipped at odyssey-019 as “and I spoke to him and addressed him with winged words” (`l` “winged words I addressed to him”), and the draft has it exactly. The table row for ἔπεα πτερόεντα προσηύδα (3rd person) is “spoke winged words”, and the προσηύδων row at 9.363 says προσαυδάω keeps “spoke” and “addressed” is reserved for προσέειπε/προσέφη. So the shipped wording and the table disagree. Kept the shipped wording: the packet and runbook require the shipped English for a repeated line, and the unit as a whole (lines 55–56) is not a validator match, so it is a rule-of-the-house choice, not forced; changing it would split one formula into two renderings between parts. Not a draft error. Suggest a QUESTIONS.md line to settle which one the table keeps.

## Findings considered and refused

- Quotation style: speeches use single ‘ ’ marks as in odyssey-044/049/050 (the whole tale is Odysseus's narration); correct. Speech marks: ‘ on 57, ’ on 58; ‘ on 60, ’ on 77; 80 both; ‘ on 92, ’ on 96; `mark` on 57, 60, 80, 92. Speech by Tiresias begins at 99 and runs into odyssey-052: no mark opened here, correct. odyssey-050's last unit (573) is narration, so nothing is open on entry.
- Paragraph flags `p`: match every ¶ in the packet (1, 13, 23, 51, 57, 59, 79, 81, 84, 90, 97).
- βαθύρροος “deep-flowing”: the table avoids “deep-flowing” as a rendering of βαθυδίνης, but not as a reserved word; βαθύρροος is literally ‘deep-flowing’. Kept.
- πυγούσιον “a cubit long” with a note on “elbow to knuckle”: matches the table row (10.517). Kept.
- ἄπισχε “imperative of ἀπέχω” (48, 95): ἀπίσχω is a present stem of the same verb. Kept.
- “same verb as the imperative above” for ἀναχασσάμενος (97): same base verb χάζομαι, different preverb. Kept.
- The note at 7 saying κεκαλυμμένοι “agrees with the men”: true in sense (nominative picking up the genitive ἀνδρῶν). Kept.
- Notes that refer back to Circe's instructions in odyssey-050 (lines 13, 16, 22, 23): the cross-references were checked against the packet's published lines and are true.
- Line 31, `i` “an evil lot from some power, and immense wine, did me harm”: stiff word order but follows Greek order and the new rows. Kept.
- No remembered English found in `i`; no modern translator named.
- Not done, for the second pass: gloss.json (not yet present when this pass ran).

---

# Pass 2

Independent pass: every note label, Greek to `l` word by word, `l` against `i`, remembered English, quotation and `mark` fields, all 108 novel and 11 broadened gloss entries checked against the lines where each form occurs (and the 371 known forms read for coverage), and pass 1's own edits re-checked. Pass 1's edits were all found correct (the line 6, 9, 13, 38, 44, 58, 62, 69, 74, 84, 88 changes and the two deleted new-renderings rows: ἐυεργής 9.279 “well-made” and χθὼν εὐρυόδεια 3.453 both stand in the conventions table as pass 1 said). The scansion of line 64 was re-done by hand and agrees with pass 1 and with the shipped `sc` of the same line at odyssey-050 (foot 2 ταν–τι with the ι read long, κρὺ the longum of foot 3).

## Changes (line · field · severity · what was wrong · what was done)

| line | field | severity | wrong | done |
|---|---|---|---|---|
| 14/15, 26/28, 34/36, 42/43, 97/98 | t (boundary only) | high | the build refused (“does not end at punctuation”, units 7, 13, 17, 20, 49): five mid-line cuts sat one word off the punctuation they say they stop at, so unit 14 ended “… κεκαλυμμένοι· οὐδέ”, unit 26 “… τὸ τρίτον αὖθ’”, unit 34 “… ῥέε δ’ αἷμα”, unit 42 “… ἰαχῇ· ἐμὲ”, unit 97 “… ἐγκατέπηξ’. ὁ”. The `l`, `i` and `n` of all ten units already assume the right cut (each note says the unit ends or begins at the dot) | moved one word across each of the five joins (οὐδέ to unit 15; ὕδατι· to unit 26; κελαινεφές· to unit 34; ἐμὲ to unit 43; ὁ to unit 98). No character of the text added, dropped or changed: the non-space characters of all `t` in order are identical before and after (checked by script), and the build and the validator now accept them. This is the only touch of `t`, made because the build cannot run without it; flagged here so the caller can see it |
| 15 | l, i, n | moderate | “the radiant Sun … his rays” for ἠέλιος φαέθων; the same words are shipped at odyssey-026 as “the shining sun … its rays”, and no table row fixes another word, so the first ratified rendering wins; the new-renderings row claimed it was new | “the shining sun … its rays” in all three; new-renderings row rewritten (follows odyssey-026, notes that the table’s “shining” for φαεινός is kept apart by the noun) |
| 17 | l, i, n | moderate | “starry heaven”, “from heaven” for οὐρανὸν ἀστερόεντα, οὐρανόθεν; the identical phrase is shipped at odyssey-044 as “to the starry sky” | “starry sky”, “from the sky”; new-renderings row ἀστερόεις οὐρανός changed to match |
| 17 | n | moderate | προτράπηται called “the aorist passive subjunctive”; -ηται is the ending of the second-aorist middle (ἐτραπόμην) subjunctive, the passive would be τραπῇ | “aorist middle subjunctive” |
| 17 | n | low | δειλοῖσι βροτοῖσι called “a stock phrase”: nothing shipped or in this part shows it | now says what the form is |
| 11 | n | moderate | τέταθ’ asserted to be τέταται, perfect passive; it is an elided τέταται or τέτατο (θ for τ before the rough breathing of ἱστία), which the gloss already admits | note says so and that the ending is uncertain |
| 9 | n | low | ἴθυνε called “the aorist” while the gloss says imperfect and the English is imperfect; the form is both | “imperfect or aorist; the form is the same” |
| 14 | n | low | κεκαλυμμένοι said to “agree with the men”, but ἀνδρῶν is genitive and the participle nominative | “nominative masculine plural, so in sense it goes with the men” |
| 24 | l | low | “as much as a cubit long”; the table’s πυγούσιον `l` is “a cubit’s length” (odyssey-050 ships it) | “as much as a cubit’s length” (`i` “a cubit long” was right) |
| 32 | n | low | “παμμέλαν’ is πάμμελαν”; the elided word is παμμέλανα (as odyssey-050 and the glossary say) | corrected |
| 36 | l, i, n | low | “of the dead who had died” for νεκύων κατατεθνηώτων; shipped at odyssey-050 as “of the dead, of those who have died” | “of the dead, of those who had died” (tense follows the narration); note and new-renderings row matched |
| 42 | l | low | “who in crowds around the pit” renders πολλοί (“many”) as “in crowds” and the note says “many of them” | “who many around the pit were roaming” |
| 43 | n | moderate | “Odysseus is alone at the pit”: contradicts lines 23 and 44–46, where Perimedes, Eurylochus and the companions are there | sentence cut |
| 81 | l | moderate | “and the phantom … much speaking” leaves ἀγόρευεν (finite imperfect) as a bare participle after “sat” | “much was speaking” |
| 87 | i | low | “When I saw her I wept, and I pitied her” does not echo line 55 (“Seeing him, I wept and pitied him in my heart”), though the note says the line echoes it | “Seeing her, I wept and pitied her in my heart;” |
| 88 | n | low | ἀχεύων called the participle of ἀχέω; it is ἀχεύω (the house glossary says so) | corrected |

### gloss.json (every parse checked against the lines; 108 novel + 11 broadened)

| form | severity | wrong | done |
|---|---|---|---|
| τέταθ | moderate | “plpf. pass. … (3 pl. with ἱστία)”: a 3 pl. would keep its ν (τέταντ’); the elided form is τέταται or τέτατο | rewritten: perf. 3 sg. τέταται or plpf. 3 sg. τέτατο, τ shows as θ before a rough breathing |
| προτράπηται | moderate | “aor. subj. 3 sg. pass.”: -ηται is the middle subjunctive | “aor. subj. 3 sg. mid.” |
| γουνούμην | moderate | “uncontracted epic form”: the form is contracted (ο+ο) and unaugmented | “contracted and unaugmented (= ἐγουνούμην)” |
| ἴθυνε | low | “impf. 3 sg.” only; the aorist has the same form | “impf. (or aor.) 3 sg.” |
| κατόπισθε | low | “here with a gen.” (the word “here” is not allowed, and it pins the entry to a line) | “adv., or prep. + gen.” |
| σχήσεις | low | “fut. 2 sg. σχήσω” reads as if σχήσω were 2 sg. | “fut. 2 sg. (σχήσω)” |
| βόθρου | low | “gen. of separation after ἀποχάζεο” pins the entry to a word in a line | “… after verbs of drawing back” |
| ὄπιθεν | low | known entry (“from behind, hereafter”) does not cover the static “behind” of τῶν ὄπιθεν (66) or ἰὼν ὄπιθεν (72) | added to `__broaden__`: old entry whole, then “ · also ’behind’ …” (two readings) |

All other parses were checked and stand (including the homograph ζωὴν, the broadened μή, ἐπὶ, ἐφ, ἐγώ, ἔστιν, ἢ, ἱερευσέμεν, ἄκλαυτον, χλωρὸν, πολιῆς, ἔρεσσον, each of which is the old entry whole plus the new reading, no ASCII apostrophe, no line number, all novel entries under 230 characters). The 371 known forms: every use in this part is covered by its existing entry except ὄπιθεν.

## Findings considered and refused

- Line 79 “she / her” for Elpenor (pass 1 issue a): agreed. validate_odyssey.py check 6 fails any unit whose Greek (letters only) equals a published unit unless `l` and `i` are identical, with no exemption; the Greek of the whole sentence is the same as odyssey-017, and a cut at the comma would break the unit rule. The note already says the English is wrong and why. conventions.md says the pronoun tracks the speaker’s sex for ὣς φάτο, so this is a gate problem to put in QUESTIONS.md, not a draft error.
- Line 56 and the προσηύδων row (pass 1 issue c): agreed; the shipped wording (odyssey-019 and -050 both ship “I spoke to her/him and addressed him/her with winged words”) is kept.
- Line 2 “heavenly salt-sea” against the shipped “heavenly brine” (odyssey-019, -010): the table (rows ἅλα δῖαν and ἁλί) fixes “heavenly” + “salt sea” from odyssey-024 on. Kept.
- Line 18 γαῖα “earth” (the table’s γαῖα row “country” is for the list γαῖαν … δῆμον … πόλιν): the word here is the earth under the sky; kept.
- Line 17 οὐρανός “sky” while other parts ship “heaven” or “sky” as they please: only the identical phrase (044) was matched.
- Line 20 “which Circe had pointed out” (aorist φράσε in a past perfect): English needs it; the note says “pointed out”. Kept.
- Line 29/50/89 repeated lines: wording follows the packet’s published lines as far as the sentence allows (checked line by line).
- Line 53 “Homer’s way of naming the worst fate of a dead man” and 34 “the epithet usually goes with Zeus”: the first is an interpretation of lines 54 and 72 of this part, the second is shown by the shipped κελαινεφέι Ζηνί (044); kept.
- Line 58 “On foot you got here before I did in my black ship”: built from ἔφθης … ἢ ἐγώ and σὺν νηί; nothing in it was recalled. Kept.
- Line 69 “back to the island” in `i` (no “back” in the Greek): context (he came from Aeaea); kept.
- Quotation marks: single ‘ ’ as in the shipped Odysseus-narrated parts (044, 049, 050); ‘ on 57, 60, 80, 92 with the `mark` fields; ’ on 58, 77, 80, 95; Tiresias’s speech opens at 99 and runs into odyssey-052 (no mark opened). `p` flags match every ¶ in the packet.
- Scansion of line 64: real irregularity, one sentence in the line 62 unit’s note (pass 1); verified.

## Build and validator

`python3 build_odyssey.py odyssey-051` refused before the `t` repair (five units not ending at punctuation); after it: BUILT odyssey-051: 51 units, 99 lines, 108 new glossary forms (10188 total), 12 broadened (the known broadening list now holds 12 with ὄπιθεν); scansion lines needing a person: line 64 (UNRESOLVED, settled above). `python3 validate_odyssey.py odyssey-051`: PASS, 51 units, 99 lines, glossary 10188, no WARN.
