# Analects — what one run does

Read `conventions.md` first (and the Daodejing conventions it points to). The model is
`drafts/analects-01/` and the published `analects-01.json`. Python: standard library only.
The owner is not present; decisions go in `QUESTIONS.md` with what you decided meanwhile.

## 0. Find the next part
`git pull`. The first part in `parts.json` with `status: "todo"` and no live claim in `claims/` is
yours. **One book per run.** A claim older than 6 hours is stale. Write `claims/analects-NN.md`
(date, "drafting"), commit and push before drafting. If all 20 are `published`: append a DONE line to
`LOG.md`, create the empty file `DONE` here, commit, push, stop.

## 1. Check the source
`python3 archive_analects.py` must reproduce `source/analects-zhuxi-siku.json` unchanged
(`git diff --exit-code source/`), and the book's lemma list must hash to its `sha256` in `parts.json`.
Collate the book against `KR1h0004` and `KR1h0005` (same method as the pilot: strip markup and
commentary, compare Han characters with difflib) and list every non-graphic variant for the drafter.

## 2. Draft — `drafts/analects-NN/units.py`
Same format as the pilot: one dict per lemma (stretch between Zhu Xi's comments), in order; `pas`
on the first unit of each numbered passage; `w` the tap-unit line (see the header of the pilot
file); `l`, `i`, `n`. Polyphones state their reading on every occurrence. New glossary entries go in
`glossary_seed.py` (classical senses; Zhu Xi's glosses are the primary crib), written by a separate
**glosser subagent on Sonnet** (`model: "sonnet"`) from the drafted units, and checked entry by entry in
the review pass (owner's rule of 2026-10-12, `../README.md` "Models"). Drafter and reviewer stay on the
strongest model. Units whose wording
repeats an earlier passage (e.g. 17.17 = 1.3, Book 9's 主忠信… = 1.8) take the English already shipped.
Then an adversarial review pass: every grammatical claim in every note true of this line; Chinese →
`l` → `i` agreement; echoes of famous modern translations rephrased; variants noted.

## 3. Build and validate
`python3 build_analects.py analects-NN` — it refuses on any gate failure (text ≠ source, missing
pinyin, unstated polyphone, glossary coverage or unused keys, NFC, round-trip). Then a headless render
check if a browser is available (the story loads under `data-script="chinese"`, one pinyin per
character, a word tap opens the popup).

## 4. Publish
Set the part's `status` to `published` in `parts.json`; add the `about` you wrote to the part; add a
manifest entry to `stories.json` directly after the last `analects-` entry (`work: "論語"`,
`workEn: "The Analects (Lunyu)"`, `language: "Classical Chinese"`, `part: "Book N — 〈title〉 English"`,
`seq: N`). Append a line to `LOG.md`, delete the claim, commit, `git pull --rebase`, push (never force;
on a `stories.json` conflict, re-apply your entry on top). The audio Action builds the Mandarin clips;
in a later run (or after it lands) add `"audio": "audio/analects-NN"` to the story and push.
Do not touch `reader.html`, `index.html`, or other works' files.
