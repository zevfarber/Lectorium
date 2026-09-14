# Slovo pipeline — open questions

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
