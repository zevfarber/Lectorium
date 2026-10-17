# iliad-009 (2.182–277) — review

Two passes. Pass 1: notes against the lines, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, packet scans. Pass 2: `gloss.json` against the lines. `t` was never touched (units 239 and 240 were joined by concatenating their existing `t` strings with the single space the edition prints; the whole part's `t` still equals the source lines). Severity: high = would fail the gate or put wrong English in the book; medium = wrong claim, wrong sense or house-rule breach; low = imprecision.

Totals: high 1, medium 10, low 16 (units.json 12, gloss.json 15; one item, the merge, is counted once). No scansion flags in the packet, so no hand scans were required and no metre sentences were added.

## Pass 1 — units.json

| line · field | sev | what was wrong | what was done |
|---|---|---|---|
| 239–240 · structure, `t`/`l`/`i`/`n` | high | The drafter's separate unit for 2.240b (ἑλὼν γὰρ ἔχει γέρας αὐτὸς ἀπούρας.) has the same letters as the whole unit at iliad-004 line 356 (Achilles, 1.356), which the packet did not list. The validator's whole-unit rule (letters only, punctuation ignored) would force that unit's published English: "my prize of honour" and a closing ” on Thersites' words. The draft's English ("his prize") would fail the gate. | Joined the unit with 239 (ὃς καὶ νῦν … ἠτίμησεν·), so the line-level repeat sits inside a unit with no published twin. The second half keeps the iliad-005 wording. `t` is the two existing `t` strings joined by the edition's space; `l` has two lines like `t`; the note is merged and says line 240 is word for word 1.356. A script check confirms no unit of this part now collides with a published Iliad unit; the only whole-unit repeats are 2.257 and 2.271, which match the Odyssey units exactly. |
| 185 · `n` | medium | Said "the line σκῆπτρον πατρώϊον ἄφθιτον αἰεί is the one used at 2.46". It is not a line: 2.46 begins εἵλετο δὲ, and only the last four words repeat. | "the phrase … also ends 2.46, where Agamemnon takes the sceptre up". |
| 207b · `l` | medium | πολυφλοίσβοιο rendered "loud-roaring" in `l`. The house table (Odyssey 13.220, adopted by the Iliad conventions) fixes `l` "much-roaring" and `i` "loud-roaring". | `l` "much-roaring"; the note now states both renderings. |
| 250 · `i` | medium | "you must not stand there declaiming": "stand there" adds a posture the Greek does not give, "must" is stronger than the optative with οὐκ ἂν (the note itself says "should not … a mild prohibition"), and `i` no longer parallels `l`. | "So you should not declaim with kings on your lips, hurl reproaches at them and keep watch for your homecoming." |
| 254 · `i` | medium | "you sit there reproaching … but you stand and speak out": ἧσαι ὀνειδίζων puts him seated; "stand" contradicts it and is not in the Greek. | "but you, taunting, speak out." |
| 182 · `l` | low | "it was taken care of by the herald" turns active κόμισσε (subject κῆρυξ) into a passive. | "and took care of it / the herald Eurybates …" (line division kept). |
| 195 · `n` | low | χολωσάμενος called the aorist participle of χολόω "make angry"; the form is middle ("having become angry"). | "aorist middle participle of χολόομαι ‘become angry’ (χολόω ‘make angry’ …)". |
| 221b · `i` | low | `i` "shrill reproaches" reads ὀξέα as an adjective with ὀνείδεα, against its own `l` ("shrilly") and the note ("taken as an adverb"). | "he shrilly screamed out reproaches at heavenly Agamemnon". |
| 226 · `n` | low | "τοι is τοι = σοι" (circular). | "τοι (= σοι) is ‘for you’". |
| 229 · `i` | low | "may have bound and led in" makes the aorist subjunctive a completed past. | "may bind and lead in". |
| 232 · `n` | low | κατίσχεαι said to be from κατέχω; it is κατίσχω/κατίσχομαι. | "κατίσχομαι (= κατέχω)". |
| 258 · `i` | low | "If I find you again": ἔτι with the participle is "still", as `l` has it; "again" changes the force. | "If I still find you acting senselessly as you are now". |
| `new-renderings.md` | — | Rows for κεκλήγων, ἀγορεύοις, ἀνὰ στόμ’ ἔχων, νόστον φυλάσσοις and the closing paragraph disagreed with the changed units. | Rows brought into line; closing paragraph now records the 2.240 merge (and the iliad-004 collision) as well as the 2.241–242 merge. |

## Pass 2 — gloss.json (every parse checked against the line)

All 240 novel forms are present, none is redefined, none is outside the part; every entry is under 230 characters, uses only ’, and has no line number. Checked all 240 novel entries, the 19 broadenings and the 262 known-form entries against their uses here.

| form · key | sev | what was wrong | what was done |
|---|---|---|---|
| τά (broaden) | medium | New reading "relative, neut. acc. pl." for τά τ’ αἰδῶ ἀμφικαλύπτει; τά is the subject of ἀμφικαλύπτει (the clothes), so nominative. | "neut. nom. pl." |
| πέπονες | medium | Asserted "womanish, a term of reproach" as fact, against the unit's note (meaning not known) and the existing Odyssey entry for πέπον. | Rewritten on the Odyssey entry: "in address a familiar ‘good (friend)’, exact sense uncertain; masc. voc. pl. (said to a crowd, scornfully)". |
| δειδίσσεσθαι | medium | Glossed "frighten, scare … active in sense", while the note and both layers read "to be frightened". | "δειδίσσομαι — be frightened, fear …; pres. inf. mid.: ‘to be frightened’". |
| ὀνείδεα (missing broaden) | medium | Known entry gives only "neut. nom. pl."; in the line it is the accusative object of λέγ’. | New broaden: old entry whole + "also neut. acc. pl., object". |
| δαιμόνι | medium | Gloss "my good fellow" is the πέπον rendering, turned down for δαιμόνιε (house "Strange man"; Odyssey entry "strange one"). | "‘strange one’ (gentle or chiding, tone uncertain)". |
| κατίσχεαι | medium | Parse "after ἵνα": ἵνα governs μίσγεαι; κατίσχεαι stands in the relative clause ἥν τ’ … κατίσχεαι. | "in a relative clause: ‘whom you keep back’". |
| θαλερὸν | low | Example "a big, swelling tear" contradicts the shipped "an abundant tear". | "‘an abundant tear’". |
| ἀκριτόμυθε | low | Meaning given as settled; the note says it is not known. | "(exact sense uncertain)" and the three candidate senses. |
| τι (broaden) | low | New reading "adverbial acc. … ‘at all’" for μή τι … ῥέξῃ κακὸν, but both layers take τι with κακόν ("some evil"). | "neut. acc. sg. with κακόν after μή: ‘some’". |
| αὐτὸν (broaden) | low | "plain pronoun … ‘you’" for αὐτὸν δὲ κλαίοντα, which `l` renders "you yourself". | "intensive, with the object already named by a pronoun: ‘you yourself’". |
| ὀξέα | low | "epic -έα": the neuter plural is the same in Attic. | Removed the label. |
| τόνδε | low | "this here" (the word "here" is barred in entries). | "this, this one". |
| ἥρωες (new broaden) | low | Known entry says "voc. pl. … in address"; the use is nominative subject (ἥρωες Δαναοί … διδοῦσιν). | Broadened with "also nom. pl., subject". |
| ὥς (new broaden) | low | Known entry covers "as; so that"; ὥς νύ περ ὧδε is "so, thus". | Broadened. |
| μηδ (new broaden) | low | Known entry covers only "with an imperative"; μηδ’ ἔτι … εἴην is a wish. | Broadened. |

## Findings considered and refused

- **Joining 241–242 in one unit (the drafter's question): accepted.** A standalone 242 has the same letters as iliad-003's unit (line 232), so its `l`/`i` must equal the published English, which has no closing ”; the ” cannot be added without a validator failure. The two lines are one argument (ἀλλά … ἦ γὰρ ἂν …, the γάρ clause explains the first), the join is made at the edition's own ·, 36 units in iliad-001 already carry an internal ·, and the published English for 242 is carried over intact inside the longer `i`. Not a sense-unit violation.
- **Quotation marks: all correct, no change.** Five speeches (190–197, 200–206, 225–242, 246–264, 272–277); each opens with “ on the `mark` unit and closes with ” on its last unit, 5 and 5 in both layers, and no unit between carries a stray mark. iliad-008 ends with the closing ” of Athena's speech, so 182 correctly has none; 2.278 is narrative (ὣς φάσαν ἣ πληθύς), so nothing runs on into iliad-010. `p` flags sit exactly on the seven edition paragraphs (182, 188, 198, 207, 211, 243, 265); `ln` is right on all units.
- **Remembered English:** nothing found that arrived formed rather than from the grammar; "Strange man", "My good fellows", "Zeus-nurtured kings", "counsellor", "crooked cunning", "manly/proud spirit" and "abundant tear" are all house-table renderings.
- **272–273 `i` "arming for war" against `l` "arming war":** left. The note declares the phrase bold and gives "arming battle", and `i` has to be English; no sense is lost.
- **Known entries κακῶς (253) and ἔτι:** known entries judged adequate (κακῶς "miserably" covers "badly"; ἔτι needs no "no longer" since μηκέτ’ is separate).
- **196–197 `i` "each of them" for ἑ:** left; the note explains the generalising singular.
- **193 `i` "only making trial" for μὲν … δέ; 248 `l` "I say there is no other mortal" (negation carried to the infinitive):** left as faithful in force.
- **216 "the ugliest man who came to Ilium"; 227 `i` "picked out for you"; 235 `l` "O good ones":** left; each follows the grammar and the table.
- **πολυφλοίσβοιο known glossary entry ("loud-roaring")**: left, since entries are not rewritten; the unit now follows the table.
- **Scansion:** packet flags "none"; no line was scanned by hand and no metrical sentence added.
