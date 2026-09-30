# Beowulf — what one run does

Everything you need is in this folder (`.github/pipeline/beowulf/`). Read `conventions.md` first, then this file, then
do the steps in order. The text is `source/beowulf-klaeber1922.json`, the cut is `parts.json` (one part per fitt), the
rules are `conventions.md`, the models are the three published parts in the repository root (`beowulf-prologue.json`,
`beowulf-fitt-01.json`, `beowulf-fitt-02.json`), and the gates are `build_beowulf.py` and `validate_beowulf.py`. Never
draft from memory of the poem's wording in Old English or in English. The owner is not present; decisions go in
`QUESTIONS.md` with what you decided meanwhile. Python: standard library only.

## 0. Find the next part
`git pull`. In `parts.json` the first part whose `status` is `todo` and that has no live claim in `claims/` is yours.
**One part per run.** A claim older than 6 hours is stale — delete it and take the part. Write
`claims/<id>.md` (one line: date, "drafting"), commit and push it to `main` before drafting. If all 44 parts are
`published`: append a DONE line to `LOG.md`, create the empty file `.github/pipeline/beowulf/DONE`, commit and push those
two changes, and stop. The marker is what tells the shared routine to move on (see `.github/pipeline/README.md`,
"The queue").

## 1. Make the packet
`python3 packet.py <id>` (it refuses if the source does not match the part's `sha256`; if it does, write what you found
to `QUESTIONS.md`, release the claim and stop). It writes, under `drafts/<id>/`: `packet.md` (the lines with Klaeber's
numbers, his italic letters, any low-confidence reading, the apparatus for the part's pages, any boundary note),
`novel-forms.json` and `known-forms.json`.

## 2. Draft — three roles, each a separate subagent with only the files named
Drafter and reviewer run on the strongest model available (the routine's own); the glosser runs on Sonnet
(`model: "sonnet"` in the Agent call).

**Drafter** (gets `conventions.md`, `packet.md`, and the three published parts as the model of shape and register).
Writes `drafts/<id>/units.json`: `{sentences:[{t, l, i, n, ln, v:true, p?}]}`. Nothing else — title, part label,
source statement and `about` are made by the build. `t` is cut from the packet's lines by a small script, never
retyped. Rules that matter most: the unit is Klaeber's punctuated sense-unit and may begin or end mid-line; `i` is real
English; every unit has a note that leads with what the reader needs in order to read these words; kennings are
hyphenated in `l` and unpacked in `i`; a recurring formula takes the English the published parts gave it; a word whose
meaning is guessed is said to be guessed; emendations and lost letters are explained where they matter; no modern
translation is opened or recalled. **Fitts XXIX and XXX:** the first unit's note of each says in one sentence that
Klaeber prints the section numeral [XXVIIII–XXX] at line 2039 and marks no break at 2093, and that the division at
2093 is ours. **The first dot under a vowel** that a part meets gets one sentence of explanation (Klaeber's sign that
the vowel does not count in the metre).

**Reviewer** (gets the same files plus `units.json`; adversarial — its job is to find what is wrong). First: every
grammatical label in every note true of this form in this line; every claim about where a word stands checked against
the line; no note contradicting its own `l`/`i`. Then Old English → `l` word by word (case relations, tense, mood,
negation, the demonstrative), then `l` ↔ `i` agreement in sense and force, then remembered English in `i` (a phrase
that sounds like a famous translation is rebuilt from the grammar), then consistency with the published parts'
renderings. It edits `units.json` in place by script, never touching `t`, and writes `drafts/<id>/review.md`: every
change (line · field · severity · what was wrong · what was done) and every finding it considered and refused, with the
reason. Two passes.

**Glosser** (gets `novel-forms.json`, `known-forms.json`, `units.json`, and the glossary section of
`conventions.md`). For every novel form, parsed in context from every place it occurs:
`"form": "lemma — meaning (parse)"`, general to the form, never pinned to a line; names give identity; a genuine
homograph gets both readings joined by " · ". For every known form, check the existing entry covers its use in this
part; where it does not, put a broadened entry — the old entry whole, plus " · " and the new reading — under
`"__broaden__"`. Output `drafts/<id>/gloss.json`. The reviewer's second pass reads `gloss.json` too and checks every
parse against the line.

## 3. Build and gate
```
python3 build_beowulf.py <id>      # refuses, changing nothing, on any failure; merges the glossary; adds the manifest entry
python3 validate_beowulf.py <id>   # must print PASS; read every WARN and fix what is a real problem
```
If the build writes and the validator then fails, fix the draft and build again; if you cannot, run `git checkout -- .`
from the repository root so that nothing half-built is left, write the problem to `QUESTIONS.md`, release the claim and
stop.

## 4. Publish
Set the part's `status` to `published` in `parts.json`, regenerate `plan.md` with `python3 plan.py`, append one line to
`LOG.md` (date, part, lines, units, new glossary forms, review findings by severity, anything notable), copy any new
house renderings into the table in `conventions.md`, delete your claim file, and commit everything — `<id>.json`,
`beowulf-glossary.json`, `stories.json`, `drafts/<id>/`, the pipeline records — with a message like
`Beowulf: <id> — <name> (lines A–B)`. Push to `main`; if `main` has moved, `git pull --rebase` and push again; never
force. Do not touch `reader.html`, `index.html`, audio, or other works' files. Old English audio is a separate phase:
do not build any.

## If something is wrong that you cannot fix
Write it to `QUESTIONS.md` (what, where, what you decided or why you stopped), release the claim, and stop. A run that
publishes nothing and says why is a good run; a run that publishes a part it is unsure of is not.
