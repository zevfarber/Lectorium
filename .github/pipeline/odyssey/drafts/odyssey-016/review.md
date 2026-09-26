# Review — odyssey-016 (Odyssey 4.219–331)

Drafting and review pass 1 (translation) were split into three parallel slices (4.219–264, 4.265–305, 4.306–331) and reviewed independently, then merged; review pass 2 (glossary) ran over the merged, whole part. This file collects all of it.


---

## Pass 1, slice 4.219–264

# Review — odyssey-016, slice A (Odyssey 4.219–264), pass 1 (translation)

Reviewed against `conventions.md`, `packet.md` (including its "already published" list and
scansion-flags section, which is empty for this part), `new-renderings.md`, and the actually-published
`odyssey-009.json` (read directly, not from the packet's quote alone, for the one line in this slice
that reuses shipped wording, 4.243). All fixes below were applied in place to `review-in-A.json`. `t`
fields were never touched, and no unit was merged or split.

A script-verified check confirmed all 26 units' `t` fields, reassembled by line number (mid-line joins
treated as adjoining, matching the whitespace convention already shipped at Odyssey 1.26 in the
published `odyssey-001.json`, where a mid-line ano-teleia split also drops the single separating
space), reproduce packet.md's Greek for 4.219–264 character-for-character. No line dropped, duplicated,
altered or reordered.

Units are referenced by their `ln` (starting line number).

## Changes made

### Augment mislabelling (the flagged recurring weak spot)

Every past-tense verb form with an explicit augment/no-augment claim in the file (18 forms across 13
notes) was checked by hand against its actual spelling and against the standard analysis in Smyth,
Monro and Cunliffe. One clear case of an augmented form called "unaugmented" was found, plus two
related terminology errors (a genuine second/thematic aorist mislabelled "root aorist," the same class
of imprecision the augment warning is aimed at, since it blurs exactly the distinction that matters for
spotting a dropped augment) and one note whose account of an elision was simply wrong about which word
elides.

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 259 (first unit, ἐκώκυον) | n | **error** | "ἐκώκυον is an unaugmented imperfect of κωκύω" — but the text prints **ἐκώκυον** with its ἐ- intact; κωκύω is consonant-initial (κ-), so this ἐ- is the ordinary prefixed syllabic augment, not part of the stem. The unaugmented Homeric form would simply be κώκυον. This is exactly the augmented-called-unaugmented error the project is warned about | Reworded to state plainly that the form IS augmented, with the mechanism (syllabic augment on a consonant-initial stem) given, and the unaugmented alternative named for contrast |
| 220 (βάλε) | n | moderate | "βάλε is a true root aorist of βάλλω... so it is not a case of a dropped ἐ-" — βάλε is a **thematic (second) aorist** (stem + thematic vowel + secondary ending), not an athematic root aorist (Smyth's root aorists are ἔβην, ἔγνων, ἔδυν, etc.); and the claim that it is "not a case of a dropped ἐ-" directly contradicts conventions.md's own framing of this identical phenomenon ("πάθεν, ἴδεν, φύγον, τέκε are ordinary past tenses without the ἐ-") | Reworded to call it correctly "the unaugmented second (thematic) aorist," grouped explicitly with πάθεν/ἴδεν/φύγον/τέκε, and contrasted with the athematic root-aorist type (ἔβην) and with the augmented κατέδυ a few units later |
| 227 (πόρεν) | n | moderate | Same mislabelling: "πόρεν is a root aorist (πορ-)" — πόρεν is likewise thematic, not a root aorist | Reworded to "unaugmented second (thematic) aorist," cross-referenced to the βάλε fix above and distinguished from a true root aorist |
| 219 (ἐνόησ’) | n | moderate | The claim "IS augmented" is correct, but its own explanation was wrong: it said the augment "is simply elided before the vowel of αὖτ’" (αὖτ’ precedes ἐνόησ’ in the line and has nothing to do with its ending) and called Ἑλένη's initial breathing "smooth" (Ἑλένη in fact carries a **rough** breathing — that is where the *h* in "Helen" comes from). What is actually elided is ἐνόησε's own final -ε, dropped before the following vowel-initial Ἑλένη | Rewrote the sentence: the initial ἐ- is the (unelided) augment; the elision is of the verb's final vowel before Ἑλένη, whose breathing is rough, not smooth |

All other augment/no-augment claims in the file were checked by hand against the printed spelling and
found correct: the optatives at 222/224 (καταβρόξειεν, βάλοι, κατατεθναίη, δηιόῳεν, ὁρῷτο — optatives
are never augmented, correctly not claimed either way); the participles at 244/263 (δαμάσσας, βαλών,
νοσφισσαμένην, δευόμενον — participles never augment); κατέδυ (246, augmented root aorist of δύω,
correctly *distinguished* in the file from the mislabelled βάλε/πόρεν, since δύω's ἔδυν genuinely is one
of Smyth's root aorists) and its cross-referenced repeat at 249; ἤισκε (247, augmented imperfect,
η- from ε-, correctly flagged as easy to mistake); ἀβάκησαν (249, correctly unaugmented — the ἀ- is the
privative prefix, not a lengthened augment); ἀνέγνων and ἀνηρώτων (250, both correctly augmented,
augment fused inside the tmesis compound); ἀλέεινεν (251, correctly unaugmented); λόεον, χρῖον, ἕσσα
(252, correctly unaugmented) and ὤμοσα (252, correctly augmented, ο→ω); δῶχ’ = δῶκε (259, correctly
unaugmented — δίδωμι is consonant-initial, and the augmented Attic form would show a prefixed ἐ-, which
is absent here).

### Style/shape (`n` field mechanics)

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 219, 220, 232, 233, 237, 242, 249, 250, 251, 259 (×2), 263 | n | minor | 12 English possessives (poem's, god's, verb's ×2, Zeus's, Telemachus's, unit's, Odysseus's ×2, women's/woman's, Aphrodite's, Helen's ×2, speaker's) used the ASCII apostrophe instead of the required typographic ’ (U+2019) | Replaced all 14 instances with ’ |

### House-table application

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 227 (Πολύδαμνα / ζείδωρος ἄρουρα) | n | moderate | conventions.md's house-table row for ζείδωρος ἄρουρα (fixed at 3.3) explicitly carries "+ note: ancient alternative 'life-giving'" — and the phrase's actual first shipping, checked directly in `odyssey-009.json` (ln 20–22), does carry that note ("ζείδωρος is usually explained as 'giving ζειά'... 'grain-giving'; an ancient alternative made it 'life-giving'"). This unit reuses the phrase at 4.229 but its note said only "already fixed at 3.3," dropping the disputed-etymology flag the table calls for | Folded the alternative etymology into the existing 3.3 cross-reference, so a reader of this part alone still gets the flag |

## Findings considered but NOT changed, with reasons

- **ἐνέηκε (233), "keeps the verb's own long root vowel rather than adding a separate augment":**
  ἐνίημι's aorist is a genuinely hard case — Homeric ἔηκε/ἕηκε plausibly shows diectasis of the
  contracted Attic ἧκε (augment + long-graded, originally digamma-initial root, artificially kept in
  two syllables), which would argue the initial ε- *is* an augment after all, in tension with the
  note's claim. Because the verb's prehistory (root vowel already long from ablaut, colliding with
  where an augment would go) makes the two readings hard to tell apart from spelling alone, and because
  this project's own precedent (this same reviewer's practice for ἵκεθ’/ἴαλλον in the odyssey-015
  review) is to leave a genuinely indeterminate augment call alone rather than assert one, this was left
  unchanged. Flagged here for a second opinion rather than edited.
- **242, "Line 243 is word-for-word the same line already published in odyssey-009... (= 4.243/329)":**
  checked directly against `odyssey-009.json` (unit at its own `ln` 98): the quoted `l`/`i` for the
  shared third line match byte-for-byte except for the terminal comma→period change the note itself
  explains, which the packet's own instructions permit ("reuse the published wording for that line as
  far as your sentence allows"). The parenthetical "= 4.243/329" is slightly compressed (it is
  cross-referencing this same Greek line's *third* recurrence, at 4.329, in a different reviewer's
  slice) but not inaccurate. Left as is.
- **263, θάλαμον rendered "marriage chamber" in `i` (l keeps plain "chamber"):** slightly more specific
  than the bare Greek noun, but θάλαμος paired with πόσις ("husband") in this exact context plausibly
  does mean the marriage bed-chamber; this is a defensible interpretive gloss for the prose layer, not
  an addition of meaning `l` lacks. Left unchanged.
- **Quotation marks and the open speech:** confirmed exactly one “ in the whole slice (unit 235,
  `mark: "Helen speaks"`, correctly placed on the unit with Helen's actual first words rather than on
  the narrator's `ἐξαῦτις μύθοισιν ἀμειβομένη προσέειπεν·` line before it) and zero ” anywhere. The
  final unit (263, `ln` 263) explicitly states in its note that the speech is not closed in this slice
  and will close only at 4.265 in the next one. No changes needed.
- **Segmentation:** all 26 units end at a genuine full stop, `·`, or (three times: 222, 252, 259-second)
  a deliberate comma-cut. Checked each of the three comma-cuts by hand: 222–226 and 252–256 are both
  single sentences that would otherwise run 5 lines, cut at the strongest available syntactic pause
  (222: before the two οὐδ’ εἴ clauses; 252–255: at the correlative μή…πρίν… break, completed in the
  next unit); the 259(second)–264 sentence would otherwise run 6 line-numbers and is cut after the ὅτε
  clause, before the participial clause παῖδά τ’ ἐμὴν νοσφισσαμένην begins. All three keep both halves
  at or under 4 lines and cut where the syntax pauses most. No merge/split errors found.
- **New-renderings.md's 3 rows sourced from this slice** (νηπενθές τ’ ἄχολόν τε, Πολύδαμνα/Θῶνος
  παράκοιτις, Παιήονός … γενέθλης): all three checked against the units that use them (220, 227, 232)
  and found applied exactly as specified, including the required flags (Πολύδαμνα/Θῶνος correctly
  noted as otherwise-unknown names, not embellished; Παιήων correctly distinguished from Apollo Paean).
  No changes needed beyond the ζείδωρος ἄρουρα note above (a pre-existing house-table entry, not one of
  the 3 new rows).
- **House-table sweep beyond the flagged terms:** δῖα/δῖος and τανύπεπλος do not occur in this slice
  (they belong to 4.291/4.305, outside 219–264); ταλασίφρων (240) matches the fixed "enduring-minded" /
  "steadfast" exactly; Διὸς θυγάτηρ (227), applied to Helen by analogy with Athena's fixed use, matches
  the table's wording exactly; εὐρυάγυιαν (246) is correctly kept distinct from the already-fixed
  εὐρυόδεια. No collisions found.
- **`p`/paragraph accounting:** packet.md marks ¶ only at 219 and 235 within this slice; the file has
  `p: true` at exactly those two units and nowhere else.
- **Cross-references to line numbers within this slice's own notes** (3.3 for ζείδωρος ἄρουρα, 246↔249
  for κατέδυ): both checked directly against conventions.md and the unit at 244 respectively, and found
  accurate.

## JSON validity

```
python3 -c "import json; json.load(open('.github/pipeline/odyssey/drafts/odyssey-016/review-in-A.json'))"
```

Result: parses successfully, 26 units, throughout and after every edit. Final sweep confirmed: no
backtick or ASCII apostrophe remains in any `n` field; all note word counts fall in 25–110 (lowest 27,
highest 87); exactly one “ and zero ” in the file; exactly one `mark`, on the correct unit; all `t`
fields byte-identical to their original content (only `l`/`i`/`n` were edited); the 26 units'
concatenated `t`, rejoined by line number, still reproduces packet.md's Greek for 4.219–264 exactly.


---

## Pass 1, slice 4.265–305

# Review B — odyssey-016, 4.265–305 (Pass 1: translation)

Reviewed against `conventions.md`, `packet.md` (odyssey-016), and the published
`odyssey-015.json`, `odyssey-004.json`, `odyssey-014.json`, `odyssey-001.json`,
`odyssey-011.json`. `review-in-B.json` edited in place. No `t` field touched.

## Fixes made

1. **ln 271 · `n` · MAJOR (systematic-error pattern).** The note called `ἔτλη`
   "unaugmented... whose ε- belongs to the root, not to an augment." This is wrong:
   `ἔτλη` is a root aorist of the ἔβη/ἔστη/ἔγνω type (bare root τλη-, seen without
   augment only in the infinitive τλῆναι); the initial ἐ- in `ἔτλη` *is* the
   syllabic augment, prefixed to the root exactly as in ἔβη. It is augmented, not
   unaugmented — the same class of mistake (augmented form called unaugmented)
   the brief flagged as this project's recurring weak spot. Rewrote the clause to
   state `ἔτλη` is "likewise augmented... built like ἔβη and ἔστη," trimmed
   slightly afterward to bring the note back under the 110-word cap (it had
   drifted to 112 words after the first pass at the fix).

2. **ln 267 · `n` · MAJOR (same error, earlier occurrence).** This note listed
   `ἔτλη` among "the several genuinely unaugmented aorists in Menelaus's speech
   (ἴδον, ἔσκε, ἔτλη)" — the identical mislabeling, stated before the reader even
   reaches ἔτλη's own line. Removed ἔτλη from the list; ἴδον and ἔσκε are both
   genuinely unaugmented and remain as the examples.

3. **ln 282 · `n` · MODERATE (wrong cross-reference).** The note contrasted
   `μενεήναμεν` with "μενέαινεν 'raged' used of Poseidon at 1.21." Checked
   `odyssey-001.json`: that unit's `ln` is 20, not 21 (`ὁ δ᾽ ἀσπερχὲς μενέαινεν /
   ἀντιθέῳ Ὀδυσῆι πάρος ἣν γαῖαν ἱκέσθαι`). Fixed the citation to 1.20.

4. **ln 289 · `n` · MODERATE (fabricated cross-reference).** The note claimed
   `ἔχ᾽` (= ἔχε) was "the unaugmented imperfect already seen at 1.27." Checked
   `odyssey-001.json` lines 26–28 directly: no form of ἔχω appears there at all
   (line 26 is ἐτέρπετο/ἦσαν, line 27 is the back half of the Olympian-halls
   line, line 28 is the μύθων ἦρχε formula). The citation does not correspond to
   anything published. Removed the false "already seen at 1.27" and replaced it
   with a self-contained, defensible statement (ἔχε unaugmented vs. Attic εἶχε,
   without inventing a location for a prior occurrence).

## Segmentation (item 10) — firm decision

**The drafter's own flagged question:** does a unit have to end at the *first*
ano teleia it meets, or can short, tightly-bound clauses be grouped past one?

**Method:** searched every published `odyssey-0*.json` for a `·` that is not at
the very end of a `t` field (i.e., a mid-unit ano teleia). Across all fifteen
shipped parts there is exactly **one** such case: `odyssey-011.json`, ln 265 —
`ἡ δ᾽ ἦ τοι τὸ πρὶν μὲν ἀναίνετο ἔργον ἀεικὲς / δῖα Κλυταιμνήστρη· φρεσὶ γὰρ
κέχρητ᾽ ἀγαθῇσι·` — where a terse main clause ("she refused it") is followed
past the ano teleia by a γάρ-clause that explains *why*, and the two are kept
in one tap-unit rather than split.

**Firm ruling:** the rule "ends at a full stop, ; or ·" is the *default*, and
the corpus follows it almost without exception. Grouping past a mid-unit ano
teleia is a narrow, precedented exception used specifically when what follows
is a γάρ-clause giving the immediate reason for the clause just stated — i.e.
the two clauses are one argument, not two events. It is not a license to group
any two short clauses.

Applying this to the two flagged spots:

- **291–293** (`Ἀτρεΐδη Μενέλαε... / ἄλγιον· οὐ γάρ οἵ τι τάδ᾽ ἤρκεσε...`):
  matches the precedent exactly — a terse assessment ("all the more painful")
  followed by an οὐ γάρ clause justifying it. **Kept as one unit, unchanged.**
- **300–301** (`...δέμνια δὲ στόρεσαν· ἐκ δὲ ξείνους ἄγε κῆρυξ.`): does **not**
  match the precedent — the clause after the ano teleia is a plain δέ-linked
  new event with a different subject (the herald, not the maids), not an
  explanation of what precedes it. **Split** into two units at the ano teleia:
  ln 300 (`αἱ δ᾽ ἴσαν... στόρεσαν·`) and a new ln 301 (`ἐκ δὲ ξείνους ἄγε
  κῆρυξ.`), per the instruction that the second half keeps the line number it
  actually starts on. Total unit count in the file is now 22.

## Findings checked and refused (no change made)

- **ln 287, `l`** — "with his hands... pressed down... with his strong hands"
  appears to mention hands twice for one Greek χερσὶ...κρατερῇσι. Not an error:
  it mirrors the source's own hyperbaton (the phrase is split across the line
  break in the Greek too), and the note already explains the split; no sense is
  added or lost.
- **ln 271, `n`** — "echoes Helen's own account... a few lines earlier" (the
  echoed line is actually 29 lines earlier, at 4.242, in the previous
  reviewer's slice). Left as is: this is a loose descriptive phrase, not a
  specific claim to fail on, and the underlying claim is true — Helen's 4.242
  is word-for-word `τόδ᾽ ἔρεξε καὶ ἔτλη καρτερὸς ἀνήρ`, confirmed against the
  packet.
- **Quote marks and `mark` placement (item 8)** — checked exhaustively, unit by
  unit. All correct: no mark/quote on the plain narration units (265, 290, 296,
  300/301, 302, 304); `mark: "Menelaus answers Helen"` and the ”“ pair (both in
  `l` and `i`) exactly on 266; Menelaus's speech closes with a single ” at 289;
  `mark: "Telemachus answers"` and opening “ on 291; Telemachus's speech closes
  with a single ” at 294. No stray or missing marks anywhere in the slice —
  this is the one part of the brief's checklist that needed no correction.
- **Reused lines (item 7)** — 4.265 (= odyssey-015 ln 147), 4.290 and the
  vocative half of 4.291 (= odyssey-004 ln 388 and odyssey-015 ln 156), and the
  repeated half-line at 4.303 (= odyssey-014 ln 20) were pulled directly from
  the published JSONs and diffed character-for-character against both the
  packet's quotations and this draft's `l`/`i`. All match exactly, including
  the ASCII (not typographic) apostrophes in "Atreus'" and "Nestor's" that the
  published wording itself uses — left untouched, since "fixing" them to U+2019
  would break the required verbatim reuse.
- **House-table renderings (item 9)** — ταλασίφρων (270: "the enduring-minded" /
  "steadfast"), δῖος of Odysseus (280: "heavenly"), Τυδεΐδης (280: "the son of
  Tydeus"), υἷες Ἀχαιῶν (285: "sons of the Achaeans"), δῖα γυναικῶν reapplied to
  Helen (305: "heavenly-one of women" / "heavenly among women"), and θεοείκελος
  reapplied from Telemachus (3.416) to Deiphobus (276: "god-resembling" / "who
  was like a god") — all checked word-for-word against the conventions.md table
  and all correct.
- **new-renderings.md (item 11)** — Ἄντικλος → "Antiklos" (285) and τανύπεπλος →
  "long-robed" (305) both applied in `l` and `i` exactly as fixed.
- **`t` fidelity (item 13)** — reconstructed the full 265–305 text from the 22
  units' `t` fields (allowing for the whitespace convention at mid-line splits,
  confirmed against the precedent at odyssey-001 ln 26) and diffed it
  character-for-character against the packet's source block: exact match, no
  drop/add/retype.
- **Augmentation audit (item 1), full sweep beyond the two errors above** —
  every past-tense verb form in the slice was checked by hand against its
  Attic equivalent: ἔειπες, ἐδάην, ἴδον, ἔσκε, ἔρεξε, ἀκούσαμεν, ἐβόησας,
  μενεήναμεν, κατέρυκε, ἔσχεθεν, σάωσε, στόρεσαν, ἄγε (×2), κοιμήσαντο were all
  labeled correctly (only the ἔτλη instances, above, were wrong).
- **Note length / typography (item 12)** — all 22 notes now fall within 25–110
  words (one, ln 271, needed trimming after its fix); no backticks or ASCII
  apostrophes in any `n` or `t` field.

## Summary counts

- Errors/major fixes: 2 (the two ἔτλη augmentation mislabelings, ln 267 and 271)
- Moderate fixes: 3 (μενέαινεν 1.21→1.20; the fabricated "ἔχε... at 1.27"
  citation; the 300–301 segmentation split)
- Minor fixes: 1 (trimming ln 271's note back under the word cap)
- Findings considered and refused: 6 (listed above)


---

## Pass 1, slice 4.306–331

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


---

## Pass 2, glossary (whole part)

# Review 2 — Glossary pass, odyssey-016 (Odyssey 4.219–331)

This pass was split across two agent instances (the first interrupted by an infrastructure
restart before it could write up its findings). This report covers the complete picture:
what the first instance had already fixed, what this instance verified, and what this
instance additionally found and fixed.

## Method

- Read `conventions.md` (glossary section), `units.json` (60 units), `gloss.json` (183 novel
  entries + `__broaden__`), `novel-forms.json`, `known-forms.json`, and the master
  `odyssey-glossary.json`.
- Wrote a small script replicating `odyssey_lib.forms()` (the exact tokenization the build
  script uses: `WORD` regex over `t` fields, lower-cased) to check coverage.
- Built a form→context map for all 386 known forms and all 183 novel forms against every
  line they appear on in this part's `units.json`, and checked each master/gloss entry's
  stated case/number/gender/tense/mood/voice against that context.
- Grepped every unit note (`n`) that mentions "augment" (29 units did) and checked each
  claim against the actual verb's root, principal parts, and the augment rules stated in
  `conventions.md`.

## Coverage check: PASS, clean

- 569 unique word-forms appear in this part's `t` fields (800 tokens total).
- Every one has an entry, either in `gloss.json` (183 novel forms) or the master glossary
  (386 known forms). Zero forms are missing coverage.
- `novel-forms.json` and `known-forms.json` exactly partition the 569 forms: no form is in
  both lists, no form in either list is absent from `units.json`, and no form in
  `units.json` is absent from both lists.
- This confirms the build script will not refuse on missing glossary coverage.

## Work already done by the interrupted first pass (verified, not redone)

1. **Apostrophe style fix**: every English gloss and quoted-Greek gloss in `gloss.json` now
   uses the single typographic `’` (U+2019) exclusively. I scanned the whole file
   programmatically for left curly quotes (`‘`), ASCII apostrophes (`'`), and backticks —
   zero found anywhere, including inside the five `__broaden__` entries. This was a
   systematic, complete fix; nothing was left half-converted.
2. **Five `__broaden__` entries** (οἵ, ἐπὴν, ἐοικότα, δυσμενέων, ἐδήσατο, τοί) — I re-derived
   each from scratch against the actual line(s) where the form is used in this part, and
   independently confirmed all five are correct and genuinely needed:
   - **οἵ** (used twice, ll. 291 and 318): l.291 is the enclitic dative singular pronoun
     "to/for him" (accented because followed by the enclitic τι — confirmed against the
     unit's own note, which correctly reads it as dative); l.318 is the plain relative
     "who" matching the master's existing entry. Both readings needed; broaden is correct.
   - **ἐπὴν** (l.222): master had only "conj. + subj."; here it governs a bare optative
     (μιγείη) in a generalizing conditional with no ἄν/κε — a genuine second reading.
     Correct.
   - **ἐοικότα** (l.239): master had only the masc. acc. sg. participial reading
     ("fitting", ἐοικότα μυθήσασθαι); here it is neuter nom./acc. plural, substantival,
     "fitting things" (ἐοικότα γὰρ καταλέξω). Correct, distinct reading.
   - **δυσμενέων** (used twice, ll. 244 and 318): l.244 is the participle reading already in
     master (masc. nom. sg., "being hostile"); l.318 is the adjective δυσμενής, gen. pl.,
     agreeing with ἀνδρῶν ("of hostile men") — genitive plural of a 3rd-declension -ής
     adjective cannot be confused with the participle's paradigm (which would give
     δυσμενεόντων in the genitive plural), so this really is a distinct homograph. Correct.
   - **ἐδήσατο** (l.309): master had only "bound on (for herself)"; here the subject is
     Menelaus binding on his own sandals — same verb form, needs the masculine reading
     added. Correct.
   - **τοί** (l.328): master had only the nom. pl. pronoun/relative reading; here it is the
     enclitic dative singular "to you" (σοι), written with an accent because it precedes
     another enclitic (τι) — the standard rule that the first of two successive enclitics
     is accented. Correct reading, though see the one polish item below.
   - All six broaden values were checked to contain the old master-glossary text **whole**,
     followed by ` · ` and the new reading, and all are under 230 characters (the longest,
     ἐοικότα, is 223).
3. **Two note (`n`) fixes in `units.json`** made by the first pass are present at ll. 219
   (ἐνόησ’ correctly explained as augmented, with the elision it's easy to mistake for
   correctly separated from the augment question) and one other small correction; I did not
   find any regression from these, and they read correctly in context.

## New findings and fixes made in this pass

### 1. Augment mislabeling — `ἐνέηκε` (l.233 note, and its `gloss.json` entry) — FIXED

This is exactly the documented weak spot ("augment mislabeling in any parse mentioning a
verb's principal parts"). The note at l.233 said:

> "ἐνέηκε, from ἐνίημι, keeps the verb's own long root vowel rather than adding a separate
> augment"

and `gloss.json`'s own entry echoed it:

> "aor. 3 sg., root vowel kept in place of a separate augment"

Both phrasings imply ἐνέηκε has **no** augment. That is wrong, and is directly
self-contradicted two sentences later in the very same note, which correctly calls the
structurally identical form προσέειπεν "the uncontracted, **still-augmented** form" (augment
present but not fused with the following long vowel, because Homer still feels the lost
initial consonant of the root). ἐνέηκε is the same category: ἵημι-compounds in Homer
(ἐνέηκε, ἀφέηκε, μεθέηκε, προέηκε) show the augment ἐ- standing in hiatus before the root's
own long η, where Attic contracts the two into a single ἐνῆκε (per Monro's Homeric Grammar's
treatment of augment-plus-long-vowel-initial roots — the same phenomenon documented for
ἔειπε/εἶπε elsewhere in this same part). ἐνέηκε **is** augmented; it just isn't fused.

**Fix applied:**
- `units.json` l.233 `n`: now reads "ἐνέηκε, from ἐνίημι, IS augmented, like προσέειπεν just
  below: the augment ἐ- stands unfused before the root's own long η (ἐν-έ-ηκε), where Attic
  contracts the two into a single vowel, ἐνῆκε; ..." (rest of the note unchanged).
- `gloss.json` `"ἐνέηκε"`: now reads "ἐνίημι — put in, send into; aor. 3 sg., augmented,
  augment ἐ- uncontracted before the root's own long η (= Attic ἐνῆκε): 'put it in'".

### 2. Minor polish — `τοί` broaden entry wording

The added reading originally said "(= τοι, accented τοί here)". "Here" read as if pinning
the fact to this specific occurrence rather than stating the general orthographic rule
(the first of two successive enclitics is accented). Reworded to "(= τοι, accented before a
following enclitic, e.g. τοί τι)" so the entry states a rule usable wherever this word
recurs, per the "never pinned to a line" requirement for glossary entries. Not a
correctness bug — the underlying grammar was already right — just tightened for generality.

## Findings considered and NOT changed (with reasons)

- **`αὐτόθι` and `ἄντικλος` gloss entries contain the word "here"** — flagged by an automated
  string search, but both are legitimate: `αὐτόθι`'s English gloss is simply "here, on the
  spot, right there" (the word's actual dictionary meaning, not a line-pinning remark), and
  `Ἄντικλος`'s entry states "mentioned only here in the poem," a lexically checkable fact
  (Cunliffe's *Lexicon of the Homeric Dialect*, an approved aid, indexes it as occurring
  nowhere else in the Odyssey) rather than an invented or line-specific claim. The master
  glossary itself uses "here" this way in >50 existing entries (e.g. "here transferred to a
  speech," "here fig.," "here a district of Thessaly"), so this is house style, not a
  violation. Left unchanged.
- **Additional `__broaden__` entries beyond the 5 already present** — I checked all 386
  known forms' contexts against their master-glossary entries and found no case where the
  existing master reading fails to cover this part's usage, beyond the two forms (οἵ,
  δυσμενέων) that recur with a second sense within this same part, and ἐπὴν/ἐοικότα/ἐδήσατο,
  which needed broadening on their single occurrence — all five already caught by the first
  pass. No sixth broadening was warranted.
- **Repeated novel forms with potentially different senses**: four novel forms recur more
  than once in this part (καρτερὸς, κατέδυ, ἔρεξε, ἤγαγε). In every case the repeated
  occurrence carries the *same* sense/parse as the first (e.g. ἤγαγε means "brought/led" all
  three times it appears, with different objects but no grammatical difference), so a single
  entry legitimately covers all instances; no homograph-joining was needed for these.
- **Invented or smoothed-over disputes**: searched every `n` note and every `gloss.json`
  entry for "disputed"/"unknown"/"uncertain." Found exactly one, `ζείδωρος` (l.227,
  gloss.json), correctly noting the genuine ancient dispute between "grain-giving" and
  "life-giving" — this matches the already-fixed house-table entry for the same word at
  3.3 (odyssey-010) and is not an invented crux. No case was found of a real dispute being
  silently smoothed over, nor of a false dispute being invented.
- **Every other "augmented"/"unaugmented" claim in the 29 units whose notes discuss
  augment** (ll. 219, 220, 222, 224, 227, 233, 244, 247, 249, 250, 251, 252, 259×2, 266,
  267, 269, 271, 280, 282, 284, 287, 289, 300, 301, 302, 306, 309, 312, 316, 322, 325, 326,
  328) was checked individually against the verb's actual root and the standard augment
  rules (syllabic ἐ- for consonant-initial stems, temporal lengthening α/ε→η, ο→ω, ι→ῑ,
  υ→ῡ for vowel-initial stems, and the Homeric-specific "uncontracted augment before a
  root's own long vowel" category). All were correct except the one fixed above. In
  particular I double-checked the two second-pass-reviewer flagged bug pattern
  ("augmented called unaugmented") across the whole file and found no further instance of
  it beyond ἐνέηκε.
- **Translation-pass (pass 1) self-consistency**: re-read every note in `units.json` for the
  "augmented called unaugmented" bug both pass-1 reviewers reportedly found instances of.
  Found none remaining (the ἐνέηκε case found here is a glossary-note issue in the same
  family, not a leftover pass-1 regression — it was introduced/retained specifically in the
  augment-heavy commentary this part carries, and is now fixed).
- **Article-vs-pronoun, possessive ὅς/ἥ/ὅν vs relative, genuine homographs**: spot-checked
  throughout (e.g. `ὃς`, `ἣν`, `τὸν`, `οἱ`/`τοί` entries) — all correctly kept apart per the
  master glossary's existing entries and this part's added broadenings.
- **Line-pinning, length, homograph-joining across all 183 novel entries**: checked
  programmatically (length ≤ 230 for all entries, longest is 223) and by direct reading;
  no entry pins its sense to "here" (in the problematic sense) or to a specific line number.

## Summary of edits made in this pass

| File | What changed | Severity |
|---|---|---|
| `units.json` | l.233 `n`: corrected ἐνέηκε from "no separate augment" to "IS augmented, uncontracted" | Real (augment mislabeling) |
| `gloss.json` | `"ἐνέηκε"` entry: same correction | Real (augment mislabeling) |
| `gloss.json` | `__broaden__.τοί`: reworded "accented τοί here" → "accented before a following enclitic" | Polish (generality) |

No further edits were needed. `t` fields were never touched.

---

## Cross-slice seam fix (made directly, not by a per-slice reviewer)

After all three pass-1 slices were reviewed independently, a further defect was found by checking this part's own Helen/Menelaus speech seam (4.264/265/266) against actual precedent, since no single slice reviewer had both sides of that seam in view. The drafting instructions had wrongly built a combined "”“" mark at that boundary, on the false assumption that a same-part speech transition needs the same treatment as a speech left open across a *part* boundary (like odyssey-014→015's Menelaus speech). Checking odyssey-014→015's actual handling, and odyssey-015's own internal Helen/Menelaus exchange, confirmed the real rule: a reply-formula line always carries neither mark, and each speech's own closing ” belongs on that speech's own last unit. Fixed by moving the closing ” to the end of 4.264 (Helen's actual last words) and removing the stray leading ” from 4.266 (Menelaus's actual first word), with both units' notes corrected to explain the seam plainly.
