# odyssey-025 (5.291–387): review

Reviewer, two passes over `units.json`: pass 1 covered grammar and facts, pass 2 covered translation quality. All edits were
made by script. No `t` was touched. The 53 units' `t` still reproduce Murray 5.291–387 exactly, as a
diff against the pre-review file confirms. Each `l` has the same line count as its `t`, and no `i` has a line break. No ASCII
apostrophe or backtick appears in `l`, `i`, `n` or `mark`. Every note is between 25 and 110 words.
A dry run of the build's pre-scansion checks passes: tiling, `ln`, `p` at Murray's ¶, the 5-line span and
terminal punctuation. The scanner fits all 97 lines with no UNRESOLVED or AMBIGUOUS flag.

**Changes: 40 field edits in 23 units, plus `about`, plus 2 rows of `new-renderings.md`.**
By item: error 3 (wrong augment/tense labels at 291, 295, 365) · moderate 6 (379, 333–334, 343–345 `i`, 347 `i`, 300–302 `i`, 370a `i`) · minor, all the rest.

## Structural checks

- **Paragraphs.** `p: true` falls at 291, 299, 313, 333, 339, 351, 356, 365, 377, 380 and 382. These are
  exactly the packet's ¶ marks ✓.
- **Entry from odyssey-024.** The published last unit (5.290, ἀλλ’ ἔτι μέν μίν φημι ἅδην ἐλάαν κακότητος.)
  closes Poseidon's speech with `”` in both `l` and `i`. No speech is left open into this part, and 291 is
  narration ✓.
- **Exit to odyssey-026.** The last speech here (Poseidon, 377–379) closes at 379. The part ends in
  narration (385–387, Athena's winds), so nothing runs on into 5.388. Each layer has 4 `“` and 4 `”`, so the
  validator's balance warning will not fire, and LOG.md needs no run-on note.
- **Speeches.** Each speech has `“` at the start of its first unit and `”` at the end of its last unit, in
  both `l` and `i`, and a `mark` on its first unit. No quotation marks appear outside the speeches.
  - Odysseus: 299 → 312.
  - Ino: 339 → 348–350. Murray's ¶ is at 339, after the εἶπέ τε μῦθον line.
  - Odysseus: 356 → 363–364.
  - Poseidon: 377 → 379.
- **Scansion flags.** The packet reports none ("## Scansion flags / none"), and the scanner confirms it. No
  hand-scansion was needed.
- **gloss.json.** It does not exist yet, because the Glosser has not run. The gloss check in pass 2 is
  therefore **not done**. It must be done when `gloss.json` lands. In particular, check that the entries
  for σύναγεν (impf.), ἔπεσον (augmented), ὥρμαινε (augmented) and ἀλόω (diectasis) agree with the
  corrected notes below.

## Repeated lines, checked against the shipped files

| Here | Shipped | Result |
|---|---|---|
| 365, a line inside unit 365–367 | odyssey-015 4.120 | `l` line 1 and the opening clause of `i` are identical ✓ |
| 376, a line inside unit 375b–376 | odyssey-024 5.285 | `l` line 2 and the `i` clause are identical ✓ |
| 387, a line inside unit 385–387 | odyssey-008 2.352 | `l` line 3 and the `i` clause are identical (minus the speech context) ✓ |
| 302b, a half-line inside unit 300–302 | odyssey-006 2.176, a whole unit | see the verdict below ✓ |
| 298 = 355 | internal | `l` and `i` identical ✓ |
| 321b = 372b | internal | "which heavenly Calypso had given him" in both layers ✓ |
| αἰθυίῃ ἐικυῖα 337/353; κρήδεμνον … ὑπὸ στέρνοιο τανυ- 346/373 | internal | consistent ✓ |

No unit's Greek is identical to a published unit's Greek. The validator's rule 6 key was run against every
published part, and the only substring hit is 2.176.

## Verdict on 5.300–302 (drafter's first flag): **sound, keep as drafted**

- **The published 2.176 unit.** odyssey-006, `ln` 176, `t` = `τὰ δὲ δὴ νῦν πάντα τελεῖται.` It is a mid-line
  unit and is the last unit of Halitherses' speech:
  - `l`: "and now indeed all these things are being fulfilled.”"
  - `i`: "and now, indeed, all of it is coming to pass.”"

  The drafter's account is exact.
- **Why a separate unit fails.** If 302b were cut as its own unit, validator rule 6 (`letters_only` key match)
  would force exactly that English, `”` included, into the middle of Odysseus's speech. That is a real
  quotation-mark error, so splitting is not a live option.
- **Joining across the ano teleia has precedent.** The tap-unit rule says a unit ends at `·`, but three
  shipped units already contain an internal ano teleia (odyssey-011 3.265, odyssey-016 4.274, 4.291). The
  build checks only the final character.
- **The joined unit passes the gates.** It is 3 lines, under the 5-line cap, and ends at a full stop.
- **The reused wording is preserved.** The half-line keeps the 2.176 wording in both layers, minus the `”`:
  - `l` line 3 ends "; and now indeed all these things are being fulfilled."
  - `i` ends "; and now, indeed, all of it is coming to pass."

  This is as much of the 2.176 wording as the new sentence allows.
- **Rendering.** τελεῖται is taken as a present passive, as the shipped note at 2.176 also takes it. It is
  consistent with that note, though it could be a future.
- **For QUESTIONS.md (general).** The drafter is right that `conventions.md` needs a line on this: a repeated
  published unit whose English carries a `“`/`”` that does not fit its new position. The simplest rule may
  be to have validator rule 6 compare `l`/`i` with the quotation marks stripped. That is an owner decision.
  No change was made here.

## Changes made (line · field · severity · what was wrong → what was done)

### Grammar labels in notes (pass 1)

- **291 · n · error.** σύναγεν was called "the aorist of συνάγω … without its augment". σύν-αγε-ν has
  no reduplication, and the aorist of ἄγω is (ἤ)γαγον, so this is the unaugmented **imperfect**
  (= Attic συνῆγεν). → "the imperfect of συνάγω … without its augment (Attic συνῆγεν)".
- **295 · n · error.** ἔπεσον was called "an unaugmented aorist of συμπίπτω". ἔ-πεσον carries the
  augment; the unaugmented form is πέσον, as in πέσε at 315. → "an aorist of συμπίπτω; this one keeps its
  augment, beside the unaugmented πέσε of 315".
- **365 · n · error.** ὥρμαινε was called "the unaugmented imperfect". The ω is the temporal augment of
  ὁρμαίνω, and the shipped note on this very line (4.120) says so. → "the imperfect of ὁρμαίνω …, with the
  augment lengthening ὁ- to ὠ-".
- **377 · n · minor.** ἀλόω was described as "contracted from ἀλάεο". That explains only half the form:
  ἀλάεο contracts to ἀλῶ, and ἀλόω is that contraction drawn out by diectasis. → Reworded.
- **347 · n + l · minor.** The note said "οὐδέ τι is ‘not at all’", but `l` rendered τι twice ("no fear at
  all … of suffering anything"). τι is the object of παθέειν. → The note now reads "τι is ‘anything’, the
  object of παθέειν", and `l` drops "at all". `i` was also rebuilt (see below).

Other labels were checked and are correct:
- ὀρόθυνεν (292) is an aorist. The scansion needs ῡ in the 5th foot.
- ὀρώρει is an unaugmented pluperfect.
- ἔαξεν has the syllabic augment from ϝάγνυμι.
- λύτο is a root aorist middle. The draft's parse is better than the shipped 4.703 note's "aorist passive".
- ἰδόμην, φάτο, ἔλασεν, πέσε, ἔμπεσε, ὄλοντο, ὄφελον, μερμήριξε, τάνυσσεν, κάλυψεν, ἴδε and βαῖνε are all
  unaugmented as claimed.
- ἐφάψεαι is a short-vowel subjunctive, μιγήῃς an aorist passive subjunctive, ἀρήρῃ a perfect subjunctive,
  ἐικυῖα and μεμαώς perfect participles, and ἔμμορε and εἵμαρτο from μείρομαι.
- ἐβάρυνε is left as "aorist". The ῡ fits either tense, and aorist is the standard reading.

### Position claims and cross-references (pass 1): all checked, no change needed

- **Position claims:** Ζεύς at the head of 304; ἄμβροτον alone at the head of 347; the name-formula closing
  354; ἀθανάτων held over to 357; πικρήν into 323; καρφαλέων into 369; ἔνθα καὶ ἔνθα at the end of 330.
  All ✓.
- **Cross-references:** 4.703 (the same λύτο γούνατα καὶ φίλον ἦτορ, of Penelope) ✓; 5.207 κήδε’ ἀναπλῆσαι ✓;
  1.11/1.37 αἰπὺς ὄλεθρος ✓; 4.562 πότμον ἐπισπεῖν "to meet your fate" ✓; 5.255 steering-oar ✓; 5.254
  yard ✓; 5.264 clothes ✓; 5.248 ἁρμονίῃσιν "joinings" ✓; 1.6 ἀλλ’ οὐδ’ ὥς ✓; 1.62 ὠδύσαο pun ✓; 1.20
  μενέαινεν ✓; 1.74 Zeus on Poseidon ✓; 5.279–281 the mountains ✓; 5.175 "dread and grievous" ✓; 5.282
  Poseidon unnamed ✓; 5.290 κακότητος ✓.
- **new-renderings precedents:** 3.295 "South Wind" ✓; 2.421 "West Wind" ✓; 4.515 θύελλα "storm-blast" ✓;
  3.283 "storm-blasts" / 3.320 "storms" for ἄελλα ✓; 3.392 κρήδεμνον "covering" ✓; 1.262 "bronze-fitted" ✓;
  2.61 λευγαλέοι "feeble" ✓; 4.30/4.332 "greatly vexed" ✓; 2.93, 4.437, 4.452 δόλος "trick" ✓; 4.372
  "suffering pains" ✓; 1.34 "pains have" ✓; 3.91 "open sea" ✓.

### Translation: Greek → `l`, and `l` ↔ `i`

- **300–302 · l · minor.** "who said **to me** that … I would fill up" rendered μ’ twice. μ’ = με is the
  subject of ἀναπλήσειν. → "who said that I, on the open-sea, before reaching my fatherland, / would fill up
  my pains;". The 2.176 half-line is unchanged.
- **379 · l, i, n · moderate.** `l` "to find fault with your evil" reads in English as "you won't complain",
  which reverses the sense. The `i` "find your share of evil too small" gave a different sense again, so the
  two layers disagreed. LSJ s.v. ὄνομαι, c. gen., cites this very line as "make light of". Changes:
  - `l` → "to make light of your evil".
  - `i` → "I do not expect you will think your evil a small thing".
  - The note now gives both readings honestly: 'will not be able to call it small' (followed in the English)
    or the ironic 'no cause to complain of too little'. The drafter's version picked the ironic reading in
    `i` and in the note but not in `l`.
- **351 · l, i · minor.** The note says she "dived" where before she "rose", but both layers said "plunged".
  → Both now say "dived". `i` "the surging sea" was also rebuilt as "the sea as it swelled with waves",
  following the note's gloss of κυμαίνοντα.
- **315 · i · minor.** "He himself was flung" put an agent into πέσε. → "fell", which matches `l`.
- **339 · l, i · minor.** `l` "so / come-to-hate you, so terribly" doubled ὧδε. → "so / come-to-hate you,
  terribly". `i` "so many evils" added "so" to κακὰ πολλά. → "many evils".
- **365 · l, i · minor.** "arching over" drifted from κατηρεφές 'roofed over', which the note glosses. → `l`
  "roofed over", `i` "roofing him over".
- **370b · l · minor.** "bestrode" became "went astride", following the note. "as if riding" became "like one
  driving", following the note's ἐλαύνων 'driving'.
- **377 · i · minor.** "suffering many evils" lost the aorist παθών. → "with the many evils you have
  suffered".
- **385 · l, i · minor.** "before him" became "ahead of him", matching the note. The old wording was also
  close to remembered wording (see below).
- **about · minor.** It said the wave "snaps the mast". At 316–317 it is the θύελλα, not the wave. →
  "a squall snaps the mast, and he is held under".

### Remembered English in `i` (and `l`), rebuilt from the grammar

These phrases matched, or came close to, the wording of Murray's 1919 English as I recall it. Murray is a
silent meaning-check only, and the rule is the same one the odyssey-024 review applied.

- **333–334 · l, i, n · moderate.** βροτὸς αὐδήεσσα "a mortal of human speech" is, as far as I recall,
  Murray's wording verbatim, and the drafter fixed it as a new house rendering. → `l` "a mortal endowed with
  speech" (the formation αὐδή + -εις), `i` "a mortal, speaking with a human voice". The note was reworded
  to match. **The row in `new-renderings.md` was amended accordingly.**
- **343–345 · i · moderate.** "swim with your hands and strive to reach the land of the Phaeacians, where it
  is your fate to escape" was close to Murray throughout, and it also dropped νόστου. → "and, swimming with
  your hands, strive for a homecoming to the land of the Phaeacians, where your portion is to escape."
- **347 · i · moderate.** "there is no fear that you will suffer any harm, or perish" was close to Murray. →
  "then you need have no fear of coming to any harm, or of being lost."
- **300–302 · i · moderate.** The construction "…was unerring, when she told me that out on the sea, before I
  reached my fatherland, I would fill up the full measure of my pains" followed Murray's line almost clause
  for clause. → "I fear that all the goddess said was unerring, she who told me I would fill up my pains to
  the full out on the sea, before ever I reached my fatherland;". The 2.176 tail was kept exactly.
- **370a · i · moderate.** "so the wave scattered the long timbers of the raft" is essentially Murray. →
  "so were the raft’s long timbers scattered." This also keeps the Greek's unstated subject.
- **331–332 · i · minor.** "Now the South Wind would toss it … and now the East Wind would yield it to the
  West Wind to …" followed Murray's frame. → "At times … would toss it over to the North Wind to be carried,
  at times the East Wind would give it up to the West Wind to chase."
- **299 · l · minor.** "what now is to befall me at the last?" was close to Murray. → "what now will happen
  to me in the end?", which matches `i`'s "in the end" and the note's gloss of μήκιστα.
- **311 · l, i · minor.** "the Achaeans would be spreading my fame" was close to Murray. → "carrying my fame
  abroad", the note's own gloss of κλέος ἄγειν.
- **313 · i · minor.** "whirled the raft around" became "spun the raft about". `l` keeps "whirled", the
  literal ἐλελίζω.
- **341 · i · minor.** "for all his raging" became "however much he rages".
- **353 · i · minor.** "and the dark wave hid her" became "covered her", matching `l`.
- **356 · i · minor.** "leave the raft" became "step off the raft", matching `l` and ἀποβῆναι.
- **363 · i · minor.** "shakes the raft to pieces" became "shakes my raft apart", matching `l` and μοι.

### Marks

- **299, 356, 377 · mark · minor (consistency).** The draft had "Odysseus speaks to his own heart" twice and
  "Poseidon speaks to his own heart". odyssey-024 shipped "Poseidon speaks to himself" at 5.286 for the
  identical κινήσας … θυμόν formula. That is the only shipped precedent for a self-address mark. → All
  three are now "… speaks to himself". The θυμός is already carried by the formula line in `l`/`i`. A
  stage direction should read the same wherever the situation is the same, and all three are speeches to
  oneself.

## The drafter's other flags: judged

- **κρήδεμνον "head-veil": sound, kept.** It is literal to the formation (κάρη + δέω). It is distinct from
  καλύπτρη "veil" (5.232), and no καλύπτρη occurs in this part. It is used identically at 346, 351 and 373
  in both layers. The row omitted one fact, and I added it to the row: shipped 1.334 already renders
  Penelope's λιπαρὰ κρήδεμνα as "veil", and 4.623 καλλικρήδεμνοι as "fair-veiled". "Head-veil" is compatible
  with both, so no conflict arises, but the publisher should know that "veil" has already done service for
  κρήδεμνον once.
- **ἄελλα "blast" / θύελλα "storm-blast": sound, kept.** They are kept apart throughout: ἄελλα at 292 and
  304, "blasts" in both layers; θύελλα at 317, "storm-blast". The notes gloss them differently ('blast,
  gust' vs 'storm-blast, squall'). Shipped usage had already blurred the two: ἄελλα was "storm-blasts" at
  3.283 and "storms" at 3.320, and θύελλαι was "storm-winds" at 4.727. The row discloses this. Fixing the
  pair from here on is an improvement.
- **αἰθρηγενέτης (296): honest.** Both readings are given, passive and active. **αἴθυια (337): honest.**
  The note says "whose kind is not known" and names three candidates. The English "shearwater" follows the
  φήνη "sea-eagle" precedent (table row 273). **Αἰγαί (381): honest.** The note says "which of several
  places … is not certain". **αὐδήεσσα: honest,** with the note reworded as above.
- **ἤλασε subject (367): honest.** The note says "may be Poseidon or the wave". **δεινόν (314): honest.**
  The note reads "agrees with κῦμα, though it can also be taken as an adverb". **σύν (293): honest.** The
  note gives adverb or tmesis. περί at 314 is handled the same way.
- **ὀνόσσεσθαι κακότητος (379).** See the changes above. The draft's note flagged a debate, but its `l` and
  `i` took different sides of it. It is now consistent and states both readings.
- **Odysseus naming Zeus (304).** The note states this without "correcting" him. Kept.

## Considered and left as drafted

- **308 · l, i · "Would that I too / If only I too".** γε emphasises ἐγώ and does not strictly mean
  "too". The "too", however, is the contextual sense: "I, like those Danaans". It stays as a defensible
  reading in both layers, which agree with each other.
- **Forced literal overlaps with Murray,** left because the Greek or a fixed house rendering allows almost
  nothing else:
  - "which heavenly Calypso had given him" (321/372, a new house row)
  - "had died and met my fate on that day when" (308; πότμον ἐπισπεῖν is fixed at 4.562)
  - "roused a great wave against him, dread and grievous" (366; house wording)
  - "shaking his head he spoke to his own heart" (376; shipped repeat)
  - "until Zeus-born Odysseus should come among" (387; shipped repeat of 2.352)
  - "stretched the head-veil beneath his chest" (373)
  - "not lacking in sense" (342, the litotes of οὐκ ἀπινύσσειν)
  - "this way and that" (327/330; common English, and different from Murray's structure there)
- **377 · i "come among Zeus-nurtured men".** This is the natural sense of μίγνυμι + dat. and matches 386.
  Left.
- **368 · i ends with a comma where `l` has `;`.** The unit is the first half of a simile that finishes in
  369. The comma is better English. Left.
- **373 · i "plunged headlong" for κάππεσε "fell".** It is a legitimate idiom for falling headlong into
  water, and `l` keeps "fell". Left.
- **τελεῖται (302) as present passive.** It could be future, but the parse matches the shipped 2.176 note.
  Left.
- **The other rows in `new-renderings.md`** are consistent with the table and the shipped precedents, as
  checked above: the four winds, δυσαής, ὀπωρινός, κραιπνός, ζαής, καλλίσφυρος, ἄμβροτος "deathless",
  αἰθυίῃ ἐικυῖα, εἶπέ τε μῦθον, τρὶς μάκαρες, χαλκήρεα, Πηλεΐων, λευγαλέος, τέλος θανάτου, μέλαν κῦμα,
  δόλον ὑφαίνειν, φιλήρετμοι, διοτρεφέες, the 382 line, κλυτὰ δώματα, ἄλγε’ ἔχοντα / ἄλγεα πάσχων,
  ἱμάσσω, πέλαγος, the 297 and 298 formulas, the cries, and the 342/360 pair.

## For QUESTIONS.md / the publisher

1. Repeated published units that carry a speech mark which does not fit a new position (2.176 → 5.302b).
   Consider a `conventions.md` line, or letting validator rule 6 compare English with “ ” stripped.
2. Self-address `mark` wording is now "X speaks to himself" in three parts' worth of speeches. Consider
   fixing it in `conventions.md`, next to the `mark` rule.
3. κρήδεμνον: "head-veil" from here on. Shipped 1.334 "veil" and 4.623 "fair-veiled" stand as shipped, and
   the row now records them.
4. The glossary stage (not yet run) must parse σύναγεν as an imperfect, ἔπεσον as augmented, ὥρμαινε as
   augmented, ὀρόθυνεν as an aorist and ἀλόω as diectasis. The reviewer's pass-2 gloss check is still owed.
