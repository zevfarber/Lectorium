# odyssey-092 (19.1–103) — review

Reviewer: adversarial, two passes. Pass 1: `units.json` against the Greek, the table in `conventions.md`, the shipped parts and the source. Pass 2: `gloss.json` (appeared 07:02) parse by parse against the line, plus a second sweep of the units. `t` was never touched. A dry run in a scratch copy of the repository (build, then `validate_odyssey.py`) ends in PASS with no WARN. No modern translation was consulted.

Severity scale: major = wrong sense or wrong text; moderate = false grammatical label, false cross-reference, or a breach of a fixed table rendering; minor = wording, consistency, completeness.

Counts: 0 major, 6 moderate, 26 minor (32 changes in all). Findings refused: 14 (listed at the end).

## Changes to units.json

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 19.4 · n | moderate | Cross-references false. The note said the order was given "at 16.283–285" and the excuse is "at 16.286–294". In the source, 16.283 is the nod, the order itself is 16.284–285, 16.286–287 are the end of 19.5 and 19.6, and the excuse is 16.288–294. | Rewritten: order at 16.284–285 "nearly in the same words"; the end of 19.5 and 19.6 are 16.286–287; excuse at 16.288–294. |
| 19.29 · n | moderate | "ἔπλετο is the unaugmented aorist of πέλομαι" is false: ἔπλετο carries the ordinary augment ἐ- (odyssey-008's note says so; the glossary entry calls it plain aor.). | "ἔπλετο is the aorist of πέλομαι ‘become, be’, which carries the ordinary augment ἐ-." |
| 19.74 · i | moderate | "Such are beggars and wandering men": the table fixes ἀλήμων as "vagrants" in both layers (17.376, shipped 085) and keeps "wandering" for ἀλάομαι / ἀλητεύω. | i now "Such are beggars and vagrants;" (`l` already had "vagrant men"). |
| 19.72 · n | moderate | "ῥυπόω … in its Ionic contracted form" is false: ῥυπόω is the uncontracted present (Attic contracts to ῥυπῶ). | "an uncontracted present (Attic would contract it to ῥυπῶ)". Matches the gloss entry. |
| 19.37 · i | minor | "as though of blazing fire": the table gives αἰθομένας δαΐδας "burning torches" and expressly avoids "blazing"; "blazing" is the table's rendering of κηλέον. | "as though of burning fire". |
| 19.59 · l | minor | "There sat down then circumspect Penelope." The wording shipped at 16.48 is "There then sat down …", and the new-renderings row says the shipped wording is kept. | "There then sat down circumspect Penelope." Row in `new-renderings.md` corrected to match. |
| 19.102 · l | minor | Same as 19.59. | "There then sat down much-enduring, heavenly Odysseus." |
| 19.22 · l | minor | "presence-of-mind": the table row for ἐπιφροσύνη (5.437) has "presence of mind" with no hyphens; a second spelling for one word. | "presence of mind"; the `new-renderings.md` cell corrected to match. |
| 19.47 · i | minor | "the place where he had always slept": "always" is not in the Greek (πάρος "formerly" + iterative optative); `l` has "used to sleep". | "where he used to sleep". |
| 19.47 · n | minor | "κείων is a participle of κεῖμαι with a wish in it" is loose: the form is the desiderative participle of κείω (so the glossary says). | "κείων is the desiderative participle κείω, from κεῖμαι, ‘wishing to lie down’". |
| 19.66 · i | minor | "will you go on distressing us": "us" is an object the Greek does not give (the note itself says "with no object given"); the table avoids supplying objects (cf. ἀλαπάζω). | "will you go on causing distress here even now". |
| 19.66 · n | minor | "δέ joins a second question to the first" is wrong: it is one question (one ;) with two verbs. | "δέ adds a second verb to the same question." |
| 19.91 · i | minor | "you bold creature": θαρσαλέη is "bold one" (`l`, note); "creature" is the word fixed for τάλαν. | "you bold one, you unafraid dog". |
| 19.31 · n | minor | Note glossed ἐσφόρεον "they were carrying in" while `l`/`i` say "began to carry in" / "began carrying in". | Note now "‘they set about carrying in’". |
| 19.10 · n | minor | 143 words (validator band 20–130, WARN). | Trimmed to under 130 by dropping the glosses on ἔμβαλε and ἔριν στήσαντες; nothing else changed. |
| 19.73 · n | minor | 16 words (validator WARN under 20), and no comment on what the line does. | Lengthened: γάρ gives the reason for the begging; he begs because he must, which answers Melantho’s sneer. |

## Changes to gloss.json (pass 2)

Existing glossary entries were not rewritten; only the `__broaden__` block was extended, old entry kept whole.

| form · field | severity | what was wrong | what was done |
|---|---|---|---|
| φαίνοντ · entry | moderate | Parsed as impf. 3 pl. (= ἐφαίνοντο) "appeared". In the line it is present, φαίνονται with elided -αι, "appear" (19.39, and the unit note says φαίνονται). | "pres. 3 pl. mid., elided (φαίνοντ’ = φαίνονται): ’they appear’". |
| δινωτὴν · entry | moderate | Gave "wrought in circles, inlaid" and the gloss ’inlaid’ with no word of doubt: the sense is uncertain, and the table reserves "inlaid" for ποικίλος of wood and metal. | "turned in a lathe or inlaid in rings (sense not certain); fem. acc. sg. (δινέω ’turn round’)". |
| δοκοί · entry | minor | "beam, rafter"; "rafters" is kept free for other words (new-renderings row). | "beam". |
| εὐρυνόμην · entry | minor | "Ionic -ην" implies a contrast with Attic that is not there. | Dropped "Ionic -ην". |
| μεσόδμαι · entry | minor | "cross-beam, supporting beam" stated as fact; the fitting is not known. | "cross-timber of a house (exact fitting not known; also a ship’s mast-block)". |
| ἀναγκαίη · entry | minor | "= Attic ἀνάγκη" attached to the wrong thing (the form is the fem. of the adjective used as a noun). | "ἀναγκαῖος — necessary; fem. ἀναγκαίη as a noun, necessity (= ἀνάγκη)". |
| ὑπερμενέοντες · entry | minor | "of surpassing might, overbearing": "overbearing" is the word the table keeps for ὑπερηνορέοντες; no tone noted. | "of surpassing strength (with a tone of arrogance)". |
| λήθει · entry | minor | Gloss "’escapes, unseen’" is not English. | "’escapes notice’". |
| τῇ · broaden | minor | Added reading ’in which’ for the dative relative, but the unit renders "by which". | "of respect or means: ’in which, by which’ … ’the beauty by which you excel’". |
| λευκώλενοι · broaden | minor | Entry said fem. voc. pl. only; the use in the part is nom. pl. | Added "also fem. nom. pl., epithet agreeing with a noun". |
| ταμίην · broaden | minor | Entry is masc. ταμίης only; the use is the fem. ταμίη "housekeeper". | Added "also ταμίη — housekeeper, fem.; fem. acc. sg.". |
| εὐρυνόμη · broaden | minor | Entry nom. only; the use is vocative. | Added "also fem. voc. sg., in address". |
| εἴρεσθαι · broaden | minor | Entry covers only the imperatival use; the use here is the complementary infinitive after ἔμελλον. | Added "also pres. inf. mid., complementary after μέλλω: ’to ask’". |
| ἀκηδέα · broaden | minor | Entry nom. pl. only; the use is acc. pl. (agrees with the object ἔντεα). | Added "also neut. acc. pl., agreeing with an object". |
| βάλλετο · broaden | minor | Entry has only "slung on" (active sense); the use is a middle with passive sense, ἐπὶ … βάλλετο κῶας. | Added the passive-sense reading with ἐπί in tmesis. |
| ἔνθεν · broaden | minor | Entry has "thence" and "on the one side"; the use is relative, "from which". | Added "also relative, ’from which, whence’". |

All 91 novel forms are present and nothing else was added; every parse not listed above was checked against the line and stands. Existing known-form entries with doubtful labels (εἴρεσθαι "aor.", κιών "aor.") were not rewritten, per the rule.

## Checks that passed (no change)

Paragraph marks (¶ at 1, 4, 14, 16, 21, 26, 29, 36, 41, 47, 53, 70, 89, 91, 96) match `p` on exactly those units. `mark` stands on the first unit of all ten speeches and on the nested speech at 19.7. Quotation marks balance: “ at 19.4, 16, 22, 27, 36, 42, 66, 71, 91, 97 and ” at 19.13, 20, 25, 28, 40, 46, 69, 88, 95, 99; the nested ‘ opens at 19.7 and closes ’” at 19.13. Every unit whose Greek (letters only) repeats a published unit has identical `l`/`i` (19.5b–6, 19.7–9, 19.26, 19.29, 19.41, 19.53–54, 19.70, 19.78–79; and 19.51–52 equals 19.1–2). Cross-references checked in the source: 7.230, 16.48, 16.291, 17.36–37, 17.57, 17.100, 17.419–423, 18.307, 18.321, 18.327, 18.428, 5.437, 14.194, 2.424. Positions checked: 19.87 first word Τηλέμαχος, 19.99 first word ὁ ξεῖνος, 19.39 φαίνοντ’ in the third line of its unit, 19.68 θύραζε repeated at 19.69. Numbering oddities (3.304/305, 14.63/64, 10.456, 16.101, 23.49) do not fall in this part.

## Sanity checks asked for

**Merged unit 19.10–13 (accepted).** The convention ends a unit at an ano teleia, and this one runs on past the · after μνηστύν to the full stop at the end of 13 (4 lines, not over the limit). The drafter's reason holds: the one-line unit αὐτὸς γὰρ ἐφέλκεται ἄνδρα σίδηρος would have the same Greek as the published unit at 16.294 and so (validator rule 6) would have to carry the published English "…a man iron.’", closing only the inner quotation and leaving Odysseus's speech without its ”. Merging is the only way to close both marks, and the first three lines keep the published English word for word. The note says why. 19.10 itself differs from 16.291 (δαίμων for Κρονίων), so no repeated-unit rule is broken. Kept.

**Four-line unit 19.74–77 (accepted).** The source prints no stop after ἔασι at the end of 74, and the build requires a unit to end at punctuation, so 74 cannot stand alone; the unit is exactly four lines and ends at the · after 77. Lines 75–77 reuse the published English of 17.419–421 exactly; line 74 is new. The note states that no stop is printed. Kept.

## Findings considered and refused

1. 19.53–54 · l/i end in a comma although the Greek ends in a full stop. Refused: the Greek repeats the published unit at 17.36–37 (letters only), so validator rule 6 forces the published English, comma included; any change would fail the gate. The English comma reads slightly oddly before the new paragraph's next unit; noted for the owner if the rule is ever relaxed.
2. 19.62 · i "had been drinking" against `l` "were drinking". Refused: pluperfect-like English in a subordinate clause after "took away", same sense.
3. 19.56 · i "had once made it … and had set" for aorists ποίησε / ἧκε. Refused: past anterior to the narrative, same sense.
4. 19.24 · i drops ἔπειτα; 19.65 · i drops αὖτις (`l` has both). Refused: `i` may omit a weak particle or an adverb that duplicates "second time".
5. 19.99 · i "for I want to question him" against `l` "and". Refused: δέ is explanatory here; `l` is the literal layer.
6. 19.93 · "heavily" (i) against "closely" (l) for πυκινῶς. Refused: no table row; sense fits.
7. 19.16 · "lays a hand on" for ἅπτηται. Refused: idiomatic for "touch", and the note says it means eating from his stores.
8. 19.34 · note calls κάτθεσαν a tmesis "standing for κατέθεσαν". Refused: τῇ παρὰ … κάτθεσαν is a tmesis of a double preverb and the note's gloss "set beside" is true.
9. 19.38 · ὑπερμενέοντες: no change to `l`/`i` ("exceeding-strong men" / "men of surpassing strength" are the new-renderings row and the table's ὑπερμενής).
10. Scansion. The scanner marks "spondaic fifth" on 19.2 (= 19.52), 19.15, 19.21 and 19.28; the packet flags no line, nothing is UNRESOLVED or AMBIGUOUS, and a spondaic fifth foot is a recognised licence, not an irregularity of transmission. No sentence added to any note.
11. Gloss: αἶσα (with ἐλπίδος) not broadened. Refused: the existing "plain subject: ’portion, lot’" covers it.
12. Gloss: αὐτῶν (ἐπ’ αὐτῶν) and αὐτῷ (ἐπ’ αὐτῷ) not broadened. Refused: existing readings "personal pronoun after a preposition" and "plain pronoun of a thing, ’it’, after a preposition" already cover them.
13. 19.60 · note renders μῦθον as "with a word" while it is formally an accusative. Refused: it follows the table's πρὸς … ἔειπε rows and the shipped English, which the unit must match.
14. 19.46 · "wear vile clothes" in `i` against "evil clothes" in `l`. Refused: the table fixes κακός as "evil" in `l` and lets `i` vary ("vile", "foul").

## For the caller

Two cells in `new-renderings.md` were changed to match the units (ἔνθα καθέζετ’ `l` "There then sat down …"; ἐπιφροσύνας `l` "presence of mind"); copy those versions into the table. Everything else in that file stands.
