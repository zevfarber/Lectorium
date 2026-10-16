# Lectorium pipeline — how texts are produced and published unattended

*Written 2026-09-14, the day this publishing model was proved.*

Lectorium's texts are prepared by scheduled Claude runs (routines at claude.ai/code) that have
**this repository attached**, which is what lets them push. The site is GitHub Pages served from
`main`, so a push to `main` is publication. Each language or work has its own folder here with:

- the verified public-domain **source text** and a `parts.json` describing how it is cut;
- **conventions.md** — the editorial rules for that work, distilled from its published parts;
- **plan.md** — the parts and their status;
- **runbook.md** — what one run does, step by step;
- a **validator** the run must pass before pushing;
- `LOG.md`, `QUESTIONS.md`, `claims/` — the run's own records.

Rules that apply to every run, whatever the work:

1. The repository is the only source of state. Derive what is published from the files in it, not
   from memory, not from a log line.
2. One batch per run, claimed before drafting, gated before pushing, pushed to `main` with an
   ordinary commit; rebase-and-retry on a moved `main`, never force.
3. Sole-source translation: the public-domain original plus public-domain reference works. No
   modern translation is opened for wording.
4. The owner is not present. Decisions go in `QUESTIONS.md` with what was decided meanwhile;
   nothing waits on him. A run never sends email, never uses Google Drive, and never creates,
   changes or disables a routine.
5. **Missing punctuation in the pinned source is corrected by the run, without asking.** If the
   source drops a stop, comma or other mark that the printed edition has (or that an already-published
   part prints for the same line), the run adds it to the source file, updates the `sha256` of every
   part containing that line in `parts.json`, makes the draft's `t` match, and carries on. Limits:
   punctuation only, never a letter, accent or word; one mark per place; nothing else in the source
   changes. Record each correction (work, line, mark added, parts re-pinned) in the work's `LOG.md`.
   The owner approved this on 2026-10-06 (first cases: Odyssey 16.185 and 17.146); the run does not
   need to ask, and does not need to stop. A defect that is not punctuation still goes to `QUESTIONS.md`.
6. Audio for modern languages is built by `.github/workflows/audio.yml` on the runner when a root
   `*.json` is pushed; ancient-language audio is a separate phase per work.
7. **If a piece can't be done, set it aside and keep going** (owner's standing rule, 2026-10-16).
   A firing must not be spent stopping on a problem. When a run cannot produce part of the text —
   the source is damaged or unreadable, the conventions do not cover the case, or the content is
   something you will not translate — set aside the smallest piece you can (a few lines rather
   than the whole part, night or chapter), finish and publish the rest, and mark the gap for the
   reader with a short note. Record in `QUESTIONS.md` exactly what was set aside, where and why.
   If the piece cannot be published at all without what is missing, mark it blocked: add its id
   and the reason, one per line, to `BLOCKED` in the work's folder, then go straight on to the
   next piece **in the same firing**. When finding the next part, pass over every id listed in
   `BLOCKED`; a blocked part is not retried until the owner rules on it, and a work whose only
   unpublished parts are blocked counts as finished for the queue (write `DONE` and say so in
   `QUESTIONS.md`). This overrides any "write it down and stop" in a work's runbook. A firing
   should end with something published unless there was truly nothing left it could do.

## Models — the cheapest one that does the job (owner's standing rule, 2026-10-12)

Every run, in every routine: if Sonnet can do a piece of work without losing accuracy, Sonnet does
it (`model: "sonnet"` in the Agent call). The strongest model available (the routine's own — Opus,
or Fable) is kept for what needs it, and is used freely there.
- **Sonnet:** mechanical and copying work — shaping text already cut by a script into the work's
  JSON, glossary entries, reformatting, applying a decided list of edits, summarising logs, checking
  coverage or file lists; and any role a runbook gives to Sonnet.
- **Strongest model:** reading scans and plates where no second reader checks the result, drafting
  translations and notes, adversarial review, adjudicating disputes, and any judgment where an error
  would reach the reader unnoticed.
- Sonnet's output is checked by script or by a strongest-model reviewer wherever it matters; never
  take its word that it checked itself.
- Where a work's runbook names a model for a role, follow it. If a Sonnet role keeps producing errors
  that the review has to catch, move that role back to the strongest model and say so in
  `QUESTIONS.md`. The LOG line says which roles ran on Sonnet.

## The queue — one routine for every work, forever

There is one routine, *Lectorium — text pipeline*, for all works. It does not know which text it is
working on until it reads `queue.txt` in this folder: one work-folder name per line, in the order
the owner wants them produced (blank lines and lines starting with `#` are ignored). A work is
finished when its folder contains an empty file named `DONE`, which the work's own runbook creates
when the last part is published.

What a run does first, before reading anything else:

    git pull
    for each name in .github/pipeline/queue.txt, in order:
        if .github/pipeline/<name>/DONE does not exist → this is the work; open its runbook.md and follow it
    if every listed work has a DONE marker → stop at once

Stopping at once means: no other file read, no commit, no LOG line, no message to anyone. An idle
firing must cost almost nothing, because the routine keeps its schedule while the owner is between
texts, and only the queue decides whether there is work. Adding a text to Lectorium is: put its
folder here (source, parts, conventions, runbook, validator), add its name to `queue.txt`, and
delete any stale `DONE`. Nothing about the routine itself changes.

The laptop's old five-minute "auto-publish" task (OneDrive master → repository) has been retired in
favour of this model; the repository is the master now.

`HEARTBEAT.md` is the record of the 2026-09-14 smoke test that proved a routine can push.

## Run 3 — the unusual texts (since 2026-10-12)

A second, separate routine works through `queue-run3.txt` (Hammurabi, Kebra Nagast, Secret History, Mabinogi,
Cid, Azatiwada, Sumerian King List) with its own tools in `run3/` — see `run3/README.md` and `run3/RUNBOOK.md`.
It never reads or changes `queue.txt`, and the text pipeline never reads `queue-run3.txt`.
