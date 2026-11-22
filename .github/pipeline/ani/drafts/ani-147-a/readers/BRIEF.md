# Reader brief — ani-147-a (Budge 1895, Plate XI upper register, Spell 147 — the seven gates (ārits), halls 1–3, pp. 56–59)

You are one of TWO INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at the other reader's file in drafts/ani-147-a/readers/ nor at any other
part's reader files or established files. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 56 = PDF 220, p. 57 = PDF 221, p. 58 = PDF 222, p. 59 = PDF 223). Page sizes: pp. 56, 58 1128 × 1543 points;
pp. 57, 59 1165 × 1545 points. (At zoom 1 the text block runs roughly y = 200–1200 points.)
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page). Look at each
row image with the Read tool. PyMuPDF is installed (python3). (The PDF's text layer is bad OCR: do not use it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/87523b4e-47a3-58c2-b774-448c143b658f/scratchpad/<your-reader-id>/

## What to read — Ani's text only
1. p. 56: rows 1–2 are the previous part (they end "pu" "Rā is."): do NOT read them. Start under the heading
   "PLATE XI.—Upper Register." with the row beginning "The First Ārit. 1." — first word "ārit" ("Hall"). Read that row and
   the next ("āśt - āru … semà", ending "the herald"). STOP at the horizontal rule: everything below it ("The following lines
   conclude this chapter in Lepsius, Todtenbuch, Bl. 11:" and its rows "àr ār - sen …" to "χefti - f") is NOT Ani's text
   (it concludes Spell 17 from another edition) and is never read.
2. p. 57: every row (rows 1–10, from "àm - s" to "senet'em"). Footnotes 1 (after "ertu - k") and 2 (on "seχem - k")
   are not signs: record their text in "footnotes" (hieroglyphs as codes).
3. p. 58: every row (rows 1–11, from "men" to "tā - k"). "(sic)" marks printed over a sign are not signs: say in "unsure"
   on that word that Budge prints (sic) over it.
4. p. 59: every row up to and including "Re - stau" ("in Re - stau.") in the last row, just before "The Fourth Ārit. 1.".
   STOP there; the Fourth Ārit is the next part.
The English labels "The First Ārit.", "The Second Ārit.", "The Third Ārit." printed in the left margin are Budge's, not
signs: do not record them as words. Instead give every word a field "hall": 1, 2 or 3 (the ārit it belongs to).
plate = "XI" throughout. line = the small bold numeral in force (a numeral applies from the word right after it; a word
whose group is split by a numeral keeps the line in force at its first sign). LINE NUMBERS RESTART AT 1 IN EACH ĀRIT
(hall 1 runs 1–17, hall 2 from 1, hall 3 from 1) — record them as printed. The first word "ārit" is hall 1, line 1.
Square brackets in the HIEROGLYPH line (e.g. p. 56 "[N35]" after en; p. 57 row 9 "[D21 A1]"; p. 58 "[ārit]", "[Seqet]"-group;
p. 59 the bracketed group in "unχ") = Budge's restorations: "restored": true, and say in "unsure" which signs are inside.
Brackets only in his English or transliteration without bracketed signs are not restorations (but note them).
Overlines (rubric, red ink): mark exactly the words under a ruled line with "rubric": true. The thin rule across the
top of the page is not an overline; an overline is a line ruled directly over particular groups (many rows here have
them — check where each one starts and ends).
Hatched / dotted lacunae printed in a row inside Ani's text: record in "gaps" with page, line and position.

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
