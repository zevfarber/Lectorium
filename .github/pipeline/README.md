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
5. Audio for modern languages is built by `.github/workflows/audio.yml` on the runner when a root
   `*.json` is pushed; ancient-language audio is a separate phase per work.

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
