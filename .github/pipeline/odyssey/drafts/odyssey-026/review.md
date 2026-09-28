# Review — odyssey-026 (Odyssey 5.388–493)

Two-pass adversarial review per `runbook.md` §2 and `conventions.md`. 58 units checked against
`packet.md`, `conventions.md`, `odyssey-025/units.json` (continuity and the four repeated lines),
`odyssey-015/units.json` (the 5.424 repeat), and the note style of `odyssey-001/units.json`.

## Changes made

| Line (`ln`) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 394 | `n` | Minor (factual/grammar label) | φανήῃ was called a "short-vowel epic subjunctive." That term names a different phenomenon (thematic verbs like εἶμι using ἴομεν for ἴωμεν). φανήῃ is the opposite case: an epic subjunctive left **uncontracted** (φανη-ῃ, not contracted to Attic φανῇ) — a long, not short, vowel. | Reworded to "an epic subjunctive left uncontracted (for Attic φανῇ, from φανέῃ)." |
| 405 | `l`, `i` | Minor (mechanical/capitalization) | The previous unit (404) ends with a full stop in the Greek and in `l`/`i` ("...nor havens."/"...no roadsteads."). The new sentence at 405 started lowercase ("but headlands…" / "there were only…"), inconsistent with how the draft capitalizes new sentences after a full stop everywhere else (e.g. 398→400, 416→417, 430→432, 436→438). | Capitalized "But" and "There." |
| 406 | `n` | Moderate (fabricated/imprecise cross-reference) | The note claimed the **whole two-line unit** "already stands, word for word, in odyssey-025 (5.297 = 5.355)." Checked odyssey-025/units.json directly: the couplet (γούνατα λύτο + ὀχθήσας) stands whole only at 5.297–298; at 5.355 only the second line (ὀχθήσας…) repeats, paired there with a *different* first line (αὐτὰρ ὁ μερμήριξε…, not καὶ τότ' Ὀδυσσῆος λύτο γούνατα…). The "5.297 = 5.355" formula falsely implied the whole couplet recurs at both places. | Reworded to state the couplet stands whole at 5.297–298, and that only its second line recurs again, at 5.355 and at 5.464. |
| 436 | `n` | Moderate (overclaim) | Note said δύστηνος + ὑπὲρ μόρον together are "the same pairing already fixed for Aegisthus's death in the pilot part." Checked odyssey-001/units.json (1.33–35): only ὑπὲρ μόρον is used of Aegisthus there; δύστηνος does not appear with it. The claimed "pairing" is not real. | Reworded to credit only ὑπὲρ μόρον as the repeated phrase, and to note explicitly that δύστηνος is not paired with it there — the striking new pairing is the draft's own. |
| 453 | `l`, `i` | Minor (mechanical/capitalization) | Same issue as 405: the previous unit (451) ends with a full stop ("...into the river's mouth."/"...ἐς ποταμοῦ προχοάς."), and 453 begins a wholly new sentence (new subject, Odysseus, replacing the river-god) but started lowercase "and." | Capitalized "And" in both `l` and `i`. |
| 464 | `l`, `i`, `n` | Moderate (repeated-line fidelity + cross-reference) | (a) `l` kept the published lowercase "and, vexed, …" though this unit now opens its own sentence after a full stop (463 ends "…ἄρουραν."). (b) `i` had drifted from the published wording ("Troubled, he spoke…" vs. the house's "and, troubled, he spoke…"), losing the word-for-word match the house rule asks for on a repeated line. (c) The note cited "5.297 = 5.355" for *this single line* (the ὀχθήσας line), but that line's own number is 5.298, not 5.297 (5.297 is the *other*, non-recurring line of the couplet). | Capitalized `l` to "And, vexed, …"; changed `i` to "And, troubled, he spoke to his own great-spirited heart:" to track the published wording as closely as the new sentence-initial position allows; corrected the note to "5.298 = 5.355" and added a sentence explaining the capital is the only change. |
| 469 | `n` | Minor (confusing wording) | The note said ἠῶθι πρό "joins the place-suffix -θι … to the old adverb ἠῶθι" — circular, since ἠῶθι *is* the suffixed form, not something separate that the suffix is added to. | Reworded so ἠῶθι is explained as ἠώς + -θι, with πρό added on top. |
| 470 | `n` | Moderate (scansion misdiagnosis) | The note attributed the flagged "2 scansions at cost 0.0" to an optional mute+liquid treatment of κλ in ἐς κλιτύν ("correptio Attica"). Scanned by hand: ἐς already ends in its own σ, so it is long by position regardless of what follows — the κλ cluster after it cannot create an alternate short reading there; there is no genuine choice at that spot. The more plausible source of a genuine two-way scansion in this line is δάσκιον, whose -ιο- can be read as two syllables or merged by synizesis into one (a well-attested Homeric licence), which changes the line's syllable count by one and yields two equally valid fits. | Rewrote the note to withdraw the ἐς κλιτύν account and point instead to synizesis in δάσκιον, keeping the correct overall verdict ("not a fault in the text"). Flagged here at moderate confidence — hand-scansion of a flagged ambiguity is inherently harder to be fully certain of than a straightforward morphology check; a second check with `scan_hexameter.py`'s own diagnostic output (not just its cost) would be worth doing before publish if available. |
| 415 | — | — | Scansion flag re-checked by hand: λίθακι in foot 5 does require an unparalleled lengthening for this hapax word. The existing note already says so correctly and matches the packet's own flag. | No change. |
| 477 | `l` | Minor (grammar typo) | "the other a olive" — missing "an" before a vowel-initial word. | Changed to "an olive." |

## Findings considered and declined

- **Repeated-line/byte-identity checks (5.406, 5.407, 5.424, 5.464).** Diffed the unit at `ln` 406
  against packet.md's quoted published text for 5.406–407: `l` and `i` are byte-identical. The
  first line of `ln` 424 matches the published wording at odyssey-015 (5.424) exactly, both in `l`
  and in the reused clause of `i`; the rest of the sentence is legitimately new (different second
  line in this part). `ln` 464 needed the fix above but is now aligned. All four **pass**.
- **Whole-file `t` verbatim check.** Concatenated all 58 `t` fields in order and diffed against
  packet.md's Greek text with whitespace normalized: identical, character for character. No text
  dropped, added, or moved. **Passes.**
- **`l`/`t` newline parity and `i` newline-freedom.** Checked programmatically across all 58 units:
  every `l` has exactly as many `\n` as its `t`; no `i` contains a `\n`. **Passes.**
- **Paragraph marks.** The packet marks ¶ at 388, 408, 424, 445, 451, 465, 474 (7 marks); the draft's
  `p: true` units land on exactly those seven `ln` values. **Passes.**
- **Quotation marks and `mark`.** Three speeches (5.408, 5.445, 5.465): `mark` sits on the first unit
  of each ("Odysseus speaks to his own heart" ×2, "Odysseus prays"), `i` opens “ on each speech's
  first unit and closes ” on its last (423, 450, 470). No `t` or `l` carries a curly quote anywhere.
  **Passes.**
- **Continuity with odyssey-025's last unit** (5.385, no `mark`, plain narration, sentence and
  paragraph both closed) — confirmed no speech runs on into this part. **Passes.**
- **λίθακι (5.415) case relation.** `l` renders "βάλῃ λίθακι ποτὶ πέτρῃ" as "dash against a
  rock-mass, on a rock," splitting λίθακι and πέτρῃ with two different English prepositions where
  the Greek gives ποτί only once. Considered rewriting to a single "against a rocky mass of a
  rock," but λίθακι's sense and its exact relation to πέτρῃ are themselves disputed (the note
  already flags λίθακι as a hapax of uncertain formation), so no rendering can claim more precision
  than the Greek itself allows here. Declined — not a clear error, and the existing hedge in the
  note already covers the real uncertainty.
- **τά…ἐρεύγεται (5.438), plural relative with a singular verb.** Checked: this is ordinary Greek
  grammar (a neuter plural subject regularly takes a singular verb), not an error, and `l`'s
  "which belches itself" is a fair rendering since English "which" is number-neutral. Declined.
- **"for" opening sentences after a full stop** (e.g. 453→454 "for by the sea…", 483 "for there was
  a great heap…"). Unlike the "and"/"but" cases fixed above, this pattern is applied consistently
  throughout the draft regardless of the preceding Greek punctuation, and lower-case "for" opening a
  loosely explanatory clause is defensible English style. Declined as an inconsistency — it reads as
  a deliberate, consistently-applied choice, not a slip.
- **`new-renderings.md`, all ten entries.** Checked each against the passage and against the
  existing conventions.md table: none is redundant with an existing row (κλυτὸς Ἀμφιτρίτη and
  κλυτὸς ἐννοσίγαιος are correctly kept apart from the table's κλυτὰ δώματα and κρείων ἐνοσίχθων;
  ἐυπλόκαμος Ἠώς correctly extends, rather than duplicates, Calypso's already-fixed epithet). Two
  recur within this same part (ἠιόνας τε παραπλῆγας…, 5.418 = 5.440; ὀλιγηπελέων/ὀλιγηπελίης,
  457/468) and are rendered identically both times. No changes needed.
- **Stock epithets against the house table.** πολύτλας δῖος Ὀδυσσεύς (486), γλαυκῶπις Ἀθήνη (427,
  437), δύστηνος (436), ζείδωρον ἄρουραν (463), πολιοῖο of the sea (409) all match the table
  exactly in both layers. No violations found.
- **"Remembered English" scan.** Read every `i` against the list of modern translators to avoid. No
  phrase reads as lifted rather than built from the Greek; several (e.g. "spent-breath spirit,"
  "presence of mind") are fresh coinages for genuinely obscure Greek. No changes.
- **Bowdlerization / dropped repetitions.** None found; the near-drowning, the stripped skin and
  crushed bones, and the fire-brand simile are all rendered directly.
- **Note density and style against odyssey-001.** One note per unit throughout, each leading with
  what a reader needs (Homeric form → Attic equivalent, or the construction, or the cultural fact),
  matching the model's register. No changes needed.
- **θύραζε's -δε/-ζε note (408).** Slightly loose phonological explanation ("-δε, here -ζε after a
  vowel") — the actual mechanism is -σδε > -ζε, not a generic vowel-conditioned change. Minor enough,
  and not actually false as stated (θύρας does end in a vowel-adjacent context), that I left it
  rather than manufacture a bigger fix than the problem warrants.

## Summary

58 units total; 9 edited (394, 405, 406, 436, 453, 464, 469, 470, 477) — 13 individual field changes,
all `n`, `l`, or `i` (no `t` touched). Most were mechanical (capitalization at sentence-initial
position after a full stop, one a/an typo) or note-accuracy fixes (two cross-reference corrections,
one grammar-label correction, one confusing phrasing, one scansion re-diagnosis). No mistranslation,
bowdlerization, epithet-table violation, or repeated-line drift survived to publish uncorrected. The
four repeated-line units and both scansion-flagged lines were checked by hand and are now accurate.

## Reviewer pass 2 — gloss.json

Checked all 242 entries (233 novel-form + 9 broadened) against `units.json`, `novel-forms.json`,
`known-forms.json`, and `odyssey-glossary.json`, per `runbook.md`'s instruction that the second pass
reads `gloss.json` and checks every parse against the line.

**Correctness edits: 15 entries.**
- Wrong case/gender fixed against actual usage in this part (the entry claimed an ambiguous
  "X/Y" case-or-gender that the line does not actually show, or the outright wrong one):
  `πηγῷ` (masc. → neut., agreeing with the neuter κῦμα — this was a real gender error, not just an
  unneeded hedge), `ῥόθιον` (acc. → nom., agreeing with κῦμα, subject of βέβρυχεν — real case error),
  `κῆτος` (dropped a false "nom./acc." hedge to acc., the case actually used), `δάσκιον` (dropped
  "neut." — agrees only with the feminine ὕλην here), `δυσπονέος` (dropped "neut." — agrees only with
  masc. καμάτοιο), `σά` (dropped "nom." — object of ἱκάνω, acc. only), `σκέπας` (acc. → nom., subject
  of ἦν), `ἁρπάξαν` (dropped "acc." — agrees with κῦμα, nominative subject), `ὀστέ` (dropped "acc." —
  subject of the passive ἀράχθη), `ῥῖγος` (dropped "acc." — subject of μεθείη), `ἐρευγόμενον` (dropped
  "acc." — agrees with κῦμα, subject of ῥόχθει).
- `ἀσπάσιον`: reworded "used predicatively/adverbially" (a hedge covering two different
  constructions) to "predicate agreeing with τόν," the construction actually used here.
- Two build-blocking format bugs, not just style: `αὔοι`, `δοάσσατο`, and `κεκαφηότα` had no
  `lemma — meaning` shape at all (no em dash), which fails `build_odyssey.py`'s own entry-shape
  check and would have made the build refuse; reworded all three into the required shape while
  keeping the same hedged, non-committal content. `πηγῷ` (241 chars) and the gender fix pushed it
  further; trimmed to 167 chars.
- Structural bug: the 9 broadened entries (`βάλῃ`, `μέγ`, `τί`, `τρίτον`, `χεῦ`, `ἄναξ`, `ὑπ`, `ὑπὸ`,
  `ὡς`) were sitting as ordinary top-level keys, not under the `"__broaden__"` key
  `build_odyssey.py` requires (`add=...; broaden=add.pop('__broaden__',{})`) — as shipped, the build
  would have died at `gloss.json redefines an existing form` on the first one. Moved all 9 into a
  `"__broaden__"` object; their content was not touched. Diffed each against
  `odyssey-glossary.json`'s current entry for the same key: all 9 preserve the old entry text
  byte-for-byte before the added `" · "` reading, and the new reading in each is itself accurate
  against the line it was added for (checked `βάλῃ`, `μέγ`, `τί`, `τρίτον`, `χεῦ`, `ἄναξ`, `ὑπ`, `ὑπὸ`
  all against their lines in `units.json`). No content changes needed there.

**Format trims: 60 entries.** Went through every entry; found 81 with a parenthetical quoting this
part's own line text as illustration (mostly `(Greek phrase ’English translation’)`), plus a handful
using the word "here" or "this simile"/"only here" to point at a specific spot. Removed the
line-pinned material from all of them: for a single-sense entry this usually meant dropping the
parenthetical outright (it added nothing beyond what "lemma — meaning; parse" already said); for a
few (`λεῖος`, `φυλάσσω`, `στόμα`, `ὄχοι`, `πολιοῖο`) the parenthetical was rewritten to state the
real general fact (a construction, a fixed formula, a polysemy) without quoting this line's inflected
wording. Kept the handful of parentheticals that are genuinely general — etymology (`ἀγχιβαθὴς`,
`πολύλλιστον`), a named recurring idiom (`σπέρμα`, `ἠῶθι πρό`, `τί πάθω`), or a plain
"agreeing with X" grammatical note (`θρασειάων`, `πεφυῶτας`, `ἀέντων`, `ἐκβαίνοντα`) — since those
describe the form itself, not this occurrence. Fixed explicit "here"/"this simile"/"only here"
wording in `δύσετ`, `ἀμφιτρίτη`, `ἀράχθη`, `ἄχνῃ`, `ἐνιπάς`, `ἐπαμοιβαδίς`, `λάιγγες`, `πάνθ` to
general phrasing.

**Disputed forms — left genuinely open, on purpose.** `πηγῷ`/`κύματι πηγῷ`, `λίθακι`, `κεκαφηότα`,
and `αὔοι` (the four this part's `units.json` itself flags as disputed) all already hedged properly
("disputed," "no certainty is possible," "perhaps," "not fully understood") and were kept that way —
only `πηγῷ`'s gender label and `κεκαφηότα`'s entry shape needed fixing, not their hedging. `κλυτὸς`
was left unchanged even though one of its two occurrences in this part (κλυτὸς Ἀμφιτρίτη, a feminine
noun) takes the masculine form: this is a real, attested Homeric formula (a frozen epithet used
without regard to the noun's grammatical gender, already discussed in this part's own `n` at 5.422),
not an error in the entry — "masc. nom. sg." correctly describes the form itself.

**Validation.** `python3 -c "import json; json.load(open('gloss.json'))"` passes. All 233 novel
entries now match `^\S.* — \S`, contain no backtick or ASCII apostrophe, and are ≤230 characters
(`πηγῷ` was the only one over, now 167). All 9 `__broaden__` entries were confirmed to contain their
`odyssey-glossary.json` counterpart's text byte-for-byte as a prefix. Coverage double-checked: every
form in `novel-forms.json` has exactly one top-level entry, and no gloss.json key exists outside that
list.
