# Reader brief — ani-029-027-058-059 (Budge 1895, Spells 29, 27, 58 and 59, Plates XV–XVI, pp. 96–105)

You are one of TWO INDEPENDENT readers of your stretch, establishing a hieroglyphic text from page scans of Budge's 1895
interlinear edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-029-027-058-059/readers/
nor at any other part's reader files or established files. Do not consult any translation of the Book of the Dead; work
only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 96 = PDF 260, p. 97 = 261, p. 98 = 262, p. 99 = 263, p. 103 = 267, p. 104 = 268, p. 105 = 269). Even pages are
1128 × 1543 points, odd pages 1146 × 1544. At zoom 1 each printed row (hieroglyphs, transliteration, English) is about
100–110 points tall.
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page); for a dense row
look at its left and right halves separately. Look at each image with the Read tool. PyMuPDF is installed (python3).
(The PDF's text layer is bad OCR: do not use it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/bc9236a5-aef0-5085-99cc-4323621ad734/scratchpad/<your-reader-id>/

## What to read — Ani's text only. Your task names ONE of the two stretches below.
STRETCH 1 (pp. 96–99): Chapters XXIX and XXVII.
 a. p. 96, the LAST row only (roughly y = 1020–1120 points), Chapter XXIX: "1. Re en temt erṭāt neḥemtu àb se mā - f em"
    ("Chapter of not allowing to be taken away the heart of a person from him in"). Everything above it on p. 96 (the top
    rows and the chapter "1. Re en sesenet nifu …") is Budge's Appendix from Naville / Nebseni: NOT Ani's text, do not read it.
    The footnotes on p. 96 belong to that Appendix: ignore them.
 b. p. 97, all rows down to "ta t'es - sen" ("ground their own.") — the end of Chapter XXIX (lines 2.–3.); then, under the
    short rule, Chapter XXVII: "1. Re en temt erṭāt θet ḥāti en se mā - f em" ("Chapter of not allowing to be taken away the
    heart of a man from him in"), its next row, then the heading "PLATE XVI." and the row under it ("neχefiut 2. àrit en
    ten …"). Words ABOVE the "PLATE XVI." heading are "plate": "XV"; words below it "XVI". Note the small marks printed
    on p. 97 (an "×" near āptui in row 1, "(sic)" in row 4): say exactly what you see in "unsure".
 c. p. 98, all rows (Chapter XXVII continued, lines 2.–5. or so). Plate XVI.
 d. p. 99, rows 1–2 only (roughly y = 210–460 points): "Neter - χert 6. Àusàr ān Ani maāχeru em ḥetep maāχeru em" /
    "Amentet nefert ḥer set ent ḥeḥ" ("the mountain of eternity."). STOP at the short rule under it: the heading
    "Appendix." and everything below it (Chapter XXIX A from Naville) is NOT Ani's text.
 Chapters: "XXIX" for a.–b. up to "t'es - sen"; "XXVII" from the second "1. Re en temt" on.
STRETCH 2 (pp. 103–105): Chapters LVIII and LIX.
 a. p. 103, from the row that begins "1. Re en seset nifu seχem em mu em Neter - χert" ("Chapter of breathing the air and
    having power over the water in the nether-world"), below the short rule (roughly y = 700 points), to the foot of the
    page. Everything above that rule on p. 103 (rows 1–3, ending "qeres - en - sen", "they bury [them]") is Budge's
    Appendix (Chapter XXVIII from Naville): NOT Ani's text.
 b. p. 104, all rows: Chapter LVIII continued and its closing rubric ("ár reχ re pen …", "If be known chapter this …",
    to "pert em neter - χert ent", "coming forth from the netherworld"), then, below the next rule, Chapter LIX
    "1. Re en seset nifu seχem em mu em Neter - χert" to the foot of the page.
 c. p. 105, rows 1–3 only (roughly y = 210–560 points), to "Ani em maāχeru" ("Ani in triumph."). STOP at the rule: the
    chapter "1. Re en temt mit em nem" below it is the next part.
 Chapters: "LVIII" for a.–b. up to "neter - χert ent"; "LIX" from the second "1. Re en seset" on. Plate: "XVI" throughout.
LINE NUMBERS: Budge's papyrus-line numerals restart at 1 for each chapter. Give every word "line" = the numeral in
force (a numeral applies from the word right after it; a word whose group is split by a numeral keeps the line in force
at its first sign) and "chapter". Read the numerals off the page and say in "notes" where each one stands.
A small raised numeral set high beside a word (¹, ²) is a FOOTNOTE MARK, not a line numeral.
A word Budge prints with NO transliteration under it: still record it, with "budge": "—" and his English as gloss, and say
so in "unsure". Dots "……" printed in his transliteration/English for a lacuna: say so in "notes" and record what is printed.
Square brackets in the HIEROGLYPH line = Budge's restorations: "restored": true on that word, and say in "unsure"
which signs are inside. Brackets only in his English ("[what]", "[in]", "[them]") are not restorations; give his English as printed.
Overlines (rubric, red ink): mark exactly the words under a ruled line with "rubric": true. The thin rule across the
top of the page is not an overline; an overline is a line ruled directly over particular groups (e.g. over the chapter
titles, and over parts of rows such as p. 104's closing rubric) — check where each one starts and ends, row by row.
"(sic)" or "(?)" printed by Budge: say in "unsure" on that word exactly what is printed and where.
## For every word write
{"page": 57, "plate": "XI", "chapter": "XXIII", "line": 4, "signs": ["M17","D21"], "q": "0:1", "budge": "àr", "gloss": "As"}
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

## Rulings from the established Spell 18 sections F–J (Plate XIV) — apply where the same shape is printed
the stroke after t'at'at / neteru / àpu a single dashed stroke Z1; enemy/dead classifier with raised arm A13 approx;
baiu G29 with R7 (R7 coded before G29 where at the bird's foot); the blood classifier (zigzag to a small cross) D26
approx; ṭā / erṭā with D21 over the flat arm D36 where so printed (D37 where the forearm holds a loaf — code what is
printed); maāχeru may be printed Aa11 P8 without the sickle; Teḥuti G26 X1 Z4 (or compressed / G26 alone — code what
is printed); Ani's det A52 where he squats with flail, A1 where plain; the hatched trapezoid W11 for ḳ, T28 for χer;
the low U15 after words with no ā in Budge (code what is printed and say so); īut begins with D54 where so printed.

## Rulings from the established Spells 23–24 (Plate XV) — apply where the same shape is printed
Ani's det A52 (squatting with flail); the wrapped seated figure with stick A47; the flat bar with a small tie Y1; the
tall upright with a side hook Y1a; seated god A40; em G17 or Aa15 as printed (G17 Aa15 together where both are printed).


## Rulings from the established Spells 26 and 30B (Plate XV) — apply where the same shape is printed
erṭāt with Budge's dot as printed, D21 + D36 (flat arm, no loaf) or D37 (arm holding a loaf) — code what is printed;
ḥāti F4 over X1 then F34; the rope coil V1 approx as a classifier of binding; two upright strokes Z4A (three = Z2);
the owl with an arm-tab against its chest = G17 D36 ligature, the owl followed by the low flat sign = G17 U15;
Neter-χert R8 D21 T28 (D21 approx); Àusàr Q1 D4 A40 or Q2 D4 as printed; Ani with two or three strokes as printed.


## Rulings from the established Spells 61 and 54 (Plate XV) — apply where the same shape is printed
tem (the negative) X1 U15 Aa15 (bevelled sign); neḥem's bowl with a three-pointed rim N41 approx; a tiny tick over ba is
not coded; the low flat U15 where no ā is read (code what is printed, say so); Ani's det the kneeling man A1 where no
flail is printed; à "Hail" a standing man with arm raised A26 approx; the plain long bar Y1 approx; ut'ā G43 I10 D36 Aa21
D54 where so printed; peḥti Q3 X1 F22 Z4 F9 (approx) where so printed; wp with the horns F13 (code what is printed).

## This part — words to look at closely (do not assume; code exactly what you see, name doubtful shapes in "unsure")
Stretch 1: temt / tem (the negative group), erṭāt (arm with or without loaf), neḥemtu / θet (the sign for "take away":
the rope / tether / lasso shape — name it), àb and ḥāti (the heart jar F34; ḥāti F4 + X1 + F34), se (man), mā - f
(owl-arm ligature?), Neter - χert, t'et àn Àusàr, Ani's det, maāχeru, ḥa - k (turn back), āptui (messenger; the "×"),
àu, ī - nek, ānχu, the negative àn, ṭātu, χentu, setem, neteru, ḥetepet (sic), ḥer, χer - sen, ḥrà, θeti, neχefiut, àrit,
ànet' - ḥrà - ten (the hand/arm group of "homage"), nebu, ḥeḥ, t'etta, tebā - ten (the finger), seχeperu, t'etet, tut
(evil), ḥerentet, rennu, χenti, χat (body), mat, seχem, entef, neb, àuk, req, ututet, Amentet, nefert, set (mountain).
Stretch 2: seset nifu (the sail P5), seχem, mu (water), un - nà, the bracketed [ni], trà, entek, sebi, χeper, nimā, enti,
ḥenā - k, Merti, ruà, ṭep, teken, Mesqen, ṭā - f, ta - à, ḥet, qem - ḥrau, saq baiu, ren, māχenti, neśi śen (hair),
useru (oars), sert, mat'abet, semet āqa, ḥemi, matet setut, qeres, sun, erṭāi - ten, māḥerà, àrtet, śens, pasi, ḥeni (sic),
àuf, Ànpu, àr reχ re pen, āq, pert, nehet (sycamore), Nut, ṭā - nà, mu (?) (Budge's query), àmt, χen, àuset, ḥer - àbt,
Unnu, sau - nà, suḥt, nekek ur, rut - s, ānχ, seset, maāχeru.
