# odyssey-072 — review, pass 1 (translation) — Odyssey 15.86–171

Reviewer, adversarial. Files read: runbook.md (step 2), conventions.md (whole, in chunks), packet.md, units.json, new-renderings.md, drafts/odyssey-001/units.json (shape), odyssey-071.json (last unit, for speech marks), and every published unit that shares a line with this part (found by script, accent-insensitive, not only the packet's whole-line matches). No modern translation was opened or recalled. `units.json` was edited in place by script; `t` is byte-identical to the drafter's (checked), no other field outside the list below changed.

Checks run by script after editing: concatenated `t` unchanged; `l` newline count equals `t` newline count in all 54 units; no `\n` in any `i`; the validator's repeat rule (whole-unit same Greek = same `l` and `i`) now passes for every unit; “ and ” balance 6/6 in `l` and 6/6 in `i`; `ln` and `p` on every unit agree with the edition and with the packet's ¶ marks (86, 92, 125, 130, 151, 154, 160, 167, 169).

Speech marks: odyssey-071's last unit closes Menelaus's offer with ” and this part opens in narration, so nothing runs in from the previous part. Opening “ / closing ” / `mark` stand on: 87–91 (Telemachus), 111–119 (Menelaus), 125–129 (Helen), 151–153 (Menelaus again), 155–159 (Telemachus), 167–168 (Peisistratus). Helen's second speech (171) opens in the next part; unit 53 carries no mark and says so. No change needed.

## Counts

15 findings applied (22 field edits): 2 high, 6 medium, 7 low. 21 findings considered and refused (listed below), plus 3 recommendations for files this role does not edit.

## Changes made

Severity: high = the validator would stop the build or a shipped line is contradicted; medium = a false statement in a note, a broken cross-reference, or a repeated passage not following its published English; low = imprecision, ambiguity, small consistency.

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 119 | `l`, `i` | high | The Greek of the unit (τεῒν δ’ ἐθέλω τόδ’ ὀπάσσαι.) is identical to the published unit at 4.619 (odyssey-019), but `l` ("this to bestow") and `i` ("it is to you that I wish to give this") differed. The validator fails on this. | Both replaced by the published wording: l "and to you I wish to give this.”", i "and now I want to give it to you.”" |
| 137 | `l`, `i`, `n` | high | The Greek (παρὰ δὲ ξεστὴν ἐτάνυσσε τράπεζαν.) is a whole published unit at 2.138 (odyssey-002) and again at odyssey-014, -031, -048, all with the same English; the draft gave different English. The packet did not list it because it lists only lines that stand whole inside a published unit, and 15.137 is half of the line 15.137 (νίψασθαι· παρὰ δὲ …), whose first half is the end of the previous unit. The validator fails on it. | `l` and `i` replaced by the shipped "and beside them she drew up a polished table." / "and she drew a polished table up beside them."; note: "here 'draw out, set up'" became "here 'draw up'" and a sentence added that the line is shipped word for word at 2.138 and the English is kept. |
| 115b–117a | `l`, `i`, `n` | medium | These lines are 4.615b–617a verbatim (the packet missed them: Murray prints ἔστιν at 4.616 and ἐστὶν at 15.116, so the line was not a whole-line match). The English must be kept ("a repeated line gets the same English every time"); the draft re-translated ("and of silver / it is, all of it … and the work of Hephaestus"). | `l` and `i` now follow the shipped passage ("silver / it is entirely, and with gold upon its rims it has been finished, / the work of Hephaestus;" and "it is entirely silver, its rims finished with gold, the work of Hephaestus;"; only the closing punctuation differs, as at 113–114). Note: "'finished off with gold'" made "'finished with gold'" to agree with `l`, and a sentence added that these lines also stand at 4.615–617. |
| 128b–129 | `l`, `i`, `n` | medium | The last line (οἶκον ἐϋκτίμενον καὶ σὴν ἐς πατρίδα γαῖαν.) is also shipped, at 4.476 (odyssey-018) and 6.315 (odyssey-029): "your well-built home and your own fatherland" / "your well-built home and your own native land". The draft had "house", dropped "own", and "fatherland" in `i`. By the table's own precedent (πατρίδα γαῖαν row, on 5.15) an exact repeat keeps its shipped English. | `l` now "at your well-built home and your own fatherland.”"; `i` now "And may you come rejoicing, as I wish, to your well-built home and your own native land.”"; note: σήν is "your own", and a sentence added that the line also stands at 4.476 and 6.315 and its English is kept. |
| 135 | `n` | medium | Cross-reference wrong: the note puts λεβήτων in Menelaus's list "at 15.82". The word is at 15.84 (confirmed in the source; the table has λέβης at 15.84). | "15.82" → "15.84". |
| 110 | `n` | medium | "Nobody has spoken to Menelaus" is false as written: Telemachus has just asked to leave (87–91) and Menelaus is answering that request by his actions. | Replaced by "Nothing has just been said to Menelaus (Telemachus's request is back at 87–91), so this is an opening and not a reply." |
| 171 | `n` | medium | The note says τόν "can be taken as the object of ὑποφθαμένη … or as the person spoken to; both give the same scene". The second option is not grammatical: φάτο takes μῦθον as its object and no accusative of the person addressed, and Helen's words go to the whole company, not to Menelaus alone. The scene is not the same. | The false alternative removed; the note now says τόν is Menelaus and the object of ὑποφθαμένη, and that μῦθον is the object of φάτο. |
| 156 | `l` | medium | αἲ γάρ opens a wish. The table fixes the wish-opener αἲ γάρ / αἴθε / εἴθε as `l` "Would that", `i` "If only"; the draft used "if only" in `l`. | `l` line 1 "if only I, just so," → "Would that I, just so,". `i` already "If only". |
| 86 | `n` | low | "whose offer of a journey through Hellas and Argos closed the previous part": what closes odyssey-071 is the list of parting gifts (82–85), not the journey. | "an offer of a journey and of parting gifts". |
| 99 | `n` | low | "Megapenthes is named here for the first time" read as a claim about the poem; he is named at 4.11. | "… for the first time in this part". |
| 101 | `n` | low | The scansion sentence was incomplete (see the hand scan below). | The one sentence now also says the scanner must read the α of ἵκανον as long, "which is not certain". |
| 134 | `n` | low | "the dual of an aorist of ἕζομαι": ἑζέσθην is the dual of the imperfect-type stem; the part's gloss.json itself hedges "aor./impf.". A label not shown to be true. | "an aorist" dropped: "the dual of ἕζομαι 'seat oneself'". |
| 141 | `n` | low | "the last son of Menelaus named in this part is Megapenthes (103)": he is named again at 122 (and at 100). | "the only son of Menelaus named in this part is Megapenthes (100, 103, 122)". |
| 150 | `l` | low | "and greeting them he spoke" — "them" directly after "the horses" reads as the horses; the Greek has no object for δεδισκόμενος. | "and greeting (them) he spoke:" (house practice for a supplied pronoun, as in "held (them) back"). |
| 140 | `i` | low | `i` began "Beside them …" with a capital after a unit ending in a semicolon; every other continuation unit begins in lower case, and `l` has "and beside them". | "and beside them the son of Boethous carved the meat …". |

### The hand scan of line 101 (flagged: UNRESOLVED; metrical lengthening ὅθι)

ἀλλ’ ὅτε δὴ ῥ’ ἵκανον ὅθι κειμήλια κεῖτο: syllables ἀλ(–, position) λὅ τε (⏑⏑) | δὴ (–) ῥῑ (–, ῑ taken long) | κα (?) νο νὅ (⏑⏑) | θι (?) κει (–) | μή (–) λι α (⏑⏑) | κεῖ (–) το (×). Foot 2 can be δὴ ῥ’ ἵ with ι long or short; after it, κα νον ὅ θι κει needs a long to begin foot 3 and another to begin foot 4. Neither κα (the α of ἵκανον) nor θι is long by nature or position. The scanner's best fit is α of ἵκανον long and θι of ὅθι long as the longum of foot 4; with α short there is no fit at all. So the irregularity is real as transmitted. The drafter's sentence named only the ὅθι; it now names the ἵκανον α as well. No other line of the part is flagged and the scanner fits all 86.

## Findings considered and refused

1. **133 κάρη (unit 29).** Kept: "fair as to the head" in `l`, κάρη left out of `i`, the note saying the construction is uncertain. The house glossary and the shipped notes (1.90, 2.6, 2.407) already take κάρη as an accusative of respect, and the note does not claim more. κάρη is not an epithet, so dropping it from `i` does not break the every-epithet rule.
2. **88–89 οὖρον (unit 2).** Kept "warden". The table already fixes οὖρος Ἀχαιῶν (3.411) as "warden of the Achaeans" and warns against "wind". The note names the homograph and gives the reason from κατέλειπον ἐπὶ κτεάτεσσιν. The reading of the glossary entry is for pass 2 (the draft gloss.json's `__broaden__` already adds the guardian sense to οὖρον).
3. **138/139 split.** Correct: Murray has an ano teleia after φέρουσα at 15.138 (the published unit at 2.139 has a comma), and the segmentation rule ends a unit at an ano teleia. The English of each half is the published English cut at the same place (checked word by word against 2.139, odyssey-014, -031, -048).
4. **107/114 κάλλιστος.** 107 takes the table's κάλλιστος row (`l` "fairest", `i` "the most beautiful"); 114 keeps the shipped "fairest … / finest" because the line is the repeat of 4.613–614 and the English of that passage is kept. The two `i` words differ on purpose; the glossary entry already carries both ("fairest, finest").
5. **ἀργὴν χῆνα (unit 46).** Kept "white". The note gives both senses ("bright, white" and "swift") and says why "white" is taken; the table's "swift" row is specific to κύνες ἀργοί and itself says "white" is possible. "Swift" for a goose carried in talons would be wrong in either layer.
6. **New epithets against published English.** καλλιπάρῃος ("fair-cheeked"), κηώεις ("fragrant"), παμποίκιλοι / ποικίλμασιν ("all-intricate" / "intricate work"), ἀρηΐφιλος ("Ares-loved" / "dear to Ares") and the three speech introductions (110, 166, 171) were each searched in all 71 published parts. None occurs earlier, none contradicts a published rendering, and each follows its table analogue (μιλτοπάρῃοι / φοινικοπάρῃος; ποικίλος δεσμός; ἀρηίφατοι; the shipped τοῖσι δὲ μύθων ἦρχε lines; the shipped δὴ τότε … προσέφη row).
7. **166 `l` "Nestor's son, Peisistratus".** Published `l` has both "Peisistratus, Nestor's son" (odyssey-015, -071) and "Nestor's son Peisistratus" (odyssey-009, -013). The draft keeps Greek order, which is `l`'s rule; the comma is harmless. No change.
8. **135 "silver basin" against the table's λέβης "cauldron" (basin listed as avoided).** The unit is word for word the shipped 2.136–137 unit, and its English is fixed by the validator. The note already says the λέβης here is the basin that catches the water. Not changed.
9. **"about": "a silver mixing-bowl that Hephaestus made".** It is Menelaus's claim at 117 and the same phrase is the house line for ἔργον Ἡφαίστοιο. Left.
10. **160 `i` "As soon as he had spoken".** Over-sharp for the dative participle εἰπόντι, but it is the only place in this unit where the immediacy of an omen is the sense. Left.
11. **Notes' ὥς with the accent / printed ὣς (units 11, 42).** The printed form is ὣς; the glossary entry for ὣς already says "also postpositive after its noun, = comparative ὡς 'as, like'". The note's label is the house one. Left.
12. **Unit 2 note "the sense is fixed by …".** Strong, but the sense is the traditional one and the contrast with a wind is the reason given. Left.
13. **Unit 8 κατεβήσετο "an aorist middle".** True of the form (the -σε/ο- aorist of βαίνω); active in sense. Left.
14. **Unit 12 νείατος "lowest, last; of garments undermost".** True of the word; Left.
15. **Unit 28 πείρινθα "probably of plaited wicker".** Hedged; the word is flagged rare. Left.
16. **Unit 39 λείψαντε "taken as from λείβω".** The note says "taken as", i.e. hedged. Left.
17. **Unit 40 i "stopped" for στῆ.** "took his stand" in sense; l keeps "stood". Left.
18. **Unit 41 i "tell Nestor … the same".** The note explains the elliptical object. Left.
19. **Unit 24 note "Helen answers the gift Menelaus has just given".** A reply in kind, not in speech; the word is loose but not false. Left.
20. **Quotation marks and `mark` on each speech.** Checked; nothing to change (see above).
21. **Remembered English in `i`.** Every `i` was read for ready-made phrasing. The two candidates ("bring … to pass", "heavenly among women") are house wording or a rebuilt rendering of τελέσειεν; nothing else arrived fully formed. Nothing changed.

## For files this role does not edit

- **new-renderings.md, row for 15.110**: the parenthesis "speech introduction with no earlier speech to answer" and "nothing has been said to him" repeat the claim corrected in unit 14 above. Suggest "no speech has just been made to him" before the row is copied into conventions.md.
- **new-renderings.md, row for ποικίλμασιν**: the row gives `l` "in intricate work", the unit has `l` "in its intricate work" (`i` agrees). Suggest the row take the unit's wording.
- **Validator WARNs to expect**: unit 9 (note about 160 words) and unit 45 (about 140) are over the note band; unit 1, 4, 15 are near it. Not shortened here.
- **Pass 2**: gloss.json was not read (pass 1 only). Points to check there: οὖρον (`__broaden__` already present), ἑζέσθην ("aor./impf."), and that no entry for ἵκανον fixes the quantity the scanner had to guess at 101.

---

# odyssey-072 — review, pass 2 (translation and glossary)

Reviewer, adversarial, second pass. Read afresh: runbook.md (step 2), conventions.md (entry-format and notes sections), packet.md, units.json (all 54 units, Greek against `l`, `l` against `i`, every note label against its line), gloss.json (every entry against the line or lines where the form stands), known-forms.json against the root `odyssey-glossary.json` (12,826 keys), and the published parts that share lines with this one. No modern translation or dictionary was opened or recalled. `units.json` and `gloss.json` were edited in place by script; `t` is byte-identical to pass 1 (asserted in the script), all 54 `l`/`i` quotation marks are as they were, and the only fields touched are those listed below.

## Counts

Units.json: 5 findings applied (7 field edits): 0 high, 1 medium, 4 low. Gloss.json: 13 findings applied (13 entries changed: 10 novel entries, 3 `__broaden__` entries): 3 high, 4 medium, 6 low. Findings considered and refused: 12. All 12 `__broaden__` entries start with the root file's existing entry whole followed by " · " (checked by script); all 63 novel entries are under 230 characters, use ’ only, contain no line numbers and no "here" (checked by script, after the edits).

## Changes made, units.json

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 150 | `l`, `i` | medium | Pass 1 left "greeting (them)" directly after "the horses" in `l`, and `i` had "greeting the pair, spoke to them": in both the object of the greeting reads as the horses, but the note says the Greek names no object and leaves the two young men to be understood for προσηύδα. δεδισκόμενος has no stated object. | `l` "and in greeting he spoke:"; `i` "He stopped in front of the horses and spoke in greeting:". Note unchanged (still true). |
| 127 | `n`, `l` | low | The note glossed τῆος as "meanwhile, until then"; τῆος is "meanwhile, for so long" (the correlative of ἧος), and there is no "until" in it. `l` had "your dear mother" with no mark that "your" is supplied, although the note says the Greek has no "your" (house practice marks a supplied pronoun, as "(them)" at 150). | Note "meanwhile, for that time"; `l` "beside (your) dear mother". |
| 146 | `n` | low | "προθύροιο is a genitive of place": it is the genitive of the place left, governed through ἐκ … ἔλασαν; "of place" suggests "where". | "a genitive of the place left, going with ἐκ … ἔλασαν". |
| 156 | `i` | low | `i` began "If only I might reach Ithaca" with a capital after unit 44's `i`, which ends in a semicolon; the same continuation rule pass 1 applied at 140. | "if only I might reach Ithaca …". |
| 106 | `n` | low | The note spelt the noun "ποικίλμα"; the glossary entry and the word are ποίκιλμα, so the two disagreed in the same part. | "ποικίλμα" → "ποίκιλμα". |

## Changes made, gloss.json

| form | severity | what was wrong | what was done |
|---|---|---|---|
| κιοίτην | high | Parsed "2 dual (= Attic κίοιτον)". The subject at 149 is the two young men (3rd person: ὄφρα … κιοίτην, "so that the two might go"), so the form is the 3rd dual optative (-οίτην), not the 2nd (-οιτον). The entry named the wrong person and the wrong Attic form. | "pres. opt. 3 dual (= Attic -οίτην), secondary dual ending -την: ’the two might go’". |
| ἔκιε | high | "tmesis with μετά" is false: τοὺς δὲ μετ’ … ἔκιε is the preposition μετά ("after") governing τούς (the root glossary's μετ entry already has "after, + acc."); nothing is divided from a verb. Also "impf./aor." for a form of the present stem. | "impf. 3 sg. act., augmented ἔ-: ’went’". |
| ἵκανον | high | "impf./aor. 3 pl., epic (= Attic ἵκον)": ἵκον is not Attic, and the aorist reading has no ground for ἱκάνω. Pass 1 asked that no entry fix the quantity of the α (the scan of 101 is unresolved); this entry did not, but its "(= ἵκον)" invited a comparison of quantities. | "ἱκάνω — come, arrive at; impf. 3 pl. act., unaugmented, epic (Attic ἀφικνέομαι)". No syllable length is stated anywhere in the entry. |
| βοηθοΐδης | medium | Contains "here" and is pinned to the line ("here Eteoneus"). | "… patronymic (-ίδης), used alone as a name for Eteoneus, Menelaus’s attendant". |
| ἑζέσθην | medium | "(aor./impf., unaugmented)": ἕζομαι has an imperfect in this stem; the root glossary treats ἕζοντο and ἕζετο as impf. The aor. hedge made the entry disagree with them. | "impf. 3 dual mid. (cf. ἕζοντο): ’the two sat down’". |
| καλλιπάρῃος | medium | "(= Attic καλλιπάρῃος, uncontracted)" names the same word as its own Attic equivalent and says nothing true. | "epic -ῃος, from παρῃά ’cheek’ (Attic παρειά)". |
| ποικίλμασιν | medium | "epic -ασιν": the dative plural in -μασι(ν) of a neuter in -μα is the ordinary ending, not an epic one; the entry named a Homeric form that is not one. | "neut. dat. pl., with movable ν, dat. of respect". |
| οὖρον (`__broaden__`) | low | New reading "guardian, watcher" and "I left no guard behind": the house word for this οὖρος is "warden" (table, 3.411), the root file's own οὖρος entry says "warden, guardian", and `l`/`i` in the unit say "warden". | "οὖρος — warden, guardian (related to ὁράω ’see, watch’) … ’I left no warden behind’". The old entry and " · " are untouched. |
| χειρῶν (`__broaden__`) | low | "gen. pl. of source with μνῆμα" and ’a keepsake from Helen’s hands’: the genitive Ἑλένης χειρῶν depends on μνῆμα ("of Helen’s hands"), and the unit's own English is "a memorial of Helen’s hands". | "gen. pl., dependent on μνῆμα … ’a memorial of Helen’s hands’". |
| ὡς (`__broaden__`) | low | The indirect-statement reading quoted ’I would say that I am coming’; the form at 158 is an optative of wish (αἲ γάρ … εἴποιμ’), and the unit reads "might tell how, … I come". | "’that, how’ (εἴποιμ’ ὡς … ἔρχομαι ’I might tell how I am coming’)". |
| εἴποιμ | low | "’I would say’" for the optative of a wish. | "optative of wish: ’I might say’". |
| φαεινόν | low | "epic (= Attic φανός, φαεινός)" lists the form itself as its Attic equivalent. | "(cf. φαίνω ’show, shine’)"; no Attic equivalent claimed. |
| ὑποκρίναιτο | low | Gloss ’how he might interpret’; the unit's `l` and `i` read "answer" (the note says the answer is an interpretation of the portent). | "’how he might answer’". |

## Checked and found correct (no change)

Every other novel entry was checked against each line where the form stands, as a parse (case, number, tense, mood, voice, person), a meaning and, for Homeric forms, an Attic equivalent. Points the assignment named:

- **οὖρον**. Guardian, not wind: κατέλειπον ἐπὶ κτεάτεσσιν "I was leaving behind over my possessions" cannot be said of a wind; the accusative οὖρον is the object of κατέλειπον and οὐ negates it. The `__broaden__` entry keeps the fair-wind and furrow-length readings whole and adds the guardian one. Corrected only in wording (above).
- **ἑζέσθην**. 3 dual middle, as the dual νῶϊν at 168 shows for the same two persons; tense corrected to match the root glossary (above).
- **ἵκανον**. No entry states a quantity for any syllable of ἵκανον or ὅθι (checked all 63 + 12 entries, and the root entries for ἵκοντο and ὅθι, which are unchanged). The metrical question at 101 stays in the note only, as "not certain".
- **The 12 `__broaden__` entries.** γυναῖκες (162), δώματος (109), οὖρον (88), πολύ (96), τί (91), χειρῶν (125), ἐπί (88), ἐφ’ (87), ὃ (113: nominative neuter relative, subject of ἐστι, correct), ὡς (158), ὥς (111: accented before the enclitic τοι, correct), οἱ (105): each new reading is the use at the line cited, and each old entry stands whole before " · " (script-verified against the root file).
- **Known forms with a use the root entry lacks.** Scanned all 364 known forms against the root file. The uses that looked new were already covered: ᾗ (possessive, 92), ἔργον (Ἡφαίστοιο, 117), ἢ (first alternative of an indirect question, 167), ἐπ’ (142), μετ’ (147), ὑπέρ (135), παρά (127, 137), ἀργύρεον, κεῖται. No further `__broaden__` entry is needed.

## Findings considered and refused

1. **ἑζέσθην "unaugmented".** Kept out of the new entry, not forced in; the root entries for ἕζοντο and ἕζετο carry none either. Nothing to add.
2. **κάρη (29).** Pass 1's refusal stands; the root entry for κάρη already has the accusative of respect, and the note says the construction is uncertain.
3. **Unit 9 note, "the scanner can fit it only by counting the last syllable of ὅθι long … and must also read the α of ἵκανον as long".** True of the scanner's fit as pass 1 recorded; nothing in the note claims the length is real. Left.
4. **Unit 4 note, "the order Menelaus announced in his speech in the previous part".** Checked in odyssey-071's last unit: "δεῖπνον ἐνὶ μεγάροις τετυκεῖν ἅλις ἔνδον ἐόντων" is there. True.
5. **Unit 30 note, "the half-line is a formula for settling guests".** Shown by the published parts: κατὰ κλισμούς τε θρόνους τε ends lines in odyssey-002, -012 and -047. Left.
6. **Unit 14 `i` "And fair-haired Menelaus said to him:" after a unit ending in a semicolon.** It is the new formula row in new-renderings.md, a fresh sentence introducing a speech; the capital follows the row. Left.
7. **Unit 36 note, "the only son of Menelaus named in this part is Megapenthes".** True (100, 103, 122); "the likely meaning" is hedged. Left.
8. **Unit 42 note and `l`/`i` for 152.** The second line of the unit is the published line at odyssey-064; `l` and `i` follow that English word for word. Checked; left.
9. **Units 31, 38, 39 repeats.** 135–137 (odyssey-002/-014/-031/-048), 145–146 (odyssey-013) and μελίφρονα (odyssey-031/-048/-062) follow the shipped English in `l` and `i`. Checked; left.
10. **Unit 46 `i` "As soon as he had spoken".** Pass 1's refusal stands.
11. **Unit 34/35 diction "meat" against "meats" in `l`.** `l` keeps the plural of κρέα and `i` the English mass noun; same as the shipped practice. Left.
12. **αἰετὸς "epic αἰετός (= Attic ἀετός)".** The headword is the Attic spelling and the epic form is the printed one; the entry says so. Left.

## For files this role does not edit

- Nothing new beyond pass 1's two new-renderings.md suggestions, which still stand.
