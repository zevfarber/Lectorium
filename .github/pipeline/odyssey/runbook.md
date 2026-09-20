# Odyssey — what one run does

Everything you need is in this folder (`.github/pipeline/odyssey/`). Read `conventions.md` first, then
this file, then do the steps in order. The text is `source/odyssey-murray1919.json`, the cut is
`parts.json`, the rules are `conventions.md`, the model is `drafts/odyssey-001/` (the pilot the owner
approved on 2026-09-20), and the gates are `build_odyssey.py` and `validate_odyssey.py`. Never draft
from memory of the poem's wording in Greek or in English. The owner is not present; decisions go in
`QUESTIONS.md` with what you decided meanwhile. Python: standard library only.

## 0. Find the next part
`git pull`. In `parts.json` the first part whose `status` is `todo` and that has no live claim in
`claims/` is yours. **One part per run.** A claim older than 6 hours is stale — delete it and take the
part. Write `claims/odyssey-NNN.md` (one line: date, "drafting"), commit and push it to `main` before
drafting. If all 119 parts are `published`: append a DONE line to `LOG.md`, create the empty file
`.github/pipeline/odyssey/DONE`, commit and push those two changes, and stop. The marker is what tells
the shared routine to move on (see `.github/pipeline/README.md`, "The queue").

## 1. Make the packet
`python3 packet.py odyssey-NNN` (it refuses if the source does not match the part's `sha256`; if it
does, write what you found to `QUESTIONS.md`, release the claim and stop). It writes, under
`drafts/odyssey-NNN/`: `packet.md` (the lines with Murray's paragraph marks; every line of this part
that already stands in a published part, with the English it has there; the lines the scanner could
not fit cleanly), `novel-forms.json` and `known-forms.json`.

## 2. Draft — three roles, each a separate subagent with only the files named
Drafter and reviewer run on the strongest model available (the routine's own); the glosser runs on
Sonnet (`model: "sonnet"` in the Agent call).

**Drafter** (gets `conventions.md`, `packet.md`, and `drafts/odyssey-001/units.json` as the model of
shape and register). Writes `drafts/odyssey-NNN/units.json`:
`{title, titleEn, part, about, sentences:[{t, l, i, n, ln, v:true, p?, mark?}]}` — `title` a short Greek
title of our own for the stretch, `titleEn` = `<English name> — Odyssey <cite>`, `part` =
`<English name> (<cite>)`, with `<cite>` exactly as in `parts.json`. The English name is ours; take it
from the action, not from any translation's headings. `t` is cut from the packet's lines by a small
script, never retyped. The drafter never writes `tr` or `sc`; the build makes them. Rules that matter
most: the unit is the punctuated sense-unit and may begin or end mid-line; `l` keeps the line division
of `t`; `i` is real English; every unit has a note that leads with what the reader needs in order to
read these words; every stock epithet is translated every time, by the house rendering where the
table has one; a repeated line takes the English the packet shows for it; a word whose meaning is not
known is said to be unknown; no modern translation is opened or recalled, and an English phrase that
arrives fully formed is rebuilt from the grammar. A new formula or epithet that will plainly recur
(a whole-line speech introduction, a noun–epithet pair) gets a rendering chosen with the same care as
the table's, and the drafter lists every such choice in `drafts/odyssey-NNN/new-renderings.md`.
Line numbering: Murray prints 3.304/305 and 14.63/64 transposed and omits 10.456, 16.101 and 23.49;
the text follows him, and the unit that contains such a spot says so in its note.

**Reviewer** (gets the same files plus `units.json`; adversarial — its job is to find what is wrong).
First: every grammatical label in every note true of this form in this line; every claim about where a
word stands checked against the line; every cross-reference checked; no note contradicting its own
`l`/`i`. Then Greek → `l` word by word (case relations, tense, mood, particles), then `l` ↔ `i`
agreement in sense and in force, then remembered English in `i`, then quotation marks (“ on a speech's
first unit, ” on its last, `mark` on the first unit of each speech; a speech may run on from the
previous part or into the next — check the neighbouring part's last unit in the repository root).
It scans by hand every line the packet flags and, where the irregularity is real, adds one plain
sentence to that unit's note. It edits `units.json` in place by script, never touching `t`, and writes
`drafts/odyssey-NNN/review.md`: every change (line · field · severity · what was wrong · what was
done) and every finding it considered and refused, with the reason. Two passes.

**Glosser** (gets `novel-forms.json`, `known-forms.json`, `units.json`, and the entry-format section of
`conventions.md`). For every novel form, parsed in context from every place it occurs:
`"form": "lemma — meaning; parse"`, general to the form, never pinned to a line, no line numbers, no
"here", typographic ’ only, under 230 characters; Homeric forms name their Attic equivalent; article-
forms are pronouns; the possessive ὅς is kept apart from the relative; a genuine homograph gets both
readings joined by " · ". For every known form, check the existing entry covers its use in this part;
where it does not, put a broadened entry — the old entry whole, plus " · " and the new reading — under
the key `"__broaden__"`. Never rewrite an existing entry otherwise. Output `drafts/odyssey-NNN/gloss.json`.
The reviewer's second pass reads `gloss.json` too and checks every parse against the line.

## 3. Build and gate
```
python3 build_odyssey.py odyssey-NNN      # refuses, changing nothing, on any failure; makes tr and sc; merges the glossary; adds the manifest entry
python3 validate_odyssey.py odyssey-NNN   # must print PASS; read every WARN and fix what is a real problem
```
If the build writes and the validator then fails, fix the draft and build again; if you cannot, run
`git checkout -- .` from the repository root so that nothing half-built is left, write the problem to
`QUESTIONS.md`, release the claim and stop. A line that does not scan at all stops the build: report
it, do not publish around it.

## 4. Publish
Set the part's `status` to `published` in `parts.json`, regenerate `plan.md` with
`python3 plan.py`, append one line to `LOG.md` (date, part, cite, units, new glossary forms, review
findings by severity, scansion flags, anything notable), copy the rows of `new-renderings.md` into the
table in `conventions.md`, delete your claim file, and commit everything — `odyssey-NNN.json`,
`odyssey-glossary.json`, `stories.json`, `drafts/odyssey-NNN/`, the pipeline records — with a message
like `Odyssey: NNN — <English name> (<cite>)`. Push to `main`; if `main` has moved, `git pull --rebase`
and push again; never force. Do not touch `reader.html`, `index.html`, audio, or other works' files.

## If something is wrong that you cannot fix
Write it to `QUESTIONS.md` (what, where, what you decided or why you stopped), release the claim, and
stop. A run that publishes nothing and says why is a good run; a run that publishes a part it is
unsure of is not.
