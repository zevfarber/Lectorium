# Review — odyssey-012 (Odyssey 3.313–403), pass 1 (translation)

All edits were made to `units.json` by script (`t` asserted byte-identical before and after
every write). `new-renderings.md` was brought into line with the changed wording. Every note is
back inside the 25–110 word band. Quotation-mark count is 4 opening / 5 closing in both `l` and
`i`: that is correct, because Nestor's speech opened in odyssey-011 (3.254) closes here at 3.328.
Expect the validator's WARN for it.

Totals: **1 error, 0 major, 7 moderate, 11 minor.**

## Changes made

1. **3.368 · `n` · error.** The note called ἵκετο "an unaugmented aorist". Scanned by hand and
   with `scan_hexameter.py`: ἐπεὶ τεὸν ἵκετο δῶμα needs a **long** ι (foot 5 begins νῑ-). The
   stem vowel is short, as the subjunctive ἵκηται at 355 shows (ῐ by metre). So the long ι here
   is the augment (ι lengthened), which the spelling can't show. This is the drafter's known
   augment weak spot again. The note now says so and points to 355.
2. **3.388 · `n` · minor.** The note called ἵκοντο unaugmented without saying why. Here the
   label is **correct**: the metre (δώμαθ’ ἵκοντο = – ⏑ ⏑ | – …) gives a short ι. The note now
   gives the metrical reason and contrasts it with 368.
3. **3.390 · `n` · moderate.** The note said "ἀνὰ … κέρασσεν is tmesis for ἀνεκέρασσεν". That
   puts back an augment the separated verb doesn't have: κέρασσεν is unaugmented (Attic ἐκέρασε).
   Rewritten as "tmesis of ἀνακεράννυμι; κέρασσεν is an unaugmented aorist".
4. **3.394 · `n` · moderate.** εὔχετο was flatly called "an unaugmented imperfect". Augment of
   εὐ- would be ηὐ-, but Attic itself often leaves εὐ- unchanged (Smyth on the augment of ευ).
   So the spelling can't prove the verb is unaugmented. The note now says "shows no augment
   (ηὐ- would), though Attic too often leaves εὐ- unchanged."
5. **3.402 · `n` · minor.** καθεῦδε was called "unaugmented". Softened to "an imperfect with no
   augment (Attic καθηῦδε or ἐκάθευδε)" for the same reason as 4.
6. **3.393 · `n` · minor.** κεράσσατο is now labelled unaugmented aorist middle (true, ἐκεράσσατο
   would show the augment), to match 390.
7. **3.330 · `l`, `i`, `n` · moderate.** Missed half-line repeat. τοῖσι δὲ καὶ μετέειπε was
   shipped at 2.157 (odyssey-006) as `l` "And among them spoke also …" and `i` "And among them …
   spoke up as well". The draft had "also spoke" and "also spoke among them". Aligned both layers
   with 2.157. Added a note sentence and updated the `new-renderings.md` row.
8. **3.396 · `l`, `i`, `n` · moderate.** Missed half-line repeat. κακκείοντες ἔβαν οἶκόνδε
   ἕκαστος = 1.424 (odyssey-004), shipped `l` "to lie down going, each one went to his own
   house", `i` "each of them went off home to bed". Adapted the draft's line to that wording:
   `l` "they, to lie down going, each one went to his own house," and `i` "the others each went
   off home to bed,". Noted it, and added a row to `new-renderings.md`.
9. **3.399 · `l`, `n` · moderate.** τρητοῖσι λέχεσσι was already shipped at 1.440 (odyssey-004)
   as `l` "the bored bedstead" and `i` "the corded bedstead". The draft's `l` "pierced" broke
   that. Changed `l` to "bored". `i` "corded" stays because it is the shipped wording. I had
   suspected it was a remembered older-translation phrase, but consistency with 1.440 decides
   it. The note now explains the `l`/`i` difference ("bored" is literal, "corded" says what the
   holes were for) and cites 1.440.
10. **3.399 · `l`, `i` · minor.** ἐρίδουπος went from "echoing" to "loud-echoing" in both layers.
    ἐρι- is intensive, the note already glossed it "loud-echoing", and the bare "echoing" dropped
    half the compound. There is no shipped precedent. `new-renderings.md` row updated.
11. **3.357–358 · `l`, `n` · moderate.** The drafter turned the `l` into a passive ("that you /
    should be obeyed by Telemachus") to keep σοί first. That reverses the Greek's voice and
    subject, and the rule's "as far as English can bear" doesn't require it. New `l`: "and it is
    fitting that to you / Telemachus should be obedient, since far better it is so." σοί still
    comes first, the verb is active, the sense is clear, and the line division is unchanged. Note
    adjusted.
12. **3.348 · `n` · minor.** "ἦ … strengthening πάμπαν" was too narrow. ἦ stands before παρά and
    gives weight to the whole description (πάμπαν ἀνείμονος ἠδὲ πενιχροῦ). Reworded. Also added
    that παρά governs τευ … ἀνείμονος. The reading itself (Murray's circumflex ἦ = the affirming
    particle 'truly') is kept, and `l` "truly utterly" is unchanged.
13. **3.372 · `n` · moderate.** On transformation vs. simile, "the words do not settle" was
    stated too flatly. εἰδομένη + dative is the participle used of her real change of shape at
    2.268 (Μέντορι εἰδομένη), which favours transformation. It can also mean just "resembling".
    The note now says both and then says the words alone don't decide it. I also fixed a
    misstatement: "ὣς ἄρα φωνήσασ’ is the elided aorist participle" now reads "in ὣς ἄρα
    φωνήσασ’ … φωνήσασ’ is the elided aorist participle". The species hedge (sea-eagle / osprey
    / lammergeier proposed, name used only as a label) is kept.
14. **3.326 · `n` · minor.** δῖος of a place. The table's δῖος row ("heavenly") and every other
    shipped δῖος (Nestor 1.284, Orestes 3.306, Clytemnestra 3.266, δῖα θεάων / γυναικῶν) use
    "heavenly". So "heavenly Lacedaemon" in both layers is right. There is a **live
    inconsistency** in odyssey-010: ἅλα δῖαν at 3.153 is "heavenly brine" in `l` but "bright
    salt sea" in `i`. It is not harmonised here. The note now states it, and so does the
    `new-renderings.md` row.
15. **3.327 · `n` · minor.** Added the source of "the unerring truth": νημερτὲς ἐνίσπες at 3.98
    (odyssey-009), where `l` and `i` both end "tell me the unerring truth." Verified. The same
    two words here make the borrowing right.
16. **3.375 · `n` · minor.** ἄναλκις was rendered "cowardly" at 3.310 (odyssey-011, of Aegisthus)
    and "strengthless"/"feeble" here. It isn't a stock epithet, so the variation is allowed. It
    is 65 lines apart in the same speech-scene, though, so the note now says so.
17. **3.391 · `n` · minor.** Arithmetic. "Laid down for ten years" became "'in the eleventh
    year': opened when ten full years had passed since it was laid down". That is Greek
    inclusive-style ordinal counting. The `l`/`i` "in its eleventh year" was already right.
18. **3.374 · `n` · minor.** "The second half of the fixed approach formula" became "the closing
    half-line of the fixed two-line approach formula". The borrowed words ἔπος τ’ ἔφατ’ ἔκ τ’
    ὀνόμαζε are only half of the formula's second line.
19. **3.403 · `n` · minor.** The πόρσυνε hedge said "can also imply that the wife shares the
    bed", which was a little assertive. It now reads "Of a wife it has been taken to mean that
    she shares the bed too, but the words say only that she made it ready."

To keep the band, I also trimmed a few redundant clauses from the notes at 324, 346, 375, 390,
397 and 402 (for example, a repeated gloss of πομπῆες, and "the pronoun comes first"). Nothing
substantive was removed.

## The drafter's flagged judgment calls: how each was settled

- **Cut 3.318–322 after τοῖον (321): accepted.** The alternative was a cut after εἰλήλουθεν
  (318), which splits the main verb from its close appositional expansion ἐκ τῶν ἀνθρώπων (of
  ἄλλοθεν). The ὅθεν τέ περ clause at 321 has a new subject (the sea, the birds), so the syntax
  pauses most there. The result is 3½ + 1½ lines.
- **Cut 3.346–350 after πενιχροῦ (348): accepted, with a note.** A cut after ἄλλοι (346) would
  also have been legal (346 | 347–350 = 4 lines). But τό γ’ is proleptic and ties the ὡς-clause
  tightly to the wish. The ᾧ-clause that starts at 349 only expands the pauper. The note already
  gives the reason.
- **Cut 3.395–401 into 395–396 / 397–399 / 400–401: accepted.** Both cuts fall at a μέν/δέ or δέ
  hinge (οἱ μέν | τὸν δ’; πὰρ δ’ ἄρ’). 397–401 as one unit would be 5 lines, over the limit.
- **Break at 335/336 (ἔοικεν·): accepted.** The note at 335 explains Murray's raised point, and
  the note at 336 ties the infinitives back to it. `i` reads "…and it is not fitting: we should
  not sit on long at the feast of the gods, but go home." That's sensible, and the colon carries
  the dependency. I considered restoring "For" (γάρ) at the head of 335 `i` and refused: the
  previous unit's `i` already ends "for it is time for that", and a second "For" adds nothing.
- **3.327 "the unerring truth" from 3.98: verified** character for character in odyssey-009, and
  it fits. The note now cites it (change 15).
- **3.401 ὄρχαμος ἀνδρῶν "chief of men": accepted.** "Chief" is not a fixed rendering anywhere.
  It is only in the "avoided" column for ἡγήτωρ, and the only shipped use is a free `i` at 1.245
  for ἄριστοι. No collision with ἡγήτωρ "leader", ποιμένι λαῶν, or ἄναξ ἀνδρῶν.
- **3.348 ἦ: reading kept, note sharpened** (change 12).
- **3.372 φήνη: species hedge kept; transformation/simile statement corrected** (change 13).
- **3.373 ὅπως 'when': accepted.** The temporal use of ὅπως (= ὅτε/ὡς) is recognised in the
  lexica with this line cited, and the note gives the 'how' alternative too.
- **3.378 Τριτογένεια, 3.382 ἦνις, 3.385 Παλλάς: accepted.** Each note says the meaning is
  unknown, uncertain or disputed and lists the ancient explanations without choosing one.
  ἦνις is "yearling" in both layers, with the uncertainty in the note, which is the same handling
  as ἀμύμων "blameless".
- **3.392 κρήδεμνον / ἑνδεκάτῳ ἐνιαυτῷ:** κρήδεμνον as the jar's covering is right (LSJ's
  wine-jar sense). The arithmetic wording is tightened (change 17).
- **3.399 τρητοῖς / ἐρίδουπος: resolved against the 1.440 precedent** (changes 9, 10).
- **3.403 πόρσυνε: hedge tightened** (change 19).
- **3.358 passive `l`: replaced** (change 11).
- **3.326 δῖαν: kept "heavenly"; inconsistency in 010 stated, not harmonised** (change 14).
- **3.337 ἦ ῥα, precedent at 2.321: verified.** It is in **odyssey-008** (2.321–434), not
  odyssey-006 as the brief said. Shipped as `l` "He spoke", `i` "So he said". The draft's "She
  spoke, the daughter of Zeus" / "So said the daughter of Zeus" matches.
- **3.328 ψεῦδος δ’ οὐκ ἐρέει· = 3.20: verified character for character.** odyssey-009 has the
  unit `t` "ψεῦδος δ’ οὐκ ἐρέει·", `l` "and a falsehood he will not speak;", `i` "he will not
  tell a falsehood;", identical to the draft. The second half, μάλα γὰρ πεπνυμένος ἐστίν., differs
  from 3.20's ἐστί. only by movable ν. It is not a validator-identical unit, but its `l`/`i` ("for
  he is very prudent.”") match 3.20 anyway.
- **Mark at 3.375 "Nestor speaks again": accepted.** The speech opens addressed to Telemachus.
  The turn to prayer at 380 happens inside it, with no narrator line in between, and the note at
  380 says so. "Nestor prays" would mislabel the first five lines.

## Other checks, no change needed

- **Speech boundaries and quotation marks.** odyssey-011's last unit (3.311) has no closing ”
  and its note says the speech continues. The draft's 3.313 has no opening “ and no `mark`. The
  speech closes with ” at 3.328 in both layers. Athena 3.331–336, Nestor 3.346–355, Athena
  3.357–370 and Nestor 3.375–384 each open with “ and close with ” in both `l` and `i`. `mark`
  appears only on 331, 346, 357 and 375. `p` is on exactly Murray's nine ¶ lines.
- **Full repeated-line scan** (every line against every published unit, plus a 4-word-sequence
  scan). Whole-line repeats are 338 = 1.146, 339 = 1.148, 356 = 1.178/1.221/3.25/3.229, and
  389 = 1.145, all with shipped wording reused. The only internal repeat is 342 = 395. The
  half-line repeats at 327 (3.19), 328 (3.20) and 374 (2.302) are handled correctly. The two
  missed half-lines, 330 (2.157) and 396 (1.424), are fixed above.
- **House table.** γλαυκῶπις Ἀθήνη (330, 356, 371), θεά, γλαυκῶπις Ἀθήνη, τὸν δ’ αὖτε προσέειπε,
  ὣς ἔφατ(ο) "So he spoke" (329, 385), Γερήνιος ἱππότα Νέστωρ (386, 397), πεπνυμένος "prudent"
  (328), θεοειδής (343), ξανθὸς Μενέλαος (326), ὦ γέρον (331), Ὀδυσσῆος φίλος υἱός (352),
  θεῖος "divine" (398), δῖος "heavenly" (326), κλέος ἐσθλόν (380), αἰδοίη "revered" (381),
  μεγάθυμος (364, 366), νηῦς θοή "swift ship" (347), κοίλη νηῦς "hollow" (344, 365),
  (νηῦς) μέλαινα "black" (360, 365), κούρη Διὸς αἰγιόχοιο (394), καθαπτόμενος (345),
  ὣς ἄρα φωνήσασ’ (371), ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζε (374), Παλλὰς Ἀθήνη (385), ταμίη
  "housekeeper" (392). All are exact.
- **Every other augment label** (νώμησαν, βάλλον, σπεῖσαν, κατέρυκε, ἕλε ×2, θαύμαζεν, ἴδεν,
  κοίμησε, πόρσυνε unaugmented; ἔβαν as epic ἔβησαν; ὤιξεν augmented οἰ- → ὠι-; ἐπέλειβον,
  ἐπεστέψαντο, κατέλεξας augmented) was re-derived and is correct.
- **Every line-position claim** (ἐλθεῖν at the head of 318, νῦν at the head of 366, the line-end
  θεά, γλαυκῶπις Ἀθήνη, ψεῦδος first, ἐστίν at line end, the held-back Τηλέμαχον at 398) was
  checked against the line and is true.
- **Every cross-reference** (1.1, 1.55, 1.145–148, 1.178, 2.157, 2.267, 2.268, 2.302, 3.5,
  3.19, 3.20, 3.36, 3.98, 3.103, 3.153, 3.199, 3.211, 3.254, 3.310, and the internal ones) was
  checked against the published JSON or the packet.

## Findings considered and refused

- **"Most glorious" (κυδίστη) against the table's φαίδιμος "glorious".** Refused. The table
  already gives "glorious" to the κῦδος-family ἐρικυδής ("a glorious feast"). κυδίστη shares that
  root, and the superlative keeps it distinct from φαίδιμος.
- **3.345 `i` drops αὖ; 3.402 `i` drops αὖτε.** Refused. `l` keeps "in turn" both times, and the
  `i` loss is idiomatic, not a change of sense.
- **3.401 `i` "the one of his sons who was still unmarried"** implies he is the only one, which
  the Greek does not say outright. Refused. It is the natural implication of singling him out.
- **ἦ (3.337) "found almost only in this form".** Refused. That is true of Homer, and close
  enough for Attic, where only ἦν/ἦ δ’ ὅς occur.
- **Typographic ‘ ’ versus ASCII ' for glosses in notes.** Refused. odyssey-010 and odyssey-011
  use ‘ ’, while 001–003 and 005–009 use ASCII. The question is open in QUESTIONS.md (raised at
  005/006), so I did not normalise it here.
- **Mark placement drift in published parts** (for information, not changed). odyssey-010 and
  odyssey-011 put `mark` on the narrator's introductory line (for example 3.229 "Athena speaks"
  on τὸν δ’ αὖτε προσέειπε…). conventions.md and odyssey-007–009 put it on the speech's first
  unit, and this draft follows the rule.
- **Published error found in passing, not fixable here:** odyssey-004's note at 1.424 calls ἔβαν
  "the unaugmented aorist of βαίνω". It is augmented (ἔ-βαν = ἔβησαν). This draft's note at 396
  is correct. Worth a line in QUESTIONS.md.

## Pass 2 (glossary)

Checked all 170 novel entries and all 9 broadenings in `gloss.json` against the line each form
comes from. Edits were made by script (load, change named keys, write back, same `indent=1`
layout). After the write, every entry passed these checks: no ASCII ' or backtick, 230 chars or
fewer, and every `__broaden__` value starts with the exact `known-forms.json` text followed by
` · `. The last check was done character for character by `startswith`. All 9 original
broadenings passed it too. `units.json` was not changed. I cross-checked every note that makes
a grammatical claim (augment, tmesis, contraction, homograph) against the glossary. After the
fixes below, none contradicts the glossary except the two shipped entries under "For
QUESTIONS.md".

Totals: **0 error, 0 major, 17 moderate, 52 minor.** That is 64 novel entries rewritten, 2
broadenings corrected, and 3 broadenings added.

### Changes made — moderate

1. **ὀνόμαζεν · gloss · moderate.** "= ἐξωνόμαζεν" put back an augment the verb doesn't have.
   ὀνόμαζεν is unaugmented (Attic ὠνόμαζε). This is the same slip pass 1 fixed in the 390 note.
   The entry now says "impf. 3 sg., unaugmented (= Attic ὠνόμαζε); with ἐκ in tmesis … ’called
   by name’". This agrees with the 374 note (ἐξονόμαζεν).
2. **ἀνὰ (broadening) · gloss · moderate.** Same error: "ἀνὰ … κέρασσεν = ἀνεκέρασσεν". Changed
   the appended reading to "(ἀνὰ … κέρασσεν, from ἀνακεράννυμι ’mix up’)". The old text is
   intact.
3. **νέον (broadening) · gloss · moderate.** At 367, οὔ τι νέον γε agrees with χρεῖος, which is
   the subject of ὀφέλλεται. So the form is nominative, not "neut. acc. sg.". The appended
   reading is now "neut. nom./acc. sg., ’new’ (οὔ τι νέον …, of a debt)".
4. **κνέφας · gloss · moderate.** Parsed as "neut. acc. sg." But in ἐπὶ κνέφας ἦλθε (329) it is
   the subject. Now "neut. nom./acc. sg.".
5. **ζώω · gloss · moderate.** "Epic uncontracted (= Attic ζῶ)" is false. ζώω is a separate
   epic stem, not an uncontracted ζάω. The form can also be indicative. Now "ζώω (Attic ζάω) —
   live, be alive; pres. indic. or subj. 1 sg. (= Attic ζῶ)". The lemma matches the shipped ζώει.
6. **δεπάεσσι · gloss · moderate.** "(= Attic -άεσσι/-ασι)": -άεσσι is not Attic. Now "(= Attic
   δέπασι)".
7. **κεράασθε · gloss · moderate.** It was called "uncontracted" and "distended" at once, and it
   gave the Attic with the wrong accent (κεράσθε). The form is distended from contracted κερᾶσθε,
   and it can be indicative as well as imperative. Now "κεράννυμι (epic pres. κεράω) … pres.
   imper. or indic. mid. 2 pl., with distended vowel (= contracted κερᾶσθε)". This matches the
   332 note.
8. **καταλέξεται · gloss · moderate.** The lemma "καταλέγομαι" is not an LSJ headword. Now
   "καταλέγω — lay down; mid. lie down (from λέγω ’lay’ …; distinct from καταλέγω ’recount’)".
   I added "(epic aor. subj. has the same form)" to keep the entry general, following the shipped
   καταλέξω ("fut. 1 sg. or aor. subj. 1 sg.").
9. **λεξαίμην · gloss · moderate.** The lemma "λέχομαι" is not an LSJ headword. It is λέγω ’lay’,
   mid. ’lie down’. I dropped "potential", which belongs to κε in the line and not to the form.
10. **πάρα · gloss · moderate.** It was lemmatised as πάρειμι with "pres. 3 sg./pl.". LSJ puts
    πάρα = πάρεστι/πάρεισι under παρά, and the shipped πάρ also uses παρά. There is also a
    genuine homograph: παρά in anastrophe after its noun. Now "παρά — beside; πάρα (accent drawn
    back) stands for πάρεστι/πάρεισι … · also prep. placed after its noun (anastrophe)".
11. **πόρσυνε · gloss · moderate.** It was labelled "impf." only, with the gloss ’was making
    ready’. The imperfect and the liquid aorist of πορσύνω are spelled alike, and the 403 note
    rightly says "past form". Now "impf. or aor. 3 sg. (the forms coincide), unaugmented".
12. **ἵκετο · gloss · moderate.** The entry was tied to this line's metre ("a metrically
    lengthened ι shows the augment"). An entry has to hold for the form everywhere, and ἵκετο
    with a short ι would be unaugmented. Rewritten as a general statement: long ι by metre means
    augmented, short means unaugmented. The augment analysis (ῑ in augmented tenses of ἱκνέομαι)
    is unchanged and still agrees with pass 1's fix to the 368 note.
13. **ἵκοντο · gloss · moderate.** Same problem the other way round ("unaugmented (short ι,
    unlike augmented ἵκετο)"). Rewritten in the same general form. It agrees with the 388 note.
14. **καύκωνας · gloss · moderate.** "Location and identity not otherwise specified in Homer" is
    a claim about the rest of the poems, and it is doubtful (the Iliad names Caucones among the
    Trojan allies). Cut to "Καύκωνες — the Caucones, a people; masc. acc. pl.".
15. **τοῖον · `__broaden__` (new) · moderate.** The glosser said this could not fit under the cap.
    It does. The old entry is 198 chars; with " · also ’so’, qualifying an adj." added it is
    **230**. That is the μέγα τοῖον sense at 321, 'so great', which the old adverbial 'in such a
    way' does not give.
16. **ὄφρ · `__broaden__` (new) · moderate.** Also said not to fit, and it does. The old entry is
    199 chars; with " · also ’while’ + ἄν and subj." added it is **229**. That is ὄφρ’ ἂν … ζώω
    at 353. The old entry had temporal ὄφρ’ only with the indicative.
17. **ὅπως · `__broaden__` (new) · moderate.** Also said not to fit, and it does. The old entry is
    209 chars; with " · also ’when’ = ὅτε" added it is **229**. That is the temporal use at 373
    (LSJ cites the line). The old entry already has 'how', so both readings the 373 note offers
    are now present.

### Changes made — minor (52)

- **Lemma or label precision (8).** αἰδοίῃ lemma accent (αἰδοίος → αἰδοῖος). ἵληθι headword
  order (ἵλημι, mid. ἵλαμαι; Autenrieth and Cunliffe give ἵλημι). ἐπαρξάμενοι (headword ἐπάρχω,
  mid. ἐπάρχομαι). φάγωσιν ("root ἐφαγ-" → "aor. ἔφαγον"; it also gave a present κατεσθίωσιν as
  the equivalent of an aorist). καθεῦδε ("unaugmented" → "no augment shown …", aligned with pass
  1's hedged 402 note). ἔφησθα ("epic ending" while also calling ἔφησθα Attic → "the old ending
  -σθα (Attic ἔφησθα or ἔφης)"). φήνῃ (added lammergeier to the proposed species, matching the
  371 note; still "species uncertain"). αὐδησάσης (dropped "governed by ἔκλυον").
- **Genuine homographs added with " · " (3).** ἐχόντων (· also pres. imper. 3 pl.). ἡγεμόνευε
  (· also pres. imper. 2 sg.; "augment not visible on ἡ-" added rather than any
  augmented/unaugmented claim). ῥέξω (fut. 1 sg. or aor. subj. 1 sg.).
- **Entries pinned to this passage, made general to the form (41).** βοῦν, γεραιός, γλώσσας,
  δεινόν (it also said πέλαγος was "understood", but the noun is expressed at 321), εὐρυμέτωπον,
  θάμβος, θαρσύνω, κάρτος, κίοιτε, καλά, κοίτοιο, κρήδεμνον ("here transferred"), λέχος, νέῳ,
  παίδων, σοῖς, σοῖσιν, τάμνετε, τρητοῖς, τό, φάος, φιλότητι, χρεῖός, ἀγακλυτὰ, ἀλάλησο,
  ἀποσφήλωσιν, ἄλλοις, ἄνασσ, ἐμὰ, ἐνεύδειν, ἐριδούπῳ, ἐσθλόν, ἑνδεκάτῳ, ἔλθῃς, ἔλποιτό, ἔλυσε,
  ἔπιον (aor. 1 sg. or 3 pl.), ἰκριόφιν (-φι serving as gen. or dat.), ὀλίγον, ὀλύμπια, ὅσον.
  Each had either "agreeing with X" or "(construction) here", or gave only the one case/gender
  of this line where the form is ambiguous (e.g. σοῖσιν "neut." only, ἐσθλόν "neut. acc." only).

### Augment labels re-derived (no change needed)

βάλλον, θαύμαζεν, κέρασσεν, κεράσσατο, κοίμησε, νώμησαν, σπεῖσάν (all unaugmented, each ≠ its
ἐ- form); κατέρυκε broadening (unaugmented, augmented would be κατήρυκε); ἐπέλειβον, κατέλεξας,
ἤγαγεν, ἤθελε, ἔδυ, ἔλυσε, ἐτίμα, ἔκλυε (augmented); ἱέσθην (augment invisible, no claim made);
εἰλήλουθεν (perfect, no augment question). All correct.

### Findings considered and refused

- **δῖαν broadening unnecessary?** The old entry's 'heavenly, divine, illustrious; fem. acc.
  sg.' already covers Λακεδαίμονα δῖαν in meaning and parse. The appended place-name reading is
  not needed, but it is true and under the cap, so I left it.
- **ὁμηλικίη broadening** ("predicated of a plural subject") against the 363 note's "in
  apposition to πάντες". Refused as a contradiction: the two describe the same construction.
- **ἰδόντας lemmatised under ὁράω** rather than LSJ's εἶδον. Kept, because the shipped ἴδεν uses
  ὁράω and consistency within the glossary decides it.
- **ἔκλυε / ἔκλυον "aor."** (LSJ also treats ἔκλυον as an impf. with aorist force). Kept, to match
  the shipped ἔκλυον.
- **αὐτόετες headword** (LSJ may print αὐτοετές). Not changed: I couldn't confirm the LSJ accent
  from the permitted sources with confidence, and the entry is otherwise right.
- **ἦνις** is "a year old, yearling (of a calf); rare word, precise sense not certain". That is
  correct as it stands (Cunliffe queries it too) and agrees with the 382 note.
- **βάλλον / ἐπέλειβον as 1 sg.** too. Not added: the homograph (impf. 1 sg.) is trivially
  regular, and the entry is not wrong for the form.

### For QUESTIONS.md (cannot be fixed here — shipped entries are additions-only)

- **κακὸν** is already **329 chars** in the shipped glossary, over the 230 cap before anything is
  added. At 375 it is predicative 'base, cowardly'. Adding that is impossible without replacing
  the entry. Genuinely blocked.
- **Τηλεμάχοιο** is already **235 chars**, also over the cap. Its use at 364 (gen. after
  ὁμηλικίη) is arguably covered by "plain possessive gen.". Genuinely blocked either way.
- **τοῖον, ὄφρ’ and ὅπως were not blocked**: they are broadened above (230 / 229 / 229).
- **ὤιξεν** is shipped as "aor. 3 sg., unaugmented". That is wrong: οἰ- → ὠι- is the augment,
  which the 390 note correctly says. Shipped entry error, needs a decision.
- **ἔκ** is shipped with "(ἔκ … ὀνόμαζε = ἐξωνόμαζε)". This restores an augment the separated
  verb doesn't have (should be ἐξονόμαζε). The same class of error was fixed in this part's
  ὀνόμαζεν and ἀνά.
