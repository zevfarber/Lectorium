## Pass 1

I read Plate III (langdon1923_0044.jpg) line by line at 2–7× zoom: Col. V 42–47 (V 42–43 for comparison) and Col. VI 6–30. For the claims below I also read Plate IV (langdon1923_0045.jpg): VII 20, VII 45, VIII 15, VIII 17 and the colophon (VIII 46). I checked Langdon pp. 15–16 (langdon1923_0020–0021.jpg): transliteration, translation and footnotes 1–10. I also read conventions.md, runbook.md, run3/RUNBOOK.md, packet.md, the published king-list-*.json (glossaries and the IV 1–10 and IV 30 units of ur-i-awan), and the review of uruk-ii-to-kish-iii.

Edits were made by script (scratchpad reviewer/rev1.py, plus one small follow-up for `about`). The JSON was loaded and dumped with indent 1, ensure_ascii=False and no trailing newline, and the dump round-trips byte for byte. No cuneiform was retyped: glyphs were only deleted. Afterwards:
- every glyph sign is a key in signs-cuneiform.json `signs`;
- every `u` name resolves in Unicode;
- every morph `g` covers its word's glyphs exactly once;
- every lemma also in a published glossary has the published wording. The only differences are the line-level numeral glosses ("10; 2 here = 20") and "king (here plural 'kings')", as in the published parts;
- `r3.py build` gives 20 units and `validate` gives **PASS**, with one WARN: the 7 linecheck lines, all confirmed below;
- `signs.py check` says "in sync".

After the build, stories.json was restored with git checkout and the generated story file was deleted. gloss.json and new-lemmas.json were not touched, and no sign was added.

### Changes

- VI 9, VI 13 · words / l / n / morph · **major** · The drafter shipped Langdon's Gimil as two glyphs, x (LACUNA) + ŠU, as `x-šu-{d}suen`. His evidence was that the second part is "drawn like the ŠU of the colophon (VIII 46) and of Gimil-ᵈSin in VIII 15". It is not. In VIII 15, VIII 17 and VIII 46 the copy draws ŠU as one compact upright box with two or three horizontals. Here the drawing is different. It is a wide part, pointed at the left, cross-hatched in the middle and closed by an upright, which touches a box with three long horizontals that ends in a crossing. That two-part long form recurs, identical, in VII 20 (Gimil-ili) and VII 45 (Gimil-ᵈEn-zu), and Langdon reads it as one unit, "Gimil", in all four places. Splitting it into "x + ŠU" gives a reading that neither the copy nor Langdon supports. The copy cannot settle whether it is one sign or two, or whether it is ŠU, so Langdon's reading is the base (conventions: "keep Langdon's reading as the base"), as with the wide two-part NE in VI 30 and the conventional UD.KUŠU₂.
  · Done:
  - The LACUNA glyph was deleted, leaving one SHU glyph (log, šu).
  - Readings are now `šu-{d}suen` and `šu-{d}suen-ke₄`, with say "šusuen" and "šusuenke".
  - The lemma is now `šu-{d}suen` (the VI 3 lemma), and its gloss is broadened to flag the long form.
  - In `l`, "x-Shu-Suen" is now "Shu-Suen".
  - The VI 9 note is rewritten with the comparison above. The VI 13 note now says "Langdon's Gimil in the same long form … (shown as ŠU, uncertain)".
  - `about` is adjusted to match.
- VI 4 · words · **major** · `lugal` was unbracketed in a line that is wholly restored and that the copy shows as lost ("Lines 1–5 defaced"). That presents restored text as preserved, against IV 3 of ur-i-awan ("[lugal]"). · Now "[lugal]".
- VI 4 · n / l / morph gloss of in-ag · minor · The note said "in-ag … ib-ag; both are the plural 'they ruled'", and the gloss called in-ag a "plural reign verb". In ì-n-aĝ₂ the -n- marks a 3rd-person singular agent. Langdon's own fn. 1 says the Scheil tablet writes "correctly … the plural in-ag-meš", which implies that in-ag is not plural.
  · Done:
  - The note now gives the analysis and quotes fn. 1.
  - In `l`, "they-ruled" is now "he-ruled", which follows the house rule for totals with ni-ag (V 32, 41).
  - The `i` keeps "Six kings reigned 93 years."
  - The morph gloss is rewritten. The lemma string `in-ag` is unchanged.
- VI 6 · l · style · "its-[kingship]" bracketed the whole word, but only NAM is in the break. LUGAL and BI are clear on the copy. · Now "its-king[ship]".
- VI 17 · say · style · "ašdarmuti" voiced Langdon's Ašdar for a sign shipped as unread x. The house precedent (IV 30 x-nun-na, say "…nunna") gives an unread sign as "…". · Now "…muti". The `l` and `i` keep "Ashdar(?)-muti" / "Ashdar-muti (?)", and the note explains.
- VI 2 · n · minor · "(perhaps 'he has a god'), but that is a guess" was an etymology that is not in the source. · Now "looks Semitic; its sense is not explained here".
- VI 16 · n · minor · The note did not say that the traces inside the hatching are two horizontal strokes, which do not obviously belong to U (a single corner wedge). · Added. The bracket on [u] stays.
- VI 9, VI 16, VI 17, VI 28–30 · n · style · The notes referred to "the drafter", which means nothing to a reader. · Rephrased as "not identified here", "cannot be confirmed … from the copy" and "a reading of the copy made here".
- about · minor · The list of differences said "two signs it draws that are not identified here (x)". · Now it lists one x (Ashdar-muti) and says that Langdon's Gimil is kept, flagged, where the copy draws the long form.

Counts: 2 major, 5 minor, 3 style.

### Drafter's claims tested

1. **KI after Akšak in V 44 and VI 6: confirmed.**
   - V 44 reads: a compact boxed sign, a horizontal running into a headed upright, then the pointed hatched lozenge, then a closed box with horizontals, then a gap, UN and ZI.
   - The lozenge is the KI of V 42 (KIŠ KI) and VI 8. The closed box is the EŠ₂ of VI 8 and VI 30.
   - VI 6 has the same two Akšak signs, then the lozenge KI, then GIŠ and KU as in V 42, and then hatching.
   - Langdon prints neither KI. Shipping it is right, and the notes say so.
2. **EŠ₂ after Unug{ki} in VI 23: confirmed.**
   - The line is NAM, LUGAL, BI, UNUG, KI, a closed box with horizontals, BA, DU.
   - The box has no triangular tail, so it is not the GA of VI 24 (unug{ki}-ga). It matches EŠ₂ in VI 8 and VI 30.
3. **Gimil in VI 9 and VI 13: refused** (see Changes, major).
4. **Ašdar in VI 17 as one unidentified sign x: accepted.**
   - The copy draws one large sign: a wedge at the left, a box with horizontals and two uprights on top. MU and TI follow, then MU, 1 u + 1 diš, NI and AK.
   - It is not the MUŠ₃ drawn in VI 12, and no other sign could be confirmed.
5. **Hatched signs bracketed: confirmed** (V 45 NI, VI 7 NAM, VI 12 UR, VI 13 dumu, VI 14 MU, VI 15 [zi-m]u, VI 16 U).
   - In each case the copy hatches the sign away, with at most an unidentifiable trace at the edge.
   - In V 45 the first corner-wedge of 30 stands at the edge of the break and AK is drawn at its far edge, so "30" is left unbracketed with a note. This is the same treatment as damaged-but-visible signs elsewhere.
6. **dé in VI 30 as one NE: accepted.**
   - The line is A, GA, then a box with a crossing touching a box of corner-wedges, then KI, EŠ₂, BA, DU.
   - The two parts touch and fit NE's box-and-wedges form. Taking them as one sign agrees with Langdon's single dé. The note flags the reading.
7. **{d}suen, {d}za-ba₄-ba₄, {d}šakkan₂ by sign: accepted.** These are readings by sign with Langdon's form in the notes and glosses, as the house rule ("ᵈBabbar → {d}utu") requires.
   - VI 12 shows AN, ZA, a boxed sign and the same boxed sign again at the line's end, which fits ZA.MUŠ₃.MUŠ₃.
   - VI 1 (GIR₃) is restored, so the usual spelling applies.
   - Note for signs.py: MUSH3's `values` list has no ba₄. That does not block the build. I did not add it.
8. **VI 21 total: the drafter is right.**
   - The copy has 8 uprights (four over four) = 8 geš = 480, then a corner wedge and an upright = 11, giving 491.
   - The reigns are 25 + 400 + 30 + 7 + 11 + 11 + 7 = 491, and there are seven names for "7 lugal".
   - Langdon's fn. 10 begins "The total is correct."
   - The listing of VI 21 in conventions.md among "totals that do not add up" is an error in conventions.md. It should be removed when the part is published. The note is accurate and was not changed.
   - Checked: the 97 2/3 of fn. 10 (491 − 400 + 6 2/3) and the 93 of the Akšak total (30 + 6 + 6 + 20 + 24 + 7).

### VI 1–5 against ur-i-awan IV 1–8

The units follow the same pattern: one unit per reign line, a two-line total, every word bracketed, and a note saying that the signs are the usual spelling and that the prism's own are lost. The one deviation was the unbracketed `lugal` in VI 4, now fixed. Langdon gives VI 1–5 with no "(?)", so shipping them as signs is right.

### Plate record, line by line

- V 44: Akšak (2 signs), KI, EŠ₂, UN, ZI.
- V 45: LUGAL, A AN, MU, u at the edge of the break, hatched, AK.
- V 46: UN DA LU LU, MU, 6 (3/3), NI AK.
- V 47: UR UR, MU, 6, NI AK. A ruling below.
- VI 1–5: "Lines 1–5 defaced".
- VI 6: Akšak (2), KI, GIŠ KU, hatched.
- VI 7: hatched, LUGAL, BI.
- VI 8: KIŠ KI EŠ₂, BA DU.
- VI 9: KIŠ KI, Gimil (long form), AN EN ZU.
- VI 10: TUR KU₃ AN BA U₂ KID.
- VI 11: LUGAL A AN, MU, 25, NI AK.
- VI 12: hatched + trace, AN ZA MUŠ₃ … MUŠ₃.
- VI 13: hatched, Gimil (long form), AN EN ZU KID.
- VI 14: hatched + trace, 6 geš, 4 u, NI AK.
- VI 15: hatched + trace, DAR RA, MU, 30, NI AK.
- VI 16: hatched (two horizontal traces), 3 signs (Langdon ṣi wa tar), MU, 7, NI AK.
- VI 17: x, MU TI, MU, 11, NI AK.
- VI 18: IŠ, trace, hatched, AN UD, MU, 11, NI AK.
- VI 19: NA AN NI IA AḪ, MU, 7, NI AK.
- VI 20: 7, LUGAL.
- VI 21: MU BI, 8 geš, u + diš, IB AK.
- VI 22: KIŠ KI GIŠ KU BA AN SIG₃.
- VI 23: NAM LUGAL BI UNUG KI EŠ₂ BA DU.
- VI 24: UNUG KI GA LUGAL ZAG GI SI.
- VI 25: LUGAL A AN, MU, 25, NI AK.
- VI 26: 1, LUGAL.
- VI 27: MU, 25, NI AK.
- VI 28: UNUG KI GIŠ KU BA AN SIG₃.
- VI 29: NAM LUGAL BI.
- VI 30: A GA NE (two parts) KI EŠ₂ BA DU.

All glyphs in units.json now agree with this record.
- Numerals:
  - The repeated U for 20/30 and FOUR U for 40 follow the published parts.
  - The `u` names are SIX/SEVEN/FIVE/FOUR/THREE DISH, SIX/EIGHT GESH2 and FOUR U.
  - The values are 30, 6, 6, [20], [24], [7], [93], 25, 400, 30, 7, 11, 11, 7, 491, 25, 25.
- The grammar labels (-še₃, -am₃, -bi, -ke₄ = gen. + erg., locative -ga, ba-an-sig₃, ba-ĝen, ni-ag / ib-ag) are right for the forms. `l` and `i` agree, and the house formulas are applied.

### Findings considered and refused

- **Bracket the "30" of V 45 (two of the three u are in the break)** · refused. One u is visible and Langdon prints the figure whole. As elsewhere, a damaged but partly visible form is noted, not bracketed, and the note says the figure is his.
- **Identify the VI 16 signs (ṣi, wa) independently** · refused. They cannot be confirmed from the copy. The note and the gloss already say the reading rests on Langdon's.
- **"Zababa, the god of Kish" (VI 12 note) as outside knowledge** · kept. It is the standard identification of the god's name, and the reading by sign is the house rule. Langdon's Ilbaba is given.
- **V 44 / VI 8 morph gloss for -šú carries the Mari broadening** · left for pass 2 and the glosser. It does not contradict the form.

### For the glosser / pass 2 / the owner

- Lemma removed: `x-šu-{d}suen`. Both occurrences now use the existing lemma `šu-{d}suen`, whose gloss is broadened to "… where the copy draws the first element in a long form unlike its usual ŠU, the identification is Langdon's and uncertain". gloss.json and new-lemmas.json still have `x-šu-{d}suen` and need to follow.
- The `in-ag` lemma string is unchanged, but its gloss is corrected: ì-n-aĝ₂, 3sg agent, "not itself plural". Any gloss.json entry calling it plural must change.
- conventions.md wrongly lists VI 21 among totals that do not add up.
- For the drafters of VII 20 and VII 45: the same long form of Gimil appears there. Treat it as here.
- For signs.py (not done): MUSH3 lacks the value ba₄, and KUSHU2's value list has only "akšak".
