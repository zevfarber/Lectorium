# Part 9 review — pass 2 (adversarial, independent of pass 1)

Reviewed `part9-draft.json` (current, post-pass-1-fixes, 22 units) against `conventions.md`,
`slovo-proem.json`, `slovo-part1.json`, `slovo-part8.json` (consulted to verify one specific
cross-reference claim), `parts.json`, `source-1800.txt`, `runbook.md`, `LOG.md`, `QUESTIONS.md`,
and `part9-review1.md` / `part9-draftnotes.md` for context. All checks below were re-derived
independently (programmatic diff/hash for items 1, 4, 5; close reading for the rest) rather than
taken on pass 1's word.

## Per-item results

**1. `t`-concatenation vs. source, char-for-char — PASS.** Concatenated all 22 `t` fields with
single spaces, whitespace-normalised, and diffed against (a) the source block given in the task
prompt and (b) a fresh extraction from `source-1800.txt` using `parts.json`'s part-9 `opens`/`ends`
strings. Both are byte-identical to the draft's concatenation: 301 words, 1925 chars, sha256
`924b413c921b66ca19678fa3e278eabb63638387ed5435a6083c203a3d43e3f6`, matching `parts.json`'s
recorded value exactly. No drift from the unit 20/22/24→merge operations.

**2. Unit 14 `l`/`i` polarity — PASS.** Both now read "**not otherwise**": `l` = "Was it not
otherwise, [Igor] said, [with] the river Stugna..."; `i` = "'Was it not otherwise,' he said, 'with
the river Stugna...'". The note also now says "'was it not otherwise,' i.e. 'unlike you'" —
`l`, `i`, and `n` are consistent with each other. Pass-1's contradiction is resolved.

**3. Merged Gzak/Konchak units (20/22/24 pattern → 3 units) — PASS.** Confirmed word counts of the
three merged units are 13, 15, 26 — exactly matching pass 1's predicted post-merge counts, all
inside the 12–30 target. Each reads as one fused sentence, tag-plus-quote, in `t`/`tr`/`l`/`i`
alike (e.g. `l` unit 20: "Gzak speaks to Konchak: since the falcon flies to [its] nest, let us
[two] shoot the falcon-chick with our gilded arrows."). This matches the fused-tag pattern of this
same part's units 11–12 (Донецъ/Игорь) and of part 1's "И рече ему Буй Туръ Всеволодъ: одинъ
братъ..." — no isolated speech-tag units remain anywhere in the file.

**4. `на ветрѣхъ` → `vetrěxŭ` — PASS.** Unit 13 `tr` now reads "...Črĭnjadĭmi na vetrěxŭ." — plain
`e`, not `ě`. Correct per convention (only ѣ maps to ě; the source word is «ветрѣхъ» with plain е).

**5. Stray Cyrillic in `tr` fields — PASS, none found.** Regex-scanned every `tr` field in the file
(Unicode Cyrillic block U+0400–U+04FF) programmatically; zero matches. The two Cyrillic-`а` leaks
pass 1 found in units 21/23 (old numbering) are gone in the merged units' `tr` (confirmed both
now start with Latin `a`: "aže sokolŭ...").

**6. Fresh whole-part adversarial pass — PASS, no blocking defects found.**
- *t-vs-source*: covered by item 1, exact.
- *False grammar claims*: checked every aorist/imperfect/dual claim against the actual form.
  претръгоста (3rd-dual aorist, -оста), рострѣляевѣ/опутаевѣ (1st-dual present/future, -евѣ, same
  pattern as part 1's «есвѣ»), нама/наю (dat./acc. dual of "we"), Погасоша (aorist 3pl, -оша),
  свисну/кликну/стукну/прысну (punctual -ну- aorists, zero ending, all internally consistent with
  each other and with unit 1's «Прысну»), стрежаше (imperfect, -аше) all check out. One place
  worth a light touch, not a blocking error: unit 6's note calls «Князю Игорю не быть» "the very
  same pattern as" the proem's «Не лѣполи ны бяшетъ ... начяти» — both are dative-subject
  constructions built on быти-family forms expressing impersonal necessity, which is true in
  spirit, but the proem line has a separate finite copula (бяшетъ) plus a separate infinitive
  complement (начяти), while unit 6 has the dative subject governing the bare infinitive «быть»
  directly, no separate copula. "The same broad construction" would be more exact than "the very
  same pattern." Non-blocking.
- *Overclaimed history / dark places*: Rostislav Vsevolodovich's 1093 drowning on the Stugna
  (Primary Chronicle), Gzak and Konchak as real 1185 khans, Vladimir Igorevich's later marriage to
  a daughter of Konchak's, and Svyatoslav's 1183 Dnepr campaign against Kobyak (cross-checked
  against `slovo-part8.json`, which independently corroborates the Kobyak campaign and confirms
  unit 11's claim that this part's Donets-speaks-first exchange inverts part 8's
  Yaroslavna-addresses-first pattern — both true) are all stated with correct facts and honest
  hedges. Every genuine dark place («Комонь въ полуночи», «не быть», «стругы ростре на кусту»,
  the «стугою»/Стугна pun, «почнутъ наю птици бити») is flagged as unresolved, none resolved with
  invented confidence.
- *Childish or content-adding `i`*: none found. Register stays "lightly elevated," matching the
  models. A few `i` fields add a light connective word not literally in the source (unit 9 "all in
  one flight," unit 10 "alongside," unit 21 "instead," unit 17 "no,") — these are idiomatic glue,
  not new facts or claims, and are within the same latitude the model files themselves take
  (e.g. part 1 unit 8's `i` adds "and" and restructures beyond `l`). Not a defect.
- *Correct `p` placement*: PASS, re-derived independently. `source-1800.txt` has a blank line
  immediately before "Прысну" and immediately after "Половецкомъ." and zero blank lines inside
  that span — part 9 is one source paragraph, so `p:true` on unit 1 only (confirmed the only such
  unit in the file) is correct.
- *Echoes of famous modern translations*: judged unit 3's "Игорь спитъ, Игорь бдитъ, Игорь
  мыслію..." triad, units 11–12's Donets/Igor exchange, and units 20–22's Gzak/Konchak riddle
  against my own recollection of well-known English Slovo renderings (Nabokov 1960 principally,
  the source most likely to be echoed given its currency). I do not have confident verbatim
  recall of any of these three passages in a named translation precise enough to call a specific
  phrase in this draft a reproduction; the current wording ("Igor sleeps, Igor keeps watch, Igor
  measures the steppe in thought..."; "Great is your glory, great Konchak's displeasure..."; "let
  the two of us shoot down the falcon-chick with our gilded arrows") reads as independently
  arrived-at rather than lifted. This is the best check obtainable without web access and should
  not be taken as a substitute for a source-checked comparison if one becomes available.

## Process note (not a text defect — nothing in `part9-draft.json` needs editing for this)

`runbook.md` step 3 requires an echo-check spot-check to be **recorded in the `LOG.md` line**
before publish, and every already-published part's `LOG.md` entry carries exactly this ("Echo-
checked X, Y, Z — clean"). `LOG.md` currently has no part 9 entry (part 9 is still unpublished),
so this required record is still outstanding. Pass 1 raised this as its blocking defect #1; this
pass performed the substantive check (see above, item 6) and found nothing to fix in the draft
itself, but whoever runs the publish step (step 4–5 of the runbook) still needs to write the
`LOG.md` line documenting it — this is a housekeeping/gate step, not a translation defect.

## Non-blocking watch items (carried over / newly noted, at drafter's discretion)

- Unit 5's note still says Ovlur is "spelled Овлуръ here, Влуръ two sentences on." Re-counted
  independently in the current 22-unit numbering: «Влуръ» is in unit 10, and «Овлуръ» is in unit
  5 — units 6, 7, 8, 9 all fall between them, so it's the fifth sentence on, not the second. Same
  item pass 1 flagged as non-blocking; still unfixed, still harmless.
- Unit 6's note phrase "the very same pattern as" (see grammar item above) could be tightened to
  "the same dative + быти-family impersonal construction as," to avoid overstating the syntactic
  identity with the proem's opening line.

## Verdict

**CLEAN — ready to publish**, once the `LOG.md` echo-check line is written at the publish step per
`runbook.md` (a housekeeping step for whoever runs it next, not a change to the draft file). All
six review-brief checks pass; no blocking defects found in the translation itself.
