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
