# Review — odyssey-107 (Odyssey 22.101–194)

## Pass 1

Method: every note read against the Greek of its unit and the packet line by line; Greek to `l` word by word; `l` against `i`; `l`/`i` against the shipped wording for the repeated and near-repeated lines (a similarity scan of all 94 lines against every published unit, not only the packet's exact repeats); quotation marks and `mark` checked unit by unit, and the neighbour (odyssey-106, last unit at 22.99, ends `winged words he spoke:` with Telemachus about to speak, so the note on 22.101 is true). No scansion flags in the packet, so none scanned by hand. `t` untouched (verified identical before/after). `gloss.json` not read or touched.

Counts: high 1 fixed + 1 open; medium 4; low 11.

### Changes made

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 22.165 | l, i, n | high | ὀϊόμεθ’ is present (‘we suspect’); the note itself said ‘we suspect’, but `l` and `i` (and the note's gloss) said ‘suspected’. | `l` ‘whom we ourselves suspect’, `i` ‘the one we ourselves suspect’, note made to say present throughout. |
| 22.102 | l | medium | ‘an all-bronze helmet, fitted upon the temples’ departs from the shipped line κυνέη πάγχαλκος, ἐπὶ κροτάφοις ἀραρυῖα (odyssey-091): ‘a helmet all of bronze, fitted upon my temples’; new-renderings.md wrongly presented πάγχαλκος as a new choice. | `l` now ‘and a helmet all of bronze, fitted upon the temples’ (`i` already had ‘all of bronze’). |
| 22.127 | i | medium | ‘at the very top of the threshold’ drops παρά ‘beside’ and moves ἀκρότατον off οὐδόν; disagrees with `l` ‘by the topmost threshold’. | `i` ‘and beside the topmost threshold of the well-founded hall’. |
| 22.154–156 | n | medium | Note says ‘The ano teleia ends the unit’; the unit ends at the full stop after ἀμείνων, and the ano teleia is mid-line 156 after ἀγκλίνας. | Note now says the ano teleia falls in the middle of line 156 and the unit ends at the full stop. (See open finding below.) |
| 22.192–193 | n | medium | ‘Nothing says whom the rope is tied to’ contradicts the Greek ἐξ αὐτοῦ and the note on 175 (‘attached to him’). | Replaced by: ἐξ αὐτοῦ ‘from him’ is again the rope made fast to the man, as in 175. |
| 22.101 | n | low | τοι called a particle ‘I tell you’, while `l` and `i` render it as ‘you’ (‘bring you’). | Note now gives both possible readings and says the English takes ‘you’. |
| 22.102 | n | low | ‘here πάγχαλκος “all-bronze”’ no longer matches `l` after the change above. | ‘all of bronze’. new-renderings.md row for πάγχαλκος changed to ‘all of bronze’ / ‘all of bronze’, citing odyssey-091. |
| 22.121 | l, n | low | ‘against the all-shining wall-faces’ departs from the shipped ἔκλιναν πρὸς ἐνώπια παμφανόωντα (odyssey-014, ‘against the shining inner wall’). | `l` ‘against the shining inner walls’ (matches `i`); note: παμφανόωντα ‘shining’ (literally ‘all-shining’). |
| 22.129 | l | low | δέ in τὴν δ’ not rendered. | `l` ‘And this Odysseus bade …’. |
| 22.136 | n | low | ‘a stock epithet of kings’ is a claim about the rest of the poem this part cannot show, and Agelaus is a suitor. | ‘a stock epithet meaning “Zeus-nurtured”’. |
| 22.138 | n | low | Glossed ὅς τ’ ἄλκιμος εἴη as ‘who is valiant’ and ‘if he is valiant’; the verb is optative and `l` says ‘if he were valiant’. | Note says ‘who would be valiant’ … ‘if he were valiant’, the optative matching ἐρύκοι. |
| 22.139–140 | n | low | ‘The ano teleia falls in the middle of the line’ left the line unnamed. | ‘… of line 140’. |
| 22.140–141 | n | low | Quotes ‘ὁ υἱός’, which is not in the line (it reads φαίδιμος υἱός). | Quote corrected. |
| 22.165 | l | low | κεῖνος δ’: δέ not rendered. | `l` begins ‘and that ruinous man again’. |
| 22.169 | l | low | ‘in your own house’: σῷ is plain ‘your’ (as `i` and the note say); ‘own’ belongs to ᾧ at 117, not here. | ‘in your house’. |
| 22.184 | n | low | ‘a word that belongs to a person and is unusual with a thing’ asserts usage beyond this part. | ‘γέρον … is the neuter of γέρων “old man”, a word for a person, here said of the shield that was a man’s.’ |

### Open finding (not fixed: instructed not to touch `t`)

- **22.122–125, 22.129–130, 22.154–156 · unit boundaries · high.** Three units contain an ano teleia before their end: unit 122 (after ἔνευεν· at the end of 124), unit 129 (after αὐτῆς· mid-130), unit 154 (after ἀγκλίνας· mid-156). Conventions (‘Verse and segmentation’) end a unit at every full stop, Greek question mark or ano teleia; the pilot and odyssey-106 have no such internal stop. Splitting means re-cutting `t` (text preserved, only the boundary moves), plus splitting `l`, `i` and `n` for each. Proposed cuts: 122–124 | 125 (`εἵλετο δ’ ἄλκιμα …`); 129–130a (`…αὐτῆς·`) | 130b (`μία δ’ οἴη γίγνετ’ ἐφορμή.`); 154–156a (`…ἀγκλίνας·`) | 156b (`τῶν δὲ σκοπὸς ἦεν ἀμείνων.`). The `validate_odyssey.py` does not check this, so it will not stop the build; it needs a decision before building (the glosser's work is unaffected by the split).

### Considered and refused

- 22.101 `i` ‘Father’ for ὦ πάτερ: vocative O dropped in `i` only; `i` is permitted to lighten interjections, as in 22.132 and 22.151.
- 22.117 `i` ‘taking aim at each’: ‘at each’ is not in the Greek but follows ἕνα … αἰεί; harmless in `i`.
- 22.126 `n` ἔσκεν ‘simply there was’: ἔσκεν is the iterative-type form of ἦν, but the note only claims the sense here; left.
- 22.130 `n` γίγνετ’ ‘is γίγνετο, the imperfect’: γίγνετ’ could also be an elided γίγνεται; the context (past narrative) and `l` ‘was’ settle it, and the note claims no more. Left.
- 22.136 (second unit) `l` ‘the court’s fair doors’: ἄγχι could take αὐλῆς (‘near the court’) instead; the note already says ‘The Greek does not say what the doors are near’. Both readings are honest; left.
- 22.147 `i` ‘and his heart too’: shipped wording (odyssey-025), must stay.
- 22.151 `i` ‘against us’ for νῶϊν ‘for us two’: reads as the force of ἐποτρύνει πόλεμον; the note gives the literal dative. Left.
- 22.186 `i` ‘simply lay there’: ‘simply’ carries δὴ … γε … ἤδη; left.
- 22.149 `n` ‘short and flat after the long description’: a literary remark, not a grammatical claim; left.
- 22.140, 159, 165 ὀΐω rendered ‘suppose / suspect’ where earlier parts mostly have ‘I think’: odyssey-074 and -105 already use ‘suppose’, the table has no ὀΐω row, and the choice is recorded in new-renderings.md; left. (Medium risk of reading as inconsistent; the owner may want one row.)
- 22.142 `n`/`l` ‘clefts’ for ῥῶγας, 22.126 ‘raised door’, 22.122 ‘four-layered’, 22.174 ‘tie boards on behind’: all uncertain words, each already said to be unknown in its note; no further edit.
- Remembered English: none found. Phrases checked as possibly arriving formed (‘the task before him seemed a great one’, ‘spattered with grime’, ‘gave way’, ‘bond that grieved the heart’) are built from the case relations or are shipped wording.
- Quotation marks: all correct (opens 101/106/132/136/151/154/164/171; closes 104/107/134/141/152/159/169/177; `mark` on each first unit; 22.194 introduces a speech that falls in the next part, no marks needed here).

### For pass 2
Re-read `gloss.json` against the edited lines (esp. ὀϊόμεθ’ ‘suspect’ and πάγχαλκος); confirm the unit-split decision.

## Pass 2

Done on the coordinator's instruction (the runbook authorises re-cutting `t` for internal ano teleiae). The open finding of Pass 1 is closed by the three splits below. Counts for Pass 2: high 0 (the Pass 1 open high finding is resolved by the splits), medium 8, low 7, all in `gloss.json`.

### Splits (units 50 → 53)

`t` re-cut by script at the ano teleia; the joined `t` of all 53 units equals the packet's lines exactly (whitespace-insensitive check passed). `ln`, `v`, `p`, `mark` and quotation marks kept correct: `mark` and the opening “ stay on the first half (154), no ” on either half of 154–156 (the speech runs to 159).

| Old unit | New units | Notes |
|---|---|---|
| 22.122–125 | 122–124 `…ἔνευεν·` / 125 `εἵλετο δ’ ἄλκιμα…` | `l`, `i`, `n` divided; note on 122 gains ‘the ano teleia after ἔνευεν ends the unit’; note on 125 says it opens a new sentence |
| 22.129–130 | 129–130a `…αὐτῆς·` / 130b `μία δ’ οἴη γίγνετ’ ἐφορμή.` | second half `l` ‘and only one was the way of attack.’, `i` ‘for there was only one way to attack from.’ |
| 22.154–156 | 154–156a `…ἀγκλίνας·` / 156b `τῶν δὲ σκοπὸς ἦεν ἀμείνων.` | note on first half now ends ‘the unit ends at the ano teleia’; second half carries τῶν/σκοπός/ἀμείνων and says the speech ends only at 159 |

### Re-check of all units
Quotation marks balanced and paired in `l` and `i` for all eight speeches; every speech's first unit has `mark`; line counts of `t` and `l` agree in all units; no ASCII apostrophes; every `t` ends at a stop. Nothing further found in the Greek → `l` → `i` pass beyond Pass 1.

### `gloss.json` — changes
| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| κεκορυθμένα | medium | gloss ’tipped’ contradicts the note and `l` (‘armed’) | ’armed’ (with bronze) |
| ἄζῃ, πεπαλαγμένον | medium | ‘mould’ gloss while the rendering is ‘grime’ (‘mould’ was refused in new-renderings.md) | ’with grime’, ’smeared’ (with grime) |
| κουρίξ | low | example gloss ’dragged by the hair’ pinned to the line and put a verb into an adverb's gloss | ’by the hair’ |
| τετραθέλυμνον | low | ‘of an ox-hide shield’ asserts what this part does not show | removed |
| ἀΐδηλος | medium | stated ‘destructive, baneful, hateful’ as certain; sense is disputed (‘destroying’ or ‘unseen’) | now says disputed |
| ἀγχιστῖνοι | low | meaning given as known | ‘sense inferred from ἄγχι’ |
| ὀρσοθύρη, ὀρσοθύρην | medium | ‘a door set up above floor level’ stated as fact; note says kind of opening not known | ‘(kind of opening not known)’ |
| ἔρυσάν, ἔρυσαν | low | ‘= Attic εἴρυσαν’ is not an Attic equivalent | clause removed |
| εἴη (138) | medium | existing entry has no relative-clause generic optative without κε | broadened |
| ἔσκεν (126) | medium | existing entry only ‘used to be’; here plain ‘there was’ | broadened |
| ἐπεπείθετο (108) | medium | existing entry says plpf. ‘was won over’; the form is the imperfect of ἐπιπείθομαι ‘obey’ (augment after the preverb) | broadened with the correct reading; old entry kept whole |
| ἤμβροτον (154) | low | existing entry ‘I missed (+gen.)’; here ‘I erred’ with accusative of respect | broadened |
| ἐνώπια (121) | low | existing entry is specific to the porch; here a hall | broadened |
| λόφος (124) | medium | existing entry ‘ridge, hill’ only; here a helmet's crest | broadened |
| αἰνῶς (136) | low | existing readings do not include intensifying an adverb (ἄγχι αἰνῶς) | broadened |

Checked and left: ὀϊόμεθ’ (known entry ‘we suppose’, present, agrees with the corrected ‘we ourselves suspect’), πάγχαλκον (‘all of bronze’, matches the edited `l`), the other 85 novel entries and 11 broadened entries already present (parses true of the line), all under 230 characters; every token of `t` is covered by `known-forms.json`, `novel-forms.json` or `gloss.json`. Left as is: μεμαῶτας ‘= Attic μεμαότας’ (not a true Attic form, but harmless); σάκε ‘Attic σάκη’ (acceptable); κάλλιπον ‘aor. 1 sg.’ (the only use here).
