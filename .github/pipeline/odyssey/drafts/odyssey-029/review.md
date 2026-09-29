# odyssey-029 — review of units.json (Odyssey 6.223–331), units pass

Reviewer pass 1 (notes, then Greek to `l`, `l` and `i`, remembered English, quotation marks and `mark`, hand-scan of flagged lines) and pass 2 (re-read of every edited unit against the Greek; structural gates of build_odyssey.py / validate_odyssey.py re-checked by a read-only mirror script: tiling, `ln`, `p`, `v`, `l` line count, no newline in `i`, no backtick, note band 20–130 words, quote balance, same-Greek repeats). `t` untouched (verified identical to the pre-review file, and to the edition by the tiling check). `title`, `titleEn`, `part`, `about` untouched. The gloss pass is still to come; items for it are listed at the end.

Severity: **major** = a false statement or a wrong sense that would mislead a reader; **moderate** = a note or rendering that is imprecise or drops something; **minor** = polish, consistency, remembered-English risk.

## Changes made (line · field · severity · what was wrong · what was done)

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 229 | n | major | Said τὸν μέν "has no matching δέ". κὰδ δέ in the next line is its δέ. | Now: τὸν μέν is balanced by κὰδ δέ in the next line. |
| 247 | n | major | Called κλύον **and ἐπίθοντο** unaugmented aorists. ἐπίθοντο (ἐ-πίθ-οντο, aorist middle of πείθομαι) carries its augment. | κλύον alone is called unaugmented; ἐπίθοντο is the aorist middle of πείθομαι. |
| 301 | i | major | "are nothing like it: such is the house of the hero Alcinous" — "it" has no referent, and the sentence says Alcinous' house is unlike the Phaeacian houses, of which it is one. The note (and l) read τοῖσι as the other houses. | "are nothing like other houses: such is the house of the hero Alcinous." |
| 303 | n | major | κεκύθωσι called a "perfect subjunctive" of κεύθω. It is the reduplicated aorist subjunctive (the perfect is κέκευθα). | Label corrected. |
| 307 | n | major | εἵατ’ called elided εἵατο and "perfect in form, present in sense". εἵατο would be a past tense, contradicting `l`/`i` ("sit"); the present is εἵαται (elided). | Now: elided εἵαται, epic 3 pl. of ἧμαι, 'they sit'. |
| 224 | l | moderate | "washed off his skin": makes χρόα the thing washed away. | "washed his skin … / of the brine that covered …" |
| 224 | i | moderate | "in the river" for ἐκ ποταμοῦ (out of / from the river); disagreed with `l` "from the river". | "with water from the river". |
| 224 | n | moderate | "ἀμφ- reduced before π" — there is no π after the word-start; the form is ἀμφέχω in its ἀμπ- shape. | "the ἀμφ- having become ἀμπ-". |
| 262 | n | moderate | "The ἐπήν clause never receives its verb": it has its verb (ἐπιβήομεν); what never arrives is the main clause. | "never receives its main clause". |
| 268–269 | n | moderate | Packet flag on 269 (UNRESOLVED), real on hand-scan: the line does not scan without treating the short final syllable of σπεῖρα as long at the main caesura (foot 3 longum). No sentence in the note. | Added one sentence: "Line 269 is metrically irregular as transmitted: the short final syllable of σπεῖρα has to be read long, at the main caesura, for the line to scan." (Note is 61 words, inside the band.) |
| 278 | l, i | moderate | που ("perhaps"), glossed in the note, was missing from both layers. | l "Either some wanderer, perhaps, she has taken in …"; i "Either she has perhaps taken in some wanderer …" |
| 286 | i | moderate | "I would blame … who did … who mingled … had come": νεμεσῶ is a present indicative and the subjunctives are general, so the conditional and past sequence changed the force and disagreed with `l`. | "I am indignant too at any other girl who does such things, who mingles with men … before a public wedding has come." |
| 325 | n | moderate | ἄκουσον and ἄκουσας both "taking the genitive μευ": ἄκουσας takes ῥαιομένου (μευ understood), as the note's next sentence half-says. | Rewritten to give each verb its genitive. |
| 330 | n | moderate | "These two lines repeat, from the middle of the first, a line of the poem's opening": unclear, and it hid that ἐπιζαφελῶς replaces ἀσπερχές. Checked against the edition: 1.20 (second half) and 1.21. | "Except that ἐπιζαφελῶς stands where ἀσπερχές stands there, the words repeat 1.20–21, from the middle of 1.20." |
| 227 | n | minor | Cross-reference "(6.214)": 6.214 has the maids lay out the clothes at Nausicaa's order given at 6.212–213. | "(see 6.212–214)". |
| 223 | i | minor | "a little way off": ἀπάνευθεν is 'apart, at a distance', with no "little". | "went apart" (as at 236). |
| 258 | n | minor | ἀπινύσσω "the word behind πεπνυμένος": derivation stated more strongly than the aids warrant. | "the root of πινυτός 'prudent', a word of the same family as πεπνυμένος". |
| 289 | n | minor | "ἐμέθεν is … (epic ἐμέθεν, with the -θεν suffix)": circular. | "the epic genitive of ἐγώ, 'from me' (Attic ἐμοῦ)". |
| 291 | i | minor | "Near the road" for κελεύθου; ὁδός is "road/way" elsewhere in this part (264, 261), κέλευθος is 'path'. | "Near the path". |
| 293 | l | minor | Own phrasing "a man, having shouted, makes himself heard" against the shipped wording for the same clause (ὅσσον τε γέγωνε βοήσας, odyssey-026 line 400: "as one shouting makes himself heard"). | Reused the shipped l. |
| 293 | i | minor | "a man’s shout carries": shipped i for the same clause is "as a man’s shout can carry". | "a man’s shout can carry". |
| 280 | l | minor | l "descending from heaven" beside "the wide sky" (243) and i "from the sky". | "descending from the sky". |
| 305 | l | minor | "a wonder to behold": a stock English phrase, and `i` has "to see". | "a wonder to see". |
| 308 | n | minor | "αὐτῇ … must mean the hearth or the queen": κίονι (a pillar, also feminine) is just as possible. | "may mean the hearth, the pillar or the queen". |
| 318 | i | minor | `i` identical to `l` ("and well they strode out"), not real prose. | "and they ran well, and strode out well with their feet;" |
| 318 | n | minor | "imperfect of τρώχω": the lemma is not certain and the 3 pl. -ων ending is not explained by it. | "an unaugmented imperfect 3 pl., 'they ran'" (lemma left to the glossary pass). |
| 319 | i | minor | "very carefully" for μάλα: adds "carefully", which is the sense of νόῳ later in the line. | "She drove well," (matches `l` "right well"). |

Totals: 27 rows, touching 30 unit fields on 25 units (lines 224, 293 and 278 have more than one field). By severity: **5 major, 9 moderate, 13 minor**. No finding remained open; none needed QUESTIONS.md.

## Checks that passed (no change)

- Every cross-reference in the notes was looked up in the edition: 6.209 (= 246), 6.218 (start of Odysseus's speech), 258, 291, 297, 299, 316, 280 (the ἤ answering ἦ at 278), 284 (end of the taunt), 1.2 (πλάγχθη). All true.
- Quotation marks: the neighbouring part (odyssey-028, last unit, line 221–222) closes Odysseus's speech with ”, so unit 223 opens no quotation. Speeches here: Nausicaa to the attendants (239–246; “ on 239, ” on 246), Nausicaa to Odysseus (255–315; “ on 255, ” on 315), the imagined taunt (276–284; ‘ on 276, ’ on 283, nested), Odysseus's prayer (324–327; “ on 324, ” on 327). `mark` sits on the first unit of each of these four (239, 255, 276, 324), and nowhere else. Counts: “ 3 / ” 3 in both layers.
- Paragraph marks `p` fall on 223, 239, 247, 251, 316, 328, as Murray prints.
- Repeated Greek: 6.328 (odyssey-012) l and i are identical to the shipped ones. 6.246, 6.315, 6.324, 6.331 sit in units of different extent, so the validator does not bind them; their l/i agree with the shipped wording line for line (checked against odyssey-028, 018, 021, 001). 258 is word for word odyssey-025 line 342, and l and i are identical to it. 247 keeps the row fixed for 3.477 with the feminine subject (new-renderings row). 243/6.242 "who hold the wide sky" matches odyssey-001 line 65. Half-line formulas (ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν, ὁ πῖνε καὶ ἦσθε, ὣς ἔφαθ’ αἱ δ’, ἀπάνευθε κιὼν ἐπὶ θῖνα θαλάσσης) agree with the house rows or shipped English.
- New-renderings rows all applied as written (247, 251, 252, 264, 264, 265, 266, 274, 242, 280, 319, 329, 330, 237, 297).
- Hand-scan of the flagged lines: **245** scans as a regular hexameter (ἐν-θά-δε | ναι-ε-τά | ων‖ καί | οἱ ἅ-δοι | αὐ-τό-θι | μίμ-νειν): the only licences are the digamma hiatus at καί οἱ (οἱ = ϝοι) and the ordinary epic correption of -οι in ἅδοι before αὐτόθι; the "ambiguity" is the unmarked quantity of the α of ἅδοι and does not change the line. Not irregular, so no sentence added to the note of 244–245. **269** is irregular (see table).

## Findings considered and refused (with reason)

- 245: adding a metrical sentence to the note. Refused: the irregularity is not real (above).
- 249 `i` "Then he drank and ate" for ἦ τοι: "Then" is a mild loss but the note gives 'indeed, truly' and the sequence reads correctly. Kept.
- 240 note "a way of saying that some god, at least, has willed it": an interpretation, but the standard one for οὐ πάντων ἀέκητι, and `l`/`i` are literal. Kept.
- 227 "πόρε … of πόρω": LSJ gives only the aorist, but naming πόρω as the dictionary form is how the aids list it. Kept; parse left to the glossary pass.
- 277 "εὗρε has no augment (Attic ηὗρε)": the usual description of the Homeric form. Kept.
- 242, 274, 280, 330 notes offering 'unsightly', 'insolent', 'much-invoked', 'vehemently' as glosses: the "avoided on purpose" words govern `l` and `i`, which use the table's word ("unseemly", "overweening", "much prayed to", "furiously") every time. Kept as lexical glosses.
- 274 note's remark that ὑπερφίαλος is not the word used for ὑπερηνορέοντες: checked against the table row for 6.5 ("overbearing"). True. Kept.
- 247 note "a stock way of saying that an order was carried out": true of the line's other occurrence (3.477, in the table). Kept.
- 283 `i` "so many and so good", 276 `i` "fine, tall": English intensifier and a compromise for καλός that the note itself explains. Kept.
- 270 `i` "care nothing for bow or quiver": checked for remembered English; ordinary collocation built from μέλει with οὐ, and `l` gives the literal. Kept.
- 301 "ἥρωος … 'the hero'": table row. Kept.
- 240–241 `l`/`i` "godlike Phaeacians" for ἀντιθέοισι: table ("godlike"). Kept.
- 308 accent on ὥς and 307 δμωαί/'maids' for δμῳαί: table reserves "maids" for δμῳαί; correct.
- Note word counts: all between 22 and 95 words (band 25–110 warns below 20 / above 130); 277 (22 words) and 277 (32) are short but complete; not padded.

## For the gloss pass (second pass over units.json, with gloss.json)

- εἵατ’ (307) must be parsed as εἵαται (present, 3 pl. of ἧμαι), not εἵατο.
- κεκύθωσι (303): reduplicated aorist subjunctive of κεύθω.
- ἐπίθοντο (247): aorist middle of πείθομαι, augmented; κλύον unaugmented (check the existing entries for κλύον and ἐπίθοντο cover both lines, 3rd pl.).
- τρώχων (318): 3 pl. imperfect; lemma to be settled (LSJ τρωχάω is the likely head).
- ἐμέθεν, ἄμπεχεν, ἀρίγνωτ’ (= ἀρίγνωτα, neut. pl.), εἰρύαται (perfect of ἐρύω, 'are drawn up'), ἐπιβήομεν (aorist subjunctive with diectasis of ἐπιβαίνω), κεκλιμένη vs κεκλημένος (two different verbs: κλίνω and καλέω) need care.
- ἥ (224) and ἥ (286, 287) are relatives; ἧς (278) and ἣν (262, 330) are the possessive ὅς in 278 and 330 but the relative in 262 (ἣν πέρι): keep apart.
- οἱ (224, 244, 307...) is a dative pronoun; ἡ (305) is a pronoun, not the article; τοί (242, 283, 321) is relative in 242 and 283, pronoun in 321.

## Pass 2 (glossary)

Checked all 171 entries in `gloss.json` (170 novel forms plus the `__broaden__` block of 18 forms) against the lines in `units.json`, from the Greek alone. Novel keys equal `novel-forms.json` exactly; every `__broaden__` entry begins with the known entry whole, byte for byte, then ` · `. Mechanical gates on all entries: no ASCII apostrophe, no backtick, no line numbers, no over-230-character novel entry (the six long entries are all broadened ones and are long only because the old entry is kept whole). Spot-checked the known forms the first pass flagged (κλύον, ἐπίθοντο, ἥ, ἧς, ἣν, οἱ, ἡ, τοί/τοὶ, ἐμέθεν, ἐρετμὰ, κλῦθί, ἄκουσας): existing entries cover their use here. Parses of εἵατ’ (εἵαται), κεκύθωσι, κεκλημένος/κεκλιμένη, ἐπιβήομεν, ἄμπεχεν and ἀρίγνωτ’ are correct as written.

| Form | Sev. | What was wrong | Done |
|---|---|---|---|
| τρώχων | moderate | Called "epic uncontracted -ων"; an uncontracted 3 pl. would be -αον, so the label was false for the lemma given. | Rewritten: unaugmented impf. 3 pl. (= ἔτρεχον); -ων would be contracted from -άον if from τρωχάω; lemma uncertain (τρωχάω, also τρώχω). |
| ἱκώμεθα | moderate | "short-vowel subj." is false: the mood vowel is ω (long). | Label removed. |
| ποῦ (`__broaden__`) | moderate | Example translated ποῦ δέ μιν εὗρε; as "where did he find her?"; μιν is the object (him), the finder is the subject (Nausicaa). | "and where did she find him?" (old entry untouched). |
| τούσδε | minor | Contained the word "here" ("this (here)"). | "(here)" removed. |
| εἰρύαται | minor | Named a non-existent Attic equivalent εἴρυνται. | "epic -αται (for -νται)". |
| εἶπον | minor | Parse "3 pl." only; the form is equally 1 sg. | "aor. 3 pl. (also 1 sg.; = ἔειπον)". |

Totals: 6 changes (0 major, 3 moderate, 3 minor).

Findings considered and refused:
- The word "here" inside the old ποῦ entry ("here in indirect use"): part of the existing entry, which may not be rewritten. Kept.
- Six broadened entries over 230 characters (αἱ, αὐτῇ, φίλον, ἐοικότα, ἐποιχομένη, ὅπως): old entry whole plus new reading is required, so the limit cannot apply. Kept.
- ἡγεμονεύσω "fut. 1 sg.": the form is also an aor. subj., but the main-clause use in the line is future. Kept.
- ἐρέεσθαι "pres. inf. (= Attic ἐρέσθαι)", νεῶν "(= epic νηῶν)", κατέχευε "(= Attic κατέχεεν)": conventional equivalents, not false. Kept.
- κεκλημένος 'called': the sense 'named my husband' fits the line. Kept.
