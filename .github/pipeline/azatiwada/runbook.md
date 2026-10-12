# Azatiwada — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to Azatiwada. Read `conventions.md` first.

## First firing only (before drafting azatiwada-22-37)
Correct the pilot as conventions.md says. The signs A070, A089, A057 (and the 21 other new signs §22–§75 need)
were added to signs-anatolian.json and the reader at setup. In `azatiwada-luwian.json` change the five glyphs'
`sign` and `s` by script (SUPER+ra/i at §8, §9, §10: A270 → A070, s = glyph(A070) + glyph(A383); tu at §20:
A088 → A089; INFRA at §21: A056 → A057; s from signs-anatolian.json), and reword the §17 note to say the clause
is not preserved in either copy as the corpus gives them. Commit that as its own commit, then go on to draft.

## ACTION draft
Packet: for each clause, the transcription and transliteration, and for each written word its glyph-units with
sign keys, the interpreted word, ACLT's lemmas/glosses/grammar per clitic, damage and register breaks.

**Drafter** gets `conventions.md`, `packet.md`, `azatiwada-luwian.json` (the model). Writes
`drafts/<id>/units.json`:
```
{"titleEn": "The Azatiwada Inscription (Karatepe) — §A–§B", "part": "§A–§B · <name>", "about": "<optional>",
 "sentences": [{"ln": 22, "p": true, "l": "...", "i": "...", "n": "...",
   "words": [{"reading": "Azzattiwadas", "say": "Azzattiwadas", "nl": false,
              "glyphs": [{"keys": ["A378"], "role": "det", "tr": "LITUUS"}, {"keys": ["A019"], "role": "phon", "tr": "á"},
                         …, {"keys": ["A439", "A383"], "role": "phon", "tr": "wa/i+ra/i"}, …],
              "morph": [{"lemma": "Azzattiwada-", "gloss": "Azatiwada (PN)", "g": [1, 2, 3, 4]}, {"lemma": "-s", "gloss": "nominative singular", "g": [5]}]}]}]}
```
One unit per clause slot; an absent clause is `{"ln": 42, "absent": true, "l": "[This clause is not preserved.]",
"n": "…", "words": [{"reading": "[…]", "say": "[…]", "glyphs": [{"keys": ["DAMAGED"], "role": "log", "tr": "[…]"}],
"morph": [{"lemma": "[missing clause]", "gloss": "…", "g": [0]}]}]}`. The validator checks every word's keys
against the source.

**Glosser** (Sonnet): `drafts/<id>/gloss.json` `{lemma: gloss}` for lemmas not yet in a published part's glossary.

Build: `python3 ../run3/r3.py build azatiwada <id>`, then `validate`; `python3 ../run3/signs.py check`. No audio.
