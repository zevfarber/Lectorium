# Review — iliad-150 (Iliad 23.700–796)

Two passes. Pass 1: notes (labels, positions, cross-references checked against `source/iliad-monro-allen1920.json` and the packet), Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks and marks, repeated lines against the packet, house table (`conventions.md` and `../odyssey/conventions.md`) grepped for every epithet and formula. Pass 2: every changed unit re-read in full, and `gloss.json` read against the lines. `t` was not touched (checked by script: all 59 `t` identical to the original; `ln`, `p`, `mark` unchanged). Edits to `units.json` and `gloss.json` by script only (scratchpad `rev150.py`, `rev150b.py`, `gl150.py`).

Counts (units.json): 8 major, 3 medium, 13 low = 24 rows; plus 10 gloss.json fixes (1 medium, 9 low). No high. Scansion flags in the packet: none.

## Changes made to units.json

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 708 · l | major | πολύμητις rendered “Odysseus of many wiles” in `l`. The table (πολύμητις; 5.214, 7.207, 8.165, 18.51) fixes `l` “many-wiled”, `i` “of many wiles”. | `l` “and up many-wiled Odysseus stood, knowing cunning ways.” (`i` already right; note unchanged.) |
| 754 · l | major | Same fault, second occurrence. | `l` “and up many-wiled Odysseus, and then Nestor’s son”. Line 754 itself still equals the published unit (iliad-148). |
| 740 · l, i | major | τετυγμένον: the table (κρητῆρα τετυγμένον, 4.615) gives `l` “wrought”, `i` “well-wrought”, and reserves “well-made” for ἐυεργής. Draft had `l` “well wrought” (adds “well”) and `i` “well made”. Also ἄεθλα was “prizes” in `l` while every other occurrence (700, 785) and the note say “contest-prizes”. | `l` “other contest-prizes for speed, / a silver mixing-bowl, wrought;” `i` “… a silver mixing-bowl, well-wrought;”. Note: “made, wrought”. |
| 728 · l, i, n | major | θάμβησαν rendered “were amazed”. The table (θάμβησεν, 1.199) gives “was struck with wonder” and turns “was amazed” down (“amazement” is reserved for τάφος); and “gazed in wonder” for θηεῦντο would have put “wonder” twice in the clause (table: θηεῦντο “gazed at”, 10.524). | `l` “both gazed and were struck with wonder.” `i` “the people gazed, and were struck with wonder.” Note says “gaze at” and “be struck with wonder”. |
| 770 · l | major | ποδοῖιν row in new-renderings.md fixes `l` “come as a good helper to my two feet”; the unit had “to my feet come as a good helper” (word order, and the dual lost). | `l` “Hear, goddess; come as a good helper to my two feet.” |
| 765 · l | major | ῥίμφα: the table (12.182, 13.83) fixes “nimbly” and turns “lightly” down. `i` and the note already said “nimbly”. | `l` “always running nimbly;” |
| 777 · l, i, n | major | Note and `l` made στόμα the subject (“was filled his mouth and nostrils”) and called ῥῖνας part of the subject: ῥῖνας is accusative only; στόμα is accusative here too. Both are accusatives of the part affected; the subject is Ajax. A false grammatical label and an `l` that does not follow the Greek. | `l` “and with ox-dung he was filled, in mouth and nostrils;” `i` “and he was filled with ox-dung in mouth and nostrils;” note rewritten (unnamed subject Ajax; two accusatives of respect). |
| 757 · n | major | “στὰν … the same as ἔστησαν”: ἔστησαν is the transitive aorist (the note at 744 says so); the intransitive aorist is ἔσταν. | “στὰν is ἔσταν, the intransitive aorist of ἵστημι”. |
| 791 (second unit) · l, i, n | medium | ἐριδήσασθαι rendered “contend”. The table turns “contend” down for ἐριδαίνω (1.574, 16.765: “quarrel”) and ἐρίζειν of feet is “rival” (13.325); “contend” is also the word for ἀεθλεύω (737). None of those fits a race exactly, so a neutral word was taken. | `l` “to strive for Achaeans”, `i` “to strive with him on foot”, note “to strive with the feet … (‘quarrel’, here of a contest)”. A row is needed in new-renderings.md: ἐριδήσασθαι (23.792) “strive” · “strive”, avoiding “contend” (ἀεθλεύω), “rival” (ἐρίζω), “quarrel” (strife). |
| 724 · l | medium | μελήσει: table (11.332, 11.352, 12.70) `l` “will be a care to”; unit had “will be Zeus’ concern” (the `i` wording). | `l` “and these things, in turn, to Zeus will all be a care.” (`i` “concern” is the table’s `i`.) |
| 765 · n | medium | “χέ’ is the unaugmented aorist of χέω”: it is χέε, the imperfect (the gloss was right). | “χέ’ is χέε, the unaugmented imperfect of χέω.” |
| 757 · l, i, n | low | σημαίνω: table (7.175) “mark”; draft “pointed out” / “showed”. | `l` “Achilles marked the limits.” `i` “Achilles marked out the limits of the course.” note “σήμηνε is ‘marked’”. |
| 719 · n | low | “The second clause ends with ἔχεν”: it ends with ἲς Ὀδυσῆος. | “In the second clause ἔχεν ‘held’ has no object …” |
| 731 · n | low | “κάππεσε at 727”: the word stands at the start of 728 (727 ends Ὀδυσσεύς). | “at 728”. |
| 744 · n | low | “Thoas, named only here”: Θόας is named elsewhere in the poem. | “named only here” cut. |
| 744 · l | low | “made it stand in harbours” gives στῆσαν an object, which the note says the Greek does not state. | “and made stand in harbours,” |
| 704 · n | low | “She is a captive … the poem says so plainly”: the Greek says only that she is valued at four oxen and knew many works. | “Like the tripod she is given a price: …” |
| 780 · n | low | “what he says is ironic”: the note asserts a tone the line does not give. | Cut. |
| 723 · n | low | ἀνάειρ’ called “the aorist imperative”; the form is the (present-stem) imperative, and the aorist imperative of ἀείρω is ἄειρον. | “the imperative of ἀναείρω”. |
| 725 · l | low | “of the trick not forgetful was Odysseus” gives an adjective for λήθετ’, an aorist verb (note and `i` say “did not forget”). | “and of the trick did not forget Odysseus;” |
| 729 · i | low | “a knee was hooked in” puts an interpretation (a hook) into γνάμψεν “bent”; `l` and note say “bent”. | “and a knee was bent in;” |
| 763 · i, n | low | “could settle round them”: ἀμφιχυθῆναι is “be poured round”; “settle” means come to rest, and is a ready-made phrase. | “could spread round them”; note “has spread round them”. |
| 770 · n | low | “(… used of Athena as helper at 4.390)” read as the Iliad’s 4.390; the table’s ἐπίρροθος (4.390) is the Odyssey. “ἀγαθή … agreeing with the goddess” is not an agreement (ἐπίρροθος is the noun). Also filler. | “in the Odyssey …”; “ἀγαθή is feminine because the helper asked for is the goddess herself”; “the prayer is short and to the point” cut. |
| 740 · n | low | Note glossed τετυγμένον “made” only; `l` is now “wrought”. | “made, wrought”. |

## Changes made to gloss.json

| form | severity | what was wrong | what was done |
|---|---|---|---|
| θάμβησάν | medium | “be amazed” against the table’s “be struck with wonder”. | “be struck with wonder, marvel”. |
| ἀμφιχυθῆναι | low | “to settle over” is not the meaning. | Cut; “to be poured around”. |
| στήθεός | low (glosser’s query) | “gen. of nearness: at the breast” fits ἀγχόθι στήθεος but not the first στήθεός (the rod “of the breast”, dependent on κανών). | “gen. with ἀγχόθι (‘near the breast’) or dependent on a noun (‘the breast’s’)”. |
| ἀμείβοντες | low (glosser’s query) | Sense stated flat. | “traditionally taken as a noun, ‘rafters’ (sense uncertain)”. |
| ἐριδήσασθαι | low | “contend”; “dat. of the opponent” (the dative in the line is Ἀχαιοῖς, of the person). | “quarrel, strive; … (+ dat. ‘with’): ‘to strive’”. |
| ἐρείδεσθον | low | “strain” vs `l` “press on”. | “press on”. |
| ἐμπυριβήτην | low | “going on the fire” vs “fire-treading”, note “stand over a fire”. | “treading the fire, made to stand on the fire”. |
| κανών | low | “the weaver’s rod of the loom” claims the exact part; the note says it is not said. | “in weaving, exact part uncertain”. |
| μίν | low | Entry pinned to one use (“acc. subject of an infinitive”); the form is object at 722. | “object, or subject of an infinitive”. |
| θόαντι (__broaden__) | low | Old entry “Thoas, Aetolian leader”; the new use is the king of Lemnos. | Second reading now “another Thoas, king of Lemnos”. |

Glosser’s other two queries: λοισθήϊ’ (“neut. acc. pl., elided; as last prize”) is correct for 751 and left; ἀϋτμένα (“acc. sg., stem ἀϋτμεν-”) is correct (ἀϋτμήν, -ένος) and left. All 86 novel forms are covered; no entry over 230 characters, no line numbers, no straight apostrophes.

## Checked and found true (no change)

- Quotation marks: eight speeches, “ on the first unit and ” on the last (707 single unit; 723–724; 735–736; 753; 770; 782; 787–791b; 795–796), `mark` on exactly the eight first units; same marks in `l` and `i`. The neighbouring part (iliad-149) ends at 699 with no speech open. `p` falls on 700, 725, 738, 740, 784, 793 = every ¶ of the packet.
- Repeated lines identical to the published English: 706 and 752 (whole unit, identical to iliad-145), 738 (iliad-052, `l` and `i`), 771–772 (iliad-028), 723 (iliad-008), 713 (iliad-101 wording kept), 754 (iliad-148 wording kept).
- Cross-references verified in the source: 11.811, 16.213, 9.79 (full stop there), 5.121–122, 6.505, 23.684, 2.173; in-part references 702, 709, 718, 741, 750, 751, 754, 756, 757, 759, 760, 763, 767.
- Table items that conform: δῖος “heavenly”, πολύτλας “much-enduring”, κέρδεα εἰδώς “knowing cunning ways”, ποδώκης “fleet-footed”, πόδας ὠκύς, γλαυκῶπις “gleaming-eyed”, ἐϋζώνοιο “well-girdled”, ἠεροειδέα, φαίδιμος “glorious”, ἐριμύκων “loud-bellowing”, Τελαμώνιος, ταχὺς Αἴας Ὀϊλῆος, κρατερή “strong”, ὢ πόποι “Ah”, ἡδὺ γέλασσαν, κραιπνοῖσι, ἐπίρροθος “helper”, νότιος ἱδρώς, ἀναΐξαντε, ἐϋκνήμιδας, ἱέσθην/ἱεμένῳ, ἀνίαζον, ὦνον, κώληψ, ἔκφερε, νύσσα, κανών, ὠμογέρων, κύδηνεν, μέλεος αἶνος, ἀγραύλοιο, μύθοισιν ἀμειβόμενος προσέειπεν (as 3.437).
- Scansion: no flagged lines.

## Considered and refused

- τῖον “valued” against the table’s τίω “honour” (1.508, 2.21): the price context (ἐνὶ σφίσι, δυωδεκάβοιον) requires “valued”; the new-renderings row records it. Left; the row could add that τίω is “honour” elsewhere.
- 748 `i` “for his own companion’s games” (“games” not in the Greek): the genitive οὗ ἑτάροιο is the occasion of the prize; the note says so. Left.
- 774 βλάπτω “harm”: the Iliad rows give “hinder/hamper” for horses and chariots, but the table keeps “harm” where a person is hurt; `l`, `i`, note agree. Left.
- 707 `i` “try your strength” for πειρήσεσθον: nothing in the table; `l` “make trial” is literal and the phrase is not a set one. Left.
- 729 note “the natural reading is that Ajax hooks his knee”: a reading stated as such, with `l`/`i` leaving the subject open. Left.
- 744 `i` “moored”: sense assumed from the note; kept as the plain reading of στῆσαν ἐν λιμένεσσι.
- 787 `l` “To those who know, I shall tell you, friends, all of you”: awkward but follows εἰδόσιν … πᾶσιν. Left.
- Duplicate `ln` values (758, 791): two units begin mid-line in each; consistent with other parts.
