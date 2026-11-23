# Book of the Dead of Ani — conventions

The work is the Papyrus of Ani (British Museum EA 10470) as a whole, read from E. A. W. Budge's 1895 interlinear
edition. The model of shape, register and depth is the published part `ani-spell125-opening.json` (the 42
declarations of Spell 125, built by hand with the owner in July 2026): read it before drafting, and reuse its
lemma spellings, glosses and renderings. Background: project docs `claude/egyptian-script-model.md` (the word /
glyph / morph model) and `claude/egyptian-audio-status.md` (the pronunciation convention).

Owner's order (2026-11-16): the rest of Spell 125 first — its introduction and its rubric — then the papyrus
from Plate I to the end. 51 parts (`parts.json`), one of them a marked supplement.

## What is Ani's text
Budge prints three things in the same hieroglyphic type; only the first is the papyrus:
1. **Ani's text** — under each "PLATE n." heading: chapter titles, the chapters, rubrics, and the words written
   beside the figures in the vignettes. All of it is published.
2. **Appendix sections** — headed "Appendix.", supplied from Naville's *Todtenbuch* or other papyri (Nebseni, Nu…)
   where Ani's scribe left a chapter short or out. In his Table of Chapters these are the chapters in [brackets].
   Left out. The note on the unit before the gap says, in one sentence, what other papyri have at that point.
3. **Footnotes**, some of which print a "less corrupt" parallel text in hieroglyphs. Left out; where a footnote
   shows that Ani's scribe has garbled a passage, the note says so and translates what Ani has.
Words Budge sets in [ ] in the text line are his restorations of damage: kept, flagged `"restored": true` on the
glyphs, and the note says they are restored. The speculation principle applies throughout: this is an 1895
printed transcription of a scribe's cursive hieroglyphs; say plainly where a reading is doubtful.
**One supplement** (owner's ruling, 2026-11-16): the address to the gods that other papyri have after the
Confession — Budge's Appendix on pp. 203–212, which Ani's papyrus does not have — is published as its own part,
`ani-125-address`, marked for the reader as not on Ani's papyrus (the build puts the mark on its first unit and a
different source statement; `titleEn` / `part` say "supplement"; the `about` says in plain words that Ani's scribe
stopped at the declarations and that this is how other papyri go on). Its notes never speak of "Ani's scribe" as
the writer; where the text names the dead person, say whose name Budge's source has. No other Appendix is
published.

## The scribe's mistakes
Ani's papyrus is beautiful and careless. Under the misprints rule (../README.md 5b) a slip the sense allows only
one way to read — a dropped or doubled sign, a wrong determinative — is corrected *in the reading and the
translation*, never in the signs: the glyphs always show what the papyrus has (as Budge prints it), `reading`
gives the word meant, and the note opens "The papyrus writes X; read Y." Where more than one reading is possible,
translate what stands and say so. Budge's own misprints (a transliteration that does not match his signs) follow
the signs.

## Signs
- Every glyph is a Gardiner code; the character comes from Unicode by code (hooks.py), never typed.
- `role` is what the sign does *in this word*: `phon` (phonogram, one or more consonants), `comp` (phonetic
  complement: repeats a consonant already carried by a multiliteral sign; its `tr` is that consonant), `det`
  (determinative; `tr` empty), `log` (logogram / ideogram writing the whole word, with or without the stroke Z1;
  the stroke itself is `det` with empty tr), `suff` (suffix pronoun written as its own sign(s)), `num` (numeral).
- `tr` chunks are per glyph; the word's `reading` is separate (complements double letters, determinatives add none).
- A sign not yet in `signs-egyptian.json` is added with `python3 ../run3/signs.py add egyptian <code> 'EGYPTIAN
  HIEROGLYPH <X000>' '{"name": …, "type": "uniliteral|biliteral|triliteral|logogram|determinative|…", "sound": …,
  "pron": null, "determines": …}'` — entries describe the sign in general (all its common values), in the style
  of the 86 already there. `signs.py check` must say "in sync".
- Layout `q` is carried from the established file (Budge's type). It is the layout of the print, which
  regularises the scribe; the source statement says so.

## Transliteration and the "say" line
- Leiden convention, reed written `i` (as the published part): ꜣ i y ꜥ w b p f m n r h ḥ ḫ ẖ s (z where the
  sign is the bolt, written s in `say`) š q k g t ṯ d ḏ. Suffix pronouns joined with `·` in `reading` (`ḏd·i`).
  Compound names hyphenated (`wsḫ-nmtt`).
- `say`: the classroom pronunciation, by rule: e between consonants; ꜣ, ꜥ → a; w → u (w before a vowel);
  i, y → i / y; ṯ → tj; ḏ → dj; ḫ, ẖ → kh; š → sh; ḥ, h → h; q → q. Gods and places with a settled modern name
  take it (Osiris, Anubis, Thoth, Ra, Maat, Horus, Isis, Atum, Ptah); for any other name, check how the published
  parts say it before coining a form. *prj* "come forth" is `peri`; *pr* "house" is `per`; *m* is `em`.
- **Budge's transliteration** (1895) is a check on the signs, never the reading shown. His letters: à = reed (i);
  ā = arm (ꜥ); a = vulture (ꜣ); i, ī = double reed / strokes (y); u = quail chick or coil (w); χ = ḫ / ẖ;
  θ = ṯ; t' = ḏ; ś = š; ṭ = d (hand); t = t; ḥ = ḥ; h = h; q = q; k = k; ḳ = g; s = s and z; his vowels e are
  his own insertions. His divine names are the old conventional ones (Àusàr = Osiris wsir, Ànpu = Anubis inpw,
  Ḥeru = Horus ḥr, Teḥuti = Thoth ḏḥwty, Sut = Seth stẖ / swty).

## Units and translation
- One unit per sentence or per clause-group that reads as one thought; a chapter title or a rubric is its own
  unit. `ln` = the papyrus line (Budge's numeral) in which the unit begins; `"p": true` on the first unit of a
  chapter, rubric or speech. A unit with rubric words says in its note that the papyrus writes them in red.
- `l`: structurally transparent English in the Egyptian's order where English can bear it (verb–subject shown
  where it teaches: "comes-forth he"), never gibberish. `i`: real English, lightly formal; no Budge-isms
  ("triumphant", "saith", "homage to thee" are his 1895 wording: build from the grammar — *mꜣꜥ-ḫrw* is "true of
  voice / vindicated").
- Notes lead with what the reader needs to read these signs: which sign carries which sounds, the complement,
  the determinative and what it classifies, the verb form, the idiom; then the religious background in a
  sentence. Recurring things (the suffix pronouns, *mꜣꜥ-ḫrw*, *Wsir N* "the Osiris N", the sḏm·n·f) get a full
  note the first few times in the work and a nudge afterwards.
- Glossary: one entry per lemma, `lemma — meaning (grammar)`, general to the lemma. Names of gods, demons and
  places: the meaning of the name where it is transparent, and Budge's old spelling in brackets as the published
  part does ("(Budge: Usekh-nemtet)") so a reader with an old translation can find it.
- No modern translation is opened or recalled (Faulkner, Allen, Quirke, Goelet…). Budge's English under each
  word is in the packet as a 130-year-old check on sense only.
- House renderings (from published parts): Spell 147's ꜥryt is "gate" (Budge "hall"), each gate with its doorkeeper (iry-ꜥꜣ), watcher (sꜣwty) and announcer (smi); Budge's line numerals restart in each gate and `ln` keeps them as printed.
- Never bowdlerise; the content advisory rules of the project apply where a chapter calls for one.

## Titles
Story `title` is the work's Egyptian title (work.json). `titleEn`: "Book of the Dead of Ani — <part name>";
`part`: the part name with the plate, e.g. "Spell 125 — entering the Hall of the Two Truths (Plate 30)". Use
"Spell" for Budge's "Chapter". Plate numbers in Arabic numerals for the reader.

## Voice
The declarations were voiced by hand with the owner approving every take (a voice that reads differently each
time). That cannot be repeated for a book. No voice is settled for the rest: parts publish without audio, with
`say` filled in, until the owner chooses one (QUESTIONS.md). The run never builds audio.
