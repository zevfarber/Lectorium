# Cantar de mio Cid — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to the Cid. Read `conventions.md` first.
Every part takes two firings: first ACTION establish (the text), then ACTION draft.

## ACTION establish
`python3 ../run3/r3.py establish-packet cid <id>` writes `drafts/<id>/establish.md` with the procedure:
start from `source/ocr/<id>.txt`, read every line on the page image (`python3 ../run3/page.py
source/raw/pidal1923_text.pdf <pdf page> --zoom 1.4`, then 8-line strips at zoom 2 with `--clip`), correct the
letters, mark Pidal's italics as [brackets], write `source/established/<id>.txt`, pin it.

## ACTION draft
Packet: the established verses with their numbers and tirada breaks, flags, glossary status;
`novel-forms.json` / `known-forms.json`.

**Drafter** gets `conventions.md`, `packet.md`, `cid-tiradas-01-04.json` (the model). Writes
`drafts/<id>/units.json`:
```
{"titleEn": "The Song of the Cid — <name> (tiradas A–B, lines X–Y)",
 "part": "Tiradas A–B · <name> (lines X–Y)",
 "sentences": [{"t": "<1–4 verses joined by \n, cut by script>", "l": "<one line per verse>", "i": "...", "n": "..."}]}
```
The build sets `v`, `ln` and `p` (first unit of each tirada) itself. The name is the part's `name` in
parts.json unless the drafter has a better one from the action.

**Glosser** (Sonnet): every novel token, in the cid-glossary.json format; `__broaden__` for known ones.

Build: `python3 ../run3/r3.py build cid <id>`, then `validate`. No audio.
