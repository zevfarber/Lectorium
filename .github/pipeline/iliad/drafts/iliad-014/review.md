# iliad-014 (2.676–779) — review, pass one

Reviewer pass one, on `units.json` and `new-renderings.md` only. `t` was not touched in any unit (checked after the edits: the units' `t` are identical to the draft's). No gloss.json yet; the second pass reads it.

Severity: high = a false statement, or something the gate or the reader will trip on; medium = a house-rendering, reuse, cross-reference or grammatical-label error; low = wording, precision, or a claim stated more strongly than the line shows.

Counts, changes made: 1 high, 15 medium, 11 low (27), plus 1 high left unresolved (needs `t`, below).

## Unresolved (needs the caller)

1. **724 · `t` (unit 1) and `t` (unit 2) · high · the cut falls one word too early.** Unit 1 has `t` = `ἔνθ’ ὅ γε κεῖτ’`, unit 2 begins `ἀχέων· τάχα δὲ …`. The ano teleia is after ἀχέων, not after κεῖτ’; unit 1's `l`/`i` ("There he lay grieving;") and note ("ends at the ano teleia") already assume the right cut, and `build_iliad.py` line 35 will refuse unit 1 because its `t` ends in an elision mark, not punctuation. Not changed, because `t` is not mine to touch. Fix by re-cutting: unit 1 `t` = `ἔνθ’ ὅ γε κεῖτ’ ἀχέων·`; unit 2 `t` = `τάχα δὲ μνήσεσθαι ἔμελλον\nἈργεῖοι παρὰ νηυσὶ Φιλοκτήταο ἄνακτος.` Their `l`, `i`, `n` then fit as they stand (unit 2's `l` already begins "and soon").
2. **ποδώκης · convention clash, not a draft error.** The Iliad table (conventions.md, the ποδάρκης row) reserves "fleet-footed" for ποδώκης, and 764 follows it. The Odyssey's published parts ship "swift-footed" for ποδώκης (odyssey-055 line 471, odyssey-056 line 538), which is also the Iliad's "swift-footed" for ποδάρκης. Left as drafted; the owner may want one of the two rows reconciled.

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| `about` | high | Said "the mares of Admetus’ son, which Eumelus drives". Φηρητιάδαο is "son of Pheres", usually taken to be Admetus, and Eumelus is Admetus' son and the driver (the note at 763 says so). Also "is dead … is dead" doubling about Protesilaus. | "the mares of “Pheres’ son” (usually taken to be Admetus), which Eumelus drives"; "Protesilaus, killed as he leapt …, has his troops marshalled by his younger brother Podarces". |
| 761 · `l`, `i`, `n` | medium | The drafter rendered a question (`?`) though the edition ends 762 with a full stop. The Greek is τίς … σύ μοι ἔννεπε Μοῦσα: the question is put inside a command ("tell me … who …"), which is why the edition does not print a question mark. A question mark contradicted the edition and the note said so. | `i`: "Tell me, Muse, which of them was far the best, of the men themselves and of the horses that followed with the sons of Atreus." `l`: kept the Greek order, "Who then of these was by far the best — do you tell me, Muse — / of themselves and of the horses that together with the sons of Atreus followed." (full stop, line division kept; "which" → "that", since the relative covers men and horses). `n`: the sentence "it is a question, though the edition prints a full stop" replaced by one saying the question sits inside a command and the English keeps the edition's full stop. |
| 699 · `l`, `i`, `n` | medium | γαῖα μέλαινα rendered "black earth". The Odyssey table (11.365) and the published Odyssey (odyssey-054, -056, -093) fix "the dark earth" in both layers, with "black" kept for ships. | "dark earth" in `l` and `i`; note says μέλαινα is "dark" here and "black" of the ships at 710. |
| 681 · `i` | medium | "who lived in Pelasgian Argos": the Catalogue rows fix ναίω as "dwelt in" in both layers and list "lived in" as avoided; `l` and `n` already say "dwelt"/"dwell". | "who dwelt in Pelasgian Argos". |
| 745 · `n` | medium | "ὑπερθύμοιο … the Odyssey’s epithet of Creon and of Thrasymedes": false. The published Odyssey has ὑπέρθυμος of Creon (odyssey-053) and of the Giants (odyssey-030); Thrasymedes is μενεπτόλεμος (odyssey-013). | "of Creon and of the Giants". |
| 748 · `n` | medium | "ἦγε the unaugmented imperfect of ἄγω": false label; ἦγε is the augmented imperfect (ἦ- is the lengthened ἀ-). | "ἦγε the imperfect of ἄγω ‘bring’". |
| 751 · `i` | medium | "had their farmlands" for ἔργα νέμοντο: νέμομαι is "inhabited" in both layers through the Catalogue (table), and `l` already says "inhabited"; "had" is ἔχω's word. | "and those who inhabited the farmlands around lovely Titaressus"; new-renderings row updated. |
| 775 · `l`, `i` | medium | λωτὸν ἐρεπτόμενοι is the same two words as Odyssey 9.97 (odyssey-039 line 97), published as "feeding on lotus" in both layers; the draft had "eating lotus" and listed "feeding on" as avoided. | "feeding on lotus and marsh-nurtured celery" in `l` and `i`; new-renderings ἐρέπτομαι row rewritten. |
| 775 · `n` | medium | Said "the lotus of the Odyssey is a fruit that men eat, and which plant either is, is not known", leaving out that the Odyssey ships "clover" for λωτός in a horse-pasture list (odyssey-019, 4.603, the Iliad's own sense). | Note now gives both Odyssey uses and says which plant is not known; the λωτός row in new-renderings records why "lotus" stays (the shared half-line) and why "clover" was not taken. See refused finding 4. |
| 778 · `i` | medium | ἔνθα καὶ ἔνθα rendered "here and there" in `i`; the Odyssey table fixes `i` "this way and that" (`l` keeps "here and there"), as in iliad-011 459 and iliad-012 474. | "went to and fro, this way and that, through the army". |
| 713 · `n` | medium | "the mother’s name, Ἄλκηστις, comes last": false; Πελίαο θυγατρῶν εἶδος ἀρίστη follows it. | "is held back until after her epithet". (Also dropped the unneeded "(πάϊς is the epic παῖς)" gloss to keep length.) |
| 740 · `n` | medium | "The leader formula of 698, τῶν αὖθ’ ἡγεμόνευε": 698 has τῶν αὖ, not αὖθ’ (the note at 698 itself says so). | "The leader formula τῶν αὖθ’ ἡγεμόνευε (698 has τῶν αὖ), with …". |
| 755 · `l` | medium | "the water of Styx": the same half-line Στυγὸς ὕδατός ἐστιν ἀπορρώξ is published at Odyssey 10.514 (odyssey-050) as "the water of the Styx" in both layers; `i` already matched, `l` did not. | "the water of the Styx"; new-renderings row updated. |
| 760 · `l` | medium | ἡγεμόνες Δαναῶν καὶ κοίρανοι ἦσαν is published in iliad-012 (line 487) as "the leaders of the Danaans, and rulers"; `l` here reordered it. | "These then were the leaders of the Danaans, and rulers;" (`i` already agreed with the published `i`). |
| 736 · `n` | medium | Scansion flag. Hand-scanned: τῶν ἦρχ’ | Εὐ-ρύ-πυ | λος Εὐ | αί-μο-νος | ἀ-γλα-ὸς | υἱ-ός, 15 syllables, a good hexameter with main caesura after λος, but λος is a short syllable ending in a consonant that stands in the long place of the third foot before the vowel Εὐ- (no consonant to make position). The irregularity is real (the scanner's second reading needs the same lengthening). | One plain sentence added: "The line is metrically irregular as transmitted: the last syllable of Εὐρύπυλος is short but stands in a long place, at the main caesura before the vowel of Εὐαίμονος." |
| 771 · `n` | medium | ἀπομηνίσας: rare verb, given one confident sense ("so ‘having withdrawn in wrath’"); the force of ἀπο- (away / utterly / ceasing) is not settled. | Note says the force of ἀπο- is not certain and the English takes "having withdrawn in wrath"; new-renderings row marked "+ note". |
| 687 · `i` | low | "to lead them into the ranks": ἐπὶ στίχας is "to the ranks" (`l` says so); "into" changes the sense and is a ready-made phrase. | "to lead them to the ranks". |
| 704 · `l` | low | ὁπλότερος γενεῇ is published at Odyssey 19.184 (odyssey-093) as "the younger by birth". | `l` "the younger by birth;" (`i` "and younger by birth" kept, it follows a list of kin). |
| 763 · `l` | low | "Pheres’ son": other patronymics in `l` are hyphenated ("Atreus’-son", "Heracles’-son", "Selepus’-son", "Phylacus’-son"). | "Pheres’-son"; new-renderings row updated. |
| 680 · `n` | low | "in the same line as 516" is wrong English for "this line is the same as 2.516". | "the line is the same as 516". |
| 690 · `n` | low | διαπορθέω described as "the verb πέρθω … with δια-"; it is formed on πορθέω, a by-form of πέρθω. | Corrected. |
| 694 · `n` | low | "The poet looks ahead to Achilles’ return": a claim about the rest of the poem that this part cannot show. | "The poet looks ahead to the end of the withdrawal." |
| 698 · `n` | low | ζωός called "the epic form of ζῶν"; it is the Ionic adjective "alive" (Attic ζῶν). | Corrected. |
| 708 · `n` | low | δεύονθ’ labelled only "an elided form of δεύομαι". | "the imperfect δεύοντο of δεύομαι ‘lack’, elided before the rough breathing of ἡγεμόνος" (the θ is the τ aspirated by it). |
| 719 · `n` | low | ἐμβέβασαν described as "an epic form taken as ‘were on board’". It is the pluperfect (like ἕστασαν, 777). | "the epic pluperfect of ἐμβαίνω ‘go aboard’ … ‘had gone aboard’, that is ‘were on board’". `l` "had embarked" and `i` "were on board" already agree. |
| 724 (unit 2) · `n` | low | "The Iliad does not tell what follows": a claim about the rest of the poem. | Sentence removed. |
| 742 · `n` | low | "took vengeance on the Pheres": the same name as Pheres the father at 763, in one part. | "the Φῆρες, the beasts"; "what looks like a masculine form" shortened to "a masculine form". |

Cross-references checked and found true (no change): 1.8, 1.36 (Leto ἠΰκομος), 1.69, 1.268, 1.306, 1.602; 2.401, 484, 516, 524, 527, 534, 540, 552, 563, 570, 596, 601, 632, 640, 674 against the source; Odyssey: 5.13 (odyssey-022) κρατέρ’ ἄλγεα πάσχων; ἀγλαὸς υἱός of Nestor's son (odyssey-014) and of Philoctetes (odyssey-010); 10.188 ἐγχεσίμωρος Myrmidons (odyssey-010); 7.57 εἶδος ἀρίστη Periboea (odyssey-030); δῖα γυναικῶν of Penelope and Helen (odyssey-004, -016, -072, -081); 11.195 ἔνθ’ ὅ γε κεῖτ’ ἀχέων of Laertes (odyssey-052); ὀλοόφρων of Atlas, Aeetes, Minos (odyssey-001, -046, -054); μενεπτόλεμος Thrasymedes (odyssey-013); 15.169 ἀρηΐφιλος Menelaus (odyssey-072); πτολιπόρθιος of Odysseus (odyssey-044, -070); 10.514 ἀπορρώξ (odyssey-050); 4.626 (odyssey-019, the unit at 625 holds 625–627): the repeated line 2.774 is reused word for word in `l` and in the shared words of `i`; ποθέοντες "missing"/"longing for" (odyssey-079, -109); τρηχεῖαν (iliad-013 632, odyssey-026, -039). Reused English: 680, 733 (iliad-012 516), 710, 737, 759 (iliad-012 534), 747 (iliad-012 524) are identical to the published units, and 703 = 726 agree with each other.

## Findings refused

1. **700 ἀμφιδρυφής, `i` "with her cheeks torn in mourning".** Kept. The Greek says only "torn on both sides"; "cheeks" and "in mourning" are the lexicon explanation (LSJ/Autenrieth, the permitted aids), the note says so, and the note flags that the Greek says only "torn all round". The "avoided" column of the new-renderings row says each of "scratched", "tearing her face" decides what is torn, which `i` itself does by the lexicon; left, since the other option ("torn on both sides") is not English.
2. **764–765 ὄτριχας / οἰέτεας / ἐΐσας.** Kept as drafted: "alike in hair, of one age" are the usual lexicon senses, "well-balanced" is the table's ἐΐσας, and the note says the sense of the phrase is not certain. "as if by the plumb-line" in `i` adds "as if" to a dative of means; kept, it is how the dative reads in English. One thing for the caller: the archive prints σταφύλῇ (with a circumflex on the η); the note quotes σταφύλῃ. That is the edition's `t`, which I cannot change; the note's form is the normal spelling.
3. **729 κλωμακόεις.** Kept: "stony" with the note that "terraced" is another reading; the note says the sense is not certain.
4. **775 λωτός → "clover".** Considered, because odyssey-019 ships "clover" in a horse-pasture list. Refused: the Odyssey table fixes "lotus", the two-word half-line λωτὸν ἐρεπτόμενοι is "feeding on lotus" in the Odyssey, and "clover" decides the plant. The note now tells the reader about the Odyssey's "clover". A decision for the owner if "clover" is preferred.
5. **742 subject.** Checked: κλυτὸς Ἱπποδάμεια is the nominative (masculine adjective form with a feminine name, as the edition prints it), the subject of τέκετο; τόν is Polypoetes; the subject of ἐτίσατο is Peirithous. No change.
6. **763 Φηρητιάδαο.** Kept: patronymic, "the son of Pheres", note that the man is usually taken to be Admetus (713 shows Admetus has the son Eumelus, who drives, 764). Only the `l` hyphen changed.
7. **744 "forced them on to the Aethices" for πέλασσεν.** Kept: LSJ gives "drive near" for πελάζω with ὦσε before it; the choices that avoided "forced" ("drove", "brought") are reserved words (ἐλαύνω, ἄγω).
8. **721–723 "suffering … suffering" in `i`.** Kept: πάσχων and μοχθίζοντα both come out "suffering" by the new-renderings choice; `l` keeps "suffering" and "toiling" apart, and every alternative adds a degree or loses the sense.
9. **694 and 724 ἔμελλεν/ἔμελλον: `l` "was going to", `i` "was to".** The Odyssey table (17.412) has "was about (to)"; refused because the Iliad's published rendering (iliad-007, 2.35 and 2.39: "not going to be fulfilled", "was yet to lay") is "going to" in `l` and "to" in `i`, and the Iliad's own earlier part governs.
10. **703 and 726 "Yet they were not without a commander".** Kept: οὐδὲ μὲν οὐδ’ is idiom, the note explains it, and 703 = 726 agree.
11. **Units that end at a comma** (676, 681, 683, 688, 690, 695, 697, 711, 716, 729, 734, 738, 742, 749, 751, 753, 756, 758, 763). The 4-line rule says a comma cut is for a period that would run past four lines, and several of these periods are shorter. Refused as a finding: the Catalogue parts already published cut the same way (iliad-012 has one-line comma units at 488 and 499; 70 of 732 published units end at a comma), build and validator allow it, and the formula lines 710, 737, 759 must be separate units to match the published ones.
12. **701 `i` "from his ship" against `l` "from the ship".** Kept: it is Protesilaus' ship in the sentence.
13. **753 note "but it does not" against `l` "and yet it does not".** Not a contradiction (both render οὐδ’ ... γε after a relative clause); kept.
14. **761 τὰρ = τε ἄρα.** Could not confirm beyond the cross-reference to τίς τ’ ἄρ at 1.8 with the aids allowed; kept as drafted.
15. **Note length.** After the edits 713, 742, 761 and 771 and 775 are over 110 words (validator WARN, not FAIL); 704 and 721 were already at 110. Kept: each carries a grammatical point or a correction that would otherwise be lost. Trim if the WARNs matter.
16. **Remembered English.** Read every `i` for phrases that arrive fully formed; found none that does not rebuild from the grammar apart from 687 "into the ranks", changed above. "half-finished" (700), "marshalled" (704, 727) and "feeding on" (775) are the table's, the Odyssey's or follow from the lexical senses.

## Not yet checked

Pass two: gloss.json (not yet written), the build and validator output, and a second read of `l` ↔ `i` after these edits.

---

# Pass two

Pass two read `units.json` afresh (Greek → `l` word by word, `l` ↔ `i`, every label and cross-reference in the notes) after the orchestrator's re-cut of 724, and read every entry of `gloss.json` (253 new forms and 19 broadened readings) against the line it stands in. `t` was not touched (checked: the units' `t` joined are word for word the source, 698 words, 2.676–779; the line divisions of `l` match those of `t` in every unit). Place identifications that cannot be read from the Greek were softened or removed; where a claim rests on the public-domain aids (LSJ, Autenrieth) it was kept. Scripts: `/tmp/rev014/pass2_units.py`, `/tmp/rev014/pass2_gloss.py`.

## Re-cut at 724 — checked

Unit 1 `t` = `ἔνθ’ ὅ γε κεῖτ’ ἀχέων·` (ends at the ano teleia), unit 2 `t` = `τάχα δὲ μνήσεσθαι ἔμελλον` / `Ἀργεῖοι παρὰ νηυσὶ Φιλοκτήταο ἄνακτος.` Unit 1: `l` "There he lay grieving;", `i` the same, `n` ("the same words as the Odyssey has of old Laertes", "the same phrase as in 694", "ends at the ano teleia in the middle of 724") all true of the new cut. Unit 2: `l` "and soon were going to call to mind / the Argives…", `i` "and soon the Argives beside the ships were to remember lord Philoctetes", `n` ("‘and soon they were going to’", μνήσεσθαι future infinitive with the genitive, "as in 694") all fit. Both keep `ln` 724 and `v`; no `p`. The pass-one unresolved item 1 is closed.

Counts, pass two (rows below): 0 high, 22 medium, 24 low (46); 2 medium and 6 low in `units.json`, 20 medium and 18 low in `gloss.json`. Nothing unresolved that needs `t`.

## Changes — units.json (all `n`, none to `t`, `l` or `i`)

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 694 · `n` | low | ἀνστήσεσθαι "in the epic form without the second α": imprecise (the form is ἀναστήσεσθαι with ἀνα- shortened). | "with ἀνα- shortened to ἀν-". |
| 692 · `n` | low | "ἄνακτος ‘lord’ agrees with Εὐηνοῖο": the Greek has Εὐηνοῖο Σεληπιάδαο ἄνακτος and ἄνακτος could as well follow the patronymic; the note stated what the line does not decide. | "stands last, in the same case as Εὐηνοῖο and Σεληπιάδαο". (`i`/`l` keep "lord Euenus … Selepus’-son, the lord", a natural reading.) |
| 729 · `n` | low | "Οἰχαλιῆος being the epic form of Οἰχαλιεύς": a form of what? (it is the genitive). | "the epic genitive of Οἰχαλιεύς". |
| 734 · `n` | medium | "Τίτανος, a place-name": stated flatly; τίτανος is also the common word for chalk, gypsum (LSJ), which would suit λευκά, and the Greek does not decide. | "taken as a place-name (τίτανος is also the common word for ‘chalk, gypsum’, so the sense is not certain)". `l`/`i` keep "Titanus", as the table's κάρηνα row does. |
| 755 · `n` | low | "the water of Styx" against `l`/`i` "the Styx". | "the water of the Styx". |
| 764 · `n` | low | οἰέτεας "(οἶος ‘one’ + ἔτος ‘year’)" stated as certain; the first part is an inference. | "probably". |
| 751 · `n` | medium | "καλλίρροον ὕδωρ … the Odyssey’s καλλίρροος": no published Odyssey unit has the word (checked against all `odyssey-*.json`). | "from καλλι- ‘fair’ and ῥόος ‘stream’." |
| 742 · `n` | low | "as in the φῆρες of 1.268": 1.268 has the dative φηρσίν, not φῆρες. | "as in φηρσίν at 1.268". |

## Changes — gloss.json

Structural checks, all pass: every form of the part's `t` has an entry (451 forms: 198 already in the glossary, 253 new in `gloss.json`; none missing, none extra); no new key redefines an existing form; every new entry ≤ 230 characters, typographic ’ only, no ASCII apostrophe or backtick, no line number, no "here"; all 19 `__broaden__` entries are exactly old entry + ` · ` + new reading (checked against `iliad-glossary.json`).

| key · field | severity | what was wrong | what was done |
|---|---|---|---|
| καλλίρροον | medium | "= Attic καλλίρρουν" was given as καλλίρρους (the nominative); the neuter accusative in Attic is καλλίρρουν. | Corrected. |
| καλεῦντο | medium | "epic uncontracted": the form is the epic contraction -εῦντο (from -έοντο), not an uncontracted one. | "epic -εῦντο (= Attic ἐκαλοῦντο), unaugmented". |
| κορωνίσι | low | "epic -σι (= Attic -σιν)": not a dialect difference (ν-movable only). | Parse reduced to "fem. dat. pl., agreeing with νήεσσι". |
| νέμοντο | medium | "’dwelt in, worked’": "worked" is not the table's νέμομαι ("inhabit") and not the sense in the Catalogue. | "dwell in, inhabit, hold; ’inhabited’". |
| ἔργα (broadened) | medium | The added reading gave "’worked the farmland’" for ἔργα νέμοντο. | "tilled land, farmland (ἔργα νέμοντο ’inhabited the farmlands’)". Old entry kept whole. |
| λωτὸν | medium | "a clover-like fodder plant": the entry decided the plant, and the unit's note says which plant is not known. | "a plant (a fruit men eat in the Odyssey, fodder for horses in the Iliad; which plant is uncertain)". |
| κλωμακόεσσαν | low | "rocky, craggy" against the draft's "stony" and the note's "‘terraced’ another reading". | "stony or terraced (sense uncertain; from κλῶμαξ ‘heap of stones’)". |
| λεχεποίην | medium | "adj. of two endings, masc. acc. sg." decided a gender the form does not show (the -ην accusative here belongs to the epithet of Πτελεόν); also "ποία" for ποίη. | "acc. sg., agreeing with Πτελεόν"; "from λέχος and ποίη". |
| ἀγχίαλόν, ἀντρῶνα, ἴτωνά, ἀστέριον, ὀρμένιον, τρηχῖνα | medium | Genders of place names stated (Ἀντρών masc., Ἴτων fem., Ἀστέριον/Ὀρμένιον neut., ἀγχίαλος masc.): the Greek shows them only through agreeing words, and for Ἀντρῶνα/Ἀστέριον/Ὀρμένιον it shows nothing. (Ἴτωνα is felt as feminine because of μητέρα, but that is the appositive's gender.) | Gender dropped; "acc. sg." only. Also "Asterion" → "Asterium", to match `l`/`n`. |
| ἅρματα, ἅρμασιν | low | "(pl. for a single chariot)": false at 777, where the chariots are many. | Parenthesis removed. |
| ἀπομηνίσας | medium | "be angry to the end, nurse wrath against": decided the force of ἀπο-, which the note says is not certain; "having nursed his wrath" is not the English of the unit. | "be wrathful, with ἀπο- of uncertain force (‘away’, ‘utterly’) … ’having withdrawn in wrath’". |
| ἀπορρώξ | low | "outflow, trickle": "trickle" is not what a broken-off piece of a river means. | "broken-off piece, hence an offshoot". |
| ἐμβέβασαν | medium | "plpf. … with simple past force": a pluperfect of this verb has the sense of the perfect (‘stand in’), which is why it means "were aboard"; no Attic equivalent was named. | "plpf. 3 pl. (= Attic ἐνεβεβήκεσαν), with the sense ‘stood in’: ’had embarked, were aboard’". |
| ἕστασαν | low | No Attic equivalent named for a Homeric form. | "(= Attic εἱστήκεσαν)". |
| τιτάνοιό | medium | "a place-name in Thessaly (sense of the form uncertain: hill or town)": place and region from memory. | "taken as a place-name (τίτανος is also ‘chalk, gypsum’; sense uncertain)". |
| τὰρ | low | "crasis of τε + ἄρα" stated flatly; could not be confirmed beyond τίς τ’ ἄρ (1.8) and the existing τ entry ("in τ’ ἄρ with a question, ’then’"). | "τὰρ is taken as τε + ἄρα run together (compare τίς τ’ ἄρ)". |
| πρώτιστον | medium | "neut. acc. sg. used adverbially (or masc.)": the word stands in apposition to the masculine participle ἀποθρῴσκοντα, with πολύ before it; the strengthened superlative was not explained. | "the strengthened superlative πρώτιστος: ’very first’; masc. acc. sg., agreeing with the participle ἀποθρῴσκοντα (πολύ ’by far’ before it)". |
| ὄτριχας, οἰέτεας | medium | Lemmas and etymologies given as settled (ὄθριξ; οἰ- + ἔτος) and "of the mares" pinned to the line. | ὄτριχας: "ὄθριξ (lemma uncertain)", "the word is not secure"; οἰέτεας: "first part uncertain; traditional sense"; "of the mares" removed. |
| φῆρας | medium | "epic name of the Centaurs": the Greek has only the beasts (and the unit's note says the Greek does not use the name). | "wild beast (Aeolic = Attic θήρ), used of the beasts Peirithous fought, traditionally the Centaurs". |
| Θήβη, Λυρνησσός, Μύνης | medium | "a town of the Troad", "a king of Lyrnessus": from memory, not in the Greek of this part. | "a town whose walls Achilles sacked"; "a town sacked by Achilles"; Mynes "son of Euenus, struck down by Achilles". |
| Πρωτεσίλαος (2) | medium | "first of the Achaeans to leap ashore at Troy": the note itself says the Greek does not say first to do what. | "a leader of the men of Phylace and its neighbours, killed as he leapt from his ship"; the genitive entry likewise. |
| Λεοντεύς, Πολυποίτης, Πειρίθοος (2) | medium | "a Lapith leader", "king of the Lapiths": the Greek of the part never says Lapith. | "joint leader with Polypoetes"; "son of Peirithous and joint leader with Leonteus"; "father of Polypoetes". |
| Πελίας | low | "king of Iolcus": not in the Greek here. | "father of Alcestis". |
| Πηρείη | medium | "a place in Thessaly": from memory (the name is read also as Pieria in some texts). | "a place named only as where Apollo reared the mares". |
| Αἰθίκες | medium | "a people of the Pindus region": from memory. | "a people whose land the Greek does not name". |
| Βοίβη, Θαυμακίη, Μηθώνη, Μελίβοια, Ὀλιζών, Κύφος | low | "a town of Thessaly / Magnesia", "a town of Perrhaebia": the region is from Strabo, not the Greek. | Boebe "a town by the Boebeian lake"; the four of Philoctetes "a town among Philoctetes’ places"; Cyphus "a place in northern Greece" (the neighbouring Enienes and Perrhaebi are named in the Greek). |
| Κάσος, Κράπαθος | low | "near Cos", "of the Dodecanese" (a modern name); "Casos" against `l` "Casus". | "an island of the south-east Aegean"; "Casus". |
| Ἄλος, Ἀλόπη, Τρηχίς, Ἑλλάς | low | "a town of Phthia / Thessaly": the Greek groups them with Phthia and Hellas in Achilles' entry. | "a town of Achilles’ realm"; Hellas "a district beside Phthia in Achilles’ realm"; "Alos" → "Alus" (as `l`). |
| Ὑπέρεια | low | "agreeing with κρήνην" for a noun in apposition. | "in apposition to κρήνην". |
| Φηρητιάδης | low | "(patronymic, of Admetus)" stated as fact. | "usually taken to be Admetus", as the note says. |
| ποδώκης | low | Meaning "swift-footed": the Iliad table reserves "fleet-footed" for ποδώκης and keeps "swift-footed" for ποδάρκης. | "fleet-footed". |
| οἰκί | low | Lemma οἰκία (the Attic feminine singular) for a Homeric neuter plural. | Lemma οἰκίον, "neut. pl. οἰκία". |
| οἷσιν, πέλασσεν, μοχθίζοντα, ναίεσκον, σταφύλῃ, σέλινον, ἀνθεμόεντα | low | Meanings pinned to the line or to a different English than the units ("drove (them) to", "in torment", "used to dwell", "dat. of measure", "wild celery, parsley"); ἀνθεμόεντα's gender not marked in order. | "its own"; "bring near, drive to"; "toiling, suffering"; "kept dwelling"; "dat. of means" (as the note); "celery or parsley (or a plant like them)"; word order only. |
| κλυτὸς (broadened) | medium | New reading said "fem. nom. sg. (two-ending adj.)": κλυτός is a three-ending adjective, and the unit's note rightly calls the form masculine with a feminine name. | "also the masc. form used with a fem. name, nom. sg., agreeing with Ἱπποδάμεια". Old entry kept whole. |
| πτελεὸν (broadened) | medium | New reading "masc. acc. sg." (gender not shown by the Greek; the epithet λεχεποίην is -ην). | "Pteleum, a town of Thessaly; acc. sg., with λεχεποίην". |
| ἄργος (broadened) | low | "a district of Thessaly": from memory; the note says "northern Greece". | "northern Greece". |
| ἐΐσας (broadened) | low | "equal, matched … level along the back": not the unit's "well-balanced". | "’balanced, level’ (… ’balanced along the back’)". |
| ἐπὶ (broadened, new) | low | ἐπὶ νῶτον ("along the back") is not covered by the existing entry's "to" for ἐπί + acc. | Added " · also + acc. of extent, ’over, along’ (ἐπὶ νῶτον ’along the back’)". Old entry whole. |

Parses re-checked against the line and found true (no change): the whole of the other new entries, among them δεύονθ, διαπορθήσας, δυσηχέος, δυσχείμερον, ἐξείλετο, ἐπιρρέει, ἐρεπτόμενοι, ἐτίσατο, ἡγήσαιτο, ἡγείσθην, ἡγεμόνος, ἐμνώοντο, ἐλέλειπτο, κεῖτ/κεῖτο, πεπυκασμένα, φορεούσας, φορέεσκον, μάχοντο, μήνιεν, ὦσε/ὄρνιθας, θρέψ, ἔλαυνε, ἔννεπε, ἀνστήσεσθαι, ἀποθρῴσκοντα, ἰητῆρ, ἀγαθὼ, παῖδε, υἷε, ἀρχόν, ἄρισται, ἀρείων, ἱέντες, μοῦσα, πτολιπόρθῳ, Ὀϊλῆϊ, Οἰχαλίη; the 19 broadened readings other than those above (αὐτῶν, εἰνοσίφυλλον, παρ, περὶ, ποδάρκης, πρότερος, τίς, τὸ, τῆς, ἔνθα, ὄφρ, ὑπ, ὑπὸ) fit the line they cite and are exactly old + ` · ` + new. The known (already-glossed) forms were each read against their line in this part; the existing entries cover the use except as broadened.

## Findings refused (pass two)

1. **Ἴτων / Ἀντρών genders.** Not kept as the glosser gave them; refused to *state* a gender (see changes). The Greek shows Ἴτων only as the appositive of μητέρα and Ἀντρών not at all.
2. **Thessaly for Tricca, Ithome, Argissa, Gyrtone, Orthe, Elone, Oloosson, Ormenium, Asterium, Hypereia, Pherae, Iolcus, Glaphyrae, Phylace, Pyrasus, Pelion, the Peneius, Magnesia.** Kept: well known from the public-domain aids (Strabo, LSJ, Autenrieth) and the part's own `about`. Only claims narrower than that, or contradicted by nothing in the text but unsupported by it, were softened.
3. **Δάρδανος "of the Trojan people … used as an adjective with ἀνήρ".** Kept: Δάρδανος ἀνήρ is "a Dardanian man" (an adjective in Homer as in LSJ), matching the note.
4. **λωτός.** Kept "lotus" in `l`/`i`, as in pass one (finding 4).
5. **Ἐνιῆνες, Περαιβοί "a people of (northern) Greece / Thessaly".** Kept (Autenrieth).
6. **ποδώκης vs the Odyssey's "swift-footed".** Still the pass-one unresolved item 2 (convention clash); the gloss now follows the Iliad table.
7. **Notes 678 and 692 ἄνακτος.** `l`/`i` of 678 ("Thessalus, Heracles’-son, the lord"; "lord Thessalus, the son of Heracles") and of 692 take ἄναξ with the first name; the note at 678 already says only "after it". The English is one fair reading; not changed.
8. **Units in which the note says "the Odyssey’s epithet" etc.** Checked against the published Odyssey units: ἀρηΐφιλος Menelaus (odyssey-072), κορωνίς of ships (odyssey-093), ποντοπόρος of ships (odyssey-057, -062, -063), πτολιπόρθιος (odyssey-044, -070), ἰητῆρα (odyssey-016/-085 area), κοίρανος (odyssey-088), καλλιγύναικα of Sparta (odyssey-065) are true; the καλλίρροος claim was not (changed above).

## Unresolved (needs the caller or the owner)

1. **`ἕποντο` entry in `iliad-glossary.json` is wrong.** It reads "impf. 3 pl. mid., augmented (ἕποντο = εἵποντο)"; ἕποντο is the *unaugmented* form (εἵποντο is the augmented). Not rewritten (additions only, per the runbook; broadening would have to keep the false text whole). The unit notes at 710 etc. say "unaugmented", which is true; the glossary entry contradicts them. A rewrite is for the owner.
2. **ποδώκης convention clash** — as pass one.
3. **Note lengths** — as pass one (WARN only).
