# Mencius — what one run does

Read `conventions.md` first, then `../analects/conventions.md` it builds on. The model of shape and
register is the published Analects (`../../../analects-02.json` and later) and `../analects/drafts/`.
Python: standard library only. The owner is not present; decisions go in `QUESTIONS.md` with what you
decided meanwhile.

## 0. Find the next part
`git pull`. The first part in `parts.json` with `status: "todo"` and no live claim in `claims/` is
yours. **One part per run.** A claim older than 6 hours is stale. Write `claims/mencius-NN.md` (date,
"drafting"), commit and push before drafting. A part you cannot do: set its status to `blocked`, say
why in `QUESTIONS.md`, release the claim and take the next (README rule 7). If every part is
`published`: append a DONE line to `LOG.md`, create the empty file `DONE` here, commit, push, stop.
Never write DONE while a part is blocked.

## 1. Check the source
`python3 archive_mencius.py` must reproduce `source/mencius-zhuxi-siku.json` and `parts.json`'s
source fields unchanged (`git diff --exit-code source/ parts.json` — only `status` lines you changed
may differ; if the archive rewrites a status, restore it). The build itself refuses a part whose lemma
list does not hash to its `sha256`. Collate the part against Zhao Qi (`source/witness/KR1h0002_*`;
strip markup, parentheses and commentary, compare Han characters with difflib) and list every
non-graphic variant for the drafter. A clear transcription slip goes into `emend.json`.

## 2. Draft — `drafts/mencius-NN/units.py` and `drafts/mencius-NN/about.txt`
Same unit format as the Analects (see the header of `../analects/drafts/analects-01/units.py`): one
dict per lemma, in order; `pas` on the first unit of each chapter (`"4B.25"`); `w` the tap-unit line;
`l`, `i`, `n`. Polyphones state their reading on every occurrence. `about.txt`: one paragraph for the
reader — which book and chapters, who is talking to whom, what is argued, what the original lacks
(punctuation), the chapter-number note for 7A.

Three roles, each a separate subagent:
- **Drafter** (strongest model): units and about.
- **Glosser** (Sonnet, `model: "sonnet"`): new and first-use entries in `glossary_seed.py` from the
  drafted units — including rewriting every Analects-seeded entry this part uses for the first time
  (see conventions). Zhu Xi's and Zhao Qi's glosses are the primary crib; classical senses only.
- **Reviewer** (strongest model), adversarial: every grammatical claim in every note true of this
  line; Chinese → `l` → `i` agreement; house renderings; echoes of famous modern translations
  rephrased; variants noted; every glossary entry checked.

## 3. Build and validate
`python3 build_mencius.py mencius-NN` — it refuses on any gate failure (text ≠ source after emends,
chapter marks ≠ source, missing pinyin, unstated polyphone, glossary coverage or unused keys, NFC,
round-trip, no about). Then a headless render check if a browser is available.

## 4. Publish
Set the part's `status` to `published` in `parts.json`. Add a manifest entry to `stories.json` directly
after the last `mencius-` entry (the first one goes after the last `analects-` entry):
`work: "孟子"`, `workEn: "Mencius (Mengzi)"`, `language: "Classical Chinese"`,
`part: "4B.25–33 — 離婁 Li Lou"` (cite — 篇 title — English), `seq: N`, `title`/`titleEn` as in the
story. Append a line to `LOG.md`, delete the claim, commit, `git pull --rebase`, push (never force; on
a `stories.json` conflict, re-apply your entry on top). The audio Action builds the clips; a later
run adds `"audio": "audio/mencius-NN"` once `align.json` exists. Do not touch `reader.html`,
`index.html`, or other works' files.
