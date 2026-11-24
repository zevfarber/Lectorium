# Review: cid-tiradas-118-119 (tiradas 118–119, vv. 2403–2473)

Checked against the pinned packet; Pidal 1923, PDF pp. 284–288 (printed 280–284: text and italics, the rubrics of
tiradas 118, 119 (and 120, 121), and the footnotes 2404, 2407, 2411, 2414, 2417, 2422, 2437, 2450, 2452, 2456,
2460, 2465, 2467, 2469); the margin labels of pp. 282–283 for the numbering question; the published parts for
the lines cited in the notes (vv. 8, 119, 148, 300, 481, 751, 766–67, 979, 1010, 1744, 2342, 2376, 2388, 2399)
and for house renderings (Valençia, co[u]nt, Dí[a]go, R[o]y, the en buen ora formula in `l`); `conventions.md`;
`known-forms.json`, `novel-forms.json`; the last line of LOG.md.
`t` integrity (by script, before and after the edits): all `t` joined by "\n" equal the 70 packet verses (2437b
included) in order; 27 units, none across a tirada break; every `l` has as many lines as its `t`; no `t` was
touched. Both files edited by script (json load/replace/dump, indent 1, ensure_ascii=False).

## Pass 1: units.json

1. 2460 (vv. 2460–61) · n · **error** · "the surviving text shows the Infantes doing nothing in the battle but
   Fernando's flight": the flight is not in the surviving verse; it is told only in the chronicle prose Pidal
   sets in the lost folio (vv. 2339–40 have only Pero Vermudoz vouching for Fernando's boast). Done: "in the
   verse that survives the Infantes do nothing of note in the battle, and Fernando's flight is known only from
   the chronicle prose Pidal sets in the lost folio."
2. 2434 (vv. 2434–37) · i · **weak** · "his face drawn up in folds": the note itself cites Pidal (note to v. 1744)
   that la cara fronzida is to be understood of the coif gathered about the face, and 95-95 renders v. 1744 so
   ("his coif gathered about his face"). Done: "his face framed in the gathered coif, his mail-hood thrown back,
   the coif over his hair a little rumpled."
3. 2455 (vv. 2455–56) · n · **weak** · (a) "as the Çid's prayer at v. 8": v. 8 is grado a tí, señor padre, not
   Grado a Dios; now quoted. (b) The footnote was described as "Pidal's note printed as 2456" and then attached
   to e al padre with no word on where the footnote falls; the numbering paragraph did not say why the
   footnote fits this line and not the next. Rewritten: the speaker (Minaya, come up at v. 2449, answered by the
   Çid at v. 2462); the footnote quoted exactly (Conjunción e pleonástica, v. 300), with v. 300 (a Dios e al Padre
   spirital) and Pidal's note to 2342 (Dios … e el Padre, comp. v. 300); then the numbering stated as a question,
   uncertain, in three sentences. `i` "God, the Father on high" kept: it is what the pleonastic e means.
4. 2414 (vv. 2412–14) · n · **style** · Pidal's note quoted as "más famoso[s] del Poema, p. 49, 50 n. y 51": a
   bracket inside a quotation of Pidal, and a comma dropped. The print reads "más famoso del Poema, p. 49, 50,'
   n. y 51" (the ' a blemish). Done: quoted as printed, "(famoso, for famosos, as printed)".
5. 2465 (vv. 2465–67) · l · **style** · "All [the] gain[s]": only the os of l[os] is Pidal's, and English "the"
   has no counterpart to it, so a bracket round the whole word overstates the restoration (house: brackets in
   `l` only for restored words or letters with an English counterpart). Done: "All the gain[s]" (the plural s
   answers the restored -dos; kept).
6. 2465, 2471 · l · **style** · "Valencia" in `l`: the house keeps Valençia in `l` (102-102 to 112-114, 96-101).
   Done: "Valençia" in both.

Checked and kept:
- Every quotation of Pidal verified on the scan: 2404 (Esta descripción está imitada de las Chansons de geste
  francesas, p. 39-40), 2407, 2411 (comp. 3030), 2414 (ensayar, 'probar, emplear', v. 2376), 2417 (comp. 979),
  2422 (Comp. 766 — the drafter's gloss, Martín Antolínez's stroke at Galve, checked against 35-39), 2437
  (yaquanto, 'algo'. Para la cofia froncida, comp. 1744), 2450 (p. 105; de tabla), 2452, 2456, 2460 (v. 2388),
  2465 (ganados, 'ganancias', v. 481), 2467, 2469 (v. 119). The reports of Pidal's notes to 1744 and 2388 and of
  751 match the published parts. All exact; none invented.
- Rubrics 118 and 119 quoted exactly; English versions fair. The closing reference to tirada 120 (El Cid
  satisfecho de su victoria y de sus yernos. (Repetición)) is right.
- Grammar labels confirmed: veriedes (conditional); cofonda (present subjunctive); ca[d]iól, Respuso, nasco,
  Alegrós, dixo, touieron, Matastes, f[o]stes (preterites, strong or old); vi[di]e, ca[di]e, vinía, avie, tenien
  (imperfects); Ve[e]rte as, saludar nos hemos (split futures); dádol ha, llegado ha (perfect, participle first);
  dieran (-ra pluperfect); tollidas gela[s] (participle agreeing with carbonclas); eran llegados, es llegado, son
  ensayados (ser + participle); librado … lo al (absolute participle, sense flagged); destellando (loose gerund).
- The drafter's specific points: 2409 dalent = d'alent, 'from beyond' (right); 2423 librado todo lo al — the
  absolute construction and al 'the rest' are right, librado flagged uncertain, Pidal silent: kept; 2438
  vi[di]e = veía, imperfect, the italic's extent flagged as LOG.md has it: right; 2455 speaker Minaya: right
  (the poem does not name him, the context does); 2471 F[o]ron, subject most naturally the Infantes (2468–70
  run on), "may be the whole company" kept; 2472 a sazones left uncertain (no note of Pidal's on this page);
  2473 Muchos son alegres, mucho adverbial agreeing in number: right.
- House renderings: Minaya Álvar Fáñez, Babieca, Búcar, Diego and Fernando, Count Don Gonzalo, Ruy Díaz, the en
  buen ora formula ("(in) a-good (hour)" for buen[a] nasco), Dí[a]go, co[u]nt, R[o]y, w[e]re, h[i]s in `l`.
- 2437b note (the moved line, Pidal's 2455 kept in the note, 2437b ours) and 2460 note (2459 printed nowhere)
  are accurate and agree with the reading below.

Refused / left as drafted:
- 2455 `i` "Thanks be to God, the Father on high" against 18-18 v. 300 "to God and to the spiritual Father" and
  115-117 v. 2342 "God … and the Father on high": here Pidal's footnote says outright that the e is pleonastic;
  the earlier parts are not wrong enough to touch. Left.
- 2415 `i` "till we are out in the sea" for fata dentro en la mar: loose (it is Búcar who means to reach the
  sea and his ships) but not wrong. Left.
- 2423 `i` "cleaving all the rest" for librado: a shade beyond 'dispatched', but the note flags librado. Left.
- 2422 `l` "from-him-[them]" for gela[s]: the restored s does answer English "them". Left.

Pass 1 counts: error 1 · weak 2 · style 3 (6 items).

## Pass 2: gloss.json

1. __broaden__ e · **error** · the pleonastic e was illustrated by "e a vos, Çid, que en buen ora fostes nado",
   whose e is a plain 'and'; the pleonastic e is the one in a Dios e al padre (v. 300 a Dios e al Padre spirital).
   Done: "pleonastic 'and' joining two names of the one person (a Dios e al padre 'to God, the Father'; Pidal
   'conjunción e pleonástica', cf. v. 300)".
2. escarnio · **error** · "Pidal's es[carnio]": the whole word is Pidal's, [escarnio]. Done, with tener a
   escarnio 'to take as mockery'.
3. ensayados · **weak** · "tried, tested … 'have been tried'": the unit (with Pidal's 'aquí se han
   distinguido' and his note to 2388) reads ensayarse 'exert oneself, do deeds of prowess', ser as perfect
   auxiliary. Done.
4. juntarás · **weak** · lemma "juntar + te" on a form that has no te. Done: juntar, with juntarse con uno in the
   gloss.
5. cofonda · **weak** · lemma "confonder" where the text and the unit have cofonder. Done.
6. __broaden__ fronzida · **weak** · added "of the face: creased, drawn (sense uncertain)", against Pidal (note
   to v. 1744, already in the known entry: la cara fronzida = the coif gathered about the face). The known entry
   covers both uses here. Removed.
7. __broaden__ muchos · **weak** · missing: known 'many'; here Muchos son alegres 'very glad are' (adverb
   agreeing in number). Added.
8. __broaden__ preçiados · **weak** · missing: known 'valuable, precious' (of things); here of men, adelant
   serán preçiados 'will be esteemed'. Added.
9. __broaden__ avie · **weak** · missing: known 'he had' / temporal 'it had been'; here impersonal 'there was'
   (non avie recabdo). Added.
10. as · **style** · defined only by the line (veerte as); made general: 'you have' (= has), also the future
    auxiliary of the split future.
11. cadiól · **style** · "cadió, -ió kept" meant nothing; now "the old form with -d-".
12. dádol · **style** · "split perfect" for dádol ha: the participle set before aver. Done.
13. yaquanto · **style** · "creased somewhat from it" → della yaquanto 'somewhat of it' (Pidal 'algo').
14. __broaden__ della · **style** · same wording, and the coif named.
15. __broaden__ raçión · **style** · "cadie a la raçión" reversed the text's a la raçión cadie. Done.
16. arrancamos · **style** · "'to clear the field'" and "= arrancamos": now 'to rout the enemy from the field',
    = derrotamos, preterite noted as the reading (the form is also present).

Checked and kept: cáenlos, caer, cabeças, yelmos, migeros, torna, venist, dalent, veerte, saludar, tajaremos,
amiztat, veot, quieres, estropieça, saltos, alcançándolo, alcançólo, braças, tollidas, librado (flagged), tizón,
vençió, preçiava, matança, vinía, soltado, pelos, alegrós, fio, espadado, logrado, veínte, matado, matastes,
bienes, fartos, touieron, cadie, tomaron, cuydaron, minguados, arreados, sazones (flagged), pieles;
__broaden__ tienes, val, llegado, faz, cade, avien, así, te, salvo, recabdo, ganados, algo, de.
Keys of gloss.json minus __broaden__ equal novel-forms.json (54). Every __broaden__ (19: 1 removed, 3 added) is
the known-forms entry whole + " · " + the new reading (checked by script). The other known forms were checked
against this part's uses; alcaz, tanto, part, caden, al, aquís, elle, yas, firme, contado, privado, vidie,
cofia, almófar, fermoso, arrancada, gelos, dieran, destellando, grado, padre, nado, fostes, foron, tenien, a
('as' in tener a), en ('on'), por ('in' after fiar) already cover them.

Refused:
- __broaden__ gelo for non gelo avien logrado ('it from him'): 'it to him' with lograr is close enough, and
  Pidal glosses the whole phrase. Left.
- braças "exact length uncertain": harmless. Left.
- tizón "the sword of King Búcar": the poem says he won it from Búcar; fair. Left.

Pass 2 counts: error 2 · weak 7 · style 7 (16 items).

## Readings left uncertain in the notes
- 2423 librado todo lo al: the shade of librado (Pidal silent).
- 2455 numbering (below).
- 2471 F[o]ron: the Infantes most naturally, perhaps the whole company.
- 2472 a sazones: 'in season(s)', food in due time or in good supply.
- Italic extents from LOG.md, repeated in the notes: el[le] 2428, vi[di]e 2438, espad[ad]o 2450, gana[dos]
  2465, ca[di]e 2467.

## For QUESTIONS.md: the double label 2455 (tirada 119)
Pidal prints the margin label 2455 twice: on "De todas partes sos vassallos van llegando" (p. 282, which he has
moved up between 2437 and 2438) and on "Grado a Dios e al padre que está en alto" (p. 283). Counting from the
label 2450 on "el escudo trae al cuello", "Grado" is the fifth line after it, so the second 2455 agrees with
the count on the page; but that count ignores the moved line. If "De todas partes" (2455) stood in the
manuscript between 2454 "de veínte arriba ha moros matado" and "Grado", then "Grado" is 2456, "e a vos, Çid"
2457, "Matastes" 2458, "Todos estos bienes" 2459 and "E vuestros yernos" 2460, as labelled. Three things support
this: (1) the moved line's own label 2455 says that is where it belongs; (2) the number 2459, otherwise printed
nowhere with no line missing, is accounted for; (3) Pidal's footnote 2456, "Conjunción e pleonástica, v. 300",
fits "Grado a Dios e al padre" (v. 300: a Dios e al Padre spirital; his note to 2342 also points to v. 300) and
not "e a vos, Çid", whose e is an ordinary 'and'. The footnote 2460 ('aquí se han distinguido') falls on "E
vuestros yernos" either way. Verdict: the drafter is right, and the case is stronger than he put it — the
second 2455 is a slip of the print (most likely a leftover label from before the line was moved), and the
correct numbering is De todas partes = 2455 (not 2437b), Grado = 2456 … Todos estos bienes = 2459. In this
firing the pinned numbers stand and the notes on 2437b, 2455 and 2460 state the question; renumbering is the
owner's decision (it touches the pinned text's labels and the provisional 2437b).
