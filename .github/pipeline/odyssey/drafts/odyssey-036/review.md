# Review — odyssey-036 (8.292–386)

Reviewer: adversarial, two passes. Pass 1 covered every note label, every positional claim, every cross-reference, Greek to `l` word by word, `l` to `i`, remembered English, quotation marks and `mark`s, the neighbouring part (odyssey-035 ends at 8.291 with no speech open; the first unit here opens Ares' speech, as its note says), the packet flags, and the `new-renderings.md` rows against `conventions.md` and the shipped parts. Pass 2 re-read every unit after the edits, then read `gloss.json` (complete when I began; unchanged by anyone but me afterwards, checked by checksum) (160 new forms, 13 broadened) against the lines, and ran a build and validate in a scratch copy of the repository (nothing in the real repository was built).

`t` was never touched (checked by script: every `t` identical before and after). Edits were made by script to `units.json`, `gloss.json` and `new-renderings.md`.

## Changes to units.json (line · field · severity · what was wrong · what was done)

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 293 | i | low | γάρ unrendered in i: the reason-relation to the previous unit was lost | "Hephaestus is no longer at home" → "for Hephaestus is no longer at home" |
| 296 | n | medium | false grammatical label: ἔχυντο has the augment (ἐ-χυ-ντο); it is not unaugmented | "ἔχυντο is the aorist middle 3 plural of χέω 'pour', without the augment: the bonds" → "ἔχυντο is the aorist middle 3 plural of χέω 'pour' (a short athematic form, Attic ἐχέαντο): the bonds" |
| 302 | l | medium | Ἠέλιος shipped as "the Sun" in odyssey-035 (8.270) and 009; εἶπέ τε μῦθον is a table formula ("and uttered a speech" / "and spoke") | "for Helios kept a lookout for him, and uttered the word." → "for the Sun kept a lookout for him, and uttered a speech." |
| 302 | i | medium | same: "the Sun" as in odyssey-035; table i for εἶπέ τε μῦθον is "and spoke" | "for Helios was keeping watch for him and gave him word." → "for the Sun was keeping watch for him and spoke to him." |
| 302 | n | low | note said the formula "can introduce a speech" (an unshown claim about the poem) and contradicted the table rendering; now consistent with l/i | "γάρ explains why he turned back: Ἠέλιος 'Helios, the Sun' sees everything. οἱ is the dative 'for him'. σκοπιήν 'lookout, watch-post' and ἔχεν = εἶχεν 'was keeping', without the augment. εἶπέ τε μῦθον is a phrase that can introduce a speech, but here μῦθον is simply the object: Helios 'told the word', that is, gave the news." → "γάρ explains why he turned back: Ἠέλιος is the Sun (Helios), who sees everything. οἱ is the dative 'for him'. σκοπιήν 'lookout, watch-post' and ἔχεν = εἶχεν 'was keeping', without the augment. εἶπέ τε μῦθον is the half-line formula 'and uttered a speech'; no speech follows in the Greek, so what the Sun said is the news itself." |
| 303 | i | low | sentence-initial word lower-case after a full stop | "and he set off" → "And he set off" |
| 311 | n | low | τὼ labelled only "those two" though l/i render it as the relative "who" | "τοκῆε is the dual of τοκεύς 'parent', 'the two parents', and τὼ is the dual 'those two', who are the subject of ὄφελλον." → "τοκῆε is the dual of τοκεύς 'parent', 'the two parents', and τὼ is the dual pronoun used as a relative, 'who': they are the subject of ὄφελλον." |
| 313 | i | low | "up" is not in βάντες εἰς | "gone up into my bed" → "gone into my bed" |
| 324 | n | low | "used only to mean" is an over-claim about the word's use elsewhere | "θηλύτεραι is a comparative of θῆλυς 'female', used only to mean 'the female sex among them': 'the female goddesses'." → "θηλύτεραι is a comparative form of θῆλυς 'female' with no comparing force here: 'the female goddesses'." |
| 325 | l | low | lower-case sentence opening after a full stop | "and they stood in the forecourt" → "And they stood in the forecourt" |
| 325 | i | low | same | "and the gods, givers of good things, stood in the forecourt;" → "And the gods, givers of good things, stood in the forecourt;" |
| 328 | l | low | same | "and thus someone would say" → "And thus someone would say" |
| 328 | i | low | same | "and as each looked at the one beside him" → "And as each looked at the one beside him" |
| 346 | l | low | same | "and, lifting his voice, to him winged words he spoke:" → "And, lifting his voice, to him winged words he spoke:" |
| 346 | i | low | same | "and lifting his voice he spoke winged words to him:" → "And lifting his voice he spoke winged words to him:" |
| 326 | i | low | table ἄσβεστος: i "that would never go out" (ἄσβεστον κλέος 4.584, shipped 019, 032) | "laughter that nothing could put out rose" → "laughter that would never go out rose" |
| 334 | n | low | false label: προσέειπεν carries the augment; it is not "unaugmented" | "προσέειπεν is the unaugmented aorist of προσεῖπον 'speak to'." → "προσέειπεν is the Homeric aorist of προσεῖπον 'speak to'." |
| 340 | i | medium | table ἀπείρων = "boundless" in both layers (shipped 002, 018, 022, 032); i had "endless". Also capital after ";" inside a speech | "Let there be bonds three times as many, and endless, to hold me" → "let there be bonds three times as many, and boundless, to hold me" |
| 344 | l | low | l did not match the new-renderings row/table style (κλυτοτέχνης "famous in craft") | "Hephaestus, famous in his works," → "Hephaestus, famous in works," |
| 347 | n | low | l/i supply "him" with no word to say so in the note | "λῦσον is the aorist imperative of λύω 'release', and the high point after it" → "λῦσον is the aorist imperative of λύω 'release'; it has no object in the Greek, and Ares is understood. The high point after it" |
| 347 | i | low | κελεύεις: "require" is stronger than the l "bid"; "ask" fits Poseidon's plea | "as you require" → "as you ask" |
| 350 | l | low | κελεύω is "bid/urge", not "ask" (cf. ὡς σὺ κελεύεις at 347, l "as you bid") | "“Do not, me, Poseidon earth-holder, ask this;" → "“Do not, me, Poseidon earth-holder, bid this;" |
| 350 | i | low | same: "ask" drops the force of κέλευε "urge, bid" | "“Do not ask me for this, Poseidon earth-holder;" → "“Do not press this on me, Poseidon earth-holder;" |
| 359 | i | low | "So he spoke, and the strength of Hephaestus" reads as two agents; μένος Ἡφαίστοιο is the speaker himself (shipped precedent: "So speaking, he sank", 019.570) | "So he spoke, and the strength of Hephaestus loosed the bond." → "So saying, the strength of Hephaestus loosed the bond." |
| 359 | n | low | note said "was loosing" against i "loosed" | "ἀνίει is the imperfect of ἀνίημι 'let go, loosen', 'was loosing'." → "ἀνίει is the imperfect of ἀνίημι 'let go, loosen'; English gives it as a simple past, 'loosed'." |
| 360 | n | medium | false grammatical label: it is not a genitive absolute (the participle agrees with δεσμοῖο in ἐκ δεσμοῖο) | "κρατεροῦ περ ἐόντος is a genitive absolute, 'strong though it was'." → "κρατεροῦ περ ἐόντος agrees with δεσμοῖο, 'the bond, strong though it was'." |
| 360 | l | low | βεβήκει is a pluperfect (note: "had gone"); l "went" contradicted the note | "he to Thrace went," → "he to Thrace had gone," |
| 367 | l | medium | same Greek unit as odyssey-033 line 83 (shipped): validator check 6 requires identical l and i | "These things then the minstrel was singing, the very-famous;" → "These things then the minstrel was singing, far-famed;" |
| 367 | i | medium | same | "This was what the very famous minstrel sang;" → "These were the things the far-famed minstrel sang;" |
| 367 | n | medium | note must not contradict l/i; records the shipped rendering | "ἀοιδός 'minstrel'; περικλυτός 'very famous'." → "ἀοιδός 'minstrel'; περικλυτός 'very famous', which the same half-line already shipped at 8.83 renders 'far-famed' in both layers, kept here so that the repeated line reads the same." |
| 370 | i | low | "else" is not in οὔ τις | "since no one else competed with them" → "since no one competed with them" |
| 374 | l | medium | l rendered τήν (the ball, object of ῥίπτασκε) as "this one", leaving the throw without an object and ἕτερος doing double duty | "this one of them would throw toward the shadowy clouds," → "it one of them would throw toward the shadowy clouds," |
| 374 | i | low | "far" is not in ὀπίσω | "bending far back" → "bending backward" |
| 374 | n | medium | garbled parse: τήν is the pronoun "it", not "this one of the two" | "τὴν ἕτερος 'this one of the two' picks up the ball;" → "τήν 'it' (the ball, picked up from σφαῖραν) is the object of ῥίπτασκε and ἕτερος 'one of the two' its subject;" |
| 374 | n | medium | the note named no parse for the flagged form μεθέλεσκε | "μεθέλεσκε is a rare form, and 'would catch it' is taken from the picture." → "μεθέλεσκε seems to be the iterative of a compound of μετά and the aorist stem ἑλ- of αἱρέω 'take', so 'would take (it) up'; 'would catch it' is read from the picture and the exact sense is not certain." |
| 377 | l | low | σφαίρῃ is dative ("with the ball"), not a genitive object "of the ball" | "But when they had made trial of the ball straight up," → "But when they had made trial with the ball straight up," |
| 377 | i | low | same | "And when they had tried the ball straight up," → "And when they had made trial with the ball straight up," |
| 377 | n | medium | flagged risky spot: a disputed phrase was stated as one reading; the alternative was not named; ταρφέ’ unlabelled; "of the ball" contradicted the dative | "πειρήσαντο is the aorist middle of πειράω 'make trial of', with the dative σφαίρῃ 'of the ball'. ἀν’ ἰθύν is 'straight up' (ἀνά + ἰθύς 'straight'), the sense being taken from the game just described; it is not certain." → "πειρήσαντο is the aorist middle of πειράω 'make trial', with the dative σφαίρῃ 'with the ball'. ἀν’ ἰθύν is a phrase built on ἀνά and ἰθύς 'straight'; 'straight up' is taken from the game just described, but it may equally mean 'straight on', in a straight line, so the sense is not certain. ταρφέ’ is ταρφέα, a neuter plural used as an adverb, 'thick and fast'." |
| 379 | i | low | force: ἐπελήκεον is the main verb, ἑστεῶτες the circumstance; i made "stood" the verb | "and the other young men stood round the gathering-place beating time, and a great din went up from beneath." → "and the other young men, standing round the gathering-place, beat time, and a great din went up from beneath." |
| 384 | l | low | σέβας rendered "awe" in the shipped twin (010.123) and in i/note | "wonder holds me, looking on.”" → "awe holds me, looking on.”" |
| 332 | i | low | ASCII apostrophe in i (house style is typographic ’) | "adulterer's" → "adulterer’s" |
| 338 | n | medium | backticks in a note: validator check 3 fails on any backtick | "is kept in `i` without" → "is kept in the English without" |
| 296 | n | low | the note gave an Attic equivalent (ἐχέαντο) different from the glossary's (ἐχύθησαν); the note now claims no equivalent | "(a short athematic form, Attic ἐχέαντο)" → "(a short athematic form)" |
| 295 | n | low | glossary (shipped) parses φάτο as an imperfect; note said "aorist" | "φάτο is an unaugmented aorist of φημί" → "φάτο is an unaugmented past tense of φημί (= ἔφατο)" |
| 367 | n | low | note said "passive", glossary says "mid."; l and i give both senses | "τέρπετ’ is τέρπετο, the imperfect passive of τέρπω 'delight': 'was delighted'." → "τέρπετ’ is τέρπετο, the imperfect middle of τέρπω 'delight': 'was delighted, took delight'." |
| 329 | n | low | validator WARN: note of 19 words is under the 25-word band; added only checkable statements | "κακὰ ἔργα 'evil deeds'." → "κακὰ ἔργα 'evil deeds' is the subject. The present tense fits a saying that holds at all times. The gods speak one at a time (τις at 328), and the mark 'The gods speak' covers them all." |
| 357 | n | low | validator WARN: note of 16 words is under the 25-word band | "ἠμείβετ’ is ἠμείβετο, the imperfect middle of ἀμείβομαι." → "ἠμείβετ’ is ἠμείβετο, the imperfect middle of ἀμείβομαι. τὸν 'him' is Poseidon, the one addressed, and περικλυτὸς ἀμφιγυήεις is the subject, as at 300 and 349." |

## Changes to gloss.json (form · severity · what was wrong · what was done)

| form | severity | what was wrong | what was done |
|---|---|---|---|
| βητάρμονας | low | U+2018 quote in an entry (house style: typographic ’ only) | old: "βητάρμων — dancer (‘one who steps in time’; the second element is obscure); masc. acc. pl.: ’dancers’" — new: "βητάρμων — dancer (’one who steps in time’; the second element is obscure); masc. acc. pl.: ’dancers’" |
| ἅλιον | low | U+2018 quote in an entry | old: "Ἅλιος — Halius (‘Sea-man’), a Phaeacian youth; masc. acc. sg." — new: "Ἅλιος — Halius (’Sea-man’), a Phaeacian youth; masc. acc. sg." |
| οὖδας | medium | false claim "(used only in nom./acc.)": οὖδας also has gen. οὔδεος and dat. οὔδει | old: "οὖδας — ground, floor; neut. acc. sg. (used only in nom./acc.)" — new: "οὖδας — ground, floor; neut. acc. sg." |
| ἀγέροντο | medium | false Attic equivalent: ἠγείροντο is an imperfect, not the augmented form of this aorist | old: "ἀγείρω — gather, assemble; aor. 3 pl. mid., unaugmented, epic (= Attic ἠγείροντο): ’gathered’" — new: "ἀγείρω — gather, assemble; aor. 3 pl. mid., unaugmented, epic (= ἠγέροντο): ’gathered’" |
| μεθέλεσκε | medium | riskiest form: lemma "μεθαιρέω" unattested here and "take in turn" (from μετά) was not in the note; parse rebuilt to agree with the unit note | old: "μεθαιρέω — take in turn, catch; iterative aor. 3 sg. in -σκε(ν), unaugmented, μετ- + ἕλεσκε: ’would catch it in turn’" — new: "αἱρέω, with μετά (μεθ- before the rough breathing) — take up, catch; iterative aor. 3 sg. in -σκε(ν), unaugmented (μετ- + ἕλεσκε): ’would catch (it)’; the sense is inferred from the scene" |
| φιλομμειδὴς | low | "laughter-loving" is the rendering new-renderings.md rules out; the compound is φιλο- + μειδάω "smile" | old: "φιλομμειδής — laughter-loving (φιλέω + μειδάω ’smile’); fem. nom. sg. (grave, mid-clause form), epithet of Aphrodite" — new: "φιλομμειδής — smile-loving (φιλο- + μειδάω ’smile’); fem. nom. sg. (grave, mid-clause form), epithet of Aphrodite" |
| ἀριδείκετε | low | "very glorious, far-shining" contradicted the note, the new-renderings row and l/i ("most conspicuous"/"most distinguished") | old: "ἀριδείκετος — very glorious, far-shining; masc. voc. sg." — new: "ἀριδείκετος — very conspicuous, distinguished (ἀρι- intensifying; the second part is obscure); masc. voc. sg." |
| ἀναεῖραι | low | lemma accent (ἀναείρω) | old: "ἀνάειρω — lift up, raise; aor. inf., epic (= Attic ἀνᾶραι): ’to raise’" — new: "ἀναείρω — lift up, raise; aor. inf., epic (= Attic ἀνᾶραι): ’to raise’" |
| __broaden__/φίλη | medium | "dear (wife)" pins the entry to a wrong context: the speaker is Ares, and Aphrodite is not his wife | old: "φίλος — dear, one’s own; fem. nom. sg. · also voc. sg. in address: ’dear (wife)!’" — new: "φίλος — dear, one’s own; fem. nom. sg. · also voc. sg. in address: ’dear one!’" |
| __broaden__/πειρήσαντο | medium | known entry says "+ gen."; here the object is the dative σφαίρῃ (broadening missed) | old: "(none)" — new: "πειράω — try, test, make trial of (+ gen.); aor. 3 pl. mid., unaugmented (= ἐπειρήσαντο) · also + dat., ’make trial with (a thing)’: σφαίρῃ … πειρήσαντο ’made trial with the ball’" |
| __broaden__/ἀμειβομένω | medium | known entry glosses only "exchanging words, answering"; no words are exchanged here (broadening missed; a flagged risky spot) | old: "(none)" — new: "ἀμείβω — exchange; mid. answer, reply; pres. part. dual nom.: ’the two exchanging words, answering one another’ · also of dancers, no words spoken: ’taking turns, changing places with each other’ (ταρφέ’ ἀμειβομένω); sense inferred from the scene" |
| __broaden__/ἑτοῖμα | medium | known entry is acc. pl. "ready, at hand"; here the form is nominative plural, subject of τέτυκτο, in the sense "real, true" | old: "(none)" — new: "ἕτοιμος — ready, at hand; neut. acc. pl. · also neut. nom. pl., predicate: ἑτοῖμα τέτυκτο ’had proved real, had come true’" |
| __broaden__/ποτὶ | low | known entry gives "+ dat. against" only; here "on the ground" | old: "(none)" — new: "πρός — to, toward, against; prep., epic ποτί, here as preverb in tmesis (ποτὶ … βάλε = προσέβαλε) · also a plain preposition + acc., no tmesis: ποτὶ τοῖχον ’against the wall’ · also + dat. ‘against’ · also + dat., ’on, upon’: ποτὶ χθονί ’on the ground’" |
| __broaden__/περ | low | known entry covers concessive and adverb/pronoun uses, not εἴ περ | old: "(none)" — new: "περ — even, though; concessive particle, esp. with a participle (= Attic καίπερ) · also used to intensify an adverb or pronoun rather than concede a point: ἔνθα περ ’in the very place where, just where’ · also after εἰ, ’if indeed, even if’: εἴ περ γάρ κεν ’if indeed ever’" |
| __broaden__/τὼ | low | relative use (l "who") not covered | old: "(none)" — new: "ὁ, ἡ, τό — he, she, it; that (in Homer a pronoun); masc. nom. dual: ’the two of them’  ·  also acc. dual, object of a verb of address: τὼ … προσέφη ’spoke to the two of them’ · also relative, nom. dual, ’who (the two)’: τοκῆε δύω, τὼ μὴ γείνασθαι ὄφελλον" |
| __broaden__/λαῶν | low | partitive use with an adjective not covered | old: "(none)" — new: "λαός — people, host; masc. gen. pl., governed by ἄνασσε ’was lord over’ · also gen. with a noun: ’of the people’ (ποιμένα λαῶν ’shepherd of the people’) · also governed by ἐκ: ἔκ ... λαῶν ’from the people’ · also partitive gen. after a relative: οἵ ... λαῶν ἡμετέρων ’those of our people who’ · also partitive gen. after an adjective of rank: πάντων ἀριδείκετε λαῶν ’most distinguished of all the people’" |

## Changes to new-renderings.md

- κλυτοεργός · low · l cell "famous-in-works" did not match the table style (κλυτοτέχνης "famous in craft") or the unit; now "famous in works"
- κρείων · low · avoided cell said βασιλεύς / ἄναξ "are kept apart", but the table renders ἄναξ "lord" and κρείων keeps the "lord" shipped for κρείων Ἐτεωνεύς; cell rewritten to say so
- ἄσβεστος γέλως · low · i cell "laughter that nothing could put out" differed from the table's ἄσβεστον κλέος i "fame that would never go out" (used again in 019 and 032); now "laughter that would never go out"

## Counts

Total changes: 66 (units.json 47, gloss.json 16, new-renderings.md 3).

By severity: high 0, medium 20, low 46.

Severity scale: high = a false statement in the reader-facing English or a build blocker that I could not fix; medium = a false grammatical label, a house-rendering or shipped-precedent violation, a mistranslation, or a gate failure that I fixed; low = wording, capitalisation, form, over-claim, note/glossary agreement.

## Unresolved (needs a decision; not fixable inside this part)

1. **8.384 · `l`/`i` · validator FAIL (blocker).** The unit σέβας μ’ ἔχει εἰσορόωντα. has the same Greek as odyssey-010 line 123, so validate check 6 demands exactly l = "awe holds me, looking on you." and i = "Awe takes hold of me as I look at you." Those strings add an object "you" that the Greek does not have (an accusative participle agreeing with μ’) and that is true only of 3.123, where Nestor looks at Telemachus. Here Odysseus is watching the dancers. The unit was left true: l "awe holds me, looking on." i "awe takes hold of me as I look on." (σέβας is now "awe" in `l`, as shipped.) Options for the owner: (a) correct odyssey-010 line 123 to drop "you" (l "awe holds me, looking on." · i "Awe takes hold of me as I look on."), then this unit passes as it stands; (b) accept the shipped strings here and live with a wrong "you"; (c) leave the validator failing. I recommend (a). I did not touch a published file. Merging this unit with the one before it would dodge the check but breaks the rule that a unit ends at the first ·.
2. **8.367 · περικλυτός.** The table row (8.287) fixes περικλυτός as "very-famous" / "very famous" and reserves "far-famed" for τηλεκλυτός, but the half-line ταῦτ’ ἄρ’ ἀοιδὸς ἄειδε περικλυτός· shipped at 8.83 (odyssey-033) as "far-famed" in both layers (and 4.325 as "far-famed" / "famous"). The unit here must repeat 033 exactly (check 6), so it now reads "far-famed" and its note says why. The table and the shipped parts disagree; the owner may want to settle which wins. Nothing else in this part uses περικλυτός for a minstrel.

## Packet flags, confirmed by hand

- **8.355** (scanner: AMBIGUOUS, "short closed final lengthened before vowel: χρεῖος + ὑπαλύξας"). Scanned by hand: Ἥ-φαιστ’ | εἴ-περ | γάρ-κεν Ἄ | ρης-χρεῖ | ος ὑ-πα | λύ-ξας. Fourteen syllables give two dactyls (feet 3 and 5) and four spondees, so the -ος of χρεῖος must fill the longum of foot 5 before the vowel of ὑπαλύξας; χρεῖος with synizesis leaves foot 5 unfillable, and no other placement of the dactyls works. The drafter is right: the syllable is short by nature and stands long. The note already says this in one sentence, correctly and where it belongs; no change. (The scanner's "ambiguity" is only whether the υ and α of ὑπαλύξας are counted short; it does not touch the licence.)
- Repeated lines named in the packet (8.306, 8.333, 8.346, 8.369, 8.386) all reuse the published wording (8.333 as a whole unit, identical to odyssey-032 line 334 and accepted by the validator; 8.306, 8.346, 8.369 and 8.386 sit inside larger units and match line for line, with "him" for "her" at 8.346 as the Greek requires). One repeat the packet did not name (8.367 first half, and the 8.384 half-line) is item 1 and 2 above.

## Findings considered and refused

- **8.292 τραπείομεν, "epic lengthening".** Considered as a false label. Refused: the form (Attic τραπῶμεν) is a Homeric subjunctive with ει for ε, and "lengthened" is the label the glossary also gives; I cannot show it false, and nothing in the English depends on it.
- **8.302 "Ἠέλιος … sees everything".** Considered as a claim about the rest of the poem the part cannot show. Refused: it is a cultural fact about the Sun, not a claim about this poem's events.
- **8.297 / 8.326 πολύφρων: l "much-minded", i "of the many counsels".** Matches the table row (δαΐφρων · πολύφρων · ταλασίφρων) exactly in both layers; the note explains it. Kept.
- **8.372 δαΐφρων: gloss "warlike" vs note "fiery-minded".** Both are LSJ's alternatives for the burn-root reading, and the gloss entry says the sense is uncertain; l "wise-minded" / i "wise-hearted" follow the table. Kept.
- **8.377 ἀν’ ἰθύν, "straight up".** Considered changing both layers to "straight on". Refused, because I cannot show either reading right and a different flat guess would be no better; instead the note now names the second reading and says the sense is uncertain, and the glossary entry for ἀν says "in a straight line". Only "of the ball" → "with the ball" was a plain error (dative), and was fixed.
- **8.379 ταρφέ’ ἀμειβομένω.** The sense "taking turns" is inferred; note and (now) the broadened glossary entry say so. Kept.
- **8.375–376 μεθέλεσκε.** The iterative -σκ- and the μετά + ἑλ- parse are sound; the sense "catch" is inferred from the scene; note and gloss now say so. l "would easily catch it" kept as the best reading.
- **8.355 the note's one sentence on metre.** Kept unchanged (see above).
- **8.306 note ("whole-line address").** True. Kept.
- **8.310 ἀρτίπος "sound-of-foot" and 8.311 ἠπεδανός "infirm".** Rows checked: "feeble" is indeed spoken for by λευγαλέος (2.61, table row 424). Kept.
- **8.309 ἀίδηλος "destroying" / i "destructive".** Matches the row; the note states the doubt. Kept.
- **8.321 χαλκοβατὲς δῶ.** Note keeps "floor or threshold" open, l and i match the row. Kept.
- **8.322–323 ἐριούνης, ἑκάεργος.** Unknown/disputed meanings are said to be so; rows agree with l and i. Kept.
- **8.338 ἀργεϊφόντης and 8.335 διάκτορος.** Match table rows 113 and 114 and the shipped 022–023 wording. Kept.
- **8.334 l "And Hermes was addressed by the lord …".** The passive is an admitted device to keep the Greek order and is in the row. Kept.
- **8.346 l/i.** Adapts the shipped 002.120 line by changing "her" to "him" as the Greek μιν requires. Kept.
- **8.359 i "So he spoke, and …".** The shipped precedent (002.125, 009.51 …) uses "So he spoke" for ὣς εἰπών, but here the "he" and the subject μένος Ἡφαίστοιο are the same person, so I changed it (see table) rather than refuse.
- **8.360 βεβήκει "had gone" against i "went off".** The known glossary entry says "had gone, went"; the pluperfect is given in `l`. Kept in `i`.
- **Notes with an ASCII apostrophe (Ares', Hephaestus').** The apostrophe rule is for the Greek text and glossary entries; shipped notes use the ASCII form. Kept.
- **8.324 i drops "female" (θηλύτεραι θεαί).** The note explains it, and `l` keeps it. Kept.
- **8.329 mark "The gods speak" though the speaker is one god at a time (τις).** The mark is a label for the group who speak; the note says so now. Kept.
- **8.349 / 8.354 / 8.357 reply-formulas.** Match table rows 126–127 and the new rows. Kept.
- **8.369 half-line and 8.386.** Identical to the shipped units apart from a lower-case "and" after a comma, which is right in context.
- **New row ἀμφιγυήεις "the both-limbed one".** A guess, honestly said to be one; avoids the two guesses. Kept.
- **Gloss δαΐφρων, ἀμφιγυήεις, διάκτορος, ἐριούνης, ἑκάεργος.** Each says the sense is uncertain or disputed; consistent with the notes. Kept.
- **Gloss 13 broadenings other than the ones edited (αἴσιμα, γένοιτο, γίγνωσκον, θεοὶ, κακὰ, κατέδραθον, κυνώπιδος, μάκαρες, χρεῖος, ἱερὸν, ἴδησθε, ἵνα).** Each old entry kept whole and the new reading checked against the line; all true.

## Gate result (scratch copy)

Build: BUILT, 61 units, 95 lines, 160 new glossary forms, 20 broadened. Validate: every check passes except line 384 (unresolved item 1). The two length WARNs (units at 8.329 and 8.357) were fixed. Scansion flag: 8.355 only, confirmed above.
