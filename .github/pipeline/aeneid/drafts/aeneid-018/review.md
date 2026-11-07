# aeneid-018 review (Aeneid III.99-208), two passes

Findings: **major 3, medium 17, low 28** (48 in all). Changes were made in `draft.py` (the `U` list and `ABOUT`; the file was regenerated from the reviewed list, so re-running `make_units.py` is safe and gives exactly the reviewed text) and `units.json` was rebuilt with `make_units.py`: 43 of 87 units changed (15 `l`, 13 `i`, 30 `n` fields) plus `about`. `t`, `ln`, `p`, `v` are byte-identical to the pre-review file (checked by script), every `l` has the line count of its `t`, every `i` is one line. One entry added to `scan-fixes.json` (3.108). Pass 1 was a full read of all 87 units against the Latin; pass 2 re-read every changed unit and re-ran the structural checks (below).

Speech marks (“ in the unit with the first word, ” in the unit with the last, in `t`, `l` and `i`): Anchises 103-117 (u3 to u16), sailors 129 (u25, both marks), Penates 154-171 (u46 to u61), Anchises 182-188 (u69 to u72). Counts of “ and ” are 4 and 4 in each of `t`, `l`, `i` (and `n` mentions them four times each); checked after the edits. `p` flags at 99, 121, 135, 147, 172, 192 match the packet's paragraph marks.

## Changes
Major
1. u36 (143-144) `l`: "bids my father go" turns `pater` (subject of `hortatur`) into the one told to go, and `mari` had slid onto the line before. Now "Again to the oracle of Ortygia and to Phoebus, retraced, / urges the father to go by sea, and to beg for favour". `i` already right.
2. u22 (125-127) `l`: "and with many lands we skim the seas set thick" read `crebris` with `legimus` and `consita` as "set thick"; `crebris… terris` is the ablative with `consita` ("sown with crowded lands"). `Cycladas` had also moved up a line. Now line 2 ends "and scattered over the sea", line 3 "Cyclades, and we skim the straits sown with crowded lands". `i`: "loud with Bacchic revels" (not in `bacchatam`) is now "with Bacchic revels on its ridges". `n` gains the ablative `crebris… terris`.
3. u70 (184-185) `n`: `haec` was called the subject of `portendere`. It is the object, `debita` agrees with it, and the subject (Cassandra) is unexpressed ("I recall her portending"). `l` mixed a passive ("were being foretold") with an active "she called"; now "Now I recall her to portend these things, owed to our race, / and often Hesperia, often Italian realms to call". `vocare` note: same unexpressed subject.

Medium
4. u1 (99-101) `n`: "the whole sentence is in the present" is untrue of `exorta` (perfect, with `est` left out); now says `quaerunt` is the vivid present and `est` is missing. "(the 'us wanderers')" tidied.
5. u4 (104) `n`: "the adjective `medio` separates `ponto` from `iacet`" is meaningless, and `insula` is not last in the line. Now: `medio… ponto` frame `iacet insula`; `insula` "set late".
6. u11 (111-112) `n`: "the Great Mother and her cult were believed to have come from Crete to Phrygia" stated as general belief; now it is Anchises' claim.
7. u20 (122-123): `l` dropped `deserta` ("were empty" served for both `deserta` and `vacare`) and the infinitives were finite in `l`; now "and the deserted shores of Crete, / the houses to be free of the enemy, and the abandoned seats to stand ready". `n` said "three more infinitives" and named two, and said `domum` would give "empty of the foe's houses" (no such construction); now two infinitives, and `domum` "a genitive plural, which would change the construction".
8. u26 (130-131) `n`: `Curetum` called "the old genitive plural in -um… for Curetorum"; `Curetes` is a Greek third-declension noun and `-um` is its regular genitive plural. "First priests of Jupiter" (unsupported) became "guardians of the infant Jupiter".
9. u28 (133-134) `n`: "`Pergameam` (a city, understood from `urbis`)" garbled; it is an adjective used as a noun. `i`: "on high roofs" invented "high"; now "with its roofs". `n`: "dwellings built about it" is now "buildings".
10. u30 (136) `n`: `operor` "takes the ablative" in poetry; `conubiis arvisque novis` could not show an ablative (dative and ablative plural coincide) and `operor` takes the dative; reworded.
11. u32 (137-139) `n`: "`tabida`, `miseranda` and `letifer` all describe `lues`" contradicts the end of the same note; `letifer` goes with `annus`. `l` had `came` on the wrong line and "wasting… piteous to trees and crops, came a plague" is now "pitiable came / to both trees and crops a plague, and a deadly year".
12. u34 (141) `i`/`n`: "scorched the fields to barrenness" and "the fields are barren as a result" make `sterilis` resultative; Latin has the plain adjective. Now "scorched the barren fields".
13. u36 (143) `n`: `oraclum` "Greek-derived syncope" is false (`oraculum` is Latin); now "the unstressed vowel dropped, as often in verse".
14. u41 (148) `n`: "`effigies` is the subject… `visi` picks it up": `visi` is masculine, agreeing with `Penates`; now said.
15. u42 (149-150) `n`: `quos` "connecting relative"; it is an ordinary relative pronoun inside a sentence.
16. u62 (172) `n`: "the dash marks that the sentence breaks off (anacoluthon)… the construction starts afresh" is wrong; `attonitus` is picked up by the `I` of `corripio` after a parenthesis. Rewritten.
17. u63 (173-174) `i`: "their living presence" turns `praesentia ora` (faces present) into an abstraction with "living"; now "their faces present before me". "It was no dream" (a familiar English phrase) now "It was not sleep". `n`: `velatas comas` "bound with fillets" now "covered with a veil or bound with a fillet".
18. u65 (178-179) `i`: "put Anchises in the picture" is modern-casual. Now "gladly informed Anchises, and laid out the whole matter in order".
19. u84 (205-206) `l`/`i`: `primum` and `se` were dropped. `l` now "land first itself to raise at last / was seen…"; `i` "seemed first to lift itself". `n`: "a haze or the smoke of hearths" (invented) removed; `primum… tandem` explained.
20. Scansion 3.108 (see below).

Low
21. u2 (102) `n`: "the usual way Virgil names him in this book" for `genitor` (unprovable) now points to `pater` of line 144; "compare the old genitive in -um you saw earlier" for `virorum` (a regular form) removed.
22. u7 (107-108) `n`: "Greenough's older form of the name" → "the form of the name that Greenough prints".
23. u9 (109-110) `i`: "did not yet stand" for the pluperfect `steterant`; now "were not yet standing".
24. u21 (124) `n`: `pelago` "ablative of the way" → "of route or means".
25. u23 (128) `n`: "as the crews call to one another in different ways" (not in the Latin) → "shouting in rivalry".
26. u26 (130) `l`: "a wind as we go" lost the object `euntis`; now "a wind, us as we go".
27. u35 (142) `i`: "refused its food" → "refused food".
28. u40 (147) `n`: `terris` "dative or ablative of place" → ablative of place where.
29. u43 (150-151) `l`: `adstare` stood on the wrong line; now "seemed before the eyes to stand of one lying / in sleep…".
30. u44 (151-152) `l`: `se` and `per insertas fenestras` dropped; now "where itself / the full moon through the inset windows was pouring".
31. u48 (158) `n`: "the Roman honours" → "glory for the race".
32. u49 (159) `n`: "the 'what you must do in return'" (not in the Latin) removed.
33. u52 (161-162) `l`: `Delius` on the wrong line; now line 1 ends `has urged`, line 2 begins "the Delian". `n`: `Cretae` "an old locative" → "a locative".
34. u53 (163) `n`: `Grai` "the old form" → "the contracted form… (two syllables in the verse)", which is what the scansion needs.
35. u54 (164) `l`: "the fertile soil" for `ubere glaebae` → "the richness of soil".
36. u56 (165) `n`: "`fama` (is) is understood" → "`est` is understood".
37. u57 (167) `n`: "'our own', 'propriae', 'lasting'" garbled → "`nobis` ... 'ours'; `propriae` 'our very own, permanent'".
38. u60 (170-171) `i`: "Ausonian land" for plural `terrasque… Ausonias` → "lands".
39. u64 (175-178) `l`: line division (`supinas`, `manus`) shifted; now "I stretch upturned / to heaven with a cry my hands, and gifts I pour out / undefiled on the hearths".
40. u66 (180) `l`: "double line" for `prolem ambiguam` → "doubtful stock".
41. u69 (182-183) `i` (echo of a stock "harried by the fates of Ilium"): now "tried so hard by the fates of Ilium".
42. u76 (194-195) `l`: `mihi` dropped; `i`: "storm-cloud… came to rest… night and tempest" (stock echo) → "rain-cloud halted… night and foul weather"; `n`: "(Aeneas is seeing it)" removed, `inhorruit` from `inhorreo` or `inhorresco`.
43. u79 (198-199) `l`: line division (`caelum` belongs to line 198); now "…and wet night the sky / has taken away".
44. u82 (201) `i`: `negat` "swears" → "declares".
45. u85 (207) `n`: "rowers stand to heave" (unsupported) removed.
46. u86 (208) `i`: "churn the foam and sweep the blue water" (stock "sweep the blue") → "whirl up the foam and rake the blue water".
47. `about`: "as he lies awake" (the Latin has `in somnis` then denies sleep) → "as he lies there".
48. `about`: "pours an unmixed libation" (`intemerata`, unspoiled) → "pours out unspoiled offerings".

## Refused / checked and kept
- u43 `iacentis` as genitive singular with an unstated `mei` (the other reading, accusative plural, would have no noun to agree with): kept. u46 `Ortygiam` accusative of motion without preposition (island name): kept. u47 `idem` nominative plural: correct (contracted `iidem`). u12 `subiere` (`-ere` = `-erunt`), u55 `coluere`, u75 `tenuere`, u79 `involvere`: labels true. u15 `distant`: plural subject unstated, as the note says. u18 `pecudem` feminine (`pecus, pecudis`), `albam` agrees: true. u73 `ovantes`: true.
- u6 "Homer's 'Crete of a hundred cities'" and u42 "Hector's ghost gave them to Aeneas" carry no line cites and are standard; kept. No Servius, no modern translator, no line cites of other authors anywhere in the part (checked). Cross-references inside the part (`pater` 144, `visi` 150, `corripio` 176, speech ends 117, 171, 188 and their openings 103, 154, 182) checked against the lines.
- Latin Library disagreements: spelling only at 3.102 `monimenta` (not noted, harmless), 3.114, 3.115, 3.125, 3.148, 3.150, 3.173, 3.180 `Adgnovit`, 3.193, 3.194 (all but 3.102 noted); the two that bear on sense, 3.123 `domum` (u20, rewritten above) and 3.127 `concita` (u22), and 3.180 `parentis` (u66, spelling of the accusative plural), are noted.
- `l` against `t` word by word and `l` against `i`: the only other points found are the items above. `i` echoes checked: no remembered line of a known version found beyond items 17, 41, 42, 46; u50 "great walls for the great" follows the Latin's own play and is kept.

## Scansion
Method: hand-scanned the three flagged lines and every line with Greek `eu`, initial `Ae-`, and consonantal `i`, by listing syllables with natural quantities, position and elision and testing them against the scanner's parse; a script listed every vowel or `-m` + vowel/`h` junction and every elision in all 110 lines, and the only junctions the scanner leaves unelided are before consonantal `i` (104 `Creta Iovis`, `medio iacet`; 114 `qua iussa`; 116 and 171 `Iuppiter`; 125 `iugis`; 136 `iuventus`; 146 `iubeat`; 150 `iacentis`; 162 `iussit`; 197 `iactamur`), which is right. No true hiatus in the part. Unflagged lines (cost under 2.0) were otherwise not re-parsed foot by foot.

Entry added:
- **3.108** (flagged COSTLY 2.7) `Teucrus Rhoeteas primum est advectus in oras`: Teu-crus | Rhoe-te | as prī | (mum) est ad | vec-tus-in | o-ras, thirteen syllables. Teu- Greek diphthong (as 1.38); Rhoe- the diphthong; the `te` of `Rhoeteas` long (Greek Ῥοίτειος, ει); `primum` has long first syllable and elides before `est`. The scanner split `Rhoe` into Rho-e and shortened `e` and `te` (fourteen syllables). Unconfirmed (the long `te` rests on the Greek).

Hand-scanned, scanner right, no entry:
- **3.163** (COSTLY 2.0) `Est locus, Hesperiam Grai cognomine dicunt`: Est lŏ-cŭs | Hes-pĕ-rĭ | am Grā | ī cog | nō-mĭ-nĕ | dī-cunt. `Grai` must be two long syllables (Graii contracted) and `cognōmine` has a long `ō`; with `Grai` as one syllable no parse exists.
- **3.168** (COSTLY 2.0) `Iasiusque pater, genus a quo principe nostrum`: Iā-sī | us-que pă | ter gĕ-nŭs | ā quō | prīn-cĭ-pĕ | nōs-trum; `us` long by position before `que`, `ter` long by position before `g`. The cost is the long `Ia-` and `si`. A second parse (Ī-ă-sĭ-us-que, four dactyls) also fits; neither can be confirmed from the Latin alone, the scanner's left in place. Unconfirmed.
- Greek `eu`: **3.108** (fixed), **3.186** `Teucros` (Teu- one syllable, Hes-pe-ri-ae | ven | tu-ros | li-to-ra | Teu-cros fits), **3.130** `euntis` (Latin `eo`, ĕ-un-tis in two syllables; right).
- Initial `Ae-` and `-ae-`: **3.111** `aera` (ae one syllable, `-que` elides before it), **3.126, 157, 191** `aequor`, **3.197** `aequora`, **3.140, 142** `aegra`, **3.194** `caeruleus` (cae-ru-le-us), **3.105, 112** `Idaeus`, `Idaeum-`: all right.
- Consonantal `i` after a prefix: none in the part (no coniunx, iniuria, disiecit). **3.199** `ingeminant` (in-gĕ-mĭ-nant, as 1.747), **3.198** `involvere`, **3.136** `conubiis` (cŏ-nŭ-bĭ-is, nu short as in 1.73 `conubio`, published): right.
- Other checks: **3.122** `Idomenea` (nēa one long syllable by synizesis, 15 syllables; only fit), **3.125** `Donysam` (Dŏ-nȳ-sam, `ny` long, Greek ου), **3.127** `Cycladas` (Cyc-la-das), **3.124/143/154** `Ortygiae/-am` (Or-tў-gĭ-), **3.135** `fere` (`re` long, only fit), **3.136** (above), **3.114** `Ergo agite` and `et divom`, **3.100** `moenia` (moe-ni-a).

## Counts
major 3, medium 17, low 28.
