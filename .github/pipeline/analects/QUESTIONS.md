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
