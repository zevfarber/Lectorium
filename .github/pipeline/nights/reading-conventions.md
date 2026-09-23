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

### Verse is copied, not vocalised

The edition **does** point its verse, and the archive keeps those marks exactly as printed. So a
verse line's archived text is already final: copy every pointed verse word from the archive
character for character — no added vowels, no added or re-encoded hamza, no "corrected" iʿrāb.
The only things that are yours in a verse block are the joins (` * ` between hemistichs, `\n`
between lines). The single exception is a verse word the archive leaves **bare**: that one you
vocalise, like prose. If a printed vowel looks wrong, keep it and say so in `n`.

This is checked by script, not by eye: `check_slice.py` and `validate_night.py` compare every
pointed verse word with the archive codepoint for codepoint, and `check_slice.py --fix` puts the
archive's word back. (Added 2026-09-23. On Night 8 drafters re-pointed printed verse, in three
places rewriting the archive's combining hamza as precomposed أ/إ; on Night 4 they had added
hamza the edition does not print. Both strip to the same letters, so the bare-strip check could
not see it.)

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

Nobody can see this defect — the two encodings render identically — so nobody is asked to look
for it. The orchestrator runs `tools/check_slice.py` on every drafting slice as it comes back
(publish-runbook.md 4a) and the night gate re-runs the same identity on the whole file. A
drafter's report that it "verified" its hamza encoding is not evidence and is not requested.

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

**Every prefix you name, you explain.** بِـ, لِـ and كَـ carry meaning, and it changes with
what governs them, so the entry has to say what the prefix does *here*: either in the parts
("bi-, with (prep.) + …") or in the quoted English ('and in the house'). "gen. after بِـ" alone
names the prefix without explaining it. Say so when the verb chooses the preposition (أَتَى بِـ
"bring", أَمَرَ بِـ "command", أَيْقَنَ بِـ "be certain of", مَرَّ بِـ "pass by"), and when the بِـ
follows إِذَا of surprise it only marks what appears (وَإِذَا بِغَزَالَةٍ "and behold, a gazelle").
The whole-night review agent checks this. (Added 2026-09-23: 68 entries through Night 8 split
off a بِـ or لِـ and left it unexplained; all were rewritten that day.)

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

Prepared clips are the shipped experience for every text. For the Nights they work as of
2026-09-21: the audio Action synthesizes one clip per sense unit with the pinned voice
`ar-XA-Chirp3-HD-Achernar` (a Modern Standard Arabic reading of the vocalised text) and writes the
word timings. So every story file carries `"audio": "audio/<id>"` from the moment it is published.
The Action starts by itself when the story file reaches main and commits `audio/<id>/` some
minutes later (up to an hour for a long night); until then Listen is silent for that night, which
is accepted. A publishing run writes the field and stops there — it never touches `audio/`, never
waits for the clips, and never spends time checking them.

(History: until 2026-09-21 the nights were published without the field. The clips had in fact been
built, but every word-timing list was empty, because the aligner's word splitter knew no Arabic
letters. That is fixed in `.github/scripts/wordre.py`, and the published nights were switched on in
one pass that day.)
