# Review — aeneid-099 (Aeneid XII.843–952), adversarial reviewer

**Severity counts:**
- **Major: 9.** All 9 are wrong scansions: 847, 881, 887, 905, 909, 919, 929, 935 and 939. The packet flagged only 905 (UNRESOLVED). Four had a cost of 0.0 (847, 909, 929, 935). Two were false fits with the right syllable count (881 and 929).
- **Medium: 3** findings (26 edits).
  - One elision was missing (947 *Tun(e) hinc*).
  - 844 `l` attached *fratris* to the verb instead of to *armis*.
  - Twenty-four `i` renderings were rephrased as a precaution against remembered modern versions, mostly in Juturna's lament, the dream simile, Turnus's plea and Aeneas's last words.
- **Low: 17** findings (16 edits plus 5 scan-fixes).
- **Refused or upheld without change: 22.**
- **Scan-fixes added: 14.** They were written straight into `scan-fixes.json` by `drafts/aeneid-099/add_scan_fixes.py --write` and appended after 12.837 in line order. The keys are 12.847, 12.863, 12.868, 12.881, 12.887, 12.903, 12.904, 12.905, 12.909, 12.919, 12.929, 12.935, 12.937 and 12.939.
  - 9 fix wrong scans (Major).
  - 2 change only the syllable division (Low: 868, 937).
  - 1 is a confirmation entered to clear the packet's COSTLY flag (Low: 863, as 12.704 and 12.812).
  - 2 are carrier entries (Low: 903, 904). They hold the scanner's own fit, because a unit with an unresolved line (905) gets no sc at all from the scanner, as 5.431 beside 5.432.
  - The git diff of `scan-fixes.json` is 159 insertions and 0 deletions.

Nothing blocks the build. The `scan_check.py` replica gives sc for 54 of 54 units and applies all 14 entries. It has no report left, no metre failures and no line-up failures. `build_aeneid.py` has no dry-run mode (it takes only the part id and writes), so it was not run.

## How the review was done

**Pass 1** went through all 54 units word by word:
- `l`, `i` and `n` against the Latin, and every grammatical label. Every elision list was checked line by line, and also mechanically against the scanner's elided syllables. Apart from the 947 gap, they agree; the hand scansions of the fixed lines elide the same words.
- The speech marks. There are six speeches: Juturna 872–884, Aeneas 889–893, Turnus 894–895, Turnus 931, Turnus 932–938 and Aeneas 947–949. `t`, `l` and `i` each have 6/6. At 938, `l` and `i` close the speech on the *ulterius* unit and carry no mark on the *Stetit* unit (see below).
- The `p` flags at 843, 887 and 919. All three are right.
- The top-level advisory (see Refused 2).
- Cross-references checked in `source/aeneid-greenough.json`:
  - 12.139–141 (*erepta pro virginitate*, the rule over pools and rivers);
  - 12.785 (Juturna returns the sword);
  - 12.754 (*iam iamque tenet*);
  - 2.774 (*vox faucibus haesit*);
  - 1.92 (*Aeneae solvuntur frigore membra*);
  - 10.495–505 (the belt, *Turno tempus erit*);
  - 10.517–520 (captives for Pallas's pyre);
  - 11.831 (= 952);
  - 5.432 (*genua labant*);
  - 886 *condidit* (picked up by *condit* at 950).

  All are right.

All 110 lines were hand-scanned by quantity and compared with the scanner's fit. `scan_check.py`, `review_check.py` and `add_scan_fixes.py` are 098's, pointed at 099; `review_edits.py` is new, in 098's form. Precedent entries:
- *Aeneas* 12.311, 12.760, 12.783 and 12.794;
- *coniunx* 12.17 and 12.80;
- *adrectas* 12.618 and *Adrexere* 12.251 (division);
- *quies* 12.309 and 10.745;
- *seu* 6.880 and 9.680;
- *genua* 5.432;
- carrier entries 5.431 and 1.330;
- confirmations 12.704 and 12.812.

Sources: the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2** re-read every changed field (42 fields) against `t`:
- each `l` was checked for words on the wrong line;
- each `i` was checked for drift, tense, `l` ↔ `i` agreement and remembered phrasing.

One further fix came out of it. In 940–944 `i`, "Turnus had overcome him" could be read as Aeneas, so it now reads "the boy". It is folded into the M3 edit, and the script was rerun once from the drafter's file.

**Script runs.**
- A copy of the drafter's `units.json` and of `scan-fixes.json` was kept before editing, at `/tmp/claude-0/-home-user-Lectorium/0863283f-111c-5e52-91ff-d94256272702/scratchpad/units.orig.json` and `scan-fixes.orig.json`.
- `review_edits.py` runs once from the drafter's file and makes 42 edits to 42 fields. Each old string is asserted to occur exactly once. Its guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part`, `about` and `advisory` are unchanged;
  - `l` line counts equal those of `t`;
  - no `i` contains a line break;
  - every note is 15–139 words;
  - the 952 house `l` and `i` are intact.
- `review_check.py` prints no faults:
  - it exempts the mark count at 938 and the quoted marks in the 930 and 938 notes, for the reasons below;
  - marks are t 6/6, l 6/6, i 6/6;
  - notes run 42–109 words;
  - 54 units, 110 lines;
  - `BUILD REPLICA: OK`;
  - `t/ln/p/v vs drafter: OK`.
- `make_units.py` was not rerun and still holds the drafter's strings. Build from `units.json`, and do not rerun `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 847 | **0.0** | *eōdem* has a long o, so it cannot stand as two shorts. Its *eo* is one long syllable by synizesis, with *uno* elided into it: ū-n(o) eō \| dēm-quĕ tŭ \| līt pār \| tū pă-rĭ \| būs-quĕ rĕ \| vīn-xit (15). The scanner read e-o-dem with a short o (16). The draft's note already said synizesis. |
| 881 | 0.8 | *frātrī* has a long a (frāter) and a long -ī, and *cŏmĕs* is short-short: nūnc cēr \| t(e) ēt mĭ-sĕ \| rō frā \| trī cŏ-mĕs \| ī-rĕ pĕr \| ūm-bras (15). The scanner made fra-tri short and co-mes long. This is a false fit with the same count. |
| 887 | 1.2 | *Aeneas*: Ae-nē \| ās īns \| tāt cōn \| trā tē \| lūm-quĕ cŏ \| rūs-cat (13). The scanner split Ae- (14). |
| 905 | UNRESOLVED (flagged) | *genua* has a consonantal u, gen-wa, as 5.432: gēn-wă lă \| bānt gĕ-lĭ \| dūs cōn \| crē-vīt \| frī-gŏ-rĕ \| sān-guis (15). |
| 909 | **0.0** | *quies* is quĭ-ēs (as 12.309), *noctĕ* has a short -ĕ, *nēquīquam* is long-long, and *ăvĭdōs* is short-short-long: nōc-tĕ quĭ \| ēs nē \| quīqu(am) ă-vĭ \| dōs ēx \| tēn-dĕ-rĕ \| cūr-sus (15). The scanner ran quies into one syllable and got four quantities wrong (14). |
| 919 | 1.2 | *Aeneas*, with *telum* elided into it: Cūnc-tān \| tī tē \| l(um) Ae-nē \| ās fā \| tā-lĕ cŏ \| rūs-cat (13). The scanner split Ae- (14). |
| 929 | **0.0** | *lātē* is long-long and *nĕmŏră* short-short: mōns cīr \| c(um) ēt vō \| cēm lā \| tē nĕ-mŏ \| r(a) āl-tă rĕ \| mīt-tunt (14). The scanner made la-te short and ne-mo long. This is a false fit with the same count. |
| 935 | **0.0** | *seu* is one syllable and *mē* is long: ēt mē \| seū cōr \| pūs spŏ-lĭ \| ā-tūm \| lū-mĭ-nĕ \| mā-vis (14). The scanner split se-u and made me short (15). |
| 939 | 1.2 | *Aeneas*: Ae-nē \| ās vōl \| vēns ŏ-cŭ \| lōs dēx \| trām-quĕ rĕ \| prēs-sit (14). The scanner split Ae- (15). |

### Low (scan-fixes)

- **Division only**, with the same feet and quantities as the scanner's fit. Each scanner division put an open long mark on a short vowel, which the audio would voice long. This follows the recent Book XII practice (093–098; QUESTIONS items 85 and 90; 12.618, 12.17).
  - **868** *adrectaeque* is now ad-rēc-tae-que, not a-drec-.
  - **937** *coniunx* is now con-iunx, not co-niunx.
- **863** was flagged COSTLY 2.0. It is confirmed by hand: quae quōn \| d(am) īn būs \| tīs aūt \| cūl-mĭ-nĭ \| būs dē \| sēr-tis (13). The cost comes from the spondaic fifth foot (*culminibus desertis*). The entry only clears the flag, as at 12.704 and 12.812.
- **903, 904** are carrier entries holding the scanner's own fit, both hand-checked. The scanner gives no sc to a unit containing an unresolved line, and 903–905 are one unit; without these entries the build would leave 903 and 904 blank. This follows 5.431 and 1.330–333.

### Checked by hand and found right, so no entry

- **889** *deinde* is two syllables by synizesis, and the scanner has it so (as 12.195).
- **882** *eg(o) Aut* is elided across the question mark. **883** *Ō quae* has no hiatus, since *erit* ends in a consonant.
- **942** *bāltĕŭs* has three syllables. **903** *ĕ-ūn-tem* is not the diphthong eu.
- **923** *ātri* has a long a by nature, so the open long is right.
- **898** *ă-grō*, **876** *vŏ-lŭ-crēs*, **889** *rĕ-trāc-tas*, **924** *rĕ-clū-dit* and **901** *trĕ-pĭ-dā* all keep a short open vowel before the mute and liquid.
- **896, 897, 904** *sa–xum* keep the house division before x (as 9.448 and 7.567).
- **927** *poplite* is left as the scanner has it (*po–pli*), as 12.492 was published in aeneid-095. See Refused 3.
- Every other line has the quantities and elisions the scanner gives it. The Ae- of *aegris*, *aethere*, *aeternam* and *aegri* is the ordinary diphthong, read right.

There is no hiatus in the part. There is no Greek eu. The only consonantal i after a prefix is *coniunx* at 937.

## Medium

- **M1 (missing elision, 947).** The 947 unit's note said "No elisions". It now gives "Elision 'Tun(e) hinc'". The scanner and the hand scansion both elide it.
- **M2 (844 `l`).** "and Juturna prepares from her brother to send away, from the arms" made *fratris* depend on the verb. It is genitive with *armis*. It now reads "and Juturna prepares, of her brother, to send away from the arms".
- **M3 (`i`, precautionary rephrasings, 24 edits).** Each was rebuilt from the Latin. `l` was not touched in these edits. The old wordings are in `review_edits.py`.
  - **869–871.** "she marred her face with her nails and beat her breast with her fists" is now "the unhappy sister tore at her loosened hair and disfigured her face with her nails, her breast with her fists". This keeps the one verb *foedans*.
  - **872.** "What help can your sister give you now, Turnus?" is now "Turnus, what is there now that your sister has the power to do for you?"
  - **873–874.** "Can I stand against such a monster as this?" is now "Am I one to set myself against a portent such as this?"
  - **875–878.** "Do not terrify me… I am frightened already… I do not mistake the haughty orders" is now "Do not try to frighten me… I am afraid already… I read aright the proud commands".
  - **878.** "Is this what he pays me for my maidenhood?" is now "Is this what he gives me back in exchange for my maidenhood?"
  - **879.** "Why did he give me a life without end?" is now "To what end did he make my life endless?"
  - **879–881.** "…and go with my poor brother through the shades!" is now "Why am I denied the lot of death? … keep my poor brother company on his way through the shades!"
  - **882–884.** "Oh, what earth will gape deep enough for me, and send a goddess down to the Shades below?" is now "Oh, where is the earth that will open deep enough for me, and carry a goddess down to the lowest of the Shades?"
  - **885–886.** "So much she said… with many a groan" is now "She said no more… groaning deeply". "sea-grey" is now "grey-green", as the note has it.
  - **889.** "What is the delay now? Why are you still holding back, Turnus?" is now "What is it that keeps us waiting now? Turnus, why do you still shrink back?"
  - **894–895.** "Your hot words do not frighten me, savage: it is the gods that frighten me, and Jupiter my enemy" is now "…fierce as you are; the gods are what frighten me, and Jupiter, who is now my enemy". `new-renderings.md` is updated to match.
  - **903–905.** "his knees gave way, and his blood thickened, frozen with cold" is now "running or walking… he did not know himself; his knees buckled, and his blood went cold and thick".
  - **908–912 (the dream simile).** The whole sentence is rebuilt, still in the present: "And just as in sleep, when at night a heavy rest has pressed our eyes shut, we seem to want, and want in vain, to lengthen our eager running, and halfway through the struggle we slump, spent; the tongue has no power, the strength we know gives out in the body, and no voice comes, no words:".
  - **926–927.** "Struck, huge Turnus fell to the ground, his knee bent double under him" is now "Hit, the huge Turnus came down to the ground, his knee folding under him".
  - **930–931.** "I have earned this, truly, and I make no plea against it" is now "I have deserved it, I grant, and I ask no reprieve". The gesture is now "Brought low, a suppliant, he lifted his eyes and held out his right hand to plead".
  - **932.** "Make use of your fortune" is now "Take what your fortune gives".
  - **932–936 (Turnus's plea).** "If any thought for an unhappy parent can touch you (you too had such a father in Anchises)…" is now "If care for a father in his misery can move you at all (and Anchises was such a father to you), I pray you, take pity on the old age of Daunus, and give me back to my own, or, if you choose, my body, stripped of the light".
  - **936–937.** "You have won, and the Italians have seen me beaten…; Lavinia is yours to marry" is now "The victory is yours, and the men of Ausonia have watched me, beaten, stretch out my hands; Lavinia is yours for a wife".
  - **938.** "do not carry your hatred any further" is now "let your hatred stretch no further". This keeps the *tendere* / *tende* play the note points out.
  - **940–944.** "the ill-fated baldric… flashed with its familiar studs" is now "the ill-starred baldric caught his eye, and the belt of the boy Pallas glinted with the studs he knew so well: Turnus had overcome the boy…". "ill-starred" matches `l`.
  - **947–948.** "You, dressed in the spoils of one of mine, are you to be snatched out of my hands?" is now "Are you to be torn from my grasp here, you, decked out in the spoils of one of mine?"
  - **948–949.** "It is Pallas who deals you this wound, Pallas who offers you up as a victim…" is now "This wound is the wound of Pallas; Pallas makes an offering of you, and takes his payment out of your guilty blood". The "It is Pallas who…" frame is common to remembered versions. `new-renderings.md` is updated to match.
  - **950–951.** "in a blaze of fury" is now "and as he spoke he drove the sword deep into the breast that faced him, burning with rage".
  - **951.** "But Turnus's limbs went slack and cold" is now "But the cold undid Turnus's limbs". The 952 part of `i` and all of `l` are the house rendering and are unchanged; the script asserts it.

## Low

- **L1 (863 note).** Added the spondaic fifth foot, *culminibus desertis*, as the gloss for the confirmation entry.
- **L2 (879 note).** "the other part of Jupiter's payment with her rule over pools and rivers (12.139–141)" implied that 139–141 names her immortality, but they name only the rule over waters. It is now "which she counts as Jupiter's payment along with the rule over pools and rivers that the poem named".
- **L3 (881 note).** Added that *cŏmĕs* is short-short and *frātrī* has a long a (scan-fix gloss).
- **L4 (891–893 `l`).** "choose the steep" for *opta* is now "wish the steep", as in the note ("wish, pray").
- **L5 (895 note).** The draft said "'terrent' and 'me' turned round from the first clause". They are not: both clauses have *me… terrent*. It now says the *me… terrent* of the first clause is repeated, with the real subject now named.
- **L6 (905 note).** *genua* as gen-wa is now marked "as in the same words at 5.432".
- **L7 (909 note).** Added *quies*, two syllables, and *nēquīquam*, with its first two syllables long (scan-fix gloss).
- **L8 (929 note).** Added that *late* has both syllables long (scan-fix gloss).
- **L9 (935 note).** Added that *seu* is one syllable (scan-fix gloss).
- **L10 (937 note).** "given up in five words" is wrong, since *tua est Lavinia coniunx* is four. The note now also says *coniunx* is con-iunx.
- **L11 (938 notes, rule-5b form).** Both notes are aligned with 098's 803/806 house formula:
  - the *ulterius* unit drops "so l and i close it there while t keeps the print";
  - the *Stetit* unit now reads "The closing speech mark the print sets before 'Stetit' belongs to the end of the previous unit; t keeps it, and l and i carry none here."
- **L12 (940–944 note).** "the day would come when he wished it untouched (X.495–505, from memory)" is wrong. At 10.503–505 Turnus will wish *Pallas* untouched (*intactum Pallanta*) and hate the spoils and the day. It now says that.
- **L13 (867, 948, 951 notes).** "from memory" is dropped from 2.774, 10.517–520 and I.92, which were checked in the pinned source (3 edits).
- **L14–L17** are the scan-fixes listed above: 863 (confirmation), 868 and 937 (division), and 903 and 904 (carriers).

## Refused or upheld (no change)

1. **931 `deprecor, ”inquit:` and 938 `odiis. ”Stetit`** are upheld as misprints under rule 5b, handled as 098's 12.806: `t` as printed, `l`/`i` corrected, and the note opening "The print has…".
   - At 931 the marks counts agree in every layer. Only the spacing is wrong; *inquit* stands outside the marks.
   - At 938, `l`/`i` close on the *ulterius* unit, and the *Stetit* unit carries none in `l`/`i`. `review_check.py` exempts 938, and the 930 and 938 notes quote the marks.
2. **The advisory** is upheld as accurate. Juturna's *Haec pro virginitate reponit?* (878) names the act of 12.140–141 in one phrase, inside a bitter question about her immortality. Nothing is described. It follows aeneid-092's advisory and form (lede/more) under "sexual violence always". The lede's line references (878; 140–141) are right.
3. **927 *poplite*** keeps the scanner's division and long open *po–*, as 12.492 (aeneid-095), 10.699 (080) and 9.762 (071) were published. If *pŏples* has a short o (my belief, not checked in a public-domain dictionary), then *pop-li* with the syllable long by position is the right division. That belongs with item 85's sweep, not a one-line exception here.
4. **896, 897, 904 *sa–xum*** keeps the house division.
5. **889 *deinde***: the scanner is right.
6. **868 and 937** keep the scanner's third-foot trochaic caesura. **910** keeps the scanner's caesura after *in*. These are markings, not quantities.
7. **845 note**: the Dirae taken as Allecto and Tisiphone, with Megaera the third, is upheld as the usual reading.
8. **873 *durae*** with both readings given is upheld. `i` takes "hard-fated".
9. **882 "Immortal, am I?"** and **875 "Now, yes, now I leave the field"** are kept as not distinctive.
10. **862 `i`** keeps "the little bird"; the note names the owl.
11. **Unchanged `i` elsewhere** was checked for echo and kept as close to the Latin and not distinctive:
    - 843–866 (except 869–871);
    - 887–888, 890, 891–893, 896–902, 906–907, 913–925 and 928–929;
    - 938–939 (Aeneas stands) and 945–947 (*Ille, oculis postquam…*).
12. **952** is the house rendering (conventions.md, XI.831 = XII.952) and is unchanged in `l` and `i`.
13. **"From memory" attributions** to other works keep their markers. Each was checked for plausibility, and all are plausible:
    - Aeschylus, *Eumenides* (Night mother of the Furies);
    - Iliad 21.403–405 (Athena's boundary-stone);
    - 5.302–304 and 12.445–449 (stones beyond two men of today);
    - 22.199–201 (the dream);
    - 7.220 (Ajax's sevenfold shield);
    - 22.338–343 and 24.486ff. (Hector's and Priam's pleas).
14. **Variants.** The drafter notes 883/884 *dehiscet/demittet*, 893 *clausumve*, 899 *illud*, 904 *manus* and 930 *supplexque*, which is enough. The rest are orthography.
15. **`p` flags** at 843, 887 and 919 are upheld.
16. **`about`** is not a field the reviewer edits. It is plain and accurate and was left alone.
17. **932 `l` "If of a wretched you any, parent,"** is ugly but transparent, and is kept.
18. **940 `l` "now, now more and more"** for *iam iamque magis* is kept.
19. **908 `l` "when our eyes, languid, has pressed"** is kept. The commas show that *languida* goes with *quies* on the next line.
20. **901 `i` "hurled"** for *torquebat* is kept. The note explains the imperfect.
21. **Note lengths** (42–109 words) are within the house range.
22. **No new house renderings.** `new-renderings.md`'s "None" stands, and its candidate wordings are updated to the reviewed `i` for 895 and 948–949.

## For the run lead

- **`scan-fixes.json`** now holds 14 new keys, 12.847 to 12.939 as listed, appended after 12.837. Nothing else in the file changed.
- **Rule 5b, for `QUESTIONS.md`/`LOG.md`:** two corrections in the reading text, with `t` as printed:
  - 12.931 `deprecor, ”inquit` → `deprecor,” inquit`;
  - 12.938 `odiis. ”Stetit` → `odiis.” Stetit`.

  These are the closing-mark spacing pattern of items 82–86 and 90 (once more: fix it in `archive_aeneid.py`?).
- **Advisory** (878) is kept, following 092. The owner may drop both if he rules that a one-phrase mention does not qualify (item 84).
- **Unchecked, from memory:**
  - the vowel of *poples* (927);
  - the Homeric and Aeschylean references listed above;
  - Allecto and Tisiphone as the two Dirae.
