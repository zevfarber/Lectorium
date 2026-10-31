# iliad-117 review (Iliad 18.97–201) — two passes

Pass 1: `units.json` only (Greek → `l` word by word, `l` ↔ `i`, notes against the line, cross-references, remembered English, quotation marks and marks, house-renderings table and the published parts, Iliad and Odyssey). Pass 2: units re-read after the pass-1 edits, plus `gloss.json` (every new parse checked against the line; every known form checked against its existing entry in `known-forms.json`). Edits to `units.json` and `gloss.json` were made by script; `t` is byte-identical before and after (checked, together with title, titleEn, part, about). `l` still has one `\n` for each `\n` in `t`; no backtick or straight apostrophe in any note, `l`, `i` or gloss entry. No scansion flags in the packet, so no line was scanned by hand. Paragraph marks (`p`) agree with the nine ¶ lines of the packet; speech marks and “ ” are right on every speech (98–126 Achilles; 128–137 Thetis; 140–144 Thetis to the Nereids; 170–180 Iris; 182; 184–186; 188–195; 197–201). Thetis’ speech that ends the previous part closes with ” in iliad-116, so unit 18.97 correctly opens without a mark. Identical Greek gets identical English inside the part (18.183 = 18.196). `build` and `validate` were not run, nothing committed.

Counts by severity (a finding that touches several places is one finding): **high 2 · medium 24 · low 22 · total 48** (units, rows 1–26: 2 high, 12 medium, 12 low; gloss, rows 27–48: 12 medium, 10 low).
Severity key: high = wrong Greek→English, or a note that misleads the reader about the text; medium = false cross-reference or false claim, house-table violation, wrong/missing reading in the glossary; low = consistency, wording, hedging.

## A. Changes to `units.json`

| # | Line · unit | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 18.146 (ἐνείκαι) | l, n | high | The note called ἐνείκαι an infinitive after ὄφρα (‘to bring’) and `l` followed it. The printed accent (ἐνείκαι, not the infinitive ἐνεῖκαι) and the ὄφρα clause show the Aeolic aorist optative of φέρω, 3 sg. (= ἐνέγκοι), in a purpose clause after the past ἤϊεν. | `l` “went, so that she might bring her dear son famous armour.”; the note now says optative and why. `i` (“to bring”) kept, since English gives the purpose either way. |
| 2 | 18.189 | l | high | “before I myself, her coming, see with my eyes” made αὐτήν (accusative, “her herself”) into “I myself”; the note had it right. | “before I see her herself, having come, with my eyes;” |
| 3 | 18.98, 18.171 | l, i, n | medium | ἐπαμῦναι and ἐπάμυνον rendered “come to the aid of / stand by and help”. The table fixes ἐπαμύνω as “come to the defence of” (turning “aid” down as a first draft; iliad-033, 039, 075, 082, 104). | Both units: “defence” in `l`, `i`, `n` (18.98 `i`: “to come to my companion’s defence as he was killed”). |
| 4 | 18.112 | l | medium | θυμὸν … φίλον: `l` dropped φίλον. The table keeps “dear” in `l` and drops it in `i` only. | “having subdued the dear heart in our breasts”. |
| 5 | 18.115, 18.117 | l, n | medium | κῆρα (singular) was “death-spirit”. The table has singular κήρ as “death-fate” (3.32, 3.360, 3.454) and keeps “death-spirits” for the plural. | “death-fate” in both `l`; note on 18.115 changed; `new-renderings.md` row corrected. |
| 6 | 18.124 | l, i, n | medium | ἁδινὸν στοναχῆσαι: “thickly … deeply”. The table fixes the adverb ἁδινόν as “heavily” (ἁδινὸν γοόωσα “sobbing heavily”). | “heavily” in `l` and `i`; note says the adverb of ἁδινός ‘thick, thronging’, here ‘heavily’. |
| 7 | 18.142 | l, i, n | medium | μακρὸν Ὄλυμπον was “great Olympus”; the table fixes “tall Olympus” in both layers (1.402). | “tall Olympus” in `l` and `i`; note names μακρόν ‘tall’. |
| 8 | 18.184 | l, i, n | medium | κυδρὴ παράκοιτις was “august consort”, a departure from the Odyssey’s Διὸς κυδρὴν παράκοιτιν “the glorious consort of Zeus” (odyssey-056) and from the table’s κυδρός “glorious” (11.576). The stated reason (keep apart from φαίδιμος) is not a reason the Iliad context forces. | “the glorious consort of Zeus” in both layers; note rewritten; `new-renderings.md` row rewritten (“august” recorded as the first draft). |
| 9 | 18.185 | l | medium | Κρονίδης ὑψίζυγος: `l` had the `i` form “who sits on high”. The shipped `l` is “the son of Cronus, sitting on high” (iliad-022, 041, 069), as `new-renderings.md` already claimed. | `l` “and the son of Cronus, sitting on high, does not know”. |
| 10 | 18.187 | n | medium | “the same as at 1.84 and 3.215”: the other occurrence is 1.215 (iliad-003 is 1.206–311); there is no Iliad 3.215 formula. | “1.84 and 1.215”. |
| 11 | 18.188 (πῶς τὰρ ἴω μετὰ μῶλον;) | l, n | medium | `l` “among the toil of Ares” and the note “μῶλον Ἄρηος is the fixed phrase”: the line has only μῶλον; Ἄρηος is not there. | `l` “How then am I to go among the toil?”; note says Ἄρηος is not said here and that `i` spells it out as ‘the toil of battle’. |
| 12 | 18.194 | l, i, n | medium | δηϊόων was “slaying / laying men low”; the table (iliad-065, 084, 113) has δηϊόω “cut down”, and the known gloss entry says so. | `l` “cutting down”, `i` “cutting men down with his spear”, note ‘cut down’. |
| 13 | 18.130 | n | medium | Note read ἀλλά τοι as “but, mark you” while `l`/`i` (and the note at 18.197) take τοι as “your”: the note contradicted its own `l`. | Note: enclitic τοι ‘to you’, read as ‘your’ armour (the particle ‘mark you’ is also possible). |
| 14 | 18.154 | i | medium | φλογὶ εἴκελος ἀλκήν: `i` “as fierce as flame” loses ἀλκήν; the table has εἴκελος ἀλκήν “like … in might” in both layers (4.253). | `i` “like flame in might”. |
| 15 | 18.97 | i | low | ὀχθήσας … μέγα: `i` “Deeply troubled”; the published four have “Greatly troubled” for the same Greek. | “Greatly troubled”. |
| 16 | 18.101 | n | low | “the main clause is held back to the next lines” was vague. | “a long sentence of reasons that is not completed until the wish at line 107”. |
| 17 | 18.105 | l, i | low | καὶ ἄλλοι: “also” not rendered. | “others too who are better”. |
| 18 | 18.107 | i | low | ἀέξεται: `i` “swells”, note and gloss “grows”. | “grows”. |
| 19 | 18.117 | l, n | low | ὅς περ: `l` “he who”, note “who although”, `i` “though”. | `l` “he who indeed”; note: ὅς περ ‘he who indeed’, `i` makes it “though”. |
| 20 | 18.120 | i | low | ὁμοίη: `l` “like”, `i` “the same” (stronger). | “a similar fate”. |
| 21 | 18.128 | i | low | ναὶ δὴ ταῦτά γε: the house `i` is “Yes indeed” (iliad-003, 047, 059, odyssey). | “Yes indeed, child, that is true:”. |
| 22 | 18.129 | n | low | The note quoted “τειρομένοις ἑταίροισιν”; the line has ἑτάροισιν. | Spelling corrected. |
| 23 | 18.151 | n | low | “the condition is given at line 165”: εἰ μή stands at 166 (165 holds the apodosis). | “line 166”. |
| 24 | 18.158 | i, n | low | ἀλκὶ πεποιθώς: `i` “strength” (the table has ἀλκή “might”, 5.299); the note called ἐπαΐξασκε and στάσκε “iterative imperfects” while the glossary says aorist-based. | `i` “might”; note “iterative forms with the ending -σκ-”. |
| 25 | 18.160 | l, i, n | low | χάζετο: “give way / fell back”; the published word is “draw back”. | “draw back” (`l` “but backward he would not at all draw back”, `i` “drew back”). |
| 26 | 18.188 (ἔχουσι δὲ τεύχε’ ἐκεῖνοι) | l | low | `l` “for they have my armour”: δέ is not “for”, and “my” is not in the Greek. | “and they have armour, those men;” (`i` keeps “my”). |

## B. Changes to `gloss.json`

| # | Form · line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|---|
| 27 | δῆσεν (18.100) | entry | medium | “aor. 3 sg. act., unaugmented (= ἔδησεν)”: ἔδησεν is the aorist of δέω ‘bind’; the Attic equivalent of this form is ἐδέησεν. | “contracted and unaugmented (= ἐδέησεν)”. |
| 28 | ἅλιον (18.141) | `__broaden__` | medium | Known entry: only ἅλιος ‘vain’. Here γέρονθ’ ἅλιον is ἅλιος ‘of the sea’, a different word. | Broadened with “ἅλιος — of the sea … a different word from ἅλιος ’vain’”. |
| 29 | ἔρυκε (18.126) | `__broaden__` | medium | Known entry: impf. ‘held back’ only; here it is the imperative after μή. | Added “pres. imper. 2 sg. act., with μή: ’do not hold back’”. |
| 30 | ἴω (18.188) | `__broaden__` | medium | Known entry covers only ὁππότε … περ; here a deliberative subjunctive. | Added “pres. subj. 1 sg. in a deliberative question”. |
| 31 | ἴδηαι (18.135), ἴδωμαι (18.190) | `__broaden__` | medium | Neither known entry covers πρίν γε + aorist subjunctive (‘before you/I see’). | Both broadened. |
| 32 | ὡς (18.107) | `__broaden__` | medium | Known entry has a wish only with ὄφελεν; here ὡς with the bare optative ἀπόλοιτο. | Added “introducing a wish with the optative alone: ’would that’”. |
| 33 | ἐτώσιον (18.104) | `__broaden__` | medium | Known entry: adverb ‘in vain’; here an adjective agreeing with ἄχθος. | Added “neut. nom./acc. sg., adj. agreeing with ἄχθος: ’useless’”. |
| 34 | ἔλθῃ (18.180) | `__broaden__` | medium | Known entry: after εἰς ὅ κε and ὄφρα; here after αἴ κεν. | Added “after αἴ κεν: ’if … should come’”. |
| 35 | ἕ (18.119) | `__broaden__` | medium | Known entry: “subject of an infinitive”; at 18.119 it is the direct object of a finite verb. | Added “direct object of a finite verb”. |
| 36 | βαθυκόλπων (18.122) | entry | medium | “deep-bosomed, deep-girdled”: “deep-girdled” is the rendering of βαθύζωνος, which `new-renderings.md` itself turns down. | “deep-bosomed (κόλπος, the fold of the dress over the breast)”. |
| 37 | ἐπαμῦναι (18.98) | entry | medium | “come to the aid of” against the table’s “come to the defence of” (and the known ἐπάμυνον entry). | “come to the defence of, ward off from (+ dat.)”. |
| 38 | ἐτήτυμον (18.128) | `__broaden__` | medium | Known entry: adverb ‘truly’; the unit reads it as a predicate adjective ‘true’. | Added “neut. nom. sg., predicate adj.: ’true’”. |
| 39 | πάρ (18.191) | `__broaden__` | low | Known πάρ lacks παρά + gen. ‘from beside’ after its noun (Ἡφαίστοιο πάρ’). | Added. |
| 40 | κεφαλὴν (18.176) | `__broaden__` | low | Object of πῆξαι and ταμόντα not among the known readings. | Added. |
| 41 | κακόν (18.128) | `__broaden__` | low | Predicate adjective (‘it is no bad thing’) not among the known readings. | Added. |
| 42 | αὔτως (18.198) | `__broaden__` | low | ‘just as you are’ not named. | Added. |
| 43 | κίχον (18.153) | entry | low | Form is 1 sg. or 3 pl.; the entry said 3 pl. only. | “aor. 1 sg. or 3 pl.”. |
| 44 | στάσκε (18.160) | entry | low | “iterative impf. … (= Attic ἵστατο)” misdescribed a form built on the aorist stem. | “iterative 3 sg. in -σκε-, built on the aor. stem στα-”. |
| 45 | ἔδυσαν (18.145) | entry | low | “(= Attic ἔδυσαν)” says nothing. | “the root aorist ἔδυν, intransitive”; the stripping reading kept as the homograph. |
| 46 | κεῖσο (18.178) | entry | low | Imperative at 18.178 given as “also impf.”, with no Attic equivalent for the imperfect, and a gloss (“lie still”) that fits neither line. | “pres. imper. 2 sg. (same in Attic): ’lie!’ · also impf. 2 sg., epic (= Attic ἔκεισο): ’you lay’”. |
| 47 | γέρονθ (18.141) | entry | low | Did not say τ became θ before the rough breathing of ἅλιον. | Added. |
| 48 | ᾐσχυμμένος (18.180) | entry | low | “shame, disgrace … ’disgraced’” against the line’s ‘disfigured’. | “disfigure, shame, disgrace … ’disfigured’”. |

Gloss entries checked and left: every other novel form parses correctly against its line (including ἐνείκαι, which agrees with finding 1; καταδύσεο; ἔφθιτ’; ὀψόμεναί; ὁμόκλα; ἐφέηκε; χαλεπῆναι; τεθναίην). Every novel form has an entry; `τράπεθ` is correctly under `__broaden__` (the Odyssey already has it; the 3 sg. middle reading is the addition, and the old entry stands whole). All entries are under 230 characters, typographic ’ only.

## C. Findings considered and refused

- 18.125 `i` “stayed out of the fighting” for πέπαυμαι: a fair rendering of “I have ceased from war” in this context; `l` keeps “ceased”.
- 18.132 οὐδέ rendered “and” in `l`, “but” in `i`: ordinary difference of layer.
- 18.138 πάλιν rendered “turned back / turned away”: sense kept.
- 18.165 `i` “to tell him to arm” (against the published 18.167 “to have us arm”): the participants differ (Iris to Achilles, not Athena to the Achaeans); the `l` is the published `l`.
- 18.182 γάρ not rendered in a question (“which of the gods …?”): the idiom; the published Iliad does the same.
- 18.28/18.148 `i` “with a wondrous cry going up and man-slaying Hector driving them” for ὑφ’ Ἕκτορος: an interpretation of “under Hector”, and the note says “pressed by him”.
- 18.176 `i` reorders “fix the head on stakes, cutting it” to “cut the head … and fix it”: order of action, same sense.
- 18.191 στεῦτο “vowed” (13.597 has “declared”): the context is a promise, and the note and known entry give both.
- 18.104 ἐτώσιον as “useless” (the table has “in vain” for the adverb): a different construction; handled in the gloss (finding 33).
- 18.126 ἔρυκε / 18.126b: the line repeats iliad-039 (6.360) in its last words only; the English “and you will not persuade me” matches it.
- Gloss τεῦ: the “also indef. τις” reading is not strictly needed for the printed circumflex form, but it is a real homograph in the poem and harmless; left.
- Gloss ὅ (ὅ τοι at 18.197): the known entry already has ‘that’ after a verb of knowing; no broadening needed.

## D. Notable

- The two real Greek errors were a mood (ἐνείκαι, optative not infinitive) and a case (αὐτὴν, not “I myself”).
- `new-renderings.md` was changed for κυδρή (now “glorious”, as the Odyssey) and κῆρα (“death-fate”); every other row stands. “Tall Olympus”, “defence”, “heavily”, “cut down” are table renderings, not new ones.
- Cross-part: 18.97 follows iliad-116 (Thetis’ speech closed there); 18.201 closes Iris’ speech, so iliad-118 should open with the narrator.
