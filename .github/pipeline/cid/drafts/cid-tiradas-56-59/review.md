# Review — cid-tiradas-56-59 (tiradas 56–59, lines 960–1023)

Adversarial review against the pinned packet, Pidal's rubrics and footnotes on the scan (PDF pp. 194–198, read at
200 dpi, with crops at 500 dpi for [el] [a]mi[z]tad (v. 965), Pidal's note to 985, de’llaño (v. 1003), cozínal
(v. 1017) and Pidal's note to 1017), conventions.md, the pilot (01-04) and the published parts 05-09 … 49-55
(especially 44-48 and 49-55). PDF p. 110 checked to confirm that Pidal's "p. 106" (notes to 997, 1023) is in his
introduction (Valor arqueológico). All edits made by script (json load/dump, ensure_ascii=False, indent=1). No `t`
changed: the 64 `t` lines concatenated equal the packet's 64 lines exactly (checked by script before and after the
edits); one `l` line per `t` line in all 29 units.

## Pass 1 — units.json

Counts: error 1 · weak 8 · style 8 (17 changes)

| unit (first words) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 1008 Vençido a esta batalla | n | error | "a = ha written without h; a esta batalla, the object marked by a": one a made both the auxiliary and an object marker; there is only one a | a = ha only; esta batalla the direct object, said plainly |
| 975 Del conde don Remont | n | weak | "the count of Barcelona, Ramón Berenguer" given as a historical identification; Pidal's note to 958 names the historical count Berenguer Ramón 'el fratricida' | the poem's name in modern spelling, and Pidal's historical count named, both kept apart |
| 985 Ya cavalleros | n | weak | Pidal's note reported as "longe facti sunt, 'they withdrew'"; on the scan (500 dpi) Pidal renders it 'los alejaron' | note quotes Pidal's gloss as printed |
| 985 Ya cavalleros | n | weak | "metedos = meteos (meted + os)": the old pronoun is vos; os is the later form | meted + vos, the v lost (metedvos > metedos) |
| 992 Ellos vienen cuesta yuso | l, i, n | weak | siellas coçeras rendered "light": no source; the note itself called it an approximation | `l` "insecure", `i` "unsteady", after Pidal's 'inseguras' (note to 1007); note says the rendering follows Pidal's description, not the word, and the sense is uncertain |
| 994 nos cavalgaremos | n | weak | "the heavy saddles of the west": drafter's invention, not in the text or the footnotes | removed; note says what made Galician saddles better is not stated here, keeps the pointer to p. 106 |
| 1002 Vi[di]eron | n | weak | de’llaño = del llaño stated as fact; no footnote; and the subject of çerca es asserted ("the host") | apostrophe confirmed on the scan; del llaño given as the reading taken, said to be uncertain (could be a bare elision de + llaño); subject "most likely the Franks' host" |
| 1002 Vi[di]eron | n | weak | mandólos ferir: los stated to be the Çid's men; los can equally be the object of ferir (cf. vayámoslos ferir in the glossary) | both constructions given; the Çid's men as the more likely, with v. 311 as parallel; `l`/`i` already neutral |
| 1011 I venció esta batalla | n | weak | "prísole = le prisó": invented stressed form (the preterite is priso) | priso + le, the written accent explained |
| 962 Dentro en mi cort | n | style | el sobrino "i.e. the Çid's" asserted while saying the text does not name him | "presumably the Çid's" |
| 983 Essora lo connosçe | l | style | quitar "free-themselves": no reflexive in the text | "get-free" |
| 983 Essora lo connosçe | n | style | den = de ende; earlier parts analyse dent as de + ent | "de + en (= ende) … as dent (de + ent) at v. 951" |
| 1005 esto fazen los sos | i | style | "striking down some and unhorsing others": "striking down" anticipates derrocando, which Pidal's note says is the point (no killing, no wounding needed) | "striking some and unhorsing others" |
| 1005 esto fazen los sos | n | style | "(st. 529)": Pidal writes "Alexandre, 529" | "(529)" |
| 1010 hi gañó a Colada | n | style | "taken from the count": neither the line nor the rubric says from whom | "won there in the battle (the line does not say from whom)" |
| 1011 I venció esta batalla | n | style | "Cantar pp. 865–866" unexplained | "his Cantar de mio Cid, pp. 865–866" |
| 1021 Non combré | i | style | "ill-shod louts": "louts" added to malcalçados | "ill-shod men" |

Checked and found sound (no change):
- Rubrics against the scan: 56 El Cid trata en vano de calmar al conde; 57 Arenga del Cid a los suyos; 58 El Cid vence
  la batalla. Gana la espada Colada; 59 El conde de Barcelona, prisionero. Quiere dejarse morir de hambre.
  Assonances re-derived from every line end: 56 á (grandes 968, mensaje 975 á-e), 57 á-a (ganançia, vázias with -ia
  counting as a), 58 á-o, 59 á-a (ajunta[van], adobavan, paravan included). Right in all four first notes.
- Footnotes reported correctly: 958 (pointing to 964), 962 (the Çid in Barcelona, p. 18, n. 1), 965 (tornar amistad,
  the formula 'tórnovos amistad et desafíovos …'), 971 (= el pinar de Tévar, 912, 999; document of 1209; Monroy and
  Tastavins; Tarragona and Castellón), 974 (diçe 'desciende'), 979 ('esto no será así', 2417, 3028), 985 (now as
  printed), 986 (meterse en armas, 3550, synonym of bestir las armas, 991), 991 (girth tightened before charging),
  997 (v. 1007 and p. 106), 1002 (los francos = the Catalans; Carolingian march), 1007 (derrocando 'derribando';
  siellas coçeras inseguras; Alexandre 529; no need to kill or wound; comp. 997), 1013 (creendero 'servidor fiel';
  second capture of the count, Morella, 1090; p. 16 and Cantar 865–866), 1017 (cozina 'vianda o comida aderezada al
  fuego'), 1023 (p. 106; malcalzado as a nickname; sale of 1230, 'Pedro Martín, nieto de Malcalzado'). No footnote on
  960 (follón), 968, 975 (lês), 993 (amojadas), 1003 (de’llaño), 1014; the notes now claim none.
- Italics on the image: [el] [a]mi[z]tad (el, a and z italic at 500 dpi), llegando[s], viene[n] esforçado[s] …
  cuyda[n], co[m]de (979, 987, 1009, 1012), Vi[di]eron, buen[a], tie[nd]a, ajunta[van]. lês circumflex, de’llaño
  apostrophe, cozínal accent, ganancias with c (1016), no stop after grandes (968): all confirmed.
- Grammar labels checked and right: tiene, tovo, firióm, enmendó, córrem, desafié, nil, ir gelo he demandar,
  llegando[s] van, se le allegan, penssaron de, alcançaron, cuyda[n], diçe/llegava (tense-mixing), lês (hedged),
  digades, tenga, lievo, déxem, respuso, tódom, pechará, vino desondrar, tornós, connosçe, fazed, guarnid, dar nos ha,
  dexarié, sea, apretad, bistades, trahen, elas, cavalgaremos, devemos, presentémosles, firgades, tollerme, ovo
  fablado, avién presas, sedién, nasco, van enpleando, a … le a tomado, gañó, ondró, levava/mandava, plogo, adobavan,
  preçia, gelo/gelos, adúzenle, comeres, sosañava, combré, perderé/dexaré, vençieron.
- House renderings: Çid in `i` throughout; "in a-good (hour)" in `l` at 1004 and 1008; "born in a good hour" in `i`;
  "he of Vivar" / "my Çid of Vivar" in `i` as 18-18 and 44-48; "the pine-wood of Tévar" as 49-55. No Minaya in this
  part.

Findings refused:
- 975 lês = les + es: no footnote; the drafter's reading is the natural one (ser auxiliary with venido, as venido es in
  the glossary) and it is already hedged. Left.
- 971 `i` "with their bare hands": "bare" is the English idiom for a manos 'by hand, without a fight'. Left.
- 1000 `i` "All are ready when my Çid has said this": the present/perfect mix follows the line's tense-mixing (son …
  ovo fablado). Left.
- 1017 cozínal = cozina + l(e): Pidal's note heads cozina, which supports splitting off the l; the oddity of a clitic
  on a noun is already stated. Left (hedged).
- 1018 non gelo preçia nada, the force of ge: hedged already. Left.
- 971 Pidal's "(v. 300)" after "912, 999" not reported: a cross-reference the reader cannot follow here. Left.
- 1021 `i` "Spain" for España (the `l` keeps España): normal English for the name. Left.

## Pass 2 — gloss.json

Counts: error 6 · weak 17 · style 21 (44 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| firióm | error | example "'he struck my nephew'" and "the Cid's men wounded the count's nephew": the sense reversed; the nephew is the subject | 'the nephew struck me' |
| metedos | error | "the -d- dropped before the enclitic" (it is the v of vos that is lost) and modern "= metedos, ponedos" (not modern forms) | meted + vos, metedvos > metedos; = meteos |
| bistades | error | "imperative 2nd pl. in -ades": it is the present subjunctive; modern "= vestíos de, vestid" | lemma bestir (b for v); present subjunctive 2nd pl. as exhortation; = vistáis |
| presentémosles | error | "the -s of -mos dropped before les": the s is there | "the s of -mos kept" |
| enpleando | error | lemma "empleár": invented accent and spelling | enplear |
| __broaden__ que | error | "que — 'for, because' (que a menos de batalla …)": at v. 984 que is 'that', the clause lo anticipates; the other uses (relative 'which', so … that) are in the known entry | broaden removed |
| follón | weak | "wicked, boastful", and "modern follón = rascal": unsupported glosses | 'arrogant, overbearing', uncertain, Pidal gives no note |
| penssaron | weak | "they took care … 'to strive to'": the house sense of pensar de + inf. is 'set about' (01-04, 10-14, 18-18 …) | 'set about' only |
| den | weak | "de + en … uncertain whether den is not simply de + ent": confused | de + en, short form of ende, as dent = de + ent; = de allí, de ello |
| coçeras | weak | "saddle with a kick-flap or rear guard … from coz 'kick'": invented sense and etymology | Pidal's 'insecure' (note to 1007), set against siellas gallegas, sense uncertain |
| amojadas | weak | "sense debated, also 'wet, soaked'": a debate and a sense from no source here | 'slack, loose', Pidal gives no note, uncertain |
| gallegas | weak | "i.e. heavy war saddles": invented | set against the enemy's siellas coçeras |
| verenguel | weak | "l for r by dissimilation": unverified explanation | removed |
| vençido | weak | "a before the participle": in vençido a the a follows it | "with a (= ha) after the participle" |
| preson | weak | "prisoner, captivity (masc. noun)": the word is feminine (prisión) and means 'prison, captivity' | 'prison, captivity (fem. noun)'; example 'has taken him prisoner' |
| prísole | weak | "prís(o) … + le/lo … exact analysis uncertain": the analysis is plain | priso + le; = le prendió |
| cozínal | weak | "the -al may instead be el/al": unsupported alternative; Pidal's gloss not used | cozina (Pidal 'vianda o comida aderezada al fuego') + l(e), hedged as in the note |
| malcalçados | weak | "wretched, barefoot rabble … = harapientos": 'barefoot' contradicts huesas sobre calças; harapientos is an invented equivalent | 'badly shod', a sneer; Pidal's nickname note; = malcalzados |
| __broaden__ a | weak | "'has' before the participle … with the object preceding (vençido a esta batalla …)": wrong (a follows the participle, the object follows), and both uses are in the known entry already | broaden removed |
| __broaden__ menos | weak | missing: known menos does not cover a menos de 'without, short of' (984, 989) | broaden added |
| __broaden__ antes | weak | missing: known antes 'before' does not cover 'rather' (1022) | broaden added |
| __broaden__ paravan | weak | missing: known 'took their stand, halted (reflexive)' does not cover transitive 'set before' (1019) | broaden added |
| __broaden__ preçia | weak | missing: the known entry is built on preçia' = preçian (3rd pl.); here 3rd sg. 'he values' (1018) | broaden added |
| conde | style | example "'Count Ramón'": `i` has Count Remont | 'Count Remont' |
| córrem | style | "for me/against me" | 'raids on me', dative of the person harmed |
| nil | style | "give him back (my) friendship" | 'withdrew my friendship from him' (the note's sense) |
| torné | style | Pidal's sense of tornar amistad not given | 'to withdraw friendship' (Pidal: 'retirar la amistad') |
| busca | style | "when he goes looking for it" (the note reads quando as 'since') | 'since he seeks it of me' |
| adeliñan | style | modern "= encaminan, dirigen" (they need se) | = se encaminan, se dirigen |
| diçe | style | "from Latin descendere … lemma slightly uncertain": Pidal's gloss not cited | Pidal 'desciende' cited; hedge dropped |
| remont | style | "i.e. Ramón Berenguer, count of Barcelona" as identification | the poem's name for the count, in full Remont Verenguel |
| connosçe | style | lemma "connoscer" (the text has ç) | connosçer |
| devemos | style | "we are able to" | 'we must, we are bound to' (as the note) |
| sedién | style | "= … sedían": not modern | removed |
| francos | style | "Catalans/French of the march" | the Catalans, after Pidal's note to 1002 |
| derrocando | style | Pidal's 'derribando' not cited | cited |
| colada | style | "won by the Cid from the count of Barcelona": the line does not say from whom | 'won by the Çid at Tévar' |
| creenderos | style | "from creer 'to entrust'" (creer is 'believe, trust') | Pidal's 'servidor fiel'; etymology dropped |
| tales | style | example "such wretches" | 'such ill-shod men' |
| __broaden__ ca | style | redundant: known 'for, because' covers v. 1016 | removed |
| __broaden__ es | style | "Pidal's lês = les es" under es: lês is its own token, glossed under lês; çerca es is plain 'is' | removed |
| __broaden__ verdad | style | missing: non será verdad 'it shall not be so' (Pidal, 979) | broaden added |
| __broaden__ de | style | missing: de’llaño = del llaño | broaden added, hedged as in the note |
| __broaden__ mal | style | missing: tener a mal 'take amiss' (977) | broaden added |

Checked: the gloss keys (97, excluding __broaden__) equal the novel-forms.json keys exactly. Every __broaden__ value
(8: sea, menos, antes, paravan, preçia, verdad, de, mal) begins with the known-forms.json entry exactly, then " · "
(checked by script). All 273 tokens of the 64 lines (brackets stripped, lowercased, split at the apostrophe:
de’llaño → de, llaño) are covered by known + gloss. Other entries checked and right in lemma and grammar: vanidat,
tuertos, cort, tuerto, tovo, enmendó, desafié, amiztad, demandar, llegandos, allegan, tras, alcançaron, cuydan,
lês (hedged), oyó, enbió, digades, tenga, lievo, déxem, tódom, pechará, sabrá, desondrar, mandadero, apart, fazed,
guarnid, dexarié, apretad, cuesta, yuso, trahen, elas, cinchas, cavalgaremos, huesas, vençer, llaño, firgades, verá,
tollerme, adobados, fablado, presas, fuerça, fondón, hi, vale, ondró, mandava, ajuntavan, adobavan, adúzenle, comeres,
quiere, sosañava, combré, bocado, perderé, cuerpo, dexaré, vençieron; broaden sea. No other broaden missing: quitar
('to leave, quit'), çerca 'near', tornós, trae, salto/dava, i 'there', o 'where', gelo/gelos, ha 'there is', tomado,
venido, llegava, ganancias are covered by the known entries.

Findings refused:
- desafié "formal breaking of feudal ties": interpretive but harmless and consistent with Pidal's note to 965. Left.
- lês "= les ha venido": the modern equivalent uses haber, correctly. Left.
- sea broaden ('let it be', hortatory): close to the known 'may be' but useful for aquí sea la batalla. Left.
- Known tornós 'she turned back' (subject he here): an old entry, general enough. Left.

## Readings left uncertain

- v. 960 follón: 'arrogant' from the context (paired with vanidat); no footnote.
- v. 972 se le … cuyda[n] tomar: how se is construed.
- v. 975 lês = les + es: no footnote.
- v. 993 coçeras and amojadas: no gloss by Pidal for either word; 'insecure' follows his description in the note to
  1007; 'slack' is the context.
- v. 1003 de’llaño read as del llaño, and the unexpressed subject of çerca es.
- v. 1004 mandólos ferir: los the Çid's men (more likely) or the Franks.
- v. 1014 un salto dava: subject and sense.
- v. 1017 cozínal = cozina + l(e), and v. 1018 the force of ge in gelo.

## For the owner

- No defect found in the pinned text: every letter, italic and mark checked above agrees with the scan.
- The count's name: the poem's Remont Verenguel is Ramón Berenguer in modern spelling, but Pidal identifies the
  historical count as Berenguer Ramón 'the Fratricide' (note to 958). The notes now say both; `i` keeps the
  poem's "Remont".
