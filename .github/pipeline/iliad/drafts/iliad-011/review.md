# iliad-011 — review (Iliad 2.369–468)

Two passes over `units.json` (47 units). Pass 1: notes' labels and cross-references, then Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks, published-English reuse (Iliad and Odyssey). Pass 2: the whole of `l` and `i` read again in their final state, every edited note re-read, `new-renderings.md` brought into line. `t` was not touched (checked by script: every `t` identical before and after). `units.json` was edited in place by script (`json.dumps(..., ensure_ascii=False, indent=1)`, byte-identical round trip before editing). The build was not run. `gloss.json` did not yet exist, so no parse in it was checked; the glosser's output still needs the second-pass read the runbook asks for.

Totals: 19 changes — 0 high, 6 medium, 13 low.

## Changes

| line · field · severity | what was wrong | what was done |
|---|---|---|
| 373 · n · medium | The note derived ἠμύσειε from ἀμύω. An optative takes no augment, so the η is in the stem: the verb is ἠμύω ‘bow down, sink forward’ (the drafter's own caution against ἀμύνω was right, the lemma was not). | Note now says ‘the aorist optative of ἠμύω’. `new-renderings.md` row corrected the same way. |
| 446 · n · medium | The note said the verb of μετὰ δὲ γλαυκῶπις Ἀθήνη was ‘carried over from θῦνον’. False: Athena's verb is διέσσυτο at 450, after the picture of the aegis; θῦνον is the kings' verb. | Note now says Athena's verb is διέσσυτο at 450 and that the English supplies ‘was’ to carry the picture. `l` and `i` unchanged. |
| 416 · i · medium | `i` read ‘…and burned its doors with hostile fire,’ / ‘and tear Hector’s tunic…’: after ‘before I have thrown down … and burned’ the third infinitive came out as a bare ‘tear’, which does not parse. | `i`: ‘and torn Hector’s tunic to rags about his chest with bronze;’ (so the three verbs after ‘before I have’ agree). Row in `new-renderings.md` updated. |
| 400 · l, n · medium | Odyssey formula not reused. The Odyssey table fixes θεῶν αἰειγενετάων as `l` ‘of the gods, the forever-born’ (24.373) and ships ‘forever-born’ at 14.446, 23.81 and odyssey-008/-070/-111/-118; the draft had ‘ever-born’ with no departure noted. | `l`: ‘of the gods, the forever-born,’. Note's two ‘ever-born’ glosses changed to ‘forever-born’. Row rewritten (follows 24.373). `i` ‘everlasting’ was already right. |
| 412 · l, i · medium | Odyssey half-line not reused. αἰθέρι ναίων is shipped in odyssey-076 as `l` ‘in the aether dwelling’, `i` ‘who dwells in the bright upper air’; the draft had ‘in the upper air dwelling’ / ‘who dwell in the upper air’ and rejected ‘aether’ without marking a departure. | `l`: ‘in the aether dwelling’; `i`: ‘who dwell in the bright upper air’. Row rewritten. δι’ αἰθέρος at 458 stays ‘through the upper air’, which is what the Odyssey ships for the word elsewhere (odyssey-022, -074). |
| 459 · i · medium | Departure from the table without need. The Iliad table fixes ἔθνεα as `l` ‘tribes’, `i` ‘swarms’ (2.87, 2.91), and the second simile answers the first with the same word (ὣς τῶν ἔθνεα πολλά, 464). The draft's ‘flocks’ for the birds broke the echo in `i`. | `i`: ‘the many swarms of winged birds’. Note says ‘swarms … as at 464’. The departure row was replaced by a row that follows the table. |
| 379 · i · low | Odyssey phrase not reused. οὐδ’ ἠβαιόν at the end of 3.14 ships `l` ‘not even a little’, `i` ‘not the least bit’; the draft's row claimed the Odyssey's rendering was ‘not at all’, which is not what odyssey-009 has. | `i` ends ‘not the least bit.’ (`l` was already the Odyssey's). Row corrected. |
| 386 · i · low | Same phrase, same repair, kept identical to 379. | `i`: ‘…no pause among us, not the least bit, unless night comes…’. |
| 402 · l · low | `l` ‘five years old’; the Odyssey ships πενταέτηρον as ‘five-year-old’ in `l` (odyssey-070, -096). | `l`: ‘a fat one, five-year-old,’. Row corrected. |
| 404 · i · low | `i` began a new sentence with capital ‘He summoned…’ after the previous unit's `i` ended on a comma (402–403); the pilot continues lower-case across such a break. | `i`: ‘and he summoned the elders…’ (δέ, as in `l`). |
| 465 · l · low | κονάβιζε `l` ‘resounded’ collided with σμαραγεῖ ‘resounds’ three lines earlier, and iliad-010 ships κονάβησαν as ‘rang’ (odyssey-049 κονάβιζε likewise). | `l`: ‘frightfully rang with the feet…’. Row corrected. |
| 437 · i · low | ἴομεν is hortatory (‘let us go’), parallel to the heralds' imperative; ‘while we go’ turned it into a statement. | `i`: ‘…along the ships, and let us go all together in this way…’. |
| 396 · n · low | Note said ἔνθ’ ἢ ἔνθα is ‘the same words as’ ἔνθα καὶ ἔνθα (462). It is not the same words (ἢ / καί), only the same sense. | ‘the same sense as’. |
| 410 · n · low | περιστήσαντο was glossed ‘they stationed themselves round, with the ox as its object’, which contradicts itself. | Now: with the ox as object it is literally ‘they set the ox round (themselves)’, and the sense is ‘stood round the ox’. |
| 467 · n · low | ἀνθεμόεις is from ἄνθεμον ‘blossom’, not ἄνθος. | Note corrected. |
| 370 · n · low | Note stated flatly that αὖτ’ looks back to Nestor's speech in Book 1 (1.254–284). It may equally mean the speech just ended; the Greek does not say. | Note now says it ‘may recall’ the Book 1 speech ‘or simply the speech he has just made’. |
| 371 · n · low | Double space after ‘Achaeans’.’ | Single space. |
| 412 · n · low | Note was 147 words (validator warns above 130). | Trimmed to 128 words: two glosses and a parenthetical dropped, no claim changed (‘upon (us)’ became ‘upon’, since the Greek has only ἐπί). |
| 459 · n · low | Note was 177 words; it also cited the dative as Ἀσίῳ while `t` prints Ἀσίω (no iota subscript). | Rewritten to 128 words; cites Ἀσίω as printed (‘the dative, usually written Ἀσίῳ’); ‘swarms’ as above. |

## Drafter's flagged notes — verified

- ὀρέοντο (398): ‘an epic form with the root of ὄρνυμι’ is true and suitably hedged (the epic imperfect middle, ‘they hurried off’). κεδασθέντες as passive participle of κεδάννυμι is right. No change.
- ἠερέθονται (448): ‘from a rare verb … hang waving’ is the traditional sense of ἠερέθομαι (hover, flutter); the note does not claim more. No change.
- παιφάσσουσα (450): ‘participle of the rare verb παιφάσσω, “darting about” being the usual understanding’ is true and hedged. διέσσυτο as aorist middle of διασεύω is right; σὺν τῇ = ‘with the aegis’ is right. No change.
- λεγώμεθα (435): ‘hortatory subjunctive of λέγομαι’ is a true label; the note already says ‘talk’ is the usual understanding and not certain. The `l`/`i` ‘talk’ matches. No change.
- ἀΐδηλον (455): ‘either “destroying” or “unseen”, and the English takes the first’ is true; `l` ‘destroying’ / `i` ‘destructive’ is the Odyssey's ἀίδηλον Ἄρηα (8.309) and ἀΐδηλον ὅμιλον. No change.
- ἄρκιον (393): ‘sufficient, certain’ as the usual understanding, with ‘no sure way for him’, is correct. No change.

## Other checks that passed

- Every cross-reference was looked up: 1.4–5, 1.130, 1.184, 1.220, 1.254–284, 1.304, 1.317, 1.458–461, 1.464–468, 1.469, 2.50–52, 2.91, 2.100, 2.111–112, 2.121, 2.149–154, 2.169, 2.362, 2.368 (end of Nestor's speech, last unit of iliad-010 closes with ”), Od. 3.67–68, Od. 11.397.
- Published repeats, compared by script on the letters of `t`: 369 (= iliad-002), 421–424 and 427–429 and 430–431 (= iliad-005), 444 (= iliad-007), 432–433 (= odyssey-009) are all identical in `l` and `i` to the published unit. 442–443 follows iliad-007 (2.50–51) and odyssey-005 correctly. 371–372 matches the Odyssey's shipped αἲ γάρ… `l` and `i` word for word (odyssey-017/-032/-083/-090/-118). 407 matches iliad-008 (2.169). 464 reuses the published wording of 2.91 for its first line.
- Odyssey formula reuse otherwise correct: κελαινεφές ‘dark-clouded one’ / ‘you of the dark clouds’ (odyssey-063); ὠκυπόδεσσιν ‘swift-footed’; θᾶσσον ‘the more quickly’ / ‘the sooner’; ἄφαρ ‘straightway’ / ‘at once’; ἔνθα καὶ ἔνθα ‘here and there’ / ‘this way and that’; χαλκοχιτώνων, γλαυκῶπις, διοτρεφέες βασιλῆες, Παναχαιῶν, βοὴν ἀγαθός, ἀμέγαρτον, μέλαθρον (departure marked and reasoned), ἀνθεμόεις, κλαγγή, ἐΰξοον, ἱππότα, ἀγήρως.
- Quotation marks: speech 1 (370–393) opens on the unit at 370 (`mark`) and closes at 393; speech 2 (412–418) opens at 412 and closes at 418; speech 3 (434–440) opens at 434 and closes at 440; interior units carry none; counts 3/3 in both layers. No speech runs on into the next part (the part ends in narrative at 468).
- `ln` of each unit checked against the packet (including the mid-line units at 417, 451, 465), `l` line counts equal `t` line counts, `p` on 369, 394, 419, 441, 455, 459 only (the six ¶ marks of the packet), `mark` on the first unit of each speech.
- Scansion flags: none listed in the packet, so no hand scansion was required and no metrical sentence was added to any note. No irregularity was met in reading.
- Numbering jumps: none fall in 2.369–468; no bracketed lines; no note needs the edition-spot sentence.

## Findings considered and refused

- 408 `i` ‘unbidden’ for αὐτόματος: an ordinary word, rebuilt from the adjective's sense (‘self-moved’), and `l` has the literal ‘of his own accord’. Left.
- 418 `i` ‘bite the earth’ for ὀδὰξ λαζοίατο γαῖαν: the literal Greek is ‘take the earth with the teeth’ (kept in `l`); ‘bite the earth’ is the plain English for that act and the row lists the rivals it avoids. Left.
- 414 `i` ‘Priam’s palace’ for μέλαθρον (`l` ‘roof’): departure from the Odyssey's ‘rafter’ is already argued in the row (a house, not a single beam). Left.
- 468 `i` ‘countless as the leaves and flowers that come in their season’ and 467 ‘flowery meadow of the Scamander’: both follow the Greek's word order and sense (μυρίοι, ὅσσα τε, Σκαμανδρίῳ ἀνθεμόεντι) and were rebuilt in the drafter's own words; no phrase carries over from any translation I could identify. Left.
- 419 `l` ‘did the son of Cronus bring it to fulfilment’ for the imperfect ἐπεκραίαινε: a negated imperfect of this kind is naturally ‘did not (yet) fulfil’; the pilot does the same with negated imperfects. Left.
- 434 `i` drops νῦν (‘no longer now’) into ‘now’ attached to ἐγγυαλίζει: ‘no longer’ keeps μηκέτι, and `l` carries both words; the force is not lost. Left.
- 441 `i` ‘So Nestor spoke’ where the Greek has only ὣς ἔφατ’: the speaker is named for clarity, as at 394 for Agamemnon; harmless. Left.
- 398 `i` ‘scattering’ for the aorist passive κεδασθέντες: the note and `l` (‘scattered’) carry the passive; `i` reads naturally. Left.
- 375 `i` ‘has given me pains’ for the aorist ἔδωκεν: perfect for aorist is a normal English choice for a present state of affairs. Left.
- 400 `l`/`i` ‘Ares’ for battle and 381/440 Ἄρηα: consistent with the Odyssey table's use (20.50) and the notes say Ares stands for war. Left.
- Table row for ὑπερμενέϊ Κρονίωνι: not a new row (the Odyssey table already has ὑπερμενής ‘exceeding-strong’ / ‘of surpassing strength’); the draft's wording follows it. Left.
