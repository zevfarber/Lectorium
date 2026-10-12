# Review of beowulf-fitt-14 (lines 925-990)

Method. `t` was checked by script against the packet lines (26 units, whole text tiled, no gaps or overlaps) and was never edited. Every change below was made by script to `units.json` or `gloss.json`; both files are still valid JSON, keys unchanged. Published parts (fitts 01-13) and the glossary were grepped for house renderings.

Coverage checks that passed with no change:
- The dot under a vowel: the first one in the part is `ǣnịge` (972), explained once there; `hǣþẹnes` (986) refers back to it. A script found no dotted vowel in 925-971.
- All six italic spots (936, 949, 963, 965, 976, 985) and all bracket spots (`secg[a]`, `[n]ǣnigra`, `[dōm]`, `Ec[g]-` at 957 and 980, `stīð[r]a`, `egl[u]`) have a note saying what the manuscript has, taken from the apparatus.
- Quotation marks open at 928 and close at 956, then open at 958 and close at 979.
- Ecgtheow's feud (459-472, Fitt VII) and Unferth's challenge (499, Fitt VIII) were checked in the published notes and are supported.

## Pass 1 (units.json)

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 925 | l | medium | l said "pillar", i said "step" (l and i disagree) | l now "step"; note names "pillar" as the other choice |
| 925 | n | medium | said the dash "holds back" Grendel's hand, but no dash precedes `hond` | rewritten: `Grendles hond` is a second object joined to `hrōf` by `ond` |
| 925 | n | low | `stapole` wording did not match the l/i choice | note now says "step" is a guess and "pillar" the alternative |
| 929 | l, n | medium | `lāþes` is genitive singular, but l gave plural "hateful things" | l "of harm"; note says genitive singular neuter, and that `gebād` takes the genitive as well as `fela` |
| 930 | l | low | l "may" against note "can" and i "can" | l "can" |
| 930 | i | low | "Guardian" for `Hyrde`; the house rendering is "keeper" | i "Keeper of glory" |
| 930 | n | medium | said `wunder` and `wundre` are both "object forms"; `wundre` is dative after `æfter` | corrected |
| 932 | l | medium | "of any of woes to myself" garbled the genitive and `mē` | "of any woes for myself" |
| 932 | n | low | "depending on it" was ambiguous (the genitive depends on `bōte`) | made explicit |
| 932 | n | low | `ungeāra` called a guess without noting that 601 renders it "soon" | note now explains the tense difference between 601 and here |
| 936 | n | low | `wīdeferhð` "for all time" against l "ever" | note now "ever, for all time" |
| 939 | l | low | "man" for `scealc`; fitt 13 (918) uses "retainer" | l "retainer" (i kept "warrior"; see refusals) |
| 942 | l | medium | `ðone` rendered "this" (demonstrative); `mægþa` rendered "kindreds" against 923 "maidens" | l "that son", "of maidens" |
| 942 | i | medium | "the eternal Measurer" was an imported phrase; `eald` is "old" | i "the ancient Lord" |
| 942 | n | low | said `Hwæt` is in the "house table"; it is in the conventions text | reworded |
| 942 | n | medium | treated the first `þæt` as part of the object clause; it points ahead | explained both `þæt` |
| 942 | n | low | `mægþ` senses in the wrong order for the l chosen | reordered, cites 923 |
| 942 | n | **high** | called `ēste` a "dative adjective"; it is a predicate adjective (`hyre` is the dative) | corrected |
| 942 | n | medium | called `bearngebyrdo` simply "a dative"; the ending is unusual | now "best taken as a dative of respect", flagged as a guess |
| 942 | n | low | said the mother "may thank God"; the text says she may say God was gracious | corrected |
| 946 | n | low | `secg [se]` glossed "the man who" (not in the packet); "adopts ... by his words alone" unsupported | both removed |
| 948 | i | low | "this new bond" added a demonstrative not in the Old English | "the new bond" |
| 949 | l | low | "of any of worldly wishes lack" garbled | "of any of the world's wishes lack" |
| 951 | n | low | "if he has paid so much for less" is not in the text | reworded to what the lines support |
| 957 | l | low | bracketed `Ec[g]theow` in l; published parts do not bracket letter-level emendations in names | "Ecgtheow" |
| 958 | l, i, n | medium | `ellenweorc` rendered "deed of courage"; fitt 9 (660) set l "valor-work", i "deed of valor" | l, i and note aligned |
| 958 | n | **high** | note broke off after "‘of the unknown’:" | sentence completed |
| 960 | l | medium | "I would have granted rather": `ūþe` is a simple past, and fitt 8 (501) renders it "grant" | l "I granted rather"; note corrected |
| 960 | i | low | "weary to his fall" is stilted and disagrees with the note | "wearied unto death" |
| 960 | n | low | "would have shown the whole body" was overstated | reworded as Beowulf's wish |
| 963 | i | medium | "seize" for `wrīþan` ("bind") | "bind" |
| 967 | n | medium | said `fēþe` is "the power to go"; unsupported | "going, travel on foot", marked a guess |
| 970 | n | low | `līfwraþe` "found only here" asserted; the hand "as a footprint of the fight, or the price of leaving" was speculation | reworded and hedged |
| 972 | n | low | `þǣr` glossed "by that" while l has "there" | note now "there, that is, in that matter" |
| 974 | i | medium | "He lives no longer for it" reads as "he is dead"; the Old English is "none the longer" | "lives none the longer for it" |
| 974 | n | low | `nīð-` called "hostile" (it is a noun) and `nȳd-` unglossed | glosses corrected |
| 977 | i | low | i kept "Measurer", while published i gives "God" or "Lord" | i "the bright Lord"; note states the l/i pair |
| 980 | i | medium | i "looked at the hand beneath the high roof" contradicted l "over" and the note "up at" | i "above them, under the high roof"; note aligned |
| 984 | l | medium | `stīðra` rendered "stiffer"; the strong genitive plural ending is -ra, and the note says genitive plural | l "of the stiff nails" |
| 984 | n | low | "one editor wants `gehwylc` cancelled": the apparatus names several | "several editors" |
| 987 | l | medium | `heardra` rendered "harder" (same -ra ending as above) | "of hard ones" |
| 987 | l, i, n | low | `āhlǣcan` rendered "fierce fighter" / "monster"; published parts and glossary use "awesome one" / "fearsome one" | aligned |

## Pass 1 findings considered and refused

- `folme` is "hand" in l and i, but fitt 11 (745) has "palm". Refused: the glossary gives "palm, hand", and here the next words are "arm and shoulder".
- `scealc` i kept as "warrior"; fitt 13 has "retainer" in both layers. Refused for i because "warrior" is the epithet of a hero; l now agrees with the published word.
- `ðāra` "gen. pl." and `beweredon` "past subjunctive": the plural past has the same form in the indicative. Refused: the label is true of the form, and the subjunctive comes from the clause after `ne wēndon`.
- `scuccum` "demons", `scinnum` "fiends" in l against i "spectres": refused, since the note says `scinna` is rare and "spectres" is a guess.
- `Ealdmetod` l "Old-Measurer": kept. The apparatus shows editors print two words.
- `ungeāra` "not long ago": kept, since a past verb requires it. Glossary broadening handled in pass 2.
- `handsporu` occurs once in the poem: checked against the source file, true. `līfwraþe`, `landgeweorc` and `grynna` also occur once.
- `Ke.` read as Kemble in the apparatus: standard sigla, kept.
- `gryn` as "snare": cannot be checked without a lexicon lookup, which the rules forbid. It stays a guess in the note.
- `āwa tō aldre` l "ever to eternity": kept (`aldor` is "life, age"); the note gives the literal.
- `wylle` l "will love": kept, since the sense is volitional future.

Pass 1 counts: high 2, medium 17, low 23.

## Pass 2 (fresh full re-read of units.json, then gloss.json)

### units.json

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 929 | n | low | said `gryn` "properly means snare" while the gloss entry read "affliction"; the two contradicted | note reworded; gloss entry rewritten (see below) |
| 949 | n | low | `gād` called "rare" although the same phrase is at 660 | "rare" removed, 660 cited |
| 960 | n | low | "odd for a monster, so read it loosely" gave no real statement | now says the sense is a loose reading and a guess |
| 963 | n | low | "before my (grip)" was awkward | "`for mundgripe mīnum` is ‘before my hand-grip’" |
| 987 | l, i, n | medium | `onberan` rendered "bear off"/"carry off" while `beadufolme` is dative (the glossary entry for `onberan` takes the dative: "bear on, apply to") | l "would bear [on]", i "nor make a mark on", note "bear on", flagged a guess |

### gloss.json (every parse checked against the line)

| key | severity | what was wrong | what was done |
|---|---|---|---|
| feorhgenīðlan | **high** | parsed "dative singular, in apposition to him"; it is accusative, in apposition to `hine` | corrected |
| bearngebyrdo | medium | "genitive or dative singular ... variant of -u" was unsupported | now a dative of respect, case uncertain |
| eglu | medium | "restoration of a lost letter" is wrong: brackets mark emendation, parentheses mark lost letters | "supplied by Klaeber's emendation" |
| stīðra | medium | "comparative" parse contradicted the unit (`-ra` is also the strong genitive plural) | genitive plural, comparative noted as a possibility, "supplied by emendation" |
| lāþes (broaden) | medium | existing entry covers only masculine "the hated one"; here it is neuter, "what is hateful" | added broadened reading |
| sār (broaden) | medium | existing entry gives accusative only; here it is the nominative subject of `hafað` | added broadened reading |
| ungeāra (broaden) | medium | existing "soon, shortly" does not cover the past sense | added broadened reading |
| ðæt (broaden) | medium | existing entry covers only the conjunction; here it is the neuter demonstrative | added broadened reading |
| wēa | low | "in apposition to the subject": `wēa` is itself the subject of the participial clause | corrected |
| grynna | low | gender and sense asserted without support | rewritten under `grin`, figurative sense marked as a guess |
| swīþor | low | example "would rather have granted" was unnatural for `ūþe` | example reworded |
| ðæs, āhlǣcan (broaden) | low | examples glossed "fierce fighter"; the house term is "awesome one" | examples aligned |
| hafast, hǣþẹnes | low | contained "here", which the glossary rules forbid | removed |

All other novel and known forms were checked and kept as written. Keys in `gloss.json` match `novel-forms.json` exactly, every `__broaden__` entry begins with the old entry whole followed by " · ", and no entry has a line number or "here" in new text (the old `ðæt` entry keeps its own "here" because it is kept whole).

### Pass 2 findings considered and refused

- `balwon` "weak-stem spelling" (gloss): odd but not wrong for the form; kept.
- `heardan` "the weak -an ending for -um": true of the form as printed; kept.
- `magan` example "who bore this son" in the gloss against l "that son": the example is a quotation of the sense, not a rendering; kept.
- `nīdgripe` lemma `nīdgrip` with `nīð` "strife, malice" while the note reads `nīd` as "force": the gloss hedges "violent grip, hostile grasp"; kept.
- `folme` broadening ("palm, hand" in the accusative): correct for this use; kept.
- The `þē` broadening covers relative, dative, accusative and reflexive uses; `ðē` (941) is the relative and is covered by the existing `ðē` entry; no change.

Pass 2 counts: high 1, medium 8, low 9 (units: 1 medium, 4 low; gloss rows: 1 high, 7 medium, 5 low, a row naming several keys counted once).

## Totals

| | high | medium | low |
|---|---|---|---|
| Pass 1 | 2 | 17 | 23 |
| Pass 2 | 1 | 8 | 9 |
