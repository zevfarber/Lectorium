# Review — ani-hymn-to-osiris

## Pass 1

I edited units.json by script (scratchpad review1/edit1.py; checks in review1/verify.py). No sign code, sign order or glyph count changed. After the edits the concatenated glyph sequence (548 signs) still equals source/established/ani-hymn-to-osiris.json. Every morph g-list is non-empty and covers its word's glyphs exactly once. Every q covers its glyphs once. The rubric flags match the established file sign by sign (w0, w97, w98 only). The approx flags match, except where the drafter flagged every instance of a code the established file lists once (see "Considered and refused"). The restored flags sit only inside the one restored word (w75).

Units are numbered U0–U23 in draft order.

### Changes

Format: unit · field · severity · what was wrong · what was done.

1. U7 (ln4) m-bꜣḥ ꜥ nb-r-ḏr · l, i, n · minor · The draft rendered "before the arm(?) of the Lord of All" and called the ꜥ unclear. The published Spell 125 part has the same phrase, m-bꜣḥ ꜥ nb-r-ḏr. There it is l "before · the-hand · of-the-Lord-to-the-Limit", i "in the presence of the Lord of All", and the note says the hand names the god's power. · l "the-arm(?)" → "the-hand". i → "The Two Lands flourish for you in vindication, in the presence of the Lord of All." The note now gives the phrase as in Spell 125 and drops the doubt.
2. U2 (ln1) rmṯ · n · minor · The note opened "The papyrus writes rmṯ with r and ṯ only …; read rmṯ", presenting a scribal slip under the misprints rule. The published parts treat the m-less r-ṯ / r-t writing as an ordinary shortened spelling. Spell 125 (Ani's own text) reads it silently, and the address calls it "a shortened spelling of the later papyri". It is not a slip, and the correction formula claims too much. · I removed the opening correction sentence. The sentence on nṯrw rmṯ now says that rmṯ is written r and ṯ only, the shortened spelling the papyrus also uses in Spell 125, and that the classifiers and the pairing with nṯrw make the word sure.
3. U4 (ln3) nty · l, i, n · minor · The note took nty only as picking up ib·k ("the heart that is in the desert hills"). The relative may equally take up the suffix ·k, "you who are in …". That reading gives the usual sense, the god in the cemetery, and avoids the forced repetition of "the heart" in i. · The note now gives both antecedents and takes ·k. l "which-is" → "who-is". i → "Your heart is glad, you who are in the desert hills(?)." The closing sentence was adjusted to match. The doubt on st is kept.
4. U6 (ln4) ḫꜥ·ti · reading, n · minor · The reading ḫꜥ·ti did not follow the spelling, which has the tethering rope ṯ. The published hymn to Ra writes the same word ḫꜥ·ṯi (and ii·ṯi, smi·ṯi), and the draft's own say is "khaatji". · reading → ḫꜥ·ṯi. The note's head-word was changed to match. The lemma stays ·ti, the known key.
5. U7, U9 mꜣꜥ-ḫrw · glyph role · style · The oar P8 was coded phon "ḫrw". Every published part codes it log "ḫrw" (Aa11 phon mꜣꜥ, P8 log ḫrw). · P8 → log in both words, tr unchanged. The restored flags on P8 G43 A2 in U9 are untouched.
6. U18 (ln10) ḫd · morph lemma, n · style · The lemma was "ḫd" beside "ḫnti" for its partner verb in U19. Both are infinitives of verbs with a weak third radical, and U19 explains the infinitive t while U18 is silent about it. · lemma ḫd → ḫdi (new key either way). The note now says that this is the infinitive of ḫdi with its ending t unwritten. The reading stays ḫd, following the spelling.
7. U1 (ln1) sbby · n · style · The form was described only as "the form that speaks of action going on". · Named it: "the imperfective participle".
8. U10 (ln6) · n · style · The note explains the run of name-puns but did not point out the one in this line. · Added "here wsr 'might' plays on wsir".

**Counts:** major 0 · minor 4 · style 4 (8 changes).

### Checked and found correct (no change)

- **Splits and joins, and their q.** The draft makes four: ḥr + ib → ḥry-ib (q 0:1-2:3); wꜣḏ / n·k; ta + ḥer + seta-nef → tꜣ-ḥr-stꜣ·n·f (q 0-1:2-3-4:5-6-7:8-9:10, with Budge's numeral 6 inside); di·tw / n·i; and āq per → ꜥq / pri. Each q follows the rule (cut at the boundary, join with "-"), and each split or join is stated in its note.
- **ln and p.** Every unit's ln is the papyrus line of its first word, checked against the packet (lines 1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 19). The numerals 4, 6, 7, 10, 15 that fall inside words are reported in the notes. p is set on U0 (title) and U12 (the new address ind ḥr·k).
- **Rubric and restored.** U0 says dwꜣ is red, and U12 says ind ḥr·k is red. U9 says the oar, chick and man of mꜣꜥ-ḫrw are Budge's bracketed restoration.
- **The restored flag on w75.** The established file carries `"restored": true` on the word. Its own unsure note says that only P8 G43 A2 are inside the brackets, and U1 + Aa11 stand outside. The drafter put `restored` on those three glyphs only. That is the published practice: hymn-to-ra flags only the restored A1 of mꜣꜣ·i, and 125-introduction flags only its bracketed glyphs. The build cannot refuse it. hooks.py `assemble` copies the glyph-level `restored` flag and `validate` compares only the sign sequence, and neither run3/r3lib.py nor r3.py looks at `restored`. No change.
- **Grammatical labels.** I checked these and found them right:
  - the sḏm·n·f forms šsp·n·f, stꜣ·n·f, sk·n·f, ḥqꜣ·n·f;
  - the statives mn (U5, U22), ḫꜥ·ṯi (2nd sg.) and ꜣw (after a noun subject);
  - the participles sbby, wtt (passive, used as a noun), iṯ and ꜥnḫ;
  - the nisbas tpy, imy and ḥry-ib;
  - the prospective di·k;
  - the passives n šnꜥ·tw and iw di·tw;
  - the dual ꜥwy·fy with the dual suffix;
  - the infinitives dwꜣ, ḫd, ḫntyt, ꜥq and pri;
  - the adjective + noun phrases qꜣ ḥḏt, ꜥꜣ snḏ, wsḫ šnbt and nfr ḥr;
  - the "X of Xs" superlatives;
  - the direct genitives iꜣwt itw·f and ḥnty nḥḥ.
- **Glyph roles.** Determinatives all have empty tr. The bolt O34 is tr "z" throughout (sbby, st, ḫsbd, skr). The suffixes are coded suff, including Z1 as ·i in n·i and V13 + M17 as ·ṯi. Complements carry the repeated consonant. The two reeds have tr "y" in pwy, as in the published address.
- **Names and say.** These match the published parts: Osiris, Wenen-nefer / "Wennefer", Abedju, Djedu, Iunu, Neb-er-djer / "Lord of All", Nut, Horus, Ani, "the Osiris, the scribe Ani". The say for "Geb", "Sokar" and "Duat" is the settled modern name. Igeret, Ta-djeser, Ta-her-setanef and Sekhet-Iaru follow the rule. Every other say follows the rule; I checked each word.
- **No Budge-isms.** l and i contain no hath / saith / thee / thou / homage / triumph. Budge's English is quoted only inside notes, and is marked as his. mꜣꜥ-ḫrw is always "vindication" (as a noun). "Hail to you" is the published rendering of ind ḥr·k.

### Considered and refused

- **U11 "The papyrus writes wn-n with two loaves t …; read wnn·f".** Kept. The two t's are not explained, and Budge's untet-f also reads the verb "endure". I see no second reading that the signs and the sense both allow (a noun wnnt "existence" would leave the construction hanging before ḥnty nḥḥ), so the correction formula stands.
- **U1, U11 reading ḥḥ for nḥḥ.** Left. The reading follows the spelling, and the lemma names the word, as with psd/psḏ and iṯy/ity in the hymn to Ra. The note explains this.
- **U0 R17 as ꜣbḏw, U6 / U19 S34 for ꜣb, U13 / U16 unread t's, U22 ꜣḥt / it, U19 ꜥq pri from two staff-bearers, U4 st.** Each is honestly flagged as doubtful or approximate in its note, with (?) in l/i where the rendering depends on it. I found nothing over-claimed. I also found no better reading that the signs support.
- **U9 sk "haul" (Budge's 'toweth') against the known sense "wipe".** Left. The note says the sense is taken from Budge and is uncertain, and l/i carry (?).
- **U10 wsr·f as verb ("he is mighty", Budge).** Refused. The draft's reason is sound: ꜣw would then have no construction.
- **U21 iw di·tw n·i as a wish (Budge "may there be given").** Refused. iw marks a statement. The note gives Budge's view, and the prayer sense survives either way.
- **U17 p: true where the prayer begins (di·k).** Not added. It is not a new speech or chapter: the address that began at U12 goes on.
- **approx on every M8 (w91) and every N21 (w106, w111).** Kept. The established file lists the code once ("approx F16,M8"; "approx N21"), but its unsure notes describe all of them as the same approximate sign ("coded M8 x2, approx"). The build does not compare approx flags.
- **U0 nṯr R8 coded log here, phon in nṯrw (U2).** Left. The published parts use both.
- **U15 "if it is the staff ḏꜥm (S41)".** Left. S40 also writes ḏꜥm in some copies, but the note's doubt is right, and the coding is the establisher's.

### For the glosser (outside this pass)

These lemmas share a key with a known entry of another sense. The build would fill the wrong gloss unless `__broaden__` adds the sense:
- sꜣ (known: protection) — here "son".
- skr (known: to bury) — here Sokar, the god.
- st (known: place, seat; dependent pronoun) — here the doubtful "desert hills".
- ḥry-ib (known: middle, midst, noun) — here the epithet "who is in the midst of, dwelling in".
- ḥqꜣ — used both as the verb "rule" (ḥqꜣ·n·f) and the noun "ruler".

These are new keys: nḥḥ, ḏt, ꜥḥꜥw, tpy, wtt, iry-pꜥt, wrrt, ḥḏt, ḥqꜣt, nḫꜣḫꜣ, iꜣwt, itf, ꜣw, mn, nst, tꜣ-ḥr-stꜣ·n·f, sk, snḏ, ḥnty, iṯi, igrt, ḏꜥm, ḥꜥw, ḫsbḏ, mfkꜣt, iwn, wsḫ, šnbt, tꜣ-ḏsr, ẖrt-nṯr, ḫdi, ḫnti, šnꜥ, dwꜣt, qbḥ, sḫt-iꜣrw, it, bdt.
