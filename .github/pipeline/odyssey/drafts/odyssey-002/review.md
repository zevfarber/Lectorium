# odyssey-002 (1.96–212) — reviewer's report

Two passes, in the order the runbook sets them out. Pass 1 checked every grammatical label,
every claim about where a word stands, every cross-reference (all references into odyssey-001 were
checked against that part's `units.json`, not from memory), the `t` stream against the packet, `ln`
and `p`. Pass 2 checked Greek → `l` → `i`, speech boundaries re-derived from the verbs of speaking,
the house renderings and the new renderings, the repeated line 169 = 206, the honesty of the
"unknown meaning" notes, and a hand check of several lines for metre.

## Mechanical checks that passed

- **`t` reproduces the packet exactly.** The 64 units' `t`, joined in order (mid-line joins with a
  space, `\n` at each verse end), rebuilds all 117 packet lines character for character. No ASCII
  apostrophe and no U+02BC anywhere in `t`; elision marks are all U+2019. NFC-identical.
- **`ln`** is correct on all 64 units (each equals the line the unit starts on) and non-decreasing.
- **`p: true`** stands on exactly the units beginning 96, 113, 123, 125, 144, 156, 178 — Murray's
  seven paragraphs, no more and no fewer.
- **`l` line division** matches `t` on every unit (same number of `\n`); no `\n` in any `i`.
- **Nothing was open coming in.** odyssey-001's last unit (1.93–95) closes its `l` and `i` with `”`,
  so Athena's council speech ends at 1.95 and no speech runs into this part. Line 96 (ὣς εἰποῦσ’)
  confirms it.
- **169 = 206.** The packet prints the two lines identically apart from the final point (`·` at 169,
  `,` at 206), and the two units' `l` and `i` are word-for-word identical, differing only in that
  trailing mark. The new-renderings entry is applied at both.
- **Stock epithets** were checked one by one against conventions.md: γλαυκῶπις Ἀθήνη "gleaming-eyed
  Athena" (156, 178), ταλασίφρων "enduring-minded"/"steadfast" (129), δαΐφρων "wise-minded"/"wise-hearted"
  (180), νόστιμον ἦμαρ "the homecoming day"/"the day of his homecoming" (168). No deviation.
  The new renderings (winged words, τὸν δ’ αὖτε προσέειπε, lordly suitors at 106 and 144, πατρώιος
  ξεῖνος at 176 and 187, οἶνοψ, ἀλλόθροος, αἴθων, πολυμήχανος, φίλη πατρὶς αἶα, κοίλῃς ἐνὶ νηυσίν,
  αἰδοίη ταμίη, ὑλήεις, θεοειδής, ὀβριμοπάτρη, δῖος) are applied consistently everywhere they recur.
- **Words of unknown meaning** are honestly flagged: πεσσοί (107, "what the game was is not known"),
  Παλλάς (125, "whose meaning is not known"), γλαυκῶπις (156, "the exact sense is uncertain"),
  δαΐφρων (180, both readings given), αἴθων (184, "of iron the sense is disputed"), ἀκαχμένον (99,
  "of obscure formation"). None of them is given a confident gloss elsewhere in the part.

## Changes made

Severity: **error** = a false statement or a missing structural mark; **minor** = an inexact or
over-reaching claim, or an internal inconsistency in the English.

| line · field | sev | what was wrong | what I did |
|---|---|---|---|
| 212 · `l`, `i` | error | **Athena's speech was left unclosed.** The drafter states that it runs on past 212; it does not. Murray's next line, 1.213, is the reply formula τὴν δ’ αὖ Τηλέμαχος πεπνυμένος ἀντίον ηὔδα, and 1.214 (τοιγὰρ ἐγώ τοι, ξεῖνε, μάλ’ ἀτρεκέως ἀγορεύσω) answers her 179 word for word — Telemachus is speaking from 213, so 212 ends the speech. The part boundary at 212 is itself the paragraph break Murray prints before that reply. | Added the closing `”` to both `l` and `i` of the 212 unit. All three speeches in the part now open and close correctly (123→124, 158→177, 179→212), each with `mark` on its first unit. |
| 212 · `n` | error | The note asserted "Athena's speech does not end here; it runs on past the last line of this part." | Replaced with "The line ends Athena's speech, and the English layers close their quotation marks here." |
| 110 (unit at 109) · `n` | error | "ἔμισγον and νίζον are unaugmented imperfects" — ἔμισγον is augmented (ἔ-μισγον; the unaugmented form would be μίσγον). νίζον is correctly unaugmented. | "ἔμισγον keeps its augment and νίζον beside it is an unaugmented imperfect". |
| 136 · `n` | error | "ἐπέχευε is an unaugmented imperfect of ἐπιχέω" — wrong on both counts. χευ- is the aorist stem (the same unit family the draft itself parses correctly at 146, "ἔχευαν … aorist"), and the ε after ἐπ- is the augment inside the compound. | "ἐπέχευε is the aorist of ἐπιχέω, the stem that comes again in ἔχευαν at 146, with its augment inside the compound (ἐπ-έ-χευε)." |
| 147 (unit at 146) · `n` | error | "παρενήνεον is an unaugmented imperfect" — the unaugmented form would be παρανήνεον; παρ-ε-νήνεον shows the augment after the elided preverb. | "…with its augment inside the compound (παρ-ε-νήνεον) and reduplication in the stem." |
| 168 · `n` | error | "ὤλετο is the unaugmented aorist middle of ὄλλυμι" — ὤ- is ἐ + ὀ, i.e. augmented; the unaugmented form is ὄλετο/ὄλοντο, which is in fact what stands at the 1.7 the note cites. | "ὤλετο is the aorist middle of ὄλλυμι and keeps its augment, beside the unaugmented ὄλοντο used of the companions at 1.7." |
| 194 (second unit) · `n` | error | "ἔφαντ’ is ἔφαντο, the unaugmented imperfect middle of φημί" — ἔ-φαντο is augmented (unaugmented φάντο). | "…the imperfect middle of φημί with its augment…". |
| 209 (unit at 208) · `n` | error | "ἐμισγόμεθ’ is the unaugmented imperfect of μίσγω" — ἐ-μισγόμεθα is augmented. | "ἐμισγόμεθ’ is ἐμισγόμεθα, the imperfect middle of μίσγω with its augment." |
| 188 · `n` | error | "εἴ περ with the **optative** εἴρηαι" — εἴρηαι is a subjunctive (-ηαι), not an optative (that would be ἔροιο); the note's own parenthesis "Attic ἔρῃ" is itself a subjunctive, so the note contradicted itself. | "εἴ περ with the subjunctive εἴρηαι (an uncontracted second singular subjunctive middle of the epic εἴρομαι = ἔρομαι, Attic ἔρῃ)". |
| 203 · `n` | error | "αἶα is the by-form of γαῖα used at 1.21 and 1.75" — 1.21 reads ἣν **γαῖαν**, not αἶαν. αἴης stands at 1.41 (ἧς ἱμείρεται αἴης) and 1.75; odyssey-001's own note at 1.74 says "αἴης is the by-form of γαίης seen at 1.41". | "…used at 1.41 and 1.75". |
| 152 · `n` | error | "τε is the epic τε that marks a standing truth, as at 1.51" — 1.51 (νῆσος δενδρήεσσα, θεὰ δ’ ἐν δώματα ναίει) contains no τε. The epic τε in odyssey-001 stands at 1.50 (ὅθι τ’), and again at 1.52–53. | "…as at 1.50". |
| 118 · `n` | error | "The line closes the sentence begun at 113" — 117 ends with a full stop, so 118 is a fresh sentence; and the note at 113 says in so many words that the sentence "runs on to the end of 117", so the two notes contradicted each other. | "The full stop at the end of 117 has closed the long sentence; this line begins again and gathers up both of its ideas, his thoughts and his seat among the suitors, in that order." (The order claim itself checks out: 118 has τὰ φρονέων first, μνηστῆρσι μεθήμενος second.) |
| 205 · `n` | error | The note glossed ὥς κε νέηται as "'that he is to return'" (the published wording at 1.87) while its own `l` reads "how he is to return" — a note contradicting its unit. | "…there 'that he is to return' after νόστον and here 'how he is to return' after φράσσεται…". `l` and `i` left alone: after φράσσεται "how" is the right English. |
| 129 (unit at 126) · `n` | minor | "the intransitive ἵστατο **at the end of** 129" — ἵστατο is not the last word of 129; πολλά is. | "the intransitive ἵστατο **in** 129". |
| 106 (first unit) · `n` | minor | "ends with a full stop in the middle of the verse, as at 1.19 and 1.26" — at 1.26 the mid-verse mark is an ano teleia (ἔνθ’ ὅ γ’ ἐτέρπετο δαιτὶ παρήμενος·), not a full stop. 1.19 is correct. | Dropped "and 1.26". |
| 169 · `n` | minor | "the imperative ἄγε used as an interjection, as at 1.76" — 1.76 prints the plural, ἀλλ’ ἄγεθ’ (= ἄγετε). | "…as the plural ἄγετε is at 1.76". |
| 180 · `n` | minor | "εὔχομαι, the verb Telemachus used at 172" — at 172 he used εὐχετόωντο, a different (if related) verb, as this draft's own note at 172 is careful to say. | "…after εὔχομαι, which answers Telemachus' εὐχετόωντο at 172". |
| 172 · `l` | minor | `l` read "Who did they **claim** to be?" while the unit's own note says the verb is "'declare oneself to be' rather than 'boast'", `i` reads "declare themselves", and the answering units at 180 and 187 both use "declare" in `l`. The one word broke the chain the note draws. | `l` → "Who did they declare themselves to be?" |
| 125 · `n` | minor | "ἕσπετο is the **unaugmented** aorist of ἕπομαι" — contestable: in Attic the non-indicative forms (σπέσθαι, σπόμενος) have no ἑ-, which makes the ἑ- of ἕσπετο the augment, though epic ἑσπέσθαι shows it reanalysed as stem. Not a label I can certify. | Dropped the word: "ἕσπετο is the aorist of ἕπομαι 'follow'." |
| 149 · `n` | minor | "…and it will return whenever a meal is described" — a claim about the rest of the poem that this part cannot show (conventions.md, *Notes*). | Sentence trimmed to "The whole line is a formula that closes the serving and opens the eating." |
| 188 · `n` | minor | "ἐπελθών … is the compound seen in μετελθών at 134" — they are two different compounds of ἔρχομαι, not the same one. | "ἐπελθών, 'having gone to him', is ἐλθών under another preverb, as μετελθών was at 134." |
| 145 (unit at 144) · `l`, `i` | minor | The two words for a seat were rendered the other way round from 130 and 132: θρόνος is "chair" at 130 and κλισμός "seat" at 132, but 145 had κλισμούς = "chairs" and θρόνους = "high-seats". A reader following either word through the part is actively misled. First rendering wins (conventions.md on repetition). | `l` "along the **seats and the chairs**", `i` the same. The note, which names both Greek words and cross-refers to 130 and 132, still reads true. |

**Totals: 22 edits — 13 error, 9 minor.** `t` was not touched in any unit; the rebuild check was
re-run after the edits and still reproduces the packet exactly.

## Findings considered and refused

1. **96 · `i` "keeping pace with the breath of the wind."** πνοιῇς is plural and ἅμα is "along with".
   Refused: "keeping pace with" is a fair rendering of ἅμα with a dative of accompaniment, `l` carries
   the plural ("the breaths of the wind"), and `i` is licensed to be English prose.
2. **101 · `n` "ὀβριμοπάτρη … a title of Athena alone"; 106 · `n` "in the Odyssey the word leans
   towards 'overbearing'"; 122 · `n` "the poem's commonest introduction to a speech."** All are, strictly,
   claims this part cannot demonstrate. Refused as a class: they are lexicographical facts of the kind
   Autenrieth and Cunliffe state and a tutor is expected to state, and striking them would mean
   rewriting a dozen notes. Only the one genuinely *predictive* claim (149, "it will return whenever…")
   was cut.
3. **101 · `n` κοτέσσεται "short-vowel aorist subjunctive."** Refused: this is the standard parse
   (LSJ s.v. κοτέω cites Od. 1.101 as a subjunctive) and the τε-clause of general truth requires it.
4. **106 · `n` "εὗρε keeps its augment."** εὑ- shows no visible augment, and Homer has no ηὗρε to
   contrast it with. Refused rather than reversed: the ε of εὗρον is commonly explained as the augment
   of ἐ-ϝρ-, so the claim is arguable and the opposite claim would be no safer.
5. **136 · `l` "poured over them … over a silver basin."** "Over" twice in one sentence. Refused:
   the ἐπι- of ἐπιχέω needs an object in English, and ὑπὲρ ἀργυρέοιο λέβητος is a separate phrase.
   Style, not error.
6. **155 · `i` "lifted up a beautiful song"** beside the note's "καλόν is an adverbial accusative …
   'to sing beautifully'". Refused: `l` carries the adverbial faithfully; `i` keeps the same sense in
   ordinary English.
7. **160 · `l` "unpunished"** beside the note's and `i`'s "without paying for it". Refused: νήποινος
   carries both "unavenged" and "without recompense", and "devour … unpunished" is within the word.
8. **179 · `l`/`i` "Well then … very exactly" / "Then … quite exactly."** A small drift in the force
   of τοιγάρ. Refused: `l` carries the particle; `i` is prose.
9. **185 · `l`/`i` "lies at her moorings"** for ἕστηκεν, which the note glosses "stands, is lying".
   Refused: the ship is ἐν λιμένι, and the perfect of ἵστημι of a ship is exactly "is lying"; "at her
   moorings" adds no fact the line does not give.
10. **149 · `i` "put out their hands to the good things lying ready before them."** Checked for
    remembered English; it runs close to Murray's own wording. Refused: Murray is the edition of
    record and public domain, not one of the banned modern translations, and this is the plainest
    possible construal of ἐπ’ ὀνείαθ’ ἑτοῖμα προκείμενα χεῖρας ἴαλλον. Nothing in the part reads as
    Lattimore/Fagles/Fitzgerald/Lombardo phrasing; 164 ("lighter on his feet rather than richer in
    gold and clothing") was checked on the same ground and falls straight out of the case relations.
11. **171 · τε left untranslated** in ὁπποίης τ’. Refused: a connective epic τε with no English
    equivalent here.
12. **193 · `n` "γουνός is a rise of ground"; 210 · `n` "ἀναβαίνω ἐς is to go up from the coast to an
    inland place."** Both are LSJ/Cunliffe senses, stated without overclaim. Refused.
13. **209 · `i` "astonishingly"** for αἰνῶς where `l` has "terribly". Refused: the note's "almost
    uncanny" covers both, and `l` keeps the literal word.
14. **Scansion.** The packet flags none. I scanned 1.100, 1.101, 1.157, 1.165 and 1.208 by hand;
    all fit dactylic hexameter without a licence worth recording — 157 needs correption in οἱ ἄλλοι,
    208 the familiar lengthening of καλά (κάλϝος), both of them ordinary. No flag raised, and no
    line in the part looks structurally broken.

## Verdict

**Ready to publish as it now stands.** The one finding that would have stopped publication — Athena's
speech left without its closing quotation marks, on the drafter's mistaken belief that it runs past
1.212 into the next part — is fixed, and with it the note that asserted the same thing. Murray's
1.213 is Telemachus' reply formula, so the speech is complete inside this part and nothing is left
hanging for odyssey-003.

One thing for the next part to carry forward: the drafter's weak spot here was the augment, six of the
thirteen errors being forms called "unaugmented" that in fact carry the augment, four of them inside
compounds (ἔμισγον, ἐπέχευε, παρενήνεον, ὤλετο, ἔφαντ’, ἐμισγόμεθ’). Worth a standing check.

## Pass 3 — glossary (`gloss.json`)

Every entry was read against the line or lines where its form actually stands in `units.json`, and
against the unit's own note where there is one: all **479** new entries and all **15** entries under
`__broaden__`, not a sample. Thirteen entries were changed; the rest stand.

### Mechanical checks that passed

- **Coverage is exact.** The 479 keys are precisely the 479 forms in `novel-forms.json` — none
  missing, none invented — and the 15 `__broaden__` keys are all in `known-forms.json`. Every one of
  the 494 keys is found in this part's `t` (case-folded), so no entry describes a form that is not here.
- **No key collides with the shipped glossary.** None of the 479 new keys already stands in
  `odyssey-glossary.json`, so the merge adds and never overwrites.
- **All 15 broadenings begin with the old entry character for character**, followed by ` · ` and the
  new reading. Checked by string comparison against `odyssey-glossary.json`, not by eye. Nothing was
  dropped or reworded: e.g. `περὶ` still carries the whole of "περί — around, about; prep. + gen.:
  ’superior to, beyond’; also as adv.: ’exceedingly, surpassingly’" before the new plain sense.
- **Format**: every entry is `<lemma> — <meaning>; <parse>` (the four bare particles `ἄν`, `κ`, `κεν`,
  `σφι` have no parse to give and carry no semicolon, as the shipped glossary's own particle entries
  do); keys all lowercased; typographic ’ throughout, no ASCII apostrophe, no backtick, no double
  quote anywhere; longest entry 227 characters, all under 230.
- **No entry is pinned to a line.** No entry contains a line number, and after the one fix below none
  says "here" except the four whose meaning *is* ’here’ (τόδε, ἐνθάδ, ἥδ, ὧδε).
- **Homographs.** All five are real and both readings occur in this part: `τοι` (enclitic dative at
  170, 179 · particle at 155, 200, 203), `ἦ` (affirming 155 · interrogative 158 · = ἤ in ἠέ … ἦ 175),
  `ἦλθον` (3 pl. 144 · 1 sg. 194), `εἰς` (prep. 172 · 2 sg. of εἰμί 170, 207), `πόσιν` (the new
  ’drink’ at 191, beside the inherited ’husband’). `καλὸν` likewise carries adjective (131) and
  adverbial accusative (155). None is padding.
- **Disputed meanings are owned**, and the list is right for this part: αἴθωνα (of iron the sense is
  disputed), γλαυκῶπιν (sense uncertain), δαΐφρονος (δαῆναι or δάϊς), οἴνοπα (colour unsettled),
  πεσσοῖσι (game unidentified), ἀκαχμένον (formation obscure), παλλὰς (origin unknown), ἀναθήματα
  (not yet ’votive offering’), βλάπτουσι and κατάλεξον (not yet the later senses).

### Changes made

Each is a single scoped edit to one entry's string; nothing else in the file moved.

1. **δῶ** · the entry read "indeclinable epic noun, **here** acc. sg.: ’to our house’" — the one
   entry pinned to its context, both in the forbidden word "here" and in a gloss (’to our house’)
   that only fits ἡμέτερον δῶ at 176. → "δῶ — house, home; indeclinable epic noun (= δῶμα), used as
   nom./acc. sg."
2. **τά** · lemma wrong. τά is a form of ὁ, ἡ, τό used relatively, not a form of ὅς, ἥ, ὅ (whose
   neuter plural is ἅ). conventions.md says so outright ("the article is a pronoun … τοί can be
   relative"), the unit note at 97 says so ("τά is the article-form used as a relative"), and the
   shipped glossary lemmatises τοὶ, τόν, τῷ exactly this way. → relemmatised under ὁ, ἡ, τό with
   "also relative: ’which’". The bare "(accented τά)" was replaced by the reason for the accent, the
   enclitic μιν that follows.
3. **τοῖσίν** · the same lemma error (τοῖσιν is not a form of ὅς, ἥ, ὅ). → relemmatised under
   ὁ, ἡ, τό, "also relative: ’with whom’", keeping the correct note on the accent before enclitic τε.
4. **τελέεσθαι** · parsed "pres. inf. mid." It is the **future** middle infinitive: it depends on
   ὀίω at 201, and the unit's own note calls it "the uncontracted future middle infinitive". →
   "fut. inf. mid., epic uncontracted (= Attic τελεῖσθαι)".
5. **ῥινοῖσι** · gender wrong: ῥινός is feminine in Homer (LSJ ἡ ῥινός). → "fem. dat. pl."
6. **ἔδουσιν** · parsed "pres. 3 pl., … **unaugmented**" — a present cannot be unaugmented. The same
   slip the drafter kept making on past tenses, now the mirror image. → "pres. 3 pl., from the epic
   present ἔδω (= Attic ἐσθίουσι)".
7. **μέν** · "(accented μέν when not followed in its phrase by another word)" is not why the acute
   stands at 127. It stands because the next word is the enclitic ῥ’. → "(the acute μέν is kept
   before a following enclitic; elsewhere μὲν)".
8. **τί** (`__broaden__`) · the new half said the indefinite is "(accented τί after οὐ … γάρ)". The
   accent at 173 comes from the enclitic σε that follows τι, not from what precedes it — every other
   entry in the file states this correctly. → "(accented τί before an enclitic)". The old entry's
   text is untouched, and the whole is 219 characters.
9. **πευθοίαθ** · "epic -αθ(ε)" invents an ending. The ending is the epic -ατο for -ντο; -αθ’ is that
   ending elided before οἱ and aspirated by its rough breathing, as the unit note says. → "epic -ατο
   for -ντο, elided and aspirated (πευθοίαθ’ = πευθοίατο)".
10. **εἴρηαι** · no tense given ("subj. 2 sg. mid."). It is the present subjunctive of εἴρομαι
    (the aorist would be ἔρηαι, without the εἰ-). → "pres. subj. 2 sg. mid., uncontracted
    (= Attic ἔρῃ)".
11. **κρειῶν** · "epic **uncontracted**" is the wrong label: κρεάων is the uncontracted genitive
    plural, κρεῶν the contracted one, and κρειῶν is κρεῶν with ει for ε (Monro §105). → "epic κρειῶν
    with ει for ε (= Attic κρεῶν)". **Left for the owner:** the note at 141 in `units.json` says
    "uncontracted" too. `units.json` is out of this pass's scope and was not touched, but the note
    and the entry now disagree and the note is the one that is wrong.
12. **χρυσοῖό** · the entry explained the added acute but not the form: it is the epic genitive in
    -οιο, which every comparable entry in the file (ἀνέμοιο, ἀργυρέοιο, προθύροιο, ποτοῖο, ὑψηλοῖο)
    names. → "gen. sg., epic -οιο (= Attic χρυσοῦ), accented on the ultima before the enclitic τε".
13. **εἴ** · "(accented εἴ, e.g. before an enclitic **or πέρ**)" implies περ is not an enclitic; it
    is, which is why the file's own πέρ entry explains *its* accent by a following enclitic. →
    "(accented εἴ before a following enclitic, περ among them)".

### Considered and left as it stands

1. **κρέα** · "neut. acc. pl., uncontracted (= Attic κρέα contr.)" reads oddly, since the two are
   spelled alike. It is nevertheless a real point — the Homeric plural is two short syllables (at 112
   κρέα scans ⏑⏑, with δὲ long before κρ), the Attic one contracted — so it is left.
2. **ταμίη, γρηῦς, ξεῖνος, πνοιή, κεῖνος, ἑξείης** and the like are lemmatised on the epic headword
   with the Attic given, not on the Attic headword LSJ files them under. That is the house practice
   (conventions.md's own model is `ἔμμεναι` → "εἰμί … epic (= Attic εἶναι)"), it is what Autenrieth
   and Cunliffe do, and the shipped glossary already has `αἴης` → αἶα. Consistent, so left.
3. **ἕντο** is lemmatised ἵημι, not ἐξίημι, with "in tmesis with ἐξ" in the parse. Defensible either
   way: the preverb stands apart in the line and has its own broadened entry under ἐξ. Left.
4. **Collocations inside parses** — αὐλείου "(οὐδοῦ ἐπ’ αὐλείου …)", κακὸν "inner acc. with μόρον",
   πολλά "(agreeing with ἔγχεα)", οἷσιν "(agreeing with δώμασιν)", ἀρχῆς "(ἐξ ἀρχῆς …)". These name a
   phrase, not a line, and they are what makes the parse checkable; conventions.md's own model entry
   for τὸν does the same with ’him’. Left, but they are the edge of the rule.
5. **ἀναβήμεναι** "go up (from the coast inland)" was checked against 210 (ἐς Τροίην) and against the
   pass-2 decision on that unit's note, which accepted the same LSJ/Cunliffe sense. Left.
6. **ὥς** (`__broaden__`) · the new reading ’how’ is right for 205, but the accent on ὥς there is
   thrown back by the enclitic κε and is not the accent of ὥς ’thus’ that the shipped `ὡς` entry
   contrasts. The broadening gives the reading without explaining the accent. Not wrong, and the
   entry is near the length limit; left.
7. **βρῶσίν, ὅττεό** carry an acute from a following enclitic that the entry does not explain,
   where χρυσοῖό, ἐσθῆτός, τοῖσίν, κεῖνόν, ἐγώ and πέρ all do. An inconsistency in helpfulness, not
   an error. Left.
8. **ἴδον** is parsed "aor. 1 sg." (its use at 212) though the form is also the epic 3 pl. Only the
   first-person use occurs in this part, and the entry is parsed in context as the runbook asks.
   Left; a later part that has the 3 pl. will broaden it.
9. **ὀβριμοπάτρη** is glossed ’of the mighty father’ without a doubt flag. Unlike ἀργεϊφόντης the
   compound is transparent (ὄβριμος + πατήρ) and no caution is owed. Left.

### Verdict

**`gloss.json` is ready to merge into `odyssey-glossary.json` at build time.** The 479 new entries
add no key that already exists, and the 15 broadenings preserve their old entries whole, so the
merge is additive in both directions, as conventions.md requires. The one thing the owner should
know is item 11 above: the note at 141 in `units.json` still calls κρειῶν "uncontracted", and that
note, not the glossary entry, is now the inaccurate one.
