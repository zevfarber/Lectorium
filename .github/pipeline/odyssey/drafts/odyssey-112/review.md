# odyssey-112 (23.97–182) — review

## Pass 1

Method: conventions.md (prose sections in full; the house-renderings table checked by word against every Greek word of the part), runbook section 2, packet, new-renderings, units.json, odyssey-111.json (last unit). No translation consulted. Edits made to units.json by script (`scratchpad/edit112.py`), fields `n`, `i`, `l` only; every `t` verified byte-identical before and after. 14 units changed.

Checked and found sound: all 12 paragraph marks (`p`) against the packet's ¶ list; every `ln`; all quotation marks (16 open/close marks, balanced, same in `l` and `i`; opens on units 1, 5, 9, 17, 21, 30, 39, 44 with a `mark` on each; closes on units 3, 7, 15, 19, 25, 31, 42, 46); unit 48 (181b–182) carries no closing mark and neighbouring odyssey-111's last unit carries no opening one (Telemachus's speech in 112 opens at unit 1, and 111's last unit says so); `l` and `t` have equal line counts everywhere; no `\n` in any `i`; published repeated lines (23.104, 112, 123, 129, 141, 152, 155, 157–161, 164, 173) agree with the packet's `l`/`i`; all notes' cross-references (100–102/168–170, 103/172, 114/181, 122/131, 129, 166/174, 171/177, 177/181) and "falls in the middle of line N" claims checked against the lines; the four new renderings agree with new-renderings.md in `l`, `i` and note; house-table rows for ἄνωγα, ὄχ’ ἄριστα, κεδνὰ ἰδυῖα, ὀχθήσας, πηός, πολύμνηστος, γυναικῶν θηλυτεράων, δαιμονίη/δαιμόνιε, φόρμιγξ λίγεια/γλαφυρή, κακὰ χροῒ εἵματα, ῥήγεα σιγαλόεντα, κάτθετε εὐνήν, πυκινὸν λέχος, ἐϋσταθής, δολιχηρέτμοισι, τετληότι θυμῷ, πατρίδα γαῖαν all honoured.

Scansion: the packet flags none. I also ran the scanner: every line fits; seven lines (102, 126, 134, 145, 170, 176, 177) carry the plain note "spondaic fifth", a regular feature of the hexameter, not an irregularity; no note added.

### Changes

| Line · unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 100 · "οὐ μέν κ’ ἄλλη γ’ ὧδε" | n | medium | Note called οἱ an ethic dative "for him", fixing its referent as the husband; the pronoun in ὅς οἱ … ἔλθοι can point to the husband (reflexive) or to the wife, and the Greek does not say which. | Reworded: "a dative of interest, which English drops; whom it points to (the husband himself, or the wife) the Greek leaves open." `l` unchanged (its "for him" is the word-for-word rendering). |
| 168 · same three lines repeated | n | medium | Same claim as 100, repeated. | Same rewording, shortened. |
| 105 · "τέκνον ἐμόν, θυμός μοι" | n | medium | "μοι is the dative 'in me'" is a false label: ἐν is carried by ἐνὶ στήθεσσι; μοι is the possessive/interest dative ("my"). | Note now reads: μοι 'my' (a dative of interest), ἐνὶ στήθεσσι 'in the breast'. |
| 114 · "τάχα δὲ φράσεται" | i | medium | "she will see the matter more clearly" adds an object ("the matter") not in the Greek, drifts from `l` "observe, and better", and is the kind of ready-made English the conventions say to rebuild. | `i` → "and soon she will observe better." |
| 114 · same | n | medium | The note quoted 'she will see more clearly' as the first reading the English keeps. | Quoted reading changed to 'she will observe better' to match the new `i`. |
| 115 · "νῦν δ’ ὅττι ῥυπόω" | n | nit | "τοὔνεκ’ is τούτου ἕνεκα": the crasis is of τοῦ ἕνεκα (τοῦ the pronoun-article). | "τοῦ ἕνεκα (τοῦ = τούτου)". |
| 117 · "ἡμεῖς δὲ φραζώμεθ’" | i | low | "may all turn out best of all": the "all" is an addition (ἄριστα is "best"); the house `i` for ὄχ’ ἄριστα is "best of all". | `i` → "how it may turn out best of all." |
| 124 · "σὴν γὰρ ἀρίστην" | i | nit | "of all mortal men" adds "all"; Greek is καταθνητῶν ἀνθρώπων. | → "no other man among mortal men". |
| 113 · "Τηλέμαχ’, ἦ τοι" | i | nit | "here" in "test me here in the halls" is not in the Greek. | Removed "here". |
| 131 · "πρῶτα μὲν ἂρ λούσασθε" | i | medium | `l` has "bid" for ἀνώγετε; `i` had "tell". The table keeps "bid" for the ἄνωγα family (ἄνωγα "I bid" at 122 in this part; ἀνώγει row follows it and turns down "told"). | `i` → "and bid the maids in the halls to take up their clothes;". |
| 141 · "ὣς ἔφαθ’, οἱ δ’ ἄρα τοῦ" | n | medium | Note said κλύον and ἐπίθοντο "have the pronoun τοῦ as their object"; τοῦ is a genitive after the verb of hearing and cannot be the object of πείθομαι (which takes the dative). | Note now says κλύον takes τοῦ 'him' in the genitive, as verbs of hearing do, and ἐπίθοντο has the same 'him' understood. |
| 143 · "ὁ δ’ εἵλετο θεῖος ἀοιδός" | i | low | `l` has "song-and-dance" for μολπή (house row ἤρχετο μολπῆς: "led the song and dance", turning down a bare "singing" that drops the dancing); `i` had bare "sweet song". | `i` → "a longing for sweet song and dance and for blameless dancing." |
| 150 · "σχετλίη, οὐδ’ ἔτλη" | l, i, n | medium | πόσιος οὗ κουριδίοιο is a bare genitive; it cannot mean "for" (no preposition) and must hang on δῶμα ("the great house of her own wedded husband"), set ahead of the infinitive. Draft had "for her own wedded husband" in both layers and a note saying the genitive says "for whom". | `l`: "of her own wedded husband, / to guard the great house"; `i`: "to guard the great house of her own wedded husband continually"; note now says the genitive depends on δῶμα. |
| 150 · same | n | low | "an exclamation nearer dismay than cruelty" contradicts the "Cruel one!" it glosses and claims a force the word's use here does not show. | → "an exclamation of reproach." |
| 164 · "ἂψ δ’ αὖτις κατ’ ἄρ’ ἕζετ’" | n | low | "ἕζετο is the aorist of ἕζομαι": the tense label is not secure (the form is traditionally taken as imperfect/aoristic). | → "a past tense of ἕζομαι". |
| 181 · "ὣς ἄρ’ ἔφη πόσιος πειρωμένη" | n | nit | "It is the same verb as πειράζειν" (114): the forms are πειράω and πειράζω. | "the same verb (πειράω beside πειράζω)". |

### Considered and refused

- **181–182 closing quotation / speech running into next part.** No change: unit 48 correctly has no closing mark, no `mark`, and its note says why. The 111/112 junction (Telemachus's rebuke) is likewise correct.
- **Line 129 `l` "addressed" for ἀπαμειβόμενος προσέφη.** Equals the published 031 wording and the table row; kept.
- **Unit 38 `l` "and her with a word he addressed" for καί μιν πρὸς μῦθον ἔειπε.** The table is itself split: the 20.261 row has "and to him a speech he said" (and bars "addressed him with a word"), but the rows for 16.460, 17.74, 17.495 and 19.96 all have "with a word addressed", and the 14.492 row has "a speech he uttered". The draft follows the majority; I did not unify them (a table decision for the owner). Flagged here so that it is seen.
- **Unit 1 `i` "and do not sit beside him to question him and inquire"** (participle ἑζομένη made a purposive infinitive, "with words" dropped). Judged within the licence of free English; both negatives and the sense of the reproach survive.
- **Unit 1 `i` "unnatural mother"** for δύσμητερ: the note states the sense ("a mother who does not act as one"); agrees with it.
- **Unit 2/40 `i` "when he had come … after toiling"** for the relative optative: acceptable (the optative is the generalising mood of the clause, and the fact is Odysseus's own return); shared by `l`/`i` at both places and kept identical, as the note promises.
- **Unit 21 `i` "I will tell you"** (the "you" is supplied): idiomatic, nothing lost.
- **Unit 22 `i` "their clothes"** (possessive supplied for εἵματα): the maids are plainly the ones dressing; left.
- **Unit 11 `i` "shabby"** for κακά: the house row for κακὰ χροῒ εἵματα has `l` "bad", `i` "shabby"; matches.
- **Unit 13 note "ἐνὶ δήμῳ is 'in the land'"**: matches the table's δῆμος "land" row; left.
- **Unit 8 note "winged because they fly from speaker to hearer"**: an explanation, not a label; left.
- **Unit 25 φρασσόμεθ’ "future"**: the future reading is the standard one; left.
- **Unit 35/36 repeats of the Book 23 lines 157/158/159–161 by published units.** The packet lists them as inside-unit repeats; the draft reuses the published wording as far as its sentence allows (only 162 differs in Greek, ὣς μὲν τῷ περίχευε, and is translated accordingly).

### For the caller (not a `units.json` fix)

**Line 129 has no closing mark in the pinned source** (`…πολύμητις Ὀδυσσεύς` with nothing after it), so unit 20 ends without punctuation and `build_odyssey.py` will refuse it ("does not end at punctuation"). The published 031 prints `·` here. This is the case of runbook "Missing punctuation in the source": add `·` after Ὀδυσσεύς at 23.129 in `source/odyssey-murray1919.json`, re-pin odyssey-112's `sha256` in `parts.json`, and make the same one-character change to unit 20's `t` (I was told never to touch `t`, and did not). `l` and `i` for that unit are already identical to 031's. Line 141 also ends bare (`ἐπίθοντο`), but unit 26 runs on to the `·` in 143, so it is not affected.

Counts by severity: high 0 · medium 8 · low 4 · nit 4 (16 table rows; 14 units changed).

## Pass 2

Method: conventions.md (prose sections in full, house-table rows checked against the part), runbook section 2, packet, units.json as left by Pass 1, gloss.json, known-forms.json, novel-forms.json. No translation consulted. Units re-run in full (notes labels, Greek to `l`, `l` and `i`, remembered English, quotation marks); every gloss entry (49 novel, 9 `__broaden__`) re-parsed against the line(s) where it occurs. Edits by script; every `t` verified identical before and after (`t` at 23.129 now ending ·, at 23.141 ending ,, as given). Mechanical checks: every printed word has an entry in known-forms or gloss (none missing); gloss keys equal novel-forms exactly; no ASCII apostrophe or backtick in any entry; no entry of 230 characters or more; no line numbers; no "here"; all 9 broadened entries begin with the old entry whole; quotation marks balanced and identical in `l` and `i` (opens on units 1, 5, 9, 17, 21, 30, 39, 44, each with `mark`; closes on 3, 7, 15, 19, 25, 31, 42, 46); `l` and `t` line counts equal.

### Changes to units.json

| Line · unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 124 · "σὴν γὰρ ἀρίστην" | l, n | low | σός is plain "your"; "your own" (note and `l`) imports the sense of the possessive ὅς, which the Greek does not have here. | `l` "for your, the best"; note "σήν is the possessive 'your'". `i` already had "your cunning". |
| 141 · "ὣς ἔφαθ’, οἱ δ’ ἄρα τοῦ" | l | nit | Line 1 of `l` ended in ";" where `t` has a comma and the published 013 wording of this line ends in a comma. | "obeyed;" to "obeyed,". |

Counts by severity, units: high 0 · medium 0 · low 1 · nit 1 (2 units changed). Pass 1's fixes were re-checked and stand (100/168 οἱ, 105 μοι, 114, 117, 131, 141 note, 143, 150, 164, 181).

### Gloss-parse (entries changed in gloss.json)

| Key | Severity | What was wrong | What was done |
|---|---|---|---|
| δύσμητερ | medium | Lemma was the vocative form itself; meaning "hard-hearted" is not the word's sense and contradicts the note ("a mother who does not act as one"). | Lemma δυσμήτηρ; "ill-mother, unnatural mother, one who does not act as a mother". |
| μεγαλίζομαι | medium | "make much of" is the wrong sense for 23.174 (she disowns exalting herself). | "exalt oneself, be haughty, give oneself airs". |
| ἀφεσταίη | medium | "(mid. sense)" is not a true parse; the form is the strong aorist active in form, intransitive in sense. | "strong aor. opt. 3 sg., intrans., potential with κε (Attic ἀποσταίη)". |
| φρασσόμεθ | medium | Attic equivalent printed as malformed φράσόμεθα. | Attic φρασόμεθα. |
| περιστεναχίζετο | low | "make resound" is transitive; the form is passive and the house is what resounds. | Added the passive sense "resound, be filled with echoes". |
| πειρωμένη | low | "Attic πειρωμένη, dep. πειράομαι" muddled; the participle is the same form in Attic. | Lemma "πειράω, mid. πειράομαι"; "(same form in Attic)". |
| προσφάσθαι | low | Lemma unaccented as a paroxytone (προσφημί); LSJ has πρόσφημι; meaning "say, utter" loose. | Lemma πρόσφημι; "speak to, address"; "pres. inf. mid.". |
| στερεωτέρη | low | No Attic equivalent given for the Ionic feminine. | "epic -η (= Attic στερεωτέρα)". |
| γλυκερῆς | low | Same. | "epic -ῆς (= Attic γλυκερᾶς)". |
| στόρεσον | nit | Attic equivalent gave only the present. | Added "imper. στρῶσον". |
| ἀμφιέσαντο | low | "epic" without saying what is epic; Attic form has the augment. | "unaugmented (= Attic ἠμφιέσαντο)". |
| ἀμφιέσασθε | nit | "epic" label false of an imperative that is identical in Attic. | Label removed. |
| ἀνώγετε | low | Quoted gloss ’order’ against the house rendering "bid" (used in `l` and the table). | ’bid’. |
| φράσεται | low | Quoted gloss ’find out’ differs from the part's reading "observe". | ’will observe, perceive’. |
| ἐρίσειε | nit | Quoted ’could rival’ against `i` "would rival". | ’would rival’. |
| ἡγείσθω | nit | "(+ dat.)" omits the genitive of what is led (ὀρχηθμοῖο). | "+ dat. of those led, + gen. of what is led". |
| __broaden__ ἄρειον | nit | Example quoted ’will perceive even better’, not the part's reading. | ’will observe better’. |

Counts, gloss: 17 entries changed (medium 4 · low 8 · nit 5); 33 novel entries and 8 other `__broaden__` entries re-parsed and left (the κε, κέν, κῆρ, μὴ, πυκινὸν, σιδήρεον, ἀπηνέα, πολὺ additions each agree with the cited line and keep the old entry whole).

### Considered and refused (Pass 2)

- **Unit 18 `l` and `i` "along with you" for ἅμ’ ἑψόμεθ’.** The pronoun is not in the Greek, but ἅμα with ἕπομαι has the speaker's father as the evident companion, and the note says ἅμα is "along with"; supplied object is within free English. Kept.
- **Unit 32 `l` "a fine cloak threw" against published 013 "had thrown" for line 155.** The difference is the tense of the clause (main verb here, ἐπεί-clause there), not a variant rendering; kept.
- **Unit 1 οἱ.** Pass 1's open-referent wording is right; the usual reading (the wife) is not required by the Greek and the note does not assert it.
- **Unit 31 τά.** Parsed as object of ἴσαν with the people outside as the unexpressed subject; the note's "those things" agrees with this. Kept.
- **Unit 4 "ἐρέεσθαι (uncontracted; Attic ἐρέσθαι)".** Attic ἐρέσθαι is the aorist, but the Attic correspondence is the same verb; the note does not claim the same tense. Kept.
- **Unit 0 `i` "do not sit beside him" (μύθοισιν dropped; participle turned finite).** Already refused in Pass 1; sense and force survive.
- **Gloss γλαφυρήν, καλλιζώνων, γνωσόμεθ, παιζόντων "of a lyre / of women / ’we shall know each other’ / ’of the men dancing’".** Context tags are close to line-pinning, but each is a true parse of the form and carries no line number; left.
- **Gloss ἀτέραμνον.** The derivation is uncertain but the meaning is not; the note and new-renderings.md already say so. Left.
- **Known-form entries.** Spot-checked ὅς, οἱ, οὗ, ἧς, ᾧ, τῇ, τῷ, τὰ, τὸν, τοῖσιν, ἦ, ἄρ, ἂρ, κέ, κ, δ, γ, ὅττι, εἰν, ἔωσιν, ἔθηκαν against the lines; each existing entry already covers the use in this part, so no further `__broaden__` is needed.
