# iliad-033 (5.627–718) — reviewer, pass 1 (units only)

`gloss.json` not read or touched (glosser concurrent). `t` unchanged in all 48 units (checked by script). Pass 2 (gloss.json) still to do. Unit index = position in `sentences` (0-based).

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 698 (unit 37) · `l`, `i` | major | κεκαφηότα θυμόν is already fixed in the Odyssey table (5.468, odyssey-026): `l` "spent-breath spirit", `i` "exhausted, gasping spirit". The draft invented "his spirit that was gasping grievously" / "which had been gasping grievously", departing from a binding house rendering without a reason, and with `l` (“was gasping”) and `i` (“had been gasping”) disagreeing in tense. | `l` now "his badly spent-breath spirit"; `i` now "revived his grievously exhausted, gasping spirit" (κακῶς carried as "badly"/"grievously"). `new-renderings.md` row for 5.698 still shows the old wording: the caller must correct it. |
| 698 (unit 37) · `n` | major | Claimed κεκαφηότα is "a verb that occurs only here"; false, it stands at Odyssey 5.468 with the same noun. | Note rewritten: rare perfect participle, derivation disputed, also at Od. 5.468, English follows the Odyssey; sense uncertain. (Flag from drafter: resolved.) |
| 704–707 (units 41, 42, 43) · `l`, `i`, `n` | moderate | Name spelled "Orestbius" for Ὀρέσβιος (ὄρος + βίος); the stray t is an error and the form is not the Latinised "Oresbius". Occurred in 41 `l`+`i`, 42 `n`, 43 `n`. | Changed to "Oresbius" everywhere in units. The glosser's `gloss.json` and `new-renderings.md` may carry the old spelling; caller to check. |
| 718 (unit 47) · `n` | moderate | "the exhortation is in the aorist subjunctive μεδώμεθα": false label. μέδομαι has present stem; μεδώμεθα is a present subjunctive (the published note at iliad-025 says only "subjunctive of exhortation"). | "aorist" → "present". |
| 714–716 (unit 45) · `n` | moderate | "stand in published parts, spoken there by other people": false for 5.714, which is Hera's own address to Athena at 2.157 (iliad-008); only 5.716 was spoken by someone else (Agamemnon, 2.112). | Note now says exactly that. |
| 665–667 (unit 20) · `n` | minor | Note says "the Greek has no object" while `l` reads "so that he might step on it" (contradicts its own `l`). | Note now adds that `l` supplies "it" to complete the English. `l` left as is. |
| 663 (unit 18) · `n` | minor | "the same half-line is repeated at 692": 663 and 692 are identical whole lines. | "half-line" → "whole line". |
| 692 (unit 34) · `n` | minor | "The first half-line is the same as 663": same error, same position claim. | "first half-line" → "first line". |
| 633–634 (unit 3) · `n` | minor | ἐόντι said to agree with both τοι and φωτί; φωτί is a dative noun in apposition, the participle agrees with τοι. | Reworded: ἐόντι agrees with τοι, φωτί in apposition to it. |
| 637 (unit 4) · `n` | minor | "that is, the heroes of the previous generation": Greek says only ἐπὶ προτέρων ἀνθρώπων, "in the time of earlier men"; "previous generation" over-specifies. | "men of earlier generations". |
| 652–653 (unit 12) · `n` | minor | τεύξεσθαι called "the future infinitive … used passively": imprecise label (it is a future middle form, passive in sense). | "future middle infinitive of τεύχω ‘make’, passive in sense". Reading itself confirmed, see Refused. |
| 681 (unit 29) · `n` | minor | "Hector sets out to rescue Sarpedon": not what the lines say at this point (he goes through the front rank after seeing Odysseus' slaughter; Sarpedon's plea comes in 684 ff.). | Reworded to what the lines say. |
| 696 (unit 36) · `n` | minor | Note glossed κέχυτ' as "had been poured" while its own `l`/`i` say "was poured". | "‘was poured’ (the pluperfect gives the state reached)". |

Counts: major 2, moderate 3, minor 8 (13 note/unit edits across 12 units; the Oresbius fix counted once).

## Considered and refused

- **τεύξεσθαι (5.653)**: the drafter's reading kept. Taken as the future of τυγχάνω ("you will obtain"), it would need the accusative with a verb that takes the genitive, and σοί (dative) could not be its subject; taken as the future middle of τεύχω in passive sense ("slaughter and death-fate will be brought about for you"), σοί is the dative of interest, φόνον καὶ κῆρα the accusative subject, and the construction then shifts to σέ (understood) with δαμέντα … δώσειν. The note describes exactly this. `l` "will be brought about", `i` "will come upon you" agree with it.
- **κατὰ πληθὺν Λυκίων, "toward the throng" (676)**: κατά with the accusative of motion toward/among is defensible; "among" would not be clearly better. Kept.
- **νόησε "noticed" in `l` (665, 669) vs "had the wit" in `i` (665)**: `i` takes the sense of the verb with an infinitive (think to do); same `l` word each time. Kept.
- **κεῖσθαι, `l` "lie there" / `i` "lie here" (684–685)**: Greek gives no place; both supply one for the speaker's situation. Kept.
- **Ἄρηα as "accusative subject of an unexpressed ‘was’" (702)**: it is the object of ἐπύθοντο with a predicative phrase; the note's gloss gives the right English. Kept, as an acceptable shorthand.
- **ἤϊξαν "plural verb after a neuter plural subject" (656)**: true of the form as an observation; no claim about Attic rule. Kept.
- **Quotation marks**: all checked. “ and `mark` on 633 (Tlepolemus), 648 (Sarpedon), 684 (Sarpedon to Hector), 714 (Hera); ” on 646, 654, 688, 718. No quotation mark on the reply-formula units (647, 655, 689, 711) or on the unit before each speech; iliad-032 ends on narrative (no speech crosses in). Nothing to change.
- **Scansion**: no lines flagged in the packet; no note added.
- **Shared lines (627, 630, 671, 681, 713, 714, 716, 718)**: published English reused as the packet and new-renderings state; checked against the packet.

# Pass 2 (gloss.json, new-renderings.md)

`units.json` not changed in pass 2 (`t` untouched). Every non-broaden entry (140) matches `novel-forms.json` one to one; all under 230 characters, typographic ’ only, no line numbers, no "here". Each of the 17 `__broaden__` entries starts with the old `known-forms.json` entry whole + " · " (checked by script); each added reading was checked against the line.

## Changes

| entry | severity | what was wrong | what was done |
|---|---|---|---|
| τεύξεσθαι | major | Parsed as τυγχάνω "get, obtain (+ acc. here)", contradicting the unit (future middle of τεύχω, passive in sense; σοί dative of interest, φόνον καὶ κῆρα subject) and the unit's `l`. Also had "here". | Lemma τεύχω, "passive in sense, ’will be brought about’", with a pointer that the future form is identical to τυγχάνω's. |
| ὀρέσβιον | moderate | "Orestbius" | "Oresbius". |
| ἐμπνύνθη | moderate | "augmented": the ἐμ- is the preverb ἐν-, there is no augment (cf. ἀμπνύνθη); "pass. dep." mislabels a passive aorist form with intransitive sense. | "aor. 3 sg. pass. form, intrans. in sense, unaugmented (preverb ἐν-)". |
| γόνον | moderate | Called "acc. subject of an infinitive"; σέ is the subject of εἶναι, γόνον is the predicate. | "predicate accusative with an infinitive". |
| δώσειν | moderate | "that (he) will give": the understood subject is σέ, "you" (as the unit's `l`/`i` and the note say). | "that (you) will give". |
| ἐπιβαίη | minor | Gloss ’so that he might walk’ departed from the verb ("step on"). | ’so that he might step’. |
| κέχυτ | minor | Gloss ’lay poured out, was shed’ disagrees with the unit's "was poured". | ’was poured’. |
| κηφισίδι | minor | "adj. of two endings" is wrong for a feminine Κηφισίς. | "fem. adj., dat. sg. Κηφισίδι". |
| ὀστέω | minor | Text prints ὀστέω with no iota subscript; entry called it dat. sg. without saying so. Reading (dat. of ὀστέον with ἐγχριμφθεῖσα) confirmed. | Entry says "printed without iota subscript (= ὀστέῳ …)". |
| παρήϊξεν | minor | Attic equivalent misaccented (παρῆξε). | παρῇξε. |
| __broaden__ κακῶς | moderate | Added ’grievously, sorely’ / ’gasping grievously’, which does not match the unit's "badly spent-breath" / "grievously exhausted". | ’badly, grievously’ (κακῶς κεκαφηότα ’grievously exhausted’). |
| __broaden__ κακῷ | minor | ’cruel (word)’ but `l` has "evil word" and the note ‘evil word’. | ’evil (word)’. |
| __broaden__ ἐμοὶ | moderate | "dat. of the agent after ὑπό … ’by me’": ὑπ’ ἐμοὶ δμηθέντα is "subdued under me" (ὑπό + dat. of place under); agent claim and "by me" unsupported. | "dat. governed by ὑπό: ’under me’ … ’subdued under me’". |
| __broaden__ κατὰ | minor | πληθύν written with acute; text has πληθὺν. | πληθὺν. |
| new-renderings.md 5.652–653 | major | Said τεύξεσθαι is "a passive future of τεύχω". | "future middle of τεύχω, passive in sense (not τυγχάνω)". |
| new-renderings.md 5.698 | major | Old wording ("his spirit that was gasping grievously", "had been gasping grievously", "verb occurs only here"). | Row now `l` "his badly spent-breath spirit", `i` "revived his grievously exhausted, gasping spirit", rare participle also at Od. 5.468, follows odyssey-026. |
| new-renderings.md 5.666 | minor | Row said only "the Greek has no object", at odds with `l` "step on it". | Added: `l` adds "it" to complete the English (matches the unit note). |

Counts: major 3, moderate 6, minor 8 (17 edits). Name check: "Orestbius" now appears nowhere except in this log's description of the pass-1 fix.

## Considered and refused

- ὕλῃ (Ὕλῃ, town in Boeotia, "of place", also the homonym ὕλη "woodland"): correct, kept.
- Other broadened readings (αἰχμητὴν, αὐχένα, βίην, εἷλεν, μάχης, μέσσον, μακρὸν, μῦθον, οἷόν, περικαλλέϊ, πλήξιππον, ἀγαυοῦ, ἐπὶ, ἕλοιτο, and the rest of κατὰ): each reading occurs and is correctly parsed. οἷόν τινά is masc. predicate accusative; kept as "agreeing with τινά".
- βεβλήκειν "3 sg. … or 3 pl.": the form is general; only 3 sg. occurs, no change.
- ἅλιόν (Halius, "also the adj. ἅλιος ’vain’"): the adjective at the line of Hera's speech is the known key ἅλιον, whose entry already covers it; kept.
- Broadened entries are over 230 characters by accumulation; the limit is read as applying to new entries. Not exhaustively audited: whether every other known-form entry covers its use in this part (only the 17 the glosser flagged were checked).
