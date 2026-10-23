# Review — iliad-055 (Iliad 9.307–429), pass 1

Reviewer pass 1 of 2 (`gloss.json` does not exist yet; the second pass reads it). `units.json` edited in place by script; `t` untouched (checked: every unit's `t` identical before and after, and the joined `t` equals the packet's 123 lines). Build not run.

Severity: **major** = the validator would fail, or a house rendering is broken; **minor** = wrong or misleading in sense, wording or a note's claim; **nit** = small accuracy or tidiness.

Method: every note claim checked against the form and the line; Greek to `l` word by word; `l` against `i`; house table (Iliad and Odyssey) grepped word by word; every line and every unit of the part compared against all published Iliad and Odyssey units (the packet lists only four repeats; a script found a fifth, 9.422); quotation marks (“ on 9.308, ” on 9.429, none elsewhere; part 054 ends with ” at 9.306, so 9.307 opens in narration, correct); `mark` and `p` (only 9.307 `p`, only 9.308 `mark`, as the packet's single ¶ and one speech require); `ln` of every unit; `l` line count equals `t`; no `\n` in `i`; typographic ’ only; no backticks. Scansion flags: none in the packet, so no hand scansion was required.

## Changes made

| Line (unit `ln`) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 314 | `l`, `i` | major | The unit's Greek (letters only) is identical to the published unit at iliad-052 line 103, so the validator (check 6) requires its `l` and `i` word for word. `l` had an added "it" and both layers closed with a colon, which would fail the gate. | Set `l` = "But I shall say as it seems to me to be best." and `i` = "But I will say it as it seems best to me." (exactly the published strings); note gains a clause saying the English closes with a full stop as it does where the words first stand. |
| 422 | `l`, `i` | major | 9.422 τὸ γὰρ γέρας ἐστὶ γερόντων is the same unit as iliad-024 line 323 (4.323); the packet did not list it, but the validator will. `i` read "the prize of honour of elders" against the published "the old men’s prize of honour", and the punctuation differed. | Set `l` = "for that is the prize of old men." and `i` = "for that is the old men’s prize of honour." (the published strings). The note already agrees. |
| 385 | `l`, `i`, `n` | major | θυμαλγέα λώβην rendered "outrage". The Odyssey table fixes λώβη with θυμαλγής as "heart-paining insult" / "the insult that pained the heart" (rows 18.347, 24.326) and explicitly turns down "outrage" for that pairing; the Iliad table (1.232) keeps "outrage" only for the plain noun and says "insult" is kept for λώβη with θυμαλγής. The note claimed "fixed renderings" while using the wrong one. (`new-renderings.md` lists the phrase as "reused"; it was reused wrongly.) | `l` "the whole heart-paining insult."; `i` "the whole insult that pains my heart."; note now says λώβη with θυμαλγής is "heart-paining insult" and "insult" is kept. |
| 406 | `l`, `i`, `n` | major | ξανθὰ κάρηνα rendered "tawny heads". The table gives ξανθός "fair" (ξανθὸς Μενέλαος "fair-haired", ξανθὰς τρίχας "the fair hair") and lists "tawny" as reserved for αἴθων. | "the fair heads of horses" in both layers; note says ξανθός is the colour word kept as "fair" (of horses a yellowish brown). |
| 308 | `l`, `i` | minor | `l` "murmur at me sitting beside me" gave παρήμενοι an object it does not have (μοι belongs to τρύζητε) and repeated "me"; `i` "sit beside me murmuring" dropped the "at me" of μοι τρύζητε. | `l` "so that you not murmur at me, sitting beside, one from one side, another from another"; `i` "so that you do not sit beside me and murmur at me, one from one side and another from another". |
| 315 | `l` | minor | "Neither me, Atreus’-son Agamemnon, will persuade, I think, / nor the other Danaans" does not show the construction (Ἀτρεΐδην Ἀγαμέμνονα and ἄλλους Δαναούς are the two accusative subjects of πεισέμεν; ἔμεγ’ is the object) and can be read with the persons the wrong way round. | "Neither me will Atreus’-son Agamemnon persuade, I think," (`i` was right and is unchanged). |
| 315 | `n` | nit | The note did not say how οὔτ’ … οὔτ’ is built. | Added: the two accusative subjects and ἔμεγ’ as object, governed by οἴω. |
| 330 | `i` | minor | "many fine treasures" for πολλὰ καὶ ἐσθλά: "fine" is reserved for καλός in the table (ἐσθλός is "good", `l` already had "good"). | "many good treasures". |
| 330 | `n` | nit | τάων ἐκ πασέων called "relative-demonstrative … ‘out of all of which’"; τάων is the demonstrative pronoun (‘of those’), not a relative. | "the article as a demonstrative pronoun, ‘out of all of those (cities)’". |
| 348 | `l`, `i` | minor | ἐπ’ αὐτῷ "beside it" / "along it", and "planted" for κατέπηξεν, "wide, great": the same words stand in the Iliad table at 7.440–441 (τάφρον … ἐπ’ αὐτῷ … εὐρεῖαν μεγάλην "close by it … wide and great"; κατέπηξαν "fixed"). Same Greek, same English. | `l` "a ditch close by it, / wide and great, and in it he has fixed stakes"; `i` "dug a ditch close by it, wide and great, and fixed stakes in it". |
| 356 | `n` | minor | "One sentence runs over three units": the sentence 356–361 is two units (356–358, 359–361); the next, 362, is a new sentence. | "two units". |
| 367 | `i` | minor | γέρας rendered "my prize"; the table keeps γέρας "prize" in `l` and "prize of honour" in `i` at every occurrence (and 334, 344, 422 do). | "my prize of honour". |
| 393 | `n` | minor | "σαῶσι is σαώσωσι" (a sigmatic aorist subjunctive) misstates the form; σαῶσι is the contracted present subjunctive of σαόω (as σαῷ in 424). | "σαῶσι is the contracted subjunctive of σαόω". |
| 412 | `n` | minor | "Τρώων is the epic genitive plural": Τρώων is the same in Attic; nothing epic about it (Τρώεσσιν in 337 is). | "Τρώων is the genitive plural". |
| 401 | `n` | nit | ψυχῆς "life, here what a man stakes": nothing is staked at 401. | "‘life’". |
| 404 | `n` | nit | πετρηέσσῃ called Pytho's "stock epithet": this part cannot show that. | "‘rocky’ describes the place". |
| 417 | `n` | nit | The table (7.30–31 row) asks that τέκμωρ of Ilios be told apart from the "sign" of 1.526; the note was silent. | Added "(at 1.526 the same word is a ‘sign’)". |
| 340 | `n` | nit | The note did not say that μερόπων ἀνθρώπων can go with μοῦνοι or with ἀλόχους, which affects how `l` and `i` read. | One sentence added: both readings possible; the reading layer takes ‘alone of men’. |
| (header) | `about` | nit | "undying fame": the house keeps "undying" off ἄφθιτος (it is "unfailing"). | "unfailing fame". |

Totals: 19 findings, 27 fields changed. **Major 4, minor 8, nit 7.**

## Findings considered and refused

- **9.309 μῦθον not in `i`** ("I must speak my mind bluntly"): `l` has "the word"; `i` is idiomatic English for μῦθον ἀποειπεῖν, and μῦθος is not a stock epithet. Left.
- **9.327 σφετεράων "their own"** dropped to "their" in `i`: `l` and the note carry "own"; in `i` it adds nothing. Left.
- **9.399 ἄκοιτιν "a fitting mate / partner"** against the table's plain "wife" for ἄκοιτις (and 397's "my dear wife"): "wife" would repeat ἄλοχον ("a wedded wife, a fitting wife"); "mate" and "partner" are not on the table's avoided list. Left; the second pass should glance at it.
- **9.367 `i` "has taken back"** for aorist ἕλετο (against "he took" at 335): an English perfect for a recent grievance in speech; `l` keeps "took". Left.
- **9.388 γαμέω "a present form with the sense ‘I shall marry’"**: the form is a future or short-vowel subjunctive; the note's description is a safe one and the English is right. Left.
- **9.418 δήετε "a future of δηέω (a defective form)"**: LSJ lists it under δήω; the claim is close enough and the gloss is right. Left.
- **9.409 `i`** "it can neither be raided nor taken to make it come back": clumsy but true to λεϊστή / ἑλετή with πάλιν ἐλθεῖν; a smoother version would lose the infinitive. Left.
- **9.359 `l` capital "You"** after a comma-ended preceding unit: it matches the published `l` of iliad-024 for the same words; `i` is lower-case as the continuation requires. Left.
- **9.337–340 unit cuts at "·" and "?"**: all correct by the sectioning rule; units ending at a comma (323, 356, 379, 401) each sit in a period longer than four lines, so the comma cut is allowed.
- **9.422 note** calling τό a demonstrative pointing at the task: tenable (the published note for 4.323 reads τὸ γὰρ γέρας differently, but the validator checks only `l` and `i`). Left.
- **Packet's missed repeat**: 9.422 (fixed above). A script compared all 123 lines and all 66 units against iliad-001…054 and odyssey-001…: no other whole-unit repeat; whole-line repeats are 9.307, 9.308 (many Odyssey and Iliad occurrences, all with identical English to ours), 9.314, 9.359, 9.422; 9.312 follows Odyssey 14.156 (ὁμῶς Ἀΐδαο πύλῃσι) and 9.376 ἕκηλος follows the table (8.512, 13.423).

## Notes for the second pass and for the drafter's file

- `new-renderings.md` lists θυμαλγέα λώβην among the "reused" items; the units now do reuse the Odyssey/Iliad rendering ("insult"). The file was not edited here.
- The second pass should read `gloss.json` for: ἐρίβωλον (two uses), ἀπηλεγέως, δόσκον / δασάσκετο / ἔχεσκεν / ἐθέλεσκε (iterative -σκ-), ἄμμι, ἑθεν / εὑ, δήετε, πείσει’ (optative), σαῷ / σαῶσι (contracted subjunctives), ἀφήτορος, καρός, ἱρά / ἅλα δέ, κάτθαν’, κάλλιπον, ὀάρων, and the homograph pair ἑὴν (possessive, 420).

---

# Pass 2 (reviewer, second pass; reads `gloss.json`)

`units.json` and `gloss.json` edited in place by script; `t` untouched (every unit's `t` compared before and after). `gloss.json` was checked with the build's own rules, read-only (not run): no new form redefines an existing one, every key is in the part, ’ only, under 230 characters, no line numbers, every `__broaden__` entry contains the published entry whole, no form without an entry. Build not run.

Method: units re-read in full against the Iliad and Odyssey house tables (word by word, plus a 3-word-sequence comparison of every unit against all published Iliad and Odyssey units for phrases the packet did not list); every one of the 179 new glossary entries and 8 broadened entries parsed against the line; the 437 known-form entries compared with their use in this part.

## Changes made

| Line / form | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 328 ἀλάπαξ’ | `l`, `i`, `n` | major | ἀλαπάζω rendered "sacked". The table fixes ἀλαπάζω as "lay waste" (2.367, 5.166; Odyssey 17.424 "laid waste") and keeps "sack" for ἐκπέρθω. | "cities I laid waste of men" / "I laid waste twelve cities of men"; note says ‘lay waste’. `about` "sacking cities" became "laying waste cities". |
| 356 ἱρὰ Διὶ ῥέξας | `l`, `i`, `n` | major | "sacred offerings … having sacrificed" / "when I have sacrificed to Zeus". The table renders ἱρά "the sacrifices" and turns down "the offerings" (2.420); iliad-002 ships ἱερὰ ῥέξας as "performed the sacrifices". The new-renderings row treated a reused phrase as new and used a turned-down word. | `l` "tomorrow sacrifices to Zeus having performed"; `i` "when I have performed the sacrifices to Zeus and to all the gods"; note rewritten. |
| 332 δασάσκετο · ἔχεσκεν | `l`, `i` | minor | The note says the verbs are iterative, but neither layer showed it ("distributed few, and many kept"; "took them, shared out a few, and kept many"), unlike δόσκον in 331 and the table's -σκ- rows (3.216–219 "would"). | `l` "would distribute few, and many keep"; `i` "he would take them, share out a few, and keep many". |
| 369 ὡς ἐπιτέλλω | `l`, `n` | minor | `l` "as I charge you"; the table keeps ἐπιτέλλω "enjoin" in `l`, "charge" in `i` (2.10; iliad-007 line 9 has "as I enjoin"). | `l` "as I enjoin"; note names both. |
| 398 ἄκοιτιν | `l`, `i`, `n` | minor | "a fitting mate" / "a fitting partner". The table says ἄκοιτις "is a plain word for wife" and turns down "spouse", "bedfellow", "consort"; "mate"/"partner" are the same family. (Pass 1 left this open.) | "a wedded wife, a fitting wife" in both layers; note says ἄλοχον and ἄκοιτιν are two words in apposition, both "wife". |
| 388 γαμέω | `n` | minor | Note called γαμέω "a present form"; the glossary calls it a future. Contradiction, and the present is the wrong label. | Note: uncontracted future (or short-vowel subjunctive with future sense; Attic γαμῶ). Glossary entry given the same two options. |
| 417 δήετε | `n` | minor | Note: "future of δηέω"; glossary: lemma δήω. A lemma δηέω does not exist. | Note: "future-sense form of δήω ‘find’ (a defective verb)". |
| 427 κατακοιμηθήτω | `n` | minor | Note: "aorist passive imperative … ‘let him be put to sleep’"; glossary and `l`/`i` have "lie down / sleep" (middle sense). | Note: passive form with middle sense, ‘let him lie down to sleep’. |
| 319 ἰῇ | `n` | nit | "Ionic" feminine dative; ἰῇ is the Homeric (epic) form, Ionic is μιῇ. | "epic". |
| 325 ἀνδράσι μαρνάμενος | `l` | nit | "fighting / with men" can be read as "alongside"; 315 has "against". | "fighting / against men". |
| 330 τάων ἐκ πασέων | `l` | nit | "From all of these treasures many and good" reads τάων with κειμήλια. | "From all of these, treasures many and good". |
| 419 ἑθεν | `n` | nit | Note wrote ἕθεν (orthotone); the line has enclitic ἑθεν. | "ἑθεν". |

### `gloss.json` (novel entries; each checked against the line)

| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| ἀλάπαξ | minor | Meaning "sack, plunder, destroy", gloss ‘I sacked’; house word is "lay waste". | "lay waste, sack, plunder"; ‘I laid waste’. |
| ἱρὰ | minor | "sacrifices, offerings". | "sacrifices". |
| ἀπομηνίσαντος | minor | "nurse one’s wrath, rage"; ‘while I raged’ does not match the line, `l` or the shipped ἀπομηνίσας "withdrawn in wrath" (2.772). | "rage in wrath, hold aloof in wrath (the force of ἀπο- uncertain)"; ‘with me withdrawn in wrath’. |
| ἀπτῆσι | minor | Lemma ἄπτης with "epic -ῃσι (= Attic -αις)": the dative plural of ἀπτήν is a third-declension form, not an epic first-declension ending. | "ἀπτήν — unfledged, not yet able to fly; adj., masc. dat. pl. ἀπτῆσι, agreeing with νεοσσοῖσι". |
| μάστακ | minor | Lemma μάστας; the noun is μάσταξ, μάστακα (LSJ). | Lemma μάσταξ. |
| γαμέω | nit | See 388 above. | Fut., or short-vowel subjunctive with future sense. |

### `__broaden__` (known entries that gave a false or misleading parse for this part; old entry kept whole, new reading added after " · ")

| Form | Severity | Gap | Added |
|---|---|---|---|
| κάρηνα | minor | Entry says acc. pl.; ἵππων ξανθὰ κάρηνα is nominative and means horses' heads. | neut. nom. pl., ‘heads’ |
| πλεῖστα | minor | Entry says acc. pl.; 382 is nominative with κτήματα. | neut. nom. pl. with κτήματα |
| ἀχαιΐδες | minor | Entry says "of men as an insult"; 395 is literal. | fem. nom. pl., literal ‘Achaean women’ |
| ἴσχειν | minor | Entry says "as an imperative"; 352 is the complement of δύναται. | complementary infinitive ‘to hold back’ |
| δόμοις | minor | Entry says "plural for one dwelling … after ἔνι"; 382 means houses, with ἐν after the noun. | ‘houses’, ‘in the houses’ |
| πόλεις | minor | Entry says "in apposition to the place-names"; 328 is a plain object. | direct object of a verb of sacking |
| πειράτω | nit | Entry says "+ inf."; 345 takes the genitive (μευ). | + gen. ‘make trial of’ |
| φθίην | nit | Entry says "with -δε"; 363 and 395 have none. | without -δε, goal; after ἀνά |
| τέλος | nit | 411 τέλος δέ is accusative with -δε, not an object. | with the -δε of direction |
| ἑθεν | nit | Entry only for "after εἵνεκα". | with the preverb of ὑπερέσχε, ‘over it’ |

The eight Pass-1/glosser broadenings (αἱματόεντα, διέπρησσον, θυμαλγέα, κιχείη, λώβην, ἕτερον, ὅ, πολεμίζοι) were each checked against the line and are right.

### `new-renderings.md`

- θυμαλγέα λώβην was listed among the reused phrases without saying which rendering; now marked **reused, "insult"** ("heart-paining insult" / "the insult that pains my heart"; "outrage" kept for the plain noun) (minor).
- The ἱρὰ ῥέζω row presented a reuse as a new choice with a turned-down word; replaced by a reuse row (minor).
- The 9.314 sentence said the `l`/`i` close with a colon; Pass 1 had already set the published full stop, so the claim was false; corrected (nit).
- ἀλαπάζω "lay waste" and ἄκοιτις/ἄλοχος "wife" added to the reused list (nit).

## Findings considered and refused (Pass 2)

- **334 δίδου** `l` "was giving" against `i` "would give": the surrounding verbs are habitual (δόσκον, δασάσκετο), and the note says "imperfect". Left.
- **353 ἐθέλεσκε** `l` "was not willing": the table's -σκ- rows show the iterative in `i` ("never went", 1.490) as often as in `l`; `i` here has "never willing". Left (332 was changed because neither layer showed it).
- **376 ἕκηλος** `i` "at his ease" against the table's "at ease": the pronoun is in the Greek context (οἱ) and 14.479 has "at their ease". Left.
- **367 "has taken back"**, **309 μῦθον**, **327 σφετεράων**: refused in Pass 1; upheld.
- **ἐρίβωλον** gloss "rich-soiled, fertile" against `l` "rich-clodded": the glossary gives meaning, not the house word. Left.
- **εἵλετο** known entry "took up (for himself)" for 344/368/377; **μάχην** entry "object of καταδύμεναι"; **ἀμείνω** entry "with ὀμίχλην"; **ἠϋκόμοιο** and **ἰχθυόεντα** entries naming other nouns: all give the right lemma and parse; the examples are specific but not false. Not rewritten (rule: never rewrite existing entries except to broaden).
- **ἀπάτησε** gloss (aor., "unaugmented") for 375, where it is the tmesis form of ἐξαπατάω: the parse is right for both; the note says it. Left.
- **τετλαίη** "perf. opt." and **ἀμείψεται** "aor. subj. (short vowel) … or fut.": both defensible readings; left.
- **Other repeated word-sequences** (the 3-word comparison against all published Iliad and Odyssey units gave 74 hits in this part): all agree with the published English (ditch 348, "Scaean Gates and the oak" 352, "fence of the teeth" 409, "stout flocks" 406, "dear fatherland" 414, "Hellas and Phthia" 395) except the three fixed above (328, 356, 369).
- **9.348 "close by it"** and **9.407 "stout flocks"**: match the table; left.

## Totals (Pass 2)

32 findings: **major 2, minor 19, nit 11.**
By file: `units.json` 12 (major 2, minor 6, nit 4); `gloss.json` novel entries 6 (minor 5, nit 1); `__broaden__` additions 10 (minor 6, nit 4); `new-renderings.md` 4 (minor 2, nit 2). Combined with Pass 1 (4 major, 8 minor, 7 nit): **major 6, minor 27, nit 18.**
