# Analects Book 14 (憲問) — draft, third part: lemmata 49–74 = passages 14.34–14.47 (UNITS_C[0] is lemma 49).
# Lemma 75 (論語卷七) is the running head that closes the juan, not text; the build skips it.
# Token format as the pilot:
#   tokens separated by " | "; a token is  CHARS[PUNCT][=pinyin][/context gloss[//char gloss//char gloss]]
#   a leading "^" breaks the verse line before the token.
# Punctuation is editorial (the edition has none) and always trails the word before it.
# Pinyin defaults to the glossary's first reading; every polyphone states its reading here, and so does
# every bound compound and every character not yet in the glossary (on every occurrence).
# Passages follow Zhu Xi's chapter breaks (胡氏: 凡四十七章): 14.34 = units 49–50, 14.35 = 51, 14.36 = 52–54,
# 14.37 = 55–56, 14.38 = 57–58, 14.39 = 59–62, 14.40 = 63, 14.41 = 64, 14.42 = 65–67, 14.43 = 68–69,
# 14.44 = 70, 14.45 = 71, 14.46 = 72, 14.47 = 73–74. Each stretch holds one chapter (no npas). 14.40
# (子曰作者七人矣) is its own chapter: the transcription lost the ○ before it, but Zhu Xi comments on it apart
# (李氏曰), and the note says so.
# Quotation marks balance within every unit. Where a speech runs on past one of Zhu Xi's comments (14.36 unit
# 54, the Master; 14.39 units 60–62, the Master) the continuation is left unquoted, Chinese and English alike
# (as Books 8–13). The Documents' words in unit 68 sit inside Zizhang's question (《書》云：『…』, ‘…’), as
# 2.21. The two lines of the Ode (衛風·匏有苦葉) that the basket-carrier recites at the end of unit 66 carry
# no marks of their own, as the Ode lines of 12.10 and the Changes line of 13.22.
# Repeats (shipped English reused): 堯舜其猶病諸 (71) l 'Even Yao and Shun still felt themselves short in this'
#   / i 'Even Yao and Shun felt they fell short in this' (6.28; 堯 | 舜 unbound, as there); 上好禮 (70)
#   'those above love the rites' (13.4); 微生 the surname, as 微生髙 Weisheng Gao (5.23); 佞 'glib(ness)'
#   (5.4, 11.24); 硜硜 'clinking hard like pebbles' (13.20); 果 'resolute, carried through' (13.20 行必果);
#   童子 'a boy' (7.28); 先生 'the elders' (2.8); 百姓 'the hundred clans' (12.9); 達 'to get through' (12.20,
#   13.5, 13.17); 欲速 'want speed' (13.17); 色斯舉 cited as 10.18; 何謂也 'what is meant?'; 孔子 'Kongzi'.
# Readings decided:
#   與 yú, final question particle (49, 64, 73: Zhu Xi 與平聲; 58 ×2, Zhu Xi 與平聲); 與 yǔ 'with' (74);
#   為 wèi in 何為 'why' (49, 56); 為 wéi (49 為佞, 50 為佞, 64 為之, 72 是為賊); 栖栖 xī xī (49; Zhu Xi 依依也);
#   佞 nìng; 疾 jí 'to hate' (50; Zhu Xi 疾惡也); 稱 chēng (51 ×2); 驥 jì; 報 bào (52–54); 夫 fú (55; 音扶);
#   夫 fū in 夫子 (57, meaning Jisun: Zhu Xi 夫子指季孫); 知 zhī (55, 56 ×2, 64, 66); 愬 sù (57); 肆 sì
#   (57); 朝 cháo (57; 朝音潮); 將 jiāng (58 ×2; 73 將命 'to carry messages'); 行 xíng (58, 74); 辟 bì =
#   避 'to avoid' (59–62; Zhu Xi 辟去聲, the reading of 避); 宿 sù (64); 擊 jī; 磬 qìng; 荷 hè (65; Zhu Xi
#   荷去聲 'to carry on the shoulder'); 蕢 kuì; 己 jǐ in 莫己知 (66; Zhu Xi 莫已之已音紀), 已 yǐ in 斯已而已矣
#   (餘音以); 厲 lì; 淺 qiǎn; 掲 qì (66; 起例反); 難 nán (67); 諒隂 liáng ān (68, by the traditional reading of
#   the mourning term, also written 諒闇/亮陰; Zhu Xi gives no sound and says 未詳其義); 薨 hōng; 總 zǒng;
#   己 jǐ (69); 冢 zhǒng; 聽 tīng; 好 hào, 易 yì (70; 好易皆去聲); 脩 xiū (71 ×5); 幼 yòu; 孫 xùn, 弟 tì
#   (72; 孫弟並去聲); 長 zhǎng (72; 上聲); 叩 kòu (72; Zhu Xi 叩音口, modern kòu, as the glossary); 脛 jìng
#   (72; 其定反); 闕 què in 闕黨 (73); 見 jiàn (74 ×2); 並 bìng (74).
# Glyphs kept as printed: 徳 (51–54), 栖 (49), 隂 (68), 髙 (68, 69), 掲 (66), 脩 (71).
# Bound (keys exist): 孔子, 子貢, 子路, 子張, 夫子, 何如, 硜硜, 君子, 百姓, 童子, 先生.
# New bound keys needed (names and compounds bound here):
#   微生畝 (wēi shēng mǔ — Weisheng Mu: a man of Lu (?) who called the Master by his personal name; Zhu Xi
#     微生姓畝名也…葢有齒徳而隠者 'probably an old recluse of age and virtue'; Bao Xian in He Yan 微生姓也畝名也);
#   栖栖 (xī xī — restless, clinging on, unable to settle; Zhu Xi 栖栖依依也);
#   公伯寮 (gōng bó liáo — Gongbo Liao: a man of Lu (Zhu Xi 魯人) who denounced Zilu to the Jisun; Ma Rong in
#     He Yan: 魯人弟子也, a disciple);
#   季孫 (jì sūn — Jisun: the head of the Ji house of Lu, the Ji clan by its full name; cf. 季氏, 孟孫);
#   子服景伯 (zǐ fú jǐng bó — Zifu Jingbo: Zifu He 子服何, grandee of Lu; Zhu Xi 子服氏景諡伯字; Ma Rong 子服何忌);
#   石門 (shí mén — Shimen, 'the Stone Gate': a place name, Zhu Xi 地名);
#   晨門 (chén mén — the morning gatekeeper: Zhu Xi 掌晨啟門, a worthy hidden in the post of gatekeeper; He Yan
#     晨門者閽人也);
#   孔氏 (kǒng shì — the Kong house: Kongzi and his household, as 管氏);
#   髙宗 (gāo zōng — Gaozong: King Wuding 武丁 of Shang; Zhu Xi 商王武丁也; Kong Anguo 殷之中興王武丁也);
#   諒隂 (liáng ān — the royal mourning seclusion: Zhu Xi 天子居喪之名未詳其義; Kong Anguo 諒信也隂猶默也);
#   冢宰 (zhǒng zǎi — the Chief Steward: Zhu Xi 冢宰大宰也; Kong Anguo 天官佐王治者);
#   原壤 (yuán rǎng — Yuan Rang: an old friend of Kongzi's; Zhu Xi 孔子之故人母死而歌葢老氏之流; Ma Rong 魯人孔子故舊);
#   闕黨 (què dǎng — Que village, the name of a 黨 community; Zhu Xi 闕黨黨名).
# New single characters needed (not yet GLOSS keys), with the sense used here:
#   畝 mǔ (Mu, a personal name; a mu of land), 栖 xī (in 栖栖; = 棲 'to roost, perch'), 驥 jì (a thoroughbred,
#   Zhu Xi 善馬之名), 報 bào (to repay, to answer), 寮 liáo (Liao, in 公伯寮), 肆 sì (to lay out a corpse in
#   public, Zhu Xi 陳尸也), 石 shí (stone), 晨 chén (morning, dawn), 擊 jī (to strike), 磬 qìng (a chime-stone,
#   Zhu Xi 樂器), 荷 hè (to carry on the shoulder, Zhu Xi 擔也; 去聲), 蕢 kuì (a straw basket, Zhu Xi 草器也),
#   淺 qiǎn (shallow), 掲 qì (to hitch up one's clothes to wade, Zhu Xi 攝衣涉水曰掲; 起例反), 諒 liáng (in 諒隂;
#   elsewhere liàng 'truly', Kong Anguo 信也), 隂 ān (in 諒隂; the edition's form of 陰, otherwise yīn), 薨 hōng
#   (the death of a lord), 總 zǒng (to gather up, Zhu Xi 總攝), 冢 zhǒng (great, chief, in 冢宰), 壤 rǎng (Rang,
#   in 原壤), 幼 yòu (young), 脛 jìng (the shin, Zhu Xi 足骨也; 其定反), 並 bìng (side by side, abreast).
# Existing entries that need broadening (for the glosser): 夷 ('to squat', Zhu Xi 夷蹲踞也; Ma Rong 踞也);
#   疾 ('to hate', Zhu Xi 疾惡也, 14.34); 固 ('obstinacy, holding to one thing', Zhu Xi 執一而不通); 徳
#   ('of a horse, good training and temper', Zhu Xi 調良; 'a kindness, a favour', Zhu Xi on 14.36 恩惠);
#   尤 ('to blame', 不尤人); 惑 (惑志 'a mind led astray'); 作 ('to rise and go off', 李氏 作起也); 次 ('the
#   next', 其次); 辟 (bì = 避 'to avoid', Zhu Xi 去聲, 14.39); 自 ('from where?', 奚自; Zhu Xi 自従也); 厲 ('to
#   wade through water in one's clothes', Zhu Xi 以衣涉水曰厲); 果 ('resolute in', Zhu Xi 果於忘世); 末 (already
#   'no'); 述 ('to be spoken of, praiseworthy', Zhu Xi 述猶稱也); 賊 ('one who harms others', Zhu Xi 賊者害人之名);
#   將 (將命 'to carry messages', Zhu Xi 傳賓主之言); 益 ('to advance, make progress', 求益); 孫 (xùn, already);
#   聽 ('to take orders from', 聽於冢宰); 官 (百官 'the hundred offices').
# Not bound, meaning what their parts mean: 何 | 為, 無 | 乃, 為 | 佞, 報 | 怨, 下 | 學, 上 | 達, 市 | 朝,
#   賢 | 者, 其 | 次, 作 | 者, 荷 | 蕢, 擊 | 磬, 既 | 而, 而 | 已 | 矣, 何 | 必, 百 | 官, 堯 | 舜 (as 6.28), 孫 |
#   弟, 將 | 命, 速 | 成, 並 | 行.
# Collation (Ruan 1816 KR1h0004 agrees with Zhu Xi after graphic normalisation, and reads 莫己知 and 總己).
#   He Yan SBCK (KR1h0005), noted in the unit: 50 孔子對曰; 57 惑志於公伯寮也; 59–62 避 for 辟; 64 石門石門晨門
#   (likely dittography); 65 荷簣, 孔子之門; 67 未之難矣; 71 脩己以敬人; 73 將命矣; 74 踞於位. Not noted
#   (graphic): 畒, 德, 丗, 巳 (for 己/已), 鲁, 緫, 聴, 䘮, 㓜, 遜悌 (= 孫弟), 賔, 将.
# Misprints (owner's rule 5b, in emend.json): unit 66 — the print has 莫已知; the text reads 莫己知 (Zhu Xi
#   莫已之已音紀); unit 69 — the print has 總已; the text reads 總己 (Zhu Xi 總己謂總攝己職). Each note opens
#   "The print has X, a misprint for Y, corrected here."

UNITS_C = [
# ---------------- 14.34 ----------------
dict(pas="14.34", w="微生畝=wēi shēng mǔ/Weisheng Mu//Wei- (微生, a two-character surname)//-sheng (of the surname)//Mu (his personal name) | 謂/said to | 孔子=kǒng zǐ/Kongzi | 曰：「/saying | ^丘，/Qiu | 何/why | 為=wèi/for | 是/this | 栖栖=xī xī/clinging and restless//to perch, roost//to perch, roost | 者/one | 與？=yú/(question) | ^無/is it not | 乃/rather | 為=wéi/practising | 佞=nìng/glibness | 乎？」/(question)",
  l="Weisheng Mu said to Kongzi, saying: “Qiu, why are you this clinging, restless one?\nIs it not rather that you practise glibness?”",
  i="Weisheng Mu said to Kongzi: “Qiu, what keeps you hanging on everywhere, never at rest? Is it not that you make a trade of a clever tongue?”",
  n="微生畝 Weisheng Mu: Zhu Xi says 微生 is the surname (as Weisheng Gao, 5.23) and 畝 the personal name; he calls the Master by his personal name, 丘 Qiu, and his words are very haughty, so he was probably a recluse of age and virtue (葢有齒徳而隠者). Bao Xian in He Yan gives only surname and name. 何為 'for what, why': 為 is wèi. 是栖栖者 'this restless one': 是 'this, such', 者 makes 栖栖 a person. 栖栖 xī xī (栖 = 棲 'to perch') Zhu Xi glosses 依依 'clinging, hanging on'. 無乃…乎 'is it not rather…?'. 與 is the question particle yú (Zhu Xi: 與平聲). 為佞 'to practise glibness' (為 wéi): Zhu Xi, that he makes a business of a ready tongue to please people (務為口給以悦人)."),
dict(w="孔子=kǒng zǐ/Kongzi | 曰：「/said | ^非/(it is) not (that I) | 敢/dare | 為=wéi/practise | 佞=nìng/glibness | 也，/(assertion) | ^疾=jí/(I) hate | 固/obstinacy | 也。」/(assertion)",
  l="Kongzi said: “It is not that I dare practise glibness;\nI hate obstinacy.”",
  i="Kongzi said: “I would not presume to be a smooth talker. It is stubbornness I cannot abide.”",
  n="非…也 'it is not that…', answered by a second 也 clause giving the real reason. 疾 jí is 'to hate' here (Zhu Xi: 疾，惡也), not 'illness'. 固 'obstinacy': Zhu Xi, holding to one thing and not getting through (執一而不通). He reads the reply as a warning to Mu himself: the sage, toward one honoured for age, is respectful in manner and straight in speech, and his warning to him is a deep one (聖人之於達尊禮恭而言直如此其警之亦深矣). Bao Xian in He Yan takes the obstinacy to be the world's: 'I chafe at the age's narrow obstinacy, and wish to put the Way in practice to change people' (疾丗固陋欲行道以化人也). Variant: He Yan's text reads 孔子對曰 'Kongzi answered', the word for replying to an elder or superior."),
# ---------------- 14.35 ----------------
dict(pas="14.35", w="子/the Master | 曰：「/said | ^驥=jì/a thoroughbred | 不/is not | 稱=chēng/praised (for) | 其/its | 力，/strength; | ^稱=chēng/(it is) praised (for) | 其/its | 徳/virtue | 也。」/(assertion)",
  l="The Master said: “A thoroughbred is not praised for its strength;\nit is praised for its virtue.”",
  i="The Master said: “What people praise in a fine horse is not its strength but its virtue — its good training and temper.”",
  n="驥 jì is the name for a fine horse (Zhu Xi: 善馬之名). 稱 chēng 'to praise, to speak of'. A horse's 徳 'virtue' (徳 is the edition's form of 德) is, Zhu Xi says, its being well trained and good-tempered (調良); Zheng Xuan in He Yan says the same (德者謂調良之德也). Zhu Xi quotes Yin Tun: though a thoroughbred has strength, what it is praised for is its virtue; if a man has talent and no virtue, what is there in him worth esteeming? (人有才而無徳則亦奚足尚哉)."),
# ---------------- 14.36 ----------------
dict(pas="14.36", w="或/someone | 曰：「/said | ^以/(by) using | 徳/virtue | 報=bào/to repay | 怨，/resentment — | 何如？」=hé rú/how is it",
  l="Someone said: “Repaying resentment with virtue — how is it?”",
  i="Someone said: “What do you say to answering a grudge with kindness?”",
  n="以徳報怨 'with virtue to repay resentment': 以 'by means of' comes first, then the verb 報 bào 'to repay, to answer' and its object 怨 'resentment, a grudge' — the wrong someone has done one. Zhu Xi: this was a saying people quoted, now found in the book of Laozi (或人所稱今見老子書; Daodejing 63 has 報怨以德); here 徳 means a kindness done, a favour (徳謂恩惠也), and the i says 'kindness' for it. 何如 'how is it?' (1.15)."),
dict(w="子/the Master | 曰：「/said | ^何/what | 以/with | 報=bào/(would one) repay | 徳？」/virtue",
  l="The Master said: “Then with what does one repay virtue?”",
  i="The Master said: “Then what would you answer kindness with?”",
  n="何以 'with what': the question word 何 stands before 以, as an interrogative object of a preposition does. Zhu Xi: if one has already repaid with kindness those one resents, what is left to repay those who have done one kindness? The Master's answer runs on past Zhu Xi's comment; the next unit is left unquoted."),
dict(w="^以/with | 直/straightness | 報=bào/repay | 怨，/resentment; | ^以/with | 徳/virtue | 報=bào/repay | 徳。/virtue",
  l="With straightness repay resentment;\nwith virtue repay virtue.",
  i="Answer a grudge with fair and straight dealing; a kindness done you, answer in kind.",
  n="Two lines of one shape, 以 X 報 Y. 直 'straight' is Zhu Xi's key word: toward the one he resents, a man's love and dislike, his taking and refusing, are all ruled by perfect fairness with nothing private in it — that is 'straightness' (愛憎取舍一以至公而無私所謂直也); toward one who has done him kindness he must repay kindness and never forget it. The questioner's saying, he goes on, may be called generous, but seen beside the sage's it comes from a private intention, and both repayments lose their balance; only the Master's way gives each its due — and since resentment is not avenged while every kindness is repaid, it too is generous. The words are plain and brief, but their meaning turns and returns, like the workings of nature, simple and easy to know yet endlessly subtle; learners should savour it closely."),
# ---------------- 14.37 ----------------
dict(pas="14.37", w="子/the Master | 曰：「/said | ^莫/no one | 我/me | 知=zhī/knows | 也/(assertion) | 夫！」=fú/(exclamation)",
  l="The Master said: “No one knows me — ah!”",
  i="The Master said: “Ah — not one person knows me for what I am.”",
  n="莫我知 is 莫知我 'no one knows me', with the pronoun object 我 drawn before the verb after the negative 莫 (as 13.15 莫予違). 也夫 a final sigh; 夫 is fú (Zhu Xi: 夫音扶). Zhu Xi: the Master sighs to himself, so as to draw a question from Zigong (夫子自歎以發子貢之問也)."),
dict(w="子貢=zǐ gòng/Zigong | 曰：「/said | ^何/why | 為=wèi/for | 其/is it that | 莫/no one | 知=zhī/knows | 子/you | 也？」/(question) | ^子/the Master | 曰：「/said | ^不/(I) do not | 怨/resent | 天，/Heaven, | 不/do not | 尤/blame | 人；/others; | ^下/below | 學/(I) learn | 而/and | 上/above | 達。/(I) get through | ^知=zhī/knowing | 我/me | 者，/the one | 其/surely | 天/Heaven | 乎！」/(exclamation)",
  l="Zigong said: “Why is it that no one knows you?”\nThe Master said: “I do not resent Heaven, do not blame others;\nI learn below and get through above.\nThe one who knows me — surely it is Heaven!”",
  i="Zigong said: “How can it be that no one understands you?” The Master said: “I bear Heaven no grudge and lay no blame on men. I learn from the things close at hand and work my way through to what is high. If anyone understands me, it must be Heaven.”",
  n="何為其…也 'why is it that…?' (為 wèi); 子 is 'you', addressed to the Master. 尤 'to blame'. 下學而上達: 下 and 上 are 'below' and 'above' used as adverbs — learning in the low, everyday things, getting through to the high ones. Zhu Xi: not finding favour with Heaven, he does not resent Heaven; not fitting with men, he does not blame men; he only knows to learn below and so of itself get through above. This is only his speaking of turning back on himself and cultivating himself step by step, nothing very different from others that would make him known; yet savoured deeply, it holds a mystery men cannot reach and Heaven alone knows. In the Kong school only Zigong's wisdom came near this, so the Master spoke to bring it out — a pity, Zhu Xi adds, that Zigong still did not quite get there. He quotes Master Cheng: 'not resenting Heaven, not blaming others — that is how it ought to be by principle'; 'in learning below and getting through above, the meaning lies beyond the words'; 'learners must hold to the words 下學上達; they are the key to learning.' The comment closes: learning the affairs of men below is itself getting through to the principle of Heaven above, but practise without examining it and one will not get through. In He Yan: its own comment says Zigong, puzzled at the Master's words, asked; Ma Rong — Kongzi, not used by his age, did not resent Heaven, and though men did not know him did not blame them; Kong Anguo — 下學 is learning the affairs of men, 上達 knowing the decree of Heaven above (上知天命); and He Yan's own comment: the sage matches Heaven and Earth in virtue, so he says only Heaven knows him."),
# ---------------- 14.38 ----------------
dict(pas="14.38", w="公伯寮=gōng bó liáo/Gongbo Liao//Gong- (公伯, a two-character surname)//-bo (of the surname)//Liao (his personal name) | 愬=sù/denounced | 子路=zǐ lù/Zilu | 於/to | 季孫。=jì sūn/Jisun | ^子服景伯=zǐ fú jǐng bó/Zifu Jingbo//Zi- (子服, the house name)//-fu (of the house name)//Jing (his posthumous name)//Bo (his courtesy name, 'eldest') | 以/(with it) | 告/reported (it) | 曰：「/saying | ^夫子=fū zǐ/that lord | 固/certainly | 有/has | 惑/a led-astray | 志/mind | 於/over | 公伯寮；=gōng bó liáo/Gongbo Liao | ^吾/my | 力/strength | 猶/still | 能/is able | 肆=sì/to lay out (his body) | 諸/in | 市/the market | 朝。」=cháo/or the court",
  l="Gongbo Liao denounced Zilu to Jisun.\nZifu Jingbo reported it, saying: “That lord certainly has a mind led astray over Gongbo Liao;\nmy strength is still able to lay him out in the market or the court.”",
  i="Gongbo Liao spoke against Zilu to the head of the Ji house. Zifu Jingbo came and told Kongzi of it: “His lordship has certainly let Gongbo Liao lead him astray. But I still have power enough to have the man put to death and his body shown in the market-place or at court.”",
  n="公伯寮 Gongbo Liao was a man of Lu (Zhu Xi: 魯人); Ma Rong in He Yan makes him a disciple. 愬 sù here is to bring a complaint against someone, to slander (Ma Rong: 愬，譖也). 季孫 Jisun is the head of that house, the Ji clan by its full name (季氏, 3.1). 子服景伯 Zifu Jingbo: Zhu Xi — 子服 his house, 景 his posthumous name, 伯 his courtesy name, the Lu grandee Zifu He 子服何 (Ma Rong: 子服何忌). 以告 'reported it' — to Kongzi (Ma Rong). 夫子 here is not the Master but Jisun, 'that lord' (Zhu Xi: 夫子指季孫), who has doubts because of Liao's words. 肆 sì is to lay out a corpse for show (Zhu Xi: 陳尸也): Jingbo means he would have Liao put to death. 諸 = 之於 'him in'. 朝 is cháo 'the court' (Zhu Xi: 朝音潮). Zheng Xuan in He Yan: 'my power can make Jisun see that Zilu is blameless, and have Liao executed and laid out'. Variant: He Yan's text reads 惑志於公伯寮也, adding 也."),
dict(w="子/the Master | 曰：「/said | ^道=dào/the Way's | 之/(clause marker) | 將=jiāng/being about to | 行=xíng/prevail | 也/(pause) | 與，=yú/(is it so?) | 命/(it is) what is decreed | 也；/(assertion) | ^道=dào/the Way's | 之/(clause marker) | 將=jiāng/being about to | 廢/be cast aside | 也/(pause) | 與，=yú/(is it so?) | 命/(it is) what is decreed | 也。/(assertion) | ^公伯寮=gōng bó liáo/Gongbo Liao | 其/how ever (could he) | 如/do about | 命/what is decreed | 何？」/what",
  l="The Master said: “The Way about to prevail — it is what is decreed;\nthe Way about to be cast aside — it is what is decreed.\nGongbo Liao — what could he do about what is decreed?”",
  i="The Master said: “If the Way is to prevail, that is as it is decreed; if the Way is to be cast aside, that too is as it is decreed. What can Gongbo Liao do against that?”",
  n="道之將行 'the Way's being about to prevail': 之 turns the clause into a topic; 將 jiāng 'about to'; 行 xíng 'to go forward, to prevail'; 廢 'to be cast aside'. 也與 closes each topic with a questioning lift — 與 is yú (Zhu Xi: 與平聲) — and 命也 is the answer. 命 'what is decreed', the decree (12.5). 其如…何 'what could he do about…?' (as 7.22, 9.5). Zhu Xi quotes Xie Liangzuo: even if Liao's slander had succeeded, that too would have been decree; in truth Liao could do nothing. And adds in his own voice (愚謂): the Master said this to enlighten Jingbo, settle Zilu and warn Liao; where gain and harm are concerned, the sage does not need to wait for the decree to decide before he is at ease."),
# ---------------- 14.39 ----------------
dict(pas="14.39", w="子/the Master | 曰：「/said | ^賢/the worthy | 者/ones | 辟=bì/avoid | 世。」/the age",
  l="The Master said: “The worthy avoid the age.”",
  i="The Master said: “The worthiest of men withdraw from their age itself.”",
  n="辟 is read bì, the word 'to avoid', later written 避 (Zhu Xi: 辟去聲, and so below); He Yan's text writes 避 throughout this chapter. 賢者 'the worthy'. Zhu Xi: when the world is without the Way they withdraw into hiding, like Boyi (5.22) and the Grand Duke (太公). Kong Anguo in He Yan: no ruler of the age can make them his ministers. The Master's saying runs on past Zhu Xi's comments; the next three units are left unquoted."),
dict(w="^其/the | 次/next | 辟=bì/avoid | 地。/a place",
  l="The next avoid a place.",
  i="Those next to them withdraw from a particular place.",
  n="其次 'the next (after them)', the next grade (13.20). Zhu Xi: they leave a disordered state for a well-ruled one (去亂國適治邦) — Ma Rong in He Yan says the same."),
dict(w="^其/the | 次/next | 辟=bì/avoid | 色。/a look",
  l="The next avoid a look.",
  i="Those next, from a look on a ruler's face.",
  n="色 'the face, the look'. Zhu Xi: when the courtesy of the ruler's manner declines, they go (禮貌衰而去). Kong Anguo in He Yan answers with the words of 10.18, 色斯舉也 (the text there: 色斯舉矣 'at a look, up it rose')."),
dict(w="^其/the | 次/next | 辟=bì/avoid | 言。/a word",
  l="The next avoid a word.",
  i="Those next, from a word.",
  n="Zhu Xi: when there are words at odds with them, then they go (有違言而後去也); Kong Anguo in He Yan: when there are harsh words, they leave. Zhu Xi quotes Master Cheng: though the four are spoken of in order from great to small, there is no better or worse among them; it is only that what each man met was different (所遇不同耳)."),
# ---------------- 14.40 ----------------
dict(pas="14.40", w="子/the Master | 曰：「/said | ^作/(those who have) risen (and gone) | 者/ones | 七/seven | 人/men | 矣。」/(now)",
  l="The Master said: “Those who have risen and gone are seven men now.”",
  i="The Master said: “There are seven men now who have got up and gone.”",
  n="Zhu Xi treats this as a chapter of its own: the transcription has lost the ○ that should stand before it, but he comments on it separately, quoting a Mr Li (李氏): 作 is 'to rise' — those who have risen and gone off into hiding are now seven; who they were cannot be known, and to insist on finding names to fill the number is forcing it (必求其人以實之則鑿矣). Bao Xian in He Yan reads 作 as 為 'to do (this)', and names the seven: Changju and Jieni, the old man with the basket, the gatekeeper of Shimen, the basket-carrier (14.41–42 here), the border warden of Yi (3.24) and the madman of Chu, Jieyu (長沮桀溺丈人石門荷簣儀封人楚狂接與, the print's 與 for 輿)."),
# ---------------- 14.41 ----------------
dict(pas="14.41", w="子路=zǐ lù/Zilu | 宿=sù/lodged for the night | 於/at | 石門。=shí mén/Shimen//stone//gate | ^晨門=chén mén/the morning gatekeeper//morning//gate | 曰：「/said | 奚/where | 自？」/from | ^子路=zǐ lù/Zilu | 曰：「/said | 自/from | 孔氏。」=kǒng shì/the Kong house | ^曰：「/(he) said | 是/(is) this | 知=zhī/knowing | 其/it | 不/(can)not | 可/be done | 而/and (yet) | 為=wéi/sets about | 之/it | 者/the one | 與？」=yú/(question)",
  l="Zilu lodged for the night at Shimen.\nThe morning gatekeeper said: “From where?”\nZilu said: “From the Kong house.”\nHe said: “Is this the one who knows it is impossible and yet sets about it?”",
  i="Zilu spent a night at Shimen. The keeper of the gate, opening it at dawn, asked him: “Where are you from?” “From Master Kong's,” said Zilu. “Is that the man who knows the thing cannot succeed and works at it regardless?”",
  n="宿 sù 'to lodge for the night'. 石門 Shimen, 'Stone Gate', is a place name (Zhu Xi: 地名). 晨門 is the man in charge of opening the gate at dawn (Zhu Xi: 掌晨啟門); Zhu Xi thinks him probably a worthy man hidden in the post of gate-warden (葢賢人隠於抱関者也). He Yan: the 晨門 is a gatekeeper (閽人). 奚自 'from where?': the question word 奚 comes before 自 'from' (Zhu Xi: 自，従也 — asking where he had come from). 孔氏 'the Kong house', the Master and his household (as 管氏, 3.22). 是…者與 'is this the one who…?' (與 yú; Zhu Xi: 與平聲). Zhu Xi quotes Hu Yin: the gatekeeper knew the age could not be set right and so did nothing, and with this he mocked Kongzi; but he did not know that for the sage there is no time when the world cannot be worked on. Bao Xian in He Yan: Kongzi knows the age cannot be set right and forces himself to try. Variant: He Yan's text reads 子路宿於石門石門晨門曰, with 石門 twice — most likely a doubled copying ('the Shimen gatekeeper')."),
# ---------------- 14.42 ----------------
dict(pas="14.42", w="子/the Master | 擊=jī/was striking | 磬=qìng/the chime-stones | 於/in | 衛。/Wei | ^有/there was (one) | 荷=hè/shouldering | 蕢=kuì/a straw basket | 而/and | 過/passing | 孔氏=kǒng shì/the Kong house | 之/'s | 門/gate | 者，/who | ^曰：「/said | ^有/there is | 心/heart (in it) | 哉，/how | 擊=jī/striking | 磬=qìng/the chime-stones | 乎！」/(exclamation)",
  l="The Master was striking the chime-stones in Wei.\nThere was one shouldering a straw basket and passing the gate of the Kong house, who said:\n“There is heart in it — the striking of the chime-stones!”",
  i="The Master was playing the chime-stones in Wei. A man with a straw basket on his shoulder, going past the Master's gate, said: “There is something on his mind, the one who strikes those stones!”",
  n="磬 qìng is a musical instrument (Zhu Xi: 樂器), a set of shaped stones hung on a frame and struck. 擊 jī 'to strike'. 荷 is hè 'to carry on the shoulder' (Zhu Xi: 荷去聲; 荷，擔也); 蕢 kuì a straw basket (草器也). 有…者 'there was one who…', with the whole description between. 有心哉，擊磬乎 'there is heart (in it), the striking of the chime-stones!' — the exclamation first, its subject after. Zhu Xi: the basket-carrier too was a recluse; the sage's heart never forgot the world, and this man heard it in the sound of the stones — so he was no ordinary man. He Yan's comment: 'having heart' means anxious and troubled (契契然). Variants: He Yan's text reads 荷簣 for 荷蕢 (簣 is usually 'a basket for carrying earth', but He Yan's comment glosses it 草器 'a straw basket', as Zhu Xi glosses 蕢, so the difference may be only in the graph), and 孔子之門 'Kongzi's gate' for 孔氏之門."),
dict(w="既/(when it was) done | 而/and then | 曰：「/(he) said | ^鄙/crude | 哉，/how | ^硜硜=kēng kēng/clinking hard like pebbles | 乎！/(exclamation) | ^莫/no one | 己=jǐ/him | 知=zhī/knows | 也，/(assertion) | ^斯/then | 已/(let him) stop | 而/and | 已/that is all | 矣。/(so it is) | ^深/deep — | 則/then | 厲，/wade in your clothes; | ^淺=qiǎn/shallow — | 則/then | 掲。」=qì/hitch them up",
  l="When it was done he said: “Crude indeed,\nclinking hard like pebbles!\nNo one knows him —\nthen let him stop, and that is all.\nDeep, then wade in your clothes;\nshallow, then hitch them up.”",
  i="Then he went on: “How narrow — that hard little clink, clink! If nobody knows him, he should leave off, and there's an end of it. Deep water, wade through in your clothes; shallow water, lift them up.”",
  n="The print has 莫已知, a misprint for 莫己知, corrected here. Zhu Xi's own sound note says so: 'the 已 of 莫已 is read like 紀, the others like 以' (莫已之已音紀餘音以) — it is 己 jǐ 'himself, him', and the two 已 of 斯已而已矣 are yǐ 'to stop'; Ruan Yuan's 1816 text prints 己. 既而 'when it was done, after a while'. 鄙 'crude, mean'. 硜硜 kēng kēng (13.20): Zhu Xi — the sound of stone, and also the sense of being single-minded and unbending (專確). 莫己知 is 莫知己 'no one knows him', 己 drawn before the verb after 莫. 斯已而已矣 'then (he should) stop, and that is all'. The last two lines are from the Ode 匏有苦葉 in the Airs of Wei (衛風; Zhu Xi): to go through the water in one's clothes is 厲 lì, to hold up one's clothes and wade is 掲 qì (以衣渉水曰厲，攝衣涉水曰掲; 掲起例反). Zhu Xi: he mocks Kongzi for not stopping when men do not know him, and for not being able to suit himself to the depth of the water. He Yan's comment: this hard clinking is merely trusting in himself, and is of no use; Bao Xian: one should go along with the age as one meets it — in water one must get across somehow; knowing it cannot be done, one should not do it."),
dict(w="子/the Master | 曰：「/said | ^果/resolute | 哉！/how | ^末/there is nothing | 之/(about) it | 難=nán/hard | 矣。」/(so it is)",
  l="The Master said: “Resolute indeed!\nThere is nothing hard about it.”",
  i="The Master said: “He has made up his mind, that one! And if that were all, nothing would be hard.”",
  n="果 'resolute, carried through' (13.20 行必果). Zhu Xi: 'resolute indeed' sighs at how resolute the man is in forgetting the world; 末 is 'none, nothing' (末，無也). The sage's heart is one with Heaven and Earth: he sees all under Heaven as one family and the Central States as one man, and cannot forget them for a single day; so, hearing the basket-carrier, he sighed at his resolve to forget the world, and said that if a man's going out to serve or staying at home were only like this, there would be nothing hard in it (人之出處若但如此則亦無所難矣). He Yan's comment: the man mocked him without knowing his aims, and that is what makes him 'resolute'; and there is no answering him, since he cannot understand the Master's Way. Variant: He Yan's text prints 未之難矣 'not yet hard'; but its comment, which also prints 未, glosses the word 無 'none' (未無也) — Zhu Xi's gloss of 末 — so 未 is most likely a slip for 末 in both places."),
# ---------------- 14.43 ----------------
dict(pas="14.43", w="子張=zǐ zhāng/Zizhang | 曰：「《/said | 書》/the Documents | 云：『/say | ^髙宗=gāo zōng/Gaozong//high//ancestor, (in temple names) 'Ancestor' | 諒隂，=liáng ān/(kept) the mourning seclusion//(in 諒隂)//(in 諒隂) | ^三/three | 年/years | 不/(he) did not | 言。』/speak | ^何/what | 謂/is meant | 也？」/(question)",
  l="Zizhang said: “The Documents say: ‘Gaozong kept the mourning seclusion;\nfor three years he did not speak.’\nWhat is meant?”",
  i="Zizhang said: “The Documents tell us that Gaozong, in mourning, kept silent for three years. What does that mean?”",
  n="《書》 the Documents (2.21). 髙宗 Gaozong ('High Ancestor', a temple name; 髙 is the edition's form of 高) is King Wuding of Shang (Zhu Xi: 商王武丁也; Kong Anguo in He Yan: the king who restored Yin). 諒隂 is read liáng ān by tradition; Zhu Xi says only that it is the name for the Son of Heaven's dwelling in mourning, and that its sense is not clear (天子居喪之名未詳其義). Kong Anguo takes it word by word: 諒 'truly', 隂 'silent' (諒信也，隂猶黙也) — 'truly silent, he did not speak for three years'. 何謂也 'what is meant (by it)?'."),
dict(w="子/the Master | 曰：「/said | ^何/why | 必/necessarily | 髙宗？=gāo zōng/Gaozong | ^古/of old | 之/(of) | 人/the people | 皆/all | 然。/(were) so | ^君/the lord | 薨，=hōng/having died | ^百/the hundred | 官/offices | 總=zǒng/gathered up | 己=jǐ/their own (charges) | 以/and | 聽=tīng/took orders | 於/from | 冢宰=zhǒng zǎi/the Chief Steward//great, chief//steward | 三/(for) three | 年。」/years",
  l="The Master said: “Why only Gaozong?\nThe people of old were all so.\nThe lord having died,\nthe hundred offices gathered up their own charges and took orders from the Chief Steward for three years.”",
  i="The Master said: “Why Gaozong in particular? All the men of old did it. When a ruler died, every officer took his own duties in hand and looked to the Chief Steward for orders for three years.”",
  n="The print has 總已, a misprint for 總己, corrected here. Zhu Xi's comment reads 總己 and explains it: each gathered up and held his own office (總己謂總攝己職); Ruan Yuan's 1816 text prints 己. 何必 'why necessarily…?'. 薨 hōng is the death of a lord. Zhu Xi: saying 君 'the lord' means that the feudal lords did so too, not the king alone (言君薨則諸侯亦然). 冢宰 zhǒng zǎi is the Chief Steward (Zhu Xi: 冢宰大宰也, the Grand Steward of 9.6; Kong Anguo in He Yan: the Heaven officer who helps the king govern); since the hundred officers took orders from him, the lord could go three years without speaking. Kong Anguo: when the three years of mourning were over, the king took up the hearing of government himself. Zhu Xi quotes Hu Yin: ranks differ in honour, but all are born of father and mother alike, so the three years' mourning runs from the Son of Heaven to the common people; Zizhang did not doubt that — he probably feared that if a ruler did not speak for three years his ministers would have nowhere to take their orders, and disorder might rise from it; Kongzi told him they took orders from the Chief Steward, so disorder was not to be feared."),
# ---------------- 14.44 ----------------
dict(pas="14.44", w="子/the Master | 曰：「/said | ^上/(if) those above | 好=hào/love | 禮，/the rites | ^則/then | 民/the people | 易=yì/(are) easy | 使/to employ | 也。」/(assertion)",
  l="The Master said: “If those above love the rites,\nthen the people are easy to employ.”",
  i="The Master said: “When those at the top love the rites, the people are easily led.”",
  n="上好禮 'those above love the rites' as 13.4. 好 is hào 'to love', 易 yì 'easy' (Zhu Xi: 好易皆去聲). 易使 'easy to employ': the verb after the adjective is taken passively, as 13.25 易事. Zhu Xi quotes Xie Liangzuo: when the rites reach everywhere, each man's lot is settled, so the people are easy to employ (禮達而分定故民易使). He Yan's comment: none of the people dare be irreverent, so they are easy to employ."),
# ---------------- 14.45 ----------------
dict(pas="14.45", w="子路=zǐ lù/Zilu | 問/asked about | 君子。=jūn zǐ/the gentleman | ^子/the Master | 曰：「/said | 脩=xiū/(he) cultivates | 己/himself | 以/with | 敬。」/reverence | ^曰：「/(Zilu) said | 如/like | 斯/this | 而/and | 已/that is all | 乎？」/(question) | ^曰：「/(the Master) said | 脩=xiū/(he) cultivates | 己/himself | 以/so as to | 安/give peace to | 人。」/others | ^曰：「/(Zilu) said | 如/like | 斯/this | 而/and | 已/that is all | 乎？」/(question) | ^曰：「/(the Master) said | 脩=xiū/(he) cultivates | 己/himself | 以/so as to | 安/give peace to | 百姓。=bǎi xìng/the hundred clans | ^脩=xiū/cultivating | 己/oneself | 以/so as to | 安/give peace to | 百姓，=bǎi xìng/the hundred clans — | ^堯=yáo/Yao | 舜=shùn/(and) Shun | 其/even they | 猶/still | 病/felt themselves short | 諸！」=zhū/(in) this",
  l="Zilu asked about the gentleman.\nThe Master said: “He cultivates himself with reverence.”\nHe said: “Like this, and that is all?”\nHe said: “He cultivates himself so as to give peace to others.”\nHe said: “Like this, and that is all?”\nHe said: “He cultivates himself so as to give peace to the hundred clans.\nCultivating oneself so as to give peace to the hundred clans —\neven Yao and Shun still felt themselves short in this.”",
  i="Zilu asked about the gentleman. The Master said: “He cultivates himself and is reverent.” “Is that all?” “He cultivates himself and so brings peace to those around him.” “Is that all?” “He cultivates himself and so brings peace to the whole people. To cultivate oneself and so bring peace to the whole people — even Yao and Shun felt they fell short in this.”",
  n="脩 xiū (= 修) 'to put in order, to cultivate'. 以 first 'with, in' (脩己以敬), then 'so as to' (以安人). 如斯而已乎 'like this, and that is all?' — 而已 'and stop there'. 百姓 'the hundred clans', the whole people (12.9). The last line is 6.28's, with its English. Zhu Xi: 'cultivating oneself with reverence' — the Master's words were complete and exhaustive, but Zilu thought them too little, so he told him twice more of how this, filled out and full, reaches others of itself; there is no other way. 人 is said against oneself; 百姓 takes in all men. That Yao and Shun still felt short means nothing can be added beyond this — so as to check Zilu and make him turn back and look for it close at hand. The sage's heart has no limit: however well the age is governed, how could he be sure that within the four seas not one thing failed of its place? He quotes Master Cheng: 'the gentleman cultivates himself so as to give peace to the hundred clans; earnest and reverent, and the world is at peace' (篤恭而天下平, the Doctrine of the Mean). Kong Anguo in He Yan: 人 means friends and the nine degrees of kin; 病 is 'to find it hard' (病猶難也). Variant: He Yan's text reads 脩己以敬人 'cultivates himself so as to respect others' (its print writes 巳 for 己), but Kong Anguo's comment there, 'to be reverent in his person' (敬其身也), fits Zhu Xi's text."),
# ---------------- 14.46 ----------------
dict(pas="14.46", w="原壤=yuán rǎng/Yuan Rang | 夷/squatting | 俟。/waited | ^子/the Master | 曰：「/said | ^幼=yòu/young | 而/and | 不/not | 孫=xùn/humble | 弟，=tì/(or) deferential; | ^長=zhǎng/grown | 而/and | 無/nothing | 述/to be told | 焉；/of him; | ^老/old | 而/and | 不/not | 死：/dying — | 是/this | 為=wéi/is | 賊。」/a despoiler | ^以/with | 杖/his staff | 叩/(he) tapped | 其/his | 脛。=jìng/shin",
  l="Yuan Rang waited squatting.\nThe Master said: “Young, and not humble or deferential;\ngrown, and nothing to be told of him;\nold, and not dying — this is a despoiler.”\nWith his staff he tapped his shin.",
  i="Yuan Rang sat waiting on his haunches. The Master said: “Not humble or respectful as a boy, nothing worth telling as a man, and now old and still not dead — you do nothing but harm.” And he rapped him on the shin with his staff.",
  n="原壤 Yuan Rang was an old friend of Kongzi's; Zhu Xi recalls that when his mother died he sang, and calls him probably one of Laozi's sort who set themselves outside the rites (葢老氏之流自放於禮法之外者). 夷 is to squat (Zhu Xi: 夷，蹲踞也; Ma Rong in He Yan: 踞也), 俟 'to wait': seeing Kongzi coming, he squatted and waited for him. 孫 xùn = 遜 'humble' and 弟 tì 'deferential' (Zhu Xi: 孫弟並去聲); 幼 yòu 'young'; 長 zhǎng 'grown up' (上聲). 述 'to be told of', Zhu Xi 猶稱也 'to be praised'. 賊 'a despoiler' — Zhu Xi: the name for one who harms others; from youth to age he had shown no single good thing, and living on long in the world he served only to spoil custom and disorder ways. 叩 kòu 'to knock' (Zhu Xi: 叩音口, i.e. kǒu; modern kòu; Kong Anguo: 叩，擊也), 脛 jìng 'the shin' (其定反; 足骨也). Zhu Xi: having rebuked him, Kongzi gave his shin a light tap with the staff he was trailing, as if to make him stop squatting."),
# ---------------- 14.47 ----------------
dict(pas="14.47", w="闕黨=què dǎng/Que village//(in 闕黨; a gate-tower)//community, village | 童子=tóng zǐ/a boy | 將=jiāng/carried | 命。/messages | ^或/someone | 問/asked (about) | 之/him | 曰：「/saying | 益/making progress | 者/one (who is) | 與？」=yú/(question)",
  l="A boy of Que village carried messages.\nSomeone asked about him, saying: “One who is making progress?”",
  i="A boy from the village of Que was carrying messages for the Master. Someone asked about him: “Is he coming on well?”",
  n="闕黨 Que is the name of a 黨, a village community (Zhu Xi: 黨名). 童子 'a boy': Zhu Xi, one not yet capped (未冠者之稱), as 7.28. 將命 'to carry the charge', passing words between host and guest (Zhu Xi: 傳賓主之言; Ma Rong in He Yan, taking them in and out); 將 is jiāng. 益者與 'one who is advancing?' (與 yú; Zhu Xi: 與平聲): Zhu Xi, the questioner supposed the boy had made progress in his learning, so that Kongzi had him carry messages as a mark of favour. Variant: He Yan's text reads 闕黨童子將命矣, adding 矣."),
dict(w="子/the Master | 曰：「/said | ^吾/I | 見=jiàn/see | 其/him | 居/sitting | 於/in | 位/a (grown man's) place | 也，/(pause) | ^見=jiàn/see | 其/him | 與=yǔ/with | 先生=xiān shēng/his elders | 並=bìng/side by side | 行=xíng/walking | 也：/(pause) | ^非/(he is) not | 求/seeking | 益/to make progress | 者/one (who is) | 也，/(assertion) | ^欲/wanting | 速/quickly | 成/to be grown | 者/one (who is) | 也。」/(assertion)",
  l="The Master said: “I see him sitting in a place,\nsee him walking side by side with his elders:\nhe is not one seeking to make progress;\nhe is one wanting to be grown quickly.”",
  i="The Master said: “I see him take his seat among the grown men, and walk abreast of his elders. He is not after progress; he wants to be grown up in a hurry.”",
  n="Zhu Xi: by the rites a boy should sit in a corner and walk behind (禮童子當隅坐隨行); Kongzi says he sees this boy not keeping to the rule — he does not seek to advance, he only wants to be grown quickly. So the Master gave him the errands to run, to watch the order of elder and younger and practise the manners of bowing and giving way: it was to check and teach him, not to favour and single him out. 居於位 'to sit in a place': He Yan's comment — a boy sits in a corner and has no place; only grown men have one. 先生 'the elders' (2.8; Bao Xian in He Yan: 先生，成人也 'grown men'). 並 bìng 'side by side'; 與 yǔ 'with'. Bao Xian: walking abreast, not falling behind, is against the rites; such a one wants to be grown quickly and is not seeking to advance. Variant: He Yan's text reads 吾見其踞於位也 'I see him squatting in a place'; its own comment speaks only of the boy's having no place, so 踞 may be a slip for 居."),
]
