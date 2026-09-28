# odyssey-028 (Odyssey 6.110–222) — review, pass 1

Checked: every note label, positional claim and cross-reference against the line; Greek to `l` word by word; `l` and `i` agreement; remembered English in `i`; quotation marks and `mark`; the flagged line 159 by hand. Mechanical checks all clean: `t` joined reproduces the packet's 113 lines exactly; one `\n` in `l` per `\n` in `t`; no `\n` in `i`; `ln` values right; the three repeated lines (6.112, 6.145, 6.213) carry the published English; every speech has “ on its first unit and ” on its last (119–126, 149–185, 187–197, 199–210, 218–222), with `mark` on each first unit, and no speech runs in from or out to a neighbouring part (odyssey-027 ends at 6.109 with the simile's closing line, no open quotation). `t` was never touched (checked by script). Only `units.json` was edited; `gloss.json` was not touched. Pass 2 still has to check `gloss.json`.

Severity: HIGH = false statement or breach of a fixed house rendering; MED = misleading or unsupported claim, or a real l/i/note disagreement; LOW = polish or precision.

## Changes made

| line · field | sev | what was wrong | what was done |
|---|---|---|---|
| 122 · l | LOW | "womanish" for θῆλυς: pejorative in English, and the note says 'female'. | "a female cry". |
| 125 · n | MED | "the voiceless-seeming nymphs" is unsupported; Odysseus has just heard the nymphs' cry, and nothing in the lines makes them voiceless. | "as against the nymphs he has just imagined". |
| 130 · l | LOW | ὑόμενος καὶ ἀήμενος are passive participles (the note says so), but `l` turned them into a noun phrase, "through rain and wind". | "who goes, rained on and blown on,". (`i` keeps "through rain and wind", a fair prose rendering.) |
| 136 · n | LOW | Note gave ἵκανε as imperfect "was coming upon", while `l` and `i` say "had come". | Note now says the imperfect of ἱκάνω 'come upon' is rendered 'had come upon (him)' because the clause gives a reason. |
| 139 · l, n | LOW | τῇ glossed 'in her', which doubled with ἐνὶ φρεσί 'in her mind' in `l` ("in her Athena … in her mind"). It is a dative of interest. | `l` "for to her Athena"; note "'to her'". |
| 148 · n | MED | Note said "The · introduces the speech", but line 148 ends in a full stop (t ends `μῦθον.`), not an ano teleia. False positional claim. | Note now says the full stop closes the sentence and the speech follows in the next unit. |
| 153 · l | HIGH | "thrice blessed" (twice) for τρὶς μάκαρες. The table (5.306) fixes `l` "Three times blessed" and lists "thrice blessed" among the renderings avoided on purpose. | "three times blessed" in both places. `i` already had it. |
| 158 · n | MED | `l` says "having outweighed **you**" (σε is the object of βρίσας), `i` says "outweighs his **rivals**", and the note only justified the second. The Greek does not name the rivals. | Note now states the grammar (object σε, literally "outweighed you", as `l`) and says "his rivals" is an interpretation. `l`, `i` and the new-renderings row left as drafted (see refused items). |
| 162 · n | LOW | "τοῖον … points forward to the comparison at 168": asserts more than the line shows. τοῖον is just "such (as she is)"; the correlative with ὡς is the τοῖον of 167. | Note now says τοῖον means the sapling was of the same kind as she is, with the comparison spelled out at 167–168. |
| 164 · n | MED | Label wrong: ἕσπετο called "unaugmented aorist … (Attic εἵπετο)". ἕσπετο is the aorist (Attic ἑσπόμην); εἵπετο is the Attic imperfect. | "ἕσπετο is the aorist of ἕπομαι 'follow' (Attic ἑσπόμην)". |
| 164 · n | LOW | "The aside says why he was at Delos": it does not say why. | "tells how he came to see the palm: he went to Delos too, with many followers". |
| 166 · n | LOW | ἀνήλυθεν glossed "has come up", but `l` and `i` have "had come up". | Note now says aorist 'came up', put in the pluperfect after ἐτεθήπεα. |
| 172 · n | LOW | "κάββαλε is κατέβαλε … with no augment" contradicts itself, and κατά loses its final vowel, not "its last syllable". | Rewritten: κατά + βάλε, final vowel lost, τ assimilated, no augment (= κατέβαλε). |
| 184 · i | LOW | ἄλγεα ("pains" in `l`, and the table's ἄλγεα πάσχων "suffering pains") rendered "grief" in `i`; "grief" is πένθος at 169 in the same speech. | "much pain to those who wish them ill". |
| 187 · n | MED | "what follows explains why she speaks kindly": not what follows. She turns to Zeus (188–190) and takes up the point again with a fresh ἐπεί at 191. | Note now says exactly that. |
| 190 · i | LOW | "these things too": `l` has no "too" and καί που is "and perhaps". | "too" removed. |
| 195 (l.197) · i | LOW | βίη rendered "strength" in `i` against "force" in `l`; "strength" is already `l` and `i` for ἀλκί at 130. | "the might and force of the Phaeacians". |
| 204 (l.205) · n | LOW | "at the edge of the world" is a claim about geography that these lines do not show (they show only isolation). | "'farthest' (of all peoples)". |
| 217 · n | LOW | "Odysseus's second speech" is a wrong count (soliloquy at 119, speech to Nausicaa at 149, this one is the third). | "Odysseus's last speech in this part". |
| 218 · l | LOW | `l` "while I myself" against the note and `i` "so that I may wash". | `l` "so that I myself". |
| 222 · i | MED | Same phrase κούρῃσιν ἐυπλοκάμοισι as 135 ("the fine-plaited girls") and 198 ("fine-plaited attendants"), but `i` gave "girls with such fine plaits". A stock epithet must be translated the same way each time, and "such" is not in the Greek. | "to be naked among the fine-plaited girls". |

## Flagged line 159

Hand scan of ὅς κέ σ’ ἐέδνοισι βρίσας οἶκόνδ’ ἀγάγηται: 14 syllables, so exactly two dactyls among feet 1–5; foot 1 ὅς κε σ’ἐ is a dactyl, and the second dactyl must be foot 5 (κόνδ’ ἀ γά), leaving spondees in feet 2, 3, 4 (ἐέδνοι · σι βρί · σας οἶ). The scanner's two scansions differ only in the open-vowel quantities of βρίσας and ἀγάγηται, and the alternative is impossible (it needs a short α in -σας and long α's in ἀγάγ-). Result: no licence is needed and nothing is metrically irregular beyond a run of three spondees, so **no metre sentence was added** (the convention mentions metre only where it explains a form).

## Findings considered and refused

- **119 · i "Oh me!" against the table's i "Oh me," (5.299 row).** Refused: the exclamation mark is punctuation only, in a speech opening where the table gives the wording, not the stop; `l` keeps the dash.
- **147 and 180 · i "angered in her heart" / "all that your own heart desires" for φρήν ("mind" in the note and `l`).** Refused: in prose, "heart" is the idiomatic English for both phrases; the note and `l` keep the Greek word's sense, and the fixed κατὰ φρένα καὶ κατὰ θυμόν is untouched.
- **168 · i "lady" for γύναι (l "woman").** Refused, but flagged for the lead: row 271 keeps "lady" for δέσποινα/πότνια, and γύναι is neither, so it is not a breach of the table's letter. "Woman" as an address would sound rude in English. If the lead wants the reservation kept strictly, the alternative is `i` "woman".
- **168 · i "such a trunk … as you, lady, whom I marvel at".** Refused (style): the construction is stiff but carries the Greek comparison; a rewrite would add words the Greek lacks.
- **158 · `i` "outweighs his rivals" / new-renderings row.** Refused a change to `l`/`i`; I only made the note honest. The drafter's reading (prevailing over other suitors by gifts) is the traditional one and "loading you with gifts" (the row's avoided rendering) would be worse. Lead should keep the row's wording in conventions but may want its "avoided" cell to add that the object of βρίσας is σε.
- **135, 222 · l "girls" against 122, 142, 147 "maidens/maiden" for κούρη.** Refused: κούρη is not a stock epithet with a house rendering, and the packet's own odyssey-027 line uses "maiden".
- **201 · i "bringing war" for δηιοτῆτα ("battle" in `l` and the note).** Refused: a fair prose equivalent; not a stock word.
- **127 · note "χροΐ is the uncontracted dative of χρώς".** Refused: the epic χροΐ (two syllables, printed χροῒ) is uncontracted against the Attic contracted forms; the label holds.
- **209 · note leaves ἐπί in ὅθ’ ἐπὶ σκέπας ἔστ’ unexplained.** Refused: an omission, not a false statement; the likely tmesis reading (= ἔπεστι) is not certain enough to assert.
- **198 · note glosses ἐύ- 'fine' in ἐυπλοκάμοισι, but 'fair' in ἐυώπιδα (113).** Refused: the table itself glosses ἐύ- both ways by word ('fair' in ἐυστέφανος, 'fine-plaited' fixed for Calypso).
- **155 (l.157) · `i` "so fine a young shoot" for τοιόνδε.** Refused: adds mild colour but no sense the Greek denies.
- **Remembered English in `i`.** Read every `i` for phrases that arrive ready-made; every one rebuilds from the case relations, and none was changed on that ground.
- **221 · note "ἄν with a future is unusual".** Refused: the note commits to 'future' for λοέσσομαι (it could be a short-vowel aorist subjunctive) but says the use is unusual, which is honest enough.

---

# Pass 2 — `gloss.json` and a re-check of `units.json`

Checked: all 197 novel entries and all 25 `__broaden__` entries (each broadened entry keeps the old one whole and its new part was read against the line it serves); every parse against the form as printed and the line it stands in, including the hedged ones (`πειρήσομαι`, `χρίσομαι`, `ἀπολούσομαι`, `λοέσσομαι`, `ἴδωμαι`, `ἔχουσ`, `διερὸς`); and the 380 known forms one by one for uses the existing entry does not cover. Mechanical checks all pass: every novel form is in this part and not yet in the glossary; nothing is missing; every entry is under 230 characters, has the `lemma — meaning; parse` shape and no ASCII apostrophe or backtick; every broadening contains the old entry whole (the ‘ marks in the `κῦμ` entry belong to the old text and are kept). `units.json` still tiles the edition exactly, `t` is untouched, and `l` line divisions, `i` single-line and `p` flags are all right after pass 1.

## Changes made in pass 2

| item | sev | what was wrong | what was done |
|---|---|---|---|
| gloss `φῶτα` (199) | HIGH | Parsed "masc. acc. pl.". φῶτα ἰδοῦσαι is one man (accusative singular of φώς; the plural is φῶτας). | "masc. acc. sg." |
| gloss `ἔγρετο` (117) | MED | Called a "root aorist"; ἔγρετο is a thematic 2nd aorist middle, and "= Attic ἠγέρθη" gave a form-equivalence that is only a sense-equivalence. | "2nd aorist, epic (sense of Attic ἠγέρθη)". |
| broaden `τοῖον` (162, 167) | MED | New part covered only "neut. acc. sg. agreeing with a neuter noun" (τοῖον … ἔρνος, 162). At 167 τοῖον agrees with δόρυ, the nominative subject of ἀνήλυθεν, which no reading covered. | Addition changed to "neut. nom./acc. sg. … τοῖον … ἔρνος (acc.), τοῖον … δόρυ (nom.) ’such a shoot, such a trunk’". |
| broaden `τί` (new, 179) | LOW | εἴ τί που εἴλυμα: τί is the enclitic indefinite used adjectivally with εἴλυμα; the old entry's adjective use is only a fragment ("· adj. ·"). | New broadening: old entry whole + "also the enclitic indefinite as an adjective agreeing with a noun, accented before enclitic που: εἴ τί που εἴλυμα ’if any wrapper’". |
| broaden `μήδεα` (129) | LOW | Typo "also also"; and "private parts" is the euphemism the table's row for μήδεα φωτός refuses (`i` "his genitals"). | "also the genitals (of the body): … ’the man’s genitals, about the skin’". |
| gloss `ἵκανε` (136) | LOW | "unaugmented": an initial ἱ- cannot show whether the augment is there (the augment would give ῑ), so the label is unverifiable; the "(= ἵκανεν)" adds nothing. | Now "impf. 3 sg."; and the unit note at 136, which I had rewritten in pass 1 with the same "unaugmented", now says "the imperfect of ἱκάνω". |
| gloss `πίσεα` (124) | LOW | "(= Attic πίση)": no such Attic form is known; the claim invents an equivalent. | "uncontracted -εα (contracted -η)". |
| gloss `ἀντιάσαντα` (193) | LOW | Omitted the genitive it governs (ὧν), which the unit note relies on; "come to (you)" adds an object the Greek lacks. | "meet, meet with, come by (+ gen.) … ’one who has met with’". |
| gloss `δείξειε` (144) | LOW | "indirect question … ’whether she might show’" against the note and `l` ("in case she might show"). | "after εἰ of hope: ’in case she might show’". |
| gloss `πυκινὸν` (134) | LOW | Example gloss "strong-built" against the note and `i` "solid". | ’solid’. |
| gloss `ὀρεσίτροφος` (130) | LOW | Only "mountain-bred", the rendering the table avoids on purpose. | "mountain-nurtured, mountain-bred". |
| gloss `νοήμασιν` (183) | LOW | "dat. of accord" is not a standard label; the dative is one of respect. | "dat. of respect: ’in thought’". |
| units 122 `i`, 123 `l`, 162 `l` | LOW | ASCII apostrophes in "woman's", "mountains'", "Apollo's", "palm-tree's"; every published Odyssey `l`/`i` uses ’. | Replaced by ’. |

## Findings considered and refused (pass 2)

- **`κάρηνα` "κάρηνον (pl. of κάρη)".** Refused: LSJ gives the plural κάρηνα both under κάρη and under a neuter κάρηνον; the entry says what the form is used for, and the unit note agrees with it.
- **`ἐυώπιδα` "fair-faced, bright-eyed" against the house "fair-eyed"; `ἐυπλοκάμοισι(ν)` "fair-tressed" against "fine-plaited".** Refused: glossary meanings give the dictionary sense, not the house English; the notes carry the house rendering.
- **`ἄνασσα` "queen, lady, mistress" against the reservation of "lady".** Refused: it is a dictionary gloss covering the range, and the entry's first word is "queen".
- **`ὠγυγίης` parsed as the adjective Ὀγύγιος.** Refused: νήσου ἀπ’ Ὠγυγίης is 'from the Ogygian isle'; the adjective reading is sound (the unit note calls it a genitive of the name Ὠγυγίη, which is the same word used as a noun elsewhere).
- **`ἄγαμαί`, `γουνοῦμαί`, `ἀμφιβαλέσθαι`, `ἤνωγον` (impf. of a perfect stem) and the other verb parses.** Read against the line and left: all correct.
- **Known forms not broadened, checked for uncovered uses:** all 380 read. The ones nearest the edge were `ὧν` (193, relative genitive plural neuter; the entry "of whom, whose … not the possessive" covers the relative, and the gender is not part of the parse); `τῇ` (139, "her, with her"); `ἐπί` (117, 'to a distance'); `ἦ` (all five uses covered); `νέον` (163, "young" is in the head-word); `ὥς` (122, 130, "or ὡς ’as’, accented before enclitic τε" covers ὥς τε); and `βασίλεια` (115, nominative, covered by the second reading). None needs broadening.
