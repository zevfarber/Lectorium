# aeneid-008 — review (I.657–756)

Adversarial review in two passes, from the Latin and public-domain references only (Lewis & Short, Allen & Greenough, general
knowledge of the commentators). No modern translation was opened and no English wording was recalled as a source.

- **Pass 1:** every unit, field by field. Every grammatical label in every `n` was checked against the form in its line (the five
  the drafter flagged first), the Latin against `l` word by word and line by line, `l` against `i`, remembered English in `i`,
  speech marks, `p` flags, the five-line limit and the cut points, and the factual claims in `n` and `about`. Then **all 100 lines**
  were scanned by hand, syllable by syllable, against the natural quantities (not merely "does the scanner find a hexameter"): the
  shared scanner accepts any metrical parse and, as in 1.522, hands back valid lines with wrong quantities.
- **Pass 2:** a re-read of the edited file, a script that applies `scan-fixes.json` over `scan_latin.scan_story` exactly as
  `build_aeneid.py` does and runs the validator's hexameter test on all 100 lines (**100 pass, 0 fail**, no COSTLY or UNRESOLVED report
  left), a check that `t`, `ln`, `v`, `p`, `title`, `titleEn` and `part` are byte-identical to the draft and that every `l` keeps the
  line count of its `t` and no `i` has a line break, and a word-count check of the notes (one was over 140 and was trimmed).
- **The full build was not run** and nothing was published. `draft.py` was **not** updated and now disagrees with `units.json`;
  **do not re-run `make_units.py`**, it would overwrite the review. Edits to `units.json` were made by script (json load / modify /
  dump, `ensure_ascii=False`, `indent=1`).

**Counts:** Major 5 · Medium 25 · Low 31 (61 findings in text) · scan fixes added 18 (17 lines the scanner had wrong,
1 carrier line) · refused / verified and kept 16. Changed: 37 of 51 units (0 `t`, 15 `l`, 6 `i`, 37 `n`) and `about`. Title,
`titleEn` and `part` were checked and left alone.

**Speech marks.** Venus 664–688 opens #4, closes #14; Dido's toast 731–735 opens #36, closes #37; Dido 753–756 opens #49, closes #50.
`t`: 4 openers, 3 closers; `l`: 4 and 3; `i`: 3 and 3. The extra opener is the second “ Greenough prints before `insidias` (754) with no
closing mark between; it is a stray mark inside one speech. It stays in `t` (never edited) and in `l` (which mirrors `t`) and is left out of
`i` (so the English balances); #49's note says so. The validator will therefore print a WARN for `t` and `l` (it is a warn, not a fail);
that is expected and not a defect. No other change to the marks was needed.

**Line 711 (the bracketed line).** Brackets are carried in `t`, `l` and `i`; the note of #25 (and #24, and `about`) says Greenough marks the
line as spurious, that it repeats 648–649, and that the archive keeps it. One unverifiable claim in that note ("some manuscripts omit it") was
replaced. Scansion is regular (SSDSDS).

**Remembered English.** Checked from memory of the well-known versions, not by collation. Rephrased as stock phrases of older versions:
#47 / `about` ("drank deep and long of love", "drinks long draughts of love"), and the casual "all sorts of talk". Nothing else is a
distinctive echo (#4 "make light of the Typhoean bolts", #14 "overjoyed", #36 "Jupiter—for they say you are the giver of laws to guests"
and #41 "labours of the sun" were looked at and kept).

**The drafter's doubtful labels.** 665 *patris summi*: the claim that Cupid is called Jupiter's child is not in the line (#4, major).
671–2 *hospitia*: "plural for singular, abstract made concrete" removed (#7). 679 *pelago et flammis restantia*: the case is open (datives
or ablatives); now hedged (#11). 712–4 *pesti devota*: right as it stood (dative with *devota*), wording made explicit (#26).
724 *vina coronant*: ambiguity stated, Homer cite removed (#31).

## Major (false label, false fact, wrong translation, or an unsafe certainty)

1. **#4 `n`** — 665 patris summi (flagged by drafter): asserted that Cupid is called Jupiter's child, which the line does not say; also misspelt 'Typhoea' for the form in the text, 'Typhoia'.
2. **#11 `n`** — 677 false fact: Ascanius is named at 659 and 689-691 is not the first naming.
3. **#12 `n`** — 682 false label: 'qua' cannot be 'aliqua' agreeing with a noun; the subject is 'puer', so it is the adverb.
4. **#16 `n`** — 694 false label: a participle does not govern 'umbra'; both are ablatives of means.
5. **#49 `l`** — 754 l: 'he says' for 'inquit' of Dido (she); wrong in the translation.

## Medium

1. **#1 `n`** — 661 bilinguis: 'for bilinguis = bilingues' says nothing; now the ending is named.
2. **#2 `i`** — 662 i: 'rouses her anger again' changed the sense (urit = burns/torments her, Venus); l already said 'burns her'.
3. **#5 `l`** — 667-8 l: 'pelago' stood in the second line and 'omnia circum' ran over; line division now follows the Latin (667 ends circum).
4. **#7 `n`** — 671-2 hospitia (flagged by drafter): 'plural for singular, abstract made concrete' was a guess at the grammar; the plural of hospitium needs no such label.
5. **#11 `n`** — 679 pelago et flammis restantia (flagged by drafter): case of 'pelago et flammis' stated flatly; now hedged.
6. **#14 `n`** — 686 regalis: 'for regalis' says nothing.
7. **#15 `i`** — 690 i: 'goes off' is not 'incedit' (he walks, he does not leave yet).
8. **#17 `n`** — 696 'who had not yet seen them' was invented; dative simply 'to'.
9. **#19 `n`** — 700 'super after its noun': super stands after 'strato', not after 'ostro'.
10. **#20 `n`** — 702 line cite 1.136-143 from memory, cannot verify here; now book only.
11. **#21 `n`** — 704 line cite 7.103 from memory; now book only.
12. **#25 `n`** — 711 'some manuscripts omit it' cannot be verified here.
13. **#26 `n`** — 712-4 pesti devota (flagged by drafter): checked: devota + dative is the ordinary construction (devotus morti), so the label stands; wording made explicit.
14. **#30 `n`** — 720-2 n: Boeotia spring and ghost claims softened ('whose ghost she has remained faithful to' was wrong: it is his memory); praevertere gloss rewritten (it was 'ahead of Sychaeus's memory', which is not what it governs); 'key sentence' dropped.
15. **#31 `n`** — 723 garbled grammar ('+ perfect or ablative absolute'; 'second course followed').
16. **#31 `n`** — 724 vina coronant (flagged by drafter): Greek form and line cite Odyssey 1.148 from memory, removed; ambiguity of 'coronant' stated.
17. **#33 `n`** — 727 false description of the word order ('conquer' is the last word, not between).
18. **#36 `n`** — 732 'jussive or optative': a wish is optative.
19. **#37 `n`** — 734 'jussive' for a wish.
20. **#37 `l`** — 735 l: 'with favouring words' added a noun and changed the participle 'faventes'.
21. **#40 `n`** — 740-1 n: 'invention of Virgil's' cannot be verified; line cites 1.325ff, 8.62ff and the Apollonius comparison removed; note now says personat has no object.
22. **#40 `l`** — 741 l: 'makes it sound' supplied an object ('it' = the lyre) that personat does not have, and the lyre is ablative.
23. **#45 `n`** — 745 'accusative of respect' is not the construction.
24. **#46 `n`** — 747 'cf. the Odyssey's guests at a song' unsupported; 'Troes' called 'an old form': it is the Greek nominative.
25. **#49 `n`** — 753-4 n: 'showing Virgil's reverting to direct speech' was wrong (inquit is parenthetical); leaked internal field names ('`t`', '`l`', '`i`') to the reader; Odyssey 8.572ff cite from memory removed.

## Low

1. **#2 `n`** — 662 atrox: 'standing epithet' is not established for Juno.
2. **#3 `n`** — 663 'historical present': the whole scene is in the narrative present, nothing is being recalled.
3. **#5 `n`** — 667 ut + subjunctive after nota: 'indirect clause' is not a construction; it is an indirect question.
4. **#8 `n`** — 672 'ablative of time' is not the construction.
5. **#11 `l`** — 677-8 l: 'Sidonian' stood a line early and 'city' a line late; division now follows the Latin (677 ends urbem).
6. **#12 `l`** — 680-2 l: 'recondam' (end of 681) stood in the first line; 'qua' was untranslated.
7. **#13 `l`** — 683 l: line 1 ended on 'appearance' but the Latin line ends on 'unam'; 'faciem' now precedes 'noctem… unam' as in the Latin.
8. **#14 `i`** — 687 i: 'hugs' is modern-casual.
9. **#17 `n`** — 695 'a pun' is not established.
10. **#17 `l`** — 695-6 l: 'royal gifts' was split against the Latin line division (dona ends 695, regia begins 696).
11. **#18 `l`** — 697-8 l: 'on a golden couch' (698) stood in the first line.
12. **#20 `n`** — 701 'Greek-derived' not established.
13. **#21 `l`** — 703-4 l: 'cura' (704) stood in the first line.
14. **#23 `n`** — 708 'toris' stated as ablative; either case is defensible.
15. **#24 `n`** — 710 invented detail ('a light the boy does not have').
16. **#30 `l`** — 719-22 l: every Latin line after the first was shifted (matris, incipit).
17. **#34 `n`** — 729 'context points to a libation' is not established.
18. **#34 `n`** — 729-30 clearer parse; 'founder' is not established.
19. **#34 `i`** — 730 i: 'had been used to' left the verb out.
20. **#36 `l`** — 733 l: 'for our descendants' made the accusative subject a dative.
21. **#38 `l`** — 737 l: ore is 'mouth'.
22. **#39 `n`** — 739 'new wine' invented.
23. **#39 `l`** — 739 l: Greenough prints no stop after 'auro'; l had added a semicolon.
24. **#40 `i`** — 741 i: brought into line with the corrected l.
25. **#44 `n`** — 744 etymology softened.
26. **#45 `l`** — 745-6 l: 'winter' (746) stood in the first line and 'Ocean' (745) in the second.
27. **#47 `i`** — 749 i: 'drank deep and long of love' is a stock phrase of older versions; rephrased. 'all sorts of talk' was casual.
28. **#48 `n`** — 752 stated flatly; now 'usually taken as'.
29. **about** — about: 'drinks long draughts of love' is a stock phrase of older versions; rephrased.
30. **#49 `n`** — 753 n: over the 140-word note limit (161 words); trimmed.
31. **#30 `n`** — 343– left dangling in the Sychaeus note; now 343–352.

## Scan fixes added to `scan-fixes.json` (18)

Hand-scanned lines (every line was scanned; the rest agree with the scanner's quantities): 657, 663, 667, 675, 683, 686, 690, 697, 699, 709, 715, 722, 723, 728, 740, 747, 753, 754.
- **1.657** — Cȳ-thĕ-rē-ă four syllables (as 1.257); novas has short no-
- **1.663** — āliger has short -li-, -ge-; scanner's li/ge long; needs Ergo not elided (flagged, see below)
- **1.667** — Aeneas split A-e-ne-as; 17 syllables
- **1.675** — Aeneae split
- **1.683** — carrier: hand scan agrees with the scanner (flagged COSTLY line)
- **1.686** — rēgālis (ga long); lăticem (la-ti short)
- **1.690** — Ĭūlī trisyllabic (precedent 1.556); fifth foot dactyl
- **1.697** — venit present; aulaeis au-lae-is; sē rē-gī-na long
- **1.699** — Aeneas split
- **1.709** — Aeneae split; Ĭūlum trisyllabic
- **1.715** — Aeneae split
- **1.722** — desuēta: dē long, sue one syllable
- **1.723** — quiēs two syllables; prima -ma short
- **1.728** — rēgīna long rē-, gī-
- **1.740** — Ĭōpas, vowel I; fifth foot dactyl
- **1.747** — ingeminant short ge, mi; Tyrii short Ty- (poem's convention)
- **1.753** — prīma long; ŏrīgo short ŏ-; hospes short
- **1.754** — Danaum three syllables

The four lines `packet.md` flagged: **683** the scanner was right (carrier entry); **690**, **709**, **740** it was wrong (Iulus/Iopas
treated as consonantal, Ae- split on 709). Greek *eu*: none in the part. Initial *Ae-*: 667, 675, 699, 709, 715 (all fixed);
705 *aetate*, 756 *aestas* and 697 *aulaeis* were fine or fixed under other findings. Consonantal *i* after a prefix: none (668 *iniquae* is
in + *iniquus*, with a vowel i). Hiatus: none in this part (735 *O coetum* is not one).

## Refused / verified and kept (16)

1. **683** — flagged COSTLY, hand scan agrees with the scanner: kept (recorded as a carrier entry).
2. **682** *mediusve occurrere* — the scanner's parse needs *-us* long before the elided *-ve* and a vowel; I cannot justify that quantity
   from the references available and could not find another parse that fits. **Kept as the scanner has it; flagged for the owner.**
3. **663** *Ergo his aligerum* — the only parse that keeps the natural quantities of *āligerum* is with *Ergo* not elided before *his*.
   Hand scansion entered, **flagged for the owner**: if the established reading elides *go*, the line cannot have these quantities.
4. **703** *intus*: the parse needs *-tus* long; accepted as the scanner has it (only fitting parse).
5. **733** *huius*: *hū-ius* with long *hu-* accepted (only fitting parse).
6. **693** *amāracus*: *ma-* long (only fitting parse); not changed.
7. **Tyr-**: *Tyrii*, *Tyriis*, *Tyriosque* kept with short *Ty-*, as in the published parts.
8. **697** *Cum venit*: present (short *e*), which the metre requires; the note's "present" stands.
9. **#28 ends at `fovet,`**: a comma, not a full stop; the build allows it and the cut is at internal punctuation. Kept (`t` is not mine to move).
10. **#49 / 753–754 speech marks**: stray mark kept in `t` and `l`, out of `i` (see above). Kept.
11. **711 bracket note**: kept except for the unverifiable manuscript claim.
12. **665 *Typhoia*** — the Greek form and the Typhoeus story kept.
13. **#18 `cum venit`** — see 8.
14. **Notes citing the Odyssey** (#20, #21, #31, #40, #49): kept at book level ("Odyssey 1", "Odyssey 7"); every line cite given from memory
    was removed or reduced to the book. **Aeneid-internal cites** (15–18, 343–352, 469–73, 267–288, 647–655, 648–649) were checked against
    the text of the poem and kept.
15. **Title fields**: "Cupido Ascanius. Convivium Didonis" kept.
16. **Echoes** listed above that were looked at and kept.
