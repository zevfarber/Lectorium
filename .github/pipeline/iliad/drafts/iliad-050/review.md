# Review of iliad-050 (Iliad 8.381–468)

Two passes over `units.json` (52 units). Pass 1: every grammatical label, positional claim and cross-reference in the notes, checked against the line and against the neighbouring lines (399, 401, 1.212, 1.332–333, 2.8, 4.20–24, 5.719, 5.767, 8.32–37, 8.374 and Odyssey 1.99–101, 4.39–42 were read in the archive or the shipped parts). Pass 2: Greek to `l` word by word, `l` against `i`, remembered English, quotation marks and `mark`, then `gloss.json` against the lines (read only, not edited).

`t` is untouched: the units' `t`, joined, still equal 8.381–468 of the archive character for character. Eleven fields changed in seven units (below). Severity scale: **major** = wrong grammar label, or `l`/`i` that breaks a fixed house rendering; **minor** = true but imprecise or misleading; **nit** = consistency of wording only.

## Changes made

| Line (unit) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 414 | `l`, `i`, `n` | major | ἐπαμυνέμεν rendered "to come to the aid of". The table fixes ἐπαμύνω as "come to the defence of" (6.361, 5.685), and `new-renderings.md` gave no reason for a departure ("aid" was only an unexplained choice). | `l` and `i` now "to come to the defence of the Argives"; note gloss changed to ‘come to the defence of’; `new-renderings.md` row rewritten (follows 6.361 and 5.685). |
| 441 | `l`, `i`, `n` | major | βωμοῖσι rendered "stands". The table fixes non-sacrificial βωμός as "pedestal" (odyssey 7.100, with "altar" reserved for sacrifice), and the drafter's own row listed "pedestals" as avoided without a reason. | `l` "upon the pedestals", `i` "on its pedestals"; note now says the word is more often "altar" but no sacrifice is in view; `new-renderings.md` row rewritten. |
| 429 | `n` | major | "ἀποφθίσθω is the aorist passive of ἀποφθίνω". The form is the aorist middle imperative (root aorist ἀπεφθίμην); the passive would be ἀπεφθίθη-. | "aorist passive" changed to "aorist middle". |
| 429 | `n` | minor | "κεῖνος … is Zeus, who is not named." Zeus is named at 427 and 428; he is unnamed only in this sentence. | Now "who is not named in this sentence (he is in 427–428)". |
| 389 | `n` | minor | The scansion sentence said "the syllable of φλόγεα that is short by nature … in the third foot", but all three syllables of φλόγεα are short by nature. By hand and by the scanner (`UNRESOLVED`; licence "metrical lengthening: φλόγεα [longum of foot 3]"), the syllable counted long is the last one, α, which opens foot 3. The irregularity is real. | Sentence now reads "the last syllable of φλόγεα, short by nature, has to be counted long, as the long syllable that opens the third foot." |
| 455 | `n` | minor | "ἂν with the dual imperfect of ἱκνέομαι" states as fact a parse that the form does not decide. ἵκεσθον could also be a short-vowel subjunctive (this is how `gloss.json` takes it). The sense in the line, after τὸ δέ κεν τετελεσμένον ἦεν, is past ("would not have come"). | Note now says the form is ambiguous, could be read as a subjunctive, and that the context asks for the past sense. See the gloss findings below. |
| 404 | `n` | nit | Note named the verb ἀπαλθαίνομαι, `gloss.json` has ἀπαλθήσκομαι; neither can be checked here without a dictionary, and note and entry must not disagree. | Note now gives ἀπαλθήσκομαι ‘be healed of’ (related to ἀλθαίνω ‘heal’), as the gloss does. |
| 381 | `n` | nit | The note cited only 5.719 (Athena obeying Hera). The whole line also stands at 5.767 (Hera obeying Zeus, speaker "he"), which is the reason `l`/`i` differ here. | Added "and the whole line stands at 5.767, said of Hera obeying Zeus." |
| 414, 441 | `new-renderings.md` | — | Rows out of step with the units. | Both rows rewritten as above. (Row 1, 8.381, had already been reworded by the drafter and was left as it stood.) |

## Hand scan of the flagged line

389 `ἐς δ’ ὄχεα φλόγεα ποσὶ βήσετο, λάζετο δ’ ἔγχος`: scanned as ἐς δ’ ὄ|χεᾱ φλό|γεᾱ πο|σὶ βή|σετο λά|ζετο δ’ ἔγ|χος (final α of ὄχεα long before φλ-, final α of φλόγεα lengthened in the longum of foot 3 at the main caesura). The unit's note already had a sentence on it; it is now precise (above). No other line is flagged.

## Pass 1 and 2: checked and found true (no change)

- Every cross-reference in the notes: 5.719, 5.757, 8.32–37, 1.212, 1.332, 1.333, 2.8, 4.20–24, 8.47, 374, 393, 397, 398, 399, 401–408, 437, 447, 452, and Odyssey 1.100–101, 4.39–42.
- Speech marks: openings at 399, 413, 427, 447, 462 and closings at 408, 424, 431, 456, 468, each on both `l` and `i`; counts balance (5 and 5). `mark` is on the first unit of each speech. Athena's speech closes in iliad-049's last unit (379–380), so unit 0 correctly has no opening mark. Hera's last speech ends at 468, with the “ ” that the shipped 8.37 has. Iris's report of Zeus (415–422) carries no inner marks, as indirect speech.
- `p` marks at the seven paragraphs (381, 397, 409, 425, 432, 438, 457).
- Units equal to shipped ones (382–383, 387–388, 392, 393, 394–395, 401, 446, 457–458, 459–460, 461, 462, 464–465, 467, 468) repeat the shipped `l` and `i` exactly; the validator's identical-Greek check will not fire. Lines 389–391 follow the shipped 8.389–390 and Odyssey 1.100–101 English.
- House renderings confirmed against the table: λευκώλενος, πρέσβα, μώνυχας, νεφεληγερέτα, εὐρύοπα, μακρὸν Ὄλυμπον, καλλίτριχας, κυδιάνειρα, φαίδιμα, ἀλαπαδνός (cf. ἐπιεικτόν at 8.32), αἰνότατε (cf. 1.552), δακρυόεντα, λῖτα, θρόνος, κλισμός, δίφρος, γυῖα, κότος, ἠπείλησε, ὀνήσει, ἀκέων, σκυζομένη, κατέχευε, θωρήσσω.
- Remembered English: no phrase in `i` arrives fully formed from a published translation; the ones that read familiar ("Be off with you", "took hold of your glorious limbs", "savage anger took hold of her") are the table's or the shipped repeats.

## Findings considered and refused

| Line | Finding | Reason refused |
|---|---|---|
| 397 | ἄρ’ is left untranslated in `l` ("when he saw, was incensed dreadfully"). | A particle that English cannot carry; the shipped `l` of 392 (5.748) leaves ἄρ’ out in the same way. Not an error. |
| 399–400 | `i` adds "with me" to ἄντην ἔρχεσθ’ ("come face to face with me"). | The note says the person faced is unstated and understood; συνοισόμεθα ("we shall come together") makes it Zeus. Keep. |
| 404, 418 | `i` "lay on you" for μάρπτῃσι (`l` "seize"). | Recorded and reasoned in `new-renderings.md`; the note gives the Greek sense. Keep. |
| 413 | `i` loses the dual of σφῶϊν. | The note and `l` carry it; `i` is allowed to be idiomatic. Keep. |
| 423 | `i` uses a dash ("dog, you fearless one — if you truly dare"). | 26 shipped Iliad units use a dash in `i` or `l`. Keep. |
| 433 | `l` of 435 has "they leaned" where the Odyssey's `l` has "leaned" with a different subject. | Different unit and different sentence; the Odyssey `l` does not fit this subject. Keep. |
| 429–431 | `i` names "Zeus" for κεῖνος. | The note says who κεῖνος is; naming is the same device as 8.381 and 8.397. Keep. |
| 448 | ὀλλῦσαι called a feminine participle "agreeing with the two goddesses" (plural form, dual subject). | Correct as written and parallel to the other plural-for-dual forms the notes already flag. Keep. |
| 413 | Note lemma μέμονα, `gloss.json` lemma μέμαα (μάομαι). | Both are one perfect paradigm (dual μέματον); not a conflict in the sense, left to the glosser's lemma convention. |
| Notes 10, 12, 25, 28, 30, 4, 2 | Notes run past the 110-word band (117–142 words). | Warning only; the length is content (a speech's opening, or tmesis, dual and house-rendering remarks), and shortening would cut true statements. |
| 393–395 | Unit 6 ends at a comma, with the sentence running on 393–396 (four lines, not past four). | The cut matches the shipped units for the same Greek (5.749, 750, 752), which the identical-Greek rule requires. Keep. |

## Second pass: `gloss.json` against the lines (report only; the file was not touched)

Real problems, for the glosser:

1. **ἔωθεν** (408, 422): entry reads "from dawn, at daybreak, early; adv." In both lines it is the 3 sg. perfect of ἔωθα (= εἴωθα) "be accustomed", with movable ν, governing the infinitive ἐνικλᾶν. As written, the entry is wrong for this part.
2. **ἵκεσθον** (455): entry parses an aorist subjunctive with ἄν and glosses ‘you two will come back’, but the line is past ("would not have come" in `l`/`i`). Read it as ambiguous (dual past form of ἱκνέομαι with ἄν) and give the past sense; the unit note now says the form is ambiguous.
3. **βωμοῖσι** (441): entry "raised base, stand, platform (also altar)". The rendering is now "pedestal(s)"; word the entry "pedestal, raised base (usually ’altar’)".
4. **ἐπαμυνέμεν** (414): "come to help, defend". The rendering is now "come to the defence of"; word the entry the same way.
5. **χρυσόπτερον** (398): "golden-winged". The house rendering is "gold-winged"; "golden" is avoided (it belongs to χρύσεος).
6. **κότος**: the entries for ἔθεσθε ("you conceived wrath") and the `__broaden__` entries for αἰνὸν ("grim wrath") and τοῖσιν ("you conceived wrath") use "wrath", which is the house word for μῆνις. κότος is "resentment" (as in `l`).
7. **ἐΰτροχον** (438): "well-wheeled" is kept for ἐύκυκλος; ἐΰτροχος is "well-rolling".

Smaller points: ἀγγελέουσα(ν) glossed "to announce" (the house phrase is "to bring news"); ἄξειν/ἄξω "smash" (the lines say "break to pieces"); βαλέω "I will hurl" ("throw" in the lines); τετελεσμένον with ἦεν "would be fulfilled" (the lines say "would have been fulfilled"); ἀδεὲς should say that the form may be vocative or adverbial; χώσατ ’grew angry’ (house "be incensed"). Parses checked and true: all other novel forms and the `__broaden__` readings for καλὰ, μάχηται, πολέμου, πυκινὸν, στῆθος, τοῖσιν, τόσον, ἐμόν, ἐφ, ἔννεπε, ἕλκε, ᾗ.

## Counts

Changes made: 3 major, 3 minor, 2 nit (plus the two `new-renderings.md` rows). Findings refused: 11. Gloss findings reported: 7 real, 6 small.
