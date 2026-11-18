# Reader brief — ani-125-rubric (Budge 1895, Plate XXXIII, the rubric of Spell 125, pp. 222–224)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-125-rubric/readers/ other than
your own. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 222 = PDF 386, p. 223 = 387, p. 224 = 388). Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page; --info prints
the page size). Look at each row image with the Read tool. Your scratch directory: /tmp/claude-0/-home-user-Lectorium/54984d59-3841-5235-8c22-8d0fdafad7cb/scratchpad/<your-reader-id>/

## What to read
Under the heading "PLATE XXXIII." on p. 222: from line "1." àn Àusàr Ani maāχeru (See Osiris Ani, triumphant) through
all of p. 223 to p. 224, line 10, ending "ḥeḥ en sep" (millions of times), just above the short rule and the heading
"Appendix." Everything below that rule on p. 224 is OUT. On p. 222 the footnote (a "less corrupt text" from Naville,
printed in hieroglyphs with its own numerals 1.–4., below the long rule) is OUT. The footnotes on p. 223 ("Var." 1–4)
are OUT, but report every footnote's text (with what its superscript number is attached to) in your "footnotes" list.
Plate for every word: "XXXIII". Superscript footnote numbers (¹ ² ³ ⁴) next to signs are not signs.

A printed row is three lines: hieroglyphs, Budge's transliteration (italic), his English. Each transliteration group
sits under one group of signs = one word (Budge's own word division; a hyphenated suffix "un - nef" stays in its word).
Budge draws a horizontal line over signs written in red ink (rubric): most of this text is rubric — check every word.

## For every word write
{"page": 222, "plate": "XXXIII", "line": 1, "signs": ["M17","N35"], "q": "0:1", "budge": "àn", "gloss": "See"}
- line = the small bold numeral in force ("1." "2." … set inside the rows). A numeral applies from the word right after it.
- signs = Gardiner codes in reading order (left→right, top→bottom within a group). Every sign you see, including strokes
  (Z1, Z2 plural strokes, Z3 vertical three, Z4 dual strokes), determinatives and suffix figures.
- budge = his transliteration EXACTLY as printed, with his letters: à ā ī χ θ ś t' ṭ ḥ ḳ, hyphens with spaces as printed
  ("un - nef"), [ ] and "(sic)" as printed. gloss = his English words under it, as printed (best alignment).
- q = layout (omit for one sign or a plain left-to-right string): indices into signs; "-" between groups set side by side,
  ":" between signs stacked top-to-bottom inside a group, "*" between signs side by side inside a stacked group.
  e.g. ["D21","Z1"] with D21 above Z1 → "0:1"; ["G35","N29","D54"] with G35, then N29 above D54 → "0-1:2".
- "rubric": true if Budge draws a line over the signs (red ink). "restored": true if he sets the word or part in [ ] in the
  hieroglyph line — say which signs in "unsure" if partial.
- "approx": [codes] for a sign with no exact Gardiner/Unicode match (use the nearest standard code) + "unsure" describing it.
- "unsure": "<what you see>" whenever you are not sure of a sign. Never complete a word from its transliteration without
  seeing each sign; Budge's transliteration is a CHECK: the phonetic signs must spell it (his letters: à = reed M17;
  ā = arm D36; a = vulture G1; ī/i = double reed or strokes; u = quail chick G43 or coil Z7; χ = Aa1 or F32 (ẖ);
  θ = tether V13; t' = cobra I10 / D; ś = pool N37; ṭ = hand D46; ḳ = jar-stand W11; ḥ = twisted wick V28; h = shelter O4).
  If the signs cannot give his reading, look again.

## House rulings (from the established Spell 125 introduction — apply them)
- First-person suffix / seated-man determinative of a person: A1 (seated man) — code A1 unless the figure clearly is
  a different A-sign (e.g. A2 hand to mouth for speech/eat verbs, A30 adoring, A40 seated god).
- maā (mꜣꜥ) / maāχeru: U1 sickle + Aa11 plinth (closed). The preposition em written with the bevelled open sign: Aa15
  (em is often also the owl G17 — code what is printed).
- Abstract determinative = papyrus roll: Y1a when standing upright (tall rectangle, tie at side), Y1 when lying flat.
  Never N16 for it.
- Low flat sign (runner with upcurled left end, upright tab at right, no stick): U15.
- ī - nà "I come": M18 (reed with legs) + M17 … ; ṭā "give": D37 (forearm holding conical loaf).
- Four strokes under N35: Z2 + Z1. Sky under ḥeri: N1. ses: O34, N37, Z9, D54.
Common sign codes in this text: N35 water line (n); D21 mouth (r); X1 bread (t); I9 horned viper (f); V31 basket (k);
O34 bolt (s); S29 folded cloth (s); Q3 stool (p); N29 hill-slope (q); G17 owl (m); W24 pot (nw); V30 basket (nb);
R8 axe-flag (nṯr); D4 eye (ir); Q1 seat (st, as in Àusàr: Q1+D4+A40 or similar); D58 foot (b); E34 hare (wn);
G39 pintail (sꜣ); G38 goose; O1 house (pr); O49 town; N25 hills; Z2/Z3 plural strokes.

## Class rulings from the established Spell 125 address (apply only where the type shows the same shape)
The thin dashed vertical line after words is the stroke Z1; flat roll with tie Y1 vs hand D46 are distinct shapes
(t'eṭ = D46); trà M6; χer V12; ḳ = W11, χert = T28; the hatched low rectangle O31 (where that shape is printed; uat' "vegetables" here may be written otherwise — code what you see); tall loop for θ V13;
the owl-over-arm ligature read mā is G17 + D36.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...],
 "footnotes": ["p. 203 n. 1: For the text see Naville, Todtenbuch, Bd. I., Bll. 137, 138.", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.
