## Pass 1

I read Plate II (langdon1923_0043.jpg) line by line for III 39–45 and IV 1–44 at 2–4× zoom, and compared III 7 for the mes sign. I also checked Langdon pp. 13–14 (langdon1923_0018–0019.jpg): transliteration, translation and footnotes. Edits were made by script (scratchpad reviewer/rev1.py), with the JSON loaded and dumped (indent 1, ensure_ascii=False, no trailing newline, as before), and no cuneiform was retyped. Afterwards: the JSON parses, every glyph sign is a key in signs-cuneiform.json, and every morph `g` covers its word's glyphs exactly once. Build not run.

### Changes

- IV 30 · morph (x-nun-na) · minor · The visible but unread first sign was glossed with its own morph `[…]` "a lost stretch of text", but the sign is not lost. Its glyph is now part of the name's morph (lemma x-nun-na, g [0,1,2]), as kish-i I 46 counts its gap glyph in the name. The note now says the sign is not lost, which is why it is unbracketed and shown as x, and that the LACUNA marker carries it only because no key exists for an unread visible sign.
- III 39 (III 39–41) · n · minor · "DUP also stands in Meskemgašer (Meskiaggasher, III 1)": in III 1 (and III 4) the mes is in the break. The visible instance is III 7 (Enmerkar's filiation), drawn the same as III 40/43. Also, "the copy draws a box with upright wedges, as he says" credited Langdon with a description he does not give. Both are reworded. Langdon's fn. 1 citation was missing and has been added: CT 12, 14a 18 = K. 10072, 4, DUP(me-iš) = iṭlu.
- IV 17 (IV 17–19) · n · minor · The note said the EŠ₂ of kiš{ki}-še₃ (IV 19) is "partly damaged". On the copy it is whole, and the hatching starts after it. The note now says the sign is clear.
- IV 39 (IV 39–40) · l · minor · "Hamazi: Hadanish, …" breaks the house literal for a city with no case-ending written. Compare kish-i I 43 "in-Kish," and this draft's IV 8 and IV 20. Now "in-Hamazi, Hadanish, …" (the `i` already reads "In Hamazi").
- IV 41 (IV 41–42) · l · minor · "1 king; its-years 6-sixties ruled." gave ib-ag no subject, unlike the morph gloss ('they ruled') and the other totals (IV 3, 15, 34; kish-i II 42; uruk-i III 35). Now "1 king; their-years 6-sixties they-ruled."
- about · minor · "Two totals do not match what survives — Ur's restored 177 against the 171 of other copies, and Kish's 3,195 against reigns that come far short of it" had two problems. Ur's 177 is wholly restored and equals the reigns as Langdon reads them. "Far short" also overstated the case while two Kish reigns are lost. Reworded with the figures: 177 = sum of reigns as read, against 171 in two other copies; 3,195 against 1,946 surviving, with two figures lost.
- IV 20 (IV 20–22) · l · style · "he-ruled" was unbracketed though ni-ag is wholly restored. Now "[he-ruled]", as the draft does in IV 12, 13, 24.
- IV 23 · l · style · Same issue: "[he-ruled]".
- IV 17 (IV 19) · l · style · "to-Kish went" was unbracketed though ba-ĝen is wholly restored. Now "to-Kish [went]".

Counts: 0 major, 6 minor, 3 style.

### Drafter's questions settled

- (a) III 40/42/43 mes: on the copy, the first sign of Mesannipadda (III 40, 43) and of Meskiaĝnanna (III 42) is a box with three upright wedges inside and a short horizontal at the left. Langdon (fn. 1) explicitly identifies it as DUP (REC 385), "not REC 363", and his cited gloss DUP(me-iš) = iṭlu supports the reading mes. **DUB is kept for this part.** The key's character is 𒁾 CUNEIFORM SIGN DUB, which is right for that identification. **Inconsistency, published file not edited:** king-list-uruk-i.json III 7 (en-me-kar dumu mes-ki-aĝ₂-…) ships MES (𒈩) for what the copy draws as the same sign. Its review (Pass 1) reads it "TUR MES KI". Langdon's fn. 1 ("Also in Meskemgašer the sign is DUP") applies to it. uruk-i III 1 and III 4 [mes] are restored, and MES there is only the restorer's choice. For the owner: either switch uruk-i III 1/4/7 to DUB, or note there that Langdon reads the sign as DUP.
- (b) IV 30 unread sign: kept as LACUNA with tr "x" and reading "x-nun-na" (unbracketed), with the morph fixed (above). Precedent: uruk-i III 31 and kish-i I 46 show an unread sign as "[…]". Those signs are damaged or hatched, while IV 30's is fully drawn (Langdon fn. 3 'PISAN + RU ?'), so a bracketed gap would falsely mark it as lost. **Unresolved, for the owner:** the LACUNA entry's name ("a lost stretch of text") still shows on the glyph. A marker key for a visible but unread sign (e.g. label "x") would be cleaner, added with signs.py. Not added in this pass.
- (c) Bracketing against Langdon's unbracketed print, checked on the copy:
  - **IV 14:** after MU and 3 u + 6 diš (units at the edge), the rest of the line is hatched, so [ni-ag] is right.
  - **IV 28:** NI is clear, then hatching to the line end, so ni-[ag] is right.
  - **IV 35:** IB is drawn half-hatched, then hatching, so ib-[ag] is right.
  - **IV 17:** GIŠ is only begun at the edge, KU and BA are hatched, and at the right are an upright wedge and a compact sign. {ĝeš}[tukul] [ba]-sig₃ is right.
  - **IV 29:** AK is drawn in part, so unbracketed and noted is right.
- (d) New signs:
  - **LAH4** (𒁻 DU OVER DU) at IV 20: the copy shows a boxed sign with stacked internal strokes, half in the break. The fit is possible but not sure. It is shipped as laḫ₄(?) and the note and gloss say so. Accepted. Langdon prints plain "Laḫ(?)" with no index, so LAḪ₄ is the drafter's identification, and the note does not claim it is Langdon's.
  - **UMUSH** (𒆂 KA TIMES SHID) at IV 29: the copy draws a tall box filled with horizontals, which does not look like a KA-form (compare KA in IV 26). The identification is Langdon's reading only, and the note says so. Accepted as flagged.

### Checked and confirmed (no change)

- **Coverage:** units III 39–41 | 42–45 | IV 1 | 2 | 3–4 | 5–7 | 8 | 9 (lost) | 10 | 11 (lost) | 12 | 13–14 | 15–16 | 17–19 | 20–22 | 23 | 24–25 | 26–28 | 29 | 30 | 31–32 | 33 | 34–35 | 36–38 | 39–40 | 41–42 | 43–44. Every line is present, in order, and no unit crosses a column. `nl` falls on the first word of each new prism line only.
- **Plate (line by line):**
  - III 39: ŠEŠ AB KI … MA. III 40: DUB AN NI PAD … DA. III 41: LUGAL A AN MU, 1 geš + 2 u, NI AK. III 42: DUB KI AĜ₂ AN ŠEŠ KI. III 43: TUR DUB AN NI PAD DA. III 44: LUGAL … A … AN. III 45: MU, 3 u + 6 diš, NI AK, with a ruling below.
  - IV 1–11: hatched. IV 12: MU + hatching. IV 13: KU + a half sign. IV 14: as above. IV 15: 3 diš, then hatching. IV 16: MU BI, 5 geš (3 over 2), a 'sic' tens group with one diš, then hatching.
  - IV 18: NAM LUGAL … BI. IV 19: KIŠ KI EŠ₂, gap, hatching. IV 21: LUGAL … A … AN. IV 22: MU, 3 geš, 2 u + one wedge, hatching.
  - IV 23: DA DA SIG MU, hatching. IV 24: MA₂ MA₂ GAL + a half-hatched sign. IV 25: MU, 6 diš, ŠU IGI, hatching. IV 26: KA AL BU, hatching. IV 27: TUR MA₂ GAL GAL + a trace.
  - IV 30: a complex sign, NUN NA MU, 3 geš, NI AK. IV 31: I BI ERASURE NI + a half sign. IV 32: MU, 4 geš, 5 u 'sic', NI AK. IV 33: LUGAL MU MU, 6 geš, NI AK. IV 34: 8 diš (4 over 4) LUGAL.
  - IV 36: KIŠ KI GIŠ KU BA AN + a compact sign. IV 37: NAM LUGAL … BI. IV 38: ḪA MA ZI KI EŠ₂ BA DU. IV 39: ḪA MA ZI (no KI) ḪA DA NI IŠ. IV 40: MU, 6 diš, ŠU IGI, NI AK. IV 41: 1 diš LUGAL. IV 42: MU BI, 6 diš, ŠU IGI, IB AK. IV 43: ḪA MA ZI KI GIŠ KU BA AN + a compact sign. IV 44: NAM LUGAL BI UNUG KI EŠ₂ BA DU.
- **Numerals:**
  - All `u` names resolve in Unicode, and repeated U glyphs are used where Unicode has no TWO/THREE U (as kish-i and uruk-i).
  - Values: 80, 36, [25], [36], [177] = 2 geš + 5 u + 7 diš, 36, 35[6], 201+…, 360 (6 šu-ši), 195 = 3 geš + u + 5 diš, 360 (6 geš), 180, 290 = 4 geš + 5 u, 360, 8, 3,195 = 5 geš'u + 3 geš + u + 5 diš, 360, 1, 360.
  - Sums: Ur 80+36+25+36 = 177 (with Poebel's 30, 171). Kish II reigns as read 201+?+?+360+195+360+180+290+360 = 1,946 + unknowns, with 3,195 − 1,946 = 1,249. Langdon's 3,600+180+12 = 3,792. All are reported, not corrected.
- **Footnotes:** pp. 13 fn. 1–8 and 14 fn. 1–8 are all reported in the notes (fn. 1 p. 13 is now complete). Fn. 4 p. 14's "The length of the second reign is missing here" is covered by the IV 34 note's treatment of Dadasig.
- **House formulas and renderings:** "In X, Y became king; he reigned N years", "N kings reigned M years" and "X was smitten with weapons; its kingship was carried to Y" are applied, and l/i match kish-i and uruk-i. Lemmas and glosses match the published parts except for the -ma item below. Grammar labels (locative -ma, -am₃, -še₃, ba-/ba-an-, -bi, ni-ag/ib-ag, possible -mu 'my') are right for the forms.

### Findings considered and refused

- Bracket the 6 in l "356" (IV 15) / mark "35[6]" in l · refused: uruk-i III 1 likewise leaves "325" plain in l while `reading` has 32[5]; the note gives the restoration.
- IV 24's fourth sign (visible, half-hatched) shown as "[…]" rather than "x" · refused: it is damaged at the edge of the break, and uruk-i III 31 shows such a sign as a gap; the note describes it.
- IV 5 l "Ur" for Langdon's restored urim₂{ki}-ma (with -ma) · refused: the note says the restoration with -ma is kept as printed; l follows Langdon's own 'Ur by weapons was smitten'.
- III 42 "'hero who loves Nanna'" as remembered English · refused: it is built from the sign values (mes = iṭlu per Langdon's fn. 1, ki-aĝ₂ 'love', Nanna) and given as an analysis, not a translation of record.

### For pass 2 / the owner

- Lemma "-ma": published kish-i glossary has "genitive -a(k) 'of', written -ma after a final m (elam{ki}-ma)"; this part uses -ma as locative (urim₂{ki}-ma 'in Ur'). gloss.json needs a broadening (e.g. "-a after a final m: genitive or locative"), not a second sense under the same key silently.
- uruk-i MES vs DUB (see (a)) and an unread-sign marker key (see (b)).
