# Review of iliad-128 (20.103–198) — pass 1 (units)

Pass 1 read units.json against packet.md, conventions.md (Iliad and Odyssey house-renderings tables), the
published Iliad and Odyssey parts in the repository root, and drafts/iliad-127/units.json. gloss.json was being
written concurrently and is not reviewed here (pass 2). `t` untouched (the edit script asserts every `t` is
unchanged); `l` keeps the line division of `t` in every unit; no `\n` in `i`; every note within 25–110 words.
Edits made by script (scratchpad `edit128.py`), plus three row changes in new-renderings.md (below).

Checked and found right: paragraph marks (`p` on 103, 110, 132, 144, 153, 156); `ln` of every unit; the four
speeches (Apollo 104–109, Hera 115–131, Poseidon 133–143, Achilles 178–198) open with “ and `mark` and close
with ” in both layers; iliad-127 closes Aeneas’s speech at 20.102, and source line 199 is Aeneas’s reply
formula, so nothing runs across either boundary. Repeated lines 20.110, 20.111, 20.159, 20.176, 20.196–198 carry
the published English (iliad-093, -026, -037, -016, -108); 20.184–185 match iliad-037 (6.194–195); 20.193 matches
iliad-040/-107 (ἐλεύθερον ἦμαρ ἀπούρας); 20.113 matches 4.251 (“up through the crowd of men”); 20.152 ἤϊε Φοῖβε
matches iliad-094 (15.365).

## Changes (unit by first line · field · severity · what was wrong · what was done)

| line | field | sev | what was wrong | done |
|---|---|---|---|---|
| 108–109 | l, i, n | medium | μηδέ σε … ἀποτρεπέτω rendered “let one / let no one turn you”; the unexpressed subject is the last-named third person, κεῖνος (Achilles), whose taunts Apollo means; ἀρειῇ: table 17.431 and published iliad-112 have “threats” | l “let him turn away, and with threats”, i “do not let him turn you aside … with pitiful words and threats”; note names Achilles as the understood subject |
| 131 | l, i, n | medium | ἐναργεῖς “in clear view / in plain view” as a new rendering; the binding table (Odyssey 7.201, shipped odyssey-031, -078) has “manifest” / “in manifest form” and turns down “in plain view” | l “and hard are gods to appear, manifest.”, i “for gods are hard when they appear in manifest form.”; note; row removed from new-renderings.md |
| 158–160 | l, i, n | medium | ἔξοχ’ ἄριστοι “above all others the best”; the Odyssey ships the same words as “far the best” (4.629, odyssey-019), and new-renderings.md claimed no Odyssey departure | “far the best” in l and i; note; new-renderings row changed to follow the Odyssey |
| 161–162 | l, n | medium | κόρυθι βριαρῇ l “heavy helmet”; table (11.375, 16.413) and published iliad-103/-105 have l “weighty”, i “heavy” | l “weighty helmet” (i keeps “heavy”, as the table); note gives “weighty” and βρίθω |
| 170–171 | l, i, n | medium | μαστίεται “lashes”: the table keeps “lash” for ἱμάσσω and “whip” for μαστίζω; and the note called the form a present of μαστίζω, but μαστίεται is from the epic μαστίω | “whips” in l and i; note: present middle of μαστίω, epic form of μαστίζω ‘whip’ |
| 178–179 | i | medium | ὁμίλου “crowd”; table 3.340 fixes ὅμιλος “throng” and turns down “the crowd” (l already “throng”) | i “so far from the throng” |
| 179–181 | l, i, n | medium | τιμῆς τῆς Πριάμου rendered “in the honour of Priam”: the genitive is what ἀνάξειν is lord of, with Τρώεσσιν the dative “among”; the note gave only the dative construction | l “hoping among the horse-taming Trojans to be lord / of the honour of Priam?”; i “in the hope of being lord, among the Trojans, tamers of horses, of the honour that Priam holds?”; note explains both cases (ἀνάσσω “be lord”, table 1.180) |
| 183 | l, i, n | medium | ἀεσίφρων “unsteady-minded / unsteady of mind” as a new rendering; the binding Odyssey table (21.302) and shipped odyssey-104 have “senseless” (+ note: meaning not known for certain) | “and not senseless” in l and i; note follows the table’s note; row removed from new-renderings.md |
| 104–105 | n | low | note glossed αἰειγενέτης “ever-born”, which the table turns down (“forever-born”), against its own l | “‘forever-born’” |
| 105–106 | n | low | “χερείονος is the comparative of an adjective meaning ‘worse’”: χερείων is itself the comparative; table 17.539 keeps “worse” for κακίων | “the genitive of χερείων ‘lesser, inferior’, itself a comparative form” |
| 112–113 | l, n | low | Ἀγχίσαο πάϊς “Anchises’ child”; table pattern for πάϊς with a father’s name is “son” (6.154 Ἱππολόχοιο πάϊς “Hippolochus’ son”; 2.819 πάϊς Ἀγχίσαο “son of Anchises”); i already “son” | l and note “Anchises’ son” |
| 115–116 | n | low | “Ποσείδαον is the epic form of the name”: it is the vocative of the (epic) Ποσειδάων | “the vocative of Ποσειδάων” |
| 123–124 | l | low | τὸ πάρος περ “who before, as ever,” does not render περ and reads oddly | “who even before now” |
| 125–126 | i | low | i began lower-case after a full stop in the previous unit | “And we have all come down …” |
| 127–128 | i | low | same picture as Odyssey 7.197–198 (odyssey-031: “spun for him with the thread when he was born, when his mother bore him”); i had “with its thread at his birth” | i reuses the Odyssey wording (“lot” kept, as the table’s αἶσα `i`) |
| 134–135 | l, i | low | ἐπεὶ ἦ πολὺ φέρτεροί εἰμεν is a shipped Odyssey half-line (9.276: “since indeed much stronger we are” / “since we are, in truth, far stronger”); draft varied it and dropped ἦ in i | Odyssey wording in both layers |
| 136–137 | l, i, n | low | πόλεμος δ’ ἄνδρεσσι μελήσει is the published 6.492 (iliad-040: “war will be the care of men” / “the concern of … men”); draft had “a care to men” / “the men’s concern” | l “the care of men”, i “the concern of men”; note cites 6.492 |
| 141–143 | i, n | low | δαμέντας i “overpowered”; table δάμνημι l “subdued”, i “overcome” (11.821); l already “subdued” | i “overcome”; note “‘subdued, overcome’” |
| 151–152 | n | low | note said ἤϊε “is left out of the English”, contradicting its own l (“Ēïe Phoebus”) | “the word-for-word line keeps it as Ēïe, the plain English leaves it out” |
| 164–165 | i | low | i began lower-case after a full stop | “And from the other side …” |
| 165–166 | n | low | “τε καί adds that men too are eager” contradicts l “even men”; τε is the epic generalising τε; ἀποκτάμεναι unlabelled as aorist | note: epic τε of a general statement, καί ‘even’ with ἄνδρες; “epic aorist infinitive” |
| 168–169 | n | low | note under 25 words | one clause added (the froth of the wounded lion) |
| 172–173 | n | low | φθίεται looks like a present indicative; it is the short-vowel aorist subjunctive parallel to πέφνῃ, and the note did not say so | sentence added (= φθίηται) |
| 181–182 | i, n | low | i “even if”: there is no καί, and l has “if”; note “if you were to kill” describes an optative, but the verb is κεν + subjunctive | i “But if you kill me …”; note “‘if you kill and strip’, κεν with the subjunctive” |
| 188–190 | l, i, n | low | κατ’ Ἰδαίων ὀρέων i “the mountains of Ida”: published iliad-065/-092/-093/-106 and table 11.196 have “the Idaean mountains” in both layers (“down the slopes of Ida” turned down); ταχέεσσι πόδεσσι “swift feet” beside καρπαλίμως “swiftly” (the table keeps “swiftly” for καρπαλίμως and ὠκύς; the Odyssey ships ταχέεσσι πόδεσσιν “quick feet”, 13.261) | i “from the Idaean mountains”; “quick feet” in l, i, note |
| 195–196 | n | low | note called ἐρύεσθαι “the same verb as ἐρρύσατο” while the previous note gives ἐρρύσατο under ῥύομαι | “ἐρύομαι ‘rescue, protect’, another form of ῥύομαι, the verb of ἐρρύσατο” |

Counts: high 0, medium 8, low 18 (26 changes; several touch more than one field). new-renderings.md: the
ἐναργεῖς and ἀεσίφρων rows removed (they follow existing table rows), the ἔξοχ’ ἄριστοι row changed to the
Odyssey’s “far the best”, and one sentence added to the closing paragraph saying so.

## Hand scan of line 112 (flagged AMBIGUOUS / UNRESOLVED, “metrical lengthening: Ἀγχίσαο, longum of foot 3”)

οὐ-δέ-λα | θαγ-χῑ | σᾱ-ο-πα | ϊς-λευ | κώ-λε-νον | Ἥ-ρην: – ⏑ ⏑ | – – | – ⏑ ⏑ | – – | – ⏑ ⏑ | – –. The ι of Ἀγχίσης
is long by nature, and so is the α of the first-declension genitive in -ᾱο (as in Ἀτρεΐδαο); ϊς is long by
position before λ. The line scans regularly with no licence; the scanner’s flag comes from treating -αο as
short. No sentence added to the note.

## The drafter’s flagged guesses

- κάρκαιρε (157): kept. A rare verb; ancient explanations run to “shook” or “resounded”. The note says the meaning is not known and that “shook” is a guess. Right.
- ἀεσίφρων (183): changed (above): the table already fixes it.
- ἤϊε (152): kept; matches table 15.365 and iliad-094. Only the note’s wording fixed.
- μεθορμηθείς (192): kept. μεθορμάομαι is “start after, pursue” (μετά “after”); “set out in pursuit” renders it
  without supplying an object, and the note says the Greek does not say after whom. Right.
- ἐρύεσθαι (195): kept as “rescue”. The table’s 9.248 row has ἐρύεσθαι “draw (out)” in `l`, but that is
  tied to ὑπό “from under”, which is absent here; with no ὑπό and directly after ἐρρύσατο “rescued” the
  sense is protect/rescue, and keeping one English verb across 194–195 lets the reader hear Achilles’ echo. The
  passive turn in `i` is declared in the note. Only the note’s lemma wording fixed.
- line 112: regular (above).

## Findings considered and refused

- 155 κέλευε “was bidding / gave his bidding”: the table is split (some rows keep “bid” for ἄνωγα and give
  κελεύω “order”, iliad-127 review), but 5.528 πολλὰ κελεύων fixes κελεύω “bid, order” with l “bidding”, and
  κέλευε here has no object, so “ordering” would be stranger than the Greek. Kept.
- 167–168 ἐάλη l “he is hemmed in”, i “he crouches”: looks like an l/i mismatch, but it is the table’s own
  split (13.408: l “was hemmed in”, i “crouched”). Kept.
- 130 note “ἐναντίβιον … literally ‘against his strength’”: follows the table (8.255). Kept.
- 144 note “literally ‘dark-maned’” for κυανοχαίτης: a gloss of χαίτη in the note, not a rendering; the
  layers keep the table’s “dark-haired”. Kept.
- 134–135 θεοὺς … ἡμέας τοὺς ἄλλους “the rest of us gods”: the Greek is ambiguous (us, the others / us
  against the others); the rendering is a fair one and the note says Poseidon counts himself among them. Kept.
- 131 l: the bare infinitive (“hard are gods to appear”) could be read as “find it hard to appear”; the note
  says the infinitive gives the respect (“when they appear”). Kept with the comma after “appear”.
- 158 note “μεμαῶτε … (perfect of μέμαα)”: μέμαα is itself the perfect; the parenthesis says the form belongs
  to it, which is true. Kept.
- 103 note “προσέειπεν … with the epic uncontracted -εε-”: ἔειπον beside εἶπον is usually described so. Kept.
- 189 l puts “I drove you” (σεῦα, line 189) in the first `l` line: English order; the line count is kept and
  the rest of the line division holds. Kept.
- 104 l “to the gods, the forever-born” vs table 14.446 “the gods who are forever-born”: published iliad-019
  has the same dative as “to the gods, forever-born”, and the table’s 2.400 row uses the appositive form.
  Kept.
- 117–118 ἀνῆκε “has urged on”: table 5.405 “has urged on” exactly. Kept.

# Pass 2 (units re-read; gloss.json against the lines)

Pass 2 re-read every unit of units.json against the Greek, with fresh eyes on the 26 pass-1 changes, and checked
every parse in gloss.json (77 novel forms, 14 `__broaden__` entries) against the line(s) where the form occurs,
plus the entry format (shape, under 230 characters, ’ only, no line numbers, no “here”, Attic equivalents,
article-forms as pronouns, homographs joined by “ · ”). Each `__broaden__` entry was checked by script to contain
the known-forms entry whole. Edits made by script (scratchpad `pass2_128.py`). `t` is untouched (asserted), every
note is still 25–110 words, and every gloss key matches novel-forms.json.

The pass-1 changes all stand: 108 (κεῖνος as understood subject), 131 and 183 (table “manifest”, “senseless”),
158 (“far the best”), 161 (“weighty”), 170 (μαστίω “whips”), 178 (“throng”), 179–181 (τιμῆς as the genitive
after ἀνάξειν), 188 (“the Idaean mountains”, “quick feet”), and the low-severity note fixes.

## Changes — units.json

| line | field | sev | what was wrong | done |
|---|---|---|---|---|
| 123–124 | n | low | pass 1 changed l to “who even before now”, but the note still quoted “who as before ward off for the Trojans”, so the note no longer matched its own l | note quotes “who even before now ward off … for the Trojans” |
| 174–175 | n | low | “ὄτρυνε the unaugmented aorist”: with ῡ in both stems the form could be imperfect or aorist, and the shipped glossary entry for ὄτρυνε gives imperfect, so the note contradicted it | “the unaugmented imperfect of ὀτρύνω ‘urge on’ (an aorist would look the same)” |
| 120–121 | n | low | παρσταίη not explained: the apocope παρ- for παρα- is the thing that makes the form hard to recognise | “with παρ- cut from παρα-; Attic παρασταίη” added |

## Changes — gloss.json

| form | sev | what was wrong | done |
|---|---|---|---|
| φθίεται | medium | “pres. mid. 3 sg. … short-vowel subj.”: contradicted itself. The line scans with φθῐ short (ἀνδρῶν \| ἢ αὐ \| τὸς φθῐ ε \| ται πρώ \| τῳ ἐ νο \| μί λῳ), and the present φθίω has ῑ, so the form is the root-aorist subjunctive (ἐφθίμην), as the unit’s note says | “root aor. subj. 3 sg. mid., short-vowel (= φθίηται; aor. ἐφθίμην), not the present” |
| παρσταίη | medium | “(= Attic παραστάη/παρασταίη)”: παραστάη is not a form | “epic παρ- for παρα- (= Attic παρασταίη)” |
| τιμῆς (`__broaden__`) | medium | the new reading “with ἀνάξειν: ’in the royal honour’ (’in the office of Priam’)” contradicts units 179–181, where τιμῆς is the genitive of what one is lord of (pass 1’s fix) | the new reading is now “gen. of what one is lord of, after ἀνάσσω: ’of the honour’”; the old entry is kept whole |
| ἐρύεσθαι (`__broaden__`) | medium | not needed: the old entry (ἐρύομαι “rescue, protect … ’to rescue’”) already covers 20.195. The added reading named a third lemma (ῥύομαι) for the same form and gave a passive “to be rescued”, which is the `i`’s turn of phrase, not the force of the middle | removed; the old entry stands |
| σεύαιτο (`__broaden__`, new) | medium | the old entry (“mid. rush, dash … ’whenever he dashed’”) does not cover 20.148 ὁππότε μιν σεύαιτο, where the middle is transitive (“whenever it drove him”) | broadened: old entry + “ · also mid. with acc., ’chase, drive’” |
| ἀνάξειν (`__broaden__`) | low | the new reading (“after ἐλπόμενον”) gave the context but not the construction, + gen. of the thing ruled, which is the hard part | new reading: “+ gen. of what one is lord of, with dat. of the people” |
| ἑὲ | low | “here reflexive”: “here” is not allowed | “often reflexive, esp. with αὐτόν”, Attic ἑαυτόν |
| ὑψηλόν | low | “(neut. here, agreeing with τεῖχος)”: “here”, and tied to one line | “masc. acc. sg. or neut. nom./acc. sg.” |
| κτείνῃς | low | “pres. subj.” only: the aorist ἔκτεινα has the same subjunctive, and the aorist is the likelier reading of αἴ κεν ἐμὲ κτείνῃς | “pres. or aor. subj. 2 sg.” |
| μαστίεται | low | no Attic equivalent; the gloss “lashes” clashed with the table, which keeps “lash” for ἱμάσσω | “μαστίω — whip, lash (epic by-form of μαστίζω); … (= Attic μαστίζεται): ’whips (himself)’” |
| σκοπιήν | low | Ionic -ήν named with no Attic form | “(= Attic σκοπιάν)” |
| ὑπέκφυγες | low | unaugmented, and not said | “unaugmented (= ὑπεξέφυγες)” |
| ἀμύνουσιν, φιλέουσιν | low | real homographs (also pres. part. dat. pl.) given only the finite reading | participle reading added after “ · ” |
| κῆτος, γιγνομένῳ, χερείονος, δυσηλεγέος, ἐλπόμενον, ἀμφίχυτον | low | the parse was narrowed to the one agreement in this part (e.g. κῆτος “acc.” only; χερείονος “masc./fem.”, “agreeing with θεοῦ”), which is not general to the form | the full range of the form given (nom./acc.; any gender; masc./neut.) |

Counts (pass 2): high 0, medium 5, low 18, 23 changes in all (units.json: 3 low; gloss.json: 5 medium, 15 low,
counting each form in the grouped rows separately).

## Findings considered and refused (pass 2)

- Pass 1’s refusal of “μεμαῶτε … (perfect of μέμαα)” (158, also 165): re-examined. The phrase gives the lemma, as the glossary does (“μέμαα — … perf.”). Kept.
- 103 “προσέειπεν is the aorist of προσεῖπον”: προσεῖπον is the glossary lemma for this aorist-only verb; the wording follows it. Kept.
- 157 l “and shook the earth under the feet”: in English it could be read as transitive, but `l` keeps the Greek order (verb before subject) as elsewhere in the part (103, 132), and `i` and the note settle it. Kept.
- 195 ἐρύεσθαι: some take it as a future. The present-middle reading the note gives (with σε understood, “rescue”) fits ὀΐομαι with νῦν and is the glossary’s existing reading. Kept.
- Known entries pinned to another line (λευκώλενον “agreeing with Ἀνδρομάχην”, θοῦριν “agreeing with ἀλκήν”, θεοῦ “possessive with …”): the meaning and parse still cover their use here (Ἥρην, ἀσπίδα, ἐκ θεοῦ); the glossary often pins an entry to its first agreement this way (αἴθοπι, βριαρῇ). Not broadened.
- Gloss entries such as “agreeing with ἐπέεσσιν” (λευγαλέοις), “after ἐκ” (ὀμφῆς), “depending on ὀφρύσι” (καλλικολώνης): the glossary already does this (αἴθοπι, βριαρῇ, φυταλιῆς), so not treated as pinning to a line. Kept.
- σίντης “adj.”: LSJ gives a noun (“ravager”) that is used as an adjective with λέων; the entry’s “adj., … agreeing with λέων” is true of the use, and the note and l say “ravager”. Kept.
- ἀεσίφρων gloss “unsteady of mind, witless” beside the table’s “senseless”: a gloss gives meanings, not the house rendering, and it marks the doubt. Kept.
- ἔολπα under ἔλπω (gloss) but “from ἔλπομαι” (note 186): both are LSJ-sanctioned (the perfect goes with either), and neither is false. Kept.
- πείσεται `__broaden__` (πάσχω beside πείθω): a real homograph, the old entry kept whole, joined by “ · ”. Right. The other broadens (κέν, ἔλθῃ, φέρε, χαλέπαινε, ἐθέλοιμι, ῥέξειν, ἄρρηκτον, ἔγνω, παρ, ἐκ) were checked against their lines and are right.
