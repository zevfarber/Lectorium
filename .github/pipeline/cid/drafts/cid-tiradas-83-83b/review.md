# Review — cid-tiradas-83-83b (tirada 83, second part, lines 1453–1526 with 1492b, 1494b, 1499b)

Adversarial review against the pinned packet, Pidal's rubric (PDF p. 223) and the text and footnotes on the scan
(PDF pp. 227–231 read at 300 dpi, with crops of vv. 1471, 1475–76, 1491–96, 1499–1507; v. 1494 also at 600 dpi;
Pidal's introduction p. 105 = PDF p. 109, for the reference in his note to v. 1509), conventions.md, the pilot
(01-04), the published parts (32-34 for virtos, 69-74 for hart, 44-48 and 78-82 for names, 83a), the established
texts of earlier parts and the OCR drafts of later ones (for every cross-reference only), and known-forms.json.
All edits made by script (json load/dump, ensure_ascii=False, indent=1). No `t` changed: the 77 `t` lines
concatenated with "\n" equal the packet's 77 verses (1453–1526 with 1492b, 1494b, 1499b) in order exactly, checked
by script before and after the edits; one `l` line per `t` line in all 28 units.

## Pass 1 — units.json

Counts: error 3 · weak 4 · style 7 (14 changes)

| unit (index / first line) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 15 / 1494 E en Medina | n | error | "the number 1494b is his": Pidal prints no label beside the italic line (margin labels on p. 225 are 1490, 1492b, 1495); by the conventions the b-letter of an unnumbered italic line is ours | "He prints no number beside it: the label 1494b is this edition's provisional letter after the preceding line, not Pidal's" |
| 12 / 1487 Dixo Ave[n]galvón | n | error | "Minaya's answer to the abbot at v. 1448": Respuso Minaya: “fer lo he de veluntad.” is v. 1447 (1448 is Yas espiden) | v. 1447 |
| 17 / 1499 afevos aquí | n | error | afevos referred to "(v. 1432)": v. 1432 is “Merçed, Minaya, cavallero de prestar!”; afevos is at v. 1431 | (v. 1431) |
| 3 / 1462 por Santa María | l, n | weak | `l` "by Santa María you are-to pass" drops the reflexive vos and turns vayades + passar into one verb; note "vos … passar, 'pass through'" | `l` "by Santa María yourselves you-are-to-go to-pass,"; note: ir with the reflexive vos and a bare infinitive, 'go on your way and pass (by it)' |
| 20 / 1507 Bien salieron den çiento | l, i, n | weak | den taken as partitive 'of them' only, against den = de + ende 'thence' (known-forms: 'from there, from it'), which the reader's tap shows; they ride out of Medinaceli | `l` "went-out thence"; `i` "Fully a hundred rode out from there"; note gives 'thence', the partitive as also possible |
| 17 / 1499 | n | weak | "(Pidal reads the word as art where it appeared before)": vague, and no place named | names v. 1204 (non i avía hart) and Pidal's note there: sin art 'without deceit', then 'perfectly' (as 69-74) |
| 13 / 1488 Essa noch | n | weak | "they asked him for a hundred knights (v. 1465)": v. 1465 is the Çid's plan; the asking is Muño Gustioz's message at v. 1483 | (v. 1483) |
| 20 / 1507 | n | style | Pidal's "Sobre el escudo al cuello, v. p. 105" paraphrased with "ready for use", not on p. 105 | p. 105 (introduction, checked on the scan): the shield hung at the neck by a strap (tiracol o correa), gripped against the heart, still hanging there, to charge |
| 1 / 1457 Qui buen mandadero | i | style | "may look for the like" weakens deve ('must, ought') | "should look for the like in return" |
| 14 / 1491 Passan las montañas | i | style | "in such good order that they have no fear": "good order" added to de tal guisa que | "in such a way that" |
| 14 / 1491 | n | style | "Pidal numbers the middle line 1492b": the unit has four lines; and Pidal's note to v. 1492 gives v. 1544 for campo de Taranz | "the line de tal guisa … 1492b (the label is printed in his margin)"; "which the poem elsewhere calls campo de Taranz (v. 1544)" |
| 15 / 1494 | n | style | Pidal's note to v. 1494 reads "comp. 1511, 1567"; 1511 (in this part) dropped | "(compare vv. 1511, 1567)" |
| 16 / 1497 el uno fincó | n | style | Virtos treated as new, though it stood at v. 657 (creçen estos virtos, 32-34 'hosts') | "as at v. 657 (creçen estos virtos)" |
| 24 / 1517 Quando llegó | i | style | "When Avengalvón came up and has him in sight, he went": the present inside one English clause reads as a slip | "had him in sight" |

Checked and found sound (no change):
- Rubric (p. 219 of the print, PDF 223): the first note quotes the second half (Pedro Vermúdez parte de Valencia para
  recibir a Jimena. En Molina se le une Avengalvón. Encuentran a Minaya en Medinaceli) exactly. Assonance á with á-e
  counting: right. The tirada ends at v. 1526; tirada 84 (Sorrisós de la boca …) begins on p. 227 in á-a: right.
- Footnotes against the scan, wording and numbers right: 1461 ('para las necesidades de lidiar', 'como para lid',
  1695; comp. 1374 y 123), 1462 (Albarracín; Santa María del Oriente de Andalus / del Occidente o del Algarve;
  Aben Razín; 2645; 'porque la poseía …'), 1475 (Bronchales, 25 km, Teruel rayano con Guadalajara, 45 km, una
  jornada, v. 2877), 1491 (montes de Luzón 2653, Lusones, Estrabón, 'los robledales y pinares …'), 1492 (campo
  Taranz, 'una llanura pedregosa …', Soria y Guadalajara), 1493 (riachuelo afluente del Jalón … 1543, 2656; "y p.
  28" not carried, harmless), 1494 ('hay toda clase de precauciones'; 'desde Medina se divisa …'), 1501 (coranado,
  1993, coronado 1288, 1460, 'clérigo'), 1502 ('alcaide', 'el que tiene a su cargo una fortaleza', 1464, 1545),
  1509 ('antiguamente se adornaban …'), 1513 ('explorar, reconocer el terreno'; batidores … Pero Vermúdez y
  Avengalvón), 1514 ('comienzan a deportarse'; 'solazarse con ejercicios corporales'), 1519 ('le besa en el
  hombro'; 3030 saludar 'besar'; Boabdil; Roland 601), 1523 (auze 'ventura, dicha', 2366). "Pidal gives no note"
  on conssigrá (p. 223), on tal (1457) and on Virtos: right — no such notes on pp. 223–227.
- Print points on the scan: 1471 seríe (acute on the i, clear); 1476 viniéron (acute over the e; vinieron at 1475);
  1494b wholly italic (vídolos … Fáñez, the whole line slanted; Alvar's A not certainly accented); 1499 doz delant
  italic, label 1499b printed; 1500 Martin unaccented; 1503 óndral (acute over a damaged o); 1505 printed beside
  Esso ffo (by count 1506), with 1500, 1510 and the notes to 1501, 1502, 1509 fixing the count: the notes say all
  this correctly. Italics confirmed: Vermudoz, Jerome, Avengalvón (n), con, desí, Taranz (a), Arbuxuelo (ue),
  sopiessen, detardan, sues, vayamos (second a), ffo (o), traen, quomo (o), lo (1517), so (1519), far (1524),
  Fronchales (chales).
- Cross-references checked: 123, 1288–1303 (Jerome made bishop), 1374, 1382, 1396 (Omillom), 1401, 1403, 1405–12,
  1409, 1432 (de prestar, unit 2), 1464, 1527, 1543–45, 1567, 1695, 1993, 2366, 2645, 2653, 2656, 2877, 3030.
- Grammar labels checked and right: Direvos (future + enclitic), plógol, tornós a, conpeçó de, cavalguedes and
  vayades (present subjunctive as command), tiénela, conssigrá (read as future, hedged), id, pudiéredes (future
  subjunctive), aduzídmelas, costadom ha, seríe, desenparás (imperfect subjunctive 1st sg., apocopated — cf. the
  known spidiés), Troçieron, vinieron albergar, saliólos reçebir, saludava (imperfect of a message), mandólo,
  privádol, acorrades, adugades, gelas, partades, fer lo he, çientol, temiós, sopiesse[n], ff[o], nos = non se,
  saliera (-ra pluperfect), ivan mesurando (ir + gerund), tómanse a, hivalo, ondrar vos hemos, queramos, gelo,
  abrá, muchol.
- Names in `i`: Minaya Álvar Fáñez / Álvar Fáñez (Albar/Alvar/Álbar kept in `l`), Per Vermudoz, Muño Gustioz,
  Martín Antolínez (also for the unaccented Martin of 1500), Don Jerome, Avengalvón, Medinaceli for Medina (as
  78-82 and 83a), Valencia, Vivar, my Çid, the Campeador, Bronchales, the Jalón for Salón (Pidal's 1493 note).
- `l` ↔ `i` unit by unit: sense and force agree after the changes; no remembered English found.

Findings refused:
- 1471 desenparás as 1st sg. ('if I abandoned it'): could be 3rd sg. ('if one abandoned it'), but the Çid is
  speaking of his own staying; the 1st sg. is the natural reading. Kept.
- 1503 de grand óndral dar: le = the Çid (as `i`) or Minaya's party; the note already says so. Kept, listed below.
- 1488 `i` "a great feast" for conducho … grand: free but within the note's 'here a lavish supper'. Kept.
- 1482 `i` "charged us to ask this of you": adds "us", but the sense of mandólo recabdar is kept. Kept.
- 1457 note on tal ('the good news that comes back'): interpretive, but hedged ("The exact point of tal is not
  certain"). Kept.
- 1479 amigo natural as 'true friend': natural in its 'by nature, bound' sense, as the note explains. Kept.

## Pass 2 — gloss.json

Counts: error 5 · weak 11 · style 14 (30 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| desenparás | error | "future 2nd sg. after si, 'if you abandon it', generic 'one'": the future would be desenpararás; the form is the imperfect subjunctive desenparasse apocopated, as the unit says | "(if) I abandoned … (imperfect subjunctive 1st sg., desenparasse with the final -e dropped; = desamparase)" |
| direvos | error | "infinitive dezir + enclitic vos + auxiliary, split future: direvos for dezir vos he": direvos is the synthetic future diré with vos after it | "future 1st sg. diré + enclitic vos, the pronoun set after a verb that opens the line" |
| fronchales | error | "taken to be Fronchales in the Sierra de Albarracín … not certain; = Fronchales": Pidal's note to v. 1475 identifies it as today's Bronchales | Bronchales, Teruel, on the Guadalajara border, 25 km from Albarracín, a day's ride from Molina (Pidal); -chales his restoration |
| conssigrá | error | "the sense 'accompany' is Pidal's reading": Pidal has no note here; "e of the stem syncopated": the vowel lost is the i of the infinitive (conseguirá > consigrá) | syncopated future consigrá for conseguirá; sense read from the context, Pidal giving no note |
| mesurando | error | "keeping measure, going at a restrained pace … exact sense uncertain", against Pidal's note to v. 1513 ('explorar, reconocer el terreno'), which the unit follows | 'scouting, reconnoitring', Pidal quoted |
| troçieron | weak | lemma "trocir" (the form has ç; known troçir, v. 307); example misquoted "troçieron Santa María"; "the reading 'pass' is Pidal's", no such note | troçir; Troçieron a Santa María; cf. tres an por troçir; attribution cut |
| mata | weak | "brush-land near Taranz (Guadalajara)… the placing is the usual one": not Pidal's account | Pidal's note to v. 1492: today's campo Taranz, a stony plain over the head of the Arbujuelo valley, Soria / Guadalajara |
| coranado | weak | lemma coronar 'crowned'; example "obispo coranado 'tonsured bishop'" not in the text (coranado leal) | coranado, variant of coronado used as a noun, Pidal 'clérigo'; coranado leal |
| ombro | weak | "a salutation by touch": Pidal's note to v. 1519 says a kiss on the shoulder | Pidal's 'le besa en el hombro' |
| saluda | weak | the entry gives only 'greets'; the line's sense (Pidal: saludar 'besar') missing | sense 'greets with a kiss' added with Pidal |
| deprunar | weak | 'descend steeply': "steeply" has no authority | 'to go down, descend' |
| avengalvón | weak | "from Arabic ibn Ghalbūn": an unsupported reconstruction | "Aven- = Arabic ibn 'son of'"; lord (alcaide) of Molina |
| __broaden__ recabdo | weak | 'all in order, all well provided' against Pidal's note to v. 1494 | known entry verbatim + " · also todo el recabdo está 'every precaution is taken' (Pidal …)" |
| __broaden__ don | weak | missing: the known entry has no temporal 'when', the sense of Don llegan los otros (unit 23) | added: 'when, where (= donde, of time)' |
| __broaden__ quieren | weak | missing: known 'they wish, are about to' does not cover que vos quieren sin hart 'who love you' | added: 'they love, hold dear' |
| __broaden__ maría | weak | missing: known "Santa María, the cathedral of Burgos" is wrong for v. 1462 (Albarracín, Pidal's note) | added: 'Santa María — Albarracín (Teruel), held by the Aben Razín (Pidal)' |
| levaron | style | "-aron written -aron/-ar-on": meaningless | cut |
| coraçon | style | "final -n form": meaningless | "printed unaccented coraçon" |
| pudiéredes | style | "(as soon as)": quanto here is 'as much as' | "you shall be able"; = pudiereis, modern podáis |
| costadom | style | "m before the next word" | "enclitic me reduced to -m" |
| seríe | style | the print point (accent on the i) not said | added, as the unit |
| viniéron | style | the probable misprint not said | added, as the unit |
| adugades | style | "closest llevéis": aduzir is 'bring', not 'take' | cut (= traigáis) |
| temiós | style | unbalanced parenthesis | mended |
| alcáyaz | style | Pidal's note to v. 1502 not used | Pidal quoted |
| óndral | style | "= honrarle, honra" | "= darle gran honra"; printed accent noted |
| ffo | style | "fo + restored letter" | "the o restored by Pidal: ff[o]" |
| tómanse | style | "accent shifted"; Pidal's gloss not used | "the accent written on the verb's stressed vowel"; Pidal 'comienzan a deportarse' |
| deportar | style | Pidal's note to v. 1514 not used | Pidal 'solazarse con ejercicios corporales' |
| sonrrisándose | style | lemma sonrisar, against the shared glossary's sonrrisar (sonrrisava) | sonrrisar; example added |

Checked: gloss keys (74, excluding __broaden__) equal the novel-forms.json keys exactly. Every __broaden__ value
(7 after the edits: natural, recabdo, tornó, sabor, don, quieren, maría) begins with the known-forms.json entry
verbatim + " · " (asserted by script). All tokens of the 77 lines (brackets stripped, lowercased, apostrophe
splitting) are covered by known + gloss. Other entries checked and right: menssaje, plógol, deve, sperar,
cavalguedes, vayades, iaze, tiénela, dixieron, podredes, aduzídmelas, locura, ffincaré, fincan, moro, speró,
saludava, recabdar, privádol, ffata, partades, çientol, pidieron, montañas, armados, trahe, llegarán, pareçen,
cuberturas, çendales, peytrales, cascaviellos, cuellos, seso, saliera, llegando, toman, homillar, hivalo, husaje,
traedes, valdremos, ondrar, abrá, muchol, torpe, conosçe; broadens natural (natural 'native, true'), tornó
('went back'), sabor (por sabor de). virtos (known, 'forces, hosts', v. 657) fits this line; no broaden.
Gloss and notes now agree on desenparás, conssigrá, troçieron, Fronchales, mesurando, tómanse/deportar, alcáyaz,
coranado, ombro/saluda, recabdo, Don, den (known 'from there', now the unit's reading).

Findings refused:
- conssigrá: whether the verb is conseguir at all: the reading is the draft's and hedged in both files; no
  authority to hand for anything better. Kept, listed below.
- husaje "no common modern form, closest uso": usaje survives only as a rarity; harmless. Kept.
- fieras (known 'great, mighty … uncertain nuance') for montañas … fieras: covers 'wild, great'. No broaden.
- así (known "así como 'as soon as'") for así commo a mí dixieron 'as they told me': the main sense 'thus, so'
  covers it. No broaden.
- Known valençia ("whose king Tamín is addressed") and maría/santa ("the cathedral of Burgos") carry context from
  their first parts; outside this pass except where this part's sense was missing (maría broadened).

## Readings left uncertain

- v. 1457 tal deve sperar: what 'the like' is (good news in return for a good messenger).
- v. 1465 conssigrá: read as a syncopated future of conseguir, 'escort'; no note in Pidal.
- v. 1471 desenparás: 1st sg. ('if I abandoned it') or 3rd sg. generic.
- v. 1498 Virtos: 'forces, troops', the form uncertain (as v. 657).
- v. 1503 de grand óndral dar: whom le refers to (the Çid or Minaya's party).
- v. 1507 den: 'from there' (de ende) or partitive 'of them'.
- v. 1493 deprunar: 'go down', a rare word.

## Text observations for the establishing run (no `t` changed)

- v. 1494 recabdo: at 300 and 600 dpi a dark wedge touches the top of the e (looks like "récabdo"); it joins the
  letter instead of standing above it as Pidal's accents do (cf. está in the same line), so most likely an ink
  blemish. Pinned recabdo kept; no QUESTIONS entry needed unless the owner wants it recorded.
- The print points already in QUESTIONS.md (1471 seríe, 1476 viniéron, 1503 óndral, 1494b Alvar, 1505 label)
  confirmed on the scan; nothing to add.
- No misreading of the established text found in this part.

## Validation

units.json: 28 units, fields t/l/i/n only (as the draft), 77 `t` lines = the 77 packet verses in order, `l` line
counts equal `t`. gloss.json: 74 keys = novel-forms.json, 7 broadens all prefix-exact, no token uncovered. Both
files load as JSON.
