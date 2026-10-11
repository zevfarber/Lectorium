# odyssey-118 (24.327–437) — review, pass 1

Method: notes first (every label, every positional claim, every cross-reference, each note against its own `l`/`i`), then Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks, repeated lines against the published parts, hand check of flagged lines. Edits were made to `units.json` by script (exact-match replacement, one hit each); `t` was not touched. Afterwards the joined `t` was compared with `source/odyssey-murray1919.json` 24.327–437 and matches (5025 characters, same text), and `git diff` shows no `t` line changed. No modern translation was opened or recalled.

Counts of changes by severity: **high 1, medium 8, low 25** (34 in all; the `about` text counts as three). Three further low corrections were made to `new-renderings.md` (listed at the end). Findings refused: 14 (listed below).

Severity: high = the English says something the Greek does not or has the construction wrong; medium = a false grammatical or factual statement in a note, a house rendering not followed, or `l` and `i` out of agreement; low = wording, precision, small overstatement.

## Changes

| Line · unit | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 327 | n | low | Said αὖ is "the same particle as αὖτ’"; αὖτ’ is the elided αὖτε, a longer form. | Now says αὖ is the short form of the αὖτε (αὖτ’) found in other reply-lines. |
| 330 | n | medium | Called προσέφη "an unaugmented aorist". It has the augment (προσ- + ἔφη). The unit's own `l`/`i` were fine. | Now: "the past tense of πρόσφημι ‘speak to’, with its augment". |
| 331 | i | low | "look with your own eyes": "own" is not in the Greek. "a boar gave me" for ἔλασεν (struck) loses the blow. | "look with your eyes at this scar, which a boar dealt me on Parnassus". |
| 333 | l | low | σὺ δέ rendered without its δέ ("you sent me forth"). | "and you sent me forth". |
| 333 | i | medium | μητρὸς φίλον: "my mother’s father" drops φίλον (`l` has "dear one"). | "my mother’s dear father". |
| 333 | n | low | "the nearer subject σύ" is a positional claim that does not hold: σύ stands before the verb with δέ με between, πότνια μήτηρ follows it directly. Also said the noun was "understood from πατέρ’"; φίλον simply agrees with πατέρ’. | Rewritten: verb agrees with σύ, "lady mother" added after the verb; φίλον agrees with πατέρ’. |
| 336 | n | low | "an adjective Homer gives to houses and towns" is a claim about the poem beyond this part. | "an adjective this part also gives to a town (377)". |
| 338 | i | low | "told me what it was" adds content: ἔειπες ἕκαστα is "spoke each". | "named each one and told me of it". |
| 341 | i | low | ὧδ’ is "thus", not "in the same way" (an inference from the previous trees). | "And so you named for me fifty rows…". |
| 347 | n | low | Said Odysseus "is named only at the end of the sentence that follows"; he is also named at 346. | "named again at the end". |
| 347 (2nd unit) | n | low | "ποτὶ οἷ is πρὸς ἑαυτῷ, ‘to himself’": πρὸς with the dative is not the Attic form of this phrase and "to" misdescribes it. | "‘close to himself’, οἷ being the dative of the pronoun ἕ after ποτί". |
| 349 | l, i, n | medium | `l` "he addressed him" and `i` "spoke to him" supply an object that προσέειπε lacks, and the note itself says the speech is addressed first to Zeus. The note contradicted the `l`/`i`. | `l`: "he addressed (them):" (the table’s bracket style); `i`: "he answered and spoke again in these words:"; note says the "(them)" is the gods, addressed in the next line. Row in `new-renderings.md` corrected. |
| 349 | n | low | "ἄμπνυτο is ἀνέπνυτο": ἄμπνυτο is unaugmented, so it is not ἀνέπνυτο. | Now: aorist middle of ἀναπνέω, without augment, preverb shortened to ἀν- then ἀμ- before π. |
| 353 | l, i, n | high | ἀγγελίας: (1) the table fixes ἀγγελίη as "news" and lists "message" as withdrawn; (2) `i` "send messages urging on the cities" makes the cities the object of ἐποτρύνωσι, but πολίεσσι is a dative of destination and ἀγγελίας is the object. `l` was right in construction. | `l`: "and news everywhere speed on to the cities of the Cephallenians"; `i`: "and speed the news everywhere to the cities of the Cephallenians"; note rewritten to say object and dative. |
| 361 | n | low | "Attic would have plurals": Attic has duals too, though it seldom uses them. | "Attic would usually have plurals". |
| 365 | n | low | "a woman from Sicily" is more than Σικελή says; "returns to her at 389" assumes the identity of the two women. | "‘Sicel’, of the Sicels, a people of Sicily; a Sicel woman is named again at 389". |
| 370 | n | low | "usual ones for a hero who has been washed and dressed" is a claim about the rest of the poem this part cannot show. | Now says it is the English of an earlier shipped bath-and-dress line. |
| 371 | i | medium | ἄντην dropped in `i` ("looking like the immortal gods"); the house row for θεῷ ἐναλίγκιος ἄντην is "like a god to look upon". | "when he saw him, like the immortal gods to look upon". Row in `new-renderings.md` corrected. |
| 373 | n | low | "θῆκεν ἰδέσθαι ‘made (you) look’" is not the sense (made you better to look upon). | Corrected. |
| 386 | i | medium | ἀγχίμολον: the table’s `i` is "close by" (and lists "soon" as avoided); `i` had "close upon this", which reads as "soon after". | "and close by came old Dolius". |
| 386 | n | low | "οἱ μέν is answered by ἦλθ’": the answering particle is the δέ of ἀγχίμολον δέ. | Corrected. |
| 388 | n | medium | "the same Sicel woman as in 366" asserts an identity the Greek does not give (366 is an ἀμφίπολος, 389 a mother of sons). | Now says a Sicel woman has been named at 366 too and the text does not say whether she is the same. |
| 391 | i, n | low | `l` "amazed", `i` "stunned" for τεθηπότες. | `i` and note: "amazed" (also matches θάμβος at 394). |
| 394 | i | low | `l` "forget", `i` "put away" for ἀπεκλελάθεσθε. | `i`: "forget your amazement". |
| 407 (2nd unit) | n | medium | "has nothing to do with the adjective πένης ‘poor’" is false: πένομαι "toil" and πένης are related. | Replaced by "not ‘be poor’". |
| 417 | n | low | οἴκων (plural) was rendered "the house" in `l`/`i` without comment. | Note now says it is a plural for the one house. |
| 429 | i | low | ἢ καὶ ἐς Ἤλιδα: `i` lost "even" that `l` has. | "or even heavenly Elis". |
| 433 | l, i | medium | ἐσσομένοισι: the table (11.76) fixes "those to come" / "those yet to come" and lists "future generations" as avoided; `i` used the avoided phrase, `l` had "those yet to be". | `l`: "even for those to come"; `i`: "even for those yet to come". |
| 433 | i | low | "For this will be an outrage": ἐστί is present. | "For this is an outrage". |
| 437 | i | low | μὴ φθέωσι is a fear clause; "or those men will cross over" asserts it as fact. | "or else those men may cross over and get ahead of us.”" |
| 437 | n | low | "‘cross over’, that is the sea" states as fact what the Greek leaves implicit. | "presumably the sea, on the way to Pylos or Elis". |
| about | text | low | (a) "Laertes thanks the gods": his lines 351–352 are half-doubt, not thanks. (b) "the old Sicel woman bathes Laertes" asserts the identity above. (c) "before Odysseus can escape across the sea" overstates περαιωθέντες. | (a) "calls on Zeus and the gods"; (b) "a Sicel handmaid bathes Laertes"; (c) "before Odysseus can get away to Pylos or Elis". |

Corrections to `new-renderings.md` (to match the unit changes): the ἐξαῦτις row (new `l`/`i` and a sentence on the missing object); the ἀθανάτοισι θεοῖς ἐναλίγκιον ἄντην row (`i` now "like the immortal gods to look upon", "looking like" added to the avoided column); the ἀμφίπολος Σικελή row, which said ἀμφίπολος is "handmaid" in the table. The table has "attendants" for the plural; the shipped singular is "handmaid" in odyssey-002, -004, -015 and "attendant" in odyssey-113. The row now states this accurately.

## Quotation marks and the end of the part

- Preceding unit: odyssey-117's last unit (ln 325, which contains 326) ends with ” and says the speech begun at 321 closes there. Line 327 is narration, so unit 1 correctly has no opening mark and no `mark`.
- Source line 438 (`source/odyssey-murray1919.json`) is `ὣς φάτο δάκρυ χέων, οἶκτος δ’ ἕλε πάντας Ἀχαιούς.` with Murray’s paragraph mark. It is narration (ὣς φάτο, "so he spoke") and closes Eupeithes’s speech. The drafter’s assumption that the speech ends at 437 is therefore right, and the ” on the last unit (437) stands. **odyssey-119 opens in narration at 438, not mid-speech**: its first unit needs no opening quote and no `mark`.
- All speeches in this part open with “ on the first unit and close with ” on the last, with nothing inside: Laertes 328–329 (one unit); Odysseus 331–344 (units at 331…343); Laertes 351–355; Odysseus 357–359/360; Odysseus 373–374; Laertes 376–382; Odysseus 394–396; Dolius 400–405 (the unit at 400 ends without ”, the unit at 403 closes); Odysseus 407 (two units, closed at the second); Eupeithes 426–437. Every `mark` is on the first unit of a speech and names the right speaker, and every `p` agrees with Murray’s ¶ lines.

## Repeated lines

All whole-unit repeats (330, 356, 406 reply formula; 357; 372; 383; 399; 412) were compared with the published English by script and are identical (the 383 unit keeps its published semicolon). Line-level repeats inside larger units (368, 376, 384–385, 403, 408 with Dolius for "the swineherd", 420–421, 431) follow the published words.

## Findings considered and refused

1. 329 πεποίθω: `l` "trust", `i` "be convinced". Refused: the note gives both senses, `i` is the sense in context, and "trust" with no object would be worse English.
2. 383 `l`/`i` end with a semicolon where the Greek has a full stop. Refused: the semicolon is the published English of this line, and the validator requires it to match.
3. 421 `l` "before them" against `i` "among them" for τοῖσιν. Refused: both are legitimate for the dative of the assembled, and the Greek has μετέειπε "spoke among" right after; no house row fixes it.
4. 392 `i` "spoke to them, addressing them directly" double-renders προσέειπεν and καθαπτόμενος. Refused: the table gives "addressing him directly" for the pair; the drafter’s version keeps both verbs and loses nothing.
5. 381 `i` omits ἄνδρας ("the men, the suitors"). Refused: apposition, no difference in sense in English.
6. 345 `i` "at once" for αὐτοῦ, though the note calls it the adverb "on the spot". Refused: it follows the shipped odyssey-020/-113 pair; odyssey-106 has "on the spot", so the shipped parts themselves differ (not this part’s fault).
7. 413 `l` "a messenger" against `i` "the messenger". Refused: ἄγγελος is predicative; both fit.
8. 415 `i` "all who heard it" for ὁμῶς ἀΐοντες. Refused: "alike" is carried by "all".
9. 432 `i` "for ever" against `l` "always". Refused: both render αἰεί.
10. 409 `i` "crowded round" for ἀμφί. Refused: gloss on the scene, not a change of sense.
11. 351 note cross-reference to 1.7 for ἀτάσθαλον / ἀτασθαλίαι. Checked: line 1.7 has ἀτασθαλίῃσιν, so the reference is true; kept.
12. 426 note that "Achaeans" includes the Cephallenians. Kept: it is interpretation but is marked as Eupeithes’s usage and cites 429.
13. 351 `l` "long Olympus" against `i` "tall Olympus": matches the shipped odyssey-048.
14. Scansion flags: the packet lists none, so no line was scanned by hand and no metre sentence was added.

## Unresolved

- The house table and the shipped parts disagree on the singular ἀμφίπολος ("handmaid" in -002, -004, -015; "attendant" in -113; the table row for the plural is "attendants" and lists "handmaidens" as avoided). This part follows the majority singular "handmaid"; the owner may want one rule. Nothing here blocks the build.
- Whether the Sicel handmaid of 366 is the old Sicel woman of 389 (and 24.211) is left open in the notes, as the Greek leaves it open.
- `gloss.json` does not exist yet, so the glossary parses are for pass 2.


# Pass 2

Method: the whole review was re-run on the current `units.json` (notes first, then Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, repeats), and every parse in `gloss.json` (all 95 novel entries and all 12 `__broaden__` entries) was checked against its line(s). The known-forms list (459 entries) was also read against the part for uses the existing entries do not cover. `units.json` and `gloss.json` were edited in place by script (exact-match, one hit each); `t` was compared before and after and is unchanged (64 units). Every novel entry is under 230 characters (longest 139), none has an ASCII apostrophe or a backtick, and every broadened entry begins with the existing glossary entry whole. No modern translation was opened or recalled; metre was checked with `scan_hexameter.py`.

Counts of changes by severity: **high 0, medium 8, low 23** (31 in all: 17 in `units.json`, 14 in `gloss.json`). `new-renderings.md` needed no change (no rendering in it altered; the two `l` changes below are not rows of it). Findings refused or left: 9.

## Changes to units.json

| Line · unit | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 328 | n | medium | Quoted "εἰ μὲν δή γε", but γε stands after Ὀδυσεύς in the line; and called Ὀδυσεύς a "predicate", though it is a nominative in apposition (with ἐμὸς πάϊς) to the "you" inside ἱκάνεις. | Quotes εἰ μὲν δή; says Ὀδυσεύς (γε stressing it) and ἐμὸς πάϊς are in apposition to the subject of ἱκάνεις. |
| 328 | n | low | πεποίθω "the perfect subjunctive of πείθομαι": the perfect is πέποιθα. | "subjunctive of the perfect πέποιθα (middle πείθομαι)". |
| 338 | l | low | "told me each": the Greek has no pronoun. | "you named and told each." |
| 341 | n | low | Reported two "usual guesses" for διατρύγιος (a claim about scholarship that cannot be checked here). | Removed; keeps "uncertain" and the build from διά + τρύγη. |
| 347 (1st unit) | n | low | "Attic ἔβαλε" for the tmesis compound. | "Attic ἀμφέβαλε" (as at 367). |
| 347 (2nd unit) | n | low | Pass 1 had written "close to himself"; "close" is not in ποτί, and `l`/`i` say "toward"/"to himself". | "‘to himself’, οἷ the third-person pronoun (here reflexive) after ποτί, the epic form of πρός". |
| 353 | n | low | "the Κεφαλλῆνες are the wider people to whom they belong": the lines do not say the Ithacans belong to them. | "named again at 377 and 429". |
| 362 | n | medium | Called ἵκοντο "an unaugmented aorist". The scanner needs the ι long in this line, which the known-forms entry for ἵκοντο gives as the sign of the augmented form. | "a past tense of ἱκνέομαι; the metre makes its first syllable long here, so it may well be augmented (the spelling cannot show it)". Hedged because a long ι also belongs to the present stem ἵκω, so this is not certain. |
| 367 (2nd unit) | n | low | "θῆκεν ἰδέσθαι is ‘made him (to look)’": garbled, the same fault pass 1 corrected at 373. | "‘made (him taller and stouter) to look upon’, the infinitive of respect". |
| 372 | n | low | "the speech-introduction formula for Odysseus" implies the line belongs to him alone. | "the winged-words speech-introduction; here the speaker is Odysseus". |
| 379 | n | low | ἐφεστάμεναι given as "the infinitive of ἐφίστημι", tense not stated. | "the epic perfect infinitive (Attic ἐφεστάναι) … ‘stand by’". The -άμεναι form with short α is the perfect (aorist would be ἐπιστῆναι / epic -στήμεναι). |
| 394 | n | medium | Said Odysseus speaks "to Dolius and through him to his sons" (an assertion), gave no parse, and left ἀπεκλελάθεσθε unanalysed. | Parse stated (reduplicated aorist middle of ἐκλανθάνομαι with an extra preverb ἀπο-, force unknown; imperative because it is coordinate with ἵζ’ and has no augment); the plural takes in the sons, who all stand amazed at 391. |
| 415 | n | low | ἀΐοντες called "uncontracted"; ἀΐω has no contracted form. | "the participle of ἀΐω ‘hear’ (Attic ἀκούω)". |
| 417 | n | low | ἕκαστοι "the men of each family" stated as fact. | "‘each party’ (presumably the kin of each dead man)". |
| 417 | n | low | "handed to the fishermen who sail them" overstates ἁλιεῦσι. | "presumably handed to the fishermen to be carried". |
| 421 | l, n | low | `l` "before them" for τοῖσιν δ’ … μετέειπε; the published odyssey-033 (same shape, Alcinous) has "to them". | `l` "to them Eupeithes up stood and spoke among them:"; note "‘to them’, the assembly; μετέειπε adds ‘among’". |
| 423 | n | low | "some ancient readers took it as ‘unbearable’": cannot be checked from the repository or the Greek. | "traditionally ‘not to be forgotten’ (as if from λανθάνομαι), and its root is uncertain". |

## Changes to gloss.json

Settling the doubts:

- **ἀπεκλελάθεσθε.** Parsed from the grammar: ἀπ(ο)-ἐκ-λε-λάθ-εσθε. The reduplicated stem -λελαθ- with the thematic ending -εσθε is the reduplicated second aorist, as in ἐκλελάθοιτο and ἐκλελάθωντ’ already in the glossary under ἐκλανθάνομαι. It is not a perfect middle (that would be -λέλησθε, cf. the shipped λελασμένος). There is no augment, and it is coordinate with the imperative ἵζ’, so the mood is imperative; an aorist indicative would have shown an augment after the preverbs. The glosser's lemma "ἀπεκλανθάνομαι" is not one I can confirm; the entry now uses ἐκλανθάνομαι and says the force of the further ἀπο- is unknown. (Entry: "ἐκλανθάνομαι (with a further preverb ἀπο-, force unknown) — forget utterly (+ gen.); reduplicated aor. imper. mid. 2 pl.")
- **ἐφεστάμεναι.** Perfect infinitive, intransitive ("stand by"): the short-α -άμεναι form is the perfect (cf. the shipped ἐφεστάμεν "perf. inf."), Attic ἐφεστάναι. The glosser had no tense.
- **οὖλέ.** The glosser's lemma "οὖλος / οὔλω" named a verb I cannot confirm. Rewritten as οὖλος (?) with "a greeting ‘be well’", saying that it is unknown whether the form is an imperative of a verb ‘be hale’ or the vocative of the adjective, and that the lemma is unknown. The adjective is already in the glossary (οὖλον "whole, entire").
- **προΐεις.** Left unchanged: imperfect 2 sg. of προΐημι is right (a past narrative; the Attic imperfect 2 sg. is the same form; compare the shipped προΐειν, προΐει).

| Key | Sev. | What was wrong | What was done |
|---|---|---|---|
| ἀπεκλελάθεσθε | medium | Unconfirmable lemma; "aor. 2 imper." without saying why. | See above. |
| ἐφεστάμεναι | medium | No tense. | "perf. inf." |
| οὖλέ | medium | Invented a verb lemma; claimed more than is known. | See above. |
| φθέωσι | medium | "= Attic φθάσωσι": that is the sigmatic aorist; φθέωσι is the epic subjunctive of the root aorist ἔφθην (Attic φθῶσι). | "root aor. subj. 3 pl., epic uncontracted (= Attic φθῶσι)". |
| δολίος (broaden) | medium | The known entry gives only "Dolius, father of Melantho"; this part uses the nominative of the old Dolius who comes in with his sons (386, 397, 408). | Broadened: old entry whole + " · also the old Dolius who comes in from the fields with his sons and greets Odysseus (the household slave of Δολίον); masc. nom. sg." |
| ἀναγνόντος | low | "(gen. absolute)": the participle agrees with the genitive τοῦ of the previous clause, as the note says. | "agreeing with τοῦ ’his’". |
| νόστησας | low | The form has no augment; entry said nothing. | "unaugmented (= ἐνόστησας)". |
| τεθηπότες | low | Gave a present θήπω that cannot be confirmed. | Lemma τέθηπα, "no present in use". |
| πεποίθω | low | Filed under the middle πείθομαι only. | πείθω, perf. πέποιθα (mid. πείθομαι). |
| σικελή | low | "agreeing with ἀμφίπολος and γρηῦς": only γρηῦς is in this form's line (the other is the grave-accent key). | "agreeing with a noun (γρηῦς)". |
| ἐϋκτιμένην | low | "here of tilled ground": "here" and a line pin. | "said of a town or house, and of a tilled plot". |
| νήρικον | low | "a town on a headland" says more than the line. | "a fortified place on the mainland coast (called a ’headland of the mainland’)". |
| ποτὶ (broaden) | low | Known entry has + dat. only ’against’ and ’on’; the line has ποτὶ οἷ "to himself". | Broadened: old entry whole + " · also + dat., ’to’ a person: ποτὶ οἷ ’to himself’". |
| ὁππότε (broaden) | low | Known entry has + opt. only of what may happen in time to come; the part has it of what recurs. | Broadened: old entry whole + " · also + opt., of what recurs: ’whenever’ (ὁππότε … ἐπιβρίσειαν ’whenever … press down’)". |

Every other novel entry was checked against its line and left (including δώσειν, ζωέμεν, θάμβευς, κάλεσσεν, κερῶντάς, μολών, ὀδυσεῦς "gen. sg., single σ", ἐγήθεις, ἐπιβρίσειαν, ὄσσα). All twelve glosser broadenings were checked: each begins with the existing entry whole and the added reading is the one the line needs (εἷλον, μεγαλήτορα, πάρος, περὶ, τί, φράσαι, ἀλλάων, ἀνὰ, ἂν, ἐϋκτίμενον, ἡδὺ, ἰδέσθαι); they exceed 230 characters only because the old entry must be kept whole.

## Findings considered and refused or left

1. Broadened entries over 230 characters (πάρος 505, περὶ 1038, τί 1409 …): left, because the rule is "old entry whole, plus ‘ · ’ and the new reading"; the 230 limit was applied to the novel entries.
2. The old entry for ἰδέσθαι, kept whole inside its broadening, uses ‘ ’ rather than ’ ’: not rewritten, since existing entries are never rewritten.
3. 333 `l` "my mother’s dear one" for μητρὸς φίλον (noun-like where φίλον agrees with πατέρ’): left; the note and `i` ("my mother’s dear father") are right and `l` reads as an apposition.
4. 400 `i` "who longed for it so much": the Greek has no object for ἐελδομένοισι; left as natural English (the same as `l` "longing very much").
5. Spondaic-fifth flags: `scan_hexameter.py` reports "spondaic fifth" (not UNRESOLVED) at 327, 331 and 405; the packet lists no flagged line and no note was added, since the scanner explains each as a licence it has fitted.
6. 345 `l` "and then" for αὐτοῦ against `i` "at once": a published-formula difference left as in pass 1.
7. Quotation marks re-checked: every opening “ is on a first unit with a `mark`, every ” on a last unit, none inside a speech; units 1, 28 and 45/46 are one-unit or two-unit speeches; the closing ” at 437 stands (see pass 1: line 438 is narration).
8. Repeated lines re-run against all published parts by normalised text: the whole-unit repeats (330, 356, 406, 357, 372) are identical; line-level repeats (367–368, 383, 384–385, 412, 421, 403, 408) follow the published wording, except 421 `l`, now corrected.
9. 427 `i` "led away" for ἄγων: left; "away" is the sense of leading a force out to war and no extra claim is made.

## Unresolved

- Whether ἵκοντο (362) is augmented cannot be decided from the spelling; the note now says the metre makes the first syllable long and that the form may be augmented.
- The force of ἀπο- in ἀπεκλελάθεσθε and the form and lemma of οὖλε remain unknown and are labelled so in the notes and the glossary.
