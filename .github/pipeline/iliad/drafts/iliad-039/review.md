# iliad-039 (6.332–439) — review, pass 1 (units only)

Checks run: notes' grammatical labels and position claims against the lines; Greek to `l` word by word; `l` against `i`; remembered English; quotation marks, `mark`, `p`; unit cuts against the source; house table and published parts for repeated Greek. `t` was never touched (verified: every `t` identical before and after; the units still reproduce lines 332–439 word for word, 786 words). `gloss.json` not touched.

Mechanical results: `t` reproduces the source; `ln` right for all 62 units; `l` line count equals `t` line count in every unit; `p` right on all six paragraph starts (332, 342, 359, 369, 381, 390); quotation marks balanced and placed right (open on 333, 344, 360, 376, 382, 407; close on 341, 358, 368, 380, 389, 439); `mark` on the first unit of each of the six speeches; no ASCII apostrophe, no backtick, no newline in `i`; note lengths within the band; no scansion flags in the packet, so nothing to scan by hand.

Speech end at 439: the source's 440 is `τὴν δ’ αὖτε προσέειπε μέγας κορυθαίολος Ἕκτωρ·` (¶), a fresh reply-formula by Hector to her. So Andromache's speech ends at 439 and the closing ” on the last unit is right. The next part (iliad-040, 6.440–529) begins with Hector's answer; nothing runs on.

## Changes made

| Line · field | Severity | What was wrong | What was done |
|---|---|---|---|
| `about` | medium | Said Achilles "has taken her father, her seven brothers and her mother". Achilles killed father and brothers; the mother he ransomed, and she then died by Artemis (6.425–428). | Reworded: "Achilles killed her father and her seven brothers and ransomed her mother, who then died". |
| 338 · n | low | Note said ὧδε "goes with the infinitive", but `l` puts "thus" beside "seems" and only `i` takes it with "better": the note contradicted its own `l`. | Note now says ὧδε stands between the two verbs and could go with either, and says how each layer takes it. |
| 344 · i | medium | δᾶερ rendered "Brother of my husband", against the house rendering (δαήρ "husband's brother", 3.180, "my husband’s brother") and against this part's own `i` at 354. Same Greek, two English. | `i` now begins "My husband’s brother, and so kin to a dog like me, …". |
| 344 · n | low | Said κακομηχάνου and ὀκρυοέσσης "agree with ἐμεῖο"; as adjectives they agree with κυνός (feminine in sense), which stands in apposition to ἐμεῖο. | "also go with κυνός, and so with ἐμεῖο". |
| 381 · l, i, n | medium | ὀτρηρή rendered "nimble". The Odyssey table fixes ὀτρηρός "brisk" (4.23, 4.38) and iliad-004 shipped "brisk attendants". A second English for an epithet already fixed. | "nimble" to "brisk" in `l`, `i` and the note. See the follow-ups below. |
| 398 · n | low | Note presented ἔχεθ’ Ἕκτορι "was held by Hector, that is, was his wife" as plain fact; the construction is unusual. | Added one sentence: the middle of ἔχω normally means "hold on to" with the genitive, and "was his wife" is the sense the context gives. `l` and `i` unchanged. |
| 399 · n | low | "A handmaid carries the baby behind her": "behind" is not in the Greek (ἅμα … κίεν αὐτῇ, "went along with her"). | "with her". |
| 402 · n | low | Glossed τόν ῥ’ as "him indeed", but it is the relative ("whom", as `l` and `i` have it). | "whom indeed (the article used as a relative)". |
| 414 · l | medium | "For indeed my father killed heavenly Achilles": in English this reads as the father killing Achilles. The Greek has object first (πατέρ’ ἁμὸν ἀπέκτανε δῖος Ἀχιλλεύς). | `l` now "For indeed my father heavenly Achilles killed," (object first, as in the Odyssey's "Him then … addressed Alexander" order). Note gains a clause naming object and subject. |
| 414 · n | low | (same unit) | Clause added, as above. |
| 423 · l | medium | Same fault: "for all of them killed swift-footed, heavenly Achilles" reads as the brothers killing Achilles. Also "their" cattle: no possessive in the Greek. | `l` now "for all of them swift-footed, heavenly Achilles killed / at the rolling-gaited cattle and white sheep." Note names πάντας as the object. `i` left as it was ("their" there is the reader's supply and `i` is free to make it). |
| 423 · n | low | (same unit) | Clause added, as above. |

No change to `t`, `ln`, `v`, `p`, `mark` anywhere.

## Follow-ups for others (not done by me)

- `new-renderings.md`, row for 6.381: still says "nimble" and lists "busy", "quick" as avoided; it should say ὀτρηρή "brisk" (following 4.23 and iliad-004) and put "nimble" among the avoided. I did not edit that file.
- Glosser: ὀτρηρὴ is in `novel-forms.json`; the existing glossary key is the dual `ὀτρηρὼ` ("brisk, active, ready"), so the new entry should read "brisk" too.
- Unit at 359 (`τὴν δ’ ἠμείβετ’ ἔπειτα μέγας κορυθαίολος Ἕκτωρ`): the pinned source has no closing mark at the line end, while the published iliad-038 unit with the same Greek has `·`. The units' `t` follows the source exactly (correct for pass 1). If the build or validator insists on a terminal mark, runbook rule "Missing punctuation in the source" applies; the English is identical to the published one either way.
- The same trait applies to nothing else in this part: every other unit ends on a mark the source prints, or at a comma cut that the four-line rule allows (333/334, 354/355, 392/394, 382–385, 401/402 are the comma cuts, each in a sentence longer than four lines).

## Findings considered and refused

| Line | Finding | Why refused |
|---|---|---|
| 335 · νεμέσσι (flagged) | Is this the dative of νέμεσις? | Yes, it is read as the epic dative of νέμεσις (for νεμέσει), parallel to the dative χόλῳ; "resentment" follows the house table (νέμεσις 2.296). The note says "the dative of νέμεσις spelled with doubled σ", which is true as far as it goes and claims nothing about metre or origin. Τρώων taken with both datives is the natural reading and `l`, `i` and note agree. No change. |
| 339 · ἐπαμείβεται ἄνδρας (flagged) | "goes in turn over men" is odd English; is the accusative sound? | The middle ἐπαμείβομαι "go by turns, pass from one to another" with an accusative of those it visits is the attested construction; `i` "passes from one man to another" carries the sense, and the note says so. `l` is stiff but literal and unambiguous. Kept. |
| 344 · δᾶερ ἐμεῖο κυνός (flagged) | Does `i` wrongly turn the genitive into an inference ("and so kin to")? | The genitive ἐμεῖο depends on δᾶερ and κυνός is in apposition to ἐμεῖο, so "kin to a dog like me" is a fair reading of "husband's brother of me, a dog". Only the first words were out of line with the table (fixed above). κυνός "dog" agrees with 356 and with the note's "shameless creature". Kept apart from that fix. |
| 344 · ὀκρυοέσσης | "a chilling thing" invents a noun. | `i` may supply a noun for an adjective standing alone in apposition; the note says the gloss is the traditional one. Kept. |
| 350 · ὤφελλον … εἶναι | `l` "were" but `i` "had been". | The speaker is already Paris's wife; "if only I had been" is the unfulfilled-wish sense, and `l` keeps the Greek present infinitive. Both fine. |
| 343 · προσηύδα | `l` "addressed", while the table at 9.363/12.36 keeps "spoke" and reserves "addressed" for προσέειπε/προσέφη. | The table itself uses "addressed" for προσηύδα at 4.680, 14.79 and 4.192 (Iliad), and `i` has "spoke to"; the usage is mixed in the table, so no single rendering is violated. Left. |
| 369 · note | φωνήσας glossed "having lifted his voice" while `l` says "having spoken". | Standard note gloss of the word's root (as at 1.201 in the table); `l` is the published English of the line. Left. |
| 398 · ἔχεθ’ Ἕκτορι (flagged) | Is "was held by Hector" / "had as his wife" right? | The sense (she was Hector's wife) is certain from context; the grammar is the unusual part. `l` is the literal, `i` the sense, and the note now says the construction is unusual. No change to `l` or `i`. |
| 389 · μαινομένῃ ἐϊκυῖα | `i` "a woman out of her mind" may be remembered English. | Not distinctive of any translation; `l` keeps "raging" (house μαίνομαι), and the row in `new-renderings.md` explains the choice. Rebuilt from the grammar. |
| 370–373 · `i` | `i` drops ἀλλά ("but") before "she, with her child". | The semicolon carries the contrast; no loss of force. |
| 380, 385 · δεινὴν θεόν | "dread goddess" may be remembered. | It is the plain rendering of δεινός (table "dread"), not a phrase peculiar to one version. |
| 394 · πολύδωρος, etc. | None found wrong. | Follows the Odyssey table with the note. |

## Severity count

- high: 0
- medium: 5 (about text; δᾶερ in `i` at 344; ὀτρηρή at 381; `l` ambiguity at 414; `l` ambiguity at 423)
- low: 7 (notes: 338, 344, 398, 399, 402, and the companion note clauses at 414 and 423)
- refused: 12

# iliad-039 — review, pass 2 (glossary)

Scope: every parse in `gloss.json` (168 new forms) checked against each line where the form occurs; all 21 `__broaden__` entries checked (old entry whole, then " · " plus one new reading, and the reading actually occurs in 6.332–439); every known form that occurs in the part checked for coverage of its use here. Mechanical: all novel forms present and no extras; every `known-forms.json` and `gloss.json` key covers every word of the part; no ASCII apostrophe, no line number, no "here" in any entry; every new entry under 230 characters. `units.json` and `t` not touched (no gloss finding forced a note change). Pre-pass-2 `gloss.json` was backed up in the scratchpad.

## Changes made (pass 2)

| Form · file | Severity | What was wrong | What was done |
|---|---|---|---|
| ὀτρηρὴ · gloss | medium | Entry said "nimble, quick, busy", but the part renders ὀτρηρή as "brisk" (`l`, `i`, note) and the table avoids nimble/quick/busy. | Now "brisk (traditional sense; exact meaning uncertain)". |
| 6.381 row · new-renderings.md | medium | Row gave "nimble" in both English columns. | Both now "brisk"; "nimble" added to the avoided column. |
| μαλακοῖς · gloss | medium | "masc. dat. pl." but it agrees with the neuter ἐπέεσσιν (ἔπος). | "masc./neut. dat. pl. (neut. with ἐπέεσσιν)". |
| θαλερὸς · gloss | low | Called "predicate adj."; it is attributive to the predicate noun παρακοίτης; quoted gloss "in his prime" did not match the part's "flourishing". | "agreeing with παρακοίτης: ’flourishing’". |
| ἄτης · gloss | low | "Ionic η (= Attic ἄτης)" names an Attic equivalent identical to the form, so it says nothing and misleads. | Dropped; "fem. gen. sg., after ἕνεκα". |
| λώϊον · gloss | low | "nom. sg." is not decidable: the infinitive ἔσσεσθαι has no expressed subject, so the predicate could be nom. or acc. | "neut. nom./acc. sg., predicate". |
| κράτος · `__broaden__` (new) | low | Existing entry has object of τίθει and nom. subject; the use at the end of the housekeeper's speech is an accusative subject of the infinitive after ἄκουσε. | Added " · also neut. acc. sg., subject of an infinitive in indirect statement: …". |
| παῖδ’ · `__broaden__` (new) | medium | Entry says "fem. acc. sg. … ’child, daughter’", but both occurrences in this part are the baby boy (νήπιον masc.; ὀρφανικὸν masc.). | Added a masc. acc. sg. reading, ’boy, son’. |
| παῖδά (before τε) · `__broaden__` (new) | medium | Entry says "fem. acc. sg. … ’daughter’"; the occurrence is Astyanax (νηπίαχον masc.). | Added a masc. acc. sg. reading, ’boy, son’. |

## Checked and passed

All other 163 novel entries: lemma, case, number, tense, mood, voice and the "agreeing with / after" relation true of the form in its line(s); Attic equivalents correct where given; capitalised forms (Θήβῃ, Κιλίκεσσ’, Τρώεσσ’, Ἀστυάνακτ’, Ἠετίων, Ἀνδρομάχη, Ἑκτορίδην, Ἀτρεΐδας, Πλάκῳ, Ὑποπλακίῃ, Ἀρήϊα) keyed lower-case like the house entries. All 21 original `__broaden__` entries verified against the line (αὐτῶν, αὐτὴν, εἴσω, θήβην, κάθιζ’, μητέρα, οἱ, οἷσιν, πάρος, τῇ, ἄλκιμον, ἄλλη, ἄλλοισι, ἠέ, ἥ, ἰῷ, ἴδωμαι, ἀνώγει, ἂν, ὥς, τοὔνεκά): each keeps the old entry whole (the build also enforces this) and each added reading occurs here. Known forms whose existing entry already covers the use were left alone (e.g. ἤ at 438–439 "either … or", τόν/τὴν relative, ἐπὶ in tmesis at 357 and 419).

## Considered and refused

| Finding | Reason refused |
|---|---|
| `__broaden__` entries exceed 230 characters (αὐτῶν 851, ἂν 1022, ὥς 574 …). | The cap applies to what the glosser writes; the runbook requires the old entry whole inside the new one, and the old entries were already over. The added reading in each is short. |
| δᾶερ: "Ionic-epic δαήρ, Attic would be δᾱήρ" describes the lemma, not the voc. form. | Harmless and unverifiable from the line; no wrong grammar for this form. |
| ταμίη "Ionic η (= Attic ταμία)" and θαλπωρὴ "(= Attic θαλπωρά)": Attic equivalents are doubtful as real words. | Not demonstrably wrong; the notes and house usage use the same label; left to avoid rewriting on a guess. |
| ἀπέσσυτο "Attic would be ἀπεσεύθη". | Only a rough equivalent, but flagged as such by "would be"; no better Attic form is available. |
| κιλίκων "(people of the Troad coast)". | The Cilicians of Thebe are in the Troad in the poem; the gloss states the poem's usage. |
| ἤ (438, 439) not given a new "whether … or" reading. | Existing readings "or" / "either … or" already cover both uses; no new reading needed. |
| δαμόωσιν "’will overcome’" for a subjunctive. | The subjunctive in an indirect question has this force; the entry says it is in an indirect question. |

Severity count, pass 2: high 0, medium 5 (ὀτρηρή entry, 6.381 row, μαλακοῖς, παῖδ’, παῖδά), low 4 (θαλερὸς, ἄτης, λώϊον, κράτος).
