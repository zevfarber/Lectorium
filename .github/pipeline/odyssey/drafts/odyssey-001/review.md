# review-001 — adversarial review of draft-001 (Odyssey 1.1–95)

Gate after review: `DRAFT GATE PASS: 51 units tile lines 1-95 exactly`
`t` untouched (asserted equal to the pre-review copy, `draft-001.prereview.json`). Edits applied by
`review_001_apply.py`, `review_001_apply2.py`, `review_001_apply3.py` (whole-field or asserted substring
replacement, `ensure_ascii=False, indent=1`). 43 fields changed in 27 units.
Mechanical checks run: note length 40–110 (1.81: 25–45); no `?` in any note; quotation marks only on
units 1.32 “, 1.40 ‘ ’, 1.43 ”, 1.45 “, 1.62 ”, 1.64 “, 1.78 ”, 1.81 “, 1.93 ”; `mark` on 1.32, 1.45, 1.64, 1.81 only;
1.44 = 1.80 and 1.45 = 1.81 identical in `l` and `i`.

## Changes

| line | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| 1.3 | n | high | "three clauses in a row open on the same word": false. πολλά is the LAST word of line 1 and its clause opens with ὅς; only lines 3 and 4 open on πολλ-. | Rewritten: πολλά closes line 1, πολλῶν/πολλά open lines 3 and 4. |
| 1.1 | l | low | μάλα πολλά as "very far" hid the πολλ- repetition the 1.3 note points at. | "who very much". |
| 1.1 | n | medium | "πτολίεθρον … its πτ- useful to the metre": not true of this line (ἱερὸν is closed before π- either way); conventions forbid metre remarks that do not explain the form here. | Now "an epic derivative of πτόλις, the old by-form of πόλις". |
| 1.11 | i | low | "got clear of" colloquial beside the rest; `l` has "fled". | "had escaped steep destruction". |
| 1.11 | n | medium | "destruction is pictured as a precipice" stated as fact; it is the usual explanation, not a known one. "in the next line" pointed outside the unit. | "the usual explanation is … a fall from a height"; "in line 13". |
| 1.16 | l | low | "seasons-of-years" invents a compound; ἐνιαυτῶν is simply "years". | "as the years rolled round". |
| 1.16 | i | low | "his own people" dropped φίλοισι. | "his own dear ones". |
| 1.16 | n | low | Drafter's report flags πεφυγμένος + genitive as unusual but the note was silent. | One sentence added. |
| 1.22 | i | medium | `l` "to partake of", `i` "to receive": two different senses of ἀντιάω. | `i` now "to partake of". |
| 1.22 | n | high | ἀντιόων described only as ἀντιάω "with the vowel stretched out" while `l` translates purpose ("to partake"): the form is a future participle of purpose (same form as the present). Also "the gods go to feast with them" generalises beyond this passage; "in the next line" vague. | Label corrected; generalisation cut; "burnt-faces" marked as how the Greeks heard the name; "line 23". |
| 1.26a | n | medium | δαιτί said flatly to be "governed by παρήμενος"; it may equally go with ἐτέρπετο. | Both constructions given. |
| 1.26b | l | medium | δή rendered "meanwhile" — an invented temporal sense. | "but the others, now,". |
| 1.29 | i | medium | μνήσατο (aorist) given as pluperfect "had called to mind"; `l` has "remembered". | "called to mind". |
| 1.31 | n | medium | "introduces every speech": claim beyond this part. | "introduces each speech in this part; the edition ends it with a raised point". |
| 1.32 | l | high | Finite αἰτιόωνται turned into a participle with a dash ("what a thing, now — mortals accusing"); οἷον rendered as a noun phrase while the note calls it an adverb 'how!' (note contradicted `l`). | "“Ah! how indeed, now, mortals accuse the gods;". |
| 1.32 | i | high | "Well! What a thing this is, the way mortals accuse the gods!" — "Well!" too mild and chatty for ὢ πόποι; "the way (these) mortals … the gods" reads as remembered (Fagles). | Rebuilt from the grammar: "“Ah, how mortals do accuse the gods!". |
| 1.33 | i | high | κακά softened to "troubles"; καὶ αὐτοί dropped although the note builds its point on it ('they themselves as well'). | "It is from us, they say, that evils come, when they themselves as well, by their own wanton folly, have pains beyond what was allotted,". |
| 1.37 | l | low | "knowing of" against the note's "εἰδώς takes a direct object". | "knowing the steep destruction,". |
| 1.37 | i | low | μνάασθαι "court" while `l` and the notes at 1.35/1.90 say "woo". | "woo". |
| 1.40 | n | high | ἱμείρεται called just "a subjunctive with a short vowel": it must be the AORIST subjunctive (aor. ἱμειράμην), beside ἡβήσῃ; a present has no short-vowel subjunctive. No reason was given for treating the lines as direct speech. Metrical irregularity absent. | Rewritten: aorist subj.; ὣς ἔφαθ’ Ἑρμείας (1.42) named as the evidence for direct speech; one sentence on the metre (see below). |
| 1.47 | n | high | Did not say what the edition prints. Also overstated: unaccented ὡς + optative is a legitimate wish-construction ('would that'), so the archive's ὡς need not be a slip. | Note now states the edition prints ὡς unaccented, that it is taken as 'so' (usually ὥς, cf. 1.6, 1.42), and that ὡς can also simply introduce a wish. |
| 1.48 | l | high | δαΐφρων "fiery-minded" follows a different etymology from `i` "wise-hearted" (decision a). | "wise-minded". |
| 1.48 | i | low | "his own people" for φίλων (no possessive ὅς here; phrase reserved for ὅς). | "far from his dear ones". |
| 1.48 | n | medium | Doubt stated but not which reading the unit follows; the δαίω 'kindle' view (the old `l`) unmentioned. | Rewritten; all three views, the one followed named. |
| 1.51 | n | high | "This Atlas stands in the sea": not in the Greek (he knows the sea's depths and ἔχει the pillars). | "knows the sea's depths and has the pillars in his keeping". |
| 1.55 | l, i | medium | Cleft "His daughter it is who / It is his daughter who" adds an emphasis the Greek lacks; `i` "unhappy" softens δύστηνον (`l` "wretched"); "grieves" for ὀδυρόμενον ("lamenting"); αἱμυλίοισι "cajoling" in `l`, "coaxing" in `i`. | Cleft removed; "wretched … as he laments"; "coaxing" in both. |
| 1.59 | i | high | "And still … your own heart does not turn towards him at all": σοί περ ('not even you') lost, "still" and "at all" invented. | "Yet not even your own heart, Olympian, turns to take heed." |
| 1.59 | n | medium | Aphorism "Hers is rent; his does not move"; punctuation statement vague. | Aphorism cut; note says the edition prints a full stop after Ὀλύμπιε, taken as a statement, can be read as a question. |
| 1.60 | l | medium | "do you favour" reads as an English present with "you" as subject. | "gratify you". |
| 1.60 | i | low | "please you well": "well" not in the Greek. | "please you". |
| 1.62 | l, i | high | ὠδύσαο: `l` "taken-offence" far too mild for a verb the note glosses 'be angry at, hate' and on which it builds 'man of hatred'; `i` "has he become so hateful to you" reverses the syntax (Zeus is the subject). | `l` "Why, then, him so greatly have you come-to-hate, Zeus?”"; `i` "Why then, Zeus, have you come to hate him so?”". |
| 1.64 | n | medium | Full stop mentioned, but not how it is being taken. | "The edition ends it with a full stop; it is taken here as an exclamation, and it can also be read as a question." |
| 1.68 | l | low | ἀσκελές "unrelentingly" in `l`, "stubbornly" in `i` and `n`. | "stubbornly" throughout. |
| 1.68 | i | medium | "now as always" invents "now"; "blinded in his eye" unidiomatic. | "is always stubbornly angry on account of the Cyclops whose eye Odysseus blinded". |
| 1.76 | i | medium | "work out … together, and how he is to get there": "together" invented, "get there" chatty. | "think out his homecoming, how he is to come". |
| 1.76 | n | medium | Note called ὅπως ἔλθῃσι a purpose clause while `l` translates an indirect question ("how he may come"). | Note now: 'how he is to come', shading into purpose. |
| 1.77 | i | low | Possessive ὅς: "his anger" against "his own" everywhere else. | "his own anger". |
| 1.81 | n | — | Missing. | 33-word nudge back to 1.45 (and to 1.44 = 1.80). |
| 1.88 | l | low | φρεσί "heart" here, φρένας "mind" at 1.42 (note there: seat of thought). | "mind". |
| 1.90 | l | medium | "head-long-haired" (decision b). | "the long-haired-of-head Achaeans". |
| 1.90 | i | medium | "never stop slaughtering" strains αἰεί; "so that he calls" stilted. | "so that he may call … who are always slaughtering". |

Counts: high 11 · medium 17 · low 12 · task-addition 1 (1.81 note) — 41 rows, 43 fields.

## 1.40 scanned by hand
ἐκ (long by position) · γὰρ Ὀ- (⏑⏑) | -ρέσ-τᾱ- (– –) | -ο τί-σις | ἔσ-σε-ται (ται shortened before Ἀ-) | Ἀ-τρε-ΐ- | -δᾱ-ο.
The genitive ending is -ᾱο; τίσις has short ι (LSJ) and -σις is open before ἔσσεται. So the third foot is ⏑ ⏑ ⏑ and only
scans if -ο is lengthened in the longum at the masculine caesura. I agree with the machine. Sentence added to the
note: "As transmitted, the line is metrically irregular at that word: its final -ο has to count as long at the caesura
before τίσις, whose ι is short." Nothing further is claimed. The UNRESOLVED flag should be settled as "brevis in longo
at the caesura" by a person.

## Hermes' words, 1.40–41: nested ‘ ’ kept
The primary-sequence future and subjunctives would not alone prove direct speech, but ὣς ἔφαθ’ Ἑρμείας (1.42) is the
capping formula of a quoted speech and only makes sense if the preceding words are Hermes' own. Marks kept in both
layers; the note now gives this reason.

## Three decisions
- **(a) δαΐφρων** → the δαῆναι reading in both layers: `l` "wise-minded", `i` "wise-hearted". LSJ 1897 itself assigns
  'wise, prudent' to the Odyssey and 'warlike' to the Iliad; 'fiery' (δαίω 'kindle') is the least supported. It keeps the
  three -φρων epithets distinct (wise-minded · much-minded · enduring-minded). The note states all three views.
  The conventions table row needs updating.
- **(b) κάρη κομόωντας** → `l` "the long-haired-of-head Achaeans" (`i` unchanged). Shows the accusative of respect without
  the "headlong" misreading. Table row needs updating.
- **(c) αἰπὺς ὄλεθρος** → "steep destruction" CONFIRMED for both layers, 1.11 and 1.37. "Sheer destruction" is the
  rendering of more than one modern translation; "utter" loses the image. "Steep" is LSJ's first gloss and the oddness
  is the Greek's. The note no longer asserts the precipice image as fact. Add to the table.

## Considered and refused
- 1.1 `i` "driven far off his course": checked for echo (Fagles "off course"); it is the dictionary gloss of πλάζω, kept.
- 1.8 `l` "who down the cattle … / ate": ugly, but it is what makes the tmesis visible and the note explains it; "up" would falsify κατά.
- 1.3 `i` "bore many pains" vs `l` "suffered": same force; left.
- 1.9 `i` "the day of their homecoming" coincides with a modern version but is the fixed house rendering and ordinary English.
- 1.16–19: considered repunctuating the sense (parenthesis); the edition's full stop rules, and the note already says so.
- 1.29 note "That household is the poem's foil": common plot knowledge, kept.
- 1.38 "Homer never tells the story" (Argus): true and standard; kept.
- 1.43 `i` "paid the whole debt in one sum": "debt" is an addition, but ἀποτίνω implies it and the note covers it.
- 1.46 `i` "lies low": considered "lies dead"; κεῖται is plain "lies", kept.
- 1.54 ἀμφὶς ἔχουσιν, 1.74 ἐκ τοῦ, 1.78–79 genitives, 1.60 τ’: notes already give both readings honestly.
- 1.62 note "'the man of hatred'": does not cite Book 19; kept.
- 1.84 "unerring" (`l`) / "unfailing" (`i`) for νημερτέα: same sense and force; left.
- 1.84 `i` "the guide, the slayer of Argus": awkward triple title but it is table policy.
- 1.92 "crumple-horned": table policy; note already marks ἕλικας uncertain.
- Did not edit `conventions.md` (fixed policy; a person should ratify a, b, c and then update the table).

## For a person to rule on
1. Ratify (a), (b), (c) and update the house table before Part 2.
2. 1.47 ὡς: check the printed Loeb page. Either reading is defensible; the note covers both.
3. 1.40: record the scansion ruling (lengthening at the caesura) so `sc` can ship without the UNRESOLVED flag.
4. ὢ πόποι now "Ah" in both layers; it recurs through the poem and needs a fixed house rendering.
