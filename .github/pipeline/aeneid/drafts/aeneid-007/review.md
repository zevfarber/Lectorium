# aeneid-007 — review (I.561–656)

Adversarial review in two passes, from the Latin and public-domain references only (Lewis & Short, Allen & Greenough, general
knowledge of Servius and Conington). No modern translation was opened and no English wording was recalled as a source.

- **Pass 1:** every unit, field by field. Every grammatical label in every `n` was checked against the form in its line, the Latin
  against `l` word by word (line division included), `l` against `i`, remembered English in `i`, speech marks, `p` flags, the
  five-line limit and the cut points, and the factual claims in `n` and `about`. Then all 96 lines were scanned syllable by
  syllable against the quantities themselves (not merely "does the scanner find a hexameter").
- **Pass 2:** a re-read of the edited file plus a script that applies `scan-fixes.json` over `scan_latin.scan_story` exactly as
  `build_aeneid.py` does and runs the validator's hexameter test on all 96 lines: **95 pass, 0 fail**, and the one half-line (636)
  passes by the validator's "Half-line" rule. No UNRESOLVED or COSTLY report is left. It also caught two items of its own
  (the `Simoentis` syllable count and the `ornatus` parse, both added to notes).
- **The full build was not run** (per instructions), and nothing was published.

All edits to `units.json` were made by script (json load / modify / dump, `ensure_ascii=False`, `indent=1`). **`t`, `ln`, `p`
and `v` are untouched** (asserted by the script, unit for unit). `draft.py` was **not** updated and now disagrees with `units.json`.
**Do not re-run `make_units.py`**: it would overwrite the review.

**Counts:** Major 11 · Medium 37 · Low 31 (79 findings) · scan fixes added 22 (18 lines the scanner had wrong, 1 half-line, 3 carrier
lines) · refused / verified and kept 17. Changed: 42 of 52 units (0 `t`, 22 `l`, 21 `i`, 31 `n`) and `about`. Title, `titleEn` and `part` were
checked and left alone (see "Title fields").

Speech marks (all three layers, one of each per speech): Dido 562–578 opens #1, closes #10; Achates 582–585 opens #13, closes #16;
Aeneas 595–610 opens #22 and closes #28 in `l` and `i`; Dido 615–630 opens #31, closes #40. Counts are 4 and 4 in `t`, `l` and `i`.
**610:** the edition prints the closing mark after a space and glued to `Sic` (`terrae. ”Sic`), so, as in aeneid-004, the cut ends at
`terrae.`, the mark stands at the head of #29's `t`, and `l`/`i` of #28 carry it. #28's note now says so; #29's already did.

Remembered English: checked from memory of the well-known versions, not by collation. Distinctive echoes were rephrased in #2
("oblige me to such measures … my borders far and wide"), #10 ("trusty men … bid them search"), #22 ("Here I am, the man you seek …
saved from the Libyan waves"), #23 ("worn out by every misfortune of land and sea") and #28 ("while rivers run … the sky feeds the stars,
your honour, your name and your praises"). Nothing else is a distinctive echo.

## Major (false label, false fact, build refusal, or an unsafe certainty)

1. **#3 `n` (565–566)** — "'quis' stands for 'quis' as a plain interrogative pronoun (nominative)" says nothing, and "'tanti… belli' —
   genitive of 'tantum bellum'" is a false label (it is simply the genitive agreeing with `belli`). `Aeneadum` now said to be the poets'
   genitive in -um for -arum, with its syllables.
2. **#20 `n` (593)** — "'circumdatur' … the metal is set around the other" reversed the construction. The silver or the marble is
   encircled by the gold (`auro`, ablative of means).
3. **#24 `n` (600)** — "'grates' is the archaic accusative plural of 'gratia'". False: `grates` is a separate noun found only in the plural.
4. **#25 `n` (603–605)** — "a jussive (wishing) subjunctive". A wish is an optative subjunctive.
5. **#26 `i` (605–606)** — contained a line break; the build refuses ("i must not contain line breaks"). Also rephrased.
6. **#36 `n` (623)** — "'cognitus' agrees with the nearest word (as in 583 above)". False: it agrees with the first, `casus`; at 583 the
   participle follows its nouns and agrees with the nearer one. Fixed.
7. **#37 `n` (626)** — "'Teucrorum' — old genitive plural." It is the regular -orum. Replaced with a gloss of `Teucros`/`Teucri`
   (the Trojans, named from their early king Teucer, not the Greek Teucer of 619), and the Greek eu noted.
8. **#43 `n`, `i`, `l` (636)** — **the doubt you asked about.** The draft stated flatly "'dii' is the old genitive of 'dies': 'the gifts and
   the gladness of the day'" and `i` built on it ("the feast-day", "no less generously", "the cheer of the feast-day"). I cannot establish
   from the references I may use which reading the line has: `dii` can be an old genitive of `dies` (= `diei`, "the gladness of the
   day", the feast day) or a spelling of `dei` ("of the god", that is Bacchus, so the wine; compare `adsit laetitiae Bacchus dator`, 734, where the god's name stands for the gift). I do not claim a commentator's verdict I cannot check. The note now says both readings are possible and the English
   keeps both open: `l` "gifts and the gladness of the god (or of the day)", `i` "gifts, and good cheer besides" (no "feast-day", no "generously").
   The scansion is the same either way (dĭ-ī, two syllables), so the hand scan below does not depend on the choice.
9. **#44 `n` (637)** — "'regali… luxu' — ablative of quality or means." Not of quality (that needs a noun with an adjective as a predicate
   description), and not means: it is the ablative of cause or respect with `splendida`.
10. **#45 `n` (640)** — "'caelata… in auro' — engraved in gold (the silver is engraved with scenes)" contradicts itself. The engraving is
    in gold (on gold plate).
11. **`about`** — "the fate of Troy and the names of its kings". Dido says `regesque Pelasgi`: the *Greek* kings. Fixed. The summary was also
    cut from 448 to 355 words (and Aeneas "clasps the hands" became "greets": `petit dextra`).

## Medium

12. **#2 `l`** — the line division was broken (`talia`, in 563, stood in line 2). **#2 `i`** — echo, rephrased (above).
13. **#5 `l`** — `optatis` was in line 1, though it stands in 570 (restored). The note's "comes at the end" is now "stands in the second half".
14. **#6 `l`/`i`** — "Or" is not in the Latin and `et` (also) was unrendered; `i` added "if" and "instead" and a colon for the semicolon.
15. **#8 `n`** — "'mihi' is a dative of the agent": at most possible with a finite passive. Now "dative of the person concerned, 'with me'", with
    the agent reading noted as possible.
16. **#10 `l`** — `iubebo` and `extrema` were in the wrong lines. **#10 `i`** — echo, rephrased.
17. **#11 `l`** — `ardebant` (581) stood in line 2.
18. **#13 `n`** — "'animo' — either dative or ablative": a dative is not a possible reading. Ablative of place without `in`.
19. **#14 `n`** — "the lost ships have been found" was an unsupported reading of `receptos`. Now: Achates reports what Venus promised at I.390.
20. **#16 `n`** — the prophecy was misstated ("his lost ships would be safe"). Venus said his comrades and fleet would return (I.390).
21. **#17 `l`** — `repente` belongs to line 586 (`circumfusa repente`).
22. **#19 `l`** — `genetrix`, `nato` and `adflarat` were in the wrong lines. **#19 `n`** — "'oculis' is dative of the person affected": it is
    "in his eyes", dative or ablative of place.
23. **#20 `l`** — `flavo` belongs to line 592.
24. **#21 `l`/`i`** — `repente` was left out of both.
25. **#22 `i`** — echo, rephrased. **#22 `n`** — "the relative clause comes before its unexpressed antecedent" was wrong (`Troius Aeneas` is in apposition
    to the subject and is the antecedent). The Greenough/Latin Library `Lybicis`/`Libycis` remark was deleted: orthography, which the
    conventions say not to note.
26. **#23 `l`** — `exhaustos` and `terraeque marisque` were in the wrong lines. **#23 `i`** — echo, rephrased.
27. **#24 `l`** — `non opis est nostrae` (601) stood in line 1.
28. **#25 `l`** — `praemia digna ferant` (605) stood in line 1. **#25 `i`** — "a living thing" had no Latin behind it; rewritten.
29. **#26 `l`** — `tulerunt` (605) stood in line 2.
30. **#28 `l`** — `montibus` (607) stood in line 2. **#28 `i`** — "will remain with me" invented "with me"; echo rephrased.
31. **#30 `l`** — "the heavy fortune" for `casu … tanto` ("so great a calamity").
32. **#33 `n`** — the hiatus at `Dardanio Anchisae` (617) was not mentioned. Added, and "dative of the father" replaced by "dative with `genuit`".
33. **#35 `l`** — `opimam` (621) stood in line 2.
34. **#36 `l`** — `Troianae` (624) stood in line 1.
35. **#39 `i`** — `similis` ("a like fortune") omitted.
36. **#43 `l`** — `magnorum` (634) stood in line 3.
37. **#46 `l`** — `passus amor` (644) stood in line 1.
38. **#49 `l`** — `extulerat` (652) stood in line 1.
39. **#50 `n`** — "a coronet with a second circlet" had no support; the sense of `duplicem` is said to be uncertain. "`collo` dative of the
    person" became "dative of reference".

(Medium items 12–39 above are numbered by unit; a unit with two separate mistakes in two fields is counted twice, so the 37 findings fall in 28 numbered paragraphs.)

## Low

40. **#1 `n`** — `Teucri` glossed, eu noted. 41. **#4 `n`** — "The sense: …" hedged as "as commonly taken".
42. **#6 `n`** — `et` = also. 43. **#7 `n`** — the attraction is made explicit. 44. **#8 `n`** — singular verb with the pair.
45. **#11 `i`** — "Heartened" is not `arrecti`. 46. **#11 `n`** — "title as father of his people" was an assumption.
47. **#13 `i`** — clumsy. 48. **#15 `n`** — Orontes is Servius's identification; hedged. 49. **#16 `l`** — `dictis` first, as in the Latin.
50. **#19 `i`** — "noble" is not `decoram`. 51. **#23 `n`** — "the Greeks who had left them alive" garbled; `reliquias` quantity noted.
52. **#24 `i`** — closer to the Latin. 53. **#28 `n`** — `convexa` hedged (hollows or slopes), `montibus` parsed; 54. closing-mark remark added.
55. **#29 `i`** — "takes by the hand" is stronger than `petit`. 56. **#32 `n`** — an interpretive remark deleted.
57. **#33 `i`** — "waters" for `unda`. 58. **#33 `n`** — `Simoentis` has four syllables. 59. **#34 `n`** — `Teucrum` parsed.
60. **#37 `l`** — "to be believed" is not in `volebat`. 61. **#37 `i`** — "claimed" for `volebat`.
62. **#38 `n`** — the O printed before `tectis` belongs to `iuvenes`. 63. **#42 `n`** — `divom` belongs to `divus`, and `templis` was
    called a dative while `l` has "at"; 64. `Aenean` parsed. 65. **#45 `i`** — "endless" overstates `longissima`.
66. **#49 `n`** — `hymenaeos` label made precise; 67. `ornatus` parsed. 68. **#50 `i`** — awkward "a crown, doubled".
69. **#51 `i`** — "with these orders" invented; `ita` rendered.

(31 low findings: the numbered items, with items that name two fields of one unit counted twice.)

## Hand scansions added to `scan-fixes.json` (22)

Every line was scanned by hand; these are the ones where the scanner was wrong (or the line could not be fitted). Most were *valid*
hexameters with wrong syllables or quantities, so only a hand scan finds them; only 596 and 617 were COSTLY and 636 UNRESOLVED.

| line | scanner had | correct |
|---|---|---|
| 1.562 | `Te-u` split | Teū one syllable (Teucri): … tūm Teū / crī sē … |
| 1.576 | `A-e-ne-as`, `Equidem` long | Aē-nē / ās Ĕ-quĭ (Aeneas three syllables) |
| 1.580 | `A-e-ne-as` | Aē-nē / ās iam |
| 1.581 | `A-e-ne-an` | Aē-nē / an com |
| 1.588 | `A-e-ne-as` | Aē-nē / ās cla / rā(que) in |
| 1.594 | `regina` with short gi, `adloquitur` with long lo, qui (no flag) | rē-gī(nam) / ad lŏ-quĭ |
| 1.596 | COSTLY 2.0: `Tro-ius`, `A-e-ne-as` | Trō-ĭ-ŭs / Aē-nē / ās Lў-bĭ / cīs ē / rep-tŭs ăb / un-dis |
| 1.598 | `re-liqu-ias` (synizesis), one dactyl too few (no flag) | rē-lĭ-quĭ / ās Dă-nă / um ter |
| 1.611 | `nea` one syllable, `pe-` long | Ī-lĭ-ŏ / nē-ă pĕ / tit dex (see doubts) |
| 1.615 | `na` short, `ta`, `pe` long (no flag) | nā-tĕ dĕ / ā per / tan-tă pĕ / rī-cŭ-lă |
| 1.617 | COSTLY 4.4: `A-e-ne-as`, `Dardanio` elided, `Anchisae` as `sa-e` | Tūn(e) ill(e) / Aē-nē / ās quem / Dar-dă-nĭ / **ō An** (hiatus) / chī-sae |
| 1.618 | `moen` one syllable, `Si` long (no flag) | Sĭ-mŏ-en-tis, four syllables; the line is dactylic throughout |
| 1.619 | `Te-u` split | dem Teū / crum mĕ-mĭ |
| 1.625 | `Te-u` split | tis Teū / cros in |
| 1.626 | `Te-u` split, `tum` not elided | (tum) an-tī / qua Teū / crō(rum) ab |
| 1.631 | `A-e-ne-an` | Aē-nē / an in |
| 1.633–635 | (carriers) | scanner correct; entered because 636 is in the same unit (as 1.330/331/333 in aeneid-004) |
| 1.636 | UNRESOLVED | **Half-line**: mū-nĕ-ră / laē-tĭ-tĭ / ām-quĕ dĭ- / ī, three dactyls and a half foot |
| 1.643 | `A-e-ne-as` | Aē-nē / ās nĕ ĕ / nim pa-trĭ |
| 1.650 | `na`, `tus` short, `He`, `le` long (no flag) | or-nā / tūs Ar / gī(vae) Hĕ-lĕ |

**Hand-scanned lines named in the packet and the brief:**
- *Packet flags:* 596, 617, 636.
- *Greek eu:* 562 Teucri, 619 Teucrum, 625 Teucros, 626 Teucrorum (all four wrong in the scanner), and 611 Ilionea.
- *Initial Ae-:* 565 Aeneadum (scanner **right**: Ae-nĕ-ă-dum), 576, 580, 581, 588, 596, 617, 631, 643 (all wrong, A-e-ne split).
- *Consonantal i after a prefix:* the only candidate is 578 `eiectus` (ē-iec-tus; scanner right); there is no `adiicio`-type word in the part.
  Initial consonantal i (`iamdudum`, `iuvabo`, `iactatam`, `iuventae`, `iustitia`, `iuvenes`) is read correctly.
- *Hiatus:* 617 `Dardanio Anchisae` (a true hiatus; the scanner elided it) and 627 `agite O` (elision, scanner right).
  Synizesis at 614 `deinde` (standard) is right; 565 and 597 `Troiae` (Troj-ae) is right.

All other lines were also scanned and agree with the scanner.

## Doubts left for the owner (not scanner errors, not changed)

- **1.656** `ita ad naves`: with `ita` elided before `ad` the only fit makes the *i* of `ita` long. With ĭtă and no elision the line also
  scans (a hiatus), but that is not what the scanner shows. I could not settle it; left as the scanner has it. (Some texts read `iter ad
  navis` here; `ita` is Greenough's.)
- **1.611** `Ilionea`: my five-syllable scan (nē lengthened) is the only fit that keeps present `petit` short. If a reader prefers the
  synizesis `nea`, `petit` must have a long first syllable. Marked as the reason in the entry.
- **1.569** `Saturnia` with long Sā- is forced by the metre; **1.634** `viginti` with long vī-; **1.647** `Iliacis` with long Ī-; **1.655**
  `bacatum` with long ba-. All four are what the scanner has and what the line needs; none is in conflict with the references I may use.

## Title fields

`title` (`Dido hospita. Aeneas se aperit`), `titleEn` and `part` were checked against `parts.json` (cite `I.561–656`, an en dash) and the
pilot's pattern (`<English name> — Aeneid <cite>`; the `part` ends `(I.561–656)`). Both carry the citation exactly; the Latin title is
correct Latin (`aperit se`, "reveals himself"). Left unchanged. `about` was corrected and shortened (Major 11).

## Refused, or verified and kept

1. **The drafter's "dii = old genitive of dies"** — not kept as a certainty and not replaced by the opposite certainty (Major 8).
2. **`l` "We Phoenicians" against `i` "We Carthaginians" (#4)** — kept: `Poeni` is both; `l` is the literal word and the note explains it.
3. **#0 "Dido's first speech"** — kept: she has not spoken before in the poem (she appears at 494 and is named at 299, 340, 446).
4. **#9 `adforet` = `adesset`, "a wish about the present"** — kept (true).
5. **#15 "I.113–117"** — kept (Orontes' ship), identification hedged.
6. **#34 Teucer, son of Telamon, Salamis in Cyprus; #37 Hesione, daughter of Laomedon** — kept (the usual account, as marked in the notes).
7. **#4 "Poeni … hence Punic"** — kept.
8. **#23 `socias` as second singular of `socio`; `terraeque marisque` as a genitive with `casibus`** — kept.
9. **#27 `genuere` = `-erunt`** — kept. **#40 litotes `non ignara mali`** — kept.
10. **#33 `ille Aeneas` "that famous"** — kept. **`alma`** "nourishing" — kept.
11. **Latin Library variant 596 `Lybicis`/`Libycis`** — orthography only; not noted (conventions).
12. **Cuts:** all 52 units end at punctuation and run to at most five lines (#23 is four lines, cut at `socias,`; #43, #45 are four).
    Nothing was recut: `t` is untouched.
13. **`p` flags** — correct on the eight paragraph openings (561, 579, 586, 594, 613, 631, 637, 643) = units #0, 11, 17, 21, 30, 41, 44, 46
    and nowhere else; `#42` (631, second unit on the line) correctly has none.
14. **#48 / #49 / #50 order and apposition claims** — kept.
15. **No `Fitzgerald`/modern translator names** appear in `n`, `i`, `l`.
16. **`draft.py`** — not mirrored (`units.json` is authoritative).
17. **Notes length** — all are within the validator's 140-word limit (longest after edits: #23, 107 words).
