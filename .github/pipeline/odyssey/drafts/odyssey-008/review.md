# Review — odyssey-008 (Odyssey 2.321–434), pass 1 (translation review)

Reviewer pass over `units.json` and `new-renderings.md`. Edits were made directly in
`units.json` (and none were needed in `new-renderings.md`, which checked out). Severity
vocabulary: **error** (factually wrong / breaks a hard rule) · **major** (a real, user-facing
mistranslation or systemic omission) · **moderate** (a real but contained inaccuracy)
· **minor** (a defensible-but-improvable choice).

## Verifications performed first (all passed)

- **Repeated-line reuse**, checked character-for-character against the actual published
  JSON, not just against packet.md's own quotation of them:
  - 2.347 (`Εὐρύκλει', Ὦπος θυγάτηρ Πεισηνορίδαο.`) — matches odyssey-004.json's unit at
    `ln:428` (the line itself is the second line of that 4-line unit) word for word, and the
    shipped `l`/`i` are reused verbatim. Confirmed.
  - 2.359 (`εἶμι γὰρ ἐς Σπάρτην τε καὶ ἐς Πύλον ἠμαθόεντα`) — matches odyssey-007.json's
    unit at `ln:214` word for word; only the shared first line's `l` is reused (correctly
    limited, since the following line differs). Confirmed.
  - 2.371 (`τὴν δ' αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα·`) — matches odyssey-003.json's
    unit at `ln:213` exactly, `l`/`i` identical. Confirmed.
  - 2.401 (`Μέντορι εἰδομένη ἠμὲν δέμας ἠδὲ καὶ αὐδήν,`) — matches odyssey-007.json's unit
    at `ln:267` (the line itself is the second of that 3-line unit, i.e. actually book-line
    268 — see note below); `l` reused verbatim with only the terminal punctuation changed
    from comma to colon, as the note says. Confirmed.
- **Πεισηνορίδαο / "Peisenor's grandson" analysis**: confirmed correct. Πεισηνορίδης
  "son of Peisenor" is a patronymic in agreement with Ὦψ (nom. Ὦψ, gen. Ὦπος), not with
  Εὐρύκλεια. So the Greek says Ops was Peisenor's son; Eurycleia, as Ops's daughter, is
  Peisenor's **granddaughter**, not "grandson" (wrong gender either way). The shipped
  odyssey-004 `l` is indeed backwards, and per the repeated-line rule it cannot be
  corrected in `l` here. The unit's note at line 345 already states this clearly and
  correctly for a reader (identifies the agreement, states the correct relationship,
  explains why the wording is nonetheless kept, and confirms `i` already reads correctly).
  **No edit needed** — the note was adequate as drafted.
- **Speech-boundary continuity at the 007/008 seam**: odyssey-007.json's last unit
  (`ln:320`) closes with `”` on both `l` and `i` ("...course."”). odyssey-008's first unit
  (`ln:321`) opens with plain narrative (ἦ ῥα, καὶ...), no unmatched quotation mark, and
  correctly treats the just-finished speech as already closed. No speech left open across
  the boundary.
- **`t`-tiling**: programmatically joined all 71 units' `t` in order and diffed against
  packet.md's 114 lines (both whitespace-normalized). The only differences are the single
  interword spaces lost at unit boundaries that split mid-line — the identical pattern
  already present in the shipped odyssey-003/004/007 files at their own mid-line splits
  (e.g. odyssey-007 `ln:214`/`215` boundary). No word was dropped, added or moved. All 114
  lines (321–434) are covered exactly once, with no gaps or overlaps, and the 15 `p:true`
  paragraph flags match Murray's 15 `¶` marks in packet.md exactly.

## Findings and fixes

### 1. Missing quotation marks on every one of the 7 speeches — **major**
`conventions.md` requires "“ ”" quotation marks in the English layers around every speech
(the Greek carries none, but `l`/`i` must). Despite all 7 `mark` cues being correctly
placed (325, 331/332, 349, 363, 371/372, 402, 410), **not a single `“` or `”` appeared
anywhere in the entire draft** — `l` and `i` for all 71 units. This is a part-wide,
systemic omission, confirmed by grepping the whole file for the two curly-quote
characters (zero hits) before editing.

Fixed by adding `“` to the start of `l` and `i` on the first unit of each of the 7
speeches, and `”` to the end of `l` and `i` on the last unit of each:
- Suitor 1 (325–330): open at `ln 325`, close at `ln 328`.
- Suitor 2 (331–336): open at `ln 332`, close at `ln 335`.
- Telemachus to Eurycleia (349–360): open at `ln 349`, close at `ln 359`.
- Eurycleia's lament (363–370): open at `ln 363`, close at `ln 369`.
- Telemachus's reply (372–376): open at `ln 372`, close at `ln 373`.
- Athena-as-Mentor (402–404): open at `ln 402`, close at `ln 404`.
- Telemachus to comrades (410–412): open at `ln 410`, close at `ln 411`.

Placement and format (quote directly abutting the first/last word, no extra space) were
matched against the established pattern in odyssey-007.json's own speech-opening and
-closing units.

### 2. Recurring augment/no-augment mislabeling — **major** (pattern), 4 instances fixed
The task flagged this as a known recurring drafter weakness, and it recurred here. Four
notes asserted a form was "unaugmented" when it in fact *shows* the regular augment
(and, in most cases, the genuinely unaugmented sibling form is directly attested
elsewhere, including within this very part or within this very table):

- **363, `ἔπλετο`** — claimed "an unaugmented aorist." In fact ἔπλετο carries the ordinary
  augment (ε- + root πλ-); Homer's unaugmented sibling is πέλετο/πέλεν (Autenrieth cites
  both). Fixed: note now says it carries the augment and is not an instance of the
  no-augment pattern.
- **365, `ὤλετο`** — claimed "another unaugmented aorist." In fact it shows the regular
  augment (ὀ- lengthened to ὠ-); the unaugmented form keeps the omicron, ὄλετο/ὄλοντο —
  the very ὄλοντο already cited in conventions.md's own table note at Odyssey 1.7. Fixed.
- **377, `ἀπώμνυ`** — claimed "an unaugmented imperfect." In fact the compound shows the
  augment fused in (ἀπο- + augment ἐ- + stem ὀμνυ-, ο→ω). Fixed, with the real
  explanation (and the syncopated final -ε) substituted.
- **395, `ἔχευε`** — claimed "an unaugmented imperfect," in the very same note that
  correctly cross-references the *actually* unaugmented χεῦον/χεῦεν used earlier in this
  same part (354, 380) — i.e. the note's own cross-reference contradicts its own claim.
  ἔχευε carries the augment (ἐ- + stem χευ-). Fixed.
- Also checked and additionally fixed: **407, `κατήλυθον`** — claimed "an unaugmented
  aorist." The η here is not a droppable augment (Attic κατῆλθον shows the identical long
  vowel), so whatever its diachronic origin, it isn't an example of the Homer-vs-Attic
  no-augment pattern the convention is teaching. Fixed to say so plainly. (Slightly lower
  confidence than the other four, but the label was misleading either way.)
- **Checked and left alone** (considered, not an error): **321, `ἦ` (of ἠμί)** and
  **416, `ἕζετο`/tmesis `καθέζετο`** — both genuinely show no augment marker, but neither
  verb has an attested alternate form that the augment could be said to be "missing"
  from (ἠμί's ἦ/ἦν never take a syllabic augment in any source I could confirm; ἕζομαι's
  imperfect is athematic-initial-vowel in both Homer and Attic). Calling these
  "unaugmented" is at worst imprecise, not factually backwards like the five above, so I
  left them as drafted rather than risk introducing my own error under time pressure.
  **321, `σπάσατ'`** and **414, `κάτθεσαν`** were checked and are correctly identified as
  genuinely unaugmented (their Attic equivalents ἐσπάσατο / κατέθεσαν do show the ε-
  that Homer's forms lack) — no issue.

### 3. `i` silently drops "divine" while `l` keeps it — **moderate**
Line 340 (`ἄκρητον θεῖον ποτὸν ἐντὸς ἔχοντες`): `l` correctly rendered θεῖον literally
as "divine drink," but `i` read "holding the strong, unmixed liquor within" — dropping
θεῖον/"divine" entirely and silently adding "strong" (not itself objectionable, since
ἄκρητον "unmixed" wine was understood as strong, and the note explains this) while losing
the one word `l` explicitly carries. Fixed `i` to "holding the strong, unmixed, divine
drink within," restoring agreement between the two layers.

### 4. `i` drifts from the fixed rendering of `Ὀδυσσῆος φίλος υἱός` — **minor**
Conventions.md fixes `i` as "the dear son of Odysseus" for this periphrasis. At line 415
(`ὡς ἐκέλευσεν Ὀδυσσῆος φίλος υἱός`), `l` correctly used "Odysseus' dear son," but `i`
also used "Odysseus' dear son" instead of the table's fixed i-wording, effectively
duplicating `l`'s phrasing. Fixed `i` to "...just as the dear son of Odysseus had
ordered."

## Considered and explicitly not acted on

- **New-renderings.md's four proposed fixed renderings** (διογενής, ἱερὴ ἲς Τηλεμάχοιο,
  ἀθανάτοισι θεοῖς αἰειγενέτῃσιν, the ἔνθ' αὖτ' ἄλλ' ἐνόησε θεά formula): all checked
  against the Greek and against every occurrence in the part (διογενής at 352 and 366;
  the θεά formula at 382 and 393) — accurate, applied consistently both times, and
  reasonably distinguished from neighboring reserved epithets (δῖος, θεῖος, θεοειδής,
  θεοὶ αἰὲν ἐόντες). No changes.
- **The three flagged judgment calls**:
  - 388–390's unnamed subject of εἴρυσε/ἐτίθει taken as Athena (still disguised as
    Telemachus): I agree this is the natural reading (continuing from ἡ δ' αὖτε at 386),
    and the note already flags it as an inference ("most naturally... continuing her
    stage-management") rather than asserting it flatly. Left as drafted.
  - 356's ἴσθι read as an imperative of οἶδα rather than εἰμί: agreed — the note correctly
    identifies the ἴσθι/εἰμί–οἶδα ambiguity (a real, well-known formal syncretism) and
    supports its choice with an accurate cross-reference to 412 (μία δ' οἴη μῦθον
    ἄκουσεν). Left as drafted.
  - 409's ἱερὴ ἲς Τηλεμάχοιο periphrasis: agreed as sound and well-explained (correctly
    parallels the Homeric βίη Ἡρακληείη-type periphrasis). Left as drafted.
- **370's ἀτρύγετον rendering**: the note says the rendering is "kept the same" as the
  table's fixed ἁλὸς ἀτρυγέτοιο row when applied to πόντον instead of ἅλς, but the actual
  `i` wording used ("the unharvested sea") is a simplification of the table's fixed i
  ("the sea that yields no harvest") rather than a verbatim reuse. This is defensible,
  since the table's fixed pairing is for the whole ἁλὸς ἀτρυγέτοιο formula rather than
  the bare adjective, and the adjective itself ("unharvested") is kept literal and
  consistent — but flagging it here as a borderline call I chose not to overturn.
  Not edited.
- **427's `i` "filled the belly of the sail"** for Greek μέσον ἱστίον ("the middle of the
  sail," which `l` renders literally): "belly" is a natural nautical image for a sail's
  bulging middle and is not on the forbidden-translations list, but it is a step beyond
  strict literalism. Considered as a possible "remembered English" flag but judged to be
  ordinary idiomatic English rather than a phrase recalled from a specific named
  translation; not edited.
- **Citation style "(1.428)" for the Εὐρύκλει' line** in both the unit-345 note and
  new-renderings.md's "inherited discrepancy" section: the repeated single line is
  physically book-line 1.429 (the second line of the 4-line unit whose `ln` is 428), and
  likewise the Μέντορι line cited as "line 267" in packet.md is physically 2.268 (matching
  what the unit's own note in units.json correctly says, "2.268"). This citation-by-
  unit-start-line convention is inconsistent between packet.md and the unit notes, but it
  matches the framing already used in the task's own instructions and in packet.md, so I
  treated it as an established (if slightly imprecise) house convention rather than an
  error, and made no edit.
- **House-renderings table compliance**: checked every table row whose Greek occurs in
  this part (πεπνυμένος reply-formula, κάρη κομόωντας, ἐυκνήμιδες, θεῖος, γλαυκῶπις
  Ἀθήνη, "sandy Pylos," ὣς φάτο, βῆ ῥ' ἴμεν/ἰέναι, etc.) against every occurrence; all
  matched verbatim or were correctly extended to a new referent with a note explaining
  the extension (as new-renderings.md documents). No drift found beyond the two items
  fixed above (§3, §4).
- Ran a keyword scan of every `i`/`l` against the table's full "avoided on purpose" list;
  the only hits ("dark" at 388, "noble" at 391) were false positives on unrelated Greek
  words (σκιόωντο "grew shadowy," ἐσθλοί "noble/good" of comrades) rather than the
  specific epithets those avoidances target. No action needed.

## Summary of edits made to `units.json`

| Line(s) | Field(s) | Severity | What was wrong → what was done |
|---|---|---|---|
| 325, 328, 332, 335, 349, 359, 363, 369, 372, 373, 402, 404, 410, 411 | `l`, `i` | major | No speech in the part had opening/closing “ ” despite conventions.md requiring them and all 7 `mark` cues being present. Added “ to the first unit and ” to the last unit of each of the 7 speeches, in both layers. |
| 363 | `n` | major | `ἔπλετο` wrongly called "unaugmented" (it is augmented; πέλετο/πέλεν is the real unaugmented form). Corrected. |
| 365 | `n` | major | `ὤλετο` wrongly called "unaugmented" (it is augmented, ὀ→ὠ; ὄλετο/ὄλοντο is the real unaugmented form, cf. 1.7). Corrected. |
| 377 | `n` | major | `ἀπώμνυ` wrongly called "unaugmented" (compound augment ο→ω is present). Corrected. |
| 395 | `n` | major | `ἔχευε` wrongly called "unaugmented," self-contradicting the note's own cross-reference to the truly unaugmented χεῦον/χεῦεν at 354/380. Corrected. |
| 407 | `n` | moderate | `κατήλυθον` labeled "unaugmented"; the η is not a droppable augment (Attic κατῆλθον matches). Corrected. |
| 340 | `i` | moderate | `i` dropped θεῖον/"divine" entirely, disagreeing with `l`. Restored. |
| 415 (unit `ln:414`) | `i` | minor | `i` used "Odysseus' dear son" instead of the table's fixed i-wording "the dear son of Odysseus." Corrected. |

No edits were needed in `new-renderings.md`.

## Totals

- **error**: 0
- **major**: 6 (the all-part missing-quotation-marks omission, counted once as a systemic
  finding, plus 4 augment mislabelings individually significant enough to be major on
  their own merits per the recurring-weakness note in the task)
- **moderate**: 2 (κατήλυθον mislabel; the θεῖον/"divine" drop)
- **minor**: 1 (Ὀδυσσῆος φίλος υἱός `i`-drift)
- **considered, not actioned**: 6 (see list above)

Most significant fix: the complete absence of opening/closing quotation marks across
all 7 speeches in the part — a systemic, part-wide omission that would have shipped
every quoted speech in this part unmarked in the English layers, directly contravening
conventions.md.
