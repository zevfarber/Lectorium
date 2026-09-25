# Review — odyssey-014 (Odyssey 4.1–112), pass 1 (translation)

Reviewed against `conventions.md`, `packet.md`, `novel-forms.json`/`known-forms.json`, and the last
unit of the previously published `odyssey-013.json`. Two full passes were made over `units.json`
(re-read fresh for the second pass); all fixes below were applied in place. `t` fields were never
touched.

Units are referenced by array index and by their `ln` (starting line number).

## Changes made

### Augment mislabelling (the recurring class of error this project is warned about)

Fourteen notes called a form "unaugmented" when the spelling itself shows the augment — either a
plain ἐ- prefix on a consonant-initial root, a compound preposition's final vowel elided before the
augment (revealing it), or the tell-tale α→η / ο→ω lengthening. Two further notes called a **present**
tense form "unaugmented," a category error since augment applies only to past indicative forms.

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 3 (ln 6) | n | error | ὑπέσχετο called "unaugmented" — ὑπο- has elided its final vowel before the augment (ὑπ-έ-σχετο); the augmented compound is exactly what the spelling shows | reworded to "augmented," with the elision explained |
| 3 (ln 6) | n | error | ἐξετέλειον called "unaugmented" — ἐκ- only becomes ἐξ- before a vowel, and the root τελε- starts with a consonant, so the ε after ξ can only be the augment | reworded to "augmented" |
| 5 (ln 10) | n | error | ἤγετο called "unaugmented" — ἄγω's root is α-initial; augment lengthens α→η, and the text has η (ἤγετο), not α | reworded to "augmented" |
| 6 (ln 12) | n | error | ἔφαινον called "unaugmented" — φαίνω's root is consonant-initial (φ); the bare ἐ- prefix in the text is the augment, unambiguously | reworded to "augmented" |
| 6 (ln 12) | n | error | ἐγείνατο called "unaugmented" — same test, root γειν- is consonant-initial; ἐ- is the augment | reworded to "augmented" |
| 8 (ln 17) | n | error | ἐμέλπετο called "unaugmented" — root μελπ- is consonant-initial; ἐ- is the augment | reworded to "augmented" |
| 8 (ln 17) | n | error | ἐδίνευον called "unaugmented" — root δινευ- is consonant-initial; ἐ- is the augment | reworded to "augmented" |
| 18 (ln 37) | n | error | διέσσυτο called "unaugmented" — δια- has elided its α before the augment (δι-έσσυτο, with the compensatory geminate σσ of augmented ἔσσυτο) | reworded to "augmented"; also clarified that κέκλετο (correctly called unaugmented) is unaugmented because it is a *reduplicated* root aorist, not because the augment is simply missing |
| 20 (ln 43) | n | error | εἰσῆγον called "unaugmented" — ἄγω's root again; α→η shows the augment (εἰσῆγον, not εἰσάγον) | reworded to "augmented" |
| 35 (ln 68) | n | error | προσεφώνεε called "unaugmented" — root φων- is consonant-initial; the extra ε-syllable after προσ- is the augment | reworded to "augmented" |
| 43 (ln 81) | n | error | ἠγαγόμην and ἦλθον both called "unaugmented" — both show η (the augment grade) where the unaugmented Homeric forms would show α (ἄγαγον) and ε (ἔλθον) respectively | reworded to "augmented," both explained together |
| 47 (ln 90) | n | error | ἠλώμην called "unaugmented" — ἀλάομαι's root is α-initial; augment lengthens to η, and the text has η | reworded to "augmented" |
| 54 (ln 107) | n | error | ἔμελλεν called "unaugmented" — root μελλ- is consonant-initial; ἐ- is the augment | reworded to "augmented" |
| 46 (ln 87) | n | moderate | παρέχουσιν (present indicative) called "an unaugmented present" — present-tense forms are never augmented or unaugmented; the category doesn't apply | reworded to state plainly it is present tense, dropping the augment language |
| 55 (ln 110) | n | moderate | ὀδύρονται (present indicative) called "an unaugmented present" — same category error | reworded to state plainly it is present tense |

Sanity check on the fixes: ἀπώλεσα at unit 49 (ln 94) was already correctly called "an ordinary
augmented aorist" (ο→ω lengthening, ἀπώλεσα not ἀπόλεσα) — that one confirms the drafter does know
the test in principle, which makes the volume of the above mislabellings look like a real, systematic
lapse rather than a one-off slip. All other "unaugmented" claims in the file were checked by hand
against the specific word as it stands in the line and found correct: ἷξον, ἔλων, εὗρον, πέμπεν,
ἄνασσεν, δαίνυντο, ἴδετο, κέκλετο, θαύμαζον, πέλεν, ἕζοντο, τίθει, πάρθεσαν (apocope, not augment —
see below), λοῦσαν/χρῖσαν, ἴαλλον, ξύνετο, ἱκόμεθ’/ἱκόμην/ἱκόμην, πάθον. (ἰδόντες, a participle, can
never carry augment either way; left as is.)

### Cross-reference errors

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 11 (ln 26) | n | major | Cited "διοτρεφής... already given to kings collectively (4.63)" — but 4.63 comes *after* 4.26 in this same part, so it cannot be "already given." The true house-fixed source is `διοτρεφέες βασιλῆες (3.480)` in conventions.md's table (an earlier, already-shipped part) | reworded to cite the real fixed source, 3.480, and to describe 4.63 correctly as a later recurrence within this part |
| 21 (ln 43) | n | major | Same error repeated: "διοτρεφέων βασιλήων already fixed at 4.63" — again citing a line that comes later in the same part as if it were the precedent | corrected the same way, citing 3.480 as the fix and 4.63 as a later recurrence |
| 22 (ln 45) | n | moderate | Cited "already fixed earlier in this part (4.15–16, 4.46)" for ὑψερεφές/Μενελάου κυδαλίμοιο — but 4.46 *is* the very line this note is annotating, not a separate earlier citation | dropped the self-referential "4.46" from the citation list |
| 33 (ln 65) | n | major | Claimed the "so he spoke" formula "stands with an ano teleia by itself" at "1.42–43 in the pilot part" — checked odyssey-001.json directly: line 42 there is "ὣς ἔφαθ’ Ἑρμείας, ἀλλ’ οὐ φρένας Αἰγίσθοιο / πεῖθ’ ἀγαθὰ φρονέων·", which is not the bare formula and does not stand alone; a full-text search of odyssey-001.json for "ὣς φάτο·"/"ὣς ἔφατο·" standing alone returns no hits at all | removed the false citation and false claim; kept only the verified contrast with 4.37 |
| 35 (ln 68) | n | major | Cited "at 2.157" for the shipped line "holding his head close...so that the others should not hear" — checked odyssey-002.json directly: that unit's `ln` is 156, not 157 | corrected to "2.156" |
| 39 (ln 76) | n | moderate | Claimed ἔπεα πτερόεντα προσηύδα is "repeated here a third time in this part (see 4.25, 4.77)" — a search of packet.md shows the formula occurs at 4.25 and 4.77 only, i.e. twice, and "4.77" is self-referential (it is the very line being annotated) | corrected to "a second time... (see 4.25)" |

### Scansion (packet.md's flagged line 13)

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 6 (ln 12, covers line 13) | n | moderate | The note hedged at length ("if that lengthening proves real rather than a licence of recitation...") instead of stating the finding plainly, as required | Scanned line 13 by hand: ἐπεὶ δὴ τὸ πρῶτον ἐγείνατο παῖδ’ ἐρατεινήν. The line's very first syllable (ἐ- of ἐπεί) must bear the ictus of foot 1, which requires a long syllable; ἐπεί's initial ε is short by nature and not lengthened by position (single consonant π follows). This matches the packet's own flag exactly ("metrical lengthening: ἐπεὶ [longum of foot 1]"). The irregularity is real. Replaced the hedging sentence with one plain sentence stating this and where |

## Findings considered but NOT changed, with reasons

- **Unit 0 (ln 1), "ἷξον... (Attic ἷκον)"**: the parenthetical implies a specific "Attic" form. ἵκω/ἱκνέομαι is barely attested in Attic prose at all (mostly tragic/epic), so "Attic ἷκον" is a slightly loose gloss. Not confidently wrong enough to rewrite without inventing a replacement claim I can't verify from the permitted lexica; left as is.
- **ἴαλλον (unit 34, ln 67), ξύνετο (unit 39, ln 76), ἱκόμεθ’/ἱκόμην (units 16, 44)**: all ι-initial (or, for ξύνετο, ε-initial-but-not-lengthening) roots where Greek's temporal augment is orthographically invisible (short vowel lengthens to long vowel of the same letter, no diacritic shows it in this edition's text). Could not disprove the "unaugmented" claims from spelling alone, and had no independent scansion evidence for these specific lines to settle it. Left unchanged rather than guess.
- **πάρθεσαν (unit 33, ln 65)**: at first glance the dropped vowel looked like it might be hiding an elided augment (the same pattern as several confirmed errors above), but on inspection it is *apocope* of παρά before a consonant-initial root (θέσαν, itself the genuinely unaugmented root aorist of τίθημι) — the same Homeric phenomenon as the already-correctly-noted κὰδ δώματα (4.72). Confirmed correct; added a cross-reference to 4.72 for clarity rather than treating it as an error.
- **κέκλετο (unit 18, ln 37)**: reduplicated root aorist (κε-κλε-το) with no separate ἐ- augment; genuinely unaugmented, distinct from the augmented Homeric variant ἐκέκλετο (which would show both reduplication and augment). Left as correctly labeled; only clarified with "reduplicated" for precision.
- **Quotation marks (item 8)**: checked every `mark`/opening “/closing ” across all 56 units against the speeches' actual boundaries. All four speeches (Eteoneus, Menelaus's rebuke, Menelaus's welcome, Telemachus, Menelaus's long reply) open and close correctly, and — checked against odyssey-013.json's actual last unit (plain narration, sundown, no open speech, no `mark`) — this part correctly opens with no continued quotation. Menelaus's final speech (from unit 40, ln 78, to the end) correctly has no closing ” anywhere, and the note at the last unit says so. No changes needed.
- **p / v flags, unit-line accounting**: checked `p: true` against every ¶ in packet.md (10 paragraph marks, 10 units flagged, exact match on `ln`); checked `v: true` present on all 56 units; checked every unit's `t`/`l` have matching `\n` counts and `i` has none; checked no `t` exceeds 5 lines (the longest is 4, unit 19/ln 39, correctly noted as cut at a comma because the sentence runs past 4 lines to its next full stop). No changes needed.
- **Remembered lines (item 7)**: checked all nine spans the packet.md documents as already published (4.52, 4.53, 4.55, 4.56, 4.57, 4.58, 4.67, 4.68, 4.70) byte-for-byte against `l`/`i` in this draft. All identical to the published wording except where a legitimately different terminal punctuation mark is called for (explained correctly in-note each time, e.g. 4.55–56 and 4.57–58 close with a full stop here vs. an ano teleia in odyssey-002, because the surrounding sentence structure differs). No changes needed.
- **House-table stock epithets (item 10)**: spot-checked every fixed epithet this part actually uses — Μενελάου κυδαλίμοιο (new-renderings.md row, 4 occurrences), ξανθὸς Μενέλαος (3x), διοτρεφής (3x), ἥρως, ἀγλαός, ἔπεα πτερόεντα προσηύδα (2x), ποιμένι λαῶν, ὠκέας ἵππους, αἰδοίη ταμίη, θεῖος (of both the minstrel and the house), Ἀτρεΐδην Μενέλαον (extension of the fixed Ἀτρεΐδῃ Ἀγαμέμνονι pattern), ἐχέφρων Πηνελόπεια, περίφρων Πηνελόπεια (correctly kept distinct) — all applied consistently in both `l` and `i`, matching conventions.md's table or new-renderings.md's declared new pairs. No violations found.
- **Disputed words (item 12)**: confirmed τηλύγετος (unit 5, ln 10) and κητώεσσαν (unit 0, ln 1) are both honestly flagged as disputed in the note, with the working choice ("late-born," "full-of-ravines") consistent with the pattern used elsewhere in the house table for other disputed words (translate with the best-supported reading, flag the dispute, don't paper over it). Ἐρεμβοί (unit 44, ln 84) is likewise honestly flagged as an unidentified people. No changes needed.

## JSON validity

Ran from `/home/user/Lectorium/.github/pipeline/odyssey`:

```
python3 -c "import json; json.load(open('drafts/odyssey-014/units.json'))"
```

Result: **parses successfully, no errors.** (Also re-verified after every edit in this pass, and again
in a final check: 56 units, all `t`/`l` newline counts match, all `i` fields newline-free, no unit's
`t` exceeds 5 lines, all `v: true`.)
