# iliad-007 (2.1–83) — reviewer's report

Reviewer pass 1 and pass 2 on `units.json` only (a separate check of `gloss.json` follows). `t` was never touched: the script that applied
the edits asserts every `t` is byte-identical to the original. Unit numbers below are 0-based positions in `sentences`, followed by the
starting line (`ln`). No modern translation was opened or recalled; Odyssey comparisons were made against the shipped `odyssey-NNN.json`
units and the Odyssey house table.

Counts: **0 major, 8 moderate, 12 minor** (20 changes, 23 field edits). 14 findings refused (listed below).

## What was checked and found sound

- Every unit's `t` joins to the packet's 83 lines with none dropped; `l` has the same line count as `t`; `i` has no `\n`.
- `p` stands on exactly the six units that open Monro & Allen's paragraphs (1, 16, 35, 48, 53, 76). `mark` stands on the first unit of each of the five
  speeches (Zeus 8, the Dream 23, Agamemnon 56, the Dream in Agamemnon's report 59, Nestor 79).
- Quotation marks: 4 “ (units 2, 13, 34, 52) and 3 ” (units 7, 21, 49); the part ends inside Nestor's speech (unit 54 has no ”), as expected. The nested
  ‘ opens in unit 37 (line 59) and ’ closes in unit 45 (line 70), in both `l` and `i`; Agamemnon's own speech resumes in unit 46. The
  last unit of iliad-006 (end of Book 1) is narrative, so no speech runs in from the previous part. No straight quotes in `l`, `i` or `n`.
- Merged unit 2.5–7 (unit 1): the merge is necessary, because line 7 alone is a whole-unit repeat of the published 1.201 and would be forced to "to her";
  `l` "to it" / `i` "to the Dream" is the departure recorded in `new-renderings.md`, and the note says so. Accepted.
- Merged unit 2.59–60 (unit 37): line 60 = line 23, whose unit carries “; merging keeps the repeated English intact (checked: `l` and `i` of 60 are
  word-for-word those of 23, only the opening mark differs, ‘ for “). Accepted.
- Repeated lines, compared by script (marks stripped): units 6 = 19 = 43; 14 = 38; 15 = 39; 16 = 40; 17 = 41; 47 = 54; 5 = 18 differ only in ἕλοι/ἕλοις
  (he/you), 18 = 42; units 7, 20, 44 differ only by the added ἐκ Διός. All identical as they should be. Packet repeats: 2.44 (`l` identical to odyssey-005, `i`
  reused for the clause that stands in the unit); 2.78 (unit 51) identical to iliad-001 in `l` and `i`; 2.7 departs as recorded.
- Cross-references to other lines (1.2, 1.8, 1.25, 1.73, 1.201; 8, 10, 11–12, 14–15, 19, 20–21, 23–32, 26–27, 28–29, 33–34, 35, 57, 60–70, 63, 72, 83) all
  checked against the lines; the faulty ones are in the table below.
- Scansion flags: none in the packet, so no line was due a hand-scan.
- Odyssey half-line matches (found by an n-gram search, since the packet lists whole lines only) were compared; the ones that mattered are in the table.

## Changes made

| # | Unit (ln) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 0 (1) | n | moderate | "the favour to Achilles that Thetis asked for in the last part": false cross-reference. Thetis asks at 1.503–510, which is iliad-005; iliad-006 is Zeus's answer. | "that Thetis asked of Zeus, and he promised, in the last two parts." |
| 2 | 3 (9) | n | minor | "Ἀγαμέμνονος Ἀτρεΐδαο has the epic genitive in -αο": the label is not true of Ἀγαμέμνονος. | Now "Ἀτρεΐδαο has the epic genitive in -αο (= Attic -ου)." |
| 3 | 6 (13) | n | minor | "The line comes three times": it is a two-line passage (13–14, 30–31, 67–68). | "These two lines come three times in this part." |
| 4 | 7 (14) | n | moderate | "The first unit of the next paragraph shows the news is a lure": the next paragraph begins at 16 (the Dream goes), which shows nothing of the kind; the narrator's comment is at 37–40, a paragraph later. | "Lines 37–40 show that the news is a lure: the hope it raises will fail." |
| 5 | 11 (20) | n | minor | "the man Agamemnon trusts most": the Greek (τῖ’ … μάλιστα) and `i` say honoured, not trusted. | "honours most". |
| 6 | 15 (26) | n | minor | Grammar: "as does the same words". | "as do the same words". |
| 7 | 16 (26) | n | moderate | "the two verbs κήδεται and ἐλεαίρει share the object σεῦ": σεῦ is already the genitive of ἄνευθεν (the note says so a clause earlier), and ἐλεαίρω does not take a genitive; the note contradicted itself on the form. | "κήδεται and ἐλεαίρει have no object of their own written, and ‘you’ is understood for both from σεῦ." |
| 8 | 17 (28) | n | minor | "Nothing else changes": κέλευε (imperative, 11) becomes κέλευσε (aorist, 28), which the note itself says. | "Nothing else changes but the verb form, and the English repeats." |
| 9 | 20 (31) | n | minor | "the sentence runs on into the next unit": the unit ends at an ano teleia, so it is the speech that runs on. The unit also says twice that "from Zeus" is an addition. | Reworded: "This is the Dream’s own wording, not Zeus’s, and the speech runs on into the next unit." |
| 10 | 22 (35) | i | minor | "things that were never to be fulfilled": οὐ … ἔμελλον is "were not going to / not to be"; "never" adds force the Greek lacks (`l` has "were not going to be"). | "were not to be fulfilled". |
| 11 | 24 (39) | l | minor | "groanings": every shipped rendering of ἄλγεά τε στοναχάς τε is "pains and groans" (odyssey-066), and `i` here has "groans". | "pains and groans". |
| 12 | 28 (46) | i | moderate | "his father’s sceptre": πατρώϊον is "of the fathers / ancestral" (`l` "of his fathers", the note "handed down from his fathers", and the Odyssey table's πατρώιος ξεῖνος "fathers’ time"); singular "father" in `i` disagrees with `l` and the note. | "his fathers’ sceptre, which never fails". |
| 13 | 31 (52) | l, i, n | moderate | The Greek of 2.52 is the Odyssey's 2.8 (odyssey-005, line 8) apart from the accent οἳ/οἱ and the final mark, so the packet did not list it. The draft changed its shipped English ("They made-proclamation, and the others gathered very quickly." / "The heralds made the proclamation, and the people gathered very quickly.") to "These … those assembled" / "the men assembled", with no departure recorded and nothing in the Iliad that forbids the Odyssey's wording. | Restored the shipped `l` and `i`; note adjusted ("were roused, gathered"; "the heralds and the people"). |
| 14 | 34 (56) | i | minor | "Listen, friends:" — the same two words (κλῦτε, φίλοι) are shipped in odyssey-070 as `l` "Hear, friends:" / `i` "Hear me, friends;". The reason in `new-renderings.md` ("Hear me" reserved for κλῦθί μευ) is not borne out by that shipped unit. | "Hear me, friends:". |
| 15 | 36 (57) | l | moderate | "it nearly resembled": ἄγχιστα is a superlative; the note says "most nearly", `i` says "most nearly", and the Odyssey's same words (odyssey-028) have `l` "most nearly liken". The `l` lost the superlative. | "it most nearly resembled;". |
| 16 | 37 (59) | i | minor | "spoke these words to me": `l` has "a word" (μῦθον singular) and the Odyssey's same half-line (odyssey-098) has `i` "spoke to him". | "It stood above my head and spoke to me:". |
| 17 | 37 (59) | n | minor | "ἔειπεν is the aorist of εἶπον in its epic reduplicated form": the standard description is the epic form of εἶπεν (the double ε is augment plus lost digamma); "reduplicated" is at best disputed. | "ἔειπεν is the epic form of εἶπεν ‘spoke’". |
| 18 | 48 (73) | l, i | moderate | "as is lawful": the Odyssey table fixes θέμις as "custom" ("right" and "law" avoided), and the same formula ἣ θέμις ἐστί is shipped as "as is right" (odyssey-009), "as is right"/"as is proper" (odyssey-010) and as "custom" (odyssey-067, 14.130). "Lawful" is none of these and sits next to the avoided "law"; the draft's own note called θέμις "what is customary". | "as is the custom" in both layers, following the table row (see open point 1). |
| 19 | 48 (73) | n | moderate | Two false labels: "πειρήσομαι takes the dative (ἔπεσιν)" — ἔπεσιν is the dative of means, and πειράομαι would take the genitive of the person tried, who is left unwritten; "ἣ = ᾗ": the printed form is the nominative relative, agreeing with θέμις (as in the Odyssey units' notes). | Rewritten: "πειρήσομαι is ‘I will make trial’ (of the army, understood), with ἔπεσιν ‘with words’ the dative of means. ἣ θέμις ἐστί is ‘as is the custom’: ἥ is the relative, feminine like θέμις, ‘which is the custom’; θέμις is what established usage allows." |
| 20 | 52 (79) | i | minor | "and the rather turn away from it": an archaism for its own sake (the convention bars that), and the phrase is the kind that arrives ready-made; `l` has "all the more". | "and all the more turn away from it;". |

## Findings considered and refused

1. Unit 0 `i` "All the other gods": ἄλλοι is the complement of Zeus alone, so "all the other" is the English for it; not an added quantifier in force.
2. Units 14 and 38 `l` "peoples" against `i` "the people": λαοί is plural, and "peoples" keeps the plural in the literal layer while "the people" is the English collective; same sense.
3. Units 15 and 39 `l` "to me give heed": ἐμέθεν is a genitive after συνίημι; English "give heed to me" cannot show the case, and the note names it a genitive.
4. Unit 23 `i` "that very day" for ἤματι κείνῳ: "that same/very day" is the ordinary sense of the demonstrative; `l` keeps "on that day".
5. Unit 33 `l` "These, having called them together" (τοὺς … συγκαλέσας): "them" doubles the object; English needs an object for the participle, and "These" keeps the fronted τούς. Literal layer is allowed this.
6. Unit 53 `l` "he saw it" / `i` "has seen it" for aorist ἴδεν after νῦν δ’: English perfect is the right rendering of an aorist of present result; `l` keeps the aorist.
7. Capital or lower-case at the start of `i` after a semicolon (units 3–6 lower, 14–16 capital): the published iliad-001/-004/-005 mix both after ";" and ":", so there is no rule to enforce.
8. Unit 11 `i` and unit 37 "above his head" (the Odyssey ships "over his head" in `i`): the departure is recorded in `new-renderings.md` and the sense is the same.
9. Unit 13 `l` "son of Atreus, wise-minded, horse-taming" reads as epithets of the vocative: it follows the Greek order (genitives agreeing with Ἀτρέος); `i` and the note state the construction correctly.
10. Units 22 and 29 `l` "indeed" for μέν ῥα: stock particle rendering, as in the Odyssey.
11. Unit 48 `l` "their many-thwarted ships": "their" is supplied by English for σὺν νηυσί; the `i` has it too, and the army's ships are meant.
12. Unit 50 split at a comma (lines 76–77, then 78): line 78 is a whole-unit repeat of iliad-001's 1.73 and must stand alone, and the part before it is under four lines. Accepted.
13. Unit 1 note's reason for merging ("the second is only the speech-introduction"): true as far as it goes; the further reason (the whole-unit rule on 2.7) is in `new-renderings.md`. Left as is.
14. Unit 36 `i` "above all … most nearly": double superlative follows the Greek (μάλιστα … ἄγχιστα); kept.

## Open points for the owner or the next step (not changed here, since the reviewer edits `units.json` only)

1. `new-renderings.md` rows now out of step with `units.json` and to be corrected before the rows are copied into `conventions.md`:
   - θέμις / "ἔπεσιν πειρήσομαι, ἣ θέμις ἐστί": `l`/`i` now "as is the custom" (avoided list should name "as is lawful" instead of listing "as is proper" only). The Odyssey itself is not uniform here (odyssey-009/010 "as is right", the later table row 14.130 "custom"); I followed the table. If the owner prefers the shipped "as is right", change units.json 2.73 in both layers.
   - ἄλγεα … στοναχάς: `l` "lay both pains and groans".
   - σκῆπτρον πατρώϊον: `i` "his fathers’ sceptre, which never fails".
   - εἶδός τε μέγεθός τε … ἄγχιστα ἐῴκει: `l` "in form and in size and in stature it most nearly resembled".
   - οἳ μὲν ἐκήρυσσον: now the Odyssey's wording ("They made-proclamation, and the others gathered very quickly." / "The heralds made the proclamation, and the people gathered very quickly.").
   - κλῦτε φίλοι: `i` "Hear me, friends" (reasoning in the row about "Hear me" being reserved is wrong given odyssey-070).
2. The glossary pass should note that the unit-48 note now treats ἥ as the relative (nominative feminine) in `ἣ θέμις ἐστί`, and that ἔειπεν is described as "the epic form of εἶπεν".
