# Chunhyang (열여츈향슈졀가, Wanpan 84-leaf, Dagaseopo printing) — pilot 001, leaves 1a–2a.
# Transcribed by eye from the University of Tokyo scan (L174842), 2026-11-22.
#
# Notation for old-Hangul syllables (expanded to conjoining jamo by build_chunhyang.py):
#   {hA}=ᄒᆞ  {hAi}=ᄒᆡ  {dAi}=ᄃᆡ  {sAing}=ᄉᆡᆼ  {bAik}=ᄇᆡᆨ  {mAi}=ᄆᆡ  {jAi}=ᄌᆡ  {nAi}=ᄂᆡ
#   {sdAi}=ᄯᆡ  {sgAi}=ᄭᆡ  {sgis}=ᄭᅵᆺ
# 〻 is the print's own repeat mark (U+303B).
#
# Each unit: t = printed text, words divided editorially (the print has no spaces);
# mt = modern spelling, one per word of t; say = what the voice reads (mt + punctuation);
# l / i / n as everywhere in Lectorium; p = starts a paragraph.

UNITS = [
 dict(p=True,
  t="슉종{dAi}왕 직위 초의 셩덕이 너부시사 셩자셩손은 계〻승〻{hA}사 금고옥족은 요슌 시졀이요 의관문물은 우탕의 버금이라",
  mt="숙종대왕 즉위 초에 성덕이 넓으시사 성자성손은 계계승승하사 금고옥족은 요순 시절이요 의관문물은 우탕의 버금이라",
  say="숙종대왕 즉위 초에 성덕이 넓으시사, 성자성손은 계계승승하사 금고옥족은 요순 시절이요, 의관문물은 우탕의 버금이라.",
  l="Of King Sukjong, at the accession’s beginning, the holy virtue being broad, the holy sons and holy grandsons generation after generation succeeding, the golden-drum jade-foot [days] were Yao and Shun’s age, and the robes-and-caps and culture were next after Yu and Tang.",
  i="In the first years of King Sukjong’s reign his holy virtue reached far and wide, and his sons and grandsons followed one another on the throne. It was a golden age like the days of Yao and Shun, and in dress and learning it came second only to the reigns of Yu and Tang.",
  n="The story opens the way Korean tales of its kind open, by naming a reign: Sukjong ruled Korea from 1674 to 1720. The print writes 대 ‘great’ as ᄃᆡ, with the old letter ㆍ (arae-a, ‘lower a’), which you will meet on every page — the toggle shows the modern spelling. 〻 is the print’s repeat mark: 계〻승〻 is 계계승승 ‘generation after generation’. 초의 is 초에 ‘at the beginning’: this book writes the place ending -에 as -의 throughout. 너부시사 is 넓으시사, spelled as it sounds, with the honorific -시- for the king. Yao, Shun, Yu and Tang are the sage-kings of ancient China, the standard of good rule. 금고옥족 is a set phrase for a golden age; editors disagree about which Chinese characters it stands for, and the literal line follows one guess."),
 dict(
  t="좌우보필은 쥬셕지신이요 용양호위난 간셩지장이라",
  mt="좌우보필은 주석지신이요 용양호위는 간성지장이라",
  say="좌우보필은 주석지신이요, 용양호위는 간성지장이라.",
  l="The left-and-right helpers were pillar-and-cornerstone ministers, and the dragon-rearing tiger-guards were shield-and-wall generals.",
  i="The ministers at his side were the pillars of the state, and the guards around him, fierce as dragons and tigers, were generals who stood like a city wall.",
  n="Both halves are built from Sino-Korean four-syllable phrases, Chinese words said the Korean way: 쥬셕지신 is 柱石之臣 ‘ministers who are pillars and cornerstones’, and 간셩지장 is 干城之將 ‘generals who are shield and city wall’. The 지 in each is Chinese 之 ‘of’. You’ll see this constantly: the narrator moves between plain Korean and strings of Chinese phrases, the learned style that pansori singers put on for grand moments. 호위난 is 호위는: the print writes the topic ending -는 as -난, as Jeolla speech says it."),
 dict(
  t="조경의 흐르난 덕화 힝곡의 폐엿시니 사{hAi} 구든 기운이 원근의 어려잇다",
  mt="조정에 흐르는 덕화 향곡에 퍼졌으니 사해 굳은 기운이 원근에 어려있다",
  say="조정에 흐르는 덕화 향곡에 퍼졌으니, 사해 굳은 기운이 원근에 어려있다.",
  l="The virtue-and-teaching flowing in the court had spread to the country villages, so the four seas’ firm spirit hung over far and near.",
  i="The good influence that flowed from the court had spread to every village, and a steady strength settled over the whole land, far and near.",
  n="조경 is printed for 조정 (朝廷) ‘the royal court’. 힝곡 is the print’s spelling of 향곡 (鄕曲) ‘the countryside, the villages’. 폐엿시니 is 퍼졌으니 ‘had spread, so…’. 사해, ‘the four seas’, means the whole realm. 구든 is 굳은 ‘firm’ and 어려잇다 is 어려 있다 ‘hangs over’ — once again the print spells words as they sound when spoken together."),
 dict(
  t="츙신은 만조{hA}고 효자열여 가〻{jAi}라",
  mt="충신은 만조하고 효자열녀 가가재라",
  say="충신은 만조하고 효자열녀 가가재라.",
  l="Loyal ministers filled the court, and filial sons and faithful wives were in house upon house.",
  i="Loyal ministers filled the court, and every house had its dutiful sons and faithful wives.",
  n="만조 (滿朝) is ‘filling the court’. 가〻{jAi}라 is 가가재(家家在)라 ‘they are in every house’. 열여, modern 열녀 (烈女), is the woman who keeps faith with her husband whatever it costs — the word in this book’s own title, 열여츈향슈졀가, ‘The Song of the Faithful Woman Chunhyang Keeping Her Chastity’."),
 dict(
  t="미{jAi}〻〻라",
  mt="미재미재라",
  say="미재미재라.",
  l="Beautiful indeed, beautiful indeed!",
  i="How fine it was, how very fine!",
  n="미재 is Chinese 美哉 ‘how beautiful!’, and the two repeat marks double the whole word: 미ᄌᆡ미ᄌᆡ. A short exclamation like this is the singer’s voice coming through the printed page."),
 dict(
  t="우슌풍조{hA}니 함포고복 {bAik}셩덜은 쳐〻의 격양가라",
  mt="우순풍조하니 함포고복 백성들은 처처에 격양가라",
  say="우순풍조하니 함포고복 백성들은 처처에 격양가라.",
  l="Rain being mild and wind timely, the mouths-full belly-drumming commoners [sang] everywhere the ground-striking song.",
  i="The rain came gently and the wind in its season, and everywhere the people, their bellies full, sang the old song of contentment.",
  n="우슌풍조 (雨順風調) is ‘the rain is gentle and the wind comes in season’ — good harvests. 함포고복 (含哺鼓腹) ‘mouth full of food, drumming on the belly’ is a contented people. 격양가 (擊壤歌) is the song of an old farmer in Yao’s time who beat time on the ground and sang that the emperor’s power meant nothing to him, because he never felt it: the classic picture of perfect peace. 덜 is the plural -들, as the region says it; 쳐〻의 is 처처에 ‘in every place’."),

 dict(p=True,
  t="잇{sdAi} 졀나도 남원부의 월{mAi}라 하난 기{sAing}이 잇스되 삼남의 명기로셔 일직 퇴기{hA}야 셩가라 {hA}는 양반을 다리고 셰월을 보{nAi}되",
  mt="이때 전라도 남원부에 월매라 하는 기생이 있으되 삼남의 명기로서 일찍 퇴기하여 성가라 하는 양반을 데리고 세월을 보내되",
  say="이때 전라도 남원부에 월매라 하는 기생이 있으되, 삼남의 명기로서 일찍 퇴기하여 성가라 하는 양반을 데리고 세월을 보내되,",
  l="At this time in Namwon district of Jeolla Province there was a kisaeng called Wolmae; being the famous kisaeng of the Three Southern Provinces, she had early retired from kisaeng life and, taking a yangban called Seong, was passing the years,",
  i="At this time there lived in Namwon, in Jeolla Province, a kisaeng named Wolmae. She had been the most famous kisaeng of the three southern provinces, but she had given up that life early and was living out her years with a gentleman named Seong.",
  n="잇{sdAi} is 이때 ‘at this time’, the narrator’s word for moving the story on; you’ll see it again and again. ᄯ is the old way of writing the tense consonant ㄸ. A 기생 (kisaeng) was a trained entertainer — singer, dancer, poet — and by law of the lowest class; 퇴기 is a kisaeng who has left the profession. A 양반 (yangban) is a member of the hereditary aristocracy. That a retired kisaeng and a yangban live together is the root of the whole plot: their daughter will belong to neither world. 졀나도 is 전라도, 다리고 is 데리고 ‘taking with her’, and the ending -되 leaves the sentence open: the ‘but’ comes in the next one."),
 dict(
  t="연장 사슌의 당하야 일졈 혈륙이 업셔 일노 한이 되야 장탄슈심의 병이 되것구나",
  mt="연장 사순에 당하여 일점 혈육이 없어 일로 한이 되어 장탄수심에 병이 되겠구나",
  say="연장 사순에 당하여 일점 혈육이 없어, 일로 한이 되어 장탄수심에 병이 되겠구나.",
  l="Her age reaching four decades, having not one dot of blood and flesh, by this it becoming grief, from long sighs and a sorrowing heart it was becoming an illness!",
  i="but she had reached forty without a single child of her own. It had become her great grief, and all her sighing and sorrow were wearing her into sickness.",
  n="사슌 (四旬) is ‘four tens’, forty. 일졈 혈륙 (一點血肉), ‘one drop of blood and flesh’, means a child of one’s own body. 일노 is 일로 ‘because of this’. 한 (恨) is a grief carried a long time, a word Koreans feel to be their own. 되것구나 is 되겠구나, and -구나 is an exclamation: the narrator speaks straight to the listeners, as a pansori singer does."),

 dict(p=True,
  t="일일은 크게 {sgAi}쳐 예사람을 {sAing}각{hA}고 가군을 쳥입{hA}야 엿자오되 공슌이 {hA}난 마리",
  mt="일일은 크게 깨쳐 옛사람을 생각하고 가군을 청입하여 여쭈오되 공순히 하는 말이",
  say="일일은 크게 깨쳐 옛사람을 생각하고 가군을 청입하여 여쭈오되 공순히 하는 말이,",
  l="One day, greatly awakening, she thought of the people of old, invited in the master of the house, and humbly addressing him, the words she said respectfully [were]:",
  i="One day she came to herself. Remembering what people had done in the old stories, she asked her husband in and spoke to him respectfully:",
  n="{sgAi}쳐 is 깨쳐 ‘waking up to it’ (ᄭ is the old way of writing ㄲ). 가군 (家君) ‘master of the house’ is how she refers to her husband. 엿자오되 is 여쭈오되, a humble verb for speaking to someone above you. 마리 is 말이 ‘the words (were)’: this book spells many words as they are pronounced, so 말이 comes out 마리. A speech is introduced with ‘the words she said’ and then simply begins."),
 dict(p=True,
  t="드르시요",
  mt="들으시오",
  say="들으시오.",
  l="Please listen.",
  i="Listen to me.",
  n="들으시오, the polite request ‘please listen’, spelled as it sounds."),
 dict(
  t="젼{sAing}의 무삼 은혜 {sgis}쳐던지 이{sAing}의 부〻 되야 창기 힝실 다 바리고 예모도 슝상{hA}고 여공도 심숫것만",
  mt="전생에 무슨 은혜 끼쳤던지 이생에 부부 되어 창기 행실 다 버리고 예모도 숭상하고 여공도 힘썼건만",
  say="전생에 무슨 은혜 끼쳤던지 이생에 부부 되어, 창기 행실 다 버리고 예모도 숭상하고 여공도 힘썼건만,",
  l="In a former life what kindness I bestowed, [that] in this life we became husband and wife; I threw away all a courtesan’s conduct, and revered propriety too, and labored at women’s work too, but",
  i="Whatever kindness I did you in a former life, in this one we became husband and wife. I gave up all a courtesan’s ways, I held to proper conduct, and I worked hard at a woman’s tasks.",
  n="전생 and 이생, ‘former life’ and ‘this life’, are Buddhist ideas everyone used: a marriage is a debt from a past life. 무삼 is 무슨 ‘what’. 부〻 is 부부 ‘husband and wife’. 창기 (娼妓) is a courtesan. 여공 (女工) is needlework and the household crafts. 심숫것만 is 힘썼건만 ‘I worked hard, but…’: in Jeolla speech ㅎ before i turns into s (힘 → 심), and the print writes it so. 바리고 is 버리고 ‘throwing away’."),
 dict(
  t="무삼 죄가 진즁{hA}야 일졈 혜륙 업셧스니 육친무족 우리 신셰 쳔영힝화 뉘라 {hA}며 사후감장 어이 하리",
  mt="무슨 죄가 진중하여 일점 혈육 없었으니 육친무족 우리 신세 선영향화 뉘라 하며 사후감장 어이 하리",
  say="무슨 죄가 진중하여 일점 혈육 없었으니, 육친무족 우리 신세 선영향화 뉘라 하며 사후감장 어이 하리.",
  l="What sin being heavy, [we] have had not one drop of blood and flesh; without kin and without family, our lot — the incense at the ancestral graves, who will do it, and burial after death, how will it be done?",
  i="But some sin of mine must weigh heavy, for we have not one child. We have no family to follow us. Who will burn incense at our ancestors’ graves, and who will bury us when we die?",
  n="혜륙 is printed here for 혈륙 (혈육) ‘blood and flesh’, which the page spelled in full a few lines earlier. 육친무족 (六親無族) ‘no close kin, no clan’. 선영향화 (先塋香火), the incense and offerings at the ancestors’ graves, were a son’s duty: this duty is the real cost of childlessness in a Confucian household. 쳔영 is the print’s spelling of 선영, and the reading of that word in the woodcut is uncertain. 뉘라 is ‘who’, 어이 is 어찌 ‘how’."),
 dict(
  t="명산{dAi}찰의 신고이나 {hA}야 남녀간 낫커드면 평{sAing} 한을 풀 거시니 가군의 뜻시 엇더{hA}오",
  mt="명산대찰에 신공이나 하여 남녀간 낳거드면 평생 한을 풀 것이니 가군의 뜻이 어떠하오",
  say="명산대찰에 신공이나 하여 남녀간 낳거드면 평생 한을 풀 것이니, 가군의 뜻이 어떠하오?",
  l="If, making devotions at famous mountains and great temples, we bear [a child], man or woman, I will undo the grief of a lifetime; what is the master’s mind?",
  i="If we offer prayers at the famous mountains and the great temples and have a child, boy or girl, it would ease the grief of a lifetime. What do you think?",
  n="명산대찰 (名山大刹) ‘famous mountains and great temples’ were where one went to pray for a child. 신고 is printed where the sense needs 신공 (身功) ‘devotions’. 남녀간 is ‘whether boy or girl’ — and it will be a girl. 낫커드면 is a dialect form of 낳거든 ‘if (we) bear’. 뜻시 is 뜻이 ‘your intention’: the print writes the ㅅ twice across the syllable break. 엇더ᄒᆞ오 is 어떠하오 ‘how is it?’, a polite question to a husband."),

 dict(p=True,
  t="셩참판 하는 마리",
  mt="성참판 하는 말이",
  say="성참판 하는 말이,",
  l="The words Seong the Vice-Minister said [were]:",
  i="Seong, the Vice-Minister, answered:",
  n="참판 (參判) is a vice-minister in one of the six ministries of state. Wolmae’s companion holds high office."),
 dict(
  t="일셩 신셰 {sAing}각{hA}면 자{nAi} 마리 당연{hA}나 비러셔 자식을 나흘진{dAi} 무자한 사람이 잇슬이요 {hA}니",
  mt="일생 신세 생각하면 자네 말이 당연하나 빌어서 자식을 낳을진대 무자한 사람이 있으리오 하니",
  say="일생 신세 생각하면 자네 말이 당연하나, 빌어서 자식을 낳을진대 무자한 사람이 있으리오, 하니,",
  l="“If I think of our lot over a lifetime, your words are right, but if by praying [one] could bear a child, would there be any childless person?” he said, and",
  i="“When I think of our whole life, you are right. But if children came from praying, would anyone be childless?” he said.",
  n="일셩 is printed for 일생 ‘a whole life’. 자네 is ‘you’ said to a wife or to someone younger. -ㄹ진대 means ‘if it is so that…’. 잇슬이요 is 있으리오, a question that expects no answer: ‘would there be…?’ — of course not. {hA}니 ‘he said, and…’ closes the quotation and hands the turn to Wolmae."),
 dict(p=True,
  t="월{mAi} {dAi}답하되",
  mt="월매 대답하되",
  say="월매 대답하되,",
  l="Wolmae answering said:",
  i="Wolmae replied:",
  n="-되 after a verb of saying introduces the speech: ‘she answered, saying…’."),
 dict(
  t="쳔하{dAi}셩 공부자도 니구산의 비르시고 졍나라 졍자산은 우셩산의 비러 나계시고",
  mt="천하대성 공부자도 이구산에 비시고 정나라 정자산은 우성산에 빌어 나계시고",
  say="천하대성 공부자도 이구산에 비시고, 정나라 정자산은 우성산에 빌어 나계시고,",
  l="“Even Master Kong, the great sage under heaven, was prayed for at Mount Niqiu, and Zichan of the state of Zheng was born by praying at Mount Useong,",
  i="“Even Confucius, the greatest sage under heaven, came of prayers on Mount Niqiu, and Zichan of Zheng was born after prayers on Mount Useong.",
  n="공부자 (孔夫子) is Confucius. His parents are said to have prayed for a son on Mount Niqiu (尼丘), and he was named Qiu after it. Zichan (died 522 BCE) was a famous minister of the state of Zheng; we do not know the source of the prayer story told of him here. 니구산 keeps the old initial n that modern South Korean spelling drops (이구산). The honorific -시- in 비르시고 and 나계시고 shows Wolmae’s respect for the sages."),
 dict(
  t="아동방 강산을 이를진{dAi} 명산{dAi}쳔이 업슬손가",
  mt="아동방 강산을 이를진대 명산대천이 없을쏜가",
  say="아동방 강산을 이를진대 명산대천이 없을쏜가.",
  l="If one speaks of the rivers and mountains of our Eastern Land, could it be that there are no famous mountains and great rivers?",
  i="And if we speak of the mountains and rivers of our own Eastern Land, are there no famous mountains and great rivers here?",
  n="아동방 (我東方) ‘our Eastern Land’ is Korea, as Koreans called it in the classical language. -ㄹ손가 (modern -ㄹ쏜가) is a question that means ‘surely not’: of course there are."),
 dict(
  t="경상도 웅쳔 쥬쳔의난 늘도록 잔여 업셔 최고봉의 비러더니 {dAi}명쳔자 나계시사 {dAi}명쳔지 발거스니",
  mt="경상도 웅천 주천의는 늙도록 자녀 없어 최고봉에 빌었더니 대명천자 나계시사 대명천지 밝았으니",
  say="경상도 웅천 주천의는 늙도록 자녀 없어 최고봉에 빌었더니, 대명천자 나계시사 대명천지 밝았으니,",
  l="Ju Cheonui of Ungcheon in Gyeongsang Province, having no children into old age, prayed on the highest peak, and a Son of Heaven of the great Ming was born, and heaven and earth grew bright with a great brightness;",
  i="Ju Cheonui of Ungcheon in Gyeongsang Province had no children into his old age. He prayed on the highest peak, and a Son of Heaven of the great Ming was born to him, and the whole world grew bright.",
  n="Wolmae tells a Korean legend that made the founder of China’s Ming dynasty (1368) the son of a man from Ungcheon in Korea, and she treats it as fact. The sentence plays on 대명: 大明 ‘the great Ming’ and ‘great brightness’, so the Ming emperor’s birth makes 대명천지, ‘the great bright world’, bright. 잔여 is printed where the sense needs 자녀 ‘children’, and 늘도록 is 늙도록 ‘until old age’. 발거스니 is 밝았으니 ‘grew bright, so…’."),
 dict(
  t="우리도 졍셩이나 듸려 보사이다",
  mt="우리도 정성이나 들여 보사이다",
  say="우리도 정성이나 들여 보사이다.",
  l="Let us too try offering devotion at least.",
  i="Let us try what devotion can do.",
  n="정성 (精誠) is wholehearted devotion. 듸려 is 들여 ‘offering it’, and -어 보- means ‘try doing’. -사이다 is the old polite ‘let us’, modern -ㅂ시다."),
 dict(
  t="공든 탑이 무너지며 심근 남긔 쎅길손가",
  mt="공든 탑이 무너지며 심은 나무 꺾일쏜가",
  say="공든 탑이 무너지며 심은 나무 꺾일쏜가.",
  l="Would a tower built with labor collapse, would a planted tree be broken?",
  i="Would a tower built with care fall down? Would a tree you planted snap?",
  n="공든 탑이 무너지랴, ‘would a tower built with care fall?’, is a proverb still used today: real effort is never wasted. 남긔 is an old form of 나무 ‘tree’. 쎅길손가 is our reading of a worn word in the woodcut; the sense must be 꺾일쏜가 ‘could it be broken?’."),
]
