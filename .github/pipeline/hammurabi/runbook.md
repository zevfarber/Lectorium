# Laws of Hammurabi — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to Hammurabi. Read `conventions.md` first.

## Stele parts (ACTION draft)
Packet: `drafts/<id>/packet.md` — Harper's transliteration line by line (col · line), the plates that carry
those columns (PDF pages of `source/harper1904-cornell.pdf`), and the sign keys already in the glossary.

**Drafter** gets: `conventions.md`, `packet.md`, the published part `hammurabi-laws-26-41.json` (repository
root) as the model, and the plate images it renders itself (`python3 ../run3/page.py source/harper1904-cornell.pdf
<page> --zoom 3` and crops; read every sign — the plate decides which sign Harper's normalized word stands
for). Writes `drafts/<id>/units.json`:
```
{"titleEn": "Laws of Hammurabi — §A–B: <our English name> (<col> <line> – <col> <line>)",
 "part": "Laws §A–B · <name> (Col. <col> <line> – <col> <line>)",
 "about": "<what these laws do, in a short paragraph, like the published parts' about>",
 "sentences": [
  {"col": "XII", "line": 63, "ln": 42, "p": true,
   "l": "...", "i": "...", "n": "...",
   "words": [
     {"reading": "šum-ma", "say": "šumma",
      "glyphs": [{"sign": "TAG", "role": "phon", "tr": "šum"}, {"sign": "MA", "role": "phon", "tr": "ma"}],
      "morph": [{"lemma": "šumma", "g": [0, 1]}]},
     {"reading": "a-wi-lum", "say": "awīlum", "glyphs": [...], "morph": [...]},
     {"reading": "A.ŠÀ", "say": "eqlam", "nl": true,
      "glyphs": [{"sign": "A", "role": "log", "tr": "A", "val": "eqlam"}, {"sign": "SHA3", "role": "log", "tr": "ŠÀ", "val": ""}], ...}
   ]}]}
```
A multi-sign Sumerogram carries the whole Akkadian value on its first glyph and `"val": ""` on the others
(as `AGA₃.ÚS` = rēdûm in hammurabi-laws-26-41). `p: true` on the first unit of each law. The epilogue parts use `ln` = the stele line and no `p` except at a
new paragraph of sense. `title`/`titleRead` are made by the build from the first two words.

**Glosser** gets `units.json`, the list of lemmas used that are not in an earlier part's glossary (compute it
by script from the published `hammurabi-*.json` glossaries), and the glossary section of `conventions.md`;
writes `drafts/<id>/gloss.json` `{lemma: "gloss"}` in the house format (look at `hammurabi-laws-26-41.json`'s
glossary: meaning, the forms met, the sign spelling where it matters).

**Reviewer**: as in RUNBOOK.md, plus — every sign against the plate; every Sumerogram's `val` and `say`;
`reading` reconstructs from the glyphs; the line division matches Harper's lines (the validator writes
`drafts/<id>/linecheck.md`, listing every stele line whose values differ from Harper's transliteration —
confirm each on the plate, they are mostly logograms Harper writes as the Akkadian word).

## Gap parts (hammurabi-gap-a, hammurabi-gap-b)
First firing: ACTION establish — follow `drafts/<id>/establish.md` (written by `R3 establish-packet`).
It establishes the WHOLE erased section into `source/established/hammurabi-gap-a.json` and `-gap-b.json`
and pins both. Drafting firings then work as for the stele, with these differences: each unit carries
`"w": "<siglum>"` and `"ref": "<the established unit's ref>"` instead of col/line, its note names the tablet
in plain words, a lost stretch is a gap unit (one word `{"reading": "[…]", "say": "…", "glyphs": [{"sign":
"LACUNA", ...}]}` — add the LACUNA pseudo-sign once with signs.py: `add cuneiform LACUNA 'WHITE SQUARE WITH
ROUNDED CORNERS' '{"name": "a lost stretch of text", "type": "marker", "sound": null, "determines": null,
"values": [], "label": "[…]"}'`), and the `about` says the stele is erased here.

## Audio
None to do: every pushed `hammurabi-` part is voiced by `audio.yml` automatically (German carrier voice).
