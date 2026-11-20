# Reader brief — ani-022-072 (Budge 1895, Plate VI, Spell 22 and the rubric of Spell 72, pp. 25–27)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-022-072/readers/ other
than your own, nor at any other part's reader files. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 25 = PDF 189, p. 26 = 190, p. 27 = 191). Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page; check the page
size first). Look at each row image with the Read tool. PyMuPDF is installed (python3).
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/129e82a3-f9cf-51e6-8298-54a5745055b9/scratchpad/<your-reader-id>/

## What to read (whole part)
- p. 25: every row, from the first row (Chapter XXII's title "Re en ertāt re en Àusàr …", overlined) to the last row
  ("em Śe nesert … χenti"). Plate = "VI" throughout this part (the page head of p. 26 says Plate VI).
- p. 26: every row of Chapter XXII down to "nebṭet ḳerḥ / of fire and night." (its line 10); then, below the short
  rule, the Rubric of Chapter LXXII (it begins "Àr reχ śāt ten …" with its own numeral "1.") to the last row
  "… śenār - tu - f / shall he be repulsed." Below the long rule is footnote 1 ("Read … re pen, 'this chapter'?"):
  OUT as words; report it in "footnotes" with the codes of the hieroglyphs it prints. Its superscript "1" (after
  the group "pu") is not a sign.
- p. 27: every row from "3. àu ṭā - tu nef …" to "… àu Àusàr ān Ani / Osiris scribe, Ani." STOP above the heading
  "PLATE VII." — nothing from "PLATE VII." on belongs to this part.
- line = the small bold numeral in force as printed. Budge restarts his numerals: Chapter XXII runs 1.–10.
  (words before "1." on p. 25 are line 1), then the Rubric restarts at 1. (p. 26) and runs to 7. (p. 27).
  Record the numerals exactly as printed; add "section": "XXII" or "LXXII-rubric" to every word.
- Square brackets in the hieroglyph line (e.g. around signs in ḥesb neter on p. 25, [uà] and [àritu-s] on p. 26)
  = Budge's restorations: "restored": true, and say in "unsure" which signs are inside the brackets. Brackets only in
  his English are NOT restorations of signs: ignore them.
- Rubric overlines: many rows have a line ruled over all or part of the row. Check every row and mark exactly the
  words under the line with "rubric": true.
- Small crosses / "x" marks printed in groups (after -f, -tu, in χesef, etc.) — code them as signs inside the word
  (Z9 or the nearest code) when they belong to the group above a transliteration; say so in "unsure" if unsure.
- "(sic)" printed over a group (p. 25, tep-f (sic)) — keep "(sic)" in "budge" as printed and note it.
- The asterisk-like marks before "4." (p. 25) and "7." (p. 27) — say whether they are signs (e.g. N14 star in ṭuat)
  belonging to the next word.

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
- Repeated words: Àusàr, ān, Ani, maāχeru, re-à, t'eṭu-à, àm-f, em, neb, tep ta, àu-f, ṭā-tu nef, neteru.
- Code what is printed at every occurrence, even of a word you have already coded: the type varies.
- Unusual groups: Neter-χert, uben-kuà, suḥt, àmt ta śeta, χesef-tu, ā-à, t'at'at, Re-stau, peseś, ennu, enti, tep-f (sic),
  χet, merer, Śe nesert, āχem-nà, ànet' ḥrà-k, neb seśep, χenti, ḥet ḥert, keku samau, χu-k, āb-kuà, āāui-à, ḥa-k, tenà-k,
  tepu-ā-k, unnut-f, nebṭet, ḳerḥ, reχ, śāt, àritu-s, ānu, qeres, χeperu, mer-f, āq, àuset, śenār-tu-f, heq, ur, àuf,
  χaut, Seχet-Àaru, utu, Ṭeṭṭeṭ, pert, beti, unen, uat', enen, śes maā, ḥeḥ en sep.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...], "gaps": [...],
 "footnotes": ["p. 26 n. 1: Read …", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.
