# aeneid-028 (IV.408–503): reviewer's record

Two passes. (1) Every grammatical label checked against its form and its line. (2) Latin against `l` word by word, `l` against
`i`, line division of `l` against `t`, `i` for echoes of remembered English versions, speech marks, and every claim in a note
that is not read off the Latin. For scansion I read all 96 lines against the scanner's printout (`scan_latin.scan_line` on each
line, not `build_aeneid.py`), not only the flagged ones. `units.json` was edited by script; the script asserted that `t`, `ln`,
`p` and `v` are unchanged and that every `l` has the same number of lines as its `t`. `draft.py` was then regenerated from
`units.json` and `make_units.py` run from it reproduces `units.json` byte for byte (do not restore the old `draft.py`). No
modern translation was consulted.

Counts: units/notes **major 4, medium 14, low 35**; scansion **major 4, medium 1, low 1**.
Overall **major 8, medium 15, low 36**.

## Speech marks (checked, no change needed)
“ opens unit 4 (416, Dido to Anna) and unit 42 (478, Dido to Anna); ” closes unit 19 (436) and unit 50 (498). `l` and `i`
carry the same marks on the same units as the printed `t`; no other unit carries a mark. (The task brief calls the first
speech "Anna's speech"; it is Dido's speech to Anna, and two notes said so wrongly: see below.)

## Units: major
- **1 (409–411) `n`.** "'fervere' is the verb that closed the ant simile ('fervet opus')": the simile ends at 407 with
  `opere omnis semita fervet`, not `fervet opus`. Now "recalls the ants' path in the simile just before, which 'fervet' (407)".
- **4 (416) `n`.** "Anna's speech opens here": the speaker is Dido; Anna is the addressee. Now "Dido's speech to Anna".
- **19 (436) `n`.** Same error at the close ("Anna's speech ends here"). Now "Dido's speech to Anna ends here".
- **24 (443–444) `n`.** "'stridor' is a fourth-declension noun": it is third declension (`stridor, -oris`). Corrected.

## Units: medium
- **1 `l`.** `quosve`: the note says `-ve` is 'or', `l` began "And what groans". Now "Or what groans".
- **8 (420) `n`.** "'miserae' … agreeing with 'mihi' two words later": `mihi` is the last word of the sentence (Anna comes between),
  not two words later. Rewritten. Also the gloss of `tamen` ("even though she cannot stop him") invented a reason; now "she
  says she will bear the blow, but still asks this", which is what the preceding `potero` gives.
- **10 (423) `i`.** "when he was gentle" moved `mollis` onto the man. `mollis` agrees with `aditus` (`l` and the note say
  so). Now "the gentle ways of approaching the man, and the right moments".
- **15 (430) `n`.** `facilem` was glossed 'favourable' while `l` has 'easy' and `i` 'smooth'. Now "'easy', here a smooth,
  untroubled passage".
- **17 (433–434) `n`.** "'me victam' is a double accusative": `doceat` takes the person (`me victam`) and the thing taught, the
  infinitive `dolere`; `me victam` is one object, not a double accusative. Rewritten.
- **22 (440) `n`.** "the divine will that Mercury brought. So Virgil makes it Aeneas's duty rather than his hardness of
  heart" is an interpretation stated as fact. Now hedged: "the reader may think of the divine order Mercury brought. The line
  puts the cause in fate and a god, not in Aeneas's own hardness of heart."
- **23 (441–443) `n`.** "a type of Homeric simile (… as in Iliad 16)": a Homeric parallel I could not pin from the Latin;
  removed. Now "an epic simile: winds struggling over a tree".
- **24 `n`.** "'altae… frondes' encloses 'terram': the high leaves lie on the ground, in the word order too" was false (the pair
  frames the whole clause, and the word order does not show leaves on the ground). Now "frames the rest of the clause".
- **34 (460–461) `n`.** "'obscura' is a predicate adjective": it agrees with `nox`; rewritten as "agrees with 'nox'".
- **40 (471–473) `n`.** "(Aeschylus' Eumenides; Euripides' tragedies on the story too)": parallels not read off the Latin;
  replaced by "a story the Greek tragedians put on the stage".
- **41 (474–477) `n`.** "a chiasmus-like pair": `consilium voltu tegit, spem fronte serenat` runs object–ablative–verb,
  object–ablative–verb, which is parallel, not crossed. Now "a matched pair".
- **43 (480–482) `n`.** "whom Homer too puts at the world's edge": Homeric parallel, removed. "'aptum' is a perfect participle":
  it is the adjective `aptus` (fitted), construed with the ablative; rewritten.
- **49 (494–497) `n`.** "'secreta' is a feminine nominative agreeing with 'Tu'" is only one of two readings (it can also be
  an adverbial neuter plural). Now "most likely agrees with 'Tu' … could also be read as an adverbial neuter plural".

## Units: low
- 0 `i`: "What did you feel then, Dido, as you looked on such a sight?" is close to a remembered standard rendering; now "Dido, what
  passed through your heart then, as you beheld such things?".
- 2 `n`: `improbus` glossed "without measure, unrestrained"; now "shameless, wicked … relentless". 2 `i`: "to what will you not
  drive the hearts of mortals?" echoes a familiar version; now "what is there that you do not force mortal hearts to do?".
- 5 `n`: "it ends the line it opens on" (nonsense) → "it closes line 416".
- 6 `i`: "the canvas is calling for the breeze" (a familiar phrase) → "the sails are already beckoning the breezes". 6 `n`:
  `et` glossed 'also' while `l` has 'and'; now "joins this clause to the last and stands second in its own clause". "Garlands on
  the ships are a mark of departure" → "suggest a departure at sea" (hedged).
- 10 `n`: "anaphora" for `sola… solam` (two lines apart, different cases) → "the same word repeated".
- 12 `l`: `classemve` rendered "nor a fleet"; `-ve` is 'or' (as `Manisve` was already) → "or a fleet". 12 `i`: `Manis`
  (plural 'spirits') rendered "the spirit"; now "the shade of his father Anchises".
- 14 `l`: "as a gift" left `munus` out of the object; now "This last gift, to the wretched woman in love, let him give:", which
  matches the note ("Extremum hoc… munus encloses the verb").
- 16 `n`: "'pulchro' is bitter: she concedes him his Italy" → "may be bitter: she grants him his fair Italy".
- 17 `i`: "I ask only for" added 'only' → "I ask for".
- 23 `n`: "'robur' is the hard heart of the oak" → "oak-timber, the hard wood".
- 24 `n`: ant column "goes" at 405 → 404 (`it nigrum campis agmen`).
- 25 `n`: "Virgil is reusing his own lines on the tree from Georgics 2" kept in substance (I am sure of the passage, a tree whose
  top reaches the sky as far as its root reaches Tartarus) but hedged to "had written almost these words of a tree in Georgics
  2", no line number. "'haeret scopulis' is a dative" → either a dative after `haereo` or an ablative of place.
- 28 `n`: "readers have divided over it" → "the line leaves it open". 28 `l`: "roll down" → "roll" (`volvuntur` has no 'down').
- 31 `n`: "(poetic plural)" for `latices` removed (`latex, -icis` is plural normally). 31 `i`: "a thing dreadful to tell" (a stock
  English tag) → "a horror to speak of".
- 33 `n`: `velleribus` glossed "woollen fillets"; `l` has 'fleeces' → "snow-white fleeces (strips of wool)".
- 34 `n`: "This is the ghost of Sychaeus summoning her" → "The voice she hears is her dead husband Sychaeus calling." 34 `l`:
  "seemed those of her husband" made `viri` a predicate; `viri` goes with `vocantis` → "seemed, of her husband,".
- 36 `n`: "The two phrases" for the one genitive phrase `vatum… priorum` → "The genitive phrase … is split around 'praedicta'".
- 37 `n`: "Dido's picture of him, not the poet's judgement" → "how the dream shows him, not necessarily the poet's verdict".
- 39 `n`: "The Furies belong in Greek tragedy to Orestes, not Pentheus" → "In Greek tragedy the Furies pursue Orestes…". 39 `l`:
  "and double itself to show Thebes" read `duplicis` as a verb; now "and, double, to show themselves Thebes".
- 40 `i`: "driven across the stage" ('across' is not in `scaenis agitatus`) → "driven on the stage".
- 48 `i`: "your own sweet life" for `dulce caput`, where the note says 'head for the person' → "your own dear self".
- 49 `i` and `about`: "the inner court of the house" (`tecto interiore` is only 'the inner part of the house') → "inner part of the house";
  the same fix in the part summary.
- 50 `n`: "Every word can be read two ways" (overstated) → "Her words can be read two ways".
- 51 `n`: "A short closing line like this is Virgil's usual way to close a speech" (a generalisation I cannot verify) → "A short line
  of narration like this closes the speech."
- 53 `i`: "strange new rites" ('strange' is not in `novis`) → "new rites".
- 54 `n`: kept the claim that 503 is a half-line because it can be checked from the Latin (`ergo iussa parat` is six syllables, and a
  hexameter needs at least twelve) and from `scan-fixes.json` (4.361 and 4.400 are the same kind); added that reason, and
  replaced "the quiet irony that Anna builds the pyre" (not in these lines) by "Anna doing as she is told, not knowing what it is for".

## Refused findings (checked, left as they were)
- 0 `n`: "the Trojan preparations described at the end of the last part": the last part ends at 407 with the ants simile of the
  Trojans' departure; true.
- 27 `n` "immota… lumina (331)": checked against the text of 4.331; true. 48 `n` "as at 357": 4.357 `testor utrumque caput`; true.
  24 `n` "ant column 'goes'" (now 404) and 1 `n` (407): checked against the text of the last part.
- 33 `n` (Sychaeus killed by Pygmalion) and 53 `n` ("the murder in Book I"): myth and plot, certain.
- 39 `n` Euripides' Bacchae (Pentheus sees two suns and a double Thebes): I am sure of this passage (Bacchae 918–919) and kept it
  without a line number. The sentence about Pentheus being mad for resisting Dionysus also stays.
- 12 `n` Latin Library `negat` / `cinerem` and 15, 3, 48 `n` LL variants: these are statements about the printed variants in
  `packet.md`, true as stated.
- 1 `n` "totum and aequor enclose the clause", 14 `n` "Extremum hoc… munus encloses the verb", 18 `n` "frames the verb 'oro'", 38
  `n` "longam… viam frames incomitata videtur ire": hyperbaton claims read off the Latin; all true.
- 9, 35 `n`: `colere/credere` and `queri/ducere` as historic infinitives: correct.
- 45 `n` "the usual boasts of magic" and 38 `n` 'deserta' (either 'terra' or Dido): left; the first is a mild general statement,
  the second is given as two readings.
- Echo checks in `i` with no change: 3, 7, 9, 19, 20, 21, 26, 27, 29–32, 35, 37–38, 42, 44–47, 50, 52–54. The renderings are
  close to the Latin but I could not tie any of them to a distinctive remembered phrase.

## Scansion
I read every line against the scanner's printout. Added to `scan-fixes.json` (appended after 4.400; no other entry touched):

- **4.433 (major).** `requiem`: the scanner read the `i` of `qui` as consonantal (`qu` + `i` + vowel, as if `iam`), producing a
  wrong two-syllable `requ | iem`. It is re-quĭ-em, three syllables; the line is five dactyls.
- **4.458 (major).** `coniugis`: the scanner read co-ni-u-gis (four syllables); it is con-iŭ-gĭs (consonantal i after a prefix).
  Same blind spot as 4.48, 4.172, 4.431, which the scanner got right this time.
- **4.466 (major).** `Aeneas`: the scanner split Ae- into A-e (four syllables); it is Ae-nē-ās (three). `somnis` is ablative
  plural so `-nīs` is long.
- **4.494 (major).** `secreta pyram`: the scanner gave `se`, `cre` short and `ta`, `py` long, which is the right shape with the
  wrong vowels. `sē-crē-ta` (long, long, short) and `pў-ra` (short y) give Tū sē | crē-tă pў | ram tec | …. The old marks would have
  made the audio pronounce `secreta` wrongly.
- **4.469 (low, confirmed).** Flagged COSTLY 3.0. I scanned it by hand and the scanner's reading is right: Eu- in `Eumenidum` and
  `-eu-` in `Pentheus` are the Greek diphthong (one long syllable each); the cost comes from `veluti` (final long -ī) and `dēmens`
  (long dē-). Entered with the same marks so the reading is on record.
- **4.503 (medium).** Flagged UNRESOLVED. Half-line, six syllables: ergō | iūs-să pă | rat. Entered like 4.44, 4.361 and 4.400.

Checked by hand and left to the scanner (all correct): 4.431 `coniugium` (cost 1.5, but it read con-iŭ-gĭ-um correctly), 4.425
`Troianam`, 4.426 `Aulide iuravi`, 4.446 `aetherias`, 4.481 `Aethiopum` and `maxumus`, 4.442 `Boreae`, 4.470 `Thebas`, 4.471
`Agamemnonius`, 4.479 `eum`/`eo`, 4.484 `Hesperidum`, 4.492 `deos`, `tuumque`, 4.496 `iugalem`, `exuviasque`, 4.497 `perii`,
`superimponas`, 4.498 `monumenta iuvat`, 4.500 `praetexere`, 4.502 `Sychaei`. All lines with `eu` (469), initial `Ae-`
(411, 446, 451, 466, 481) and consonantal `i` after a prefix (431, 458) are covered.

Doubtful, not changed:
- The scanner lengthens short function words in the arsis (`et` at 414, 418, 463, 470 twice, 472, 476, 491; `ut` at 432; `-tur`
  at 414). This is ordinary hexameter practice and nothing else fits, so I left it.
- `Massylae` (483): the `y` is made long to fit the foot; the quantity of the `y` in the Greek name is uncertain.
- `Tyrios` (468): `Ty` short (as the scanner has it); it is the only fit and matches `Tyrii` in 1.12, but I could not confirm the quantity
  from the Latin alone.
- `veluti` with final long -ī (469): see above.
- 4.419: `sperare` is scanned with long `spē-`; I believe this is right (from `spes`).

`draft.py` is regenerated from `units.json`; `gloss.json`, `known-forms.json` and `novel-forms.json` are untouched (the edits changed
no Latin and no form in `t`).
