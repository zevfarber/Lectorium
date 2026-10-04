# review-074 — adversarial review of odyssey-074 (Odyssey 15.260–350), pass 1 of 2

`t` untouched (asserted equal unit by unit to the pre-review copy; the 56 `t` values joined still reproduce packet lines 260–350 exactly). The file has no `tr` or `sc`; none added. Edits applied by one script (asserted substring replacement, `ensure_ascii=False, indent=1`; the file round-trips byte for byte before editing). 24 changes (2 high, 10 medium, 12 low) touching 33 fields in 22 units and the `about`. `new-renderings.md` updated (rows 15.264, ὕβρις changed; ἀγγελίη, Ἐπειοί, ἐρίζω added).

Mechanical checks run: l and `t` have the same number of lines in every unit and `i` has none; quotation marks “ on units 260, 266, 272, 280, 307, 326, 341 and ” on 264b, 269, 278b, 281, 321, 337, 347 only, each in both layers; `mark` only on those seven first units (260 Theoclymenus speaks, 266 Telemachus answers, 272 Theoclymenus answers, 280 Telemachus answers, 307 Odysseus speaks, 326 Eumaeus answers, 341 Odysseus answers); `p` on 260, 271, 279, 282, 296, 301, 307, 325, 340 (Murray's nine paragraphs) and nowhere else; the last unit of /home/user/Lectorium/odyssey-073.json carries no quotation mark and says the opening mark of Theoclymenus's speech is printed here, as 260 does. Every unit whose `t` is identical (diaeresis and punctuation ignored) to a shipped unit in odyssey-001…073 has `l` and `i` identical to it apart from the quotation marks: that check found four whole-unit repeats the packet does not list (264a, 264b, 266 beyond the three listed, 296 beyond the one listed; see below), and all now agree. Scansion: the packet flagged no line, so none was scanned by hand.

## Changes

| line | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| about | about | high | "Theoclymenus, whom Telemachus has found at the ship": reversed. In the last unit of 073 Theoclymenus comes up and finds Telemachus (ἐκίχανεν); the note at 15.260 itself says Theoclymenus "came up to Telemachus". | "Theoclymenus, who has come up to Telemachus at the ship, asks him who he is and begs…". |
| 15.328–329 | l, i, n | high | ὕβρις rendered "outrage" and the drafter's new-renderings row said "insolence" was reserved for other words. The shipped renderings of the same noun are "insolence" in both layers every time (1.368 odyssey-004, 4.321 odyssey-016, 4.627 odyssey-019, 14.262 odyssey-068), and the table's ὑπερβασίη row says "insolence"/"arrogance" are reserved for ὕβρις and its family; "outrage" is the shipped `i` of the different noun ὑπερβασίη (3.206). | "whose both insolence and violence the iron heaven reaches." / "whose insolence and violence reach the iron sky." Note now says 'insolence' and 'violence'. Row in new-renderings.md rewritten (answers the drafter's open point 7). |
| 15.264b | l | medium | πόθι τοι πόλις ἠδὲ τοκῆες; is a whole unit shipped three times (002 line 170, 048 line 325, 067 line 187) with `l` "Where is your city and your parents?"; the draft had "Where is your city, and where your parents?" and a new-renderings row defending it. The packet missed it because Murray's line holds two units. | `l` restored to the shipped wording; the new-renderings row corrected to say so. `i` already agreed. |
| 15.296 | l, i | medium | The unit ended with a semicolon in both layers. The identical unit δύσετό τ’ ἠέλιος σκιόωντό τε πᾶσαι ἀγυιαί· is shipped at 013 line 497, 051 line 12 and 073 line 185 (the last with the same ano teleia) with a full stop in both layers; the packet listed only the three-line unit at 008. The drafter's open point 14 reasoned from the 3.497 row, but 073 shows how the ano teleia is rendered for this exact unit. | Full stops: "And the sun set, and all the streets grew shadowy." / "The sun set, and all the streets grew dark." |
| 15.298 | l, i, n | medium | "the Epeians hold sway": the same half-line ὅθι κρατέουσιν Ἐπειοί is shipped at 13.274 (odyssey-064) as "where the Epeans hold sway" in both layers. | "Epeans" in both layers and in the note; row added to new-renderings.md. |
| 15.321 | i | medium | "no other mortal could rival me in service, whether in building up a fire … in carving … in all the things": "whether" opens no alternative. | "…in service, at building up a fire well and splitting dry logs, at carving and roasting and pouring wine, at all the things that lesser men do for their betters." |
| 15.260–261 | l, i, n | medium | δαίμονος given as "the power". The table's δαίμων row (an unnamed divine power) is `l` "a power", `i` "some power", as shipped at 7.248 (odyssey-032) and 11.61 (odyssey-051); the Greek has no article, and "some power" suits a god Theoclymenus does not know. | `l` "by a power", `i` "by some power"; note says "by a power (δαίμονος, the divine power to whom the sacrifices are made, left unnamed)". Drafter's open point 12 refused as written. |
| 15.273 (unit 9) | n | medium | "φεύγω in 276 completes the thought": φεύγω is the verb of the next sentence, not the missing verb of 272–273; the note also contradicted its own `i`, which supplies "I am away". | Now: "the English supplies 'I am away', and the verb φεύγω does not come until 276, in the next sentence." |
| 15.285 | n | medium | οἷ called "the dative of ὅς reflexive": οἷ is the third-person pronoun (οὗ, οἷ, ἕ), not the possessive/relative ὅς. | "the dative of the third-person pronoun, here reflexive". |
| 15.287 | n | medium | ἑτάροισιν said to be the dative object of ἐκέλευσεν; the dative belongs with ἐποτρύνας, and the infinitive after ἐκέλευσεν takes the same men as understood object. | Rewritten to say that. |
| 15.307 | n | medium | κέκλυθι called "the old perfect imperative": it is the reduplicated aorist imperative of κλύω. | Label corrected. |
| 15.337 | n | medium | "ἔλθῃσιν (-ῃσιν as in ἵκηται elsewhere)": ἵκηται is a middle ending, not -ῃσιν; false comparison. | "a third singular with the old ending -ῃσιν". |
| 15.286b | l, i | low | τοὶ δὲ πρυμνήσι’ ἔλυσαν is a half-line shipped at 008 line 418 ("And they loosed the stern-cables," / "And they cast off the stern-cables,"); the draft reordered `l` and chose "loosed" in `i`. | Shipped wording reused: "and they loosed the stern-cables." / "and they cast off the stern-cables." |
| 15.314 | l, i, n | low | ἀγγελίην rendered "message"; shipped for ἀγγελίη is "news" (4.408, 5.30, 5.42, 14.244), and the draft's own `about` says "carry news". | "tell news to circumspect Penelope" / "bring news to circumspect Penelope"; note 'news, tidings'; row added. |
| 15.321 | l | low | "could contend": the shipped `l` and `i` for ἐρίσσεται at 14.80 are "rival me". | "in service could not rival me another mortal,"; row added. |
| 15.311 | i | low | "I myself must roam … by necessity": "must" and "by necessity" say ἀνάγκῃ twice. | "I myself will roam through the city out of necessity, in case…". |
| 15.267 | n | low | "an Homeric imperfect". | "a Homeric". |
| 15.275 | n | low | ὑπαλέομαι: the aorist participle ὑπαλευάμενος belongs to ἀλεύομαι (aor. ἀλευάμην), so the lemma is ὑπαλεύομαι. | Lemma corrected. |
| 15.281 | n | low | φιλήσεαι "a future passive": the passive future is φιληθήσομαι; this is the future middle used with passive sense. | "a future middle of φιλέω with passive sense". |
| 15.274 | n | low | "ἱππόβοτος … is Argos's standing epithet": makes a claim about the poem this part cannot show (the word stands once here). | "is the epithet of Argos here". |
| 15.284 | n | low | ποντοπόροιο "the ship's standing epithet": same overreach. | "the epithet of the ship here". |
| 15.295 | n | low | καλλιρέεθρον "a standing epithet of Chalcis": same overreach. | "the epithet of Chalcis here". |
| 15.319 | n | low | διάκτορος "found only as a title of Hermes": same overreach. | "here a title of Hermes". |
| 15.318 | n | low | "The colon is the Greek ano teleia": confuses the English mark with the Greek one. | "The unit ends at the Greek ano teleia, shown as a colon in English…". |

## Findings considered and refused

- **Open point 2, "favorable"/"favoring" in 15.292–294.** The repeated line τοῖσιν δ’ ἴκμενον οὖρον ἵει γλαυκῶπις Ἀθήνη is shipped at 008 line 420 with American spelling; a repeated line keeps its shipped English and the table's own row (11.7) is only a different word-order. Left as shipped; the spelling split between the table ("favouring") and the shipped parts is for the owner.
- **Open point 13, κεφαλή "by your own head" (15.262).** Row 1331 wants a person-naming `i` where "head" alone reads as a body part ("such a man"); here "by your own head" is an English oath-form and keeps the image, as ἕρκος ὀδόντων does. The note says the head stands for the person.
- **Open point 5, 15.335a ἀλλὰ μέν’· as a two-word unit.** The convention ends a unit at the ano teleia; the drafter's alternative would not honour the Greek punctuation. Kept.
- **Open point 4, four-line units (303–306, 313–316, 321–324) and the cuts after 320 and 346.** All within the four-line allowance; the cut after 320 (period would run six lines) and after 346 (five lines) fall at the syntactic pauses. Kept.
- **Open point 6, ἡγεμών "a good leader" (15.310).** Agrees with the reasoning (διάκτορος "the guide" nine lines later); row kept.
- **Open point 8 ἰσχανάᾳς and open point 9 ἐπαιγίζοντα / ἴκμενον.** The notes say the sense is uncertain and give the alternative; the renderings are the ordinary traditional guesses. Kept.
- **Open point 10, οὕτω τοι καὶ ἐγών (15.272).** Verbless `l`, supplied verb in `i`, other reading ("likewise") named by the drafter; the note states the verb is missing. Kept.
- **Open point 11, "his" in `i` at 15.273.** Stated in the note; the sense (the dead man's kin) is the only one the context allows. Kept.
- **Open point 14.** Refused as written (see 15.296 above).
- **15.333 σίτου καὶ κρειῶν "food and meat".** The half-line σίτου καὶ κρειῶν is shipped at 9.8 (odyssey-039) as "bread and meats", while the table's σῖτος row says "food" and avoids "bread". The verb differs, so it is not a repeated line; the table row governs. Flagged for the owner as a standing inconsistency, not changed.
- **15.276 νύ "indeed" in `l`, "now" in `i`.** Both are ordinary senses of the enclitic; kept.
- **15.275 `l` "black death-fate" against the note's "death-spirit".** The table uses both for κήρ (ἔκφυγε κῆρα, κὴρ θανάτοιο); the note names the sense, `l` and `i` follow the two table rows. Kept.
- **15.343 `i` "nothing worse for mortals than roaming" as remembered English.** The structure is forced by οὐκ ἔστι κακώτερον ἄλλο and "roaming" is the table's word for πλαγκτοσύνη; rebuilt from the case relations it comes out the same. Kept.
- **15.264a note on εἶς / εἰς.** The edition prints εἶς; the note is clumsy but not false. Kept.
- **Glossary.** `known-forms.json` and `novel-forms.json` are outside this pass; the form ὑπαλευάμενος in the novel list is unchanged by the lemma correction in the note.
- Title Φυγὰς καὶ πτωχός ("Exile and Beggar"), English name, `v`, `ln` of every unit, and the placement of all mid-line cuts (273, 278, 281, 286, 288, 302, 311, 327, 333, 335) checked and kept.

# Pass 2 of 2 (fresh adversarial pass, including gloss.json)

Order followed: note labels, claims and cross-references; Greek to `l` word by word; `l` against `i`; remembered English in `i`; quotation marks (last unit of /home/user/Lectorium/odyssey-073.json checked again: no mark, and it says the opening mark of Theoclymenus's speech is printed in this part, as 260 does); house renderings and repeated lines against the packet and against every shipped part odyssey-001…073 (by a run-matching script, not by the packet: every unit and every half-line of three or more words shared with a shipped unit was listed and compared); pass 1's 24 changes re-read for new errors (none found; the 15.296 full stops, "Epeans", "news", "rival", ὕβρις "insolence", and the 264b `l` all agree with the shipped parts). `t` untouched (asserted unit by unit against the pre-pass copy; the units' `t` joined, whitespace-normalised, still equal packet lines 260–350). No `tr`/`sc` in the file. Edits applied by script (asserted single-occurrence replacement, `ensure_ascii=False, indent=1`). 26 changes in all: 0 high, 6 medium, 20 low (10 rows in units.json touching 11 fields, 16 forms in gloss.json; see tables). Whole-unit repeats (264a, 264b, 265, 266, 279, 287–288a, 296, 341 pair) re-verified identical to the shipped `l` and `i` apart from the opening/closing quotation mark. `new-renderings.md` updated (15.325 row).

## Changes: units.json

| line | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| 15.260 | l | medium | κιχάνω is "come upon" in `l` wherever shipped (064 line 228, the same half-line ὦ φίλ’, ἐπεί σε … κιχάνω τῷδ’ ἐνὶ χώρῳ: "since you first I come upon in this place"; 073 ἐκίχανεν "came upon"); the draft had "find you" in `l`. | "since sacrificing I come upon you in this place". `i` keeps "find" as in 064. |
| 15.347–350 | l, i | medium | "in the halls of Hades" for εἰν Ἀΐδαο δόμοισι; the same half-line is shipped at 021 (line 831, "in the house of Hades" in both layers) and 053 (line 210, "Hades’ (house)"). | "in the house of Hades" in both layers. |
| 15.282 | l | low | ἐδέξατο is "received" in `l` in every shipped part (002 line 120 for this very phrase ἐδέξατο χάλκεον ἔγχος, 026, 037, 067, 072); the draft had "took". | "from him he received the bronze spear". `i` ("took … from him") kept, as in 067 and 072. |
| 15.325 | l | low | The speech-introduction was built from the shipped τὸν δὲ μέγ’ ὀχθήσας προσέφη (014 line 30, 017 line 332: "Him then, greatly vexed, addressed …"), but opened "And him". | "Him then, greatly vexed, you addressed, Eumaeus the swineherd:"; row in new-renderings.md changed. |
| 15.326 | i | low | νόημα in the half-line ἐνὶ φρεσὶ τοῦτο νόημα ἔπλετο is "notion" in the shipped `i` (008 line 363). | "why has this notion come into your mind?" |
| 15.333 | l | low | σίτου καὶ κρειῶν is "food and meats" in the shipped `l` (039 line 7, 070 line 454); the draft had "meat". `i` ("food and meat", as 070) kept. | "with food and meats and wine are weighed down." |
| 15.269 | l | low | πευσόμενος πατρὸς δὴν οἰχομένοιο is "to learn of … father, long gone" at 003 line 280. | "to learn of my father, long gone." |
| 15.272 (unit 9) | n | low | "κατακτάς … in its epic form (Attic κατακτείνας)": the form is the short-stem (athematic) aorist participle, and the gloss says κατακτανών; the note and gloss disagreed. | "the short-stem aorist participle of κατακτείνω 'kill' (the Attic equivalent is κατακτανών)". |
| 15.329 | n | low | The explanation said "outrage" after pass 1 had made both layers "insolence". | "insolence and violence". |
| 15.331 | n | low | λιπαρός glossed "sleek, glossy": "glossy" is on the table's avoided list for this word. | "'sleek' (as if rubbed with oil)". |

## Changes: gloss.json

| form | sev | what was wrong | what I did |
|---|---|---|---|
| δρηστοσύνῃ | medium | "Ionic η (= Attic -α)": false; nouns in -σύνη keep η in Attic. | removed the claim. |
| πλαγκτοσύνης | medium | "Ionic η" for the same reason. | removed. |
| κοτύλην | medium | "Ionic η (= Attic -α)": Attic κοτύλη has η after λ. | removed. |
| ἄλη | medium | "Ionic η": Attic ἄλη has η after λ. | removed. |
| __broaden__ τῶν | low | The known entry has "of them", article-like and distributive uses only; 15.329 (τῶν ὕβρις τε βίη τε … ἵκει) is relative "of whom, whose", which the note itself says. | broadened: old entry whole + " · also relative ὅς, ἥ, ὅ: gen. pl. ’of whom, whose’ (…)". |
| __broaden__ ὑπὲρ | low | the new reading's gloss was "by the sacrifices and the god", against `l` "by a power". | ’by the sacrifices and a power’. |
| __broaden__ ἀγαθοῖσι | low | "the good (masters)": nothing in the line says masters. | "(men of rank)", as the note. |
| __broaden__ μοι | low | the example quoted ’who are mine’ and glossed it ’who are with me’. | ’who are mine’. |
| ἀνιᾶται | low | quoted ’is vexed’; "vexed" is kept for ὀχθέω, the unit has "distressed". | ’is distressed’. |
| κατατρύχω | low | quoted ’so that I not wear out’ (not English). | ’so that I may not wear out’. |
| ἐπαιγίζοντα, δανὰ | low | the notes say the sense is uncertain; the entries did not. | "(sense uncertain)" added. |
| ὄπασσον, τάνυσεν, βοεῦσι | low | ὄπασσον had no Attic equivalent; τάνυσεν missed "unaugmented"; βοεῦσι gave "(= Attic βοεῦσι)", the same form (the shipped βοεῦσιν entry has none). | "(= Attic ὄπασον)"; "epic, unaugmented"; equivalent removed. |

Every one of the 88 new entries and 17 broadened entries was read against each line where the form stands (parse, case, agreement, the sense used in the line); entries not named above are right. The 17 `__broaden__` entries each begin with the shipped entry whole (checked against odyssey-glossary.json itself, not only known-forms.json); the new entries are all under 230 characters with typographic ’ only, no line numbers, no "here". The known forms were also checked against their uses here (about 300 forms): the only use not covered was τῶν (above).

## Findings considered and refused

- **15.275 κῆρα μέλαιναν.** The same half-line θάνατον καὶ κῆρα μέλαιναν is shipped at 007 (line 283) and 011 (line 241) as "death and black doom" in both layers, while 058 line 156 has "death and the death-spirit". The table's own rows (κὴρ θανάτοιο, "doom" reserved for πότμος; ἔκφυγε κῆρα "escaped death-fate") were written after 007 and 011 and govern the later parts; the draft follows them ("black death-fate" / "the black spirit of death"). Left; the shipped parts 007 and 011 are the ones out of line, for the owner.
- **15.288 ἐσσυμένως "eagerly".** Shipped `l` elsewhere is "hurriedly" / "hastily" (039, 069); the known glossary entry reads "hastily, eagerly" and "eagerly" is a sense of the participle (cf. ἐσσύμενον "eager", 017). Kept.
- **15.281 φιλήσεαι "welcomed".** Shipped 002 line 123 has "befriended"/"treated as a friend" for the same form, but the table row for φιλέω of a host is "welcomes" and φιλέοι 15.305 is the same verb; the contexts differ (a promise of entertainment, not a greeting). Kept.
- **15.317 σφίσιν "among them".** The broadened entry says "not reflexive"; the suitors are also the subject of ἐθέλοιεν, so a reflexive reading is possible; the rendering is the same either way. Kept.
- **15.272 τοι "you see".** The note takes τοι as the particle; the known entry says the two are not easy to keep apart; the rendering "you see" is harmless. Kept.
- **15.280 ἐΐσης note "it means 'even, equal'".** Slightly self-contradictory beside "sense not certain", but not false (the root sense is stated, the application to a ship is what is uncertain). Kept.
- **15.267 note "the next unit goes further" / εἴ ποτ’ ἔην.** Reading is defensible. Kept.
- **Pass 1's refusals** (open points 2, 4, 5, 6, 8–11, 13, 14; 15.333 σίτου καὶ κρειῶν beyond the `l` plural now aligned; 15.276 νύ; 15.343) re-examined; no reason found to reverse any.
- No metrical flag in the packet; none scanned by hand.
