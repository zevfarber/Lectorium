# Review — odyssey-085 (Odyssey 17.306–408)

Reviewer, two passes. Sources used: runbook section 2, conventions.md (read in full for the sections, and by search for the
house table plus the appended rows), packet.md, units.json, new-renderings.md, the published odyssey-*.json files in the repository root
(every cross-reference below was checked there), and odyssey-084 for the speech state going in. `t` was not touched
(verified after every edit: the units' `t` are byte-identical to the draft, and joined they equal the source lines; `ln`, `p`, `v`, `mark` unchanged).
No modern translation was opened or recalled. `build_odyssey.py` was not run.

Severity scale: **high** = blocks the build or makes the page wrong and cannot be fixed within the reviewer's remit;
**medium** = false grammatical or positional claim, house-rendering breach, or `l`/`i` contradicting its own note;
**low** = polish, a particle dropped, an imprecise phrase.

Counts

| | high | medium | low |
|---|---|---|---|
| Pass 1 (units.json) | 1 (open) | 15 (fixed) | 21 (fixed) |
| Pass 2 (units.json) | 0 | 0 | 1 (fixed) |
| Pass 2 (gloss.json, reported only) | 0 | 3 | 10 |

## OPEN — needs the caller before the build

**H1 · 388/389 · `t` · high · unit cut in the wrong place (not fixed, `t` is off limits).**
Unit 48 (ln 388) ends `…πέρι δ’ αὖτ’` and unit 49 (ln 389) begins `ἐμοί· αὐτὰρ ἐγώ γε`. The ano teleia after ἐμοί is where the
sense-unit ends; the draft's own notes, `l` and `i` all assume the cut falls there (unit 48 `l`/`i` already contain "to me", unit 49 `l`
begins "but I, for my part", unit 48's note says "ends … at the ano teleia after ἐμοί"). Only `t` is cut one word early. The fix is
mechanical and leaves the joined text unchanged: move the word `ἐμοί·` from the front of unit 49's `t` to the end of unit 48's `t`
(unit 48: `…δμωσὶν Ὀδυσσῆος, πέρι δ’ αὖτ’ ἐμοί·`; unit 49: `αὐτὰρ ἐγώ γε\nοὐκ ἀλέγω, …`). `ln` stays 388 / 389. Until it is done, unit 48's
`l`/`i` translate a word its `t` lacks, and unit 49's `t` has a word its `l`/`i` lack. No note needs changing once `t` is re-cut.

## Pass 1 — changes made (line · field · severity · what was wrong · what was done)

Positions and cross-references were checked in the repository. Verified true as written: 17.296 and 17.300 κεῖτ’ = κεῖτο; 17.297 κόπρῳ;
17.294 ἀγίνεσκον; 17.244 ἀγλαΐας; 17.247 Μελάνθιος, αἰπόλος αἰγῶν; 14.340 δούλιον ἦμαρ; 16.457 λυγρὰ … εἵματα … περὶ χροΐ;
5.244 (ξέσσε); 2.85 and 2.303 (the same vocative pair, rendered identically); 17.311 = 17.380 and 17.346 = 17.351; 17.330 and 17.342 ἐπὶ οἷ καλέσας; 5.28 ἦ ῥα καὶ … ἀντίον ηὔδα (the pattern the 17.396 rendering follows).

| line | field | sev | wrong | done |
|---|---|---|---|---|
| 310 | l | low | ἀγλαΐης **δ’** : δέ left out of `l` (`i` has "and"); `l` "keep them" against the note's and `i`'s "tend" (κομέουσιν, as 319) | "and for the sake of splendour lords tend them.”" |
| 313 | i | medium | ἀλκήν rendered "strength"; the house table fixes ἀλκή as "might" (row on 9.214, "kept apart from μένος 'strength'") | "speed and might" |
| 317 | n | medium | "περιῄδη … with no augment": the form is ᾔδη (augmented), cf. the published notes on ᾔδη (odyssey-005 line 15, odyssey-070 line 433) | "with the old ending -η for -ει (Attic ᾔδειν)" |
| 318 | n | medium | "ὤλετο … with no augment": ὤλετο is augmented (the unaugmented form is ὄλετο; the published notes say so at odyssey-002 line 168 and odyssey-008 line 365) | "‘perished’, and keeps its augment (the unaugmented form is ὄλετο)" |
| 318 | i | low | "since his lord has perished": δέ made causal, a force the Greek (ἄναξ δέ οἱ …) does not state | "…misery; his lord has perished far from his fatherland, and …" |
| 320 | l | low | "have mastery" for ἐπικρατέωσιν ἄνακτες; the same words are published at 066 line 60 as "hold sway" | "when no longer hold sway the lords" |
| 322 | i | low | "on the day when the day of slavery takes hold of him": the day said twice | "…half of a man’s excellence, once the day of slavery takes hold of him.”" |
| 322 | n | low | δούλιον ἦμαρ glossed "a day of slavery" against `l` and the table's "the day of slavery" | "the day of slavery" |
| 328 | n | medium | position: συβώτην is "two lines on" from τόν; it stands in the next line (329) | "in the next line" |
| 328 | n | low | "νεῦσ’ is ἔνευσε": nothing said of the elision/augment | "νεῦσ’ is νεῦσε, elided and unaugmented (Attic ἔνευσε)" |
| 333 | n | low | "ἐφέζετο is the aorist middle": the published notes on the Homeric ἕζετο family call it the imperfect | "the imperfect middle of ἐφέζομαι" |
| 339 | n | medium | "ἷζε … with no augment": unsupported (the circumflex long ῑ is the augmented shape; published notes say only "imperfect of ἵζω") | claim removed |
| 339 | n | low | "The last line is nearly the same as 5.244": 5.244 has ξέσσε **δ’**, 17.341 has no δ’ | stated exactly |
| 345 | l | low | φέρων rendered "taking them" (that is ἑλών elsewhere in this part, and 333 renders φέρων "carrying") | "carrying them" |
| 345, 350 | l | low | μάλα in μάλα πάντας dropped from `l` (the note glosses it "every one") | "going round to every one of them, the suitors;" in both (they repeat each other) |
| 345 | n | low | "The same line recurs at 351": the unit is two lines; only 346 recurs | "Its second line, 346, recurs at 351." |
| 347 | l | medium | "for a needy man to have beside him" contradicts the note, which reads the line as "shame is not good to be present for a needy man" | "and shame is not good to be present for a needy man.”" |
| 353 | n | medium | "προσέφη is the unaugmented aorist": προσέφη = πρός + ἔφη, augmented; published notes say "the aorist of πρόσφημι" | "the aorist of πρόσφημι" |
| 354 | l, i, n | medium | ὄλβιον rendered "fortunate". The house table fixes ὄλβιος as "prosperous" (row λαοὶ ὄλβιοι, which rejects "fortunate"; shipped "prosperous" at 052 line 136, 055 line 448, 062 line 40). The drafter's new-renderings row contradicts the table | "prosperous to be" / "may be prosperous among men"; note: "ὄλβιον is ‘prosperous’, as the same word is rendered elsewhere" |
| 356 | n | low | "ἦ ῥα καί … here in the middle of the narrative": it closes a speech | "which closes a speech and moves the story on" |
| 360 | l, i | medium | πύρνα rendered "loaves": the table's κοτύλη · πύρνος row and the 17.12 row fix "a wheaten loaf" in both layers and reserve "loaf" alone for other words (the part's own ἄρτος row says "wheaten loaf (reserved for πύρνος)") | "wheaten loaves" in both layers |
| 364 | n | low | the note leaves the subject open but `l`/`i` commit to "she" | added "the translation takes Athena" |
| 370 | n | low | "with περί after its noun’s adjective": muddled | "with περί standing between the demonstrative and its noun" |
| 374 | n | low | "Συβώτην is the object": capital S, the Greek has lower case | "The object is συβώτην." |
| 375 | l | low | τίη δὲ **σύ**: σύ dropped from `l` | "why then you this man to the city / led?" |
| 378 | l, n | medium | ὄνοσαι rendered "scorn" in `l`; the same verb is published at odyssey-025 line 379 as "make light of" in both layers; the drafter's row splits `l`/`i` | "Or do you make light of it that your lord’s livelihood they eat up," ; note reordered to put ‘make light of’ first |
| 381 | n | medium | note says καλά is "used as an adverb", while `l` reads it as the object ("fair things") | "‘not indeed fair things’, … the object of ἀγορεύεις, which English turns into ‘not well’" |
| 382–385 | i | low | "delight **us** by his singing": "us" is not in the Greek | "who may delight by his singing?" |
| 386 | n | medium | position: "a line-closing phrase also found at 1.98". At 17.386 it closes the line, at 1.98 (ἠδ’ ἐπ’ ἀπείρονα γαῖαν ἅμα πνοιῇς ἀνέμοιο) it stands mid-line | "a phrase that closes this line and stands mid-line at 1.98" |
| 387 | i | low | "a beggar who will **only** wear down his host": "only" not in the Greek | "who will wear down his host" |
| 387 | n | low | trailing space | stripped |
| 392 | n | medium | "ηὔδα the unaugmented imperfect": ηὔδα is augmented (αὐ- → ηὐ-), as the published notes say | "the imperfect of αὐδάω, augmented (αὐ- lengthened to ηὐ-)" |
| 396 | n | low | sentence without a verb ("Ἀντίνοον being the object …") | "Ἀντίνοον is the object of προσηύδα" |
| 396 | n | medium | "προσηύδα is the unaugmented imperfect": augmented (προσ-ηύδα) | "the imperfect of προσαυδάω, ‘spoke to’, with its augment inside the compound (προσ-ηύδα)" |
| 397 | i | low | "as a father does of his son" | "does for his son" |
| 399 | i | low | `l` "this", `i` "that" for τοῦτο | "this" |
| 401 | i | medium | ἅζευ rendered "hold back out of awe of" in `i`; the same verb is already published at odyssey-044 line 477 as "shrink from" in `l` and `i`, and `l` here says "shrink from" | "So do not shrink from my mother in this, nor from any other of the servants …" |

Counts above are by finding: medium 15 (317, 318, 328, 347, 353, 354, 360, 378, 381, 386, 392, 396, 401, 313, 339), low 21, high 1.

## Findings considered and refused

- **Units 56 (400) and 58 (403–404) contain ano teleiae inside the unit** (three in 400, one after νόημα in 403). By the segmentation rule a
  unit ends at an ano teleia; splitting these would change `t`, which the reviewer may not do. 26 published units already do the same
  (e.g. odyssey-011 line 265, odyssey-016 line 274), and the draft's note on 400 says so ("Three short sentences share one line"). Left as is; if the caller
  wants strict cutting, 400 should become three units and 403/404 two, re-cut from the source lines, with `l`/`i` and notes split to match.
- **347 `i` "a good companion"**: παρεῖναι is an infinitive of respect; "companion" interprets it. Kept: it is natural English for "be present with a man in need" and no sense is added.
- **312–: Unit 12 (326) `i` drops αὖ ("in turn")**; 375 `i` drops σύ; 396 `i` drops "too" (καί). `i` is prose and may drop weak particles; `l` carries them.
- **375 `i` "well-known" against the shipped "easily known/recognized" for ἀρίγνωτος** (015, 029, 084). A vocative "easily known swineherd" is not English; the new-renderings row
  records the choice and `l` keeps "easily-known". Kept.
- **330 δίφρος "stool"** against the table's "chariot / car" for δίφρος: the sense is different (a seat, as the note says), and the row records it. Kept.
- **336–337 `i` "on a staff"** is not in the Greek, but the note says "the staff is understood, not named". Kept.
- **311 and 380 note "the poet … speaks to Eumaeus as ‘you’"** repeats published wording and matches the formula's published rendering. Kept.
- **306 mark "Odysseus asks"**: the speech is partly a remark and partly an implied question; acceptable. Kept.
- **364 subject** (Athena vs Odysseus): both readings are possible; the draft's choice is now stated in the note. Kept.
- **354 `i` "I pray that …"** supplies a verb for the infinitive of wish; the note says the infinitive stands for a wish. Kept.
- **313 `i` "still" and "in performance"** (for εἴη and ἔργα): "still" is implied by the condition; "performance" is a loose but defensible rendering of ἔργα, and `l` carries "deeds". Kept.
- **393 `i` "I ask you"** for the dative μοι: kept as an ethic-dative rendering.
- **Scansion:** the packet flags no line; nothing to scan by hand, nothing added to any note.
- **Metre/quotes:** 11 opening “ against 10 closing ” is correct: Antinous's speech starts at 406 and runs past 408 (unit 61 has no closing mark). Marks stand on the first unit of each of the 11 speeches; the neighbouring last unit of 084 (17.304–305) is narration, so no quote is open on entry.

## Repository checks that passed

`t` of all 62 units joins to the source lines; `ln` correct for every unit (including the mid-line starts at 310, 338, 360, 389, 399); `p` on exactly the 14 paragraph openings (306, 311, 324, 328, 336, 348, 350, 353, 356, 369, 374, 380, 392, 396); `l` has the same number of lines as `t` in every unit; no `\n` in any `i`; no straight quotes or backticks anywhere; the four whole-unit repeats (311, 353, 380, 392) are identical in `l` and `i` to every published occurrence; the line 361 wording and the line 406 wording follow the published `l`/`i` of 081 and 005.

## Required follow-ups outside units.json (not done by the reviewer)

new-renderings.md will not match units.json after this review; the caller should correct it before its rows are copied into conventions.md:
1. **ὄλβιος row (17.354)**: delete. The table already has ὄλβιος (11.136) as "prosperous"; units.json now follows it.
2. **ἅζομαι row (17.401)**: delete or change to `l` "shrink from" / `i` "shrink from" (the shipped odyssey-044 wording); the avoided-list should drop "hold back out of awe of".
3. **ὄνομαι row (17.378)**: `l` "make light of" (not "scorn"); `i` "make light of" (as shipped at odyssey-025 line 379).

## Pass 2

Pass 2 re-read every unit after the edits (Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks, every note against its own `l`/`i`) and re-ran the structural checks above.
One low item found and fixed: unit 42 note said ὅτι "gives the thing scorned", out of step with the reworded `l`; now "gives the matter taken lightly".
Nothing else found in units.json. H1 remains open.

### gloss.json (read in pass 2; every parse checked against its line; not edited, since it is the glosser's file)

All 101 novel forms are present, no extras. All parses not listed below were checked and are correct for their lines. Needed changes:

| key | sev | wrong | proposed |
|---|---|---|---|
| ἀγείροι | medium | "aor. opt." — ἀγείροι is the present optative (the aorist is ἤγειρα, opt. ἀγείραι/ἀγείρειε) | "ἀγείρω — gather, collect; pres. opt. 3 sg., in a purpose clause with ὡς ἄν: ’that he might collect’" |
| κεχρημένῳ | medium | lemma "χρῄζω"; the glossary's existing entries for κεχρημένος/κεχρημένον/κεχρημένοι all use χράομαι | "χράομαι — use; perf. part. (+ gen.) ’in need of, lacking’; masc. dat. sg., used alone: ’needy, in want’" |
| (known) εἴη | medium | the existing entry covers wishes and fear clauses only, not the uses here: protasis after εἰ (εἰ τοιόσδ’ εἴη), ὡς εἰ … εἴη, indirect question after a past verb (τίς εἴη) | add to `__broaden__`: old entry whole + " · also in a conditional protasis: ’if he were’ (εἰ τοιόσδ’ εἴη) · also in an indirect question after a past verb: ’who he was’ (τίς εἴη)" |
| ἀλήμονές | low | "vagabonds": the table avoids it (ἀλήτης row: "vagrants" · avoid "vagabonds") | "…used as a noun: ’vagrants’" |
| ὄλβιον | low | "fortunate, blessed": "blessed" is reserved for μάκαρ and the house word is "prosperous" | "ὄλβιος — prosperous, fortunate; …" |
| ὄνοσαι | low | meaning list lacks "make light of", the rendering the verb has elsewhere in the poem | "ὄνομαι — make light of, scorn, find fault with; …" |
| προτὶ (broaden) | low | entry says tmesis "called in"; the unit note reads it as the adverb ‘besides’ | harmonise: "also adverb ’besides, in addition’, or preverb in tmesis (προτὶ … ἐκάλεσσας)" |
| ἐπικρατέωσιν (broaden) | low | "whenever they have mastery"; the rendering is now "hold sway" (as shipped at 066 line 60) | "’whenever they hold sway’" |
| ἧός | low | existing entry says "accented before the enclitic με"; here it is before μοι, and the sense is "as long as" | broaden: add " · also ’as long as’, accented before the enclitic μοι (ἧός μοι … ζώει)" |
| ἓ | low | "reflexive here with αὐτόν": the convention bars "here" | "reflexive, with αὐτόν: ’himself’" |
| δίοιτο | low | "whatever it chased": the subject is the dog, and ὅττι is the object, not a word it follows | "…in a general relative clause: ’whatever he chased’" |
| ἐφέζετο | low | "augmented": the augment cannot be seen in this compound | drop "augmented" |
| πύρνα | low | lemma "πύρνον … neut." against the shipped entry πύρνος (masc.) for πύρνον | "πύρνος (pl. πύρνα) — wheaten loaf; neut. acc. pl.: ’loaves’", or leave and note the gender inconsistency |
