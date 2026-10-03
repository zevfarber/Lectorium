# odyssey-066 (Odyssey 14.1–108) — review

## Pass 1

Method: every grammatical label in every note checked against the form in its line; every statement of position and every cross-reference checked against the line numbers; each note read against its own `l` and `i`; then Greek → `l` word by word, `l` ↔ `i`, remembered English in `i`, quotation marks and `mark`/`p` placement. The shipped parts and the house table in `conventions.md` were searched for the words the notes call "the house rendering" (ἀεικέλιος, ἐνδυκέως, ἐσχατιή, ζατρεφής, κισσύβιον, ὑπέρβιον, ὑπερφίαλος, ἀνάρσιος, λυγρός, ἄλφιτα λευκά, ἄσπετος, ὦ γέρον, Ἴλιον εἰς ἐύπωλον, ἀλλόθροοι, ὄρχαμος ἀνδρῶν, κατέχευε, ῥῶπες, ἠπείρῳ, ὣς εἰπών, ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν) and against `new-renderings.md`; all rows of `new-renderings.md` are carried out in `l`, `i` and notes except the one corrected below (χοίρε’). Speeches: 37–47 (opens at 37, closes at 47), 53–54 (both marks on the one unit), 56–71 (opens 56, closes 71), 80– (opens 80, runs on past 108, correctly unclosed in this part). Neighbouring part odyssey-065 ends with Athena leaving for Lacedaemon, no speech open, so 14.1 opens without a quotation mark. `p` is on exactly the eight units that begin Murray's paragraphs (1, 5, 29, 37, 48, 53, 72, 80); `mark` is on the first unit of each speech (37, 53, 56, 80). `t` was asserted equal to the packet lines unit by unit, before and after the edits (and the 64/63 transposition is in the order Murray prints). `l` has the same number of lines as `t` and `i` has none, in every unit. The one repeated line (14.58 = odyssey-028) agrees with the published `l`; `i` was brought nearer to the published wording (below). Pass 2 (the glosser's `gloss.json`) was not available to this run and is not done here.

Scansion: the packet flags no line. `scan_hexameter.py` was run over all 108 lines anyway: it fits every line and raises one flag on two lines, 14.37 and 14.84, "spondaic fifth" (not a licence the build treats as unresolved). Scanned by hand: 14.37 (…κύνες διεδηλήσαντο) closes with a spondee in the fifth place (–– on δη-λή) and the sixth –×; 14.84 (…αἴσιμα ἔργ’ ἀνθρώπων) has ἔργ’ ἀν (long by position) as a spondaic fifth and θρώ-πων as the sixth. A spondaic fifth foot is an ordinary Homeric variation, not an irregularity of the transmitted text, so no note was added (see "considered and refused").

### Changes made (all by script on `units.json`; `t` untouched)

| Unit (line) | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 17 | n | moderate | "προΐαλλε is the imperfect of προΐημι": the form is the imperfect of προϊάλλω (ἰάλλω 'send, hurl'), not of προΐημι. | "imperfect of προϊάλλω 'send forth'". |
| 17, 105 | n | moderate | The notes refer to "`l`" and "`i`" in backticks; the validator fails any backtick in a note (and a note is not to speak of the layers by their field names). | "the house table gives 'sleek' for the literal line and 'well-fed' for the prose" (17); the same turn at 105. |
| 11 | i | moderate | "after splitting off the dark wood of an oak": "off" asserts that the dark wood is what is removed, which contradicts `l` ("split-around") and the note ("split round"; the sense of the phrase "is not certain"). | "after splitting the dark wood of an oak all round" (follows ἀμφι-; commits to nothing about which part is kept). |
| 24 | n | moderate | "the others are three more of Eumaeus's men … the four dogs were counted in line 22, and these are four herdsmen": οἱ ἄλλοι are four herdsmen in all (three go off, οἱ τρεῖς, the fourth is sent to town at 26), not three; the reference to the dogs is irrelevant and confusing. | οἱ ἄλλοι "the herdsmen besides Eumaeus, four in all"; οἱ τρεῖς says which of them go off with the swine; the fourth is sent in the next unit. Dog sentence and the separate "stands in apposition" sentence removed. |
| 37 | l | minor | "poured disgrace": the table's κατέχευεν is "poured-down" in `l` (θεσπεσίην … χάριν κατέχευεν; κατ’ αἶσχος ἔχευε), and the note itself says "poured down". | "poured-down disgrace". |
| 37 | i | minor | "in an instant" for ἐξαπίνης; the same word is "suddenly" in the shipped parts (odyssey-050, 060) and in this part at 14.29. | "Old man, suddenly the dogs very nearly mauled you, and …". |
| 48 | l, i, n | moderate | ῥῶπας rendered "brushwood". The table fixes ῥῶπες (10.166) as "twigs" and lists "brushwood" among the renderings avoided; the same word recurs here and `new-renderings.md` does not mention a departure. | `l` "thick twigs he spread beneath", `i` "spread thick twigs beneath him"; the note names the word and the table's "twigs". |
| 53 | n | moderate | "ὑπέδεξο is the second person of the aorist ὑπεδέξατο": the 2nd person of ὑπεδέξατο would be ὑπεδέξω; ὑπέδεξο is the 2nd person of the short aorist (the same one as ὑπέδεκτο at 51, which the note on 51 says correctly). The two notes contradicted each other. | "the second person of the short aorist of ὑποδέχομαι, the same aorist as ὑπέδεκτο at line 51". |
| 58 | i | minor | "and any gift from us is small and welcome": the repeated line 14.58 stands in odyssey-028 with `i` "a small gift is welcome"; the packet asks for the published wording as far as the sentence allows, and it allows it here. | "and a small gift from us is welcome". (`l` already agrees with the published `l`.) |
| 61 | n | minor | 137 words (the validator's note band tops out at 130 and warns). | Tightened to 114 words with no claim lost except the aside that κατά "could instead go with νόστον", which was not checked and was dropped. |
| 67 | l | minor | "So much would have benefited me": τῷ is "therefore, in that case" (as the note says), but "So much" reads as a degree word attached to "much" (πόλλ’). | "Then much would have benefited me". `i` left (it carries the force by the conditional). |
| 68 | l, i | minor | "the whole race of Helen": nothing in φῦλον or ἀπό … ὀλέσθαι says "whole"; the word is added. | "the race of Helen" in both. |
| 70 | n | moderate | "εἵνεκα placed after its noun": in Ἀγαμέμνονος εἵνεκα τιμῆς, εἵνεκα stands before τιμῆς (its noun) and after Ἀγαμέμνονος, which depends on τιμῆς. The claim about where a word stands was false. | "εἵνεκα 'for the sake of' taking the genitive τιμῆς, and Ἀγαμέμνονος, which depends on τιμῆς, standing before it". |
| 80 | l | minor | "piglet-meat": the new-renderings row for χοίρεα has `l` "piglet-meats" and `i` "piglet meat". | `l` "piglet-meats". |
| 81 | n | minor | "φρονέοντες 'heeding'": contradicts `l` "minding" and `i` "taking no thought" (and "heed" is a word the new-renderings row keeps away from ὄπις). | "'minding, giving thought to'". |
| 89 | l | minor | "of that man's grievous destruction": the "of" makes ὄλεθρον look genitive; it is the accusative, in apposition to αὐδήν (as the note says); κείνου is the genitive. | "that man's grievous destruction". |
| 98 | n | minor | "σύν with Ionic ξυν-": ξυν- is the older form of σύν, not specifically Ionic. | "σύν in its older form ξυν-". |
| 100 (δώδεκ’) | n | moderate | "the next unit repeats it three times: twelve herds, twelve flocks, twelve droves": the next unit's three items are flocks of sheep, droves of swine and herds of goats; "herds" is this unit's own item and goats were left out. | "repeats the number three times, for flocks of sheep, droves of swine and herds of goats". |
| 100 (τόσα) | n | minor | "πλατέ’ … 'wide, broad', here 'large'": the note gives a sense different from the "wide" in its own `l` and `i`. | "'wide, broad', a herd of wide extent, that is a large one". |
| all 59 notes | n | minor | English glosses were quoted with ASCII ' (the elision mark was already ’); every shipped part uses typographic ‘ ’ for glosses. | Converted to ‘ ’ by script (openers and closers paired per note; possessives made ’). No wording changed. |

## Considered and refused

- 14.5–7, περισκέπτῳ / περίδρομος (unit 5): the note already says both words are uncertain and gives the guess; `i` follows it. Left.
- 14.11–12, the note's "most likely the dark heartwood" for τὸ μέλαν δρυός: hedged ("the exact sense of the phrase is not certain"). Left; only `i` was changed so that it no longer contradicts the hedge.
- 14.7–9 note "(Penelope is meant but not named)": a reading of δέσποινα from the earlier parts, not a claim about later books. Left.
- 14.30 ἕζετο "the aorist of ἕζομαι": handbooks differ on whether ἕζετο is an imperfect or an aorist in Homer; the label cannot be shown false from the line. Left. (The same applies to the aorist label for εἷσεν, which is sound.)
- 14.30 κερδοσύνῃ "marks the sitting down, not the dropping of the staff": the comma after ἕζετο and the natural reading support it; the note does not rest on word order. Left.
- 14.33 μετασπών "a participle of a rare verb": deliberately non-committal; correct as far as it goes. Left.
- 14.32 ᾧ "the possessive 'his own', and its owner is Odysseus": ᾧ refers back to the subject of πάθεν; the note's reading is the plain one. Left.
- 14.44 ὄπις "the watching eye of the gods that punishes": offered as the usual understanding of a word the note says is uncertain, and the same note flags the uncertainty. Left.
- 14.57 "all strangers and beggars are from Zeus" (`i` of the published odyssey-028): the English is shipped and the validator requires it for a whole repeated unit. Not changed here. Noted for the owner only as a close match to ordinary English renderings of the line; the grammar gives no other order.
- 14.83–84 `i` "honour justice and the proper deeds of men": reads as a literal rendering of τίουσι δίκην καὶ αἴσιμα ἔργα; "proper" comes from αἴσιμα 'in due measure' (the note says so), and "cruel" is the house word for σχέτλια. Rebuilt from the cases, nothing recalled. Left.
- 14.32/36/55 etc. ἄναξ "lord" for the (unrecognised) Odysseus in narrator's voice: house "lord" for ἄναξ; the note on 36 already explains it. Left.
- 14.42 `i` "wanting food" for ἐελδόμενος … ἐδωδῆς, while `l` has "longing": `i` is allowed to be plainer; sense agrees. Left.
- 14.56–59 `l` "the way of servants is this, always afraid": "is this" has no Greek counterpart but marks that δειδιότων agrees with δμώων; reads as the Greek order allows. Left.
- 14.57–58 note "εἰσιν ἅπαντες … has the two nominatives … as its subject": loose (ἅπαντες agrees with them) but not false. Left.
- 14.10 ῥυτοῖσιν λάεσσι "hauled stones": new-renderings row; ῥυτός 'dragged'. Left.
- 14.37 and 14.84 spondaic fifth foot (scanner flag, not a packet flag): not an irregularity of the text; no metrical sentence added to the notes.
- Title, `titleEn`, `part`: carry the cite `14.1–108` exactly; `about` read against the units and found accurate.
- British spelling (harbour, honour, colour) kept: it is the shipped majority (57 : 8 for harbour/harbor over parts 001–065).

## Counts

Major 0 · moderate 8 · minor 12 (the typography conversion counted as one minor).

## Pass 2

Method: `units.json` re-read afresh, unit by unit (labels against the form and line, positions, cross-references, `ln`/`mark`/`p`, `l` ↔ `i`, quotation marks, no backticks, ’ only in glosses), `t`, `l` and `i` compared before and after (unchanged); then every entry of `gloss.json` parsed against its lines, the 162 novel entries and the `__broaden__` block; then the known forms of the part read against their existing entries for uses the entry does not cover.

### Changes made (by script; `t`, `l`, `i` untouched)

| Where | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| unit 0 (14.1) | n | minor | "The ὁ that opens the line": ὁ is the second word, after αὐτάρ. | "The ὁ after αὐτάρ". |
| unit 15 (14.31) | n | minor | ἕζετο called "the aorist"; the shipped glossary entry for ἕζετο says imperfect, so note and glossary contradicted each other (pass 1 refused only because the label cannot be proved false). | Label dropped: "ἕζετο ‘sat down’ is a past tense of ἕζομαι". |
| unit 42 (14.78) | n | minor | κίρνη "(Attic ἐκίρνα)" against the glossary's "= ἐκίρνη"; the Attic form of the imperfect was asserted without ground. | "the imperfect of κίρνημι ‘mix’, without augment". |
| unit 43 (14.80) | n | minor | ὦ called a "particle"; it is an interjection (the glossary says so). | "the interjection ὦ". |
| gloss δασύ | parse | moderate | "neut. nom. sg.": in μέγα καὶ δασύ the adjective agrees with ἐνεύναιον, itself accusative in apposition to δέρμα. | "neut. acc. sg. (nom. and acc. alike), agreeing with ἐνεύναιον". |
| gloss ἔπειρεν | parse | moderate | "unaugmented (= ἔπειρε)": the initial ἐ- of ἔπειρεν is the augment; the gloss contradicted itself. | "impf. 3 sg. (augmented ἔ-πειρε), ν-movable". |
| gloss τάσδε | text | minor | "this here" contains "here" (forbidden word). | "this, this one". |
| gloss ῥῶπας | meaning | minor | "brushwood, bush" put first; the table's rendering is "twigs" and the shipped entry for ῥῶπάς reads "twig, bush, brushwood". | "twig, bush, brushwood", as the shipped entry. |
| gloss μετασπὼν | lemma | minor | Lemma "μετασπάω" is a form the glosser could not vouch for. | Hedged: "μεθέπομαι (lemma uncertain) … from the aorist stem σπ- of ἕπομαι" (cf. ἐπισπών, ἐφέσπετο); meaning kept. |
| __broaden__ ὅττι | new reading | minor | "conj. ‘that’" while the note on unit 26 says ‘because’ (after χαῖρε either fits). | "‘that, because’". |
| __broaden__ ὑπέδεκτο (new) | known entry | moderate | Existing entry "undertake, promise, agree to" does not cover ‘receive as a host’. | Old entry whole + " · also ‘receive as a host, welcome’ …". |
| __broaden__ τέταρτον (new) | known entry | moderate | Existing entry is neuter only; the use is masc. acc. with the article (τὸν τέταρτον). | Broadened. |
| __broaden__ πέφραδε (new) | known entry | moderate | Existing entry has only "aor. imper. 2 sg."; the use is the indicative 3 sg. | Broadened. |
| __broaden__ ὑπέρβιον (new) | known entry | minor | Adjective only; both uses are adverbial. | Broadened. |
| __broaden__ ἔργον (new) | known entry | minor | Nominative use listed only for an impersonal verb; ἔργον ἀέξεται is an ordinary passive. | Broadened. |
| __broaden__ τι (new) | known entry | minor | No reading for a plain ‘something’ in a statement (καί τι ἴσασι). | Broadened. |
| __broaden__ ἔνθα (new) | known entry | minor | Doubled ἔνθα καὶ ἔνθα not covered. | Broadened (without the forbidden word). |

All 23 earlier `__broaden__` entries re-checked: each is the old entry whole + " · " + a new reading, ’ only, and covers the use (αὐτοῦ, αὐτῆς, αὐτοῖς, αὐτός, αἴσιμα, δοίη, δώῃ, ἀέξῃ, οἴω, ἐστόρεσεν, ἔλυσε, ὅτ, ᾗ, ἡ, τὸν, τὸ, τις, τοσσοῦτον, φυλάσσω, ἄριστον, κέ, κέν). Every new entry is under 230 characters, has no digits-as-line-numbers, no "here", no ASCII apostrophe.

### Considered and refused

- Flagged doubt θέρμ’: θερμός, neut. acc. pl., elided, agreeing with the roast meat is sound (θέρμος/θέρμα is the Homeric accentuation); left.
- χοίρε’: χοίρεος neut. pl. as a noun ‘piglet meat’ agrees with the unit (χοίρεα, the table row); left.
- εὗσέ ‘unaugmented’: εὕω has stem εὑ-, so εὗσε is the unaugmented aorist and Attic ηὗσε the augmented one; left.
- συβῶτα: vocative in -α, apposed to Εὔμαιε; correct.
- πρόχνυ ‘of uncertain origin (perhaps down on the knees)’: hedged both in the glossary and in the note; left.
- ἰονθάδος ‘sense not certain’ and ὑλακόμωροι ‘-μωρος unknown’: honest statements of what is unknown; parses fit (fem. gen. sg. with αἰγός; masc. nom. pl. with κύνες).
- μετασπὼν: kept the hedge ("lemma uncertain") rather than assert the lemma; the unit note stays non-committal.
- ἔλασσε (known entry "unaugmented"): shipped entry, not part of this part's work; not touched.
- ἔνεικε, ἴδον, ἔβαν etc.: known entries cover the uses.
- δῖος "epithet of heroes" (known entry) applied to the swineherd: the note on unit 0 already says so; left.
- Spondaic fifth feet at 14.37 and 14.84: unchanged from pass 1.

### Counts (pass 2)

Major 0 · moderate 5 · minor 12. Pass 1 + pass 2 together: major 0 · moderate 13 · minor 24.
