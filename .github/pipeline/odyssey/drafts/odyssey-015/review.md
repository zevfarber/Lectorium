# Review — odyssey-015 (Odyssey 4.113–218), pass 1 (translation)

Reviewed against `conventions.md`, `packet.md`, `new-renderings.md`, and the last unit of the
already-published `odyssey-014.json` (checked directly, not from memory), plus spot checks into
`odyssey-001.json` and `odyssey-002.json` for cross-referenced lines. Two full passes were made over
`units.json` (re-read fresh for the second pass); all fixes below were applied in place. `t` fields
were never touched. A script-assisted check confirmed the 56 units' `t` fields, concatenated in
order, reproduce packet.md's Greek for 4.113–218 exactly (no line dropped, added or moved).

Units are referenced by array index and by their `ln` (starting line number).

## Changes made

### Quotation marks and speech boundaries (the largest finding)

Systemic and structural. None of the file's 56 units carried a single “ or ” anywhere, despite six
marked speeches, and four of the six `mark` fields were on the wrong unit.

**No quotation marks at all.** Per conventions.md ("English layers carry ordinary “ ” quotation marks
round speech") and the pattern in the published odyssey-014.json (checked directly: e.g. its ln 31 and
ln 78 units both open with “ in `l` and `i`, and the speech-closing units close with ”), every one of
this part's six speeches needed an opening “ on the first unit of the speech and a closing ” on the
last, in both `l` and `i`. None were present anywhere in the draft. Added all twelve (6 speeches ×
open/close) in both layers.

**`mark` on the wrong unit, four times.** The house convention (explicitly stated by the drafter's own
note at unit ln 137: "This narrator's line announces the coming speech without quoting it... which is
why the following unit, not this one, carries the mark") is that `mark` and the opening quote belong on
the unit with the speech's actual first words, never on the narrator's reply-formula line that
introduces it. This was followed correctly for "Helen speaks" (ln 138) and "Peisistratus speaks" (ln
190) — both of which follow a plain narrator announcement, correctly left unmarked. But for the three
`τὸν/τὴν δ’ ἀπαμειβόμενος προσέφη ξανθὸς Μενέλαος·` reply-formula lines and the `τὸν δ’ αὖ Νεστορίδης
Πεισίστρατος ἀντίον ηὔδα·` line, the `mark` was placed on the formula line itself (pure narration, e.g.
"Him answering addressed fair-haired Menelaus:") rather than on the following unit where the speaker's
actual words begin — the same reply-formula pattern that, in the published odyssey-014.json, is
correctly left unmarked every time (verified directly: ln 30, ln 59, ln 76 are all unmarked
reply-formula/introduction lines, each followed by the actually-marked unit with the real first words).

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| all 6 speeches | l, i | error | No “ ” anywhere in the file, though 6 speeches are marked | Added opening “ to `l`/`i` of units 13 (ln138), 19 (ln148, after the mark move below), 23 (ln156, after the mark move), 29 (ln169, after the mark move), 39 (ln190), 49 (ln204, after the mark move); added closing ” to `l`/`i` of units 17 (ln144), 21 (ln151), 27 (ln164), 34 (ln181), 47 (ln201), 53 (ln214) |
| 18 (ln147) | mark | error | `mark: "Menelaus answers Helen"` sat on the reply-formula narration line, not on the speech | Removed the `mark`; added a sentence to the note explaining why; moved the mark (and opening “) to unit 19 (ln148), the actual first words |
| 22 (ln155) | mark | error | `mark: "Peisistratus answers"` sat on the `ἀντίον ηὔδα` narration line | Removed; moved mark + opening “ to unit 23 (ln156) |
| 28 (ln168) | mark | error | `mark: "Menelaus answers Peisistratus"` sat on the reply-formula line | Removed; moved mark + opening “ to unit 29 (ln169) |
| 48 (ln203) | mark | error | `mark: "Menelaus answers Peisistratus again"` sat on the reply-formula line | Removed; moved mark + opening “ to unit 49 (ln204) |

Verified after the fixes: exactly 6 `mark` fields remain (indices 13, 19, 23, 29, 39, 49), each on the
unit with the speech's actual opening words; exactly 6 “ and 6 ” in the file, correctly paired to the
same six speeches; unit 0 (ln113, the part's opening line) has no `mark` and no opening “, correctly
read as narration confirming the previous part's speech has closed, not as a new speech; the 10 `p:
true` paragraph flags (matching packet.md's 10 ¶ marks) were left untouched by this fix, since Murray's
paragraph breaks fall on the reply-formula lines themselves, independent of where the speech-quote
mark belongs.

### Augment mislabelling (the recurring class of error this project is warned about)

One genuine mislabelling was found: an augmented form called "unaugmented."

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 3 (ln 120) | n | error | ὥρμαινε called "unaugmented imperfect of ὁρμαίνω" — the root is ὁ-initial (ὁρμή), so the augment lengthens ο→ω; the text prints ὥρμαινε with omega, i.e. the augmented spelling. The unaugmented Homeric form would be ὅρμαινε (short ο) | Reworded to "augmented," with the ο→ω lengthening stated and the unaugmented alternative given for contrast |

All other augment/no-augment claims in the file were checked by hand against the actual spelling in the
line and found correct: βάλε, μερμήριξε, φέρεν (unaugmented) / ἔθηκεν (augmented) at ln114/123; ἔναι(ε)
(augmented, ln125) correctly described as showing "a plain ἐ- before the consonant-initial stem";
ἐέλδετο (ln162, correctly unaugmented — its ἐε- is inherited reduplication of the present stem, not a
second augment layer, since a genuine augment on an already-ε-initial reduplicated stem would lengthen
to η, giving ηελδετο, which is not what the text shows); ἔχεν (ln184, unaugmented, correct); μνήσατο
(ln187, unaugmented, correct — and cross-checked against 1.29, see below); ἀγόρευεν (ln189, unaugmented,
correct — α is not lengthened to η); ἴδον (ln200, unaugmented, correct, and matches conventions.md's own
worked example ἴδεν); διέκρινεν (ln178, correctly identified as augmented via an elided preposition
vowel, δι’ ἔκρινεν).

Two forms were left unresolved as genuinely indeterminate from spelling alone, following the exact
precedent set in odyssey-014's own review of this same phenomenon: ἵκεθ’ (ln169) and ἴαλλον (ln218) are
both ι-initial roots, where Homeric temporal augment (lengthening a short vowel to its long counterpart)
is orthographically invisible without a macron. odyssey-014's review explicitly flagged this exact class
and left it unchanged rather than guess; the same call is made here.

### Grammatical-label errors (non-augment)

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 3 (ln 120) | n | moderate | θυώδεος (agreeing with θαλάμοιο) called a "genitive in -οιο" — but θυώδεος is the genitive of the 3rd-declension adjective θυώδης, ending in uncontracted -εος (Attic -ους), not the 2nd-declension -οιο ending that θαλάμοιο and ὑψορόφοιο actually show | Split the claim: ὑψορόφοιο correctly kept as "-οιο"; θυώδεος reworded to "genitive in -εος (uncontracted, Attic -ους)" |
| 49 (ln 206) | n | moderate | "ἀρίγνωτος... governs the genitive γόνος ἀνέρος" — this is backwards. γόνος is nominative (subject of the implied copula, "the offspring is easily known"); ἀρίγνωτος is a predicate adjective agreeing with it, not a governing word; only ἀνέρος within the phrase is genitive, and it is governed by γόνος ("offspring of a man"), not by ἀρίγνωτος | Reworded: "ἀρίγνωτος is a nominative predicate adjective agreeing with γόνος... which itself governs the genitive ἀνέρος" |
| 46 (ln 201–202) | n | moderate | Claimed both περὶ δ’ ... γενέσθαι and πέρι μὲν θείειν show "anastrophe, accent thrown back, as already at 1.65–66" — checked the actual accents: only πέρι μὲν θείειν shows the recessive accent of anastrophe; περὶ δ’ ... γενέσθαι keeps the ordinary preposition accent (used adverbially, but not anastrophized). The cross-reference to 1.65–66 was also checked directly against odyssey-001.json: both instances of περί there (περὶ μὲν νόον ἐστὶ, περὶ δ’ ἱρὰ) are spelled with the ordinary accent too, so that passage does not in fact show anastrophe and cannot be cited as an "already" case | Reworded to correctly distinguish the two instances and dropped the false 1.65–66 citation for the anastrophe claim specifically (the general "adverbial περί" description of 1.65–66 remains valid and wasn't touched) |

### Cross-reference errors

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 11 (ln 136) | n | moderate | Cited "cf. 1.17" for ἦεν = ἦν — checked odyssey-001.json directly: the unit covering that stretch starts at `ln` 16, and ἦεν actually falls on the third line of that unit's `t`, poem line **18** ("πεφυγμένος ἦεν ἀέθλων"), not 17 | Corrected to "cf. 1.18" |
| 54 (ln 216) | n | major | "This line is identical to 4.217 from the already-published odyssey-014" — but 4.217 is *this part's own line* (the unit's `ln` is 216, spanning 216–217), not a line of odyssey-014. The genuinely already-published precedent for `ὀτρηρὸς θεράπων ... κυδαλίμοιο` is at 4.23 (confirmed in conventions.md's house table and in packet.md's "already stands in a published part" note, which documents that 4.217 here repeats the Greek of the unit at odyssey-014's `ln` 22, i.e. line 23 there) | Reworded to correctly say the house-fixed wording comes from 4.23 (in odyssey-014), and that *this* line, 4.217, repeats that same Greek verbatim and must (and does) match the wording already shipped there |

All other cross-references in the file were checked and found accurate: 1.29 (μνήσατο γὰρ κατὰ θυμὸν
ἀμύμονος Αἰγίσθοιο — confirmed in odyssey-001.json, itself glossed there as "μνήσατο is unaugmented");
1.31 (τοῦ ὅ γ’ ἐπιμνησθεὶς — confirmed, exact construction present in odyssey-001.json at that line);
3.442 and 3.448 (μενεπτόλεμος and ὑπέρθυμος of Thrasymedes — confirmed against conventions.md's house
table, which cites those same two lines for those two words); 4.111 (ἐχέφρων Πηνελόπεια — confirmed
against conventions.md's table); the odyssey-014 cross-reference in unit 0's note (Menelaus's speech
"left open... (4.78–112)" — confirmed directly against odyssey-014.json: its `mark` "Menelaus answers"
starts at `ln` 78 and the file's last unit ends at line 112 with no closing quotation mark, exactly as
described); all internal cross-references within this same part (4.113↔4.183 tmesis note, 4.115↔4.154
gesture repeat, 4.138↔4.156 διοτρεφές, 4.147↔4.168/4.203 reply-formula, 4.158↔4.195 νεμεσσ- root,
4.164↔4.187 "father who is gone", 4.187 Antilochus named only at 4.199).

### House-table / new-renderings.md wording collision

| Unit (ln) | Field | Severity | What was wrong | Fix |
|---|---|---|---|---|
| 24 (ln 158) | l, i, n | moderate | σαόφρων (of Telemachus, "self-controlled, of sound mind") was translated "sound-minded" / "sound of mind" — but "sound-minded" is already the house-fixed rendering of the *different* epithet ἐχέφρων Πηνελόπεια (conventions.md, 4.111), which the table explicitly reserves as distinct from the other φρήν-compounds. Using the same English for a different Greek word contradicts the table's own stated policy (spelled out at length in its own ἐχέφρων row) of never collapsing distinct φρήν-compounds into one English word | Changed to "self-possessed" in both `l` and `i`; reworded the note's dictionary gloss and added a sentence explaining the avoidance of "sound-minded" and why |

### The `about` field

| Field | Severity | What was wrong | Fix |
|---|---|---|---|
| about | moderate | Claimed "Menelaus's memories of Odysseus and of **his own long exile** set the whole company weeping." Checked the actual content of Menelaus's second speech (4.169–182): it recalls Odysseus's toils at Troy and imagines a homecoming and shared life in Argos that never happened — it does not mention Menelaus's own wandering/exile at all (that theme belongs to later stretches of Book 4, outside 4.113–218) | Reworded to "Menelaus's memories of Odysseus's own hardships, and his regret that the two of them never shared a home together, set the whole company weeping" — accurate to what this part actually contains |

## Findings considered but NOT changed, with reasons

- **new-renderings.md — κυνῶπις rendered "dog-faced" / "shameless" (used at ln 145):** ὤψ, the second
  element, is literally 'eye/face', and the house table's existing practice for -ωπ- compounds is
  "-eyed" (γλαυκῶπις Ἀθήνη → "gleaming-eyed"). "Dog-faced" is a defensible traditional gloss and not
  wrong, but it breaks with the established -ωπ- → "-eyed" pattern and isn't flagged as a deliberate
  departure anywhere in new-renderings.md's own "avoided on purpose" column (which considers and
  rejects "shameless-eyed" for a different reason — losing κύων — without ever weighing "dog-eyed").
  This is a real, if minor, internal-consistency question, not a clear error, and changing it would mean
  touching both `new-renderings.md`'s own fixed row and two units' `l`/`i`. **Flagged here for the
  orchestrator's judgment rather than changed**, since it's a defensible translation choice, not a
  wrong one.
- **Unit 39 (ln 190), Ἀτρεΐδη used alone, rendered "Son of Atreus" without "the":** conventions.md's
  house table fixes "Ἀτρεΐδης / Ἀτρεΐδην used alone as a name-substitute" as "**the** son of Atreus" in
  both layers, citing 3.193 (accusative, non-vocative). Here the usage is vocative ("Ἀτρεΐδη," direct
  address), where English vocatives don't normally take a definite article ("O son of Atreus," not "O
  the son of Atreus"). This is a grammatically motivated departure for a case-use the house-fixed row
  doesn't actually cover (that row's precedent is accusative), not a violation of it. Left unchanged.
- **ἵκεθ’ (ln 169) and ἴαλλον (ln 218), both called "unaugmented":** both are ι-initial roots where the
  temporal augment is orthographically invisible (a short vowel lengthens to the long vowel of the same
  letter, unmarked in this edition's text). Could not confirm or disprove from spelling alone; no
  scansion data is available for these specific lines (packet.md flags no lines in this part for hand
  scansion). This mirrors exactly the class of form odyssey-014's own review flagged and left unresolved
  for the same reason. Left unchanged rather than guess.
- **Unit 8 (ln 131), "ἀργύρεον, held over from line 131 by enjambment, agrees with τάλαρον":** ἀργύρεον
  is physically the first word of line 132, not 131; the note's phrasing (that the sense is "held over
  from line 131," i.e. carried by enjambment from the noun phrase begun there) is correct in substance,
  if slightly compressed. Not changed — a stricter reading of the words could momentarily suggest
  ἀργύρεον itself sits in line 131, but the note is describing the enjambment relationship accurately,
  and this unit's own `ln` is 131, so "held over from line 131" is naturally read as "from earlier in
  this unit."
- **Quotation marks — the part's own opening (item 8 of the runbook):** confirmed unit 0 (ln113) has no
  `mark` and no opening “, correctly reflecting that this line is narration confirming the close of
  Menelaus's speech from odyssey-014, not a new speech of its own. Checked directly against
  odyssey-014.json's actual last unit: it ends at line 112 with no closing quotation mark and its own
  note says explicitly "the part ends here still inside Menelaus's speech... no closing quotation mark
  is given" — matching exactly what this part's unit 0 note claims about it.
- **Scansion (item 9):** packet.md reports no scansion flags for this part, and none of the units carry
  an `sc` field (expected — scansion is added by the production script later, not at draft stage). No
  hand-scanning was needed.
- **Stock epithets (item 10), broad sweep:** spot-checked every recurring fixed rendering actually used
  in this part against conventions.md's table (re-read directly, not from memory) — ξανθὸς Μενέλαος
  (3×), διοτρεφής (2×, singular vocative applications of the table's plural διοτρεφέες βασιλῆες root),
  κατὰ φρένα καὶ κατὰ θυμόν (2×), ὣς φάτο (2×), ἔπεα πτερόεντα (with a varying verb, as the table's own
  odyssey-014 precedent allows), ἀμύμων, ἀγλαός, Γερήνιος ἱππότα Νέστωρ, ὄρχαμος-variant ὄρχαμε λαῶν,
  εὐρύοπα Ζεύς, νηῦς θοή (pluralized), τὴν/τὸν δ’ ἀπαμειβόμενος προσέφη ξανθὸς Μενέλαος (3×), πεπνυμένος
  (twice, both generalized beyond Telemachus but keeping the fixed word), Ἀτρεΐδης/Ἀτρεΐδη patterns for
  Menelaus (extending the already-established odyssey-014 precedent for that name). All consistent
  except the σαόφρων collision fixed above.
- **Remembered-translator English (item 7):** read every `i` field for phrasing that might echo a known
  modern translator rather than being built fresh from the Greek. Nothing found that reads as
  distinctively borrowed; renderings like "the black cloud of death had closed over us" are direct
  images from the Greek (θανάτοιο μέλαν νέφος) rather than an imported phrase. No changes.
- **Text-completeness check:** script-verified that all 56 units' `t` fields, concatenated in the
  file's order, reproduce packet.md's Greek for 4.113–218 character-for-character (after normalizing
  whitespace/line breaks). No line dropped, duplicated or reordered.
- **`p`/paragraph accounting:** all 10 of packet.md's ¶ marks have a matching `p: true` unit at the same
  `ln`, and no extra `p: true` appears elsewhere. Confirmed unaffected by the `mark`-relocation fix
  above (paragraph breaks and speech-quote marks are independent).
- **The two already-published lines (4.217, 4.218):** both checked byte-for-byte against packet.md's
  quoted published wording (from odyssey-014 and odyssey-002 respectively) and found to match exactly
  in `l` and `i` (differing only in trailing punctuation where a unit's own sentence structure requires
  it, e.g. 4.217 here ends the unit with a period where the odyssey-014 source has a comma mid-sentence
  — the underlying wording is identical).

## JSON validity

Ran from `/home/user/Lectorium`:

```
python3 -c "import json; json.load(open('.github/pipeline/odyssey/drafts/odyssey-015/units.json'))"
```

Result: **parses successfully, no errors.** Re-verified after every edit and again at the end: 56
units, all `t`/`l` newline counts match, all `i` fields newline-free, no unit's `t` exceeds 4 lines,
all `v: true`, exactly 10 `p: true` flags matching packet.md's paragraph marks, exactly 6 `mark` fields
each on the correct unit, and exactly 6 matched “/” pairs across the file's six speeches.
