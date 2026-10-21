# iliad-037 review (6.116–231) — passes 1 and 2

Severity: high = wrong Greek-to-English or false grammar label that misleads about the text; medium = false claim or cross-reference in a note, or an `i` that can be misread; low = wording, house-consistency, tidiness. `t` untouched (checked: units still reproduce the packet). Gloss changes are made in `gloss.json`.

Totals (rows in the tables below): high 0 · medium 10 · low 23. Pass 1 (units.json): medium 6, low 13. Pass 2 (gloss.json): medium 4, low 10.

## Pass 1 — units.json (line · field · severity · wrong · done)

| line | field | sev | what was wrong | done |
|---|---|---|---|---|
| 121 | n | low | "Diomedes speaks before he can" — "he" ambiguous and unsupported | "Diomedes is the first to speak." |
| 139 | n | low | "Zeus struck him, and then every god hated him" asserted an order the Greek does not give | "he was hateful to every god, not to Zeus alone." |
| 141 | n | low | dative of the opponent attached to ἐθέλοιμι; it belongs to μάχεσθαι | rewritten |
| 145 | n | low | note said "why then", `l` says "why indeed" | note now "why indeed" |
| 147 | n | low | "φύλλα as the object of both verbs" — ἄλλα is the object of φύει | note: τὰ μέν object of χέει, ἄλλα of φύει |
| 147 | i | low | "when the season of spring comes on" turns a coordinate clause into a subordinate one | "…puts forth others, and the season of spring comes on;" |
| 167 | i | medium | "so that he might die" reads as the father-in-law dying | "so that Bellerophon might die." |
| 167 | n | medium | subject of ὄφρ' ἀπόλοιτο not stated; note also 156 words (WARN band) | rewritten, 127 words, names the subject |
| 174 | n | low | "one ox for each day's feast" stated as fact | hedged: Greek does not say one a day |
| 178 | l | low | πεφνέμεν as "slay"; table gives ἔπεφνε "killed" (4.397), the unit's own κατέπεφνε are "killed", "slay" is kept for ἐναίρω | "kill" |
| 180 | n | medium | 4.398 is where Tydeus lets Maeon go, not a victory won by portents | note now says same clause as 4.398, both heroes act on signs |
| 185 | n | medium | "ἀνδρῶν goes with the superlative" contradicts the note's own 3.241 parallel and the `i` ("fighting of men") | "goes with μάχην" |
| 191 | n | low | trimmed to stay in band | — |
| 191 | n | low | scansion flag, line 192 | added: "Line 192 is metrically irregular as transmitted: θυγατέρα has its first syllable lengthened in the fifth foot, and its short last syllable stands in the long place of the sixth, before ἥν." |
| 194 | i | low | "above all others" for ἄλλων adds force | "above others" |
| 205 | n | medium | "All three children are named and their ends told" — Hippolochus's end is not told | "two die here, Isander and Laodamia; the third, Hippolochus, lives to be Glaucus' father" |
| 205 | n | low | χολωσαμένη labelled participle of χολόω | χολόομαι |
| 216 | n | low | cross-reference "verb of 191"; κατέρυκε stands in 192 | 192 |
| 222 | n | medium | 4.376–398 is Tydeus' embassy before the war, not the war in which he died | rewritten |

Line 192 hand scan: αὐ-τοῦ | μιν κα-τέ | ρῡ-κε δί | δου δ'ὅ γε | θῡ-γα-τέ | ρα ἥν. Sixteen syllables, four dactyls; feet 5 and 6 only work if θυ- is lengthened and the short -ρα counts long before ἥν (it would by position if ἥν began with a digamma, which the note does not claim). Irregularity real; sentence added.

Unit 219–221 (merged): correct. Nothing is printed at the end of 220, not even a comma, and a comma would not end a unit anyway; the clauses run on joined by καί, μιν is the cup (the neuter use is real), and `l`/`i` follow. Note true as written; left unchanged. Caveat for a human: I cannot look at the printed edition, so if it prints a stop after ἀμφικύπελλον the archive has dropped it and the build would not notice.

Boundary check: iliad-036 ends with Hector's speech closed (”) at 115; 037 opens in narrative. 037 closes Diomedes' speech at 231; nothing runs on. Quotation marks balanced and placed (“ 123, ” 142; “ 145, ” 211; ‘ ’ Anteia 164–165; “ 215, ” 230); marks and `p` flags correct (116, 119, 144, 212).

## Pass 1 — findings refused

- Ἐφύρη as "Ephyre" (Odyssey list has "Ephyra"): iliad-013 already ships "Ephyre" for the Iliad.
- χολωσαμένη "angered / in anger" against table "enraged": the shipped Iliad uses both (iliad-009, -013, -026 "angered"; -020, -025 "enraged"); drafter's row records the choice.
- ψευσαμένη "lying" (possible misreading as "reclining"): idiomatic in context; "falsely" and "with a lie" were considered and turned down in new-renderings.
- `i` "paths of men" for singular πάτον: collective singular, no change of sense.
- "scatters" for χέει of leaves: rebuilt from `l` "pours" and recorded; not a remembered phrase.
- "perfect of μέμονα" for μεμαῶτε: LSJ/Autenrieth file the participle under both μέμονα and μέμαα; label not false.
- `i` "in fear" for φοβηθείς: smoothing, `l` has "frightened". (Observation only: new-renderings row 25 says "frightened" is kept for φοβηθείς, which is true of `l` only; fix when the rows are copied.)
- `l` ending "—" against `i` ":" at 150–151: both punctuate the same break.
- 2.389 "man-covering shield" picture of the shield: hedged ("the picture is of"), reference checked and true.
- All other cross-references checked against the source and published parts and true: 1.496, 2.658, 3.210, 3.241, 4.139, 4.392, 5.335, 5.813, 5.855, 6.4, and the in-part references.

## Pass 2 — gloss.json (every parse read against the line)

205 keys: 204 novel forms (all present, none extra) plus 25 `__broaden__` entries; each broadened entry begins with the old entry whole plus " · " (checked by script); no existing key overwritten; coverage complete; every entry under 230 characters, typographic ’ only, no backticks.

| key | sev | what was wrong | done |
|---|---|---|---|
| φύει | medium | "transitive 'brings forth'" only; it is intransitive "grows" in the line "one grows, one ceases" | both uses |
| σεβάσσατο | medium | lemma σέβομαι with "shrank from", against σεβάζομαι "feel awe" in the note and `i` | σεβάζομαι, "felt awe" |
| ξείνισ | medium | "ξείνισ' = ξείνισσε": elision of ξείνισσε would leave ξείνισσ' | = ξείνισε |
| λυκούργου, λυκόοργος | medium | "Λυκούργου (= Attic Λυκούργου)", self-equating; lemma not the usual Λυκοῦργος | lemma Λυκοῦργος, uncontracted/contracted stated |
| ἀμαιμακέτην | low | gave "irresistible, raging" as if known; note says unknown | unknown, guesses named |
| ἀντιανείρας | low | "traditional sense" hid the dispute | sense disputed |
| κατέπεφνε, κατέπεφνεν, πεφνέμεν | low | lemma "πέφνω"; the glossary already uses φένω / καταπέφνω (φένω); "slew" vs "killed" | aligned |
| βασιληΐδος | low | lemma βασιλήϊος for a form of βασιληΐς, -ΐδος | lemma corrected |
| θυμοφθόρα | low | "life-destroying" against the shipped "heart-destroying"; sense not clear | fixed |
| λαοδάμειαν, λαοδαμείῃ | low | "Laodameia"; the English layers say "Laodamia" | spelling |
| νυσήϊον | low | "mount" asserted; the place is unknown | "a place sacred to Dionysus (site unknown)" |
| σολύμοισι | low | gloss "with the Solymi" reads as "alongside" | object of μαχέσσατο: "the Solymi" |
| συνίτην | low | lemma συνέρχομαι; the verb is σύνειμι (εἶμι) | corrected |
| τεθναίης | low | "or command"; it is a wish | removed |

Pass-2 refused: κέρδιστος "most cunning, craftiest" (entries give general meaning, `i` has "shrewdest"; fine); ἐπαμείψομεν "fut. indic. (or short-vowel aor. subj.)" (hedge is accurate); κατέρυκε "unaugmented" (Homeric ἐρύκω keeps ε; defensible); φαίδιμος broadening naming Glaucus (parallels the existing Hector/Ajax wording); πυκινὸν "close-woven, cunning" broadening (adds the reading `l`/`i` use at 187).

## Counts

Pass 1 (units.json): high 0, medium 6, low 13.
Pass 2 (gloss.json): high 0, medium 4, low 10 (table rows; 17 keys edited).
Both passes: high 0, medium 10, low 23.
