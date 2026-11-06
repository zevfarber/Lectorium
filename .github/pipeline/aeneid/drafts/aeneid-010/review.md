# aeneid-010 — review (II.105–194)

Adversarial review in two passes, from the Latin and public-domain references only. No modern translation was opened and no English
wording was recalled as a source. Cross-references to other lines of Book II (3, 7, 16, 17, 106) were checked against
`source/aeneid-greenough.json`.

- **Pass 1:** every unit field by field: each grammatical label in each `n` against the form in its line; Latin to `l` word by word;
  `l` to `i`; `i` for remembered English; every cross-reference and generalisation; speech marks; `p` flags (the seven Greenough
  paragraphs, 105, 108, 122, 145, 154, 162, 176, all on the right units); the five-line limit. Then **all 90 lines** scanned by hand,
  syllable by syllable, against natural quantities (not "does a hexameter fit"): the scanner reported nothing, but it hands back valid
  lines with wrong quantities.
- **Pass 2:** a re-read of every edited field; a script that applies `scan-fixes.json` over the scanner exactly as `build_aeneid.py`
  does and runs the validator's hexameter test on all 90 lines (**90 pass, 0 fail**; the scanner report is empty); a check that `t`,
  `ln`, `v`, `p`, `title`, `titleEn`, `part` are byte-identical to the draft, that every `l` keeps the line count of its `t`, that no
  `i` has a line break, and that every note is 15–140 words (one 12-word note, #28, expanded). `units.json` was edited by script
  (load / modify / dump, `ensure_ascii=False`, `indent=1`, no trailing newline, as the draft file had). `draft.py` was **not**
  updated and now disagrees with `units.json`; **do not re-run `make_units.py`**.
- The build was **not run** (lead's step). `gloss.json` is not in the folder yet.

**Counts:** Major 4 · Medium 18 · Low 28 (50 findings, each a field of a unit) · scan fixes added 7 (6 lines the scanner had wrong,
1 confirmation) · refused / verified and kept 27. Changed: 31 of 49 units (0 `t`, 5 `l`, 6 `i`, 28 `n`) and `about`.
Title, `titleEn` and `part` were checked and left alone.

## Speech marks

t, l, i all carry: Sinon's first speech opens #3 (108), closes #22 (144); the oracle opens #8 (116); Priam opens #25 (148), closes #30 (151);
Sinon's second speech opens #33 (154) and closes #49 (194). **Line 155:** Greenough's stray second opening mark stays in `t` and `l`
(#33) and is out of `i`; the note of #33 says so (the mention of "aeneid-008 line 754" in it was removed, see Medium 11). **The oracle
has no closing mark in Greenough** (none after 119): `t` and `l` therefore have no mark at #9, and `i` closes it (`won.”`) so that `i`
is balanced (3 open, 3 close in `i`; in `t` and `l` 6 open, 4 close, as the source). The note of #9 says it. Verified, kept.
#31 (*Dixerat.*) and #2 (the colon before 108) are outside any mark. No change.

## Major (false label, false fact, wrong translation, or an unsafe certainty)

1. **#11 (II.122) `n`** — "'medios' being an accusative plural in -os for -is" is false: *medius* is an o-stem and *medios* is its ordinary accusative plural.
2. **#22 (II.141) `n`** — "*miserere* is the imperative of the deponent *miseror*": the verb that takes the genitive is *misereor*.
3. **#46 (II.183) `l`** — "that the sad sacrilege might atone" made *nefas* the subject; *quae* (the image) is the subject and *nefas* the object: "which was to atone for the sad sacrilege".
4. **#49 (II.194) `l`** — "for our descendants those fates remain": *manere* governs *nepotes* in the accusative, "await"; now "and our descendants those fates await".

## Medium

1. **#7 (II.114) `n`** — "as if he were one of the Greeks": in his story Sinon is one of the Greeks.
2. **#8 (II.116) `n`** — "a loose way of saying 'when the expedition first set out for Troy'" was an unsupported gloss of *venistis ad oras*; the note now says the words do not fit the usual Aulis story and that Sinon need not be consistent.
3. **#9 (II.118) `l`** — *reditus* is nominative plural (the metre needs a long -us: *rĕdĭtūs ănĭmā-que*); "the return" -> "the returns".
4. **#9 (II.118) `n`** — same: "the return is to be sought" with *est* understood is singular; now plural *reditus*, *sunt* understood.
5. **#11 (II.122) `n`** — "his later claim that Ulysses had plotted against him": nothing in this part or the packet supports a "later claim"; removed.
6. **#13 (II.124) `n`** — "for fear of Ulysses": a motive the Latin does not give (*taciti* only says they were silent).
7. **#14 (II.126) `n`** — "'bini' and 'quini' being distributive numerals": *bini* is not in the line (*bis* is an adverb); only *quinos* is distributive.
8. **#20 (II.137) `n`** — "'dulcis' is accusative plural for 'dulcis'": garbled; the -is accusative plural stands for *dulces*.
9. **#20 (II.137) `n`** — "the Trojans, who themselves are fathers": an unverifiable generalisation; removed.
10. **#23 (II.145) `n`** — "Aeneas ... says the Trojans' kindness was their undoing": Virgil's Aeneas does not say it here; removed.
11. **#25 (II.148) `n`** — "*Graios* (a Greek accusative form of *Graii*)": it is the ordinary Latin accusative plural of *Graius*.
12. **#33 (II.154) `n`** — "(the same stray mark as at aeneid-008 line 754)": a cross-reference to another part and pipeline housekeeping in a reader note; removed.
13. **#41 (II.171) `n`** — "tied to Lake Triton in Libya": an unverifiable claim about the origin of *Tritonia*; removed.
14. **#42 (II.172) `n`** — "the beginning of a 'vix… cum' sort of sentence": there is no *cum*; the clause is asyndetic with *arsere*.
15. **#42 (II.173) `n`** — "ablative of quality or of manner" for *luminibus arrectis*: an unsafe label; now a plain "ablative phrase".
16. **#44 (II.180) `n`** — "the horse-for-gods swap": garbled; the story is that the Greeks have gone for fresh help.
17. **#47 (II.185) `n`** — "timber fitted together as for the horse at line 16": 2.16 has fir (*abiete*), not oak; now says *textis* echoes *intexunt* and that the timber there is fir.
18. **#48 (II.189) `n`** — "the commentators take *ipsum* to be Calchas": an appeal to authority not checkable here; now "most naturally on Calchas himself".

## Low

1. **#3 (II.108) `i`** — "tried to plan their flight, and to sail away": *cupiere* (desired) was lost and *discedere* narrowed; now "longed to contrive their flight and be gone".
2. **#5 (II.111) `n`** — "the old form with a 'p'": unverifiable; now "a variant spelling with an extra 'p'".
3. **#7 (II.114) `n`** — "Sinon names him as though the Trojans should know him": a guess; removed.
4. **#13 (II.125) `i`** — "watching" for *videbant*; now "foreseeing what was to come".
5. **#13 (II.124) `n`** — *mihi* "dative of interest ('to my hurt')": over-read; plain "to me".
6. **#14 (II.126) `i`** — "shielded by his silence" over-read *tectus*; now "closing himself in".
7. **#18 (II.132) `n`** — "a lively tense": the historic infinitive is a construction.
8. **#20 (II.137) `l`** — "my ancient homeland", "my sweet sons": possessives not in the Latin.
9. **#20 (II.137) `n`** — the objects of *videndi*: "the two 'nec' phrases" misdescribed the second *nec*.
10. **#21 (II.139) `n`** — *fors* "from 'fors sit'": guessed etymology removed.
11. **#22 (II.141) `n`** — "*per* is placed before its noun": trivial and misleading for *te per superos*.
12. **#24 (II.146) `n`** — "the two nouns are the objects (as subject of the infinitive)": accusatives, subject of *levari*.
13. **#28 (II.150) `n`** — 12 words (validator WARN); expanded.
14. **#30 (II.151) `n`** — "(a votive offering)" for *religio*: now "an act of worship".
15. **#32 (II.152) `n`** — "the usual way to describe the gesture of prayer": unverifiable generalisation.
16. **#36 (II.160) `n`** — "(a polite command)" for the wishing subjunctives.
17. **#38 (II.163) `n`** — "the patronymic of Tydeus's son Diomedes": *Tydides* is the son of Tydeus, that is Diomedes.
18. **#39 (II.167) `n`** — *audeo* is semi-deponent.
19. **#40 (II.169) `i`** — "began to ebb": the historic infinitive is not inceptive, and "ebbed ... slipping back" echoed a stock rendering; rephrased.
20. **#42 (II.174) `l`** — "wonderful to tell" -> "wonderful to say" (*dictu*).
21. **#42 (II.174) `i`** — "wonderful to tell" is the stock English of the tag; now "a marvel to speak of".
22. **#42 (II.174) `n`** — gloss of *mirabile dictu* matched to `l`.
23. **#45 (II.182) `n`** — "The verb is in the present: Calchas's prophecy is Sinon's alleged source": muddled; replaced.
24. **#46 (II.183) `n`** — "as 'ita' above": meaningless; the participle's agreement stated.
25. **#47 (II.187) `n`** — the Latin Library variant *posset* is a morphological (tense) variant that does not change the sense; conventions say not to note it.
26. **#48 (II.190) `n`** — "jussive subjunctive" for a wish: *convertant* is optative.
27. **#49 (II.194) `i`** — "that fate awaited our grandsons": *nepotes* is descendants, and *manere* is present.
28. **about** — "swears" for what Sinon does at 154-159 (he calls the powers to witness and declares himself free).

## Scan fixes (scan-fixes.json: 7 entries added, each with its reason)

All 90 lines were scanned by hand; the 83 lines not listed here were checked syllable by syllable and the scanner's parse is the right one.
Wrong in the scanner (6, each a valid hexameter with wrong quantities or a wrong syllable count): **2.157** *sacrata* (sa- long by
position, -crā- long, -ta short, re- short; the scanner had them the other way round); **2.162** and **2.170** *Danaum* read as Da-naum
with a long Da- (the same blind spot as 2.14, 2.36, 2.44, 2.65 of aeneid-009); **2.174** *sudor iit* (iit as one syllable forced the
short final -or long; read as ĭ-ĭt, every quantity natural; flagged doubtful in its reason); **2.182** *improvisi aderunt* (pro- and vi-
long, a- and -de- short, wrongly the other way); **2.193** *Pelopea ad* (pea shown as one long syllable instead of pē with -a elided).
Entered as a confirmation only: **2.164** *Tydides* (Ty- must be long, the one parse that fits; Ulixes short U-).

**Checked and kept (the scanner is right):** 2.114 *Eurypylum* (Eu one syllable, the -si of Suspensi elides before it; ry and py short);
2.111 *hiemps* (hi-emps, hi short); 2.108 *Troia relicta* (ablative, so the -a is long); 2.112 *praecipue* (adverb, long -ē; *iam* elided
before *hic*); 2.115 *adytis* (ă-dў-tis); 2.117 *Iliacas* (Ī-lĭ-ă-cas); 2.119 *Argolica* (ablative, Ar-gŏ-lĭ-cā, the reverse of the
2.78 problem; *Volgi* Vol- long); 2.123 *divom* (dī-vom); 2.131 *unius*; 2.136, 2.142, 2.159, 2.161, 2.189 *si* long in thesis or
arsis (the only parse; the scanner makes short monosyllables long where the metre needs it), 2.189 *manus vi-* with the -nus long
at the main caesura (pause lengthening, the only parse); 2.148 *iam obliviscere* (*iam* elided, *Graios* Grā-ios, two syllables);
2.151 *religio* (long re-, relligio); 2.154 *aeterni ignes* (ae a diphthong, *-ni* elides); 2.155 *ait* (ă-it, long by position
before *vos*); 2.165 *sacrato avellere* (sa- long by position, *avellere* long ā-); 2.166 *Palladium* (Pal-lă-dĭ-um, four syllables,
no synizesis); 2.171 *Tritonia*; 2.172 *simulacrum arsere*; 2.176 *Extemplo*, *Calchas*; 2.177 *Argolicis* (ăr-gŏ-lĭ-cīs); 2.179
*avexere* (right quantities; the syllable division a-ve-xe-re is the scanner's uniform treatment of x and was left); 2.180 *Mycenas*
(Mȳ-cē-nās); 2.187 *recipi*, *duci in*; 2.190 *exitium*; 2.192 *vestram ascendisset*; 2.194 *venturam et*.
No line has Ae- split wrongly here (*aeterni*, *aethere*, *Aeolus* does not occur) and no consonantal-i-after-prefix problem
(*iubet*, *iussit*, *iam*, *ius* are all right); no Greek *eu* other than *Eurypylum* (right).

## Refused findings (verified and kept)

1. #2 "as at 'simulant' in line 17": checked against the source (2.17 *votum pro reditu simulant*); true.
2. #6 "compare 'intexunt abiete costas' at line 16": true (2.16).
3. #17 "'infanda' is the same word as 'infandum' at line 3": true (2.3 *Infandum, regina*).
4. #38 "compare 'Ulixi' at line 7": true (2.7).
5. #38 "ex quo ... ex illo (169)", #40 "ex quo of line 163", #46 "fas, line 157", #40 "historic infinitives, as in line 132": all in this part and true.
6. #1 *ardemus* "vivid present of narrative": acceptable description; kept.
7. #1 *Pelasgae* "the old inhabitants of Greece": the standard gloss; kept.
8. #3 *cupiere* as -ere for -erunt; *Troia relicta* ablative absolute: true.
9. #4 *utinam* with the pluperfect, wish that cannot be fulfilled: true.
10. #5 "*ponti* genitive of *pontus*" and *euntis* "accusative plural of the present participle": true.
11. #7 the Latin Library variant *scitatum* (a supine, same sense): kept; the note says so.
12. #8 *placastis* syncopated; *virgine caesa* ablative absolute; *Danai* vocative: true.
13. #10 *cui fata parent, quem poscat Apollo* indirect questions with the verb of wondering understood: true.
14. #12 *quae sint ea numina divom* indirect question: true.
15. #15 *composito* as an adverbial ablative: true; *vix tandem*: true.
16. #19 *si forte dedissent* pluperfect for a future perfect in secondary sequence: the usual explanation; kept.
17. #21 *quos* connecting relative; *piabunt* with *miserorum morte*: true.
18. #22 *restet* relative clause of characteristic; *ferentis* genitive singular; *quod* adverbial accusative: true.
19. #23 *His lacrimis* as a dative: the usual reading; kept (the ablative of cause is also possible, and the translation is neutral).
20. #27 *immanis* genitive singular agreeing with *equi*: true.
21. #29 *-ve* "a form of vel": the usual account.
22. #33 *hostia* in apposition to the unexpressed *ego*; *vestrum* neuter with *numen*; *deum* genitive plural; *ait* parenthetic: true.
23. #34 *qua* neuter plural after *si*; *sub auras*: true.
24. #36 *Troia* "vocative or nominative" (the same form; the metre cannot tell): kept; *servata ... serves* polyptoton: true.
25. #43 *ni ... repetant, reducant* with the present subjunctive in indirect speech; *avexere*: true. #44 *remenso* passive sense: true.
26. #47 *neu* = *neve*; *caelo* dative of direction (poetic): true.
27. #49 *nostros nepotes* "ours" of the Trojans (Sinon has just been taken in): true; *Pelopea* from *Pelops*, father of Atreus: true.
