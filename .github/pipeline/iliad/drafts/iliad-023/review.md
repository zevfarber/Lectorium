# iliad-023 (Iliad 4.183–271) — review

## Pass 1

Method: runbook §2 order. (1) every grammatical label and every where-it-stands claim in every note checked against the line, cross-references checked against the source file (`source/iliad-monro-allen1920.json`) and the published parts, notes read against their own `l`/`i`; (2) Greek → `l` word by word; (3) `l` ↔ `i`; (4) remembered English in `i`; (5) quotation marks, `mark`s, `p`s (checked by script against the packet's ¶ list and against the last unit of iliad-022, which ends with Agamemnon's speech at 4.182). `t` was not touched (verified unit by unit after the edit); `units.json` was edited by script and round-trips byte-for-byte except for the edits below. Scansion flags: none in the packet, so no hand scansion was required and no note was given a metre sentence. The validator was not run (it needs the built `iliad-023.json`; that is the build step).

Counts of changes: high 4, medium 3, low 13 (20 edits in all).

### Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 190 · n | high | παύσῃσι was labelled a subjunctive "(3 pl.)". The 3 pl. subjunctive is -ωσι; this is the 3 sg. in -ῃσι, and the neuter plural φάρμακα takes a singular verb. | "(3 sg.; a neuter plural subject takes a singular verb)". |
| 190 · n | low | φάρμαχ’ called "elided" only; the κ→χ comes from the rough breathing of ἅ. | Added "(κ becomes χ before the rough breathing of ἅ)". |
| 210 · n | high | ἵκανον called "unaugmented aorist of ἱκάνω"; it is the imperfect (the Odyssey and Iliad glossaries both say impf.). | "unaugmented imperfect". |
| 268 · n | high | μαχώμεθ’ called an "aorist subjunctive"; it is the present subjunctive of μάχομαι (the aorist would be μαχεσσώμεθα). | "has a present subjunctive". |
| 242 · n | high | "ἰόμωροι occurs only here" is false: it recurs (the same address to the Argives) at 14.479, and a note may not assert about the rest of the poem what this part cannot show. | "ἰόμωροι is a word whose meaning is not known"; the guess about ἰός + μῶρος is kept. |
| 235 · n | medium | "the same clause as in 4.67 and 4.72": the source has ἄρξωσι πρότεροι ὑπὲρ ὅρκια δηλήσασθαι there (infinitive), not the finite δηλήσαντο. | "the same words as in 4.67 and 4.72, where the verb is the infinitive δηλήσασθαι". |
| 264 · i | medium | "the man you have always boasted that you are": πάρος is "formerly, before", not "always"; `i` added force and shifted the tense relation to `l` ("such as you formerly boast to be"). | "and be the man you have boasted until now that you are". |
| 222 · n | medium | "who had put off their arms during the truce" asserts a fact about earlier books that this part does not show. | Rewritten to what the part does show: the Trojans, subject of the previous line, are already advancing as "shield-bearing", and αὖτις "again" says these men arm a second time. |
| 270 · i | low | αὖ ("and for them, in turn") was dropped from `i`, though `l` and the note carry it and 238 renders αὖτ’ ("for our part"). | "and in their turn death and troubles will come to them afterwards". |
| 185 · n | low | "three subjects … in the order πάροιθεν, ὑπένερθε" left unclear which subject goes with which adverb. | Spelled out: belt guards in front; waistcloth and belly-guard guard underneath. |
| 210 · n | low | "ἕλκεν is an imperfect, ‘was drawing’" while `l`/`i` say "drew": note and layers looked at odds. | Note now says the imperfect means the drawing is still going on when 214 begins (no English claim left to conflict). |
| 208 · n | low | ὄρινε called "the unaugmented aorist"; 3 sg. aorist and imperfect coincide, and the glossary and iliad-020's note say only "a past tense". | "an unaugmented past tense of ὀρίνω". |
| 214 · n | low | ἄγνυμι glossed "break" but the sense given is "bent back" with no bridge. | Added "literally ‘were broken back’, so ‘were bent back’". Label and the hedge ("not certain") kept. |
| 215 · n | low | "the belly-guard is a guard of metal" stated flat; the table (4.137) gives it as the usual explanation. | "is, on the usual explanation, a guard of metal". |
| 223 · n | low | The three participles were said to follow "οὐδ’ … οὐδ’"; the negatives are οὐκ ἂν … οὐδέ … οὐδ’. | Corrected. |
| 227 · n | low | "the patronymic Πτολεμαίου Πειραΐδαο" muddled the father's name with the patronymic. | Rewritten: υἱὸς Πτολεμαίου, and Πειραΐδαο the patronymic of Πειραΐδης in the epic genitive, saying whose son Ptolemaeus was. |
| 231 · n | low | "Line 250 will repeat this half-line": what 250 repeats is the last three words (ἐπεπωλεῖτο στίχας ἀνδρῶν), not a half-line. | "repeats its last three words". |
| 235 · n | low | "waits for ἡμεῖς in the next line": ἡμεῖς is at 238, three lines on. | "in 238". |
| 243 · n | low | τίφθ’ explained as "π + h = φ"; both π and τ are aspirated (τίπτ’ + οὕτως). | "(πτ + h = φθ)". |
| 250 · n | low | "repeat the words of 230–231": 230 has κοιρανέοντα, 250 κοιρανέων. | Says so: κοιρανέοντα in 230; the last three words of 231 exactly. |

### Considered and refused

- **ἄγεν 4.214** (flagged). Label kept: 3 pl. aorist passive of ἄγνυμι (= ἐάγησαν) is the standard reading (cf. ἄγη, 3.367, in the table), ἄγεν elsewhere in the poem is the imperfect of ἄγω (2.557), and the note already says the form is uncertain. `l` "were bent" and `i` "were bent back" stay (new-renderings.md records the avoided alternatives). Only the bridge from "break" to "bent" was added (above).
- **ἰόμωρος 4.242** (flagged). Beyond the false "only here", kept: the guess ἰός + μῶρος is hedged in the note and the English says it is a guess. "arrow-dull" in `l` and "dull archers" in `i` stay.
- **εἰρύατ’ 4.248** (flagged). "3 pl. perfect passive of ἐρύω ‘draw’, so ‘are drawn up’" is true of the form and fits the line (ships on the beach); the same form recurs with this sense elsewhere. The alternative ‘guarded’ would change `l` and is not needed. Unchanged.
- **ἀμύμονος ἰητῆρος 4.194** (flagged). The note's claim that both genitives belong to Ἀσκληπιοῦ is right (υἱόν is accusative, so a genitive pair cannot go with it); `l` and `i` agree; ἀμύμων is said to be unknown in meaning, as the conventions require. Unchanged.
- **δαιτρόν 4.262** (flagged). "the usual explanation" hedge is present; `l` and `i` ("allotted portion") agree; "a rare word" is a statement about the word, not a claim about other lines I could falsify, and the form does occur in only this line within the Iliad text I searched (δαιτρεύειν at 11.705 is another word). Unchanged.
- **Note length at 235 (115 words).** The part's other long notes are 100–102 words, and the published parts run to 186; the note leads with what the reader needs (the γάρ reason) and carries a five-line sentence with three constructions, so nothing was trimmed.
- **κεν + subjunctive, 191, `l` "may make cease" vs `i` "will stop".** Prospective relative clause; `i` gives the force in natural English; the new-renderings row records it. Unchanged.
- **"Rise up" (204) vs "Rise" in iliad-018 (3.250), and `l` "he summons you" vs "they are calling you".** The Greek is not identical (person, καλέει/καλέουσιν), so the validator rule does not apply; `up` renders the preverb sense and is recorded in the note. Unchanged.
- **`l` supplies "you" at 204 without parentheses while "(me)" and "(it)" are bracketed at 185 and 191.** Published precedent (3.250 "they are calling you") does the same; left.
- **ὦ left untranslated in `l` at 189.** The note mentions it; vocative ὦ without force is routinely dropped. Left.
- **ἕποντο "unaugmented imperfect" (201).** The Iliad glossary says "augmented (= εἵποντο)", which looks wrong, but the note is right (ἕποντο is the unaugmented form) and glossary entries are the glosser's. Flag for the second pass / glosser.
- **"Thessalian town" and "Catalogue gave Tricca to Machaon's troops" (201).** 2.729–732 checked: Tricca, then "of these the two sons of Asclepius were leaders, Podaleirius and Machaon". Cross-reference sound.
- **Cross-references otherwise verified:** 1.130 (reply formula), 1.478 (εὐρὺν στρατὸν Ἀχαιῶν), 4.92 (ἱσταμένη, "she"), 4.151 (ὄγκους), 4.137 (μίτρης), 3.310 (ἰσόθεος φώς), 199 (βῆ δ’ ἰέναι), 185–187 ≈ 215–216, 196–197 = 206–207, 195 vs 205, 232/240/234, 226/231, 237/238, 254/268, 270/236. All true.
- **"ἔστητε … ‘you stand’" for an aorist (243).** The English present is natural for this aorist and the note labels the form correctly. Left.
- **"heartily cheer" (232) vs "revile sharply" (240) for the same μάλα; `l` has "greatly" in both.** `i` is free to vary; both are real English. Left.

### Layer checks with nothing to change

- Greek → `l`: all 48 units read word by word; case, tense, mood and particles right apart from the items above. `l` line division equals `t` line division in every unit (scripted).
- `l` ↔ `i`: sense and force agree in every unit after the 264 and 270 edits; `i` has no newlines; Machaon is named at 208 and 210 and "the Achaeans" at 222 where the Greek subject switches, as the notes say.
- Remembered English: none found beyond the "always" at 264 (fixed); house renderings (δαΐφρων "wise-minded"/"wise-hearted", κάρη κομόωντες, αἴθοπα οἶνον, κυδιάνειραν, ἱππόβοτος, βοὴν ἀγαθός, ἄναξ ἀνδρῶν, χαλκοχιτώνων, ἀσπιστάων as at 4.90–91) match the tables and published parts. Shared lines: 4.188 and 4.203 identical to the published English.
- Quotation marks and marks (scripted and read): “ on 184, 189, 193, 204, 234, 242, 257, 266 (each with a `mark`); ” on 185, 190, 195, 204, 238, 247, 264, 270; 235, 261 and 268 correctly carry the speech across units without closing. `p` on 183, 188, 192, 198, 208, 220, 223, 240, 242, 250, 265 = the packet's ¶ list exactly. iliad-022 ends with Agamemnon's speech at 4.182, and 183 correctly opens as narration with no opening mark.

## Pass 2

Method: `units.json` re-read fresh (every note against its line, `l`, `i`; the 20 pass-1 edits each re-checked; `t` compared with the packet's lines by script, unchanged). Then every entry of `gloss.json` (151 novel forms and the 14 `__broaden__` entries) checked against the line(s) where the form stands: lemma, meaning, parse true of that form, Attic equivalent named for Homeric forms, length under 230 (the `__broaden__` entries are old entry plus new reading and are exempt), typographic ’ only, no line numbers, no "here". Each `__broaden__` entry was also checked to begin with the existing glossary entry whole (all 14 do). `gloss.json` and `units.json` were edited in place by script; `t` untouched (the diff touches one `n` only). Pass-1 edits introduced no error.

Counts of changes: high 1, medium 3, low 7 (11 edits in all).

### Changes

| where · field | severity | what was wrong | what was done |
|---|---|---|---|
| 235 · units `n` | high | "τέρενα is the neuter plural of τέρην": χρόα is the accusative singular of χρώς (the existing glossary says masc. acc. sg.), so τέρενα is masculine accusative singular. | Rewritten: masculine accusative singular, agreeing with χρόα. (The gloss entry τέρενα already lists both readings.) |
| ἑστᾶσ’ 243 · gloss | medium | Parsed as a perfect participle fem. nom. pl. (ἑστᾶσαι); the note, and the usual reading, take it as the finite 3 pl. perfect ἑστᾶσι (= ἑστάασι), "they stand", the main verb of the simile. Entry and note disagreed. | Entry now: perf. 3 pl., elided (= ἑστᾶσι, for ἑστάασι; Attic ἑστήκασι): ’they stand’. |
| κέρωνται 257 · gloss | medium | "= Attic κεράννυνται" is an indicative; the form is a subjunctive, and the Attic subjunctive is κεραννύωνται. | "(Attic subj. κεραννύωνται)". |
| ἔχευαν · broaden | medium | New reading "threw together" contradicts the lemma "pour" and the note ("pour together"). | "poured together, confounded". |
| ἰόμωροι · gloss | low | "perhaps ’mere archers’" gave a sense the unit does not (the unit's note and `l` give the guess ἰός + μῶρος "arrow-dull"), and leaves μῶρος unnamed. | "perhaps ’arrow-dull’ (ἰός ’arrow’ + μῶρος ’dull’)"; still marked disputed. |
| εἰρύατ’ 247 · gloss | low | Homeric ending -αται given without its Attic equivalent. | Added "(Attic -νται)". |
| ἀγηγέραθ’ 211 · gloss | low | Homeric ending -ατο given without its Attic equivalent. | Added "(Attic -ντο)". |
| τίω 257 · gloss | low | Epic present with no Attic equivalent named. | Added "(= Attic τιμῶ)". |
| ἀλκῆς 234, χάρμης 222, τρίκης 202 · gloss | low | "Ionic -ῆς / -ης" implies a contrast with Attic; Attic has the same genitive after κ, so the label is misleading. | The label removed (three entries). |

### Considered and refused

- **ἕποντο entry (existing, "augmented (ἕποντο = εἵποντο)").** Looks wrong (ἕποντο is the unaugmented form; the unit note is right), but the runbook forbids rewriting existing glossary entries. Left; reported to the caller for the corpus owner.
- **εἰρύατ’ as εἰρύαται (perfect) rather than εἰρύατο (pluperfect).** Present tense in the line ("are drawn up"), so the perfect reading stands; as in pass 1 the lemma ἐρύω "draw" is kept.
- **πάσσε "impf./aor."** The form is unaugmented and the two tenses coincide in the 3 sg.; the hedge is correct. Kept.
- **ἄγεν (broaden), ἰητῆρος, ἀμύμονος, δαιτρόν.** Re-checked against the line; true as written (ἄγεν = ἐάγησαν reading, hedged in the note).
- **πλεῖον (broaden) "(or read as the comparative, ’a larger cup’)".** Honest hedge about a real ambiguity; `l` and `i` ("full") agree with the first reading. Kept.
- **ἴδῃ (broaden).** New reading (aor. subj. act. 3 sg. after ὄφρα, 195) is true; the old entry's wording was left untouched.
- **ἔδυν "intransitive" though the line has an object (τεύχε’).** The label describes the second-aorist paradigm; the meaning gives "put on (armour)". Kept.
- **Length.** No novel entry reaches 230 characters (longest 152 after edits); `__broaden__` entries αὐτῶν, τά, τὸ, φίλα, ἴδῃ exceed it only because the old entry is carried whole, as the runbook requires.
- **Typography, line numbers.** No ASCII or left single quotes, no line numbers or "here" in any entry (scripted).
