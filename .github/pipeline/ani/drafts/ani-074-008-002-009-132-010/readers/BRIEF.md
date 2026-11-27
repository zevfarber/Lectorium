# Reader brief — ani-074-008-002-009-132-010 (Budge 1895, Spells 74, 8, 2, 9, 132 and 10, Plate XVIII, pp. 118–122)

You are one of TWO INDEPENDENT readers of your stretch, establishing a hieroglyphic text from page scans of Budge's 1895
interlinear edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-074-008-002-009-132-010/readers/
nor at any other part's reader files or established files. Do not consult any translation of the Book of the Dead; work
only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 118 = PDF 282, p. 119 = 283, p. 120 = 284, p. 121 = 285, p. 122 = 286).
Even pages are 1128 × 1543 points, odd pages 1146 × 1544. At zoom 1 each printed row (hieroglyphs, transliteration,
English) is about 110 points tall; the text block starts at roughly y = 200 points.
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page); for a dense row
look at its left and right halves separately. Look at each image with the Read tool. PyMuPDF is installed (python3).
(The PDF's text layer is bad OCR: do not use it.)
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/8232a218-7db0-5b60-b357-6ff368cf12f6/scratchpad/<your-reader-id>/

## What to read — Ani's text only. Your task names ONE of the three stretches below.
Page running heads ("B.D. Chapp. …", "PLATE XVIII.") are not text. Plate: "XVIII" for every word.
STRETCH 1 (pp. 118–119): Chapter LXXIV and Chapter VIII.
 a. p. 118, from the row below the long rule (roughly y = 640 points) that begins "1. re en unt reṭ per em ta t'eṭ àn
    Àusàr" ("Chapter of walking with the two legs …") to the foot of the page (5 rows). The four rows ABOVE that rule
    (ending "ba - f", "his soul.") are the previous part: do not read them.
 b. p. 119, all rows: LXXIV continued to "maāχeru em ḥetep" (row 2, "triumphant in peace."); below the rule the title of
    Chapter VIII "1. re en āba Àmentet [pert] em hru …" and its rows to the foot of the page ("àp - f - tu emmā neteru").
 Chapters: "LXXIV" up to "ḥetep" on p. 119 row 2; "VIII" from the p. 119 title on.
STRETCH 2 (pp. 120–121 top): Chapter II and Chapter IX.
 a. p. 120, all rows: Chapter II "1. Re en pert em hru ānχ emχet mit …" to "ānχiu" ("among the living.", row 6); below the
    rule Chapter IX "1. Re pert em hru emχet āba àmmehet …" to the foot of the page. The FOOTNOTE at the bottom of p. 120
    ("¹ Read …") is OUT: do not record it as a word; copy what it says into "footnotes" (its signs as codes if you can).
 b. p. 121, rows 1–6 only (IX continued, to "uat Àusàr ān Ani maāχeru", "a way, the Osiris, the scribe Ani, triumphant.";
    roughly y = 200–870 points). STOP at the long rule: "1. Re en erṭāt rer su se …" below it is stretch 3.
 Chapters: "II" up to "ānχiu" on p. 120; "IX" from the p. 120 second title on.
STRETCH 3 (pp. 121–122): Chapter CXXXII and Chapter X.
 a. p. 121, from the row below the long rule (roughly y = 870 points) that begins "1. Re en erṭāt rer su se er maa pa - f
    ṭep ta" to the foot of the page (3 rows). The six rows ABOVE that rule are stretch 2: do not read them.
 b. p. 122, all rows: CXXXII continued to "ḥetep Àusàr Ani" (row 2, "peace Osiris Ani."); below the rule "1. ki re en pert
    se em hru er χefta - f em …" (Budge's Chapter X, = XLVIII) to the last row "Ani pen χemt em χāāu - f" ("Ani this,
    without his ……….") — the end of the part.
 Chapters: "CXXXII" up to "Ani" on p. 122 row 2; "X" from the p. 122 title on.
LINE NUMBERS: Budge's papyrus-line numerals restart at 1 for each chapter. Give every word "line" = the numeral in
force (a numeral applies from the word right after it; a word whose group is split by a numeral keeps the line in force
at its first sign) and "chapter". Every stretch here begins with a chapter title
numbered "1.", so no numeral carries over from before your stretch; a chapter continued onto the next page keeps the last
numeral printed on the page before. Read the numerals off the page and say in "notes" where each one stands.
A small raised numeral set high beside a word (¹, ²) is a FOOTNOTE MARK, not a line numeral.
A word Budge prints with NO transliteration under it: still record it, with "budge": "—" and his English as gloss, and say
so in "unsure". Dots "……" printed in his transliteration/English (e.g. p. 119 "tep ....", "…. em", p. 121 "ātef . . . - à", p. 122 last row "his ……") : say so in "notes" and record what is printed.
Square brackets in the HIEROGLYPH line = Budge's restorations: "restored": true on that word, and say in "unsure"
which signs are inside. Brackets only in his transliteration or English ("ku[à]", "[there be]") are not restorations of
signs unless the hieroglyph line also has brackets: look at the sign line and say what you see.
Overlines (rubric, red ink): mark exactly the words under a ruled line with "rubric": true. The thin rule across the
top of the page is not an overline, and the long rules that separate chapters are not overlines; an overline is a line
ruled directly over particular groups (e.g. over the chapter titles, over "t'et àn", and over closing rubrics) — check
where each one starts and ends, row by row.
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

## Rulings from the established Spells 29, 27, 58, 59 (Plates XV–XVI) — apply where the same shape is printed
the × at the viper's head is its horns: I9 alone; θet V13 + D54; t'eṭet with the hand D46; maāχeru U1 D36 where the arm is
printed; mā / māχenti the owl-arm ligature G17 D36; sebi O35; semet O34 D53 X1 Z4A Y1a; Ànpu C6; ruṭ D46; pasi O1 as printed.
Line numerals printed inside a word leave the word in the line in force at its first sign.

## Rulings from the established Spells 44, 45, 46, 50, 93 (Plates XVI–XVII) — apply where the same shape is printed
θes / θest / θesu S24 (girdle knot), not V13; nem's slanting rod T34 approx; un / unu's hatched rectangle O31 (house);
àmen's man behind a wall A5; urṭ's det A7; the loop-and-tail curl F51 approx; the bird with arm-like projections in
seχem / useru coded G24 approx; t'a / t'ait's det (flat base carrying a small sprawling shape) P1 approx; ḥetem's second
sign D58 approx where so printed; ennu(ṭ)'s U19 (house); taui N16 Z4 N16 Z4; maāχeru as printed (U1 Aa11 D36 P8 G43 A2 etc.).


## This part — things to look at closely (do not assume; code exactly what you see, name doubtful shapes in "unsure")
Every sign of every word, but especially: unt / reṭ (legs, walking); Seker; qerert (the cavern sign); Neter-χert;
the "Leg of heaven" uart; χu and χakeru; Teḥuti; the eye signs (maat, D4 vs D10); ānχ; āba / àmmehet; ḥesq (knife);
Suti (Set); setet / seṭeṭefu (arrows); nemmat; ḥeka; Budge's "(sic)" on p. 120 row 4 and p. 122 row 5 (say exactly
which sign it stands beside); every overline (chapter titles, "t'eṭ àn"); Budge's [ ] in the hieroglyph line (p. 119,
p. 120, p. 121, p. 122: many). Ani's determinative (A1 / A52 / A2 as printed); maāχeru; any sign with no good code.
