# iliad-096 (15.471–558) — review

Neighbours checked: iliad-095 ends with Teucer's speech closed by ” at 470, so unit 471 opens with no quotation mark and no speech runs on; iliad-097 (559) is not yet drafted, and Hector's speech closes at 558 here. All four speeches (Ajax 472–477, Hector 486–499, Ajax 502–513, Hector 553–558) have “ + `mark` on the first unit and ” on the last. `t` untouched (word-for-word check against the packet: 620 = 620 tokens, equal). Paragraph marks `p` match the packet's ¶ lines (471, 478, 484, 500, 514). Line counts of `l` equal those of `t` in every unit. Cross-references checked against the source: 3.336–337, 5.470, 5.787, 6.112, 7.447, 7.460, 8.173–174, 10.135, 11.285, 13.95, 13.155, 13.174–176, 13.756 all say what the notes say. Published repeats (15.480, 482, 485, 486, 500, 514, 549, 550–551) have the published `l`/`i`.

## Pass 1 — units.json

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 478 | n | medium | called τετραθέλυμνον "the stock word for a shield made of four layers"; the table says its meaning is not known | "the Odyssey’s word for this shield, and its meaning is not known" |
| 478 | n | medium | packet flag, scanned by hand: ὣς φά|θ’ὃ, then δὲ τόξ|ον μὲν ἐ|νὶ κλισ|ίῃσιν ἔ|θηκεν. Only the second foot fails: δὲ is short by nature and stands on the long place after the dactylic first foot; every other syllable scans (ον is long before μ, νὶ before κλ). The irregularity is real | added: "The line is metrically irregular as transmitted: δὲ in ὃ δὲ, short by nature, falls on the long place of the second foot and has to be read long." |
| 478 | n | low | φάθ’ called "the aorist φάτο … with its vowel elided"; the form is unaugmented φάτο (iliad-095, 442, says so) | "the unaugmented φάτο … elided before the rough breathing of ὅ" |
| 478 | l, i, n | low | θέτο "put"/"put on"; the Odyssey unit (odyssey-107, same σάκος θέτο τετραθέλυμνον) has "set" | "set" in `l`, `i`, note |
| 472 | n | low | said συνέχευε "has no stated object" while `l`/`i` say "everything" | note now says the English supplies "everything" |
| 494 (ὃς δέ κεν) | i | medium | "let him die" for τεθνάτω; the note itself says the perfect gives the state, not the dying, and the table has τεθνάμεν "to be dead" (21.155) | "let him be dead" |
| 496 | i | medium | "for him to die" for τεθνάμεν; same table row | "for him to be dead in defence of his fatherland" |
| 497 | n | low | "The words σὺν νηυσὶ … γαῖαν are those of 7.460": line 499 is the whole of 7.460 | "The last line is the whole of 7.460." |
| 501 | n | low | "on the Greek side": "Greek(s)" for the people is not used in any earlier note | "Achaean side" |
| 504 | n | low | ἐμβαδόν glossed "on foot, stepping"; new-renderings.md lists "stepping" as avoided | "on foot" |
| 506 | l, i, n | medium | ἦ οὐκ rendered "Or do you not hear" though ἦ (not ἤ) is printed and 504 renders the same ἦ "Truly"/"really"; `i` also had "all his people" for λαὸν ἅπαντα (`l` "all the people") | `l` "Truly do you not hear …"; `i` "Do you really not hear Hector urging on all the people, he who …"; note says ἦ opens a question again; new-renderings.md row extended |
| 511 | l, n | medium | δηϊοτῆτι "in dread battle"; table δηϊοτής "fighting" (11.516), "battle" belongs to other words | "in dread fighting" (`l`, note) |
| 515 | n | low | "a Greek", "allies of the Greeks" | "a man of the Achaean side", "allies of the Achaeans" |
| 518 | l | medium | "Poulydamas" in `l`, while 520 `l` and the table (12.80) have "Polydamas" | "Polydamas" |
| 521 | l | low | "Panthous’-son" for Πάνθου υἱόν (a noun with genitive, not a patronymic; 515, 517, 545 have "X’s son") | "Panthous’ son" |
| 523 | n | low | called Κροίσμου "the genitive" without saying that `l`/`i` make it the object of "wounded/stabbed" | note says the genitive is the man and στῆθος μέσον the part struck |
| 524 | l | medium | "and he thudded as he fell" for δούπησεν δὲ πεσών; every other occurrence (iliad-026, 027, 032, 068, 079, 081, 095, odyssey-106, 119) is "fell with a thud" | "and he fell with a thud;" (`i` already so) |
| 524 | i | low | "began to strip" for the imperfect ἐσύλα (`l` "was stripping") | "was stripping" |
| 528 | l, i, n | medium | `l` "wounded … a shield": the table (11.434, οὔτησε κατ’ ἀσπίδα) refuses "wounded" where nothing is wounded; `i` "Phyleus’ son" where the table pattern is "son of Phyleus" | `l` "thrust at the middle of Phyleus’-son’s shield with a spear"; `i` "the shield of the son of Phyleus"; note says the thrust lands on a shield and nothing is wounded |
| 529 | n | low | "the curved plates" decides the shape that new-renderings.md says is left open | "hollowed plates" |
| 535 | n | medium | called νύξ’ "the elided aorist ἔνυξε"; ἔνυξε would elide to ἔνυξ’, so the form is unaugmented νύξε | "the unaugmented aorist νύξε, elided" |
| 537 | l | medium | "tore off" for ῥῆξε; `i` has "broke off" and the table has ῥήγνυμι "break" (3.348, 12.440) | "broke off" |
| 537 | n | low | κάππεσεν "is κατέπεσεν": the form has no augment | "κατ- with the unaugmented πέσεν, the τ assimilated to the π" |
| 545 | l, i | low | "Hicetaon’s son": patronymic Ἱκεταονίδην; the table row has "Hicetaon’s-son" / "son of Hicetaon" | `l` "Hicetaon’s-son"; `i` "the son of Hicetaon" |
| 547 | i | low | "he had grazed" (pluperfect) for the imperfect βόσκ’; `l` "was grazing" | "he was grazing" |
| 547 | n | medium | called βόσκ’ "the elided ἔβοσκε"; that would elide to ἔβοσκ’ | "the unaugmented imperfect βόσκε, elided" |
| 550 | n | low | said the lines are those of 13.175–176 with only a comma changed; 13.175 has ἐς where here is εἰς | note names the εἰς for ἐς as well |
| 555 | n | low | "the Greeks are stripping" | "the Achaeans" |
| 556 | n | medium | ἑλέειν is an active infinitive, but `l`/`i` give it as "is taken / has been taken" and the note listed it as "to take" without saying so | note says ἑλέειν is active and that the English puts it passively beside the passive κτάσθαι |

## Pass 1 — new-renderings.md

| row | severity | what was wrong | what was done |
|---|---|---|---|
| ἦ ἔλπεσθ’ (15.504) | low | the same ἦ at 15.506 had a different English (see 506 above) | row extended to both questions |

All other rows were set against the units (Greek, `l`, `i`) and match after the edits above; the rows for names, μινύθω, ἄρκιον, ἐμβαδόν, γυάλοισιν, κύμβαχον, εὐράξ, λιάζομαι, ἀποσταδόν agree with the table where it has an entry. No row was missing for a formula that will recur.

## Pass 1 — findings considered and refused

- 490 ῥεῖα … ἀρίγνωτος: ῥεῖα has no separate English ("easily" is said once, in "easily-known"). Refused: ἀρίγνωτος already carries "easily" in the table (iliad-077, 15.206), saying it twice would be a pleonasm the Greek does not make; the note names both words.
- 472 "your many arrows" (ταρφέας, `l` "thick"): the Odyssey table gives `i` "arrows that came so thick"; "many" is a fair reading of the crowded arrows and the table avoids only "frequent" and "showering". Kept.
- 496 ἀμυνομένῳ "defending": the table has ἀμύνω "ward off" in some rows and "defend" for the absolute use (13.312, 13.814); kept as "defending … in defence".
- 502 ἄρκιον: `i` "the choice is sure" is an interpretation, but new-renderings.md logs it and the note says "I read it as the choice being settled"; kept.
- 521 note "as at 13.756": that line has Πανθοΐδην, the same man; kept.
- 515 "Hector kills Schedius, a man of the Achaean side" and the other facts about the speakers in notes (Phocians, Cyllene): story facts, not renderings; consistent with the lines.
- 553 μεθήσομεν: note does not name the tense, and "are we to slacken" is the table's deliberative; kept.
- 542 `l` "through the chest rushed through": clumsy but literal (διέσσυτο + genitive); `i` is clean; kept.
- Quotation marks and `mark` labels: nothing wrong. Speech introductions 471, 485, 501, 552 use the table's formulae.

# Pass 2

Fresh re-check of units.json (note labels against each line, `l` against the Greek, `l` ↔ `i`, quotation marks and `mark`, repeated-line English against the published units by script), then every entry of gloss.json and every `__broaden__` entry against the line it stands in, then new-renderings.md against the conventions table. `t` untouched (checked equal before and after). Quotation marks, `mark` labels, `p` marks, line counts of `l` and `t`, no Greek in `l`/`i`: nothing wrong. Repeated lines (500, 514 = 5.470 etc.; 549 = 13.174; 556 = odyssey-111; 480, 482, 484, 486 against iliad-019, 047, 059, 066, 078, 086, 095, odyssey-107) match the published English. All 83 novel forms are in gloss.json, none extra; every `__broaden__` entry begins with the old entry whole; every new entry is under 230 characters, with ’ only and no line numbers.

## Pass 2 — units.json

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 553 | n | low | μεθήσομεν: note named no tense (glosser's flagged doubt). The -σ- is the future marker; a short-vowel aorist subjunctive of μεθίημι would be μεθέομεν | "first plural future of μεθίημι", still deliberative |
| 553 | n | low | κταμένοιο called "the aorist participle … in the passive sense"; it is the root-aorist middle participle (ἐκτάμην) with passive sense | "root-aorist participle … middle in form and passive in sense" |
| 556 | n | low | κτάσθαι "a form of κτείνω read here as passive" (glosser's flagged doubt) | "the root-aorist middle infinitive of κτείνω (cf. κταμένοιο at 553), passive in sense" |
| 523 | n | low | typo "and and οὔτασε" | one "and" |
| 500 | n | low | ὄτρυνε called "the unaugmented aorist"; the form is the same for aorist and imperfect, and the glossary entry and 4.73 note say "unaugmented past" | "the unaugmented past" |
| 492 | i | low | "will not defend" for οὐκ ἐθέλῃσιν ἀμύνειν; loses ἐθέλω, and `l` has "does not wish" | "is unwilling to defend" |

## Pass 2 — gloss.json

| form | severity | what was wrong | what was done |
|---|---|---|---|
| ἕπουσιν | low | "epic -ουσιν (= Attic -ουσι)": the forms are identical, the ν is movable. Flagged doubt resolved: only an active ἕπω can have this ending (ἕπομαι would be ἕπονται), so "be busy about" is the active, with περί + acc. | "pres. 3 pl. act., ν-movable"; the entry now says the middle ἕπομαι is "follow" |
| μεθήσομεν | low | hedged "fut. 1 pl. (or short-vowel aor. subj.)". Flagged doubt resolved: -σ- excludes the short-vowel subjunctive (μεθέομεν) | "fut. 1 pl. (the -σ- marks a future, not a subjunctive), deliberative" |
| κτάσθαι | low | "root aor. inf. in passive sense" did not say it is the middle infinitive. Flagged doubt resolved: the root aorist ἐκτάμην (κτάμενος, κταμένοιο) has the middle infinitive κτάσθαι; passive in sense, as the line needs | "root aor. inf. mid. (aor. ἐκτάμην, cf. κταμένοιο), epic, passive in sense" |
| ἐεισάσθην | low | "epic reduplicated aor.": the ἐει- is not a reduplication | "aor. 3 dual mid. ἐεισάσθην, epic (cf. ἐείσατο)" |
| γυάλοισιν | low | "hollow, curved plate": new-renderings.md says the shape is left open | "hollow, the hollow plate of a breastplate" |
| ἕλοιεν (`__broaden__`) | medium | old entry covers only the fear clause after μή and εἰς ὅ κ’; 476 is a negative wish (μὴ μάν) | old entry whole + " · also aor. opt. 3 pl., in a negative wish after μὴ μάν: ’may they not take’" |
| ἕλῃ (`__broaden__`) | low | old entry says "after εἰ κεν"; 504 is after ἢν, without κεν | old entry whole + " · also aor. subj. 3 sg., after ἢν (= ἐάν), without κεν: ’takes’" |
| νύξ (`__broaden__`) | low | old entry "νύξ’ = ἔνυξε"; 535 is unaugmented νύξε (pass 1, line 535) | old entry whole + " · also aor. 3 sg. act., unaugmented, elided (νύξ’ = νύξε): ’stabbed’" |

All other parses were set against the line and stand (cases, tense, mood, voice, agreement): in particular αἰχμῆς, δαμασσάμενοί, εἰδότα, κροίσμου, μάρναό, μάχεσθ, μῖξαι, ἀκούετε, ἀμυνομένῳ, ἀπήμβροτεν, ἀρηρότα (acc. with τόν), ἐγγυαλίξῃ, ἐνένιπεν, ἐπόρουσεν, ἱεμένη, ὁτέοισιν, ὅτινας, τεθνάτω, τεθνάμεν, σόη, ἀκήρατος; and the eight old `__broaden__` additions (δολιχὸν, μέσον, οἴχωνται, ἀεικὲς, ἐθέλῃσιν, ἐπίσπῃ, πρίν, ἀφ, κατ, περὶ, ἕλε) each fit the line they were added for.

## Pass 2 — new-renderings.md against conventions.md

Rows re-set against the table: reply formula (1.172, 6.263, 12.364, 739), ἀριστῆες (2.404), ἀγχιμαχητής (2.604), ἄρκιον (2.393), εὐράξ (11.251), κασίγνητος (8.330), ἀνεψιός (9.464, 10.519), ἐνίπτω (3.438), ἔπος τ’ ἔφατ’ (1.361, 6.485), ἀμφιέλισσαι, εἰλίποδας (6.424), ἱπποδασείης (3.369), ἀλεωρήν (12.57), γύαλον (5.189), ξεῖνος (6.215 ff.), πρυλέες (5.744, 12.77), κύμβαχος (5.586), φοῖνιξ (4.141, 6.219), ἔλπομαι (9.40), μεθίημι (4.234, 6.523), θούριδος ἀλκῆς, εὖ εἰδώς: all agree. One edit: the μεθήσομεν row now says "future indicative used deliberatively" and cites 6.523 for the absolute use. No row missing.

## Pass 2 — findings considered and refused

- 508 κέλετ’: the note says only "an elided form of κέλομαι"; the existing glossary entry reads it as κέλεται (present), which matches `l` "does he bid". Not wrong; kept.
- 509 note on the double comparison (τοῦδε … ἢ …): true of the Greek; kept.
- 497 note "if the Achaeans go off" against `l`/`i` "have gone": οἴχομαι has perfect force, and the note says "be gone"; kept.
- 532 note "here for a lesser king": a story judgement, not a rendering; kept.
- 529 `about`: "the breastplate his father brought home saves him" is ambiguous in English but 534's note settles it (Phyleus is Meges’ father); kept.
- ἀκρότατον (known form): existing entry names other nouns (χρόα, χαλκόν) but gives the same parse (masc. acc. sg.); no broadening needed.
- 478 metre: re-scanned, δὲ in ὃ δὲ on the long place of the second foot is the one failure; the pass 1 sentence stands.
- νέον (known form, "lately, just now" as adverb): covers "newly" at 538; kept.
- ὄτρυνε (known form): the glossary says "impf."; the unit note now says "past", which covers both; no change to the entry.
