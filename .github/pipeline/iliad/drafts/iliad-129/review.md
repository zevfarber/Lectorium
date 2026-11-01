# iliad-129 (20.199–308) — review, pass 1 (units only; gloss.json does not exist yet)

Severity: **major** = wrong against the house table or a false grammatical label that would mislead the glosser or reader; **minor** = incomplete or loose note, small inconsistency; **nit** = wording.
`t` was not touched (checked: all 57 `t` strings are byte-identical before and after, and match the packet's lines).

## Changes made

| # | line | field | severity | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 208 | n | minor | The packet flags 208; the note said nothing of its metre. Hand scan: αὐ-τὰρ-ἐ / γὼν-υἱ / ὸς-με-γα / λή-το-ρος / Ἀγ-χί / σα-ο. There are 15 syllables and no regular parse: the fifth foot can only be a spondee if the short ι of Ἀγχίσαο counts long, and the last foot only if the short -σα- counts long. The scanner's result agrees (UNRESOLVED, spondaic fifth, lengthening of Ἀγχίσαο). The irregularity is real. | Added one sentence: "Line 208 is metrically irregular as transmitted: Ἀγχίσαο fills the last two feet only if its short ι and its short -σα- are both counted long, which gives a spondee in the fifth foot." |
| 2 | 210 | n | nit | "will be in mourning by evening" adds a time the Greek does not give (only σήμερον). | "before the day is out". |
| 3 | 215 | l, i | major | πολυπίδακος Ἴδης: the table's 14.157 row (a stock epithet of Ida, "likely to recur") fixes "many-springed" in both layers; the draft had "many-fountained" / "Ida of many springs" (the 8.47 wording). | l "many-springed Ida"; i "many-springed Ida". |
| 4 | 221 | n | nit | Note glossed βουκολέοντο as "grazed" while `l` says "were pastured". | "so ‘were pastured’". |
| 5 | 226 | n | minor | The note never explained καρπόν, which `l` renders ("the fruit of the ears"). | Added "ἀνθερίκων καρπόν is ‘the fruit of the ἀνθέρικες’" and that "the ears" is the English for it. |
| 6 | 234 | l, i, n | major | ἀνηρείψαντο: the Odyssey table (20.77, shipped at odyssey-020) gives `l` "snatched away", `i` "carried off", and new-renderings.md wrongly says "carried off" is reserved for another verb. The draft had "snatched up" in both layers. | l "snatched away"; i "carried him off"; note "‘snatch away’". (new-renderings.md row for ἀνηρείψαντο must be corrected by the caller.) |
| 7 | 237 | n | minor | "the five sons are in the accusative, each with τε": Τιθωνόν has no τε. | "the last four each with τε". |
| 8 | 260 | n | minor | "ἀμφί takes the dative δουρὸς ἀκωκῇ" stated as fact; in the line ἀμφί stands before σάκος and may be a bare adverb with the dative as cause. | Note now gives both readings and says which the English takes. |
| 9 | 262 | n | minor | "the sentence runs six lines": the sentence is 262–266, five lines (261 ends at the ano teleia). | "five lines". |
| 10 | 267 | l, n | major | δαΐφρων: the table's rows (4.252, 5.277, 5.813) fix `l` "wise-minded" and `i` "wise-hearted". The draft had "wise-hearted" in `l`, and the note said "wise-hearted is followed". | l "wise-minded Aeneas"; note says "wise-minded" in the literal English and "wise-hearted" in the free English. |
| 11 | 269 | i | major | πτύχες of a shield: the table's 18.481 row gives `l` "folds", `i` "layers". The draft had "folds" in `i` (new-renderings.md calls "layers" avoided, which contradicts the table). | i "two of the layers", "five layers"; `l` keeps "folds". |
| 12 | 273 | l, n | major | Note said "the person hit is in the genitive, the thing in the accusative". False: Αἰνείαο is the possessive genitive with ἀσπίδα. `l` "struck Aeneas on the shield" followed the false label. | Note rewritten (possessive genitive; κατά + acc. "on"); l "and struck, on the shield of Aeneas, equal on every side,". `i` ("struck Aeneas on his shield") left, since it is a fair free rendering. |
| 13 | 281 | l, i, n | major | μυρίον: the table's 18.88 row (πένθος μυρίον) gives "countless grief" in both layers; the draft had "vast". new-renderings.md says "countless" is kept for plurals only, which the table does not say. | l "countless", i "countless grief", note "‘countless’". (new-renderings.md row to be corrected or dropped.) |
| 14 | 281 | n | minor | χύτο called "aorist passive"; it is the (unaugmented) aorist middle of χέω. | "aorist middle". |
| 15 | 293 | n | major | Ἄϊδος δὲ κάτεισι: δέ was not accounted for, and "Ἄϊδος names the place" leaves it a stray particle. The house treatment (iliad-044 (7.329–330) and iliad-107) is: genitive Ἄϊδος plus the ending -δε "to", printed apart. | Note: "Ἄϊδος δέ, printed as two words, is the genitive Ἄϊδος with the ending -δε ‘to’ (‘to the house of Hades’), and κάτεισι is the future of κάτειμι ‘go down’." `l`/`i` ("to Hades will go down" / "go down to Hades") already agree. |
| 16 | about | about | minor | "tears through the rims of Aeneas’ shield" uses the word new-renderings.md rejects for κύκλους; "five metal folds" now disagrees with `i`. | "circles"; "five metal layers". |

Counts: 7 major (rows 3, 6, 10, 11, 12, 13, 15), 7 minor (1, 5, 7, 8, 9, 14, 16), 2 nit (2, 4). Total 16 rows, 21 unit fields plus `about`.

## Checked and found correct (no change)

- Every cross-reference: 6.150 and 6.211 (iliad-037, units at ln 150 and 211: Glaucus's lines, correct), 13.292 (iliad-080, ln 292), 3.147 (iliad-017, unit at ln 146 contains 147 Λάμπον … ὄζον Ἄρηος), 5.302–304 and 5.304 (iliad-029, ln 302: the rock; ὃ δέ μιν ῥέα πάλλε καὶ οἶος is the second half of 5.304), Odyssey Cleitus lines (odyssey-073, ln 250 = Od. 15.250–251), and the internal ones (220/233, 236–240).
- Reused English: 20.213 (whole-unit `l`/`i` identical to iliad-037), 20.238, 20.241, 20.244, 20.285–287 (match iliad-029 with Aeneas for Tydeus’-son), 20.257 θᾶσσον (iliad-122), 20.283 σμερδαλέα ἰάχων (iliad-029/-049), 20.291 ὀξὺ νόησε (iliad-020/-029/-033/-046/-047), 20.199 (Odyssey Alcinous formula), 20.292 (iliad-019/-057/-128).
- Quotation marks: “ on 200 (mark "Aeneas answers") and on 293 (mark "Poseidon speaks"); ” on 257 and 307. iliad-128's last unit closes Achilles' speech with ”, so 199 is narration. No ” leaked into the 241 unit (the packet's iliad-037 version has one because the speech ends there; here it goes on). Paragraph flags `p` at 199, 259, 273 are right.
- Grammar labels verified against the line, including: ἔλπεο (imperative), δειδίξεσθαι (future infinitive), ἴδμεν, ἐκγεγάμεν, ἐξαπονέεσθαι (present infinitive, future sense), δαήμεναι, κτίσσε (unaugmented), πεπόλιστο, εἰσάμενος, ἠράσσατο + genitive, σκιρτῷεν (iterative optative), θέεσκον, ἄνδρεσσιν, ὅππως, ὁ as demonstrative at 243, ἄροιτο (potential optative), εἴπῃσθα, ἐπακούσαις, νεικεῦσι, ἰοῦσαι, γευσόμεθ’, ἐρύκακε, ἐπέην, ἤϊξεν, λάκε, ἐάλη, ἱεμένη, ἀλευάμενος, πάγη, ὅ = ὅτι at 283, ἐπεσσύμενον, ἀπηύρα, κεχολώσεται (future perfect), ὄληται, φίλατο, ἕθεν = Zeus, ἔχθηρε, ἀνάξει.
- Greek → `l` → `i` for all 57 units; `l` has the same line count as `t` in every unit; no straight apostrophes; `ln` is right for every unit (units that open mid-line carry that line's number).
- Table conformity: νεφεληγερέτα Ζεύς, μεγαλήτωρ "great-spirited", ἀμύμων, ἀντίθεος "godlike", δολιχόσκιον "long-shadowed", κυλλοποδίων ("the crook-footed one" / "the crook-footed god"), μερόπων, ἑκάτοιο, ὄζον Ἄρηος, ἀμφιβρότης, ἐΐσην, ζείδωρος "grain-giving", ἀρετή "excellence", ὀφέλλω "increase", μινύθω "lessens", στρεπτός "turnable", κυανοχαίτης "dark-haired", τίκτω "begot"/"bore", ἀναίτιος "blameless", κεχαρισμένα "pleasing", ἄφαντος "unseen", Ἄρηος, ἦ ῥα καί "He spoke, and" / "So he said, and", ὢ πόποι "Ah", Κρονίδης "son-of-Cronus", ἄντυξ "rim", ἀσπίδος "shield". Ἁλοσύδνη kept as a name as in the Odyssey. The ῥηγμῖνος departure ("surf" in `i`) is recorded and reasoned in new-renderings.md and is accepted.
- Line 244 note: "Line 244 stands also at 13.292" is correct.

## Findings considered and refused

1. **μὰψ at 298 ("to no purpose" / "in vain").** The table's later rows (13.627, 15.40, and 5.876's note) fix μάψ as "recklessly", but iliad-008 shipped "in vain"/"to no purpose" for it, and "recklessly" with "suffers pains" would say that Aeneas is reckless, which the Greek does not mean. Left unchanged and escalated to the caller: either keep it and record it in new-renderings.md as a departure, or change both layers to "recklessly".
2. **`i` of 215 drops αὖ "in turn".** `l` carries it and the free layer may drop a light particle; no change.
3. **"The colon opens his reply" (199) and "the colon opens his speech" (292).** The Greek mark is the ano teleia; the colon is the English. The sense is clear enough; no change.
4. **ἔνι "is ἔνεστι" at 248 with a plural subject.** ἔνι stands for both ἔνεστι and ἔνεισι; the gloss is true as written.
5. **γευσόμεθ’ "subjunctive of exhortation" at 257.** A short-vowel aorist subjunctive is the standard reading; the future-indicative alternative gives the same English; no change.
6. **`i` of 288 "had Poseidon earth-shaker not been quick to notice" after "with his sword at close quarters,".** Follows the table's 5.680 row exactly; no change.
7. **Dropping "even" from `l` at 246 (οὐδ’ ἂν … "and not").** `i` has "not even"; `l` is the literal layer and οὐδέ = "and not" is within it.
8. **`i` of 262–266 "nor made to give way" for ὑποείκειν.** The infinitive is active, but with δαμήμεναι under "for mortal men" the free English is sound; no change.
9. **`about` calls the shield layers "metal"; the gold, bronze and tin are metal.** True; kept.

## For the caller (new-renderings.md, which the reviewer does not edit)

Rows to correct before the table is updated: ἀνηρείψαντο (now "snatched away" / "carried off", following Od. 20.77), πτύχας (now "folds" in `l`, "layers" in `i`, following 18.481), ἄχος … μυρίον (now "countless" in both layers), and a new row for πολυπίδακος Ἴδης ("many-springed", following 14.157) is unnecessary because it follows the table unchanged. Decision needed on μάψ (refused finding 1).
