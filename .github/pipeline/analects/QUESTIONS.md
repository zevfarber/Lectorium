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
