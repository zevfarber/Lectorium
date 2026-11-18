# Review — cid-tiradas-75-77 (tiradas 75–77, lines 1221–1286)

Adversarial review against the pinned packet, Pidal's rubrics and footnotes on the scan (PDF pp. 212–216 read at
150 dpi, with crops at 450 dpi of a[r]ruenço v. 1229, abondados v. 1245, menores v. 1234 and Roy Diaz v. 1237),
conventions.md, the pilot (01-04) and the published parts (05-09, 15-17, 18-18, 19-23, 32-34, 40-43, 49-55, 69-74
in particular), the shared glossary and known-forms.json. All edits made by script (json load/dump,
ensure_ascii=False, indent=1). No `t` changed: the 70 `t` lines concatenated equal the packet's 70 verses in order
exactly, checked by script after the edits; one `l` line per `t` line in all 26 units; no unit crosses a tirada.

## Pass 1 — units.json

Counts: error 0 · weak 5 · style 6 (11 changes)

| unit (first words) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 1228 Fata dentro | i | weak | "Moors swept along against the current": Pidal's gloss is 'ronceando (a la ronza contra la corriente)', struggling/drifting against the current, not carried by it | "Moors floundering against the current" |
| 1245 Los que exieron | n | weak | "rictad, v. 687, which Pidal glosses 'riqueza'": rictad is v. 688 (second line of the unit at 687 in 32-34) | v. 688 |
| 1251 Esto mandó | n | weak | spidiés "its -sse cut away": that would give *spidié*; it is espidiesse with the final -e lost (-sse > -s), as curiás v. 329 (18-18) | relabelled, with the cross-reference |
| 1257 "si vos quisiéredes | n | weak | "in Pidal's note to v. 1245 they [los que son aquí] are the later recruits": Pidal says only that los que son aquí and mios vasallos are set against each other, as exiles against newcomers; which is which is our inference | "Pidal's note … sets them against mios vasallos (v. 1261), so presumably the later recruits" |
| 1260 que si algunos | n | weak | "These are the old vassals of Pidal's note to v. 1245": same inference stated as his | "presumably the old vassals" |
| 1221 Ya folgava | n | style | âquel: the note did not say Pidal gives no note on the form (the parallel note at 1261 did) | "(Pidal gives no note on the form)" added |
| 1228 Fata dentro | n | style | amidos "v. 83": the word is at v. 84 (fer lo he amidos) | v. 84 |
| 1232 Buena f[o] | n | style | los menores "the rank and file as against the captains" stated flat, though unsourced | "apparently the rank and file …" |
| 1255 Afevos | n | style | recabdo "v. 23": con grand recabdo is v. 24 (as the 69-74 review cites) | v. 24 |
| 1260 que si algunos | n | style | "curian = curiar": a finite form equated with the infinitive | "curian, present 3rd pl. of curiar … (curiás, v. 329)" |
| 1266 alégrasle | l | style | "rejoices-himself-to-him the heart": the se is the heart's, not the Çid's | "rejoices-itself-to-him the heart" |

Checked and found sound (no change):
- Rubrics against the scan, all three right: 75 El Rey de Sevilla quiere recobrar Valencia (p. 212); 76 El Cid
  deja su barba intonsa.—Riqueza de los del Cid (p. 213); 77 Recuento de la gente del Cid.—Este dispone nuevo
  presente para el rey (p. 215). Assonances re-derived: 75 á-a (ganançia counts); 76 á-o (nasco); 77 á with the
  á-e endings madre, heredades, naturales, mensage, iffantes, Fáñez. Right in all three first notes.
- Footnotes against the scan, wording right: 1222 (Seville from 1091 Almoravid; rey of Moors = any general or emir,
  v. 637; the Almoravid general who governed Seville), 1224 (ver 'atacar', comp. 1124), 1229 ('los moros
  ronceando …'; fugitives gorging on water; Fernán González 358c, the tolosanos driven against the Ebro, 'bevían mal
  de su grado'; Roland 2473, Saracens pursued by Charlemagne drown in the Ebro), 1232 (la casa 'la población, la
  ciudad', comp. 62, 1550, 2877), 1233 (mas mucho = 'más'; arrancada 'victoria'), 1235 (Las nuevas 'los asuntos,
  los negocios'), 1241 (comp. 2059; beard, hair and nails left uncut as a sign of grief after oath; the Catholic
  King after the death of Prince Don Juan), 1242 (moros e cristianos 'todo el mundo', comp. 145), 1245 (exiles vs
  newcomers, 1248, vv. 917, 1199; los que son aquí 1258 vs mios vasallos 1261; city shared to old vassals, p. 99;
  allegadizos share only the booty), 1252b ('despídome de vos et bésovos la mano …'), 1254 (palo 'horca'), 1260
  (fallaro, see note to 825; 'si le hallare menos', 'si le echare de menos', comp. 798), 1261b (arrobdar 'rondar,
  hacer el servicio de guardia exterior en una fortaleza'), 1268 (más pocos 'menos', comp. más mucho 1233; casa
  'población, lugar'), 1277 (quenlas dexe 'que me las deje'), 1282 (Essora 'entonces', v. 983). No other footnotes
  to these lines (1288 and 1290 on p. 216 belong to the next part). The "Pidal gives no note" claims (âquel, non
  gela enparan, barata, la de Valençia, menores, ritad, contado, furtare, âquestos, corth, quinientos) are right.
- 1277 quenlas: the draft unit already follows Pidal's footnote (que + me + las); the glosser's que + non + las was
  wrong and is corrected in pass 2.
- Italics seen on the image and reported: ve[e]r, a[r]ruenço (first r only, crop), [Sevilla], f[o], ve[e]des,
  R[o]y, [el Campeador contado], f[o]ron, [que con él ganaron algo], f[o]sse, conseja[ndo], fallar[o], [doña
  Ximena], [naturales], f[o]re, [a toda su voluntad], [quinientos]. Pidal's closing quote after echado (1240), the
  full stop after folgando (1243) with small c in con (1244), y in casas y heredades, and the broken second vowel
  of abondados (crop: the o is damaged, read as o) all confirmed.
- Cross-references checked in the published parts: lâ v. 914 (49-55), le caen v. 1217, rritad v. 1189, Afevos
  v. 262, prestalde v. 118, guisa v. 131, santa María madre v. 333, San Pero / abbot Sancho v. 237 ff., Essora
  v. 983, visquier[o] v. 825 and fallar menos v. 798 (40-43, which already cites fallaro v. 1260 with the -o first
  person), rictad (Pidal 'riqueza', 32-34).
- Grammar labels checked and right: veriédes (conditional 2nd pl.), dixera (-ra pluperfect), entrarié / avrié
  tajado (conditional, conditional perfect), fablassen, pudiessen, tomássenle / pusiéssenle (imperfect subjunctive,
  enclitic le), ploguiere, quisiéredes, f[o]re, fallar[o] (future subjunctive), caya, dexe, sean (present
  subjunctive), meterlos he (split future), fer lo ien (split conditional), Yal, vale = va le (ir + gerund), sis,
  sil, nol, nos le parte (no se), ques, gela / gelo, ídgelos (id + ge + los), besalde (-dl- > -ld-), Mandólos,
  fízolos, arrancólos, alégrasle, tornós, Tornado es, avién tomados and avemos fechas (participle agreeing), ovo
  conssejado, aver a + inf. (avrá a tornar), ixiemos / pudiemos (-iemos), vernán, el arrancada, bever (infinitive
  for a finite verb), escapa (present amid preterites).
- `l` ↔ `i` unit by unit: no remembered English found. House usage kept: "my Çid", Çid in `i`, "born in a good
  hour" (1237), Minaya Álvar Fáñez / Álvar Fáñez in `i` (Álbar kept in `l`), Ruy Díaz in `i`, Vivar, Castile,
  "be sure of it" / "know-ye" for sabet, iffantes 'children' (as 15-17), contado 'renowned' (as 05-09, 10-14).

Findings refused:
- 1249 `i` "they would gladly go off home": "home" is not in the line, but it is where they would go; light
  interpretation. Left.
- 1237 `l` "Roy Díaz" for `t` Roy Diaz: the published `l` lines accent the name; the print at 450 dpi may carry a
  faint accent on the i (see uncertain readings). Left.
- 1251 ovo conssejado "(the past anterior)": formally right; the poem uses it as little more than a past. Left.
- 1221 non gela enparan, 1228 barata, 1232 la de Valençia, 1260 furtare, 1286 quinientos: each already hedged with
  "Pidal gives no note" and "not certain"; no better reading from the allowed sources. Left.
- 1221 âquel / 1261 âquestos as a + aquel / a + aquestos: consistent with Pidal's other circumflexes (lâ, lês, mê
  read as two vowels run together in published parts) and with the sense ('to that king', 'to these my vassals');
  hedged at 1261, now also marked "no note" at 1221. Left.

## Pass 2 — gloss.json

Counts: error 3 · weak 12 · style 9 (24 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| quenlas | error | analysed as que + non + las, against Pidal's footnote to v. 1277 'que me las deje' | que + me + las, Pidal cited, the me worn to n before l (cf. quem in the shared glossary) |
| fallaro | error | "future subjunctive 3rd sg … 'if he finds him missing'": Pidal's 'si le hallare menos' has the Çid as subject; the -o is the old 1st sg. ending (as 40-43 says, citing this line) | 1st sg., 'if I find him missing', Pidal's gloss quoted |
| ritad | error | "probably 'fullness, entirety, requital' … perhaps Latin rectitas": invented sense and etymology, contradicting the unit and the shared rictad (Pidal 'riqueza') / rritad | "uncertain … most likely a noun made on rico, 'riches, wealth'", rictad v. 688 and rritad v. 1189 cited, in line with the shared rritad entry |
| sevilla | weak | "held in the poem's time by the Almoravids": Pidal says from 1091 | from 1091, Pidal's note to v. 1222 credited |
| enparan | weak | "'they do not defend it for him'" against the unit's 'do not hold it against him (the Çid)' | aligned with the unit, uncertainty of 'him' kept |
| aprés | weak | "Latin ad pressum; cf. French après": unsourced etymology | cut |
| barata | weak | "barata 'cockroach' being unrelated", relation to barato: unsourced and beside the point | 'turmoil, a scramble', 'a dealing' otherwise; no note; uncertain (as the unit) |
| provechosa | weak | example "mucho fue provechosa 'was much more profitable'" drops mas and misreads mas mucho (Pidal: = 'más') | "mas mucho fue provechosa 'was more profitable'" |
| spidiés | weak | "final -sse lost": it is the final -e (-sse > -s) | relabelled, e- dropped noted (as spidiós in the shared glossary) |
| furtare | weak | "(if) he steal" flat; the unit reads 'steal away' with a hedge | both senses, no note, hedged |
| curian | weak | "the tense could also be taken as imperfect": curiar is an -ar verb (imperfect curiava); curian is only present | clause cut |
| corth | weak | "th a learned spelling": unsourced | "so spelled, with final -th; no note in Pidal" |
| ídgelos | weak | "= idlos a llevar": drops the ge (se); gloss line garbled ("go … it-to-him … them") | "go … them to him"; = id a llevárselos |
| __broaden__ vale | weak | "probably va + le or valer in an auxiliary sense … uncertain" against the unit's va + le | va + le, ir + gerund with enclitic le |
| __broaden__ iffantes | weak | 'daughters of rank, young ladies (= infantas)' against the unit's and 15-17's 'children'; the known entry covers the use | removed |
| âquel | style | "â aquel rey" quoted as if printed so; no word that Pidal has no note | âquel rey quoted; "Pidal … gives no note" |
| uerta | style | "u- spelling for h-" | "spelled without h" |
| arruenço | style | "cf. roncear 'to dawdle'": modern sense beside Pidal's | Pidal's Spanish quoted and Englished; his restored r noted |
| menores | style | "the common soldiers, the humblest" flat | "apparently the rank and file; no note in Pidal" |
| besalde | style | "kiss his!" | "kiss … his" |
| dexe | style | "'that he let them be brought out'" against Pidal's 'que me las deje' | "'that he let me take them out'" |
| sacar | style | same | "let (me) take (them) out" |
| vernán | style | "syncopated stem" only | syncope and the n/r exchange (venir-án > vernán) |
| __broaden__ casa | style | unneeded: the known entry already has 'settlement, town (Burgos la casa)' | removed |

Checked: gloss keys (78, excluding __broaden__) equal the novel-forms.json keys exactly. Every __broaden__ value
(14: armas, parte, ivan, vale, passar, fo, pocos, mucho, arrancada, nuevas, guisa, voluntad, le, por) begins with
the known-forms.json entry verbatim + " · " (checked by script). All tokens of the 70 lines (brackets stripped,
lowercased, apostrophe splitting) are covered by known + gloss. Other entries checked and right: folgava,
arrancólos, luenga, xúcar, veriédes, bever, escapa, cayeron, allongando, dixera, atanto (hedged), alffonsso,
entrarié, tigera, pelo, tajado, fablassen, folgando, exieron, abondados, provando, veelo, tomados, sis, pudiessen,
conssejado, ningún, besás, sil, alcançado, tomássenle, pusiéssenle, palo (Pidal), saber, meterlos, escripto, sean,
âquestos, myos, arrobdando (Pidal), falló, fízolos, nonbrar, çientos, alégrasle, sonrrisar, ixiemos, riquiza,
destas, rogad, naturales, enbiaré, sabed, mensage, ciento, servirle, carrera. Known entries covering this part's
uses (no broaden needed): veer (ir veer 'to attack' covers vino los ve[e]r), nos (no se, nos le parte), recabdo
(care / account), tornar ('give back'), menos (fallar menos), contado, pagados, tornós (tornarse a + inf.), do,
casa, mandó, y, a, es, que, sabet.

Findings refused:
- tigera "Latin tonsoria": an etymology not in Pidal's notes, but standard and harmless. Kept.
- alffonsso "who exiled the Cid": stated in the text itself (v. 1240). Kept.
- __broaden__ ivan: the known va already has ir + gerund, but ivan's known entry does not. Kept.
- veer: a broaden for venir veer was considered; the known 'ir veer … to attack' (Pidal) is close enough. Not added.

## Readings left uncertain

- v. 1221 non gela enparan: whose 'him' (the Çid, or the king of Seville) is not certain; no note.
- v. 1222 âquel, v. 1261 âquestos: read as a + aquel / a + aquestos; Pidal gives no note on the circumflex here.
- v. 1228 barata: 'turmoil, a scramble'; no note.
- v. 1229 en a[r]ruenço: Pidal's 'ronceando (a la ronza contra la corriente)'; the exact sense of the phrase.
- v. 1232 la de Valençia: which feminine noun is understood (ganançia or arrancada).
- v. 1234 los menores: 'the lesser men', no note.
- v. 1237 Diaz: pinned without accent; at 450 dpi the dot of the i is slanted and may be an accent (Díaz). `t` not
  changed; for the establishing run to confirm.
- v. 1245 ritad: 'wealth', a noun on rico, by analogy with rictad (Pidal 'riqueza'); no gloss on the page.
- v. 1258 / 1261 los que son aquí = the newcomers, mios vasallos = the old vassals: inferred from Pidal's note to
  v. 1245, which pairs but does not label them.
- v. 1260 furtare: 'steal away' or 'steal'; algunos with a singular verb; no note.
- v. 1263 corth: = corte; the -th spelling unexplained.
- v. 1286 [quinientos]: Pidal's restoration; that it is half the thousand, and what the other half is for, is not
  said.

## Validation

`python3 -c "import json; json.load(open('units.json')); json.load(open('gloss.json'))"` — both load. units.json:
26 units, fields t/l/i/n only, 70 `t` lines = the 70 packet verses in order, `l` line counts equal `t`, no unit
crosses a tirada. gloss.json: 78 keys = novel-forms.json, 14 broadens all prefix-exact, no token uncovered.
