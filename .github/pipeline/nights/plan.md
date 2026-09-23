# Plan — Alf Layla wa-Layla (Calcutta II, vol. 1)

## Phase 1 — transcription (this routine)

Source: `source/calcutta2-vol1-p<A>-<B>.pdf`, 50 PDF pages per chunk, PDF pages 1–938.
Arabic text: PDF pages 19–938 = printed pp. 1–920 **for PDF pages up to 47**. Eight PDF pages
claimed per run, but a run's archive may cover fewer printed pages if the scan holds a
duplicate leaf (see below) — never guess the mapping, read each batch's first page's own
printed header number against the expected value before transcribing.

**Offset correction (found 2026-09-17, see QUESTIONS.md):** PDF pages 48 and 49 are duplicate
re-scans of printed pp. 28 and 29 (confirmed by direct image comparison), not new pages 30 and
31. They were excluded from the archive. **From PDF page 50 onward, printed = PDF − 20** (not
PDF − 18), confirmed against PDF page 50's own printed header "٣٠", until/unless another such
scan anomaly turns up later in the volume.

| status | PDF pages | printed pp. | archive | note |
|---|---|---|---|---|
| done (pilot, by eye) | 19–21 | 1–3 | root `nights-frame-01-source.json` | pilot text; p. 3 re-done below |
| done (attended, 2026-09-16) | 21–30 | 3–12 | `archive/pp003-012.json` | frame story to the start of Night 1 |
| done (2026-09-16, unattended) | 31–38 | 13–20 | `archive/pp013-020.json` | Third Sheikh's tale; ends at the frame's return to the merchant/jinni |
| done (2026-09-17, unattended) | 39–46 | 21–28 | `archive/pp021-028.json` | fisherman-and-jinni tale continues; frame's poem, second sheikh's tale opens (King Yunan and the physician Duban) |
| done (2026-09-17, unattended) | 47, 50–54 (48–49 excluded, duplicate leaves) | 29–34 | `archive/pp029-034.json` | King Yunan and Duban tale ends (Duban's execution scene); the Sindbad-the-falconer frame opens and runs to the ghouleh encounter and prince's prayer |
| done (2026-09-17/18, unattended) | 55–62 | 35–42 | `archive/pp035-042.json` | Duban is executed and his poisoned book kills King Yunan; the fisherman-and-jinni frame resumes and closes (the jinni is freed and departs); the Tale of the Enchanted Prince opens: the four colored fish, the black slave rising from the palace wall |
| done (2026-09-18, unattended) | 63–70 | 43–50 | `archive/pp043-050.json` | printed = PDF − 20 confirmed (PDF 63 header read "٤٣"); continues the Tale of the Ensorcelled Prince inside the frame "قصة البركة والسمكات الملونة": the sultan questions his army and vizier about the pond, then hears the young man's (half-marble) account of his wife's enchantment — catching her with her lover under a dome, wounding him, her curse turning the city to the pond/fish and him to stone; verse laments continue at the batch's end |
| next | 71–78 | 51–58 (tentative) | `archive/pp051-058.json` | printed = PDF − 20 until told otherwise; verify PDF 71's header reads "٥١" before trusting this |
| … | … | … | … | one archive per run |
| end | ~933–938 (offset now −20; recheck near the end) | ~913–920 | | then create `DONE` |

**Last PDF page done: 70 (archive ends at printed p. 50). Pages remaining: ~868 PDF pages
(approximate, pending the corrected offset holding). Lines archived: 1052. calc.traineddata last
successfully retrained 2026-09-17 (still the committed model — the 2026-09-18 retrain attempt
regressed on held-out pages and was discarded, see LOG). 113 new verified line pairs (pp. 43,
45-48; pp. 44/49/50 excluded, crops don't map 1:1) added to `tools/lines/` for the next attempt.
Next retrain attempt due when lines archived pass 1250.

## Phase 2 — the reading edition (live since 2026-09-18, same routine)

Not a later project any more: the two phases interleave, one job per firing, and **publishing
wins whenever a complete night is unpublished** (`runbook.md` step 0 → `publish-runbook.md`). The
rule exists because 50 pages of archive had accumulated with not one word of it readable, and at
eight pages a run the backlog was growing faster than it could ever be cleared. The editorial
rules are in `reading-conventions.md`; the pilot `nights-frame-01` is the worked model.

Units are the text's own nights, not page ranges. `tools/nights_index.py` derives them from the
opening formula فلما كانت الليلة and says which are complete and which are published — the
repository is the state, never this table. Run it rather than trusting what is written here.

| unit | archive range | state |
|---|---|---|
| frame, part 1 (pilot) | printed pp. 1–3 | published 2026-08-02, now via glossaryFile (migrated 2026-09-20/21) |
| frame, part 2 | P03L18(w11)–P10L09 | published 2026-09-20/21, 114 sense units (incl. one lead-in unit reusing the pilot's own last two sentences to cover the archived line P03L18 straddles — see QUESTIONS.md); created nights-glossary.json |
| Night 1 | P10L10–P14L08 | published 2026-09-20/21, 71 sense units; 505 new glossary entries |
| Night 2 | P14L09–P20L10 | published 2026-09-21, 184 sense units; 587 new glossary entries |
| Night 3 | P20L11–P25L11 | published 2026-09-21, 101 sense units; 514 new glossary entries |
| Night 4 | P25L12–P30L09 | published 2026-09-21/22, 117 sense units; 488 new glossary entries |
| Night 5 | P30L10–P38L01 | published 2026-09-22, 179 sense units; 648 new glossary entries |
| Night 6 | P38L02–P41L17 | published 2026-09-22, 69 sense units; 377 new glossary entries |
| Night 7 | P41L18–P48L19 | published 2026-09-23, 155 sense units; 721 new glossary entries |
| Night 8 | P48L20–P54L08 | published 2026-09-23, 108 sense units (7 verse); 547 new glossary entries |
| Night 9 | P54L09–P64L21 | complete, unpublished — next in the publishing queue (transcription itself has moved well past it; run `tools/nights_index.py` for the current table) |

A night runs 84–163 archived lines (about 5½ printed pages), so eight transcribed pages yield
roughly one and a half nights. Eight units are waiting as of 2026-09-18, so the next several
firings will publish rather than transcribe; after that it settles to about two transcribing runs
in five.

### Open items for phase 2

1. **Done 2026-09-20/21.** `nights-glossary.json` now exists (1331 entries: the pilot's 421 plus
   910 new from frame, part 2) and `nights-frame-01.json` carries `glossaryFile` instead of its
   old inline `glossary`. Every night after this one merges into the shared file.
2. **Done 2026-09-21 (attended, Cowork).** Arabic audio is on. The Action had been building the
   clips all along, but with an empty word-timing list for every sentence: the aligner's word
   splitter was a Latin-only copy of the reader's and found no words in Arabic. Fixed by one
   shared splitter (`.github/scripts/wordre.py`), a check that re-times any story whose timings
   do not match its words, and a loud failure when a story gets no timings at all. The voice is
   pinned (`ar-XA-Chirp3-HD-Achernar`). `nights-frame-02`, `nights-01` and `nights-02` now carry
   `audio`, and every new night carries it from publication (`publish-runbook.md` §6).
3. **The owner has never signed off on the pilot** (the phase 1 exit gate, open since August). He
   reads Arabic well enough to catch gross error, not to audit translation quality. Worth his eyes
   on the first night published under this pipeline.
4. Vols. 2–4 scans are already identified, so the volume boundary is not a blocker:
   `aliflailaorbook01unkngoog` / `aliflailaorbook02unkngoog` (v.2), `aliflailaorbooko03macn`
   (v.3), `aliflailaorbooko04macn` (v.4). Check each one's own printed headers before trusting any
   page offset, as with vol. 1.
