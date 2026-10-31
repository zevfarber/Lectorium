# Review, iliad-120 (18.410–508)

Two passes. Pass 1: every note's grammatical labels, positional claims and cross-references (checked against the lines here, iliad-005, -024, -034, -038, -047, -053, -087, -099, -116, -118, -119 and odyssey-009, -022, -024, -047, -065); Greek → `l`; `l` ↔ `i`; remembered English; repeated lines against the packet and the published files; house renderings against both tables; quotation marks, `mark`s and `p`s. Pass 2: `gloss.json` (written by the glosser while pass 1 ran), every parse against its line, and the known forms of this part against their existing entries. `t` untouched throughout (asserted by the edit scripts; the units' `t`, joined, still equal the packet's lines). `l` keeps the line division of `t` in every unit; no `\n` in any `i`; no ASCII quotes.

Checked and sound: `p` on every ¶ line (410, 428, 462, 468, 478, 483, 490). Speeches: Hephaestus 424–427 (“ at 424, ” at 427), Thetis 429–461 (“ 429, ” 461), Hephaestus 463–467 (“ 463, ” 467), each with `mark` on its first unit; iliad-119 closes Hephaestus' speech to Charis with ” at 409, so 410 rightly opens in narrative; 508 ends in narrative and iliad-121 is not yet published. Whole units with the same Greek as published Iliad units are identical to them in `l` and `i`: 424–425 (iliad-119), 426b–427 (iliad-087), 428 (iliad-005), 437b, 438–440a, 440b–441, 442–443 (iliad-116), 462 (iliad-119). Repeated lines inside larger units: 423 (iliad-038/-119 formula, "her"), 444–445 (iliad-099, third person), 457 (odyssey-009), 463 (odyssey-065), 468 (iliad-024 pattern), 487 (odyssey-024, 5.273, which prints ἄμαξαν lower-case), 488–489 (odyssey-024, final stop only): all agree. Cross-references hold: 397 χωλόν, 376 the tripods, 380 and 1.608 ἰδυίῃσι πραπίδεσσι, 409, 4.292, 9.121, 14.195–196, 16.56/58, 18.26–27, 18.56, 18.385–386, 18.393, Od. 5.89, 5.273–275.

## Hand scan of 493 (the only flagged line)

ἠγίνεον ἀνὰ ἄστυ, πολὺς δ’ ὑμέναιος ὀρώρει. Sixteen syllables: ἠ γῑ (– –) | νε͜ον ᾰ νᾰ (– ⏑ ⏑; εο in synizesis, the final ν going over to ἀνά; νὰ stays short in hiatus before ἄστυ, which had a digamma) | ἄσ τυ ‖ πο (– ⏑ ⏑, feminine caesura) | λὺς δ’ῠ μέ (– ⏑ ⏑; λύς long by position) | ναι ος ὀ (– ⏑ ⏑) | ρώ ρει (– ×). No other division fits: without synizesis the second foot would open on a short syllable. The scanner gives the same pattern.

The two licences are not irregularities. Synizesis of -εον in this verb is ordinary Homeric prosody. The "long scanned short: ὑμέναιος" is the scanner's doing: its quantity hints mark every word beginning ῡμε- long (the hint is for ὑμεῖς, ὑμέτερος), and ὑμέναιος is caught by it; the line needs its υ short, and nothing in the poem says it is long (it is the only Homeric instance). So no "metrically irregular as transmitted" sentence is wanted. The drafter's sentence at 491 ("ἠγίνεον is sounded as three syllables, its εο run together (synizesis), and ὑμέναιος has its first syllable short; read so, the line scans regularly") is true as written and claims no irregularity; kept unchanged.

## Changes, pass 1 (units.json)

| Line | Field | Severity | Was wrong | Done |
|---|---|---|---|---|
| 426 (αὔδα ὅ τι φρονέεις·) | l, i, n | moderate | Took the Odyssey's English ("Say what you have in mind;" / "Tell me what is on your mind;", odyssey-022, 5.89), but the Iliad has already shipped this half-line at 14.195 (iliad-087) as "speak what you have in mind" in both layers, and inside the Iliad the same Greek takes the same English. The packet missed the line because 14.195 is split across two published units. | `l` and `i` "Speak what you have in mind;". Note now says it keeps the English of 14.195 and gives the Odyssey's wording. new-renderings.md: added to "Reused" and to "Departures from Odyssey English" (validator will warn against odyssey-022, expected). |
| 483 (ἐστεφάνωται, 485) | l, i, n | moderate | "is crowned", with "is wreathed" listed as avoided. The Iliad has shipped ἐστεφάνωται as "is wreathed" (5.739, iliad-034) and the Odyssey the same (10.195, odyssey-047); the existing glossary entry also says "is wreathed round". | `l` and `i` "is wreathed"; note "ring the sky like a wreath", with the 5.739 cross-reference. new-renderings.md row rewritten. |
| 461 | n | moderate | "κεῖται … and the speech ends on it": false; the speech ends on θυμὸν ἀχεύων. | "κεῖται ‘lies’ is the same verb Thetis used of Peleus at 435: father and son both lie helpless." |
| 429 | l | minor | "Cronus’ son Zeus" for Κρονίδης Ζεύς; the Iliad's `l` for this order is "the son of Cronus, Zeus" (8.141, iliad-047), and the table's Κρονίδης is "son of Cronus". | "as the pains that to me beyond all the son of Cronus, Zeus, has given?" `i` was already right. |
| 429 | n | minor | τοσσάδ’ given as "= τοσαῦτα"; the form is epic for τοσάδε. | "(= τοσάδε)". |
| 424 | n | minor | "the very words his wife Charis used at 424–425 = 385–386": garbled. | "used at 385–386". |
| 446 | n | minor | φρένας ἔφθιεν given only as intransitive + accusative of respect; ἔφθιεν is also taken as transitive here ("was wasting his heart"). | Alternative added; `l`/`i` keep the intransitive reading. |
| 448 | n | minor | "Agamemnon’s list at 9.121, which began περικλυτὰ δῶρ’ ὀνομήνω": 9.121 introduces the list, which begins at 9.122. | "the words with which Agamemnon introduced his list at 9.121". |
| 450 | i | minor | "many men" for πολὺν … λαόν: the table's λαός of an army is "troops" in `i`, and "men" is among the avoided words (2.577 row). | "many troops". |

## Considered and refused (pass 1)

- **ἔρρων 421, "going painfully" / "made his painful way"** against the table's ἔρρων "coming here wretchedly" (8.239). Accepted. The 8.239 row is pinned to ἐνθάδε ἔρρων, where the verb carries ill fortune; here it describes the lame god's walk, and the old lexica take it of this line as "limping, going with difficulty". The departure is recorded in new-renderings.md with the reason, and the note gives both senses. A broadening was added to the gloss (pass 2) so the glossary does not say only "wretchedly".
- **426b–427** keep iliad-087's English (with ”), which differs from odyssey-022 only by the closing quote. Correct.
- **432 `i` "he subdued me to a man"**: the table's δαμάζω is "subdue" in `l` and "overcome" in `i`, and "overcame" is kept for the victorious sense (6.159 row). For a goddess given in marriage "subdued me to a man" is the plain sense, and the note explains the image. Kept.
- **499 εὔχετο "vowed"** against the table's εὔχομαι + inf. "claim" (3.430). Both readings of 499–500 are ancient; the note sets out both and new-renderings.md records the choice. Kept.
- **491 δαΐδων ὕπο λαμπομενάων "under blazing torches"**: follows odyssey-114 (23.290); odyssey-092 has "flaring". Not a whole repeated line here; the later Odyssey wording is a fair choice. Kept.
- **476 `i` "on the anvil-block"** against odyssey-035's `i` "on its block" (8.274): the `l` agrees, and the lines are not the same line. Kept.
- **506 `i` "rose one after another"** beside "in turn": an inference from ἀμοιβηδίς that the note supports. Kept.
- **417 and 421 `i` "to support him", "holding him up"**: interpretive, consistent with each other and with the notes. Kept.
- **454 n, Euphorbus and Hector**: a statement about Book 16 that this part cannot show; true and needed to explain Thetis' compression. Kept.
- **500 πιφαύσκων `i` "declaring it"**: the table's `i` varies ("made known to us", "to signal"); "declaring" is within the verb's sense. Kept.
- **Μενοιτίου ἄλκιμον υἱόν "Menoetius’ sturdy son"**: matches iliad-069, -071, -072. Kept.
- **παχύ "thick" sceptre beside στιβαρόν "stout" neck**: keeps the two words apart, as the 12.446 row does. Kept.

## Pass 2: gloss.json (113 novel forms, 14 broadenings as delivered)

All 113 novel forms present, none extra; every delivered broadening starts with the existing entry whole; all novel entries under 230 characters; typographic ’ only. Every parse checked against its line.

| Key | Severity | Was wrong | Done |
|---|---|---|---|
| χοάνοισιν | moderate | Lemmatised as χοάνη (fem.) "with the epic ending -οισιν (= Attic χοάναις)": impossible, a first-declension noun cannot take -οισιν. The form is from χόανος, masc. | "χόανος — crucible, melting-pot (from χέω ’pour’); masc. dat. pl., epic -οισιν (= Attic χοάνοις)" |
| χεῖρ (broaden) | moderate | Existing entry gives only χεῖρ’ = χεῖρα; with ἄμφω (414) it is the dual χεῖρε, as the unit's note says. | Broadening added: dual, ’both hands’. |
| ἔρρων (broaden) | minor | Existing entry only ’coming wretchedly’. | Broadening added: of a lame walk, ’going painfully, limping’. |
| ἀγορῇ (broaden) | minor | Existing entry only ’assembly’; 497 is the place. | Broadening added. |
| εὔχετο (broaden) | minor | Existing entry ’pray’ only; 499 has + inf. | Broadening added: ’vowed’ or ’claimed’, both readings. |
| τοῖσιν (broaden) | minor | Existing entry masculine only; 506 τοῖσιν refers to the sceptres. | Broadening added: neut., ’with these’. |
| τῇς (broaden) | minor | New reading "relative after ἐν, ’in whom’" against the unit's note and `l` ("in them"). | Reworded "with ἐν, ’in them’". |
| κρατερήν | minor | Pinned to the line ("agreeing with ῥαιστῆρα"). | "fem. acc. sg., Ionic -ήν (= Attic κρατεράν)". |
| ῥαιστῆρα | minor | "masc. acc. sg." where the same gloss and the note make it feminine here. | "acc. sg., masc. in form but feminine in Homer". |
| τρίπλακα | minor | "adj. of two endings, fem. acc. sg.": τρίπλαξ is a one-ending adjective; the form is masc./fem. | Corrected. |
| ἄμμορός | minor | "fem. nom. sg." only; the adjective is two-ending. | "masc./fem. nom. sg." |
| λαχνήεντα | minor | Only neut. pl.; also masc./fem. acc. sg. | Added. |
| μελόντων | minor | Genuine homograph with the participle gen. pl. not given. | Added. |
| ποίει | minor | Homograph with the imperative 2 sg. not given. | Added. |
| ἄντυγα | minor | "rim (of a shield)" only; first entry for the form should be general (chariot rail, 5.262). | "rim (of a shield), rail (of a chariot)". |
| ἔφθιεν | minor | One reading only, worded for this line. | Both readings, as in the note. |
| ἥφαιστ | minor | Printed form given lower-case. | "Ἥφαιστ’". |
| ὠκυμόρῳ | minor | "short-lived", the word the table reserves for μινυνθάδιος. | "swift-doomed, soon to die". |

Refused in pass 2: entries pinned in the existing glossary (καλάς "agreeing with κνημῖδας", ἱερῷ "agreeing with δίφρῳ", ἠέλιόν "with ὑπό", αὐχένα, μαρμαρέην "agreeing with ἅλα") are not wrong of the form and the runbook forbids rewriting them; not broadened. ἀρημένος, αἴητον, ἠεροφώνων, πραπίδεσσιν say their uncertainty; kept. ἐξανιεῖσαι, ἱέσθην, εἵατ’, ἀποφθιμένου, ἐείλεον, ἐφύσων, ἔπραθον checked and right.

new-renderings.md: the ἐστεφάνωται row rewritten; 18.426a added to "Reused" and to "Departures from Odyssey English". Nothing else in it changes with the units.

## Counts

Changes: 5 moderate (426a repeated-line English, 485 ἐστεφάνωται, 461 note, gloss χοάνοισιν, gloss χεῖρ’ dual), 22 minor (6 in units, 16 in the gloss), 0 severe. Refused: 11 in pass 1, 1 group in pass 2. Scansion: 493 hand-scanned, regular; no sentence added, the existing one kept.
