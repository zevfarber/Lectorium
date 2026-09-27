# Review — odyssey-020 (Odyssey 4.641–741)

Two passes made, per the runbook. Pass 1 covered (a)–(h) (grammar labels, word-position claims,
cross-references, note/`l`/`i` agreement, Greek→`l` fidelity, `l`↔`i` agreement, remembered English,
quotation marks/`mark`). Pass 2 re-read the corrected `units.json` against `packet.md` alone —
`gloss.json` does not exist yet in `drafts/odyssey-020/`, so **the glossary cross-check is deferred**
to whenever the glosser's pass produces it; the runbook's second-pass instruction to check `gloss.json`
could not be carried out this round.

`units.json` was edited in place; no `t` field was touched (verified by diff and by a script that
confirms every `t`, in order, still reproduces the packet's Greek exactly — see rejected finding 5
below).

## Changes made

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 4.657 | `i` | medium | θυμὸς ἀγήνωρ is house-fixed (conventions.md) as `l` "manly spirit" / `i` "proud spirit" (4.548). The draft's `l` correctly used "manly spirit," but its `i` dropped "spirit" entirely — "a proud amazement seized their hearts" — breaking the fixed rendering the table requires for a repeated formula. | Rewrote `i` to "So he spoke, and went off to his father's house, and in both men their proud spirit was seized with wonder," restoring the fixed phrase while keeping the sense. |
| 4.677 | `n` | high | The note labelled ἐπεύθετο "aorist middle of πυνθάνομαι." It is actually the **imperfect** (middle) of πεύθομαι, a Homeric present-stem by-form of πυνθάνομαι (Cunliffe/Autenrieth both give ἐπεύθετο under πεύθομαι as an imperfect; πυνθάνομαι's aorist is the distinct ἐπυθόμην/πυθόμην). Wrong tense and wrong lemma. | Corrected the label to "ἐπεύθετο is an imperfect (middle) of πεύθομαι, a Homeric present by-form of πυνθάνομαι, 'was learning of, was getting wind of' (describing his overhearing as it went on, not a completed act)." |
| 4.694 | `n` | high | The note claimed ἀεικέα ἔργα "echoes the fixed ἀεικής already given for ἐν δόμῳ at 3.132/3.194." Checked against conventions.md's actual table: the row at 3.132/3.194 is the entry for **λυγρός** ("grievous"), an unrelated word — there is no ἀεικής entry there, and no "ἐν δόμῳ" phrase either. A false cross-reference. | Replaced with the real, existing cross-reference: the table's `ἀεικέα πότμον` row (4.339, 4.340), which does fix "unseemly" for this same adjective ἀεικής. |
| 4.703 | `n` | medium | The note said the γούνατα-καὶ-φίλον-ἦτορ double subject is "the whole-and-part construction seen already at ἕρκος ὀδόντων." ἕρκος ὀδόντων is a fixed idiom/kenning (a plain genitive of material, "the fence *of* teeth"), not a genitive-of-person-plus-nominative-of-body-part construction — the grammatical parallel asserted is false, even though ἕρκος ὀδόντων itself is a real, correctly-cited table entry. | Removed the false analogy; described the genitive-of-the-whole (τῆς ... αὐτοῦ) plus nominative-of-the-part (γούνατα, ἦτορ) construction on its own terms, which is accurate. |
| 4.715 | `n` | low | Companion to the 4.674 addition below, for internal consistency now that 4.674 carries the fuller note. | Added one sentence: "Ὀδυσῆος again keeps the single -σ- for the metre, as at 4.674." |
| 4.674 | `n` | low | The note said nothing about Ὀδυσῆος's single -σ-, although conventions.md's own Notes section names *exactly this word* ("Ὀδυσσῆος beside Ὀδυσῆος") as the paradigm case for when metre must be mentioned in a note — and this part genuinely uses both spellings (single-σ at 674, 715; double-σ at 682, 689, 741), each metrically required (verified by running `scan_hexameter.py`: the single-σ spelling keeps -δυ- short where a double σ would close and lengthen the syllable). This was a real, citable omission, not an invented one. | Added: "Ὀδυσῆος keeps the single -σ- here, beside the regular double-σ Ὀδυσσῆος/Ὀδυσσεύς used elsewhere in this same part (4.682, 689, 741): Homer varies the spelling of the name to keep the following syllable short or long as each line's metre needs." |
| 4.722 | `n` | high | The note said "ἐκ πασέων is 'beyond all', governing the partitive genitive ὅσσαι." This is doubly wrong: ὅσσαι (= ὅσαι) is **nominative** plural, not genitive at all, and it is not "governed" by ἐκ πασέων — it is ἐκ that governs the genitive πασέων. ὅσσαι is the subject of the following relative clause (τράφεν, ἐγένοντο). | Corrected: "ἐκ πασέων, 'beyond all', is itself the partitive genitive governed by ἐκ; ὅσσαι (nominative plural, 'as many as') is not itself governed by ἐκ but introduces the following relative clause, agreeing with πασέων and serving as subject of τράφεν and ἐγένοντο." |

7 changes: 3 high, 2 medium, 2 low.

## Findings considered and rejected

1. **δαΐφρονος applied to Telemachus, not Odysseus (4.687)** — the drafter's own report flagged this
   as a judgment call. Checked against the house table's δαΐφρων/πολύφρων/ταλασίφρων row (fixed for
   "three different epithets of Odysseus **in this part**", i.e. the pilot part) and against the
   general rule that "stock epithets are translated every time, the same way every time, even where
   they sit oddly with the context." Murray's Greek genuinely does apply δαΐφρονος to Telemachus here
   (κτῆσιν Τηλεμάχοιο δαΐφρονος, 4.687), and the fixed English "wise-minded" is used correctly and
   flagged honestly in the note. No change.

2. **θεῖος of Odysseus (4.682, Ὀδυσσῆος θείοιο) and of kings (4.691, θείων βασιλήων) rendered
   "divine"** — checked against the table's reservation of "divine" for θεῖος (opposed to "heavenly"
   for δῖος, fixed at the δῖος row and cross-referenced at the θεῖος/Phemius row). Both are genuine
   θεῖος forms, correctly parsed, and the rendering is internally consistent between the two
   occurrences. No change.

3. **Two units cut at a comma rather than run to the next period/ano teleia, because the sentence
   would otherwise exceed four lines (4.687–689 / 690–691, and 4.735–738 / 739–741)** — checked
   against the actual packet lines by counting. In the first case, running the sentence from
   δαΐφρονος· (mid-687) to βασιλήων· (end-691) would touch five line-numbers; the comma chosen (after
   τοκεῦσιν, at the end of 689) is the strongest available syntactic pause within the four-line cap
   (it closes the whole relative clause "what sort of man Odysseus was..." before the participial
   elaboration begins) — an earlier comma (after ἀκούετε, or ἐόντες,) would have been a weaker break
   inside the same clause. In the second case, the only comma at all within the first four lines
   (735–738) is the one after καταλέξῃ, at the end of 738 — the next comma falls in 740, six lines in
   — so the cut is not just defensible but the only one available. Both are correct as drafted. No
   change.

4. **πλῆσθεν with dual ὄσσε, a number mismatch (4.705)** — checked. πλῆσθεν is a genuine, well-attested
   Homeric apocopated 3rd-plural aorist passive (-θεν for -θησαν) used, as often, with the old dual
   ὄσσε; the note's label is grammatically accurate. The draft's own note two lines earlier (4.662,
   ἐίκτην, correctly dual and correctly labelled dual) shows this was a deliberate, informed contrast
   being drawn, not a slip. No change.

5. **Joining every unit's `t` in order does not byte-for-byte reproduce the packet's raw Greek** — an
   automated check found the concatenation differs from the packet text by exactly one whitespace
   character (a space or a line-break) at every unit boundary that falls mid-line or at a line-end;
   inserting that one character at each such boundary makes the two texts identical letter for letter,
   with no word, letter, elision mark or punctuation mark added, dropped, or reordered anywhere. This
   is a uniform, mechanical property of the slicing script (which trims the single inter-unit space),
   not a drafting error, and in any case `t` is outside the reviewer's remit to alter. No change.

6. **Scansion** — packet.md reports "Scansion flags: none" for this part. Ran `scan_hexameter.py` by
   hand over all 101 lines (4.641–741): 0 lines needed an unresolved licence, 0 failed to fit at all.
   Five lines (4.682, 685, 698, 701, and one more) come in above the ordinary cost floor, but each
   resolves with a named, catalogued Homeric licence (synecphonesis at ἦ εἰπέμεναι, lengthening before
   an initial nasal, mute-plus-liquid not making position, a short closed final lengthened before a
   vowel) — none of these is the kind of *unexplained* irregularity the convention says merits a note.
   "Scansion flags: none" stands confirmed. No change.

7. **Quotation marks and `mark` placement across all 8 speeches, and continuity from odyssey-019** —
   checked systematically (script-assisted): each of the 8 speeches carries `mark` on exactly its
   first unit (never on the narrator's intro-formula line), opens with “ and closes with ” in both `l`
   and `i` on the correct units, and no stray quotation marks appear mid-speech. Read odyssey-019's
   final three `sentences`: the part ends in plain narration (ἔφαθ’, οἱ δ’ ἀνὰ θυμὸν ἐθάμβεον ... οὐ
   γὰρ ἔφαντο ...), no speech left open, no dangling `mark`. odyssey-020's own opening unit (4.641,
   the reply-formula τὸν δ’ αὖτ’ Ἀντίνοος προσέφη) is correctly unmarked narration, and the first
   speech (Antinous's question) begins cleanly at the next unit. No change.

8. **new-renderings.md's 8 new formulas** — checked each for register/method against the house table
   and for self-consistency across every recurrence inside this part: the ὣς ἄρα φωνήσας ἀπέβη
   masculine pair (4.657 = 4.715) keeps identical wording at both occurrences; Μέδων πεπνυμένα εἰδώς
   (4.696, 4.711) keeps identical epithet wording at both occurrences even though the surrounding
   reply-verb differs ("addressed" at 696 for προσέειπε vs "answered" at 711 for ἠμείβετο — correctly,
   since those two verbs already have their own separate fixed renderings in the table, and only the
   epithet needed to repeat). All 8 are well-chosen and consistent. No change.

9. **Paragraph markers (`p: true`)** — cross-checked all 13 against packet.md's ¶ marks (641, 648,
   657, 663, 673, 675, 681, 696, 703, 707, 711, 715, 722): exact match, no extra or missing marker. No
   change.

## Status

Ready to hand to the glosser. The glossary cross-check itself is deferred, per the runbook, until
`gloss.json` exists.
