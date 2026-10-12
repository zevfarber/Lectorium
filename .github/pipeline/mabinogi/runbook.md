# The Four Branches — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to the Mabinogi. Read `conventions.md` first.
Every part takes two firings: ACTION establish (the text), then ACTION draft.

## ACTION establish
`python3 ../run3/r3.py establish-packet mabinogi <id>` writes `drafts/<id>/establish.md` (inputs, the worklist
counts, the procedure). Work through every 'check' and 'loss' item in `source/drafts/<id>-diffs.txt` on the page
image; log each decision in `drafts/<id>/establish-log.md`; write `source/established/<id>.txt` (paragraphs
separated by blank lines, in the format of `source/mabinogi-001-established.txt`); pin it.

## ACTION draft
Packet: the established paragraphs and the establishment log (supplied words and kept slips the notes must
mention); `novel-forms.json` / `known-forms.json`.

**Drafter** gets `conventions.md`, `packet.md`, `mabinogi-001.json` (the model). Writes `drafts/<id>/units.json`:
`{"about": "<optional>", "sentences": [{"t": "<a sentence, cut by script>", "l": "...", "i": "...", "n": "..."}]}`.
The build sets `p` (paragraph starts), title, titleEn (`<branch title in English> — <part name>`), group and source.

**Glosser** (Sonnet): every novel form in the mabinogi-glossary.json format; `__broaden__` for known ones.

Build: `python3 ../run3/r3.py build mabinogi <id>`, then `validate`. No audio.
