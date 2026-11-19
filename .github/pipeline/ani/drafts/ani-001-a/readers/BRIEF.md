# Reader brief — ani-001-a (Budge 1895, Plate V, Spell 1 first half, pp. 19–20)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-001-a/readers/ other
than your own. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 19 = PDF 183, p. 20 = PDF 184). Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page; --info prints
the page size, 1164 x 1545 points). Look at each row image with the Read tool. PyMuPDF is installed (python3).
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/13465694-557d-57be-aff8-12f1d9656a1d/scratchpad/<your-reader-id>/

## What to read
- p. 19: everything ABOVE the heading "PLATE V." (Plate IV, ending "χer Àusàr / before Osiris.") is OUT.
  From "PLATE V.": line "1." ḥā em reu nu pert em hru … — every row to the foot of p. 19 (Plate V ll. 1–5,
  last word on the page āāa "great"). Plate = "V" for every word. Budge rules a line over the first rows
  (rubric = red ink): say exactly which words lie under an overline.
- p. 20: the rows from the top (enma ṭepet "in the boat") down to and INCLUDING "Ànnu / in Heliopolis" on the last
  row (Plate V l. 13). STOP there: the last three groups of that row — nuk / Ṭetṭeti / se ("I am Tetteti, the son of")
  — are OUT (they begin the next part). The footnote on p. 20 (to àmṭu, "Or temṭu; see Brugsch…") is OUT as a word;
  copy it into "footnotes". The superscript 1 after àmṭu is not a sign. Budge's "[uā]" on l. 8 is set in square
  brackets in the hieroglyph line too: flag "restored": true and say which signs are bracketed.
Footnotes are OUT as words; report their text in brief in your "footnotes" list.
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

## Rulings from the established judgment scene (Plates III–IV) — apply where the same shape is printed
D53 for the hooked sign with issue in embaḥ and met; A51 for Ani's seated-on-chair determinative where the chair and flail
are printed, A1 where he kneels or sits plainly; U35 one ligature in χesef; O50 in sep; G26 X1 Z4 for Teḥuti; G41 (bird
alighting) in pa; Aa21 alone in ut'ā; U6 in mer; M3 in àm-χet; V38 (loop crossed by a band) for ut where printed;
Budge's dotted letters followed exactly as printed (t'eṭ vs t'et, ṭep, qem).

## Things to watch in this text
- Rubric: the overlined rows at the start of Plate V (the chapter title ḥā em reu nu pert em hru …, and perhaps the
  following speech head) — check every word under the line.
- The repeated phrase semaāχeru Àusàr er χefta-f "making victorious Osiris over his enemies" (twice), hru pui en ut'ā
  t'etet "that day of weighing words", nuk ... àmṭu-k (the unusual sign group at the start of àmṭu), Neter-χert,
  Teḥuti (Thoth), Nut, χenrà, sebàu, sebi-nà, Ḥet ur, ur àmmi Ànnu, t'a'at (the divine chiefs), qeres (burial),
  enma ṭepet (the boat): code every sign including determinatives.
- Code what is printed at every occurrence, even of a word you have already coded: the type varies.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...], "gaps": [...],
 "footnotes": ["p. 11 n. 1: An interesting variant …", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.
