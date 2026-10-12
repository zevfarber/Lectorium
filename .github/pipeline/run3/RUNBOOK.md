# Run 3 — what one firing does (all works)

Run 3 is the owner's third production run: the unusual texts, finished one part per firing, one work after
another (`.github/pipeline/queue-run3.txt`). It is separate from the shared text pipeline
(`queue.txt`) and from the Nights; it never touches their files. The owner is not present; decisions go in
the work's `QUESTIONS.md` with what was decided meanwhile, and nothing waits on him. Python: standard
library, plus PyMuPDF (`pip install pymupdf`) where a step reads a scanned page.

Run every command from the work's folder, `.github/pipeline/<work>/`; `R3` below means
`python3 ../run3/r3.py`.

## 0. Find the part
`git pull`. Run `R3 next`. It prints one of:
- `ALL DONE` — every work in the queue has its DONE marker. Stop at once: no other file read, no commit,
  no log line. An idle firing must cost almost nothing.
- `WORK <w>` + `COMPLETE` — every part of <w> is published: run `R3 done <w>`, commit and push the DONE
  marker and the LOG line, and stop. The next firing moves to the next work by itself.
- `WORK <w>` + `BUSY` — another firing holds a live claim on every remaining part: stop.
- `SKIP <w>` lines — a work whose only remaining parts are blocked is passed over (its blocked parts wait for the
  owner); the answer that follows is this firing's job.
- `WORK <w>`, `PART <id>`, `ACTION establish|draft` — this firing's job. Read `<w>/conventions.md` and
  `<w>/runbook.md` now.

Claim the part: `R3 claim <w> <id> <action>`; commit the claim file and push it to `main` before any other
work. A claim older than 6 hours is stale; `R3 next` ignores it — delete it in the same commit.

## 1a. ACTION establish (scan-based works: Cid, Mabinogi, the Hammurabi gap)
The text of the part does not exist yet in reliable form. Nothing is drafted in this firing.
`R3 establish-packet <w> <id>` writes `drafts/<id>/establish.md`: the inputs and the exact procedure.
Follow it — the page image is the authority for every letter. Write the established file it names, then
`R3 pin <w> <id>` (it checks the file and pins its sha256; status becomes `established`). Append a LOG line
(lines corrected, readings unsure), release the claim (`R3 release <w> <id>`), commit everything, push, stop.

## 1b. ACTION draft
`R3 packet <w> <id>` — refuses if the pinned source no longer matches the sha256 in `parts.json` (follow
"If something is wrong" below). It writes `drafts/<id>/packet.md` and, for most
works, `novel-forms.json` / `known-forms.json`.

## 2. Draft — three roles, each a separate subagent with only the files named
Drafter and reviewer run on the strongest model available (the routine's own); the glosser runs on Sonnet
(`model: "sonnet"` in the Agent call). The work's `runbook.md` says exactly what each role gets and writes.

**Drafter** — writes `drafts/<id>/units.json` in the work's schema (runbook.md). `t` / the source words
are cut from the packet by a small script, never retyped. The model of shape and register is the work's
published pilot (named in runbook.md). Every unit has `l`; `i` wherever it differs from `l`; a note that
leads with what the reader needs in order to read these words. No modern translation is opened or
recalled; an English phrase that arrives fully formed is rebuilt from the grammar. Uncertain readings are
said to be uncertain.

**Reviewer** — adversarial; same files plus `units.json` (and `gloss.json` on its second pass). Checks every
grammatical label in every note against the form, original → `l` word by word, `l` ↔ `i` in sense and
force, remembered English in `i`, consistency with the published parts' renderings and the house
renderings in conventions.md; for words-model works, every sign, role and value against the source/plate.
Edits `units.json` in place by script and writes `drafts/<id>/review.md` (every change: unit · field ·
severity · what was wrong · what was done; every finding refused, with the reason). Two passes.

**Glosser** (Sonnet) — glossary entries for every new form/lemma in the work's entry format, general to the
form, never pinned to a line; a known entry that does not cover this part's use is broadened (old entry
whole + " · " + new reading) under `"__broaden__"`. Writes `drafts/<id>/gloss.json`. The reviewer's
second pass checks every entry against the text. Sonnet invents modern forms and misnames grammar — the
reviewer budgets a real check.

## 3. Build and gate
```
R3 build <w> <id>       # refuses, changing nothing, on any error; writes the story, glossary, manifest entry
R3 validate <w> <id>    # must print PASS; read every WARN and fix what is a real problem
```
For cuneiform and Luwian works a sign missing from the shared sign glossary is added only with
`python3 ../run3/signs.py add …` (it takes the character from Unicode by name and updates the copy embedded
in `index.html` / `reader.html` — the only change a run may make to those two files). `python3
../run3/signs.py check` must print "in sync" before you commit.
If the build or the validator cannot be satisfied: `git checkout -- .` from the repository root (and remove
any new untracked story file), then follow "If something is wrong" below.

## 4. Publish
`R3 publish <w> <id>` (re-validates; status published, plan.md, claim released). Append one line to `LOG.md` (date, part,
cite, units, new glossary forms, review findings by severity, anything notable). Copy any new house
renderings into conventions.md. Commit everything — the story file, the glossary, `stories.json`,
`drafts/<id>/`, the pipeline records (and the sign glossary + index.html + reader.html if signs.py added
a sign) — with a message like `<Work>: <id> — <name>`. Push to `main`; if `main` has moved,
`git pull --rebase` and push again; never force.

Audio is not this run's job: `.github/workflows/audio.yml` voices a pushed part by itself when its
language has a settled voice (Akkadian does; see `run3/README.md`), within the $10/month budget. Do not
build or edit audio.

## If something is wrong that you cannot fix
Nothing survives a firing unless it is pushed. So:
- a problem only this firing hit (a tool failed, the work ran out of time, a draft would not validate but could
  next time): write it to QUESTIONS.md (what, where, what you decided or why you stopped), release the claim
  (`R3 release <w> <id>`), commit QUESTIONS.md, LOG.md and the claim removal, push, stop;
- a problem the next firing would hit again (the pinned source is wrong, a page is unreadable, a sign has no
  Unicode character, the conventions do not say what to do): `R3 block <w> <id> "<one-line reason>"` — it marks
  the part blocked so later firings go on to the next part, writes the reason to QUESTIONS.md and releases the
  claim — then add the detail to QUESTIONS.md, commit, push, stop.
A run that publishes nothing and says why is a good run; a run that publishes a part it is unsure of is not.
Never send email, never use Google Drive, never create, change or disable a routine. Never touch another
work's files, `queue.txt`, or anything outside `.github/pipeline/<w>/`, the work's story and glossary files,
`stories.json`, and (via signs.py only) the sign glossaries and their embedded copies.
