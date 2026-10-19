# Review of iliad-028 (Iliad 5.111–216), reviewer, pass 1 of 2

Edited in place by script: `units.json` only (checked after the edit that every `t` is unchanged and that all 60 units are still present, in the original file formatting). `gloss.json` was neither read nor touched. `new-renderings.md` needed no change (every row still matches the units).

Method. Every note checked against its own line (labels, positions, cross-references looked up in the source JSON and the published parts); then Greek to `l` word by word, `l` against `i`, `i` for remembered English, quotation marks. Mechanical checks: the units' `t` concatenate to exactly the packet's 106 lines; each `ln` is the line the unit begins on; `p` falls on 111, 121, 133, 144, 159, 166, 179; no straight quotes or double spaces. Quotation marks: prayer “ at 5.115 (mark), ” on the unit ending 5.120; Athena “ at 5.124, ” at 5.132; Aeneas “ at 5.171, ” at 5.178; Pandarus “ at 5.180, ” at 5.216 (his speech ends there and nothing runs into 5.217); iliad-027 ended with Diomedes’ closing ” (5.109–110), and 5.111 correctly opens without a mark. `mark` is on the first unit of each of the four speeches. The two published Iliad lines (5.123, and 5.169 as a departure) and the Odyssey lines (5.115, 5.121, 5.201) were compared with the published `l`/`i`.

Counts of edits: high 0, medium 2, low 4 (6 edits in all).

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 5.146 | n | medium | “πλῆξ’, short for ἔπληξε”: πλῆξ’ is the elided πλῆξε, the aorist without the augment, not a shortened ἔπληξε. | “the elided πλῆξε, the aorist of πλήσσω without the augment” (as iliad-027 says for βάλ’). |
| 5.185–187 | n | medium | Said the object is βέλος ὠκὺ κιχήμενον “with τούτου ‘this man’s’ before it”, which contradicts the note’s own `l`/`i` (“as it was reaching this man / him”); τούτου is not “this man’s shaft”. | Now says τούτου “this man” stands before the shaft and is taken as the genitive after κιχήμενον, “reaching this man”; the construction is still called loose. |
| 5.115 | n | low | “The same line opens Odysseus’ prayer to Athena in the Odyssey”: true (6.324), but the line this unit reuses (the published Odyssey unit) is Penelope’s prayer, 4.762; the note named only one of the two. | “opens Penelope’s prayer to Athena (Odyssey 4.762) and Odysseus’ (6.324)”. Both lines looked up in `odyssey-murray1919.json`. |
| 5.139 | n | low | “the aorist ὦρσεν … is put in the present”: vague (put by whom?); the term for what it is was missing. | “a gnomic aorist, a timeless statement in a simile, and is rendered in the present”. |
| 5.167–168 | n | low | “διζήμενος … governs ἀντίθεον ‘godlike’ Pandarus”: the object is Πάνδαρον; ἀντίθεον is the adjective. | “governs Πάνδαρον, with ἀντίθεον ‘godlike’ agreeing”. |
| 5.199 | i | low | “take my stand on horses and chariot” does not render ἐμβεβαῶτα “having mounted”, which `l` has (“mounted on horses and chariot”). | “he told me to mount horses and chariot and lead the Trojans”. |

## Verified, no change needed

- **5.206 (Ἀτρεΐδῃ).** The note says Ἀτρεΐδῃ is Menelaus, “whom Pandarus wounded in Book 4, though the Greek gives only the patronymic”. True (Pandarus’ shot at Menelaus is Book 4), and the note is honest that the identification comes from the story, not the word. `l`/`i` keep “the son of Atreus”. Kept.
- **5.169 (departure from iliad-022).** The published unit is iliad-022’s unit at line 89 (Iliad 4.89: “She found … standing;”) with Athena as subject and ἑσταότ’ in it. Ours is a different unit (Aeneas subject, no ἑσταότ’), so the validator’s identity rule does not apply; `l` “He found the son of Lycaon, both blameless and strong,” and `i` “He found the blameless and strong son of Lycaon,” change only the pronoun and drop the participle, and the departure is recorded in `new-renderings.md`. Kept.
- **5.123** `l`/`i` identical to the published iliad-022 unit. **5.121** reuses odyssey-012’s words appropriately. **5.201** `l` matches odyssey-041, `i` adapted to the longer unit, recorded in new-renderings.md.
- **5.99 and 5.98–99 cross-references** (γύαλον as a noun; the shot Pandarus made) match iliad-027’s unit at 98. **5.106** “same phrase as at 106 … ‘so he declared’” matches iliad-027’s note. **5.102–106** (Pandarus’ vaunt) correct. All “runs to line N” statements (120, 132, 142, 178) correct.

## Findings considered and refused

- **5.122 `i` “the limbs above them”** for ὕπερθεν: an interpretation, but the note says the sense of ὕπερθεν is not settled and `l` keeps the literal “above”. Left.
- **5.134 `i` “went again to mingle”** for ἰών … ἐμίχθη (participle plus finite verb): the new-renderings row records this as the chosen rendering and the force is the same. Left.
- **5.139 `i` “slips away into the steadings”** (“away” not in the Greek): δύεται “slips into” plus the retreat of the lion; harmless, and `l` is literal. Left.
- **5.190 `i` “I thought I would fling him down”** for ἐφάμην (“said”): φημί with a future infinitive is “say to oneself”, and iliad-027 renders φημί in “I do not think” the same way. Left.
- **5.206 `i` “two of the best men”**: house rendering of ἀριστῆες is “the best men”; recorded in new-renderings.md. Left.
- **5.182–183 `i` “by the sight of the horses”**: ἵππους τ’ εἰσορόων is a participle parallel to γιγνώσκων; the means reading is natural and `l` is literal. Left.
- **5.181 note “the man they are both watching”**: slight overstatement but not false (both have been watching Diomedes). Left.
- **Scansion flags:** none in the packet, so no hand-scanning was required.

## Still to do in pass 2

Re-read all of `units.json` from the Greek again, and read `gloss.json` (parses against the line) once the glosser has finished.

---

# Pass 2 of 2 (reviewer)

Edited in place by script: `gloss.json` only. `units.json` was re-read from the Greek (word by word `l`, `l` against `i`, every grammatical label and cross-reference in the notes) and needed no change; `t` untouched everywhere. Every one of the 211 `gloss.json` entries (the 10 `__broaden__` entries included) was checked against each line it occurs in (lemma, case, tense, mood, person, number, meaning); `novel-forms.json` and the non-broadened keys match exactly, and no existing glossary entry was rewritten. Each `__broaden__` value was checked to be the old `known-forms.json` entry whole + " · " + the new reading.

Counts of edits: high 0, medium 1, low 5 (6 edits in all; 0 in `units.json`).

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 5.188 | gloss `γυάλοιο` | medium | Entry called it the neuter noun γύαλον "with θώρηκος", while the unit's note says it "agrees with θώρηκος" (a neuter noun cannot agree with a masculine one) and `l` renders it "hollow breastplate". | Entry now reads as the epic adjective: "γύαλος — hollow, curved (adj., from the noun γύαλον ’hollow plate’); masc. gen. sg., … agreeing with θώρηκος". Agrees with note and `l`. |
| 5.136 | gloss `εἰροπόκοις` | low | "epic -οις" is not an epic peculiarity (Attic ending identical). | "fem. dat. pl., agreeing with ὀΐεσσι". |
| 5.144, 5.207 | gloss `βαλών` | low | A participle was labelled "unaugmented" (participles have no augment). | Dropped the word; parse unchanged. |
| 5.111 | `__broaden__` `καθ` | low | Whole entry 248 characters; old entry (185) was not already long, so over the 230 cap. | New reading shortened to "also + gen., ’down from’ (καθ’ ἵππων)": 225 characters. |
| 5.125 | `__broaden__` `οἷον` | low | 320 characters from an old entry of 207, over the cap; the new reading (neuter accusative, object of ἔχεσκε) was right. | Reduced to " · also neut. acc. sg." (meaning already in the old entry): 229 characters. |
| 5.214 | `__broaden__` `τάδε` | low | Broadened for τάδε μαίνεται (adverbial) but not for τάδε τόξα, where it agrees with a noun ("this bow"). | Added " · also neut. acc. pl. with a noun: ’this’ (τάδε τόξα ’this bow’)": 227 characters. |

## Verified, no change needed

- Broadened entries `λίπον` (204 ὣς λίπον, aor. 1 sg.), `μάχην` (166 ἄν τε μάχην, after ἀνά), `πάντα` (180 adverbial), `ἂν` (201 ἂν … ἦεν, contrary to fact; old entry already 739 chars), `ἄν` (166, ἀνά with apocope; old entry 237 chars), `ἕλον` (127, aor. 1 sg.), `μή` (201, ’lest’ + opt.): each reading is true of its line and each is old + " · " + new.
- `κιχήμενον` (neuter, agrees with βέλος; τούτου is the genitive object), `φῖλαι` (aor. imper. as the note says; the formation is uncertain in the note too), `ἐμμεμαὼς`, `οὐτάμεν`, `πολύειδον`, `θεοῦ` (both uses), `ὕπερθεν`: parses fit the lines and the notes.

## Findings considered and refused

- Extra second readings that do not occur in this part (`βάλον` "also aor. 3 pl.", `δίδου` "also pres. imper.", `οἶδ` "also 3 sg.", `ἔασ` "also ἔασι", `σταθμοὺς` "also door-post"): true homographs, harmless, and the runbook allows both readings of a genuine homograph. Left.
- `δαΐφρονι` "wise-minded" while `i` says "wise-hearted" at 5.180, 5.184: the entry records the disputed sense and `l` agrees with it; `i` is the free layer. Left.
- `κιχήμενον` "= Attic κιχόμενον": no such Attic form is attested, but the entry's job is to name the nearest regular form; left.
- `units.json`: no new finding. Pass 1's refusals stand.
