# The Secret History — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to the Secret History. Read `conventions.md` first.

Packet: every word of the part in order — index · § · line · Ming gloss · Han · romanized word — plus
`novel-forms.json` (tokens not yet in secret-history-glossary.json, each with its Ming gloss) and
`known-forms.json`.

**Drafter** gets `conventions.md`, `packet.md`, and `secret-history-01-06.json` (the model). Writes
`drafts/<id>/units.json`:
```
{"titleEn": "The Secret History of the Mongols — §§A–B: <our English name>",
 "part": "§§A–B — <our English name>",
 "about": "<optional short paragraph>",
 "sentences": [{"t": "<romanized words of a run of consecutive indices, single spaces, cut by script>",
                "l": "...", "i": "...", "n": "...",
                "words": [{"morph": [{"lemma": "qaγan", "gloss": "qan, sovereign, emperor [皇帝]"},
                                     {"lemma": "-(n)u", "gloss": "genitive: of … [的]"}]}, …]}]}
```
One `words` entry per source word, in order; the units together consume every word of the part exactly once.

**Glosser** (Sonnet) gets `novel-forms.json`, `known-forms.json`, `units.json`, and the glossary section of
`conventions.md`; writes `drafts/<id>/gloss.json` `{"<token>": "<dictionary form> — <meaning> (<grammar>) [<Ming
gloss>]", "__broaden__": {…}}`. The reviewer checks every lemma against the morph it supports.

Build: `python3 ../run3/r3.py build secret-history <id>`, then `validate`. No audio (voice not chosen).
