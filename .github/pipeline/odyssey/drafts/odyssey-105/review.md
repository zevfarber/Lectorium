# odyssey-105 (21.320–434) — review

Reviewer: adversarial, two passes. `t` untouched throughout (checked: the units' `t`, whitespace removed, reproduce the same string before and after; tiling, `ln`, `p`, line-count of `l`, closing/opening “ ” count re-checked by a read-only simulation of build and validator check 6). Nothing built, nothing committed. Unit numbers below are by the line the unit starts on (`ln`), as units were split and merged.

Totals: pass 1 — 2 high, 7 moderate, 12 minor (21 changes). Pass 2 — 0 high, 2 moderate, 5 minor (7 changes to gloss.json). Units 73 → 71 (one split, one merge).

## The validator problem (speech-final units 383–385 and 430b)

What is enforced (`validate_odyssey.py` check 6, `odyssey_lib.letters_only`): the key is the whole unit's Greek reduced to its letters (all Greek-range characters, accents kept, case folded, punctuation and spaces dropped). If a unit's key equals the key of any earlier published unit (or earlier unit of this part), its `l` and `i` must equal that unit's exactly, closing mark included. The test is on whole units only; a repeated line inside a longer unit is free. `build_odyssey.py` enforces only tiling, terminal punctuation (`. ; ·` or `,`), line counts and the five-line limit; it does not look at repeats.

Choice made (validator not weakened, no source change): change the unit boundaries so the key no longer matches, and keep the published wording word for word.

- **383–385** (identical in letters to odyssey-104 unit at 237, whose `i` ends without ”): split at the comma inside 384, `…ἐν ἕρκεσι,` / `μή τι θύραζε …`. The cut falls exactly where the protasis ends and the apodosis begins. `l`/`i` are the published wording divided at that point; the second half now carries the closing ” in both layers. Both halves end on an allowed comma, `ln` 383 and 384, and the notes are rewritten (the 383 half takes the published note's reading of the genitives).
- **430b** (`τὰ γάρ τ’ ἀναθήματα δαιτός.`, identical to odyssey-002 unit at 152, whose `i` ends in ‘;’): merged with the unit before it (428–430a, `νῦν δ’ ὥρη … μολπῇ καὶ φόρμιγγι·`), giving a three-line unit with a new key. The published clause is reused verbatim at the end (`for these are the adornments of a feast.”` / `for these are the things that crown a feast.”`). This is the same device as the odyssey-076 precedent (units merged to avoid a forced closing ”).

After both changes every repeated whole-unit (320, 330, 343, 350, 353, 354, 355, 356, 361) still equals its published English, and the opening/closing marks balance in both layers (9/9; the inner single quotes at 323–328 close at 327). The tolerated WARN about unbalanced marks should not appear.

## Pass 1 — Greek notes, `l`, `i`, remembered English, quotation marks

| line · field | severity | what was wrong | what done |
|---|---|---|---|
| 383 · `i`,`l`,`n` (unit) | high | Eumaeus' speech (opened at 381) had no closing ” at 385; the unit was fixed by the validator to the odyssey-104 English | split at the comma in 384 (see above); closing ” on the second half in `l` and `i` |
| 383 · `n` | moderate | note read `ἀνδρῶν ἡμετέροισιν ἐν ἕρκεσι` as “in our courts of men”, which the Greek does not say (ἀνδρῶν depends on both genitives of hearing; published note has it so) | new note for the first half: ἀνδρῶν depends on στοναχῆς and κτύπου, ἐν ἕρκεσι is “in our courts” |
| 428–430 · `l`,`i`,`n` (unit) | high | Odysseus' speech (opened 424) had no closing ” at 430; the half-line `τὰ γάρ τ’ ἀναθήματα δαιτός.` is fixed by the validator to odyssey-002's English, which ends in ‘;’ | merged with 428–429 (see above); closing ” added; `i` “in the light” made “in daylight”; merged note |
| 331 · `n` | moderate | “ἔδουσιν is the uncontracted ἔδω” — ἔδω is not a contract verb; the label is false | “from ἔδω, the poetic ‘eat’, Attic ἐσθίω” (agrees with the shipped glossary entry) |
| 363 · `i` | moderate | “the swift dogs that you reared yourself will eat you up … alone, away from men” — “yourself” has no Greek behind it (οὓς ἔτρεφες) and the whole clause arrived in Murray's cadence | rebuilt: “the swift dogs you reared will devour you among the swine, alone, away from men,” |
| 388 · `n` | moderate | ἆλτο called “without the augment”: unverifiable (the long ᾱ is not understood as a missing augment; earlier parts removed the same kind of claim) | claim dropped; the glossary entry already gives the aorist and Attic equivalent |
| 392 · `n` | moderate | “ἕζετ’ is the aorist of ἕζομαι”; the shipped glossary and odyssey-104's note at the same line both treat it as ἕζετο (imperfect) without a tense label | note now says “ἕζετ’ is ἕζετο, ‘sat down’” |
| 412 · `n` | moderate | “ἐτράπετο … the verb ending the line” — it stands at the start of line 413, not the end of 412 | “the verb held over to the start of the next line” |
| 426 · `i` | moderate | “not as the suitors, in dishonouring me, make it out” lost the verb ὄνονται (‘scorn’, which `l` and the note both have) | “My strength is still firm, not as the suitors scorn me, dishonouring me.” |
| 322 · `i` | minor | “nor, indeed, would it be fitting” — adds a conditional and “indeed”; the Greek is the plain indicative οὐδὲ ἔοικεν | “nor is it fitting;” |
| 323 · `i` | minor | “Men far worse than he” — “than he” is not in the Greek (χείρονες has no stated standard) and `l` has none | “Men far worse are wooing …” |
| 327 · `i` | minor | “who has come here” — “here” not in ἐλθών | “who has come” |
| 337 · `n` | minor | “ἐξερέω is the future of ἐξερέω” — circular | “the uncontracted future ‘I will speak out, declare’” (as the glossary has it) |
| 366 · `i` | minor | “because so many were shouting” — πολλοί is “many”, not “so many” | “because many were shouting” |
| 368 · `n` | minor | “Telemachus is across the hall from the swineherd” — not in the Greek (ἑτέρωθεν only says ‘from the other side’) | replaced by “The Greek does not say which side he stands on” |
| 372 · `l` | minor | “so far than all” for τόσσον with a comparative (note and `i` say “so much”) | “so much than all” |
| 374 · `i` | minor | “to his grief” sat too close to remembered English and over-translates στυγερῶς | “send one of them off in misery from our house” |
| 402 · `i` | minor | “If only he may meet with” — wrong mood for the optative of wish | “might meet with” |
| 416 · `n` | minor | “πάρακειμαι” (accent on the wrong syllable) | “παράκειμαι” |
| 431b · `n` | minor | “φίλην is ‘own’” while `l` says “dear” | “φίλην ‘dear’ is used almost as ‘own’” (`i` leaves it out, as the table does for φίλον ἦτορ) |
| `about` | minor | “Telemachus threatens them” — he threatens the swineherd, and the suitors then laugh it off | “Telemachus threatens the swineherd, the suitors laugh the matter off, and Eumaeus …” |

Verified without change (checked word by word against the line): every case relation and mood in `l`; all nine speeches' “ ” and `mark` (321 Eurymachus, 331 Penelope, 344 Telemachus, 362 suitor, 369 Telemachus, 381 Eumaeus, 397 and 402 suitors, 424 Odysseus), the inner single quotes 323–328, the 16 `p` flags against Murray's ¶, odyssey-104's last unit (Penelope's speech closes with ” at 319, so 320 opens cleanly) and the part's end (no speech open into odyssey-106); all cross-references (329 → 333, 320 → 343, 360 → 367, 361 → 401, 376 → 404, 328 → 407, 330 → 423, 426 “still firm” → Odysseus' doubt in odyssey-104 about strength lost to wandering, the 21.339–342 gift list against odyssey-077); the stock epithets against the table (ἀμέγαρτε “unenviable/luckless”, δαΐφρων “wise-minded/wise-hearted”, εὐερκής “well-fenced/well-secured”, ἀλήτης “vagrant”, ἐπίκλοπος “thievish/trickster”, ὑπερηνορεόντων “overweening/overbearing”, ἄττα “father”, ὑφορβός/συβώτης “swineherd”); the twelve new renderings against the units (all applied as listed). Scansion: the packet flags no line; none was added to any note.

## Pass 1 — findings considered and refused

- 321 `i` “as your husband” (not in the Greek): ἄξεσθαι is the middle, ‘lead home for oneself’, and the note says so; the gloss is the sense of the verb.
- 326 `i` “cannot string”: οὐδέ τι ἐντανύουσιν is a plain present, but the speaker's point is failure; the note keeps ‘they string’.
- 331–333 `i` order (“men of good name … can be those who dishonour”): a faithful rendering of the accusative-and-infinitive with an unstated subject, which the note explains.
- 336 `i` “and let us see” for ὄφρα + subjunctive: the note gives the purpose reading; `l` keeps it; `i` is allowed its own syntax.
- 337 note “pledges herself”: interpretive but harmless.
- 343 note “πεπνυμένος … perfect participle of a verb meaning ‘be wise’”: shipped wording; the glossary entry carries the real caveat.
- 363 `ἐφ’ ὕεσσι` coverage by the known entry for ἐφ’ (‘on, over’): near enough to “among the swine”; no broadening forced.
- 368 `ἐγεγώνει` as imperfect of γεγωνέω: LSJ gives the form as imperfect or as pluperfect of γέγωνα; either is harmless and the glossary and note agree.
- 378 note “τά … the article as a demonstrative”: τά with a noun is the article in a demonstrative shade; the glossary entry for τά covers it.
- 398 `αὐτῷ` (‘for himself’) against the known entry: covered by the intensive sense.
- 411 `i` “under his hand” (supplied touch): already flagged in the note as an English supplement; kept.
- 424–426 `i` “in your halls” for ἐνὶ μεγάροισιν: ‘your’ is context; keeps the address.
- 419–421 `i` “set it to the bow-grip … notched end”: the note flags the uncertainty; the English is rebuilt from the grammar.
- 431 `l` “He spoke, and with his brows he nodded;” / `i` “So he spoke”: matches the new-renderings row exactly.
- The new-renderings rows: every Greek/`l`/`i` entry matches the units; no row changed.

## Pass 2 — gloss.json (104 new forms, 18 broadenings), edited in place

Checked: 104 keys equal `novel-forms.json`; every form of the part has an entry (new or known); no redefinitions; every new entry under 230 characters, typographic ’ only, shape `lemma — meaning; parse`; every broadening keeps the old entry whole. Each of the 104 parses was read against the line it occurs in (case, number, tense, mood, voice, agreement); the 460 known entries were read against their uses in this part.

| form · field | severity | what was wrong | what done |
|---|---|---|---|
| τοῦ (broadening) | moderate | added “neut. gen. sg. ‘of it’ … (τοῦ γὰρ κράτος ‘for the mastery of it’)” — contradicts unit 353's note and the shipped reading of 11.353 and 1.359 (τοῦ = ‘of him’, the speaker); the old entry already covers it | broadening deleted |
| τοσσοῦτον (missing broadening) | moderate | the known entry gives only adverbial ‘so far’ and ‘so much’ with ἄφενος; at 402 it is the quantity ‘so much’ with partitive ὀνήσιος | broadened: old entry whole + “ · also neut. acc. sg. of quantity with a partitive gen.: ’so much’ (τοσσοῦτον ὀνήσιος ’so much of profit’)” |
| ὁμόκλεον | minor | Attic equivalent given as ὡμόκλων; contract imperfect 3 pl. is ὡμόκλουν | corrected |
| πλαγκτέ | minor | quoted English ’you wanderer’ (the house word for ἀλαλήμενος); the unit has “you roamer” | ’you roamer’ |
| χαλκοβαρής | minor | quoted ’bronze-weighted’; unit and table say “bronze-heavy” | ’bronze-heavy’ |
| ἀγκυλομήτεω | minor | meaning “of crooked counsel, crafty” — the new-renderings row fixes “of crooked cunning” and avoids “crafty” | “of crooked cunning (exact sense uncertain)” |
| ἀναστρωφῶν | minor | “contracted (= -ῶν)” says nothing | “contracted (from -άων)” |

Parses read and found correct (no change): αἴθοπι, βιήσεται, βιόν, γλυφίδας, δίωμαι (δίεμαι), δόμεναί, εἰκέλη, εὐερκέος, εὐπηγής, κέλεταί, κατέδονται, κείατο, κεκορυθμένος, μέθιεν (3 pl., subject μνηστῆρες), νεῦσεν, νωμᾷ, οἰός, πήχει, παρέκειτο, πειρήσατο, πιθήσεις, ποιησέμεν, στειλειῆς, τετυκέσθαι, τιτυσκόμενος, ἀριστῆος, ἄεισε, ἆλτο, ἐβάστασε, ἐγεγώνει, ἐθέλωμι, ἐλέγχεα, ἐρέουσ, ἐτράπετο, ἐϋκλεῖας, ἑψιάασθαι, ἔδοιεν, ἔκτυπε, ἕλκεν, ἤμβροτε/ἤμβροτον (1 sg. at 425), ἱλήκῃσι, ὀνήσιος, ὀϊόμεθ, ὄνονται, ὅπλον, and the rest. Broadenings kept as correct: αὐτοῦ (ἄγχι), αὐτῇ (ἐνὶ χώρῃ), γένοιτο, γυναικῶν, διά (ἧκε, ἦλθε), δόμεναι, δώῃ, εἴην, τόν (the arrow), ἐντανύσῃ, ἐπέδησε, ἐπιστάμενος, ἔκαμον, ἡ (the string), ἤ (‘either … or’), ἱπποβότοιο (Elis), ὅτ (ὡς ὅτ’ + finite verb). Known entries checked against their uses (κε/κέ/κεν/κ’ in each construction, μή with infinitive at 384, πρός + gen. at 347, περί + dat. at 407, ἑζετ’ as imperfect, ἄρ, ὥς before enclitic με, ἠὲ/ἢ ‘either … or’, ᾧ, ὅ as relative, ἀνά, ὑπό): all covered by their shipped entries except τοσσοῦτον (above).

Refused in pass 2: the length of the broadened entries (several shipped entries are far over 230 characters already; the build checks the cap only on new entries); the glosser's αὐτῷ/ἐφ’ non-broadenings (see pass 1); ἐγεγώνει tense (see pass 1).
