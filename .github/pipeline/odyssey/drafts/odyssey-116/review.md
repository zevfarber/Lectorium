# odyssey-116 (24.106–213) — review, pass 1

Unit numbers below are the unit's `ln`. `t`, `tr` and `sc` were not touched (checked by script: every `t` is unchanged, and the concatenated `t` equals the packet's lines word for word; the unit `ln` values and the `p: true` units 106, 131, 138, 147, 191, 203, 205 all agree with the packet's paragraph marks). Severity: major = a false statement of grammar or sense, or a note contradicting its own `l`/`i`; minor = faithfulness, house-table or consistency slip; nit = wording.

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 111 · n | major | Said that the accusative participles περιταμνομένους and μαχεούμενοι both agree with the understood ‘you’. μαχεούμενοι is nominative plural. | Now: περιταμνομένους is the accusative agreeing with ‘you’; μαχεούμενοι is nominative, cannot agree with it, and the Greek does not say whose fighting is meant. |
| 138 · n | major | ἐπεπείθετο was called “built on the perfect stem of πείθω”. It is the augmented imperfect of ἐπιπείθομαι (ἐπι- + ε- + πείθετο), as the shipped note at odyssey-057 has it. | Rewritten to the imperfect of ἐπιπείθομαι, augment after the preverb, not a perfect. |
| 138 · n | nit | “ἡμῖν is ‘our’” left the case unnamed. | Now “a dative of interest, ‘to us’, so ‘our’”, as odyssey-057. |
| 172 · n | major | “τόξον μὴ δόμεναι is an infinitive used as a command” mislabels it: it depends on ὁμοκλέομεν (indirect command). | Relabelled as the infinitive of an indirect command after ὁμοκλέομεν. |
| 172 · l, i, n | major | The note said neither giver nor receiver is named, but `l` read “not to give him” and `i` “they must not give him the bow”, supplying both. | `l` now “the bow not to give, not even if…”; `i` now “that the bow must not be given, no matter how much he said”; the note says the English turns it passive. |
| 176 · n | major | ἐτάνυσσε called an imperfect of τανύω; it is the aorist (ἐτάνυσσε, σσ). | Changed to aorist. |
| 205 · n | major | κατέβαν called “unaugmented”; it carries the augment (κατ-έ-βαν). | Now “the athematic aorist, with the augment, for κατέβησαν”. |
| 167 · n | minor | ἄνωγε called “the imperfect of the old perfect ἄνωγα”, which is not a category (a perfect has no imperfect; the pluperfect is ἠνώγει). | Now the unaugmented imperfect of ἀνώγω, the verb that also has the perfect ἄνωγα ‘I bid’. |
| 107 · i, n | minor | “could a man have picked out” put a past counterfactual on a κεν + aorist optative (potential, no past time), and dropped the participle’s force. | `i` now “Nor could a man, choosing in any other way, pick out the best men throughout the city.”; the note says the participle carries the condition ‘if he were choosing’. |
| 109 · i | minor | “among your ships” for ἐν νήεσσι suggests a fleet round them; the Greek is ‘in (the) ships’. | “in your ships”. |
| 208 · n | minor | Called κλίσιον “an outbuilding or lean-to”, which fixes a structure; the table and new-renderings row say the structure is not known and avoid both words. | Note now says the structure is not known and ‘shed’ is a working guess. |
| 211 · i | minor | κομέεσκεν is iterative (the note says so), `l` has “used to tend”, but `i` had plain “looked after”; the house table keeps -εσκ- as “used to” (ἰαύεσκον) and unit 208 does so. | “who kindly used to look after the old man”. |
| 196 · i | nit | The table row ἐπιχθόνιος ἄνθρωποι gives `i` “men who live on the earth”; the unit had “men on earth”. | “for men who live on the earth”. |
| 196 · n | nit | Glossed χαρίεσσαν “graceful, charming”; “charming” is on the avoided list in new-renderings. | “graceful” only. |
| 199 · n | nit | Said the subject of ὀπάσσει is song or woman, undecided, while `l` and `i` both say “it” after “song”. | Added that the English takes it to be the song. |
| 203 · n | nit | ἑσταότ’ “elided” without saying from what; the two speakers are two. | Added “most naturally from the dual ἑσταότε for the two speakers”. |
| 146 · l | nit | Greek ends in a full stop (the unit’s `t` has “.”, not the published ·), but `l` ended in a semicolon, carried over from the published unit. Wording is the published wording. | Final semicolon changed to a full stop; wording unchanged. |
| 106 · n | nit | Glossed ὁμήλικες “of the same age”, a phrase the table row (ὁμήλιξ “of an age with”) puts on its avoided list. | “of an age with one another”. |

## Checks that found nothing

- Scansion: packet flags none. Run through scan_hexameter.py anyway: no line flagged or UNRESOLVED; only ordinary licences (correption, lengthening before μ at 129/147/162/187, spondaic fifth at 128/151/153/189/210). No irregularity note added. 164 (νοός printed with final acute) scans without a licence; the note already mentions the accent.
- Repeated-line units whose whole `t` equals a published unit (129, 131, 138, 139, 141): `l` and `i` identical to the published, checked by script. Partial repeats (121, 134–137, 142–145, 146, 157, 168–169, 202, 203): the `l` lines reuse the published wording line for line; `i` reuses the published phrases as the sentence allows.
- Quotation marks: “ on first unit of Agamemnon’s speech (106), ” on 118/119; “ on 121, ” on 188–190; ‘ on 131, ’ on 134–137 (Penelope inside Amphimedon, single marks as odyssey-115 does for Nestor); “ on 192, ” on 199–202; no mark opened at 213 (speech is in the next part). `mark` field present exactly on 106, 121, 131, 192. Same pattern as 115 (“X speaks”/“X answers”). `l` and `i` agree on every mark, and line counts of `t` and `l` agree on every unit.
- Cross-references and position claims (checked against the lines): σσ/σ spelling of Ὀδυσ(σ)ῆος at 125 vs 195; “end of line 145/158”; “middle of line 130/181/195/196”; “seven lines” (131–137); “more than six lines” (196–202); “διοτρεφές in the second line” (122); “ἀθάνατοι set after the object” (197/198); θεῖος vs δῖος at 151. All true.
- New-renderings choices (all 20 rows): consistent with the house table and with the units; “the dusky earth”, “good wits/good sense”, “Prosperous son of Laertes… man of many devices”, “Sicel woman, an old one”, “bound servants”, “worked kindly/with a good will”, “arrows full of groaning”, “dark gore”, “harsh talk”, “fine, well-wrought” all as in the table. No remembered modern-translation phrasing found in `i`.

## Considered and refused

- 114 · n “εἰρομένῳ is the present participle of ἔρομαι”: the form is the epic present εἴρομαι (LSJ lists it under ἔρομαι); the label is true as written.
- 141 · n “τρίετες an adverbial accusative”: LSJ lists it as an adverb ‘for three years’; accusative is the usual reading; left.
- 159–161 · l/i “we rebuked / abused” for the imperfect ἐνίσσομεν: simple past is acceptable English for a descriptive imperfect, and 162 renders the participle consistently; no change.
- 147–150 · l “dwelt in his house” for δώματα ναῖε: “his” is supplied but natural, and plural δώματα for one house is the usual idiom; no table row requires otherwise.
- 147 · i “shining like the sun or the moon”: “shining” is supplied beside ἐναλίγκιον ‘like’; it is the sense of the comparison and costs nothing; left.
- 118 · i “only with difficulty”: “only” is slight emphasis on σπουδῇ; left.
- 192–193 · i “a wife of great excellence” for σὺν μεγάλῃ ἀρετῇ ἐκτήσω ἄκοιτιν: `l` keeps “with great excellence you acquired”; the note says the excellence is Penelope’s, and both readings are ancient. Left, as the note states the choice.
- 213 · l “to his son” (no possessive in the Greek): idiomatic, and `l` elsewhere adds such possessives.
- 138 · l/i vs 24.138 published (“our own proud hearts”, plural for singular θυμός): enforced by the repetition rule; kept as published.
- 146 · l “So that she finished”: reads like a purpose clause but is the published wording; wording kept, only the stop changed.
- 106, 131 `p`/`mark` placement and the cut at 133/134 comma: allowed by the four-line rule (sentence is seven lines).
- 183 · l/i “following their own strength”: the table’s μένεϊ σφῷ is not a row, but the note explains σφῷ as ‘their own’; no change.

## Counts

Changes: 18 table entries (major 6, minor 5, nit 7) across 16 units. Findings refused: 12.

---

# Pass 2

Redone from the top on the current `units.json` (including pass 1's edits) and on `gloss.json`: note labels against the line, Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks; then every novel-form parse and every `__broaden__` entry against each line the form occurs in, and (beyond the brief) the known-forms entries that the part leans on, for coverage. No modern translation opened or recalled. `t` untouched (checked by script: the list of `t` strings is identical before and after); JSON re-dumped in the original layout (indent 1, no trailing newline; a round-trip test passed before editing). Same severity scale as pass 1; a gloss entry that states a false parse or a false Attic equivalent is major.

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| gloss μαχεούμενοι | major | Gave the Attic equivalent as μαχούμενοι, which is the future participle of μάχομαι. The form is the epic present participle (μαχεόμενοι lengthened), Attic μαχόμενοι, as the note at 111 already says. | “= Attic μαχόμενοι”. |
| gloss νοός (164) | major | Parsed as “masc. gen. sg. (= Attic νοῦ)”. In Διὸς νοός αἰγιόχοιο the word is the subject of ἔγειρε, the nominative νόος printed with the acute on the ending, as the note at 164 says; a genitive makes no sense of the clause. | Now “masc. nom. sg., uncontracted (= Attic νοῦς); the edition puts the accent on the ending (νοός)”. |
| 167 · n | minor | Pass 1's “unaugmented imperfect of ἀνώγω” contradicted the shipped glossary entry for ἄνωγε (perfect of ἄνωγα with present/past force, ‘bade, had bidden’). | Now “the third singular of the old perfect ἄνωγα ‘I bid’, which Homer also uses with past force (the pluperfect is ἠνώγει)”. Pass 1's point (a perfect has no imperfect) is kept. |
| 183 · n | minor | Note read μένεϊ σφῷ as “with their own strength” (instrumental), but `l` and `i` both say “following their own strength”, and the shipped glossary entry for μένεϊ makes it the object of ἐπισπόμενοι. | Note now takes it as a dative object of the participle (ἕπομαι takes the dative), matching `l`, `i` and the glossary, and names the instrumental reading as the other possibility. |
| gloss κλίσιον | minor | “shed, outbuilding (exact formation unknown…)”: “outbuilding” is on the avoided list in new-renderings and the note at 208, and the thing not known is the structure, not the formation. | “shed (a working guess; the exact structure is not known; from the root of κλίνω ’lean’)”. |
| gloss πολυκερδείῃσιν | minor | Meaning “much gain, cunning” and gloss “by cunning wiles”: new-renderings reserves “cunning” and “wiles” for μῆτις / πολύμητις and fixes “by many-gainful ways”. | “alertness to gain, shrewdness (cf. πολυκερδής ’many-gained’) … ’by many-gainful ways’”. |
| gloss ἀμύμονι | minor | “blameless, noble”: “noble” is on the table's avoided list for ἀμύμων, and the conventions require a word of unknown meaning to say so. | “blameless (the real sense is not known)”. |
| 167 · n | nit | “‘shrewd calculation’ is what the context gives” introduced a third English for πολυκερδείῃσιν beside the fixed `l` and `i`. | Now names the idiomatic layer: ‘with his alertness to every advantage’. |
| 106 · n | nit | Glossed ὁμήλικες “of an age with one another” while `l`/`i` say “of one age”. | Note keeps the table's phrase and says it is put as ‘of one age’ because no word follows to be ‘with’. |
| 107 · n | nit | “no selection made any other way could have found better men” put a past counterfactual on the potential optative again. | “could find”. |
| 118 · n | nit | “Agamemnon’s speech ends with this line”; the unit is two lines and the speech ends at 119. | “ends with the second line of this unit, line 119”. |
| 194 · n | nit | Called ἀμύμονι Πηνελοπείῃ a dative of possession but glossed it only as “in blameless Penelope”. | Now ‘blameless Penelope had’, which the English puts as ‘in blameless Penelope’. |
| 211 · n | nit | “ἐν δέ is ‘and in (it)’, the house” states as fact an antecedent the Greek does not give (the nearest is ἐν τῷ, the κλίσιον). | “most naturally the house”. |
| gloss ἐρεμνὴν | nit | “dark, dusky”: “dark” is reserved for μέλας. | “dusky (not μέλας ’dark’)”. |
| gloss ὁμήλικες | nit | “of the same age” is on the table's avoided list for ὁμήλιξ. | “of an age with, age-mate”. |
| gloss περιταμνομένους | nit | ‘cutting off, rustling’: “rustling” is a modern idiom and not what `l`, `i` or the note say. | ‘cutting off’. |
| gloss ἔδυτε | nit | “(= ἔδυτε)” gives the form as its own Attic equivalent. | “(same in Attic)”. |
| gloss ἐφίει | nit | “iterative sense” pinned the entry to the line's context; the form is a plain imperfect. | “impf. 3 sg.: ’was sending at, kept sending’”. |
| `__broaden__` πηνελοπείῃ (198) | nit | The four readings did not cover ἐχέφρονι Πηνελοπείῃ after τεύξουσι (dative of advantage, ‘for’). | Appended “ · also dat. sg. of advantage: ’for (sound-minded) Penelope’ (ἐχέφρονι Πηνελοπείῃ)”; old entry kept whole. |

## Checks that found nothing

- Labels in every note re-checked against the line (case, tense, voice, lemma, position and cross-reference claims, line-range claims, “ano teleia ends the unit” at every unit boundary); all other labels true. `l` has the same number of lines as `t` in every unit; no `\n` in any `i`; no ASCII quote, apostrophe or backtick in `l`, `i`, `n` or `gloss.json`.
- Quotation marks: “ on 106, 121, 192; ” on 118, 188, 199; ‘ on 131 and ’ on 134; `l` and `i` agree on every mark; `mark` on 106, 121, 131, 192 only; `p: true` on 106, 131, 138, 147, 191, 203, 205, matching the packet.
- Repeated lines: 129, 131, 138, 139, 141 whole-unit repeats identical to the published `l`/`i` (script); partial repeats reuse the published wording.
- `gloss.json`: keys equal `novel-forms.json` exactly (81); every entry is under 230 characters, uses only the typographic ’, carries no line number and no “here”; every `__broaden__` entry begins with the whole old entry from `known-forms.json`, and the added reading is true of the line it cites (δόμεναι 173–174, κέν 134, κακοῖσιν 161, κακός 149, κακὸν 124, κοῦροι 131, πηνελοπείῃ 194, ἐναλίγκιον 148, ἐτελέσθη 143, ὃ 190, ἑσταότ’ 204).
- Parse of every other novel form checked and left (βέλεα, βαλλόμενος, βιοῖο, βολῇσιν, βρότον, γνωτὸν, γοάοιεν, θέε, θανόντων, κατέβαν, κατθέμενοι, κεύθεσι, κομέεσκεν, κουριδίου, κτεάτισσεν, κτείνασα, κτεῖνον, λέξαιτο, μέλανα, μέμνημαι/μέμνητ’/μέμνῃ, μηνὶ, μνώμεθ’, οὔλῳ, πάϊ, παρπεπιθόντες, περήσαμεν, πλύνασ’, πολλ’ (only the unaccented adverbial πολλ’ at 174 is a novel key; the accented πόλλ’ at 143 and 207 are known forms), προγενέστεροι, προφανέντ’, σελήνῃ, σικελὴ, σιτέσκοντο, σώματ’, φραζομένη, χαλεπὴν, ἀγαθαὶ, ἀγορεύοι, ἀμφίμεδον/ἀμφιμέδοντος, ἀναγκαῖοι, ἀοιδὴ, ἀπονίψαντες, ἀργαλέους, ἀρτύναντε, ἐκτήσω, ἐνίσσομεν, ἐνισσόμενος, ἐπιτάρροθος, ἐργάζοντο, ἐτελεύτα, ἐτόλμα, ἐϋσσέλμων, ἑοῖσι, ἔπεσίν, ἔσσετ’, ἠρνεῖτο, ἡμείων, ἦμεν, ἵζανον, ὀλεῖται, ὀπάσσει, ὀτρυνέων, ὁμοκλέομεν, ὑμέτερον, ὑφήνασα, ὕστερος, ὠτειλέων).
- Known-forms entries for the forms of this part read for coverage (about 230 forms): every use here is covered or was already broadened (κεν 107, 137; κε 132; κ’ 189, 202; ὅ 182; τὰ 158; τὸν 159; περί 113, 143, 158, 208; οἱ 196, 203, 208; ἧς 197; ὧν 187; πολλὰ 134 all fit an existing reading). No further `__broaden__` entry needed.
- New-renderings rows (20) re-checked against the units; consistent after the gloss fixes above.
- Scansion: packet flags none; no change.

## Considered and refused

- 138 · l/i “lordly heart” / “proud hearts” against the later table row θυμὸς ἀγήνωρ (4.548) “manly spirit” / “proud spirit”, which says only this epithet keeps “spirit”: the unit repeats a published unit (odyssey-006, 2.103) and the validator requires identical wording; the note describes the shipped wording truly. The conflict between the shipped part and the later table row is real and is for a human decision (a QUESTIONS.md item), not for this part.
- gloss ἐκλήϊσεν lemma “κλήϊζω (κλῄω)”: I could not settle from memory whether LSJ files the form under κληΐω or κληΐζω; the parse (aor. 3 sg.), the meaning and the Attic equivalent are right; left.
- 175 · n “Telemachus alone took the other side”: an inference, but plain from 172–174 where the suitors shout the opposite; left.
- 196 · i “in honour of sound-minded Penelope” for the dative ἐχέφρονι Πηνελοπείῃ: `l` keeps “for”, the note names the dative of advantage; “in honour of” is the idiomatic reading of a song made for someone; left.
- 126 · i “the marriage she hated” for στυγερὸν γάμον: assigns the hatred to Penelope, which the context supports; `l` keeps “hateful”; left.
- 151 · i “in his black ship” (σὺν νηῒ μελαίνῃ): “his” is supplied but natural; left.
- 115 · i “on the well-benched ships” beside `l` “on well-benched ships”: article added in the idiomatic layer only; left.
- 142–145 · l/i “the seasons passed by / had passed” for ἐπήλυθον (‘came on’): published wording, enforced by the repetition rule.
- 176 · l “sent an arrow through the iron”: the object is supplied in both layers and the note says so; left.
- 161 · i “insulting words” beside `l` “evil words” (κακοῖσιν): idiomatic layer, same sense; left.
- 111 · i “driving off cattle” beside `l` “cutting off cattle”: the note says the verb is a raider's word for driving off a herd; left.
- 203–204 · l “houses of Hades”, i “halls of Hades”: the layers may differ; no table row for δόμοις of Hades; left.
- 106 · l/i “of one age” for ὁμήλικες: the table row is for ὁμήλιξ governing a dative (“of an age with”); with nothing to govern, “of one age” is not on the avoided list; the note now says why.
- 139 · n “ἀλλύω … the same word as ἀναλύω”: agrees with the shipped glossary entry for ἀλλύεσκεν; left.

## Counts (pass 2)

Changes: 19 table entries (major 2, minor 5, nit 12): 8 in `units.json` notes (across 7 units), 11 in `gloss.json`. Findings refused: 14.
