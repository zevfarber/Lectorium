# Cantar de mio Cid — conventions (Run 3)

Distilled from the project's `old-spanish-cid-conventions.md` (2026-07-20) and the published pilot
`cid-tiradas-01-04.json` (tiradas 1–4, lines 1–64), the model of shape and register.

## Edition and sources (sole-source rule)
- Text: Ramón Menéndez Pidal, *Poema de mio Cid*, 2.ª edición corregida (Clásicos Castellanos 24, Madrid 1923)
  — public domain. Scan: archive.org `PoemaDeMioCid2ed` (`source/raw/pidal1923_text.pdf`; printed page = PDF
  page − 4). The OCR (`source/raw/pidal1923_djvu.txt`) is never used as text; the mechanically cleaned
  per-part drafts in `source/ocr/` are a starting point only. The structure (152 tiradas, lines 1–3730, every
  margin label and tirada break) was checked by eye on all 236 poem pages on 2026-10-12 (`source/tiradas.json`).
- Lexical aids, PD: Pidal's own notes at the foot of the page, his *Cantar de mio Cid: texto, gramática y
  vocabulario* (1908–11). Modern translations (Hamilton & Perry, Raffel, Harney, Such & Hodgkinson …) are never
  opened.

## The manuscript and honesty
Single manuscript (Vivar codex; colophon "Per Abbat … era de mill e CC XLV", AD 1207). The first folio is
lost; Pidal's prose reconstruction of the opening is not included. Two more folios are lost (after v. 2337 and
after v. 3507): Pidal fills them with italic prose from the chronicles (tiradas 115, 149, 150) — we do NOT
include that prose; the unit where the gap falls says in its note what is lost and that Pidal supplies the sense
from the *Crónica de Veinte Reyes*.

## Orthography (established text)
- Pidal's critical text exactly, inconsistencies included (puorta/puerta, llegaua/tornava, buolto, run-together
  dela), old accentuation (tí, Vío). Pidal does NOT accent "mio" — the OCR does; the image decides.
- Pidal's italics = editorial restorations → [brackets] at letter/word level: entróv[e], su[e], ve[e]r,
  R[o]y (only the o is italic), [Burgos]. A wholly italic (restored) line is printed plain and flagged in its note.
- Quotation marks: one opening “ and one closing ” per speech; Pidal's repeated line-initial quotes dropped.
- No transliteration; no plain-letters toggle needed (ç is readable).

## Sectioning, numbering, segmentation
- Work = Cantar de mio Cid; parts = runs of whole tiradas (≈55–110 lines), a very long tirada split at a strong
  sense break; ids `cid-tiradas-NN-MM` (a/b/c for split tiradas).
- Line numbers are Pidal's, b-numbers included (14b). `ln` = the integer part of the unit's first line (the
  reader computes the range by counting lines, so a range across a b-line reads one high — accepted, as in the
  pilot). Pidal moves lines but keeps their numbers: follow his print order, keep his numbers, and say so in the
  note where it happens. A line with two numbers (1044-5) takes the first in `ln`; the note gives both.
- Verse stays verse: tap-unit = punctuated sense-unit (1–4 lines, never more than 6), lineation kept with "\n",
  `v: true`; `p: true` on the first unit of each tirada. Caesura not marked.
- Pidal's tirada rubrics are editorial: fold a short English version into the first note of each tirada
  ("Tirada 2 (assonance ié-a) — Omens on the road to Burgos").

## Translation and notes
- `l` structurally transparent, keeping the line division of `t` (one `l` line per verse); hyphenate glued
  clitics sparingly (oviéronla "they-had-it", ferídal "a-blow-to-it", nol "not-him"). `i` real English, one
  paragraph, lightly elevated, never childish.
- Recurring patterns (first few times, then a nudge): initial f- for modern h- (fablar, fincar); aver
  'have/hold'; the split conditional (conbidar le ien); enclitic squeeze (nol, gela, tornós, l'an); double
  negative; epic tense-mixing; article + possessive (las sus bocas); a new assonance = a new tirada.
- House renderings: v. 20 "God, what a good vassal — if only he had a good lord!"; the *en buen ora* formula
  "in a good hour you girded on your sword" (and its variants: "born in a good hour").
- Never bowdlerize.

## Glossary
Shared `cid-glossary.json` (`{work, workEn, language, note, glossary}`), keyed by the reader's tokens (brackets
stripped, lowercased; an apostrophe splits: l'an → `l`, `an`), value "lemma = modern Spanish — meaning
(grammar)" as in the existing entries. 100 % coverage, checked by the validator.

## Pronunciation and audio
Reconstructed twelfth-century Castilian (ç = [ts], z = [dz], intervocalic -s- = [z], x = [ʃ], j/g(e,i) = [ʒ],
initial f- = [f], v distinct from b). `langCode: null`. A voice has not been chosen by the owner; parts
publish without audio until he chooses. Do not build audio.

## Decisions taken while setting up Run 3 (2026-10-12; listed in QUESTIONS.md)
- Lost-folio prose left out, with a note (as the pilot did with the reconstructed opening).
- Pidal's print order followed where he moves lines; his numbers kept.
- Unnumbered wholly italic lines take provisional letters after the preceding number (181b, 181c, …), as the
  pilot did with 14b, and the note says the letter is ours.
- The six numbers printed nowhere (99, 1043, 2432, 2459, 3663, 3679) and the label 2455 printed twice: follow
  the print; the establishing run checks each on the image (Pidal's footnotes may explain) and records it.
- The pilot's `[Roy]` at v. 15 and v. 58 should be `R[o]y` (only the o is italic); left for the owner.
