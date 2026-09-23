# Runbook — publishing one night

*Added 2026-09-18. The transcription runbook (`runbook.md`) gets the words off the page; this one
turns them into something a reader can open. `runbook.md` step 0 decides which of the two a given
firing does — you are here because a complete night was sitting unpublished.*

**Why this exists.** Transcription alone builds an archive nobody can read. The owner's rule is
that the reading edition must never fall more than about one night behind the transcription, so
publishing takes priority over transcribing whenever a complete night is waiting. One night per
run, and a run that publishes does not also transcribe.

## 0. The unit

    python3 tools/nights_index.py            # the whole table, for the LOG
    python3 tools/nights_index.py --next     # the one unit to do, as JSON

`--next` gives `{night, id, start, end, lines}`. That is your unit; do not choose another, and do
not re-derive the boundaries by eye. If it prints nothing, there is no complete unpublished
night — you should not be in this runbook; go back to `runbook.md` step 0.

If the table prints `ORDINAL MISMATCH`, a night formula was missed or wrongly detected. Publish
nothing past it: record it in `QUESTIONS.md` with what you found, and transcribe instead.

**Night 0 (`nights-frame-02`) is a special case.** It is the frame material between the pilot and
Night 1, and it overlaps the pilot. Read `nights-frame-01.json`'s last sentence, strip its
vowels, find those words in the archived lines, and begin your text at the word after them —
never at P03L01, which would republish what the pilot already covers. Say in the LOG where you
started.

## 1. Claim

Create `claims/publish-<id>.md` (e.g. `claims/publish-nights-03.md`) with the UTC time and your
session id; commit and push it before drafting anything. A claim under 3 hours old belongs to
another run — stop. Older than 3 hours, it is abandoned: overwrite it.

## 2. Read before drafting

`reading-conventions.md` — all of it, every run. Then open `nights-frame-01.json`, the pilot, and
look at how one sentence is built: vocalised `t`, IJMES `tr`, literal `l`, idiomatic `i`, note
`n`. It is the model; match it rather than inventing a house style per night.

Get your text:

    python3 tools/nights_index.py --text <night> > /tmp/unit.json

That is the archived lines, in order, with their page/line references. **The archive is the only
authority for the consonantal text.** You are adding vowels, translation, notes and glosses to
it; you are not re-reading the scan and not changing a letter. If a line looks wrong, leave it
and note it in `QUESTIONS.md` — correcting the archive is the transcription pipeline's job.

## 3. Segment

Cut the lines into sense units — sentences, not lines. A unit usually spans several archived
lines; keep the printed line's words in printed order and drop the line breaks. Where the archive
marks verse (`"v": true`), the sense unit is the verse block: set `"v": true`, keep the ` * `
hemistich separator, and put the line breaks back as `\n`. Do not flatten verse into prose.
Verse `t` is **copied from the archive as printed** — the edition points its verse, and that
pointing is final (`reading-conventions.md`, "Verse is copied, not vocalised").

Expect roughly 30–60 sense units for a night of ~120 archived lines.

## 4. Draft

Use the Agent tool, `general-purpose`, over **disjoint slices** of the sense units — ten or so
units each, four or five agents. Disjoint slices are what stop the glosses from diverging; the
pilot's overlapping drafters produced 61 conflicting entries and every one had to be swept.

Cut the slices on archived-line boundaries and record each slice's `--from` and `--to` refs
before you launch it: the check in 4a needs them.

Give every agent, in its prompt, the full text of `reading-conventions.md` and its own slice.
**Say in the prompt, in these words: "Verse lines are copied from the archive exactly as given,
marks and all; vocalise only verse words that arrive with no marks at all. Prose you vocalise
fully."** Never tell an agent to supply full tashkīl on its whole slice — on Night 8 that
instruction made every agent re-point printed verse.
Each returns, for each sense unit: `t` (vocalised prose; verse as printed), `tr`, `l`, `i` (omit
where the literal is already natural), `n` (only where genuinely useful), plus a glossary entry for every word form in
its slice. Have it write its result to a file (`/tmp/slice<N>.json`, sentences plus glossary)
rather than only into its reply — the file is what gets checked.

**Do not ask an agent to verify its own slice, and give no weight to a claim that it did.** On
Night 5 all five agents reported "verified mechanically, zero mismatches" and 1224 of 1798 tokens
were wrong: precomposed hamza is indistinguishable from the correct encoding to anyone reading
the text, model or human. Tell the agents the encoding rule; do not tell them to check it. The
check is yours, and it is a script:

### 4a. Check every slice by script, the moment it comes back

    python3 tools/check_slice.py /tmp/slice<N>.json --from <REF> --to <REF>

It runs the bare-strip identity on that slice alone against the archived lines. If it prints
`RESULT FAIL` with "mechanically repairable", run it again with `--fix`: it rewrites precomposed
hamza to the combining form wherever the edition prints the bare letter, puts the archive's own
spaces back where a drafter fused the stray `و` (or a line-break split) into its host word, joins
what a drafter split, and carries the same fixes into the slice's glossary keys. Anything it
cannot repair — a wrong, missing or extra word — it lists as `FAIL token N`. It also compares
every pointed verse word with the archive codepoint for codepoint (`FAIL ... verse word(s)
re-vocalised`); `--fix` puts the archive's word back and renames the matching glossary key.
A wrong, missing or extra word is a drafting
error, and you fix it by hand against the archive (never by re-reading the scan, never from
memory). Any glossary key it had to split is printed under `WARN`; rewrite those two meanings.

A slice goes into the night only after `check_slice.py` prints `RESULT PASS` on it. No
exceptions, and no "the agent said it was fine".

Then **one review agent over the whole night**: register consistency (the you/your rule, the
`al-` rule), glosses that disagree across slice boundaries, and a copyright echo check against
the two known traps in `reading-conventions.md`, and every glossary entry
that names a بِـ, لِـ or كَـ says what that prefix does in this night's sentence. It reports; you apply. It does **not** check
the hamza encoding — the script already has, and a reviewer will sooner or later recommend NFC
in good faith. The full-night gate in step 7 is the second, independent run of the same check.

## 5. The shared glossary

`nights-glossary.json` at the repository root, reached from the story by
`"glossaryFile": "nights-glossary.json"`.

**First publishing run only:** that file does not exist yet. Create it from the pilot's inline
421-entry glossary, then edit `nights-frame-01.json` to drop its inline `glossary` and carry
`glossaryFile` instead. This is the migration the corpus plan has been waiting on; do it as part
of the first night and say so in the LOG.

Merge your night's entries into it: add new keys, and **never overwrite an existing key with a
different meaning**. If an existing entry is actually wrong, fix it deliberately and say so in
the LOG.

## 6. Assemble

Write `nights-<NN>.json` (or `nights-frame-02.json`) at the repository root, with the metadata
`reading-conventions.md` specifies — `source`, `about`, `work`, `workEn`, `part`, `rtl`,
`script`, `trStyle`, `langCode`, `glossaryFile` — and `"audio": "audio/<id>"` (for example
`"audio": "audio/nights-03"`), placed after `trStyle` as in the published nights. Write the field
and nothing more: the repository's audio Action builds the clips and word timings by itself once
the story file lands on main (see `reading-conventions.md`, Audio). Never create or edit anything
under `audio/`.

Add the entry to `stories.json`, beside the other nights: `id`, `title`, `titleEn`, `language`,
`work`, `workEn`, `part`, `file`.

## 7. Gate

    python3 tools/validate_night.py ../../../nights-<NN>.json --from <start> --to <end>

must print `RESULT PASS`. It also checks that pointed verse is exactly as printed (repair: `check_slice.py
--fix`, as below). The check that matters most is the bare-strip identity: the vocalised text,
with the combining marks removed, must equal the archive token for token. If every slice passed
4a this should pass first time; a failure here means a slice was merged without its check, or an
edit after 4a introduced a precomposed hamza — fix the word (`check_slice.py --fix` works on the
assembled file too, with the night's own `--from`/`--to`). **Never run NFC over the file to make
it pass**; that breaks every Arabic text in the library.

`git diff --stat` must show only: the new story file, `stories.json`, `nights-glossary.json`, and
your own pipeline files (claim, LOG, plan). Never `reader.html`, never `index.html`, never
another work's files.

## 8. Publish

Commit `Nights: night <N> published` (or `Nights: frame, part 2 published`). Push to `main`; if
`main` moved, `git pull --rebase` and push again, up to three times; never force. Then delete the
claim, update `plan.md`'s phase 2 table, append the LOG line, commit and push.

Confirm it is live: the site serves `stories.json` and the new file from `main` within a minute
or two.

## 9. Record

`LOG.md`, one line, under 400 characters: UTC time · the unit · sense units · glossary entries
added · tokens · anything a person should know. `QUESTIONS.md` for any decision the rules did not
settle, with what you decided meanwhile. Nothing waits on the owner.

## What a publishing run never does

Publishes more than one night; merges a slice that `check_slice.py` has not passed; re-points
the edition's printed verse; takes an
agent's word that it checked its own text; changes a letter of the archive; touches `reader.html`,
`index.html`, audio, or another work's files; opens a modern translation of the Nights for
wording; runs NFC over an Arabic file; sends email; uses Google Drive; creates, changes or
disables a routine.
