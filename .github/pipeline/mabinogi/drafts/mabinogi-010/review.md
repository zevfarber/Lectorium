# mabinogi-010 — review

## Pass 1 (units)

Reviewer pass 1 (2026-11-14). I read all 102 units against conventions.md, packet.md (the established text and the establishment log, including the "For the drafter" summary), the published mabinogi-001 to 009 and drafts/mabinogi-009/review.md. For formulas and names I searched the published parts directly: *ym kyffes y Duw*, *dyd da*, *Duw a rodo / a ro da*, *Pan doy*, *ual y byd*, *broch yg got*, *Penn Annwn*, *a dotter*, *uym pryder*, *wely dy*, *y teruyna y geing*, *Gorssed Arberth*, *a gey*, *yrdaw*, *kanys/canys*, *tryded*, *ny myn-/ny uyn-*, *hut*, *ansawd*, *kyuarwydyd*, and Arglwyd in address. Aids: Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. Third witness: Rhŷs & Evans 1905 (Red Book), `source/raw/rhys-evans1905_djvu.txt`, printed pp. 54–58, read through the OCR's usual misreadings of 6, ſ and r-rotunda. No English translation was consulted. For every unit I checked each grammatical label in the note against the form, Welsh → `l` word by word, `l` ↔ `i`, the house renderings, and that every establishment-log item stands in the note of its unit. Edits were made by a Python script (load, change fields by index, dump with ensure_ascii=False, indent=1). No `t` was touched. Afterwards a script confirmed that there are 102 sentences and that the `t` list equals cut.json's exactly.

**Unit numbers are 0-based.**

### Changes

- 37 · n · major · The note said "the Red Book has ymodi here too". It has *teimlaw* (*rac dy welet yn teimlaw y pryf hwnnw*), as at 22; the establishment log names only the first place, and the drafter inferred the second wrongly. · The note now says the Red Book has *teimlaw* at both, so *ymodi* is the White Book's own word.
- 61 · n · minor · *gehy* was offered as "a by-form … or a slip for *geffy*". The Red Book has *Ti a gey hynny* here, which matches *a gey* in 009. · The note now takes *gehy* as a by-form of *gey* and cites the Red Book; the slip reading is dropped.
- 8 · l, n · minor · *ansyberwyt* had l "discourtesy". The house l is "un-courtesy". · l now reads "un-courtesy"; the note gives the house pair.
- 72 · l, n · minor · *a Guawl* had l "on Gwawl", while the note glosses 'with Gwawl, meaning on him'. Also, the object *guare* stands unsoftened after the subject *i*, which the note did not say, although note 11 explains *Orssed* by that very rule. · l now reads "with Gwawl". The note adds the unsoftened *guare*, which is also *gware* in the Red Book.
- 52, 53 · l, i, n · minor · 52 had "will-buy-her" / "buy her", and 53 had i "seven pounds for her", but *yrdaw* is the masculine 'for it/him'. The bishop goes on with *gollwng ef*, so the English changed gender mid-speech. · 52 l and i now read "it", and its note says why. 53 i now reads "for it". The log item (*a'y*, the mouse, f.) is kept as it was.
- 59 · n · minor · "after ny one expects uynny". The published parts write *ny mynneis* (002) and *ny mynnwys* (004) unsoftened, beside *ny uynhei* (007), and the Red Book also has *Cany mynny* here. · The note now gives the variation and the Red Book.
- 9 · n · minor · The reading of *a chanys gwnn* as *kan* + *nys* was argued without the Red Book, which has *a chanys nys gwnn*. · Added that reading, with the alternative it opens: the White Book may have lost a *nys* after *chanys*. The sense, 'since I do not know', stands either way.
- 55, 57 · n · minor · *Kanys gollyngy* / *Canys collyghy* were read as *kan* + *nys* on sense alone. The Red Book writes *Kan nys gollynghy* and *Kan nys gellyngy*, which confirms it. · Added to both notes.
- 39 · n · minor · *deir punt* "softened as an object separated from its verb". The rule is sound, but the note did not say that the Red Book has *teirpunt* unsoftened, or that *pedeirpunt* (55) stands unsoftened in the same position. · Added.
- 85 · n · minor · *ef a doy* was read as *doei* on sense alone. The Red Book has *ef a doei*. · Added.
- 5 · n · minor · "as 'them': the infixed pronoun 's attached to bei". The infixed pronoun is carried by the preverbal particle *a*, so *as* = *a's*. · Corrected.
- 74 · n · minor · Unsoftened *tryded*: the rule given (the ordinal is softened after the article before a feminine noun) is right. The note did not say that the Red Book also has *A'r tryded nos*. · Added.
- 4 · n · minor · *yr lygryssit*: the reading as *y* + *'r* (= *ry*) was left wholly open. The Red Book has the same *yr* before the verb. · Added, so the reader knows it is not a slip of this scribe. The analysis is still marked as not certain.
- 18 · n · minor · *Na weleis* as an answer to 'why?'. The Red Book makes the analysis explicit: *am na weleis* 'because I have not seen'. · Added.
- 94, 97 · n · minor · The vivid present *y gollwng hi* and *pan edrych* is right. The Red Book has preterites in both places (*y gellyngawd ef hi*, *a phan edrychawd ef*). · Added.
- 6 · n · style · *kymoned* was explained as "ky- + boned" with nothing on the *m*. · The note now says *kyf-* + *b* gives *kym-*.
- 0 · n · style · Establishment-log item: Evans writes *y2 ystauell* together, and the text divides *y'r* as the second witness does. · Added.
- 5 · i · style · "her I caught … hang her". Manawydan does not yet know the mouse is female, the Welsh has no pronoun here, and his next speeches say 'it'. · Now "that one I caught, and it is in the glove … hang it".
- 11 · l · style · *a sengi* had l "planting". The note glosses 'treading', and `l` follows the word. · l now reads "treading-in".
- 36 · i · style · *ar ansawd llygoden* had i "in the form of". *ansawd* is 'appearance' in the house table and the published parts. · Now "with the appearance of a mouse".
- 84 · l, i, n · style · *da y medreist* had "aimed", while the same verb in 85 is "hit". · All three now read "hit" ("you have hit the mark well").
- 53 · n · style · The base was given as "blwyned", where 13 has "blyned". · Now "blyned, mlyned, in 13".

Checked and in place: every establishment-log item has its note:
- the raised *y* (0), *h* (29) and *y* (47);
- the two "!" marks (19, 25);
- *caffwnn i wy oll* (7) and *a'y prynaf* (52);
- *geccaf* (94) and the dropped asterisk;
- *lledrith* (64) and *lletrith* (75);
- *ymodi* (22, 37);
- the three spellings of 'my wife' (68, 74, 92);
- *bydyn* and *kywein gueir* (99);
- *y geing* and *Mabinogy* (101), and *Mynweir a Mynord* (100);
- *doethwyf* (52), *eisswys* (6), *En llawen* (41) and *gehy* (61);
- *ar y seith meirch* (57) and *Y herwa* (70).

The following follow the house table: *heb ynteu*, *y rof a Duw*, *Ie*, *Dioer* (84), *Meuyl ymi*, *teulu* (household-troop / warband, 73), *kedymdeithas* 'fellowship' (71), and "Lord" in address throughout.

### Refused
- 39 · *deir punt*, the drafter's flag. The softening of an object separated from its finite verb by another word (here *it*) is a real Middle Welsh rule, and the note does not claim that *teir* softens *punt*. Kept, with the Red Book's variation added (above).
- 74 · *tryded*, the drafter's flag. The rule given is right and the form is shared with the Red Book. Kept, with the Red Book added.
- 52 · *doethwyf*. The analysis (stem *doeth-* with the 1 sg. ending *-wyf*, used as a perfect) is said to be uncertain, and the Red Book's *deuthum* is cited. Nothing better can be offered. Kept.
- 44 · *rwtter*. The Red Book has the same word, and the note already calls the form uncertain. Kept.
- 99, 100 · *yrd porth*, *kywein gueir*, *Mynord*. Each is already marked uncertain where it is, with the Red Book forms (*bydynt*, *kywein geir*, *mynnweir a mynoad*). Kept.
- 5 · *ym kyffes y Duw* "ym is 'my' (uy); the nasal … is not written". This matches the published note at 004 (34), which cites the Red Book's *ym kyffes i y Duw*. Kept.
- 12, 30 · *ual y byd* called "the vivid present". *byd* is properly the habitual present-future of *bot*, but the published notes at 001 (6, 14) and 004 (58) treat the formula the same way. Kept for consistency.
- 68 · i "I would not be seeking her release" for *nys dillyngwn* 'I would not release her'. In context the bishop is ransoming her, so this is a fair rendering, and `l` gives the bare words. Kept.
- 72 · *pan y gwnaeth*, with *y* as the infixed object. Middle Welsh *pan* normally takes no particle, so the infixed pronoun is the better analysis, and the note says "best taken". Kept.
- 19 · i "I am only passing through". This is a light gloss on the verbal noun put first (*mynet … yd wyf*). Kept.
- 91 · *a'y graessawu* with *'y* 'their' and *g* as the word's own initial. This is right. *graessaw/grayssaw* with *g* is the Middle Welsh form, and the Red Book has *greffaw*. Kept.
- 8 · *goglyt* glossed with modern *gochel*. It is a verbal-noun variant (*gogelyd/goglyd*) of the same verb. Kept.

## Pass 2 (glossary)

Reviewer pass 2 (2026-11-14). I checked every entry in gloss.json against the text where the form occurs and against the unit notes as they stand after pass 1. That covers all 142 new entries (one per key of novel-forms.json) and the 49 drafted `__broaden__` entries. For each entry I checked four things:
- the lemma: the Middle Welsh form first, then a real modern form or "no modern form";
- the meaning;
- the grammar: part of speech, person, number, tense and mood, gender;
- the mutation and its real cause.

I also read known-forms.json against this part's text, to find known entries whose sense or mutation cause would mislead a reader here. I checked every item the glosser flagged and carried the pass-1 corrections into the entries. For the third witness I used Rhŷs & Evans 1905 (`source/raw/rhys-evans1905_djvu.txt`, pp. 54–58), as in pass 1. Aids: Strachan, Morris-Jones, Silvan Evans and GPC (for meanings), from knowledge. No translation was consulted. Edits were made by a Python script (load, replace values, dump with ensure_ascii=False, indent=1). No unit note needed correcting, and no `t` was touched. Afterwards a script confirmed these points:
- the gloss.json keys other than `__broaden__` equal the novel-forms.json keys (142);
- no value is empty;
- each of the 60 `__broaden__` keys is in known-forms.json, and each value begins with the old entry verbatim + " · ";
- units.json has 102 sentences, and its `t` list equals cut.json's.

### Changes

- chanys · major · The entry glossed 'and since I know', which is the opposite of the sense; note 9 reads *kan* + *nys* 'since … not … it'. · Rewritten as *kan* + *nys* 'since I do not know it', with the Red Book's *a chanys nys gwnn* and the possible lost *nys*.
- gollyngy, collyghy · major · Each was glossed 'since you will release (it) for that', and the mutation was put down to *kanys*. *collyghy* was also offered a derivation from *colli*. *Kanys*/*Canys* is *kan* + *nys* here: the Red Book has *Kan nys gollynghy* and *Kan nys gellyngy* (notes 55, 57). · Both now read 'since you will not release it', radical after the infixed *'s*. The *colli* derivation is dropped.
- deir (broadening) · major · The broadening said "written deir with no softening cause …; teir does not soften, so d is a spelling for t". Note 39 gives the cause: the object is softened when *it* stands between it and the verb. · Now so, with the Red Book's *teirpunt* and the contrast with *pedeirpunt*.
- wanas · major · The entry gave 'a raised seat, platform, bench or stool', which does not fit a glove hung by its string. *gwanas* is 'peg, holdfast, support', as note 0 has it. · Corrected.
- dulath · major · The entry gave 'noose, loop', from *dul* 'noose'. The *dulath* is laid in the two forks: it is the crossbeam (note 30). · Corrected: second element *llath* 'rod, beam', softened in the compound; the first element is not clear.
- swmer, swmereu · major · The entries gave 'pack-horse'. The seven *swmer* are *on* the seven horses (*ar y seith meirch y maent arnunt*), so they are packs or loads, and `l` and note 44 have 'packs'. · Corrected.
- yrd · major · "perhaps a gate-fitting, post or leaf, or the borrowed 'yard'". Note 99 gives *ord* 'sledge-hammer' (modern *gordd*, plural *gyrdd*), and that is also the *-ord* of the title *Mynord*. · Corrected; what the gate-hammers were is left uncertain.
- wreigyang · major · The entry gave 'woman, … formed from gwreic with a suffix'. It is *gwreic* + *ieuanc* 'young woman'; the Red Book has *wreic ieuanc*. · Corrected.
- trewis · minor · The lemma was "trewi (modern form uncertain)". It is the preterite of *taraw* (*taro*), as note 94 says. · Corrected.
- dieleis · minor · The lemma was "dielu (dialu) … lemma form uncertain". It is *dial* (*dial*), as note 72 says. · Corrected.
- as · minor · The lemma was "bei + 's (ei)". *as* is the preverbal particle *a* carrying the infixed *'s* (note 5). · Corrected.
- ymodi · minor · "the Red Book has teimlaw … at a parallel place". The Red Book has *teimlaw* at both places (22 and 37; pass-1 major). · Corrected. The sense 'handle', taken from the context, and 'properly stir, move' are now as in note 22.
- gehy (broadening, new) · minor · The known entry did not say that this is a by-form of *gey*. The Red Book has *Ti a gey* here (note 61). · Added.
- mynny, cany (broadenings, new) · minor · The known *cany* entry says it softens the verb, but here *Cany mynny* is unsoftened, and so in the Red Book (note 59). · Added to both.
- kanys, canys (broadenings, new) · minor · The known entries give only plain 'since, for', which would mislead at 55 and 57. · Added the *kan* + *nys* use with the Red Book forms; *canys* also gets the plain use at 75.
- guare (broadening, new) · minor · Not noted: the object stands unsoftened after the subject *i* (note 72). · Added.
- yrdaw (broadening, new) · minor · The known entry has only 'for him, for his sake'. Here it is 'for it', the creature (note 53). · Added.
- tryded (broadening, new) · minor · Not noted: *tryded* stands unsoftened after the article before a feminine noun (*A'r tryded nos*; note 74). · Added.
- uydwn (broadening, new) · minor · The known entry has only "1 pl. future 'we will be'". Here *mi a uydwn* is 1 sg. imperfect, conditional, 'I would be'. · Added.
- gwnn (broadening, new) · minor · Added the radical *gwnn* after the infixed *'s* (*a chanys gwnn*).
- herbyn (broadening, new) · minor · The known entry has only *yn y herbyn* 'to meet her'. · Added *yn eu herbyn* 'to meet them'.
- doy (broadening) · minor · It said "3 sg. present/future 'will come'". Note 85 reads *doy* as *doei*, the imperfect 'would come', and the Red Book has *ef a doei*. · Corrected.
- golles (broadening) · minor · It said "'until the two were lost'". *y deu* is the object: 'until he lost the two'. · Corrected.
- hwnn (broadening) · minor · It said "'but the one that is due'; the phrase is uncertain". It means 'that which it deserves', and the phrase is clear. · Corrected.
- edrych (broadening) · minor · It cited "a phan edrych ef". The *ef* belongs to the next clause (*ef a welei*). · Corrected, with the Red Book's *edrychawd*.
- crogwn · minor · "mi a'y crogwn 'I would hang it'", but here *'y* is 'them' (note 5). · Corrected.
- allut · minor · It gave the softening "after the interrogative particle a". The *a* is the relative particle after the fronted question phrase. · Corrected.
- grogi · minor · "after y 'to'". *y grogi* is 'its hanging', with possessive *y* (notes 24, 40). · Corrected.
- torei · minor · 'would break … hinder me', with "sense uncertain". Note 28 gives the established idiom *torri* 'matter to, concern'. · Corrected.
- geccaf · minor · The head "deccaf (decaf)" was a mutated lemma with an invented modern form, and the entry called the cause of the softening "uncertain". · Now *teccaf* (*tecaf*), softened after the feminine singular noun.
- medreist, metrut · minor · 'succeed, be able, done well'. Pass 1 aligned *medru* on 'hit (a mark)' at 84 and 85. · Corrected.
- forch, fyrch · minor · The lemma was "fyrch", with "o for y" given for *forch*, and *fyrch* was glossed as singular 'the fork'. *fforch* is singular and *ffyrch* plural. · Corrected.
- anwymp, hydreul, kymoned · minor · The softening inside each compound was not named, and *hydreul* was given "modern form uncertain". · Now *gwymp* > *wymp*; *treul* > *dreul* (modern *hydraul*); *kyf-* + *b* > *kym-*. *kymoned* now has the sense of note 6, 'of equal birth'.
- diholedic · minor · "meaning uncertain … perhaps 'forlorn, hapless'". It means 'banished, outcast' (modern *deoledig*), as note 18 has it. · Corrected.
- diuwynyssit, goglyt, gyffuryf, alauoed, mynweir, mynweireu, waredaf · minor · Each had an invented lemma or modern form, or "uncertain" where GPC has the word:
  - *diuwyno* (*difwyno*);
  - *gogelyd* (*gochel*);
  - *kyffuryf* (*cyffurf*) 'form, manner';
  - *alaw* (*alaf*) 'herds', plural *alauoed*;
  - *mynweir* (*mynwair*) 'collar';
  - *gwaret* (*gwared*), the verbal noun of 64, for an invented "gwaredu".
  · Corrected.
- mynord · minor · "perhaps a fitting of the gate". Note 100 gives *mwn* + *ord* 'neck-hammer'. · Aligned, still marked uncertain, with the Red Book's *mynoad*.
- doethwyf · minor · "the ending -wyf is the 1 sg. of bot". This etymology is stated as fact, while note 52 says the analysis is not certain. · Aligned with the note.
- gymeint · minor · "whether this y is 'its' or the article is uncertain". Note 56 reads *y* 'its', and *kymeint* takes no article. · Corrected.
- diuayssant, bydyn · minor · *diuayssant* was "3 sg./pl.", and *bydyn* was "subjunctive/habitual". · Now 3 pl., and habitual imperfect.
- pedeirpunt · minor · Not noted that it is unsoftened in the position where *deir punt* is softened. · Added.
- rwtter · minor · "noun m." was asserted without grounds. · Gender now not stated; the likely English borrowing (note 44) is added.
- datrithwys, hudlath · minor · *datrithwys* had "da- + rhith" and "modern form uncertain"; *hudlath* did not name the compound softening of *llath*. · Now *dat-* + *rithaw* (*datrithaw*, *datrithio*), and *llath* > *lath*.
- teimlaw, kyuanhedu · style · The head was a modern form where the Middle Welsh form belongs (*teimlo*), or a modern spelling (*kyuanheddu*). · Corrected.

Checked and kept: *lygryssit* (*ry* written *yr*, as note 4); *grofdeu*; *sengi* 'tread, press in'; *kyuarwydyt* 'tale'; *herwa*; *aghynghor* (nasal after *an-*); *yghot*; *graessawu*; *mynwgyl* (no change after *y* 'her'); *gueir* and *kywein* (uncertain, with the Red Book's *geir*); *essynn*; and the remaining broadenings (*y*, *yr*, *yn*, *ar*, *wrth*, *uanec*, *wneuthur*, *dyrchauael*, *wyd*, *wy*, *uot*, *orssed*, *welsei*, *na*, *uu*, *ueichawc*, *benn*, *gwbyl*, *dala* and the rest).

### Refused
- dylyut · "imperfect subjunctive". For *dylyu* the imperfect serves as 'ought, should', so the label is acceptable. Kept.
- defnyd · "no mutation after bei gwypwn inheu". A softening *d* > *dd* would not show in this spelling. Kept.
- gardotta, gellwg, gellwng, ellynghaf · The lemma heads are *cardota* and *gollwng*, where Middle Welsh *kardotta* and *gellwng* would be stricter. The modern form follows in each case, and the work glossary has these heads already. Kept for consistency with known-forms.json.
- wyte · "te, a form of the pronoun ti (uncertain)". The hedge is harmless. Kept.
- ymdiala · "the final -a is uncertain". This is true: GPC's verbal noun is *ymddial*. Kept.
- known *ansyberwyt* ("anseberwydd") and *ym* · These come from earlier parts and are outside this part's new entries. *ym* already carries the *ym kyffes* sense. Not touched. Owner may wish to check *anseberwydd* against GPC.
