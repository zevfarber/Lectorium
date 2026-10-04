# odyssey-071 review (15.1–85)

Edited `drafts/odyssey-071/units.json` in place (fields `l`, `i`, `n` only; no `t`, `ln`, `p`, `mark` touched). The build was not run. Checked afterwards: l/t line counts equal, no `\n` in `i`, quotation marks balance (5/5 in both layers).

## Changes (line · field · severity · what was wrong · what was done)

| line | field | sev | wrong | done |
|---|---|---|---|---|
| 4 | n | low | "forecourt-room": `forecourt` is the house word for πρόθυρον | "room or porch in front of the main hall" |
| 7 | n | low | μελεδήματα "is from μέλω" (derivation asserted) | "is related to μέλω" |
| 10 | n | high | "Lines 11 and 13, and most of 12, are the words of 3.313–316" muddled: 11–13 repeat 3.314–316 (12 differs only by φάγωσι/φάγωσιν), and what line 10 shares with 3.313 is its ending; also called ἀλάλησο an imperative (label unverified); κατὰ … φάγωσι called "tmesis for κατέδω" (φάγωσι is the aorist of ἐσθίω) | rewritten: 11–13 = 3.314–316, line 10 ends like 3.313, no label on ἀλάλησο, tmesis for καταφάγωσι; added "overbearing, as at 3.315" |
| 10 | l, i | low | unit ends in ";" but the clause runs on into the next unit (and the published 3.315 l has a comma) | ";" → "," in both layers |
| 13 | i | med | "while you make a fruitless journey" turns the μή-dependent subjunctive into a plain temporal fact | "and that you make a fruitless journey" (still under "for fear that") |
| 13 | n | high | "The unit is cut at the ano teleia that ends line 12": false. Murray's ano teleia is mid-line, after ὑπερφιάλους; no stop ends line 12 | note now states what is true (see refused finding 1 for the cut itself) |
| 21 | n | med | μέμνηται and μεταλλᾷ both said to "take the genitives παίδων and τεθνηκότος"; τεθνηκότος qualifies the husband; μεταλλάω's genitive unverifiable; "husband of her youth's marriage" garbled | μέμνηται takes παίδων and κουριδίοιο φίλοιο, τεθνηκότος agrees with the husband; μεταλλᾷ has the same objects understood; κουρίδιος 'wedded, lawful' |
| 24 | l | med | "going home" (ἐλθών has no "home") and "to a maidservant" (δμῳάων is the partitive plural after ἥ τίς) | "having come … to one of the maidservants, whichever seems …" |
| 24 | n | low | partitive not mentioned | added "partitive after ἥ τίς" |
| 31 (2nd unit) | n | med | "πρίν takes a future indicative here" asserts a construction I cannot verify | now only says καθέξει is the future of κατέχω after πρίν |
| 33 | n | low | πλείειν called "uncontracted" (Attic πλεῖν is the contraction, Homer's form is not simply uncontracted) | "Homeric infinitive of πλέω (Attic πλεῖν)" |
| 36 | n | med | "Line 38 and the first half of 39 are 13.404–405": all of 39 is 13.405 (οἶδεν for οἶδε) | corrected |
| 46 | n | high | ὑφ’ … ζεῦξον called tmesis for ὑποζεύγνυμι; ὑφ’ stands before its noun ἅρματ’ and is the preposition 'under' with the accusative | rewritten; line 80 note's "compare ὑφ’ … ζεῦξον at 47" re-pointed to "ζεῦξον ὑφ’ ἅρματ’" |
| 49 | n | low | "both young men would drive": unverifiable | "the plural shows he speaks for both of them" |
| 51 | n | low | "subject of all three verbs" (two finite verbs, two participles) | "subject throughout" |
| 56 | n | high | said the English pronoun "is as in" 10.541 without telling the reader the speaker is Peisistratus; "ἤλυθεν is the unaugmented aorist": false (ἤλυθεν is augmented; the published 10.541 note has it right) | note: "the speaker is Peisistratus, so read 'he'; the English says 'she' because this line repeats 10.541 and the published English is kept"; ἤλυθεν "epic aorist (Attic ἦλθεν)"; "as Peisistratus predicted at 50" |
| 57 | n | low | καλλικόμοιο glossed from κάλλος | "καλλι- 'fair' + κόμη" (house reading of καλλι-) |
| 59 | n | med | Telemachus "is named only at 63": he is named at 4, 7, 10, 49 | "whose name does not come until line 63" |
| 59 | n | low | δῦνεν "imperfect of δύω" | "of δύνω" |
| 61 | n | low | "ἐπὶ … βάλετ’ is the aorist middle" read as a tmesis pair; ἐπί governs ὤμοις | rewritten |
| 72 | l | med | "whoever one not willing to go / a guest-friend urges on, and whoever one hastening holds back" can be parsed with "one" as subject | "whoever a guest-friend not willing to go / urges on, and whoever holds back one hastening" |
| 78 | n | low | ἴμεν's "unspoken 'you'" ignores the plural participle | "unspoken subject of ἴμεν, the two guests" |

## Decisions on the two known issues

(a) Line 56 (ὣς ἔφατ’, αὐτίκα δὲ …). `validate_odyssey.py` check 6 fails a unit whose Greek (letters only) equals an earlier published unit unless `l` and `i` are identical, and the build takes the first ratified rendering. So "So she spoke" must stay in both layers for Peisistratus; changing it to "he" would fail the validator. Lawful fix: keep l/i, and make the note tell the reader to read "he" (same remedy as the odyssey-055 and 060 entries). The repeated-line rule is not broken; recorded in QUESTIONS.md for the owner anyway.

(b) Line 12 ὑπερφιάλους. Table rows 6.274, 9.106 and 13.205 fix ὑπερφίαλος as "overweening" and keep "overbearing" for ὑπερηνορέοντες. But the half-line pair 15.11–13 repeats shipped 3.314–316 (odyssey-012), whose English is "so overbearing, lest they eat up everything", and the conventions rule (and the precedent at conventions row πατρίδα γαῖαν, 5.15) is that a repeated line keeps its published English; the packet says to reuse it as far as the sentence allows. Kept "overbearing" in l and i, matching 3.315; the note says "as at 3.315". The shipped rendering contradicts the table; flagged for the owner, not changed (published part).

## Findings refused or not fixable here

1. Unit boundary at 15.12/13 (needs `t`, so out of my remit). Murray prints the ano teleia mid-line, after ὑπερφιάλους. By the tap-unit rule the first unit should end there (lines 10–12a) and the next begin "μή τοι κατὰ πάντα φάγωσι / κτήματα … ἔλθῃς." The draft instead cuts after φάγωσι, where there is no stop. Every other mid-line stop in the part (17, 31, 40, 71, 82 and so on) is cut correctly, so this one is an oversight. The validator does not check it, so it would pass. Repair means moving ὑπερφιάλους· into unit 1 and the rest of line 12 into unit 2 (t, l, i, n; the second unit's `ln` becomes 12). Left for the drafter; in QUESTIONS.md. I made the note true in the meantime and put commas at the join.
2. Line 41 i "A host ought to…" against l "One must…": the Greek subject is generic, but 38–40 are all about the host, so I left it.
3. Line 22 i "have come back from Pylos" ("back" not in εἰλήλουθας): idiomatic and implied by the context; left.
4. Line 8 l "was increasing" / i "has been adding": the imperfect is carried by both; left.
5. Line 20 i "with all your companions" for καὶ πάντας ἑταίρους (companions are a second object of ὀτρῦναι): the sense is the same; left.
6. Line 14 l word order ("Of the suitors you purposely the best men …") is clumsy but follows the Greek and the house row; left.
7. Line 1 note "εὕδοντ’ is the dual participle": accepted (both objects are dual).

## Checked and found true

Cross-references, checked against the Murray text in `source/` and the shipped parts: 3.313–316 (odyssey-012 unit at 313), 4.671 (= 15.29), 4.823 (= 15.30), 13.396 and 13.428 (= 15.32), 13.427 (= 15.31), 13.404–405 (= 15.38–39), 10.541 (= 15.56), 4.155 (= 15.48), 4.156 (= 15.64; spoken by Peisistratus to Menelaus). Position claims checked against the lines: Peisistratus named at 46; ὀτρύνω at 37, 40; ὀφέλλω at 21; ἱέμενον at 69; ἔγειρεν at 8 and 44; Ἀτρεΐδη at 64; 72–73 and 47 references. Repeated lines match the packet's published l/i (15.29–32, 38, 48, 64; l of 11–13). Quotation marks: “ on the first unit of each of the five speeches (10, 46, 49, 64, 68), ” on the last (42, 46, 55, 66, 85); `mark` and `p` correct at every paragraph start (1, 10, 43, 46, 48, 56, 64, 67). Scansion flags: none in the packet.

## Menelaus's speech at 85

Closed with ” at 85. The Greek supports ending there: 80–85 is a complete conditional offer, ending in a four-term ἠέ … ἠέ … ἠέ … ἠέ list that reads as a conclusion, and there is a paragraph break at 86. If odyssey-072 opens with Menelaus still speaking, the ” at 85 must be removed and the validator WARN accepted; nothing in the Greek of 15.80–85 forces that, so it is shipped closed.

## Pass 2 (gloss.json and the re-cut units 4/5)

Units 4/5 (15.10–12a / 12b–13) after the split: l, i, n, quotation marks and `p`/`mark` all correct (the “ stays on unit 4, closes at 42). Unit 4 ends "so overbearing," and unit 5 opens "lest they eat up everything," / "for fear that they eat up everything,", so the fear clause reads through. One edit: unit 5 note said "Lines 12–13 are also 3.315–316", but only the second half of 12 is; now "The rest of line 12 and line 13".

gloss.json: all 86 parses checked against their lines; morphology and cases were right. Changed (all in gloss.json, units.json changed only as above):
- εὐχάλκων "well-bronzed", μώνυχας "single-hoofed", καλλικόμοιο "fair-haired", περίφρονι "prudent": words the table avoids; reworded to the house readings.
- κτῆμα: said nom. sg. with φέρηται passive; the unit (note, l, i) takes φέρηται as middle with the mother as subject, so κτῆμα is acc.; φέρηται now "she may carry off (for herself)".
- ὑποζεύξω: hedged "aor. subj." in a main clause; now fut. 1 sg. (aor. subj. possible in form).
- πλείειν "uncontracted" (as unit note, now "epic form"); ἔγρεο "= Attic ἔγρου" (not a good Attic form, dropped); ἴδῃς "= Attic ἴδῃς" (empty, dropped).
- __broaden__ βάλετ’: new reading called tmesis with ἐπί; the note takes ἐπί with ὤμοις, so it now says "with ἐπί governing the dative".
Other broadenings (αἴσιμα, αὔτως, κέ, κεν, παιπαλοέσσης, πηνελοπείῃ, σιγαλόεντα, φαίνεται, ἱέμενοι) fit their lines and keep the old entries whole.
