# Review C — odyssey-016, review-in-C.json (Odyssey 4.306–331)

Pass 1 (translation-focused). Reviewer role: adversarial check against conventions.md, packet.md,
and the four cross-referenced published parts (odyssey-001, -004, -005, -009). Twelve units
checked exhaustively per the review method in the task brief. `t` fields were never touched.

## Changes made

1. **Unit 0 (ln 306) · `l` · MAJOR (verbatim-reuse violation)**
   - Was: "up rose from his bed, good at the war-cry, Menelaus,"
   - Problem: the packet requires that, for the subject-swapped dawn-arming couplet (4.306/308,
     reusing odyssey-005 2.1–3), only the subject-specific words change — the shared portion must
     match verbatim. The shipped template reads "up rose from his bed Odysseus' dear son," with no
     comma between "bed" and the subject phrase. The draft inserted two commas around the new
     subject phrase, altering the supposedly-shared wording.
   - Fix: "up rose from his bed good at the war-cry Menelaus," — subject phrase now abuts "bed"
     exactly as the template does, with the epithet kept in Greek (adjective-then-name) order.

2. **Unit 0 (ln 306) · `n` · MAJOR (systematic augment mislabeling)**
   - Was: "ὤρνυτ’ is ὤρνυτο, an UNaugmented imperfect middle of ὄρνυμι, ... not an aorist."
   - Problem: ὤρνυτο is built with omega (ω), the regular temporal augment of an ο-initial stem
     (ὀρνυ- → ὠρνυ-, exactly parallel to ὀφείλω/ὤφειλον). The unaugmented form would be *ὄρνυτο*
     (short ο). The draft had the augmentation backwards — this is the exact "augmented form called
     unaugmented" error the review brief flagged as this project's recurring weak spot.
   - Fix: relabeled AUGMENTED, with the ὤφειλον parallel given. Also corrected the odyssey-005
     citation from "(2.1–2)" to "(2.1–3)" (the reused unit is three lines, not two — confirmed
     against odyssey-005.json ln 1, whose `t` runs 2.1–2.3) and "couplet" → "three-line passage".

3. **Unit 1 (ln 309) · `n` · Follow-on fix (consequence of #2)**
   - Was: "ἐδήσατο is an AUGMENTED aorist middle (contrast the unaugmented ὤρνυτ’ just above)."
   - Fix: removed the now-false contrast; both forms are augmented ("like ὤρνυτ’ just above"). The
     ἐδήσατο-is-augmented claim itself was correct and is kept.

4. **Unit 6 (ln 316, mark "Telemachus states his errand") · `n` · MAJOR (systematic augment
   mislabeling, second instance)**
   - Was: "ἤλυθον is an UNAUGMENTED aorist (= Attic ἦλθον, ...), not to be mistaken for an
     augmented form."
   - Problem: ἤλυθον carries the same lengthened η as ἦλθον (temporal augment on the ε-initial
     root ἐλθ-/ἐλυθ-); it is simply the epic by-form with an epenthetic -υ-, not an unaugmented
     variant. The project's own glossary entries for ἤλυθε/ἤλυθες/ἤλυθεν (checked directly) already
     equate them to ἦλθε/ἦλθες/ἦλθεν without ever calling them unaugmented, confirming the draft's
     claim was backwards.
   - Fix: relabeled AUGMENTED, with the mechanism spelled out. Trimmed the rest of the note (it had
     drifted to 121 words) back under 110.

5. **Unit 7 (ln 318) · `n` · MODERATE (cross-reference / line-number error)**
   - Was: "Line 320 repeats 1.90 word for word."
   - Problem: checked against odyssey-001.json directly — the unit cited begins at `ln` 90, but the
     matching line "μῆλ’ ἁδινὰ σφάζουσι καὶ εἰλίποδας ἕλικας βοῦς." is the third line of that unit,
     i.e. Odyssey 1.92, not 1.90.
   - Fix: "repeats 1.92 word for word."

6. **Unit 7 (ln 318) · `i` · MODERATE (repeated-line English not reused)**
   - Was: "...suitors of my mother, with their overweening insolence."
   - Problem: 4.321 is a byte-identical repeat of odyssey-004 1.368 ("μητρὸς ἐμῆς μνηστῆρες
     ὑπέρβιον ὕβριν ἔχοντες,"), confirmed against odyssey-004.json ln 368. Per the packet's own
     instruction ("reuse the published wording for that line as far as your sentence allows") and
     the house rule that a repeated line takes the same English every time, the already-shipped
     `i` for this clause is "you with your overbearing insolence" — "overbearing", not
     "overweening" (the draft's `l`, correctly, already used "overweening", matching the shipped
     `l`; only `i` had drifted).
   - Fix: "overweening" → "overbearing" in `i`, keeping the necessary and correct pronoun change
     (their/your) since here Telemachus speaks of the suitors rather than to them.

7. **Unit 9 (ln 325) · `n` · MINOR (self-contradiction)**
   - Was: "...the English already shipped for the identical Greek at 3.95 (odyssey-009)... περί...
     (though printed περί rather than πέρι here)..."
   - Problem: the note asserted the Greek was "identical" and then, one sentence later, admitted an
     accentual difference (odyssey-009 prints πέρι, anastrophe; this part's archive prints περὶ,
     confirmed against odyssey-009.json ln 95) — a direct self-contradiction. The English reuse
     itself is fine and unaffected.
   - Fix: "identical Greek" → "same recurring Greek formula", removing the contradiction while
     keeping the (correct) note of the accent difference that follows.

## Findings considered and NOT changed, with reasons

- **Segmentation splits at 314 (Greek `;`) and 325 (ano teleia)**: both checked against
  conventions.md's tap-unit rule and confirmed legitimate mid-line boundaries; `ln` is correctly
  set to the line each half-unit starts on (314 and 325 respectively) in both cases, not advanced
  to the next line. No change needed.
- **Quotation structure**: confirmed exactly one “ / ” pair (Menelaus's question, opens at unit 2 /
  ln 312, closes at unit 4 / ln 314) and one further un-closed “ (Telemachus's plea, opens at unit 6
  / ln 316). No closing ” appears anywhere after that, through the end of the file (checked by
  scanning every `l`/`i` for U+201D). The final unit's note states explicitly that the speech
  continues past this part into odyssey-017. This matches the brief's requirement exactly.
- **`t` fields**: checked word-for-word against the packet's own source block for 4.306–331 (concatenating unit by unit, including the two mid-line splits); reproduces the archive exactly,
  including the archive's own inconsistency of no comma after Ὀδυσσεὺς at line 328 (versus a comma
  in odyssey-009's printing of the "same" line) — since `t` must track this part's own archive
  exactly and was never touched, this is not an error in the draft.
- **House-table renderings**: βοὴν ἀγαθὸς Μενέλαος, θεῷ ἐναλίγκιος ἄντην, πεπνυμένος, the fixed
  vocative Ἀτρεΐδη Μενέλαε διοτρεφές ὄρχαμε λαῶν, μῆλ’ ἁδινά, εἰλίποδας ἕλικας βοῦς, Λακεδαίμονα
  δῖαν — all checked word-for-word against the conventions.md table and found exact matches (apart
  from the two fixes above).
- **Reused-line cross-references at 4.322–324 (odyssey-009 3.92–95) and 4.326–327 (odyssey-009
  3.96–97)**: checked byte-for-byte against odyssey-009.json directly; both `t` and both English
  layers are exact matches. No issue.
- **Reused-line cross-reference at 4.329–331 (odyssey-009 3.98–101)**: English layers (`l`/`i`)
  match odyssey-009 exactly, word for word — the note's "verbatim" claim is about the English, not
  the Greek, so the archive's own minor comma difference at 328 doesn't make the note wrong; left
  unchanged.
- **Reply-formula "already shipped three times... in odyssey-004"** (unit 5, ln 315): checked
  against odyssey-004.json — the formula does appear 3 times, but with τόν twice (388, 412) and τήν
  once (345); the note doesn't actually assert all three use τόν (re-read carefully: it just says
  "already shipped three times, with τόν," describing the current line's own pronoun rather than
  claiming uniformity) — on reflection this reads ambiguously but not falsely, and rewriting risked
  overcorrecting a note that a careful reading does not actually contradict the facts. Left as is;
  flagged here for the human owner's judgment call.
- **odyssey-014 / odyssey-015 closing-quote mechanics**, referenced in the final unit's note ("...
  exactly as odyssey-014's last open speech was closed only in odyssey-015"): verified that
  odyssey-014's speech is indeed left open with no closing ” at its last unit, and that
  odyssey-015's first unit ("ὣς φάτο...") is indeed the narrative close of that same speech — but
  neither file actually prints a closing ” character anywhere, so "closed" is true in narrative
  substance (via ὣς φάτο) but not literally typographic. This is a pre-existing property of two
  already-published files, outside this pass's scope to edit; flagged for the human owner as a
  possible upstream inconsistency, not fixed here.
- **δήμιον ἦ ἴδιον cross-reference to 3.82 (odyssey-009)**: checked against odyssey-009.json ln 82
  ("πρῆξις δ’ ἥδ’ ἰδίη, οὐ δήμιος, ἣν ἀγορεύω.") — exact match, line number correct. No change.
- Word counts, backticks, ASCII apostrophes, `l`↔`t` line-count parity, `p`/`v`/`ln` fields, and
  paragraph-start flags (¶ at 306, 312, 315) all checked programmatically across all 12 units — no
  further issues found.

## Summary of fix counts

- Major: 3 (unit 0 `l` verbatim-reuse comma insertion; unit 0 `n` augment mislabel; unit 6 `n`
  augment mislabel)
- Moderate: 2 (unit 7 `n` wrong line number; unit 7 `i` repeated-line English not reused)
- Minor: 2 (unit 1 `n` follow-on contrast fix; unit 9 `n` self-contradiction)
- Findings considered and refused: 5 (documented above)

## Most important thing for the next pass / human owner

Both augment-mislabeling errors were "wrote UNAUGMENTED where the form is actually AUGMENTED" —
the reverse of the more commonly-warned direction. Pass 2 (or a human) should specifically
re-verify every remaining past-tense verb claim in this slice by hand rather than trusting the
polarity the draft asserts; I found two real instances of exactly this failure mode (ὤρνυτ’, ἤλυθον)
in a file of only twelve units, both in notes that otherwise read confidently and cited real
parallels. I'd also flag the odyssey-014/015 closing-quote gap for the human owner's attention,
since it's a substantive-looking inconsistency in already-published material that this pass has no
mandate to fix.
