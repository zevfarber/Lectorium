# Mencius (孟子) — Lectorium conventions

*Set 2026-11-20, at setup, as an easy-win reserve on the Analects machinery. The Mencius follows the
Analects' conventions (`../analects/conventions.md`), and through them the Daodejing's
(`claude/chinese-daodejing-conventions.md` in the project docs), in everything not stated here: pinyin,
the words model, binding, polyphones, `br` verse breaks, glossary format, tones, audio. Read
`../analects/conventions.md` first; this file records only what differs.*

## What the text is (say it plainly in each part's `about`)

Conversations and sayings of Mencius (Mengzi 孟子, c. 372–289 BC), the Confucian teacher a century
after Confucius, with kings, rivals and his own disciples. Seven books, each in two halves (上 and
下), named from opening words. Tradition says Mencius compiled it with his disciples Wan Zhang and
Gongsun Chou; most scholars think disciples put it together after his death. Its arguments are long
and built step by step — unlike the Analects' short sayings. The original has no punctuation.

## Edition and witnesses

- **Text drafted from Zhu Xi 朱熹, 孟子集注**, Wenyuange Siku Quanshu copy (1782), as transcribed by
  Kanripo (`KR1h0015`, juan 010–016, archived verbatim in `source/kanripo/`) — the same edition and
  the same file series as the Analects.
- **Collation witness: Zhao Qi 趙岐, 孟子章句**, Sibu Congkan reprint of a Song edition (`KR1h0002`,
  in `source/witness/`). Pre-1930. Zhao Qi (2nd century) is also the older commentary: where his reading
  differs from Zhu Xi's and matters, the note gives it.
- `source/witness/KR1h0001_*` is Kanripo's punctuated TLS text. It is a modern digital edition, used
  only as a finding aid (its chapter numbers locate passages; its punctuation is never copied).
- **Variants:** as the Analects — sense-changing readings noted, naming the witness; graphic variants
  (宫/宮, 髙/高, 衆/眾, 逺/遠, 説/說, 恒/恆) not noted. The printed text is always Zhu Xi's.
- **Transcription errors** in Kanripo's Siku file are corrected through `emend.json` (owner's rule
  5b, 2026-11-06). The build requires the unit's note to open "The print has X, a misprint for Y,
  corrected here."; add after it that the slip is the transcription's and which witness reads Y.
  Known at setup: 6A.1 把柳 for 杞柳 (four times; already in `emend.json`). Look for others in each
  collation and add them the same way.

## Cut and segmentation

- **34 parts.** Each of the fourteen 篇 (1A … 7B) is cut into parts of whole chapters of about
  1,000 characters (`parts.json`: `book` like `"4B-2"`, `cite` like `"4B.25–33"`, `firstPassage`,
  `passages`).
- **Units:** one per stretch between Zhu Xi's commentary interruptions, as the Analects. The archive
  already splits a stretch at a chapter's ○, so a unit never holds two chapters — no `npas`.
- **Chapters:** the first unit of each chapter has `pas: "4B.25"` (book code + chapter number within
  the 篇). The build checks it against the archive's `newChapter` and counts on from `firstPassage`;
  `ln` is the chapter number. Chapter numbering is Zhu Xi's own count (the head of each 篇 states it,
  e.g. 凡四十六章): 7A has 46 chapters where some modern numberings have 45, so after 7A.12 our numbers
  can run one ahead of a modern translation's. Say so in the `about` of the 7A parts.
- Long speeches: break lines at the editorial punctuation as the Analects; a unit of several hundred
  characters is normal here (Mencius argues at length). Keep lines readable on a phone: a line is a
  clause, not a paragraph.

## Translation — house renderings

The Analects' table holds (仁 humaneness, 義 what is right, 禮 the rites, 君子 the gentleman, 道 the Way,
孝 filial, 弟 tì deference, 忠 wholehearted, 信 good faith, 德 virtue). Added for the Mencius:

| Chinese | House rendering | Avoided |
|---|---|---|
| 孟子 | Mencius (English); Mengzi in the glossary | — |
| 王 in address | l "King"; i "Your Majesty" | — |
| 1A.1 王何必曰利 | l "King, why must (you) say 'profit'?"; i "Why does Your Majesty have to talk of profit?" | "Why must Your Majesty use the word 'profit'?" |
| 仁義 | humaneness and what is right | "benevolence and righteousness" |
| 心 | the heart | "mind" as the running word (the note may say 心 is also where one thinks) |
| 性 | (human) nature | — |
| 四端 (2A.6) | the four beginnings | "four sprouts", "four germs", "four principles" |
| 不忍人之心 | a heart that cannot bear (to see) others suffer | "a heart sensitive to the suffering of others" |
| 浩然之氣 (2A.2) | l "the vast-flowing qi"; i "a vast, surging qi" — keep *qi* untranslated, glossed | "flood-like ch'i", "passion-nature" |
| 良知 / 良能 (7A.15) | knowing / ability one has without learning it | "innate knowledge", "intuitive knowledge" |
| 民為貴 (7B.14) | l "the people are most precious"; i "the people matter most" | "the people are of supreme importance" |
| 王道 / 霸 | the kingly way / a hegemon | "the Way of the true King" |
| 牛山 (6A.8) | Ox Mountain | — |

- **Crib precedence: Zhu Xi**, then Zhao Qi. Legge's 1861 English may be silently consulted as a
  meaning check; never for wording. **Modern translations are never opened** (Lau, Legge's wording,
  Van Norden, Bloom, Dobson): famous passages (1A.1, 1A.7 the ox, 2A.2, 2A.6 the child at the well,
  3A.4, 4A.17 the drowning sister-in-law, 6A.1–6, 6A.8, 6A.10 fish and bear's paw, 7B.14) are checked
  against memory of them for verbatim echo, and distinctive echoes rephrased.
- Persons: kings by their posthumous names in the English (King Hui of Liang, King Xuan of Qi),
  disciples by the name the text uses (Gongsun Chou, Wan Zhang), full identification in the glossary
  and the note on first appearance in each part.

## Glossary

- Shared work-level `mencius-glossary.json` (`glossaryFile`), separate from the Analects'.
  `glossary_seed.py` was seeded from the Analects' seed so pinyin and particles start right; its
  entries still cite Analects passages. **Before a part is built, rewrite every seed entry the part
  uses for the first time**: drop the Analects citations, keep the senses the Mencius uses, add the
  Mencius ones. Once a key is in `mencius-glossary.json` it may only be broadened.
- Add entries only; broaden by addition, never shorten.

## Audio

As the Analects: `langCode: "zh-CN"`, voice `cmn-CN-Chirp3-HD-Achernar`, built by the audio Action on
push; the story ships without `audio`; a later run adds it once `audio/<id>/align.json` exists.
