# Conventions — Alf Layla wa-Layla, Calcutta II transcription

*Editorial rules for the transcription phase. The translation phase, when it comes, adds the
language and reader conventions recorded in the project doc `arabic-nights-conventions.md`.*

## The edition

William Hay Macnaghten, ed., *The Alif Laila, or Book of the Thousand Nights and One Night*,
vol. 1, Calcutta 1839 ("Calcutta II"). Public domain. The scan is archive.org
`aliflailaorbooko01macn`, 300 ppi, 938 PDF pages; the Arabic text begins at PDF page 19 =
printed page 1, so **printed page = PDF page − 18** up to PDF page 47 — the scan then carries two
duplicate leaves (PDF 48–49 repeat printed pp. 28–29), so **from PDF page 50 on, printed page =
PDF page − 20**; read each page's own printed header number rather than trusting either formula
(see QUESTIONS.md, 2026-09-17). The archive.org OCR is unusable; the page
images are the only source. Every printed edition of the Nights is the late Egyptian recension
(ZER), not a medieval text; that is stated to the reader in the translation phase, not here.

## What the archive is

A page-referenced record of exactly what is printed: `{"ref": "P<pp>L<ll>", "t": "…"}` per
printed body line, printed page and line numbers, so any word can be traced to the scan. Flags:
`"v": true` for a verse line, `"h": true` for a section heading. It is a photograph in letters.
Nothing is normalised, repaired, vocalised or emended.

## Transcription rules (the same ones every prompt states)

- **Prose is the bare rasm, plus whatever mark the print itself puts there.** The edition prints
  its prose essentially unpointed, so almost every prose line has no vowel marks, no sukūn, no
  shadda, no tanwīn. But now and then it does set a mark on a prose word (a shadda on عليّ or
  وسّطها, a damma or kasra on a short word), and **those are transcribed as printed** — the owner's
  ruling of 2026-10-04: the archive records every mark the print has. A mark on a prose word is
  kept only when it is unmistakable on the image; a faint or doubtful one goes to the adjudicator
  like any other dispute, and ink noise is not a mark. (Until 2026-10-04 the rule stripped every
  mark from prose; the words so stripped are listed in QUESTIONS.md for a transcribing run to
  restore from the images.) The gate warns on marked prose words so the run can confirm each one.
- **Verse is transcribed with its printed marks.** Calcutta II points its verse. Two hemistichs
  per line, right one first, separated by ` * `. Marks are recorded as printed even where faint;
  a doubtful mark goes to the adjudicator, not to a guess.
- **Hamza and madda only where printed.** Bare alif is written `ا` even where modern spelling
  has `أ`/`إ` (`اراك`, `راى`, `امراة`). `أ إ آ ئ ؤ` only where the mark is visible on the page.
  The edition does print them sometimes (`وجئت`, `رآه`, `الآن`), so look at the mark.
- **Copy the dots.** `ة`/`ه` and `ى`/`ي` exactly as printed: the edition writes `اخوة` "his
  brother", `وحدة` "alone", `رآة` "he saw him"; `قل` for `قال` throughout; `عندك` where the sense
  wants `عندي`. These are the text.
- **Spacing as printed.** A prefixed `و` is attached (`وكان`). Kashida inside a word is not a
  space. Where the print runs two words together ambiguously, follow the ink; the adjudicator
  decides the disputes.
- **Punctuation and furniture.** Keep the edition's `( )`. An end-of-line filler rule is
  written `—`. The running header (tale title and page number) and the catchword under the
  last line are not body lines and are not transcribed. A section heading (`حكاية التاجر
  والجني`) is its own line, `h`. A night label (`الليلة الاولى`) is printed inline at the head
  of a prose line in larger type and stays inside that line.
- **Never repair.** This is Middle Arabic, printed by a nineteenth-century Calcutta press.
  Irregular forms are readings, not errors.

## Why two passes and an adjudicator

Measured on the first ten pages (September 16, 2026): a single correction pass reaches about
99 % of characters and 94 % of words against an adjudicated text, and its residue is not random —
both passes tend to add hamza where the print has bare alif, write `اخوه` for the printed
`اخوة`, and "fix" `عندك`. Two independent passes disagree about four times a page; the
adjudicator decides those from the images and reads every page join. The same control run
found that the pilot's double-blind text had a wrong word (`ورجعت` for the printed `وجئت`), so
the process is at least as good as what it replaced, at a fifth of the cost.

## Cost (measured)

Per page, all in: ~80k tokens per pass × 2, plus ~20k adjudication ≈ **170k**. Eight pages a
run ≈ 1.4M; two runs a night ≈ 2.8M; vol. 1 (908 pages remaining) ≈ 114 runs ≈ two months.

## Freeze-and-ask

Write it in `QUESTIONS.md` and carry on with the rest of the batch when: a line is illegible
after magnification (record it as `[illegible]` in `t` with a note in the LOG — never guess); a
page join cannot be made to read and the missing text cannot be found in the bands; the scan has
a missing or duplicated page. Stop the run only if the source chunk itself will not open.
