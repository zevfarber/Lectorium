# Drafter brief — ani-125-address (one of four chunks)

You are drafting part of the Lectorium edition of the Book of the Dead: part `ani-125-address`, the address to the gods
that other papyri add to Spell 125 after the 42 declarations (Budge 1895, pp. 203–213, his Appendix from Naville's
Todtenbuch). It is a SUPPLEMENT — not on Ani's papyrus. Your notes never speak of "Ani's scribe" as the writer
(say "the scribe", "the copyist", "Naville's text", "the papyrus Budge follows"), and Ani is not named in this text.
The work's folder is /home/user/Lectorium/.github/pipeline/ani/ . Read, and use only:
- conventions.md (the rules; follow exactly)
- drafts/ani-125-address/packet.md — the established words; you draft ONLY your index range (below)
- drafts/ani-125-address/known-lemmas.json — lemma keys and glosses already used; reuse these keys and spellings
- /home/user/Lectorium/ani-spell125-opening.json (the model of shape, register and depth) and
  /home/user/Lectorium/ani-125-introduction.json (the most recent published part; same schema, read several units)
No modern translation is opened or recalled (Faulkner, Allen, Quirke, Goelet, etc.). Budge's English in the packet is
a 130-year-old check on sense only — never take wording from it; build every English phrase from the grammar.
Do not use the web.

## Output
Write /home/user/Lectorium/.github/pipeline/ani/drafts/ani-125-address/chunks/units-<X>.json :
{"sentences": [ unit, unit, ... ]}  with each unit
{"ln": <Budge's line number where the unit begins, int>, "p": true (first unit of a speech/section only),
 "l": "...", "i": "...", "n": "...",
 "words": [{"reading": "ḏd·i", "say": "djedi", "q": "0:1-2",
            "glyphs": [{"sign": "I10", "role": "phon", "tr": "ḏ"}, ...],
            "morph": [{"lemma": "ḏd", "g": [0, 1]}, {"lemma": "·i", "g": [2]}]}]}
Build the glyph lists BY SCRIPT from the packet / the established file
(source/established/ani-125-address.json, key "words", each with "signs", "q", "budge", "gloss", "unsure",
"approx", "restored") — never retype codes. Copy `q` from the established word; if you join two established words
into one, re-index q (second word's indexes shifted, joined with "-") ; if you split one, re-index from 0.
Every established sign in your range must appear exactly once, in order — nothing added, nothing dropped.
Carry "approx": true / "restored": true onto the glyph where the established word has approx (codes list) / restored.
roles: phon, comp (complement; tr = the consonant repeated), det (tr ""), log, suff, num — as in conventions.md.
morph g-lists must cover every glyph of the word exactly once. Determinatives belong to the lemma's g-list.
No "s", no "t", no "gloss" in morph (unless this occurrence truly needs its own wording).
"say" per the conventions' rule; for suffixes joined without a hyphen as in the introduction (djedi, rekhkui...).
Check how the two published parts write recurring words and copy them.

## Lemma keys
Reuse known-lemmas.json keys exactly (pr, n, ir, sš have homographs under one key — keep that). For a new lemma use
the bare Leiden citation form (verb stem / masculine singular noun / name as reading), no suffix; suffix pronouns
are their own lemmas as in the published parts (·i, ·k, ·f, ·tn, ·n, ·s, ·sn ...). Also write
chunks/lemmas-<X>.json: {lemma: "lemma — meaning (grammar)"} for EVERY lemma you used that is NOT in
known-lemmas.json, general to the word, never pinned to a line; names of gods/places: meaning where transparent and
Budge's old spelling in brackets "(Budge: Hept-re)". (A glosser will refine these; give your best.)

## Units and notes
One unit per sentence or clause-group (questions and answers of the dialogue are separate units; each door-part's
speech is its unit, the name-answer its own). "p": true on the first unit of a new speech or section.
`l`: transparent English in Egyptian order, words separated as in the model (look at how the model writes l).
`i`: real English, lightly formal, no Budge-isms ("homage", "saith", "triumphant", "thee/thou" are out).
`n`: lead with what the reader needs to read THESE signs (which sign carries which sounds, complements,
determinatives, verb form, idiom), then background in a sentence. Be honest: where the reading or the sign is
doubtful (packet UNSURE / approx flags, untransliterated groups, Budge's "(?)") say so plainly. Where the type is
plainly corrupt and only one reading makes sense, the misprints rule applies: glyphs stay as printed, `reading`
gives the word meant, note opens "The text writes X; read Y." Otherwise translate what stands and say it is
uncertain. Where Budge brackets a word ([...]) the glyphs are restored: say so. Where you join/split Budge's word
groups, say so in the note. Recurring items (suffixes, sḏm·n·f, mꜣꜥ-ḫrw) get a nudge rather than a full note if the
published parts already explained them — but this part is read on its own too, so the first occurrence in YOUR chunk
gets a short real explanation.
Do not write "about", "titleEn" or "part" (the lead does). Finish by running a short self-check script: signs of
your units flattened == established signs flattened over your range; every q covers its glyphs once; every morph
covers glyphs once. Report: units written, any doubtful readings, any lemma-key choices other chunks should match.
