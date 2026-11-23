# Review: cid-tiradas-109-111 (tiradas 109–111, vv. 2190–2277)

Checked against the pinned packet; Pidal 1923, PDF pp. 269–274 (printed 265–270: text, italics, the rubrics of
tiradas 109–111 and the footnotes 2193, 2199, 2200, 2206, 2207, 2212, 2217, 2220, 2222, 2223, 2224, 2226, 2228,
2233, 2238, 2243, 2249, 2251, 2256, 2259, 2263, 2270, 2272, 2275); the established texts and the published story
files for every verse cross-reference; `conventions.md`; `cid-glossary.json`.
`t` integrity (by script, before and after the edits): all `t` joined by "\n" equal the 88 packet verses; 34
units, none over 6 verses (largest 4), none across a tirada break; every `l` has one line per verse; no `t` was
touched. Both files edited by script (json load/replace/dump, indent 1, ensure_ascii=False).

## Pass 1: units.json

1. 2253 (vv. 2253–55) · l + n · **error** · al was used twice: the note read sines al 'without other thing' and
   then al çiento 'the hundred', and `l` had "without other the hundred". One al cannot be both. Done: al goes
   with sines ('without anything else', as the glossary's al 'other thing', lo al v. 2173); `l` "in beasts
   without other a-hundred [he-has] given"; note says çiento has no article, the line is terse and Pidal has no
   note on it (none on the scan). `i` ("in beasts alone — has given away a hundred") already read it so; kept.
2. 2256 (vv. 2256–57) · n · **error** · "past counting (compare v. 915)": v. 915 is Quando esto fecho ovo, a cabo
   de tres se[d]manas. non son en cuenta stands at vv. 918 and 1983. Done: "(non son en cuenta, vv. 918, 1983)".
   For the owner: the conventions line from 103-104a also says "(cf. v. 915)"; it should be 918.
3. 2203 (vv. 2203–04) · l + n · **weak** · ca non yo rendered "for not I", and the note called ca "usually 'for',
   here only sets the two sides against each other". The glossary already has ca non 'and not (that)' (Pidal 'y
   no que', v. 1839), which is this use. Done: `l` "and-not I"; note points to ca non at v. 1839 and says it is not
   the causal ca.
4. 2249 (vv. 2249–50) · n · **weak** · "Pidal's note sends to v. 1602: the tablado was a little castle of
   boards …": Pidal's note here is only "tablados, v. 1602"; the description is the house gloss, not his words
   at this line. Done: "Pidal's note here is only 'tablados, v. 1602', where the knights at play broke tablados:
   a tablado was …".
5. 2227 (vv. 2227–29) · i + n · **weak** · `i` "The ladies rise and stand, and he gave them into his hand": the
   "he … his" leaves the reader guessing; Pidal's note 2228 is plain (el Cid las entrega en manos de Minaya). Done:
   "The ladies rise to their feet, and the Çid gave them into Minaya's hand"; the note marks ge as singular
   ('to him', Minaya).
6. 2210 (vv. 2210–13) · i · **style** · "The Infantes ride out and made their way": the epic tense-mixing
   belongs in `l` and the note, not in the English. Done: "mount and make their way".
7. 2238 (vv. 2238–40) · i · **style** · "gave them the blessings and has sung the mass": same. Done: "sang".
8. 2274 (vv. 2274–75) · n · **style** · des = de + es (ese) is right but unsupported. Done: "(as en es día,
   v. 1678)"; the glossary's es already has 'that (apocopated esse)'.

Points the brief asked to weigh, judged:
- 2275 des: the drafter's analysis (de + es, es the shortened ese, 'of that') is right and is kept; the
  glosser's "de + este, the final -e lost and the t assimilated" is an invented sound change (de + este gives
  dest/deste, which the poem has at v. 2276). Glossary brought into line (pass 2). Pidal's 2275 note says
  nothing on des.
- 2213 a sabor: kept. 'at (their) pleasure, at ease', as the glossary's a so sabor 'at his pleasure'; it suits
  qué quedos entraron. Pidal has no note.
- 2258 acordados: kept as drafted ('agreed, of one mind', hedged, with the 'well-advised' of 2217 offered).
  Pidal's only note is at 2217 ('prudente', v. 1290), which the 2217 unit quotes right. The glossary entry now
  carries both senses.
- 2255 sines: see item 1.
- 2270 rastados: kept; Pidal 'han quedado' quoted right; a rastado at v. 1733 checked.
- Title "Ximena glad, the Cid wary; the weddings in Valencia": kept. Ximena is the house spelling in titles
  (105-108: "the Cid tells Ximena"); parts.json's "Jimena … uneasy" follows Pidal's rubric spelling. "wary"
  fits what the Çid actually says (he puts the match on the king) as well as "uneasy" fits Pidal's recela; no
  ground to overrule the drafter.
- Cross-references flagged by the drafter: 247 (prendet de mí ospedado), 1716 (de Valençia dieron salto), 1733
  (a rastado), 1762 (ivan posar … preçiosos escaños), 1902 (amas a dos), 2052 (se le omillan iffantes), 2088
  (afellas en vuestra mano): every one right, none off by one (established texts and published files agree).
  Also right: 48, 52, 804, 1169, 1290, 1577, 1602, 1905, 2080, 2093, 2131–2140, 2137, 2141, 2148, 2149, 2163,
  2172, 2173, 2183, 2187, 2189. Wrong: 915 (item 2).
- Pidal attributions checked on the scan: rubrics 109, 110, 111 (exact); notes 2193, 2199, 2200 (with v. 2080),
  2206, 2207, 2212, 2217, 2220, 2222, 2223, 2224, 2226, 2228, 2233 (with v. 2137), 2238, 2243 (with v. 1577),
  2251 (with v. 1169), 2256 (with v. 804), 2259, 2263, 2270, 2272, 2275 — accurate, apart from item 4.
- Italics: every bracket described rightly (de quien son servidas, vu[e]stro, creçr[e]mos, se[e]r, s[o]s,
  el[l]e, Jero[me], vi[d]ie, alcaç[er], [cr]ebantaron, [ha], f[o]ron, ave[r]es, R[o]y, Di[da]go, co[m]de,
  Gonçal[v]o).

Grammar labels confirmed: casáredes (future subjunctive), creades / prendan / vavamos / plega / pague / vala
(present subjunctive), tomassedes / entrassen (imperfect subjunctive), creçremos (syncopated future), abriedes
(conditional), sabet / venit / dadlas (imperative), sope / metí / nasco / tovieron (strong preterites), vi[d]ie /
sedié (imperfects), seer 'to sit', pedidas … rogadas and avien dados (participle agreeing with the object), son
juntados / es levantado / venidos son / son rastados (ser + participle), the enclitics (Besáronle, Metivos,
métolas, Afevos, dovos, metiógelas, vistiós, sediellos, dióles, espidiéndos, ques, aquis, yas).

Refused / left as drafted:
- Restored letters carried into English words ("yo[u]r", "gr[o]w", "w[e]re", "co[u]nt"): house practice (see
  105-108 review); left.
- 2274 `i` "have joy of that marriage" for ques pague des casamiento: fair for pagarse de; left.
- 2192 note: menguadas read as the daughters, hedged ("most likely"); left.
- 2230 note "Minaya points to himself": Afevos delant Minaya is Minaya naming himself in the third person; fair.
  Left.
- 2205 rubric summary "the weddings end with gifts to the guests" for "Las bodas acaban; regalos a los
  convidados": the Spanish is quoted in full beside it; left.

Pass 1 counts: error 2 · weak 3 · style 3 (8 items).

## Pass 2: gloss.json

1. metiógelas · **error** · "ge, = les 'to them' … 'he placed them in their hand'": ge is singular here, Minaya
   (Pidal 2228 'las entrega en manos de Minaya'). Done.
2. rastados · **error** · "the form is unclear, perhaps (re)stados … or a scribal slip for fincados": invented;
   Pidal glosses son rastados 'han quedado', and the glossary has rastar (a rastado, v. 1733). Done.
3. duraron · **error** · 'they lasted … at the wedding feast': the subject is the guests and Pidal 'emplearon,
   gastaron'. Done: 'they spent (time)'.
4. encortinado · **error** · "Pidal 'colgado de cortinas'": not his words; his note is 'cubierto de tapices por
   el suelo y por las paredes'. Done.
5. __broaden__ des · **error** · "de + este, the final -e lost and the t assimilated": invented sound change.
   Done: de + es (the shortened ese) 'of that', matching the unit and the glossary's es.
6. __broaden__ sines · **error** · "'in animals, up to a hundred' (Pidal; …)": Pidal has no note on v. 2255, and
   'up to' is not in the line. Done: sines al 'without anything else'.
7. __broaden__ mandado · **error** · gelo he mandado glossed 'I have ordered it to him': Pidal 2223 'otorgado, o
   prometido', already covered by the entry's 'granted'. Done: the new sense is only 'ordered, charged'
   (a mí lo ovo mandado), with a pointer for 2223.
8. acordados · **weak** · pinned to 'in accord … likelier here': the form also stands at 2217 where Pidal says
   'prudente'. Done: both senses.
9. sediellos · **weak** · "whose l assimilated": nothing assimilates; the l is written double. Done.
10. vavamos · **weak** · "with b/v and -ay- for -av-": meaningless. Done: so printed, Pidal paraphrases vayamos.
11. xámed · **weak** · "Greek hexámitos via Arabic … closest 'seda rica'": unsupported route and not Pidal's
    gloss. Done: Pidal 'tela de seda'.
12. âlgo · **weak** · "the sense unclear: perhaps … or 'had it for gain'": Pidal gives the sense ('el que lo
    estimó en algo'). Done: aver a algo 'to hold in some esteem', the reading doubtful.
13. __broaden__ mandados · **weak** · 'ordered, given' of the mounts: mandar here is 'grant, bestow'. Done.
14. __broaden__ pague · **weak** · entry only 1st sg. (fata que yo me pague); here 3rd sg. Added.
15. __broaden__ parando · **weak** · entry only 'leaving (them black)'; here parar mientes. Added.
16. __broaden__ partiendo · **weak** · entry only 'sharing out'; here 'departing'. Added.
17. __broaden__ sí · **weak** · entry only the optative particle; here por sí 'for himself'. Added.
18. __broaden__ posar · **weak** · entry only 'to lodge'; here 'to sit' (on a bench). Added.
19. casáredes · **style** · "you shall marry (to us)" → "marry (someone) off, give in marriage".
20. reçibiólos, métolas, dióles · **style** · "accent shifted": the stress does not move; the accent is written.
21. sperando · **style** · "prosthetic e lost" → "spelt without the initial e".
22. preciado · **style** · noted the missing cedilla (lemma preçiado).
23. recabdando · **style** · "= recaudando" (modern 'collect taxes') → Pidal 'despachando'.
24. tovieron · **style** · Pidal 'jugaron las armas' added.
25. amores · **style** · Pidal 'los agasajos' added.
26. levanté · **style** · Pidal 'no lo inicié, no lo hice' added.

Checked and kept: servidas, menguadas, pedidas, rogadas, atan, cosa, sope, metivos, ados, creades, suelo,
pórpola, paño, abriedes, seer, adeliñavan, quedos, ssu, omillaron, preçioso, escaño, mientes, levantado, imos,
tardando, amo, affé, sabedes, fallir, bendiçiones, estoz, levántanse, derechas, tomassedes, palacio, adelinnando,
eclegia, bendictiones, cantado, ecclegia, cavalgaron, cameó, vidie, cavalgado, alcaçer, siete, entrassen,
crebantaron, dones, abastado, ospedados, espidiéndos, gonçalvo, hyernos, moran, cerca, coplas, acabando;
__broaden__ casa (casar 'marries off'), needed. Every __broaden__ (10) is the known-forms entry whole + " · " +
the new reading (checked by script). The keys of gloss.json minus __broaden__ equal novel-forms.json (77). The
275 known forms were checked against this part's readings; ca (ca non 'and not'), al ('other thing'), es
('that'), sabor, parado, largos, cuenta, fincar, corredores, salto, armas, aguisado already cover them.

Pass 2 counts: error 7 · weak 11 · style 8 (26 items).
