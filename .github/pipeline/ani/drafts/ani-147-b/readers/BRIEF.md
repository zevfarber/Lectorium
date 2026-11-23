# Reader brief — ani-147-b (Budge 1895, Plates XI–XII upper register, Spell 147 — the seven gates (ārits), halls 4–7, pp. 59–63)

You are one of TWO INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at the other reader's file in drafts/ani-147-b/readers/ nor at any other
part's reader files or established files. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 59 = PDF 223, p. 60 = PDF 224, p. 61 = PDF 225, p. 62 = PDF 226, p. 63 = PDF 227). Page sizes: pp. 60, 62
1128 × 1543 points; pp. 59, 61, 63 1165 × 1545 points. (At zoom 1 the text block runs roughly y = 200–1200 points.)
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page). Look at each
row image with the Read tool. PyMuPDF is installed (python3). (The PDF's text layer is bad OCR: do not use it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/3613ea84-7cb1-59fe-96f9-c5cd0469413b/scratchpad/<your-reader-id>/

## What to read — Ani's text only
1. p. 59: everything up to "Re - stau" ("in Re - stau.") in the last row belongs to the previous part: do NOT read it.
   Start in the last row with "The Fourth Ārit. 1." — first word "ārit" ("Hall the"), then "àft" ("fourth."), "ren"
   ("The name"), to the end of that row.
2. p. 60: every row (rows 1–10, from "en" "of" to "Teb - ḥrà - keḥa -"). In the 8th row Budge's English for ut'ā - nà is
   printed in braces ("I have weighed in judgment"): record it as his gloss. "The Fifth Ārit." in row 8 is a margin label.
3. p. 61: every row above and below the heading "PLATE XII." (from "χeft" to "Ates -"). The short horizontal rule
   and the heading "PLATE XII." are not text: words before the heading have plate "XI", words after it plate "XII".
4. p. 62: every row (from "ḥrà" to "rer - k pet maa - k Rā maa - k"). The dots "....." after "em" in row 5 are
   Budge's: record them in "gaps" (page, line, position, what is printed) — they are not a word.
5. p. 63: rows 1–4 only, from "reχit" to "χer - k" ("before thee."). STOP there: row 5 ("1. t'etet χeft sper er
   sebχet tept …", "Words spoken when [one] cometh to pylon the first", with a long overline) begins Spell 146, the
   next part — do not read it. Footnote 1 ("Var." with four rows of hieroglyphs and the Naville reference, below the
   rule) is a footnote, not Ani's text: do not read its signs as words; give in "footnotes" only where its mark "1"
   stands in the text (it is after "user - f", p. 63 row 2) and that it prints a variant text from Naville.
The English labels "The Fourth Ārit.", "The Fifth Ārit.", "The Sixth Ārit.", "The Seventh Ārit." printed in the
rows are Budge's, not signs: do not record them as words. Instead give every word a field "hall": 4, 5, 6 or 7 (the
ārit it belongs to). LINE NUMBERS RESTART AT 1 IN EACH ĀRIT — record them as printed (the small numerals "1." "2." …
set inside the rows; a numeral applies from the word right after it; a word whose group is split by a numeral keeps
the line in force at its first sign). The first word "ārit" on p. 59 is hall 4, line 1.
Square brackets in the HIEROGLYPH line = Budge's restorations: "restored": true on that word, and say in "unsure"
which signs are inside (e.g. p. 61 row 2 "[N35]"? — check; p. 62 row 4 the bracketed group of "maat en"; p. 62 last
row the bracketed sign of "maa - k"). Brackets only in his English or transliteration without bracketed signs are not
restorations (but note them). "(sic)" printed by a sign (e.g. p. 62 row 6, under/over a sign of Sekhem - Maṭenu) is not
a sign: say in "unsure" on that word that Budge prints (sic) there.
Overlines (rubric, red ink): mark exactly the words under a ruled line with "rubric": true. The thin rule across the
top of the page is not an overline; an overline is a line ruled directly over particular groups (several rows here
have them, mostly over "ārit + numeral" and "ren" — check where each one starts and ends).

## For every word write
{"page": 57, "plate": "XI", "hall": 1, "line": 4, "signs": ["M17","D21"], "q": "0:1", "budge": "àr", "gloss": "As"}
- signs = Gardiner codes in reading order (left→right, top→bottom within a group). Every sign you see, including strokes
  (Z1, Z2 plural strokes, Z3, Z4 dual strokes), determinatives and suffix figures.
- budge = his transliteration EXACTLY as printed, with his letters: à ā ī χ θ ś t' ṭ ḥ ḳ, hyphens with spaces as printed
  ("ān - f"), [ ] as printed. gloss = his English words under it, as printed (best alignment).
- q = layout (omit for one sign or a plain left-to-right string): indices into signs; "-" between groups set side by side,
  ":" between signs stacked top-to-bottom inside a group, "*" between signs side by side inside a stacked group.
  e.g. ["D21","Z1"] with D21 above Z1 → "0:1"; ["G35","N29","D54"] with G35, then N29 above D54 → "0-1:2".
- "rubric": true / "restored": true as above.
- "approx": [codes] for a sign with no exact Gardiner/Unicode match (nearest standard code) + "unsure" describing it.
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

## Rulings from the established Spell 17 part 2 (Plates VII–VIII) — apply where the same shape is printed
Àmsu R22 + R12; śuti's plume H6; àmt Z11 (upright crossed by a bar); the seated figure after àtef / mesu coded A1;
uat' (utchat context aside) the M14 ligature; āba O26 N29 G1 U15; the low hooked sign U15 throughout; θet has D54;
Set with a hatched rectangle N37 (approx); Māāāat G17 + D36; ḥesmen U32 + N33×3; nest G48; Neter-χert R8 D21 T28
(D21 approx); the eye of the utchat D10 if the type shows the falcon-cheek markings, otherwise D4 — say which.
Seχet-Àaru kept one word. Meḥ-urt is one word (as Budge hyphenates).

## Rulings from the established Spell 17 part 3 (Plates VIII–X) — apply where the same shape is printed
χet / em-χet M3 (horizontal branch); àmiu-χet one word; ennu's low tabbed sign U19 (approx); Mesθà Aa15; śāt / śāṭ M44
(approx); maā U1 D36 where so printed; pa G40; sa Aa18; neteru / nebu two words; T'afi: small × Z9, bird G47 (approx),
Z9 + I9, Z4, two seated gods A40; ba G29 with R7 at its foot where printed; ḥer-àb D2 Z1 F34 Z1; small strokes after
words Z1.

## Rulings from the established Spell 17 parts 4–5 (Plate X) — apply where the same shape is printed
āḥā Y1; ḥer-àb D2 F34; ḥuau V4; àati D57 + O1; χennu F32; strokes Z2; seated figures A1 except after gods (A40);
maāχeru may be printed without the sickle (Aa11 P8 — code what is printed); Àusàr Q2 D4 where a low seat and no god
figure; ḥept's det D32 approx; A7 (weary man) / A14 / A47 where printed; X6 in paut; N2 in keku; mesi/mesit's table-like
sign R3 approx; θeḥent S15 approx; àri A47; χer printed T28 + D21 + Z1; māχatu F32 + F51 approx; θes rer S24 + D21 + Y1a;
ta of taui with two bow-tie signs N21 approx; Suten-ḥenen's figure A1 approx; Budge's dotted ṭ followed exactly;
Nebt-ḥet with I12 (cobra) where printed; ta "earth" with a curled flat sign N16 approx; θet V13 + D54; Set's plain
rectangle N37 approx; àn's sign W25 approx.

## Rulings from the established Spell 147 halls 1–3 (Plate XI) — apply where the same shape is printed
t'eṭ / t'eṭṭu printed as a cobra-and-hand ligature: code I10 D46; āa of àri āa (doorkeeper) the upright hatched sign O29
approx (O31 possible — say which shape); the watcher's word sati: X1 and Z4 over U15, then O34 (code what is printed);
Metti / χemet's hooked sign D53; Ani squatting with flail, no chair, A52; seated god det A40; rer V10 approx; maa (see)
D4 + U1 ligature where so printed; uṭen's hooked loop V1 approx; seśeṭ's and unχ's looped cord V6 approx; Teḥuti G26 X1 Z4;
Àbṭu S34 approx; ḥauatu V4 approx; the curled flat sign U15 where it stands like an arm with no ā in Budge's reading (code
what is printed and say so in "unsure"); Re-stau D21 Z1 V2 (approx) Z1 Z2 N25; t'et àn Àusàr "Saith Osiris" — t'et
is the cobra-and-hand ligature, àn the fish-like sign W25 approx (house) — code what you see.
