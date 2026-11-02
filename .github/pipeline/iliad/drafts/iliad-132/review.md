# iliad-132 (Iliad 21.1–96) — review

Two passes over `units.json` (50 units). `t` was not touched: it was checked against the packet's lines 1–96 (identical apart from line division), and the edited file was re-compared to the original unit by unit. `l` keeps the line division of `t` in every unit; `ln`, `p` (paragraph marks at 1, 17, 34, 64), `mark` (54, 74), the opening “ and closing ” on both speeches (54–63, 74–96) and the full coverage of lines 1–96 were checked and are right. Neither neighbouring part leaves a speech open (iliad-131 ends in narrative at 20.503; the speech that opens at 21.74 closes at 21.96, before iliad-133).

Pass 1: notes (labels, line references, claims about position), then Greek → `l`, `l` ↔ `i`, remembered English, quotation marks. Pass 2: re-read of every changed unit, a mechanical check that every Greek form quoted in a note is either in that unit's `t` or a lemma/ending named as such, and a re-check of every edit against the house tables (`conventions.md`, `../odyssey/conventions.md`). `gloss.json` is not yet reviewed (second pass on it is pending).

## Changes (line · field · severity · what was wrong · what done)

| line | field | severity | what was wrong | what done |
|---|---|---|---|---|
| 3 | n | low | Note said φοβέοντο ‘were fleeing’ while `l`/`i` say “had fled” (the day is past), so note and `l` disagreed. | Note now glosses φοβέοντο ‘fled’. |
| 7 | l, i, n | medium | ῥέεθρα rendered “channels”; the house table fixes ῥέεθρα as “streams” (2.461, 8.369 “the steep streams”, 17.749). | “the steep streams resounded” / “roared”; note gloss ‘the streams’. |
| 10 | l, n | medium | ἔνθα καὶ ἔνθα rendered “this way and that” in `l`; the Odyssey table fixes `l` “here and there”, `i` “this way and that” (20.24). | `l` now “swam here and there”; `i` unchanged; note gloss follows `l`. |
| 12 | n | low | Note added a picture the Greek does not give (“a rush of fire through dry grass”). | Replaced with a statement drawn from the Greek only. |
| 15 | n | medium | Note claimed Ἀχιλλῆος “has the single λ of the metre”; the line prints the double-λ form (the single-λ form is Ἀχιλῆος, as at 1.1; Ἀχιλεῦ at 74 is the single-λ one). False claim about the line. | Claim removed. |
| 17 | n | low | Packet flag, line 18 (see "Flagged lines" below): irregularity is real but the note was silent. | One sentence added to the note. |
| 25 | l, i | medium | ῥέεθρα “channels” again (see line 7). | “along the streams of the dread river” in both layers. |
| 49 | l | medium | `l` read “Him then, as noticed swift-footed, heavenly Achilles”, dropping “he”; the table's τὸν δ’ ὡς οὖν ἐνόησε is “Him then as he noticed, [Name],” (3.21, 3.30, 5.95). | `l` now “Him then, as he noticed, swift-footed, heavenly Achilles,”. |
| 55 | n | medium | Note said ὕπο in φυγὼν ὕπο νηλεὲς ἦμαρ “has ὕπο after its noun”; it stands after the participle and before the noun. Wrong claim about word position. | Note now says it is a tmesis of ὑποφυγών (ὕπο apart from the participle), ‘escaping the pitiless day’. |
| 60 | l, i, n | medium | ἀκωκή rendered “point”; the Iliad table fixes ἀκωκή “tip” (11.253, 16.323 “the tip of the spear”) and keeps “point” for αἰχμή. | “the spear’s tip” / “the tip of my spear”; note gloss ‘the tip of the spear’. |
| 67 | l, i | medium | ἤτοι ὃ μέν … ὃ δέ rendered “Indeed he, on the one hand” / “Now …”; the table (11.338, 11.373) gives “He then, for his part” / “For his part” and turns “Indeed” down. | `l` “He then, for his part, a long spear held up, …”; `i` “For his part, heavenly Achilles held up his long spear, …”. |
| 71 | n | low | Note said λάβε γούνων stood “two lines earlier”; it is in line 68, three lines before 71. | “three lines earlier (line 68)”. |
| 83 | l, n | low | “Father Zeus” capitalised for the dative Διὶ πατρί; the table has “father Zeus” (3.350) and keeps “Father Zeus” for the vocative. | “father Zeus” in `l` and in the note. |
| 88 | n | low | (a) Packet flag, line 88 (see below): irregularity real, note silent. (b) Note said Lycaon tells Achilles “Priam had many sons by many women”; the Greek says only that Priam had many other wives. | (a) One sentence added. (b) Reworded to “had many wives, which prepares the point …”. |
| 89 | l | low | δειροτομήσεις given in the Odyssey's hyphenated form “cut-the-throat-of”; the Iliad table's ἀποδειροτομήσω (18.336) is “cut the throats of” and the unit's own `i` already says so. | `l` now “both you will cut the throats of”. |

Counts by severity (table rows): high 0 · medium 8 (lines 7, 10, 15, 25, 49, 55, 60, 67) · low 7 (lines 3, 12, 17, 71, 83, 88, 89). 15 units changed, 23 field edits; `t` untouched.

## Flagged lines (hand scan)

- **Line 18** `κεκλιμένον μυρίκῃσιν, ὃ δ’ ἔσθορε δαίμονι ἶσος` (17 syllables). It scans only as κεκλι·μέ | νον μυ·ρί | κῃ·σιν ὃ | ἔσ·θο·ρε | δαί·μο·νι | ἶ·σος, which needs both μυ and ρί short. The scansion table counts the υ of μυρίκη long (iliad-062, line 466, was noted in the same terms), so the line is irregular as the table reads it. Real; sentence added to the note of the unit at line 17.
- **Line 88** `τοῦ δ’ ἔχε θυγατέρα Πρίαμος, πολλὰς δὲ καὶ ἄλλας` (16 syllables). Scans as τοῦ δ’ ἔ·χε | θῡ·γα·τέ | ρα Πρί·α | μος πολ | λὰς δὲ καὶ | ἄλ·λας, with θυ lengthened as the long of foot 2 and καὶ shortened before ἄλλας. The lengthening of θυγατέρα is the same licence the earlier parts record as irregular (iliad-012, -037, -069, -081, -093); sentence added in the same terms.

## Findings considered and refused

- **21.73** “to him” against the Greek equal to published 1.201 (“to her”): decided by the owner and recorded in `new-renderings.md` (as at 2.7, 4.312, 4.369, 8.101); the note already says μιν is Achilles here. Left.
- **21.70 “flesh” for χροός**: the Iliad table keeps “skin” for χρώς in a surface sense (4.237) but 11.574 gives χροὸς ἆσαι “flesh”; this is the same phrase, so “flesh” stands. Left.
- **21.70 “sated” (`l`) for ἄμεναι**: the table renders the same stem in ἆσαι “glut” (5.289, 11.574), so “glut” in `l` would be closer; but the drafter registered “sated” in `new-renderings.md` and `i` already says “glut”. Left, flagged for the owner as a possible harmonisation.
- **21.55 `l` “seeing how” for οἷον δή**: slightly participial, but it matches the `i` (“see how”) and the note calls it an exclamation. Left.
- **21.10 `i` “with a great outcry”** (ἀλαλητῷ has no “great”): a free-layer intensifier, not a change of sense. Left.
- **21.88 `l` “His daughter Priam had, and many, too, others”**: awkward but follows the Greek order; ἔχε “had” (to wife) is explained in the note. Left.
- **21.83 `i` “I must be hateful”** for μέλλω: `l` keeps “I am destined … to become hateful”; “must” is a fair free rendering of the inference. Left.
- **21.54 `i`** keeps “my own eyes” where the Greek has no “own”: it reuses the published 13.99 wording, as the packet requires. Left.
- **Quotation marks**: no problems found; none refused.
- **Remembered English**: nothing in `i` read as a recalled translation; the phrases that came closest (“eager to glut itself on human flesh”, “the black spirit of death”) are house-table renderings, not memory.

## Gloss pass (`gloss.json`)

Every one of the 99 novel entries was checked against the form and the way it is used in `units.json`, and against the format rules (lemma, parse, Attic equivalent for Homeric forms, no line numbers, no "here", typographic ’ only, under 230 characters). The key set equals `novel-forms.json` exactly. All 12 `__broaden__` entries start with the old `known-forms.json` entry whole and add a reading that the part really uses. The remaining known forms occurring in the part were read against their entries to find uses not yet covered. The glosser's eight uncertain parses are settled below.

### Changes (key · severity · what was wrong · what done)

| key | severity | what was wrong | what done |
|---|---|---|---|
| κελάδων | medium | Called an "uncontracted" form of the Attic κελαδῶν; the accent (κελάδων, not κελαδέων) shows an epic barytone present, so the stated Attic equivalent and the "uncontracted" label were false. | Parse reworded: epic, accent of a barytone verb, contracted Attic participle is κελαδῶν. |
| ἔπεφνον | none | Lemma θείνω looked wrong (the root is φένω), but `known-forms.json` already records ἔπεφνεν as "used as aorist of θείνω". | Refused: kept, so that the glossary stays consistent. |
| ἀκωκῆς | medium | "Ionic -ῆς (= Attic -ᾶς)" is false: ἀκωκή is an η-stem in Attic too and has the same genitive. Also glossed "of the point" against the house "tip". | Attic equivalence removed; meaning order kept; example ’of the tip’; object relation named as partitive object of γεύω. |
| μεγακήτεος | medium | "Huge, with great gulfs" asserted an etymology; the house table and the unit note say probably μέγα- + κῆτος "sea-monster", formation not secure. | Meaning now "huge (probably μέγα- + κῆτος ’sea-monster’, but the formation is not certain)". |
| ἔννεον | medium | "unaugmented in form" is wrong: ἔννεον is augmented, with the ν doubled for the metre. | Now "epic doubled ν (= Attic ἔνεον)". |
| ἕκτορός | medium | "accent thrown back before enclitic εἰμι" is wrong (an enclitic gives the preceding word an extra acute, nothing is thrown back), and "gen. after ὁμογάστριος" pinned the form to its line. | Now "with the extra accent of a following enclitic: ’of Hector’". |
| ἀνώϊστον | low | "neut. nom. sg." claimed a case that the form (nom. or acc.) does not fix. | Now "neut. nom./acc. sg." with the ἀ- + οἴομαι derivation. |
| ἐτέρπετο | low | "with acc. of respect" disagrees with the unit note (θυμόν is the object of a middle verb) and pins the entry to a line. | Dropped; now "impf. 3 sg. mid., augmented: ’delighted’". |
| τεθηπότας | low | "epic -ότας" is not an epic peculiarity (ordinary perfect participle ending). | Removed. |
| ἄνευθεν (broaden) | low | Known entry gives only the adverb; the part uses it with the genitive (away from my father). | Added "also prep. + gen." reading. |
| ὕπο (broaden) | medium | Known entry has no tmesis reading; φυγὼν ὕπο νηλεὲς ἦμαρ is ὑποφυγών with ὕπο after the participle, which is also what the unit note now says. | Added the tmesis reading. |
| κτεῖν (broaden) | medium | Known entry gives only aor. 3 sg. (= ἔκτεινε); the part has the present imperative κτεῖν’ = κτεῖνε after μή. | Added the imperative reading. |
| ἔπεσον (broaden) | low | Known entry mentions tmesis with σύν only; ἐν δ’ ἔπεσον is tmesis with ἐν. | Added that reading. |

Counts: 0 high · 7 medium (κελάδων, ἀκωκῆς, μεγακήτεος, ἔννεον, ἕκτορός, ὕπο, κτεῖν) · 5 low (ἀνώϊστον, ἐτέρπετο, τεθηπότας, ἄνευθεν, ἔπεσον). 12 gloss.json entries changed or added (8 novel entries reworded, 4 `__broaden__` entries added, making 16 broaden keys); 1 finding refused (ἔπεφνον).

### The glosser's uncertain parses

- **πίτνα** correct: imperfect 3 sg. of πίτνημι (= πετάννυμι), unaugmented. Kept.
- **κελάδων** see table; fixed.
- **πεφυζότες** correct as a perfect active participle, masc. nom. pl.; the lemma is a verb formed on φύζα and is hedged as such in the entry. Kept.
- **τεθηπότας / τεθηπώς** correct: perfect participle of τέθηπα (aor. ταφεῖν) in the acc. pl. and nom. sg. Kept; the stray "epic" label removed.
- **ἄμεναι** accepted as the epic aorist infinitive of ἄω = Attic ἆσαι, with the genitive (χροός). Kept.
- **λύμην** accepted as athematic aorist middle 1 sg., unaugmented; the "passive in sense" label stays since the unit renders it "I was ransomed". Kept.
- **ἀνώϊστον** case made general (see table).
- **ἕκτορός** see table; fixed.

### Left alone and considered

- λῆμνον's broadened entry is exactly 230 characters; the 230 limit is for novel entries, and several older broadened entries are far longer.
- The agreement notes ("agreeing with …") in novel entries name the nearby word; this is how the existing known entries are written, so they were not treated as line-pinning.
