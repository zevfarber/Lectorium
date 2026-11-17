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
