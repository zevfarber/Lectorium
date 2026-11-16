# The Sumerian King List — conventions (Run 3)

Distilled from the project's `sumerian-conventions.md` (2026-07-14), the Hammurabi display decisions where they
are general to cuneiform, and the published pilot `king-list-antediluvian.json` (Col. I 1–41), the model.

## Source and the sole-source rule
- S. Langdon, *Oxford Editions of Cuneiform Texts II* (Oxford 1923) — the Weld-Blundell Prism (WB 444):
  transliteration pp. 8–21, autograph Plates I–IV. Public domain. Langdon's transliteration of every line of
  Cols. I–VIII was transcribed from the page images on 2026-10-12 (`source/langdon-translit.json`, 370 entries,
  with Langdon's restorations, damage and footnote remarks per line); page images in `source/pages/`
  (transliteration pp. 8–21 = langdon1923_0013–0026.jpg; Plates I–IV = langdon1923_0042–0045.jpg).
- PD aids: Prince, *Materials for a Sumerian Lexicon* (1908); Delitzsch, *Sumerisches Glossar* (1914); Deimel's
  sign list. Modern sign lists (Borger's MZL, Labat) may be consulted silently to identify a sign on the plate — sign pages only, never an edition's translation or running text.
- Readings are 1923-vintage: keep Langdon's reading as the base, flag the modern understanding in the note.

## Data model (as the pilot; see also ../hammurabi/conventions.md for the glyph contract)
Unit `{ln, col, line, t, l, i, n, words[]}`; `ln` = the prism line (`numbering: "line"`), `col` = the column
(I–VIII); units never cross a column. `t` is built from the words. Glyph (drafter): `{sign, role, tr, val?, nl?,
u?}` — `sign` a key in `signs-cuneiform.json` (shared with Hammurabi; add new ones with run3/signs.py), roles
log/phon/det/comp/num; numerals with real sexagesimal signs (ŠAR₂ 3600, ŠAR'U 36000 …): the numeral sign whose
character varies with its count gives `u` = the Unicode name (e.g. "CUNEIFORM NUMERIC SIGN EIGHT SHAR2").
`reading` academic (modern subscript indices, determinatives in braces, hyphen-joined); `say` readable.
Langdon's accents are NOT converted by arithmetic: map each value by its sign (his dé is NE, de₃).

## Lines and damage
- Langdon's restorations [ ] are kept in `reading` (brackets) and their glyphs shipped; the note says what is
  restored. A wholly lost line is a gap unit `{"lost": true, …}` with one LACUNA glyph (if it is not already in signs-cuneiform.json, add it once with signs.py:
  `add cuneiform LACUNA 'WHITE SQUARE WITH ROUNDED CORNERS' '{"name": "a lost stretch of text", "type": "marker",
  "sound": null, "determines": null, "values": [], "label": "[…]"}'`). Col. V 1–10 is one lost entry.
- Langdon's printed misprints (IV 6 mam-lugal-bi; V 21, VII 24 ka-an-sīg; VII 14 bagín; V 16 -šú-ba-gín): the
  plate decides the sign; `reading` follows the plate; the note says what Langdon prints.
- His parenthesized corrections in VIII 18, 19, 26 and the IV 48 480/420 discrepancy go in the notes; `t` and
  `reading` follow the prism. Totals that do not add up (II 43, IV 35, VI 21, VII 12, VII 51, VIII 20, VIII 45)
  are reported in the notes, not corrected.

## Translation and notes
House rendering: nam-lugal an-ta e₁₁-de₃-a-ba → "When kingship came down from heaven". The formulae get fixed
English (decide on first use and record): "In X, Y became king; he reigned N years"; "N kings reigned M years";
"X was smitten with weapons; its kingship was carried to Y". Numbers: show the numeral signs and the value; the
value is interpretive. Honesty as in the pilot's `about`.

## Pronunciation and audio
Conventional reconstructed Sumerian. `langCode: null`. No voice chosen; parts publish without audio.

## Decisions taken while setting up Run 3 (2026-10-12; in QUESTIONS.md)
- Parts at the list's own seams (8 parts, I 42 – VIII 46; see plan.md).
- Differences between Langdon and the published Col. I (e.g. line 5 Á-la(l)-gar, 25/30 Zimbar, the e₃ sign E vs
  UD.DU, restored [nam-] and [Eri]du unmarked) are listed in QUESTIONS.md for the owner; the published part is
  not changed by the run.
- The sign inventory in `source/sign-inventory.json` is a first pass from Langdon's readings, not plate-verified:
  the drafter confirms every sign on the plate.

## House renderings settled in king-list-kish-i (2026-11-16)
- Formulas as above, applied: "In X, Y became king; he reigned N years"; total "N kings reigned M years"; "X was smitten with weapons; its kingship was carried to Y".
- Readings by sign, Langdon's form in the note: -šú → -še₃ (lemma kept `-šú`), ba-gín → ba-ĝen (lemma kept `ba-gín`), ĕ → e₃ (UD.DU), sib → sipa (PA.LU), galu → lu₂, ᵍⁱˢku → {ĝeš}tukul, -ge → -ke₄ (KID), ita → iti, ud → u₄; sīg/sig → sig₃ (PA.GAN₂, flagged: the copy draws one compact sign).
- Lost line = one unit per prism line, one LACUNA glyph (role punct, tr "[…]"); doubtful restorations of Langdon's (with his own ?) are not shipped as signs.
- Numerals shown as written (geš'u/geš/u/diš clusters); `reading` = the value; the note gives the composition.

## House renderings settled in king-list-uruk-i (2026-11-16)
- e₂-an-na-ka (column-end line) → "In Eanna"; en-am₃ … lugal-am₃ → "was lord and became king"; lu₂ X mu-un-du₃-a → "the one who built X"; verbless clauses ("his city (was) …", "his father (was) …") → "whose city was …", "whose father was …".
- Readings by sign, Langdon's form in the note: em/aga → aĝ₂ (AĜ₂); ᵈBabbar → {d}utu; tur 'enter' → ku₄ (TU); ĝar-sag → ḫur-saĝ (plate: ḪUR); dū → du₃ (KAK); Uri → urim₂; Kullab → kul-aba₄; eri → uru; bûr → a.
- Phonetic complements such as Lugal-banda(da) → glyph role `comp`, reading in braces. Divine names: {d} its own morph, the name lemma without it.
- Damaged-but-visible signs Langdon leaves unbracketed: noted only; bracketed where the copy hatches them away entirely.

## House renderings settled in king-list-ur-i-awan-kish-ii-hamazi (2026-11-16)
- urim₂{ki}-ma → "In Ur" (-ma = locative -a after final m); city with no case ending (ḫa-ma-zi, IV 39) → literal "in-Hamazi," and, with no lugal-am₃, "In Hamazi, Hadanish reigned N years".
- One-king total: "1 king; their-years N they-ruled" → "One king reigned N years".
- Readings by sign: Langdon's Mes (fn. DUP) → DUB, tr mes; Mes-ki-em-ᵈNannar → mes-ki-aĝ₂-{d}nanna; Ḫa-ma-ṣi → ḫa-ma-zi (ZI); A-wa-an → a-wa-an{ki} (PI = wa). English names write š as sh (Hadanish, Umushe).
- A visible but unread sign: LACUNA glyph with tr "x", unbracketed, inside the name's morph; the note says it is not lost.
- Damaged forms Langdon prints unbracketed but the copy hatches away entirely (IV 14, 28, 35 ag) are bracketed.

## House renderings settled in king-list-uruk-ii-to-kish-iii (2026-11-16)
- City at the head of a dynasty with -ga after final g (unug{ki}-ga) or -a (adab{ki}-a) → locative "In X"; with -še₃ instead (ma-ri₂{ki}-še₃, V 23) → literal "to-X (sic)", English follows the formula "In X".
- A reign line with no named subject (IV 47–48) → "He (?) reigned / exercised …"; totals written with ni-ag (V 32, 41) keep the singular in `l`.
- ba-gub after a city with no case ending → "its kingship was established at X" (as the pilot's Larak/Shuruppak).
- Readings by sign: Langdon's Ma-er → ma-ri₂{ki} (URU, as drawn); An-sir → an-sir₂ (BU); Kug-ᵈBaú → ku₃-{d}ba-u₂; munuz → munus; suĝuš → suḫuš; Akšak → akšak{ki} (UD.KUŠU₂, flagged). English: Mari, Akshak, Ku-Bau; munus lu₂ kaš-tin-na → "a woman tavern-keeper".
- A restored number carrying Langdon's "(?)" is a LACUNA glyph, not shipped as signs (V 26), and the arithmetic goes in the note.
