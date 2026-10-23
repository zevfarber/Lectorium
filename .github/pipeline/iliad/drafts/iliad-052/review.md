# Review of iliad-052 (Iliad 9.1–113), pass 1 (units)

`units.json` (77 units) read against `runbook.md` section 2, all of `conventions.md` (the Iliad table was checked row by row for every word of the part, including lines 1251–2699 that the drafter skipped, and the Odyssey table, which is binding too, was checked the same way), `packet.md`, `new-renderings.md` and the published parts in the repository root. Cross-references were looked up in the shipped Iliad and Odyssey parts: 1.189, 1.275–284, 1.356, 2.79, 2.110–141, 2.409, 2.419, 2.434, 2.512, 3.84, 4.370, 5.498, 5.740, 7.30, 7.282, 7.323–326, 7.379, 7.440–441, Odyssey 1.149, 12.291, 13.477. 8.553–565 is not in a published part and was read in the archive (`source/iliad-monro-allen1920.json`).

`t` is untouched (compared unit by unit with the original file after every edit, and the `ln` of every unit matches the edition's line it opens in). `units.json` was edited in place by script; its format (indent 1, no trailing newline) is unchanged. Every note is still inside 25–110 words (longest 100) and has no backtick. Severity scale as in iliad-050: **major** = false statement in a note, missing/wrong speech mark, or `l`/`i` that breaks a fixed house rendering; **minor** = true but imprecise, misleading, or not following a shipped line as far as the sentence allows; **nit** = punctuation or wording consistency only.

## Changes made

| Line (unit) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 111b–113 (unit 76, last) | `l`, `i`, `n` | **major** | Nestor's second speech was left open: no closing ” in `l` or `i`, and the note said "the part ends in the middle of his speech". The speech ends at 113: the first line of iliad-053 (9.114) is narration, `τὸν δ’ αὖτε προσέειπεν ἄναξ ἀνδρῶν Ἀγαμέμνων`, and Agamemnon's answer follows at 115. This is the same mistake as the open question in QUESTIONS.md for iliad-007 (2.83). | ” added at the end of `l` ("gentle ones.”") and `i` ("gentle words.”"); note now reads "Nestor’s proposal at last, and the end of his speech: Agamemnon answers at 114." The part now has 4 “ and 4 ” in each layer. |
| 96 (unit 66) | `n` | **major** | "Nestor’s second speech starts here and runs on into the next part, so there is no closing mark in this one." False for the same reason. | Now "Nestor’s second speech, 9.96–113, starts here and ends with the last line of this part." (The rest of the note, "The address is that of 2.434", checked: 2.434 is the same line.) |
| 6–7 (unit 3) | `l` | **major** | ἅλα rendered "the sea". The Odyssey table fixes ἅλς as "the salt-sea" in `l` ("the sea" / "the salt sea" in `i`), and the shipped Iliad `l` has "salt-sea" (iliad-003, 1.308, 1.314; iliad-004, 1.409). | `l`: "out beyond the salt-sea it has poured". `i` ("beyond the sea") is as the table allows. Note quotes the new wording. |
| 15 (unit 8) | `l`, `i`, `n` | **major** | δνοφερόν rendered "dusky". The Odyssey table fixes δνοφερός as "gloomy" (15.50) and keeps "dusky" for ἐρεμνός (11.606, 24.106; the Iliad table at 4.167 follows it). | "gloomy water" in `l` and `i`; note ‘gloomy’. |
| 65 (unit 43) | `i` | **major** | νυκτὶ μελαίνῃ rendered "black night" in `i`. The Odyssey table fixes "black night" for `l` and "dark night" for `i`. The line is also Odyssey 12.291 word for word (printed `ἦ τοι` there, `ἤτοι` here, so the validator's letters-only key does not see it; the packet did not list it), shipped in odyssey-060 as `l` "But truly now let us obey black night / and make ready our supper" and `i` "But for now let us give way to dark night and make ready our supper". | `i`: "But for now let us give way to dark night and make ready our suppers;". The note adds one sentence naming Odyssey 12.291 and saying its English is kept. |
| 65 (unit 43) | `l` | minor | "But indeed now … prepare our suppers": the shipped `l` of the same line has "truly" and "make ready" (ἐφοπλίζω is the same family as ὁπλίζω). | `l`: "But truly now let us obey black night / and make ready our suppers;". |
| 89 (unit 62) | `l`, `i`, `n` | **major** | ἀολλέας rendered "all together". The Iliad table fixes ἀολλέες (5.498) as "in a close mass" and turns down "all together" ("reserved for ἅμα / ἀθρόοι"); the Odyssey's "all together" is therefore not carried over, as in the table. | `l`: "the elders, in a close mass, of the Achaeans led"; `i`: "led the elders of the Achaeans, in a close mass, to his hut"; note ‘in a close mass’, as at 5.498. |
| 4–5 (unit 2) | `n` | minor | Hand scan of line 5 (below): the note already said Βορέης must be read with first syllable long and -εη- run together, but not that τε before Θρῄκηθεν is counted long. The line is irregular in both places. | The one sentence on line 5 now reads "Line 5 is metrically irregular as transmitted: Βορέης has to be read with its first syllable counted long and its -εη- run together, and the short τε before Θρῄκηθεν has to be counted long, in the fourth foot." |
| 6–7 (unit 3) | `n` | minor | "ἔχευεν … a simile says what happens every time, so the English uses the present", but `l` has "it has poured". | "so the free English uses the present" (`l` keeps the past, as the literal layer does for the shipped κατέλυσε). |
| 52 (unit 34) | `i` | minor | "Nestor the horseman rose and spoke": the house form is "the (Gerenian) horseman Nestor" in every shipped line (iliad-010, -011, -013, -024, -042, -043, -047) and the drafter's own row in `new-renderings.md` says it "keeps horseman Nestor". | `i`: "And among them the horseman Nestor rose and spoke:"; the `new-renderings.md` row brought into line. |
| 61–62 (unit 41) | `l`, `n` | minor | μοι was translated twice in `l` ("dishonour for me / my word") while the note says μοι goes with μῦθον to give "my word". | `l`: "and no one would dishonour for me / the word, not even lord Agamemnon."; note: "‘my word’ in the free English". |
| 71 (unit 50) | `l`, `i`, `n` | minor | εὐρέα πόντον rendered "the broad sea". The shipped line with the same words (iliad-038, 6.291) has "the wide sea" in both layers; "broad" belongs to εὐρέα νῶτα. | "wide sea" in `l` and `i`; note ‘wide’. |
| 77 (unit 54) | `n` | minor | "the enemy fires of the line before": the fires (πυρὰ πολλά) stand in the same line, 77, in the previous clause. | "of the clause before". |
| 101 (unit 69) | `l` | minor | "whenever to any man the heart bids / to speak": τινα is the accusative object of ἀνώγῃ (the note says so), but "to any man" reads as a dative. | "whenever any man the heart bids / to speak for good;". |
| 103 (unit 71) | `l` | minor | "But I shall speak as it seems …": the note says ἐρέω is ‘I shall say’, and the same line stands in odyssey-112 (Odyssey 23.130, `τοιγὰρ ἐγὼν ἐρέω ὥς μοι δοκεῖ εἶναι ἄριστα`) with `l` "I shall say as it seems to me to be best". | `l`: "But I shall say as it seems to me to be best." `i` left (it already follows the Odyssey sense). |
| 45 (unit 29) | `l` | nit | The Greek ends in a full stop (`διαπέρσομεν.`) and `i` has one; `l` had ";". | `l` ends "until we sack Troy." |
| 79 (unit 56) | `l`, `i` | nit | Same: Greek ends `.`; both layers kept the ";" of the shipped 7.379, where the Greek has `·`. (The Greek here differs by `ἠδὲ πίθοντο`, so the whole-unit rule does not bind.) | Both layers end with "." (wording still the shipped 7.379 English). |
| (file) `new-renderings.md` | Nestor row | — | Out of step with unit 34. | `i` column corrected as above. |

Counts: 6 major rows (5 distinct findings: the open speech is one finding in two units), 9 minor, 2 nit.

## Hand scan of the flagged line

5 `Βορέης καὶ Ζέφυρος, τώ τε Θρῄκηθεν ἄητον`: Βο–ρέης (Βο lengthened in the longum of foot 1, -εης one syllable by synizesis) | καὶ Ζέ⏑φυ⏑ | ρος‖ τώ (ρος long by position before τ) | τε Θρῄ (short τε counted long before Θρ, the longum and the second long of a spondee) | κη–θεν⏑ ἄ⏑ | η–τον×. No other division gives six feet, so all three licences are needed; the main caesura is masculine, after ρος. The program agrees (`UNRESOLVED`, lengthening in foot 1, synizesis, τε long in foot 4). The irregularity is real and now stated in the note. No other line is flagged.

## Checked and found true (no change)

- **Grammatical labels and positional claims in every note**, one by one against the line: duals (ὀρίνετον, ἄητον, ἐλθόντ’, νῶϊ), βεβολήατο (pluperfect passive, -ήατο = -ηντο), ἔχον / ἔχε / ἔπε’ / δῶκε / τίθει (augmentless), tmesis at 13, 87, 89, 80, article as pronoun at 1 and 95, ἐπέσσυται (perfect passive of ἐπισεύω), ἑστᾶσ’ (3 pl. perfect), εἴξας, ἑλών, ἀπούρας (aorist participles), γενεῆφιν (-φιν), λεξάσθων (3 pl. aorist imperative middle), ἀγρομένων (syncopated aorist participle), πείσεαι, ἕξεται, ἄρξομαι + genitive, χρεώ with accusative of person and genitive of thing, γηθήσειε (aorist optative), ἐξείπω / διίξομαι, ἵκεο, ἔπλευ, βάζεις (with the persons spoken to in the accusative). Unit 25's relative ὅ τε κράτος … is neuter by attraction to its predicate κράτος: true as worded.
- **Cross-references**: 4.370 (Agamemnon's taunt, iliad-025), 1.275–284 (Nestor's advice, iliad-003), 1.356 (`ἑλὼν γὰρ ἔχει γέρας`), 2.434 (same address), 2.512 (Ascalaphus and Ialmenus of Orchomenus, iliad-012; the unit that holds it opens at 511), 7.282, 7.323–325 and 7.326 (iliad-044, same English), 7.379 and Odyssey 13.477 (`ἠδ’ ἐπίθοντο`, same English), 7.30 (τέκμωρ "end", iliad-041), 7.440–441, 2.409, 2.419, 3.84, 1.189, 2.79 (the address Nestor used), 2.110–141, 8.553–565 (Trojan fires, archive), Odyssey 1.149. Inside the part: 5, 13, 25, 27, 39, 47, 85, 94, 96 are the lines the notes point to and each says what the note says.
- **Greek to `l`, `l` to `i`, word by word**, all 77 units: no wrong case relation, tense or mood other than those changed above. Particles omitted in `l` (ἄρα, τε) are as in the shipped lines.
- **Shipped repeats**: units 11–17, 19, 33, 45, 64, 65 repeat the shipped `l` and `i` exactly (checked by script against all published Iliad and Odyssey units with the same letters); 10, 63 and 66 follow the shipped lines (2.79, 2.110–112, Odyssey 1.149, 2.434). Fuzzy matches of single lines against every shipped line (ratio ≥ 0.7) were also run; the ones that matter are those changed above.
- **House renderings checked against the whole table**: δαιμόνιε, λιγύφθογγοι, κάρη κομόωντες, ἱππόδαμος, ἀγκυλομήτης, σχέτλιος, ἄτη, κράτος, ἀλκή / ἀνάλκις / ἀπτόλεμος, ἀφραδής, ἄνεῳ ἦσαν, τετιηότες, ἀκήν, ἔλπομαι (iliad-043/044, odyssey-104), εὔχομαι εἶναι (2.82), διογενές, χώομαι, ἀτιμάζω / τίω, κρείων, κύδιστε, ἱππότα, μεγαλήτωρ, ἀγασσάμενοι (7.404 "in admiration"), θέμιστες (see below), μενοεικής, λιγύς, μελάνυδρος (Odyssey 20.158), ἰχθυόεις (Odyssey), κελαινός "dark", δῆμος, κλισίη "hut", δόρπον "supper", ἀεικής "unseemly", ἀθέμιστος "lawless", δήϊος, ὑφαίνειν μῆτιν, ἐϋφρονέων, πυκινή (2.55), ἀρεσσάμενοι, ἀγανός / μειλίχιος "gentle", δάκρυ χέων, ποιμένα λαῶν, Νεστορίδης, φοιτάω, ἕκαστος, ἄριστος, καρτερός.
- **Speech marks**: openings at 17 (Agamemnon), 32 (Diomedes), 53 (Nestor), 96 (Nestor); closings at 28, 49, 78, and now 113; each on both `l` and `i`; `mark` on the first unit of each speech; no mark inside; the preceding speech (iliad-050's last speech, Hera, ends at 8.468 with its own mark) leaves unit 0 correctly unmarked. Speech introductions end with ":" (units 9, 19, 34, 65).
- `p` marks at units 0, 5, 17, 33, 56, 62 = ¶ at 1, 9, 29, 50, 79, 89.
- **Remembered English**: no phrase in `i` arrives from a known translation except the forced calques noted below; the ones that read familiar ("fell hushed and silent", "tamer of horses", "Strange man", "wide-streeted") are the table's.

## Findings considered and refused

| Line | Finding | Reason refused |
|---|---|---|
| 96–113 (units 66, 76) | The brief for this review said Nestor's second speech "runs into iliad-053 — correct". | Not correct, see the two **major** rows above: 9.114 is `τὸν δ’ αὖτε προσέειπεν ἄναξ ἀνδρῶν Ἀγαμέμνων` (archive and plan.md both show iliad-053 opens with it), so Nestor stops at 113. If the run owner still wants the speech left open, revert unit 76 `l`/`i` and the notes of units 66 and 76; the mistake is the one QUESTIONS.md already records for iliad-007. |
| 30 (unit 18) | `l` "For a long while …" for `δὴν δ’` may look like γάρ. | It is the duration phrase "for a long while", with δέ left to the punctuation; `i` is the same. |
| 55 (unit 36) | "find fault with" for ὀνόσσεται may be a remembered phrase. | The note derives it from ὄνομαι "find fault with, scorn"; the plain English of the Greek, no whole phrase lifted. |
| 61 (unit 40) | "subjunctive of urging" for ἐξείπω (1 sg., "let me speak out") beside "will speak out" in `l`. | The note gives both; the house uses "will" for the volitive subjunctive. |
| 1 (unit 0) | "were holding watches" in `l` for φυλακὰς ἔχον. | Imperfect, literal; `i` "kept their watches". |
| 99 (unit 67) | θέμιστας is "rules of right" here, but iliad-009 (2.206, the same words) ships "the ordinances". | The table (5.761) and the Odyssey (9.112) fix "rules of right"; the shipped 2.206 is out of step. Kept, and iliad-009 should be corrected when its owner allows. |
| 63 (unit 42) | ἀφρήτωρ ἀθέμιστος ἀνέστιος as "clanless, lawless, hearthless" may be a remembered triplet. | Each member is a forced calque of an ἀ-privative; "lawless" is the Odyssey's, "hearthless" and "clanless" are the only honest renderings of ἀνέστιος and ἀφρήτωρ; the reasoning is in `new-renderings.md`. |
| 42 (unit 27) | ἐπέσσυται "driven" in `l` and "set on" in `i` although the table's 6.361 row turns down "is set". | The same collocation `θυμὸς ἐπέσσυται` at 1.173 (iliad-002) ships "is driven to it" / "is set on it"; 6.361 is a different thing (a heart rushing to help). Unit 27 follows 1.173. |
| 39 (unit 25) | The note says the neuter relative ὅ τε κράτος … "agrees with κράτος". | True as attraction to the predicate κράτος; wording kept. |
| 29, 50 (units 17, 33) | End punctuation of units 17 and 33 (";" in `l` and `i` against Greek `.`). | Forced: their Greek letters equal shipped units (9.29 = iliad-017, 9.50–51 = iliad-045), so the validator requires the shipped English. |
| 92 (unit 64) | `l` ends ";" for Greek `·`, `i` ends "." | The shipped iliad-044 English, required. |
| 77 (unit 54) | `i` "Who could be glad of this?" for `τίς ἂν … γηθήσειε;` | "could" for ἂν + optative is within the force of the Greek; the note says "would". |

## For the glosser (read only; `gloss.json` does not exist yet)

- δαίνυ (70): `odyssey-forms.json` says "impf. 3 sg."; here it is the present imperative 2 sg. (the note says so); broaden.
- ὀρίνετον (4): the odyssey form is "pres. 2 dual", here it is 3 dual (with δύο ἄνεμοι).
- ἔτισαν (110): the Odyssey entry is τίνω "pay"; here it is τίω "honour".
- δνοφερὸν (15): "gloomy" (not "dusky").
- ἀολλέας (89): house "in a close mass".
- πεπνυμένα (58), πολέεσσι, ὑποδεξίη (rare noun), ἐπιδημίου (from δῆμος) need their parse as in the notes.

## Pass 2 (gloss)

`gloss.json` (145 novel forms plus 17 `__broaden__` entries, 19 after the two added below) read against the Greek in `units.json`, the entry format of `conventions.md` / the Odyssey conventions, and `known-forms.json`. Checked by script: the keys equal `novel-forms.json` exactly; no entry is 230 characters or longer (broadened entries are exempt, being the old entry whole plus the new reading); no ASCII apostrophe or backtick, no "here", no line number; every broadened entry begins with the old entry verbatim followed by " · ". Every token of every `t` is a key of either `known-forms.json` or `gloss.json`. Every parse (case, number, gender, tense, mood, voice, lemma) was then read against its line. `units.json` and its notes were not touched: no gloss finding showed a note or label to be wrong. `gloss.json` was edited in place by script (same indent, same key order; the two new `__broaden__` keys are last).

### Changes made

| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| ἔραται | minor | "epic (= Attic ἐρᾶται)": Attic has no such form to equate; ἔραται is the athematic 3 sg. of ἔραμαι, beside the thematic ἐράω (Attic ἐρᾷ). | "pres. 3 sg. mid., epic athematic ἔραται (beside ἐράω, Attic ἐρᾷ): ’loves’". |
| ἵκεο | minor | Tense missing from the parse ("2 sg. mid."); the form is the aorist (ἱκόμην), and the gloss ’you reached’ is a past. | "aor. 2 sg. mid." |
| ἠμάτιαι | minor | "used as an adverb": the form is the predicative adjective agreeing with νῆες ("the ships … day by day"), not an adverb. | "predicative with the subject (νῆες): ’day by day’". |
| κρείοντος | minor | The only occurrence in this part is the proper name Κρείων (father of Lycomedes), but the entry led with "ruler, lord" and gave the name as an afterthought, with the parse stated once for both. | Common noun first, then " · also the proper name Κρείων, Creon (father of Lycomedes); masc. gen. sg." |
| βοᾶν | nit | "in an indirect command after μή": the infinitive depends on κελεύων and is negated by μὴ δέ (a negative command, not an indirect command after μή). | "negated by μὴ δέ, depending on κελεύων: ’not to shout’". |
| εὕρωμεν | nit | Gloss ’we find, until we find’ is muddled. | ’(until) we find’. |
| ἐμὸς (`__broaden__`) | minor | Known entry "agreeing with δαήρ" does not cover its use with πάϊς (ἐμὸς … πάϊς). | Old entry whole + " · also masc. nom. sg., agreeing with πάϊς: ’my own’". |
| ἐσθλῆς (`__broaden__`) | minor | Known entry "with δαιτός" does not cover its use with an understood βουλῆς (ἐσθλῆς καὶ πυκινῆς). | Old entry whole + " · also fem. gen. sg., agreeing with an understood βουλῆς: ’of good (counsel)’". |

Counts: 0 major, 6 minor, 2 nit. (No gloss finding concerned `units.json`.)

### Checked and found true (no change)

- **Attic equivalents from memory, verified by grammar.** ἀπτόλεμος: the epic πτόλεμος is the epic form of πόλεμος (the same π-τ- onset as in πτόλις), so ἀπτόλεμος = ἀ-πόλεμος, Attic ἀπόλεμος: true. δήϊος: the Ionic-epic form of the adjective whose non-Ionic form is δάϊος (ᾱ becomes η in Ionic, and ϊ after it); the entry says only "(= δάϊος)", claims no Attic prose form, and is true as worded.
- **Other equivalences**: εἰλήλουθμεν (Attic ἐληλύθαμεν), βεβολήατο (ἐβέβληντο), κήαντο, μενοεικέα (-ῆ), ἀφαρῆά (-έα), ἀρεσσάμενοι, ὀνόσσεται, πολέεσσι, ἔπεσσι, στήθεσσι, γενεῆφιν (-φιν case), κούροισιν (Attic κόροις), ἀπεμυθεόμην, ἀφραδέοντι (ἀφραδοῦντι), σαώσει (σώσει), πείσεαι / ἔλπεαι (-ῃ), κρηῆναι (κρᾶναι), τείχεος, πένθεϊ, φραζώμεσθ’, ἐφοπλισόμεσθα, all true.
- **Case, number, gender**: every agreement claim checked against its line (αἰγίλιπος with πέτρης, δνοφερὸν with ὕδωρ, κρυόεντος with φόβου, ἀτλήτῳ with πένθεϊ, ὀρυκτὴν with τάφρον, ἰχθυόεντα with πόντον, ἑτοῖμα with ὀνείαθ’, ἡμέτερόν with νόον, μενοεικέα with δαῖτα, ἀπτολέμους with υἷας, ἐπιδημίου with πολέμου, μελάνυδρος with κρήνη, ἀγανοῖσιν with δώροισιν); φόβου as genitive depending on ἑταίρη; χρεώ with accusative of person and genitive of thing.
- **Tense, mood, voice**: duals ὀρίνετον, ἄητον; subjunctives (διαπέρσομεν short-vowel, εὕρωμεν, βουλεύσῃ, βουλεύῃσθα, ἄρχῃ, ἀνώγῃ, ἐξείπω volitive, χολωθῇς prohibitive, πεπίθωμεν, φραζώμεσθ’); optatives (γηθήσειε, εἴης, ἀτιμήσει’ for ἀτιμήσειε); futures (λήξω, ἄρξομαι, ἕξεται, πείσεαι, μενέουσι, σαώσει, διαρραίσει, διίξομαι, νοήσει, ὀνόσσεται); participles (ἀγρομένων syncopated, χωομένου, εἴξας, φὰς, προκείμενα, τετιηότες); λεξάσθων 3 pl. aorist imperative middle; ἔπλευ = ἔπλεο; all agree with the line.
- **Meanings against `l` and `i`**: no entry contradicts the English of its unit apart from the points changed above. (Pass 1 already changed "dusky" to "gloomy", ἅλα to "salt-sea", ἀολλέας to "in a close mass"; the entries for δνοφερὸν and ἀολλέας already say so.)
- **`__broaden__`**: all 17 new readings checked against their lines (βουλῇ 53; δαῖτα 70, 89; εἰπεῖν 101; κέ 61; κε 48; καθ 107; μέσον 87; πάρ 43; πολέμου 63; πολλὸν 6; σέο 97, 102; τάφρου 87; ἀγαθόν 101; ἀνάλκιδας 40; ἄριστα 103; ἐλθόντ 4 (dual, with ἄνεμοι δύο); ὥς 42 and 103): each is a true reading in its line, each begins with the old entry whole, and each is joined with " · ".
- **Known forms**: all 393 distinct known tokens of the part were run through their existing entries; the ones whose use is covered by a general reading (περί, ἐπ’, τοῦ in ἐκ τοῦ, κεν in a general relative clause, ἂν with ὡς and with the optative, τίς in οὔ τίς, εἰς ὅ κέ περ, ὥς κέν μιν) were left alone. The only two not covered were ἐμὸς and ἐσθλῆς (above).

### Findings considered and refused

| Form | Finding | Reason refused |
|---|---|---|
| ἧδ | The edition prints ἧδ’ (circumflex), but elided ἥδε would be ἥδ’. | `t` is the edition of record and may not be touched; the entry parses the word correctly as ὅδε fem. nom. sg. elided. Left. |
| ἀτιμήσει | The key also fits the future 3 sg. of ἀτιμάω. | The only occurrence is the elided optative (ἀτιμήσει’, with κέ); the entry says so. A future reading is not needed in this part. |
| ἄητον | Third dual of the imperfect would regularly end in -την, not -τον. | Homer has ἄητον as the 3 dual; the entry says "impf. 3 dual, unaugmented", which is the usual lexical statement. |
| ὀρίνετον, ἄητον | "(of two winds)" is a context remark. | It names the grammatical subject of the dual, not a line, and is not pinned to a line number. Kept. |
| ἔτισαν | Second reading τίνω ’paid for’ is not needed here. | Homograph with the same aorist form; the glosser's rule is to give both readings of a genuine homograph. Kept. |
| κέν (known) | Existing entry does not list "with the subjunctive in an indirect question" (ὥς κέν μιν … πεπίθωμεν). | The generic entry is not false for this use and the construction is already fixed by the entry for ὥς (broadened earlier: "ὥς κε + subj. in an indirect question"). Not broadened. |
| νοήσει | Could be an aorist subjunctive (short vowel) rather than a future. | After οὐ γάρ τις … ἄλλος the future is the natural reading and the one the entry gives. Kept. |
