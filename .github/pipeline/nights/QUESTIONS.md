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
- **apply_verdicts.py's hardcoded PDF-18 offset (recurring since run 2026-09-17 pp. 47-54, still
  recurring as of run 2026-09-27 pp. 135-142).** The committed tool still assumes printed =
  PDF-18 throughout; every run since the pp. 47-54 offset discovery has worked around this with
  a locally-patched copy (never committing the change, since the runbook's gate step expects
  `git diff --stat` to show only the archive plus claim/LOG/plan). The offset has now held for
  every run from PDF 50 through PDF 142 (confirmed again this run by the p.135 header read,
  "١١٥"), roughly a dozen runs and counting. Left the tool as-is again this run, consistent with
  precedent and the gate's scope rule (the patch lives only in a `/tmp` copy, never touching the
  repo), but this is well past "one-off anomaly" at this point — worth Zev fixing the constant
  properly (or making it a `--offset` argument like `nights_ocr.py` already has) rather than
  every future run re-discovering and re-patching the same line.
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


- **A drafting slice cut exactly at a sentence boundary the archive doesn't share can orphan a fragment (found 2026-09-24, publishing Night 10).** Slice 2 was bounded at P66L10–P68L02 and slice 3 at P68L03–P69L13, a clean archived-line boundary as the runbook requires — but the Arabic *sentence* زالخليفة وجعفرا ومسرور [...] ثم أنهم جلسوا للشراب actually straddles that line break (the clause continues past P68L02's last word نعم into P68L03's جلسوا). Slice 2's agent correctly noticed its slice ended mid-sentence and wrote the two dangling words (ثم انهم) as their own sense unit rather than inventing an ending, exactly as instructed — but slice 3 was never told it was inheriting an unfinished clause, so it started its own first sentence fresh at جلسوا, dropping the subject. Both slices passed check_slice.py cleanly (the bare-strip identity doesn't care how sentences are cut, only that the tokens are right), so this was only caught by reading the assembled night in order. Fixed by merging the two into one sentence by hand. **Future runs:** when a slice boundary falls mid-sentence (it will, since slices are cut on archived-line boundaries, not sentence boundaries), check the last sense unit of each slice against the first sense unit of the next slice for exactly this seam before assembling — the mechanical gate cannot see it.

- **`nights_index.py --text` silently drops the archive's `v` (verse) flag on every line (found 2026-09-24, publishing Night 11).** `load_lines()` (used by both `build()` and `--text`) reads each archived line as `line.get("t", "")` only — it never carries `line.get("v")` through. So `python3 tools/nights_index.py --text <night>` hands back every line as plain, unmarked text, even where the archive marks it `"v": true`. This night has 4 verse blocks (13 lines) in the P73L19–P79L11 range; had I handed the `--text` output straight to the drafting agents as the runbook's step 2 literally directs, every verse word would have been treated as ordinary prose and fully re-vocalized — exactly the trap `reading-conventions.md`'s "Verse is copied, not vocalised" section and the 2026-09-23 Night 8 incident already warn about, just introduced one step earlier and by the orchestrator's own tool rather than a drafting agent. Caught only because I diffed `--text`'s output against the raw `archive/pp*.json` files by hand before drafting and noticed the verse lines had lost their tag. **Decided meanwhile:** built the night's dataset directly from `archive/` (preserving `v`) instead of using `--text`, and gave each drafting agent's slice its verse lines pre-tagged. `check_slice.py`/`validate_night.py` were unaffected since they read `archive/` directly, not `--text`'s output, so the mechanical gate still would have caught a re-vocalized verse word eventually — but only after a full drafting pass had to be redone. **Whoever next touches `nights_index.py`:** `load_lines()` should return `(ref, t, v)` (or the whole line dict) instead of `(ref, t)`, and `--text`'s output should carry `"v": true` on marked lines the same way `archive/pp*.json` does, so a future run's drafting agents get accurate input without the orchestrator having to route around the tool by hand. Not fixed in `tools/` this run (publishing runs don't touch `tools/`, per the same scope rule noted in the Night 9 `check_slice.py` finding).

- **Same `nights_index.py --text` v-flag bug recurred (2026-09-24, publishing Night 12), still
  unfixed.** Second occurrence of the finding directly above. Worked around the same way: built
  the night's line data (with `v`) straight from `archive/pp075-082.json` and `archive/pp083-090.json`
  rather than trusting `--text`. This is now confirmed to hit every publishing run with a verse
  passage, not a one-off — worth a transcribing run (which is allowed to touch `tools/`) picking
  up the one-line fix described above rather than leaving each publishing run to route around it
  by hand.
  **Fixed 2026-09-25 (attended session, at the owner's request).** `--text` now reads each
  archived line's full record and carries `"v": true` wherever the archive sets it; the table,
  `--next` and the night boundaries are unchanged (output checked identical). Checked on Nights 1,
  5 and 12: 8, 20 and 10 verse lines now tagged, text identical. Publishing runs can use `--text`
  as the runbook says. Closed.

- **Ambiguous grammatical person on `اِحْتَاجَ`, P82L19 (publishing Night 12).** بِمَا احْتَاجَ إِلَيْهِ
  ("with what was needed"/"with what he needed") is printed with the unambiguous 3ms perfect
  consonant skeleton (rules out a 1cs reading, which would need a final ت). Kept as 3ms, read as
  an impersonal relative clause ("what was needed") rather than assuming the narrator misspoke;
  flagged in the sentence's own note rather than silently resolved.

- **A genuine scan-corruption defect, PDF page 114 / printed p. 94 (run 2026-09-25, transcribing
  pp. 111-118).** `nights_ocr.py`'s automatic line detector returned only 1 "body line" for PDF
  page 114 (all other 7 pages in the batch detected normally), and rendering the page at any DPI
  via three independent tools (`pdftoppm`/poppler, PyMuPDF, `mutool`) all reproduced an identical
  chaotic "shredded"/checkerboard visual artifact over a large area of the frame. Traced to the
  page's embedded image objects directly with `pikepdf`: the page composites a full-page JPXDecode
  (JPEG2000) color background (`fzImg1`) with a JBIG2Decode 1-bit `SMask` acting as the text/ink
  layer. Extracting and decoding *both* streams independently (`pdfimages`, `jbig2dec -e`) showed
  the *same* chaotic pattern occupying the *same* region in both — independently-encoded formats
  sharing an identical defect geometry rules out a single codec's decode bug and points to damage
  in the master scan image both streams were derived from. The affected region turned out to sit
  entirely in the exterior background/book-cover area *outside* the actual printed leaf (confirmed
  by checking, at several rows, that no real ink extended into it — a verse-couplet block on this
  page that looked "indented" at first glance was cross-checked against a second couplet on the
  same page with an identical right-margin start, showing the indent is this page's own
  block-quote layout for its calligraphy specimens, not lost text). Decided meanwhile: cropped the
  exterior region out (`x < 1290`, `y > 460` on the 1619×2804 render) before generating this page's
  `band1-3.png` (plus a `band3_bottom.png` for the last two lines near the frame edge), so the
  correction-pass agents worked from clean, complete images with an explicit note explaining why no
  `lineNN.png` crops existed for this page; both independent passes converged on the same 17-line
  reading with only ordinary-rate disagreements, and both page joins into/out of p.94 read
  continuous — corroborating that nothing was actually lost. **Future runs:** if `nights_ocr.py`
  reports a wildly low body-line count on an otherwise-normal page, don't assume the batch is
  unrecoverable or stop the run — render the page with 2-3 different tools first (identical output
  across tools rules out a rendering bug and points to the source PDF itself); if the artifact
  region turns out to be entirely outside the actual leaf (checkable by comparing against a clean
  neighboring page's known text/margin extent), the fix is just a manual pre-crop before band
  generation, not a lost-text situation. `raw.githubusercontent.com` (used here to re-fetch
  `arabest.traineddata` for an unrelated retrain attempt) and other GitHub-hosted raw-content hosts
  are reachable through this environment's network policy even though most external hosts are not
  — worth knowing if a future run wants to verify a suspect local PDF chunk against a fresh copy,
  though archive.org itself was NOT reachable when tried (403 from the outbound proxy), so a
  genuinely corrupted *source* chunk (unlike this run's exterior-only defect) cannot currently be
  re-verified against the original archive.org scan from within this environment.

- **`apply_verdicts.py`'s two known verdict-application gaps both recurred this run (2026-09-25,
  pp. 111-118): the silently-dropped word-insertion verdict (empty `pass1` text) and, new to this
  run, a matched pair of one insertion + one deletion verdict on the same disputed hemistich-break
  mark that between them left a bare double space.** Five insertion verdicts had empty `pass1`
  text this run (p112 "ما", p114 "بنه"/"ش"/the "*" hemistich mark, p118 "ابلق") and all five were
  silently skipped by `apply_verdicts.py` exactly as the pp.103-110 run's QUESTIONS entry
  describes; caught by the same by-hand audit that entry recommends (grep `verdicts.json` for
  falsy `pass1` with a non-empty `verdict`) and inserted by hand into the assembled archive after
  `apply_verdicts.py` ran, not before (the tool has no insert-into-already-applied-text path, so
  this was a direct string edit against the output archive). The hemistich-mark case (P94L14) was
  a genuine word-reorder in miniature: the adjudicator moved the `*` divider from between
  "وحكمت"/"فينا" to between "بالفراق"/"وحكمت", expressed as a deletion verdict (`pass1: '*',
  verdict: ''`) plus an insertion verdict (`pass1: '', verdict: '*'`) at the same line — the
  deletion applied via the tool's ordinary substring-replace and left a double space where the `*`
  had been, and the insertion was silently dropped per the bug above, so the line needed both a
  double-space collapse and a hand-inserted `*` at the correct position. **Future runs:** after
  `apply_verdicts.py` runs, in addition to the existing empty-`pass1` grep, also grep the finished
  archive for `'  '` (double space) as a general symptom of *either* known bug (a dropped insertion
  or an applied deletion) rather than assuming a double space always means the reorder case
  specifically — this run's single double-space hit only revealed the deletion half of a paired
  insert/delete; a batch with double spaces but no matching low/medium-confidence hemistich note
  nearby would need the same manual detective work the pp.87-94 run's word-reorder case describes.

- **A detached prefixed-و that both independent passes agreed on again recurred, entirely within
  page 114's later companion page 118 / printed p. 98 (run 2026-09-25, pp. 111-118).** As in the
  pp.87-94 and later runs, `diff_passes.py` cannot flag a detached-waw slip both passes made
  identically, since it only reports *disagreements*. This run's proactive full-archive `\bو \S`
  sweep (now standard per the pp.95-102 run's process note) found 18 such lines, all but one on
  PDF p.118/printed p.98 alone (the page with the shape-shifting sorcery duel) — swept and
  reattached after gating, per precedent. Consistent with the standing observation that this is a
  systematic habit of the drafting/correction agents rather than a one-off, and worth the same
  periodic regex sweep on every future batch regardless of dispute count.

- **Night 13 (published 2026-09-25): "الفرنجي الثاني" ("the second Frank") where "العفريت" (the
  efrit) is contextually expected, P86L03.** The archive (already gated PASS at transcription,
  pp083-090.json) reads "...قال للصبية يا سيدتي لها رقصت القبة رقصا قويا الا والاقطار قد اظلمت..."
  introduced by "ان الفرنجي الثاني قال للصبية" — but every surrounding sentence is plainly about
  the efrit Jirjīs returning to the vault, and "العفريت" is what the next few lines actually call
  him. No modern edition was consulted to resolve this (out of scope for this pipeline), so it is
  translated literally as printed ("the second Frank[ish man]") with a note flagging the oddity,
  per the no-repair rule — decided meanwhile: treat it as the same referent as "العفريت" a few
  sentences later, since nothing else in the passage introduces a second character. Worth a look
  by anyone with access to another independent transcription/edition of this passage, since it
  reads like either a compositor's slip in the original print or (less likely, since the
  transcription pipeline's two-pass-plus-adjudication already checked this page) a transcription
  artifact — but the pipeline has no way to distinguish those without consulting another source,
  which the rules forbid for wording. Left as printed in nights-13.json's sentence 1 note; not
  escalated further since nothing here blocks publication and the owner does not read code.

- **A non-dictionary word kept as printed, P99L01 and P99L05 (transcribing pp. 119-126,
  2026-09-26): "تلارت" where "تدارت" ("[a grain] scattered/rolled about") would be the
  sense-fitting word.** Context: "ذلك الحب حتى لم يترك ولا حبة فبالامر المقدر تلارت حبة في ..."
  (the rooster picks up every grain of pomegranate seed the ifrit's fire scattered, but by fate
  one grain rolls/scatters out of reach — the grain Sitt al-Husn later becomes to fight the ifrit's
  fish-form). Both independent transcription passes and the adjudicator read the second letter as
  an unambiguous tall-stroke lam, not the low dal-hook seen elsewhere on the same page (e.g. in
  الدخان) — a genuine letterform difference confirmed by zoom on both instances, not just a
  low-confidence guess. "تلارت" is not a standard root; left as printed rather than "corrected" to
  "تدارت", per the no-repair rule — this is very likely a compositor's slip in the original 1839
  print (a single dal/lam mistake repeated because the compositor set both occurrences from the
  same mental read, or copied one from the other), since both occurrences on the page share the
  identical error. Worth a look if anyone ever has access to another edition of this passage, but
  not escalated further since the reading is unambiguous from the scan itself and nothing here
  blocks the archive gate.

- **Night 14 (published 2026-09-26): title convention for a night whose text straddles two
  separate tales.** Every night published so far has stayed within one tale, so `title`/`titleEn`
  could just name that tale (adding ", continued" in English when picking up mid-tale). Night 14
  is the first exception: it finishes the Second Qalandar's tale (53 of its 90 sense units) and
  opens the Third's (the remaining 37) in the same night, with no clean tale-boundary between
  nights. Decided meanwhile: titled it "خِتَامُ حِكَايَةِ الْقَرَنْدَلِيِّ الثَّانِي وَبِدَايَةُ حِكَايَةِ
  الْقَرَنْدَلِيِّ الثَّالِثِ" / "The End of the Second Qalandar's Tale, and the Beginning of the
  Third's", naming both rather than picking one. No rule in `reading-conventions.md` covers this
  case; worth the owner's eye if he wants a different convention for future nights that split
  across tales the same way (this text has several more embedded tales coming, so it will recur).

- **Night 14: `زَادَ` extended to a two-sense homograph entry in `nights-glossary.json`.** The
  shared entry only covered the verb sense ("zāda, to increase"). This night's own occurrence
  (P103L09, "زاد شهر كامل", "a whole month's provisions") is the unrelated noun "zād, provisions"
  in its bare/indeterminate form. Rather than overwrite the existing entry (forbidden) or leave
  the key unresolved, extended it in place to name both senses and let context decide — the first
  genuine homograph collision hit in this glossary. Worth a look if the reader's glossary lookup
  ever needs to disambiguate homographs more visibly than one entry that just lists both meanings.

- **A second confirmed لام/دال compositor substitution page, P111 (PDF 131, run 2026-09-26 pp.
  127-134) — and an adjudicator error caught before finalizing.** Five words on this one page
  (P111L02 twice, L08, L12, L17) were disputed between a pass reading the classically-expected دال
  (بعد، العبيد، وقد) and a pass reading a literal لام (بعل، العبيل، وقل), the same failure mode
  first documented at PDF p109/printed p.89 (run 2026-09-19/20, see above) where the adjudicator
  found the "uniform لام" claim did NOT hold up under direct zoom. This time the adjudicator went
  the other way — sided with the classically-expected دال at all five spots as "required by sense"
  — without re-zooming the crops itself. Direct pixel-level inspection (this run, before finalizing)
  of all five spots found the same tall-ascender لام shape at every one, unambiguous and consistent
  with the confirmed لام reference shape elsewhere on the same page (e.g. "ولده") — the print
  genuinely reads بعل، العبيل، وقل throughout this page, not a mix. The five verdicts were
  overridden back to the literal لام reading directly in the applied archive (P111L02, L08, L12,
  L17) per the no-repair rule; pass 2's original transcription, not the adjudicator's, was correct
  here. **Standing note for future runs, updated:** this لام-for-دال substitution is a real,
  recurring feature of specific pages in this edition (at least PDF pp. 109 and 131 so far) but is
  NOT safe to assume uniform even within one page (p109's case) or to resolve by "which reading
  makes sense" (p131's case) — the only reliable method found so far is direct zoom against a
  confirmed لام/دال letterform pair on the same page.

- **Unpointed verse on PDF pp. 131-133 (printed pp. 111-113, run 2026-09-26 pp. 127-134).** Every
  verse block on these three consecutive pages was independently transcribed bare (no tashkil) by
  both correction passes and confirmed by the adjudicator at direct zoom — genuinely printed
  without vowel marks, unlike every other verse block archived so far in this edition (which the
  edition otherwise points consistently, per conventions.md). Hamza, madda and shadda (consonantal
  marks, not vowel pointing) are still present where printed on these same lines. One drafting
  agent on PDF p131 initially filled in a full "best-effort classical" vocalization instead of
  reading the page (a real rule violation, caught and the page fully re-transcribed before
  adjudication — see the LOG line for this run). Decided meanwhile: archived as genuinely bare,
  matching what two independent re-checks plus the adjudicator agree is printed. Worth the owner's
  eye, and worth checking whether this bare stretch continues past printed p.114 or is a
  localized feature of this one gathering.

- **Rough page join, printed p.107→p.108 (PDF 127→128, run 2026-09-26 pp. 127-134).** p.107 ends
  "...وهو وحده فلما رآني اصفر" ("...and he was alone; then when he saw me, [he] turned pale") and
  p.108 opens with a word both passes read differently (pass1 "اونه", pass2 "انه") before "فسلمت
  عليه" ("so I greeted him"). Neither reading bridges cleanly with "اصفر" (turned pale), which
  wants a following noun (e.g. "لونه", "his colour/complexion" — "اصفر لونه" = "his colour turned
  pale" is the ordinary idiom, and would make the whole join read cleanly into "فسلمت عليه"
  immediately after). Direct zoom on the crop (this run) was inconclusive: the disputed word's
  first letter shows a tall vertical stroke that could be أ/ا (supporting "انه"/"اونه" as
  transcribed) or the ascender of a connecting لام (supporting "لونه"), and the crop is faint at
  exactly that spot. Decided meanwhile: left the adjudicator's medium-confidence "اونه" as applied
  (P108L01) rather than substitute a guessed "لونه" neither pass actually read off the page — per
  the freeze-and-ask rule, recording the join concern here instead of silently emending. Worth a
  fresh look at the original high-resolution scan (not just this run's crop) if the reading matters
  later, e.g. for the reading-edition pass over this stretch.

- **Second retrain attempt this run, discarded (run 2026-09-26 pp. 127-134).** See plan.md and
  LOG for the numbers. Two consecutive retrain attempts (this run's and the prior pp.119-126 run's)
  have now both regressed on the same two held-out pages; 301 verified line pairs from both
  attempts are committed in `tools/lines/` waiting for the next try. Nothing to decide here yet,
  but if a third consecutive attempt also regresses, worth reconsidering the retrain recipe itself
  (iteration count, learning rate, or the held-out pages) rather than continuing to accumulate
  discarded attempts unchanged.

- **2026-09-27, publishing run: `nights_index.py`'s marker regex had a false positive that split
  Night 15 in two and mislabeled every night after it.** `--next` first reported "night 15" as
  P105L03-P108L08 (72 lines) and a "night 16" as P108L09-P110L14 (52 lines). Checked the archive
  directly: P108L08-09 reads "...فاصبح والدي في صريخ و بكاء فلما كانت الليلة القابلة علقت والدتي
  بي..." ("...then when the following night came, my mother conceived me...") — the young man's
  own backstory using "the following night" in ordinary narration, not the frame's own
  night-formula (no قالت/قال/قلت tag follows "القابلة", unlike every genuine marker; confirmed by
  grepping all 16 "كانت الليلة" hits in the whole archive — every real one is immediately followed
  by a form of قال, this false one by علقت). `ORDINAL MISMATCH` never fired because `ORDINALS`
  only covers nights 1-10 and the check is skipped past that. Real boundary, confirmed against the
  standard end-of-night formula at P110L13-14 ("...وادرك شهرزاد الصباح فسكتت عن الكلام المباح")
  immediately followed by the genuine Night 16 opening at P110L15 ("فلما كانت الليلة السادسة عشر
  قال بلغني..."): Night 15 is P105L03-P110L14 (124 lines), Night 16 (not yet complete) starts at
  P110L15. Decided and done: fixed `tools/nights_index.py`'s `MARKER` regex to require the
  narrator's tag word immediately after the ordinal (also fixing the two-word "عشر" teen ordinals,
  which the old single-word capture would have broken this same tag requirement against); re-ran
  against the whole archive and every night 1-14's already-published boundary reproduced exactly
  (see `nights_index.py`'s plain table), so the fix is not disturbing settled history, only this
  and later nights. Published Night 15 using the corrected P105L03-P110L14 range. Worth the
  owner's eyes if he ever audits the tool, but nothing here needed him to proceed.

- **Third consecutive retrain regression, and no committed CER-scoring script (run 2026-09-27,
  pp. 135-142).** No `tools/` script measures held-out CER; each retraining run has written its
  own throwaway comparison. This run's from-scratch Levenshtein-CER script gave a baseline
  (committed model) of 9.86% combined on the same two held-out pages (printed 40, 55) that
  earlier runs reported as 8.64%/8.72% — the direction of the regression this run found (9.86%→
  10.79%, discarded) is unambiguous regardless, since both numbers came from the same script on
  the same two models, but the absolute numbers are not comparable across runs and next run's
  measurement won't be comparable to this one either. Decided meanwhile: reported this run's own
  numbers rather than force a match to the old ones. Also, this is the third discarded retrain
  attempt in a row (pp. 119-126, 127-134, now 135-142), with 435 verified line pairs now waiting
  unused — per the standing note two entries up in plan.md, worth reconsidering the retrain
  recipe itself (iteration count 1500, learning rate 0.0005, or the two held-out pages, one of
  which — printed p. 40 — has gotten worse in the last two attempts specifically) before a
  fourth attempt just repeats the pattern. Committing a small `tools/score_cer.py` (fixed
  held-out pages, one consistent metric) would also stop each run from re-deriving its own
  ad hoc comparison.

- **2026-09-27/28, publishing run (nights-16): duplicate glossary keys differing only in
  combining-mark canonical order.** The whole-night review agent found that at least four very
  common word forms — أَنْ, إِلَى, أَنَا, إِلَّا — exist in the assembled night's (and, after
  merging, the shared) glossary under two distinct string keys apiece: same letters, same marks,
  but the hamza-combining-mark (U+0654) and an adjacent short-vowel mark are ordered differently
  between the two spellings, so they are byte-for-byte different keys that render pixel-identical.
  This traces back to the "t" field text itself (different drafting agents, or the same agent at
  different points, wrote the same word's marks in a different internal order), which is out of
  scope for a glossary-only review pass to touch (fixing it means editing already-gated "t" text).
  Decided meanwhile: left it alone rather than touch "t" outside its own gate. This is not a
  reader-facing defect today — `validate_night.py`'s glossary-coverage check and the reader's own
  lookup both fall back to the diacritic-insensitive bare-skeleton match on an exact-key miss
  (reading-conventions.md: "a single absent fatḥa can never orphan a word"), and that fallback
  strips exactly the marks whose *order* differs here, so both spellings still resolve. But it
  does mean the shared glossary is quietly carrying duplicate entries for some of the corpus's
  most common words, and a future night could plausibly hit a case the bare-skeleton fallback
  doesn't cover cleanly. Worth a dedicated pass some day: normalize combining-mark order (NOT full
  NFC — canonical *reordering* of combining marks only, never precomposition, so hamza stays
  decomposed as the house rule requires) across `nights-glossary.json` and, ideally, catch it at
  the source by having `check_slice.py` canonicalize mark order as part of its existing hamza
  repair pass, rather than leaving it to accumulate night by night.

- **Same run: check_slice.py's `--fix` remap can silently drop a still-valid glossary key when
  the same surface form covers two different join/split cases in one slice.** On slice A
  (وَلَطَمَ) and slice G (وَ + قَالَ/قَالَتْ/قُلْتُ and مَا + جَرَى), the same fused surface form
  appeared twice in one slice: once where the archive itself prints it fused (a valid glossary
  key, unchanged) and once where the archive prints it as two separate tokens (needing the
  fix's split/join repair). `--fix`'s glossary remap processes every *old* key present in the
  glossary and rewrites it according to the *first* changed occurrence it finds, which silently
  destroys the still-valid fused-form entry even though the sentences still contain that literal
  fused surface form elsewhere. In slice G this additionally produced a bogus empty-string
  glossary key (from a join case whose second half's remap target was `""`). Neither defect
  shows up in `check_slice.py`'s own PASS result, since that tool only checks bare-strip identity
  of the *sentence* text, never glossary coverage. Caught this run only because the orchestrator
  ran an explicit extra coverage sweep (every word form in every "t" resolves in that slice's own
  glossary) on all 7 slices before assembling, not just the ones `check_slice.py` had flagged;
  fixed by hand in both cases (restored the dropped fused-form key with its own correct gloss,
  removed the bogus empty key). Decided meanwhile: no code change to `check_slice.py` this run
  (the fix is correct for the common case and only breaks on this fairly rare double-occurrence
  pattern), but future orchestrators should keep running that coverage sweep on every slice after
  `--fix`, not just trust its own PASS — and `check_slice.py`'s remap logic is worth hardening
  (e.g. only remap a glossary key when every occurrence of that surface form in the slice changed
  the same way) if this recurs.

- **Verse pointing stops mid-poem, crossing the p.125→p.126 page break (run 2026-09-28,
  pp. 143-150).** The poem describing the young man's beauty is printed pointed (fatha/kasra/damma
  visible, e.g. "زحلُ السوادِ") on P125L12-22, but its last six lines, P126L01-06, continuing the
  same poem on the next page, are printed with no vowel marks at all — confirmed both by direct
  pixel-level inspection this run (adjudicator) and by the fact that the two correction passes,
  reading independently, converged on the same bare reading for P126 without prompting. This is a
  new variant of the already-documented pp.131-133 unpointed-verse anomaly (see the 2026-09-26
  entry above): there, three whole consecutive pages were unpointed; here, the loss of pointing
  happens abruptly mid-poem, exactly at a page turn. Decided: archived exactly as printed (pointed
  through P125L22, bare from P126L01), per the "photograph, not an edition" rule — no marks were
  invented to make the poem's vocalization consistent across the page break. Also on this same
  page, pass 2 independently claimed P130L19-20 (a different, later poem) WAS fully pointed, flatly
  contradicting pass 1's and the adjudicator's reading of no marks at all there; the adjudicator's
  own direct re-inspection sided with "unpointed," and pass 2's vocalized version looked
  reconstructed from memory rather than read off the page — the same failure mode already on
  record (run 2026-09-19, PDF p.98) for an agent supplying "well-known" tashkil instead of checking
  the image. **Future runs: unpointed verse in this edition is not confined to the pp.131-133
  gathering — it recurs at least twice more by PDF p.150, and can start or stop mid-poem at a page
  break. Treat any correction agent's claim of full vocalization on a verse block already flagged
  bare by another pass or a prior run as suspect by default, and re-verify at zoom rather than
  trust it.**

- **Adjudicator's stated reasoning for a hemistich-divider placement was wrong; caught by direct
  pixel measurement, not by trusting the report (run 2026-09-28, pp. 143-150).** Two verse lines
  (P126L01-02) needed a hemistich " * " divider inserted — pass 1 had recorded the caesura only as
  an ordinary-looking double space, with no literal "*", so `apply_verdicts.py`'s known
  empty-pass1-text gap (documented since run 2026-09-19/20) silently dropped both insertion
  verdicts, same as every time before. Applying them by hand, the adjudicator's own note for
  P126L01 said the widest gap sat "right after قامته," but a column-wise ink-density measurement
  of the actual line image showed the single widest gap (120px, roughly double any ordinary
  inter-word gap on the same line) sits one word later, after التي — which is also exactly where
  pass 1's own double space already was. For P126L02 the adjudicator's verdict didn't specify a
  position at all (pass 1's double space there was, on the same pixel check, in the WRONG place —
  the true widest gap fell one word earlier, between حركاته and وسكونه, confirmed by the same
  120px-wide gap recurring at nearly the same horizontal column position across both lines, i.e.
  the typesetting aligns the caesura column down the page). Placed both dividers by direct
  measurement rather than by the adjudicator's description or pass 1's inherited spacing. **Future
  runs: a subagent's prose description of "the wider gap is here, not there" is worth checking
  against an actual pixel measurement of the line crop before trusting it for anything as precise
  as a hemistich boundary — inter-word gaps in this typeface vary enough (16-90px is ordinary) that
  eyeballing at 2x zoom is not reliable for picking out the one true ~120px caesura from an
  merely-larger-than-usual ordinary gap.**

- **`tools/lines/` is keyed by PDF page number, not printed page number — nearly corrupted 12
  pre-existing pairs this run by assuming otherwise (run 2026-09-28, pp. 143-150, caught before
  committing).** Building this run's retrain pairs, `pNNN_LL.png`/`.gt.txt` were first written
  using the printed page number (123-130, this batch's own printed range) — `git status` showed
  most of the "new" files as **modified**, not untracked, which is what caught it: the existing
  `p123_01.gt.txt` held content ("اعجب واغرب وهي سبب لحلق ذقني...") that is actually archived at
  `P103L01`, i.e. printed p. 103 = PDF p. 123 (103+20). The established naming has always been the
  **PDF** page number (confirmed against `p135_01.gt.txt`, which holds printed p. 115's own text —
  115+20=135), not the printed one, and this run's own two new batches of numbers (`123-130`
  printed vs. `143-150` PDF) happened to collide with real pre-existing pairs from the pp.099-106/
  pp.107-114 retrain batches. Reverted every modified file with `git checkout --` before writing
  anything, then rewrote all 134 pairs under the correct `p143_*`.. `p150_*` names with zero
  collisions. **Future runs: `tools/lines/pNNN_LL` is always the PDF page number — never the
  printed page number the rest of a transcribing run otherwise works in — and `git status` after
  writing new pairs (expecting all `??`, zero `M`) is a cheap, effective check that the numbering
  wasn't mixed up, worth doing as a matter of course before committing.**

- **Fourth retrain attempt deliberately held, not attempted (run 2026-09-28, pp. 143-150).** Lines
  archived passed 2800 (the plan.md-noted next-retrain trigger) with this batch. Per the standing
  note left by the previous three consecutive discarded attempts (pp.119-126, pp.127-134,
  pp.135-142, all regressing on the same two held-out pages with the same unchanged recipe: 1500
  iterations, lr 0.0005, `arabest.traineddata` base), decided meanwhile not to spend a fourth cycle
  repeating the identical recipe on identical held-out pages, since nothing about the setup would
  give a fourth attempt better odds than the previous three. Committed this run's own 134 new
  verified prose-only line pairs to `tools/lines/` regardless (569 pairs now waiting across four
  runs since the last successful retrain), so nothing is lost if a future run or the owner does
  revisit the recipe. **Not done, flagged for whoever next attempts a retrain:** try a materially
  different iteration count (1500 iterations at ~10% train BCER each time suggests undertraining,
  not overtraining — worth trying e.g. 3000-4000 before assuming the corpus itself is the limit);
  commit a small `tools/score_cer.py` (fixed held-out pages, one Levenshtein-based metric) so every
  attempt's numbers are comparable to the last, which no committed tool currently provides (each of
  the last three runs wrote its own throwaway comparison, and the numbers are not consistent with
  each other per the 2026-09-27 LOG entry); and consider whether printed p. 40 specifically (the
  held-out page that has gotten worse in the last two attempts) should be swapped for a different
  held-out page, in case it is an outlier rather than representative.

- **p157->p158 join (run 2026-09-29, PDF 157-158).** P137L23 ends 'واحضر قضيبا من' with printed catchword 'ع' under it, but P138L01 begins 'فترجل ونزل به'. The catchword does not match; the bands show no missing line on either page. Decided meanwhile: archived exactly as printed, nothing inserted (probable printer's catchword slip or omitted word in the edition).
- **Shadda in prose (same run).** The print shows a shadda on وسّطها (P137L11) and عليّ (P137L21); the gate forbids marks in prose, so both are archived bare. If marks-in-prose should be kept, the validator needs a rule.

- 2026-09-30, nights-19: sentence 72 (`حَتَّى إِنِّي أُحْضِرَهُ`) — note says indicative, pointing is subjunctive. Left as is; fix the note or the pointing on a later pass.

- **p222->p223 join (run 2026-10-02, PDF 223-230).** P202 ends with 'ربع دينار' and P203L01 begins 'فما علمتني واعطتني اياه'; reads elliptical, a clause may be missing. Not verified against the p222 image this run. Decided meanwhile: archived exactly as printed.
- **Runbook offset.** nights/runbook.md still says printed page = PDF − 18; the archives use −20 (tool output agrees). Left runbook unchanged.

- **Marks in prose (run 2026-10-03, PDF 249).** P229L14 (اف) and P229L17 (وعب) carry printed damma/kasra/shadda; the gate forbids marks in prose, so archived bare (same as the earlier shadda note).

- **2026-10-04 (attended session, the owner's rulings and one bug).** (1) **Publishing had stopped
  since Night 19 (2026-09-30).** `nights_index.py`'s ordinal pattern allowed one word plus an
  optional عشر, so الحادية والعشرون (Night 21) and every compound ordinal after it was never
  found; Night 20 never became "complete", `--next` printed nothing, and twelve firings in a row
  transcribed (archive now to printed p. 242) while Nights 20–29 sat complete and unpublished.
  Night 30's formula is الموفية للثلثين, which the old pattern would have matched — so the
  next firing would have published Nights 20–29 as one "Night 20". Fixed: the pattern takes one
  to four words before the tag, every ordinal is parsed to a number (units, teens, و-compounds,
  tens, الموفية للـ…, بعد المائة) and checked against the night's position, and `--next` refuses
  to publish past a MISMATCH or a unit over 400 lines. Verified against all 30 archived formulas.
  Runbook step 0 now says a long unpublished stretch is a missed formula, not nothing to do.
  (2) **Library labels.** `part` is `Night N · <tale>`, no page ranges; split nights name both
  tales (`… ends / … begins`); the frame is `Prologue · …`. The 21 published entries were
  relabelled in `stories.json`; the story files' own `part` fields still carry the old strings
  and may be aligned in a later pass (the library reads `stories.json`).
  (3) **Marks on prose words.** The archive now keeps a mark the print clearly sets on a prose
  word (conventions.md, prompts, gate = WARN). Words stripped under the old rule, to be restored
  from the images by a transcribing run that has the pages open, or by a dedicated pass: P16L11
  عليّ, P62L18 أَلَذِّ (as read), P137L11 وسّطها, P137L21 عليّ, P145L02 علىّ, P211L19 اليّ,
  P229L14 اف and P229L17 وعب (damma/kasra/shadda as printed). Not urgent; nothing waits on it.
  (4) **Unpointed verse** (pp. 111–113, p. 126, and later) is vocalised editorially in the reading
  edition, with the block's `n` saying the print has no marks there (reading-conventions.md).
  (5) The Night 14 titling question above is RESOLVED by (2).

- **Night 20 review (2026-10-04).** Shared-glossary entries from earlier nights that read wrongly for this night were NOT overwritten: بَعْلًا (entry says misprint of بَعْدًا; here it is 'husband', sentences 61/105), الْأَوَّلِ, حِينٍ, أَنْ (stray 'after yanbaghī'), and several بِـ entries (بِذَلِكَ, بِأَرْضِ, بِثَلَٰثَةِ, بِالْأُمُورِ, بِإِحْضَارِ) whose prefix explanation does not fit; the keys can carry only one meaning, so a deliberate sweep is needed. Also p.148 'حكاية الوزير نور الدين…' mid-line heading is kept as its own sentence; Night 20 part label names both tales.

- **Night 30 review (2026-10-08).** The review agent proposed rewording four shared-glossary entries (بِنَفْسِي 'by my own life' [oath], لِبَعْضِ, بِصَاحِبِ [after wa-idhā, 'behold'], بِي 'of me'); NOT applied because the keys carry earlier nights' meanings — a deliberate sweep is needed. Also the print has the stray word أصل قائي for أصدقائي (P243L05); text kept, noted in l. Hyphenation level of `l` in slice 5 is heavier than elsewhere; left.

- **Night 32 review (2026-10-09).** 713 glossary keys shared with earlier nights carry different wording in the Night 32 drafts; NOT overwritten (existing keys kept, deliberate reconciliation left for later). Table shows 'ORDINAL MISMATCH' at Night 33 (الثلثة والثلثون) only because its tail is not yet transcribed; nothing published past Night 32.

- **Night 33 ordinal (2026-10-10).** The earlier "MISMATCH at Night 33" was not only the unread tail: nights_index.py did not know the alif-less spelling الثلثة. Added ثلثه/ثلاثه to UNITS; --next now offers Night 33. Decided meanwhile: nothing else changed. p300→p301 join repeats قد; kept as printed.

- **Night 34 (2026-10-11).** Review also asked that the `l` layer of the last third of the night (from "the youth had not known…") drop the hyphens that join every proclitic ("And-she-said", "the-shouting"), as the earlier slices do; and that quote marks in `i`/`n` be normalised to curly. Not done this run (risk of mechanical damage). Decided meanwhile: published as is; a later tidy pass could do both.

- **Night 37 review (2026-10-13).** Not applied: (a) shared-glossary entries from earlier nights that read wrongly here (وَلَّى, بِالسَّمَكِ, بِالْبَابِ, بِالْجَارِيَةِ, بِالْخَلِيفَةِ, بِنَفْسِكَ, بِكُمْ, بِشُرْبِ, لِسَيِّدِهَا) — existing keys kept; (b) sentence 125 خص الخوني probably a slip for الخولي (Overseer), left as 'caterer's shed' with the note's doubt; (c) straight vs curly quotes in `i` across sentences 107–136, and verse line breaks in `i` of some verse blocks, left as drafted. Nothing waits on the owner.

- **Night 38 review (2026-10-14).** Not applied: (a) earlier-night glossary entries that read wrongly here (بِالْجَارِيَةِ, بِالْوَزِيرِ, لِيْ "against me", لِمَا, لِعَلِيِّ, بِقَضِيَّةِ, بِكَلَامِهِ, لِلْمَلِكِ, بِي, سَاوَى as a verb for the vizier's name, case of الْمُعِينَ, إِبْرَاهِيمَ) — existing keys kept; (b) Sāwī (S29–50) vs Sāwā (S111–125) follow the print's pointing, unified neither way; (c) glossary style differs between slices (Arabic morphemes vs not) and شَرْبَةَ/شِرْبَةِ for one noun. Nothing waits on the owner.

## 2026-10-14 — Night 39 not published by the unattended run (needs the owner)

Night 39 (P320L14–P327L02) is complete and unpublished, but the first slave's tale (P324L04–P325L08) narrates, in explicit detail, sexual acts between a twelve-year-old boy and a ten-year-old girl (P324L08–P324L19 especially). The run did not draft a translation (literal/idiomatic layers) of that passage and so published nothing. The claim was released and no files other than this note and the LOG line changed. Until decided, the pipeline will pick Night 39 again on every firing and stop the same way; consider telling the runbook how to handle it (e.g. skip Night 39 with a placeholder, publish the Arabic text only for those lines, or have the owner handle this night by hand).

**RULED 2026-10-16 (owner, attended session).** Night 39 is published (revised the same day: the gap note says only
"A passage is skipped here for now."; the opening advisory says what the night contains that is
skipped, nothing more — see publish-runbook.md §0a step 3). Everything in it is translated except the passage itself, which is left out of the reading
edition (its lines listed in `omit.json`, a `[…]` and a note marking the gap). The owner will supply
that passage himself. Procedure: `publish-runbook.md` §0a, which also covers any such passage in a
later night. Shared rule 7 in `.github/pipeline/README.md`: a problem never costs a whole firing.

- **Night 39 published (2026-10-16).** Omitted range P324L08–P324L19 (first slave's tale; sexual acts involving children), listed in omit.json; gap and advisory set as in publish-runbook.md §0a. Review items not applied: earlier-night glossary entries kept where keys collide (624 differ in wording); slice-edge fragments at P321L19/P322L23/P323L23 are marked in n. Several print slips kept as printed and noted (تالم, الخمر for الخبر, ن for ت in بنانه/وزوجنه/فانت). Nothing waits on the owner.

- **Night 42 review (2026-10-18).** Not applied: (a) glossary entries for existing keys (مَا, أَنْ, بِهِ, بِهَا, مِنْهَا, مَعَ, بِمَا, بِهَٰذَا, صَوَابٍ, وَمَالِي, الْعَيْنِ, فَإِذَا) whose new wording was wider than the shared entry — existing keys kept; وَأَلْزَمَ in the shared glossary is probably wrong (reads lazima) and could be fixed deliberately later; (b) الَّتِي new-entry typo "alladhī" for allatī — not added since the key already exists; (c) doubled-shadda lemma spellings in a dozen new glossary values (الـ + دَّار etc.) and "caliph"/"Caliph" case in glosses, left as drafted. Nothing waits on the owner.

- **Night 45 review (2026-10-19).** Not applied: glossary entries for the 534 keys shared with earlier nights whose wording differs; existing keys kept. Nothing waits on the owner.

- **Night 46 review (2026-10-20).** Not applied: glossary entries for the 461 keys shared with earlier nights whose wording differs; existing keys kept. Nothing waits on the owner.

- **Night 47 review (2026-10-20).** Not applied: wider glossary wordings for existing shared keys (مِنَ, مَا, كَانَ, لَهُ, لَكَ, لِي, بِهِ, مِنْهُ, etc.) — existing keys kept. Print slips kept as printed and noted (للمصراع, تعرف for تعرفين, fused words, الم—باح at the close). Nothing waits on the owner.

- **Night 49 review (2026-10-21).** Not applied: glossary wordings for existing shared keys that differ from the new night's; existing keys kept. The archive splits يق—ول and الاب—ات at line breaks into two tokens; the story keeps them split (يَقُ ولُ, الْأَبْ اتَ) with a note, so the bare-strip gate passes. Nothing waits on the owner.

- **Night 50 review (2026-10-22).** Not applied: 12 glossary rewordings for keys already in the shared file (e.g. وَلَّى, كَرَّ, بِكَ, بِذَلِكَ, بِنَا, بِهِمْ); existing keys kept. The king printed as حر دوب (P382L21) is Ḥardūb; the print splits the name. Nothing waits on the owner.

- **Night 54 review (2026-10-24).** Existing shared-glossary entries that read wrongly for this night, kept per the no-overwrite rule: وَالْخَمْسُونَ ("fifty-first"), اثْنَيْنِ ("Monday"; here "two"), الْعَصْرِ ("era"; here "afternoon"), رَأْسَ ("capital"; here "head"), الْعِظَامَ, وَمَا before زَالَ, اِذْ, بِ, تَرُوحُ, قَرِيبَ, صَغِيرٌ, وَأَخَذَ, وَشَرَعَ, رِجْلَيْهِ, عَلَيَّ, لِيْ, كَمْ, فَأَنَا, بِخَمْسَةِ. The story's own translation layers are correct; only the shared glossary popup is off. Nothing waits on the owner.

- **Night 56 review (2026-10-26).** Applied: tr case endings and run-together words, literal/idiomatic fixes, ṭurṭūr, sheikh, store-house, Sharkān note, notes rewritten for the reader. Not applied: ~75 rewordings of shared-glossary entries for keys already in the file (e.g. كَمْ, لَمَّا, عَلَيْكَ, الدِّيوَانِ, جَلِيلَةٌ, بَالِغَةٌ, وَإِيَّاهَا, the بِـ/لِـ entries for بِهَذَا, بِأَنْ, بِيَدِهَا, لَهَا) — existing keys kept per the no-overwrite rule; the story's own layers are correct, only those popups may read off here. Nothing waits on the owner.

## 2026-10-27 (run pp. 447–454)
- Adjudicator read the night-opening word as قلت (6 places); the crop shows قالت, matching earlier archives, so قالت kept at the four night openings plus P433L19/P434L13 left as قلت (first-person "I said"). Worth a second look if the owner audits.
- Night labels on pp. 447/450/453/454 are on their own centred line (not inline); all four flagged h, as P419L21 and P422L11 are. P425L07 earlier has no h — inconsistency in an older archive, not changed.
- Passes 1/2 on pp. 447–450 skipped the line crops; fixed from the adjudicator's crop reading. Wave 2 was told to read crops.

## 2026-10-28 (run pp. 455–462)
- The scan repeats printed pp. 436–437 at PDF 458–459 (a second duplicate leaf, like PDF 48–49). Archived once as P436–P437 from PDF 456–457; PDF 458–459 not archived. From PDF 460 printed = PDF − 22 (header 438 confirmed by the adjudicator). Next run's batch starts at PDF 463 = printed 441; check its header, and note `apply_verdicts.py` still has −20 built in (this run used −22 on a copy for PDF 460–462). Pass over any further duplicate the same way.
- P435L22 ends "فقال انت" and P436L01 begins "الفصل فاشتراه": the print is discontinuous although the headers read 435 and 436. Archived as printed; nothing lost in transcription.
- Night 64 is printed "اللية" (no second ل) at P435L20, and night 65 opens "قات" (no ل) at P437L13; archived as printed; the night index now accepts both.
- Doubtful P440L01 mark over the alif of الا (adjudicator: low-confidence آلا): kept as bare الا per the doubtful-mark rule.

## 2026-10-30 (run pp. 441–448)
- The print has "الليلة التاسعة والستون" at both P444L19 and P446L18 (nights 69 twice; the second should be the 70th). Archived as printed; the night index may mis-number nights 70+ until the owner or a later run decides how to handle it. Night 71 label is at P448L11.
- Passes on pp. 463–466 skipped the line crops again (as on 447–450); the adjudicator checked them. Pass 2 on Sonnet gave 34 disputes over 8 pages (under the 10-a-page limit).
- Doubtful verse marks on P448 L18–21 (hamza ticks, sukun over final ي) kept as the adjudicator read them, low confidence.

## 2026-10-31 (publishing run, night 69)
- Night 70 (P446L18–P448L10) is still held by the ordinal MISMATCH (print repeats "التاسعة والستون" at P446L18; the index reads it as night 69). The next firing's `--next` will therefore refuse or print a mismatch, and the run will transcribe instead; publishing past it waits until the index is taught to accept the repeated label for night 70 (that edit is to tools/, which a run may do under the nights folder). Nothing waits on the owner; not changed in this run.
- Night 69 content: P445L16 اِختي kept as printed (kasra on alif); P445L17 الآ; "لامراراده" and "ومد" read tentatively and flagged in the notes.

## 2026-10-31 (publishing run, night 70)
- The held MISMATCH at night 70 is resolved: `tools/nights_index.py` has a `PRINTED_AS = {70: 69}` table accepting the print's repeated “69th” label for that night only; `--next` now offers night 70 and the table shows ordinal_ok. Night 70 published with a note in `n` on the repeated label. Night 71 (P448L11) is still an unread tail; later nights are unaffected.
- Night 70 doubtful readings: P448L05 كذلك ان اتعب (obscure, probably a dropped particle; read tentatively), P447L14 محلمة (probably محملة), P447L19 ما بقي لي هنا تعود (loose). Kept as printed.

## 2026-11-01 (run pp. 449–456, PDF 471–478)
- Night labels on pp. 450, 452, 454, 456 are printed as their own centred lines, not inline; archived as separate lines (not flagged h on every page; passes differed). Publishing run should treat them as labels.
- Fatha over the lam-alif ligature recorded as لَا (mark sits over the ligature). Kashida in المباح/شعر/الابيات not written as filler dash.
- 82 disagreements over 8 pages (10.25/page), mostly verse marks on p. 449; Sonnet Pass 2 kept for now (one batch over/at the limit, watch next).
- Night 71 (2026-11-01): verse in P449 prints قل where sense and rhyme want قد; copied as printed, read as qad in the note. Closing line P449L22 (حكمت فينا برغم كف أولاد الزواني) is obscure; translated literally with a note, nothing set aside.

## 2026-11-01 (publishing run, night 72)
- Night 72 doubtful readings, kept as printed and flagged in `n`: P451L03 فخلاء (read as فخلاه), P450L22 واتلقني (read as واتلفني), P452L15 واعطه اباها (read as إياها), P452L04 verse line 3 obscure (translated tentatively). The archive was not changed.

## 2026-11-02 (publishing run, night 73)
- Night 73 doubtful readings, kept as printed and flagged in `n`: P454L01–02 زحرك (read as زجرك), اتلقتها (read as أتلفتها), انة (ة for ه); P453L08–09 فلا تدخل في خطيئتي (loose); P453L14–15 the stoker's closing sentences are loosely built. The archive was not changed.

## 2026-11-03 (run pp. 457-464, PDF 479-486)
- Pass agents on PDF 479-482 worked from the bands and draft without opening line crops; the adjudicator caught 12 agreed errors (e.g. المحنة for المحفة). Wave 2 (483-486) opened crops. Future runs should say "read every lineNN.png" in the pass prompt. Disputes were low (33 over 8 pages).
- Tight spacing ضوءالمكان / نزهةالزمان (no space) adopted where the print runs them together, medium confidence; a reviewer may spot-check P457L14, P458 L07-09,12,15, P461L18,21, P464 L01-04.
- Verse vowel marks on P457 (lines 5-9, 11-12) and P460 first half only partly legible; kept as agreed, unverified at mark level.
- Kashida inside words dropped, per archive convention; stretched final line of P464 (and P459L13) written المب—اح as at P450L07.

## Night 80 ordinal not understood (2026-11-04, publishing run for Night 78)

`nights_index.py` reads the Night 80 opening (P470L01) as «الموفيه المثمانين» and flags
`MISMATCH: ordinal not understood`; presumably the print or archive has a damaged
«الموفية الثمانين». Night 79 (P467L11–P469L23) is unaffected and is next. Decided meanwhile: nothing;
once 79 is published, the next firing will hit the mismatch and, per runbook step 0, transcribe
instead. The archive line at P470L01 should be checked against the page image (transcription
pipeline's job), or the tool's ordinal pattern taught the 80th formula.

## 2026-11-04 — Night 80 formula not understood by nights_index.py
`nights_index.py` reads the night-80 formula (P470L01) as «الموفيه المثمانين» and flags ORDINAL MISMATCH; night 80 is also marked "tail unread" (archived only to P472L21). Probably a transcription slip for «الموفية الثمانين» ("the eightieth") — the archive was not changed. Decided meanwhile: night 79 published; the next firing should record/handle the mismatch per runbook step 0 (transcribe, publish nothing past it) and the tool's ordinal pattern may need الموفية الثمانين / the archive line checked against the image.

## 2026-11-05 — Night 80/81 ordinal mismatch resolved (transcribing run, PDF 495-502)
Cause found and fixed in `tools/nights_index.py`, archive untouched: night 80's print reads «الموفيه المثمانين» (misprint of الثمانين; added `مثمانين`→80 to TENS) and night 81 is printed «الليله الحاديه والثمانون» with final ه (MARKER now accepts الليله). Nights 80–84 are now complete and queued for publishing (night 85 starts P480L19, tail unread). Decided meanwhile: nothing else; the next firing publishes night 80.
Night-label lines on their own line: adjudicator recommended no `h`; I kept `h` on all four (P474L02, P475L17, P478L05, P480L19) to match earlier archives (P465L01, P470L01) and the archive's own method note. Say if you want them unflagged.
Pass agents for pp. 495-498 (four of eight pass-1/pass-2 reports) did not open the line crops despite the prompt; I re-launched wave 2 with the requirement stated and it was obeyed. The adjudicator opened crops for every disputed line. No retrain this run (not attempted).

## 2026-11-06 (publishing run, night 83)
- Night 83 doubtful readings, kept as printed and flagged in `n`: P477L23 سام (sense wants سلم, “is safe”), P476L20 بين والدك (يدي dropped before والدك), P477L15 خشعتّ (stray shadda), P476L11 حق (no accusative alif), P475L20 مهيٌ. Corrected misprints are in emend.json (P475L18, P476L09, P477L02); فقراً (P477L11) is corrected in the text by the hamza-on-alif reading and noted. The archive was not changed.

## 2026-11-07 (publishing run, night 85)
- Doubtful, kept as printed and flagged in `n`: P481L20 استبرأوهن (verb in print; sense wants استبراؤهن), P481L17 مخالفتي لك, P482L02 من منذ. Corrected misprint in emend.json: P482L01 بوالدين→بولدين. The archive was not changed.

## 2026-11-08 (publishing run, night 86)
- Doubtful, kept as printed and flagged in `n`: P483L07 لابستوحش (perhaps لا يستوحش; clause left partly unrendered), P484L02 ولاينيدك (verb unidentified), P484L07 للموزبردندان (garble for للوزير دندان), P484L09 خزنته (perhaps خزانته). Corrected misprints in emend.json: P482L05 قات→قالت, P483L19 يقدنا→يفدنا. The archive was not changed. هرّأ (P483L05) read as intransitive 'fell into shreds'.

## 2026-11-08 (publishing run, night 87)
- Corrected misprints in emend.json: six اى→الى (P485L05, P485L12, P486L02, P486L04, P486L08, P486L11). Doubtful, kept as printed and flagged in `n`: P486L10 جمع ما (perhaps جميع ما). Run-together words kept as printed and noted: السعيدأن, السّران, لا نتظار, ارادان, امران, صاربين. The archive was not changed.

## 2026-11-09 (publishing run, night 88)
- Corrected misprints in emend.json: P487L09 اخوة→اخوه, P488L02 الدوهي→الدواهي, P488L08 النمعان→النعمان, P489L02 عمان→عنان ("thirty thousand reins"), P489L05 كالبد→كالبدر. Doubtful, kept as printed and flagged in `n`: P487L02 وتانى (read as تأنّى; perhaps وتأتي), P488L01 احدوا لهم (obscure; perhaps احوالهم), P488L05 انه before ذات الدواهي, P488L15 بوادي النعمان. Run-together and split words kept as printed and noted: السعيدان, وأسافرانا, ونريدان, فمامر, طارحتى, الخطيراني, يالعيسى, قرّعينا, كا لفر نسيس, الصعا ليك, سار وا. The archive was not changed.

## 2026-11-09 (publishing run, night 89)
- Corrected misprint in emend.json: P490L20 اخوة→اخوه. Doubtful, kept as printed and flagged in `n`: P491L03 تتقربوا / وتتمسكوا (no final nūn after انكم). The passage about the patriarch's dung (P491L09–L15) is mocking but not in the omit class; translated as printed. The archive was not changed.

## 2026-11-09 (publishing run, night 90)
- Corrected misprints in emend.json: P492L06 وجههه→وجهه, P492L22 اخوة→اخوه, P493L16 ثانب→ثاقب, P493L20 لمج→لمح. Doubtful, kept as printed and flagged in `n`: P492L11 الشروهمان (read as الشر + an unidentified وهمان), P492L20 والفتوا (probably والتفتوا), P494L01 الصوى (perhaps الهوى). Run-together words kept as printed and noted: اريدان, منادينادي, يبرزلي, برزاليه, كادان, ولاحماس, ومدّيده. Name variants شملوط/شلموط kept as printed. The patriarch's-dung passage (P492L01–L04) is mocking but not in the omit class; translated as printed. The archive was not changed.

## 2026-11-10 (publishing run, night 91)
- Corrected misprints in emend.json: P494L10 واعلموا→واعملوا, P494L18 الله→لله (والحمد), P495L14 الصباج→الصباح, P496L03 مكان→المكان (ضوء المكان), P496L06 البقر→البقرة, P496L08 تواوا→تولوا, P496L14 واتسم→واقسم. Doubtful, kept as printed and flagged in `n`: P494L09 وتزهد, P496L02 والزار (perhaps الزنار), P495L17 المركب (perhaps المراكب). Run-together words kept as printed and noted: السعيدان, ولازال, ولايعرف, لعدوالله, الفاكما, والّابرئتم. The patriarch's-dung passage (P496L13) is mocking but not in the omit class; translated as printed. The archive was not changed.

## 2026-11-10 (transcribing run, PDF 519-526 = pp. 497-504)
- P502L01 (verse, top of p. 502) is badly printed; the adjudicator's reading «وَيَزِيْنُ شُمْعَتَهُ … عَطْرُ الْقَبِيْحَةِ لَابَفِيْ بِفَسَاهَا» is low confidence and worth a human look at PDF p. 524. Archived as read.
- Word spacing: the adjudicator followed the print (solid where set solid: ولاكبير, لابدان, السعيدان, اريدان, سائراقاليم, وعبادالله, صارله); one exception by sense, P501 وخد اصفر (low). Earlier archives are split on such pairs. Decided meanwhile: follow the print, as the conventions say.
- Misprints archived as printed (for the publishing run's emend.json): P498 با, قتال, والنساد; P499 واما; P500L23 المباج; P502L22 مُربنا; P504L05 وحنى.

## 2026-11-10 (publishing run, night 92)
- Corrected misprints in emend.json: P497L04 باراجي→ياراجي (run-together kept), P497L09 ومانت→ومالت, P497L15 اعضب→العضب (a verse word: the print's اْعَضْبِ drops the lām; the corrected word is pointed by us, the rest of the verse is as printed — say if verse misprints should instead stay as printed), P498L02 با→يا, P498L03 فاصق→فالصق, P498L05 قتال→فقال, P498L08 والنساد→والفساد, P499L14 واما→ولما, P499L15 همزيمة→هزيمة, P500L23 المباج→المباح. Read by likeliest sense and flagged in `n`: P498L02 اعظم الجناحين ("the greater of the two wings"), P500L17–18 the old woman's brew and kerchief (what she does with it is unclear as printed), P500L21 لاعدم المسيح طلعتك (pointed لَا عَدِمَ). Run-together words kept as printed and noted. The archive was not changed.

## 2026-11-11 (publishing run, night 93)
- Corrected misprints in emend.json: P501L06 ولهانم→ولهافم (“and she had a mouth”, set solid), P501L13 جاربة→جارية, P502L22 مُربنا→مُرينا (fem. imperative, “command us”), P503L20 بصائعنا→بضائعنا. Doubtful, kept as printed and flagged in `n`: the verse P501L22–P502L01 (عَلَاتَيَّهَا perhaps علا تيهها; لَابَفِيْ perhaps لا يفي), P504L02 ويهمكم (read wa-yahummakum), P503L01 ضوو (for ضوء), P504L05 the monastery name مطر وحنى (given as printed). The passage on Dhāt al-Dawāhī's siḥāq with the slave-girls (P501L12–L20) concerns adults and is not in the omit class; translated plainly. The archive was not changed.
- Housekeeping: the checkout's local `main` had diverged from origin/main by 50 commits (same as last run). Not reset this time; the run worked on a branch made from origin/main and pushed to main with an ordinary push.

## 2026-11-11 (publishing run, night 94)
- Corrected misprint in emend.json: P506L12 يأني→يأتي (a verse word, «وَحَبِيْبٌ يَأْتِي بِلَا مِيْعَادِ»; the rest of the verse is as printed — same handling as night 92's verse correction, still awaiting your word on whether verse misprints should stay as printed). Printed verse vowels kept and flagged in `n`: P505L02 اِنَّ where the sense wants اِنْ, and الْحَمَامَ (ḥamām, doves) where the sense wants ḥimām (death); P505L05 قَاصِ for qāṣin. Read by likeliest sense and noted: P506L02 اعطينه as uʿṭiyannahu (energetic), not a misprint. Spacing kept as printed and noted: ولوا قيم (= ولو اقيم), ولابدلي, مايرزقني, وعبادالله, لاتحملوا, يامولانا, بمالم, لَاتَرَى, اِذْفَوْقَ. The archive was not changed.

## 2026-11-12 (publishing run, night 95)
- Corrected misprints in emend.json: P509L01 بكاو→بكاء (bukāʾan), P509L11 فاترأ→فاقرأ (a verse word, «فَاقْرَأْ سُطُوْرَ الْعِدَى»; the rest of the verse as printed; same handling as nights 92 and 94, still awaiting your word on verse misprints), P511L10 قصدة→قصده, P511L14 بأكله→يأكله, P512L07 جاربة→جارية.
- P508L14 فرّق: the print sets the shadda on the rāʾ (farraqa, "divided"); the sense wants fa-raqqa ("and softened"). The archive's mark is kept, as the rule on printed prose marks requires, and the reading is translated by sense and explained in `n`. A misplaced mark cannot be listed in emend.json, which works on bare letters. Say if such marks should be moved instead.
- Doubtful, kept as printed and flagged in `n`: P509L20–21 «لم تفعل الا وقت التحية» (perhaps لم تفطر), P512L15 «البطريق مطروحنى» (the man killed is the monk). The new names are rendered Daqyānūs (دقيانوس) and Tamāthīl. Rustam keeps the vocalisation رُسْتُم already in the glossary. Run-together words kept as printed and noted. The archive was not changed.
- Housekeeping: the checkout's local `main` had again diverged from origin/main by 50 commits; it was reset to origin/main before the run.

## 2026-11-12 (publishing run, night 96)
- Corrected misprints in emend.json: P513L19 واخاة→واخاه, P515L11 فد→قد, P516L12 ماواة→ماواه and P516L13 مسعاة→مسعاه (ة for ه; the pair rhymes), P517L07 الراهد→الزاهد. Doubtful, kept as printed and flagged in `n`: P514L05 واستاذنها (singular among plurals; perhaps واستاذنوها), P514L21 برّاج الحمّام (print's shadda gives "bath"; sense wants al-ḥamām, pigeons — mark kept, translated as pigeons), P516L16 في اداء الاسنة (perhaps الاعداء), P516L04 مفاوز (read "open stretches", uncertain). The archive was not changed.
- Shared glossary: about 38 existing entries were deliberately broadened (not narrowed) so they also fit this night — mostly bi-/li- prefix senses, plus حَمَلَتْ (charge), فَأَرَاهُمْ (I see them), الْمَعْرُوفِ (well-known), and the two شَرْكَان entries now read Sharrukān to match every tr.

## 2026-11-12 (publishing run, night 97)
- Corrected misprints in emend.json: P518L02 دات→ذات, P519L01 فيام→نيام, P519L05 اخاة→اخاه, P519L17 ناخذة→ناخذه (ة for ه), P519L20 اى→الى, P520L02 هذة→هذه, P520L06 احل→احد. Doubtful, kept as printed and flagged in `n`: P518L13 عِداة (read ʿidātan "enemies"; perhaps عداه/عداتي), P520L01 «فلما نظر … ان عساكر الكفار» (the first ان reads as if for الى; translated by that sense). Run-together words kept as printed and noted: واريدان, يجسران, تقدران, تريدان, يتعرضوالهم, الاعميانا. The archive was not changed.
- Shared glossary: 33 existing entries deliberately broadened to fit this night (bi- senses chosen by the verb, case notes); the entry أَمَّا wrongly glossed a wa- its key does not have, and is fixed.

## 2026-11-12 (transcribing run, PDF 543-550 = pp. 521-528)
- Both passes agreed on two words the print does not have; the adjudicator and the run corrected them from the image: P524L21 «هلى» (print; both passes had على — a misprint for the publishing run's emend.json) and P528L02 «مطر وحنى» (both passes had مطار وحتى; this is the monastery name already published in night 93). Agreement between the passes is therefore not proof; nothing to decide, recorded for the publishing run.
- Misprints archived as printed (for emend.json): P524L21 هلى (for على); the adjudicator also noted وبأنينا, حنّ, النذيز, اى, ماوخنا in this batch.
- These pages set many more prose shaddas than usual (42 gate warnings against ~20–30). Two lines were spot-checked against the crops (P525L11, P525L15); the marks are printed. Kept.
- Nights 98 and 99 are now complete and unpublished; the next two firings should publish them.

## 2026-11-13 (publishing run, night 98)
- Corrected misprints in emend.json: P520L17 لبعضها→لبعضهما (dual), P520L19 والوزيز→والوزير, P521L02 ووزيرة→ووزيره, P522L03 وبأنينا→ويأتينا (the transcribing run's note). Kept as printed and noted: الاقتلكم, لايكون, مايريده, العسكران (run-together words), امتلائت, رأهم (pointed رَأٰهُمُ with a dagger alif). P520L18 وجزانا read as the verb jazānā; the note gives the noun jazāʾunā as the other reading. P521L07 عرفناكم pointed as form II ʿarrafnākum, "we have told you"; the note gives form I. The archive was not changed.
- Decision needed (house-wide, not new): since about night 90 the `t` points the name شَرْكَان (Sharkān) while `tr` and `i` give Sharrukān, and shared glossary entries are split (some say Sharkān, some Sharrukān). Meanwhile this night follows the precedent (شَرْكَان in t, Sharrukān in tr). Say which one should be used, and a run will bring the published nights into line.
- Shared glossary: 19 existing entries were broadened or corrected to fit this night (bi-/li- senses after wakkala, rāḥa, waʿada, atā; مَا now covers questions and the negative before an imperfect; أَرَادَ lost a wa- that its key does not have; يَبْقَ romanisation yabqa).

## 2026-11-13 (publishing run, night 99)
- Corrected misprints in emend.json: P523L05 حنّ→جنّ (“the darkness fell”; the printed shadda kept), P524L02 معها→معهما (dual, “with the two of them”). Kept as printed and noted: P522L20 جعلُ (printed ḍamma on the last letter of a perfect verb; read jaʿala, the mark kept, as conventions require for printed prose marks); run-together ارادان, لاغير, اريدان (×2), السديدان, ناروهم, الاخيرا; the misplaced space in P524L14 لوا نتبهوا (for لو انتبهوا) kept, glossed in two keys. The archive was not changed.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next firing: night 100 is not yet complete (its tail is unread), so the next run should transcribe.

## 2026-11-13 (transcribing run, PDF 551-558 = pp. 529-536)
- `nights_index.py` could not read the ordinals «الحادية بعد المائة» (night 101) and «الثانية بعد المائة» (night 102): it knew «X والعشرون بعد المائة» but not a bare unit before «بعد المائة». It printed ORDINAL MISMATCH. This run added that one case to `ordinal_number` (unit + بعد + hundred); the table now reads nights 100 and 101 as complete. Nothing else in the tool changed.
- Both night labels in this batch (P529L15, P533L01) are printed centred on their own line in larger type, so they are archived as their own `h` lines, as with night 35. On P533L01 the alif of الليلة carries a hamza-like flag; the adjudicator took it for a type defect and archived الليلة.
- Both passes agreed on فشكره at P536L03; the print has فشكرة (with dots, as on P535L10). Corrected from the image. Agreement between passes is still not proof.
- For the publishing runs (emend.json candidates or doubtful readings, all archived as printed): P535L14 «ونادوا حنّى ومريم» (shadda printed; perhaps for يا حنّا/حتى); P535L15 «وقدا قبل» (space misplaced, for وقد اقبل); P534L16 «وتسست»; P534L21 «يبخوا» (for ينجوا?); P530L05 and P534L22 «اى» (for الى); run-together words ضوءالمكان, السعيدانّ, امرالّا, تريديا, اريدان kept.
- Nights 100 and 101 are now complete and unpublished; the next two firings should publish them.

## 2026-11-13 (publishing run, night 100)
- Corrected misprints in emend.json: P524L21 هلى→على, P525L04 هذة→هذه, P525L08 خنت→خفت ("what I feared"), P525L13 النذيز→النذير, P525L20 اى→الى, P525L21 and P528L16 بنورة→بنوره. Doubtful, kept as printed and flagged in `n`: P525L05 بدونكم (read dūnakum, "at them!", with an extra bi-), P525L05 خلفكم (sense wants خلفهم), P525L09 حياة (perhaps حيلة, "no way out but the jihād"), P528L08 «الملهمين وحي الاشارة» (compressed; read by sense). P527L03: Rustam proposes 10,000 horse, the two emirs choose 20,000 — kept as printed and noted. Printed verse oddities (وَسَلِمْتَنِي, الشُّجَّاعَةِ, حَذَرْتُهُ, اِنِّي) kept and noted. The monastery دير مطروحنى is pointed مَطْرُوحَنَى, as for the monk in nights 95–96; the meadow مرج ماوخنا is given as printed. Run-together and split words kept as printed and noted. The archive was not changed.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next: night 101 is complete and unpublished; the next firing should publish it.

## 2026-11-13 (publishing run, night 101)
- Corrected misprint in emend.json: P530L05 اى→الى. Kept as printed and noted: P531L08 «فقالوا له … فقالوا له» (question and answer both "they said"); P530L12 باخ (colloquial akh for akhī); P532L15 لينل (dagger alif); ة for the pronoun -hu in جوادة (×2), اخوة, فاتركوة; run-together words (السعيدانّ, يدعولي, الاشهيدا, الاخوفا, فبينماهم, امانظرت, مازال) kept. New name تركاش pointed Turkāsh (vowels editorial; to confirm if it recurs pointed). The archive was not changed.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next: night 102 needs its tail transcribed (P537+); the next firing should transcribe.

## 2026-11-13 (transcribing run, PDF 559-566 = pp. 537-544)
- Both passes agreed on افريدون at P537L19; the print has «افربدزن» (one dot under the tooth, a dotted ز for و). Archived as printed; an emend.json candidate (→ افريدون) for the publishing run. Both passes also split «فلمارأى» (P539L01), which the print runs together; archived joined.
- The night labels for 103 (P539L06) and 104 (P542L12) are centred on their own lines and archived as `h` lines, like P529L15 and P533L01. `apply_verdicts.py` did not carry the adjudicator's `h` flag through, so the run set both by hand. Nothing to decide.
- For the publishing runs (all archived as printed): P539L11 «اغيه» (for اخيه), P542L11 «المباج» (for المباح), P537L19 «افربدزن» (for افريدون); run-together كادان, السعيدان, اوصوابه, اخرجوالك kept; P543L16 لَاذابها carries a printed fatha.
- Night 102 is now complete and unpublished; the next firing should publish it, then night 103.

## 2026-11-13 (publishing run, night 102)
- Corrected misprints in emend.json: P534L21 يبخوا→ينجوا, P534L22 اى→الى, P537L19 افربدزن→افريدون, P538L02 ينبت→يثبت ("does not stand firm"). Kept as printed and noted as doubtful: P534L16 وتسست (obscure), P535L14 «حنّى» (perhaps for Yuḥannā), P535L02 تطاوحت, P534L14 رحاة, P533L20 «الا سواء», P536L21 «فان قتلتني» (sense wants "if he kills me"), P537L17 خولنج (read as a wood). New name لاويا pointed Lāwiyā (vowels editorial). The archive was not changed.
- Incident, fixed, nothing to decide: the night 102 publish commit (26318b27d) was built on a tree that predated another run's commits on main, so for about a minute it reverted that run's Ardā Wirāz files, its stories.json entry, and its changes to reader.html, index.html and progress.json. Commit 8225ab58f put every one of those files back exactly as that run left them (checked: main now differs from that run's state only by nights-102.json, nights-glossary.json and the one stories.json entry). Cause: a `git reset --soft origin/main` after a fetch that had moved main; the run now re-checks `git diff --stat origin/main` before pushing.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next: night 103 is complete and unpublished; the next firing should publish it.

## 2026-11-13 (publishing run, night 103)
- Corrected misprints in emend.json: P539L11 اغيه→اخيه, P539L16 وهنّأنه→وهنّأته, P540L04 انتضى→اقتضى ("their judgement called for"), P542L11 المباج→المباح. Kept as printed and noted as doubtful: P540L07 فملس (read malasa, "stroked"; perhaps for فلمس), P540L03 «واقل الاهوال» (sense poor; perhaps for اهول), P541L09 مغائر (read as mughāyir, "unmatched"), P541L22 بثائر (for بثأر); the printed shadda on the lām of وقبلّوا (P539L16) kept where it stands; the misplaced space in P542L06 «واتواخيا مهم» (for واتوا خيامهم) kept, glossed in two keys. The verse at P541L10–13 is copied as printed (لَوْسَابَقَ, يُسْبِقُهُ kept and noted). The archive was not changed.
- The text names Bahrām "emir of the Turks" here, reversing earlier nights (Bahrām of the Daylam, Rustam of the Turks), and calls Ḥardūb "king of the Armenians" (elsewhere king of the Rūm). Both are kept as printed and noted for the reader. Nothing to decide.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next: night 104 needs its tail transcribed (P544+); the next firing should transcribe.

## 2026-11-13 (transcribing run, PDF 567-574 = pp. 545-552)
- The night 105 label (P545L06) is printed «فلما كانت الميلة الخامسة بعد المائة» — الميلة, a misprint for الليلة (checked on the crop). Archived as printed. `nights_index.py` could not see the night, so it read night 104 as running to P549L08 and the ordinals 106/107 as mismatches. This run added الميلة to the tool's list of label spellings (beside الليله, اللية) and anchors the night on the matched word; the table now reads nights 104, 105, 106 as complete with no mismatch. Nothing else in the tool changed. For the publishing run: an emend.json candidate (P545L06 الميلة→الليلة).
- Pass 2 on Sonnet disagreed with Pass 1 115 times over the 8 pages (~14 a page, worst on the verse pages 571–572), above the runbook's 10 a page, so Pass 2 was rerun on the strongest model for the whole batch (52 disputes). This is the first batch over the threshold; the previous one was at ~6. If the next batch also runs high, Pass 2 goes back to the strongest model by the runbook's rule.
- `apply_verdicts.py` cannot split a pass-1 line when pass 1 merged a centred night label into the next prose line (P552L01–02); the run fixed those two lines by hand and set `h` on all three labels (P545L06, P549L09, P552L01). Nothing to decide.
- For the publishing runs (all archived as printed): P546 زوحتى, حزنيا, انريدون (for افريدون); P549 حيت; P550 verse نَرَكْتَ; P552 ونريدان نحكي (for تحكي), والمنكلم (for المتكلم), ثكثروا (for تكثروا); P547 نعن (perhaps فعن/وعن, low confidence); P549 خمات (for ختمات?). Run-together words السعيدان, السعيدانه, وهوانه, مايزيل kept as printed (spacing judged tight; low/medium confidence).
- Nights 104, 105 and 106 are now complete and unpublished; the next three firings should publish them.

## 2026-11-13 (publishing run, night 104)
- Misprint corrected (emend.json): P542L14 جانسا→جالسا. Kept as printed and flagged in the notes: P544L01 «لا تبع», a misplaced space in لاتبع (la-atbaʿu, "I will surely follow"), read across the space; P543L04 "King Sharrukān" sitting by Sharrukān (the king meant must be Ḍawʾ al-Makān); P543L11 قليل without the accusative alif; P543L15 آفة رقطا (perhaps for افعى رقطاء, "speckled viper"). The archive was not changed.
- Shared glossary: 16 existing entries were widened with this night's sense (none overwritten), and وَكَذَلِكَ was rewritten so it explains كَـ. Nothing to decide.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next: nights 105 and 106 are complete and unpublished; P545L06 الميلة→الليلة is the emend candidate for night 105.

## 2026-11-13 (publishing run, night 105)
- Corrected misprints in emend.json: P545L06 الميلة→الليلة (night label), P546L03 زوحتى→زوجتى, P546L09 حزنيا→حزينا, P546L19 انريدون→افريدون. Kept as printed and flagged in the notes: P547L17 «نعن الاقامة» (the sense wants فعن or وعن, "do not turn aside from staying"; the reviewer suggested correcting to فعن, but initial ن and ف differ in shape as well as dots, so it stays a doubtful reading); P545L14 «واكتفاء من المال» (loose; read wa-iktifāʾan, "and enough money"); P548L06 بمَسيح الرصاص (read masīḥ, "molten", from sāḥa; the fatḥa is the print's). The verse at P548L16–17 is copied as printed (اَخُ with short u kept; بحيلة has no tanwīn, read ḥīlatin for the metre and noted). The archive was not changed.
- Ḥardūb's relation to Dhāt al-Dawāhī: this night calls him her son (ابني حردوب), as the tale usually does; Night 104's text (P543) calls him her father (والدها), and its `about` follows that. Both are kept as the text has them; night 105's note points out the difference. Nothing to decide unless the owner wants Night 104's `about` reworded.
- Sharkān/Sharrukān: still following the precedent (شَرْكَان in t, Sharrukān in tr and i), pending the decision asked for under night 98.
- Next: night 106 is complete and unpublished; the next firing should publish it.

## 2026-11-13 (publishing run, night 106)
- Corrected misprints in emend.json: P549L12 حيت→حيث, P549L13 خمات→ختمات (khatmāt, Qurʾan recitations), P550L04 نركت→تركت (verse). Kept as printed and flagged in the notes: P550L04 lacks the و before نلت that metre and sense want (not added: a missing word, not a clear letter slip); obscure verse phrases تسر بما تلاقى, ساوت الرشقى, اصدقا (P550L05–08), تعني (P550L16), الاضعان with ض for ظ.
- Review raised again the Sharkān/Sharrukān mismatch (t شَرْكَان, tr sharrukān; ~110 cases across Nights 95–106). Still following precedent, pending the decision asked for under night 98.
- Next: night 107 is incomplete (tail unread); the next firing should transcribe.

## 2026-11-14 (transcribing run, PDF 575-582 = pp. 553-560)
- **Pass 2 is back on the strongest model.** Sonnet's Pass 2 ran 92 disputes over the 8 pages (11.5 a page, 26 and 24 on the verse pages 578 and 582). That is above the runbook's 10 a page for the second batch running, after 567–574. Three of the eight Sonnet agents also skipped the line crops and read only the bands, and one took the two-line running header on p. 578 for a section heading. By the rule in `runbook.md` §2, Pass 2 was rerun on the strongest model (38 disputes) and is moved back to the strongest model for good; `runbook.md` now says so at the top of the Pass 2 paragraph. This costs about 15k more tokens a page. Nothing to decide unless the owner wants Sonnet tried again.
- Two archive changes made by hand after the adjudicator's report, each checked on the image: P556L03 and P558L11 (night labels 108 and 109, printed centred on their own lines like 110 at P560L14) were given `h`. P558L07 ثلثة→ثلٰثة: the dagger alif is printed, as on P558L14; both passes had missed it. The adjudicator thinks the first شئت on P554L01 (verse) may carry a damma; it was left as the passes agreed.
- For the publishing runs (all archived as printed): P555L20 يالدر (for بالدر); P557L01 قئما (for قائما); P557L04 اتينك (for اتيتك?); P557L10 باستنام (for باستلام); P559L08 فاضاو (for فاضاء); P560L06 ولازات (for ولازالت/وما زالت); P558L10 البــاح, P556L02 المباح (end-of-night formula). Night 107 runs P552L01–P556L02, night 108 P556L03–P558L10 and night 109 P558L11–P560L13; all three are complete and unpublished.
- `gate.json` (nights_ocr.py) undercounts the running header when it runs to two lines (pp. 556–557) or is faint (553, 559). That is why it raised false "dropped line" flags. The passes handled it, so nothing was lost. Nothing to decide.
- Next: the next three firings should publish nights 107, 108 and 109.

## 2026-11-14 (publishing run, night 107)
- Corrected misprints in emend.json: P552L05 نحكي→تحكي, P552L07 والمنكلم→والمتكلم, P552L10 لها→له («يقال لها الملك سليمان شاه», the لها carried over from the city a line above), P552L20 ثكثروا→تكثروا, P555L20 يالدر→بالدر. Kept as printed and flagged in the notes: the last verse line (P554L01) «لم يُجْلِ في العُمُرِ» — obscure, perhaps for لم يُجْدِ, and off the poem's -ru rhyme; بخلفه (ه for ة), افضي, الي, مقالى (ي/ى spellings); run-together السعيدان, السعيدانه, ونريدان, وماجرى, مايزيل, وهوانه, اتريدان, لايعلم, لايدري, ولاشرف, ولايحسن, لانظير, لارهبانيّة, لايتوجه, ولاتعُدْ, الّابها. The archive was not changed.
- Library label: Dandān's story-within-the-story begins this night (Sulaymān Shāh, the princess of the White Land; the text names it only «حكاية العاشق والمعشوق والمتكلم بينهما»). Labelled `Night 107 · King ʿUmar ibn al-Nuʿmān, continued / The Lover and the Beloved begins`, taking the tale's name from Dandān's own words, since the print gives the inner tale no heading here. Later nights will use `The Lover and the Beloved, continued` until the owner prefers another name (e.g. the hero's name, once he appears).
- Shared glossary: four existing entries (بِالْهَدَايَا, بِحُبِّهَا, بِقُدُومِهِ, لِلْمَلِكِ) were extended or rewritten so their بِـ/لِـ explains this night's use; nothing overwritten with a different meaning.
- Next: nights 108 and 109 are complete and unpublished; the next two firings should publish them.

## 2026-11-14 (publishing run, night 108)
- Corrected misprints in emend.json: P557L01 قئما→قائما; P557L04 اتينك→اتيتك (the vizier speaks as “I”, annī; the transcribing run had queried it as اتيتك?). Kept as printed and flagged in the note: P557L10 باستنام (istinām gives no good sense; perhaps باستلام, reverent kissing, but a guess).
- Verse P556L08–16: the first line (al-hudā … al-mujtanā / al-mujtanī) and the fifth (rāfatan) are obscure and translated as far as the words allow; the print's الْمُدَى (mudā, "knives") is translated as madā, "span", noted, not emended (verse pointing is final).
- Library label: `Night 108 · The Lover and the Beloved, continued`, following the night-107 decision. Nothing to decide.
- Next: night 109 is complete and unpublished; the next firing should publish it.

## 2026-11-14 (publishing run, night 109)
- Corrected misprints in emend.json: P558L18 تكونوا→يكونوا (between يخرجوا and ينشروا under the same أن), P559L01 وانفق→واتفق, P559L08 فاضاو→فاضاء, P560L06 ولازات→ولازالت. Kept as printed and flagged in the notes: the verse at P559L23–P560L03 (وَآفَاقُ … الرَّآسَةَ with cases the grammar does not want; لَاتَرْكَبُوهُ, probably for لا تُرْكِبُوهُ; اَوْطَاءَ for awṭaʾa); اربعة عشر سنة (P560L11–12, numeral gender as printed); صارله run together. The archive was not changed.
- Library label: `Night 109 · The Lover and the Beloved, continued`. The hero, Tāj al-Mulūk, is born and named this night; if the owner would rather the inner tale be labelled by his name from here on, that is a relabel for an attended session. Nothing waits on it.
- Next: night 110 is incomplete (tail unread); the next firing should transcribe.

## 2026-11-14 (transcribing run, PDF 583-590 = pp. 561-568)
- Pass 2 ran on the strongest model, per the runbook since this morning: 44 disputes over 8 pages (5.5 a page), back to the usual rate. Page 589 had no disputes at all; the adjudicator spot-checked nine of its lines against the bands and found nothing both passes missed.
- Night labels 111 (P563L19), 112 (P566L06) and 113 (P568L16) are each printed centred on a line of their own; all three carry `h` (two set by hand after apply, checked on the image). The night 111 label reads الليلة, not الميلة as at P545L06.
- For the publishing runs (all archived as printed): P561L20 verse, last hemistich «هُنَاكَ سَوُءِ لَمْ» is damaged and obscure (low confidence); P562L07 فاما (for فلما?) and بانباعه (for باتباعه); P564L03 verse يَاصَاحِ, where only one dot shows, so it may be بَاصَاحِ; P564L19 عُليّ with a printed damma; P565L03 بضاعنك (for بضاعتك); P566L03 استنعت (for امتنعت, as printed on L08); P566L16 verse اَكْذَبَ (marks uncertain); P568L11 and P568L13 فرق (for فوق). Run-together words kept as printed: عشرعاما, جاؤابه, وارادان, لَوْمَسَّ, قهراعنه.
- Nights 110, 111 and 112 are now complete and unpublished; the next three firings should publish them.

## 2026-11-14 (publishing run, night 110)
- Corrected misprints in emend.json: P561L03 (verse) اسُّلُوُّ→السُّلُوُّ (dropped lām); P562L04 والدة→والده (the father; the verb and name are masculine); P562L05 and P562L17 شاة→شاه (Sulaymān Shāh); P562L07 فاما→فلما, بانباعه→باتباعه; P563L04 and P563L12 اى→الى. Kept as printed and flagged in the notes: P561L20 verse «سَوُءِ لَمْ يَصْطَبِرْ», damaged and obscure, vocalised as printed and left untranslated («…») in l and i; اَحْسَنُ (P561L11) and حُلْوُ (P561L19) with printed vowels the grammar does not want; انصبو (no final alif) and وانصبوا, read as form IV; أتني for iʾtinī; فرأي; run-together عشرعاما, يرجوانه, جاؤابه, ودعواله, وارادان. شهر زاد is set as two words at P563L17. The archive was not changed.
- Library label: `Night 110 · The Lover and the Beloved, continued`. The night ends as Tāj al-Mulūk sees the pale young merchant; if a new inner tale is named in night 111, the next run labels it then.
- Shared glossary: 12 existing entries extended with this night's sense (لِمَا, عَلَمَ, بِحَقِيقَةِ, بِالثَّمَنِ, بِالصَّيْدِ, بِالْمَلِكِ, بِجَمِيعِ, بِتِلْكَ, بِخَبَرِ, شَاهْ, الْمَنْزِلَ, الِاصْفِرَارُ) and الْفُلَانِيِّ made general; nothing overwritten with a different meaning.
- Next: nights 111 and 112 are complete and unpublished; the next two firings should publish them.

## 2026-11-14 (publishing run, night 111)
- Corrected misprints in emend.json: P565L03 بضاعنك→بضاعتك, P566L03 استنعت→امتنعت (as printed on P566L08). The printed damma on عُليّ (P564L19) is a slip for ʿalayya: the text is pointed عَلَيَّ and the note says so. emend.json cannot record it, since the bare letters are the same. Kept as printed and flagged in the notes: verse P564L03 يَاصَاحِ (run together, one dot faint; read yā ṣāḥi); P564L04 وَقُلْ (abrupt, perhaps for wa-qultu); P564L11 تَخْدَعُوا pointed active where the sense wants tukhdaʿū; P565L09 شَهْدِ without tanwīn; P565L20 وَبِي حُبِّكُمْ, hard to construe, translated as "for love of you"; رأه (P564L14), pointed with a dagger alif; run-together السعيدان, لَوْمَسَّ, قهراعنه. The archive was not changed.
- Library label: `Night 111 · The Lover and the Beloved, continued`. The young merchant has not yet been named or given his own tale heading, so nothing changes. Nothing to decide.
- Next: night 112 is complete and unpublished; the next firing should publish it.

## 2026-11-14 (publishing run, night 112)
- Corrected misprints in emend.json: P568L07 روئحي→روائحي (dropped alif), P568L11 and P568L13 فرق→فوق. Kept as printed and flagged in the notes: verse P566L16 لَا اَكْذَبَ اللّٰهَ (pointed as a past tense; translated as lā akdhibu, “I will not lie to God”); P566L14 صَفْوَ in the accusative; P566L19 اُجَرِّعُهُ, hard to construe exactly; اري with ي; مسطبة with س; masculine بِهِ for the feminine فرجية; run-together السعيدان, مالم, مايحتاج; شهر زاد as two words. The archive was not changed.
- Library label: `Night 112 · The Lover and the Beloved, continued`. The young merchant is named this night: he is ʿAzīz, and his cousin is ʿAzīza (P567L12–13, in his father's words). The print still gives his story no heading of its own, so the label is unchanged. If the owner would like the inner tale labelled “ʿAzīz and ʿAzīza” from here on, that is a relabel for an attended session. Nothing waits on it.
- Next: night 113 is incomplete (tail unread), so the next firing should transcribe.

## 2026-11-14 (transcribing run, PDF 591-598 = pp. 569-576)
- **P574L01 recovered by hand.** The line detector dropped the first line of PDF 596 and the bands clip it; both passes began the page at «ازل كذلك». The run rendered the page top at 250 dpi, read the line («استيقظ فاجدها سهرانة من اجلي ودمعها يجري على خدها ولم»), inserted it in both passes, and the adjudicator confirmed it letter by letter and the 573→574 join. Worth knowing: a dropped *first* line is not caught by the double-pitch GATE (it flagged p596 only after line 9), so a run should compare the line count with the page image when a page comes out short (this one had 20 lines against the usual 22).
- **هذه / هذة.** The adjudicator read P571L06 as وهذة, but the glyph on that crop is the same as هذه on P569L08 (same type, same mark after the hā'), and the archive writes it هذه 543 times against 22. Decided meanwhile: archived as وهذه, for consistency. If the owner wants the 22 earlier هذة re-examined, that is a separate pass.
- For the publishing runs (all archived as printed): P570L02 وانبلت (for واقبلت) and P570L03 النياب (for الثياب), both clear misprints; P570L16 verse اَنْقَلِ (the rhyme may want another word; low sense confidence); P572L12 prose وَاَدْلَته printed fully vowelled; P573L03 verse اَمِيْرِىْ فِى (one sukun ambiguous, low confidence); P576L13 احدٰهما with dagger alif; P569L06 رأيحة/الرأيحة (hamza on the alif, undotted tooth after: printed form of رائحة); P574L16 هنّاك; P575L02 رفصت/P575L17 فرفصته (dots as printed); run-together لايكتب, يابنت, ماحصل, تريدان, انهالك, ولابها. P572L18 «تنشد هذه الابيات» ends in a kashida, not a filler rule.
- Nights 113 and 114 are now complete and unpublished; the next two firings should publish them.

## 2026-11-14 (publishing run, night 113)
- Corrected misprints in emend.json: P570L02 وانبلت→واقبلت, P570L03 النياب→الثياب. Kept as printed and flagged in the notes: verse P570L16 اَنْقَلِ (no sense, breaks the -di rhyme; probably ṣaḥīḥi al-naqdi, possibly al-naqli; left untranslated «…»); P570L19 قَدْ جَرَتْ … (obscure, no clear subject); P570L21 مَوَاسِمْ repeated as a rhyme word; P569L21–P570L01 تفصيل الا جمال, read as tafṣīla al-ijmāli with the print's split kept (doubtful); رأيحة/الرأيحة for rāʾiḥa; علي for ʿalā (P569L19, pointed ʿalā with a dagger alif); run-together لايكتب, يابنت, لاتسألي, لابدان, انهالك, لوكنت. The archive was not changed.
- Library label: `Night 113 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 114 is complete and unpublished; the next firing should publish it.

## Night 114 (published 2026-11-14)
- No misprints corrected; emend.json unchanged. Kept as printed and flagged in the notes: P574L20 جبينها قد انفتح سال دمها (no و before سال; possibly a dropped letter, possibly asyndeton — doubtful, so kept); P573L03 verse يَنْصِفُ (print's vowel for yunṣifu); P572L22 verse حَمَّلْتِنِي pointed feminine in a poem addressed to a man; Middle Arabic forms استمرّيت, حمتني, هنّاك, رفصتها, سهرانة, قضي, ماجري, الخمس/الخمسة اصابع. The archive was not changed.
- P572L14 جذبتها: the feminine pronoun has no clear antecedent; translated "drew back from the window", with a note.
- Library label: `Night 114 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 115 is not yet complete (tail unread); the next firing should transcribe.

## 2026-11-14 (transcribing run, PDF 599-606 = pp. 577-584)
- Both passes on the strongest model: 28 disputes over 8 pages (3.5 a page). Night labels 116 (P579L01, dropped by the line detector and read from the band by both passes), 117 (P581L12) and 118 (P584L04) are each printed centred on their own line; all three carry `h` (P584L04 set by hand).
- The adjudicator, spot-checking p606 (no disputes) and p604, proposed four changes to readings both passes agreed on: P584L02 «جنّ الليل» for «جنّ المليل», رأسى for رأسي, P584L19 «لما رات» for «لمارات», P584L20 شيأ for شياً; and P582L02 «فاذكرلها» for «فاذكر لها». The run looked at the crops: on P584L02 the second word shows a loop after the first lām, so «المليل» stays (a misprint for الليل, as printed again correctly at P584L07); the spacing and marks of the others are doubtful. Decided meanwhile: the passes' agreed readings stand. Nothing to decide unless the owner wants them re-read.
- For the publishing runs (all archived as printed): P584L02 جنّ المليل (for الليل; P584L01–02 are repeated as L06–07 after the night label, in the print itself); P582L04 البهتان (for البستان); P578L01 بكاوشديدا (for بكاء شديدا); P580L08 verse الْعَرَامِ (undotted ع; sense wants الغرام); P581L22 شرّما (low-medium confidence, perhaps a misprint); P581L21 شياْ with a small circle over the alif (low confidence); P579L04 هذة. Run-together words kept: لاانشدها, شاءالله, اذكرلها, لمارات, السعيدان.
- Nights 115, 116 and 117 are now complete and unpublished; the next three firings should publish them.

## Night 115 (published 2026-11-15)
- Corrected misprints in emend.json: P575L15 فقل→فقد ("for your joys have drawn near"), P577L19 انت→اتت ("she came to me"), P578L01 بكاوشديدا→بكاء شديدا (و for ء, and the word space restored). Kept as printed and explained in the notes: P577L04 وعلا نور النهار (read as the darkness rising over the daylight, not emended); P576L13 احدٰهما; P576L15 اسوء; P577L08 مضيأ; P575L06 شيء ما كان (nominative after kāna); رأسي treated as feminine (خفّت راسي); P576L01 المسطبة spelled with س; verse P577L15 وَبُيُوْتُ (read as a subject put first); words printed run together, such as ولابها, تريدان, اولا, مابي, ادعوالله, مماهي, يابن, ماحصل, شاءالله, مايأتي, يارب, لاانشدها, مابين. The archive was not changed.
- Library label: `Night 115 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: nights 116 and 117 are complete and unpublished; the next two firings should publish them.

## Night 116 (published 2026-11-15)
- No misprints corrected; emend.json unchanged. P579L22 تلّفت: the print's shadda is on the lām; pointed talaffattu (shadda on the fā’), with a note, as for عُليّ in night 111 (a misplaced mark, so no emend entry). Kept as printed and flagged in the notes: verse P580L08 الْعَرَامِ (ʿayn for the expected ghayn; ʿarām is a real word, so doubtful; translated as "passion"); يَلُمْنِي (shortened yalūmunī); بطني treated as feminine; هذة; ثلٰثا; ى for final ي (الصينى, زبادى, يدى, فى, عمى, معشوقتى); run-together السعيدان, مابين. The archive was not changed.
- Library label: `Night 116 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 117 is complete and unpublished; the next firing should publish it.

## Night 117 (published 2026-11-15)
- Corrected misprints in emend.json: P582L04 البهتان→البستان (“the garden”), P584L02 جنّ المليل→جنّ الليل (the next night repeats the phrase correctly at P584L07). Kept as printed and explained in the notes: P581L22 كفاك الله شرّما (read sharra mā, “the evil of what…”; possibly a misprint for شرّها, but that is a guess); P581L21 شياْ with a sukūn over the alif; P583L17 ملأن (malʾānu, diptote); P583L19 تامريني (taʾmurīnī for taʾmurīnanī); matʿūb; الراس and الي spellings; verse P582L21 مِنْ الدُّمُوعِ (sukūn before the article, read mina al-); run-together مايحتاج, ماتيسر, اذكرلها. The archive was not changed.
- ʿAzīza explains three of the four objects (the ṭāb stick, the date-stone, the carob seed) and says nothing of the knucklebone; the note says so for this night only.
- Library label: `Night 117 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 118 is not yet complete (tail unread); the next firing should transcribe.

## 2026-11-15 (transcribing run, PDF 607-614 = pp. 585-592)
- Both passes on the strongest model: 27 disputes over 8 pages (3.4 a page). Night labels 119 (P587L07), 120 (P590L14) and 121 (P592L19) are each printed centred on their own line; all three carry `h`.
- `nights_index.py` did not understand الموفية للعشرين بعد المائة (Night 120) and reported an ordinal MISMATCH. The run added that form ("completing" + tens + بعد + hundred) to `ordinal_number`, in the way earlier runs added new forms; it now reads 120, and the older forms (الموفية للستين, الموفية للمائة, الحادية والعشرون بعد المائة) still parse. Nothing to decide.
- P592L10: the adjudicator ruled ولكنك (low confidence); the run read the crop and found one kaf only (alif, lam into a mim loop, dotted nun, final kaf), so the archive keeps the print, والمنك, a misprint for ولكنك. For the publishing run: emend in `emend.json`.
- Also kept as printed, for the publishing runs: P585L06 ذبحنك (one dot; sense ذبحتك); P591L02 ثيأ (three dots; for شيأ); P591L04 با (one dot below; for يا); P590L16 خطيئها (sense خطيئتها; both passes agree); run-together ومااسم, نورالهدى, مافعلت, لاصغيرة; P588L03 وَاٰخِرُ with a dagger alif.
- The running header on PDF 613 prints ٤٩١ for ٥٩١ (printer's error; headers are not transcribed, the archive is unaffected).
- Nights 118, 119 and 120 are now complete and unpublished; the next three firings should publish them.

## Night 118 (published 2026-11-15)
- Corrected misprint in emend.json: P585L06 ذبحنك→ذبحتك (“she will slaughter you”). Kept as printed and explained in the notes: P587L01 مسّرة (shadda printed on the sīn; read masarra, mark kept, as for P508L14); verse P587L02 لَمْ اَخْلُ … الْكَأْسُ (printed vowels do not construe; sense lam ukhli … al-kaʾsa, translated so); verse P586L13 قَلْبُكَ (masculine “your”, kept); اَهْنَى for ahnaʾ; غطاوها (spoken form of غطاءها); مضي, طولى, يدى (read yadī), شياً, وجدتّها (wajattuhā); run-together ومازلت, لمارات, لاتنس. The archive was not changed.
- The night contains a frank love scene between ʿAzīz and the lady (P586L16–P587L03); it is translated in full, as the conventions require. No passage omitted.
- Library label: `Night 118 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: nights 119 and 120 are complete and unpublished; the next two firings should publish them.

## Night 119 (published 2026-11-15)
- No misprints corrected; emend.json unchanged. Kept as printed and explained in the notes: P588L04 قلت where ʿAzīza speaks (read qālat, pointed قٰلَتْ with a dagger alif, the edition's defective spelling); P588L16 حلها (ḥālihā, dagger alif); P587L15 اللتي; P588L07 البيت الشعر (for bayt al-shiʿr); P589L05 البيتين الذي (singular relative after a dual); P589L12 فتحت عيناها (nominative dual as object); P587L12 فاخذته (masculine pronoun for the cloth); spoken اشغلني, باست, ما تقرب لك, رح, متشوش, عياط; run-together السعيدان, ومااسم, نورالهدى. The archive was not changed.
- Library label: `Night 119 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 120 is complete and unpublished; the next firing should publish it.

## Night 120 (published 2026-11-15)
- Corrected misprints in emend.json: P590L16 خطيئها→خطيئتها (“her sin”), P591L02 ثيأ→شيأ, P591L04 با→يا, P592L10 والمنك→ولكنك (as the transcribing run recommended). Kept as printed and explained in the notes: P590L15 الشاب عزيز (name without accusative alif, read ʿAzīz without case ending); P590L18 علي for ʿalā; P591L06 آلاخرة (madda on the article's alif; read al-ākhira) and سلامت (open tāʾ); P591L09 هذين الكلمتين (masculine demonstrative); P591L08 يقول for a command; P591L13 ارني (masculine imperative to his mother); مقالى; run-together وماصدقت, مافعلت, وماكنت, ولاخداعنا, لاصغيرة. The archive was not changed.
- Library label: `Night 120 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 121 is not yet complete (tail unread); the next firing should transcribe.

## 2026-11-15 (transcribing run, PDF 615-622 = pp. 593-600)
- Both passes on the strongest model: 24 disputes over 8 pages (3 a page). Night labels 122 (P594L19), 123 (P597L09) and 124 (P599L21) are each printed centred on their own line; all three carry `h` (P597L09 and P599L21 set by hand, as in earlier batches).
- The running header on PDF 618 prints ٤٩٦ for ٥٩٦ (printer's error, like ٤٩١ on PDF 613; headers are not transcribed, the archive is unaffected). PDF 617 reads ٥٩٥ and PDF 619 ٥٩٩, so there is no missing or duplicated leaf.
- Kept as printed, for the publishing runs to consider for `emend.json`: P594L03 دعها (sense معها, the mim likely broken); P594L06 قاعيدهما (sense فاعيدهما); P594L13 الرمان (sense الزمان in طوارق الحدثان / الزمان; no dot seen on the zay); P595L19 بغد (dot over the ʿayn; sense بعد); P597L13 اقبلب (sense اقبلت); P598L20 الوفاو (waw for hamza; sense الوفاء, the same phrase is printed الوفاء مليح on p. 593); P593L14 حتي. Adjudicator chose ولم (not وام) at P593L15 with medium confidence. P600L13 (verse) هٰذَا is low confidence: a dagger alif and one fatha, placement ambiguous.
- Nights 121, 122 and 123 are now complete and unpublished; the next three firings should publish them.

## Night 121 (published 2026-11-15)
- Corrected misprints in emend.json: P594L03 دعها→معها, P594L06 قاعيدهما→فاعيدهما, P594L13 الرمان→الزمان (as the transcribing run suggested). Kept as printed and explained in the notes: قلت for qālat (dagger alif); حتي; كاس, راس, شاني (no hamza); قماشى; مامعني; هذين الكلمتين; ذلك الحال; اشتاقت نفسي الذهاب (no الى); verse تادّب (no hamza), يَامَيَّت (fatḥa printed on the yāʾ, read mayyita), law + jussive اَسْتَطِعْ, الْمُنْدَافِق (not a dictionary form; read as al-mundafiq/al-mutadāfiq, “gushing”); run-together شاءالله, ولاباحت, كلمابتّ, ومازلت, ولاحزن, لاادري. The archive was not changed.
- Library label: `Night 121 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: nights 122 and 123 are complete and unpublished; the next two firings should publish them.

## Night 123 (published 2026-11-15)
- Corrected misprints in emend.json: P597L13 اقبلب→اقبلت, P598L20 الوفاو→الوفاء (as the transcribing run suggested). Kept as printed and explained in the notes: P599L03 ولاد واهي (space misplaced in ولا دواهي; spacing rule); العجوزة (spoken feminine); الحيوة; وتقوى (ى for final yāʾ); عزيز without accusative alif; ولولا هي; ولا بقت; على حيلها; run-together السعيدان, الاقفل, لايصلح, اقدران. The archive was not changed.
- The young woman's frank speech (P599L08–L14, نيك) is translated in full, as the conventions require. No passage omitted.
- Library label: `Night 123 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 124 is not yet complete (tail unread); the next firing should transcribe.

## 2026-11-15 (transcribing run, PDF 623-630 = pp. 601-608)
- Both passes on the strongest model: 25 disputes over 8 pages (about 3 a page). Night labels 125 (P602L01), 126 (P603L16), 127 (P605L10) and 128 (P607L07) are each printed centred on their own line; all four carry `h` (P603L16 and P607L07 set by hand). Lines the detector missed and both passes recovered from the bands: P605L09 (the short line الكلام المباح that closes Night 126), P606L12 (فيها هذه الابيات, before the verse on p. 606), and a merged crop split on p. 604.
- Kept as printed, for the publishing runs to consider for `emend.json`: P603L08 المتزوّح (no dot under the final letter; sense المتزوّج); P602L15 هذه الليلة (second lam faint but read as lam, so no emendation needed); P606L08 لأ (hamza printed on the negative لا); P605L16 على غير استوأ (hamza over the final alif; sense استواء); P607L05 اذ اغبت (spacing; sense اذا غبت); P608L11 الخرفة (one dot; sense الخرقة); P601L01 عزيزان (run together, for عزيز ان). Run-together غيرالذي, واذابزوجتي, هذاالبكاء, وهوميت, لَوْمُتُّ, وارجوالله, ومافعلت.
- Nights 124, 125, 126 and 127 are now complete and unpublished; the next four firings should publish them.

## Night 124 (published 2026-11-16)
- No misprints corrected. Kept as printed and explained in the note: P600L04 وانت (no sense here; either وأتت, one dot, or وبانت, a letter lost — two readings, so the doubtful-reading rule applies, not the misprint rule). P601L01 عزيزان read as the vocative عزيز run together with إنّ, as the transcribing run suggested.
- The wedding night (P600L03–P600L17, with the verse P600L12–13) is between the married adult couple and is translated in full, as the conventions require. No passage omitted.
- Library label: `Night 124 · The Lover and the Beloved, continued`. Nothing to decide.
- Note: this firing's checkout had a local `main` that had diverged from `origin/main` (50/50 commits); the run worked from `origin/main` and left the local branch alone. No effect on the repository.
- Next: nights 125, 126 and 127 are complete and unpublished; the next three firings should publish them.

## Night 125 (published 2026-11-16)
- Corrected misprint in emend.json: P603L08 المتزوح→المتزوج (as the transcribing run suggested). Kept as printed and explained in the notes: اجئ (yāʾ only as hamza seat); run-together لاعلم, مالم (twice), مابقي, لابد; colloquial اريد منك انك تحكي, حكى على, قعدت انتظرتك, اقدر ما اخليك. Two idioms not found in the classical dictionaries are translated by best reading and flagged as uncertain: سالما بشحم ("safe with fat", i.e. unharmed) and الحزمة الدفرة ("the stinking bundle", her insult for the wife). The archive was not changed.
- No passage omitted. Library label: `Night 125 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: nights 126 and 127 are complete and unpublished; the next two firings should publish them.

## Night 126 (published 2026-11-16)
- No misprints corrected. Kept as printed and explained in the notes: لضوؤ (the name spelled with hamza on wāw); رجلاي, يداي (nominative dual for oblique); يضرباني (masculine dual for two women); لا يمكن اتركك (no أن); راس (no hamza); رفصتني (spoken for rafasa); جبنّا (shadda printed; read jubunn, cheese); run-together مابقي, ياسيدتي, ياعزيزة, ولابد, غيرالذي, ولالي, ولاحاجة, واذابزوجتي. ملّس على راسك is not in the classical dictionaries; translated "stroke your head" and flagged as uncertain. The archive was not changed.
- The mutilation scene (P604L12–P604L21, the lady castrates ʿAzīz) is violence between adults and is translated in full, as the conventions require; the `about` says the night contains it. No passage omitted.
- Library label: `Night 126 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 127 is complete and unpublished; the next firing should publish it.

## Night 127 (published 2026-11-16)
- Corrected misprints in emend.json: P605L12 تاج الملك→تاج الملوك (dropped wāw in the name); P606L08 لأ→لا (stray hamza on the negative). Kept as printed and explained in the notes: استوأ (hamza on a final alif, for istiwāʾ); الوداعة (for wadīʿa, 'deposit'); اذ اغبت (space set one letter early, for اذا غبت); حست (spoken for أحسّت); تري, جري (ى written ي); كدت ان اغمي (perfect after kāda an); run-together ياهل, ياولدي, مافعلت, قدمات, هذاالبكاء, وهوميت, ماحصل, وارجوالله. The verse (P606L13–19) is copied as printed; its fa-mā in line 5 is read as a filler and noted. The archive was not changed.
- No passage omitted. Library label: `Night 127 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 128 is not yet complete (tail unread); the next firing should transcribe.

## PDF 631–638 (printed pp. 609–616, transcribed 2026-11-16)
- Nothing for the owner to decide. Night labels for 129 (P609L13), 130 (P611L14) and 131 (P613L12) are each printed centred on their own line; all three carry `h`.
- The orchestrator changed four readings after the adjudication, from the crops: P635 (printed P613L22) the adjudicator had normalised شىء (undotted ى with hamza) to شيء; restored as شئ, the archive's usual spelling of that print form. Sukuns added on undisputed verse words both passes had missed: P609L04 قَالَ لِيْ, P612L09 فِيْ كَبِدِيْ.
- Left as read, possibly worth a later look: P609L01 اولا (a shadda-like mark over the و, read as doubtful and omitted); P611L14 للثلثين (the adjudicator thought it saw a dagger alif; not clear on the crop, omitted).
- Kept as printed, for the publishing runs to consider for `emend.json`: P612L05 وزبره (one dot below; sense وزيره); P613L09 ولعزير (no dot; sense ولعزيز); P614L20 تأج (hamza on the alif of تاج); P613L04 جأبه (for جاء به). Run-together words kept as printed: لاباس, بنتامن, شهرمان, اذراى, نَحْوَارْضِكُمْ, يَامُنْتَهَى, وقرّعينا (twice).
- Nights 128, 129 and 130 are now complete and unpublished; the next three firings should publish them.

## Night 128 (published 2026-11-16)
- Corrected misprint in emend.json: P608L11 الخرفة→الخرقة (as the transcribing run suggested). Kept as printed and explained in the notes: P609L01 اولا read as aw lā, "or not" (a possible shadda would give awwalan, "first"; noted); سنه (ه for ة); بنت الدليلة المحتالة (read "the daughter of Dalīla the Wily", the article and the descriptive reading noted); تصدم به الناس (read "dazzles people with it", flagged uncertain); spoken تتباعد/تتزوج بها/تغيب as requests, لعل + verb, لم تنشف, فراقي لـ; run-together ماكتبته, مافيها, ولازلت, مابي, ولازالت, ومافعلت, وماجدّد. The verse (P609L04–05, P609L07–08) is copied as printed. The archive was not changed.
- Four existing glossary entries (بِيَ, بِهَذَا, بِهَذِهِ, بِهِ) had this night's sense of بِـ appended; no meaning was overwritten.
- ʿAzīz's frank line about his mutilation (P608L21, آلة) is translated in full. No passage omitted.
- Library label: `Night 128 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: nights 129 and 130 are complete and unpublished; the next two firings should publish them.

## Night 129 (published 2026-11-16)
- Corrected misprints in emend.json: P609L18 وتصدي→وقصدي ("and my purpose"; a ت for ق); P611L10 دينا→دنيا (letters transposed in the name). Kept as printed and explained in the notes: شيأ (twice); الظمأن (no madda; long ā marked with a dagger alif in the vocalisation); بطواشي; باب الريح (read as a small wind-door or hatch, flagged uncertain); فاخذهم (masc. pl. pronoun for the dirhams); تحكي لي as a request; نظرت لها; final ى in فى, تجرى, باكى, سألتنى; run-together ماجرى, وماهو, لاباس, وعادبه. The archive was not changed.
- ʿAzīz's frank line about his mutilation (P610L19–20, آلة رجال) is translated in full. No passage omitted.
- Library label: `Night 129 · The Lover and the Beloved, continued`. Nothing to decide.
- Run note: the container's local `main` ref had diverged from `origin/main` (stale commits not on the remote); this run worked from `origin/main` and left the stale ref alone.
- Next: night 130 is complete and unpublished; the next firing should publish it.

## Night 130 (published 2026-11-16)
- Corrected misprints in emend.json (all three as the transcribing run suggested): P612L05 وزبره→وزيره; P613L04 جأبه→جاءبه (jāʾa bihi, kept run together as printed); P613L09 ولعزير→ولعزيز. Kept as printed and explained in the notes: السعيدان (al-saʿīd anna run together); للثلثين (no long alif); عصاة for ʿaṣā, "stick" (final tāʾ marbūṭa); final ى in تشتهى, ابى, يغصبنى; run-together بنتامن, ولابد, لاتحب (twice), ياملك; شهر زاد set as two words. The verse (P612L09–12) is copied as printed. The archive was not changed.
- No passage omitted. Library label: `Night 130 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 131 is not yet complete (tail unread); the next firing should transcribe.

## PDF 639–646 (printed pp. 617–624, transcribed 2026-11-16)
- Nothing for the owner to decide. Night labels for 132 (P618L17) and 133 (P622L17) are each printed centred on their own line; both carry `h`. P618L17 prints والثلٰثون (dagger alif over the lām), not الثلاثون as the draft and both passes had; corrected by the orchestrator from the crop.
- PDF 639 has a two-line running header (the tale title, with the page number ٦١٧). Both passes took it for a section heading; the orchestrator removed it before the diff, since P616L23 (نكتري لك) runs straight on into P617L01 (دكانا).
- The orchestrator changed one undisputed word from the crop: P617L06 تجّاربة (one dot below, as printed; both passes had تجّارية; the adjudicator noticed it).
- Low confidence: P620L16 فتنقّشوا (the shadda hides the dots; sense فتنشّفوا); P624L07 ولوفّتت (a single dot, so ف; neither pass had it). Medium: P620L01 اتسما (a tooth, not the loop of ق; sense اقسما).
- Kept as printed, for the publishing runs to consider for `emend.json`: P617L08 سرق (sense سوق); P617L06 تجّاربة (sense تجّارية); P618L01 ينفرّجا (sense يتفرّجا) and بالدنكم (sense ببلدكم); P618L06 زئدا (sense زائدا); P618L07 ابنات (sense البنات); P619L07 تعد (sense قعد); P620L01 اتسما (sense اقسما); P620L08 وبنظفانك; P620L15 اى (lām missing; sense الى); P620L16 فتنقّشوا; P624L01 وحضوصا (sense وخصوصا); P624L07 ولوفّتت.
- Night 131 is now complete and unpublished; the next firing should publish it. Night 132 is complete too, but `nights_index.py --next` gives one night at a time.

## Night 131 (published 2026-11-16)
- Corrected misprints in emend.json: P614L20 تأج→تاج; P615L20 الارباح→الارياح (verse; "the winds"); P617L06 تجّاربة→تجّارية; P617L08 سرق→سوق; P618L01 ينفرّجا→يتفرّجا and بالدنكم→بلادكم (letters transposed plus a stray tooth; the feminine هذه that follows fits بلاد — the least certain of the eight, noted for the reader); P618L06 زئدا→زائدا; P618L07 ابنات→البنات. Kept as printed and explained in the notes: شئ, شيأً, بقضائُها (the print's ḍamma kept), فانزلوا (causative where فنزلوا is expected), تاجر read as the verb tājara, هذة ×3, عندة, final ى/ي habits (ابنتى, غصبنى, بماجري, تقضي, اعطي), لينا ولك (li-yunāwilaka split in two), run-together وامران, اذراى, كلواحد, هاهو, لاباس and the usual ما-/يا-/لا- forms. The verse (P614L11–12, P615L06–10, P615L18–21) is copied as printed apart from the one corrected word. The archive was not changed.
- The headman of the market is said to prefer the love of boys and to "incline to sourness" (الحموضة, read as slang for the same taste, flagged uncertain); the two he has his eye on are Tāj al-Mulūk and ʿAzīz, grown young men. Translated in full; no passage omitted.
- The night was pushed once the gate passed, and the whole-night review's fixes followed in a second commit the same run. 25 shared glossary entries that carried other nights' senses had this night's sense appended (e.g. الْبُعْدِ, مَاهَذَا, الْعَرِيفُ, سَلَّمَ); nothing was overwritten.
- Library label: `Night 131 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 132 is complete and unpublished; the next firing should publish it.

## Night 132 (published 2026-11-16)
- Corrected misprints in emend.json: P619L07 تعد→قعد; P619L16 البيتن→البيتين; P620L01 اتسما→اقسما; P620L08 وبنظفانك→وينظفانك; P620L15 اى→الى. Kept as printed and explained in the notes: P620L16 فتنقّشوا (low-confidence in the archive; the sense needs فتنشّفوا, "they dried themselves", and the translation follows the sense); والبسوا (causative for لبسوا); يدة ×2, غيرة, هذة ×2 (ة for ه); شيأً, شياً; لايش; فماصدق, ومازال, ماقاله run together; the print's وَدَدْتُهُمَا (for wadidtu) and nominative دُمُوْعُهَا in verse. All verse (P619L05–06, L17–18, L20; P620L11–12, L21–P621L01; P621L04–05, L09–11, L13–14) is copied as printed. The archive was not changed.
- The headman's lust for the two young men (their quivering buttocks, his verses, the bath scene) is translated frankly; no sexual act is described and the two are grown young men. No passage omitted.
- Library label: `Night 132 · The Lover and the Beloved, continued`. Nothing to decide.
- Run note: the container's local `main` ref had again diverged from `origin/main`; this run worked from `origin/main` (the stale ref is kept as `old-local-main` in this container only).
- Next: night 133 is not yet complete (tail unread); the next firing should transcribe.

## PDF 647–654 (printed pp. 625–632, transcribed 2026-11-16)
- Nothing for the owner to decide. Night 134's label (P628L13) is printed centred on its own line and carries `h`. The running header sat in the detector's first crop on six of the eight pages; the passes were told to skip it, and both did.
- Low confidence: P628L06 اَلَسْتَ (worn type; one pass read اَمَسْتَ); P631L01 عَلَى (worn first letter). P630L22 مُنْدَفِعاً vs مُنْدَفِعًا is only where the tanwīn is encoded.
- The adjudicator turned three long strokes into kashida, not filler (P625L12 شعر, P627L02 and P631L07 الابيات). Final ة on هذة, واعطاة and خوفة is as printed. The kasras under the feminine ك on P628L02–03, L19 (اجازيكِ, ميزانكِ, فانكِ, عليكِ, فيكِ) were checked on the image and are printed.
- Kept as printed, for the publishing runs to consider for `emend.json`: P627L04 بَامَغْرُورُ (sense يَا مَغْرُورُ); P627L06 ضِيَاوَ; P627L07 وَالْقَدَرِ (sense perhaps وَالْقَمَرِ; doubtful, keep unless sure); P627L19 فالت (sense قالت); P627L22 لا بداني (spacing); P628L05 وَاعَرَبِي (sense وَاعَجَبِي); P630L05 ها تيها (sense فاتيتها?; doubtful); P631L21 لو لاخوفى (spacing).
- Night 133 is now complete and unpublished; the next firing should publish it.

## Night 133 (published 2026-11-17)
- Corrected misprints in emend.json: P624L01 وحضوصا→وخصوصا; P625L06 اى→الى; P625L07 وانسع→واتسع; P627L04 بامغرور→يامغرور (verse); P627L19 فالت→قالت; P628L06 واعربي→واعجبي (verse; "O my wonder!"). Kept as printed and explained in the notes: P624L07 ولوفّتت (low-confidence in the archive; read as wa-law fattat(at), "even if livers crumbled", the print's doubling mark kept over the fāʾ; flagged doubtful); P627L07 وَالْقَدَرِ (al-qamar would suit the sun better, but the poem already rhymes twice on qamar; kept and translated "destiny"); P627L06 ضِيَاوَ; P627L08 لَاُصْلِبَنَّكَ (the print's ḍamma); بكلوة يدها (read as the heel of the hand, flagged uncertain); فغمزة, هذة (ة for ه); توْاخذينى (the print's mark kept); حيوة/حيوتي; run-together العجوزان, الاملك, مااسمك, اوفيه, بمافيه, لا بداني, بدان and the usual يا-/ما-/لا- forms. The archive was not changed.
- The old woman's arousal (she "sweated in her trousers", rubs between her thighs) and her wish that the young man lie between Dunyā's breasts are translated frankly; all are adults. No passage omitted.
- Library label: `Night 133 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 134 is not yet complete (tail unread); the next firing should transcribe.

## PDF 655–662 (printed pp. 633–640, transcribed 2026-11-17)
- **For the owner, when convenient (nothing waits on it):** the verse at the top of P636 (L01–04, PDF 658) is printed with broken, faint type that even a 600-dpi render does not recover. Six words could not be read from the ink and are set in the archive as `[…]`. Probable readings, from the surviving marks, not used: L01 جَهْلًا (after وَظَنَنْتُ) and تُفْنَى/تُجْنَى (before عَلَيْهِ); L02 the two words before الْاَمْنَاحِ (اسبته/اسنانه? بالمعاني/بالمعاذي?); L03 فَعَلِمْتُ (line start) and تَحْتَ (before لِي جَنَاحِيْ); L04 الْغَرَامِ (after عُشِّ). Other words in these four lines were read from letter shapes whose dots are lost (وَظَنَنْتُ, دَيِّنٌ — probably a broken هَيِّنٌ, وَتَخُصُّ, تُنَالُ, وَلَوَيْتُ) and are low-confidence. If you have another copy of the page, these lines are worth a look; a publishing run should give the reader a gap note for the `[…]` words.
- **Convention conflict, decided meanwhile:** `conventions.md` says an illegible word is written `[illegible]`, but `validate_archive.py` fails any line with Latin letters. This run used `[…]` instead (passes the gate, reads as a lacuna). If you prefer another marker, say so and the conventions and gate can be aligned.
- **Model rule (README "Models"):** Pass 2 started on Sonnet for PDF 655–658. All four Sonnet agents read only the bands and skipped the 2x crops, and one repaired a misprint (وفارتت→وفارقت); disagreements ran at 13 a page (53 on 4 pages). Per the runbook the whole batch's Pass 2 was rerun on the strongest model (40 disputes over 8 pages). Recent batches had already run both passes on the strongest model; that remains the practice.
- The orchestrator added seven checks to the adjudication where both passes agreed but the image looked otherwise. Results: P633L11 وفارتت (misprint for وفارقت, kept as printed); P634 اريدان, تريدان, انشاء and انشاءالله printed joined; P640L11 للعجوزكوني printed joined; P640L01 الخامسة has no mark (the stroke is the lām); خوفا من الفضيحة confirmed.
- Low confidence: P637L04 فاوصاه (the adjudicator's reading of a broken word; pass 1 had فاوماه, pass 2 فاخفاه; the crop looks like فا وماه). Medium-worth-noting: P640L09 نضمته (ن for ف, no shadda visible); P640L12 وعنٰق (dagger alif, no alif letter); P634L08 الثلٰمائة (dagger alif).
- Kept as printed, for the publishing runs to consider for `emend.json`: P633L11 وفارتت (sense وفارقت); P634L06 تصرا or قصرا (adjudicated); P637L03 ابة (sense ابنة) and انت (sense اتت); P637L06 تالت (sense قالت); P640L09 نضمته (sense فضمته).
- Night 134 is now complete and unpublished; the next firing should publish it.

## Night 134 (published 2026-11-17)
- Corrected misprints in emend.json: P632L01 لتنلتك→لقتلتك; P633L11 وفارتت→وفارقت; P634L08 الثلمائة→الثلثمائة (the print's dagger alif kept); P637L03 ابة→ابنة and انت→اتت; P637L06 تالت→قالت; P638L22 لها→له (the first لها: the nurse tells Tāj al-Mulūk — possibly the author's slip rather than the compositor's; reverse it if you prefer the print); P639L12 الا ان→الى ان. Kept as printed and explained in the notes: ها تيها (هاتيها split), لو لاخوفى, الا وجال (read al-awjāl, flagged doubtful), صفّة and شيُ (the print's marks), فاوصاه (low-confidence in the archive), لا ننل, اريدان/تريدان/انشاء run together, جري/اسعي with ي for ى, the masculine forms for the female dove, امض addressed to Dunyā. The archive was not changed.
- **For the owner, when convenient:** the verse at P636L01–04 has six words the scan does not show (archive `[…]`). The reading text keeps `[…]` there, the unit's note tells the reader the lines are partly unreadable and the translation partly conjectural, and the unit carries `"gap": "P636L01–P636L04"`. This routine's scope does not include the root `gaps.json`, so no entry was added there and `add-passage.html` will not list it yet; to make it fillable, add `{"id": "nights-134", "file": "nights-134.json", "gap": "P636L01–P636L04", "label": "Night 134 · The Lover and the Beloved, continued"}` to `gaps.json`.
- Nothing sexual beyond Dunyā's awakening desire; no passage omitted.
- Library label: `Night 134 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 135 is not yet complete (tail unread); the next firing should transcribe.

## PDF 663–670 (printed pp. 641–648, transcribed 2026-11-17)
- Night 135 (P640L01–P643L17) is now complete and unpublished; the next firing should publish it.
- The night 136 label at P643L18 is printed `الميلة` (misprint for الليلة). It is archived as printed; `nights_index.py` still finds the night. A publishing run should add it to `emend.json` if the reading text shows the label. The line's `"h": true` was set by hand (pass 1 had left it off; every earlier night label carries it).
- Low confidence: P644L03 اَمَا (pass 1 امّا, pass 2 انّا; the adjudicator saw two fathas, no shadda, an undotted middle tooth); P646L11 التفتت (the second letter has no lām stem; it is not استفتت or انتفتت).
- Orchestrator checks (both passes agreed, but may have read by sense). All confirmed as printed. For the publishing runs to consider for `emend.json`: P641L05 `ن` (alif of ان missing: الى ن دخلا); P642L02 بانا (sense باتا); P642L03 وانفق (sense واتفق); P642L13 سعمت (sense سمعت); P645L14 الملول (sense الملوك); P645L19 وآحرا (sense وآخرا); P646L11 وفالت (sense وقالت; both passes had written وقالت, the adjudicator saw one dot); P647 محبور (sense مجبور); P644L05 فابتدأء.
- The ه/ة disputes (شاه, والده, يده, هذه, بلاده etc.) were decided one word at a time from the ink. None showed two clear dots, so all are ه.

## Night 135 (published 2026-11-17)
- Corrected misprints in emend.json: P640L09 نضمته→فضمته; P641L05 ن→ان (الى ان); P642L02 بانا→باتا; P642L03 وانفق→واتفق; P642L13 سعمت→سمعت. Kept as printed and explained in the notes: P641L04 وتحت الملك (perhaps وتخت, "the throne of King Sulaymān Shāh"; doubtful, kept); P642L23 ماشي (unclear: mā shī "nothing" or colloquial māshī; flagged); P641L16 ازدْدتُّ (the print's marks kept); قمشة "whip" (vowels uncertain); العلق (read as a coarse insult); ولدة (ة for ه); run-together للعجوزكوني, وامران, ماجرى, ماكان, ماستر, ماجسرك, شعرابطه. The archive was not changed.
- Glossary: the review found 45 existing shared entries whose wording fitted only the night they were written for (e.g. وَجْهَهَا "her maidenhead", قَبْلَهُ "read qalbahu", فَخَلَعَ "bestowed"); each was rewritten to cover both senses, not overwritten with a different meaning.
- The lovers' nights together are told in stock phrases, translated plainly; all are adults. No passage omitted.
- Library label: `Night 135 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 136 is not yet complete (tail unread); the next firing should transcribe.

## PDF 671–678 (printed pp. 649–656, transcribed 2026-11-17)
- Night 136 (P643L18–P649L06) is now complete and unpublished; the next firing should publish it. The night 137 label at P649L07 is centred on its own line, `h`, printed والثلٰثون with dagger alif.
- Low confidence: P650L14 دنّت (the adjudicator saw one dot above a tooth, not the loop of ق; the sense is دقّت).
- Orchestrator checks (both passes agreed but may have read by sense), decided from the image and archived as printed. For the publishing runs to consider for `emend.json`: P650L14 دنّت (sense دقّت); P651L03, L04, L16 للوزبر/الوزبر (sense الوزير, one dot); P654L02 and L05 اوزبر (no lām printed, sense الوزير); P654L06 اى (sense الى); P651L20 بانية (sense باقية); P655L15 غربس نعمنك (sense غريس نعمتك). Confirmed: P650L03 وذبحت (the draft had ونحت); P649L14 الذّ عيش (two words, shadda printed); P649L05 شهر زاد (two words, ر).
- Marks the adjudicator found that neither pass had: P654L06 الرَحبة (fatha) and P656L21 وَمَضىٰ (dagger alif in the verse).
- The ه/ة disputes (ولده, وولده, جواده, قصره, فلكزه) were decided as ه: no two clear dots.
- P654: the first Pass 1 agent transcribed mostly from the bands, reading only 3 crops. It was rerun properly before the diff, and only the rerun was used.

## Night 136 (published 2026-11-17)
- Corrected misprints in emend.json: P643L18 الميلة→الليلة (night label); P644L05 قئما→قائما and فابتدأء→فابتدأ; P644L19 كترة→كثرة; P645L14 الملول→الملوك; P645L19 وآحرا→وآخرا; P646L11 وفالت→وقالت; P646L15 والده→ولده (Shahramān tells the envoys to let their king know that "his son" is well; the print says "his father"; reverse it if you prefer the print). The archive was not changed.
- Kept as printed and explained in the notes: محبور (read maḥbūr, "glad"); وابيها at P649L01 ("with her husband and her father": Shahramān does ride with them three days; abīhi may be meant); ة for the pronoun ه (والدة, بلادة, خاطرة, بجانبة, هذة); اخرجو; وتوّجه with the shadda on the wāw; ʿAzīz pointed nominative after inna hādhā al-shābba (no alif in the print); the run-together الحذران, لابدان, الذّعيش, الاوتاج, اريدان.
- Left for the transcription pipeline to consider (not changed): P646L09 ساره read sārrahu "told him privately" (sarrahu "gladdened him" also possible).
- The consummation (dakhala bi-, "took her virginity") is one plain sentence between adults; no passage omitted.
- Library label: `Night 136 · The Lover and the Beloved, continued`. Nothing to decide.
- Next: night 137 is not yet complete; the next firing should transcribe.

## PDF 679–686 (printed pp. 657–664, transcribed 2026-11-17)
- Nights 137 (P649L07–P658L14) and 138 (P658L15–P660L21) are now complete and unpublished; the next two firings should publish them, one each. Night 139 begins at P661L01. Both labels are centred on their own lines, `h`.
- `nights_index.py` missed the night 138 label at first. The line after it (P658L16) prints `فالت` for `قالت` (one dot, checked on the image), and the formula pattern required قالت. I added فالت to the pattern in `tools/nights_index.py`, as was done for الميلة. Nothing else changed. A publishing run should put P658L16 فالت→قالت in `emend.json`.
- Low confidence: P659L03 وَاَعَنَابَهَا (verse; five fathas, placement unclear); P663L09 دِع (verse; an unclear mark over the dal left out); P664L04 الْفُؤادِ (one mark read as hamza, no fatha).
- Kept as printed, for the publishing runs to consider for `emend.json`: P659L05 يهزأ ابالرحيق (an extra alif, checked on the image; sense بالرحيق); P662L16 اه (sense انه; no nūn printed). `قضى فكان` (P659L18, P661L15) is the character's name, Qudiyā Fakān.
- The p661→p662 join changes topic abruptly (the mother's speech: "وكثرة احزانك" / "ولم يبعثوا لنا…"). The adjudicator found no gap and no missing line.
- The p681 line "وقول الآخر" (P659L15) had no crop and was read from the band by both passes.

## Night 137 (published 2026-11-17)
- Corrected misprints in emend.json: P650L14 دنّت→دقّت (kettledrums beaten); P651L03 للوزبر→للوزير; P651L04, P651L16 الوزبر→الوزير; P651L20 بانية→باقية; P654L02, P654L05 اوزبر→الوزير; P654L06 اى→الى; P655L15 غربس نعمنك→غريس نعمتك. The archive was not changed.
- Name of Sharrukān's daughter, قضى فكان: vocalised قَضَى فَكَانَ and romanised Qaḍā Fakān ("He decreed, and it came to be", a pair with Kān Mā Kān); the note says Quḍiya is also possible. This is the first night to romanise her name; change it across the nights if you prefer another reading.
- Kept as printed with notes: Middle Arabic and spelling habits (شيأ/شياً, اتمنّي, ايش, ة for ه in وعانقة, نزهه, طأئش), the printed mark in لو تمنّيتُ (P651L23), run-together words (مانسيتني, ولابدان, اولا, اوفي, مايروح, وبعدان, وامران).
- Library label: `Night 137 · The Lover and the Beloved ends / King ʿUmar ibn al-Nuʿmān, continued` (Dandān's story ends and the main tale resumes; I used "continued" rather than "begins" since ʿUmar's tale was already under way).
- Next: night 138 is complete and unpublished; the next firing should publish it (and add P658L16 فالت→قالت to emend.json).

## Night 138 (published 2026-11-17)
- Corrected misprints in emend.json: P658L16 فالت→قالت; P659L05 ابالرحيق→بالرحيق. The archive was not changed.
- Kept as printed with a note (doubtful, not corrected): P659L06 كما قيل فيها الشاعر (probably قال); P660L02 يطلق النظار (perhaps النظر); P658L18 "ام ضوء المكان" for his widow (perhaps ام كان ما كان); P660L07 فاغتاظت بـ.
- Printed verse kept exactly with notes on odd pointing: وَاَعَنَابَهَا (P659L03), شَهْدًا (P659L17, sense perhaps شهداء), رَشَاءُ and لَوَحِظُهُ (P659L14), ثَغَرُ (P660L04), تَكَدَّرَ اَخْلَاقَهَا (P660L19).
- Split/fused words kept as printed: لا شكينك (vocalised لَأَ شْكِيَنَّكَ), هوالّا, هذاوشاع, شهر زاد. قضي with dotted yāʾ read Qaḍā.
- Next: night 139 begins at P661L01 and is not yet complete (tail unread); the next firing transcribes.

## PDF 687–694 (printed pp. 665–672, transcribed 2026-11-17)
- Night 139 (P661L01–P665L07) is now complete and unpublished; the next firing should publish it. Night 140 begins at P665L08 (centred label, `h`).
- Low confidence: P667L13 ذَاقًا (verse; heavy mark over the rhyme, tanwīn probable, a single fatha possible).
- Kept as printed, for the publishing run to consider for `emend.json`: P670L03 بفصة (only one dot, on the fāʾ; sense بفضة). P671L07 بحيوٰة was read from a faint, broken word; the two passes had بدوة and بحيوة.
- The adjudicator logged the 664→665 join as a coverage gap, because it read the archive's printed page numbers as PDF numbers. pp657-664.json is printed 657–664 (PDF 679–686), so there is no gap. The text runs on: the mourning verse ends p. 664, and p. 665 opens "ثم انها امتنعت من الطعام والشراب". Nothing changed.

## Night 139 (published 2026-11-18)
- Corrected misprint in emend.json: P664L08 الارج→الازج (Bāb al-Azaj, the Baghdad gate). The archive was not changed.
- Kept as printed with notes (doubtful, not corrected): P661L07 تخنق (perhaps تخفق, "flutter"); P661L13 ان اباك الحاجب ابا قضى فكان (the Chamberlain is father to neither cousin); P662L16 اه (read as the sigh āh; perhaps انه); P663L07 قطع ياسه; P665L06 والآنان (read as anān, "moaning"); P664L14 بعدت (read baʿudta; baʿudtu possible).
- Printed verse kept exactly with notes: دِع (P663L09, for daʿ), اَصْغِيْ, سَهَرَتْ, لِوَجْهِكَ (masculine "your" to the cousin), كُربَ.
- Middle Arabic noted: عينيه as subject, سبعة عشر سنه, واولاة, هي واياه, جاؤا, بطّل, وعيطت, الجيعان, يا هل ترى.
- Library label: `Night 139 · King ʿUmar ibn al-Nuʿmān, continued`. Nothing to decide.
- Next: night 140 (P665L08–) is not yet complete; the next firing should transcribe.

## PDF 695–702 (printed pp. 673–680, transcribed 2026-11-18)
- Nights 140 (P665L08–P674L06) and 141 (P674L07–P678L11) are now complete and unpublished; the next two firings should publish them. Night 142 label P678L12 (centred, `h`).
- P678L11 is one word, المباح, stretched across the line by a kashida ("فسكتت عن الكلام المباح"). The detector dropped it, and it was recovered from the band. One pass read الصباح; the adjudicator read المباح with high confidence.
- Kept as printed, for the publishing run to consider for `emend.json`: P680L23 يزجع (a clear dot over the rāʾ; sense يرجع). P673L17 اراقبه: the letter after ارا did not ink and only two dots remain (ta or qāf); recorded as اراقبه from the gap and the sense, low confidence. P678L05 سعد انة: printed with a full space, but it is the name Saʿdāna.
- Hemistich mark: on P679L01 the print sets its asterisk over the kashida of الْمَحَبَّةِ. I placed ` * ` after that word, matching P678L21. The adjudicator's verdict had dropped it, so I restored it by hand.
- Nothing to decide.

## Night 140 (published 2026-11-18)
- Corrected misprints in emend.json: P666L02 ينقوت→يتقوت (the same verb is printed correctly at P666L12); P670L03 بفصة→بفضة (silver). The archive was not changed.
- Kept as printed with notes (doubtful, not corrected): P666L05 مخضبة (read mukhaḍḍaba, "dyed"; perhaps مخصبة, "fertile"); P671L17 الضربة الفاضلة (perhaps الفاصلة, "the decisive stroke"); P672L02 فضجّر (read as "grew distressed"); P673L14 غيار (read ghayyār, "raider"); P673L15 حجرة (read "mare"); P669L03 فدخلت (read dakhkhaltu, "I brought in [the elders]").
- Printed marks kept with notes: صَدِىٌ (P668L11, nominative where genitive is expected), وصفّه (P673L08, stray shadda), يا لَله (P670L12); verse: تَضْمُرُهَا, ذَاقًا, مَارَايْتُ, شَرَّدْتُ, اَسَاقِفٌ, يَتَدَفَّقُ (rhymes -aqu among -iqu).
- Names romanised for the first time: Ṣabbāḥ ibn Rammāḥ ibn Hammām (صباح, the Bedouin; vocalised صَبَّاح), Najma (نجمه, his cousin), Ghassān (the horse-thief), Kahrdāsh (the robber chief), al-Qātūl and al-Majnūn (the horse's names). Change them across the nights if you prefer other readings.
- Library label: `Night 140 · King ʿUmar ibn al-Nuʿmān, continued`. Nothing to decide.
- Next: night 141 (P674L07–P678L11) is complete and unpublished; the next firing should publish it.

## Night 141 (published 2026-11-18)
- No misprints corrected; emend.json unchanged.
- Kept as printed with notes (doubtful, not corrected): P674L10 وهاش (read hāsha, "stormed"; sense a guess); P674L21 اخرج بي (causative plus bi-); P675L22 verse مِنِيْ (read minnī, "on my part"; munā possible); P676L02 verse وَطُوْلُ (printed nominative where ṭūla is expected); P676L19 لتطفى and جمرته (whose "ember" is unclear); P678L09 ووعدتها لك (read waʿadtuhā, the old woman speaking; waʿadat-hā possible).
- Spelling and spacing kept: غمدة, هذة (ة for the pronoun), علي/حتي/جدى, لوقدر, العزّالي, and سعد انة (two printed words, romanised as one name, Saʿdāna, the old go-between, first appearance).
- Narrator slips into the first person at P675L04 (فقلت له) and back at حدّثه; noted for the reader.
- Library label: `Night 141 · King ʿUmar ibn al-Nuʿmān, continued`. Nothing to decide.
- Next: night 142 (P678L12–) is not yet complete; the next firing should transcribe.

## PDF 703–710 (printed pp. 681–688, transcribed 2026-11-18)
- Night 142 (from P678L12) is still open after these pages: no night label or closing formula on pp. 681–688 (checked in the text, not only with `nights_index.py`). At 235 lines so far it is already the longest night, so it should close early in the next batch. The next firing transcribes again.
- **ه or ة after a non-joining letter.** In this type, a stand-alone final ه after د ذ ر ز و ا is drawn as a horned loop that looks like a ة. A real ة is a round loop with two separate dots (compare والحيوة P685L02, الغنيمة P686L18). Pass 2 wrote ة for every horned ه, and the adjudicator ruled ه each time. Both passes agreed on ة in seven places, so those never reached the adjudicator: فوجدة P683L01, هذة P683L16/17/21/23, عندة P685L06, واعطاة P686L18. I checked each crop and corrected them to ه by hand before applying the verdicts. **The earlier archives may hold the same misreading:** pp. 600–680 have هذة 26 times (against هذه 65), plus عندة, وجدة and others, and a publishing run has treated "ة for the pronoun" as a habit of the print. Nothing changed meanwhile. Worth one spot-check run that looks at those crops; if they are horned ه, correct the archive (no reading text changes meaning either way).
- Low confidence: P687L06 قتلناه (dots worn; one pass had فعلناه, the other قتلناة).
- Kept as printed, for the publishing run to consider for `emend.json`: P682L11 فخرح (no dot on the last letter; sense فخرج); P687L05 واولا (sense ولولا); P687L13 رائد (no dot seen; sense perhaps زائد); P686L16 اغطاهم (a dot over the ع; sense اعطاهم). P687L22 سان سان is printed as two words; the same name is ساسان at P688L22 (kashida-stretched).
- P684L11, the verse introduction قال فيه الشاعر, had no crop. Both passes read it from the band.
- Nothing to decide.

## PDF 711–718 (printed pp. 689–696, transcribed 2026-11-18)
- Night 142 (P678L12–P692L18, 320 lines) is now complete and unpublished; the next firing should publish it. Night 143 label P692L19 (centred, `h`), still open at the end of p. 696.
- On PDF 711 and 712 the detector took the running header for body line 1; the passes were told to skip that crop. Nothing lost.
- 714→715 join: both passes read the start of P693L01 as ني منه. On the crop the second word has a dot over a flat stroke, not a tooth: مخه ("فساحت ني مخه", the hashish dissolved in his brain). Corrected by hand. The first word shows a tooth with one dot and no loop, so it stays ني as printed. The adjudicator read في. For the publishing run: ني is a misprint for في (emend.json).
- Kept as printed, for the publishing run to consider for `emend.json`: P689L22 الصاح (no tooth for ب; sense الصباح); P691L17 فقانت (sense فقالت); P694L16 ووثبث (sense ووثبت); P694L23 ياكرن (sense uncertain, perhaps باكون); P696 رابت/رابته/روباك (one dot below; sense رايت/رايته/روياك); P692L20 السعيدا and النسقية (sense الفسقية); P690L02 نكرهه (one dot above, sense تكرهه); P690L06 وحمت (sense وحنت?).
- Low confidence: P692L08 امرضه (a speck above the joined ه); P695L14 ما كان / P695L21 ماكان (the spacing of the name); P696L12 اهلك (damaged letter).
- plan.md's running line total was 175 short; it is now recounted from the archives (15447).
- Nothing to decide.

## Night 142 (published 2026-11-18)
- Corrected misprints in emend.json (14): P680L23 يزجع→يرجع, P681L14 تكون→نكون, P682L11 فخرح→فخرج, P682L21 اى→الى, P683L12 جاربة→جارية, P684L16 فقطت→فقطعت, P686L16 واغطاهم→واعطاهم, P687L05 واولا→ولولا, P687L13 رائد→زائد, P689L22 الصاح→الصباح, P690L02 نكرهه→تكرهه, P691L17 فقانت→فقالت, P691L18 باتلاقه→باتلافه, P691L22 اى→الى. The archive was not changed.
- Kept as printed with notes (doubtful, not corrected): P692L04 سمعت (samiʿtu, "I heard", where Kān Mā Kān is the one who hears: either a misprint for سمع or the narrator slipping into the first person, as in Night 141; the drafter had corrected it, and I put the print back); P685L19 اتهرك (no such word; anharaka or aqharaka likely); P690L06 وحمت (perhaps وحنت); P681L15 وينخرم; P683L04 راى الى; P688L15 واذ باهاليها.
- Spacing kept: سان سان (P687L22), سا سان, كهر داش, لا بدان, اريدان.
- Names romanised for the first time: Fātin (the warrior-maiden Kahrdāsh loved), Jāmiʿ (an emir of the Daylam), Bākūn (the old slave-woman with the poisoned dagger).
- Library label: `Night 142 · King ʿUmar ibn al-Nuʿmān, continued`. Bākūn's story of the ruined lover in the bath begins at the end of this night; the next night may want to name it once its heading or its shape is clear.
- Nothing to decide. Next: night 143 (from P692L19) is still open; the next firing should transcribe.

## PDF 719–726 (printed pp. 697–704, transcribed 2026-11-18)
- Night 143 (P692L19–P702L03, 213 lines) is now complete and unpublished; the next firing should publish it. Night 144 label P702L04 (centred on its own line, `h`), still open at the end of p. 704.
- PDF 719 has a two-line running header (the tale title wraps: "…وكان ما كان / والوزير دندان بسبب دايته مرجانة"); both lines were skipped. On PDF 719, 720, 721 and 724 the detector took the header for crop 1; nothing lost.
- This batch the ة/ه check found nothing to correct: every word that both passes ended in ة after a non-joining letter is a real ة (خرزة, ابريزة, مدة, شدة and so on). Where the horned ه was disputed, the adjudicator ruled ه from the image (الخرزه P697L05, هذه P704L13).
- Low confidence: P704L06 ففرح (one pass read a dot over the last letter, ففرخ; the adjudicator saw only a slanted speck).
- Kept as printed, for the publishing run to consider for `emend.json`: P700L01 التقانة (both passes; sense perhaps التفاتة); P700L23 "فسارت قضى فكان بنفسها" (reads oddly; both passes agree); P703L09 وثاقهم was ruled ق, not ت; P702L16 قدا هديت and P704L03 وقدا تحفته (spacing as printed, sense قد اهديت / قد اتحفته); P698L10 البرمن (set solid, sense البر من).
- Marked prose words confirmed by both passes: سرّا, ثلٰث/ثلٰثة/ثلٰثمائة, فَاخَذَنا, استقلّيت, حنّ, وحلّ, الاخوّة, متهيّئين, ونَفتْ, واُنهب, يعدّ, يدلّهم, ميّزوهم, الشقيّين.
- Nothing to decide.

## Night 143 (P692L19–P702L03, published 2026-11-18)
- Corrected misprints in emend.json (10): P692L20 السعيدا→السعيد, P692L20 النسقية→الفسقية, P693L01 ني→في, P694L16 ووثبث→ووثبت, P694L20 وجداه→وجدها, P694L23 ياكرن→باكون, P696L02 رابت→رايت, P696L10 رابته→رايته, P696L11 روباك→روياك, P700L01 التقانة→التفاتة. The archive was not changed.
- Kept as printed with notes (doubtful, not corrected): P695L02 استيقظه (intransitive verb with an object suffix; likely استيقظ or ايقظته); P694L14 بمخارف (read as "fables"; perhaps زخارف); P696L10 الذيذ (read ladhīdh with a stray alif; perhaps الذّ); P694L08 كنت اصبر (two readings given); P693L06–07 ثم فعل وهو ساكت (verb without object); P699L09 قصته (perhaps قصتها); P699L14 ابن اخته (Kān Mā Kān is in fact his brother's son); P700L23 فسارت قضى فكان بنفسها kept, read "went in person".
- Spacing kept: يجدا حدا (P692L22, pointed as yajid aḥadan across the split), البرمن, ماعندي, كلواحد, قدمات, قدارسل, فعند ما.
- Names romanised for the first time: Rūmzān (رومزان, king of the Rūm, Ḥardūb's grandson by Abrīza), Zalīṭ (زليط, the hashish-eater's nickname; the gloss "perhaps 'stark naked'" is marked as a guess).
- Decided meanwhile: Sharrukān is spelled so in English (tr/l/i/n), as in Nights 101–141; Night 142 alone has "Sharrkān" (left alone). The Arabic t keeps the corpus's شَرْكَان pointing. If the owner prefers one spelling throughout, it is a mechanical sweep.
- Library label: `Night 143 · King ʿUmar ibn al-Nuʿmān, continued` (Bākūn's bath-house story is an inset, not a headed tale).
- Nothing to decide. Next: night 144 (from P702L04) is still open; the next firing should transcribe.

## PDF 727–734 (printed pp. 705–712, transcribed 2026-11-18)
- Night 144 (from P702L04) is still open after these pages: no night label or closing formula on pp. 705–712 (checked in the text, not only with `nights_index.py`). It stands at 239 lines. The next firing transcribes again.
- The running header changes to the inset tale of Ḥammād the Bedouin and ʿAbbād ibn Thaʿlaba before King Rūmzān. Verse runs through pp. 707–712.
- PDF 730: the detector dropped the verse introduction P708L11 وتنشد هذه الابيات (a double-pitch gap). Both passes recovered it from the band. PDF 734: crop 21 held two verse lines, and both passes split them. On PDF 730, 731, 733 and 734 the detector took the running header for crop 1; nothing was lost.
- Two agents read the PDF 734 header as ٧١٣. On the image it is ٧١٢ (Persian-style ۲), so −22 holds.
- P712L02: both passes had يا حماد انا. The ink reads يا حمادا نا, with the gap after the alif. I set it as printed by hand. For the publishing run: a spacing slip, read يا حماد انا.
- The ة/ه check found nothing to correct. Every word where both passes ended in ة after a non-joining letter is a real ة (كسوة, مدة, شاردة, بلدة, غادة, دورة and so on).
- Low confidence: P707L17 ما ذكرتم (narrow gap); P712L20 اِطِّرَادٍ (which letter each kasra belongs to).
- Kept as printed, for the publishing run to consider for `emend.json`: P712L13 توسل (the ل rises to full height; sense perhaps توسد); P710L17 قلت (two dots, not the قلث one pass saw); P712L18 مَفَرْ (broken م head).
- On P708L11/16 and P709L07 the adjudicator read اللّٰهِ / لِلّٰهِ with a shadda and dagger alif, which neither pass had. This matches the archive's usual spelling.
- Nothing to decide.

## Night 144 (P702L04–P713L13, published 2026-11-18)
- Corrected misprints in emend.json (2): P704L20 إثواب→اثواب (hamza set under the alif of athwāb), P712L13 توسل→توسد (he "pillowed" his sword under his head). The archive was not changed.
- Kept as printed with notes (doubtful, not corrected): P706L20 الفارسي (al-Fārisī, "the Persian", for a Bedouin of Fazāra; perhaps a slip for al-fāris, "the horseman" — a drafter had corrected it, and I put the print back as not certain); P703L22 ضاع منها المال (feminine for the merchant; likely منه); P705L03 اشتراؤها (nominative hamza seat where an object is expected); P706L01 فنزلنا (read "set out"); P708L14 ذا الخيل; P709L18 من بلال; P710L01 رخيم الرجس (perhaps rajīm); P710L06/09 تلقي (sense talqā); P710L13 وكل الامر; P713L02 قالت له (for لي).
- Spacing kept: فلماكانت (the night's heading), كلواحد, بينماهم, قدا هديت, وقدا تحفته, يافرسان, اوتريدون, فليبرزلي, يا حمادا نا (pointed yā Ḥammādu anā), لما ذا, and the usual ما/لا run-togethers.
- Names romanised for the first time: Ḥammād al-Fazārī (the Bedouin narrator), Bilāl and Hilāl (two of his companions), ʿAbbād ibn Tamīm ibn Thaʿlaba and the Banū Thaʿlaba, Iblīs.
- The P703L20 text calls Sharrukān Kān Mā Kān's ʿamm, which is right (his father is Ḍawʾ al-Makān); two draft notes that said otherwise were corrected in review.
- Library label: `Night 144 · King ʿUmar ibn al-Nuʿmān, continued` (Ḥammād's tale is an inset told before the kings, not a headed tale).
- Nothing to decide. Next: night 145 (P713L14–P716L06) is complete and unpublished; the next firing should publish it.

## Night 145 (P713L14–P716L06, published 2026-11-18)
- Corrected misprints in emend.json (4): P714L01 حرودب→حردوب (Ḥardūb), P714L13 جازبت→جازيت, P714L17 ونكشت→ونكشف, P715L22 اللّعيش→العيش. The archive was not changed.
- Kept as printed with notes (doubtful or Middle Arabic): P715L12 فقرط بيده على اضلاعها (read qaraṭa, "squeezed", vowels a guess); P713L17 فاطلعته من علائقه (sense uncertain); P715L18 يتجارى (for yatajarraʾu); P715L22 والهناه; P716L02 ضو المكان; اكتروه اهل بيت المقدس (plural verb before its subject).
- Spacing kept: السعيدان, العبيدان, شهر زاد.
- The review again noticed that شَرْكَان (as the corpus points it) reads Sharkān while tr has Sharrukān; I kept the corpus pointing, as decided for Night 143. If the owner wants شَرُّكَان throughout, it is a mechanical sweep.
- Library label: `Night 145 · King ʿUmar ibn al-Nuʿmān ends` — the night closes the tale; the bird tales (header حكاية البطة مع الشبل) begin in Night 146.
- Nothing to decide. Next: night 146 (from P716L07) is still open; the next firing should transcribe.

## PDF 743–750 (printed pp. 721–728, transcribed 2026-11-19)
- Night 146 closes at P724L15. Night 147's label is on its own centred line at P724L16, and Night 148's at P727L01; both are flagged h. Nights 146 and 147 are now complete and unpublished. The next two firings should publish them.
- The running header changes from حكاية الشبل مع النجار to the peacock, duck and gazelle material, and then to حكاية الراعي العابد (p. 728).
- P726L18: a single centred word, وورد ("it is related"), introduces the anecdote of the pious man and the doves. It is transcribed as its own line, flagged h. The detector missed it, and missed P726L06 ثم قالت ايضا هذا البيت (centred); both passes recovered both lines from the bands.
- The adjudicator confirmed that this edition's free-standing final ه has a hooked top and no dots. Pass 1 had read several of them as ة (هذه, اخذه, بيده, ظهره, امره, وصبره, اولاده), and they were decided as ه. Every remaining final ة in the archive is a real feminine ending.
- Kept as printed, for the publishing run to consider for `emend.json`: P726L16 ساعة وقل / قيل (I checked the ink and it reads وقل; the sense wants وقد قيل); P724L08 البقظة (for اليقظة); P727L19 انشعرّ (for اقشعرّ); P723L12 فتعل; P723L18 اتيسه (perhaps انيسه); P721L16 البراي (one ر); P724L07 وقدرماك run together; P724L21 اتعدى (sense اقعدي).
- Low confidence: P727L19 ايّتها (the shadda sits between the ي and ت).
- Nothing to decide.

## Night 146 (P716L07–P724L15, published 2026-11-19)
- Corrected misprints in emend.json (11): P717L01 موتكما→مودتكما (the duck comes "desiring your friendship", not "your death"), P717L22 وكولى→وكوني, P718L16 السطان→السلطان, P720L05 با→يا, P720L10 ويشدة→ويشده (ة for the pronoun ه, as on Nights 88–96), P720L19 غظيا→غيظا, P721L06 واو→ولو, P721L16 البراي→البراري, P722L10 نكون→تكون, P723L18 اتيسه→اقيسه ("so that I can fit it to your size", which picks up قياس on the line before; the transcribers' other candidate انيسه was judged less likely), P724L08 البقظة→اليقظة. The archive was not changed.
- Kept as printed with notes (doubtful): P718L15 الخريف العقل (perhaps الخرف, "dotard"); P718L21 الطفر (for ثفر, "crupper"); P720L12 الصرع (the rein; form unclear); P720L15 انتحل ظهرى; P720L18 ويسلي شحمي; P721L16 الهج; P722L02 وبيده اطفال صغار; P722L05 ولا قاع (perhaps ولاقاه, "and met him"; that would need a spacing change too); P723L12 فتعل (sense "got to his feet"); P723L17 مسامير مطرفة.
- Spacing kept: لاتخافي, لاباس, لاارى, ولابما, يابن, ياسيدي, لاتطاق, يا نجارما, مافات, وقدرماك, بلاشك, ولاريب, فكبريا, and the stray و at P718L23.
- غبرة is pointed ghabra throughout (one slice had ghabara; the corpus has both).
- Library label: `Night 146 · The Duck and the Lion Cub`, from the running header حكاية البطة مع الشبل. The tale has no heading of its own in the text. Night 147 continues it.
- Nothing to decide. Next: night 147 (P724L16–P726L21) is complete and unpublished; the next firing should publish it.

## Night 147 (P724L16–P726L21, published 2026-11-19)
- Corrected misprints in emend.json (4): P724L21 اتعدى→اقعدى and P725L01 تعدت→قعدت (the print has حتى قعدت on the line between; تعدت cannot be a first-person form), P725L20 وام→ولم, P726L16 وقل→وقد (wa-qad qīla; the reviewer judged the only alternative, a dittography of قيل, gives the same sense). The ت/ق pair is a body-shape error, not a dot slip; it is corrected because the sense allows one reading. The archive was not changed.
- Kept as printed with notes: لاننّا (shadda on the second nūn), نستوفاه, جزئر, الحشايش, جري, أكلين (read ākilīn), the printed fatḥas of آمَنين/آكَلين, الاّ, and the verse's لِاُخْبِرُهُ (indicative after li-) and bare يَوْم.
- Spacing kept: لاينفك, فبينماهما, الحذروان, هاهوقد, هوالآخر, ماقتلها, شهر زاد.
- غبرة pointed ghabra, as in Night 146.
- Library label: `Night 147 · The Duck and the Lion Cub ends / The Hermit and the Pigeons begins`. The new anecdote opens with the centred word وورد (P726L18) and has no heading; the running header on p. 728 calls the next material حكاية الراعي العابد. The name "The Hermit and the Pigeons" is mine; change it if the owner prefers another.
- Nothing to decide. Next: night 148 (from P727L01) is still open; the next firing should transcribe.

## PDF 751–758 (printed pp. 729–736, transcribed 2026-11-19)
- Night 148 closes at P733L14. Night 149's label is on its own centred line at P733L15. The adjudicate prompt has no way to set the flag, so I set h on it by hand, as for earlier labels. Night 148 is now complete and unpublished; the next firing should publish it.
- The running header is حكاية طير الماء والسحلف. The print spells the animal السحلف (س ح ل ف) throughout, the header included; it is kept as printed. The publishing run may want to note it as a form of سلحفاة.
- Lines dropped by the detector and recovered from the bands by both passes: P732L10 فانشد طير الماء يقول, P732L20 (a centred اعلم), P733L14 عن الكلام المباح, and the verse line طال ما قد ساء قلبي on p. 735. P735L20 شعر — is a centred label, flagged h.
- Both passes wrote ة on six words where the print has a hooked final ه with no dots. The adjudicator found them, and I corrected them by hand before applying: P730L23 وولده, P734L06 عبده, three cases of هذه on p. 734, and وآخره. P730L21 هذة does have two clear dots (I checked the crop), so it is kept as printed.
- For the publishing run (kept as printed): P734L18 تيل (two dots above; a misprint for قيل), P734L22 المتل (for المثل), P734L07 التعميف (sense unclear), P736L08 فَلَاَ صْفَحَنْ (verse; printed with a gap inside the word), P730L22–23 يغترّبها / المغترّبها (run together).
- Nothing to decide.

## Night 148 (P727L01–P733L14, published 2026-11-19)
- Corrected misprints in emend.json (2): P727L19 انشعرّ→اقشعرّ ("shuddered"), P730L19 وسرري→وسروري. The archive was not changed.
- Kept as printed with notes (doubtful): P731L02 الديه (read ladayhi; perhaps اليه repeated); P731L12 يعد لها (pointed yuʿaddu lahā as printed; يعدلها "equals it" is the alternative); P734-side items from the transcription note (تيل, المتل) fall in Night 149, not here. Also noted: P729L14 the verse's printed actives انتهينا/امرنا (usually quoted as passives); P732L12 printed فَرَجَتْ; P729L20 فقبله (qabilahu or qabbalahu); P732L13–14 انساق القضاء اليه بازيا.
- Middle Arabic kept: اغناما after كان له, ان … رجل, يخافا, حتي, علي for على, تري, شيأ, التايه, مثل ذكرته.
- Spacing kept: ارجوان, الّاعظاما, يغترّبها/المغترّبها, لاازال, لاتملّى, ذوحيل, لاحول, لاصبر, ولابيني, مالا, شهر زاد / شهرزاد.
- السحلف is the print's spelling for the tortoise throughout; pointed al-siḥlif and noted once. Rendered "tortoise" in English.
- Library label: `Night 148 · The Hermit and the Pigeons ends / The Water-Bird and the Tortoise / The Wolf and the Fox begins`. It names three tales because the night holds three; the shepherd episode is part of the hermit material (the running header calls it حكاية الراعي العابد). The name "The Wolf and the Fox" is mine, since the tale has no heading in the text.
- Nothing to decide. Next: night 149 (from P733L15) is still open; the next firing should transcribe.

## PDF 759–766 (printed pp. 737–744, transcribed 2026-11-19)
- Night 149 runs on through all eight pages; no night label or closing formula appears. It has 248 lines so far, from P733L15, which is long but within the range seen before (Night 144 had 252). The running header is حكاية الذئب والثعلب.
- Lines dropped by the detector and recovered from the bands by both passes: the centred verse intros قول الشاعر (p. 737 and p. 741) and وقول الآخر (twice on p. 743). They are plain lines, not h.
- Both passes wrote ة in هذة at P737L20. The adjudicator found an undotted hooked ه there, and I corrected it to هذه by hand before applying.
- For the publishing run (kept as printed): P739L01 ولانساد (perhaps ولا فساد); P739L03 الثلعب (letters transposed, for الثعلب); P739L13 البزية (a dot over the ر, for البرية); P738L17 ذانك (one dot; perhaps ذالك); P741L15 اى (for الى); P741L03 وكائه (printed hamza; sense وكانه); P744L11 الاعقوبة (run together).
- Low confidence: P739L08 الجافل (faint); P741L11 بِاَخَرِيْنَا (the mark over the alif).
- Nothing to decide.

## PDF 767–774 (printed pp. 745–752, transcribed 2026-11-19)
- Night 149 is complete: its closing formula is the last line of p. 744. Night 150's label is the first line of p. 745, on its own line (h). Night 150 closes at P751L06, and Night 151's label is on its own centred line at P751L07 (I set h by hand). Nights 149 and 150 are both complete and unpublished, so the next two firings should publish.
- Four centred one- or two-word anecdote openers are flagged h: ومما يحكى P747L03, بلغني P748L15, وحكي P749L12 and زعموا P750L15. I set h by hand on بلغني and زعموا, where one pass had left it off, so that they match وورد P726L18. The running headers in the batch are حكاية الفأرة وبنت عرس, حكاية الغراب والسنور and حكاية البرغوث والفأرة.
- Lines dropped by the detector and recovered from the bands by both passes: P746L01–02, P746L19 هذه الابيات, P747L03, P748L14 من الهلكة قالت نعم, P748L15, P749L01 (verse), P749L12 and P750L15. On p. 751 two verse lines were merged in one crop, and both passes split them.
- ه/ة: the adjudicator gave ه wherever the final hook is not two clear dots: P745L07 لايجاوزه, P745L22 هذه, P747L01 وحده, P747L18 ماهذه, P747L21 هذه/ارصده. conventions.md cites وحدة as an example of the edition's spelling, but this page shows the hooked ه.
- For the publishing run (kept as printed): P749L22 اى (lām missing, for الى; the join to p. 750 reads دعتني الى ملاطفتك); P748L13 دمن (for ضمن?); P745L20 تخانه (one dot above; perhaps تخافه); P745L09 المواخاة; spacing kept: P745L12 شرافشاه, P746L12 وبصروابه, P747L22 ماخطر, P750 مالاتدرك/ولاتصح.
- Nothing to decide.

## Night 149 (P733L15–P744L23, published 2026-11-19)
- Corrected misprints in emend.json (9): P734L18 تيل→قيل, P734L22 المتل→المثل, P738L17 ذانك→ذاتك (the feminine adjectives مفارقة/زائلة/راحلة follow), P739L01 ولانساد→ولافساد (kept as one word, as printed), P739L03 الثلعب→الثعلب, P739L13 البزية→البرية, P740L08 اصادتك→اصادقك (ت/ق, as in Night 147), P741L15 اى→الى, P743L15 فقالت→فقال (the fox is masculine throughout). The archive was not changed.
- Kept as printed with notes (doubtful): P734L07 التعميف (perhaps التعنيف); P735L04 انك نلته ما املّته; P736L02 التسليق; P739L06–11 بأزيا/البأزي (hamza printed on bāzī); P739L10 آتيتك به; P741L03 وكائه (perhaps وكأنه); P741L20 verse فَرِّضْ (perhaps فَرَضِّ); P743L20 اغل ربك (perhaps اغدر بك, "betray you"; translated by that sense); P744L04 استدرك ما انسل; P744L12 فنطيت (colloquial "jumped").
- Spacing kept: مالا, بلاتعب, فيخلولي, وارجوان, هل لابدأت, لاَنوبنّ, ولا صعدنّ, ولا طعمن, فلا عجّلن, لا علمنك, الاعقوبة, شهر زاد; the line-split و / لم at P737L06–07 and P739L09–10.
- Library label: `Night 149 · The Wolf and the Fox, continued`. The tale goes on into Night 150. The fable of the falcon and the partridge is told inside the fox's speech, so it is not named in the label.
- Nothing to decide. Next: night 150 (P745L01–P751L06) is complete and unpublished; the next firing should publish it.

## Night 150 (P745L01–P751L06, published 2026-11-19)
- Corrected misprints in emend.json (4): P745L20 تخانه→تخافه, P747L08 وخففته→وجففته ("dried"; the sesame is called مجففا a few lines on), P749L09 فهده→فهذه, P749L22 اى→الى. The archive was not changed.
- Kept as printed with notes (doubtful): P748L13 دمن (perhaps ضمن; reading uncertain); P748L10 وعاشت فيه (perhaps وعاثت, "made havoc"); P750L07 الاجلاء (perhaps الاخلاء, "close friends"); P746L04 verse الْعِطَافَا; P746L20 verse فَاخْتَطَفَتْ (pointed active, sense passive); P746L18 فرأه, الفرحات; P746L07 بسيّدة (ة for the pronoun ه).
- Library label: `Night 150 · The Wolf and the Fox ends / The Mouse and the Weasel / The Crow and the Cat / The Fox and the Crow begins`. It names four tales because the night holds four. The flea and the mouse is told inside the fox's speech, so it is not named in the label. The names are mine, from the running headers.
- Nothing to decide. Next: night 151 (from P751L07) is still open; the next firing should transcribe.

## PDF 775–782 (printed pp. 753–760, transcribed 2026-11-19)
- Night 151 closes at P753L15, and Night 152's label is on its own centred line at P753L16. Night 152 closes at P760L19, and Night 153's label is on its own line at P760L20. Nights 151 and 152 are both complete and unpublished, so the next two firings should publish.
- Centred one-word anecdote openers are flagged h: زعموا P753L13, بلغني P754L08, ويحكى P755L06, بلغني P757L03 and P757L18, and بلغني P758L13. I set h by hand on four of them (P753L13, P754L08, P757L03, P757L18) and on the Night 152 label, where pass 1 had left it off. Most of these lines had no crop and were read from the bands by both passes.
- ه/ة: both passes wrote واخذه at P760L11, but the adjudicator found two clear dots (واخذة), and I corrected it by hand before applying. The print has ة at P753L07 هذة, P753L19 شرة and twice عندة on p. 759, but an undotted عنده at P759L10. All are kept as printed.
- For the publishing run (kept as printed): P758L03 اخذ (the dot is faint; pass 1 read اخل); P759L20 الطاوُوس (here with a damma; elsewhere الطاؤوس); P756L06 مِلْ (the sukun is medium confidence); P760L12 ار احسن (two words set close together).
- Nothing to decide.

## Night 151 (P751L07–P753L15, published 2026-11-19)
- No misprints corrected; emend.json unchanged.
- Kept as printed with notes (doubtful): P751L10 مطر السلامة (an unusual figure, perhaps corrupt); P751L19 كفى بصدق المودة صلاح النية (the case of صلاح; both readings given); P752L04 الممكّنة (read mumakkana); P752L07 وان استحكمت قوة المحتال (a compressed clause); P753L03 صلة بقطيعة (the force of bi-).
- P753L08 صحبَته: the print sets a fatḥa on the b. By the rule that a printed mark on a prose word is kept, it is pointed صَحَبْتَهُ (ṣaḥabtahu), and the note gives the Classical ṣaḥibtahu. The drafter had moved the vowel instead; I put the print's mark back.
- The shared glossary entry بِالنَّهَارِ said 'with the day'; it now says 'by day'. Five other shared entries had a sense added for this night's use of bi- or maʿa kawnika; no existing meaning was removed.
- Library label: `Night 151 · The Fox and the Crow, continued`. The flea and the mouse is told inside the fox's speech, and the falcon fable begins inside the crow's, so neither is named in the label. The title follows the running header حكاية الثعلب والغراب.
- Nothing to decide. Next: night 152 (P753L16–P760L19) is complete and unpublished; the next firing should publish it.

## Night 152 (P753L16–P760L19, published 2026-11-19)
- Misprints corrected (emend.json): P757L01 القنفل → القنفذ; P758L04 لى → الى (the alif-lām of ilā lost, as with اى).
- Kept as printed with notes (doubtful): P754L03 يطرح (no object; read "yields", يطمع considered); P754L10 رميس (a lamb or kid by context, word unknown, glossed with "?"); P753L22 صار قُوّته (masculine verb with the print's quwwatuhu); P757L04 سنده (town unidentified, read Sindah); P757L15 واراد (singular verb for the two sharpers; perhaps a dropped dual alif); P757L23 شرائُها (the print's damma after min kept); P756L05, P756L07 المطال, P756L14 وكلما, P760L13 امني (readings given in the notes).
- P758L09 فأخذ (for fa-ākhudha): a drafter put a combining madda on the printed أ; the review replaced it with a dagger alif, فَأٰخُذَ, following رَأٰهُ (P754L11). No letter changed.
- Shared glossary amended for this night's uses, no existing sense removed: زَادُ (adds the split name يَا شَهْرَ زَادُ), شَهْرَ, لِأَ, عِنْدَةُ, عِنْدِةِ.
- Library label: `Night 152 · The Fox and the Crow ends / The Hedgehog and the Ringdove / The Thief and His Ape / The Sparrow and the Peacock`. The sparrow-and-peacock fable ends in this night (Night 153 opens a new tale at P760L20). Title follows the night's longest new tale, حكاية القنفذ والورشان.
- Nothing to decide. Next: night 153 is not yet complete; the next firing should transcribe.

## PDF 783–790 (printed pp. 761–768, transcribed 2026-11-20)
- Night 153 closes at P766L21, and Night 154's label is on its own centred line at P767L01. I set h on that label by hand. Night 153 (P760L20–P766L21, 133 lines) is complete and unpublished, so the next firing should publish it.
- Lines the detector dropped, recovered from the bands by both passes: P761L13 فيها الشاعر, P761L21 ولسان الحال يقول, P764L05 (verse).
- Lines read from the bands only: pass 1 on p. 765 and both passes on p. 767 read most lines without opening their 2x crops. The adjudicator then checked p. 767's prose lines against the crops, and they matched. It corrected one line both passes agreed on: P767L04 الابيات (the long stroke is a kashida, not a filler dash).
- Misprints kept as printed (both passes and the adjudicator agree), for the publishing run: P762L15 الاتمار (for الاقمار); P764L08 زبديني (for زيديني); P764L16 سَلَتْنِي (for سلبتني); P765L12 ورشّشن; P767L14 بَدَيْكَ (for يديك).
- Low confidence: P767L17 آالهُ (the print sets آ, then ا, then a single-lam له; both passes wrote آاللّهُ). Medium confidence: P764L06 اَرَدَّتَّ, P767L05 مَافِى, P767L15 الَّتِى.
- Spacing: P761L22 فَعَزِّا لْفُوَادَ is kept as printed. On P768L17 the adjudicator thought the print may run اميرالمؤمنين together, but nobody disputed it, so the agreed spaced form stands.
- Nothing to decide.

## Night 153 (P760L20–P766L21, published 2026-11-20)
- Misprints corrected (emend.json): P762L05 تأني → تأتي; P762L15 الاتمار → الاقمار (the same simile, كانهن الاقمار, stands at P761L09–10); P764L08 زبديني → زيديني.
- Kept as printed with notes (doubtful): P761L02 واله (probably ولده, "his son", but more than a dot away; the translation brackets "[his son]"); P761L19 صدك (read ṣaddaka, "towards you"; perhaps قصدك); P763L15 يحيل (for يحول); P765L14 جانب سرير (no article). Verse kept as printed with the likely reading in the note: P761L14 نَذْرُ (for نَزْر), P764L01 الرِّسَالَةً, P764L02 اَشْكُوْحَا لِيَهْ, P764L04 عَارِبَهْ (for عَارِيَة), P764L16 سَلَتْنِي / شَلَتْنِي (the least certain reading in the night), P764L17 تَحْوَى.
- Shared glossary: three existing entries named a bi- sense that does not fit this night's use. I added a sense to each and removed nothing: بِعَشْرِ (bi- after idhā of surprise), بِالْبَابِ ("at the door"), بِقُبْلَةٍ (the gift bestowed after anʿama ʿalā).
- Library label: `Night 153 · ʿAlī ibn Bakkār and Shams al-Nahār`. The title follows the running header, حكاية علي بن بكار مع شمس النهار. The night opens the tale fresh, so the label has no "begins".
- Process note: the draft was first parked on the development branch claude/zen-hopper-tklt7x (pre-review), because a stop hook asked for uncommitted work to be pushed and pushing to main would have published the night before its review. That branch holds only that draft and can be deleted.
- Nothing to decide. Next: night 154 is not yet complete (tail unread), so the next firing should transcribe.

## PDF 791–798 (printed pp. 769–776, transcribed 2026-11-20)
- Night 154 closes at P772L02. Nights 155 (P772L03–P774L04) and 156 (P774L05–P776L10) fall entirely within this batch. Night 157's label is on P776L11. All three labels sit on their own lines, and all three have h; I set the h on P772L03 and P774L05 by hand. Three nights, 154–156, are now complete and unpublished, so the next three firings should publish them.
- I overrode the adjudicator twice, in favour of what is printed. In both places the adjudicator chose the intended word and read it as a broken letter. I checked both 2x crops myself, and both show the misprint plainly:
  - P773L21: the print has خرنا, a misprint for خوفا.
  - P774L03: the print has ننسه, a misprint for نفسه.
  Both are for the publishing run's emend.json under rule 5b.
- Also for the publishing run:
  - P775L09 حافقة: the print has no dot, and the sense is خافقة. The adjudicator kept it as printed.
  - P776L19 اصَّبْرِ: the print has no lam, for الصَّبْرِ. Both passes agree.
  - P776L08 لِلدَمْعِي: the print has two lams.
- Low confidence:
  - P773L18 حَبِيبْ: the type is damaged at the end of the line. The other pass read حَاسِبْ.
  - P775L02 قَالَتْ: the lam is damaged, but its fatha is printed.
  - P776L08 بُعْدِي: the damma is faint.
- Spacing: the print joins ابوالحسن throughout p. 773, and also السعيدان, بكاريا, فبينماهم and لابدان. All of these are kept joined as printed.
- Nothing to decide.

## Night 154 (P767L01–P772L02, published 2026-11-20)
- Misprint corrected (emend.json): P767L14 بَدَيْكَ → يَدَيْكَ ("your hands", in the verse). The transcription run had flagged it.
- Kept as printed, with notes:
  - P767L17 آالهُ: read as the question a-ilāhun, "are you a god…?". The metre wants tanwīn where the print has a single ḍamma.
  - P767L16 لَيْسَ الْعَجِيبُ كَوْنُكَ: both nouns are nominative.
  - P770L12 التحائف: for tuḥaf, "rarities".
  - P771L02 the second بَانَ (the ben-tree): the print points it bāna; the transliteration reads bāni.
  - P771L03 اَنَسَتْ: the metre needs ānasat.
  - P771L22 آخِرُ after كان: nominative as printed.
  - P769L01 سببا: an accusative predicate after inna, a Middle Arabic form.
- Shared glossary: the drafters found 49 existing entries whose sense does not fit this night. Most of them are names read as plain words: الحسن, مسرور, عفيف, علي. Each entry got an appended "Also …" sense, and no existing text was removed. One existing entry was wrong and I corrected it: الشَّابَّيْنِ had "gen., second term of the iḍāfa after hādhayni". It now reads "gen., in apposition to the demonstrative hādhayni", because a demonstrative cannot govern a genitive.
- Library label: `Night 154 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Nights 155 and 156 are complete and unpublished, so the next two firings should publish them.

## Night 155 (P772L03–P774L04, published 2026-11-20)
- Misprints corrected (emend.json): P773L07 منة → منه; P773L21 خرنا → خوفا; P774L03 ننسه → نفسه. The transcription run flagged the last two. I added منة myself: an ة where the sense needs the pronoun ه makes it a different word, so it is a misprint, not the edition's usual spelling.
- Kept as printed, with notes:
  - P773L18 حَبِيبْ: the type is damaged, and the other transcription pass read حَاسِبْ. The final foot does not scan as wāfir, and the -īb rhyme sits loosely with -āʾib. The note says the word may be corrupt.
  - P774L02 عَلّى: a stray shadda on the preposition. The mark is kept, the word is read ʿalā, and the note says so.
  - P773L04 ادري: read as the elative adrā, "better acquainted", because of the following min ghayrī. The note gives adrī, "I know", as the alternative.
- Library label: `Night 155 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 156 is complete and unpublished, so the next firing should publish it.

## Night 156 (P774L05–P776L10, published 2026-11-20)
- Misprints corrected (emend.json): P774L09 دارة → داره ("his house", ة for ه, as in earlier nights); P775L09 حافقة → خافقة ("fluttering", ح for خ).
- Kept as printed, with notes:
  - P774L21 (verse) نَارَتْ / نَقَشْ: the sense and the parallel with تَنَلْهُ point to نالت, and the metre wants the noun naqshan. The pointing is the print's own, so it is kept and the note gives the likely reading.
  - P776L08 (verse) لِلدَمْعِي: probably a doubled lām for لِدَمْعِي, "for my tears". Kept, read li-damʿī, and noted.
  - P774L11 ملقي: the print's ي for ى (mulqan, "lying"). Noted.
  - P776L09 الصفة: read as al-ṣuffa, "the dais". Noted.
- Library label: `Night 156 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 157 is still incomplete (its tail is unread), so the next firing should transcribe.

## PDF 799–806 (pp. 777–784, transcribed 2026-11-20)
- Hand corrections after adjudication (from the images): P779L18 هذة (both passes had هذه; the print dots it); h added to the night labels P779L08 and P783L18; h removed from the verse introducer P778L05 وقول الآخر (precedent P767L12).
- Adjudicator kept as printed: P781L18 يأنيني (one dot above; sense wants يأتيني) — a possible misprint for the publishing run to judge. P778L15 the passes read طلمع/وام; the adjudicator found the print has طلع and ولم (a broken lam join), so no misprint there.
- Low confidence: P779L16 وقبلّها (shadda between ب and ل, nearer the lam).
- Two Pass-1 agents (PDF 804, 806) read only some line crops and took the rest from the bands. Their dispute counts (9, 6) were normal, so they were not rerun; noted in case it recurs.
- Nights 157, 158 and 159 are now complete and unpublished; the next three firings should publish them.

## Night 157 (P776L11–P779L07, published 2026-11-20)
- Misprints corrected (emend.json): P776L19 (verse) اصَّبْرِ → الصَّبْرِ (dropped lām, "the ropes of patience"); P777L09 آكتمي → اكتمي (stray madda on the imperative uktumī).
- ة written for the pronoun ه (خبرة, امرة, عندة ×4, جسدة, شعرة, هذة ×2) kept as printed and noted, following Night 152 and the conventions' list of the edition's spelling habits; Night 156's دارة → داره was emended. The two precedents differ; I followed the majority (keep) because the habit is pervasive on these pages. If the owner prefers these emended, it is a list of ten entries.
- Kept as printed, with notes: P776L18 (verse) يَعْقِبُ (sense wants yuʿqibu); P778L08 فَزَعَتْ (usual faziʿat); P778L10 اَسْطُرَ (fatḥa where genitive and rhyme want -ri; nearest to a misprint, but it is the print's verse pointing); P778L12 الْقِوَامِ (usually qawām); P777L20 وبكي.
- Library label: `Night 157 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Nights 158 and 159 are complete and unpublished; P781L18 يأنيني (noted by the transcription run) is for Night 159's publisher to judge.

## Night 158 (P779L08–P780L21, published 2026-11-20)
- No misprints corrected (emend.json unchanged).
- Kept as printed, with notes:
  - P779L16 وقبلّها: the print's shadda sits on the lām; it is kept there, the bāʾ's shadda is supplied, and the word is read qabbalahā. The note says where the printed mark stands.
  - P779L18 هذة: ة for ه, kept per Night 157.
  - P780L04 قطما: read as qaṭṭu mā run together; the spacing is kept.
  - P780L07 ثاير, P780L05 هنيا, P780L10 لاتطفى: hamza dropped (thāyir, haniyyan, tuṭfī); noted.
  - P779L22 (verse) تَغْفَلُ: who is heedless is uncertain ("you" or the eye); the note gives both.
  - P780L14 دفعتها: read as first person ("I handed it"), following قرأتُها; the narration slides back to the third person at P780L19 (وخرج ابوالحسن), noted.
- The poem P779L19–P780L01 is treated as the opening of Shams al-Nahār's letter, which runs on through the rhymed prose to the couplet at P780L12.
- Library label: `Night 158 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 159 is complete and unpublished, so the next firing should publish it; P781L18 يأنيني is for that run to judge.

## Night 159 (P781L01–P783L17, published 2026-11-20)
- Misprint corrected (emend.json): P781L18 يأنيني → يأتيني ("he would come to me", ن for ت), as the transcription run flagged.
- Kept as printed, with notes:
  - (verse) P781L08 وَرَوَّعَ: printed active, but the sense wants the passive ruwwiʿa. P781L11 حُبِّيكَ: read as ḥubbīka, lengthened for the metre. P781L12 كَفَعَالُ: damma where the grammar wants a kasra. The verse also calls Lubnā's Qays "al-Majnūn", which mixes up two lovers; the note says so.
  - P782L22 اودّعه: the print's shadda gives Form II (waddaʿa), but the sense is "entrust" (Form IV). The shadda is kept and the note says it may be a slip.
  - P782L15 ارباب الديون: taken as Abū al-Ḥasan's debtors, not his creditors, and noted as loose.
  - P781L19 الجارية: read as Shams al-Nahār herself.
  - ة written for the pronoun ه (صدرة, امرة, عندة, غيرة, يجدة, دارة, سيدة, فوجدة): kept and noted, following Night 157. The old shared glossary entry أَمْرِةِ called this a misprint; it was rewritten to call it the print's habit.
- Library label: `Night 159 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 160 is incomplete (its tail is unread), so the next firing should transcribe.

## PDF 807–814 (pp. 785–792, transcribed 2026-11-20)
- P786L01 (verse, top of page) had no line crop. The adjudicator re-read it from 500-dpi crops and found marks that both passes had supplied from expectation (وَاسْتَطلْ with no kasra, وَعَزَّ, اَقْبَلْ, اُطِعِ, bare-alif fathas where pass 1 had hamzas). The full verdict line was set by hand, because `apply_verdicts.py` cannot apply a whole-line check once a dispute on the same line has changed it. Low confidence: أهُنْ (the mark over the alif looks like a hamza head, possibly a heavy sukun).
- Possible misprints for the publishing run to judge (kept as printed): P788L18 تخل مني (sense wants تخدمني, "she serves me"); P788L14 المشير (ش dots visible; sense wants المسير); P789L11 بصعي (for بسعي); P790L06 نطرق (for فطرق) and P790L10 قان (for فان).
- P792L09 والفرش: an ink blot covers the middle letters; medium confidence (the Vision draft read النيش).
- Night labels P785L11, P789L13, P791L15 are on their own lines with h, per precedent. Nights 160, 161 and 162 are now complete and unpublished; the next three firings should publish them.
- Environment: `python3` here is 3.11 with no numpy/cv2; `pip` installs into /usr/bin/python3 (3.13). Run the tools with `/usr/bin/python3`.

## Night 160 (P783L18–P785L10, published 2026-11-20)
- Misprint corrected (emend.json): P784L01 الجاربة → الجارية (ب for ي).
- Kept as printed, with notes:
  - P784L21 سرّتني: read as sārratnī, "she confided to me" (Form III with the long ā unwritten, supplied with a dagger alif). sarratnī, "she gladdened me", does not fit the bad news that follows. This is our reading, and the note says so.
  - P785L03 لانها كانت تميل وتصغي الى ابي الحسن: "she" is taken as the slave-girl. Her mistress is also possible, and the note gives both.
  - P784L15 عسي (ي for ى) followed by اكون without أن: Middle Arabic, noted.
- Demonstratives (ذلك, هذه, هذين, لكن) are written without a dagger alif, as in Nights 150–159. One drafter had used the dagger form, and it was made plain.
- Library label: `Night 160 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Nights 161 and 162 are complete and unpublished, so the next two firings should publish them. The transcription run flagged possible misprints in 161 (P788L18 تخل مني, P788L14 المشير, P789L11 بصعي) for that run to judge.

## Night 161 (P785L11–P789L12, published 2026-11-21)
- Misprints corrected (emend.json): P788L14 المشير → المسير ("going", as at P788L01 and L09); P789L11 بصعي → بسعي ("by striving").
- Kept as printed, with notes:
  - P788L18 تخل مني: makes no sense as printed; probably تخدمني, "who serves me". Kept as two words, pointed تَخْلُ مِنِّي, and translated by that guess, which the note says.
  - (verse) P785L17 يَطْمَعُنِيْ: pointed as Form I, but the sense wants Form IV yuṭmiʿunī; P786L01 اَقْبَلْ: the print gives aqbal, and the contrast with وَلِّ suggests uqbil; P787L01 مَكْتُوْمَةٌ (nom. as kānat's predicate), غَضَبَا, and P787L02 الِيْ for ilayya. All are the print's points, kept and noted.
  - P789L05 ان لي دار غير: nominative after inna (Middle Arabic), noted. P788L19 غلمانه: the jeweller has just said he keeps only one old slave-woman; noted.
  - P788L05 مترّددا: the print's shadda is on the rāʾ; kept, with the dāl's shadda added.
- Library label: `Night 161 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 162 is complete and unpublished, so the next firing should publish it.

## Night 162 (P789L13–P791L14, published 2026-11-21)
- Misprints corrected (emend.json): P790L06 نطرق → فطرق; P790L10 قان → فان; P791L01 منة → منه; P791L02 ويضغف → ويضعف (the emend entry was first written as يضغف and failed the check, because the print fuses the و; fixed before drafting was merged).
- Kept as printed, with notes: السعيدان (spacing); P790L08 علي همّي and P790L15 بكي (ي for ى); P791L02 يقوي pointed yaqwā; P791L03–04 فليت اجلي قريب كنت ارتاح (Middle Arabic); لااخالف, فماترى (spacing). Verse P790L17 لِلْمُبْتَلِي is the print's active pointing; P790L20 اِلَّا هُوَ where Classical wants iyyāhu — both kept and noted.
- Library label: `Night 162 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. No complete night is waiting now (163's tail is not yet transcribed), so the next firing should transcribe.

## Transcription PDF 815–822 (pp. 793–800, 2026-11-21)
- Kept as printed (possible misprints, for the publishing run to judge): P793L06 واصحلته (for واصلحته); P793L19 تي (for في); P795L22 الناني (for الثاني); P796L08 فقات (for فقلت); P798L21 السيعدان (spacing/letters, for السعيد ان); P798L02 الحارت.
- Night labels P795L03 (164), P798L20 (165), P800L21 (166) are on their own lines with h, per precedent. Nights 163, 164 and 165 are now complete and unpublished; the next three firings should publish them.
- Nothing to decide.

## Night 163 (P791L15–P795L02, published 2026-11-21)
- An earlier firing claimed this night at 06:22 UTC and pushed its emend entries, then published nothing. This run took over the claim at 10:23 (over 3 hours old, so abandoned) and reused those entries.
- Misprints corrected (emend.json): P792L01 غليها → عليها; P793L06 واصحلته → واصلحته; P793L19 تي → في; P794L02 فرجدت → فوجدت; P794L09 احي → اخي.
- Kept as printed, with notes:
  - P792L12 فقلت ما يحضر به الاّ انت: the masculine انت fits the slave-girl speaking to the jeweller better (فقالت). Kept as فقلت and noted.
  - P793L21 كلامه, for the little maid's words (possibly for كلامها). P795L02 داره الثانية التي هو ساكن بها: read as "his other house", because the "second house" is the one that was stripped. P794L22 احسن جماعة: an odd phrase, possibly corrupt.
  - Verse: الْاَرِقَا, اَعْشِقُ, سَأُعُدُّهَا, خُمْرَةَ and الْعُسَّالِ are the print's points, kept and noted.
  - Middle Arabic: استقرّيت, نطّيت, تخبّيت, يصدفوهم (no -na), الي for ilā.
- Library label: `Night 163 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Nights 164 and 165 are complete and unpublished, so the next two firings should publish them.

## Night 164 (P795L03–P798L19, published 2026-11-21)
- Misprints corrected (emend.json): P795L22 الناني → الثاني (the same phrase is printed correctly at P797L14); P796L08 فقات → فقلت.
- Kept as printed, with notes:
  - P798L02 الحارت: read as al-ḥārāt, "the quarters", with the long ā unwritten and a dagger alif supplied. It may be a misprint for الحارات.
  - P796L22 انشاءه: the sense wants ifshāʾahu, "divulging it". Kept as printed, because anshaʾa can be stretched to "spread (news)". The note says the reading is uncertain.
  - P797L07 وقسم منهم عليّ: the print's shadda gives ʿalayya, so the thieves split into those "with me" and those "against me". ʿAlī is raised in the note and rejected.
  - P795L17 ولابواب: read as wa-lā bawwābin, "and no doorkeeper"; wa-lā abwābin is given as the alternative. P798L08 فطلَعنا: read as Form II ṭallaʿanā, "he put us aboard"; ṭalaʿnā is noted.
  - The print's habit of writing ة for the pronoun ه (دارة, وراءة) is noted. نحن الذي (singular alladhī for the plural) and لم نرهما are Middle Arabic, noted.
  - P797L12–13: the "we" walking back to the river is the jeweller, the thieves and the lovers together, as فعل بي ايضا (P798L06) shows. The notes on the units either side of the slice join were made to agree.
- Library label: `Night 164 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 165 is complete and unpublished, so the next firing should publish it.

## Night 165 (P798L20–P800L20, published 2026-11-21)
- Misprint corrected (emend.json): P798L21 السيعدان → السعيدان (kept run together, as the print sets it elsewhere).
- Kept as printed, with notes:
  - P800L03 لا قول: read li-aqūla, "so that I may say" (spacing kept); lā qawla makes no sense here.
  - P800L10–11 فهربنا عندهم: an unusual pairing, read "took refuge with them". P800L18 وصلت: read waṣalat (the skiff reached land); waṣaltu is possible.
  - P799L11 فجأوا read jāʾū with a dagger alif; P800L04 وحلفتني read Form II ḥallafatnī; P799L21 اتصل تلك الناحية, ittaṣala with a direct object; P800L08 فيأخذونني indicative after fa- (Middle Arabic); P800L14 فتّش على for فتّش عن.
  - From P800L07 the narrating "I" is the slave-girl, inside the jeweller's account; the note says so.
- Library label: `Night 165 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 166 is not complete yet (only its heading is transcribed), so the next firing should transcribe.

## Night 166 (P800L21–P803L02, published 2026-11-21)
- Misprints corrected (emend.json): P801L06 يدبها → يديها; P802L04 وانفقوا → واتفقوا; P802L09 نكونوا → تكونوا (the watchmen ask "who are you?"); P802L10 وحرجت → وخرجت.
- Kept as printed, with notes:
  - P801L02 جاو بها: read jāʾa bihā, "(the man who) brought her", with the hamza unwritten; pointed جَاؤَ on the printed letters. The plural jāʾū is ruled out by the singular الرجل الذي.
  - P801L06 فرشّت: the print's shadda kept; read first person, "I sprinkled", pointed رَشّْتُ (shadda and sukūn on one letter, as at Night 83). By its letters alone it would be rashshat, "she sprinkled"; noted.
  - P801L03 فلما اصبحت الصباح: read aṣbaḥat ("when she reached the morning"), with aṣbaḥtu noted as the alternative; اندهشت/قطعت/تقدمت read first person (the slave-girl), "she" noted as possible.
  - P802L10 سكرت: read sakirtu, "I had been drinking", part of Shams al-Nahār's story to the watch. P802L07 احضرلنا kept as one word. P802L21 تعوض على الناس, Middle Arabic ʿawwaḍa ʿalā. P801L04 منعت انا للجوارى, li- marking the object.
- Library label: `Night 166 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 167 is complete and unpublished, so the next firing should publish it.

## Night 167 (P803L03–P805L15, published 2026-11-21)
- Misprints: none.
- Kept as printed, with notes:
  - P803L06 امضي: read amḍī ("I will go"), with imḍī ("go!") noted. P803L20 لحظة: taken with what precedes ("bring him to me for a moment"); the other attachment is noted.
  - P803L04–05: the opening sentence starts "that the jeweller, when the slave-girl said to him…" and slides into his own "I" without finishing; the note explains it. P804L22 "the jeweller said to him" in the third person inside his own narration; noted.
  - P805L12 ولم اعلمها: read lam uʿlimhā ("nor told her the reason"); lam aʿlamhā noted. P805L14 فان ما عندها احفظ واقرب لكتمان السر غيري: loose grammar, read "she has no one besides me more trustworthy…"; noted.
  - Run-together ماجرى, مابك, مايسرّك, واعتذرلي kept as one word. Verse (P804L20–21) copied as printed; اَمَّا with no fa- in its answer noted.
- The night ends mid-speech of the slave-girl; her quotation is left open, as at the end of Night 165.
- Library label: `Night 167 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Night 168 is not complete yet (its tail is unread), so the next firing should transcribe.

## Transcription PDF 831–838 (pp. 809–816, 2026-11-21)
- Night labels P809L05 (169), P811L01 (170), P812L14 (171), P814L16 (172), P816L05 (173) are on their own lines with h, per precedent. Nights 168–172 are now complete and unpublished; the next five firings should publish them.
- P810 → P811: the print has no `وادرك شهرزاد الصباح فسكتت عن الكلام المباح` before the Night 170 label; the adjudicator confirmed no line is lost. The publishing run should close Night 169 without it (or note its absence).
- Kept as printed (possible misprints, for the publishing run to judge): P816L08 بالامراو (for بالامراء); P816L02 ظَفْرِهِ (verse; fatha on ظ). Spelling of حيٰوتي/حيوٰتي varies in where the small alif sits (P811, P812, P813) — copied as each image shows.
- Tightly set words split per archive precedent (امر لها, فيا ليت, ولا نهارا, لا تميل, ولو سعى, ولو سقيت); the print shows no visible space.
- Nothing to decide.

## Night 168 (P805L16–P809L04, published 2026-11-22)
- Misprints corrected (emend.json): P808L09 رأبته → رأيته; P808L18 رأنني → رأتني (the subject is ʿAlī's mother).
- Kept as printed, with notes:
  - P806L07 اتصر: not a known word; vocalised as aqṣir ("desist"), with iqtaṣir/ikhtaṣir named as alternatives. Not corrected, because ت/ق differ by more than dots and the reading is not certain.
  - P806L02–03 ولا تطول … ولا تبعد: read as jussive commands, lā tuṭawwil / lā tubʿid ("do not draw out … do not put off"); noted.
  - P807L09 فننجو read subjunctive fa-nanjuwa (indicative noted); P807L18 رفعت read rafaʿat (rufiʿat noted); P807L20 اني اذا رأيتني مت اذهب, an unfinished sentence that turns into a command; وهو with feminine وصية.
  - P807L23/P808L02 تغنّى read tughannī (ى for ي), taghannā noted. قدمات, اقدران and other run-together words kept as one word.
  - Verse P808L03–07 copied as printed; وَجِيْرَة with no final vowel and اِلْفِ/اجْتِمَاعِ with a single kasra are read with tanwīn in tr, as the metre requires; noted.
  - P808L15 cites Qurʾān 3:145; identified in the note.
- ʿAlī ibn Bakkār dies in this night; the tale continues (the jeweller's story to Shahrazād's frame), so the label stays "continued".
- Library label: `Night 168 · ʿAlī ibn Bakkār and Shams al-Nahār, continued`.
- Nothing to decide. Nights 169–172 are complete and unpublished; the next firings should publish them. Note for Night 169: the print has no closing formula before the Night 170 label (see transcription PDF 831–838).

## Night 169 (P809L05–P810L21, published 2026-11-22)
- Misprints: none corrected.
- Kept as printed, with notes:
  - P809L17 وقد علمت صبرها: read wa-qad ʿalimtu ṣabrahā ("and I knew what she was bearing"); عدمت ("she had lost her patience") is the likelier sense and is named in the note, but the printed reading makes sense, so it is not emended.
  - P810L09–11: the jeweller briefly in the third person ("the girl said to the jeweller", "he said to her"), "I" again from فقمت; noted. P810L11 تجديني noted as jussive or colloquial shortening.
- The print has no closing `وادرك شهرزاد الصباح` formula; the night ends on the bridge to King Shahramān's tale, and the last note says so.
- Glossary: the shared entry for شَهْرَمَانَ (Night 131's king of the Camphor Islands) was given an added sense for Qamar al-Zamān's father; بِأَعْجَبَ was corrected (bi- marks laysa's predicate; "than" is min).
- Library label: `Night 169 · ʿAlī ibn Bakkār and Shams al-Nahār ends`. The next tale's English name is for the Night 170 run to take from its heading.
- Nothing to decide. Nights 170–172 are complete and unpublished.

## Night 170 (P811L01–P812L13, published 2026-11-22)
- Library label: `Night 170 · Qamar al-Zamān begins`; title حِكَايَةُ قَمَرِ الزَّمَانِ. The print gives the tale no heading (Night 169 only announces "the tale of King Shahramān"), so the run named it after its hero; later nights should use `Qamar al-Zamān, continued`. Rename if you prefer another name.
- Misprints: none corrected.
- Kept as printed, with notes: P811L12 بالزيّنة (the shadda printed over the yāʾ, which no reading of zīna needs; kept, read bi-al-zīna); شكى/دعى with ى; مالي read mā lī ("I have no wish"); P812L06 verse اَوْقَلَّ run together (aw qalla); P812L08 يُعْطِى with ى (yuʿṭī); النِّسَا shortened for the metre. The first verse pair is attributed in its note to ʿAlqama ibn ʿAbada.
- Nothing to decide. Nights 171–172 are complete and unpublished.

## Night 171 (P812L14–P814L15, published 2026-11-22)
- Library label: `Night 171 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P813L04 خدة→خده, P813L05 وقدة→وقده, P813L11 and P813L12 والدة→والده (ة for ه), P813L18 الزاوج→الزواج.
- Kept as printed, with notes: P813L01 سري pointed sarā with the printed ي; ويروى read yarwī (yurwā possible); P814L04 مُظَفَّرَات with ظ for ض (braided); P814L05 مُجَرَّعَات passive where the sense may want active; P814L08 وَغَدٍ genitive where ghadan is expected; P814L09 تُسْكِنُهُ Form IV where Form I fits; P814L13 اختلي with ي for ى; first poem's metre named only as "appears to be" munsariḥ; the -āṣī poem's metre left unnamed.
- Nothing to decide. Night 172 is complete and unpublished; the next firing should publish it.

## Night 172 (P814L16–P816L04, published 2026-11-22)
- Library label: `Night 172 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P815L07 ولدة→ولده, P815L13 خصرة→خصره (ة for ه, as in Night 171).
- Kept as printed, with notes: واقفون (read as a circumstantial clause); مرت عليه يوم (feminine verb); يستحى with ى; رآيه; ويشكي; العاكر; ازدرت جفونه بالصارم البتار (obscure, candidates named); تهيّج read tahayyaja (imperfect noted); verse الْكَرَي, عَقَارِبٍ, حَرْكَاتِهِ, ظَفْرِهِ, وَارَى, وَاسِ noted; the poem is kāmil and is another version of a poem in Night 17. The night breaks off at يوم موسم; the print splits شهر زاد.
- Nothing to decide. No complete night is waiting; Night 173 needs the next transcription batch (PDF 839 on).

## Night 173 (P816L05–P817L09, published 2026-11-22)
- Library label: `Night 173 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P816L08 بالامراو→بالامراء (و for ء, as بكاو/ماو before); P817L08 احدوا درك→احد وادرك (space misplaced; entered as two word-level corrections, احدوا→احد and درك→وادرك, because emend.py matches single words).
- Kept as printed, with notes: الي beside الى; كؤس (vocalised kuʾus as printed, Classical kuʾūs); شان; ثلٰث; مسكوه (Form I); فى, يدى; ياولد set solid; شهامة الملك read al-mulk (al-malik named in the note).
- Nothing to decide.

## Night 174 (P817L10–P818L09, published 2026-11-22)
- Library label: `Night 174 · Qamar al-Zamān, continued`.
- Misprints: none corrected.
- Kept as printed, with notes: P818L05 با لوزير split (read bi-al-wazīri); عامي vocalised ʿāmmiyyin (no shadda printed); ماجرى, لاينفعه set solid; فى with ى; وأمره read wa-ʾmurhu with the printed أ.
- Glossary: shared كِتَافَهُ corrected from 'his shoulders' to 'his bonds'; the shared وَالِدِهِ entry carried a remark about "sentence 97" of some earlier night (house business) — dropped; the night it came from was not traced.
- Nothing to decide. Nights 175–178 are complete and unpublished.

## Night 175 (P818L10–P819L16, published 2026-11-22)
- Library label: `Night 175 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P818L14 والده→ولده (the king is anxious about his son; the same sentence goes on لم يكن له ولد سواه).
- Kept as printed, with notes: الغضاة (al-ghaḍā); متشوش; لم يجىء; شيأ; فى/في; على الذي اساء الادب (alladhī as a bare "that"); the khādim and the mamlūk who serve the prince are not said to be one man; no شعر rubric before the third poem.
- Verse copied as printed; tr follows the printed vowels (uqūlu for اُقُوْلُ, ḍūʾa for ضُوْءَ, banāta for وَبَنَاتَ), the intended reading in the note, as in earlier nights. ساهٍ after raʾaytu, اَلْقٰى (subject left open), and تَبْرِي (as printed "pares"; translated "heals" by the sense) noted.
- Nothing to decide. Nights 176–178 are complete and unpublished.

## Night 176 (P819L17–P820L13, published 2026-11-22)
- Library label: `Night 176 · Qamar al-Zamān, continued`.
- Misprints: none corrected.
- Kept as printed, with notes: P820L12–13 فسكتت من الكلام المباح (min, where the print has ʿan in every other dawn formula; sound Arabic, so not treated as a misprint); الد مرياط split (one name, al-Dimiryāṭ, vowels uncertain); بئر روماني معمورة (masculine adjective on a feminine noun); قميص مشمع ("waxed shirt", the cloth doubtful); الاطلس المعدني (probably satin shot with metal thread); ليلة اربعة عشر (bare masculine number); موقود (later form for mūqad); كانه, فى; second محشوة printed without shadda (supplied).
- Nothing to decide. Nights 177–178 are complete and unpublished.


## Night 177 (P820L14–P822L17, published 2026-11-22)
- Library label: `Night 177 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P822L03 انسم→اقسم ("I adjure"; the next sentence answers لقد اقسمت عليّ); P822L08 الميلة→الليلة ("this night"; P822L11 repeats في هذه الليلة).
- Kept as printed, with notes: شيأ; فاستجاربها and وتريدان run together; لعطبه used transitively ("would destroy him"); the verse's printed pointing; فى/في.
- Nothing to decide. Night 178 is complete and unpublished.
## Night 178 (P822L18–P824L03, published 2026-11-23)
- Library label: `Night 178 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P823L10 وجراب→وجواب ("and a ready answer", paired with عقل وافر; جراب "bag" gives no sense).
- Kept as printed, with notes: verse ثَلْثُ ذَوائِبِ (print's vowels do not scan; thalātha dhawāʾiba wanted); لَوْ لَا اُمْسِكَ (singular where the metre wants umsikā); تعلّق في ضعيف and اذا همّت تقوم; الخيّال with printed shadda (khayāl probably meant); باعكان; كماينبغي and اذكرلك set solid; line-final lone و before متصل; شيأ; سيدتى/سيدتي.
- Glossary: shared يَرَاهُ corrected (lemma raʾā; the old remark about an indicative for a subjunctive was wrong, the forms are identical).
- Nothing to decide. Night 179 is not yet complete (its tail is untranscribed).

## PDF 847–854 (pp. 825–832, transcribed 2026-11-23)
- For the publishing run (Night 180/181): P828L01 is printed ملّي where the sense wants عليّ (لكِ عليّ ذلك, joining from P827L23) — a clear misprint; archived as printed, to correct via emend.json per README rule 5b.
- Kept as printed, possibly misprints, for the publisher to judge: P826L02 اقوه اقوه (the ق shows a single dot; افوه possible); P829 verse يَنْصِفُ; P832 verse فَالمَّاسُ (sense wants فالناس); P832L20 موعوبا; P830L01 ميمولة (ميمونة meant?); second دهنش on P829L01 possibly printed دهمش.
- Word splits kept where the print leaves a word-width gap: بند قي (P828), وجما لهما, الا ثنين, احد هما (P832). P830L20 verse has no gap between hemistichs, so no " * ".
- The plan's "Lines archived" running sum had drifted (the 2026-11-22 run did not add its 173); replaced with the count from archive/ (18450).
- Nothing to decide.

## Night 179 (P824L04–P826L13, published 2026-11-23)
- Library label: `Night 179 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P826L02 اقوه→افوه twice (the interjection of disgust, printed افوه in Night 23); P826L04 ربالتك→ريالتك ("your drool", with سالت); P826L07 فلبي→فابي ("and he refused"; فلبّى "he complied" contradicts the next clause فلما خالف اباه). The last is the least certain of the four (one letter, ل for ا); if the owner prefers it kept as printed, drop its emend.json entry and restore the note.
- Kept as printed, with notes: السعيدان, وصفتهالك, ولابد, ياسيدتي, اوتأسريني set solid; وارسل كاتب الملوك (no و between the verbs; kātiba al-mulūki possible); عشرة عجائز, السبع/السبعة قصور; قوارة البول (qawwāra not in Lane; read as a form of qārūra); معشوقتي (fem.) of Maymūna's male beloved; ضِحكت with printed kasra.
- Glossary: shared مَيْمُونَةَ rewritten (it described only the Night 5 couplet's Maymūna as if universal, with "see note"); shared لِأَنِّي now glosses its li-.
- Nothing to decide. Nights 180–182 are complete and unpublished.

## Night 180 (P826L14–P828L11, published 2026-11-23)
- Library label: `Night 180 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P828L01 ملّي→عليّ (لكِ عليّ ذلك, joining from P827L23).
- Kept as printed, with notes: قدا فرغا (space misplaced in قد افرغا; pointed across the break, qad ufrighā); بند قي (bunduqī, "Venetian", set as two words); بتأمّل (possibly يتأمّل, one dot; kept); verse الخَنِق (الحَنِق possible) and nominative خَوْفُ where an accusative of reason is wanted; دهنشا with accusative alif only on P827L06; الساعه, تقضى, اجئ/تجئ; rubric شعر kept in the prose unit before the verse.
- Nothing to decide. Nights 181–182 are complete and unpublished.

## Night 181 (P828L12–P830L02, published 2026-11-23)
- Library label: `Night 181 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P828L18 verse تَذَلُّلًا وَتَذَلُّلَا → second word وَتَدَلُّلَا ("abasement … coquetry", one dot; the same verbal noun joined to itself by wa- is not idiom). The drafter rated it doubtful, the reviewer clear; corrected as clear. If the owner prefers the print, drop the emend.json entry and restore "abasement upon abasement".
- Kept as printed, with notes: verse يَنْصِفُ (yunṣifu wanted), رَايْتُ, وَاهْوِ (ihwa expected), مُنْحِفُ, وَدَدْتُهُمَا, لَوْاَنَّ set solid; prose اواخوان set solid; تخفى. P829L11 بِالْعَجْزِ … وَاَضْعَفُ is stiff; the reviewer suggested la-aʿjazu, declined because it breaks the kāmil metre.
- Nothing to decide. Night 182 is complete and unpublished.

## Night 182 (P830L03–P832L17, published 2026-11-23)
- Library label: `Night 182 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P832L07 verse فَالمَّاسُ → فَالنَّاسُ ("people beat on cold iron"; the printed shadda after the article only fits a sun letter, and الماس "diamond" gives no sense). Print's other marks kept.
- Kept as printed, with notes: verse انْصَفُوا (anṣafū), اَنَّهُ (innahu wanted), هَجْرُكَ (hajraki wanted), رَقَّصَتْ without object, لِلْاِعْدَادِ, تَرْنِيْ; prose السعيدان, لابداني, بلاشعور, يادهنش, ياقشقش, اريدان set solid; وجما لهما, الا ثنين, احد هما split; عيناة/يداة/رجلاة (ة for ه); ايها السيدة; المداري (exact sense uncertain).
- Glossary: review corrected several older shared entries' senses for this night (الْأَسَدِ, بُرْغُوثٍ, رَفِيقِهِ, مَحْبُوبِي, أَحْسَنْتَ, اَحْسَنَ) by appending.
- Nothing to decide. Night 183 is not yet complete (its tail is untranscribed).

## PDF 855–862 (pp. 833–840, transcribed 2026-11-23)
- For the publishing runs (Nights 183–187), clear misprints archived as printed, to correct via emend.json per README rule 5b: P834L13 بجابنى (sense wants بجانبى); P839L22 الاوض (الارض); P837L01 لقمر الرمان (ز undotted; الزمان everywhere else). P840L23 is archived طلعت (one pass saw طلمعت, an extra tooth; the adjudicator read طلعت).
- Possible misprints, for the publisher to judge: P834L12 عضب (غضب wanted; first letter undotted); P836L14 وانطرالى (ظ undotted?); P836L17 خط where the sense wants غط; P835L13 وفرصتها (قرصتها?); P839L04 ورفصه (ورقصه?).
- P835L03 verse: both passes omitted a sukun on the final و of جودوا; added by hand after checking the crop. The first و may carry one too and سادتي may have a sukun on the ي; not added, marks too doubtful at this crop.
- P838 ه/ة: five finals after د/ذ (وساعده, عنده, فوجده, هذه) read ه by the adjudicator (medium confidence; the glyph lacks the separate dots of the nearby ة).
- Nothing to decide.

## Night 183 (P832L18–P834L04, published 2026-11-23)
- Library label: `Night 183 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P832L20 موعوبا→مرعوبا ("terrified"; the same sentence closes Night 182 with مرعوبا).
- Kept as printed, with notes: P834L03 لا تملى بها read as li-atamallā bihā, "that I may take my fill of her", one word split by the print's spacing (tamallā bi- as in Night 179; the drafter's alternative lā tumlī bihā, "do not delay with her", named in the note); P834L01 حذري read as ḥazrī "my guess" (ḥadharī possible); P833L04 بقامة النيّة (الفيّة possible); verse وَرْدُ خَدٍّ lacks the wa- the munsariḥ metre needs; غِزَالًا with kasra; فَسَاعَةُ nominative; السعيدان, لايقدر, ماشاء set solid; ثلث, نائمه, هى/وهى/زوّجنى.
- The reviewer believed the couplet بدت قمرا ومالت غصن بان is al-Mutanabbī's; not verifiable from the sources this pipeline may use, so not stated to the reader.
- Nothing to decide. Nights 184–186 are complete and unpublished.

## Night 184 (P834L05–P836L03, published 2026-11-23)
- Library label: `Night 184 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P834L12 عضب→غضب; P834L13 بجابنى→بجانبى; P835L13 وفرصتها→وقرصتها (the flea "nipped" her, as Dahnash in Night 183).
- Kept as printed, with notes: P834L07 لا تملّى بها read li-atamallā bihā, as in Night 183 (lā tumlī named, needs the shadda set aside); P834L11 والفت read as alfata, "turned (his face) away" (lafata with a stray alif, or iltafata, named); بالنيام pointed niyām (verbal noun of nāma, Lane), not Middle Arabic; اني اذا نبّهتها loosely built; ومنقوش without accusative alif; مالي, ومافعله set solid; شيأ, استحى. P834L20 تذكرة لها read "a reminder for her" (keepsake of her named).
- Glossary: the shared entry مَهْمَا analysed a wa- the key lacks; corrected to the plain particle.
- Nothing to decide. Nights 185–186 are complete and unpublished.

## Night 185 (P836L04–P837L17, published 2026-11-23)
- Library label: `Night 185 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P836L14 وانطرالى→وانظرالى (set solid as printed); P836L17 خط→غط (ghaṭṭa fī al-nawm); P837L01 الرمان→الزمان; P837L14 موصغا→موضعا.
- Kept as printed, with notes: P837L10 صدرها ("her chest"; the sense seems to want صدره "his chest" — doubtful, the idiomatic line follows his); P836L06 هذ اشاب (alif misplaced by the spacing, read hādhā shābb); بحيوتي; فم without accusative alif; السعيدان, ماباله, مالك set solid; الخضرة (dusky skin or garden imagery, left open); هارشني/ناغشنى (exact sense uncertain); وثقلت read thaqulat (thaqqalat possible).
- Frank passage (Budūr caresses the sleeping Qamar al-Zamān, both adults) translated in full, per "never bowdlerize".
- Nothing to decide. Night 186 is complete and unpublished.

## Night 186 (P837L18–P839L11, published 2026-11-23)
- Library label: `Night 186 · Qamar al-Zamān, continued`.
- No misprint corrected. Kept as printed, with notes: P838L01 ثم كتبت له وثيقة انه اعتقها read annahu aʿtaqahā (the pronouns fit the scene poorly; انها اعتقته would be expected — doubtful, not emended); P838L20–21 وهل وصل من قدرك انت الآخر انك تخادعني loosely built, sense given as scorn and flagged uncertain; P839L05 سلبة "rope" pointed salaba (uncertain); P839L07 يغطس read yughaṭṭisu (Form II, transitive); الا قليلا, انثي, رفصه, شاله, نشله, ولازال as Middle Arabic; شهر زاد split across P839L10/11.
- The servant is named Ṣawāb here for the first time.
- Nothing to decide. Night 187 is not yet complete (its tail is untranscribed).

## Night 187 (P839L12–P841L13, published 2026-11-23)
- Library label: `Night 187 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P839L22 الاوض→الارض (على وجه الارض).
- Kept as printed, with notes: P839L18 الغطاس read al-ghiṭās "dunking" (vowels a guess); P839L20 وتشطب read tashaṭṭaba "was scratched" (Form V); P840L09 سجنه read sajnihi "his imprisoning" (sijnihi possible); P840L16 ويكلفنى اني اخبره لها وبمن اخذها loosely built, bi-man also possibly "by means of whom"; P841L06 فسلامة شبابك… read as a wish (an oath reading possible, no bi-); يهدي for يهدأ, مغلوق, kallafa + anna + imperfect as Middle Arabic; فرأه pointed with dagger alif; شهرزاد solid as printed.
- Review: يا مولانا السلطان pointed al-sulṭāna (accusative apposition after the vocative); earlier nights are split on this (‑u 7, ‑a 4, ‑i 6) — not swept, left as published.
- Nothing to decide. Nights 188–191 are complete and unpublished.

## Night 188 (P841L14–P843L23, published 2026-11-24)
- Library label: `Night 188 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P841L22 نقال→فقال; P842L13 اضعاث→اضغاث (printed correctly at P842L15).
- Kept as printed, with notes: P843L11 وانا مها بجانبي vocalised mahan "oryxes" (likely a dropped ع of معها "with her"; the idiomatic line gives that sense); P843L19 ثم عد انّي بالجواب vocalised innī with the print's shadda (likely sense ilayya, "to me"); بطل read baṭṭala (baṭala … al-ḍarbu possible); قلبتها qallabtuhā; والّا يهلكني indicative; كلّيت kallaytu; يرفص yarfuṣu; فرماة with ة for ه; احد ثك and الا مركلّه split as printed.
- Glossary: the shared entry إِنَّمَا analysed a wa- the key lacks; corrected.
- Nothing to decide. Nights 189–191 are complete and unpublished.

## Night 189 (P844L01–P846L05, published 2026-11-24)
- Library label: `Night 189 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P845L04 العضب→الغضب (bi-ʿayni al-ghaḍabi, "with the eye of anger").
- Kept as printed, with notes: P846L02 وشوّفتنى read wa-shawwaftanī (likely شوّقتنى "made me long for her", one dot away — doubtful, not emended; the idiomatic line follows "long"); P844L10 ابشْر with the print's misplaced sukūn (read abshir); P844L15 لاسمرّنك with the print's shadda on the rā (read la-asmurannaka; Form II la-usammirannaka named); P845L12 جمادي الاخرى (usual al-ākhira); ة for ه in بشرّةِ, واخبرة, والدة, وراءة; السعيدان, قدجنّ, ماجنّ, وارادان, ذوالقعدة set solid; الثلثاء with dagger alif.
- Nothing to decide. Nights 190–191 are complete and unpublished.

## Night 191 (P847L01–P848L13, published 2026-11-24)
- Library label: `Night 191 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P848L01 ويأنيك→ويأتيك, pointed wa-yaʾtiyaka (subjunctive, continuing ḥattā yufarrija).
- Kept as printed, with notes: P847L13 ترغبني read turaghghibunī (Form II, no shadda printed); P848L04 ان مابك جنون read an mā bika junūnun "there is no madness in you"; P848L06 بالله … انك تفعل read innaka (annaka possible); P848L07 والامتّ set solid, wa-illā muttu; مختفي, وقل (dagger alif), لولا … كنت without la-, ناول … لابيه as Middle Arabic; verse P848L02 الدَّهْرُ nominative after لعلّ and P848L09 تَزْوِيرُ nominative as predicate of kāna kept as printed and noted.
- The night ends on وانشد هذه الابيات; the verses open Night 192.
- Nothing to decide. Night 192 is not yet complete (its tail is untranscribed).

## Night 192 (P848L14–P851L10, published 2026-11-24)
- Library label: `Night 192 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P849L07 والدك→ولدك (the vizier speaks of the king's son, as at P849L12); P850L01 التصر→القصر; P850L06 الديباح→الديباج; P851L01 الملح→المليح (printed in full at P851L05); P851L04 البست→الست.
- Kept as printed, with notes (all verse): وَلَا تَخْدَعُوا printed active (sense wants passive tukhdaʿū); مُقْلَتَيْهِ possibly for مقلتيها; خَرَّسَتْ Form II for the metre; مُنْصِفُ nominative after mā. Spelling habits noted: ة for ه (ولدة, والدة, عندة), متي, رأه (dagger alif), باسها, ينفسد, فليداوي, ليالي, السبعة قصور.
- nights-191: its last note said the verses "open the next night"; Night 192 shows they are never given (he recites "also these verses"). Note corrected.
- Nothing to decide. Nights 193–194 are complete and unpublished.

## Night 193 (P851L11–P854L17, published 2026-11-24)
- Library label: `Night 193 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P853L09 اخيك→اختك (ukhtaka; the mother speaks of Budūr, حصل لها); P853L15 بذور→بدور; P854L02 وانفا→واقفا (qāma wāqifan).
- Kept as printed, with notes: P851L22 فقتلها read with the sword as subject (likely a dropped ت for فقتلتها, doubtful, not emended); P854L05 اقسام read "conjurations" ("sections" of his books possible); P853L20 ثاني يوم العشاء loosely built; P852L14 راس given its hamza as at P852L12; غلام بائتا, اقصي, بنته, لعل ان as Middle Arabic.
- Nothing to decide. Night 194 is complete and unpublished.

## Night 194 (P854L18–P856L19, published 2026-11-24)
- Library label: `Night 194 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P855L03 فطننت→فظننت; P856L15 جرائر→جزائر (printed correctly on the lines around it).
- Kept as printed, with notes: P855L06 او اعانتة read iʿānatahu "helping him" (likely اعانقه "embrace him", one letter away — doubtful, not emended); P856L06 تمشي read as the perfect tamashshā (ي for ى); verse P856L03 مَزُورِ "one visited" (sense uncertain); الطيرب vocalised al-Ṭayrab (a guess); ة for ه (امرة, اخذة, اعتراة, هذة, verse اراة); السعيدان, وانايا, البرفستة set solid.
- Shared glossary: وَأُفَتِّشُ said its marks were the print's; at P855L22 the print has none — sense appended saying so.
- Nothing to decide. Night 195 is not yet complete (its tail is untranscribed).

## Night 195 (P856L20–P858L01, published 2026-11-24)
- Library label: `Night 195 · Qamar al-Zamān, continued`.
- `nights_index.py` flagged ORDINAL MISMATCH at nights 200 (الموفية للمائتين) and 201 (الاولى بعد المائتين): it did not know the dual "two hundred". This run added مائتين/مايتين/مائتان/مايتان = 200 to its number table, as earlier runs added forms for 101 and 120; the table now reads 195–200 complete with no mismatch. Night 195 lies before the flagged nights and was published.
- Misprints corrected (emend.json): P857L10 and P857L18 اى→الى.
- Kept as printed, with notes: P857L10 لا نقل vocalised li-anqula "so that I may bring (him) in" (لانقذ "to rescue", one letter away, named, not adopted); يطلّع read yaṭṭallaʿu (Form V, "pry into"); ردّت روحه read passive ruddat (raddat possible); المقدركان set solid; الممشاة with ة; شهر زاد set as two words; يكفي ماجرى, ربما انك, مسكه من شعر رأسه, في حال العدم as Middle Arabic.
- Nothing to decide. Nights 196–200 are complete and unpublished.

## Night 196 (P858L02–P859L06, published 2026-11-24)
- Library label: `Night 196 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P858L22 نقال→فقال.
- P858L15 وصفَته: the print's fatḥa sits on the fāʾ, which no reading with the sense "you described" (waṣaftahu) allows; the mark is moved and pointed وَصَفْتَهُ, as with تلّفت (P579L22), and the note gives the print's placement. No emend entry (marks only).
- Kept as printed, with notes: من منذ, فابي (ى as ي), فى, ملقى, حيٰوته and ثلٰث with printed dagger alif, السعيدان, لايتكلمون, والّافتروح set solid, اذا … لا تنظر without fa-.
- Nothing to decide. Nights 197–200 are complete and unpublished.

## Night 197 (P859L07–P860L15, published 2026-11-24)
- Library label: `Night 197 · Qamar al-Zamān, continued`.
- No misprints corrected. Verse P859L13–P860L11 copied as printed; kept with notes: رُمِيْْتَ (two sukūns, read rumīta), شَجِي after ذا read for the noun shajā, لِحَاظُ nominative after لٰكِنَّ, اِنِّي with kasra after تحسبوا, خِضَابُ without tanwīn, مُتَّهِمِي read as "accuser", الْفَضْلَ accusative after قلت, وَاعْجَمِ with bare alif, tanwīn on Luqmān, Yūsuf, Dāwūd, Yaʿqūb, Yūnus and Ayyūb. Prose: صغى with ى (ṣaghā), قمرالزمان and شهر زاد spaced as printed.
- Shared glossary: الْفَضْلَ (only the name al-Faḍl) and تَحْكِي (only "you tell") given the senses needed here.
- Nothing to decide. Nights 198–200 are complete and unpublished.

## Night 198 (P860L16–P862L03, published 2026-11-25)
- Library label: `Night 198 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P861L20 نطاوعه→فطاوعه.
- P860L17 ان مرزوان قال لوالده يا ابي: the print gives Marzawān words that Night 197 gives to Qamar al-Zamān (to his father). More than one letter is involved, so kept as printed and explained in the note; not emended.
- Kept as printed, with notes: يرمى (ى for ي), اسو حال (hamza dropped), علي يدي (ي for ى), فى, مابه and قرّعينك and قمرالزمان set solid, والسبعة قصور, فرحت الناس.
- Shared glossary: الْجَوَّانِيَّةِ said the print marks the shadda; at P861L03 it is bare — note appended.
- Open (for the owner, nothing waits): published nights write both li-llāhi (≈42×) and li-Allāhi (≈31×) in `tr`; this night uses li-llāhi. Meanwhile runs follow the majority li-llāhi.
- Nothing else to decide. Nights 199–200 are complete and unpublished.

## Night 199 (P862L04–P862L21, published 2026-11-25)
- Library label: `Night 199 · Qamar al-Zamān, continued`.
- No misprints corrected. Kept as printed, with notes: السعيدان set solid, عند هما split, بماجري (solid, ي for ى); verse صَدِيْق printed without tanwīn (read ṣadīqun for the metre); وردت read passive ruddat (raddat possible).
- Shared glossary: فَرْحَتِهِ gave the verb's form faraḥa for the noun farḥa; corrected.
- Nothing to decide. Night 200 is complete and unpublished.

## Night 200 (P863L01–P864L12, published 2026-11-25)
- Library label: `Night 200 · Qamar al-Zamān, continued`.
- No letter misprints. P863L05 فزينّت: the print's shadda sits on the nūn; moved to the yāʾ (فَزُيِّنَتِ), note gives the print's placement (marks only, Night 196 precedent; no emend entry).
- Kept as printed, with notes: السعيدان, ياسيدي, لايقدر, اريدان, لاتبت, الاليلة, غدتأتي, الابك, وامران set solid; انك + imperative استأذن; اننا ندبر; ولا تخلي; الف يوم مبارك الذي قواك (الذي without antecedent; read as a blessing on whoever healed him); verse بِسَاطُ nominative, سُلَيْمَانِ with kasra, فَدَيْتُكُ, اَلَيْكَ, bare عَذَاب, فَاصْلَى without hamza.
- In verse, tr gives the reading (fadaytuka, ilayka) where the print's vowel is impossible, but follows the print where it is merely irregular (bisāṭu, Sulaymāni). Noted for consistency; nothing waits.
- Nothing to decide. Night 201 is not yet complete (tail unread); the next firing transcribes.

## Transcription pp. 865–872 (PDF 887–894, 2026-11-25)
- **P870L01 restored by hand.** The detector counted the page's first body line, وكتب ايضا (stretched across the measure with a kashida, ending in alif), as part of the running header (gate header_lines=2), so neither pass saw it. The adjudicator flagged the 869→870 join as broken; the line was read from a 250 dpi render of PDF 892 and inserted, and the page renumbered (P870L02–L24). Written without "—": the stroke is kashida inside ايضا, not a filler rule. Worth knowing for later pages that open with a short centred-ish line: check gate header_lines > 1.
- **P869L01–L20: the saj' asterisks restored by hand.** The print sets `*` between the rhymed clauses of Qamar al-Zamān's letter; both passes dropped every one (so no dispute arose). Added from the image; the text between them is unchanged (checked by script). The prompt does not mention prose asterisks; a future prompt edit might say "keep a printed `*` in prose too".
- **السعيدان / السعيد ان in the night formula.** The adjudicator reports the print sets it solid; both passes split it on P865L19, P867L08, P868L11 (undisputed, left as the passes wrote it) and the disputed P870L18 was ruled solid. Earlier archives are also mixed. Decided meanwhile: no hand change; a publishing run reads the formula the same either way.
- Misprints recorded as printed, for emend.json at publishing: P869L18 فزير (for غزير), P872L13 بعانيتها (for بعافيتها, low confidence), P872L16 شوتها (for شوقها).
- Nothing waits on the owner.

## Night 201 (P864L13–P865L17, published 2026-11-25)
- Library label: `Night 201 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P864L18 عظهما→عظمهما.
- Kept as printed, with notes: ثلٰثة (dagger alif printed), مازالا, مانريد and ماسلا set solid, ما ذا split, نعم ما apart; نجر of bones (read 'hacked'; a slip for another verb possible); سائرين plural for dual; مقطّعا/عليه singular for two garments; اخذنا بها منه الاذن (bi- of time); verse فَاسْتَوْجِبُ with ḍamma, الرِّضَى, هَاجِرِيْ, تُبْدِى.
- Nothing to decide. Nights 202–204 are complete and unpublished.

## Night 202 (P865L18–P867L06, published 2026-11-25)
- Library label: `Night 202 · Qamar al-Zamān, continued`.
- No misprints corrected. Kept as printed, with notes: علي for على (P865L20), مطلى (ى; read spoken maṭlī), فى, ثلثة, جاؤا, الرؤس (one wāw), مارأوا set solid; وترمي read subjunctive after the prohibition (indicative possible); باقلام المطالب loose in sense (noted); "he took the gear" said twice (P866L14–15), the narrator's repeat, not a misprint.
- tr uses bi-Allāhi (house majority, ≈108 vs 6), not bi-llāhi.
- Nothing to decide. Nights 203–204 are complete and unpublished.

## Night 203 (P867L07–P868L09, published 2026-11-25)
- Library label: `Night 203 · Qamar al-Zamān, continued`.
- No misprints corrected. P867L14 prints انزل أ اتنا: a lone precomposed أ, then اتنا. Kept as printed (two tokens), pointed انْزِلِ أ أْتِنَا (the lone أ left unvowelled as the silent opening alif) and read iʾtinā, 'bring us'; the note says the reading is likeliest but not certain.
- Kept as printed, with notes: شيٌ with printed tanwīn after ايّ (tr shayun, following the pointing); verse وَالْمَعْنِي and فِى; يدى with ى; زوّجته بها, يستعجل على, مسكه, الست, قدّام flagged as later usage; اطلعه 'brought him up'.
- Nothing to decide. Night 204 is complete and unpublished; the next firing publishes it.

## Night 204 (P868L10–P870L16, published 2026-11-25)
- Library label: `Night 204 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P869L17 كثيرا لزفرات → كثير الزفرات (the article's alif set on the previous word; two entries), P869L18 فزير → غزير.
- Kept as printed, with notes: وابرؤها/فابرؤها (ؤ; read Form IV ubriʾuhā), علي and الي (read ʿalā, ilā), تطفى without hamza, مايتمنّى set solid; ولا اظرف read wa-lā aẓrafa, 'none more gracious' (a slip for another word, e.g. aẓlam, possible); والبلاء لمن يئس taken as its own clause; وادخل بها read adkhala bi- (doubled transitivity); verse عَارِفُ, مُتَحَيِّرُ, سَلَامُ with single ḍamma, الْهَوَي with ي, فَارْسِلِي without hamza (tr fa-irsilī).
- Shared glossary: three wrong entries corrected — فِيْ ('extra yāʾ for the meter' → printed sukūn on the long vowel), اَلْقَاهُ (Form IV / 'Middle Arabic spelling' → Form I of laqiya, ى written ا before a suffix), سَلِي (salī for isʾalī).
- Nothing to decide. Night 205 is not yet complete (tail unread); the next firing transcribes.

## Transcription pp. 873–880 (PDF 895–902, 2026-11-25)
- **Header detection went both ways this batch.** On PDF 896, 898 and 901 the running header was counted as body crop line01 (gate header_lines=0); on PDF 897 the centred night label, and on PDF 900 the page's first four verse lines, were cut off as header (header_lines=2) and had no crops. The run spotted it from the gate numbers and told the passes; both passes recovered the lines from band1 and agreed on them. Worth a detector fix some day; meanwhile a run should look at band1 whenever header_lines ≠ 1.
- **Both passes read most prose lines on PDF 896, 898 and 900 from the bands, not the crops**, so shared errors would not show as disputes. The adjudicator re-read those lines against the crops and found two shared misses (P878L15 يا لَله fatha, P878L08 verse فِيْ sukūn), both fixed by verdict.
- Misprints recorded as printed, for emend.json at publishing: P875L02 ليبصرة (for ليبصره), P876L19 تمر الزمان (for قمر), P878L13 تجدة (for تجده), P879L02 ومازات (ل damaged or missing; for ومازالت), P879L10 الآنبوس (for الآبنوس), P880L06 لم أامن (for آمن), P880L08 الآ ان (spurious madda on الا).
- Nothing waits on the owner. Nights 205–208 are complete and unpublished; the next firings publish them.

## Night 205 (P870L17–P873L05, published 2026-11-25)
- Library label: `Night 205 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P871L08 فرعت→فرغت, P872L13 بعانيتها→بعافيتها.
- Kept as printed, with notes: P872L16 شوتها (not a word as printed; read 'her desire', likely شهوتها with hāʾ dropped, شوقها possible); P872L20 استهدى سرّ (read as استهدأ, 'his heart was at rest'; doubtful); verse عَظْمِ pointed ʿaẓm where the sense wants ʿuẓm 'greatness'; verse مِنْكَ masculine to a feminine eye; وصلبت in the later sense 'braced'; السعيدان, كادان, بعد كما, شهر زاد and verse يَاعَيْنُ/فَيَاكَبِدِي/مَاكَوَاكَ spacing as set.
- Nothing to decide. Nights 206–208 are complete and unpublished; the next firings publish them.

## Night 206 (P873L06–P874L22, published 2026-11-25)
- Library label: `Night 206 · Qamar al-Zamān, continued`.
- No letter misprints. P873L17 prints سنّية with the shadda on the nūn; the word is saniyya, so the pointing corrects it to سَنِيَّة and the note gives the print's form (rule 5b; bare letters unchanged, so no emend.json entry). The reviewer proposed keeping both shaddas and romanising sanniyya; not taken, as that reads a non-word.
- Kept as printed, with notes: الهجن العشاري (ʿushārī uncertain), وحمل read Form II, هي واياه, اوصاه على, بنته, الكلاء, كلما for كل ما, فياترى, ما ذا, شهر زاد; verse الزَّمَان without case vowel and الْعَشْرَةِ pointed 'ten' where the sense is ʿishra 'companionship'.
- Nothing to decide. Nights 207–208 are complete and unpublished; the next firings publish them.

## Night 207 (P875L01–P876L17, published 2026-11-25)
- Library label: `Night 207 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P875L02 ليبصرة → ليبصره.
- Kept as printed, with notes: يالَلّٰه العجب ان read yā la-llāhi! al-ʿajabu anna (inna possible); البلاد العمار read al-ʿamār (ʿimār/ʿummār possible); verse وَصَمَمْتُهُمْ 'deaf to them' or 'stopped them up'; verse لَا تُبْقِي indicative read as statement; وحسّ, ساخت روحه, جريتي/مشيتي, تعبانا, مرق, الهنا, لحّ flagged as later usage; run-together وطاربه, الجوفنام, وارادان, شهرزاد kept as set.
- Nothing to decide. Night 208 is complete and unpublished; the next firing publishes it.

## Night 208 (P876L18–P879L07, published 2026-11-26)
- Library label: `Night 208 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P876L19 تمر الزمان → قمر, P878L13 تجدة → تجده, P879L02 ومازات → ومازالت.
- Kept as printed, with notes: مرابعا / لاجل المرابع (read murābiʿ, a sharecropping garden hand; the vowels and sense are ours, and المرابع may stand for المرابعة); بيوت الاشجار read as the water basins round the trees; الفاس pointed al-faʾs; وان عندنا مركبا read wa-anna (inna possible); الحمد لله الذي اتيت with no returning pronoun (a later-language turn); ويعمل joined loosely to قعوده; حيٰوة with printed dagger alif; يا لَله العجب as in Night 207; verse قَرِيحَةٌ/مُتَيَّمُ nominative after مَا/لَا, as printed.
- Nothing to decide. Night 209 is not yet complete (tail unread); the next firing transcribes.

## Transcription pp. 881–888 (PDF 903–910, 2026-11-26)
- **Header detection again went both ways.** On PDF 904–907 the running header was crop line01 (gate header_lines=0); on PDF 910 (header_lines=2) the page's first two body lines (P888L01 prose, P888L02 verse) had no crops; on PDF 909 the centred ومن ذلك قوله (P887L14) fell in a gap with no crop. All recovered from the bands by both passes and confirmed by the adjudicator. Still worth a detector fix some day.
- **Both passes left the own-line night label P883L02 without `h`**; set to `h` by the run before adjudication, matching every earlier own-line label (the adjudicator confirmed it is centred).
- **51 shared misses** were fixed by the adjudicator on lines the passes read from the bands (mostly sukun on long vowels in verse; also شهر زاد spaced at P883L01, السعيدان solid at P887L05, حيٰوة with upright alif at P887L20–21, matching P879L06).
- Misprints recorded as printed, for emend.json at publishing: P881L03 مَذَا (for ماذا), P887L06 "على عليه" (على presumably for عدى; doubtful — keep and note). Low confidence: P881L05 عَلِقْتُهُمْ (type damaged; علقتهم from sense).
- Nothing waits on the owner. Nights 209–211 are complete and unpublished; the next firings publish them.

## Night 209 (P879L08–P883L01, published 2026-11-26)
- Library label: `Night 209 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P879L10 الآنبوس → الآبنوس, P881L03 verse مذا → ماذا, P882L20 هذة → هذه.
- Kept as printed, with notes: السعيدان run together (السعيد ان); لم أامن with printed hamza + alif for آمن; الخيّام with a printed shadda; تايه for تائه; الآ read illā; the name spelled حيوٰة (dagger alif over the wāw) on p. 880 and حياة on pp. 881–882; verse عَلِقْتُهُمْ (damaged type, likeliest reading); verse كَرَمُ ابْنُ زَائِدَةِ with nominatives where the sense wants acc./gen.; هنّوها, دعوا لها جميع الخلق, اضمر على flagged as later usage; stray و at P882L12 kept as set.
- Nothing to decide. Nights 210–211 are complete and unpublished; the next firings publish them.

## Night 211 (P884L17–P887L03, published 2026-11-26)
- Library label: `Night 211 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P886L08 ونظاروا → ونظروا.
- Kept as printed, with notes: ordinal الحادية عشر (ʿashar for ʿashrata); الي for الى; يزالو without final alif; وزغرتت / الزغاريت; رؤسهم; وحثّوا with printed shadda (ḥaththū, where throwing dust wants ḥathaw; doubtful); verse بِجَنَانِهِ pointed janān where the sense wants jinān (Paradise); verse حَلِفِ الضَّنَى (ḥalif for ḥalīf); verse يَحْظُ pointed with damma for jussive yaḥẓa; run-together ماكان, وماصدق, واولداه, verse لَاتَعْذُلُوا, لَايُزِيْلَ, وَسَارَعَنَّا; شهر زاد as set.
- Nothing to decide. Night 212 is not yet complete (tail unread); the next firing transcribes.

## Transcription pp. 889–896 (PDF 911–918, 2026-11-26)
- **The passes write ه where the print has ة.** The adjudicator noticed it; a dedicated check of all ~274 word-final ه/ة on these pages against the crops restored 18 printed ة (هذة ×5, رآة, واراة, وواراة, جسدة, فجهّزة, امعاءة, واستاجرة, اشتهاة, واخذة, وجودة, ووعدوة, فاحبّوة, بلادة). In this type the two dots on an isolated ة are often fused into two small horns, which reads as a plain ه at a glance; P893L17 هذة has two clearly separate dots and still went past both passes and the adjudicator. Earlier archives have هذه 27 times against هذة once in pp. 865–888, so **earlier pages probably carry the same normalisation**. Not re-checked here (outside this batch). Decided meanwhile: publishing runs should treat a final ه on a pronoun as possibly a printed ة (it does not change the reading). A later run could re-check old archives with the same dot test, and future transcribing runs should keep the dot check as a step.
- Kept as printed, for publishing: P890L06 واها (no lam/nūn, likely misprint for وانها; doubtful); P890L15 verse وَتُعَلِّبُوْا (lam for dhāl, misprint for وتعذّبوا); P891L19 verse اَرَاهَمْ (fatha for damma); P891L18 verse عَيَنِيْ and فَاَدْمَعُهَا; P896L22 verse انَشَدَ (fatha shifted from alif); spacing قمرا لزمان P891L21, تا توابه P894L16, اوحدث P891L13, ومرّبه P889L18.
- Join 895→896: "كل ذلك | قمر الزمان" — a و (وقمر) seems not to have inked in the indent; kept as printed.
- Night labels 213–216 all read الليلة (P892L15 passes had الميلة; the lam-lam ligature looks like a mim; adjudicator and dot check both read الليلة).
- Nothing waits on the owner. Nights 212–215 are complete and unpublished; the next firings publish them.

## Night 212 (P887L04–P889L05, published 2026-11-26)
- Library label: `Night 212 · Qamar al-Zamān, continued`.
- Misprint corrected (emend.json): P887L06 على → عدى ("علم انه عدى عليه وافترسه اما وحش واما قاطع طريق"). The transcribing run had called it doubtful; decided here that the sense allows only عدى (one letter, ل for د). Reversible by deleting the emend entry if the owner disagrees.
- Kept as printed, with notes: run-together السعيدان and ولوفى; جدر شجرة (probably for جذر, "stump"; not certain); والدة read wālidahu "his father" with ة for ـه (as in earlier nights; the glossary key وَالِدَةُ now carries both "mother" and this sense); فبطته (loose agreement); تسير المركب (fem. verb); verse اِنِّيْ after اَعْلَمُ, تَنَالُهُمْ indicative after an imperative, يَوْمَ acc. twice in P887L12.
- Nothing to decide. Nights 213–215 are complete and unpublished; the next firings publish them.

## Night 213 (P889L06–P890L02, published 2026-11-26)
- Library label: `Night 213 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json), all ة for ه, as in earlier nights: P889L11 امعاءة → امعاءه, P889L12 جلدة → جلده, P889L15 فوجدة → فوجده, P889L16 رآة → رآه, P889L17 هذة → هذه.
- Kept as printed, with notes: جدرها read jidr "root, stump" (probably for جذر; as in Night 212, not certain); الفاس pointed al-faʾs; شيأ, فدنى, فاتي, علي, فى spellings; ومرّبه set as one word (wa-marra bihi); طابقا read ṭābaq "trapdoor" (least certain word of the night); the opening recap has ووالده joined to firāq ("parting from his wife and his father") where Night 212 had him remember his father.
- Nothing to decide. Nights 214–215 are complete and unpublished; the next firings publish them.

## Night 214 (P890L03–P892L14, published 2026-11-26)
- Library label: `Night 214 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P890L06 وهذة → وهذه; P890L15 verse وتعلبوا → وتعذبوا (ل for ذ); P891L02 واراة → واراه; P892L09 جسدة → جسده, فجهّزة → فجهّزه, وواراة → وواراه; P892L10 تم → ثم.
- Kept as printed, with notes: P890L06 واها read as the exclamation wāhan "ah, how fine!" (likely a slip for ولها "and it has", not certain — reversible by an emend entry if the owner prefers); verse اَرَاهَمْ, عَيَنِيْ, فَاَدْمَعُهَا, الرَّبُوْعُ, وَسَاكِنِيْهَا, تَجَلُّديْ as pointed; spacing قمرا لزمان, فياترى, اوحدث, لايردّ; حيوٰته with dagger alif; مطر/امطار glossed as jars; ولبّس عليهم read "covered them over" (possibly "disguised it from them"; noted).
- Nothing to decide. Night 215 is complete and unpublished; the next firing publishes it.

## Night 215 (P892L15–P894L05, published 2026-11-26)
- Library label: `Night 215 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json), all ة for ه as in earlier nights: P892L17 واستاجرة → واستاجره, P893L07 هذة → هذه, P893L14 اشتهاة → اشتهاه, P893L17 هذة → هذه, P894L03 واخذة → واخذه.
- Kept as printed, with notes: المركب feminine throughout (سافرت, هذه المركب) with masculine طاب الريح; solid لاسيما and ماله (mā lahu); ما هذا الّا ذهبا with accusative; ملآنة for Classical malʾā; العصافيرى with ى; حياة النفوس spelled here with ا (not حيوٰة). Doubtful vowels flagged in notes: القاقلي (qāqullī), كوم (kawm/kūm), دكة (dikka), الشيل (shayl).
- Shared glossary entries corrected deliberately (not appended): الشَّجَرِ ('of the tree' → 'of the trees', collective), مَلْآنَةً (agreement explained), مَالَهُ (mā-negation of a nominal clause is Classical, not Middle Arabic), كَوْمُ (old entry was a placeholder "same, nominative").
- Nothing to decide. Night 216 is not yet complete (tail unread); the next firing transcribes.

## Transcription pp. 897–904 (PDF 919–926, 2026-11-26)
- The ه/ة dot check (kept as a step, per the entry for pp. 889–896) restored 13 endings: هذة ×6 (P897L02 ×2, P899L05, P899L21, P901L04, P904L05), بيدة P900L04 and بنورة P901L06 (medium: pronoun endings with the two horns), and final ي for ى in تخشي P897L05, العلي P899L18, الي P899L22/P904L21 (medium: smeared dots), ونسي P902L19. The adjudicator had read تخشى/العلى/ونسى undotted; the run looked at the three crops and the dots are clear, so the dot check stands. P899L18 العلي: the لي ligature looks like لمي (OCR and one pass read العلمي); the formula لا حول ولا قوة الا بالله العلي العظيم and two readers give العلي.
- P904L06 العاشقه, المفارقه are printed with plain ه (no dots), unlike the ة elsewhere on the page — kept as printed.
- diff_passes.py misaligned p920 (all verse, six short "وقول الآخر" lines): both passes had the same 22 lines in order, but it reported phantom MISSING LINE disputes. The adjudicator gave "" for those and three fixes (الآخر, اِلى ×2) were made by hand in pass1.json. Decided meanwhile: nothing to change; a verse page with many short identical lines can confuse the aligner, so read its disputes before applying.
- Kept as printed, for publishing: P902L12 الافراج (sense wants الافراح; ج dot clear); P902L08 نرضاة and P902L19 اباة (printed ة on a pronoun); P902L17 زوجته where the sense wants زوجتيه; P899L11 هيّأتنا (sense: سيّئاتنا).
- Volume 1 has 6 pages left (PDF 927–932); the next transcribing batch is short by the runbook and the one after starts at PDF 936 (vol. 2). Nights 216–217 are complete and unpublished; the next firings publish them. Nothing waits on the owner.

## Night 216 (P894L06–P901L18, published 2026-11-26)
- Library label: `Night 216 · Qamar al-Zamān, continued`.
- **Two passages left out under §0a** (owner's ruling 2026-10-16), in omit.json and gaps.json, with the advisory "This night contains two passages, skipped for now, in which verses that Budūr recites describe sexual acts involving boys.": P897L10–P897L11 (a couplet narrating penetration of "the little one", al-ṣaghīr) and P898L04–P898L09 (the heading وقول الآخر and two pieces preferring beardless boys to women, one describing positions). The owner can supply them from add-passage.html.
- **Decided meanwhile, reversible:** the main scene is translated in full. Budūr, posing as the king, argues that Qamar al-Zamān is "one of the little children" and below the age of legal responsibility, but he is her grown husband and the act is between them; the remaining bawdy verses are about women, or are not explicit (the Lot couplet P896L16, P898L02–03), and were kept. If the owner wants the boundary drawn wider, widen the omit ranges.
- Misprints corrected (emend.json): ة→ه ×17 (وجوده, ووعدوه, هذه ×8, بهذه, فاحبّوه, نفسه, بلاده, يده, وفوأده, بيده, بنوره); P895L08 رأنه → رأته; P895L04 ولياني → وليالي; P897L13 النساو → النساء.
- Kept as printed, with notes: P896L22 verse انَشَدَ (metre wants فأنشد); P899L11 هيّأتنا (sense سيّئاتنا); P899L12 اجادوا حسن (spacing for أجاد وأحسن); P899L16 بينهما وبينه; P896L10 للاختيار read ikhtiyār "elder" (doubtful); verse آمن الارهاص (P900L14) obscure.
- Review fixed one misreading: P899L22–P900L01 لعلّه ينتصب refers to "the familiar (thing)" Budūr pretends to have, not to Qamar al-Zamān's member.
- Nothing waits on the owner. Night 217 is complete and unpublished; the next firing publishes it.

## Night 217 (P901L19–P903L19, published 2026-11-27)
- Library label: `Night 217 · Qamar al-Zamān, continued` (the princes al-Amjad and al-Asʿad enter here, but the print gives no new tale heading, so the label stays on Qamar al-Zamān).
- Misprints corrected (emend.json): P902L08 نرضاة → نرضاه; P902L12 الافراج → الافراح (the transcription kept ج as printed; the sense allows only الافراح, "the wedding festivities", so it is corrected under the 2026-11-06 rule); P902L19 اباة → اباه.
- Kept as printed, with a note: P902L17 زوجته (the sense wants زوجتيه "his two wives", as منهما on the next line shows; doubtful, so not corrected; the idiomatic layer reads "his wives"). Spacing السعيدان, لماصار, ماكان, ولانخرج kept.
- Nothing waits on the owner. Night 218 is not yet complete (tail unread); the next firing transcribes (PDF 927–932, the last six pages of volume 1).

## Transcription pp. 905–910 (PDF 927–932, 2026-11-27): end of volume 1
- **Volume 1 is fully transcribed.** The batch was short by the runbook (it may not cross PDF 932). P909L06 "وبقيّة حكاية الامجد والاسعد فى الربع الثاني" ("the rest of the tale of al-Amjad and al-Asʿad is in the second quarter") is marked h; P909L07–P910L21 are the editor's colophon in rhymed prose, transcribed as body lines with the print's `*` separators (the small printed circle on P910L17 is also written `*`). Night 219 (heading P905L01) runs on into volume 2, so it shows as "tail unread" until the next transcribing run reaches PDF 936 onward. Decided meanwhile: a publishing run should not take the colophon (P909L07–P910L21) as part of Night 219's story text; it is the editor's afterword. How (or whether) to present it to readers is the owner's call. Nothing waits on it.
- Header check: PDF 930's page number has a broken ٨ that reads like ٥ (both passes reported "905"); the run of headers 903–910 across PDF 925–932 confirms it is p. 908.
- Dot check (adjudicator): 9 endings restored to ة. Judgement call left as pass 1 read it: on P908 the endings of اخوه, اخبره, واخبره, قصره are a rounder ه with one knob, read as plain ه (the archive has قصره 21×, قصرة 0×).
- Kept as printed, for publishing: P906L05 قوب (sense قرب), P906L17 برضيك (sense يرضيك), P909L18 النضائل (sense الفضائل), P908L20 القيضة (sense القضية), P909L04 بالبكا وايضا; spacing بماجرى, ماجرى, لاغروان, سهومن. P910L12 وشيء: one pass wrote ئ; the adjudicator saw a dotted ي and a separate hamza.
- Night 218 is complete and unpublished; the next firing publishes it. Nothing waits on the owner.

## Night 218 (P903L20–P904L21, published 2026-11-27)
- Library label: `Night 218 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P904L05 هذة → هذه; P904L09 اجدة → اجده; P904L11 حصرة → حصره.
- Decided meanwhile, reversible: P904L11 وعجزت عن حصره الحساب is pointed الْحُسَّابُ, "the reckoners" (a broken plural, so the feminine verb agrees), rather than الْحِسَابُ, which would leave the feminine verb unexplained; the note says the reading is ours. العاشقه, المفارقه (ه for ة) kept as printed and pointed pausal (-ah).
- Next: Night 219 runs on into volume 2 and is not complete; the next firing transcribes (PDF 936 onward). Nothing waits on the owner.

## Transcription pp. 914–921 (PDF 936–943, vol. 2 pp. 4–11, 2026-11-27): first volume-2 batch
- **The opening of Night 220 is not in the scan.** Volume 1's story ends cleanly with Night 219 at P909L05 (وادرك شهرزاد الصباح فسكتت عن الكلام المباح), followed by the "rest of the tale is in the second quarter" heading (P909L06) and the editor's colophon. In volume 2's only scan, the title page (PDF 933), a placeholder for its blank verso (934) and the half-title الربع الثاني (935) come before p. 4 (PDF 936, header ٤), and p. 4 opens mid-sentence: مشهور في يدة والدم يقطر من مناخيرة… (Qamar al-Zamān standing with his sword drawn, King Armānūs asking what is wrong). So the Night 220 formula and the start of that night are missing: the king's return and the accusation against al-Amjad and al-Asʿad, probably no more than a page. Either the title and half-title are unnumbered and text pp. 1–3 are missing, or p. 3 held text the scan lacks. pagemap.json is not changed: the numbering from p. 4 on is right either way.
- **Decided meanwhile (reversible):** `tools/nights_index.py` now has `LOST_OPENINGS = {"P914L01": 220}`, so Night 220 runs P914L01–P915L15 and starts mid-sentence. It also has `NOT_STORY`, so Night 219 ends at P909L05 and the colophon (P909L06–P910L21) belongs to no night. Without these, `--next` would have offered Night 219 as P905L01–P915L15, folding in the colophon and the surviving part of Night 220, and would have numbered every later night one too low. Nights 1–218 index exactly as before. A publishing run should publish Night 220 as it survives, with a gap entry for the lost opening (README rule 7), so the owner can fill it from another copy of the 1839 print if one turns up. **Owner:** if you can get a scan of Calcutta II vol. 2 pp. 1–4, the opening can be restored.
- `tools/validate_archive.py` now accepts a jump over the excluded PDF pages (vol. 2 title leaves = archive pp. 911–913), as it already did over missing pages. Before this it failed every archive that followed p. 910.
- Night labels 221–225 (P915L16, P917L04, P918L16, P920L03, P921L10) are each printed centred on a line of their own in larger type and are marked h. On P915L16, المائتين sits below the baseline, which made one pass take it as two lines.
- Volume 2's type sets shaddas on prose words much more often than volume 1's (validator WARNs on most pages); both passes agree on them, so they are kept as printed. The dot check restored 16 final ة (يدة, مناخيرة, فاخبرة, صهرة, خازندارة, لامرة, قدّرة, صدرة, خدّة, وراءة, اولادة ×3, ولدة ×2, حزناة), plus فِى ×2 in the P917L01 verse. As in recent volume-1 batches, هذه was not changed: the adjudicator could not reliably tell its ending from a plain ه.
- Third readings by the adjudicator: P917L01 فَهُنَّ (both passes had فَمِنْ), P917L20 كُحَلُ, P918L20 فعَلاَ, P919L05 مشوُمة (a damma, not a hamza, over the waw). Spacing kept as printed: السعيدان, اريدان, لانروح, ياليتنا, وثاروامّا.
- Nights 219–224 are complete and unpublished; the next firings publish them. Nothing waits on the owner.

## Night 219 (P905L01–P909L05, published 2026-11-27)
- Library label: `Night 219 · Qamar al-Zamān, continued`. Last night of volume 1; the colophon (P909L06–P910L21) is not part of it, as decided at transcription.
- Misprints corrected (emend.json): ة→ه ×9 (هذه ×5, غمده, انهاه, يده ×2); P906L05 قوب → قرب; P906L17 برضيك → يرضيك; P908L20 القيضة → القضية.
- Kept as printed, with notes: P906L01 split وقدا صبحت (wa-qad aṣbaḥat); P908L14 يصيرتا (doubtful; perhaps تصيرا), vocalised as printed; P906L11 ودلّ (ذلّ possible); P907L08 verse كَيْلَا يُصِيبُكَ (indicative); جري, حكي, بالحيوة, بالبكا, بن without alif.
- Decided meanwhile: shared-glossary senses that clashed with this night were appended, never replaced. The reviewer notes that the existing key اللّٰهُ claims the dagger alif is the edition's own mark, which is not so where the print has bare الله; this night no longer uses that key, and it was left unchanged.
- Nothing waits on the owner. Night 220 (lost opening, see the transcription entry above) is next; nights 220–224 are complete and unpublished.

## Night 220 (P914L01–P915L15, published 2026-11-27)
- Library label: `Night 220 · Qamar al-Zamān, continued`. First night of volume 2.
- **Lost opening, marked as a gap.** The night's formula and the start of its first scene are not in the scan (see the transcription entry for pp. 914–921). The first sense unit starts mid-sentence (مشهور في يده…), its `l`/`i` open with "[…]", its note says the beginning is skipped for now, and it carries `"gap": "Opening of Night 220 (before P914L01): not in the scan"`, with a matching entry in the root `gaps.json`. **Owner:** `reader.html` shows an owner insert *after* the unit that carries the gap, so if you supply the opening through `add-passage.html` it will currently appear after the first sentence, not before it. Placing it before needs a small reader change (e.g. a `gapBefore` flag), which a run may not make. Nothing else waits on this.
- Misprints corrected (emend.json): ة→ه ×7 (يده, مناخيره, فاخبره, صهره, خازنداره, لامره, قدّره).
- Kept as printed, with notes: P915L11 لاتجزعني (pointed lā tujazziʿnī, "do not make me grieve"; لاتجرعني, "do not make me swallow", is one dot away and fits غصة/تسقني better, so doubtful, not corrected); P914L15 واخرج لهما (sense بهما, "take them out"); قنانيتين (dual of a later qanāniya, "flask"); ودعى, يا ولداي, ياسيداي, يهنّياه, صابرون after a dual subject.
- Review suggestion not taken: reordering the existing shared key فِعْلًا (existing entries are only appended to).
- Nights 221–224 are complete and unpublished; the next firing publishes Night 221. Nothing waits on the owner.

## Night 221 (P915L16–P917L03, published 2026-11-27)
- Library label: `Night 221 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P916L04 صدرة → صدره; P917L02 ما تريد منك → ما نريد منك (one dot; al-Amjad speaks for both brothers, as مالنا before shows).
- Kept as printed, with notes: هذه كلّه; اخى; فبكي; يا سيداي; ما يقتل قبل الا انا; ولاتدعهما (dual with no clear antecedent; تدعها, 'leave it' (the fire), expected; doubtful, not corrected); spacing ماجرى, ولاقوة, مالنا.
- Decided meanwhile, reversible: P916L20 انشده is read as narrative (anshadahu, al-Amjad recites to the treasurer); the imperative anshidhu, still inside his instructions, is equally possible and the note says so.
- Review suggestion not taken: rewording the existing shared key الْأَسْعَدَ ('in apposition after inna' — it is the noun of inna); existing entries are only appended to.
- Nights 222–224 are complete and unpublished; the next firing publishes Night 222. Nothing waits on the owner.

## Night 222 (P917L04–P918L15, published 2026-11-27)
- Library label: `Night 222 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P917L05 ما تريد منك → ما نريد منك (as at P917L02 the night before); ة→ه ×3 (خدّه, شعره, يده); P918L06 verse مُزْدَةٍ → مُزْدَهٍ (muzdahin, 'puffed up'; مزدة gives no word).
- Kept as printed, with notes: السعيدان (al-saʿīdu anna run together); verse تَفْجَا and الثَّار without hamza; P917L20 كُحَلُ (read as kuḥl with a metrical vowel; kaḥal, the natural dark rim of the eyelids, offered as the alternative); P918L07 وَتَرَتْ read as watarat with no joining 'and', its force flagged as uncertain; P917L09–10 printed without hemistich breaks.
- Decided meanwhile, reversible: P918L01 ذَنْبِي اِلَى الدَّهْرِ read as a topic with ذَنْبَ الْحُسَامِ as object of فَلْيَكْرَهْ; P917L19 اللَّيَالِي read al-layāliya (accusative, as the metre needs).
- Nights 223–224 are complete and unpublished; the next firing publishes Night 223. Nothing waits on the owner.

## Night 223 (P918L16–P920L02, published 2026-11-27)
- Library label: `Night 223 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): ة→ه ×5 (فؤاده P918L18, وراءه P918L19 and P919L08, خبره P919L13, سيده P919L22, 'his master's two sons').
- Kept as printed, with notes: run-together السعيدان, وثاروامّا, ماحصل, ياليتنا, لانروح, ماجرى, لاحول ولاقوة; فعَلاَ with the print's fatḥa on the lām-alif; مشوُمة (pointed مَشُوُمَةٌ, mashūma for mashʾūma, as the shared keys مَشُومَة have it; Night 47 pointed the masculine مَشْوُمُ); اريح; mukattafīna plural for the two brothers.
- Decided meanwhile, reversible: P919L10 كان read as ka-anna ('as though'), with kāna given as the alternative; P919L23 واقفين read as the dual wāqifayni (plural possible, noted).
- Nights 224 is complete and unpublished; the next firing publishes it. Nothing waits on the owner.

## Night 224 (P920L03–P921L09, published 2026-11-27)
- Library label: `Night 224 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): ة→ه ×2 (اولاده P920L20, 'his sons'; P921L09, 'his sons' clothes').
- Kept as printed, with notes: P921L07 قتُلا, whose printed ḍamma sits on the tāʾ (the passive is qutilā). The rule keeps printed prose marks, so `t` shows قُتُلَا while `tr` gives qutilā, and the audio may say "qutulā". **Owner:** should a mark the print sets in the wrong place be corrected the way a misprinted letter is? For now it is kept. Also kept: P921L01 وقد قال لي, a singular verb for the two brothers (one brother speaking for both, or a dropped dual alif; flagged as doubtful); قنانيتين (pointed as qanānītayni, a guess); verse اِصْلُ (read aṣlu); حاشى; and the run-together السعيدان, اريدان, ياسيداي.
- Review suggestions not taken: rewording the existing shared keys الْأَسَدِ ("here Sharkān", left over from an earlier night) and الْخَازِنْدَارِ ("gen. after ʿalā"). Existing entries are only appended to.
- Night 225 is not complete yet (its tail is still to be transcribed); the next firing transcribes. Nothing waits on the owner.

## Transcription pp. 922–929 (PDF 944–951, 2026-11-27)
- **Night 226's label is misprinted اليلة** (P923L03, "فلما كانت اليلة السادسة والعشرون بعد المائتين"; one lam). Archived as printed. `tools/nights_index.py` did not see it and reported an ordinal MISMATCH for nights 226–229; it now accepts اليلة in the night formula, like the earlier اللية/الميلة cases, and the table reads 225–230 in order. The publishing run should correct the label to الليلة under the misprint rule and record it in emend.json.
- Night labels on their own centred line are marked `h` (house convention from earlier archives); wave-1 passes had left them unflagged, and the run set the flag before the diff.
- PDF 950 (p. 928): the detector merged the 15-line verse block into 8 crops; both passes and the adjudicator built the lines from the bands, and the line count (20) was checked against them. PDF 949: two lines with no crop (P927L04 وقول الآخر, P927L18 هذه الابيات) were recovered from the bands.
- The apply step wrote a doubled sukun (اَحْبَابِيْْ) at P928L01 where the verdict had one; corrected to the verdict by hand.
- Kept as printed, possibly misprints, for the publishing run: P924L13 الصوق (for السوق; the same page prints السوق at L19), P925L23 حظت (for حطت, "she set down"; a dot is beside the ط), P925L11 مجتعون (for مجتمعون), P925L07 ينتظرلي (perhaps ينتظرني; not confirmed on the image), P929L19 يملّيه (could be a heavily inked يسلّيه).
- Volume 2's type keeps setting shaddas on prose words (59 gate WARNs, against 65 in the last batch); both passes agree on them, so they are kept.
- Next batch: PDF 954–961 (PDF 952–953 = vol. 2 pp. 20–21 are missing from the scan). Nothing waits on the owner.

## Night 225 (P921L10–P923L02, published 2026-11-27)
- Library label: `Night 225 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): ة→ه ×5 (اولاده and ولده P921L12, ولده P921L14, حزناه P921L19, امره P922L14).
- Kept as printed, with notes: in the first poem, يَمُسَّ (P922L02; one syllable too many and hard sense, probably يَمِسْ "sway", which the idiomatic layer follows) and مَعَاطِفَ (the metre wants tanwīn); the first half of P922L04 and the second half of P922L08 do not scan cleanly; اِعْزِزْ (P922L10), where the print's kasra stands for the fatḥa of the verb of wonder; مُتَسَاوِيهِ (P922L10, no clear grammar; translated as "where the base and the noble lie as equals"); وا ولداه, "alas my son", in the singular for two sons. Also kept: وترامي, واشتكي, اعلا and the run-together السعيدان, لاحول ولاقوة.
- Nights 226–229 are complete and unpublished; the next firing publishes Night 226 and should correct its misprinted label اليلة (P923L03) through emend.json. Nothing waits on the owner.

## Night 226 (published 2026-11-28, unattended)

- Corrected as misprints (emend.json): P923L03 اليلة → الليلة (night label); P924L13 الصوق → السوق (ص for س; the same page prints السوق at L19). Treated as a misprint rather than a spelling habit because the edition spells the word with س everywhere else; if the owner prefers صوق kept as a Middle Arabic spelling, drop the emend entry and restore the note.
- Kept as printed, vocalised by sense and noted: مدّ روحك (read as a colloquial "hold out, be patient"; uncertain), محراب (read as a small oratory in the wild), عين ماء يجري (masculine verb), هو واياه, اولاد of two brothers, حسبت الف حساب (ḥasabtu), لِحفه (liḥf, foot of the mountain), المدينه vocalised الْمَدِينَهِ.
- Transliteration of لله: house usage is split (li-llāhi in the pilot and Nights 216, 221; li-Allāhi in Night 224). This night follows the "al- never elided" rule and writes li-Allāhi. Decided meanwhile; a ruling would let a later attended pass make it uniform.
- The reviewer noted some weak older glossary entries (e.g. مُدَّ glossed first as passive, نَصِلُ as "continue"); senses were appended, not rewritten. Candidates for a deliberate glossary sweep.

## Night 227 (published 2026-11-28, unattended)
- Library label: `Night 227 · Qamar al-Zamān, continued`.
- Misprints corrected (emend.json): P925L11 مجتعون → مجتمعون (dropped م); P925L23 حظت → حطت ("she set down").
- Kept as printed, vocalised by sense and noted as doubtful: P925L07 ينتظرلي (colloquial "waiting for me" with li-, or a misprint for ينتظرني); P926L01 فاستغلق (translated in the sense of فاستفاق "he came to"; uncertain whether misprint or unrecorded usage); فادار كتاف الاسعد (read as kitāf, the pinion-rope); غمي عليه (ghumiya).
- The note on the black slave Ghaḍbān's description (unit 20) states plainly that this is the Nights' stock portrait pairing blackness with ugliness. Decided meanwhile; the owner may prefer a different wording.
- Existing glossary entry وَاقْشَعَرَّ said "quadriliteral form IX"; corrected to Form IV deliberately.
- Nights 228 and 229 are complete and unpublished; the next firing publishes Night 228. Nothing waits on the owner.

## Night 228 (published 2026-11-28, unattended)
- Library label: `Night 228 · Qamar al-Zamān, continued`.
- No misprints corrected. Printed verse marks kept and noted: وَرَبُّمَا (P927L07, vowels transposed; transliterated as the intended rubbamā, the note says so), لَعَلَّ اللهُ (P926L13, damma where Classical wants Allāha), sukūn on long vowels (جَارُوْا etc.), اِلَهِي without its long ā.
- Kept as printed, read by sense: P926L15 خلته as khallatahu "his need"; P927L09 وَابْشِرْ as abshir with hamza dropped (metre needs wa-bshir).
- Night 229 is complete and unpublished; the next firing publishes it. Nothing waits on the owner.
