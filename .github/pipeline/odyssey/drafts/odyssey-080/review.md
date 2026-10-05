# odyssey-080 review (Odyssey 16.308–392)

Reviewer, two passes. `t` untouched (checked: units' `t` reproduce Murray's lines 308–392 character for character; `ln`, `p` and `mark` placement checked against the archive). Edits made by script to `units.json` and, in pass 2, `gloss.json`.

Quotation marks: five speeches, each opened once and closed once in both layers — Telemachus 309–320 (opens 309, closes 318 unit, ending 320), the herald 337 (one unit), Eurymachus 346–350, Amphinomus 355–357, Antinous 364–392. Odysseus's speech closes in odyssey-079 (last unit, ln 305, ends “…τοῖον ἐόντα.” with ”), so 308 correctly carries no opening mark. Murray's 393 is `ὣς ἔφαθ’, οἱ δ’ ἄρα πάντες ἀκὴν ἐγένοντο σιωπῇ` (part 081's first line), so Antinous's speech does end at 392 and the ” on the last unit is right. `mark` is on the first unit of each of the five speeches. Line 363 (`τοῖσιν δ’ Ἀντίνοος μετέφη, Εὐπείθεος υἱός·`) takes the table's wording and the published odyssey-020 wording for that line; 321 and 360 repeat published English identically; 329's repeated line is handled under the ἀγγελίη ruling below. No scansion flags in the packet; nothing to scan by hand.

## The two conflicts the drafter flagged

1. **ἀγγελίη.** The table's ἀγγελίη row (15.314) says `l` "news" ("tell news"), `i` "news", and lists "message" as avoided ("the draft's word, withdrawn at review"). The published odyssey-071 unit shows `l` "a message to tell to…" but that is a unit whose Greek differs from ours (only one line inside our unit repeats), so the validator's whole-unit repetition rule does not bind, and the packet says to reuse the published wording "as far as your sentence allows"; the sentence allows "news". The table is the fixed house rendering, so `l` is changed to "news" at 328–329, 333–334 and 355; `i` already said "news" in the first two and is changed at 355. The odyssey-071 `l` "message" is left as shipped and is a discrepancy of the same kind as the 3.153 and 3.59 notes in the table (flag for the owner; not fixed here because other parts' files are out of scope).
2. **θεῖος "divine king".** The table fixes θεῖος as "divine" ("godlike" reserved for ἀντίθεος); row 11.238 repeats this. odyssey-019's "godlike king" translates a different line (4.621) and only the half-line θείου βασιλῆος coincides, so no repetition rule applies. Kept "divine king" at 335, consistent with the table. The shipped 019 line is left as shipped (flag, same kind of discrepancy as above).
   The closing paragraph of `new-renderings.md` ("Two points where…") is a drafter's memo, not a table row; it should not be copied into conventions.md, and its first point is now superseded by the ruling above (`l` says "news", not "message").

## Pass 1: changes to units.json

Severity: high = wrong in the Greek reading or a false statement a reader would be misled by; medium = false or misleading label, or a violation of a fixed house rendering; low = wording, unsupported assertion, small drift.

| line · field | sev | what was wrong | what was done |
|---|---|---|---|
| 328 · l, n | medium | `l` "a message to tell" against table ἀγγελίη "news" (message avoided); note glossed "message, news" | `l` "news to tell to circumspect Penelope"; note "‘news’" |
| 333 · l, n | medium | same: `l` "the same message", note "the same message" | both "the same news" |
| 333 · n | medium | note said ὑφορβός is the man "whom the next unit calls συβώτης"; the next unit (335–336) does not, συβώτης is at 338 | now "whom 338 calls συβώτης" |
| 355 · l, i, n | medium | "urge on a message" / "send on any further message" / "‘message, news’" against the table | "urge on any news" / "send on any further news" / "‘news’" |
| 365 · i | medium | "windy heights": the table's ἄκρις row gives "hilltops" and lists "heights" as avoided; also αἰέν "always" was dropped from `i` | "windy hilltops, always one man after another" |
| 346 · i | medium | ὑπερφιάλως is an adverb on τετέλεσται ("accomplished overweeningly"); `i` made it an adjective of the deed ("a great and overweening deed") and so changed what is said to be overweening | "this journey of Telemachus’s is a great deed, overweeningly accomplished" |
| 348 · l, n | medium | ἐς δ’ … ἀγείρομεν is tmesis (ἐσαγείρομεν "gather in"); note explained ἐς δ’ ἐρέτας ἁλιῆας as "and for oarsmen, seamen" and `l` dropped ἐς | note now names the tmesis; `l` "and let us gather in rowers, sea-men" |
| 374 · n | medium | "νόος … contracted in the dative": νόῳ is the *un*contracted dative (Attic νῷ); βουλῇ is not contracted either | note corrected |
| 370 · n (found in pass 2) | medium | φραζώμεθα called "aorist subjunctive"; it is the present subjunctive of φράζομαι (and the known-forms entry for φραζώμεθα says present) | "present subjunctive" |
| 389 · n (found in pass 2) | medium | ἔδωμεν called "aorist subjunctive"; ἔδω has no aorist, this is the present subjunctive (the glosser's entry says so too) | "present subjunctive" |
| 355b · i | low | "are already inside": "already" not in the Greek | "are inside" |
| 335 · i | low | "maidservants": table δμῳαί has `i` "maids" (`l` "maidservants", which `l` has) | "maids" |
| 384 · i | low | "dividing them fairly among us": table κατὰ μοῖραν `i` is "as is fitting" | "dividing them among us as is fitting" |
| 387 · l | low | "all his paternal goods": adjective πατρώϊα rendered "paternal goods"; table's πατρώϊος rows say "his father’s …" | "all his father’s goods" |
| 370 · i | low | "So let us here plan": Greek has δέ (contrast with the power that led him home), no consequence "so" | "As for us, let us here plan" |
| 372 · n | low | ἀνύσσεσθαι called only "the middle of ἀνύω"; it is the future infinitive and `l` translates it as a future | "the epic future infinitive, middle" |
| 383 · i | low | "open country" for ἐπ’ ἀγροῦ, which the same part renders "in the country" (330) | "in the country" |
| 391 · i | low | "her destined husband": "husband" and "her" are not in μόρσιμος; new-renderings row says `i` "destined" | "comes as the destined one" |
| 330 · n | low | "τέρεν … δάκρυον … is split by tmesis": the tmesis is κατά … εἴβοι, with the phrase between | note reworded |
| 342 · n | low | ἀκάχοντο called "imperfect middle"; it is a (reduplicated) past form, tense not safely "imperfect" | "a past tense, middle in form" (glosser's entry says reduplicated aorist) |
| 358 · n | low | "the crew … now see the suitors do the same": muddled, the crew do not see anything | "what Telemachus’s crew did on landing, the suitors now do" |
| 364 · n | low | "opens many speeches" (claim about the rest of the poem the part cannot show); "Antinous says it bitterly" (tone the Greek does not mark) | first clause now "the house rendering"; second sentence cut |
| 346 · n | low | "he says so sourly": same, unsupported tone | cut |
| 321 · n | low | quoted "ἡ δ’ ἄρ’ ἔπειτα" where the text has ἔπειτ’ | "ἔπειτ’" |

Counts, pass 1: high 0 · medium 10 (8 on first pass, 2 found while cross-checking the glosser's parses) · low 14 · total 24 findings, 26 field edits.

## Pass 1: findings considered and refused

- **θεῖος "divine king" (335)**: kept; see ruling above.
- **ἀγγελίη, odyssey-071 `l` "message"**: shipped file not touched; flagged.
- **309 `i` drops "O" of ὦ πάτερ**: matches the table's ὦ φίλοι `i` "Friends"; kept.
- **310 χαλιφροσύναι "slackness"**: the word is rare; note already says the sense is taken from the parts; kept.
- **313 εἴσῃ**: the note already says the form is rare and the sense from context; no better parse offered, kept.
- **316 δεδάασθαι "reduplicated epic infinitive"**: true of the form; kept.
- **328–329 cut at the comma**: the sentence 328–332 runs five lines; the cut is licensed by the four-line rule; kept.
- **354 / 345 / 363 / 308 whole-line formulas**: checked word by word against the new-renderings rows and the table; `l` and `i` agree; kept. 345 `i` "was the first to speak among them" matches the shipped 2.15 (odyssey-005) wording.
- **324–327 σφ’**: the note says σφι "for them"; the glosser's entry allows σφι or σφε; the translation ("their gear") is the same either way; kept.
- **359 / 325 near-repeat**: lines differ in word order and one particle, so no repetition rule; `l`/`i` for 360 = 326 are identical to 326's, as required.
- **358 `i` "went down to the shore"**: "down" is an English addition for ἐπὶ θῖνα; harmless, kept.
- **36 (372) `i` "ever" / "our purpose" for τάδε ἔργα**: `i` paraphrase, `l` keeps "these deeds"; kept.
- **44 (389) `i` "go on eating up"**: slight aspect drift for an aorist-looking, actually present, subjunctive with μή; reads as prohibition of continuing, which is the sense; kept.
- **384 κτήματα "possessions" (table: χρήματα "goods")**: the table row says κτήματα "takes goods too" but shipped κτήματα is "possessions" in about thirty places including the parallel 2.335 (odyssey-008); kept.
- **38 (376) Ἀχαιούς "the Achaeans" / note "the men of Ithaca"**: context-supported; kept.
- **about**: checked against the units; stands.
- **23 (351) εἴρηθ’**: the note says only "an elided form of the verb ‘say’", which is true; the tense (the glosser says pluperfect, `l` "had been said") is uncertain because the printed θ is not explained by elision before ὅτ’ ἄρ’; the glosser's entry now says so.
- **Table/convention check of all other rows** (ὑπέρβιον, ἕκηλος, θῖνα θαλάσσης, νῆα μέλαιναν, πολυβενθής, ὑπέρθυμοι θεράποντες, περικαλλής, δαίμων, ἐέδνα, βίοτος, ὣς ἔφαθ’, ὦ φίλοι, ὢ πόποι, κατὰ μοῖραν, δῖος ὑφορβός, ἠὼς δῖα, ἠνεμόεις, ἐπασσύτεροι, αἰπὺν φόνον, ἰφθίμη βασίλεια, θυμηδέ’, μόρσιμος): agree with `l`/`i` apart from the changes listed.

## Pass 2: gloss.json

gloss.json was complete when read (80 novel forms plus `__broaden__` with 16 entries). Every novel parse was checked against the line; every `__broaden__` entry was checked to begin with the old entry whole (all did); the known-forms were then scanned for uses in this part their entries do not cover. Format: all under 230 characters, typographic ’ only, no line numbers.

| form · field | sev | what was wrong | what was done |
|---|---|---|---|
| πειράζειν | medium | "+ acc." but in 318–319 the person tried (ἀνδρῶν) is genitive and ἡμέας is the infinitive's subject; also contradicts the known entry πειρητίζω "+ gen." | "+ gen. or acc. of the person tried" |
| ἐράπτομεν | medium | "prothetic ἐ-": it is the ordinary augment, with ρ not doubled (Attic ἐρρ-) | relabelled |
| εἴσιδον (known) | medium | known entry covers aor. 1 sg. only; here 3 pl. ("they saw", 356) | broadened with the 3 pl. reading |
| πάνθ’ (known) | medium | entry says "neut. nom. pl."; here neut. acc. pl. object of μυθήσασθαι (339) | broadened |
| εἴρηθ | low | stated "plpf. … for εἴρητο" as fact; the θ is not explained by elision (ὅτ’ ἄρ’ has a smooth breathing) | hedged: "read as εἴρητο, the printed θ not explained by elision alone" |
| θυμηδέ | low | asserted agreement with χρήματα only; the unit's note and `l` take it adverbially, as a stated choice | "agreeing with χρήματα or used adverbially" |
| κλυτίοιο | low | "an Ithacan man": not shown by the line | "a man whose house is named" |
| πατρώϊα | low | gloss ’paternal goods’ (an interpretation of the English layer) | "’what is one’s father’s’" |
| τέρεν (broaden) | low | "(τέρεν = τέρην, unelided)": τέρεν is the neuter of τέρην, not an unelided τέρην | reworded |
| αὐτῆς, τῆς (broaden) | low | example translation "the same message" | "the same news", to match the ἀγγελίη ruling |
| ἐφ (known) | low | no reading for ἐφ’ ἡμέας (385, distributive "among us") | broadened |
| δοῖμεν (known) | low | entry says "potential with κε"; 385 has no κε | broadened with the κε-less hortatory use |

Counts, pass 2: high 0 · medium 4 · low 8 · total 12 gloss edits (plus the 2 unit notes listed above, found in this pass).

Refused in pass 2: ἔρυσσαν known entry ("= Attic εἴρυσαν") left alone, not wrong; ὀτρύνομεν "aor. subj." (present and aorist subjunctive of this verb are identical in form), left; κε entry has no explicit "+ opt. in a relative clause" reading (391 ὅς κε … πόροι) but the existing "+ opt., potential" and the ἔλθοι broadening cover it, left; "(ν-movable)" labels on -σι subjunctives (ἀγγείλωσι, ἐξελάσωσι, ῥέξωσι) are loose but not false of the -σι(ν) ending, left; ἐγώ before γε (accent) not worth an entry; the broadened αὐτόν / αὔτως / τοί / οὕνεκα / οὕνεκά / στρεφθεὶς / ἔχωμεν / ἔλθοι / ὑπεκφύγοι / ὀτρύνομεν / κε / πᾶν readings are all true of their lines.
