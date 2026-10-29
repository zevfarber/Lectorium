# iliad-104 (16.477–568) — review, pass 1 (no gloss.json yet)

Method: every note label checked against the form and the line (and every cross-reference against the archived text of the edition, by script); Greek to `l` word by word; `l` against `i`; `i` for remembered English; quotation marks; every repeated line compared with the shipped English, by script over all published Iliad parts (not only the packet's list). `t` was never touched (checked by comparing every `t` and every top-level field with the original). 63 fields changed in 35 of the 53 units. Findings by severity (table rows below): HIGH 10, MED 15, LOW 13; 38 rows in all.

Severity: HIGH = the house table or a shipped rendering is contradicted, or a note states something false; MED = `l` or `i` misleads or drops a word, or a note claim is wrong but harmless to the English; LOW = polish, or a note made more exact.

## A defect in the packet (reported, not fixed)

The packet's list of repeated lines is incomplete. It misses 16.477–480 (= 5.16–18, iliad-027), 16.527 (= 1.457, iliad-005, a whole unit with identical Greek), 16.503 (= 13.618, iliad-083) and the half-line αὐτὰρ Ἀχαιούς at 16.553 (also 4.514, 9.1 and 15.61, in iliad-026, iliad-052, iliad-091, with different continuations). The drafter therefore could not have known them; the rows below that fix 477–481 follow from this. packet.py should be checked for lines whose published unit begins or ends mid-line.

## Changes

| line · field | sev | what was wrong | what done |
|---|---|---|---|
| 477–478 · l, i, n | HIGH | The first lines are 5.16–17 (shipped, iliad-027): "and he did not hit him", "left shoulder"; here "did not strike him" and the clumsy "shoulder, the left one". | l "over Patroclus’ left shoulder went the tip of the spear, and he did not hit him"; i "did not hit him"; note "‘nor did he hit’". ("tip" kept, see refused findings.) |
| 480–481 · l, i, n | HIGH | 16.480 is the same line as 5.18, shipped as "the shaft did not escape in vain" / "his shaft did not leave his hand in vain"; the draft had "flew from the hand" and its note and new-renderings row cited "16.407", which is a different line (the phrase is at 14.407 and 22.292). | l and i reuse the shipped English; note says the line is also 5.18; new-renderings row corrected. 481 "struck" changed to "hit" to match 5.19. |
| 481 · l, i, n, new-renderings | HIGH | ἁδινὸν κῆρ given "the thick heart"; the Odyssey table fixes ἀδινὸν κῆρ "thronging heart" (19.516) and ἁδινός "thronging" (2.87, 2.469). The note called ἁδινός "thronging of flocks" (2.87 and 2.469 are bees and flies) and the new-renderings row wrongly said "thronging" was being kept for flocks. | "thronging heart" in l and i; note: "used of bees at 2.87 and of a heart at Odyssey 19.516"; row corrected. |
| 482–484 · n | MED | ἐξέταμον called "unaugmented". It is augmented (ἐκ- + ἔ-ταμον). | Note corrected. |
| 487–489 · n | LOW | "The simile has no main verb of its own" is false (ἔπεφνε, ὤλετο are its verbs). | Replaced by "The next unit, with ὣς, gives the thing compared." |
| 490–491 · n | MED | "the end of the line shows what the eagerness is for" is false: the end of the line is the call to Glaucus. | Note says the Greek does not say what he was eager for; the call shows where his mind is. i "was full of eagerness" kept (see refused). |
| 492 · i | MED | μάλα "very much" given as "above all", a comparison the Greek does not make. | "now you very much must be". |
| 494 · l, n | MED | l "longed for by you" departs from the table (ἐέλδομαι "wishes" in l, "longs" in i, 13.638); the note called the construction unusual but did not say why. | l "wished for by you"; note says elsewhere the one who longs is the subject (13.638, 14.276), so πόλεμος as subject is odd, and the sense is the traditional one. i "your longing" kept. |
| 496, 533 · l, n | LOW | ἐποιχόμενος "going about" in l; the table has "going to and fro" in l, "went about" in i (5.720). | l "going to and fro" in both units; notes follow; i unchanged. |
| 497 · i, n | LOW | καὶ αὐτός "yourself also" lost its καί in i. The note gave μάρναο the ending "-ο (= Attic -ου)", which is wrong for an athematic verb (it is -σο with the σ lost). | i "yourself too"; note corrected. |
| 498–500 · l, i, n | MED | καὶ ἔπειτα not rendered in i; in l "both afterwards … and" mis-pairs the two καί (there are only two: καὶ ἔπειτα, καὶ ὄνειδος). The note's "ἔπειτα is ‘afterwards’" ignored the καί. | l "even afterwards"; i "hereafter too"; note "καὶ ἔπειτα is ‘even afterwards, hereafter’". |
| 498 · n | LOW | κατηφής "downcast" glossed as a man "with his eyes lowered" as if known. | "a downcast look, traditionally that of a man with his eyes lowered". |
| 500 · n | MED | ἀγών "as at 8.200": 8.200 of the Iliad has no ἀγών (the table's 8.200 is the Odyssey's). | Replaced by "ἐν ἀγῶνι also at 16.239". |
| 501 · l, n | HIGH | λαός "the army" in l; the table has "people" in l, "army"/"troops" in i. | l "the people, all of it"; note. |
| 509 · l, i, n | MED | προσαμῦναι "help": the table has προσαμύνω "come to the defence" (5.139, 5.685). | l "come to the defence"; i "come to his defence"; note says no object is given and Sarpedon is meant. |
| 511–512 · l, i, n | HIGH | l "ruin from his comrades": ἑτάροισιν is a dative of advantage ("for"), the shipped 12.334 has "ruin for his companions"; l "him Teucer, rushing on, struck" put "rushing on" next to Teucer, though ἐπεσσύμενον agrees with μιν (Glaucus); i "his comrades" after "he rushed" read as Glaucus’s; "comrades" is not the table’s word (ἑταῖρος "companion"). The note's "takes the genitive as its goal" stated a construction as fact. | l "him, rushing on, Teucer struck … ruin for his companions warding off"; i names Teucer as the one warding off ruin for his companions; note says μιν is the participle’s noun and the genitive is read as the goal. |
| 514 · i | LOW | "Hear me" supplies an object κλῦθι does not have. | "Hear, lord". |
| 515 · n | LOW | ἀνέρι called "to a man" with ἀκούειν. | "a man, the one who is heard". |
| 517–519 · n | LOW | "μοι … (twice)": it stands three times (517, 518, 519). | "three times, at 517–519". |
| 524–525, 561 · l, i, n | HIGH | "comrades" for ἑτάροισι, ἑταίρων; the table (2.417, 4.113) has "companions"; "comrades" is turned down. | "companions" at all three places, in l, i and the notes. |
| 527 · n | HIGH | ἔκλυε called "unaugmented" (it is augmented); the cross-reference gave only 1.43. | Corrected; "and at 1.457" added (the whole unit stands in iliad-005 with the same English, checked). |
| 528 · n | MED | τέρσηνε called the causative aorist "of τέρσομαι". It is the aorist of τερσαίνω. | Corrected, with τέρσομαι "become dry" (519) named beside it. |
| 534 · l, i, n | MED | μακρὰ βιβάσθων "striding with long strides"; the same form is shipped twice (13.809, 15.676) as "taking long strides". | l, i and note follow the shipped English. |
| 538 · n | LOW | The note pointed to the accent at 515 without saying that 538 prints none. | "(here it has none)". Both accent claims checked against the characters printed: 515 εἲς has the grave on ι, 538 εἰς has none. |
| 540 · l, i, n | HIGH | ἐπαμύνειν "ward off for them" / "defend them"; the table and the shipped parts (6.361, 8.414, iliad-039, -075, -082) have "come to the defence of", and the table turns "ward off for" down for ἐπαμύνω. | l "to come to the defence"; i "to come to their defence"; note. |
| 543 · i | MED | δάμασ’ "subdued": the table's i for δαμάζω/δάμνημι is "overcome" (2.860, 5.106). | i "has overcome him". |
| 544 · l, i, n | HIGH | νεμεσσήθητε "be indignant" / "feel indignation": the table keeps νεμεσσάω "feel resentment" (2.222–223, 2.296, 4.413) and turns "be indignant" down; the draft's new-renderings row wrongly listed "resent" as the thing avoided. | l and i "feel resentment"; note says it is nearer to righteous indignation; row corrected. |
| 549–550 · n | MED | ἔσκε glossed "he used to be" while l and i say "he was"/"he had been" (the glossary already has "was, used to be"). | Note: "‘was, used to be’, here simply ‘he was’". |
| 550–551 · l, i | HIGH | l "many peoples": the table turns "peoples" down (λαοί "people" in l, "troops" in i). i "was always the best": the shipped ἀριστεύεσκε μάχεσθαι (6.460, 11.744, 16.291) is "used to be the best at fighting". | l "many people"; i "used to be the best among them at fighting". |
| 553–554 · i | LOW | "it was … that roused" adds a cleft the Greek does not have; the shipped 2.851 puts the heart first. | i "but the shaggy heart of Patroclus, son of Menoetius, roused the Achaeans". |
| 555 · n | MED | προσέφη said to be "without augment" (it is augmented: πρός + ἔφη). | Corrected. |
| 556 · l, i, n | MED | ἀμύνεσθαι "ward off" with the object "the enemy" supplied in i; the glossary already has the middle as "defend oneself", and 562 says the same wish with ἀλέξασθαι. | l and i "defend yourselves"; note; new-renderings row added. |
| 558 · n | MED | "the credit of being first is Patroclus’" garbled. | "that he was the first is Patroclus’ claim as the speaker". |
| 559–561 · l, i, n | MED | i "bring down" for δαμασαίμεθα ("overcome" in the table's i); the note stated "has no main clause and is a wish" as certain. | i "overcome one of his companions"; note "is read as a wish". |
| 562 · n | LOW | "elsewhere in the poem" for a repeated line. | "at 15.565". |
| 568 · i | LOW | εἴη "might be" given as "might go on". | "might be". |
| 506–507 · i | LOW | φοβέεσθαι "flee in panic": "panicked" is on the table's avoided list (12.470). | "eager to flee". |
| 509 · i | LOW | ὠρίνθη: the table's i is "was stirred" (16.280); this is in the same unit as the 509 row above. | "was stirred" (done in the same edit). |

## Findings considered and refused

- **ἀκωκή "tip" (477–478) against shipped 5.16 "point".** The table (11.253, 16.323) fixes ἀκωκή "tip" and keeps "point" for αἰχμή (505); 5.16 was shipped before that rule. Kept "tip". The caller may want to know that 5.16 now disagrees with the table.
- **φρένες "midriffs" in l against the table’s l "the midriff" (Odyssey 9.301).** Plural noun with plural verb ἔρχαται; "midriff" is the table's word. Kept. The note is honest about the organ.
- **πέπον (492).** l "good one", i "my good fellow", note "meaning not known": exactly the table. No change.
- **ἐελδέσθω (494).** Kept the traditional sense; note now says the construction is odd and why.
- **κατηφείη, βεβρυχώς, λάσιον κῆρ.** κατηφείη: note says the sense is not fixed, softened as above. βεβρυχώς: same Greek and English as shipped 13.393 (checked identical); note admits the uncertainty. λάσιον κῆρ: table 2.851; l keeps the Greek order as shipped 5.514 does ("but the Achaeans / roused …"), the note says what the subject is; i fixed.
- **503–504 ῥῖνας / μιν.** μιν goes with εἰπόντα as object of κάλυψεν, ῥῖνας is ῥίς plural "nostrils" (accusative of the part); the note is right. No change.
- **509 ὅ τ’ "because".** The neuter relative as conjunction ("that, because") is right; no change.
- **515 εἲς vs 538 εἰς.** Both are the second singular of εἰμί; the accents are as printed (checked by code point). No change beyond the note at 538.
- **551 λαοί.** Fixed to the table (see above).
- **556 ἀμύνεσθαι, 559 optatives.** Fixed / softened above; the wish reading kept (εἰ with the optative, no main clause).
- **ἁδινός / ἀδινός spelling.** Only the lemma differs by breathing; not a finding.
- **Unit 6 i "was full of eagerness".** Awkward but it does not supply an object; the table’s "eager" with a participle would need one. Kept.
- **Unit 20 i "had given him with an arrow" for βάλεν ἰῷ.** Sense-true and natural; shipped 12.388 says "struck … with an arrow". Not changed, since the note says it is the wound that wears him down.
- **δίκῃσι plural "justice".** Abstract plural, English singular; kept.
- **οὗ at 522.** The glossary already has the possessive ὅς "his own" (οὗ πατρός); the note’s label is right.
- **Repeated English.** Units 3, 4, 29, 34, 45 are identical in l and i to the shipped units (checked by script); 495/532 and 496/533 agree in l and i; ἀμύνων, ἔμπεδον, ἅλιος, αἰνὸν ἄχος, ὀνόμηνεν ἑταῖρον agree with the table.
- **Quotation marks.** “ on 492, 514, 538, 556 in l and i with `mark`; ” on 501, 526, 547, 561 in l and i; no speech runs in from iliad-103 (its last unit ends the fight) or out of this part.
- **Scansion.** The packet flags nothing; no note added.

## Open for pass 2

gloss.json is not yet written. Pass 2 must check every parse against the line, in particular εἲς / εἰς, ἐελδέσθω, ἀμύνεσθαι (now "defend oneself", the existing entry), οὗ, ἔσκε, λαοί (existing entry "people, host" fits), τέρσηνε (lemma τερσαίνω), ἐξέταμον (augmented) and the notes' new cross-references (1.457, 5.18, 13.809, 15.565, 15.676, 16.239).

---

# Pass 2 (gloss.json checked; units.json and new-renderings.md re-checked)

Method: every one of the 74 novel entries read against each line it occurs in; every one of the 13 `__broaden__` entries compared with the old entry (each must be the old entry whole plus " · also …"); every known form in the part (402) checked against its existing entry in the line where it stands (full entries printed for the doubtful ones); every cross-reference in the notes re-read in the edition text (16.466–469, 5.16–19, 4.498, 13.389–393, 13.618, 15.428, 5.602, 16.371, 16.437, 12.387–391, 12.334, 5.553, 5.696, 4.169, 4.455, 5.527, 13.747, 13.638, 14.276, 5.720, 15.307, 13.809, 15.676, 4.420, 5.859, 5.892–893, 4.117, 2.851, 2.87, 1.43, 1.457, 1.509, 15.565, 16.239, 11.215, 12.415, 5.643, 1.341) and the repeated English against the shipped units (iliad-005, -027, -081, -097). All cross-references are true. `t` untouched (compared with pass-1 file). Mechanical checks on gloss.json: 74 novel keys = `novel-forms.json`; every `__broaden__` value begins with the old entry; no ASCII apostrophe; no novel entry over 230 characters (longest 189); no line numbers; no "here"; no form of the part is missing from the known or the novel list.

Findings by severity (gloss and units rows below): HIGH 5, MED 19, LOW 20; 44 rows in all. Of the 27 `__broaden__` entries now in gloss.json, 13 are the glosser's (5 corrected) and 14 are new from this pass; the 74 novel entries keep their keys; 27 were rewritten (the rest were checked and left).

## Changes to gloss.json

| form · kind | sev | what was wrong | what done |
|---|---|---|---|
| γλαύκῳ · broaden (new) | HIGH | The old entry has only "of the person deprived: ’from Glaucus’"; 508 is the dative of the person affected ("grief came to Glaucus"). The glosser missed it. | Old entry + "of the person affected: ’to Glaucus’". |
| ὄτρυνον, ὄτρυνε · broaden (new) | HIGH | Old entries parse both as "impf. 3 pl." / "impf. 3 sg."; at 495 and 532 ὄτρυνον is the aorist imperative 2 sg., at 501 ὄτρυνε the present imperative 2 sg. (the unit notes already say so). | Both broadened with the imperative readings. |
| ἁδινὸν · novel | HIGH | "thick, close-packed, dense … ’thick (heart)’" contradicted the unit ("thronging heart"), the Odyssey table (19.516) and the Iliad glossary (ἁδινάων "thronging, close-packed"). | "thronging, close-packed, crowded (sense debated; thick) … ’thronging (heart)’". |
| προσαμῦναι, ἐπαμύνειν · novel | HIGH | "come to help" / "to defend" against the house "come to the defence of" (table; units fixed in pass 1). | Both "come to the defence of, ward off from … ’to come to the defence’". |
| νεμεσσήθητε · novel | HIGH | "feel righteous indignation … ’feel indignation’": the table turns "be indignant" down; the unit has "feel resentment"; the lemma should be the house νεμεσσάομαι. | "νεμεσσάομαι (νεμεσάω) — feel resentment, be indignant; aor. pass. imper. 2 pl. (dep.) … ’feel resentment’". |
| ἐξέταμον · broaden (new) | MED | Old entry "cut out" only; the tree simile is "cut down" (shipped 13.391, iliad-081). | Added "’cut down’, of trees". |
| ἀποφθινύθουσι · broaden (new) | MED | Old entry "perish, waste away … ’are dying off’" is the intransitive use; 540 takes θυμόν as object. | Added the transitive use. |
| λυκίην · broaden (new) | MED | Old entry covers goal of motion and "after κάτα"; 541 is a direct object. | Added "direct object". |
| αἴθωνα · broaden (new) | MED | Old entry "of a lion"; 488 is a bull. | Added "of a bull: ’fire-bright’". |
| νύκτ · broaden (new) | MED | Old entry "accusative of duration"; 567 is the object of τάνυσε. | Added "direct object". |
| εἰπόντα · broaden (new) | MED | Old entry "agreeing with τὸν"; 502 agrees with μιν. | Added. |
| πάντα · broaden (new) | MED | No reading agreeing with ἤματα. | Added "’all (days)’". |
| κέ · broaden (new) | MED | The old entry's "εἰ … κέ + short-vowel subj. in a condition" does not cover the long-vowel συλήσωσι at 499. | Added "εἴ κέ + long-vowel subj. in a condition". |
| ἔνθ · broaden (new) | MED | "there, then"; 481 ἔνθ’ ἄρα τε is relative "where". | Added. |
| ὅττί · broaden (new) | MED | "that" after a verb of rejoicing, and the accent before οἱ, are not covered (old: before κεν; after knowing; cause of anger). | Added. |
| θοός · broaden (new) | LOW | Old entry names the enclitic περ; 494 is before ἐσσι. | Added. |
| αὐτῷ · broaden | MED | The new reading read "’with him’ … ’his wits followed with it’": αὐτῷ is the spear and φρένες here are the midriff. | "’with it’ (φρένες αὐτῷ ἕποντο ’the midriffs followed with it’)". |
| καρτερὸν · broaden | MED | "severe, grievous": "grievous" is kept for ἀργαλέος (table). | "’strong, severe’ (τόδε καρτερὸν ἕλκος ’this severe wound’)". |
| εἰς · broaden | LOW | Example "you are forgetful" is not the sense ("you have forgotten"); "Ionic". | "epic εἶς … ’you have forgotten’, with a perfect participle". |
| εἲς · novel | LOW | "Ionic". The parse "you are" is right in both lines. | "epic εἶς". |
| παιδὶ · broaden | LOW | "of concern: ’for his son’" for περὶ παιδί, where the unit says "around his dear son" (and the old περί entry has "+ dat. of place: around"). | "after περί, of place or concern: ’around’". |
| προτὶ · broaden | LOW | "’along, with it’" with example "followed along". | "’along with it’ … ’followed along with it’". |
| δάμασ, δαμασαίμεθα · novel | MED | "overpower, subdue": the table's English for δαμάζω is "overcome" (and the units say so). | "overcome, subdue". |
| ἔρχαται · novel | MED | "enclose … ’are enclosed’" for the unit's "are shut about"; the Attic equivalent was masculine, but the subject φρένες is feminine. | "shut in, enclose … Attic εἰργμέναι εἰσί, fem.: ’are shut in’". |
| ἕρμα · novel | LOW | "bulwark" is on the avoided list of new-renderings.md. | "prop, support". |
| ὀλοὸς · novel | LOW | "deadly, destructive, baneful": order reversed against the unit. | "baneful, deadly, destructive". |
| ὠρίνθη · novel | LOW | "’was stirred up’" for the unit's "was stirred" (table, 16.280). | "’was stirred’". |
| κοίμησον · novel | LOW | "’put to rest’" for "put to sleep". | "’put to sleep!’". |
| ἄσχετον · novel | MED | "neut. acc. sg., agreeing with πένθος": πένθος is the subject of λάβε, so nominative. | "neut. nom. sg.". |
| ἐελδέσθω · novel | MED | "’let it be longed for’" stated the odd construction as plain meaning; "ἐ- doubled" is wrong (prothetic ἐ-). | "’let it be longed for’, with the thing wished as subject (usually the one who longs is the subject)"; "prothetic ἐ-" (as in the Iliad glossary's ἐέλδεται). |
| ἀρείους · novel | MED | "masc. nom. pl. … + gen. of comparison" (copied from the Odyssey entry): there is no genitive at 556, and the case of ἀρείους after ἦτε is not settled (the pass-1 note said accusative). | "masc. pl. (nom. or acc. form), as predicate with an understood ἦτε: ’better’"; note at 556 made case-free (see units rows). |
| ἀλλοδαπός · novel | LOW | "used as a noun" for a predicate adjective with ἐών. | "predicate with ἐών: ’a foreigner’". |
| ἀμφιμάχεσθαι · novel | LOW | "epic ἀμφιμαχέσθαι, Attic ἀμφιμάχεσθαι": the printed form is the same as Attic; the epic form is the present stem ἀμφιμαχέομαι. | "ἀμφιμάχομαι (epic ἀμφιμαχέομαι) … (Attic ἀμφιμάχεσθαι)". |
| κατηφείη · novel | LOW | Attic equivalent printed κατηφεία (the Attic noun is κατήφεια); "Ionic". | "epic -είη (= Attic κατήφεια)"; meaning "shame, dejection (from κατηφής ’downcast’; exact sense uncertain)". |
| μενοιτιάδεω · novel | LOW | "epic -άδεω (= Attic -ιάδου)": the two endings did not correspond. | "epic -ιάδεω (= Attic -ιάδου)". |
| πάρστητε · novel | LOW | Lemma "πάρ-ἵστημι". | "παρίστημι … preverb cut short". |
| νέκυι · novel | LOW | "(= Attic νεκρῷ)" suggests the same form; νέκυς is a different noun-stem. | "the poetic word; prose νεκρός". |
| ἀεικίσσωσι, ἀεικισσαίμεθ · novel | LOW | "treat shamefully, maltreat" for the units' "abuse" (and "treat unseemly" in l). | "treat shamefully, abuse (from ἀεικής ’unseemly’)"; Attic αἰκίσωσι, αἰκισαίμεθα are real forms (αἰκίζω), not reconstructions. |
| τέρσηνε, τερσῆναι · novel | MED | The glosser's own doubt: "Attic equivalents" ἐξήρανε, ξηρανθῆναι belong to ξηραίνω, which is the real Attic verb; they are not reconstructions, but they are not the same verb. τερσῆναι was glossed "to dry up" as if transitive. | "(the Attic verb is ξηραίνω, aor. ἐξήρανε)" and "(… ξηραίνομαι, aor. ξηρανθῆναι)" stated as verb substitution; τερσῆναι "intransitive … ’to become dry’". |
| ἐπίεζε · novel | LOW | "(ἐ-πίεζε; Attic ἐπίεζε(ν))": the Attic form is the same, so no equivalence is given. | "augmented". |

## Changes to units.json

| unit · field | sev | what was wrong | what done |
|---|---|---|---|
| 556 · n | MED | "ἀρείους, the accusative plural … agreeing with the ‘you’" stated a case the Greek does not decide (after ἦτε a nominative would be expected). | "the plural of ἀρείων ‘better, braver’, a predicate that goes with an understood ἦτε". |
| 555 · n | LOW | μεμαῶτε "from μέμονα": the glossary lemma is μέμαα. | "from μέμαα". |
| 548 · n | LOW | "here simply ‘he was’" while `i` has "had been". | Note says why ("because he is dead"). |
| 477, 479 · n | LOW | The notes did not say that 478–479 down to αὐτόν, and the half-line ὃ δ’ ὕστερος ὄρνυτο χαλκῷ, are 5.16–17 and the end of 5.17 (the English follows them). | One sentence added to each note. |

## new-renderings.md

Checked row by row against `l` and `i` of the units: all 27 rows agree. One row clarified (517 reads "a wound I have, this strong one" in `l`, for the word order).

## Considered and refused

- **ἀκωκή "tip" against shipped 5.16 "point"**: the Iliad table fixes "tip" (conventions, 11.253 and 16.323, with the departure from 5.16 recorded). Kept; pass 1 was right.
- **εἴ (559, εἴ μιν ἀεικισσαίμεθ’) as "if only"**: left as "if"; the note says the clause is read as a wish and the English says "if only". Not added to the entry because the Greek has no main clause either way and the reading is the note’s, not the word’s.
- **δαμάζω "kill"**: the unit 543 note says "which means kill"; the entry stays "overcome, subdue" (the table’s English).
- **ἀνέρι (515), ἀκούειν, ἀΐοντι, φθογγῆς, κηδομένῳ**: parses checked (dative agreeing with ἀνέρι; genitive of the sound heard); no change.
- **εἲς / εἰς "you are"**: confirmed in 515 and 538 (accent as printed, checked by code point in pass 1); both second singular of εἰμί; the `__broaden__` entry for εἰς and the novel entry for εἲς agree.
- **ἔσκε, οὗ, ᾗσιν, ᾧ, ἀμύνεσθαι, λαοί, ἅπαντα**: existing entries cover the uses (ἔσκε "was, used to be"; οὗ possessive "his own"; ᾗσιν and ᾧ possessive; ἀμύνεσθαι "defend oneself"; λαός "people, host"; ἅπαντα "all (the army)"). No change.
- **ἔλδεται-type entries**: ἐελδέσθω keeps the traditional sense; the Greek construction is odd and the entry says so.
- **Cross-references named by the caller** (1.457, 5.18, 13.809, 15.565, 15.676, 16.239, 5.16–17 added): all true as read in the edition; 15.565 and 1.457 also agree in English with iliad-097 and iliad-005.
- **Notes**: no other false label found; "ἅμα … τε καὶ", "ὅ τ’ because", "οἱ in him" and the 12.388/12.334 comparisons are true of the lines.
