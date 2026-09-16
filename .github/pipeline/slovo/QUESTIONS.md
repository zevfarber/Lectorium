# Slovo pipeline — open questions

## 2026-09-16 07:16 UTC — process note, not a text-in-doubt case: an agent prompt paraphrased the source text instead of quoting it, and the drafter caught and corrected it

When claiming part 5, I extracted and verified its text against `source-1800.txt`/`parts.json` myself first (clean match, as always). But when I then wrote the drafting sub-agent's prompt, I retyped the segment from memory/summary rather than pasting the verified extraction, and introduced real errors (wrong word forms, an invented sentence, a duplicated phrase not in the source). The drafter agent independently re-extracted part 5 from the authoritative `source-1800.txt` using the same opens/ends method as `validate_slovo.py`, noticed the mismatch, flagged it clearly, and used the correct source throughout — nothing wrong was drafted. `validate_slovo.py`'s gate 2 (concat `t` == source) would have caught this even if the drafter hadn't, since it re-derives the segment from `source-1800.txt` independently rather than trusting the prompt.

**Decided:** nothing needed correcting in the published output; this is a note for future runs. When delegating drafting to a sub-agent, paste the verified source segment as a file or exact quoted block (or better, tell the agent to extract it itself from `source-1800.txt` using `parts.json`'s `opens`/`ends`, as this run's later prompts did) rather than retyping it into the prompt text — retyping risks silent corruption that only the mechanical gate or an alert reviewer would catch.

## 2026-09-14 15:58 UTC — part 2 metadata in `parts.json` does not match its own text (run stopped, nothing drafted)

Step 1 of the runbook requires checking the extracted part's word count and sha256 against
`parts.json` before drafting, and stopping if they don't match. They don't match, for part 2 only.

**What I checked.** I extracted every part 0–10 the same way `validate_slovo.py` does: whitespace-
normalise `source-1800.txt`, find `opens`...`ends` for each part, and compare the resulting word
count / char count / sha256 against the recorded fields in `parts.json`.

- Parts 0, 1, 3, 4, 5, 6, 7, 8, 9, 10 all match exactly (words, chars, sha256) — confirmed against
  the file's only commit (171da3cd).
- Part 2 alone fails: word count matches (224 = 224), but the recorded `chars` is 1519 and the
  actual extracted segment is 1518 characters; the recorded `sha256`
  (`e281dc79c75a500f000b20561282e71c595d28849d97027ed7bc2cdb7a41dad5`) does not match the actual
  segment's sha256 under any of NFC/NFD/NFKC/NFKD normalisation (NFC/NFKC give
  `6694b3b5f75ffae16631f945bd549f9aeb384e2a02cd6ee69c66e96515088e12`, len 1518; NFD/NFKD give
  `907f52788a8439bbef4e17985625c13e5cd6a20c12f3dd8ec1832d183be25e74`, len 1520).

**What is *not* in doubt.** The `opens`/`ends` boundary strings for part 2 are each unique in the
source (found exactly once), and all eleven parts tile `source-1800.txt` exactly end-to-end with a
single space between each and nothing left over — I verified this by locating every part's start
and end offset and confirming the gaps are all a single space. So the segment part 2 actually
cuts out of the source is not ambiguous, and it is a plausible, coherent piece of the poem (opens
"Съ заранія въ пяткъ потопташа...", ends "...отъ тебе Яръ Туре Всеволоде." — matches the title
"The two days of battle" and plan.md's boundary description). This looks like a one-character
bookkeeping slip when `parts.json` was authored (171da3cd, the file's only commit), not a problem
with the source text or the cut points.

**What I decided:** nothing — this is a step-1 "text itself is in doubt" case, so per the runbook
I stopped rather than drafting from unverified text. I did not edit `parts.json`, `source-1800.txt`,
or anything else. No claim file was created (drafting never started). This run published nothing;
see the LOG.md line for 2026-09-14.

**Recommendation for whoever resolves this** (owner or a future run explicitly tasked with it,
not to be applied unilaterally by the next scheduled drafting run without re-deriving it
independently first): if a fresh independent extraction of part 2 by the same opens/ends method
again yields chars=1518 and sha256=`6694b3b5f75ffae16631f945bd549f9aeb384e2a02cd6ee69c66e96515088e12`,
correct those two fields for part 2 in `parts.json` to match, then re-run this pipeline normally.

*(Resolved by a later run, 2026-09-14 18:01 UTC: independently re-derived the same chars/sha256,
corrected `parts.json`, and published part 2 — see `LOG.md`.)*

## 2026-09-15 06:xx UTC — `validate_slovo.py` gate 3 required `p:true` on every part's first
sentence, which is false for parts 3–7 (fixed in this run, not a text-in-doubt case)

While gating part 3, the drafter/reviewer correctly followed `conventions.md`'s actual rule —
"`p: true` on the first unit of each source paragraph" — and put no `p:true` anywhere in part 3,
because part 3 does not open a new source paragraph.

**What I checked.** `source-1800.txt` has exactly 7 paragraphs (split on blank lines). Their
whitespace-normalised start offsets are `[0, 697, 3122, 3717, 14087, 15066, 16992]`. Cross-referencing
against every part's `[opens, ends)` span in `parts.json`: paragraph 4 (1648 words, offset 3717)
begins inside **part 2**, at its unit 6 ("Другаго дни велми рано...", which already correctly
carries `p:true` in the published `slovo-part2.json`), and runs with no blank line anywhere inside
it through the ends of parts 3, 4, 5, 6, **and** 7 (paragraph 4 ends exactly at part 7's `ends`
string, "...копіа поютъ на Дунаи."). So parts 3, 4, 5, 6 and 7 each sit entirely inside one already-
open paragraph and should carry **no** `p:true` at all — only parts 0, 1, 2, 8, 9, 10 open a fresh
paragraph. I verified this is exactly consistent with the `p:true` placement already published in
`slovo-proem.json`, `slovo-part1.json`, and `slovo-part2.json` (a corrected gate built from these
offsets reproduces their existing `p:true` placement exactly, with zero regressions).

But `validate_slovo.py`'s gate 3 read `sents[0].get('p') is True` unconditionally — true by
accident for parts 0–2 (each does open a fresh paragraph) but mechanically unsatisfiable, without
fabricating a paragraph break the source doesn't have, for parts 3 through 7.

**What I decided:** this is not a step-1 "text itself is in doubt" case — the extracted text, word
counts and checksums for part 3 all verified clean against `parts.json`. It is a tooling bug, so
per the "nothing waits on him" rule I fixed it rather than stopping the whole pipeline over it:
replaced gate 3 with a check that derives real paragraph-start offsets from `source-1800.txt`'s own
blank lines and requires `p:true` to mark exactly those offsets (no more, no fewer), in its own
dedicated commit, separate from part 3's publish commit — the same pattern as the part 2 metadata
fix above. Re-ran the new gate against all three already-published files first and confirmed zero
behavior change for anything already live before touching part 3. I did not touch `parts.json`,
`source-1800.txt`, or any published story file. This will also apply, unchanged, to parts 4–7 when
their turn comes — future runs should not need to revisit this.
