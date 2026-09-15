# Bhagavadgītā — editorial conventions (from the chapter 1 pilot, 2026-09-15)

## Text
- The received (vulgate) text, as read by Śaṅkara's commentary: Mahābhārata 6.23–40, 18 chapters, 700 verses.
- Two independent witnesses are collated for every chapter before drafting: the Devanagari of
  Sanskrit Wikisource (भगवद्गीता/<chapter name>) and the IAST of the GRETIL e-text "Bhagavadgītā with
  Śaṅkara's commentary" (bhgsbh_u.htm; chapters 1–17 — chapter 18 needs another witness).
  Discrepancies are adjudicated by the Śaṅkara reading where his gloss shows it, otherwise by the
  common printed vulgate, and every real variant gets a note. Orthographic differences (anusvāra vs
  class nasal, e.g. पुङ्गव/puṃgava) are not variants. Collation against a pre-1930 printed edition
  is still pending and is stated as pending in `source`.
- Chapter 1 adjudications: 1.8 saumadattis tathaiva ca (not saumadattir jayadrathaḥ); 1.22
  nirīkṣe (Wikisource misprint nirikṣe corrected); 1.44 narake 'niyatam (Śaṅkara), variant niyatam noted.

## Unit and layout
- One verse = one unit: `ln` = verse number, `v: true`, `t` = the two half-verse lines joined by
  `\n`, each ending in its daṇḍa (। and ॥); verse numbers are not in `t` (the `ln` chip shows them).
  `numbering: "stanza"`; the chapter is the part.
- Speaker lines (धृतराष्ट्र उवाच etc.) are their own units with `p: true` and no `ln`, literal
  "Dhṛtarāṣṭra said", no `i`. The `i` of the following verse does not repeat "X said".
- Script `devanagari`, `langCode: null`, no audio yet.

## Words model (the sandhi layer)
- Every space-delimited Devanagari token is one `words` entry with one glyph (`s` = the token as
  written) and `reading` = the same token with sandhi undone and compound members hyphenated, IAST.
  The last token of each half-line carries a second glyph for the daṇḍa (`role: "punct"`, `tr: " "`).
  The first token of the second line carries `br: true`.
- `reading` rules: sandhi is undone to dictionary-boundary forms (pāṇḍavāḥ ca eva, not pāṇḍavāś
  caiva); final -m is written -m, not -ṃ; an avagraha's lost a- is restored (tumulaḥ abhavat);
  compounds are hyphenated between members (dharma-kṣetre, lupta-piṇḍa-udaka-kriyāḥ) and the
  vowel fusion inside a compound is undone at the hyphen (mahā-iṣvāsāḥ).
- `morph`: one entry per word or compound member, in order: `lemma` = dictionary stem (verbs by
  root with prefixes, e.g. abhi-rakṣ; names in IAST with capital), `gloss` = meaning, then in
  parentheses the form and, on its first occurrences, the sandhi that produced the surface
  (`-aḥ + c- → -aś c-`). Every `g` is `[0]` (one glyph per word).
- Proper names stay untranslated in `l` and `i`; epithets are translated in `l` on first use
  ("Lord-of-the-senses") and given as the name in `i` (Kṛṣṇa), the meaning going in the gloss.
- Untranslated terms in `i`: dharma (when it means the cosmic/social order; "law" when it is
  kula-dharma), yoga, brahman, the three guṇas. Everything else is translated.

## Translations and notes
- `l`: structurally transparent; hyphenate the compounds as in the reading; keep the Sanskrit
  order where English bears it, stop before word-salad. `i`: real English, lightly formal, never
  archaic-for-effect. Never bowdlerize.
- Notes lead with what the reader needs to read the verse: the sandhi or compound that hides the
  words, the construction (gerund chain, locative absolute, gerundive, relative-correlative), then
  who the names are. Recurring patterns are flagged fully the first two or three times, then nudged.
- Sole-source rule: draft from the Sanskrit with Monier-Williams (1899) and Apte (1890) and, for
  the traditional sense, Śaṅkara's commentary. No modern translation is opened. Famous verses get
  house renderings decided before drafting: 2.47, 4.7–8, 11.32, 18.66 (to be set when their chapters
  are reached) and are echo-scanned against Edgerton, Zaehner, Miller, Easwaran, Prabhupada at
  validation.

## Glossary
- The story's `glossary` is keyed on the Devanagari token exactly as written (for the tutor's
  context lookup; the reader's tokenizer now covers Devanagari) with value
  `reading — lemma — gloss; lemma — gloss`. A shared work-level glossary keyed on lemmas can come
  when several chapters exist.

## Validation (build.py does all of this and stops on failure)
- The Devanagari tokens of the words, joined with spaces, equal the Wikisource lines exactly
  (after the adjudicated corrections, each of which is named in a note).
- Every verse has l; i unless equal to l; every word has a reading and at least one morph;
  every token has a glossary key. JSON parses. Readings' letters sanity-checked against the
  surface transliteration.
