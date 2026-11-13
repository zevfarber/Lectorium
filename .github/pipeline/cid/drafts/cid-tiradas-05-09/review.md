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
