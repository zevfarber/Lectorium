# odyssey-052 — review (Odyssey 11.100–209)

Two passes over `units.json` (edited in place by script; `t`, `ln` and `p` verified unchanged against the pre-review copy) and a second-pass check of `gloss.json` (edited directly). After the edits, a scratch build and `validate_odyssey.py` in a copy of the repository: **PASS**, no WARN, scansion flags none.

**Counts, units.json and header:** high 12, medium 40, low 51 — 103 changes. **gloss.json:** 10 entries corrected, 10 broadenings added, 1 proposed broadening removed.

Pass column: 1 = first pass (notes, grammar, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, the table and the shipped parts); 2 = second pass, on the edited file and on `gloss.json`.

## Changes to units.json

| pass | line | field | severity | what was wrong | what was done |
|---|---|---|---|---|---|
| 1 | 101 | l | medium | τοι (‘for you’) left out of l, though the note and i both carry it. | Added ‘for you’ to l. |
| 1 | 101 | l | medium | τοι of ὅ τοι omitted in l; i and the note both say ‘against you’. | Added ‘against you’ to l. |
| 1 | 101 | n | low | ὅ called simply ‘the relative’; it is the old demonstrative-pronoun form doing duty as one. | Label made exact. |
| 1 | 104 | l | medium | ‘own’ added in l for σόν (σός is ‘your’, not the possessive ὅς ‘own’); ‘restrain’ for ἐρυκακέειν where the shipped rendering of the same verb is ‘hold back’. | ‘own’ dropped; ‘hold back’. |
| 1 | 104 | i | medium | Same as l. | Same as l. |
| 1 | 104 | n | low | ‘a long, epic form of the infinitive’ names no tense or formation. | Tense and formation named. |
| 1 | 106 | n | medium | Label ‘dative of place’ wrong: with πελάσῃς it is the goal (‘bring near to’); the form is the adjective, not the bare name. | Rewritten. |
| 1 | 106 | n | low | A rare epithet given as plain fact. | Marked as the traditional gloss. |
| 1 | 106 | n | low | Note’s ‘looks over’ did not match l ‘oversees’. | Aligned with l. |
| 1 | 110 | l | medium | ‘even so’ renders nothing: the line has καί but no ὥς (that was line 104). | ‘then too’. |
| 1 | 110 | n | medium | τὰς is feminine; μῆλα is neuter, so the pronoun cannot be said to pick up the flocks grammatically. | Rewritten. |
| 1 | 110 | n | high | ἐάσῃς is the aorist subjunctive; the uncontracted present subjunctive ἐάᾳς corresponds to Attic ἐᾷς (as the glossary entry and 147 show). False equivalence in a note. | Corrected, and ‘present’ added. |
| 1 | 110 | n | low | Tense not stated. | Added ‘present’. |
| 1 | 110 | n | medium | ‘almost word for word’ overstates: only the last half-line recurs. | Said what actually recurs. |
| 1 | 113 | l | medium | The same three phrases (ὀψὲ κακῶς, ὀλέσας ἄπο πάντας ἑταίρους, νηὸς ἐπ’ ἀλλοτρίης) already ship in odyssey-044 line 532 as ‘late and badly’, ‘having lost all his companions’, ‘on another’s ship’; here l varied them. | Brought into line with the shipped wording. |
| 1 | 113 | i | medium | Same: odyssey-044 i has ‘late and in misery, having lost all his companions, on a ship not his own’. | Aligned. |
| 1 | 115 | n | high | Label false: tmesis separates a preverb from its verb; here a preposition is separated from its noun. | Label corrected. |
| 1 | 115 | n | low | Case not given. | Case added. |
| 1 | 118 | n | low | βίας is an accusative plural of βία, not simply ‘the plural of βίη’. | Corrected. |
| 1 | 119 | l | medium | (1) The clause κτείνῃς ἠὲ δόλῳ ἢ ἀμφαδόν already ships in odyssey-003 (line 1.293) as ‘by guile or openly’; l had ‘by trick’. (2) δή left out of l. | ‘guile’, and ‘indeed’ added. |
| 1 | 119 | i | medium | i had ‘by a trick’; the shipped i of the same clause is ‘whether by guile or in the open’. | Aligned. |
| 1 | 119 | n | medium | Accent of αὐτὰρ misquoted; κτείνῃς called ‘aorist’ although the glossary parses it as present subjunctive (the form is the same; the sense with ἐπήν is completed action). | Accent fixed; tense label removed. |
| 1 | 119 | n | low | Follows the l/i change. | Aligned. |
| 1 | 119 | n | low | ‘fitted with all its gear’ is an interpretation the line does not show. | Cut. |
| 1 | 122 | n | high | Case relation false: ἀνέρες is nominative, τοὺς accusative; it cannot be in apposition to τοὺς. | Rewritten. |
| 1 | 124 | n | low | Claim about the rest of the poem that this part cannot show. | Cut. |
| 1 | 126 | n | low | μάλ’ not accounted for in l or i; note silent. | Said honestly in the note. |
| 1 | 127 | l | medium | τοι is one word, but l says ‘to you … you’ (it is the dative with συμβλήμενος, ‘meeting you’). | Doubled pronoun removed. |
| 1 | 127 | n | high | φημί has no aorist; φήῃ is the present subjunctive (glossary agrees). | Corrected. |
| 1 | 129 | n | high | False: the first command of the instruction is ἔρχεσθαι at 121; ‘go home’ is not the first. | Rewritten. |
| 1 | 129 | n | low | συῶν is the genitive plural of σῦς, which is not gendered. | Corrected. |
| 1 | 132 | l | low | μάλ’ left out of l. | ‘quite’ added. |
| 1 | 132 | n | medium | Quotes ἱερὰς, but the line has ἱερᾶς; asserts what the rest of the poem does (‘each time’) which this part cannot show. | Quotation exact; claim limited to what the packet shows. |
| 1 | 134 | l | medium | μάλα (‘very’) left out of l, though i has ‘a very mild death’. | ‘very’ added. |
| 1 | 134 | i | medium | πέφνῃ is ‘slay’ (and l says so); ‘carry you off’ softens it. Never bowdlerize. | ‘kill’. |
| 1 | 136 | n | medium | ‘a land at peace’ is not in the Greek (ὄλβιοι is ‘prosperous’). | Cut. |
| 1 | 138 | n | high | (1) ἔφατ’ called ‘unaugmented’: ἔφατο is augmented (the unaugmented form is φάτο). (2) The note hid that ‘she’ is simply wrong here behind ‘its ‘she’ was fixed for another speaker’; (3) ‘wherever it recurs’ is a claim about the rest of the poem. Known open point: the validator forces the shipped English. | Label corrected; the note now says plainly that ‘she’ is wrong for Tiresias and why it stands, and gives the right reading. l and i untouched (validator check 6). |
| 1 | 139 | n | high | ‘unaugmented’ false (ἐπ-έ-κλωσαν carries the augment); ‘the Fates’ is a personification this part does not show (the Greek says θεοί). | Corrected. |
| 1 | 140 | n | low | Claim about the whole poem. | Limited to what the packet shows. |
| 1 | 141 | n | low | ‘throughout’ is a claim about the poem. | Limited. |
| 1 | 142 | n | medium | Parse (‘participle of ἀκέω’) disagrees with the glossary lemma ἀκέων and rests on a verb that is hardly found. | Aligned with the glossary. |
| 1 | 142 | n | low | Quoted with the wrong accent (the line has ἑὸν). | Fixed. |
| 1 | 142 | n | low | General claim about the dead that this part does not state. | Replaced by what the lines show. |
| 1 | 145 | n | high | ‘without its augment’ false: ἐφάμην begins with the augment (φάμην is the unaugmented form). | Corrected. |
| 1 | 146 | n | high | ‘complement of ἔπος’ is not a construction; ῥηΐδιον is an adjective agreeing with ἔπος, which is the object. | Corrected. |
| 1 | 147 | l | medium | Same Greek clause (νεκύων κατατεθνηώτων / αἵματος ἆσσον ἴμεν) already ships in odyssey-050, 051 as ‘of the dead, of those who had died’ and ‘nearer the blood to go’ / ‘come nearer the blood’; l had ‘near’, and dropped the doubled phrase. | Aligned. |
| 1 | 147 | i | medium | Same. | Aligned. |
| 1 | 147 | n | medium | ‘neuter noun’ is not a firm label (adverbial accusative is as likely); ‘fixed phrase’ is a claim about the poem; ἴμεν unparsed; ‘near’ for the comparative. | Rewritten. |
| 1 | 149 | n | medium | εἶσιν is a present form with future sense (the glossary says so); not ‘the future’. | Corrected. |
| 1 | 150 | i | low | ‘With these words’ is the very rendering the table lists as avoided for the neighbouring formula ὣς ἄρα φωνήσασ’; using it for ὣς φαμένη blurs the two. | ‘So speaking’ (matches l). |
| 1 | 150 | n | high | ‘unaugmented’ false: ἔβη has the augment (unaugmented is βῆ). | Corrected. |
| 1 | 152 | l | medium | μένον ἔμπεδον already ships in odyssey-032 as ‘stayed on steadily’ (both layers) and the glossary gives ἔμπεδον ‘steadily’. | ‘steadily’. |
| 1 | 152 | i | medium | Same. | Same. |
| 1 | 152 | n | medium | ‘Tiresias’s warning’ is not in this part (and the gloss differs). | Cut; aligned with the glossary. |
| 1 | 152 | n | high | ‘unaugmented’ false: ἤλυθε carries the augment. | Corrected. |
| 1 | 152 | n | medium | Names Zeus’s epithet, which this part cannot show. | Cut to the compound. |
| 1 | 153 | n | low | Loose wording. | Tightened. |
| 1 | 155 | mark | low | The mother is never named in this part (μήτηρ, τέκνον); the mark and note name her. | Role used. |
| 1 | 155 | n | low | Names what this part cannot show (and contradicts itself). | Cut. |
| 1 | 163 | n | high | ‘unaugmented’ false (see 138). | Corrected. |
| 1 | 164 | mark | low | Name not in this part. | Role used. |
| 1 | 170 | n | low | The first request begins ἀλλ’ ἄγε, not εἰπέ. | Corrected. |
| 1 | 171 | n | medium | Note says ‘doom’, the table reserves ‘doom’ for πότμος and l has ‘death-spirit’. | Aligned with l. |
| 1 | 171 | n | low | The question is not itself one of two alternatives. | Rewritten. |
| 1 | 172 | n | low | ‘sudden’ is not in the Greek. | Cut. |
| 1 | 174 | n | low | ‘kingly’ not in the Greek; note at 184 says ‘privilege of rank’. | Aligned. |
| 1 | 177 | l | medium | μνηστὴν ἄλοχον already ships in odyssey-001 (line 35) as ‘the wedded wife’ in both layers; l had ‘wooed wife’. | ‘wedded wife’ in both layers. |
| 1 | 177 | n | medium | Follows the l change. | Rewritten. |
| 1 | 180 | n | low | ‘used of goddesses’ cannot be shown by this part. | Cut. |
| 1 | 181 | mark | low | Name not in this part. | Role used. |
| 1 | 181 | n | low | Same. | Same. |
| 1 | 182 | n | low | Generalizes about Homer. | Limited to this line. |
| 1 | 184 | l | low | ἀλεγύνω already ships as ‘see to’ (δαῖτας ἀλεγύνετε, odyssey-004, 006, 033). | ‘see to’. |
| 1 | 184 | i | low | Same. | Same. |
| 1 | 184 | n | low | Follows l/i. | Aligned. |
| 1 | 184 | n | medium | Speaks of ἐίσας ‘as an epithet of ships’, which nothing in this part shows. | Cut. |
| 1 | 187 | n | low | Names a man the part never names. | Cut. |
| 1 | 188 | l | medium | The phrase ῥήγεα σιγαλόεντα ships as ‘glossy rugs’ (odyssey-027, both layers) and the pair χλαῖναι καὶ ῥήγεα as ‘cloaks and rugs’ (odyssey-012); here ‘blankets’. | ‘rugs’. |
| 1 | 188 | i | medium | Same. | Same. |
| 1 | 188 | n | low | Follows l/i. | Aligned. |
| 1 | 188 | n | low | The sentence spans three and a half lines, not four. | Corrected. |
| 1 | 192 | l | medium | ἀνὰ γουνὸν ἀλωῆς οἰνοπέδοιο ships in odyssey-002 (line 191) as ‘the rising ground of his vineyard plot’; the drafter’s new-renderings.md said οἰνόπεδος is ‘not otherwise rendered’, which is wrong. | Aligned with the shipped wording. |
| 1 | 192 | i | medium | Same. | Same. |
| 1 | 192 | n | low | Follows l/i. | Aligned. |
| 1 | 195 | l | medium | ἀέξει ships everywhere as ‘makes it grow’ (odyssey-040, 042) and the glossary says ‘make grow’; ‘nourishes’ is new. | ‘makes grow’. |
| 1 | 195 | i | medium | Same; also πένθος ships as ‘grief’ (odyssey-004, 028, 031). | Aligned. |
| 1 | 195 | n | low | Empty remark (σός simply is ‘your’). | Cut. |
| 1 | 198 | i | low | l has ‘come upon’ (ἐπήλυθεν); i changed the verb. | Aligned. |
| 1 | 202 | n | low | ‘occurs only here’ is a claim about the poem. | Cut. |
| 1 | 204 | l | low | φρεσί is ‘mind’ everywhere else in this part (146, 195); i has ‘in my mind’. | ‘mind’. |
| 1 | 206 | l | low | l shifts from ‘her’ (rushed upon her, seize her) to ‘it’, and i says ‘she’. | ‘she’. |
| 1 | 208 | n | low | Asserts what is in the next part. | Limited to this part. |
| 2 | 177 | l | medium | ἔμπεδα πάντα φυλάσσειν already ships in odyssey-007 (line 2.226) as ‘to keep all things steadfast’ / ‘keep everything secure’; l had ‘securely guards’, i ‘keep everything safe’ (the drafter’s new-renderings row set these two choices). | Both layers aligned with the shipped wording; the row in new-renderings.md corrected too. |
| 2 | 177 | i | medium | Same. | Same. |
| 2 | 177 | n | low | Follows l/i. | Aligned. |
| 2 | 149 | i | low | ‘anyone you begrudge it’ is not English: the dative ᾧ needs ‘to whom’. | Repaired. |
| 2 | 202 | l | low | με (the person deprived) not rendered in l. | ‘from me’ added. |
| 2 | 195 | n | low | Left a stray double space and comma after an earlier cut; ‘increases’ differs from l ‘makes grow’. | Repaired. |
| 2 | 184 | n | low | Redundant clause left after the earlier cut. | Cut. |
| 2 | 138 | n | low | Pass-1 note ran to 122 words (validator band 25–110; fails over 130). | Tightened to about 100 words; sense unchanged. |
| 2 | 164 | l | medium | Square-bracket insertion in l; no shipped l uses brackets, and the shipped treatment of a bare εἰς Ἄϊδος (odyssey-050 line 502) is ‘to Hades’. | Brackets removed; l follows 050.502. |
| 2 | 164 | n | low | Follows the l change. | Aligned. |
| 1 | — | about | low | Summary named Penelope, Laertes and the Phaeacians (none named in these lines), called the death ‘gentle’ (ἀβληχρός is of unknown meaning; ‘gentle’ is reserved for ἀγανός), said ‘prosperous old age’ (the Greek has λιπαρόν ‘sleek’; ‘prosperous’ is ὄλβιοι, of the people) and ‘embrace’ for ἑλέειν. | Rewritten: ‘his wife’, ‘his father’, ‘a mild death, in a sleek old age with his people prosperous about him’, ‘take hold of her’; Phaeacians dropped. |

## Changes to gloss.json (second pass)

Every novel form was parsed against its line. Corrected, or (for known forms) broadened where the existing entry did not cover the case or sense used here. The `__broaden__` entries keep the old entry whole.

| form | was | now | why |
|---|---|---|---|
| ῥηΐδιόν | ῥηΐδιος — easy; neut. nom. sg., epic (= Attic ῥᾴδιος), predicate with ἔπος | ῥηΐδιος — easy; neut. acc. sg., epic (= Attic ῥᾴδιος), agreeing with ἔπος | Neuter accusative, agreeing with ἔπος, the object at 146 (not nominative, not a predicate). |
| εὕρητε | εὑρίσκω — find; aor. subj. 2 pl., unaugmented, with κε: ’you may find’ | εὑρίσκω — find; aor. subj. 2 pl., with κε: ’you may find’ | A subjunctive has no augment; ‘unaugmented’ was meaningless. |
| κὴρ | κήρ — doom, death-fate; fem. nom. sg., personified power of death (distinct from κῆρ ’heart’) | κήρ — death-spirit, power of death, doom; fem. nom. sg., personified (distinct from κῆρ ’heart’) | Table renders κήρ ‘death-spirit’ and reserves ‘death-fate’ and ‘doom’; entry aligned with the English layers. |
| περῆσαι | περάω — cross, pass over; aor. inf., epic uncontracted (= Attic περᾶσαι): ’to cross’ | περάω — cross, pass over; aor. inf., epic -ῆσαι (= Attic περᾶσαι): ’to cross’ | The long η is Ionic for Attic ᾱ (περᾶσαι), not an uncontracted form. |
| ἀβληχρὸς | ἀβληχρός — gentle, soft, feeble; masc. nom. sg. | ἀβληχρός — mild (meaning not known: ’gentle, feeble, slow’ have all been guessed); masc. nom. sg. | Meaning unknown: conventions require the glossary to say so. |
| ἀθηρηλοιγὸν | ἀθηρηλοιγός — winnowing-shovel (’chaff-destroyer’, sense traditional); masc. acc. sg. | ἀθηρηλοιγός — chaff-ruiner, traditionally a winnowing-shovel (first element disputed); masc. acc. sg. | Meaning disputed (first element); entry gave the winnowing-shovel as plain sense. |
| τεκμαίρομ | τεκμαίρομαι — ordain, foretell by signs; pres. 1 sg. mid., elided (τεκμαίρομ’ = τεκμαίρομαι) | τεκμαίρομαι — fix, mark out, ordain; pres. 1 sg. mid., elided (τεκμαίρομ’ = τεκμαίρομαι) | Aligned with the table’s ‘I fix’. |
| ἐπιβήτορα | ἐπιβήτωρ — mounter, covering male; masc. acc. sg., with συῶν: ’boar-stud of swine’ | ἐπιβήτωρ — mounter, covering male; masc. acc. sg., agreeing with κάπρον and governing συῶν: ’mounter of swine’ | ‘boar-stud’ is the wording the new-renderings row refuses; the word also agrees with κάπρον and governs συῶν. |
| νεῖαι | νέομαι — go, come back; pres. 2 sg., epic -αι (Attic νεῖ), future sense: ’you will return’ | νέομαι — go, come back; pres. 2 sg., contracted epic νεῖαι (= νέεαι), future sense: ’you will come back’ | ‘Attic νεῖ’ is not a real Attic equivalent; the form is contracted νέεαι. |
| ἴφια | ἴφιος — stout, sturdy, fat; neut. acc. pl., with μῆλα | ἴφιος — stout, sturdy (the traditional gloss; ’fat’ also given); neut. acc. pl., with μῆλα | The sense is the traditional gloss; said so. |
| __broaden__[εἴκελον] | εἴκελος — like, resembling (+ dat.); epic (= Attic ἐοικώς, ὅμοιος); neut. nom. sg. · also fem. nom. sg. (two-ending adj.), agreeing with ψυχή: ’like’ (σκιῇ εἴκελον) | (removed) | Proposed reading ‘fem. nom. sg., agreeing with ψυχή’ is morphologically impossible (the feminine would be εἴκελος; εἴκελον is neuter) and the old entry (neut. nom. sg.) already covers 207. |
| __broaden__[κελαινεφές] | κελαινεφής — dark with cloud, black as a cloud; adj., neut. nom. sg., said of blood | κελαινεφής — dark with cloud, black as a cloud; adj., neut. nom. sg., said of blood · also neut. acc. sg. (same form), agreeing with αἷμα as object: ’dark-clouded (blood)’ | Used as accusative with αἷμα at 153. |
| __broaden__[μήδεα] | μῆδος — counsel, plan, device; neut. acc. pl. μήδεα · also the genitals (of the body): περὶ χροῒ μήδεα φωτός ’the man’s genitals, about the skin’; neut. acc. pl. | μῆδος — counsel, plan, device; neut. acc. pl. μήδεα · also the genitals (of the body): περὶ χροῒ μήδεα φωτός ’the man’s genitals, about the skin’; neut. acc. pl. · also neut. nom. pl. (same form), subject: ’counsels’ (σά τε μήδεα … ἀπηύρα) | Nominative subject at 202; entry gave only accusative. |
| __broaden__[σά] | σός — your; possessive adj., neut. acc. pl. | σός — your; possessive adj., neut. acc. pl. · also neut. nom. pl., agreeing with μήδεα as subject | Nominative with μήδεα at 202. |
| __broaden__[πτερὰ] | πτερόν — feather, wing; neut. acc. pl. | πτερόν — feather, wing; neut. acc. pl. · also neut. nom. pl., predicate: ’wings’ (τά τε πτερὰ νηυσὶ πέλονται ’which are wings for ships’) | Predicate nominative at 125. |
| __broaden__[ῥέεθρα] | ῥέεθρον — stream, running water, current; neut. acc. pl. | ῥέεθρον — stream, running water, current; neut. acc. pl. · also neut. nom. pl., subject: ’streams’ (δεινὰ ῥέεθρα) | Nominative subject at 157. |
| __broaden__[δέμνια] | δέμνιον — bedstead, bed; neut. acc. pl. | δέμνιον — bedstead, bed; neut. acc. pl. · also neut. nom. pl., in apposition to εὐναί: ’bedding’ | Nominative in apposition to εὐναί at 189; sense ‘bedding’, as shipped in odyssey-012. |
| __broaden__[σὸν] | σός — your, yours (sg.); masc. acc. sg. | σός — your, yours (sg.); masc. acc. sg. · also neut. acc. sg., agreeing with γέρας: ’your (prize)’ | Neuter accusative with γέρας at 184; entry gave masculine only. |
| __broaden__[ἢ] | ἤ — or; disjunctive conj. (epic ἠέ/ἤ) · also ’than’ after a comparative: κρεῖσσον … ἢ ὅτε ’better than when’ · also ’before’ after a verb of anticipating (ἔφθης … ἢ ἐγώ ’you got here before I did’) | ἤ — or; disjunctive conj. (epic ἠέ/ἤ) · also ’than’ after a comparative: κρεῖσσον … ἢ ὅτε ’better than when’ · also ’before’ after a verb of anticipating (ἔφθης … ἢ ἐγώ ’you got here before I did’) · also introducing the first alternative of an indirect question: ’whether’ (ἢ ἔτι … ἦέ τις ’whether still … or someone’) | ‘whether’ at 175 (first alternative of an indirect question). |
| __broaden__[θυμόν] | θυμός — heart, spirit, soul; acc. sg. | θυμός — heart, spirit, soul; acc. sg. · also the life that leaves the body: ’life’ (μελέων ἐξείλετο θυμόν ’took the life out of the limbs’) | ‘life’ at 201 (the table: θυμός of the life that leaves the body). |
| __broaden__[θυμὸν] | θυμός — heart, spirit, soul; acc. sg. | θυμός — heart, spirit, soul; acc. sg. · also the life that leaves the body: ’life’ (μελιηδέα θυμὸν ἀπηύρα ’took away (my) honey-sweet life’) | ‘life’ at 203 (same). |

Not changed (additions-only rule), but wrong, and flagged for the owner: the existing glossary entries ἔβη (“root aorist, unaugmented”) and ἔγνω (“aor. 3 sg., no augment”), since both forms carry the augment (the unaugmented forms are βῆ and γνῶ-). The notes of this part do not repeat the error.

## Findings considered and refused

- **11.138 `l`/`i` (“So she spoke …”).** Known open point. The validator (check 6) requires a repeated unit to carry the shipped English, and the shipped line is for a woman speaker. Kept. The note now says in plain words that ‘she’ is wrong for Tiresias, why it stands, and how to read it; the flag section of `new-renderings.md` was reworded to match.
- **11.163 ‘So she spoke’.** Correct: the speaker is Odysseus’s mother.
- **11.146 `i` “an easy thing” against `l` “an easy word” (ἔπος).** Left. ἔπος is ‘word, speech, thing said’ (glossary), ‘an easy word’ is not natural English, and the sense and force agree.
- **ἴφια → “stout”, although ‘stout’ stands on the avoided lists of ἴφθιμος, κρατερός and κρατερώνυχας.** Left. The avoided lists are per Greek word and say nothing about ἴφιος; ‘fat’ is reserved for πίονα and ‘mighty’ for ἴφθιμος. The note now marks ‘stout’ as the traditional gloss.
- **ἀθηρηλοιγός `l` “chaff-ruiner” (picks ‘chaff’ for ἀθήρ).** Left. LSJ gives ‘awn, chaff’; the note says the first element is disputed and the glossary now says so too.
- **κατέδουσι “eat up” against ‘devour’ (odyssey-007, line 237).** Left. The shipped English is itself split (‘devour’ there, ‘eat up’ in odyssey-012, line 313).
- **βουλήν τε νόον τε “counsel and mind” against odyssey-007 ‘plan and purpose’.** Left. The shipped English is split; odyssey-016 (‘the counsel and the mind’) is the closer match and the one followed.
- **πῆμα “woes” against odyssey-044 ‘troubles’ (εὕροι δ’ ἐν πήματα οἴκῳ).** Left. ‘Woes’ is the table’s rendering and the majority of the shipped uses.
- **δόλος: the table row for δόλον ὑφαίνειν says ‘trick’; `l`/`i` at 119 now say ‘guile’.** Changed to ‘guile’ (see the change at 119) because the identical clause κτείνῃς ἠὲ δόλῳ ἢ ἀμφαδόν ships with ‘guile’ in odyssey-003. Shipped parts use both words; flagged for the owner.
- **ῥήγεα: the table row (10.352) says ‘blankets, as shipped in odyssey-016 and odyssey-032’ and lists ‘rugs’ as avoided.** Used ‘rugs’ at 188–189: the phrase ῥήγεα σιγαλόεντα ships as ‘glossy rugs’ (odyssey-027) and the pair χλαῖναι καὶ ῥήγεα as ‘cloaks and rugs’ (odyssey-012). Table row and shipped parts disagree; flagged for the owner.
- **χαλεπὸν γῆρας “harsh old age” (the table keeps ‘harsh’ for persons and peoples, ‘hard’ for tasks).** Left. The same construction ships as ‘harsh grief’ (odyssey-028, χαλεπὸν δέ με πένθος ἱκάνει); ‘hard’ is kept for 156, a thing hard to see.
- **ὣς φαμένη ψυχή with ‘she’ for Tiresias.** Refused, as the drafter did: the feminine is the noun’s gender. The `i` ‘With these words’ was changed to ‘So speaking’ because the table lists it as avoided for the neighbouring formula ὣς ἄρα φωνήσασ’ (listed under changes).
- **Note at 102 names Poseidon (“a name for Poseidon”).** Left. Poseidon is named in this part (130), and the note at 101 says the god is not named yet; the note at 102 only says what the epithet refers to.
- **Quotation marks.** Checked by script and by eye. Opening ‘ on the first unit of each of the six speeches (100, 139, 146, 155, 164, 181), closing ’ on the last (137, 144, 149, 161, 179, 203); no stray marks; `mark` on exactly those six units. Continuity: in the last unit of odyssey-051 (lines 98–99) the seer’s previous speech (92–96) is already closed and the unit ends with his next speech about to begin, so a fresh ‘ at 100 is right. The outer speech from 9.2 stays unclosed. Line 209 introduces Odysseus’s speech, which opens in the next part, so no mark is left open here. The validator’s balance check (check 5) counts only “ ”, which this part does not use.
- **Scansion.** The packet flags none, and the scanner reports no licences. The one metrical remark in a note (ἀνέρες, 123, first syllable lengthened) agrees with the scanner (long first syllable).
- **Unit cuts at commas (104, 119, 127, 129).** Checked: each sits in a sentence longer than four lines (104–109, 119–134, 127–134), and each falls where the syntax pauses.
- **Repeated lines and the validator.** 138, 140, 145, 163, 170 carry the shipped `l`/`i` verbatim (checked with the validator’s own matching). 133 (inside 132–134), 154, 173, 199 and 209 reuse the shipped wording inside larger units, with ‘him’ → ‘her’ at 209 and ‘him’ dropped at 199, as the sentence requires.
- **Trimmed from notes and marks (things this part cannot show).** Anticleia, Laertes, the Fates, Zeus’s epithet of κελαινεφής, ἐίσας ‘of ships’, ‘recurs elsewhere in the poem’, ‘occurs only here’, ‘used of goddesses’, ‘Tiresias’s warning’, ‘a land at peace’, ‘sudden’ death, ‘kingly’, ‘the speech falls in the next part’; all listed above.

## Items for the owner (not for this part)

- `conventions.md`: the ῥήγεα row (10.352) and the shipped odyssey-012 and odyssey-027 disagree (‘blankets’ against ‘rugs’); the δόλος rows (‘trick’) and odyssey-003 (‘guile’) disagree.
- Glossary entries ἔβη and ἔγνω say ‘unaugmented’ and ‘no augment’, which is wrong.
- Shipped odyssey-007 and odyssey-016 render βουλήν τε νόον τε differently (‘plan and purpose’ against ‘counsel and the mind’); this part follows -016.
- 11.138: if the shipped line is ever made speaker-neutral, 11.138 should read “So he spoke, and I answered him and said.”
