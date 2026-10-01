# odyssey-050 (10.475–574) — review

Two passes. Pass 1: notes, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks, flagged lines.
Pass 2: re-read of the edited units, then every parse in `gloss.json` against its line, then
`new-renderings.md` against the table's format and the units. `t` was never touched. Checked by script:
the units' `t` joined reproduce the edition (sha matches), `l` line counts match `t`, no `\n` in `i`,
`ln` of every unit is the line it starts on, `p` flags equal Murray's ¶ lines (after the fix below),
whole-unit repeats of published units (476, 487, 503, 568) carry identical `l` and `i`, no ASCII quotes
in `l`/`i`, units.json and gloss.json parse. `validate_odyssey.py` was not run: it opens the built
`odyssey-050.json`, which does not exist before the build.

## Changes

Format: line · field · severity · what was wrong · what was done.

1. 562 · `p` · medium · the unit carried `p: true`, but Murray's paragraph breaks in this stretch are at 561 and 566, not 562 (562 starts a speech inside the 561 paragraph, which `mark` already covers) · removed `p`.
2. 475 · `n` · medium · "ἔφαν is the plural of ἔφη, with no augment": false, ἔφαν has the augment (ἔ-φα-ν) · now "the third plural imperfect of φημί ‘say’ (Attic ἔφασαν)".
3. 483 · `n` · medium · πεμψέμεναι labelled as an infinitive with Attic equivalent πέμψαι; it is the future infinitive (Attic πέμψειν), as the glossary already says · fixed.
4. 485 · `i` · low · "and those of my other companions" after "my heart" (singular θυμός); `l` has "that" · "that of my other companions".
5. 490, 531, 563 · `l`, `i`, `n` · medium · ἐπαινή rendered "dread", but "dread" is reserved for δεινός in the table (rows for αἰνὰ πέλωρα and ἔκπαγλος say so; δεινὴ θεός, δεινὸν πέλωρ use it), and the note called the word "dread" without saying its sense is uncertain · "grim" in `l` and `i` at all three occurrences (490 Persephone, 531, 563); note at 490 now says ‘rendered “grim”: traditionally “dread, awful”, exact sense not certain’; 531 note adjusted; `new-renderings.md` row changed to match.
6. 490 · `n` · low · packet flag for 493 (AMBIGUOUS). Hand scan: μάν-τη | ος ἀ-λα | οῦ τοῦ | τε φρέ-νες | ἔμ-πε-δοί | εἰ-σι. It scans only if the final short syllable of μάντηος (ος) is made long as the longum of foot 2 before ἀλαοῦ; οἱ of ἔμπεδοί is short by ordinary correption. The irregularity is real · added one sentence: "The line is metrically irregular as transmitted: the final short syllable of μάντηος is treated as long at the start of the second foot, before ἀλαοῦ."
7. 494 · `l` · low · καί of τῷ καὶ τεθνηῶτι ("even") left out of `l` (it was in `i`) · "to him, even dead,".
8. 494 · `n` · medium · πεπνῦσθαι called "the perfect infinitive of a verb related to πεπνυμένος"; it is the perfect infinitive of πέπνυμαι itself, of which πεπνυμένος is the participle · fixed.
9. 507 · `i` · low · "will carry her" after "…and sit;" has no antecedent in the prose (the ship was last named in the previous unit's "by the ship") · "will carry the ship for you".
10. 516 · `i` · low · "about a cubit long on each side": "about" hedges a measure the Greek states (ὅσον τε πυγούσιον), and "each side" implies a square pit; the Greek is ἔνθα καὶ ἔνθα "this way and that" · "a cubit long in each direction".
11. 521 · `i` · low · "fill the pyre" where `l` and the Greek (πυρήν, no article, first mention) have "a pyre" · "a pyre".
12. 546 · `n` · low · "dative plurals of μείλιχος": the adjective in the line is μειλίχιος · fixed.
13. 550 · `i`, `n` · medium · drafter's flagged conflict, "So I said" in `i` and note. The shipped plain ὣς ἐφάμην lines (odyssey-041, 042, 044, 045, 047, 048, 049) are all "So I spoke"; "So I said" in `i` belongs only to the two fixed reply formulas (487 and 503 here, shipped in odyssey-017, whole-unit repeats the validator enforces). 550 is a plain line · "So I spoke" in `i`, note "so I spoke".
14. 566 · `i` · medium · same conflict; the published unit containing this exact line (odyssey-047, 198) has "So I spoke", and the packet says to reuse the published wording for a repeated line inside a longer unit · "So I spoke".
15. 556 · `l`, `n` · medium · `l` "when his companions were stirring" and the note's "as his companions stirred" turned κινυμένων ἑτάρων into a temporal clause; it is a genitive depending on ὅμαδον καὶ δοῦπον (sound of companions stirring) · `l` "of his companions stirring, the din and the clatter hearing,"; note rewritten as a genitive plural participle of κινύομαι (the glossary's lemma). `i` was already right.
16. 556 · `n` · low · packet flag for 559 (UNRESOLVED). Hand scan: ἀλ-λὰ-κα | ταν-τι | κρὺ-τέ-γε | ος-πέ-σεν | ἐκ-δέ-οἱ | αὐ-χήν. No regular fit: the υ of καταντικρύ must be long as the longum of foot 3 (and the second foot is spondaic on ταν-τι), οἱ is shortened by correption. The irregularity is real. The irregular word stands in this unit (the line is split between this unit and the next) · added one sentence: "Line 559 is metrically irregular as transmitted: καταντικρύ fits the hexameter only if its last syllable is lengthened, at the start of the third foot."
17. 568 · `n` · medium · "ἀλλ’ οὐ γάρ τις is ‘but there was none’, the ἀλλὰ … γάρ idiom with the second clause giving the reason for the first": wrong (there is no first clause), and it contradicts the note on this very line already shipped in odyssey-047 · note now follows the shipped one: "‘but (it did no good), for …’; the thought the Greek leaves out is that weeping was useless".
18. 571 · `i` · low · "slipping easily past us": "slipping" is imagery the Greek does not have (ῥεῖα παρεξελθοῦσα is "easily passing by") and reads as remembered English · "passing easily by".
19. gloss `μελικρήτῳ` · medium · "honey-and-water mixture"; LSJ and the unit-23 note have honey and milk · "mixture of honey and milk (traditional gloss)".
20. gloss `ἔμπεδοί` · low · "masc. nom. pl." although it agrees with fem. φρένες (two-ending adjective) · "masc./fem. nom. pl. (here with fem. φρένες)".
21. `new-renderings.md` · row ὣς ἐφάμην · medium · the row said `i` "So I said" for the plain line and also that 566 "was shipped as ‘So I spoke’" yet kept "So I said", contradicting the shipped parts and itself; its "avoided" cell was not an avoided-list · rewritten in the table's format: plain lines "So I spoke" / "So I spoke"; the two shipped formula lines keep "So I said".
22. `new-renderings.md` · row ἐπαινή · medium · see 5 · "grim" / "grim", with "dread" listed as avoided (reserved for δεινός).
23. `new-renderings.md` · two rows added · low · whole-line formulas 541 (ὣς ἔφατ’, αὐτίκα δὲ χρυσόθρονος ἤλυθεν Ἠώς) and 561 (ἐρχομένοισι δὲ τοῖσιν ἐγὼ μετὰ μῦθον ἔειπον) are new, plainly formulaic and were not listed · rows added with the English the units already carry.

## Considered and refused (or left for the owner)

- **482, ἔπεα πτερόεντα προσηύδων: kept "winged words I addressed to her" / "I spoke to her and addressed her with winged words".** The table row for προσηύδα says "winged words he spoke" / "spoke winged words", and row 888 says προσηύδων keeps "spoke", and the shipped 042–049 follow it. But the exact line 10.482 already stands in odyssey-019 (548) as "addressed", and the exact-repeat rule (first ratified rendering wins; the packet's "reuse the published wording for that line"; table row 366 applies the same rule over its own table) decides for the published wording. The unit is not a whole-unit repeat, so the validator would accept either; I followed the repeat rule for consistency with published parts. The deviation sits in odyssey-019 and should be fixed there, if at all (it also uses "addressed", which the table reserves for προσέειπε / προσέφη).
- **heart(s) / spirit(s): no change.** θυμὸς ἀγήνωρ keeps "spirit" (row 278; 475, 550), plain θυμός is "heart" (483–484), ἦτορ and κῆρ are "heart" (496, 566, 485, 497). The plural "spirits" at 550 and "hearts" at 566 are the distributive singular, as row 295 and the shipped 047 (198) do, and the 550 note says so.
- **Unit boundaries at 484 and 520 (not fixed, `t` is locked).** Line 484 has an ano teleia after πεμψέμεναι· and unit 5 instead ends at the comma after ἤδη, although the sentence (483–486) is only four lines; line 520 has one after ὕδατι· inside unit 23, which therefore ends past an ano teleia. The convention says a unit ends at an ano teleia. Correct cuts would be after "πεμψέμεναι·" and after "ὕδατι·" (the next units then start mid-line). Splitting changes `t`, which I was told not to touch; ten such units already exist in the shipped parts and the validator does not check it. Left for the owner.
- **ἐπεπείθετο:** the note says "imperfect middle", the shipped glossary entry says "plpf. 3 sg. with impf. sense". Same sense; the entry stands (first entry wins), note left.
- **ἐπέφραδε:** lemma ἐπιφράζω in the shipped entry versus the reduplicated aorist of φράζω; shipped entry stands, not a wrong parse.
- **κινυμένων:** lemma κινύομαι (glossary) kept in the note; I could not confirm κίνυμαι against LSJ from memory, so the two now agree on the glossary's form.
- **ἀμείβετο "with no augment" (487, 503):** true for ἀμείβετο (Attic ἠμείβετο); left.
- **Shipped glosses with line-pinned wording** (ὁπότ’ "here introducing a vivid simile", ἐρίδουπος "loud-crashing" against the house "loud-echoing"): not wrong parses; additions-only rule, left. The gloss for ἐπαινός keeps "dread, awful (traditional gloss)" because a gloss is the dictionary sense, not the house rendering.
- **Quotation marks:** six speeches (483–486, 488–495, 501–502, 504–540, 548–549, 562–565), each opened with ‘ and `mark` on its first unit, each closed with ’ on its last unit; no outer double marks needed (the 9.2 speech stays open); the crew's speech that opens 049 closes in 049. No change.
- **i 494 "so that he alone has understanding" for οἴῳ πεπνῦσθαι, i 521 "many times over" for πολλά, i 14 "us" after ἡγεμονεύσει:** within the licence of `i`, left.
- **Published repeats:** 476–477, 487, 503, 568 whole-unit repeats match exactly; 539–540, 543–544, 547 reuse the published line English.

## Severity count

high 0 · medium 12 · low 11 (rows 1–23 above; row 5 counted once for its three occurrences)
