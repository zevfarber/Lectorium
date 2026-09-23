# Review: odyssey-007 (Odyssey 2.208–320)

Reviewed against `conventions.md`, `packet.md`, `new-renderings.md`, `QUESTIONS.md`, and the relevant
units of the published `odyssey-003/units.json`, `odyssey-004/units.json`, `odyssey-005/units.json` and
`odyssey-006/units.json` (all lines this part's packet or notes claim as repeats or cross-references,
plus the two immediately preceding parts' closing units for the boundary check). This is Pass 1
(translation) only — `gloss.json` does not exist yet for this part, and the glossary pass is out of
scope here. Done twice, as the runbook requires: a first structural/mechanical pass (verified by script
that the concatenated `t` reproduces `packet.md` exactly, treating the mid-line unit split at 2.244 as a
single-space join rather than a newline join; every `l`'s `\n` count equals its `t`'s; no `i` contains
`\n`), then a second sense/wording pass, checking every note's grammar claims, every cross-reference,
every house-table formula, and the two flagged judgment calls against LSJ/Cunliffe/Autenrieth. **55
units, all read.**

**15 findings, 15 `units.json` edits** (one edit per affected unit; several units' edits touch more than
one field). No `t` field was touched. Severity: **1 error, 7 moderate, 7 minor**. Several further points
were considered and refused, listed at the end, with reasons.

## Changes to `units.json`

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 2.300 | `l`, `i`, `n` | **error** | ἀνιεμένους (of the goats, ἀνίημι 'send up, let go, release') was rendered "singeing," invented to parallel εὕοντας ("scorching/roasting"); ἀνίημι does not mean 'singe' in LSJ, Cunliffe or Autenrieth — that sense belongs only to εὕοντας (from εὕω). This is exactly the "English phrase arrives fully formed" case the sole-source rule warns against, and it also left εὕοντας itself mistranslated "roasting" in `l`/`i` even though the unit's own (now-corrected) note always knew it meant 'singe'. | Rebuilt from the grammar: ἀνιεμένους = goats being let loose/driven into the courtyard (presumably from their pen, for slaughter); εὕοντας = hogs being singed for roasting — two distinct feast-prep actions, not one action named twice. `l` → "goats being driven in, and fat hogs being singed, in the courtyard."; `i` reworded to match; `n` rewritten to state the correct sense of ἀνίημι and retract the false parallel. |
| 2.217 | `l`, `i`, `n` | moderate | κλέος (ἥ τε μάλιστα φέρει κλέος ἀνθρώποισιν) was rendered "fame" in `l`, which also contradicted the unit's own `i` ("brings men report") and, worse, contradicted the identical formula already published at 1.283 in odyssey-003 (`l` "brings report to men", note: "κλέος here has its root sense, 'what is heard', report"). `i` also confused the two different Greek nouns, rendering both ὄσσα and κλέος as "report" ("hear a report... which brings men report"). | `l`: "fame" → "report", matching the published formula. `i`: "a report sent from Zeus" → "a rumor sent from Zeus" (ὄσσα), keeping "report" only for κλέος, removing the doubled word. `n` extended with the cross-reference to 1.283/odyssey-003. |
| 2.269 | `l`, `i`, `n` | moderate | The house-fixed formula ἔπεα πτερόεντα προσηύδα ("winged words he/she spoke") was restructured to "addressed him with winged words" (`l`) / "spoke to him with winged words" (`i`), departing from the wording already published for this exact formula at 1.122 in odyssey-002 ("...to her winged words he spoke:" / "...he spoke winged words to her:"). | Rebuilt on the published pattern, with the goddess's own gender (φωνήσασ', feminine, vs. the earlier φωνήσας): `l` → "and, lifting her voice, to him winged words she spoke:"; `i` → "and, raising her voice, spoke winged words to him:". `n` records the cross-reference. |
| 2.245 | `l` | moderate | πλεόνεσσι ('a greater number', per the note's own gloss, and per its second occurrence at 2.251 "greater numbers") was rendered "more numerous ones" in `l` — inconsistent with the note's own definition, with `i`'s own "greater numbers," and with the second occurrence. | `l`: "more numerous ones" → "greater numbers of them", matching `i`, the note, and 2.251. |
| 2.261 | `i` | moderate | new-renderings.md fixes πολιὴ ἅλς as `l`/`i` both "the grey sea"; the unit's own `l` already used "the grey sea," but `i` used "the grey water" instead, an unforced deviation from the newly-proposed fixed rendering the unit's own note cites. | `i`: "grey water" → "grey sea". |
| 2.278 | `i` | moderate | The note states the clause οὐδ' ὄπιθεν κακὸς ἔσσεαι οὐδ' ἀνοήμων (verbatim-repeated from 2.270) "is kept to the same English both times" — true of `l`, but `i` actually differed ("you will not be base hereafter, or witless" vs. 2.270's "you will not be a base man hereafter, nor a witless one"), so the note contradicted its own unit. | `i` reworded to match 2.270's wording for the shared clause exactly. |
| 2.221 | `n` | moderate | Cited the parallel passage already fixed at 2.221 in the published odyssey-003 (Odyssey 1.289) as spoken by "Mentor advising Telemachus" — checked against odyssey-003/units.json: that speech (marked "Athena counsels him", beginning 1.253) is Athena's own, disguised as Mentes (Book 1's disguise), not Mentor (who belongs to Book 2 and does not appear in Book 1 at all). | Corrected "there Mentor advising Telemachus" → "there Athena, disguised as Mentes, advising Telemachus". |
| 2.306 | `n` | moderate | Claimed Antinous's mocking promise of "a ship and picked oarsmen... from the Achaeans" is "the very promise Leiocritus had already made on his behalf" — but Leiocritus's speech (2.252–256) says the opposite: that Telemachus will sit waiting for news in Ithaca and "never accomplish this journey" (τελέει δ' ὁδὸν οὔ ποτε ταύτην). Leiocritus predicts failure; he makes no such promise. | Reworded to describe Antinous's promise as standing in ironic contrast to, not a repetition of, Leiocritus's earlier prediction, with the correct cross-reference (2.255–256). |

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 2.234 | `i` | minor | The house-fixed line πατὴρ δ' ὣς ἤπιος ἦεν has `i` "and was as gentle as a father" per conventions.md's table and the identical published wording at 2.47 in odyssey-005; this unit's `i` added an unfixed "he" ("and he was as gentle as a father"). | Removed "he" to match the fixed table and 2.47's own published `i` exactly. |
| 2.239 | `n` | minor | Claimed "the sense only becomes clear with the ἀλλά of 2.239" — line 239 actually opens νῦν δέ ("but now"), not ἀλλά; there is no ἀλλά in that line. | Corrected "the ἀλλά of 2.239" → "the νῦν δέ of 2.239", with a one-clause gloss of the contrast. |
| 2.255 | `n` | minor | Self-contradictory within one sentence: "ἀγγελιάων is an Ionic form (Attic ἀγγελίας)... with an uncontracted genitive plural ending -άων (Attic -ῶν)" — ἀγγελίας is a singular form, but the sentence's own second half correctly identifies the ending as genitive *plural* (Attic -ῶν, i.e. ἀγγελιῶν). | Removed the wrong singular parenthetical; folded the correct Attic equivalent (ἀγγελιῶν) into the one already-accurate clause about the ending. |
| 2.257 | `n` | minor (scope) | "the word is otherwise rare in Homer" (of αἰψηρήν) is a claim about the word's frequency across the whole poem, which this 113-line part cannot verify — the same class of unverifiable claim odyssey-004's review already flagged and QUESTIONS.md records as barred. | Removed the claim; kept the (verifiable, in-part) gloss. |
| 2.305 | `i` | minor | ἀλλά μοι ἐσθιέμεν καὶ πινέμεν has μοι, 'to/for me' (Antinous, singular, an ethical dative) — `i` rendered it "eat and drink **with us**," introducing a plural group sense not in the Greek and not matching `l`'s own (correct) "eat, for me, and drink." | Removed "with us" from `i`. |
| 2.316 | `n` | minor (citation) | "the same κήρ already met at 2.284" — κῆρα (θάνατον καὶ κῆρα μέλαιναν) is on packet line 2.283, not 2.284. | Corrected 2.284 → 2.283. |
| 2.319 | `n` | minor (scope) | "ἐπήβολος + genitive... is a rare word outside this idiom" — another whole-poem frequency claim this part cannot verify (same class as the 2.257 fix above). | Reworded to "is confined to this fixed idiom of ownership" — a claim about the word's use, not an unverifiable frequency claim about the rest of Homer. |

Re-verified after all fixes: JSON valid, 55/55 units; the concatenated `t` still reproduces `packet.md`
exactly (the mid-line join at 2.244 included); every `l`'s `\n` count still equals its `t`'s; no `i`
contains `\n`.

## The two flagged judgment calls

- **ἀνιεμένους σιάλους θ' εὕοντας (2.300)** — see the error-severity fix above. The drafter's "singeing"
  for ἀνιεμένους, built to parallel εὕοντας, has no support in LSJ, Autenrieth or Cunliffe: ἀνίημι's
  Homeric senses are "send up, let go, release, relax, permit," never "singe." Corrected to the ordinary
  sense (goats being let loose/driven into the courtyard, i.e. from their pen, for slaughter), keeping
  "singe" for εὕοντας alone, where it is actually attested (εὕω).
- **ὑψαγόρη (2.303)** — checked and left as drafted; the drafter's claim holds up. The shared clause
  Τηλέμαχ' ὑψαγόρη, μένος ἄσχετε is rendered `l` "Telemachus, lofty-talker, unrestrained-in-fury" / `i`
  "Telemachus, you lofty talker, unrestrained in your fury" at both 2.303 (this part) and 2.85 (odyssey-005,
  confirmed by direct read of the published `odyssey-005.json`, unit `ln` 85) — word for word identical.
  The near-miss at 1.385 in odyssey-004 (ὑψαγόρην τ' ἔμεναι, a predicate infinitive rather than this
  vocative) is correctly left as its own case per QUESTIONS.md's existing note on the two occurrences.

## Verified and confirmed without change

- **Quotation-mark balance.** 7 `mark`s, 7 opening “ on `l` and `i`, 7 closing ” on `l` and `i` — all
  balanced, matching the drafter's claim of 7 speeches, all opened and closed within this part. Verified
  each boundary against the actual Greek, not just the presence of a mark:
  - 2.209–223 (Telemachus, "Telemachus speaks") — opens after the narration reply-formula at 2.208, closes
    at 2.223 before the narration ἦ τοι ὅ γ' ὣς εἰπὼν... at 2.224. ✓
  - 2.229–241 (Mentor, "Mentor speaks") — opens after the narration/speech-intro at 2.228, closes at 2.241
    before the narration reply-formula at 2.242. ✓
  - 2.243–256 (Leiocritus, "Leiocritus speaks") — opens after the narration reply-formula at 2.242, closes
    at 2.256 before the narration ὣς ἄρ' ἐφώνησεν... at 2.257. ✓
  - 2.262–266 (Telemachus's prayer, "Telemachus prays") — opens after the narration at 2.260–261, closes
    at 2.266 before the narration ὣς ἔφατ' εὐχόμενος... at 2.267. ✓
  - 2.270–295 (Athena as Mentor, "Athena, disguised as Mentor, answers") — opens after the narration/
    speech-intro at 2.267–269, closes at 2.295 before the narration ὣς φάτ' Ἀθηναίη κούρη Διός at 2.296. ✓
  - 2.303–308 (Antinous, "Antinous speaks") — opens after the narration/speech-intro at 2.301–302, closes
    at 2.308 before the narration reply-formula at 2.309. ✓
  - 2.310–320 (Telemachus, "Telemachus replies") — opens after the narration reply-formula at 2.309, runs
    to the end of the part (2.320), correctly closed (the part does not end mid-speech). ✓
  - Confirmed against the boundary with odyssey-006: its own last unit (2.205–207, Eurymachus) is left
    without a closing ” by design (per that part's own review, modelled on odyssey-005's practice for a
    speech that runs to a part's edge) — but Eurymachus's speech in fact ends at 2.207, immediately before
    this part's own opening narration reply-formula at 2.208, so nothing carries over into odyssey-007 for
    this part to close.
- **`p` (paragraph) flags**: exactly on 208, 224, 260, 267, 270, 296, 303 and the packet's other ¶ marks
  (229, 242, 257) — matching every ¶ in `packet.md` and nothing else.
- **Lines already published, checked character-for-character against the primary files** (not just
  packet.md's own copies):
  - 2.208 = odyssey-004 (Book 1, `ln` 388): `l`/`i` identical. ✓
  - 2.221 = odyssey-003 (Book 1, `ln` 289): not a full-unit match (different person/mood), correctly left
    as a partial echo rather than forced identical, per the unit's own (now-corrected) note. ✓
  - 2.229 = odyssey-005 (`ln` 25): `l`/`i` identical. ✓
  - 2.309 = odyssey-004 (Book 1, `ln` 388): `l`/`i` identical. ✓
  - 2.215/2.264 (πατρὸς δὴν οἰχομένοιο, internal repeat): `l` identical both times, as the note claims;
    `i` legitimately differs (different surrounding syntax, and the note only claims the phrase itself is
    fixed, not the whole sentence). ✓
  - 2.273/2.318 (ἁλίη, internal repeat): "fruitless" kept in both `l` and `i`, as the note claims. ✓
- **House-table formulas**, checked at every occurrence: Πύλον ἠμαθόεντα (214, 262, "sandy Pylos");
  μνηστῆρες ἀγήνορες (235, 299, "the lordly suitors," kept distinct from ἀγαυοί); ἀγορήσατο καὶ μετέειπεν
  (228); κέκλυτε δὴ νῦν μευ... (229, verified against odyssey-005 as above); πεπνυμένος of Telemachus
  (208, 309); the reply-formula τὸν δ' αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα (208, 309); ἀμφίαλος Ἰθάκη
  (292, "sea-girt Ithaca"); θεῖος of Odysseus (233, 258, "divine," correctly kept distinct from δῖος
  "heavenly"). All exact and consistent.
- **new-renderings.md's 6 proposed entries**, checked at every occurrence against collisions with the
  fixed table and against their own use in `units.json`: the Leiocritus reply-formula (242), the Athena
  narrator-formula (296), the Antinous approach-and-address formula (301–302), μνηστῆρες/-ας ἀγαυοί/-ούς
  (209, 247), ἐπ' ἠεροειδέα πόντον (263) all match their proposed wording exactly and collide with
  nothing in the fixed table. πολιὴ ἅλς (261) needed the `i` fix recorded above. πατρώιος ἑταῖρος /
  πατρώιοι ἑταῖροι (254, 286) checked and left — see "considered and refused" below.
- **Structural/mechanical.** The concatenated `t` reproduces `packet.md` exactly, including the mid-line
  unit split at 2.244 (joined by a single space, not a newline, since both halves sit on the same source
  verse line — the correct reconstruction, confirmed against the model set by the duplicate-`ln` pattern
  odyssey-006's review already established for mid-line splits). Every `l`'s `\n` count matches its `t`'s
  (55/55). No `i` contains `\n`. No mechanical defects found (unlike odyssey-006, which had two).
- **Scansion.** `packet.md` says "none" flagged; re-checked this claim is not stale by reading every line
  for an obvious irregularity (unresolved short vowels before mute+liquid, suspicious hidden quantities)
  without running the scansion script. Nothing stood out. No unit's note claims a metrical irregularity,
  correctly matching the "none" flag.
- **Remembered English.** Read every `i` against the list of in-copyright translations to avoid
  (Lattimore, Fagles, Fitzgerald, Lombardo, Mandelbaum, Rieu, Mitchell, Verity, Green, Wilson,
  Mendelsohn). Found one phrase that read as if it had arrived fully formed rather than built from the
  grammar — "singeing goats" at 2.300 — which turned out on checking to be an invented sense rather than
  a borrowed one; fixed above. No other suspect phrase found.
- **Article/pronoun and possessive/relative labelling**, spot-checked throughout (τόν 208, τά 211, οἷσιν
  233, ἑόν 247/258/286 — confirmed 247 is genuinely the first instance of the possessive ἑός in this
  part, by search) — all correct.
- **"A note asserts nothing about the rest of the poem that this part cannot show."** Applied the
  narrower reading already settled in QUESTIONS.md (bar unverifiable/specific claims — quoted text,
  exclusivity/frequency claims, misattributable facts; allow broad thematic framing). Two frequency
  claims failed this test and were removed (2.257, 2.319, above). Left in place as acceptable broad
  framing: "Mentor is introduced here for the only time before he lends his shape to Athena later in this
  same part" (224, scoped to this part itself, not the rest of the poem); "foretells the suitors'
  slaughter to come" (283, a low-risk thematic/dramatic-irony aside, not a specific checkable claim).

## Findings considered and refused

- **πατρώιος ἑταῖρος / πατρώιοι ἑταῖροι (2.254, 2.286).** The `i` wording differs between the plural
  ("his father's companions from the start") and singular ("a companion of your father's day")
  occurrences — the plural's extra "from the start" reflects ἐξ ἀρχῆς, a separate Greek phrase actually
  present only at 2.254, not part of the πατρώιος formula itself. Since new-renderings.md's own row
  already varies this phrase by person and number (it is not yet a word-for-word-fixed house-table entry,
  only a proposal), and the difference is fully explained by a real difference in the Greek, this was not
  treated as an error. Left as drafted.
- **κατ' ἄρ' ἕζετο (2.224), called an instance of "the missing augment this poem shows throughout."**
  Checked whether ἕζετο is genuinely unaugmented (vs. a lengthened ἡζετο). This is defensible under
  Homeric grammar (ἕζομαι regularly appears unaugmented in epic) and not clearly wrong; left unchanged
  rather than relitigating a genuinely uncertain point beyond what any of the sole-source lexica settle
  outright.
- **ASCII vs. typographic apostrophe (`'` vs `’`) in `l`/`i`/`n`.** This part mixes both, matching the
  still-unresolved corpus-wide question already restated at odyssey-005 and odyssey-006. Not touched, on
  the same precedent (a maintainer decision, not a line-by-line judgment call for this review).
- **The `βίοτον καὶ νόστον` "close to a hendiadys" reading (2.218–219) and other interpretive glosses**
  (e.g. "a homely realistic touch of feast preparation" at 2.300, retained in the corrected note; "closes
  the part on a note of bitter irony" at 2.320). Checked against the Greek and found each accurate to
  what this part itself shows; left as legitimate tutorial commentary, not overreaching claims.

## For QUESTIONS.md

Nothing new to add. The two items this part specifically bore on are resolved above without reopening
either open question: ὑψαγόρη(ν) (1.385 vs. 2.85 vs. 2.303) is confirmed consistent at 2.85/2.303 and the
existing near-miss note on 1.385 stands unchanged; the ASCII/typographic-apostrophe question remains open
and this part is left mixed, consistent with existing practice.

## Review pass 2 (glossary)

Done in a second session, once the glosser produced `gloss.json` (241 novel-form entries + 19
`__broaden__` entries). I checked **all 241 novel entries** — lemma, part of speech, meaning and parse
— against how each form is actually used in `units.json`'s `t` fields (built a script-assisted mapping
from every gloss key to its occurrence(s) in `units.json`, then read every one by hand against its line),
and all **19 broadenings** for the additions-only/substring rule against `odyssey-glossary.json`'s shipped
text. I also specifically cross-checked the five items the glosser flagged for special attention.

**3 findings, 3 `gloss.json` edits** (all in novel entries; no broadening needed a fix). No `units.json`
field was touched in this pass — the notes the glossary check surfaced did not themselves misstate
anything (see the κίε/Τηλεμάχοιο item below: the error was confined to `gloss.json`, and the corresponding
`units.json` note at 2.301 never made the same claim). Severity: **0 error, 3 moderate, 0 minor**. One
further tension was found and is recorded below rather than "fixed," since no fix is possible without
breaking either the 230-char cap or the additions-only rule.

### Changes to `gloss.json`

| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| ἠγαθέην | moderate | Lemma given as **ἠγαθέη**, the inflected feminine nominative form actually used only as a citation of itself — not the LSJ/Autenrieth/Cunliffe headword. This 3-termination compound adjective (ἀγα- intensive + θεῖος) is dictionary-lemmatised under its masc. nom. sg. form, **ἠγάθεος**, exactly as this same file correctly does elsewhere for parallel cases (e.g. `ἁλίη`: lemma given as masc. ἅλιος, not the fem. form itself; `μέλαιναν`: lemma μέλας, not a feminine headword) — ἠγαθέην was the one adjective entry in the file that used the inflected feminine as if it were the headword. | Lemma corrected to ἠγάθεος; parse extended to cite the actual form (ἠγαθέην) explicitly, keeping the existing note on Πύλον's occasional feminine agreement in this formula (also true, separately confirmed against 2.214's masc. Πύλον ἠμαθόεντα in the same part — a real, noteworthy gender variance for this place-name, correctly flagged). |
| κίε | moderate | Claimed κίε itself governs a genitive ("+ gen.: 'went straight for'"), with Τηλεμάχοιο cited as that genitive's object. But the already-shipped, already-known entry for ἰθύς (`known-forms.json`, unedited by this glosser) states plainly: "ἰθύς — straight; prep. + gen. ... 'straight towards'" — i.e. the genitive in ἰθὺς … κίε Τηλεμάχοιο (2.301) is governed by ἰθύς, the epic equivalent of Attic εὐθύς + gen., not by the bare verb κίω "go." | Removed the false "+ gen." claim and the "went straight for" gloss (which smuggled ἰθύς's sense into κίε alone); reworded to "went," with an explicit note that the genitive belongs to ἰθύς, not this verb. |
| τηλεμάχοιο | moderate | Companion error to the κίε fix: "governed by κίε" repeats the same misattribution for the noun entry. | Corrected to "governed by ἰθύς ’straight toward’ (not by κίε)". |

All three re-verified after editing: still valid JSON, still under the 230-char cap (120 / 147 / 115
characters respectively, well inside the limit), typographic ’ only, no ASCII apostrophe or backtick.

### The four flagged special-attention items

- **εἰδομένη** (2.268, Μέντορι εἰδομένη ἠμὲν δέμας ἠδὲ καὶ αὐδήν, of Athena's disguise as Mentor).
  Checked against Autenrieth's *Homeric Dictionary*, whose entry for εἴδομαι lists the aorist system as
  "aor. εἰσάμην, part. εἰσάμενος, **also εἰδόμενος**" — i.e. the -όμενος spelling used here is itself
  classed under the aorist, not a separate present-tense form, in the standard reference. This matches
  `units.json`'s own note at 2.267–269 (already passed in Pass 1), which independently calls it "the
  aorist participle of εἴδομαι." The shipped glossary entry (`known-forms.json`, from an earlier part)
  labels the word "pres. part." — under the additions-only rule that text cannot be replaced, only added
  to, so the glosser's broadening (adding "· also functioning as aor. part. (the same -όμενος form serves
  both in Homer), ’having made herself like’ (Μέντορι εἰδομένη)") is the correct and only available way
  to record the right reading for this part's usage. Verified adequate as written; no further fix needed.
- **περὶ and τί** — both broadenings are correct as far as they go but are compressed to a bare tag
  ("· + dat." for περὶ 2.244's περὶ δαιτί, anastrophe, "over/for the sake of a feast"; "· adj." for τί
  2.303's μή τί τοι ἄλλο... κακὸν, the indefinite used adjectivally with a neuter noun rather than
  adverbially as in the base entry's οὔ τι). Checked the actual arithmetic: the pre-existing shipped
  entries are already 217 and 219 characters; the glosser's additions bring both to 226; only **4
  characters** of headroom remain under the 230 cap on either one. Nothing informative (a case citation,
  a short sense-gloss, a line reference) fits in 4 characters, and the additions-only rule forbids
  shortening or restructuring the existing text to make room. This is a genuine, unresolvable tension
  between the 230-char cap and the convention that an entry be self-explanatory — recorded here rather
  than silently accepted or force-"fixed" into something equally cryptic. Both entries are technically
  correct (real, distinct uses of περί + dat. and of τί as indefinite adjective are attested exactly where
  claimed); they are simply as terse as the cap allows.
- **ὁμίλει** — confirmed a genuine homograph within this part. The only occurrence (2.288, ἀλλὰ σὺ μὲν
  πρὸς δώματ’ ἰὼν μνηστῆρσιν ὁμίλει, ὅπλισσόν τ’ ... ἄρσον ...) sits in a run of second-person commands
  (ὅπλισσόν, ἄρσον, both explicit aor. imper. 2 sg.) with an explicit σύ subject and a nominative
  participle ἰών agreeing with it — grammatically this can only be a 2 sg. imperative ("mingle!"), never
  a 3 sg. form, so it cannot be the shipped impf. 3 sg. reading from wherever ὁμίλει was first glossed.
  For a contract verb in -έω, the unaugmented impf. 3 sg. (ὡμίλεε → ὁμίλει) and the pres. imper. 2 sg.
  (ὁμιλέ-ε → ὁμίλει) are genuinely identical surface forms, so this is a real homograph, not an invented
  one. The broadening states both readings correctly and ties the imperative reading to this line's own
  text. No fix needed.
- **ὃ** (2.262, κλῦθί μευ, ὃ χθιζὸς θεὸς ἤλυθες ἡμέτερον δῶ). Checked against the actual line in
  `units.json` and against Monro/Autenrieth: a relative pronoun heading a clause with its verb in the
  2nd person, in direct address, is a recognized epic/prayer idiom, not an aberration — the closest
  parallel is *Iliad* 3.277, Ἠέλιός θ’, ὃς πάντ’ ἐφορᾷς καὶ πάντ’ ἐπακούεις, "Helios, thou who seest all
  and hearest all," where the (morphologically 3rd-person-shaped) relative ὅς is followed by 2nd-person
  verbs (ἐφορᾷς, ἐπακούεις) because the referent is being addressed directly — exactly the pattern
  claimed here for ὃ … ἤλυθες. The un-sigmatised ὅ (rather than ὅς) functioning as a masc. nom. sg.
  relative is itself already established for this corpus (the shipped `ὅ` entry already lists "also
  relative, masc. nom. sg., ... ’who’"), so nothing here is unprecedented. The glosser's claim holds up;
  confirmed correct, no fix needed. (The task description's own citation of "2.262" matches `units.json`'s
  `ln` for this unit exactly.)

### Verified and confirmed without change (method and representative sample)

Built a script-assisted map from all 241 novel keys to their occurrence(s) in `units.json` (241/241
matched; zero orphan keys), then read every entry against its line by hand: lemma correctness, part of
speech, and full agreement (case/number/gender for nominals and adjectives; person/number/tense/mood/voice
for verbs) with what the word actually does in its clause. No second error of the ἠγαθέην kind (an
inflected, non-headword form given as the lemma) turned up elsewhere — spot-checked this specifically by
programmatically flagging every entry whose lemma equals its own key, and hand-checking each: all were
either 1st-person-singular-cited defective/deponent verbs (εἶμι, γίγνομαι, πυνθάνομαι, μεγαίρω,
νεμεσίζομαι — correctly cited in their dictionary-standard 1 sg. present form), adverbs (σχεδόθεν, σχεδόν,
ἔνδοθι, ὄπιθεν, ἅλις — headword is the adverb itself), nouns whose nom. sg. coincides with the form in use
(βασιλεύς, γυνή, γόνος, δέμας, θυμός, μῆτις, ἐλπωρή, ἑταῖρος, ἔμπορος, ἤια), or 2-termination adjectives
already in their shared masc./fem. -ος form (νήπιος, πρόφρων, σκηπτοῦχος, χαλεπός, ἀνοήμων, ἀτέλεστος,
ἐπήβολος) — none of these needed a separate headword. Homeric-to-Attic equivalence is noted wherever the
spelling is not self-evident (ὀτρυνέει/ὀτρυνεῖ, τελέει/τελεῖ, ἀπέσσεται/ἀπέσται, ἔσσεαι/ἔσῃ, ἐσσὶ/εἶ,
καταπαυέμεν/καταπαύειν, πινέμεν/πίνειν, ἐσθιέμεν/ἐσθίειν, ἀγγελιάων/ἀγγελιῶν, ἐρετάων/-ῶν,
πλεόνεσσι/πλείοσι, πυκινοῖσιν/-οῖς, ἤλυθες/ἦλθες, ἦα/ἦν, and others) — all checked and correct.
Article-forms are correctly called pronouns for Homer wherever they occur (τῶ, "in Homer a pronoun ...
used adverbially"). The possessive ὅς/ἥ/ὅν is kept distinct from the relative ὅς/ἥ/ὅν throughout: ἑὰ and
the already-shipped ἑὸν are correctly confined to the possessive reading (no relative confusion), ἃ is
correctly confined to the relative reading ("ἃ μενοινᾷς ’what you desire’"), and the one genuine homograph
in this territory, ὃ, is correctly split by ` · ` in its broadening (see above) rather than merged or
mislabelled.

### Structural checks

- 241 novel entries in `gloss.json`, matching `novel-forms.json`'s 241 keys one for one (checked by
  script; zero missing, zero extra). 19 `__broaden__` entries.
- All 19 broadenings re-verified (after the three novel-entry edits above, which did not touch any
  broadening) to literally contain their `odyssey-glossary.json` old entry's exact text as a leading
  substring, with only new material after it — never shortened, reworded or replaced. Confirmed
  programmatically: 19/19 pass.
- No entry (novel or broadened) contains an ASCII apostrophe or backtick, before or after this pass's
  edits; English glosses use the typographic ’ throughout.
- Every entry is under the 230-character cap, before and after this pass's edits (longest entries, both
  pre-existing broadenings, sit at 226/230 — see the περὶ/τί discussion above).
- JSON re-validated after edits; novel-entry count unchanged at 241 (only values edited, no keys added or
  removed), broadening count unchanged at 19.

### Findings considered and refused

- **A stricter fix for περὶ/τί.** Considered rewriting either broadening to be more explicit within the
  remaining 4-character budget; no phrasing that adds real information fits. Considered instead trimming
  the *existing* (pre-broadening) text to make room, but that would violate the "old entry whole and
  unchanged" rule — refused. Left both as the glosser wrote them and recorded the tension above instead of
  acting unilaterally on a maintainer-level cap/completeness trade-off.
- **εἰδομένη's shipped "pres. part." entry itself.** Considered whether the underlying shipped
  (pre-existing) entry ought to be corrected, since Autenrieth's classification suggests it was wrong when
  first written. Out of scope: that text lives in `odyssey-glossary.json`, already published, and this
  review's edit access is to `drafts/odyssey-007/gloss.json` only; the additions-only convention is
  explicit that such an entry is broadened, never replaced. Flagged here for whoever next touches that
  earlier part's own review trail, but not acted on.
- **ἠγαθέην's "here treated as fem., as often in this formula" aside.** Checked against this same part's
  other Πύλος occurrence, 2.214's masc. Πύλον ἠμαθόεντα — confirmed the two really do differ in the
  gender of their agreeing adjective within this one part, so the aside is accurate, verifiable within
  this part, and not overreaching; left as is (only the lemma itself needed the fix, not this note).
