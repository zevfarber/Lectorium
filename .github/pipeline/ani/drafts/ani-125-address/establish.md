# Establish — ani-125-address: Spell 125 — the address to the gods (supplement: not on Ani's papyrus)

Budge 1895, interlinear text, printed pp. 203–213 (PDF pages 367–377 of source/raw/budge1895.pdf; PDF page = printed page + 164).
Chapters expected here (from Budge's running heads and his Table of Chapters; first pass, confirm on the page): [CXXV], the Appendix after the Confession — from Naville, Todtenbuch, Bd. I, Bll. 137, 138
Plates: none: the line numbers are those of Budge's Appendix (use plate "App.")

Start: the heading "Appendix." on p. 203, directly under the last declaration of the Confession: its first numbered line is 2, "ànet' ḥràu-θen neteru àpu" (Homage to you, O gods these). Footnote 1 on p. 203 names the source (Naville, Todtenbuch, Bd. I, Bll. 137, 138): copy it into "witness".
End: the last word of this Appendix, immediately before Ani's text resumes with the title of Spell 42 (about p. 212–213). Read every footnote on the way for what it says about the source papyri and put that in "witness" too.
The page ranges in parts.json are a first pass from the running heads: the page itself decides. Record the pages you really used.

THIS PART IS A SUPPLEMENT (owner's ruling, 2026-11-16). Its text is the Appendix section itself, which Ani's papyrus
does not have: for this part only, the rule below is turned round — the Appendix named under Start/End is IN, Ani's own
text before and after it is OUT, and footnotes stay OUT. Give every word "plate": "App." and the Appendix's own line
numbers. Add a top-level "witness" string to the established file: what Budge's footnotes say the text is taken from
(edition, plate numbers, and the papyrus if he names it), in one sentence.

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
7. Write source/established/ani-125-address.json in the layout given at the top of hooks.py, with "start", "end" (page, plate, line,
   lastWord = Budge's transliteration of the last word, note = the last few words of his English) and "skipped".
8. `python3 ../run3/r3.py pin ani ani-125-address` checks it and pins it. LOG.md: pages used, words, differences between the two
   readers and how many the third reader decided each way, signs marked approx/unsure, what was skipped.
