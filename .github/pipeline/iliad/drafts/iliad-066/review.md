# iliad-066 (Iliad 11.221–327) — review

## Pass 1

Method: notes checked form by form against the line; every position claim and cross-reference checked against `units.json`, `packet.md` and the published parts (iliad-001…065, odyssey-001…120); Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks and `p`/`mark` placement checked by script and by hand; lines 226, 230 and 271 scanned by hand and with `scan_hexameter.py` (read-only). `t` untouched (verified identical to the packet's lines before and after). No modern translation opened.

Units are cited by the line they begin on. Severity: **major** = a translation error in `l` or a false statement in a note (grammar, position, cross-reference); **moderate** = a house-rendering departure or a claim the part cannot support; **minor** = wording, consistency, tidiness.

### Changes (line · field · severity · what was wrong · what was done)

| Line | Field | Sev. | Wrong | Done |
|---|---|---|---|---|
| 314–315 (unit at 314b) | `l` | major | “if the ships take Hector of the glancing helmet” reverses the case relations: νῆας is the object, κορυθαίολος Ἕκτωρ the subject of ἕλῃ (`i` was right). | `l` now “it will be, if the ships he takes, Hector of the glancing helmet.” |
| 262 | `n` | major | Said “Ἄϊδος εἴσω is ‘within Hades’, so the house of Hades is understood”. δόμον is in the line: δόμον Ἄϊδος εἴσω is “into the house of Hades”. | Rewritten: δόμον Ἄϊδος εἴσω “into the house of Hades”, εἴσω “within” standing last, δόμον the accusative of the place gone to. |
| 269 | `n` | major | “the τε after it [προϊεῖσι]” — the τε stands after τό, before the verb (τό τε προϊεῖσι). | “the relative τό ‘which’ has τε after it, which marks the general truth.” |
| 324 | `n` | major | “The whole unit is in the dual” — false: κυδοίμεον is plural (ἐκυδοίμεον for the pair), and κυσί, ὅμιλον are plural nouns. | Now lists the dual words (τὼ, ἰόντε, κάπρω, φρονέοντε, πέσητον) and says κυδοίμεον is plural. |
| 281 | `n` | major | “The Greek uses the dual only here” — false in this part: the dual recurs at 313 (παθόντε) and 324–326. | “The dual here is for the pair of horses, and the next unit goes back to the plural.” |
| 225 | `n` | major | Cross-reference wrong: “the line used of Bellerophon at 6.191”. The published unit starts at 6.191; αὐτοῦ μιν κατέρυκε… is its second line, 6.192. | 6.191 → 6.192. |
| 257 | `n` | major | “In the lines before and after, ὃ is a pronoun and the subject changes” — a position claim that is false (neither 256 nor 259 has ὃ). | “The subject changes here: ὃ is a pronoun, and it is Coön, not Agamemnon:” |
| 320 | `i` | moderate | “So he spoke, and struck Thymbraeus…” — the house rendering of ἦ καί in `i` is “So he said, and” (“So he spoke” is reserved for ὣς φάτο / ὣς ἔφατο; conventions rows 1.219, 1.528, 3.292). `l` “He spoke, and” was right. | `i` now “So he said, and struck Thymbraeus…” |
| 232 | `l` (line 3 of the unit, 234) and `n` | moderate | ζώνην rendered “belt” in `l`; the table has ζώνη “girdle” (iliad-012 ships “girdle” for ζώνην at 2.479; the Odyssey the same, odyssey-024, -050, -053) and ζωστήρ “belt”. The note did not say the two words name one piece. | `l` “on the girdle”; `i` keeps “belt” (it must show it is the same belt as 236); note gains: “ζώνη is ‘girdle’ in the word-for-word line, and it is the piece the next unit calls a ζωστήρ ‘belt’; the free English says ‘belt’ for both.” |
| 241 | `l`, `i`, `n` | moderate | ἀστοῖσιν ἀρήγων: `l` and `i` supplied “his” (“his townsmen”) that the Greek does not have (the Odyssey ships plain “townsmen” for ἀστοί, 63.192); the note said “the people of Troy, to whom he was an ally”, which the part does not show and which contradicts “his”. | `l` “helping the townsmen”; `i` “though he had come to help the townsmen”; note: “the citizens of Troy, for whom he had come to fight (the Greek says only ‘townsmen’, with no ‘his’).” |
| 321 | `n` | moderate | “Odysseus does the same to the charioteer” — the text says θεράποντα “attendant”; “charioteer” is not shown by this part. | “…to the attendant.” |
| 225 | `n` (metre) | minor | Flagged line 226 (UNRESOLVED): the note's metre sentence did not say the line is irregular as transmitted. Hand scan agrees with the scanner: αὐ-τοῦ | μιν κα-τέ | ρυ-κε δί | δου δ’ ὅ γε | θῡ-γα-τέ | ρα ἥν, the first syllable of θυγατέρα long as longum of foot 5, hiatus before ἥν (ϝήν). | Sentence now opens “The line is metrically irregular as transmitted:” and says “longum of the fifth foot”. |
| 229 | `n` (metre) | minor | Flagged line 230 (AMBIGUOUS, spondaic fifth). Hand scan: foot 3 ὼν ἐς Ἴ, foot 4 λι-ον, foot 5 εἰ-λη (spondee), foot 6 λού-θει; ον long before the digammated εἰληλούθει — the note's claims are true. | Sentence now opens “The line is metrically irregular as transmitted:”; nothing else changed. |
| 269 | `n` (metre) | minor | Flagged line 271 (UNRESOLVED). Hand scan: Ἥ-ρης | θυ-γα-τέ | ρες πι | κρὰς ὠ | δῖ-να-σι… θυ long as longum of foot 2 — the note's claim is true; the sentence did not say “irregular”. | Sentence now “The line (271) is metrically irregular as transmitted: …”. |
| 248 | `l` | minor | ῥά rendered “indeed” (“strong grief indeed him”); ἄρα/ῥα is “then” everywhere else in this part (225, 231, 254, 304, 309) and in the table. | “strong grief then him”. |
| 267 | `n` | minor | “The line comes round again as the last line of the simile” — 272 differs (ὣς ὀξεῖ’ for ὀξεῖαι δ’). | “…comes round again, with ὣς for δ’, as the last line…” |
| 269 | `n` | minor | “returns to Agamemnon in the words of line 268” — not word for word. | “in nearly the words of line 268 (ὣς for δ’).” |
| 292 | `n` | minor | “as of pigs elsewhere” asserts about the rest of the poem what this part cannot show. | Clause deleted. |
| 244 | `n` | minor | “a hundred cattle at once” — πρῶθ’ … ἔπειτα is “first … then”; “at once” is not in the Greek. | “a hundred cattle first”. |
| 227 | `i` | minor | “Straight from the bridal chamber” — “straight” is not in the Greek (the note already says ἐκ θαλάμοιο shows how soon he left). | `i` “Once he had married, he came from the bridal chamber after the fame of the Achaeans, with twelve curved ships that followed him.” |
| 236 | `l`, `i` | minor | `l` “yet he did not pierce” for οὐδ’ (“and not”); `l` “far before” and `i` “for long before that” differ from the Odyssey's shipped ἀλλὰ πολὺ πρίν (“but well before then” / “but long before that”, odyssey-006 ln 167). | `l` “and he did not pierce … but well before”; `i` “but long before that”. |
| 309 | `i` | minor | “So thick and fast” adds “fast” (πυκνά is “thick”). | “So thickly were the heads of the people overcome beneath Hector.” |
| 324 | `n` | minor | “fierce and turned at bay” is not in the text. | Replaced by “two boars that fall in among hunting dogs”. |

Totals: 23 findings acted on — **7 major, 4 moderate, 12 minor** (no critical). 23 fields changed in 22 units.

### Shared lines checked

**Iliad (published).** 11.226, 232, 260, 275, 276, 286–287, 291, 310: the whole unit or the shared line's `l` and `i` are identical to the published wording (226 = 6.192, 232 = 3.15, 260 = 4.469, 275 = 8.227, 276 = 2.79 / 9.17 / 10.533, 286–287 = 8.173–174, 291 = 5.470 / 6.72, 310 = 8.130); all cross-references in the notes verified against these (6.66 and 6.110 for the μακρὸν ἀΰσας line also verified).

**Odyssey (grep of odyssey-001…120 for every line of the part, and for every run of three or more words).** Agree with the Odyssey: 238 εὐρὺ κρείων Ἀγαμέμνων; 239 ἐκ δ’ ἄρα χειρός; 243 πολλὰ δ’ ἔδωκε; 247 βῆ δὲ φέρων; 248 τὸν δ’ ὡς οὖν ἐνόησε (and the table's row 3.21); 254 τ’ ἄρ’ ἔπειτα; 263 δόμον Ἄϊδος εἴσω; 276 ἡγήτορες ἠδὲ μέδοντες; 280 ἵμασεν καλλίτριχας ἵππους; 281 τὼ δ’ οὐκ ἀέκοντε πετέσθην (`l` and `i` identical to odyssey-013, 3.484); 287 θούριδος ἀλκῆς; 295 βροτολοιγῷ ἶσος Ἄρηϊ; 311 καί νύ κεν; 314 ἀλλ’ ἄγε δεῦρο πέπον, παρ’ ἔμ’ ἵσταο (“good one” / “my good fellow”); 316 τὸν δ’ ἀπαμειβόμενος προσέφη (reply formula); 318 ἔσσεται ἦδος (“pleasure”). Changed to agree: 236 (above). Departures, kept: **253 ἀκωκή “tip”** where the Odyssey ships “point” (odyssey-096, ln 452, δουρὸς ἀκωκή); `new-renderings.md` gives the reason (“point” is kept for αἰχμή, which this part has at 237) but its row does not say it departs from the Odyssey — the drafter or the caller should add that. **312 κέκλετ’** (“called” / “called on” for the table's “gave orders to”) is recorded in `new-renderings.md` with its reason. 291 ὄτρυνε “urged on” (Odyssey “roused”) is the published Iliad wording of the same whole unit (iliad-031), which governs.

### Findings considered and refused

- **226, extra licences.** The scanner also puts a long μιν in the thesis of foot 2 and a long final syllable of θυγατέρα before ἥν; it names neither as a licence. The note keeps one sentence, on the licence the scanner and the hand scan agree on (θυγατέρα, longum of foot 5).
- **230, AMBIGUOUS.** Both scansions agree on what the note says (ον long before εἰληλούθει, spondaic fifth); the ambiguity is only the quantity of the iota of Ἴλιον, which the note does not claim.
- **312 κέκλετ’ “called on”** against the table's “gave orders to”: kept; the departure is recorded, the Greek verb is “call on, urge”, and “ordered” would make Odysseus Diomedes' commander. 285 ἐκέκλετο keeps the table's “gave orders to” in `i` (Hector commands his own army).
- **253 ἀκωκή “tip”** (see above): kept for the αἰχμή/ἀκωκή distinction in one part; only the missing mention of the Odyssey line is raised.
- **248 οὖν “then”** in “Him then as he noticed”: the Odyssey's `l` omits it, but the Iliad table row (3.21, 5.95) has exactly this wording.
- **278 `i` “has not allowed”** for the aorist εἴασε: acceptable in direct speech (“Zeus has not allowed me”), `l` keeps “allowed”.
- **317 `l` “I shall stay”** against the Odyssey's “I will stay”: both “shall” and “will” stand in the published first-person `l`s; the Odyssey's line is a different sentence.
- **326 `i` “rushing back into the fray”** supplies a goal for πάλιν ὀρμένω: left as a fair reading of an elliptical participle; `l` and the note say “rushing back”.
- **259 `i` “his bossed shield”**, **261 `i` “standing beside him”**: the possessive and the pronoun are natural readings (the shield is Coön's; “him” can only be Coön, whose head is cut off); no ambiguity a reader would stumble on.
- **285 note “the line is the same shape as 6.66 and 6.110”**: verified (μακρὸν ἀΰσας ends both; also 8.172).
- **229 note “Percote, a town in the Troad”**, **225 note on γήμας “said of the man”**: geographical and grammatical facts a tutor would give; nothing in the part contradicts them.
- **Quotation marks and `p`/`mark`.** Checked and correct: opens on 276, 286, 313, 317; closes on 279 (unit 276), 290 (unit 289b), 315 (unit 314b), 319 (unit 317b); `mark` on the first unit of each of the four speeches; `p` on the ten paragraph starts (221, 248, 264, 280, 284, 291, 299, 310, 316, 320) and nowhere else. The previous part's last unit (iliad-065) is a narrator's question, so no speech runs on into this part; the last speech here closes inside it.
- **Raised-dot notes.** Every “stops at the raised dot” claim (14 units) checked against the end of `t` and the half-line named.
- **Greek → `l` word by word and `l` ↔ `i`** for all 56 units: no other error found beyond the table; `l` and `i` differ only where the convention allows (word order, particles dropped from `i`, formula wording).

## Pass 2 (gloss pass)

Method: every one of the 134 novel entries in `gloss.json` checked against each line where the form occurs (case, number, tense, mood, voice, agreement, Attic equivalent, homographs, article-forms, possessive vs relative ὅς), against the unit's `l`, `i` and note; entry length (all under 230), typographic ’ only, no line numbers or "here"; the 9 `__broaden__` entries checked for old-entry-whole + ` · ` + new reading, the old text compared character for character with `iliad-glossary.json`; and all 412 known forms re-read against their use in this part to see whether the existing entry covers it. Coverage by script: every word form of `t` is in the glossary or `gloss.json`; `gloss.json`'s keys equal `novel-forms.json`. `units.json` was not changed in this pass (verified byte-identical before and after); `t` untouched. All 9 original `__broaden__` entries were verbatim-correct; 10 more were added.

### Changes (form · field · severity · what was wrong · what was done)

| Form | Where | Sev. | Wrong | Done |
|---|---|---|---|---|
| αἷμ (known) | `__broaden__` (new) | major | Existing entry says "neut. acc. sg., elided"; in 265 αἷμ’ is the subject of ἀνήνοθεν, nominative. | Added " · also neut. nom. sg., elided (αἷμ’ = αἷμα), subject". |
| φαεινοῦ (known) | `__broaden__` (new) | major | Existing entry "masc. gen. sg., agreeing with πέπλοιο"; in 253 it agrees with δουρός, neuter. | Added " · also neut. gen. sg., agreeing with δουρός". |
| ὀφέλτιον (known) | `__broaden__` (new) | major | Existing "Opheltius, a Trojan" (iliad-036, 6.20); the Opheltius of 11.302 is in the list of Danaan leaders (ἡγεμόνας Δαναῶν, 304). | Added the Danaan namesake. The old text stays (additions only). |
| ἀγέλαον (known) | `__broaden__` (new) | major | Existing "Agelaus, a Trojan" (iliad-048, the son of Phradmon); the Agelaus of 11.302 is a Danaan leader, as above. | Added the Danaan namesake. |
| πολλὸν | `__broaden__` | moderate | New reading "with κυλίνδεται: ’much, greatly’" contradicts the unit: `i` “the wave rolls on, greatly swollen” and the note “πολλόν is ‘greatly’” take it with τρόφι (also `new-renderings.md`: πολλὸν τρόφι “greatly swollen”). | Reading now "adverbial, with τρόφι: ’greatly’ (πολλὸν … τρόφι ’greatly swollen’)". |
| ἀνεμοτρεφὲς | entry | moderate | Entry asserted "grown tall in the wind (of a spear’s ash shaft)", a sense and a wood the note says are not known. | "wind-nurtured (of a spear); meaning not known, ’grown in the wind’ is a guess"; parse "adj. of two endings, neut. acc. sg." |
| ἀργεστᾶο | entry | moderate | Lemma ἀργέστης (accent on the penult) disagrees with the printed gen. -ᾶο and the Attic equivalent -οῦ named in the same entry (both point to an oxytone ἀργεστής); the meaning was stated as "bright, clearing" with only "sense not certain", whereas the note says "its meaning is not known, ‘bright’ is the usual guess". | Lemma ἀργεστής; "meaning not known, ’bright’ the usual guess" (agrees with `l` “bright”). |
| λελάσμεθα | entry | moderate | No Attic equivalent named for the Homeric form; "present sense" next to the gloss ’have we forgotten’ read as contradictory; lemma gave only λήθομαι though the note says λανθάνομαι. | "mid. λανθάνομαι, λήθομαι … perf. 1 pl. mid., epic λέλασμαι (= Attic λέλησμαι), present force: ’have forgotten, forget’". Parse itself (perfect, 1 pl., + gen. θούριδος ἀλκῆς) verified. |
| ὀρμένω | entry | moderate | "pres. part." asserted a tense the line does not settle (ὀρμένος is the syncopated 2nd-aorist participle of ὄρνυμι in the usual account, with pres. ὀρνύμενος). | "mid. part. (syncopated 2nd aor.) masc. nom. dual: ’rushing’" (dual nom., agreeing with the two heroes: verified). |
| ἀργύρῳ (known) | `__broaden__` (new) | moderate | Existing "dat. of material: ’with silver’"; in 237 it is the dative object of ἀντομένη (note: "ἀντομένη ‘meeting’ goes with αἰχμή"; `l` “against silver meeting”). | Added the object-of-ἀντομένη reading. |
| ὁπότε (known) | `__broaden__` (new) | minor | Existing "+ opt. in a general clause"; 305 has the aorist subjunctive στυφελίξῃ, no κε. | Added " · also + aor. subj. in a general temporal clause, with no κε". |
| χειρὸς (known) | `__broaden__` (new) | minor | Existing separative reading names ἀπό in tmesis; 239 has ἐκ … σπάσσατο. | Added "with ἐκ in tmesis: ’out of the hand’". |
| ἠέ (known) | `__broaden__` (new) | minor | Existing "than (after a comparative)"; 317 δοῦναι κράτος ἠέ περ ἡμῖν has no comparative (preference after βόλεται). | Added "after a verb of wishing, with no comparative: ’rather than’". |
| κλέος (known) | `__broaden__` (new) | minor | Existing readings are both "object"; in 227 it is governed by μετά (‘after the fame’). | Added "governed by μετά: ’after the fame’". |
| ὄφρά (known) | `__broaden__` (new) | minor | Existing readings are "so that … with the subj."; 265 has ὄφρά + indicative, "as long as". | Added "ὄφρα + indic., temporal: ’so long as’". |
| ζώνην | `__broaden__` | minor | New reading quoted ’at the belt’ but `l` (after pass 1) is “on the girdle”. | ’at the girdle’; old entry unchanged. |
| ἀΰτει | entry | minor | Did not say the form is contracted (-εε → -ει); "= ἠΰτει" lacked "Attic". | "unaugmented, contracted -εε → -ει (= Attic ἠΰτει)". Parse (impf. 3 sg., after ἕλκε) verified; accent excludes pres. ἀϋτεῖ. |
| τρόφι | entry | minor | Form class stated flatly ("adj., neut. nom. sg."); the construction is itself uncertain. | "adj. (or adv.) … sense and form not certain". |
| ὑπεραέϊ | entry | minor | Note and `new-renderings.md` say the sense of ὑπερ- is not certain; the entry did not. | Added "(sense of ὑπερ- not certain)". |
| ἔνερθε | entry | minor | "adv., also prep." — at 232 and 252 it is a preposition + gen. (θώρηκος, ἀγκῶνος). | "prep. + gen., also adv.: ’below’". |
| αἶγας | entry | minor | "fem. acc. pl." — αἴξ is of common gender. | "masc./fem. (common gender) acc. pl." |
| καρήαθ | entry | minor | No Attic equivalent of κάρηα named. | Added "(= Attic κάρα)". |
| ἀνήνοθεν | entry | minor | Root is uncertain (note in `new-renderings.md`); the entry was silent. | Added "root uncertain". |
| ἀκωκή | `new-renderings.md` | minor | The row did not state that "tip" departs from the Odyssey’s "point" (odyssey-096, δουρὸς ἀκωκή), as pass 1 asked. | Row now says it departs, and why (αἰχμή and ἀκωκή both in 11.237 and 11.253; "point" is the house word for αἰχμή). |

Totals for pass 2: 24 findings acted on — **4 major, 6 moderate, 14 minor** (no critical). 23 `gloss.json` fields changed (11 entries rewritten; 2 `__broaden__` entries fixed and 10 added) plus the `new-renderings.md` row. Note for the owner: the shipped entries ὀφέλτιον ("a Trojan", iliad-036) and ἀγέλαον ("a Trojan", iliad-048) are correct for their lines; the two new readings are for namesakes.

### Findings considered and refused

- **ὀξεῖ, ὄϊς, λίς homographs.** ὀξεῖ’ (elided fem. nom. pl.) is also the dat. sg. ὀξεῖ; ὄϊς is also nom. sg.; λίς “lion” is also “smooth rock” (the Odyssey glossary has that reading). This part uses only one reading of each, and the rule is additions-only: a later part that meets the other reading broadens the entry. Kept.
- **πανημέριον** "neut. acc. sg. used as an adverb": a masc. acc. agreeing with ἐμέ is also grammatically possible, but LSJ takes it adverbially and the sense is identical. Kept.
- **στήθεα** "neut. acc. pl." (kept; a "nom./acc." label was considered): the note takes it as the accusative of the part after ἄφρεον, and `l` “foamed at the chests” agrees; a nominative reading would need a different `l`.
- **πέσητον** (3 dual; the 2 dual is spelled alike): the two boars are the subject, so the parse is right; not a homograph a reader meets here.
- **βροτολοιγῷ** entry "man-destroying, bane of mortals" against `l` “mortal-ruining”: the meanings agree and `i` says “the ruin of mortals”; the entry names both senses.
- **ἔλεγχος** "neut. nom. sg." (masc. in Attic): neuter in Homer (cf. ἐλέγχεα); right for this line. Left unchanged.
- **κέκλετ** (known) "called out to (+ dat.)" against `l` “called” and `i` “called on”: the entry is the existing wording and covers the use.
- **ἄορί, ἔγχεΐ, μεγάλοισί** accent claims ("before the enclitic τε"): checked, true (proparoxytone + enclitic). Kept.
- **ἐπεί/ἐπί, κατά, ἐν, ὑπό, τοῖο, τόν, ὅ, ἥν, ἧς and the other article-forms and the possessive ὅς** in 225 (ἥν) and 243 (ἧς relative): existing entries already cover the uses in this part (ἥν has the possessive reading; ἧς is the relative). No broadening needed.
- **ἐκέκλετο, ἕκτορι ("for Hector" against ὑφ’ Ἕκτορι “beneath Hector”)**: the existing entry gives the dative form and the preposition’s entry gives the construction; left.
