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

## Pass 2 (glossary)

I checked all 213 novel entries and all 11 `__broaden__` entries in `gloss.json`. Each one was
checked against every line where its form occurs in the final `units.json`. The occurrences were
found by script with the reader's own tokenizer (`odyssey_lib.forms`). The edits were also made by
script: load the file, change the named keys, and write it back with the same `indent=1` layout.
After the write, every entry passes these checks:
- no ASCII ' or backtick, and every entry is 230 characters or fewer;
- `<lemma> — <text>` shape (the build's regex);
- no novel key already exists in `odyssey-glossary.json`;
- every `__broaden__` value starts with the exact shipped text followed by ` · `. This was checked
  character for character by `startswith`. All 11 of the Glosser's broadenings passed.

Every form in the part has a shipped entry or a new one. `units.json` was not changed, because no
note contradicts the corrected glossary.

I also read the shipped entries of all the other forms in this part against their lines. That
produced 4 new broadenings.

Totals: **0 error, 0 major, 16 moderate, 36 minor.** 48 novel entries were rewritten and 4
broadenings added (λαῶν, αἰπὺ, κεχάροιτο, ἴτω). The Glosser's 11 broadenings were kept unchanged.

### Changes made — moderate

1. **ἔσχον · augment.** The entry said "unaugmented". ἔσχον is ἐ- plus the aorist stem σχ-, so it
   is augmented. It is now "aor. 3 pl. (or 1 sg.), augmented".
2. **ἐκάλυψαν · augment.** The entry said "unaugmented". The ἐ- is the augment (the unaugmented
   form is κάλυψαν). Fixed. The tmesis note (= κατεκάλυψαν) is kept.
3. **ἐκάη · augment.** The entry said "unaugmented". ἐκάη is augmented (the unaugmented form is
   κάη). Fixed, and the tmesis is given as κατεκάη.
4. **ἔβαινον · augment.** The entry said "unaugmented". ἔβαινον is augmented. Fixed.
5. **λιπέτω · augment.** An imperative was labelled "unaugmented". Only the indicative takes the
   augment, so the label implies a contrast that cannot exist. Removed.
6. **μέλαν · case.** The entry said "neut. acc. sg., agreeing with αἷμα". In 455, μέλαν αἷμα is the
   subject of ῥύη. It is now "neut. nom./acc. sg.", and the pinned agreement is dropped.
7. **ὑφ · construction.** The entry said "+ acc." That fits 476 (ὑφ’ ἅρματ’), but 478 has
   ὑφ’ ἅρμασιν with the dative. It is now "+ gen., dat. or acc."
8. **χαλκήια · construction and sense.** The entry said "used substantively: ’bronze tools’". At 433
   the word is attributive to ὅπλ’ (ὅπλ’ … χαλκήια), not substantive. LSJ's sense is "of a smith"
   (it cites this line). It is now "of a smith, a smith’s; of bronze; neut. nom./acc. pl."
9. **οἷσίν · gender and homograph.** The entry said "neut. dat. pl." The antecedents at 434 are
   ἄκμονα (masc.), σφῦραν and πυράγρην (fem.), and ὅπλα (neut.), so the form is "masc./neut. dat.
   pl.". I also added the possessive homograph (οἷσι ’to his own’), as the shipped οἷς has it.
10. **ἄεσαν · lemma.** The entry gave "ἄημι/ἰαύω (root ἀεσ-)". ἄημι ’blow’ is a different verb, and
    this also contradicts the shipped ἀέσαμεν ("ἀέσαι (root ἀϝεσ-, distinct from ἄημι ’blow’)").
    The entry now follows the shipped lemma, "prob. akin to ἰαύω ’sleep’".
11. **ἐλάαν · Attic equivalent.** The entry said "= Attic ἐλᾶν". But Attic ἐλᾶν is the future
    infinitive. ἐλάαν is the present infinitive of the by-form ἐλάω, with the vowel stretched out
    from contracted ἐλᾶν. The Attic present infinitive is ἐλαύνειν. The entry now says this, which
    matches the 494 note.
12. **ἵζεσκεν · false Attic.** The entry said "(= Attic ἵζεσκε)". Attic has no iterative forms; this
    only removed the movable ν. The entry now says: iterative, unaugmented, "as iteratives usually
    are". This matches the 408 note.
13. **ἐχέφρων · missed homograph.** The key is lowercased, so it also serves the common adjective
    ἐχέφρων ’sensible, prudent’ (e.g. 13.332). I added it with " · ".
14. **πρέσβα · sense and construction.** See the ruling below.
15. **οἰσέμεν · tense.** The entry said "epic fut. inf." without any hedge. Monro and LSJ class the
    form with the mixed aorist (imper. οἶσε). It is now "built on οἰσ- (the stem of fut. οἴσω),
    usu. classed with the mixed aor." This still matches the 427 note.
16. **κεχάροιτο · new broadening.** The shipped entry says "perf. opt. …, potential". At 438 the
    form is in a purpose clause with ἵνα after a past tense, and the 437 note calls it a
    reduplicated aorist optative. I added "also in a purpose clause after a past tense, ’might
    rejoice’ …; usu. classed as a reduplicated aor. mid. opt." The shipped "perf." cannot be
    removed; see the QUESTIONS.md items at the end.

### Changes made — minor (36)

- **Parses made general to the form**, where the entry had given only the case or gender of this
  passage's occurrence:
  - τέκνα: nom./voc./acc.
  - ἐέλδωρ, πεδίον, ἅρματα: nom./acc.
  - ἐναργὴς, ἐυποίητόν, ἐριδούπου: masc./fem., since these adjectives have two terminations.
  - πυρηφόρον
  - μένετ, εἴπατε: imperative, or indicative.
  - ἱλάσσομ: also the future indicative.
  - σφ: elided σφ’ can stand for σφι or σφε.
- **Tense label added:** "aor." for ἔλθῃσιν, "pres." for πρήσσῃσιν.
- **Passage-pinned wording removed:**
  - "here": ἤλασεν, ἀνά, κατά.
  - "his": εὐνῆφι, ἑτέρῃ.
  - "after ὄφρα": ἔλθῃσιν.
- **Lemmas brought to LSJ headwords:**
  - ἄϊδόσδε: ᾍδης (epic Ἀΐδης). The Glosser had "Ἅιδης".
  - πυράγρην: πυράγρα (epic -η).
  - κνίσῃ: κνῖσα (epic κνίση).
  - ξείνια: ξείνιος, with τὰ ξείνια as a noun.
  - τἆλλα: the lemma field had held "crasis of …".
  - ἔδουσι: ἐσθίω, from ἔδω, matching the shipped ἔδουσιν.
- **βήσετο:** The gloss ’mounted’ belongs to ἀνά. The form alone is ’went’, and it is
  unaugmented. Added.
- **ἤλασεν:** "augmented" added. **ἦνον:** "augmented" and "not the adv. ἄνω" added.
- **ὄροντο:** Added the ὄρνυμι alternative that the 471 note mentions.
- **Hedges:**
  - ἀμνίον: "sense from ancient explanation", as in the 444 note.
  - λίπ: "perh. … noun ’fat’". The elision equation was missing and is now there.
- **δίπτυχα:** "used adverbially" changed to predicative with ποιέω.
- **χερσί:** "before a pause" was a false reason for the missing ν (it is metrical). Changed to
  "(without movable ν)".
- **περσεὺς:** Dropped "(grave accent, not in pause)". The house convention for accent-doublet
  keys is identical entries (ζεύς/ζεὺς, ὀδυσσεύς/ὀδυσσεὺς, δέ/δὲ).
- **New broadenings:**
  - λαῶν: the shipped entry was pinned to ἄνασσε; this part has ποιμένα λαῶν.
  - αἰπὺ: the shipped entry was pinned to ὄρος; this part has αἰπὺ πτολίεθρον.
  - ἴτω: the shipped entry has only ’let her go’; at 421 the subject is a man.

### The Glosser's flagged items: rulings

- **πρέσβα.** One word, one lemma: the poetic feminine of πρέσβυς. So a " · " split would be
  artificial. But the entry was too narrow. It left out the main Homeric use, ’august, revered’ as
  a title (Ἥρη πρέσβα θεά), and it built "+ partitive gen." into the parse, though most uses have no
  genitive. It is now "eldest, first in rank; august, revered (a title of honour, as of goddesses);
  fem. nom./voc. sg.; with partitive gen. ’eldest of’". That matches the 450 note's hedge.
- **ἦνον.** The mapping is correct. LSJ ἄνω (A) ’accomplish’ = ἀνύω, impf. ἦνον, citing this line.
  I added "augmented" (ἀ- to ἠ-) and a warning against the adverb ἄνω ’up’.
- **ἀκροπόρους.** No change. LSJ gives ’piercing with the point’ for this line without a query, so
  the entry does not overclaim, and it matches the 461 note.
- **ἄεσαν.** The root identification was wrong: it used ἄημι. Fixed; see moderate 10.
- **περικαλλέα.** Left unbroadened. The shipped entry is 223 characters. The shortest honest
  addition, " · masc. acc. sg.", would reach 240. A bare " · masc" (230) would read like a
  typo. The label does not mislead about the form: περικαλλής has two terminations, so the masc.
  and fem. acc. sg. are spelled identically, and the 481 note makes no gender claim. The only
  error is an incomplete label. This is low severity and goes to QUESTIONS.md with the other
  entries blocked by the character cap.
- **Accent-doublet proper names.** The convention is confirmed: separate keys with the same entry
  (ζεύς/ζεὺς, ὀδυσσεύς/ὀδυσσεὺς, ἀχαιοί/ἀχαιοὶ). The keys match the `t` text exactly: περσεύς
  (414, acute before τ’), περσεὺς (444, grave), ἄρητός (414, extra acute before τε), ἄρητος (440).
  I kept ἄρητός's note "(acute added before the enclitic τε)", because the second acute is unusual
  enough to need saying (the same precedent as the shipped τί and ὅ). I removed περσεὺς's grave
  note (minor list).

### Augment labels checked, no change needed

These labels were checked by hand and are correct:
- **Unaugmented:** περίχευεν, ἀγέτην, προβάλοντο, ὀλόλυξαν, σφάξεν, ῥύη, λίπε,
  τάμνον, καῖε, λεῖβε, μίστυλλον, λοῦσεν/λοῦσέν, βάλεν, δαίνυνθ’, λάζετο, μάστιξεν, πετέσθην,
  λιπέτην, σεῖον, ζεύγνυντ’, ἔλασαν (the ἐ- is the stem; augmented would be ἤλασαν), ὑπέκφερον,
  κλύον, ἔχεν.
- **Augmented:** εἰργάζετο (εἰ- from ϝ), εἶχε, ἐπίθοντο, ἔθηκεν, ἐφῖζε. For ἐφῖζε, the circumflex
  shows ῑ from the augment of ἵζω, whose ι is short.

### For QUESTIONS.md (not fixed here, because shipped entries are additions-only)

- **περικαλλέα:** "fem. acc. sg." with no masc. label, used at 481 with masculine δίφρον. A
  broadening is blocked by the 230-character cap (see above).
- **κεχάροιτο:** The shipped entry says "perf. opt. …, potential". The form is usually classed as a
  reduplicated aorist, and the potential sense is not general to the form. It is broadened, but
  the old wrong label stays.
- **κατεβήσετο** (shipped, not in this part): labelled "unaugmented (= κατέβη)". κατ-ε-βήσετο is
  augmented. This is the same error class as moderate 1–4.
- **σκιόωντό** (shipped): the lemma is σκιάω but the entry has "= Attic ἐσκιοῦντο". The 487 note
  correctly has ἐσκιῶντο.
- **χερσὶ** (shipped): "epic -σί (= Attic χερσίν)". χερσί is equally Attic; the only difference is
  the movable ν.
