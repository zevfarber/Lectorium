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
