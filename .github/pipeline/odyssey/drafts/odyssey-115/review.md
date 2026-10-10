# odyssey-115 (24.1–105) — review

## Pass 1

Scope: grammatical labels in every note checked against the form and line; claims about word position checked against the line; cross-references (lines 18, 20, 22, 23, 25, 27, 47, 48, 57, 59, 60, 62, 70, 81, 89) checked; Greek to `l` word by word; `l` to `i`; remembered English; house-table agreement (epithets and formulas); quotation marks and `mark`; `p` marks and `ln`; repeated published lines (24.4, 16–18, 22, 27, 53, 98); the neighbouring part. All edits made by script (`units.json`, never `t`; `t`, `ln`, `p`, `mark` verified identical to the draft as received; 58 units before and after).

Totals: 0 high, 14 medium, 25 low (39 changes to `units.json`); 5 corrections to `new-renderings.md`.

Quotation marks: “ ” 2/2 in both layers (Achilles 24–34 opens unit 12, closes unit 16; Agamemnon 36–97 opens unit 18, closes unit 53); Nestor’s inner speech ‘ ’ opens unit 29 and closes unit 30, in `l` and `i`; each speech’s first unit carries `mark` (Achilles speaks, Agamemnon answers, Nestor speaks). The last unit of odyssey-114 (“Athena hid them in night and led them out of the city”, 23.371–372) is narration, so no speech runs on from the previous part; the speech introduced at 24.105 runs into the next part, and the note of that unit says so. `p` on units 0, 8, 12, 29, 31, 54 matches Murray’s paragraphs at 1, 19, 24, 54, 57, 98.

Scansion: the packet flags none. By hand and by `scan_hexameter.py`, all 105 lines fit; the scanner records "spondaic fifth" for 24.13, 24.35, 24.64, 24.71, 24.75, 24.81, 24.82. These are ordinary hexameters (a spondee in the fifth foot is a licence of the metre, not an irregularity in the transmission), so no sentence was added to any note.

### Changes (line · field · severity · what was wrong · what was done)

| Line | Field | Sev. | What was wrong | Done |
|---|---|---|---|---|
| 24.2 | n | low | χερσίν called "the old dative ending -σιν"; it is simply the dative plural of χείρ | reworded |
| 24.5 | n | low | τῇ called "relative-like article"; here it is a plain demonstrative ('with this'), the relative is τῇ τε at 24.3 | relabelled |
| 24.19 | n | low | οἱ said to be "the souls of the three just named" while four heroes are named in 15–18 | now "the souls just named", κεῖνον Achilles as the one they gather about |
| 24.19 (2nd unit) | i | low | "there came up" renders ἔπι, which the note glosses 'next'; `l` says "came next" | "there came next" |
| 24.28 | i | low | "Yet" for ἦ τ’ ἄρα (note: 'truly, then') | "Indeed" |
| 24.30 | n | low | lemma ἀπόναμαι; LSJ headword is ἀπονίναμαι | corrected |
| 24.30 | n | med | "θάνατον καὶ πότμον ἐπισπεῖν is the phrase of line 22 in the infinitive": line 22 has the verb θάνον, not θάνατον | says it echoes 22, with the noun for the verb 'died' |
| 24.32 | l | med | "a tomb would have been made by all the Achaeans": passive for the active ἐποίησαν (and `i` is active) | "a tomb all the Achaeans would have made" |
| 24.34 | n | low | ἁλῶναι called "infinitive passive" (it is the active-form 2nd aorist, passive in sense) and the unsupported image of death as a net | relabelled, net removed |
| 24.36 | l, i, n | med | ὄλβιος rendered "Fortunate" although the house table fixes ὄλβιος as "prosperous" (17.420, 11.136; "fortunate" is listed as avoided); the new-renderings row contradicted the table | "Prosperous" in `l`, `i`, note (note says it is the house rendering and what Agamemnon means by it) |
| 24.36 | l | med | θεοῖς ἐπιείκελος rendered "like-the-gods"; the table fixes ἐπιείκελος as "resembling" in `l` (15.414) | "resembling the gods" (`i` "like the gods" unchanged); note updated |
| 24.37 | n | low | "μαρνάμενοι … the verb Homer prefers for battle": a claim about the poem this part cannot show | removed |
| 24.39 | n | low | note says 'great in his greatness' but `l` has "your" | "your" |
| 24.41 (2nd unit) | l | low | "stopped it": supplied object not bracketed (house practice is "(it)", and the note says "(it)") | "stopped (it)" |
| 24.43 | n | med | κάτθεμεν explained as "τ doubled to θ before the rough breathing": no breathing follows; it is κατέθεμεν with the vowel lost | rewritten |
| 24.47 | n | low | "immortal women of the sea" against `l` "sea-ones" and `i` "goddesses of the sea" | note now gives all three |
| 24.50 | n | med | ἔβαν called "the unaugmented aorist of βαίνω": it carries the augment (ἔ-βαν) | "the epic 3rd plural aorist, Attic ἔβησαν" |
| 24.50 | l | low | ἀναΐξαντες "springing up"; table (ἀναΐξας 13.197) has "having sprung up" | "having sprung up" |
| 24.54 | n | low | "as in line 62 Ἀργείων and in line 81 Ἀργείων … στρατός" given as examples of the two names side by side, which they are not | now lists Ἀργείων at 62 and 81 and Ἀχαιοί at 57 |
| 24.55 | l | low | repeat of 24.47 ("the immortal sea-ones") lost the article; the note says the two are translated the same | "with the immortal sea-ones" |
| 24.58 | n | low | ἔστησαν called "the intransitive aorist" (the form is the weak aorist, used intransitively here) | "the aorist of ἵστημι, here intransitive" |
| 24.60 | n | low | ἀμείβομαι "the verb used elsewhere of replying in speech": not shown by this part | removed |
| 24.61 | i | low | "could not have found" for ἐνόησας; `l` and note have 'noticed' | "would not have noticed" |
| 24.63 | l | low | "days and nights" reverses νύκτας τε καὶ ἦμαρ (`i` was right) | "nights and days" |
| 24.63 | n | med | "μέν after σε has no matching δέ": μέν stands after δέκα, before σε, and is answered by ὀκτωκαιδεκάτῃ δ’ in the next unit | corrected |
| 24.65 | l | low | "we gave you" supplies an object the Greek lacks, unbracketed | "we gave (you)" |
| 24.65 | l | med | ἕλικας βοῦς rendered "cattle with crumpled horns"; the table (εἰλίποδας ἕλικας βοῦς, βοῶν ἑλίκων 22.292) fixes `l` "crumple-horned cattle" | "crumple-horned cattle" (`i` already matched) |
| 24.68 | i | med | "around the pyre as it burned": καιομένοιο is masculine and the note says it agrees with the 'you'; "it" contradicts the note and misplaces the participle | "as you burned" |
| 24.70 | n | low | ὀρυμαγδός "of the warriors and the fire": the fire is not in the line | "of the warriors" |
| 24.71 | n | med | ἤνυσεν called "unaugmented"; ἤ- is the augment | corrected |
| 24.71 | n | low | "ἐν between adjective and noun" for οἴνῳ ἐν ἀκρήτῳ (order is noun, ἐν, adjective) | "between noun and adjective" |
| 24.73 | n | low | mother "who has just come out of the sea" (she came at 47) | "who came out of the sea in line 47" |
| 24.74 | n | low | ἔργον Ἡφαίστοιο "is the phrase for the finest craft": generalises beyond the part | "marks a thing as the finest craft" |
| 24.80 | l, i, n | med | ἱερὸς στρατός rendered "holy host"; the table fixes ἱερός as "sacred" ("holy" reserved for ἠγάθεος); new-renderings wrongly claimed the table said "holy" | "sacred host" in all three |
| 24.83 | l | med | τηλεφανής rendered "conspicuous"; table reserves "conspicuous" for ἀριδείκετος ("most conspicuous") | "visible from afar" (`i` and note already say 'seen from far') |
| 24.95 | i | med | "wound the war up to its end"; the table (πόλεμον τολύπευσε, shipped at 1.235, 4.487, 14.368) fixes "wound up the war" in both layers | "now that I have wound up the war?" ; note keeps the sense 'brought it to its end' |
| 24.96 | n | med | "Αἰγίσθου ὑπὸ χερσίν with ὑπό and the genitive": the text has dative χερσί; Αἰγίσθου is the genitive depending on it | rewritten |
| 24.102 | n | low | 'the dear son of Odysseus' offered as a parallel that is not in this part | removed |
| all | n, about | low | notes had ASCII apostrophes/quote marks (709 uses); odyssey-114 ships typographic ‘ ’ ’ | converted in 57 notes and `about` (opening ‘ after space, bracket or dash; all other ' to ’); `l` and `i` had none |

### Findings considered and refused

- 24.4 (unit 1) `l`/`i` use "charms" for θέλγει although the table (10.291 etc.) fixes θέλγω as "enchant". Refused: the packet requires the published wording of 24.4 (odyssey-022) as far as the sentence allows, and the validator enforces published repeats; "charms" is that wording.
- 24.28 (unit 13) "Indeed" vs literal "Truly": kept, `l` has "Truly then"; the idiomatic layer is free.
- 24.30 (unit 14) `i` "still enjoying" for the aorist participle ἀπονήμενος: refused as a change; the participle is prior to the dying, and "still enjoying the honour" is a fair reading in prose.
- 24.13 `l` "came along" vs `i` "came to" for κατά with the accusative: both are within the range of κατά of motion; left.
- 24.47, 24.73, 24.85 `l` "your mother" for bare μήτηρ: the possessive is supplied from the address; kept without brackets, as a possessive in the literal layer is ordinary (an object pronoun is another matter: see 24.65, 24.41 above). Noted for the owner if brackets are wanted on supplied possessives.
- 24.76 `l` "for you … your" rendering a single τοι: left; the note says τοι is σοι and the double is a harmless literal layer.
- 24.98 `i` "went straight up" for ἰθὺς κίον: the movement is toward the souls; `l` "straight on" is looser. Left.
- 24.57 note "Agamemnon is still speaking" and no “ on the new paragraph (unit 31): the validator counts “ ” balance only, and Murray’s paragraph is a paragraph of Agamemnon’s speech, not a new speech. Left unmarked; the validator’s balance check (2/2) passes.
- 24.1–17 `about`: "Agamemnon recognises Amphimedon and speaks to him" — the speech itself is in the next part, but 105 introduces it; left as a summary of where the part ends.
- Note word counts above the 110 band (24.1, 24.2, 24.5, 24.6 (141), 24.11, 24.15, 24.45; 24.70 is 19): validator WARN only, no wrong statement in them; not trimmed.
- 24.10 (`i` "the Harmless" with `l` "Akakêta"): matches the table’s treatment of ἀργεϊφόντης; note states the meaning is unknown. Left.
- 24.81 ἀμύμονα τύμβον "blameless tomb": the note says why the stock epithet is kept. Left.
- Glossary (`gloss.json`) is not reviewed in this pass (pass 2 per runbook).

### new-renderings.md

Checked every row against the units. Listed formulas and epithets are complete for what is new (ἀκάκητα, εὐρώεντα κέλευθα, Λευκάδα πέτρην, Ἠελίοιο πύλας, δῆμον ὀνείρων, εἴδωλα καμόντων, the three προσεφώνεε introductions, ἀθανάτῃς ἁλίῃσιν, παλαιά τε πολλά τε εἰδώς, θερμὰ δάκρυα, ἄμβροτα εἵματα, ἔσχοντο φόβου, ἀργυρόπεζα Θέτις, περικαλλέ’ ἄεθλα, ἀριστήεσσιν Ἀχαιῶν, καλὸν χρόα). Corrections made to the file:

1. ὄλβιος row deleted: it contradicted the table ("prosperous"); the unit now follows the table.
2. θεοῖς ἐπιείκελος row: `l` changed to "resembling the gods" to follow the table row for 15.414.
3. ἀρίστη φαίνετο βουλή row: `l` and `i` did not match the units; now reads as the units do (οὗ καὶ πρόσθεν ἀρίστη φαίνετο βουλή, "whose counsel earlier too appeared best" / "whose counsel had also seemed best before").
4. ἱερὸς στρατός row: "the sacred host", following the table’s ἱερός "sacred".
5. τολύπευσα row deleted: the table already fixes "wound up the war" (14.368 and the earlier shipped lines).

## Pass 2

Scope: all 58 units re-read afresh (notes' grammatical labels, Greek to `l`, `l` to `i`, remembered English, quotation marks, `mark`, `p`, cross-references to lines 9, 18, 20, 22, 23, 25, 27, 47, 48, 57, 59, 60, 62, 70, 81, 89 all checked against the packet), the 39 pass-1 edits re-checked (all stand; none introduced an error), the house table re-grepped for every epithet and formula, and `gloss.json` checked entry by entry against every line where the form occurs, plus all 397 known forms against their stored entries for uses the stored entry does not cover. `t`, `ln`, `p`, `mark` untouched (verified identical; 58 units). Edits by script. Quotation marks re-verified: “ ” 2/2 and ‘ ’ 1/1 in `l` and `i`, none in `t`; no ASCII quote or backtick in `l`, `i`, `n`, `about`.

Totals: 0 high, 2 medium, 4 low in `units.json` (6 changes); 2 medium, 16 low in `gloss.json` (counting the five de-pinned entries separately and the 3 new `__broaden__` entries: μοῦσα medium, κέ and αὐτοῖσι low); no change to `new-renderings.md` (every row still matches the units).

### Changes to units.json (unit by first line · field · severity · what was wrong · what was done)

| Line | Field | Sev. | What was wrong | Done |
|---|---|---|---|---|
| 24.98 | n | med | κίον called a dual form with θαμβήσαντ’ and ἐσιδέσθην; κίον is the plural (3 pl.) shape, as the glossary entry itself says; only θαμβήσαντ’ (for -τε) and ἐσιδέσθην are dual | note now says the dual subject takes a plural verb; ending named -σθην |
| 24.32 | l, n | med | Παναχαιοί rendered "all the Achaeans" in `l`; the table fixes `l` "the Achaeans all together", `i` "all the Achaeans" | `l` "the Achaeans all together"; note names both layers |
| 24.32 | n | low | ἤρα’ said to be "an elided aorist" with "the elision hides the ending": it is the 2nd sg. aorist middle ἤραο (a -τ- cannot be elided, so not ἤρατο), and the note should say so | note states ἤραο, 2 sg. |
| 24.63 | l, i | low | the unit opens with δέ, which both layers dropped ("Seventeen…", "For seventeen…"; "For" implies γάρ) | `l` "And seventeen…", `i` "And for seventeen…" |
| 24.76 | l, n | low | ἔξοχα: `l` "above all", note "exceedingly"/"outstandingly"; the table fixes ἔξοχα "beyond measure" (15.70; "exceedingly" avoided) | `l` "beyond measure of all", note "beyond measure (the house rendering)" |
| 24.67 | n | low | ἐσθῆτι θεῶν "that is the deathless garments of line 59": an identification the text does not state | "presumably" |

(Lines above are the line each unit starts on; the κίον note is in the unit at 24.98–101.)

### Changes to gloss.json

| Form | Sev. | What was wrong | Done |
|---|---|---|---|
| ἤρα | med | parsed aor. 3 sg. = ἤρατο; the form is 2 sg. aor. mid. ἤραο elided ('you would have won'; the unit's `l`/`i` and note say "you") | "aor. 2 sg. mid., elided (ἤρα’ = ἤραο; Attic ἤρω): ’you won’" |
| λέγομεν | low | parsed only as a present ('narrative present'), while the unit note and `l`/`i` read an unaugmented imperfect | both readings joined by " · " |
| ἄεθλα | low | "prize" only; the form also means "contests" (24.89) | "contest; prize won in a contest" |
| ἐσιδέσθην | low | Attic equivalent given with odd accents (εἰσεῖδέσθην) and the form not marked unaugmented | "unaugmented (… = Attic εἰσειδέσθην)" |
| ὄλβιε | low | "fortunate" against the house "prosperous" | "prosperous, blessed" |
| τηλεφανὴς | low | "conspicuous" (reserved for ἀριδείκετος) | "visible from afar" |
| ἀλείφατι | low | "epic -ατι": -ατι is the regular dative of ἄλειφαρ (gen. -ατος), not epic | removed |
| ἀπονήμενος | low | Homeric form with no Attic equivalent named | "(= Attic ἀπονάμενος)" |
| κείροντό | low | unaugmented form with no Attic equivalent named | "(= ἐκείροντο)" |
| λίγεια, λευκάδα, ἱερὸς, παραστήσεσθαι, τάφῳ | low | entries pinned to the line ("of the Muse’s voice", "a landmark on the road to the underworld", "epithet of a host", "of fate", "with ἀντιβολέω") | context tags removed; meaning kept |
| ἁλίῃσιν (`__broaden__`) | low | "sea-nymphs" in the new reading (the house avoids that word for ἀθανάτῃς ἁλίῃσιν) | "sea-goddesses"; old entry still whole |
| μοῦσα (`__broaden__`, new) | med | stored entry gives voc. sg. only; 24.62 Μοῦσα λίγεια is nominative | old entry whole + " · also nom. sg. …" |
| κέ (`__broaden__`, new) | low | stored entry for accented κέ has no temporal-clause use; 24.7 ἐπεί κέ τις ἀποπέσῃσιν | old entry whole + " · also + subj. in a temporal clause …" |
| αὐτοῖσι (`__broaden__`, new) | low | stored entry gives only "for them, to them"; 24.80 ἀμφ’ αὐτοῖσι is "around them" | old entry whole + " · also plain personal pronoun after a preposition …" |

Format re-checked: all new entries under 230 characters, ’ only (no ASCII ' or ‘), no line numbers, no "here"; every `__broaden__` value contains the stored entry whole (tested against known-forms.json); keys equal novel-forms.json exactly; no article form is parsed as an article.

### Findings considered and refused (pass 2)

- 24.93–94 unit ends at Murray's comma after Ἀχιλλεῦ although αὐτὰρ ἐμοὶ… begins a new sentence: the build allows a comma end, the text is as printed, the unit is two lines. Left; not a punctuation omission (a mark is printed).
- 24.29 ἀλεύεται: stored glossary entry parses it "aor. subj. 3 sg., short vowel, perhaps a fut."; the note and `l` read a general present 'avoids'. Both fit the Greek (a short-vowel subjunctive/future in a general relative clause); stored entries are not rewritten.
- 24.76 μίγδα Πατρόκλοιο… "depending on ‘bones’": μίγδα can govern the genitive, but the note's reading matches `l` ("those of Patroclus"); left.
- 24.97 οὐλομένης: the stored entry says "perf. part." while the form is the aorist middle participle; stored entry is not rewritten; the part's note says only 'participle of the aorist'. Not broadened (a mislabel, not a missing use). Reported for the owner.
- 24.90 θηήσαο gloss "’you would marvel at’" against 'would have marvelled' in `l`/`i`: a general rendering of an aorist with κε; left.
- Supplied possessives (24.47, 24.73, 24.85, 24.97 "my ruinous wife") remain unbracketed, as in pass 1.
- 24.43 κάτθεμεν "aor. 1 pl." in the glossary means first person plural, not 'first aorist': the glossary's usage throughout; left.
- 24.7 ποτέονται, τετριγυῖαι, νυκτερίδες: checked; no fault.
- Gloss ἀκάκητα "or ’giver of ease’": a second guess not in the note; the entry already says the meaning is disputed. Left.
