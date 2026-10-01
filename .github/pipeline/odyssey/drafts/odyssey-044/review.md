# odyssey-044 review (9.475–566)

Reviewer pass on `units.json` (edited in place by script; `t`, `ln`, `p`, `mark` verified byte-identical to the drafter's file). Two passes: pass 1 (grammar labels, positional claims, cross-references, Greek → l, l ↔ i, house renderings, remembered English, quotation marks, paragraph flags); pass 2 re-read every unit after the fixes, re-ran the mechanical checks (concat = edition; every whole-unit repeat has identical l and i; l line counts; no `\n` in i; speech marks open and close at 0/1, 9/12, 14, 16/23, 25, 27/28; marks on the first unit of each of the six speeches) and checked `gloss.json` (106 entries, present and unchanged between the two passes).

## Counts

Changes made: 39 (high 0, medium 20, low 19). Findings refused: see below. Gloss findings reported to the glosser (not edited): 6.

Severity key: high = the unit says something false about the Greek or the shipped English contradicts it; medium = a label, parse or rendering that is wrong or breaks a house row; low = wording, trimming, cleanup.

## Drafter flags resolved

1. **9.522 `she/her`.** `validate_odyssey.py` check 6 keys on `letters_only(t)` of the whole unit against every published story and, for the same part, against earlier units; a unit whose Greek matches must have `l` and `i` identical to the first one. Unit 522 is a whole unit with the same Greek as odyssey-017 (lines 375, 394) and odyssey-018 (464), all with `So she spoke, …`. So the check is enforced and `l`/`i` stay as published; the conventions table itself calls this the 'gender-neutral formula fixed at 4.464'. I changed only the note (memo 'flagged for the reviewer' removed; it now says plainly that the Greek does not say which sex speaks and that 'she' and 'her' are to be read 'he' and 'him' here). The same problem will recur wherever this line is spoken of a man; a validator exception, or a neutral first rendering (`So he/she spoke`), is a decision for the caller.

2. **κὰδ’ δ’ at 9.539.** Confirmed in the source JSON (`source/odyssey-murray1919.json`) as printed with the apostrophe after κὰδ; `t` is kept as printed. It is not a true elision: κατά loses its last syllable by apocope and assimilates to the δ’ that follows, so no apostrophe is needed; read it as the κὰδ δ’ of 482. The note at 537 now says this instead of 'appears to be a misprint'.

3. **Words said to be unknown.** Checked: θέμωσε (486, 542), ἄκικυς (515), ἐρίηρες (555), ἀπέλεθρον (538) are each said to be unknown or uncertain in the note where the word first or most prominently stands, and the new-renderings rows say so. Nothing is papered over. ἀμύμων, διάκτορος, ἀτρύγετος etc. do not occur in this part. κελαινεφής and παλαίφατα are transparent compounds and rightly carry no 'unknown' note. No change needed.

## Changes

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 475 | n | low | note over the 110-word band (114); 'in the Cyclops' eyes' stated without a cross-reference | trimmed; cross-reference to 513–516 added |
| 480 | n | low | note 146 words, over the band | trimmed to about 105 words; no claim changed |
| 484 | n | medium | note said ἐκλύσθη is κλύζω 'with ἐκ-, up out'; the form is ἐ-κλύσθη, an ordinary augmented aorist (an ἐκ- compound would be ἐξεκλύσθη), so the claim was false of this form | claim replaced by the augment parse |
| 485 | n | low | note named the ship's word in 482 as νηός; the line prints νεὸς | corrected to νεός |
| 485 | n | low | note glossed 'back-surging' while l has 'back-flowing' (note and l disagreed) | note now matches l |
| 487 | n | medium | note said κελεύω takes the dative here; the dative ἑτάροισι is governed by ἐποτρύνας (κελεύω normally takes the accusative), so the label was doubtful and misleading | re-attributed the dative to ἐποτρύνας |
| 491 | l | medium | l 'twice so much of the salt-sea' read ἅλα as a partitive genitive; ἅλα is accusative (the ground covered), and δὶς τόσσον is adverbial. Also 'I was addressing' breaks the house προσηύδων 'I spoke (to)' (conventions row 9.363: 'addressed' reserved for προσέειπε/προσέφη) | l recast with the accusative kept apart from the adverb; 'I spoke to' as in the house row |
| 491 | i | medium | i 'then I called out to the Cyclops' varies the house προσηύδων 'I spoke to' (and 'the sea' for ἅλα where the house i is 'the salt sea') | i now 'I spoke to', 'the salt sea' |
| 491 | n | medium | note glossed 'I was addressing', matching the old l | note matches the new l; ἅλα parse made explicit below |
| 491 | n | low | note did not say the case of ἅλα, which the old l had misread | case stated |
| 492 | l | medium | l and i rendered μειλιχίοις as 'soothing'; the house row for μειλίχιος (9.363) is 'gentle' and lists 'soothing' as avoided | 'gentle words' in l and i |
| 492 | i | medium | see l: 'soothing' is on the avoided list for μειλίχιος | 'gentle words' |
| 492 | n | low | note glossed 'gentle, soothing' | 'gentle' only |
| 497 | l | low | l 'by throwing a jagged rock' lost the dative of μαρμάρῳ and made the aorist participle βαλών an -ing form, hiding both | dative and participle kept |
| 502 | n | low | note 116 words; 'the speech's whole point' is an overstatement | trimmed |
| 506 | i | medium | i 'So I said' folds the ἠμείβετο formula into the προσέειπεν formula; the house row 9.272 (ὣς ἐφάμην … ἀμείβετο) keeps 'So I spoke' and forbids that fold. Also own unit 2 had 'So I spoke' | 'So I spoke'; new-renderings.md row for 9.506 changed to match |
| 513 | n | low | clumsy wording that misdescribed the relation ('the word of which 475 had') | reworded |
| 515 | l | medium | l 'me, being small and worthless and feeble' attached the nominative participle ἐών to μ’ 'me'; ἐών agrees with the unstated subject (Odysseus), as the note itself said (note contradicted its own l) | 'he being' supplied so the participle goes with the right word |
| 515 | i | low | i 'blinded me of my eye' is not English | 'blinded me in the eye' |
| 519 | n | low | note said the verbs at 519 and 527 are 'the same in form'; εὔχεται (present) and εὔχετο (imperfect) are different forms of one verb | corrected |
| 522 | n | medium | note said 'This is flagged for the reviewer' (drafter's memo left in a reader-facing note) and described 'she/her' as standing for 'he/him' without saying plainly that the Greek is neutral. The validator (validate_odyssey.py check 6) forces l and i to be identical to the published unit with the same Greek, so 'she/her' must stay | memo removed; note now says plainly that 'she/her' are inherited and are to be read 'he/him'; l and i untouched |
| 526 | i | low | i 'So I said' for a non-reply ὣς ἐφάμην; published precedent (odyssey-042 line 353) and own unit 2 use 'So I spoke' | 'So I spoke' |
| 526 | i | medium | i ended in a semicolon while l and the note have a colon and a speech (Greek ano teleia introducing the prayer) follows | colon |
| 528 | i | low | i had 'reach his home … who has his home' (οἴκαδ’ and οἰκί’ both 'home' in one sentence); the fixed i of 505/531 'has his home' stays | οἴκαδ’ rendered 'home', as l already has |
| 537 | i | medium | i dropped ἐξαῦτις 'again' though the note glosses it | 'again' restored |
| 537 | l | low | unit 30 ended with a full stop and unit 31 (forced identical to unit 3 by the validator) begins lower-case 'and the sea' | semicolon in l and i, as the units before it do |
| 537 | i | low | same | same |
| 537 | n | medium | note glossed ἀπέλεθρον 'immense' (on the avoided list, reserved for ἀθέσφατος); note said the apostrophe 'appears to be a misprint' without saying why; ἐπιδινήσας 'whirled' vs l 'swung'; note 125 words. Drafter flag (2) κὰδ’ δ’ resolved: t is kept as printed, the note says it is not a true elision | 'immense' dropped; κὰδ’ δ’ explained (apocope, not elision); 'swung'; trimmed; 540 note corrected to say the punctuation difference ('full stop for its comma') |
| 541 | n | low | note 14 words, under the 20-word floor | extended |
| 543 | n | medium | note called ἥατ’ ἥαται, a present, in a past narrative whose l has 'sat'; the elided form read as ἥατο is the imperfect (the shipped glossary entry for ἥατ gives ἥατο) | corrected parse |
| 546 | i | low | i 'There we came in' added 'in' and left ἐλθόντες unrendered as a participle | participle kept |
| 548 | l | medium | μῆλα rendered 'sheep'; the house row (9.184/9.187) is 'flocks', 'sheep' being kept for ὄις. The second line is the published l and is unchanged | 'flocks' |
| 548 | i | medium | see l | 'flocks' |
| 548 | n | medium | note glossed 'sheep' | 'flocks' |
| 550 | l | medium | μήλων rendered 'sheep' (house: 'flocks') | 'flocks' |
| 550 | i | medium | see l | 'flocks' |
| 550 | n | medium | note called μήλων δαιομένων a genitive absolute, which fits i ('when …') but not l ('from the flocks …'); l and i took different constructions with no note saying so. Also 'sheep' and a 122-word note | note now says the Greek leaves both readings open; trimmed |
| 553 | i | low | i 'all my well-benched ships' added a possessive that the Greek has only for the companions (ἐμοὶ … ἑταῖροι) | 'my' removed from the ships |
| about | about | low | 'alone' is not in the Greek (ὀλέσας ἄπο πάντας ἑταίρους 'having lost all his companions'); 'sheep' for μῆλα (house 'flocks') | both corrected |

Also changed: `new-renderings.md`, row for 9.506, `i` now `So I spoke, and he groaned and answered me:` with 'So I said' added to its avoided column (same reason as the 506 `i` edit above). The row for 9.526 (ὣς ἐφάμην … εὔχετο) is not in the table; the unit's `i` now follows odyssey-042 line 353 ('So I spoke').

## Findings considered and refused

| where | finding | reason refused |
|---|---|---|
| 477 i | `Cruel one` capitalised mid-sentence | The house row for σχέτλιε (9.351) fixes `i` as 'Cruel one' with capital; the drafter applies it consistently in l and i. Left. |
| 481–483 / 537–540 | `i` 'hurled it, and cast it down' double verb | ἧκε and ἔβαλε are two verbs in the Greek (hurled / cast down); `l` and `i` keep both. Left. |
| 490 i | 'threw themselves forward' for προπεσόντες 'falling forward' | Matches the shipped glossary entry gloss ('throwing themselves forward') and 489 `i` ('throw themselves upon the oars'); the sense is the same. Left. |
| 502 l/i, 531 l/i | 505 = 531, `i` 'who has his home' beside 'reach home' | 505 and 531 are the same line and must be identical (validator check 6); the fix was made on the other side (οἴκαδ’ → 'home' only), see Changes. |
| 500 i | προσέφην rendered 'addressed' | Conventions row 9.363: 'addressed' is reserved for προσέειπε / προσέφη; προσέφην is that verb. Left. |
| 517 l/i | 'to give you an escort' adds 'you' (δόμεναι has no stated recipient) | The recipient (Odysseus, the τοι of the same clause) is the only possible one; `l` already keeps the Greek order. Left. |
| 504 note | αἴ κέν 'if ever', 'αἲ is a form of εἰ, used before κε' | Matches the shipped glossary entry for αἴ. Left. |
| 486 / 542 θέμωσε | l/i 'forced' | Row in new-renderings.md says sense unknown, note says so at 486 and 542. 'forced' is the drafter's context reading and stated as such. Left. |
| 513 ἐδέγμην | note calls it 'a past form' of δέχομαι | Vague but not false (shipped glossary: 'aor. (root form)'); sentence meaning 'I was expecting' is carried by l/i. Left. |
| 486 κατερχομένης ὑπὸ πέτρης | genitive with ὑπό 'beneath' as 'under … as it came down' | Genitive with ὑπό of the thing from under which / by which: sense fine. Left. |
| 492 l | 'my companions' without a possessive in the Greek (ἑταῖροι) | The same drafter pattern in 543, 560 and in the shipped parts; context makes them his. Left. |
| scansion | none flagged in the packet | Ran scan_hexameter.scan_line on all 92 lines: every line fits as a hexameter with no unresolved flag (only ordinary licences: correption, hiatus, synizesis of -εω/ἡμέων/ἡμέας, mute+liquid, initial ρ doubled in ἐπὶ ῥηγμῖνι, lengthening before ἀκαχήμενοι at 565). No unit note needs an irregularity sentence. |
| note word counts | notes of units 0, 2, 30, 36 are 115–123 words by whitespace split | Validator warns only outside 20–130; all inside. Nothing to do beyond the trimming already done. |

## Gloss findings (`gloss.json`, not edited: the glosser owns it)

| form | issue | severity |
|---|---|---|
| εἴρηται | `ἐρέω (λέγω) … perf. pass. 3 sg. 'has been said, was foretold'` is the wrong verb for 9.503. αἴ κέν τίς σε … ὀφθαλμοῦ εἴρηται … is 'if anyone asks you about …': aor. subj. mid. 3 sg. of εἴρομαι 'ask' (= ἔρηται). The note at 502 says so; the gloss contradicts it. Medium (wrong parse in a shipped reference). | medium |
| ἐκλύσθη | `κλύζω (ἐκ-)` implies an ἐκ- preverb; the form is ἐ-κλύσθη, augmented aor. pass. of κλύζω (same correction as made to the note at 484). | low |
| κεκοτηότι | `neut. dat. sg.`: it agrees with θυμῷ, masculine. | low |
| ὀτρύνω | `pres. 1 sg. 'I urge'`: in 517 it stands in a purpose clause after ἵνα, so pres. subj. 1 sg. (short-vowel form, same as the indicative), 'I may urge'. | low |
| κατεγήρα | `aor. 3 sg., epic -α (= κατεγήρασε)`: the form is equally the imperfect, which is how the note at 510 takes it ('was growing old'); say 'impf. (or aor.)'. | low |
| κρονίδῃ | `(Κρονίδῃ = Attic Κρονίδῃ)` says nothing; drop the parenthesis or give the real contrast. | low |

All other 100 gloss entries were checked against this part's l, i and notes: parses agree (θέμωσε, ἥατ in known-forms = ἥατο imperf, ἀπῆμεν, ἅζεο, ἐδεύησεν, ἐκέκαστο, κίοι, φάμεν, ἑὴν, etc.). `known-forms.json` entries were checked for the forms the notes lean on and need no change.
