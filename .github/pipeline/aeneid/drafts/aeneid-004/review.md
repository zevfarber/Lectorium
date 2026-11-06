# aeneid-004 — review (I.297–386)

Adversarial review in two passes, from the Latin and the public-domain references only (Lewis & Short, Allen & Greenough, Conington).
Pass 1: every unit field by field (every grammatical label in every `n` against the form in its line; Latin to `l` word by word, including
the line division; `l` against `i`; remembered English in `i`; speech marks; factual claims in `n` and `about`), then a hand scansion of all
90 lines. Pass 2: re-read of the edited file, three more edits (#3, #19, #36), every one of the 90 lines re-tested by script as six valid feet
after `scan-fixes.json` is applied, and the build run (see "Build" below).
All edits to `units.json` were made by changing `draft.py` and re-running `make_units.py`. `t` was never edited; its cut points moved in four units
only (see Major 1), and the text joined is still the edition's.

**Counts:** Major 7 · Medium 22 · Low 18 · scan fixes added 15 (12 lines the scanner had wrong or could not fit, 3 carrier lines) · refused / verified and kept 16.
Changed: 40 of 51 units (4 `t` cuts, 12 `l`, 12 `i`, 33 `n`) and `about`.

Remembered English: checked from memory of the well-known verse and prose versions, not by collation. Seven `i` lines that sat close to a
familiar phrasing were rephrased (counted under Low); none of the others is a distinctive echo.

## Major (false label, broken `l`, or the build refusing)

1. **Cuts at 370 and 385 (units #41, #42, #49, #50).** The edition prints the closing speech mark with a space before it and none after
   (`iter? ”Quaerenti`, `pulsus. ”Nec`). The draft cut at `iter? ”` and `pulsus. ”`, so the next unit began mid-token and the build refused
   ("ends mid-word at line 370"). The cuts now end at `iter?` and `pulsus.`; the closing mark therefore stands at the head of the next
   unit's `t` (as printed) and is carried at the end of `l` and `i` of #41 and #49, where the speech ends. The notes of all four units say so. The source was not
   touched. This is a defect of the archive's normalisation, not of the draft; it will recur wherever the TEI has a space before `</q>`.
2. **#0 `n`** — "`Maia` is genitive": it is the ablative of origin (`Maia genitum`, born of Maia, no preposition).
3. **#5 `l` (and `i`)** — `constituit` was missing from both; `l` now "to ask, he resolved, and…", `i` "to ask—such is his resolve—and…".
4. **#6 `l`** — "himself alone he goes, accompanied by Achates" made `uno` mean "alone" and contradicted `comitatus`. Now "himself he goes,
   accompanied by one, Achates,".
5. **#17 `n`** — "the singular `dextra` with plural `nostra`": both are singular ablatives; `nostra` is "our", the hand is one collective hand.
6. **#30 `n`** — `celo` "takes a double accusative" (not here: `factum` is its only object) and `amantem` "a present participle used as a
   noun" (it agrees with `aegram`; both are the object of `lusit`, with an understood `eam`). Rewritten.
7. **#43 `n` and `l`** — the shaky `ante diem… componat`: the note read `diem` twice (as `ante diem`, "before the day is done", and as the object
   of `componat`). `ante` is an adverb ("sooner, before I could finish"), `diem` the object of `componat`, `clauso Olympo` an ablative
   absolute. `l` now "before, the day, Olympus being shut, would Vesper lay to rest." (`i` already carried the sense.)

## Medium

8. **#1 `l`** — "swiftly stands" for the perfect `adstitit`; now "stood". `n` notes the vivid present before it.
9. **#4 `i`, `n`; #5 `i`** — the `i` of #4 translated `constituit` (which is in #5) and the note said the sentence runs "to line 309" (it runs to 312).
   Kept the English `resolves` as a deliberate anticipation (it gives the reader a verb), changed "to ask" to "to find" so `quaerere` is not
   said twice, and said so in the note.
10. **#6 `n`** — "fidus Achates, as the poem will call him": the poem has already (I.188, checked in the source).
11. **#7 `l`** — line division: `et virginis arma` is in 315 but `l` put "Spartan" at the end of its second line; `Spartanae` is the first word of 316. Realigned.
12. **#8 `l`, `i`, `n`** — "a handy bow had hung the huntress" made the bow the subject of `suspenderat` (she hung it); `i` "light" for `habilem`; the note's
    "`os` and `genu` as the limit of the adjective" was garbled (the accusative of respect is common with `os`, `umeros`, `genu`). All three fixed.
13. **#9 `l`, `n`** — extra quotation marks inside the speech (“Hey,” she says, “young men…) broke the rule of one “ and one ”; "Hey" is modern for `heus`;
    `me` was added; the first line ended with `sororum`, which is the end of 322. Now one “ and one ”, "Ho", and the line division follows the Latin.
14. **#15 `n`** — "the preposition `sub` is put after its noun": it stands between `quo` and `caelo` (and `in` after `quibus`/before `oris`), inside the phrase. Rewritten.
15. **#18 `l`** — "of such do I think myself worthy an honour" was garbled; now "of such an honour do I deem myself worthy".
16. **#20 `i`** — "…, Tyrians, and the city of Agenor" read as an address to Aeneas and Achates; `Tyrios` is an object. Now "the Tyrians".
17. **#21 `n`** — `genus` "in apposition to `Libyci`" (an adjective); it is in apposition to the people that `fines Libyci` stands for.
18. **#25 `n`** — `Phoenicum` "the old genitive plural in -um"; it is the ordinary third-declension genitive plural of `Phoenices`. Comma-end note added.
19. **#27 `l`, `n`** — `l` doubled the comparison ("before others more monstrous than all"); the note's "Greenough's -es" for `omnes` (ordinary accusative) and
    "double comparison" were wrong. Rewritten.
20. **#28 `n`** — `Quos` left vague ("between brother and sister and husband"); it is Pygmalion and Sychaeus.
21. **#30 `i`** — "kept the grieving lover amused" for `lusit`/`aegram amantem`; now "mocked with an empty hope the sick-hearted woman who loved".
22. **#33 `l`** — line division: `tellure` (358) stood on the third `l` line and `thesauros` (359) on the second, so the lines did not match the Latin; "an old buried store of wealth" for `veteres thesauros`. Realigned.
23. **#40 `n`** — `possent` "a relative clause of characteristic": it is the subjunctive of the terms of the bargain (virtual indirect speech).
24. **#41 `l`, `n`** — `venistis` without "you", `aut` unrendered; and the note said the closing mark stays in `t` (no longer true after Major 1).
25. **#44 `n`** — `forte sua` "contrasts with Juno's storm": nothing in the line says so. Now "of its own accord, not at our bidding".
26. **#45 `n`** — "the reader has been told this from the first line of the part": `pius` first occurs at 305.
27. **#46 `n`** — `genus ab Iove summo` glossed as Aeneas's descendants; it is his own stock (Dardanus, Jupiter's son, came from Italy), which is why Italy is the *patria*.
28. **#48 `n`** — "as the scanner does not know" (a reader's note must not mention the scanner) and a muddled last sentence. Rewritten.
29. **`about`** — "Aeneas, not fooled": he suspects a goddess but does not recognise his mother (I.402–409). Now "sensing a goddess".

## Low

30. **#0 `l`** — "might lie open" for the present `pateant`; now "may". **#0, #4, #9** notes over 140 words trimmed.
31. **#3 `n`** — "the pair of adjectives is split around the verb": only `quietum` is.
32. **#13 `n`** — "the second a gentler one" (the next unit gives two further guesses). **#23 `n`** — "a place to check the scansion" removed from a reader's note.
33. **#36 `n`** — `auro` "ablative of material" → of means. **#26 `n`** — `primis` "means this was her first marriage" hedged to "probably".
34. **#29 `n`** — the hyperbaton described as the victim's name "placed first"; it is at the line's end.
35. **#49 `n`** — "asyndeton, three words" (there are two). **#16 `n`** — added that `locorumque` elides into `erramus` (hypermetric line 332).
36. **#25, #31, #39 `n`** — each comma-ended unit now says why it ends on a comma (see Refused 1). **#4 `n`** likewise.
37. **#9 `i`** ("Ho there, young men… hard on the track of a foaming boar") rephrased as "You there, young men—tell me whether you have seen one of my sisters wandering here,
    girt with a quiver and wrapped in the hide of a spotted lynx, or pressing a foaming boar's trail with her cries."
38. **#17 `i`** ("will fall by our right hands before your altars") → "Many a victim will fall before your altars, struck by our right hand."
39. **#19 `i`** ("lace the high purple boot about the calf") → "…to carry the quiver and to bind their calves, high up, in purple buskins."
40. **#32 `i`** ("unmasked the whole hidden crime of the house") → "laid open every secret of the crime done within the house."
41. **#33 `i`** ("speed her flight and leave her country… a hoard of silver and gold that no one knew of") → "bids her hurry her flight and quit her country… a store of silver and gold that nobody knew of."
42. **#40 `i`** ("as much as they could enclose with a bull's hide") → "as much as one bull's hide would go round."
43. **#47 `i`** ("my goddess mother showing the way… the fates I had been given") → "my mother, a goddess, pointing out the way… the fates assigned me."
(Items 37–43 are the seven echoes; #8 `i` was rewritten under Medium 12.)

## Scansion — hand scansion of all 90 lines

The scanner leaves every vowel that is not fixed by position free, so a "cost 0" fit can still have the wrong quantities; each line was therefore
tested against the lexical quantities (`ēs`, `dē`, `mōs`, `sē`, `prīmā`, `vēnor`, `ōmen`, `aurī`, `argentī`, `cēlo`, `vānus` …) with a small fitting script.
**Fifteen lines added to `scan-fixes.json`** (reasons are in the file):

| line | what was wrong |
|---|---|
| 1.299 | `Teucris` is two syllables (Teu-cris); the scanner split Te-u |
| 1.304 | `Teucros`, same |
| 1.305 | initial `Ae-` (Aeneas): Ae-nē-ās; the scanner split Ae and made a dactyl |
| 1.314 | `sēsē tulit`: the scanner made both `se` short and `tu-` long; the fit is sē-sē (second lengthened at the pause) with short `tulit` |
| 1.316 | `Threissa` is three syllables (Thrē-is-sa); the scanner took two and had to lengthen `-lis` and `e-` of `equos` |
| 1.318 | `dē` and `mōre` are long, `habilem` short-short; the scanner had the reverse |
| 1.330, 1.331, 1.333 | the scanner is right; entered only because they share units with 332, and a unit with an unresolved line gets no `sc` |
| 1.332 | hypermetric: `locorumque` elides into `erramus` (333); the scanner cannot fit it (the packet's flag) |
| 1.341 | `iniuria`: consonantal i after the prefix (in-iu-ri-a); `Longa est` elides |
| 1.343 | `coniunx`: con-iunx, not co-ni-unx |
| 1.372 | `prima` is the ablative (prīmā); the scanner made `pri-`, `-ma` short and `re-pe-` long |
| 1.378 | initial `Ae-` (Aeneas) |
| 1.383 | `Euro`: Eu one syllable; the scanner split E-u |

Readings accepted from the scanner after testing (not in the file): 1.297 `Haec ait, et Maia` (`ait` and `Maia` both fit only with a long `ia`;
trisyllabic `a-it` taken as the scanner has it); 1.300 `aera`; 1.301 `ala` (āla); 1.308 `videt` lengthened at the pause; 1.310 `rūpe`;
1.317 `Hebrum` (long by muta cum liquida); 1.320 `genu` with long final u; 1.322 and 1.375 `sī` lengthened; 1.327 `te` lengthened in the arsis;
1.337 `altē` long; 1.343 `Sy-` long; 1.361 `odium` with short `o`; 1.377 `sua` (one lengthening, either way); 1.384 `peragro` (-ra long before `gr`);
1.385 `Europa` (Eu one syllable; correct). Hiatus: none. Elisions (`nam in`, `qui ex`, `datast`-type `data est`, `circumdare`) checked.
Greek `eu`: Teucris 299, Teucros 304, Euro 383 fixed; Europa 385 correct; Heus 321 correct. Initial `Ae-`: Aeneas 305, 378 fixed; aethera 379, aegram 351, aera 300 correct.
Consonantal i after prefix or hiatus: iniuria 341 and coniunx 343 fixed; coniugis 354, traiecta 355, iugarat 345, iuvenes 321, iactemur 332 (fixed with the line), Iove 380, iit 376 correct.

## Build

`python3 build_aeneid.py aeneid-004` now passes the scansion gate (all 90 lines six feet, no COSTLY or UNRESOLVED) and stops only at the missing
`drafts/aeneid-004/gloss.json` (the glosser's file), before writing anything. One change to `build_aeneid.py` was needed: the filter that removes a
hand-scanned line from the scanner's report compared the words of an `UNRESOLVED` entry with their punctuation, so a line with a comma or full stop
inside it (332: `iactemur, doceas. Ignari…`) could never be cleared even with a fix. It now compares the words
(`A.WORD_RE.findall(strip(…))`). It changes nothing for lines that were already clearing.

## Refused / verified and kept

1. **Comma-ended units** (#4 at 308, #25 at 344, #31 at 354, #39 at 366). The build accepts `,`. #4 is necessary (305–312 is eight lines). #25, #31 and
   #39 could be joined to their successors as four-line units (343–346, 353–356, 365–368), which the convention ("ends at `. ; : ? !`") prefers; this was not done because
   it would move the cuts of `t`, and I was told not to touch `t`. Left for the owner; each now has a note.
2. **Line 309 has no stop at its end** (source as printed; `referre` runs on into 310). Not altered; the note of #5 says so.
3. **`quaecumque` (#15)** — verified: feminine nominative singular, `quaecumque (es)`, the Roman hedge in addressing an unknown god. Kept.
4. **`interfata` (#50)** — verified: perfect `interfata est` of the deponent `interfor`. Kept.
5. **`ante diem… componat`** — see Major 7; the drafter's alternative (taking `ante diem` as a phrase) is the weaker reading and was dropped.
6. **#2 `n`** "`deo` is Mercury, though a reader will sense Jupiter behind him": a defensible reading of `volente deo`; kept.
7. **#13 `n`** the Odyssey 6 comparison (Odysseus and Nausicaa): true; kept. **#1 `n`** `remigium alarum` at VI.19: checked in the source; true.
8. **#45 `n`** Penates saved from Troy at II.717: checked (`patriosque Penatis`); true.
9. **#24 `l`/`n`** `sequar` as future (it could be a hortatory subjunctive): kept as future.
10. **#38 `i`** "a woman is the leader of the deed": literal and the line is famous; kept (the note and `new-renderings.md` no longer treat it as a house rendering).
11. **#12 `l`** "O how you shall I call": awkward but a word-for-word `quam te memorem`; kept.
12. **#10 `n`** `orsus (est)`, **#22 `n`** `profecta`, **#26 `n`** `iugarat`, **#34 `n`** zeugma, **#44 `n`** `iit`, `auris`: verified; kept.
13. **#20 `n`** Agenor as father of Cadmus and Europa; **#21 `n`** Iarbas (Book IV): standard; kept.
14. **#40 `n`** the ox-hide story (the hide cut into strips): the usual account, not in the lines; kept as marked.
15. **Latin Library**: no variants in this stretch (the packet says none).
16. **Speech marks**: Venus-as-huntress 321–324 (opens #9, closes #9), Aeneas 326–334 (opens #11, closes #17), Venus 335–370 (opens #18, closes #41, `l`/`i` only;
    the edition's mark is at the head of #42), Aeneas 372–385 (opens #43, closes #49, `l`/`i` only; the edition's mark is at the head of #50). Every “ is on the first unit and every
    ” on the last of its speech in `l` and `i`; counts in `l` and `i` are equal (4 and 4).
