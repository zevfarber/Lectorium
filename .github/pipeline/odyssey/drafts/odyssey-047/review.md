# odyssey-047 (10.174–273) — reviewer pass 1

Edited `units.json` in place by script. `t` untouched (verified: every `t` identical to the original, and the `t`s joined reproduce all 100 lines of the packet). `l`/`i` newline counts still match `t`; no `\n` in any `i`. The build was not run.

Counts by severity (rows below, one per line · field): **high 2, medium 21, low 26** (49 rows, 59 string edits plus `about`).

Sources used beyond the list I was given, so the owner knows: the published `odyssey-0NN.json` files (to check repeated words and half-lines), `LOG.md` and `QUESTIONS.md` (for the nested-speech precedent and the earlier 9.522 she/her case), a grep of `conventions.md`, and `scan_hexameter.py` (run on line 251 only). No translation was consulted.

## Checks that came out clean

- Four whole-unit repeats (10.183–184, 185–186, 187–188, 270) match the published `t`, `l`, `i` character for character, before and after my edits (checked by script).
- Paragraph flags `p` fall on exactly the twelve Murray breaks (174, 178, 189, 198, 203, 226, 229, 244, 251, 261, 266, 270). `mark` is on the first unit of each of the six speeches (174, 189, 226, 251, 266, 271).
- Quotation state at the end of 046: odyssey-046 has no quotation mark anywhere, and its last unit (10.172) ends with a colon introducing the speech that 047 opens. Nothing is open there. 047 therefore correctly opens with ‘ at 174. The outer speech (9.2) is never closed, and there is no “ or ” anywhere in 047. ‘ and ’ now sit on both `l` and `i` of the first and last unit of each of the six speeches (see the medium rows), and on nothing outside them (checked by script).
- Every position claim in the notes was checked against the line: mid-line ends at 193, 196, 209, 231, 235, 247, 268; "second half of 229", "256–257 repeat 230–231", "253 = 211"; "Eurylochus named for the first time in this part" (205); "the goddess is not named until the next line" (220–221).
- Whole-unit and half-line repeats against published parts: 10.180 = 10.171, 10.211/253, 10.239 "as before indeed", 10.220 "stood in the forecourt", 10.224 "of speeches made-beginning", 10.247 "and in him the eyes" (6.130), 10.271 "beside the hollow black ship", 10.197 = 10.148 (see rows).

## High

| line · field | what was wrong | what was done |
|---|---|---|
| 233 · `l`, `i`, `n` | `κατὰ κλισμούς τε θρόνους τε` is the published half-line of 1.145 and 12.388, shipped as "along the seats and the chairs" in both layers. The draft's "easy-chairs / easy chairs" (new-renderings row for κλισμός) breaks the rule that a repeated line keeps its English, and would put two renderings of κλισμός into the book ("seats" at 1.145, 12.388; "inlaid seat" 1.132; "chair" 15.136). | `l` and `i` now read "along the seats and the chairs"; the note says so and cites 1.145 and 12.388. Open for owner: the κλισμός row in new-renderings.md must not enter the table as "easy-chairs"; it should follow the shipped "seat(s)". |
| 270 · `n` | The unit is the published 017/018/044 formula, "So she spoke, and I answered her and said". Here the speaker is Eurylochus and Odysseus answers him: `ὣς ἔφατ’` is 3 sg. of the speaker of 266–269 (addressed `διοτρεφές`, 264 `ὅ γ’`), `μιν` is the one answered, and 271 opens `Εὐρύλοχ’`. "She/her" is simply wrong. The old note said this only obliquely ("stand here for Eurylochus"). | Wording of `l`/`i` unchanged (validator requires identity). The note now says plainly: the English is the published wording of a woman-speaker line and is wrong here; read "he" and "him". **Open question for the owner**: same defect as 9.522 (odyssey-044, QUESTIONS.md). Options: a validator exception for formula units whose Greek has `μιν`/`ἔφατ’` but no sex of the speaker, or a neutral first rendering at 4.464/017/018 ("So was the answer, and I answered…" or "…answered the speaker"), after which 044 and 047 follow. Until then each male-speaker use will carry this note. |

## Medium

| line · field | what was wrong | what was done |
|---|---|---|
| 174 · `l` | No opening ‘ on `l`; published nested speeches (040, 041, 043, 045) carry the mark on both layers. | Added ‘. |
| 176 · `l` | No closing ’ on `l`. | Added ’. |
| 189 · `l` | No opening ‘. | Added. |
| 196 · `l` | No closing ’ on `l` at the end of the speech 189–197. | Added. |
| 226 · `l` | No opening ‘. | Added. |
| 228 · `l` | No closing ’. | Added. |
| 260 · `l` | No closing ’ at the end of Eurylochus' report. | Added. |
| 269 · `l` | No closing ’ at the end of 266–269. | Added. |
| 273 · `l` | No closing ’ at the end of the part. | Added. |
| 226 · `i` | "is singing so finely that the whole floor echoes": γάρ dropped, and the paratactic `καὶ … δέ` ("and the whole floor echoes") made a result clause; this is not what the Greek says and does not match `l`. | `i`: "‘Friends, for someone inside … is singing finely, and the whole floor echoes all around; either a goddess or a woman;". |
| 196 · `l`, `i`, `n` | Half-line `διὰ δρυμὰ πυκνὰ καὶ ὕλην` is published at 10.148 (odyssey-046) as "through thick coppices and woodland" in both layers; draft had "thick thickets" / "the dense thickets and the woodland". | Both layers now "through thick coppices and woodland"; note says it is the same half-line as 10.148. |
| 251 · `l`, `i`, `n` | Same word δρυμά ("thickets") against the shipped "coppices" at 10.148. | "coppices" in `l`, `i`, note. |
| 192 · `l` | `θᾶσσον` is a comparative; shipped `l` for it is "more quickly" (045, lines 31, 44, 72). Draft `l` said "quickly" while its own note said "more quickly". | `l` "more quickly" (`i` stays "quickly", as at 045.44). Note adds that the second layer says "quickly". |
| 228 · `l` | Same. | Same. |
| 268 · `l` | Same. | Same. |
| 247 · `l` | "and in his head the eyes": "head" is not in the Greek. The half-line `ἐν δέ οἱ ὄσσε` is shipped at 6.130 (odyssey-028) as "and in him the eyes". | `l` "and in him the eyes"; note adjusted (οἱ is the dative "in him"). |
| 259 · `l`, `i` | "appeared again": `ἐξεφάνη` is "came into view"; "again" is not in the Greek and is false (they had not appeared before). | "came into view" in both layers. |
| 251 · `n` | The scansion sentence said ἤιομεν "needs its opening long syllable read short". Hand scan (see below) does not support that. | Replaced by one plain sentence. See the scansion section. |
| 210 · `n` | Said "the English keeps the second reading" of περίσκεπτος, but the table row, and the English "with a view all round", keep both readings open. The note contradicted its own `l`/`i` and the table. | "the English phrase … is meant to keep both readings open, and the note does not decide." |
| 237 · `n` | `ἐέργνυ` explained as "imperfect of ἔργνυμι with a lengthened first vowel": unsupported. The form is the epic ἐέργνυμι (= ἔργνυμι, εἴργνυμι). | Reworded; no claim about the vowel. |
| 229 · `n` | "the participle being the uncontracted καλέοντες": the printed form is καλεῦντες, which is καλέοντες with εο run together as ευ; the label was backwards. | Reworded. |

## Low

| line · field | what was wrong | what was done |
|---|---|---|
| 176 · `i` | "while there is *still* food": ὄφρα has no "still" (not in `l`). | "still" removed. |
| 176 · `n` | μνησόμεθα "from μνάομαι … works as an exhortation": tense not stated. | "a future form of μνάομαι … used here as an exhortation". |
| 178 · `n` | "tmesis for ἐκκαλύψασθαι" (an infinitive for a participle); "it is usually understood" (an unverifiable claim about scholars). | "tmesis for the participle of ἐκκαλύπτομαι"; "the likeliest sense is". |
| 180 · `n` | "10.171, where the stag was first described": not so (the stag is described from 158). | "the same line as 10.171 and has the same English". |
| 181 · `n` | τεύχοντ’ "an imperfect": it is the middle (-ο elided). | "the middle imperfect". |
| 190 · `n` | "repeated three times in οὐδ’ ὅπῃ": ὅπῃ comes four times in the unit. | Count corrected. |
| 194 · `n` | "preposition after its noun": πέρι follows the relative pronoun τὴν. | "after the pronoun it governs". |
| 201 · `n` | "λιγύς, the word in the fixed 'clear-voiced heralds'": the heralds' word is λιγύφθογγοι. | "the first part of λιγύφθογγοι". |
| 203 · `n` | "the epithet is the one Homer gives the Achaeans": claims usage outside this part. `ὀπάζω` glossed "assign", a word the table avoids for ὄπασσα. | "a stock epithet"; gloss "grant, give". |
| 214 · `n` | ἀνέσταν "shortened aorist ἀνέστησαν": imprecise. | "root aorist of ἀνίστημι, third plural in -αν (Attic ἀνέστησαν)". |
| 216 · `n` | "preposition after its noun" (ἀμφί follows the pronoun τοὺς); the "strong-hoofed of mules" sentence asserts something about 6.253 that this part cannot show. | Both reworded; "ὄνυξ can mean 'claw' or 'hoof'; for wolves and lions it is the claw". |
| 219 · `n` | Gloss "dreadful" for αἰνά; the table keeps "dread" for δεινός. | "fearsome". |
| 220 · `n` | ἔσταν as in 214; "Κίρκης is the genitive with the participle" (it is the genitive after ἄκουον). | Both reworded. |
| 226 · `n` | "the phrase of the previous unit": the words are the same but in another order; ἀοιδιάει called "a lengthened form of ἀείδω" (it is a verb built on ἀοιδή). | Both reworded. |
| 192, 228, 268 · `n` | Note said θᾶσσον is "more quickly" with `i` "quickly" and no explanation. | Added "(the second layer says simply 'quickly')". |
| 241 · `n` | "ἐέρχατο … 'they had been shut in'" against `l` "were shut in". | "so 'they were (by then) shut in'". |
| 244 · `l`, `n` | `l` "went" against `i` and the note "came"; note gloss "bitter, cruel" (the table refuses "cruel"). | `l` "came"; note "bitter … precise sense uncertain". |
| 246 · `n` | ἐκφάσθαι "aorist infinitive": φάσθαι is not safely aorist. | "the infinitive". |
| 247 · `n` | See the 247 `l` row. | Note reworded as there. |
| 252 · `n` | "The line is the same as 211": ambiguous, the second line (253) is. | "The second line, 253, …". |
| 258 · `n` | Said the line is 232 with ἐγών and ὑπέμεινα, omitting αὐτάρ for δέ. | Added. |
| 271 · `l` | "you indeed remain": reads as a statement; μέν’ is the imperative. | "you indeed, remain". |
| 273 · `l`, `n` | `l` "for" translated δέ, which is "and". | `l` "and strong upon me has come necessity"; note says δέ gives the reason, so "for" in `i`. |
| `about` | "wakes" the companions; "runs back" (the Greek says came); the men keep "their own minds" garbled; "begs Odysseus not to go" (Eurylochus begs not to be taken back there and urges flight). | Reworded. |

## Scansion, line 251

Hand scan of `ἤιομεν, ὡς ἐκέλευες, ἀνὰ δρυμά, φαίδιμ’ Ὀδυσσεῦ·`: with ι and ο kept apart the line has 18 syllables and cannot be a hexameter; with ιο as one syllable it has 17 and is five dactyls and a spondee: ἤ–ιο⏑μεν⏑ | ὡς– ἐ⏑κέ⏑ | λευ– ες⏑ ‖ ἀ⏑ | νὰ– (long by position before δρ) δρυ⏑μά⏑ | φαί– δι⏑μ’Ὀ⏑ | δυσ– σεῦ×. The first syllable ἤ is long, so the old note's "opening long syllable read short" was false; the only licence needed is the fusion of ιο into one short syllable (the scanner's "synizesis … long scanned short" is that same fused syllable). Real, as transmitted. The note now ends with one plain sentence: "Line 251 is metrically irregular as transmitted: it scans only if the ι and ο of ἤιομεν are run together into one short syllable (ἤ–ιο–μεν)."

## Table / new-renderings.md consistency (not edited; for the owner)

- κλισμός: must be "seat(s)" (shipped 1.145, 12.388), not "easy-chairs" (high row above).
- κρατερώνυχες: the existing row at line 503 of conventions.md (mules) lists "strong-clawed" among the *avoided* renderings; the new row uses it for wolves and lions. Fine in sense, but 503's avoided column needs amending ("strong-clawed" for mules only) or the two rows contradict.
- ἀπείριτος: the new row says "boundless" is reserved for ἀπείρων; the table also gives ἄσπετα κρέα "boundless" (line 847) and 183–184 here ship "boundless meat". "Limitless" itself is fine and distinct; fix the reservation wording.
- ἀδευκής "bitter": consistent with the shipped "bitter" in odyssey-018 (unit at line 487) and odyssey-029 (unit at line 273); the table's πικρός also uses "bitter", so the two share a word; acceptable, note in the row.
- λιγέως, καλλιπλόκαμος ("fair-plaited", distinct from ἐυπλόκαμος "fine-plaited" at 10.135 and 10.136), αἰνὰ πέλωρα ("fearsome" against δεινὸν πέλωρ "dread"), ἄκυλος: consistent with the table and with the units.
- δρυμά "coppices": shipped at 10.148 and now used at 10.197 and 10.251; no table row yet.
- θᾶσσον: no table row; shipped practice is `l` "more quickly" / `i` "quickly" (045); worth a row.

## Findings considered and refused

- 174, 190: `i` drops "for" (γάρ) at the head of a speech. Refused: "for" cannot open a speech in English, and the reason is carried by the sentence that follows; `l` keeps it.
- 267 `l`/`i` "come back", "bring back": "back" is not in ἐλεύσεαι / ἄξεις, but both layers agree and the sense (Eurylochus says Odysseus will not return from the hall) is the evident one. Left; flagged here only.
- 230 "at once" against 244 "quickly" for αἶψα/αἶψ’: shipped parts use both ("at once" 5.6; "quickly" 4.392, 7.291, 13.455, 16.282). No table row; left.
- 212 `i` "by giving them evil drugs" for ἐπεὶ … ἔδωκεν (cause rather than means): same state of affairs; left.
- 259 `l` "all in a body" for ἀολλέες: shipped uses "all together" (13.412, 46.132) but also "thronging together"; `i` carries it. Left.
- 193 `i` "though" for δέ (`l` "but"): acceptable weakening in the idiomatic layer.
- 192 `i` "is left to us" for ἔτ’ ἔσται: paraphrase, same force.
- Notes calling βῆ δ’ ἰέναι and μύθων ἦρχε "the formula": the repeat of both is shown by the published parts (5.9, 1.28, 30.46). Left.
- 208 note "makes twenty-three men": derivable from this part alone (Eurylochus + 22). Left.
- 234 note "χλωρόν a pale greenish-yellow": gloss in the note only; rendering "yellow honey" is as in the table. Left.
- `mark` wording ("Odysseus rouses the crew", etc.): no convention fixes it; consistent with 040–045.
- Remembered English: I rebuilt each `i` from the Greek and found no phrase that looked supplied rather than built ("their dear hearts were broken within them", "closest of my companions", "something to soothe the heart" all follow the grammar).

## Open questions for the owner (summary)

1. 10.270: published "she/her" formula against a male speaker (same as 9.522). Needs a validator exception or a neutral first rendering.
2. κλισμός: table row must follow shipped "seats" (1.145, 12.388).
3. κρατερώνυχες row against line 503; ἄσπετος/ἀπείρων "boundless" reservation.
4. Line 251: scanner flags it UNRESOLVED ("long scanned short"); hand scan says the only licence is the single short syllable from ιο, so the scanner's label may need a synizesis exception for ἤιο-.

---

# Pass 2 (adversarial reviewer, second of two)

Re-checked `units.json` afresh in pass 1's order (notes' grammatical labels; Greek against `l`; `l` against `i`; remembered English against the published parts; quotation marks; the scansion note at 251), then every entry of `gloss.json` against its lines, then `new-renderings.md`. Edited `units.json` and `gloss.json` in place by script with exact-match asserts. `t` untouched (the `t`s are identical to pass 1's output, and still tile all 100 packet lines word for word). `l`/`i` newline counts and the no-`\n`-in-`i` rule still hold. Build not run. No translation consulted; sources were the published `odyssey-0NN.json`, `odyssey-glossary.json`, `source/odyssey-murray1919.json` (for line numbers), `conventions.md`.

Pass 1's edits introduced no new grammatical error that I found. Its tile, paragraph, `mark` and quotation-mark bookkeeping is correct (opening ‘ and closing ’ on the first and last unit of each of the six speeches, in both layers, nothing elsewhere; no ASCII quotes in `l`/`i`). The four whole-unit repeats (180, 183–184, 185–186, 187–188, 270) are still character-identical to the published `t`/`l`/`i` after both passes, checked by script against every published part (the 270 unit against 017, 018 and 044 at once).

Counts by severity (change rows below): **high 1, medium 5, low 10** (16 rows). Open owner questions are listed separately and are not counted. Refused findings are listed at the end.

## Changes

| line · field | severity | what was wrong | done |
|---|---|---|---|
| 233 · `n` | high | The note (and pass 1's review, and the task brief) cites the shipped half-line as "1.145 and 12.388". Part odyssey-012 is Book 3 (3.313–403), not Book 12: the shipped line is **3.389** (checked against `source/odyssey-murray1919.json`: 1.145 and 3.389 both read ἑξείης ἕζοντο κατὰ κλισμούς τε θρόνους τε). A false cross-reference. | "1.145 and 12.388" → "1.145 and 3.389". The same slip (part id read as a book) is in pass 1's κλισμός rows above ("12.388") and for the lone κλισμῷ ("15.136", really 4.136, part odyssey-015); both corrected in `new-renderings.md`. |
| 198 · `l`, `i` | medium | The half-line Λαιστρυγόνος Ἀντιφάταο is shipped at 10.106 (odyssey-046) as "of Antiphates the Laestrygonian" in both layers; the draft had "of the Laestrygonian Antiphates". A repeated half-line keeps its English. | Both layers now "of Antiphates the Laestrygonian" (the note already read "Antiphates the Laestrygonian"). |
| 220 · `l`, `i`, `n` | medium | ὀπὶ καλῇ after ἀειδούσης / ἀοιδιάουσ’ is shipped at 5.61 (odyssey-022) as "singing with a beautiful voice" (`l`) and "singing in a beautiful voice" (`i`). The draft said "a fine voice" in both layers and the note glossed it so. | `l` "singing with a beautiful voice", `i` "singing in a beautiful voice"; the note says "beautiful voice" and that it is the same words and English as at 5.61. (καλός is "fine" elsewhere; the shipped half-line wins.) New row in `new-renderings.md`. |
| 189 · `n` | medium | κέκλυτε called "the perfect imperative of κλύω"; it is the reduplicated aorist imperative (as `gloss.json` already says, and as the notes at odyssey-005, 031, 033, 037, 038 say). The unit contradicted its own glossary entry. | "the reduplicated aorist imperative of κλύω". |
| 176 · `n` | medium | μνησόμεθα called "a future form of μνάομαι", while `gloss.json` has "aor. subj. mid. 1 pl., short-vowel, hortatory (= μνησώμεθα)" under μιμνήσκομαι. Note and glossary disagreed on the parse of the same form. | Note now: a short-vowel subjunctive (= μνησώμεθα) of μιμνήσκομαι, used as an exhortation. (I could not settle future against short-vowel subjunctive from the aids at hand; the exhortative sense is the same either way, and the glossary was left as it stood.) Owner may prefer a hedge. |
| 271 · gloss `μέν` | medium | Not a unit field. The printed μέν’ in σὺ μέν’ αὐτοῦ is the elided imperative μένε (the note says so), but the shipped entry for `μέν` (the form is identical once the apostrophe is dropped) knows only the particle and the asseverative. A reader would be told the word is "on the one hand". | New `__broaden__` entry: old entry whole + " · also μένω — stay, wait; pres. imper. 2 sg., elided (μέν’ = μένε): ’stay’". |
| 220 · gloss `καλλιπλοκάμοιο` | low | Glossed "fair-tressed", the word the table reserves for ἐυπλοκαμῖδες and the new-renderings row refuses; the units say "fair-plaited". | "with beautiful locks, fair-plaited (κάλλος + πλόκαμος ’lock’)". |
| 240 · gloss `τὸ` | low | In ὡς τὸ πάρος περ the τὸ is the article before the adverb πάρος; the shipped entry has only the pronoun and the article before a noun. | `__broaden__` entry added (old whole + " · also article-like before the adverb πάρος: ’as before’ (ὡς τὸ πάρος περ)"). |
| 229 · gloss `καλεῦντες` | low | Called "epic uncontracted (= Attic καλοῦντες)": καλεῦντες is the shortened by-form of the uncontracted καλέοντες, not itself uncontracted. (The unit note, rewritten in pass 1, is right.) | "epic by-form of καλέοντες (= Attic καλοῦντες)". |
| 178 · gloss `καλυψάμενοι` | low | Added "throwing off their cloaks", which the unit note expressly refuses to decide ("the object is not stated"). | Reduced to "’uncovering themselves’". |
| 201 · gloss `λιγέως` | low | "clearly, loudly, shrilly … of wailing": pins a context, and "loudly"/"shrilly" are the renderings the new row turns down. | "λιγύς — clear-toned, clear-voiced; adv. λιγέως: ’clearly, in a ringing voice’". |
| 216 · gloss `κρατερώνυχες` | low | "ὄνυξ ’claw’" only, though the shipped κρατερώνυχας entry reads ὄνυξ as hoof. | "’claw, hoof’". |
| 195, 219, 176, 203 · gloss `ἀπείριτος`, `αἰνὰ`, `βρώμης`, `ὄπασσα` | low | Entries pinned to the line ("of the sea", "of the monsters", "with μνησόμεθα ’think of food’"); `ὄπασσα` said "assign", a word the table avoids; `ἀπείριτος` listed "boundless" before "limitless". | Pins removed; "grant"; "limitless, boundless". |
| 207 · gloss `ἔθορε` | low | Lemma θρώσκω; LSJ lemmatises θρῴσκω and the unit note uses θρῴσκω. | Lemma θρῴσκω. |
| 247 · `n`, 235 · `n` | low | Notes assert something about the rest of the poem: "θυμός is ‘heart’, as always"; "the epithet λυγρός always ‘grievous’". | "as always" cut; "the adjective λυγρός ‘grievous’". |
| `about` | low | Order wrong: Odysseus takes sword and bow and orders Eurylochus to lead (261–263) before Eurylochus clasps his knees and begs (264–269); the summary put the plea first and had Odysseus take sword and bow after his reply. | Reordered: takes sword and bow and orders him to lead back; Eurylochus clasps his knees, begs not to be taken there, urges flight; Odysseus tells him to stay and says he will go himself. |

Not a count of rows: `new-renderings.md` was edited (below).

## `new-renderings.md`

- κλισμός row: now "seats" in both layers, "along the seats and the chairs", citing 1.145 and 3.389 (and 1.132 "inlaid seat"; the lone κλισμῷ at 4.136 shipped "chair"), with "easy-chairs" among the avoided renderings. (Pass 1's "12.388" and "15.136" are part ids; corrected.)
- ἀπείριτος row: the claim "boundless is reserved for ἀπείρων" was false (ἄσπετα κρέα is also shipped "boundless", 10.183–184 and the table's own row); reworded to say so.
- κρατερώνυχες row: now says plainly that it clashes with the existing mule row (open question below).
- Added rows: ὀπὶ καλῇ ("beautiful voice", shipped at 5.61); δρυμά ("coppices", 10.148, 10.196, 10.251); θᾶσσον (`l` "more quickly", `i` "quickly" as at odyssey-045 lines 44 and 72; "sooner" shipped where the sense is 'so that … sooner'). Every other row was checked against the final `units.json` and matches (λιγέως, καλλιπλόκαμος, αἰνὰ πέλωρα, χλωρὸν μέλι, Πραμνεῖος, ἄκυλος, ἀδευκής, περίσκεπτος, ἀγάομαι, διοτρεφές, ὀρέστεροι, ὄπασσα).

## Open owner questions (not edited; existing table rows left alone)

1. κρατερώνυχες: `conventions.md` row (mules, 6.253) lists "strong-clawed" as an avoided rendering; this part uses it for wolves and lions at 10.218. Either amend the avoided column ("strong-clawed" for mules only) or choose one rendering for both animals.
2. "boundless": the table gives it to ἀπείρων (7.286) and ἄσπετα κρέα (9.162), and the table's ἀθέσφατος and ἀπέλεθρος rows say "boundless (reserved for ἀπείρων)". That reservation is already broken by ἄσπετα, shipped again at 10.183–184. ἀπείριτος is "limitless" here and kept apart; the owner should say whether "boundless" stays shared by ἀπείρων and ἄσπετος.
3. 10.270: the published "So she spoke … answering her" formula against a male speaker (Eurylochus); same defect as 9.522. Unchanged from pass 1; the note says it is wrong here.
4. Line 251: the scanner flags ἤιομεν as UNRESOLVED; the hand scan below confirms pass 1 and the only licence is the single short syllable from ιο.
5. μνησόμεθα (10.177): future or short-vowel aorist subjunctive. Note and glossary now agree on the subjunctive; confirm.
6. καλός is "fine" (κάλλιμα row) but shipped as "beautiful" in ὀπὶ καλῇ (5.61); the new row records it as an exception.

## Scansion, line 251 (re-checked)

ἤιομεν, ὡς ἐκέλευες, ἀνὰ δρυμά, φαίδιμ’ Ὀδυσσεῦ with ι and ο apart is 18 syllables, one too many for a hexameter. With ιο as one short syllable it is 17: ἤ ιο μεν | ὡς ἐ κέ | λευ ες ἀ | νὰ δρυ μά | φαί δι μ’Ὀ | δυσ σεῦ. That is five dactyls and a spondee/trochee, with ἀνὰ lengthened by position before δρ. Pass 1's conclusion and the note's single sentence stand. One slip in pass 1's review log, not in the note: its foot division is misaligned (it prints "ἤ–ιο⏑μεν⏑ | ὡς–"); the syllable count and the licence are right.

## Findings considered and refused

- ἀννεῖται gloss "of the sun" and φαεσίμβροτος "epithet of the sun": a word-usage remark, as with "epithet of Dawn" in published entries; left.
- 190 `l`/`i` lower-case "sun" against the table's "the mortal-lighting Sun" (10.138, Helios the god): here the heavenly body, as ἠέλιος elsewhere in the part; left.
- 230/256 "at once" against 244 "quickly" for αἶψα: pass 1 refused; shipped practice uses both, no table row; left. (A row would end the drift; owner's choice.)
- ἐέρχατο gloss "(= Attic εἴργμην-type)", ἀννεῖται lemma ἀννέομαι, ἐκφάσθαι "(= ἐκφάναι)": unverifiable in the aids to hand; plausible; left.
- Gloss entries over 230 characters: only the `__broaden__` entries (αὐτῶν, βάλεν, κακὸν, πρὶν, τῶν, and my two additions μέν, τὸ). The cap applies to novel entries (LOG.md, 5.1–96 pass 2); all novel entries are under 230.
- ἐγώ (270, before enclitic μιν) against the shipped entry's "accented ἐγώ before the enclitic τοι": same accent rule, parse true; left.
- 247 `l` "and in him the eyes": the half-line ἐν δέ οἱ ὄσσε is shipped at 6.131 (odyssey-028) in exactly that form. The other shipped parallel, 4.704–705, reads τὼ δέ οἱ ὄσσε δακρυόφι πλῆσθεν (different words), so "her two eyes" does not bind. Pass 1 right (its "6.130" is a line off, 6.131; not in the units).
