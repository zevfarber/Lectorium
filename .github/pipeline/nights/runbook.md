# Runbook — one unattended run of the Nights transcription pipeline

This is the procedure behind the routine *Lectorium — Nights transcription* (twice nightly). The
repository owner (Zev) set it up and is not present during runs; he does not read code, so every
decision here is yours within these rules, and anything you cannot decide goes into `QUESTIONS.md`.

**What this pipeline produces:** the verified Arabic text of Macnaghten's *Alif Laila* (Calcutta
1839), page by page, as page archives in `archive/` — **and**, from those archives, the readable
nights the site actually serves. Two jobs, one firing each; step 0 chooses.

## 0. Which job this run does

Changed 2026-09-18. Transcription alone builds an archive nobody can read, and at eight pages a
run the unreadable backlog grew faster than anyone would ever clear it. The owner's rule now: the
reading edition never falls more than about one night behind the transcription.

So, after `git pull` and before anything else:

    python3 tools/nights_index.py --next

- **It prints a unit** → a complete night is sitting unpublished. **Publish it**: stop reading
  this file and follow `publish-runbook.md` instead.
- **It prints nothing** → every complete night is published. **Transcribe** the next eight pages:
  continue with 0.1 below.

That is the whole decision, and it is self-regulating: eight pages yield about one and a half
nights, so transcription proceeds at roughly two runs in five and the backlog stays at a night or
so. Nothing here needs the owner, and the ratio needs no tuning.

## 0.1 Orientation (a transcribing run)

1. `git pull`. Read `.github/pipeline/README.md`, this file, `conventions.md`, `plan.md`,
   `LOG.md` and `QUESTIONS.md` (if present). Do **not** read the archives in full; open one
   (`archive/pp003-012.json`) to see the shape.
2. Derive the state from the repository: the last transcribed PDF page is the highest page in
   the `pages` field across `archive/pp*.json` (`printed pp. A-B (PDF pages X-Y)`; use Y). The
   next batch is PDF pages **Y+1 … Y+8** (eight pages per run). Vol. 1 ends at PDF page 938
   (`plan.md`); if Y = 938 the volume is done: create the empty marker `DONE`, append a LOG line,
   commit, push, stop.
3. Claim: create `claims/pp<Y+1>-<Y+8>.md` with the UTC time and your session id, commit and
   push it before doing anything else. If a claim for those pages exists and is less than 3 hours
   old, another run holds it — stop. A claim older than 3 hours is abandoned; overwrite it.

## 1. Tools

Everything is under `.github/pipeline/nights/`. Make the environment ready (skip what is already
present; none of this needs approval):

    pip install opencv-python-headless numpy pymupdf
    apt-get install -y poppler-utils tesseract-ocr        # if apt works; otherwise pymupdf renders and the draft is skipped

**The OCR model.** `tools/td/calc.traineddata` is Tesseract's Arabic model fine-tuned on this
book's type. If the file is missing from the repository (it was too large for the first upload),
build it once and commit it, so later runs skip this:

    cd .github/pipeline/nights/tools
    curl -L -o td/arabest.traineddata https://raw.githubusercontent.com/tesseract-ocr/tessdata_best/main/ara.traineddata
    unzip -o lines.zip                       # the verified training lines (png + gt.txt)
    TD=td ITER=1500 bash finetune.sh         # ~10 min CPU; writes td/calc.traineddata

If `lstmtraining` is not available, use `--model arabest` in the call below instead (a slightly
weaker draft) and say so in the LOG. `arabest.traineddata` itself is never committed (fetchable).

`tools/nights_ocr.py` renders, finds the lines, OCRs a draft with the model, and writes per-page
crops and bands. If `tesseract` cannot be installed the script still runs and the
draft is empty — the correction agents then transcribe from the crops alone. That costs a little
more attention, not correctness.

The scan is split into 50-page chunks in `source/`: `calcutta2-vol1-p<A>-<B>.pdf` holds PDF pages
A–B. Pass `--offset A-1` so output folders carry absolute page numbers. A batch that straddles two
chunks is run as two calls into the same `--out` folder.

    python3 tools/nights_ocr.py --pdf source/calcutta2-vol1-p001-050.pdf --pages 31-38 --offset 0 \
        --out /tmp/run --tessdata tools/td --model calc

Read its output. A line `<-- GATE` means a double-pitch gap: a line may have been dropped by the
detector. That is not a stop — the page bands cover it — but note the page for the adjudicator.

## 2. Transcribe — two independent passes, one adjudication

Use the Agent tool, `general-purpose`, in waves of four pages at a time.

**Pass 1** — for each page, one agent: prompt = `prompts/correct.md` with `__DIR__` replaced by
the absolute path of `/tmp/run/p<ppp>` and `__OUT__` by `pass1.json`. Tell it to read the prompt
file and follow it. Record each agent's token count.

**Pass 2** — the same, fresh agents, `__OUT__` = `pass2.json`, and add to the instruction: *ignore
pass1.json in that folder; do not open it*. Independence is the point.

**Diff** — `python3 tools/diff_passes.py /tmp/run <first> <last>` → `/tmp/run/disputes.json`.
Expect roughly four disagreements per page. Forty on one page means a pass went wrong; rerun
that page's worse pass before adjudicating.

**Adjudicate** — one agent for the whole batch: prompt = `prompts/adjudicate.md` with `__RUN__`
replaced by `/tmp/run`; tell it the page range so it reads every page join. It writes
`/tmp/run/verdicts.json`.

**Apply** — `python3 tools/apply_verdicts.py /tmp/run <first> <last> archive/pp<A>-<B>.json`
where A and B are the **printed** page numbers (PDF page − 18), zero-padded to three digits. Read
its output: any `JOIN NOTE` that reports a broken join means a line is missing somewhere — find it
in the bands, fix `pass1.json` by hand from the image, and re-apply. Low-confidence verdicts go in
the LOG line.

## 3. Gate

    python3 tools/validate_archive.py archive/pp<A>-<B>.json --prev archive/<previous>.json

must print `RESULT PASS`. Read the page joins it prints; every one must read as continuous text.
`git diff --stat` shows exactly: the new archive (added), the pipeline files you touched (claim,
LOG, plan). Nothing else — never a file in the repository root, never another work's files.

## 4. Publish

Commit message: `Nights: pp. <A>-<B> transcribed`. Push to `main`; if `main` moved, `git pull
--rebase` and push again, up to three times; never force. Then delete your claim file, update
`plan.md` (last page done, pages remaining), append the LOG line, commit and push.

## 5. Retrain the OCR model (every run whose archive brings the total past a multiple of 200 lines)

The line images and verified text of every archived page are training data for the draft model,
and the draft gets better as the corpus grows. When `plan.md` says a retrain is due: for each page
of this batch, write `tools/lines/p<ppp>_<ll>.png` (the 1x flattened crop `nights_ocr.py` used;
regenerate with `--keep-ocr-crops`) and `.gt.txt` (the archived line, bare text, one line) — only
for lines whose crop matches exactly one printed line — then run `bash tools/finetune.sh` from
`tools/` (needs `lstmtraining`; `apt-get install -y tesseract-ocr` provides it; if unavailable,
skip and note it in the LOG). Commit the new `tools/td/calc.traineddata` and the lines with the
batch. Never commit a model that made the draft worse on the batch's own pages.

## 6. Record

`LOG.md`: one line per run — UTC time · PDF pages · lines archived · disagreements · low-confidence
verdicts · tokens (pass 1 / pass 2 / adjudication) · anything a person should know. Under 400
characters. `QUESTIONS.md`: decisions the rules do not settle, with what you decided meanwhile.
Do not send email, do not use Google Drive, do not create, change or disable any routine.

## What a transcribing run never does

*(A publishing run has its own list at the end of `publish-runbook.md`; it is the one kind of run
allowed to write a story file and `stories.json`.)*

Transcribes more than eight pages; touches `reader.html`, `index.html`, `stories.json`, audio,
any story file, or another work's files; edits `source/`; consults a modern edition or
translation of the Nights for the wording of a line (the images are the only authority); pushes
an archive that failed the gate; "corrects" the edition's spelling.
