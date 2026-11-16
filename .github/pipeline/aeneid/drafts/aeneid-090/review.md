# Review — aeneid-090 (Aeneid XI.836–915), adversarial reviewer

**Severity counts:**
- **Major: 7.** Scansion errors on 7 lines (842, 858, 872, 890, 904, 908, 910). The scanner flagged only 904; 842 and 872 had a cost of 0.0.
- **Medium: 4.**
- **Low: 22** (21 text edits and 1 syllable-division scan-fix, 870).
- **Refused or upheld without change: 22.**
- **Scan-fixes added: 8**, written directly into `scan-fixes.json` by `drafts/aeneid-090/add_scan_fixes.py`. The keys are 11.842, 11.858, 11.870, 11.872, 11.890, 11.904, 11.908 and 11.910. All eight are corrections. 904 was flagged COSTLY, but the scanner's parse was wrong, so its entry corrects the line rather than confirming it. The entries use the existing `{"sc": [...], "why": "..."}` format: the file's key is `why`, not `reason`.

Nothing blocks the build. COSTLY is only printed in the build's report and never fails it, and the 904 flag is cleared anyway. One item is for QUESTIONS.md: the rule-5b record of the 11.849 misprint (see "For the orchestrator").

## How the review was done

**Pass 1** went through all 32 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference that can be checked in the pinned source;
- the speech marks (841–849 and 855–857);
- the Latin Library variants and the `p` flags (836, 868 and 896, all right).

I hand-scanned all 80 lines by quantity and compared each one with the scanner's fit (`scan_check.py`, adapted from 089's, which runs the scanner the way `build_aeneid.py` does). The only sources were the Latin, the pinned source and my memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). I opened no translation.

**Pass 2:**
- I re-read every field that pass 1 changed.
- I re-read all `l` for words carried into the wrong line, which turned up 852 *se* and 906–907 *feruntur*.
- I re-read all `i` for subject/object reversals and for distinctive remembered phrasing.

**Script runs.** The drafter's file round-trips byte-identically through `aeneid_lib.jdump`. `review_edits.py` was run once. It made 27 replacements, and each old string was asserted to occur exactly once. The guards confirm:
- `t`, `ln`, `p`, `v` and the top-level fields (`title`, `titleEn`, `part`, `about`) are unchanged;
- `l` has as many lines as `t`;
- no `i` contains a line break;
- notes run 53–114 words;
- `t`, `l` and `i` each have 2 “ and 2 ”.

**`review_check.py`** is 089's, with `EXEMPT = NOTE_MARKS = {848, 849}`. It prints no faults and `BUILD REPLICA: OK`.

**`scan_check.py`** applies all 8 new entries. The scanner report comes back empty, there are no metre failures, and every unit's `sc` lines up with its words.

**Files:**
- `units.json` was edited only by `review_edits.py`.
- `make_units.py` was not touched and still holds the drafter's strings. Build from `units.json` and do not re-run `make_units.py`.

## Scansion (major, one per line; plus one low)

| line | scanner (cost) | right reading |
|---|---|---|
| 842 | **0.0**, not flagged | *Teucros* has one *eu*, and *cōnāta* has its first two syllables long: sup-plĭ-cĭ \| um Teu \| crōs cō \| nā-tă lă \| ces-sĕ-rĕ \| bel-lo (15). The scanner read Te-u-cros with short *co-na-* and counted 16. |
| 858 | 1.5, not flagged | *Threissa* has three syllables (Thrē-is-sa, as 1.316), and *vŏlucrem* has a short first syllable: dī-xĭt ĕt \| au-rā \| tā vŏ-lŭ \| crem Thrē \| is-să să \| git-tam (15). The scanner read *Threis-sa* as two syllables and lengthened *vo-* and *-lu-*. |
| 872 | **0.0**, not flagged | *Teucros* has one *eu*: Nec quis \| qu(am) ins-tan \| tīs Teu \| crōs lē \| tum-quĕ fĕ \| ren-tis (13). The scanner made a dactyl *tis Te-u*. |
| 890 | 1.3, not flagged | *arietat* has three syllables with consonantal *i* (as *ariete* at 7.175). *dūros* has a long *u*. *obice* is ob-ĭ-cĕ, as 2.444 and 4.549. The line: ar-yĕ-tăt \| in por \| tās et \| dū-rōs \| ob-ĭ-cĕ \| pos-tis (14). The scanner had ā-rĭ-ĕ-tat and *dŭros*. |
| 904 | **COSTLY 2.0** | Not confirmed, but wrong. *Aenēās* has three long syllables: cum pă-tĕr \| Ae-nē \| ās sal \| tūs in \| gres-sŭs ă \| per-tos (14). The scanner split *A-e* and shortened *-ne-*. |
| 908 | 1.2, not flagged | The same *Ae-* error: ac sĭ-mŭl \| Ae-nē \| ās fū \| man-tīs \| pul-vĕ-rĕ \| cam-pos (14). |
| 910 | 1.5, not flagged | The same *Ae-* error, here in the accusative *Aenēān*: et sae \| v(um) Ae-nē \| ān ad \| gnō-vit \| Tur-nŭs ĭn \| ar-mis (13). |

**870 (low): syllable division only.** The scanner wrote *di-siec-ti*. The quantities are the scanner's, but the division is now *dis-iec-ti*, following the precedent of 2.608 and 1.128. *-nī-* of *manipli* is long by position before *pl*, which is right.

**Checked and found right, so no entry:**
- 841 *Heu*;
- 875 *quă-drŭ-pĕ | dum-quĕ pŭ | trem*, where mute and liquid lengthen the first syllable and not *pŭ*;
- 845 *indĕcŏrem*;
- 857 *Tūn(e)*;
- 866 *oblīt(i) ignōto*;
- 893 *trepidae iaciunt*, with no elision before consonantal *i*;
- 901 *Iovis*;
- 905 *exsuperatque iugum*;
- 914 *tinguat*, two syllables;
- 860, 861, 891, 903, 906, 907 and 909, at costs of 0.3 to 0.6.

There is no hiatus in the part.

## Medium

- **M1 (848 and 849, `n`): the misprint notes.** The cut matches 089's handling of 827, and that is upheld:
  - `t` keeps `merita.` and the next unit's `”Fuit`;
  - `l` and `i` close Opis's speech after *merita.*;
  - `EXEMPT = {848, 849}`.

  The fault was the notes. They did not follow rule 5b's form as 089 applied it, where the note opens "The print has X, a misprint for Y, corrected here." Both notes now open "The print has 'merita. ”Fuit', a misprint for 'merita.” Fuit', corrected here", which is word for word the 827 form. `NOTE_MARKS = {848, 849}`, as 089 had `{827}`.
- **M2 (910, `l`).** "so savage Aeneas recognised Turnus in arms" keeps the Latin order, but the English then makes Aeneas the one who recognises. It now reads "so Turnus recognised savage Aeneas in arms".
- **M3 (903–905, `n`).** The note took *ingressus* as finite, with *est* understood. That contradicted the unit's own `l` ("both overcomes… and…"), which reads *exsuperatque… silvaque* as the double *-que*. The note now gives the participle with the double *-que* first and mentions the *ingressus est* reading as an alternative.
- **M4 (852, `l`).** "Here the goddess herself" turned the reflexive object of *sistit* into an intensive. It now reads "Here the goddess first… / sets herself, and Arruns…". The pronoun moves to the second line for sense.

## Low

**Elision lists** (L1–L6). Each item below was missing from its unit's list, apart from L3, which was wrong:
- 863: *stridor(em) aurasque*;
- 866: *oblit(i) ignoto*;
- 885: *accipe(re)* was corrected to *acciper(e) orantis*;
- 887: *ant(e) oculos*;
- 911: *flatusqu(e) audivit*;
- 915: *ant(e) urbem*.

**Labels, facts and quotations** (L7–L14):
- **L7 (848).** The quotation of XI.591 now reads *volnere*, as Greenough prints it (checked in the source); it had *vulnere*.
- **L8 (838) and L9 (886).** *-entum* for *-entium* was called "Greenough's old" genitive. It is the poets' form, not a spelling of the edition.
- **L10 (844).** *umero* was called "Greenough's spelling of *humero*". *umerus* is the better spelling (L&S), so the note now says it is "also spelled *humero*".
- **L11 (847).** *famam… inultae*: the genitive agrees with an understood *tui*, not with the nominative "you" of *patieris*.
- **L12 (855) and L13 (875).** The Latin Library spelling differences *derige* and *quadripedumque* were removed, as the conventions require and as 089 did (its L8).
- **L14 (868).** "'fugit' repeated three times" is now *fugit… fugiunt… fugit*.

**Scansion pointer** (L15): the 858 note now says *Threissa* has three syllables.

**`l`:**
- **L16 (838).** *medio* goes with *clamore*. The line now reads "in the midst of the raging young men's shouting".
- **L17 (906–907).** "are borne" (*feruntur*) stood in the 907 line. Re-divided.

**`i`:**
- **L18 (845).** "at the very end of death" is now "at the very point of death".
- **L19 (893–894).** "they make do for iron" is now "they make wood do the work of iron".
- **L20 (910).** "Aeneas in his savage armour" moved *saevum* onto the armour. It now reads "Aeneas, savage in his armour," as the note glosses it.
- **L21 (915).** "entrench themselves by the walls" now reads "the walls are ringed with ramparts", which agrees with *moenia vallant* and the note.
- **L22 (875 = VIII.596).** "shake the crumbling plain" is now "batter the crumbling plain". This is a precaution against a stock rendering of the famous line.

## Refused or upheld (no change)

1. **The 848/849 cut and its EXEMPT handling.** Upheld as consistent with 089's 827 handling. Only the note form changed (M1). The sense allows only one reading: *Fuit ingens…* is narrative. The same pattern appears at 11.827, 11.98 and 10.451.
2. **857 cross-reference X.829–830.** Verified in the source: *Hoc tamen infelix miseram solabere mortem: / Aeneae magni dextra cadis.* Right.
3. **Other cross-references checked in the source, all right:**
   - XI.532–596, 567–584, 590, 590–594, 591–592 (wording apart from L7), 726 *altus*, 801–802, 806, 832–833, 511–531 and 820–827;
   - I.316 *Threissa*, VIII.596, II.487–488;
   - XII.661 *acer Atinas*, for "named again in Book XII".
4. **Variants noted for sense: upheld.** These are 839 *mulcatam*, 844 *pharetras* ("hardly changes"), 854 *fulgentem armis* and 901 *poscunt*. 887 *lacrumantum*, 910 *adgnovit* and 914 *tinguat* are glossed as Greenough's spellings, which the conventions allow once.
5. **845 *indecorem* from *indecoris*.** Upheld.
6. **892 *ut videre Camillam* as "as they had seen Camilla do".** Upheld as the drafter's reading. The alternative ("when they saw Camilla fallen") exists, but it is not needed.
7. **883 *Pars claudere portas* as a historic infinitive.** Upheld.
8. **859 *cornu… tetendit*, with the case left open.** Upheld.
9. **893–894 *robore duro* as a separate ablative of means**, rather than "stakes of hard oak". Upheld; both readings are defensible.
10. **915 *moenia vallant*, "both armies dig in".** Upheld; only `i` was aligned (L21).
11. **870 *manipli* as a Roman anachronism.** Upheld.
12. **863 *una* as an adverb.** Upheld.
13. **855: one opening mark around *inquit*.** Upheld, because the mark counts must equal those in `t`.
14. **855–857 split into two units.** Upheld.
15. **836: Opis in Callimachus and as a name of Artemis, "from memory".** Upheld.
16. **Homeric references "from memory": upheld.** They are Iliad IV.123, XI.369–372, XXI (Priam's gates), VII.282 and VIII.485–486.
17. **`p` flags** at 836, 868 and 896: right.
18. **858–862 `i` "almost met".** Upheld as an interpretation of *donec… coirent*.
19. **The scanner's fits of 875 and 870's quantities**, and the low-cost lines listed above: right.
20. **901 *saeva Iovis* and 893 *trepidae iaciunt*: no elision**, rightly not listed.
21. **`about`.** Not touched; it is accurate.
22. **841 `i` "too cruel, far too cruel".** Built from the Latin; there is no distinctive echo.

## For the orchestrator

- **`scan-fixes.json`** now holds 8 new keys: 11.842, 11.858, 11.870, 11.872, 11.890, 11.904, 11.908 and 11.910, appended after 11.813. Nothing else in the file changed; the git diff shows additions only.
- **QUESTIONS.md (rule-5b record, as item 81 did for 11.827).** 11.849 prints `morte luet merita. ”Fuit ingens` and should read `merita.” Fuit`.
  - The closing mark stands at the head of the unit `”Fuit ingens monte sub alto / … tectum:` in `t`.
  - `l` and `i` close Opis's speech after *merita.*.
  - The notes of 848 and 849 open with the print's reading.
  - This is the same Perseus pattern as 11.827, 11.98 and 10.451.
- **No new house renderings, no set pieces, no advisory.**
