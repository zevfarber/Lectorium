# Analects Book 10 (鄉黨) — draft, second half: lemmata 29–60 = passages 10.8–10.18.
# Token format as the pilot:
#   tokens separated by " | "; a token is  CHARS[PUNCT][=pinyin][/context gloss[//char gloss//char gloss]]
#   a leading "^" breaks the verse line before the token.
# Punctuation is editorial (the edition has none) and always trails the word before it.
# Pinyin defaults to the glossary's first reading; every polyphone states its reading here, and so does
# every bound compound and every character not yet in the glossary.
# Passages follow the ○ breaks printed in Zhu Xi's single chapter (舊說凡一章; see unit 0): 10.8 (food)
# runs over ten units, 29–38; 10.9 one (39); 10.10 two (40–41); 10.11 two (42–43); 10.12 one (44);
# 10.13 four (45–48); 10.14 one (49); 10.15 two (50–51); 10.16 five (52–56); 10.17 two (57–58);
# 10.18 two (59–60). The copy also prints a stray ○ at the end of Zhu Xi's comments on units 45 and 50,
# inside the parentheses; these are not section breaks.
# Lemma 61 (論語卷五) is the running head and is skipped by the build.
# Unit 49 (10.14 入太廟每事問) repeats 3.15's opening clause (Zhu Xi: 重出); its l and i are those
# shipped for 3.15, with "he" for "the Master" because this text has no 子.
# Quotation marks balance within every unit; no speech here runs past one of Zhu Xi's comments.
# Glyphs kept as the edition prints them: 甞 (= 嘗, units 43, 45), 廏 (= 廄, 44), 太 in 太廟 (3.15 has
# 大廟), 䙝 (= 褻, 53), 内 (= 內, 58).
# Readings decided:
#   食 sì 'rice, cooked grain' where Zhu Xi marks 音嗣 (29 食不厭精, 30 食饐, 32 勝食氣, 38 疏食; as 7.15);
#     shí 'to eat' / 'food' elsewhere (30, 31, 33, 35, 36 不食; 34 薑食; 37 食不語; 45 君賜食; 46 侍食) —
#     Zhu Xi marks none of these, and 45's 食 is cooked food in general (his 食恐或餕餘), so shí.
#   勝 shèng 'to overcome, outweigh' at 32 不使勝食氣 (Zhu Xi gives no note; his paraphrase 不使肉勝食氣
#     is 'overcome'), against shēng 'bear' at 10.5 如不勝 (平聲).
#   量 liàng (去聲); 惡 è 'bad' (30); 臭 xiù 'smell, odour' (30: the neutral word, 惡 supplies 'bad');
#   宿 sù 'to keep overnight' (36); 語 yǔ 'to converse' (37: Zhu Xi 答述曰語); 齊 zhāi in 齊如也 (38: Zhu Xi
#     and Kong Anguo 嚴敬貌, the gravity of the purifying fast, 10.7; Zhu Xi marks no reading here);
#   飲 yǐn; 朝 cháo (41, 44, 47; Zhu Xi 10.1 直遙反下同); 儺 nuó (乃多反); 見 jiàn (53); 與 yǔ 'and' (53);
#   齊衰 zī cuī (53, as 9.9); 畜 xù 'to rear' (45); 飯 fàn (46, 扶晚反); 首 shòu 'to turn the head toward'
#   (47, Zhu Xi 去聲; a different word from shǒu 'head', so kept); 拖 tuō (47: Zhu Xi 徒我反, which would
#   give modern duò; modern practice reads tuō, which we give — the note says so); 召 zhào; 行 xíng;
#   車 chē; 盛 shèng; 式 shì; 嗅 xiù (許又反); 共 gòng 'to set out, serve' (60: Zhu Xi 九用反 first, with
#   Xing Bing's 共具之; his 又居勇反 gǒng = 拱 goes with Chao's and Liu's alternatives — the note says so).
# New bound compounds (need glossary entries): 康子 kāng zǐ (Ji Kangzi), 太廟 tài miào (as 大廟),
#   阼階 zuò jiē (the eastern steps, Zhu Xi 東階也). Existing used: 朋友, 齊衰, 子路.
#   Not bound (they mean what their parts mean): 疏 | 食 (as 7.15), 菜 | 羹, 鄉 | 人, 朝 | 服, 祭 | 肉,
#   車 | 馬, 凶 | 服, 負 | 版, 盛 | 饌, 迅 | 雷, 山 | 梁, 雌 | 雉.
# Collation (first witness Ruan 1816 KR1h0004, second He Yan SBCK KR1h0005), noted in the unit:
#   Ruan: 38 必 for 瓜 (as Zhu Xi's Lu Deming: 魯論瓜作必); 52 居不客 for 居不容.
#   He Yan: 41 立阼階 (no 於); 42 再拜送之 (no 而); 43 不敢甞之 (adds 之); 45 先甞 (no 之);
#   53 子見齊衰者 (adds 子); 60 供 for 共.
#   Not noted (graphic, or a transcription slip): Ruan's doubled 不食 in 31; 蔬, 嘗, 廄, 內; He Yan's 郷,
#   䟽, 悪, 㘴, 廐, 毎.

UNITS_B = [
# ---------------- 10.8 ----------------
dict(pas="10.8", w="食=sì/(his) rice | 不/not | 厭/(did he) refuse | 精，=jīng/(for being) finely polished | ^膾=kuài/minced meat | 不/not | 厭/(did he) refuse | 細。=xì/(for being) finely cut",
  l="Rice — he did not refuse it finely polished;\nminced meat — he did not refuse it finely cut.",
  i="He had no objection to rice hulled clean and white, or to raw meat sliced thin.",
  n="Book 10 now turns to the Master's food and drink, and this section (10.8) runs over ten units. 食 here is read sì, 'cooked grain, rice' (Zhu Xi: 食音嗣…食，飯也; as 疏食 in 7.15), not shí 'to eat'. 精 'fine' is rice well hulled (Zhu Xi: 精，鑿也). 膾 kuài is raw meat cut fine — Zhu Xi: the raw flesh of ox, sheep or fish, sliced and then cut, is called 膾. 不厭 is literally 'did not reject': Zhu Xi says it means he counted these good, not that he insisted on having them so; rice fine nourishes a man, meat coarse can harm him. He Yan has no comment here."),
dict(w="食=sì/rice | 饐=yì/gone sour with heat | 而/and | 餲，=ài/off in taste | ^魚=yú/fish | 餒=něi/gone soft | 而/and | 肉/meat | 敗，/spoiled | ^不/not | 食。=shí/(he) ate | ^色/the colour | 惡，=è/bad | ^不/not | 食。=shí/(he) ate | ^臭=xiù/the smell | 惡，=è/bad | ^不/not | 食。=shí/(he) ate | ^失/missing | 飪，=rèn/the right cooking | ^不/not | 食。=shí/(he) ate | ^不/not | 時，/in season | ^不/not | 食。=shí/(he) ate",
  l="Rice gone sour and off in taste,\nfish gone soft and meat spoiled —\nhe did not eat.\nColour bad —\nhe did not eat.\nSmell bad —\nhe did not eat.\nCooking amiss —\nhe did not eat.\nNot in season —\nhe did not eat.",
  i="Rice that had soured or turned, fish that had gone soft, meat that had begun to rot — none of these would he eat. Nor would he eat what had lost its colour or smelled wrong, what was underdone or overdone, or what was out of its season.",
  n="Zhu Xi's readings: the first 食 is sì 'rice' (食饐之食音嗣); 饐 yì (於冀反), 餲 ài (烏邁反), 飪 rèn (而甚反; modern rèn). Zhu Xi: 饐 is rice spoiled by heat and damp, 餲 its taste turned; fish going bad is called 餒, meat putrefying 敗. 色惡 and 臭惡 are food not yet spoiled whose colour or smell has changed — 臭 is 'smell' in general (read xiù), and 惡 è 'bad' says which. 飪 is the measure of rawness and doneness in cooking. 不時 is, for example, grain not grown to fullness or fruit not yet ripe. All of these can harm a man, so he did not eat them; 不食 'he did not eat' is shí each time. He Yan's Kong Anguo: 饐 and 餲 are changes of smell and taste; fish spoiled is 餒; 失飪 is missing the point between raw and cooked. His Zheng Xuan reads 不時 differently: 'not at the times' — not at morning, evening or midday, the hours of meals."),
dict(w="割=gē/cut | 不/not | 正，/square | ^不/not | 食。=shí/(he) ate | ^不/not | 得/getting | 其/its | 醬，=jiàng/sauce | ^不/not | 食。=shí/(he) ate",
  l="Cut not square —\nhe did not eat.\nNot getting its sauce —\nhe did not eat.",
  i="Meat not cut square he left alone, and he would not eat a dish without the sauce that belonged to it.",
  n="割 'to cut' is the carving of meat; 正 here is 'square, true'. 其醬 'its sauce': Zhu Xi says each meat has the sauce proper to it. Zhu Xi: meat not squarely cut he would not eat, not leaving what is correct even in haste; he adds that in the Han, Lu Xu's mother (陸續之母) never cut meat other than square and cut her onions to the inch — a fine nature that happened to match this. Without its sauce he would not eat, disliking a dish incomplete; neither of these harms a man, but he would not eat carelessly for the sake of taste. He Yan's Ma Rong gives an example: minced fish without mustard sauce he did not eat. (The Ruan witness doubles the last 不食; it is a slip of the transcription and is not followed.)"),
dict(w="肉/meat | 雖/though | 多，/plentiful | ^不/not | 使/letting (it) | 勝=shèng/outweigh | 食=sì/the rice's | 氣。/share, force (lit. breath) | ^唯=wéi/only | 酒/wine | 無/had no | 量，=liàng/fixed measure | ^不/not | 及/reaching | 亂。/disorder",
  l="Meat, though plentiful —\nhe did not let it outweigh the rice.\nOnly wine had no measure —\nnot reaching disorder.",
  i="However much meat there was, he never let it outweigh the rice. Wine alone he did not stint, but he never drank to the point of confusion.",
  n="食 is again sì 'rice' (Zhu Xi: 食音嗣), and 量 is liàng 'a measure' (量去聲). 勝 Zhu Xi leaves unmarked; we read shèng 'to overcome, outweigh', the word of his own paraphrase (不使肉勝食氣), not shēng 'to bear' as in 如不勝 (10.5). 氣 is literally 'breath, vital force': the meat must not overpower what the grain gives. 唯 wéi 'only'. Zhu Xi: in eating, grain is the main thing, so meat is not let outweigh it; wine is for joining men in gladness, so he set no quantity, only taking drunkenness as the limit and stopping short of disorder. He quotes Master Cheng: 'not reaching disorder' means not only that the mind is not thrown into disorder — even the blood and breath must not be disordered; to be warmed through, and no more, is right. He Yan has no comment on this unit."),
dict(w="沽=gū/bought | 酒/wine | 市=shì/market-bought | 脯，=fǔ/dried meat | ^不/not | 食。=shí/(he) took",
  l="Bought wine, market dried-meat —\nhe did not take.",
  i="Wine bought from a shop and dried meat from the market he would not touch.",
  n="沽 and 市 are both 'to buy' here (Zhu Xi: 沽、市皆買也) — 沽 is 'to sell' in 9.12, but the word served for both sides of a trade. 脯 fǔ is dried meat. 不食 covers the wine too: 'he did not take (them)'. Zhu Xi: he feared they might not be fine and clean and might harm him — the same thought as not tasting Kangzi's medicine (10.11). He Yan has no comment."),
dict(w="不/not | 撤=chè/removing | 薑=jiāng/the ginger | 食。=shí/(at his) food",
  l="He did not take away the ginger at meals.",
  i="Ginger he never had cleared from the table.",
  n="撤 chè 'to clear away'; 薑 jiāng 'ginger'; 食 shí 'food, the meal'. Zhu Xi: ginger reaches the spirit's clarity and drives off foulness, so he did not have it removed. He Yan's Kong Anguo ties it to the fast: 撤 is 去 'to remove'; during a fast strong-smelling things (薰物) were forbidden, but ginger, though pungent, does not smell, so it was not removed."),
dict(w="不/not | 多/much | 食。=shí/(he) ate",
  l="He did not eat much.",
  i="And he never ate more than he needed.",
  n="Zhu Xi: he ate enough and stopped, with no greed in his heart. He Yan's Kong Anguo: 不過飽 'never beyond full'. Zhu Xi prints this apart from the ginger clause before it, so both commentaries take it of eating in general, not of the ginger."),
dict(w="祭=jì/sacrificing | 於/at | 公，/the duke's (rites) | ^不/not | 宿=sù/keeping overnight | 肉。/the meat | ^祭=jì/sacrificial | 肉/meat | 不/not | 出/going past | 三/three | 日。/days | ^出/past | 三/three | 日，/days | ^不/not | 食=shí/eaten | 之/it (is) | 矣。/(so it is)",
  l="Sacrificing at the duke's,\nhe did not keep the meat overnight.\nSacrificial meat did not go past three days.\nPast three days,\nit is not eaten.",
  i="Meat he brought back from the duke's sacrifice he did not keep even one night. His own sacrificial meat he did not keep beyond three days; after three days it would not be eaten.",
  n="祭於公 is assisting at the sacrifice of the ruler of the state. 宿 sù is 'to keep overnight'. Zhu Xi: the meat of the offering (胙肉) received at the duke's sacrifice was given out as soon as he came home, without waiting a night — not holding back the spirits' bounty. The meat of his family's own sacrifice he gave away within three days, for after three days it would spoil and people would not eat it, which would be to slight the leavings of the spirits; still, it could wait a little longer than the lord's gift. He Yan's Zhou Shenglie: the portions of the victims received from assisting at the lord's sacrifice were distributed on his return, not keeping back the spirits' bounty; and his Zheng Xuan: the second clause is about his own family's sacrifice; past three days it is not eaten, which would slight the spirits' leavings."),
dict(w="食=shí/eating | 不/not | 語，=yǔ/conversing | ^寢/lying down to sleep | 不/not | 言。/talking",
  l="At meals, no conversing;\nin bed, no talking.",
  i="Over his food he held no conversation, and once he had lain down he said nothing.",
  n="食 shí 'eating'; 寢 'to lie down to sleep'. Zhu Xi distinguishes the two words for speaking: answering or telling others is 語 (read yǔ here), speaking of one's own accord is 言. He quotes Fan Zuyu: the sage's mind does not wander — at the time to eat he eats, at the time to sleep he sleeps, and talk then is out of its time. And Yang Shi: the lungs govern the breath and the voice comes from them; in sleeping and eating the breath is blocked, and talking might harm it — a reading Zhu Xi says also works (亦通). He Yan has no comment."),
dict(w="雖/even (with) | 疏=shū/coarse | 食=sì/rice | 菜=cài/vegetable | 羹，=gēng/broth | ^瓜=guā/melon | 祭，=jì/(he) offered | ^必/always | 齊=zhāi/grave, as at the fast | 如/(-like) | 也。/(assertion)",
  l="Even coarse rice and vegetable broth,\nmelon — he offered,\nalways gravely.",
  i="Even when the meal was only coarse rice, vegetable broth and a melon, he set aside the offering from each, and always with a solemn face.",
  n="疏食 shū sì 'coarse rice' (Zhu Xi: 食音嗣; as 7.15); 菜羹 cài gēng is broth of vegetables. Zhu Xi explains the offering: the ancients, at every kind of food and drink, set out a little of each in the space between the dishes as an offering to the first men who made food and drink — not forgetting the root. Confucius made the offering even from poor things, and made it with reverence — the sage's sincerity. 齊如 'grave-looking' (Zhu Xi: 嚴敬貌; He Yan's Kong Anguo the same): Zhu Xi marks no reading, and we read zhāi, the word of the purifying fast of 10.7, whose gravity it describes. Variant: Zhu Xi quotes Lu Deming that the Lu Analects has 必 for 瓜, and the first collation witness (Ruan's 1816 text) reads so: 雖疏食菜羹，必祭，必齊如也 'even with coarse rice and vegetable broth, he always offered, always gravely' — no melon. He Yan's Kong Anguo, reading 瓜, speaks of 'three things' (rice, broth, melon): though meagre, they were offered with reverence. Zhu Xi's summary of 10.8: it records the measure Confucius kept in eating and drinking. He quotes Xie Liangzuo: the sage ate like this not to satisfy mouth and belly but to nourish breath and body without harming life; yet what the sage would not eat, those who indulge the palate sometimes eat, desire getting the upper hand so that they have no time to choose."),
# ---------------- 10.9 ----------------
dict(pas="10.9", w="席=xí/the mat | 不/not | 正，/square | ^不/not | 坐。=zuò/(he) sat",
  l="The mat not square —\nhe did not sit.",
  i="Until his mat lay straight he would not take his seat.",
  n="席 xí is the mat one sat on; 正 'set straight, square'. A section of a single line. Zhu Xi quotes Xie Liangzuo: the sage's mind rests in what is correct, so he would not stay in a place that was not correct, small as the matter was. He Yan has no comment."),
# ---------------- 10.10 ----------------
dict(pas="10.10", w="鄉/(at) the village | 人/people's | 飲=yǐn/drinking | 酒，/of wine | ^杖=zhàng/(those with) staffs | 者/the ones | 出，/went out | ^斯/then | 出/(he) went out | 矣。/(so it was)",
  l="At the villagers' wine-drinking,\nwhen those with staffs went out,\nthen he went out.",
  i="When the people of his district met to drink together, he left as soon as the old men with their staffs had left, and not before.",
  n="鄉人飲酒 is the district's ceremonial drinking: He Yan's Kong Anguo says its rite centres on the old, and when the old had finished and left, Confucius followed them out. 杖者 'those with staffs' are the old: Zhu Xi says men of sixty carry a staff in the district (六十杖於鄉). 斯 here is 'then, thereupon'. Zhu Xi: before they had gone he did not dare go first; once they had gone he did not dare stay behind."),
dict(w="鄉/(when) the village | 人/people | 儺，=nuó/performed the exorcism | ^朝=cháo/(in) court | 服/robes | 而/he | 立/stood | 於/on | 阼階。=zuò jiē/the eastern steps//east (steps)//steps",
  l="When the villagers held the exorcism,\nin court robes he stood on the eastern steps.",
  i="When the villagers went round driving out the demons of sickness, he put on his court dress and stood on the eastern steps.",
  n="儺 nuó (Zhu Xi: 乃多反) is the rite of driving out pestilence; Zhu Xi says the Rites of Zhou put it in the charge of the Fangxiang shi (方相氏). 朝服 cháo fú 'court robes' (朝 read cháo as in 10.1). 阼階 zuò jiē are the eastern steps (Zhu Xi: 東階也). Zhu Xi: though 儺 was an ancient rite, it came close to play; that he still attended it in court dress shows there was nothing into which he did not put sincerity and reverence. Some say (或曰) he feared it would startle the spirits of his forebears and of the five household sacrifices, and wished them to rely on him and be at peace. Zhu Xi's summary: this section records Confucius's conduct in his district. He Yan's Kong Anguo: 儺 drives out the demons of pestilence; fearing it would startle his forebears, he stood in court dress on the eastern steps. Variant: He Yan's text reads 立阼階, without 於 'on'."),
# ---------------- 10.11 ----------------
dict(pas="10.11", w="問/(sending) to ask after | 人/someone | 於/in | 他/another | 邦，/state | ^再/twice | 拜/(he) bowed | 而/and | 送=sòng/sent off | 之。/him (the messenger)",
  l="Sending to ask after someone in another state,\nhe bowed twice and saw him off.",
  i="When he sent a messenger with greetings to someone in another state, he bowed to him twice as he saw him off.",
  n="問 here is 'to send to inquire after, to send greetings to'. 之 is the messenger. Zhu Xi: he bowed to the messenger as he left, with the reverence he would have shown on seeing the friend himself; He Yan's Kong Anguo says the same. Variant: He Yan's text reads 再拜送之, without 而."),
dict(w="康子=kāng zǐ/Kangzi — Ji Kangzi, a grandee of Lu//Kang (his posthumous name)//(title of respect) | 饋=kuì/sent as a gift | 藥，=yào/medicine | ^拜/(he) bowed | 而/and | 受=shòu/accepted | 之。/it | 曰：「/(and) said | ^丘/I, Qiu, | 未/do not yet | 達，/understand (it) | ^不/not | 敢/(I) dare | 甞。」=cháng/taste (it)",
  l="Kangzi sent him medicine;\nhe bowed and accepted it, and said:\n“I, Qiu, do not yet understand it;\nI dare not taste it.”",
  i="When Ji Kangzi sent him a gift of medicine, he bowed as he took it, and said: “I do not know enough about this, and will not venture to try it.”",
  n="康子 is Ji Kangzi 季康子, the Lu grandee of 2.20 and 6.6 (the commentaries do not name him here; Yang Shi below calls the giver a grandee, 大夫). 饋 kuì 'to send as a gift'. 丘 is Confucius's personal name, used of himself. 達 'to understand thoroughly' — what the medicine was and what it did. 甞 is the edition's form of 嘗 cháng 'to taste'. Zhu Xi quotes Fan Zuyu: whenever food is given, one tastes it and then bows; medicine not understood he dared not taste; to accept it and not drink it would empty the gift, so he told the giver this — and so drinking what may be drunk and not drinking what may not are both contained here. And Yang Shi: when a grandee sends a gift, to bow and accept it is the rite; not tasting what one does not understand is care about illness; telling him so is straightforwardness. Zhu Xi's summary: this section records Confucius's sincerity in dealing with others. He Yan's Bao Xian: Kangzi gave Confucius medicine; Kong Anguo: not knowing its nature, he did not taste it, and this was the rite. Variant: He Yan's text reads 不敢甞之, 'dare not taste it'."),
# ---------------- 10.12 ----------------
dict(pas="10.12", w="廏=jiù/the stables | 焚。=fén/burned | ^子/the Master | 退/withdrew | 朝，=cháo/from court | 曰：「/(and) said | ^傷/was hurt | 人/anyone | 乎？」/(question) | ^不/not | 問/(he) asked about | 馬。/the horses",
  l="The stables burned.\nThe Master, coming back from court, said:\n“Was anyone hurt?”\nThe horses — he did not ask.",
  i="There was a fire in the stables. Home from court, the Master asked: “Has anyone been hurt?” Of the horses he said not a word.",
  n="廏 jiù is the edition's form of 廄 'stable'; 焚 fén 'to burn'. 退朝 'to withdraw from court' — 朝 read cháo. 傷人乎 'hurt — anyone?'. Zhu Xi: it was not that he did not care for horses, but his fear that men had been hurt was so great that he had no leisure to ask; to value men and hold beasts cheap is as it should be. He Yan's Zheng Xuan: valuing men and slighting beasts; 退朝 is coming home from the Lord of Lu's court. Neither commentary says whose stables they were."),
# ---------------- 10.13 ----------------
dict(pas="10.13", w="君/(when) the lord | 賜/bestowed | 食，=shí/cooked food | ^必/(he) always | 正/straightened | 席=xí/the mat | 先/(and) first | 甞=cháng/tasted | 之。/it | ^君/(when) the lord | 賜/bestowed | 腥，=xīng/raw meat | ^必/(he) always | 熟=shú/cooked | 而/and | 薦=jiàn/offered (to his forebears) | 之。/it | ^君/(when) the lord | 賜/bestowed | 生，/a live (beast) | ^必/(he) always | 畜=xù/reared | 之。/it",
  l="When the lord bestowed food,\nhe always set his mat straight and first tasted it.\nWhen the lord bestowed raw meat,\nhe always cooked it and offered it.\nWhen the lord bestowed a live beast,\nhe always reared it.",
  i="Cooked food sent by his lord he would taste first, sitting on a mat set straight. Raw meat from his lord he had cooked and presented at his ancestral altar. A live animal from his lord he kept and raised.",
  n="Three gifts, three responses: 食 shí cooked food, 腥 xīng raw meat (Zhu Xi: 生肉), 生 a living animal. 薦 jiàn 'to present (to the forebears)'; 畜 xù 'to rear'. Zhu Xi: cooked food might be leavings (餕餘), so he did not offer it to his forebears; straightening his mat and tasting first was as though he faced the lord; 'first tasted' implies he then gave the rest away. Raw meat he cooked and offered to his forebears, honouring the lord's gift. Rearing the live animal was humaneness toward the lord's kindness: without cause he would not dare kill it. He Yan's Kong Anguo: it was reverence for the lord's kindness; after tasting he gave it away; 薦 is offering to his forebears. Variant: He Yan's text reads 先甞, without 之."),
dict(w="侍=shì/attending | 食=shí/at a meal | 於/upon | 君，/the lord | ^君/(when) the lord | 祭，=jì/made the offering | ^先/(he) first | 飯。=fàn/ate",
  l="Attending the lord at a meal,\nwhen the lord made the offering,\nhe ate first.",
  i="When he sat at a meal with his lord, he began eating while the lord made the offering.",
  n="侍食 'to attend at a meal' with a superior. 祭 is the small offering before eating (10.8). 飯 fàn 'to eat' (Zhu Xi: 扶晚反). Zhu Xi cites the Rites of Zhou: when the king ate his full meal, the steward (膳夫) handed him the offering and tasted the food, and only then did the king eat. So one attending at the lord's meal does not make an offering himself while the lord makes his, but eats first, as though tasting the food for the lord — not daring to take the part of a guest. He Yan's Zheng Xuan says the same: when the lord made the offering he ate first, as if tasting it beforehand (the archived text of his comment writes 先飲 'drank first')."),
dict(w="疾，/(when he was) ill | 君/the lord | 視/came to see | 之，/him | ^東=dōng/(to the) east | 首，=shòu/(he) turned his head | ^加/(he) laid on (himself) | 朝=cháo/court | 服，/robes | ^拖=tuō/(and) drew across | 紳。=shēn/the great sash",
  l="Ill, and the lord came to see him:\nhe turned his head to the east,\nlaid his court robes over him,\nand drew the sash across.",
  i="Once when he was ill and his lord came to visit, he lay with his head to the east, his court robes spread over him and the great sash laid across them.",
  n="首 is read shòu, the verb 'to turn the head toward' (Zhu Xi: 首去聲), as against shǒu 'head'. 拖 'to draw, trail': Zhu Xi marks 徒我反, which would give a modern duò; modern practice reads tuō, which we give. 紳 shēn is the great sash of formal dress (Bao Xian: 紳，大帶). 朝服 cháo fú 'court robes'. Zhu Xi: the head to the east was to receive the breath of life (生氣); lying ill he could not dress and tie his sash, yet could not meet his lord in everyday clothes, so he had the court robes laid on his body and the sash drawn over them. He Yan's Bao Xian: the Master was ill, lying under the south window with his head to the east; he had his court robes laid on him and the sash drawn across, not daring to see his lord except in court dress."),
dict(w="君/the lord | 命/commanding | 召，=zhào/(and) summoning (him) | ^不/not | 俟=sì/waiting for | 駕=jià/the yoking (of the horses) | 行=xíng/(he) set off | 矣。/(at once)",
  l="When the lord's command summoned him,\nnot waiting for the yoking, he set off.",
  i="When his lord sent for him, he did not wait for his carriage to be made ready but set out on foot.",
  n="召 zhào 'to summon'; 俟 sì 'to wait for'; 駕 'to yoke (the horses to the carriage)'; 行 xíng 'to go'. 矣 marks the thing done. Zhu Xi: he hurried at the lord's command, setting out on foot, and the carriage, once yoked, followed him; He Yan's Zheng Xuan says the same. Zhu Xi's summary: this section records the rites by which Confucius served his lord."),
# ---------------- 10.14 ----------------
dict(pas="10.14", w="入/(he) entered | 太廟，=tài miào/the Grand Temple — of the Duke of Zhou, in Lu//grand (read tài)//temple | ^每=měi/each | 事/thing | 問。/(he) asked about",
  l="He entered the Grand Temple;\nabout each thing he asked.",
  i="When he went into the Grand Temple, he asked about every detail.",
  n="Zhu Xi notes only 重出 'a repeat': these are the opening words of 3.15 (子入大廟，每事問), and the English is the one given there, with 'he' for 'the Master', since this text has no 子. The edition writes 太廟 here, 大廟 there; both are read tài miào, the temple of the Duke of Zhou in Lu. 每事問 puts the object first: 'each thing (he) asked about'. He Yan's Zheng Xuan: he had gone in to assist his lord at a sacrifice; the Grand Temple is the Duke of Zhou's temple."),
# ---------------- 10.15 ----------------
dict(pas="10.15", w="朋友=péng yǒu/a friend | 死，/died | ^無/(with) no (one) | 所/to whom | 歸，/(he might) go home | 曰：「/(he) said | ^於/at | 我/my (house) | 殯。」=bìn/lay him out",
  l="A friend died,\nwith no one to go home to; he said:\n“Lay him out at mine.”",
  i="When a friend died with no family to take him in, he said: “Let him lie in his coffin at my house.”",
  n="無所歸 'nowhere to return to': He Yan's Kong Anguo explains, no near kin. 殯 bìn is to coffin the dead and keep the body until burial. Zhu Xi: friends are joined by what is right; when one died with nowhere to go, he could not but lay him out. Kong Anguo: it shows how he valued the kindness of friends."),
dict(w="朋友=péng yǒu/a friend's | 之/'s | 饋，=kuì/gifts | ^雖/even (if) | 車=chē/a carriage | 馬，/(and) horses | ^非/(if) not | 祭=jì/sacrificial | 肉，/meat | ^不/not | 拜。/(did he) bow",
  l="A friend's gifts,\neven carriage and horses —\nif not sacrificial meat,\nhe did not bow.",
  i="For gifts from a friend he did not bow, even for a carriage and horses — only for meat from a sacrifice.",
  n="車馬 'carriage and horses', the weightiest of gifts; 車 chē. Zhu Xi: friends share their goods as a matter of right (通財之義), so even for so weighty a gift he did not bow; for sacrificial meat he bowed, honouring the friend's forebears as he would his own kin. He Yan's Kong Anguo also explains the not bowing by the right of sharing goods. Zhu Xi's summary: this section records what Confucius held right between friends."),
# ---------------- 10.16 ----------------
dict(pas="10.16", w="寢/lying asleep | 不/not | 尸，=shī/(lying like) a corpse | ^居/at home | 不/not | 容。/(putting on) formal bearing",
  l="Asleep, not like a corpse;\nat home, no formal bearing.",
  i="He did not sleep sprawled out like a dead man, nor did he sit about at home as if on ceremony.",
  n="尸 shī 'corpse' is a verb here, 'to lie like a corpse'. Zhu Xi: 尸 is lying flat on the back like a dead man; 居 is being at home; 容 is formal bearing. He quotes Fan Zuyu: not lying like a corpse was not that he disliked resembling the dead; slack and idle breath never settled in his body, and though he stretched out his limbs he was never sprawling. Without formal bearing at home was not slackness either — only that he was not as when offering sacrifice or receiving guests: the ease of 申申夭夭 (7.4). He Yan's Bao Xian: lying on the back with the four limbs spread out like a dead man; Kong Anguo: the reverence of household life is hard to keep up for long (so he did not keep formal bearing). Variant: the first collation witness (Ruan's 1816 text) reads 居不客, which would make it 'at home he did not behave like a guest'."),
dict(w="見=jiàn/seeing | 齊衰=zī cuī/mourning dress//hemmed (read zī)//mourning hemp (read cuī) | 者，/one in | ^雖/even if | 狎，=xiá/(an) intimate | ^必/always | 變。/(his face) changed | ^見=jiàn/seeing | 冕/the ceremonial cap | 者/one in | 與=yǔ/and | 瞽=gǔ/blind | 者，/one (who was) | ^雖/even if | 䙝，=xiè/(seen) often, informally | ^必/always | 以/with | 貌。/(due) bearing",
  l="Seeing one in mourning dress,\neven an intimate,\nhis look always changed.\nSeeing one in the ceremonial cap, or one blind,\neven at ease,\nalways with due bearing.",
  i="If he saw someone in mourning, even a close friend, his expression changed. Someone in a ceremonial cap, or a blind man, he always treated with formal courtesy, however often they met.",
  n="Compare 9.9, where Zhu Xi says the rest is explained (餘見前篇). 齊衰 zī cuī is mourning dress; 冕 the ceremonial cap of men of rank; 瞽 gǔ 'blind'. 見 jiàn 'to see'; 與 yǔ 'and'. 狎 xiá is long familiarity; 䙝 (the edition's form of 褻, xiè) is meeting at leisure; 貌 is the bearing the rites require. Zhu Xi: 狎 means already close and familiar; 褻 means seeing someone informally (燕見); 貌 is ritual courtesy. He Yan's Kong Anguo: 狎 is long familiarity; Zhou Shenglie: 䙝 is seeing often; even so he must keep his bearing, which is the rite. Variant: He Yan's text reads 子見齊衰者, with 子 'the Master' as subject."),
dict(w="凶=xiōng/mourning | 服/dress | 者/(one in) | 式=shì/(he) bowed (at the crossbar) | 之。/to him | ^式=shì/(he) bowed (at the crossbar) | 負=fù/carrying | 版=bǎn/the registers | 者。/(to one)",
  l="One in mourning dress — he bowed to him at the crossbar.\nHe bowed at the crossbar to one carrying the registers.",
  i="From his carriage he bowed to anyone in mourning clothes, and bowed too to the men who carried the state's registers.",
  n="式 shì is the crossbar at the front of a carriage, and so the verb 'to bow over the crossbar' (Zhu Xi: when there is someone to honour, one leans forward and rests on it). 凶服 is mourning dress. 負版 'carrying the boards': Zhu Xi and He Yan's Kong Anguo both say these are men carrying the maps and registers of the state (邦國圖籍). Zhu Xi: he bowed to the two out of grief for those in mourning and regard for the count of the people; man is the most spiritual of all things and what the king takes as his Heaven, so in the Rites of Zhou the count of the people is presented to the king and he receives it with a bow — how much less could those below him fail to honour it? Kong Anguo takes 凶服 as the clothes and goods for sending off the dead (送死之衣物)."),
dict(w="有/(when) there was | 盛=shèng/a lavish | 饌，=zhuàn/meal | ^必/always | 變/(he) changed | 色/countenance | 而/and | 作。/rose",
  l="When there was a lavish meal,\nhe always changed countenance and rose.",
  i="When a host set a sumptuous meal before him, he always rose with a changed face.",
  n="盛 shèng 'abundant, lavish'; 饌 zhuàn here is the meal served; 作 'to rise' (Kong Anguo: 起也). Zhu Xi: it was to honour the host's courtesy, not the food. He Yan's Kong Anguo: it honours the host's serving him in person (親饋)."),
dict(w="迅=xùn/sudden | 雷=léi/thunder | 風=fēng/(and) wind | 烈，=liè/fierce | ^必/always | 變。/(his look) changed",
  l="Sudden thunder, fierce wind —\nhis look always changed.",
  i="A crack of thunder or a violent wind always made his face grow grave.",
  n="Zhu Xi: 迅 is 'swift', 烈 'fierce'; his look changed in reverence for Heaven's anger. He cites the Record (the Book of Rites): if there is a fierce wind, swift thunder or heavy rain, one must change countenance, and even at night must rise, dress, put on one's cap and sit. He Yan's Zheng Xuan: reverence for Heaven's anger. Zhu Xi's summary of 10.16: this section records the changes in Confucius's bearing."),
# ---------------- 10.17 ----------------
dict(pas="10.17", w="升=shēng/mounting | 車，=chē/the carriage | ^必/always | 正/squarely | 立，/(he) stood | ^執/(and) held | 綏。=suí/the mounting cord",
  l="Mounting the carriage,\nhe always stood square\nand held the cord.",
  i="Getting up into his carriage, he always stood upright and took hold of the strap.",
  n="綏 suí is the cord one pulls on to climb into a carriage (Zhu Xi: 挽以上車之索也). Zhu Xi quotes Fan Zuyu: standing square and holding the cord, mind and body are all upright and sincere intent is grave and respectful; the gentleman's gravity is everywhere, and in mounting a carriage it shows in this. He Yan's Zhou Shenglie: standing square and holding the cord was for safety."),
dict(w="車=chē/the carriage | 中，/in | ^不/not | 内/backward | 顧，=gù/looking round | ^不/not | 疾/hurriedly | 言，/speaking | ^不/not | 親/himself | 指。/pointing",
  l="In the carriage,\nhe did not look round behind,\ndid not speak hurriedly,\ndid not point himself.",
  i="Inside the carriage he did not turn to look behind him, did not talk fast, and did not point at things.",
  n="内顧 'looking back' (Zhu Xi: 回視也); 内 is the edition's form of 內. 疾 here is 'quick'; 親 'oneself, in person'. Zhu Xi cites the Record: in looking about, one does not look past the wheel hub; all three lose one's bearing and unsettle others. His summary: this section records Confucius's bearing in his carriage. He Yan's Bao Xian: looking ahead no farther than the yoke-bar, to the side no farther than the side-rails and hub."),
# ---------------- 10.18 ----------------
dict(pas="10.18", w="色/(at) a look | 斯/then | 舉=jǔ/(it) rose | 矣，/(at once) | ^翔=xiáng/(it) wheeled | 而/and | 後/after (that) | 集。=jí/settled",
  l="At a look, up it rose;\nit wheeled, and after that settled.",
  i="Catching a hard look in a man's face, the bird was off; it circled, and only then came down to rest.",
  n="The subject, a bird, is not named; the next unit's pheasant may be it. 舉 is a bird's rising, 翔 its circling flight, 集 its alighting. Zhu Xi: it says that a bird, seeing an unfriendly look on a man's face, flies off, circles and looks carefully, and only then comes down to rest; a man, seeing the first signs, should act, and choose with care where he will stay, in the same way. But he adds that there must be text missing before and after this (此上下必有闕文矣). He Yan's Ma Rong: seeing an unfriendly look, it leaves; Zhou Shenglie: it circles and looks carefully, then comes down to rest."),
dict(w="曰：「/(he) said | ^山/(by) the hill | 梁=liáng/bridge | 雌=cí/the hen | 雉，=zhì/pheasant | ^時/timely | 哉！/how | 時/timely | 哉！」/how | ^子路=zǐ lù/Zilu | 共=gòng/set out (as food) | 之，/it | ^三/three times | 嗅=xiù/(he) smelt (it) | 而/and | 作。/rose",
  l="He said: “The hen pheasant by the hill bridge —\nhow timely! How timely!”\nZilu set it out;\nthree times he smelt it, and rose.",
  i="The Master said: “The hen pheasant there by the footbridge on the hill — she knows her moment! She knows her moment!” Zilu served it up to him; he sniffed it three times and got up from his place.",
  n="The book ends on its hardest lines. Zhu Xi quotes Xing Bing: 梁 is a bridge; 時哉 says the pheasant drinks and pecks at the right time; Zilu did not understand, took it for a delicacy of the season and set it out (共具之, 共 read gòng); Confucius did not eat it, but smelt it three times and rose. Zhu Xi then gives two other readings: Chao Yuezhi says the Stone Classics write 戞 for 嗅, meaning that the pheasant cried out; Liu Mianzhi (劉聘君) says 嗅 should be 狊, 'to spread both wings' (citing the Erya). On those two readings, Zhu Xi says, 共 should have the sense 拱執 'to clasp the hands, hold' (his 又居勇反, gǒng) — so that, as we understand it, the three times would be the bird's, crying or spreading its wings before it rose. But he concludes that text must be missing here and no explanation should be forced; he records what he has heard to wait for one who knows. He Yan's commentary (unattributed) reads as Xing Bing does: the Master says the hen pheasant on the hill bridge has found its time while men have not found theirs, and so he sighs; Zilu, taking it for a thing of the season, served it up; it was not what the Master meant, and not eating carelessly, he smelt it three times and rose. 嗅 xiù 'to smell' (Zhu Xi: 許又反). Variant: He Yan's text writes 供 'to provide' for 共, which supports gòng. The book closes here."),
]
