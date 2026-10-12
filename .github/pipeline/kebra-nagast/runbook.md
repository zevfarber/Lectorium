# Kebra Nagast — what one firing does

Follow `../run3/RUNBOOK.md`; this file adds what is particular to the Kebra Nagast. Read `conventions.md` first.

Packet: `drafts/<id>/packet.md` — the Geʿez of the part, paragraph by paragraph (chapters marked
`== chapter N ==`), and the last unit of the previous part. `novel-forms.json` lists every word form not yet
glossed in a published part; `known-forms.json` the ones that are (with their entries).

**Drafter** gets `conventions.md`, `packet.md`, and `kebra-nagast-ch1.json` (repository root) as the model.
Writes `drafts/<id>/units.json`:
```
{"titleEn": "The Glory of Kings — <our English name> (<cite as in parts.json>)",
 "part": "<cite> — <our English name>",
 "about": "<optional: one short paragraph on what happens here>",
 "sentences": [{"t": "<Geʿez, cut by script>", "l": "...", "i": "...", "n": "...", "p": true}, ...]}
```
The units' `t`, joined, must reproduce the part's Geʿez exactly (whitespace aside); each ends at ። ፤ or ፨.
No `tr`, no `words` — the build makes them.

**Glosser** (Sonnet) gets `novel-forms.json`, `known-forms.json`, `units.json` and the glossary section of
`conventions.md`; writes `drafts/<id>/gloss.json`: `{"<form>": "<lemma> — <meaning> (<grammar>)", …,
"__broaden__": {…}}` — every novel form, parsed from every place it occurs; Dillmann is the authority.

**Reviewer**: as in RUNBOOK.md; also checks every gloss's lemma and parse (the popup shows it on every tap).

Build: `python3 ../run3/r3.py build kebra-nagast <id>`, then `validate`. No audio (voice not chosen yet).
