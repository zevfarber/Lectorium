# Review — ani-018-introduction (Spell 18, the introduction, Plate 12)

## Pass 1

All edits were made by script (`review1_018.py` in the reviewer's scratchpad). It loads units.json, asserts that every old string or sign it replaces is present exactly once, and writes the file back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, which is how the drafter wrote it. A second script (`check_018.py`) then confirmed these points:
- the 480 sign codes, joined in order, equal the sequence in `source/established/ani-018-introduction.json`.
- every word's `rubric` flag matches the established file. The red writing is ḏd in … ḏd·f in the first section, dwꜣ in the second and fourth, in … ḏd·f in Ani's two speeches, and only ḏd·f in the third (ḏd in black). Each of these units' notes says so.
- `restored` matches the established file except in w15 (U2 ꜣny), where the established word carries `restored` but its own note says that only M17 M17 A1 stand inside Budge's brackets. The draft flags those three signs only, which is correct (see "Considered and refused").
- every morph `g` list covers its word's glyphs exactly once. Every det has an empty `tr`, every role is one of the six, and every O34 has `tr` 'z' (sp U11, snw U26).
- every unjoined, unsplit word's `q` equals the packet's. The joins and splits are re-indexed correctly: ḫr·tn (U1, from two words `0:1` + `0:1:2`); in·n·i + n·tn (U2, from `0-1:2-3-4:5:6`); ii + ḫr·tn (U16, from `0-1-2:3-4:5-6:7:8`); in·n + n·tn (U17, re-split this pass, from `0-1:2-3:4:5` to `0-1` + `0-1:2:3`); di·k + n·i (U24).
- `ln` is the packet line of each unit's first glyph, and Budge's numerals restart in each of the four sections. `"p": true` stands on each section's first unit, on the "says" units, and on the first unit of each speech, as in ani-146-b.
- no Budge-ism (saith, triumphant, homage, thee/thou/thy, hath, cycle, right and truth, nether-world, estate, motive, divine chiefs, possesseth, cakes, soul) is left in any `l` or `i`.

Counts: 4 major, 11 minor, 5 style.

### Changes

- U14 · l, i, n · major · `l` "(from)-seeing(?)" and `i` "turned back from seeing(?) the sun disk" supply a "from" that is not written. It is Budge's construction ("my soul from the sight of the disk"), and it hangs the rest of the line on the negative clause · mꜣꜣ(?) and dgg are now infinitives, more things asked for after di·k n·i (U12), like pr, ii and ꜥq, so nothing has to be supplied. `l` "not · being-turned-back · ba-my · seeing(?) · the-Disk · beholding · the-Moon · for-ever · (twice)", `i` "without my ba being turned back; seeing(?) the Disk and beholding the Moon for ever. (Twice.)". The note gives Budge's construction and says the 'from' is not written. "the Disk" and "the Moon" follow ani-hymn-to-ra U28, the same wish.
- U18 w103 and U25 w144 · reading, say, tr, morph, l, i, n · major · The draft read sḥ "booth", made a "plot of land" of it, and followed Budge's "estate". sḥ has no sense of land (known-lemmas: "booth, pavilion, hall"). The published weighing of the heart has the same wish with the same sign coded O22 and the land wedge ("ꜣḥt mn m sḫt-ḥtpw … mi šmsw ḥr"). It reads the word ꜣḥt 'field' with a query, as the Hymn to Osiris does, and says why Budge's seḥ is rejected · reading `ꜣḥt` / `ꜣḥt·i`, say `ahet` / `aheti`, O22 `log` 'ꜣḥt', morph `ꜣḥt` (a known lemma). `l` "a-field(?)" / "field(?)-my", `i` "a field(?)" / "my field(?)". The notes now give Budge's seḥ, say why it is not followed, and call the reading doubtful (no sign clearly writes ꜣḥ, and no t is written).
- U2 w13 and U17 w95–96 · glyphs, morph, q, n · major · Both units said that "the papyrus writes ·tn without the preposition n; read n·tn". This correction was not justified, and the morph did not match the reading:
  - U17: the group is W25 N35:N35 X1:N35:Z2. With one n for the sḏm·n·f and the other as the preposition, the phrase is written in full: in·n n·tn. Only the complement n of in is missing, which is the house spelling in the weighing of the heart (W25 N35 = in·n·i). Under the misprints rule, what stands is translated · re-split W25 N35 | N35 X1 N35 Z2: in·n (W25 phon 'in', N35 phon 'n'; morph ini [0], sḏm·n·f [1]) and n·tn (N35 phon 'n', lemma n; X1 N35 Z2 ·tn), q `0-1` and `0-1:2:3`. The note was rewritten: no correction, and the 'I' is not written.
  - U2: the group after in·n·i is N35 over X1 over Z2, n above t, which is the reverse of the ·tn stacks in this part (ḫr·tn, ḥnꜥ·tn: t over n). So the n is the preposition, and the suffix lacks its own n. The draft made the n part of ·tn, and its morph had no `n` lemma, although the reading n·tn contains the preposition · N35 is now `phon` 'n' with lemma `n` [0], and X1 Z2 are ·tn [1,2]. The note opens "The papyrus writes n·t with plural strokes; read n·tn 'to you'". The sense allows only this reading, so the formula applies here. The note also says that the third section writes the phrase in full.
- U11 · i, n · major · The note itself identifies the ordinal snnw 'second' (two strokes + nw). Yet `i` "I have not done a double deed(?)" and the note's "a deed done double, two-faced" follow Budge's "a motive double". The known glossary entry for snnw gives "sp snnw 'a second time'" · `i` "I have not done a deed a second time(?)." The note now gives the literal 'a second deed', the phrase 'a second time' and the possible sense 'I have not repeated a wrong'. It says that Budge's 'double' reads the numeral and not the ordinal, and that the sense is not sure. `l` "deed · second(?)" is kept.
- U14 w82 · reading, say, tr, n · minor · The reading `tgg` is not a word. It gave the sign coded X4 (a loaf, which has no value t) the tr 't'. The house reads this verb `dgg` (ani-hymn-to-ra U28, the same wish, with the hand d) · reading `dgg`, say `degeg`, X4 `phon` 'd'. The note says that the first sign stands where the hand should be, that it is doubtful, and that Budge reads t (teḳeḳ).
- U14 w78 · morph · minor · šnꜥ·tw had one morph `šnꜥ` over all four glyphs. The house splits off the passive (ani-hymn-to-osiris U20, ani-001-b U28) · `šnꜥ` [0,1], `sḏm·tw·f` [2,3]. The correction "The papyrus writes šn·tw; read šnꜥ·tw" is kept (see below).
- U2 w12 · morph · minor · in·n·i had `ini` over [0,1,2], which hid the n of the sḏm·n·f. The house has ini [0,1], sḏm·n·f [2], ·i [3] (ani-147-b U16–17, ani-017-c U2) · changed to match.
- U1, U8, U16, U22 ii (w4, w46, w90, w127) · glyph role/tr, U1 n · minor · Z4 was `det`. The house has the two strokes of ii as `comp` 'i' (ani-weighing-of-the-heart U27, ani-125-address U89–90) · Z4 `comp` 'i'. The U1 note now reads "with a second reed and two strokes as complements and the walking legs as classifier".
- U9 w52 isft · glyph role/tr, n · minor · The tall tied sign (Y1a, approximate) was `det` and "not read", and the note called S29 "the bolt s". S29 is the folded cloth, not the bolt (O34). The house reads the same tied sign in isft as the reed bundle is (ani-017-c U22: Y1a phon 'is', S29 comp 's') · Y1a `phon` 'is', S29 `comp` 's'. The note now says this and names the folded cloth.
- U22 · n · minor · The note called S29 in sḫrw·k "the bolt s" · "the folded cloth s".
- U1, U16, U19, about · l, i, n · minor · ḏꜣḏꜣt was "council". In the published parts it is "tribunal" four times (ani-001-a, ani-017-c, ani-022-072, ani-weighing-of-the-heart) and "council" once (ani-125-introduction) · "tribunal" throughout. The U1 forward reference now reads "Spell 18 proper, from Plate 13, goes through such tribunals one by one".
- U12, U24 · l, i, n · minor · nbw mꜣꜥt was "lords of truth". The house has "lords of Maat" (ani-017-c U15, U20; ani-125-address U30; ani-125-introduction U40) · "lords of Maat".
- U13 · l, i · minor · The note rightly says that ii and ꜥq, each written with the walking legs alone, are Budge's readings and doubtful, but `l` and `i` carried no query · `l` "coming(?) · going-in(?) · in · the-necropolis", `i` "coming(?) and going in(?) in the necropolis," (this also removes the awkward "going in within").
- U15 · n · minor · "a title of Horus as the loving son of Osiris" contradicts the name, which the note explains as 'the son whom he loves': Horus is the beloved, not the lover · "a title of Horus as the beloved son of Osiris, also borne by the priest who takes the son's part in the rites".
- U21 · n · minor · On p. 74 n. 1 the note said the papyrus has "two reeds …: i ḥr·k". Two reeds are not one i, and the note did not use the misprints formula · it now says the signs shown are Budge's and that his footnote gives a second reed where he prints nḏ. It reads "the papyrus writes ii ḥr·k …; read ind-ḥr·k", and says the greeting is the only sense the place allows. The glyphs keep Budge's print, as conventions require.
- U14 w83 iꜥḥ · n · style · The ꜥ that is not written was mentioned in passing. ani-hymn-to-ra U28 corrects the same spelling with the formula · "The papyrus writes iḥ, without the arm ꜥ; read iꜥḥ 'the Moon'".
- U11 · n · style · The note said "n ir·i", but the reading is iry·i · "n iry·i".
- U15 w88 sꜣ-mr-f · glyph role · style · G39 was `phon` 'sꜣ'. The house has the pintail sꜣ as `log` with its stroke (ani-001-b U0, ani-017-a U22) · `log`.
- U18 · l, i, n · style · nfw "air". The house has "breath" (ani-125-address U28, U53: "Lord of Breath", "Giver of Breath") · "breath".
- U14 · i · style · "the sun disk … the moon" · "the Disk … the Moon", as in ani-hymn-to-ra U28.

### The drafter's flagged doubts

- w80 (Budge [maa], unidentified sign coded D4) · kept as D4 `log` 'mꜣꜣ' with "seeing(?)". The note says the sign matches nothing and that Budge's bracketed maa is a guess from the sense. ani-hymn-to-ra U28 restores the same verb in the same wish. Making the glyph `det` with an empty reading would leave the line without a verb that the parallel shows is there.
- n·tn (w13, w94 in packet numbering) · changed (above). In the third section the phrase is written in full, so no correction stands there. In the first section the correction is kept in a different form: the preposition is written, and the n of the suffix is missing.
- šnꜥ·tw (w78) · the correction is kept. With n and bꜣ·i as subject, only šnꜥ 'turn back' gives sense: šni 'encircle, question' does not. The Hymn to Osiris has the same phrase with the arm. Only the morph was changed.
- sp snnw (w62–63) · changed in `i` (above). Z4 `num` 'sn' + W24 `phon` 'nw' with reading snnw is kept.
- ii / ꜥq (w73–74) · the readings are kept, as Budge's and doubtful. Query marks were added to `l` and `i`. The established note says the second pair of legs may face backwards (D55). D55 usually writes a verb of turning back, but Budge's ꜥq is not contradicted by the print, and the note already says that the signs show only a verb of motion.
- tgg / dgi (w82) · changed to dgg (above).
- Unread signs in btꜣ·f and isft · btꜣ·f: kept. The cup (W10, approximate) stays `det` and unread, and the note offers a misprinted ṯ as a possibility without asserting it. The reading btꜣ follows the signs and the lemma is bṯꜣ, which is right. isft: changed to the house reading is (above).
- p. 74 n. 1 (w119) · handled (above).
- Iun-mut-ef / Sa-mer-ef background · U0 is kept: "Pillar of his mother", a form of Horus as son, and the priestly title of the son in the rites for the dead. It is stated plainly and no further. U15 was corrected ("beloved"). The `about` ("two speakers who bear titles of Horus as the son of Osiris") is kept. The forward reference to Plate 13 in U1 and U26 is kept, as it only says that the spell continues there and goes through tribunals.

### Considered and refused

- U2 w15 ꜣny `restored` on M17 M17 A1 only, against the established word-level flag: kept. The established file's own note puts G1 N35 Z2 outside Budge's brackets, and the glyph flags follow the print.
- U3 "n sḏm·f, here of the past": kept. Negated n sḏm·f is the past "he has not / did not" (it is n sḏm·n·f that is the general "he cannot"), so the label is right. The same holds for U10 n ḏd.
- U24 r-gs with Aa15 `log` 'gs': kept. ani-weighing-of-the-heart U8 reads the same printed sign the same way. The note gives Budge's erma.
- U26 šsp as a sḏm·f wish ("may I receive") with the 'I' unwritten: kept, although an infinitive after di·k (as in U12–U14) would need nothing supplied. In English "and the receiving of offering loaves" is strained, the part leaves 'I' unwritten again and again (ii, ḏd), and the note states the choice.
- U12 m-bꜣḥ with no noun after it ("into the presence at the altar"): kept. The note says the noun is not written and how the phrase is taken. No better parse is available from the signs.
- U7 ḥry-ib "who dwells in": kept. ani-hymn-to-osiris U0 uses "who dwells in Abydos" in `i`. The `l` "who-dwells-in" differs from that part's "who-is-in-the-midst-of", but both are in house use.
- U9 reading isft with the t unwritten, U22 sḫrw with the w unwritten, U1 imyw with the y unwritten: kept. The house normalises readings this way, and each note says what is not written.
- U5 psḏt with X6 `log` 'psḏ': kept. It matches ani-017-a U12.
- U21 nw after a singular noun: kept. The note correctly calls it the plural genitive adjective.
- U0 and U15 say forms "Iun-mut-ef", "Sa-mer-ef": kept. They follow the say rule and the house's "-ef" for names ending in ·f. No published part has either name.
- U5, U19 "Adoring Osiris": kept. It matches ani-hymn-to-osiris U0 and ani-125-introduction U0.
- U13 a D55 reading: not adopted (above).
- `titleEn` / `part`: they follow the house pattern ("Spell 146, the pylons, part 2"; "(Plates 11–12)").

### For the glosser and pass 2

New lemmas after this pass (not in known-lemmas.json): iwn-mwt-f, sꜣ-mr-f, ꜥpr. They are all in gloss.json already. `ꜣḥt`, `n` (preposition), `sḏm·n·f` and `sḏm·tw·f` are now used, and all are known.

gloss.json was not edited, because the glosser is writing it. Pass 2 should check:
- the `__broaden__` entry for `sḥ` is no longer needed: the word is now ꜣḥt.
- the `sꜣ-mr-f` entry says "the loving son of Osiris" and should say "the beloved son".
- the `sḫr` broaden (noun 'plan, counsel') is needed for U22.

## Pass 2

All edits were made by script (`review2_018.py` in the reviewer's scratchpad, plus a one-line fix to the sḫr Budge form). Each file is loaded with json and written back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, as it was. `check_018.py` was run again afterwards, and it confirmed these points:
- the 480 sign codes, joined in order, equal the established file's sequence;
- every morph `g` list covers its word's glyphs exactly once, every det has an empty `tr`, and every O34 has 'z';
- rubric and restored flags are as in pass 1 (the w15 word-level flag is the known, refused case);
- no Budge-ism is in `l` or `i` (the only hit, "thou", is inside "without").

Lemma coverage was recomputed after the pass-1 changes. The morph lemmas not in known-lemmas.json are exactly iwn-mwt-f, sꜣ-mr-f and ꜥpr. These are now exactly the top-level keys of gloss.json: none is missing and none is unused. The lemmas that pass 1 brought in (ꜣḥt, n as a preposition, sḏm·n·f, sḏm·tw·f, dgi as dgg) are all known, and their known entries cover the senses used here. ꜣḥt is "field, arable land"; n includes "the preposition 'to, for'"; dgi is "also written dgg". So no new entry or broadening was needed for them. The one `__broaden__` key left, sḫr, is in known-lemmas.json, is used (U22), and its value begins with the known entry copied whole, then " · ".

Every `say` whose reading occurs in a published ani-*.json was compared with the published form (29 readings). All agree except snnw (below).

Counts: 0 major, 3 minor, 4 style.

### Changes

- gloss.json `__broaden__` sḥ · entry · minor · After pass 1 no unit uses sḥ, because U18 and U25 now read ꜣḥt. The broadening ("written with the classifier of land: plot, holding of land (Budge: 'an estate')") would also have added an invented sense to the glossary · removed.
- gloss.json sꜣ-mr-f · entry · minor · "a title of Horus as the loving son of Osiris" contradicts the meaning the same entry gives ('the son whom he loves') · now "the beloved son of Osiris". "borne by the priest who plays the son" is softened to "also borne by a priest who takes the son's part in the rites for the dead".
- U11 w63 snnw · say · minor · "sennu" breaks the say rule (e between consonants: s-n-n-w), and the published form is "senenu" (ani-weighing-of-the-heart) · `senenu`.
- gloss.json iwn-mwt-f · entry · style · "a title of Horus as the son who upholds his mother" turned the name into a claim about the god's role · now "a title of Horus as the son of Osiris and Isis". The priest's title is worded as for Sa-mer-ef. The meaning of the name, 'Pillar of his mother', and Budge's Ān-māut-f are kept.
- gloss.json sḫr `__broaden__` · entry · style · The added sense, "(noun m.; sḫrw·k 'your counsels', the plural ending w not written)", was pinned to this passage and to its spelling. The house asks for entries that are general to the lemma · now "plan, counsel, design (noun m.; plural sḫrw; Budge: seχeru)", with Budge's form as the packet gives it.
- gloss.json ꜥpr · entry · style · Budge's spelling was missing, while the house gives it for new verbs (ani-146-b gloss) · it now adds "Budge: āper" (packet w129). The sign is described as "the sign ꜥpr, a bag on a cord".
- U12 and U14 · i · style · U12 "May you give me bread, and coming forth into the presence at the altar …" joined a noun and a bare gerund with a comma · now "May you give me bread and a coming forth into the presence, at the altar of the lords of Maat,", as in the house wording of the same wish (ani-weighing-of-the-heart U25 "a going forth into the presence"). U14 had a semicolon before a phrase with no verb ("…turned back; seeing(?) …") · now a comma, so the infinitives read as further objects of di·k, which is what the note says.

### Fresh read of units.json (no change)

- `l` word by word against the words in every unit. Each `l` token maps to one word or a hyphenated join. The supplied subjects are bracketed ("have-come-(I)", "spoken-(I)", "receive-(I)"), and the unwritten 'and' is in brackets in U5 and U19.
- `i` against `l`: the force matches in every unit. Every "(?)" in `l` (U11, U13 twice, U14, U18, U25) is carried into `i`.
- Grammar labels in the notes checked again:
  - n sḏm·f is past (U3, U10, U11);
  - the passive sḏm·tw·f is in U14;
  - the stative is used for rḫ·kwi, ꜥpr·kwi and mn (U22, U23, U25);
  - imi is the imperative of rdi with a subjunctive sḏm·f after it (U4);
  - nw is the plural genitive adjective after a singular noun (U21);
  - imyw is the plural nisba (U1, U16).
  All are correct.
- Say forms not found in the published parts follow the rule: iryi, betaef, aperkwi, rekhkwi, sekheruk, aheti, Iun-mut-ef, Sa-mer-ef, Sekhet-Hetepet.

### Considered and refused

- Adding an entry or broadening for ꜣḥt: not needed. The known entry "field, arable land" covers the use, and the doubt belongs in the notes, which state it.
- Broadening mi, ḥry-ib, in, ḫr, ꜥꜣ, ḏt or tꜣ: not needed. Each known entry already lists the sense used here (mi 'like', ḥry-ib 'who dwells in', in 'says N', ḫr 'to, before' of persons, ꜥꜣ 'great', ḏt 'everlastingness', tꜣ 'land, earth').
- The gloss for iwn-mwt-f / sꜣ-mr-f mentioning the priestly title: kept, but softened ("also borne by a priest"). It is general to the name and not pinned to this passage.
