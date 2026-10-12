# Kebra Nagast (The Glory of Kings) — conventions (Run 3)

Distilled from the project's `geez-kebra-nagast-conventions.md` (2026-07-23) and the published pilot
`kebra-nagast-ch1.json` (Chapter 1), which is the model of shape and register.

## Source and the sole-source rule
- Text: Carl Bezold, *Kebra Nagast: Die Herrlichkeit der Könige* (Munich 1905) — public domain. The Geʿez is
  Ran HaCohen's Unicode text of Bezold (tau.ac.il/~hacohen/KN, from Michal Jerabek's 1995 digitization),
  archived 2026-10-12 as `source/kebra-nagast-bezold1905.json` (chapters 1–117 + the colophon, paragraphs as
  in HaCohen). Checked: chapter 1 is character-identical to the published pilot; chapter 82 was compared
  with Bezold's printed page by eye and agrees. Never retype the Geʿez; cut it from the source by script.
- Lexical aid: Dillmann, *Lexicon Linguae Aethiopicae* (1865). Budge's 1922 English may be consulted
  silently as a meaning check on a hard passage only — never for wording. Modern translations are never opened.

## Data model
Words model with a MECHANICAL interlinear (`hooks.py`): the drafter writes sense-units `{t, l, i, n, p?}`;
the build makes each word's per-sign transliteration from Unicode names, the word `reading` (schwa rule:
6th-order ə kept word-initially and after a consonant, dropped word-finally and after a vowel), the
readable `say`, the unit's `tr`, and every word's morph from the glossary. Numerals are words: Ethiopic
digits get role `num`; ወ between numerals is "and".
- Unit = a sense-unit ending at ። ፤ or ፨ (the last unit of a part may end where the part ends). The chapter
  heading (e.g. ፪ ፡ በእንተ ፡ ዕበየ ፡ ነገሥት ።) is its own unit with `p: true`; the first unit of each paragraph has
  `p: true`. A unit longer than ~45 words is cut at a ፤.
- Glossary: inline per part, keyed by the word form exactly as written (proclitics included: ወዜና, ለደቂቀ),
  value `"<lemma in Geʿez> — <meaning> (<grammar>)"`; the morph shown in the popup is built from it, so the
  lemma before " — " must be the dictionary form. A form already glossed in a published part reuses that
  entry (broaden it if this use is new). Numbers: the entry gives the spoken Geʿez number words with our
  transliteration (decided 2026-07-23): ፫፻፲ወ፰ → "spoken ሠለስቱ ምእት ወዐሠርቱ ወሰመንቱ (śälästu məʾət wä-ʿäśärtu
  wä-sämäntu) 'three hundred and eighteen'".

## Orthography and transliteration
Bezold's fidäl exactly; the wordspace ፡ tokenizes. Transliteration: ś = ሠ-series, ʿ = ዐ-series, ə = 6th
order, 1st order ä, 4th order a; labiovelars kʷ, gʷ, qʷ, ḫʷ. The word-level romanization is approximate and
the source statement says so.

## Translation and notes
- `l` structurally transparent (construct chains as "glory-of kings", proclitics hyphenated: "and-account");
  `i` real English, dignified and plain — a royal-ecclesiastical chronicle, never faux-archaic.
- Notes: the construct state, the proclitics ወ- ለ- በ- ዘ- እም-, verb stems and their prefixes, scriptural
  allusions named plainly (Genesis 1:26, Psalm 74:2), the Zion/Ark (ታቦት) theology, Ethiopian names and
  places. Flag a recurring pattern on first occurrence, then nudge.
- Proper names in Geʿez form in `l`, conventional English in `i` (ሰሎሞን Solomon, ንግሥተ ሳባ the Queen of Sheba,
  ማክዳ Makeda, ምኒልክ Menelik, ጽዮን Zion).
- Uncertain words are said to be uncertain; cruxes resolved against Dillmann say so.

## Honesty
A 1905 critical edition, digitized; the Geʿez is proofed against HaCohen's text; word-level romanization is
mechanical; translations are fresh. The owner reads some Geʿez (2026-10-11) but no text waits for a human
check (his ruling, 2026-10-11).

## Pronunciation and audio
`langCode: null`. The pronunciation convention (traditional Ethiopian liturgical vs reconstructed Geʿez) and
the voice are NOT yet chosen by the owner; parts publish without audio until he chooses (Run 3 setup,
2026-10-12). Do not build audio.

## Decisions taken while setting up Run 3 (2026-10-12)
- Parts: chapters 2–117 and the colophon; short chapters grouped to ~300–600 words, a chapter over 650 words
  cut at the ። nearest an equal division (86 parts; see plan.md). Part titles are ours, from the action.
- The mechanical transliteration of ዘ before a numeral is now per sign (zä), where the pilot hard-coded "za";
  the reading of such a word is still "za-318".
