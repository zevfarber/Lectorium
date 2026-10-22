# Review — iliad-049 (Iliad 8.292–380)

Two passes. Pass 1: units.json against packet, conventions (prose and house table, both poems) and the end of iliad-048 (Agamemnon's speech closes there with ”; Teucer's reply opens at 8.292 as narration, mark on 8.293; quotation marks on the three speeches 293–299, 352–356, 358–379 are correct and each has its mark). Pass 2: gloss.json against the lines (all 136 novel forms present, none extra; every entry under 230 characters, typographic ’ only; the six `__broaden__` entries each begin with the old entry whole). `t` untouched (checked by script against the original); l/t line counts equal in every unit; JSON valid. Scansion flags: none in the packet, so no hand-scansion was required. No high-severity findings.

Counts: high 0 · medium 13 (12 in units.json, 1 in gloss.json) · low 16 (11 in units.json, 5 in gloss.json); 10 findings refused.

## Changes to units.json (line = `ln` of the unit)

| Line | Field | Sev | What was wrong | What was done |
|---|---|---|---|---|
| 297 | n | low | χροΐ printed with acute+iota; the text has χροῒ (diaeresis) | respelled χροῒ |
| 299 | n | low | λύσσα called "dog-like frenzy" (unproven etymology), and "raging brute" used the word the renderings table keeps clear of | "λύσσα ‘wild frenzy’ … ‘frenzied brute’" |
| 302 | i | medium | "with this one he missed Hector": "this one" is not in the Greek (τοῦ is "him") and reads as the arrow | "and he missed Hector," |
| 302 | n | medium | same error in the gloss of τοῦ | "‘him indeed he missed’" |
| 312 | n | medium | ἡνιοχῆα called the epic form of ἡνίοχος; it is the accusative of ἡνιοχεύς (-ῆα) | now "accusative of ἡνιοχεύς, an epic by-form of ἡνίοχος" |
| 314 | n | medium | ἤριπε said to be "without the augment"; the η- is the augment | "(the η- is the augment)" |
| 317 | i | low | ἔπειτα dropped (the published English of the same line keeps "then") | "Then he let him be, …" |
| 324 | n | low | κληΐς spelled differently from the text's κληῒς | respelled |
| 328 | n | low | καρπῷ "wrist" stands three lines after καρπῷ "fruit" (307) with no word to the reader | one sentence added saying the wrist is a different word |
| 330 | l, i, n | low | ἀμφεκάλυψε given "covered about / covered"; the table keeps ἀμφικαλύπτω "enfold" (2.262, 3.442) | l "the shield enfolded", i "enfolded him with his shield", n "enfold, cover on all sides" |
| 332 | i | medium | "carried him to the hollow ships, groaning heavily" hangs "groaning" on the carriers; στενάχοντα agrees with τόν (Teucer) | "carried him, groaning heavily, to the hollow ships" |
| 345 | n | medium | κεκλόμενοι called a perfect participle; it is the reduplicated aorist of κέλομαι (gloss.json agrees) | corrected |
| 348 | n | medium | ἀμφιπεριστρώφα called "uncontracted (Attic -ᾱ)": -α is the contracted ending and is Attic too; the real feature is the missing augment | "without the augment (Attic ἀμφιπεριεστρώφα)" |
| 354 | i | low | "for he rages": δέ is not "for" | "while he rages past bearing" |
| 354 | n | low | "(Attic ἔοργεν)" implies a different Attic form; there is none beyond movable ν | removed |
| 358 | l | medium | optative of wish translated "would lose" (potential, no ἄν); note and `i` say wish | "Indeed, quite, may this man at least lose might and life," |
| 360 | n | medium | σχέτλιος and ἀλιτρός called "nouns of reproach"; the first is an adjective, the second adjective or noun | label corrected |
| 364 | i | low | αὐτάρ answering ἤτοι ὃ μέν lost its contrast ("and Zeus") | "but Zeus" |
| 366 | l, i, n | medium | πυλάρταο rendered "gate-closing / gate-closer"; the Odyssey table (11.277, binding here) has "gate-fastener", and the departure was not logged | l "Hades the gate-fastener", i "Hades, the gate-fastener", n "‘gate-fastener’" |
| 370 | l | low | "Achilles, the city-sacker": the table's πτολίπορθος `l` is "city-sacking" (`i` "city-sacker" is kept) | "Achilles the city-sacking." |
| 373 | i | low | "But there will be a time": μάν is "indeed", not "but" | "There will indeed be a time when …" |
| 376 | l | medium | "for us two" renders a dative; νῶϊ is nom./acc. dual (dative νῶϊν, 374) | "whether at us two," |
| 376 | n | medium | note glossed προφανέντε as "we two" without saying how νῶϊ is construed | sentence says νῶϊ goes with προφανέντε, Hector glad at "us two having appeared" |

## Changes to gloss.json (pass 2)

| Key | Sev | What was wrong | What was done |
|---|---|---|---|
| ἡνιοχῆα | medium | lemma ἡνίοχος with "-ῆα (= Attic -έα)" is incoherent; the form is from ἡνιοχεύς | lemma ἡνιοχεύς (by-form of ἡνίοχος) |
| ὑστάτιόν | low | lemma muddled (ὕστατος … ὑστάτιος) | lemma ὑστάτιος, by-form of ὕστατος |
| δύναμίς, στῆθός | low | "accent thrown back before the enclitic": an enclitic adds an acute on the last syllable | "extra accent on the last syllable before the enclitic" |
| πτολίπορθον | low | invented "Attic πολίπορθος" | replaced by the elements (πτόλις = Attic πόλις + πέρθω) |
| προφανέντε | low | "nom." only, against the line's construction | "nom./acc." |

Glosser's flags: κεκλόμενοι (reduplicated aorist of κέλομαι: correct, the unit note was the error, fixed above); πῆχθεν ("aor. pass. 3 pl., unaugmented, -εν for -ησαν": correct as it stands); ἀμφιπεριστρώφα ("unaugmented": correct, the unit note was the error, fixed above). ὑπό: the known entries ὑπ’ (agent genitive at 359 χερσὶν ὑπ’ Ἀργείων; "from under" at 363) and ὑπὸ (+ dat. "under" at 344 Τρώων ὑπὸ χερσίν) already cover every use here; no broadening. ἀγρίου: known entry is "masc./fem. gen. sg." and covers συὸς ἀγρίου; no broadening. Other known forms with unusual uses (ἂν irrealis at 369, ὄφρ’ ἂν at 375, ἦ "or whether" at 379, ἤτοι, ὃ μέν/ὃ δέ, τοῦ in ἐκ τοῦ, τι in οὐδέ τι) were checked and are covered (τοῦ, τι, βάλεν, εἴπῃ, ἀπὸ, ἐμῶν are correctly broadened).

## Findings considered and refused

1. 302–305 ὀπυιομένη "after she was wedded" (present participle): the gloss "being wedded" is exact, but the English "after she was wedded" is an ordinary English reading of a completed marriage; no change.
2. 311 l "for threw-off-course Apollo": clumsy but literal word by word; the unit is a crib line; no change.
3. 320 l "the all-shining one": παμφανόωντος agrees with δίφροιο and `i` has "shining chariot"; l is a literal gloss; no change.
4. 306–308 βαρυνθέν agrees with κάρη, so "he drooped his head, weighed down by the helmet" shifts the participle to the man: the note says so; no change.
5. 297 τανυγλώχινας "γλωχίν": LSJ gives both γλωχίς and γλωχίν; no change.
6. 328 "stood on knee … dropped" / `i` "dropped on his knee and stayed there": sense is sound; no change.
7. 345 `i` "held where they were … standing fast": covers both ἐρητύοντο and μένοντες; no change.
8. 379 `i` omits "even" of ἦ τις καί: the force is carried by "or whether"; no change.
9. 363/40 `i` "labours set by Eurystheus": the "set" is interpretive but harmless and consistent with ὑπό + gen.; no change.
10. ἐρίηρες ἑταῖροι, κάρη κομόωντες, βροτολοιγός, σμερδαλέα ἰάχων, μώνυχες ἵπποι, ὢ πόποι, ἦ ῥα καί, ἐλεαίρω/ἐλεέω, Ἀτρεΐδη κύδιστε, κορυθαίολος: all agree with the table; no change.

## For the drafter or the publisher

- `new-renderings.md` is now out of step with units.json and was not edited by the reviewer: the πυλάρταο row ("gate-closing", "gate-closer") should be dropped, because the table already has πυλάρτης "gate-fastener" (Odyssey 11.277); the πτολίπορθον row should read `l` "Achilles the city-sacking"; the 8.317 row `i` should read "Then he let him be, though he grieved for his companion,"; the ἀμφεκάλυψε use is table-conformant and needs no row.
- The 8.314, 8.316 units are identical in `l` and `i` to the published iliad-047 units; the 8.354 unit keeps the published wording.
