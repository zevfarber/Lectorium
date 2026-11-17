# Review — aeneid-096 (Aeneid XII.554–649), adversarial reviewer

**Severity counts:**
- **Major: 9.** Eight wrong scansions, none of them flagged by the scanner: 554, 562, 580, 613, 623, 628, 642 and 648. Two had a cost of 0.0 (623 and 642). The rest ran from 0.6 to 1.5, under the COSTLY threshold, and 628 was a false fit with the right syllable count. The ninth is the packet-flagged half-line 631 (UNRESOLVED), which blocked the build until it got a half-line entry.
- **Medium: 4** findings (11 edits). One elision in a list was wrong (633 *ha(ec) in*: *haec* ends in -c). Six elisions were missing (554, 557, 603, 612, 637/638 across units, 638). The 631 note gave the wrong metre for the half-line. Three `i` renderings were rephrased as a precaution against remembered modern versions (638–640, 646, 646–647).
- **Low: 8** findings (13 edits plus 1 scan-fix). There were 7 note findings, 1 of them carried into `l`/`i` at 632, and 1 scan-fix that changes only the syllable division (618).
- **Refused or upheld without change: 20.**
- **Scan-fixes added: 10.** Written straight into `scan-fixes.json` by `drafts/aeneid-096/add_scan_fixes.py --write`, appended after 12.553 in line order. The keys are 12.554, 12.562, 12.580, 12.613, 12.618, 12.623, 12.628, 12.631, 12.642 and 12.648. Of these, 8 are wrong scans (Major), 1 is the half-line (Major, build-blocking), and 1 is a division-only fix (Low, 618). The git diff of `scan-fixes.json` is 108 insertions, 0 deletions.

Nothing blocks the build: `scan_check.py` replica gives sc for 54 of 54 units, no report left, no metre failures and no line-up failures. `build_aeneid.py` itself was not run.

## How the review was done

**Pass 1** went through all 54 units word by word:
- `l`, `i` and `n` against the Latin, every grammatical label, and every elision list line by line (each line also hand-scanned, which is how the missing elisions showed up).
- The speech marks. There are four speeches: Aeneas 565–573, Turnus to himself 620–621, Juturna 625–630, and Turnus 632–649. 631 *Turnus ad haec:* is narrative and is rightly unmarked. `t`, `l` and `i` are all 4/4, and match unit by unit.
- The `p` flags (554, 593 and 614, all right).
- The bracketed lines 612–613: the note says Greenough brackets them as spurious, as the conventions require.
- The rule-5 semicolon at 616 (commit `51a5905bb`).
- Cross-references checked in `source/aeneid-greenough.json`: 12.64–69, 12.222–224, 12.457, 12.460, 12.463, 12.467, 12.469, 12.529–534, 12.543, 4.519, 4.666, 4.668, 7.371–372, 11.471–472 and 1.76. All are right.

All 96 lines were hand-scanned by quantity and compared with the scanner's fit. `scan_check.py` and `review_check.py` are 095's, pointed at 096. Precedent entries: Aeneas 12.311, Teucros 12.506, adlapsa 12.319, abrupto 12.451, and the half-line entries (for example 11.375). Sources: the Latin, the pinned source and memory of the public-domain references only. No translation was opened.

**Pass 2** re-read every changed field, every `l` for words on the wrong line, and every `i` for drift, tense and remembered phrasing. It found three things to fold into `review_edits.py`, which was rerun from the drafter's copy:
- a redundant gloss added at 632 was dropped;
- the 612 addition was merged into the existing 'Aenean' gloss;
- one more precautionary `i` rephrasing was added at 646–647.

**Script runs.**
- The drafter's `units.json` round-trips byte-identically through `aeneid_lib.jdump`. A copy was kept at `/tmp/claude-0/-home-user-Lectorium/566d2cb7-a930-50c3-aedc-6b98622ba27f/scratchpad/units.orig.json` before editing.
- `review_edits.py` runs once from the drafter's file and makes 24 edits to 22 fields. Each old string is asserted to occur exactly once. Its guards confirm:
  - `t`, `ln`, `p`, `v`, `title`, `titleEn`, `part` and `about` are unchanged;
  - `l` line counts equal those of `t`;
  - no `i` contains a line break;
  - every note is 15–139 words.
- `review_check.py` prints no faults:
  - marks are t 4/4, l 4/4, i 4/4;
  - notes run 32–107 words;
  - 54 units, 96 lines;
  - `BUILD REPLICA: OK`;
  - `t/ln/p/v vs drafter: OK`.
- `make_units.py` was not rerun and still holds the drafter's strings. Build from `units.json`, and do not rerun `make_units.py`.

## Scansion

### Major (one per line)

| line | scanner (cost) | right reading |
|---|---|---|
| 554 | 1.2 | *Aeneae* (dative) Ae-nē-ae, with *mentem* elided into it: Hīc mēn \| t(em) Ae-nē \| ae gĕ-nĕ \| trīx pūl \| chēr-rĭ-mă \| mī-sit (14). The scanner split Ae- (15). |
| 562 | 0.6 | *Teucrum* Teu-crum, Greek eu; *quō* long: dūc-tō \| rēs tŭ-mŭ \| lūm-quĕ că \| pīt quō \| cē-tĕ-ră \| Teu-crum (15). The scanner split Te-u and shortened *quo* (16). |
| 580 | 1.2 | *Aeneas*, with *magnā* (ablative with *voce*) and *incūsat* long, so four spondees open the line: Ae-nē \| ās māg \| nāqu(e) īn \| cū-sāt \| vō-cĕ Lă \| tī-num (13). The scanner split Ae- (14). |
| 613 | 1.2 | *Aenean* Ae-nē-ān (bracketed line, scanned as it stands): Dār-dă-nĭ \| (um) Ae-nē \| ān gĕ-nĕ \| rūm-qu(e) ād \| scī-vĕ-rĭt \| ūl-tro (15). The scanner split Ae- (16). |
| 623 | **0.0** | *huic* is one syllable (as 12.488): Ātqu(e) huīc \| īn fă-cĭ \| ēm sŏ-rŏr \| ūt cōn \| vēr-să Mĕ \| tīs-ci (15). The scanner read hŭ-ĭc (16). |
| 628 | 1.0 | *Aeneas* Ae-nē-ās; *Ĭtalis* has a short I (as *Itali* 1.109, *Italos* 12.582): Īn-grŭ-ĭt \| Ae-nē \| ās Ĭ-tă \| līs ēt \| proē-lĭ-ă \| mīs-cet (15). The scanner split Ae- and made Ī-tā- long, a false fit with the same count. |
| 642 | **0.0** | *Teucri* Teu-crī, Greek eu: ād-spĭ-cĕ \| rēt Teu \| crī pŏ-tĭ \| ūn-tūr \| cōr-pŏ-r(e) ĕt \| ār-mis (15). The scanner split Te-u (16). |
| 648 | 1.5 | *istīus* has three syllables with a long ī, and *ănĭma* is short-short: Sānct(a) ād \| vōs ănĭ \| m(a) ātqu(e) īs \| tī-ūs \| nēs-cĭ-ă \| cūl-pae (14). The scanner made a-ni- long and ran *is-tius* into two syllables (13). |
| 631 | UNRESOLVED (flagged) | Half-line: Tūr-nŭs ăd \| haec, a dactyl and one syllable. Entered as `['1Tur–nus⏑', 'ad⏑', '2haec×']` with a `Half-line (hemistich)…` why, like the 58 existing half-line entries. The validator's half-line rule passes. |

### Low (syllable division only; same feet and quantities as the scanner's)

- **618** *adrectasque* is ad-rēc-tās, not a-drec-. The open long a- would be voiced as a long vowel. This follows 12.319 *adlapsa* and 12.451 *abrupto*. No caesura is marked, as in the scanner's parse.

### Checked by hand and found right, so no entry

- **561** *Mnesthea*, the Greek accusative, is Mnēs-thĕ-ă: a dactyl, then Sēr-gēs \| tūm-quĕ vŏ…
- **629** *Teucris* is Teū-cris (cost 1.5, right). **582** *Ĭtalos* has the short I (0.0, right).
- **610** *coniugis* has the consonantal i, con-iŭ-gis (1.5, right). **626** *Troiugenas* is Trō-iŭ-gĕ-nās.
- **620** *Ei* is one syllable. **646** *miserum est* is prodelision, *miserumst* (16 syllables).
- **633** *haec in* is not elided, since *haec* ends in -c. The scanner is right here, and the note was wrong (M1).
- **637** *ag(o) aut* elides across the question mark, and the scanner has it.
- **603** *nod(um) informis*, **612** *s(e) incusat* and **638** *Vid(i) oculos* are all in the scanner's fit. Only the notes lacked them (M2).
- **568** *pārēre* (long ā) and **604** *accēpēre*. **605** *Lāvīnia*. **641** *Ūfens*. **639** *Murrānum*.
- **559** *quiētam*, **596** *incessī*, **609** *it scissā*, **619** *urbĭs ĕt*, **630** *nĕc hŏnore* and **649** *magnor(um) haud*.
- **555**–**557**, **563**–**579**, **581**, **583**–**602**, **606**–**608**, **611**, **614**–**617**, **621**–**622**, **624**–**627**, **632**, **634**–**641** and **643**–**647**: the quantities and elisions are as the scanner has them.

There is no hiatus in the part.

### Left as scanned (house practice, QUESTIONS item 31)

- **583** *E-xo-ritur* and **592** *sa-xa* divide before x.
- Prefix divisions that close the syllable anyway (*ads-piceret* 642 in the scanner's own fit, *adg-novi* 632, *exs-pectem* 570) do not put an open long mark on a short vowel. They need no entry.

## Medium (text)

- **M1 (632 note).** The elision list had *ha(ec) in*. *haec* ends in a consonant, so nothing elides. The note now reads: "Elisions 'dud(um) adgnovi', 'tequ(e) haec'; 'haec in' does not elide, since 'haec' ends in a consonant."
- **M2 (missing elisions, 6 edits):**
  - 554 *ment(em) Aeneae* (unit 554 note);
  - 557 *Ill(e) ut*;
  - 603 *nod(um) informis*, where the note said "No elisions";
  - 612 *s(e) incusat*;
  - 637 *ag(o) aut*, across the question mark (added to the *Nam quid ago?* unit, which said "No elisions");
  - 638 *Vid(i) oculos*.
- **M3 (631 note).** The note said "two and a half feet". *Turnus ad haec* is Tūr-nŭs ăd \| haec, a foot and a half. The note now reads "a foot and a half, Tūr-nŭs ăd \| haec" (scan-fix 12.631).
- **M4 (`i`, precautionary rephrasings against remembered modern versions).** Each phrase is close to stock modern renderings, so each was rebuilt from the Latin. `l` was not touched.
  - **638–640.** "calling out to me by name, go down to his death, a giant overcome by a giant's wound" is now "crying out to me, go down to his death, a huge man felled by a wound as huge". "by name" was also not in the Latin.
  - **646.** "Is death so very hard a thing?" is now "Is dying, then, so utterly wretched?" This is closer to *miserum*.
  - **646–647.** "Shades of the dead, be kind to me, since the gods above have turned their favour from me!" is now "Shades below, be gracious to me, since the will of heaven is set against me!"

## Low

**Notes:**
- **L1 (564).** *Celso… aggere* was said to frame "the line"; the unit starts mid-line. It now says "framing 'medius stans'".
- **L2 (593).** *fessis… Latinis* "framing the line" is now "round 'etiam fortuna'". *totam… urbem* "framing the second line" is now "round 'luctu concussit funditus'". 2 edits.
- **L3 (570).** The note said "he does not know they are Juturna's doing", which is not in the text. It now reads "Aeneas treating Turnus as a man already beaten, who keeps refusing the fight."
- **L4 (616).** This is the rule-5 semicolon. "supplied by Lectorium where the digital source dropped a mark; the lowercase 'attulit' shows Greenough did not print a full stop" is now "was added to Lectorium's source under the pipeline's rule for missing punctuation: the Perseus text drops the mark here, and the lowercase 'attulit' shows that Greenough's sentence runs on."
- **L5 (630).** *pugnae* was given only as a dative with *recedes*. The note now adds that some take it with *numero*, "in the tally of the fight". The `i` suits both readings.
- **L6 (632).** *adgnovi* is "recognised", as the note itself says.
  - `l`: "long since I knew you" is now "long since I recognised you".
  - `i`: "I knew you long ago" is now "I saw through you long ago".
- **L7 (scansion glosses that go with the scan-fixes, 5 edits):**
  - 579: *Ĭtalos* has a short I;
  - 628: *Italis*, short I again;
  - 623: *huic* is one syllable;
  - 648: *istius* is is-tī-us, three syllables;
  - 612: *Aenean*, Ae- one long syllable.

**Scan-fixes:**
- **L8** is 618, listed above.

## Refused or upheld (no change)

1. **Narrative `i` tense:** it is already past throughout, so there is nothing to change. The bee simile (587–592) keeps the present, and so do the speeches.
2. **Speech marks:** they are right in `t`, `l` and `i` for all four speeches. 631 is unmarked narrative.
3. **612–613 note:** upheld. It says Greenough brackets the lines, says the Latin Library omits them, and points to XI.471–472 (checked: *qui non adceperit ultro … asciverit urbi*, "with small changes" is right). The `i` carries no brackets, which is house practice: brackets are checked in `l` only.
4. **554 *Aeneae* as a dative** ("put into Aeneas's mind"): upheld.
5. **557 *immunem tanti belli* as a "genitive of separation"**: upheld (A&G, genitive with adjectives of freedom, in poetry).
6. **595 *incessi*, "present passive infinitive of incesso, not a misprint"**: upheld.
7. **598 *mentem turbata*, accusative with a passive participle, "a Greek usage"**: upheld.
8. **604–606 *laniata* with two accusatives, "middle participle"**: upheld.
9. **630 "ablatives of respect"**: upheld.
10. **643 *Exscindine* = *exscindi* + *-ne***: upheld.
11. **646 *miserum est*, "really prodelision, 'miserumst'"**: upheld.
12. **647 *superis* as a dative of possession**: upheld. It could be taken with *aversa*, but the note's reading is standard.
13. **Cross-references** were checked in the source and are right: 607 → IV.668; 608 → IV.666; 602 → IV.519; 605 → 12.64–69; 632 → 12.222–224 (Camers); 623 → 12.469; 641 → 12.460; 645 → 12.463; 557 → 12.467; 574 → 12.457; 638 → 12.529–534 and 543; 648 → VII.371–372; 631 → I.76.
14. **"From memory" marks:** Apollonius II (587) and Servius (603) carry them. Achilles and the dust in Iliad XVIII (611) is well known. Upheld.
15. **649 `i` "never unworthy of my great forefathers"** is a literal rendering of *haud umquam indignus avorum* and not a distinctive echo. Kept.
16. **572 `i` "the head and sum of this accursed war"** is literal (*caput… summa*). Kept.
17. **Variants:** the drafter's notes on 641 (*nostrum ne* / *ne nostrum*) and 648 (*nescia* / *inscia*) are enough. The rest are orthography or morphology (*adcendit*, *Nequa*, *volgatur*, *adrectas*, *aures/auris*, *nec/neque*, *adgnovi*, *volnere*, *adspiceret*).
18. **Scanner right at 561, 582, 610, 629 (and the rest listed above):** no entries.
19. **Prefix divisions with a closed syllable (632, 642, 570) and before x (583, 592):** no entries, following QUESTIONS item 31.
20. **`p` flags (554, 593 and 614) and `new-renderings.md` ("None"):** upheld. No set piece falls in the part. 646 *Usque adeone mori miserum est?* is famous but not on the set-piece list.

## For the run lead

- **`scan-fixes.json`** now holds 10 new keys, 12.554 to 12.648 as listed, appended after 12.553. Nothing else in the file changed.
- **Rule 5 at 616** is already logged by commit `51a5905bb`. The 614 unit's note now says what was done and why.
- **No misprint found. No advisory:** Amata's suicide (601–603) is told in one sentence without graphic detail. It is not sexual violence, and `claude/content-advisory.md` gives it no trigger. Compare QUESTIONS on Dido's suicide, which is still open.
- **Unchecked, from memory:**
  - Apollonius *Arg.* II bee simile;
  - Servius on the hanged denied burial;
  - Iliad XVIII dust;
  - *Ĭtalus* with a short I at 1.109 (confirmed in the source text by the metre only).
