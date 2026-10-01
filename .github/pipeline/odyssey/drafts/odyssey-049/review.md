# review-049 — adversarial review of draft-049 (Odyssey 10.375–474)

## Pass 1

`t` untouched (asserted equal to the pre-review copy for all 59 units; units still tile the 99 lines, 455 → 457 as printed). Edits applied by script (`review_049_apply.py` plus one short follow-up trimming two notes), each an asserted single-substring replacement of `l`, `i` or `n`. 51 logged changes (43 distinct fields in 33 units; three fields were edited twice, and two notes were then re-trimmed): 1 high, 15 medium, 35 low. Mechanical checks re-run after the edits: `l` has one `\n` per `\n` in `t`; no `\n` in `i`; every note 25–110 words (units 438 and 472 were pushed over the band by my own additions and trimmed back); first-letter case of every `l`/`i` checked against the previous unit's closing punctuation; every ¶ of Murray (17) carries `p`; `mark` on the first unit of each of the nine speeches (378, 383, 401, 419, 423, 431, 443, 457, 472) and nowhere else; ‘ on each speech's first unit and ’ on its last in both `l` and `i` (378–381, 383–386, 401–405, 419–421, 423–427, 431–437, 443–445, 457–463/465, 472–474; the last two end with the `’` on units 463 and 472). The part's first unit is narrative and odyssey-048 ends in narrative (373, no open speech), so no ‘ or ’ crosses the boundary. Repeated lines checked against the published English (grep of every root odyssey-0NN.json): 10.382, 401, 430, 442, 466, 468, 474 and the lines of 428 and 444 agree with the packet and with every other published occurrence (468 also stands in 044 and 047, 382 in 017/018/044/047/048; all identical).

### Changes

| line | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| 10.378 | n | high | "τίφθ’ … with the τ written φ before the rough breathing of ἕζεαι": false. The rough breathing is that of οὕτως (the next word, not ἕζεαι), and it is πτ (from τίπτε) that becomes φθ, not τ alone. | Rewritten: τίφθ’ is τίπτε (= τί ποτε), elided before the rough breathing of οὕτως, which turns πτ into φθ. |
| 10.378 | n | low | "θυμὸν ἔδων … the standing phrase": claims usage elsewhere in the poem that this part cannot show. | "an idiom for brooding grief". |
| 10.375 | l | medium | "came and stood close beside me, and spoke winged words": "came" is not in παρισταμένη (a present participle), and the formula left the house `l` ("winged words he spoke"). | "close beside me standing, winged words she spoke:". (`i` keeps "came and stood", the table's `i` for the same type of phrase.) |
| 10.375 | i | low | "saw" for ἐνόησεν while `l` says "noticed". | "noticed". |
| 10.375 | i | low | "weighed down by strong grief": an image the Greek (ἔχοντα, κρατερόν) does not have. | "gripped by strong grief". |
| 10.375 | n | low | "agrees with the second με": there is only one με in line 376. | "the third, ἔχοντα, agrees with με and has κρατερὸν πένθος as its object". |
| 10.375 | n | low | "the words themselves begin in the next unit": the formula is in this unit; it is the speech that begins next. | "the speech itself". |
| 10.380 (δειδίμεν) | n | low | Parse incomplete (δειδίμεν is a perfect infinitive with present sense), and "the type that recurs throughout Homer" is a claim about the rest of the poem. | "the perfect infinitive of δείδω … with present sense … (= δεδιέναι)". |
| 10.381 | i | low | Capital "For" after the previous unit's semicolon. | "for". |
| 10.382 | n | medium | "προσέειπον … the first person of προσεῖπον without augment": false; the form carries its augment (shipped notes in 017/041/048 do not say it). | "the first person of the aorist whose third person is προσέειπε". |
| 10.383 | l | medium | "what man, for, who might be one …": γάρ stranded between two commas; reads as nonsense. | "for what man, who might be one with a sense of what is fitting,". |
| 10.388 | n | low | "‘holding the wand’": note contradicted its own `l`/`i` ("a wand"; ῥάβδον has no article). | "‘holding a wand’". |
| 10.388 | n | medium | ἐννεώροισιν "stands in apposition after it": wrong label; it is an adjective agreeing with σιάλοισιν. | "is an adjective agreeing with it". |
| 10.393 | i | low | Lower-case "and" after the previous unit's full stop. | "And". |
| 10.395 | l | low | Capital "And" after a semicolon. | "and". |
| 10.398 | n | medium | "ὑπέδυ is the unaugmented aorist": false; ὑπέδυ is ὑπ- + ἔδυ, augmented. | "the aorist of ὑποδύομαι". |
| 10.410 | i | medium | "field-dwelling calves": the table row (new-renderings) fixes the `i` of ἄγραυλοι πόριες as "calves that live in the fields"; also περὶ βοῦς ("around the cows") had become "to meet the cows". | "As when calves that live in the fields all frisk together around the cows of the herd, facing them, as they come to the yard, when they have had their fill of grazing;". |
| 10.415 | n | low | Note said θυμός is the subject while `l`/`i` render it as "in heart"; contradiction between note and layers. | Note now gives the literal construction (their heart seemed to them so to be) and says the English puts it as "in their hearts it seemed". |
| 10.418 | l | low | Lower-case "and" after unit 415's full stop. | "And". |
| 10.418 | i | low | Same. | "And". |
| 10.421 | i | low | Capital "But" after a semicolon. | "but". |
| 10.421 | n | low | Quotes "τῶν ἄλλων ἑταίρων"; the line prints ἑτάρων. | "ἑτάρων". |
| 10.422 | n | medium | "προσέφην is the unaugmented first person aorist": false; προσέφην (πρός + ἔφην) is augmented. | "a first-person past tense of πρόσφημι" (shipped 044 wording). |
| 10.425 | i | low | Capital "But" after a semicolon. | "but". |
| 10.425 | n | low | "as in the ‘sacred glens’ of the approach to the house": a cross-reference into another part, not checkable here. | "as again at 445" (checked: ἱερὰ … δώματα). |
| 10.427 | n | low | "the object being the food and drink of the line before" contradicts the noun reading the note itself offers one sentence earlier. | "with the food and drink of the line before in view". |
| 10.428 | n | low | "The raised point of the edition is here a full stop": garbled. | "The edition ends the sentence here with a full stop …". |
| 10.429 | n | low | "as later lines show": vague cross-reference. | "as line 441 shows" (checked: πηῷ). |
| 10.431 | n | low | δειλοί glossed "wretched, miserable"; the table keeps "wretched" for δύστηνος and fixes "miserable". | "‘miserable’, not ‘cowardly’". |
| 10.432 | i | medium | "pigs": table row σιάλοισιν keeps "swine" for σῦς (10.433); `l` already says swine. | "swine". |
| 10.432 | n | low | κεν … ποιήσεται labelled as one parse; the form may be future or a short-vowel aorist subjunctive. | Both stated. |
| 10.434 | i | medium | The relative clause οἵ κέν οἱ … φυλάσσοιμεν (434–436) was turned into a main clause ("and we should have to guard"), and "should have to" adds an obligation (ἀνάγκῃ is already "under compulsion"); the note says "we who". | "we who would guard her great house, even under compulsion, as the Cyclops did …". |
| 10.434 | n | low | "‘we should guard’". | "‘we would guard’" to match `i`. |
| 10.434 | n | low | θρασύς glossed "bold, rash"; the table turns "rash" down as a rendering. | "bold". |
| 10.437 | l | low | Capital "For" after a semicolon. | "for". |
| 10.438 | i | medium | "debated … whether to draw the sword …, strike off his head": makes drawing the sword part of the debate. σπασσάμενος is a participle (the sword is already out), as `l` and the note say. | "… I debated in my mind, drawing the long-pointed sword from beside my stout thigh, whether to strike off his head with it and bring it down to the ground …". |
| 10.438 | n | low | Note silent on the drawn sword and on what πηῷ agrees with; it was already 114 words (over the 110 band). | Rewritten, 100 words. |
| 10.443 | n | medium | "πὰρ is παρά elided": wrong; it is apocope. | "with its final vowel dropped (apocope, not elision)". |
| 10.443 | n | low | μένειν … ἔρυσθαι "infinitives of purpose": ἐάω takes the infinitive as complement ("let him stay and guard"). | Reworded as infinitives depending on ἐάσομεν. |
| 10.452 | i | low | Capital "We" after a semicolon; the Greek δέ continues the sentence. | "and we found them all feasting well in the halls." |
| 10.453 | n | medium | "εἶδον the unaugmented aorist": false; εἶδον is augmented (ἴδον at 414 is the unaugmented one, as the shipped notes say). | "the aorist of ὁράω (with its augment; ἴδον at 414 has none)". |
| 10.455 | n | low | "Murray prints no line 456" was too bare. | "Murray's numbering passes from 455 to 457: this edition prints no line 456, and the next unit begins at 457." |
| 10.457 (first unit) | n | low | The 456 gap falls between two units; only the earlier one said so. | One closing sentence added to the unit that begins at 457. |
| 10.463 | l | low | Lower-case "but now" after unit 460's full stop (the full stop is inside line 463). | "But now". |
| 10.463 | i | low | Same. | "But now". |
| 10.466 | n | medium | "‘and for us in turn’" and "the fixed phrase of 406": the shipped `l`/`i` (forced by the repeat rule) say "then", "our own", "lordly heart"/"proud hearts", while 406 carries the house "manly spirit"/"proud spirit". The note contradicted its own layers and hid the two renderings of one phrase in one part. | The note says the shipped English is kept (ἡμῖν read "our own", αὖτ’ "then") and that 406 has the house rendering, 466 the shipped one. |
| 10.466 | n | medium | (second edit of the same note) "the fixed phrase of 406". | As above. |
| 10.469 | l | low | Capital "But" after a semicolon. | "but". |
| 10.469 | i | low | Same. | "but". |
| 10.472 | n | medium | δαιμόνιε: note picks "said here with gentle reproach", while the table row says the force is uncertain and turns down "silently picks the gentle sense". | "whether it is gentle reproach or plain urging is not known". |
| 10.472 | n | low | The shipped 474 `i` "native land" (kept by the repeat rule) sits two lines after "fatherland" for πατρίδος αἴης and is not flagged. | One clause in the note says so. Note then trimmed to 106 words. |

### Considered and refused

- **θυμὸς ἀγήνωρ at 406 vs shipped 10.466.** The table row (4.548) fixes "manly spirit" / "proud spirit"; the shipped 006 unit at 466 has "lordly heart" / "proud hearts" and the validator makes unit 466 identical to it. Left as is: 406 follows the table, 466 follows the shipped text; the difference is now stated in the note at 466 (change above). Aligning 406 to "lordly heart" would contradict the table and every later θυμὸς ἀγήνωρ.
- **"native land" at 474.** Kept: the line stands in shipped odyssey-030 (`i` "your own native land"), the table's πατρίδα γαῖαν row excepts exact repeats, and the packet says to reuse the published wording. Flagged in the note (change above). 472 stays "fatherland".
- **δαιμόνιε "Strange man" in both layers.** Kept; it is the table row. Only the note was changed.
- **457a "no longer" note.** Checked: μηκέτι + present imperative ὄρνυτε = prohibition ("stop raising") is correct; θαλερόν cross-refers truly to 409; `l` "No longer now …" and `i` "… no more" agree. No change.
- **436 relative clause.** The clause is οἵ κέν οἱ … φυλάσσοιμεν (434) with the ὅτε-clause running to 436; the grammar of the note was right, `i` was not (changed above). The second οἱ (435, "his") is glossed by `l`/`i` and left unglossed in the note: refused as too small.
- **ἔρξ’ (434–435).** Could be ἔρδω or ἔργω; the note says ἔρδω with the object understood. Refused: ἔρδω is the usual reading and nothing in `l`/`i` depends on it.
- **"For you" (419 `l`).** The usual crib for the causal dative; the note explains ("at you having come home"). Refused.
- **"with my own eyes" / "their own eyes" (386, 387, 414).** The "own" is English idiom for ἐν ὀφθαλμοῖσιν, not a different force. Refused.
- **"streaming forward in tears" (414).** Table-fixed wording for ἔχυντο; the note already says the Greek does not name where they streamed. Refused (low).
- **"which before had grown the ruinous drug" (393 `l`).** English reads ambiguously, but the Greek order is kept deliberately and the note names the subject. Refused.
- **First πρίν at 384 rendered "before" in `l`.** In Greek it is probably "sooner" (πρίν … πρίν = sooner … than); `l` is a crib and `i` resolves it correctly. Refused.
- **"now at last" (472 `i`) for ἤδη νῦν ("already now").** Slight shift of force but fits the year just passed. Refused (low).
- **"eating your heart out" (378 `i`).** Ordinary English idiom, a literal match to θυμὸν ἔδων; no sign of a remembered rendering. Refused.
- **Capital "There" at 467 (`l`).** The preceding shipped `l` (unit 466) ends in a semicolon only because it was shipped mid-sentence; the Greek has a full stop there. Refused.
- **κατὰ … χέοντας tmesis (409).** Not mentioned in the note; nothing false is said and the table drops κατά in the house rendering. Refused.
- **Scansion.** The packet flags none; nothing scanned by hand and no metrical sentence added.
- **10.456.** Murray's omission is stated in the notes of the unit ending at 455 and of the unit beginning at 457 (change above).

## Pass 2

Re-read `units.json` as edited in Pass 1 and, for the first time, `gloss.json` (127 new entries and 22 broadened ones). `t` again asserted untouched. The gloss was checked entry by entry against the line(s) where each form stands, and the 330 forms taken from the existing glossary were checked for readings the old entries do not cover. Mechanical checks: every form of the part has an entry (existing glossary, new, or broadened); no new entry reaches 230 characters; no ASCII apostrophe or backtick; no line numbers, "line" or "here"; every broadened entry begins with the old entry whole followed by ` · `; all notes 25–110 words.

### Changes

| where | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| gloss ἔτραφεν (10.417) | entry | medium | Hedged "aor. 3 sg./pl."; the form is the epic third plural (-εν for -ησαν) with ἐγένοντο, "they were reared". | "intrans. aor. 3 pl., epic -εν (= Attic ἐτράφησαν): ’they were reared’". |
| 10.415 | n | medium | Note called ἔτραφεν "plural in sense": no parse. | "the epic third plural (= ἐτράφησαν) of the passive aorist of τρέφω"; two redundant glosses trimmed to stay under 110 words (my own Pass 1 addition had pushed the note to 116). |
| gloss ἔρξ (10.435) | entry | medium | "ἔρξ’ = ἔρξε, epic for ἔρεξε": ἔρξε is the aorist of ἔρδω, not a shortening of ἔρεξε. | "ἔρδω (= ῥέζω) — do, act; aor. 3 sg., elided (ἔρξ’ = ἔρξε): ’did’". |
| gloss τανύηκες (10.439) | entry | medium | "long-pointed or long-edged … disputed": offers the sense the table turns down and says nothing of the note. | "long-pointed (second element ἀκ- ’point’, sense not fully certain)". |
| 10.438 | n | low | The note gave ἀκ- ‘point’ as fact; matches the new gloss now: "the second element is not fully certain". | Added. |
| gloss ἀμφιθέουσι | entry | medium | "uncontracted (= Attic ἀμφιθέουσι)": false and empty; θέω does not contract ε+ου in Attic either. | Parse kept, claim removed. |
| gloss ἱκοίατο | entry | low | "= Attic ἵκοιντο": ἵκοιντο is not Attic. | "epic -οίατο (= -οιντο)". |
| gloss ἀνέῳξε | entry | low | "ἀνοίγω (epic for ἀνοίγνυμι)": ἀνοίγω is the other present, not an epic form. | "ἀνοίγνυμι (also ἀνοίγω) …". |
| gloss δαιμόνι | entry | medium | "chiding or wondering" picks between senses the table says are uncertain. | "the force, gentle or chiding, is uncertain". |
| gloss δειλοί | entry | low | Gloss and example said "wretched"; the table's word for δειλός is "miserable". | "miserable, wretched, poor … ’oh miserable ones’". |
| gloss ἰχθυόεντι | entry | low | "fishy": the table turns it down (wrong connotation). | "teeming with fish". |
| gloss ἱμερόεις | entry | low | "lovely, desirable": the table turns down "desirable"; the sense here is longing. | "causing longing, full of longing". |
| known ἀνήιον (10.446) | broadened | medium | Old entry parses only "impf. 1 sg."; here it is 3 pl. ("they went up"). | Old entry whole + ` · also impf. 3 pl.: ’they went up’ (…)`. |
| known ὁ (10.436) | broadened | low | Entry gives only the pronoun reading; ὁ θρασὺς Ὀδυσσεύς is article-like. | Old entry whole + ` · also article-like …`. |
| known αὐτῶν (10.391) | broadened | low | δι’ αὐτῶν, plain "them" after a preposition, is not among the readings (the old entry has only a neuter, a possessive and intensive uses). | Reading added, old entry whole first. |
| broadened τοὺς (10.449) | entry | low | New clause "article-like with a noun: τοὺς ἄλλους ἑτάρους" duplicates the old clause "demonstrative with a noun … τοὺς ἄλλους … ἑταίρους". | Broadened entry removed (old entry stands). |

### Considered and refused

- **ἔρξ’ (judgement call).** ἔρξε from ἔρδω ("did", object understood) is kept in the note and the gloss; the alternative from ἔργω ("shut in") is not stated, since I know of no firm ancient support and nothing in `l`/`i` depends on it.
- **ἔτραφεν as 3 sg.** Refused: with ἐγένοντο the plural reading is the standard one; the unit's English ("they were reared") already agrees.
- **τανύηκες.** Sense kept as the table's "long-pointed", and now flagged as not fully certain in both note and gloss; the table row's avoided "long-edged" is mentioned only as the alternative in the gloss' hedge, not as a gloss.
- **ἐπεπείθετο (406, 466).** The existing entry says "plpf. 3 sg. with impf. sense" while the unit notes say "imperfect middle". The two agree in sense and the entry is shipped; I am not certain enough of the parse to broaden or contradict it. Left.
- **προσέειπον "aor. of πρόσφημι" (existing entry).** Odd lemma, but shipped and used by many parts; not touched.
- **κρατερὸν masc./neut., μέσσαυλον gender, κόπρον "dung".** Checked against 376, 435, 411: all acceptable.
- **δοκέω "unaugmented", στεναχίζετο/τελέσθη "unaugmented", κονάβιζε.** Checked against the forms: all true.
- **τε in ἵνα τ’ ἔτραφεν and ὡς εἴ τ’ (417, 420).** Covered by the existing "epic τε" readings; no broadening.
- **Existing entries for the many particles, prepositions in tmesis (κατ’ ἕζεαι, ἐκ … ἔλασεν, ἀμφὶ … βάλεν, σὺν … εἵπετ’, περὶ … στεναχίζετο), ὃς (relative at 383, 393), οἵ (relative 434), οἱ (all six places), πὰρ (apocope, + dat.).** Each reading is already present; no change.
- **My Pass 1 `l`/`i`/`n` edits.** Re-read for new errors (i of 434 "we who would guard", i of 438, `l` of 375, 383; notes 1, 5, 28, 49): none found beyond the two note-length and ἔτραφεν points above.
