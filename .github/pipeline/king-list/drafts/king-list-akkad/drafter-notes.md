# Drafter notes — king-list-akkad (VI 31 – VII 14)

## Signs needed (not in signs-cuneiform.json; units.json already uses these keys)
- `DUG` — CUNEIFORM SIGN DUG (U+12081). Third sign of SAG.ŠU.DUG = sagi "cup-bearer" (VI 33). Suggested entry: name "dug (jar); in SAG.ŠU.DUG = sagi 'cup-bearer'", type logogram, values ["dug — jar, pot", "third sign of sagi (SAG.ŠU.DUG) 'cup-bearer'"], label "DUG".
- `DUR` — CUNEIFORM SIGN GU2 TIMES KAK (U+12119), the sign read dur ("bond"). Only in Langdon's restoration [Gimil-dur-ūl] (VII 9). The packet's first pass suggested GU2 TIMES NUN; GU₂×KAK is the sign usually given the value dur in the sign lists. Please confirm this before you add it. Suggested label "DUR".

The build with these two keys swapped for existing ones (KA, DU) gave BUILT and validate PASS. There were two WARNs: the unit 0 note is long, and one linecheck line (VI 33 sagi / Langdon ka-šu-duĝ, expected). The files it wrote were reverted.

## Plate vs Langdon, line by line (Pl. III, Pl. IV)
- **VI 31**: A GA NE, then ŠAR RU KI IN, 7 signs, as Langdon. There is no KI after Agade. NE here is a single box with a crossing, and the box of corner-wedges that follows is ŠAR: the same sequence is in VI 37 and VI 41 (dumu ŠAR RU KI IN).
  **Check for the previous part:** VI 30 (published) treats "box with crossing + box of corner-wedges" as one wide NE. Given VI 31, VI 34 and VII 13, where NE is the crossed box alone, the reviewer of VI 30 may want another look. I have not changed anything there.
- **VI 32**: NI LU BA NI + NU GIŠ SAR, as Langdon (-ì-lu-ba-ni nu-giš-šar). The copy draws a dotted outline (damaged surface) round NI and LU. They are not drawn like the AB-BA of III 18 (ab-ba-ni), so Langdon's reading is kept and flagged as uncertain. nu-giš-šar is read nu-{ĝeš}kiri₆ by sign (GIŠ.SAR = kiri₆).
- **VI 33**: The first sign is a pointed head with one upright and no inner strokes. It is unlike the KA of II 10 (a box of horizontals), so it is taken as **SAG**: SAG.ŠU.DUG = **sagi**. Langdon reads ka-šu-duĝ. This is a decision from the drawing and it is uncertain.
  In Ur-ᵈIl-ba-ba the copy draws UR AN ZA, then **a single upright marked "sic!"**, then MUŠ₃ MUŠ₃. Langdon does not read the upright. It is shipped as a DISH glyph, role punct, tr "(sic)", lemma "(sic)". The reading is ur-{d}za-(sic)-ba₄-ba₄.
- **VI 34**: The copy has 8 signs where Langdon prints 10:
  - LUGAL, **A (marked "sic!")**, NE: a-de₃, with no GA and no KI.
  - then a sign with a "?" drawn in it, read lu₂ after Langdon's galu;
  - then A GA NE KI.
  Langdon prints "A-ga-de (ki)" for the first. The plate is followed: reading `a-de₃`, `lu₂(?)`. The `l` has "of-A(ga)de (sic)".
- **VI 35–36**: These lines agree with Langdon. 56 = 5 u + 6 diš.
- **VI 37–41**: These lines agree with Langdon. VI 40 ri-mu-šu-uš is kept as written (his fn. 4 "Sic!").
- **VI 42**: mu 15 is clear. **NI AK are hatched, with traces**. Langdon prints them unbracketed; here they are [ni-ag].
- **VI 43**: NA RA AM, then the break, with a trace at the far right.
- **VI 44**: dumu MA, then the break.
- **VI 45**: MU only. The number is a LACUNA glyph (Langdon "38 (?)").
- **VI 46**: Only the left part of ŠAR survives (Langdon "Ša[r").
- **VI 47–48**: Wholly hatched. VI 48's number is a LACUNA glyph (Langdon "24 (?)").
- **VII 1**: The first half is hatched. Then A (at the edge of the break), BA, A.AN, NU, LUGAL, as Langdon.
- **VII 2**: At the edge of the break the copy shows a boxed sign with uprights, two uprights and a slanting sign. Langdon reads all this as one gí (GI₄). That is kept, and the note says it is not certain.
- **VII 3–5**: Only LUGAL is visible. The names are restored by Langdon.
- **VII 6**: **No figure is drawn.** The line is hatched to the middle and then shows LUGAL. Langdon prints 4 unbracketed; here it is [4].
- **VII 7**: IB AK are clear; [mu 3] is restored.
- **VII 8**: **MU is in the break** (Langdon prints it unbracketed), so it is [mu]. Of the 21, the first u is a trace at the edge of the break; it is not bracketed (house rule: a figure of which a wedge survives).
- **VII 9–10**: dumu DU DU KID are clear. The name is restored. [mu] 15 ni-ag.
- **VII 11–12**: These lines are clear. 11 = u + diš. 181 = 3 geš + 1 diš (Langdon "180 + 1").
- **VII 13–14**: These lines are clear. NE is a single crossed box. Langdon's "bagín" = BA DU.

## Totals
- **VII 12** cannot be checked. The surviving reigns make 56 + 9 + 15 + 3 + 21 + 15 = 119, and Naram-Suen and Shargalisharri are lost. Langdon's 38 and 24 are reckoned back from 181 (his fn. 3). The variants' 197 is reported. Nothing is corrected.
- **VII 6–7**: 4 kings, 3 years (restored figure). There are no reigns to add.

## Uncertain readings
- VI 31–32: the name. Langdon reads Šar-ru-ki-in-ì-lu-ba-ni as one name. NI and LU are damaged on the copy.
- VI 33: SAG (vs Langdon's KA) in sagi. The stray upright marked "sic!".
- VI 34: lu₂(?), from the "?" on the copy.
- VII 2: whether the visible signs are one GI₄.
- VII 9: the whole name is restored. KIB is read ul after Scheil and given as ulₓ. DUR is a sign identification for a restored value.

## New house renderings (proposed)
- City at a dynasty's head with no case-ending and no KI (a-ga-de₃, VI 31): literal "in-Agade,", English "In Agade, …".
- šar-ru-ki-in: `l` "Sharrukin", `i` "Sargon". The first entry, VI 31–32, has Langdon's long name "Sharrukin-ilubani (Sargon)".
- English names:
  - Rimush; Manishtishu; Naram-Suen (ᵈEn-zu → {d}suen, as Shu-Suen); Shargalisharri (Langdon's ga kept); Igigi; Imi; Nani; Elulu; Dudu.
  - Shu-Durul: Gimil → šu per conventions. KIB is given as ulₓ.
- nu-giš-šar → nu-{ĝeš}kiri₆, "gardener".
- ka-šu-duĝ → sagi (SAG.ŠU.DUG), "cup-bearer of X" (genitive unwritten).
- šeš-gal → "elder brother".
- lugal a-ga-de₃ lu₂ a-ga-de₃{ki} mu-un-du₃-a → "the king of Agade, the one who built Agade" (as Uruk-I III 7).
- **VII 1** a-ba-am₃ lugal a-ba-am₃ nu lugal:
  - `l` "[who-was king]? who-was not king?"
  - `i` "Who was king? Who was not king?"
- "X lugal" list entries (VII 2–5), name + lugal with no copula:
  - `l` "X, king."
  - `i` "X was king."
- "N lugal / mu N ib-ag" (VII 6–7): "Four kings reigned 3 years" (the house total formula).
- A stray wedge marked "sic!" on the copy: DISH glyph, role punct, tr "(sic)", lemma "(sic)".
- Agade written without GA: reading `a-de₃`, lemma a-ga-de₃; `l` "A(ga)de (sic)".

## Glossary notes for the glosser
- Existing lemmas whose published gloss needs broadening (units.json carries the proposed broadened text in morph):
  - `e-lu-lu`: also the king of Agade (VII 5).
  - `ur-{d}za-ba₄-ba₄`: VI 33, where the name is clear. The published gloss says "UR lies in a break", which is true only of VI 12.
  - `a-ga-de₃`: written without GA or KI.
- New lemmas (glosses in morph):
  - šar-ru-ki-in-i₃-lu-ba-ni, šar-ru-ki-in, nu-{ĝeš}kiri₆, sagi
  - ri-mu-uš, ri-mu-šu-uš, ma-ni-iš-ti-iš-šu, šeš-gal
  - na-ra-am-{d}suen, šar-ga-li₂-šar-ri
  - a-ba, nu
  - i-gi₄-gi₄, i-mi, na-ni, du-du, šu-dur-ulₓ
  - (sic), 11
