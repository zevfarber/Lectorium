# Reader brief — ani-001-b (Budge 1895, Plates V–VI, Spell 1 second half, pp. 20–24)

You are one of two INDEPENDENT readers establishing a hieroglyphic text from page scans of Budge's 1895 interlinear
edition of the Papyrus of Ani. Do not look at any other reader's file in drafts/ani-001-b/readers/ other
than your own. Do not consult any translation of the Book of the Dead; work only from the page.

Source: /home/user/Lectorium/.github/pipeline/ani/source/raw/budge1895.pdf — PDF page = printed page + 164
(p. 20 = PDF 184, p. 21 = 185, p. 22 = 186, p. 23 = 187, p. 24 = 188). Render with
  python3 /home/user/Lectorium/.github/pipeline/run3/page.py <pdf> <pdfpage> --zoom 1 --out <scratch>/x.png   (whole page)
and zoom into ONE printed row at a time with --zoom 4 --clip x0,y0,x1,y1 (points of the unzoomed page; the page is
1164 x 1545 points). Look at each row image with the Read tool. PyMuPDF is installed (python3).
Your scratch directory: /tmp/claude-0/-home-user-Lectorium/acd391db-aa6c-5b56-aa64-d7e06e734af6/scratchpad/<your-reader-id>/

## What to read (whole part; your task names which pages are yours)
- p. 20: ONLY the last three groups of the LAST row: nuk / Ṭetṭeti / se ("I am Tetteti, the son of"), Plate V l. 13
  (check the line numeral in force). Everything before them on p. 20 is OUT (previous part).
- pp. 21–22: every row (Plate V, ll. 14–30; p. 22 ends "baiu / souls").
- p. 23: heading "PLATE VI." — every row from "31." (menχu em pa Àusàr …); plate = "VI" from here on.
- p. 24: every row to the end of the chapter, the last row "sesu-θà em sep-[f] / have been emptied of [his] trial."
  Below the rule at the foot of p. 24 nothing belongs to this part.
- Footnotes: p. 21 n. 1 (variants of the group before Reχtet, printing hieroglyphs: British Museum papyrus 9964,
  Lepsius Todtenbuch, Birch) and p. 23 n. 1 ("We must read …" followed by hieroglyphs) are OUT as words: report them in
  brief in "footnotes" (describe the hieroglyphs of n. 1 on p. 23 as codes if you can, since it corrects the text).
  The superscript numerals that call them are not signs.
- Budge's "...." in a transliteration (e.g. "....Reχtet", ".... set", ".... tu") means he leaves something unread:
  code every sign printed above it anyway and say so in "unsure".
- Square brackets in the hieroglyph line (e.g. around signs in hesb neter … on p. 24, and the [f] of sep-[f] at the end)
  = Budge's restorations: "restored": true, and say in "unsure" which signs are inside the brackets. Brackets only in
  his English (e.g. "[on] the day") are NOT restorations of signs: ignore them.
- Rubric overlines: several rows on pp. 22–24 have a line ruled over part of the row (e.g. p. 22 last row from "à
  setekeni", p. 23 rows of ll. 34, 35, 37, 38…). Check each row for an overline and mark exactly the words under it.
- Small crosses / "x" marks printed between groups (e.g. after χefta-f, in ll. 17–18 and elsewhere) — say whether
  each is a sign (e.g. Z9 / determinative) inside a word or a separate mark; code it inside the word if it belongs
  to the group above a transliteration.

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
- Repeated words: semaāχeru Àusàr er χefta-f (several times), Teḥuti, ḥenā Ḥeru, hru, Tettetu, Re-stau, menχu,
  pa Àusàr, maāχeru, ḥenā-ten, Àn Àni, the -ten suffix (N35 + X1 + Z2 or similar), the sḏm·f forms with -f.
- Code what is printed at every occurrence, even of a word you have already coded: the type varies.
- Unusual groups: àakebit, Reχtet and the group before it, Teśteś, tephetu, urt āb, seśet, Seχem, ābet, Ṭenàt,
  Rere, segai, seśet ḥebet, χerp āb, ertāt ḥennu, māχait, χebasi, Suten-ḥenen, setekeni, ṭāṭāiu, tràui, Àbṭu,
  uniu, àpui, mātennu, ḥesb, gementu, māχat, sesu-θà, sep.

## Output
Write ONE JSON file (path given in your task):
{"reader": "<id>", "pages": [first, last], "words": [...all words in order...], "gaps": [...],
 "footnotes": ["p. 11 n. 1: An interesting variant …", ...],
 "notes": "anything about the section boundaries, layout, line numerals, damaged or odd print"}
Use a script (python json.dump, ensure_ascii=False, indent=1) to write it. Be complete: every word of every row in your
page range, in order. Zoom in, one row at a time, at zoom 4. Accuracy of every sign matters more than speed.
