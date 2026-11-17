# Review — aeneid-097 (Aeneid XII.650–745), adversarial reviewer

**Severity counts:**
- **Major: 11.** All 11 are wrong scansions, and the scanner flagged none of them. They are 653, 654, 678, 680, 689, 697, 709, 711, 723, 730 and 744. Four had a cost of 0.0 (689, 711, 730 and 744). Three were false fits with the right syllable count (653, 680 and 730).
- **Medium: 3** findings (16 edits).
  - Four elisions were missing (682, 719, 722, 725).
  - One `l` rendered a genitive as a goal (690 *urbis ad muros*).
  - Eleven `i` renderings were rephrased as a precaution against remembered modern versions.
- **Low: 11** findings (23 edits plus 4 scan-fixes).
- **Refused or upheld without change: 22.**
- **Scan-fixes added: 15.** They were written straight into `scan-fixes.json` by `drafts/aeneid-097/add_scan_fixes.py --write` and appended after 12.648 in line order. The keys are 12.653, 12.654, 12.678, 12.680, 12.686, 12.687, 12.689, 12.697, 12.704, 12.709, 12.711, 12.723, 12.729, 12.730 and 12.744.
  - 11 fix wrong scans (Major).
  - 3 change only the syllable division (Low: 686, 687, 729).
  - 1 is a confirmation entered to clear the packet's COSTLY flag (Low: 704, as 9.811).
  - The git diff of `scan-fixes.json` is 174 insertions and 0 deletions.

Nothing blocks the build. The `scan_check.py` replica gives sc for 49 of 49 units, with no report left, no metre failures and no line-up failures. `build_aeneid.py` itself was not run.

## How the review was done

**Pass 1** went through all 49 units word by word:
- `l`, `i` and `n` against the Latin, every grammatical label, and every elision list line by line. Each line was also hand-scanned, which is how the missing elisions showed up.
- The speech marks. There are three speeches: Saces 653–664, Turnus 676–680 and Turnus 693–695. `t`, `l` and `i` are each 3/3, and they match unit by unit.
- The `p` flags at 650 and 697. Both are right.
- The rule-5b handling of 723 *alitur*, 727 *letum;* and 743 *orbes*.
- Cross-references checked in `source/aeneid-greenough.json`:
  - 12.573 (*ferte faces*);
  - 12.595–603 (Amata);
  - 7.691 (Messapus, *equum domitor, Neptunia proles*);
  - 11.869 (*fugit acer Atinas*);
  - 10.870–872 (the same lines on Mezentius, with 872 bracketed);
  - 12.632 (Juturna recognised);
  - 12.90–91 (Daunus's sword);
  - 12.468–470 (Metiscus thrown from the chariot);
  - 5.759–761 (Venus at Eryx, Anchises' tomb).

  All are right.

All 96 lines were hand-scanned by quantity and compared with the scanner's fit. `scan_check.py`, `review_check.py` and `add_scan_fixes.py` are 096's, pointed at 097. Precedent entries:
- *Aeneas* 12.311 and *Teucros* 12.506;
- *Troes* 1.524, 9.689 and 9.811;
- *abrupto* 12.451, *sublatis* 12.26 and *Etruria* (Et-ru) 12.232;
- *ariete* 7.175.

Sources: the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2** re-read every changed field (34 fields) against `t`, checked each `l` for words on the wrong line, and checked each `i` for drift, tense and remembered phrasing. Nothing further was found.

**Script runs.**
- The drafter's `units.json` round-trips byte-identically through `aeneid_lib.jdump`. A copy was kept at `/tmp/claude-0/-home-user-Lectorium/b0556cfd-434d-57f0-9c80-564604a6c0cc/scratchpad/units.orig.json` before editing, and a copy of `scan-fixes.json` beside it at `scan-fixes.orig.json`.
- `review_edits.py` runs once from the drafter's file and makes 39 edits to 34 fields. Each old string is asserted to occur exactly once. Its guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` are unchanged;
  - `l` line counts equal those of `t`;
  - no `i` contains a line break;
  - every note is 15–139 words.
- `review_check.py` prints no faults:
  - marks are t 3/3, l 3/3, i 3/3;
  - notes run 33–107 words;
  - 49 units, 96 lines;
  - `BUILD REPLICA: OK`;
  - `t/ln/p/v vs drafter: OK`.
- `make_units.py` was not rerun and still holds the drafter's strings. Build from `units.json`, and do not rerun `make_units.py`.

## Scansion

### Major (one per line; none flagged by the scanner)

| line | scanner (cost) | right reading |
|---|---|---|
| 653 | 0.6 | *sūprēma*: su- is long by position before the mute and liquid, divided sup-rē-ma (as 12.232). *să-lūs*: Tūrn(e) īn \| tē sūp \| rē-mă să \| lūs mĭ-sĕ \| rē-rĕ tŭ \| ō-rum (15). The scanner made su-/pre- short and ma-/sa- long, a false fit with the same count. |
| 654 | 1.2 | *Aeneas*: Fūl-mĭ-năt \| Ae-nē \| ās ār \| mīs sūm \| mās-quĕ mĭ \| nā-tur (14). The scanner split Ae-. |
| 678 | 1.2 | *Aeneae*, with *manum* elided into it: Stāt cōn \| fēr-rĕ mă \| n(um) Ae-nē \| ae stāt \| quīd-quĭd ă \| cērb(i) ēst (14). The scanner split Ae-. |
| 680 | 0.6 | *ōrō* long-long, *sĭnĕ* short-short, *mē* long: ām-plĭ-ŭs \| hūnc ō \| rō sĭ-nĕ \| mē fŭ-rĕ \| r(e) ān-tĕ fŭ \| rō-rem (16). This is a false fit with the same count. |
| 689 | **0.0** | *disiecta* is dis-iec-ta, with a consonantal i after the prefix: īn-vōl \| vēns sē \| cūm dīs \| iēc-tă pĕr \| āg-mĭ-nă \| Tūr-nus (14). The scanner gave 15. |
| 697 | 1.2 | *Aeneas*: Āt pă-tĕr \| Ae-nē \| ās aū \| dī-tō \| nō-mĭ-nĕ \| Tūr-ni (14). The scanner split Ae-. |
| 709 | 0.6 | *coiisse* has four syllables, cŏ-ĭ-īs-se: īn-tēr \| sē cŏ-ĭ \| īs-sĕ vĭ \| rōs ēt \| cēr-nĕ-rĕ \| fēr-ro (15). The scanner read co-iis-se (14). |
| 711 | **0.0** | *coniectis* is con-iec-tis, with a consonantal i after the prefix: prō-cūr \| sū ră-pĭ \| dō cōn \| iēc-tīs \| ē-mĭ-nŭs \| hās-tis (14). The scanner gave 15. |
| 723 | 1.5 | Scanned as printed. *alitur* and *aliter* have the same quantities, and -tur/-ter is long before Tr- either way. *Aeneas*: nōn ă-lĭ \| tūr Trōs \| Ae-nē \| ās ēt \| Daū-nĭ-ŭs \| hē-rōs (14). The scanner split Ae-. |
| 730 | **0.0** | *Trōēs* has two syllables, and -es is long before tr-. *trĕpĭdi*: ēt fĕ-rĭt \| ēx-clā \| mānt Trō \| ēs trĕ-pĭ \| dī-quĕ Lă \| tī-ni (15). The scanner made Troes one syllable and tre-pi long-long (14). |
| 744 | **0.0** | *Teucri* is Teu-crī. *ĕnīm* has -nim long before d-, and *densā* is an ablative: ūn-dĭ-qu(e) ĕ \| nīm dēn \| sā Teū \| cr(i) īn-clū \| sē-rĕ cŏ \| rō-na (14). The scanner split Te-u (15). |

### Low (scan-fixes)

- **686** *sublapsa* is sub-lap-sa, **687** *abruptum* is ab-rup-tum and **729** *sublatum* is sub-la-tum. Each has the same feet and quantities as the scanner's fit; only the division changes. The scanner's su-/a- would put an open long mark on a short vowel, which the audio would voice long. This follows 12.451 *abrupto* and 12.26 *sublatis*.
- **704** was flagged COSTLY 2.2. It is confirmed by hand: Iām vē \| r(o) ēt Rŭ-tŭ \| lī cēr \| tāt(im) ēt \| Trō-ĕs ĕt \| ōm-nes (14). Troes is two syllables with -ĕs short before *et*. The scanner was right, and the entry only clears the flag, as at 9.811.

### Checked by hand and found right, so no entry

- **733** *Fugit ocior euro*: eu is one syllable, and the line has 17 syllables, all dactyls (cost 1.5, right).
- **738** *Teucri* is Teu-crī, and *pālantia* has a long pā (cost 1.5, right).
- **655** *deiecturum* is dē-iec, which the scanner has. *exscĭdio* has a short i (from *exscindo*); the metre requires it.
- **706** *ariete* is ar-ye-te, as 7.175.
- **654**, **678**, **697** and **723** are the Ae- lines, fixed above.
- **651** *Săcēs* is an unknown name, so the scanner's quantities stand. **659** *praetereā*, *tŭī*. **679** *indĕcŏrem*. **693** *tel(a) ĭnhĭbēte*, where h makes no position. **694** *me(a) est*. **701** *Ăthōs*, *Ĕryx*. **715** *Sīla*. **721** *obnīxi*. **726** *imponit di-*. **739** *suffēcit*, *de(i) ad*, *Vōlcānia*. **740** *fūtilis*, *glaciēs*, *ceu*. **741** *fulvā*. **742** *āmens*. **743** *inde huc*.
- **650**–**652**, **656**–**677**, **681**–**685**, **688**, **690**–**696**, **698**–**703**, **705**–**708**, **710**, **712**–**722**, **724**–**728**, **731**–**737**, **739**–**743** and **745** have the quantities and elisions the scanner gives them.

There is no hiatus in the part.

### Left as scanned (house practice, QUESTIONS item 31)

- **684** *sa-xum* is divided before x.
- Prefix divisions that close the syllable anyway, such as *res-pexit* (671), *res-plendent* (741), *obs-tipuit* (665) and *cons-cendebat* (736), need no entry. So do *ā-vulsum* (685) and *ā-mens* (742), where the vowel is long by nature.

## Medium

- **M1 (missing elisions, 4 edits):**
  - 682 *perqu(e) hostis* (unit 681);
  - 719 *tot(a) armenta* (unit 717);
  - 722 *coll(a) armosque* (unit 720);
  - 725 *aequat(o) examine* (unit 725).
- **M2 (690 `l`).** "thus to the city rushes, to the walls" made the genitive *urbis* a destination. It now reads "thus of the city rushes to the walls", which agrees with the note ("to the walls of the city") and with `i`.
- **M3 (`i`, precautionary rephrasings, 11 edits).** Each phrase is close to stock modern renderings, so each was rebuilt from the Latin. `l` was not touched.
  - **653.** "our last hope of safety is in you: have pity on your people" is now "the last of our safety lies in you: take pity on your own".
  - **663.** "a harvest of iron bristles with drawn blades" is now "their drawn blades bristle like a standing crop of iron".
  - **668.** "valour that knew its own worth" ("conscious worth" is a stock phrase) is now "the courage he knew was his".
  - **677.** "where god and cruel Fortune call, let us follow" is now "let us go where the god and harsh Fortune summon us".
  - **680.** "Let me, I beg you, rage out this madness first" is now "I beg you, let me first rage this madness through to its end".
  - **701–703.** "huge as Athos, or as Eryx, or as father Apennine … snowy crown" is now "as vast as Athos or Eryx, or as father Apennine himself, roaring with his shimmering holm-oaks and glad to rear his snow-capped head into the air".
  - **714.** "chance and courage blended into one" is now "luck and valour were mixed past telling apart".
  - **723–724.** "clash with their shields; a mighty crash filled the heavens" is now "run together shield against shield; a vast din filled the upper air".
  - **725–727.** "held up a pair of scales with the beam level … which side death would weigh down" is now "lifted the two pans of his balance, the pointer set true, and placed in them the separate destinies of the two, to learn which of them the struggle would doom and to which side death's weight would drag the beam".
  - **739–741.** "the mortal blade shattered at the blow like brittle ice" is now "the blade of mortal make burst apart at the stroke as brittle ice does".
  - **743.** "weaving aimless circles this way and that" is now "winding this way and that in loops that led nowhere".

## Low

- **L1 (651 `l`).** "by an arrow, in front" read as if *adversa* went with the arrow. The metre shows *adversă* is short, so it goes with *ora*. It is now "in front, by an arrow", the Latin order.
- **L2 (665 `l`).** "by the varied confused image" made *confusus* an adjective of the image. It is now "by the varied, confused, image of things".
- **L3 (716–717 `l`).** "when two, turned into hostile battle, bulls / with brows charge" attached "turned" to the battle. It is now "when two, with turned, into hostile battle, bulls / brows charge", with *conversis… frontibus* kept together.
- **L4 ("framing the line" where it does not, 4 edits).** The phrase was removed at four places:
  - 663 *strictis… mucronibus* is now "round 'seges'";
  - 716 *conversis… frontibus* is now "the noun held over to the next line";
  - 732 *in medio… ictu* is now "round 'ardentem deserit'";
  - 742 *diversa… aequora* is now "round 'fuga petit'".
  - Also 725 *duas… lances* is now "round 'aequato examine'" (in the L7 edit).
- **L5 (693).** "one at each end of the line" was wrong, since *Rutuli* is the third word. It is now "one in each half of the line".
- **L6 (723, rule 5b wording).** The quotation marks were added: "The print has 'alitur', a misprint for 'aliter', corrected here:". The rest of the drafter's handling is upheld: `t` as printed, `l` and `i` reading *aliter*, and the note opening with the print's reading.
- **L7 (727 *letum;*, rule 5b form, 2 edits).** The drafter's remark sat at the end of the note. It is now the opening, in the house formula (as aeneid-080 and 094): "The print has a semicolon after 'letum' (727), with 'Emicat' following in capital, a misprint for a full stop, corrected here." The unit already ends at the semicolon, and `l` and `i` end the sentence there, so neither changed.
- **L8 (743 *orbes*, rule 5b form).** The note now reads: "The print has no mark after 'orbes' (743), a misprint for a stop (a semicolon is read here), corrected here: 'enim' begins a new clause." This follows the aeneid-069 *Idaeae* wording. `l` and `i` already had the semicolon.
- **L9 (scansion glosses that go with the scan-fixes, 11 edits):**
  - 653 *suprema*;
  - 654, 697 and 723 *Aeneas*, Ae- one long syllable (723 adds that the line scans the same with either reading);
  - 680 *oro*, both syllables long;
  - 689 *disiecta* and 711 *coniectis*, consonantal i;
  - 704 and 730 *Troes*, two syllables;
  - 709 *coiisse*, four syllables;
  - 744 *Teucri*.
- **L10** is the division-only scan-fixes 686, 687 and 729, listed above.
- **L11** is the 704 confirmation entry, listed above.

## Refused or upheld (no change)

1. **Narrative `i` tense** is past throughout, so there is nothing to change. The similes (684–689, 701–703, 715–722) and the speeches keep the present. 735 "The story goes" is a frame and is fine.
2. **Speech marks** are right in `t`, `l` and `i` for all three speeches. 681 *Dixit* and 692 *incipit ore:* are unmarked narrative.
3. **`p` flags** at 650 and 697 are upheld. `new-renderings.md` says "None", which is upheld: no set piece falls in the part.
4. **651 *adversa… ora* as an "accusative of respect, the Greek construction"** is upheld. The metre confirms the short -ă.
5. **659 *tui fidissima*, "objective genitive"** is upheld (genitive with an adjective).
6. **667 *mixto… luctu*, "ablative absolute or of attendant circumstance"** is upheld.
7. **688 *exsultat solo*, "ablative of separation"** is upheld. "Over the ground" is also possible, but the note's reading is defensible.
8. **694 *verius*, with *est* understood** is upheld.
9. **727 *quo… pondere*, "with which weight"** is upheld. Some take *quo* as "whither" with *pondere* instrumental. The `i` ("to which side death's weight would drag the beam") suits both readings.
10. **732–733 *deserit… ni… subeat* as a mixed condition** with a vivid indicative is upheld (A&G).
11. **655 *exscidio* as a "dative of goal"** is upheld. The *exscidium/excidium* remark is right.
12. **656 *Latini* as plural**, set against *rex ipse Latinus*, is upheld.
13. **708–709 *ingentis… viros*, "framing two lines"** is upheld. It is loose, since *viros* is mid-line, but the hyperbaton does span the two lines.
14. **723 rule 5b** is upheld. The correction is clear: *alitur* does not construe, *non aliter* is Virgil's formula, and the Latin Library has *aliter*.
15. **743 rule 5 (adding the mark to the source)** was not applied. Nobody has seen Greenough's printed page, so it is not known that the print has the mark. It is treated under 5b as aeneid-069 was. The run lead may decide otherwise (see below).
16. **"From memory" attributions** all keep their markers. Each was checked for plausibility:
    - Iliad XIII boulder (684 note; Hector as the rolling rock, about 13.136–142);
    - Iliad XIII snowy mountain (701 note; 13.754);
    - Iliad II earth groaning (713 note; about 2.781–785);
    - Georgics III bull-fight (715 note; about 3.209–241);
    - Iliad XXII scales (725 note; about 22.209–213);
    - Iliad XXII chase round Troy (742 note).
    All are plausible.
17. **Cross-references** were checked in the source (listed above) and are right.
18. **Variants.** The drafter's notes on 662 *acies* and 714 *miscetur* ("sense the same") are enough. 655, 670, 673, 720, 739, 740 and 743 are orthography or morphology.
19. **Unchanged `i` lines** were checked for echo and kept as literal: 650, 656, 665, 676, 693–696, 713, 733, 735–737 and 741. They include "The earth groaned" for *Dat gemitum tellus* and "faster than the east wind".
20. **The scanner is right** at 655, 704, 706, 733, 738 and the other lines listed above, so they get no new entries beyond the 704 flag-clearing one.
21. **Prefix divisions that close the syllable, and the division before x**, get no entries, following QUESTIONS item 31.
22. **No advisory.** 659–660 mentions Amata's suicide in one line, without detail. The rest is ordinary battle.

## For the run lead

- **`scan-fixes.json`** now holds 15 new keys, 12.653 to 12.744 as listed, appended after 12.648. Nothing else in the file changed.
- **Rule 5b, for `QUESTIONS.md`/`LOG.md`:** three corrections in the reading text, with `t` as printed:
  - 12.723 *alitur* → *aliter*;
  - 12.727 *letum;* + capital *Emicat* → a full stop;
  - 12.743 no mark after *orbes* → a semicolon.
- **Decision for you:** 743 could instead go under rule 5 (add the semicolon to `source/aeneid-greenough.json` and re-pin) only if you are satisfied that Greenough's printed page has the mark. I could not verify the print. It is handled under 5b, as aeneid-069 handled *Idaeae*.
- **Unchecked, from memory:**
  - the Homeric line numbers above;
  - *exscĭdium* with a short i (inferred from the metre and from *scindo*);
  - *fūtilis* with a long u;
  - *Săcēs* (quantities unknown; the scanner's kept).
