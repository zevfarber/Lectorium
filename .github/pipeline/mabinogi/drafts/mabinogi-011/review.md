# mabinogi-011 — review

## Pass 1 (units)

Reviewer pass 1 (2026-11-14). I read all 116 units against conventions.md, packet.md (the established text and the establishment log, including the "For the drafter" summary), the published mabinogi-001, 009 and 010 (and 002–008 for recurring formulas: *eneit*, *kyffes*, *hut*, *lledrith*, *Duw a ro*, *En/Yn llawen*, *teulu*, *Dioer*, *Ie*), and drafts/mabinogi-010/review.md. Third witness: Rhŷs & Evans 1905 (Red Book), `source/raw/rhys-evans1905_djvu.txt`, printed pp. 59–64, read through the OCR's usual misreadings of 6, ſ and r-rotunda. Aids: Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. No English translation was consulted. For every unit I checked each grammatical label in the note against the form, Welsh → `l` word by word, `l` ↔ `i`, the house renderings, and that every establishment-log item stands in the note of its unit. Edits were made by a Python script (load, change fields by index with an exact-match assertion, dump with ensure_ascii=False, indent=1). No `t` was touched. Afterwards a script confirmed that there are 116 sentences and that the `t` list equals cut.json's (and the pre-review file's) exactly.

**Unit numbers are 0-based.**

### Changes

- 6 · l, i, n · major · The English gave the second brother as "Eueydd", a modern-looking form built on the Red Book's *eueyd*. The text is the White Book's *Euyd* (an establishment-log item: Euyd, not Gwydion), and names in English take the modern Welsh form. · l and i now read "Eufydd son of Dôn"; the note gives Eufydd as the modern spelling of *Euyd* (u = /v/, d = /ð/) and says the Red Book spells it *eueyd*.
- 6 · l, n · minor · *a'r teulu* had l "the warband"; the house `l` is "household-troop" (as 001, 003, 010). · l now "the household-troop"; the note states the house pair (l 'household-troop', i 'warband'). i keeps "warband".
- 2 · i · minor · "could not live unless his two feet lay in the lap of a maiden, save only when the tumult of war prevented him" reads like a remembered stock phrasing. · Rebuilt from the Welsh: "could not stay alive except while his two feet rested in a maiden's lap, unless the uproar of war hindered it."
- 15, 20 · i · minor · *eneit* in address had i "my soul". The published parts (003, 004, 006, 008, 009) give l "soul", i "friend". · i now "friend" in both.
- 33 · n · minor · "ba 'what' softens ffuruf". ff is not subject to mutation; *furuf* is *ffuruf* written with one f, as *frwytha* (14). The Red Book has *ba ffuryf*. · Corrected, with the Red Book.
- 38 · n · minor · "ragot ← racot … softened after the verb". The g of *ragot* is the final c of *rac* written g before the personal ending (as in all the conjugated forms), not a mutation, and the r/rh distinction is not written. · Corrected.
- 39 · n · minor · "deguyr: deg + gwyr, softened in the compound". *deg* does not soften; *deguyr* is *deg* + *guyr* with the two g's written as one (Red Book *degwyr*). · Corrected.
- 45 · n · minor · *Ynteu Wydyon*: the softening was stated with no cause. · Now: softened in apposition after the pronoun *ynteu* (Red Book also *Ynteu wydyon*), with the contrast of unsoftened *ynteu Giluaethwy* in col. 82.
- 46 · n · minor · *gan paub* (and *gan Pryderi*) stands unsoftened after *gan*, which softens; the note was silent. · Added, with the Red Book's *gan bawp*.
- 47 · n · minor · (Drafter's flag.) *mi uu hun* "apparently for uy hun" was argued without the Red Book, which has *no miui uy hun*. · Note now calls *uu* apparently a slip for *uy* and cites the Red Book.
- 49 · n · minor · "lawn ← llawn, softened before the adjective it strengthens". A following word does not cause a mutation. The Red Book has *llawn da* unsoftened; *tauawt* is usually masculine. · Note now says the White Book writes one l, and that whether this is a softening or only a spelling is not clear.
- 64 · l · minor · *am y geir* had l "from the word"; the note glosses 'about the word'. · l now "about the word". i "your release from the word" kept as English.
- 78 · i, n · minor · i "the strongholds of Gwynedd" for singular *kedernit* (95 has "fastness"); the unsoftened object *kedernit* after *a gyrchwn* was not noted. · i now "the fastness of Gwynedd"; the note adds the unsoftened object and the Red Book's agreeing *kedernit*.
- 86 · n · minor · "gwysc 'track' after eu, written hwysc with h" implies that *eu* turns g into h. · Now: the word is (g)wysc without its g, which takes h after *eu* as a vowel-initial word does; the Red Book also has *yn eu hwysc*.
- 100 · l, i · minor · The note says the English uses the modern Dolbenmaen, but l and i had "Dôl Benmaen". · l and i now "Dolbenmaen", as the note says.
- 101 · l · minor · (Drafter's flag.) *clymu* had l "drawing-together", while the note glosses 'binding' and says the sense is uncertain. `l` follows the word. · l now "binding". The note's hedge and i "came to terms" kept.
- 104 · n · minor · (Drafter's flag.) *y deulu*: the two readings are given correctly, but the Red Book evidence that decides for 'two hosts' was missing: where the White Book has *y deu lu* in 108, the Red Book writes *y deulu*. · Added.
- 107 · n · minor · "uynet ← mynet, softened as the verbal noun after ar neb". *neb* does not cause softening; *uynet* is the object of *chymellaf* with words between. · Corrected. (*dros* + soft mutation, and the hedge on its sense, checked and kept: see Refused.)
- 109 · l, i · minor · *Dygaf y Duw uyg kyffes* had l "I-take to God my confession", i "I take God to witness". 007 has the same oath, *Y Duw y dygaf uyg kyffes*, as l "To God I-bear my confession", i "To God I make my confession". · l now "I-bear to God my confession"; i "I make my confession to God that …".
- 114 · n · minor · (Drafter's flag.) *y Maen Tyuyawc*: "y stands for yn 'at' (or y 'to'), with nothing written for the mutation". The nasal mutation leaves M unchanged, so nothing could be written; *y* 'to' would soften *Maen*. · Now: *y* most likely for *ym* (yn assimilated before M), the m not written; *y* 'to' is unlikely because *Maen* is unsoftened. Added the Red Book's *ymaen tyuyawc*.
- 114 · i, n · minor · *hut a lledrith* had i "magic and enchantment", which turns *lledrith* 'illusion' into 'enchantment' (010: *yr hut a'r lledrith* "the enchantment and the illusion"; l here already "magic and illusion"). The note glossed *o nerth grym ac angerd* as a list while l has "strength of-might". · i now "by magic and illusion"; the note gives "strength of might and fury (or strength, might and fury)".
- 7 · i · style · "set his heart on her … what to do for her". The Welsh says *y uryt* 'his mind' and *ymdanei* 'about her'. · Now "set his mind on the maiden, and loved her so that he did not know what to do about her."
- 11 · i · style · "“Why?” said he." The house `i` for *heb ynteu* is "he said". · Changed.
- 40, 85 · n · style · *uuant*, *uu* "softened" with no cause given. · Both now say: softened after the fronted predicate, as after the unwritten particle *a*.
- 52 · n · style · *ditheu* "softened" with no cause. · Now the auxiliary pronoun after *dy* + verbal noun, as *di* in *dy uedwl di*.
- 60 · n · style · *uot* "softened after its subject" was unclear about whose subject. · Now: softened as the object of *dylyei*, standing after its subject *hayarn*.
- 90 · n · style · (Drafter's flag.) *a Chiluathwy*: the analysis is right; the Red Book has the same *a chiluaethwy*. · Added.
- 108 · i · style · "to set his own body against his" put the "own" on the wrongdoer; *y eidaw ynteu* is Pryderi's own. · Now "to set his body against Pryderi's own".

Checked and in place: every establishment-log item has its note:
- the large initial M (0); the raised *y* of *deryw* (10); the "!" (33) and "\" (36) marks; the dot after *arglwyd* (25);
- *Euyd*, the stray *o*, *o nyeint* with the Red Book's *y nyeint* and the uncertainty, and [a aei] not supplied (6);
- *ac nacaha ui* without the negative, the Red Book's *ac na naccaa ui*, nothing supplied (53);
- *yg Heredigyawn* (39), *ygwarthaf* (73), *yghymherued* (96); *kynllyuan* and the dropped [e] (59);
- *yguelei Uath* (91, Red Book *ygwelei uath* confirmed); *Phyderi* (97); *diueuessur* (99, Red Book *diuessur* confirmed);
- Goewin/Goewyn (3, 91); Kaer Tathyl/Dathyl (81); Kyredigyawn/Keredigyawn (1, 73); Giluathwy/Giluaethwy (7); Guydyon/Gwydyon/Wydyon (9, 45, 78, 90);
- *e ymlad* (107), *e Wydyon* (69), *E rof a Duw* (106), *E gwyr hynny* (113); *pedwyryd* (102); *Dol Penmaen* as two words in Evans (100);
- *Hobeu* and the aside (25, 32); the two asides in brackets (32, 67); [heb y Guydyon] not supplied (109); *harueu* (115).

The following follow the house table: *Ie* "Yes" throughout (17, 33, 42, 51, 57, 68, 106, 112); *heb ef/heb ynteu*; *y rof a Duw* (106); *Dioer* (108); *Duw a ro da it* (63, as 010); *En llawen* "Gladly" (38); *Sef*; *a wnaeth/a wnaethant* folded in `i`; *gwyrda* "noblemen" (102); *cantref*; *llys* "court"; "Lord" in address.

### Refused
- 16 · *o ry kyuarfo* (drafter's flag). *ry* is the perfective particle with the present subjunctive, 'if it has met'; *ry* does soften, and the note says the k is written plain. The Red Book's line is garbled in the OCR (*o: ykyfarfío*), so nothing can be cited. Kept.
- 16, 2, 21 · *a'y guybyd*, *a'y llesteirei*, *a'y paraf* "no mutation after the infixed 'y". Right for the 3 sg. masc. infixed pronoun. Kept.
- 6 · *o nyeint* (drafter's flag). The note says the sense of *o* is uncertain, as the log asks, and gives the Red Book's *y nyeint*. Kept.
- 104 · *y deulu* (drafter's flag). The reading 'the two hosts' is the better one and is now supported by the Red Book (above); the 'his warband' alternative stays in the note as a possibility. l "the two-hosts" kept.
- 107 · *dros* (drafter's flag). *dros* softens *gwneuthur* > *wneuthur*; 'instead of' is its ordinary sense with a verbal noun; the note marks the sense here as not certain. The Red Book has the same *dros wneuthur ohonam*. i "in our place, when we ourselves might be doing our utmost" follows the 'instead of' reading and is kept.
- 101 · *clymu* (drafter's flag). The Red Book has the same *clymu a wnaethant*. The note's 'binding … probably came to terms, uncertain' is as far as the evidence goes. Only l changed (above).
- 90 · *a Chiluathwy* (drafter's flag). The spirant *ch* is correctly explained "as though the name began Kil-", and the Red Book agrees. Kept, with the Red Book added.
- 47 · *mi uu hun* (drafter's flag). The Red Book supports the slip reading; *uu* is not glossed as a separate form. Kept, with the Red Book added.
- 0 · "before oed the particle a is not written". Acceptable for the abnormal sentence with *oed*; consistent with how the published parts treat it. Kept.
- 96 · *arhoed* "impersonal preterite". The ending *-et/-ed* is the impersonal preterite, as *dodet*, *gossodet*, *anuonet* in this part; the Red Book has *arhoet*. Kept.
- 48 · i "No," for *Na well*. A natural English answer; `l` keeps "No better". Kept.
- 40 · i "They were made welcome." Fair for *Llawen uuant wrthunt*; `l` gives the bare words. Kept.
- 97 · i "on both sides" for *o pop parth* 'from every side'. There are two sides to this battle. Kept.
- 113 · i "The two men" for *E gwyr hynny* 'those men'. The men are the two champions. Kept.
- 72 · *o'r pryt pwy gilyd* "a day and a night". The note's gloss is sound and i says "from one hour to the same hour next day". Kept.
- 91 · i "they laid … drove … and he lay with her". The verbal nouns have no expressed subject; the English supplies the one the story requires. Kept.

Pass 1: 1 major / 20 minor / 7 style
