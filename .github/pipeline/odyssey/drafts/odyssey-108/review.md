# Review — odyssey-108 (Odyssey 22.195–291) — Pass 1

Reviewer pass 1 of 2. Pass 2 (after `gloss.json`) is still to do: it also checks every parse in the glossary against the line.

**Changes to `units.json`: 69 — high 20, medium 23, low 26.** `t` was not touched (asserted in the edit script: the 53 `t` strings are identical before and after; every `l` keeps its line count; quotation marks and `mark`/`p` placement were checked and needed no change).

Severity: high = a wrong case relation or sense, or a rendering that contradicts a ratified house rendering in the conventions table; medium = a false label, wrong cross-reference, l/i disagreement, or an inconsistency with shipped parts; low = polish, over-precise or loose wording.

## What was checked

- Every grammatical label and every claim about where a word stands, in every note, against the line (all 53 units).
- Greek → `l` word by word; `l` ↔ `i`; remembered English in `i` (no phrase found that looks imported; the `i` wording problems found were the table-contradicting ones listed below).
- Quotation marks: the last unit of `odyssey-107.json` (22.194, `Taunting him, you said to him, Eumaeus the swineherd:`) carries no opening mark, and 195 opens “ with `mark` `Eumaeus speaks`, closing ” at 199 (unit 197). Speeches: 195–199 Eumaeus; 208–209 Odysseus; 213–223 Agelaus; 226–235 Athena as Mentor; 248–254 Agelaus; 262–264 Odysseus; 287–291 the herdsman. Each opens on its first unit, closes on its last, and `mark` and `p` sit on the right units (all 15 Murray paragraphs match the packet). No change needed.
- Scansion flag, line 238: scanned by hand, see below.
- `new-renderings.md` against the conventions table and the shipped parts (grep of the Greek in `odyssey-001..107.json`).

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 195 | l | low | ἔοικε is rendered "befits"; the house (and the glossary entry for ἔοικεν) has "it is fitting" everywhere else. | l: "as it is fitting for you". |
| 195 | i | low | Same: "befits" against the house "fitting". | i: "as is fitting for you". |
| 195 | n | low | Note repeated "befits". | Note follows l. |
| 195 | n | low | Label false: νῦν is an adverb, not a particle, so "a pile of intensifying particles" was not true of the whole phrase. | Note now says which word is which. |
| 203 | l | high | μένος is "strength" in the conventions table (μένος ἡμιόνοιιν, ἱερὸν μένος Ἀλκινόοιο, μένος αἰὲν ἀτειρής; "the sacred might of Alcinous" is in the avoided list); "might" is the table's ἀλκή. Also l "stood up" for ἐφέστασαν contradicted the note's "took their stand". | l: "breathing strength … they took their stand". |
| 203 | i | high | Same μένος error in i. | i: "breathing strength". |
| 203 | n | high | Note stated a house rendering ("μένος … might") that the table contradicts. | Note corrected. |
| 205 | n | medium | Cross-reference wrong: the published unit begins at 2.267 and the Mentor line is its second line, 2.268. | Line number corrected. |
| 205 | n | low | Label: the glossary parses εἰδομένη as a present-form participle that also serves for the aorist; 'the aorist participle' was too definite. | Reworded without the tense label. |
| 210 | i | medium | The table row for λαοσσόος (15.244) fixes i "rouser of the people"; i had a relative clause. | i follows the table. |
| 210 | n | medium | The note gave the derivation as fact; the table row for λαοσσόος requires a note that the derivation is disputed. | Disputed derivation stated. |
| 211 | n | low | The table row for ὁμοκλέω ("shouted") turns down "threatened"/"rebuked" because each picks one sense; the note's gloss picked one. | Gloss reduced to "shout". |
| 213 | l | medium | Case relation: οἱ αὐτῷ is dative "for him himself" (Mentor to defend Odysseus); "defend himself" made Odysseus the one defending. | l: "defend him himself". |
| 213 | n | low | Label imprecise: the epic ending is -ῃσιν (for -ῃ), not "-σιν for -ῃ". | Corrected. |
| 215 | i | medium | ὀΐω is "I suppose" in the table (row 22.140/159/165); "I think" is in its avoided list. l already had "I suppose". | i: "I suppose". |
| 215 | n | medium | Label false: with a passive infinitive (as the note itself says) νόον is its subject, not its object. | Corrected. |
| 216 | l | low | "too" has no Greek behind it (ἐν δὲ σὺ τοῖσιν ἔπειτα); δέ was turned into "then … too". | l follows the Greek words. |
| 219 | l | medium | l "forces" reads as armies; i said "strength" and the glossary gives βία "force, violence". l and i disagreed in sense. | l: singular "force". |
| 221 | l | high | κεδνός is "trusty" in the table (κεδνὰ ἰδυῖα) and in the shipped parts (κεδνὴ ἄλοχος, κεδνὴ μήτηρ); "careful" is in the table's avoided list. | l: "trusty". |
| 221 | i | high | Same. | i: "trusty". |
| 221 | n | high | Note stated "careful" as the house rendering. | Corrected. |
| 221 | n | low | Label: the verb is πολεύω (an infinitive of πολέω would be πολεῖν). | Corrected. |
| 224 | n | low | Garbled sentence ("the house reviles"). | Reworded. |
| 224 | n | low | Shipped odyssey-106 (22.26, same phrase) has i "with angry words". | Note follows. |
| 224 | i | low | Shipped odyssey-106 has "with angry words" for the same phrase. | i: "with". |
| 226 | l | high | μένος is "strength" and ἀλκή is "might" in the table (9.214 row: "ἀλκή is 'might', kept apart from μένος 'strength'"; shipped odyssey-041, 044, 058, 085); the draft had them as "might" and "valour". | l: "firm strength … any might". |
| 226 | i | high | Same. | i corrected. |
| 226 | n | high | Note stated the wrong house renderings. | Corrected. |
| 229 | l | medium | Shipped odyssey-055 (11.516, πολλοὺς δ’ ἄνδρας ἔπεφνεν ἐν αἰνῇ δηιοτῆτι) has "killed in fearsome fighting"; the draft's l had "slew" while its i had "killed". | l: "killed". |
| 231 | l | low | "own" is not in the Greek (σόν); l is the literal layer. | Removed. |
| 236 | l | low | δίδου is an imperfect; l had a simple past. | l: "was giving". |
| 236 | l | high | κυδάλιμος is "glorious" in the table (Μενελάου κυδαλίμοιο row, which turns down "illustrious" and "renowned") and in 14 shipped places; "glory-full" / "full of glory" made a second English. | l: "glorious". |
| 236 | l | high | ἀλκή is "might" in the table; see 226. | l: "might". |
| 236 | i | high | Same two errors in i. | i corrected. |
| 236 | n | high | Note repeated the wrong rendering. | Corrected. |
| 236 | n | high | Same. | Corrected. |
| 236 | n | low | The finite verb was not mentioned. | Added. |
| 236 | n | low | Scansion flag checked by hand (see review.md): the irregularity is real. The sentence is kept; it spoke of "the scanner", which is not a reader's concern. | Sentence made plain. |
| 239 | n | medium | Label false against the house glossary (ἕζετο: ἕζομαι, impf. 3 sg.). | Corrected to imperfect. |
| 241 | l | high | Case relations reversed: μνηστῆρας is the accusative object and Ἀγέλαος (nominative, with its patronymic) the subject; the l read "the suitors urged on … Agelaus". | l reordered so that the English keeps Greek order and the right subject: "the suitors Damastor's son Agelaus urged on". |
| 248 | l | high | The table row ἀάπτους (11.502) fixes l "untouchable", i "irresistible" (+ note: meaning not known; both are traditional guesses); shipped odyssey-106 (22.70, same phrase) has l "untouchable". The draft had "irresistible" in both layers. | l: "untouchable". |
| 248 | n | high | Note did not match the table row (meaning not known; two guesses). | Corrected. |
| 248 | mark | low | Second speech of Agelaus in this part, marked as the first ("Agelaus speaks"); the note itself says "speaks again", and shipped marks use "speaks again". | mark: "Agelaus speaks again". |
| 249 | n | medium | Label false: ἔβη carries the augment ε-; it is not unaugmented. | Corrected. |
| 251 | n | low | Label: ἐφίετε is not an uncontracted form of anything (it has the same shape in Attic). | Removed. |
| 251 | l | low | ἀκοντίζω is "hurled" in the other units of this part; "cast" here and at 262 made two Englishes. | l: "hurl". |
| 251 | i | low | Same. | i: "hurl". |
| 254 | n | medium | The note implied the same rendering as the table; the table has κήδεα "sorrows" (and says κῆδος is "sorrow"), so l "concern" is a departure that the note must own. | Note says so. |
| 255 | i | low | 255 "threw" against "hurled" at 265, 272, 282 for the same verb. | i: "hurled". |
| 256 | l | high | ἐϋσταθής is l "well-standing", i "sturdy" in the table (20.258), with "well-founded" in the avoided list. (Shipped odyssey-107 uses "well-founded" at 22.120 and 22.127: see Observations.) | l: "well-standing". |
| 256 | n | high | Same. | Corrected. |
| 256 | n | low | Cross-reference: two lines (257–258) repeat at 274–275; 259 is the next unit and repeats at 276. | Corrected. |
| 259 | n | medium | Label reversed: ἄλλου is the genitive depending on μελίη ("another man's ash spear"); it governs nothing. | Corrected. |
| 262 | l | medium | ἐξεναρίξαι is "to kill" in the table (11.273 row: "having killed"; "slew and stripped" turned down); "to strip us of life" is an invented compound. Also "cast" → "hurl" as in 251. | l: "should hurl … to kill us". |
| 265 | n | low | Only the clause repeats; the lines then differ (ὡς ἐκέλευεν / ὀξέα δοῦρα). | Corrected. |
| 266 | l | medium | The table row for βοῶν ἐπιβουκόλος ἀνήρ (20.235) fixes l "the man, the herdsman of the cattle" (the draft dropped the second "the"), and "killed" is the house verb for ἔπεφνε. | l corrected. |
| 266 | i | medium | ἔπεφνε means "killed" and the next lines show all four dead, but i said "hit" for three and "killed" for the fourth; and "the swineherd Elatus" can be read as the swineherd being named Elatus. | i recast so that every victim is dead and who killed whom is clear. |
| 266 | n | medium | Note matched the inaccurate i. | Corrected. |
| 269 | n | medium | Cross-reference wrong: odyssey-065 and -068 (and others) are earlier than this part. | Corrected. |
| 274 | l | high | Same as 256 (repeat must match). | Corrected. |
| 281 | n | medium | Cross-reference wrong: 266 does not end with ὀξέα δοῦρα; 265 and 272 do. | Corrected. |
| 283 | n | low | Position claim: βάλε is the third word of the line, not "at the start". | Reworded. |
| 283 | i | low | "and the swineherd Polybus" can be read as a swineherd named Polybus (the Greek order is object, subject). | i recast with "by". |
| 285 | l | low | Table row fixes l "the man, the herdsman of the cattle". | Corrected. |
| 285 | n | medium | "First two … the third" did not match the line: βάλε is stated for Odysseus and understood for the two in 284; βεβλήκει belongs to the herdsman. | Reworded. |
| 287 | i | medium | Syntax: εἴκων is a participle and the verb is the infinitive εἰπεῖν; i made "yield" the thing forbidden and "speak" a second one. | i follows the Greek construction. |
| 290 | l | medium | ὅν is masculine, so it refers to ποδός "foot", not to the neuter ξεινήϊον; l put "which" after "guest-gift". And ἀλητεύω is "wandering" in the table (14.126) and "goes wandering through the house" in shipped odyssey-086 (17.501); "as a vagrant" added a noun that the verb does not have. | l reordered and "wandering through the house" used. |
| 290 | i | medium | Same ἀλητεύω point. | i corrected. |
| 290 | n | medium | Note did not say what ὅν refers to. | Antecedent stated. |

### Changes to `new-renderings.md` (made because the rows contradicted the conventions table or shipped parts, and would otherwise have been copied into the table at publish)

- high: **deleted** rows ἀλκή "valour", κεδνὴν ἄλοχον "careful wife", κυδάλιμος "glory-full", ἐϋσταθὴς μέγαρον "well-founded", ἄαπτος l "irresistible", ἀλητεύω "going about as a vagrant": each Greek word already has a row in the table (ἀλκή 9.214 "might"; κεδνὰ ἰδυῖα "trusty"; Μενελάου κυδαλίμοιο "glorious"; ἐϋσταθής 20.258 "well-standing"/"sturdy", "well-founded" avoided; ἀάπτους 11.502 "untouchable"/"irresistible"; ἀλητεύω 14.126 "wandering"), and the draft's choice differed.
- high: **replaced** the μένος row: μένος is "strength" (the draft said "might" and listed "strength" as reserved for ἲς/σθένος; the table has μένος "strength" and "the sacred might of Alcinous" in its avoided list).
- medium: σθένος row now "strength" (avoiding "might", reserved for ἀλκή), noting the same English as μένος, as already shipped.
- medium: κῆδος row said the table's κήδεα is "cares"; the table has "sorrows". Corrected; the row now says why l uses "concern".
- low: ἐπιβουκόλος row l now "the man, the herdsman of the cattle" (table 20.235); νείκεσσεν row i "with angry words" (shipped odyssey-106).

## Scansion flag, 22.238

`ἠμὲν Ὀδυσσῆος ἠδ’ υἱοῦ κυδαλίμοιο`. By hand: ἠ-μὲν-Ὀ is a dactyl (the closed μέν is short before the vowel Ὀ); δυσ-σῆ a spondee; then the closed final syllable -ος of Ὀδυσσῆος stands before the vowel of ἠδ’, where no position can make it heavy, so it has to be read long as the longum of the third foot (-ος ἠδ’, a spondee, which is also the line's caesura place); υἱ-οῦ is the fourth-foot spondee; κυ-δα-λι is the dactylic fifth foot (the α and ι of κυδάλιμος are short) and μοι-ο the last foot. The scanner's "ambiguous" concerns only whether α and ι of κυδάλιμος are scanned short or long at equal cost; it does not change the line. The one real licence is the lengthened -ος of Ὀδυσσῆος. The irregularity is real, so the unit's note keeps one plain sentence saying so (reworded to drop "the scanner"). No other line in the packet is flagged.

## Findings considered and refused

| Line | Finding | Reason refused |
|---|---|---|
| 195–291 (passim) | γε left out of `l` at 212, 215, 219, 226, while kept at 197 and 254. | Refused. The shipped practice is to render γε only where English can bear it (odyssey-007 at 2.279 has `οὐδέ σε πάγχυ γε` with γε untranslated); the notes name γε where it matters, and adding "at least" to four more lines would make the literal layer worse. |
| 200 | `i` has "bonds" (plural) for δεσμῷ (singular), `l` has "bond". | Refused. Number only; the idiom of the English plural does not change the sense. |
| 239 | μέλαθρον "rafter" against shipped odyssey-089 (17.150) "roof". | Refused. Sitting "up the roof" is not the picture ἀνὰ μέλαθρον gives; the word is "roof-beam, roof" and the note already says it is also used for "roof". Kept as a conscious second English, listed in `new-renderings.md`; the orchestrator may want the table row to say "rafter" only for this use. |
| 251 | βλῆσθαι called "the aorist passive infinitive in epic form". | Refused. The form is the athematic aorist infinitive of βάλλω (middle-passive in shape, passive in sense); LSJ gives it under the aorist passive, and the note adds no claim beyond it. |
| 289 | φέρτεροί εἰσι "stronger" against shipped odyssey-077 (unit at line 89, `ἐπεὶ ἦ πολὺ φέρτεροί εἰσι`) "far superior", `i` "better" in odyssey-058. | Refused. The same Greek words stand in odyssey-041 (`ἐπεὶ ἦ πολὺ φέρτεροί εἰμεν`) with l "much stronger", i "far stronger", which `l`/`i` here follow; 058's φέρτερον is the neuter predicate "better", a different use. The disagreement is among shipped parts, not made by this draft. |
| 248 | `i` "irresistible as they were" adds "as they were". | Refused. It is the draft's way of keeping the epithet in the past tense of the sentence; the sense is not changed, and the table fixes i "irresistible". |

## Observations outside this part (not edited)

- Shipped `odyssey-107` renders ἐϋσταθέος μεγάροιο (22.120, 22.127) "well-founded" in both layers, against the table's ἐϋσταθής row (l "well-standing", i "sturdy"; "well-founded" avoided). This part follows the table. 107's two units (and the 22.257/274 repeats here) will differ until someone decides which is wrong.
- Shipped `odyssey-005` (unit at line 61) has ἀλκή "valour", against the table and the other shipped parts ("might"). Not touched.
- The glossary entry for `ἔβη` says "aor. 3 sg., root aorist, unaugmented (= ἔβη)"; ἔβη has the augment. This is a glossary error (the note at 249 is now right). For the glosser/pass 2.
- Shipped `odyssey-077` renders ἐπεὶ ἦ πολὺ φέρτεροί εἰσι "far superior" while odyssey-041 has "much stronger" for the same words; here `l`/`i` follow 041.

## Counts

High 20 · medium 23 · low 26 · total 69 edits to `units.json` in 53 units (plus the `new-renderings.md` corrections above). Refused: 8.


# Pass 2 — units.json re-read fresh, and every entry of gloss.json against the line

`t` was not touched (asserted in the edit script: the 53 `t` strings are identical before and after, every `l` keeps its line count, and the 7 speeches still open with “ and close with ”, with `mark` on the same 7 units). No modern translation was opened or recalled.

**Changes in pass 2: 23 — high 4, medium 8, low 11** (7 to `units.json`: high 4, medium 3; 16 to `gloss.json`: medium 5, low 11). Refused or left as found: 8.

## Changes to units.json

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 266 | l | high | Case relation: "and Peisander killed the man, the herdsman of the cattle" reads as Peisander killing; Πείσανδρον is the object and the herdsman the subject. (Pass 1 left it in that order when it moved "killed".) | l: "and Peisander the man, the herdsman of the cattle, killed." (table wording kept) |
| 277 | l | high | "And Amphimedon Telemachus struck" reads in English as Telemachus striking Amphimedon; the Greek is subject, object, verb. | l: "And Amphimedon struck Telemachus on the hand at the wrist". |
| 279 | l | high | Same reversal: "And Ctesippus Eumaeus … the shoulder grazed" reads as Eumaeus grazing Ctesippus. | l: "And Ctesippus, above the shield, with a long spear / grazed Eumaeus on the shoulder;" (line count kept). |
| 283 | l | high | "Eurydamas struck city-sacking Odysseus" reads as Eurydamas striking Odysseus; the Greek has Εὐρυδάμαντα object, Ὀδυσσεύς subject. | l: "Then in turn Eurydamas city-sacking Odysseus struck," so that the object-subject order of the next line (Amphimedon Telemachus, Polybus the swineherd) reads the same way. |
| 203 | n | medium | Label false: πολέες is not "the uncontracted form of πολλοί"; it is the epic plural of πολύς, a different stem from πολλοί. | Corrected. |
| 251 | n | medium | Label false: ἀρέσθαι belongs to ἄρνυμαι 'win, gain' (so the shipped glossary), not αἴρομαι. | Corrected. |
| 274 | n | medium | Note called βεβλήκειν "the plural pluperfect" while the glossary entry called it the singular with ν-movable; neither can be shown from the line (the subject is the distributive ἄλλος … ἄλλος). Note and glossary contradicted each other. | Note now says: the same pluperfect with a final ν, or else the plural ending -ειν; the glossary entry says the same. |

Checked and found true (no change): all other grammatical labels in the 53 notes, including the dual forms at 201, ὁμόκλεον, παραιπεπίθῃσιν, κτέωμεν/πεφήσεαι, ἥλω, the speech introductions and closings, and every cross-reference (2.268 and 206; 22.131 at 247, the shipped odyssey-107 unit 131; 255/265/272 ὀξέα δοῦρα; 256 ἱέμενοι; 257–258 = 274–275; 259 = 276; 242 and 277; 268 and 285; 202 and 281; 194 and 287; 20.299, shipped odyssey-101, ln 299; 1.6). The 7 speeches and their `mark`/`p` are unchanged and correct. l ↔ i, l ↔ note, and the repeats (257–258 = 274–275, 259 = 276) agree.

## Changes to gloss.json

Every one of the novel entries was read against each line it occurs in (all 94 forms occur; none is missing from `gloss.json`; no entry has a digit except person/number, a line number, "here", an ASCII apostrophe or backtick, or 230+ characters). The 16 `__broaden__` entries were compared with the shipped glossary: each is the old entry whole plus ` · ` and a new reading, as the runbook requires.

| Key | Severity | What was wrong | What was done |
|---|---|---|---|
| νίκην | medium | "Ionic -η (= Attic νίκην)" is false: νίκη is the same in Attic, and the form is not Ionic. | Label removed. |
| ἵστασο | medium | "epic -σο (= Attic ἵστασο)" is false: the form is identical in Attic and not epic. | Label removed. |
| ἔπεφνε | low | "ν-less (= ἔπεφνε(ν))" is a confused label (the ending -ε is the ordinary 3 sg.). | Removed. |
| ἀρήν | medium | "Ionic -ήν (= Attic ἀράν)" contradicts the entry's own "unrelated to ἀρή ’prayer’": Attic ἀράν is 'prayer, curse', a different word; and the bane word has no Attic equivalent. | Now "epic; a different word from ἀρή ’prayer’ (Attic ἀρά)". Not a joined homograph: at 208 ἄμυνον ἀρήν is 'ward off ruin' and the only reading in this form's occurrence is 'bane'; a joined entry would assert a second reading that the line does not have. The shipped key ἀρὴν (grave accent, other occurrence) is a different key and stands. |
| κτέωμεν | low | "epic short-stem form with -ωμεν (root aor. κτα-/κτε-)" did not name the Attic equivalent. | "epic κτέωμεν (= Attic κτάνωμεν)". |
| βεβλήκειν | medium | "3 sg., ν-movable" asserted what the line cannot show (see unit 274 above). | States both possibilities. |
| ἀφελώμεθα | low | "in a temporal clause with ἐπήν" pins the entry to the line. | Removed; "’we shall have taken away’" kept. |
| εὐπατερείῃ | low | "epithet of Helen" pins the entry to the line. | "epithet of a woman". |
| ἑτεραλκέα | low | Meaning given as certain; the note and the house treatment say the sense is disputed (conventions: disputed meaning says so). | "sense disputed" added. |
| ἀκοντίσατ | low | ’cast!’ against the house "hurl" used in `l`/`i` after pass 1. | ’hurl!’. |
| υἱοῦ | low | "(Attic υἱοῦ)" names an equivalent identical to the form. | Removed. |
| __broaden__ βίας | low | "of an army or household" is a guess about the use, and "might" is the house word for ἀλκή. | "’strength, force’ (ὑμέων βίας ’your strength’)". |
| __broaden__ εἰπεῖν | medium | "aor. inf. complementing a participle, ’to speak (big)’" is false: εἴκων is a participle and εἰπεῖν the infinitive standing for a prohibition after μή (pass 1's note on 287–289). | "aor. inf. as a prohibition after μή, ’never speak’". |
| __broaden__ πνείοντες | low | "(might)" against the house "strength" for μένος. | "(strength)". |
| __broaden__ τοῖσιν | low | The line also has ἐν … τοῖσιν 'among them', which the old "from/to them" does not cover. | That reading added before the neuter one. |
| __broaden__ ἄκρον | low | "masc./neut." asserted a gender for ἄκρον with ῥινόν that the line does not settle. | "adj. acc. sg. with ῥινόν". |

## Left as found, and why (existing glossary and refused findings)

| Item | Finding | Reason |
|---|---|---|
| ἔβη (shipped glossary) | The shipped entry says "root aorist, unaugmented (= ἔβη)": ἔβη has the augment, and "(= ἔβη)" equates the form with itself. It occurs at 249. | **Not changed.** `known-forms.json` carries it; the runbook says "Never rewrite an existing entry otherwise", and `__broaden__` can only add a reading (old entry whole), so it would keep the wrong word. The unit note at 249 is right. For the owner: the shipped entry should read "aor. 3 sg., root aorist (= Attic ἔβη); ἐ- is the augment". |
| ἀρήν (pass-1 observation) | Whether to join ἀρή 'prayer'. | Not joined (see the table above): the occurrence is 'bane' only. |
| ἐφέστασαν | Parse "aor. 3 pl., epic -στασαν" is not provable from the line (it could be read as a pluperfect with imperfect sense). | Kept: the shipped glossary has the same type (ἔσταν "aor. 3 pl., root aorist, intrans., epic"), the note says only 'a past tense', and the sense 'took their stand' is the same either way. |
| μεταμίξομεν | Lemma μεταμίγνυμι and "fut. 1 pl." not checkable against the line beyond the context (a future after the aorist subjunctive clause). | Kept; the entry already says the form is also a short-vowel aorist subjunctive. |
| χαλκοβάρεια | Lemma given as the feminine form itself, not a masculine headword. | Kept; the same practice stands for εὐπατέρεια, and no masculine form occurs in the part. |
| βλῆσθαι | "aor. inf. pass." | Refused again (pass 1): the form is a root-aorist infinitive of passive sense. |
| τὰ (broaden), γε left out of `l` at several lines, ἐπιτρέψαι, ἕλον, ἐάσομεν, δούρατ’, δαΐφρων, ποδὸς, ποτε, τοῦτό, τά, περί | Checked against the line; no fault found. | No change. |
| 283 (`i`) | "was hit by", i in the passive while `l` is active. | Refused: the `i` layer may recast the clause for English; the sense and the killers are the same. |
| 241 (`i`) "with him" after Polybus | Extra words not in the Greek. | Refused: harmless, the sense is of the six standing together. |

## Counts

Pass 2: **high 4 · medium 8 · low 11 = 23 changes** (units.json 7: high 4, medium 3; gloss.json 16: medium 5, low 11). Findings refused or left as found: 8 (the table above). Pass 1 + pass 2 together: high 24, medium 31, low 37 = 92 changes.
