# Review of odyssey-056 (Odyssey 11.538–640)

Two passes over `units.json` (pass 1: grammatical labels, word-position claims, cross-references, notes against `l`/`i`; pass 2: Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks), then `gloss.json` checked against the lines. `t` was not touched (checked afterwards: the units' `t` joined still reproduces the packet's 103 lines). `units.json` was edited in place by script; every edit asserted its old text occurred exactly once.

Severity: **high** = the English or a note says something false about the Greek or changes its sense; **medium** = wrong cross-reference, house-rule departure, note contradicting `l`/`i`, or a muddled statement; **low** = polish, over-statement, or consistency.

Totals: 36 edits to `units.json` and 7 to `gloss.json`; by severity high 5, medium 15, low 23.

## Changes to units.json

Line = the unit's `ln`; unit = index in `sentences` (0-based).

| Line | Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|---|
| 538 | 0 | n | medium | Note labelled γηθοσύνη a dative, but the printed form has no iota subscript and is formally nominative; label made true of the form. | “γηθοσύνη is a dative of cause, ‘in joy’;” → “γηθοσύνη is ‘in joy’ (printed without an iota subscript, so the form can be read as a nominative in …” |
| 541 | 1 | n | low | Cross-reference overstated: the whole formula νεκύων κατατεθνηώτων recurs at 564 only; 567 has only κατατεθνηώτων. | “a formula that returns at 564 and 567 (” → “a formula that returns at 564, and κατατεθνηώτων again at 567 (” |
| 541 | 1 | n | low | Tense label (aorist) asserted for a form that is the Homeric past of εἴρομαι and is labelled imperfect in LSJ-type usage; made neutral rather than wrong. | “εἴροντο is the aorist middle of εἴρομαι ‘ask’” → “εἴροντο is a past middle form of εἴρομαι ‘ask’” |
| 549 | 6 | n | medium | Cross-reference pointed to 11.467, which is where the earlier unit begins, not where the repeated line stands (470). | “The last line repeats the last line of a unit in the part before (at 11.467), an…” → “The last line repeats the last line (11.470) of the unit that begins at 11.467 in the part before, a…” |
| 549 | 6 | i | low | Packet: a repeated line takes the published wording as far as the sentence allows; published i has ‘after the blameless son of Peleus’, draft added ‘next’. | “in form and in deeds, next after the blameless son of Peleus.” → “in form and in deeds, after the blameless son of Peleus.” |
| 552 | 7 | n | low | Note offered ‘honeyed’ and ‘gentle’ as glosses, both on the avoided list for this formula in new-renderings.md. | “(μειλίχιος ‘soothing, honeyed, gentle’;” → “(μειλίχιος ‘soothing’;” |
| 553 | 8 | n | high | False word-position claim: εἵνεκα stands before τευχέων (χόλου εἵνεκα τευχέων), not after it. | “εἵνεκα is ‘on account of’ and follows τευχέων, the genitive plural of τεῦχος ‘arms’.” → “εἵνεκα is ‘on account of’ and governs τευχέων, the genitive plural of τεῦχος ‘arms’; it stands befor…” |
| 553 | 8 | n | medium | Cross-reference wrong: the 9.2 speech was closed at 11.360; the speech that is still open was reopened at 11.378 (odyssey-054). | “so the mark is the single ‘ ’; the double “ opened at 9.2, where Odysseus began …” → “so the mark is the single ‘ ’; the double “ with which Odysseus’ long speech was opened afresh at 11…” |
| 555 | 9 | i | medium | House rule: πῆμα is kept ‘woe’ (row for 5.179); ‘bane’ is not the house word. | “The gods made them a bane to the Argives” → “The gods made them a woe for the Argives” |
| 556 | 10 | n | low | Note presented one agreement for φθιμένοιο although the genitive is equally possible with Achilles; the ambiguity is now stated. | “it most naturally agrees with σεῖο, ‘you having perished’, although it stands af…” → “it most naturally agrees with σεῖο, ‘you having perished’, although it stands after Πηληϊάδαο and co…” |
| 562 | 13 | n | low | Note quoted the words in an order the line does not have. | “θυμὸν ἀγήνορα (accusative of θυμὸς ἀγήνωρ)” → “ἀγήνορα θυμόν (accusative of θυμὸς ἀγήνωρ)” |
| 563 | 14 | i | medium | House row for ψυχὴ νεκύων κατατεθνηώτων (11.37): ‘of the dead, of those who had died’; the draft’s i varied it, though unit 1 of the same part has it correctly. | “the souls of the dead who had died.” → “the souls of the dead, of those who had died.” |
| 563 | 14 | n | low | Note called the whole line the formula; only its second half is. | “The last line is the formula already met at 541.” → “The words νεκύων κατατεθνηώτων are the formula already met at 541.” |
| 565 | 15 | n | low | Tense label: προσέφη is imperfect or aorist (the forms coincide; the repository labels it both ways); ‘past’ is true under either. | “with an aorist indicative, as in προσέφη, κε marks” → “with a past indicative, as in προσέφη, κε marks” |
| 565 | 15 | n | low | Same point. | “προσέφη is the aorist of πρόσφημι ‘speak to’.” → “προσέφη is a past tense of πρόσφημι ‘speak to’.” |
| 565 | 15 | i | low | κεχολωμένος is ‘enraged’ in both layers at 544 (same participle), i changed to ‘angry’. | “angry as he was” → “enraged as he was” |
| 568 | 17 | l | low | Note says κατά with the accusative is ‘throughout’ and i has ‘throughout’; l had ‘in’. | “sitting and standing in the wide-gated house of Hades.” → “sitting and standing throughout the wide-gated house of Hades.” |
| 568 | 17 | n | medium | Note said the first layer keeps the ambiguity, but l says ‘around him’ outright, like i: note contradicted l. | “and ἀμφί is either the adverb ‘around’ or ‘about’ the judgments; the first layer…” → “and ἀμφί could be the adverb ‘around’ (him) or ‘about’ the judgments (ἀμφὶ δίκας); both layers take …” |
| 572 | 18 | i | low | Repeated κατ’ ἀσφοδελὸν λειμῶνα is ‘along the asphodel meadow’ in both layers at 539; i had ‘over’. | “over the asphodel meadow” → “along the asphodel meadow” |
| 572 | 18 | n | low | ‘desolate’ is on the avoided list for οἰοπόλος in new-renderings.md. | “usually glossed ‘lonely, desolate’, and” → “usually glossed ‘lonely’, and” |
| 577 | 20 | i | low | δύνοντες is ‘entering, sinking into’ (as the note says); ‘burrowing’ adds a manner the Greek does not give. | “burrowing into the membrane within” → “sinking into the membrane within” |
| 580 | 21 | l | low | ἕλκησε is ‘dragged’; ‘away’ is not in the Greek. | “for Leto he dragged away,” → “for Leto he dragged,” |
| 580 | 21 | n | high | Wrong grammatical label: the note called Λητώ nominative while calling it the object of the verb. | “Λητώ is the nominative, here the object of ἕλκησε,” → “Λητώ is an accusative here (the form is the same as the nominative), the object of ἕλκησε,” |
| 585 | 25 | l | low | ἀπολέσκετ’ is iterative (-σκ-); the note says ‘kept being lost’, l had a plain ‘was lost’ while the next verbs have ‘kept’. | “so often the water was lost, swallowed up,” → “so often the water kept being lost, swallowed up,” |
| 588 | 26 | l | low | ὑψι- is ‘high’; ‘tall-leaved’ suggests tall leaves. | “And tall-leaved trees poured” → “And high-leaved trees poured” |
| 588 | 26 | i | low | Same. | “And tall-leaved trees shed” → “And trees with lofty foliage shed” |
| 588 | 26 | n | low | Same. | “δένδρεα ὑψιπέτηλα is ‘tall-leaved trees’ (ὑψι- ‘high’ + πέταλον ‘leaf’).” → “δένδρεα ὑψιπέτηλα is ‘high-leaved trees’, ‘trees with lofty foliage’ (ὑψι- ‘high’ + πέταλον ‘leaf’).” |
| 588 | 26 | n | medium | Note was garbled: it said χέε ‘takes a singular verb’, when χέε is itself the singular verb. | “χέε is the imperfect of χέω ‘pour’, with no augment, and takes a singular verb w…” → “χέε is the imperfect of χέω ‘pour’, with no augment, and stands in the singular with the neuter plur…” |
| 613 | 38 | i | high | i narrowed μηδ’ ἄλλο τι τεχνήσαιτο ‘nor contrive anything else’ to ‘another’ (belt); l and the note say ‘anything else’. | “never have made it, and never make another.” → “never have made it, and never make anything else.” |
| 613 | 38 | n | low | Hard spot 613–614: the second reading of μὴ τεχνησάμενος was not recorded. | “should neither have made it nor make anything again.” → “should neither have made it nor make anything again. The participle can also be taken as ‘having mad…” |
| 615 | 39 | n | medium | Cross-reference wrong: the earlier occurrence is in odyssey-047 (10.265), not ‘the part before’ (odyssey-055). | “The second line is the formula of the part before:” → “The second line stands in the same words at 10.265 (an earlier part):” |
| 617 | 40 | l | high | ὅν περ is ‘the very one which’ (as the note says): the same doom Heracles bore. l/i had ‘of the kind’/‘such as’, which changes the sense to a similar doom. | “of the kind I myself used to bear beneath” → “the very one I myself used to bear beneath” |
| 617 | 40 | i | high | Same. | “such as I myself bore beneath” → “the very one I myself bore beneath” |
| 626 | 46 | i | medium | δέ is ‘and/but’, not ‘for’; i made the clause causal, a force l does not have. | “for Hermes and gleaming-eyed Athena sent me.’” → “Hermes and gleaming-eyed Athena sent me.’” |
| 626 | 46 | n | medium | Note updated to match. | “δέ is ‘and’ (the first layer) or ‘for’ (the second, where it gives the reason), and ἰδέ” → “δέ is ‘and’ (the first layer; the second layer simply sets the clause beside the last), and ἰδέ” |
| 639 | 53 | n | medium | Same cross-reference error as unit 8. | “opened with the double mark at 9.2, is still open” → “opened afresh with the double mark at 11.378, is still open” |

## Changes to gloss.json

| Key | Severity | What was wrong | What was done |
|---|---|---|---|
| γηθοσύνη | medium | Parse said fem. dat. sg. ‘dative of cause’, but the printed form has no iota subscript and is formally nominative; both readings now given. | entry replaced: “γηθοσύνη — joy, gladness; fem. nom. sg., or dat. sg. γηθοσύνῃ (the printed form has no iota subscript): ’in joy’” |
| κρατερώτερον | medium | Parse said neut. acc. sg.; the noun is masculine (ἄλλον … ἄεθλον, ἄλλον cannot be neuter), so masc. acc. | entry replaced: “κρατερός — strong, hard, harsh; comp. κρατερώτερος, masc. acc. sg. (with ἄεθλον, masc. after ἄλλον): ’harder’” |
| νίκης | low | ‘Ionic -ης (= Attic -ης)’ equates a form with itself: Attic νίκης is identical. | entry replaced: “νίκη — victory; fem. gen. sg.” |
| τοῦδέ | low | Parse said neut. only; the noun compared with is ἄεθλον, which after ἄλλον is masculine, and the form is the same in both genders. | entry replaced: “ὅδε, ἥδε, τόδε — this; masc./neut. gen. sg., genitive of comparison: ’than this’” |
| ἕλκησε | medium | Entry gave ‘Attic εἵλκυσε’, a different aorist of another stem, and omitted the missing augment; the unit note says ἥλκησε. | entry replaced: “ἑλκέω (ἕλκω) — drag, pull about, maltreat; aor. 3 sg., unaugmented (= ἥλκησε); ἑλκέω is the epic form beside ἕλκω” |
| μὴν | medium | ‘epic/Ionic = μέν’ is wrong: μήν is a distinct particle, not a dialect form of μέν. | entry replaced: “μήν — truly, indeed; affirmative particle; καὶ μὴν ’and moreover, and further’” |
| ἑῇ | low | ‘dative of means’ described the phrase, not the form; made general. | entry replaced: “ὅς, ἥ, ὅν (possessive; epic ἑός) — his own, her own; fem. dat. sg. (with τέχνῃ)” |

Checked and left alone in gloss.json: the other 161 of the 168 novel-form entries parse correctly against their lines; all 16 `__broaden__` entries begin with the existing entry whole (verified by script against `known-forms.json`) and their added readings fit the lines they cite; no novel entry is 230 characters or longer; no ASCII apostrophes, no line numbers. A spot-check of about 70 known forms (ἦ, ἵνα, ὃς, ὅ, οἱ, τόν, τά, τῶν, μετ’, ἀμφί, κατά, ἐπί, περ, δῶ, σεῖο, σφιν, ἔλθοι …) found each existing entry already covers its use in this part.


## Decisions

**Quotation marks.** Checked by script: `“`/`‘` and closers occur only on units 8 (553, opens ‘), 13 (562, closes ’), 40 (617, opens ‘) and 46 (626, closes ’), with `l` and `i` agreeing; `mark` stands on 553 (“Odysseus to Ajax”) and 617 (“Heracles speaks”), the first unit of each speech; `p` falls on exactly Murray's thirteen paragraph openings. Both speeches lie inside Odysseus' own long speech to the Phaeacians, so the inner marks are single ‘ ’, as in odyssey-054 (397, 405) and odyssey-055 (436, 441, 473, 478, 488, 505). **The 055 line 463 question:** odyssey-055's unit at 463 opens with “ and closes with ” at 464, against the single marks round every other inner speech in that part. The cause is the repeated-line rule: that unit is the whole of 4.492 and 4.837, shipped before as top-level speech, and its note says the English "is kept exactly as when this half-line was shipped before". It is therefore a deliberate carry-over, not a drift in convention. Decision: odyssey-056 keeps ‘ ’ for both inner speeches (its own lines are not repeats of top-level speech: 553–562 and 617 onward are new, and the one repeated opening, 11.617 = 5.203, is a reuse of words, not of quotation state). Odyssey-055 is not edited. Remaining oddity for the owner: in 055 the one inner speech at 463–464 shows “ ”; the reader will see the double mark inside the long speech once. The outer double mark that is still open at the end of this part was reopened at 11.378 (odyssey-054), not at 9.2; notes at units 8 and 53 corrected.

**Scansion.** The packet flags none. Scanned by hand (and by `scan_hexameter.py`) every line the task named as hard: 556–558, 584, 597, 605–606, 613–614. All fit with no unexplained licence. The only licences are ordinary ones: 597 short final -ε of ἀποστρέψασκε before κρ- (mute + liquid, no position); 614 a long vowel kept in hiatus (ἑῇ ἐγκάτθετο); the digamma hiatuses at 573 (ὁμοῦ εἰλεῦντα) and 615 (ἐπεὶ ἴδεν). None is "really irregular", so no sentence was added to any note (the runbook asks for one only where the irregularity is real).

**The five hard spots, on the sense.**
- 11.613–614: the optative/participle wish read both ways; `i` fixed (high) to match `l` and the note; second reading added to the note.
- 11.597: κραταιίς read as a noun for a force (nominative); left. ἀποστρέψασκε has no object; the note already says so.
- 11.584: στεῦτο (disputed sense) and οὐκ εἶχεν ἑλέσθαι both stated as uncertain / idiomatic in the note; `l` and `i` agree. Left.
- 11.556–558: φθιμένοιο agreement stated as an option (low edit); κεφαλή periphrasis consistent in `l` and `i` and with new-renderings.md; the Ἀχιλλῆος/Ἀχιλῆος spelling remark verified (546 vs 557).
- 11.605–606: ἀτυζομένων left ambiguous (birds or dead) in `l`, `i` and note alike, as the Greek is.

## Findings considered and refused

1. **`i` omits φίλοισι (566, “in my dear breast”).** The note says so openly, and odyssey-034 (unit at 178) does the same ( `l` “dear breast”, `i` “the heart in my breast”). Consistent with precedent.
2. **“ruthless” for ἀναιδής (598) while νηλεής is “pitiless”, and the avoided-list at the νηλεής row names “ruthless”.** The avoided list is what NOT to use for νηλεής; ἀναιδής is a different word with its own new-renderings row, `l` keeps “shameless”, and νηλεής never appears in this part. No collision in the reader's text.
3. **“labours” for ἀέθλους/ἄεθλον (622, 624) against the table row that fixes ἀέθλους as “contests” “passim”.** The new row separates the games (contests, 548 here stays “contest”), the toils of Odysseus (trials) and the tasks imposed on Heracles (labours); the sense is different. Kept. When the row is copied into `conventions.md`, it should say it is a deliberate exception to row 621.
4. **`i` “rose” for ἦν in “around him rose a clamour” (605).** Idiomatic English for a noise, no sense added beyond the Greek's `ἦν`; `l` has “was”. Left.
5. **`i` “a labour … harder” / “stronger” in `l` (624).** Matches the new-renderings row.
6. **“long before” for τὸ πρόσθεν in `i` (627).** The gloss.json broadened entry for τὸ already says ‘died long before’; the adverb is “formerly”, “before”; “long” is a fair rendering of the time-gap between Theseus and Pirithous and Odysseus. Left.
7. **`i` “still more of the men of earlier times” (630) for ἔτι προτέρους ἀνέρας.** ἔτι is “still, further”, the comparative προτέρους “earlier”; `l` has “still earlier men”. Both defensible, no sense lost. Left.
8. **`l` “Not having contrived it” adds “it” (613).** The belt is the understood object; the note says the Greek has none, and omitting it would make the English unreadable. Left.
9. **`i` “has covered” (549) against `l` “covered”.** An English perfect for an aorist stating a present result; ordinary. Left.
10. **`i` “their feasts” (603) for θαλίῃς.** Possessive supplied by English, the feasts are the gods'. Left.
11. **`i` “were you then not to forget … even in death” (553) is stiff.** Not wrong: ἔμελλες + future infinitive, ἄρ’, question; the stiffness mirrors the Greek's reproachful irony. Left.
12. **`l` and `i` identical in the 632 unit.** Allowed; `l` is already close to the Greek.
13. **Remembered English.** Searched `i` for phrases that arrive fully formed: “ruthless stone”, “wide-gated house of Hades”, “caught sight of”, “pale fear”, “the Gorgon head”. Each was rebuilt from the grammar (ἀναιδής; εὐρυπυλές = εὐρύς + πύλη; εἰσενόησα; χλωρὸν δέος, already shipped at 11.43; Γοργείη κεφαλή as the new-renderings row). No change.
14. **“Odysseus to Ajax” as a `mark`** departs from the “X speaks / X answers” pattern. 054 already ships “Odysseus asks Agamemnon”; the form is fine.
15. **Unit 9 (555–556) `i` “for you, who were such a tower to them, perished”.** Moves the participial sense into a relative clause; the Greek has the same τοῖος πύργος ἀπώλεο apposition. Left.
16. **Reuse of published lines.** 11.589–590, 616, 617, 637 and 638 were compared with the published `l` and `i` (030, 047, 024, 040, 039): all match as far as the sentence allows (551 was brought into line, low edit above). No whole-unit repeat exists, so the validator's identical-unit rule does not apply.
17. **Titles and `about`.** `title`, `titleEn`, `part` and the cite agree with `parts.json` (11.538–640, 103 lines); `about` is accurate to the part.

## Notes for the publishing step
- The glosser's file was edited here directly; if the glosser writes again it will overwrite those seven corrections (listed above) — they should be re-applied.
- `units.json` has been rewritten with the same serialisation as before (indent 1, no trailing newline); `t` is byte-identical.
