# odyssey-030 (7.1–132) — reviewer, pass 1

Scope of pass 1: notes' labels, positions and cross-references; Greek to `l`; `l` to `i`; remembered
English; quotation marks and `mark`; hand scan of 7.119; the drafter's listed doubts; notes over 115
words. `t` was not touched (checked by comparison with the pre-review file, and the header fields are
unchanged). Glossary parse checks are left to pass 2, when `gloss.json` exists. All edits were made by
one script on `units.json` in place. Checked after the edits: every unit whose Greek repeats a published
unit (7.27, 7.37, 7.38) now carries exactly the published `l` and `i`; `l` has as many line breaks as `t`;
no `\n` in `i`; no backticks; no note over 115 words; quotation marks balanced (see below).

Counts: 1 high, 6 medium, 23 low = 30 changes. Unit indices are 0-based positions in `sentences`.

## Changes

| Line (unit) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 38 (#21) | l, i, n | HIGH | The whole unit ὁ δ’ ἔπειτα μετ’ ἴχνια βαῖνε θεοῖο. already stands at 2.406, 3.30 and 5.193 (odyssey-008, -009, -024) with l "And he then walked following in the footsteps of the god." and i "and he followed close behind in the footsteps of the god." The draft had "after the footsteps … of the goddess" and "in the goddess’s footsteps", which the validator (check 6) would fail and which breaks the repeated-line rule. The packet did not list this line among the repeats. The note also said nothing of the repetition. | `l` and `i` set to the published wording. Note rewritten: says the line stands at 2.406, 3.30, 5.193 (checked against the source: the three lines are identical), keeps the English, and explains that θεός serves for a goddess, so "the god" is Athena. |
| 13 (#6) | n | MEDIUM | Cross-reference wrong: "πῦρ … ἀνέκαιε answers δαῖε … πῦρ three lines earlier". δαῖε is in line 7, ἀνέκαιε in line 13: six lines. | "three" changed to "six". |
| 7 (#3) | i | MEDIUM | ἀμφιέλισσαι rendered "curved ships"; the house rendering is "curved on both sides", and the note itself says so. An epithet was compressed in `i`. | "whom ships curved on both sides once brought from Apeire". |
| 84 (#45) | n | MEDIUM | "The first line is the line used of Menelaus’ house at 4.45; only its second half names another owner." Both lines repeat 4.45–46; only the last two words of the second line (the owner) differ. As written it said the first line repeated and the second half of that same line differed. | "Both lines are those used of Menelaus’ house at 4.45–46; only the owner’s name at the end of the second line differs." (4.45 and 4.46 checked in the source.) |
| 69 (#38) | n | MEDIUM | "τετίμηταί τε καὶ ἔστιν … with the participle carried over": there is no participle in the line; τετίμηται is a finite perfect and ἔστιν stands with 'honoured' understood. | "'honoured' being understood again with ἔστιν." |
| 86 (#46) | n | MEDIUM | ἐληλέδατ’ labelled a perfect passive "in the ending -δατ(αι)". The form is the elided pluperfect ἐληλέδατο (3 pl.), used as an imperfect in this description. | "a pluperfect passive … in the ending -δατ(ο), used like an imperfect". |
| 95 (#50) | n | MEDIUM | Same label for ἐρηρέδατ’ (pluperfect ἐρηρέδατο), "-δατ(αι)". | "a pluperfect passive … -δατ(ο)". |
| 1 (#0) | n | low | φέρεν "with no augment and the ending -εν": -εν is the ordinary movable ν, not a Homeric ending. | "the imperfect ἔφερε without its augment, with movable ν". |
| 3 (#1) | n | low | Over 115 words (123); "ἡ … not the article" wordy; "imperfect middle" redundant. | Trimmed (ἡ, οὗ, ἵσταντ’, ἔσφερον clauses); 113 words. |
| 7 (#3) | n | low | νέες called "the uncontracted plural of νηῦς"; it is the epic plural beside Attic νῆες. | "the epic plural of νηῦς (Attic νῆες)". |
| 7 (#3) | n | low | 116 words after the νέες fix above (114 before). | Dropped the θάλαμος/πόλος etymology in brackets; 109 words. |
| 10 (#4) | n | low | "the accented ὥς following the word it governs": ὥς governs nothing; θεοῦ is governed by ἄκουεν. | "…following the word it goes with". |
| 14 (#8) | n | low | 116 words. | Trimmed two clauses (μεγαθύμων genitive plural; χεῦε wording); 109 words. |
| 18 (#9) | i | low | "made like a young maiden": ἐικυῖα is 'like', not 'made like'; the shipped parallel at 7.78 is "in the likeness of". | "in the likeness of a young maiden carrying a jar". |
| 34 (#18) | n | low | "νηυσὶ θοῇσιν and ὠκείῃσι are two datives in -ῃσι(ν)": νηυσί is not in -ῃσι. | "θοῇσιν and ὠκείῃσι are two adjectives in the dative -ῃσι(ν), both agreeing with νηυσί …". |
| 36 (#19) | n | low | Same νέες label. | "the epic plural of νηῦς". |
| 48 (#26) | mark | low | "Athena speaks" for her third speech (after 7.27 "Athena answers"); the pilot uses "Athena speaks again" (1.81). | "Athena speaks again". |
| 54 (#31) | n | low | τοκῆες resolved flatly as "loose … 'forebears'". The two statements (same parents as Alcinous; daughter of his brother, 63–66) do conflict, but the resolution is an inference. | "must be loose here, 'forebears', if the two statements are to agree." Lines 63–66 checked (Rhexenor's daughter, Alcinous' niece). |
| 69 (#38) | n | low | 127 words after the fix above. | Dropped "its formation old and unusual", "θεὸν ὥς is 'as a god'", and shortened the ἐκ clause; 111 words. |
| 73 (#39) | n | low | "καὶ αὐτή … as well as Alcinous, with whom she shares her people’s honour": an unhedged guess about what the 'too' adds to. | "'she herself too', in her own right besides the honour just described." |
| 82 (#44) | n | low | Note calls πολλά adverbial 'much'; `i` says "many thoughts". Not a contradiction of sense but the note should say so. | Note now says it is a neuter plural used adverbially, and that 'many thoughts' spells out the same sense. |
| 91 (#49) | n | low | πραπίδες "originally the midriff" stated as fact. | "often taken as originally the midriff". |
| 99 (#52) | n | low | ἐπηετανόν "a neuter used as a noun". The drafter's own new-renderings row calls 7.99 adverbial; the Greek allows both. | Note: "the neuter of 'never-failing', here the object of ἔχεσκον, 'a never-failing supply' (taken as an adverb it would be 'unfailingly')". `l`/`i` unchanged (see refused). |
| 103 (#54) | n | low | 118 words. | Dropped "the point of comparison is not said"; 111 words (118 before). |
| 118 (#62) | n | low | Ζεφυρίη: "a noun such as 'breath' is understood": a guess. | Removed the parenthesis. |
| 118 (#62), line 119 | n | low (flag) | Packet flag on 7.119, see hand scan below. | Added one sentence: "The line is metrically irregular as transmitted: the first syllable of Ζεφυρίη, short by nature, must be counted long, and the ending of φύει is shortened before ἄλλα." |
| 122 (#64) | n | low | ἀλωή is "vineyard" here, "orchard" at 6.293 (shipped). The note did not tell a reader who remembers 6.293. | Added "(at 6.293 the same word is 'orchard')" after the vineyard clause. |
| 122 (#64) | n | low | "τῆς is the relative 'of which'"; `i` has "one part of it", and the pronoun could be either. | "τῆς is a pronoun, 'of it' or 'of which'". |
| 125 (#65) | i | low | "in front of these": πάροιθε has no genitive in the Greek; "of these" supplies a referent the line does not give. | "and in front are unripe grapes …". |
| 127 (#66) | n | low | πεφύασιν "in the Ionic ending -ασιν": it is the older perfect without the κ of Attic πεφύκασι, not simply an Ionic ending. | "the perfect of φύω without the κ of Attic πεφύκασι". |

## Hand scan of 7.119 (flagged UNRESOLVED)

Ζεφυρίη πνείουσα τὰ μὲν φύει, ἄλλα δὲ πέσσει. Sixteen syllables: Ζε|φυ|ρί = foot 1 (– ⏑ ⏑) only if Ζε, short by
nature, is taken long in the longum; η πνεῖ = spondee; ου|σα|τὰ = dactyl; μὲν|φύ|ει = dactyl only if the diphthong of
φύει is shortened before ἄλλα (correption); ἄλ|λα|δὲ = dactyl; πέσ|σει = foot 6. So the line fits the hexameter but
only with two licences, the lengthened opening syllable and the shortened φύει. Both are as the scanner reported. The
irregularity is real (as transmitted), so the sentence was added to the note of the unit that contains the line (#62).

## Drafter's doubts, decided

- **ἀλωή "vineyard" against 6.293 "orchard"**: kept. In 7.112 ὄρχατος is already "orchard", and the grapes, drying and
  treading of 122–126 make ἀλωή a vineyard; "orchard" twice in a row would blur two different plots. 6.293 stays as shipped;
  the note now points to it (see change above).
- **ἐπηετανόν 7.99 / 7.128**: l/i "never-failing" kept in both (house row). Note hedged (noun or adverb). Open item for
  the copy step: `new-renderings.md` calls 7.99 "adverbial"; the row should read "7.99 as a noun or adverb, 7.128 adverbial".
- **ἐραννός / ἐρατεινός**: consistent with the table: "delightful city" (7.18, `l` and `i`), "lovely Scheria" (7.79). No other word
  in the part uses either English word. Accepted.
- **7.74 ᾗσι**: relative, feminine dative plural (Attic αἷς), object of ἐὺ φρονέῃσι in a general clause; the possessive would need
  a noun. Note and `l`/`i` ("the women she thinks well of") accepted.
- **Subject of ναίει 7.29**: accepted as the man of the house (Alcinous), unexpressed; the note says so. The only other candidate,
  δόμος, is already the accusative object of δείξω.
- **τοκῆες 7.54**: hedged (change above); `i` keeps the literal "same parents".
- **Notes over 115 words**: the four the drafter listed (#1 123, #8 116, #38 131 after its fix, #54 118) trimmed to 111 to 113 words; #3 (pushed to 116 by its own label fix) trimmed to 109.

## Findings considered and refused

- **Unit #6 ἥ "again the relative"** against `l` "she it was who": ἥ before the enclitic οἱ keeps its acute whether
  relative or demonstrative; a relative continuing the sentence gives exactly "she it was who". Left.
- **Unit #15 "dative of interest" for μοι**: μοι is a dative going with πατρός; the label is not false. Left.
- **Unit #15 `i` "the house you ask for"** against `l` "which you bid me": same content; the note glosses κελεύεις "bid, ask".
  Line 48 keeps "bid me point out" because the Greek adds πεφραδέμεν. Left.
- **Unit #15 "he lives" with no antecedent in `i`**: adding "Alcinous" would put in a name the Greek omits; the note explains. Left.
- **Unit #36 `i` "struck down while he was still a bridegroom"**: "down" and "still" render βάλε … νυμφίον in context (the note says
  "newly married"); no sense is lost. Left.
- **Unit #43 "puts it first for emphasis"**: Ἀλκινόου does open line 82 (checked); the emphasis is a mild inference. Left.
- **Unit #63 γηράσκει "that is ripens and ages"**: keeps the house "grows old" in `l`/`i`; the note only explains. Left.
- **Unit #16 τοῖον, `i` "go on in silence"**: the note already says the adverb's force is uncertain. Left.
- **Unit #4 `i` "They had picked her out"**: pluperfect for a backstory aorist is idiomatic. Left.
- **Unit #1 `i` "brought the team to a halt"**: στῆσεν has no expressed object; the note says so. Left.
- **Repeated 7.111 = 2.117** (not in the packet because of a grave/acute difference in the archive): `l`/`i` match odyssey-006's
  rendering ("to know very-beautiful works, and a noble mind" / "skill in very beautiful handiwork … a noble mind"). Fine.
- **Remembered English in `i`**: read all 69; every phrase is built from the case relations or from shipped house wording
  ("a wonder to see", "thinks kindly", "wanton", "earth-shaker"). Nothing looks pre-formed. No changes.
- **Quotation marks**: “ on #11 (7.22), #15 (7.28), #26 (7.48), in both layers; ” on #13 (7.26), #19 (7.36), #41 (7.77), in both
  layers; no stray marks; `mark` on the first unit of each of the three speeches (Odysseus asks / Athena answers / Athena speaks
  again). 7.27 (#14) and 7.37 (#20) are narrative and carry none. The neighbouring part odyssey-029 ends on a narrative unit
  (ln 330), so #0 correctly opens with no quotation mark. Paragraph marks `p` are on the units for lines 1, 14, 22, 27, 37, 48, 78,
  matching the packet. Nothing to change.

## Left for pass 2

Parse checks of `gloss.json` against the lines (not yet present).

---

# Pass 2

Scope: every parse in `gloss.json` (226 novel forms) checked against the line where the form stands in
`units.json`; the 24 `__broaden__` entries checked against their uses in this part; a second adversarial read of
`units.json`; the `new-renderings.md` ἐπηετανός row. After the edits, `gloss.json` was checked against the build
gate's own rules (old entry whole inside each broadened one; novel entries under 231 characters, no ASCII
apostrophe or backtick, shape `lemma — meaning`; every form of the part covered, none extra).
Counts: 0 high, 4 medium, 10 low = 14 changes to `gloss.json`, plus 1 low edit to `new-renderings.md` (0/4/11 in all). `units.json`: no change.

## Changes

| Form | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| ἐρηρέδατ’ | gloss | MEDIUM | Lemma ἀραρίσκω. The form is the pluperfect of ἐρείδω (the reduplication ἐρηρ- is that of ἐρείδω; ἀραρίσκω gives ἀρηρ-), as the note of the unit now says. | "ἐρείδω — prop, fix firmly; plpf. 3 pl. …". |
| Εὐρυμέδουσα | gloss | MEDIUM | "Arete’s old nurse": she is Nausicaa’s nurse (the line says she reared Nausicaa; Arete's nurse is nowhere said). | "Nausicaa’s old nurse". |
| καιρουσσέων | gloss | MEDIUM | Lemma "καιρούσσιος" is not a dictionary word; the form is the contracted feminine genitive plural of καιρόεις (-όεσσα). | "καιρόεις — close-woven (of cloth); fem. gen. pl., contracted from -οεσσέων, epic -έων …; exact sense disputed". |
| ἐπώνυμον | gloss | MEDIUM | "named to fit, having a fitting name" asserts what the note and the house table refuse to assert (that the name fits). | "named, bearing a name (whether it fits or means anything is uncertain)". |
| ἐραννήν | gloss | low | "lovely, charming": "lovely" is the house word for ἐρατεινός; ἐραννός is "delightful". | "delightful, charming". |
| ἐυδμήτων | gloss | low | "well-built" is reserved for ἐυκτίμενος; house rendering is "well-constructed". | "well-constructed". |
| ταλαπείριος | gloss | low | "wretched" is on the house list of words avoided for this word. | "much-tried, enduring trials". |
| ἀφιεῖσαι | gloss | low | "putting forth" the blossom reverses the sense used in the unit ("shedding"). | "’letting go, shedding’". |
| προτιόσσεο | gloss | low | Only "address, accost"; the unit renders "look at" and its note says some take "address". | "look toward, look at (some take ’address’)". |
| ἀπόλλυται | gloss | low | Gloss "is lost" against the unit's "perishes". | "’perishes’". |
| τετίμηταί | gloss | low | "is honoured" for a perfect; the unit has "has been honoured". | "’has been honoured’". |
| μίν (broadened) | gloss | low | New reading covered only "object of a participle"; in this part μιν is also the object of the finite ἔτισ’ (and stands with ἀμφίς). | Reading now "object of a verb or participle", with both examples. |
| τῆς (broadened) | gloss | low | "relative" while the unit's note (after pass 1) calls it a pronoun that may be read "of it" or "of which". | "with the force of a relative". |
| αὐτῶν (broadened) | gloss | low | The quoted example "τῶν αὐτῶν τοκήων" is not the order of the line (τοκήων τῶν αὐτῶν). | Example given in the line's order. |
| ἐπηετανός row, `new-renderings.md` | table | low | Row said "7.99 … adverbial"; the unit and its note take 7.99 as a noun or adverb. | Row now says 7.99 as a noun ("a never-failing supply") or an adverb, 7.128 adverbial. |

## Checked and accepted (no change)

- Every other novel parse (case, number, tense, mood, voice, the Attic equivalents named) agrees with the line: for example
  δῦνε (imperfect), δαῖε, βεβλήατο and ἐληλέδατ’ (pluperfects), ἐλήλαται (perfect), δειδέχαται, τεχνῆσσαι (= τεχνήεσσαι),
  σφέας, στείχῃσ’ and φρονέῃσι (-ῃσι subjunctives), συκέαι, ὑπερθύμοισι, ἀργύρεοι, ἑτέρας (fem. acc. pl.), ὑψηλά (neut. acc. pl.).
  The digits in the entries are person numbers ("3 sg."), not line numbers.
- `ἄκουεν` "hear, listen to, obey": the unit has "listened to him"; "obey" is a listed sense, not a wrong parse. `ἡγήσαιο` "could you guide"
  is the polite-request reading used in the unit. `ὄντας` "(= Attic ὄντας)" is redundant but true.
- All 24 broadened entries contain the old entry whole and their new readings are each used in this part: αὐτοῦ (πρόσθ’ αὐτοῦ, Ἀλκινόοιο
  αὐτοῦ), αὐτῶν (ἡρώων, τῶν αὐτῶν), γυναικῶν (partitive, possessive), δεύεται (lacks + gen.), λαῶν (after ἐκ), λύει (νείκεα), οὗ (possessive),
  περὶ (adverb of place; + acc.; + gen. beyond; + dat. περὶ κῆρι), τῷ (adverbial), Ἀθήνην (the city), ἀθανάτους (adjectival), ἀργύρεον, ἄλλη,
  ἐνὶ (adverb), ἐρέεινε (imperative), ἔλθοι (protasis), ἕτερον, ἱστούς (loom), ὅτε (+ subj.), ὡς (as, ὡς εἰ), ὦρτο (set out), ᾗσι (relative).
  The word "here" in αὐτοῦ belongs to the old entry (which must stay whole).
- The broadened entries are longer than 230 characters; the build's 230 limit applies to novel entries only (build_odyssey.py line 62).

## Second read of `units.json`

Re-read all 69 units against the Greek, the notes' labels and cross-references, and the house table after the pass-1 edits. Nothing new
found that needed changing. Considered and refused: the pass-1 refusals stand; `i` "the west wind, always blowing" (7.118) keeps
μάλ’ αἰεί as "always"; the note for #64 now says both 6.293 and 7.122 in one place, which is accurate.
