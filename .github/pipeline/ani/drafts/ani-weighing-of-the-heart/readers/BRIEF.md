# Reader brief — ani-weighing-of-the-heart (Budge 1895, Plates III–IV, the judgment scene, pp. 11–19)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-weighing-of-the-heart/readers/ other
than your own. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 11 = PDF 175 … p. 19 = PDF 183). Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page; --info prints
the page size). Look at each row image with the Read tool. (python3 is 3.11; PyMuPDF is installed for it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/49eb51cf-4a65-547b-84e0-5c746f5367db/scratchpad/<your-reader-id>/

## What to read (the whole part; your task names which pages are yours)
- p. 11: from the heading "PLATE III." (lower half): line "1." t'et àn Àusàr (Speech by Osiris …) to the foot of the page.
  Everything ABOVE "PLATE III." (the end of Plate II) is OUT.
- p. 12: the rows down to "setem-k / Good, good is it for thee to hear ......" (l. 15); THEN the legend headed
  "[Above the head of Anubis.]" — IN (words written beside a figure of the vignette): t'et àn àm ut … er āḥāu - s.
  Give its words the plate "III" and the line in force (15) and add "legend": "Above the head of Anubis" to each.
  The heading itself is Budge's, not a word. Where Budge prints a hatched rectangle (damage) with "......", do NOT
  invent a word and do not put a word with no signs: add an entry to a top-level "gaps" list in your file:
  {"page": 12, "line": 15, "afterWord": "<budge of the word before the gap>", "what": "<what is printed, how wide>"}.
  Footnotes 1 and 2 on p. 12 (Hunefer, Ànhai variants) are OUT as words.
- pp. 13–15: the section headed "Appendix." (Parma and Paris papyri, Naville) is OUT, down to the heading
  "PLATE III.—(continued)." near the foot of p. 15. From that heading: line "16." T'eṭ àn Teḥuti … embaḥ — IN.
- p. 16: every row (Plate III ll. 19–27). On l. 26 Budge prints "…. en set": look whether the hieroglyph line has a gap,
  hatching or brackets there and record it exactly (a "gaps" entry as above if there is a gap).
- p. 17: every row of Plate III (ll. 27–30, ending "mà śesu Ḥeru / like the followers of Horus"), then the heading
  "PLATE IV." and Plate IV ll. 1–3 (plate "IV" from there).
- p. 18: rows down to "un - à mà ḥesi enti" (Plate IV l. 9) above the footnote rule. Footnote 1 (Hunefer) is OUT.
  On p. 18 l. 5 Budge brackets part of Ani's name in the hieroglyph line: flag "restored" and say which signs.
- p. 19: the rows ending "χer Àusàr / before Osiris." above the heading "PLATE V." Everything from "PLATE V." down is
  OUT (it is Spell 1, the next part).
Footnotes (below a rule at a page foot) are OUT as words, but report every footnote's text in brief (with the word its
superscript number is attached to) in your "footnotes" list; where a footnote prints hieroglyphs, you may summarise
("prints a parallel text in hieroglyphs, 2 rows") — no need to code them.
Superscript footnote numbers and small asterisks next to signs are not signs. Bold line numerals set inside the rows are not
signs either.

## For every word write
{"page": 11, "plate": "III", "line": 1, "signs": ["M17","N35"], "q": "0:1", "budge": "àn", "gloss": "See"}
- line = the small bold numeral in force. A numeral applies from the word right after it; words before "2." are line 1.
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

## House rulings (from the established Spell 125 parts — apply them)
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
(t'eṭ = D46); trà M6; χer V12; ḳ = W11, χert = T28; the hatched low rectangle O31 (where that shape is printed); tall loop for θ V13;
the owl-over-arm ligature read mā is G17 + D36.

## Rulings from the established hymn to Ra (Plate I) — apply where the same shape is printed
Q1 for the tall seat in Àusàr, Q2 (approx) for a low couchant-shaped seat; jabiru G29 for ba (no human head); three
vertical strokes side by side = Z2 (as in Ani's name); small wedge N21 (approx) in resi / meḥtet / taiu; C1 for Rā;
A40 for neter and Àusàr; Z4 for two oblique strokes; G27 (approx) for the bird in se-ḥetem; ankh-like sign at the start of
Àbṭu S34 (approx) where U23 is expected — code what is printed and say so.

## Things to watch in this text
- Rubric lines (overline) appear at the start of most speeches: t'et àn Àusàr (p. 11 l. 1), t'et - f (l. 3), T'eṭ àn Teḥuti
  (p. 15 l. 16), t'et àn paut neteru (p. 16 l. 26), t'et àn Ḥeru (p. 17 Pl. IV l. 1), àn Àusàr Ani / t'et - f (p. 18 ll. 5–6).
  Check each word under the line; say exactly which words it covers. A line over a numeral is not a word.
- The heart words: àb (jar F34 or W-type pot?) and ḥāti (F4 forepart of lion?), χeperu (scarab L1), māχait (the balance
  sign U38), ut'ā (weighing), meter (witness), Àmemet (the devourer), Teḥuti (Thoth, ibis on a standard G26), paut neteru
  (Ennead), Šenit, Àmentet, Seχet-ḥetepu, śesu Ḥeru, sennu (cakes), ḥesi: code every sign and the determinative.
- "ḥen (?)" on p. 11 l. 11 — Budge marks his own doubt: describe the sign exactly.
- Code what is printed at every occurrence, even of a word you have already coded: the type varies.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...], "gaps": [...],
 "footnotes": ["p. 11 n. 1: An interesting variant …", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.
