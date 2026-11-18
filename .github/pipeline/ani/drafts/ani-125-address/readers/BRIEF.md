# Reader brief — ani-125-address (Budge 1895, the Appendix after the Confession, pp. 203–213)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file (drafts/ani-125-address/readers/A*.json,
B*.json other than your own). Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 203 = PDF 367). Pages are 1128 × 1543 points. Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 2 --out <scratch>/x.png
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points). Look at each row image (Read tool).
Use your scratch directory for images: /tmp/claude-0/-home-user-Lectorium/1bf9d824-5093-5b04-ad69-519e6dac3af4/scratchpad/<your-reader-id>/

## What to read
The section headed "Appendix." (footnote 1: Naville, Todtenbuch, Bd. I, Bll. 137, 138) that begins on p. 203 under the
42nd declaration, with the line numeral "2." (first word ànet' "Homage"), and runs to p. 213, ending "su er - à" /
"Hath decreed it he for me." — just above the horizontal rule after which line "1." àu šen en Àusàr (Spell 42) begins.
Everything above "Appendix." on p. 203 and everything below that rule on p. 213 is OUT. Footnotes are OUT (but report
every footnote's text in your "footnotes" list).

A printed row is three lines: hieroglyphs, Budge's transliteration (italic), his English. Each transliteration group
sits under one group of signs = one word (Budge's own word division; a hyphenated suffix "t'et - ten" stays in its word).

## For every word write
{"page": 203, "plate": "App.", "line": 2, "signs": ["M17","U23","..."], "q": "0-1:2", "budge": "ànet'", "gloss": "Homage"}
- line = the small bold numeral in force ("2.", "3." … set inside the rows). A numeral applies from the word right after it.
- signs = Gardiner codes in reading order (left→right, top→bottom within a group). Every sign you see, including strokes
  (Z1, Z2 plural strokes, Z3 vertical three, Z4 dual strokes), determinatives and suffix figures.
- budge = his transliteration EXACTLY as printed, with his letters: à ā ī χ θ ś t' ṭ ḥ ḳ, hyphens with spaces as printed
  ("ren - ten"), [ ] as printed (bā[n] - à). gloss = his English words under it, as printed (best alignment).
- q = layout (omit for one sign or a plain left-to-right string): indices into signs; "-" between groups set side by side,
  ":" between signs stacked top-to-bottom inside a group, "*" between signs side by side inside a stacked group.
  e.g. ["D21","Z1"] with D21 above Z1 → "0:1"; ["G35","N29","D54"] with G35, then N29 above D54 → "0-1:2".
- "rubric": true if Budge draws a line over the signs (red ink). "restored": true if he sets the word or part in [ ] in the
  hieroglyph line (shaded/bracketed signs) — say which signs in "unsure" if partial.
- "approx": [codes] for a sign with no exact Gardiner/Unicode match (use the nearest standard code) + "unsure" describing it.
- "unsure": "<what you see>" whenever you are not sure of a sign. Never complete a word from its transliteration without
  seeing each sign; Budge's transliteration is a CHECK: the phonetic signs must spell it (his letters: à = reed M17;
  ā = arm D36; a = vulture G1; ī/i = double reed or strokes; u = quail chick G43 or coil Z7; χ = Aa1 or F32 (ẖ);
  θ = tether V13; t' = cobra I10 / D; ś = pool N37 or S29-ish per type; ṭ = hand D46; ḳ = jar-stand W11 / G;
  ḥ = twisted wick V28; h = shelter O4). If the signs cannot give his reading, look again.

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

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...],
 "footnotes": ["p. 203 n. 1: For the text see Naville, Todtenbuch, Bd. I., Bll. 137, 138.", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.
