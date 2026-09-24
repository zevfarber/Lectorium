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

## Review pass 2 (glossary)

Reviewer pass over `gloss.json` (290 novel entries + 25 broadenings) against `units.json`
(the pass-1-reviewed translation), `novel-forms.json`/`known-forms.json`, and the actually
shipped `odyssey-glossary.json`, plus a final whole-part sanity re-check of `units.json`.
Same severity vocabulary as pass 1.

### Verifications performed first (all passed)

- **Every one of the 290 novel-form keys** occurs as an actual token (elision-stripped,
  case-insensitive) somewhere in `units.json`'s `t` fields — checked programmatically,
  zero misses. The 290 keys also match `novel-forms.json` exactly (no extra, none missing),
  and none overlaps `known-forms.json`.
- **Apostrophe style in `gloss.json`**: zero ASCII `'` or backtick anywhere in any of the
  290 novel entries or the 25 broadenings — all English glosses use the typographic ’
  only, as `conventions.md`'s Glossary-entries section requires. (Checked separately that
  `units.json`'s own `l`/`i`/`n` fields use the *ASCII* apostrophe for English glosses and
  possessives, 652 times, with only 3 incidental typographic ’ where a bare elided Greek
  form is quoted inside a note — this is `units.json`'s own long-established, different
  convention from the glossary's, consistent throughout the file and not something pass 1
  or this pass needed to touch.)
- **Entry length**: none of the 290 novel entries exceeds 230 characters. Three of the 25
  *broadened* entries do (τηλεμάχοιο 235, ἂν 379, ἦ 292 chars) — but this is structural,
  not a drafting fault: the rule requires the old text be kept whole and only appended to,
  and the shipped ἂν entry was **already** 250 characters (over 230) before this part's
  broadening ever touched it. Noted, not actioned (old text may never be edited).

### The 7 flagged homographs (task step 2) — all confirmed genuine, none invented

Identified as the two-joined-readings entries where the two readings are genuinely
different grammatical/lexical facts (not just the same lemma+case turning up with a new
referent, which is what most of the 25 broadenings are): **ἂν** (modal particle ἄν, both
subjunctive/future and unreal-conditional uses, vs. = ἀνά as a tmesis preverb standing
apart from its verb), **ἐν** (plain preposition/adverb vs. tmesis preverb), **μετ**
(preposition μετά vs. tmesis preverb), **ποτὶ** (tmesis preverb ποτί vs. plain
preposition), **ἥ** (relative pronoun vs. ὁ/ἡ/τό personal-demonstrative 'she'), **ἦ**
(affirming/interrogative particle vs. the verb ἠμί 'say, 3 sg.'), and **ἴσθι** (novel
entry, not a broadening: imperative of οἶδα 'know!' vs. identical imperative of εἰμί
'be!'). Checked each against its actual line(s):
- ἂν: tmesis confirmed at 416 (ἀν … βαῖνε = ἀνέβαινε) and 419 (ἂν … βάντες = ἀναβάντες);
  the particle uses are the ordinary Homeric κε(ν)/ἄν pattern `conventions.md` already
  documents. Real, not invented.
- ἐν: tmesis confirmed at 330 (ἐν … βάλῃ = ἐμβάλῃ) and 354 (ἐν … χεῦον = ἔγχεον). Real.
- μετ: tmesis confirmed at 406 (μετ’ … βαῖνε = μετέβαινε), matching the unit's own note.
  Real.
- ποτὶ: tmesis (old, shipped) vs. the plain preposition at 342 (ἑξείης ποτὶ τοῖχον
  ἀρηρότες, 'against the wall', no verb to construe with). Real, and this is exactly the
  same preposition/tmesis-preverb ambiguity as ἂν/ἐν/μετ — not a fabricated distinction.
- ἥ: the relative-vs-personal-pronoun ambiguity is explicitly named in `conventions.md`'s
  grammar list ("the 'article' is a pronoun... τοί can be relative"; "Possessive ὅς, ἥ,
  ὅν... easily mistaken for the relative"). Confirmed at 434 (παννυχίη μέν ῥ’ ἥ γε καὶ ἠῶ
  πεῖρε κέλευθον — ἥ γε is 'she' the ship, not a relative; there is no antecedent clause
  for a relative reading). Real.
- ἦ: confirmed at 321, the part's very first word (ἦ ῥα, καὶ ἐκ χειρὸς χεῖρα σπάσατ’
  Ἀντινόοιο — unit's own note already correctly identifies this as unaugmented ἠμί, 'said'
  closing the previous part's speech). This is one of the best-known Homeric homographs.
  Real.
- ἴσθι: confirmed at 356 (αὐτὴ δ’ οἴη ἴσθι) — the unit's own note (left alone by pass 1)
  already discusses exactly this ambiguity and settles it in favor of οἶδα by the parallel
  at 412. The gloss entry states both readings correctly and flags which one applies here.
  Real, well-known formal syncretism, not invented.

None of the 7 is a fabricated distinction; all match documented Homeric grammar and all
match their actual line(s) in this part.

### Finding 1 — `ναιεταόντων` mislabeled "diectasis" (should be "uncontracted") — **major**

`gloss.json`'s entry read: "ναιετάω — ...; pres. part. gen. pl., **epic diectasis** (=
Attic ναιετώντων)". Diectasis (the example `conventions.md` itself gives is αἰτιόωνται) is
the *artificial* Homeric "stretching apart" of a vowel sequence that was **already**
contracted at an earlier stage of the language, and it is visibly recognizable by a
resulting **-όω-** spelling (compare this part's own genuinely-diectasis `σκιόωντό`,
correctly labeled). `ναιεταόντων`, by contrast, spells the sequence **-αο-**
(ναιετα-όντων), exactly the ordinary, plain uncontracted present-participle stem +
ending that Homer freely uses for -άω/-έω verbs throughout this part (compare the
correctly-labeled `ὑπερηνορεόντων`, `φορέουσι`, `ᾔτεε`, all "epic uncontracted," no
diectasis claim). The unit's own note at 399 (`ln:399`) already calls the phrase
"an uncontracted genitive phrase" — `gloss.json`'s "diectasis" contradicts the unit note
it is glossing. This is the same class of error the task flagged as a recurring drafter
weakness (cf. pass 1's augment mislabelings) applied to a different grammatical category.
**Fixed**: changed "epic diectasis" to "epic uncontracted" in `gloss.json`.

### Finding 2 — `ἀκραῆ` claimed "uncontracted" without support — **moderate**

The entry read "ἀκραής — ...; masc. acc. sg., uncontracted". Genuine Homeric "uncontracted"
σ-stem (-ής/-ές) adjective accusatives show visible hiatus (two separate vowel letters,
e.g. ἀκηδέα), because the σ-stem contraction of -εσα → -εα → -η is optionally left open by
the epic tradition the same way -έω/-άω verb contractions are. But the actual attested
spelling here, `ἀκραῆ` (a hapax legomenon, occurring only at this line), already shows the
single contracted vowel -ῆ, identical to the Attic form given as the point of comparison —
there is no visible hiatus to call "uncontracted," and I could not confirm a genuine
alternate uncontracted Homeric form for this specific (rare) word. Since the claim is
unsupported by the word's own spelling, I removed it rather than assert a different,
equally unverifiable claim. **Fixed**: entry now reads "ἀκραής — blowing keen and fresh
(of wind); masc. acc. sg." with no contraction claim. Flagged moderate rather than major
because the underlying case/gender/number parse was already correct and the translation
was never affected — only the grammatical side-note was unsupported.

### Finding 3 — `ἀφορμηθέντος` mislabeled "genitive absolute" — **moderate**

The entry called this "genitive absolute (unexpressed subject 'I')." A true genitive
absolute is a participial clause grammatically detachable from the rest of the sentence,
with its own subject unconnected to any other constituent (e.g. this part's own, correctly
labeled, `ἰούσης` at 428: νηὸς ἰούσης, 'as the ship went', freestanding from the wave that
is the main clause's subject). `ἀφορμηθέντος` at 375 is different: it is the direct
genitive complement of ἀκοῦσαι ('hear'), the regular Greek construction where a verb of
perception takes a genitive participle for the person perceived doing something ('hear
[me] having set out') — removing it would leave ἀκοῦσαι without its content, so it is not
grammatically free-standing and the label "absolute" does not apply, even though the
case/tense/voice/number parse and the 'unexpressed subject "I"' identification (matching
the unit's own first-person reading, correct given this is Telemachus's own speech about
himself) were all already right. **Fixed**: reworded to "genitive participle governed by
ἀκοῦσαι (verb of perception + gen. participle), unexpressed subject 'I'," and softened the
gloss translation from 'when I have set out' to 'that I have set out' to match the
perception-verb construction rather than a temporal clause.

### Finding 4 — the οἶδ' broadening (task step 3): **glosser's claim confirmed, not overturned**

The shipped `odyssey-glossary.json` entry for `οἶδ` reads "οἶδα — know; perf. 1 sg., elided
(οἶδ’ = οἶδα)" — a first-person-only parse. This part's sole occurrence is at 332 (`τίς δ’
οἶδ’, εἴ κε καὶ αὐτὸς ἰὼν κοίλης ἐπὶ νηὸς...`), where οἶδ(ε) agrees with the interrogative
subject τίς, 'who' — grammatically **third singular**, not first: the unit's own note
already says so explicitly ("τίς δ' οἶδ(ε) is a common Homeric turn, 'and who knows...'.
οἶδε is a perfect with present force, 'knows'"). The glosser's broadening — adding "· also
perf. 3 sg. (identical elided form): 'he/she knows' (τίς δ' οἶδ(ε) 'who knows')" — is
therefore correct: the shipped entry's 1st-sg.-only parse genuinely does not cover this
part's usage, and the fix genuinely supplies the missing 3rd-sg. reading rather than
duplicating the old one. **No change needed**; the glosser's "real person mismatch" claim
is upheld.

### The 25 broadenings (task step 4): all verified byte-for-byte against the shipped file

Programmatically compared every one of the 25 `__broaden__` entries' leading portion
against the corresponding key's actual value in `odyssey-glossary.json`'s `glossary`
object (not the top level of that file, which holds only metadata — `work`, `workEn`,
`language`, `note`, `glossary`). **All 25 old-text portions are byte-for-byte identical**
to the shipped text, with exactly ` · also...` appended in each case and nothing else
touched — including the three cases (ἂν, ἐν, ἦ) where the *shipped* entry itself already
contained an internal ` · also` clause from an earlier part's broadening, which the new
broadening correctly preserved in full before appending its own further clause.

Also confirmed each new reading is a genuine, distinct usage actually attested in this
part's `units.json` (not a restatement of what the old entry already covers): αἰνῶς
(intensifier with ἵεται, 327) · αὐτὴν (intensive infinitive-subject, 375) · αὐτῆς (plain
gen. with ἄγχι, 417) · αὐτῇ (anaphoric 'it' with ἐν, of the ship, 389) · εὐρύκλει
(nominative apposition, not vocative, 345) · θεοῦ (gen. with ἄνευ, 372) · θεῖον (neut.
acc. agreeing with ποτόν, 341) · κατήλυθον (3 pl., of Telemachus and Athena, 407, vs. the
shipped 1 sg.) · κῦμα (acc. after κατά, 429, vs. the shipped nom.) · μέλαιναν (agreeing
with νῆα, 430) · μέσον (attributive with ἱστίον, 427) · μετ (tmesis, 406) · οἶδ (see
Finding 4) · ποτὶ (plain preposition, 342) · πρίν (+ temporal clause, 374) ·
τηλεμάχοιο (plain possessive in the ἱερὴ ἲς periphrasis, 409) · φίλοι (vocative address,
410) · ἂν, ἐν, ἥ, ἦ, μετ, ποτὶ (tmesis/homograph readings, see above) · ἔπλετο (aorist
force, 364, vs. the shipped present force) · ἦρχε ('led the way' absolute, 416, vs. the
shipped 'began' + gen.) · ἱστὸν ('mast', 424, vs. the shipped 'loom') · ᾤχετο (durative
'went about', 383, vs. the shipped punctual 'had gone'). Every one checks out as real and
non-duplicative.

### Sampled deep review of the 290 novel entries

Given the volume, every entry was checked programmatically for occurrence, apostrophe
style and length (all pass, see above), and a substantial sample — all entries touching
tmesis, augment, contraction/diectasis, genitive absolutes, person/number syncretism, and
gender-agreement claims, plus roughly 60 further entries chosen across the part — was
checked by hand against the actual line(s) and against the unit's own note where one
exists. Aside from Findings 1–3 above, no wrong lemma, wrong gender, wrong tense/mood, or
parse-vs-line mismatch was found. Specifically checked and confirmed correct: the
tmesis set (βάλῃ/βάντες/βαῖν’/βαῖνε and the ἀν/ἐν/μετ/ποτί broadenings above), the
principal-part choices for defective/irregular verbs (ἀνώγει, ἐνείκῃ, ἵεται, φάν, ἕστασαν,
ἀπόληται), the -σκε iterative (εἴπεσκε), the numerals and directional-suffix nouns
(δώδεκα, εἴκοσι, οἴκαδε, θαλαμόνδε, σπάρτηθεν, τηλόθι), and the gender-agreement claims on
epithets governed by hyperbaton (εὐρύν/θάλαμον at 337–338, ἡδύν at 349, ἀκραῆ/Ζέφυρον at
420–421 aside from the contraction note fixed above).

### Final whole-part sanity pass on `units.json` (task step 5)

- **Quotation-mark balance**: re-confirmed programmatically. Both `l` and `i`, concatenated
  across all 71 units, contain exactly 7 `“` and 7 `”` each, matching the part's 7 `mark`
  cues one-for-one (325, 332, 349, 363, 372, 402, 410). No unmatched or missing quote.
- **`t`-tiling**: re-confirmed programmatically against `packet.md`'s 114-line block
  (whitespace-normalized): the two texts are character-identical, 4,231 characters each.
  The 15 `p: true` flags match `packet.md`'s 15 `¶` marks exactly, in the same order.
  (Same result pass 1 already reported; re-run independently here as the task asked.)
- **Spot check of 10 further units** not named individually anywhere in pass 1's findings
  or "considered" list (ln 322, 337, 344, 355, 367, 383, 392, 406, 418, 430): read `t`,
  `l`, `i` and `n` for each. No stray or missing quotation marks (none of these fall at a
  speech boundary, and none carries one), no `l`/`i` mistranslation against `t`, and notes
  consistent with the Greek. No issues found; no edits needed.

### Considered and explicitly not acted on

- **The three near-230-character broadened entries** (τηλεμάχοιο 235, ἂν 379, ἦ 292 chars)
  — a structural consequence of the additive-only broadening rule, already present before
  this part's edit in the shipped ἂν entry (250 chars pre-broadening); cannot be fixed
  without editing old text, which is forbidden. Not actioned.
- **ἐυκνήμιδες labeled "masc. nom. pl."** at 402: ἐυκνήμις is technically a two-termination
  compound adjective (built on the fem. noun κνημίς) that never distinguishes a separate
  feminine form; "masc. nom. pl." is a defensible simplification for its use here
  (agreeing with the masculine ἑταῖροι) rather than an error. Not actioned.
- **ἐπιστεφέας/ἐϋρραφέεσσι "uncontracted" labels**: rechecked against the diectasis
  question raised by Finding 1 — these are genuine uncontracted epic datives/accusatives
  (-έεσσι, -έας) of σ-stem/ές-stem adjectives, a different and unproblematic case from
  either the diectasis or the ἀκραῆ situations. Confirmed correct, left alone.

## Totals (pass 2)

- **error**: 0
- **major**: 1 (`ναιεταόντων` mislabeled diectasis instead of uncontracted, contradicting
  the unit's own note)
- **moderate**: 2 (`ἀκραῆ`'s unsupported "uncontracted" claim; `ἀφορμηθέντος`'s "genitive
  absolute" mislabel for what is actually a verb-of-perception genitive complement)
- **minor**: 0
- **confirmed, not overturned**: 1 (the οἶδ' broadening — glosser's "real person mismatch"
  claim is correct)
- **considered, not actioned**: 3 (see list above)
- **broadenings verified byte-for-byte against the shipped glossary**: 25 / 25, all clean
- **homographs verified as genuine, non-invented grammatical facts**: 7 / 7

No corrections were needed in `units.json`; all fixes for this pass were made in
`gloss.json`. The glossary and the translation are both, as far as this review can
determine, ready for build/validate.
