# Review of odyssey-042 (Odyssey 9.281–370)

Reviewer: adversarial, two passes, runbook order (labels in notes; Greek → `l` word by word; `l` ↔ `i`; remembered English; quotation marks; hand-scan of the flagged line). `t` untouched (checked by script: every `t` identical before and after; the tiling and `p`/`ln` checks of `build_odyssey.py` also run clean on the edited file, without writing anything). Sources used: Murray's Greek, `conventions.md` and its table, the neighbouring part odyssey-041, and from memory only LSJ, Autenrieth, Cunliffe, Monro, Smyth. No modern translation opened or recalled. `gloss.json` not touched and not checked (a later pass does that).

Severity: high = wrong sense or a false claim that would mislead; medium = a label or rendering that is untrue or off in force; low = wording, consistency, tidy-up.

Totals: **high 0 · medium 6 · low 19** (pass 1: 25 changes; pass 2, a fresh full re-read of every `t`/`l`/`i` after the edits: no further change needed).

## Changes made to units.json (unit numbers count from 0; line = the unit's `ln`)

| line (unit) | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| about | about | medium | Said the Cyclops, "in return for a guest-gift, demands Odysseus' name"; the Greek has him promise a guest-gift and ask the name (9.355–356), so the exchange was inverted. | Now: "…then, promising a guest-gift, he asks Odysseus' name." |
| about | about | low | "asks for a second and a third": the Cyclops asks once (δεύτερον, 9.354); Odysseus gives three times (9.361). | "asks for a second cup, and Odysseus gives him three". |
| about | about | low | "as he lies full and asleep": this part says only that he lay stretched out (9.298); sleep is not stated. | "as he lies stretched out, full of his meal". |
| 283 (1) | i | low | "the wind carried it": the Greek has no article; `l` has "a wind". | "a wind carried it in from the sea". |
| 283 (1) | n | low | 157 words, over the validator's band. | Trimmed to about 130; nothing of substance dropped. |
| 287 (2) | i | medium | "he dashed them against the ground": κόπτε is 'struck'; "dashed" is a stronger verb than `l` ("struck them") and a phrase that arrives ready-made. | "he struck them against the ground like puppies". |
| 291 (4) | i | low | "limb from limb" (a set phrase) against `l` "limb by limb" (μελεϊστί). | "limb by limb". |
| 294 (6) | n | medium | Called ἀνεσχέθομεν "the aorist middle of ἀνέχω". The ending -ομεν is active; the form is an epic past tense built on σχεθ- (by-form of ἔχω), not a middle. | Note now says: 'we held up', an epic past tense of ἀνέχω built on the stem σχεθ-, with active endings. |
| 310 (14) | n | low | Called τά "the article-pronoun strengthening" the possessive; here it is the plain article before τὰ ἃ ἔργα, and "pronoun" is the wrong label in this line. | "τά before it is the plain article." |
| 312 (15) | l | low | δέ in δειπνήσας δ’ dropped from `l` ("Having eaten…") while every other δέ is shown. | "And having eaten his meal, …". |
| 325 (24) | n | medium | The note spelled the dative ἑταίροισιν; the line prints ἑτάροισιν (9.326; ἑταῖροι with αι is 9.367). A claim about the very word that carries the drafter's flagged rough breathing was quoted wrongly. | Corrected to ἑτάροισιν. The breathing claim itself stands (see below). |
| 325 (24) | i | low | ASCII apostrophe in "fathom's" (house style is ’). | "fathom’s". |
| 329 (27) | n | low | "ἥ ῥα is 'which, indeed'" but neither layer shows "indeed". | Note now says ἥ is the relative, feminine like κόπρῳ, and ῥα the weak particle ἄρα, left untranslated in both layers. |
| 329 (27) | n | low | "σπείους an old genitive": "old" is not something the aids settle. | "the epic genitive of σπέος". |
| 331 (28) | l | low | "by lot to cast lots" says κλήρῳ twice over. | "But the others lots to cast I bade,". |
| 334 (29) | n | medium | Called ἐλέγμην "the aorist passive" of λέγω. It is an aorist middle (ἐλέγμην) with passive force; the aorist passive would be ἐλέχθην. | "an aorist middle … passive in force: 'I was counted'". |
| 347 (35) | i | low | "so that you may learn" for ὄφρ’ εἰδῇς; `l` has "know". | "know". |
| 351 (38) | l, i | low | ἐπεί is causal and the note says "since"; both layers said "when". `l` also had "the many men" for ἀνθρώπων πολέων (no article). | Both layers "since"; `l` "of many men". |
| 362 (46) | i | low | ASCII apostrophe in "Cyclops' wits". | "Cyclops’ wits". |
| 364 (47) | n | low | "ἐξερέω is the future of ἐξερέω": circular. | "'I will tell out, declare', the epic future (Attic ἐξερῶ)". |
| 365 (48) | n | low | ὑπέστης called "middle sense"; it is the intransitive (second) aorist of ὑφίστημι. | Reworded. |
| 366 (50) | n | low | ἠδέ … ἠδ’ glossed 'both … and'; the line has three terms, mother and father and companions: 'and … and'. | Reworded. |
| 368 (51) | n | low | "The colon opens his reply": the Greek has an ano teleia (the colon is only our English). | "The ano teleia opens his reply." |
| 369 (52) | i | medium | "last, after his own companions, and the rest before him": μετά + dative is 'among', not 'after'; and "his companions … the rest" named the same men twice, muddying who is eaten when. `l` was right. | "I will eat Nobody last among his own companions, and the others before him;" |
| new-renderings.md | μοχλός row | low | The row listed "lever" as avoided without noting that μοχλοῖσιν is shipped "levers" at 5.261 (odyssey-024, conventions line 694). | Row now records that 5.261 stands as shipped, and "stake" is for this sharpened post only. |

## Checks that found nothing to change

- **Labels and cross-references.** Every line/unit reference in the notes was checked against the text: 290, 302, 313, 316, 321, 327, 349, 350, 353, 365, 366, 370 (where the ano teleia or full stop falls); "line 313 calls θυρεός", "βούλευσα in 299", "word of 295", "promise at 356", "same line as 272", "line 342 = 309", "343 = 310", "358 repeats 9.111" all true. Repeated lines: 9.307, 309, 310, 340, 341, 342, 343, 358, 368 reuse the packet's published English (368 is whole-unit identical; the validator's check 6 will pass it).
- **Quotation marks.** Five inner speeches (283–286, 347–352, 355–359, 364–367, 369–370) in ‘ ’, one opening on the `mark` unit and one closing on the last unit of each; no “ ” in this part because the outer speech (Odysseus' tale, opened 9.2) runs on from odyssey-041 (whose last unit closes the Cyclops' question with ’) and on into odyssey-043. `mark` on the first unit of each of the five speeches; `p` on every Murray ¶ (281, 283, 287, 307, 318, 347, 353, 355, 360, 364, 368) and nowhere else.
- **Greek → `l`.** Case relations, tense, mood and particles were checked word by word in every unit; no mistranslation beyond the items above.
- **The 9.366 scan flag** (packet: UNRESOLVED, spondaic fifth, metrical lengthening). Hand scan: Οὖ-τις-ἐ | μοί-γ’ὄ-νο | μα-Οὖ | τιν-δέ-με | κικ-λήσ | κου-σι: dactyl, dactyl, spondee (μα of ὄνομα lengthened, at the main caesura), dactyl, spondee, final. This agrees with the scanner. The irregularity is real, and the one sentence in the notes of both units (366a and 366b) states it correctly: last syllable of ὄνομα long before Οὖτιν; fifth foot a spondee made of the first two syllables of κικλήσκουσι. No other line is flagged by the packet. (The scanner also records "spondaic fifth" without UNRESOLVED at 304, 306, 346; these are ordinary and unflagged, so not noted.)
- **Drafter's three unverified points.**
  1. *Rough breathing in ἑτάροισιν (κ → χ in παρέθηχ’)*: confirmed. ἑταῖρος / ἕταρος has the rough breathing (LSJ), and Murray prints ἐπέθηχ’ before ὡς at 9.314 on the same principle. Only the spelling in the note was wrong (fixed above).
  2. *ἥ ῥα as relative*: confirmed. ἥ with the accent is the relative (the article would be unaccented ἡ); the antecedent κόπρος is feminine; ῥα is the ordinary weak particle. The note now says so and no longer promises an "indeed" neither layer carries.
  3. *σπείους as genitive of σπέος*: consistent with LSJ/Autenrieth (σπέος, gen. σπείους, dat. σπῆι, pl. σπέα / σπέσσι / σπήεσσι), with κατά + genitive 'all over'. I could not check a page; kept as "the epic genitive", with "old" removed.
- **Remembered English.** Looked hard at "struck/dashed", "limb from limb", "brooding evil", "stowed away", "past all bearing", "a piece broken off from ambrosia and nectar", "grind it into his eye", "the wine had gone round the Cyclops' wits"; only the first two were changed. The rest are built from the grammar and either follow the table or are stated in new-renderings.md.
- **new-renderings.md.** All fourteen rows agree with the units (every cited line checked against the `l`/`i` actually used; "fair-coated", "fat flocks", "famous flocks", "human flesh", "unmixed milk", "ivy-wood bowl", "club", "midriff", "a fathom" / "a fathom's length", "past all bearing", "Cruel one", "with words … gentle ones", "meal"/"supper", "Nobody"). One row corrected (μοχλός, above).

## Findings considered and refused

- **9.358 `l`: "makes it grow" against the published 9.111 `l` "makes them grow".** Refused. The published `l` had "vines" as its antecedent; here the antecedent is "wine" and σφιν "for them" (the Cyclopes) stands in the same clause, so "makes them grow" would point at the wrong noun. `i` matches the published `i` ("makes it grow").
- **364 `i` "and I will tell it" for αὐτάρ ('but').** Refused: the contrast is mild, and "and" reads better after "you ask me for my famous name"; `l` keeps "but".
- **365 `i` "the guest-gift" against `l` "a guest-gift".** Refused: the promised gift is definite in English; ξείνιον itself has no article, and "the" here is a reading, not a change of sense.
- **294 `i` "hearts" against `l` "heart".** Refused: the table's τετληότι θυμῷ "with enduring hearts" is the precedent for a singular θυμός of several men.
- **283 `i` "Poseidon, the earth-shaker" against the table's "Poseidon earth-shaker".** Refused: no whole-formula row fixes it; ἐνοσίχθων keeps "earth-shaker" in both layers.
- **Adding a new-renderings row for ἀφραδίῃσιν "in his folly" (9.361).** Refused: a single use, no stock formula; "folly" does not collide with the table's "wanton folly" (ἀτασθαλίαι).
- **Whether ἀποξῦναι (9.326) is a true aorist infinitive.** Left as the note has it; I cannot settle the formation from memory, and the sense ('scrape smooth') is certain.
- **Moving the 9.366 metrical sentence to a single unit.** Refused: the line is split across two units; the first-half unit carries the sentence and the second points back to it.
- **Note length.** Units 0, 2, 8 and 38 are 115–129 words, over the 110 soft band but under the validator's 130 warning line; left, because each carries several forms that need saying. Unit 1 (157) was trimmed.
- **Glossary / `gloss.json`:** out of scope for this run.

## Glossary pass

Checked all 134 novel entries and the 12 `__broaden__` entries against the printed lines (units.json `t`). All novel entries are under 230 characters and use only the typographic ’; no line numbers or "here". Broadened entries exceed 230 characters only because they carry the old entry whole plus the new readings. Changes (7 novel, 4 broadened):

Novel entries
- δολίοις: removed the misleading "(Attic -οις)" (the form is the same in Attic); now "agreeing with ἐπέεσσι".
- καλλίτριχα: "epic stem -τριχ-" was wrong (θ > τ before the aspirate is ordinary dissimilation, not epic); reworded.
- κατέαξε: "(Attic κατέαξε…)" named no Attic difference; now says it is from the ᾱ-stem aorist ἔᾱξα.
- ἀνεσχέθομεν: parsed "aor. mid."; -ομεν is an active ending (aorist stem ἀνεσχεθ-, cf. ἔσχεθον); corrected to aor. 1 pl. act. (= ἀνέσχομεν).
- τισαίμην: lemma now τίνω, mid. τίνυμαι; dropped the pointless "(τίσαιμην)" respelling.
- πέμψειας: opt. stands in an εἰ-clause; gloss now "you would send".
- ἑτάροις: "epic -οις" named no difference; now "= Attic ἑταίροις".

Broadened entries
- δοίη: the new reading "independent wish: may (she) give" disagrees with the unit translation, where δοίη continues the εἴ πως clause; reworded as a wish continued after εἴ πως with a new subject.
- ἄκρον: the old ‘ … ’ (left-quote opening) was corrected to ’ … ’.
- μεγάλ: "in abundance" duplicated ἤλιθα; now "greatly, very", strengthening ἤλιθα.
- ὥς: new reading said "ὡς … accented", but the word is printed ὥς in ὥς περ; reworded.
- Other eight broadened entries (διὰ, ἐρυσσάμενος, τοῦ, κατὰ, ἡδὺ, δῶ, ἀμβροσίης, μεγαλήτορα) checked and kept.

Findings refused or left open
- δυνάμεσθα "pres. opt." (= δυναίμεθα): the formation is debated (opt.-like with κεν); kept as is.
- ἀποξῦναι as aor. inf. of ἀποξύω: formation uncertain (as in the main review); kept.
- οὐτάμεναι "aor. inf.": athematic, LSJ treats it as aorist; kept.
- Old-entry wording in the broadened entries (e.g. "(of Odysseus)" on μεγαλήτορα, the ὥς causal example) not reopened: additions-only rule; only an orthographic fix made.
- ἔρεξας / φάγες "aor. 2 sg.": means aorist, second person; kept.
