# Sumerian King List — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to the King List. Read `conventions.md` first.

Packet: Langdon's transliteration of the part's lines with his confidence, restorations and remarks; the page
images to read; the value→sign map prepared at setup (first pass — verify every sign on the plate).

**Drafter** gets `conventions.md`, `packet.md`, `king-list-antediluvian.json` (the model), the plate image(s)
and transliteration pages named in the packet (`source/pages/*.jpg`; crop and zoom with Pillow/PyMuPDF and read).
Writes `drafts/<id>/units.json`:
`{"titleEn": "Sumerian King List — <name> (<range>)", "part": "<name> (<range>)", "about": "<optional>",
  "sentences": [{"col": "II", "line": 1, "ln": 1, "l": "...", "i": "...", "n": "...", "words": [...]}]}` —
words exactly as in the Hammurabi runbook (glyphs with `sign` keys; `u` for count-numerals). Units never cross a
column; together they cover every line of the part in order (a lost entry = one `lost` unit).

**Glosser** (Sonnet): `{lemma: gloss}` for lemmas not in the published King List glossary.

Build: `python3 ../run3/r3.py build king-list <id>`, then `validate` (it writes `drafts/<id>/linecheck.md`: lines
whose values differ from Langdon — confirm each on the plate); `python3 ../run3/signs.py check`. No audio.
