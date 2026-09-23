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

- **Night 0's pilot overlap falls mid-archived-line, not at a line boundary (run 2026-09-20/21,
  publishing nights-frame-02).** `publish-runbook.md` says to begin the new text "at the word
  after" the pilot's last sentence, but `validate_night.py`'s `--from`/`--to` only accept whole
  archive line refs and pull the *entire* line's tokens for the bare-strip check. The pilot's
  last word (اسمعه) falls at the 10th of 14 tokens on P03L18; the other 4 (`فقال له يا اخي`) open
  the new content. Decided: used `--from P03L18` (the only line-granular choice that includes the
  new words at all) and added one extra lead-in sense-unit at the very start of nights-frame-02
  covering the archived line's first 10 tokens — reusing nights-frame-01's own last two sentences'
  translation verbatim (word-for-word identical Arabic, confirmed programmatically) rather than
  re-translating already-published text. The lead-in's note tells the reader this opens
  mid-exchange, continuing directly from the pilot. **Future runs: if another Night 0-style pilot
  overlap ever recurs, or any future unit's start/end falls mid-line, the same pattern applies —
  extend to the nearest line boundary and add a small lead-in/trailing unit reusing the
  overlapping text's already-published translation, rather than trying to make the validator
  accept a partial line (it can't).**
- **Two slice-drafting agents mis-tokenized a word at their slice boundary (run 2026-09-20/21,
  publishing nights-frame-02).** Drafting this unit in 8 parallel slices, one agent split the
  archive's single fused token `اويومين` (P07L21) into two words `او يومين`, and a different agent
  fused the archive's two separate tokens `و` / `كرامة` (split across the P10L06→P10L07 line
  break) into one word `وكرامة`. Both were plausible-looking calls in isolation (matching normal
  Arabic word-division) but broke the mechanical bare-strip identity against the archive, which
  preserves the print's own token boundaries exactly. Caught by a full programmatic diff of the
  concatenated draft against the archive before assembling the story file (not by the two
  drafting agents' own self-reported validation, which each checked only its own slice and so
  didn't have the neighbouring context to catch the boundary error), then fixed by hand at the
  token level, re-verified, and only then run through `validate_night.py`. **Future runs: a
  slice-agent's own "verified against the archive" claim covers only its own slice; always
  reconcatenate every slice's tokens across the whole unit and diff against the archive
  start-to-finish before trusting the gate to catch a boundary-straddling mistake, since
  validate_night.py's own diagnostic only reports the *first* mismatch and a shift-by-one at slice
  N's end can otherwise masquerade as wall-to-wall corruption in slices N+1 onward.**
- **Two of this run's 113 sense units needed the deflowering/killing formula and the coercion
  scene translated at full frankness (no new decision — flagging for continuity).** Both episodes
  read plainly in both layers, matching the pilot's own established register; the review pass
  spot-checked both explicitly. No open question, just confirming the "never bowdlerize" rule was
  exercised, not merely stated, on this run.
- **Arabic audio may no longer be "never confirmed to work" — found while publishing Night 1
  (run 2026-09-20/21), not acted on.** Commit `2ecd88a1` ("Audio: build clips + align.json for
  nights-frame-01 nights-frame-02", 2026-09-20 ~22:42 UTC, just before this run) shows the
  `ar-XA` audio Action actually ran and built clips for both existing files:
  `nights-frame-01.json` already carries `"audio": "audio/nights-frame-01"`, and
  `audio/nights-frame-02/` has 117 clips on disk — but `nights-frame-02.json` itself was never
  updated with the `audio` field, so the site isn't serving them for that story. This run left
  both alone (fixing `nights-frame-02.json` is outside a publishing run's one-file scope; chasing
  audio is explicitly out of scope per `reading-conventions.md`) and published Night 1 without
  `audio` too, per the same rule. **Decided meanwhile:** nothing changed about this run's own
  output. **For the owner or a dedicated pass:** check whether the clips are actually correct
  (voice, alignment), wire up `nights-frame-02.json`'s missing field, and decide whether audio
  should now be added going forward (or backfilled to Night 1) rather than treating `ar-XA` as
  still broken.
- **A real vocalization error caught by the whole-night review pass, not by the gate (run
  2026-09-20/21, publishing Night 1).** At P12L14 ("مثل ماقتلت ولدي وحشاشة كبدي"), the slice-3
  drafting agent vocalized the fused rasm ماقتلت as 1cs مَاقَتَلْتُ ("as I killed") and translated
  it as the jinni confessing to killing his own son — but the parallel accusation at P10L15
  (same words, drafted independently by slice 1) correctly reads it as 2ms مَاقَتَلْتَ ("as you
  killed"), i.e. the jinni accusing the merchant. The bare-strip gate cannot catch this class of
  error (unvocalized rasm is identical either way; only the diacritics differ, and the gate
  strips diacritics before comparing). Caught by the review agent cross-checking the two
  occurrences' glossary entries against each other and against narrative sense. **Future runs:**
  the gate proves nothing was added or dropped, not that ambiguous unvocalized forms (a common
  class: 1cs vs 2ms perfect verbs, in particular) were read correctly — the whole-night review
  pass earns its keep here and should keep explicitly cross-checking repeated/parallel phrasing
  against itself, not just against style rules.
- **New pipeline gotcha found by the review pass: combining-mark codepoint order, not just
  precomposed-vs-combining hamza (run 2026-09-20/21, publishing Night 1).** Independently-drafted
  slices sometimes ordered a word's short-vowel and hamza combining marks differently (e.g.
  hamza-below before its vowel instead of after) — invisible to the eye, and it doesn't break the
  bare-strip gate (which just strips all combining marks), but it silently breaks *exact* glossary
  key matching: the same word can fail to match itself across slices, or fail to match an already
  existing shared-glossary key, purely on mark order. The review agent canonicalized combining-mark
  order (by Unicode combining class, never touching base letters or the 8 legitimate precomposed
  hamzas) across all "t" fields and glossary keys before merging, and this caught real would-be
  duplicate entries. **Future runs:** worth doing this canonicalization as a matter of course before
  any glossary merge, the same way the hamza-encoding rule already gets an explicit check.
- **Residual uncertain readings in Night 1, left as translated pending a second opinion (nobody
  waiting on these, recorded for completeness):** فَسَأَتُ (P13L03) appears to drop a root letter
  outright rather than just an alif/hamza-seat, read as a colloquial contraction of سَأَلْتُ; اِيتِنِي
  (P13L09/13/15, "bring me!") prints with no hamza indication at all rather than the usual bare-alif
  seat — two independent drafting agents (slices 4 and 5) converged on the same reading
  unprompted, which is reassuring but not certain; the sheikh's line "ما دينك الا دين عظيم" plausibly
  puns between دين = "debt" (echoing the merchant's literal debts) and a colloquial extended sense
  "affair, predicament" — vocalized identically either way and flagged rather than resolved;
  زَرْزُورِيَّةٌ ("dapple/starling-colored", describing the third sheikh's mule) was glossed by
  inference from the زرزور (starling) root rather than a confirmed lexicon citation. None of these
  affect the gate or the bare text; a Lane's-Lexicon check on زرزورية and فسأت would be the most
  useful next step if anyone has time.
- **Systematic hamza-encoding error, caught before gating, run 2026-09-21 publishing Night 2 — a
  pipeline gotcha future prompts should guard against explicitly.** All 5 disjoint drafting agents
  independently used precomposed hamza-on-alif/waw/ya (أ إ ؤ ئ) for editorially-supplied hamzas,
  instead of the required combining-mark encoding (base letter as the archive prints it, plus
  combining U+0654 above / U+0655 below) — hundreds of instances (e.g. "ان"→"أن" instead of
  "اٴن", "الى"→"إلى" instead of "اٍلى"). This is exactly the "looks like a bug" trap
  `reading-conventions.md` already warns about, but the drafting prompt's own restatement of the
  rule was apparently not concrete enough to stop 5-for-5 agents getting it wrong. Caught only
  because the final merge script diffed the assembled text's bare-strip tokens against the archive
  word-for-word before gating (as `validate_night.py` itself does) rather than trusting the agents'
  own self-reported verification. Fixed mechanically: every precomposed hamza letter was decomposed
  to (base letter appropriate to the archive's own printed seat) + (any interposed short-vowel/
  sukun marks, unchanged) + (the correct combining hamza mark), which is a lossless, deterministic
  transform once you know which base letter the archive prints at that position — 316 words fixed
  this way, verified to reproduce the archive exactly, token for token, afterward. A future
  publishing run's drafting prompt should probably show a worked before/after example of this exact
  transform (not just cite the codepoints), and the orchestrating run should always re-derive the
  bare-strip diff itself after merging slices rather than accepting each agent's self-report at
  face value.
- **One archived line-wrap artifact required manual rejoining, run 2026-09-21 (Night 2).** The
  archive fuses "فلما" and "كان" into one line-final token "فلماكان" (P14L19, a compositor
  spacing slip, not a Middle Arabic form) — one drafting agent correctly read it as two words but
  wrote them with a space, which the gate's token-for-token check would have rejected; fixed by
  rejoining them into one unspaced vocalised token (فَلَمَّاكَانَ) to mirror the archive's own
  (accidental) fusion, per "spelling is preserved unaltered."
- **Night 2 content uncertainties, left as translated/vocalised pending a second opinion (nobody
  waiting on these, recorded for completeness).** حَنَّ قَابُهُ (P14L12) is almost certainly
  قَلْبُهُ ("his heart [softened]") with the lām dropped — a probable compositor's slip, pointed to
  fit the printed letters rather than corrected. غَابَةَ الْعَجَبِ (P14L17/P15L02) likely
  misprints غَايَةَ الْعَجَبِ ("the utmost of wonder"), a bā'/yā' confusion — same treatment.
  هَذَا مُقَدَّرُوهَا (P16L21) matches no recognized word (مقدورها, "its fated lot," with ر/و
  transposed, is the likely intended form) — vocalised as printed. فَقَامَ فِعْلٌ (P17L04-05) is
  opaque as printed; read loosely as "so, in the end, I agreed," a guess rather than a restoration.
  الْمُسْفَرَ (P17L16, "وجهزنا المسفر") is read as an obscure non-Classical noun for "the
  journey's preparations/gear" with no confirmed parallel found. تَهَبُ لِي ثُلُثَ ذَنْبِهِ
  (P16L05) reads ذَنْب as "guilt" (paralleling the دَم/"blood" of the same bargain elsewhere in
  this frame) rather than ذَنَب "tail," which the two dogs might otherwise suggest but cannot
  sensibly mean here. وَهُوَ الذَّاهِبُ الْآخَرُ (P16L18) reads الذهب as الذَّاهِب ("the other
  one to travel," the same medial-alif-dropping spelling as ثلاثة elsewhere in this text) rather
  than as "the gold" (nonsensical for a brother); note this glossary entry folds to the same bare
  skeleton as any future entry for the ordinary word "gold" would — a genuine homograph in the
  underlying rasm, not a glossing error, worth remembering if a later night's fallback lookup ever
  looks wrong for that skeleton. فَتَعَلَّتْ بِهِمْ (P18L23) is read as "she prevailed over them"
  (root ع-ل-و) though a scribal slip for فَفَعَلَتْ ("she did [it] to them") is equally plausible.
  تَخَالُصَهُمْ (P19L01, "their release") has a grammatical role that is not fully certain from
  context. وَقٰلَ لَهَا هَذَا عَجِيبٌ (P20L01) is read with the JINNI as speaker (marvelling at
  the mule and addressing her, since she cannot answer in speech) and the following وَقُلْتُ as the
  sheikh resuming his own narration — the unpointed original would also allow a less coherent
  imperative reading. أَنْتَ طَالِبٌ (P19L21) is grammatically loose as the predicate of تَصِيرُ;
  translated by evident sense rather than regularised.
- **Pre-existing glossary issues found while drafting Night 2, not this night's to fix but worth a
  look.** `nights-glossary.json`'s entry for وَلَّى was wrong ("to turn away, decline, depart") and
  has been corrected in this run to "to appoint, install in office," per Night 1's own note on the
  identical idiom وَلَّى وَعَزَلَ ("appointed and dismissed") — a clear case of "the existing entry
  is actually wrong," fixed deliberately per the glossary rule. Left untouched, flagged for a future
  pass: the entry for وَجْهَهَا bakes in a one-off euphemistic reading ("her maidenhead") that does
  not fit this night's own plainly literal use of the same vocalised form (a daughter covering her
  actual face); the entry for مَا characterises mā + perfect negation as "a Middle Arabic usage
  where Classical prose has lam," when mā + perfect is itself good Classical Arabic (e.g. Qur'anic
  mā kadhaba al-fu'ād); the entry for أَرْسَلَتَ ("you sent," 2ms) appears mis-vowelled — a 2ms
  perfect of form IV should have sukūn on the lām (أَرْسَلْتَ); and the entry for اَمَا
  (interrogative "did I not…?") shares a bare skeleton with this night's own أَمَّا ("as for…"),
  so a reader relying on the bare-fold fallback for the latter would currently see the wrong gloss.
  None of these affect this night's own gate.
- **Rubric display flag used for the first time, publishing Night 3 (2026-09-21).** The edition's
  own section heading at P20L17 (حكاية الصياد, transcribed with `"h": true`) is rendered in
  `nights-03.json` as its own sense unit with both `"r": true` (rubric styling — a CSS class
  reader.html already defines, `.sent.rubric`, but which no published night had ever actually set)
  and `"p": true` (paragraph start). The one earlier precedent, `nights-frame-02.json`'s heading
  for حِكَايَةُ التَّاجِرِ وَالْجِنِّيِّ, used only `"p": true`, leaving the heading in the
  ordinary text color. Reading reader.html's own code, `"r"` exists for exactly this case and
  seems like the more complete, intended rendering (distinct color for a section title, like a
  chapter heading) rather than an oversight to imitate. Decided to set both flags on Night 3's own
  heading rather than match the frame's incomplete precedent. **Not touched:** whether
  `nights-frame-02.json`'s own heading should retroactively gain `"r": true` too, for visual
  consistency across the library — that file is out of this run's scope (a publishing run may
  touch only its own night), and it is a purely cosmetic question with no gate impact. Worth a
  look if anyone reads the two side by side and finds the inconsistency jarring.
- **Likely compositor's slip, publishing Night 3 (2026-09-21): P24L19's اعتقتك.** The efrit's line
  "فقال العفريت لما اعتقتك وانا ما اقتلك الا لاجل ما خلصتني" prints اعتقتك unambiguously, on its
  bare consonants alone (not just an unvocalized ambiguity), as أَعْتَقْتُكَ — "I freed you"
  (1st-person subject, 2nd-person object). This inverts the logic the passage plainly needs: the
  efrit is explaining why he now kills the very man who just freed *him* from the jar (the
  sentence's own second verb, خَلَّصْتَنِي, "you delivered me," is grammatically sound and gives
  the true sense, and the logic — killing your rescuer precisely because he rescued you — is the
  same bitter point the Umm ʿĀmir proverb makes two units later). This reads as the same class of
  error already on record for other nights (a swapped pronoun/object suffix, compare Night 2's
  حَنَّ قَابُهُ for قَلْبُهُ). Per the rule, the archive was not touched: اعتقتك is vocalized
  exactly as printed (أَعْتَقْتُكَ) in `nights-03.json`, but the translation renders the sentence
  by evident sense (the efrit kills him *because* he was freed), with a note explaining the
  discrepancy for the reader. Flagging here in case a future pass over the page image itself wants
  to double-check whether the print truly shows ك rather than a hard-to-distinguish ني.
- **Style seams found by the whole-night review pass, publishing Night 3 (2026-09-21), left
  unfixed this run — not correctness issues, logged for a future normalization pass.** (1) The
  `tr` layer shows a systemic split: roughly the first two of five drafting slices (idx 0-39)
  consistently transliterate a sentence-final word's short case/mood vowel in full (waṣl style,
  e.g. `al-arḍi`), while roughly the last three slices (idx 40-100) mostly drop it (waqf/pausal
  style, e.g. `al-qumqum`), with a handful of exceptions in both directions. Both styles are
  linguistically defensible on their own, but mixed within one file it is a visible seam. (2) The
  literal (`l`) layer shows a three-way shift in dialogue-reporting convention across the same
  five slices: natural word order with bare-colon speech (idx 0-19) → heavily hyphenated,
  Arabic-word-order calque with quotation marks (idx 20-79) → natural word order with quotation
  marks (idx 80-100). Read closely at all four slice-boundary seams (idx 19/20, 39/40, 59/60,
  79/80) for narrative continuity — no dropped content or repetition at the story level, so these
  two items are presentational only. Recommend a future pass pick one `tr` vowel convention
  (probably always-full, matching the "complete tashkīl" ethos) and one `l`-layer dialogue
  convention, and normalize retroactively; not attempted this run given the number of individual
  units it would touch and the risk of introducing a real error while chasing a style fix under an
  unattended run's own time budget.
- **Several individually-uncertain readings in Night 3, translated by evident sense and flagged in
  their own notes (nobody waiting on these, recorded for completeness).** فَوَجَلَ (P21L04, "he
  found," expected root و-ج-د) is a non-standard spelling kept as printed. هَيَا (P21L13, an
  interjection before "لا بل من كرامة") has no confident resolution. عِفْرِينًا (P23L10, with ن
  rather than the usual عفريت) is read as a genuine variant form Lane records related augmented
  roots for (عِفْر, عِفْرِيَة). بِزَوَالِ السِّتْرِ عَنْكَ (P23L21, the fisherman's curse back at
  the efrit) is translated as an idiom for ill fortune/exposure, not confidently sourced. مَلِيًّا
  in "أَصْنَعُ مَعَكَ مَلِيًّا" (P24L21) does not parse cleanly against its ordinary senses
  ("a long while" / "one of substance") and is read as a non-standard variant of the "do a good
  turn" idiom. شَيٍ (P25L08, "a thing") prints with no hamza seat at all, not just a missing hamza
  sign — a colloquial spelling, vocalized on its two printed letters alone. None of these affect
  the gate.
- **Publishing Night 4 (2026-09-21/22): a legacy glossary-key inconsistency found, not touched.**
  The shared glossary already carries two keys for the same preposition: `إِلَى` (with the
  combining hamza U+0655, per the house rule, and used by nearly every night since) and a lone
  `اِلَى` (no hamza mark at all), the latter's own gloss noting it was "printed without the hamza
  sign" — apparently a one-off decision from the pilot, before the hamza-encoding rule was fully
  settled. Night 4's new entries all use the standard `إِلَى` form; the stray `اِلَى` key was left
  as-is (touching `nights-frame-01.json`, which uses it, is out of this run's scope) but is worth
  a dedicated cleanup pass: either retire the unmarked key in favor of the marked one, or confirm
  the pilot's specific occurrence genuinely differs and document why.
- **Publishing Night 4: an archive line-break artifact, worked around rather than fixed.** At the
  P29L02/P29L03 boundary the archive tokenizes "والانعام" ("and the bounty") as two separate
  tokens — a lone `و` ending one printed line, `الانعام` starting the next — rather than as the
  single glued word Arabic orthography requires. This has the shape of the "detached wāw" defect
  the transcription LOG mentions catching and reattaching several times elsewhere (e.g. p.19,
  p.51); this particular instance apparently weathered phase 1's two-pass-plus-adjudication
  unflagged. Per the publishing runbook, the archive itself was not touched; the published
  vocalised text instead reproduces the same two-token split (a visible mid-word space in
  `nights-04.json`) so the bare-strip gate matches token-for-token. Worth a transcription-side
  look at whether this is a genuine detached-wāw miss that should be corrected in the archive
  proper, which would let Night 4's text rejoin the word normally.
- **Several individually-uncertain readings in Night 4, translated by evident sense and flagged in
  their own notes (recorded for completeness, nobody waiting on these).** "ورمق البارد كمه وحضم"
  (P26L03) resists confident parsing on either البارد or حضم (neither confirmed against
  Lane/Hava); vocalized and translated by best-effort sense. "نبرئني" (P27L09) is printed with an
  initial ن where the dialogue plainly wants a 2nd-person verb ("will you cure me?"); kept as
  printed. "دون" (P30L03) almost certainly truncates "دوبان" (Duban), most likely a compositor's
  dropped syllable; kept as printed rather than silently expanded. "غايه الغرب" (P30L01) sits
  oddly beside "غايه الاكرام" a few words earlier; no confident emendation offered. "دبنارا"
  (P29L02, for "دينارا"/dinars) and "ملى" (P29L05, for "مدى") both read as probable printer's
  letter-substitutions, reproduced exactly as printed. "سرت"/"سرى" (P28L03) disagree in gender for
  the same subject الدواء within a few words of each other; both vocalized as printed rather than
  harmonized. None of these affect the gate.
- **Publishing Night 5: drafting agents' own "verified mechanically" claims did not hold up, and
  the run had to redo the hamza encoding wholesale before the gate would pass.** All five drafting
  agents reported checking the bare-strip identity themselves and finding zero mismatches; on
  reconstruction, the whole night in fact had 1224 of 1798 tokens wrong, because every agent had
  vocalized hamza with the ordinary precomposed letters (أ إ ؤ ئ) — which look identical to the
  correct combining-mark encoding in any terminal or editor, so a human or model eyeballing the
  text cannot tell them apart, and only look different at the codepoint level tools/validate_night.py
  actually checks. Fixed by token-aligning every sentence against the real archive text and
  rewriting each mismatched word programmatically (273 word-level hamza fixes, 22 places where a
  word had to be split back into two — see next item — plus the same correction propagated into
  new glossary keys, since a duplicated word could legitimately need different fixes at two
  positions where the edition itself spells it two different ways, e.g. "ابرأك" vs "ابراك" for
  "he cured you", both real, both kept distinct). Net: the gate passed clean, but a "the agent
  says it verified" claim about hamza encoding specifically should never be trusted without an
  independent mechanical recheck — visual inspection cannot catch this class of error at all.
  Worth adding a line to the drafting prompt/runbook making this failure mode explicit.
  **Acted on 2026-09-22 (owner's instruction):** the check is now a script, not a claim.
  `tools/check_slice.py` runs the bare-strip identity on each slice as it returns, repairs the
  hamza/split/join classes mechanically with `--fix`, and reports anything else; publish-runbook.md
  4a makes it a condition of merging a slice, and drafters are no longer asked to verify anything.
- **Publishing Night 5: the archive prints a bare "و" as its own space-separated token before its
  host word at roughly 22 points across P30L10–P38L01** (e.g. "و هو", "و قال", "و قتله", "و اطلبه"),
  far more than the single instance Night 4's QUESTIONS entry flagged. Per the bare-strip rule the
  published text must reproduce this exactly rather than joining the proclitic the way ordinary
  Arabic orthography would, so nights-05.json keeps a handful of sentences with a visible mid-word
  space (e.g. "وَ قَالَ", "وَ اطْلُبْهُ") to match; the corresponding glossary entries were split
  into two (the bare وَ plus the following word on its own) wherever this happens, rather than one
  fused key, so glossary coverage still resolves. Given how frequent this is turning out to be
  across nights, it looks like a real, recurring transcription-pipeline artifact (not a one-off)
  and is worth a dedicated pass on the phase-1 side to see whether it is a systematic OCR/line-join
  defect that should be fixed in the archive itself.
- **Two genuinely uncertain readings in Night 5, flagged for the transcription side rather than
  silently resolved.** اِنْشَلَّ (P37L15-16, "...حاق في الدواء انشل الحكيم دوبان يقول") is form VII
  of ش-ل-ل ("to become paralysed"), which does not fit as the verb governing "the sage Duban...
  saying" that follows; this tale elsewhere introduces recited verse with وَأَنْشَدَ...يَقُولُ, and
  انشل/انشد differ by only their last letter (ل vs د), so it is read and translated as أَنْشَدَ
  ("he recited") while the letters are reproduced exactly as printed. لا ابقاك (P38L01, closing
  "...وانت ايها العفريت لو ابقيتني لا ابقاك الله") is printed with a word-space, which read
  literally negates ("God did not spare you") — but the parallel sentence three words earlier
  fuses the identical law...la- construction as one word (لابقاه = لَأَبْقَاهُ, "He would have
  spared him"), and this line is generally read as its positive mirror ("had you spared me, God
  would have spared you"). Published as the literal negated reading, per "the images are the only
  authority" and not silently emending; worth checking the scan directly for whether that space is
  really there, since the two readings are opposite in polarity. Neither affects the gate.
- **Several individually-uncertain readings in Night 5, translated by evident sense and flagged in
  their own notes (recorded for completeness, nobody waiting on these).** أَمِيرُ الرَّخَةِ
  (P30L20, an officer announcing the hunt) has no confirmed sense for الرخة in Lane or Hava.
  قَيَالَةٍ (P31L10, "the hour of ___") is read as a Middle Arabic/dialectal form of قَيْلُولَة,
  "midday rest". النَّفْطَ (P31L14, describing the poison dripping from the tree) may be a ف/ق
  misprint for النُّقْطَة, "the drop". مَاذَا ذَا (P31L04, a doubled interrogative) is kept as
  printed, likely dittography. سِلْسِلَة (P37L02, "a chain in which was some powder") is an odd
  vessel for powder, possibly a compositor's error for a word like سُلَّة, "basket". حَارَ
  الدِّيوَانُ (P36L23, "the council-hall was dazzled/bewildered like the flower of the garden")
  is vocalized on its ordinary sense rather than a suspected corruption of زَهَا, "to be
  resplendent", which would pun with the following كَزَهْرِ. اِبْرِطِيلٍ (P36L09, "a bribe") is
  read as a colloquial/dialectal spelling of Classical بِرْطِيل. None of these affect the gate.
- **check_slice.py's align() can corrupt a legitimate precomposed hamza when the same word also
  needs a detached-waw line-split fix (run 2026-09-22, publishing Night 6).** One drafting agent
  wrote وَالْتَأَمَ ("and it closed up") fusing the line-break's detached وَ onto التأم — but
  التأم's own تأم root carries a hamza the *edition itself prints* (precomposed, kept per the
  rules). check_slice.py's fused-token branch always calls decomposed() on the whole word before
  trying to split it against the archive's two tokens ("و" + "التأم"); decomposed() blindly maps
  precomposed أ to a base-alif+combining-hamza sequence even when that أ was already correct, and
  bare()'s strip regex then deletes the resulting combining mark entirely (it's in the same
  diacritic range as tashkīl) — so the fused-match check compares against a hamza-less string and
  fails, leaving the word unfixed and desyncing every following token in the diff (a single failed
  word produced ~75 cascading FAIL lines). Decided meanwhile: fixed by hand — rewrote the word as
  وَ الْتَأَمَ (space at the archive's own line-break boundary, precomposed hamza in التأم
  preserved), matching the "wa- as its own printed token" precedent already established for Night
  5. **Future runs / whoever next touches check_slice.py:** the align() fused-branch should try
  the *undecomposed* word against the archive concatenation first (db = bare(w), not
  bare(decomposed(w))) and only fall back to decomposed() if that fails — right now it always
  decomposes first, which is correct for a word that needs a hamza *added* but wrong for a word
  that already has the archive's own precomposed hamza and merely needs re-splitting at a line
  break. Not fixed this run (publishing runs don't touch tools/ per scope; flagging for whoever
  next works on the script).
- **One slice "corrected" the edition's defective قل to full قَالَ instead of the house dagger-alif
  convention (run 2026-09-22, publishing Night 6).** P40L02/03 prints قل for قال (the same
  recurring defective spelling as every other قل in this text, e.g. Night 1-3's own instances).
  The drafting agent for that slice spelled it قَالَ (full alif, matching the archive's *other*,
  differently-spelled فقال two lines earlier) rather than قَٰلَ (dagger alif over the qāf,
  preserving the two-letter rasm) — caught by the gate's bare-strip check, since قَالَ strips to
  "قال" (3 letters) not "قل" (2). Fixed by hand to match the established convention (see
  nights-01/02/03's own instances of the same defective spelling) and renamed the glossary key to
  match. **Future drafting prompts:** the worked example given to agents shows the *rule* for
  dagger alif but not a concrete before/after transform the way the hamza rule now gets one —
  worth adding one, since this is the same class of "looks right, isn't" mistake as the hamza trap.
- **Two genuinely uncertain readings in Night 6, left flagged rather than resolved (nobody waiting
  on these, recorded for completeness).** عَائِكَة (P38L08-09, "امانة مع عائكة") does not match any
  confirmed word in Lane or Hava; read on its printed letters as if a proper name (ʿĀʾika) in a
  proverb about a kindness repaid, but the fisherman's own in-story reply ("what did I ever do
  with ʿĀʾika?") suggests it may already have been unclear at the story level, not just to this
  pipeline — worth a second look if the phrase recurs elsewhere in the volume. The second
  fish-verse's وَاِنْ هَجَرْتُمْ قَدْ فَانَا تَدْفَيْنَا (P41L16) differs from the first verse's
  parallel وَاِنْ هَجَرْتِ فَاَنَا قَدْ تَهَافَيْنَا (P40L21) in both person/number (هَجَرْتِ vs
  هَجَرْتُمْ) and the final rhyme word (تَهَافَيْنَا "we would have perished/rushed together" vs
  تَدْفَيْنَا, which does not parse as cleanly) — reproduced exactly as the archive prints it
  (already pointed, not re-derived), translated by the same general sense as the first verse, and
  flagged as a probable compositor's rearrangement rather than silently normalized to match.

- **Drafting agents re-vocalizing already-pointed verse words, invisible to check_slice.py (run 2026-09-23, publishing Night 8).** `conventions.md` states Calcutta II's verse is transcribed with its own printed marks ("nothing is normalised, repaired, vocalised or emended"), so a verse line's archived `t` is already the final, authoritative vocalisation — there is nothing for a drafting agent to add, unlike prose. The drafting prompts for this night did not make that distinction explicit and instead told agents to supply full tashkīl on their whole slice; several agents dutifully re-vocalized already-marked verse words — in three of the night's 7 verse blocks this took the specific form of rewriting the archive's own correctly-encoded combining-mark hamza (ا + U+0654/0655) as precomposed أ/إ, i.e. exactly the hamza trap, just applied to text that was already correct. Because both encodings strip to the same bare alif, `check_slice.py` and `validate_night.py`'s bare-strip identity cannot catch this — it passed clean both times. Caught only by a manual word-for-word diff of each verse sentence against the raw archive. Decided meanwhile: rebuilt all 7 verse blocks word-by-word, keeping the archive's own word (marks and all) wherever it carried any diacritic at all, and accepting a drafting agent's vocalisation only for a word genuinely bare in the archive (Night 8 had exactly one such case: the second hemistich of P53L01, plus a handful of unmarked final consonants in P53L02 that were left as the archive has them, not "completed" with an inferred sukūn). **Future runs / whoever next touches the publish-runbook or its prompts:** the drafting prompt should say explicitly that verse `t` is copied from the archive verbatim (only the hemistich " * " / line "\n" joins are the agent's own work) and is never re-vocalized, the same way the runbook already says the consonantal text is never touched — this should also fold into a verse-specific check in `check_slice.py`/`validate_night.py` (e.g. flag any verse-flagged sentence whose word skeleton, WITH diacritics, differs from the archive on a word the archive already marks) so this class of bug is caught mechanically rather than by hand next time.
  **Acted on 2026-09-23 (attended session, at the owner's request).** The drafting prompt now carries a fixed verse sentence (publish-runbook.md step 4) and reading-conventions.md has a section "Verse is copied, not vocalised". `check_slice.py` and `validate_night.py` now compare every pointed verse word with the archive codepoint for codepoint; `check_slice.py --fix` puts the archive's word back. Run over every published night: Nights 1, 3, 5, 6, 7, 8 clean; Night 4 had 4 verse words with a hamza the edition does not print (P28L12 اَبَا, اَبَى; P28L13 اَنْوَارُهُ; P28L15 اَوْلَيْتَنِي) — restored to the archive's words in nights-04.json; nothing else in the file changed. Closed.

- **`check_slice.py`'s `decomposed()` step corrupts an already-correct precomposed hamza during
  fused-word repair (found 2026-09-23, publishing Night 9).** `align()`'s fused-word branch (a
  drafter wrongly glued a detached و onto its host word) calls `decomposed(w)` on the *whole*
  candidate word before testing whether it splits cleanly against the archive. `decomposed()`
  unconditionally rewrites every precomposed hamza character (أ/إ/ؤ/ئ/آ) into the decomposed
  combining form, with no check for whether the word's hamza was already correct as printed. For
  a word that is *only* wrongly fused (no hamza problem at all) this is harmless, since the
  rewritten and original hamza strip to the same bare letter either way — except when the word's
  hamza is one of the cases reading-conventions.md says to keep *precomposed*, because the edition
  itself prints it that way (e.g. خزائن in this night, one of the pilot's own seven listed
  exceptions). There, `decomposed()` turns ئ into a *different* bare letter after stripping (ي
  instead of ئ, since bare() strips the combining hamza mark U+0654 but not the standalone letter
  ئ), so the split-match against the archive silently fails and align() falls through to
  `problems.append(...)` instead of repairing — and because align() still advances both cursors
  by one on a problem, every token after that point in the slice is now off-by-one and reads as a
  cascade of unrelated "FAIL token N" mismatches, even though the only real defect is the one
  fused word. Root-caused this run by hand-tracing `align()`/`decomposed()`/`bare()` against a
  failing slice (see LOG); worked around by manually splitting the one culprit word before
  re-running `--fix`, which then cleaned up the rest once the cursors resynced. Not fixed in
  `tools/` this run (publishing runs don't touch `tools/`, and the gate's scope rule — `git diff
  --stat` shows only the archive/story files plus pipeline records — held even for an attended
  fix in the Night 8 verse case above, so this should go through the same kind of dedicated pass,
  not get folded into a publishing run's diff). **Whoever next touches `check_slice.py`:** the fix
  is to only call `decomposed()` on the *specific sub-piece* that fails a direct match, after the
  split points are already known — or, simpler, to try the fused-match first with `w` as printed
  and fall back to `decomposed(w)` only if that specific attempt fails — rather than decomposing
  the whole candidate word unconditionally up front. Worth a regression test using خزائن or a
  similar precomposed-hamza-plus-fusion case, since the two-encodings-render-identically problem
  that makes the *drafting* side of this trap invisible also made it easy to overlook on the
  *tooling* side.
- **A word can be both a genuine detached-waw error at one position and genuinely archive-fused
  at another position, in the same night (found 2026-09-23, publishing Night 9).** When hand-
  repairing the cascade above, and separately when cleaning up `check_slice.py --fix`'s glossary
  WARNs on two other slices, the fix was applied by renaming the glossary key for *every* instance
  of a bare word form (e.g. وقالت، وفي، وتجردت) from its fused spelling to its split spelling —
  without checking whether some other occurrence of that same bare form elsewhere in the slice was
  *correctly* fused as printed (the archive is not internally consistent about spacing this
  conjunction, occurrence by occurrence). This orphaned the glossary key for the still-fused
  occurrences, caught only at the final `validate_night.py` gate's glossary-coverage check (5
  words: وصارت، وتجردت، ولعبت، وأشارت — each verified against the raw archive line before being
  restored as its own glossary entry alongside the already-corrected split form). **Future runs:**
  after any manual or scripted glossary key rename during slice-fixing, re-run the missing/extra
  key diff against the *actual* text before moving on, rather than trusting that a bare-form
  rename is safe everywhere it appears.
