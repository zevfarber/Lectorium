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
| done (2026-09-18, unattended) | 71–78 | 51–58 | `archive/pp051-058.json` | printed = PDF − 20 confirmed (PDF 71/72/73/77 headers read "٥١"/"٥٢"/"٥٣"/"٥٧"; PDF 74-76's numerals were faint/worn but the sequence and narrative both confirm no anomaly); the Tale of the Ensorcelled Prince concludes (his account of the sorceress's rage, the frame closes) and "حكاية الحمال و الثلث بنات" (The Porter and the Three Ladies) opens on p. 56 — its heading was dropped by the line detector and recovered from the band as an h:true line |
| done (2026-09-18/19, unattended) | 79–86 | 59–66 | `archive/pp059-066.json` | printed = PDF − 20 confirmed (PDF 79/86 headers read "٥٩"/"٦٦"); "حكاية الحمال و الثلث بنات" continues: the porter drinks with the three ladies, reciting verse between rounds; both correction passes and the line detector dropped a verse-introducer line at the very end of p. 59 ("يقول شعر") and the two-line verse it introduces at the top of p. 60 — recovered by checking the scan directly, see LOG |
| done (2026-09-19, unattended) | 87–94 | 67–74 | `archive/pp067-074.json` | printed = PDF − 20 confirmed (PDF 87 header read "٦٧"); "حكاية الحمال و الثلث بنات" continues to its end: the caliph, Jafar and Masrur are admitted disguised as merchants, the porter and the three ladies with their two black bitches, then the three qalandars arrive and the door-condition is set; a long verse block (two ghazals) interrupts the ladies' story; the tale closes with the qalandars' framing story beginning (the first qalandar's account opens) |
| next | 95–102 | 75–82 (tentative) | `archive/pp075-082.json` | printed = PDF − 20 until told otherwise; verify PDF 95's header before trusting this |
| … | … | … | … | one archive per run |
| end | ~933–938 (offset now −20; recheck near the end) | ~913–920 | | then create `DONE` |

**Last PDF page done: 94 (archive ends at printed p. 74). Pages remaining: ~844 PDF pages
(approximate, pending the corrected offset holding). Lines archived: 1573. calc.traineddata
retrained 2026-09-19 with 91 new verified line pairs (pp. 63-66, all four pages clean 1:1
crop-to-line matches); verified against held-out pages not used in training (printed pp. 40 and
55): combined CER 9.74%→9.31%, not a regression, so committed. tools/lines/ now holds pairs for
pp. 13-19, 29-32, 43, 45-48, 63-66. Next retrain attempt due when lines archived pass 1600 (i.e.
next run, pp. 95-102).

## Phase 2 — reading edition (not yet scheduled)

Re-cut the archives into nights (`arabic-nights-conventions.md`, "Chunking"), then the usual
Lectorium pipeline per night: vocalisation, two translation layers, morphemic glossary into the
shared `nights-glossary.json`, notes, audio (`ar-XA`). The pilot `nights-frame-01` is the model.
Design this phase once ~50 pages of clean text exist; do not start it inside this routine.
