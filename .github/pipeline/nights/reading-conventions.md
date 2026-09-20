# Reading conventions — Alf Layla wa-Layla

*The rules for turning an archived page into a readable night. `conventions.md` beside this file
governs the transcription phase and stops at the bare rasm; this file starts there. Decided
July 31 – August 3, 2026 on the pilot `nights-frame-01`, which is the worked model: read it
before drafting your first night.*

## What a published unit is

One **night**, from its own opening formula (فلما كانت الليلة …) to the next night's formula —
the text's own sectioning, the way Beowulf has fitts. Never a page range: pages cut mid-sentence
and mean nothing to a reader. The frame material before Night 1 is cut by narrative episode
instead. `tools/nights_index.py` decides the boundaries; do not re-derive them by eye.

## Vocalisation — the core of the work

The edition prints prose essentially unpointed. **We supply complete tashkīl ourselves**: every
short vowel, sukūn, shadda, tanwīn and iʿrāb. This is an editorial act on every word and must be
declared in `source`. It is also where the value is — the reader's "bare" toggle strips it back
to exactly what Macnaghten prints, so the apparatus retracts as the reader grows.

Where the text's own grammar is non-Classical, **vocalise what the text actually says** and note
it. Do not repair Middle Arabic into Classical by way of the pointing.

### Hamza encoding — load-bearing, and it looks like a bug

The bare state strips U+064B–U+065F, U+0670 and U+06D6–U+06ED, and the result **must** equal the
archive character for character. So where we supply a hamza the edition does not print — and it
prints bare alif almost everywhere (اخيه, فان, الى, امراة, ياكل) — write base alif U+0627 plus
**combining** U+0654 (above) or U+0655 (below). **Never** the precomposed أ (U+0623) or إ
(U+0625): they survive the strip and would leave the bare script showing an orthography the
edition does not have.

Where the **edition itself** prints a precomposed character, keep it precomposed — it is in the
archive that way, and the strip test expects it. In the pilot passage that was exactly seven
words: الآخرين، بجزائر، دائمين، رآة، رآه، رأى، يسأل.

**Never run NFC over an Arabic story file.** A reviewer will eventually recommend it in good
faith, because decomposed hamza looks like an encoding defect. It would silently break the bare
state on every Arabic text in the library. `tools/validate_night.py` is the thing that decides.

**Defective spellings take the dagger alif.** Where the edition prints قل for قال, point it with
U+0670: it reads correctly, preserves the rasm, and strips cleanly.

## The three layers

- **`tr` — transliteration.** Simplified IJMES, as a line overlay (`trStyle: "line"`), never a
  column. House rule: the article is always written `al-` and **never elided** — `wa-al-salām`,
  `bi-al-samʿ wa-al-ṭāʿa`. Drafters split on this every time; it is not negotiable.
- **`l` — literal.** Structurally transparent: the reader should be able to see how the Arabic
  produces the meaning. Hyphenate glued concepts where it reveals structure ("the sent-ones",
  "the former-ones"). Stop before it becomes gibberish; coherence wins ties.
- **`i` — idiomatic.** Real English, elevated and lightly old-fashioned in diction and rhythm
  ("O my brother, I see that your body has grown feeble") — **modern "you/your", never
  "thee/thou"**. No archaic-pronoun pastiche. Omit `i` only where the literal is already natural.

**Rhymed prose (sajʿ) is pervasive** in the frame and the formulaic passages. Preserve it as a
feature: the literal layer should show where the rhyme falls rather than flattening it.

**Never bowdlerize.** The Nights is frank about sex and violence; that is why Calcutta II was
chosen over the censored Būlāq. Translate what is there, in both layers.

## Notes (`n`)

Middle Arabic is neither Classical nor MSA, and no grammar book prepares a reader for it. Treat
non-Classical forms as features to identify and move past, not as errors — the same posture as
archaic German. Flag a recurring construction the first few times, then nudge. Admit uncertainty
rather than papering over it: where a form is obscure or possibly corrupt, say so and name the
candidate, as the pilot does for ورحاق.

Notes address the reader, not the editor, and carry no house business.

## Glossary — shared, morphemic

Every unique word form, in the **shared** `nights-glossary.json` at the repository root, reached
by `"glossaryFile": "nights-glossary.json"`. Never an inline glossary: the Nights is long and
heavily inflected, and per-night glossaries would be enormous and near-duplicative.

Arabic glues proclitics and enclitics onto the orthographic word, so entries are written
**morphemically** — name the parts, then the lemma:

    "وبالبيت": "و + بِـ + الـ + بَيْت — bayt, house (m.); 'and in the house'"

**Keys stay vocalised** — that is what distinguishes كَتَبَ from كُتِبَ. The reader falls back to
the bare skeleton when an exact key misses, so a single absent fatḥa can never orphan a word.

Where glossing is split across agents, glosses diverge — the pilot's drafters produced 61 word
forms with conflicting entries. Either gloss over disjoint slices, or budget a reconciliation
pass. When adding to the shared file, **never overwrite an existing key with a different
meaning**: if the existing entry is wrong, fix it deliberately and say so in the LOG.

## What every night's metadata says

`source` — the Calcutta II edition and printed pages; that **all vocalisation is editorial**
(ours, not the edition's); that romanisation is simplified IJMES; that spelling including Middle
Arabic forms is preserved unaltered; and the audio convention, a Modern Standard Arabic reading,
stated as the admitted convention choice it is.

`about` — plainly, that every printed edition of the Nights including this one belongs to the
late Egyptian recension (ZER), an eighteenth-century expansion padded out to a literal 1001
nights; that **no printed edition is a medieval text**; and that Macnaghten regularised the
language here and there, so some Middle Arabic texture is a nineteenth-century retrofit. Honesty
is a feature, not a disclaimer to bury.

`work`/`workEn`/`part` — الف ليلة وليلة / The Thousand and One Nights / "Night 3", so the library
groups the nights together. `rtl: true`, `script: "arabic"`, `langCode: "ar-XA"`.

## Copyright

Draft only from the archive plus public-domain lexical aids (Lane's *Arabic-English Lexicon*,
Hava; Wehr is **not** public domain). The Nights has famous, distinctive modern translations and
the temptation is real. Two echoes caught in the pilot, both worth watching for again: rendering
بالسمع والطاعة as "To hear is to obey" — the most recognisable Nights catchphrase in English,
which also invents direct speech the Arabic does not have — and Burton's title form "The Thousand
Nights and a Night". Use "with hearing and obedience" unquoted, and "the Thousand and One
Nights". The *literal* layer legitimately produces "a thousand nights and a night"; that is
simply what the Arabic says.

## Audio

Prepared clips are the shipped experience for every text, and Arabic TTS is good, but the `ar-XA`
Action has **never been confirmed to produce clips** — it did not commit them for the pilot and
nobody has read the run log since (see `plan.md`, open items). So: publish the text without
audio, leave `audio` out of the story file, and do not spend a run chasing it. When the Action is
fixed, one pass adds audio to every published night at once.
