# Analects Book 10 (鄉黨) — draft, first half: lemmata 0–28 = passages 10.1–10.7. Token format as the pilot:
#   tokens separated by " | "; a token is  CHARS[PUNCT][=pinyin][/context gloss[//char gloss//char gloss]]
#   a leading "^" breaks the verse line before the token.
# Punctuation is editorial (the edition has none) and always trails the word before it.
# Pinyin defaults to the glossary's first reading; every polyphone states its reading here, and so does
# every character not yet in the glossary.
# Passages. Zhu Xi prints the book as one chapter (舊說凡一章) and divides it into sections; his heading
# says 今分為十七節, but the copy prints eighteen ○ breaks, and we number the eighteen printed sections
# as passages 10.1–10.18 (the familiar finer numbering of modern editions runs to 27). In this half:
# 10.1 = units 0–1, 10.2 = 2–3, 10.3 = 4–7, 10.4 = 8–12, 10.5 = 13–15, 10.6 = 16–26, 10.7 = 27–28.
# Quotation marks balance within every unit (the only speech in this half, 賓不顧矣, sits in unit 7).
# Readings decided: 朝 cháo 'court' throughout (units 1, 2, 26 ×2; Zhu Xi 直遙反，下同); 便便 pián pián
# (旁連反); 與 yǔ 'with' (units 2, 5) and 與與 yú yú (平聲; Zhu Xi allows 如字 too); 齊 zī in 攝齊 (11,
# 音咨) and zhāi 'to fast' (27, 28; 側皆反); 食 shí in 變食 (28; Zhu Xi gives no 音嗣 there); 勝 shēng
# 'to bear' (13; Zhu Xi 平聲 — the word differs from shèng 'to overcome', so the old reading is kept);
# 長 cháng in 20 and 21 (Zhu Xi marks 21 去聲, zhàng 'in length'; modern practice reads cháng, the note
# says so); 去 qù (23; Zhu Xi 上聲 = qǔ; modern practice, as the glossary entry already says); 殺 shài
# (24, 去聲 'to taper'); 有 yòu 'and' in 一身有半 (as 2.4 十有五); 侃侃 kǎn kǎn (Zhu Xi 苦旦反, a
# departing tone; modern kǎn); 踧踖 cù jí; 躩 jué; 擯 bìn; 襜 chān; 閾 yù; 屏 bǐng; 蹜蹜 sù sù; 紺 gàn;
# 緅 zōu; 麑 ní; 降 jiàng; 冠 guān (noun); 衣 yī (noun) throughout; 為 wéi; 中 zhōng (中門, verb 'stand
# in the middle of', no reading note); 唯 wéi; 召 zhào; 使 shǐ; 復 fù; 沒 mò.
# Glyphs kept as printed: 顔 (12, so 顔色 is a new key beside 顏色), 䙝 (17, 20; = 褻 xiè), 𤣥 (25, U+24965,
# = 玄 xuán), 黃.
# Bound: 孔子, 恂恂, 便便, 大夫, 侃侃, 誾誾, 踧踖, 與與, 鞠躬, 顔色, 怡怡, 蹜蹜, 愉愉, 君子, 帷裳 (a term:
# the full-width skirt), 吉月 (the first of the month, not 'a lucky month'), 明衣 (a term: the robe after
# bathing). Not bound, meaning what their parts mean: 鄉 | 黨 (as 6.3), 宗 | 廟, 朝 | 廷, 公 | 門, 容 | 色,
# 享 | 禮, 私 | 覿, 䙝 | 服, 䙝 | 裘, 絺 | 綌, 朝 | 服, 寢 | 衣, 狐 | 貉, 復 | 命.
# Collation (first witness Ruan 1816 KR1h0004, second He Yan SBCK KR1h0005): noted where it bears on the
# wording — He Yan 左右其手 (unit 5, adds 其); 如有循也 (13, adds 也); 縝 for 袗 and 必表而出 without 之
# (18); 齋必有明衣布也 (27, adds 也). Ruan has no sense-bearing variant in this half. Not noted (graphic):
# 郷 賔 𣸪 䒭 爲 狢 惟(帷) 玄 齋 䄡 顏. No misprint found.

UNITS_A = [
# ---------------- 10.1 ----------------
dict(pas="10.1", w="孔子/Master Kong | 於/in | 鄉=xiāng/(his) district | 黨，=dǎng/(and) village | ^恂恂=xún xún/earnest and plain//earnest, truthful//earnest, truthful | 如/(the look of) | 也，/(assertion) | ^似=sì/seeming | 不/not | 能/able | 言/to speak | 者。/one who (is)",
  l="Master Kong, in district and village,\nearnest and plain he was,\nseeming like one unable to speak.",
  i="Among the people of his home district, Master Kong was earnest and plain, as though speaking did not come easily to him.",
  n="The book is named 鄉黨 from its opening words. Zhu Xi prints it as a single chapter (舊說凡一章, 'the old account has it as one chapter'; He Yan's heading also says 凡一章) and divides it into sections; his heading says seventeen, but his copy marks eighteen, and we number those eighteen as passages (the finer numbering used in many modern editions runs to twenty-seven). Almost all of it describes the Master's bearing, dress, food and conduct rather than his sayings. Zhu Xi's heading quotes Yang Shi: the Way the sage speaks of never leaves daily use, so his disciples watched his every movement and recorded it in detail; and Yin Tun: how eager the disciples were to learn — there was nothing in the sage's looks, words or movements they did not carefully write down for later ages, so that reading it now he seems to stand before our eyes; yet the sage did not do these things stiffly — with virtue at its fullness, every movement fits the rites of itself, and a learner who wants to steep himself in the sage should seek him here. 孔子 'Master Kong', as outsiders name him: the book describes him from without. 鄉 and 黨 are units of local organisation (Zhu Xi on 6.3: 12,500 and 500 households); here, he says, they stand for the place where his elders and his clan live (父兄宗族之所在). 恂 xún (Zhu Xi: 相倫反): Zhu Xi glosses 恂恂 'the look of truthfulness and substance' (信實之貌); He Yan's Wang Su, 'gentle and respectful' (溫恭之貌). X如也 'X-like, he was' — a reduplicated descriptive word, 如 'in the manner of', and the assertion 也 — is the pattern of this whole book. 似…者 'like one who…'. Zhu Xi: he seemed unable to speak because he was humble and yielding and did not put himself ahead of others on account of his worth or knowledge."),
dict(w="其/he | 在/(when) at | 宗/the ancestral | 廟/temple | 朝=cháo/(or) the court's | 廷，=tíng/hall | ^便便=pián pián/clearly, fluently//fluent//fluent | 言，/spoke | ^唯=wéi/only | 謹/carefully | 爾。/(and that was all)",
  l="When he was at the ancestral temple or at court,\nhe spoke clearly and fully,\nonly carefully.",
  i="But in the ancestral temple and at court his speech was clear and full, and every word of it careful.",
  n="朝 here is cháo 'court' (Zhu Xi: 直遙反, and so in the passages that follow), not zhāo 'morning'; 廷 tíng is the court's open hall. 便便 is read pián pián (Zhu Xi: 旁連反), not biàn 'convenient': Zhu Xi glosses it 辯也 'clear, discriminating in speech'. 唯…爾 'only…, that is all': 爾 here is not 'you' but a final particle, 'just so'. Zhu Xi: the ancestral temple is where the rites and laws are kept, the court is where government issues; there speech cannot be unclear, so he asked about everything in detail and said all that needed saying — only carefully, never loosely. He Yan's Zheng Xuan agrees: though fluent, he was careful and respectful (雖辦而謹敬, 辦 there for 辯). Zhu Xi sums up the section: it records how the Master's speech and looks differed in his home district, in the temple and at court."),
# ---------------- 10.2 ----------------
dict(pas="10.2", w="朝，=cháo/at court | 與=yǔ/with | 下/the lower | 大夫=dà fū/grandees | 言，/speaking | 侃侃=kǎn kǎn/forthright//forthright//forthright | 如/(the look of) | 也；/(assertion) | ^與=yǔ/with | 上/the upper | 大夫=dà fū/grandees | 言，/speaking | 誾誾=yín yín/mild yet unyielding//mild but firm in argument//mild but firm in argument | 如/(the look of) | 也。/(assertion)",
  l="At court, speaking with the lower grandees, he was forthright;\nspeaking with the upper grandees, he was mild but unyielding.",
  i="At court, before the lord appeared, he talked frankly and directly with the lower grandees, and with the upper grandees agreeably but without giving way.",
  n="Zhu Xi: this is at court before the lord has come out to hold audience (此君未視朝時也). He cites the Royal Regulations (王制): a feudal lord's upper grandees are his ministers (卿), and his lower grandees number five. He takes his glosses from Xu Shen's Shuowen (許氏說文): 侃侃 'firm and straight' (剛直), 誾誾 'agreeable, yet remonstrating' (和悅而諍). He Yan's Kong Anguo reads them otherwise: 侃侃 'easy and cheerful' (和樂之貌), 誾誾 'balanced and upright' (中正之貌). 侃 is kǎn in modern practice (Zhu Xi spells it 苦旦反, a departing tone); 誾 yín (魚巾反). 與 yǔ 'with'."),
dict(w="君/the lord | 在，/present | ^踧踖=cù jí/reverent and uneasy//uneasy//reverent | 如/(the look of) | 也，/(assertion) | ^與與=yú yú/measured, composed in bearing//measured//measured | 如/(the look of) | 也。/(assertion)",
  l="The lord present,\nreverent and uneasy he was,\nmeasured and composed he was.",
  i="Once the lord was there, he was respectful to the point of unease, yet his bearing kept its proper measure.",
  n="君在 'the lord present': Zhu Xi and He Yan's Ma Rong both say this is when the lord holds audience (視朝). 踧踖 cù jí (Zhu Xi spells them 子六反, 子亦反): Zhu Xi, 'the look of one respectful and not at ease' (恭敬不寧之貌); Ma Rong, 'respectful'. 與與 yú yú (Zhu Xi: 平聲, or read as the ordinary word, yǔ): Zhu Xi and Ma Rong alike gloss it 'the look of deportment just as it should be' (威儀中適之貌); Zhu Xi adds Zhang Zai's view, that 與與 means never forgetting to face toward the lord, and says that reading also works. Zhu Xi sums up: this section records how the Master differed at court in serving those above and dealing with those below."),
# ---------------- 10.3 ----------------
dict(pas="10.3", w="君/the lord | 召=zhào/summoned (him) | 使=shǐ/to have (him) | 擯，=bìn/receive the guests | ^色/his face | 勃=bó/changed | 如/(the look of) | 也，/(assertion) | ^足/his feet | 躩=jué/moved in measured turns | 如/(the look of) | 也。/(assertion)",
  l="When the lord called him to receive the guests,\nhis face changed,\nhis feet moved in measured turns.",
  i="When the lord called on him to receive visitors from another state, his expression altered and his step became measured and ceremonious.",
  n="擯 bìn (Zhu Xi: 必刃反): Zhu Xi, the man the lord of the host state sends out to receive guests; He Yan's Zheng Xuan, when there were guests he was sent to meet them. 勃 bó: Zhu Xi, 'the look of a changed colour' (Kong Anguo: his colour always changed). 躩 jué (Zhu Xi: 驅若反): Zhu Xi and He Yan's Bao Xian gloss it 盤辟貌 / 槃辟貌, the look of turning and winding steps, the gait of ceremony. Zhu Xi: both come from respect for the lord's command."),
dict(w="揖/bowing to | 所/those | 與=yǔ/with (whom) | 立，/(he) stood | ^左/to the left | 右=yòu/(and) to the right | 手，/(went) his hands | ^衣=yī/his robe | 前/front | 後，/(and) back | 襜=chān/hanging trim | 如/(the look of) | 也。/(assertion)",
  l="Bowing to those he stood with,\nhis hands went left and right,\nhis robe front and back hung trim.",
  i="As he bowed to the men standing with him in the line, moving his clasped hands now to the left, now to the right, the skirts of his robe front and back stayed neatly in place.",
  n="所與立 'those with whom he stood': Zhu Xi, the others serving as receivers with him. He explains: the receivers number half the rank-count (命數) — for a high duke of nine ranks, five men — and they pass the message along in order; bowing to the man on his left he moved his hands to the left, to the man on his right, to the right. He Yan's Zheng Xuan says the same, adding that with each bow down and up (一俛一仰) the robe swung front and back. 左 and 右 are verbs here, 'to the left, to the right'. He Yan's text reads 左右其手 'turned his hands left and right', with 其. 襜 chān (Zhu Xi: 赤占反), 'the look of neatness' (整貌)."),
dict(w="趨=qū/hastening | 進，/forward | ^翼=yì/winged, spread like wings | 如/(the look of) | 也。/(assertion)",
  l="Hastening forward,\nwinglike he was.",
  i="When he hurried forward, his clasped arms were held out like the wings of a bird.",
  n="趨 is the quick, short-stepped walk of respect. Zhu Xi: he hastened forward with his arms spread in a clasp, upright and fine, like a bird spreading its wings (張拱端好如鳥舒翼). He Yan's Kong Anguo: 翼如 speaks of being upright and fine (端好)."),
dict(w="賓=bīn/the guest | 退，/having withdrawn | ^必/(he) always | 復/reported back (on) | 命，/the charge | 曰：「/saying | ^賓=bīn/the guest | 不/no longer | 顧=gù/looks back | 矣。」/(and so it is)",
  l="The guest having withdrawn,\nhe always reported back on his charge, saying:\n“The guest no longer looks back.”",
  i="Once the visitor had gone, he never failed to report to the lord: “The guest has left and is not looking back.”",
  n="復命 'to return the command', to report that a charge has been carried out. He Yan's Kong Anguo: he reported to the lord that the guest had gone. 顧 gù 'to turn the head, look back': a guest no longer looking back has gone, and the ceremony of seeing him off is over. Zhu Xi: he reported it to release the lord from his respectful attendance (紓君敬也). Zhu Xi sums up: this section records the Master's bearing when he served his lord as receiver of guests."),
# ---------------- 10.4 ----------------
dict(pas="10.4", w="入/entering | 公/the duke's | 門，/gate | ^鞠躬=jū gōng/bent low//to bend//the body | 如/(the look of) | 也，/(assertion) | ^如/as if | 不/(it did) not | 容。/hold (him)",
  l="Entering the duke's gate,\nbent low he was,\nas if it could not hold him.",
  i="Going in through the gate of the duke's palace, he drew his body in and bowed low, as though there were not room for him to pass.",
  n="Zhu Xi: 鞠躬 is bending the body; the duke's gate is high and wide, yet he went as if it could not take him in — respect at its height. He Yan's Kong Anguo: 'drawing in the body' (斂身). 容 here is 'to hold, to have room for', not 'bearing'."),
dict(w="立/standing | 不/(he did) not | 中=zhōng/(stand) in the middle of | 門，/the gateway | ^行=xíng/walking | 不/(he did) not | 履/tread on | 閾。=yù/the threshold",
  l="Standing, he did not stand in mid-gate;\nwalking, he did not tread on the threshold.",
  i="He would not stop in the middle of the gateway, and in passing through he never stepped on the sill.",
  n="中門 'to be in the middle of the gate' (Zhu Xi: 中於門): between the side-posts (棖) and the central post (闑), where the lord goes in and out. 閾 yù (Zhu Xi: 于逼反) is the threshold (Zhu Xi and He Yan's Kong Anguo: 門限). Zhu Xi cites the rites: officers entering and leaving the lord's gate pass on the right of the central post and do not step on the threshold. He quotes Xie Liangzuo (謝氏): to stand in the middle of the gate would be to take the place of honour; to tread on the threshold would be careless (不恪)."),
dict(w="過=guò/passing | 位，/the (lord's) place | ^色/his face | 勃=bó/changed | 如/(the look of) | 也，/(assertion) | ^足/his feet | 躩=jué/moved in measured turns | 如/(the look of) | 也，/(assertion) | ^其/his | 言/words | 似=sì/seemed | 不/not | 足/enough | 者。/(like one whose)",
  l="Passing the lord's place,\nhis face changed,\nhis feet moved in measured turns,\nhis words seemed to fall short.",
  i="As he went past the place where the lord stands, though it stood empty, his expression changed and his step grew careful, and he spoke as though he had scarcely words enough.",
  n="位 here is the lord's place, empty at this moment. Zhu Xi: it lies between the gate and the screen wall, where the lord stands (the spot called 宁); even though the lord is not there, one passing it must show respect and not slight it because it is empty; his words seemed not enough because he did not dare speak freely. He Yan's Bao Xian: passing the lord's empty place. 似…者 'like one who…', as in 10.1."),
dict(w="攝/gathering up | 齊=zī/the hem | 升/(he) went up (to) | 堂，/the hall | ^鞠躬=jū gōng/bent low | 如/(the look of) | 也，/(assertion) | ^屏=bǐng/holding in | 氣/his breath | 似=sì/as though | 不/not | 息=xī/breathing | 者。/(one who were)",
  l="Holding up his hem, he went up to the hall,\nbent low he was,\nholding his breath as though not breathing.",
  i="Lifting the hem of his robe as he climbed the steps to the hall, he bent his body low and kept his breath in, as if he had stopped breathing.",
  n="齊 is read zī here (Zhu Xi: 音咨), 'the lower hem of a garment' (Zhu Xi: 衣下縫; He Yan's Kong Anguo: 衣下曰齊); 攝 is 'to lift' (Zhu Xi and Kong: 摳). Zhu Xi: the rites say that, about to go up to the hall, one lifts the robe with both hands a foot off the ground, for fear of treading on it, stumbling, and losing one's composure. 屏 bǐng 'to hold in, store away' (Zhu Xi: 藏也); 息 is the breath going in and out of the nose; near the most honoured one, his breathing too was grave. Kong Anguo: all this is great care."),
dict(w="出，/coming out | 降=jiàng/(and) going down | 一/one | 等，=děng/step | ^逞=chěng/(he) let go | 顔色，=yán sè/his countenance | 怡怡=yí yí/(and was) at ease, cheerful//glad//glad | 如/(the look of) | 也；/(assertion) | ^沒=mò/at the end of | 階，=jiē/the steps | 趨=qū/hastening | 進，/forward | 翼=yì/winglike | 如/(the look of) | 也；/(assertion) | ^復/back in | 其/his | 位，/place | 踧踖=cù jí/reverent and uneasy | 如/(the look of) | 也。/(assertion)",
  l="Coming out and going down one step,\nhe let his face relax, and was at ease;\nat the foot of the steps, hastening forward, winglike he was;\nback in his place, reverent and uneasy he was.",
  i="Coming out, once he was a step down he let his breath go and his face eased into contentment; at the foot of the steps he hurried forward with his arms spread like wings; and back in his own place he was once more respectful and watchful.",
  n="等 děng is a step of the stair (Zhu Xi: 階之級). 逞 chěng 'to let loose' (Zhu Xi: 放也): as he drew away from the one he honoured, he let out his breath and relaxed his face; 怡怡 'glad and easy' (和悅). 顔 is the edition's form of 顏. 沒階 'to the end of the steps' (沒 mò 'to come to an end'; Zhu Xi and Kong Anguo: 盡). 趨 is to hasten to his place. Zhu Xi: in his place he was still 踧踖 — what remained of his respect. He Yan's Kong Anguo takes 其位 as the place he had passed on the way in (来時所過位). Zhu Xi quotes Lu Deming (陸氏): the base text has no 進 after 趨, and the common copies that have it are wrong; Zhu Xi's own text prints it all the same, as do both our witnesses. Zhu Xi sums up: this section records the Master's bearing at court."),
# ---------------- 10.5 ----------------
dict(pas="10.5", w="執/holding | 圭，=guī/the jade tablet | ^鞠躬=jū gōng/bent low | 如/(the look of) | 也，/(assertion) | ^如/as if | 不/not | 勝。=shēng/(able to) bear (it) | ^上/(held) high | 如/as (in) | 揖，/a bow | 下/(held) low | 如/as (in) | 授；=shòu/handing over | ^勃=bó/changed | 如/(the look of) | 戰/trembling | 色，/(in his) face | ^足/his feet | 蹜蹜=sù sù/in short, close steps//to step short//to step short | 如/as if | 有/there were (something) | 循。/to follow",
  l="Holding the tablet,\nbent low he was,\nas if he could not bear it.\nHigh, as in bowing; low, as in handing over;\nhis face changed, as if trembling;\nhis feet in short steps, as if following something.",
  i="When he carried the jade tablet as envoy, he bent low as though it were too heavy for him; he held it no higher than in a bow and no lower than in passing a thing to someone; a look of awe came into his face, and he walked with short, close steps, his feet hardly leaving the ground, as if following along something.",
  n="圭 guī, Zhu Xi says, is the jade tablet a feudal lord receives as his charge (命圭); when he sends to visit a neighbouring state, a grandee carries it to establish good faith. He Yan's Bao Xian likewise: sent as the lord's envoy to a neighbouring state, he carried the lord's tablet. 勝 is read shēng 'to bear, to be equal to' (Zhu Xi: 平聲), not shèng 'to overcome'. Zhu Xi: carrying his lord's vessel, light as it is, as if he could not bear it — respect and care at their height; 上如揖，下如授 means he held the tablet level, his hands level with his heart, no higher than in a bow, no lower than in handing over. He Yan's Zheng Xuan explains the pair otherwise: 'high, as in a bow', because in handing over the jade one should be respectful; 'low, as in handing over', because one does not dare forget the rites. 戰色 'a face that trembles', Zhu Xi: fearful in look. 蹜 sù (Zhu Xi: 色六反): 蹜蹜 is lifting the feet in short, cramped steps; 如有循, Zhu Xi says, is what the Record calls 'raising the front of the foot and dragging the heel' (舉前曳踵) — walking without the feet leaving the ground, as if going along something. He Yan's text ends 如有循也, with 也."),
dict(w="享=xiǎng/(at) the presentation | 禮，/rite | ^有/(he) had | 容/an (easy) bearing | 色。/(and) countenance",
  l="At the rite of presentation,\nhe had an easy bearing and look.",
  i="At the presentation of gifts that followed, his face was open and pleasant.",
  n="享 xiǎng 'to present' (Zhu Xi and He Yan's Zheng Xuan: 獻也). Zhu Xi: after the visit of state (聘) comes the presentation, with a tablet and a jade disc (圭璧) and goods set out in the courtyard (庭實) — Zheng Xuan says the same, citing the Rite of Visits (聘禮). 有容色 'had bearing and countenance': Zhu Xi glosses it 'at ease' (和也), and quotes the Yili: 'let the breath out and fill the face' (𤼵氣滿容)."),
dict(w="私=sī/(at) the private | 覿，=dí/audience | ^愉愉=yú yú/cheerful, glad//glad//glad | 如/(the look of) | 也。/(assertion)",
  l="At the private audience,\ncheerful he was.",
  i="And when he met the host lord privately, with gifts of his own, he was openly glad.",
  n="覿 dí 'to see, to have audience' (He Yan's Zheng Xuan: 見也). Zhu Xi: 私覿 is seeing the host lord with gifts of one's own (以私禮見); 愉愉 is more at ease still. Zheng Xuan: after the presentation he saw the lord with his private gifts; 愉愉 is a pleasant face. Zhu Xi sums up: this section records the rites the Master observed when visiting a neighbouring state for his lord. He then quotes Chao Yuezhi (晁氏): Confucius held office in Lu from the ninth year of Duke Ding until the thirteenth, when he went to Qi, and in that time there were no court visits or embassies at all; so perhaps the two items on receiving guests and carrying the tablet only record what Confucius said these rites should be."),
# ---------------- 10.6 ----------------
dict(pas="10.6", w="君子/the gentleman | 不/did not | 以/use | 紺=gàn/dark red-blue | 緅=zōu/(or) crimson | 飾。=shì/(as) trimming",
  l="The gentleman did not use dark red-blue or crimson for trimming.",
  i="The gentleman would not have his collars and cuffs edged in a dark red-shot blue or in crimson.",
  n="Zhu Xi: 君子 here means Confucius. 紺 gàn (古暗反) is, he says, a deep blue with a glint of red (深青揚赤色), the colour of the clothes for fasting; 緅 zōu (側由反) is crimson (絳色), used in the three years' mourning to trim the 練 dress (練服) put on at a later stage of it; 飾 is the edging of the collar (領縁). He Yan's Kong Anguo: cloth dipped once (in the dye) is called 緅; 飾 is the edging of collar and sleeves; 紺 is the full colour of fasting clothes, and to trim with it would look like fasting dress; at the 練 stage of the three years' mourning clothes are trimmed with 緅, and to trim with it would look like mourning; so neither was used."),
dict(w="紅=hóng/red | 紫=zǐ/(and) purple | 不/(he did) not | 以/use | 為=wéi/to make | 䙝=xiè/informal, at-home | 服。/clothes",
  l="Red and purple he did not use for clothes worn at home.",
  i="He would not wear red or purple even in his clothes for home.",
  n="䙝 is the edition's form of 褻 xiè 'intimate, for private wear'. 服 'clothing'. Zhu Xi: red and purple are mixed colours (閒色), not the proper ones, and are close to women's dress; 䙝服 is what one wears at home, and if he would not use them even for that, it follows that he would not use them for court or sacrifice. He Yan's Wang Su: home clothes are not for public occasions; when not even these are made in such colours, they have no place at all in formal dress."),
dict(w="當=dāng/in | 暑，=shǔ/the hot season | ^袗=zhěn/unlined | 絺=chī/fine kudzu | 綌，=xì/(or) coarse kudzu | ^必/(he) always | 表=biǎo/set (it) outside | 而/and | 出/brought out | 之。/it",
  l="In the hot season,\nin unlined fine or coarse kudzu,\nhe always wore it on the outside, over something.",
  i="In hot weather, wearing a single layer of fine or coarse kudzu cloth, he always had something on underneath.",
  n="Zhu Xi: 袗 zhěn is 'single, unlined' (單也); kudzu (葛) cloth that is fine is 絺 chī, coarse 綌 xì. 表而出之, he says, means putting on an under-robe first and then wearing the kudzu over it on the outside, so that the body should not show — as in the Odes' 'covering that crinkled kudzu' (蒙彼縐絺). He Yan's text reads 縝 for 袗 and 必表而出 without 之; his Kong Anguo reads it the other way about: in the heat he wore single clothes, and when he went out he put an upper garment on top (加上衣)."),
dict(w="緇=zī/(with) a black | 衣，=yī/robe | 羔=gāo/lamb | 裘；/fur | ^素/(with) a white | 衣，=yī/robe | 麑=ní/fawn | 裘；/fur | ^黃=huáng/(with) a yellow | 衣，=yī/robe | 狐/fox | 裘。/fur",
  l="With a black robe, lambskin;\nwith a white robe, fawnskin;\nwith a yellow robe, fox fur.",
  i="His black robe went with lambskin, his white robe with fawnskin, his yellow robe with fox fur: each robe matched the fur beneath it.",
  n="Zhu Xi: 緇 zī is black, and the lamb's fur is the skin of a black lamb; 麑 ní (研奚反) is a fawn, and white; the fox is yellow. The robe 衣 yī is worn over the fur (衣以裼裘) and is meant to match it. He Yan's Kong Anguo: the colours of the outer and inner garments match."),
dict(w="䙝=xiè/the at-home | 裘/fur | 長，=cháng/long | ^短=duǎn/shortening | 右=yòu/the right | 袂。=mèi/sleeve",
  l="The home fur: long,\nthe right sleeve shortened.",
  i="For wear at home his fur was long, but he had the right sleeve made shorter.",
  n="Zhu Xi: long because he wanted it warm; the right sleeve short to make work easier. He Yan's Kong Anguo says the same. 短 is a verb here, 'to make short'; 袂 mèi is the sleeve."),
dict(w="必/(he) always | 有/had | 寢/a sleeping | 衣，=yī/garment | ^長=cháng/long | 一/one | 身/body | 有=yòu/and | 半。=bàn/a half",
  l="He always had a sleeping garment,\nlong, a body and a half.",
  i="He always had a nightrobe, one and a half times his own length.",
  n="長 is read cháng here by modern practice; Zhu Xi marks it 去聲 (zhàng, 'in length'). 有 yòu 'and' joins the numbers (as 2.4 十有五). Zhu Xi: when fasting, reverence comes first; one cannot sleep undressed, nor sleep in the bright robe (10.7), so there was a separate sleeping garment, and the extra half was probably (蓋) to cover the feet. He quotes Master Cheng: this slip is out of place (錯簡) and belongs after 齊必有明衣布 (10.7); Zhu Xi adds that then this item would join the bright robe and the changed food as one kind, and the at-home fur and the fox and raccoon-dog furs would stand together as another. He Yan's Kong Anguo: it is what is now called a 被, a coverlet."),
dict(w="狐/fox | 貉/(and) raccoon-dog (furs) | 之/(clause marker) | 厚/thick | 以/(were) for | 居。/(being at) home",
  l="The thick furs of fox and raccoon-dog were for home.",
  i="At home he wore the thick furs of fox and raccoon-dog.",
  n="Zhu Xi: the fur of fox and raccoon-dog is deep, warm and thick; at home he chose it for comfort. He Yan's Zheng Xuan: he wore them at home for receiving guests. 狐貉之厚 'the thick ones among fox and raccoon-dog': 之 joins the furs to the quality picked out."),
dict(w="去=qù/having put off | 喪，=sāng/mourning | ^無/there was nothing | 所/that | 不/(he did) not | 佩。=pèi/wear at his girdle",
  l="Mourning put off,\nthere was nothing he did not wear at his girdle.",
  i="Except when in mourning, he wore every pendant at his girdle.",
  n="去 'to put off, set aside': Zhu Xi marks it 上聲 (qǔ); we give the modern qù, as elsewhere (He Yan's Kong Anguo: 去，除也). 喪 sāng 'mourning'. 佩 pèi 'to wear hung from the girdle'. Zhu Xi: the gentleman does not part with his jade without cause, and the bodkin (觽) and whetstone and the like are all worn too. Kong Anguo: when not in mourning, he wore all that should be worn."),
dict(w="非/(if) not | 帷裳，=wéi cháng/the curtain-skirt//curtain//skirt | ^必/(he) always | 殺=shài/tapered | 之。/it",
  l="If not the curtain-skirt,\nhe always had it tapered.",
  i="Apart from the full-width skirt worn at court and at sacrifices, his skirts were always cut narrower at the waist.",
  n="殺 is read shài here (Zhu Xi: 去聲), 'to reduce, to taper', not shā 'to kill'. 帷裳 'the curtain-skirt': Zhu Xi explains that the skirt of court and sacrificial dress is made of full widths of cloth like a curtain (帷), pleated at the waist and with no tapered seams at the sides; other garments, such as the 'deep robe' (深衣), whose waist is half the width of the hem, have no pleats but tapered seams. He Yan's Wang Su: garments always have tapered seams; only the curtain-skirt has none.."),
dict(w="羔=gāo/lamb | 裘/fur | 𤣥=xuán/(and) black | 冠，=guān/cap | ^不/(he did) not | 以/use (them) | 弔。=diào/(to pay) condolence",
  l="Lambskin and a black cap\nhe did not wear to condole.",
  i="He never went to offer condolences in lambskin and a black cap.",
  n="𤣥 (U+24965) is the edition's form of 玄 xuán 'dark, black'. 弔 diào 'to condole with mourners'. Zhu Xi and He Yan's Kong Anguo say the same: mourning takes white as its keynote, auspicious occasions black (喪主素，吉主𤣥); Zhu Xi adds that in condoling one must change dress, so as to grieve for the dead, and Kong that good and ill fortune have different dress."),
dict(w="吉月，=jí yuè/(on) the first of the month//auspicious//month | ^必/(he) always | 朝=cháo/court | 服/(in) dress | 而/and | 朝。=cháo/attended court",
  l="On the first of the month,\nhe always put on court dress and went to court.",
  i="On the first day of each month he always went to court, dressed for it.",
  n="吉月 is the first day of the month (Zhu Xi and He Yan's Kong Anguo: 月朔也), not 'a lucky month'. 朝 cháo both times: 'court dress' and 'to attend court'. Kong Anguo: the court dress is the deerskin-cap dress (皮弁服). Zhu Xi: the Master did this in Lu after he had retired from office. He sums up: this section records the rules of the Master's dress; and he quotes Su (蘇氏): these are miscellaneous records of the lesser rites left in the writings of the Kong family, and not only about Confucius."),
# ---------------- 10.7 ----------------
dict(pas="10.7", w="齊，=zhāi/(when) fasting | ^必/(he) always | 有/had | 明衣=míng yī/a bright (clean) robe//bright//garment | 布。=bù/(of) cloth",
  l="When fasting,\nhe always had a bright robe, of cloth.",
  i="For the fast before a sacrifice he always kept a clean robe of plain cloth.",
  n="齊 is read zhāi here and in the next unit (Zhu Xi: 側皆反), 'to fast, to purify oneself before a sacrifice' (= 齋; He Yan's text writes 齋). Zhu Xi: when fasting one must wash and bathe, and on finishing the bath put on the bright robe, which keeps the body bright and clean; it is made of cloth. He adds that after this a slip — the sleeping garment of the previous section (10.6) — has dropped out (此下脫前章寢衣一簡). He Yan's Kong Anguo: a cloth robe for after washing and bathing. He Yan's text reads 齋必有明衣布也, with a final 也."),
dict(w="齊=zhāi/fasting | 必/(he) always | 變/changed | 食，=shí/(his) food | ^居/(where he) stayed | 必/(he) always | 遷/moved | 坐。=zuò/(his) seat",
  l="Fasting, he always changed his food;\nwhere he stayed, he always moved his seat.",
  i="While fasting he always changed what he ate, and moved from where he usually sat.",
  n="食 is shí 'food' here; Zhu Xi gives it no reading note. Zhu Xi: changing the food means not drinking wine and not eating strong-smelling plants (不茹葷); moving the seat means changing one's usual place. He Yan's Kong Anguo: changing the usual food, and changing the usual place. Zhu Xi sums up: this section records how carefully the Master kept the fast; and he quotes Yang Shi: fasting is how one comes into contact with the spirits, so one makes oneself clean to the utmost and changes what is usual, to be wholly reverent."),
]
