# Beowulf — editorial conventions

Distilled from the project's Old English rules (decided July 2026) and the three parts published in July
(`beowulf-prologue.json`, `beowulf-fitt-01.json`, `beowulf-fitt-02.json` in the repository root). Those three files
are the model of shape, register and note-writing: read at least one whole before drafting.

## The text

- **Edition:** Fr. Klaeber, *Beowulf and the Fight at Finnsburg*, 1st ed., 1922 — public domain everywhere. The whole
  poem is in `source/beowulf-klaeber1922.json`, transcribed from the page images on 2026-09-30 (every page read twice,
  every disagreement settled on the page). It is the only text. Never draft from memory of the poem.
- **Sole-source rule:** draft only from Klaeber's text plus public-domain lexical aids (Klaeber's 1922 glossary,
  Bosworth–Toller 1898, Clark Hall). No modern translation is opened or recalled for wording — Heaney, Tolkien,
  Chickering, Liuzza and the rest are in copyright and the famous passages tempt echoes. An English phrase that arrives
  fully formed is rebuilt from the grammar.
- **What the characters mean** (see the source file's `encoding`): þ ð æ as printed; macrons mark long vowels; a
  circumflex marks a contracted vowel — Klaeber prints one mark over a pair of vowels and we place it on the second
  (Līffreâ, geþeôn, heân); a dot under a vowel (dōgọra, trūwọde) is Klaeber's sign that the vowel does not count in the
  metre — explain it the first time a part meets one; ę is e caudata; `[ ]` = letters or words Klaeber added by
  emendation; `( )` = letters restored where the fire-damaged manuscript is lost; rows of dots = words lost; † = a
  passage Klaeber marks as corrupt. Klaeber's italics (letters he changed) are listed in the packet, not marked in `t`.

## Everything is speculative, and the reader is told so

The single manuscript was scorched in 1731; its edges are lost and some readings survive only in the 1787 Thorkelin
transcripts; the poem is full of words that occur nowhere else. Every part carries the standing `about` paragraph (the
build copies it). Notes admit uncertainty instead of papering over it: a word whose meaning is guessed is called a
guess; where Klaeber emends (brackets, parentheses, italics), the note says what the manuscript has when the packet's
apparatus gives it and it matters for the sense.

## Units

- The unit is Klaeber's punctuated sense-unit. It may begin or end in mid-line (Klaeber punctuates across the line
  constantly), but a line is never broken anywhere else: `t` holds whole verse lines joined by `\n`, except where the
  unit starts or ends at a mid-line punctuation mark. Every unit has `v: true` and `ln` = the line it starts on.
- `t` is cut from the packet's lines by a small script, never retyped.
- Long sentences may be cut at any semicolon or colon; eight lines is the ceiling for one unit.

## The three layers

- **`l` (literal):** structurally transparent where English can bear it, and stops before it becomes gibberish —
  Old English word order is freer than German's, and coherence wins ties. One paragraph (no line breaks).
- **`i` (idiomatic):** real English a person would say, lightly old-fashioned in register, never childish. Omit it only
  where it would equal `l`.
- **`n` (note):** on (nearly) every unit — the published parts sit at 95–100 % and that is the standard, not a defect to
  trim. Lead with what the reader needs to read these words: the grammar that produces the sense (case, mood, word
  order), then the word or kenning, then culture or story where it helps. Quote Old English in single curly quotes
  (‘…’). Plain sentences; no assert-by-negation, no vague atmospheric closers, no abstract aphorisms.

## Recurring treatments

- **Kennings and compounds:** hyphenated-literal in `l` ("whale-road", "bone-house"), unpacked in `i` ("sea", "body"),
  explained in a note on their first occurrence in the poem, a short nudge thereafter.
- **Proper names** stay untranslated as Klaeber prints them (Bēowulf, Hrōðgār, Grendel, Higelāc); the glossary gives
  their meaning or identity.
- **House renderings already set** (do not relitigate): `Hwæt` = "What!" in `l`, "Listen!" in `i`. Before choosing an
  English rendering for a recurring word or formula (maþelode, the speech introductions, epithets of God, of Beowulf, of
  Hrothgar), search the published parts (`grep` the root `beowulf-*.json`) and reuse what they chose. A new formula that
  will plainly recur gets a rendering chosen with care and recorded in the table below.
- **A famous crux** with no house rendering: render it from the lexica as plainly as the grammar allows, say in the
  note that the reading is disputed, and write it to `QUESTIONS.md` with what you chose.

## Glossary (`beowulf-glossary.json`, shared by every part)

- Key = the word as printed, lowercased, brackets and parentheses stripped (þon[n]e → þonne) — exactly the reader's
  `wordKey()`. Dots below and circumflexes are part of the key (dōgọra, heân).
- Entry: `"lemma — meaning (parse; brief remark)"`, general to the form, never pinned to a line: no line numbers, no
  "here". Names give identity ("Hrōðgār — Hrothgar, king of the Danes, son of Healfdene").
- Additions only. An existing entry may be broadened (the old entry whole, then " · " and the new reading) under
  `"__broaden__"`; it is never rewritten.

## House renderings added by runs

| form | l | i | first used |
|---|---|---|---|
