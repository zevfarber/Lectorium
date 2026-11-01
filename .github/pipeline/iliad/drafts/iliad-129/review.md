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

---

# Pass 2 (units.json re-read adversarially; gloss.json now checked against the lines)

`t` was not touched (all 57 `t` strings still match the packet's lines word for word; `l` has the same line count as `t` in every unit; no straight apostrophes; “ ” balanced except where a speech opens or closes, as it should be). Severity as in pass 1.

## Changes made

| # | line / form | field | severity | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 283 βέλος | l, i, n | major | The Iliad table fixes βέλος as "shaft" for arrows and spears (4.185, 5.18, 13.289 πέσοι βέλος "the shaft"); "missile" is kept only for thrown stones and general plurals (8.85, 12.159, 12.458, 16.737). Here βέλος is Achilles' spear, and the draft had "missile" in both layers and in the note. | l "near him the shaft was fixed"; i "the shaft had stuck fast"; note "βέλος ‘shaft’ is the spear". |
| 2 | 251 νεικεῖν; 253 νεικεῦσ’ | l, i, n (two units) | major | The table renders the present system of νεικέω as "rebuke" (1.521, 2.221–277, 12.268; the 12.268 row says "revile" is for the aorists); the draft had "revile" in `l`, `i` and both notes. | l "to rebuke, each other" / "rebuke one another"; i "rebuking each other" / "rebuke each other"; both notes say ‘rebuke’. (The 4.241 and 4.359 rows ship "revile" for the present system; the later 12.268 row is explicit and is followed.) |
| 3 | 277 λάκε | l, i, n | major | The table (13.616) fixes λάσκω as "cracked" (avoiding "crashed", "burst", "shrieked"); the draft had "rang", and the note called that a free choice. | l and i "the shield cracked under it"; note: whether it cracked or rang is not settled, ‘cracked’ is used as at 13.616. |
| 4 | 288 ἐπεσσύμενον | i | minor | The table's ἐπεσσύμενος row (12.388) has "rushed on" in `l` and "rushed at" in `i`; the draft had "rushed on" in both. | i "as he rushed at him". `l` keeps "as he rushed on". |
| 5 | 221 ἀταλῇσι | n | minor | ἀταλῇσι is feminine and the note said it "goes with πώλοισιν" without saying that this makes πώλοισιν feminine (fillies); the gloss had called πώλοισιν "masc." | Note adds that ἀταλῇσι is feminine and πώλοισιν is read as feminine here. |
| 6 | gloss δειδίξεσθαι | gloss | major | Entry said "aor. inf. mid. (in form also fut.)". The aorist infinitive is δειδίξασθαι; δειδίξεσθαι is the future infinitive (as the unit note at 200 says, and as ἔλπομαι takes). | "fut. inf. mid. (not the aor. inf. δειδίξασθαι), after ἔλπεο". |
| 7 | gloss ἄροιτο (`__broaden__`) | gloss | major | Known entry is ἄρνυμαι "win, gain"; at 247 ἄροιτο is from αἴρω/ἀείρω ("could bear the load", as the unit note says), so the known entry gives the wrong word. | Old entry whole + " · also αἴρω (ἀείρω) — lift, bear; aor. opt. 3 sg. mid., potential with ἄν: ’could bear’ (ἄχθος ἄροιτο …)". |
| 8 | gloss ἁλοσύδνης | gloss | minor | Entry contained "here" (barred by the entry format). | "used as an epithet of Thetis". |
| 9 | gloss καλλιπλοκάμου | gloss | minor | "fair-tressed" is reserved by the table for ἐυπλοκαμῖδες (the house word is "fair-plaited", which the unit uses); "epic -ου" is wrong, since -ου is the ordinary genitive. | "fair-plaited (… ’plait, lock of hair’); adj. of two endings, fem. gen. sg." |
| 10 | gloss νεικεῖν, νεικεῦσ’ | gloss | minor | Quoted English ‘to revile’ / ‘they revile’ contradicted the corrected units (row 2). | ‘to rebuke’ / ‘they rebuke’. |
| 11 | gloss ἀνηρείψαντο | gloss | nit | "snatch up and carry away" disagrees with the units ("snatch away", ‘carried off’; Od. 20.77). | "snatch away, carry off". |
| 12 | gloss φίλατο | gloss | nit | "root aorist" is the wrong term (φίλατο is a sigmaless aorist in -ατο, not like ἔβην). | "sigmaless and unaugmented". |
| 13 | gloss πώλοισιν, πώλους | gloss | nit | Gender given as masc. only; ἀταλῇσι (221) makes the dative feminine. | "masc./fem." in both. |
| 14 | gloss πτύχας (`__broaden__`) | gloss | minor | Known entry "layer (of hide)" does not cover the metal layers of the shield (269–270). | Old entry whole + " · also a layer of metal in a shield: ’layers’ (πέντε πτύχας ’five layers’)". |
| 15 | gloss σμερδαλέῳ (`__broaden__`) | gloss | minor | Known entry "masc. dat. sg., agreeing with χαλκῷ"; at 259 it agrees with neuter σάκει. | Old entry whole + " · also neut. dat. sg., agreeing with σάκει: ’frightful’". |
| 16 | gloss κ’ (`__broaden__`) | gloss | nit | Known κ’ entry has no κ’ + subjunctive in a general relative clause, which is εἴπῃσθα at 250 (the κ’ + opt. use is covered). | Old entry whole + " · also κ’ + subj. in a general relative clause: ’whatever’ (…)". |

Counts: major 5 (rows 1, 2, 3, 6, 7); minor 7 (4, 5, 8, 9, 10, 14, 15); nit 4 (11, 12, 13, 16). Total 16 rows: units.json 5 rows (1–5; 14 unit fields across 8 units), gloss.json 11 rows (6–16). `t` untouched.

## Checked and found correct in pass 2 (no change)

- All 16 pass-1 changes re-verified against the line; the 208 metre sentence stands (15 syllables, spondaic fifth foot only with Ἀγχίσαο lengthened).
- Every parse of the 97 new entries in gloss.json against its line(s), including: ἔλπεο, γευσόμεθ’, εἴπῃσθα, θέεσκον, κατέκλων, κτίσσε, πεπόλιστο, σκιρτῷεν, ἠράσσατο, ἐπέην, ἐπακούσαις, ἔχθηρε, ἰοῦσαι, ἴδες, ἴσασι, ὑποείκειν, ἐτεά (neut. acc. pl., 255), χαλκείας (acc. pl. with πτύχας understood), κεχαρισμένα, μόριμον, ἄσπερμος/ἄφαντος, the proper names and their case.
- All 19 original `__broaden__` entries (23 now, with rows 7, 14, 15, 16): the old entry is whole in front of " · " in every one, and each new reading is true of the form as used (αἵματος 241, βροτῶν 248, γένωνται 308, γυναικῶν 305, δάρδανος 219, μή 301, μετείη 235, νώτου 279, πέρ 300, πρώτην 275, τάων 223, ἀνέσχε 278, ἀχέων 298, ἐθέλῃσιν 243, ἕθεν 305, ἕλε 280, ἤλασε 270, ὕπο 275, ῥινὸς 276). Their length over 230 comes from the old entries and is not a defect; no line numbers, no straight quotes.
- The 449 known-form entries were each read against their uses in the part; apart from rows 7, 14, 15, 16 they cover the use (αὐτῆς already has ὑπ’ αὐτῆς "under it"; κεν has the past-unreal ἔνθά κεν; μή has εἰ μὴ + aor. indic.; ἔσχετο has both "held" and "was checked"; ἕλος is the marsh).
- Table conformity re-checked from conventions.md: ἀμφιβρότης, ἐΐσην, δεινός "dread", ὄβριμον "mighty", χαλκήρης "bronze-fitted", ἀκωκή "tip", παχείῃ "stout", θυμοβόρος "heart-devouring", χερμάδιον "rock", σμερδαλέα ἰάχων, παρελέξατο, εἰσάμενος, ἐρύκακε, ἀναίτιος, ἄφαντος "unseen", θᾶσσον (`l` "more quickly", `i` "quickly"), ἀφνειός "rich", κάρτιστος "strongest", ἑκάτοιο, ἀτάλαντος not involved, ἄϊδος δέ as pass 1.
- Quotation marks and `mark`/`p` fields re-checked: “ at 200 and 293, ” at 257 and 307, narration at 259 onward and 199.

## Findings considered and refused in pass 2

1. **ἔλπεο "hope" (200).** The table keeps "hope" for a good outcome (1.545, 9.40 note); Achilles hoping to frighten Aeneas is hope from his side, so "hope" stands. No change.
2. **ὅππως (243) known entry "introducing an indirect question".** The κεν entry already has "ὅππως κεν + subj., in an indirect question: ’how … may’" and the ἐθέλῃσιν broaden covers the sense "in whatever way he wishes". No further broadening.
3. **ὑποείκειν "both go with ἀνδράσι θνητοῖσι" (264).** The dative is the person for whom the gifts are (not) easy; this is the note's loose way of saying so and the English is sound. No change.
4. **οἷο "possessive ὅς" (known entry) against the note's "reflexive genitive" (234).** Both describe the same form (οἷο = ἑοῖο, "his own"); no change.
5. **ῥηγμῖνος `i` "breaking surf" (228).** A departure from the 2.773 row already accepted in pass 1 and recorded in new-renderings.md.
6. **ἔτεκον entry "augmented (= Attic ἔτεκον)".** Redundant but not false; left.
7. **Gloss quotes ‘rings’ (κύκλους entry, ἕλε broaden example) while the units say "circles".** The gloss quotes are glosses of the Greek, not the house rendering, and the κύκλους entry is an existing one that may not be rewritten.

## For the caller (new-renderings.md, which the reviewer does not edit)

Add or correct rows: νεικεῖν / νεικεῦσ’ (20.251, 20.253): "rebuke" in both layers, following the present-system rows; λάκε (20.277): "cracked", following 13.616; βέλος (20.283, of a spear): "shaft", following 4.185 / 13.289. The row for ἀνηρείψαντο, πτύχας and ἄχος … μυρίον still need the pass-1 corrections. The μάψ decision from pass 1 is still open.
