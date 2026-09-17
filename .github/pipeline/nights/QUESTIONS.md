# QUESTIONS — Nights transcription

Open decisions the rules do not settle. A run writes the question and what it decided meanwhile.

- **Verse vowel marks.** The edition points its verse; the archive keeps the marks (`v` lines).
  Decided 2026-09-16: keep them — they are part of what is printed, and the translation phase
  needs them. The reader's "bare" toggle will have to leave `v` lines alone.
- **Tanwīn vs damma in verse.** The type barely distinguishes `ٌ` from `ُ`. Decided: follow the
  rhyme word where the line's rhyme settles it; otherwise mark low confidence.
- **Stray mark on a prose word (P16L11, run 2026-09-16 pp. 31-38).** The adjudicator read a
  faint shadda-like mark over `عليّ` in a prose line and kept it, high confidence. Decided
  meanwhile: dropped it — conventions.md is explicit that prose carries no marks at all
  regardless of what is faintly visible, and the gate enforces this. If future pages show a
  pattern of genuine marks appearing in prose (not just ink noise), revisit the rule.
- **Abrupt page join, printed p. 17→18 (PDF 35→36, run 2026-09-16 pp. 31-38).** p. 17 ends
  "...ولا يغرنك حالي فلما سمعت" and p. 18 opens a new "فلما..." clause without ever giving the
  apodosis of the first فلما. Both independent transcribers agree on the exact wording, and
  nothing in the bands suggests a dropped line, so decided meanwhile: transcribed as printed
  (Middle Arabic prose is not always grammatically tidy) rather than treated as an error.
- **Duplicate scan leaves, PDF pages 48-49 (run 2026-09-17 pp. 47-54).** The two-pass
  transcription of the claimed batch (PDF 47-54) found PDF pages 48 and 49 to be near-verbatim
  duplicates of printed pp. 28-29: p048's 22 lines match archive `pp021-028.json` P28 almost
  word for word, and p049 matches p047 (both = printed p. 29, with the usual OCR-quality
  differences between two independent reads of the same leaf, not two different pages).
  Confirmed by rendering all four page images at 150 dpi and comparing them directly (PDF 46 and
  48 are visually identical scans, both headed "٢٨"; PDF 47 and 49 are visually identical, both
  headed "٢٩") and by rendering PDF page 50, whose header reads "٣٠" — confirming it is the
  genuine next page, printed p. 30, not printed p. 32 as the flat `PDF − 18` formula would give.
  **This means the archive.org scan has two extra duplicate leaves inserted right after PDF page
  47, and from PDF page 50 onward the offset is `printed = PDF − 20`, not `PDF − 18`, until or
  unless another such anomaly is found.** Decided meanwhile: excluded PDF pages 48-49 from the
  archive entirely (no new printed-page content), built `archive/pp029-034.json` from PDF pages
  47, 50, 51, 52, 53, 54 mapped to printed pp. 29-34, and updated `plan.md`'s running total and
  offset note accordingly. **Every future run must read each new PDF page's own printed header
  number rather than trust the flat formula blindly** — nights_ocr.py has no way to check this
  automatically, so the correction agents or the batch-planning step should sanity-check the
  first page's header against the expected printed number before transcribing a full batch, in
  case a further scan anomaly (another duplicate, or a missing leaf) appears later in the volume.
