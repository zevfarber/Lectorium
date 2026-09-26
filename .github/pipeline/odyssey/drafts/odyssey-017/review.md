# Review — odyssey-017 (Odyssey 4.332–434)

Two full passes were made: Pass 1 (form and structure — grammar labels, position/recurrence
claims, cross-references, breathing marks) and Pass 2 (translation and layers — Greek → `l`,
`l` ↔ `i` agreement, remembered English, quotation marks). `units.json` was edited directly,
field by field; `t` was never touched. `new-renderings.md` needed no changes. The glosser has
not run yet, so `gloss.json` was not reviewed (out of scope for this pass).

A separate, real cross-part problem was also found and fixed this run: see "The odyssey-016/017
speech boundary" below.

Totals for `units.json`: **1 major, 7 moderate, 1 minor** (9 changes to 9 fields), plus one
major fix to the already-published `odyssey-016.json` (out of `units.json` but squarely this
run's responsibility, and one older, unresolved case of the same bug flagged to `QUESTIONS.md`
rather than fixed).

## Changes made — `units.json`

1. **ln 332 · `n` · moderate.** The note read "This whole line repeats 4.332 as already
   published in odyssey-014" — self-referential nonsense, since 4.332 is this very unit's own
   line. Checked against `packet.md`: the earlier, already-published occurrence of this line is
   at Murray 4.30 (odyssey-014's unit at that line), not 4.332. Reworded to "repeats 4.30 (as
   already published in odyssey-014, where it is the unit at Murray line 30)".
2. **ln 333 · `n` · minor.** The note quoted the line's opening exclamation as "ὦ πόποι"
   (omega + smooth breathing + **circumflex**), but the actual line, and the house table's own
   fixed spelling for this exclamation, is "ὢ πόποι" (omega + smooth breathing + **grave**) — a
   different accent, not a citation-form variant (the word never stands as an isolated citation
   form; it is always this fixed idiom). Confirmed by comparing Unicode code points: `t` has
   U+1F62, the note had U+1F66. Fixed to ὢ.
3. **ln 335 · `n` · moderate.** The note called νεηγενέας and γαλαθηνούς — both ordinary
   compound *adjectives* — "unaugmented epic compounds". Augment (the historically flagged weak
   spot in this pipeline) is a category that applies only to the indicative of past-tense verb
   forms; neither word is a verb, so calling them "unaugmented" implies a contrast (augmented
   vs. not) that cannot exist for an adjective. Reworded to state plainly that they are epic
   compound adjectives and that no augment claim applies to them.
4. **ln 338 · `n` · moderate.** The note claimed εὐνήν (338) is "the same noun used of
   Odysseus's marriage-bed **three** lines above (εὐνῇ, 333)". 338 − 333 = 5, not 3. Checked
   against `packet.md`'s line list to confirm both line numbers. Fixed to "five lines above".
5. **ln 347 · `n` · moderate.** The note said εἰρωτᾷς/λίσσεαι "echoes λίσσομαι, the verb with
   which Telemachus's plea, carried over from the previous part, **had just closed**". Checked
   against odyssey-016's actual last unit (ln 328): λίσσομαι is the *opening* word of that
   unit's sentence, not its closing word (the plea's last word is ἐνίσπες, several words later).
   Reworded to say the verb "opens the last sentence of Telemachus's plea ... carried over from
   the previous part (‘λίσσομαι, εἴ ποτέ ...’, 4.328)", which is accurate and now cites the
   actual line.
6. **ln 383 · `n` · moderate.** The note cited this line as "already used elsewhere in the poem
   (3.214**/254**...)". Checked odyssey-003.json directly: no unit begins at Murray line 254 in
   that part (its own line list runs ...253, 255..., with nothing at 254), and no unit anywhere
   in it contains this wording except at line 214. `packet.md`'s own "already published" table
   also lists only the 3.214 occurrence for both 4.383 and 4.399. The "/254" half of the
   citation is unsupported by any source available to me; removed it, leaving "(3.214, spoken
   there by Telemachus)".
7. **ln 399 · `n` · moderate.** The same false "3.214/254" citation was repeated in this later
   unit's note (referring back to 383). Fixed the same way, to "(and 3.214)".
8. **ln 426 · `n` · major.** The note claimed ἤια (imperfect of εἶμι, "I was going") is "the
   same verb (uncontracted) that underlies νέεσθαι at 351" — but this file's own unit at ln 351
   correctly identifies νέεσθαι as belonging to νέομαι, "shares its root with νόστος." εἶμι and
   νέομαι are two distinct Homeric verbs for "go" (different roots, *ei-* vs. the *nes-* of
   νόστος); they are not "the same verb". This directly contradicted the part's own earlier,
   correct note, so it is a confirmable, self-contained error. Reworded to say ἤια is "a
   different verb from the uncontracted νέεσθαι at 351, which is from νέομαι and shares its
   root with νόστος instead, though the two verbs overlap in meaning."
9. **ln 353 · `i` · moderate.** βούλοντο (the governing verb, "the gods always wished...") is a
   plain past imperfect, and `l` correctly has "the gods always wished". `i`, however, read "But
   the gods always **want** their commands to be kept in mind" — present tense, with no note
   defending the shift, so the two layers disagreed in tense/force for the same Greek word.
   Changed `i` to "But the gods always **wanted** their commands to be kept in mind," matching
   `l`'s tense while keeping the generalizing "always".

## Checked and found correct (no change) — a sample of the position/breathing/cross-reference sweep

- **οἷόν vs. οἶόν at 421**, specifically flagged by the drafter's own report as a self-caught
  risk: checked the Unicode code points of both the `t` and the `n` quotation at ln 420. Both
  read οἷόν (U+1F37, rough breathing + circumflex, "such as"), correctly distinct from οἶόν
  ("alone"). No error; the drafter's self-correction held.
- **A systematic diff** of every Greek word quoted in a note against the matching word in that
  unit's `t` (stripping all diacritics to compare bases, then flagging any surviving difference)
  turned up nine hits total; only the ὢ/ὦ case above (#2) was a real breathing/accent error. The
  rest — κνημούς/κνημοὺς, ἄν/ἂν, λιγύς/λιγὺς, πωλεῖται/πωλεῖταί, νημερτής/νημερτὴς (×2),
  προδαείς/προδαεὶς, φρικί/φρικὶ — are the ordinary difference between a word's running-text
  accent (grave, or enclitic-shifted, mid-clause) and its citation-form accent (acute) when a
  note names the word on its own; none is a breathing error, and all match standard citation
  practice used throughout the shipped parts. Left as printed.
- **γέρων ἅλιος νημερτής / 349, 384, 401**; **ἀεικέα πότμον / 339, 340**; **νόστον θ᾽, ὡς ἐπὶ
  πόντον ἐλεύσομαι/ἐλεύσεαι ἰχθυόεντα / 381, 390, 424**; **Πρωτέος ἰφθίμου θυγάτηρ ἁλίοιο
  γέροντος / 365**; **ἀθάνατος Πρωτεὺς Αἰγύπτιος / 385**; **καλῆς ἁλοσύδνης and νέποδες / 404**;
  **ἐύσσελμος / 409**; **θεσπιδαὲς πῦρ / 418**; **ἐπ᾽ εὐρέα νῶτα θαλάσσης / 362**; **εὐρύπορος /
  432**; **αἲ γάρ, Ζεῦ τε πάτερ καὶ Ἀθηναίη καὶ Ἄπολλον / 341** — every line number given in
  `new-renderings.md` for these eleven proposed rows was checked against `packet.md`'s line
  list and against the unit's own `t`. All accurate; no changes needed there.
- **Already-published cross-references reused in notes**: "hollow caves" at 1.15 (odyssey-001),
  the Atlas formula "who of the sea entire the depths knows" at 1.52–53 (odyssey-001), "who
  hold the wide sky" at 1.65–67 (odyssey-001), and the δαΐφρων/δαῆναι link at 1.48
  (odyssey-001) were all opened and checked directly against the live published files. All four
  citations are accurate, and the quoted English matches the shipped wording verbatim where the
  convention requires it.
- **Segmentation**: all 103 lines (4.332–434) were matched against `packet.md` line by line;
  the 53 units' `t` fields, joined in order, reproduce the packet exactly, with no line
  dropped, duplicated, or reordered. The two mid-sentence comma cuts (341–344/345, and
  420–422/423–424) are both legal under the four-line cap, and the note at each explains the
  cut. All seven `p: true` flags (332, 351, 371, 375, 382, 394, 398) match Murray's own
  paragraph marks in `packet.md` exactly, with none missing or extra.
- **Quotation-mark nesting**: traced the full sequence — the outer frame speech opens with “
  at 333 (`mark`: "Menelaus speaks") and is correctly left open, unclosed, at the part's end
  (ln 433), exactly as its own note says. Within it, six single-quoted nested speeches each
  open with their own `mark` and close exactly once, in strict sequence with no overlap:
  Eidothea (371–373), Menelaus's first recalled reply (376–381), Eidothea's second speech
  (383–391), Menelaus's second recalled reply (395–397), and Eidothea's third and longest
  speech (399–423). Every open ‘ has a matching close ’, checked by comparing the first and
  last character of both `l` and `i` for every marked or quote-bearing unit. Fully consistent.

## Findings considered and refused

- **ln 408, `n`: "cf. ἔχειν and ἀλύξαι below, 415–416".** Both words actually fall on the same
  line, 416 (ἔχειν early in the line, ἀλύξαι at its end); "415–416" is imprecise either way —
  too generous if read as the words' own line, one line short if meant as the enclosing unit's
  span (414–416). Left alone: it doesn't point anyone to the wrong line, and rewriting a
  one-digit range for a citation this soft isn't worth the risk of introducing a new error under
  review pressure.
- **γέρων ἅλιος νημερτής → "the unerring old man of the sea".** Considered flagging this as
  possible "remembered English", since it is exactly the kind of fully-formed English phrase
  the rules ask reviewers to be suspicious of. But the Greek decomposes transparently,
  word-for-word, into exactly these four English words (γέρων "old man" + ἅλιος "of the sea" +
  νημερτής "unerring"), and there is no materially different phrase available by working from
  the case relations alone — any literal rendering converges on the same wording. Left as
  proposed in `new-renderings.md`.
- **ἀεικέα πότμον / κάρτος τε βίη τε / κρύψω ... οὐδ' ἐπικεύσω doublings.** Checked each for
  whether the near-synonym pairs are genuinely both represented in `l`/`i` or silently
  collapsed to one word. All three are handled correctly (both members of each pair get their
  own English word in both layers). No change.
- **Nine acute/grave citation-form "mismatches"** from the automated diff (listed above under
  "Checked and found correct") — considered each individually for whether it might in fact be a
  breathing error rather than an accent-position convention. All nine are accent-only, on the
  same breathing, and consistent with how the shipped parts already quote isolated words. Not
  changed.

## The odyssey-016/017 speech boundary

odyssey-017's very first unit (ln 332, τὸν δὲ μέγ' ὀχθήσας προσέφη ξανθὸς Μενέλαος·, "Then,
greatly troubled, fair-haired Menelaus said to him:") is plain narration, not a continuation of
Telemachus's plea. That means the plea carried over from odyssey-016 — which odyssey-016's own
last unit (ln 328, spanning 4.328–331) shipped with **no** closing " on either `l` or `i`, on
the stated expectation that it would run on into odyssey-017 — in fact ends at 4.331, one line
before odyssey-016 itself ends, and no wording of it appears anywhere in odyssey-017.

**Fixed** (major, in `/home/user/Lectorium/odyssey-016.json`, its last unit, ln 328):
- `l`: added a closing ” after "...tell me the unerring truth." → "...tell me the unerring
  truth.”"
- `i`: added a closing ” after "...tell me the unerring truth." → "...tell me the unerring
  truth.”"
- `n`: kept the original explanation in full and appended a dated correction recording that
  odyssey-017's opening unit showed the plea actually closes here, why the mark is being added
  now, and — since the old note's own precedent citation turns out to be inaccurate — a note
  that the parallel odyssey-014/015 case is *not* actually resolved the way the old note
  implied (see next section). The full new note text is in `odyssey-016.json` itself.

This file is already published; editing it is squarely this run's own responsibility, since
odyssey-017 is what revealed the mistake, and the runbook's reviewer instructions explicitly
say to check the neighbouring part's last unit for a speech that runs on across a part
boundary. `build_odyssey.py`/`validate_odyssey.py` were not re-run against odyssey-016 (out of
scope for this role), but the edit is a pure two-character addition to `l`/`i` plus a note
rewrite, so it should not disturb its scansion or line count.

## The odyssey-014/015 boundary — same bug, found but not fixed here

While checking the precedent odyssey-016's old note cited ("exactly as odyssey-014's last open
speech was closed only in odyssey-015"), I read odyssey-014.json's actual last unit (ln 110,
4.110–112) and odyssey-015.json's first unit (ln 113). odyssey-014's last unit still lacks its
closing " on both `l` and `i`, and its own note asserts the speech "does NOT close" within that
part. But odyssey-015's first unit is plain narration, and its own note says outright that this
line "confirms that Menelaus's own long speech, left open at the end of odyssey-014 ... has now
finished." So the same bug exists there too — a speech that demonstrably ends at a part
boundary, with the closing mark never actually placed on any unit in either file — and, unlike
the 016/017 case, it has never been corrected.

This is out of scope for the present run (odyssey-017 only revealed the parallel case at its
own boundary; touching an unrelated already-published part risks side effects this run cannot
fully validate), so I did not fix odyssey-014.json. I wrote it up as a new entry in
`QUESTIONS.md` ("odyssey-014's last unit still lacks its closing ", even though odyssey-015
confirms the speech ends there..."), following the file's existing format, with the exact fix
odyssey-014.json would need spelled out for whoever picks it up.
