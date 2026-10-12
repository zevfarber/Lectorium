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
