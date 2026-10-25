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

*Settled in pass 2 (see below): `new-renderings.md` now matches `units.json`, and `gloss.json` has been checked against every line.*

- **new-renderings.md is now out of step with units.json** and must not be copied into conventions.md as it stands. Rows to correct or drop: ἔθνεα πεζῶν ("hosts" → `l` "tribes", `i` "bands"), ἄλλυδις ἄλλος ("one this way, one that"), ἔντεα ("gear", not "armour"), σὺν τεύχεσι / τεύχεα ("armour", not "arms"), ἀϋτῇ ("battle-cry"), θωρήσσοντο ("were arming themselves"), ξείνια ("the things due to guests" / "the hospitality due to guests"), ἄστυ ("town"), τόφρα ("for that time"), πόλλ’ ἐπέτελλον ("commands" / "charged you strictly"), μετακλαύσεσθαι (`i` "greatly"), αἴ κέν τι φόως (the 8.282 English), and the ἱππηλάτα Πηλεύς / τερπικέραυνος rows (table forms).
- No `gloss.json` exists yet in this draft folder, so the second-pass check of glossary parses was not possible; it should be done when the glosser has run.

## Pass 2

Reviewer pass 2. `t` untouched (checked identical to the pass-1 file for all 83 units). Edits made by script (`rev070p2.py`, `gloss070p2.py`, `nr070p2.py` in the scratchpad) with each replacement asserted to match exactly once. Every cross-reference number in the notes was re-checked against the packet's line numbers (660, 686, 688, 692, 709, 711, 713, 714–716, 715, 739, 756–758, 765, 789, 2.27, 6.208, 7.157, 8.282, 9.252–253, 9.259, 11.646, Od. 9.42, 9.549, 14.100–101): all stand. The section "Left for the drafter" above is now settled: `new-renderings.md` has been brought into line (see the third table). Severity key as above; no H found in pass 2.

Totals: **H 0 · M 17 · L 25** (gloss.json 6 M + 14 L; units.json 3 M + 2 L; new-renderings.md 8 M + 9 L).

### gloss.json (every parse checked against its line in units.json; 201 novel entries, 11 `__broaden__` entries)

| # | Key | Sev | What was wrong | What was done |
|---|---|---|---|---|
| G1 | περίτρεσαν | M | Attic equivalent given as ἐπερίτρεσαν; the augment of a compound goes inside, so the equivalent is περιέτρεσαν. | Corrected. |
| G2 | τριηκόσι | M | Parsed as masc. acc. pl. τριηκόσιοι (elided); the elided form is neut. acc. pl. τριηκόσια (the three hundred head, 697), and an -οι elision is not what is printed. | Re-parsed: neut. acc. pl., elided τριηκόσι’ = τριηκόσια, Attic τριακόσια. |
| G3 | ὄληται | M | Called a "short-vowel subj."; it is the ordinary long-vowel (η) thematic aorist subjunctive. The "(= Attic ὄληται)" was empty. | Both removed. |
| G4 | θεύσεσθαι | M | Meaning ’to be going to run’ is wrong for the bare infinitive (ἔμελλον supplies "were going to"); "(= Attic θεύσεσθαι)" was empty. | Meaning ’to run’; empty equivalent removed. |
| G5 | διείπομεν | M | "aor. διεῖπον" is not the aorist of διέπω. | Parse now: 1 pl. past, impf. of διέπω (augment inside the compound) or aor. of διεῖπον ’tell through’, as the note reads it. |
| G6 | οὕνεκά | M | "(= Attic οὕνεκα)" is a non-equivalent; the Attic prose equivalent is ὅτι. | "epic (= οὗ ἕνεκα; Attic ὅτι)". |
| G7 | θέουσ | L | "epic uncontracted (Attic θέουσα)": Attic θέουσα is the same word. | Removed the false contrast. |
| G8 | νομῆας | L | Attic equivalent -εῖς; the Attic accusative plural is νομέας. | Corrected. |
| G9 | ἀπονήσεται | L | Lemma ἀπονίναμαι; LSJ lemmatises ἀπονίνημι (and the unit note says so). | Lemma ἀπονίνημι. |
| G10 | ἀρήνης | L | "(= Attic -ης, after ρ -ας)" is nonsense for an η-stem. | Removed. |
| G11 | κάσχεθε | L | "κατ- assimilated" disagrees with the note (preverb shortened). | "κατ- shortened by syncope". |
| G12–G20 | ἀγέλας, ἀπέτραπε, ἐλίγαινον, ἑπέσθω, ἔτρεσαν, ἠθέλετον, ἤγαγον, ὑπῆσαν, παρέθηκεν | L | An "(= Attic …)" equivalent identical to the Homeric form (or, for ἀπέτραπε and παρέθηκεν, a non-difference), which teaches nothing and is false as a dialect claim. | Equivalents removed; ἐλίγαινον given the rendering ’cried out clearly’ to match the unit. |

`__broaden__` entries: all eleven checked (old entry whole, then " · ", then one new reading), each justified by a use in this part: βίῃ (787, dative of respect; the βίη at 670 and 690 is nominative and is covered by the existing βίη entry), κ (764 ἐπεί κ’ + subj.), κατ (770 κατ’ Ἀχαιΐδα), μάχεσθαι (746 after ἀριστεύεσκε), παῖδ (710 and 750, dual), πρεσβυτάτην (740), τύχε (684), ἑταίρου (793), χειρὸς (675 ἀπὸ χειρὸς), τίς (705 μή τίς οἱ). No change. Known-form check for missed broadenings, forms whose use differs from the stored reading: ὃ, οἱ, ᾗσι, ᾧ, οἷσιν, τῷ, τὼ, τῶν, τοὺς, τὰ, τὸν, ὡς, ὃς, ὅσσοι, ὅσσον, ἐπεί, πὰρ, ἐνὶ, ἀμφὶ, μετὰ, μετ, κατὰ, ἦ, ἔμελλον, θωρήσσοντο, πολλὰ, πολλὸν and the rest of the 528 were read against their lines; none needs a broadening. No entry contains a line number, "here", an ASCII apostrophe or a backtick; all novel entries are under 230 characters; article-forms are glossed as pronouns (none are novel here); the possessive ὅς (ᾗσι, ᾧ, οἷσιν) is kept apart from the relative (οἷσι at 686 is the relative).

### units.json

| # | Unit | Field | Sev | What was wrong | What was done |
|---|---|---|---|---|---|
| U1 | 767 νῶϊ δέ τ’ | l, n | M | ἐπέτελλε `l` "gave his charge"; the house `l` for the plain verb is "laid his charge" (4.301, 9.259, and 765 in this part), `i` "gave his charge". | `l` "how he laid his charge"; note gloss matched. |
| U2 | 783 Πηλεὺς μὲν | l, i | M | `l` "gave charge" and `i` "charged his son Achilles"; the plain ἐπέτελλε is "laid his charge" / "gave his charge" (the "charged strictly" idiom belongs to πόλλ’ ἐπέτελλεν). | `l` "laid his charge"; `i` "gave his son Achilles his charge, always to be the best and to stand above the others;". |
| U3 | 785 σοὶ δ’ αὖθ’ | l, n | M | `l` "thus gave charge". | `l` "thus laid his charge"; note gloss matched (`i` "gave this charge in turn" already house). |
| U4 | 701 τοὺς δ’ αὖθι | n | L | "the epithet the Iliad gives Agamemnon": a claim about the rest of the poem that this part cannot show. | "the phrase the translation also gives Agamemnon". |
| U5 | 739 γαμβρὸς δ’ ἦν | n | L | "the same word as for Menelaus": same kind of claim. | "the translation’s word for ξανθός of people", as at 680. |

Re-read once more and found sound: all `l`/`t` line divisions, all quotation marks (“ at 656, ‘ at 786, ’ at 788–789, ” at 802), all `mark` and `p` values, the two-unit lines 759, 762 and 790, the published/repeated lines (655, 670, 679, 766, 778, 784, 790), and the house renderings for ἄστυ "town", τεύχεα "armour", ἔντεα "gear", θωρήσσοντο "were arming themselves", ἀϋτή "battle-cry", τόφρα "for that time", πόλλ’ ἐπέτελλον, ἱππηλάτα Πηλεύς, τερπικέραυνος, αἴθοψ, δαΐφρων, ἄλλυδις ἄλλος and αἴ κέν τι φόως, each against its table row.

### new-renderings.md (brought into line with units.json)

Every quoted `l` and `i` cell was machine-checked as a substring of the unit text (ellipses split). The rows that pass 1 listed as contradicting the units were handled as follows: ἔθνεα, ἄλλυδις ἄλλος, ἔντεα (the ἀνὰ … ἔντεα row), μετακλαύσεσθαι, ξείνια and ἀϋτῇ were corrected; there is no row for τεύχεα / σὺν τεύχεσι, θωρήσσοντο, ἄστυ, τόφρα, πόλλ’ ἐπέτελλον, αἴ κέν τι φόως, ἱππηλάτα Πηλεύς or τερπικέραυνος in the file (the units take the table's English for each, so none is a new rendering), and none was added.

| # | Row | Sev | What was wrong | What was done |
|---|---|---|---|---|
| R1 | ἔθνεα πεζῶν | M | `l`/`i` "the hosts of men on foot"; the units have `l` "tribes", `i` "bands". | Row states "tribes" / "bands" with the reason. |
| R2 | ἄλλυδις ἄλλος | M | "one this way, another that" / "and another that"; units use the table's "one this way, one that" / "and one that". | Corrected. |
| R3 | ἀνὰ … ἔντεα | M | "armour"; units (755, and 731) use the table's "gear". | Corrected; "armour" listed as reserved for τεύχεα. |
| R4 | μετακλαύσεσθαι | M | `i` "will weep long afterwards"; the unit has "will weep greatly afterwards". | Corrected. |
| R5 | ξείνιά τ’ εὖ παρέθηκεν | M | `l` "set out well the hospitality"; the unit has "the things due to guests". | `l` and `i` corrected; reference corrected to the Odyssey table (14.404). |
| R6 | ἀϋτῇ | M | "with a shout"; the units have "with a battle-cry" (the table's ἀϋτή). | Corrected. |
| R7 | δαιτρεύω | M | Said the infinitive at 705 was "shared out"; both layers read "to divide". | Row now covers 688 and 705. |
| R8 | ἀτεμβόμενος · ἴσης | M | Did not say the clause is the Odyssey's English (9.42, 9.549). | Added, with the full `l`/`i`. |
| R9 | Μολίονε | L | Only the 709 rendering; 750 has "the two of Actor’s line, the Molions" / "the pair of Actor’s line, the Molions". | Both places stated. |
| R10 | ἀρετῆς ἀπονήσεται | L | Table reference 8.237 (an unrelated row); the ἀρετή row is 8.535; ἀπονίνημι is not in the table. | Reference fixed; ἀπονίνημι said to be new. |
| R11–R15 | ἲς … μέλεσσιν, ἠοῖ φαινομένηφι, ὀδὰξ ἕλον οὖδας, βοῦν ἀγελαίην, δῆμος | L | "the table’s" row cited by an Odyssey number (11.393, 16.270, 22.269, 17.181, 16.425) with no "Odyssey", so read as Iliad references. | "Odyssey table" added. |
| R16–R17 | βεβλήαται …, ὑπερηφανέοντες … | L | `l` "have been struck" / `i` "treated with insolence" are not contiguous in the unit text (indeed / us). | Ellipses added. |

### Findings considered and refused in pass 2

- **Unit 724 ἔθνεα `i` "bands" against the table's ἔθνεα "swarms" (2.87, 2.91).** The table's `i` "swarms" serves the simile; these are men on foot, and 7.115 gives "band"; kept, and the row now says why.
- **704 δῆμος "the people" against the Iliad table's "land".** Already settled in pass 1 (Odyssey 16.425 row); kept.
- **Gloss Arene "a town of Elis", Alesium "a place in Elis", Minyeïus "a river of Elis".** Locations are the usual ones for these names and are not contradicted by the part; kept.
- **ἐπέφραδε as reduplicated 2nd aorist of φράζω.** Matches the note and LSJ's ἔπεφραδον; kept.
- **ἔκταθεν "(= Attic ἐκτάνθησαν)".** A real Attic correspondent for the passive sense; kept.
- **ἀθλοφόροι "prize-bearing, prize-winning".** Both are dictionary senses; the unit uses the first; kept.
- **ἴσης "(μοίρης understood)".** Accepted gloss for the genitive of separation; kept.
- **Notes naming the Odyssey's γέρων ἱππηλάτα Νέστωρ (772).** Backed by the shipped table row (7.125); kept.
- **Unit 777 `l` "led us in … bade us" against the published 11.646 "led him in … bade him".** The pronoun differs because the persons differ (the note says so); kept.
- **ἀμφὶ βοὸς … κρέα ἕπετον (776) as needing an ἀμφί + gen. broadening.** Taken as ἀμφέπω in tmesis with κρέα as object, which the existing ἀμφὶ entry (preverb in tmesis) and the ἕπετον entry already cover; no broadening.
- **Gloss κέαται, κίοι, κιόντι "(= Attic …)" equivalents.** Real dialect differences; kept.
