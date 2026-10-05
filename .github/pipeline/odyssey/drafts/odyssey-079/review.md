# review-079 — adversarial review of the draft of Odyssey 16.213–307

## Pass 1

Scope: grammatical labels in every note; Greek → `l` word by word; `l` ↔ `i`; remembered English in `i`; quotation marks;
the packet-flagged line 277; and, as asked, the reading of 16.255, κρατέουσι with datives at 16.264–265, and the rows of
`new-renderings.md`. `gloss.json` did not exist at this pass; the glosser's output is for pass 2. Conventions.md was read
through, table included, and every house row that touches a word of this part was checked against the draft.

Edits were made to `units.json` in place by script (`review_079_pass1.py` plus three small follow-ups, whole-field or asserted
single-substring replacement, `ensure_ascii=False, indent=1`). `t` was asserted equal to the pre-review copy after every
step. 55 fields changed in 27 of 54 units (21 `l`, 16 `i`, 18 `n`); `l` line counts equal the `\n` count of `t` throughout; no
`\n` in any `i`; no `?` or backtick in any note. `new-renderings.md` was also edited (see the end) because two of its rows
contradicted rows already in the table and would have been copied into it at publish.

Mechanical checks after the edits:
- Units whose Greek repeats a published unit: 224, 225 (odyssey-067), 240, 262 (004), 258, 266 (067), 281, 299 (055) are
  identical in `l` and `i` to the published ones; 223 and 243 (ἄγη μ’ ἔχει) were NOT, and are fixed below.
- Quotation marks: “ on 222, 226, 241, 259, 263, 267 and ” on 224, 239, 257, 261, 265, 307 in both layers (6 and 6); inner ‘ on
  288 and ’ on 294 in both layers; `mark` on exactly those six units plus 288; `p` on 213, 222, 258, 262, 266, 288 (= Murray's
  paragraph marks). Neighbouring part: the last unit of odyssey-078 (line 211–212) ends in ” and closes Odysseus' speech,
  so nothing runs on into 213; 307 closes the speech and 308 is a new line of narrative in odyssey-080's cut.
- Cross-references checked: 13.136 (= 16.231) is in odyssey-063 (13.113–216); lines 235, 240, 256, 257, 258, 260, 261, 264, 281, 283,
  287, 294 and the five/six-line sentence counts were counted against the lines.

Severity: high = wrong sense, a false grammatical or cross-reference claim a reader would be misled by, or something the build
gate refuses; medium = a house row (conventions table) or a repeated-line rule broken, or `l` and `i` disagreeing in sense;
low = precision, internal consistency, capitalisation; nit = wording only.

### Changes to units.json

| line | field | sev | what was wrong | what done |
|---|---|---|---|---|
| 223 | l | high | Same unit as odyssey-002 line 172, 067 line 189 and 077 line 58 (`τίνες ἔμμεναι εὐχετόωντο;`); the packet lists only whole-line repeats and missed it. `l` began “who”, the published `l` is “Who”: the validator refuses a repeated unit with different English. | “Who did they declare themselves to be?” (the unit follows a question mark, so the capital is right). |
| 243 (ἄγη μ’ ἔχει) | l, i | high | Same unit as odyssey-011 line 227 (`ἄγη μ’ ἔχει.`, l “Amazement holds me.”, i “I am amazed at the thought.”), again unlisted by the packet; draft had “amazement holds me;” / “I am amazed;” (gate failure). | Published English adopted exactly. Knock-on, low: the units on either side now sit round a full stop, so 243 εἶπες `l` “… you have said.” and `i` “but you have spoken of something far too great.”; 243 οὐδέ κεν `l` “Nor could it be …”, `i` “Two men could not fight …”. |
| 233 | l | high | “that with the ill-disposed, concerning slaughter, we may take counsel” reads as counsel taken with them; δυσμενέεσσι is the dative of the persons the plan is against. `i` was right. | “that against the ill-disposed, concerning slaughter, we may take counsel.” |
| 233 | n | high | Same point left unsaid in the note. | “a dative of the persons the counsel is against” added after δυσμενής. |
| 254–255 | n | high | “πολύπικρα καὶ αἰνά … is its object, with βίας ‘of violence’”: βίας is not a genitive (the epic genitive is βίης) but the accusative plural ‘acts of violence’, object of ἀποτίσεαι, exactly as at 11.118 (table row); πολύπικρα καὶ αἰνά is adverbial. | Note rewritten: object βίας (acc. pl., ‘not a genitive, which would be βίης’), πολύπικρα καὶ αἰνά ‘in very bitter and dread ways’; the sentence “The grammar is hard” kept. |
| 254–255 | l, i | high | “pay back … of violence” / “paying back their violence at a very bitter and terrible price” gives ἀποτίνομαι the active sense ‘repay’ and invents a ‘price’; the table fixes “exact payment (for) … violence” (11.118). | `l` “lest, in very bitter and dread ways, for acts of violence you exact payment, having come.”; `i` “… I fear that in coming you will exact payment for their violence in a very bitter and terrible way.” |
| 213 | i | medium | “noble father” for πατέρ’ ἐσθλόν; the table keeps ἐσθλός “good” throughout (and turns “noble” down at 5.110). | “good father” (`l` already had it). |
| 213 | l, i | medium | δάκρυα λείβων rendered “shedding tears”; “shedding” is reserved for δάκρυ χέων, and the table row fixes λείβων as `l` “tears pouring”, `i` “pouring out his tears”. | `l` “wailed, tears pouring,”; `i` “wept, pouring out his tears,”. |
| 216 | l, n | medium | λιγέως `l` “in a clear voice”; the table row (and 10.201) fixes `l` “clearly”, `i` “in a clear voice”. The note said “in a clear voice, the house rendering”. | `l` “they wept clearly,”; note states both. |
| 216 | l, i, n | medium | φῆναι rendered “eagles” and the new-renderings row refused “sea-eagles”; but φῆναι is the plural of φήνη, already in the table (3.372: “a sea-eagle”, species unknown, “vulture”/“osprey” avoided). Two English words for one Greek word, and a duplicate row that would contradict the shipped one. | `l` and `i` “sea-eagles or crook-/hook-taloned vultures”; note says ‘sea-eagle’ is the shipped stand-in (3.372); the row is removed from new-renderings.md. Note also trimmed (138 → 120 words). |
| 216 | i | low | “and they wept” began with a lower-case letter after a full stop. | “And they wept …”. |
| 219 | l, i, n | medium | εἶβον rendered “shed”; the table (κατὰ δάκρυον εἴβων, 11.391) fixes εἴβω as “letting fall”, “shedding” being χέων. | `l` “… from beneath their brows let fall.”; `i` “So they let pitiable tears fall from beneath their brows.”; note “‘let fall’”. |
| 232 | l | medium | “by the will of the gods”; table row θεῶν ἰότητι: `l` “by the gods’ will”, `i` “by the will of the gods”. | `l` “by the gods’ will”. |
| 233 | l | low | νῦν αὖ `l` “Now again”, note and `i` say ‘in turn’ (αὖ = “in turn” elsewhere in the table). | “Now in turn here I came”. |
| 243 (εἶπες) | l, n | low | `l` “but too greatly a thing you have said” (unidiomatic and loses λίην μέγα “too great”); note: “μέγα stood in the line before”, but 241 is two lines earlier (242 intervenes). | `l` “but too great a thing …”; note “in line 241”. |
| 256–257 | i | medium | `l` “consider that someone might defend”, `i` “consider whether someone would defend”: different senses; the note itself reads ὅ as ‘that’. | `i` “consider that someone might defend the two of us with a ready heart.” (loose, as the note says). |
| 256–257 | l | low | “with a ready heart”; the note says πρόφρων is the house ‘ready-minded’ (table, 5.143). | “with a ready-minded heart.” |
| 259 | l | low | σύνθεο `l` “attend” but note “take it in”. | “you take it in”. |
| 264b–265 | n | medium | “κρατέουσι is the uncontracted third plural … it takes the datives”: stated as fact, but κρατέω normally takes the genitive and a plural verb after dual ὥ is irregular; the form can equally be a dative plural participle agreeing with ἀνδράσι, ‘to other men who hold sway’, with ‘helpers’ understood. | Note now gives the reading taken (3rd plural, datives) and says the other is possible and why; `l` and `i` left on the reading taken; “completes the thought of 264” → “of lines 263–264”. |
| 264b–265 | i | low | `l` “who also”, `i` “even over other men”. | “also”. |
| 267–269 | l, i, n | medium | μένος Ἄρηος “the might of Ares”; the table keeps μένος “strength” and “might” for ἀλκή (7.167, 11.270, 9.514). | “the strength of Ares” in all three. |
| 270 | n | low | “ἠοῖ φαινομένηφιν has the old ending -φιν”: the ending is on the participle; ἠοῖ is the dative of ἠώς. | Note says so. (New-renderings row had the same false label; see below.) |
| 272 | n | low | “λευγαλέος is ‘pitiful, wretched’”: “wretched” is reserved for δύστηνος by the new row and the table. | “‘pitiful’”. |
| 274–277 | l | low | “though I am suffering ill” for a genitive absolute (the note says ‘while’; the concessive comes only at ἤν περ καί). | “while I am suffering ill,”. |
| 274–277 | n | nit | “The line 277”. | “Line 277” (note otherwise kept: see scansion below). |
| 278 | l, i, n | medium | παραυδῶν “addressing them” / “speaking to them”; table (παραυδάω 11.488): “speak/talk soothingly”. `i` “foolishness” is the shipped `i` of ματίη, which the table reserves; ἀφροσύνη is ἀφραδίη's family (“folly”). | `l` “with gentle words speaking soothingly;”; `i` “stop their folly, talking soothingly to them with gentle words;”; note “‘speak soothingly to’”. |
| 282 | l | low | “in my mind”: the note says the owner of the mind is left unsaid in the Greek; `i` and the note carry the sense. | `l` “in the mind”. |
| 282 | n | low | “the whole sentence runs five lines”: 282–287 is six. | “six lines”. |
| 283 | l, i, n | medium | Ἀρήϊα τεύχεα “war-gear of Ares” / “arms of war”; the table has ἀρήιος “warlike” and τεύχεα “armour”. | `l` “all the warlike armour that for you in the halls lies”; `i` “take up all the warlike armour that lies in your halls and put it away … every piece”; note says τεύχεα ‘armour’. |
| 286 | i, n | low | Follows from 283: “missing the arms”. | “missing the armour”; note “the armour”. |
| 291 | l | low | “and besides this” began lower-case after a full stop (`i` had the capital). | “And besides this”. |
| 294 | l, i | low | ἐφέλκεται is middle (the note says ‘draw towards oneself’); “draws on a man” / “draws a man on” lose that. | `l` “for of itself draws to it a man iron.’”; `i` “for iron of itself draws a man toward it.’”. |
| 295 | l, i | low | Lower-case starts after the full stop closing the inner quotation. | “But for us two alone …” / “But to leave …”. |
| 295–297 | l, i, n | medium | “rushing upon them, we may seize them”: ἐπιθύσαντες has no object, so the first “them” (the suitors?) is invented, and the second “them” (the arms) is then ambiguous. | `l` “so that, rushing in, we may seize them;”; `i` “so that we can rush in and seize them;”; note “‘rush in’, with no object given”. |
| 297–298 | l, i, n | medium | θέλξει rendered “will bewitch”; table row θέλγω (10.291, 10.318, 10.326): “enchant”, with “bewitch” among the avoided words. The new-renderings row (“will bewitch”, refusing “charm/beguile”) overlooked it and would have put a second, contradictory row in the table. | “will enchant” in `l`, `i`, and note; the new-renderings row removed. |
| 305 | n | low | ὅπου glossed nowhere though `l` has “where” and `i` “who”. | “ὅπου ‘where’ here means ‘in whose case’” added. |
| 226 | n | low | “in which his own part is told without invention”: nothing in this part shows that, and the note should not grade the speech. | “a plain account of how he came”. |

### Scansion: line 277 (packet flag `UNRESOLVED`, ‘metrical lengthening: βέλεσι’)

Scanned by hand: `ἢ βέ-λε-σι | βάλ-λω-σι σὺ δ’ εἰ-σο-ρό-ων ἀ-νέ-χε-σθαι` gives ἢ βέ λε | σι βάλ | λω σι σὺ | δ’εἰ σο ρό | ων ἀ νέ |
χε σθαι = dactyl, spondee, three dactyls, spondee, with the third-foot trochaic caesura after βάλλωσι. The only way to
make six feet is to count the final -σι of βέλεσι (short by nature) long as the first half of foot 2; there is no other
division. The irregularity is real, and the drafter's one sentence is accurate, so it is kept (only “The line” → “Line”).

### Findings considered and refused

- 16.255 reading beyond the fix above: μή + future (fear), ἀντήσομεν + genitive absolute of πάντων ἔνδον ἐόντων, ἐλθών —
  all true as written; the sense “I fear you will exact payment for their violence at bitter cost” is the one the line bears
  and the note states that the grammar is hard; no further hedge was added.
- 16.264–265: reading kept on the plural verb (see note rewrite); both readings give the sense that Athena and Zeus are
  strong helpers, and the datives sit with ἐπαμύντορε either way. Not changed to the participle reading because that would
  take κρατέουσι as agreeing with ἀνδράσι only while the sentence pairs ἀνδράσι τε … καὶ ἀθανάτοισι θεοῖσι.
- 241 κλέος “report” (not “fame”): kept; the table's row is for ἐσθλὸν κλέος, the note explains the choice, and ἄκουον “I
  heard” requires it.
- 213 ὣς ἄρα φωνήσας κατ’ ἄρ’ ἕζετο row: kept (consistent with the masculine rows ὣς ἄρα φωνήσας ἀπέβη / πόρε).
- πολύβουλος, βοάγρια, γυναικῶν ἰθύν, λευγαλέος (of a beggar) rows: kept, each checked against the neighbouring rows
  (πολύφρων “of the many counsels”, πολύμητις “of many wiles”, βουλή “plan”, ἰθύς from context, λευγαλέος θάνατος
  “a pitiful death”); no collision.
- 231 κάτθεσαν “= κατέθεσαν, with the preverb’s vowel lost”: kept (apocope of the preverb; accurate enough for a note).
- 288 κατῄκισται lemma spelling in the note: not touched; left to the glosser.
- 290 ἀϋτμή `l` “blast”, `i` “breath”: accepted (table has ἀυτμή “breath, vapour”; the two agree in sense).
- 227 σφέας … εἰσαφίκηται “to them comes”: accepted (the verb takes the accusative).
- 222 ποίῃ … νηΐ “dative of means”: accepted.
- 251–253 note, “108” sum: 52 + 24 + 20 + 12 = 108; correct. “Telemachus begins with the largest group”: correct.
- 249–250 “This unit ends at the comma”, 282, 300, 301 (comma cuts): each sentence runs more than four lines (249–253: 5;
  282–287: 6; 300–304: 5): permitted.
- Remembered English: nothing found beyond what is above; “iron … draws a man on” was changed for the middle voice, not for
  provenance. 243 “I am amazed at the thought” is the shipped wording, not a new choice.
- Notes over the 110-word band: 216 (120), 274 (127), 301 (126) are advisory WARNs only (the gate fails above 130) and every
  sentence in them is true; left for pass 2 to trim if a reader-facing trim is wanted.
- The packet lists only whole-line repeats; the two missed above (223, 243) are mid-line units. Worth telling the pipeline's
  owner (QUESTIONS.md) if it recurs: `packet.py` could list unit-level repeats too.

### Changes to new-renderings.md (outside units.json; recorded because publish copies these rows into the table)

| row | sev | what was wrong | what done |
|---|---|---|---|
| φῆναι | medium | Duplicate of the shipped φήνη row (3.372, “a sea-eagle”) with a conflicting rendering (“eagles”, refusing “sea-eagles”). | Row removed; the table's φήνη row governs. |
| θέλξει | medium | Contradicts the table's θέλγω row (“enchant”; “bewitch” avoided). | Row removed. |
| ἅμ’ ἠοῖ φαινομένηφιν | low | “ἠοῖ with the old ending -φιν”: the ending is on φαινομένηφιν. | Label corrected. |
| ὣς ἄρα φωνήσας κατ’ ἄρ’ ἕζετο | nit | Cited only the feminine ὣς ἄρα φωνήσασ’; the masculine rows (ὣς ἄρα φωνήσας ἀπέβη / πόρε) exist. | Cited. |

Remaining rows (λευγαλέος of a beggar, πολύβουλος, βοάγρια, γυναικῶν ἰθύν, and the 213 formula) are consistent with the table and with the draft.

### Counts by severity (distinct findings)

units.json: high 4 (223; 243 ἄγη; 233; 254–255), medium 13, low 17, nit 1. new-renderings.md: medium 2, low 1, nit 1.

Pass 2 to follow `gloss.json`: parses to be checked against the line, the θέλγω entry (“enchant”) and the φήνη/φῆναι entry
(species unknown) in particular.

## Pass 2

Scope: a fresh full pass on `units.json` (every note label against its line; Greek → `l` word by word; `l` ↔ `i`; quotation marks; repeated sense-units against all 4,488 published units), then every parse in `gloss.json` against the lines where the form stands, the entry-format rules, the `__broaden__` entries, and the 376 known forms against their use in this part. No translation or lexicon was opened or recalled. `build_odyssey.py` and `validate_odyssey.py` were read, not run. Edits were made by script (`pass2.py`, `pass2g.py` in the scratchpad), asserted single-substring replacements; `t` was asserted identical to the pre-pass copy; `ensure_ascii=False, indent=1`.

Gate facts read from the scripts: a new glossary entry must match `^\S.* — \S`, contain no ASCII `'` or backtick, and be 230 characters or fewer, and its form must occur in the part; a `__broaden__` entry must contain the old entry whole, and the build applies NO length cap to it (the validator has none either, only the shape check), so the long broadened entries (κε-family) are within the rules. A part form with no entry fails the build (checked: none missing; 109 new entries, none redefining an existing form).

Pass 1's edits to `units.json` were re-read for new errors. Findings: none of the labels pass 1 rewrote (254–255 βίας, 233 δυσμενέεσσι, 264 κρατέουσι, 270 φαινομένηφιν, 297 enchant, 216 λιγέως/φῆναι, 213, 219) is false; quotation marks balanced (6 “ / 6 ” in `l` and `i`, inner ‘ on 288, ’ on 294); repeated units 223, 224, 225, 240, 243 (ἄγη μ’ ἔχει), 258, 262, 266, 281, 299 identical in `l` and `i` to every published occurrence (machine-checked against all published stories; the only other overlap, odyssey-009 line 75, is a longer unit, not a repeat).

### Changes to units.json

| line | field | sev | what was wrong | what done |
|---|---|---|---|---|
| 235 (εἰδέω) | n | medium | “ὄφρα takes the short-vowel subjunctive εἰδέω”: εἰδέω is the uncontracted long-vowel subjunctive (= εἰδῶ), not a short-vowel subjunctive. | “the subjunctive εἰδέω, uncontracted (= εἰδῶ)”. |
| 241 | n | low | “σεῖο … in -οιο”: σεῖο has no -οιο ending. | “the epic genitive of σύ (Attic σοῦ)”. |
| 280 | n | low | “as in νόστιμον ἦμαρ”: a claim about the rest of the poem that this part cannot show (conventions, Notes). | Sentence rewritten without it; the sense (day of their death) kept. |
| 286 (παρφάσθαι) | n | low | Note said πάρφημι, the lemma in the glossary is παράφημι: the two disagreed. | Note says παράφημι, preverb shortened to παρ-. |
| 288 (κατῄκισται) | n | low | Note κατηκίζω vs. glossary κατηικίζω (pass 1 left it to the glosser); the ῃ is the augment of αι, so the verb is καταικίζω. | Note and glossary both καταικίζω. |
| 291 | n | medium | “aorist subjunctives τρώσητε and καταισχύνητε”: καταισχύνητε is not shown to be aorist; for this verb the present and aorist subjunctives coincide. | “τρώσητε (aorist) and καταισχύνητε (present or aorist; the forms coincide)”. |
| 291 | i | medium | “has put this greater thought into my mind: that … you may wound” loses the μή of fear (`l` has “lest”); read as a wish. | “… into my mind, for fear that, grown drunk … you may wound one another …”. |
| 301 | n | low | “γνώομεν … with lengthened vowel”: the glossary says uncontracted; the form is the uncontracted aorist subjunctive. | “uncontracted (= γνῶμεν)”. |
| 216, 274, 301 | n | nit | Notes 120, 127, 126 words (advisory band 110). | Trimmed to 113, 120, 105 by dropping glosses already given elsewhere (301: ἴστω’s τό γε, the repeated ‘you and I alone’; 274: ἀτιμάω gloss, κῆρ ‘heart’; 216: the nestlings sentence). 274 stays over the band by 10; every remaining sentence is a label or a construction a reader needs; advisory only. |

`l`/`i` Greek→English: re-read word by word, no further change; 243 split units (three) and the five/six-line sentence counts checked again.

### Changes to gloss.json (new entries)

| form | sev | what was wrong | what done |
|---|---|---|---|
| θέλξει | high | “charm, bewitch, beguile”: the table (θέλγω) fixes “enchant” and avoids both. | “θέλγω — enchant, cast a spell over; fut. 3 sg.”. |
| κ (broaden) | high | New reading quoted “will charm them” for θέλξει. | “will enchant them”. |
| εἶβον | medium | “unaugmented”: initial ει- shows no augment either way, so the label is false; “= Attic ἔλειβον” attached to the wrong claim. | “impf. 3 pl.; epic by-form of λείβω (= Attic ἔλειβον)”. |
| καταισχύνητέ | medium | “pres. subj.” asserted; present and aorist coincide. | “pres. or aor. subj. 2 pl. (the forms coincide)”. |
| κατῄκισται | low | Lemma κατηικίζω (see above). | καταικίζω, “augmented, hence ῃ”. |
| κρατέουσι | medium | Gave only the 3rd plural + dat.; the note says a dative-plural participle is the other reading, and κρατέω normally takes the genitive; the glossary is to carry both readings of a homograph. | Both readings joined by “ · ”; “+ dat.” dropped from the first. |
| παραυδῶν | low | “talk round, coax with words”: table (παραυδάω 11.488) “speak soothingly”. | “speak soothingly to, coax”. |
| παρφάσθαι | medium | “pres. inf. mid.” asserted (tense not certain for this form); lemma/meaning disagreed with the note. | “παράφημι — talk round, put off, coax; mid. inf., preverb παρ- for παρα-”. |
| πετεηνὰ | low | “neut. nom./acc. pl. as noun”: here an adjective (predicate with τέκνα). | “adj., neut. nom./acc. pl.… also as noun”. |
| πολύβουλος | low | “of many counsels”: reserved for πολύφρων; draft and house row are “of many plans”. | “of many plans, of much counsel”. |
| πολύπικρα | low | “bitter things” for a form the note takes as adverbial. | “neut. acc. pl., also adverbial: ‘very bitterly’”. |
| ἀδινώτερον | low | Example “more shrilly” vs. house “heavily”. | “more heavily”. |
| ἀρήϊα | nit | “(= Attic ἀρήιος)”: same word, no real Attic equivalent; “of war” pinned to the line. | Dropped both; “neut. nom./acc. pl.”. |
| βάλλωσι, ἕλκωσι | nit | “epic -σι (= Attic βάλλωσι(ν))” presented movable ν as an epic form. | “(Attic …(ν))”. |
| θῇσιν | nit | Example “whenever she shall put” pinned to Athena. | “whenever … shall put”. |
| ἔπορον | low | Lemma form differed from the shipped πόρε entry. | Same lemma line as πόρε; “they gave”. |

### Changes to gloss.json (`__broaden__`)

Rule obeyed: old entry whole, then “ · ” and the new reading; no length cap exists in the scripts for broadened entries.

| form | sev | what was missing | what done |
|---|---|---|---|
| φῆναι | high | Not listed at all. The shipped entry is φαίνω ‘to show’; here the word is the plural of the bird φήνη. A reader would be told a bird is ‘to show’. | Broadened with “φήνη — a bird of prey, species unknown (sea-eagle, osprey and lammergeier proposed); fem. nom. pl. φῆναι”. |
| αἵματος | medium | Entry pinned to “with ἆσσον”; here a genitive of descent after εἰμί. | Added. |
| νῶϊ | medium | Nominative only; at the second use it is the accusative. | Added “dual acc.: ‘us two’”. |
| οἷσί | low | Entry says “accented before περ”; here before τε, and a dative of interest. | Added. |
| ἑλοίμεθα | medium | “potential with κεν”; here an optative of purpose after ὡς ἄν. | Added. |
| ἂν | low | Not covering ὡς ἄν + opt. of purpose. | Added. |
| ἀμφὶς | low | “adverb” only; here it takes a genitive. | Added. |
| ἐγώ | nit | Accent explained only before τοι / μιν; here before τε. | Added. |
| κέν | medium | Pass-1 reading “relative clause: who might” contradicted the unit note (ὅ is ‘that’, and the shipped ὅ entry has “= ὅτι ‘that’”). | Reading changed to “in a clause with ὅ ‘that’”. |

Known forms checked and found adequate (no change): all other 350 or so, including αὐτῆς (intensive with a name is already there), κε (ὄφρα κε), κεῖται (stored objects), μή (fear, εἰ μή, imperative), ὁππότε, ὄφρα, ὅ (= ὅτι), ὑπό, εἰ, οἱ, and the pass-1 broadenings of αὐτὸς, ἄκουον, ἄγαγον, σφέας, καπνοῦ, πέρι, ὁπότε, κ, κέ, κεν, μὴ, τ (each new reading checked against the line it names).

### Findings considered and refused

- Entry-format: all 109 new entries are 230 characters or fewer (re-checked by script after the edits), use only ’, carry no line numbers or “here”.
- κιών (known entry: “aor. part.”): the shipped entry labels it aorist; it is a present participle of κίω. Existing entries are never rewritten, so not touched; the unit note says only “participle of κίω”, which is true.
- κάτθεσαν note “= κατέθεσαν” versus the shipped “(= κατέθηκαν)”: both are valid Attic equivalents of the same aorist; kept.
- μειλίχιος: the table’s rows disagree with each other (“gentle” at 9.363, “soothing” at 11.552). The draft’s “gentle words … speaking soothingly” follows the 9.363 row and the 10.442 reservation; no change.
- ἀμύμονα, πεπνυμένος, ναυσίκλυτοι, ὑπερφίαλος, κοῦροι, μητίετα, Παλλάς, δυσμενής, φήνη, ἀδινός (“heavily”), μαλακοῖς ἐπέεσσι, παραυδάω rows: each checked against the table; draft agrees.
- μνηστύν entry “the suitors’ feasting” is slightly context-coloured but does not name a line; kept.
- Unit 274 note remains 120 words (advisory WARN only, gate fails nothing); not trimmed further.

### Counts by severity (Pass 2, distinct findings)

units.json: high 0, medium 3, low 5, nit 1. gloss.json new entries: high 1 (θέλξει), medium 4, low 7, nit 3. `__broaden__`: high 2 (φῆναι missing; κ “will charm”), medium 4, low 3, nit 1. Combined: high 3, medium 11, low 15, nit 5.
