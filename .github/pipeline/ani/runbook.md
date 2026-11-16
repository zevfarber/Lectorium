# Book of the Dead of Ani — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to Ani. Read `conventions.md` first. Every part
is established in one firing and drafted in a later one. Parts are established in the order of `parts.json`
(a part marked "after" needs that part's established file for its starting point).

The scan: `source/raw/budge1895.pdf` (fetched by the runner; PDF page = Budge's printed page + 164). If the file
is missing, the fetch has not landed: write one line to QUESTIONS.md and stop.

## ACTION establish
`R3 establish-packet ani <id>` writes the procedure with this part's pages, start and end. In short: two
independent readers on the strongest model read every printed row (signs as Gardiner codes, Budge's
transliteration and English, page / plate / line, layout); `python3 hooks.py diff A.json B.json` lists where they
differ; a third reader decides each difference from a tight crop; Budge's transliteration is the check on every
word. Leave out Appendix sections and footnotes. Write `source/established/<id>.json`, then `R3 pin ani <id>`.
Reading hieroglyphic type is the one place this work can go quietly wrong: zoom in, one row at a time, and never
let a reader "complete" a word from its transliteration without seeing each sign.

## ACTION draft
`R3 packet ani <id>` lists every established word (signs, layout, Budge's reading and English) and writes
`known-lemmas.json`.

**Drafter** (strongest model) gets `conventions.md`, `packet.md`, `known-lemmas.json`,
`../../../ani-spell125-opening.json` (the model) and the most recently published `ani-*.json`. Writes
`drafts/<id>/units.json`:
```
{"titleEn": "Book of the Dead of Ani — <name>", "part": "<name> (Plate n)", "about": "<2–4 sentences: what this
  chapter is for and where it sits on the papyrus>",
 "sentences": [{"ln": 1, "p": true, "l": "...", "i": "...", "n": "...",
   "words": [{"reading": "ḏd·i", "say": "djed-i", "q": "0:1-2", "rubric": true,
              "glyphs": [{"sign": "I10", "role": "phon", "tr": "ḏ"}, {"sign": "D46", "role": "phon", "tr": "d"},
                         {"sign": "A1", "role": "suff", "tr": "·i"}],
              "morph": [{"lemma": "ḏd", "g": [0, 1]}, {"lemma": "·i", "g": [2]}]}]}]}
```
The glyph list of each word is copied from the packet by script (codes and order), never retyped; `q` is copied
from the packet and re-indexed if words are joined or split. No `s` and no `t`: the build makes them. No
`gloss` in morph unless this occurrence needs its own wording: the build fills it from the glossary.

**Glosser** (Sonnet): `drafts/<id>/gloss.json`, `{lemma: "lemma — meaning (grammar)"}` for every lemma not in
`known-lemmas.json`; a known entry too narrow for this part goes under `"__broaden__"` (old entry whole + " · " +
the new sense).

**Reviewer** (strongest model, two passes): every sign's role and `tr` against the word's reading; every reading
against the signs and against Budge's transliteration (a disagreement with Budge is fine when the signs support
it and the note says why); every grammatical label; `l` word by word; `i` against `l`; any phrase of Budge's
English or of a remembered modern translation in `l` / `i`; names and renderings against the published parts.

New signs: `python3 ../run3/signs.py add egyptian …` for each code the packet marks `*`, then
`python3 ../run3/signs.py check`. Then `R3 build ani <id>`, `R3 validate ani <id>` (the build refuses unless the
units use exactly the established signs in order), `R3 publish ani <id>`. No audio.

When the last part is published, `R3 done ani`. Leave every part's draft mark as it is: the owner decides when a
text stops being a draft.
