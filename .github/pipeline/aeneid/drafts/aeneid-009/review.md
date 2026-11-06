# aeneid-009 — review (II.1–104)

Adversarial review in two passes, from the Latin and public-domain references only (Lewis & Short, Allen & Greenough, general
knowledge of the commentators). No modern translation was opened and no English wording was recalled as a source.

- **Pass 1:** every unit, field by field. Every grammatical label in every `n` was checked against the form in its line; the Latin
  against `l` word by word and line by line; `l` against `i`; `i` for remembered English (II.49 and the Laocoön and Sinon speeches
  above all); every cite and generalisation in `n` and `about`; speech marks; `p` flags (the six Greenough paragraphs, 1, 21, 40, 57, 67, 77,
  all land on the right units); the five-line limit and the cut points. Then **all 104 lines** were scanned by hand, syllable by syllable,
  against the natural quantities (not "does the scanner find a hexameter"): the shared scanner accepts any metrical parse and hands back
  valid lines with wrong quantities.
- **Pass 2:** a re-read of the edited file (five further small changes), then a script that applies `scan-fixes.json` over the scanner
  line by line exactly as `build_aeneid.py` does and runs the validator's hexameter test on all 104 lines (**104 pass, 0 fail**; the three
  scanner reports, 2.41 COSTLY, 2.66 UNRESOLVED, 2.68 COSTLY, are all now covered by an entry), a check that `t`, `ln`, `v`, `p`, `title`,
  `titleEn` and `part` are byte-identical to the draft and that every `l` keeps the line count of its `t` (and no `i` has a line break),
  and a word-count check of the notes (one 9-word note expanded, one 147-word note trimmed; all now 15–140).
- **The full build refuses, for a reason outside the text** (see "Build" below). Nothing was published; `parts.json` and `LOG.md` untouched.
  `draft.py` was **not** updated and now disagrees with `units.json`; **do not re-run `make_units.py`**, it would overwrite the review.
  `new-renderings.md` still shows the old II.49 `i`; the new one is in `units.json`. Edits to `units.json` were made by script
  (json load / modify / dump, `ensure_ascii=False`, `indent=1`; an unedited round trip is byte-identical).

**Counts:** Major 9 · Medium 28 · Low 56 (93 findings, each a field of a unit) · scan fixes added 16 (15 lines the scanner had wrong,
1 confirmation of a COSTLY flag) · refused / verified and kept 24. Changed: 48 of 59 units (0 `t`, 11 `l`, 17 `i`, 43 `n`) and `about`.
Title, `titleEn` and `part` were checked and left alone.

## Build

`python3 build_aeneid.py aeneid-009` refuses before writing anything: `BUILD REFUSED: unit 6: ends mid-word at line 13`. Cause: Greenough
prints `incipiam.Fracti` (II.13) with no space after the full stop. Unit #7 ends at `incipiam.` and #8 begins at `Fracti` (this is what
`t` must be: cut from the source, the note of #7 already says so), but the tiling loop in `build_aeneid.py` requires a space or newline
at every unit boundary (`if S[pos] not in ' \n': die(... ends mid-word ...)`). Nothing in the text can be changed to satisfy it; the
check needs to accept a boundary after terminal punctuation (`A.TERMINAL`), or the source line needs a normalisation. I did not touch
the build script. The hand scansions were tested instead by the scripted pass above, which does what the build does after the tiling step.
The next refusal, once this is cleared, will be the missing `gloss.json` (not yet written for this part; `known-forms.json` and
`novel-forms.json` are in the folder).

## Speech marks

Aeneas's long speech (II.3–104, its first line follows the colon at line 2) carries none in Greenough, so none in the units. Laocoön 42–49
opens #26, closes #32; the Sinon cry 69–72 opens #41, closes #42; Sinon 77–104 opens #47, closes #59. `t`, `l`, `i`: 3 openers and 3
closers each, in the same units. #46 (the bracketed line 76) is outside any mark. No change needed.

## Line 76 (the bracketed line)

Brackets are carried in `t`, `l` and `i`; the note of #46 says Greenough marks the line as spurious and that the Latin Library omits it.
Scansion is regular (SDSDS, with Il(le) elided into haec).

## Remembered English

Checked from memory of the well-known versions, not by collation. Rephrased: **#32 (II.49)** — the old `i` ("Whatever that thing may be,
I fear the Greeks, and fear them with presents in their hands") kept the whole familiar shape (whatever it is / I fear the Greeks /
gifts); now "Whatever this thing is, I am afraid of the Greeks, even when it is presents that they bring." The `l` ("Whatever it is, I
fear the Danaans, and them bringing gifts") is the structural layer and stays. **#26** ("what madness is this"), **#28** ("gift of the
Greeks is free of treachery"), **#31** ("do not trust the horse"), **#41** ("what land, what seas can ... receive me" shape). Looked at
and kept: #36 "sure of his nerve and ready either way", #42 "a wretch like me", #39 "learn what they all are", #54 "like a madman", #59
("take your vengeance now ... the sons of Atreus would pay a great price for it"), #3 "a grief too great for words" (a plain rendering of
*infandum*; the Virgil-quotation "unspeakable grief" is in `l` only).

## Major (false label, false fact, wrong translation, or an unsafe certainty)

1. **#4 (II.5) `l`** — l: "quorum" is genitive plural, "of which", not "in which".
2. **#35 (II.54) `n`** — n: "for Romans the left was often the unlucky side" is false or at best unsafe (in Roman augury the left was usually the favourable side); gloss reduced to what the word means here.
3. **#36 (II.57) `l`** — l: "to the great king with great shouting" - magno agrees with clamore, not regem; "interea" and "iuvenem" re-ordered to the Latin.
4. **#36 (II.57) `n`** — n: same error as l - magno does not agree with regem.
5. **#45 (II.74) `n`** — n: "the three clauses without et are asyndeton" was false (quo sanguine cretus and quidve ferat are joined by -ve); memoret is the verb the questions hang on and is not a jussive in an indirect question.
6. **#47 (II.77) `n`** — n: "'vera' as predicate (the hyperbaton wraps the verb around the verse)" - vera is the noun-adjective pair with cuncta, not a predicate, and the hyperbaton remark was meaningless.
7. **#52 (II.86) `n`** — n: the subject of stabat/vigebat is Palamedes, and the note let it read as the father (or Sinon); the invented inference about the father's poverty ("could not afford to send his son as anything but a follower") removed.
8. **#53 (II.90) `n`** — n: "indignant with myself" - Sinon is not angry at himself; mecum means "within, to myself".
9. **#54 (II.94) `n`** — n: "with 'me esse' dropped" - me is in the line; only the infinitive is dropped.

## Medium

1. **about `about`** — about: the Greeks hide on a deserted shore of Tenedos (deserto in litore), not behind the island.
2. **#1 (II.1) `n`** — n: "unexpressed subject 'omnes'" - omnes is expressed in the line; it is the subject of both verbs.
3. **#2 (II.2) `n`** — n: the toro / ab alto agreement is now stated; the parenthetical repeat of Book I removed.
4. **#4 (II.5) `n`** — n: "a second object to renovare" was a guess at the construction; now stated loosely.
5. **#4 (II.5) `n`** — n: unverifiable claim ("famous in Latin") removed.
6. **#5 (II.6) `n`** — n: "Ulysses is hard for his cunning" is not what durus says (hard, stern); invented explanation removed.
7. **#8 (II.13) `n`** — n: "a noun in apposition with equum" mislabelled instar; "hill" corrected to mountain.
8. **#11 (II.18) `n`** — n: "ablative of material" - the ablative with complere is means.
9. **#12 (II.21) `n`** — n: "an open roadstead with no shelter" was an invented detail.
10. **#14 (II.25) `n`** — n: only petiisse was called a contraction; abiisse is the same kind of form (abeo, perfect abii).
11. **#17 (II.27) `n`** — n: "the Doric region of Greece" is not a safe description.
12. **#19 (II.30) `n`** — n: "dative of possession" is wrong for classibus hic locus.
13. **#22 (II.32) `l`** — l: line division did not follow t (line 1 of t is only "primusque Thymoetes"); redistributed within the same three lines.
14. **#22 (II.32) `n`** — n: "elder" is not in the line (unverifiable).
15. **#23 (II.35) `n`** — n: "the sea or fire" / "the third course" - the -que after subiectis joins the first two verbs; wording made accurate.
16. **#25 (II.40) `i`** — i: "hot-faced" invented a detail; "at the head of a great crowd" misread comitante caterva (the crowd accompanies him).
17. **#32 (II.49) `i`** — i: II.49. The Greeks-bearing-gifts shape (and "Whatever it is") is what every reader knows; rephrased so that the fear comes first and the gifts are a concession, still reading et as "even".
18. **#32 (II.49) `n`** — n: superlative claim ("most-quoted in the book") unverifiable.
19. **#32 (II.49) `n`** — n: pipeline housekeeping does not belong in a reader note.
20. **#33 (II.50) `i`** — i: "drove ... and hurled it" gave two verbs for contorsit; one remains.
21. **#35 (II.54) `n`** — n: "that is, to break open" was a guess.
22. **#38 (II.63) `n`** — n: garbled label.
23. **#49 (II.79) `n`** — n: "the opening of an enumeration" is not what the phrase is.
24. **#50 (II.79) `n`** — n: "a play on its two senses" is not in either clause (both mean "make him X").
25. **#51 (II.81) `n`** — n: unverifiable claim about the reader of Virgil's day.
26. **#52 (II.86) `i`** — i: "in his rule" removed; nos given as "I".
27. **#52 (II.86) `l`** — l: "his kingship" for regno - the subject of stabat is Palamedes (illi), and regno is the realm, not his own kingship.
28. **#54 (II.94) `n`** — n: sequence-of-tenses point made precise.

## Low

1. **#1 (II.1) `l`** — l: "fixed" is not in the Latin (ora tenebant, imperfect).
2. **#1 (II.1) `n`** — n: wording ("turned") made to match the sense.
3. **#2 (II.2) `l`** — l: "from on high" for ab alto misplaced the adjective; alto agrees with toro (the high couch).
4. **#3 (II.3) `l`** — l: eruerint is a perfect subjunctive; "have overthrown" is the nearer English.
5. **#3 (II.3) `n`** — n: dependence stated more carefully (the clause explains the grief; it is not governed by the infinitive).
6. **#4 (II.5) `i`** — i: "sights" narrowed the sense of the neuter relative; "myself" kept as "with my own eyes".
7. **#5 (II.6) `n`** — n: a potential (would), not a deliberative (should I?).
8. **#8 (II.13) `i`** — i: "hill" for montis; "tot" (so many) restored.
9. **#8 (II.13) `n`** — n: ship-timber aside dropped; case named; scansion point for the reader added.
10. **#9 (II.17) `n`** — n: "offering" -> "vow" (votum; the i already says vow).
11. **#11 (II.18) `n`** — n: "repeatedly" made specific.
12. **#12 (II.21) `n`** — n: "small ... visible" softened to what the line says (est in conspectu).
13. **#13 (II.24) `n`** — n: "active sense" was loose.
14. **#14 (II.25) `i`** — i: "taken them home" is more than petiisse (sought, made for); and rati takes the Trojans as subject of the thought.
15. **#15 (II.26) `n`** — n: case added.
16. **#16 (II.27) `n`** — n: 9 words (validator WARN); expanded.
17. **#17 (II.27) `n`** — n: "where their ships had been beached" is an addition.
18. **#19 (II.30) `l`** — l: classibus is plural.
19. **#20 (II.30) `n`** — n: Aeneas is the speaker.
20. **#22 (II.32) `n`** — n: "locative-like" replaced by the plain label.
21. **#22 (II.32) `n`** — n: ambiguity of dolo stated.
22. **#24 (II.39) `n`** — n: "a very Roman image" is not supportable.
23. **#25 (II.40) `n`** — n: "another" dropped.
24. **#26 (II.42) `i`** — i: remembered English ("what madness is this"); rephrased.
25. **#26 (II.42) `n`** — n: unverifiable generalisation removed.
26. **#28 (II.43) `i`** — i: remembered English ("gift of the Greeks is free of treachery"); rephrased.
27. **#30 (II.45) `n`** — n: "(to climb the walls)" - purpose not in the line (the purpose clause follows: to look into houses, to come down on the city).
28. **#31 (II.48) `i`** — i: remembered English ("do not trust the horse"); rephrased.
29. **#32 (II.49) `n`** — n: hedged.
30. **#34 (II.52) `n`** — n: "though no one hears what it means" was an invention.
31. **#34 (II.52) `n`** — n: gloss of recutio.
32. **#35 (II.54) `l`** — l: fuisset supplied in the second protasis.
33. **#35 (II.54) `n`** — n: the subject of impulerat stated.
34. **#35 (II.54) `n`** — n: the ellipsis in the first half of the protasis stated.
35. **#35 (II.54) `n`** — n: trimmed to keep the note under 140 words (the gloss "Argolic = Greek" is in the l).
36. **#37 (II.62) `i`** — i: "carry through" over-reads versare.
37. **#37 (II.62) `n`** — n: "outcomes" misdescribed versare dolos.
38. **#39 (II.65) `n`** — n: hedge.
39. **#40 (II.67) `n`** — n: "the region around Troy" is loose.
40. **#41 (II.69) `i`** — i: remembered English ("what land, what seas can now receive me"); rephrased.
41. **#42 (II.70) `i`** — i: super (and in addition) restored.
42. **#42 (II.70) `l`** — l: cui is "to whom" (dative), not "who have".
43. **#45 (II.74) `i`** — i: "what he has come to tell us" repeated "tell" and added to ferat.
44. **#46 (II.76) `n`** — n: wording.
45. **#46 (II.76) `n`** — n: "stage direction" trimmed.
46. **#47 (II.77) `i`** — i: inquit restored; i is now a faithful twin of l (equidem still omitted).
47. **#49 (II.79) `i`** — i: hoc is "this".
48. **#51 (II.81) `i`** — i: "whom ... mourn him" doubled the object.
49. **#51 (II.81) `l`** — l: aliquod agrees with nomen.
50. **#51 (II.81) `n`** — n: case and meaning.
51. **#52 (II.86) `n`** — n: Latin Library orthographic variant (consiliis/conciliis) removed: conventions say not to note orthography.
52. **#54 (II.94) `n`** — n: parallel stated.
53. **#55 (II.97) `n`** — n: gloss of labes widened.
54. **#56 (II.100) `n`** — n: forward reference made explicit.
55. **#58 (II.102) `n`** — n: wording.
56. **#59 (II.103) `n`** — n: tense point restated.
## Scan fixes (scan-fixes.json: 16 entries, each with its reason)

All 104 lines were scanned. The 88 lines not listed here were checked syllable by syllable and the scanner's parse is the right one.
Wrong in the scanner (15): **2.2** *Aeneas* (Ae- split; Ae-nē-ās, 15 syllables); **2.26** *Teucria* (Greek eu split, se short; 13 syllables);
**2.48** *Teucri* (eu split, and cre- short / -di- long: the reverse of crēdĭtĕ); **2.37** *subiectis* (consonantal i after the prefix read as
a vowel); **2.14, 2.36, 2.44, 2.65** *Danaum* read as Da-naum, a diphthong, with the first syllable long (and in 2.36, 2.65 the whole of -naum
elided); **2.3** *regina iubes* (re-gi short / na long, iu long: wrong quantities in a valid line; rē-gī-nă iŭ-bēs); **2.9** *suadent*
(su-a two shorts: sua is one long syllable); **2.78** *Argolica* (go and li long, ca short: wrong quantities in a valid line);
**2.84** *quia* (contracted to one syllable); **2.100** *requievit* (rĕ-quĭ-ē-vit read as re(qu)-ie-vit, with a long re-); **2.66** the half-line
*disce omnes*, UNRESOLVED (hemistich entry, same form as 1.534 and 1.560); **2.68** *circumspexit* (the quantities were right but the syllables
were shown as cir-cums-pe-xit; now cir-cum-spex-it). Entered as a confirmation only: **2.41** *Laocoön*, the COSTLY flag cleared (four
syllables Lā-ŏ-cŏ-ōn; the scanner's parse was right).

**Hand-scanned lines named in the packet and the brief, all checked individually:** 2.2 Aeneas (wrong, fixed); 2.12 *animus
meminisse horret ... refugit* (right; quam-quam elides, refūgit with long u forced by the sixth foot); 2.13 *incipiam.Fracti* (right,
incipiam and Fracti are two words; the full stop with no space does not affect the scansion); 2.16 *aedificant ... abiete* (right; Ae- is a
diphthong here, abiete is ab-je-te); 2.26 *Teucria* (wrong, fixed); 2.34 *seu iam* (right; seu one syllable, iam consonantal i, no hiatus);
2.41 (right, entry added); 2.45 *inclusi* (right); 2.48 *Teucri* (wrong, fixed); 2.54 *deum* (right; dĕ-um two syllables, the only fit);
2.55 *Argolicas* (right); 2.64 *inludere* (right); 2.66 (fixed); 2.68 (fixed); 2.69 *Heu ... inquit* (right; tellūs long); 2.76 (right);
2.79 *si miserum ... Sinonem* (right); 2.100 (wrong, fixed); 2.103 *iamdudum* (right). Also checked, with no change: 2.7 (-ve elides before
aut), 2.11 (*supremum* with long su-, the only fit), 2.21, 2.24, 2.30 (*hic* long before a vowel), 2.35, 2.50-2.53, 2.56, 2.60, 2.62, 2.77,
2.81 (*pervēnit*, perfect, long ve-), 2.85, 2.88, 2.102, 2.104.

## Refused findings (verified and kept)

1. #2 *pater* as Aeneas's regular title: true (and the note says "in the poem", not "always").
2. #3 *Danai* "one of the commonest names for the Greeks": true.
3. #7 *quamquam ... horret, refugit* "concession, indicative": true.
4. #7 the missing space in `incipiam.Fracti`: left in the note; `t` is cut from the source and cannot be changed.
5. #22 *duci ... locari* "present passive infinitives with the accusative 'equum' understood": the usual reading; kept.
6. #27 *hostis* as accusative plural (-is) and subject of the infinitive: true.
7. #35 pluperfect indicative *impulerat* for the apodosis: the usual explanation (A&G 517); kept.
8. #35 the Latin Library variant *staret* is noted because it changes the sense; kept. The LL variants *volgus*/*uulgus* (2.39, 2.99),
   *Laocoon* (2.41), *quidquid* (2.49), *omnes*/*omnis* (2.66) and *consiliis*/*conciliis* (2.89) are orthographic or morphological and are
   not noted (the *quidquid* mention in #32 is the familiar form, allowed by the conventions; the *conciliis* remark in #52 was removed).
9. #41 *inquit* with no commas: Greenough's printing, shown in the note; kept.
10. #46 "the Latin Library does not print it at all": agrees with the packet (LL empty at 2.76); kept.
11. #48 *me ... negabo* "accusative and infinitive with esse dropped": true (me is expressed, esse dropped).
12. #50 "Sinonem is the first time the prisoner is named": true (79).
13. #51 *Belidae* "descendant of Belus": true (Palamedes' line goes back to Belus through Nauplius); *demisere neci*, *cassum lumine*: true.
14. #51 the anacoluthon (the *si* clause is never completed): a fair description; kept.
15. #56 *Calchante ministro* as ablative absolute: true.
16. #58 *omnis* = *omnes* with *Achivos*: true.
17. #55 *volgum* as the masculine accusative (at 39 neuter *volgus*): true.
18. #30 *aut ... aut ... aut* "three alternatives": the *aut hoc ... aut haec ... aut aliquis* triplet is plain; kept.
19. #43 *Quo gemitu* as connecting relative: true.
20. #6 "the stars falling (cadentia) are the stars setting" and the courtesy remark: interpretive but harmless; kept.
21. #25 "Greenough keeps the diaeresis in 'Laocoön'": true to the packet (the LL prints *Laocoon*).
22. #33 *validis ... viribus*, *ingentem ... hastam* interlocking (ABAB): true.
23. #12 *dum ... manebant* with the imperfect indicative, plural *regna* for the one kingdom: true.
24. #38 *ruit* singular beside plural *certant* for the collective *iuventus*: true.
