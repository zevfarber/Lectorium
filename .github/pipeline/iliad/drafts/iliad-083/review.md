# Review — iliad-083 (13.560–659), pass 1

Reviewer pass 1 of 2. `t` untouched (checked: units' `t` joined equals the packet lines, 100 lines; each `l` has the same line division as its `t`; no `\n` in any `i`). Edits made to `units.json` by script. `gloss.json` not read or touched (glosser runs in parallel; pass 2 reads it).

Checks run: every grammatical label in every note against the form in the line; every cross-reference (3.15, 3.32, 3.361, 4.461/503/526, 5.67, 5.134, 5.499, 5.659, 9.440, 2.851, Od. 23.145, 559, 565, 567, 570, 586, 596, 648, 616–620) against the source or published parts; Greek → `l` word by word; `l` ↔ `i`; the repeated lines (13.566/596/648 = 3.32; 13.604 = 3.15; 13.605 = 11.232; 13.610 = 3.361; 13.580 = 5.659; 13.575 = the 4.461 formula; 13.637 = Od. 23.145) against the published English (all identical); every house-table row for the stock words (grepped in both tables); quotation marks (“ on unit 620, ” on unit 639, `mark` once, on 620; no stray marks; speech neither runs in from nor out into the neighbouring part, since 559 and 660 are narrative); paragraph marks `p` on 560, 576, 581, 601, 640, 643 against the ¶ in the packet; note length (all now ≤110 words by whitespace count). No line is flagged by the scanner, so no hand-scan was owed.

Counts: 33 edits — high 9, medium 5, low 19 (a finding that touches `l`, `i` and `n` is counted once per field).

## Changes

Unit = the unit's `ln`; for the two units that start at 570 the second is the simile.

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 560 | n | medium | Note called λῆθ’ an unaugmented aorist and said it is ἔληθε; λῆθε is the unaugmented imperfect of λήθω (the aorist would be λάθε). Note was also 121 words (limit 110). | Label corrected; note trimmed to under 110 words (dropped the redundant καθ’ ὅμιλον gloss and the "last figure of the previous part" aside). |
| 564 | n | medium | Note said the part 'with the point' sticks in the shield, then said the Greek does not say which part is which: the note contradicted itself. | Removed 'with the point'. |
| 567 | n | low | Note was 111 words (limit 110). | Cut the parenthetical about 570. |
| 570 | n | low | Note said δόρυ stands 'in the line before'; δουρί is at 567, two lines earlier (569 is the line before). | Changed to 'at 567'. |
| 570 (simile) | l | high | ἀσπαίρω is fixed in the house table as 'gasping' (3.293–294, 10.521; the Iliad row keeps it). The draft chose 'writhed' and recorded the departure in new-renderings.md; the table is binding and the reason given (an ox on ropes) does not license a departure. | l: 'writhed' -> 'gasped'. |
| 570 (simile) | i | high | Same: i 'writhed' departs from the table's 'gasping'. | i: 'writhed about it' -> 'gasped about it'. |
| 570 (simile) | n | high | Note defended 'writhed'. | Note now matches the house 'gasped'. |
| 570 (simile) | n | low | Note was 146 words (limit 110). | Rewritten and trimmed. |
| 573 | l | high | Second occurrence of ἤσπαιρε: 'writhed' departs from the table's 'gasping'. | l: 'writhed' -> 'gasped'. |
| 573 | i | high | Same, i layer. | i: 'writhed' -> 'gasped'. |
| 576 | l | high | κόρση is fixed in the house table (4.502) as 'the side of the head'; 'temple' is the table's rendering of κρόταφος and is listed there as avoided for κόρση. | l: 'on the temple' -> 'on the side of the head'. |
| 576 | i | high | Same, i layer. | i changed likewise. |
| 576 | n | high | Note gloss 'temple' for κόρση. | Gloss corrected. |
| 580 | n | low | Cross-reference to the κόρση rendering in 576. | Brought into line. |
| 584 | n | low | Note quotes τώ with an accent the line does not have (the line prints τὼ). | Accent corrected. |
| 588 | n | low | Note was 147 words (limit 110). | Trimmed (dropped the list of glosses for κύαμοι, ἐρέβινθοι, μελανόχροες, which `l` and `i` already show, and the 5.499 cross-reference). |
| 602 | n | low | Note was 113 words (limit 110). | Trimmed (dropped the gloss of ἄγε). |
| 604 | n | low | Note said Μενέλαος is named 'in the next line but one'; Μενελάου stands in 606, the very next line after 605. | Corrected. |
| 608 | n | low | Note was 128 words (limit 110). | Trimmed. |
| 611 | n | low | Note quotes the accusative πέλεκκον; the line has the dative πελέκκῳ. | Form corrected to the one in the line. |
| 613 | n | medium | Wrong tense label: ἐφίκοντο is a (second) aorist, like ἵκοντο; there is no imperfect of this shape. | Label corrected. |
| 614 | n | low | Note was 154 words (limit 110). | Trimmed to the limit (dropped the ἤτοι gloss and the sentence repeating that μέτωπον is the part struck). |
| 616 | i | medium | ἰδνώθη is fixed in the Odyssey table (2.266) as 'doubled over' in both layers; i had 'doubled up'. | i: 'doubled up' -> 'doubled over'. |
| 616 | n | low | Gloss brought in line with the rendering. | Corrected. |
| 620 | l | high | ξείνιος Ζεύς is fixed in the Odyssey table (9.271) as 'the guest-god' in `l` and 'the god of guests' in `i`. The draft put the `i` form in `l`, and new-renderings.md wrongly says the table's `l` is 'the god of guests'. | l: 'the god of guests' -> 'the guest-god'. |
| 620 | n | low | Note was 221 words (limit 110). | Rewritten to the limit, keeping the construction points (genitives, cognate object, agreement of ξεινίου); dropped glosses already visible in `l`/`i`. |
| 626 | n | low | `l`/`i` render the present φιλέεσθε as 'were being', with nothing in the note saying so. | Note now says the English puts it in the past. |
| 636 | n | low | Note was 137 words (limit 110). | Trimmed. |
| 640 | n | low | Runbook/Odyssey conventions: a word whose meaning is not known is said to be unknown; ἀμύμων is the named example, and the sibling notes (1.92, 4.9...) say so. | Added the clause. |
| 656 | n | low | Note refers the reader to 'the table', which the reader cannot see. | Reworded. |
| 658 | l | low | House table (5.84): δάκρυα λείβων is 'tears pouring' in `l` (the `i` 'pouring out his tears' was already right). | l changed to the table form. |
| 653 | n | medium | Wrong tense label: ἑζόμενος is a present participle, not an aorist. | Label corrected. |
| 576 | n | low | Note (after the κόρση fix) reached 111 words. | Dropped "a man the poem does not describe". |

## Follow-up for the caller (files I did not edit)

`new-renderings.md` is the drafter's file and still records three things that are wrong after this pass, and the runbook copies its rows into the `conventions.md` table at publish time. Before that copy: (1) delete the row ἀσπαίρω "writhed" (the table already has "gasping"; the closing paragraph's claim that "writhed" is new also goes); (2) change the ξείνιος row to `l` "the guest-god", `i` "the god of guests", and drop the mistaken claim that the table's `l` is "the god of guests"; (3) add κόρση "the side of the head" / "the side of the head" as following the table (4.502). The ἰδνώθη and δάκρυα λείβων fixes follow existing table rows and need no new row. The ἐριβρεμέτης row stands (see below).

## Findings considered and refused

- **ἐριβρεμέτης "loud-rumbling" (new choice).** Checked both tables: no row for ἐριβρεμέτης or any βρεμ- compound except ὑψιβρεμέτης ("high-thundering"), which lists "loud-thundering" as avoided; the new choice does not collide with it, nor with ἐρίγδουπος "loud-crashing" (ἐρι- = "loud", as there) or εὐρύοπα "far-thundering". Accepted; the unit's note says the epithet is rare. Left in new-renderings.md.
- **κόρος ἐστί: `l` "there is satiety" / `i` "there comes a fullness" (unit 636).** No table row; `i` reads slightly off κόρος ("satiety") but the draft records it and the clause is consistent with ἀκόρητος "cannot have enough". Accepted.
- **ἀνέσαντες `l` "having lifted" vs note "having put up" (unit 656).** The lemma is uncertain and the note says so; both are in the same range. Accepted.
- **ἐϋστρεφεῖ οἰὸς ἀώτῳ σφενδόνῃ (unit 598): does ἐϋστρεφεῖ agree with ἀώτῳ or σφενδόνῃ?** Both are dative singular and ἐϋστρεφής has one ending for masculine and feminine; the draft's reading (twisted wool, the sling the thing it is made into) is a possible one and note and `i` agree with each other. Accepted.
- **Unit 626 `l`/`i` render present φιλέεσθε as "were being".** Considered changing the tense; kept (the sentence is in the past through οἴχεσθ’ ἀνάγοντες, and the note now says so). Low.
- **Unit 583 `i` drops πῆχυν.** Matches the table row πῆχυς τόξου (11.375): `l` "the arm of the bow", `i` "the bow", and the note says so. Accepted.
- **Unit 614 `i` "bridge of the nose" for ῥινὸς πυμάτης.** Declared in new-renderings.md and flagged in the note as the part nearest the forehead; not a table word. Accepted.
- **Unit 605 οἱ = Peisander ("from him").** As in the published 11.232 (οἱ is the man the spear misses); consistent with the published `l`/`i`. Accepted.
- **Unit 576/578 τρυφάλεια `l` "helm" / `i` "helmet".** Checked against the table: correct.
- **Menelaus speech, unit 620–639:** `mark` "Menelaus speaks" once; “ in both layers on 620, ” in both on 639. Correct, nothing to change.
- **Unit 656 "τόν is Harpalion"; Παφλαγόνες as his father’s people (2.851).** Checked: Pylaemenes leads the Paphlagonians at 2.851. Correct.
- **Scansion:** packet lists no flags; nothing added to any note.
- **Glosses (gloss.json):** not read in this pass.

Pass 2 should re-read the edited notes (units 560, 570 simile, 576, 588, 602, 608, 614, 620, 636) and check gloss.json parses against the line.
