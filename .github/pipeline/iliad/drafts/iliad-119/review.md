# Review, iliad-119 (18.310–409)

Two passes. Pass 1: notes, Greek to `l`, `l` to `i`, remembered English, quotation marks and marks, paragraph marks, line coverage, cross-references (every cited line and part checked against parts.json and the packet). Pass 2: `gloss.json` against the lines. `t` untouched throughout (checked by script before writing). Scansion: the packet flags none, so no metrical sentence was added.

Checked and sound: every `p` falls on a ¶ line (310, 324, 343, 360, 368, 388); every speech opens “ on its first unit and closes ” on its last (Achilles 324–342, Zeus 357–359, Hera 361–367, Charis 385–387 and 392, Hephaestus 394–409), each with `mark` on the first unit; iliad-118 ends with Hector's speech closed at 309, so 310 correctly opens in narrative; Odyssey and Iliad cross-references (8.542, 5.274, 1.551, 6.253, 4.58–61, Od. 8.437, 10.360, 10.367, Od. 5.91, 23.175–176, 1.590–594) all hold.

## Changes, pass 1 (units.json)

| Line | Field | Severity | Was wrong | Done |
|---|---|---|---|---|
| 323 | n | moderate | μετεφώνεε said to have "-εε for -εεν": false; it is the uncontracted imperfect (Attic μετεφώνει) | note corrected |
| 324 | i | minor | "surely" for ἦ ῥ’, which the note calls "truly" and the table renders "truly" (5.715) | "truly" |
| 326 | i | moderate | "For I said": the Greek has δέ, not γάρ, and `l` has "and" | "I said to him that I would take …" |
| 328 | n | minor | πάντα "in the middle of the clause": it stands just before the verb | reworded |
| 336 | n | minor | κταμένοιο called an "aorist passive participle": middle in form, passive in sense | reworded |
| 346 | n | minor | ἵστασαν glossed "were setting up" against `l`/`i` "set up" | "set up" |
| 346 | n | minor | ἑλόντες said to have the wood as "unstated" object; ξύλα is stated, shared with δαῖον | reworded |
| 349 | l, i, n | moderate | the flagged ἤνοπι χαλκῷ: Odyssey-048 has "bright bronze" but the Iliad table (16.408, published in iliad-103) has "gleaming bronze" and lists "bright" among the rejected words. Decision: the Iliad's own row governs (it is the older, written rule here, and the published Odyssey line is one occurrence) | "gleaming bronze" in `l` and `i`; note says the Odyssey has "bright bronze" and the Iliad's rendering is kept; the validator may warn on the difference from the Odyssey (expected); new-renderings.md row rewritten |
| 352 | n | minor | λεχέεσσι: epic plural of a single bier not said | added "here used of a single ‘bed’" |
| 352 | n | minor | ἑανός stated flatly as "fine, soft"; table says sense not certain | "fine", exact sense not certain |
| 354 | n | minor | "repeats the second half of 315": it repeats all of 315 but the first word | reworded |
| 361 | n | minor | (flagged) edition ends 361 with a full stop where published iliad-006 has ";". ποῖον makes it a direct question, `l` and `i` ask it, and both are word for word identical to the published unit, so the English has the same force | one sentence added to the note saying so; `l`/`i` unchanged |
| 362 | i | moderate | `l` "accomplish things for a man", `i` "carry things through with a man": different sense | `i` "accomplish things for a man" |
| 369 | n | moderate | κυλλοποδίων said to leave "the god himself unnamed"; Hephaestus is named in Ἡφαίστου two words earlier | note corrected |
| 382 | i | minor | "saw her as she came forward": "she" could be read as Thetis; προμολοῦσα agrees with Charis | "came forward and saw her" |
| 403 | n | minor | ᾔδεεν called an "imperfect" of οἶδα; it is a pluperfect in form with past sense | reworded |

new-renderings.md: only the ἤνοπι row changed. Everything else in it agrees with the units.

## Considered and refused (pass 1)

- 391 κέκλετο "called on" against the table's "gave orders to": kept. Charis names no command, there is an accusative object, and the table's own departure at 11.312 ("called on", an appeal between equals) is the precedent; it is listed in new-renderings.
- 356 προσέειπε "addressed / spoke to": matches the table rows (3.437, 6.440).
- ἦ ῥά νυ (357, 394): "truly then" and "truly (now)" are acceptable for the asseverative-ironic force; "can it be that" would be a different reading. Kept.
- 329 ἐρεῦσαι "redden": θ drops before σ (ἐρευθ-σαι), and the table's ἐρεύθων (11.394) is the same verb; blood left understood, as the note says.
- 341 καμόμεσθα: an aorist indicative middle, unaugmented, "toiled"; accepted (the gloss was wrong, see below).
- 341 `i` "our long spears" for singular δουρί μακρῷ: collective idiom in English, `l` keeps the singular; kept.
- 396 κυνώπιδος "dog-faced" / "shameless": follows the Odyssey-pair row (3.180, 4.145); kept.
- 400–401 κάλυκας "flower-cups", ἕλικας "spirals": the notes already say the forms are not known.
- 318–319 ἁρπάσῃ: aorist subjunctive in a simile rendered "has snatched"; acceptable English for the general aorist, the note names the construction.
- 396–397 `i` "because I was lame" for χωλὸν ἐόντα: causal sense is natural for the participle; `l` is literal.
- 338 τόφρα `l` "in the meantime" / `i` "Until then": same sense in context.
- 330 γέρων ἱππηλάτα "the formula the poet also gives Nestor": true (table 7.125).
- Scansion: no line flagged by the packet; none added.

## Pass 2: gloss.json (120 novel forms, 15 broadenings)

All 120 novel forms present, none extra; all broaden entries start with the existing entry whole; no ASCII quotes, all under 230 characters. Every parse checked against its line.

| Key | Severity | Was wrong | Done |
|---|---|---|---|
| καμόμεσθα | moderate | "aor. 2 subj. mid., short-vowel subjunctive, ‘we shall toil’": the sense is past ("toiled", with a dual participle sacking cities), and the note says aorist | "aor. 2 ind. mid. 1 pl., unaugmented, epic -μεσθα (= Attic ἐκαμόμεθα): ‘we toiled for’" |
| __broaden__ τώ | minor | adds "adv. (= τῷ): ‘therefore, so’", which the existing entry already has | entry removed from `__broaden__` |
| __broaden__ δεινή | minor | ‘awesome’ against the house "dread" | ‘dread’ |
| γάστρην | minor | "Ionic": the form is epic syncopated | corrected |
| θέρμετο | minor | ‘was growing hot’ for "grew warm" | ‘was growing warm’ |
| κτεριῶ | minor | ‘I will bury’, the rendering the table rejects | ‘I will give funeral rites to’ |
| ἁδινοῦ | minor | "vehement", rejected; house is "thronging" | "thronging, thick-set, close-packed" |
| ἀποδειροτομήσω | minor | "slaughter" asserted; meaning (throat or beheading) not settled | reworded |
| φῆν | minor | "uncontracted": it is unaugmented | corrected |
| ᾔδεεν | minor | ‘had known’ for "knew" | ‘knew’ |
| λιπαροκρήδεμνος | minor | "shining head-band or veil" against house "sleek head-veil" | "with sleek head-veil" |

Refused in gloss: ἐλαφηβόλος "deer-hunting" as a definition (lemma meaning, not the rendering); "aor. 1 sg." for ὄφελον/ἔκβαλον (the file's usual abbreviation, 1 = person); ἄμφεπε "play about" (dictionary gloss, harmless).
