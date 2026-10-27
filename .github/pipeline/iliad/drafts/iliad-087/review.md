# iliad-087 (Iliad 14.109–221) — review, pass 1 of 2

Reviewer: adversarial, strongest model. Files read: conventions.md (rules sections; the table grepped), runbook.md section 2, packet.md, units.json, new-renderings.md, drafts/iliad-001/units.json (model), iliad-086.json (last unit), the source for 5.375, 5.859–861, 13.10 and the Odyssey source for 8.362. `units.json` was edited in place by script; every `t` is byte-identical to the draft's (checked by comparing the 63 `t` strings before and after). No modern translation consulted. There is no iliad-088 draft or published part yet, so the end of the part is checked only inside the part.

Result: 0 high, 3 medium, 11 low changes; 12 findings refused.

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 143 · l | medium | κοτέουσιν rendered "angry" in `l` ("are the blessed gods angry"), against the table (κοτέω keeps "bear a grudge", 1.181, 2.222, 3.345, 5.177; "angry" is kept for χόλος), and against the unit's own `i` ("bear a grudge") and the unit at 190 ("bearing a grudge") | `l` now "but with you not yet quite utterly do the blessed gods bear a grudge," |
| 143 · l | low | "not yet at all utterly" gave μάλα as "at all"; οὔ πω μάλα is "not yet quite" | "not yet quite utterly" (folded into the line above) |
| 143 · n | low | "σοί … the dative of the man the gods’ grudge … would fall on" was garbled | "σοί ‘with you’ is the dative of the person the grudge is held against (κοτέουσιν ‘bear a grudge’)" |
| 121 · i | medium | "rich in substance" for ἀφνειὸν βιότοιο; the table fixes ἀφνειὸς βιότοιο (5.544) as "rich in livelihood" in both layers and lists "rich in substance" as avoided on purpose. `l` already had "rich in livelihood" | `i` now "a house rich in livelihood" |
| 121 · i | low | πυροφόροι (table: "wheat-bearing") was turned into "fields of wheat", dropping the epithet | `i` "he had wheat-bearing fields in plenty" |
| 121 · n | low | "βίοτος means both ‘life’ and ‘means of living’, here substance" contradicted the restored rendering | "…‘means of living’, and here it is the second" |
| 139 · n | medium | "γηθεῖ (the uncontracted γηθέει, ‘rejoices’)": false label, since γηθεῖ is the contracted form of γηθέει | "(the third person singular of γηθέω ‘rejoice’)" |
| 115 · l, i, n | low | γάρ ("πορθεῖ γὰρ …") dropped in both layers and not noted | "For to Portheus …" in `l` and `i`; one clause added to the note saying γάρ gives the ground of the claim to a good father |
| 129 · i | low | ἔπειτα and αὐτοί ("ourselves") lost in `i` ("And there, for our part, let us hold back"); `l` has both | "And there, then, let us ourselves hold back…"; the μέν contrast with the next unit is carried by its "but" |
| 133 · n | low | note named "ἔκλυον ‘heard’", a form not in the line (the line has κλύον, unaugmented) | "κλύον is ἔκλυον ‘heard’ without the augment (here ‘listened to’), taking the genitive τοῦ ‘him’" |
| 183 · n | low | note only 18 words (the validator warns under 20) and said nothing of the form | expanded: χάρις is the beauty that shone from her adorned body; ἀπελάμπετο imperfect of ἀπολάμπω; πολλή agrees with χάρις |
| 190 · n | low | "the one verb ἀρήγεις serves both halves, and ἐγώ has none of its own" implies one form does both jobs; ἀρήγεις is second person | "ἐγώ has no verb of its own: ἀρήγεις is second person (‘you help’), so ‘I help’ is understood from it" |
| 193 · n | low | note thin (23 words) and left ἠμείβετ’ and its object unparsed | "ἠμείβετ’ is the imperfect of ἀμείβομαι ‘answer’, and τήν is Hera, its object" |
| 211 · n | low | scansion flag, hand-scanned (below): irregularity real, not in the note | one sentence added: "The line is metrically irregular as transmitted: with one μ the short λο of φιλομειδής has to be scanned long, as the first syllable of the fourth foot (the double μ of φιλομμειδής would make it so)." |
| `about` | low | "the gods are not yet wholly against the Achaeans": Poseidon says the gods are not yet wholly angry with Agamemnon (143, σοί) | "against Agamemnon" |
| new-renderings.md, βιότοιο row | low (file other than units.json) | row recorded "rich in substance" as a new rendering, contradicting the table row at 5.544 and the fix at 121 | row now "rich in livelihood" / "rich in livelihood", "unchanged from the table’s ἀφνειὸς βιότοιο (5.544)"; copy it into the table (or drop it) accordingly at step 4 |

## Scansion, line 211

τὴν δ’ αὖτε προσέειπε φιλομειδὴς Ἀφροδίτη. By hand: τὴν δ’ αὖ | τε προ-σε | ει-πε φι- | λο-μει | δὴς Ἀ-φρο- | δί-τη, that is spondee, dactyl, dactyl, spondee, dactyl, spondee. Feet 1 to 3 fill with the usual licences of the reply-formula (τε long before πρ; the digamma of ἔειπε holds the hiatus). Foot 4 can be filled only if the short ο of φιλο- is scanned long: the line is regular with the double μ of φιλομμειδής (5.375, Odyssey 8.362, checked in the sources) and irregular with the single μ printed here, as at 3.424 and 4.10 (see iliad-020, iliad-021). Real, so the sentence is added. The second flag, "mute+liquid no position: Ἀφροδίτη (φρ)", is the ordinary licence that keeps the α short in the fifth foot; it appears in the regular reading too and is not added.

## Checked and found right (no change)

- Every other note label against the line: cases, tenses, moods, tmesis claims (κατὰ … καλύπτει, ἀπὸ … ἐλύσατο, ἐν … ἧκεν, πρὸς … ἔειπε, ἐκ … ὀνόμαζε), cross-references (5.860–861 verified in the source; Odyssey 5.89–90, 8.362, 18.298; "line 153", "line 200", "line 130"), "ends/begins at the ano teleia in mid-line N" for all 63 units, and the `ln` and `p` flags (¶ at 109, 133, 135, 147, 153, 193, 197, 211, 214 all carry `p`).
- Greek → `l`, word by word, and `l` ↔ `i`; the house renderings used unchanged (ἄναξ ἀνδρῶν, βοῶπις πότνια, χρυσόθρονος, αἰγιόχοιο, εὐρύοπα, κρείων ἐνοσίχθων, δῖα θεάων, ἀλαοσκοπιή, κέκαστο, ἀτρυγέτοιο, χαλκοβατὲς δῶ, τρίγληνα μορόεντα, νηγατέῳ, πευκαλίμῃσι "keen" as at 8.366, φρένες "wits", ἄκριτα "unsorted"/"endless").
- Repeats: 109 and 133 identical to the published `l`/`i`; 148–149 and 152 reuse the published wording of iliad-035 and iliad-064; 161 and 186 reuse iliad-058 and iliad-007 with the pronoun changed; 195–196 and 212 reuse the Odyssey lines. All the departures listed in new-renderings.md are what they say. 14.138: μιν is Agamemnon, so "to him", correct.
- Quotation marks: the speeches are 110–132 (Diomedes), 139–146 (Poseidon), 190–192 (Hera), 194–196 (Aphrodite), 198–210 (Hera), 212–213 (Aphrodite), 219–221 (Aphrodite); each has “ on its first unit and ” on its last, `mark` on the first unit of each, none stray. The 212 unit ends with a semicolon and no ”, the speech running on to 213. iliad-086 ends on 108 with ” (Agamemnon's speech closed), so Diomedes' speech opening at 110 is a new speech and 109 is narration: correct.
- Remembered English: nothing in `i` found to match a familiar version's phrasing; the phrases that came fluently ("looking like an old man", "bustling through the battle that brings men glory", "unfastened from her breast") were each rebuilt from the grammar and stand.
- `title`, `titleEn`, `part` and cite match parts.json (14.109–221).
- Note lengths: all 20–130 words (WARN band 25–110 exceeded only at 121 with 122 words and 148 with 111, both under the 130 limit).

## Findings considered and refused

1. 110 note, "ἀνήρ has no article: the man is not named": thin but true, and it prepares the reader for 112. Left.
2. 127 `i` turns ὅν κ’ ἐῢ εἴπω into "if I speak it well": the relative with κε and the subjunctive is general ("whatever I say well"), so the conditional keeps the force, and `l` keeps the literal relative. Left.
3. 119 "ὃ μέν is Oeneus" in `i` ("But Oeneus stayed"): the `i` layer may name a pronoun's referent; the referent is certain from 117–118. Left.
4. 116–117 note says Agrius and Melas "are its subject": loose (they stand in apposition to the unexpressed "they") but not false, and the note says "placed after it". Left.
5. 134 "ἦρχε takes the dative σφιν": the dative of the persons led after ἄρχω is Homeric (the formula ἦρχε δ’ ἄρά σφιν); label true.
6. 198 δαμνᾷ "second person singular present of δάμνημι": true as a person/tense label whichever voice it is; left. (The Odyssey's own entries read it the same way.)
7. 216 ποικίλον "intricate" for a strap: the table reserves "inlaid" for wood and metal and "intricate" for woven or worked stuff (3.327, 6.289); the strap is embroidered. Left.
8. 219 "tuck it into your bosom" for ἐγκάτθεο: a little looser than `l` "lay up", but the sense (put away in the fold) is right, the register is not borrowed from any version, and the new-renderings row already records it. Left.
9. 142 σιφλώσειε "maim": the note says the sense is a guess, and the table row does the same. Left.
10. 128 ἀνάγκῃ "since we must" in `i` for "by necessity": same force. Left.
11. 111 "takes offence in resentment" (redundant in English): the new-renderings row explains the choice (κότος and ἀγάομαι in one phrase); the pair is kept. Left.
12. 211 title of the epithet note: "5.375 and Odyssey 8.362 print φιλομμειδής" verified in both sources; the sentence is right.

Open for pass 2: gloss.json does not exist yet; the second pass reads it. The `about` and notes should be re-read once more after any gloss-driven change.


---

# Pass 2 of 2 (adversarial; units.json from scratch, then gloss.json)

Files read: runbook.md section 2, the conventions tables (grepped for κότος, ἀγάομαι, εὔχομαι, ὀλοός, ἄκριτος, ἀρετή, ἔξοχος and others), packet.md, units.json (all 63 units, every note label against the line), gloss.json (all 140 new entries and the broadened ones against the line and against the published iliad-glossary.json), new-renderings.md, the published iliad-027 (for καθεῖσεν). `units.json` and `gloss.json` were edited by script; every `t` is byte-identical to before (checked), no existing glossary entry was changed, and every `__broaden__` entry still contains the published old entry whole (checked by script). No modern translation consulted. Pass-1 edits were re-read for new errors: none found (143, 121, 139, 115, 129, 133, 183, 190, 193, 211, `about` all stand).

Result: 0 high, 5 medium, 12 low changes (17 in units.json and gloss.json), plus 3 low changes in new-renderings.md; 13 findings refused. Layer checks run by script on all 63 units: every `l` has the line count of its `t`, no `i` has a line break, no straight quote or doubled space, “ and ” balance (open on 110, 139, 194, 198, 212, 219 and the ones carrying the speech from 190, closed on 131, 143, 195, 208, 213, 220), `mark` on the first unit of each of the seven speeches, `p` on every ¶.

## Changes

| line / form · field | severity | what was wrong | what was done |
|---|---|---|---|
| 110 (αἴ κ’ ἐθέλητε …) · n | medium | "μή τι … ἀγάσησθε is a prohibition": false label. The subjunctive is governed by the same αἴ κε as ἐθέλητε (the glossary entry itself says "after αἴ κ’"), so it is a second negative condition, not a prohibition | note now says so ("‘and if none of you is indignant’") |
| 110 (αἴ κ’ ἐθέλητε …) · i | medium | "none of you takes offence": the table’s ἀγασσάμενοι (7.41) fixes ἀγάομαι "be indignant" ("feeling indignation") and lists "taking offence" as avoided on purpose | `i` "none of you is indignant in resentment"; the note drops "take offence" |
| 202 (οἵ μ’ ἐν σφοῖσι …) · n, l, i | medium | note called καθεῖσε "the aorist of καθίημι ‘send down’". It is the aorist of καθίζω (causative, ‘set down, seat’), as the published iliad-027 note and glossary (καθεῖσεν) have it, and as gloss.json has it; `l` "sent down" and `i` "sent Cronus down" took the wrong verb’s sense | note: aorist of καθίζω, "set down"; `l` "set down beneath the earth"; `i` "set Cronus down below" (row added to new-renderings.md) |
| gloss θελκτήρια | medium | "neut. acc. pl." but the word is the subject of τέτυκτο (θελκτήρια πάντα τέτυκτο) | "neut. nom. pl., subject of τέτυκτο" |
| gloss πεφασμένον | medium | "neut. acc. sg., agreeing with μῦθον": μῦθος is masculine | "masc. acc. sg." (lemma φημί kept, see refused 1) |
| 129 (ἔνθα δ’ ἔπειτ’ …) · n | low | note took ἄρηται from αἴρω; the published glossary entry (and the broadened one for this part) take it from ἄρνυμαι; the note and the glossary must agree | note: "aorist subjunctive of ἄρνυμαι ‘win, take for oneself’" |
| 135 (οὐδ’ ἀλαοσκοπιήν …) · n | low | "ends at the ano teleia, four lines on": the unit has four lines (135–138), so the stop is three lines on; ambiguous | "ends at the ano teleia at the end of line 138" |
| 183 · n | low | ἀπελάμπετο called "the imperfect of ἀπολάμπω" without saying that the form is middle (the gloss says so) | "imperfect (middle form) of ἀπολάμπω" |
| gloss πορθεῖ | low | "epic (= Πορθέϊ), of possession": the form is the (also Attic) contracted dative; the case is that of the parent with ἐξεγένοντο, not possession | "masc. dat. sg., contracted (Homeric Πορθέϊ), of the parent: ’to Portheus’" |
| gloss καθεῖσε | low | "κατ-έ-εἷσε" doubles the augment (εἷσε is already the augmented aorist of ἕζω) | "(καθεῖσε = κατ-εἷσε, with εἷσε the aor. of ἕζω ’seat’, augment included)" |
| gloss ἱμείραιτο | low | voice missing: the -αιτο ending is the middle | "aor. opt. 3 sg. mid. dep." |
| gloss ἀνέσαιμι | low | asserted ἀνίημι and "σ-aorist" flatly while the unit note says verb and sense are not certain | "ἀνίημι (verb and sense uncertain)"; "σ-aorist" dropped |
| gloss κοτεσσαμένη | low | translation ’having become angry’; the house rendering (table, unit 190) is "bear a grudge" | ’bearing a grudge’ |
| gloss ἐγκάτθεο | low | "syncopated": the loss is of the final vowel of the preverb κατά, which is apocope | "apocope of κατά (ἐγκάτθεο = ἐγκατάθου)" |
| gloss ἀγάσησθε | low | quoted ’you take offence’, against the 7.41 row | ’you are indignant’ |
| `__broaden__` γένος | low | the new reading made 14.113 (γένος εὔχομαι εἶναι) an accusative of respect, against the unit note and the Odyssey table (εὔχομαι with the object γένος, "my birth I declare") | new part now gives "object of εὔχομαι: ’my birth’" and keeps "of respect: ’in birth’" for γένος κακόν |
| `__broaden__` ὥς | low | the new reading (ὥς = ὡς ’like’, after its noun, ἠέλιος ὥς) repeats the old entry’s own reading (βόες ὥς ’like cattle’): a broadening that adds nothing | key removed from `__broaden__`; the published entry is untouched. 17 broadenings remain (the file held 18, not 19) |

new-renderings.md (not units.json): the ἀφνειὸν βιότοιο row is dropped (it only restates the table row ἀφνειὸς βιότοιο, 5.544, and pass 1 said "copy it into the table or drop it"); it is now named in the "Uses of existing table rows without change" paragraph. The ἀγάσησθε row now has "is indignant" and "takes offence" among the avoided. A row for καθεῖσε ("set down") is added. Other rows that say "unchanged from the table" (βοῶπις πότνια Ἥρη, χαλκοβατὲς δῶ, τρίγληνα μορόεντα, νηγατέῳ, εὐρύοπα Ζεύς, ἄκριτα νείκεα, ἀτρυγέτοιο, κλυτὸς ἐννοσίγαιος) are likewise restatements; left, since each is a single line with a different Greek context and copying them is harmless, but the publisher may skip them.

## The uncertain forms named for this pass

- πεφασμένον: lemma φημί, perfect passive participle, "spoken": kept (the unit note says only "a perfect passive participle" and "a word spoken", true on either derivation); gender fixed.
- καθεῖσε: fixed, see above (unit and gloss now agree with each other and with iliad-027).
- ὁμωθῆναι: aorist passive infinitive is certain from the ending; the lemma ὁμόω "unite" (from ὁμός) is the usual one; kept, and the unit note’s "to be united" matches `l`/`i`.
- ἱμείραιτο: the parse stands (aorist optative middle, after εἴ πως, Zeus is the subject); voice added.
- ἀφεστᾶσ’: correct as the perfect 3 plural of ἀφίσταμαι (contracted ἀφεστᾶσι, elided before οὐδέ), subject οἳ; "stand aloof" matches `l`; kept.
- πορθεῖ: Πορθεύς in the dative with ἐξεγένοντο, as the unit note says; fixed above. It is not the verb πορθέω (a verb would leave τρεῖς παῖδες without a sense for "to").
- the 18 broadenings (not 19): each old entry is present whole and in front; each new reading was checked against the line (θυγατρῶν, καλῷ, κόσμον, λευκὸν, στήθεσφιν, τετελεσμένον, ἀγαθοῦ, ἀμβρόσιον, ἀπόλοιτο, ἀφνειὸν, ἄρηται, ἔνι, ἕρματα, ἧκεν, ὀλοὸν, ἄγριος right as written; γένος and ὥς fixed as above).

## Findings considered and refused

1. πεφασμένον from φαίνω ("shown") instead of φημί: both are argued; the gloss and the note say "spoken", which is the sense the line needs; left, no claim is made that the derivation is certain beyond the lemma φημί.
2. ἐπῆρσε "(= ἐπήραρε)": the two aorists are different formations of the same verb; the equation is loose but the meaning given is right. Left.
3. ὀλοὸν κῆρ "deadly": the table has "baneful/baleful" at 1.342, 3.133, 9.305 and "deadly" at 12.425, 13.629; the later rows and the row in new-renderings.md agree. Left.
4. 113 "declare … to be" for εὔχομαι εἶναι: the Iliad table has "claims to be" (2.82), but the Odyssey table fixes εὔχομαι as "declare" and has the same phrase with γένος (my birth I declare); the Iliad’s own "claim" rows are for other contexts. Left.
5. 110 `i` "none of you" for ἕκαστος: a paraphrase of "each" that keeps the force. Left.
6. 133 "μάλα μέν … looks forward to the ἠδέ": loose but the pairing μέν … ἠδέ is real. Left.
7. 134 "βάν for ἔβησαν": the Attic equivalent is given, not a claim of identity of formation. Left.
8. 163 note: χεύῃ "aorist of χέω" without saying subjunctive: the sense (‘she might pour’) shows the mood and the gloss states it. Left.
9. 198 δαμνᾷ "second person singular present of δάμνημι": true under either voice; the gloss gives the middle. Left (as in pass 1).
10. 190 κοτέω entry "be angry" in the gloss: the glossary lists meanings, and the house "bear a grudge" is first. Left.
11. 208 ἀνέσαιμι: the note and the gloss now both say the verb is uncertain; `l`/`i` "bring back" kept.
12. 175 ἐκ κράατος "from her immortal head": the preposition is rendered literally, the force (locks falling from the head) is clear. Left.
13. Quote-mark placement at 190: “ and ” fall in one unit; correct since the whole speech is that unit.

No other label, case relation, tense, mood, particle or cross-reference was found false; every "begins/ends at the ano teleia in mid-line N" was recounted against the line count of `t` (115, 121, 129, 148, 153, 181, 184, 219 all right).
