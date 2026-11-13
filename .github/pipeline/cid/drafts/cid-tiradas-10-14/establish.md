# Establish — cid-tiradas-10-14: tiradas 10–14, lines 174–241

Starting draft: source/ocr/cid-tiradas-10-14.txt (OCR text layer, mechanically cleaned; line labels and tirada
breaks already checked by eye on 2026-10-12 — keep them unless the image plainly shows otherwise, and say so
in LOG.md if you change one). Page images: source/raw/pidal1923_text.pdf, PDF pages 140–145
(printed page = PDF page − 4).

Flags on this part (from the structural check): wholly italic restored line(s): 181b, 181c, 181d

Procedure — the image is the authority for every letter:
1. Render each page with pymupdf (`pip install pymupdf` if needed) at zoom 1.3–1.5, cropped between the
   printed rule under the running head and the rule above Pidal's footnotes (footnotes are smaller type,
   each beginning with a line number — never verse). Then read strips of about 8 lines at zoom 2.
2. Correct every line letter by letter against the image. Known OCR faults: ç read as q, £, (J or c;
   an accent added to Pidal's unaccented "mio" (OCR "mió"); accents lost or added; rn→m, e→c; spaces
   inside words; a line number stuck to the first word; the overflow of a long line printed on the next
   line after "[" — put it back at the end of its own line; words dropped at line end.
3. Italics are Pidal's restorations and the OCR never shows them: look for them on every line. Letter- or
   word-level italics become [brackets] (entróv[e], R[o]y, [Burgos]); a wholly italic line is printed plain
   and keeps the marker "	[ITALIC LINE]" after its text (the drafter flags it in the note).
4. Quotation marks: keep a single opening “ and closing ” per speech; drop the repeated quote Pidal sets at
   the start of every line inside a speech. No inverted ¡ ¿ unless Pidal prints them.
5. Leave out Pidal's prose restorations of the lost folios (lines marked PROSE): the poem does not have
   them; the drafter's note says what is lost and what Pidal supplies from the chronicle.
6. Write source/established/cid-tiradas-10-14.txt in the same layout as the draft: "## tirada N" lines, then one
   verse per line as "<label>\t<text>" in Pidal's PRINT order (he sometimes moves lines but keeps their
   numbers — keep his order and his numbers).
7. `python3 ../run3/r3.py pin cid cid-tiradas-10-14` checks it (every label of the draft present, in order; no OCR
   junk characters; brackets balanced) and pins it. Record in LOG.md how many lines you corrected and any
   reading you were unsure of; put a genuinely unreadable spot in QUESTIONS.md and mark it in the text with
   the OCR reading and a trailing "\t[UNSURE]".
