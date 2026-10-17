# iliad-006 (Iliad 1.511–611) — review

Reviewer, two passes. `t` untouched (concatenated `t` re-checked against the packet lines: identical). Line counts of `t`/`l`, `ln`, `p` marks, `mark` fields and quote balance checked by script after the edits. Whole-unit reuse (1.560, 1.576, 1.601, 1.602) matches the published `l`/`i` exactly; the one line reused inside a unit (1.610) follows the published wording. No scansion flags in the packet, nothing to scan. The part ends outside any speech; the previous part (iliad-005) closes Thetis' speech at 1.510, so 1.511 correctly opens in narration; no iliad-007 exists yet.

Severity: major = breaks a gate or a sense; moderate = house-rendering conflict, `l`/`i`/note disagreement, or an undisclosed supply; minor = cross-reference, polish, wording.

## Pass 1 — changes made to units.json

| line · field | sev | what was wrong | what was done |
|---|---|---|---|
| 549–550 · l, i | major | Zeus' speech (545–550) never closed: the last unit lacked ” in both layers. | Added ” to `l` and `i`. |
| 536–538 · n | moderate | Note said “the line runs ‘and not him Hera … did not know’” and in the same breath that μιν goes with ἰδοῦσ’; the literal gloss contradicted the claim. (μιν is the object of ἰδοῦσα; ἠγνοίησεν takes the ὅτι clause.) | Rewrote: μιν is the object of ἰδοῦσ’; ἠγνοίησεν = ‘fail to know’, with οὐδέ ‘did not fail to know’. |
| 536–538 · l, i, n | moderate | οὐδέ μιν … ἠγνοίησεν ἰδοῦσα is the Odyssey formula at 5.77 (odyssey-022: “failed to recognize, seeing him” / “did not fail to know him the moment she saw him”). The draft used “was not ignorant” / “was not unaware” without saying why it departed. | `l` now “did not fail to recognize that …”, `i` “did not fail to know that …”; note names the Odyssey parallel. The new-renderings row for ἠγνοίησεν must be rewritten (see below). |
| 566 · l, n | moderate | ἀάπτους: `l` “irresistible”, but the house `l` is “untouchable” (odyssey 11.502, and three published units), `i` “irresistible” (+ note: meaning not known). | `l` “untouchable”; note now says both are ancient guesses. |
| 517 · i | moderate | ὀχθήσας: the Odyssey fixes `l` “vexed”, `i` “troubled” (15.325 is the same formula, τὸν δὲ μέγ’ ὀχθήσας προσέφης). Draft `i` had “vexed”. | `i` “Greatly troubled”. |
| 570 · i | moderate | Same verb ὄχθησαν, same rule. | `i` “were troubled”. |
| 586 · i | moderate | κηδομένη περ rendered “troubled”, which the Odyssey table keeps for ὀχθέω in `i` (and the draft’s own avoided-list called “troubled” reserved). | `i` “worried as you are”. |
| 578–579 · l | moderate | `l` “and along with us confound the feast” read σύν as a preposition with ἡμῖν; the note (rightly) says σύν is in tmesis with ταράξῃ and ἡμῖν is ‘for us’. | `l` “and for us confound the feast”. |
| 581 · n | moderate | `i` “the best of us” supplies ‘of us’ without saying so, while the note called the sense “plainly ‘the most powerful’” though `i` says ‘best’. (Odyssey 8.129 has πάντων; here no group is named.) | Note now: ‘best’ means best in strength; the Greek names no group; ‘of us’ is supplied from context. |
| 596 · l, n | moderate | `l` “with her hand” and the note’s “with her hand” asserted whose hand χειρί is, while `i` says “her son’s hand”: `l` and `i` disagreed in force. The Greek (genitive παιδός, dative χειρί) does not say. | `l` “by hand”; note says whose hand is not stated and `i` reads ‘from her son’s hand’, the usual sense. |
| 520 · l | minor | αὔτως: the Odyssey table’s `l` is “just so” (14.151, 16.143); draft had “even as it is”. | `l` “even just so”. |
| 521 · n | minor | “the accusative μέ as its subject, the construction of 408”: 1.408 is ἀρήγω + dative, not accusative + infinitive; the cross-reference was false. | Reworded: μέ is the subject; ἀρήγειν takes the dative Τρώεσσιν, as at 408. |
| 529 · n | minor | “ἄνακτος … a genitive tied to the head”, but `l`/`i` read ‘the locks of the lord’. Note contradicted its own `l`. | “a genitive with χαῖται, ‘the lord’s locks’”. |
| 557 · l, n | minor | ἠερίη: iliad-005 (1.497) and the table have `l` “morning-early”; draft `l` “early in the morning”. Note said Thetis “rose at dawn” at 497; she went up to Olympus. | `l` “morning-early”; note corrected. |
| 565 · n | minor | “ἀκέων ‘in silence’ (34)”: the word stands in this part at 511; 34 is another part. | Changed to (511). |
| 571 · l | minor | ἐπίηρα φέρων: note said ‘bringing pleasing things’, `l` “bringing what pleases”; at 578 the reverse. Note and `l` disagreed in both units. | `l` of 571 “bringing pleasing things”; note of 577 “to bring pleasing things”. Both now agree with `l`. |
| 577 · n | minor | (see the row above) | done as above. |
| 584 · l | minor | ἀναΐξας: Odyssey table `l` “having sprung up” (13.197); draft “springing up”. | `l` “having sprung up”. |
| 587–589 · i | minor | ἀχνύμενός περ rendered “grieving as I may” (a potential); the note and the Greek say ‘though I am’. | “grieving as I am”. |
| 563 · i | minor | καί (‘even’) dropped in `i` while `l` has “even worse”. | `i` “worse still for you”. |
| 561 · i | minor | “I can never escape your notice” adds a modal; οὐδέ σε λήθω is plain present. | “I never escape your notice”. |
| 542 · l | minor | πρόφρων: Odyssey table `l` is “ready-minded” (`i` “with a ready mind”); draft `l` used the `i` form. | `l` “ready-minded”. |
| 539 · l | minor | κερτομίοισι: Odyssey table `l` “with taunting ones”, `i` “with taunts”; draft `l` “with taunts”. | `l` “with taunting ones”. |

Counts of changes, pass 1: 1 major, 9 moderate, 13 minor (23 findings, 28 fields; `t` untouched).

## Pass 1 — the drafter’s flagged claims, verified

- **536–538, μιν with ἰδοῦσ’**: true (μιν is the object of ἰδοῦσα, ἠγνοίησεν has the ὅτι clause), but the note’s literal gloss contradicted it; fixed (above), plus the Odyssey-formula departure.
- **566, ἰόνθ’**: kept. ἰόντα elided and aspirated before ὅτε (rough breathing) is the accusative singular of the participle of εἶμι, agreeing with an unexpressed ‘me’ (the subject of the infinitive-less clause), which is the standard reading and is what `l`/`i`/note say. A dative ἰόντι is conceivable but not the usual one; no change.
- **580–581, unfinished sentence**: kept. εἴ περ γάρ κ’ ἐθέλῃσιν … στυφελίξαι has no apodosis; ὃ γὰρ πολὺ φέρτατός ἐστιν gives the reason. The note’s “left unfinished” is accurate; the dash in `l`/`i` is right. The ‘of us’ supply was the only fault (fixed).
- **590, ‘you’ supplied**: kept. ἀλεξέμεναι has no object; Hera is the natural one in Hephaestus’ mouth, the `l` leaves it out, and the note says the English supplies it. Disclosed, so no change.
- **553, καὶ λίην**: kept. ‘Truly’ for καὶ λίην with πάρος γε ‘before now at least’ is a sound reading of an affirming intensifier; the note says “an intensifier” and does not claim more. The rival reading (λίην with the verb, ‘far too much’) is a stretch with οὔτε … οὔτε and would be a different sentence.
- **596, χειρί**: changed (above).

## Pass 1 — other findings considered and refused

- 511 note “Thetis has ended her plea (1.505–510)”: her speech begins at 503, but the request proper begins at 505; true as worded.
- 522 μή τι νοήσῃ: purpose ‘lest’, as the note says; no change.
- 542 `i` “pass judgement on them”: ‘on them’ is mild; δικάζω without object needs one in English.
- 545–546 `i` “do not hope to know all my words”: fine for μὴ δὴ … ἐπιέλπεο … εἰδήσειν.
- 548 `i` “before you”: the note says the English supplies it (πρότερος ‘earlier’), and the sense is plain.
- 563 note “the same phrase stands at 325”: 1.325 has καὶ ῥίγιον ἔσται; true.
- 564 `i` “it must be what pleases me”: μέλλει + infinitive for what is bound to be; fine, and listed in the table.
- 565 `i` “So sit in silence”: ἀλλά after a concessive clause; ‘So’ is acceptable.
- 575 `i` and the Odyssey line (18.403): wording identical to the published unit; correct.
- 592 `l` “setting sun” for the aorist participle: matches the published Odyssey `l`.
- 603–604: `i` “nor … or” for οὐ μὲν … τε, with the genitives hanging on ἐδεύετο: correct and disclosed in the note.
- 609 `i` drops “to the place” from the published 19.49 wording: allowed (“as far as your sentence allows”).
- 571–572 note “Hephaestus … son of Zeus and Hera”: 578 calls Zeus his father; no change.
- Cross-references checked and true: 32, 100, 171, 196, 228, 241, 302, 325, 408, 414, 468, 475, 497, 500, 505–510, 517, 518, 521, 534, 553, 555, 566, 572, 577, 580, 583, 589, 602; Odyssey 1.63 (reply line), 5.77, 7.92, 8.294, 8.326, 9.161, 9.474, 10.70, 17.365, 18.403, 19.49, 20.103, 24.92.
- Quote marks: speeches 514–515, 518–527, 540–543, 545–550, 552–559, 561–567, 573–583, 586–594 each open on a `mark` unit and close on the last unit (549–550 was the only break; fixed). Narration between speeches carries none.

## Pass 2 — gloss.json (281 entries: 270 new, 11 broadened)

Coverage: every key of novel-forms.json has an entry and nothing extra; all 11 `__broaden__` keys exist in the live glossary and each new entry contains the old one whole; no entry is 230 characters or more except two broadened ones (the cap in build_iliad.py applies to new entries only); no ASCII quotes; no line numbers; no backticks. Every known form (219) checked against its use in this part: the existing entries cover the uses, except the two broadening suggestions below.

I did not edit gloss.json (the glosser owns it). Each item gives the key and the replacement text.

| key | sev | problem | suggested entry |
|---|---|---|---|
| αὐτῇ | moderate | “καὶ αὐτῇ περ ‘to her too’” misreads the line: it is ‘even though she herself understands’ (αὐτῇ περ νοεούσῃ, 577). | `αὐτός — self; intensive pron., fem. dat. sg., agreeing with a dative: ’to her herself’ (αὐτῇ περ νοεούσῃ ’even though she herself understands’)` |
| μέ | minor | “accented for emphasis” is wrong: μέ takes its accent because the enclitic φησι follows (καί τέ μέ φησι). | `ἐγώ — I; acc. sg. μέ, accented because an enclitic follows: ’me’` |
| κατανεύσομαι | minor | “(Attic κατανεύσω)” is unsupported (Attic has the middle future too). | `κατανεύω — nod assent, grant; fut. 1 sg. mid.: ’I shall nod assent’` |
| ἐπερρώσαντο | minor | “waved, streamed down”; the hair streams forward (the unit’s note). | `ἐπιρρώομαι — stream on, rush upon; aor. 3 pl. mid., ἐπερρώσαντο: ’streamed forward’` |
| ἠγνοίησεν | minor | Homeric lemma is ἀγνοιέω (the unit’s note says so). | `ἀγνοιέω (Attic ἀγνοέω) — fail to recognize, not know; aor. 3 sg. act., negated by οὐδέ: ’did not fail to recognize’` |
| νεικείῃσι | minor | translation “lest he quarrel” where the verb is ‘rebuke’ in this book. | `… after ὄφρα μή: ’lest he rebuke’` |
| δαιμονίη | minor | “ill-starred” has no support; the Odyssey entries say ‘strange, puzzling’. | `δαιμόνιος — strange, puzzling, uncanny; fem. voc. sg., epic -η (= Attic -α), reproachful address: ’strange one’` |
| κηδομένη (broaden) | minor | Existing “care for, be concerned” does not state the sense used here (‘be distressed’); the Odyssey glossary has it for κηδόμενόν. | add to the old entry: ` · also be troubled, distressed (κηδομένη περ ’worried though you are’)` |
| ὡς (broaden) | minor | Existing “as, how, that … since” has no temporal sense, which 600 uses (ὡς ἴδον ‘when they saw’). | add: ` · also temporal, ’when’ (ὡς ἴδον ’when they saw’)` |

Other entries checked and left: αἰγλήεντος, βηλοῦ, δολομῆτα, διέτμαγεν, ἐμπεφυυῖα, ἐνῶρτο, ἆλτο, ἀνέσταν/ἔσταν, ἰόνθ’ (matches my verification above), ἰδυίῃσι, κολῳὸν, κακκείοντες, καθῆστο, κοιμᾶθ’, ποῖον (masc. acc., correct for 552), τάδ’ (nom./acc., correct for 573), τεταγὼν, ἀμφιγυήεις, ἀμφικύπελλον, χρυσόθρονος, the eleven broadenings (each use verified in the line).

Counts, pass 2 (gloss): 1 moderate, 8 minor, none applied.

## Totals

units.json: 1 major, 9 moderate, 13 minor (applied). gloss.json: 1 moderate, 8 minor (reported, not applied).

## Files to bring into line (not mine to edit)

new-renderings.md rows now out of date after the edits above:
- ὀχθέω: `i` “troubled” / “were troubled” (the Odyssey’s); drop “troubled” from the avoided list.
- τὴν δὲ μέγ’ ὀχθήσας προσέφη …: `i` “Greatly troubled, Zeus who gathers the clouds said to her:”.
- ἠγνοίησεν ἰδοῦσ’: `l` “did not fail to recognize”, `i` “did not fail to know”; follows odyssey-022 (5.77); “was not ignorant”, “was not unaware” become the avoided alternatives.
- ἐπίηρα φέρων: `l` “bringing pleasing things” (same as φέρειν).
- ἣ δὲ καὶ αὔτως: `l` “even just so”.
- κερτομίοισι: `l` “with taunting ones” (add a row or fold into the existing κερτομίοισι … προσηύδα row: the `l` is the Odyssey’s).
- ἠερίη: `l` “morning-early” (as 1.497).
- κηδομένη περ: `i` “worried as you are”.
- φέρτατος: note that ‘of us’ is supplied.
- ἀναΐξας: the row says the Odyssey has “leapt up”; its table gives `l` “having sprung up”, `i` “sprang up”; `l` now follows that.
- πρόφρων: `l` “ready-minded” (Odyssey table).
- λοίγια ἔργα, ἀάπτους rows are unaffected; ἀάπτους is not new (Odyssey 11.502), so no row is needed.
