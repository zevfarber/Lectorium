# Reader brief — ani-018-b (Budge 1895, Spell 18 sections F–J and the closing rubric, Plate XIV, pp. 79–83)

You are one of TWO INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at the other reader's file in drafts/ani-018-b/readers/ nor at any other
part's reader files or established files. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 79 = PDF 243, p. 80 = PDF 244, p. 81 = PDF 245, p. 82 = PDF 246, p. 83 = PDF 247). Page sizes: p. 79 1165 × 1545
points; p. 80 and p. 82 1128 × 1543; p. 81 and p. 83 1146 × 1544. At zoom 1 the text block runs roughly y = 200–1180
points; each printed row (hieroglyphs, transliteration, English) is about 100–110 points tall.
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page); for a dense row
look at its left and right halves separately. Look at each image with the Read tool. PyMuPDF is installed (python3).
(The PDF's text layer is bad OCR: do not use it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/d240c473-d667-5404-9029-9d76132ba26e/scratchpad/<your-reader-id>/

## What to read — Ani's text only
1. p. 79: under the heading "PLATE XIV.", start at row 1 with "F. 1." "àr" "t'at'at" ("Now the divine chiefs") and read
   every row to the end of the text on p. 79 (row 6, "§ G. 1. àr t'at'at āāt àmt àp mitu Teḥuti pu").
2. p. 80: every row. 3. p. 81: every row. 4. p. 82: every row.
5. p. 83: every row, to "ḥeḥ sep" ("millions of times."), the end of the chapter (the last rows are a rubric under
   overlines: "If be said chapter this …"). STOP there. (p. 84 is PLATE XV, the next part.)
Footnotes (below the rule at the foot of each page — p. 79 nn. 1–2, which print variant texts in hieroglyphs; p. 81
nn. 1–3): do NOT read their signs as words; list in "footnotes" which word carries each mark and what the footnote
says (one line each, transliteration only).
SECTIONS AND LINE NUMBERS: Budge marks sections "F." (printed without §), "§ G." … "§ J." and the papyrus line numerals
RESTART AT 1 in each. Give every word "hall" = the section letter as a string ("F" … "J"), and "line" = the numeral in
force (a numeral applies from the word right after it; a word whose group is split by a numeral keeps the line in force
at its first sign). Approximately:
  F = from "F. 1. àr t'at'at" (p. 79 row 1) to "sen" before "§ G." (p. 79 row 5);
  G = from "§ G. 1." (p. 79 row 6) to "χefta - f" before "§ H." (p. 80 row 7);
  H = from "§ H. 1." (p. 80 row 7) to "seśeta āru" before "§ I." (p. 81 row 6);
  I = from "§ I. 1." (p. 81 row 6) to "χefta - f" before "§ J." (p. 82 row 5);
  J = from "§ J. 1." (p. 82 row 5) to the end, "ḥeḥ sep" (p. 83 last row) — the rubric at the end of p. 83 (from
      "t'ettu re pen" on) belongs to J and carries on J's line numerals (5., 6. …).
Check these boundaries on the page and say in "notes" if the page differs.
PLATE: every word is "plate": "XIV".
A word Budge prints with NO transliteration under it: still record it, with "budge": "—" and his English as gloss, and say
so in "unsure".
Square brackets in the HIEROGLYPH line = Budge's restorations: "restored": true on that word, and say in "unsure"
which signs are inside. Brackets only in his English ("[on]", "[with]", "[the festival of]") are not restorations.
Overlines (rubric, red ink): mark exactly the words under a ruled line with "rubric": true. The thin rule across the
top of the page is not an overline; an overline is a line ruled directly over particular groups (e.g. the long line over
"àr t'at'at āāt àmt …" at the head of each section, short ones over "à" before Teḥuti, over "àr sāpt" on p. 80 row 1,
and the lines over the closing rubric rows on p. 83) — check where each one starts and ends, row by row.
"(sic)" or "(?)" printed by Budge: say in "unsure" on that word exactly what is printed and where.

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

## Rulings from the established Spell 146 pylons 7–10 (Plates XI–XII) — apply where the same shape is printed
the tall upright with a small tie on its left Y1a; Ani's det A52 where he squats with flail; āχem's bird G17;
smammet Aa11; hereret Y1; χet M3; strokes after words Z1.

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


## Rulings from the established Spell 147 gates 4–7 (Plates XI–XII) — apply where the same shape is printed
kneeling figure with hand at mouth A2 in ren / t'et / χeru (where it is printed so — A1 if the arm is raised, open hand);
seated long-wigged figure after names A40; Ani squatting with flail A52; meter's / χemet's hooked sign D53; pool on legs
N37 + D54; qemam T14 + M15 approx; ordinal numerals as stacked strokes: Z15A (2), Z15B (3), Z15c (4), Z15d (5), Z15e (6), Z15f (7) as the Spell 147
parts coded them — count the strokes exactly and give the count in "unsure" if unclear; sebχet "pylon" — code each sign you see (O34 D58 Aa1 X1 + the pylon / gateway determinative: O16/O17/O36?
name the shape in "unsure" if no exact code fits).

## Rulings from the established Spell 146 pylons 1–6 (Plate XI) — apply where the same shape is printed
Budge's dotted letters as printed (t'eṭet / t'etet, ṭept, qeṭ — copy exactly what this page prints); àri (… A47) and
āa - s as Budge's transliteration groups them (one word if he prints one group "àri āa - s"); the lozenge-tipped rod
O29 lying over D36 in āāt / āāau; the hatched frieze O29 over U15 where printed; numerals Z15c/d/e/f (4–7 strokes),
eight / nine / ten strokes: count them and code Z15g (8), Z15h (9), V20 (10) where that is what is printed, giving the
stroke count in "unsure"; χeft A14 where the falling-man sign is printed; sart Aa18 approx; seṭebḥ M3; the pylon
determinative of sebχet O16 approx (say which shape: tall tower, or L-shaped building with frieze); sper's F42 approx;
Àusàr Q2 D4 without god figure where so printed; Ani's det varies (A52, A1, none) — code what is printed;
Semati / names with U1 over the vulture as a ligature where so printed.

## Rulings from the established Spell 18 introduction (Plate XII) — apply where the same shape is printed
t'at'at: U28 + the small eared ring W24 approx (T22 possible — say which shape) + X1 + U28 + N1 (approx, barred sign) +
A40 + strokes (house); àmu with the chick G43 where no owl face; āāt / āā low flat ā D36 (close to U15 — code what is
printed); ànet' Aa27 approx; maāt with the plinth Aa11 (upright or lying — code what is printed); àmt Z11 (upright
crossed by a bar) + G17 or X1 as printed; the negative àn D35 approx; seated god after names A40, seated man A1.

## Rulings from the established Spell 18 sections A–E (Plate XIII) — apply where the same shape is printed
à "Hail" M17 + kneeling hand-to-face figure A2; semaāχeru O34 U1 Aa11 P8 G43 A2 (code what is printed);
Ṭeṭṭeṭu / Teṭṭeṭu R11 R11 G43 O49 with Budge's dotted letters exactly as printed; t'at'at U28 W24(approx) X1 U28 N1(approx)
A40 Z2 in that order (house reordering); Naàrereṭef's hanging loop T12 approx (V4 possible); seated god det A40;
enemy classifier with raised arm A13 approx (A14 possible — say which shape); Set with the Set-animal E20/C7 as printed.
