# The Upanishads — what one run does

Everything you need is in this folder (`.github/pipeline/upanishads/`). Read `conventions.md` first,
then this file, then do the steps in order. Never draft from memory of the Upanishads' wording: the
text is `source/`, the rules are `conventions.md`, the gate is `validate_up.py`. The owner is not
present; decisions go in `QUESTIONS.md` with what you decided meanwhile.

Python needs `indic_transliteration` (`pip install indic_transliteration`) for transliteration checks.

## 0. Find the next part
`git pull`. In `parts.json` the first part whose status is `todo` and that has no live claim in
`claims/` is yours (a claim older than 6 hours is stale: delete it and take the part). Write
`claims/<part>.md` (one line: date, "drafting"), commit and push it to `main` before drafting. If
every part is `published`: append a DONE line to `LOG.md`, create the empty marker file
`.github/pipeline/upanishads/DONE`, commit and push those two changes, and stop. A part you cannot
do: set its status to `blocked`, say why in `QUESTIONS.md`, release the claim and take the next part
(README rule 7). Never write DONE while a part is blocked.

## 1. Verify the text
`python3 -c "import up_lib as U; print(U.sha(U.text('<part>')))"` must equal the part's `sha256` in
`parts.json`. If not, the source has changed since setup: write it to `QUESTIONS.md`, release the
claim and stop.

## 2. Draft — three roles, each a separate subagent with only the files named
The drafter and the reviewer run on the strongest model available (the routine's own model); the
glosser runs on Sonnet (`model: "sonnet"`).

**Drafter** (gets `source/<part>.txt`, `conventions.md`, `../gita/conventions.md`, `../../../gita-ch01.json`
as the model of shape and register, the published Upanishad parts before this one, and the witness
in `source/witness/` for this Upanishad if there is one). Produces `drafts/<part>/words.txt`,
`trans.txt`, `about.txt` (formats at the top of `build_up.py`; `python3 -c "import up_lib as U;
[print(k, U.words_of(u)) for k,u in enumerate(U.read_part('<part>'),1)]"` lists the words to cover,
unit by unit). Units are keyed #1, #2 … in order, numbered or not.

**Reviewer** (same sources plus the drafter's files). First duty: every factual claim in every note
is true against the Sanskrit (a form named wrongly, a wrong root, a false statement about the text),
and every reading undoes the sandhi correctly. Then: the house renderings in `conventions.md` used
as written; witness differences reported; translation accuracy; register. Returns corrections by
unit; the drafter applies them. Two passes.

**Glosser** (gets `words.txt` and the published parts' glossaries). Every morph gloss a dictionary
meaning plus the form in parentheses; the same token glossed the same way as in published parts;
names identified on first occurrence.

`about.txt`: one paragraph on what the section is and does, for the "Background information" box.
For the first part of each Upanishad, add two sentences on the Upanishad itself (which Veda it
belongs to, what it is known for).

## 3. Build and gate
```
python3 build_up.py <part>         # refuses if the words do not tile the source
python3 validate_up.py <part>      # must print PASS; read every WARN and fix what is a real problem
```
Then add the part to `stories.json` after the previous Upanishad part (or, for the first, at the
end): `{"id", "title", "titleEn", "language": "Sanskrit", "work": "उपनिषदः", "workEn": "The
Upanishads", "part": <label>, "group": <Īśa|Kena|Kaṭha|Muṇḍaka|Māṇḍūkya>, "file", "seq"}` from
`parts.json`, and check `python3 -c "import json;json.load(open('stories.json'))"` from the root.

## 4. Publish
Set the part's status to `published` in `parts.json`, append one line to `LOG.md` (date, part, units,
glossary size, review passes, witness differences noted, anything notable), delete your claim file,
and commit everything — the story `.json`, `stories.json`, `drafts/<part>/`, the pipeline records —
with a message like `Upanishads: katha-1 — Naciketas Goes to Death`. Push to `main`; if `main` has
moved, `git pull --rebase` and push again; never force. Do not touch `reader.html`, `index.html`,
audio, or other works' files.

## If something is wrong that you cannot fix
Write it to `QUESTIONS.md` (what, where, what you decided), mark the part `blocked`, release the
claim, and go on to the next part if the firing has room, else stop.
