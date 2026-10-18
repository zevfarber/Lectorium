# iliad-018 (3.171–263) — review, two passes

`t` was never touched (a script asserted every `t` unchanged before writing; the 53 units, their order, `ln`, `v`, `p` and `mark` are as drafted). `units.json` was edited in place by script. `gloss.json` does not exist yet for this part, so no parse could be checked against it; the glosser's output still needs the second-pass read. No modern translation was opened or recalled. Cross-checks were made against `conventions.md`, `../odyssey/conventions.md`, the packet, iliad-016 and iliad-017 `units.json`, and the shipped `odyssey-*.json` parts.

Severity: major = a wrong fact or wrong translation that would ship; moderate = a false statement in a note, or a departure from a house rendering; minor = an imprecision or an unsupported aside.

## Pass one — notes, labels, positions, cross-references, scansion, quotation marks

Every label in every note was checked against the form in its line; every "as at N" / "see N" / "line N is line M" was checked against the line named.

### Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 172 | n | moderate | The scansion sentence called the line irregular partly because it "has only fifteen syllables" (15 is ordinary for a hexameter with three spondees) and because "the short ος of αἰδοῖός is counted long at the start of the second foot" (it is long by position before τέ, with no licence involved). Hand scan: αἰ-δοῖ / ός-τε-μοι / ἐσ-σι-φι / λε-ἑ-κυ / ρε-δει / νός-τε = 15 syllables; μοί short by correption (regular); λε of φίλε long in the fourth foot (the scanner's lengthening); ρε of ἑκυρέ long before δεινός (δϝ-), giving a spondaic fifth foot. The scanner flag is therefore real, but only for those two lengthenings. | Rewrote the sentence to name only the two real irregularities and the resulting spondee in the fifth foot; dropped "only fifteen syllables" and the ος clause. |
| 173 | n | moderate | "λιποῦσα … with three objects" lists θάλαμον, γνωτούς, παῖδα, but the participle has four (ὁμηλικίην is the fourth, in line 175). | "four objects", with ὁμηλικίην added and pointed to the explanation later in the note. |
| 180 | n | minor | "she doubts that her old life was real" states as fact an interpretation the words (εἴ ποτ’ ἔην γε, "if ever that was so") do not fix. | "she speaks as if the old tie were something long gone." |
| 182 | n | minor | δεδμήατο was called a pluperfect with the gloss "had been subdued", while `l` says "were subdued" and `i` "were made subject": the note contradicted its own `l` as it stood. | Note now says the form is literally "had been subdued" but that the pluperfect states a past condition, so "were subdued". `l`/`i` unchanged. |
| 205 | n | minor | ἀγγελίη glossed "message, embassy" without saying that the house English elsewhere is "news" (Odyssey table 15.314; Iliad table 2.787); the departure to "embassy" was unexplained, though new-renderings.md said "the note says so". | Note says it is "news" elsewhere and that here the word names the errand itself. new-renderings.md row adjusted to match. |
| 212 | n | minor | "a picture of speech-making as weaving that the Odyssey also uses": the Odyssey table has the image only for plans and tricks (δόλον ὑφαίνειν 5.356, μῆτιν ὑφαίνω 13.303), not for speech. | Reworded to say exactly that. |
| 212 | n | minor | "ἐπιτροχάδην … is shipped in the Iliad table": the shipped row is the Odyssey table's (18.26); the Iliad table has none. | "shipped in the Odyssey table (18.26)"; new-renderings.md row corrected the same way. |
| 239 | n | moderate | "ἅ μοί ἐστιν ‘which are mine’ says that the shame of Helen’s name is on her brothers too": the form says the reproaches are Helen's (μοί), not that anything is "on her brothers"; the note misdescribed its own gloss. | "says that the reproaches are Helen’s own, which her brothers dread to share." |
| 261 | n | minor | "κατὰ … τεῖνεν is likewise κατέτεινεν": the line has the unaugmented form, so the note named a form that is not in the line. | "is likewise the imperfect of κατατείνω ‘draw tight’, without the augment." |
| 263 | n | minor | "ἔχον … said of the horses’ course": the horses are the object of ἔχον, not its subject or a course. | "ἔχω ‘hold, keep’, with ἵππους as its object, ‘held the horses on their way’, so ‘drove’." |

### Checked and found true (no change)

- Positional claims and cross-references, all verified: 164–165 (kindness, iliad-017 unit at 164), 166–167 (the question, 017), 162 (φίλον τέκος), 168 (γεραρόν), 167 (ἠΰς … μέγας), 166 (πελώριον), 181 (ὁ γέρων; ἀγάομαι) and 224, 190 (ἑλίκωπες), 191 (ὁ γεραιός), 200, 202/208 (μήδεα πυκνά), 232–233, 171 (reply formula), 4.305 (τανύπεπλος), 4.184 (Διὸς ἐκγεγαυῖα), 1.8 (τίς τ’ ἄρ), 1.16 (κοσμήτορε), 1.284 (ἕρκος), 11.300 (the repeated Castor line), 127 (= 251), 136 (= 253), 72 (κτήμαθ’ in the second line of the iliad-016 unit at 71), 73–75 and 74 (νεέσθων), 3.145 (Σκαιαί).
- "τόν is Priam" at 171: the last unit of iliad-017 (170, "…ἔοικε.”") closes Priam's speech, so 171 correctly opens with no quotation mark and no `mark`.
- Grammar labels checked form by form and found correct: ὄφελεν aor., ἁδεῖν aor. inf., ἑπόμην impf., λιποῦσα aor. part., τέτηκα pf. (intransitive), μεταλλᾷς contracted pres., ἐσσί, ἑκυρέ and φίλε vocatives, ἔσκε iterative, ἔην, ἠγάσσατο aor., φώνησέν accent from τε, δεδμήατο 3pl plpf. pass., εἰσήλυθον, ἐστρατόωντο, ἐλέχθην ("count"), ἐρέειν’ = ἐρέεινε, ἐΐσκω, τράφη, ἔειπες, ἤλυθε, ἐξείνισσα, ἐδάην, ἔμιχθεν, ἀγρομένοισιν, στάντων, ἑζομένω (dual), ὑπείρεχεν, ἀναΐξειεν (aor. opt.), στάσκεν/ἴδεσκε/ἔχεσκεν, πήξας, ἐνώμα, ἀστεμφές (neuter adverb), εἵη (aor. opt. of ἵημι), ὄπα (acc. of ὄψ), ἐρίσσειε, ἀγασσάμεθ’, ἕστηκ’, ἠγερέθονται, ξείνισσεν (unaugmented), ἵκοιτο, μυθησαίμην, γνοίην, ἑσπέσθην (dual), ἕποντο, καταδύμεναι, δειδιότες, κάτεχεν, πατρίδι (adj.), ἄρνε (dual), ὄτρυνεν and φέρε (unaugmented), ὄρσεο, τάμητε (aor. subj., 2pl), μαχήσοντ’, ἕποιτο, ναίοιμεν (1pl opt.), νέονται, ῥίγησεν, ζευγνύμεναι, ἐπίθοντο, ἂν … ἔβη (tmesis), βήσετο, Σκαιῶν, πεδίον δ’.
- Scansion flag, line 172: scanned by hand (see the table); the unit's note now carries one plain sentence saying the line is irregular as transmitted and where. No other line was flagged.
- Quotation marks and `mark`/`p` (checked in a script and by eye): eight speeches (Helen 172–180; Priam 182–190; Priam 192–198; Helen 200–202; Antenor 204–224; Priam 226–227; Helen 229–242; Idaeus 250–258). Each opens with “ on its first unit (which carries `mark`) and closes with ” on its last, in both `l` and `i`; no unit inside a speech carries a mark; no straight quotes; all counts balanced. The ten ¶ paragraphs of the packet (171, 181, 191, 199, 203, 225, 228, 243, 245, 259) are exactly the ten units with `p`. `l` and `t` have the same number of lines in every unit; `i` has no line breaks.

## Pass two — Greek → `l` word by word, `l` ↔ `i`, remembered English, repeated lines

### Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 220 | l, i, n | moderate | ἄφρονα was rendered "foolish" in `l` and "a fool" in `i`. The Odyssey table fixes ἄφρων as "senseless" in both layers (17.586) and reserves "foolish" and "fool" for νήπιος, "witless" for ἀνοήμων; odyssey-103 ships "senseless". The drafter cited odyssey-028 and -100 ("foolish"), but those predate the table row, which governs. | `l` "simply senseless", `i` "simply senseless", note "ἄφρονα ‘senseless’ (without φρένες ‘wits’; the table’s ἄφρων)". new-renderings.md row rewritten, recording that the earlier "foolish" is not followed. |
| 241 | l, n | moderate | μάχην was "the battle of men" in `l`. The Iliad table renders μάχη "fighting" in both layers (2.823, 3.84–85) and lists "battle" among the avoided words. `i` already had "fighting". | `l` "to enter the fighting of men"; note's gloss changed to "the fighting of men"; new-renderings.md row corrected. |
| 241 | i | minor | `l` has "but now again are unwilling", `i` had "and now will not enter": "will not" is a refusal of will, "are unwilling" is the Greek (οὐκ ἐθέλουσι, present), and αὖτε was lost. | `i` "and now again are unwilling to enter the fighting of men". |

### Repeated lines (checked word for word against the packet)

- 3.177: `l` and `i` use the published Odyssey words; only the final stop became a colon, and the note says why. Kept.
- 3.237: `l` and `i` identical to odyssey-053's wording for the line. Kept.
- 3.251: `l` "of the horse-taming Trojans and the bronze-shirted Achaeans" identical to iliad-017; `i` is the published wording with "of" repeated before "the bronze-shirted" so the sentence reads, as new-renderings.md says. The table's row for 3.127 = 3.131 agrees. Kept.
- 3.253: `l` and `i` as iliad-017 up to the verb; the second line differs in its Greek (γυναικί for σεῖο), so "a woman" is correct. Kept.
- 3.256 and 3.258: the Greek differs from iliad-016 (ναίοιμεν for ναίοιτε; νέονται for νεέσθων), so the validator's identity rule does not apply; the wording is reused with "we" for "you" and "are going back" for "let them go back", and the third line is word for word the published one. The note states both changes. Kept.

### Considered and refused

- 172 `l` "Revered to me you are": τέ … τε ("both … and") is not shown; the table's own αἰδοῖός τε φίλος τε rows drop it the same way. Refused.
- 172 note, "δεινός ‘dread’, one who inspires awe": consistent with the Iliad table (1.200, "dread"). Refused.
- 173 `i` "on the day I followed": ὁππότε is "when"; "on the day" is within the sense (the single occasion of the departure). Refused.
- 175 ὁμηλικίη rendered "the company of my own age", where the Odyssey ships "of an age with" for the adjective ὁμήλιξ/ὁμηλικίη (odyssey-012, -027, -108) and "contemporaries" (-006): the noun here is collective and the drafter's new-renderings entry is argued. Refused.
- 175 τηλύγετος "late-born": confirmed shipped at odyssey-014 and -077, and the note says the origin is unknown. Refused.
- 177 colon in place of the stop: argued in the note. Refused.
- 180 `l` "my own": ἐμός is "my", "my own" is fair for the position after the verb. Refused.
- 184 `i` lacks "already" for ἤδη; 188 `i` lacks "too" for καί; 215 `i` lacks "indeed" for ἦ; 234 lacks μέν: particles whose force is carried by the sentence. `l` has them. Refused.
- 223 `l` "would … rival", `i` "could … rival": the potential optative with ἄν is both; the note says "would". Refused.
- 238 `l` "bore to me" against note and `i` "for me": a literal layer against a smooth one. Refused.
- 247 θεῶν not glossed in the note ("the faithful oaths of the gods"): the English follows the Greek; the note explains what the phrase names. Refused.
- 256 νέονται: the note calls it the present; it may also be read as a short-vowel subjunctive, but "present" is true of the form and both layers read it as a present with future force. Refused.
- 205 ἀγγελίη kept as "embassy" (not forced back to "news"): the sense is the mission; the note now says why it departs. Refused as a change of rendering.
- 218–219 ἀΐδρεϊ φωτί "a man who knew nothing": slightly strong for ἄϊδρις ("without knowledge"; cf. "no knowledge of the place", odyssey-048), but the note says "without knowledge" and the new-renderings entry is argued. Refused.
- 201 δήμῳ "land": follows the Odyssey table; the note says "land, district". Refused.
- `about`: "Priam calls him fortunate" paraphrases μάκαρ/ὀλβιόδαιμον and is not a rendering. Refused.
- Remembered English in `i`: every phrase was rebuilt from the grammar and the table ("heavenly among women", "tamer of horses", "bulwark", "words like wintry snowflakes", "ranges along the ranks of men", "waste away in tears", "stood out above the Argives in head and broad shoulders", "is numbered among them", "heart-cheering wine"); none arrives as a stock translation phrase. Nothing changed on this ground.
- `v`, `p`, `ln`, `mark` values: unchanged and correct.

## Counts

| | major | moderate | minor |
|---|---|---|---|
| Pass one (notes etc.) | 0 | 3 | 7 |
| Pass two (Greek, `l`, `i`) | 0 | 2 | 1 |
| Total | 0 | 5 | 8 |

(Findings, not fields: the 220 and 241 changes each touch several fields. `new-renderings.md` was updated for 205, 212 (Odyssey table), 220 and 241.)

## Glossary pass

Checked all 208 novel entries and the 10 `__broaden__` entries against the lines they occur in. Six entries changed (script, in both `gloss.json` and the root `iliad-glossary.json`):

- ἐρατεινῆς · claimed "Ionic -ῆς (= Attic -ᾶς)"; the alpha-purum rule does not apply after ν, so the Attic form is the same · now "Attic form identical".
- κραναῆς · same false equivalence (-ᾶς) · now "Attic form identical".
- ἔνι · "= ἐν νηυσί" is the Ionic/epic form, not the Attic equivalent · now "= Attic ἐν ναυσί".
- ὀδυσῆΐ · "= Ὀδυσσῆϊ" is not Attic · now "(= Attic Ὀδυσσεῖ)".
- ὀλβιόδαιμον · lemma misaccented (ὀλβιόδαίμων) · now ὀλβιοδαίμων.
- εἵη · called "epic", but εἵη is the ordinary aor. opt. 3 sg. of ἵημι in Attic too · now "the Attic form too".

Broadened entries (οὕς, σῷ, τοῦτο, τώ, τὸ, ἀγαθὸν, ἐρέειν, ὑπαὶ, ὡς, νημερτὲς): old entry intact in each, joined by ' · ', and each new reading is true of the form in its line. No change.

Refusals:
- ὑπαὶ "(his brows)" is a supplied gloss, not in the Greek; kept as the standard understanding of "from under", the reading itself is true.
- εὐρέας/ἀγρομένοισιν/ἐδάην etc.: parses and Attic equivalents are correct. No change.
- No ASCII apostrophes, line numbers, "here", or entries of 230+ characters found; article-forms are labelled pronouns.
