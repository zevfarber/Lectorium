# Analects pipeline — open questions for the owner

## Legge 1861 is named in the plan but could not be read from here (pilot, 2026-10-12)
The plan names the Chinese text of Legge, *The Chinese Classics* vol. 1 (1861). Its scans (archive.org
`chineseclassics01legg_0`) cannot be fetched from the pipeline's shell, and the OCR text does not carry
the Chinese of the text pages. Decided meanwhile: the text is Zhu Xi's 論語集注 from the Siku Quanshu
copy (1782) as transcribed by Kanripo, collated against two further pre-1930 printings; this is the
received text Legge printed, and the source statement says so without claiming a check against
Legge's pages. If you want Legge's pages checked, a session with browser access can do the Daodejing
treatment (page-image spot-check per batch).

## Disputed readings where the pilot follows Zhu Xi (pilot, 2026-10-12)
1.7 賢賢易色 ("esteeming worth in exchange for [love of] beauty"), 1.8 學則不固 (one thought with
不重, against Kong Anguo's "learning, he is not blinkered"), 1.13 因不失其親 (因 = depend on, 宗 = take
as head). Each note names the alternative. Revisit only if you prefer the older commentary as the
default crib.

## Glossary kept separate from the Daodejing's (pilot, 2026-10-12)
The two books share many characters but use some in different senses (德 "virtue" here, "potency" in
the Daodejing). Decided: a separate `analects-glossary.json`. Say if you would rather have one Chinese
glossary for the library.

## Juan-end running heads in the source archive (analects-02, 2026-11-17)
`archive_analects.py` strips the running head that opens each juan but not the one that closes it, so
the archived lemma lists of books 2, 4, 6, 8, 10, 12, 14, 16, 18 and 20 end with 論語卷一…論語卷十 (the
`lemmata` counts in `parts.json` include it). Decided meanwhile: the pinned source stays as archived,
and `build_analects.py` skips a lemma that is exactly 論語卷N; book 2 has 39 units against 40 pinned
lemmata. If you would rather fix the archive script and re-pin those ten books, say so.

## 2.17 是知也 read zhī with Zhu Xi (analects-02, 2026-11-17)
Many readers take the last 知 as 智 zhì "this is wisdom". Zhu Xi marks no separate reading and glosses
it as knowing (不害其為知), so the text reads zhī "this is knowing" and the note gives the other.

## Misprint corrected in 3.9: 把 → 杞 (analects-03, 2026-11-17)
Under the rule of 2026-11-06 (README 5b). The Siku copy as transcribed by Kanripo prints 把不足徵也
(and 把夏之後 in Zhu Xi's comment); Ruan 1816 and He Yan SBCK both have 杞, and only 杞 (the state of
the Xia heirs) makes sense. The pinned source is unchanged; the correction is recorded in
`emend.json` (new — the Analects had no emendation list), and `build_analects.py` applies it in the
text gate and requires the unit's note to open "The print has 把, a misprint for 杞, corrected here."
Nothing waits on you; say if you would rather the reading text keep 把.

## 3.8 盻 kept, read pàn (analects-03, 2026-11-17)
The print has 盻 (xì 'to glare') in 美目盻兮; Zhu Xi glosses it 普莧反, i.e. 盼 pàn, which Ruan
prints. Treated as the edition's graphic form, not a misprint: the text keeps 盻, the pinyin is pàn,
and the note says so.

## 大 not in POLY (analects-03, 2026-11-17)
大 is read tài in 大廟 and 大師 (Zhu Xi 大音泰), stated on every occurrence in Book 3; but 1.12 and
2.22 use 大 dà without an explicit reading, so 大 is not in the POLY set the build enforces. Later
books should state tài wherever it occurs.

## Misprint corrected in 4.14: 已 → 己 (analects-04, 2026-11-18)
Under rule 5b. The Siku copy as transcribed prints 不患莫已知 ('no one knows me' needs 己); the copy
confuses 己/已/巳 throughout, the Master Cheng saying Zhu Xi quotes on the line has 求其在己者, and the
first witness reads 己. Recorded in `emend.json`; the pinned source is unchanged. Nothing waits on you.

## 恕 rendered 'fellow-feeling' (analects-04, 2026-11-18)
4.15 忠恕 is 'wholeheartedness and fellow-feeling' (i: 'to be wholehearted, and to put yourself in the
other man's place'), following Zhu Xi's 推己之謂恕. Decided meanwhile as the house rendering for 恕
(it recurs in 5.12/15.24); say if you prefer another.

## 茍 kept as printed, read gǒu (analects-04, 2026-11-18)
4.4 prints 茍 (strictly a different character, jì) for 苟, as old prints commonly do; Zhu Xi's own
comment writes 苟. Treated as the edition's graphic form, like 盻 in 3.8: text keeps 茍, pinyin gǒu,
note says so.

## Misprint corrected in 5.9: 宰子 → 宰予 (analects-05, 2026-11-18)
Under rule 5b. The Siku copy as transcribed prints 宰子晝寢; Zhu Xi's own comment on the line names 宰予,
the Master goes on to call him 予 (於予與何誅), and both witnesses read 宰予. (Hu Yin, quoted by Zhu Xi,
also appears as 宰子 in this copy — the same 子/予 confusion.) Recorded in `emend.json`; pinned source
unchanged. Nothing waits on you; say if you would rather the reading text keep 宰子 'Master Zai'.

## Misprint corrected in 5.15: 已 → 己 (analects-05, 2026-11-18)
其行己也恭 'in conducting himself': the copy prints 已, as at 4.14; first witness reads 己. In `emend.json`.

## 巳 kept in 5.26, read yǐ (analects-05, 2026-11-18)
巳矣乎 is printed with 巳 (also in Zhu Xi's comment); elsewhere this copy prints the particle as 已.
Treated as the edition's graphic form, like 茍 and 盻: text keeps 巳, pinyin yǐ, note says so, 巳 added
to POLY. Say if you would rather it be corrected to 已 under rule 5b.

## 輕 in 5.25 (analects-05, 2026-11-18)
The transcription of our Ruan witness (KR1h0004) sets 輕 in 衣輕裘 in round brackets, apparently marking
it as a suspected later addition. Zhu Xi and He Yan both have it; kept, and the note says so (hedged).

## 足 not in POLY yet (analects-05, 2026-11-18)
Book 5 has 足 jù 'excessive' (5.24 足恭, stated in the unit). 足 cannot join the POLY set the build
enforces until the zú occurrences in books 2–4 (analects-02 unit 16, analects-03 unit 12, analects-04
units 8 and 12) state =zú; left as is so published books are untouched. Same for 三 (5.19 Zhu Xi sàn,
printed sān).

## Older glossary entries with ';' inside brackets (analects-05, 2026-11-18)
The glossary review found that a ';' inside parentheses cuts the popup's first clause mid-bracket.
Fixed in all Book 5 entries; older entries with the same fault (其諸, 共, 殆, 禄, 車, 嗚呼, 辟, 盻, 杞)
were left untouched (broaden-only rule). A later run could move those semicolons outside the
brackets if you agree.

## 6.24 井有仁焉 read with Liu Mianzhi as 人 (analects-06, 2026-11-18)
Zai Wo's question 'if someone told him there was 仁 in the well': Zhu Xi quotes Liu Mianzhi 劉聘君 that
仁 should be 人 'a man (fallen in)'. The printed 仁 is kept in the text (a doubtful reading, not a clear
misprint, so rule 5b does not apply); the English follows Zhu Xi with 'a man', and the note gives the
print, Liu's reading and He Yan's 井有仁者焉. Say if you would rather the English keep 'humaneness'.

## 宋朝 read zhāo (analects-06, 2026-11-18)
6.14 宋朝 Prince Zhao of Song: pinyin zhāo; the note says cháo is also heard. Decided meanwhile.

## No quotation marks on 6.28's continuation units (analects-06, 2026-11-18)
The Master's answer in 6.28 runs over three units; since a unit cannot open with 「, the second and
third units (夫仁者… and 能近取譬…) carry no quotation marks, as with 5.x follow-ups.

## Passage numbering is Zhu Xi's 28 chapters (analects-06, 2026-11-18)
Zhu Xi joins 雍也可使南面 with 仲弓問子桑伯子 (6.1) and 子華使於齊 with 原思為之宰 (6.3), so our numbers run up
to two behind the 30-chapter numbering some editions use (Nanzi is 6.26, the mean 6.27, 博施 6.28). This
follows the conventions ("Zhu Xi's chapter breaks"); the parts.json passage count (28) agrees.

## Misprint corrected in 7.28: 已 → 己 (analects-07, 2026-11-18)
Under rule 5b. 人潔己以進 'a man purifies himself to come forward': the copy prints 已 (as at 4.14, 5.15,
6.28); the first witness reads 絜己. In `emend.json`; pinned source unchanged. Nothing waits on you.

## 祗 kept in 7.34, read qí (analects-07, 2026-11-18)
禱爾于上下神祗: the copy writes 祗 (properly zhī 'reverent') for 祇 qí 'earth spirits', in the text and in
Zhu Xi's comment (地曰祗); the first witness has 祇. Treated as the edition's graphic form, like 盻, 茍
and 巳: text keeps 祗, pinyin qí, note says so. Say if you would rather correct it under rule 5b.

## 葉公 read yè gōng, not shè gōng (analects-07, 2026-11-18)
Zhu Xi reads 葉 舒涉反 (shè), and the traditional reading 葉公 shè gōng is still common; we give the current
standard yè and the note (and glossary) give shè. Say if you prefer shè as the house reading.

## Smaller points left open (analects-07, 2026-11-18)
- 7.26 射: Zhu Xi's 食亦反 is noted as an older reading; we give shè.
- 7.32 文莫: follows Zhu Xi (莫 'perhaps'), with He Yan's 莫 = 無; the reading of 文莫 as one word
  'striving' (忞慔) is not mentioned. Say if you want it in the note.
- 7.16: the note cites the Lu reading 亦 for 易 as recorded by Lu Deming (經典釋文), which is not in the
  archive; the first witness's 亦 is the archived evidence.
- 孫 (xùn, 7.35) and 和 (hè, 7.31) are stated in Book 7 but not added to POLY, since earlier books use
  them with their first readings unstated.

## Misprint corrected in 8.4: 地 → 也 (analects-08, 2026-11-18)
Under rule 5b. 鳥之將死，其鳴也哀 'when a bird is about to die, its cry is mournful': the copy prints 其鳴地哀;
both witnesses read 也, and the parallel 其言也善 follows. In `emend.json`; pinned source unchanged. Nothing waits on you.

## build_analects.py now accepts CJK Extension B characters (analects-08, 2026-11-18)
8.7 士不可以不𢎞毅: the edition writes 𢎞 (U+22390, outside the Basic Multilingual Plane) for 弘. The build's
character patterns covered only the BMP, so they were widened; books 1–7 build exactly as before. The glyph is
kept as printed (pinyin hóng, glossary '= 弘'). If a reader's font lacks it, it may show as a box — say if you
would rather print 弘 with a note.

## 8.1 literal: 'Taibo — he can surely be called utmost virtue' (analects-08, 2026-11-18)
The l keeps the Chinese construction (a person 'called' 至德) so that 其可謂至德也已矣 reads the same in 8.1 and 8.20;
the i smooths it ('surely deserves to be called the utmost'). Say if you prefer 'a man of utmost virtue' in 8.1.

## Smaller points left open (analects-08, 2026-11-18)
- 8.14 不在其位不謀其政 recurs in Book 14, where Zhu Xi marks it 重出; its passage number there (14.26 or 14.27 —
  Zhu Xi's heading counts 47 chapters but 46 ○ starts are marked) is for the Book 14 run to settle.
- 8.2 君子篤於親…: Zhu Xi quotes Wu that it should be a separate chapter; kept in 8.2 as he prints it, note says so.
- 8.12 至 read as printed with Zhu Xi's suspicion that it should be 志 given in the note (doubtful, so not emended).
- 8.20 婦人: Zhu Xi reports Liu Shidu's view that the woman is Yi Jiang; 劉侍讀 left as 'Academician Liu', unidentified.
- Some commentator identifications (蘇氏 Su Shi, 晁氏 Chao Yuezhi, 稷 'Lord Millet', 內則 as a Record of Rites
  chapter) come from general knowledge, as in earlier books.

## Misprints corrected in 9.5 and 9.11: 子 → 予 (analects-09, 2026-11-18)
Under rule 5b. 9.5 匡人其如予何 'what can the men of Kuang do to me?' and 9.11 且予縱不得大葬，予死於道路乎: the copy
prints 子 for 予 in both (the same confusion as 宰子 at 5.9); Zhu Xi's own paraphrase (匡人其奈我何) and both
witnesses read 予. In `emend.json`; pinned source unchanged. Nothing waits on you.

## 牢 in 9.6 given as 'Lao' (analects-09, 2026-11-18)
牢曰 'Lao said': Zhu Xi identifies him as a disciple surnamed Qin 琴, courtesy name 子開 or (another account) 子張 — not
the well-known Zizhang. Since the text uses his personal name, the English says 'Lao' (as 'You' for 由). Say if you prefer
a courtesy name.

## Smaller points left open (analects-09, 2026-11-18)
- 9.11 病閒: given jiàn (modern reading); Zhu Xi marks 閒如字 — the note says so without naming a tone.
- 9.23 法語之言: 語 given yǔ 'words'; Zhu Xi marks no reading, though his gloss 正言之 is verbal (yù 'to tell') — arguable.
- 9.30 偏其反而: 反 given fǎn; Zhu Xi takes it = 翻 'to turn over'; the Ode lines (lemma 43) stand without quotation
  marks, since a unit cannot open with punctuation and the speech-continuation rule applies; the note marks it as a lost Ode.
- 9.29/9.30: He Yan's heading counts 31 chapters (Huang Kan 30) and his commentary reads 唐棣 with the 權 saying; where his
  extra chapter falls could not be located in the archived text (no breaks marked). We follow Zhu Xi's 30.
- 9.6: Zhu Xi's 孔氏 quotation is read as ending at 未可知也, so 與者疑辭… is Zhu Xi's own.
- Facts from general knowledge, as in earlier books: 利者義之和 from the Changes, 易簀 from the Record of Rites, 雄雉 in
  the Bei 邶 section, the Book 14/15 repeats (知者不惑…, 好德如好色), commentator identities (Hou Zhongliang, Hu Yin, etc.);
  9.12-related cross-references to 12.1 and 12.22 should be checked when Book 12 is drafted.

## Book 10: 18 sections, not 17 (analects-10, 2026-11-18)
Zhu Xi's heading says 舊說凡一章，今分為十七節, but the Siku copy marks 18 ○ section starts (朝與下大夫, 君召, 入公門, 執圭,
君子不以紺緅, 齊必有明衣布, 食不厭精, 席不正不坐, 鄉人飲酒, 問人於他邦, 廏焚, 君賜食, 入太廟, 朋友死, 寢不尸, 升車, 色斯舉矣
after the opening). Only 12 of them close with 此一節記…; 席不正不坐, 廏焚, 入太廟 (重出) and 色斯舉矣 do not, so which pair
Zhu Xi counted as one is unclear. We follow the printed breaks: 10.1–10.18, parts.json passages 17 → 18. The about and
the 10.1 note mention that many modern editions divide the book into 27. Say if you want 17 (merging which two) or 27.

## Smaller points left open (analects-10, 2026-11-18)
- Readings: 首 in 東首 (10.13) kept shòu per Zhu Xi's 去聲 (a different word, 'to face toward'); 長 cháng (10.6, Zhu Xi
  去聲) and 拖 tuō (10.13, Zhu Xi 徒我反 → duò) follow modern practice, notes say so; 勝 shēng in 10.5 (平聲) but shèng in
  10.8 不使勝食氣 (no note from Zhu Xi); 齊如也 (10.8) read zhāi, Zhu Xi marks nothing; 去喪 去 given qù (Zhu Xi 上聲).
- 10.18 曰山梁雌雉…: i says 'The Master said' (He Yan's unattributed comment, Xing Bing); l keeps 'He said'. Zhu Xi's
  必有闕文 stated; 共 read gòng, with the 拱 reading (Chao Yuezhi, Liu Pinjun) in the note.
- Zhu Xi's commentary prints 狊 古闐反 (10.18), probably for 古闃反; commentary only, not the text, left alone.
- General knowledge kept, as in earlier books: 康子 = Ji Kangzi (from 2.20/6.6), the 殯 gloss, 沽 for both buying and
  selling, commentator identities (Lu Deming, Chao Yuezhi, Xing Bing, Zhang Zai, Xie Liangzuo).
- The headless render check could not run this time (permission refused for a local server + browser); a later run
  with a browser should load analects-10 once.

## 由 written Yóu in Book 11 (analects-11, 2026-11-18)
Books 2, 5 and 6 print Zilu's personal name 由 as 'Yóu' (accented, to keep it apart from English 'you'); Book 9 (and the 牢 entry above)
uses plain 'You'. Book 11 uses Yóu throughout and its 11.12 note explains the accent. Say which you want and a later run will bring
Book 9 into line.

## Smaller points left open (analects-11, 2026-11-18)
- Readings against Zhu Xi's marks, each noted once: 德行 xíng (his 去聲 xìng), 從我 / 從者 cóng (his 去聲), 三復 sān (as 5.19).
- 比及 (11.25) read bì, the traditional reading (Zhu Xi 必二反; Book 4 shipped 比 bì); some modern readers say bǐ. 屢空 (11.18) read kòng
  'in want'; Zhu Xi marks nothing and kōng is also heard; the note says both. 夫二三子 (11.10) read fú 'those', unmarked by Zhu Xi.
- 11.25 lemmata 60–61: Zhu Xi's split of speakers (Zeng Xi asks, the Master answers) is followed; the note gives the other reading
  (all the Master's reply).
- Particle-only He Yan variants (孰賢乎, 過猶不及也, 足民也, 能之也…) are noted, following the 'character added or dropped' rule.
  Say if you would rather drop particle-only variants from the notes.
- Commentators named by surname only in Zhu Xi (洪氏, 吳氏, 王氏) are given as 'Hong', 'Wu', 'a Mr Wang', without identification;
  11.11's He Yan comment is credited to Chen Qun 陳群 on the strength of 陳群曰.
- The He Yan transcription (KR1h0005_006) lacks page 2b, so 11.4–11.5 and the start of 11.6 could not be collated against He Yan.

## Smaller points left open (analects-12, 2026-11-19)
- 12.8 惜乎夫子之說君子也: punctuated with Zhu Xi as 夫子之說，君子也 ('your words, sir, are a gentleman's'), which his gloss 子成之言乃君子之意 requires; the note gives the other common punctuation (one sentence, 'what a pity, sir, the way you speak of the gentleman').
- Readings against Zhu Xi's marks, each noted once: 去 qù (his 上聲), 譖 zèn (莊蔭反), 選 xuǎn (息戀反), 告 gào in 忠告 (工毒反), 行 xíng in 行違 (去聲). 祗 in 亦祗以異 read zhǐ 'only' (Zheng Xuan 祗適也); the glossary's first reading for 祗 stays qí (7.34), so this occurrence states its reading.
- He Yan's 12.5 comment is headed 鄭之曰, treated as a slip for 鄭玄曰 (Zheng Xuan) and hedged; Kong Anguo's gloss on 復 in 12.1 prints 及 where 反 is expected, reported as printed. 12.19 He Yan 子爲改焉用殺 (改 for 政) reported as a probable slip, not proved.
- Sima Niu's brother: Zhu Xi names him 向魋 here and identifies 桓魋 with 向魋 at 7.22; the note follows that.
- General knowledge kept, hedged 'in tradition': Gao Yao as Shun's minister of punishments, Tang as founder of the Shang, 司馬 as the minister of war's title.
- 12.15 repeats Book 6's 博學於文 passage (6.25 in our numbering); Zhu Xi's text here lacks 君子, so l supplies 'one'.

## 2026-11-19 — Book 13

- **Two chapters on one card (13.6–7, 13.13–14).** Zhu Xi's copy prints these pairs with only a ○ between them and no commentary, so the unit-per-lemma rule puts each pair in one unit. Decided meanwhile: one card, numbered with a range chip ("6–7", "13–14"), via a new `npas` key in the draft and build; the note on each says the card holds two chapters. The same will happen at 15.18–19 and 15.22–23. If you would rather split such stretches into two cards at the ○ (which needs the gate to allow a lemma to span two units), say so and the build can be changed before Book 15.
- **13.20 行己有恥** — clear misprint (已 for 己) corrected in the reading text under rule 5b; recorded in emend.json.

## 2026-11-19 — Book 14

- **Two misprints corrected (rule 5b), recorded in emend.json:** 14.42 莫已知也 → 莫己知也 (Zhu Xi's own sound note 莫已之已音紀餘音以 confirms; the two 已 of 斯已而已矣 stay 已 yǐ, as he says), and 14.43 總已以聽 → 總己 (his comment 總己謂總攝己職; Ruan 總己).
- **14.40 子曰作者七人矣** is numbered as its own chapter: the Kanripo transcription shows a blank where the ○ should be, but Zhu Xi comments on it separately (李氏曰), and his count 凡四十七章 needs it.
- **14.17 九合諸侯:** Zhu Xi reads 九 as 糾 'to marshal' (督也). The translation keeps a neutral 'time after time' (i) and the plain numeral in l, and the note gives his reading. If the owner prefers Zhu Xi's reading in the English as crib precedence would suggest, only u22's l/i change.
- **Readings decided:** 諒隂 liáng ān (traditional; Zhu Xi gives no sound and says 未詳其義); 孔氏 bound as a name (as 管氏 in Book 3); 何為 'why' read wèi (14.34, 14.37; not marked by Zhu Xi); readings against Zhu Xi's marks, each noted once: 行 xíng (14.4, 14.29), 盪 dàng (土浪反), 糾 jiū (居黝反), 使 shǐ (14.26), 叩 kòu (音口).
- **He Yan transcription slips, reported as printed and hedged:** 陳桓 for 陳恒 (also in Ma Rong's comment there), 孔子與人坐, 賜也賢乎我, 石門石門, 未之難 (its own comment prints 未無也), 踞於位, 脩巳以敬人. Ma Rong's comment on 總己 reads 已已百官也 in the transcription and is not cited.
- Glossary: the first `;` of many entries falls inside a parenthesis (as in Book 13), so the popup's default gloss may cut mid-parenthesis where a token gives no in-context gloss; every Book 14 token carries its own gloss, so nothing visible changes, but the format may be worth a later pass.

## 2026-11-19 — Book 15

- **15.4 恭己** — clear misprint (已 for 己) corrected under rule 5b; recorded in emend.json.
- **15.25 今亡已夫** kept as printed (Zhu Xi's own quotation of Yang Shi has 已夫); Ruan and He Yan read 矣夫, noted. Say if you would rather treat 已 as a misprint.
- **Binding left unbound (decided meanwhile):** 俎豆 (Book 8 binds 籩豆 — binding it would be consistent; a one-unit change plus a glossary key), 志士 / 仁人 (Zhu Xi glosses as ordinary phrases), 明日, 直道, 没世. 三代 and 師冕 are bound.
- **15.30 (lemmata 41–43):** one sentence split at Zhu Xi's 句 marks; as at 7.6 and 8.8, these units carry 子曰： without a quotation mark.
- **Commentary transcription oddities, paraphrased not quoted:** He Yan's 未事 for 末事 (15.1), Zhu Xi's 冇得 (15.2), 聽之侯人 (15.26). 15.3 prints 德 (not the edition's usual 徳); kept.
- 蘇氏 is given as 'Su' (as Books 1–12) while Books 13–14 say 'Su Shi'; a one-word change if you want them unified.

## 2026-11-19 — Book 16

- **A ○ inside 16.1.** The print has a ○ before 丘也聞 (lemma 9), outside Zhu Xi's comment brackets. Treated as not a chapter break, since his count of fourteen chapters needs 16.1 to run to 蕭牆之内也; the unit's note says so.
- **Claims from memory cut (decided meanwhile):** that later critics suspect 寡 and 貧 have changed places in 不患寡而患不均，不患貧而患不安, and that Zheng Xuan's example (Yang Hu imprisoning Ji Huanzi) came before Ran You served the Ji. Neither is in Zhu Xi or He Yan's collection. If you want the transposition mentioned (it is a well-known Qing suggestion), it needs a public-domain source to cite.
- **Kept, hedged:** unit 0 says the head of the Ji was 'presumably Ji Kangzi', which is an inference, not in the commentaries.
- **16.12 displaced couplet:** Zhu Xi quotes Hu Yin: Master Cheng put 誠不以富亦祗以異 (12.10) at the head of this chapter, and Hu judges it seems to belong just before 其斯之謂與; Zhu Xi calls this near right and adds that 孔子曰 has probably dropped out. Nothing moved; the note gives the account (and agrees with what the shipped 12.10 note says Cheng held).
- **Readings against Zhu Xi's marks:** 亢 kàng (his 音剛 gāng; as 1.10's note), 探 tàn (吐南反), 辟 pì in 便辟 (婢亦反), 逺 yuǎn in 逺其子 (去聲) — each noted once.
- **Binding (decided meanwhile):** bound 夫人, 小童, 小君 (titles), 大人, 庶人, 陪臣, 血氣; not bound 便辟, 便佞, 善柔 (Zhu Xi glosses each as a unit — binding would be a three-unit change plus keys), 君夫人, 寡小君, 公室, 文徳, 干戈, 子孫.
- **文徳** is 'the virtue of letters' in l and 'the virtue of peace and learning' in i, to keep the house 文. Say if you want something else.
- **Line breaks:** Book 16 makes the number of ^ breaks in each w equal the number of lines in l, and breaks after an opening 「 as Book 15 does. The build does not enforce this, and the shipped 15.1 has one more break than lines; say whether it should become a gate.
- **Older glossary entries** (禄, 辟, 諒, 毁, 隠 and others) have an unclosed parenthesis before their first ';', so their default popup gloss cuts mid-parenthesis (as noted for Books 13–14). The Book 16 entries were written to avoid it; the older ones would need their text changed, not just added to, so they were left.

## 2026-11-19 — Book 17

- **17.17 = 1.3** reuses the shipped English; He Yan's text lacks the chapter entirely, and the note says so.
- **Readings decided:** 歸 guī in 歸孔子豚 (Zhu Xi 歸如字一作饋; the note gives kuì for those who follow 饋); 亡 wú 'away from home' (unmarked); 莞 wǎn (Zhu Xi 華版反, which points to huǎn — noted once); 佛肸 bì xī (佛音弼, 肸許密反); 亟 qì 'often' (好亟知並去聲); 識 shí, 興 xīng (unmarked); 鄉原 xiāng yuàn (原與愿同, no sound mark); 徼 jiāo after Zhu Xi's 古堯反 — some modern editions read jiǎo; say if you want that.
- **Binding (decided meanwhile):** bound 陽貨, 公山弗擾, 公山氏 (as 孔氏/管氏), 佛肸, 中牟, 周南, 召南, 鄉原, 孺悲, 莞爾, 女子 (doubtful — could equally be 女 | 子); not bound 東周 (Zhu Xi reads 為東周 as 興周道於東方, not the period name), 匏瓜, 上知, 下愚, 牛刀, 絃歌, 日月, 從事, 鳥獸, 草木, 六言, 六蔽.
- **Speaker attributions following Zhu Xi:** 17.1 the unnamed answers 曰不可 are Kongzi's (隨問而對) in i, a bare "He said" in l; 17.21 unit 46 (女安則為之…) is the Master's (此夫子之言也), left unquoted because it opens its unit; 17.24 unit 51 splits the Master's question from Zigong's answer (惡徼以下子貢之言也).
- **17.25** translated on Zhu Xi's household reading (小人 = servants, 僕𨽻下人; women and servants of a house, 臣妾); the note explains, without comment.
- **Echoes left, judged literal (reviewer's list):** 蔽 'clouding' in 17.8 is close to Legge's 'beclouding' — the alternative would be 'screening' (Zhu Xi 遮掩), a 12-place change plus the glossary; 17.16 'quarrelsome and contrary' / 'perverse'; 17.5 'a Zhou in the east'; 17.18 'sharp mouths that overturn states'.
- **General knowledge kept:** the Guanju as the first poem of the Zhounan (17.10).

## 2026-11-19 — Book 18

- **Readings decided:** 長沮 cháng jǔ (Zhu Xi 沮七余反 points to qū — noted once); 騧 guā (烏瓜反 points to wā — noted once); 三黜 sān (Zhu Xi 去聲, as 5.19); 施 printed and read shī but translated as 弛 'neglect', following Zhu Xi (陸氏本作弛; 弛遺棄也); 食 sì, 見 xiàn (18.7); 中 zhòng ×4, 降 jiàng (18.8); 大師 tài shī; 少 shào in 少連/少師; 飯 fàn. Say if you want Zhu Xi's qū / wā.
- **Zhu Xi's 18.4 comment prints 定公四十年**; the note says it is evidently for 十四年 (Duke Ding did not reign forty years). Commentary text only, not the reading text, so not in emend.json.
- **Binding (decided meanwhile):** bound 微子 箕子 比干 季桓子 接輿 長沮 桀溺 孔丘 虞仲 夷逸 朱張 少連 方叔 魯公, the eight officers of 18.11, 士師, 逸民 (Zhu Xi's term), 丈人 (doubtful), 憮然, 滔滔; the musicians of 18.9 as office + name (大師 | 摯, 亞飯 | 干, 三飯 | 繚, 四飯 | 缺, 少師 | 陽). Not bound: 女樂 (doubtful), 季 | 孟, 楚狂, 隠居, 鳥獸, 四體, 五榖, 明日, 長幼, 大故, 已而, 鼓, 播 | 鼗, 擊 | 磬.
- **Romanisations of obscure names** are the run's choice: Yu Zhong, Yi Yi, Zhu Zhang, Shao Lian; the eight officers Bo Da, Bo Kuo, Zhong Tu, Zhong Ren, Shu Ye, Shu Xia, Ji Sui, Ji Gua.
- **Speakers:** 18.8 unit 20 (我則異於是…) is the Master's words with no 曰, left unquoted as 17.21 unit 46. 18.7 unit 15: the note gives both Zhu Xi's report of the Fuzhou text (子路反子曰) and Zheng Xuan's reading.
- **Echoes left, judged literal:** 'birds and beasts', 'the madman of Chu', 'He is a recluse', 'presented his two sons to him'.
- **Glossary brackets:** the reviewer counts about 215 shipped entries (Books 9–17) whose first clause has an unclosed bracket before the first ';' (as already noted for Books 13–16). Fixing them means changing text, not adding, so it was left. Book 18's new entries avoid it. Approve a one-off pass if you want them fixed.
- **Manifest title:** `part` is "Book 18 — 微子 The Viscount of Wei" (title translated, as Book 15 "Duke Ling of Wei").

## 2026-11-19 — Book 19

- **Readings decided:** 文 wén in 小人之過也必文 (Zhu Xi 文去聲, i.e. wèn — noted once; translated 'dress up', after 文飾); 洒 sǎ, 掃 sǎo (Zhu Xi 色賣反 / 素報反 point to shài / sào — noted); 亡 wú (亡讀作無); 與 yú in 我之大賢與 / 我之不賢與; 泥 nì, 好 hào, 惡 wù in 惡居下流, 更 gēng, 識 zhì ×2, 語 yù, 量 liàng, 知 zhì ×2 in 19.25 (知去聲); 道 dǎo in 道之斯行 (He Yan's text writes 導); 見 jiàn in 多見其不知量 (He Yan's 適自見不知量 may intend xiàn 'to show' — say if you prefer it); 多 kept duō though read as 祇 'only' (Zhu Xi 多與祇同).
- **Binding (decided meanwhile):** bound 儼然 堂堂 言游 孟莊子 孟氏 陽膚 仲尼 公孫朝 叔孫武叔 陳子禽 (whole name, rather than 陳 | 子禽). Not bound: 下流 (as 17.24, though Zhu Xi glosses it as one place), 文武, 丘陵, 宮牆, 室家, 常師, 百工, 小道, 致命, 洒掃, 應對, 進退, 草木, 親喪, 日月, 百官, 邦家.
- **仲尼 'courtesy name':** the archive shows only that 仲尼 = 孔子; the note and glossary call it his courtesy name from general knowledge. Hedge if you want everything grounded.
- **Commentary slips (not reading text, so not in emend.json):** Zhu Xi on 19.15 prints 少試實 (probably for 誠; hedged in the note); on 19.12 非以其未為先 (未 for 末; paraphrased, not quoted). He Yan's book heading reads 凢卄四章/九卄五章 — a 24-chapter count beside 25; not mentioned.
- **19.25 於變時雍:** Zhu Xi cites it without naming the source (the Documents, from memory); the note leaves it unnamed.
- **Echoes left, judged literal:** 'seen from afar' (19.9), 'strength to spare' (19.13, as 1.6), 'has not fallen to the ground; it is among men' (19.22), 'Those who find its gate are perhaps few' (19.23), 'what harm would that do to the sun and moon?' (19.24).
- **Glossary brackets:** 肆 and 矜 (older entries) also have an unclosed bracket in their first sense; left, as with the ~215 noted under Book 18.
- **Manifest title:** `part` is "Book 19 — 子張 Zizhang".

## Book 20 (堯曰), 2026-11-20 — decided meanwhile
- **Unit 4 (雖有周親…在予一人) unquoted:** King Wu's words have no 曰, and a unit cannot open with 「 (punctuation trails the word before it), so they stand unquoted in Chinese and English; the note says whose they are (Zhu Xi: from the Great Declaration 泰誓).
- **Tang in unit 2:** the l opens "(Tang) said:" following Zhu Xi's 曰上當有湯字.
- **帝 'the High Lord':** used for 帝 throughout 20.1 (皇皇后帝 'the most august Sovereign, the High Lord'; i 'Lord on High').
- **Binding:** bound 厯數, 皇皇, 一人 (予一人 'I, the One Man'). Not bound: 后帝, 萬方, 周親, 仁人, 權量, 法度, 從政, 五美, 四惡, 衆寡, 衣冠, 瞻視, 出納.
- **屏 bǐng, 出 chū:** Zhu Xi gives no mark for 屏 (Kong Anguo 屏除也); modern bǐng given. He marks 出去聲; modern chū given, noted once.
- **He Yan's 右 for 后** (Kong Anguo's gloss 皇大也右君也): quoted as printed with a word that 右 stands for 后. Commentary, not reading text, so not in emend.json.
- **Render check:** not run this time (refused by the session's permission layer); a later run with a browser may check analects-20 loads under data-script="chinese".
- **DONE:** not written this run, so that the next run can still add Book 20's `audio` field once the Action lands it; that run then finds all 20 published and writes DONE.

## 2026-11-20 — Analects finished
- All 20 books are published with audio; `DONE` written. Every work in `queue.txt` now has a DONE marker, so the routine idles until a new work is added to the queue. Still open from Book 20: a headless render check of analects-20 was never run.
