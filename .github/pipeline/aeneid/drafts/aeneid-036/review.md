# aeneid-036 (V.485–579) — adversarial review

Two passes over all 46 units. Pass 1: every grammatical label in every note; Latin to `l` word by word; `l` against `i`; speech marks; echoes of known versions. Pass 2: re-read of each changed unit, then a hand scansion of every flagged line and every line with Greek eu, initial Ae-, consonantal i, hiatus, Iulus, Hippocoöntis. `t`, the source and the `parts.json` sha are untouched (checked: every `t` identical before and after). Edits were made by script to `units.json`; scansion fixes were added to `scan-fixes.json` (additions only, no existing entry disturbed).

Counts: **11 major, 17 medium, 12 low** (40 findings).

## Major (11)

Scansion (9). All lines checked by simulating the build's scanner pass plus the new entries: no UNRESOLVED or COSTLY remains, and all 46 units get `sc`.
1. 5.485: Aeneas split A-e-ne-as. Ae-nē-ās, three syllables. Entry added.
2. 5.514: Eurytion split E-u, and the a of fratrem shortened. Eu is one syllable and fratrem elides before it (tr(em)Eu-rў-tĭ | ōn in | vō-ta vo | cā-vit). Entry added. (495 and 541 have the same name and the scanner's fit there is right.)
3. 5.530: Teucri split Te-u. Entry added.
4. 5.531: Aeneas split. Entry added.
5. 5.545: Aeneas split. Entry added.
6. 5.546: consonantal Iu- and short co, mi lengthened (COSTLY 2.0). Iulus is Ĭ-ū-lus; the line fits only with sese read sēsē (marked UNCONFIRMED in the entry). Entry added.
7. 5.569: Iulo as consonantal, spondaic fifth foot (COSTLY 2.0). Vowel I, dactyl. Entry added.
8. 5.570: Iulus likewise, every foot a spondee (COSTLY 2.0). Entry added.
9. 5.574: half-line `fertur equis.` UNRESOLVED, which would stop the build and leave unit 43 with no `sc`. Hand scansion `fĕr-tŭr ĕ | quīs` entered, and 5.573 entered as a carrier (scanner's own fit, checked) because it shares the unit.

Grammar (2).
10. Unit 11 (511): "the preposition set between adjective and noun in 'ab alto'" is false: in `malo… ab alto` the noun comes first and `ab` stands between noun and adjective. Reworded.
11. Unit 23 (533): "its object, 'honores', waits for the next line" is false: `honores` is the object of `ducere`, not of `sume`. Reworded (object understood; the gift is named at 535). `i` changed from "Take them" to "Take it".

## Medium (17)

12. Unit 1 (490): the note offered `aerea galea` as a possible ablative; that leaves `accepit` without a subject. Alternative removed.
13. Unit 6 (500–501): `l` left `viri` untranslated ("each man for himself"). Now "for himself each of the men".
14. Unit 8 (505): the note took `pennis` with `timuit` (means or manner) while `l` and the Latin group it with `exterrita`. Now `exterrita pennis`, ablative of respect.
15. Unit 12 (512): `l` left out `in` before `nubila`. Now "and into the lofty clouds".
16. Unit 13 (514): the misprint note was buried mid-note. Rule 5b: the note now opens "The print has 'Pota', a misprint for 'vota', corrected here…", says `t` keeps the print; `l` and `i` already read `vota`.
17. Unit 14 (517): `l` and `i` read `decidit` as present ("falls", "tumbles") while the note calls it a perfect beside `reliquit`. `l` and `i` now past.
18. Unit 25 (535–538): stray opening “ at the head of `i`, in a continuation unit (the speech opens in unit 23). Removed.
19. Unit 31 (548–551): the missing comma before `ait` was mentioned only at the end. Note now opens with the print's reading, cites rule 5, says `t` keeps the print; `l` and `i` already have the comma and close after "tell".
20. Unit 33 (554): "'omnis' is Greenough's spelling of the nominative feminine singular" is wrong (that is simply the ordinary form) and hid a real ambiguity. Now: nominative singular with `iuventus` (taken here) or his spelling of accusative plural `omnes` with `quos… euntes`.
21. Unit 34 (556): misprint note did not open with the print's reading and `l` kept the lowercase. Note now opens "The print has 'omnibus' … a misprint for 'Omnibus', corrected here", says `t` keeps the print; `l` now "To all…" (`i` already capital).
22. Unit 42 (570–572): "The last two lines are 538 with 'ferre' changed to 'esse'" is false; only 572 is. Corrected.
23. Unit 45 (577): `i` "ridden their gaze over the whole gathering and the eyes of their own people" garbles `lustravere… oculosque suorum`. Now "ridden round the whole assembly and past the eyes of their own people".
24–28. Units 27, 30, 41, 42, 43: reader-facing notes mentioned the scanner ("The scanner flags …", "marks it UNRESOLVED"). Deleted (no published part does this). The half-line note at 574 now says what the published 020 note says about hemistichs.

## Low (12)

29. Unit 3: `victor` called predicative; it is in apposition to `Mnestheus`.
30. Unit 6: `quisque`/`viri` described as a "sense agreement"; reworded with the `l` fix (item 13).
31. Unit 12: `fugit` "fled, flees away, a perfect tense" contradictory; now says the form could be present or perfect and the sense is perfect.
32. Unit 17: "could also be an ablative of quality" for `magno augurio` removed (dative of purpose is the only reading that works with `futurum`).
33. Unit 19: `i` "trail their long hair of light" and "torn loose" are close to well-known versions of 527–528; rephrased ("wrenched from the sky run across it, flying, and drag a long train of light behind them").
34. Unit 25: "genitive of source" for `Ipsius Anchisae… munus`; now possessive genitive (the bowl was Anchises's).
35. Unit 27: `i` "honest Eurytion" for `bonus` (the note says good, generous); now "good-hearted".
36. Unit 28: `i` "Next to him" adds a reference the Latin does not make; now "Next steps up".
37. Unit 30: `i` "into a trusted ear" is a stock rendering of `fidam ad aurem`; rephrased ("says to him in confidence").
38. Unit 33: note gave `pariter` as "together" against `l` "equally"; now both.
39. Unit 43: `cetera` (neuter plural) with feminine `pubes` unexplained; one clause added.
40. Unit 44: "the fathers who fought at Troy" is a guess; now "their forefathers".

## Refused or left as drafted (no change)

- 5.520 `aerias`: scanner reads a-e-ri-as (four syllables, aerius with ā-ĕ-rĭ-); this is correct, and the line fits only so. Not entered.
- 5.495 and 5.541 Eurytion: the scanner's fit (Eu one syllable, tuus two shorts at 495) is right. Not entered.
- 5.490 `aerea`, 5.518 `aetheriis`: Ae- correctly one syllable. 5.492 Hippocoöntis (Hip-pŏ-cŏ-ōn-tis): correct. 5.488, 5.490, 5.509, 5.542 `traiecto`, `deiectam`, `deiecit`: consonantal i handled right. 5.522 `obicitur`: quantities (long, short, short, long) are right, though the scanner syllabifies o-bi- rather than ob-ji-. Not entered.
- 5.571 `Sidonio` with short -do-: only fit; scanner right.
- Aeneas, Teucri, Iulus entries follow the published precedents (1.617, 1.556, 2.674, 4.140).
- Unit 5 `i` "old as he was": implied by `iuvenum laborem` and `et ipse`; left.
- Unit 8 `i` "quivered": agrees with the note that the Latin Library's `micuitque` would give the same picture; left.
- Unit 13 `l` "missile" singular for `tela`: the note already explains the plural for one arrow; left.
- Unit 7 "transferred epithet" for `volucres auras`: debatable, harmless; left.
- Unit 36 `levis` as accusative plural: the alternative (nominative with `pars`) is possible, but the note's choice is defensible; left.
- Misprints in `t` (514 `Pota`, 551 `”ait`, 556 `omnibus`): `t` not changed, per the instruction and rule 5b (it must match the pinned source).
- Source and `parts.json` sha: not touched.

## scan-fixes.json entries added (10)

5.485, 5.514, 5.530, 5.531, 5.545, 5.546, 5.569, 5.570, 5.573 (carrier), 5.574 (half-line).

Doubtful quantities for QUESTIONS: `sese` read sēsē at 546 (second syllable long); Sidonio with short -do- (571); Eurytion as Eu-rў-tĭ-ōn (495, 514, 541); Atys with short A- and 'tys' long by position (568, 569); Epytides with long E- (547, 579).
