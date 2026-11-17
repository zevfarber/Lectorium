## Pass 1

### What I read

- Pipeline files:
  - run3/RUNBOOK.md (the Reviewer section), runbook.md
  - conventions.md (all the "House renderings settled" sections), QUESTIONS.md
  - packet.md, drafter-notes.md and units.json
- For house practice:
  - the published king-list-uruk-iv-gutium.json and king-list-antediluvian.json
  - the `l`/`i` of every published king-list-*.json, for the formulae (dynasty openings, "son of X — years N", one-king totals, the smitten refrain, numeral glyph and morph shapes)
  - drafts/king-list-uruk-iv-gutium/review.md (for the format)
- signs-cuneiform.json: the `values` of every sign key the part uses (checked by script against each glyph's `tr`).
- Langdon pp. 19–21 (langdon1923_0024–0026.jpg): the transliteration and translation of VIII 1–46 and fns. 7–9 (p. 19), 1–13 (p. 20) and 1–6 (p. 21).
- Pl. IV (langdon1923_0045.jpg), Col. VIII, cropped and zoomed 3–6× (scratchpad reviewer/):
  - every line from VIII 3 to the colophon, each sign counted against Langdon's print;
  - for comparison, side by side:
    - the AMAR of VIII 13/15 against the sign of VIII 34/37;
    - the final sign of VIII 34 against the KID of VIII 13, 17 and 25 and the IB of VIII 20;
    - the start of VIII 31 against the start of VIII 36;
    - the final DU of VIII 8 against that of VIII 22;
    - the NE-like sign of VIII 17 against the A-ga-de₃ line of Col. VII.

### How the edits were made and checked

Edits were made by script (scratchpad reviewer/rev1.py): load, modify, dump with indent=1 and ensure_ascii=False (the file's own format, checked to round-trip byte for byte before editing). No cuneiform was retyped. One glyph (AN) and one morph were deleted; four glyph roles were changed; the rest are text edits.

Checks:
- The script asserts that each replaced string occurs exactly once, and that every morph `g` covers its word's glyphs exactly once.
- hooks.assemble + hooks.validate, in memory → no errors. One WARN: 5 linecheck lines (VIII 13, 15, 17 by-sign readings; VIII 20, 45 numeral notation), all confirmed on the plate as the drafter says.
- The linecheck.md that validate wrote was deleted again. `r3.py build` was not run. Nothing outside drafts/king-list-uruk-v-ur-iii-isin/ was touched (git status: units.json modified, review.md new).

### Changes

- **VIII 31 · words, l, n, about · major**
  - What was wrong: the draft ships a divine determinative that is not on the copy.
    - On the plate, VIII 31 begins at the very left edge of the column with LI: its corner-wedges and the closing upright, as in VIII 36, drawn over a hatched patch.
    - In VIII 36 the AN (a clear star) stands at that left edge and LI follows it. In VIII 31 LI itself starts there, so there is no room for an AN before it.
    - Langdon prints ᵈLi- unbracketed. The drafter wrote "the divine determinative and LI stand at the edge of a hatched patch".
  - What was done:
    - The AN glyph and the {d} morph were removed. The reading is now li-[bi-it-…].
    - The note now says no AN is drawn, that Langdon prints ᵈ, and that the plate is followed (cf. VIII 27, Shu-ilishu with no dingir).
    - The li-bi-it-ašdar gloss was made general to the form: it no longer says "the divine determinative and LI survive".
    - `about` adds this to the list of places where the copy differs from Langdon's print.
- **VIII 31 · n · minor**
  - What was wrong: the note said "P. No. 2 X 7 *also* has 'son of Idin-Dagan'". Langdon's fn. 11 says "So P. No. 5 Rev. 12, *but* No. 2 X 7 has 'son of Idin-Dagan'": a different father, not the same one.
  - What was done: the note now says "has instead".
- **VIII 9 · l, i, n · minor**
  - What was wrong: `l` read "Ur-[Namma] king", without the house "(was)" for an unwritten copula, and `i` read "was king".
    - The draft proposed a new house rendering, "X lugal" → "X was king", after Akkad's VII 2–5.
    - But the pilot has the same construction with no -am₃ (I 3, eridu{ki} a₂-lu-lim lugal). There it is `l` "in-Eridu, Alulim (was) king", `i` "In Eridu, Alulim became king". Conventions fix the opening formula as "In X, Y became king; he reigned N years".
    - Akkad's "X lugal" is the anarchy line ("Igigi was king"), not a dynasty opening.
  - What was done:
    - `l` is now "in-Ur, Ur-[Namma] (was) king; years 18 [he]-ruled.", with NI in the break as in the reading [ni]-ag (cf. VIII 33 "[… he]-ruled").
    - `i` is now "In Ur, Ur-Namma became king; he reigned 18 years."
    - The note gives Langdon's "was king" and the house formula.
- **VIII 23 · l, i, n · minor**
  - What was wrong: the same as VIII 9.
  - What was done:
    - `l` is now "in-Isin, Ishbi-Erra (was) king; …".
    - `i` is now "In Isin, Ishbi-Erra became king; he reigned 33 years."
    - The note was adjusted to match.
- **VIII 44 · n · minor**
  - What was wrong: the note said Langdon reckons the dynasty "with the king omitted at the end" as 15 kings and 226 years. In fn. 6 the 15th king is the six-month reign after Girra-imiti that this scribe leaves out. The omitted last king (Damiq-ilishu) is Langdon's reason for dating the prism to Sinmagir's reign, a separate point.
  - What was done: the note now gives both points as fn. 6 does, including the conclusion (8 years for Erra-imiti, not 7).
- **VIII 41 · n · minor**
  - What was wrong: the note describes five drawn signs, I, DI, IR, KA and ŠA, as if each could be seen.
    - On the copy, the stretch between AN and MU is four groups of wedges: a box with diagonals; a corner-wedge with a horizontal and uprights; a box with a long horizontal ending in an upright; and a box of horizontals.
    - These do not part cleanly into Langdon's five signs.
  - What was done: a sentence was added saying that the sign-by-sign assignment follows Langdon's reading, not the drawing. The signs and readings are unchanged (Langdon's fn. 4 confirms the name from a date formula).
- **VIII 23, 25, 38 (ARAD), VIII 41 (KA) · glyph role · minor**
  - What was wrong: er₃ and pi₄ are syllabic values here (er₃-ra spells the god's name syllabically; pi₄ spells Akkadian pî), but the glyphs had role `log`.
  - What was done: both roles are now `phon`, as for i-bi₂ (NE) and ṭe (DI) in the same names.
- **about · minor**
  - What was wrong:
    - It called -ke₄ "a 'by'". -ke₄ is the genitive plus the ergative (the notes and gloss say so).
    - It said the Isin reigns "on the prism" add up to 213, but three of the fourteen figures are Langdon's restorations.
  - What was done:
    - -ke₄ is now "('of', marking 'son of Ur-Ninurta' as the subject)".
    - It now reads "whose reigns, with three figures restored by Langdon, add up to 213".
    - The VIII 31 dingir was added (see above).
- **VIII 3 · l · style**
  - What was wrong: "days 7" reversed the order of the signs (mu 7 šu-ši 7 u₄). House order follows the signs (gutium VII 49 "days 40" for u₄ 40).
  - What was done: it is now "…, 7 days [he-ruled]."
- **VIII 5 · l · style**
  - What was wrong: "its-years" for mu-bi. Every published total, including one-king totals (IV 41, V 40), has "their-years". "[days] 7" had the same order fault as VIII 3.
  - What was done: it is now "1 [king]; their-years 7 (and) a-sixth (?), 7 [days] [he-ruled]."
- **VIII 7 · l · style**
  - What was wrong: "its-kingship to-Ur [went]". The drafter's own reading has ĝen surviving and the terminative -še₃ restored (urim₂[{ki}-ma-še₃ ba]-ĝen), so the brackets were on the wrong word.
  - What was done: it is now "its-kingship [to]-Ur went."
- **VIII 21 · l, n · style**
  - What was wrong: "Ur(-ma) with-weapons". House `l` uses parentheses for what is *not* written, but here -ma is written.
  - What was done:
    - It is now "in-Ur (sic) with-weapons was-smitten", on the model of "to-X (sic)" for a misplaced -še₃ (V 23, VII 15).
    - The note says so; the English is unchanged.
- **VIII 36 · l · style**
  - What was wrong: "Lipit-Enlil, son of-Bur-Suen, years 5". House `l` puts " — " before the reign after "son of X" (as VIII 11–17, 25–29 here).
  - What was done: it is now "son of-Bur-Suen — years 5 he-ruled."

### Flagged decisions reviewed and kept (findings refused, with reasons)

- **VIII 4/6 "mu 7 šu-ši 7 u₄"**
  - The plate confirms MU, 7 (four over three), ŠU, IGI, 7, UD in VIII 4, and MU BI 7 ŠU IGI 7 in VIII 6.
  - Kept as Langdon's 7⅙ (?) years and 7 days, per conventions ("keep Langdon's reading as the base"). His fn. 7 gives the basis.
  - The note's alternative (7 šu-ši = 420, by the prism's own II 30 usage) is argued from the text, not from a modern edition.
  - Not changed. Open question for the owner: see below.
- **VIII 31 Ašdar as a LACUNA glyph**
  - Langdon's restoration carries no "?". So, strictly, the house rule would ship it as signs in brackets.
  - But he gives a value (Ašdar), not a writing. The packet's AB+DIŠ is an unverified first pass. In VI 17 the run could not identify his Ašdar on the copy (the published x-mu-ti).
  - Any sign chosen here (MUŠ₃, eš₄-tar₂ …) would be a modern supply, not Langdon's.
  - Kept: [bi-it] as signs, Ašdar as the gap glyph, with the lemma and the English as Langdon's. For QUESTIONS.md.
- **VIII 34 trailing KID**
  - Compared side by side, the box beyond the break matches the KID of VIII 13, 17 and 25 (horizontals with upright heads), not the IB of VIII 20 (which would end the father's name ᵈNin-IB).
  - Kept, flagged.
- **VIII 8 surviving DU**
  - It is the same form as the final DU of VIII 22. Only ŠEŠ of urim₂ survives at the break (AB is in it). Langdon prints Uri unbracketed.
  - The reading urim₂[…] leaves the AB unbracketed, while VIII 34 splits a logogram as {d}su[en] after Langdon's S[in].
  - Both follow Langdon's own bracketing, and the notes say what survives. Not changed. A house rule for a half-surviving two-sign logogram would help (QUESTIONS).
- **Bur-Suen: BUR vs AMAR**
  - Confirmed: VIII 13/15 draw an upright, horizontals and an arrowhead/diamond. VIII 34/37 draw a closed box with horizontals and upright heads.
  - Different signs; AMAR for Ur III and BUR (flagged) for Isin kept.
- **ARAD for Gir\***: the same sign in VIII 23, 25 and 38 (a horizontal with slanting wedges and uprights). ARAD (er₃) kept, flagged as in the note; Langdon himself stars it.
- **NE in Ibi-Suen (VIII 17)**
  - A box with crossing diagonals joined to a box with an upright. That is not BAD (Langdon's be).
  - Kept as NE (bi₂), flagged.
- **KAK vs DU₆ in Ur-dukuga (VIII 42)**: the drawing does not settle it. KAK follows Langdon's dù and the house dū → du₃ (KAK). Kept, flagged.
- **GIR₂ in magir (VIII 43)**: a box with corner-wedges; Langdon gir. Kept, flagged.
- **VIII 13/15/17 readings**
  - Confirmed:
    - VIII 15 has a compact ŠU (not the long Gimil), with no AN before it.
    - VIII 17 has no sign between ZU and KID (so not Langdon's -Sina-).
    - VIII 13 has dumu {d}šul-gi-ke₄.
- **Brackets for signs Langdon prints unbracketed but hatched away** (VIII 5 lugal, VIII 6 u₄, VIII 9 {d}namma, VIII 10 ni, VIII 28 ni-ag, VIII 33 {d}nin-urta): each confirmed on the plate. Kept.
- **ib-ag gloss "plural reign verb"**: an existing glossary entry (QUESTIONS 2026-11-16 notes that the -b- is not a plural marker). Not changed here; left to the published glossary decision.
- **The drafter's proposed house renderings**:
  - "X lugal (no -am₃) → was king" is refused (see VIII 9).
  - "Ur(-ma)" is replaced (see VIII 21).
  - The rest are accepted: "X, years N he-ruled" for one-line reigns, "7⅙ (?) years and 7 days", colophon "By the hand of PN", and the English names.

### Sign glossary values (noted, not edited)

The `values` lists in signs-cuneiform.json lack, in substance, the value this part uses for:
- ARAD er₃
- IB urta
- ENGUR namma
- KA pi₄
- KAK du₃
- DI ṭe (it lists ṭi)
- IG ĝal₂
- UR2 (no `values` at all; the name gives úr)

Present only in accented form:
- NE bí (= bi₂)
- GAN ḫé (= ḫe₂)

The drafter's "BUR in Bur-Suen" is not a gap: BUR lists bur. Values used in earlier parts and already noted (KU tukul, PA sig₃, EN suen) are not repeated here.

### For QUESTIONS.md

- VIII 4/6: Langdon's 7⅙ years (šuš = 1/6) is kept, against the prism's own use of šu-ši = 60 elsewhere (which would give 420). The owner may want a ruling.
- VIII 31: Ašdar shipped as a gap glyph, although Langdon's restoration has no "?", because no sign can be given for it. The dingir Langdon prints is not on the copy and was removed.
- A half-surviving two-sign logogram (urim₂ in VIII 8, suen in VIII 34) is bracketed inconsistently, following Langdon each time. A house rule would help.
- Sign `values` gaps listed above.

**Counts: 1 major, 7 minor, 5 style.**

## Pass 2

### What I read

- gloss.json: all 23 new entries and the 4 `__broaden__` entries.
- The published entries for šu-ši, -ma, -na and šu-{d}suen, taken from r3lib.merged_inline_glossary('king-list'), to check that each broadening keeps the old entry whole.
- units.json once more after the pass-1 edits: every unit's `l`, `i` and `n`, and every morph gloss compared by script against gloss.json and the published glossary.
- The plate, as in pass 1, for the entries that describe drawn forms. These are the absence of AN before Lipit-Ashdar (VIII 31) and before Bur-Suen (VIII 37), the compact ŠU (VIII 15) and the AMAR/BUR contrast.

### How the edits were made and checked

Edits were made by script (scratchpad reviewer/rev2.py): load, modify, dump with indent=1 and ensure_ascii=False, which is the format of both files (checked to round-trip). After the edits:
- The script asserts that each broadening starts with the old entry whole + " · ".
- Every morph gloss in units.json was set to its gloss.json or `__broaden__` text. That made 10 morph glosses consistent: -ma ×3, šu-ši ×2, šu-i₃-li₂-šu ×2, bur-{d}suen ×2 and li-bi-it-ašdar ×1.
- The numeral morphs (diš/u/geš "N here = …") and "lugal (here plural 'kings')" differ from the glossary on purpose, as in every published part. They were left alone.
- hooks.assemble(units, gloss) + hooks.validate, run in memory → no errors. One WARN: the same 5 linecheck lines as in pass 1. The linecheck.md it wrote was deleted. No build, no commit.

### Changes

- **li-bi-it-ašdar · gloss.json + morph · major**
  - What was wrong: the entry still opens with Langdon's ᵈLi-[…]. It did not say that the copy draws no divine determinative, the change pass 1 made to the text (VIII 31). A reader would take the dingir to be on the prism.
  - What was done: added "Langdon prints a divine determinative before the name, but none is drawn on the copy". The units morph was aligned to the entry.
- **-ma · __broaden__ + morphs · minor**
  - What was wrong:
    - The broadening was pinned to a line ("'Ur was smitten', VIII 21").
    - It left out the use the text also has, -ma before the terminative (urim₂{ki}-ma-še₃, VIII 8). The VIII 8 morph carried a different, unmerged gloss, and the VIII 9 morph carried the old entry. That gave three texts for one lemma.
  - What was done:
    - The entry is now the old entry whole + " · also written after urim₂{ki} where no 'of' or 'in' is expected — before the terminative (urim₂{ki}-ma-še₃ 'to Ur') and in the smitten refrain, where other cities stand bare; its function there is not clear". It has no line number.
    - All three morphs now carry this entry.
- **šu-ši · __broaden__ + morphs · minor**
  - What was wrong: the broadening was pinned to one reign ("(Utuhegal's reign)").
  - What was done: it is now general to the form: "after a number of years (mu 7 šu-ši 7 u₄) taken by Langdon as '1/6' (of a year) …; uncertain". The old entry is kept whole.
- **šu-i₃-li₂-šu · gloss.json + morphs · minor**
  - What was wrong: "NI-NI (i₃-li₂, Akkadian ilī 'god')". ilī with a long ī is 'my god'. The form before -šu is ili, the genitive of ilum: ili-šu 'of his god'.
  - What was done: it now reads "Akkadian ili, genitive of ilum 'god'".
- **bur-{d}suen · gloss.json + morphs · minor**
  - What was wrong: "written with the divine determinative". In VIII 37 (dumu bur-{d}suen-ke₄) the copy draws no AN before BUR, and Langdon prints none.
  - What was done: added "(once without it)".

### Entries checked and kept

- **utu-ḫe₂-ĝal₂, ur-{d}namma, šul-gi, amar-{d}suen, i-bi₂-{d}suen, i₃-si-in**: the signs agree with the text and the plate, and the uncertain identifications are flagged.
- **iš-bi-er₃-ra, i-din-{d}da-gan, iš-me-{d}da-gan, er₃-ra-i-mi-ti, en-lil₂-ba-ni, za-am-bi-ia, i-ṭe-er-pi₄-ša, ur-du₃-ku₃-ga, suen-ma-gir₂**: the same holds.
  - The Akkadian etymologies are glossed as plain words: 'Dagan gave', 'Dagan heard', bāni 'creator', magir 'favourable'.
  - Iterpisha's 'her word saves' and the Hilprecht writing are Langdon's (fn. 4).
- **ur-{d}nin-urta, li-bi-it-{d}en-lil₂, nu-ur₂-{d}nin-šubur, 14, šu**: agree with the text and the plate.
- **"On this prism …" in several entries**: kept. These describe the form on the single source, as the published šu-{d}suen entry does. They are not line references.
- **-na and šu-{d}suen broadenings**: the old entry is whole + " · " + the new reading, and the new readings are general. Kept.
- **The glosser's modern forms**: no invented or modern forms were found. Every lemma matches the drafter's by-sign readings, and every entry gives Langdon's form.

### units.json re-check after pass 1

- Nothing further. The pass-1 `l`/`i` changes (VIII 3, 5, 7, 9, 21, 23, 36) and notes (VIII 31, 41, 44) read correctly against the plate and Langdon's footnotes.
- Glyph roles are consistent: ARAD and KA are phon, as are NE and DI in the same names.

**Counts: 1 major, 4 minor, 0 style.**
