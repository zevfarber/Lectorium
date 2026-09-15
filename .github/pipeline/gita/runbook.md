# Bhagavadgītā — what one run does

Everything you need is in this folder (`.github/pipeline/gita/`). Read `conventions.md` first,
then this file, then do the steps in order. Never draft from memory of the Gītā's wording: the
text is `source/`, the rules are `conventions.md`, and the gate is `validate_gita.py`. The owner
is not present; decisions go in `QUESTIONS.md` with what you decided meanwhile.

Python needs `indic_transliteration` (`pip install indic_transliteration`).

## 0. One-time housekeeping
If the legacy pilot files `build.py`, `words-01-16.txt`, `words-17-32.txt`, `words-33-47.txt`, `trans.txt`,
`wikisource-ch1.txt`, `gretil-ch1.txt`, `wiki-parsed.json` still exist in this folder, `git rm` them in
your first commit — they were superseded by `drafts/ch01/`, `source/` and `build_gita.py`.

## 0b. Find the next chapter
`git pull`. Read `plan.md`: the first chapter whose status is `todo` and that has no live claim
in `claims/` is yours. A claim file older than 6 hours is stale — delete it and take the chapter.
Write `claims/chNN.md` (one line: date, "drafting"), commit and push it to `main` before drafting,
so a concurrent run takes the next chapter. If all 18 are published, append a DONE line to
`LOG.md` and stop.

## 1. Verify the text you will draft from
`python3 -c "import gita_lib as g; print(g.sha(g.chapter_text(NN)))"` must equal the chapter's
`sha256` in `parts.json`, and `g.collate(NN)` must return only the verses listed in
`variantsVsBORI` as `VAR` (plus any number of `orth`). If either fails, the source is in doubt:
write what you found to `QUESTIONS.md`, release the claim, and stop without drafting.

## 2. Draft — three roles, each a separate subagent with only the files named
Create `drafts/chNN/` with `words.txt`, `trans.txt`, `about.txt` in the formats described at the
top of `build_gita.py` (copy the shape of `drafts/ch01/`).

**Drafter** (gets: the chapter's verses from `source/`, `conventions.md`, `drafts/ch01/` as the
model, the chapter's `variantsVsBORI` list with the BORI readings from `source/bori-iast.txt`,
and the `corrections.json` entries for the chapter). Produces `words.txt` and `trans.txt`. Rules
that matter most: every space-delimited Devanagari token is one word-line; the reading undoes
sandhi and hyphenates compounds; every morph has lemma and gloss in the fixed format; `l` is
structurally transparent, `i` is real English; notes lead with what the reader needs to read the
verse, and the note of every verse in `variantsVsBORI` states the BORI reading, the note of every
corrected verse names the correction. No modern translation is opened, ever; Monier-Williams,
Apte and Śaṅkara's commentary are the only aids. The house renderings for the famous verses in
`conventions.md` are used as written.

**Reviewer** (gets the same sources plus the drafter's two files). Its first duty is to check that
every factual claim in every note is true against the Sanskrit — a form named wrongly, a wrong
root, a false statement about the text — and that every reading undoes the sandhi correctly.
Then translation accuracy, then register. It returns a list of corrections with the verse number;
the drafter applies them. Two passes.

**Glosser** (gets `words.txt` only). Checks that every morph gloss is a dictionary meaning plus the
form in parentheses, consistent across repeated words in the chapter (the same token gets the same
gloss), and that names are identified on first occurrence.

`about.txt`: one paragraph on what the chapter is and does, for the "Background information" box.

## 3. Build and gate
```
python3 build_gita.py NN          # refuses if the tokens do not tile the source, or a required note is missing
python3 validate_gita.py NN       # must print PASS; read every WARN and fix what is a real problem
```
Then add the chapter to `stories.json` (copy the `gita-ch01` entry, change id/titleEn/part/file;
place it after the previous chapter's entry) and check `python3 -c "import json;json.load(open('stories.json'))"`
from the repository root.

## 4. Publish
Set the chapter's status to `published` in `parts.json` and `plan.md`, append one line to
`LOG.md` (date, chapter, verses, glossary size, review passes, anything notable), delete your
claim file, and commit everything — the story `.json`, `stories.json`, `drafts/chNN/`, the
pipeline records — with a message like `Gita: chapter NN — <title>`. Push to `main`; if `main`
has moved, `git pull --rebase` and push again; never force. Do not touch `reader.html`,
`index.html`, audio, or other works' files.

## If something is wrong that you cannot fix
Write it to `QUESTIONS.md` (what, where, what you decided or why you stopped), release the claim,
and stop. A run that publishes nothing and says why is a good run; a run that publishes a chapter
it is unsure of is not.
