## Pass 1

### What I read

- Pipeline files:
  - run3/RUNBOOK.md (the Reviewer section)
  - conventions.md (all house renderings), runbook.md
  - packet.md, drafter-notes.md, linecheck.md and units.json
- For house practice:
  - the published king-list-akkad.json, king-list-akshak-kish-iv-uruk-iii.json and king-list-antediluvian.json
  - the `l` forms and glossaries of all published king-list-*.json (unwritten cases in "(…)", "son of X" with no hyphen when the genitive is unwritten, "to-X (sic)", numeral glyph and morph shapes)
  - drafts/king-list-akkad/review.md (for the format)
  - QUESTIONS.md
- signs-cuneiform.json: the entries ESH, ESZ, ESH2, GIGIR, SHU2, DUH, DUN, TAR, KAL, BAD, LAGAB.
- Langdon pp. 18–19 (langdon1923_0023–0024.jpg): the transliteration, the translation, fns. 4–12 and 1–6.
- Pl. IV (langdon1923_0045.jpg), cropped and zoomed 2–6× (scratchpad reviewer/):
  - Col. VII 15–51, every line, with the numeral column checked separately (lines 29–48).
  - For comparison: Col. VIII 1–2 (GU TU, EŠ₂) and VIII 15 (the compact ŠU).

### How the edits were made and checked

Edits were made by script (scratchpad reviewer/rev1.py): load, modify, dump with indent=1 and ensure_ascii=False. No cuneiform was retyped. Two `mu` words were deleted, one sign key was changed (ESZ → ESH), and the rest are text edits.

Checks:
- The script asserts that every morph `g` covers its word's glyphs exactly once.
- `r3.py build` → BUILT, 30 units.
- `validate` → **PASS**. One WARN: the 3 linecheck lines (VII 20, 21, 51), all confirmed on the plate as the drafter says.
- `signs.py check` → in sync.
- Afterwards stories.json was checked out and king-list-uruk-iv-gutium.json deleted. `git status` shows only units.json changed.
- signs-cuneiform.json, index.html and reader.html were not touched. Their sign additions are already committed (649e80fec).

### Changes

- **VII 31 · words, l, n · major**
  - What was wrong: the draft ships a MU 'years' that is not on the copy.
    - On the plate the line is NI, a box (kil), LA, then GAB (the DU₈ box with its corner-wedges), and then straight to 6 diš, NI and AK.
    - Every other reign line in the column draws MU between the name and the figure (VII 19–21, 29, 30, 32, 34–44, 47, 48). On this copy MU is a cluster of corner-wedges on a horizontal, closed by an upright. In VII 36 that MU stands clearly after the same GAB.
    - Langdon prints "mu 6 ni-ag" unbracketed. The drafter wrote "VII 29–35: These signs agree with Langdon".
  - What was done:
    - The `mu` word was removed.
    - `l` is now "Nikillagab, 6 (years) he-ruled." `i` is unchanged.
    - The note now says that there is no MU, that Langdon prints one, and that the figure is taken as years.
- **VII 33 · words, l, n · major**
  - What was wrong: the same fault. After E LU LU the copy has ME (an upright with a horizontal) and three corner-wedges, i.e. ME.EŠ, and then goes straight to 6 diš. There is no MU.
    - The three corner-wedges are not a MU. They match the EŠ of VII 34, which there stands before a MU drawn in the usual way.
    - The drafter identified ME.EŠ correctly but also shipped Langdon's mu.
  - What was done:
    - The `mu` word was removed.
    - `l` is now "Elulu-mesh, 6 (years) he-ruled."
    - The note says that no MU is drawn and that Langdon prints one, and that whether the scribe left mu out or wrote ME.EŠ where mu belonged is not clear.
- **VII 33 · words (glyph 4) · minor**
  - What was wrong: EŠ was keyed ESZ. conventions/QUESTIONS say that new parts use ESH, and VII 34 and 35 of this same part use ESH for the same drawn sign.
  - What was done: the key is now ESH, tr "" (ME carries meš).
- **VII 50 (VII 51 total) · n · minor**
  - What was wrong: the arithmetic was stated without its basis and did not say how far apart the figures are.
  - What was done:
    - The note now says that the 19 figures (VII 29–48) were each checked on the copy, and that VII 31 and 33 are counted as years although they write no mu.
    - The sum is 91 years plus 40 days. That is 34 years short of the restored 125. Langdon's "only 86" is 5 less than the figures he himself prints, and he does not say how he reached it.
    - Nothing is corrected.
- **about · minor**
  - What was wrong:
    - It said the years "Langdon fills … as 125 years and 40 days". But only mu-bi 125 is restored: UD and 40 survive (VII 51).
    - It quoted "had no king by name" without the query that `l` and `i` carry.
    - "Twenty named Gutian kings" is wrong, since one name is lost.
  - What was done:
    - It now reads "125 (the 40 days survive), far more than the 91 years and 40 days…".
    - It now has "had no king by name (?)" and "Twenty Gutian reigns follow…".
    - The missing mu of VII 31 and 33 was added to the list of places where the copy differs from Langdon's print.
- **VII 45 · n · minor**
  - What was wrong: the note said the long-form Gimil is "the same long form as in VI 9, VI 13 and VII 45", a reference to the line itself.
  - What was done: it now says VII 20.
- **VII 24, VII 27, VIII 1 · l · style**
  - What was wrong: "the-horde of-Gutium". House `l` uses "of-X" only where a genitive is written (VII 17 "son of-Ur-nigin") and "of X" where it is not (VII 45 "son of Hablum"; kish-i "son of Etana"). Here the genitive is unwritten, as the notes themselves say.
  - What was done: all three now read "the-horde of Gutium".
- **mu, e-lu-lu, šu-{d}suen · morph glosses · style**
  - What was wrong: the broadened glosses carried line numbers ("(VII 28)", "(VII 33)", "(VII 45)"). Glossary entries are general to the form (RUNBOOK, Glosser).
  - What was done: the line numbers were removed. The mu gloss now quotes the phrase "had no king by name".

**Counts: 2 major, 4 minor, 2 style.**

### Drafter's flagged points: verdicts

- **VII 15 unug{ki}-še₃: accepted, flagged.**
  - The third sign is a box with a middle horizontal and two upright heads, with no inner wedge.
  - It matches the EŠ₂ of VIII 2 (unug{ki}-še₃, the same hand). It does not match the GA of VII 47 (a box with a pointed wedge inside).
  - "to-Uruk (sic)" follows the V 23 / V 44 precedent.
- **VII 15 and 17, nigin; VII 17, gigir: accepted as flagged.**
  - nigin is a pointed head joined to a box of horizontals.
  - GIGIR is drawn as a plain box followed by a box with a diagonal.
  - The copy alone cannot settle either sign. Langdon's reading is kept, which is house practice (akkad VI 33).
- **VII 19 kud-da: accepted.**
  - The copy has two signs: a horizontal crossed by an upright with a slanting wedge, and DA (the box with an inner horizontal and wedge, as in VII 47).
  - TAR (kud) is a reasonable identification of the first sign and is flagged. It differs from the GIŠ of VII 24 (an upright crossed by horizontals).
- **VII 20 šu-i₃-li₂: accepted.**
  - The long two-part sign is the same as in VII 45, and unlike the compact ŠU of VIII 15. It is kept as Langdon's ŠU under the house rule.
  - Then come two NI exactly like the NI of ni-ag, then MU, 5, NI and AK.
- **VII 26/27, the unread sign: accepted as x.**
  - Both lines draw, between TU and UM, a cluster of 3–4 corner-wedges joined to a box of horizontals. UM is the box with uprights, as in VII 41–43.
  - I cannot identify it. Shipping it as x inside the name's morph is house practice (IV 30, VI 17).
- **ugnim signs: accepted.**
  - In VII 26, 27 and VIII 1 there are three separate signs: a pointed sign like KI, a box of horizontals, and a box with a crossing.
  - KI.KAL.BAD after Langdon's reading is flagged as uncertain.
- **VIII 1 unbracketed GU TU: accepted.**
  - On the copy five signs stand before the hatching: the three of ugnim, GU (the same box with an inner wedge as in VII 26), and TU at the edge.
  - Langdon brackets the whole name. The house rule brackets only what is hatched away.
- **VII 28 lugal-mu nu-tuk "by name (?)": accepted.**
  - It is Langdon's own translation ("had not a king by name").
  - mu = 'name' is good PD-lexicon sense.
  - The query is right, because the syntax of lugal-mu is unexplained.
  - "nu-tuk 'did not have'": a negated bare stem with no finite prefix. "not-had" in `l` is acceptable.
- **The Gutian total: confirmed and stated precisely (see Changes).**
  - Every figure was read on the plate: 3, 6, 6, 6, 6, 5, 6, 15 (1 u + 5), 3, 3, 1, 3, 2, 2, 1, 2, 7, 7, 7 (VII 29–48). That makes 91 years.
  - Tiriga reigned u₄ 40, 40 days.
  - Langdon's 86 cannot be got from his own printed figures.
  - The count of 21 is 20 entries (VII 29–49, VII 48's name lost) plus the kingless time (his fn. 5). That is correct.
- **VII 30 šu₂, VII 31 kil, VII 33 -meš, VII 35 GI+EŠ, VII 38 no "(gaš)": accepted.**
  - VII 30: the small corner-wedge with a tail.
  - VII 31: a plain box with a small inner stroke.
  - VII 35: GI and EŠ run together.
  - VII 38: nothing is supplied.
- **VII 47 [ia], VII 49 [ti-ri]-ga, VII 50 21 unbracketed, VII 51 [mu-bi 125] u₄ 40: accepted, as drawn.**
  - VII 47: AR stands at the edge of the hatching.
  - VII 49: only the right point of GA survives.
  - VII 50: a corner-wedge and an upright are clear in the hatched patch.
  - VII 51: UD at the edge, then 40, IB and AK.

### Findings considered and refused

- **The first sign of VII 26/27 GU looks like BA.** The box with an inner wedge resembles the BA of VII 24. But Langdon reads GU, the drawing is also consistent with GU, and the same sign appears in VIII 1. Nothing was changed.
- **The LA of VII 36, 38 and 47 might be two signs.** It is drawn as two parts, a cluster of uprights and a box of horizontals. But the same two-part form recurs in every LA of these names, and in VII 31 it is compressed into one. It is one sign, LA. The sign counts of the names agree with Langdon.
- **The numeral glosses ("1; 6 here = 6") and "king (here plural 'kings')".** These differ from the published glossary text, but they follow the published per-word morph practice (akkad VII 11). They were left.
- **The `mu` lemma broadened to "name".** It was kept. The glosser's gloss.json must carry the broadening.

### For QUESTIONS.md

- **VII 31 and VII 33: no MU 'years' on the copy**, where Langdon prints mu unbracketed. Decided meanwhile: the copy is followed (no mu word), the figures are counted as years, and Langdon's print is in the notes. In VII 33 the ME.EŠ (-meš) stands where mu would.
- **VII 51 Gutian total**: the prism's 19 figures make 91 years and 40 days. The restored total (P. No. 2) is 125. Langdon's fn. 5 says "actual total only 86". Decided meanwhile: all three are reported and none corrected. conventions.md lists VII 51 among the totals that do not add up, which stands.
- **VII 15 unug{ki}-še₃** at the head of a dynasty, where Langdon prints Unug-(ki) and the usual form is -ga. It is the third such -še₃ (after V 23 Mari and V 44 Akshak). Decided meanwhile: "to-Uruk (sic)", English "In Uruk".
