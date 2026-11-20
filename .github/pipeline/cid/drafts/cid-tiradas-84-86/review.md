# Review — cid-tiradas-84-86 (tiradas 84–86, lines 1527–1609 with 1573b)

Adversarial review against the pinned packet, Pidal's rubrics and footnotes on the scan (PDF pp. 231–236 at
200 dpi; v. 1557 and v. 1566 cropped at 400 dpi; PDF p. 349 = printed p. 345 for the reference in the note to
v. 1592), conventions.md, the pilot (01-04), the published parts (24-26 for presentaja and Taranz, 44-48, 78-82
for portero, 83a, 83b), the established texts and OCR drafts (for cross-references only), and known-forms.json.
All edits made by script (json load/dump, ensure_ascii=False, indent=1). No `t` changed: the 84 `t` lines
joined with "\n" equal the packet's 84 verses in print order (1527–1583, 1584, 1587, 1585, 1586, 1589, 1588,
1590–1609, with 1573b), checked by script after the edits; one `l` line per `t` line in all 31 units. Longest
note after edits: 950 characters.

## Pass 1 — units.json

Counts: error 3 · weak 4 · style 4 (11 changes)

| unit (index / first line) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 11 / 1555 Otro día manaña | n | error | "de[l]los … the second l Pidal's": on the scan (400 dpi) the first l is italic, the second roman, as the bracket in `t` shows | "the first l Pidal's (in italics)" |
| 23 / 1589 Por nombre | n | error | "the Çid will run Babieca again before the king (v. 3513 and the lines about it)": Pidal's note says p. 345, which is the chronicle prose filling the lost folio after v. 3507 (checked, PDF p. 349), not the verse; and v. 3513 is the Çid speaking (Mandástesme …) | says the run is on p. 345, in the prose Pidal supplies for the lost folio (not given here), and that he compares v. 3513, where the Çid recalls that the king bade him run the horse |
| 0 / 1527 Sorrisós | n | error | "The n of Ave[n]galvón is Pidal's (in italics), as throughout this part": at v. 1532 the name is printed whole, Avengalvón, in roman (scan and `t`) | "as again at vv. 1545 and 1551; at v. 1532 the name is printed whole" |
| 2 / 1532 Dixo Avengalvón | n | weak | Pidal's note is only "presentaja, 'obsequio, agasajo'"; the draft folded its own reading ("here … Minaya's offer of supper, not a gift of goods") into the quotation | Pidal's gloss quoted alone; the reading given as ours and hedged ("most likely"), contrast with vv. 516, 1315 and v. 522 (offer of price, as 24-26) |
| 10 / 1553 aun las ferraduras | n | weak | "las … takes in Minaya with the ladies, drawn to the nearer noun": stated as fact; las may be the ladies alone | both readings given; "the line allows both" |
| 28 / 1603 Oíd lo que dixo | l | weak | "Hear what that said he who": lo que garbled | "Hear that-which said he who" |
| 3 / 1534 Entraron en Medina | n | weak | "Medinaceli is the last town of his realm": a historical claim stated flat | "The poem treats Medinaceli as the edge of his realm" (consistent with the known glossary entry) |
| 1 / 1529 Si Dios me llegare | n | style | Pidal's 1530 note ("Luego omite el poeta referir lo que aquí anuncia; v. p. 85") paraphrased as "leaves untold the reward" | quoted, with "the requital Minaya promises" marked as gloss; p. 85 kept |
| 7 / 1546 El obispo | n | style | "Latin dextrarius": Pidal prints dexterarius | "Latin dexterarius" |
| 18 / 1573 e aduxiéssenle | i | style | "in the rout of him": not English | "at that king's rout" |
| 23 / 1589 | i | style | "so wondrous that when he had run …": adds a result clause the Old Spanish does not have | "it was so wondrous; when he had run, all marvelled." |

Checked and found sound (no change):
- Rubrics against the scan, exact: 84 (p. 227: Los viajeros descansan en Medina. — Parten de Medina a Molina. —
  Llegan cerca de Valencia), 85 (p. 229: El Cid envía gentes al encuentro de los viajeros), 86 (p. 230: Don
  Jerónimo se adelanta a Valencia para preparar una procesión. — El Cid cabalga al encuentro de Jimena. — Entran
  todos en la ciudad); 87 (p. 232, Las dueñas contemplan a Valencia desde el alcázar) matches the last note.
  Assonances á-a / á-o / á-a and the word lists: right. Tirada 85 is six lines (1562–67) and runs on into 86: right.
- 1573b: printed wholly in italics, label "1573b" in Pidal's own margin (p. 230), footnote "1573 b Dudas acerca de
  este verso, p. 85": the note says all three correctly.
- Print order on p. 231: 1584 (unlabelled, indented), 1587, 1585, 1586, 1589, 1588, 1590 (labels 1587, 1585,
  1589, 1588, 1590 printed): the notes to units 22 and 23 state it correctly.
- Footnotes against the scan, wording and numbers right: 1530 (p. 85), 1532, 1534 (2877), 1544 (véase 1492),
  1548 (cheval en destre, destrier; entero y de gran talla; palafré; estribo izquierdo; acémila; Cantar p. 628 and
  Bertoni not carried, harmless), 1549 (Entre pleonástico, 191), 1553 (atención … obligación; herrar el caballo
  del vasallo a quien llamaba a vistas), 1559 ('cerca'), 1576 ('donde estaba en completa seguridad'; 1566, 1471),
  1577 (jugar las armas; 1602, 2243; 2887, 2896; 2613, 2673, 2687), 1581 ('que se habían preparado (v. 3058-59)
  con tiempo' (?); Bello 'juntarse a rezarlas', arbitrariamente; Hinard 'qui arrivèrent à l'heure'), 1587
  (voz desconocida; gonela o túnica de seda; Fernando II; p. 108), 1592 ('al terminar la carrera'; corrida 1588;
  eslai; Tencendur, Baligant, Roland 2997, 3166; novel caballero), 1602 ('jugaban las armas (v. 1577) y
  quebrantaban tablados'; castillejo de tablas). "No note" claims: none made falsely.
- Italics on the scan, all matching `t` and the notes: Ave[n]galvón (1528, 1545, 1551), [a] 1533, tomara[n],
  sacara[n], T[a]ranz, Jero[me] (1546, 1579), aguarda[va], su[e]s (1548, 1593), su[e] 1570, alcáç[e]r, de[l]los,
  buen[a] [çinxo espada], mandád[ol] [leva]van, f[o] (1562, 1588, 1591), Doz[ien]tos, [estava], acordara[n],
  desca[va]lgava, pie[de]s, [e] 1597, [cr]ebanta[van], buena [çinxo espada], [doña Ximena], mi[o].
- Cross-references checked in the established texts: 1 (De los sos ojos), 191, 516, 522, 1161, 1222–30, 1226,
  1356, 1380 (Pidal's note there cites 1536–39, as 78-82 says), 1407, 1470–72, 1488, 1491–93, 1494, 1499, 1508,
  1518, 1520–26, 2877, 3058–59, 3513.
- Grammar labels checked and right: sorrisós, sodes, llegare (future subjunctive), vea, perderedes, plazme,
  daré, sirvíalos, tomara[n]/sacara[n] (-ra pluperfect), quitar, quito, venida es/oída es, entrados son, sirvié,
  ovieron, gelas, despendié, f[o], yál, reçiban (present subjunctive after past), sedíe (imperfect of seer),
  guardassen, aduxiéssenle, avié, quel, serié, abrié, querié, reçebidas (absolute), salién + infinitive, nasco,
  vistiós, ensiéllanle, ovo corrido, se preçió, cinxiestes (2nd pl. preterite), sacada me avedes (agreement),
  afeme, avíen, tenien, comigo, he ganada (agreement with heredad).
- House renderings: "in a good hour girded on his sword" / "born in a good hour"; Minaya Álvar Fáñez and Álvar
  Fáñez in `i` (Álbar kept in `l`; the reversed "Álvar Fáñez Minaya" of v. 1527 as at 19-23); my Çid, the
  Campeador, Don Jerome, Doña Ximena, Avengalvón, Medinaceli, the Jalón, the Arbujuelo, Taranz, as in earlier
  parts. Bavieca first named here; `i` gives Babieca (the modern form, as Medinaceli/Jalón).
- `l` ↔ `i` unit by unit: sense and force agree after the changes; no remembered English found.

Findings refused:
- 1566 sedíe: the drafter asked whether the print lacks the accent. At 400 dpi the i of sedíe carries a clear
  slanted acute (a stroke, not the round dot of the i's in bien, Valençia nearby). The pinned sedíe is right.
- 1528 amigol, 1538 Medinal, 1544 luégol: each read as noun/adverb + le and each already said to be uncertain in
  the note; no better reading from Pidal's notes (he gives none). Kept.
- 1554 las: hedged (above), not changed to a single reading.
- 1581 oras: the note follows Pidal and reports his query, Bello and Hinard correctly. Kept.
- 1587 sobregonel 'surcoat': flagged in the note as a guess, as Pidal calls the word unknown. Kept.
- Unit 6 `i` "then crossed" for luégol 'at once': the note gives 'at once'; "then" is within the sense of a
  sequence of stages. Kept.
- Unit 18 `l` "little it-had-been" for poco avié: literal enough for impersonal aver. Kept.

## Pass 2 — gloss.json

Counts: error 10 · weak 13 · style 3 (26 changes, 3 of them new broadens)

| entry | sev. | what was wrong | what was done |
|---|---|---|---|
| amigol | error | "fairly sure, the alternative 'el' is not possible": contradicts the note (uncertain) and is unfounded | "the le read as the Cid … the reading is not certain" |
| luégol | error | "Pidal's accent luégo marks the stress": no form luégo; leísmo stated flat | accent explained (stress stays on lué-); le "probably" el campo, "not certain" |
| mandádol | error | "the final -o stressed by Pidal" (the accent is on á); "Pidal's reading of a damaged line" invented | stress on -dá-; "the ol is Pidal's restoration" |
| oras | error | "they had agreed on the hours, i.e. ready for the office": Bello's reading, which Pidal calls arbitrary; against the note | con oras 'in time', Pidal's queried reading; Bello's rejected |
| acordaran | error | "they had agreed, were in accord … = se habían acordado": not Pidal's 'se habían preparado' | 'made ready', Pidal's gloss with his query, compare v. 3059 |
| tablados | error | "wooden board, target … spear-throwing game": Pidal: a little castle of boards struck with lances to bring it down | rewritten from Pidal's note |
| crebantavan | error | "Pidal's cr[e]bantavan": the restoration is [cr]ebanta[van] | corrected |
| tenien | error | 'they held arms': here tener las armas = 'play at arms' (Pidal, vv. 1577, 1602) | 'played at arms', Pidal's gloss |
| sorrisós | error | "sorrisar survives as sonreírse": invented descent; = sonrió omits the reflexive | lemma sorrisar(se), = se sonrió, compare sonrrisándose (v. 1518) |
| llegare | weak | "= llegue": after si modern Spanish uses the present indicative | "modern si + present indicative, si Dios me lleva" |
| despendié | weak | "paid his own expenses" (he spent of his own on them); "despender is lost" | "spent of his own"; "survives only as a rare word" |
| sedíe | weak | "imperfect 3rd sg. sedié": the form glossed is sedíe | printed sedíe, stressed on the í |
| abrié | weak | "Latin habere + habebat contracted abrié": muddled | infinitive aver + imperfect ending -ié |
| sobregonel | weak | "sobre + gonel": Pidal says gonela and calls the word unknown | gonel(a); Pidal's words added |
| maravillavan | weak | "without the reflexive se": the line has se maravillavan | "with se, maravillarse" |
| preçió | weak | "= se preció / apreció": modern se preció means 'prided himself' | "= fue apreciado", with the warning |
| merced | weak | "'have mercy', a plea of respect": here thanks (as the note says) | "mercy, thanks … suppliant or of thanks" |
| avíen | weak | "= tenían, había": wrong number | "= tenían, habían" |
| __broaden__ quito | weak | "= libre, quite": quite is not the Spanish adjective | "= libre, exento" |
| __broaden__ diestro | weak | "en diestro — led by the hand, at the bridle": Pidal: led at the knight's right | "led unmounted at the rider's right hand", Pidal |
| manaña | style | "ñ not marked n-tilde": confused | "so printed, the first n without the tilde" |
| ésta | style | "pronoun/adj., accent only a mark of Pidal" | "demonstrative pronoun, accented in Pidal's print" |
| deleyt | style | "Latin delectum": doubtful etymology | dropped |
| __broaden__ corrida (new) | error | known entry 'raid, foray' does not cover fizo una corrida, the display gallop (Pidal's 1592 note) | broadened: old entry whole + " · also corrida — a run, a display gallop …" |
| __broaden__ tener (new) | weak | known 'to hold, keep' does not cover tener las armas (v. 1577) | broadened with Pidal's 'jugar las armas' |
| __broaden__ presentaja (new) | weak | known 'gift; offer of price' does not cover 'obsequio, agasajo' (v. 1532) | broadened with Pidal's gloss |

Broadens checked: every value in __broaden__ (now 10: quito, mandava, quitar, diestro, avié, una, del, corrida,
tener, presentaja) begins with the known entry whole + " · also ", checked by script. Kept as needed: quito (adj.
'free of debt'), mandava ('ruled'), quitar ('to settle'), diestro (en diestro), avié (poco avié que), una (a una),
del (cause). del is borderline (de of cause is covered by the de entry) but harmless.

Checked and found sound: the other 66 novel entries (lemma, grammar, meaning, example, modern form), including
perderedes, adobada, sirvíalos, tomaran, sacaran, medinal (hedged), passada/venida/oída, aguardava, hivan,
ferraduras, ondrança, curiando (no modern form, closest cuidar), guardassen, aduxiéssenle (modern aducir
'adduce' only), corredor, ssi, parada, capiella, sobrepelliças (= sobrepellices), salién, vistiós, ensiéllanle
(ensellar, modern ensillar), fuste, des, quant, cosso (= coso), sacada, afeme (= heme aquí), criadas, querida.
Known entries otherwise cover their uses here (sobrél 'over him', echava 'throwing himself', cabo 'end', salvo
'safe keeping', fo, a, de, en, le). Key set of gloss.json minus __broaden__ = the 86 keys of novel-forms.json
(script).

Findings refused:
- que in que nunqua más nin tanto ('as never …'): not separately covered by the que entry, but the sense is
  carried by the note; a broaden for one idiom of this kind left to the owner's taste.
- capiella "diminutive, Latin cappella": loose (cappella is itself the diminutive) but not wrong. Kept.

## Verdict on the text points
- 1566 sedíe: the pinned reading looks right; the acute is printed (400 dpi crop).
- 1557 de[l]los: the italic l is the first, as pinned.
- 1573b wholly italic, label Pidal's; print order 1584, 1587, 1585, 1586, 1589, 1588, 1590 confirmed on the scan.
- 1595 cinxiestes printed with plain c, as pinned; 1532 Avengalvón printed without italics, as pinned.
- No reason found to change any `t`.
