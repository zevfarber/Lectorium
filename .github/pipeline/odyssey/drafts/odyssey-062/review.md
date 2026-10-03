# Review — odyssey-062 (13.1–112)

Reviewer: adversarial, two passes. Files read: conventions.md in full, runbook.md, packet.md, units.json, new-renderings.md, odyssey-001 draft units, known-forms.json, novel-forms.json, gloss.json (pass 2), published odyssey-001 … 061 (root) for cross-references, repeated lines and shipped wording. No modern translation was opened or recalled. `t`, `ln`, `p`, `mark`, title, titleEn and part were not touched (checked by script against a copy of the draft: every `t` identical).

## Counts

| | high | medium | low | total |
|---|---|---|---|---|
| Pass 1 (units.json, notes, l, i) | 0 | 11 | 22 | 33 |
| Pass 2 (units.json residue, gloss.json, new-renderings.md) | 0 | 5 | 12 | 17 |
| **Total** | **0** | **16** | **34** | **50** |

High = Greek sense wrong in `l`/`i`; medium = a grammatical or positional claim false, a wrong cross-reference, `l`/`i` against the table or against shipped English, or a build blocker; low = polish, consistency, over-claim. Nothing high was found: the Greek→`l` pass (case relations, tense, mood, particles, every unit, word by word) found one real `l` fault (13.4 τῷ). Refused findings: 13.

State after the second pass: tiling, `l` line counts, `p`, speech marks (4 “ and 4 ” in each of `l` and `i`: speeches at 13.4–15, 13.38–46, 13.50–52, 13.59–62; the previous part ends its speech with ”, so 13.1 opens narration), note word-bands and glossary shape all check clean by script; gloss.json covers every form of the part (155 new entries, 15 broadenings, each broadening contains the old entry whole, no entry over 229 characters, no ASCII apostrophe or backtick). I did not run build_odyssey.py or validate_odyssey.py (they write to the repository root).

## Pass 1 — changes to units.json

| # | line · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | 13.1 · n | low | Note glossed ἀκήν as 'in silence', duplicating σιωπῇ and contradicting `l` 'still in silence'. | ἀκήν glossed 'still, hushed'; 'say nearly the same thing twice'. |
| 2 | 13.4–6 · l | medium | τῷ rendered 'so that you…', a purpose clause the Greek does not have; τῷ is 'therefore' (the note itself said so). | l now 'therefore you, driven astray again, I do not at all think …'. |
| 3 | 13.4–6 · n | low | Claimed δῶ is 'found only in this shape': a claim about the rest of the poem that this part cannot show. Also over the 130-word band. | Claim removed; four dispensable clauses trimmed (note now within band). |
| 4 | 13.7–9 · i | low | αἴθοπα οἶνον rendered 'wine, with its look of fire'; the four shipped occurrences (2.57, 3.459, 7.295, 9.360) and the table row say 'the wine that has the look of fire'. | i now 'the elders’ wine that has the look of fire'. |
| 5 | 13.10–12 · n | low | Said εἵματα 'takes the singular verb κεῖται'; κεῖται serves the whole list (εἵματα, χρυσός, δῶρα). | Note says so. |
| 6 | 13.26 · n | medium | Labelled κήαντες 'uncontracted Homeric shape'; it is the Homeric aorist stem κηα- (Attic καύσαντες), not an uncontracted form. The known glossary entry says the same. | Label corrected. |
| 7 | 13.31–32 · i | low | ἕλκητον (present, 'drag') rendered 'have dragged'. | 'have been dragging … all day long'. |
| 8 | 13.31–32 · n | low | Said the colour of οἴνοπε 'is a dark one'; the table treats the colour of οἶνοψ as unknown. | 'whose exact colour is not known'. |
| 9 | 13.33 · i | low | ἀσπασίως rendered 'gladly'; the table row (8.450, 10.131) fixes `i` 'with joy' (`l` 'gladly'). | i now 'and with joy for him the light of the sun goes down'. |
| 10 | 13.36–37 · n | low | Asserted πιφαυσκόμενος is 'a reduplicated present of φάσκω'; the derivation is not certain. | Derivation claim dropped; meaning kept. |
| 11 | 13.38 · n | medium | Note contained backticks (`l`, `i`); the validator fails any note with a backtick, so the build would have refused. | Replaced by 'the literal English' / 'the free English'. |
| 12 | 13.38–39, 13.59 · n | low | Notes gloss χαίρετε / χαῖρε as 'rejoice', which the table reserves and which contradicts `l` 'be glad'. | Both notes now say 'be glad'. |
| 13 | 13.42–43 · n | low | ἀρτεμέεσσι glossed 'sound, unharmed'; 'unharmed' is reserved for ἀπήμων of persons (new-renderings row says so). | 'sound, whole'. |
| 14 | 13.45–46 · l, i, n | medium | μεταδήμιον rendered 'among the land' (not English) and 'befall the land'; the note said 'among the community'. Shipped 8.293 (odyssey-036) renders the same word 'among the people', so the new-renderings row also contradicted shipped English. | l and i 'no evil among the people'; note cites 8.293; row 'μεταδήμιος' rewritten to follow the shipped `l`. |
| 15 | 13.53–54 · l, i, n | low | ἐπισταδόν rendered 'standing close by (each)'; shipped 12.392 (odyssey-061) and the table say 'standing by each' / 'standing by each man'. | l 'standing by each', i 'standing by each man', note adjusted. |
| 16 | 13.56–58 · n | low | Note asserted a custom ('the way the departing guest honours the hostess') that nothing in the line shows. | Removed. |
| 17 | 13.66–68 · l | medium | τὴν δ’ ἑτέρην rendered 'the other'; table row 1109 says the Greek counts and 'the other' is avoided for ἑτέρη (the next unit's ἡ δ’ ἄλλη is 'the other'); two 'the other' in succession blurred who carries what. | l now 'and the second a solid chest gave along to carry' (matches the `i` and the note). |
| 18 | 13.73 · l, i | low | λίνον rendered 'linen sheet' while the note and the table (λῖτα) say 'linen cloth'. | 'linen cloth' in both layers. |
| 19 | 13.75 · n | low | Tmesis note gave the whole verb as ἀνέβη; the form is ἀνεβήσετο. | Corrected. |
| 20 | 13.78 · i | low | ἅλα πηδῷ rendered 'with their oar-blades'; shipped 7.328 (odyssey-032) has `l` 'the oar-blade', `i` 'the oar'. | i now 'with the oar'; new-renderings row πηδόν rewritten to cite the shipped pair. |
| 21 | 13.81–83 · n | medium | Stated 'The tenses are present'; ὁρμηθέντες is an aorist participle. | Note now says the main verb is present and ὁρμηθέντες an aorist participle. |
| 22 | 13.84–85 · l, i, n | medium | πορφύρεον of a wave rendered 'purple'; the shipped renderings of the same collocation are 'surging' (2.428, 11.243) and the glossary entry says 'not a colour term here'. The note called it 'purple'. | l 'surging', i 'a great surging wave … came rushing' (θῦε), note rewritten with both cites. |
| 23 | 13.84–85 · n | low | Note gave πολυφλοίσβοιο as 'loud-roaring' where `l` has 'much-roaring'. | Both given. |
| 24 | 13.88–92 · n | medium | 'The relative clause that began in line 89': ὃς πρὶν … begins in line 90 (89 describes the man). | Corrected. |
| 25 | 13.90–91 · n | medium | Cross-reference 'repeated from 8.182' (inferred, not looked up) is wrong: ἀνδρῶν τε πτολέμους ἀλεγεινά τε κύματα πείρων is 8.183 (odyssey-034 unit 182 opens on πολλὰ γὰρ ἔτλην, the second half of 8.182). | 8.183. |
| 26 | 13.93–95 · n | medium | 'Ithaca … is named in the next line': it is named in 97, two lines on. | 'two lines on, at 97'. |
| 27 | 13.93–95 · n | low | Claimed προσεπίλνατο has 'two preverbs'; from the permitted sources I cannot tell whether ἐπι- is a second preverb or the augment after προσ-. | Claim removed ('a compound aorist of πίλναμαι'). |
| 28 | 13.26–27 · l, i | low | ἐρικυδέα δαῖτα rendered 'the glorious feast' / 'feasted on the glorious feast'; table row and shipped 3.66 and 10.182 give 'a glorious feast' / 'feasted a glorious feast'. | Conformed in both layers. |
| 29 | 13.27–28 · i | low | ἐμέλπετο θεῖος ἀοιδός rendered 'the divine minstrel sang'; the half-line is shipped at 4.17 (odyssey-014) as 'was making music'. | i 'the divine minstrel was making music'. |
| 30 | 13.102–104 · l, i, n | medium | ἐπήρατος rendered 'lovable' / 'pleasant'; shipped 4.606 (odyssey-019) and 8.366 (odyssey-036) render it 'lovely' in both layers, so the 'new' row was not new. | 'lovely' in both layers, note adjusted, row rewritten with the cites. |
| 31 | 13.107–108 · n, i | low | θαῦμα ἰδέσθαι: `i` 'a wonder to see' where the shipped half-line (8.366) has 'a wonder to behold'; φάρε’ 'cloths' beside φᾶρος 'cloak' (67) was unexplained. | i 'a wonder to behold'; note ties φάρεα to φᾶρος. |
| 32 | 13.4–6, 13.20–22, 13.81–83 · n | low | Three notes exceeded the validator's 130-word WARN band (147, 131, 136 words). | Trimmed to within band without losing a claim the line needs. |
| 33 | all units · l, i, n, about | low | ASCII apostrophes and straight single quotes (947 in notes, 7 in l/i, 1 in `about`); recent shipped parts use typographic ‘ ’ / ’. | Converted to ‘ ’ and ’; Greek untouched. |

## Pass 2 — second read of every unit, then gloss.json, then new-renderings.md

The second read of units.json (all 60 units, notes against `l`/`i` and the Greek again) turned up the items marked above that were not caught in pass 1: the backticks in the 13.38 note, the shipped-wording conflicts (13.26–28, 13.84, 13.102, 13.107), the ‘next line’ claim at 13.93 and the over-long notes. gloss.json (written concurrently, read at 07:00) was checked entry by entry against its line; the glossary corrections and the new-renderings corrections follow.

| # | line · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | gloss: μένος (broaden) · gloss.json | medium | Added reading ‘the mighty Alcinous’, which the table row ἱερὴ ἲς / μένος Ἀλκινόοιο explicitly avoids (erases the periphrasis). | Reading now ‘the sacred strength of Alcinous’, a periphrasis for Alcinous himself. |
| 2 | gloss: ἐλαφρότατος · gloss.json | medium | ‘light, swift … ’swiftest’’ contradicts the new row (swiftest is avoided; `l`/`i` ‘lightest’). | ‘light, nimble … ’lightest’’. |
| 3 | gloss: οἴνοπε · gloss.json | medium | ‘wine-dark, wine-coloured’ contradicts the shipped οἴνοπα entry and the house rendering ‘wine-faced’ (colour unsettled). | Aligned with the shipped οἴνοπα entry. |
| 4 | gloss: εὐήνορα · gloss.json | low | Gave ‘manly, stout’ only; the unit reads it as εὖ + ἀνήρ ‘good for men’. | ‘good for men, manly (εὖ + ἀνήρ; …)’. |
| 5 | gloss: λίνον, παισί · gloss.json | low | Both said ‘accented before enclitic’; neither accent is enclitic-induced (λίνον and παισί are accented as written). | Claims removed. |
| 6 | gloss: προσεπίλνατο · gloss.json | low | Lemma προσπίλναμαι with ‘προσ-ε-πίλνατο’ contradicted the unit note’s preverb count and the shipped ἐπιπίλναμαι entry. | Lemma πίλναμαι, ‘in compound’, no preverb count. |
| 7 | gloss: ἰόντι (broaden) · gloss.json | low | Known entry gives only ‘for you, going’ / ‘for me, as I went’; here it is ‘for him, as he goes’ (the ploughman). | Reading added. |
| 8 | gloss: ἕκαστοι (broaden) · gloss.json | low | Known entry ‘each of us’; here a third party, ‘each man’. | Reading added. |
| 9 | gloss: γερούσιον · gloss.json | low | Added ‘of wine drunk at the elders’ table’, pinned to the line and not in the Greek. | Trimmed. |
| 10 | gloss: Ἀρήτῃ, ἑτέρην, κληῗσιν, ἀειρόμενοι, προικὸς, αἱ (broaden) · gloss.json | low | Respectively: redundant ‘Ἀρήτῃ’ in its own parse; ‘the other (of two)’ and ‘epic -ην’ for ἑτέρην (house ‘second’, Ionic η); ‘= Attic κληῖσι’ is not Attic and the sense list differed from the shipped κληῖσιν entry; ‘bounding up’ for ἀειρόμενοι; ‘at one’s own cost’ for προικός (unit: ‘with no return’); ‘the one set’ in the αἱ μέν … αἱ δ’ reading. | Each tidied in place (see gloss.json). |
| 11 | new-renderings: μεταδήμιος · new-renderings.md | medium | Row contradicted shipped 8.293 (see 13.45–46 above). | Rewritten: `l` and `i` ‘among the people’, cite and reason. |
| 12 | new-renderings: ἐπήρατος · new-renderings.md | medium | Row claimed ‘lovable’/‘pleasant’ as new, against shipped ‘lovely’ (4.606, 8.366). | Rewritten to ‘lovely’ with cites. |
| 13 | new-renderings: πηδόν · new-renderings.md | low | Row contradicted shipped 7.328 (`i` ‘the oar’). | Rewritten with cite. |
| 14 | new-renderings: βουληφόροι · new-renderings.md | low | Chose ‘counsellors’ and listed ‘councillors’ as avoided: the same word in two spellings. | Avoided list now ‘senators’. |
| 15 | new-renderings: εὐήνωρ · new-renderings.md | low | ‘also of wine’: remembered from outside this part, unverified. | Removed. |
| 16 | new-renderings: χαῖρε · new-renderings.md | low | Header cited ‘13.43–46 context’ (no χαίρ- there) and omitted the shipped 5.205 ‘farewell’. | Header corrected, 5.205 cited. |
| 17 | new-renderings: ἀενάων · new-renderings.md | low | ‘perennial (reserved for ἐπετήσιος)’: the table lists perennial as turned down for ἐπετήσιος, not reserved. | ‘turned down for ἐπετήσιος’. |

Parses checked and found right (no change): every remaining novel entry, including the aoristic and optative parses (βλάπτοι, εὕδοι, εὕροιμι, ὁμαρτήσειεν, ποιήσειαν, ὀπάσειαν, ἐϋφραίνοιτε, σπερχοίατ’, ἵκωνται, ἕλκητον), the elided forms (κατέθηχ’, πάθ’, τισόμεθ’, δῶρ’, μήδε’, σπερχοίατ’), diectasis (σκεπόωσι, παμφανόωντα), the datives in -εσσι/-ῃσι, and the 13 original broadenings (αἱ, αὐτοί, μένος, κακὸν, οἱ, ἡ, πρὸς, θανάτῳ, ἵστατο, βουληφόροι, περιμήκεες, παμφανόωντα, ἱρὸν). New-renderings: 28 data rows (29 table lines with the header), checked against the table and the shipped parts; the rows not mentioned above are consistent.

## Findings considered and refused

1. **13.5–6 οὔ τι … ὀΐω (drafter's unverified claim)** — Checked. οὔ τι is the negative of ὀΐω ('I do not think'), with σε … ἀπονοστήσειν as accusative + future infinitive and παλιμπλαγχθέντα agreeing with σε. The note's labels are true of the form in this line, `l` follows the Greek order, and `i` conveys it ('I do not think you will be driven off course again on your way home'). The only defect found at 13.4–6 was τῷ ‘so that’ in `l` (changed, above).
2. **13.1 ἔφαθ’ / 13.20 κατέθηχ’ aspiration note (drafter's unverified claim)** — Checked and true. ἔφατο → ἔφατ’ → ἔφαθ’ before οἱ (rough breathing, across the comma, as Murray prints and as the shipped note at 11.333 explains); κατέθηκε → κατέθηχ’ before ἱερόν (rough). Both notes say exactly this. No change.
3. **13.59 `i` ‘all your days’ for διαμπερές** — Considered a conflict with the table's ἤματα πάντα ‘for all your days’. Refused: the phrases differ, the sense (‘continuously, until old age and death come’) is right, and ‘all your days … until old age’ is not redundant in English. Left.
4. **13.86–87 οὐδέ κεν … ὁμαρτήσειεν ‘could have kept up’** — Aorist optative + κεν is a potential that Homer uses of past scenes; ‘could have kept up’ (`l`) and ‘could have kept pace’ (`i`) are acceptable and agree with the note. Left.
5. **13.93 φαάντατος ‘brightest’ (row says ‘most shining’ is reserved for φαεινός)** — φαάντατος is the superlative of φαεινός, so the row's reasoning is loose, but ‘brightest’ is the natural English, does not collide with φαεινός ‘shining’ or φαέθων ‘shining’, and ἀργῆτι ‘bright’ shows ‘bright’ is not fenced off. Left (the row is harmless).
6. **13.63 ὣς εἰπών `i` ‘So he spoke’** — Table row 465's own `i` is ‘So he spoke’ although its avoided column lists the same words; the draft follows the row's `i`. Left. The owner may want to reconcile row 465.
7. **13.76 κόσμῳ `i` ‘each man in his place’ (table 911 has ‘in very good order’ for κατὰ κόσμον)** — A different phrase and a fair paraphrase of ‘in order’; `l` keeps ‘in order’. Left.
8. **13.27 λαοῖσι ‘peoples’ (`l`) / ‘the people’ (`i`); 13.38 λαῶν note ‘peoples’ vs ‘people’** — Literal plural in the note and `l`, idiomatic singular in `i`; both are in the table's range. Left.
9. **13.9 γερούσιον ‘the elders'’** — ‘of the elders’ is the lexical sense (γέροντες); no change.
10. **Scansion: scanner flags ‘spondaic fifth’ at 13.3, 13.98, 13.110 (packet lists none)** — Hand-scanned, following the scanner's syllables. 13.3: the fifth foot is a spondee (φώ|νη), the line is the reply formula as shipped at 7.298 and 7.308. 13.98: ταὶ is shortened before ἀπορρῶγες (ordinary epic correption), caesura after γες, fifth foot πεπ|τη. 13.110: ταὶ shortened before ἀνθρώποισιν (the same correption), caesura in the third foot, fifth foot ἀν|θρώ. In all three the only irregularity the scanner reports is the spondee in the fifth foot, which is a rare but ordinary variant of the hexameter, not a licence; the packet flagged no line, the build requires no note, and conventions mention metre only where it explains a form. No sentence added to any note.
11. **13.76 ‘oarlocks’ note ('follows the wording used for this formula elsewhere in the poem')** — Verified against the shipped formula (odyssey-008 unit 418, odyssey-039 unit 103, and later); the claim is true. Left. (Side remark for the owner: conventions.md row 687 cites it as ‘8.418 and 19.576’, which are odyssey-008 and odyssey-019 unit numbers, not poem line numbers; I did not touch the table.)
12. **13.12 ‘Phaeacian counsellors’ vs ‘the counsel-bearers of the Phaeacians’ (`l`)** — Both layers are in the row; `i` is natural, `l` literal. Left (only the avoided-column spelling was changed).
13. **13.16, 13.17, 13.18, 13.36, 13.47–49, 13.53, 13.70, 13.91 reused English** — Compared with the packet and with the published units: units 0, 1, 26, 27 are identical to the shipped units (the validator's repeat check, run by hand against all published parts, finds no mismatch); line 13.36 and half-lines 13.31/13.56/13.70/13.91 reuse the shipped wording. Nothing to change beyond the items in the table.

## Cross-references checked

7.298 and 7.308 (reply formula), 7.178–179 (the Pontonous order: first line and a half identical, then ὄφρ’ εὐξάμενοι for ἵνα καὶ Διὶ …): true. 11.333–334 (same hush, same spell): true. 6.15 (πολυδαίδαλον): true. 3.467 (φᾶρος as a man's cloak): true. 1.32 (αἰτιόωνται, diectasis): true. 8.183, not 8.182: corrected. 8.293 (μεταδήμιος, cited in the new 13.45 note): true. Within the part: lines 20/23 (μέν … δέ), 24, 29, 30/61 (νέεσθαι, νέομαι), 31/35/33, 67/108 (φᾶρος), 74/78 (νήγρετος), 81/84, 89/90, 97: checked; two were wrong (89/90, ‘next line’ at 93–95) and are corrected.

## For the owner (not changed here)

* conventions.md row 687: ‘shipped at 8.418 and 19.576’ uses odyssey-NNN unit numbers as if they were poem lines (the units are 2.418 and 4.576).
* conventions.md row 465 lists ‘So he spoke’ among its avoided renderings while giving it as its own `i`.
* The scanner reports ‘spondaic fifth’ on 13.3, 13.98, 13.110 although the packet lists no flagged lines.
