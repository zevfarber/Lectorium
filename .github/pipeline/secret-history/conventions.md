# The Secret History of the Mongols — conventions (Run 3)

Distilled from the project's `middle-mongol-secret-history-conventions.md` (2026-07-29) and the published
pilot `secret-history-01-06.json` (§§1–6), the model of shape and register.

## What the text is (say it plainly to the reader)
The Mongolian original, in Mongolian script, is lost. What survives is a Ming teaching edition: the Mongolian
written phonetically in Chinese characters, a Chinese gloss over every word, and an abridged Chinese
translation. So (1) the characters are Chinese and mean nothing in Chinese; (2) the Mongol line is a
reconstruction — editors differ over vowels; (3) the glosses are the Ming glossators' own, carried in
square brackets.

## Source and the sole-source rule
- Text: Shiratori Kurakichi 白鳥庫吉, 音訳蒙文元朝秘史 (Tokyo 1943), after the Ye Dehui print of 1905/1908, from
  the Japanese Wikisource transcription — archived 2026-10-12 (all 36 pages, `source/raw/`), extracted to
  `source/secret-history-shiratori.json` (282 sections, 29,353 words; §§1–6 identical, word for word, to the
  pilot's verified archive). PD basis signed off by the owner 2026-07-29 (Shiratori d. 1942).
- While drafting: Shiratori's text and the Ming interlinear glosses only. Permitted meaning check: Naka
  Michiyo, 『成吉思汗実録』 (1907) — meaning only, never wording. Modern translations (de Rachewiltz, Cleaves,
  Onon, Atwood) are never opened.

## Data model (the build does the mechanics)
- One glyph per word: the Han transcription (the edition's FVS "small character" markup U+180B/U+180C is
  stripped at build — never by hand; U+FE00 stays as in the pilot). `glyph.tr` = the romanized word as
  printed (with its punctuation); `reading` = "<Han> <romanized word without punctuation>".
- `t` = the unit's romanized words joined by single spaces, exactly as printed. `ln` = the § number (§ chip);
  `p: true` on the first unit of every §.
- The drafter supplies each word's `morph`: one entry per morpheme the reader sees, `{"lemma": dictionary form
  (töre-, a-, deġü), "gloss": "… [Ming gloss]"}` — e.g. Qaγan-(n)u → qaγan + -(n)u.
- Glossary: shared `secret-history-glossary.json`, keyed by the reader's tokens of `t` (Qaγan-(n)u → `qaγan`
  and `nu`), value `"<dictionary form> — <meaning> (<grammar>) [<Ming gloss>]"`. 100 % coverage, no unused keys.

## Segmentation and translation
- Sense-unit = Shiratori's own punctuation where he has it (`.` closes a sentence), otherwise the natural
  clause. Genealogies stay whole. Long converb chains are broken into readable units and the note says so.
- `l`: possessor before its noun, converbs as "-ing", -tü as "wife-having", no copula supplied; stop before
  word-salad. `i`: plain, a little formal — a chronicle, never "verily".
- Grammar is the payload and the Ming glossators are the co-teacher (their 行 = dative-locative, 着 = converb,
  有的 = possessive). Recurring patterns flagged first, nudged after: converb chain; possessive -tü/-tu/-tai/-tei;
  reflexive-possessive -beġen/-deġen/-jüġen; vowel harmony in case endings; ese vs ülü.
- Notes admit uncertainty (börte čino is "blue-grey wolf" and a name; 訥 writes -nu and -nü).
- Proper names: Shiratori's form in `l`, a plain English spelling in `i` (Činggis → Chinggis, Temüžin → Temüjin).

## Characters
Three CJK Extension B characters occur in §§1–6 and more later; never substitute them — a box is honest.

## Pronunciation and audio
`langCode: null`. A Middle Mongol voice has not been chosen (it also waits for the Stele of Yisüngge); parts
publish without audio until the owner chooses. Do not build audio.

## Decisions taken while setting up Run 3 (2026-10-12)
- Parts: whole sections in order, grouped to about 300–520 words; a section longer than that is its own part
  (66 parts; see plan.md). New part ids use three-digit § numbers (secret-history-007-010).
- `p: true` on the first unit of every § (the conventions' rule; the pilot omitted it once, at §3).
