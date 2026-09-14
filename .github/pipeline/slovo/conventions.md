# Слово о пълку Игоревѣ — conventions for every part

These are the rules the two published parts (`slovo-proem.json`, `slovo-part1.json` in the
repository root) already follow. **Read both files before drafting; they are the model.** New parts
must be indistinguishable from them in shape, register and depth.

## Edition and text

- Text = the editio princeps: *Ироическая пѣснь о походѣ на половцовъ удѣльнаго князя
  Новагорода-Сѣверскаго Игоря Святославича*, ed. A. I. Musin-Pushkin, Moscow, Senate Press, 1800.
  Public domain. The verified text is `source-1800.txt` in this folder (sha256 in `parts.json`);
  it is the only source of the poem's words. **Do not fetch the text from anywhere else and do not
  "correct" it** — the 1800 orthography (ѣ, ъ, ь, і, titlo numerals such as ĩ, д̃, г̃, the printed
  punctuation, the capitalised Князь) is kept exactly, misprints and all. A suspected misprint gets
  a note, never an emendation.
- The poem survives in no manuscript: the one copy burned in 1812. Everything descends from this
  1800 printing and Catherine II's copy. The `about` field of every part says so in a sentence, and
  the notes admit uncertainty rather than smoothing it over: the "dark places" (тёмные места) are
  flagged, the competing readings named, and no rendering claims more certainty than survives.

## Units

- The 1800 edition prints continuous prose. **We keep prose**: no verse lineation (every modern
  lineation is a copyright-era editorial construct), no `v: true`, no `\n` inside `t`.
- The tap-unit is a sense-unit cut at the edition's own punctuation — a sentence, or a clause group
  ending at `;` or `:` where a full sentence would run to 60+ words. Part 1 averages ~18 words per
  unit; aim for 12–30. Never split inside a phrase.
- `p: true` on the first unit of each source paragraph (most parts are inside one paragraph, so
  usually only the first unit).
- The units of a part, concatenated with single spaces, must equal the part's source text exactly
  (the validator checks this).

## Fields per unit

- `t` — the 1800 text, verbatim.
- `tr` — transliteration, scholarly Slavist romanisation, one line per unit: ž š č c x; ě = ѣ;
  ŭ / ĭ = ъ / ь (also word-finally); ju / ja = ю / я; ī for і-titlo read as a numeral is written
  as the romanised letter (`ī`), with the numeral's value explained in the note; і = i; ы = y;
  й = j; щ = šč; ц = c; ѳ = f; ѵ = i; capitalisation as in the source. It is a reading aid for the
  Cyrillic, not a phonetic reconstruction.
- `l` — literal: structurally transparent, follows the Old East Slavic word order wherever English
  can bear it, keeps the aspect and mood visible, never gibberish.
- `i` — idiomatic: real English, lightly elevated (this is a heroic lay), never childish; omit only
  when it would be word-for-word the same as `l`. Part 1 has `i` on every unit; do the same.
- `n` — note: grammar that a reader of modern Russian would stumble on (aorist and imperfect
  forms, dual number, the vocative, dative absolute, enclitic ся, short-form participles), the
  mythology and history (who Boyan, Troyan, Div, the Polovtsians, the named princes are; the 1185
  eclipse), and the dark places with the main proposed readings. Every factual claim in a note
  must be true — a reviewer's first duty is to check that. Not every unit needs a note; the
  published parts note most units because the text is dense, so expect to as well.

## Glossary

- Inline `glossary` object in the part file, as in the published parts (this work does not use a
  shared glossary file). Key = the token as the reader's tokenizer produces it, lowercased,
  brackets stripped. Value = `lemma — gloss (grammatical info)`, e.g.
  `"бяшетъ": "быти — was / would be (imperfect 3sg; here conditional 'would it be')"`.
- 100 % coverage of every token in the part, no unused keys. `validate_slovo.py` enforces both
  under the reader's own regular expression.
- Proper names stay untranslated in `l`/`i` (Игорь, Всеволодъ, Боянъ, Каяла) and are glossed
  (`"каялѣ": "Каяла — the river Kayala (unidentified; loc.)"`).

## Translation provenance (copyright)

- Translate from the 1800 text only. **Do not open, fetch, quote or paraphrase any modern
  translation** (Nabokov, Zenkovsky, the Likhachev school, Jakobson, or any other) for wording.
  Old public-domain aids only, and only for meaning on a hard word: Sreznevsky's *Материалы*
  (1893–1912), the 1800 edition's own modern-Russian *переложение*, Vasmer is post-1930 and must
  not be used.
- The famous passages — Yaroslavna's lament (part 8), the Golden Word (part 5), the opening of
  part 2 with the bloody dawns — invite echoes of well-known English renderings. Decide house
  renderings for the distinctive phrases first, from the Old East Slavic alone, and note in the
  LOG which phrases were checked.
- Fresh translations of a public-domain original are new works belonging to this project.

## Story-file header

Copy the header shape of `slovo-part1.json`: `id` = `slovo-part<N>`; `title` = «Слово о пълку
Игоревѣ»; `titleEn` = "The Tale of Igor's Campaign — <roman numeral>: <title from parts.json>";
`titleRead`, `work`, `workEn`, `language` = "Old East Slavic", `langCode: null`, `trStyle: "line"`;
`provisional: true` with a `draftNote` describing the movement; `source` in the same wording as
part 1's (edition, orthography, prose units, transliteration, pronunciation convention, "translations
made fresh from the 1800 original"); `about` — one paragraph placing the movement in the poem and
stating the single-witness situation. `part` = "<roman numeral> · <title>".

## Manifest entry (`stories.json`)

Insert a new object immediately after the previous Slovo part's entry (so the parts stay in order):
```
{"id": "slovo-part<N>", "title": "Слово о пълку Игоревѣ",
 "titleEn": "The Tale of Igor's Campaign — <roman>: <title>",
 "language": "Old East Slavic", "work": "Слово о пълку Игоревѣ",
 "workEn": "The Tale of Igor's Campaign", "part": "<roman> · <title>", "file": "slovo-part<N>.json"}
```
Write the manifest back with `json.dump(..., ensure_ascii=False, indent=1)` and no trailing
newline — that reproduces the file byte-for-byte apart from the insertion (check with `git diff
--stat`: one file, additions only).

## Pronunciation and audio

Reconstructed late-12th-century Old East Slavic, one convention applied consistently (no akanye;
weak yers silent, strong ъ=[o], ь=[e]; ѣ=[e]; г=[g]; palatalisation of coronals before front
vowels and yers; free stress approximated). **Audio is not part of a text run**: the voice recipe
(ru-RU-Wavenet-A with per-word IPA pins over a modern carrier) is not yet wired into the
repository's audio workflow. Leave `audio` absent and `langCode: null`; the audio phase is
separate and comes after the text is complete.
