# Review: odyssey-005 (Odyssey 2.1–102)

Reviewed against `conventions.md`, `packet.md`, `new-renderings.md`, `known-forms.json` and the last
three units of the published `odyssey-004.json`. I checked all 64 units by script for structure
(t-reconstruction against packet, `\n` parity between `t` and `l`, paragraph marks, quotation marks) and then
read each one line by line for grammar, line positions, cross-references, `l`/`i` agreement and formulas.
I checked all 299 novel glossary entries and 9 `__broaden__` entries against the Greek of each line.
**19 units edited** (25 field changes). **17 novel gloss entries corrected**, **5 broadenings corrected**
and **3 broadenings added**. No `t` field was touched, and the concatenated `t` still reproduces packet.md
exactly.

## Pass 1: changes to `units.json`

1. **2.28–29 (τίνα χρειὼ τόσον ἵκει) · `l`, `i`, `n` · major.** The draft read τίνα as agreeing with
   χρειώ ("What need so great has come upon him"). That is impossible. τίνα is accusative and χρειώ is
   nominative, the subject of ἵκει. The Greek asks "*whom* has so great a need come upon?", and the
   partitive genitives νέων ἀνδρῶν / οἳ προγενέστεροι depend on τίνα ("whom, of the young or the
   older?"). The draft's "him" had no Greek source. I rewrote `l` as "Whom has need so great come upon, /
   either of the young men or of those who are older?", rebuilt `i` to match, and rewrote the note to
   parse τίνα as the object. With this fix, 2.41 (μάλιστα δέ μ’ ἄλγος ἱκάνει, "upon *me*") answers the
   question more exactly. The gloss entry for χρειὼ, which carried the same misreading, is fixed too (Pass 2).

2. **2.48–49 · `n` · moderate (line-position claim).** "πάγχυ and πάμπαν … stand one in each line" is
   false. Both are in line 49 (πάγχυ διαρραίσει, … ἀπὸ πάμπαν ὀλέσσει). Changed to "one in each clause of
   line 49".

3. **2.50 · `n` · moderate (augment).** ἐπέχραον was called "the unaugmented aorist". It is augmented:
   ἐπ-έ-χραον, and the unaugmented form would be ἐπίχραον. Corrected. The gloss had the same error.

4. **2.19–20 · `n`, `l` · moderate (augment) + minor.** ἔκτανε was called "the unaugmented aorist of
   κτείνω". The ἐ- is the augment, and Homer's unaugmented form is κτάνε. Corrected. The `l` "and made him
   the last supper he readied" duplicated the verb ("made … readied"). Reworded to "and as his last supper
   made him ready", which keeps πύματον … ὡπλίσσατο δόρπον in order.

5. **2.94 · `n` · minor (augment).** ὕφαινε was called "the unaugmented imperfect". An augment on initial
   ῠ- only lengthens the vowel and cannot be seen in writing, so the claim cannot be made. Changed to "the
   imperfect … (an augment on initial υ- would not show in writing)". Fixed in the gloss as well.

6. **2.24, 2.39 · `n` · minor (form mislabel).** μετέειπε and προσέειπεν were said to have "the vowel
   stretched out", which is the language of diectasis. They are augmented forms with the augment left
   uncontracted: ἐ- + εἰπ-, where Attic has contracted μετεῖπε / προσεῖπε. Corrected both. The published
   known-forms entry for προσέειπε already says "epic uncontracted", so the notes now agree with it.

7. **2.85 · `n` · moderate.** The note equated ἄσχετος with ἀνάσχετος. They mean opposite things. ἄσχετος
   is ἀ- privative + σχετός, "not to be held back". ἀν(α)σχετός means "bearable", and it is the word the note
   at 2.63 correctly explains for ἀνσχετά. Corrected the note and cross-referred to line 63 to keep them
   apart. In the same note, "ἔειπες … with an epic prefixed ἐ-" now says it is the augment left uncontracted.

8. **2.64–66 · `n` · minor.** περιναιετάουσι was said to have "the vowel stretched out" (diectasis). It is
   simply uncontracted (-άουσι for Attic -ῶσι); a diectasis form would be -όωσι. Corrected. The gloss had
   the same error.

9. **2.89 · `n` · minor.** "εἶσι is the future of εἶμι". εἶσι is the present of εἶμι with future sense,
   which is what the gloss entry says. Aligned the note with the gloss.

10. **2.58 (τὰ δὲ πολλὰ κατάνεται) · `n` · minor.** "The three words stand between…". There are four
    words. Corrected.

11. **2.58–59 · `n` · minor.** "ἀπὸ … ἀμῦναι is 'ward off from'" presented ἀπό as a preverb in tmesis. In
    ἀρὴν ἀπὸ οἴκου ἀμῦναι, ἀπό stands directly before and governs οἴκου as an ordinary preposition. Rewrote
    the note as "ἀπὸ οἴκου 'from the house' … ἀμῦναι … gives the purpose". The same bad example was removed
    from the ἀπὸ broadening (Pass 2).

12. **2.52–54 · `l`, `i`, `n` · minor.** "who came to him with favour" is ambiguous in English. It could mean
    bringing favour, and it did not match the note's (correct) gloss of κεχαρισμένος as "welcome, pleasing".
    Changed both layers to "who came to him welcome". I also trimmed the note from 124 to 109 words.

13. **2.42–44 · `i` · minor.** The note says the English echo of 2.30–32 is deliberately identical except
    for the persons. `i` at 43 had "having learned of it first", but 31 has "since he learned of it first".
    Changed to "since I learned of it first" so that the echo holds.

14. **2.60–61 · `i` · minor (mood).** ἐσόμεσθα is a future indicative, and `l` correctly has "we shall be".
    `i` had "we should prove feeble", which is conditional in mood. Changed to "we shall prove feeble".

15. **2.62 · `l` · minor (`l`/`i`/`n` disagreement).** The note and `i` take ἀμυναίμην as middle, "defend
    myself", but `l` had "ward it off". Changed `l` to "Truly I would defend myself".

16. **2.96 · `mark` · minor.** Penelope's quoted words (2.96–102) are a speech. The convention puts a `mark`
    "at the first unit of every speech". Added `mark: "Antinous quotes Penelope"` and shortened the note's
    now-redundant opening sentence (114 → 107 words).

17. **2.1, 2.99 · `n` · minor (length).** These notes were 128 and 126 words, over the 25–110 band.
    Trimmed them to 106 and 105 words without dropping any grammatical point. In 2.1 I also removed "in this
    formulaic line" and the "usually taken to be" gloss on the dawn image. In 2.99 I removed "Odysseus'
    father", which this part cannot show, and added "μιν is 'him', Laertes" to make the referent explicit
    for the quotation question below.

## Pass 1: verified and confirmed without change

- **Penelope's inner quote closing at 2.102 (confirmed).** In 99–102 μιν (99) is the object of καθέλῃσι
  and must be Laertes, the one the shroud is for. κτεατίσσας (102) is masculine nominative singular, so the
  subject of κεῖται is Laertes ("if *he* should lie without a winding-sheet, having won much"), not
  Penelope. Line 102 is the protasis to νεμεσήσῃ (101), so it is still Penelope's sentence. Her speech ends
  at the end of this part, and the next part begins at a Murray paragraph break (parts are cut only there),
  so the drafter's reasoning holds. The closing ’ at 102 is correct, and Antinous' outer “ correctly stays
  open into odyssey-006.
- **No speech carries in from odyssey-004 (confirmed).** Its last three units (1.438, 1.439–442, 1.443–444)
  are narrative: Eurycleia leaving the chamber, and Telemachus lying awake. There are no open quotation
  marks. 2.1 is a new dawn.
- **Quotation marks.** Aegyptius “25 … ”33–34, Telemachus “40 … ”79, Antinous “85 (open), Penelope ‘96 …
  ’102, identical in `l` and `i`. There are no stray marks on intervening units.
- **Paragraphs.** `p: true` is on exactly 1, 25, 35, 40, 80, 85, 96, and on nothing else.
- **Scansion flags.** packet.md says "none", confirmed. No line needed a hand scan.
- **Cross-references inside the part** were all checked against packet.md and are accurate. Examples:
  line 5 βῆ δ’ ἴμεν; 8–9 ἀγείρω forms; 14 θώκῳ / 26 θόωκος; 18 νηυσίν / 27 νηυσί; 2 = 35 line-end
  Ὀδυσσῆος φίλος υἱός; 28 ἤγειρε / 41 ἤγειρα; 30–32 / 42–44; 34 / 36 / 92 μενοινάω; 37–38 staff; 41 λαόν;
  24 / 95 μετέειπε; 64 / 101 νεμεσ-; 86 ἡμέας, 95 ἡμῖν; 19 Ἄντιφος at the head of the line; 46 δοιά at the
  head of the line; 58 μαψιδίως at the head of the line; 83 χαλεποῖσιν at line-end.
- **Comma cuts** (2.1–3, 42–44, 50–51, 70–71, 96–98). Each sentence really runs past four lines (5, 5, 5, 5
  and 6 lines), and each cut is at a real syntactic pause.
- **Article-pronoun labelling** is correct throughout: οἱ/τοί 8, τῷ γε 11–12, τόν 13, 19, τοῖσι 15, τοῦ
  17, 23, 24, ὁ μέν 21, τό μέν 46, τῶν 51, ἡ δέ 93. **Possessive vs relative** is also correct: ᾗσι 34
  possessive; ὅς 16, 46 relative; ὅ 45 (= ὅτι); ὅ 48 relative; ᾧ 54 relative.
- **House renderings, each checked at every occurrence:** κάρη κομόωντας Ἀχαιούς (7) · ἀντίθεος
  "godlike" (17) · κοίλῃς ἐνὶ νηυσί(ν) (18, 27; `l` identical, "in hollow ships") · ἐν σπῆι γλαφυρῷ "in
  his hollow cave" (20, the singular of the table's plural) · δῖος "heavenly" (27, 96) · πεπνυμένα
  "prudent" (38) · μνηστῆρες plain "suitors".
- **new-renderings.md.** Each entry is used identically wherever its phrase occurs: ὣς φάτο "So he spoke"
  (35, 80); ἥρως "the hero" (15, 99); Ὀδυσσῆος φίλος υἱός (2, 35); βῆ δ’ / ῥ’ ἴμεν "set out to go" (5, 10);
  αἴθοπα οἶνον "the fire-faced wine"; ἐυκνήμιδας "well-greaved"; τανηλεγέος "that lays-at-length", with
  the unknown meaning stated.
- **"Remembered English".** I found no phrase in `i` that reads as lifted from a published translation.
  The avoided forms listed in new-renderings.md ("rosy-fingered", "wine-dark"-type calques) are in fact
  avoided.

## Pass 1: findings considered and refused

- **ASCII apostrophes / straight single quotes in `l`, `i`, `n`.** Throughout this part, possessives
  ("Odysseus' dear son") and glosses inside notes use ASCII `'`. odyssey-004 was normalised to ’, but
  odyssey-001 to 003 as published use ASCII `'` in exactly this way (hundreds of instances). The validator
  forbids ASCII only in `t` and in glossary entries. I left them alone because house practice is split and
  this is not a translation error. **For QUESTIONS.md:** should notes and layers be normalised to ’
  corpus-wide?
- **κοίλῃς ἐνὶ νηυσί at 2.27, `i` "in *his* hollow ships"** (the table's `i` is "in their hollow ships").
  `l` is the table's wording exactly. The only subject in 27 is Odysseus, and the pronoun is English
  supplement, not rendering. The table itself adapts the pronoun for ἐν σπέσσι γλαφυροῖσι ("her"/"the").
  Left as is.
- **2.40 οὗτος ἀνήρ rendered "that man".** οὗτος can point to the man just asked about. The rendering is
  natural and does not mislead. Left.
- **2.97 "until this robe".** φᾶρος has no demonstrative, but the deixis is harmless when she is standing at
  the loom. Left.
- **2.45 ὅ = ὅτι "namely that".** A relative reading ("which has fallen…") is also possible. The note's
  reading is the standard one and is presented as "best taken". Left.
- **2.102 κεῖται as a short-vowel subjunctive (= κέηται).** This is the standard analysis in Monro. Left.
- **"Rest of the poem" claims.** Unlike 004, this part's notes make almost none. The survivors are
  background only: "ancient readers argued" (ἀργός, 2.11) and "Homer uses either as the metre requires"
  (Ὀδυσῆι/Ὀδυσσῆος, which lines 2 and 17 show). Neither asserts a specific fact about another passage.
  Left. The drafter's remark in new-renderings.md that 2.55–58 and 2.93–102 "recur later nearly verbatim"
  is in a proposal file, not a note, so it was out of scope. It is noted here for whoever ratifies that
  file.
- **new-renderings.md: ὑψαγόρην at 1.385 (odyssey-004) "should be checked".** I was instructed to read only
  the last 2–3 units of odyssey-004, so I could not check this. It is passed on to the next stage.

## Pass 2: changes to `gloss.json`

Novel entries:

| form | problem | fix |
|---|---|---|
| χρειὼ | idiom glossed "’what need has come upon him’" (see Pass 1 #1); also "nom./acc." | "fem. nom. sg. … ’whom has need come upon?’" |
| ἐύπωλον | "neut. acc. sg." but Ἴλιος is feminine; ἐΰπωλος has two terminations | "masc./fem. acc. sg. (two terminations; with fem. Ἴλιος)" |
| ἴλιον | no gender | "fem. acc. sg." |
| δάκρυ | key also covers δάκρυ’ (2.81) = elided δάκρυα, neut. acc. pl., not covered | added "· also elided δάκρυ’ = δάκρυα, neut. acc. pl." |
| ἐπέχραον | "unaugmented (= ἐπέχρησαν)": it is augmented, and the Attic comparison is odd | "augment after the preverb (ἐπ-έ-χραον)" |
| ὕφαινε | "unaugmented (= ὕφαινεν)": meaningless | "impf. 3 sg. (an augment on initial υ- does not show in writing)" |
| κατάνεται | lemma κατανύω; LSJ has its own headword κατάνω for this form | "κατάνω … (epic = κατανύω)" |
| ἀπαιτίζοντες | lemma ἀπαιτέω; LSJ headword is ἀπαιτίζω | "ἀπαιτίζω … (epic = ἀπαιτέω)" |
| ἔτλη | lemma "τλῆναι" (an infinitive); LSJ lemmatises under τλάω | "τλάω … (ἔτλην, inf. τλῆναι)" |
| ὀλέσσει | lemma ἀπόλλυμι, pinned to the tmesis; the form itself is from ὄλλυμι | "ὄλλυμι … (= Attic ὀλεῖ); in tmesis ἀπὸ … ὀλέσσει = ἀπολέσει" |
| περιναιετάουσι | "(diectasis)": it is plain uncontraction | "epic uncontracted (= Attic -ῶσι)" |
| μετέειπε, προσέειπεν, ἔειπες | "epic stretched" / "prefixed ἐ-" | "epic uncontracted, augment ἐ- kept" |
| ἄσχετε | "(= ἀνάσχετος)": opposite meaning (see Pass 1 #7) | "(ἀ- + σχετός; epic also ἀάσχετος)" |
| πίονας | "masc. acc. pl." but it agrees with fem. αἶγας | "masc./fem. acc. pl. (fem. usually πίειρα)" |
| λυγρῷ | "neut." only; the entry is meant to be general to the form | "masc./neut. dat. sg." |

Broadenings. I checked all 9: each contains its known-forms entry verbatim as a prefix followed by " · ".

- **χαῖρε · wrong tense.** "also aor. 3 sg. … (χαῖρε = ἔχαιρε)" is self-contradictory. ἔχαιρε is the
  imperfect (the present stem χαιρ-); the aorist is ἐχάρη. Changed to "impf. 3 sg., unaugmented".
- **ἀπὸ.** Removed the "ἀπὸ … ἀμῦναι = ἀπαμῦναι" example (see Pass 1 #11). The old entry, "from; + gen.",
  already covers ἀπὸ οἴκου. Kept the two real tmeses (49, 78).
- **τι.** "plain indefinite, not negatived" does not fit 2.44 οὔτε τι δήμιον ἄλλο, which is negated but
  still adjectival. Changed to "also adjectival indefinite: ’some, any’".
- **ὅ (360 chars) and περὶ (258 chars)** exceeded the 230-character limit. I compressed the appended part
  only, keeping the old entry whole: ὅ → "· also = ὅτι ’that’; εἰς ὅ ’until’" (224), and περὶ → "· also preverb
  in tmesis" (217).
- **ᾧ, φίλος, ὅτε, ὑπὸ.** The broadening is justified and accurate. Left.

Broadenings added. Each is a known form whose existing entry does not cover this part's usage and which the
glosser missed:

- **οἷος** (2.59, οἷος Ὀδυσσεὺς ἔσκεν). The known entry is "οἶος — alone, only", the smooth-breathed word.
  It is wrong for this rough-breathed relative of quality. Added "· rough-breathed οἷος is relative ’such as,
  of the kind that’".
- **οὗ** (2.27, 2.90, ἐξ οὗ). The known entry is "masc. gen. sg.: ’whose’". Added "· also neut. gen. sg. in
  ἐξ οὗ ’since, from the time when’".
- **κεῖται** (2.102). The known entry covers only the present indicative. Added "· also subj. (= κέηται):
  ’should lie’".

Checked and left:

- Every other parse was checked against its line: case, number and gender against the noun each form
  agrees with, and tense, mood and voice against the construction.
- Article-pronoun forms are glossed as pronouns, and possessive/relative ὅς is kept distinct.
- No entry contains an ASCII apostrophe or a backtick.
- All entries are under 230 characters after the edits.
- πέπνυμαι as the lemma of πεπνυμένα is left: LSJ has a cross-reference headword, and the entry names πνέω.

**Not fixable by me (for QUESTIONS.md):** the published known-forms entry for **ἔβη** reads "aor. 3 sg.,
root aorist, unaugmented (= ἔβη)". ἔβη is the augmented form; βῆ is the unaugmented one. Entries are
additions-only, and the file is outside my remit, so I have flagged it here and not changed it.

## Structural checks (after edits)

- 64 units. The concatenated `t` reproduces packet.md exactly, and every `t` is byte-identical to the draft.
- The `\n` count of every `l` equals that of its `t`. No `i` contains `\n`.
- `p` marks and quotation marks are as listed above. There are 4 `mark`s: 25, 40, 85, 96.
- Every note is 25–110 words: the longest are 109 (2.52) and 107 (2.96); the shortest is 34 (2.81).
- gloss.json: 299 novel entries, which match novel-forms.json exactly; 12 `__broaden__` entries.

## Summary

- **Units touched:** 19 of 64 (2.1, 19, 24, 28b, 39, 42, 48, 50, 52, 58a, 58b, 60b, 62, 64, 85, 89, 94,
  96, 99).
- **Severity:** 1 major (the τίνα misconstrual at 2.28, which changed the sense of both layers). 5 moderate
  (the πάγχυ/πάμπαν position claim, the two false "unaugmented" claims at 2.19 and 2.50, ἄσχετος =
  ἀνάσχετος, and the wrong tense in the χαῖρε broadening). The rest are minor.
- **Gloss:** 17 novel entries corrected, 5 broadenings corrected, 3 broadenings added.
- **For QUESTIONS.md:**
  1. ASCII vs typographic ’ in `l`/`i`/`n` across the corpus.
  2. The wrong "unaugmented" on the published ἔβη entry.
  3. ὑψαγόρην at 1.385 to be checked against 2.85.
