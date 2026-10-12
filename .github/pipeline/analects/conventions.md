# Analects (論語) — Lectorium conventions

*Set 2026-10-12 with the Book 1 pilot (`analects-01`). The Analects follows the Daodejing's
conventions in everything not stated here — read `claude/chinese-daodejing-conventions.md` in the
project docs (pinyin, words model, binding rules, polyphones, `br` verse breaks, glossary format,
validation). This file records only what is specific to the Analects or decided at the pilot.*

## What the text is (say it plainly to the reader)

Sayings and short exchanges of Confucius (551–479 BC) and his disciples, collected by their followers
over several generations. Twenty books (篇), each named from its opening words; the books were not
composed as a whole and Confucius wrote none of it. The original has no punctuation — every mark is
editorial. Each part's `about` says this.

## Edition and witnesses

- **Text drafted from: Zhu Xi 朱熹, 論語集注**, Wenyuange 文淵閣 Siku Quanshu copy (1782), as transcribed
  by the Kanseki Repository (Kanripo `KR1h0015`, juan files 001–009, archived verbatim in
  `source/kanripo/`). Zhu Xi's is the received text of the last eight centuries and substantially the
  text Legge printed in *The Chinese Classics* vol. 1 (1861), which the plan named.
- **Collation witnesses** (also archived): Ruan Yuan's 1816 reprint of the Song 論語注疏 (`KR1h0004`) and
  He Yan's 論語集解, Sibu Congkan reprint of a Song edition (`KR1h0005`). Both pre-1930.
- **Legge 1861 itself was not reachable as text from the pipeline** (archive.org scans are blocked
  from the shell and its OCR does not carry the Chinese of the text pages). The source statement
  therefore names Zhu Xi/Siku as the edition and Legge only as the printing it matches. A future run
  with page-image access should spot-check passages against Legge's pages, as the Daodejing did
  against Carus.
- **Variants.** A reading that changes the sense (a character added, dropped, or a different word) goes
  in the unit's note, naming the witness. Graphic variants (悌/弟, 爲/為, 説/說, 逺/遠) are not noted.
  Single-character variants are recorded, not acted on; the text printed is always Zhu Xi's.
- **Glyphs as the edition prints them.** The Siku copy prints 衆 (not 眾); keep it.
- `source/analects-zhuxi-siku.json` is built by `archive_analects.py`; each book's `sha256` in
  `parts.json` pins its lemma list. A mismatch means stop.

## Cut and segmentation

- **One part per book.** 20 parts. Book 10 (鄉黨) is printed by Zhu Xi as one chapter in 17 sections;
  treat the sections as passages.
- **Within a book, one unit per stretch between Zhu Xi's commentary interruptions** — his commentary
  plays the role Wang Bi's lemmata play for the Daodejing. Book 1: 26 units, 16 passages.
- **Each numbered passage starts a card:** its first unit has `p: true` and `ln` = the passage number
  within the book; `numbering: "stanza"` makes the reader show a single number. Passage numbers are
  the standard ones (1.1–1.16 etc.), which match Zhu Xi's chapter breaks (the ○ marks).
- Verse-style lineation as the Daodejing: `v: true`, `\n` in `t`, `br` on the first word of each line.
  Lines break at the editorial punctuation; speech openers 子曰：「 sit on the first line.

## Translation

- **House renderings (fixed at the pilot):**

| Chinese | House rendering | Avoided |
|---|---|---|
| 子曰 | The Master said | — (standard, unavoidable) |
| 君子 | the gentleman | "the noble man", "the exemplary person", "the superior man" |
| 仁 | humaneness | "goodness", "benevolence", "authoritative conduct", "humanity" |
| 禮 | the rites | "ritual propriety", "observances" |
| 孝 | filial (devotion); i: "a good son" | "filial piety" in i |
| 弟 (tì) | deference (to elders); i: "a good/dutiful younger brother" | "brotherly respect" |
| 忠 | wholehearted(ness) | "loyalty", "doing one's best" |
| 信 | good faith; true to one's word | "trustworthiness" |
| 德 | virtue | "excellence", "potency" (the Daodejing's 德 is different) |
| 義 | what is right | "rightness", "appropriateness" |
| 和 | ease (Zhu Xi: 從容不迫) | "harmony" as the running word |
| 文 | letters, the literary arts | "culture", "refinement" |
| 道 | the Way | "the Tao" |
| 1.1 學而時習之 | l "To learn, and in season rehearse it"; i "Learning, and going over it again each time its season comes round" | "practise it at due times", "apply it from time to time" |

- **Crib precedence: Zhu Xi's commentary** — it is printed with the text in the edition we use. Where
  an older reading (He Yan's collected commentators, Kong Anguo, Bao Xian) differs and matters, the
  note gives it. Legge's 1861 English may be silently consulted as a meaning check on a hard passage;
  never for wording.
- **Modern translations are never opened.** The Analects is heavily translated (Lau, Waley,
  Slingerland, Ames & Rosemont, Leys); famous passages are checked against memory of those for
  verbatim echo and distinctive echoes are rephrased.
- **Tones:** modern Mandarin reading practice, not Zhu Xi's 四聲別義 tone notes. Where he marks a
  reading modern practice ignores (行 xìng, 遠 yuàn), we give the modern reading and the note says
  so once. Where the reading changes the word (說 yuè, 樂 lè/yuè, 弟 tì/dì, 道 dǎo, 為 wéi/wèi,
  好 hào/hǎo, 與 yǔ/yú, 乘 shèng, 鮮 xiǎn), it is stated on every occurrence.
- Disciples are named by courtesy name in the English (Zigong, Zixia), with the full name in the note
  and glossary on first appearance. 有子 and 曾子 keep "Master You", "Master Zeng".

## Binding (Daodejing rules apply)

Bound in Book 1: personal names (有子, 曾子, 子夏, 子禽, 子貢), 夫子, 君子, 弟子, 朋友, 父母, 先王, 千乘,
何如, 其諸. Not bound, because they mean what their parts mean: 巧言, 令色, 遠方, 恥辱. 子 alone as a
speaker is not a compound (it is "the Master").

## Glossary

- Shared work-level `analects-glossary.json` (`glossaryFile`), keyed on characters plus bound
  compounds; format `"pinyin — meaning (grammatical info)"`. Entries are written in
  `glossary_seed.py` and the build copies the ones the corpus uses (no unused keys allowed).
- **Separate from the Daodejing glossary on purpose:** the two books use the same characters in
  different senses (德, 學, 子), and their glosses should not fight.
- Add entries only; broaden an existing entry by addition, never shorten it.

## Audio

Same as the Daodejing: `langCode: "zh-CN"`, voice `cmn-CN-Chirp3-HD-Achernar`, built by
`.github/workflows/audio.yml` on push (zh-CN is in its voice list). The story ships **without** an
`audio` field; once the Action commits `audio/<id>/align.json`, a follow-up commit adds
`"audio": "audio/<id>"`.
