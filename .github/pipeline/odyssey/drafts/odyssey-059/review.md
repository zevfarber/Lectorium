# odyssey-059 review (Odyssey 12.192–278), pass 1

Reviewer, pass 1 only (a second pass with `gloss.json` follows). Checked: every grammatical label, positional claim and
cross-reference in every note against the line and the source text (`source/odyssey-murray1919.json`); Greek → `l` word by
word; `l` ↔ `i`; remembered English in `i`; quotation marks; the flagged line 267 scanned by hand. `t` was not touched
(verified against the before-copy, and the joined `t` still equals Murray 12.192–278). Line division of `l` equals that of
`t` in every unit; no `\n` in any `i`; no ASCII quotes or backticks in `l`/`i`/`n`; `ln` and `p` verified against the
source (¶ at 192, 201, 208, 222, 234, 260, 271, 277). No modern translation consulted.

Counts: **0 major, 5 moderate, 15 minor** (20 rows; the quotation-mark conversion is one moderate row across four
units). 10 findings considered and refused (below).

Severity: major = a wrong fact or wrong quotation state that would ship; moderate = a false grammatical label, false
positional claim, wrong force in `i`, or a convention break; minor = imprecise wording, ambiguous cross-reference, small
inconsistency between note and layers.

## Changes

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 208, 219, 271, 276 (the four speech-edge units) · `l`, `i`, `n` | MODERATE | Quotation marks were single ‘ ’. `conventions.md` (“English layers carry ordinary “ ” quotation marks round speech”) and the runbook (“ on a speech’s first unit, ” on its last) require double marks, and `validate_odyssey.py` counts only “ ” (so single marks escape its balance check). Odyssey-001…039 ship “ ”; 040…058 (incl. 058) drifted to ‘ ’ (see “Outside this part”). The two speeches here are 12.208–221 and 12.271–276; neither runs on from or into a neighbouring part (058’s last unit closes the Sirens’ speech at 191; 12.192 is narration; Eurylochus’s speech begins after 278). | Opening “ on the first unit of each speech (208, 271), closing ” on the last (219, 276), in both `l` and `i`: 4 + 4, balanced. The notes of units 219 and 276 said “closes the single mark”; now “closes the quotation”. |
| 235 · `n` | MODERATE | “Scylla has none until line 245.” Line 245 has Σκύλλη, but its verb ἕλεθ’ is the first word of line 246 (ἓξ ἕλεθ’). | “until ἕλεθ’ in line 246”. |
| 219 · `n` | MODERATE | βάλῃσθα called “the second singular aorist **middle** subjunctive”. It is the active aorist subjunctive of βάλλω with the old 2 sg ending -σθα (= βάλῃς); ἐς κακὸν ἄμμε βάλῃσθα has an active sense and object. | “second singular aorist subjunctive active with the old ending -σθα (= βάλῃς)”. |
| 219 · `l`, `i`, `n` | minor | μή σε λάθῃσι rendered “lest she escape you” (`l`) / “in case she escapes you” (`i`): that reads as slipping out of his control; λανθάνω with the accusative is “escape the notice of”. `n` also said κεῖσ’ points “back toward the smoke and wave”, which the line does not say. | `l` “lest she escape your notice” (line division unchanged); `i` “in case she darts off that way unnoticed by you, and you cast us into evil”; `n` “escape your notice”, and κεῖσ’ “presumably toward the smoke and wave”. |
| 214 · `i` | MODERATE | αἴ κε δώῃ rendered “in case Zeus may … grant”. “In case” means a precaution (it is what μή needs, and is used correctly at 219 and 223); αἴ κε is “if perhaps”, a hope. The force was reversed. | “if Zeus may somehow grant that we flee from this destruction and escape it” (`l` already had “if somehow”). |
| 195 · `i` | minor | “pulled them tighter”: ‘them’ (the bonds) is not in the Greek; the object of πίεζον is the same μ’ (‘me’) as δέον, and the verb is ‘press’. | “and pressed me tighter”. |
| 195 · `n` | minor | “Eurylochus speaks again in the last unit of this part.” He does not speak in this part: the last unit only introduces his reply (278), which comes in the next part. | “is named again as the speaker in the last unit of this part”. |
| 201 · `n` | minor | “the strait itself is named at 235–236”: στεινωπόν is 234 (235–236 name Scylla and Charybdis). | “234–236”. |
| 206 · `n` | minor | “The second line is the formula already met at 10.172–173”: only the second line (12.207 = 10.173) is repeated; 10.172 differs from 12.206. | “already met at 10.173”. |
| 211 · `i` | minor | “through my own excellence”: ἐμῇ is ‘my’, not emphatic ‘my own’ (the table keeps “own” for the possessive ὅς and for ἐμοῖς … ὀφθαλμοῖσι). “one day we shall remember”: που is ‘perhaps’; “one day” adds a time not in the Greek (the future infinitive carries the future). | “through my excellence”; “and I think that perhaps we shall remember this too”. |
| 226 · `n` | minor | Cross-reference “(from about line 116)” was vague. Checked against the source: Circe’s warning against lingering to fight Scylla is 12.116–126 (121–123: ἢν γὰρ δηθύνῃσθα κορυσσόμενος παρὰ πέτρῃ …; 120: φυγέειν κάρτιστον). | “(12.116–126, especially 121–123)”. |
| 234 · `n` | minor | στεινωπόν labelled “accusative of the way”, which is not a construction the conventions or Smyth name; it is simply the object of the compound verb ἀνεπλέομεν. | “the object of ἀνεπλέομεν, ‘sailed up’ it”. |
| 240 · `i`, `n` | minor | ὑπένερθε rendered “far below” (`i`, `n`): ὑπένερθε is ‘below, beneath’; “far” is not in the word. | “below”, in both. |
| 240 · `n` | minor | ἐβεβρύχει only “a reduplicated past form of βρύχω”, leaving the reader unable to place it. Hedged as the drafter flagged (see refused list: the parse is not forced). | Added “probably a pluperfect used like an imperfect”; sense “would roar” unchanged. |
| 247 · `n` | MODERATE | τῶν … ἀειρομένων called “the genitive absolute”. It is not absolute: τῶν is attached to πόδας καὶ χεῖρας (‘their feet and hands’) in the same clause, and the participle agrees with that τῶν. | “τῶν ‘of them’, which goes with πόδας καὶ χεῖρας and is agreed with by the participle ἀειρομένων ‘as they were lifted’”. |
| 260 · `n` | minor | “the next island is in view”: the text only says they reach it (ἱκόμεθ’), nothing about sighting. | “they reach the next island”. |
| 262 · `i` | minor | “There were fine cattle there, broad of brow”: second “there” duplicates the first (ἔνθα is one word). | “There were fine cattle, broad of brow,”. |
| 264 · `n` | minor | αὐλιζομενάων glossed “lodging in the fold”, while `l` says “in the yard” (αὐλή is the court/yard). | “lodging in the yard”, matching `l`. |
| 266–267 · `n` | minor | μάντηος left unexplained although the form is Homeric; the packet flagged line 267 (see scansion below). | Added “μάντηος being the epic genitive of μάντις (Attic μάντεως)”; and, line 267 being irregular as transmitted (hand scan below), one plain sentence appended: “Line 267 (μάντηος ἀλαοῦ, Θηβαίου Τειρεσίαο) is metrically irregular as transmitted: the final short syllable of μάντηος has to be counted long at the start of the second foot, before ἀλαοῦ.” (Same wording and verdict as odyssey-050, where the same two words stand at 10.493.) |
| 275 · `l` | minor | Unit begins mid-sentence after the preceding ·, and `i` correctly starts “for”; `l` began “For” with a capital, and dropped the iterative of ἔφασκεν (which the note itself stresses: ‘she kept saying’). | “for there the most fearsome evil to be for us she kept saying.” |

## Scansion of line 267 (by hand)

μάντηος ἀλαοῦ, Θηβαίου Τειρεσίαο. Syllables, with quantities: μάν (long, closed) · τη (long, η) · ος (short) · ἀ (short,
privative) · λα (short) · οῦ (long, diphthong) · Θη (long) · βαί (long) · ου (long) · Τει (long) · ρε (short) · σί (short) ·
α (long, -αο genitive) · ο (final). Fourteen syllables, so two dactyls and four spondees. Feet 3–6 are regular and fall out
unaided: οῦ Θη | βαί ου | Τει ρε σί | α ο. That leaves μάν τη ος ἀ λα for the first two feet: μάν τη is a spondee, and the second foot
ος ἀ λα can be a dactyl only if ος, short by nature and followed by a vowel (so not lengthened by position), is counted long in
the thesis. The alternative, taking μάντηος with synizesis (μάν-τηος, two syllables), leaves ἀ λα οῦ with two shorts to open
a foot and no long to carry it, so it fails. The scanner’s second (“ambiguous”) reading differs only in the quantity of the α of ἀλαοῦ, not in the
licence needed at foot 2. So the irregularity is real and the scanner’s licence is the right one; the sentence in the note
is therefore true. The same two words are scanned and annotated in the same way in odyssey-050.

## Checked and found true (no change)

All other labels checked against their line: ἱεῖσαι, φάσαν, νευστάζων, προπεσόντες, δέον, ἀνστάντες, παρήλασαν, tmesis
ἀπὸ … ἕλοντο, ἄλειψ’, ἐλείπομεν, ἴδον/ἄκουσα, ἔπτατ’, ἔσχετο, ὤτρυνον, εἰμεν, εἴλει, σπῆι, -φι endings (κρατερῆφι βίηφιν,
βίηφι), ἐκφύγομεν, ὀίω, μνήσεσθαι, πειθώμεθα, κώπῃσιν, ῥηγμῖνα, δώῃ, ὑπεκφυγέειν, κυβερνῆθ’ (θ before rough breathing),
βάλλευ (-ευ for -εο), οἰήια, ἔεργε, ἐπιμαίεο, ἐξορμήσασα, ἐμυθεόμην, ἀπολλήξειαν, δοῦρε (dual), καταδύς, ἴκρια, ἐδέγμην,
φανεῖσθαι, dual ὄσσε, ἔκαμον, γοόωντες, ἀνερροίβδησε, ἐξεμέσειε, ἀναμορμύρεσκε, φάνεσκε (iteratives), ἀναβρόξειε, ᾕρει,
ἕλεθ’, ἐνόησα, φθέγγοντο, καλεῦντες, προΐησι, ἀείροντο, κεκληγῶτας, δηιοτῆτι, οἴκτιστον, ἐμόγησα, ἱκόμεθ’, ἔσαν, ἐών,
ἔμπεσε, ἐπέτελλε, ἀλεύασθαι, μετηύδων, κέκλυτε, ἔφασκεν, ἄμμιν, ἔμμεναι, κατεκλάσθη, ἠμείβετο. Positional claims checked
against the source: every “ends at the ano teleia in the middle of line N” (194, 204, 217, 243, 249, 262, 266; 230 for πρῴρης;
“νηῦς stands at the start of the next line”, 205; “ἐνὶ θυμῷ … 217”). Cross-references checked: 10.173, 10.178, 10.189, 10.198,
10.138 (φαεσιμβρότου Ἠελίοιο), 12.153 (the opening line of 058’s unit), 12.176 (Ὑπεριονίδαο), 12.127–128 (Θρινακίην … ἴφια
μῆλα), 195 (Eurylochus), 196 and 199–200 (bonds, wax), 219 (smoke and wave), 235–236. Repeated lines: 207 (= 046 unit, its `l`/`i`
reproduced for that line), 222 (the published `l`/`i` for that line carried over), 270 (identical to 058’s unit 153, `l` and `i`
verbatim), 271 (the line’s `l`/`i` equal 047’s apart from the comma/punctuation the unit text itself differs in), 277 (047’s
wording for that line), and 273–274 = 268–269 word for word in both layers. House renderings checked in the table and
followed: κληῖσι “the rowing-benches”/“the oarlocks” (row at 9.103), ἐρίηρες ἑταῖροι “trusty companions”, χλωρὸν δέος “pale
fear”, ἠεροειδέα “misty-looking”, δῖα “heavenly”, στυγερῷ μύθῳ “hateful”, φαεσίμβροτος (the model for τερψίμβροτος), κλυτά
“famous”, and every row of `new-renderings.md`.

## Findings considered and refused

1. **ἕπει (209).** Murray prints ἕπει, read as ἕπω ‘be about, attend’. The drafter’s `l` “is upon us” and the note’s “the form is
   unusual” already say the parse is not certain, and I can verify no better form from LSJ/Autenrieth/Cunliffe without the
   apparatus. Alternative parsings would change only the label, not the sense. Left hedged.
2. **προήκεα (205).** ‘Tapering’ (προήκης) is the LSJ/Autenrieth gloss; the note says “usually taken as”. Left.
3. **κληΐς (214).** Table row at 9.103 fixes “the rowing-benches” in `l` and “the oarlocks” in `i`, and the note already says the
   exact object is not certain. Left; the oddity of “sitting at the oarlocks” is the house rendering’s, not this part’s.
4. **ἐβεβρύχει (242).** Only a clarification was added (“probably a pluperfect used like an imperfect”); a firmer label is
   not provable from the aids, so the hedge stays.
5. **δόλον κατὰ εἴδατα (252).** “Casting a lure among baits” is a poor but honest rendering of an uncertain phrase, and the
   note says the construction is not certain. I considered “down for food” but cannot show it is better; refused to substitute
   one guess for another. Note stays hedged.
6. **“And they” (`l`, 194) against “but they” (`i`).** δέ is both; `i` needs the contrast with the bound Odysseus, `l` stays
   literal. Not an inconsistency of sense.
7. **“strangers to trouble” (208), “huddle … inside” (225), “to my cost” (230).** Each rebuilt from the Greek (ἀδαήμονες
   ‘unversed’, πυκάζοιεν ‘pack/cover closely’, dative of disadvantage μοι); none reproduces a phrase I can identify as remembered
   from a translation, and no replacement is demonstrably closer. Left. “Sitting at the oarlocks” and “distress beyond remedy”
   are table renderings.
8. **ἀρετῇ ‘skill in a crisis’ (211) and ἔνθεν ‘from the Cyclops’s cave’.** Interpretive but argued in the note from the context;
   not a false label. Left.
9. **The same `mark` “Odysseus speaks to his companions” on 208 and 271.** Both are speeches to the crew; a second one at 271 follows
   a narrative intro (270). Accurate; “again” would be a stylistic choice and the shipped marks do not use it. Left.
10. **ἦ τοι (237) not rendered in `i`.** Present in `l` (‘Truly’), a weak emphasis that the English “Whenever … would”
    already carries; dropped from `i` on purpose and the note glosses it. Left.

## Outside this part (for the owner, not touched here)

- **Quotation-mark style drift.** Odyssey-001…039 use “ ” (as `conventions.md` and the validator require); odyssey-040…058
  use ‘ ’, and 058’s review says it followed that “single-mark style used for the other speeches”. 059 now uses “ ” per
  the written rule; 040–058 were not edited (not this part’s files). Either those parts should be converted, or
  `conventions.md`, the runbook and `validate_odyssey.py` (which counts only “ ”, so ‘ ’ parts are unchecked) should be
  amended to the single mark. This is a decision for the owner; the 059 choice follows the standing text.
- Published 12.271 (odyssey-047 unit at 10.189) carries a ‘ in `l`/`i`; the 059 unit’s text differs (no comma, longer unit), so
  the validator’s identical-unit rule does not apply, and the English of that line was kept word for word except the mark.

## Pass 2

Reviewer, pass 2. Redid the whole review on the current `units.json` (every note label against its form and line, every
positional claim and cross-reference against `source/odyssey-murray1919.json`, Greek → `l`, `l` ↔ `i`, remembered English,
quotation marks, line 267 re-scanned) and, new in this pass, read every house-rendering row of `conventions.md` that touches
a word of this part (179 rows). Then checked every entry of `gloss.json`: all 110 novel forms and the 11 `__broaden__`
entries against the lines, and all 314 forms of `known-forms.json` for whether the existing entry covers the use here.
`t` untouched (verified against a before-copy and against Murray 12.192–278 with whitespace removed); `l` keeps `t`’s line
division in every unit; no `\n` in `i`; no ASCII quotes or backticks; “ ” balanced 2/2 in `l` and in `i`, on 208/219 and
271/276; `ln`, `p`, `mark` re-verified. Pass 1’s edits were all re-checked and stand. No modern translation consulted.

Counts for pass 2: **0 major, 6 moderate, 10 minor** (16 rows). 10 findings considered and refused (below).
(Both passes together: 0 major, 11 moderate, 25 minor.)

### Changes (pass 2)

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 235 and 240 · `l`, `i`, `n` | MODERATE | “briny water” for ἁλμυρὸν ὕδωρ. The table row ἁλμυρὸν ὕδωρ (9.470) fixes “the salt water” in both layers and lists “briny water” among the renderings avoided on purpose. Pass 1 said it had checked the table and missed this. | `l` “the sea’s salt water” (235, 240); `i` “the salt water of the sea” (235, 240); note at 235 “ἁλμυρὸν ὕδωρ is ‘salt water’”. |
| 256 · `l`, `i`, `n` | MODERATE | “in fearsome strife” for ἐν αἰνῇ δηιοτῆτι. The table row δηιοτής (11.516, the identical words) fixes “fighting” and reserves “strife” for ἔρις. | `l` and `i` “in fearsome fighting”; note “‘fighting, battle’”. |
| 249 · `n` | MODERATE | καλεῦντες called “the uncontracted participle of καλέω”. It is the epic form (ευ for εο) of καλέοντες, i.e. the contracted-looking form (Attic καλοῦντες), as the glossary entry already says; καλέοντες would be the uncontracted one. | “the epic form of the participle of καλέω ‘call’ (= καλέοντες, Attic καλοῦντες)”. |
| 223 · `n` | MODERATE | μή πώς … ἀπολλήξειαν labelled “a clause of fear”. It follows οὐκ ἐμυθεόμην, a verb of not telling, and gives the reason for silence: a negative purpose clause (‘lest’), as `l` and `i` render it; no verb of fearing governs it. | “a negative purpose clause with the optative after a past tense”. The same wrongly worded label in `gloss.json` (ἀπολλήξειαν, πυκάζοιεν, βάλῃσθα) is corrected below. |
| gloss ἀνεπλέομεν | MODERATE | “= Attic ἀνεπλέομεν, contracted -πλοῦμεν”: the Attic equivalent given is the same form as the headword, and contradicts itself. | “epic uncontracted (= Attic ἀνεπλοῦμεν)”. |
| gloss πίεζον (known form, 196) | MODERATE | The existing entry is “impf. 1 sg.” only; in 196 the form is 3 pl. (Perimedes and Eurylochus pressed). | `__broaden__` entry: old entry whole + “also impf. 3 pl.: ‘they pressed’”. |
| 245 · `l`, `i`, `n` | minor | φέρτατοι rendered “strongest”. The table row φέρτατος (11.478) is “the best” and lists “mightiest”, “bravest”, “noblest” as renderings avoided because each narrows the word; “strongest” narrows it in the same way, and χερσίν τε βίηφί τε already says in what. | `l` “were the best”; `i` “the ones who were best in hands and in might”; note “‘who were the best’”. |
| 247 · `i` | minor | “lifted high above me”: ‘me’ is not in the Greek (ὕπερθεν ὑψόσ’ ἀειρομένων is absolute). | “lifted high above”. |
| 251 · `l` | minor | δόλον κατὰ εἴδατα “a trick, over baits” in `l` but “among baits” in `i` and in the note. | `l` “a trick, among baits, casting”. |
| gloss κατήσθιε | minor | “epic (= Attic κατήσθιεν)”: the form differs from Attic only by the absence of movable ν, which Attic also allows; “epic” is misleading. | “impf. 3 sg., without movable ν (= κατήσθιεν)”. |
| gloss πλείοσί | minor | “uncontracted πλείοσι”: πλείοσι is not an uncontracted form of anything; it is simply the dative plural of πλείων. | “comp. πλείων, masc. dat. pl.”. |
| gloss στεινωπὸν | minor | “masc. acc. sg.” given with confidence; the gender of στεινωπός as a noun is not shown by the line (στεινωπόν could be neuter) and the aids do not settle it. | “acc. sg., used as a noun”; Attic equivalent kept. |
| gloss κέρας | minor | Clumsy parenthesis “(the horn of the ox as part of the line)” added nothing and was not a parse. | “neut. acc. sg., object of προΐησι”. |
| gloss ἀνερροίβδησε | minor | Lemma ἀναροιβδέω (one ρ); LSJ and the note to 235 have ἀναρροιβδέω. | Lemma corrected; added ‘it sucked down’. |
| gloss κάλλιμον (known form, 192) | minor | Existing entry “masc. acc. sg., agreeing with χρόα”; here it agrees with fem. ὄπα. | `__broaden__`: old entry whole + “also fem. acc. sg. (two-ending adjective), agreeing with ὄπα”. |
| gloss ἠεροειδέα (known form, 233) | minor | Existing entry “masc. acc. sg.”; here it agrees with fem. πέτρην. | `__broaden__`: old entry whole + “also fem. acc. sg. (two-ending adjective), agreeing with πέτρην”. |
| gloss βάλῃσθα, ἀπολλήξειαν, πυκάζοιεν | (with 223) | “in a fear clause after μή” (see 223). | “in a ‘lest’ clause after μή” (βάλῃσθα), “in a negative purpose clause after μή” (the other two). |

All other novel entries were checked against the line (case, number, tense, mood, voice, the Attic equivalent, and that the
lemma is the one LSJ uses) and are left as drafted; all 11 original `__broaden__` entries keep their old entry whole and
add a reading this part really uses (κέ, κακὸν, κακόν, παρὲξ, πόδας, σφέας, τοῖς, τόνδε, ἐρετμά, ὅτ’, ὡς). Every form of
the part has an entry (none missing); every new entry is under 230 characters, with only ’ … ’ quotation, no line numbers.
The two flagged-by-gloss risks, ἀμύμων and ἐρίηρος, are already marked as of uncertain meaning in their old entries.

### Findings considered and refused (pass 2)

1. **τοῖσιν (277) not broadened.** Existing “masc. dat. pl. ‘from/to them’” covers a dative of interest (‘in them’); the
   note says ‘in them’ and the entry’s ‘to’ is the dative.
2. **κατὰ (252, κατὰ εἴδατα) not broadened.** The old entry’s first reading is “down, throughout, in”, and the note already
   says the construction is not certain; adding ‘among’ would only be adding a second guess.
3. **ἕπει (209) and ἐβεβρύχει (242).** Same verdict as pass 1 (items 1 and 4): hedged in the note, nothing in LSJ /
   Autenrieth / Cunliffe that fixes a better parse; the glossary entries state the usual parse without line numbers.
4. **αὐτούς (225) not broadened.** Existing entry has the intensive reading ‘the very men themselves’, which is what
   σφέας αὐτούς shows; σφέας is broadened for the reflexive use.
5. **“the ground” in `i` (242) beside γαῖα “the dark earth” in the table.** The table row γαῖα μέλαινα keeps “earth” for
   the earth as a whole; here γαῖα is the sea-floor and `l` has “earth”; `i` varying to “ground” is not a rendering of a
   fixed formula. Left.
6. **“settling in for the night” (264, αὐλιζομενάων) and “huddle together inside the ship” (225).** Each follows the gloss
   (‘lodge in a yard, spend the night’; ‘pack closely’) and the note says so; ‘the ship’ is the sense of ἐντός. Left, as in
   pass 1 item 7.
7. **“the colon says so” (206) and “the colon announces” (278).** The Greek has the ano teleia, but the sentence refers to
   the colon of the English layers, which is what the reader sees. True as written.
8. **ἀλύξαι ‘epexegetic’ in the known entry vs complementary here.** The infinitive depends on δώῃ; the entry’s label is
   loose but the sense is covered and the rule is “additions only”. Left.
9. **ἀνώγει “the past of ἄνωγα” (226).** Vague but not false (the form is the pluperfect/imperfect of the perfect-with-present
   ἄνωγα, as the glossary entry says); the sense ‘was bidding’ is right in `l`. Left.
10. **“And they” (194, `l`) beside “but they” (`i`), and “hateful words” (278 `i`) for μύθῳ singular.** Pass 1 item 6 for the first; for the second, `l` keeps the
    singular “a hateful word”, and `i` “hateful words” is idiom for one speech (the table row στυγεροὶ ἐπέεσσιν is “hateful words”). Left.

### State after pass 2

`units.json` and `gloss.json` edited in place by script; `t` unchanged; build not run (that is the next step). Severity
counts for the whole file: 0 major, 11 moderate, 25 minor.
