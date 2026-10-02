# Review of odyssey-057 (Odyssey 12.1–100)

Two passes over `units.json` (pass 1: grammatical labels, word-position claims, cross-references, notes against `l`/`i`; Greek → `l` word by word; `l` ↔ `i`; remembered English; quotation marks. Pass 2: the whole file again including every pass-1 edit, plus the gate rules the validator applies), then `gloss.json` read (not edited) and checked against the lines. `t` was not touched (checked against a copy taken before the first edit: all 49 units' `t` identical). `units.json` was edited in place by script; every edit asserted its old text occurred exactly once; the file keeps its original JSON layout. `new-renderings.md` was read against the units and needs no change. Conventions, runbook section 2, packet, and `new-renderings.md` read in full; no modern translation opened or recalled.

Severity (as in the 056 review): **high** = the English or a note says something false about the Greek or changes its sense; **medium** = wrong cross-reference, house-rule departure, gate failure, note contradicting `l`/`i`, or a muddled statement that would mislead; **low** = polish, over-statement, consistency, note length.

Totals: 32 edits to `units.json` (high 2, medium 12, low 18); 0 edits to `gloss.json` (not touched; 4 findings handed back below).

Scansion: the packet flags none, so no line was scanned by hand and no note gained a metre sentence.

Quotation marks: the last unit of `odyssey-056.json` (line 639) is narration; Heracles' single-marked speech closed at 626, and its note says Odysseus' tale (double mark, reopened at 11.378) is still open. So 057 correctly opens no `“` and closes no `”` (validator count 0/0 in both layers). Circe's first speech (12.21–27) opens `‘` on its first unit (`mark: Circe speaks`) and closes `’` on the last (line 25 unit), balanced in both layers. Her second speech opens `‘` at 12.37 (`mark: Circe speaks again`) and runs on past 12.100 (the last unit's note says so), so one single mark is deliberately left open: LOG.md should say that Circe's speech continues into odyssey-058. `p` is on exactly the seven ¶ lines (1, 8, 16, 21, 28, 37, 73).

## Changes to units.json

Line = the unit's `ln`; unit = index in `sentences` (0-based).

| Line | Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 0 | n | low | Note 147 words (validator warns above 130); a repeated first-person-plural remark and the εὐρυπόροιο gloss (the epithet is in the table) were surplus. | “the verbs from line 5 are first person plural, and … This unit is a clause of time with no main verb yet; the main clause begins in line 5.” → “; the ship has just crossed the river Oceanus. This is a clause of time, and the main verb comes in line 5.”; “εὐρυπόροιο is ‘wide-wayed’, said of the sea.” removed (125 words). |
| 5 | 1 | l, i | medium | Gate failure: the Greek of lines 5–6 is the whole of a published unit (odyssey-044, line 546), so `l` and `i` must equal the published English exactly, and the draft ended both with `;` where the published ones end with `.`. | Both layers set to the published text (`…surf-line of the sea.` / `…where the sea breaks.`). |
| 8 | 3 | n | low | Over-statement about the rest of the poem: “the man left unburied at Circe’s house” (this part shows only that the body is fetched from there). | “the burial of the man left unburied at Circe’s house.” → “the burial of the dead man Elpenor.” (the last sentence of the note already says where the body is). |
| 13 | 5 | l | medium | House departure: τεύχεα is “armour” in the table (βεβροτωμένα τεύχεα), and the note and `i` already say armour; `l` had “arms”. | “the arms of the dead man” → “the armour of the dead man”. |
| 18 | 8 | l | medium | Misleading parse: “together with her attendants were carrying” reads as “with her-attendants”; the Greek is ἅμα … αὐτῇ “together with her”, ἀμφίπολοι the subject. | → “and together with her, attendants were carrying”. |
| 18 | 8 | i | low | Clumsy doubling: “red wine, the wine that has the look of fire”. | → “food, plenty of meat, and the red wine that has the look of fire.” |
| 31 | 16 | l | medium | House departure: ἕκαστα is “each thing” in `l` throughout (new-renderings.md; already so at 12.16 and 12.25); `l` had “everything”. | “asked about everything;” → “asked about each thing;” (`i` keeps “everything”, which the row allows). |
| 31 | 16 | n | low | Note 148 words; glossed ἕκαστα as “every detail” against `l`; said the first line “is repeated in part”. | Dropped the κατέδυ/κνέφας sentence (the repeated line), “that hold a beached ship”, and “its English follows the earlier rendering”; ἕκαστα → “each thing”; “repeated in part” → “repeated” (121 words). |
| 31 | 16 | n | medium | Overstated: “the Greek says only that she lay down by him” fixes a sense of προσέλεκτο that is not certain (the form can also be read as ‘conversed with’; the glosser's entry even leads with that). | “…in the sense ‘lay down’, with πρός ‘beside’: the Greek says only that she lay down by him.” → “…is taken here as the aorist middle of λέγω ‘lay down’, with πρός ‘beside’; some read it as ‘conversed with’, so the sense is not certain.” `l`/`i` unchanged. |
| 37 | 19 | mark | low | Off-idiom: the house says “X speaks again” for a speaker's later speech (Athena, Nestor, Odysseus … speaks again). | “Circe continues” → “Circe speaks again”. |
| 41 | 21 | l | medium | Misparse: “to him no wife and infant children / having returned home stand beside him” hangs “having returned home” on the wife and children; νοστήσαντι agrees with τῷ, ‘him’. | “having returned home stand beside him, nor do they rejoice,” → “stand beside him, returned home, nor do they rejoice,”. |
| 47 | 23 | n | low | “τῶν ἄλλων is ‘of the others’” leaves the partitive unexplained, and the `l` line-break puts “hear / of the others”, which reads ‘hear about’. | Note now says τῶν ἄλλων is a partitive genitive with τις, ‘any of the others’, which the line-break separates from it. `l` kept (order of the Greek). |
| 49 | 24 | n | high | False label: ἀνήφθω called the “aorist passive imperative” of ἀνάπτω. An imperative takes no augment, so the η is reduplication: it is the perfect passive imperative (an aorist passive would be ἀναφθήτω). | “aorist passive imperative” → “perfect passive imperative”. |
| 49 | 24 | n | low | Note 148 words; two small glosses (αὐτός ‘you yourself’, σ’ is σε) and a purpose-clause label were surplus. | Dropped “How Odysseus may listen.”, “αὐτός is ‘you yourself’, set against the companions.”, “σ’ is σε,”, “with the aorist subjunctive”; “in which the mast stands” → “for the mast” (126 words). |
| 53 | 25 | l | low | One word rendered twice: “still more, in more bonds” (ἔτι πλεόνεσσι is one phrase). | → “let them then bind you in still more bonds.” |
| 53 | 25 | i | medium | `l` ↔ `i`: “to set you free and order them to loose you” renders the single infinitive λῦσαι twice and adds an action `l` does not have. | → “if you beg your companions, and order them to set you free, then let them bind you with still more bonds.” |
| 53 | 25 | n | medium | False label: διδέντων called a form of “διδέω”. The ending -ντων is added straight to the stem διδε-, an athematic imperative (like τιθέντων); the verb is δίδημι, a reduplicated by-form of δέω. (The glosser's entry already says δίδημι.) | “the third plural imperative of διδέω, a form of δέω ‘bind’” → “…of δίδημι, an athematic by-form of δέω ‘bind’”. |
| 59 | 28 | i | low | Lost the explanatory γάρ of ἔνθεν μὲν γάρ, which `l` and the note keep. | “On the one side are overhanging rocks” → “For on the one side are overhanging rocks”. |
| 65 | 31 | n | medium | False word-position claim: “named as ‘father Zeus’ in the line before”; Διὶ πατρί stands in line 63, two lines earlier (line 64 is the smooth-rock line). | → “named as ‘father Zeus’ at line 63”. |
| 66 | 32 | n | low | Note said τῇ is ‘there’ while `l` has “from there”. | → “τῇ here is ‘there’, so ‘has escaped from there’.” |
| 66 | 32 | n | low | νεῶν called “the Ionic genitive plural”; the form is also the Attic one (only νηός, the singular, differs). | → “νεῶν is the genitive plural of ναῦς (the form is the same in Attic)”. |
| 69 | 33 | l | medium | Greek → `l`: κείνη (‘that one’, which the note glosses) and δή were dropped, οἴη ‘alone’ became “Only one … ship”, and an aorist became a perfect with an added “there”. | “Only one sea-crossing ship has passed by there, / Argo” → “Alone indeed that one sailed past, the sea-crossing ship, / Argo” (Greek order). |
| 69 | 33 | i | low | Same loss of ‘that one’. | “Only one sea-crossing ship” → “Only that one sea-crossing ship”. |
| 73 | 35 | l | medium | “a cloud around it has set / dark” — ‘set’ is read as sunset; ἀμφιβέβηκε is a perfect, ‘has gone round and stands’ (note: ‘stands around, wraps’). | → “a cloud around it has come to stand / dark;”. |
| 79 | 38 | n | low | Note glossed ‘like a rock polished all round’ against `l` “like to one polished” and `i` “like something polished”. | → “‘like something polished all round’, the feminine περιξεστῇ agreeing with an understood πέτρῃ.” |
| 80 | 39 | l | medium | “in the middle crag” suggests a third crag; μέσσῳ ἐν σκοπέλῳ is ‘in the middle of the crag’ (as `i` and the note have it). | → “And in the middle of the crag is a misty-looking cave,”. |
| 89 | 44 | l | low | The dative οἱ of ἓξ δέ τέ οἱ δειραί (‘to her’) was left unrendered. | “and six necks very long” → “and to her six necks, very long”. |
| 95 | 46 | l | low | ἃ μυρία rendered “such as countless”; ἅ is the relative ‘which’ and the note says ‘which, countless’. | “a sea-beast, such as countless loud-groaning Amphitrite feeds.” → “a sea-beast, which, countless, loud-groaning Amphitrite feeds.” |
| 95 | 46 | i | low | βόσκει is ‘feeds’ (`l` and note); `i` had “rears”. | “that loud-groaning Amphitrite rears.” → “…feeds.” |
| 95 | 46 | n | low | Glossed μεῖζον as a separate ‘something bigger’; it agrees with κῆτος across the line-end (as `i` has it). | “‘and if anywhere she catches something bigger, a sea-monster’” → “‘and if anywhere she catches a bigger sea-monster’, with μεῖζον agreeing with κῆτος across the line-end, and”. `l` kept: “something bigger / a sea-beast” is its line-break bridge. |
| 98 | 47 | n | high | False label: εὐχετόωνται called “the uncontracted form of εὔχωνται, from εὔχομαι”. εὔχωνται would be the subjunctive of εὔχομαι; this is the indicative third plural of εὐχετάομαι with epic diectasis (Attic εὐχετῶνται). | → “the third plural of εὐχετάομαι, a lengthened form of εὔχομαι ‘declare’, with the vowels left uncontracted (Attic εὐχετῶνται)”. |
| 21 | 10 | n | low | Note 135 words; the ‘hard, reckless, past bearing’ list duplicated the new-renderings row. | → “kept as ‘cruel’ by house rule, though here it is an exclamation of dismay at what they have done, as the clause that follows shows.” (128 words). |

Not an edit, but checked and true: every repeat is intact (12.7, 12.28, 12.29–30 whole units equal the published ones; 12.5–6 after the fix above; the single lines 12.8, 12.23, 12.31 keep the published English as far as the sentence allows); `l` has the same number of lines as `t` in all 49 units; `i` has no newline; no ASCII quote or backtick in any note; `t` untouched.

## Findings considered and refused

| Line | Unit | Finding | Why refused |
|---|---|---|---|
| 1 | 0 | `i` “swell” for κῦμα beside `l` “wave”. | Same sense; “the swell of the sea” is the English idiom for κῦμα θαλάσσης, and `i` is not bound to the `l` word. The house “wave” is kept in `l` and at 12.60 in `i`. |
| 1 | 0 | Note says the main verb comes in line 5. | Checked: ἐκέλσαμεν, line 5. True. |
| 8 | 3 | προΐειν “epic for προΐην”. | Checked: first singular imperfect of προΐημι (ἵειν); the label is true. |
| 11 | 6, 13 | ‘sent’ / ‘carry’ in `l` vs “fetch” in `i`. | οἴσω is ‘bring, carry’; `i` may vary. |
| 13 | 4, 5 | ἀκροτάτη “farthest out” (headland) beside ἀκροτάτῳ “topmost” (mound). | One word, but spatial superlative of ἄκρος; the headland is ‘outermost’ and the mound ‘uppermost’, and the note says so for both. Not a stock epithet. |
| 16 | 7 | “her preparations made” for ἐντυναμένη. | The middle voice supports ‘her own’; the note keeps open whose and what. |
| 21 | 10 | `l` “once only” for ἅπαξ (‘only’ added). | ἅπαξ is ‘once (and no more)’ against δισθανέες; no change of sense. |
| 24 | 13 | `i` “some grievous bad planning” (‘some’ for τι). | τι with ἵνα μή is ‘at all’; `l` has “not at all”; `i` “some” softens, does not alter. |
| 28 | 14 | θυμὸς ἀγήνωρ “lordly heart” / “proud hearts”. | Published wording of a repeated unit; fixed by rule. |
| 32 | 21 | `i` “Whoever draws near … no wife … stand beside him” (anacoluthon). | The Greek has the same construction (relative clause, then τῷ … resumptive). |
| 41 | 21 | Cut of a long sentence at a comma. | The sentence runs lines 41–46, six lines, over the four-line limit. Allowed. |
| 47 | 22 | Object ‘him’ of θέλγουσιν supplied in `l`/`i`. | Understood in the Greek; note says so. |
| 53 | 24 | “Wandering Rocks” could be remembered English. | Rebuilt: Πλαγκταί is ‘the wandering (rocks)’ (πλάζω); it is the literal name; new-renderings.md gives the reasons. |
| 58 | 27 | `l` “and” vs `i` “but” for δέ. | Particle can be either; the sentence before ends on the contrast. |
| 62 | 30 | οὐδὲ … οὐδέ as “not even … nor”. | Checked against `l` and `i`; consistent. |
| 66 | 32 | `l` “whichever has come” for aorist subjunctive ἵκηται. | Perfect for the general aorist subjunctive is acceptable; `i` “that has come”. |
| 71 | 34 | `l` “And even her” for καὶ νύ κε … τήν; “would it have thrown” with a supplied subject. | The note says no subject is stated and why `i` turns it passive; καί is ‘even/indeed’. |
| 73 | 35 | Note: “only the first is described in this part”. | ὁ μέν marks the first crag, and no second crag is described before line 100. True of this part. |
| 75 | 36 | Note's reading of neuter τὸ μέν. | Plausible and flagged as ‘the cloud-covering as a whole’; the form is neuter, the note does not overclaim. |
| 85 | 41 | `l` “yelling” vs `i` “shrieking” vs note “cry out, shriek” for λελακυῖα. | Near-synonyms for a word of sound; no conflict of sense. |
| 86 | 42 | `l` “is as great as a newborn puppy’s / becomes” reads stiffly. | It is the literal parse (ὅση … γίγνεται); the note gives ‘is, comes to be’. |
| 87 | 43 | `l` “at the sight of her” for ἰδών. | Participle recast as a noun phrase, same sense; keeps the line-break. |
| 95 | 46 | `l` “something bigger / a sea-beast” (see the n edit above). | Kept as the line-break bridge. |
| 98 | 47 | `i` “have yet declared” for the present εὐχετόωνται; `uninjured` moved to the escape. | Same sense; new-renderings.md allows “declared / declare”. |
| 99 | 48 | `l`/`i` “for” for δέ τε. | Explanatory δέ; the note says so; the sentence explains why no sailor claims to have passed. |
| 83 | 40 | `i` “Not even a vigorous man” for οὐδέ. | Within the range of οὐδέ, supported by αἰζήιος; not a change of force. |
| — | — | Notes 1 (115) and 13 (111) are over the 110-word guide. | Inside the validator's band (it warns above 130); both carry only needed labels. |
| 1–100 | all | Remembered English in `i`: scanned each `i` (“close-packed and crowded”, “keep the number complete”, “men who die twice”, “of concern to all”). | Each phrase is rebuilt from the case relations or is the drafter's logged choice; none is a set English phrase for the Greek. |

## gloss.json (read-only; handed back, not edited)

`gloss.json` was being written concurrently, so it was only read. Mechanical checks passed: all 148 novel forms present, no missing coverage, no key already in the glossary, every entry under 230 characters with typographic ’ only, every `__broaden__` entry starts with the old entry. Each parse was then checked against its line. Findings for the glosser or the person publishing:

1. **προσέλεκτο** (medium): the entry leads with “converse with (some take it ‘lay beside’)”, but the unit reads ‘lay down beside’ and now says ‘some read it as conversed with’. Reverse the order to match: lead with ‘lay down’ (λέγω, aor. mid.), add ‘some read it as “converse with”’.
2. **νεογιλῆς** (low-medium): lemma given as νεογιλής with “gen. sg.”; the printed -ῆς is the first-declension feminine genitive agreeing with σκύλακος, so the lemma should be νεογιλός, ή, όν, fem. gen. sg.
3. **θάπτομεν** (low): “pres. 1 pl. (or unaugmented impf.)” — the unit note says imperfect (it narrates a past funeral); the hedge could be dropped.
4. **ἀλγήσετε** (low): “fut. 2 pl. (or short-vowel aor. subj.)” — after ἵνα μή the unit note takes it as the short-vowel subjunctive; the hedge could be dropped. (**διδέντων** is lemma δίδημι, which now agrees with the corrected note.)
