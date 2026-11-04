# Review — iliad-149 (Iliad 23.586–699)

Two passes. Pass 1: notes, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks and marks, flagged lines, cross-references checked against `source/iliad-monro-allen1920.json`, house table checked against `conventions.md`. Pass 2: re-read of every changed unit, a fresh check of the whole file for typography and structure, and `gloss.json` (present by then) read against the line and against the notes. `t` was not touched (checked by script against the original: identical for all 92 units; `ln`, `p`, `mark` also unchanged). Edits made to `units.json` only, by script.

Counts: 16 rows fixed in `units.json` (1 high, 5 medium, 10 low), 21 field edits. Reported but not fixed (other files, or would touch `t`): 1 structural point, 1 stale file (new-renderings.md), 5 faults in gloss.json. Scansion flags in the packet: none.

## Changes made to units.json

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 613 · n | high | The note said ὃ δ’ (“and he”) is Antilochus “who now takes his own prize”. The cauldron is the third prize (23.267) and went to Menelaus (third in the race); Antilochus’ prize was the mare (23.265, second). Menelaus gives the mare to Noemon and takes the cauldron himself. The note misled the reader about who the subject is. | Note now says ὃ δ’ is Menelaus, who takes the cauldron that was third (23.267), and that Antilochus keeps the mare, which was the second. `l`/`i` left as they were (they keep the Greek’s ambiguity of “he”). |
| 587 · l, i | medium | ἄνσχεο rendered “Endure now” / “Be patient now”. The house table (1.586, 5.382, 7.110) fixes “Endure” for τέτλαθι only and gives ἀνέχομαι (ἀνάσχεο) “hold out” (`l`) / “bear up” (`i`), and lists “be patient” as avoided. new-renderings.md claimed the opposite. | `l` “Hold out now;” `i` “Bear up now;” |
| 591 · i | medium | “So let your heart bear it” would now collide with “Bear up” two units earlier, and ἐπιτλήτω is the τλάω-verb that the table renders “endure” (τέτλαθι “Endure it”). | `i` “So let your heart endure it;” (`l` “let your heart endure” was already right). |
| 609 · n | low | Note said Antilochus “asked him to be patient (587)”, now out of step with the rendering. | “asked him to bear up (587)”. |
| 629 · l, i, n | medium | First line (εἴθ’ ὣς ἡβώοιμι …) rendered “in my prime” after the Odyssey. The Iliad table (7.133, 7.157; 9.446; 12.382) fixes ἡβώοιμι as “young” and lists “in my prime” as avoided (it loses ἡβάω); the line is also 7.157 and 11.670 (iliad-042, iliad-070) except τέ for δέ. The Odyssey wording is to be reused “unless the Iliad context forbids it”; the Iliad table forbids it. Note also called an optative wish “a wish that cannot be met” (the optative says no such thing; the context does). | `l` “If only I were so young, and my strength were firm,” `i` “If only I were as young as that, and my strength were firm, as when …” (the published Iliad wording, iliad-070). Note now names 7.157 and 11.670, the τέ/δέ difference, and says “a wish, here for a strength he no longer has”. |
| 647 · l, i, n | medium | πρόφρων rendered “willingly” / “gladly”. The table (8.23, 8.39, 22.302) fixes “ready-minded” (`l`) / “with a ready mind”, “readily” (`i`) and lists “willingly”, “gladly” as avoided. | `l` “And this I, ready-minded, accept, …” `i` “I accept this readily, …”; note gives “ready-minded” (πρό + φρήν) and “readily”. |
| 696 · i | medium | “his head lolling to one side” is a remembered English phrase (it arrived fully formed), and “to one side” is also off: ἑτέρωσε is “to the other side”, as the `l` and the note say. | Rebuilt from κάρη βάλλονθ’ ἑτέρωσε and the note (“let drop”): “his head dropping to the other side;” |
| 634 · n | low | “Five victories follow … in boxing, wrestling, running and the spear throw”: four contests, five men. And “Ἤνωψ” is not the nominative of Ἤνοπος (it is Ἤνοψ). | “Four victories follow (634–637), over five men, …”; “Ἤνοψ”. |
| 592 · n | low | “the main clause follows in the next two units”: it is one unit (593–595). | “next unit”. |
| 603 · i | low | “you were never one to swing aside, nor senseless” does not follow οὔ τι … οὐδ’ (a “neither … nor”); the second term is left hanging. | “you were neither one to swing aside nor senseless;” |
| 627 · n | low | “The edition prints no commas in this line” is false: there is a comma after πόδες. What is true is that none stands round φίλος. | “The edition prints no commas round φίλος.” |
| 643 · n | low | “ἐμὲ δέ two lines on”: it is the next line (644). | “in the next line”. |
| 650 · i | low | “in return for this” for τῶνδ’ (plural) while the note and `l` say “these things”. | “in return for these things.” |
| 685 · n | low | “(as at 23.258)” for ἐς μέσσον ἀγῶνα: 23.258 does not have the phrase; it has the people sitting in the ἀγών. | “(they sit down in it at 23.258)”. |
| 692 · l | low | μέλαν … κῦμα “a black wave” in `l`; the Odyssey table (6.91) and the Iliad rows for μέλαν ὕδωρ / μέλαν αἷμα (5270, 2727) give “dark”, and `i` already said “dark”. | “a dark wave covered it”. |
| about | low | Straight apostrophe in “young man's”; the file uses ’ throughout. | “young man’s”. |

## Checked and found true (no change)

- Quotation marks: six speeches, each opened with “ on its first unit (587, 602, 618, 626, 658, 667) and closed with ” on its last (593–595, 610–611, 620–623, 650, 663, 675); `mark` is on exactly those six units; no stray marks. The neighbouring part’s last unit (iliad-148, repository root) ends Menelaus’ speech at 585 with ”, so 586 correctly opens with no mark. `p` falls on 586, 596, 612, 624, 651, 664, 676 = every ¶ of the packet.
- Reused lines: 626 (odyssey-089), 657 (iliad-145), 672 (iliad-003), 676 (iliad-017) are identical in `l` and `i` to the published units; 601/625 follow 1.201 with the pronoun changed, as new-renderings.md records; 658 first line is the published wording.
- Cross-references checked against the source: 2.621, 2.707, 3.167, 4.187, 7.156 (παρήορος), 10.226, 16.471, 22.257, 23.163, 23.258, 23.264–271, 23.484, 23.573, 23.581, 1.212 — all true as cited. 11.455/18.334/7.41 appear only in new-renderings.md and the table, where they were checked.
- Every `l` has the same number of lines as its `t`; `i` has no newline; the units reproduce the packet lines exactly (script).
- Scansion: the packet flags nothing. The scanner reports “spondaic fifth” at 645, 666, 680, 684 (not UNRESOLVED/AMBIGUOUS); that is a regular variant, not an irregularity, so no sentence was added to any note.

## Findings considered and refused

- 592 `i` “And even if …” where the Greek (εἰ καί) has no connective: natural English after “…the one that I won.” and does not change the force. Left.
- 604 `i` “but this time” for asyndeton νῦν αὖτε: marks a real contrast with πάρος (603). Left.
- 615 `l` “as he had driven” against the note “as he drove”: pluperfect-sense in English for the aorist, same fact. Left.
- 640 `i` “in indignation” against the table’s `i` “feeling indignation” (7.41): the participle needs a phrase in a longer sentence; the word and sense are the table’s and new-renderings.md says so. Left.
- 651–652 αἶνος “praise … of the son of Neleus” could be read as praise *for* Nestor: αἶνος is Nestor’s speech of praise (note says “Nestor’s speech of thanks”); `l`, `i` and note agree. Left.
- 671 `i` “can ever become” for ἦν … γενέσθαι: a gnomic present for the imperfect; sense (“it was not possible”) is the same. Left.
- 674 αὖθι and 640 αὐτόθι both “on the spot”: different words, but both mean “right there”. Left.
- The “both-sides-set”, “toil-enduring”, “swung-aside” renderings of ἀμφίθετος, ταλαεργός, παρήορος: unknown or uncertain words, declared as such in the notes and in new-renderings.md; the παρήορος departure from the table’s 7.156 and 16.471 rows is stated there. Left.
- 627 vocative φίλος: the only reading that the grammar allows; the note says so. Left.
- 596 `i` “led the horse up” (the “up” is not in ἄγων): harmless, the horse is brought to Menelaus. Left.
- Comma splits: see below.

## Reported, not fixed (outside `units.json` or would touch `t`)

1. **Comma-ending units.** 19 of 92 units end at a comma (indexes 7, 12, 18, 19, 36, 38, 40, 46, 49, 50, 59, 62, 65, 71, 74, 79, 85, 88, 90; the other Iliad parts have 2–13 %). The Odyssey rule is to cut only at a stop unless the sentence runs past four lines. Clear cases of a short sentence cut at a comma: 602–603 (two units, 2½ lines), 638–640 (three lines), 643–645 (three units for three lines), 647–649. Mending them means moving `t`, which the reviewer may not do; the drafter or the owner should decide. The build does not enforce it.
2. **new-renderings.md is now stale** (not edited, other file). Rows to correct before the table is copied to conventions.md: ἄνσχεο (now `l` “Hold out”, `i` “Bear up”; “be patient” is the table’s avoided word, not “kept” for it); ἐπιτλήτω (`i` now “endure it”; the avoided column no longer mentions “be patient”); the 23.629 row (now the Iliad wording of 7.157/11.670, not the Odyssey’s); add πρόφρων (“ready-minded” / “readily”, the table’s). Also remove “lolling” from the κάρη βάλλονθ’ row (`i` now “dropping to the other side”).
3. **gloss.json (second pass; the glosser’s file was present)**: all 116 novel forms are covered, all 12 `__broaden__` entries are true of the line, no entry is 230 characters or more, typography is ’ throughout. Faults:
   - `ἄνσχεο`: gloss “’be patient’” contradicts the table (“hold out”); change to ’hold out’.
   - `ἀρόμην`: lemma αἴρομαι “(= Attic ἠράμην)” is wrong and disagrees with the unit’s note; ἀρόμην is the unaugmented second aorist of ἄρνυμαι (ἠρόμην, inf. ἀρέσθαι), “win”.
   - `θίν`: “(= dat. θῖνι or acc. θῖνα)” leaves open an accusative; after ἐν only the dative is possible here; say “= dat. θῖνι”.
   - `κτερέϊζε`: lemma spelt κτερείζω; the note and LSJ have κτερεΐζω.
   - `ἀέθλοισι`: lemma ἄεθλον, while the note says ἄεθλος; harmless but not the same word. (Minor.)
