# Review — cid-tiradas-05-09 (first pass, no glossary)

Reviewed against `conventions.md`, `packet.md`, and the published pilot `cid-tiradas-01-04.json`.

## Continuity check (done first, and re-verified after edits)
Concatenated every unit's `t` (split on "\n", 109 lines) against the packet's full verse
sequence for lines 65–173 (including 69b, and the 98→100 jump with no 99), character for
character: **0 mismatches, before and after my edits.** Every unit's `l` also has exactly the
same number of "\n"-separated lines as its `t` (checked by count, all 47 units). No unit exceeds
4 lines (soft target respected throughout).

Assonance claims were re-derived from the actual line-endings in `t`, not taken on trust:
Tirada 5 (65–77) = í-o ✓, Tirada 6 (78–87) = á-a ✓, Tirada 7 (88–95) = á-o ✓, Tirada 8 (96–98) =
á-a ✓, Tirada 9 (100–173, 74 lines) = á-o ✓ with v. 105 (apartaron, oxytone, stressed on the
final syllable) correctly flagged as the one exception — confirmed by scanning all 74
line-endings. All five tiradas' first units open "Tirada N (assonance X-Y) — gloss" as required.
The quirks of this part (69b following the pilot's 14b/16b precedent; the missing 99 with
tirada 8 ending at 98 and tirada 9 beginning at 100; v. 135's short line hedged as "may be
defective" rather than asserted) are all handled correctly and without false confidence.

## Changes made

1. **Unit 6 (v. 75–77) · `n` · error.** The note glossed the reduced future auxiliary in
   "querer m'a" as "(he)" — but the subject is "el rey" (third person: ha), not the speaker
   (first person: he). "(he)" is the wrong person for this form. Also, the note called it
   "exactly like conbidar le ien in the opening tiradas," but conbidar le ien is the *split
   conditional* (per conventions.md and the pilot's own note), while querer m'a is the *split
   future* — a different tense sharing only the split-verb shape. Fixed both: now reads
   "...the reduced auxiliary a (from ha, 'has', 3rd person — the subject here is el rey), the
   same split-verb trick as the split conditional conbidar le ien in the opening tiradas, but
   with the future auxiliary rather than the conditional one."

2. **Unit 10 (v. 85–87) · `i` · weak.** "bastir quiero dos arcas" (I want to build two chests)
   was rendered "I mean to have two chests built" — a causative construction that adds a nuance
   (delegated labor) not in the Spanish, which is plain active voice. Changed to "I mean to
   build two chests."

3. **Unit 19 (v. 106–108) · `n` · weak/error.** The note called "a moros nin a cristianos"
   an instance of "the usual double negative (non … nin)." "non … nin" here is ordinary
   correlative negation ("not … nor"), present in Spanish then and now and unremarkable to an
   English reader (English does the same); it is not the kind of redundant negative-concord
   oddity ("ninguno non," "nol … nada") the convention's "double negative" flag is meant to
   mark, and mislabeling it dilutes that flag elsewhere. Reworded to clarify it is the ordinary
   correlative, not the redundant double negative.

4. **Unit 20 (v. 109–112) · `l` · weak.** "quanto que f[o] algo" was glossed in `l` as "as-much-
   as was of-worth," while every other occurrence of "algo" in this draft (vv. 123, 157) is
   glossed literally as "something" in `l`, with the "value/money" sense left to `i` or the note.
   Changed `l` to "as-much-as was something" for consistency; `i`'s "whatever had value" already
   carries the intended sense.

5. **Unit 27 (v. 127–128) · `n` · error.** "prendámoslas, metamos" were labeled "deliberative
   subjunctives." Deliberative subjunctive is the Latin-grammar term for subjunctive used in a
   self-addressed question ("what should I do?"); these are plain first-person-plural
   commands/suggestions ("let's take them," "let's put them"), i.e. hortative (exhortative)
   subjunctives. Fixed the label.

6. **Unit 32 (v. 137–138) · `n` · weak/error.** The note read "the speaker turns back to Martín
   Antolínez without being named," which (on its natural reading) suggests Martín Antolínez is
   being addressed. Grammatically he must be the speaker: "que nos dedes los marcos" uses
   "dedes" (2nd-person-plural, addressed to Raquel e Vidas) asking them to hand the marks "to
   us" — so this has to be Martín Antolínez pressing the lenders, not the reverse. Reworded for
   clarity: "it is Martín Antolínez speaking again, without being named — que nos dedes shows he
   is pressing Raquel e Vidas, not the reverse."

(One edit attempt briefly broke the JSON — a nested unescaped `"let's…"` in fix #5 — caught
immediately by re-validating the file and corrected to a single-quoted form before any other
work continued. The file was re-validated as parseable JSON and the full continuity/line-count
check was re-run clean after all six fixes.)

## Findings considered and NOT acted on

- **Unit 1 (v. 65–66) · `l`: "to his men" for "alos sos."** "sos" alone (lit. "his [own]") is
  stretched to "his men" in `l` to make sense in English; nothing forces this addition, but
  without it the gloss is unreadable, and the note immediately glosses `s[o]s = sos = sus
  'his (men)'` with the same parenthetical. Left as is — a necessary minimal addition, not an
  invented clause.
- **Double-negative pattern not flagged for "no trayo [nada]" (unit 7, v. 82).** This is a
  genuine double negative (no + nada) and the convention asks for the pattern to be flagged
  "first few times, then a nudge." The pilot already introduced and explicitly named this
  pattern (v. 21, v. 58); by this second part, the `l` gloss alone ("not carry [nothing]")
  already preserves it transparently. Left unflagged in the note as within the "nudge" policy
  rather than a gap.
- **Tense-mixing not flagged at unit 15 (v. 96–98): "passó" (preterite) beside "entrava,
  demandava" (imperfect).** A real instance of the pattern, but the draft does flag it
  explicitly twice elsewhere in this part (units 17/"the epic slides between tenses," 38/"Tense-
  mixing again," 47 implicitly) — consistent with "first few times, then a nudge" rather than
  flagging every instance. Left as is.
- **Unit 20 (v. 109–112) · `n`: "f[o] = fue, the older preterite" applied uniformly to three
  different syntactic roles** (perfect auxiliary with a motion verb in "f[o] entrado," plain
  copula in "f[o] algo," passive auxiliary in "f[o] acusado"). The claim is not false — all
  three really are the preterite of ser — just less granular than it could be. Not a factual
  error; left as is.
- **Unit 23 (v. 117–118) · `n`: "the sum is left courteously unnamed for another seventeen
  lines, until the lenders themselves ask."** The 17-line count is correct (v. 118 to v. 135,
  where the figure is actually named), but it is Martín Antolínez, not the lenders, who states
  the figure; the lenders only ask for it at v. 129–130 (11 lines on). Read generously ("until…
  ask [and are told]") the sentence is defensible as a compressed description of the whole
  exchange. Left as is, flagged here for visibility rather than rewritten.
- **Unit 46 (v. 170–171) · `n`/`l`/`i`: "veriedes = veríais, 'you would have seen'."** "veríais"
  is a simple conditional ("you would see"); "you would have seen" is a conditional perfect.
  The mismatch is between the note's stated Spanish equivalent and its English gloss, but "you
  would have seen" is a standard, idiomatic English rendering of this kind of epic narrator
  aside (a counterfactual address to an absent audience) and matches ordinary translation
  practice; it is not a mistranslation of sense. Left as is.
- **Note density: every one of the 47 units carries an `n`, unlike the pilot, which leaves a
  few transitional lines unannotated (e.g. its ln=35 unit).** Not acted on — the content of each
  note here is substantive and non-redundant, not padding; there was no unit where the note
  seemed forced.

## Not checked (explicitly out of scope per instructions)
Glossary coverage against `cid-glossary.json` — that file does not exist yet and this is a
first pass; left entirely alone.

## Second pass (glossary)

Checked `gloss.json`'s 300 entries plus its 7 `__broaden__` entries against `packet.md`,
`units.json`, and (for the broadened tokens only) the current `cid-glossary.json`; cross-checked
every grammatical claim in `units.json`'s 47 `n` notes against the matching `gloss.json` entry and
vice versa; spot-checked the glossary-key stripping rule; did a final sweep of `units.json` itself.
Did not reopen any of the first pass's six "considered and NOT acted on" items — no new objection
to any of them.

### Changes made

1. **287 entries (format, bulk) · severity: cosmetic, but systematic.** Essentially every entry
   in `gloss.json` was written as "TOKEN — LEMMA — MEANING (grammar)", repeating the raw key as a
   redundant first segment before the lemma (e.g. `"oro": "oro — oro — gold"`, `"abástales":
   "abástales — abastar + les — he supplies them (…)"`). The real `cid-glossary.json` never does
   this: every entry (checked directly) is strictly "LEMMA — MEANING (grammar)", with the token
   repeated as the lemma only when the token already *is* the dictionary form, and never as a
   separate leading segment. Stripped the redundant leading token from all entries where it
   matched the key exactly, via a script (then hand-verified the result), leaving e.g. `"oro":
   "oro — gold"` and `"abástales": "abastar + les — he supplies them (…)"`. One entry (`vino`) was
   wrongly caught by this same script, see item 2.
2. **`vino` · format · error (self-inflicted, caught and reverted).** The bulk script above
   stripped `vino`'s leading "vino —" on the assumption it was a redundant copy of the key, but
   for this entry the token genuinely *is* the lemma for sense 1 (the noun "wine"), with a second,
   different-lemma sense ("also venir — he came …") following — exactly the dual-sense pattern the
   real glossary's `"ya"` entry models. Restored the lemma: `"vino — wine (noun); also venir — he
   came (…)"`.
3. **`burgalés` · format · error.** Ended with a dangling, uninformative `"; = burgalés"` (the
   word's modern spelling is identical to itself, so this added no information and didn't match
   the house bracket-clause style). Dropped it.
4. **`alos` · format · error.** Was `"alos — a + los, to the (contraction; = a los)"` — the
   decomposed lemma `a + los` was glued into the meaning with a comma instead of being the entry's
   lemma field, and `"= a los"` merely repeated the decomposition a second time. Restructured to
   `"a + los — to the (contraction)"`.
5. **`fo` · `n`/meaning · error.** Claimed "fo entrado, fo algo, fo acusado are all
   periphrastic/passive ser + past part. constructions" — false for `f[o] algo` (v. 111, "quanto
   que f[o] algo" = "fue algo," a plain copula with the pronoun **algo** as predicate, not a past
   participle). Reworded to separate the two genuine ser+participle periphrases (`fo entrado`, `fo
   acusado`) from the plain-copula case (`fo algo`).
6. **`tred` · grammar tag · missing/inconsistent.** Every other imperative entry in this file
   (`dat`, `prended`, `meted`, `prendet`, `ponedlas`, …) states person/number, e.g. "(2nd pl.
   imperative)"; `tred` alone omitted it. Added "(2nd pl. imperative, old form, …)" — confirmed 2nd
   plural from context: "Amos tred al Campeador," addressed to both Raquel and Vidas.
7. **`avédesme` · meaning · error (overreach).** Gave the headline meaning as "you have forgotten
   me" — but `avédesme` by itself is only *avedes* (aux. "you have") + enclitic *me*; the sense
   "forgotten" belongs to the next, separately-keyed word, `olbidado`. The real glossary's
   `estávalos` entry models exactly this situation with an ellipsis: "he-was + them: 'was … them'".
   Reworded to `"you-have … me (…; avédesme olbidado = 'you have forgotten me', a host's
   mock-reproach)"`, moving the complete-clause gloss into the parenthetical where it belongs.
8. **`auien` · modern-Spanish form · incomplete.** Gave only `"= avían"`, itself an archaic/
   orthographic cousin rather than true modern Spanish. The sibling spelling `avien` is already in
   the shared `cid-glossary.json` as `"aver — they had (imperfect 3rd pl.; = avían/habían)"`.
   Brought `auien` into line: `"= avían/habían"`.
9. **`__broaden__.i` · format · error.** Read `"also i — ibi — there, therein (adverb, Latin ibi,
   …)"` — a redundant middle segment that both repeated the key as a second "lemma" field *and*
   duplicated the Latin etymon already given in the parenthetical. Dropped the middle segment:
   `"also i — there, therein (adverb, Latin ibi, …)"`.

### `__broaden__` verification (all 7)

Checked each against the *current* `cid-glossary.json` entry (read directly, not assumed) and
against its actual occurrence(s) in `packet.md`:

- **a** (prep. "to, at" → + aver "he/she has," h-less *ha*, 3rd sg., as in `el rey me a ayrado`,
  v. 90/114) — genuinely new sense, correct grammar, correctly formatted once fixed.
- **e** ("and" → + aver "I have," apocopated *he*, 1st sg., `Espeso e el oro`, v. 81) — genuinely
  new, correct.
- **conpra** (noun "buying" → + comprar "he/she buys," 3rd sg., `non lo conpra`, v. 67) — genuinely
  new, correct.
- **grado** ("thanks" → + "will, good will," `de grado`, vv. 84/136/149) — a different *sense* of
  the same root, not covered by the existing "thanks" entry; correct, kept.
- **i** ("and" → + "there, therein," Lat. *ibi*, `meted i las fedes`, v. 120) — genuinely new;
  format fixed per item 9 above.
- **qué** (exclamative "what a …!" → + interrogative "what? which?," `de qué será pagado`, v. 129)
  — genuinely new, correct.
- **cabo** (prep. "beside" → + noun "end," `fasta cabo del año`, v. 162) — genuinely new, correct.

All 7 match "<old entry in full> · <new reading>" (verified the "<old entry in full>" half against
`cid-glossary.json` character-for-character in each case), and each new reading's grammar is
correct for its actual occurrence in this part.

### Glossary-key spot-check

Stripped brackets/split apostrophes by hand against `packet.md` and compared to `gloss.json`'s
keys: `f[o]stes` → `fostes` ✓, `m'a` → `m`, `a` ✓ (and the `a` broadened sense is exactly the "ha"
reading needed for this `m'a`), `convus[c]o` → `convusco` ✓, `am[o]s` → `amos` ✓. All four keys
match the stripping rule exactly. **Passed.**

### Cross-check: `units.json` `n` notes vs. `gloss.json`

Walked all 47 units' notes against the `gloss.json` entries for the same words (lemma, tense/
person/number/mood, meaning) in both directions. Found and fixed one discrepancy worth noting:
unit 20's note ("f[o] = fue, the older preterite, restored three times in four lines") makes no
claim about participle-vs-copula, so the error in `gloss.json`'s `fo` entry (item 5 above) was
internal to that file, not a cross-file disagreement — fixed there. No other disagreement found;
in particular, double-checked (among others) `so`/`so ayrado`, `o`/`ó`, `querer m'a` + the
broadened `a`, `prendámoslas`/`metamos` (hortative, matching the first pass's correction),
`aguisado` (treated as "the same word as guisado" in both files, consistently), and `veriedes` —
all consistent.

### Findings considered and NOT acted on

- **`grádanse` · initially suspected person/number error.** On a first read appeared to say
  "(reflexive present 3rd sg.)" for a plural subject (Raquel e Vidas); re-verified the live JSON
  byte-for-byte and it already correctly reads "3rd pl." No error; not changed.
- **Lemma style for lexicalized past participles (e.g. `menguados` lemma'd as the adjective
  `menguado`, vs. `ventado` lemma'd as the infinitive `ventar`).** Inconsistent within `gloss.json`,
  but not wrong: the real `cid-glossary.json` itself uses both patterns side by side (`mudado`,
  `abierto` lemma'd as the participle; others as the infinitive). Within house tolerance — left
  alone.
- **`aguisado` lemma'd as `guisar` rather than a separate `aguisar`.** `units.json`'s own note
  (already reviewed and accepted in the first pass) explicitly treats `aguisado` as "the same word
  as guisado," so the gloss entry is consistent with an editorial judgment already on record, not
  an independent error. Left alone.
- **The `__broaden__` entries' "also LEMMA — meaning" phrasing**, and the main file's analogous
  dual-sense entries (`so`, `o`, `vino`, `pagado`) **use the word "also" inside the `<new reading>`
  half**, where the instructed template is literally "<old entry in full> · <new reading>". Judged
  this as the content of the `<new reading>` itself (not a structural violation) and applied
  uniformly across all 7 broadened tokens and the dual-sense entries alike — left alone rather than
  stripped, since stripping "also" would make the dual-sense entries read as a single run-on
  lemma + meaning instead of two senses.
- **`seiense` and other seer/estar + enclitic + gerund compounds** state the compound's meaning in
  English ("they were sitting …") without a separate explicit "(3rd pl.)" tag. This matches the
  real glossary's own `estávalos` entry, which likewise carries no explicit person/number tag on an
  analogous compound. Left alone.
- Re-read all six first-pass "considered and NOT acted on" items (unit 1's `l`, the double-negative
  nudge policy, the tense-mixing nudge policy, `f[o]`'s uniform preterite label *in units.json*,
  the "seventeen lines" compression, and `veriedes`'s conditional-perfect rendering). No new
  objection to any of them; none reopened.

### `units.json` final sweep

No additional changes made. Re-verified: the 0-mismatch continuity check still holds (no edits
touched any `t`/`l` text in this pass), and every grammatical claim surviving in `n` notes was
re-checked against `gloss.json` as above with no disagreement left outstanding.

### Summary

`gloss.json`: 293 of the 300 regular entries changed from their pre-review state net (287
mechanical format fixes from the bulk pass + `burgalés` + `alos`, both format, + 4 substantive
content/grammar fixes: `fo`, `tred`, `avédesme`, `auien`); one further regular entry, `vino`, was
touched by the mechanical pass and then restored to its original (correct) form, so it nets to no
change and is not counted among the 293. Separately, 1 of the 7 `__broaden__` entries (`i`) also
had a format fix. `units.json`: 0 additional notes changed. Glossary-key spot-check: passed.
