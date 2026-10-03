# odyssey-061 (12.371–453) — reviewer pass 1

Edited `units.json` in place by script (`t` untouched, checked unit by unit; `l` line counts still equal `t`).
38 field edits in 27 entries: **1 high, 12 medium, 14 low**. Nothing was edited outside `units.json`
(see "For the controller" for two items that live in other files).

Checked: every note label and cross-reference against the line (all `ln`, ¶ marks and sense-unit cuts agree
with the packet); Greek → `l` word by word; `l` ↔ `i`; every repeated line or half-line against the
published parts (word-trigram search of all published units); the house table and `new-renderings.md`;
quotation marks, including the last unit of odyssey-060 (ends with a colon, no mark; the Odysseus speech
opened at 9.2 is still open, so `“` at 371 opens only the nested cry).

## Changes

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 413 | n | **high** | “κάππεσ’ … with the κ assimilated to the following π” is false: it is the τ of κατ- that assimilates | “with the τ of κατ- assimilated to the following π” |
| 399 | l, i, n | medium | ἱστὸν … ἀνά θ’ ἱστία λεύκ’ ἐρύσαντες is the shipped 9.77 half-line (odyssey-039: “having hoisted” / “hoisted the white sails”); draft said “hauled up” | l “the mast having set up and the white sails having hoisted.”, i “… hoisting the white sails.”, note “having hoisted” |
| 379–381 | l, i, n | medium | οὐρανός rendered “heaven”; the house phrase εἰς οὐρανὸν ἀστερόεντα is “starry sky” (table, odyssey-044), and 11.18 ships ἀπ’ οὐρανόθεν “from the sky” | “starry sky”, “from the sky” in l, i and the note |
| 391–392 | l, i | medium | νείκεον “rebuked”; the table row for νείκεσέ τ’ ἄντην lists “rebuked” as avoided and fixes “reviled” (shipped in odyssey-034 and 035) | “reviled” in l and i |
| 391 | n | medium | “as the next verb, νείκεον ‘I rebuked’ … shows” that κατήλυθον is first person; νείκεον is the same form for 1 sg and 3 pl, so it shows nothing | rewritten: first person because Odysseus goes down to the men; νείκεον agrees (form could be 3 pl); δυνάμεσθα widens to “we” |
| 399, 403 | l | medium | Κρονίων given as “the son-of-Cronus”; every shipped Κρονίων (odyssey-004, 009, 010, 020, 045) is “the son of Cronus” in `l`; only the vocative Κρονίδη is hyphenated | “the son of Cronus” in both units (i unchanged) |
| 420–422 | n | medium | “οἱ is ‘from it’”: οἱ is a dative, not “from”; the sense “out of” comes from ἐκ | “οἱ is a dative ‘to it’, the ship, which with ἐκ gives ‘out of it’” |
| 422–423 | n | medium | packet flag: ἐπίτονος scans only with its first syllable lengthened (scanner: ἐ- long in foot 1; four-short-syllable word, cannot otherwise start a hexameter); hand-scanned: ἐ(–)πί(⏑)το(⏑) | added: “The line is metrically irregular as transmitted: the first syllable of ἐπίτονος, short by nature, has to be read long to make the first foot.” |
| 452–453 | l, i, n | medium | the tale Odysseus opened at 9.2 (reopened 11.378) ends here (13.1 is narrator); no closing mark on its last unit, so the speech never closes (cf. 054 at 11.332) | `”` added to l and i; note says the mark closes the whole tale. Validator will WARN 3 open / 4 close in this part — say so in LOG |
| 401 (399 unit) | l, i | medium | αἶψα rendered “at once”; table row καρπαλίμως keeps “quickly” for αἶψα, ὦκα, θᾶσσον (αὐτίκα is “at once”); shipped αἶψ’ εἴσβαινον is “quickly went aboard” | “quickly” in l and i |
| 407 (and note at 407) | l, i, n | medium | same: αἶψα γὰρ ἦλθε “for at once came” | “for quickly came” (l), “for quickly the West Wind came” (i), note “for quickly” |
| 427 | l, i, n | medium | ὦκα rendered “swiftly”; “swiftly” is reserved for θοός/ὠκύς (same table row) | “quickly” in l, i, note |
| 424 | l | medium | ὁμοῦ (“together”) unrendered in `l` (the note glosses it) | “jointly the keel and the mast as well” |
| 425 | l, i | low | φερόμην ὀλοοῖς ἀνέμοισιν is half of shipped 9.82 “carried by deadly winds”; draft added “the” (no article in Greek) and “along” | “carried by deadly winds” in l and i |
| 387–388 | l, i | low | μέσῳ ἐνὶ οἴνοπι πόντῳ is shipped (023, 032) “in the middle of …”; draft “in the midst” | “in the middle” in both |
| 431 | l | low | half-line ἀνερροίβδησε θαλάσσης ἁλμυρὸν ὕδωρ is shipped (059 12.235) “sucked down the sea’s salt water”; draft reordered | “sucked down the sea’s salt water” (i already matched) |
| 410 | l | low | ὅπλα τε πάντα is shipped (049) “and all the gear” | “and all the gear” |
| 403 | l, n | low | τὴν νῆσον rendered “that island”; the same words are shipped (059 12.201) as “the island” | “the island”; note adjusted |
| 372 | l | low | ἦ … μάλ’ : μάλα had no trace in `l` | “truly indeed” |
| 374 | n | low | ὠκέα asserted to be a neuter-plural adverb; it could equally be the feminine agreeing with Λαμπετίη, and I cannot settle it from the aids | hedged: taken as adverb, could be feminine “swift” |
| 376 | n | low | typo “complaint,.” | “complaint.” |
| 382 | l | low | “into Hades’ and” leaves a bare possessive; shipped practice (053, 054) writes “Hades’ (house)” | “into Hades’ (house)” |
| 438 | n | low | “is the usual Greek way to say …” is a general claim the line does not show | “The dative ἐελδομένῳ … μοι names the person for whom they were late.” |
| 439 | n | low | “The time meant is late afternoon” asserted as fact; the Greek says only “for supper” | “the hour of the evening meal” |
| 447 | i | low | ἔνθεν δ’ ἐννῆμαρ φερόμην is shipped (039) “From there for nine days I was carried”; draft reordered | reordered to the shipped wording |
| 450 | n | low | “the narrator turns to the host” — the speaker is Odysseus, “narrator” also means the poet | “Odysseus turns to the host” |
| 451 | n | low | τοι stated flatly as particle, but ἤδη γάρ τοι is dative “to you” in 049; σοί below makes the particle reading better but it is not certain | hedged: taken as particle, could be dative, σοί already names the hearer |

## Considered and refused

- **φαείνω (383) “either subjunctive or indicative”.** The 1 sg ω-form is the same for both, so the note is true as written; it says only that it “continues the future δύσομαι”, which holds for either mood. φάεινε at 385 is correctly the imperative. Kept.
- **ἰφθίμῃ (451).** Note and “mighty wife” agree with the table row ἰφθίμη κούρη / ἴφθιμος “mighty” and with shipped 046 and 050. Kept.
- **τοι at 450.** Dative “to you” is right there (τάδε follows, σοί comes later only at 451). Kept.
- **ἐπ’ αὐτῷ (422).** αὐτῷ is masculine/neuter dative; τρόπις is feminine, ἱστός masculine and just named in the line: “the mast” is the only possible referent; note and l/i agree. Kept.
- **παρέξ + accusative (443).** περιμήκεα δοῦρα is accusative, so the label is true of the line; the gloss “out beside” fits l and i. I cannot check LSJ, so no stronger claim added. Kept.
- **391 first person.** The change from shipped “they” (008, 033) / “we” (017, 019, 051) to “I” is the minimum the Greek needs; l and i otherwise reuse the published wording word for word. Kept.
- **449.** l and i equal shipped 046 and 058 (“a dread goddess endowed with speech” / “who speaks with a human voice”) and the table row; 032 differs only because the Greek lacks αὐδήεσσα there. Kept.
- **ἄτη “ruin” (372) vs shipped “blindness” (4.261).** Different sense of the word (LSJ gives “ruin” as a sense; ἀάομαι keeps “blinded”); the new-renderings row and the note cover it. Kept.
- **ὠκέα “swiftly” vs ὦκα “quickly”.** ὠκύς is “swift” (table), ὦκα “quickly”; the two are told apart on purpose.
- **κατεσκίαον lemma (κατασκιάζω).** Cannot be verified against LSJ here and is only a label in a note; left for the gloss pass.
- **ἔμβαλε “augment absent”, ἀποαίνυτο “unaugmented”.** Both are standard readings of the forms. Kept.
- **“bitterly ironic” (373), “began to show” (394).** Interpretation, flagged as such in the note or justified by the imperfect (“a series of signs”). Kept.
- **`i` 439–441 “after judging”.** Idiomatic for the present participle in a time-clause; l keeps “judging”. Kept.
- **ἀμφ’ ὀβελοῖσι: l “around”, i “upon”.** Follows the table row 3.461 (“around spits” / “on spits”). Kept.
- **ὑπ’ αὐτῆς (406) “beneath it, the cloud”.** νηός is also feminine, but “beneath the cloud” is the standard reading and the note says what is taken. Kept.
- **γε (379, ἐγώ γε) unrendered.** Emphasis only; acceptable in both layers. Kept.
- **Quotation marks.** Draft uses “ ” for the three nested speeches, as odyssey-059 and 060 do (040–058 use ‘ ’; open owner question already in QUESTIONS.md). `mark` on 371, 377 and 385 only, which are the first units of the three speeches. Kept.
- **`about` “rebukes”.** Summary prose, not a rendering. Kept.
- **Unit cuts.** Every cut is at a full stop or ano teleia except 378 (comma inside a five-line sentence, cut where the syntax pauses most) — correct under the four-line rule; every ¶ sits on a unit’s first line. Kept.

## For the controller (not edited; outside `units.json`)

1. `new-renderings.md`: the Κρονίων row gives `l` “the son-of-Cronus”; the unit now says “the son of Cronus” (shipped practice). Amend the row to `l` “the son of Cronus” before it is copied into conventions.md.
2. Row ἄτη: its `i` “to my ruin” stands; add if wanted that shipped 4.261 reads “blindness” (different use).
3. LOG: the closing `”` at 12.453 ends the tale opened at 9.2; the part has 3 opening and 4 closing marks, so the validator will WARN (expected).

---

# odyssey-061 — reviewer pass 2

Re-checked `units.json` after pass 1 (no new errors introduced by pass 1's edits; `t` untouched, concatenation still equals
the edition and the sha, `l` line counts equal `t`, no ASCII apostrophe or backtick, no `\n` in `i`, note lengths in band;
every repeated line against the published parts; house table and `new-renderings.md`; cross-references 1.9, 1.11, 1.37,
3.3, 9.2, 9.82, 11.378, 12.343, 12.353, 12.370 against the source). Quotation marks: `“` at 371, 377, 385 and `”` at
373, 382, 387, 453 (3 open, 4 close in `l` and `i`). `validate_odyssey.py` only WARNs on an open/close mismatch (section 5)
and `tr`/`sc` are not in the draft file, so nothing there fails; the WARN stays expected (see LOG). Then checked `gloss.json`:
all 426 forms covered by the root glossary or this file, no stale keys, no novel key already in the root, every
`__broaden__` entry is the old root entry whole + ` · ` + new reading, every novel entry under 230 characters with only
typographic ’, no line numbers or “here”, every parse tested against its line(s).

**Changes: 12 edits (0 high, 3 medium, 9 low).**

| Line / form | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 437 | l, n | medium | νωλεμέως is “unceasingly” in the table (νωλεμέως κτείνοντο) and in shipped 016, 043, 054; draft had “without slackening” | l “And unceasingly I held on”; note “unceasingly, without slackening” (i “without letting go” = shipped 043, kept) |
| μῆχος | gloss | medium | parsed “neut. nom. sg.”, but at 392 it is the object of εὑρέμεναι (accusative) | “neut. nom./acc. sg.” |
| ὠκέα | gloss | medium | glossed only as neuter-plural adverb, while the note (374) says it may be the feminine agreeing with Λαμπετίη | added “· also fem. nom. sg., epic -έα (= -εῖα): ’swift’” |
| 377 | l | low | “Laertes’ son Odysseus”; every shipped Λαερτιάδης is “son of Laertes” | “the companions of the son of Laertes, Odysseus,” |
| 422 (line 423) | n | low | “The line is metrically irregular” inside a two-line unit; which line was unstated | “Line 423 is metrically irregular as transmitted” |
| 371 | n | low | κοιμήσατε is an unaugmented aorist (Attic ἐκοιμήσατε); note was silent | “without augment” added |
| κοιμήσατε | gloss | low | same: no mention of the missing augment | “unaugmented (= Attic ἐκοιμήσατε)” |
| 435 | n | low | κατεσκίαον called the imperfect of κατασκιάζω; the form (-αον, uncontracted) belongs to κατασκιάω, as the gloss says | “imperfect of κατασκιάω, the epic form of κατασκιάζω” (left over from pass 1) |
| κεκληγὼς | gloss | low | quoted gloss ’roaring’; l, i and note say “screaming” | ’screaming’ |
| φαείνω | gloss | low | “pres. 1 sg.” only; the note says indicative or subjunctive | “indic. or subj. (subj. with future sense)” |
| ἄραξε | gloss | low | unaugmented aorist (Attic ἤραξε) not marked | “unaugmented (= Attic ἤραξε)” |

## Considered and refused (pass 2)

- **Pass 1's closing `”` at 453 and the 3/4 count.** Consistent with 059/060 (nested cries in “ ”, tale never closed in earlier parts); the validator only warns. Kept.
- **Quotation marks at 373, 382, 387.** Each closes the nested speech opened at 371, 377, 385; the `mark` lines sit on the first unit of each speech. Kept.
- **δικαζομένων “pres. part.” without “mid.”** The entry already says “mid. go to law”. Kept.
- **κατέχυνθ’ (ἐχύθησαν), ἐξεφαάνθη (= ἐξεφάνη), ἠέλι, χαρύβδιος parses.** True of the lines. Kept.
- **δυνάμεσθα, ἔκταμεν, ὄφρ’, ὡς, πολλὸν, ἡ, πέσον, ἐφοίτων, τρόπιος, ἐμυθεόμην, ἰφθίμῃ, εἶχον, τανύπεπλος `__broaden__` entries.** Each starts with the old root entry exactly and adds a reading the line needs; none replaces. Kept.
- **Root entries for the other 330 forms.** Each covers the use here (checked ὅ ‘that’, ὁπότ’ + opt., κατήλυθον 1 sg., ἦλθον 1 sg./3 pl., κεν past potential, μέσῳ, ἱστόν ‘mast’). No further broadening needed.
- **403 note “κυανοχαίτης ‘dark-haired’”.** Matches the table row; kept.
- **ἔνθ’ ἦ τοι “Then indeed”.** Shipped 039 precedent (also “There indeed” elsewhere for the place sense). Kept.
