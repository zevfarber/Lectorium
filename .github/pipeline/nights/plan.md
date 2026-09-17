# Plan — Alf Layla wa-Layla (Calcutta II, vol. 1)

## Phase 1 — transcription (this routine)

Source: `source/calcutta2-vol1-p<A>-<B>.pdf`, 50 PDF pages per chunk, PDF pages 1–938.
Arabic text: PDF pages 19–938 = printed pp. 1–920. Eight PDF pages per run, twice nightly.

| status | PDF pages | printed pp. | archive | note |
|---|---|---|---|---|
| done (pilot, by eye) | 19–21 | 1–3 | root `nights-frame-01-source.json` | pilot text; p. 3 re-done below |
| done (attended, 2026-09-16) | 21–30 | 3–12 | `archive/pp003-012.json` | frame story to the start of Night 1 |
| done (2026-09-16, unattended) | 31–38 | 13–20 | `archive/pp013-020.json` | Third Sheikh's tale; ends at the frame's return to the merchant/jinni |
| done (2026-09-17, unattended) | 39–46 | 21–28 | `archive/pp021-028.json` | fisherman-and-jinni tale continues; frame's poem, second sheikh's tale opens (King Yunan and the physician Duban) |
| next | 47–54 | 29–36 | `archive/pp029-036.json` | |
| … | … | … | … | one archive per run |
| end | 931–938 | 913–920 | | then create `DONE` |

**Last PDF page done: 46. Pages remaining: 892. Lines archived: 571. calc.traineddata last
retrained 2026-09-16 (400 lines, 13.5%→3.3% CER). Next retrain when lines archived pass 600.**

## Phase 2 — reading edition (not yet scheduled)

Re-cut the archives into nights (`arabic-nights-conventions.md`, "Chunking"), then the usual
Lectorium pipeline per night: vocalisation, two translation layers, morphemic glossary into the
shared `nights-glossary.json`, notes, audio (`ar-XA`). The pilot `nights-frame-01` is the model.
Design this phase once ~50 pages of clean text exist; do not start it inside this routine.
