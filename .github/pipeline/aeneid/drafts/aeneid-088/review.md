# Review — aeneid-088 (Aeneid XI.648–724), adversarial reviewer

**Severity counts:**
- **Major: 7.** These are scansion errors on 7 lines. The scanner left 6 of them unflagged, and 3 of those had a cost of 0.0.
- **Medium: 4.**
- **Low: 16.**
- **Refused or upheld without change: 17.**
- **Scan-fixes added: 8**, in `drafts/aeneid-088/scan-fixes-088.json` (not in `scan-fixes.json`; the orchestrator merges it). The keys are 11.657, 11.659, 11.662, 11.665, 11.678, 11.680, 11.685 and 11.691. Seven are corrections; 11.659 confirms the scanner and clears its COSTLY flag.

Nothing blocks the build. Nothing needs to go to QUESTIONS.md.

## How the review was done

**Pass 1** went through all 29 units word by word. I checked:
- `l`, `i` and `n` against the Latin;
- every grammatical label and every elision list;
- every cross-reference that can be checked in the pinned source;
- the speech marks (686–689, 705–708, 715–717);
- the Latin Library variants and the `p` flag (648 only, which is right).

I hand-scanned every line of the part, not only the lines with Greek names. The only sources were the Latin, the pinned source and my memory of the public-domain references (Lewis & Short, Allen & Greenough, Conington, Servius). I opened no translation.

**Pass 2:**
- I re-read every field that pass 1 changed (16 fields).
- I re-read all `l` for misattached words, which turned up M2.
- I re-read all `i` for distinctive remembered phrasing. I found none that needed recasting; the renderings are plain and literal throughout.

**Script runs.** I restored the drafter's file, which round-trips byte-identically through `aeneid_lib.jdump`, and ran `review_edits.py` once. It made 20 replacements, and each old string was asserted to occur exactly once. The script's guards confirm:
- `t`, `ln`, `p`, `v` and the top-level fields are unchanged;
- `l` has as many lines as `t`;
- no `i` contains a line break;
- notes run 66–132 words, within the limit of 139;
- `t`, `l` and `i` each have 3 “ and 3 ”.

**`review_check.py`** runs `make_units.py`'s checks against the edited file. It also contains a replica of `build_aeneid.py`'s per-unit checks: tiling, `ln`, `p`, the five-line limit, ending at punctuation and coverage of 648–724. Everything passes and the replica prints `BUILD REPLICA: OK`. There is no EXEMPT and no NOSTOP.

**`scan_check.py`** applies `scan-fixes.json` and then `scan-fixes-088.json`, as the build will once the files are merged. All 8 entries apply and the scanner report comes back empty. No metre failures remain and every unit's `sc` lines up with its words.

**Files:**
- `units.json` was edited only by `review_edits.py`.
- `make_units.py` was not touched and still holds the drafter's strings. Build from `units.json` and do not re-run `make_units.py`.
- `add_scan_fixes.py` writes `scan-fixes-088.json`. Each entry is asserted against:
  - the build's word-match rule;
  - the validator's metre rule;
  - the syllable count stated in its `why`;
  - for corrections, that the result differs from the scanner's own output;
  - for 659, that it is identical to the scanner's own output.

  It also asserts that no key is already in `scan-fixes.json`.

## Scansion (major, one per line)

The scanner flagged only 659, and that line was right. Six of the seven lines it actually got wrong were not flagged, and the seventh it flagged as a spondaic fifth foot:

| line | scanner (cost) | right reading |
|---|---|---|
| 657 | 1.5, not flagged | *dīa* has two syllables (*dī-ă*) and *decus* is long by position: Ī-tă-lĭ \| dēs quās \| ip-să dĕ \| cūs sĭ-bĭ \| dī-ă Că \| mil-la. The scanner made *dia* one syllable and lengthened both syllables of *sibi*. |
| 659 | COSTLY 4.0 | **Confirmed.** *Thrēĭcĭae* has four syllables (Greenough prints *Threïcius* at VI.645), followed by a spondaic fifth foot on *Thermōdōn*: quā-lēs \| Thrē-ĭ-cĭ \| ae cum \| flū-mĭ-nă \| Thēr-mō \| dōn-tis. The entry exists only to clear the flag. |
| 662 | 1.5, not flagged | *Penthesilēa* has five syllables (as *Penthesilea furens*, I.491) and *rĕfert* has a short first syllable: Pen-thĕ-sĭ \| lē-ă rĕ \| fert mag \| nōqu(e) ŭ-lŭ \| lān-tĕ tŭ \| mul-tu. The scanner ran *-lea* together and lengthened *re-*. |
| 665 | 1.5, not flagged | *dēĭcis* has three syllables, and *-cĭs* is short before *Aut*. The line is holodactylic: dē-ĭ-cĭs \| aut quŏt hŭ \| mī mŏ-rĭ \| en-tĭ-ă \| cor-pŏ-ră \| fun-dis. |
| 678 | **0.0**, not flagged | *Ĭāpyge* has four syllables with a vowel I (Ἰᾶπυξ; *Iapyge* at VIII.710 and *Iapyx* at XII.391 were checked in the source), so *vēnātŏr* keeps a short *-or*: ig-nō \| tīs ĕt ĕ \| quō vē \| nā-tŏr Ĭ \| ā-pў-gĕ \| fer-tur. The scanner read *Ja-*. |
| 680 | **0.0**, not flagged | The syllable count was right but the quantities were wrong: pug-nā \| tōr(i) ŏ-pĕ \| rīt că-pŭt \| in-gens \| ō-rĭs hĭ \| ā-tus. The scanner made *-nā-tō-* short and *ŏpĕ-* long. |
| 685 | 1.8, not flagged | *trāĭcit* has three syllables, and *-cĭt* is short before *et*: trā-ĭ-cĭt \| ēt sŭ-pĕr \| haec ĭ-nĭ \| mī-cō \| pec-tŏ-rĕ \| fā-tur. |
| 691 | **0.0**, not flagged | The syllable count was right but the quantities were wrong: cor-pŏ-ră \| sēd Bū \| tēn ā \| ver-sum \| cus-pĭ-dĕ \| fī-xit. The scanner made *-pō-rā* long and *-tĕn* short. |

**Checked and found right, so no entry:**
- 652 *aureus*: three syllables, no synizesis.
- 656 *Tarpēia*: the i is consonantal.
- 666 *Eunaeum*: *Eu-* is one syllable; *cūius*.
- 667 *abiete*: *āb-jĕ-tĕ*, the i consonantal and the first syllable long by position, as the drafter said.
- 675: *Tērĕăqu(e) Harpălўcumqu(e) et Dēmŏphŏōntă Chrŏminque*. *Demophoonta* has five syllables, with no synizesis.
- 677 *Ornytus*, 673 *Amastrum*, 674 *Hippotaden*, 670 *Lirim Pagasumque*.
- 687 *Advēnit*, the perfect with a long *ē*.
- 688 *redarguerit* and *patrum*, the latter long by muta cum liquida.
- 690 *Būtēn*, *Teucrum*.
- 700 *Appenninicolae*, *Auni*.
- 711 *interrită*.
- 715 *Ligus*.

There is no hiatus anywhere in the part.

To help the reader, short scansion pointers were added to the notes for 657, 659, 662, 665, 678 and 685; they are listed among the low items below.

## Medium

- **M1 (unit 699, `n`).** The note calls *Ligurum* an "old genitive plural". It is the ordinary third-declension genitive of *Ligus, Liguris*, not the old *-um* of *Teucrum*. Corrected, with a pointer to 690.
- **M2 (unit 699, `l`).** "the warrior son, Aunus," makes *Auni* an apposition. It is genitive, so the line now reads "the warrior son, of Aunus,".
- **M3 (unit 673, `n`).** "The four names are Greek accusatives" is false, because *Harpalycum* is Latin. Now: "Three of the four names have Greek accusatives ('Harpalycum' is Latin)".
- **M4 (unit 682, `n`).** "Homer marks Ajax and Agamemnon out the same way (Iliad III.193 and 227)" is wrong. III.193 is Priam saying Odysseus is shorter than Agamemnon by a head, which is not this motif. The real model is inside Virgil himself: Turnus at VII.784, *vertitur arma tenens et toto vertice supra est*, which is the same half-line plus *vertitur*, checked in the source. The note now cites VII.784, and Ajax alone at Iliad III.227 (still marked "from memory").

## Low

**Labels:**
- **L1 (unit 659).** *Thermodontis* was called a "Greek genitive". It is the Latin genitive of a Greek name (the Greek is *-ontos*). The note now says so and adds the spondaic fifth foot.
- **L2 (unit 705).** "'fido' takes the dative" now reads "the dative or the ablative; 'forti… equo' may be either".

**Elision lists** (L3–L7):
- 684 add *nequ(e) enim*.
- 692 add *galeamqu(e) inter*.
- 701 add *Ligur(um) extremus*.
- 702 add *Isqu(e) ubi*.
- 719 add *frenisqu(e) adversa*.

**Scansion pointers in `n`** (L8–L13):
- 657 *dia*, two syllables.
- 662 *Penthesilea*, five syllables (I.491).
- 665 *deicis*, three syllables; the line is all dactyls.
- 678 *Iapyge*, four syllables, with VIII.710.
- 685 *traicit*, three syllables.
- 659 is covered by L1.

**Cross-references checked in the source, so "from memory" is dropped** (L14):
- X.830 *Aeneae magni dextra cadis*;
- VII.808–811, where 808 is *Illa vel intactae segetis per summa volaret*.

I also confirmed these, which carried no "from memory" tag:
- XI.418 *humum semel ore momordit*;
- XI.489 *tempora nudus*;
- I.490–493, Penthesilea on Dido's temple;
- XI.532–596, Diana and Opis;
- *siqua* (e.g. XI.128) and *nequid* (XI.417) earlier in the book.

**`i`:**
- **L15 (unit 659).** The *seu… seu* was lost. The line now reads "whether around Hippolyta or when Penthesilea…".
- **L16 (unit 706).** "Send away the horse you run on" is ambiguous English for *Dimitte fugam*. It now reads "Give up your means of escape".

## Refused or upheld (no change)

1. **671 *suffosso* / LL *suffuso*.** The handling is right. The variant changes the sense, so a note is warranted, and "sprawled under him" is a fair gloss of *suffuso* (Servius glosses it as *prostrato*). Greenough's reading is kept.
2. **688 *redarguerit* / LL *redargueret*.** Mentioning it is acceptable: the brief asked for both variants to be handled, and the note says plainly that it is a shade of tense. The perfect-subjunctive label is right for Greenough's text.
3. **717 closing mark after `Auno,`.** Upheld. The speech is 715–717, and *haec fatur virgo* lies outside it. `l` and `i` match.
4. **The speech marks** on 686/688 and 705/706 are right in `t`, `l` and `i`, one opening and one closing mark each.
5. **711 *interrita* as nominative.** Upheld, because a short final *-a* is required by the fifth-foot dactyl.
6. ***pugnatori* taken with *cui*, with *iuvenco* mentioned.** Upheld.
7. ***agrestis*, both constructions given.** Upheld.
8. **702 *pugnae*, dative of separation.** Upheld.
9. **662 *magno… ululante tumultu*, "ablative absolute".** Upheld. It is a participle with its noun; "attendant circumstance" would also do.
10. **660 *pulsant*, "with their horses' hooves".** Upheld as a reasonable reading.
11. **650 *denset* from *denseo*.** Right: *denso* would give *densat*.
12. **690 anacoluthon.** The note's description is upheld.
13. **Homeric and Georgic references kept "from memory".** These cannot be checked in the source, but I believe them right:
    - Iliad I.46 (the arrows clattering on Apollo's shoulder);
    - Iliad XVI.692–693 (whom first, whom last, Patroclus);
    - Iliad X.334 (Dolon's wolf-skin);
    - Odyssey XV.526 (the hawk as Apollo's swift messenger);
    - Iliad XXII.139–142 (Achilles as hawk, Hector as dove);
    - Georgics III.31 (the Parthian shot);
    - Servius citing Cato on the Ligurians.
14. **696 `i`, "begged and prayed and pleaded".** This uses three verbs for *oranti et multa precanti*. It is slightly expansive but true to *multa*, so I left it.
15. **721 `i`, "swooping".** This is an addition implied by *ab alto*. It is not a distinctive echo, so I left it.
16. **686 `i`, "Did you think, Etruscan, that you were out in the woods chasing game?"** The wording follows from the Latin. I recall no distinctive version that it copies.
17. **`about`.** It is a top-level field and was not touched. I checked it and it is accurate.

## For the orchestrator

- **Merge `drafts/aeneid-088/scan-fixes-088.json` into `scan-fixes.json`.** It holds 8 keys (11.657 to 11.691, in line order) and none of them is already present.
- **Nothing for QUESTIONS.md.**
- **Drafter's line reference confirmed.** `drafter-notes.md` dates Tarchon's rebuke to XI.732 ff., and that is right: the speech opens at 732 with *Quis metus*.
