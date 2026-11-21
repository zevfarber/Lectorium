# Marcus Aurelius, *Meditations* — what one run does

Everything you need is in this folder (`.github/pipeline/meditations/`). Read `conventions.md` first, then this
file, then do the steps in order. The text is `source/meditations-leopold1908.json`, the cut is `parts.json`, the
rules are `conventions.md`, the model of shape and register is the Aesop fables (`aesop-001.json` … in the
repository root — prose units with `t`, `l`, `i`, `n`), and the gates are `build_meditations.py` and
`validate_meditations.py`. Never draft from memory of any translation. The owner is not present; decisions go in
`QUESTIONS.md` with what you decided meanwhile. Python: standard library only.

## 0. Find the next part
`git pull`. In `parts.json` the first part whose `status` is `todo` and that has no live claim in `claims/` is
yours. **One part per run.** A claim older than 6 hours is stale — delete it and take the part. Write
`claims/meditations-NNN.md` (one line: date, "drafting"), commit and push it to `main` before drafting. If no part
is `todo` and none is `blocked`: append a DONE line to `LOG.md`, create the empty file
`.github/pipeline/meditations/DONE`, commit and push those two changes, and stop. Never write DONE while a part is
blocked (see `.github/pipeline/README.md`, "The queue").

## 1. Make the packet
`python3 packet.py meditations-NNN` (it refuses if the source does not match the part's `sha256`; if it does,
write what you found to `QUESTIONS.md`, release the claim and stop). It writes, under `drafts/meditations-NNN/`:
`packet.md` (the text chapter by chapter, block by block, with verse quotations and subscriptions marked, and
every sentence that already stands in a published part, with its English), `novel-forms.json`,
`known-forms.json`, and `aesop-forms.json` (forms new here that the Aesop glossary has — a starting point for the
glosser, checked against Marcus's use).

## 2. Draft — three roles, each a separate subagent with only the files named
Drafter and reviewer run on the strongest model available (the routine's own); the glosser runs on Sonnet
(`model: "sonnet"` in the Agent call).

**Drafter** (gets `conventions.md`, `packet.md`, and one published Aesop part, e.g. `aesop-001.json`, as the model
of shape). Writes `drafts/meditations-NNN/units.json`:
`{title, titleEn, part, about, sentences:[{t, l, i, n}]}` — `title` a short Greek title of our own for the
stretch, `titleEn` = `<English name> — <cite>`, `part` = `<English name> (<cite>)`, with `<cite>` exactly as in
`parts.json`; `about` two or three plain sentences on what this stretch is about, for the library. `t` is cut from
the packet's blocks by a small script, never retyped; units tile each block in order and never cross a block.
The drafter never writes `tr`, `ln`, `p` or `v`; the build sets them. Rules that matter most: the unit is the
punctuated sense-unit (≤70 Greek words); `l` keeps a verse quotation's line breaks and has none in prose; `i` is
real English; every unit has a note that leads with what the reader needs in order to read these words; the house
renderings are used as written; a word or reading that is uncertain is said to be uncertain; no translation is
opened or recalled, and an English sentence that arrives fully formed is rebuilt from the grammar. A new
recurring term gets a rendering chosen with the same care as the table's, listed in
`drafts/meditations-NNN/new-renderings.md`.

**Reviewer** (gets the same files plus `units.json`; adversarial — its job is to find what is wrong). First:
every grammatical label in every note true of this form here; every cross-reference checked; no note
contradicting its own `l`/`i`; every editorial sign (⟨ ⟩, [ ], †) explained where it stands. Then Greek → `l` word
by word (case relations, tense, mood, particles, the article), then `l` ↔ `i` agreement in sense and force, then
remembered English in `i` — Marcus is heavily anthologised, so any sentence of `i` that sounds like a famous
quotation is rephrased from the grammar. It edits `units.json` in place by script, never touching `t`, and writes
`drafts/meditations-NNN/review.md`: every change (chapter · field · severity · what was wrong · what was done) and
every finding it considered and refused, with the reason. Two passes.

**Glosser** (gets `novel-forms.json`, `known-forms.json`, `aesop-forms.json`, `units.json`, and the "Glossary
entries" section of `conventions.md`). For every novel form, parsed in context from every place it occurs:
`"form": "lemma — meaning; parse"`, general to the form, never pinned to a passage, typographic ’ only, under 230
characters; a genuine homograph gets both readings joined by " · ". For every known form (seeded or earlier),
check the entry covers its use here; where it does not, put a broadened entry — the old entry whole, plus " · " and
the new reading — under the key `"__broaden__"`. Never rewrite an existing entry otherwise. Output
`drafts/meditations-NNN/gloss.json`. The reviewer's second pass reads `gloss.json` too and checks every parse.

## 3. Build and gate
```
python3 build_meditations.py meditations-NNN      # refuses, changing nothing, on any failure; makes tr, ln, p, v; merges the glossary; adds the manifest entry
python3 validate_meditations.py meditations-NNN   # must print PASS; read every WARN and fix what is a real problem
```
If the build writes and the validator then fails, fix the draft and build again; if you cannot, run
`git checkout -- .` from the repository root (and delete the half-built `meditations-NNN.json` if it is new) so
that nothing half-built is left, write the problem to `QUESTIONS.md`, release the claim and stop.

## 4. Publish
Set the part's `status` to `published` in `parts.json`, regenerate `plan.md` with `python3 plan.py`, append one
line to `LOG.md` (date, part, cite, units, new glossary forms, broadened entries, review findings by severity,
anything notable), copy the rows of `new-renderings.md` into the table in `conventions.md`, delete your claim
file, and commit everything — `meditations-NNN.json`, `meditations-glossary.json`, `stories.json`,
`drafts/meditations-NNN/`, the pipeline records — with a message like
`Meditations: NNN — <English name> (<cite>)`. Push to `main`; if `main` has moved, `git pull --rebase` and push
again; never force. Do not touch `reader.html`, `index.html`, audio, or other works' files (the romanizer is
imported from `../odyssey/`, never edited from here).

## Missing punctuation in the source
If a build refuses because the pinned source lacks a mark the edition prints, apply rule 5 of
`.github/pipeline/README.md`: add the mark to `source/meditations-leopold1908.json`, re-pin the affected parts'
`sha256` in `parts.json` (`med_lib.sha` of the part's chapters), fix the draft's `t`, rebuild, and log it. Do not
stop and do not ask.

## If something is wrong that you cannot fix
Write it to `QUESTIONS.md` (what, where, what you decided or why you stopped), set the part's status to `blocked`,
release the claim, and stop (README rule 7: the next run takes the next part). A run that publishes nothing and
says why is a good run; a run that publishes a part it is unsure of is not.
