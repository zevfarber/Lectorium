# Review — iliad-032 (Iliad 5.519–626)

Two passes. Pass 1: units.json against the Greek (notes, Greek to `l`, `l` to `i`, remembered English, quotation marks, hand scan of 574 and 576, cross-references checked against the archive and the published Iliad and Odyssey parts). Pass 2: a fresh re-read of the edited units, then every entry of `gloss.json` (novel keys, `__broaden__`, and the known-forms list for forms whose old entry does not cover the use here). `t` was not touched (checked: unit `t` joined equals the archive lines 519–626). The build was not run.

Severity: high = wrong sense or wrong translation; medium = false grammatical claim, wrong cross-reference, or a broken house rule; low = polish, clarity, hedging.

Counts: high 0, medium 7, low 29 (units.json 5 medium + 13 low; gloss.json 2 medium + 13 low; new-renderings.md 3 low).

## Changes to units.json

| line | field | sev | what was wrong | done |
|---|---|---|---|---|
| 520 | i | low | καὶ αὐτοί ("they themselves too") lost its "too" in `i` (it is in `l`) | "and they themselves, too, were afraid …" |
| 522 | l, i | medium | ἀκροπόλοισιν ὄρεσσιν is the same two words as Odyssey 19.205 (odyssey-094: "high mountains"); the draft said "high-peaked mountains" and did not record a departure. The Odyssey rule is to reuse unless the context forbids, and it does not | "high mountains" in `l` and `i`; new-renderings row rewritten to say it is reused from odyssey-094 |
| 522 | n | medium | claimed the second part of ἀκρόπολος is "usually derived from πολέω"; I cannot confirm that in LSJ/Autenrieth/Cunliffe, and the note is supposed to say when a formation is not known | now: ἄκρος "top" plus a second part of uncertain origin; says the Odyssey has the same words and its English is kept |
| 532 | n | low | "now the opposite case" says the case is opposite; it is the same case (genitive), with the opposite outcome | "now for the opposite outcome" |
| 533 | n | medium | "Αἰνείω is the dative of Αἰνείας" is false: Αἰνείω is the genitive (= Αἰνείαο), agreeing with genitive μεγαθύμου ("companion of great-hearted Aeneas"), as `l` and `i` already have it | note corrected |
| 538 | i | low | "he drove it through the belt": "it" could be read as the shield | "he drove the spear through the belt" |
| 543 | n | medium | cross-reference "Odyssey 3.487–488" is wrong: the quoted clause is 3.488–489 (odyssey-013, unit at 487: Φηρὰς is line 488, Ὀρτιλόχοιο line 489) | "3.488–489" |
| 550 | i | medium | "followed the Argives" drops ἅμ’ and says the brothers came after the army; `l` and the Greek say "along with the Argives" | "followed along with the Argives" |
| 550 | n | low | "The verbs here are duals" but two of the three words are participles | "The verb and the participles here are duals" |
| 556 | n | medium | κατέκταθεν called "the dual aorist passive … in the old form -θεν for -θησαν": -θεν for -θησαν is a 3 pl. ending, so the label contradicts itself; the verb is plural after the dual αὐτώ | now "the aorist passive … -θεν for -θησαν (a plural verb after the dual αὐτώ)" |
| 556 | i | low | ὄφρα καὶ αὐτώ: "too" lost in `i` | "until they themselves, too, were killed" |
| 566 | n | low | δίε given as "the unaugmented imperfect of δείδω"; the form belongs to the by-form δίω | "an epic imperfect ‘feared’, from δίω, a by-form of δείδω" |
| 568 | n | low | μεμαώς called the perfect participle of μέμονα; the lexica put it under μάω (perfect μέμαα) | corrected (matches the existing glossary entry for μεμαῶτε) |
| 584 | n | low | ξίφει called "the epic dative"; it is the ordinary dative of ξίφος | "the dative of ξίφος ‘sword’, a dative of means" |
| 585 | i | low | `i` ended with ";" where `t` and `l` end with a full stop (and the next unit's `i` begins with a capital) | full stop |
| 585 | n | low | "βρεχμός … is ‘the crown of the head’" stated flatly of a rare word; the lexica also give the front of the skull | "the top of the head, ‘the crown’ being the usual gloss, though the word may mean the front of the skull" |
| 618 | n | low | `l` supplies "upon him" (ἐπὶ … ἔχευαν has no object); the note did not say so | note says the English supplies "him", Ajax |
| 621 | l | low | ὤμοιιν is a dual (the note says "from the two shoulders") but `l` said "from the shoulders" | "from the two shoulders" (new-renderings row updated) |
| about | about | low | stated as fact that Mydon was Pylaemenes' charioteer; the note on 580 (rightly) says the Greek does not say so | "kill Pylaemenes, leader of the Paphlagonians, and the charioteer Mydon" |

## Changes to gloss.json

| key | sev | what was wrong | done |
|---|---|---|---|
| αἰνείω | medium | parsed "masc. dat. sg." (= Αἰνείᾳ); it is the genitive, as in the line (see 533 above) | "masc. gen. sg., epic -ω (= Αἰνείαο; Attic Αἰνείου)" |
| φευγόντων | medium | "in a genitive absolute: ‘when men flee’"; there is no absolute construction in 532, the genitive depends on ὄρνυται ("of men who flee") | "gen. pl.: ‘of men who flee’" |
| κατέκταθεν | low | "root aorist in -θεν" | "passive-type aorist in -θεν for -θησαν" |
| μύδωνα | low | "a charioteer from Paphlagonia": the Greek does not say it, and the unit note says it does not say whose charioteer he was | "a charioteer" |
| παισῷ | low | gender "masc." given to a town name, unsupported | gender dropped |
| προρέοντι | low | "epic uncontracted (= Attic προρρέοντι)": Attic is uncontracted too; the difference is only ρρ | "(Attic προρρέοντι, with ρρ)" |
| εὔπωλον | low | "fem. acc. sg." where Ἴλιον may be taken as fem. or neut. | "acc. sg. (fem. or neut.)" |
| ἀμφίβασιν | low | "a standing round to protect" states the sense as known | "a stepping round; a ring of men standing about (a rare word, the sense inferred)" |
| ἐφέστασαν | low | "aor. (or plpf.) … = Attic ἐπέστησαν" disagrees with the unit note (pluperfect) | "plpf. 3 pl. with the sense of an imperfect (= Attic ἐφειστήκεσαν)" |
| ἰωκάς | low | no sign of the uncertainty the note records | "(sense uncertain: also taken as din, or rout and pursuit)" |
| ἐόντε | low | "nom. dual" but at 609 it agrees with the accusative φῶτε | "masc. nom./acc. dual" |
| __broaden__ παμφανόωντα | low | old entry "neut. nom. pl."; here it is acc. pl. with δούρατ’ | broadened (old entry whole + new reading) |
| __broaden__ σάκος | low | old entry "neut. acc. sg."; here it is the nominative subject of ἀνεδέξατο | broadened |
| __broaden__ ἔγχεα | low | old entry "neut. nom. pl."; at 568 it is the accusative object of ἐχέτην | broadened |
| __broaden__ εἰδότε | low | old entry "dual nom."; at 608 it is acc. dual with φῶτε | broadened |

The 16 existing `__broaden__` entries were each checked: the old entry is preserved whole and the added reading is true of the line. The remaining novel entries (about 165) were checked against the line and left as they were.

## Changes to new-renderings.md (copied into conventions.md later)

- ἀκροπόλοισιν ὄρεσσιν: row now "high mountains" / "high mountains", reused from odyssey-094 (low).
- αἰδομένων … πέφανται (5.531): the Greek column had a stray δ’ that is not in the line; removed (low).
- ὤμοιιν ἀφελέσθαι: `l` column "from the two shoulders to take off" (low).

## Hand scan of the flagged lines

- 574 τὼ μὲν ἄρα δειλὼ βαλέτην ἐν χερσὶν ἑταίρων: τὼ μὲν ἄ | ρα δει | λὼ βα | λέτην ἐν | χερσὶν ἑ | ταίρων. The second foot needs ρα long; ἄρα's final α is short by nature. Real irregularity; the note on the unit (573) already says so in one sentence, and the place named (the long place of the second foot) is right. No change.
- 576 ἔνθα Πυλαιμένεα ἑλέτην ἀτάλαντον Ἄρηϊ: ἔνθα Πυ | λαι με νε | α ἑ λέ | την ἀ τά | λαν τον ἄ | ρηϊ. The third foot needs the final α of Πυλαιμένεα long. Real irregularity; the note already says so and names the third foot correctly. No change.

## Checks that passed

- Quotation marks: “ on 529 (`mark` "Agamemnon speaks") and ” at the end of 532; “ on 601 (`mark` "Diomedes speaks") and ” at the end of 606; no stray marks. iliad-031 ends on narrative, and 626 ends on narrative.
- `p` on the first unit of each of the eight paragraphs (519, 533, 541, 561, 576, 590, 596, 607); `ln` of all 64 units; line division of `l` equals `t`; no `\n` in `i`; no ASCII quotes.
- Cross-references checked in the archive: 3.449, 4.495, 4.496, 4.504, 5.42, 4.521, 4.534–535, 2.552, and the in-part references (536, 539, 559/554, 560, 562, 592, 610, 616).
- Reused lines identical to the published English: 5.540 (iliad-026), 5.562 (iliad-026), 5.625 (iliad-026), 5.626 (= 4.535b, iliad-026), 5.611 (= 4.496, iliad-026).

## Findings considered and refused

- τὸν at 596 as Ares (the drafter's call): accepted; Ares is the last-named figure and Diomedes names him in the speech. The note already says "most naturally".
- Dual ἑλέτην at 576 with Menelaus and Antilochus as the joint subject, the work shared out in the next lines: accepted.
- τὼ μὲν δὴ at 568 = Menelaus and Aeneas, against Antilochus at 570: accepted.
- φοίτα at 595 with Ares as subject: accepted (Ares is the subject of the preceding clause; Enyo's clause is closed by μέν … δέ).
- ἅλα δέ read as ἅλαδε: kept. The other reading (ἅλα as the accusative of the goal, δέ the connective) gives the same English; the note states what the edition prints.
- ἰωκάς, ζαχρειῶν, κύμβαχος, ἀμφίβασιν: translations kept; each is hedged in the note. I did not find a more certain reading in LSJ, Autenrieth or Cunliffe, so none was imposed.
- "Friends, be men" (529): read as possibly a remembered formula; refused as a finding, because it is the plain rendering of ἀνέρες ἔστε.
- ἀναιδέα "shameless" in `l` and "ruthless" in `i` (593): follows the Odyssey table and iliad-026 (4.521); kept.
- ἀτρέμας "motionless" against the Odyssey's "quietly" (other contexts, other lines): kept.
- Pylaemenes appears again, alive, at 13.658: not added to the note on 576, since a note should not assert about the rest of the poem what this part cannot show.
- βάλον (588) "threw down": the known entry's lemma gloss already includes "throw"; no broadening needed.
- δίε in the gloss ("aor. or impf."): a hedge, left.
- Unit divisions (every unit ends at . ; or ·; the longest are four lines): no change.
