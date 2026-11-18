# Reviewer brief — ani-125-address, pass 2

Same task and rules as pass 1: read chunks/REVIEW-BRIEF.md first (all of it applies), and the pass-1 logs
chunks/review-1.md and chunks/review-2.md (what was already changed or refused; do not reopen refused points unless
plainly wrong). The two halves have been merged and harmonised: lemma keys nm ("who?"), wḏb, ṯn (2pl dependent
pronoun) vs tn (fem. demonstrative), imny / iꜣby; house tr: the bolt O34 = z, the folded cloth S29 = s.
Your input: chunks/review2-in-<N>.json. Output: chunks/review2-out-<N>.json and chunks/review2-<N>.md (same format
as pass 1, counts by severity at the end).

New in pass 2 — the glossary. drafts/ani-125-address/gloss.json was written by a weaker model (Sonnet), which
invents modern forms and misnames grammar: check EVERY entry (top level and "__broaden__") for the lemmas used in
your half against the text and Egyptian grammar. Entries are "lemma — meaning (grammar)", general to the word, never
pinned to a line; names: meaning where transparent + "(Budge: X)". Broadened entries must keep the known entry whole
(see known-lemmas.json) + " · " + the new sense. Do NOT edit gloss.json (the other reviewer works in parallel): write
your corrections to chunks/gloss-fix-<N>.json as {lemma: full corrected entry} (use key "__broaden__" with a nested
object for broadened ones), and list them in your .md. Also check per-occurrence morph "gloss" overrides in your half.
Self-check as in pass 1.
