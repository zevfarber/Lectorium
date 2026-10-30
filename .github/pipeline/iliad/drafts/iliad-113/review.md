# iliad-113 (17.481–581) — review

Two passes made on units.json (49 units). `t` untouched (checked against the original by script). No backticks in notes; longest note 91 words. `gloss.json` did not exist at review time, so the glossary parses were not checked in the second pass.

Checked and found sound: every unit's `t` begins at the packet line it claims; `l` and `t` have the same line count; `p` is set exactly on the eight paragraph openings (481, 491, 507, 516, 540, 543, 560, 567); quotation marks balance (six speeches: 485–490, 501–506, 508–515, 538–539, 556–559, 561–566, with “ and `mark` on the first unit of each and ” on the last). The last unit of iliad-112 (17.479–480, Automedon's speech) ends with ”, so nothing runs on into this part; the last unit here (17.580–581) is narrative, so nothing runs on into the next. Whole-unit repeats of published Greek (527–529a, 559, and 529b) were checked by script against the validator's rule.

## Changes

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 529 | l, i | high | Same Greek as iliad-081 (ln 444) and iliad-105 (ln 613); both published units close with ";" in `l` and `i`, this one with ".". The validator would fail ("same Greek … different English"). | Closing "." changed to ";" in both layers. |
| 481 | n | medium | λάζετο called "unaugmented aorist"; it is the imperfect (the table, the glossary and every earlier note say so). | "unaugmented imperfect". |
| 488 | l, i, n | medium | ἐναντίβιον rendered "face to face"; the house table (8.255 and later rows, iliad-048, -062, -092) has "head-on", and keeps "face to face" for other words. | "head-on" in both layers; the note names the word. |
| 498 | l, i, n | medium | σθένος rendered "power"; the table's σθένος is "strength" (ἀλκή "might"). | "might and strength" in both layers and in the note. |
| 543 | i | medium | ἔγειρε νεῖκος rendered "stirred up the quarrel"; the table avoids "stir up" for ἐγείρω ("rouse") and the new row for 17.552 already has "roused". | "roused the quarrel". |
| 543 | i | medium | πολύδακρυς rendered "full of tears"; the note refers to 17.192 πολυδακρύου, which is "of many tears". | "grievous and of many tears". |
| 563 | l, n | medium | ἀμύνειν Πατρόκλῳ rendered "ward off / for Patroclus" in `l`; the table (13.464, 13.481) has "defend" for ἀμύνω with a person and no thing warded off. `i` already said "defend". The note said "ward off harm for". | `l` "stand by and defend / Patroclus"; note says "defend", with the reason. |
| 491 | n | low | Packet-flagged line; scanned by hand (see below). The irregularity is real and the note was silent. | One sentence added, worded as in iliad-015 (ln 819) and iliad-029 (ln 247). |
| 492 | n | low | τώ written for τὼ (the printed form is the dual article with grave). | τὼ. |
| 494 | n | low | "the one who dies at 17.517": 517 is where Aretus is hit; he falls at 523. | "the one Automedon hits at 17.517". |
| 520 | n | low | "A comparison runs to 524": the simile proper is 520–522; 523 opens the ὣς clause, which the next unit's note already says completes it. | Reworded to say so. |
| 530 | n | low | μεμαῶτε left without saying with whom it agrees. Dual nominative and accusative are alike, so it can go with Αἴαντε or with σφω’; `i` takes it with the Ajaxes. | The note says both are possible and which the English takes. |
| 538 | n | low | The new-renderings row says "the contrast is with Patroclus, as the note says"; the note did not. | "(than Patroclus)" added after χερείονα. |
| 569 | i | low | μάλα περ ἐργομένη rendered "however often it is driven off"; the Greek says how hard, not how often. | "however hard it is driven off". |
| 576 | n | low | "unaugmented imperfect of τίω … so ‘used to honour’", against `l` and `i` "honoured". | "so ‘honoured’". |

## new-renderings.md

- νεῖκος row: `i` changed to "roused the quarrel", with the reason (see 543).
- ἔθνος Ἀχαιῶν row: added that ἔθνος ἑταίρων at 17.581 keeps "company of his companions" (the table's 11.585 row; iliad-069, -097, -109), so the two uses do not look like a conflict.
- Added rows for παλαιγενές (17.561) and κατηφείη καὶ ὄνειδος (17.556), which had none.
- "Reused unchanged" list extended with ἐναντίβιον, ἀλκῆς καὶ σθένεος, ἀμύνειν "defend", πολύδακρυς, ἀφίει μένος and λάζετο μάστιγα καὶ ἡνία.
- No other conflict with the house table: βοηθόον, κακοῖσι, ἐπιτράπεθ’, πρίν γ’ … βήμεναι, ὕπερθεν, ἶρις, χειμῶνος δυσθαλπέος, ἔγειρε, ἰσχανάᾳ (departure stated), εἰλαπιναστής, κῆρ ἄχεος μεθέηκα, ἐρωή, ἐσεμάσσατο, αἰζήϊος all agree with the rows they cite.

## Line 17.491 by hand

ὣς ἔφατ’, οὐδ’ ἀπίθησεν ἐῢς πάϊς Ἀγχίσαο has 16 syllables. The scanner's fit (checked by hand) is: ὣς ἔφα | τουδ’ ἀπί | θησε νε | ῢς πά ϊς, four dactyls with the usual elision and ἐῢς as two syllables; this leaves Ἀγ-χί for the fifth foot (a spondee) and σα-ο for the sixth, which scans only if the σα- of Ἀγχίσαο counts long. Ἀγχίσης has short ι and α, so the fifth-foot spondee and the lengthened σα- are both real. The same line-end is so annotated in iliad-015 (ln 819), iliad-029 (247), iliad-031 (468), iliad-073 (98) and iliad-081 (428). Sentence added to the note.

## Findings considered and refused

- 485–486 `i` "I have noticed" for the aorist ἐνόησα: `l` keeps "I noticed"; the perfect is the natural English of result. Left.
- 495–498 `i` omits "again" for αὖτις: "come back" carries it. Left.
- 498 ἐῢς / 491 "epic form of ἐΰς": same wording as the published note at 15.819. Left.
- 529 "unaugmented" imperfect: the glossary says ἀφίει is unaugmented (= ἠφίει); the published note says only "imperfect". Kept.
- 545 note's last clause (a change of purpose in the Danaans' favour): the note already says what Zeus' mind turned to is not stated, so it offers the sense without claiming it. Left.
- 561 `i` "aged one, of great age": the two words are distinct in Greek (γεραιέ, παλαιγενές) and `l` keeps them apart. Left.
- 524/540 νηδυίοισι and κατὰ … ἐδηδώς: labels checked and true.
- 17.552 and 17.581 both ἔθνος: the renderings differ ("band of the Achaeans", "company of his companions") but each follows the table row for its own phrase. Kept.
- Remembered English: no phrase in `i` arrived whole from memory; the ones that looked familiar ("far-thundering Zeus", "gleaming-eyed Athena", "good at the war-cry", "fair-maned") are table renderings.
