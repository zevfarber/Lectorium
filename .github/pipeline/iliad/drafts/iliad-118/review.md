# iliad-118 review (Iliad 18.202–309), pass 1 (units) and pass 2

Method: both passes read every unit against the Greek of `t` (checked against the pinned source: the units reproduce lines 202–309 exactly), the packet, `conventions.md` and the Odyssey table, the published parts named in notes (iliad-008, -044, -050, -051, -074, -117), and the gate logic of `validate_iliad.py`. `t`, `ln`, `p`, `mark`, titles and `about` were not touched. Cross-references verified true: 8.425 (iliad-050), 7.326 (iliad-044, line 326), 12.230 (iliad-074), 2.139 (iliad-008), 8.530–531 (iliad-051, unit at 529), 7.370–371 (iliad-044, unit at 370), 18.100 and 18.198 (iliad-117), and the in-part references (203, 206, 214, 271, 278, 286, 287, 306). Speech continuity: Iris’s speech closes with ” at 18.201 in iliad-117, so this part opens outside a speech; Polydamas 254–283 and Hector 285–309 are marked on their first units and closed on their last.

## Changes (line · field · severity · what was wrong · what done)

| line | field | severity | what was wrong | what done |
|---|---|---|---|---|
| 296 (second unit, οὐ γὰρ ἐάσω) | l, i | high | Same Greek as the published unit at iliad-112 line 449, whose English is "for I will not allow it."; the draft had "shall". `validate_iliad.py` step 6 fails on any difference | l and i set to "for I will not allow it." |
| 297 | l, i, n | high | Same Greek as iliad-008 line 139 (also 052, 057, 072, 089, odyssey-063); the draft ended l and i with "." where the published English ends ";". Step 6 of the validator requires exactly the published l and i, so the part would fail the gate. The note said only "a different stop" | l and i set to the published "…all of us;" and "…as I say;". Note now says the edition here prints a comma after εἴπω and a full stop, where 2.139 has none and a raised point. (`new-renderings.md` still says the final stop is "."; that sentence is out of date) |
| 214 | l, i, n | medium | σέλας rendered "flash"; the table has σέλας "blaze" (8.509, 17.739) and keeps "flash" for the thunderbolt-flash of 8.75 | "blaze" in l, i and the note |
| 233 | l, i, n | medium | μυρόμενοι rendered "lamenting"; the table has μυρομένη "mourning" (6.373) and keeps "lamenting" for γόος. The `new-renderings.md` row claiming "mourning" was avoided is wrong | "mourning" in l, i and the note. The `new-renderings.md` row for ἑταῖροι … μυρόμενοι should be dropped (it is a table row, not a new one) |
| 249 | i, n | medium | Whole-line-style speech introduction with ἦρχ’ ἀγορεύειν; the table’s i is "was the first to speak among them" (1.571, 22.461), and the note itself says it follows that pattern; i had "began to speak" | i: "And prudent Polydamas, son of Panthous, was the first to speak among them;" ; note gloss changed to match |
| 218 | i | medium | ὦρσε (ὄρνυμι) rendered "stirred up"; the table has ἐν … ὦρσεν "roused in" and turns "stirred" down; "stirred up" is the l of ὀρίνθη | "she roused a boundless uproar among the Trojans" |
| 207 | i, n | medium | i put "men who fight it out … from their own town" in apposition to "enemies", which says the besiegers fight from the town; the Greek relative οἵ τε is the men of the besieged town. The note did not say who | i: "…an island that enemies are fighting around, while its men fight it out all day long in hateful war from their own town"; note adds that οἵ τε is a change of subject to the besieged |
| 239 | n | medium | "as the next line says" attached to "the streams of Oceanus are where the sun goes down"; the next line (241) says only that the sun set | "so the sun sets, as the next line says" |
| 267 | n | medium | "the sentence puts the night after the verb": νύξ stands before ἀπέπαυσε; it is ἀμβροσίη that is held back after the verb, in the next line | note now says the word is held back to the start of the second line, after νύξ and the verb |
| 247 | l, i, n | low | ἔχε τρόμος: the table (10.25) has l "a trembling held", i "took hold of" | l "for a trembling held them all"; i "for a trembling took hold of them all"; note explains the two renderings |
| 273 | l, i | low | κηδόμενοί περ rendered "anxious as we are"; "anxious" is in no table row (1.586 and 5.382 "worried as you are"; κήδομαι "be troubled") | l "troubled though we are", i "worried as we are" (note already read ‘though we are troubled’) |
| 300 | l, n | low | ὑπερφιάλως rendered "excessively" in l; the table (Odyssey 17.481, Iliad 13.293) has "beyond measure". Note said ‘to eat up among the people’ while l said "in common" | l "distressed beyond measure"; note: ‘to eat up in common, among the people’ |
| 270 | i | low | γάρ left out of i ("whoever escapes will gladly reach…"); it gives the reason for the threat before it | "for whoever escapes will gladly reach sacred Ilium…" |
| 202 | n | low | ‘rose up, sprang up’ for ὦρτο; the table (7.162) turns "sprang up" down | ‘rose up’ |
| 230 | n | low | ἔγχεσιν called an epic dative plural; it is the ordinary dative plural (only ὀχέεσσι is epic) | note corrected |
| 280 | n | low | εἶσι called "the future of εἶμι"; it is the present used as a future | note corrected |

Counts: high 2, medium 7, low 7 (16 findings, 16 changes).

## Findings considered and refused

- ἄρεω ἀλκτῆρες (213), "ruin": the note states the other reading (Ἄρης "war"), l and i follow ἀρῆς ἀλκτῆρα at 18.100 and the table’s "a warder-off / a defence against" for the noun. Kept.
- ἀπ’ οὔατος (272): l "away from my ear", i "far from my hearing", and the note says the force of ὧδε is uncertain. The idiom is not a house phrase; kept.
- καταδημοβορῆσαι (301): parts named and the uncertainty said; l "in common" and i "eat up" are consistent with the note after the small wording fix above.
- λεχέεσσι "bed" (233) and φέρτρῳ "bier" (236): the note says both name the one bier; λέχος is "bed" in the table (1.609, 9.621). Kept.
- ὑπέρβιος "exceeding" (262): follows the Odyssey table (16.410) and the Iliad row for ὑπέρβιον (17.19). Kept, although the English is stiff.
- ὄχεσφιν "chariot" (237): the table (5.219) has "with horses and chariot" for a single car, as here. Kept.
- ἐκπληγεν "-εν for -ησαν", ἀμφέσταν "-αν for -ησαν": standard glosses for the epic endings; kept.
- ἴαχε "unaugmented aorist" (228): true of the form (its first syllable is a reduplication, not an augment); kept.
- "had kindled" for δαῖε (227), i only: a back-reference to 206, defensible; kept.
- ἠελίῳ καταδύντι (210), i "when the sun has set" without ἅμα: the table and new-renderings row agree on the rendering; kept.
- Notes at 266b (17 words) and 296b (15 words) fall under the 25-word band: the validator only warns, both are one-clause units whose notes say all that is needed. Left.
- 297 final stop: the pinned source prints a full stop and a comma after εἴπω; `t` cannot be touched and I have no evidence that the edition differs, so rule 5 was not applied. If the owner prefers the edition’s raised point the source must be corrected and the part re-pinned; as it stands the English now equals the published unit and passes step 6.
- Scansion flags: none in the packet, so nothing was scanned by hand and no metrical sentence was added.
- Pass 2 (after the edits): re-read all 65 units for case relations, tense and mood against `l`, `l` against `i`, remembered English and quotation marks; found nothing further. Marks: “ on 254 and 285 (with `mark`), ” on 283 and 309; no stray quotes elsewhere; ’ only; no backticks; the file loads (65 units), `t` unchanged, same-Greek units 253, 284, 296b and 297 now equal the published English.

## Glossary (pass 2)

Every novel entry in `gloss.json` was checked against its use in `units.json`, and the six `__broaden__` entries against the old text in `known-forms.json` and the lines where they occur. All entries are under 230 characters, use ’ only, and carry no line numbers or "here". The six broadened entries each start with the old entry whole, then " · " and the new reading; each new reading is true of the form in its line (αὐτοῦ 203 neuter "from it"; τῇς 273; χάλκεον 222 ὄπα; γυναικῶν 262; ναῦφιν 305; πολύχαλκον 288). No change was made to them.

| form | severity | what | done |
|---|---|---|---|
| ἄρεω | medium | entry took one reading as certain and said "not the god Ἄρης", against the note at 210, which leaves both open and follows "ruin"; it also called ἀρή masculine and gave no Attic form | two readings joined by " · ": ἀρή/ἄρης "bane, ruin" (= Attic ἀρῆς) and Ἄρης "war" (= Attic Ἄρεως); "ruin" first, matching 213 |
| ὑπέρβιος | medium | "overweening, violent, arrogant": "overweening" is the house word for ὑπερφίαλος, and the English at 262 is "exceeding" (table: ὑπέρβιος "exceeding") | "exceeding, excessive, of violent strength" |
| ἀλκτῆρες | medium | "defender" is declined in the table for ἀλκτήρ ("a warder-off" / "a defence against"); i has "a defence against" | "warder-off, defence" |
| ἄλγιον | medium | lemma ἀλγεινός with "comparative ἄλγιον, epic" gave no Attic equivalent and added "worse", which is not in i ("the more painful") | comparative ἀλγίων, neut. ἄλγιον, Attic ἀλγεινότερον; meaning "more painful" |
| ὄσσοντο | low | parse true; meaning "forebode" only, while i at 224 is "foresaw" and the note says "see in the mind, foresee" | "see in the mind, foresee, forebode"; "foresaw, foreboded" |
| κεκόρησθε | low | epic κεκόρημαι named, Attic perfect not | added Attic κεκόρεσμαι |
| ῥηΐτεροι | medium | no case/number parse at all, and no Attic equivalent | "masc. nom. pl.", Attic ῥᾴων |
| μίσγετο | low | unaugmented epic form, no Attic equivalent | added unaugmented, Attic ἐμίγνυτο |
| τρόπεον | low | no Attic equivalent | added Attic ἐτρόπουν |
| πτόλιός | low | epic genitive -ιος, no Attic equivalent | added Attic πόλεως |
| κηδόμενοί | low | "anxious, troubled" against i "worried" and the table (1.586 "worried as you are") | "worried, troubled" |
| κρίνονται | low | quoted sense "contend" only; i at 207 is "fight it out" | "are decided, fight it out" |
| πιθώμεθα | low | i has "we are persuaded" | added "be persuaded" |
| μέροπες | low | quoted sense order and i ("articulate speech"): table row has "speech-dividing" first | "speech-dividing" first, "mortal" second |

### Glossary findings considered and refused
- μυθέσκοντο, χαίρεσκον: iterative -σκ- imperfects have no Attic counterpart; the entries already say "unaugmented, iterative" and give the sense. Kept.
- ἀμφιμάχωνται "general relative clause without ἄν or κε": true of the form in its relative clause (207); kept.
- καταδημοβορῆσαι ’to devour publicly’ against i "to eat up": same sense, rare compound said to be rare; kept.
- περιπλομένων "aor. part.": correct (thematic aor. of πέλομαι). ἀργοὶ "swift or white": the uncertainty is real; i has "swift". Kept.
- χαίρεσκον 1 sg. (also 3 pl. in form) and τρόπεον 3 pl. (also 1 sg. in form): the pronoun ἔγωγε and the plural subject fix them; kept as parsed.
- Known forms outside the six `__broaden__` entries were not re-audited beyond these six.
