# Drafter notes — king-list-uruk-v-ur-iii-isin (VIII 3 – VIII 46)

26 units, covering VIII 3–46 in order, all in Col. VIII:
- Uruk V: Utuhegal (VIII 3–4), the total (5–6), the refrain to Ur (7–8).
- Ur III: Ur-Namma (9–10), Shulgi (11–12), Amar-Suen (13–14), Shu-Suen (15–16), Ibi-Suen (17–18), the total (19–20), the refrain to Isin (21–22).
- Isin: Ishbi-Erra (23–24), Shu-ilishu (25–26), Idin-Dagan (27–28), Ishme-Dagan (29–30), Lipit-Ashdar (31–32), Ur-Ninurta (33, one line), Bur-Suen (34–35), Lipit-Enlil (36–37), Erra-imiti (38), Enlil-bani (39), Zambiya (40), Iterpisha (41), Ur-dukuga (42), Suen-magir (43); VIII 38–43 are one line each. The total is VIII 44–45.
- The colophon (VIII 46) is its own unit. Its note says it is the scribe's signature, not a King List entry.

I checked the file in memory with hooks.assemble + hooks.validate. No story, glossary or manifest was written. The result was no errors and one WARN, five linecheck lines, all expected:
- VIII 13, 15, 17 differ by the by-sign readings amar/suen/šul/šu/bi₂.
- VIII 20 and 45 differ only in numeral notation.

## New signs needed: none
Every key used is already in signs-cuneiform.json. it = A2 (𒀉, whose values already list id/it), er₃ = ARAD, urta = IB, namma = ENGUR, šul = DUN, pi₄ = KA, gir₂ = GIR2, ur₂ = UR2, šubur = SHUBUR, du₃ = KAK, ku₃ = KU3. Some entries lack the value used here; signs.py cannot add values (QUESTIONS 2026-11-16). These are left for the owner:
- ARAD er₃
- IB urta
- ENGUR namma
- KA pi₄
- NE bi₂
- BUR in Bur-Suen
- DI ṭe
- GAN ḫe₂ (it lists ḫé)
- IG ĝal₂

## Plate (Pl. IV, Col. VIII) vs Langdon
**Signs Langdon prints unbracketed that are hatched away on the copy.** These are bracketed under the house rule:
- VIII 5: lugal.
- VIII 6: ud (u₄), together with his [ni-ag].
- VIII 9: ᵈNammu, which is clear in VIII 11. UR and LUGAL are clear.
- VIII 10: ni-, written [ni]-ag. AK is clear.
- VIII 28: ni-ag. MU and 21 are clear.
- VIII 33: ᵈNinurta. His fn. 13 says it is "partially preserved", but nothing of it is drawn after UR.

**Signs Langdon restores that survive on the copy:**
- VIII 8: the final DU (ĝen) of ba-gín stands clear beyond the break. Its form is identical to the DU at the end of VIII 22. Shipped as urim₂[{ki}-ma-še₃ ba]-ĝen. ŠEŠ is at the break edge.

**A sign Langdon does not print:**
- VIII 34: beyond the break at the line end there is a box with horizontals and upright heads. It matches the KID at the end of VIII 13, 17 and 36.
- Shipped as [dumu {d}ur-{d}nin-urta]-ke₄. The identification is flagged.

**A sign in Langdon's print that is not on the copy:**
- VIII 17: Langdon has "Gimil-ᵈSina-ge", but the copy has no sign between ZU and KID. Shipped as šu-{d}suen-ke₄.

**Two different signs for Langdon's one "Bur":**
- VIII 13 and 15 (Ur III) draw an open box with a diamond, AMAR.
- VIII 34 and 37 (Isin) draw a closed box with inner wedges, taken as BUR.
- Shipped as {d}amar-{d}suen for Ur III and {d}bur-{d}suen for Isin. BUR is flagged.

**Lines that agree with Langdon:**
- VIII 3: the GAN and IG of ḫe₂-ĝal₂ are at the edge of the break. They are unbracketed, as Langdon prints them.
- VIII 31: AN and LI are damaged at the edge of the hatching. They are unbracketed, as Langdon prints them.
- VIII 35: 21 is partly in a hatched patch, but a corner-wedge and an upright survive. It is unbracketed, with Langdon's value.

**Signs that are present where Langdon also has them:**
- VIII 23: there is no AN before Gir* (Erra).
- VIII 27: there is no AN before Gimil-ili-šu.
- VIII 37: there is no AN before Bur.

**Langdon's corrections are in the notes; the prism's figures are shipped:**
- VIII 18: the prism has 24; Langdon prints "(26)".
- VIII 19: the prism has 4 kings; Langdon prints "5".
- VIII 26: the prism has 20; Langdon prints "(10)", and his translation reverses it as "10 (20)".

**Totals reported and not corrected:**
- VIII 20: 108 is written, but the reigns add to 106 (fn. 5). Five kings are named and the prism counts 4.
- VIII 45: 203 is written, but the reigns add to 213. That 213 includes the restored 20, 11 and 28. With 10 in VIII 26 the sum would be 203 (fn. 6, fn. 9).

## Readings and decisions
- **VIII 4 and 6, "mu 7 šu-ši 7 ud"**:
  - Shipped as mu 7 šu-ši 7 u₄. `l` is "years 7 (and) a-sixth (?), days 7"; `i` is "7⅙ (?) years and 7 days", following Langdon (fn. 7: šuš is used for 60 and for 1/6).
  - The note gives the alternative by the prism's own usage: N šu-ši = N × 60, which would make "7 šu-ši" 420. The šu-ši lemma gloss is broadened to say this.
  - This is uncertain.
- **ᵈDungi** → {d}šul-gi (DUN.GI), Shulgi.
- **ᵈBur-ᵈSin (Ur III)** → {d}amar-{d}suen (AMAR), Amar-Suen.
- **Gimil-ᵈSin** → šu-{d}suen. ŠU is compact here, not the long form.
- **I-be-ᵈSin** → i-bi₂-{d}suen. The second sign is a box with crossing wedges, so NE and not BAD. Flagged. English Ibi-Suen.
- **Ur-ᵈNammu** → ur-{d}namma (ENGUR, clear in VIII 11), English Ur-Namma. In VIII 11 both father and son carry the dingir.
- **Iš-bi-Gir\*-ra** → iš-bi-er₃-ra with ARAD. The drawn sign is a horizontal with slanting wedges and uprights. Flagged. English Ishbi-Erra. The same sign gives {d}er₃-ra-i-mi-ti, Erra-imiti.
- **ᵈGimil-ì-lí-šu** → {d}šu-i₃-li₂-šu, Shu-ilishu.
- **ᵈNinurta** → {d}nin-urta, NIN + IB read urta (restored).
- **ᵈLi-[bi-it-Ašdar]**:
  - Shipped as {d}li-[bi-it-…]: [bi-it] as BI + A2, and Ašdar as one LACUNA glyph.
  - The reason is that Ištar's writing cannot be checked here; in VI 17 Langdon's Ašdar is an unidentified sign.
  - The lemma is li-bi-it-ašdar and the English is Lipit-Ashdar (Langdon's).
  - This departs from "ship Langdon's restorations as signs" for that one element. The reviewer may prefer MUSH3 ({d}INANNA) or eš₄-tar₂.
- **ᵈLi-bi-[it-ᵈ]En-lil** → {d}li-bi-[it-{d}]en-lil₂, English Lipit-Enlil. BI is read bi, and "Lipit" is Langdon's English (Akkadian lipit).
- **ᵈI-ṭe-ir-pî-ša** → {d}i-ṭe-er-pi₄-ša. DI is read ṭe; it is not the TE of VII 37. IR is read er. KA is read pi₄ (Langdon fn. 4: KA). DI and KA are flagged. English Iterpisha.
- **ᵈUr-dù-kug-ga** → {d}ur-du₃-ku₃-ga, with KAK after Langdon. The copy does not settle KAK vs DU₆. Flagged. English Ur-dukuga.
- **ᵈSin-ma-gir** → {d}suen-ma-gir₂ (GIR2). Flagged. English Suen-magir.
- **ᵈZa-am-bi-i̯a** → {d}za-am-bi-ia, Zambiya.
- **Ì-si-in(ki)** → i₃-si-in{ki} (NI); -na is the locative, so "In Isin".
- **ᵈUtu-ĝe-gál** → {d}utu-ḫe₂-ĝal₂ (GAN, IG), Utuhegal.
- **kat** → šu (ŠU) "hand"; the colophon is "By the hand of Nur-Ninshubur". **Nu-ùr-ᵈNin-subur** → nu-ur₂-{d}nin-šubur.

## House renderings proposed
- "urim₂{ki}-ma / i₃-si-in{ki}-na X lugal" (no -am₃) → `l` "in-Ur, X king", `i` "In Ur, X was king; he reigned N years", as Akkad's "X lugal".
- urim₂{ki}-ma in the smitten-refrain (VIII 21) → `l` "Ur(-ma) with-weapons was-smitten", `i` as the formula.
- A name and reign on one line → `l` "X, years N he-ruled", `i` "X reigned N years".
- Reign with šu-ši as a fraction (Langdon) → "7⅙ (?) years and 7 days".
- Colophon šu PN → `l` "hand (of) PN", `i` "By the hand of PN".
- English names: Utuhegal, Ur-Namma, Shulgi, Amar-Suen, Shu-Suen, Ibi-Suen, Ishbi-Erra, Shu-ilishu, Idin-Dagan, Ishme-Dagan, Lipit-Ashdar, Ur-Ninurta, Bur-Suen, Lipit-Enlil, Erra-imiti, Enlil-bani, Zambiya, Iterpisha, Ur-dukuga, Suen-magir, Nur-Ninshubur; Isin.

## For the glosser
- There are 23 new lemmas. Each has a full gloss in its morph in units.json; the glosser can copy them:
  - 14, šu, utu-ḫe₂-ĝal₂, ur-{d}namma, šul-gi, amar-{d}suen, i-bi₂-{d}suen, i₃-si-in, iš-bi-er₃-ra, šu-i₃-li₂-šu
  - i-din-{d}da-gan, iš-me-{d}da-gan, li-bi-it-ašdar, ur-{d}nin-urta, bur-{d}suen, li-bi-it-{d}en-lil₂
  - er₃-ra-i-mi-ti, en-lil₂-ba-ni, za-am-bi-ia, i-ṭe-er-pi₄-ša, ur-du₃-ku₃-ga, suen-ma-gir₂, nu-ur₂-{d}nin-šubur
- Four existing lemmas need broadening (the morph carries "old · new"):
  - `šu-ši`: Langdon's 1/6.
  - `-ma`: before -še₃, and in the refrain.
  - `-na`: locative after the final n of Isin.
  - `šu-{d}suen`: the Ur III king.
