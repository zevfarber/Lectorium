# Establish — mabinogi-006: Branwen's starling and the house in Ireland (Second Branch: Branwen)

Evans cols 47–55, PDF pages 56–60 of source/raw/evans1907.pdf (column c is on PDF page
(c+65)//2; odd columns on the left). Opens: «Dilit ymdidan awnaethant y nos honno tra uu da ganthunt» — closes: «ac yd ystynnwyt y urenhinaeth yr mab.».
Inputs: source/drafts/mabinogi-006-ocr.txt (Evans's OCR, his lines), source/drafts/mabinogi-006-witness.txt (the
second witness, cy.wikisource — NOT the edition, never adopted without the image), source/drafts/mabinogi-006-diffs.txt
(the worklist: 27 'check' items and 17 'loss' items to look at;
168 'glyph' items are known misreadings of Evans's special letters, settled without the image).
Issues found on 2026-10-12: Col 54 lines 15–16 (PDF p. 59): short line 'adaw hwnnw adodi' and a space in 'y law ar un [space] arall' – manuscript layout (scribe writing round a flaw); the witness has no extra words. Not a defect; print continuously.

Procedure (as for mabinogi-001; the image decides):
1. For every 'check' and 'loss' item, render a crop of the column (±2 lines, 220–260 dpi; `python3 ../run3/page.py
   source/raw/evans1907.pdf <page> --zoom 3.2 --clip x0,y0,x1,y1`) and read Evans's letters. Also look at:
   the part's opening capital (P, B, G, M are large initials the OCR drops), every raised (inserted) letter, every
   blank space the scribe left, and every witness word missing from the OCR. Log each decision in
   drafts/mabinogi-006/establish-log.md.
2. Evans's special sorts, as the conventions render them: 6-shaped w → w; r-rotunda → r; dotted y → y; long s → s.
   Raised letters go into the line. Evans's underlines, accents, ' marks and * are dropped; line-end marks
   (= - ' ^ / » «) join the word, never read as letters.
3. White Book defects: where Evans shows a blank and the sense needs the Red Book's word(s), supply only what the
   sense needs and record it for the drafter's note (source/raw/rhys-evans1905_djvu.txt is the Red Book, a
   public-domain third witness). Phrases the second witness supplies from the Red Book that the sense does not
   need are NOT supplied. A scribal slip that is still readable stays as written.
4. Apply our word division (proclitics separated; fused forms with an apostrophe: a'y, y'r, o'r, i'th, a'm …),
   modern punctuation, capitals for sentence starts and proper names only, and “ ” around speech. Follow the
   practice of the published mabinogi-001 (source/mabinogi-001-established.txt is its established text).
5. Paragraphs: a new paragraph at each change of scene or speaker-exchange (ours), separated by a blank line.
6. Write source/established/mabinogi-006.txt and pin it: `python3 ../run3/r3.py pin mabinogi mabinogi-006` (it checks the
   text against the OCR letter by letter and refuses wholesale drift).
