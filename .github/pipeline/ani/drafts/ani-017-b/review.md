## Pass 1

Changes are listed as unit · field · severity · what was wrong · what was done. Units are numbered from 0, as in units.json. Every edit was made by script (scratchpad edit.py and edit2.py). Each script asserts the old text before it replaces it. No glyph code, glyph order, role, tr, q, rubric flag or restored flag was changed.

- U8, U10, U33, U34, U45 · n · minor · Aa15 was called "the later owl m". Aa15 is not an owl: Budge's type prints it as a thin bar, and U38 of this draft describes it that way. The published parts call it "the sign Aa15" · each note now says "the sign Aa15" (for m).
- U43 · n · minor · The hatched sign in stẖ was "taken as the placenta ẖ". The placenta Aa1 writes ḫ, not ẖ · it now reads "taken as the ẖ of the name (the sign that writes it here is not clear)".
- U27 · words[iꜣrrd-f] reading, say; l, i, n · minor · The place was rendered "Naref", a name no published part uses. The introduction to Spell 125 writes the same place n-iꜣrrd-f, "En-iarered-ef". Here the n is left out, and the sense allows only that one place; Budge too reads it with n (Naàrutf). So the misprint rule applies · reading → n-iꜣrrd-f; say → En-iarered-ef; l and i → En-iarered-ef. The note now opens "The papyrus writes iꜣrrd-f; read n-iꜣrrd-f." and describes what is written. The lemma (n-iꜣrrd-f, known) is unchanged.
- U40 · l, i, n · minor · wḏꜣt was rendered "the Wedjat". Published ani-125-address renders it "the Sound Eye", which is also the known gloss · l "the-Sound-Eye", i "the Sound Eye". The note now reads "wḏꜣt 'the Sound Eye', the wedjat".
- U4 · l, i, n · minor · l had "placed-they · it(?)", but i had "setting themselves(?)". i followed Budge's sense, not the grammar: sw is the 3rd singular dependent pronoun and cannot mean "themselves". i also blurred the sḏm·n·f · l "have-placed-they · it(?)"; i "…, that is the going of Isis and Nephthys: they have placed it(?) upon his head." The note says that sw is the object, that what it stands for is unclear, and that Budge renders "themselves".
- U38 · i · style · "the gods who are in the following of Ra, Hu and Sia" reads as if Hu and Sia were also followed · → "in the following of Ra: Hu and Sia."
- U33 · words[ry] say · style · "ri" for the reading ry. The rule is y → y, as in nty "nety" · → "ry".
- U5 · n · style · sꜣk was given without saying that the signs stand in the order s, i, k, ꜣ · added "and ꜣ written after k".
- U31 · n · style · The arm sign of ḏsr was called "the arm holding a flail". Also missing was the strongest support for the reading: Budge writes ḏsr as "sert" in tꜣ-ḏsr "Ta-sert" (known lemma) · now "the arm holding a wand (D45)", plus that point about Budge. The doubt is kept.
- U11 · n · style · V29 was coded as a classifier without saying that Budge reads it as sk (χersek) · added that point, and that the reading ḫsr is not sure.
- new-lemmas.txt · wꜣḏ-wr, ẖpꜣ, ḏsr, BROADEN ·w · style · The entries carried "here" senses pinned to this occurrence, which a glossary entry should not have (the ruling of ani-017-a pass 2) · each "here" phrase is removed or made general. ḏsr now cites Ta-sert.
- new-lemmas.txt · iwt, hꜣb, mꜥꜣt · style · The entries carried notes on the signs of this occurrence ("written with the young animal…", "written with walking legs…", "written with the house classifier") · removed. The doubts are kept.

### Refused findings
- U27 sbꜣwt for both nouns, where Budge has ṭuaut first and sebaut second: the signs are identical, and the note argues for the reading and marks the doubt. dwꜣt "the Duat" would agree with feminine rst, but then the second noun would differ for no reason. Kept.
- U32 l "as-for … it-is" against i "It is the northern gate of the Duat.": the note explains the ir … pw frame and what it means. Rendering "As for the northern gate of the Duat, it is (this)" would be worse English and add nothing. Kept.
- U13 šꜥd·tw and U14 sḥri·tw, l "is-cut" / "is-driven-away" against i "the cutting" / "is driven away": the note names the passive sḏm·tw·f standing as a noun before pw. The l shows the form, and the i gives the sense. Kept.
- U3 prw·n·f called a sḏm·n·f "used as a noun after ir": a nominal sḏm·n·f after ir is grammatical. The i "his coming forth" gives the sense. Kept.
- U17 wꜥb·i, with the w "not read" and the possible stative ·kwi: both analyses (sḏm·f with ·i, or stative with k unwritten) are in the note. Kept.
- U8 wnn as the verb that opens the sentence: wnn N m X is regular. Kept.
- U2 nḏ-ḥr hyphenated: nḏ ḥr "protect" is a fixed compound, with two morphs in one word. Unlike ir-s in 017-a, this is not two independent words. Kept.
- U43 V13 coded phon "iṯ" with D54 det: the print splits the ligature V15 into tether and legs, and the note explains it. Kept.
- U21 mꜥꜣt, with the first D36 coded comp before O29: complements before the main sign are house practice (X1 before the sledge in tm). The word is shown as […]. Kept.
- U20, U22, U23 ḥḥ, C11 coded num: every published ḥḥ codes it so. Kept.
- `say` vowel-rule irregularities (saksen, itefsen, mehty, kheft, imten): these match the published parts or the 2026-11-18 QUESTIONS ruling ("left as drafted"). Kept.
- The question units (U1, U9, U12, U15, U19, U26, U36, U42) carry p:true, and ky ḏd units do not: this matches ani-017-a. Kept.
- Budge-isms and remembered wording: none found. "triumphant", "saith", "homage", "avenger", "thee", "Tmu", "Amsu", "protectresses", "tchefa", "nitre", "underworld", "failings" and "mutilation" appear only in the notes, as Budge's readings. "the cutting of the navel cord", "I am pure in my great double nest", "give me your two arms" and "the Two Companions" follow directly from the words and the grammar. Kept.
- Lemma keys: every morph lemma is a key of known-lemmas.json or a new entry in new-lemmas.txt. No new entry collides with a known key, and every BROADEN key exists. ·w, gr, pwy, m and wꜥb broadens are sensible; tr already has "time, season" and needs none for U45.

Re-check after editing: units.json parses and keeps its formatting (indent 1, no trailing newline). The 1258 sign codes, in order, equal the packet's w0..w367. Rubric flags match the packet word for word. Restored flags are unchanged (X1 D21 M17 M6 of tr in U1, N35 Z2 of ꜣny in U8, X1 of ·tn in U34 and U35). The structural checks still pass: morph coverage is exact, every det has an empty tr, every comp repeats a consonant of its word, and every Z9 at a horned viper has the viper's role with empty tr. The longest note is 1377 characters.
