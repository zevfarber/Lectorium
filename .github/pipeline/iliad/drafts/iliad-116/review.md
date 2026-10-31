# iliad-116 review (Iliad 18.1–96) — two passes

Pass 1: units only. Pass 2: units re-read after the pass-1 edits, plus `gloss.json` (every parse checked against the line, every known form checked against its existing entry). `t` was not touched: the sentence `t` values are byte-identical before and after (checked), and the joined `t` still equals the archive's 18.1–96. Edits to `units.json` and `gloss.json` were made by script. The scanner was run on all 96 lines (see the last section).

Counts by severity (a finding that touches several places is one finding): **high 0 · medium 13 · low 29 · total 42** (units 25: 9 medium, 16 low; gloss 17: 4 medium, 13 low).
Severity key: high = wrong Greek→English or a note that misleads the reader about the text; medium = false cross-reference or false claim, house-table violation, wrong lemma/reading in the glossary; low = consistency, wording, hedging, overstatement.

## A. Changes to `units.json`

| # | Line · unit | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|---|
| 1 | 18.5 | n | medium | “as at 5.298” — 5.298 is δείσας μή πώς οἱ ἐρυσαίατο νεκρὸν Ἀχαιοί; the formula stands at 11.403 and 17.90 (iliad-067). | “as at 11.403 and 17.90”. |
| 2 | 18.8 | i, n | low | `l` “in my heart”, `i` “for my heart”, note “dative of interest, ‘for my heart’”: three layers, two senses. 18.53 ἐμῷ ἔνι κήδεα θυμῷ shows the place sense. | `i` “in my heart”; note: θυμῷ is a dative of place, μοι the dative of interest. |
| 3 | 18.3–4 | l, i, n | medium | τετελεσμένα “accomplished”: the table's 1.388 row (ὃ δὴ τετελεσμένος ἐστί) gives “fulfilled” and lists “has been accomplished” among the avoided renderings; the 7.465 row says τελέω keeps “fulfil” for a plan, promise or wish. Achilles' wish is exactly that, and the note itself says the line picks up τελέσωσι (“fulfil”, 18.8) — a link the English hid. | “fulfilled” in `l`, `i` and note. |
| 4 | 18.74 | l, i, n | medium | τετέλεσται “accomplished”, same reason as 3. | “fulfilled” (`l`, `i`); note “τελέω ‘fulfil’”. |
| 5 | 18.79 | l, i, n | medium | ἐξετέλεσσεν “brought to completion” / “brought to pass”: the same event and the same verb family as 18.74, which Achilles is answering; `l` and `i` also differed. | “has fulfilled” in `l` and `i`; note “‘fulfilled’”. |
| 6 | 18.13–14 | l, i, n | medium | ἐκέλευον given “bade”: the table reserves “bid/bade” for ἄνωγα (11.641 “bade” avoided for κελεύω; 21.175 “ordered / gave his orders”), and 18.90 ἄνωγε “bid” sits seven lines away. “And yet” translates no word: ἦ τε is “truly” (3.366 ἦ τ’ ἐφάμην “Truly I thought”). | `l` “truly I was ordering him”; `i` “I did tell him” (11.641 has “told them to”); note rewritten (“ἦ τε is ‘truly’ … ‘I was ordering’ (‘bid’ is kept for ἄνωγα)”). |
| 7 | 18.18 | l | low | δαΐφρονος `l` “wise-hearted”; the table's δαΐφρων row is `l` “wise-minded”, `i` “wise-hearted” (4.252, 5.813, 11.839). | `l` “wise-minded”. |
| 8 | 18.28–30 | l | low | Same, δαΐφρονα “wise-hearted”. | `l` “wise-minded”. |
| 9 | 18.67 | l | low | ἐπισχερώ `l` “one after another”: the table (11.668) is `l` “in a row”, `i` “one after another”; new-renderings.md says it “takes the i wording” but gives no reason to depart. | `l` “in a row”. |
| 10 | 18.20–21 | l, i | low | ἀτὰρ τά γε τεύχε’ … rendered “and”; the note says ‘but’. | “but” in `l` and `i`. |
| 11 | 18.9–11 | n | low | “Achilles is quoting her to her” — Thetis is not there; he is alone. | “recalling her words”. |
| 12 | 18.35 | n | medium | “‘him’ is understood, as in the line at 1.357” — 1.357 is τοῦ δ’ ἔκλυε πότνια μήτηρ: the object is expressed. | Note says ‘him’ is understood here and that 1.357 has τοῦ expressed. |
| 13 | 18.94 | n | medium | “the feminine of the phrase used of Achilles at 1.357” — 1.357 has δάκρυ χέων, no κατά; κατὰ δάκρυ χέουσα is 1.413, of Thetis herself. | “the phrase used of Thetis herself at 1.413”. |
| 14 | 18.26 | n | low | “the dead man at 16.775”: μέγας μεγαλωστί is 16.776. | 16.776. |
| 15 | 18.73 | n | medium | “where she first came to him weeping in the camp”: at 1.348–362 Achilles weeps by the sea and Thetis rises out of it. | “where she first came up out of the sea to him as he sat weeping”. |
| 16 | 18.74 | n | low | “The two lines match 1.363” — only one line (ἐξαύδα, μὴ κεῦθε) is in the unit. | “The words match 1.363”. |
| 17 | 18.55–56 | n | low | ἀμύμων is on the convention's list of words whose sense is not known and must be so said (the table's 11.833 row does so); the note said only ‘blameless’. “When I had borne” against `l` “when I bore”. | Added “the house rendering of a word whose real sense is not known”; “when I bore”. |
| 18 | 18.52–53 | n | low | “ἔνι is ἔνεστι” asserted as fact; ἐμῷ ἔνι … θυμῷ can equally be the preposition (the glossary's own ἔνι entry has both). | Note gives ‘in my heart’ and names both readings. |
| 19 | 18.90 | n | low | “ἐπεὶ οὐδ’ ἐμέ is ‘since not even me’” disagrees with `l` (“neither … nor”). | “ἐπεὶ οὐδ’ … οὐδ’ is ‘since neither … nor’”. |
| 20 | 18.92 | i | low | “struck down” adds ‘down’ to τυπείς. | “struck”. |
| 21 | 18.93 | n | medium | “ἕλωρα … said of Patroclus' body as the thing Hector has made his own” — the Greek does not say what is paid for; this is an unsupported claim about the text. | Note: ‘prey, booty’; the Greek does not say whether the killing, the body or the armour is meant; the English keeps to “the prey he made of Patroclus”. |
| 22 | 18.82–83 | l, i | low | “his armour” — τεύχεα has no possessive, and the armour is Achilles', not Patroclus' (the note says so); “his” reads as Patroclus'. | “the armour” in both. |
| 23 | 18.45–46 | n | low | “The colon marks the pause”: the Greek mark is the high stop (·) and `l` ends in a semicolon. | “The high stop (·)”. |
| 24 | 18.47–49 | i | low | “all the other Nereids”: ἄλλαι θ’ αἳ has no ‘all’ (contrast πᾶσαι ὅσαι in 38). | “the other Nereids”. |
| 25 | 18.95 | l | low | δή dropped in `l` without cause. | “Swift-doomed indeed”. |

## B. Changes to `gloss.json`

| # | Form | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 26 | εἴρυντο (broaden, new) | medium | Existing entry is ἐρύομαι “guard”; the line has ἐρύω “draw up” (the unit's own note says so). | Broadened with ἐρύω, plpf. pass. 3 pl., ‘had been drawn up’ (of ships). |
| 27 | κλυμένη (broaden, new) | medium | Existing entry: Clymene, Helen's handmaid. Here a Nereid. | Broadened. |
| 28 | ὅττί (broaden, new) | medium | Existing entry covers ὅστις acc. and ὅτι ‘that’; 18.64 is the interrogative ‘what’ agreeing with πένθος. | Broadened. |
| 29 | ἀεκήλια | medium | “unseemly, unwelcome, shameful … cf. ἀεικής”: contradicts the unit (‘unwelcome’, “unseemly” reserved for ἀεικής, compare ἀέκων). | “unwelcome (exact sense uncertain; cf. ἀέκων ‘unwilling’)”. |
| 30 | τετέλεσται, τετελεσμένα, τελέσωσι, ἃ (broaden example) | low | English glosses ‘accomplished/bring about’ no longer matched the units after 3–4. | Lemma order “fulfil, accomplish”; examples ‘fulfilled’, ‘lest they fulfil’. |
| 31 | ἁλίη, νησαίη, ἀκταίη, κυμοδόκη, κυμοθόη, καλλιάνασσα, καλλιάνειρα, φέρουσά, ἴαιρα, μαῖρα | low | Names given in transliterated forms (Halie, Nesaie, Aktaie, Kymodoke … Pherousa, Iaira, Maira) against the units' Latin forms, which new-renderings.md explicitly chose. | Halia, Nesaea, Actaea, Cymodoce, Cymothoe, Callianassa, Callianeira, Pherusa, Iaera, Maera. |
| 32 | μαῖρα, καλλιάνειρα, γλαύκη, δωρὶς | low | Meanings stated where the note claims none (‘Sparkler’, ‘Fair Lady’), or differing from the note (Glauce ‘Gleaming’ vs ‘grey-green’; Doris ‘Giver’ vs “may be ‘gift’”). | Meanings dropped / aligned with the notes. |
| 33 | νεκταρέῳ | low | “fragrant as nectar” settles what the note says is not known. | “nectar-sweet (exact sense uncertain)”. |
| 34 | δειλή | low | “wretched, unhappy”; the house word is “miserable”, “wretched” being reserved. | “miserable, wretched”. |
| 35 | ἐκέλευον (broaden) | low | Example ‘I urged’ against the unit's ‘I was ordering’. | ‘I was ordering’. |
| 36 | δυσαριστοτόκεια | low | “coined from” asserts a coinage. | “occurs only here, built from δυσ- + ἄριστος + τόκος”. |
| 37 | ἀπωσάμενον | low | “epic ἀπώσ- (= Attic ἀπωσάμενον)” — circular; the form is the ordinary Attic one. | Deleted. |
| 38 | ἐϋπλόκαμός | low | “fair-tressed, with beautiful locks” does not give the house “fine-plaited”. | “fine-plaited, fair-tressed”. |
| 39 | ὁρᾷ (broaden, new) | low | Existing entry is the subjunctive with ἂν … κεν; 18.61 is the indicative after ὄφρα, ‘while’. | Broadened. |
| 40 | ὤφελλε (broaden, new) | low | Existing entry ‘ought’ (of what ought not to have been); 18.19 is the unfulfilled wish. | Broadened. |
| 41 | ἀνὰ (broaden, new) | low | ἀνὰ θυμόν ‘in the heart’ not covered. | Broadened. |
| 42 | βοῶπις (broaden, new) | low | Existing entry names Hera and Clymene; here a Nereid (Halia). | Broadened. |

All other parses were checked against the line and left as they are: every novel form is in the gloss and no form of the part lacks an entry in known-forms ∪ novel-forms; the 17 original `__broaden__` entries each begin with the old entry whole and add one true reading; no entry is over 230 characters, none uses an ASCII apostrophe, none names a line. The glossary entries for ἀπώλεσα (‘I have lost’), ὑποδέξομαι and the other ones that repeat the Odyssey's wording were left, because they match the Odyssey's.

## C. Findings considered and refused

| Point | Reason |
|---|---|
| νεῶν ὀρθοκραιράων, “straight-horned ships” | Extends the Odyssey row (12.348) literally; the note says plainly that what a ship's ‘horns’ are is not known, and “perhaps” hedges the guess. No referent is chosen in the English. Kept. |
| σχέτλιος of Patroclus, “cruel one” | The table gives “cruel one” for every speaker and target (2.112 Zeus, 16.203 Achilles, Odyssey 13.293 Athena to Odysseus, “you cruel man”, with the note on the real force). The note here gives the range and the tone. Kept. |
| ἀεκήλια, “unwelcome deeds” | Marked uncertain in the note, compared with ἀέκων, “unseemly” kept for ἀεικής. Kept in the units (the glossary was brought into line, 29). |
| δυσαριστοτόκεια, `l` “ill-fated”, `i` “unhappy” | Both read δυσ- ‘ill’; the note says the word occurs only here and is read from its parts. “ill-fated” is a little stronger than ‘ill’ but the two layers do not disagree in sense. The second ὤ μοι not repeated in `i`: `i` is prose and drops an echoing exclamation. Kept. |
| γουνῷ ἀλωῆς, “on the rich ground of an orchard” | Table row 9.534 with “an” for “the” (a simile, so indefinite); note keeps the doubt about γουνός. Kept. |
| ἶσον ἐμῇ κεφαλῇ, “as much as my own head” | `i` is open to being misread as a size; the alternative “as I honoured my own head” rebuilds the line more than the Greek's bare dative allows. Both layers keep ‘head’, the note says it stands for the self. Kept. |
| Nereid names | Latin forms are consistent with the Odyssey's Phaeacian practice; the ei/ea difference (Thaleia, Amatheia, Callianeira against Galatea, Actaea) follows familiar spellings, not carelessness. Meanings offered in the note are standard readings, hedged where not clear. Kept. |
| ἦ μάλα at 18.18, `l` “truly very” against 18.12 “Truly, very much so” | 18.12 is ἦ μάλα δή (table 6.255, 15.14); 18.18 has no δή and “truly” is the word the table keeps for ἦ μάλα (1.558 row). Kept. |
| παῖς `l` “child” / `i` “son” (18.89) and “child's” (18.71) | Precedent for both pairings (1.393, 6.432, 13.659, and “child” for τέκος). Kept. |
| ἔμβαλον `l` “cast” / `i` “put” (18.85) | The usual `l`/`i` division; the note says ‘put into’. Kept. |
| γυῖα “the knees especially” (18.31 note) | A gloss on the figure, not a claim about the Greek word, which the note and the English keep as ‘limbs’. Kept. |
| πεδίοιο (18.7) | Both readings are in the note; the glossary entry covers ‘over’ and ‘from’. Kept. |
| “covered Achilles” at 18.22 against 17.591 | Checked: published 17.591 (iliad-114) `l` “So he spoke, and him a cloud of grief covered, dark,” — ours is identical except the final stop; published `i` “a dark cloud of grief covered Hector”, ours identical with “Achilles” in place of the name (odyssey-117 does the same with “the old man”). The note says the Greek has only τόν. The Odyssey unit has the same Greek and a different `i`, so the validator may print its Odyssey-difference warning; that is the expected one. Kept. |
| ἀποτίσῃ “pay the price” against the Odyssey's “exact payment” (11.118) | The Iliad table's ἀπέτισαν (4.161) is “pay back”; the Odyssey row is middle voice. “Pay the price for” is an acceptable active rendering and not wrong. Kept. |
| ἀπώλεσα “I have lost” in the glossary | Same as the Odyssey entry. Kept. |

## D. Cross-references in the notes (each looked up in the archive)

Correct: 1.151 (ἶφι μάχεσθαι), 1.362, 1.363, 1.364, 1.417, 2.787 (via the table), 4.123 (σίδηρον), 9.534 (γουνῷ ἀλωῆς), 11.837, 17.591, and the in-part references “line 2”, “lines 4, 8, 74”, “line 24”, “lines 30–31”, “line 54”, “line 56”, “lines 59–60”, “lines 89–90”, “line 38”. Wrong and fixed: 5.298 (→ 11.403, 17.90), 1.357 twice (18.35, 18.94), 16.775 (→ 16.776). In new-renderings.md the Odyssey numbers 5.84, 13.208, 11.118, 14.175, 6.165 and the Iliad numbers 3.385, 10.439, 11.668, 2.483, 9.631, 9.142, 5.302, 3.364, 4.469, 1.415, 1.413, 2.35 were looked up and are right.
Published repeats: 18.5, 18.73, 18.74a (shortened from 1.363), 18.78 and the 18.36 / 18.72 / 18.23 half-lines carry the published English; 18.15 first line likewise. Quotation marks: “ on 18.6, 18.18, 52, 73, 79, 95; ” on 18.14, 21, 64, 77, 93, 96; `mark` on those six first units and no other; speech 73–77 and 79–93 run across units without marks inside. Paragraph `p` flags sit on 1, 15, 22, 65, 78, 94 as in the packet. iliad-115 ends on the narrator, so no speech runs in; 18.96 closes Thetis' speech and 18.97 begins Achilles' answer.

## E. For the publisher (outside this review's remit; not edited)

- new-renderings.md rows now out of step with the units: the τελέσωσι row (it says τετελεσμένα/τετέλεσται “accomplish” and ἐξετέλεσσεν “bring to completion”; now all three are “fulfil” / “fulfilled”, with ‘accomplished’ and ‘brought to completion’ among the avoided); the ἐπισχερώ row (`l` is the table's “in a row” again, so the row should read “unchanged”); a new row is wanted for ἐκέλευον (“ordering” / “told”, “bade” reserved for ἄνωγα) and a one-line change to the δαΐφρων use (`l` “wise-minded” as in the table).
- Scansion: the packet flags nothing and no line is UNRESOLVED or AMBIGUOUS. Run independently, the scanner marks a spondaic fifth foot at 18.3 (ὀρθοκραιράων), 18.28 (Πάτροκλός τε) and 18.41 (καὶ Λιμνώρεια), all ordinary σπονδειάζοντες, and licences (correption, hiatus, synizesis in Μενοιτιάδεω at 18.93, digamma at 18.57) that need nothing said. No metrical sentence was added to any note.
