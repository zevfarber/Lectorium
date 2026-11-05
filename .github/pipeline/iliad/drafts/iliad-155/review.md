# Review of iliad-155 (Iliad 24.302–404), pass 1 (+ sweep of own changes)

Reviewer: adversarial; `t` untouched (checked: the `t` of all 62 units joined equals the packet's 103 lines exactly). Edits made to `units.json` by script. Gloss.json not yet read (second pass).
Checks run: grammatical labels in every note; positional claims; cross-references (16.231, 3.276, 1.286, 10.384, 24.292, 24.372/377/378, Odyssey 10.279); Greek to `l` word by word; `l` to `i`; table conformity (Iliad table incl. the 24.200–301 rows already merged, Odyssey table, published Iliad units for the same Greek); quotation marks (balance per layer now 8/8 and 8/8; mark on the first unit of each of the 8 speeches; 154's last unit closes Priam's speech, so unit 0 correctly opens with none); paragraph marks (all 10 ¶ lines carry `p`); line counts of `l` against `t`; no `\n` in `i`; no backticks or ASCII apostrophes in notes; scansion flags: none in the packet, nothing to add.

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 385 | `l` | high | Closing ” missing on the last unit of Hermes' first speech (`i` had it); the layer's “ ” count was unbalanced and the validator would fail. | Added ” to `l`. |
| 403 | `l` | high | Same: closing ” missing in `l` on the last unit of Hermes' second speech. | Added ” to `l`. |
| 364 | `l`, `i`, `n` | medium | μένεα πνείοντας rendered "breathing fury". The Iliad table (2.536) fixes μένεα πνείοντες as "breathing might" and expressly reserves "fury" away from it; published 3.8 (iliad-016), 2.536 (iliad-012) and 11.508 (iliad-068) all have "breathing might". Same Greek, same English. | `l` "breathing might"; `i` "who breathe might"; note now says ‘breathing might’ and no longer glosses μένος as ‘fury’. new-renderings.md row for μένεα πνείοντας must be dropped or corrected (see below). |
| 364 | `i` | low | οὐδὲ σύ γ’ is "not even you"; `i` "Are you not afraid" lost the "even" that `l` has. | `i` now "Are not even you afraid of the Achaeans, who breathe might and are ill-disposed and hostile to you, close by?" |
| 302 | `i` | medium | ἦ ῥα καί: the table (Odyssey 8.416, extended in the Iliad at 21.590, 23.563) fixes `l` "He spoke, and" / `i` "So he said, and". `i` had "He spoke, and". | `i` "So he said, and the old man urged …". |
| 329 | `n` | medium | Label untrue: "The first οἳ is the whole escort". The first οἳ δ’ ἐπεί takes in everyone who came down (Priam and Idaeus too); only οἳ μὲν ἄρ’ in the next line is the escort that turns back, against τὼ δ’. | "The first οἳ is the whole company, Priam and Idaeus with the escort". |
| 390 | `n` | medium | Label untrue: "εἴρεαι is the Ionic form of ἐρέεσαι" (no such form). εἴρεαι is the 2 sg. present of εἴρομαι. | "εἴρεαι is the second person singular of εἴρομαι ‘ask’". |
| 306 | `n` | medium | Claim about repetition false in part: "The first two lines open a prayer in the same words as 16.231". Only line 306 and οὐρανὸν εἰσανιδών are shared; καὶ φωνήσας ἔπος ηὔδα is new here. | Note now says the first line and οὐρανὸν εἰσανιδών are the words of 16.231 and the English is kept for them. |
| 354 | `l` | medium | Δαρδανίδη rendered "descendant of Dardanus" in `l`; the table (3.303, 11.166) and every published `l` (iliad-019, -044, -065, -067, -081, -141, -153) have "Dardanus’ descendant"; "descendant of Dardanus" is the `i` form. | `l` "Take heed, Dardanus’ descendant;". |
| 354 | `i` | low | φράζεο + warning: published `i` is "Take care" at 5.440 (iliad-031), 16.446 (iliad-103), 22.358 (iliad-141); the draft had "Take heed" in `i` (the `l` "Take heed" matches iliad-031 and is kept). | `i` "Take care, descendant of Dardanus: …". |
| 358 | `l` | medium | "with the old man his mind was poured together" reads σύν as a preposition governing γέροντι; it is tmesis (σὺν … χύτο) and γέροντι is a dative of the person affected. The English suggested a wrong case relation. | `l` "and for the old man the mind was poured together"; note adds that γέροντι is a dative of the person affected. |
| 388 | `i` | low | ἄποτμος is "ill-fated" in both layers in the table (Odyssey 20.140, Iliad 24.255 "utterly ill-fated"); `i` had "unfortunate". | `i` "my ill-fated son". (new-renderings.md row for 24.388 must be corrected to match.) |
| 379 | `l`, `i` | low | Greek ends in a full stop (ἔειπες.) but both English layers ended in ";" (carried over from the published 1.286 unit, whose Greek has ano teleia). The stop of the English follows the Greek's, as the drafter did for the sandal lines. | Both layers now end "." (words unchanged). |
| 380 | `l` | low | Greek unit ends in a comma, `l` ended ";" (carried over from a ano teleia). | `l` ends ","; `i` keeps ":" (deliberate, the note explains it). |
| 385 | `n` | low | The note asserts Ἀχαιῶν "depends on μάχης" as plain fact; ἐπιδεύετ’ Ἀχαιῶν can also be taken together. | Note keeps the reading the English takes and adds that the Greek leaves the construction open. |
| 312 | `n` | low | Note glosses νοήσας ‘perceiving’ while `l` says "seeing it myself". | ‘seeing’. |
| 324 | `n` | low | Note says δαΐφρων "is rendered ‘wise-minded’" but `i` says "wise-hearted". | Note names both layers (table: 4.252). |
| 370 | `n` | low | Note renders φίλῳ … πατρί "to a dear father", `l` has "my dear father". | "my dear father". |
| top | `about` | low | "Idaeus sees him and warns Priam" follows a sentence about Priam, so "him" reads as Priam; it is Hermes whom Idaeus sees. | "Idaeus sees the stranger and warns Priam". |

Count: high 2, medium 7, low 10 (19 findings acted on; 21 field edits).

## Findings considered and refused

- ἀμφίπολον ταμίην / ἀμφίπολος "attendant" (302, 303). Iliad table row 6.491 says the Iliad's house word for ἀμφίπολος is "handmaid(s)", but (a) the exact pair ἀμφίπολον ταμίην is shipped in odyssey-078 as "the attendant housekeeper", the Odyssey table is binding for the Iliad, (b) the same table (22.442) and iliad-038, -142 ship "attendant(s)", (c) the draft's new-renderings row records the choice. Left as drafted; the owner may want to settle "handmaid" vs "attendant" in QUESTIONS.md (the corpus is split).
- ἀκήρατον "pure" (302). Odyssey 17.532 has "untouched" for ἀκήρατος of goods; here the word qualifies water, and "pure" is not among the avoided renderings. Kept; the note states the doubt about the derivation.
- ὀνείατα "helpful things" (366). Odyssey 10.9 has "dainties/delicacies" of food; here the goods on the wagon are ransom, and "delicacies" would be false. The new-renderings row records the departure. Kept.
- ἄψορροι "back again" (330). Table 3.313 has "returning", but 4.152, 7.413 and 16.376 use "back again/back" for the same stem. Kept.
- ἔσταν = ἔστησαν "intransitive aorist" (359). True: the Attic 3 pl. of ἔστην is ἔστησαν; no change.
- Formula remarks in notes ("the ordinary line for a prayer heard", "βάσκ’ ἴθι … used when a god sends a messenger"). Wider than this part shows in strictness, but each is true of the poem and matches the tables; house style across published notes. No change.
- ἐπιχεῦαι, στῆσαν, χύτο, ἔδεισας, δειδιότες, ὄπωπα, ὁρόω, ἄμμε, ἔασι, ἔξεσσι/ἔξειμι, πέπνυσαι, ἐσσυμένους, κιόντα, προφανέντε, τὰς (fem. pl., the mules): each parse checked and true; no change.
- Unit 39 (374) `i` drops ἔτι "still" in ἀλλ’ ἔτι τις; judged within the freedom of `i`. Unit 14 `i` "lamenting greatly" for πόλλ’ ὀλοφυρόμενοι fine.
- Unit 47 `i` "against the Achaeans" (l "with"): the context (Hector's fighting) supports "against"; kept.
- No scansion flags in the packet; nothing to add.

## For the caller: new-renderings.md rows that now disagree with units.json (the drafter's file, not edited here)

- Delete the row "μένεα πνείοντας (24.364)" ("breathing fury"): the table's 2.536 row already governs, "breathing might".
- Row 24.388 (ἀπότμου): `i` is now "my ill-fated son"; the avoided-list should drop "ill-fated".
- Add or fold in: φράζεο (24.354) `l` "Take heed", `i` "Take care" (follows iliad-031 / -103 / -141); ἦ ῥα καί `i` "So he said, and" (table row, no new row needed).

## Second sweep of my own changes

Re-read each edited unit against its Greek: 302, 306, 312, 324, 329, 354, 358, 364, 370, 379, 380, 385, 388, 390, 403 and `about`. No new error found: quotation marks now balanced (8/8 in both layers), no newline or apostrophe damage, `t` byte-identical. Pending for the second pass: read gloss.json and check every parse against the line.

---

## Pass 2 (gloss.json and a second look at units.json)

Checked: every key's parse and meaning against its line in units.json (83 new forms, 13 broadened); the 13 `__broaden__` entries against iliad-glossary.json (each is the old entry whole, then ` · `, then one new reading; all 13 verified, and each new reading is true of its use here); length (all new entries under 230; broadened entries are cumulative by design); typographic ’ only, no ASCII apostrophe or backtick; no line numbers or "here"; novel-forms.json and gloss.json cover the same 83 keys, none of them already in iliad-glossary.json. units.json: no backticks, no ASCII apostrophes, line counts of `l` against `t` equal; `t` untouched; nothing new found.

| Form | Severity | What was wrong | Done |
|---|---|---|---|
| λάθον | medium | "+ acc. of the one deceived": nobody is deceived; Zeus is the one who fails to notice (τὼ is the dual subject, εὐρύοπα Ζῆν the accusative). | "+ acc. of the one who fails to notice (here εὐρύοπα Ζῆν)". |
| λιτανεύσομεν | medium | Gloss gave only the future, but the note at 356 says the form may be a short-vowel aorist subjunctive ("let us beseech"); entry and note disagreed. | Entry now gives both. |
| ἔλασσαν | medium | "augment ἔ-" is wrong: the form is unaugmented (ἐλασσ-), as the shipped ἔλασσε entries in both glossaries say. | "epic -σσ-, unaugmented (= Attic ἤλασαν)". |
| ἔξειμι | low | Homograph with ἔξειμι ‘go out’ (Odyssey glossary entry) left unmarked. | Added "(not ἐξ + εἶμι ’go out’)". |
| ἔνισπες | low | "strong aor. 2 sg. act. ἔνισπες" was circular. | "aor. 2 sg. act. (2nd aor. ἔνισπον)". |
| πνείοντας | low | Said "with the acc. μένεα" only; the participle agrees with Ἀχαιούς. | Now "agreeing with Ἀχαιούς and governing the acc. μένεα". |
| ἀντιβολῆσαι (broadened) | low | New reading asserted μοι as dative of the person met; the note at 374 leaves open whether μοι goes with ἧκεν or ἀντιβολῆσαι. | New reading hedged; old entry untouched. |

Count: high 0, medium 3, low 4 (7 changes).

Refused / left as is: ἀμφίπολον "handmaid" (the Odyssey glossary has "handmaid, attendant"; the Iliad entry is dictionary-gloss, unaffected by the `l` choice); πρόχοόν (gender not given, LSJ's feminine not certain enough to assert); ἀγητός "(from ἄγαμαι)", αἰσυμνητῆρι "in apposition", παλλόμενος, ἄγαγ’ (imperative), ἐπιδεύετ’ (impf.), φίλτατόν (accent before enclitic), ἐξείρετο-type old entries: each checked and true. Broadened τὴν "demonstrative … object of ἔχων" overlaps the older "standing for a feminine thing" reading but is true of the use; kept.
