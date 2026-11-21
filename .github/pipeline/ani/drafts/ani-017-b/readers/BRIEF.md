# Reader brief — ani-017-b (Budge 1895, Plates VII–VIII, Spell 17 part 2, pp. 32–36)

You are one of INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-017-b/readers/ other than your
own, nor at any other part's reader files or established files. Do not consult any translation of the Book of the
Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 32 = PDF 196 … p. 36 = PDF 200). Page size 1164 × 1545 points. Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page). Look at each
row image with the Read tool. PyMuPDF is installed (python3).
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/0ec69b85-8cee-54f8-85a0-b12549d28777/scratchpad/<your-reader-id>/

## What to read (whole part; your task says which pages are yours)
- p. 32: START in the FIRST row with the group "nuk" (I am) that follows "kerḥ pu" after the numeral "30.". "hru àr
  t'etta pu kerḥ pu" before it are NOT this part. Then every row of p. 32, including the heading "PLATE VIII." and the
  row after it (numeral 36. "Tem …"). Plate = "VII" for words above the heading PLATE VIII., "VIII" from it on.
- pp. 33, 34, 35: every row (Plate VIII).
- p. 36: every row UP TO AND INCLUDING the group "neśeni" (storms in the sky) in the LAST row. STOP there: the final
  "pu trà" ("What then") on p. 36 is NOT this part.
- line = the small bold numeral in force (30. on p. 32 … 70. on p. 36). A numeral applies from the word right after it.
- Overlines (rubric, red ink): the questions "Who then is this?" / "What then is it?", "ki t'et" (otherwise said) etc.
  are often ruled over. Mark exactly the words under a ruled line with "rubric": true. The thin rule across the top of
  each row band is NOT an overline; an overline is a shorter/heavier line ruled directly over particular groups.
- Square brackets in the hieroglyph line (e.g. p. 32 second row "[ … ]" before trà) = Budge's restorations:
  "restored": true, and say in "unsure" which signs are inside the brackets. Brackets only in his English are NOT
  restorations of signs.
- "(sic)" printed over a group: keep "(sic)" in "budge" as printed and note it.
- Small crosses printed in groups (after -f, at the horned viper's head, in χesef, etc.): code them inside the word as
  Z9 (ruling of the latest parts: the horned viper with its × is Z9 + I9), say so.
- A word whose hieroglyphs are split by a numeral stays ONE word; its line is the line in force at its first sign.
- Report any footnote in "footnotes" (OUT). Report any section headed "Appendix." (OUT) — none expected.

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

## Rulings from the established Spell 1 (Plates V–VI) — apply where the same shape is printed
Neter-χert ligature with D21 (approx) for its loop; U28 (approx) for the tall tapering t' sign; N1 (approx) for the
barred sign of t'at'at; Àusàr D4 Q1 A40 (D4 over the pair) where so printed; Z15e for the numeral VI; R7 coded before
G29 where printed at the bird's foot; A2 for kneeling man with hand to mouth; Budge's dotted letters followed exactly.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...], "gaps": [...],
 "footnotes": ["p. 26 n. 1: Read …", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.

## Rulings from the established Spell 17 part 1 (Plate VII) — apply where the same shape is printed
Neter-χert R8 D21 T28 (D21 approx); kneeling man with arm raised A1 (nuk, àuà), hand to mouth A2 (trà); flat roll with
tie Y1 (men, āḥā, enti); Nu with N35A (three water lines stacked as one group); ḥems N41 (approx) + A1;
 the tether V13 for θ; ḥeq / suten seated figure with staff A42 (approx).
