# aeneid-015 review (Aeneid II.588-688), two passes

Findings: **major 3, medium 25, low 25** (53 in all). Changes made by script to `units.json` (44 `l`/`i`/`n` fields in 33 units, plus `about`; `t`, `ln`, `p`, `v` and the `l` line counts checked unchanged against the original, `i` is one line everywhere) and 13 entries added to `scan-fixes.json` (2.597, 2.605, 2.608, 2.614, 2.623, 2.640, 2.648, 2.651, 2.673, 2.674, 2.677, 2.678, 2.682). Speech marks: Venus 594-620, Anchises 638-649, Aeneas 657-670, Creusa 675-678. Counts of the opening mark are 5 in `t` and `l` (Anchises' speech has the stray second “ at the head of 639) and 4 in `i`; closing marks 4 in each layer; each speech opens in the unit that holds its first word and closes in the unit that holds its last, in all three layers. The stray “ at 639 stays in `t` and `l` and is not in `i` (checked after the edits).

`draft.py` still holds the pre-review text: do not re-run `make_units.py`, it would overwrite these edits.

## Changes to units.json
Major
1. u21 (624-625) n: "visum (est)... with the accusative and infinitive 'omne Ilium considere'" is false. `Ilium` is nominative; `visum` agrees with it (personal use, nominative and infinitive, `Troia... verti` likewise). Fixed.
2. u29 (642-643) n, `l`, `i`: `una` taken as an adverb "once". The adverb `una` means "together" and "once" would be `semel`; the metre (short -a) and the sense point to the neuter plural `una` agreeing with `exscidia`, "one destruction" (plural of `excidium` for a single downfall). Note rewritten; `l` "Enough one and more than enough"; `i` "One downfall is enough...".
3. u51 (676-677) `l`, `i`, n: `expertus` was made to go with `spem` ("some tried hope") and the note said it "suggests that his trust rests on weapons proved by use". It is masculine nominative and cannot agree with `spem`; it agrees with the subject (`tu`), "having tried". `aliquam` goes with `spem`. `l` "but if, having tried, some hope you place...", `i` "but if you have made trial and still put any hope in the arms you have taken up", note rewritten (also states that `in` stands after `sumptis`).

Medium
4. `about`: "he reproaches his father and the gods" is wrong (the second address is to his mother, 664). Now father, then mother; also "soaked in Priam's blood" (an addition) to "come from Priam's blood".
5. u13 (610-612) `l`: "from his great trident dislodged" made the ablative of means a source. Now "with great trident dislodged".
6. u19 (621) `l`: "in the thick of night herself hid shadows" left `umbris` as if an object of `condidit`. Now "in thick shadows of night herself she hid".
7. u22 (626-628) `l`: `instant` sat on the line below its Latin line (line 3 began "press"). Moved to line 2: "...double axes press on / to uproot, the farmers, in rivalry".
8. u23 (628-631) n: "a participle used with a retained accusative" is the wrong label for `tremefacta comam`; it is the Greek accusative of respect (the first half of the note had it right). Fixed.
9. u23 `i`: `congemuit traxitque` (perfects, and `l` has past tense) rendered as "gives... brings"; now "it groaned one last time and, torn from the ridges, dragged its ruin down". `l` "shaken... shaken" for `tremefacta` and `concusso`: first now "set trembling".
10. u24 (632) n: "'inter' follows its two objects" is false (it stands after the first and precedes the second). Fixed.
11. u37 (654) n: "(the preposition 'in' stands after its noun)" is false; `in isdem` is preposition and adjective, split from `sedibus`. Fixed.
12. u40 (657-658) `l`: made `tantumque nefas patrio excidit ore` depend on `sperasti` ("Did you hope... and that so great a crime fell"); it is a second, main-clause question (as the `i` had it). Now "and has so great a crime fallen from a father's mouth?".
13. u41 (659-663) `l`: "by the gods pleases" for the dative `Superis`. Now "to the gods pleases".
14. u41 n: "a chiasmus (object-A, object-B, object-B, object-A)" is not a chiasmus and was garbled. Replaced by what is there: `natum` and `patrem` the two objects of `obtruncat`, Polites killed before Priam's face, Priam at the altar. Also the dative `perituraeque Troiae` is governed by `addere`, not by the participle (clarified).
15. u42 (664-667) n: "The second 'utque' introduces a second object" is wrong; it opens a second `ut`-clause sharing `cernam`, whose objects are `Ascanium patremque... Creüsam`. Fixed.
16. Deponent participles labelled "with present sense": u1 `confessa`, u30 `adfati`, u49 `complexa`, u51 `expertus`. They are perfect participles, active in meaning ("having revealed", "having addressed", "having clasped", "having tried"); "present sense" contradicts the glosses given. Fixed in four notes (u30 note otherwise rewritten, see 38).
17. u54 (681-684) n: "A new paragraph." is false (`packet.md` has ¶ at 588, 624, 634, 650, 671, 679; 681 has none; `p` is correctly absent). Removed. Also the note on `visus`/`visa` now says `visus` is attracted to the first subject and `visa` would be the form with `flamma`.
18. u54 `l`: "behold light from the top... seemed to pour light" (`levis` and `lumen` both "light"), and "to lick the hair flame" (order `lambere flamma comas`). Now "behold lightweight... to pour light a tip... to lick flame the hair".
19. u7 (601-602) `i`: "that does this to you" is not in the Latin (the clause is elliptical until `divom inclementia`). Now "It is not the hated face of Helen, the Spartan woman, nor the blame that lies on Paris:".
20. u27 (638-640) `i`: `ait` left out (the `l` had it). Now "whose blood—he says—is whole". Single “ kept.
21. Scan-fix 2.597 (coniunx, three syllables read for two; li- of `liqueris` long, as `linquo` has perfect `līqui`).
22. Scan-fix 2.605 (mortalis hebetat: four wrong quantities at cost 0.0).
23. Scan-fix 2.648 (demoror ... divom: me short, mo long in the scanner's fit; cost 0.3).
24. Scan-fix 2.651 (coniunxque).
25. Scan-fix 2.678 (coniunx, sixteen syllables for fifteen).
26. Scan-fix 2.674 (Ĭūlum trisyllabic; spondaic fifth foot, cost 2.0).
27. Scan-fix 2.677 (Ĭūlus; cost 2.0).
28. Scan-fix 2.682 (Ĭūlī; cost 2.6).

Low
29. u0 (588) n: bracket note. Checked against `source/aeneid-greenough.json` (`bracketed`: 2.567-2.588 all printed in [ ]) and the packet: the note's "the last of the stretch 567-588" is true; the packet shows only 588 bracketed because 567-587 are at the end of the previous part (014 says so). Note now says that. "It rounds off Aeneas' angry thoughts" made "closes the angry words of the lines just before".
30. u4 (596-597) n: "a command or an urgent question (a question expecting the answer yes...)" tangled; now a future in a question that works as a command. `liqueris` was "a perfect form"; now perfect subjunctive 2nd singular (and says why subjunctive).
31. u5 n: "agrees with the nearer subject" (the verb precedes both); now "the first of its two subjects".
32. u6 `i`: "All of them the Greek battle-lines are circling" was inverted English; and "drained" in the second half. Now "Greek battle-lines are circling all of them on every side... have drunk their blood".
33. u8 n: "(the height of its pride)" for `a culmine` unsupported; removed.
34. u10 n: `tuenti` agrees with `tibi` below; said so.
35. u14 n: "The line is a short one" was ambiguous in a unit of three lines; now names 614.
36. u21 n: `Neptunia` explained by a legend ("see his work on them at 610-611", where he is tearing them down); now "in the legend the god helped to build Troy's walls, which is why it is his hand that shakes them down".
37. u24 n: "the god is Venus" stated as fact; the word is masculine. Now "taken to be Venus".
38. u30 n: "in the gesture of lying down as if laid out for burial" is not in the Latin; removed; `positum` said to agree with `corpus`.
39. u26 `i`: "my father's house, the old home, my father" (patriae sedis; father twice in the line). Now "my ancestral home, the old dwelling, my father".
40. u34 n: "`hominum` another" (genitive in -om), but `hominum` is the ordinary genitive plural.
41. u48 (671-672) `i` and n: "shield-strap", "(strap)" is not in the Latin. `clipeo` only.
42. u49 `l`: "and the little one to the father held out Iulus" doubled `parvum... Iulum`. Now "and small to the father held out Iulus".
43. u3 `i` (echo): "Why this rage? Or where has your care for us withdrawn?" to "Why are you raging? Or where has your care for us gone?".
44. u41 `i` (echo): "fresh from the blood of Priam" to "come from all that blood of Priam's".
45. u43 `i` (echo): "Arms, men, bring arms" to "Men, bring arms, bring arms".
46. u44 `i` (echo): "the last light calls the conquered" to "the final daylight summons the defeated".
47. u53 `i` (echo): "wonderful to tell" to "marvellous in the telling".
48. u56 `i`: "stretched his hands to heaven with his voice" to "and, lifting his voice, stretched his palms to heaven".
49. Scan-fix 2.608 (disiectas: dis | iec | tas; syllabification only, quantities were right; the scanner fused si+e by synizesis, cost 1.8).
50. Scan-fix 2.673 (coniunx: con | iunx; syllabification only).
51. Scan-fix 2.614 (half-line, UNRESOLVED).
52. Scan-fix 2.623 (half-line).
53. Scan-fix 2.640 (half-line).

## The drafter's doubtful points
- **597 liqueris / aspicies.** `aspicies` is a future (in a question with the force of a command); `liqueris` is perfect subjunctive in an indirect question, parallel to `superet`. Note fixed (30). Scan fix (21).
- **643 una.** Changed (2).
- **631 iugis.** Left. In both readings `iugis` is the ablative plural of `iugum` (separation with `avolsa`, or place/way with `traxit`); the note says both and does not choose; `l` and `i` take "torn from the ridges". Not a dative.
- **678 relinquor.** Left. First person singular passive, agreeing with the speaker (`coniunx quondam tua dicta`); `Iulus` and `pater` are joined to it loosely, as the note says; the `i` correctly gives the plural "are... left" to the three. Only the scansion was wrong (25).
- **684 visus / visa.** Left, with the note's wording tightened (17). `visus` agrees with `apex`; `visa` is understood for `flamma`.
- **644 adfati.** Nominative plural masculine of the perfect participle of `adfor`; label fixed (16, 38); `i` "address my body as it lies, and leave" turns a participle plus imperative into two imperatives and drops `O`: left, the sense is kept.
- **633 unnamed god** (`ducente deo`, 632 in this part's numbering). Left as "a god" in `l` and `i`; note now says the word is masculine and the guide is taken to be Venus (37).
- **588 bracket note.** See 29; correct as drafted, clarified.
- **614 / 623 / 640 half-lines.** Entered in `scan-fixes.json`, reasons begin "Half-line" (51-53). Scansion: 614 fer-r(o) ac | cin-cta vŏ | căt; 623 nū-mĭ-nă | măg-nă dĕ | um (deum as two syllables); 640 vōs ăgĭ | tāte fŭ | gam.

## Refused / checked and kept
- No Homer or Servius cites are left in any note (grep for Homer, Iliad, Odyssey, Servius, Conington, Austin, Dryden, manuscript: none). The A&G cites are all to general headings (objective genitive, impersonal passive, -ura participles, historic infinitive, supine) and are true.
- u32 (645) `l` "will pity me the enemy" supplies `me`, which the Latin omits: left; the note says the object is omitted and the `l` is a gloss.
- u15 `l` uses dashes where the Latin has commas around `respice`: left (punctuation of the gloss, not meaning).
- u53 `l` present "arises" against `i` past "arose": left; historic present, and the `i` follows `replebat`.
- u34 `i` "the father of the gods and king of men": left; it is the only English for the formula `divom pater atque hominum rex`.
- u12 `i` "stones torn from stones": left; literal `avolsa saxis saxa`.
- u47 `i` "We shall not all die today unavenged" for `Numquam omnes hodie moriemur inulti`: left.
- u2 `quis` as adjective, u11 `qua` for `ulla`, u36 elliptical verb of begging, u46 `sinite revisam` without `ut`, u55 historic infinitives, u29 `captae superavimus urbi` (dative with `superare`, "survive"), u41 `placet... nihil relinqui`: labels checked against the forms and left.
- Latin Library disagreements in the packet (597, 598, 602, 608, 617, 622, 630, 631, 643, 648, 651, 653, 666): all spellings; noted only where drafted (597, 598, 608, 617, 622, 629-630, 643, 653).
- Two passes: the first read every note against its form and line, `l` against `t` word by word and `l` against `i`; the second took the scansion (every line, natural quantities) and re-checked the edited fields, speech marks, line counts and paragraph flags by script.

## Scansion
Every line scanned by hand with natural quantities of every open syllable (the scanner leaves them to the metre, so can return a valid fit with wrong quantities; this found 2.605 and 2.648, both at cost 0.0 or 0.3).

Entries added (all checked against the validator's rules: letters equal the words, six feet, dactyl/spondee patterns, sixth foot –×; half-lines numbered 1..k with one ×):
- 2.597 coniunx = con | iunx (15 syllables): li-que-ris | An-chi | sen su-pe | ret con | iunx-ne Cre | ü-sa.
- 2.605 mortālīs hĕbĕtat: mor-tā | līs hĕ-bĕ | tat vī | sus tĭ-bĕt | ū-mĭ-dă | cir-cum (scanner: mor-tă-lĭs | hē-bē, four wrong quantities).
- 2.608 dis-iec-tas (syllabification only).
- 2.614, 2.623, 2.640 half-lines.
- 2.648 dē-mŏ-rŏr | ex quō | mē dī | vom pă-tĕr | at hŏ-mĭ | num rex (scanner had mē short and mo long).
- 2.651 con | iunx (Nos con | ef-fu | si la-cri | mis con | iunx-que Cre | ü-sa).
- 2.673 con | iunx (syllabification only).
- 2.674, 2.677, 2.682 Ĭūlum / Ĭūlus / Ĭūlī three syllables, fifth foot a dactyl (as 1.556, 1.690, 1.709 and 1.267 Iulo); the scanner made three spondaic fifth feet (a spondeiazon three times in fifteen lines is the sign).
- 2.678 con | iunx (sixteen syllables read for fifteen).

Hand-scanned, scanner right, no entry (notable): 2.589 clāra (cost 0.9, `non` long); 2.593 continuit (-it lengthened in arsis at the pause; the only fit); 2.598 Graiae (Grā-iae); 2.602 divom ... divom (dī- long, as at 648); 2.606 caligat (ca- and -li- both long, forced at the line start); 2.607 parere and 2.622 Adparent (pa- long in both, forced); 2.612 Scaeas (Scae-as, two syllables); 2.616 Gorgone (-ne short, Gorgo -onis); 2.620 Nusquam abero (quam elided, a- short); 2.624 mihi (final -i long in arsis, forced; cost 0.6); 2.625 Ilium et ex imo (the fit needs the i of imo long; only fit, left); 2.631 iugis (consonantal i; ablative plural -īs long); 2.638 Vos O and 2.644 Sic O (no elision of -s, no hiatus); 2.646 exuviasque (e-xu versus ex-u, same weights; left); 2.653 urguenti (gu consonantal: ur-guen-ti, the cost 1.5 is the scanner's synizesis route to the right count); 2.656 consilium (um elided); 2.661 ianua (iā-nu-a); 2.666 utque at the line end (six feet complete; not hypermetric); 2.686 excutere et (re elided). Greek eu: none (neu at 607 is one syllable). Initial Ae-: none in this part (aetate 596, aevi 638 are the diphthong ae). Consonantal i after a prefix: coniunx (597, 651, 673, 678), disiectas (608). Hiatus: none.

Found outside this part (not changed): the published `aeneid-014` line 2.563 (`parvi casus Iuli`) was hand-scanned there with a spondaic fifth foot and consonantal I (cost 2.8). On the evidence above Iuli is Ĭūlī there too (fifth foot a dactyl, `mus` still lengthened at the caesura). A scan-fixes entry for 2.563 would change the published sc only on a rebuild of 014.

## Counts
major 3, medium 25, low 25.
