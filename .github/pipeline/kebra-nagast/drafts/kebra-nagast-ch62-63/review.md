# Review, pass 1: kebra-nagast-ch62-63 (ch. 62-63)

Reviewer: pass 1, units.json only (gloss.json untouched, `t` untouched; verified identical before and after). Changes: 47 (major 1, moderate 22, minor 24).

## Flags resolved

- **አልዋሕ vs known lemma ሊሕ.** አልዋሕ is the regular broken plural of ሉሕ (ʾalwāḥ, cf. Arabic alwāḥ; Dillmann ሉሕ 'tabula, board'). Lemma ሉሕ; ሊሕ is not the base. The drafter's 'tablets' was stronger than the evidence: a replica is being built and the book of the law laid inside it, and the published house gloss is 'boards, planks'. Units 8 l/i/n changed to 'boards (?)', 'tablets' kept as a possibility in n. For pass 2: gloss.json `__broaden__` entry for አልዋሕ should lead with ሉሕ 'boards, tablets' and not describe ሊሕ as a 'variant'; the old ሊሕ entry should be replaced, not kept as the lemma.
- **ትሠውዕ 3fs vs known 2ms.** The form is identical for 2ms and 3fs; here the subject is the Pharaoh's daughter (ትሠውዕ ወትሰግድ ሎሙ after እንዘ ይሬእያ), so 3fs is correct. gloss.json already broadens the known entry accordingly; no change to l/i. Unit 22 n reworded (it spoke of 'the known glossary entry').
- **ሶፎር = Ophir.** Confirmed: Greek Sophir/Sophera of the LXX for Ophir (1 Kings 9:28 etc.), in a list of costly materials with gold; 'ingots (?) of Ophir' stands. Proper name: conventional English in i, as in l, matching the pilot (l uses English names). No change.
- **ሰርዴዮን = sardius.** Confirmed: Greek sardion (σάρδιον), the stone of Exodus 28:17 and Revelation 21:20; 'sardius' matches the published ch. 17-20 gloss (ሰርድዮን) and ch. 60b ('stone of sardius'). Spelling differs (ሰርዴዮን / ሰርድዮን); not changed, as it is Bezold's. No change.

## Changes (unit · field · severity · what was wrong · what was done)

Units are numbered from 0 in units.json order (0 = ch. 62 heading, 14 = ch. 63 heading).

- **about · about · moderate** · Same remembered 'too hard' (see unit 1). Done: `nothing is too hard for God` -> `nothing is impossible for God`

- **1 · i · moderate** · 'too hard for God' is the stock English of Genesis 18:14 / Jeremiah 32:17 (KJV/RSV), arriving ready-made; the Geʿez is ምንት እምተስእኖ, l 'what from-impossibility'. Rebuilt from the grammar. Done: `what is too hard for God` -> `what is impossible for God`

- **1 · n · moderate** · Note justified the remembered phrase 'too hard'; now matches i. Done: `I read the idiom as 'what is too hard for God', resembling Genesis 18:14 / Jeremiah 32:17 in force (?)` -> `I read the idiom as 'what is impossible for God', close in force to Genesis 18:14 / Jeremiah 32:17 (?)`

- **3 · n · minor** · ተጋነየ is the long-vowel tä-stem (täqatälä-type, ተጋነየ), not the Gt (täqättälä/täqatälä); label corrected to the plain 'tä-stem' used in the work's glossary. Done: `(Gt of ገነየ` -> `(tä-stem of ገነየ`

- **4 · n · minor** · Count wrong: five perfect verbs (ወሖሩ ወቦኡ ወሰአሉ ወተጋነዩ ወበፅዑ), not six. Done: `Six perfect verbs in a row` -> `Five perfect verbs in a row`

- **4 · n · minor** · Subject here, not accusative: the -ተ of ሊቃውንተ is the construct state before እስራኤል. Done: `ሊቃውንተ is the accusative-construct form of ሊቃውንት, plural of ሊቅ` -> `ሊቃውንተ is the construct form (subject here) of ሊቃውንት, plural of ሊቅ`

- **4 · i · minor** · በፅዑ is flagged uncertain in l and n but i stated it flatly; (?) added for consistency with the other uncertain words in i. Done: `and made their entreaty to God` -> `and made their entreaty (?) to God`

- **5 · n · minor** · Process reference ('conventions') in a reader-facing note. Done: `which is the book's central theology (conventions)` -> `which is the book's central theology`

- **6 · n · minor** · Note pointed to 'the glossary' (a build-side file the reader never sees) for a verb not in this part; replaced by the actual grammatical point and the uncertainty. Done: `(3ms perfect, passive of ነሠተ 'take away', as in the glossary (?))` -> `(3ms perfect, tä-stem, passive of ነሠተ 'take away'; it may rather be a short spelling of ተነሥአ 'rose up, departed', the verb used of Zion in ch. 63, so the sense is uncertain (?))`

- **7 · i · minor** · i supplied 'this' as an object, but n (and the form እምዝ ዳግመ, 'from this time again') takes no spoken object; i now follows n and the glossary entry. Done: `Do not reveal this again to the foreign peoples.` -> `Do not, from now on, reveal it again to the foreign peoples.`

- **8 · l · moderate** · አልዋሕ rendered 'tablets' against the published house gloss 'boards, planks'; the context (a replica being built, the book of the law to be laid inside, 'overlay with gold') points to boards of a chest; 'tablets' is possible but not secure. Done: `And-these-too tablets which` -> `And-these-too boards(?) which`

- **8 · i · moderate** · Same: 'tablets' (suggesting the tables of the law) was unflagged and stronger than the evidence. Done: `And these tablets here, which are fixed (?)` -> `And these boards (?) here, which are fixed (?)`

- **8 · n · moderate** · Resolves the flagged አልዋሕ vs ሊሕ: አልዋሕ is the regular broken plural of ሉሕ (ʾalwāḥ, as in Arabic), so the lemma is ሉሕ and ሊሕ is not the base; also removes process talk ('the glossary form earlier read') from a reader-facing note. Done: `አልዋሕ is the plural of ሉሕ 'tablet, board'; the glossary form earlier read ሊሕ, and the plural of ሉሕ is the likelier base (?); it takes` -> `አልዋሕ is the broken plural of ሉሕ 'board, tablet' (the lemma is ሉሕ, not ሊሕ); 'boards' is the safer sense here, since a replica is being made and the book of the law is to be laid inside it, though 'tablets' is possible (?); it takes`

- **10 · n · minor** · Label: ሥምረቶ is ሥምረት + the accusative form of -ሁ (-ኦ); '-ቶ' is not a suffix. Done: `(ሥምረት, with -ቶ)` -> `(ሥምረት + the accusative -ኦ 'his', written ሥምረቶ)`

- **11 · n · minor** · Label: the suffix on ፈቃዶ is -ኦ (accusative of -ሁ), not '-ዶ'. Done: `has an anticipating suffix (-ዶ)` -> `has an anticipating suffix (ፈቃድ + -ኦ 'his', written ፈቃዶ)`

- **13 · l · moderate** · l glossed ኪዳነ as construct 'covenant-of', contradicting n (accusative) and the grammar: it is followed by the relative ዘምስለ, which a construct cannot precede. Done: `Remembering covenant-of that-with` -> `Remembering covenant that-with`

- **13 · i · minor** · ተዘኪሮ is a gerund ('remembering', as l has it); i turned it into a finite future 'He will remember'. Done: `He will remember the covenant with our fathers Abraham, Isaac and Jacob; he will not falsify` -> `Remembering the covenant with our fathers Abraham, Isaac and Jacob, he will not falsify`

- **13 · n · minor** · Sentence repeated. Done: `. ከመ ኢያማስን is ከመ ኢ- + jussive 'so that he not destroy'.` -> `.`

- **14 · l · moderate** · ኀበ 'to-where' vs i 'How': neither fits; ኀበ is 'where' before a clause. Done: `63. To-where united` -> `63. Where united`

- **14 · i · moderate** · 'How' has no support in ኀበ (to, toward, at; where); the heading is 'Where ... united', with the sense uncertain. Done: `Chapter 63: How the great men of Israel agreed` -> `Chapter 63: Where the great men of Israel united (?)`

- **14 · n · moderate** · Note defended 'how'; rewritten to match; also subject, not accusative. Done: `ኀበ ordinarily means 'to, where'; here it opens a clause 'where/in what they united'. I take the sense as 'how the elders of Israel came to be of one mind' (?).` -> `ኀበ 'where' (conjunction) opens a clause, 'where the great ones of Israel united'; since the chapter tells of their agreement with Solomon, a sense 'in the matter in which they agreed' is possible (?).`

- **14 · n · minor** · Subject here; -ተ is the construct. Done: `ዐበይተ is the accusative-construct plural of ዐቢይ` -> `ዐበይተ is the construct plural (subject here) of ዐቢይ`

- **15 · i · moderate** · 'the Lord your God' adds 'Lord' (house rendering of እግዚኣብሔር is 'God') and 'be done' (not in ትኩን, 'be'; echoes 'Thy will be done'). Rebuilt from l. Done: `Let your pleasure be done, and the pleasure of the Lord your God.` -> `Let your pleasure be, and the pleasure of God, your God.`

- **15 · l · minor** · መላህቅተ is from መልህቅ 'anchor'; sense 'elders' is from context only; (?) added. Done: `answered-him elders-of Israel` -> `answered-him elders(?)-of Israel`

- **15 · n · moderate** · Note called መልህቅ 'elders'; the word means 'anchor' (Heb. 6:19 in the Geʿez Bible; Dillmann), so 'elders' is a figurative use taken from context. Also subject case. Done: `መላህቅተ 'elders', the accusative-construct plural of መልህቅ 'elders' (?).` -> `መላህቅተ 'elders', the construct plural of መልህቅ, which properly means 'anchor'; the sense 'stays of the people, elders' is taken from context and from the same word's use elsewhere in this work (?).`

- **15 · n · minor** · Gloss of አልቦ ዘንትዐደው contradicted its own parse ('none who transgresses' vs 1cp 'that we transgress'). Done: `'there is none (of us) who transgresses', with ዘ- + 1cp imperfect` -> `'there is nothing that we transgress', with ዘ- + 1cp imperfect`

- **15 · n · minor** · The -ሙ of ኢናየድዖሙ was left unexplained; it anticipates ለባዕድ አሕዛብ, as with other doubled objects in the part. Done: `1cp imperfect + -ሙ 'them' (?); the object is` -> `1cp imperfect + -ሙ 'them', anticipating ለባዕድ አሕዛብ (?); the thing told is`

- **16 · l · minor** · As unit 15: (?) on መላህቅተ. Done: `elders-of Israel with their-king` -> `elders(?)-of Israel with their-king`

- **17 · i · moderate** · ረስዐ is 'forget' (l 'forgot'); i 'lost' changes the sense. Done: `and lost his wisdom through his great love of women` -> `and forgot his wisdom through his great love of women`

- **17 · n · moderate** · 'forget, lose' - 'lose' has no basis. Done: `ረስዐ 'forget, lose', with` -> `ረስዐ 'forget', with`

- **19 · l · moderate** · እብኑ is እብን + -ሁ ('its stone'); the suffix was dropped. Colour words are not plurals (see n), so 'blacks reds' unfounded. Done: `and-wall-of stone pieces(?) in-blacks reds, in-whites greens,` -> `and-wall-of its-stone pieces(?) in-black red, in-white green,`

- **19 · i · moderate** · Same two points: 'its stone', and singular colour words. Done: `its stone wall was of slabs (?) in blacks and reds, whites and greens` -> `its stone wall was of slabs (?), in black and red, in white and green`

- **19 · n · moderate** · Mislabel: አስዋድ አሕማር አብያድ አክደር are Arabic masculine singular colour adjectives (afʿal pattern: aswad, aḥmar, abyaḍ, akhḍar); Arabic plurals are sūd, ḥumr, bīḍ, khuḍr. Also adds the suffixed እብኑ. Done: `four colour words in Arabic-pattern plurals (compare Arabic aswad 'black', aḥmar 'red', abyaḍ 'white', akhḍar 'green') (?), 'in blacks, reds, whites, greens'.` -> `four colour words, borrowed Arabic masculine singular colour adjectives of the afʿal pattern (compare Arabic aswad 'black', aḥmar 'red', abyaḍ 'white', akhḍar 'green'), not plurals; read as pairs, 'in black and red, in white and green' (?).`

- **19 · n · minor** · እብኑ unaccounted in note. Done: `መንድቅ 'wall' (construct መንድቀ);` -> `መንድቅ 'wall' (construct መንድቀ) before እብኑ 'its stone' (እብን + -ሁ);`

- **22 · n · minor** · Process reference to 'the known glossary entry' in a reader-facing note; also resolves the flagged 2ms/3fs point: the form is identical, the subject is she, so 3fs. Done: `(the known glossary entry has the 2ms; here the subject is she)` -> `(the form is the same as the 2ms; here the subject is she, so 3fs)`

- **22 · i · moderate** · አርሰዐ is 'cause to forget' (l 'made-him-forget'); 'lose' changes the sense; see unit 17. Done: `made him lose his wisdom` -> `made him forget his wisdom`

- **23 · i · moderate** · 'who bow down' makes ወይሰግዱ a relative clause on the Egyptians; the text has 'and they bow' (subject uncertain, Egyptians or her household). Done: `of the Egyptians, who bow down to the idol;` -> `of the Egyptians; and they bow down to the idol;`

- **23 · i · moderate** · ሐውዘ silently dropped from i although n says its sense is unclear; shown as unclear (cf. the earlier part's practice of leaving unknown Geʿez in brackets in i). Done: `and, delighting in their revelry, they bowed down with her` -> `and, delighting (?) in ሐውዘ (?) their revelry, they bowed down with her`

- **23 · l · minor** · ለጣዖታ is ጣዖት + -ኣ 'her idol', singular like ለጣዖት just before; 'idols' unfounded. Done: `for-her-idols` -> `for-her-idol`

- **23 · i · minor** · Same. Done: `for her idols` -> `for her idol`

- **23 · n · minor** · Label: ተምህረ is tä-stem, matching unit 3. Done: `(Gt of ምህረ` -> `(tä-stem of ምህረ`

- **25 · i · major** · i invents a meaning ('coaxing') for በአክሞስሶ, which n itself says is unclear (?); l leaves it Geʿez-unglossed. Done: `and with her coaxing (?), along with` -> `and with አክሞስሶ (?), along with`

- **25 · i · moderate** · 'his negligence' decides what n says is open (whose negligence). Done: `through his negligence;` -> `through negligence;`

- **25 · n · moderate** · Same: no reading is forced. Done: `(whose negligence, his or hers, is not said; I read it as his)` -> `(whose negligence, his or hers, is not said)`

- **25 · i · minor** · አንስት is plural: 'women's', not 'woman's'. Done: `soft (?) woman's talk` -> `soft (?) women's talk`

- **25 · i · minor** · አፈረሰ flagged (?) in l and n but not in i. Done: `she tore his heart from` -> `she tore (?) his heart from`

- **26 · i · minor** · የዐዝዞ flagged (?) in n but not in i. Done: `until the water seizes him` -> `until the water seizes (?) him`


## Findings refused (with reason)

- Unit 1 i, 'Hear what I have to tell you' loses the -ኒ ('hear me'): refused; the idiom is natural English and l keeps 'Hear-me'.
- Unit 2 n, ዘየአብያ: a possible reading of -ያ as a 3fs object suffix on የአቢ (hence 'refuses it, to his will') was considered; refused as unprovable. The note already says the parse is uncertain and the sense is clear.
- Unit 2 i, 'In heaven above and on earth below' (cf. Deuteronomy 4:39): refused; it is the direct rendering of በሰማይ በላዕሉ ወበምድር በታሕቱ and l is parallel.
- Unit 3 i, 'bow in worship' stronger than l 'bow (?)': refused; ተጋነየ is 'adore, do homage' (cf. ገነየ glosses in published parts).
- Unit 6 n, ቈላፋን 'plural of ቈላፍ': possible alternative base ቈሉፍ; refused as unresolvable without the lexicon and not affecting the sense.
- Unit 15 i, 'we will not transgress' vs present l: refused; a pledge in the imperfect, future force is acceptable (n corrected instead).
- Unit 16 i, 'and so it has stood until now' adds a clause: refused; n explains እስከ ይእዜ as the narrator's present, and the rendering is a legitimate paraphrase.
- Unit 18 i, 'so that it gave light' resolves the ዘያበርህ antecedent that n calls open: refused; 'it' stays ambiguous in English as in Geʿez.
- Unit 19 i, 'stones of sardius' for singular ወእብነ (construct): refused; collective, and matches the ch. 60b rendering.
- Unit 24 i, past 'took pleasure' for the imperfect ያስተኣድም: refused; narrative past throughout, same practice as units 20 and 22.
- ማቅሣራ / መቅሣራ both 'Maqsara': refused as a change; consistent, and n records the spelling variant.
- ሥረዊ, ብርት, ዐረር, ደፍዳፍ, አፍራጽ, አብላቅ, ልጐት, ጸቢተ, አፈረሰ, ቀጸበ: the drafter's (?) marks are kept as they are; none can be settled from Dillmann memory without overreaching.
- Paragraph (`p`) flags, unit boundaries, and `t`: checked against the packet; correct (p on units 0, 1, 14, 15 only; ch. 62 body and ch. 63 body are one paragraph each). Unit 25 (46 words, no ፤ to cut at) correctly left whole.

## Notes for pass 2 (gloss.json; not edited here)

- በአስዋድ / አሕማር glosses call the colour words 'Arabic-pattern plural'; they are masculine singular afʿal-pattern adjectives (see unit 19 n). አብያድ, አክደር likewise if glossed.
- መላህቅተ gloss: lemma መልህቅ properly 'anchor' (the published ch. 43 gloss has መልህቀ 'anchor'); keep 'elders' as figurative from context, as the ch. 38-39 gloss does; the ልሕቀ cf. in the entry is unsupported guesswork, drop or keep (?).
- ሊቃውንተ, ዐበይተ: construct, not 'accusative/construct' where used as subject.
- ሐውዘ: gloss and unit 23 now agree it is unclear.
- ተጋነየ forms and ተምህረ: label 'tä-stem' (not Gt).
- አልዋሕ: see above.


## Pass 2 (gloss.json)

Reviewer: pass 2. Edited gloss.json by script (valid JSON, 162 keys, every form of units.json still glossed, no stray keys); units.json untouched (byte-identical; `t` re-checked: joined `t` equals chapters 62-63 of the pinned source). Changes: 30 (major 0, moderate 9, minor 21).

### Changes (form · severity · why · new entry)

- **አልዋሕ · moderate** · lemma must be ሉሕ, leading, 'boards (?)'; ሊሕ was wrongly the lemma and called a variant (pass-1 instruction). New: `ሉሕ — boards (?) (plural አልዋሕ, the broken plural of ሉሕ 'board, tablet'; 'tablets' is possible) · in ch. 62 the boards of the proposed replica of Zion, to be set close, overlaid with gold and adorned, with feminine plural agreement (ስሙካን, ወልጹቃን, -ን 'them')`
- **እብኑ · moderate** · parse: the final -ኑ is the 3ms suffix (አብኑ = እብን + -ሁ), not a doubtful extra; unit 19 already reads 'its stone'. New: `እብን — its stone (noun + -ሁ '3ms its'; the -ኑ is the suffix -ሁ written after ን)`
- **በአስዋድ · moderate** · not a plural: afʿal-pattern masculine singular adjective (pass-1 ruling). New: `አስዋድ — black (borrowed Arabic masculine singular adjective, cf. Arabic aswad; በ- 'in')`
- **አሕማር · moderate** · not a plural (as above). New: `አሕማር — red (borrowed Arabic masculine singular adjective, cf. Arabic aḥmar)`
- **በአብያድ · moderate** · not a plural (as above). New: `አብያድ — white (borrowed Arabic masculine singular adjective, cf. Arabic abyaḍ; በ- 'in')`
- **አክደር · moderate** · not a plural (as above). New: `አክደር — green (borrowed Arabic masculine singular adjective, cf. Arabic akhḍar)`
- **መላህቅተ · moderate** · lemma meaning must be 'anchor' (Dillmann; Heb. 6:19), 'elders' only as figurative (?); 'accusative/construct' wrong (subject); unsupported 'cf. ልሕቀ' dropped. New: `መልህቅ — anchor (plural መላህቅት; construct መላህቅተ, subject here); here figuratively 'stays, elders', the sense taken from context, 'elders of' (?)`
- **ሊቃውንተ · minor** · case label: construct, not 'accusative/construct', as subject. New: `ሊቅ — chiefs, elders (plural ሊቃውንት; construct ሊቃውንተ 'chiefs of', subject here)`
- **ዘርኦሙ · moderate** · lemma: Geʿez dictionary form is ዘርእ (ዘር is not the Geʿez headword); ዘርኦሙ = ዘርእ + -ሙ. New: `ዘርእ — their seed (noun + -ሙ '3mp their'; anticipating ለአበዊነ)`
- **ወያረምም · moderate** · lemma inconsistent with አርመሙ (አርመመ); the same verb must carry one lemma. New: `አርመመ — and he is silent (ወ- + 3ms imperfect, causative-type stem; same verb as አርመሙ) (?)`
- **አርመሙ · minor** · wording aligned with ወያረምም; 'causative' of what is not shown, so 'causative-type'. New: `አርመመ — they fell silent (3mp perfect, causative-type stem) (?)`
- **ንትጋነይ · minor** · stem label: tä-stem (pass-1 ruling), as unit 3 n. New: `ተጋነየ — let us bow in worship (1cp jussive, tä-stem of ገነየ 'serve, do homage')`
- **ወተጋነዩ · minor** · stem label: tä-stem. New: `ተጋነየ — and they bowed in worship (ወ- + 3mp perfect, tä-stem of ገነየ)`
- **ወተምህሩ · minor** · stem label: tä-stem (unit 23 n). New: `ተምህረ — and they learned (ወ- + 3mp perfect, tä-stem of ምህረ)`
- **ወሥምረቶ · minor** · suffix: object of the verb, so accusative -ኦ (house style as ልቦ, ጥበቦ, ቃሎ; pass-1 on ሥምረቶ). New: `ሥምረት — and his pleasure (ወ- + noun, fem. accusative + -ኦ '3ms his')`
- **መዐቶ · minor** · suffix: object of the verb, so accusative -ኦ (house style as ልቦ, ጥበቦ, ቃሎ; pass-1 on ሥምረቶ). New: `መዐት — his wrath (noun accusative + -ኦ '3ms his')`
- **ሣህሎ · minor** · suffix: object of the verb, so accusative -ኦ (house style as ልቦ, ጥበቦ, ቃሎ; pass-1 on ሥምረቶ). New: `ሣህል — his mercy (noun accusative + -ኦ '3ms his')`
- **ኪዳኖ · minor** · suffix: object of the verb, so accusative -ኦ (house style as ልቦ, ጥበቦ, ቃሎ; pass-1 on ሥምረቶ). New: `ኪዳን — his covenant (noun accusative + -ኦ '3ms his')`
- **ነፍሶ · minor** · suffix: object of the verb, so accusative -ኦ (house style as ልቦ, ጥበቦ, ቃሎ; pass-1 on ሥምረቶ). New: `ነፍስ — his life, soul (noun accusative + -ኦ '3ms his')`
- **አስጥሞቶ · minor** · suffix: accusative -ኦ. New: `አስጠመ — to drown him (infinitive, causative accusative + -ኦ '3ms him')`
- **ሥምረተ · minor** · ሥምረተ ዚአነ (unit 11) is not a construct. New: `ሥምረት — pleasure, will (noun, fem.; construct 'pleasure of'; accusative as predicate before ዚአነ)`
- **ዘኢይሰዐር · minor** · gloss now says what the parse is doing (3ms verb with መንግሥቱ), matching unit 2 n. New: `ሰዐረ — which is not abolished, whose (kingdom) does not end (ዘ- relative + ኢ- + 3ms imperfect, G, s-ʿ-r; subject መንግሥቱ, read passively) (?)`
- **እምተስእኖ · minor** · line-pinned paraphrase removed. New: `ተስእኖ — impossibility, hardship (noun; እም- 'from, beyond') (?)`
- **ስሙካን · minor** · aligned with units 8 l/i ('set close', 'fixed'). New: `ሰመከ — fixed, set close (feminine plural adjective/participle; agrees with አልዋሕ; 'propped' possible) (?)`
- **ለጣዖታ · minor** · singular, as unit 23 after pass 1. New: `ጣዖት — for her idol (ለ- + noun, Greek loan + -ኣ '3fs her')`
- **የዐዝዞ · minor** · aligned with unit 26 i 'seizes (?)'. New: `ዐዘዘ — he seizes, grips him (3ms imperfect, G + -ሁ '3ms him') (?)`
- **እስከ (broaden) · minor** · aligned with የዐዝዞ / unit 26. New: `እስከ — until, as far as (preposition) · እስከ — conjunction before a verb, 'until' (እስከ የዐዝዞ ማይ 'until the water seizes him')`
- **ዘአውሥኦሙ · minor** · claim of a G base ወሥአ not secure; softened. New: `አውሥአ — that which he answered them (ዘ- relative + 3ms perfect, causative-type stem; the base verb is uncertain, + -ሙ '3mp them')`
- **ወአውሥኦሙ · minor** · aligned with ዘአውሥኦሙ. New: `አውሥአ — and he answered them (ወ- + 3ms perfect, causative-type stem + -ሙ '3mp them')`
- **ወቦኡ · minor** · root: ቦአ is b-w-ʾ. New: `ቦአ — and they entered (ወ- + 3mp perfect, G, b-w-ʾ)`

### Pass-1 corrections confirmed as applied
- አልዋሕ now leads with ሉሕ, 'boards (?)', and does not mention ሊሕ. Colour words: four masculine singular borrowed Arabic adjectives. ረስዐ / አርሰዐ: already 'forget' in gloss, no change. ኪዳነ: accusative in units (l and n); its entry is in known-forms and is not edited here. መልህቅ: lemma meaning 'anchor'.

### Refused (with reason)
- ታስተጣዕም lemma አስተጠዐመ: the long ጣ suggests a stem with ā (አስተጣዐመ), but I cannot confirm the headword from Dillmann memory; left as drafted, (?) kept.
- ሥረዊ, ብርት, ደፍዳፍ, አፍራጽ, አብላቅ (could be a plural of an unattested singular), ልጐት, ጸቢተ, ወንልብጦን, ወበፅዑ, ወያነግፈነ, ወኢናየድዖሙ, ወይሤርወነ, አእተተ, ወአእተዋ: dictionary forms not verifiable without the lexicon; each already (?).
- ዐበይተ ('plural, accusative form') and ሶበ-type known entries: pass 1 judged ዐበይተ here a construct subject; the entry belongs to a published part (known-forms) and is not edited; only the unit note was corrected.
- ወለሊሁኒ lemma ለሊሁ (vs ለሊ): both are attested; left.
- ወሰደኒ / ወሀለወት / ወእሉሂ lemmas (ወሰደ, ሀሎ, እሉ): acceptable dictionary forms; left.
- Numbers ፷፪ ፷፫: format follows the convention (spoken words, transliteration, English); left.
- ለሰሎሞን broaden example wording: usable as is; left.
- units.json: no change needed; l/i/n agree with the revised gloss (ሉሕ 'boards', singular colours, 'forget', 'set close', 'idol').
