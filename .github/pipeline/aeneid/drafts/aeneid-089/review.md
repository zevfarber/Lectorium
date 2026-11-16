# Review — aeneid-089 (Aeneid XI.725–835), adversarial reviewer

**Severity counts:**
- **Major: 3.** Scansion errors on 3 lines (768, 800, 813). The scanner flagged none of them, and two had a cost of 0.0.
- **Medium: 7.**
- **Low: 28.**
- **Refused or upheld without change: 22.**
- **Scan-fixes added: 4**, written directly into `scan-fixes.json` by `drafts/aeneid-089/add_scan_fixes.py`. The keys are 11.747, 11.768, 11.800 and 11.813. Three are corrections; 11.747 confirms the scanner and clears its COSTLY flag.

Nothing blocks the build. One item is for QUESTIONS.md: the rule-5b record of the 11.827 misprint (see "For the orchestrator").

## How the review was done

**Pass 1** went through all 50 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference that can be checked in the pinned source;
- the speech marks (732–740, 785–793, 823–827);
- the Latin Library variants and the `p` flag (725 only, which is right).

I hand-scanned all 111 lines by quantity and compared each one with the scanner's fit. The scanner was run in-process the way `build_aeneid.py` runs it (`scan_check.py`). The only sources were the Latin, the pinned source and my memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). I opened no translation.

**Pass 2:**
- I re-read every field that pass 1 changed.
- I re-read all `l` for words carried into the wrong line, which turned up 790–792 and 794–795.
- I re-read all `i` for distinctive remembered phrasing (M6, M7) and for tense drift across units (762–765).

**Script runs.** The drafter's file round-trips byte-identically through `aeneid_lib.jdump`. I restored it and ran `review_edits.py` once. It made 39 replacements, and each old string was asserted to occur exactly once. The guards confirm:
- `t`, `ln`, `p`, `v` and the top-level fields (`title`, `titleEn`, `part`, `about`) are unchanged;
- `l` has as many lines as `t`;
- no `i` contains a line break;
- notes run 43–119 words;
- `t`, `l` and `i` each have 3 “ and 3 ”.

**`review_check.py`** runs `make_units.py`'s checks against the edited file. It also runs a replica of the build's per-unit checks: tiling, `ln`, `p`, the five-line limit, ending at punctuation and coverage. It prints `BUILD REPLICA: OK`. It uses `EXEMPT = {827}` and `NOTE_MARKS = {827}`, because the two 827 notes now quote the print with its ” (house form of aeneid-041/042; the validator counts marks in `t`, `l` and `i` only).

**`scan_check.py`** applies `scan-fixes.json` with the 4 new entries. All 4 apply, the scanner report comes back empty, there are no metre failures, and every unit's `sc` lines up with its words.

**Files:**
- `units.json` was edited only by `review_edits.py`.
- `make_units.py` was not touched and still holds the drafter's strings. Build from `units.json` and do not re-run `make_units.py`.

## Scansion (major, one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 768 | 0.8, not flagged | *Chlōreus* (Χλωρεύς) has two long syllables, with *eu* as one diphthong: For-tĕ să \| cēr Cy̆-bĕ \| lō Chlō \| reūs ō \| līm-quĕ să \| cēr-dōs (15). The scanner read Chlŏ-rĕ-ŭs and counted 16. |
| 800 | **0.0**, not flagged | The syllable count was right but the quantities were wrong. *ācrīs* has both syllables long and *ŏcŭlōs* its first two short: con-ver \| tē-r(e) ă-nĭ \| mōs ā \| crīs ŏ-cŭ \| lōs-quĕ tŭ \| lē-re. The scanner had *ă-crĭs ō-cū-*. |
| 813 | **0.0**, not flagged | *subiēcit* has a consonantal *i* after the prefix (as 2.37 and 2.721): sub-iē \| cit pă-vĭ \| tant(em) ŭ-tĕ \| rō sil \| vās-quĕ pĕ \| tī-vit (15). The scanner read su-bi-e-cit and counted 16. |

**747 (COSTLY 2.0): confirmed.** The scanner's parse is right: ar-mă vĭ | rum-quĕ fĕ | rēns tūm | summ(a) ip | sī-ŭs ăb | has-ta, with *ipsīus* long in the middle. The entry exists only to clear the flag, as 088 did for 11.659.

**Checked and found right, so no entry:**
- 732 *dolitūr(i) Ō*: elision, the interjection standing. A hiatus parse also fits; the elision is the usual reading.
- 739 *sācra*: long by muta cum liquida.
- 761 *circuĭt*: three syllables.
- 767 *circuĭtum*: four syllables.
- 770 *ăēnīs*: three syllables.
- 779 *Trōĭă* (cost 1.6): three syllables.
- 807 *nec i(am) amplius*: *nec* is long before consonantal *i*.
- 826 *Trōiānōs*.
- 833 *dēiectā*.
- 834 *Teucrum* (cost 1.5): one *eu*.
- 835 *Evandrique*: the scanner's E–van–dri has the right count and quantities. The same form was accepted at 10.370 and 11.148, so no entry.

There is no hiatus anywhere in the part.

## Medium

- **M1 (unit 757, `n`).** *Tiburtum* was called "the old short ending '-um'", the label for *deum* and *Teucrum*. It is a third-declension genitive (*Tiburs, Tiburtis*) with *-um* for the usual *-ium*. Corrected.
- **M2 (unit 741, `n`).** "*concitat… concitus*, the same verb twice" is false. They are *concito* and the participle of *concieo*, two words of one family. Corrected.
- **M3 (unit 797, `n`).** "*Notos*, Greek accusative plural" is false. It is the ordinary Latin second-declension accusative of a Greek name. Corrected.
- **M4 (unit 833, `n`).** "*incurrunt… omnis copia*, a singular subject with a plural verb" is false: *incurrunt* has three subjects (*copia*, *duces*, *alae*). Only *densi*, masculine plural against feminine *copia*, agrees by sense. Corrected.
- **M5 (unit 772, `l`).** "from a Lycian, Gortynian, horn-bow" attached *Gortynia* to the bow; it goes with *spicula*. The line now reads "Gortynian shafts was shooting from a Lycian horn;".
- **M6 (unit 746, `i`).** "carrying the arms and the man" is the best-known English form of the poem's opening, and the distinctive echo the house I.1 rendering avoids. Now "carrying arms and a man", matching the house `l` "Arms and a man" and the note.
- **M7 (unit 828, set piece 831 = XII.952).** The drafter's `i` was "and life, crying out against its lot, passed with a groan into the world of shades." It had two faults:
  - "crying out" repeats *cum gemitu* and misreads *indignata* (resentment, not a cry);
  - "passed" loses *fugit*.

  Now:
  - `i`: "and life, bitter at its going, took flight with a groan down among the shades."
  - `l`: "and life with a groan takes flight, chafing, down under the shades." ("down under" replaces "beneath", for the motion and to match the house IV.660 `l` "under the shades".)
  - `n` adds that *fugit* is the present (short *u*, from the metre).

  The result has none of the known versions' marked words: "fled", "resentful", "indignant", "outraged", "indignity", "moan", "shades below". `new-renderings.md` has been updated to match.

## Low

**Elision lists** (L1–L4):
- 793: add *remeab(o) inglorius* (the note said "No elisions").
- 799: add *Erg(o) ut*.
- 829: add *paulat(im) exsolvit* (the note said "No elisions").
- 832: add *ver(o) immensus* (the note said "No elisions").

**Labels, facts and cross-references:**
- **L5 (725).** "an Ennian title" is unverified. The note now cites Virgil's own I.254, checked in the source.
- **L6 (735).** *adloquitur* was given as a case of the prefix *in-* kept unassimilated. Its prefix is *ad-*; the wording is fixed.
- **L7 (750).** V.438 was checked in the source, so "from memory" is dropped.
- **L8 (754).** *arrectis* is orthography only, so the Latin Library note was removed, per the conventions.
- **L9 (759).** "Virgil calls them so again and again" overstated it. The note now cites VIII.499 *O Maeoniae delecta iuventus*, checked in the source.
- **L10 (768).** The dative of *Cybelus* is now supported by Greenough's *Cybeli* at III.111, checked in the source. The note also gives the scansion pointer *Chlō-reus*, two long syllables.
- **L11 (773).** *torquebat* is now glossed "here of shooting".
- **L12 (800).** Scansion pointer *ā-crīs*.
- **L13 (827, both units).** Both misprint notes are now in the house form of aeneid-041/042 and quote the print with its mark ("The print has 'vale. ”Simul', a misprint for 'vale.” Simul', corrected here…"). The drafter's 828 note said "The print has 'vale. Simul'", which misquotes the print. The first unit also cites XI.98 *aeternumque vale* and says "at a funeral", where the drafter had "at a grave".

**`l`:**
- **L14 (734).** "A woman, scattered, drives you" made "scattered" read as the woman. Now "A woman the stragglers drives".
- **L15 (754).** "with raised bristles with scales" is now "bristles with raised scales".
- **L16 (779).** "in captured … in gold" doubled the *in*.
- **L17 (788).** "on the many coal" is now "on much live coal".
- **L18 (791–792).** "deeds" stood in 791 though *facta* is in 792. Re-divided.
- **L19 (792–793).** The order is now "if only this dread…", and "my father's" is now "my fathers'", to agree with `n` and `i`.
- **L20 (794–795).** "Phoebus" stood in the 795 line though *Phoebus* is in 794. Re-divided, with "he scattered".

**`i`:**
- **L21 (725).** The tense now agrees with the next unit, which is in the present.
- **L22 (729).** "the giving ranks" is now "the ranks giving way".
- **L23–L24 (762, 764).** Past tense changed to present, to match 759–761 and 766–767 on either side.
- **L25 (768).** "once its priest" (the mountain's) is now "once a priest". The note makes him Cybele's priest.
- **L26 (772).** "hurling arrows" is now "shooting arrows".
- **L27 (801).** "She alone" added a claim the Latin does not make (*ipsa*). Now "She herself … at all".
- **L28 (823).** "is ending me" is now "is making an end of me".

That is 28 low items: L13 counts as one, and L23–L24 as two.

## Refused or upheld (no change)

1. **827 `vale. ”Simul` as a rule-5b misprint: confirmed.** The speech certainly ends at *Iamque vale.*, and *Simul his dictis* is narrative, so the sense allows only one reading. It is the same pattern as 6.155, 6.197 and 5.400, and as XI.98 `aeternumque vale. ”Nec`, checked in the source. `t` keeps the print, with ” at the head of the *Simul* unit, and `l`/`i` close the speech after *vale.*.
2. **728 *incitat* / LL *inicit*.** Not noted, which is upheld: "stirs up anger" and "puts anger into" do not differ in sense.
3. **821 *fidam* / LL *fida*** and **830 *relinquunt* / LL *relinquens*.** Both are noted, which is upheld: each changes the construction and the sense. 770 *aënis* and 779 *Troïa* are orthography and are rightly not noted.
4. **738 *exspectate* as a scornful imperative.** Upheld for Greenough's text.
5. **760 *iaculo* taken with *circuit*,** with the alternative mentioned. Upheld.
6. **768 *Cybelo* as the dative of the mountain *Cybelus*.** Upheld, and strengthened by III.111 (L10).
7. **822 *quicum partiri curas*, "erat understood".** Upheld; it is the usual explanation of the compressed phrase.
8. **747 *ipsius* = Venulus's spear.** Upheld (Servius).
9. **Venulus "from Tibur",** in the note of 741 and in `about`. Upheld as a fair inference from *Tiburtum ex agmine* (757).
10. **732: elision *dolitur(i) O* rather than hiatus.** Upheld.
11. **745–746 `l` "turned" and `i` "turn".** Upheld: the note explains the tense shift, and `i` keeps the narrative present.
12. **774 *cassida*, "Greek-looking first-declension ending".** Upheld.
13. **832 "Ennius has similar shouts reaching the sky".** Upheld (Ennius's *tollitur in caelum clamor*, cited by Macrobius). It is left unspecific.
14. **727 "joined Aeneas in Book VIII and sailed with him in Book X".** Upheld: VIII.603–607 and X.153–156, both checked.
15. **Homeric and other references kept "from memory".** I believe all of them are right:
    - Iliad X.68–69, IV/V, XII.200–207, XVI.249–252, XV.586–590 and XXI.70;
    - Herodotus I.94;
    - Pliny on the Hirpi Sorani.
16. **Cross-references checked in the source and right:** VIII.9, XI.242–295, XI.591–592, IX.359–374 (the helmet at 373–374), 649 and 655–656.
17. **`p`.** Only 725 has it, which is right.
18. **Scanner fits of 779, 834 and 835 (costs 1.6, 1.5, 1.0).** Right, so no entries.
19. **`about`.** Not touched; it is accurate.
20. **Unit 746, the *Arma virumque* allusion in `n`.** Upheld; only the `i` wording changed (M6).
21. **Unit 785 `i`, "through whose flames".** Upheld: the fire is the god's.
22. **Unit 778 `i`, "hang Trojan armour in a temple" for *templis praefigeret*.** Upheld as idiomatic.

## For the orchestrator

- **`scan-fixes.json`** now holds 4 new keys: 11.747, 11.768, 11.800 and 11.813, appended after 11.691. Nothing else in the file changed.
- **QUESTIONS.md (rule-5b record, as items 30, 35 and 36).** 11.827 prints `Iamque vale. ”Simul his dictis` and should read `vale.” Simul`. The closing mark stands at the head of the unit `”Simul his dictis linquebat habenas, / ad terram non sponte fluens.` in `t`, and `l`/`i` close Camilla's speech after `vale.`. The same pattern stands at XI.98 `aeternumque vale. ”Nec`, already published. The repeated pattern suggests that the Perseus encoding sets these closing marks after the space.
- **New house rendering XI.831 (= XII.952).** The final row is in `new-renderings.md`. Copy it to `conventions.md` when publishing, and mark the set piece *vitaque cum gemitu fugit indignata sub umbras* as decided in the list of set pieces still ahead.
