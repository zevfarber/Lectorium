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
