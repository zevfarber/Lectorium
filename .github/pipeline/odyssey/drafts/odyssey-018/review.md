# Review — odyssey-018 (Odyssey 4.435–537)

Two full passes made over `units.json` against `conventions.md`, `packet.md`, `new-renderings.md`,
odyssey-017.json (the still-open Menelaus narration this part continues) and odyssey-002.json /
odyssey-003.json (already-shipped repeated lines). `t` was never touched; all fixes are to `l`, `i`,
`n` or `mark`.

## Changes made

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| all (73 fields, ~50 units) | `l`/`i`/`n` | **Critical** | The entire draft used the ASCII apostrophe (U+0027) for every English gloss-quote and every possessive/contraction in every note, and for the possessives in `l`/`i` at 435, 445 and 536 — e.g. `'be'`, `Aegisthus's`, `odyssey-017's`. This is exactly the defect the review brief calls out by name ("no ... ASCII apostrophe/backtick anywhere in `l`/`i`/`n`"), it is a hard validator condition, and it is a direct break with the shipped style (odyssey-017's own notes use ‘ … ’ throughout, e.g. `χαλίφρων, ‘slack-minded, foolish’`). | Rewrote every gloss-quote as ‘ … ’ and every possessive/contraction apostrophe as ’ (U+2019), by script, checking afterward that no straight apostrophe or backtick remains anywhere in `l`, `i` or `n` and that no `t` field was touched. |
| 460 | `l` | Major | The note at this unit says ὀλοφώια is "the same substantival neuter plural already fixed at 4.410 (odyssey-017) ... reused here unchanged", but the house table (and odyssey-017's own shipped unit at 4.410) fixes `l` = "baneful wiles", `i` = "baneful tricks" — and this unit's `l` used "baneful tricks" in **both** layers, silently dropping the required `l`/`i` distinction and making the note's "reused here unchanged" claim false. | Changed `l` from "knowing baneful tricks" to "knowing baneful wiles"; `i` was already correct and untouched. |
| 441 (unit "ἔνθα κεν αἰνότατος…") | `n` | Major | Claimed αἰνῶς is "echoed ... in the next line", but the source (`ἔνθα κεν αἰνότατος λόχος ἔπλετο· τεῖρε γὰρ αἰνῶς`) shows αἰνῶς standing on line 441 itself, right after the ano teleia — the very same line as αἰνότατος, not line 442. | Reworded to "echoed by the adverb αἰνῶς later in the same line." |
| 441 (same unit) | `n` | Major | Cross-referenced λοχησάμενος to "4.462", but the word is printed on line 463 (`ὄφρα μ’ ἕλοις ἀέκοντα λοχησάμενος·`), not 462. | Changed the citation to "4.463". |
| 447 | `n` | Major | Cross-referenced ἦτορ ἑταίρων to "4.373 (odyssey-017)", but that phrase is printed on line 374 of that part (`εὑρέμεναι δύνασαι, μινύθει δέ τοι ἦτορ ἑταίρων.`); 373 is only the first line of that two-line unit. | Changed the citation to "4.374". |
| 466 | `n` | Minor | Quoted a two-line span from odyssey-017 (‘ἐνὶ νήσῳ ἐρύκεαι…μινύθει δέ τοι ἦτορ ἑταίρων’, lines 373–374) but cited only "4.373", against the pipeline's own practice of citing a range for a multi-line quote (cf. the table's "3.467–468" entry). | Changed the citation to "4.373–374". |
| 448 (unit "αἱ μὲν ἔπειτα…") | `n` | Major | Claimed παρὰ ῥηγμῖνι θαλάσσης "keeps the same English already used for this phrase at 4.430 (odyssey-017)". Checked odyssey-017's shipped unit at 4.430: its wording is "upon the surf-line of the sea", not "along the surf-line of the sea" as this draft has it — the note asserted an identity that does not exist between two genuinely different Greek prepositions (παρά vs ἐπί). | Reworded the note to say the English varies the preposition to match the Greek (παρά "along, beside" vs ἐπί "upon, at"), quoting the actual odyssey-017 wording rather than misdescribing it as identical. Left the translation itself unchanged, since the difference in wording is in fact the correct choice. |
| 497 | `n` | Major | Claimed παρῆσθα shows "the epic ending -σθα in place of Attic -ησθα". This is false on both counts: ἦσθα (2 sg. impf. of εἰμί) is the ordinary Attic form too — there is no separate "Attic -ησθα" — and the true epic-only phenomenon is the different ending -ῃσθα extending a subjunctive -ῃς (as in the note's own comparison word, ἐθέλῃσθα), which the note conflated with the plain imperfect ending. This is precisely the kind of false augment/tense/mood claim the review is warned to catch. | Rewrote the note: παρῆσθα = παρά- prefixed to ἦσθα, the ordinary (non-epic-only) imperfect of εἰμί, and distinguished it explicitly from the genuinely epic subjunctive ending -ῃσθα seen in ἐθέλῃσθα. |
| 450 | `n` | Minor | Called ζατρεφέας "a rare compound found only here" — a claim about the rest of the poem (corpus-wide hapax status) that this 103-line part cannot itself show, against the explicit note-writing rule ("a note asserts nothing about the rest of the poem that this part cannot show"). | Reworded to drop the unverifiable "found only here" claim, keeping only what this part supports (the transparent ζα- + τρέφω formation). |
| 441 (unit "τεῖρε γὰρ αἰνῶς…") | `n` | Minor | Same problem for ἁλιοτρεφέων: "the word is otherwise unattested in Homer" is a corpus-wide claim this part cannot verify. | Reworded to "unattested in this part" instead of "in Homer". |
| 485 | `mark` | Minor | Labelled Menelaus's second recalled answer to Proteus in this part as "his **third** answer to Proteus"; only one earlier marked answer to Proteus exists in this part (465, itself unlabeled/first, on the same unlabeled-then-"second" pattern odyssey-017 uses for Eidothea at 376/395). | Changed the mark to "Menelaus recalls his second answer to Proteus". |

## Verified correct (no change needed)

- **Tiling**: wrote a script joining all 69 units' `t` values in order (respecting `ln`/paragraph
  structure) and walked it against `source/odyssey-murray1919.json` book 4 lines 435–537 line by
  line; every unit starts exactly where its `ln` says, every line is reproduced with no character
  dropped, added or moved, and the file ends exactly at the end of line 537.
- **`p` flags**: all 9 (435, 462, 464, 471, 481, 485, 491, 499, 512) match Murray's paragraph marks
  in the packet exactly; none missing, none extra.
- **The load-bearing repeats (item 8 of the brief)**: line 464's `l`/`i` are byte-for-byte identical
  to odyssey-017's unit at line 375, and its note honestly explains the gender mismatch (μιν/ἔφατο
  being grammatically neutral) rather than hiding it. Line 468's whole unit is byte-for-byte
  identical to odyssey-017's unit at line 379 (including the closing ’). Line 486 is byte-for-byte
  identical, in `l` and `i`, to odyssey-002's shipped unit at line 169 (the `t`, correctly, differs
  only in trailing punctuation — comma here vs ano teleia there — matching the actual source text at
  each location, which the packet's own quoted line 486 already shows ending in a comma). Lines 471
  and 491 have word-for-word identical `l` and `i`.
- **τετληότι θυμῷ** (447, 459) gets the same English both times in both layers ("with enduring
  heart" / "with enduring hearts"), as does every other in-part verbatim repeat checked: μέγ’ ἀάσθη
  (503, 509 — "greatly blinded" / "a great blindness of mind"), δολίης/δολίην τέχνης/τέχνην (455,
  529), ὣς ἐφάμην, ὁ δέ μ’ αὐτίκ’ ἀμειβόμενος προσέειπεν· (471, 491), and the new-renderings.md
  entries for ζατρεφέας, ἁλιοτρεφέων, Γυρῇσιν/Γυραίην and δολιχηρέτμοισι.
- **Quotation-mark scheme**: “ ” is used, correctly, only for Proteus's three speeches (462, 472,
  492), each opening on the actual first unit of the speech (never on the reply-formula narration
  line before it); ‘ ’ is used only for Menelaus's own three recalled replies (465, 485, and the
  already-open one continuing from odyssey-017); every open has a matching close on the correct unit
  except Proteus's third speech, which is correctly left open with no ” anywhere after line 492, and
  the last unit's note explains why. This mirrors the dominant pattern at odyssey-017 lines 383 and
  399 (Eidothea's later two speeches, both “ ”), not the single-quote anomaly at odyssey-017's very
  first Eidothea speech (371) — see "Considered and refused" below.
- Spot-checked roughly two dozen other cross-references (1.13–15, 1.14, 1.48, 1.52, 1.65–67, 1.79,
  3.4, 4.156, 4.391, odyssey-003's line 235) against the actual source/shipped text; all correct.
- Word-by-word Greek → `l` → `i` check across the whole part turned up no other false case, tense,
  mood or augment label, no other line-position error, no note contradicting its own `l`/`i`, and no
  phrasing that reads as a lifted modern translation (none of the banned translators' names or
  characteristic phrases — e.g. "wine-dark sea" — appear; the draft correctly uses the house
  "wine-faced open-sea" instead).
- Note lengths: all fall inside the 25–110 word band; none is under 20 or over 130.
- No note names a modern translator.

## Considered and refused

- **The Eidothea/Proteus quotation-mark precedent.** odyssey-017's very first Eidothea speech (371)
  actually opens with ‘ ’ (single), not “ ” — an apparent inconsistency with her later two speeches
  (383, 399), which do use “ ”, and with the review brief's own description of the precedent. I did
  not make odyssey-018 imitate the single-quote anomaly for Proteus's first speech: the stated rule
  ("“ opens a distinct new speaker's speech"), the dominant practice in odyssey-017 itself, and
  odyssey-018's own new-renderings.md judgment call all agree that a different character gets “ ”.
  The anomaly is inside already-published odyssey-017 and out of scope to touch; odyssey-018's choice
  to use “ ” consistently for Proteus is the correct one, not an error to fix.
- **ἔνεικε's augment (435).** The note hedges "whether this form has lost an original augment is
  uncertain, so no claim is made either way." ἔνεικε is in fact the standard unaugmented epic aorist
  of φέρω (parallel to the augmented ἤνεικα), so the hedge is more cautious than it needs to be — but
  it asserts nothing false, so it was left alone.
- **ζατρεφέας/ἁλιοτρεφέων corpus-frequency claims.** I could not independently re-verify, from
  inside this sandboxed environment, whether either compound recurs elsewhere in Homer. Rather than
  guess at a specific correction, I treated both "found only here" / "otherwise unattested in Homer"
  claims as violations of the note-writing rule itself (a note may assert nothing about the rest of
  the poem that this one part cannot show) regardless of whether they happen to be true, and softened
  both to what this part alone supports.
- **βάλλομεν rendered "our hands we threw" with an implied "him" (454).** The Greek has no explicit
  object; English needs one for sense. This is ordinary translational supplementation, not an added
  or dropped word in the sense the sole-source rule cares about (which is about `t`), so it was not
  flagged.
- **ὄρος rendered "mountain" in `l` but "headland" in `i` (514).** This is the expected `l`/`i`
  divergence (literal Greek sense vs. natural English sense for the well-known Cape Malea), not an
  inconsistency to fix.
- **μεγάλ(α) glossed "loudly, clearly" and rendered "heard him ... plainly" in `i` (505).** Checked
  against the Homeric idiom κλύειν μέγα ("hear well/clearly", not necessarily "loudly" in volume);
  the note's dual gloss and the `i` rendering are a defensible reading, not an error.
- **κατέπεφνεν described as "an old reduplicated aorist" (534).** Checked against Monro's account of
  the πέφνον-type root aorist; the description is standard and correct.

## Not checked exhaustively

Given the size of the draft, the glossary file (`gloss.json`) was not produced yet at review time and
so was not cross-checked here (the runbook has the reviewer's second pass read `gloss.json` once the
glosser has run). Scansion is listed as "none" flagged in the packet; no hand-scansion was needed.
