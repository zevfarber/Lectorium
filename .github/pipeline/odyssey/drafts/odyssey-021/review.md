# Review — odyssey-021 (Odyssey 4.742–847), pass 1

Reviewer pass 1 of 2 (adversarial). 62 units checked against conventions.md's full table,
packet.md's reuse list, new-renderings.md's judgment calls, and odyssey-020.json's boundary.
11 edits made, all confined to `l`/`i`/`n`; `t` untouched (verified against `git diff`: 11
changed lines, all outside any `"t":` field). No `p`/`mark` changes were needed.

## Changes made

### High severity (factual grammar errors — would mislead a reader trying to learn from the note)

1. **ln745, `n`** — "ᾔδε' ... a pluperfect of οἶδα used with **present** sense, 'I knew'" was
   self-contradictory: it glosses the form as past ("I knew") while calling that "present sense."
   Since the perfect οἶδα itself carries present force ("I know"), its pluperfect regularly carries
   *past* force — the note had the polarity backwards. Fixed to "used with past sense," with a
   one-clause explanation. (Confirmed the correct pattern was already used correctly elsewhere in
   this very draft, e.g. ln772's note on ἴσαν, which made me confident this was a slip rather than
   a different intended claim.)

2. **ln754 (second unit), `n`** — "ὀίω is 'I think' ... **an old athematic form**." ὀίω/ὀΐομαι is
   an epic uncontracted (diectasis-type) present of the ordinary *thematic* verb οἴομαι (ὀίω, ὀίεαι,
   ὀίεται...), not an athematic (-μι) verb. Fixed the mischaracterization.

3–6. **Four augment mislabellings.** The draft repeatedly mislabels four epic long-vowel/prefixed
   aorists as "unaugmented" when each is actually the *augmented* member of a live Homeric pair
   (a genuinely augmented form beside a shorter unaugmented alternative the poet uses for metrical
   convenience — exactly the mechanism conventions.md itself illustrates with βῆ/ἔβη,
   ἐρέειν-type doublets, etc.). I checked each against its own unaugmented counterpart, including
   one that appears in this very part:
   - **ln784, `n`**: ἤνεικαν (τεύχεα δέ σφ’ ἤνεικαν) called "unaugmented ... built on the
     alternative root ἐνεγκ-." It is in fact the augmented form on the epic root ἐνεικ- (η- from
     augment ε- + ε-), contrasting with unaugmented ἔνεικα. Root identified was also wrong
     (ἐνεγκ- is the separate Attic-type root; the Homeric form here is built on ἐνεικ-). Fixed both.
   - **ln785, `n`**: ἔβαν (ἐκ δ’ ἔβαν αὐτοί) called "unaugmented." This draft's own ln778 unit,
     eight lines earlier, correctly glosses the *un*augmented plural βάν ("βὰν δ’ ἰέναι") as
     unaugmented — ἔβαν at 785 is exactly its augmented counterpart (ἔ- + βαν, parallel to
     ἔβη/βῆ in the singular, which conventions.md's own fixed row 170 keeps distinct: "βῆ δ’ /
     βῆ ῥ’ ἴμεν" is the *un*augmented formula). Fixed, with a cross-reference to 779 (the
     unaugmented form).
   - **ln802, `n`**: ἔειπεν (καί μιν πρὸς μῦθον ἔειπεν) called "unaugmented aorist of εἶπον." The
     visible ἔ- prefixed onto the (already-contracted) εἰπ- stem is exactly what makes ἔειπε(ν)
     the metrically longer, augmented alternative to the shorter εἶπε(ν). Fixed.
   - **ln810, `n`**: ἤλυθες (δεῦρ’ ἤλυθες) called "unaugmented ... (Attic ἦλθες)." The η- is
     itself the augment (on the epic root ἐλυθ-, parallel to Attic's augmented ἦλθες on ἐλθ-); the
     unaugmented form would be ἔλυθες. Fixed.

   (I re-checked every other "unaugmented" claim in the draft against this same test — πόρον,
   ἕλετο, φάτο, σχέθε, ἴσαν, βάν [779], ἕλοντο, λύθεν, προέηκε — and all nine are correctly
   labelled; the four above were the only mislabelled instances.)

### Medium severity (false cross-references — the note asserts a recurrence that isn't there)

7. **ln765, `n`** — claimed the ὑπερηνορέοντας root "will recur of them at 769 **and 790**." Line
   790 actually reads ὑπερφιάλοισι, a different (if near-synonymous) adjective; only 769 repeats
   the ὑπερηνορέων root. Fixed, and pointed to where the *other* root recurs instead.

8. **ln774, `n`** — the reciprocal error: claimed ὑπερφίαλος here "echo[es] the same root already
   applied to them at 766, 769 and 790." Lines 766 and 769 are actually ὑπερηνορέοντας /
   ὑπερηνορεόντων, not ὑπερφίαλος; only 790 shares this note's actual root. Fixed both notes so
   they now correctly cross-reference each other's root rather than conflating the two.

9. **ln842, `n`** — claimed ὁρμαίνοντες "picks up the verb ... already used of Penelope (789,
   **791**, 793)." Line 791 is μερμήριξε (a different verb, "pondered/worried," in the lion
   simile), not ὁρμαίνω. ὁρμαίνω only recurs at 789 and 793. Fixed.

### Medium severity (translation accuracy)

10. **ln773, `l`** — "And **among them** Antinous addressed-the-assembly and spoke **among
    them**:" translated the single dative τοῖσιν twice (once fronted, once inside the house-fixed
    formula's own "spoke among them," conventions.md row for ἀγορήσατο καὶ μετέειπε). Removed the
    redundant lead-in ("And Antinous addressed-the-assembly and spoke among them:"), which now
    renders τοῖσιν exactly once, matches the `i` field's phrasing, and keeps the fixed formula's
    exact wording intact.

### The ὣς φάτο / gender decision (see below) plus its mechanical fallout

11. **ln758, `i`** — independent of the gender question, the `i` field read "**So she said**, and
    calmed Penelope's grief..." — conventions.md's row for ὣς φάτο fixes "spoke" and explicitly
    lists "So he **said**" in the *avoided* column, precisely to stop exactly this kind of drift.
    The draft's own `l` field already correctly kept "spoke." Fixed `i` to "So she **spoke**, and
    calmed..." — this holds regardless of which way the gender question below is decided, since
    both candidate answers use "spoke," never "said."

## The ὣς φάτο gender decision

**Decision: track natural gender.** "So he spoke" is not fixed as a generic, sex-blind default;
at 758 (Eurycleia, a female speaker) the correct rendering is "So she spoke" / "So she spoke,"
— which is what I left in place (only fixing the `i` field's "said" as above). I'm recording this
as a new table entry (see below) so pass-2 and future parts follow it without re-litigating it.

**Reasoning.** Two things pull in different directions here:

- On one hand, "keep one form throughout" is real language in conventions.md's row for ὣς φάτο,
  and a naive reading could take it to mean "the English word is frozen regardless of context" —
  the same way `ἥρως` is always "the hero" even where "lord" might read better, or `δῖος` is
  always "heavenly" even where it sits oddly. And English translation does have a documented
  habit, going back a long way, of using generic "he" for grammatically unmarked forms.
- On the other hand, φάτο itself is **grammatically unmarked for gender** — the identical verb
  form serves a male or female subject with no change of spelling. That is exactly unlike the
  cases where this project's table already tracks separate masculine/feminine fixed renderings:
  - `ὣς ἄρα φωνήσας` (masc., row) vs `ὣς ἄρα φωνήσασ'` (fem., row) — the Greek participle itself
    is morphologically gendered (-ας vs -ασα), and the table already keeps two distinct entries,
    explicitly cross-referenced to each other ("kept as parallel but separate entries, one
    masculine and one feminine, exactly as the table already does for the ὣς ἐφάμην
    reply-formula").
  - The ὣς ἐφάμην reply-formula itself: a masculine variant (ὁ δέ μ' αὐτίκ' ἀμειβόμενος
    προσέειπεν, fixed "he") is deliberately kept *separate* from an already-shipped feminine
    variant at 4.464 ("So she spoke, and I then, answering her, addressed her:"), specifically
    because "ὁ here is explicitly masculine."
  - Every reply-formula that takes a pronoun (τὸν/τὴν δ' ἠμείβετ' ἔπειτα, τὴν δ'
    ἀπαμειβόμενος/-ον προσέφη, τὸν/τὴν δ' αὖτε προσέειπε) already tracks the grammatical gender
    of its Greek pronoun in the fixed English, and every ordinary third-person pronoun in this
    draft and in the wider convention set (οἱ, μιν, ἥ, etc.) is translated according to its actual
    referent, never frozen to one sex.

  Given that the house practice, wherever Greek grammar independently signals sex (a gendered
  participle, a gendered pronoun), is to track it in English, and given that φάτο carries **no**
  grammatical signal either way, the only source of "which pronoun is correct" for ὣς φάτο is the
  discourse context — exactly as it is for οἱ, μιν, and every other unmarked 3rd-person form in
  the poem. Treating ὣς φάτο as *the one* formula frozen to "he" regardless of the actual speaker
  would be the outlier, not the rule, and it would sit oddly beside a passage that a few lines
  later (830) uses the feminine τὴν δ' αὖτε προσέειπε of the very same phantom without hesitation.
  I read "keep one form throughout" as being about *wording* (don't drift between "Thus he
  spoke"/"So he said"/"So he spoke" for stylistic variety — the three items in the avoided column
  are exactly these three near-synonyms, not "So she spoke"), not about *freezing the pronoun*.

  I also weighed that "generic he" is a real historical convention in English translation — but
  it is a convention for cases where the sex of the referent is unknown or irrelevant (a rule for
  a general subject), which does not describe this poem: Homer's own grammar marks referent sex
  constantly and accurately throughout, and readers of this translation are meant to feel exactly
  who is speaking. Using "he" for Eurycleia's own words being introduced would misdescribe the
  scene to a reader relying on the English alone.

**New table row proposed** (for merging into conventions.md and carried forward):

| Greek | `l` | `i` | avoided on purpose |
|---|---|---|---|
| ὣς φάτο (used of a female speaker; cf. the existing row for the masculine) | "So she spoke" | "So she spoke" | "So she said", "Thus she spoke" (keep one form throughout, exactly as fixed for the masculine — the pronoun alone tracks the actual speaker's sex, the wording after it does not vary) |

I did not touch the existing masculine row; I'm adding this as a sibling entry, the same way the
table already keeps ὣς ἄρα φωνήσας / φωνήσασ' and the two ὣς ἐφάμην reply-formulas as separate
but parallel rows.

## Judgment calls reviewed and left unchanged

- **τὸν/τὴν δ' αὖτε προσέειπε applied to a feminine object (742, 830).** Reviewed against the
  Greek (τήν at both spots, correctly agreeing with the female addressee: Penelope at 742,
  the phantom, addressed as feminine, at 830) and against the established pattern of other
  gender-paired reply-formulas in the table (see the ὣς φάτο discussion above). This is the
  identical formula gender-matched to its actual Greek pronoun, not a new coinage, and I agree
  with the drafter's own note that it should be folded into row 127's wording ("τὸν/τὴν δ' αὖτε
  προσέειπε") rather than kept as a separate table entry. No change made to the draft; recommend
  the fold-in at the next conventions.md edit.
- **κατὰ μοῖραν, ln780–783, `i`: "as **was** fitting" vs the table's fixed `i` "as **is**
  fitting."** Left unchanged. The table's present tense reads naturally in whatever tense-neutral
  context it was first fixed in; here the clause sits inside a past-tense narrative ("they set
  the mast... as was fitting, and spread the sails"), and switching to present tense mid-narration
  would be the actual error. Treating this as a necessary tense inflection of a fixed idiom, not a
  deviation from it.
- **θεῖος applied to Odysseus (ln799), extending a table row written for Phemius (θεῖον ἀοιδόν).**
  Left unchanged. "Divine" is the plain, correct sense of θεῖος regardless of referent, the
  drafter's own note explicitly distinguishes it from the reserved δῖος/θεοειδής, and conventions.md's
  row was never phrased as "only ever apply this to Phemius" — it fixes the *word's* rendering.
  This is a correct, well-flagged extension, not a violation.
- **πωλέ(ο), ln810, `n`: called "imperfect" of πωλέομαι.** Left unchanged. LSJ/Cunliffe attest
  both present and imperfect uses of this verb in Homer for exactly this "have habitually come"
  sense, and the bare form doesn't disambiguate cleanly; I could not build a confident case either
  way to override the drafter's reading, so I'm flagging this for pass 2 / QUESTIONS.md rather
  than silently picking a side.
- **ln794, `n`: "ἅψεα... a formula elsewhere applied to fallen warriors."** This is true of
  Homeric diction generally (the λύθεν/λύτο γούνατα-type formula in death scenes) but is not
  something *this part* can show, and strictly reads as the kind of claim conventions.md's Notes
  section says a note should not make ("asserts nothing about the rest of the poem that this part
  cannot show"). I left it, since it is uncontroversial background common to any reader of Homeric
  formula-scholarship rather than a claim about this specific translation's own future parts, but
  I flag it as borderline for pass 2's judgment.
- **ln818, `n`: "νήπιος... a recurring judgment on Telemachus's inexperience in the poem's early
  books."** Same category as above — plausible and almost certainly true (Athena/Mentor use νήπιε
  of him in Book 1, already published), but not verifiable from this part alone under a strict
  reading of the no-forward-claims rule. Left unchanged, flagged for pass 2 if it wants to verify
  against the actual odyssey-001/002 files.

## Mechanical checks — confirmed

- **Quotation marks.** Walked every unit's `l` and `i` for opening “ / closing ” against `mark`
  and against the Greek. Found **9 speech-turns** (packet said "roughly 9"; I count exactly 9,
  more than the 7 the task prompt named by way of example): (1) Eurycleia to Penelope, 743–757;
  (2) Penelope's prayer to Athena, 762–766; (3) the unnamed suitor, 770–771; (4) Antinous,
  774–777; (5) the phantom's first speech, 804–807; (6) Penelope's long reply describing her
  grief, 810–823; (7) the phantom's second speech, 825–829; (8) Penelope's second question
  ("is he alive or dead?"), 831–834; (9) the phantom's third (evasive) speech, 836–837. Every
  speech opens “ on its first unit's `l` and `i` together with the correct `mark`, and closes ”
  on its last unit's `l` and `i`, with no stray quote marks on any narration unit in between (see
  the exhaustive per-unit table I built while checking — indices 0,2–8,9–10,13–15,17–18,
  21–32,34–36,38–45,50,52,55–61 are narration or speech-interior, all correctly unmarked). No
  fixes needed here.
- **Speech boundary at the part seam.** Confirmed against odyssey-020.json's actual last unit
  (ln 739, ending `i`: "...as well.”") that its closing ” matches a completed sentence with no
  open quote, and that 4.742 opens a brand-new reply-formula (narration, no mark/quote on ln742)
  rather than continuing a speech. Matches the task's own pre-check.
- **Internal repeats within this part.** τὴν δ' ἀπαμειβόμενον προσέφη εἴδωλον ἀμαυρόν· at 824 and
  835: `l` and `i` are verbatim identical in both units ("Her answering addressed the dim
  phantom:" / "In answer the dim phantom said to her:"). No divergence found.
- **packet.md's "already published" lines.** Checked all listed recurrences (4.768 fragment,
  4.769, 4.795, 4.814–816) word-for-word against the cited published units (odyssey-004 ln365,
  odyssey-008 ln324, odyssey-008 ln382, odyssey-020 ln724). All match exactly, including the
  correctly-truncated wording where only part of a longer published sentence recurs here (4.768).
- **House-table compliance.** Went through conventions.md's ~260-row table systematically against
  every formula/epithet this part actually uses: τὸν/τὴν δ' αὖτε προσέειπε, τὴν δ' ἀπαμειβόμενος
  προσέφη, τὸν/τὴν δ' ἠμείβετ' ἔπειτα, περίφρων Πηνελόπεια, ἀμύμων, γλαυκῶπις Ἀθήνη, ἀγορήσατο καὶ
  μετέειπε, κατὰ μοῖραν, κατὰ φρένα καὶ κατὰ θυμόν, νῆα θοήν, θεοὶ αἰὲν ἐόντες-adjacent
  νόστιμός-root, ὑγρὰ κέλευθα, αἰπὺς ὄλεθρος-root (adapted to φόνον αἰπύν, correctly noted as an
  adaptation), πολύμητις, κοίλης νηός, ὣς φάτο. Found one wording deviation (ln773's doubled
  "among them," fixed above) and the ὣς φάτο gender gap (resolved above); everything else uses
  the fixed wording verbatim.
- **Scansion.** packet.md's flag list reads "none"; re-confirmed by re-reading that section. No
  scansion irregularities to check by hand for this part.

## Summary of severities

- **High** (grammar the note gets factually backwards): 6 — ᾔδε' tense-sense (745), ὀίω
  athematic/thematic (754), and four augmented-vs-unaugmented mislabels (ἤνεικαν 784, ἔβαν 785,
  ἔειπεν 802, ἤλυθες 810).
- **Medium**: 5 — two false cross-references pointing to the wrong line for a recurring root
  (765, 774), one false cross-reference citing the wrong line for ὁρμαίνω (842), one doubled
  translation of τοῖσιν (773, `l`), and the ὣς φάτο `i`-field "said"→"spoke" fix (758).
- **Judgment calls reviewed, left unresolved for pass 2 / flagged**: πωλέ(ο) tense (810), the
  ἅψεα cross-poem formula claim (794), and the νήπιος "recurring judgment" claim (818) — none of
  these looked wrong, but none could be fully closed out without material outside this part.
- **Decided and recorded as a new house convention**: ὣς φάτο tracks natural gender; "So she
  spoke" is now the fixed fem. counterpart of "So he spoke," proposed as a new table row.
