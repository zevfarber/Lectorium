# Review of beowulf-fitt-11

## Pass 1

Method: every unit read against Klaeber's line (packet), then `l` word by word, `l` against `i`, `i` for remembered phrasing, and the published parts grepped for house renderings. `t`, `ln`, `v` untouched (checked against a backup). 37 units, 37 notes. 19 field changes in 16 units.

### Changes (line · field · severity · wrong · done)

- 755 · n · high · said ‘hyge’ is a neuter noun; it is masculine. · changed to masculine.
- 731 · n · medium · said the indicative of ‘cwōme’ would be ‘cōm’; the form is ‘cwōm’. · corrected, and added that the ending ‘-e’ marks the subjunctive.
- 731 · i · medium · ‘the terrible awesome one’ was left after ‘of every one of them’, so it read as a description of the men. · moved to the front as the subject.
- 734 · n · medium · glossed ‘þā gēn’ as ‘as yet’, which with ‘ne’ would be ‘not yet’, not ‘no longer’. · now ‘gēn’ is ‘still, yet’ and ‘ne … þā gēn’ is ‘no longer’.
- 762 · l · medium · rendered ‘on weg þanon’ as “from there on his way to flee”; ‘on weg’ is ‘away’. · now “and, away from there, to flee”.
- 764 · n · medium · called ‘his fingra geweald’ an object clause; it is an accusative noun phrase with ‘to be’ left out. · rewritten.
- 764 · n · medium · “The first ‘his’”: the unit has only one ‘his’. · now “‘his’ is Grendel’s”.
- 771 · n · medium · said ‘hrūsan’ is an accusative; the ending is the same in dative and accusative. · note now says so and gives the sense from the verb of falling.
- 775 · i · medium · “was wrenched away” makes ‘ābēag’ (‘bent, gave way’) passive and violent, and the word order lost ‘þǣr … þǣr’. · now “Where the fierce ones fought, many a gold-adorned mead-bench gave way from the sill, as I have heard.”
- 720 · n · low · “The phrase is formulaic for an outcast” was asserted with no evidence. · removed.
- 724 · i · low · “patterned” against `l` and note “gleaming”; “went forward” adds a word. · “gleaming”, “went on”.
- 730 · i · low · “leapt up” adds a motion to ‘āhlōg’ (‘laughed out’). · “exulted”.
- 743 · n · low · gloss “soon” against `l` and `i` “at once”. · “at once”.
- 745 · n · low · called ‘tōgēanes’ a preposition and then said it has no object. · now said to be taken as an adverb with ‘him’ supplied.
- 750 · n · low · ‘mundgripe’ called a dative of respect as if certain; ‘mētan’ normally takes the accusative. · flagged as a puzzle and a guess.
- 760 · i · low · “making for the door” and “after him” are not in the Old English. · “on his way out”, “stepped further forward”.
- 762 · n · low · ‘wīdre’ called a plain comparative adverb though editors alter it (apparatus). · note says it is unusual and names the variants.
- 764 · i · low · “the use of his fingers” for ‘geweald’ (‘control, rule’). · “the control of”.
- 765 · n · low · “The poet pities Grendel” is a claim about the poet's feeling. · replaced with a statement about whose side ‘gēocor’ is said from.
- 782 · i · low · “strange” has no Old English behind it. · removed.

Counts by severity (20 rows, 19 field edits plus the 764 note listed twice): high 1, medium 8, low 11.

### Considered and refused

- 718 · i “to his harder luck”: awkward, but the phrase is the best English for the guessed ‘heardran hǣle’ and the note flags the guess; no better rebuild from the grammar.
- 739 · l “tore him unhindered”: ‘him’ is supplied for the unexpressed object of ‘slāt’; `l` already supplies objects elsewhere and the note says the case.
- 748 · l/i “sat up”: ‘gesittan’ can carry ‘sit up’; the note admits the ‘wið earm’ ambiguity honestly.
- 734 · i “But” and “his fate”: small additions that English needs; the force is unchanged.
- 778 · `l` “by proper means” against `i` “ordinary means”: the note says the phrase is a guess; both are within the guess.
- 750 · i “in all the world, in all the corners of the earth”: sounds familiar, but it is rebuilt from ‘middangeardes’ and ‘eorþan scēata’ and `l` shows the parts.
- 710 and 712 renderings of ‘mynte’, ‘mānscaða’, ‘hleoþu’: checked against grammar and published parts, correct.
- 731 · note “as in fitt II” for ‘awesome one’: the first āglǣca in a published part is in fitt VI, but the fitt II ǣglǣca note is where the rendering was set (QUESTIONS.md says so); left.
- 'ætstōp' from ‘ætsteppan’ (745): spelling of the infinitive varies (stæppan/steppan); left.
- 718 and 784-788 cruces (‘hǣle’, ‘helle hæfton’, ‘ealuscerwen’, ‘renweardas’, ‘geneahhe’): readings and flags in notes are honest; QUESTIONS.md entry is the drafter's/orchestrator's job.

## Pass 2

Method: as pass 1, plus every `gloss.json` entry checked against the form in each line where it occurs (all 316 forms of the text were found to be covered, either by a new entry or by an existing glossary entry whose readings were read against the line), generality (no line numbers, no "here"), guess markers, and the 30 `__broaden__` entries compared with `beowulf-glossary.json` (the old text is reproduced exactly in all 30, and each new reading is true of its form). `t`, `ln`, `v` and all glossary keys are untouched (compared with a backup). 9 units and 17 gloss entries changed, 5 broaden entries added or reworded.

### Changes (line/form · field · severity · wrong · done)

- mundgripe (750) · n and gloss · medium · the note called ‘mundgripe’ a dative and a puzzle, while the broaden entry (correctly) parses it as accusative, object of ‘mētte’; the noun’s singular is ‘-e’ in nominative, accusative and dative alike. · note now says the form does not fix the case and takes the accusative.
- mīne (776) · broaden · medium · new reading said ‘instrumental/dative singular feminine, agreeing with gefrǣge’, but ‘gefrǣge’ is neuter (the feminine dative would be ‘mīnre’). · “instrumental singular neuter”.
- wið (722/749) · broaden · medium · new reading said ‘preposition with accusative’ for ‘līf wið līce’, where ‘līce’ is dative. · now “dative or accusative”, with the dative for ‘līce’ and the accusative for ‘earm’.
- folma (745), folme (748) · gloss · medium · called ‘masculine weak’ and ‘feminine weak’; ‘folm’ is a feminine noun, and ‘folma’ is its accusative plural. · both now ‘feminine’.
- wānigean (787) · gloss · medium · circular and meaningless (“related to wānian ‘to wail, lessen’”). · rewritten as a lengthened form of ‘wānian’, marked a guess.
- gesæt (749) · broaden added · medium · the existing entry gives only ‘sat (in council)’ and a first-person reading; the reading ‘sat up’ was not covered. · broadened, old text whole.
- tōgēan[es] (747) · n · medium · said Trautmann “did not change the preposition”, an inference from the abbreviation ‘[him] r. o.’ that the packet does not support. · now says the abbreviation cannot be expanded with confidence.
- ‘fāh’ note (714) · n · low · cited ‘gore-stained at 484’; the word is ‘drēorfāh’ at 485. · corrected.
- ‘dryhtsele’ note (767) · n · low · ‘lord-hall at 484’; it is 485. · corrected.
- ‘rinc’ note (720) · n · low · “sounds grim when used of a monster” was an unsupported impression. · now says it normally means a fighting man and is used of Grendel.
- ‘lēoht unfǣger’ (726) · i · low · “ugly to see” adds ‘to see’. · “ugly”.
- ‘forman sīðe’ (739) · i · low · “at the first grasp” invents ‘grasp’ for ‘sīð’. · “the first time he quickly seized”.
- ‘bāt bānlocan’ (739) · i · low · “bit through” adds ‘through’. · “bit into”.
- ‘Sōna’ (750) · l and n · low · ‘Soon’, against ‘at once’ for ‘sōna’ at 743 and in the glossary. · ‘At once’.
- ‘Hyge wæs him hinfūs’ (755) · l · low · “set on going hence” is paraphrase in the literal line. · “hence-eager”.
- ‘Dryhtsele’ (767) · i · low · “great hall” for ‘lord-hall’. · “lordly hall”.
- ‘atelīc egesa … stōd’ (783) · i · low · “seized” for ‘stōd’. · “came upon”.
- hrūsan · gloss · low · ‘dative singular’ only, though the weak ending is the same in the accusative and the line takes ‘to the ground’. · “dative or accusative”.
- geregnad · gloss · low · ‘masculine’, but ‘medubenc’ (in the same entry set) is feminine. · gender dropped.
- hæfton · gloss · low · parsed as accusative singular without saying the ending is irregular. · irregular ‘-on for -an’ stated.
- hǣle · gloss · low · guessed sense not marked. · marked.
- heardran (broaden) · low · the guessed phrase not marked in the new reading. · marked.
- þrȳðswȳð · gloss · low · the note calls it a guess, the entry did not. · marked.
- gedǣlde · gloss · low · ‘preterite subjunctive’ stated as fact of an ambiguous weak-verb form. · now “subjunctive in sense … the form alone does not tell”.
- gedræg · gloss · low · “cf. ‘drag’? related to dreogan” was a loose guess. · “origin uncertain”.
- treddode · gloss · low · lemma ‘tredan’ for a weak form that the note derives from ‘treddian’. · lemma ‘treddian’.
- āhlōg · gloss · low · lemma ‘āhlihhan’ against the note’s ‘āhliehhan’. · made the same.
- ǣfensprǣce · gloss · low · ‘accusative’ only, while the note says ‘takes a genitive’; the form is the same in both. · “genitive or accusative”.
- ǣr (754) · broaden added · low · the existing entry has no ‘sooner’ reading. · broadened, old text whole.

Counts by severity: high 0, medium 7, low 22.

### Considered and refused

- 733 · `gēn` “no longer”: the existing glossary entry says ‘þā gēn’ “as yet”; the old entry cannot be rewritten and the note’s reading is argued from the grammar. Left.
- ‘ætstōp’ (745) lemma ‘ætstæppan’ in gloss against ‘ætsteppan’ in the note: both spellings of the infinitive occur; left (as in pass 1).
- ‘fǣttum fāhne’ (714) · i “plates of gold”: ‘of gold’ is flagged in the note as “of gold, I take it”; left.
- ‘fāgne’ (725), ‘ligge’ (727), ‘ēdrum’ (742) “Anglian spelling”, ‘ferhðe’ gender: plausible and not checkable without a lexicon in the sole-source set; left.
- 731 · note “as in fitt II” for āglǣca: unchanged (pass 1 reason).
- The old `wið` entry’s “with accusative” for ‘līf wið līce’ in the existing glossary: it is an existing entry and may not be rewritten; the new reading says the dative.
- ‘Tho.’ rendered ‘Thorpe’ in notes: ‘Thk.’ is Thorkelin in the apparatus; ‘Tho.’ is Thorpe (as in published fitt X); left.
