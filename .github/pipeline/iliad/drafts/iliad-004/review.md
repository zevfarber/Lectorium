# iliad-004 (Iliad 1.312–412): review

Reviewer pass 1 (every grammatical label, positional claim and cross-reference in every note checked against the line; the four Odyssey cross-references checked against the published Odyssey JSON; Greek → `l` word by word; `l` ↔ `i`; remembered English; quotation marks, `mark` and `p`; house tables; new-renderings rows) and pass 2 (the whole file re-read after the edits, and `gloss.json` checked parse by parse against the lines, known forms checked for uses their entries do not cover). Sources used: the Greek, the Iliad and Odyssey conventions and house tables, the published Odyssey units (every unit of this part was run against all published Odyssey and Iliad units for shared three-word sequences, since the packet lists only whole-line matches), `iliad-001`–`003` as English precedent. No modern translation consulted or recalled. `units.json` edited in place by script; `t` untouched (checked: every `t` identical to the pre-review file, the units still concatenate to the packet's 101 lines, 738 words). `gloss.json` existed at pass two and was corrected in place.

Counts, `units.json` (and its `about`): 29 changes (3 high, 6 medium, 20 low), touching 33 fields; plus 5 edits to `new-renderings.md`.
Counts, `gloss.json`: 15 changes (3 high, 4 medium, 8 low): 12 entries corrected and 3 missing broadenings added.
Total: 44 changes (6 high, 10 medium, 28 low).

Severity: high = a house rendering fixed by the Odyssey table ignored, or a note or gloss that states something false about a form; medium = a wrong claim about where a word stands or what the poem says, a note contradicting its own `l`/`i`, a gloss that mislabels or omits a use, an overconfident statement of an uncertain reading, a whole-line Odyssey match not followed; low = precision, particle force, polish, length.

## Cross-references checked (all true)
- 312: "also Odyssey 4.842": 4.842 is μνηστῆρες δ’ ἀναβάντες ἐπέπλεον ὑγρὰ κέλευθα (odyssey-021): the second half is identical. The note missed that the whole line is Odyssey 15.474 (odyssey-076), see below.
- 361: "Odyssey 4.610" is the line χειρί τέ μιν κατέρεξεν ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν (odyssey-019, second line of the unit at 609); "of a goddess, 5.181" the same line of Calypso (odyssey-023, unit at 180). Both true, and the English matches with "her".
- 342: "Odyssey 24.452" is ὁ γὰρ οἶος ὅρα πρόσσω καὶ ὀπίσσω (odyssey-119). True.
- Iliad cross-references (210, 244, 321, 323, 326, 327→316, 333, 338, 353, 355, 356, 358, 374, 379, 398, 1.11, 1.12–16, 1.22–25, 1.44, 1.94, 1.143): all true. Lines 372–375 and 376–379 repeat 1.13–16 and 1.22–25 word for word, and the English of every repeated unit is identical to iliad-001's.

## Changes: `units.json`

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 338 · l, i, n | high | ἀπηνέος rendered "ungentle". The Odyssey fixes "unkind" for ἀπηνής in four published units (18.381, 19.329, 23.97, 23.230; its note calls "unkind" the house rendering) and the Iliad table binds. The new-renderings row did not mention the Odyssey rendering or give a reason to depart. | `l` and `i` "that unkind king"; note says "‘unkind’ by the Odyssey’s house rendering … origin not known"; row rewritten (ungentle listed as the first draft, avoided). |
| 337 · n | high | "ἔξαγε is the aorist imperative of ἐξάγω". The aorist imperative of ἄγω is ἄγαγε; ἔξαγε is the present imperative (the gloss had it right). | "present imperative". |
| 386 · n | high | "κελόμην is the aorist of κέλομαι". κέλομαι has only present and imperfect (aorist κεκλόμην, ἐκέκλετο); κελόμην is the unaugmented imperfect, used as a narrative past. | Note: "the unaugmented imperfect … used as a narrative past". (Gloss corrected to match, below.) |
| 312 · l, n | medium | The whole line οἱ μὲν ἔπειτ’ ἀναβάντες ἐπέπλεον ὑγρὰ κέλευθα is Odyssey 15.474 (odyssey-076: `l` "They then, having embarked, sailed over the watery ways"). The packet did not list it (accent on οἳ differs); the draft had "They, then, … were sailing over" and the note named only the half-line 4.842. | `l` "They then, having embarked, sailed over the watery ways,"; `i` unchanged (already compatible); note now says the line is Odyssey 15.474 word for word apart from the accent, with the same English, its second half also 4.842; ἐπέπλεον ‘sailed over’ (an imperfect). |
| 334 · n | medium | "in ὔμμες, and in the dual only when he speaks of them as a pair (σφῶϊ in the next line)": ὔμμες is at 335 (the next line) but σφῶϊ is at 336, two lines on; "only" overstated, since the dual recurs at 338 (σφωϊν, ἔστων). | "in ὔμμες of the next line, and in the dual when he speaks of them as a pair (σφῶϊ at 336, σφωϊν and ἔστων at 338)". |
| 342 · i | medium | "does not know how to look at once at what lies ahead … to see how the Achaeans may fight": νοῆσαι is "think" (note and `l`), not "look"; "to see how" made the ὅππως clause a purpose. | "think at once of what lies ahead and what lies behind: how the Achaeans may fight safely for him beside the ships.” (the Odyssey’s 24.452 wording kept). |
| 365 (second unit) · n | medium | The note explained τοι (= σοι) but left ἤ unexplained, while `l` has "why indeed to you". | "ἤ is the particle ἦ ‘indeed’, and τοι is to be taken as σοι ‘to you’". |
| 380 (first unit) · n | medium | "the narrator’s name for a figure already introduced": the speaker is Achilles, not the narrator. | "Achilles’ name for Chryses, a figure the poem has already introduced". |
| 393 · n | medium | "ἑῆος is the epic genitive of ἑός ‘one’s own’": stated as fact, but ἑῆος is also read as the genitive of ἐΰς ‘good’ (the glosser records both). | "taken as ‘one’s own’ (ἑός …), though the form is also read as the genitive of ἐΰς ‘good’"; row marked "+ note" and "your good son" listed as avoided. |
| 317 · n | low | "ἷκεν … the unaugmented aorist of ἱκάνω": the form belongs to ἵκω (gloss agrees). | "the unaugmented past tense of ἵκω ‘come to’". |
| 318 (first unit) · l, i, n | low | πένοντο "were busy"/"busy"; the Odyssey ships "were busied" / "busied themselves" for the same verb in the same context (4.624, 24.412, περὶ δεῖπνον … πένοντο). | `l` "were busied with these things", `i` "busied themselves with these tasks", note "‘be busied with’ (the Odyssey’s verb for busying oneself with a meal)"; row rewritten. |
| 323 · l | low | "by the hand taking her": the note says the Greek gives no object; `l` supplied one. | "taking (her)" (supplied word in parentheses, the Odyssey's `l` practice). |
| 324 · l | low | "does not give her … shall take her" supplies two objects the Greek lacks (the note says "understood"); iliad-002 137 has the same clause without. | "does not give, I myself shall take,"; `i` keeps "her". |
| 333 · l | low | "knew it": the note says the Greek gives ἔγνω no object. | "But he knew in his own wits". |
| 333 · n | low | "(ἧσιν)" for the printed ᾗσιν. | "(= ἑῇσιν)". |
| 337 · n | low | "it is a courtesy and is not a statement of descent" (an unsupported claim about Patroclus); "epic vocative of Πάτροκλος" for the fuller form Πατροκλέης. | "a courtesy of address to Patroclus"; "the vocative of Πάτροκλος in its fuller form Πατροκλέης". |
| 338 · n | low | "μάρτυροι takes πρός with the genitive": πρός is not governed by μάρτυροι. | "is followed by πρός with the genitive, ‘in the presence of’". |
| 342 · n | low | 112 words, then 113 after the ὅππως edit (limit 110); ὅππως unparsed as a form. | "ὅππως (= ὅπως)", "is foresight and hindsight, as at Odyssey 24.452", and "said of a man in a frenzy" cut: 113 down to 102 words. |
| 352 · n | low | "ὄφελλεν … with an infinitive is a wish about the past": ὤφελον is the wish; ὄφελλεν says what should have happened. | "says what should have happened and did not, ‘ought to have’". |
| 355 · l, n | low | ἦ γάρ "for indeed" beside "for truly" at 342 in the same speech; iliad-001 78 and iliad-003 232 have "truly". | `l` and note "for truly". |
| 368 · n | low | note "chose out" for ἐκ … ἕλον; `l` and `i` "picked out". | "‘picked out’". |
| 380 (second unit) · n | low | "οἱ ‘to him’ is Apollo" without saying who the dear one is. | "the one who was dear is Chryses, and οἱ ‘to him’ is Apollo". |
| 382 · n | low | "ἀνὰ στρατὸν εὐρύν ‘up and down the wide army’" against `l` "through". | "‘through the wide army’ (ἀνά ‘up and down’)". |
| 384 · n | low | "ἑκάτοιο: ἕκατος is a short form …" never says ἑκάτοιο is the genitive. | "ἑκάτοιο the genitive of ἕκατος, a short form …". |
| 394 · l | low | "go to Olympus and beg": the Greek is a participle (ἐλθοῦσ’) beside an imperative; `l` should show it, as at 401. | "having gone to Olympus, beg Zeus,". |
| 407 · l, n | low | "Of these things now remind him": μνήσασα is an aorist participle (the note says so); note 118 words. | `l` "Of these things now having reminded him, sit beside him,"; note trimmed from 118 to 102 words ("beside παρέζεο"; the "at the sterns … salt-sea" repetition and the closing paraphrase cut). |
| 411 · n | low | 112 words; "The last half of the line, ὅ τ’ … ἔτισας" quoted the 244 form as if it were the line's own. | "The second half of the line is Achilles’ own at 244 (there ἔτισας, second person)"; trimmed from 112 to 103 words. |
| about · | low | "calls … to witness that if the Achaeans ever need him he will not be there to help them": the Greek leaves the threat unsaid (the note says so). | "to witness, should the Achaeans ever need him again to ward off ruin, a threat he leaves unfinished". |

## Changes: `gloss.json`

| form · field | severity | what was wrong | what was done |
|---|---|---|---|
| εὐξαμένου | high | "gen. absolute with τοῖο": it is not a genitive absolute; τοῖο is the object of ἤκουσεν (ἀκούω takes the genitive of the person heard) and the participle agrees with it (the unit note says so). | "agreeing with τοῖο, the genitive of the person heard". |
| τοῖο | high | "gen. absolute: ‘of him, as he’": same error. | "gen. of the person heard after ἀκούω: ‘him’". |
| κελόμην | high | "aor. 1 sg. mid." while giving "(= ἐκελόμην)", the imperfect; the form is the imperfect. | "impf. 1 sg. mid., unaugmented (= ἐκελόμην)". |
| ἑκάτοιο | medium | "far-shooting, far-darter" stated as fact; the unit note and row say the sense of ἕκατος alone is not certain; "far-shooting" is the English of ἑκηβόλος/ἑκατηβόλος. | "far-darter (epithet of Apollo, probably a short form of ἑκατηβόλος; sense not certain)". |
| ἤ | medium | "in ἤ τοι (= ἤτοι)": the unit reads τοι as σοι, so ἤ τοι is not ἤτοι. | "as printed in ἤ τοι, with τοι ‘to you’". |
| ὅτ | medium | "also ‘that’ after a verb of saying or boasting": ὅτ’ ἔφησθα is "when you said" (`l`, `i` and note); no use of ὅτε as "that" occurs. | Reduced to "ὅτε — when; conj., elided (ὅτ’)". |
| `__broaden__` λῆγ | medium | The known entry has only the imperative; 319 λῆγ’ is the imperfect 3 sg. (the unit note says so), a use the glosser did not add. | Added: old entry whole + " · also impf. 3 sg., unaugmented (= ἔληγε): ‘did cease’ (…)". |
| οἴη | low | Lemma "οἷος" ("such as") for οἶος "alone". | "οἶος — alone". |
| ἀπηνέος | low | "harsh, ungentle"; the Odyssey's house rendering is "unkind", and the origin is unknown. | "unkind, harsh (origin not known)". |
| πέρ | low | "accented after a paroxytone": τιμήν is oxytone; πέρ is accented because the enclitic μοι follows. | "accented before the enclitic μοι". |
| ᾗσιν | low | "(= Attic ᾗς)": no such Attic equivalent for a dative plural. | "epic ᾗσιν (= ἑῇσιν)". |
| ἐπαύρωνται | low | "have the benefit of, enjoy": biased to the good sense; the note says the verb is neutral and here bitter. | "get the result of, enjoy or suffer (+ gen.)". |
| ἐπασσύτεροι | low | Sense given without the uncertainty the note and row record. | "(traditional sense; formation unclear)". |
| `__broaden__` τώ | low | The known entry covers the demonstrative; 321 τώ οἱ ἔσαν κήρυκε is the dual relative use ("the two who"). | Added, old entry whole. |
| `__broaden__` τοῦ | low | 340 τοῦ βασιλῆος is "that king", with a noun; not covered. | Added, old entry whole. |

All other 262 novel entries, the 9 original broadenings and the 241 known forms (read against every line they occur in, for uses their entries do not cover) were checked and left unchanged. Format checks passed: every non-broadened entry under 230 characters, typographic ’ only, no backticks, no "here"; each new broadening keeps the old entry whole.

## new-renderings.md
- ὑγρὰ κέλευθα: row now names the whole line as Odyssey 15.474 (second half 4.842), with the line's English and the reason for "sailed".
- τὰ πένοντο: columns changed to "were busied" / "busied themselves", with the Odyssey precedent (4.624, 24.412).
- ἀπηνής: columns changed to "unkind", with the four Odyssey units named and "ungentle" listed as avoided.
- περίσχεο παιδὸς ἑῆος: marked "+ note" for the ἐΰς reading; "your good son" listed as avoided.
- βέλος: avoided column corrected (the Odyssey ships both "missile" and "arrow" for βέλος).
- Checked every other row against the units: all match.

## Checked and found correct (no change)
- `t`/packet identity; `ln` of every unit (including the 15 units that begin mid-line); `p` on exactly the six ¶ lines (312, 318, 326, 345, 357, 364); the five speeches (Agamemnon 322–325, Achilles 334–342, Achilles 352–356, Thetis 362–363, Achilles 365–412): `mark` on the first unit of each, “ on that unit and ” on the last in both `l` and `i`, no quotation marks elsewhere, `l` line division equals `t` line division in every unit. iliad-003's last unit (1.311) opens no speech and this part ends with the speech closed at 412, so the neighbouring boundaries are clean.
- Notes: all 59 within the 25–110 word band after the edits (longest 105).
- Packet-flagged lines: none. No metrical irregularity was found by hand in the lines whose notes discuss forms, so no note needed adding.
- Whole-line repeats from iliad-001 (372–375 = 1.13–16, 376–379 = 1.22–25) are exact in `l` and `i`; 361 matches the Odyssey formula in both layers; 355, 411 "wide-ruling" matches iliad-002 and Odyssey 11.248; 364 follows the reply-formula rows; "Greeks" is absent from both layers; Achaeans/Argives used consistently.
- Grammar labels checked in every note, including ἀπελυμαίνοντο/ἕρδον, λῆγ’ (imperfect, as against the imperative at 210), τώ, κήρυκε/ὀτρηρὼ θεράποντε, ἀγέμεν, δώῃσιν/ἕλωμαι, προΐει, βάτην/ἱκέσθην/στήτην, ἐρέοντο, ἔγνω, ᾗσιν, ἔρχεσθον/ἔστων, ἀπηνής, νοῆσαι, μαχέοιντο, ἐπεπείθεθ’, κίεν, λιασθείς, ὀρεγνύς, ὄφελλεν, ἠτίμησεν, εἴδομεν, ἤγομεν, διεπράθομεν, δάσσαντο, λυσόμενος, ἀφίει, τοῖο/εὐξαμένου, ἦεν, θνῇσκον, ἐπῴχετο, κελόμην, Ἀτρεΐωνα, τετελεσμένος (the loose agreement is a real feature of the transmitted line), περίσχεο, ἐλθοῦσ’, ὤνησας, ἔφησθα, οἴη, ξυνδῆσαι, ὑπελύσαο, ὦχ’, οὗ, ὑπέδεισαν, ἔδησαν, ἐπαύρωνται, γνῷ. Line-position claims (210, 244, 316, 321, 323, 326, 327, 333, 338, 353, 355, 356, 358, 374, 379, 398) and the "next line/unit" statements at 312, 331, 335 all true.

## Considered and refused
- **ἑκατηβόλου (370) and ἑκηβόλου (373) both "far-shooting" in `l`**: kept. Two Greek epithets with one English is a collision only on paper: the Odyssey fixes "far-shooting" / "who shoots from afar" for ἑκατηβόλος (8.339, 20.278) and iliad-001 fixes "far-shooting" in both layers for ἑκηβόλος; `i` tells them apart ("who shoots from afar" vs "far-shooting"), and the row records it.
- **ἑκάτοιο "of the far-darter" (385)**: kept. "far-darter" is the noun-form of the table's ἑκατηβελέτης "far-darting" (the family the note names), the sense is flagged uncertain in the note and gloss, and the Odyssey has no ἑκάτοιο to follow.
- **ἀπηνής "unkind" for a king, not "harsh"**: "harsh" is reserved for χαλεπός and ἀταρτηροῖς here; "unkind" is the Odyssey's.
- **ἑλίκωπες "quick-eyed" (389)**: kept as the masculine of the table's ἑλικῶπις; note and gloss say the sense is disputed.
- **ὀλοιῇσι φρεσὶ θύει (342)**: "in baleful wits, rages" / "rages with a baleful mind" kept: ὀλοός keeps "baleful" (table, ὀλοόφρων), θύω "rage/seethe" (table, θῦεν "seethed"). No change; the form is dative plural of ὀλοός/ὀλοιός.
- **κνίση "savour" (317)**: kept, as iliad-001 ships "savour" for κνίσης at 1.66; the Odyssey table's "smell of fat" is for a different context and the row says so.
- **λύματα "the filth" (314)**: kept; LSJ "that which is washed off", and the note says what it is.
- **ἐπασσύτεροι "one close upon another" (383)**: kept; the traditional sense, flagged in note, row and now the gloss.
- **ἤ τοι (365) read as ἦ + σοι**: kept: ἰδυίῃ is dative and needs a dative to agree with; the note now states both halves.
- **οὐδ’ ἔτ’ ἔδησαν (406) with "Zeus" supplied in `i`**: kept: the standard reading, the object is the μιν of 399; the note says the Greek has no object and the row records it; `l` leaves it unsupplied.
- **στρατός "army" (318, 382) against iliad-003 229 "wide host"**: kept: iliad-001 ships "army" for ἀνὰ στρατόν (1.10, 1.53), the same preposition as 382, and 318 is a different phrase; the Iliad already uses both words.
- **αἰδομένω "in awe of" (331)** against the Odyssey table's αἰδέομαι "revere/show respect": kept; the participle here is paired with ταρβήσαντε and the sense is awe before a king; αἰδεῖσθαι at 377 keeps "respect" (identical to iliad-001).
- **ἦ γάρ "for indeed" in iliad-003 293 against "for truly" elsewhere**: not touched in this part beyond conforming 355 to 342.
- **ἄτη "bewilderment" (412)**: kept; the Odyssey ships "bewilderment" at 21.302 and 23.223 (and "ruin", "blindness" in other uses), so the row's claim stands.
- **`i` omits οὖν-type particles (νυ at 382, δέ at several places, γε at 352)**: kept; particle force carried by word order and rhythm.
- **"salt sea" (`i` 409) against "the sea" (`i` 314, 316)**: kept; ἅλς is "salt-sea" in `l` throughout and the Odyssey's `i` uses both.
- **Glossary "Greeks" in the Ἀχαιοί/Ἀργεῖοι entries**: kept; the avoidance applies to the translation layers.
- **τιμήν, Βριάρεων glosses with an "Attic" form identical to the epic one**: harmless, not changed.
