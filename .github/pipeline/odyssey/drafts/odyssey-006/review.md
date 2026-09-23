# Review: odyssey-006 (Odyssey 2.103–207)

Reviewed against `conventions.md`, `packet.md`, `new-renderings.md`, and the relevant units of the
published `odyssey-003/units.json`, `odyssey-004/units.json` and `odyssey-005/units.json` (all lines
this part claims as repeats, plus the odyssey-005 closing-unit model for an open speech). `gloss.json`
does not exist yet, so this run is Pass 1 (translation) only, done twice as the runbook requires: a
first structural/mechanical pass, then a second sense/wording pass. **63 units, all read.** I verified
by script that the concatenated `t` reproduces `packet.md` exactly (no `t` was touched) and, after my
edits, that every `l`'s `\n` count equals its `t`'s and no `i` contains `\n`.

**28 findings, 26 units edited** (27 field changes: 3 `l`, 24 `n`; two units — 2.122 and 2.196 — each
bundle two findings into a single note edit). No `t` field was touched. Severity: **0 error, 9 moderate,
19 minor** (see tables below; the two mandated mechanical newline defects are counted as moderate, since
each broke the build's tiling check). Seven further findings were considered and refused, listed at the
end, with reasons.

## Mechanical (given; verified and fixed)

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 121 | `l` | moderate | `t` has one `\n` (2 lines: "…Πηνελοπείῃ" / "ᾔδη·"); `l` had none. | Split `l` to match: "of these, none — thoughts like Penelope's —\nknew;" — the dash keeps the object (translating line 1) set off from the verb ᾔδη (translating line 2), the split the tiling check requires. |
| 182 | `l` | moderate | `t` has two `\n` (3 lines: "αὐτὰρ Ὀδυσσεὺς" / "ὤλετο…ἐκείνῳ" / "ὤφελες."); `l` had one. | Rewrote to 3 lines: "but Odysseus\nhas perished far away, and I wish that you too, along with him,\nhad perished." Also corrected the final punctuation to a period, matching `t`'s "ὤφελες." (the draft had ended the line on a comma). |

Re-verified after both fixes: every unit's `l` now has exactly the same `\n` count as its `t` (63/63).

## Pass 1: other changes to `units.json`

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 106 | `n` | moderate | ἔληθε and ἔπειθεν were called "unaugmented imperfects" with "Attic ἐλάνθανε, ἐπείθεν" as if Attic added an augment Homer drops. Both forms already carry the augment ἐ- (ἔπειθεν = Attic ἐπείθεν, identical); the real difference for ἔληθε is not augment but stem (Homer's simplex λήθω vs. Attic's λανθάνω). | Rewrote to identify ἔληθε as the (augmented) imperfect of the epic by-form λήθω, and ἔπειθεν as a normally augmented imperfect of πείθω — removing the false "unaugmented" claim. |
| 130 | `n` | moderate | ἔτεχ’ (= ἔτεκε) was called "an unaugmented aorist of τίκτω". The ἐ- in ἔτεκε *is* the augment (Homer's unaugmented form would be τέκε, as conventions.md's own example shows). | Corrected to "an aorist of τίκτω with the regular augment ἐ- (elided and aspirated to χ before the rough breathing of the next word)". |
| 157 | `n` | moderate | "γέρων 'old' and ἡώς 'the hero'" — ἡώς means 'Dawn'; the word actually in the line, and in the house table, is ἥρως 'hero'. | Corrected ἡώς → ἥρως. |
| 161 | `n` | moderate | Claimed this line "opened Antinous's speech in the previous part (2.85)". Checked against odyssey-005/units.json: the line at 2.85 is a different line (Τηλέμαχ’ ὑψαγόρη…, mark "Antinous answers"). "κέκλυτε δὴ νῦν μευ…" instead recurs from 2.25, marked "Aegyptius speaks" — matching packet.md's own repeat table ("2.161 = a line of odyssey-005, unit at line 25"), which the drafter's `l`/`i` (already verbatim-correct) evidently used but the note misattributed. | Rewrote the note to cite 2.25 and Aegyptius correctly. |
| 196 | `n` | moderate | Asserted as settled fact that ἔεδνα are "the gifts a bridegroom's side traditionally brought". Both odyssey-003's own note on this identical, reused line and odyssey-005's note on ἐεδνώσαιτο (2.52–54) explicitly flag the direction of these gifts as long disputed among lexicographers — this note quietly overrode that acknowledged uncertainty. | Restored the disputed status, with cross-references to both earlier notes, matching the sole-source convention's rule that disputed points are stated as disputed, not papered over. |
| 171 | `l`, `n` | moderate | new-renderings.md proposes `l` "many-counselled" for πολύμητις — but the house table already assigns "of the many counsels" as the fixed **`i`**-rendering of the separate epithet πολύφρων (also of Odysseus). Given the table's explicit stated practice of keeping the three -φρων epithets of Odysseus distinct, letting πολύμητις's `l` echo πολύφρων's `i` risks exactly the conflation that practice exists to prevent. | Changed the unit's `l` from "many-counselled Odysseus" to "many-wiled Odysseus" (still literal, still visibly built on μῆτις, and clear of πολύφρων's territory); rewrote the note to state the distinction explicitly. **I could not edit new-renderings.md itself** (out of scope for this review) — flagged below for whoever ratifies that file. |
| 132 | `n` | moderate (cross-ref) | Cited the tmesis of ἀπό … πέμψω as met "already at 1.8–9 in the pilot" — but 1.8–9 is conventions.md's own example of tmesis with **κατά** (κατὰ … ἤσθιον), not ἀπό. | Reworded to correctly attribute the 1.8–9 example to κατά, keeping the (valid) general point that this is the same phenomenon. |
| 107 | `n` | minor (scope) | "ὧραι … returns at the poem's next mention of time passing" asserts something about content beyond this part, which this part cannot show (the convention: "A note asserts nothing about the rest of the poem that this part cannot show"). ὧραι does not recur anywhere else within 2.103–207 either. | Removed the forward-looking claim; kept the gloss. |
| 119 | `n` | minor (line + scope) | "of the nymph at 1.85" — the actual line is 1.86 (checked against the source text). Also claimed ἐυπλόκαμος is "already fixed in the house table" — it is not: conventions.md's table has no entry for it (it appears once, in odyssey-001's own `l`, and was never re-used, so it was never promoted to the table). | Fixed the line number to 1.86 and reworded to say it was used there (not "fixed in the house table"). |
| 122 | `n` | minor (line position) | "ἐνόησε answers νοήματα two lines above" — νοήματα is in the line immediately before (2.121), one line above, not two. | Changed to "in the line before". |
| 127 | `n` | minor (line position) | "γαμέεσθαι at 2.114" — γαμέεσθαι is in 2.113 (checked against packet.md). | Corrected 2.114 → 2.113. |
| 137 | `n` | minor | "with the next unit's εἰ δέ" — the next unit actually opens ὑμέτερος δ’ εἰ μέν, not εἰ δέ. | Reworded to "the conditional clause that opens the next unit", removing the wrong exact wording. |
| 150 | `n` | minor (terminology) | "ὄσσομαι … used absolutely with ὄλεθρον as its object" is self-contradictory — "absolutely" means used *without* an object. | Removed "absolutely"; the verb simply takes ὄλεθρον as its object here. |
| 122 | `n` | minor (typo) | αῖσα is missing its breathing mark (should be αἶσα, smooth breathing + circumflex on the diphthong). | Corrected the diacritic. |
| 163 | `n` | minor (typo) | "ὦν is the possessive…" — the word in `t` is ὧν (rough breathing, from ὅς/ἥ/ὅν); ὦν as written is not that word. | Corrected ὦν → ὧν. |
| 129 | `n` | minor (citation) | "its earlier appearance in odyssey-004 (2.129)" repeats *this* part's own line number instead of citing where it appeared in odyssey-004 (1.388, per that unit's own `ln` and packet.md's repeat table). | Corrected citation to (1.388). |
| 138 | `n` | minor (citation) | Same pattern: "(2.140, odyssey-004)" instead of the actual location, 1.374. | Corrected to (1.374, odyssey-004). |
| 141 | `n` | minor (citation) | "(2.142)" instead of 1.376. | Corrected to (1.376). |
| 143 | `n` | minor (citation) | "(2.144)" instead of 1.378. | Corrected to (1.378). |
| 145 | `n` | minor (citation) | "(2.145)" instead of 1.380. | Corrected to (1.380). |
| 177 | `n` | minor (citation) | "(2.177)" instead of 1.399. | Corrected to (1.399). |
| 196 | `n` | minor (citation) | "(2.196–197)" instead of 1.277 (folded into the same edit as the ἔεδνα fix above). | Corrected to (1.277). |
| 146 | `n` | minor (cross-ref) | "ὣς φάτο … as at 1.42 of the pilot" — 1.42 actually reads ὣς ἔφαθ’ Ἑρμείας (augmented, named), not the bare formula ὣς φάτο being illustrated. | Replaced with a verified citation: the bare formula's own two occurrences in the immediately preceding part (2.35, 2.80). |
| 181 | `n` | minor (word identification) | "The epic τε in φοιτῶσί τε and πάντες τε" — the τε particles in this couplet actually attach to δέ (line 181) and οὐδέ (line 182), not to φοιτῶσι or πάντες directly. | Reworded to "δέ τε (181) and οὐδέ τε (182)". |
| 193 | `n` | minor (line position) | "the threat … begun two units before" — the threat against Halitherses (σοὶ δέ, γέρον, θωὴν ἐπιθήσομεν…) begins in the immediately preceding unit (2.192), one unit before, not two. | Changed to "the unit before (2.192)". |
| 205 | `n` | minor (line position) | "ἐριδαίνεμεν, the infinitive noted in the pilot's closing line" — ἐριδαίνεμεν is at 1.78–79 (checked against odyssey-001/units.json); the pilot's actual closing line is 1.93–95 and is unrelated. | Corrected to "already noted in the pilot (1.78–79)". |

## Pass 1: verified and confirmed without change

- **Speech boundaries**, all checked against `mark`/quotation placement:
  - 2.103 (Antinous's speech continuing from odyssey-005): correctly carries **no** `mark` and **no**
    opening “ — confirmed against odyssey-005's own closing unit (2.102), whose note states the outer
    speech stays open, and against the model wording there for how to describe an open speech.
  - 2.127: closing ” on both `l` and `i`, immediately before the reply-formula at 2.129 (no mark/quote
    on 2.129 itself, correctly narration-only).
  - 2.130: opening “ + `mark: "Telemachus replies"`.
  - 2.145: closing ” (end of Telemachus's speech), before the narrative eagle-omen scene (no speech).
  - 2.161: opening “ + `mark: "Halitherses speaks"`, immediately after the reply-formula at 2.177... (i.e. before it, at 161, after the 157–160 narration) — confirmed correctly placed.
  - 2.176: closing ” (end of Halitherses's speech), before the reply-formula at 2.177.
  - 2.178: opening “ + `mark: "Eurymachus replies"`.
  - 2.205 (last unit): **no** closing ”, and the note states plainly, in wording matching the model set
    by odyssey-005's own final unit ("Antinous' speech goes on into the next part, and has no closing
    mark within this one"), that "Eurymachus's speech is left open here: it runs on without a break
    into the next part, and the closing ” is not given." Confirmed this is the intended model and needs
    no change.
- **`p` (paragraph) flags**: exactly on 103, 129, 146, 161, 177 — matching every ¶ in packet.md and
  nothing else.
- **Line-repeats against published parts**, all checked character-for-character against the primary
  files (not just packet.md's copies):
  - 2.129 = odyssey-004 (Book 1, `ln` 388): `l`/`i` identical. ✓
  - 2.140 (line-internal repeat within a larger unit) = odyssey-004 (`ln` 374): the shared portion of
    `l`/`i` ("see to other feasts,\neating your own possessions, taking turns through your houses." /
    "and go and hold your feasts elsewhere, eating up what is your own, moving from house to house in
    turn.") is reused verbatim as far as the unit's own boundaries allow. ✓
  - 2.142 = odyssey-004 (`ln` 376): `l`/`i` identical. ✓
  - 2.144 = odyssey-004 (`ln` 378): `l`/`i` identical (note already correctly flags the ano-teleia/full-stop
    difference in `t` as immaterial). ✓
  - 2.145 = odyssey-004 (`ln` 380): `l`/`i` identical. ✓
  - 2.161 = odyssey-005 (`ln` 25): `l`/`i` identical (the note's misattribution of speaker/line, fixed
    above, did not affect the actually-correct `l`/`i`). ✓
  - 2.177 = odyssey-004 (`ln` 399): `l`/`i` identical. ✓
  - 2.196–197 = odyssey-003 (`ln` 277): `t`, `l` and `i` all identical. ✓
- **House-table formulas**, checked at every occurrence against conventions.md's table: πεπνυμένος
  (129, of Telemachus, "prudent"); the four reply-formulas (τὸν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα
  129; τὸν δ’ αὖτ’ Εὐρύμαχος Πολύβου πάϊς ἀντίον ηὔδα 177); ὦ γέρον (178, 192); ἀγορήσατο καὶ μετέειπε
  (160); κέκλυτε δὴ νῦν μευ, Ἰθακήσιοι, ὅττι κεν εἴπω (161, verified against odyssey-005 as above); θεοὶ
  αἰὲν ἐόντες / θεοὺς … αἰὲν ἐόντας (143); ἥρως as title (157, after the typo fix); μνηστῆρες ἀγήνορες
  is not itself repeated here but its adjective ἀγήνωρ recurs at 103, correctly noted as related rather
  than claimed as the same formula.
- **new-renderings.md's 7 proposed entries**, checked against the table for collisions:
  ἐυπλοκαμῖδες, ἐυστέφανος, ἐυδείελος, εὐρύοπα Ζεύς, υἷες Ἀχαιῶν and μνηστὺς ἀργαλέη collide with
  nothing in the fixed table and are properly distinguished from their nearest neighbours (κραναὴ
  Ἰθάκη / ἀμφίαλος Ἰθάκη for ἐυδείελος; νεφεληγερέτα Ζεύς for εὐρύοπα Ζεύς; μνηστῆρες ἀγήνορες for
  μνηστὺς ἀργαλέη). **πολύμητις** did need a fix — see the table above (its `i` "of many wiles" is fine
  and distinct from πολυμήχανος's avoided-list entry of the same words, which the table reserves rather
  than bans; but its proposed `l` collided with πολύφρων's `i` and was changed in the one unit that uses
  it, per above).
- **Scansion.** packet.md says "none" flagged. I read every line for an obvious irregularity (unresolved
  short vowels before mute+liquid, suspicious hidden quantities, etc.) without running the scansion
  script; nothing stood out as a genuine metrical fault. In particular 2.146's αἰετὼ εὐρύοπα (hiatus
  without elision across a dual ending) is normal epic correption, not an irregularity worth a note. No
  unit's note claims a metrical irregularity, correctly matching the "none" flag.
- **Remembered English.** I read every `i` against the list of in-copyright translations to avoid
  (Lattimore, Fagles, Fitzgerald, Lombardo, Mandelbaum, Rieu, Mitchell, Verity, Green, Wilson,
  Mendelsohn) and found no phrase that reads as recalled rather than built from the case relations.
- **Article/pronoun and possessive/relative labelling** spot-checked throughout (τάων 121, τό 110, σῷ
  111, ὅτεῳ 113, ὅν 116, ᾧ 127, μιν 172, ὧν 163, ὅν 195) and found correct in every instance except the
  ὦν/ὧν typo already fixed.

## Pass 1: findings considered and refused

- **ASCII vs typographic apostrophe (`'` vs `’`) in `l`/`i`/`n`.** This part mixes both (320 ASCII, 21
  typographic instances). odyssey-005's review already raised this as a corpus-wide, unresolved
  question (house practice is split across parts) and declined to normalize case-by-case. I follow that
  precedent and leave it, restating the open question below rather than editing 300+ instances on my
  own authority.
- **ἐπεπείθετο at 2.103, called "built on the perfect stem of πείθω with the augment... functions as a
  plain imperfect."** On first read this looked like the same class of error as the ἔληθε/ἔπειθεν and
  ἔτεχ’ mislabels. On closer check it is not: the middle/passive perfect of πείθω is built on the stem
  πε-πειθ- (πέπεισμαι), and Homer's ἐπεπείθετο is the known case of a perfect/pluperfect middle taking a
  secondary *thematic* ending (-ετο) by analogy with the imperfect, rather than the expected athematic
  -το (which would give ἐπέπειστο). The note's description, though it avoids naming the tense outright,
  is accurate to this. Left unchanged.
- **ἐπήλυθον at 2.107, called "an unaugmented aorist… (Attic ἐπῆλθον)."** Epic ἤλυθον/ἐπήλυθον is a
  separate thematic formation from the root aorist ἦλθον/ἐπῆλθον, and by the standard grammars' account
  it genuinely lacks the augment that the Attic root aorist shows. Distinguished this from the two real
  augment errors found (2.106, 2.130) and left it.
- **new-renderings.md's own text**, not just the unit that cites it. Two of its own claims mirror errors
  I fixed in units.json: the ἐυπλοκαμῖδες row's "the fixed ἐυπλόκαμος 'fine-plaited' in the house table"
  (ἐυπλόκαμος is not in the table — see the 2.119 fix above), and the πολύμητις row's proposed `l`
  "many-counselled" (the collision fixed at 2.171). I could not edit new-renderings.md itself — out of
  scope for this review, which is confined to `units.json` and this file — so both are flagged here for
  whoever ratifies that file, rather than silently left.
- **"θεοὺς … αἰὲν ἐόντας" at 2.143 closing with a full stop where its earlier appearance (odyssey-004,
  1.378) closes with an ano teleia.** The drafter's own note already states this and correctly judges it
  immaterial (the content is identical; only the terminal mark in `t` differs, and `t` is untouchable).
  Confirmed and left as is.
- **Duplicate `ln` values** (two consecutive units both stamped `"ln": 163`, and elsewhere similar).
  Checked against precedent in odyssey-005 (e.g. two consecutive units both at `ln` 28, others at 33 and
  60): this is the established, correct pattern whenever a second tap-unit begins mid-line, since `ln`
  is "the line the unit starts on" and both units start on the same physical verse line. Not an error.
- **γαμέεσθαι/γήμασθαι used only of the woman, ὀπυίω only of the man** (2.113, 2.127, 2.205). Checked
  against each other and against conventions.md; consistent throughout the part. Left as is.

## For QUESTIONS.md

1. ASCII vs typographic ’ in `l`/`i`/`n` across the corpus (restated from odyssey-005; still open, now
   also true of odyssey-006).
2. new-renderings.md's two inaccuracies noted above (ἐυπλόκαμος wrongly described as already in the
   house table; πολύμητις's proposed `l` "many-counselled" collides with πολύφρων's `i`) should be
   corrected in that file before ratification, alongside the fix already made to the one unit that uses
   the word.
3. ἐυπλόκαμος itself (Calypso's epithet, odyssey-001 1.86, rendered "fine-plaited" there) has never been
   promoted to the house-renderings table despite being exactly the kind of recurring-type epithet the
   table exists for — worth a maintainer decision on whether to add it now that a cognate word
   (ἐυπλοκαμῖδες) has drawn attention to it.
