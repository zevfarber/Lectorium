# Review of iliad-027 (Iliad 5.1–110), reviewer, two passes

Edited in place by script: `units.json` (never `t`; checked unit for unit that every `t` is unchanged, and the build's tiling/ln/p checks still pass) and `new-renderings.md` (kept consistent with the units). `gloss.json` was neither read nor touched; the glosser's parses are for the reviewer's second pass at the gate, not part of this review.

Method. Pass 1: every note against its own line and unit (labels, positions, cross-references checked against the source files and the published parts), then Greek to `l` word by word, `l` against `i`, `i` for remembered English, quotation marks. Pass 2: the whole of `units.json` again from the Greek, plus mechanical checks (tiling and `ln`/`p` by the build's own logic; every row of `new-renderings.md` tested against the units' `l`/`i` text; straight quotes, double spaces; every cross-reference "line N", "N.M", "Odyssey N.M" looked up in the source JSON and the published JSON).

Counts of edits: high 0, medium 14, low 11 (25 edits in all; the three edits at 5.38 and the two at 5.84 and 5.101 are each one finding).

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 5.14 | n | medium | Said 3.15 is where "Paris and Menelaus close on each other"; in 3.15 it is the two armies that close (Paris steps out only in 3.16). | "the two armies". |
| 5.16 | n | medium | "ἤλυθε is an unaugmented ἦλθε": ἤλυθε carries the augment (the epic form of ἦλθε). | "the epic aorist of ἔρχομαι, Attic ἦλθε" (as iliad-018 and iliad-020 say). |
| 5.31 | n | medium | χαζώμεσθα, ἀλεώμεθα called "short-vowel subjunctives": both have the long vowel ω. The note also glossed them "let us draw back / avoid", against `l`/`i` ("we two draw back … and avoid"). | Now "subjunctives (the vowel is long, ω) continuing the question, ‘and we two draw back and avoid …?’". Row in new-renderings.md changed to match. |
| 5.38 | l, i, n | low | "and first lord of men Agamemnon" can be read with "first lord of men" as a title; the note called ἀρχόν and Ὀδίον μέγαν "both objects", but ἀρχόν is in apposition to Ὀδίον. | `l` "and first, lord of men Agamemnon"; `i` "and first Agamemnon, lord of men, threw great Odius, …"; note says apposition, one object. |
| 5.40 | n | medium | "line 41 is the same line as 57 below (which is also Odyssey 22.91)": 41 ends ἔλασσε, 57 ends ἔλασσεν (movable ν); and the Odyssey line is 22.93 (the Odyssey unit is listed "at line 91" because it begins there; the ὤμων line is its third line, 93, checked in `odyssey-murray1919.json`). | Note now says the same except for the movable ν, and Odyssey 22.93. |
| 5.47 | n | medium | ἤριπε called "unaugmented"; ἤριπε is the augmented aorist (ἔριπε is the unaugmented one, as at 68). | "the aorist of ἐρείπω". |
| 5.55–58 | n | medium | "Line 57 is the same as Odyssey 22.91": it is 22.93. | Corrected. |
| 5.62–64 | n | medium | "the accent-shifted ἐκ following its noun": ἐκ is monosyllabic and does not shift its accent (no anastrophe). | "ἐκ placed after its noun θεῶν". |
| 5.62–64 | n | low | οἷ τ’ αὐτῷ "the reflexive οἷ" with no referent; in the English a reader takes "himself" for Alexander, but it is Phereclus (the next clause is about his ignorance). | Referent stated. |
| 5.66 | n | medium | ἤλυθ’ called "the unaugmented ἦλθε" (augmented, see 5.16). | "the epic aorist ἤλυθε, Attic ἦλθε". |
| 5.66 | l | medium | `l` "straight under the bladder": κατά + acc. is not "under", the note and `i` say "through", and the row in new-renderings.md already read "through the bladder". | `l` "straight through the bladder, below the bone". |
| 5.68 | n | medium | ἀμφεκάλυψε called an "unaugmented aorist"; the augment stands after ἀμφι-. | "the aorist of ἀμφικαλύπτω". |
| 5.69 | n | medium | ἔτρεφε called an "unaugmented imperfect"; ἔ- is the augment. | "the imperfect of τρέφω". |
| 5.79 | n | medium | ἔξεσε called "the unaugmented aorist of ἐκξέω": no such verb (the preverb is ἀπό) and ἔ- is the augment. | "the aorist of ξέω ‘scrape, hew’, which with ἀπό … is ‘hew off’". |
| 5.79 | n | low | Packet flag: scanned by hand (see below); the irregularity is real. | One sentence added: the line is metrically irregular as transmitted, the last syllable of Εὐρύπυλος short in a long place at the main caesura before the vowel of Εὐαίμονος (the same sentence iliad-014 has for 2.736). |
| 5.82 | l | low | κατά dropped in `l` ("over the eyes"); the note and `i` say "down over". | "down over the eyes". |
| 5.84 | l, i | low | "in the strong battle": the table's row for κρατερὴ ὑσμίνη is "in strong battle" (4.462), and the note quotes ‘in strong battle’. | Article dropped in both. |
| 5.101 | i | medium | "shouted loudly" in `i`; the house `i` for μακρὸν ἄϋσεν (iliad-016, 3.81) is "cried out loudly" (the `l` is "shouted loudly"). The row claimed to follow iliad-016. | `i` "cried out loudly"; row corrected. |
| 5.101 | l | low | Order "loudly shouted" against the house `l` "shouted loudly". | "shouted loudly". |
| 5.103 | n | low | Gave "I do not say that he will endure" for οὐδέ ἕ φημι, while `l`/`i` say "I do not think". | Note now gives the literal and the idiom. |
| 5.106 | n | medium | ἔφατ’ called "the unaugmented ἔφατο" (the ἔ- is the augment; φάτο is the unaugmented form, as iliad-007 and iliad-026 say). | "ἔφατ’ is ἔφατο, the elided past middle of φημί". |
| about | about | low | "so that the old man is not left childless": the Greek says only that he should not be wholly grieved (ἀκαχήμενος); childlessness is added. | "not wholly grieved". |

`new-renderings.md` rows changed to agree with the units: ὕστερος ὄρνυτο (`l` "later, rushed on …"); χαζώμεσθα · ἀλεώμεθα (`l` "draw back"); θεῶν ἐκ θέσφατα (`l` "he knew nothing of the prophecies from the gods"); γνὺξ δ’ ἔριπ’ (`l` "on his knees he crashed down, wailing"); ποτέροισι (`i` "which side … was on"); μίμνον ("stand against", both layers); μακρὸν ἄϋσε (`i` "cried out loudly"). A mechanical test of every row's quoted `l`/`i` against the units now finds only one deliberate difference (ἀΐξας, merged into "rushing after him", already marked in the row).

## 5.79, the flagged line

τὸν μὲν ἄρ’ Εὐρύπυλος, Εὐαίμονος ἀγλαὸς υἱός: scanned by hand, 16 syllables: τὸν μὲν ἄρ’ (– ⏑ ⏑) | Εὐ-ρύ-πυ (– ⏑ ⏑) | λος Εὐ (– –) | αἱ-μο-νος (– ⏑ ⏑) | ἀγ-λα-ὸς (– ⏑ ⏑) | υἱ-ός (– ×). The third foot is a spondee whose first long is the closed short syllable -λος before the vowel of Εὐ-; nothing in the word makes it long, so the line is irregular as transmitted, at the main caesura. The scanner's "AMBIGUOUS" is only the two short υ's of Εὐρύπυλος (either could be taken long at the same cost); the licence is the same either way. The sentence was added to the unit's note.

## Findings considered and refused

- **5.14 / 5.42 / 5.57 repeated lines.** All three agree with the published English (5.14 `i` word for word with iliad-016; 5.42 and 5.57 reuse the published wording). No change.
- **5.22–24 `l` leaves οἱ (and δή) unrendered.** The note and the row both say οἱ is left unspoken on purpose (its reference is not settled). Kept.
- **5.48 ἐσύλευον "were stripping" in `l`, "stripped" in `i`; 5.65 κατέμαρπτε "was overtaking" / "overtook", βεβλήκει "had struck" / "struck".** The shift is declared in the rows and the notes and reads naturally; the pluperfect is noted as a plain past. Kept.
- **5.93 ὑπὸ Τυδεΐδῃ "under" in `l`, "before" in `i`.** The note explains "at his hands"; the English "before" is a fair rendering of a rout. Kept.
- **5.13/5.19/5.107 ἵπποιιν, ἵππων "horses" for the chariot.** Literal in both layers with the note saying what it stands for, as the row records. Kept.
- **5.20 Μῄονος read as "the Maeonian" with Βώρου.** The note states the reading and the row records the rejected alternative; iliad-015 has Μῄονας as the people. Kept. "A place named only here" (Τάρνη) checked: it occurs only at 5.44 in the Iliad and not in the Odyssey.
- **5.36 ἠϊόεντι "high-banked".** New row and a note that says it is uncertain. Kept.
- **5.31 "optative with ἄν as a polite suggestion" for οὐκ ἂν … ἐάσαιμεν.** A defensible label. Kept.
- **5.52 "So he declared aloud" against `l` "So he spoke, declaring".** Departure from the prayer-closing row is argued in the row and note (εὔχομαι "declare" is the Odyssey house sense); "aloud" is the drafter's gloss on a loud claim. Kept.
- **5.69 `i` "to please her husband", 5.75 "taking the cold bronze in his teeth".** Read against the Greek (χαριζομένη πόσεϊ ᾧ; ἕλε … ὀδοῦσιν); the rows list the rejected stronger readings ("bit"). Kept.
- **5.26 "χραῖσμ’ is the aorist ἔχραισμε".** Loose (the form is the unaugmented χραῖσμε) but not false as a statement of which verb-form it stands for. Kept.
- **Remembered English.** Searched `i` for phrases that arrive ready-made: "ruin of mortals", "blood-stained", "goaders of horses", "my good fellow" are the table's own wordings; nothing else found.
- **Quotation marks.** Three speeches (5.31–34, 5.102–105, 5.109–110): “ on the first unit, ” on the last, `mark` on the first, in both `l` and `i`; none inside other units. Neighbouring part: the last unit of iliad-026 (4.539–543) is narrative; its last `mark` (509) is closed. 5.110 ends Diomedes' speech (5.111 is ὣς ἔφατ’), so no speech runs into the next part. All correct.
- **Mechanical.** Tiling, `ln`, `p` (paragraph marks at 1, 9, 35, 43, 48, 59, 69, 76, 84, 95, 106), `l`/`t` line counts, no straight quotes, no double spaces: all pass.

## Notable

No `high` findings. The recurring fault was wrong augment labels (seven notes: ἤλυθε ×2, ἤριπε, ἀμφεκάλυψε, ἔτρεφε, ἔξεσε, ἔφατ’). Every Odyssey/Iliad cross-reference was looked up; two were wrong (Odyssey 22.91 should be 22.93; "Paris and Menelaus" at 3.15).

## Glossary pass

Scope: all 230 new entries and 20 "__broaden__" entries of gloss.json, each read against every line in units.json where the form occurs; format checks by script (length under 230, no line numbers, no ASCII apostrophe or backtick, no "here", every broadened entry begins with the old entry whole).

Counts by severity: major 0 · moderate 3 · minor 5 · refused 7.

### Changes (form · severity · was · now)

- ἀλεώμεθα · moderate · was: ἀλέομαι — avoid, shun, flee from; aor. subj. 1 pl. mid., short-vowel, deliberative: ’are we to avoid?’ · now: ἀλέομαι — avoid, shun, flee from; subj. 1 pl. mid., long-vowel (-ω-), pres. or aor. stem not certain, deliberative: ’are we to avoid?’
- οὔτασε · moderate · was: οὐτάω — wound (by a thrust), stab; aor. 3 sg. act., unaugmented · now: οὐτάω — wound (by a thrust), stab; aor. 3 sg. act.
- βάλλειν · minor · was: βάλλω — throw, hit, strike; pres. inf. act., epexegetic after an adjective of skill: ’to strike’ · now: βάλλω — throw, hit, strike; pres. inf. act., complementary after a verb of teaching or skill: ’to strike’
- ἔριπ · minor · was: ἐρείπω — throw down; intrans. aor., fall, crash down; aor. 3 sg., elided (ἔριπ’ = ἔριπε), unaugmented (= Attic ἤριπε) · now: ἐρείπω — throw down; intrans. aor., fall, crash down; aor. 3 sg., elided (ἔριπ’ = ἔριπε), unaugmented (cf. augmented ἤριπε)
- ἔπτατο · minor · was: πέτομαι — fly; aor. 3 sg. mid., epic (= Attic ἐπτάτο): ’flew’ · now: πέτομαι — fly; aor. 3 sg. mid., epic (Attic ἐπτόμην): ’flew’
- τάρνης · minor · was: Τάρνη — Tarne, a city of Maeonia; fem. gen. sg., epic -ης (= Attic Τάρνης) · now: Τάρνη — Tarne, a city of Maeonia; fem. gen. sg.
- ἐτέτυκτο · minor · was: τεύχω — make, contrive, bring about; pass. come to pass, happen; plup. pass. 3 sg. with impf. sense: ’had been made, had come about’ · now: τεύχω — make, contrive, bring about; pass. come to pass, happen; plup. pass. 3 sg.: ’had been made, had come about’
- κάλ (broaden) · moderate · was: καλός — fair, fine, goodly; neut. acc. pl., elided (κάλ’ = καλά), agreeing with τεύχεα: ’fine (armour)’ · also agreeing with σφυρά: ’fair (ankles)’ · also agreeing with ἔργα: ’fine (works)’ · now: καλός — fair, fine, goodly; neut. acc. pl., elided (κάλ’ = καλά), agreeing with τεύχεα: ’fine (armour)’ · also agreeing with σφυρά: ’fair (ankles)’ · also neut. nom. pl., agreeing with ἔργα: ’fine (works)’

### Reasons
- ἀλεώμεθα: the form has long ω, so "short-vowel" was false (and the unit note itself says the vowel is long). Whether the stem is present or aorist is not settled by the form, so the entry now says so; subjunctive, 1 pl., middle, deliberative stands.
- κάλ’ (broadened): the added reading is attached to ἔργα, which is the nominative subject of κατήριπε; the added clause said "acc. pl." by inheritance from the old reading. Now "neut. nom. pl.". Old entry unchanged.
- οὔτασε: οὐ- is a diphthong that the augment leaves unchanged, so "unaugmented" cannot be asserted from the form.
- βάλλειν: the infinitive depends on δίδαξε ("taught to strike"), not on an adjective; the old wording named a construction the line does not have.
- ἔριπ’: ἤριπε is Homeric, not Attic; the "Attic" label was wrong, now a plain cross-reference to the augmented form.
- ἔπτατο: "Attic ἐπτάτο" is not an Attic form; Attic aorist is ἐπτόμην. (The Odyssey glossary carries the same slip; it is not touched.)
- Τάρνης: ν precedes η, so Attic keeps -ης; "epic -ης (= Attic Τάρνης)" claimed a difference that does not exist.
- ἐτέτυκτο: "with impf. sense" contradicted the gloss "had been made" and the unit note.

### Considered and refused
- ἀστέρ’: dative ἀστέρι with elided ι (object of ἐναλίγκιον, agreeing with ὀπωρινῷ), as the unit note says; entry right.
- μάρνασθ’: infinitive μάρνασθαι elided, after ἐάσαιμεν; entry right.
- νύξ: the line has νύξ’ = elided νύξε (νύσσω); the "night" reading is not used in this part, but the key νύξ is a true homograph of the printed form (the Odyssey glossary has the same pair and the Iliad glossary has only the grave νὺξ), so both readings stay.
- ἄροιτο: entry gives ἄρνυμαι (as the Odyssey glossary does); the unit note says αἴρομαι. Not changed here (units.json is final and the Odyssey entry stands); flagged for the owner as a note/glossary lemma mismatch, same word, no difference in meaning or parse.
- οἷ: both readings stay; the line uses the orthotone dative pronoun (reflexive, per the note), the οἷος reading is the standing homograph shared with the Odyssey entry.
- μεταμάζιον: the "agreeing with or standing beside στῆθος" hedge is honest (adjective or adverb use is not settled by the line); left.
- ᾗσιν (broadened): the relative reading ("in which", after ἑκηβολίαι) is correct for the line; the old possessive reading is kept whole.
