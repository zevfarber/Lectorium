# Aeneid — what one run does

Everything is in this folder (`.github/pipeline/aeneid/`). Read `conventions.md`, then this file, then do the
steps in order. Text: `source/aeneid-greenough.json`. Cut: `parts.json`. Model of shape and register:
`drafts/aeneid-001/units.json` and the published `aeneid-001.json`. Gates: `build_aeneid.py`,
`validate_aeneid.py`. Never draft from memory of the poem's wording in Latin or in English. The owner is not
present; decisions go in `QUESTIONS.md` with what you decided meanwhile. Python: standard library; node is
used by the validator if present.

## 0. Find the next part
`git pull`. The first part in `parts.json` whose `status` is `todo` and that has no live claim in `claims/`
is yours. **One part per run.** A claim older than 6 hours is stale — delete it and take the part. Write
`claims/aeneid-NNN.md` (one line: date, "drafting"), commit and push it before drafting. If all 99 parts are
`published`: append a DONE line to `LOG.md`, create the empty file `DONE`, commit, push, stop.

## 1. Make the packet
`python3 packet.py aeneid-NNN` (refuses if the source does not match the part's `sha256`). It writes, under
`drafts/aeneid-NNN/`: `packet.md` (the lines with Greenough's paragraph marks, the Latin Library
disagreements in this stretch, the lines the scanner flags), `novel-forms.json`, `known-forms.json`.

## 2. Draft — three roles, each a separate subagent with only the files named
Drafter and reviewer on the strongest model available; the glosser may run on Sonnet.

**Drafter** (gets `conventions.md`, `packet.md`, `drafts/aeneid-001/units.json`). Writes
`drafts/aeneid-NNN/units.json`: `{title, titleEn, part, about, sentences:[{t, l, i, n, ln, v:true, p?}]}`
(`advisory` at top level if the content-advisory rules fire). `t` is cut with `aeneid_lib.cut(part, ends)`
from a list of (line, closing text) — never typed (see `drafts/aeneid-001/make_units.py`). The drafter never
writes `sc`. A set piece listed in `conventions.md` that has not yet been decided stops the run: write it to
`QUESTIONS.md`, release the claim, stop. Every new house rendering is listed in
`drafts/aeneid-NNN/new-renderings.md`.

**Reviewer** (same files plus `units.json`; adversarial). Every grammatical label in every note true of this
form in this line; Latin → `l` word by word; `l` ↔ `i` agreement; remembered English in `i` (rephrase any
distinctive echo of a known version); speech marks (“ on a speech's first unit, ” on its last; a speech may
run across parts). Scans by hand every line `packet.md` flags and every line with Greek `eu`, initial `Ae-`,
consonantal `i` after a prefix or a hiatus; where the scanner is wrong, adds the line to `scan-fixes.json`
with its reason. Edits `units.json` by script, never touching `t`; writes `drafts/aeneid-NNN/review.md`
(every change and every refused finding). Two passes.

**Glosser** (gets `novel-forms.json`, `known-forms.json`, `units.json`, the Glossary section of
`conventions.md`). For every novel form, parsed from every place it occurs: `"form": "lemma — meaning (parse)"`.
For known forms, check the entry covers this use; if not, put the broadened entry (old entry whole + " · " +
new reading) under `"__broaden__"`. Output `drafts/aeneid-NNN/gloss.json`.

## 3. Build and gate
```
python3 build_aeneid.py aeneid-NNN      # refuses, changing nothing, on any failure; makes sc; merges the glossary; adds the manifest entry
python3 validate_aeneid.py aeneid-NNN   # must print PASS (it runs reader.html's own WORD_RE in node for coverage)
```
If the build writes and the validator fails, fix the draft and build again; if you cannot, `git checkout -- .`
from the repository root, write the problem to `QUESTIONS.md`, release the claim, stop. A line no hexameter
fits stops the build: hand-scan it into `scan-fixes.json`, or report it.

## 4. Publish
Set the part's `status` to `published` in `parts.json`, run `python3 plan.py`, append one line to `LOG.md`
(date, part, cite, units, new glossary forms, review findings by severity, hand scansions, anything notable),
copy `new-renderings.md` rows into the table in `conventions.md`, delete your claim, and commit
`aeneid-NNN.json`, `aeneid-glossary.json`, `stories.json`, `drafts/aeneid-NNN/` and the pipeline records with
a message like `Aeneid: NNN — <English name> (<cite>)`. Push to `main`; if `main` moved, `git pull --rebase`
and push again (on a `stories.json` conflict, re-apply your entry on top of the incoming file); never force.
Do not touch `reader.html`, `index.html`, audio, or other works' files.

## Missing punctuation in the source
Rule 5 of `.github/pipeline/README.md` applies: add the mark to `source/aeneid-greenough.json`, re-pin the
affected parts' `sha256`, fix the draft's `t`, rebuild, log it.

## If something is wrong that you cannot fix
Write it to `QUESTIONS.md`, release the claim, stop. A run that publishes nothing and says why is a good run.
