# Review — cid-tiradas-138-143 (vv. 3250–3328 incl. 3259b, 3290b, 3318b; tiradas 138–143)

Checked: every unit's `t`/`l`/`i`/`n` (39 units) against the pinned packet, conventions.md, the pilot and the published
parts (grep of cid-tiradas-*.json for telas del coraçón, a nombre, ifançones, primas, rencura, poridad, deliçio); the scan,
PDF pp. 332–337 (printed 328–333) whole at zoom 1.4, with clips at zoom 5–16 of the footnotes to 3268 (*incurrís*,
*debía*), 3289 (every accent: *índice*, *debía* ×2, *había*, *podia*, *tenía*, *debían*, *Así*), 3290 (*tenía*, *aún*,
*sólo*, *remesón*, *Según*, *fué*), 3304 (headword *a tí*, *a ti* in the gloss), 3308 (*Martín Antolinez*). Every Pidal
footnote quoted in the notes (3251, 3256, 3262, 3264, 3268, 3269, 3272, 3277, 3282, 3283, 3286, 3289, 3290, 3295, 3298,
3304, 3307, 3308, 3316, 3318, 3319, 3320, 3321, 3322, 3326, 3327) and the rubrics of 138–144 were compared letter by
letter with the print: all exact except the accents of 3289 and 3290 (items 8, 11 below). Italics of the part seen:
[ya] 3253, [de Carrión] 3258, co[m]de 3270/3283/3287, ta[n] [alta] 3275, lue[n]ga 3282, f[o] 3282/3284, 3290b wholly
italic, Go[n]çál[v]ez 3291, co[m]des 3296, R[o]y and Vermu[doz] 3301/3306, respondier[o] 3305, costu[n]bres 3309,
pu[o]do 3311, tu[e]s 3315, [él] 3318b, qu[o]mo 3328. Paragraph indent confirmed at 3253 and 3313. Cross-references
checked in source/established: 289, 1345, 1413, 2337–2340, 2351, 2381, 2578, 2671, 2736, 2785, 3097, 3124, 3185.

The `t` fields joined by "\n" equal the packet's 82 verses in order (script); no `t` changed; every `l` has as many lines
as its `t`; both files parse after editing (asserted by the edit scripts). Keys of gloss.json = novel-forms.json +
`__broaden__` (asserted); every broaden value starts with the known entry whole + " · " (asserted).

**Establishment: no error found.** 3259b label damaged (prints like "3?50b"), verse roman; 3290 *eguada* damaged but
legible as such; 3258 *merecí*, 3295 *creciés* without cedilla as printed; 3301 *Mío* accented; 3311 *mas* unaccented;
3328 opening ¡ and closing ? as printed.

Title kept: "The Cid charges the Infantes with dishonour; Per Vermudoz challenges Fernando".

## Pass 1: units.json

1. 3253–3254 · n · weak · "se impersonal" misnames the construction: la rencura is the subject of a reflexive passive ·
   relabelled.
2. 3258–3259b · n · style · "printed without the cedilla, as printed" · "as printed" dropped.
3. 3260 · i · style · "strip me to the very membranes of my heart" differs from the published `i` of the same phrase
   (vv. 2578, 2785: "the very strings of my heart") · now "Why did you lay bare the very strings of my heart?".
4. 3260 · n · weak · the reading a qué + me was not flagged, and "the Çid means his daughters" was stated as fact · quém
   marked as our reading (Pidal no note); the daughters linked to v. 2578, where the Çid gives them as las telas del
   coraçón; cross-reference to 2578/2785 added.
5. 3261–3262 · i · style · "wealth past counting" (the house "past counting" belongs to non son en cuenta); averes
   [a nombre] at 128–130 is "riches in plenty", Pidal 'en abundancia' · now "wealth in plenty".
6. 3272–3274 · n · style · espanta given only as "he frightens" · subject unnamed, he or the beard, said.
7. 3275–3277 · n · weak · ge 'from him' given as fact (the drafter's own point 15 calls it a reading); "Pidal reads o as
   'then'" overstated a paraphrase · ge marked a reading; "Pidal's paraphrase renders o by pues, 'then'".
8. 3288–3289 · n · error · Pidal's footnote quoted with *indice*, *debia* (first), *habia*, *debian* unaccented: at zoom
   12–14 all four carry a slanted accent (only *podia* has a round dot) · corrected to *índice*, *debía*, *había*,
   *debían*.
9. 3288–3289 · n · style · "(Accents as read on the scan, several faint …)" · now "Accents as printed: podia alone
   without"; the *carne/carae* remark kept.
10. 3288–3289 · i · style · "stable-lad" adds what rapaz does not say · "a lad there".
11. 3290–3290b · n · error · *tenia que alimentar* quoted unaccented: the mark is a slanted accent at zoom 16 (compared
    with the round dots of *injuria* on the line above) · *tenía*.
12. 3293–3295 · n · style · "without the cedilla, as printed" · "as printed" dropped.
13. 3296–3298 · i, n · style · "minor nobles" against the published "lesser nobles" (104–104c) and the drafter's own `l`
    · "lesser nobles".
14. 3303–3304 · n · error · "cormanas = hermanas de padre" (that is 'paternal half-sisters') · now cormano < Latin
    germanus, 'cousin-german', modern primas hermanas.
15. 3313–3314 · i, n · weak · "you were all worth" and the plural taken as certainly both Infantes · `i` "you were worth";
    note says "seems to widen … (our reading; the plural may only be loose)".
16. 3319–3320 · i · style · "I rode on past you" adds the horse; Pidal 'pasé más allá de ti' · "I went on past you".

Refused:
- Re-quoting *Antolinez* with an accent (3308): no accent or dot is visible; quoted as printed, "Antolínez" in English.
- Changing *mal varragán* "a sorry fighter" to "coward": Pidal's 'cobarde' is quoted in the note; the `i` keeps the
  word's own shape (bad + valiant man).
- Changing "If I make the answer, you will not go into the lists" (3305): flagged as a reading, sense defensible.
- Changing the drafter's *nada* 'born' reading: flagged in the note as ours; Pidal gives only the sense.

## Answers to the drafter's readings

1. 3268: *incurrís* and *debía* — both accented, confirmed at zoom 10.
2. 3289: corrected — *índice*, *debía* (both), *había*, *tenía*, *debían*, *Así* accented; only *podia* unaccented
   (item 8). *carne* damaged, read carne: right.
3. 3290: *tenia* is *tenía* (item 11); *aún*, *sólo*, *remesón*, *Según*, *fué*, *auie* confirmed.
4. 3298: *nuestra de ıa* and *sorros* damaged as said; quoting muestra/somos with the flag is right.
5. 3304: headword *a tí* (italic, accented), gloss *a ti* unaccented: confirmed.
6. 3308: *Martín* accented, *Antolinez* plain: confirmed.
7. 3320: *más* damaged ("rrás"): read más, right.
8. 3259b: confirmed (label damaged, verse roman).
9. 3290b wholly italic, flagged; *eguada* reading supported by Pidal's *eguado*: right.
10. merecí, creciés, Mío, mas: confirmed as printed.
11. d'al "another matter": right; the singular/plural slide noted.
12. A quém = a qué + me: kept, now flagged as our reading (item 4).
13. sus honores beside Valençia: follows Pidal's 'heredad', kept.
14. 3272–3274 mockery of court-going and beard: kept (vv. 3097, 3124 confirm the bound beard).
15. gelas 3276 / 3277: kept; 3276 now flagged as a reading (item 7); 3277 'to them' rests on Pidal's 'se las dió'.
16. nada 'born': kept, flagged.
17. nimbla = nin + me + la with epenthetic b: right; the glossary entry now gives the same analysis.
18. alçada 'put away': right; broadened in the glossary.
19. Dexássedesvos as mild command: right.
20. entrarás en armas: kept as a flagged reading.
21. valiestes: plural kept, now flagged as a reading (item 15); full stop and lower-case por as printed: confirmed.
22. uviás 'had come up': right (Pidal 'llegase'); the glossary entry, which made it aver, corrected (pass 2).
23. tóveldo = tove + te + lo: right, Pidal 'túvetelo' confirms the te; glossary corrected to match.
24. mal varragán "a sorry fighter": kept.
25. Cross-references 3185, 2736, 2340, 2351, 2337: all checked and right.

## Pass 2: gloss.json

All 90 novel forms have entries; no extra keys.

1. quém · error · glossed as the relative 'who … me' of v. 3256 (that is *quem*, already known); *quém* is v. 3260's
   interrogative · now qué + me 'why … me' (a reading), consistent with the unit.
2. firiestes · error · "= herísteis": invented accent; modern heristeis · corrected.
3. diera · error · "would have given … conditional sense" against Pidal's 'se las dió' · now -ra form as plain past,
   'gave', = dio.
4. uviás · error · lemma aver, 'if I had (been there)', "2nd sg. type", flagged uncertain · now uviar 'come up, arrive in
   time', 1st sg. imperfect subjunctive with -sse dropped (as fincás), Pidal 'si yo no llegase'; flag removed.
5. tóveldo · error · "tener + le + lo … tóvele … tóvelo > tóveldo" · now tove + te (> d) + lo, tovedlo > tóveldo,
   Pidal 'túvetelo en secreto'; flag removed.
6. did · weak · "perhaps di + te … or paragogic (uncertain)" · Pidal 'dite el caballo' settles it: di + te; flag removed.
7. delibrar · weak · flagged uncertain though Pidal glosses it · Pidal 'no puede romper a hablar' added; flag removed.
8. respondiero · weak · "the ending -o is Pidal's form (uncertain)": the o is a restoration, the form not doubtful · now
   "the final o restored by Pidal"; flag removed.
9. mataras, fizieras · weak · "imperfect subjunctive" misnames the -ra form used as pluperfect indicative (the units
   say pluperfect) · relabelled; = habías matado / habías hecho.
10. croviérontelo · weak · "ethic dative" misnamed · dative of the person believed.
11. varaja · weak · 'quarrel, strife' only · Pidal 'pleito', 'alegación de dos partes litigantes ante el juez' added.
12. orejadas · weak · 'box on the ear', = bofetadas, against Pidal's ear-pulling (orejear 'tirar de la oreja') · now
    'ear-pulling', = tirones de orejas.
13. espanta · weak · 'the beard being the subject' stated as fact; the unit says he · subject unnamed, Çid or beard.
14. mudo · weak · pun said to be "on the name Pero" · on Vermudo(z).
15. barnax · weak · "= barnage, barnaje": French and a doubtful modern form · from barón, cf. Old French barnage; =
    hazaña, proeza.
16. varragán · weak · "'a poor valiant man'" · mal varragán 'a sorry fighter', Pidal 'cobarde'.
17. valiestes · weak · preterite translated as present ('you are worth') · 'you were worth'.
18. apreçiaduras · style · = tasaciones · Pidal 'especie', = pagos en especie (as the known apreçiadura).
19. llas · style · "ll by assimilation after a" (unsupported) · "l doubled, as printed".
20. nimbla · style · lemma ni + me + la, 'from me' · nin + me + la, n > m, epenthetic b.
21. bolsa · style · "kept up in my purse" · "put away".
22. enpieça · style · lemma empeçar for a form spelt with n · enpeçar.
23. jugara · style · = jugaría · Pidal 'mal te hubiera burlado'; = habría jugado.
24. fústel · style · = fuiste a él · Pidal 'le fuiste a acometer'.
25. __broaden__ nombre · weak (added) · known entry "perhaps … he gives no note; sense uncertain": his note to 3262
    settles a nombre 'in plenty'.
26. __broaden__ nada · weak (added) · participle 'born' (fijo de mugier nada), flagged as a reading.
27. __broaden__ puodo · weak (added) · known entry only preterite 'could'; here = puedo 'I can'.
28. __broaden__ valedes · weak (added) · menos valedes, the legal charge (Pidal 'incurrís en infamia').
29. __broaden__ alçada · weak (added) · known 'raised'; here 'put away, kept'.
30. __broaden__ ajuntar · style (added) · known only as a noun; aver de ajuntarse con 'close with'.
31. __broaden__ vagar · style (added) · dar vagar 'give rest' (Pidal 'reposo').
32. __broaden__ o · style (added) · ¿o quien …? 'then' (Pidal 'pues').

Checked and right: pésevos, desondraron, riebtos, merecí, vero, mejoraré, descubriestes, salida, queriedes, canes,
traidores, sacávades, espolones, solas, dexastes, recudedes, levantava, vezós, pregonadas, dexóla, alta, devién,
fizieron, porque, preçiamos, prísos, criada, cabra, rapaz, pulgada, messé, eguada, ferrán, dexássedesvos, ssodes,
creciés, perteneçien, dexamos, fiziemos, mío, cata, callas, cormanas, entrarás, detiénesle, dirévos, costunbres,
llamades, mancará, has, tues, sabré, miémbrat, lidiamos, pedist, vist, fuxiste, allegasses, passé, of, ofle, descubrí,
ovístete, alabar, osas; __broaden__ mientes (old entry whole + " · also mentir — you lie").
Glosser's uncertain flags: uviás, did, tóveldo, delibrar, respondiero — all settled by Pidal's notes (items 4–8); none
left flagged.
Refused: broadening *honores* ('heredad' is covered by 'lordship, fief'), *gelas* ('for/to him' covers the 3276
reading), *telas* (already 'what is dearest'), *ensayar* ('attack' present), *arrancar* (active 'rout' present).

## House renderings for conventions.md (final list)

- riebto/riepto "challenge" in `l`, "a (formal) challenge" in `i`: the public charge before the king's court (Pidal reto).
- menos valer / menos valedes "worth less" in `l`, "worth less, dishonoured" in `i` (Pidal 'incurrís en infamia').
- Pero Mudo kept in `l`, "Pero the Mute" in `i` (pun on Vermudo(z), v. 3302).
- las telas del coraçón "the membranes of the heart" in `l`, "the very strings of my heart" in `i` (vv. 2578, 2785, 3260).
- averes a nombre "wealth/riches in plenty" (Pidal 'riquezas en abundancia', v. 3262).
- ifançones "lesser nobles" in `i` (104–104c, 3298).
- barnax "prowess" in `l`, "a deed of valour" in `i`.
- mal varragán "bad valiant-man" in `l`, "a sorry fighter" in `i` (Pidal 'cobarde'); barragán "valiant man" kept.
- Lengua sin manos "Tongue without hands" in `l` and `i`.
- cortes pregonadas "proclaimed courts" in `l`, "the solemn courts" in `i` (Pidal 'cortes solemnes').
- varaja "dispute" (Pidal 'pleito').
- orejadas "ear-pullings" (Pidal's note to 3304).
- primas cormanas "first cousins".
