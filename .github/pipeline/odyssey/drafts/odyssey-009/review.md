# Review: odyssey-009 (Odyssey 3.1–101)

I checked this part against `conventions.md`, `packet.md`, `new-renderings.md`, `LOG.md`, the source archive
(`source/odyssey-murray1919.json`, for the line after the part) and the published `odyssey-001` to
`odyssey-008.json` at the repository root. Every repeated line and cross-reference was checked against those
shipped files, not against the packet's transcription. I did two passes. Pass 1 covered the translation: all 63
units. Pass 2 covered the glossary: all 242 novel entries and all 9 broadenings, plus a check of every known form
against its shipped entry for this part's uses.

Mechanical checks were run by script before and after the edits. The concatenated `t` reproduces `packet.md`
exactly, including the mid-line joins at 3.20, 3.22, 3.71 and 3.80. `p: true` falls exactly on Murray's 12 ¶
lines (1, 14, 21, 25, 29, 43, 51, 55, 62, 69, 75, 79). Every `l` has as many `\n` as its `t`, and no `i` contains
`\n`. The longest note is 114 words, under the validator's cap of 130. Scansion: 101 of 101 lines fit and none
is flagged, which matches the packet's "none". **No `t`, `ln`, `p` or `mark` field was touched.**

**Findings fixed: 1 error, 0 major, 21 moderate, 34 minor.** In units.json that is 1 error, 4 moderate and
8 minor. new-renderings.md has 1 minor. In gloss.json it is 17 moderate and 25 minor, which includes 13 new
broadenings of known forms that the Glosser missed. The findings I considered and refused are listed at the end.

## Pass 1 — `units.json`

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 3.98–101 | `l`, `i`, `n` | **error** | The Drafter left Telemachus's speech open and wrote in the note that it "continues into odyssey-010". The source archive says otherwise: 3.101 ends with a full stop, and 3.102 is `τὸν δ’ ἠμείβετ’ ἔπειτα Γερήνιος ἱππότα Νέστωρ·` (¶), Nestor's reply-formula. The speech closes at 3.101. As drafted, the part would have shipped 7 opening and 6 closing quotation marks, a false note, and a false hand-off to the next part's drafter. | Added ” at the end of `l` and `i`. Note: "Telemachus's speech ends here, at 3.101; Nestor's answer begins the next part." |
| 3.18 | `n`, `l` | moderate | The note called εἴδομεν "an aorist subjunctive of the stem ἰδ-" and gave its Attic equivalent as εἰδῶμεν. These contradict each other: εἰδῶμεν is the perfect subjunctive of οἶδα (the aorist subjunctive would be ἴδωμεν), and the ει-stem is the perfect's. LSJ and Cunliffe give εἴδομεν (compare Il. 1.363) as the short-vowel subjunctive of οἶδα. | Note relabelled: subjunctive of οἶδα 'know', stem εἰδ-, short vowel (Attic εἰδῶμεν), 'let us know, let us find out'. `l` changed from "let us see" to "let us find out", which matches `i`. |
| 3.89 | `n` | moderate | The note said ὁππόθ’ "could stand for ὁππόθι 'where' or ὁππότε 'when'". It cannot be ὁππότε: elided τ is aspirated to θ only before a rough breathing, and ὄλωλεν has a smooth one. | Note: ὁππόθ’ is ὁππόθι, elided; it cannot be ὁππότε, and says why. |
| 3.5 | `n` | moderate | The note said the dative κυανοχαίτῃ "shows Ionic η for Attic long α". This is false: a masculine -της noun has dative -ῃ in Attic too, since χαίτη has τ, not ε/ι/ρ, before the ending. | Sentence removed. |
| 3.45 | `n` | moderate | The note said that in ἣ θέμις ἐστί "ἥ is a relative adverb, 'in the way that'". Murray prints ἣ, which is the relative pronoun, feminine by attraction to θέμις (Cunliffe s.v. ὅς). The adverb would be ᾗ. | Note: "ἥ is the relative pronoun, feminine by attraction to θέμις, 'which is right'". |
| 3.51 | `n` | minor | The note called ἡδέος "uncontracted", but the Attic genitive of ἡδύς is also ἡδέος. | Changed to "the same in Attic". |
| 3.65 | `n` | minor | The note glossed κρέ’ ὑπέρτερα as 'the upper meat', while `l` and `i` say "outer meat" and "outer flesh". The note did not match its own unit. | Note: "literally 'the upper meat', is the outer flesh, the meat proper". |
| 3.12 | `n` | minor | The sentence was garbled ("The line reverses one of the embarkation at 2.416"). ἐκ … νηός was described as "the preposition standing apart from its genitive", which hides the tmesis that the parallel ἀν(ά) … βαῖν’ at 2.416 shows. | Changed to "reverses the first line of the embarkation at 2.416"; "ἐκ … βαῖν’ is tmesis of ἐκβαίνω 'go out', with νηός the genitive 'out of the ship'". The 2.416 cross-reference was verified in odyssey-008.json (unit `ln` 416), and the English matches it except for "aboard" becoming "out of". |
| 3.19 | `i` | minor | `i` began with a lower-case "and entreat" after the full stop that ends 3.18. | Capitalised: "And entreat". |
| 3.22 | `l` | minor | `l` began with a lower-case "and how then" after the question mark of the previous unit, while `i` has "How". | Capitalised: "And how then". |
| 3.34–35 | `n` | minor | The augment status of ἄνωγον was left unstated in a note that labels every other past form. It is unaugmented: the augmented form is ἤνωγον (LSJ s.v. ἄνωγα). | Added "an unaugmented past form (augmented ἤνωγον)". |
| 3.81 | `n` | minor | The note said Telemachus "leaves his own name, and his father's, to the lines that follow". He names his father at 3.84 and 3.98 but never names himself in 3.79–101. | Note: "in the lines that follow he names his father, and lets that stand for his own name." |
| 3.24 | `n` | minor | The note called ἐξερέεσθαι "an epic present of ἐξέρομαι with its vowels left open". The open vowels belong to the by-form ἐξερέομαι (contracted ἐξερεῖσθαι), not to ἐξέρομαι. | Note: "the uncontracted present infinitive of ἐξερέομαι, an epic by-form of ἐξέρομαι". This also matches the corrected glossary entry. |
| new-renderings.md: δέπας ἀμφικύπελλον | row | minor | The row fixed "the fair double cup" with the adjective καλόν built into the rendering, but καλόν is not in its Greek column. | The rendering is now "double cup", with 3.63's "the fair / the fine double cup" given as an example. |

Every edited unit was checked again after the fixes. The quotation marks now balance at 7 opening and 7 closing
in both `l` and `i`.

## Pass 1: the Drafter's 5 flagged items

1. **3.29–30 θεοῖο, "footsteps of the god".** The ruling is **keep**. 3.29–30 is identical in `t` to odyssey-008's
   units at 405 and 406, and the `l`/`i` are identical to the shipped text character for character. This part's
   note, that Homer uses θεός of goddesses too, is correct. The -οιο genitive does not show gender, and it is the
   narrator who uses the word. The shipped odyssey-008 note ("grammatically masculine because she is disguised as
   Mentor") is the weaker claim. It cannot be corrected in place, so I wrote it to QUESTIONS.md.
2. **αἰδώς "shame" (3.14, 3.24) against αἰδόμενος "out of respect" (3.96).** The ruling is **keep**. These are
   different words used in different ways. At 3.14 and 3.24 the αἰδώς is the young man's shame at facing an elder.
   At 3.96 Nestor would be holding back out of regard for the son, and "shame" would give the wrong sense there
   ("out of shame soften things for me"). The note at 3.96 links all three occurrences, so the connection is not
   lost.
3. **πλαζομένου (3.95) as "some other wanderer".** The ruling is **keep**. The participle stands next to ἄλλου,
   and taking it with ἄλλου is the ordinary reading. The note states the alternative, "of him wandering".
4. **εὔχετο (3.54) with no augment label.** The ruling is **correct restraint**. An augment on εὐ- may appear as ηὐ-
   or leave εὐ- unchanged (Smyth §519), so εὔχετο can be read either way.
5. **Cross-references.** All of them were verified in the shipped files:
   - 1.94 (odyssey-001 `ln` 93, 2nd line, ἤν που ἀκούσῃ)
   - 1.95 (the same unit, 3rd line)
   - 1.135 (odyssey-002 `ln` 132, 4th line)
   - 1.150 (odyssey-002 `ln` 150)
   - 1.284, "Book 1" at 3.17 (odyssey-003 `ln` 284, "question heavenly Nestor")
   - 2.405 and 2.406 (odyssey-008)
   - 2.416 (odyssey-008)

   The new-renderings sources were also verified:
   - 1.125, 1.327 and 2.405 "Pallas Athena"
   - 2.430 "the swift black ship"
   - 1.344 κλέος εὐρύ
   - 2.71 "my father, good Odysseus" (odyssey-005 `ln` 71)
   - 1.237 "in the land of the Trojans"
   - 2.280 "to accomplish these deeds"

   Every in-part line reference (lines 4, 5, 9, 13, 14, 16, 21, 22–24, 24, 32, 34, 40, 41, 43, 46, 48, 54, 56,
   57, 62, 71, 72, 77, 78, 97, 7–8) points to the word it names.

## Repeated lines: verified character for character against the shipped files

| Line | Shipped source | Result |
|---|---|---|
| 3.21 | odyssey-003 `ln` 213 | The whole unit is identical in `t`, `l` and `i`. |
| 3.25 | odyssey-002 `ln` 178 | Identical. |
| 3.29–30 | odyssey-008 `ln` 405 and 406 | Both whole units are identical. |
| 3.67 | odyssey-002 `ln` 150 | The line's `l` and `i` wording is reused as far as the sentence allows. |
| 3.75 | odyssey-004 `ln` 388 | The line is reused. It runs on here into θαρσήσας, so the final colon becomes a comma, which is correct. |
| 3.77 (from ἵνα) | 1.135 | Reused, with "him" for "her" because the person asked is now Nestor. |
| 3.78 | 1.95 | Reused verbatim. |

The reply-formulas are matched to the right Greek. τὴν/τὸν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα (3.21, 3.75)
takes the fourth formula, "To her/him in turn prudent Telemachus spoke, face to face". τὸν δ’ αὖτε προσέειπε
(3.25) takes "Him then in turn addressed". The variant with προτέρη (3.13) is built on the προσέειπε pattern.
None of the ἠμείβετο, ἀπαμειβόμενος or named formulas occurs in this part, and none was used for the wrong Greek.

## Speech boundaries

There are 7 speeches, and each one opens with a `mark` and “ in both layers. **All 7 close within this part.**

| Lines | Speaker | Ends before |
|---|---|---|
| 3.14–20 | Athena | the 3.21 reply-formula |
| 3.22–24 | Telemachus | the 3.25 reply-formula |
| 3.26–28 | Athena | ὣς ἄρα φωνήσασ’ at 3.29 |
| 3.43–50 | Peisistratus | ὣς εἰπών at 3.51 |
| 3.55–61 | Athena's prayer | ὣς ἄρ’ ἔπειτ’ ἠρᾶτο at 3.62 |
| 3.69–74 | Nestor | the 3.75 reply-formula |
| 3.79–101 | Telemachus | Nestor's reply-formula at 3.102, which Murray marks with ¶ |

The last speech was fixed above (error): it closes, and it does not run into odyssey-010.

The seam with odyssey-008 is clean. Book 2 ends with narrative at 2.434, so no speech carries over into this
part.

## Pass 2 — `gloss.json`

The shape gate from `build_odyssey.py` was run as a dry run before and after the edits, and it passes. That covers
242 novel entries, no collisions with the shipped glossary, every form in the part covered, typographic ’
throughout, and every novel entry under 230 characters. All 9 of the Glosser's broadenings contain the shipped
entry byte for byte as a prefix followed by " · ". Each added reading was checked against its line and is a real,
distinct use: τ’ (3.22), κακὸν (3.74), καλὸν (3.63), λίσσομαι (3.98), ἥν (3.18), τίνες (3.71), κίε (3.17), ἴδον
(3.34), τι (3.72).

### Novel entries corrected

| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| εἴδομεν | moderate | Same mislabel as the note: "ὁράω … aor. subj." with Attic εἰδῶμεν. | "οἶδα — know; perf. subj. 1 pl., short-vowel (= Attic εἰδῶμεν), hortatory". |
| κυανοχαίτῃ | moderate | False "Ionic η (= Attic -ᾳ)". | Removed. |
| ὁππόθ | moderate | "ambiguous … between ’when’ (ὁππότε) and ’where’". | Lemma ὁππόθι. The entry says that ὁππόθ’ could be ὁππότε only before a rough breathing, which keeps it general to the form. |
| δήμιος | moderate | Parsed "masc. nom. sg.", but in the part it agrees with πρῆξις (fem.). | "nom. sg., two-termination (the -ος form serving for the fem. too)". |
| ἐμοῦ | moderate | Lemmatised under ἐγώ "agreeing attributively", but a personal pronoun does not agree. πατρὸς ἐμοῦ is the possessive ἐμός, the headword the shipped glossary already uses for ἐμὸς. | "ἐμός — my; masc./neut. gen. sg. · also ἐγώ, gen. sg." |
| ὑποστὰς | moderate | "aor. part. mid.", but ὑποστάς is the intransitive second-aorist active. | "aor. 2 part. act. masc. nom. sg., intr." |
| τοί | moderate | Gave only 'they' (3.5) and missed the relative 'who' at 3.73 (τοί τ’ ἀλόωνται). | Added "· also relative: ’who’", which matches the shipped τοὶ. |
| ἐξερέεσθαι | moderate | "ἐξέρομαι … uncontracted (= Attic ἐξέρεσθαι)". ἐξέρεσθαι is the aorist, not the contracted form. | "ἐξερέομαι (epic by-form of ἐξέρομαι); pres. inf., uncontracted (= ἐξερεῖσθαι)". |
| ἄνωγον | minor (Glosser flag) | The entry was not in the `lemma — meaning; parse` shape and did not label the augment. | Put in the shape used by the shipped ἄνωγα entries: "past (impf. or plpf.) 3 pl. or 1 sg., unaugmented (augmented ἤνωγον)". |
| δαίτης | minor (Glosser flag) | Headed "δαίς (by-form δαίτη)", but the form is the genitive of δαίτη, which LSJ lists as its own headword. | "δαίτη (epic by-form of δαίς); fem. gen. sg. (1st decl.; δαίς itself has gen. δαιτός)". |
| τινές | minor (Glosser flag) | Lemmatised under ὅστις. The shipped glossary puts the same situation (τινα) under τις, and a bare τινές can also be the plain indefinite. | "τις, τι; masc./fem. nom. pl. · after a relative, οἵ τινες (= οἵτινες) is the pl. of ὅστις". |
| λίμνην, νεστορίδης, ἱπποδάμοιο, ἱππότα, ἀμφιτρίτης, ἕδραι | minor | Pinned to the line with "here …", which the runbook forbids. | "here" removed from each; entries kept general. |
| κύμασιν, κώεσιν | minor | Called "epic -ασι / -εσι", but these are the ordinary third-declension datives. | "epic" removed. |
| δασσάμενοι | minor | "(δασσ- for δατ-)" confused the present stem with the aorist. | "(= Attic δασάμενοι)". |
| προτέρη | minor | "adverbial", but the word agrees with θεά. | "predicative". |
| τοὔνεκα | minor | "pointing forward to a purpose or reason clause". At 3.50 it points back. | Made general: "for this reason, therefore; adv." |
| σπλάγχνα, σπλάγχνων | minor | Headword σπλάγχνα, but LSJ's is σπλάγχνον. | Headword changed to σπλάγχνον. |
| πρώτιστα | minor | Headword πρῶτος, but LSJ's is πρώτιστος. | Headword changed. |
| ἐρέει | minor | Muddled headword "εἶπον/ἐρῶ (fut. of φημί/λέγω)". | The shipped ἐρέω pattern: "ἐρέω (epic fut. of εἶπον, = Attic ἐρῶ)". |
| ἐίσης | minor | Headword "ἐίση (fem. of ἴσος)", but LSJ's is ἴσος. | "ἴσος (epic ἐίσος, fem. ἐίση)", with the doubt kept. |
| ἑκάστοθι | minor | Headed under ἕκαστος. The shipped glossary heads -θι adverbs separately (ἄλλοθι, ἔνδοθι, τηλόθι). | Headword ἑκάστοθι. |
| τεοῖσιν | minor | Headed "σός (epic by-form τεός)". The shipped τεὸν uses the headword τεός. | "τεός (epic possessive = σός)". |

### Known forms whose shipped entry does not cover this part's use (13 broadenings added)

In each broadening the shipped entry is kept whole, followed by " · also …". Each one was checked against its
line.

**Moderate:**
- **νέον** (3.24 νέον ἄνδρα): adjective, masc. acc. sg. The shipped entry is adverbial only.
- **εὐρὺ** (3.83 κλέος εὐρύ): attributive 'wide'. The shipped entry is adverbial only.
- **νημερτέα** (3.19): neut. acc. pl. used as a noun. The shipped entry is fem. acc. sg. only.
- **πυκινοῖσιν** (3.23 μύθοισι πυκινοῖσιν): masc., 'shrewd'. The shipped entry is neut., 'close-packed'.
- **χρὴ** (3.14): acc. and gen., 'need of'. The shipped entry has acc. and inf. only.
- **οἷ** (3.53 οὕνεκα οἷ προτέρῃ): the orthotone pronoun 'to her'. The shipped entry has only the elided οἷα.
- **τινα** (3.16 ὅν τινα, 3.18 ἥν τινα): masc./fem. acc. sg. The shipped entry says "neut. acc. sg.", which is a
  mislabel of its own and is written to QUESTIONS.md.
- **ἰθὺς** (3.10): adverb with no case. The shipped entry has the preposition with the genitive only.
- **βαῖν** (3.12): tmesis with ἐκ. The shipped entry names only ἀνέβαινε.

**Minor:**
- **μέν** (3.14 οὐ μέν): asseverative.
- **ἐκ** (3.11 ἐκ δ’ ἔβαν): adverb or preverb with no case.
- **ἵνα** (3.77): with the optative after a past tense.
- **τὰ** (3.92 τὰ σὰ γούναθ’): with a noun.

### The Glosser's 5 flagged items

1. **τι broadening** (3.72 ἤ τι κατὰ πρῆξιν): **keep**. The τι is neuter, so it cannot agree with πρῆξιν, and it
   is adverbial without a negative. That is a use the shipped entry does not have.
2. **τινές under ὅστις**: **relemmatised** under τις, as described above.
3. **ἄνωγον entry shape**: **fixed**, as described above.
4. **δαίτη / δαίς**: **headword changed to δαίτη**, as described above.
5. **The merged-sense οὕνεκα entry**: **keep**. Both senses occur in this part: 'because' at 3.53 and 'for the
   sake of which' at 3.61. A genuine double use joined in one entry is the house practice.

## Considered and refused

- **3.97 `i` "tell me plainly" for εὖ κατάλεξον.** "Plainly" carries the force εὖ has right after the ban on
  softening the truth, and `l` keeps the literal "well". The new-renderings row stays as proposed.
- **3.44 `i` leaves out καί ("too").** Here καί only adds light emphasis, and the cleft sentence in `i` carries it.
  `l` keeps "too".
- **3.83 `i` "I have come after" for the present μετέρχομαι.** This is idiomatic English for "I am in pursuit
  of", and the sense does not drift.
- **3.52 `i` "the prudent and just young man" for ἀνδρί.** Peisistratus's youth is established at 3.49
  (ὁμηλικίη), so "young" does not change the sense.
- **ἀέκητι (3.28) "against the will of" against 1.79's "in despite of".** This is not a house formula, and the
  construction and context differ.
- **δαίμων "a divinity" (3.27) against 2.134's "a god".** Not a house formula. The note at 3.27 depends on the
  word staying vague.
- **ἤν που ἀκούσω (3.83) against 2.360's English.** This is a half-line inside a different sentence. It is not a
  repeated whole line, and the packet does not list it.
- **Four broadenings over 230 characters in total** (κακὸν 329, καλὸν 334, λίσσομαι 344, τι 276). The shipped
  entries were already 188–227 characters, and the additions-only rule forbids shortening them. The build caps
  only novel entries. There is shipped precedent: ἂν is 379 characters, ὅ 332, ὄφρα 294 and ἦ 292. This is the
  same tension already recorded in QUESTIONS.md.
- **The shipped θεοῖο glossary entry, "masc. gen. sg."** A broadening cannot fix this cleanly, because the reading
  concerns the same line. It is written to QUESTIONS.md together with odyssey-008's note.
- **Ionic headwords πρῆξις and ὁμηλικίη, rather than LSJ's Attic πρᾶξις and ὁμηλικία.** These are kept for
  consistency with the shipped glossary's πρήσσω and ὁμηλικίη.
- **The shipped αὐτός/αὐτὸς entries give "he himself", but this part uses the words for "you yourself" (3.19,
  3.26).** The headword "self" covers every person, and the shipped αὐτή entry already shows the extension to
  other persons.
- **ἔτι "besides" at 3.60.** The shipped "still, yet" covers it closely enough.

## Open items written to QUESTIONS.md

- The note shipped at 2.406 in odyssey-008 says θεοῖο is "grammatically masculine because she is disguised",
  which contradicts this part's more accurate note on the same repeated line.
- The shipped glossary entry for τινα is mislabelled "neut. acc. sg.".
