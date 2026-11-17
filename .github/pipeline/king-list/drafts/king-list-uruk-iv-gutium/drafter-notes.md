# Drafter notes — king-list-uruk-iv-gutium (VII 15 – VIII 2)

30 units: 5 kings of Uruk IV, the Uruk total, the refrain to the Gutian horde (VII 24–26), the kingless line (VII 27–28), 20 Gutian reign units (VII 29 – VII 49, VII 45–46 as one), the Gutian total (VII 50–51), and the refrain back to Uruk (VIII 1–2, its own unit, Col. VIII).

## Signs needed (not in signs-cuneiform.json; units.json already uses these keys)
- `GIGIR` — CUNEIFORM SIGN LAGAB TIMES BAD (U+121C0). It is used in Ur-gigir (VII 17). Suggested entry: name "gigir (chariot)", type logogram, sound "gigir", values ["gigir — chariot", "in the royal name Ur-gigir (King List VII 17)"], label "GIGIR".
- `SHU2` — CUNEIFORM SIGN SHU2 (U+122D9). It is the last sign of In-ki-šu₂ (VII 30), Langdon's šù. Suggested entry: name "šu₂", type syllabogram, sound "šu₂", values ["šu₂ (Langdon šù)"], label "ŠU₂".
- `DUH` — CUNEIFORM SIGN DUH (U+12083), the DU₈ sign, read gab. It is used in Ni-kil-la-gab (VII 31) and Ia-ar-la-gab (VII 36). Suggested entry: name "gab, du₈ (open, loosen)", type syllabogram, sound "gab", values ["gab", "du₈"], label "DU₈".
- `DUN` — CUNEIFORM SIGN DUN (U+12084), read šul. It is used in Šul-me-e (VII 32). Suggested entry: name "šul, dun", type syllabogram, sound "šul", values ["šul (young man; in names, cf. Šulgi)", "dun"], label "DUN".

The test build swapped these four keys for nearest existing ones: GIGIR→LAGAB, SHU2→SHU, DUH→DU, DUN→DU. The result was BUILT and validate PASS. There was one WARN: three linecheck lines, all expected (see below). `signs.py check` reports the signs in sync. The build's side effects were then reverted: stories.json was checked out, and the generated king-list-uruk-iv-gutium.json was deleted. No glossary file changed, because the King List glossary is inline.

No new key is needed for -meš (VII 33). The copy draws ME followed by three corner-wedges, so it is shipped as ME (tr "meš") + ESZ (the existing "U-U-U, plural -me-eš" key, tr "").

## linecheck.md (three lines; all confirmed on the plate)
- VII 20: Gimil-ili → šu-i₃-li₂. Langdon's Gimil is read šu by sign (house rule). ili is NI NI on the copy.
- VII 21: Ur-ᵈBabbar → ur-{d}utu (UD, house rule).
- VII 51: the numeral notation (125 = 2 geš + 5 diš; 40 = 4 u) and ud → u₄.

## Plate (Pl. IV) vs Langdon, line by line
- **VII 15**: After UNUG KI the copy has **a box of horizontals with two upright heads**. It is drawn like the EŠ₂ of VIII 2 (and of VI 8, 23, 30) and unlike the GA of VII 47, which has a pointed wedge inside. Langdon prints only Unug-(ki).
  - Shipped as **unug{ki}-še₃**: `l` "to-Uruk (sic)", `i` "In Uruk", following the precedent of V 23 and V 44.
  - EŠ₂ vs GA is a reading of the copy. It is flagged as uncertain.
  - "nigin" is drawn as **a large pointed head joined to a box of horizontals**, not a plain LAGAB box. It is shipped as LAGAB (nigin) after Langdon and flagged. VII 17 has the same form.
- **VII 16**: These signs agree with Langdon. 7 is drawn four over three.
- **VII 17**: gigir is drawn wide, as a plain box followed by a box with a diagonal. It is taken as one LAGAB×BAD after Langdon and flagged. -ge → -ke₄ (KID).
- **VII 18**: These signs agree with Langdon.
- **VII 19**: Langdon prints "Kudda" as one word. **The copy has two signs.** The first is a horizontal crossed by an upright and a diagonal, taken as TAR and read kud. The second is DA. Shipped as **kud-da**. The TAR identification is uncertain.
- **VII 20**: Langdon's Gimil is in the long two-part form, the same as in VI 9, VI 13 and VII 45. It is kept as ŠU and flagged (house rule). ili = **NI NI**, i₃-li₂. The rest agrees with Langdon.
- **VII 21–23**: These lines agree with Langdon. VII 22: 5 is three over two. VII 23: 30 is 3 u.
- **VII 24**: **Langdon's "ka-" is a misprint.** The copy draws the small box with an inner diagonal, the same BA as in VII 26 ba-gín. Shipped as ba-an-sig₃. GIŠ and KU are as Langdon reads them. The KU of {ĝeš}tukul is drawn as a small box with an inner wedge.
- **VII 25**: This line agrees with Langdon.
- **VII 26 and VII 27**:
  - The copy has **one more sign than Langdon reads**, at the same place in both lines. The order on the copy is KI, KAL(?), BAD(?), GU, TU, then a cluster of corner-wedges joined to a box of horizontals, then UM, then BA DU in VII 26 and KI in VII 27. UM is the box-with-uprights of VII 39, 41, 42 and 43.
  - The extra sign is shipped as a visible, unread **x inside the name** (house rule): gu-tu-x-um. The lemma is kept as gu-tu-um. Whether it belongs to ugnim or to the name is not settled.
  - ugnim is drawn as three separate signs. KI.KAL.BAD is the packet's identification after Langdon's reading. Signs 2 and 3 are uncertain.
  - VII 26 has no -še₃ (Langdon fn. 6: S. has -šú). VII 27 has KI, as Langdon.
- **VII 28**: These signs agree with Langdon (LUGAL MU NU TUK).
- **VII 29–35**: These signs agree with Langdon.
  - VII 30: šù is a small sign, a corner-wedge with a tail. It is shipped as ŠU₂ (šu₂) after Langdon. The identification is uncertain.
  - VII 31: kil is a plain box, so LAGAB is given Langdon's value kil, flagged. gab = DU₈.
  - VII 33: ME and three corner-wedges, i.e. -meš.
  - VII 35: GI and EŠ run together on the copy.
- **VII 36**: These signs agree with Langdon. 15 = 1 u + 5 diš.
- **VII 37–39**: These lines agree with Langdon.
- **VII 40–41**: The starts of these lines are hatched. NE and RA stand at the edge of the break. Both agree with Langdon.
- **VII 42–44**: These lines agree with Langdon.
- **VII 45**: The long-form Gimil is the same as in VII 20, kept as ŠU and flagged. Then AN EN ZU TUR ḪA AB LUM. There is **no -ke₄** after Hablum, as Langdon prints.
- **VII 46**: This line agrees with Langdon.
- **VII 47**: IA is in the hatching ([ia], as Langdon). AR stands at the edge of the break and is unbracketed.
- **VII 48**: The name is lost. A trace touches MU at the edge of the break.
- **VII 49**: Ti-ri is hatched ([ti-ri], as Langdon). GA survives only in its right part and is unbracketed. **ud 40 is kept as days** (u₄; 40 = 4 u). NI is drawn wide.
- **VII 50**: The 21 is partly in a hatched patch, with one corner-wedge and one upright clear. It is shipped as Langdon's 21, unbracketed (house rule: a wedge survives).
- **VII 51**: mu-bi 125 is in the break and shipped bracketed, Langdon's restoration from P. No. 2. UD stands at the edge. 40, IB and AK are clear.
- **VIII 1**: **GU is clear and TU is at the edge of the break.** Langdon brackets the whole name, but here gu-tu is unbracketed. [um{ki} {ĝeš}tukul ba-an-sig₃] is restored.
- **VIII 2**: nam-lugal-bi unug{ki}-še₃ is clear. [ba-ĝen] is restored.

## Totals
- **VII 22–23 (Uruk IV)**: 7 + 6 + 6 + 5 + 6 = 30, with five names. The total is correct. Langdon fn. 5 says Scheil has 26.
- **VII 50 (21 kings)**: there are 20 names, VII 29–49, one of them lost (VII 48). Langdon counts the kingless time of VII 27–28 as one king.
- **VII 51 (years)**: the reigns on the prism add up to 3+6+6+6+6+5+6+15+3+3+1+3+2+2+1+2+7+7+7 = **91 years**, plus 40 days.
  - Langdon says "the actual total is only 86 years". That does not match this sum. It is reported as his in the note and not resolved.
  - The restored 125 comes from P. No. 2. L. No. 1 has 124 years and 40 days.
  - Nothing is corrected.

## Uncertain readings (all flagged in the notes)
- VII 15: EŠ₂ vs GA after Unug{ki}.
- VII 15 and 17: nigin (LAGAB); the drawn form is not a plain box.
- VII 17: gigir; the sign is drawn wide.
- VII 19: TAR = kud.
- VII 20 and 45: the long-form Gimil = ŠU.
- VII 26, 27, VIII 1: the signs of ugnim; the unread x in Gutium.
- VII 28: lugal-mu. Langdon reads mu as "by name". It is kept with a query in `l` and `i`.
- VII 30: šu₂.
- VII 31: kil on LAGAB.
- VII 33: -meš, kept as written; its sense after one name is unclear.
- VII 38: Langdon's "Jarla(gaš)" is not supplied.

## House renderings proposed
- The refrain to a people rather than a city (VII 24–26): `l` "its-kingship (to) the-horde of-Gutium went", `i` "its kingship was carried to the horde of Gutium". Neither 'to' nor 'of' is written.
- VII 27–28 ugnim gu-tu-um{ki} lugal-mu nu-tuk: `l` "The-horde of-Gutium a-king by-name(?) not-had.", `i` "The horde of Gutium had no king by name (?)."
- A Gutian king with lugal-am₃ but no city (VII 29): "Imta became king; he reigned 3 years."
- u₄ N in a reign (VII 49): `l` "days 40 he-ruled", `i` "reigned 40 days". In a total: "reigned [125 years] and 40 days".
- English names (š→sh, i̯a→Y as in Nanniyah):
  - Uruk: Ur-nigin, Ur-gigir, Kudda, Shu-ili, Ur-Utu.
  - Gutium: Imta, Inkishu, Nikillagab, Shulme, Elulumesh (`l` Elulu-mesh), Inimabakesh, Igeshaush, Yarlagab, Ibate, Yarla, Kurum, […]-nedin, […]-rabum, Irarum, Ibranum, Hablum, Shu-Suen, Yarlaganda, Tiriga; Gutium for the land.

## Glossary notes for the glosser
- Existing lemmas whose published gloss needs broadening (units.json carries the proposed broadened text in morph):
  - `e-lu-lu`: also a Gutian king (VII 33, with -meš).
  - `šu-{d}suen`: also a Gutian king, son of Hablum (VII 45).
  - `mu`: also "name" in lugal-mu nu-tuk (VII 28), which is uncertain. The morph carries the broadened text, but the build's story glossary still shows "year(s)" until gloss.json broadens it.
- The 27 new lemmas are in new-lemmas.json.
