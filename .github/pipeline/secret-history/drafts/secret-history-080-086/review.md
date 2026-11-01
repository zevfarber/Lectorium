# Review of secret-history-080-086 (§§80–86)

Reviewer, two passes. Unit numbers count the 66 sentences of units.json from 0 (unit numbers are those of the draft; no unit was added or removed). Ming glosses, Shiratori and the published parts (§§1–79 and the glossary) only; no modern translation opened or recalled. Counts are per edit; one flaw needing edits in l, i, n and a morph is counted in each field. Both files were backed up before editing and remain valid JSON in the same schema.

## Pass 1 — units.json

Checked by script against packet.md: all 502 words consumed exactly once in order, every `t` equal to the packet words, `words` count equal to each unit's word count, every word's morphs still carry the packet's Ming gloss in square brackets, `p: true` on the first unit of each of §§80–86 (units 0, 15, 26, 37, 46, 52, 60) and nowhere else, and no unit straddling a § boundary. Every note label was checked against the form, original → l word by word, l ↔ i, remembered English, and the house renderings (Tarqutai-Kiriltuq, Qada'an, Taichi'ud, Onan, tede 'those/they', že 'indeed, so', abura- and -žuγu as in the glossary).

### Counts (pass 1)
| severity | changes |
|---|---|
| major | 0 |
| moderate | 22 |
| minor | 84 |
| trivial | 14 |
| total | 120 |

### Changes (unit · field · severity · what was wrong · what was done)

- unit 1 · i · moderate · 'he found' is not in the words (aisuqui-dur 'when coming' is just the time clause). · "Leading his horse along, he found, as he came, that the saddle had slipped off the horse and fallen." -> "As he came, leading his horse along, his saddle slipped off the horse and fell."
- unit 1 · words[5].morph · minor · Empty morph (lemma and gloss both blank) after in-ü would show a blank chip. · "{"lemma": "", "gloss": ""}" -> "(removed)"
- unit 2 · i · minor · üžeġesü is the conditional 'when he looked' (Ming 看呵), not purposive 'to look'; 'he saw that' is not in the words. · "Turning back to look, he saw that the saddle, with breast-strap and girth still buckled, had slipped off and fallen." -> "Turning back, when he looked, the saddle had slipped off and fallen, with breast-strap and girth still buckled."
- unit 3 · i · moderate · 'you' contradicts the note (Ming 也 'also', či may be a particle); '(he said)' is not in the words; no quotation reading fits 'you may give way'. · ""Girth, you may (give way)," (he said)." -> ""The girth too, let it be;"
- unit 3 · n · minor · Note and i now agree on či. · "so či may be a particle here, not the pronoun)" -> "so či may be a particle here, not the pronoun; i reads it as 'too')"
- unit 4 · i · minor · 'But' is not in the words; the quotation begins in the previous unit. · ""But how did the breast-strap slip off as well?"" -> "how did the breast-strap slip off as well?""
- unit 5 · l · moderate · Ming 莫不 introduces a suspicion ('could it be that…'); 'surely-not' read it as a negative question. · "Heaven forbidding surely-not, saying," -> "Heaven forbidding, can-it-be,"
- unit 5 · i · moderate · 'Is Heaven not forbidding me?' expects the opposite of 莫不; 'me' is not in the words (note says the object is unstated), now bracketed. · ""Is Heaven not forbidding me?" he said," -> ""Could Heaven be forbidding (me)?" he said,"
- unit 5 · n · minor · Same. · "'surely not?', the tag that turns a statement into a question" -> "'can it be that…?', the tag that turns a statement into a question of suspicion"
- unit 5 · n · minor · Same. · "I read the line as "Is Heaven not holding me back?" The Ming leaves the object unstated." -> "I read the line as "Could Heaven be holding (me) back?" The Ming leaves the object unstated."
- unit 5 · words[2].morph gloss (-ju) · minor · 莫不 = 'could it be that', not 'surely not'. · "question tag: surely not? (Ming 莫不; form uncertain)" -> "question tag: can it be …? (Ming 莫不; form uncertain)"
- unit 6 · n · minor · Muddled arithmetic ('six … then three again…') replaced by the actual count. · "So Temüžin hides six nights in all, three and three, then three again... the text now counts a further three, and the next lines run to a total of nine (jesün qonoγ)." -> "So that is three nights, then three more, six in all; a third three follows after the rock (next units), which brings the total to nine, the jesün qonoγ 'nine nights' …"
- unit 7 · n · minor · -žuγu is one past ending (as in ažuγu, glossary 'past ažuγu'); converb + -γu was inconsistent with unit 13. · "una- 'fall' + -žu + the past -γu (倒了)" -> "una- 'fall' + the past ending -žuγu (倒了)"
- unit 7 · words[11].morph gloss (-žu) · minor · Same. · "converb: -ing" -> "past (perfect): had …-en (Ming 倒了)"
- unit 7 · words[11].morph lemma · minor · Same. · "-žu" -> "-žuγu"
- unit 8 · l · moderate · Follows unit 5. · ""Heaven forbidding surely-not," saying, turning-back again three spent." -> ""Heaven forbidding can-it-be," saying, turning-back again three spent."
- unit 8 · i · moderate · Same as unit 5; also 'again' (basa) belongs with the three nights, not with 'said'. · ""Is Heaven not forbidding me?" he said again, and turned back and spent three more nights." -> ""Could Heaven be forbidding (me)?" he said, and turned back and spent three nights more."
- unit 8 · words[2].morph gloss (-ju) · minor · Same as unit 5. · "question tag: surely not? (Ming 莫不; form uncertain)" -> "question tag: can it be …? (Ming 莫不; form uncertain)"
- unit 9 · i · moderate · 'and thought' is not in the words (the verb of saying is keġežü in the next unit); 'with no name made' invents 'made'. · "Again he stayed nine nights without food, and thought, "To die with no name made, how can it be?" -> "Again he stayed nine nights without food. "How am I to die with no name?"
- unit 9 · n · minor · 'made' is not in nere ügei. · "a man who has made no name" -> "a man with no name"
- unit 10 · i · minor · keġežü 'saying' was left unrendered. · "I will go out!"" -> "I will go out!" he said,"
- unit 11 · i · minor · 'tried to' is not in γarγasu (conditional 'if/when he went out'). · "When he tried to go out round the white rock, as big as a tent, that had fallen and blocked the entrance, it was not possible;" -> "If he went out round the white rock, as big as a tent, that had fallen and blocked the entrance, it was not possible;"
- unit 14 · n · minor · The last unit ended with ažuγu, so the chain does not 'run on' from it. · "The chain runs on from the last unit, and ends with this full stop." -> "This is a short new chain, closed by the full stop (the last unit ended in a finite verb)."
- unit 15 · i · minor · House spelling is Tarqutai-Kiriltuq (§§64–79 and the glossary). · "Targutai-Kiriltuk took Temüjin away," -> "Tarqutai-Kiriltuq took Temüjin away,"
- unit 15 · words[1].morph gloss (Tarγutai-Kiriltuγ) · minor · House spelling. · "Targutai-Kiriltuk, a man's name (Ming 人名) [人名]" -> "Tarqutai-Kiriltuq, a man's name (Ming 人名) [人名]"
- unit 16 · l · trivial · l follows žasaγ-la- 'making a rule'. · "Realm, people to-his-own, ordering," -> "Realm, people to-his-own, rule-making,"
- unit 16 · i · minor · ulus (Ming 國) was dropped; 'ordering' over-reads žasaγlažu 'making a regulation'. · "ordering his own people," -> "laying down a rule for his own realm and people,"
- unit 17 · n · minor · Note said bitü- = 'close, wrap' while the morph says 'take around'. · "and bitüġülün is bitü- 'close, wrap' with a causative and -n (Ming 徇着, 'taking round, parading'); the stem is uncertain." -> "and bitüġülün is Ming 徇着, 'taking round, parading': I read a stem bitü- (its sense uncertain; 'close' does not obviously fit) + the causative -ġül- + -n."
- unit 20 · i · moderate · 'had been put in charge of' is not in abčiražü büleġe (Ming 將着有來 'was leading/taking along'). · "At that feast, a weak young man had been put in charge of Temüjin," -> "At that feast a weak young fellow was taking Temüjin along,"
- unit 20 · n · minor · Matches i. · "So: 'a weak lad was holding him', that is the guard." -> "So: 'a weak lad was taking him along', that is, the guard."
- unit 21 · n · minor · Unsupported claim about who disperses. · "Here it is the feasters who go home, not the Taichi'ud directly. " -> "The causative -γul- needs someone who sends them off, and the sentence does not name him. "
- unit 23 · i · minor · keġežü is 'saying' (Ming 說着), not 'thinking'. · "thinking, "If I lie down inside the wood of the Onan, I shall be seen,"" -> "saying, "If I lie down inside the wood of the Onan, I shall be seen,""
- unit 23 · n · trivial · Matches i. · "keġežü 'saying' ends the thought." -> "keġežü 'saying' ends the quotation."
- unit 25 · n · minor · Speculation that the ending marks a change of subject replaced by a stated, flagged parse. · "which is perhaps why this converb ends in -γan and not -žu." -> "I read -γan as a causative -γa- + the converb -n ('letting flow'), which would explain why it is not -žu, but the Ming 流着 does not mark a causative (敎), so this is unc…"
- unit 25 · words[3].morph gloss (-γan) · minor · Same. · "converb: -ing (form uncertain)" -> "converb -n, perhaps with a causative -γa-: 'letting flow' (form uncertain)"
- unit 26 · n · moderate · Label 'let us / let him' contradicted i 'Seize him!' and the Ming. · "+ -ja (the 'let us / let him' ending, Ming 拿住)" -> "+ -ja (shaped like the 'let us' ending -je of bedereje, but the Ming 拿住 has no 咱 'us', so I read it as a call, 'seize!'; the ending is uncertain)"
- unit 26 · words[5].morph gloss (-ja) · minor · Same. · "optative: let …! (Ming 住)" -> "ending of a call: seize! (shape of the 'let us' ending -je; Ming 住; form uncertain)"
- unit 27 · n · minor · 'beat the ground' is not in 排尋. · "'searched through in a line, beat the ground'" -> "'searched in a line'"
- unit 27 · words[9].morph gloss (bedere-) · minor · Same. · "to search through, beat the ground (Ming 排尋了; stem inferred) [排尋了]" -> "to search through, search in a line (Ming 排尋了; stem inferred) [排尋了]"
- unit 29 · n · minor · 'a common saying about Temüžin' is not in the words. · "keġen 'saying' makes 'fire in the eyes, light in the face' a common saying about Temüžin, and the speech goes on in the next unit." -> "keġen 'saying' closes this stretch; who is saying it the words do not tell, and the 'they say' of i is my guess. The speech goes on in the next unit."
- unit 30 · n · minor · Note said the object is not in the words and then took it from aqa deġü-deġen. · "Whom they envied is not in the words; from the saying just before, it is Temüžin. I take aqa deġü-deġen as 'their own kin', so they envy a kinsman; the Ming does not m…" -> "I take aqa deġü-deġen (Ming 弟 自的行, with 行 marking the object) as the ones envied, 'their own kin'; Temüžin is surely the kinsman meant, but the words do not name him."
- unit 31 · words[3].morph gloss (kebte-) · minor · A morph with lemma '-' is not a morpheme; folded into the stem's gloss (cf. glossary ügüle). · "to lie down (Ming 臥着) [臥着]" -> "to lie down (the bare stem serves as the imperative here; form uncertain) [臥着]"
- unit 31 · words[3].morph · minor · Same. · "{"lemma": "-", "gloss": "imperative (form uncertain)"}" -> "(removed)"
- unit 31 · n · minor · Editorial claim not in the words. · " A short and tactful speech, and it saves Temüžin." -> " A short speech."
- unit 32 · n · minor · Ming 咱 is not on this word. · "(Ming 咱 'let us')" -> "('let us'; the Ming glosses this word 排尋 only, and adds 咱 to the same ending in the next sentence)"
- unit 32 · words[2].morph gloss (-je) · minor · Same. · "'let us' (first-person wish; Ming 咱)" -> "'let us' (first-person wish; the Ming 咱 stands on the same ending in the next sentence, not here)"
- unit 33 · l · moderate · 'said.' belongs to keġebe in the next unit. · ""The-very the-very way-by not seen (of) land-his-own having-looked, back let-us-search," said." -> ""The-very the-very way-by not seen (of) land-his-own having-looked, back let-us-search,""
- unit 33 · i · moderate · 'he said' is the next unit's keġebe; 'by the way we came' and 'go back over' over-read mör(i)-er-en. · ""Let us go back over the very same ground by the way we came, and search the places we have not yet seen," he said." -> ""Let us go back the very same way, look over the ground we have not yet seen, and search again,""
- unit 34 · words[1].morph gloss (-kü) · trivial · 'also, indeed (Ming 那般)' assigned a Ming word to kü and contradicted unit 31. · "also, indeed (Ming 那般)" -> "emphatic particle, as in tein kü above (the Ming 那般者 glosses the pair)"
- unit 35 · i · minor · 'close by the place' is not in the words. · "They went back by the same road, searching, and Sorqan-Shira again passed close by the place and said:" -> "They went back by the same road, searching, and Sorqan-Shira again passed by and said:"
- unit 35 · n · minor · saraγur-a is a dative, not an instrumental; the cross-reference was wrong. · "the -jer is the vowel-ending form, as in saraγur-a above." -> "this is the same ending as -jar in kituγai-jar(i)-jan above, in its front-vowel form."
- unit 36 · n · minor · Unlabelled bare stem. · "aisu 'come' (來有)" -> "aisu 'come' (來有; the stem shows no ending, and I read it as a present, 'are coming', from the Ming 有)"
- unit 38 · l · moderate · Ming 大王(每) 'great lords' not honoured. · ""Taičiγud sons, you bright white day whole person escaped." -> ""Taičiγud lords, you bright white day whole person escaped."
- unit 38 · i · moderate · Ming 大王每 not honoured ('sons'); 'from you' is not in the words (ta is the address 'you'). · ""Sons of the Taichi'ud, in broad white daylight a whole man has slipped away from you." -> ""You lords of the Taichi'ud, in broad white daylight a whole man has slipped away!"
- unit 38 · n · moderate · Same. · "the Ming glosses it 大王每, 'princes, great lords', so 'my lords' is the address, 'Taichi'ud sons / princes'." -> "but the Ming glosses it 大王每, 'great lords, princes', and l and i follow the Ming: 'lords of the Taichi'ud'."
- unit 38 · words[1].morph gloss (köġün) · minor · Same. · "son (Ming 大王每, 'princes') [大王(每)]" -> "son, here 'lord, prince' (Ming 大王每, which reads the plural as an honorific address) [大王(每)]"
- unit 39 · t / words · moderate · Bida opens the next sentence in Shiratori (capital B after 'olqun.'), but sat at the end of this unit; sentence-unit follows his punctuation. · "Edöġe qaraṅγui süni ker olqun. Bida" -> "Edöġe qaraṅγui süni ker olqun."
- unit 40 · t / words · moderate · Same: Bida moved to the head of the sentence it belongs to. · "basa mün mün mör(i)-jer ese üžegsen γažar(i)-jan üžeġed qarin bedereġed tarqažu" -> "Bida basa mün mün mör(i)-jer ese üžegsen γažar(i)-jan üžeġed qarin bedereġed tarqažu"
- unit 39 · l · minor · Bida removed; l no longer carries 'we'. · "Now black night how shall-we-get?" -> "Now black night how get-shall?"
- unit 39 · n · moderate · Note no longer matches the unit boundary. · "and bida is 'we (inclusive)' (咱). The ending -qun makes a question: 'how are we to get (him)?'" -> "(Bida 'we', 咱, belongs to the next sentence.) The ending -qun makes a question and marks no person; 'we' in i is the searchers' own, as the next sentence's Bida shows."
- unit 40 · l · moderate · Bida added to l. · "Again the-very the-very way-by not seen (of) land-his-own having-looked, back having-searched, dispersing," -> "We again the-very the-very way-by not seen (of) land-his-own having-looked, back having-searched, dispersing,"
- unit 40 · n · minor · Note covers the moved word. · "Basa mün mün mör(i)-jer" -> "Bida 'we' (咱) opens the sentence (Shiratori's capital). Then basa mün mün mör(i)-jer"
- unit 42 · i · trivial · Že-kü rendered 'So be it' in unit 34; 'again' is not needed after qarin 'back'. · "he said. "Very well," they agreed, and searched back again," -> "he said. "So be it," they agreed, and searched back,"
- unit 43 · i · minor · 'close' is not in the words. · "and Sorqan-Shira again passed close by and said: "So much for the searching; let us turn back and look tomorrow, so we have agreed." -> "and Sorqan-Shira again passed by and said: "So much for the searching; let us turn back and look tomorrow, so we have agreed."
- unit 43 · n · minor · 'they' and 'we' contradicted each other in the note. · "keġeldübe 'they said together'. The speech is Sorγan-Šira's, and keġeldübe 'we said together' reports the agreement made with the searchers;" -> "keġeldübe 'said together' (共說了) marks no person; since the speech is Sorγan-Šira's, I read it as 'we have agreed', the searchers and himself;"
- unit 44 · i · moderate · 'when they have broken us up' supplies a subject 'they' and contradicts the note ('when we have been dispersed'); tarqaγulun is a causative with no named agent. · "Now, when they have broken us up and finished, go and look for your mother and your brothers." -> "Now, when we have all been sent away, go and look for your mother and your brothers."
- unit 45 · i · minor · Doubled closing quotation marks; inner quotations given single marks. · "If you are seen by anyone, do not say, "He saw me." Do not say, "I was seen."" So he spoke, and went on his way." -> "If you are seen by anyone, do not say, 'He saw me.' Do not say, 'I was seen.'" So he spoke, and went on his way."
- unit 45 · n · moderate · Note said 'me' is Sorγan-Šira's, which made the proposed reading self-contradictory. · "Nama-ji is nama (the oblique stem of bi 'I') + -ji (accusative), 'me' (我行); užebe is 'saw' (見了). keġen closes a quotation (麽道). küġün-e is 'to a person' (人行); üžegdeġe…" -> "Nama-ji is nama (the oblique stem of bi 'I') + -ji (accusative), 'me' (我行); užebe is 'saw' (見了). keġen closes a quotation (麽道). küġün-e is 'to a person' (人行); üžegdeġe…"
- unit 45 · words[8].morph gloss (-le) · trivial · 'imperative' stated without caveat. · "imperative (Ming 說)" -> "ending of the forbidden verb, imperative (form uncertain; Ming 說)"
- unit 46 · i · minor · 'all' is not in the words. · "When they had all dispersed, Temüjin thought to himself:" -> "When they had been dispersed, Temüjin thought to himself:"
- unit 46 · words[0].morph gloss (an) · trivial · Stem is inferred. · "them (third-person plural oblique stem; Ming 他每) [他每行]" -> "them (third-person plural oblique stem, inferred; Ming 他每) [他每行]"
- unit 47 · i · minor · 'for me' is not in the words. · ""Yesterday, when they were making me go round the camps and lodge, I lodged at Sorqan-Shira's house, and his two sons, Chimbai and Chila'un, grieved in their hearts fo…" -> ""Yesterday, when they were making me go round the camps and lodge, I lodged at Sorqan-Shira's house, and his two sons, Chimbai and Chila'un, felt pain in their hearts."
- unit 47 · n · minor · Same. · "their hearts hurt, they felt pity." -> "their hearts ached (the Ming gives no cause; the next unit has them seeing him)."
- unit 47 · n · minor · Inconsistent with unit 17's analysis. · "bitüġülžü is the causative of bitüġül- as in §81 (徇着)" -> "bitüġülžü is bitü- + the causative -ġül- + -žü, as in §81 (徇着)"
- unit 47 · words[14].morph lemma · minor · ebedčü = ebed- + converb -čü (as kürčü, abču), not ebedče- + -ü. · "ebedče-" -> "ebed-"
- unit 47 · words[14].morph lemma · minor · Same. · "-ü" -> "-čü"
- unit 50 · l · minor · tede is 'they, those' (Ming 他每; glossary), not 'these'. · "Now just these me (acc.) will-save, so-be-it," saying," -> "Now just they me will-save, so-be-it," saying,"
- unit 50 · i · minor · 'these' for tede; 'surely' for mün-kü (Ming 只 'only'); že was dropped. · "Now surely these will save me," he said," -> "Now only they will save me — so be it," he said,"
- unit 50 · n · minor · Editorial claim not in the words. · " Temüžin has decided to go back to the sons, and this is the first time he sees them as saviours." -> ""
- unit 50 · words[1].morph gloss (-kü) · minor · Contradicted the published mün-kü entry. · "also, indeed (Ming 只)" -> "particle (as in tein-kü and mün-kü of the published parts; sense uncertain, the Ming 只 'only' covers the pair)"
- unit 50 · words[5].morph gloss (že) · trivial · The packet Ming is 也者. · "so be it (Ming 者) [也者︀]" -> "so be it (Ming 也者) [也者︀]"
- unit 52 · l · minor · 'fermented' is not the Ming (熟 'ripe'). · "House's sign: fresh mare's-milk having-poured-out, fermented-mare's-milk his-own, through-the-night until day dawned, churning was." -> "House's sign: fresh mare's-milk having-poured-out, ripe-mare's-milk his-own, through-the-night until day dawned, churning was."
- unit 52 · i · minor · 'fermented'; pluperfects had/had been for büleġe 'was'. · "As a sign of the house, they had poured out the fresh mare's milk, and all night until the day was bright they had been churning their own fermented milk." -> "As a sign of the house, they poured out the fresh mare's milk, and all night until the day was bright they were churning their own ripe mare's milk."
- unit 52 · n · trivial · qumis is an inference. · "'their own ripe mare's-milk (qumis)'" -> "'their own ripe mare's-milk (perhaps qumis)'"
- unit 52 · n · minor · qumis-making is not in the words. · "The sign would be: the household is busy making qumis, so a sound of churning marks it." -> "The sign would be the sound of churning that marks the household."
- unit 52 · words[4].morph gloss (esüge) · minor · Same. · "fermented mare's milk, qumis (Ming 熟馬妳子) [熟馬妳子自的行]" -> "ripe mare's milk, perhaps qumis (Ming 熟馬妳子) [熟馬妳子自的行]"
- unit 52 · n · minor · Participle -kü was not analysed. · "bülekü is Ming 澎, 'to splash, to churn', with büleġe 'was'." -> "bülekü is Ming 澎, 'to splash, to churn': büle- + the participle -kü (as in mültürekü), with büleġe 'was'."
- unit 52 · words[8].morph lemma · minor · Stem büle- + -kü, as büleġür in unit 53. · "bülekü-" -> "büle-"
- unit 52 · words[8].morph · minor · Added the participle -kü. · "(none)" -> "-kü=participle"
- unit 53 · i · minor · 'said' is keġebe in unit 55, not in this unit. · "Following that sign, he listened as he went, heard the sound of the churning, and came to the house; when he went in, Sorqan-Shira said:" -> "Following that sign, he listened as he went, heard the sound of the churning, and came to the house; when he went in, Sorqan-Shira—"
- unit 53 · n · minor · Duplicate sentence; points to the verb. · " Then the subject Sorγan-Šira (a name, 鎖兒罕失剌) and the colon of speech comes in the next unit. The speech follows in the next unit; no verb of saying is written here." -> " Then comes the subject Sorγan-Šira (a name, 鎖兒罕失剌); no verb of saying is written here (it is keġebe in unit 55), and the speech follows in the next unit."
- unit 54 · l · minor · 'said.' belongs to keġebe in the next unit. · "mother-your-own, younger-brothers-your-own seeking go; not-did-I-say? Why came you?" said." -> "mother-your-own, younger-brothers-your-own seeking go; not-did-I-say? Why came you?""
- unit 54 · i · minor · 'he said' belongs to keġebe in the next unit. · ""Did I not tell you to go and look for your mother and your brothers? Why have you come?" he said." -> "Did I not tell you to go and look for your mother and your brothers? Why have you come?""
- unit 54 · n · minor · 'angry' is not in the words. · "So Sorγan-Šira is angry that he came to the house, as he said what he said in §83." -> "So Sorγan-Šira asks why he came to the house after being told (§83) to go."
- unit 56 · n · trivial · Etymology not from the Ming. · " (雀兒, šibaγuqan, a diminutive of šibaγun 'bird')" -> " (雀兒)"
- unit 56 · n · minor · i silently dropped the word. · "flagged as uncertain." -> "flagged as uncertain; i leaves turimtai unrendered."
- unit 56 · n · minor · Unsupported 'old past' and speculation on repetition; made consistent with -žuγu. · "abura- 'save' + -žu + γui, an old past 'has saved'. The subject buta stands alone, which is why it is repeated." -> "abura- 'save' + the past ending -žuγui (like -žuγu in ažuγu), 'has saved'."
- unit 56 · words[5].morph gloss (-žu) · minor · Same. · "converb: -ing" -> "past (perfect): has … (Ming 救了有)"
- unit 56 · words[5].morph lemma · minor · Same. · "-žu" -> "-žuγui"
- unit 59 · i · moderate · 'behind the house' invents 'house'; 'they hid him away' drops the causative asaraγulba (the note itself says who 'had' it done is unclear); house spelling Qada'an. · "and set him on the wool cart behind the house, saying to their sister, named Qadagan, "Tell no living person." So they hid him away." -> "and set him on the wool cart at the back, saying to their sister, named Qada'an, "Tell no living person," and had him put away."
- unit 59 · n · minor · una- is 'fall' (unit 7). · "unuγulžu is una- 'mount'" -> "unuγulžu is unu- 'mount'"
- unit 59 · n · trivial · Packet writes 敎. · "(坐着教, 'making sit')" -> "(敎坐着, 'making sit')"
- unit 59 · n · trivial · Packet writes 敎. · "(教收拾了)" -> "(敎收拾了)"
- unit 59 · words[4].morph gloss (Qadaγan) · trivial · House spelling Qada'an (glossary). · "Qadagan, a woman's name (Ming 女名) [女名]" -> "Qada'an, a woman's name (Ming 女名) [女名]"
- unit 59 · words[10].morph gloss (-le) · trivial · As unit 45. · "imperative (Ming 說)" -> "ending of the forbidden verb, imperative (form uncertain; Ming 說)"
- unit 60 · i · minor · Ming 藏了 does not say 'himself'; the search of one another in the next unit presupposes a hider. · "On the third day they said together, "The man has hidden himself, surely,"" -> "On the third day they said together, "The man has been hidden, surely,""
- unit 60 · n · minor · Matches i and the glossary. · "'the person has hidden'; že is the particle 'so'" -> "'the person has been hidden'; že is the particle 'indeed, so' (Ming 也者)"
- unit 60 · n · minor · Wrong: the print closes the quotation after že. · "The quotation mark runs through 'že' to the close of the next unit." -> "The quotation closes at 'že'; the next unit has a second, short one."
- unit 60 · words[4].morph gloss (že) · trivial · Packet Ming is 也者. · "so be it (Ming 者) [也者︀]" -> "so be it (Ming 也者) [也者︀]"
- unit 61 · i · minor · 'one another's places' is not in the words. · ""Let us search among ourselves," and they searched one another's places." -> ""Among ourselves, let us search one another," they said together, and they searched one another."
- unit 61 · n · minor · 'tents' invented. · "The Taichi'ud turn from the field to their own tents." -> "They now search among themselves."
- unit 63 · n · minor · 'empty the cart' over-reads. · "So they empty the cart from the mouth towards the foot, and when they get there Sorγan-Šira speaks." -> "The sense is that they work through the wool from the cart's mouth towards its foot; Sorγan-Šira speaks in the next unit."
- unit 64 · l · minor · 'saying,' is kēġesü, the first word of the next unit. · "Sorγan-Šira: "This again such hot wool inside how bearing?" saying," -> "Sorγan-Šira: "This again such hot wool inside how bearing?""
- unit 64 · i · minor · 'said' belongs to kēġesü in the next unit; ene basa 'this again' was dropped. · "Sorqan-Shira said, "In such hot wool as this, how could anyone bear it?"" -> "Sorqan-Shira: "This too — in such hot wool, how is one to bear it?""
- unit 64 · n · minor · Wrong reference. · "The sentence has been running without a main verb since the head of §86;" -> "The sentence has been running without a main verb since unit 62;"
- unit 64 · n · moderate · 'a trick … turns the searchers away' is not in the words; kēġesü is not in this unit and 説 is not the packet's 說. · "The words are a trick: he says nobody could hide in wool so hot, and so turns the searchers away. kēġesü is keġe- + -sü, the conditional (説呵, 'when he said')." -> "Read with the context, the question means that no one could bear it inside wool so hot; the next unit has the searcher leave."
- unit 65 · i · minor · kēġesü 'when he said' was rendered 'At these words'. · "At these words the searcher climbed down and went away." -> "When he had said this, the searcher climbed down and went away."
- unit 65 · n · minor · Morph called -ġül- 'agent-maker' while it is the causative elsewhere. · "(nüṅči- + -ġül- + -sün; the ending is uncertain)" -> "(nüṅči- + an agent ending -ġülsün, perhaps the causative -ġül- + -sun; uncertain)"
- unit 65 · words[1].morph · minor · Two morphs (-ġül- 'agent-maker' + -sün) merged into one ending. · "-ġül- + -sün" -> "-ġülsün"
- unit about · about · minor · Sorqan-Shira speaks five times in §§82–83, not three. · "three speeches" -> "speeches"

## Pass 2 — units.json re-check and gloss.json

Units were re-read after pass 1 (l/i of every changed unit, quotation marks across unit boundaries, the moved word Bida, the script checks again: PASS). Every gloss.json entry was then checked against the text, its morph in units.json, the Ming bracket in novel-forms.json, grammar naming, the dictionary form, and against known-forms.json for broadening. Keys are exactly the 175 novel tokens plus `__broaden__`; broadening entries are old entry whole + ' · ' + new reading.

### Counts (pass 2)
| severity | changes |
|---|---|
| major | 0 |
| moderate | 10 |
| minor | 14 |
| trivial | 5 |
| total | 29 |

### Changes

- unit 39 · n · trivial · Stray comma left by the Bida edit. · "participle, (Bida" -> "participle. (Bida"
- unit 16 · n · minor · House spelling Tarqutai missed in the note. · "Targutai ordering" -> "Tarqutai ordering"
- gloss aqu-ju · moderate · 莫不 introduces a suspicion, 'could it be that'; agrees with units 5 and 8. · "'surely not?'" -> "'can it be …?'"
- gloss unažuγ̇u · moderate · Converb -žu + -γu split a single past ending (cf. ažuγ̇u in the glossary, and unit 13). · "una- — to fall; converb -žu + past -γu, 'had fallen' (verb, converb + past) [倒了]" -> "una- — to fall; past ending -žuγu, 'had fallen' (verb, past) [倒了]"
- gloss barija · moderate · 'let …!' optative contradicted the unit's reading and the Ming. · "bari- — to seize, hold; -ja, 'let …!' (verb + optative; Ming 住, form uncertain) [拿住]" -> "bari- — to seize, hold; -ja, an ending of a call, 'seize!' (shaped like the 'let us' ending -je, but the Ming 拿住 has no 咱; verb + ending; form uncertain) [拿住]"
- gloss urusγan · minor · Matches unit 25's flagged parse. · "urus- — to flow; converb -γan, 'flowing' (verb, converb; form uncertain) [流着]" -> "urus- — to flow; converb -n, perhaps with a causative -γa-, 'flowing, letting flow' (verb, converb; form uncertain) [流着]"
- gloss bederebe · minor · 'beat the ground' is not in 排尋. · "to search through, beat the ground" -> "to search through, search in a line"
- gloss ebedčü · minor · ebedčü is ebed- + -čü (like kürčü), not ebedče- + -ü; matches unit 47. · "ebedče- — to pain, ache (stem uncertain); converb -ü, 'aching' (verb, converb) [疼着]" -> "ebed- — to hurt, ache (stem inferred from the Ming 疼着); converb -čü, 'aching' (verb, converb) [疼着]"
- gloss esügi · minor · 'fermented' / qumis is not the Ming (熟 'ripe'). · "fermented mare's milk, qumis (noun)" -> "ripe mare's milk, perhaps qumis (noun; Ming 熟 'ripe')"
- gloss bülekü · minor · Participle -kü unanalysed; matches unit 52. · "bülekü- — to churn, splash (stem uncertain; the Ming says 澎) (verb, participle or verbal noun; form uncertain) [澎]" -> "büle- — to churn, splash (stem inferred from the Ming 澎); participle -kü, 'churning' (verb, participle; form uncertain) [澎]"
- gloss aburažuγ̇ui · moderate · Converb + 'an old past' split; matches unit 56 and ažuγ̇u. · "abura- — to save, rescue; converb -žu + -γui, an old past, 'has saved' (verb, converb + past) [救了有(來)]" -> "abura- — to save, rescue; past ending -žuγui, 'has saved' (verb, past) [救了有(來)]"
- gloss nünčiġülsün · minor · -ġül- was called 'agent-maker' though it is the causative elsewhere; matches unit 65. · "nüṅči- — to search; -ġül- (agent-maker, form uncertain) + -sün, noun-maker, 'one who searches' (verb + noun-maker; both endings uncertain) [搜的]" -> "nüṅči- — to search; agent ending -ġülsün (perhaps the causative -ġül- + -sun), 'one who searches' (verb + agent ending; uncertain) [搜的]"
- gloss šibaγ̇uqan-i · trivial · Etymology not from the Ming. · " (noun, a diminutive of šibaγun 'bird')" -> " (noun)"
- gloss kelele · trivial · Caveat as in units 45 and 59. · "imperative -le, 'speak!' (verb, imperative;" -> "imperative -le, 'speak!' (verb, imperative, form uncertain;"
- gloss an-i · trivial · Stem is inferred (unit 46). · "third-person plural oblique stem)" -> "third-person plural oblique stem, inferred)"
- gloss __broaden__.čilaγ̇un · moderate · Known entry is 'stone'; here the personal name (Ming (兒)名), units 47 and 55. · "(not broadened)" -> "also Čilaγ̇un, Chila'un, a son's name (personal name; Ming (兒)名)"
- gloss __broaden__.qadaγ̇an · moderate · Known entry is a son's name; here the sister (unit 59). · "(not broadened)" -> "also a woman's name, Qada'an, a sister (Ming 女名)"
- gloss __broaden__.nögčibe · moderate · Known entry is 'died' [死了]; here Ming 過去了 (units 31, 36, 45). · "(not broadened)" -> "also 'passed on, went on', in kēġed nögčibe 'having said, he went on' (Ming 過去了)"
- gloss __broaden__.köġüd · moderate · Unit 38: the Ming reads köġüd as 'great lords'. · "(not broadened)" -> "also 'lords, princes' in the address Taičiγud köġüd (Ming 大王每)"
- gloss __broaden__.bitüġülžü · minor · Known entry is 輪着; unit 47 has Ming 敎徇着. · "(not broadened)" -> "also 'taking round, parading' (Ming 敎徇着), the causative converb of §81's bitüġülün"
- gloss __broaden__.unužu · minor · Known entry is 騎着; unit 63 has Ming 上着. · "(not broadened)" -> "also 'mounting, climbing up' onto the cart (Ming 上着)"
- gloss __broaden__.nigente · minor · Known entry is 'once' [一遍]; unit 22 has Ming 一下. · "(not broadened)" -> "also 'at one blow' (nigente deledüġed, 'struck once'; Ming 一下)"
- gloss __broaden__.aba · minor · Known entry is 'dwelt' [住了]; unit 49 has Ming 有來. · "(not broadened)" -> "also nögčin aba, 'was passing on' (a- as 'be', past; Ming 有來)"
- gloss __broaden__.daγ̇u · moderate · Known entry is 'time, occasion' [遍]; unit 53 has Ming 聲. · "(not broadened)" -> "also 'voice, sound' (Ming 聲), as in büleġür-ün daγ̇u, 'the sound of the churner'"
- gloss __broaden__.belge · moderate · Known entry is 'betrothal gift' [定禮]; unit 52 has Ming 記號. · "(not broadened)" -> "also 'sign, mark' (Ming 記號), as in ger-ün belge, 'the sign of the house'"
- gloss __broaden__.mün-kü · minor · Known entry is 只那; unit 50 has Ming 只. · "(not broadened)" -> "also mün kü 'only, just' (Ming 只), as in edöġe mün-kü tede, 'now only they'"
- gloss __broaden__.üžegsen · minor · Known entry segments üžeg- + -sen; the part's morphs use üže- + -gsen. · "(not broadened)" -> "also read üže- 'see' + the past participle -gsen (the segmentation of §§80–86), 'seen' (Ming 見的)"
- gloss __broaden__.jen · minor · 'fermented' is not the Ming 熟 'ripe'. · "one's own fermented milk" -> "one's own ripe mare's milk"
- gloss möri · trivial · Ming bracket differed from novel-forms.json ([路 自的行]). · "[路]" -> "[路 自的行]"

## Findings refused (with reason)

- unit 58 i 'Disregarding their father's word' for ülü taγalan (不愛 'not liking'): kept; the note already flags the shade, and 'unwilling to heed' is the plain sense of a negated 'like' before üge.
- unit 12 i 'timber' for mudud: kept; Ming 木每 is a plural of 'wood, trees' and the unit is about cutting through the thicket.
- unit 18 tergel 'circle': kept; flagged uncertain in the note and the glossary entry (Ming (圖)兒).
- unit 29 i 'they say': kept as a flagged guess (note now says so); the words close with keġen and nothing else renders it.
- unit 39 i 'find' for olqun (Ming 得 'get'): kept; ol- covers both and 'find' reads naturally.
- unit 5 / 8 morph a- + -qu + -ju: the segmentation is unverifiable and already marked uncertain.
- unit 24 'the edition prints -dür at the next line's start': cannot be checked from the packet (line numbers only); left.
- unit 36 lemma '-n-u' for čin-u: odd but harmless; the token is covered by the known entry čin-u.
- unit 53 / 64 'Sorqan-Shira said': the verb sits in the neighbouring unit (keġebe, kēġesü); the colon and dash were kept as reader aids, the word 'said' removed.
- unit 21 'seized' for tatažu abču (扯着要着): kept; 'pulled and took' would only be a stiffer rendering of the same.
- unit 36 'grinding your mouths and teeth': kept; the note says the image is not understood.
- Names: Sorqan-Shira, Suldus, Chimbai, Chila'un are new in this part and follow the pilot's style; no published precedent to check.

## Remaining doubts

- The Bida move (units 39/40) follows Shiratori's capital after 'olqun.'; if the owner prefers the draft's boundary it is one word.
- Units 5 and 8: 莫不 as 'could it be that' is my reading of Yuan-period usage, not shown in the packet.
- Unit 29–30: who 'says' fire-in-eyes, and the object of naitaγdan, stay uncertain.
- Unit 33 / 40: the 'same road' + 'unseen ground' pairing is the Ming's and still odd.
- Unit 44: the agent of the causative tarqaγulun (and in unit 46) is unnamed.
- Unit 59: who 'had him put away' (asaraγulba) is unresolved; asara- here 'put away' versus 'tend, care for' elsewhere in the glossary (not broadened because the tokens differ).
- Unit 25: urusγan as causative 'letting flow' is only a guess.
- Unit 52: Ming 熟 vs qumis; bülekü / büleġür analysed as büle- + endings without a Ming gloss to confirm.
- Unit 56: turimtai remains unrendered.
