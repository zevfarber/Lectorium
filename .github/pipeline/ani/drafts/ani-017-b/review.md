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

## Pass 2

Changes are listed as U<n>/gloss · field · severity · what was wrong · what was done. Units are numbered from 0. All edits were made by one script (scratchpad edit.py), and it asserts each old value before replacing it. No glyph code, glyph order, role, tr, q, rubric flag or restored flag was changed. I found no majors. I looked hard for one, given that pass 1 also had none. The verb forms in l / i (sḏm·n·f past, sḏm·f, passive sḏm·tw·f, relative šmt·n / wḏꜣ·n, participles, infinitives after m and after n) all match the notes and the signs.

- U43 · l, i, n · minor · "hrw pwy" was rendered "the-day · it-is", and the note said that pwy "does the work of pw". pwy is the demonstrative 'that', as hrw pwy is in U41 and in part 1. No pw is written · l → "day · that · of …", i → "It is that day on which …". The note now says that pwy is the demonstrative and that 'it is' is supplied, as in U4 (line 32). It also says that pwy may stand for pw, though this is not sure. The glossary broaden of pwy ('also standing for pw') was a lexical claim made for this one passage, so I dropped it.
- U22 · l, i, n · minor · "who traverses Millions" is Budge's word ('Traverser of'). The known gloss of sm is 'go, make one's way' · → "who-goes-through" / "He who goes through Millions". Budge's word is kept in the note only as his rendering.
- U8 · n · minor · wnn had no form label ("the verb 'be' opens the sentence"). The published parts read a sentence-initial wnn as the doubled sḏm·f, often 'will be' (125-rubric, weighing) · the note now names the form and gives 'shall be' as possible. It also adds that after ii the preposition m may mean 'from'.
- U5 · n · minor · wnn·sn had no form label · the note now names the doubled sḏm·f and gives 'they will be' as possible. sꜣk now also says it is perhaps a writing of sꜣq 'gather'.
- U38 · n · minor · ḫpr after ꜥḥꜥ·n·w had no form label · the note now takes it as the stative with its ending not written, which is the construction after ꜥḥꜥ·n with a pronoun subject.
- U39 · n · minor · mꜥ was called "the preposition m in the later spelling mꜥ". That is a dating claim I cannot support · now "taken as the preposition m written with the arm (Budge: mā, 'in'); it may instead be the compound m-ꜥ 'with'". The reading is marked not sure.
- U27 · n · minor · Under the misprint rule a reading must be one the sense allows only one way. The water n printed before the name could also be the name's own n, with the genitive not written. That is also why it is n and not nt after a feminine noun · this alternative is added, with the remark that the sense is the same.
- U37 · n · style · ḥnnw was "written as in part 1 (the hoe U6 over two waters)". Part 1 codes the hoe, one water and the pot nw. Here there are two waters and no pot · the note now describes the signs as they are here and says that part 1 has the same word.
- U25 · l · style · rḫ·n·i is a sḏm·n·f, but l had "know-I" · → "have-learned-I". i keeps 'I know', as the note explains.
- U2 · n · style · "nḏ ḥr, literally 'care for the face of'" gave an etymology, not a sense · → "nḏ ḥr, with ḥr 'face', is 'protect, look after'".
- U28 · n · style · "taken as the sign ꜣb" did not name the ꜣb sign · added "(the chisel U23)".
- gloss iwt, ẖpꜣ, wꜣḏ-wr, mꜥꜣt, š-mꜣꜥt, ḏsr, bꜣḥ, hꜣb · minor · gloss.json predates pass 1's clean-up of new-lemmas.txt, and these entries still carried notes on this passage: the signs of this occurrence ("written with the bird of bad things", "written with the house classifier"), "here" senses ("here the name of one of the two nests", "reading … not sure here", "reading doubtful here"), and a reading of the passage passed off as lexicography ("a lake of Abydos", "the gods before the creator", "said of the Eye") · each entry is made general. ḏsr now cites Ta-sert, as pass 1 asked. mꜥꜣt keeps Budge's 'nitre' as his rendering. hꜣb is kept apart from hꜣb 'send'.
- gloss prw · minor · "a god's going out in procession" is an invented sense. The procession word is the feminine prt · → "coming forth, going out (noun; from pri 'go forth')".
- gloss sꜣk · minor · added "perhaps a writing of sꜣq 'gather, collect'" and a query on the sense. The attested verb has q. The known key sꜣq ('robbery, theft', from the 42 declarations) is a different matter, so I did not merge the lemma into it.
- gloss wꜣi · minor · "to set out, start on (a road)" is not the sense of the lemma · → "to go far, set out; wꜣi r with an infinitive 'to set about, be on the point of'".
- gloss rḥwy · minor · "from rḥ 'companion'" is an etymology I cannot confirm · dropped. The entry is now "a name of Horus and Seth".
- gloss ḥw · style · added the name's meaning, 'Utterance'.
- gloss __broaden__ nḏ · minor · "literally 'look after the face of'" was a speculative etymology, and "nḏ-ḥr itf·f … a name of Horus" was tied to this passage · now the known entry + " · in the compound nḏ-ḥr 'to protect, take care of' (verb; with ḥr 'face')".
- gloss __broaden__ ·w · minor · "(doubtful here, after ꜥḥꜥ·n)" was tied to this passage, and no grammar label was given · now "also the suffix pronoun of the 3rd person plural 'they' in later Egyptian, written w".
- gloss __broaden__ m · minor · "in later copies" was an unsupported dating · now "also written mꜥ, with the arm".
- gloss __broaden__ mḥtt (new) · minor · mḥty in U27 and U32 is the masculine 'northern' (in U32 it agrees with masculine sbꜣ), but the known entry gives only the feminine · added the known entry + " · also mḥty, the masculine 'northern' (nisba adjective)".
- gloss n-iꜣrrd-f · checked: gloss.json has no obsolete key. The lemma is the known key n-iꜣrrd-f, and iꜣrrd-f appears nowhere.

### Refused findings
- U13 / U14 l "is-cut" / "is-driven-away" against i "the cutting" / "is driven away", and U32 i without "as for": pass 1's reasons stand.
- U27 sbꜣwt both times (Budge: ṭuaut, then sebaut): the adjectives (rst feminine, mḥty masculine in form) do not decide the question, because the scribe also writes masculine n after both nouns. The doubt is in the note. Kept.
- U6 iꜥrwt "plural" with i "the two uraei": the ending is plural, the two cobras show the pair, and the note says both. Kept.
- U5 ḏrtw, with the second t and w coded det: the note says they double the pair and are not sounds. It is unusual but stated. Kept.
- U18 ꜥbt with U23 coded phon ꜥb (U23's value is ꜣb): the sign is an approximation for what the type shows, and 001-b reads the word ꜥbt. Kept.
- U31 sbꜣt pw ḏsrt, with masculine pw after a feminine noun: this is the same laxity in agreement as in U27, and the reading is already marked doubtful. Kept.
- U4 / U20 / U17 signs coded phon but not read (t and Z7 in ḥr-tp·f, the reed in wꜣḏ-wr, X1 in nni-nsw): the notes say they are not read, and nni-nsw matches 001-b and 017-a. Kept.
- U23 "who begets" (Budge: 'Begetter of'): wtt 'beget' has no other English. This is not a borrowing. Kept.
- Gloss entries ḏrt, šwt, irt, ḫsr, šꜥd, sḥri, ḥsmn, kꜣri, snf, mḥ, ẖrwy, ḏbꜥ, nšny and the broadens mn, sš, šn, ꜥḥꜥ, gr, wꜥb, stꜣt, ẖrt: sound and general, so kept. The "here" inside the sš broaden belongs to the known entry, which must be copied whole.

Re-check: units.json and gloss.json parse, keep indent 1 and have no trailing newline. The 1258 sign codes, in order, equal the packet's w0..w367. Morph coverage is exact. Every det has an empty tr. Every Z9 at a horned viper has the viper's role and an empty tr. Every unit with rubric words says red, and every unit with restored signs says restored. Every morph lemma is a known key or a gloss.json key, and every gloss key and broaden is used. Every __broaden__ value starts with the known entry copied whole, then " · ". The longest note is 1505 characters.
