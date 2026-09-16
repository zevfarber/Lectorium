# Runbook — one unattended run of the Slovo text pipeline

This is the procedure behind the scheduled routine *Lectorium — Igor's Campaign, one part per
run*. The routine's own instructions point here. The repository owner (Zev) set the routine up and
is not present during runs; he does not read code, so every decision here is yours to make within
these rules, and anything you cannot decide goes into `QUESTIONS.md` rather than to him.

## 0. Orientation (every run, before anything else)

1. `git pull` — you are on the checked-out `zevfarber/Lectorium`. Read, in this order:
   `.github/pipeline/README.md`, this file, `plan.md`, `conventions.md`, `parts.json`,
   `LOG.md` (if present), `QUESTIONS.md` (if present), then the two published models
   `slovo-proem.json` and `slovo-part1.json` in the repository root, in full.
2. Derive the state from the repository, never from memory or from the LOG alone: the published
   Slovo parts are the `slovo-part<N>.json` files present in the root **and** registered in
   `stories.json`. The next part is the lowest N in 2…10 that is not published. If parts 2–10 are
   all published, the poem's text phase is finished: append a `DONE` line to `LOG.md`, create the
   empty marker file `.github/pipeline/slovo/DONE`, commit and push those two changes, and stop —
   do not draft anything. The marker is what tells the shared routine to skip this work from then
   on (see `.github/pipeline/README.md`, "The queue").
3. Claim: create `.github/pipeline/slovo/claims/part<N>.md` with the UTC time and your session
   id, commit and push it before drafting. If a claim file for that part already exists and is
   less than 4 hours old, another run holds it — take the next unpublished part instead, or stop
   if there is none. A claim older than 4 hours is abandoned; overwrite it.

## 1. Extract the part

Cut the part's text out of `source-1800.txt` using the exact `opens` and `ends` strings from
`parts.json`; whitespace-normalise; check the word count and sha256 against `parts.json`. If they
do not match, stop and write the discrepancy to `QUESTIONS.md` — never draft from a text you have
not verified. Whenever a run stops without publishing, delete its own claim file in the same
commit as the LOG/QUESTIONS entry, so the next run can take the part.

## 2. Draft

Work as a small team with the Agent tool. The drafter and the reviewer run on the strongest model
available (the routine's own model); the glosser runs on Sonnet (`model: "sonnet"` in the Agent
call) — its work is mechanical and the cheaper model does it as well:

- **Drafter** — segments into sense-units at the 1800 punctuation, writes `t` (verbatim), `tr`,
  `l`, `i`, `n` for every unit, following `conventions.md` and the two models exactly.
- **Adversarial reviewer** — reads the draft against the source with the rules, hunting for:
  units whose `t` differs from the source by even one character; literal translations that
  silently follow a modern translation's phrasing; grammatical claims in notes that are false
  (check every aorist/imperfect/dual/vocative claim against the form itself); history stated
  as fact that is conjecture; dark places rendered with false confidence; `i` that is
  childish or that adds content; missing `p`. Returns a list of blocking defects with fixes.
- **Glosser** — builds the inline glossary for every token the reader's tokenizer produces
  (run `validate_slovo.py` to see the missing list), in the `lemma — gloss (grammar)` form,
  matching the style of the existing entries; reuses the exact wording of an entry that already
  exists in `slovo-proem.json` / `slovo-part1.json` for the same key.

Apply the reviewer's fixes, then run the reviewer once more on the result. Two review passes is
the norm; stop at three.

## 3. Gate

`python3 .github/pipeline/slovo/validate_slovo.py slovo-part<N>.json --stories stories.json`
must print `RESULT PASS`. Fix and re-run until it does. Also:

- `python3 -c "import json;json.load(open('stories.json'))"` after editing the manifest.
- `git diff --stat` shows exactly: the new story file (added), `stories.json` (modified, additions
  only), and the pipeline files you touched (claim, LOG, plan status). Nothing else. If anything
  else changed, revert it.
- Spot-check for echoes of modern translations on the part's most quotable lines: think of the
  best-known English renderings you can recall of those lines and make sure yours does not
  reproduce a distinctive phrase verbatim. Record what you checked in the LOG line.

## 4. Publish

The site is GitHub Pages served from `main`; there is no review step, no CI to wait for, and
publishing means pushing to `main`. The owner authorises this routine to push to `main` directly.
Commit message: `Slovo: part <N> — <title>`. If the push is rejected because `main` moved, `git
pull --rebase` and push again, up to three times; never force-push. After the push, fetch
`https://raw.githubusercontent.com/zevfarber/Lectorium/main/slovo-part<N>.json` and confirm it
parses; then delete your claim file, update the status column in `plan.md`, append the LOG line,
commit and push those housekeeping changes.

## 5. Record

`LOG.md` gets one line per run: UTC time · part · units · glossary keys · review passes · echo
phrases checked · anything a person should know. Under 300 characters.

`QUESTIONS.md` is for decisions the rules do not settle. Write the question, what you decided in
the meantime and why. Do not stop the run for a question unless the text itself is in doubt
(step 1). Do not send email, do not use Google Drive, and do not create, change or disable any
routine — the owner watches the site and the LOG.

## What a run never does

Re-issues a published part; touches `reader.html`, `index.html`, audio, or any other work's files;
edits the source text; drafts more than one part; consults a modern translation; pushes anything
that failed the gate.
