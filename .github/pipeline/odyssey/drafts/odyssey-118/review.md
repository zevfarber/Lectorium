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
