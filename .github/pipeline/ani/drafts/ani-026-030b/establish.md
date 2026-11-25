# Establish — ani-026-030b: Spells 26 and 30B

Budge 1895, interlinear text, printed pp. 88–91 (PDF pages 252–255 of source/raw/budge1895.pdf; PDF page = printed page + 164).
Chapters expected here (from Budge's running heads and his Table of Chapters; first pass, confirm on the page): XXVI; XXX B
Plates: XV

Start: right after the last word established by ani-023-024: its end is p. 87, Plate XV, line 7, last word “śuit” (… otherwise said, fleeter than a shadow (?). (p. 87 row 4, Spell 24 l. 7: the end of Spell 24; below it Budge's “Appendix.” — Chapter XXV from the papyrus of Nebseni — is not Ani's text. The next part begins at p. 88 row 2, Chapter XXVI, after the end of that Appendix.)).
End: at the end of the chapter or section if it ends on your last page or in the first third of the page after it; otherwise at the last sentence-end on your last page. Never stop inside a sentence. Read on to the next page as far as that needs.
The page ranges in parts.json are a first pass from the running heads: the page itself decides. Record the pages you really used.

What belongs to the Papyrus of Ani, and what does not (conventions.md, "What is Ani's text"):
- IN: everything Budge prints as the papyrus's own text under a "PLATE n." heading, including chapter titles, rubrics and
  the words written beside the figures in the vignettes.
- OUT: every section headed "Appendix." (text supplied from Naville's Todtenbuch or other papyri) up to the next "PLATE"
  heading or the return to Ani's text; every footnote, including footnotes that print a "less corrupt" parallel text in
  hieroglyphs; words Budge sets in [square brackets] as his own restorations are kept, with "restored": true.
  List what you left out in "skipped" (pages and Budge's label).

Procedure — the printed page is the authority for every sign:
1. Render each page with PyMuPDF at zoom 2 (`python3 ../run3/page.py` or fitz directly), cropped to the text block; then read
   one printed row at a time at zoom 3–4. A row is three lines: hieroglyphs, Budge's transliteration, his English.
2. TWO independent readers (two subagents on the strongest model, neither sees the other's output) each write every word of
   every row: the signs as Gardiner codes in reading order, Budge's transliteration exactly as printed (his ā à χ θ ś t' etc.),
   his English, the page, the plate and the papyrus-line number in force (the small "1." "2." … numerals set inside the rows;
   a word before the first numeral of a plate belongs to line 1 unless the page says otherwise).
   Word division = Budge's own: one group over one transliteration group. A suffix he hyphenates (t'et - à) stays in its word.
3. Diff the two readings word by word (`python3 hooks.py diff A.json B.json`). For every difference a third reader looks at a
   tight crop of that word only and decides. Use Budge's transliteration as a check on every word: the phonetic signs must
   spell it (his system → signs: conventions.md, "Budge's transliteration"); a word whose signs cannot give his reading is
   re-read before it is accepted.
4. A sign with no Unicode character: take the nearest standard sign, list its code under "approx" for that word, and say what
   the type shows in "unsure". A sign you cannot identify at all: put "unsure" on the word with what you see; if more than
   3 words in the part are like that, block the smallest piece (rule 7 of ../README.md), not the part.
5. Layout: "q" records how Budge's type groups the signs of the word, by glyph index: "-" between groups set side by side,
   ":" between signs stacked top to bottom inside a group, "*" between signs side by side inside a stacked group
   (the layout notation of the published part). Omit "q" for a single sign or a plain left-to-right string.
6. Rubrics: Budge marks red-ink passages with a line over the signs. Set "rubric": true on those words.
7. Write source/established/ani-026-030b.json in the layout given at the top of hooks.py, with "start", "end" (page, plate, line,
   lastWord = Budge's transliteration of the last word, note = the last few words of his English) and "skipped".
8. `python3 ../run3/r3.py pin ani ani-026-030b` checks it and pins it. LOG.md: pages used, words, differences between the two
   readers and how many the third reader decided each way, signs marked approx/unsure, what was skipped.
