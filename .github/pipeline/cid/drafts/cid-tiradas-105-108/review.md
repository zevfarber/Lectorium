# Review: cid-tiradas-105-108 (tiradas 105–108, vv. 2131–2189, with 2127–2130 in print order)

Checked against the pinned packet; Pidal 1923, PDF pp. 265–269 (printed 261–265: text, italics, margin labels,
the rubrics of tiradas 105–108 and the footnotes 2133, 2137, 2138, 2147, 2148, 2152, 2157, 2160, 2164, 2168,
2172, 2178, 2185, 2188); the established texts of earlier parts for every verse cross-reference (41, 175, 204,
205, 1067, 1400, 1405, 1449, 1706, 2088, 2097, 2123, 2125); the published parts (pilot, 10-14, 84-86, 91-94,
102-102, 103-104a, 104-104b, 104-104c and the rest for names, brackets and the formula family);
`conventions.md`; and `cid-glossary.json`.
`t` integrity (by script, before and after the edits): all `t` joined by "\n" equal the 63 packet verses in print
order (2127–2130 between 2155 and 2156); 27 units, none over 6 verses (largest 4), none across a tirada break;
every `l` has one line per verse; no `t` was touched. Both files were edited by script (json load/replace/dump,
indent 1, ensure_ascii=False).

## Pass 1: units.json

1. 2185 (vv. 2185–86) · l + i + n · **error** · "buena çinxiestes espada" was read as 'a good sword you girded
   on' (`l` "good you-girded sword", `i` "you who girded on a good sword", note "here buena goes with espada").
   It is the en buen ora formula with en and ora both left unsaid: the glossary's buena already says so, and the
   same elliptical buen[a] stands at vv. 41, 175, 1706 (girding) and 294, 379, 2053 (birth), all rendered by the
   house formula. An adjective split from its noun by the verb, in a greeting, would be unique. Pidal has no
   note on it. Done: `l` "(in) a-good (hour) you-girded sword!", `i` "— in a good hour you girded on your
   sword!", note rewritten (buena printed whole, in roman, stands for buen(a) ora; not with espada).
2. 2131 (vv. 2131–34) · n · **error** · "Pidal's note: … (for dar, 'to give away', compare v. 1405)": Pidal
   gives no sense; v. 1405 is Dio tres cavalleros Minaya, where dar is 'to dispatch, assign' (the glossary's
   Pidal 'despachó, envió'). The draft put a gloss in Pidal's mouth that the cross-reference contradicts. Done:
   "(for dar, compare v. 1405, Dio tres cavalleros, where dar is 'to dispatch, assign', Pidal 'despachó, envió')".
3. 2131 · l · **weak** · "give an-agent to whom them he-may-give": a qui las dé is 'to one who may give them'
   (qui = 'he who', as the note says); "to whom" reads as the receiver. Done: "to one-who them may-give".
4. 2182 (vv. 2182–84) · i · **weak** · "rode into the citadel": entrava says only 'was going in'. Done: "went
   into the citadel".
5. 2160, 2167, 2175 · l · **style** · "Valencia" in `l`: the house keeps the printed Valençia in `l` (64-68,
   69-74, 84-86, 96-101, 104-104c …), "Valencia" in `i`. Done in all three.
6. 2174 · l + n · **style** · "to-the Infantes": a ifantes has no article, and the part's other `l` lines say
   "of Infantes", "to Infantes". Done: "to Infantes"; the note adds that ifantes goes without the article as at
   vv. 2162, 2171, 2178.

Points the brief asked to weigh, judged:
- en buen ora family at 2185: see item 1; the house formula applies.
- "Asur González" in `i` for A[n]su[o]r Gonçál[v]ez: kept. Pidal's footnote (2172, PDF p. 268) names him
  "Asur González" and says he was the Infantes' elder brother. House practice for names spelt variously in the
  manuscript is a normalized name in `i` with the manuscript form kept in `l` (Galind Garçiaz / Galín Garcia[z]
  "Galín García"; Albar Albar[oz] "Álvar Álvarez"); Per Vermudoz keeps the text form because it is spelt one
  way. The note says the English form is Pidal's. Kept; a conventions line is proposed below.
- "w[e]nt" for f[o]ron at 2182: kept. It is house practice to carry a restored letter of a verb form into the
  English word (f[o] "w[as]" at 1993, and wa[s], h[i]s, s[e]e … in 83-83b to 96-101). The practice is not
  systematic (alcáç[er] "citadel", se[d]iendo "being" go unbracketed here and in 104-104b), and it is
  untouched here, as in earlier parts.
- Ximena: "Ximena" in `i`, note and titles, as in every published part except where Pidal's rubric (Jimena) is
  quoted. Right.
- Tirada rubrics and assonances: 105 á with á-e (natural, plaz, tomades, alabarán, Fáñez, ifantes, delant,
  velar, verdat); 106 á-o; 107 ó with ó-e (mejores, mayores); 108 á-a. All four rubrics quoted exactly (checked
  on the scan). Kept.
- vv. 2127–2130: on PDF p. 267 they stand straight after the rubric of tirada 107 and before 2156, labelled
  2127 and 2130; no footnote explains it. The note says so and says the numbers put them after v. 2126, inside
  the Çid's reply. Right; kept.
- 2162 Carrión: the scan has "Carrióu" (turned n) with no closing punctuation; the next line ends "Sol.”". The
  note says so. Kept.
- Pidal footnotes quoted (2133, 2137 with the 1297 document, 2138, 2147 embargado, 2148, 2152, 2157 with
  v. 1067, 2160, 2164 with v. 1400, 2168 with v. 1449, 2172, 2178, 2185 with v. 204, 2188): accurate, apart
  from item 2. The cross-references 204, 205, 2088, 2097, 2123, 2125 checked in the established texts.
- Italics: de[n]d, [treínta], R[o]y, se[d]iendo, [recabdo] (with its !), di[o], mi[o], luégo[l], Di[a]go,
  Vermu[doz], s[u]s, A[n]su[o]r Gonçál[v]ez, [e], se[e]d, f[o]ron, alcáç[er] — the notes describe each right.

Grammar labels confirmed: casades, tomades, dé (pres. subj. in a relative of purpose), prendellas (-dl- > -ll-),
daldas (-dl- > -ld-), juntáredes / viniere / apuntare (future subjunctive), fosse (imperfect subj., 1st sg.),
oviemos (preterite), tomedes / plega / ayades / ponga / vaya / veamos (present subjunctive), tengon (Pidal
'téngome'), sediendo (gerund of seer), Veriedes (conditional), hiremos, plogo, mengó, sopiessen, gradídmelo,
vos he casadas (participle agreeing with the object).

Refused / left as drafted:
- 2136 `i` "tell me truly how it went" for quem digades la verdat: "how it went" makes explicit what the truth is
  about (the king's own wedding proxy reporting back); `l` keeps the literal. Left.
- 2172 `i` "in all else of little worth" for non es tan pro: the litotes is fairly read; the note has 'not so
  worthy'. Left.
- 2131 `i` "my natural lord and king" for rey natural: the note explains 'natural king'; acceptable elevation.
  Left.
- 2177 `i` "quarters of their own": un reyal for the Infantes alone; acceptable. Left.
- 2164 (v. 2166) `l` "Campeador" for printed Canpeador: the house `l` normalizes this epithet nearly everywhere (two
  exceptions in 27-31, 83-83a); the note records the n. Left.

Pass 1 counts: error 2 · weak 2 · style 2 (6 items).

## Pass 2: gloss.json

1. manero · **error** · 'means, arrangement … Pidal's sense of the word is not certain to me, so the gloss is
   tentative': Pidal's footnote (2133) is explicit. Done: 'representative, proxy', Pidal 'designad un
   representante' o apoderado, dar por manero a uno.
2. tengon · **error** · analysed as tengo + -n of ende 'of it' ("likelier, not certain"): Pidal 'téngome', and
   the unit reads tengo + me (-m written n). Done.
3. tráyovos · **error** · "trayo, with -y- from the Latin -g-": Latin trahō has no g. Done: "trayo, the old
   form beside traigo".
4. dessí · **error** · "de + essí": an invented form; the unit has des + í 'there'. Done, with Pidal 'allí
   mismo se separó de él'.
5. __broaden__ he · **error** · the glossary has only aver 'I have'; at 2163 he de fijas is 'and' (the unit's
   note says so). Added.
6. dad · **weak** · "give a means to whoever shall give them away". Done: 'name a proxy …', Pidal.
7. tomades · **weak** · "when you take them": the unit reads quando as causal 'since'. Done.
8. sed · **weak** · "= sed, sé vosotros" (sé is singular) and "also written se[e]d" (seed has its own entry).
   Done: both removed.
9. velar · **weak** · hedged "only moderately certain" and 'right up to the veiling': Pidal's note is plain and
   the unit has 'through the whole of'. Done.
10. enbargado · **weak** · 'burdened, embarrassed, put under obligation'. Done: 'overwhelmed', Pidal
    'abrumado' a fuerza de atenciones.
11. daquend · **weak** · 'henceforth': not in this line. Removed.
12. escurra · **weak** · "derivation uncertain, sense from context": Pidal's note 2157 gives the sense. Done,
    with escurriólos v. 1067.
13. fazednos · **weak** · "grant us this leave, i.e. let us go": Pidal 'perdonadnos esto'. Done.
14. fernando, diago · **weak** · 'the elder / the younger Infante': nothing here says which is elder. Done:
    "one of the two Infantes of Carrión".
15. ansuor · **weak** · "= Ansur": Pidal's form is Asur, the Infantes' elder brother, as the unit has. Done.
16. bullidor · **weak** · 'boastful person'. Done: 'rowdy, a stirrer', Pidal 'bullanguero'.
17. largo · **weak** · 'here generous with, free of': largo de lengua is 'long of tongue', as the unit has.
    Done.
18. reyal · **weak** · 'royal camp, encampment': Pidal 'real, albergue', the unit 'quarters, lodging'. Done.
19. __broaden__ luégol · **weak** · the entry is pinned to 'at once it' (luégol atravessavan); here le is 'from
    him'. Added.
20. __broaden__ fosse · **weak** · only 'he were'; commo si fosse delant is 1st sg., 'I were'. Added.
21. __broaden__ pero · **weak** · only 'San Pero'; don Pero here is Per Vermudoz. Added.
22. daquent · **style** · Pidal 'aquí' added.
23. sobrel · **style** · "final e dropped" tidied to "the two e's run together".
24. hiremos · **style** · "prothetic h-" implies a sound; "the h- only a spelling", as the unit says.
25. soltó · **style** · Pidal 'dejó marchar libremente' added.
26. gonçálvez · **style** · "Ansur González" → "Asur González"; the supplied v noted.
27. esposas · **style** · 'wife, bride' → 'betrothed, bride'.
28. adugo · **style** · Pidal 'os traigo' added; "= aduzco, traigo" → "= traigo".
29. __broaden__ sol · **style** · the entry has no sense for the name (doña Sol). Added.

Checked and kept: dé, alabarán, respondió, prendellas, daldas, padrino, juntáredes, verdat, oviemos, tomedes,
enssellados, plazer, galardonado, servido, sediendo, parto, ponga, andantes, espedirse, mengó, ganó, mañas,
lengua, afelos, assomaron, mayores, apuntare, veamos, gradídmelo; __broaden__ afé (que-clause), pro (adjective,
2173), puesto ('settled', 2141), quitó ('parted from', 2157), each needed. Every __broaden__ is the glossary
entry whole + " · " + the new reading (checked by script). The keys of gloss.json minus __broaden__ equal
novel-forms.json (54). The 209 known forms were checked against this part's readings; buena, quando, mandado,
recabdo, seed, foron, i, al, quel, dend, ca already cover them.

Pass 2 counts: error 5 · weak 16 · style 8 (29 items).
