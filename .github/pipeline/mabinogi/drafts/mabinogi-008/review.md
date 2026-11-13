# mabinogi-008 — review

## Pass 1 (units)

Reviewer pass 1 (2026-11-13). I read all 83 units and the "about" against conventions.md, packet.md (the established text and the establishment log), the published mabinogi-001 to 007, and drafts/mabinogi-006/review.md and drafts/mabinogi-007/review.md. For names and formulas I searched the published parts directly: Gorssed Arberth, Llassar's epithet, Caswallawn, Kicua and her father, Dioer, Nac ef, eneit, Pa hyt bynnac, gelwir/gelwit, atuyd/aduyd and dewred. Aids: Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. Third witness: Rhŷs & Evans 1905 (Red Book), `source/raw/rhys-evans1905_djvu.txt`, the Manawydan opening (printed pp. 44–49), read with the OCR's usual misreadings of 6, ſ and r-rotunda. No English translation was consulted. For every unit I checked each grammatical label in the note against the form, Welsh → `l` word by word, `l` ↔ `i`, and the house renderings. Edits were made by a Python script (load, change fields by index, dump with ensure_ascii=False, indent=1). No `t` was touched. Afterwards a script confirmed that there are 83 sentences and that the `t` list equals cut.json's exactly.

**Unit numbers are 0-based.**

### Changes

- 29 · l, n · major · The note called *tyuu* "3 sg. preterite of tyuu (tyfu)", which is circular and wrong. *tyfu* is the verbal noun; its preterite is *tyfwys*/*tyfawd*. Here the verbal noun stands for the finite verb, with its subject straight after it, as in *Dyuot y crydyon*. The Red Book has the same. · l now reads "And in that, growing fellowship between-them …". The note now explains the verbal noun and its subject. i ("such fellowship grew") is unchanged.
- 50 · n · major · "*gelwir* … softened after the particle". *gelwir* is the radical form: *galw* with a > e before the ending. The preverbal particle *y* causes no mutation. 004, 006 and 007 gloss the form correctly. · The note now gives a > e, says g is the radical, and says the particle does not mutate.
- 76 · n · major · The same error for *gelwit*, "softened". · Corrected the same way. I also added the Red Book reading *yn drydyd* (masculine, softened) to the existing remark on the odd feminine *tryded*.
- 51 · n · major · Two errors. (a) "*ny frynit* has the soft mutation (f = v)". The soft mutation of *p* is *b*, so *frynit* can only be the spirant *ph* written *f*, as *Freinc*, *ford* and *Henford* are written in this part. (b) The note put the raised *r* in this unit's *ny phrynit*. The establishment log places it at col 66 l. 33, **na** *phrynit*, which is the shield sentence (unit 62). This unit lies before col 66 ll. 7–8 (*hyny*, unit 52). · (a) The note now says *frynit* is the same spirant, *ph* written *f*, and that the Red Book writes *phrynit* both times. (b) The raised-*r* remark was removed here and added to unit 62.
- 62 · n · minor · The establishment-log item "raised *r* in *phrynit*" was missing from its own unit (see 51). · Added: the manuscript writes the *r* above the line, over the *h*, and it is brought into the line.
- 6 · n · minor · "the subject stands first and the particle y (yr before a vowel) links it to the verb". After a fronted subject or patient the rule is *a*, not *y*. The Red Book reads *ry edewit*, with the perfective *ry*. · The note now gives the Red Book reading and says the White Book's *yr* is probably that same particle. It also explains why *y* would be unexpected here.
- 7 · n · minor · "*well* … softened, as it regularly is after nyt oes". The softening belongs to the comparative after its noun (compare *heldir well*, where *tir* is masculine), not to *nyt oes*. · Rephrased.
- 8 · i · minor · i "if ever you had wanted a realm, perhaps you would have had that one" turned the imperfect subjunctives into a past counterfactual, and l ("if you-wanted … you-would-get") disagreed with it. · i now reads "And if ever you wanted a realm, perhaps you would get that one." The note already says *aduyd* and the point of the sentence are uncertain, and *[waeth]* is not supplied. That stands.
- 13 · l, n · minor · (a) *Er amser* was glossed only as 'since the time'. In this part the White Book writes the article as *e*: *E gedymdeithas*, *E rof*. The Red Book seems to read *Yr amser*. i ("In the days when …") already took it that way, so l and i disagreed. (b) *dewred* was called "rare". It is Pwyll's *dewred* 'valour' in part 001. · l now reads "The time that she-was in her prime". The note gives the article reading first and *er* 'since' as the less likely one. *dewred* is now glossed 'valour, vigour' with the cross-reference, and 'her prime' is kept as uncertain.
- 15 · l · minor · The formula was not repeated as published. 007 has *Pa hyt bynnac y bydynt ar y ford* → l "However long they-would-be on the road". This draft had "whatever length they-were on the way". · l now reads "And however long they-would-be on the road". The note already calls it the formula.
- 25 · l · minor · l "while-he-may-be nearer" disagreed with the note ("that he be nearer") and with *a* (relative/conjunction, not 'while'). · l now reads "that may-be nearer".
- 46 · n · minor · The rare *dygyaw* was discussed without the third witness. The Red Book reads *diffygyaw a wnaethant* 'they failed, grew weary', the *diffygyaw* of part 001. · Added. The sense is still uncertain.
- 47 · l · minor · *Dioer* is l "Assuredly" in every published part (001, 004, 005); this draft had l "Indeed". · l now reads "Assuredly". i "Indeed" matches the published i.
- 49 · i, n · minor · i added "the blue enamel", which is not in the Welsh, while the note said English keeps the Welsh name because "the next sentence explains it". The next sentence explains only where the name comes from. The note also did not say that 006 already writes the epithet differently (*Llaesgygwyd*). · "the blue enamel" is gone from i. The note now says the name is kept unglossed, that the next sentence gives only its origin, and that 005 writes *Llaes Gyfnewit* and 006 *Llaesgygwyd*. The i name stays Llasar Llaes Gyfnewid, as in 005.
- 63 · n · minor · The Red Book has a different verb here, *dygwydawd*. · Added to the note on *dygywys*.
- 71 · n · minor · *galhon* was marked uncertain, with no mention that the Red Book reads *o gallon*, which supports *calon*. · The Red Book reading is added, and the unexplained *h* is noted.
- 75 · i · minor · *A dechreu a wnaeth ymgedymdeithassu …* lost "began" in i ("he made friends with"). The house practice keeps *dechreu a wnaeth* as "began". · i now reads "And he began to keep company with the best goldsmith …".
- about · minor · "the craftsmen of the place plot to kill them" is wrong for the shield town. There it is *y'w kytdrefwyr*, their fellow-townsmen. · The about now reads "the men of the place, craftsmen or townsfolk, plot to kill them".
- 0 · n · style · "g lost in the compound" did not name the mutation. · Now "gwyr softened in the compound, so its g is lost".
- 1 · i · style · "without a place to go" adds "to go"; *heb le idaw* means 'without a place for him'. · i now reads "there is no one without a place of his own tonight but me."
- 3 · n · style · "kyt (kyn before a vowel) with boet" was misleading, since *boet* does not begin with a vowel. · Now "kyt, a form of kyn 'though' (the form used before a vowel, and fixed in kyt boet)".
- 32 · n · style · "orugant is the 3 pl. of oruc, the preterite of gwneuthur" left out the softening and blurred what *goruc* is. · Now "orugant ← gorugant, softened after a: the 3 pl. of the defective preterite goruc, which serves as a past of gwneuthur".
- 35 · i · style · "there came a great noise": "great" is not in *llyma dwrwf*. The size comes in the next clause (*can ueint y twrwf*). · "great" removed.
- 44 · n · style · Added that the Red Book has *ar gic*, which supports the remark that the White Book does not write the mutation.
- 55, 67, 71, 82 · l · style · *Nac ef* is l "Not so" in 004 (i "No"). · l now reads "Not so" in all four units. i keeps "No".
- 61 · n · style · Added that the Red Book has *da a welsynt*, beside Evans's and the witness's reading without *a*.
- 64 · i · style · "Word of it came to them": *rybud* is "warning" in unit 53 (i "they had warning"). · i now reads "Warning came to them".
- 66 · n · style · Added that the Red Book supplies the object *wynt* after *lladwn*.
- 74 · i · style · "the finest cordovan to be had" lost *a gauas* 'that he got'. · i now reads "the finest cordovan he could find in the town".
- 79 · i · style · "came together": *Dyuot* is only 'coming'. · i now reads "The shoemakers came and took counsel".
- 82 · i · style · "go and see how it fares" adds to *awn y hedrych*. · i now reads "and go to see it."

Totals by entry: 4 major (29, 50, 76, 51), 14 minor (62, 6, 7, 8, 13, 15, 25, 46, 47, 49, 63, 71, 75 and about), and 13 style (0, 1, 3, 32, 35, 44, the four *Nac ef* units counted once, 61, 64, 66, 74, 79, 82).

### Establishment-log items: all now stated
*uydef* slip (21); *aduyd*, with *[waeth]* not supplied and its sense uncertain (8); *heb uil yndi* against *yndunt* (37); *onyt wyll pedwar* (38); *yn anniuer* = *an niuer* (39); *Ymedgell* left undivided (42); *Manauydan* with *u* (0); *eiryoed* with *d* (17); *deef* → *dref* (68); raised *r* in *phrynit* (now at 62, where the log puts it); *hyny* with its suspension (52); *inheu* with no expressed object (66, 81); the opening initial G (0); *da welsynt* with no *a* (61); *caffom* with *ff* (47); *Ryt Ychen* as two words (30); *bellach* (82).

### Names and formulas against 001–007: verified
Gorssed Arberth → the Mound of Arberth (002). Caswallawn → Caswallon son of Beli (007). Kicua → Cigfa. Her father Gwyn Gohoyw in 004 is "Gwyn Gloyw" here, and the note says so (the Red Book also has *gloyw*). Llassar: i follows 005's Llasar Llaes Gyfnewid, and the note now also cites 006. Lloegyr/Lloygyr → England (first occurrence; the note gives Lloegr). Ynys y Kedyrn → the Island of the Mighty. Oy a Duw → Oh God; *guae ui* → woe is me (007). *eneit* → friend (004). Ie, unben, kyuoeth, kedymdeithas, *Duw a dalo it*, *heb ef*/*heb ynteu*, digriuwch, anryded and *E rof i a Duw* all follow the house table. Sef is dropped in i at 78 and 79.

### Refused
- 2 · i "the third Yielding Chieftain". I considered "Ungrasping" or "Unassuming", but either would be a choice among disputed senses too, and the first risks echoing a remembered rendering. The note already says *lledyf* is disputed and that "Yielding" is a choice. Kept.
- 3 · i "it grieves me sorely" for *goathrist*. *go-* usually lessens, but the note states the doubt openly and says i takes it as strong. Kept.
- 19 · *Pa dywedwydat*. The Red Book has the same form (*Padywed6ydat*). The note's caution is right, and I found no better analysis. Kept.
- 35 · *na chanhoed* "imperfect of kanuot". I checked this, because *-oed* looks pluperfect. Compounds of *bot* (*gwybot*, *adnabot*, *canuot*) have an imperfect in *-oed*, so the label is right. Kept.
- 37 · *y guelyn* as the imperfect without final *t*. The Red Book has *y g6elynt*, which supports the reading. Kept.
- 44 · i "the honey of wild swarms" adds "honey" to *bydaueu*. That is what the swarms were taken for, and the l shows the bare word. It is a reasonable inference, so I kept it, though it is a light addition.
- 58 · "the object after the imperative is here left unsoftened" (*taryaneu*). The Red Book also has *taryaneu*, and *gwnawn grydyaeth* (71) shows the softening the note implies is normal. Kept.
- 63 · *y gueith wynteu*, "y here stands for 'their'". The Red Book has *eu gweith*. The note's analysis is right, so I made no change beyond the *dygywys* addition.
- 30 · i "Oxford" for *Ryt Ychen*. The note gives the Welsh name and its meaning, and l keeps *Ryt Ychen*. Kept.
- 34 · *ac yniuer gyt ac wynt*, i "their company". The Red Book has *ac eu niuer*. i is defensible either way. Kept, with no note added.
- 43 · i "to eat their way through the feast" for *treulaw y wled*. This is a fair rendering of 'consume' and fits 27 and 24. Kept.
