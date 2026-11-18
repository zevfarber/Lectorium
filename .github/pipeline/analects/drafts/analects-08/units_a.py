# Analects Book 8 (泰伯) — draft, first half: lemmata 0–15 = passages 8.1–8.10. Token format as the pilot:
#   tokens separated by " | "; a token is  CHARS[PUNCT][=pinyin][/context gloss[//char gloss//char gloss]]
#   a leading "^" breaks the verse line before the token.
# Punctuation is editorial (the edition has none) and always trails the word before it.
# Pinyin defaults to the glossary's first reading; every polyphone states its reading here, and so does
# every character not yet in the glossary.
# Passage numbering follows Zhu Xi's chapter breaks (凡二十一章; the ○ marks confirm the brief's list):
# 8.2 runs over two units (Zhu Xi records Wu's view that 君子篤於親… is a separate chapter, but prints it
# in 8.2, and so do we), 8.4 over three, 8.7 over two, 8.8 over three.
# Misprint corrected in the reading text (rule 5b; emend.json entry for unit 5 already present): 8.4 the
# print has 地 for 也 (其鳴也哀).
# Quotation marks balance within every unit (as Books 5–7). A unit cannot open with 「, so where a
# speech runs on past one of Zhu Xi's comments (8.2 unit 2, 8.4 unit 6, 8.7 unit 10) the first unit
# closes the quotation and the continuation is left unquoted, Chinese and English alike (as 6.28);
# 8.8, whose three clauses Zhu Xi interrupts after each, is left unquoted throughout (as 7.6).
# Glyphs kept as the edition prints them: 巳 (= 已, read yǐ, 8.1 也巳矣), 啓 (= 啟), 虚, 顏, 𢎞 (U+22390,
# = 弘, read hóng, 8.7).
# Readings Zhu Xi marks that modern practice does not keep: 遠 yuàn (8.4 遠暴慢, 遠鄙倍; 遠近並去聲 —
# we give yuǎn; 近 去聲 is modern jìn anyway); the note says so once. Kept: 夫 fú (8.3, 音扶), 與 yú
# (8.6, 平聲), 好 hào (8.10, 去聲), 葸 xǐ (絲里反), 絞 jiǎo (古卯反), 倍 bèi (= 背). Stated though Zhu Xi
# gives no tone note: 樂 yuè (8.8, music), 興 xīng (起也), 校 jiào (計校), 稱 chēng, 召 zhào, 任 rèn,
# 薄 bó, 予 yú, 巳 yǐ.
# Collation: He Yan's text has 所貴道者 (no 乎) in 8.4 — noted. The brief's "He Yan 好勇貧 (no 疾)" in 8.10 is
# an artefact: the SBCK transcription writes 疾 there as the private-use entity &KR0858;, which it uses for
# 疾 throughout (伯牛有&KR0858;, 子&KR0858;病), and Bao Xian's comment glosses it 患疾; no variant is noted.

UNITS_A = [
# ---------------- 8.1 ----------------
dict(pas="8.1", w="子/the Master | 曰：「/said | ^泰伯，=tài bó/Taibo — eldest son of the Great King of Zhou//great//eldest (son) | ^其/surely | 可/can | 謂/be called | 至/utmost | 德/virtue | 也/(assertion) | 巳=yǐ/(and that is all) (巳, the edition's form of 已) | 矣。/(so it is) | ^三/three times | 以/taking | 天下=tiān xià/the world | 讓，/(he) yielded (it) | ^民/the people | 無/had no (way) | 得/to manage | 而/to | 稱=chēng/praise (him) | 焉。」/for it",
  l="The Master said: “Taibo —\nhe can surely be called utmost virtue, and that is all.\nThree times he yielded the world,\nand the people found no way to praise him for it.”",
  i="The Master said: “Taibo's virtue surely deserves to be called the utmost. Three times he gave the world away, and the people never knew what to praise him for.”",
  n="The book is named 泰伯 from its first words; Zhu Xi's heading says only that it has twenty-one chapters (凡二十一章). 泰伯 Taibo was the eldest son of the Great King of Zhou (大王), with two younger brothers, Zhongyong 仲雍 and Jili 季歷. 其可謂… 'surely (he) can be called…': 其 at the head softens the judgement into 'surely'. 至德 'utmost virtue' — Zhu Xi: virtue at its utmost, to which nothing more could be added. 也巳矣 piles three final particles, 'and that is all, it is so': a judgement stated with full conviction (the same clause is said of King Wen's virtue in 8.20, and has the same English there); 巳 is the edition's form of 已 yǐ here (as at 5.26 and 6.28), and He Yan's text has it too. 以天下讓 'taking the world, yielded (it)'; 三 'three times' — Zhu Xi: 三讓 means a firm refusal (固遜), not a count. 無得而稱焉 'had no way to praise (him) for it': 焉 'for it'. Zhu Xi tells the story: Shang's Way was waning and Zhou growing strong; Jili had a son, Chang 昌, of sagely virtue, and the Great King came to mean to overthrow Shang; Taibo did not go along with this, the King wished to pass his place to Jili and so on to Chang, and Taibo, knowing it, fled with Zhongyong to the Jing Man tribes of the south. Jili inherited; Chang came to hold two parts in three of the realm — he is King Wen — and Chang's son Fa conquered Shang and had the realm — King Wu. With his virtue, at the turn from Shang to Zhou, Taibo could have had the lords at his court and held the realm; he cast it away, and effaced his tracks too, so that his yielding was hidden and left no trace to see — hence the people found nothing to praise. His heart, Zhu Xi says, was the heart of Boyi and Shuqi when they 'held the horse' (扣馬 — by tradition King Wu's, as he set out against Shang), but his position was harder; no wonder the Master sighed over him and praised him. (Taibo's not going along, he notes, is recorded in the Chunqiu commentary, 春秋傳.) He Yan's Wang Su: knowing that Chang would surely have the realm, Taibo three times yielded the world to Jili; the yielding was hidden, so no one could praise him, and that is why it was utmost virtue."),
# ---------------- 8.2 ----------------
dict(pas="8.2", w="子/the Master | 曰：「/said | ^恭/courteous | 而/but | 無/without | 禮/the rites | 則/then | 勞，/toil | ^慎/careful | 而/but | 無/without | 禮/the rites | 則/then | 葸，=xǐ/fearfulness | ^勇/brave | 而/but | 無/without | 禮/the rites | 則/then | 亂，/disorder | ^直/straight | 而/but | 無/without | 禮/the rites | 則/then | 絞。」=jiǎo/cutting, twisted too tight",
  l="The Master said: “Courteous but without the rites — then toil;\ncareful but without the rites — then fearfulness;\nbrave but without the rites — then disorder;\nstraight but without the rites — then cutting.”",
  i="The Master said: “Courtesy that does not go by the rites wears a man out; care that does not go by the rites leaves him afraid of everything; courage that does not go by the rites makes trouble; and straightness that does not go by the rites cuts like a cord pulled too tight.”",
  n="Four lines of one build: a quality, 而 'but', 無禮 'without the rites', then 則 'then' and what it turns into. 葸 xǐ (Zhu Xi: 絲里反) is the look of fear; 絞 jiǎo (古卯反) is 'to twist tight', and Zhu Xi glosses it 急切 'pressing, sharp'; He Yan's Ma Rong: 絞刺 'stinging, cutting'. Zhu Xi: without the rites there is no measure and form (節文), hence the four faults. He Yan's commentary on 葸: careful without the rites to regulate it, one is forever afraid."),
dict(w="君子/the gentleman | 篤=dǔ/(being) earnest, devoted | 於/to | 親，/(his) kin | ^則/then | 民/the people | 興=xīng/rise up, are stirred | 於/to | 仁；/humaneness | ^故舊=gù jiù/old friends, associates of long standing//old, former//old | 不/(being) not | 遺，=yí/cast off, forgotten | ^則/then | 民/the people | 不/(are) not | 偷。=tōu/thin-hearted, cold (Zhu Xi: 薄也)",
  l="When the gentleman is devoted to his kin,\nthe people rise to humaneness;\nwhen old friends are not cast off,\nthe people do not grow cold.",
  i="When the gentleman above them is warm toward his own kin, the people are stirred to humaneness; when he does not forget old friends, the people do not grow cold toward one another.",
  n="Two conditions, each joined to its result by 則 'then', with no word for 'when'. 君子 here, Zhu Xi says, is 'the man in high place' (在上之人) — the ruler whose example the people follow. 篤 dǔ is 'solid, earnest'; 興 xīng 'to rise, be stirred' (Zhu Xi: 起也); 故舊 'old associates', those one has known long; 遺 yí 'to leave behind, forget'; 偷 tōu, usually 'to steal', here 'thin, mean' (Zhu Xi: 薄也; He Yan's Bao Xian likewise ends 不偷薄也). Zhu Xi quotes Zhang Zai: when the way of men knows what comes first and what after, courtesy does not wear one out, care does not cower, courage does not riot, straightness does not cut; the people are transformed and their virtue grows thick. He also quotes Wu 吳氏: from 君子 on should be a chapter of its own, and is Master Zeng's words; and adds his own judgement: this section does not connect with what goes before and is close in spirit to 1.9 (慎終追遠), so Wu is probably right. We keep it in 8.2, as Zhu Xi prints it. Bao Xian: if the ruler is generous to his kin and does not forget his old friends, the people are transformed and rise to humane and generous conduct."),
# ---------------- 8.3 ----------------
dict(pas="8.3", w="曾子=zēng zǐ/Master Zeng | 有/had | 疾，/an illness | ^召=zhào/(he) called | 門/(of his) gate, school | 弟子/the disciples | 曰：「/(and) said | ^啓/lay bare (the covers off) | 予=yú/my | 足！/feet | ^啓/lay bare | 予=yú/my | 手！《/hands | 詩》/the Odes | 云：『/say | ^戰戰=zhàn zhàn/trembling, in dread//to tremble//to tremble | 兢兢，=jīng jīng/wary, on guard//cautious//cautious | ^如/as if | 臨/looking down into | 深=shēn/a deep | 淵，/pool | ^如/as if | 履=lǚ/treading on | 薄=bó/thin | 冰。』=bīng/ice | ^而/and | 今/now | 而/and | 後，/after | ^吾/I | 知=zhī/know | 免/(I have) come through | 夫，=fú/(exclamation) | ^小子！」/young ones",
  l="Master Zeng was ill.\nHe called the disciples of his school and said: “Lay bare my feet!\nLay bare my hands! The Odes say:\n‘Trembling and wary,\nas if looking down into a deep pool,\nas if treading on thin ice.’\nNow, and from now on,\nI know I have come through,\nmy young ones!”",
  i="When Master Zeng was ill, he called his disciples to him and said: “Draw back the covers from my feet, and from my hands. The Odes say: ‘In dread, on guard, as at the edge of a deep pool, as on ice that may break.’ From this day on I know I am safe from all that, my lads.”",
  n="曾子 Master Zeng (Zeng Shen, 1.4). 召 zhào is 'to summon'; 門弟子 'the disciples of his gate', i.e. his school (弟子 in its sense of a master's disciples). 啓 qǐ is 'to open' (Zhu Xi: 開也; the edition's form of 啟); 予 yú 'my'. Zhu Xi: Master Zeng had always held that the body is received from one's parents and must not be harmed, so now he had the disciples open his coverlet and look. The lines are from the ode Xiaomin 小旻: 戰戰 is fear, 兢兢 caution — doubled words that describe, bound here like 申申 in 7.4; one is afraid of falling at the edge of a deep pool, afraid of breaking through on ice. 而今而後 'now and after': from this moment on. 免 'to escape, come through' — Zhu Xi: only at the point of death did he know he had escaped harm to his body. 夫 fú is an exclamation (Zhu Xi: 音扶). 小子 'young ones' are the disciples (Zhu Xi: 門人也); he calls to them again when he has finished, to press the lesson home. Zhu Xi quotes Master Cheng: of the gentleman one says 'he ended', of the small man 'he died'; the gentleman counts keeping his body whole till death as finishing his task, so Master Zeng counted returning whole as 'coming through'. Yin Tun: 'whole did his parents bear him, whole should the son return'; Master Zeng had them uncover his hands and feet at the end for this reason — who could do it without having grasped the Way? Fan Zuyu: if the body must not be marred, how much less may one mar one's conduct and so disgrace one's parents? He Yan's Zheng Xuan says the same of the coverlet; Kong Anguo: he quotes the ode to liken himself — always careful, fearing harm; Zhou Shenglie: only today do I know I have escaped trouble and disaster; 小子 are the disciples, called so that they would hear and remember."),
# ---------------- 8.4 ----------------
dict(pas="8.4", w="曾子=zēng zǐ/Master Zeng | 有/had | 疾，/an illness | ^孟敬子=mèng jìng zǐ/Meng Jingzi — Zhongsun Jie, a grandee of Lu//Meng (the clan)//Jing, 'the Reverent' (his posthumous name)//master (an honorific) | 問/asked after | 之。/him",
  l="Master Zeng was ill,\nand Meng Jingzi asked after him.",
  i="Master Zeng was ill, and Meng Jingzi came to ask how he was.",
  n="孟敬子 Meng Jingzi, Zhu Xi says, was a grandee of Lu of the Zhongsun (= Mengsun) house, personal name Jie 捷; 問之 is to ask about his illness. He Yan's Ma Rong: a grandee of Lu, of the Zhongsun."),
dict(w="曾子=zēng zǐ/Master Zeng | 言/spoke (unasked) | 曰：「/saying | ^鳥=niǎo/a bird | 之/(clause marker) | 將=jiāng/being about to | 死，/die | ^其/its | 鳴=míng/cry | 也/(pause) | 哀；/(is) sorrowful | ^人/a man | 之/(clause marker) | 將=jiāng/being about to | 死，/die | ^其/his | 言/words | 也/(pause) | 善。」/(are) good",
  l="Master Zeng spoke up and said:\n“A bird that is near its death —\nits cry is sorrowful;\na man that is near his death —\nwhat he says is good.”",
  i="Master Zeng spoke to him unasked: “When a bird is dying its call is full of grief; when a man is dying, what he says comes from the best in him.”",
  n="The print has 地, a misprint for 也, corrected here. Both collation witnesses (Ruan's 1816 text and He Yan's text) read 其鳴也哀, and the clause is built exactly like the next, 其言也善, where 也 marks the pause after the topic: 'its cry — sorrowful', 'his words — good'. 鳥之將死 'a bird's being about to die': 之 between subject and verb makes the clause a time phrase, 'when a bird is about to die'; 將 jiāng 'about to'. 言曰 — Zhu Xi: 言，自言也, he spoke of his own accord, not in answer. Zhu Xi: a bird fears death, so its cry is sad; a man at the end of his road goes back to the root, so his words are good. It is Master Zeng's self-effacing way of putting it: he wants Jingzi to recognize that what follows is good and to remember it. He Yan's Bao Xian: he wished to warn Jingzi — 'I am about to die; my words are good and can be used.'"),
dict(w="君子/the gentleman | 所/what | 貴/prizes | 乎/in | 道=dào/the Way | 者/(the things) | 三：/(are) three | ^動/(in) moving | 容貌，=róng mào/his bearing and looks: the whole person//bearing//looks, outward appearance | ^斯/thereby | 遠=yuǎn/(he) keeps far off | 暴/harshness | 慢=màn/(and) insolence | 矣；/(so it is) | ^正/(in) setting right | 顏色，=yán sè/his countenance, the expression of his face//face//colour, look | ^斯/thereby | 近/(he) comes close to | 信/good faith | 矣；/(so it is) | ^出/(in) bringing out | 辭氣，=cí qì/his words and tone of voice//words//breath, tone | ^斯/thereby | 遠=yuǎn/(he) keeps far off | 鄙=bǐ/the crude | 倍=bèi/(and) the unreasonable (= 背 'to go against') | 矣。/(so it is) | ^籩豆=biān dòu/the bamboo and wooden vessels of the rites//a bamboo dish//a wooden dish on a stem | 之/'s | 事，/business | ^則/then | 有司=yǒu sī/officers in charge//there are//to manage; an officer | 存。=cún/are there (for it)",
  l="What the gentleman prizes in the Way is three things:\nmoving his bearing,\nhe thereby keeps harshness and insolence far off;\nsetting his countenance right,\nhe thereby comes close to good faith;\nbringing out his words and tone,\nhe thereby keeps the crude and the unreasonable far off.\nThe business of the bamboo and wooden vessels —\nfor that there are officers in charge.",
  i="There are three things in the Way that a gentleman sets most store by: that in every movement of his body he is free of harshness and insolence; that the face he composes is close to what he truly is; and that when he speaks, his words and his voice are free of anything crude or unreasonable. The arranging of the ritual dishes is the business of the officers in charge of it.",
  n="Master Zeng's words run on from the last unit; the commentary has broken them. 所貴乎道者三 'what (he) prizes in the Way are three': 所 + verb makes 'what he prizes', 乎 is 'in' (= 於), and 者 closes the noun phrase. Then three lines of one build: verb + object, 斯 'thereupon, thereby', and the result, sealed by 矣. Zhu Xi: 貴 is 'to set weight on'; 容貌 speaks of the whole person; 暴 is coarse and fierce, 慢 unrestrained; 信 is 'true, real' — a face set right and close to the truth, not a put-on gravity (非色莊); 辭 is words, 氣 the voice; 鄙 'common, vulgar'; 倍 is 背 'to turn one's back on' (reason). He reads 遠 and 近 in the departing tone (遠近並去聲), the verbs 'to keep far off' and 'to come near'; modern practice reads the verb 遠 yuǎn like the adjective, and we give that. 籩 biān is a bamboo dish, 豆 a wooden one (Zhu Xi: 籩竹豆，豆木豆) — the vessels of the sacrifices, standing for the counted details of the rites; 有司 'there are officers', i.e. the officers in charge. Zhu Xi: the Way is present everywhere, but the gentleman sets his weight on these three, the essentials of cultivating oneself and the root of government, to be held and examined without lapse even in haste or in ruin (造次顛沛, 4.5); the vessels belong to the Way too, but their place is the officers' charge. He quotes Master Cheng: these three correct oneself and seek nothing outside, hence 'for the vessels there are officers'; and Yin Tun: what is nourished within shows without — Master Zeng took cultivating oneself as the root of government. He Yan's Zheng Xuan reads the line the other way: he takes this 'Way' to be the rites and the results to be in others — move with dignity, and others will not dare to be harsh or insolent to you; keep a grave face, and they will not dare deceive you; speak smoothly, and no ugly, perverse words will reach your ears. Bao Xian: Jingzi neglected the great and attended to the small, so Master Zeng warned him with this. Variant: He Yan's text reads 君子所貴道者三, without 乎; the sense is unchanged."),
# ---------------- 8.5 ----------------
dict(pas="8.5", w="曾子=zēng zǐ/Master Zeng | 曰：「/said | ^以/with, being | 能/able | 問/asking | 於/of | 不/(those) not | 能，/able | ^以/with, having | 多/much | 問/asking | 於/of | 寡；/(those with) little | ^有/having | 若/as if | 無，/without | ^實=shí/full | 若/as if | 虚；/empty | ^犯/offended against | 而/yet | 不/not | 校，=jiào/keeping count, settling scores | ^昔=xī/formerly | 者/(time marker) | 吾/my | 友/friend | 嘗/once | 從=cóng/applied (himself) | 事/(to the) work | 於/in | 斯/these | 矣。」/(it was so)",
  l="Master Zeng said: “Able, and asking of the unable;\nhaving much, and asking of those with little;\nhaving, as though without;\nfull, as though empty;\nwronged, and keeping no tally —\nonce I had a friend who gave himself to these.”",
  i="Master Zeng said: “To have ability and still put questions to those who lack it; to know much and still ask those who know little; to have plenty and carry himself as though he had none, to be full and carry himself as though empty; to be wronged and never keep a score — there was a friend of mine, long ago, who worked at just these things.”",
  n="A run of phrases with no subject, each a way of acting, and the last line sums them up as 斯 'these'. 以能問於不能 'with ability, to ask of the unable': 以 'with, having', 問於 'to ask of'. 實 shí 'solid, full', against 虚 xū 'empty' (虚 is the edition's form). 校 jiào — Zhu Xi: 計校, to reckon up, keep accounts; He Yan's Bao Xian: 報也, to pay back — wronged, he does not retaliate. 昔者 'in former times'; 嘗 'once'; 從事於斯 'to follow the work of these things'. The friend, Zhu Xi agrees with Ma Rong, is Yan Yuan: his heart knew only that what is right has no end, and saw no gap between himself and others, so he could do this. Zhu Xi quotes Xie Liangzuo: not to know that the surplus is in oneself and the lack in others, not to insist that gain must be one's own and loss another's — only one who is close to having no self can do it."),
# ---------------- 8.6 ----------------
dict(pas="8.6", w="曾子=zēng zǐ/Master Zeng | 曰：「/said | ^可/(one who) can | 以/(be) used to | 託=tuō/be entrusted with | 六尺=liù chǐ/six chi tall: still a boy//six//a chi (a measure of length) | 之/(of) | 孤，/an orphan (prince) | ^可/(one who) can | 以/(be) used to | 寄=jì/be given charge of | 百里=bǎi lǐ/a hundred li (square): a state//hundred//a li (a measure of distance) | 之/'s | 命，/commands | ^臨/facing | 大/the great | 節/crisis, test (of integrity) | 而/and | 不/cannot | 可/be | 奪=duó/wrested away | 也，/(assertion) | ^君子/a gentleman | 人/man | 與？=yú/(is he)? | ^君子/a gentleman | 人/man | 也。」/(he is)",
  l="Master Zeng said: “One who can be entrusted with an orphan of six chi,\nwho can be given charge of the commands of a hundred li,\nwho, facing the great crisis, cannot be wrested away —\na gentleman, is he?\nA gentleman he is.”",
  i="Master Zeng said: “A man you could trust with a fatherless young lord, a man you could leave in charge of a whole state, a man nothing could prise loose when life and death are at stake — would you call him a gentleman? That is just what he is.”",
  n="可以託 'can be entrusted with': 可以 + verb is passive in sense here, 'one to whom … can be entrusted'. 託 tuō and 寄 jì both mean 'to put in someone's keeping'. 六尺之孤 'an orphan of six chi' (尺, a measure of length): a ruler's son who is still a boy — He Yan's Kong Anguo: 'a young lord' (幼少之君). 百里之命 'the commands of a hundred li', a state of that size — Zhu Xi: his talent is such that he could assist a young lord and act for him in the government of the state; Kong Anguo: to act for the lord in his government and orders. 臨大節而不可奪 — Zhu Xi: his integrity (節) holds even at the meeting of life and death and cannot be taken from him; He Yan's commentary: the great crisis is to keep the state safe and the altars of the land secure, and 奪 is 'to be toppled'. 與 yú is the question particle (Zhu Xi: 平聲): the line asks 'a gentleman, is he?' and answers with 也 'he is'. Zhu Xi: 與 is a word of doubt, 也 a word of decision; setting it as question and answer makes the certainty stand out. He quotes Master Cheng: with integrity like this, he may be called a gentleman."),
# ---------------- 8.7 ----------------
dict(pas="8.7", w="曾子=zēng zǐ/Master Zeng | 曰：「/said | ^士/an officer | 不/(it) will not | 可/do | 以/for (him) | 不/not (to be) | 𢎞=hóng/broad (the edition's form of 弘) | 毅，=yì/(and) resolute | ^任=rèn/(his) charge, load | 重=zhòng/(is) heavy | 而/and | 道=dào/(his) road | 遠。」=yuǎn/(is) far",
  l="Master Zeng said: “An officer must not fail to be broad and resolute:\nhis charge is heavy, and his road far.”",
  i="Master Zeng said: “A man who would serve must have breadth and staying power, for what he takes on is a heavy weight, and the way he must carry it is far.”",
  n="士 shì, the officer, the man of service who aims at the Way (as 4.9). 不可以不 'cannot do without being' — two negatives make 'must'. 𢎞 hóng is the edition's form of 弘 (He Yan's text writes 弘). Zhu Xi: 𢎞 is broad and wide (寬廣), 毅 strong and enduring (强忍); without breadth he cannot carry the weight, without resolve he cannot reach the end of the road. He Yan's Bao Xian: 弘 'great', 毅 'strong and able to decide'; only so can a man shoulder a heavy charge and go a long road. 任 rèn is 'a load, a charge'; 重 zhòng 'heavy'; 道 dào here is the road itself."),
dict(w="仁/humaneness | 以/(he) takes | 為=wéi/as | 己/his own | 任，=rèn/charge | ^不/is (it) not | 亦/indeed | 重=zhòng/heavy | 乎？/(question) | ^死/(he) dies | 而/and | 後/(only) then | 已，/leaves off | ^不/is (it) not | 亦/indeed | 遠=yuǎn/far | 乎？/(question)",
  l="Humaneness he takes as his own charge —\nis that not heavy indeed?\nDying, and only then leaving off —\nis that not far indeed?",
  i="Humaneness is the load he has taken on as his own — what could weigh more? He may set it down only when he dies — what road could be longer?",
  n="Master Zeng's words run on; the commentary has broken them. 仁以為己任 is 以仁為己任 'to take humaneness as one's own charge', with the object 仁 brought to the front for weight; 為 wéi 'to count as'. 不亦…乎 'is it not indeed…?' (1.1). 死而後已 'die and only then leave off'. Zhu Xi: humaneness is the whole virtue of the human heart, and to insist on embodying it in one's own person and practising it with all one's strength — that is heavy; while a single breath remains this resolve allows no slackening — that is far. He quotes Master Cheng: broad but not resolute, a man has no rule and can hardly stand; resolute but not broad, he is cramped and mean and has no room to dwell in it; and again: be broad and great, then resolute, and one can bear the heavy charge and reach far. He Yan's Kong Anguo: taking humaneness as one's charge, no charge is heavier; stopping only at death, no road is longer."),
# ---------------- 8.8 ----------------
dict(pas="8.8", w="子/the Master | 曰：/said | ^興=xīng/(one is) roused, stirred to rise | 於《/by | 詩》，/the Odes",
  l="The Master said: One is roused by the Odes,",
  i="The Master said: A man is stirred to life by the Odes,",
  n="Three clauses of one build, verb + 於 'by, in' + the source; Zhu Xi interrupts after each and reads them as the stages of a learner's whole life. 興 xīng is 'to rise, be stirred' (Zhu Xi: 起也; He Yan's Bao Xian the same). Zhu Xi: the Odes are rooted in men's nature and feelings, some crooked and some straight; their words are easy to understand, and chanting them, with their rise and fall and repetition, moves people and easily goes in; so it is in the Odes that the beginner is stirred to love the good and hate the bad and cannot stop himself. Bao Xian: in cultivating oneself one should first study the Odes."),
dict(w="^立/(one) stands firm | 於/by | 禮，/the rites",
  l="stands firm by the rites,",
  i="steadied on his feet by the rites,",
  n="立 'to stand, to be established' (as 2.4 三十而立). Zhu Xi: the rites have courtesy, reverence and yielding as their root and a full array of measure, form and number; they can bind fast the joints of a man's flesh and the sinews of his frame; so it is in the rites that the learner, midway, comes to stand on his own and not be shaken or swept off by things. He Yan's Bao Xian: the rites are that by which one stands."),
dict(w="^成/(one is) made complete | 於/by | 樂。=yuè/music",
  l="and is made complete by music.",
  i="and made whole by music.",
  n="樂 here is yuè, 'music'. Zhu Xi: music has the five notes and twelve pitch-pipes, singing in turn and answering one another, to give the measure of song and dance on the eight kinds of instrument; it can nourish a man's nature and feelings, wash away what is crooked and foul and melt the dregs; so it is in music that the learner, at the end, reaches the point where what is right is refined and humaneness ripe, and he is of himself in tune with the Way and virtue — learning completed. He notes that the Neize chapter of the Record of Rites has a boy learn the manners of the young at ten, music and the reciting of Odes at thirteen, and the rites only at twenty; so the three here are not the order of a child's first lessons but the order, ease and depth of what is gained over a lifetime of greater learning. He quotes Master Cheng: the world does not lack men of fine talent, but because the learning of the Way is not clear, it comes to nothing; the Odes of the ancients were like the songs of today, which even village children heard and understood, so they were roused — now even old masters cannot make out their meaning; the ancients had rites for everything, from sweeping and answering to capping, marriage, mourning and sacrifice — now all are ruined; ancient music nourished the ear with its sounds, the eye with its colours, the nature with its songs, the blood with its dances — now none of it is left; so in antiquity men were easily made, and now with difficulty. He Yan's Kong Anguo: music is that by which one's nature is completed."),
# ---------------- 8.9 ----------------
dict(pas="8.9", w="子/the Master | 曰：「/said | ^民/the people | 可/can | 使/be made | 由/to go by | 之，/it | ^不/(they) cannot | 可/(be) | 使/made | 知=zhī/to know | 之。」/it",
  l="The Master said: “The people can be brought to go by it;\nthey cannot be brought to know it.”",
  i="The Master said: “You can get the people to walk the road; you cannot get them to see why it runs where it does.”",
  n="可使 'can be made to': 使 is 'to cause'; 之 'it' is the Way, the right course. 由 is 'to go by, to follow' (He Yan's commentary: 用也, 'to use'). Zhu Xi: the people can be made to follow what principle makes right, but not made to know why it is so. He quotes Master Cheng: it is not that the sage does not wish every house to understand and every door to be enlightened; he simply cannot make them know, only make them follow. To say that the sage would not let the people know would turn it into the trick of 'four in the morning and three at night' (the monkey-keeper's ruse in the Zhuangzi) — how could that be the sage's heart? 可 is 'can', then, not 'may'. He Yan's commentary: they can be made to use it but not to know it — the common people use it every day and do not know it."),
# ---------------- 8.10 ----------------
dict(pas="8.10", w="子/the Master | 曰：「/said | ^好=hào/loving | 勇/courage | 疾/(and) chafing at | 貧，/poverty — | ^亂/disorder | 也。/(that is) | ^人/a man | 而/and yet | 不/not | 仁，/humane — | ^疾/hating | 之/him | 已/too | 甚，/much — | ^亂/disorder | 也。」/(that is)",
  l="The Master said: “Loving courage and chafing at poverty —\nthat makes for disorder.\nA man who is not humane:\nhate him too much,\nand that makes for disorder.”",
  i="The Master said: “A love of daring that cannot bear being poor ends in trouble. Hate a man who lacks humaneness too fiercely, and that too ends in trouble.”",
  n="好 is hào 'to love' (Zhu Xi: 去聲). 疾 is 'to be sick of, to hate': first of one's own poverty, then 疾之 of the inhumane man. 人而不仁 'a man, and yet not humane' (as 3.3). 已 'too, excessively'; 已甚 'too much'. 亂也 'it is disorder', i.e. it leads to disorder. Zhu Xi: one who loves courage and is not content with his lot will surely rise in revolt; one who hates the inhumane man and leaves him no place to stand will surely bring revolt on; the two hearts differ, one bad and one good, but they breed disorder alike. He Yan's Bao Xian: a man who loves courage and is galled by his own poverty and low station will surely make disorder; Kong Anguo: hating him too much also drives him to disorder."),
]

# ---------------------------------------------------------------------------------------------
# FOR THE GLOSSER — keys used in 8.1–8.10 that are NOT yet in glossary_seed.GLOSS
# (reading — sense(s) used here; Zhu Xi's gloss where he gives one)
#
# Bound names and compounds:
#   泰伯    tài bó — Taibo: eldest son of the Great King (大王) of Zhou, who yielded the succession to Jili and fled south (8.1)
#   孟敬子  mèng jìng zǐ — Meng Jingzi: Zhongsun Jie 仲孫捷, a grandee of Lu (Zhu Xi: 魯大夫仲孫氏名捷; Ma Rong) (8.4)
#   故舊    gù jiù — old friends, associates of long standing (8.2)
#   戰戰    zhàn zhàn — trembling, in dread (Zhu Xi: 恐懼) (8.3)
#   兢兢    jīng jīng — wary, on guard (Zhu Xi: 戒謹) (8.3)
#   容貌    róng mào — bearing and looks: the whole person (Zhu Xi: 舉一身而言) (8.4)
#   顏色    yán sè — the countenance, the expression of the face (8.4)
#   辭氣    cí qì — words and tone of voice (Zhu Xi: 辭，言語；氣，聲氣) (8.4)
#   籩豆    biān dòu — the bamboo and wooden dishes of the sacrifices; the counted details of the rites (8.4)
#   有司    yǒu sī — the officers in charge, the responsible officials (8.4)
#   六尺    liù chǐ — six chi (Zhou feet) tall: a boy not yet grown; 六尺之孤 a young orphaned lord (Kong Anguo) (8.6)
#   百里    bǎi lǐ — a hundred li (square): a state of that size (8.6)
#
# Characters:
#   稱 chēng — to praise, to name (8.1)      [POLY: chèn 'to fit']
#   葸 xǐ — fearful, timid (Zhu Xi: 絲里反，畏懼貌) (8.2)
#   絞 jiǎo — to twist tight; sharp, cutting (Zhu Xi: 古卯反，急切也; Ma Rong: 絞刺) (8.2)
#   篤 dǔ — solid, earnest, devoted (8.2)
#   興 xīng — to rise, be stirred (Zhu Xi: 起也) (8.2, 8.8)      [POLY: xìng 'mood, evocation']
#   遺 yí — to leave behind, to forget, cast off (8.2)
#   偷 tōu — thin, mean, cold-hearted (Zhu Xi: 薄也); to steal (8.2)
#   召 zhào — to summon, to call (8.3)      [POLY: shào, a place/surname]
#   兢 jīng — cautious, wary (兢兢) (8.3)
#   深 shēn — deep (8.3)
#   履 lǚ — to tread on (8.3)
#   薄 bó — thin (8.3)      [POLY: báo, bò]
#   冰 bīng — ice (8.3)
#   鳥 niǎo — a bird (8.4)
#   鳴 míng — to cry, call (of a bird) (8.4)
#   貌 mào — looks, outward appearance (容貌) (8.4)
#   慢 màn — insolent, unrestrained (Zhu Xi: 放肆也) (8.4)
#   氣 qì — breath; the voice, tone (辭氣; Zhu Xi: 聲氣也) (8.4)
#   鄙 bǐ — common, crude, vulgar (Zhu Xi: 凡陋也) (8.4)
#   倍 bèi — = 背, to turn one's back on, go against (reason) (Zhu Xi: 倍與背同，謂背理也); double (8.4)
#   籩 biān — a bamboo dish used in sacrifices (Zhu Xi: 竹豆) (8.4)
#   豆 dòu — a wooden dish on a stem, a sacrificial vessel (Zhu Xi: 木豆) (8.4)
#   存 cún — to be there, be present; to keep (8.4)
#   實 shí — solid, full; real, true (8.5)
#   校 jiào — to reckon up, keep accounts (Zhu Xi: 計校); to retaliate (Bao Xian: 報也) (8.5)   [POLY: xiào 'school']
#   昔 xī — formerly, in the past (昔者) (8.5)
#   託 tuō — to entrust, put in someone's keeping (8.6)
#   尺 chǐ — a chi, the Zhou foot (8.6)
#   寄 jì — to commit, give into someone's charge (8.6)
#   奪 duó — to take away by force, to wrest (8.6)
#   𢎞 hóng — = 弘 (the edition's form): broad, wide (Zhu Xi: 寛廣也) (8.7)
#   毅 yì — resolute, enduring (Zhu Xi: 强忍也) (8.7)
#   任 rèn — a load, a charge, a responsibility (8.7)      [POLY: rén, a surname]
#
# Broaden by addition (sense used here):
#   節  jié — integrity; a crisis, a test of integrity (大節, 8.6; Zhu Xi: 其節至於死生之際)
#   疾  jí — to hate, to chafe at (8.10 疾貧, 疾之)
#   道  dào — a road (8.7 任重而道遠)
#   免  miǎn — to come through unharmed (8.3, Zhu Xi: 得免於毁傷)
#   已  yǐ — too, excessively (8.10 已甚)
#   啓  qǐ — to open, uncover (8.3 啓予足, Zhu Xi: 開也)
#   予  yú — my (8.3 啓予足)
#   由  yóu — to go by, to use (8.9; He Yan: 用也)
#   臨  lín — to look down into, to stand at the edge of (8.3 臨深淵); to face (8.6 臨大節)
#   淵  yuān — a deep pool (8.3)
#   百  bǎi, 里  lǐ — in 百里, a li as a measure of distance (8.6)
