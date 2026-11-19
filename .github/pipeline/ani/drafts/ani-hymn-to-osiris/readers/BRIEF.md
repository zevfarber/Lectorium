# Reader brief — ani-hymn-to-osiris (Budge 1895, Plate II, the hymn to Osiris, pp. 8–11)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-hymn-to-osiris/readers/ other than
your own. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 8 = PDF 172, p. 9 = 173, p. 10 = 174, p. 11 = 175). Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page; --info prints
the page size). Look at each row image with the Read tool. (python3 is 3.11; PyMuPDF is installed for it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/03a7c044-3e76-5d7e-9062-f597fd199be8/scratchpad/<your-reader-id>/

## What to read
The text starts at the heading "PLATE II." in the lower half of p. 8: line "1." ṭua Àusàr Un-nefer neter āa (An adoration
of Osiris, Un-nefer, god great). Everything ABOVE that heading on p. 8 (the end of the Appendix that began on p. 5) is OUT.
Read on through p. 9 and p. 10 (every row) to p. 11, line 20, ending "Àusàr ān Ani" (Osiris, scribe Ani!) just above the
heading "PLATE III." on p. 11. Everything from "PLATE III." down is OUT (it belongs to the next part). Plate for every word: "II".
Footnotes (below a rule at a page foot) are OUT as words, but report every footnote's text (with the word its superscript
number is attached to) in your "footnotes" list; where a footnote prints hieroglyphs, give their Gardiner codes.
Superscript footnote numbers and small asterisks next to signs are not signs. Bold line numerals "2." … "20." set inside the
rows are not signs either.

A printed row is three lines: hieroglyphs, Budge's transliteration (italic), his English. Each transliteration group
sits under one group of signs = one word (Budge's own word division; a hyphenated suffix "āḥā - f" stays in its word).
Budge draws a horizontal line over signs written in red ink (rubric) — e.g. over the first word(s) on p. 8 line 1 and
over ànet' ḥrà - k on p. 10 line 8; check every word and say exactly which words the line covers. Words Budge puts in
[square brackets] in the TRANSLITERATION (e.g. "[per]" on p. 11 l. 19) — look whether the hieroglyph line also has
brackets or a gap, and say what you see.

## For every word write
{"page": 8, "plate": "II", "line": 1, "signs": ["M17","N35"], "q": "0:1", "budge": "àn", "gloss": "See"}
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
- Names: Un-nefer, Àbṭu, Nut, Nu, Àkert, Ta-sert, Neter-χert, Ṭeṭṭetu, Sekhet-Àrui, Tuat, Ànnu: code every sign and the
  determinative (town O49, desert/foreign-land N25, etc.).
- māfkia "emerald/turquoise" (p. 10), χesbeṭ "lapis", ṭesert "Ta-sert", bennu bird, the boat/sail signs in χentiθi,
  the two figures in āq per: describe exactly and give your best code.
- Code what is printed at every occurrence, even of a word you have already coded: the type varies.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...],
 "footnotes": ["p. 1 n. 1: Characters over which a line is printed are, in the papyrus, written in red.", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.

