# odyssey-070 (14.418–533) — review, pass 1

Scope of pass 1: notes' grammatical labels, claims about position, cross-references, note vs its own `l`/`i`; Greek → `l`; `l` ↔ `i`; remembered English; quotation marks (and the last unit of odyssey-069: it ends with ” closing Eumaeus's speech at 417, so 418 opens in narration and no speech runs over); scansion flags (none in the packet, so nothing to scan). `t` untouched (checked: the units' `t` joined still equal the packet's 116 lines; every `l` has the same number of `\n` as its `t`; no `\n` in any `i`). Whole-unit repeats (442, 453, 507) are identical to the published units; line-level reuse (424, 430, 451, 454, 486, 511) follows the published wording. Pass 2 (gloss.json) still to do.

## Changes

| line · field | severity | what was wrong | what done |
|---|---|---|---|
| 520 · n | moderate | cross-reference false: κατέλεξας 'recounted' is in 508, not 509 | "at 509" → "at 508" |
| 510 · n | minor | "Lines 510–511 are also 6.192–193" overstated: 511 is identical to 6.193, but 510 begins τῷ where 6.192 has οὔτ’ οὖν | note now says 511 is word for word 6.193 and 510 is 6.192 with τῷ for οὔτ’ οὖν |
| 526 · n | moderate | label wrong: νόσφιν ἐόντος called "a genitive absolute with the pronoun οἱ", but οἱ is dative | now: a genitive participle agreeing with the unstated owner of βιότου ("his", Odysseus), not with οἱ |
| 528 · n | minor | "each with its preverb in tmesis" is false of the fourth verb, εἵλετο | "the first three with their preverbs in tmesis", and εἵλετο "with no preverb" |
| 472 · n | minor | ὑπὸ τεύχεσι glossed "their armour"; `l`/`i` say "our armour" and the speaker is "we" | "our armour" |
| 496 · n | minor | "it warns that they are too far": the text does not say the dream warns of anything | γάρ now "gives the reason for the request that follows" |
| 520 · n | minor | αὐτῷ glossed "over him"; it is the dative "him", the "over" belongs to ἐπι- | gloss now says dative "him", "threw over him" with the verb |
| 532 · n | minor | κείων said to mean "be about to lie down" | "a participle from the root of κεῖμαι 'lie', with the sense 'wishing to lie down, going to lie down'" (still not the κείων of 425) |
| 448 · n | minor | "the chine he was honoured with at 437" stated as fact; the text only says "his portion" | "presumably the chine …" |
| 440 · i | minor | "you may become": a wish (optative) read as "may" | "you might become" (as `l`) |
| 462 · i | minor | `i` "I have a word to declare" drops ἐρέω "I shall say" and uses one verb for both εὐξάμενος and ἐρέω; `l` has both | "having made my declaration, I shall say a word;" ("declare" is the table's εὔχομαι; the note still says the sense is uncertain) |
| 430 · l | minor | ἐν ἐλεοῖσιν rendered "into the boards"; ἐν is "in" | "in the boards" |
| 430 · i | minor | "in a heap onto the boards": "heap" is not in ἀολλέα "together" | "and threw them together on the boards" |
| 427 · i | minor | ἐν πυρὶ βάλλε rendered "on the fire", but the same words at 422 are "into the fire" | "threw into the fire" |
| 504 · l | minor | "would give someone a cloak" reads as "someone" being the receiver; τις is the subject | "would give, someone, a cloak" |
| 503 · i | minor | "so young" is not ἡβώοιμι "be in my prime" (`l` and 468 have "prime") | "If only I were in my prime now, and my strength firm;" |
| 471 · i | minor | "had bidden": a pluperfect for the imperfect ἄνωγον (`l` "bade") | "bade it" |
| 459 · l, i | minor | the unit introduces the speech that starts at 462 but ended in ";" (the table's speech-introductions end ":") | ends ":" in both layers |
| 485 · l, i | minor | same: the note itself speaks of "the colon" leading to the next line, but the layers ended in ";" (note contradicting `l`/`i`) | both end ":" |
| 427, 435, 470, 496, 499, 501, 515 · l (7 units) | minor | ASCII ' in possessives ("Maia's", "Atreus' son", …); recent parts (067–069) use typographic ’ | ' → ’ in those `l` |

## Checked and found sound

- 14.461 ἑο κήδετο (unit 459): ἑο is the genitive of the third-person pronoun and κήδομαι takes the genitive. Nothing in the Greek fixes whether Odysseus is the carer or Eumaeus; the note says so, and `l` and `i` keep the same ambiguity. The note's "most naturally Eumaeus cares for his guest" is labelled a preference, not a fact. Left.
- κείων 425 vs 532: two different words (κείω "split", from the root of κεάζω, with ἣν λίπε; κείω "wish to lie down", from κεῖμαι, with βῆ δ’ ἴμεναι). Each note points to the other and `l`/`i` agree with their own note. Left (532 note reworded as above).
- βιότου 527 (line 526–527): βίοτος as "livelihood, property" is the gloss already in the shipped glossary ("life, livelihood, substance one lives on"); object of περικήδετο, which takes the genitive; οἱ "for him" is Odysseus. `l` "livelihood", `i` "property" agree in sense. Left (only the genitive-absolute label was wrong).
- new-renderings.md: each row checked against the text, `units.json` and the table. All 16 match the units' `l`/`i`; none contradicts a table row; the avoided words are not used. Points noted, not changed: (a) ἐϋτρεφής `i` "well-fed" is also the table's `i` for ζατρεφέας — the two differ in `l` ("well-nourished" / "sleek") and the row says why; acceptable under the house practice of "told apart by context". (b) "If only" is also used at 503 where there is no αἴθε/εἴθε (ὣς … ἡβώοιμι); that is the wish-force and matches the 468 row's English. (c) ἦ ῥα καί at 446 is the table's existing mid-narrative row, correctly not repeated here.
- Quotation marks: “ opens at 440, 443, 462, 508; ” closes at 441, 445, 506, 515; the tale inside 462–506 uses ‘ ’ (486–489, 493, 495–498), all balanced; `mark` is on the first unit of each speech (440, 443, 462, 486, 493, 495, 508). 

## Findings considered and refused

- Lower-case `l`/`i` opening after a unit that ends in a full stop (units at 425, 426, 434, 496, 513, 532) and capitals after "·": the shipped parts do the same (069 at 325, 344, 354; 001 at 31, 33) and no convention fixes it. Left.
- ἔνθ’ at 478 rendered "Then" while 520 and 523 have "there": the Greek word is both; 478 is ambiguous and the note at 478 is silent. Left.
- ἂν δόνακας "up through reeds" (472 `l`) with `i` "in the reeds": ἀνά + accusative is a loose "up/through"; the note explains it. Left.
- 438 "κύδαινε" `l` "exalted" / `i` "gladdened": the note gives "exalt, and so 'cheer'". Left.
- 476 γένετο `l` "came to be" / `i` "came on": acceptable idiom for snow. Left.
- 506 χροΐ `l` "skin" / `i` "body": the note gives "skin, body". Left.
- 425 `i` begins lower-case after "…home."; same reason as the first item. Left.
- ὅνδε δόμονδε "the suffix -δε 'toward' on both" (424): identical to the shipped 1.83 note and the shipped glossary entry. Left.
- 457 "σκοτομήνιος" and 457's `i` "foul, moonless night": the table's κακός "evil" `l` / "foul" `i`. Left.
- Scansion: no flags in the packet; no line scanned by hand, no note added.

## State

units.json edited in place by script (only `l`, `i`, `n`); `t`, `ln`, `p`, `mark`, `v`, `title`, `titleEn`, `part`, `about` unchanged. Not run: build. Pass 2 (gloss.json parses against the lines, and a re-read of the changed units) pending.

---

# Pass 2 — gloss.json and re-read

Checked: all 167 novel forms in novel-forms.json are glossed (none missing, none extra); every entry under 230 characters, typographic ’ only, no line numbers; every parse read against its line(s). Re-read of the units changed in pass 1: `l`/`i` agree, quotation marks and `t` still intact.

## Changes

| entry · field | severity | what was wrong | what done |
|---|---|---|---|
| δαιμόνιε | minor | "my good sir, my strange friend": "my good man"-type renderings are turned down in the table (δαιμόνιε is "Strange man") | "strange, uncanny, of one moved by a power beyond himself; as address ’strange one’ …" |
| μετέσσομαι | minor | Attic future written μέτεσομαι | μετέσομαι |
| ἐλεοῖσιν | minor | "table or board for dressing meat" states more than the note, which says the object is not known | "a board or table on which meat was set (exact object uncertain)" |
| `__broaden__` λόχον, μοῖραν, πίονα, ποτὶ, προέηκεν, τὸ | minor | borderline: the old entry already covers the reading (λόχον "ambush"; μοῖραν "what is fitting"; πίονα masc. acc. sg. "fat, rich"; ποτὶ "to, toward"; προέηκεν "send forth"; τὸ already has the ordinal-adverbial τὸ τρίτον) | removed (27 → 21 broadenings) |
| `__broaden__` παρὰ | minor | three additions, two already covered by the old head ("beside", "from") | kept only "+ acc., ’beside, contrary to’ (παρὰ μοῖραν …)", the one new reading |

## Verified

- All 21 remaining `__broaden__` entries begin with the old entry of odyssey-glossary.json (`glossary` key) whole, byte for byte, followed by " · ", and each adds a reading used in this part (αἰδοῖ dative of motive; γέροντος apposition; δοίη potential with κέν; εἴθ’ = εἴθε; εὗδον 3 pl.; θέτο in tmesis with ἀπό; νόσφιν preposition; οἶον neut. acc.; πρὸς tmesis; πὰρ + gen.; τὰς with ἄλλας; τὴν with ἴαν; χεῖμα nom.; ἂν = ἀνά + acc.; ἐγγὺς + gen.; ἐθέλῃ general clause; ἐφάμην "think"; ἑκὰς + gen.; ὡς ὅθ’; ξείνων partitive; παρὰ above).
- No novel key already exists in the shipped glossary.

## Refused

- Dropping the ὡς ὅθ’ and ἐγγὺς broadenings: the old ὡς entry has only the simile ὡς δ’ ὅτε, and the old ἐγγὺς only the adverb, so each adds a real use (469; 518).
- δάμναται "active sense": it takes με as object at 488; entry kept.
- πόροι under "πόρον (πορεῖν)": acceptable LSJ lemma; kept.
