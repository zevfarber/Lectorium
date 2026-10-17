# iliad-005 (Iliad 1.413–510) — review

Reviewer: two passes over `units.json` (51 units), against `packet.md`, `new-renderings.md`, `conventions.md` (+ Odyssey), the model `drafts/iliad-004/units.json` and the published `iliad-004.json` / `odyssey-*.json`. `t` was not touched (checked by script before every write: the list of `t` strings is identical before and after). `gloss.json` was read in pass 2 and not edited. No modern translation was consulted or recalled. No scansion flags in the packet, so no hand scansion was due.

Severity: major = the text says something the Greek does not; moderate = a note or English layer is wrong or misleading in a way a reader would notice; minor = imprecision, consistency, tidiness. No major findings.

## Changes made (16: 6 moderate, 10 minor)

| Line (unit) | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 425 | `l` | moderate | `l` rendered `καὶ τότ’ ἔπειτά τοι εἶμι` as “and then indeed …”; ἔπειτα is “thereafter”, not “indeed” (δή is “indeed”, and 494 `καὶ τότε δὴ` correctly has it). The Odyssey renders the same words “then thereupon / thereafter” (odyssey-026, -043, -061, -113). | “and then indeed for you I will go” → “and then thereupon for you I will go”. |
| 439 | `n` | moderate | Positional claim false: “its noun νηός ‘ship’ follows after the verb”. In `ἐκ δὲ Χρυσηῒς νηὸς βῆ ποντοπόροιο` νηός stands before βῆ; only the epithet follows the verb. | Rewritten: νηός comes after Χρυσηΐς and before the verb, the epithet is held back until after it. |
| 456 | `n` | moderate | Cross-reference wrong: ἀεικέα λοιγόν at 341 and 398 was said to be “used by Achilles and Thetis of keeping ruin from the Achaeans”. At 341 Achilles speaks of warding ruin from “the others”; at 398 he says Thetis once warded it off from Zeus (iliad-004, units at 338 and 396). | Rewritten to say exactly that. |
| 480 (481–482) | `n` | moderate | Claim that 481–482 are Odyssey 2.427–428 “apart from the augment on ἔπρησεν there” is inexact: Od. 2.427 has `ἔπρησεν δ’ ἄνεμος`, the Iliad `ἐν δ’ ἄνεμος πρῆσεν` (different word order, verb split by tmesis). 2.427–428 confirmed as the book/line (odyssey-008 = 2.321–434, unit at 427). | Note now states the real difference. |
| 505 | `i` | moderate | “Honour my son for me, who has come to be …”: the relative clause hangs on “me”, not on “son”. | “Honour for me my son, who has come to be the swiftest of all to his doom;”. |
| 490 | `i` | moderate | “the assembly where men win glory” is a ready-made English phrase for κυδιάνειρα (the rule is to rebuild such phrases from the grammar: κῦδος + ἀνήρ). | “the assembly that brings men glory”. **Follow-up for the caller: the row for κυδιάνειρα in `new-renderings.md` quotes the old `i` and must be updated before it is copied into the table.** (I did not edit that file.) |
| 446 | `i` | minor | “he placed her in his hands, and he took his dear child”: both “he”s read as Odysseus. | “in her father’s hands” (πατρὶ φίλῳ, 441). `l` left literal. |
| 477 | `l` | minor | `καὶ τότ’ ἔπειτ’` rendered bare “then”, against the Odyssey’s “then thereupon”. | “then thereupon they put out to sea …”. |
| 421 | `n` | minor | “σὺ μὲν νῦν … is answered by the δέ of 425, where she turns to what she will do”: at 425 she turns to when Zeus returns; what she will do is 426. | Reworded: the δέ of 425 sets what will happen on the twelfth day against what he must do now. |
| 430 | `n` | minor | “the ship that left at 311”: the ship sails at 312 (311 is Odysseus embarking). | “sailed at 312”. |
| 430 | `n` | minor | “the offering Calchas said Apollo wanted”: Calchas (99) says only that the hecatomb is to be taken to Chryse with the girl. | “the offering Calchas said must be taken to Chryse along with her (99)”. |
| 463 | `n` | minor | “on them the entrails were held in the fire to roast”: the Greek says nothing about the use of the forks. | Replaced by “the line does not say what they were used for.” |
| 464 | `n` | minor | Note on `κατὰ μῆρε κάη` left out that κατά is a preverb apart from κάη. | Added “with its preverb apart in κατὰ … κάη (tmesis)”. |
| 503 | `n` | minor | “the same words as Chryses at 455 and in his first prayer at 41”: 455 has ἐπικρήηνον, not κρήηνον. | “… at 41 (at 455 with a preverb added)”. |
| 506 | `n` | minor | “Her complaint repeats Achilles’ own words at 355–356”: only the second line (356) is word for word; the first differs (ἀτάρ μιν … ἄναξ ἀνδρῶν). | Reworded to the second line. English of 356 checked against iliad-004: identical apart from “my”→“his”. |
| about | `about` | minor | “leaves him grieving for the girl”: χωόμενον is “incensed”. | “angry”. |

**Counts: 0 major, 6 moderate, 10 minor — 16 changes.**

## Verified and left alone (the drafter's uncertain items)

- **ἴψαο (454).** Aorist 2nd sg. middle of the rare ἴπτω/ἴπτομαι; “greatly struck / struck … hard” is the traditional sense and the note says the verb is rare and that the Greek does not name the plague. Kept.
- **τῖσον (508) and τίσωσιν (510).** Taken as aorist of τίω “honour”: the person stands in the accusative (μιν, υἱὸν ἐμόν), as τίω takes it and τίνω “pay” would not (τίνω takes the penalty); τίμησον (505), ἠτίμησεν (507) and τιμῇ (510) all frame the request as honour. The note’s remark that the form could be read from τίνω is accurate and harmless. Kept.
- **μῆρε κάη (464).** Archive prints μῆρε; the Odyssey line has μῆρ’ ἐκάη. The note says only that it “looks like a dual” and that the sense is the same; English is the Odyssey’s (odyssey-013, 3.461). Kept. (Tmesis added to the note, above.)
- **αὐέρυσαν (459).** The Greek has no object; “drew the victims’ heads back” supplies the usual understood object and the note says so. A bare “drew back” would leave the English verb without sense. Kept.
- **Odyssey book numbers in notes.** “Odyssey 2.427–428” (unit 480) and “Odyssey 3.459” (unit 462) checked against the Odyssey manifest cites (odyssey-008 = 2.321–434, odyssey-013 = 3.404–497) and the units’ `ln` (427, 459). Both right. The Odyssey also has 1.463 (3.460, `νέοι δὲ παρ’ αὐτὸν …`) in the unit at 460, which the packet does not list; the Iliad unit’s `l`/`i` match it exactly.
- **506–507 merge (unit 506) and 417–418 (unit 417).** Each unit contains an internal ano teleia (`ἠτίμησεν·`, `ἔπλεο·`), against the Odyssey rule that a tap-unit ends at `·`. Left, for two reasons: splitting changes `t` (not mine to touch), and the corpus has the same thing 39 times in 6,006 published units; in both places the second clause is the reason for the first (γάρ; τώ), so a merge reads naturally and passes the gates. **For the caller:** iliad-004 splits the same Greek at 355/356 (`ἠτίμησεν·` | `ἑλὼν γὰρ ἔχει γέρας …`); if consistency with that is wanted, the drafter would have to split both units.
- Other refusals:
  - 420 `i` “in case he can be persuaded” (αἴ κε πίθηται): same rendering as iliad-004 407 (αἴ κέν πως ἐθέλῃσιν “in case he will be willing”). Kept.
  - 501 `i` drops ἑλοῦσα (“with her right hand under his chin” for “taking him under the chin”): no loss of sense, and the row in `new-renderings.md` states it. Kept.
  - 458, 465, 469 `i` begin “When” where the Odyssey’s `i` begins “But when”: not a whole-unit repeat, so no validator rule; the `l` keeps “But”. Kept.
  - 493 `i` “after that day” beside `l` “from that time” and note “from that (day)”: not contradictory (the point counted from is not named). Kept.
  - 499 “topmost peak of many-ridged Olympus”: the literal parts of ἀκροτάτῃ κορυφῇ and πολυ- + δειράς; no distinctive wording of any version. Kept.
  - 497 ἠερίη “early in the morning”: matches the Odyssey’s ἠέριος row (9.52), note carries the doubt. Kept.
  - 413 `l` word order and 428 “So then having spoken”: fine against the Greek.
- Mechanical: `l`/`t` have the same number of `\n` in every unit; no `\n` in any `i`; only typographic ’ and “ ”; speeches open at 414, 442, 451, 503 (each with `mark`) and close at 427, 445, 456, 510, with “ and ” in both layers; `p` on 413, 428, 446, 457, 475, 488, 493 matches the packet’s ¶; Achilles’ speech closes with ” at 412 in iliad-004. Repeated units: 436 and the 437 line equal the Odyssey’s English; 451–452 `l`/`i` equal iliad-001; 462 equals odyssey-013 (459); 463 equals odyssey-013 (460).

## Pass 2 (after the edits, and with `gloss.json`)

Re-read all 51 units against the edited text; no new problems in `l`↔`i` or notes beyond the 490 `i` above. `gloss.json` (279 keys, every `novel-forms.json` key present, 5 `__broaden__` entries) checked form by form against the lines; the parses are right (including ἐρέουσα, ἱλασόμεσθα, ἕποντο, ἴκμενον, τώ “therefore”, ἐκ τοῖο “from that time”, τίθει both readings, μῆρε “spelled as if a dual”). Two points for the glosser, not changed by me:

1. **ἴψαο** is glossed “you struck down”, which suggests killing; the unit says “struck … hard”. Suggest “you struck hard”. Its lemma is given as ἴπτομαι while the unit’s note says ἴπτω; one of the two should be brought into line.
2. No other discrepancy found.
