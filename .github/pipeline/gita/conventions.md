# Bhagavadgītā — editorial conventions (from the chapter 1 pilot, 2026-09-15)

## Text
- The received (vulgate) text, as read by Śaṅkara's commentary: Mahābhārata 6.23–40, 18 chapters, 700 verses.
- Two independent witnesses, both in `source/`, are collated for every chapter before drafting:
  `wikisource-chNN.txt`, the Devanagari of Sanskrit Wikisource (the vulgate), which is the text we
  print, and `bori-iast.txt`, the GRETIL romanized text based on the BORI critical edition (input
  Tokunaga, rev. J. Smith) — all 700 verses, one uniform witness. `gita_lib.collate(NN)` lists the
  differences: `orth` (anusvāra vs class nasal, candrabindu, sandhi written or not) is nothing;
  `VAR` is either a Wikisource misprint — corrected in `source/corrections.json`, each correction
  named in its verse's note — or a real vulgate/BORI variant, listed per chapter in `parts.json`
  as `variantsVsBORI`; the note of such a verse states the BORI reading. The vulgate is the base
  text throughout; the BORI reading is never adopted, only reported. Collation against a pre-1930
  printed edition is still pending and is stated as pending in `source`.
- Adjudicated so far (all in `corrections.json`): 1.22 nirīkṣe; 5.5 sa paśyati (stray colon);
  5.8 śṛṇvan; 16.19 krūrān. Real variants: 1.28, 1.34, 1.37, 2.5, 2.26, 3.2, 3.8, 6.7, 6.41, 8.7,
  11.16, 11.20–22, 11.32, 12.18, 13.20, 14.18, 14.25, 16.4, 16.13, 17.6, 18.25, 18.28, 18.43, 18.44,
  18.51, 18.66, 18.68 (see `parts.json`).

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
  kula-dharma), yoga, brahman, the three guṇas, sāṃkhya (named in 2.39 as yoga's structural
  counterpart, and again from 3.3 on as one of the poem's two named paths — not "analysis" or
  "reasoned discernment"). Everything else is translated.

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
  are reached) and are echo-scanned at validation (`validate_gita.py` carries a short red-flag list).

## House renderings — use as written when the chapter is reached
- 2.47 l: "In action alone is your entitlement, never in its fruits; do not let the fruit of
  action be your motive, and let there be no attachment of yours to inaction." i: "Your claim is to
  the action itself, never to what comes of it. Do not act for the sake of results, and do not
  cling to not acting either."
- 4.7 l: "Whenever indeed of dharma a fading comes to be, O Bhārata, a rising-up of adharma —
  then I send forth myself." i: "Whenever dharma wanes, Bhārata, and its opposite rises, I bring
  myself forth."
- 4.8 l: "For the rescue of the good and for the destruction of evil-doers, for the purpose of
  establishing dharma, I come to be age after age." i: "To rescue the good, to destroy those who do
  evil, and to set dharma firmly in place, I am born in every age."
- 11.32 l: "Time I am, world-destruction-making, grown-great, here set-in-motion to gather in the
  worlds; even without you, all these warriors standing in the opposing ranks will not be." i: "I
  am Time, grown vast, the wrecker of worlds, at work here to gather the worlds in. Even without
  you, none of the warriors drawn up in the facing lines will survive." (kāla is Time; the famous
  'Death' is a translator's choice we do not follow.)
- 18.66 l: "All dharmas having abandoned, to me alone as refuge come; I you from all evils will
  free — do not grieve." i: "Let go of every duty and come to me as your one refuge. I will free
  you from all evil; do not grieve."

## Speaker lines
- धृतराष्ट्र उवाच / सञ्जय उवाच / अर्जुन उवाच are two tokens; श्रीभगवानुवाच is written as one token on
  Wikisource and is kept as one word with three morphs (śrī, bhagavat, vac); its literal is "The
  Blessed Lord said". `build_gita.py` generates all speaker units; the drafter does not write them.

## Drafts folder
- `drafts/chNN/words.txt`, `trans.txt`, `about.txt` are committed with the chapter so a later run
  can rebuild or correct it. Their formats are documented at the top of `build_gita.py`.

## Glossary
- The story's `glossary` is keyed on the Devanagari token exactly as written (for the tutor's
  context lookup; the reader's tokenizer now covers Devanagari) with value
  `reading — lemma — gloss; lemma — gloss`. A shared work-level glossary keyed on lemmas can come
  when several chapters exist.

## Validation (build_gita.py and validate_gita.py do all of this and stop on failure)
- The Devanagari tokens of the words, joined with spaces, equal the Wikisource lines exactly
  (after the adjudicated corrections, each of which is named in a note).
- Every verse has l; i unless equal to l; every word has a reading and at least one morph;
  every token has a glossary key. JSON parses. Readings' letters sanity-checked against the
  surface transliteration.
