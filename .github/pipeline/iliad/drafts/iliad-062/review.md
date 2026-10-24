# iliad-062 (Iliad 10.390–481) — review, pass 1

Scope of pass 1: every note's grammar and cross-references against the line, Greek to `l` to `i`, repeated-line English (packet and the shipped tables), quotation marks and `mark` (neighbours: iliad-061's last unit, ln 389, ends with ”; iliad-063 does not exist yet, and its first line 482 `ὣς φάτο, τῷ δ’ ἔμπνευσε μένος…` is narrative, so the closing ” on 481 is right), paragraph flags (`p` on 390, 400, 412, 423, 426, 446, 454, 465 = the edition's ¶), `t` coverage (the units' `t` concatenate exactly to lines 390–481), and the two scansion flags. `t` was not touched (checked: identical before and after). Pass 2 (gloss.json) is still to do.

Severity: major = wrong in fact, force or rule; minor = imprecise or inconsistent but not false; nit = wording.

## Changes

| # | line (unit ln) | field | severity | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 418 | `n`, `l`, `i` | major | The note said οἷσιν ἀνάγκη means ‘for which there is need’, with the hearths (ἐσχάραι, feminine) as antecedent. οἷσιν is masculine or neuter dative plural and cannot agree with a feminine noun: the relative points to the men at the fires. `l` ‘for which’ and `i` ‘where there is need’ carried the same error. | Note now says ‘for whom there is need’ and why οἷσιν cannot be the hearths. `l`: ‘for whom there is need’. `i`: ‘At every one of the Trojans’ hearth-fires, the men who must are awake and bid one another keep watch;’. |
| 2 | 442 | `l`, `i` | major | Stray opening quotation mark “ on the unit at 442. Dolon's speech opens at 427 (“ on that unit) and runs to 445 (” on this unit); 442 is mid-speech, so the speech had two openers. | Removed “ from `l` and from `i`; the closing ” stays. |
| 3 | 413 | `l`, `i`, `n` | major | τοὶ γὰρ ἐγώ τοι … καταλέξω is the Odyssey's τοιγὰρ ἐγώ τοι πάντα μάλ’ ἀτρεκέως καταλέξω (24.303, shipped odyssey-117: ‘Well then, I will tell you everything quite exactly’). The draft used ‘So then’, which the Odyssey table lists as avoided, and `i` added ‘all’ (‘all this’) that the Greek does not have; `new-renderings.md` records no departure. | `l`: ‘Well then, I to you these things very exactly will recount.’ `i`: ‘Well then, I will tell you these things quite exactly.’ Note says τοιγάρ is ‘well then’, as in 24.303. |
| 4 | 427 | `l`, `i`, `n` | major | Same as 413 (‘So then’ for τοὶ γάρ). | `l`: ‘Well then, I these things also very exactly will recount.’ `i`: ‘Well then, I will tell these things too, quite exactly.’ Note: ‘well then’. |
| 5 | 465–466 | `n` (unit at 465) | major (flag) | The scansion note said only that ‘a syllable of μυρίκην that the scansion table counts as long has to be read short’. | Identified: it is the υ. The scanner's hint list has the prefix μῡρι- (made for μύριος ‘countless’), which wrongly matches μυρίκη and marks υ long; the metre needs μυ- ρί- both short. Note now reads: ‘Line 466 is metrically irregular as the scansion table reads it, at ἀνὰ μυρίκην: the final α of ἀνά is short and has to be lengthened before μ, and the υ of μυρίκην, which the table counts long, has to be read short.’ Hand scansion of 466: θῆ-κεν-ἀ | νὰ-μυ-ρί | κην-δέ-ε | λον-δ’ἐ-πὶ | σῆ-μά-τ’ἔ | θη-κε (dactyl, dactyl with νὰ lengthened, dactyl, dactyl, dactyl, spondee; 17 syllables), so the only real licence is the lengthened ἀνά before μ-. |
| 6 | 467 | `n` (unit at 466) | major (flag) | Same vague wording for 467. | Note now reads: ‘Line 467 is metrically irregular as the scansion table reads it, at μυρίκης, where the υ, which the table counts long, has to be read short, as in 466.’ Hand scansion: συμ-μάρ | ψας-δό-να | κας-μυ-ρί | κης-τ’ἐ-ρι | θη-λέ-ας | ὄ-ζους (spondee, four dactyls, spondee; 16 syllables); only the table's long υ is in the way. |
| 7 | 424 | `n` | minor | Note said ἦ ‘ends the question at the mid-line question mark’; the question ends at the mark after ἀπάνευθε, not at ἦ. | Reworded: ‘…and the question ends at the mid-line question mark after ἀπάνευθε.’ |
| 8 | 401 | `n` | minor | Note said τοι is ‘either ‘for you’ or the particle’, but `l` and `i` both take it as ‘your heart’; the note did not match its own `l`/`i`. | Note now says τοι is the dative ‘to you’, here with θυμός as ‘your heart’, and that it could also be the particle. |
| 9 | 394 | `i` | minor | Line 396 repeats 10.309 of iliad-061, whose `i` has ‘just as before’; this unit had ‘as before’. | `i`: ‘…guarded just as before,’ (`l` already matched). |
| 10 | 425 | `i` | minor | ‘Explain it all to me’ for δίειπε (‘tell right through’) adds the sense of interpreting, which the Greek does not have; `l` says ‘Tell it through’. | `i`: ‘Tell me all of it, so that I may learn.”’ |

Counts: major 6 (items 1–6, of which 5 and 6 are the scansion notes), minor 4, nit 0.

## Findings considered and refused

- 391 `i` ‘Hector has led me out of my wits’ (perfect for the aorist ἤγαγεν; ‘out of my wits’ for παρὲκ νόον). The perfect is natural in a speaker reporting what has just happened to him; ‘out of my wits’ is the drafter's own and fits ἄτη. Left.
- 402–403 `i` ‘to tame and to drive’ against passive δαμήμεναι, ὀχέεσθαι in `l`. The agent is the dative ἀνδράσι; the sense is the same and the table row says so. Left.
- 437 `i` ‘for running like the winds’ is clumsy but not wrong; `l` carries the construction. Left.
- 436 `l` ‘greatest’ against `i` ‘largest’ for μεγίστους: recorded in the note and in new-renderings. Left.
- 448–451 `i` ‘to fight us head-on’ (‘us’ not in the Greek). The object is understood from context. Left.
- 454 `i` ‘with the sword’ for φασγάνῳ (no article); the table's 8.87 row has ‘with his sword’. Left.
- 462 `i` ‘make our offerings to’ for ἐπιδωσόμεθ’: the note says the sense is not secure. The note and `i` agree. Left.
- 466 `i` ‘when they came back’ for αὖτις ἰόντε: ‘again’ can carry the return here. Left.
- Every other label I checked (cases, tenses, moods, duals, tmeses, epic forms) is true of the form in the line. Cross-references checked and correct: 10.308–309, 10.310–312, 10.314, 10.334–335, 10.298, 10.382, 10.384, 4.411 (iliad-025), Odyssey 22.371 and 22.329 (odyssey-109), Odyssey 8.165 (odyssey-034).
- Quotation marks otherwise right: openers on 391, 401, 413, 424, 427, 447, 462, 477; closers on 397, 409, 422, 425, 445, 452, 464, 481. `mark` is on the first unit of each of those eight speeches only.
- The `l`/`i` of the six repeated units (397–399, 400, 405, 423, 446, 457) are identical to the published ones.

## Follow-ups for whoever continues

- (Done in pass 2.) `new-renderings.md` had no row for τοὶ γὰρ ἐγώ τοι … (413) and τοὶ γὰρ ἐγὼ καὶ … (427); a row each (‘Well then’, following the Odyssey's τοιγάρ, 24.303) should be added before the table is updated.
- The μῡρι- hint in `../odyssey/scan_hexameter.py` is what raises both scansion flags. I did not edit the Odyssey's scanner (runbook: never edited from here). If the owner agrees the υ of μυρίκη is short, 467 is not irregular at all and 466 shows only the lengthening of ἀνά before μ.
- Pass 2 (parses in gloss.json against the line) not yet done.

# Pass 2 — gloss.json (parses against units.json)

Method: re-read units.json as edited in pass 1; checked every one of the 119 novel entries and the 20 `__broaden__` entries against its line; checked every token of the part against known-forms.json for readings the old entry does not cover; format (no line numbers, typographic ’ only, no entry of 230 or more characters among the novel ones; all 119 keys of novel-forms.json present, nothing extra; every broadened entry keeps the old entry whole and adds after " · "). The longest novel entry is 163 characters.

## Changes

| # | key | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | ἠὲ (broaden, new) | major | known ἠὲ covers only ‘or’ and ‘than’; the form is used for ‘whether’ in an indirect question at 394 (ἠὲ φυλάσσονται) and 442 (ἠὲ κατ’ αἶσαν ἔειπον). The ‘whether’ reading exists only under the acute-spelled ἠέ. | Broadened with the ‘whether’ reading. |
| 2 | ἔντεα (broaden, new) | major | Known entry says neut. acc. pl. only; at 407 and 471 ἔντεα is nominative (ἔντεα κεῖται; ἔντεα … κέκλιτο). | Broadened: neut. nom. pl., subject. |
| 3 | ἀρήϊα (broaden, new) | minor | Known entry says ‘agreeing with τεύχεα’, acc.; at 407 it agrees with nominative ἔντεα. | Broadened. |
| 4 | μυρίκην, μυρίκης | major | Both said ‘Ionic -η / -ης (= Attic μυρίκη, -ης)’: false, since Attic has the same forms (η after κ). | Dialect claim removed. |
| 5 | τοῖσδεσσι | minor | Said ‘neut.’ and glossed ‘with these things’; the dative plural is masc. or neut., and the sense after χαῖρε is ‘be glad of these’, not ‘with’. | ‘masc./neut.’, gloss ‘these’. |
| 6 | ἢ (broaden) | minor | 432 τί ἢ ἐμέ is not covered (the old entry has τί ἢ δέ only). | Added τί ἢ ἐμέ as a form of τίη, ‘why’. |
| 7 | ἀγαυοῦ (broaden, new) | nit | Known entry lists its agreeing nouns (Τυδέος, Λαομέδοντος); 391 has Πηλεΐωνος. | Added. |
| 8 | σὲ (broaden, new) | nit | Known entry lacks σέ as object of a verb of giving (462 σὲ … ἐπιδωσόμεθ’). | Added. |
| 9 | βουληφόροι | nit | Gloss ‘who are counsellors’ contradicts the house word in new-renderings (‘councillors’; ‘counsellors’ avoided). | ‘councillors’. |
| 10 | ἐσχάραι | nit | Gloss ‘fires’ differs from `i` ‘hearth-fires’. | ‘hearth-fires’. |
| 11 | ἁμάς | nit | ‘epic by-form of ἡμέτερος’: ἁμός is the Aeolic form found in epic. | Reworded. |
| 12 | πρώτην | nit | ‘(a goddess)’ pins the entry to the line. | Removed. |
| 13 | ἐπιδωσόμεθ | nit | Gloss ‘we shall make offerings to’ was given without the hedge the note and new-renderings carry. | Added ‘(sense not secure)’. |

Counts for pass 2: major 3 (items 1, 2, 4), minor 3 (3, 5, 6), nit 7 (items 7–13).

## Findings considered and refused (pass 2)

- ὅδε entries (οἷδ, τοῖσδεσσι) keep ‘this here’: the phrase is the glossary’s standing wording for ὅδε (known τόδε, Odyssey entry) and is not a line pin.
- ‘agreeing with X’ / ‘after Y’ clauses in many novel entries (e.g. θείου, ὅσσαι, ἀνέμοισιν) name the governing word in the line; the existing glossary does the same (ἀγαυοῦ, ἐμῇς), they carry no line number and are general to the construction. Left.
- εἰσί accent note: a disyllabic enclitic after a paroxytone keeps its accent, so the parse is right.
- The `__broaden__` additions for γυῖα, δώρων, καλὰ, οἷ, οἷσιν, πάρος, πρὸς, ἀνὰ, ἥρως, τῶν, εἰ, τέλος, κεφαλῆφιν, λίσσεσθαι, μητιόωσι, πρόφερε, κεν, κέ, κ were each checked against the line cited and are true; οἷσιν ‘for whom’ matches the pass-1 correction at 418.
- λύ (elided λύ’ = λῦε), δαείω, πελάσσετον (shape of a short-vowel subjunctive or future used as a command), ἀπολύσομεν, μεθῶμεν, ἐγρηγόρθασι, ἐπέφνομεν: parses checked and correct; the Odyssey table’s entries for the same forms agree.

