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

- **PDF page 55's header numeral, and two rough page joins (run 2026-09-17/18, pp. 55-62).**
  Before transcribing, PDF 55's printed-page numeral had a partial ink dropout: it read as an
  open crescent shape matching neither the confirmed "٤" (which has a descending stem) nor the
  confirmed "٥" (a closed loop) cleanly. Decided meanwhile: rendered both PDF 54 and PDF 55 at
  150dpi and diffed them pixel-by-pixel — mean difference 17.5/255, i.e. clearly different pages,
  not a duplicate leaf like the 48-49 case — and confirmed PDF 56-62 read "36"-"42" cleanly in
  sequence, so PDF 55 = printed 35 by elimination (offset printed = PDF-20 continues to hold).
  Separately, the adjudicator flagged two joins as not reading smoothly: (1) archive
  pp029-034.json's last line ends "...فقال له الملك احضرتك لاقتلك واعلم" and this batch's P35L01
  begins "روحك فتعجب الحكيم دوبان..." — "واعلم" wants an object clause that never comes; (2)
  P35L20 ends "...هذا جزائي منك تجازيني مجازاة" and P36L01 opens "التمساح قال الملك وما..." (lit.
  "the crocodile said..."), which has no connection to the surrounding Duban/Yunan narrative — no
  crocodile appears anywhere in this tale. For both: no PDF page is missing or duplicated (the
  header sequence 54-62 is complete and continuous, confirmed above), and both pass1 and pass2
  independently transcribed "التمساح" from the image with no prompting toward that reading, so
  three independent reads agree on the letterforms actually printed. Decided meanwhile: left both
  joins exactly as printed rather than emending — Middle Arabic prose in this edition is not
  always grammatically tidy (precedent: the p17→18 join, 2026-09-16) and "التمساح" may be a
  printer's error or a period idiom not yet recognised; do not silently correct it if it recurs.
  If a future run finds a clean referent for "التمساح" nearby, or another instance of this kind
  of non-sequitur, revisit whether something is systematically being mis-rendered at this spot in
  the scan.

- **Faint header numerals, PDF pages 74-76 (run 2026-09-18, pp. 71-78).** PDF 71/72/73/77's
  printed header numerals were crisp and read unambiguously "٥١"/"٥٢"/"٥٣"/"٥٧" (three independent
  correction-pass agents and a dedicated pixel-level comparison against the confirmed "٤٣" glyph
  from PDF 63, all agreeing). PDF 74-76's numerals are genuinely faint on the scan itself (confirmed
  by re-rendering at up to 1200 dpi via a tight PDF-coordinate clip — more resolution did not
  recover more detail, so this is print/ink wear on the original page, not a rendering artifact).
  One correction-pass agent misread PDF 75's numeral as "٤٨" in passing while excluding the running
  header; decided meanwhile this was a simple misread of a low-legibility glyph, not a real
  anomaly, because: (1) the surrounding pages 71-73 and 77 are unambiguous and strictly sequential;
  (2) the faint glyphs on 74-76, compared shape-by-shape against the confirmed "٥" (hook + loop,
  no stem) and "٤" (hook + long stem) reference forms, match the "٥" tens-digit shape consistently;
  (3) page 76 visibly opens a new tale ("حكاية الحمال و الثلث بنات", The Porter and the Three
  Ladies) — a sensible ~13-page transition point after the Ensorcelled Prince tale, not the kind of
  place a duplicate-leaf or skipped-page anomaly (like PDF 48-49) would be expected; (4) every page
  join in the batch, including the join to the previous archive, reads as continuous text with no
  gap. No archive or plan.md change beyond the ordinary batch entry. If a later run finds another
  anomaly nearby, revisit whether PDF 74-76 specifically need re-scanning.

- **Section heading vs. running header, PDF page 76 (run 2026-09-18, pp. 71-78).** This edition's
  running header (tale title + page number, small type, always excluded) can be hard to
  distinguish from a genuine section-heading body line (larger type, marked "h": true in the
  archive) when the heading happens to fall at the very top of a fresh page — the geometric line
  detector cannot tell them apart by position alone in that case. On p. 76 (opening "حكاية الحمال و
  الثلث بنات"), pass 1 dropped the heading entirely as if it were only the running header (21
  lines); pass 2 caught it as a real printed line and archived it (22 lines, h:true). Decided:
  checked band1.png directly — the heading is printed in the same size/weight as the tale-title
  headings on pp. 71/73/77 (which sit mid-page, unambiguously not headers), confirming it is a
  genuine body line, and it is now archived as P56L01, h:true. **Future runs: when a tale opens at
  the very top of a page, check the band image for a second, larger title line below the small
  running header before excluding anything — do not trust the line detector's header/body split at
  a tale boundary.**

- **Elliptical join, printed p. 43→44 (PDF 63→64, run 2026-09-18 pp. 63-70).** p. 43's last
  line ends "...و دخل من الدهاليز الى وسط القصر فاذا" ("...and he entered through the corridors
  to the middle of the palace, and behold—") and p. 44 opens "يجد فيه اثاثا غير انه مفروش
  بالحرير..." ("he finds furnishings in it, though it was carpeted with silk..."). The
  adjudicator flagged this as wanting a subject and negator between "فاذا" and "يجد" (e.g.
  "فاذا هو لا يجد") that isn't there. Decided meanwhile: checked both page ends directly against
  the 300dpi scan (not just the crops/bands) — the bottom of PDF 63 ends right at "فا" plus an
  illegible/smudged mark at the very page margin (no room for a further line), and the top of
  PDF 64 begins immediately after the running header with no line above "يجد" — so there is no
  additional printed line hiding at this boundary; the crop tool's page-63 gate flag ("24
  expected") was a false signal caused by its header-stripper failing on that one page (the
  title+page-number crop got counted as a body line — both correction passes correctly excluded
  it as instructed, so the archived 23-line count is right). Transcribed the join as printed
  (elliptical, like the p17→18 and p54→55 precedents) rather than treating it as evidence of a
  lost line. The final word of p. 43 ("فاذا") and the reading "يجد" (vs. "يوجد") on p. 44 are
  themselves only medium-confidence per the adjudicator — worth a second look if a cleaner scan
  of PDF page 63's bottom margin ever turns up.

- **Dropped verse-introducer + verse across the p.59→60 join (PDF 81→82, run 2026-09-18/19
  pp. 79-86).** Both correction passes on p. 59 ended at "...و شكر و شرب و انشد" ("...and he
  thanked her, and drank, and recited"), and both passes on p. 60 started directly with unrelated
  prose ("ثم تقدم الى صاحبة المحل..."). The adjudicator flagged the join as reading elliptically
  (a recited verse implied but never given). Decided meanwhile: rendered both page bottoms/tops
  fresh at 300dpi rather than trusting the crops/bands alone. p. 59's true last line is a
  verse-introducer, "يقول شعر", printed in the same widely-kashida-spaced style as other
  "[یقول] شعر" headings in this book (e.g. p. 61/62 of this same batch) — it sits just below the
  last line the automatic line detector found, so it fell inside band3's crop but had too little
  ink to register as its own detected line, and neither pass noticed it. p. 60 then genuinely
  opens with the two-line verse this heading introduces, "هاتها بالله هات * من كوس مترعات" /
  "واسقني منها بكاس * انها ماء الحياة", printed after the page's running header/title and before
  the prose both passes had transcribed as line 1 — again below the detector's threshold on both
  passes. This is the same failure mode as the "قيل شعر" drops on earlier pages, just landing at a
  page *boundary* rather than mid-page, which is why the gate's double-pitch-gap check (looks for
  a gap *between* two detected lines) never caught it. Recovered both by direct inspection and
  inserted by hand (p. 59 line 18; p. 60 lines 1-2, v:true) before applying verdicts. **Future
  runs: when a page's last transcribed line ends in "و انشد"/"و انشد يقول" or similar with no
  verse following, and/or the next page's first line is prose immediately after the running
  header, render both page ends at full resolution and check for a dropped heading/verse — don't
  rely on the crops or bands alone, since a line with mostly kashida and few ink pixels can fall
  below both the line detector's and the bands' effective coverage at a page edge.**

- **Stray printed vowel mark on a prose word (P62L18, run 2026-09-18/19 pp. 79-86).** One of the
  correction passes read a fatha-like mark over the alif and a shadda+kasra under the ذ of
  "الذ" in "في الذ عيش" ("in the most delightful life") and kept them (transcribing "أَلَذِّ"),
  reasoning that a single word can carry a printed mark inside an otherwise-bare prose line.
  Decided meanwhile, same as the P16L11 precedent: dropped the marks regardless — conventions.md
  and the gate both treat prose as categorically unpointed, and zooming into the scan left the
  mark itself ambiguous (a wavy stroke more consistent with a decorative/press-specific fatha
  rendering than a genuine hamza or madda hook). Archived as bare "الذ".

- **Both passes agreeing on a detached prefixed و (run 2026-09-19 pp. 87-94).** In every prior
  run, a detached-waw slip ("و قال" for "وقال") was always one pass's error, caught by
  disagreement with the other. This run, on 4 of the 8 pages, one specific pass (not
  consistently pass1 or pass2) detached و on ~15-20 words at once; separately, 26 lines had
  *both* passes independently write the same detached و, which diff_passes.py cannot flag
  since it only reports disagreements. Decided: checked several instances directly against the
  scan — و is one of the Arabic letters that never ligatures forward, so it always shows a
  small visual gap before the next letter whether or not there is an actual printed word-space,
  and conventions.md's rule ("a prefixed و is attached to its word") has no exception for و
  used as a bare conjunction. Resolved all disputed instances programmatically (regex-normalize
  `\bو \S` to attached, plus Persian ک to Arabic ك) without invoking the adjudicator, then
  re-swept the *entire* archived batch with the same regex after gating to catch the
  undisputed-but-still-wrong 26 lines. **Future runs: run this sweep on every batch before
  publishing, not just on disputed words — it costs nothing, and this run shows agreement
  between passes is not sufficient evidence of correctness for this specific slip.**
- **Kashida-stretched "شعر" transcribed as dashed letters (P71L13/PDF p.91, run 2026-09-19
  pp. 87-94).** Pass 1 read the verse-introducer word as three separate letters joined by
  em-dashes ("ش — ع — ر"); pass 2 read it as the plain word with a trailing alif ("شعرا"); the
  adjudicator, given both readings and the same kashida-is-not-a-space instruction used
  elsewhere in this run, still sided with pass 1's dashes. Decided meanwhile: rendered the band
  image at 2x directly — the three letters are joined by one continuous kashida stroke with no
  gaps and no separate marks, and the line ends at ر with no alif — so the true reading is the
  plain word "شعر" (no dashes, no trailing alif), overriding the adjudicator. Archived as
  "شعر". The same word occurs cleanly (no dispute) elsewhere in this batch (P73L14, "ثم يقول
  شعر"), supporting this reading. **Future runs: a dash-separated single-consonant sequence
  from one pass is itself a signal to check for kashida-stretching before trusting either
  pass's reading, even after adjudication.**
- **apply_verdicts.py's hardcoded PDF-18 offset (recurring since run 2026-09-17 pp. 47-54, most
  recently run 2026-09-19 pp. 87-94).** The committed tool still assumes printed = PDF-18
  throughout; every run since the pp. 47-54 offset discovery has worked around this with a
  locally-patched copy (never committing the change, since the runbook's gate step expects
  `git diff --stat` to show only the archive plus claim/LOG/plan). The offset has now held for
  6 consecutive runs (PDF 50 through PDF 94). Left the tool as-is again this run, consistent
  with precedent and the gate's scope rule, but flagging in case Zev would rather have the
  constant fixed properly (or made a configurable argument) now that it is clearly not a
  one-off anomaly.
- **apply_verdicts.py cannot express a word-reorder verdict (P67L22/PDF p.87, run 2026-09-19
  pp. 87-94).** The two passes disagreed on word order ("باذنك ندخل" vs "ندخل باذنك"); the
  adjudicator ruled pass 2's order correct via two separate word-level verdicts (insert "ندخل"
  at one position, delete pass 1's "ندخل" at the other). The tool's verdict application is a
  simple text-replace, so it only executed the deletion half and silently dropped the word
  entirely, leaving a double space. Caught by a post-apply scan for double spaces and fixed by
  hand. **Future runs: when an adjudicator verdict describes a word moving rather than being
  substituted, apply it by hand rather than trusting apply_verdicts.py, and it's worth scanning
  the finished archive for doubled spaces (a `  ` regex) as a general check for this failure
  mode.**

- **Running header switches mid-page with no heading line, PDF p.101/printed p.81 (run
  2026-09-19 pp. 95-102).** The running header changes from "حكاية القرندلي الاول" (First
  Qalandar) to "حكاية القرندلي الثاني" (Second Qalandar) partway through this batch, but the
  body text on that page is still the first qalandar's own narration (he is recounting how he
  met the second and third qalandars — no change of speaker, no printed section heading).
  Decided: this is unlike the earlier tale-opening cases (e.g. p.56's "حكاية الحمال" heading)
  where a genuine larger-type heading line marks a new tale; here the header simply anticipates
  content later on the page or in the next few pages. Treated as ordinary running-header
  behaviour, not transcribed, no h:true line added. If a future run finds the header/content
  mismatch persists oddly or a genuine heading is dropped nearby, revisit.

- **Doubled printed و across a page break, PDF p.100→p.101 (printed p.80→p.81, run 2026-09-19
  pp. 95-102).** p.80's last line ends on a lone, clearly detached "و" at the right margin; p.81's
  first line begins "وخليفة" (itself a separately-printed و attached to خليفة). Read together the
  passage would want a single "و" joining two titles ("امير المؤمنين وخليفة رب العالمين" =
  "Commander of the Faithful and Caliph, Lord of the Worlds"), but as printed there are two.
  Checked both page images directly at 300dpi: no catchword line exists below p.80's last line
  (the trailing و is part of the body line itself, not a separate catchword), and no line is
  missing or duplicated in the header-number sequence. Decided meanwhile: transcribed both و's
  exactly as printed rather than merging them, per the p17→18/p54→55/p43→44 precedent of leaving
  ungrammatical-looking but genuinely printed joins as-is. If this doubled-conjunction-at-a-page-
  break pattern recurs, it may be a period/press convention worth a rule of its own.

- **Correction agent used "best-effort" vocalization instead of re-verifying printed marks,
  PDF p.98 (run 2026-09-19 pp. 95-102).** One of the two independent correction passes for this
  verse-heavy page reported reconstructing tashkil for two "well-known" epigrams from memory of
  the classical text rather than confirming every mark against the crop, reasoning that the
  underlying poems were recognisable. This is exactly the kind of silent normalization the
  two-pass/adjudication design exists to catch, and it did: flagged specifically for the
  adjudicator, who re-verified the page's verse diacritics from the images and corrected several
  (صِبْتَ not صَبَتْ، تَنْعَى not تُدْعَى، الْأُسْلِ not الْاُسْدِ، and confirmed pass 1's
  "فَكَانُوهَا وَلَكِنْ" refrain over pass 2's "فَكَانُوا" as the actually-printed reading).
  **Future runs: if a correction agent's own report admits reconstructing text from a "well-known"
  or "classical" source rather than the image, treat that page's marks as unverified regardless of
  which pass it was and call it out explicitly to the adjudicator, as done here.**

- **New printed punctuation mark, PDF p.110/printed p.90 (run 2026-09-19/20, pp. 103-110).** Both
  independent correction passes noticed small ink marks in the prose — a dot sitting above a short
  comma-like hook, in the word-gap after certain words — that are not part of any letter's normal
  shape and are not tashkeel (they sit between words, not over a letter). This is the first time
  any mark beyond the edition's "( )" and the "—" end-of-line filler has turned up in the archive.
  Decided: transcribe this recurring mark as "؛" (Arabic semicolon) wherever it appears clearly
  separated from letter shapes at a plausible clause-pause position (confirmed at four spots on
  this page: P90L01, P90L04 ×2, P90L13). The adjudicator's own summary recommendation agreed with
  this, but two of its four individual line-verdicts inconsistently dropped the mark anyway —
  caught by re-inspecting the page directly and restored to match the other two. **Future runs:
  watch for this mark on other pages (it may simply not have been noticed before now, rather than
  being new to this page specifically) and transcribe it as "؛" on the same evidence — a dot+hook
  shape distinct from any letter, sitting in the word-gap, not reproducible as ordinary ink noise
  since it recurs at plausible pause points.** Not yet added to conventions.md pending a second
  occurrence elsewhere in the volume to confirm the convention is real and not page-specific.

- **Adjudicator silently normalized a printed dotless فى to modern في without checking the image
  (PDF p.110/printed p.90, run 2026-09-19/20 pp. 103-110).** Two disputes (P90L02, P90L04) pitted
  pass1's dotless "فى" against pass2's dotted "في"; the adjudicator's verdicts marked both "low"
  confidence with the note "kept pass2's standard modern spelling" — i.e. it defaulted to the
  modern form without actually verifying the glyph, which is exactly the kind of silent
  normalization conventions.md's ى/ي rule exists to prevent. Checked directly: at 2.2x zoom, line
  2 shows the print using BOTH spellings on the very same line — a clearly dotted "في" right after
  "رجلان" and a clearly dotless "فى" after "ساكنين" a few words later — so this is not a
  transcriber error to normalize away in either direction, just an inconsistently-set 1839 press.
  Line 4's disputed instance is also dotless at zoom. Reverted both to pass1's dotless reading.
  **Future runs: a "kept the standard/modern spelling" note on a low-confidence verdict is a red
  flag by itself — it means the adjudicator didn't actually look, not that the reading is settled;
  re-check any such verdict against the image before trusting it, especially for ى/ي and ة/ه.**

- **apply_verdicts.py silently drops word-insertion verdicts (empty pass-1 text), a second tool
  gap beyond the already-known word-reorder issue (run 2026-09-19/20 pp. 103-110).** The tool's
  apply loop only acts on a verdict when `v['pass1']` is truthy, so any verdict resolving a
  word pass 1 omitted entirely (pass1 text `""`, a genuine gap rather than a substitution) is
  silently skipped with no warning — found 3 cases this run (PDF p105 "يوم"/"لك" at a missing-word
  join, PDF p108's verse "أَنِّي") that would have shipped as silent text loss if not caught by an
  explicit post-apply audit of every verdict with empty pass-1 text. Applied all three by hand.
  **Future runs: after apply_verdicts.py runs, grep verdicts.json for entries where `pass1` is
  empty/falsy but `verdict` is non-empty, and apply each by hand — the tool will not do it and
  will not tell you it skipped anything.**

- **Page-specific لام/دال ascender confusion is not uniform, PDF p.109/printed p.89 (run
  2026-09-19/20 pp. 103-110).** Pass 1's agent reported that this page's print consistently shows
  a tall لام ascender where classical spelling expects a shallow دال curve (e.g. "قل" for "قد"),
  and normalized several instances on that claim, citing a cross-check against confirmed لام/دال
  shapes elsewhere on the page. The adjudicator re-checked each disputed instance individually
  rather than trusting the blanket claim, and found it did NOT hold uniformly: two of three
  disputed "وقل"/"وقد" spots are genuinely دال (pass2 correct), while "يبعل" (not "يبعد") is
  genuinely لام (pass1 correct) — a real letterform, not a page-wide font substitution. **Future
  runs: a correction pass's claim that a whole page uses one glyph shape for a letter it doesn't
  normally have needs per-instance verification, not blanket acceptance — Middle Arabic spelling
  variance and genuine print wear can look identical to a font-wide substitution but usually
  isn't.**
