# Review — iliad-070 (Iliad 11.655–803), pass 1 and pass 2

Reviewer: adversarial. `t` untouched (checked: identical to the pre-review file and to the pinned source lines 655–803). All edits were made to `units.json` by script (`rev070.py`, `rev070b.py` in the scratchpad), each replacement asserted to match exactly once. No unit changed length outside 25–110 words in `n`; line divisions of `l` still match `t`; no `\n` in `i`.

Severity: **H** = would fail the validator or makes the English wrong; **M** = house-rendering departure from the Iliad/Odyssey tables, a false grammatical label, or a false cross-reference; **L** = precision of wording, a claim the page cannot support, or a small mismatch between note and translation.

Unit key: line number of the unit's first line, plus its first Greek word, because 759, 762 and 790 each carry two units.

## Changes

| # | Unit | Field | Sev | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 790 ὣς ἐπέτελλ’ | l, i, n | H | The unit is word for word the published unit at 9.259 (iliad-054) but had different `l` and `i` ("So the old man gave charge, and you forget" / "That was how the old man charged you…"). The validator would have failed it. | `l` and `i` set to the published ones ("So he laid his charge, the old man, but you forget;" / "So the old man gave his charge, and you forget it;"). Note now says the unit is 9.259 with that line's English. |
| 2 | 660 βέβληται | n | M | "ὃ … is the article used with a name" contradicted `l` ("Struck is he, the Tydeus'-son"), which takes ὃ as the pronoun "he". | Note: ὃ is the pronoun "he" (the Homeric article), Τυδεΐδης in apposition. |
| 3 | 662 βέβληται δὲ καὶ | n | M | "The verb is βέβληται again, as in the line before": the line before (661) has οὔτασται; βέβληται is at 660. | "as at 660". |
| 4 | 664 αὐτὰρ Ἀχιλλεύς | n | M | (a) "a pair the Odyssey also puts side by side": κήδεται … ἐλεαίρει is not in any published Odyssey part; the repository has it at Iliad 2.27 (iliad-007). (b) "Argives in the next line": Ἀργείων is at 667, two lines on. | (a) "a pair that also stands together at 2.27". (b) "two lines on". |
| 5 | 668 οὐ γὰρ ἐμὴ ἲς | n | L | "reason for his fear": nothing in the Greek is fear; the γάρ gives the reason Nestor cannot act himself. | Reworded. |
| 6 | 677 ληΐδα | n | M | "The last two lines are repeated from the Odyssey": only the second half of 678 and all of 679 are (odyssey-066, 14.100–101). | Note says exactly that, with the Odyssey cite. |
| 7 | 680 ἵππους | n | L | "ἵππους is masculine in form": the accusative plural is the same for stallions and mares; "masculine" is a false label. | Reworded. |
| 8 | 682 καὶ τὰ μὲν | l, i | M | ἄστυ rendered "city". The Iliad table (προτὶ ἄστυ, 2.801) fixes "town" and reserves "city" for πόλις. | "to the town" in both layers. |
| 9 | 694 ταῦθ’ ὑπερηφανέοντες | n | L | "χαλκοχίτωνες … stock epithet of the Epeans": the table has the epithet only for the Achaeans; nothing in the repository shows it as stock for the Epeans. | Note says the translation gives the epithet to the Achaeans elsewhere and uses it here of the Epeans. |
| 10 | 698 καὶ γὰρ τῷ | n | L | (a) "μετ’ ἄεθλα is 'for the contests'" against `l`/`i` "to the contests". (b) "the next line says why they were stopped": 700 says why they had come, and the stopping is in 701. | (a) "to the contests". (b) "the next lines say why they had come and what Augeias then did". |
| 11 | 704 τὰ δ’ ἄλλ’ | l, i, n | M | (a) μή τίς … κίοι ἴσης called a "fear-clause": it is a negative purpose clause ("lest"/"so that no one"). (b) "οἱ 'from him'": οἱ is a dative of interest ("for him", "on his account"). (c) The same clause stands in the Odyssey (9.42, 9.549, odyssey-039 and -044) with fixed English ("so that no man, for me, cheated, should go off short of an equal share" / "…on my account, should go away cheated of an equal share"), which this unit did not follow. | `l`: "so that no one, for him, cheated, should go off short of an equal share." `i`: "so that no one, on his account, should go away cheated of an equal share." Note corrected and cites the Odyssey places. |
| 12 | 706 ἡμεῖς μὲν | l, i, n | M | ἄστυ as "city". | "town" in `l`, `i`, and the note's gloss. |
| 13 | 707 οἳ δὲ τρίτῳ | l, i | M | θωρήσσοντο rendered "armed themselves"; the table (4.252, 8.54) fixes "were arming themselves" and lists "they armed themselves" as rejected. The note itself says "were arming themselves". | "were arming themselves" in both layers. |
| 14 | 711 ἔστι δέ τις | l, n | L | νεάτη Πύλου ἠμαθόεντος is the table's row 9.153 ("the furthest of sandy Pylos"); `l` had "farthest". | "furthest" in `l` and in the note's quotation of `l`. |
| 15 | 722 ἔστι δέ τις ποταμὸς | l, i, n | M | ἔθνεα rendered "hosts" in both layers. The table fixes ἔθνεα as "tribes" in `l` (2.87, 2.91, 2.459, 2.464, 2.469; "hosts" listed as rejected) and "band" for ἔθνος of people (7.115; "host" rejected). new-renderings.md's justification cited 7.115 for "host", which is the opposite of what that row says. | `l` "the tribes of men on foot"; `i` "the bands of men on foot"; note follows `l`. |
| 16 | 725 ἔνθεν | l, i, n | M | σὺν τεύχεσι rendered "with our arms" / "armed with our arms". The table fixes τεύχεα as "armour" and rejects "arms"; the published parallel is "in our armour armed" / "armed in our armour" (iliad-051 line 529, iliad-064 line 49). | `l` "with our armour armed"; `i` "armed in our armour"; note likewise. |
| 17 | 725 ἔνθεν | n | L | "a river is ἱερός because it is divine": a claim the page cannot support. | "a river that receives a sacrifice in the next lines". |
| 18 | 730 δόρπον | l, i | M | ἐν ἔντεσιν rendered "armour". The table fixes ἔντεα as "gear" and reserves "armour" for τεύχεα. | "gear" in both layers. |
| 19 | 732 ἀτὰρ μεγάθυμοι | l, i, n | M | ἄστυ as "city" (twice) and "the city of 711" in the note. | "town" in `l` and `i`; note: "the town … is the πόλις of 711". |
| 20 | 743 ἐγὼ δ’ ἐς δίφρον | l, i, n | L | ὀρούσας "leapt": the published parallel (iliad-067, 359) has "sprung/sprang". | "sprung" / "sprang", and the note's gloss follows. |
| 21 | 744 ἀτὰρ μεγάθυμοι | l, i, n | M | ἄλλυδις ἄλλος rendered "one this way, another that". The Odyssey table fixes "one this way, one that" / "one this way and one that" and lists "another that" as rejected. new-renderings.md omitted this row. | "one this way, one that" / "one this way and one that"; note follows. |
| 22 | 750 καί νύ κεν | n | L | "Ἀκτορίωνε Μολίονε are two patronymic names": Μολίονε is not shown to be a patronymic; Ἀκτορίωνε is. | Note says Ἀκτορίωνε is the patronymic and Μολίονε the name the pair are known by. |
| 23 | 754 τόφρα | l, i, n | M | (a) τόφρα rendered "For so long": the table (1.509, 9.550, Od. 8.438/8.453) fixes "for that time"/"meanwhile" and lists "so long" as rejected. (b) ἔντεα καλά rendered "fine armour" (see 18). | (a) `l` "For that time indeed we followed"; `i` already "For all that time" (kept); note "for that time … until". (b) "fine gear" in both layers. |
| 24 | 759 ἔνθ’ ἄνδρα | n | M | "πύματον 'last' is the superlative of πύματος": πύματος is the lemma, not something πύματον is the superlative of. | "the accusative of πύματος". |
| 25 | 759 ἔνθ’ ἄνδρα | n | L | "ἔνθ’ is the place the last unit named": the places were named two units back (756–757). | "the place where the chase ended, named at 756–757". |
| 26 | 763 ἦ τέ μιν οἴω | i | L | "weep long afterwards" for πολλὰ μετακλαύσεσθαι, whose `l` is "greatly weep afterwards": "long" adds duration the Greek does not say. | "weep greatly afterwards". |
| 27 | 765 ὦ πέπον | n | L | "the same words are followed by the same second line" at 9.252: the first lines differ (πατὴρ … Πηλεύς there, Μενοίτιος here); only the opening and the second line are shared. | "opens the same address at 9.252; the second line here is 9.253 word for word". |
| 28 | 765 ὦ πέπον | n | L | "Nestor now turns to Patroclus": he has been answering Patroclus all along. | "turns from his own tale to Patroclus' own past". |
| 29 | 772 γέρων δ’ ἱππηλάτα | l, i, n | M | (a) Διὶ τερπικεραύνῳ in `l` as "bolt-delighting Zeus": the Iliad table and iliad-005, -012, -015 fix "Zeus delighting-in-the-thunderbolt" (the "bolt-delighting" form is the Odyssey's). (b) `i` "the old man Peleus, the horse-driver" departs from the table row (7.125) "Peleus, the old horse-driver". (c) Note: "The golden ἄλεισον 'goblet' pours αἴθοπα οἶνον" made the goblet the subject of σπένδων; the subject is Peleus. (d) "the formula that Nestor himself carries elsewhere": only the Odyssey's Nestor is in the table. | (a) `l` "for Zeus delighting-in-the-thunderbolt", note likewise. (b) `i` "Peleus, the old horse-driver". (c) "He holds a golden ἄλεισον 'goblet', σπένδων 'pouring' αἴθοπα οἶνον". (d) "that the Odyssey uses of Nestor". |
| 30 | 777 ταφὼν | n | M | "the line used of Nestor's reception of Patroclus at 645": the shared line is 11.646 (iliad-069's unit starts at 645; the matching second line is 646, and 11.778 here = 11.646). | "at 646". |
| 31 | 777 ταφὼν | l, i, n | M | ξείνια rendered "the hospitality" in `l`; the Odyssey fixes `l` "the things due to guests" and `i` "the hospitality due to guests" (odyssey-013, -069, -073, -093). | `l` "the things due to guests, as is the custom for guests"; `i` "the hospitality due to guests, as is the custom for guests"; note likewise. |
| 32 | 777 ταφὼν | l | L | ταφών opened "and, amazed, Achilles sprang up," while the published parallel (iliad-053, 193) is "and amazed sprang up Achilles,". | Set to the published order. |
| 33 | 782 σφὼ δὲ | l, i, n | M | πόλλ’ ἐπέτελλον rendered "gave many charges": the table (4.229, 6.207; Od. 11.267) fixes "commands" in `l` and "charged strictly" in `i` for ἐπέτελλον with πόλλα. | `l` "gave many commands"; `i` "charged you strictly"; note follows. |
| 34 | 783 Πηλεὺς μὲν | n | L | "the father's charge at 6.208": ambiguous (it is Glaucus' father, not Peleus, who speaks there). | "the charge Glaucus' father gave him at 6.208". |
| 35 | 790 ἀλλ’ ἔτι καὶ νῦν | n | L | δαΐφρονι called "a stock epithet of Achilles": nothing in the repository shows it so; also said "wise-minded" only, while `i` has "wise-hearted". | Note: an epithet of disputed meaning; "wise-minded" in `l` and "wise-hearted" in `i`, as everywhere else. |
| 36 | 792 τίς δ’ οἶδ’ | n | L | "helping the speaker" is ambiguous (Nestor is the speaker). | "here helping Patroclus". |
| 37 | 794 εἰ δέ τινα | n | L | "τινά is a second prophecy": the Greek says only that his mother told him of some prophecy; a second one is not in the text. | "is again 'some prophecy', understood from the first clause". |
| 38 | 796 ἀλλὰ σέ περ | l, i, n | M | αἴ κέν τι φόως Δαναοῖσι γένηαι is the same clause as 8.282 (iliad-048), already published as "if somehow a light you may become to the Danaans" / "in the hope that you may somehow become a light to the Danaans". The unit had "in case … a light to/for the Danaans". | `l` and `i` set to the published English; note says "as at 8.282". |
| 39 | 798 καί τοι | l, i, n | M | τεύχεα rendered "his fine arms"; table: τεύχεα "armour", "arms" rejected. | "his fine armour" in both layers and the note. |
| 40 | 802 ῥεῖα δέ κ’ | l, i, n | M | ἀϋτῇ rendered "with a shout"; the table (1.492, 4.328) fixes ἀϋτή as "battle-cry" and lists "the shout" as rejected. new-renderings.md lists "battle-cry" as the rejected form. | "with a battle-cry" in `l`, `i` and note. |
| 41 | 802 ῥεῖα δέ κ’ | l, i | M | προτὶ ἄστυ rendered "to the city"; table row 2.801 is exactly προτὶ ἄστυ "toward the town", "to the city" rejected. | "to the town" / "back to the town". |

Counts: H 1 · M 23 · L 17 (41 rows; units touched: 35 of 83).

## Findings considered and refused

- **Unit 0, 655 (whole-line reply formula).** `l` and `i` are identical to the published iliad-024/-047/-053/-059 and Odyssey units. Refused as a finding; nothing to change.
- **657 `i` "how great it has grown" for ὄρωρε** (`l` "has arisen"). Looked at as a drift; refused: "grief grows" is ordinary English for the same event and no other word of the Greek is lost.
- **658 `i` "the best of the men".** "of the men" is supplied but the referent is plain (οἳ … ἄριστοι); refused.
- **666 `l` "are warmed" against `i` "are set burning".** Deliberate and declared in the note ("grim understatement"); the table has no row for θέρομαι; refused.
- **664 ἐσθλός / i "good man though he is".** Matches the table (ἐσθλός "good") and the note flags the bitterness; refused.
- **674 `i` drops λαοί (folds it into "the countrymen").** λαοὶ … ἀγροιῶται is apposition; the `l` keeps both; refused.
- **685 `i` "all those" for τοὺς … οἷσι.** Natural English for the relative pair; refused.
- **687 `i` drops ἄνδρες in "Πυλίων ἡγήτορες ἄνδρες".** Pleonastic apposition, kept in `l`; the table row for ἡγήτορες has no "men"; refused.
- **704 δῆμος as "the people".** The Iliad table rows give δῆμος "land", but row 16.425 (δῆμον ὑποδείσας) already allows "the people" where folk are meant; here the δῆμος shares out goods. Kept; the draft's new-renderings.md entry stands.
- **735 συμφερόμεσθα "we clashed" (`l`) / "we met" (`i`) for an imperfect.** The note says imperfect; a plain past is acceptable English for a narrated clash; no table row; refused.
- **744 note "the sentence breaks at ·".** Awkward but true of the printed stop; refused.
- **786 `l`/`i` end in a semicolon where the edition has a full stop.** The next unit begins ἀλλ’ and the English continues the same quoted sentence; refused.
- **796 `i` "in the hope that" against `l` "if somehow".** Not a new fault: both now follow the published 8.282 pair exactly (see row 38).
- **761 δῖος Ὀδυσσεύς, 727 γλαυκώπιδι, 735 φαέθων, 750 ἐνοσίχθων, 692 ἀμύμων.** All checked against the tables ("heavenly", "gleaming-eyed", "shining", "earth-shaker", "blameless" with the note saying the sense is unknown); correct as drafted.
- **Quotation marks.** “ opens `l` and `i` of the unit at 656 (mark "Nestor answers") and ” closes the unit at 802; nested ‘ opens the unit at 786 (mark "Menoetius' charge") and ’ closes the unit at 788. iliad-069 ends with Patroclus' speech closed by ” and 655 is narration, so nothing carries over from the previous part. Checked and correct.
- **Line numbering irregularities.** None in 11.655–803 (the edition's jump at 11.543 is outside); no note needed. Packet flags no scansion irregularity; nothing hand-scanned.
- **Cross-references verified in the repository's published parts:** 2.27 (iliad-007), 6.208 (iliad-037), 7.157 (iliad-042), 8.282 (iliad-048), 9.252–253 and 9.259 (iliad-054), 11.646 (iliad-069), Odyssey 9.42 and 9.549 (odyssey-039, -044), Odyssey 14.100–101 (odyssey-066); within the part, 686, 688, 692, 709, 711, 713, 714–716, 715, 739, 751, 756–757, 765 and 789 all stand where the notes say. Eurypylus's wound and Machaon's carrying-out are in iliad-069 (the previous part), as the notes state.

## Left for the drafter / the next step (not edited here)

- **new-renderings.md is now out of step with units.json** and must not be copied into conventions.md as it stands. Rows to correct or drop: ἔθνεα πεζῶν ("hosts" → `l` "tribes", `i` "bands"), ἄλλυδις ἄλλος ("one this way, one that"), ἔντεα ("gear", not "armour"), σὺν τεύχεσι / τεύχεα ("armour", not "arms"), ἀϋτῇ ("battle-cry"), θωρήσσοντο ("were arming themselves"), ξείνια ("the things due to guests" / "the hospitality due to guests"), ἄστυ ("town"), τόφρα ("for that time"), πόλλ’ ἐπέτελλον ("commands" / "charged you strictly"), μετακλαύσεσθαι (`i` "greatly"), αἴ κέν τι φόως (the 8.282 English), and the ἱππηλάτα Πηλεύς / τερπικέραυνος rows (table forms).
- No `gloss.json` exists yet in this draft folder, so the second-pass check of glossary parses was not possible; it should be done when the glosser has run.
