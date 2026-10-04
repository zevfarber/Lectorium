# odyssey-068 (14.199–320) — review, pass 1 of 2

Reviewer: strongest-model pass 1, adversarial. `units.json` and `new-renderings.md` were edited in place by script; no `t` character was touched. The only structural change is two re-cuts (findings 27a, 27b), which move unit boundaries over the same text; the units’ `t`, joined in order, still reproduce the archive exactly (checked against `parts.json`’s sha256 and a read-only copy of the build’s tiling test).

**Totals: 40 findings — 6 high, 19 medium, 15 low.** Severity scale: *high* = a false grammatical label, or a defect that would make the build refuse; *medium* = a departure from a ratified table row or shipped rendering, a false cross-reference or structural claim, or a misleading sense; *low* = a hedge that was missing, a wording nudge, a clarification.

## What was read, and what was not

Read in full: the rules sections of `conventions.md` (everything outside the house-renderings table), the runbook, the packet, `units.json`, `new-renderings.md`, the pilot `units.json`, the builder and validator source, and the last units of odyssey-067. The house-renderings table (about 1,600 rows) was **not read row by row**; instead every Greek word and every English rendering in this part was looked up in the table by script and in the 67 published parts (their `t`, `l` and `i`). A table row that nobody’s lookup would hit could have been missed. Murray’s English was not opened; no modern translation was opened or recalled.

Not run: `build_odyssey.py` (it has no dry-run mode). Instead a read-only copy of its checks (tiling, `ln`, `p`, line counts, terminal punctuation, five-line limit, scansion fit, token alignment) and of validator rule 6 (a unit whose Greek repeats a published unit) was run against the edited `units.json`: all clear; no unit repeats a published unit’s Greek whole. `validate_odyssey.py` will still WARN on note length for eight notes over 130 words (lines 199, 202, 217, 235, 275, 281, 295, 317); left, because the content is needed and the warning is advisory.

## Neighbouring part and quotation marks

odyssey-067’s last unit (lines 196–198, “easily … even for a whole year … by the will of the gods”) carries no closing ” in `l` or `i`: Odysseus’s speech, opened with “ at 14.191, is still running. This part carries no “ or ”, no `mark`, and the opening note says so. Correct as drafted: the speech goes on past 320 (the unit at 317–320 is mid-sentence and its note says so). No nested speech anywhere in the range.

## Changes (line · field · severity · what was wrong · what was done)

Findings are numbered; a finding that touches several fields is one finding.

1. **199 · n · medium** — False cross-reference: “its infinitive εἶναι comes at 204”. The εἶναι at 204 belongs to the second εὔχομαι (204), not to the one at 199, which has no infinitive. Note rewritten (“at 204 the same words take the infinitive εἶναι”).
2. **199, 202–204 · l, i, n · medium** — εὔχομαι rendered “claim”. The table fixes εὔχομαι as “declare” (5.450, 12.98) and lists “claim” among the avoided renderings. Now “my birth I declare” / “I declare my birth to be from broad Crete”, and at 204 “of whom I declare myself to be the offspring” / “whose offspring I declare myself to be”. (Several early parts ship “claim” for εὔχομαι εἶναι; the later table rows govern.)
3. **199 · n · low** — Κρητάων: “taken as a poetic plural of Κρήτη” stated as if explained. Now: the plural is not explained, both layers read it as the one island.
4. **200 · l, i, n · medium** — ἐξ ἀλόχου rendered “from a wedded wife”, and the note said ἄλοχος “is the lawful wife”. ἄλοχος is “wife” in every published part; “wedded” belongs to κουριδίη (14.245) and μνηστήν (1.35); legitimacy is carried by γνήσιοι. Now “from a wife” / “the legitimate sons of his wife”, note rewritten.
5. **202 · n · low** — ἰθαιγενής: “usually explained … the same γένος as in 199”, with no word on how uncertain the formation is. Now hedged (formation not certain; “lawfully born” is the sense the context gives).
6. **207 · l, i · medium** — κῆρες θανάτοιο rendered “the Keres of death” (a transliteration, kept “as a name”). The table fixes κὴρ θανάτοιο as “death-spirit” (11.171). Now l “the death-spirits”, i “the spirits of death”.
7. **207 · n · high** — False grammatical label: “ἔβαν is the unaugmented aorist of βαίνω”. ἔβαν has the augment; what is old is the ending -αν (= ἔβησαν). Fixed.
8. **207 · l, i, n · medium** — Ἀΐδαο δόμους rendered “the houses / the house of Hades”. The same words εἰς Ἀΐδαο δόμους are shipped “the halls of Hades” at odyssey-047 and odyssey-050. Now “the halls of Hades” in both layers and in the note.
9. **208 · n · low** — l says “dwellings”, i says “a house”; the note now says the plural stands for one dwelling.
10. **211 · n · low** — ἀποφώλιος: “worthless, empty; its formation is obscure”. The table records the *origin* as unknown and turns down “empty”. Now “taken as ‘worthless, good for nothing’; its origin is not known”.
11. **217 · i, n · medium** — κακὰ δυσμενέεσσι φυτεύων: i had “planting evils”. The table (14.110) keeps “planting” in `l` only and gives i “devised evil”. Now i “devising evil for the enemy”; note says which layer has which.
12. **217 · n · medium** — False structural claim: “the main clause begins with ἀλλά in the next unit”. The main clause is οὔ ποτέ μοι … προτιόσσετο θυμός, inside this unit; ἀλλά only adds the contrast. Also no reason was given for ending at a comma. Rewritten (the cut is ours; the sentence would otherwise run five lines).
13. **224 · l, i, n · medium** — νῆες ἐπήρετμοι rendered “oar-fitted / fitted with oars”; shipped “oared ships” in both layers at odyssey-019, -022, -023. Now “oared ships”.
14. **224 · n · medium** — καταριγηλά (flagged by the drafter): derivation from ῥῖγος and the sense stated as fact. The note now says the word is rare, the derivation the usual one, the sense not certain.
15. **227, 273 · l · low** — ἐνὶ φρεσίν rendered “in my wits”; shipped “in … minds” in `l` at odyssey-002, -019, -021, -032 (“wits” is the shipped rendering of the other φρεσίν/φρένες phrases). Now “in my mind” at both places.
16. **228 · l, n · low** — ἄλλος … ἄλλοισιν: “in other works” reads as “other than his own”; the note called the pair “one man … another”, but the second ἄλλος is in the works. l now “in different works”; note corrected.
17. **232 · n · high** — False grammatical label: “ἐξαιρεύμην is the optative middle of ἐξαιρέω … used without κε”. An optative would be ἐξαιροίμην; ἐξαιρεύμην is the imperfect middle with Homeric -ευ- for -εο-, iterative in force and parallel to λάγχανον in the next line. Note rewritten; the “without κε” explanation dropped. (Confidence: high but not certain of the dictionary’s own label; the sense and the English are unaffected.)
18. **238 · l, i, n · medium** — μῆχος rendered “means / no way”; the table (12.392) and odyssey-061 fix “remedy” and turn down “means” and “way out”. Now “remedy” / “there was no remedy, no way to refuse”.
19. **243 · i, n · low** — κακὰ μήδετο: i “devising evils”; the table’s i is “devising evil”. Changed in i and in the note; l keeps “evils”.
20. **250 · l, i, n · medium** — ἱερήϊα rendered “sacrificial victims / animals for sacrifice”; the table (11.23) and odyssey-051, -066 fix “victims” and turn down “sacrificial animals”. Now “victims”.
21. **250 · l, i · medium** — ῥέζειν (of sacrifice) rendered “offer”; the table (12.344) fixes “sacrifice” and lists “offer up” as avoided. Now “for the gods to sacrifice” / “for them to sacrifice to the gods”.
22. **252, 299 · l, i, n · medium** — ἀκραής rendered “brisk”; shipped “fresh” (odyssey-008, ἀκραῆ Ζέφυρον “the fresh West Wind”). Now “a fresh, fine wind” at both occurrences, in both layers, and in the note.
23. **257 · l · low** — ἀμφιελίσσας rendered “curved-on-both-sides”; the table row (6.264) gives l “both-sides-curving” (odyssey-029, -030 ship it so; odyssey-010 has the older form). Now “both-sides-curving”.
24. **265 · n · low** — ἵκετο called “the unaugmented aorist”; the form can be read as aorist or imperfect. Now “an unaugmented past tense”.
25. **273 · l · medium** — ἐμοί rendered “in me”, doubling the “in” of ἐνὶ φρεσίν (“but in me Zeus himself in my wits”). ἐμοί is a dative “to/for me” (cf. 310 “but to me Zeus himself”). Now “but to me Zeus himself in my mind”.
26. **273–275 · n · medium** — ὑπέδεκτο (flagged): the note explained the aorist as “the woe had, as it were, already taken him up”, an unsupported gloss. Now: literally “for still woe received me”; a past “received” sits oddly with “still”; “was waiting to receive me” is a reading from the sense; the tense is not clearly explained.
27a. **202–206 · t boundary · high** — The unit 202b–204 (`ἐμὲ δ’ ὠνητὴ … εἶναι`) ended at no punctuation (after εἶναι, where the source prints none); `build_odyssey.py` refuses a unit that does not end at `. ; · ,`. Re-cut at the comma after Κάστωρ Ὑλακίδης: unit A = 202b–204a (ends at the comma), unit B = 204b–206 (ends at the full stop). No character moved. l, i and n split accordingly; B’s `i` begins “whose offspring I declare myself to be, and who in those days …”. The count of units is unchanged (the old 205–206 unit was absorbed into B).
27b. **273–277 · t boundary · high** — The unit 273–275 ended at the closing dash of a parenthesis (`ὑπέδεκτο—`), which the builder also refuses. Re-cut at the raised dot printed after αὐτοῦ ἐν Αἰγύπτῳ· (mid-275): unit A = 273–275a, unit B = 275b–277 (`ἔτι γάρ νύ με πῆμ’ ὑπέδεκτο—αὐτίκ’ … χειρός·`, which absorbs the old 276–277 unit). The parenthesis therefore straddles two units; the note on A says so. Unit count unchanged.
28. **292 · l, i, n · medium** — τελεσφόρον εἰς ἐνιαυτόν rendered “a year, completion-bringing” / “a complete year”; the table (10.467) and odyssey-049 fix l “for a completion-bearing year”, i “for a full year”. Now so.
29. **295 · l, i, n · medium** — ποντοπόροιο rendered “open-sea-faring” / “sea-going”; the table (12.69) fixes “sea-crossing” in both layers and turns down “sea-going”. Now “sea-crossing”.
30. **295 · l, i, n · medium** — ἄσπετον ὦνον rendered “unspeakable / enormous price”; the table (9.162, 13.395) and odyssey-063, -065, -066 fix ἄσπετος as “boundless”, and the table lists “unspeakable” among the avoided renderings (11.61). Now “a boundless price”.
31. **295 · n · low** — ἐέσσατο (flagged): the link with ἵζω was stated as fact; now “is taken as … the form is unusual and the sense comes from the context”.
32. **299 · n · low** — μέσσον ὑπὲρ Κρήτης (flagged): the note already said the sense is not clear; made explicit that the English “midway above Crete” is a literal reading, not a solved one. English left (see refused list).
33. **309 · n · high** — False grammatical label: “ἀποαίνυτο is the unaugmented aorist middle of ἀπαίνυμαι”. ἀπαίνυμαι is a present-stem verb; ἀποαίνυτο is its imperfect. Fixed.
34. **314 · n · low** — The note dropped νυκτί from “the tenth”: δεκάτῃ agrees with νυκτί (the tenth night). Note corrected; i left (“on the tenth, in the dark night”) since the table fixes “dark night”.
35. **316 · n · low** — ἀπριάτην (flagged): “used as an adverb” named no form. Now: feminine accusative singular of ἀπρίατος with nothing to agree with, so adverbial; the traditional reading, not certain.
36. **317 · n · high** — False grammatical label and unsupported sense for αἴθρῳ (flagged): the note said “where αἴθρη is clear sky and so, here, the chill”; αἴθρῳ cannot be a dative of the feminine αἴθρη, and the sense was given as fact. Now: a dative of a word related to αἴθρη “clear sky”, understood as the cold clear air brings; the sense not certain. The same note now gives the reason the raised dot at 319 sits inside the unit (see refused finding A).
37. **about · low** — “the king keeps him in Egypt for seven years”: lines 285–286 say Odysseus stayed and gathered goods because they all gave; they do not say the king kept him. Now “the king spares him; he stays seven years in Egypt, gathering gifts”.
38. **220 · i, n · low** — πόδεσσιν rendered “on foot”, which reads as foot-soldiers against chariots, a contrast the Greek does not make. Now “gave ground before me with his feet”; note matches.
39. **new-renderings.md · medium** — Eight rows duplicated or contradicted a table row or a shipped rendering (Κρήτη εὐρεῖα, κῆρες θανάτοιο, Ἀΐδαο δόμοι, Ζεὺς ξείνιος, ἄσπετος, τελεσφόρος ἐνιαυτός, ποντοπόρος, ὕβρις): removed, with the reason listed in the file’s last paragraph. Rows for ἀκραής and φρεσίν changed to match findings 15 and 22; “counsellor Zeus” and “fair-flowing Egypt” rows annotated with their overlaps (μήστωρ; καλλιρόος). Rows added for the new recurring or uncertain items: γένος εὔχομαι, ἰθαιγενής, τρώκτης, καταριγηλός, ἀπριάτην, οἰκωφελίη, ῥηξηνορίη.
## Findings considered and refused (or accepted as drafted)

A. **Drafter’s choice (a): line 320 folded into the 317b–320 unit — accepted.** Line 320 is a stock line shipped in odyssey-050 (unit at 542) with “she put on me”. A unit of its own would have the same Greek as that unit, and validator rule 6 would force exactly “she”, false here, where the king’s son is the subject. Folding keeps `t` exact, makes the unit four lines (within the five-line limit), and lets the subject (τοῦ … υἱός) stand in the same unit as ἕσσεν; the builder allows a raised dot inside a unit. Cost: this unit does not end at the first raised dot (319); the note says so. The `l` and `i` change “she” to “he” and nothing else.
B. **μέσσον ὑπὲρ Κρήτης — English kept.** “Midway above Crete” is the literal reading; no alternative (“straight over Crete”, “past Crete”) is better supported by the grammar, and each would pick one geography. Honest marking is in the note (finding 32).
C. **τρώκτης “gnawer” / “rogue” — accepted** with the note’s “sense not secure” and a new table row; l keeps the root, i the traditional sense.
D. **ἀμαιμάκετος “huge” — accepted.** The note already says the meaning is unknown and that “huge” and “irresistible” are guesses; the row says so.
E. **“counsellor Zeus” / “Zeus the counsellor” — accepted**, with the overlap with μήστωρ (shipped “counsellor”, odyssey-010 and -013) recorded in the row. The two words share a root and mean one who plans; alternatives (“wise”, “of the counsels”, “the planner”) are each already reserved or too interpretive.
F. **“fair-flowing Egypt” — accepted.** ἐύ- is “fair” in the table’s epithets (ἐυστέφανος, ἐύθρονος, ἐυῶπις); “fair-flowing” is also the shipped English of καλλιρόοιο and καλλιρέεθρον, which is a different compound, recorded in the row.
G. **“broad Crete”, “the god of guests” (Zeus ξείνιος) — accepted as drafted**, because they match existing table rows (13.256; 9.271); their new-renderings rows were removed as duplicates.
H. **Notes that cite formulas elsewhere in the poem** (ἱππότα in Γερήνιος ἱππότα Νέστωρ at 243; πεπνυμένα μήδεα εἰδώς at 288) — kept. Both are shipped formulas (odyssey-009 etc.; odyssey-005, -020) used as grammatical parallels, not claims about this part, and both were checked true.
I. **νήπια τέκνα “little children” in i** against the table’s νήπιος “an infant” (11.449) — not changed: that row is for the singular baby; the plural of grown-up’s children is a different use. “Infant children” stays in l.
J. **Scansion.** The packet flags nothing; the scanner reports a spondaic fifth foot at 199, 211, 239, 246, 252, 256, 311, a recognised licence and not an irregularity as transmitted; no UNRESOLVED or AMBIGUOUS flag. No sentence added to any note.
K. **Murray’s line-numbering irregularities** (3.304/305, 14.63/64, and the omitted 10.456, 16.101, 23.49) — none falls in 14.199–320.
L. **Repeated lines.** The English of 14.249, 256, 293–294, 302–304, 306, 308–309 and 320 was compared word for word with the shipped parts: identical where the Greek is identical; at 301 the order “Crete we were leaving” replaces “we were leaving the island”, as the note says; 320 differs only in “he”.
M. **Remembered English in `i`.** Read for phrases that arrive formed; none found that is not rebuilt from the grammar. “Would that I had died” and “such a man I was in war” are the plain English of ὡς ὄφελον θανέειν and τοῖος ἔα; left.
N. **ὤμοιϊν “a dual genitive”; ἐμφορέοντο “a verb meaning ‘carry about, toss’”** — not changed; the first is the usual explanation and works as the genitive of separation after ἀπό; the second names no lemma but is not false. Flagged for the second pass if the glosser parses ἐμφορέοντο.

## For pass 2

`gloss.json` has not been written yet; the second pass should check every parse against the line, with attention to the forms whose labels changed here: ἔβαν, ἐξαιρεύμην, ἀποαίνυτο, αἴθρῳ, ἀπριάτην, ἵκετο, κῆρες, ὑπέδεκτο, ἐέσσατο.

# Pass 2 of 2

Reviewer: strongest-model pass 2. `units.json` and `gloss.json` edited in place by script; no `t` character was touched (the list of `t` strings was compared before and after the write). The full pass-1 checks were re-run over `units.json` as it now stands (labels, l↔i, quotation marks, unit endings, repeated lines against the published parts by script), and every parse in `gloss.json` was read against the line where the form occurs. The build was not run.

**Pass 2 totals: 21 findings — 3 high, 7 medium, 11 low** (P2-8, P2-23 and P2-24 are checks with no change and are not counted).

## Units

P2-1. **265 · n · high** — ἵκετ’ was called “an unaugmented past tense”. The line scans with a long ι (`ἵκετ’`, no licence needed), and the shipped glossary entry for ἵκετ states that the long ι is the augment. Now: “a past tense of ἱκνέομαι ‘come’; the ι is long here, and that long ι is the augment.” (ἵκετο at 319 also scans long; the note there makes no claim.) The existing glossary entry for ἵκετ already covers both readings, so no broadening is needed.
P2-2. **204 · n, l · medium** — τοῦ called “the relative ‘of whom’”, with ὅς then “picking up Κάστωρ”: two relatives for one clause. τοῦ is the demonstrative pronoun (‘of him’, Castor) and ὅς is the relative that follows it. Note now says so; `l` “of whom” became “of him”; `i` left (the English relative reads naturally).
P2-3. **275 · n · medium** — ὤμοιϊν stated flatly as “a dual genitive” with “the verb ἔθηκα serves for it”, which is a construction guess. Now: “read as a dual, ‘from my two shoulders’, taken as a genitive with the ἀπὸ of ἀπὸ … ἔθηκα carried over; the case is not certain.” (Pass 1 refused this; refused no longer, because the parse is not secure and the gloss now carries the same hedge.)

Re-checks that found nothing new: every “unaugmented” claim on a vowel-initial verb (ἄγεν, ἄγειρα, ἄγον, ἄναγον, ἀποαίνυτο, ὀφέλλετο, προτιόσσετο, ἐξαιρεύμην, ἄγε) was tested with the scanner on the full line and the initial vowel scans short in each, so the claim is true; ὠπίζετο, ἠγαγόμην, ὤτρυνα, ἐπήϊσσον scan long and are called augmented. Line-number cross-references (237, 246, 253, 260, 268, 272, 280, 299, 305) were counted against the lines and are true. Repeated lines (249, 254, 293–294, 301–304, 306, 308–309, 317 half) match the shipped English except where the notes say otherwise. No quotation mark is open or closed in this part, none is needed. All units end on a raised dot, comma, full stop or dash.

## Glosser output (gloss.json)

The named concerns:

P2-4. **αἴθρῳ · high** — filed under αἴθρη, which cannot be the lemma of a masculine/neuter o-stem dative. Now filed under αἴθρος with the sense ‘cold, frost, the chill of the open air’, and the entry says the lemma and sense are not certain and that the word is related to αἴθρη ‘clear sky’. I am not sure of the dictionary form or of the accent (αἶθρος and αἴθρος are both written for the word); the sense is the one the line requires (αἴθρῳ καὶ καμάτῳ, ‘by cold and by weariness’), and the unit’s note already hedges the same way.
P2-5. **ὑπέδεκτο (broadened) · medium** — the old entry’s “unaugmented” is false (ὑπ-έ-δεκτο is augmented), and the combined entry then contradicted its own last clause (“augmented (ὑπ-έ-δεκτο, 2nd aor.)”). The one word in the old entry was corrected; everything else of the old entry is whole, and the new reading is unchanged. This is the only change made to an old entry.
P2-6. **ὤμοιϊν · medium** — “dual of the two shoulders” was stated as fact. Now ‘masc. dual (epic ὤμοιϊν = Attic ὤμοιν), taken as a gen. of separation with ἀπό carried over’, ending ‘the dual and the case are the usual reading, not certain’.
P2-7. **ἀπριάτην · medium** — lemma accented ἄπριατος (it is ἀπρίατος); the translation ‘without ransom’ gave a different idea (ransom is ἄποινα); “not agreeing with the masc. ἥρως” named the wrong noun (ἥρως is a nominative subject; the accusative would have to agree with με, which is masculine). Now: “fem. acc. sg. used as an adverb (it cannot agree with masc. με or ἥρως): ‘without price, freely’; the usual explanation, not certain.”
P2-8. **κῆρες · none** — checked: κήρ ‘death-spirit’ (fem., pl. κῆρες) is a different word from neuter κῆρ ‘heart’, which has no plural κῆρες; the entry says so and is true of the line (nominative plural, subject of ἔβαν, with φέρουσαι agreeing). Kept.
P2-9. **ἐξαιρεύμην · low** — parse true (imperfect middle, -ευ- for -εο-, Attic ἐξῃρούμην); the entry now also says ‘unaugmented’ to match the note.
P2-10. **ἐέσσατο · low** — accepted as the augmented aorist middle of the causative ἵζω (ἐ + Fέσσατο); the entry now says the form is unusual and the sense comes from the context, as the unit’s note does.

Other parses corrected:

P2-11. **ἔβημεν · high** — “aor. 1 pl. athematic (= ἔβημεν, Attic ἐβήσαμεν in the transitive sense)” was false: ἔβημεν is itself the ordinary Attic form, a root aorist, and ἐβήσαμεν is a different (causative) first aorist. Rewritten.
P2-12. **ὠκυπόροισι · medium** — “(= Attic -αις)”: ὠκυπόρος is a two-ending adjective, so the feminine dative plural is -οις in Attic. Fixed.
P2-13. **μένεϊ · medium** — “dat. of cause: ‘with their own impetuosity’” for ἐπισπόμενοι μένεϊ σφῷ; the dative is the object of ἐπισπόμενοι (‘following’), as the note says. Entry and gloss now agree (‘their own might’).
P2-14. **ἀνέμῳ · low** — “dat. of means” alone; Βορέῃ is the dative of means and ἀνέμῳ stands in apposition to it. Fixed.
P2-15. **ἕλεσκον · low** — “(= Attic ᾕρουν)” is not an equivalent of an iterative; removed.
P2-16. **ὀφέλλετο · low** — “(= ἀφέλλετο/ὠφέλλετο)”: ἀφέλλετο is not a form. Now “= ὠφέλλετο”.
P2-17. **καλῷ · low** — glossed ‘fair (wind)’, which clashes with the house reservation of ‘fair wind’ for another phrase and with `i` “fine”. Now ‘fine (wind)’.
P2-18. **μητίετα · low** — ‘counselling’ in the meaning, ‘counsellor’ in `l` and `i`. Aligned.
P2-19. **ἀμαιμάκετον · low** — entry put ‘huge’ first with ‘irresistible’ as “traditional”; the note says both are guesses. Aligned.
P2-20. **πλούτῳ, ὄλβῳ · low** — “dat. of respect” alone; the note calls the datives the grounds of the honour. Now “dat. of respect or cause”.
P2-21. **σφῷ · low** — “neut./masc.” where the line has a neuter (agreeing with μένεϊ). Now neut.
P2-22. **ἰθαιγενέεσσιν · low** — entry gave ‘born in lawful wedlock’ as certain; the note says the formation is not certain. Hedge added.

Checked and kept (no change): the remaining novel entries, parsed against their lines (including δίδοσαν, πημάνθη, στεῖλα, μεῖνα, κύσα, πόρθεον, κεχολώατο, παρπεπιθών, τεταρπόμενος, κυλίνδον, περιπλεχθείς, ἐσαγείρατο, ἔκβαλον, ἄναγον, ἀπέκτανον, σφίσιν); σφίσιν “(= Attic αὐτοῖς)” follows the shipped entry for σφισι. All 20 broadened entries were read against the line: the new readings are true of the places they cover (αἰγύπτῳ, αἰδοῖός, γένος, εἰσορόωντα, εἴ, ζωὴν, λάγχανον, μεῖναι, μέσσον, πῆμ, φίλ, φίλαι, ἀλόχου, ἄγον, ἔα, ἑλών, ῥέζειν, βάλεν, τήν); each keeps its old entry whole. Coverage: every word form in the part has an entry in the shipped glossary, `gloss.json`, or `__broaden__`. All new entries are under 230 characters, use ’ only, and carry no line numbers.

P2-23. **gloss format · none** — no ASCII apostrophe, backtick or line number in any entry; `__broaden__` entries begin with the old text.
P2-24. **review.md / new-renderings.md · none** — no new recurring rendering arose; `new-renderings.md` unchanged (the τοῦ change in `l` touches no row).
