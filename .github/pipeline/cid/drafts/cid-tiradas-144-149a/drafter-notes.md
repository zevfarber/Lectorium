# Drafter notes — cid-tiradas-144-149a

35 units, 81 verses (3329–3408, including Pidal's own 3359b), tiradas 144–149. Tirada 149 runs on into the next
part: this part stops at v. 3408, the end of the Çid's reply to the envoys. The next line, v. 3409 (Levantós el rey,
fizo callar la cort), and the rest of the rubric (Minaya's challenge, Gómez Peláez, the gifts, the lost folio) belong
to the next part. The last note says so.

`t` was cut by a script from packet.md: scratchpad `d144/build_144.py`, which reads `d144/units_src.py`
(/tmp/claude-0/-home-user-Lectorium/e5b3c394-3c1d-54ee-9e32-a6454f702641/scratchpad/d144/). Each unit is given
as its first and last verse id, and `t` is those packet lines joined by "\n". The script asserts these points:
- all 81 packet verses are used once, in order;
- each unit has 1–4 verses;
- no unit crosses a tirada break;
- the `l` line count equals the `t` line count;
- `i` and `n` have no newline;
- the JSON parses.

The title is the parts.json name: "Martín Antolínez and Muño Gustioz challenge; envoys of Navarre and Aragon arrive".

The scan was rendered with python3.13, since python3 (3.11) lacked PyMuPDF when I started.

## Rubrics as read on the scan (small caps)
- 144 (PDF 337): "Prosigue el reto de Pedro Vermúdez."
- 145 (PDF 339): "Diego desecha la inculpación de menos-valer."
- 146 (PDF 340): "Martín Antolínez reta a Diego González."
- 147 (PDF 340): "Asur González entra en la corte."
- 148 (PDF 341): "Asur insulta al Cid."
- 149 (PDF 342): "Muño Gustioz reta a Asur González.—Mensajeros de Navarra y de Aragón piden al Cid sus hijas para
  los hijos de los reyes. Don Alfonso otorga el nuevo casamiento.—Minaya reta a los de Carrión. Gómez Peláez acepta el
  reto, pero el rey no fija plazo sino a los que antes retaron.—El rey amparará a los tres lidiadores del Cid.—El Cid
  ofrece dones de despedida a todos.—(Laguna. Prosa de la Crónica de Veinte Reyes.) El rey sale de Toledo con el Cid.
  Manda a éste correr su caballo."
  - The 3392–3408 part of this rubric matches only "Muño Gustioz … casamiento". The first note quotes the whole rubric
    and says the rest belongs to the next part.

Assonances, worked out from the text:
- 144: ó (ó-e in varones);
- 145: í-o;
- 146: á (á-e in dexastes, valen);
- 147: á-o;
- 148: á;
- 149: ó (ó-e in Simen[ones]).

## Footnotes read (all quoted in the notes with an English gloss, or summarized in English where they are long)
- PDF 337: 3329, 3330.
- PDF 338: 3336, 3339, 3343, 3344, and 3350, which runs on to PDF 339.
- PDF 339: 3354, 3355, 3356, 3359, 3360.
- PDF 340: 3365, 3366, 3367, 3373.
- PDF 341: 3377, 3379, and 3380, which runs on to PDF 342.
- PDF 342: 3385.
- PDF 343: 3394, 3400.

Long notes were handled as follows:
- 3350: I quoted the first part and summarized the rest in English.
- 3377: I quoted the paraphrase and summarized the rest.
- 3379: I quoted the paraphrase and first sentence and summarized the rest.
- 3380: I quoted the definition of maquila and summarized the argument. Its bibliography (Koehne, Luchaire, Fuero
  Viejo, Fuero de León) is left out.

Paragraph indent seen at 3392 (Assí commo acaban), and the note says so.

## Readings for the reviewer to check
1. **3350 footnote accents** (zoom 4–5): the first "debia" (PDF 338) and "tenia" (PDF 339) look unaccented, and the
   second "debía" looks accented. The note quotes them that way and says so. In the unquoted rest, "desmentía" seems
   accented, while "decia" and "menti" seem unaccented.
2. **3377 footnote**: I read "diría", "habíamos" and "mío Cid" as accented, and quoted them that way. "concebian" is
   unclear and lies in the summarized part, so it is not quoted. "tenía" looks accented.
3. **3343 footnote**: "era fórmula" begins with a small e after a full stop, as printed. The note says so.
4. **3355 / 3400 footnotes**: the headwords "aparecidos" and "bendición" are printed without the cedilla. The notes
   say so.
5. **3360 [venidos] and the footnote "mismos, ripio, igual que en 847"**: the footnote glosses a word that the printed
   line does not have. Perhaps the manuscript reads mismos and Pidal replaced it in italics with venidos, but the page
   does not say so. This is flagged as uncertain in the note and needs a check against Pidal's apparatus or the
   1908–11 edition if the house has it.
6. **3341 a sos vassallos, víolos**: I read this as the object put first and taken up by los, following the comma
   after Campeador. The alternative, "turned back to his vassals", is mentioned in the note.
7. **3371 de quando dicho has**: I read quando as standing for quanto ("all that"), as in 3313 and 3351. It is printed
   so.
8. **3378 darie nuevas**: "would give us renown", following Pidal's 'recibir nobleza'. The `i` is "Who would have
   thought we should get our renown from my Çid".
9. **3379 F[o]sse**: I took this as fuesse (imperfect subjunctive of ir) used as a scornful wish, following Pidal's
   'Váyase'. Whether a reflexive se is run in is left open.
10. **3379 picar los molinos**: I glossed it as "dress the millstones" (roughen them with a pick). This is my gloss of
    the trade word, and Pidal gives only 'picar sus molinos'.
11. **3381 Quil darie … a casar**: "who would let him marry into the house of Carrión" is our reading. Pidal gives no
    separate note.
12. **3385 fártaslos**: "you glut them, sicken them" (fartar). Reading this as his food-and-wine breath at the kiss of
    peace is our interpretation. Pidal glosses only das paz 'besas'.
13. **3394–3396**: the note says that without Pidal's italic words the two knights would read as the princes
    themselves. This is my account of what the restorations do, and Pidal does not say it in so many words.
14. **3375 almorzado**: "had breakfasted". The flushed face from food and wine is inferred from v. 3384 and stated as
    the poem's joke.
15. **3331 y**: I took it as 'and', as with i in v. 2 of the pilot.
16. **3335**: there is no OCR text, as the packet flags. I used the established text as pinned and did not re-read it
    on the image beyond the 1.4 page view, where it reads as pinned.

Cross-references checked in source/established:
- 675;
- 847;
- 1376;
- 1881;
- 1906;
- 2080;
- 2084;
- 2172–73;
- 2278–2301 (the lion);
- 2546;
- 2555;
- 2683;
- 2908.

Pidal's forward references (3418, 3421, 3442, 3644, 3667, 3691, 3702, 3705, 3721) are quoted and not expanded.

## Proposed new house renderings (for conventions.md)
- alevoso: "treacherous-one" in `l`, "treacherous man" in `i`. It is kept apart from traidor "traitor", since both
  occur in v. 3383 (alevoso, malo e traidor).
- lidiar of a charge (esto te lidiaré, yollo lidiaré, esto lidiaré): "I-will-fight" in `l`, "I will maintain (this
  against you) in combat" in `i`. This follows Pidal's note to 3344, 'sustentar por medio de una lid judicial, una
  acusación'.
- otorgar of the defeated man (vv. 3329, 3350): "confess" (Pidal 'confiesa', 'confesarás'). The glossary's "confirm,
  grant" is kept for other contexts.
- Yéñego Simen[ones]: "Íñigo Jiménez" in `i` (Pidal's note to 3394: 'Yéñego, hoy Iñigo'; 'Enneco Semenones (o Iñigo
  Jiménez)'). Ojarra is kept so.
- infante / ifante de Navarra, de Aragón: "Infante" in `l`, "the prince of Navarre / of Aragon" in `i`. This keeps them
  apart from the Infantes of Carrión. Navarra and Aragón become "Navarre" and "Aragon" in `i` and titles.
- rogador / rogadores (vv. 2080, 3395): "asker" in `l`. In `i` it is rendered as one who "speaks for" the suitor, or
  as the go-between who asks for the bride (Pidal's note to 3394).
- rio d' Ovirna: "the river Ubierna" in `i` (Pidal's note to 3379).
- maquilas: "mill-tolls" in `l`, "toll of meal" in `i` (Pidal: grain or flour paid to the miller).
- dar paz: "give the kiss of peace" (Pidal 'besas', note to 3385).
- a ondra e a bendiçión: "in honour and with (the Church's) blessing" in `i`, i.e. as lawful wives (Pidal's note to
  3400).
- Riébtot el cuerpo: "I challenge your body" (Pidal 'te reto tu persona'). It is kept literal because it is the formula
  of the reto.
