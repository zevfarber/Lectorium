# Review, odyssey-046 (10.76–173)

Severity: **high** = wrong sense or a wrong claim that would mislead a reader of the Greek; **medium** = a false grammatical label, or a stock epithet or formula contradicting a shipped rendering; **low** = wording, cross-reference or house-style slip. `t` was never touched (checked byte for byte against the draft before editing). No quotation marks are needed in this part: it holds no speech (odyssey-045 closes Aeolus’s speech with ’ at 75; unit 53 ends in a colon and the speech it introduces belongs to the next part).

## Pass 1 — changes to units.json (12 field edits in 9 findings)

| # | line | field | severity | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 135 (Circe unit) | l, i, n | medium | ὀλοόφρων rendered “deadly-minded Aeetes” / “Aeetes of the deadly mind”. The same word is shipped at 1.52 (odyssey-001) as “baleful-minded Atlas” in both layers; it is a stock epithet, so the same word gets the same English. `new-renderings.md` justified the change by saying “baleful” was “kept for ὀλοφώια”, but the table’s ὀλοφώια row says “baneful”. | `l` “baleful-minded Aeetes”; `i` “baleful-minded Aeetes”; note now says ‘baleful-minded’ (ὀλοός ‘destructive’, φρήν ‘mind’), “as of Atlas at 1.52”. Also corrected the matching row in `new-renderings.md` (so the wrong row is not copied into the conventions table). |
| 2 | 135 (Circe unit) | n | medium | “ἔναιε is the unaugmented imperfect of ναίω”. ἔναιε is augmented (ἐ- is the syllabic augment; the unaugmented form would be ναῖε). | “ἔναιε is the imperfect of ναίω ‘dwell’ (its ἐ- is the augment)”. |
| 3 | 132 | n | medium | Claimed ἀολλέες “is masculine, so it points at the men aboard” against feminine αἱ ἄλλαι. ἀολλής has one form for masculine and feminine, so nothing can be inferred from its gender. | Rewritten: ἀολλέες has one form for both genders, so it can go with ships or crews and the sentence does not choose. |
| 4 | 97 | n | low | “The line returns at 148 with a comma for its ano teleia.” 97 ends ἀνελθών. with a full stop. | “…a comma for its full stop.” |
| 5 | 148 | n | low | “…except that its ano teleia becomes a comma”: same slip. | “…its full stop becomes a comma.” |
| 6 | 98 | n | low | Backticks round `i` in a note (“Quote Greek bare (no backticks)”; no published note uses them or names the layer). | “the free English puts it in the past”. |
| 7 | 121 | n | low | Same: “supplied in `i`”. | “which the free English supplies”. |
| 8 | 84 | n | low | “ἄργυφα … describes the sheep, and μῆλα is the house ‘flocks’”: the note’s own noun contradicted the house rendering used in `l`/`i`. | “describes the flocks”. |
| 9 | 172 | l, i, n | low | κὰδ δ’ ἔβαλον προπάροιθε νεός rendered “threw … before the ship”; the same words at 9.482 (odyssey-044) are shipped as “cast it down in front of the (…) ship”. Reuse the shipped wording as far as the sentence allows. | `l` “And down I cast it in front of the ship, …”; `i` “I cast it down in front of the ship …”; note “tmesis for ‘cast down’, as at 9.482 of the Cyclops’s stone”. |

Counts, pass 1: 0 high, 3 medium, 6 low.

### Scansion flag, line 106
Scanned by hand (θυγατέρ’ ἰφθίμῃ Λαιστρυγόνος Ἀντιφάταο): –⏑⏑ | –– | –‖– | –⏑⏑ | –⏑⏑ | –×. Foot 1 needs the first syllable of θυγατέρ’ long (θυ- is short by nature); foot 2 ἰφ-θί is long by position and by nature; the final -αο of Ἀντιφάταο is long before the end of the line as in the other genitives in -αο. The irregularity is real (metrical lengthening, not a mis-parse; the accusative θυγατέρα would be worse: hiatus and a short closed syllable). The unit’s note already says in one plain sentence that the line is metrically irregular as transmitted and where. No change.

### Checked and found true (no change needed)
Every cross-reference was checked against the source and the neighbouring parts: 10.25, 10.27, 10.28, 10.44–47, 9.62–63, 9.88–90 (= 10.100–102), 9.75 (= 10.143), 9.489 (= 10.129), 5.390 (= 10.144), 5.474/6.145 (δοάσσατο), 9.32, 9.187, 7.206, 4.846, 1.2 and the in-part references (91/95, 97/148, 99/117, 100–102/117, 101/109, 107/109, 114/116, 95–96/125–127, 133/132, 138–139/137). Every “ends at the ano teleia / full stop in the middle of line N” claim was checked against the printed punctuation. Reused-line English matches the shipped units (10.77, 100–102, 129, 133–134, 143, 144), and the two whole-unit repeats (133–134) are identical to 9.62–63. `l` keeps the line division of `t` in all 54 units; `i` has no newlines; ¶ marks fall on 76 and 133 only.

### Findings considered and refused
- **ὁρῶμεν (99) is present in `l` (“we see”), past in `i` (“we saw”).** Refused: the note already says the Greek tense and plural are odd in context and that `i` puts it in the past; a present in `i` would read as a change of narrative time with nothing to explain it.
- **θυμός (163) rendered “life”, not the house “heart”.** Refused: it is not an epithet; the note says why once (what leaves the body at death), and the table’s own θυμός rows (“heart”) are about the seat of feeling. Reported below as a glossary gap instead.
- **ἀνδραχθέσι “as heavy as a man could carry” (121) might be a remembered phrase.** Refused: it is the lexicon gloss (Autenrieth) of ἄνηρ + ἄχθος rebuilt from the word; `l` keeps “man-burdening” so the build is visible.
- **θυμὸς ἀνδρῶν (78), singular in `l` (“the heart”), plural in `i` (“hearts”).** Refused: a distributive singular; the note says “one heart for the whole crew”.
- **ἐπέφραδεν (111) is called an aorist of ἐπιφράζω in the note but lemmatised under φράζω in the glossary.** Refused: both are LSJ-recognised; no reader is misled.
- **“with one hand” (170–171) drops ἑτέρῃ “the other” in `i`.** Refused: sense kept; the note and `l` say “the other hand”.
- **“πλῆξα … the aorist of πλήσσω” (161) could say “unaugmented”.** Refused: harmless omission.

## Pass 2 — edited units.json, and gloss.json

Re-read every unit as edited: the 12 edits agree with each other (note ↔ `l`/`i`), `t` is unchanged, 54 units, no ASCII apostrophes or backticks, no “ ” in `l`/`i`, typographic ’ throughout, cross-references from the edits verified (1.52 ὀλοόφρονος Ἄτλαντος; 9.482 κὰδ δ’ ἔβαλε προπάροιθε νεὸς κυανοπρῴροιο). No new error found in the units on the second pass.

`gloss.json` (143 novel forms, all present; 18 `__broaden__` entries, each beginning with the old entry whole followed by ` · `; no entry over 229 characters, no ASCII quotes, no line numbers or “here”) was read against the lines. **Not edited** (the glosser owns the file); findings for whoever merges it:

| # | key | severity | problem | suggested fix |
|---|---|---|---|---|
| G1 | θυγατέρ | medium | Parsed “fem. acc. sg., elided (θυγατέρ’ = θυγατέρα)”. In 106 θυγατέρ’ is in apposition to the dative κούρῃ and stands beside the dative ἰφθίμῃ; the unit’s note reads it as the dative θυγατέρι with its ι elided. The glossary entry contradicts the note and `l`. | “θυγάτηρ — daughter; fem. dat. sg., elided (θυγατέρ’ = θυγατέρι); also acc. sg., elided (θυγατέρ’ = θυγατέρα)” — dat. first. |
| G2 | ἰφθίμῃ (`__broaden__`) | medium | The added reading says “qualifying θυγατέρ’ (an acc. noun; agreement would need ἰφθίμην)”: wrong for the same reason, and it pins the entry to a line. | Replace the added reading with “also ἴφθιμος — mighty, stout; adj., fem. dat. sg.” |
| G3 | θυμός (nom. sg.; no `__broaden__` entry) | low | Existing entry “heart, spirit”; 163 ἀπὸ δ’ ἔπτατο θυμός uses it of the life that leaves the body, and the unit’s `i` says “life”. The runbook asks that a known form’s entry cover its use. | Broaden `θυμός`: old entry whole + “ · also the life-force that leaves the body at death: ’and his life flew away’ (ἀπὸ δ’ ἔπτατο θυμός)”. |
| G4 | φαεσιμβρότου | low | “epic -ου”: -ου is the ordinary 2nd-declension genitive, not an epic ending. | Drop “epic”. |
| G5 | ἔγχει | low | “neut. dat. sg.: ’on his spear’”: pins the entry to a line and the speaker is “I”. | “spear; neut. dat. sg.” (or “’with a spear’”). |

Counts, pass 2: units 0 new findings; gloss 0 high, 2 medium, 3 low (all unedited).

## Totals
Edited in units.json: 0 high, 3 medium, 6 low. Reported for gloss.json (not edited): 0 high, 2 medium, 3 low. Refused: 7. Scansion: line 106 confirmed irregular, note already present.
