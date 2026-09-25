# Review — odyssey-013 (Odyssey 3.404–497), pass 1 and pass 2 (translation)

All edits were made to `units.json` by script. Each write asserted that every `t` was unchanged,
and the joined Greek of the 51 units is identical to the draft's. The build's tiling logic
(build_odyssey.py lines 14–41: `ln`, `p`, `l`/`t` line counts, the five-line cap, ending
punctuation, full coverage) was run again as a separate check after the last edit. It passes
with no errors. Unit structure is unchanged. Quotation marks are 2 opening / 2 closing in both
`l` and `i`, so the part is balanced and the validator should give no WARN for them. After
the trims every note is 55–109 words. `new-renderings.md` needed no changes: none of the edits
touch a proposed row.

Totals: **2 error, 3 moderate, 8 minor** (13 changes to 19 fields), plus the findings refused below.

## Changes made

1. **3.411 · `n` · error.** The note called ἐφῖζε "an unaugmented imperfect". This is the
   drafter's known weak spot again. ἵζω has a short ι, and a verb beginning with ι takes the
   augment by lengthening it (LSJ gives the imperfect ἷζον). Murray's circumflex on ῖ marks a
   long vowel, so the form is augmented. Unaugmented, it would be accented ἔφιζε. The metre
   can't decide it, because φι stands before ζ and would be long by position either way, so the
   note rests the point on the accent. Rewritten.
2. **3.477 · `n` · error.** The note called ἐπίθοντο "the unaugmented aorist middle of πείθω".
   The ἐ- is the augment. The aorist stem is πιθ-, and the unaugmented form is πίθοντο. The
   scanner needs that syllable too (κλύον ἠδ’ ἐ|πίθοντο). Rewritten.
3. **3.471 · `l`, `i`, `n` · moderate.** The note derived ὄροντο from ἐπόρνυμαι/ὄρνυμι ("rose
   to a task"), and both layers followed it ("bestirred themselves" / "rose to wait on them").
   LSJ files this line (and Od. 14.104, ἐπὶ δ’ ἀνέρες ἐσθλοὶ ὄρονται) under ὄρομαι 'watch over,
   have charge of'. Cunliffe and Autenrieth do the same as far as I recall them. That makes
   ὄροντο an unaugmented imperfect of ὄρομαι. New `l` "and over them noble men kept watch,";
   new `i` "and noble men waited on them,". The note now gives the ὄρομαι reading, links it to
   οὖρος 'warden' at 411, and still names the ὄρνυμι view.
4. **3.425 · `n` · moderate.** κελέσθω was called "a third-person aorist imperative". κέλομαι
   has no simple thematic or sigmatic aorist in Homer (its aorist is the reduplicated
   ἐκεκλόμην/κέκλετο). κελέσθω is the present imperative, 3 sg. mid. Corrected.
5. **3.437–438 · `l` · moderate.** The note makes ἄγαλμα the object of ἰδοῦσα, which is right.
   But `l` ("so that in the offering the goddess might rejoice, seeing it") attached it to
   κεχάροιτο instead, so `n` and `l` contradicted each other. New `l`: "so that the offering the
   goddess might rejoice to see." `i` already had it right.
6. **3.444 · `n` · minor.** The note said "With all four brothers in their places". Five
   brothers have tasks: Stratius and Echephron (the horns), Aretus (water and barley),
   Thrasymedes (axe), Perseus (bowl). Changed to "all five brothers at their tasks".
7. **3.451 · `n` (unit 450) · minor.** This is the packet's flagged scansion line, and the note
   said nothing about it. Hand scan: θῡγᾰτέ|ρες τε νυ|οί τε ‖ καὶ | αἰδοί|η παρά|κοιτις, that is,
   – ⏑ ⏑ | – ⏑ ⏑ | – ⏑ ⏑ | – – | – ⏑ ⏑ | – ×. The scanner gives the same pattern. The
   irregularity is real: θυγατέρες is four shorts before the -ρες closes, so its first syllable
   has to be lengthened by metrical licence. καί before αἰδοίη is ordinary epic correption, not
   an irregularity. I added one plain sentence saying so. To stay under the length cap I removed
   two routine sentences from the same note ("αἱ is a pronoun …" and "Κλυμένοιο has the
   genitive in -οιο").
8. **3.453–454 · `l` · minor.** `l` used "it" for the heifer at 453 and 454 ("lifted it", "held
   it", "cut its throat"). `i` uses "her" in both units, and so do `l` at 455 ("from her") and
   the rest of the scene. Brought `l` into line: "her".
9. **3.464 · `l` · minor.** The drafter had recast the line in the passive ("Telemachus was
   bathed by beautiful Polycaste") to keep Τηλέμαχον first. That reverses the Greek's voice.
   The odyssey-012 review ruled against the same device at 3.358. New `l`: "Meanwhile beautiful
   Polycaste bathed Telemachus,". In pass 2 I rejected my own first attempt ("Meanwhile
   Telemachus beautiful Polycaste bathed"), because in English it leaves unclear who bathed whom.
10. **3.466 · `n` · minor.** The note said "some ancient readers" took λίπ’ as an elided dative.
    I can't check that attribution. The sole-source lexicons give the elided-case explanation
    as an etymology, not as an ancient reading. Changed to "though it may instead be an elided
    case-form of a noun 'fat' (compare λίπος)". The adverb reading and its hedge stay.
11. **3.490 · `l`, `i`, `n` · minor.** The note said ξείνια here "most likely means food and
    lodging for the night", but both layers said "gifts" ("guest-gifts" / "the gifts due to
    guests"). Lodging also can't be "set beside" anyone (πὰρ … θῆκεν). The layers and the note
    are now neutral and agree with each other. `l` is "the things due to guests", `i` is "the
    hospitality due to guests", and the note says "set 'beside' them, they are most likely the
    meal".
12. **3.496 · `n` (unit 495) · minor.** ἦνον was put under ἀνύω. Autenrieth and Cunliffe (and,
    I believe, LSJ) file it under ἄνω 'accomplish', the by-form of ἀνύω. The note now says
    "the imperfect of ἄνω, a by-form of ἀνύω".
13. **3.496 · `l`, `i` · minor.** `l` "such the pace, for, they carried them onward, the swift
    horses." was hard to read, and its "such the pace" added a noun the Greek doesn't have.
    `i` dropped γάρ. New `l`: "for so well they carried them onward, the swift horses."; new
    `i`: "for so well did the swift horses carry them on." τοῖον is now "so well" in both
    layers, as the note glosses it.

Two notes went over the length band after these edits and were trimmed back: 3.410 (131 → 109
words; I cut "The staff is the sign of a king's authority" and shortened the ὁ μέν gloss) and
3.450 (117 → 100).

## Checked and found correct (no change)

- **Augment labels, all of them.** These "unaugmented" labels are correct: φάνη, ἵζεσκεν
  (iterative), περίχευεν, ἀγέτην, προβάλοντο, λῦσεν, ὀλόλυξαν, σφάξεν, ῥύη, λίπε, καῖε, λεῖβε,
  ἔχον, πάσαντο, μίστυλλον, λοῦσεν, δαίνυνθ’, λάζετο, μάστιξεν (×2), σεῖον, τέκε, ζεύγνυντ’,
  ὑπέκφερον, κλύον. ἔλασαν (493) is also correct: its ε- is the stem's, set against the
  augmented ἤλασεν at 449. These "augmented" statements are correct: εἰργάζετο (εἰ- from ϝ-),
  εἶχε, ὤπτων, ὤπτησαν. The only two false labels were ἐφῖζε and ἐπίθοντο (items 1–2). ὄροντο
  had the right augment label but the wrong verb (item 3).
- **Repeated lines, checked against the live published JSON, not only the packet.** 3.404 and
  3.491 = 2.1 (odyssey-005): `l` "When early-born appeared, rose-fingered Dawn," and `i` "When
  early-born Dawn appeared, rose-fingered," are exact, and 405 follows the shipped 2.2 pattern.
  3.470 = 3.65 (odyssey-009): the first line is exact in both layers. 3.473 = 1.150
  (odyssey-002) = 3.67 (odyssey-009): exact in both layers. 3.474 = 3.417 in this part: `l` and
  `i` are identical apart from the capital letter. The pattern follows 1.28 and 3.68, whose
  τοῖς ἄρα differs from τοῖσι δέ, and the notes say so correctly. 3.487 and 3.497 = 2.388
  (odyssey-008): exact, and 497 correctly ends with a full stop. 3.484 = 3.494: `l` and `i` are
  identical for the line.
- **A mechanical sweep for half-line repeats** (any run of four or more words shared with a
  shipped line) found two that the packet does not list. ὣς ἔφαθ’, οἱ δ’ ἄρα πάντες (3.430) =
  1.381 (odyssey-004): the draft already matches its shipped wording, "So he spoke, and they
  then, all of them," / "So he spoke, and all of them". ἂν δ’ ἄρα Τηλέμαχος (3.481) ~ 2.416
  (odyssey-008): only four words, with a different verb and object; not changed (see refused).
  ἐν δὲ γυνὴ ταμίη (3.479) matches the shipped 2.345 "a woman, a housekeeper" / "a woman, the
  housekeeper", as the note says.
- **Speeches.** Nestor 3.418–429 ("Nestor speaks"): `“` at 418, `”` at 429, and 430 resumes the
  narration with ὣς ἔφαθ’. Nestor 3.475–476 ("Nestor speaks again"): opens and closes there,
  and 477 resumes with ὣς ἔφαθ’. The last units of odyssey-012 (3.393–403) are all narration,
  and the speech from odyssey-012 closed at 3.384, so nothing carries over the seam. No speech
  is left open at 3.497.
- **Cross-references.** Thrasymedes seated beside his father at 3.39 is confirmed in
  odyssey-009 (the unit at 3.36–39, Θρασυμήδεϊ). Poseidon ἀντιόων at 1.25 is confirmed. The
  heifer vowed at 382 and the gilding promised at 384 (χρυσὸν κέρασιν περιχεύας) are
  confirmed in odyssey-012. The shipped wordings the new-renderings rows cite are confirmed: "thigh-pieces"
  and "tasted the entrails" (3.9), "robe" for Penelope's φᾶρος (2.97), "in body" (2.268),
  "inlaid" (1.132), "forecourt" (1.103, 1.119), and ὠκύμοροι (1.266).
- **Stock epithets, against the table.** Γερήνιος ἱππότα Νέστωρ (405, 417, 474), ἀντίθεος,
  μεγάθυμος, δῖος, αἴθοπα οἶνον, κατὰ μοῖραν (`l` "according to what is fitting" / `i` "as is
  fitting"), ὄρχαμος ἀνδρῶν (454, 482), ποιμένα λαῶν, ἥρως, θοή + ἐίση, νῆα μέλαιναν,
  αἰθούσης ἐριδούπου, ἀγακλυτά, ἀγλαόν, ὁ γέρων, and αἰδοίη "revered" (which also matches the
  shipped αἰδοίῃ παρακοίτι at 3.381) are all exact.
- **Proper names.** Echephron, Stratius, Aretus, Laerces, Polycaste, Eurydice, Pherae, Diocles,
  Ortilochus, Alpheus and Clymenus appear nowhere in the shipped parts or in conventions.md, so
  there is no collision. Every shipped hit for "Perseus" is edition metadata ("Perseus TEI"),
  not a name. Peisistratus, Thrasymedes and Neleus match their shipped spellings. These are the
  ordinary English forms.
- **Segmentation.** The two comma cuts are legal. 404–408 is a five-line sentence, cut after
  405. 430–435 is a six-line sentence, cut at the end of 432. Every other unit ends at `.`,
  `;` or `·`.
- **No bowdlerizing.** The stunning blow, the throat-cutting, "the black blood had flowed out
  of her", the cutting up, the burning and the spitting are all rendered plainly.

## Findings considered and refused

- **"swift" for both θοός and ὠκύς.** Kept. The table already uses "swift" for three Greek
  words: θοός ("swift ship"), ὠκύ- in the shipped ὠκύμοροι "swift-doomed", and ἀργοί ("swift
  dogs"). Splitting ὠκύς now would leave ὠκύμοροι as the one exception, and a shipped formula
  can't be changed. The new-renderings row says this openly. The owner may want to decide for
  the whole table whether "swift" should be reserved (see the report).
- **πρέσβα "eldest".** The hedge is accurate and well pitched. LSJ lists this line under the
  sense 'eldest' with the partitive genitive, and the note keeps 'august / first in rank' open.
- **ἀμνίον.** "Occurs only here in Homer" is true. The note ties the meaning to ancient
  explanation, which is the right level of caution.
- **πείρατα τέχνης.** LSJ itself explains the phrase as the tools that complete the craft.
  `l` keeps the literal "ends of his craft", `i` gives the lexicon's sense, and the note states
  the doubt. That is adequate.
- **ἀλείφατος.** The hedge (actually oiled, or only shining as if oiled) is accurate. Both
  layers say "glistening with oil", which the genitive supports on either reading.
- **λίπ’.** The adverb reading is kept. Only the unverifiable attribution was changed (item 10).
- **3.418 `l` "so that, first of the gods, I may propitiate Athena".** In English this could
  be read as Nestor calling himself "first of the gods". `i` removes the ambiguity, and the
  word order follows the Greek. Left as it is.
- **3.439 note, "two brothers, a horn each".** This is an inference, not a claim about the
  text, and it is harmless. Kept.
- **3.464 note, "ordinary hospitality, not a sign of anything more".** It is a cultural
  statement about this scene, not a claim about the rest of the poem. Kept.
- **3.481 ἂν δ’ ἄρα Τηλέμαχος (~2.416).** Only four words, and the verb and object differ. The
  draft's "And up then Telemachus" already follows 2.416's order. No forced alignment.
- **3.432 `i` "the means that bring his craft to completion".** It reads more into the phrase
  than `l` does, but it is the lexicon's own gloss, and the note carries the doubt. Kept.
- **3.430 note** doesn't mention the 1.381 half-line repeat. The wording already matches, so
  nothing depends on it. Not added, to keep the note's length.
- **Apostrophes.** Notes use ASCII ' for possessives and gloss quotes, as the shipped
  odyssey-012 does. This is left to the open QUESTIONS.md item on the house apostrophe rule.
