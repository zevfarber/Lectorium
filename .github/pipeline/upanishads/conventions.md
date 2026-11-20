# The Upanishads — editorial conventions (set up 2026-11-20)

Five principal Upanishads, chosen by the owner: Īśa, Kena, Kaṭha, Muṇḍaka, Māṇḍūkya. The words model,
the reading line and the translation rules are the Bhagavadgītā's (`../gita/conventions.md`, which
is the model for everything not said here; `../../../gita-ch01.json` is the model file).

## Text
- The received (vulgate) text as given by Sanskrit Wikisource, fetched 2026-11-20 and kept in
  `source/wikisource-raw/`. `source/<part>.txt` is that text cleaned of wiki markup and split into
  one file per section; `source/wikisource-raw/make_sources.py` made them, and `source/manifest.json`
  lists every change beyond mechanical cleaning (a verse number supplied in Kaṭha 1.1.1, Kaṭha
  1.1.3–4 split apart, Kaṭha's closing invocation un-numbered, Muṇḍaka 2.2.7 rejoined, page headings
  dropped). None changes a word. The text in `source/` is the text we print: never edit it while
  drafting. A misprint found while drafting goes to `QUESTIONS.md`; the unit's note says what the
  text should read, and the text stays as it is until the owner rules.
- Witnesses (`source/witness/`, GRETIL): the Kaṭha (after Olivelle 1998), the Īśā in the Kāṇva
  recension with Śaṅkara's commentary, and the Māṇḍūkya. They are checks, never the text and never
  copied. Where the printed text and the witness differ in a word (not in orthography: anusvāra vs
  class nasal, candrabindu, sandhi written or not), the note gives the witness's reading. Kena and
  Muṇḍaka have no witness here; doubtful readings are checked against Śaṅkara's commentary.
- Vedic marks: Wikisource writes the Vedic anusvāra as ꣳ (U+A8F3) in places and candrabindu ँ for
  final -ṃ before some consonants (तँ, विद्यायाँ). Keep them in the text exactly; the reading
  normalizes them (taṃ / tam, vidyāyām). Pluta (३, the drawn-out vowel, Kena 4.4) stays in the text
  and is explained in the note.

## Units and layout
- One source block = one unit, in order. A numbered unit carries `ln` (the section's own verse or
  paragraph number); an unnumbered unit (the peace invocation, a heading such as ॥ अथ … ॥, a colophon
  ॥ इति … ॥) has `p: true` and no `ln`. Every unit is `v: true` with the source lines as its lines,
  prose included (the prose sections keep Wikisource's line breaks).
- The daṇḍas stay in `t` as written; the build attaches them to the neighbouring word as punctuation
  glyphs. The drafter lists only the words.
- The library lists each part under its Upanishad (`group` in stories.json: Īśa, Kena, Kaṭha,
  Muṇḍaka, Māṇḍūkya) in the order of `seq`.

## Words model and translation (as the Gītā)
- `words.txt` / `trans.txt` / `about.txt` in `drafts/<part>/`, formats at the top of `build_up.py`.
  Keys are the unit's place in the part (#1, #2, …), numbered unit or not.
- `reading` undoes sandhi and hyphenates compounds (pada-pāṭha style); `morph` lemma + gloss with the
  form in parentheses and, on first occurrences, the sandhi that produced the surface.
- `l` structurally transparent; `i` real English, lightly formal. Never bowdlerize.
- Untranslated in `i`: brahman (the absolute; Brahmā the god is a name), ātman where the text is
  speaking of the Self as a technical term (else "self"), Om, dharma, yoga, the names. Everything else is
  translated. Om/ॐ is "Om" in both layers.
- The peace invocations recur: translate them fully the first time each occurs in the work, and the
  same way every time after; the note of a repeat says only where it was first explained.
- Notes lead with what the reader needs to read the unit: the sandhi or compound that hides the words,
  the construction, then the imagery or doctrine in one or two plain sentences. Recurring patterns are
  flagged fully the first two or three times, then nudged.
- Sole-source rule: draft from the Sanskrit with Monier-Williams (1899) and Apte (1890) and, for the
  traditional sense, Śaṅkara's commentaries. No modern translation is opened.

## House renderings for the famous passages (use as written)
- Īśa 1, ईशा वास्यमिदँ सर्वम्: l "By the Lord to-be-dwelt-in (is) this all"; i "All this is for the Lord
  to dwell in, whatever moves in this moving world."
- The pūrṇam invocation (ॐ पूर्णमदः पूर्णमिदम्…): l "Full (is) that, full (is) this; from the full the
  full is raised up; of the full the full having taken, the full alone remains." i "That is whole and
  this is whole. Out of the whole the whole arises. Take the whole from the whole, and the whole is
  what is left."
- Kaṭha 1.3.14 उत्तिष्ठत जाग्रत: l "Stand up! Be awake! Having reached the excellent ones, understand!
  A razor's sharpened edge, hard to cross — a hard path, the poets say, is this." i "Get up and wake!
  Go to those who know and learn from them. The poets say this road is as hard to walk as the
  whetted blade of a razor."
- Kaṭha 1.3.3–4 the chariot: ātman = the rider (rathin), body = the chariot, intellect (buddhi) = the
  charioteer, mind (manas) = the reins, senses = the horses. Keep these five words fixed.
- Muṇḍaka 3.1.1 द्वा सुपर्णा: l "Two fine-winged ones, joined companions, embrace the same tree"; i "Two
  birds, close companions, cling to the same tree."
- Muṇḍaka 3.1.6 सत्यमेव जयते: l "Truth alone conquers, not untruth"; i "Truth alone prevails, not
  falsehood." (India's national motto — say so in the note.)
- Māṇḍūkya: the four states keep their Sanskrit names in `i` after a first gloss: jāgrat (waking),
  svapna (dream), suṣupti (deep sleep), turīya ("the fourth"); and their selves vaiśvānara, taijasa,
  prājña.

## Glossary
- Per part, keyed on the Devanagari token exactly as written, value `reading — lemma — gloss; …`
  (the build makes it). The same token gets the same gloss across parts: the glosser checks the
  published parts' glossaries for a token before writing a new gloss.
