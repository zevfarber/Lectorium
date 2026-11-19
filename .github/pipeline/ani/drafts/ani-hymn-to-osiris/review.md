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

## Pass 2

I made the edits by script (scratchpad review2/edit2.py). The checks reuse review1/verify.py, plus a lemma-coverage check. After the edits:
- The glyph sequence (548 signs) still equals source/established/ani-hymn-to-osiris.json.
- No sign, role, tr, q, approx, restored or rubric flag changed. Glyphs are compared field by field against the pre-pass-2 file.
- Every morph g-list covers its word's glyphs exactly once.
- Every lemma in units.json is either in known-lemmas.json or a top-level key of gloss.json.
- gloss.json has no unused key and no key that duplicates a known lemma.
- Every `__broaden__` value begins with the known entry whole, followed by " · ".

The only approx differences are the four pass 1 already kept (M8 at w91, N21 at w106 and w111).

### Changes

Format: unit/entry · field · severity · what was wrong · what was done.

1. gloss `ḫd` → `ḫdi` · key, grammar · **major** · Pass 1 renamed the morph lemma to ḫdi (U18), so the gloss key ḫd was stale and ḫdi had no gloss at all. The entry also called the verb "2-lit". It is ḫdi, a verb with a weak third radical: the unit's note explains its infinitive ḫdt by exactly that. · Removed ḫd. Added "ḫdi — to sail downstream, fare north (verb; infinitive ḫdt; the Nile flows north)".
2. gloss `__broaden__.ḥry-ib` · missing · **major** · The known entry has only the noun "middle, midst; inner parts". U0 uses the word as the epithet "who dwells in" (nṯr ꜥꜣ ḥry-ib ꜣbḏw). Pass 1 flagged this, but there was no broaden entry, so the build would have glossed the epithet as a noun. · Added the known entry whole + " · also who is in the midst of, who dwells in (nisba epithet after a noun or name; …)".
3. gloss `ḥqꜣ` · grammar · minor · The entry said "(verb 3ae-inf)". ḥqꜣ has three strong radicals, so it is not a 3ae-inf verb. · Now "ḥqꜣ — to rule (verb); ruler (noun m.); written with the crook".
4. gloss `wtt` · grammar · minor · The entry said "(verb 3-lit)". A verb whose second and third radicals are the same is not a plain 3-lit verb, and the class label adds nothing. The second clause was a line-bound restatement. · Now "to beget, engender (verb); the begotten one, offspring (passive participle used as a noun)".
5. gloss `ḫnti` · grammar · minor · The entry said "(verb 3ae-inf)". ḫnti has four radicals with a weak last one, so the label is wrong. · Dropped the class: "(verb; infinitive ḫntyt)".
6. gloss `ḥḏt` · Budge form · minor · "Budge: ḥeṭ" is not Budge's form. He prints ḥet' (t' = ḏ). His ṭ is the hand d, so "ḥeṭ" would point a reader to the wrong word. · Changed to "Budge: ḥet'".
7. gloss `nḫꜣḫꜣ` · Budge form, wording · minor · "Budge: khu" uses his English spelling, not his transliteration, which is χu. "reading of the sign alone uncertain" is a doubt that belongs to this line, and the U3 note already gives it. · Now "(noun m.; Budge: χu)".
8. gloss `mfkꜣt` · Budge form · minor · "Budge: mafkia" lacks his ā. He prints māfkia. · Corrected.
9. gloss `tꜣ-ḥr-stꜣ·n·f` · Budge form · minor · "Ta-her-seta-nef" lacks Budge's ḥ. He prints Ta-ḥer-seta-nef, and so does the U8 note. · Corrected.
10. gloss `ẖrt-nṯr`, `sḫt-iꜣrw` · Budge form · minor · Both took Budge's English spelling or mixed it with his transliteration: "Neter-khert" and "Sekhet-Àrui". His transliteration has χ: Neter-χert, Seχet-Àrui. · Both corrected.
11. U17 · n · minor · For the same reason as 10, the note's "(Budge: Neter-khert)" changed to "Neter-χert". All the other Budge forms in the notes already follow his transliteration.
12. gloss `sk` · wording · minor · The entry had "here perhaps …", which ties a general entry to one line. It also had "(Budge: sek)": Budge forms are for names, not common verbs. · Now "to wipe, sweep (verb); perhaps also to drag, tow (?) (sense uncertain; Budge's 'toweth')". The uncertainty is kept, matching l/i "(?)".
13. gloss `it` · wording · minor · "(?)" and "reading of the bare grain sign doubtful" put this line's doubt into the lemma entry. it 'barley' is a sure word. · Now "it — barley (noun m.; often paired with bdt 'emmer')". The U22 note and the "(?)" in l/i still carry the doubt about the reading.
14. gloss `ḏꜥm` · wording · style · "reading of the sign uncertain" is a doubt that belongs to this line. · Removed. The U15 note still gives it.
15. gloss `__broaden__.st` · wording · minor · The new sense was hedged with a guess about this line, "perhaps a short writing of smyt". · Now known entry + " · also, with the hill-country sign, the desert hills, the necropolis (?) (noun; sense uncertain)".
16. gloss `__broaden__.skr` · format · style · Sokar the god is a different word from the verb "bury", but the entry joined the two with "also". · Now "a second word of the same spelling: Sokar, …".
17. U22 ꜣḥt · say · minor · The say was "akhet", but the word has ḥ, which the rule writes h, not kh. · Now "ahet".
18. U8 · i; U10 · n · minor · The name was rendered "Ta-her-sta-nef" in i (U8) and in the U10 note. The say form, and the rule used for every other name in the part (Igeret, Ta-djeser), is "Ta-her-setanef". · Both now "Ta-her-setanef".
19. U8 · n · minor · The note quoted Budge as supplying "'that which existeth [and]'". His English is "{that which existeth [and that which]} not yet hath become". · The note now quotes him exactly and says that he supplies words not in the signs.
20. U15 · n · minor · The note said that "three phrases" are each "a noun followed by the part of the body it qualifies". The third phrase, mfkꜣt ḥr-tp ꜥwy·fy, is a noun with a prepositional phrase, a different construction. · Now: two such phrases, and a third that puts turquoise upon his arms.
21. U21 · l · minor · l had "are-given". The verb is the singular passive di·tw, and i has "Bread is given". · l "is-given".
22. U4 · l · style · l had "the-desert(?)", while i and the note have "the desert hills(?)". · l "the-desert-hills(?)".
23. U16 wsḫ · say · style · The say was "wesekh". The published parts say wsḫt "usekhet" and wsḫ-nmtt "Usekh-nemtet", following the rule w → u before a consonant. · Now "usekh".

**Counts:** major 2 · minor 17 · style 4 (23 changes).

### Checked and found correct (no change)

- **Each unit against the signs and Budge's transliteration.** I checked every glyph role and tr. Every complement repeats a consonant of its sign, and every determinative has an empty tr. The ln of every unit matches the established line of its first word, checked by script. The approx remarks in the notes match the approx flags one by one: every "approximate" in a note is on a flagged sign, and no flagged sign is passed over.
- **Grammar labels.** I re-checked these and found them right:
  - the sḏm·n·f forms (šsp, stꜣ, sk, ḥqꜣ);
  - the statives mn (twice), ꜣw and ḫꜥ·ṯi;
  - the imperfective participle sbby (3ae-inf gemination), the participles iṯ and ꜥnḫ, and the passive participle wtt;
  - the nisbas tpy, imy and ḥry-ib;
  - the prospective di·k;
  - the passives šnꜥ·tw and di·tw;
  - the infinitives ḫd(t) and ḫntyt;
  - the dual ꜥwy·fy;
  - the adjective + noun phrases;
  - the direct genitives and the "X of Xs" superlatives;
  - n with the dative placed before the noun subject (wꜣḏ n·k tꜣwy);
  - nbw agreeing with sbꜣw.
- **Glossary coverage of known lemmas.** n (for / not), m (as), nb (all), ꜥ (hand), ꜣḫ (glory), wsr (power), ḥtp (offering), pr (house), ꜣḥt, kꜣ, tꜣ (land) and imy are each already covered by their known entries. The broaden entries for sꜣ, skr, st, ḥry-ib, mꜣꜥ-ḫrw, ꜥnḫ, ḥr and tp each add exactly the sense used here.
- **Names against the published parts.** Osiris, Wennefer, Abydos/Abedju, Djedu, Geb, Nut, Horus, Sokar, Lord of All, Iunu, Duat, the Osiris the scribe Ani. The l/i of ind ḥr·k, of m-bꜣḥ ꜥ nb-r-ḏr, and of n kꜣ n Wsir match the published parts.
- **No Budge-isms** (hath, thee, triumph, homage, saith) in l or i. No wording of a remembered modern translation.

### Considered and refused

- **ḥr 'upon' coded log inside tꜣ-ḥr-stꜣ·n·f (U8) but phon in U5 and U20.** Left. The published parts code D2 both ways (125-introduction phon, 125-rubric log).
- **say forms that do not insert e in every consonant cluster** (khesbed, mefkat, khentyt, henty). Left. The published parts do the same (khenty, heptu, henqet).
- **The second djed R11 in ḏdw coded det** (125-introduction has D46 comp instead). Left. The sign is different there, and treating the doubled djed as a classifier is defensible.
- **The two reeds coded tr "i i" in iṯy and ḫntyt, against "y" in pwy.** Left. The published hymn to Ra codes iṯy the same way.
- **U8 i "not yet"** (n ḫpr without the t of the sḏmt·f). Kept. The note gives both readings and says the sense is the same.
- **U16 iwn 'pillar' despite the god classifier** (Budge reads it as a name, Àn). Kept. The note states Budge's reading and the doubt is clear.
- **U22 ꜣḥt from two plough-like signs.** Kept. It is honestly flagged as doubtful, with (?) in l/i, and the signs support no better reading.
- **U11 the wn-n-t-t correction, U1/U11 ḥḥ for nḥḥ, U13's unread t.** I re-checked pass 1's reasons and agree with them.
