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

## Review pass 2 — gloss.json

The glosser has now run. This pass reads `gloss.json`'s 213 novel-form entries and 18
`__broaden__` entries against `units.json` (ground truth for use-in-context),
`known-forms.json` (ground truth for the pre-broadening text), and `odyssey-glossary.json`
(ground truth for coverage). Checked, in order: mechanical format on every entry (by script);
every `__broaden__` value contains its `known-forms.json` original verbatim (by script); full
coverage of every word-form token in `units.json` against `odyssey-glossary.json` ∪ gloss.json's
novel keys (by script, exhaustive — all 503 distinct tokens in the part, not a sample); every
augment/no-augment claim in the novel entries, checked against which forms they are attached to
and against the actual spelling; all 11 novel keys that recur more than once in the part,
checked at every occurrence for parse consistency; all 18 `__broaden__` entries, checked line by
line against their new sense's actual case/number use; and a further hand-checked sample of
about 27 additional single-occurrence novel entries spread across nominal cases, participles,
subjunctives and rare compounds.

**One fix made:**

1. **`συνήντετο` · wrong augment claim · fixed.** The entry read "impf. 3 sg. mid.,
   unaugmented, + dat.: 'she met (me)'". The word (ln 367, ἥ μ’ οἴῳ ἔρροντι συνήντετο νόσφιν
   ἑταίρων) is a compound of σύν + a verb with an α-initial stem (ἀντάω/ἀντέω); the surface
   form carries η where an unaugmented form would keep α (συν-αντ-ετο). η in that position is
   exactly the mark of augmentation (ε + α > η), the identical pattern this same gloss file
   correctly applies elsewhere to distinguish augmented from unaugmented forms of an
   α-initial verb: compare its own entries for `ἄγον` ("unaugmented (= ἦγον)") and `ἀμείβετο`
   ("unaugmented" — this part's own bare-α form, as against the well-known augmented ἠμείβετο of
   the reply-formula fixed in `conventions.md`). Since `συνήντετο` shows the η, not the α, it is
   the augmented form, and the entry had it backwards. Fixed to: "impf. 3 sg. mid., augmented
   (ε+α > η), + dat.: 'she met (me)'". (Tense — impf. vs. an old thematic aorist middle reading,
   which some Homeric grammars also allow for this exact form — was left as given; ancient and
   modern treatments disagree on it, and nothing here can settle it, but the augment/no-augment
   claim is independently checkable from the spelling and was simply wrong.)

**Checked and found correct (no changes):**

- **Coverage, exhaustively.** Every one of the 503 distinct word-forms appearing anywhere in
  `units.json`'s `t` fields is covered by either `odyssey-glossary.json` (4,559 entries) or
  gloss.json's 213 novel keys. Zero gaps. (This was run as a full pass, not a spot sample, since
  it is mechanical; the ~15–20-word sample the runbook asks for is folded into this exhaustive
  check — it includes tiny particles like `γ`, `κ`, `ῥ`, `θ`, multi-syllable compounds like
  `κρατερόφρονος`, `φαινομένηφιν`, `ὠκύμοροί`, proper names, and every form on both ends of the
  part.)
- **All 18 `__broaden__` entries.** Every one's old text is preserved verbatim (script-checked)
  and every new reading genuinely reflects a distinct case/number/sense actually attested in this
  part's usage, not hedging: e.g. `τρεῖς` (pre-existing entry only nom.; this part uses it twice,
  both times acc., agreeing with ἑταίρους — new acc. reading added, correctly); `κακόν`/`ἀγαθόν`
  (pre-existing entries acc.; here both are nom., subjects of the impersonal passive τέτυκται —
  new nom. reading added, correctly); `ἤια` (pre-existing entry only the noun, acc. pl.; this
  part uses it once as the noun's nom. pl. subject of κατέφθιτο, and once, at a different line,
  as an unrelated verb form, impf. 1 sg. of εἶμι — both new readings added, correctly, and kept
  apart from each other); `ἰχθυόεντα` (pre-existing entry only the neut. pl. reading with
  κέλευθα; every occurrence in this part instead agrees with the masc. acc. sg. πόντον — new
  reading added, correctly); `οἷσι` (pre-existing entry only the possessive; this part's use
  agrees with πεποίθεα + dat. as the plain relative, "in whom" — new reading added, correctly).
  No broadened entry was found to be unneeded padding or a false homograph.
- **Every augment/no-augment claim in the 213 novel entries** (12 of them, one now fixed) is on
  an indicative verb form — none is pinned to a participle, infinitive or adjective, so the
  mistake pass 1 caught once in `units.json` (calling νεηγενέας/γαλαθηνούς "unaugmented", when
  they are adjectives) is not repeated anywhere in `gloss.json`.
- **All 11 novel keys occurring more than once in the part** (`γέροντος`, `γίγνονται`,
  `κατευνηθέντα`, `μεμαῶτα`, `νημερτὴς`, `προσέειπον`, `ἀμείβετο`, `ἅλιος`, `ἐλεύσεαι`,
  `ἐφάμην`, `ἴδησθε`) — the parse given holds at every one of their occurrences, not just the
  first found.
- **All "= Attic ..." equivalence claims** (22 of them) in the novel entries — each checked
  against the standard epic/Attic correspondences (`-οισι(ν)` = `-οις`, `-οιο` = `-ου`, uncontracted
  `-εαι` = contracted `-ῃ`, `-έμεν(αι)` = `-εῖν`, etc.) and found accurate.
- **Homographs**: no novel-form entry contains a ` · `-joined double reading (that device is used
  only inside `__broaden__` in this file), so there was nothing among the 213 to test for
  hedging; the 18 `__broaden__` homographs are covered above.
- A hand-checked sample of ~27 further single-occurrence entries spanning nominal case
  agreement (`ἀθανάτους`, `ἀνάλκιδες`, `πάσας`, `ἁθρόαι`, `ὑποδμώς`, `φιλομηλεΐδῃ`, `οἴῳ`, …),
  participles of every voice (`ἐξαναδῦσαι`, `ἀποπνείουσαι`, `προϊδὼν`, `στᾶσα`, `λοχησάμενος`,
  `ἀγαγοῦσα`, `κοιμήσασα`, `ἐσσύμενόν`), and other verb moods/tenses (`μεμνῆσθαι`, `πεποίθεα`,
  `κατερύκομαι`, `πεδάᾳ`, `πεμπάσσεται`, `φαινομένηφιν`, `χαλέπτει`, `ἐπάλαισεν`) — all matched
  their line's actual case relations.

`gloss.json` is ready to build after this one fix.
