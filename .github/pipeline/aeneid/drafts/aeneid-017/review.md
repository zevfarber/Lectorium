# aeneid-017 review (Aeneid III.1-98), two passes

Findings: **major 5, medium 20, low 22** (47 in all). Changes made by script to `units.json` (45 `l`/`i`/`n` fields in 38 units, plus `about`; `t`, `ln`, `p`, `v` and the `l` line counts checked unchanged against the original, `i` is one line everywhere) and 4 entries added to `scan-fixes.json` (3.53, 3.74, 3.87, 3.97; no half-lines in this part). Speech marks (“ in the unit with the first word, ” in the unit with the last, in `t`, `l` and `i`): Polydorus 41-46 (u21-u27), Aeneas' prayer 85-89 (u50-u56), the oracle 94-98 (u60-u62). Counts of “ and ” are 3 and 3 in each of the three layers; checked after the edits.

`draft.py` still holds the pre-review text: do not re-run it, it would overwrite these edits.

## Changes to units.json
Major
1. u27 (45-46) `l`: "and with javelins grew sharp" makes `acutis` a predicate of the verb; it is the attributive adjective of `iaculis`. Now "and with sharp javelins grew up". `i` added "thick with keen javelins" (not in the Latin) and echoed the stock "iron harvest of weapons"; now "a crop of iron weapons covered me, pierced through as I was, and grew up in sharp javelins". Note: `acutis` agreeing with the javelins.
2. u44 (78-79) `i`: "receives our weariness" turns `fessos` (the weary, us) into an abstract object. Now "takes us in, worn out as we are, within a safe harbour".
3. u35 (60-61) `i`: "to let the south winds take the fleet" reverses `dare classibus austros` (give the fleets the south winds). Now "to let the fleet have the south winds". `l`: "the wicked to leave land" read as if `scelerata` went with `excedere`; now "from the wicked land to depart"; `hospitium` "guest-land" (invented) now "hospitality".
4. u42 (75-77): `l` "wandering from lofty Myconos and Gyaros bound fast" disagreed with `i` and `n` ("bound fast to"); `n` also gave a cause for `pius` ("because Delos sheltered his mother Leto") that the Latin does not state. `l` now "wandering, from lofty Myconos and Gyaros bound back" (`e` = `ex`, `re-vinxit`), `i` keeps "bound fast to lofty Myconos and Gyaros". `n` now says: `e` is the form of `ex` before a consonant, placed after its noun `Mycono` and before `celsa` (which agrees with it), `Gyaroque` the second ablative; `ex` with a verb of binding can mean "fastened on, hanging from", so "bound fast to"; `pius` is "dutiful, kindly", no reason given. The drafter's description of the position of `e` was true; the sense was left half-explained.
5. u28 (48) `n`: "`steterunt` (-erunt, the ending that Virgil shortens to -ere elsewhere)" is garbled (the ending is -erunt and nothing is shortened to -ere here). Now "perfect of `sto`, with `-que`, its penultimate syllable short in verse". The cross-reference "The same line comes at II.774" was checked: Greenough 2.774 is `Obstipui, steteruntque comae et vox faucibus haesit.`, identical to 3.48 except for the capital. Kept.

Medium
6. `about`: "moored fast between Myconos and Gyaros" ("between" is not in the Latin). Now "fast to".
7. u7 (13-15) `n`: (a) `vastis… campis` "ablative of description" asserted one label for an ablative that could equally be place or quality; now "of quality or of place". (b) "`Thraces` is the Greek nominative plural" is unsupported; now "nominative plural of `Thrax`". (c) "`sociique Penates` means that the gods of the two peoples were bound by a treaty" is not in the Latin; now "allied household gods, best taken as the land's own gods, friendly to Troy's".
8. u13 (28) `n`: `atro… sanguine` "ablative of description" is wrong for a phrase that goes with the verb (`liquuntur… sanguine`); now ablative of means or manner.
9. u14 (29) `n`: `Mihi… membra` "dative of the possessor": it is a dative of the person affected, close to a possessive; reworded.
10. u19 (39) `n`: the parenthesis "aimed at Dido and the court" ("court" unsupported) is now "addressed to his hearers"; the clumsy mood remark (`sileam` "plainly" subjunctive, `eloquar` "read with it") replaced by: both present subjunctive, `eloquar` having the same form as the future indicative, the question deliberative.
11. u20 (40) `n`: "`reddita` suggests the voice being returned, as an echo" read an echo into the word; now "given back, uttered".
12. u23 (42) `n`: `pias manus` "the epithet is ironical" is not supported (`pius` is Aeneas' own epithet; the ghost is appealing to it). Now "pointed", with the reason.
13. u33 (56) `n`: `quid` "an accusative of respect… used adverbially" mislabels the construction; now `quid` stands where prose would have `ad quid`. `sacra`: "here the second" now "here 'accursed' is the better sense".
14. u36 (62) `n`: the reason given for `instauramus` ("since the rites must be done again, properly, for one whose body was not buried with honour") is the drafter's invention. Now "the verb used of performing a rite afresh".
15. u52 (86-87) `i`: "a second Pergamum for Troy" gives `Troiae` the wrong case (genitive). Now "of Troy".
16. u56 (89) `i`: "pour yourself into our minds" for `inlabere` (glide in). Now "glide into our minds".
17. u34 (57) `l`: "After the terror my bones left" makes the bones the subject; the terror leaves the bones. Now "After the terror left my bones".
18. u50 (85) `l`: "Give a home of our own, Thymbraean, a house" renders `domum` twice (`propriam` and `domum` are one phrase). Now "Give our own, Thymbraean, home".
19. u38 (66-68) `l`: `cymbia` and `pateras` were both "bowls". `l` now "cups" for `cymbia` (word order kept).
20-23. Scansion: 3.53, 3.74, 3.87, 3.97 (see Scansion below).

Low
24. u0 (1-3) `i` (echo of the stock "overthrow the power of Asia and Priam's undeserving race"): now "bring down the might of Asia and Priam's people, who had not deserved it".
25. u3 (8) `n`: "the crews and fighting men" is the drafter's gloss; now "men".
26. u4 (8-9) `n`: "is a set phrase" for `dare fatis vela`: "a vivid phrase".
27. u5 (10-11) `n`: the account of the connectives ("the last two joined by `que… et`") was inexact; now `portus` joined to `litora` by `-que`, `campos` added by `et`; the `vix… iubebat` / inverted `cum` explanation tightened.
28. u8 (16) `n`: "Fortune was (with us)" added words; now "Fortune was", Troy's good fortune lasted.
29. u10 (19-21) `n`: "the auspices-givers (sponsors)" is now "sponsors of the works begun".
30. u11 (22-23) `n`: "the verb `erant` is left out" (`myrtus` is singular) is now "a verb ('there were')"; "the straight shoots look like thrown spears. The picture prepares for line 46" now "the straight shoots of the myrtle… prepares for the spears of lines 45-46".
31. u17 (34-36) `n`: `Gradivus` "the one who marches" now "traditionally connected with `gradior`".
32. u25 (44) `i` (echo of the stock "flee this cruel land, flee this greedy shore"): now "Alas, escape these cruel lands, leave this grasping shore".
33. u30 (51-52) `i`: "had begun to lose faith" for the imperfect `diffideret`; now "was losing faith".
34. u33 (56) `i` (echo of "accursed hunger for gold, to what do you not drive the hearts of men"): now "To what deed will you not drive the hearts of mortals, O hunger for gold, thing accursed?".
35. u34 (59) `i`: "the gods' portent" for `monstra` (plural); now "portents".
36. u38 (68) `n`: "the last cry of farewell that Romans addressed to the dead at the tomb" asserted a rite; now "the last call to the dead".
37. u39 (69-70) `n`: `placata… maria` "a predicative accusative": now "`placata` agrees with `maria`".
38. u41 (73-74) `n`: "not named until its god appears": Delos is not named anywhere in 3.1-98 (checked in Greenough); now "the name does not occur in these lines".
39. u45 (79) `n`: "built around the sanctuary of Apollo" is not in the Latin; now "Apollo's city on Delos (Apollo was born on the island)".
40. u46 (82) `n`: `occurrit` "is present": the present and the perfect have the same form; now says so.
41. u47 (82) `i`: "he knew Anchises for an old friend" to "he recognized Anchises as an old friend".
42. u48 (83) `n`: `hospitio` "ablative of manner": now "in hospitality (an ablative of manner or circumstance)".
43. u53 (88) `n`: "each unfinished" and "the present indicative asks what the guide is" said nothing; now a plain description.
44. u60 (94-95) `i` (echo of "will receive you on your return to her bounteous breast"): now "will welcome you back, on your return, to her rich breast".
45. u61 (96) `n`: "the colon introduces what that land will bring" is wrong (it introduces the place, `hic`); now "the answer in the next line".

## Refused / checked and kept
- **3.12 `magnis dis`**: `dis` is the contracted form (`diis`, `deis`) of the ablative plural of `deus`, as the note says; `cum` governs it with `sociis`, `natoque`, `Penatibus`. The note is true and left. "Who exactly is meant is not settled here" is the safe reading (the Penates are named separately, `magnis dis` is not glossed by Virgil here).
- **3.76 `Mycono e celsa Gyaroque`**: the drafter's description of the position of `e` was true; see 4 above for the clarified sense and the `l`/`i` agreement.
- u26 (45) `n`, Iliad and Euripides: "In the Iliad he is killed by Achilles; Virgil follows the other tradition, familiar from Euripides' Hecuba" carries no line citation and rests on well-known facts; kept. u29 `n`: "whom tradition names Polymestor (Virgil does not give his name)": true, kept. u7 `n` Lycurgus as the Thracian king who opposed Dionysus and u46 Anius as son of Apollo ("in the tradition"): kept without citations. u62 `n`: the rewritten Iliad prophecy (Poseidon, Book XX, of Aeneas' might and his sons' sons): kept without line citation. No Servius citation, no modern translator, no line cites of Homer or Euripides anywhere in the part (checked). Cross-references to lines 11, 16 (u9, u43), 40 (u59), 65 (u28, u46 `solutae crinem`), 45-46 (u11): all checked against the lines.
- u2 `Phrygiae`/Antandros as a port at the foot of Ida, u9 `loco` as the verb `loco`, u12 `monstrum` from `moneo`, u41 Doris as the mother of the Nereids, u50 Thymbra, u58 `cortina` as the oracle's cauldron/tripod, u60 "the speaker is Apollo, though the text does not say so" and "Anchises will misread it": standard and true; left.
- u0 `visum` impersonal; u1 `quaerere` infinitive of purpose; u6 `dis`; u20 `imo… tumulo` ablative of the place from which; u31 `res Agamemnonias`; u32 `potitur` with the ablative; u35 dative of possession; u37 `Iliades… crinem solutae`; u52 `Achilli` genitive: labels checked against the forms and left.
- Latin Library disagreements: 3.5 `divom`/`diuum` (noted, u1, spelling), 3.67 `sepulchro`/`sepulcro` (noted, u38, spelling), 3.82 `adgnovit`/`agnouit` (noted, u47), 3.93 `Submissi`/`summissi` (noted, u59). None changes the sense.
- `l` against `t` word by word and `l` against `i`: the only other points found were the ones above. `i` echoes checked and left: u1, u12, u14 "my blood runs icy and thickens", u28 (the same rendering as aeneid-016's 2.774, kept for consistency), u39, u40, u62. No remembered phrase of a known version was found beyond items 1, 24, 25, 32, 34, 44.

## Scansion
Hand-scanned every flagged line and every line with Greek `eu`, initial `Ae-`, consonantal `i` and hiatus, by enumerating the hexameter parses under the natural quantities (position, diphthongs, and long/short endings) and comparing with the scanner's output. Elisions were checked line by line for hiatus.

Entries added:
- **3.53** `Teucrum`: Greek eu one long syllable, as 1.38/1.626. Il(le) ŭt ŏ | pēs frac | tae Teu(crum) | et For | tū-nă rĕ | ces-sit. The scanner split Teucrum into Te-u (the only line with Greek eu in the part).
- **3.74** (flagged COSTLY 5.2): Nē-rē-ī-dum | mā(tri) et | Nēp-tū | nō Ae | gae-o, twelve syllables, all spondees. The scanner split Ae- and shortened `tu` and `no`. With both elisions (`matri et`, `Neptuno Aegaeo`) there are eleven syllables, which is no hexameter; with neither there are thirteen and no fit; with only `Neptuno Aegaeo` elided `tri` would have to be long. So `Neptuno Aegaeo` is a hiatus and the `i` of Nereidum long. Unconfirmed (see below).
- **3.87** `Pergama, reliquias Danaum atque immitis Achilli`: as 1.30 (rēliquiās, relliquiae, long first syllable; Danaum in three syllables, -um elided). The scanner took synizesis and a one-syllable `naum` (the blind spot of conventions.md).
- **3.97** `hic domus Aeneae…`: hic dŏ-mŭs | Aē-nē | ae cunc | tis dŏ-mĭ | nā-bĭ-tŭr | ō-ris. Aeneae is three syllables (1.92); `domus Aeneae` unelided (cf. 1.617), because with elision there are fourteen syllables and no parse. The scanner (cost 1.2) split Ae- and counted four syllables. Unconfirmed.

Hand-scanned, scanner right, no entry:
- **3.12** (COSTLY 2.0): cum sŏ-cĭ | is nā | tō-quĕ Pĕ | nā-tĭ-bŭs | ĕt māg | nīs dīs: three dactyls and a spondaic fifth foot (`et` long by position before `mag-`); the only fit.
- **3.51** (COSTLY 2.0): Thrē-ĭ-cĭ | ō rē | gī cum | iam dif | fī-dĕ-rĕt | ar-mis: the cost comes from the long Thre- before a vowel and the consonantal `iam`; the only fit. `Threicio` is Thrē-ĭ-cĭ-ō (four syllables, not a one-syllable `Threi`, which leaves thirteen syllables and no line).
- **3.18** `Aeneadasque meo…`: Ae-nĕ-ă | das-quĕ mĕ | ō nō | men dē | nō-mĭ-nĕ | fin-go (`Aeneadae` with short `-a-`, as in Greek -ιάδης; `meo` in two syllables). Ae- is already one syllable; no split.
- **3.8** `aestas` (Ae- one syllable); **3.41** `Aenea` (below).
- Consonantal `i`: no prefix-compound is present (no coniunx, iniuria, disiecit); `iniquis` (17) is in-i-quis (not a consonantal i), initial `i` (iubebat 9, 88; iuxta 22; iaculis 46; Iam 41; iam 51; Iungimus 83) and medial `maiore` 37, `Troia`/`Troiae` (3, 11, 15, 42, 86) all correct. `huic` 28 one syllable.
- Hiatus: none besides 74 and 97 (checked by script: every final vowel/`-m` before an initial vowel or `h` is elided in the scanner's fit except those two, which the fits above cover).
- **3.14** `Thraces arant`: the only fit has `-ces` short (as the Greek plural -ες). Left.

## Unresolved / left open
- **3.41** `Quid miserum, Aenea, laceras?`: under natural quantities (`lăcĕrās`, vocative `Aenĕa`) there is no hexameter. The scanner's fit has `la-ce` long (a spondee); the only other parse has `Aenea` as Ae-nē-ā (final -a long). Both are guesses; the scanner's (cost 0.0) left in place, no entry. Which of the two Virgil intends I cannot settle from the Latin alone.
- **3.74** and **3.97**: the hiatus and the long `i` of Nereidum / the unelided `domus` are the only fits, not checked against an edition.
- Long `-a` of `iuxta` (22), long `ra-` of `radicibus` (27, `rādīcibus`), long `-ō` of `meo` (18): each the only fit (cf. 2.714 `iuxta` in aeneid-016), left, unconfirmed.

## Counts
major 5, medium 20, low 22.
