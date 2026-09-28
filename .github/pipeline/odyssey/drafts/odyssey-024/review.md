# odyssey-024 (5.192–290): review, pass 1 (translation)

Reviewer pass 1 of 2. Only `units.json` fields `l`, `i` and `n` were edited. No `t`, `mark` or `p` was
touched. The concatenated `t` still reproduces Murray 5.192–290 exactly. Each `l` has the same line
count as its `t`, and no `i` contains a line break.

**Changes: 32 field edits in 24 units.** High/major 0 · moderate 11 · minor 21.

## Structural checks (all pass, no change)

- **Paragraphs.** `p: true` falls at 192, 203, 214, 225, 228, 262, 282 and 286. These are exactly
  Murray's breaks inside 192–290. Murray's next break is at **291** (ὥς εἰπὼν σύναγεν νεφέλας), which
  confirms that the part ends cleanly after 290.
- **Entry from odyssey-023.** The published file's last unit (5.190–191) ends
  `…ἀλλ’ ἐλεήμων.` and closes its `”` in both `l` and `i`. No speech is left open into this part, and
  5.192 opens with plain narration.
- **Speeches.** Each speech has `“` on its first unit in `l` and `i`, `”` on its last unit in `l` and
  `i`, and a `mark` on its first unit. There are no stray quotation marks.
  - Calypso: opens 203 ("Calypso speaks"), closes 211–213.
  - Odysseus: opens 215 ("Odysseus answers"; Murray's ¶ is at 214, the reply-formula), closes
    224b.
  - Poseidon: opens 286 ("Poseidon speaks to himself"), closes 290.
- **Scansion flags.** None were reported in the packet, so this step does not apply.

## Repeated lines: all checked against the shipped files, byte for byte

| Here | Shipped | Result |
|---|---|---|
| 5.193b ὁ δ’ ἔπειτα μετ’ ἴχνια βαῖνε θεοῖο. (whole unit) | odyssey-008 2.406, odyssey-009 3.30 | `l` and `i` identical ✓ |
| 5.200 (whole unit) | odyssey-002 1.149 (also 4.67, 4.218) | `l` and `i` identical ✓ |
| 5.220 line inside unit 219–220 | odyssey-011 3.233 | `l` line "to come home and see the homecoming day" ✓; `i` clause "to come home and see the day of my homecoming" ✓ |
| 5.225 (whole unit, differs only by final ν and ano teleia) | odyssey-012 3.329 | the same words, with `;` for `.` ✓ |
| 5.228 dawn line | odyssey-005 2.1, table row 168 | ✓ |
| 5.202 τοῖς ἄρα μύθων ἦρχε … | odyssey-009 3.68 "among them then of speeches made-beginning" / "was the first to speak among them" | ✓ |
| 5.286 ὢ πόποι, ἦ μάλα δή | odyssey-015 4.169 "Ah! Truly, indeed," / "Ah, truly" | ✓ |
| ὅθι δένδρεα μακρὰ πεφύκει 238 = 241b | internal | `l` ✓. The `i` did **not** match: 241 read "where *the* tall trees". Fixed (see below). |
| Καλυψώ, δῖα θεάων 202/242/246/258/276 | internal and 5.85, 5.116, 5.180 | `l` "Calypso, heavenly-one of goddesses", `i` "Calypso, heavenly even among goddesses", identical in all five ✓ |

House-table recurrences were checked at every occurrence, not only the first:

- δῖα θεάων (192, bare), δῖος Ὀδυσσεύς (269) and δῖα Καλυψώ (263): all "heavenly".
- θεῖος (198): "divine".
- πολυμήχανος (203) and πολύμητις (214): kept apart as the table requires.
- διογενής (203): `l` "Zeus-sprung", `i` "Zeus-born".
- μεγαλήτωρ (233), γλαφυρός (194, 226), ἐύξοος (237), οἶνοψ πόντος (221), ἠεροειδὴς πόντος (281),
  περίφρων (216), νόστιμον ἦμαρ (220), ὣς ἔφατ’ (225), ὣς ἄρα φωνήσασ’ (192), σχεδίη (251) and
  ἐνοσίχθων (282): all ✓.

## ἅλα δῖαν (5.261): drafter's flag (a)

**Decision: keep "the heavenly brine" in both `l` and `i`.** No change.

1. Table row 274 fixes δῖος as "heavenly" for places too, and it lists "bright" among the renderings
   avoided on purpose. The shipped "bright" in `i` is recorded there as a known slip that was left as
   shipped. It is not a precedent.
2. There is no single shipped `i` to be consistent with. 3.153 has "bright salt sea" and 4.577 has
   "bright sea". The only thing both shipped instances agree on is the `l` "heavenly brine", and
   5.261 matches that.
3. The exact-repeat rule governs whole lines and units. 5.261 (μοχλοῖσιν δ’ ἄρα τήν γε κατείρυσεν…)
   repeats neither 3.153 nor 4.577, so nothing requires the split.

Recommendation for QUESTIONS.md or the publisher: row 274 should now say that "heavenly brine" in
both layers is the rule from odyssey-024 on. The two earlier `i` renderings stay as shipped.

## Uncertain technical terms: drafter's flag (b)

Every term was checked against the unit's note. Each one is honestly hedged, and none is silently
resolved:

- σκέπαρνον: "usually … adze … exact shape is not certain".
- ἁρμονίαι: three proposals are named.
- σταμῖνες: ribs or uprights, "uncertain".
- ἐπηγκενίδες: "exact referent is uncertain".
- ὕλη (257): three proposals, "does not choose".
- ὑπέραι, κάλοι, πόδες: "usual lexicon senses; exact rigging not fully known". An alternative is
  also given for κάλοι.
- οἰσύα: "exact plant is not certain".
- περίκηλα: "sense is inferred".
- ἀκαχμένον: "obscure formation".
- ῥινόν: "disputed in antiquity … not a certain one".
- πεῖραρ: both readings are given.
- ἔπ’ (251): "force debated".
- ὀψὲ δύοντα: "usually explained".
- The tree-names (κλήθρη and the others) and the axe's double edge are also hedged.

ἐπίκριον "yard" and γόμφοι "pegs, bolts" are stated plainly. Both are the standard LSJ and Cunliffe
senses, and that is acceptable.

## Changes made

Each entry gives line · field · severity · problem → action.

### Grammar and labels in notes

- **243 · n · moderate.** ἤνυτο was parsed as the imperfect of ἀνύω. The thematic ἀνύω would give
  ἠνύετο; ἤνυτο belongs to the athematic ἄνυμι (Cunliffe s.v. ἄνυμι). → The note now reads "imperfect
  passive of ἄνυμι, the athematic by-form of ἀνύω".
- **247 · n · moderate.** τέτρηνεν was called "a reduplicated aorist". That is misleading: the τε-
  belongs to the stem of τετραίνω in every tense, and this is an ordinary unaugmented aorist (Attic
  ἐτέτρηνε). → Corrected.
- **198 · n · moderate.** ἷζεν was called "unaugmented". The ι of ἵζω is short, so the circumflexed
  ἷζεν points to a long ι, which is most naturally the temporal augment. At best the label cannot be
  verified. → The note now reads "the imperfect of ἵζω", with no claim about augment.
- **194 · n · minor.** ἷξον was called "unaugmented". With ἵκω (ῑ) the augment cannot be seen, and
  shipped notes differ on the point (3.495 has no such label; 4.1 says "unaugmented"). → The note now
  uses the neutral wording shipped at 3.495: "an aorist … formed with -σ- and the endings of the
  imperfect".
- **244 · n · minor.** ἴθυνεν was called "unaugmented". The line end στάθμην ἴθυνεν scans with a long
  first syllable, so the label cannot be verified and is probably wrong. → The note now reads "the
  aorist of ἰθύνω".
- **290 · n · minor.** ἐλάαν was called an "uncontracted" future infinitive. It is diectasis of the
  contracted ἐλᾶν, not an uncontracted form (the shipped 3.484 note says this correctly). The
  future-infinitive reading here is right (LSJ cites Od. 5.290). → Reworded, with a cross-reference to
  3.484. The meta sentence "the closing quotation mark is given here" was also cut, because a note is
  addressed to the reader and not to the editor.
- **260 · n · minor.** "doubles the preposition" was wrong: ἐν appears three times (adverb, prefix, and
  preposition with αὐτῇ). → Corrected.

### Cross-references in notes

- **194 · n · minor.** "mortal food, set against the next line" was wrong: the next line (198) has no
  ambrosia, which comes at 199. → The note now reads "set against the ambrosia and nectar of 199".
- **201 · n · minor.** "the table's speech-introduction τοῖς ἄρα μύθων ἦρχε" was inexact. The table
  row (289) is τοῖσι δὲ μύθων ἦρχε, and τοῖς ἄρα is the variant shipped at 3.68. → The note now
  names 3.68 and the table variant.
- **224 · n · minor.** "Odysseus' reply is as long as Calypso's speech" was false: hers runs 11 lines
  (203–213) and his 10 (215–224). → The note now reads "nearly as long".

### Internal repeat

- **241 · i · minor.** The `i` read "where *the* tall trees had grown", but at 238 it reads "where tall
  trees had grown". The drafter's claim of identical English was therefore untrue for `i`. → The
  article was dropped to match 238.

### English that arrived pre-formed (conventions: "rebuild from the case relations")

Several `i` phrases matched, or nearly matched, the wording of Murray's 1919 English version from
memory. Murray may be used as a silent meaning-check, but never for wording. Where a phrase was only
the forced literal rendering of the Greek, and hard to avoid, it was left alone (see Rejected).

- **205 · i · moderate.** "Still, fare you well, all the same" matched Murray's "fare thou well even
  so" and was also archaic. → "But farewell to you, all the same."
- **224 · i · moderate.** "let this be added to the rest" matched Murray's "let this also be added unto
  that". → Rebuilt from μετὰ … τοῖσι γενέσθω: "let this too come to pass along with them."
- **226 · l, i · moderate.** "took their joy in love" matched Murray's "took their joy of love".
  → "took delight in love" in both layers. This fits the note's gloss of τέρπομαι as "take delight"
  and keeps "love" for φιλότης, as in table row 390.
- **233 · i · moderate.** "she set about planning the voyage home" matched Murray's "set about
  planning the sending". → "she began to plan how great-spirited Odysseus should be sent on his way".
- **278 · i · moderate.** "where it lay nearest to him" matched Murray. → "at the point where it was
  nearest to him".
- **194 · i · moderate.** "sat down on the chair from which Hermes had risen" matched Murray.
  → "there he sat down on the very chair Hermes had risen from". The same edit changes "before him" to
  "beside him", which follows πάρα and the unit's own `l`.
- **290 · i · moderate.** "But I tell you, I will still drive him till he has his fill of evil" was
  colloquial, and "I tell you" is odd in a speech to his own heart. It was also close to Murray's "to
  his fill of evil". → "But even so, I say, I will yet drive him on until he is sated with evil." The
  `l` keeps the literal "to his fill of evil".
- **235 · i · minor.** "and in it was a very beautiful handle of olive-wood" was close to Murray.
  → "and fixed in it was a haft of olive-wood, very beautiful and well fitted". This also uses the
  `l` word "haft".
- **237 · l · minor.** "and she gave him next a well-polished adze" was close to Murray. → "and she
  gave him then an adze, well-polished;". This is closer to the Greek order: ἔπειτα, then σκέπαρνον
  ἐύξοον.
- **252 · l, i · minor.** "worked at it" / "worked on it" was close to Murray's "worked on", and drifted
  from the note's "went on making". → `l` "he went on making it"; `i` "and went on building".
- **253 · i · minor.** "finished it off" matched Murray's "finish off". → "completed it".
- **256 · l, i · minor (precautionary).** "from end to end" and "a bulwark against the wave" may echo
  Murray. → "all along" / "all along its length", and "a shelter against the wave". Both follow the
  note's own glosses, διαμπερές "all along" and εἶλαρ "defence, shelter".
- **258 · i · minor.** "brought him cloth to make sails" was close to Murray's "cloth to make a sail",
  and it lost the plural φάρεα. → "woven cloths for making sails".
- **259 · l · minor.** "skilfully fashioned these too" was close to Murray. → "he well crafted these
  too", which follows the Greek order εὖ τεχνήσατο.
- **263 · i · minor.** "when she had bathed him and dressed him in fragrant clothes" copied Murray's
  construction, and it undid the hysteron proteron that the unit's own note points out. → "having put
  fragrant clothes on him and bathed him", which keeps the Greek order.

### Other `i` fixes

- **218 · i · minor.** "for she is mortal, and you are immortal and ageless" was verbatim Murray. The
  line leaves little room, so it was only lightly varied → "for she is a mortal, while you are immortal
  and ageless". The adversative "while" also follows μέν … δέ.
- **237b · i · minor.** "long since dead and dry" added "dead", which is not in αὖα πάλαι. → "long
  since dry".

## Findings considered and rejected (left as drafted)

- **ἅλα δῖαν (261)**: see the decision above. No change.
- **203 · n · low.** The note glosses διογενής as "Zeus-born", but the `l` has "Zeus-sprung". This is
  not a contradiction: the `i` has "Zeus-born", and table row 210 fixes the split. Left.
- **210, 219 · i · low.** Table row 281 gives the `i` for ἤματα πάντα as "for all your days", but
  here it is "all your/my days". The row itself is swapped against what shipped at its source line
  (4.592: `l` "for all your days", `i` "all your days"), and other shipped parts vary. Left. This is
  a table-hygiene item for the publisher (QUESTIONS.md).
- **Forced literal matches with Murray**, left because the Greek allows almost nothing else. These
  are "fitted them to one another" and "with pegs and joinings hammered" (247–248); "nor did sleep fall
  upon his eyelids" (271, in `l`); "has no share in the baths of Ocean" (275); "the great bond of
  misery" (289, πεῖραρ, hedged in the note); "such as mortal men eat" (197); "the lord earth-shaker,
  returning from the Ethiopians" (282, a new table row in Greek order).
- **247 · n · low.** "γόμφοι … wooden dowels". The "wooden" is not in the word, but it is the
  standard sense of trenail pegs in LSJ and Cunliffe. Left.
- **205 · n · low.** "making plain that she disapproves" slightly over-reads ἔμπης. It is tolerable as
  a tutor's gloss. Left.
- **5.274 · n · low.** "From Greece the Bear never sets". This is true for Homer's latitude and epoch.
  Left.
- **5.290 ἐλάαν as a future.** Checked, and correct (LSJ). The draft's `known-forms.json` gloss gives
  only the present infinitive. **For the glossary stage**: broaden the ἐλάαν entry with
  "· also fut. inf. (Od. 5.290)", following the additions-only rule.
- **new-renderings row οὖρος ἀπήμων.** The row lists "safe" as avoided because it drops πῆμα, but
  odyssey-018 shipped νόστος ἀπήμων (4.519) as "a safe return". The phrase is different, so there is
  no conflict in this part. The publisher should note the inconsistency when the row is folded in.
- **new-renderings row μέλας οἶνος "dark wine".** This splits μέλας from the table's "black" of
  θοὴ/κοίλη νηῦς μέλαινα. The split is justified by English idiom and is disclosed in the row. Accepted.
- **The other seven new-renderings rows** (διογενὲς Λαερτιάδη…, the πολύμητις reply-formula, πότνα
  θεά, κρείων ἐνοσίχθων, κινήσας … θυμόν, ὄρεα σκιόεντα, φορτὶς εὐρεῖα) are sound and agree with the
  house table and the shipped precedents: 4.22 κρείων "lord"; 1.14 and 4.513 πότνια "lady"; 1.4 θυμός
  "heart" (row 278 NB); 1.365 and 4.768 σκιόεντα "shadowy". The count "eleven lines earlier"
  (214 − 203) is correct.

## Unresolved, for QUESTIONS.md

1. Row 274 should be updated to record that "heavenly brine" in both layers is the rule from 5.261 on.
2. Row 281 (ἤματα πάντα): the `l`/`i` columns are the reverse of the shipped 4.592.
3. οὖρος ἀπήμων row versus the shipped νόστος ἀπήμων "safe return" (4.519).
4. Glossary: the ἐλάαν entry should add the future-infinitive sense.
5. Past notes differ on ἷξον ("unaugmented" at 4.1, neutral at 3.495). Recommend the neutral wording
   poem-wide.
