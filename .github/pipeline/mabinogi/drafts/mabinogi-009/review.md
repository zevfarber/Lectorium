# mabinogi-009 — review

## Pass 1 (units)

Reviewer pass 1 (2026-11-13). I read all 93 units against conventions.md, packet.md (the established text and the establishment log, including the "For the drafter" summary), the published mabinogi-001 to 008 and drafts/mabinogi-008/review.md. For formulas and names I searched the published parts directly: Dioer, Och, Nac ef, Pa hyt bynnac, eneit, Mae, Oy a (Arglwyd) Duw, Duw a dalo, Y rof (i) a Duw, Meuyl, Ie, llyma/nachaf, Arglwyd in address, uorwyn, Kicua and her father, and the published notes on the infixed pronoun ('y/'e with keffy, kymmeraf, kygleu). Aids: Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. Third witness: Rhŷs & Evans 1905 (Red Book), `source/raw/rhys-evans1905_djvu.txt`, the Manawydan text at printed pp. 49–54, read with the OCR's usual misreadings of 6, ſ and r-rotunda. No English translation was consulted. For every unit I checked each grammatical label in the note against the form, Welsh → `l` word by word, `l` ↔ `i`, the house renderings, and that every establishment-log item stands in the note of its unit. Edits were made by a Python script (load, change fields by index, dump with ensure_ascii=False, indent=1). No `t` was touched. Afterwards a script confirmed that there are 93 sentences and that the `t` list equals cut.json's exactly.

**Unit numbers are 0-based.**

### Changes

- 22 · n · major · "un geir ← geir 'word', softened after un". *geir* is the radical (the Middle Welsh spelling of *gair*), and *un* softens only a feminine noun; *geir* is masculine. · The note now says *geir* is radical and that *un* does not mutate it.
- 40 · n · major · "'y is the infixed object 'it', which normally softens; cadwn is written unsoftened". The infixed 3 sg. masculine pronoun causes no mutation. The published parts gloss *ti a'y keffy* (003), *a'e kymmeraf* (003) and *a'e kigleu* (004) as radical forms, and this part's own *A mi a'e gwnn* (76) is radical too. The Red Book has *mi ae cadwn*. · The note now says *cadwn* is regular and gives the parallels.
- 64 · n · major · "kroft softened after teir". *teir* does not soften the noun after it. *grofd* after *deir* (the Red Book also has *deir grofft*), together with *o'e rofdeu* in 66 (Red Book *oerofteu*), suggests the scribes took *grofd* as the word's own form. · The note now says so. It still says that *teir* itself is softened after *'e* 'his'.
- 9 · l, n · major · *yrdhunt* was explained as "perhaps a form of rac (racdunt)". This part writes *racdunt* for *rac* (89). *yrdhunt* is *er* 'for, on account of' conjugated, 3 pl. (*erdunt*). The Red Book has *yrdunt*. l "without retreating from-them" followed the wrong analysis. · l now reads "without retreating for-them". The note gives *er*, 3 pl., with the Red Book form and the contrast with *racdunt*. i ("without giving ground before them") is a fair rendering of the sense, so it is unchanged.
- 15, 16, 29, 39, 73 · l · minor · *Dioer* had l "Surely". The published parts (001, 004, 005, 008) all have l "Assuredly". · Changed to "Assuredly" in all five.
- 15, 16 · i · minor · *Dioer* had i "Surely". The published parts and this draft's own 29, 39 and 73 have i "Indeed". · Changed to "Indeed". The note at 15 now gives 'assuredly, indeed' and the house pair.
- 33 · l, i, n · minor · *Och* had l "Oh" and i "Ah". 003 and 006 have l "Och" and i "Oh". i also had "my lord" in lower case, while the published parts write "Lord" in address. · l now reads "Och, my Lord", i "Oh, my Lord". The note points to 003 and 006.
- 57 · l, n · minor · *Nac ef* had l "Not it". 008 has l "Not so" every time (67, 71, 82). · Both l and the note now read "Not so".
- 13 · l, n · minor · The formula *Pa hyt bynnac y bydynt* had l "However-long they-were". 007 and 008 have "However long they-would-be", and the note itself calls *bydynt* habitual. · l now reads "However long they-would-be thus". The note gives the formula's l.
- 3 · n · minor · The note said *'e* 'their' sits inside *o ulaen*, as if it kept the softening. *'e* 'their' leaves a consonant unmutated, so the Red Book's *oeblaen* is the regular form. The White Book's *w* is the irregular one. The log item (the 6-shaped *w*, certain) was already there. · The note now explains this. The log item is unchanged.
- 39 · l, i, n · minor · *y uach*: the Red Book's *yn vach* shows that *y* stands for predicative *yn* 'as', so l "to surety" was wrong. i "as my surety" added "my". · l now reads "as surety", and i "I give you God as surety:". The note explains *y* = *yn*.
- 71 · l · minor · *wedy daruot torri*: l "after breaking" left out *daruot*. · l now reads "after finishing breaking". The note already explains the construction.
- 64 · n · minor · "nachaf … like it [llyma] softens what follows". This is false, as *nachaf twryf* in 85 shows. · Corrected.
- 85 · n · minor · "here twryf stands unsoftened after nachaf" implied that *nachaf* normally softens. · The note now says *nachaf* does not soften, and contrasts it with *llyma dwryf* (36).
- 64 · n · minor · "yn un dwf: twf softened after un". *twf* is masculine, so the plain rule for *un* does not apply. The softening comes from *un* 'the same' in close compound (compare *unfryd*). · Rephrased.
- 78 · n · minor · "degach … softened after the noun". This is not the regular rule after masculine *gwenith*, and the White Book has *wenith tegach* unsoftened in 64. The Red Book has *degach* in both places. · The note now states the variation.
- 29 · n · minor · *uuosti* was called "softened" with no cause. · The note now says it is softened as after the relative *a*, which is unwritten here but written in the parallel *a golleisti*.
- 37 · n · minor · The note did not mention that *Gwyn* stands unsoftened after *uerch*. 008 has *uerch Wyn*, and the Red Book here also has *verch gwyn*. · Added.
- 54 · n · minor · Establishment-log item missing: in *dreulwys* the final *s* is raised over the *y* and brought into the line. · Added.
- 0 · l · style · "However-long" was hyphenated, unlike 007 and 008. · Now "However long".
- 3 · i · style · "ran on ahead": *kerdet* is 'walk, go'. · Now "went on ahead of them".
- 4 · n · style · *keginwrych*: only *gwrych* was explained, and nothing was said about how certain the first element is. · The note now says the first element is not clear.
- 38 · i · style · "Manawydan watched her" for *edrych ar hynny* 'looking at that'. · Now "Manawydan looked on at this."
- 43 · i · style · "the young woman" for *y uorwyn*. l has "maiden", and so do the published parts (002, 003). · Now "the maiden".
- 45 · i · style · "Gladly, lord". The published parts capitalise "Lord" in address. · Now "Gladly, Lord".

Checked and in place: every establishment-log item has its note. These are *o'e wlaen* (3), *uyg hynghor* and the elliptic *honn yma eiryoet* with the Red Book's *nys gweleist* (15), no *eur* with *cawg* and the gap after *chadwyneu* (20, 21), *y lywenyd* against *lyueryd* (22), the raised *a* and the expunged *n* (42), *kymry* and *ehouyndre* (43), the cancelled *ni allwn* (44), *gvaegeu* (52), *blwyn* (54), *yn y doi yn y dywyssen* (71), *groft*/*grofd* (63, 84), *ni chytdremei* (91), *Gloew* (37), *yrdhunt* (9) and *yr gaer* (11). The following follow the house table: *heb ynteu*/*heb hitheu*, *Y rof a Duw*, *Duw a dalo it*, *Meuyl y mi*, *Ie*, *eneit* 'soul'/'friend', *Oy a Arglwyd Duw* and *gedymdeithas* 'fellowship'.

### Refused
- 10 · *torri kyuarth*, i "stand at bay once more". I considered 'break off the bay', that is, break away. *eilweith* goes with *kilyei*, and a renewed stand fits the cycle in 9. The note already says the phrase is uncertain. Kept.
- 10 · *ynghei*. The verb's base is not certain, and the note says its meaning comes from the context. Kept.
- 40 · *bei et uwni*. The Red Book reads *pei yt uewn i*. The note's analysis (*bei* 'if', particle *et*, *bwn* 1 sg. imperfect subjunctive, softened) is sound, so I added nothing.
- 49 · *y glanet y wr kygynhilet*. The construction is compressed, the note says so, and the Red Book agrees (*y glanet y wr kygynnilet*). Kept.
- 69 · *tra y gefyn*. The Red Book has *drae geuyn* (*dra'e geuyn*). The note's 'beyond his back' = 'back again' is right. Kept.
- 86 · *eliwlu*. The Red Book has the same word, and the note already marks its meaning as uncertain. Kept.
- 87 · *drigyaw* "dringaw written without n". The Red Book also has *dzigyaw*. The gloss is plausible and the sense is secure from the context. Kept.
- 42 · i "that is what I would have looked for from you" adds "from you". This is a light gloss on *tebygwn* 'I would expect', and l shows the bare words. Kept.
- 54 · l "a-year thus he-spent there" leaves out "it-was-that" for the abnormal *a*. The note marks the object put first, and 0 and 58 show the pattern in full. Kept, so as not to over-hyphenate.
- 89 · i "with the ears in their keeping" for *a'r tywys gantunt*. This is a fair rendering of *gan* 'with, in the possession of'. Kept.
- 7 · "llyma … softens what follows" — confirmed in this part by *llyma uaed* and *llyma dwryf* (36), against unsoftened *nachaf twryf* (85). Kept.
