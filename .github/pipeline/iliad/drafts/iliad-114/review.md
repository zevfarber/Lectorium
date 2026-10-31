# iliad-114 (17.582–672) — review, pass 1 (units and new-renderings; gloss.json not read)

Method: every note label and position claim checked against the line and against the glossary entry for the form; Greek to l word by word; l to i; wording checked against the house tables (Odyssey and Iliad) and against the published units that share lines; quotation marks and speeches; repeated lines against the published parts; line 610 scanned by hand. `t` was not touched (checked: all 53 `t` fields identical before and after; l line counts unchanged; no `\n` in any `i`; no backtick left in any note). Edits were made by script (units.json) and by line replacement (new-renderings.md).

Counts: 24 changes — high 2, medium 11, low 11. Refused: 11 (below).

## Changes (line · field · severity · what was wrong · what was done)

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 612 | n | high | backtick in a note (the validator fails on it) | "`i` names him" became "the English names him" |
| 637 | n | high | backticks in a note | "`l` and `i` there say" became "the English there says" |
| 586 | i | medium | optative with κε ("would") rendered as a future ("will be afraid"); i did not match l in force | "would be terrified of you any longer" |
| 586 | l, i, n | medium | ταρβέω is "terrified" in the table (6.469, 5.286 and the rows that reserve it); the draft used "afraid" | "terrified" in l, i and the note; new-renderings row corrected |
| 588 | l, i, n | medium | πιστὸν ἑταῖρον is "trusty companion" in the Iliad table (15.331, same words, "faithful" turned down); the draft used "faithful" and its row claimed "trusty" was kept for ἐρίηρος | "trusty companion" everywhere; row corrected, with the Odyssey's "faithful" (15.539) named as the clash |
| 591 | n | medium | note says the Odyssey has "the same half-line"; the packet shows the whole line (24.315, odyssey-117) | "the same line" |
| 603 | n | medium | τρέσσε called an imperfect; the glossary and iliad-069 parse it as an aorist (unaugmented), and ὑπέτρεσας in 587 is aorist too | "an aorist without the augment" |
| 605 | l, i, n | medium | μαζός is "breast" in the table (4.123; "nipple" turned down); draft had "nipple" | "beside the breast" in l and i; note changed to match |
| 610 | l, i, n | medium | ὀπάων is "follower" in the table (7.165); "attendant" is reserved for θεράπων (13.246, used in the draft's own row for that reason, wrongly) | "Meriones' follower and charioteer"; note and row corrected |
| 619 | l, i, n | medium | ἤριπε is "crashed down" in the table (4.462, 11.743); "fell" is kept for πίπτω; draft had "fell" | "He crashed down from the chariot" in l and i; note says "crash down" |
| 631 | i, n | medium | "missiles" is the Odyssey's alternative and the table's βέλος row (4.542) turns it down; the draft's own row said "shaft" | "the shafts of all of them hit home"; note says "shafts" |
| 634 | l, i, n | medium | "devise" is reserved for συμφράσσατο, φράζομαι is "plan" (1.554), and "plan" as a noun is reserved for βουλή while μῆτις is "cunning" (2.169, 10.497); the draft used "devise the best plan" / "think out the best plan" and called it a noted departure | l "let us plan the best cunning"; i "let us ourselves plan the best stroke of cunning"; note says why i adds "stroke of"; row rewritten |
| 640 | l | medium | ἀγγελίη is "news" in the table ("message" withdrawn); l had "message", i had "news" | "of the grievous news" in l; row corrected |
| 582 | i | low | "in the likeness of" is the table's rendering of εἴδομαι-type words, not of ἐναλίγκιος, whose i is "like" (o171) | "like Phaenops, son of Asius" |
| 582 | n | low | "οἰκία ναίων is dwelling in a house" hid that οἰκία is a neuter plural object of ναίων | note says so |
| 598 | n | low | βλῆτο called "aorist passive"; it is a root aorist middle with passive sense (glossary) | label corrected |
| 610 | n | low | line 610 is flagged UNRESOLVED; hand scan below shows the irregularity is real | one sentence added to the note (see below); also "no verb in the line" made "in the first line", since the unit's second line has ἕπετ' |
| 623 | l | low | note says καὶ αὐτός is "you yourself too" but l had no "also" | "and you yourself also know" |
| 643 | n | low | ἰδέειν called "the epic infinitive of ὁράω"; it is the aorist infinitive (glossary) | "the epic aorist infinitive" |
| 648 | l, i | low | the unit's Greek ends at an ano teleia; the English kept the comma of the published 8.245 line (iliad-048), where the Greek has a comma | comma changed to a semicolon in l and i (the wording is the published wording; no unit-level repeat, so the validator is not involved) |
| 649 | n | low | note ended "with ἐπὶ … πᾶσα 'the whole battle'", which mixed up the tmesis | rewritten: ἐπί split from φαάνθη, πᾶσα agrees with μάχη |
| 652 | l | low | θᾶσσον is "more quickly" in l (table, 16.129); draft had "the quicker" | "more quickly" |
| 666 | n | low | δίε called "the imperfect of δείδω"; the glossary leaves it as aorist or imperfect | "a past tense of δείδω (poetic δίω)" |
| 669 | l, i | low | Αἴαντ' Ἀργείων ἡγήτορε is the half-line of 4.285, published as "Ajaxes, two leaders of the … Argives" / "Ajaxes, you two leaders of the … Argives"; the dual was dropped | "two leaders" in l, "you two leaders" in i |

### Line 610, scanned by hand
αὐ-τὰ-ρὸ | Μη-ρι-ό | να-ο-ὀ | πά-ο-νά | θ'ἡ-νί-ο | χόν-τε: 17 syllables, so all five dactyls and a closing spondee. That needs the να of Μηριόναο to stand as a long syllable in the long place of foot 3 (the name's α is short; the scanner shows the same licence), and the πά of ὀπάων to be long (it is long in the other published lines with ὀπάων, as the scanner reads them: iliad-042, -048, -058, -110). There is also hiatus between the two forms (ο ὀ). No other way of dividing the syllables gives six feet. The irregularity is real, so the note of the 610 unit now says the line is metrically irregular as transmitted and where, in the same terms as the published note on Ἀγχίσαο (iliad-113, 17.491).

### Quotation marks and speeches (no change needed)
Five speeches, each opened with “ and a mark on its first unit, each closed with ”, in both layers: Apollo as Phaenops 586–590 (units at 586, 587, 588); Meriones 622–623; Ajax 629–647 (opens at the 629 unit, closes at the 647 unit; ὣς φάτο at 648 is outside); Ajax to Menelaus 652–655 (single unit, opens and closes); Menelaus 669–672. Opening and closing counts equal (5 and 5 per layer; the 652 unit carries both). No speech runs on from iliad-113 (its last unit is narrative, 17.580) or into the next part (17.673 is narrative: ὣς ἄρα φωνήσας ἀπέβη). Paragraph flags (582, 591, 597, 624, 626, 648, 656) agree with the packet.

### Repeated lines against the published parts
Whole-unit repeats at 651 and 656 (iliad-110), 659, 660 and 661 (iliad-069): l and i identical to the published units (checked by comparing the validator's own key; no difference). 592 (iliad-026), 648 (iliad-048), 664 (iliad-069, 11.555, written with ἀπὸ νόσφιν there) take the published wording. 591 is the Odyssey's line with the man named in i (departure logged in new-renderings.md). 639 departs from iliad-054 on purpose ("at" for "upon"; the Achaeans, not the Trojans, are the ones who fall); accepted.

## Findings considered and refused

1. 587 and 603 "took fright" (ὑπέτρεσας, τρέσσε) against the 11.546 row (τρέσσε "trembled / flinched"): the later Iliad row (15.586–589, ὑπέτρεσαν) fixes τρέω as "took fright", and both verbs here are fear, not the slow backing away of the lion; left.
2. 649 "mist" / "fog" for ἠέρα / ὀμίχλην, where the table has "mist" for both words: the two stand in one line and would read "mist … mist"; the departure is logged in new-renderings.md and noted; left.
3. 648 the table row for 8.245 says l "pitied"; the published unit (iliad-048) says "grieved for", and the draft follows the published unit. The table row is stale, not the draft.
4. 613 and 615 uncertain subject of ἐγγυάλιξεν and the sense of φάος: both stated as uncertain in the note and logged; the reading (Hector; rescue) is defensible from the grammar; left.
5. 618 "going in all the way" for πρυμνόν: the note and row say the sense is a guess; left.
6. 661 the Greek here has a comma after χειρῶν that the published unit lacks: the validator compares words, not marks, and l and i are identical to the published unit; left.
7. 664 ἔβη (gnomic aorist) rendered "goes" in i: that is the published English of 11.555; left.
8. 620 κιχάνει "overtake": the table has both "reach" and "overtake" for different contexts, and "overtake" fits death and fate; left.
9. 668 ἐπέτελλεν "laid charge / laid many charges on": follows 4.301 and 9.259 (laid his charge); the 5.198 and 6.207 rows are different contexts; left.
10. 652 i "as quickly as he can" for θᾶσσον (table i "quickly"): the comparative is carried in the English phrase; left.
11. 597 note "an adjective telling you which Peneleos": loose but not false; left.

## new-renderings.md
Rows checked against the tables. Rows changed: ταρβέω (inside the 17.587 row), πιστὸν ἑταῖρον, ὀπάων · ἡνίοχος, ἅπτεται, μῆτιν ἀρίστην, λυγρῆς ἀγγελίης. All other rows agree with the table and with the units; the cited rows (7.445, 15.243, 13.246, 11.753, 8.50, 1.359, 5.380, 4.421, 5.156, 11.812, 5.290, 4.542, 11.502, 13.318, 11.555) exist. Not new rows (follow the table; no entry needed): ἤριπε "crashed down", μαζός "breast", θᾶσσον "more quickly".

# Pass 2 (units.json afresh, and gloss.json)

Method: every unit read again from the Greek (l word by word, then l to i, then the note against the line); repeated lines compared with every published part by script (whole-unit repeats at 651, 656, 659, 660, 661 identical in l and i; line-level repeats agree except the intended departures at 637 and 648); quotation marks counted (5 and 5 in each layer); `t` compared with the packet (identical) and with the file before this pass (identical, as are l and i: this pass changed no l or i). gloss.json: all 62 novel forms present and no extra; all 473 word forms of the part have an entry (novel, known or broadened); every parse checked against the line where the form stands; all entries under 230 characters (longest 181); only the typographic ’; no line number, no "here"; every __broaden__ entry checked by script to be the existing entry in iliad-glossary.json whole, then " · ", then the new reading (all 21 pass); the known forms' entries read for coverage of this part's uses (prepositions in tmesis and with cases, the pronoun-article forms, κε/κεν/κέ, μή, ἦρχε, τίς/τις).

Counts: units.json 5 changes (medium 1, low 4); gloss.json 15 entries changed (medium 7, low 8). Total 20: medium 8, low 12, high 0. Refused: 6.

## units.json

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 610 | n | medium | "Lyctus … home of Meriones": the line says only that Coeranus came from Lyctus; Meriones' home is not shown by it | "where Coeranus came from"; "stock epithet" of the town made "a common epithet of towns" (the table shows it of streets and of Lesbos) |
| 640 | n | low | note still said "the grievous message" and "what the message is" after pass 1 made l "news" | "news" in both places |
| 647 | n | low | "to die in sight of the enemy" is not in the Greek (ἐν φάει is "in the light") | "to die in daylight, not blind in the mist" |
| 632 | n | low | "the contrast with the line before" is followed by "because Zeus guides it", which is a reason, not a contrast | "the reason for the line before" |
| 582 | n | low | note was 112 words (band 25–110) and "bound to Hector" and "old ending" said more than the line shows | trimmed to under 110 words |

## gloss.json

| Form | Sev. | What was wrong | What was done |
|---|---|---|---|
| ταρβήσειεν | medium | "be afraid of", "would fear": ταρβέω is "terrified" in the table and in l, i and the note after pass 1 | "be terrified of, dread"; "would be terrified of" |
| φραζώμεθα | medium | "consider, devise … ’let us consider’": φράζομαι is "plan" and "devise" is reserved for συμφράσσατο (pass 1, line 634) | "plan, consider"; "let us plan"; lemma shown as φράζω (mid. φράζομαι) |
| ὀπάονά | medium | "attendant, squire, comrade": ὀπάων is "follower" in the table and in l and i after pass 1 | "follower, attendant, comrade" |
| __broaden__ μῆτιν | medium | new reading quoted "a plan" and "let us devise the best plan", against l "plan the best cunning" | "the best cunning"; "let us plan the best cunning" |
| __broaden__ ἀγγελίης | medium | new reading quoted "of the message"; l now says "news" | "of the news" |
| __broaden__ κοίρανον | medium | existing entry says "a Lycian warrior" (5.677); the Coeranus of this part is Meriones' Cretan charioteer, so the existing entry does not cover the use | broadened: old entry whole, then the Cretan charioteer |
| __broaden__ κοίρανος | medium | existing entry is the common noun "ruler" only; the form is the name of the charioteer (nom., 612) | broadened with the name |
| __broaden__ ἠετίωνος | low | existing entry makes Eëtion "king of Thebe, father of Andromache" only; the Eëtion here is Podes' father and the note says nothing shows he is the same man | broadened: "father of Podes (not said to be the same man)" |
| __broaden__ γενώμεθα | low | "after ἠδὲ καὶ … ὅπως" put ὅπως where the line has none (it is understood from ἠμὲν ὅπως) | "in an indirect question (ὅπως understood from the first clause)" |
| __broaden__ φόβοιο | low | "before flight" for πρὸ φόβοιο, where the English layer has "in the face of grievous flight" | "in the face of flight" |
| λυγρῆς | low | Homeric (Ionic) ending without its Attic equivalent | "Ionic -ῆς (= Attic -ᾶς)" |
| μάστιε | low | epic form without its Attic equivalent | "(= Attic μάστιζε)" |
| ἐπιλίγδην | low | a word whose sense is taken from its context given without saying so | "a rare word, its sense taken from the verb it goes with" |
| πρυμνόν | low | "’to the end’" given as the sense, but the note says the sense with ὦσε is a guess, and a bare adjective parse had an adverbial gloss | says the sense with ὦσε is uncertain; "all the way in" a guess |
| ἀπονόσφιν | low | no Attic equivalent named | "no Attic form; χωρίς, ἄπωθεν in sense"; "also ἀπὸ νόσφιν" |

## Pass 1 changes checked against gloss.json
ἤριπε (existing entry: "crash down … fell headlong") covers "crashed down"; μαζόν ("breast, nipple") and πιστὸν ("faithful, trusty") cover "breast" and "trusty"; βέλε ("missile, shaft, arrow") covers "shafts"; τρέσσε ("flee in fear, shrink back") covers "took fright" and the table's own 15.586 row; none needed broadening. ταρβήσειεν, ὀπάονά, φραζώμεθα, ἀγγελίης and μῆτιν did not agree and are corrected above.

## Findings considered and refused (pass 2)
1. 600 i "had hit" for ἔβαλε (aorist): the clause explains why the point is Polydamas', and the pluperfect English is the natural order of events; l keeps the aorist; left.
2. 624 i "for fear had fallen" for ἔμπεσε: same reasoning; left.
3. 586 and 587 "took fright" and "terrified" for two different verbs: the table fixes both words; left.
4. 612 l has "he came" (Coeranus) and then "he would have put" (Hector) with no name: the Greek has none, and the note says who; i names both; left.
5. ἀπονόσφιν "also prep. + gen.": not shown by this part, but it is an attested use and the entry keeps the form general; left.
6. ἀκηχέδατ "= Attic -ανται": the Attic perfect of this verb is not the same formation; the equivalence given is of the ending only, as the entry says; left.
