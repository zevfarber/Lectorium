# odyssey-098 — review (20.1–97)

Two passes. First pass: notes (every grammatical label against the form in its line, every claim about where a word stands against the line, cross-references), Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks, the three lines already published, the rows of `new-renderings.md` against the house table, and the rows against what is already shipped. Second pass: `gloss.json` read against each form in its line, and the known forms of the part read against their existing entries. `units.json` was edited in place by script; every `t` was asserted identical before and after (57 units, same `ln`, `v`, `p`; the units' `t` still reproduce the 97 packet lines word for word, and `p` falls on exactly the ¶ lines). Nothing was built.

Counts (one count per field edited): **High 0 · Medium 15 · Low 21** (units.json 8 Medium / 13 Low; gloss.json 7 Medium / 8 Low). Rows of `new-renderings.md` amended: 2 Medium, 2 Low (counted separately, not above).

Quotation marks: “ opens on units 9 (20.18), 21 (20.33), 24 (20.37), 31 (20.45), 41 (20.61); ” closes on 12 (20.21), 22 (20.35), 29 (20.43), 36 (20.53), 52 (20.90); `mark` is on exactly those five opening units; l and i agree on every one. No speech is open at the end of the part (20.97 ends on "praying, raising his hands:" and the prayer begins at 20.98, so the next part's first unit opens it). The last unit of odyssey-097 (19.602–604) is narration, so no speech runs into 20.1. The three whole-line repeats (20.36, 20.44, 20.91) are identical to the published `l` and `i`.

## Changes, units.json (line · field · severity · what was wrong · what was done)

| line | field | severity | what was wrong | done |
|---|---|---|---|---|
| 5 (u3) | l | Medium | house table has κακὰ φρονέουσα ἐνὶ θυμῷ (10.317) as "evil thinking in her heart" / "meaning evil in her heart", with "plotting evil" turned down; the same phrase must get the same English, and the new row ("evils devising") departed from it | evils devising => evil thinking |
| 5 (u3) | i | Medium | same | devising evil for the suitors in his heart => meaning evil for the suitors in his heart |
| 5 (u3) | n | Medium | follows l/i | κακὰ φρονέων is 'devising evils' => is 'meaning evil', literally 'thinking evil things' |
| 5 (u3) | n | Low | note said θυμός, κραδίη, ἦτορ and κῆρ are all 'heart' in this part, but at 20.62 θυμός is 'life' (l 'my life') | added "(θυμός is 'life' once, in line 62, and the note there says so)" |
| 6 (u4) | n | Low | μίσγομαι is called "the plain Homeric word" for sleeping with someone: a claim about the rest of the poem this part cannot show | is the plain Homeric word for => is used of |
| 17 (u8) | n | Low | "with the augment lengthened" is a claim about ἠνίπαπε's make-up that the note cannot support (the reduplicated stem is the point) | clause deleted |
| 18 (u9) | n | Low | "its relative ἐτόλμας": 'relative' reads as the pronoun in a grammar note | relative => kin |
| 30 (u18) | i | Medium | table fixes οὐρανός as "heaven" in `l`, "sky" in `i` (σιδήρεος οὐρανός 15.329; shipped οὐρανόθεν "from the sky" in odyssey-025, -029, -040); the new row turned "from the sky" down | descending from heaven => descending from the sky |
| 30 (u18) | n | Low | follows i | οὐρανόθεν is 'from heaven' => 'from heaven', that is out of the sky |
| 40 (u26) | n | Medium | position claim wrong: μοῦνος stands in the same line 40, in the unit before, not "the line before" | in the line before => in the unit before |
| 41 (u27) | n | Low | "the verb Odysseus has used of himself throughout the passage" is false: the narrator has μερμήριζε (10), μερμηρίζων (28), and only θυμός is the subject at 38 | now: the verb that has run through the passage (lines 10, 28 and 38); here Odysseus uses it of himself |
| 43 (u29) | n | Low | note 'those things' against l/i 'these things' | those => these |
| 45 (u31) | n | Low | note 'and indeed' against l 'even someone' | καὶ μέν 'and indeed' => καὶ μέν, 'even indeed' |
| 52 (u35) | n | Low | "she has kept watch, and now sleep may have him as well" asserts a watch the line does not state | replaced by καί is 'also, too' |
| 54 (u37) | n | Medium | wrong label: ἐπὶ … ἔχευεν called tmesis, but ἐπί governs the dative βλεφάροισιν (the shipped note at odyssey-060 says "after ἐπί 'upon'") | rewritten: ἐπὶ βλεφάροισιν is 'upon the eyelids', and ἔχευεν 'poured', from χέω |
| 54 (u37) | n | Low | "the pronoun following the speaker" is meaningless of ὣς φάτο | replaced by "φάτο is ἔφατο without the augment, rendered like ὣς ἔφατ’ in lines 22 and 91" |
| 79 (u48) | n | Low | note 141 words (validator band to 130); ἐϋφραίνοιμι gloss said nothing of ὄφρα | trimmed to 125 words; "βάλοι is 'strike'" and "ἠέ is 'or'" cut; added that ἐϋφραίνοιμι still depends on ὄφρα |
| 83 (u49) | n | Medium | note contradicted its own `l`: it read τὸ … κακόν as one phrase ('that evil') while l has τὸ as subject and "holds the evil"; also 141 words | rewritten: τὸ μὲν … ἔχει κακόν is 'that holds an evil that is even bearable' (τό the subject, ἀνεκτόν with κακόν); trimmed to 128 words |
| 87 (u50) | n | Medium | wrong tense label: ἐπέσσευεν is a past tense (aorist), not the imperfect; the shipped note at odyssey-090 for the identical form says aorist | imperfect => 'a past tense (the aorist)' |
| - | about | Low | "a dream in which a man like Odysseus lay beside her": the Greek has εἴκελος αὐτῷ, not 'a man' (the row for 20.88 turns "a man like him" down) | a man like Odysseus => a figure like Odysseus |
| 1, 2, 20, 25, 36, 44, 59, 70 | n | Low | ASCII apostrophe in English possessives (Odysseus's, animal's, Penelope's, woman's, poem's) against the house ’ | replaced by ’ (one count) |

## Changes, new-renderings.md (so the rows match the units and the table)

| row | severity | what was wrong | done |
|---|---|---|---|
| κακὰ φρονέων (20.5) | Medium | contradicted the table's κακὰ φρονέουσα (10.317) | row now "evil thinking" / "meaning evil", avoids "devising", cites 10.317 |
| οὐρανόθεν (20.30–31) | Medium | row avoided "from the sky" though the table and three shipped parts use "sky" in `i` | `i` "descending from the sky"; avoided column corrected, reason cited |
| ἐτόλμας (20.20) | Low | said "endured" is reserved for τλάω, but the table has ἐπιτολμάω "endured" and τολμήεις "enduring" | reason rewritten (renderings unchanged: the near-repetition ἔτλης / ἐτόλμας is better left visible only through the note) |
| ἐν πείσῃ μένε (20.23) | Low | named the noun πεῖσα; the glossary entry (and LSJ headword) is πείση | πεῖσα => πείση |

## Findings considered and refused

- **ἀμφικαλύψῃ (20.86) 'covered … around' against the table's ἀμφικαλύπτω "enfold" (8.511).** Refused. That row justifies "enfold" by the echo between the horse in Troy and the mountain over the Phaeacian city, and the same eyelid phrase φίλα βλέφαρ’ ἀμφικαλύψας (5.491, odyssey-026, shipped before the row) is "covered all around". `l` keeps "covered … around"; the glossary entry for the form (existing) says 'enfold, cover all round'.
- **δαίμων `l` 'some power' (20.87) against the table's `l` "a power" (6.172).** Refused: the shipped l of the same Greek is "some power" at 12.295 and in odyssey-090/-093 (ἐπέσσευεν κακὰ δαίμων); the new row follows those.
- **ἐπέσσευεν `l` 'drove' / `i` 'has driven'.** Refused: identical to the shipped odyssey-090/-093 rendering of the same two words; an aorist can be English preterite or perfect.
- **ὀσσομένη 'picturing' against the table's κακὰ ὄσσετο "foresaw" (10.374).** Refused: different sense (physical sight of an absent person against presentiment); the new row says it picks one sense deliberately and the note gives the etymology.
- **ἔτλης / ἐτόλμας.** `l`/`i` unchanged ('you bore it' / 'you held out'): "endured" is not used, so the τλάω word is not doubled. The existing glossary entry for ἔτλης reads 'you dared'; it cannot be rewritten (additions only), but it is the other side of the new row's "dared reserved for θαρσέω". Left for the lead to decide whether to broaden it.
- **ἄσχετος (20.19) grammar.** μένος is the accusative of respect, ἄσχετος nominative with Κύκλωψ: note and l are right as they stand ("unrestrained in fury"; no hyphen, since here it is a predicate group, unlike the vocative row).
- **ἠνίπαπε.** Kept as a reduplicated aorist (ἠνίπαπον); only the unsupported augment clause was cut.
- **περί … βεβῶσα called tmesis (u7).** Kept: περιβαίνω with the dative is the construction, and the note says so.
- **'Four gods, four gifts' (u45).** Kept: Aphrodite, Hera, Artemis and Athena are four gods, and the gifts (beauty and discernment, height, handiwork, and Aphrodite's nurture) are four sets; the sentence is a count, not a claim about the Greek.
- **'one more time, the last and final time' (u6 `i`).** Kept: ἔτι + ὕστατα καὶ πύματα, the doubling is the Greek's.
- **'But now let sleep take you' (u35 `i`).** Kept: 'now' is the exhortative colour of ἀλλά; l is the literal.
- **ἀγαιομένου 'indignant'.** Kept: the table's ἀγάασθαι "resented" (8.565) and ἀγάομαι "in wonder" (10.249) are other shades; the new row explains.
- **'the dog of the simile just above' (u10 note).** Kept: the dog simile is lines 14–16, the word is at 18.
- **οὔ κε / τὸ μὲν … ἔχει (u49) i.** `i` 'is an evil one can even bear' stays (the row in the table carries it); only the note was brought into line with `l`.
- **Notes over the 110-word band (u1, u6, u7, u34, u46, u56: 114–127 words).** Refused: the validator band is a warning above 130, and these are inside it. Unit 33 (22 words) is above its floor of 20.
- **τοὺς (u1) and σχέτλιε (u31) notes.** τοὺς is the relative agreeing with ὀΐων; the note does not say so, but `i` resolves the antecedent ('the sheep that the Achaeans used to sacrifice'). σχέτλιε: the note says "cruel one" is the rendering and the force is nearer 'one who will not give up', as the table row (13.293) requires.
- **ὁππότε κέν τις … (u49), ὀπτηθῆναι, λιλαίεται, αἰόλλῃ, μάλα δ’ ὦκα (u16).** Checked word by word against the Greek; no change.
- **Scansion.** The packet flags none; no unit note carries a metre sentence.

## Second pass: gloss.json (changes: line-free, entries by form)

`gloss.json` had 104 novel entries (exactly `novel-forms.json`) and 15 `__broaden__` entries. Checked: each entry under 230 characters, typographic ’ only, no backtick, no line numbers, none of the 104 already in the glossary, every `__broaden__` entry contains the old entry whole. Parses checked against the line; the forms below were wrong or missing.

| form | severity | what was wrong | done |
|---|---|---|---|
| ἐγρηγορόων | Medium | parsed as a present participle of 'ἐγρηγορέω'; it is the perfect participle of ἐγρήγορα (as the unit's note says), so the lemma and tense disagreed with the note | ἐγείρω — rouse; perf. ἐγρήγορα ’be awake’; perf. part. masc. nom. sg., epic uncontracted -όων (= ἐγρηγορώς) |
| ὑλάκτει | Medium | 'uncontracted (= Attic ἐφθέγγετο/ὑλάκτει)': the form is contracted (-έε- > -ει) and the 'Attic equivalent' is no equivalent | ὑλακτέω — bark; impf. 3 sg., unaugmented: ’barked’ |
| ἄσχετος | Medium | "with Κύκλωψ (or μένος)": μένος is neuter and would need ἄσχετον | "with Κύκλωψ" only |
| ἔχευεν (broaden) | Medium | the added reading made ἐπί … ἔχευεν a tmesis ('ἐπέχευεν'); at 20.54 ἐπί governs βλεφάροισιν (note corrected above; shipped note at odyssey-060 agrees) | the reading is now: also with ἐπί + dat. as a separate preposition: ’poured upon’ (ἐπὶ βλεφάροισιν ἔχευεν) |
| κύντερον (broaden, new) | Medium | existing entry 'neut. nom. sg., with ἄλλο' (from 7.216); at 20.18 it is the accusative object of ἔτλης | broadened: also neut. acc. sg., object of a verb |
| κραδίη (broaden, new) | Medium | existing entry nom. sg. only; at 20.18 it is the vocative | broadened: also fem. voc. sg. |
| ἄρ (broaden, new) | Medium | existing entry has ἄρ’ before a vowel, ἄρ τε, ἄρ κ’; 20.86 ἐπεὶ ἄρ βλέφαρ’ is ἄρ before a consonant | broadened with that use |
| ἐσθλῶν (broaden, new) | Low | existing entry masc. only; 20.86 ἐσθλῶν ἠδὲ κακῶν is neuter, 'good things' | broadened: also neut. gen. pl. |
| ἐγρήσσεις | Low | '= Attic ἐγρηγορέναι stem' is not an Attic equivalent of a present 2 sg. | "epic present beside the perfect ἐγρήγορα" |
| ἐνεῦδεν | Low | lemma εὕδω for a compound; the glossary already lemmatises ἐνεύδειν as ἐνεύδω | ἐνεύδω — sleep in, sleep on (εὕδω with ἐν-); augmented between preverb and stem |
| ἐπέλησεν | Low | '(= Attic ἐπέλησε)' is the same form | dropped |
| ἐϋφραίνοιμι | Low | 'in a wish': it stands in the ὄφρα clause | "’I might gladden’" |
| ἀϊστώσειαν | Low | 'annihilate' is among the renderings turned down in new-renderings.md | "make unseen, make vanish" |
| ἄρτεμι | Low | 'shortened epic (= Attic Ἄρτεμι)' equates the form with itself | "the short vocative (without -ις)" |
| ἔπορ | Low | lemma πορεῖν; the glossary lemmatises every form of this aorist as πόρω (πόρε, πόρεν, ἔπορον) and the note says πόρω | πόρω — give, grant (defective, aor. only) |

Checked and left: the other 94 novel entries (cases, tenses, moods and lemmas agree with the lines; the Attic equivalents named are right). The known forms of the part (388) were read against their existing entries and their lines; the broadenings the glosser made (δῖ, κατ, λιλαίεται, νόημα, τεύξειεν, τοῖσιν, τὰς, τὸ, τῇδε, τῇσι, ὕπο, ὣς, ἠερόεντα, ὑπεκπροφύγοιμι) are right and cover the part's uses. Known entries that I considered and refused to broaden: οἴχοιτο (the existing 'with perf. sense' covers 'go off carrying'), ἐφήσω (fut. or aor. subj.; the sense is the same), σχέτλιε ('reckless, cruel' is a dictionary gloss), ὑπερφιάλοισι ('overbearing' beside our 'overweening' is a dictionary gloss), ἔτλης (see above).
