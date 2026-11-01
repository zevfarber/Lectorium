# Review — iliad-126 (Iliad 19.338–424)

Reviewer: adversarial, two passes. Pass 1: notes and cross-references, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, scansion, table conformity. Pass 2: re-read of every edited unit, then `gloss.json` (all 73 new entries and all 14 `__broaden__` entries checked against the line) and the known forms whose existing entry might not cover their use here. `t` untouched in every unit (checked by script against a copy taken before the first edit); no key added or removed. No translation consulted or recalled; the table in `conventions.md` and `../odyssey/conventions.md` were the only English references, and the repository's published parts the only source for cross-references (checked in `source/iliad-monro-allen1920.json` and in the published `iliad-*.json`).

## Counts

- units.json: 58 field-edits: High 4, Medium 30, Low 24 (56 rows in the first table, counted by unit and field, plus two edits to `about`). Total with gloss.json: High 4, Medium 37, Low 35 = 76 changes.
- gloss.json: 18 edits (Medium 7, Low 11).
- Not fixed, passed up: 1 gate-blocker (unit at 400, see below).

## Gate-blocker left for the parent

- **line 400 · t · High (not changed, as instructed).** The unit 400–401 ends at `ἡνιοχῆα` with no mark, because the pinned source prints no comma after `Βαλίε`, `Ποδάργης` or `ἡνιοχῆα`. `build_iliad.py` refuses a unit whose `t` does not end in `. ; · ,` ("does not end at punctuation"), so the build will stop here unless rule 5 of `.github/pipeline/README.md` (add the missing comma to the source, re-pin `sha256` of iliad-126 and any other part holding the line, fix `t`, log it) is applied, or the two units 400–401 and 402–403 are merged into one four-line unit. The unit's note already says that the sentence runs on into 402–403. I did not touch `t` or the source.

## Changes to units.json

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 342 | n | Low | note asserted something about book 1 that this part cannot show | “Athena, who had stood by Achilles in the quarrel with Agamemnon.” → “Athena.” |
| 355 | l | Medium | ἀπάνευθε is “apart” in the table; “far from the ships” is the phrase the table (15.348) turns down | “far” → “apart” |
| 355 | i | Medium | same | “far” → “apart” |
| 355 | n | Medium | note follows the rendering | “‘far” → “‘apart” |
| 357 | i | Low | i said “fly down” where l and note say “fly out”; ἐκποτέονται is fly out/forth | “down,” → “forth,” |
| 357 | n | Low | label “predicative” not true of ψυχραί, which is a plain second adjective with νιφάδες | “is predicative.” → “agrees with νιφάδες.” |
| 351 | l | High | θωρήσσοντο is imperfect; table (4.252) has “were arming themselves” / l had one line where t has two; build refuses (l must have the same number of lines as t) | “Achaeans at” → “Achaeans/at”; “armed” → “were arming” |
| 351 | i | Low | same | “armed” → “were arming” |
| 365 | l | Medium | καναχή is “clang” in the table (16.104); “clatter” is among the words it turns down | “clatter” → “clang” |
| 365 | i | Medium | same; “clashed” also dropped the noun | “clashed together,” → “gave a clang,” |
| 365 | n | Medium | note follows the rendering | “the ‘ring’ or ‘clatter’ of” → “”; “” → “‘clang’, a ringing” |
| 369 | n | Low | “goes with it” left unclear what καλάς agrees with | “goes” → “agrees”; “it.” → “κνημῖδας as well.” |
| 372 | n | Medium | wrong cross-reference: the sword line is 2.45 (2.44 is the sandals line) | “2.44” → “2.45” |
| 373 | l | Medium | ἀπάνευθε “apart”; γένετο “came to be” as in new-renderings row | “” → “apart”; “afar” → “a gleam”; “a gleam,” → “to be,” |
| 373 | i | Medium | ἀπάνευθε is “apart” in the table; “far off” was turned down at 10.425 | “” → “apart”; “it far off,” → “it,” |
| 373 | n | Medium | note follows the rendering / false grammatical label (ἠΰτε does not take a genitive) and an unsupported remark on whiteness | “‘from it, far off’,” → “‘apart from it’,”; “‘like’, with the genitive” → “‘as’, and”; “moon’, which gives” → “moon’ is a genitive depending on σέλας understood (‘as”; “shield’s” → “”; “its whiteness.” → “of the moon’); ἠΰτε does not govern it.” |
| 377 | l | Medium | ἀπάνευθε “apart” | “sea/far” → “sea/apart” |
| 377 | i | Medium | table: bare ἄελλαι is “blasts” in l, “storms” in i (Od. 14.383, Il. 2.293); “of the wind” is not in the Greek; ἀπάνευθε “apart” | “the blasts of the wind” → “storms”; “far” → “apart” |
| 377 | n | Medium | note follows the rendering | “” → “(‘storms’ in the free English)”; “‘far” → “‘apart” |
| 379 | n | Low | note said the sentence goes on after the stop; the stop ends it | “sentence goes on after” → “unit ends at”; “380.” → “380; the rest of that line begins the next unit.” |
| 380 | n | High | backticks in a note make validate_iliad.py FAIL (and break the house rule: Greek bare, no code marks) | “” → “a word for the helmet, called”; “`l`” → “the literal line”; “`i`;” → “the free one;” |
| 381 | n | Low | invented detail (flashing as the head moves) not in the Greek | “which flashes as the head moves, and” → “” |
| 384 | l | Medium | ἔντεα is “gear” in the table; “armour” is reserved for τεύχεα | “armour,” → “gear,” |
| 384 | i | Medium | same | “armour,” → “gear,” |
| 384 | n | Medium | note follows the rendering | “armour’.” → “gear’, that is, in his arms.” |
| 386 | n | Low | ἔντεσι stands in 384, not 385 / stated as certain; the reading is an interpretation | “385.” → “384.”; “introduces” → “is taken as introducing” |
| 387 | l | Medium | ἐσπάσατο is “pulled out” in the table (4.530); “drew” is kept for ἐρύσσατο, ἕλκω | “drew” → “pulled out” |
| 387 | i | Medium | same | “drew” → “pulled”; “from” → “out of” |
| 387 | n | Medium | same | “‘draw’,” → “‘pull out’,” |
| 388 | n | Low | 16.140 says he did not take it | “(Patroclus is” → “(Patroclus, arming, does”; “to” → “” |
| 392 | n | Low | claim about their earlier service lies outside this part | “The” → “Automedon and Alcimus are the”; “charioteers are Patroclus’ old squires, now serving Achilles.” → “men who see to Achilles’ team.” |
| 393 | l | Low | reuse of the 3.261 English (“drew tight backward”) | “back/to” → “tight backward/to” |
| 393 | i | Low | reuse of the 3.261 English (“back tight”) | “” → “tight” |
| 395 | l | Medium | table row ἵπποιιν: l “upon the pair of horses”, i “behind” | “behind” → “upon” |
| 395 | n | Medium | note misquoted the form (ἐπ’ for ἐφ’) and said “onto”, which contradicts the i layer | “ἐπ’” → “ἐφ’”; “‘onto” → “‘upon”; “two horses’:” → “pair of horses’,”; “ἵππος,” → “ἵππος; he mounts the car those two draw, so the free English says ‘behind”; “horses pulling the chariot.” → “horses’.” |
| 397 | n | Low | “steps up into the chariot” is inferred, not said | “steps up into the chariot after” → “takes his place behind” |
| 400 | n | Low | ἄλλως departs from the table’s “idly” (Od. 14.124); the note now says so and what the sense is | “now’: this time,” → “now’, not the ‘idly, in vain’ that ἄλλως often has:”; “last time.” → “the one that failed Patroclus.” |
| 404 | i | Low | προσέφη is “said to”, not “answered” (the table keeps “answer” for ἀπαμειβόμενος) | “answered” → “spoke to” |
| 407 | n | Low | only one accusative is written; “double accusative” was not true of this line | “a double accusative (him, endowed with speech),” → “αὐδήεντα as the complement of an understood object ‘him’,” |
| 408 | n | Low | note gloss differed from the table’s καὶ λίην “truly” | “very much so’,” → “truly’,” |
| 409 | n | Medium | 413 does not name the god, as the note on that unit itself says | “named” → “only described”; “(Apollo);” → “and is Apollo;” |
| 411 | n | Low | νωχελίῃ is not what ἡμετέρῃ agrees with | “cause, agreeing” → “cause; ἡμετέρῃ ‘our’ agrees”; “ἡμετέρῃ ‘our’.” → “the first and serves for both.” |
| 413 | n | Medium | wrong cross-reference: the line is 18.456 (18.454 is where the published unit begins) | “18.454” → “18.456” |
| 415 | n | Low | the label made ἥν περ part of the superlative | “” → “‘which indeed’ is the relative, picking up πνοιῇ, and”; “picking up πνοιῇ,” → “” |
| 416 | l | Medium | μόρσιμος is “destined” in the table (5.674, Od. 16.392); “fated” is reserved for the θέσφατον / μοῖρα words | “fated,” → “destined,” |
| 416 | i | Medium | same | “fated” → “destined” |
| 416 | n | Medium | same | “fated’,” → “destined’,” |
| 418 | i | Medium | φωνήσαντος is an aorist participle (“when he had spoken”); “As he spoke” made the voice cut off mid-speech, against l | “As” → “When”; “spoke,” → “had spoken,” |
| 418 | n | Low | “not struck dumb for good” is not in the Greek | “silenced, not struck dumb for good.” → “silenced.” |
| 421 | i | Low | “well enough” weakens εὖ νυ τὸ οἶδα | “enough” → “” |
| 421 | n | Low | note said “dear” is understood with both, against its own i (“my dear father and my mother”) | “goes grammatically” → “agrees”; “πατρός, but is understood with both.” → “πατρός only; μητέρος has no adjective.” |
| 424 | l | Medium | ἔχε is “hold” in l and “drive” in i in the table (5.829, 5.841) | “drove” → “held” |
| 424 | n | Medium | note follows the table | “‘held on, drove’” → “‘held’ in the literal line and ‘drove’ in the free one, with”; “” → “going” |
| 367 | n | Low | cross-reference was ambiguous about what 18.468 shows | “” → “Hephaestus made (18.468 on) and”; “from Hephaestus (18.468 on).” → “(19.3–12).” |
| 352 | l | High | l had two lines where t has three; build refuses | “Achilles, nectar” → “Achilles,/nectar” |
| 366 | l | High | l had one line where t has two; build refuses | “heart sank” → “heart/sank” |
| about | about | Medium | said Xanthus tells Achilles that "a god and Fate will kill him"; Xanthus says the blame lies with a great god and Fate (409–410) and that he is to be overpowered by a god and a man (416–417) | rewritten to say exactly that |
| about | about | Low | "grief and anger in his heart": the Greek has ἄχος and μενεαίνων (eagerness); "anger" is not there and is not the table's word | now "unbearable grief in his heart and eagerness against the Trojans" |

## Changes to gloss.json

| entry | severity | what was wrong | what was done |
|---|---|---|---|
| gloss `λέπαδν` | Medium | entry stated a definite fitting (strap joining yoke to pole), where the unit note and table say the fitting is not clear | edited entry |
| gloss `ἅρπῃ` | Medium | “a kind of falcon or harrier” picks a bird, against the table and the unit note | edited entry |
| gloss `ἐκκατεπᾶλτο` | Medium | “unaugmented-type form” false: the form carries the augment ε | edited entry |
| gloss `καναχὴ` | Low | aligned with the house rendering “clang”; “of teeth, hooves, metal” pinned the sense to lines | edited entry |
| gloss `μήνης` | Medium | “after ἠΰτε” made ἠΰτε govern the genitive, which it does not | edited entry |
| gloss `μόρσιμόν` | Low | aligned with the table’s “destined” for μόρσιμος | edited entry |
| gloss `σύριγγος` | Low | “case or sheath” brought in “sheath”, which the new-renderings row turns down | edited entry |
| gloss `ξάνθε` | Low | same name glossed ’Yellow’ here and ’Chestnut’ in the published entry for ξάνθέ | edited entry |
| gloss `ξάνθος` | Low | same | edited entry |
| gloss `αἰόλος` | Low | unit note hedges quick/dappled; entry gave one sense only | edited entry |
| gloss `ποδάργης` | Low | meaning is uncertain (conventions row 16.149–152 gives both) | edited entry |
| gloss `στεροπῆς` | Low | “Ionic -ῆς” is not a feature of the ending here | edited entry |
| gloss `ὑπερίων` | Low | “in apposition with ἠλέκτωρ” pinned the entry to the line | edited entry |
| gloss `φανήῃ` | Low | form is the aorist in -η- (passive form); label said only “aor. subj.” | edited entry |
| gloss `ἵκοιτο (broaden)` | Medium | existing entry covers general-clause and wish uses only; this is a purpose optative | edited entry |
| gloss `ἵνα (broaden)` | Medium | existing entry has ἵνα + subj. only | edited entry |
| gloss `ἄειρε (broaden)` | Medium | existing entry has the imperative only; this is the imperfect | edited entry |
| gloss `κολλητὸν (broaden)` | Low | existing entry has neut. acc. sg. only | edited entry |

## Findings considered and refused

1. **Missing commas at 400 and 401** (after `Βαλίε`, `Ποδάργης`, `ἡνιοχῆα`): left as printed, as instructed; the unit's note says the sentence runs on. The consequence for the build is under "Gate-blocker".
2. **ἡνιοχῆα** (401): note and `i` checked. The note says plainly that the Greek does not say whether Automedon or Achilles is meant; `i` "your charioteer" supplies only the pronoun the vocative address gives. Kept.
3. **Hedged readings** — ἅρπη, αἰόλος, ζεύγλη, κραταιγύαλοι, ἕωμεν, αἰθρηγενέος, οἰοπόλῳ, ὀρθοκραιράων, ἠλέκτωρ, αὐδήεντα, ἑῆος: every one is hedged in its note and neither `l` nor `i` goes beyond the table row. κραταιγύαλοι: asked for a further hedge on γύαλον; refused, the note already says "the hollow or curved plate" and the table row's own wording is the same. (The gloss entries for ἅρπη and λέπαδνα were not hedged; fixed above.)
4. **ἄλλως departure** (401): `l` "in another way, now" / `i` "in another way" departs from the Odyssey row ἄλλως "idly" (14.124) and follows the Iliad's own ἄλλως "otherwise" (11.391); it is recorded in `new-renderings.md` with the reason and is right for the sense. The note now also says the word is not the "idly" of 14.124.
5. **Cross-references verified against the repository** (all correct unless listed above as changed): 3.330–331 and 11.17–18 (greaves, same two lines), 3.332 (breastplate line, sentence runs on), 3.334 (sword), 16.141–144 (spear, with the half-line start at 141), 4.73 (line 349), 3.261 (reins), 19.294 (ἦμαρ ὀλέθριον), 19.275ff (army dismissed), 19.303–337 (the refusal and the lament), 18.468 (Hephaestus begins to forge), 16.130ff and 17.125ff (Patroclus arms, Hector strips him), 16.48 (reply formula), Od. 7.81 (πυκινὸς δόμος), 15.613 (μόρσιμον ἦμαρ, cited in new-renderings.md only). **Wrong and fixed:** 2.44 → 2.45; 18.454 → 18.456.
6. **Reuse of published English.** Whole-unit repeats checked by script: unit 369–370 (= iliad-064 at 11.17) and unit 419 (= iliad-099 at 16.48) have `l` and `i` identical to the published ones. Line repeats inside larger units: 372–373 (3.334), 388–391 (16.141–144), 371 (3.332), 414 (18.456), 341 (8.350–351), 349 (4.73), 393 κατὰ δ’ ἡνία τεῖναν ὀπίσσω (3.261, now "drew tight backward") — all follow the published wording as far as the sentence allows.
7. **Scansion.** The packet flags none. All 54 lines were also run through the Odyssey's `scan_hexameter.py`: every line fits; the only marks are ordinary licences (spondaic fifth foot at 344, 391, 403; synizesis in Βαλίε at 400 and ἕωμεν at 402; lengthening before initial μ or λ at 339, 350, 395). None is irregular as transmitted, so no scansion sentence was added to any note.
8. **ἄκμηνος** `i` "goes fasting, tasting nothing" against iliad-125's "goes without": refused. `l` "fasting" matches, and "goes without" cannot stand next to "tasting nothing" without repeating itself.
9. **ἐπὶ … στενάχοντο** `l` "in addition groaned" against the table's ἐπεστενάχοντο "groaned along": refused. The Greek here is the split (tmesis) form and the note says so; the literal `l` is right for it, `i` already reads "groaned along with him".
10. **λαμπέσθην** `i` "blazed" against `l` "gleamed": refused, within the sense of the verb; no table row.
11. **βῆ** `i` "came" against `l` "went": refused, a matter of point of view in the free English.
12. **Quotation marks.** Four speeches, each with one `mark` on its first unit and “ ” balanced in both layers: Zeus 342–348, Achilles 400–403, Xanthus 408–417, Achilles 420–423. The preceding speech (Achilles, ending 337) closes in iliad-125's last unit with ”; the part ends on narrative, so nothing runs on. Correct as drafted.
13. **gloss.json: τά at 368** (relative, accusative) and **ἔλειπον at 339** (3 pl.): existing entries are broad enough ("neut. nom./acc. pl." with a relative sense; "the form is also 3 pl."); no broadening added.
14. **gloss.json: ἑῆος** (existing entry lists "own" first, "good" second): the note leads with ἐύς and keeps the other reading; the entry lists both, so refused.

## For the parent: new-renderings.md must be corrected before its rows are copied into conventions.md

I did not edit `new-renderings.md`. The units now follow the table on these points, so the rows should say the same:

- ἄελλαι (377): `i` is "storms" (table, Od. 14.383; bare ἄελλαι is "blasts" in `l`, "storms" in `i`); the row's "the blasts of the wind" and its "avoided: storms" are wrong.
- ἀπάνευθε (355, 374, 378): "apart" in both layers (table 10.425, 15.348; "far off" and "far from the ships" are the turned-down forms). No row needed; the σέλας row (374) must read "a gleam came apart from it, like the moon's" (not "from it far off").
- ἔχε (424): `l` "held", `i` "drove" (table 5.829, 5.841); the row says `l` "drove".
- μόρσιμον (417): "destined" in both layers (table 5.674, Od. 16.392; "fated" is reserved for the θέσφατον / μοῖρα words); the row says "fated".
- ἐσπάσατο (387): "pulled out" (table 4.530); the row gives nothing for the verb and the draft had "drew".
- ἔντεα (384): "gear" (table 3.339; "armour" is reserved for τεύχεα).
- καναχή (365): "clang" (table 16.104).
- ἵπποιιν (396): `l` "upon the pair of horses" is now what the unit has; `i` "behind" unchanged.
- ἔκταν’ ἐνὶ προμάχοισι… row: "as iliad-120 (18.454)" should read 18.456.
