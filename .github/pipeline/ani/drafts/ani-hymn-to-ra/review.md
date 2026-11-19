# Review — ani-hymn-to-ra

## Pass 1

I edited units.json by script (scratchpad review1/edit1.py; checks in review1/verify.py). No sign code, sign order or glyph count changed. After the edits the concatenated glyph sequence (810 signs) still equals source/established/ani-hymn-to-ra.json. The rubric, approx and restored flags still match the established file sign by sign. Every morph g-list is non-empty and covers its word's glyphs exactly once. Every q is unchanged.

Units are numbered U0–U34 in draft order, with the papyrus line and the draft word range (the draft has 276 words, w0–w275, after the drafter's splits and joins).

### Changes

Format: unit · field · severity · what was wrong · what was done.

1. U28 (ln17, w225–w233) mꜣꜣ·i · morph, n · **major** · The restored word had a morph entry `{"lemma": "mꜣꜣ", "g": []}`. Its only printed sign is a faint A1 (Budge's outline for damage), coded suff ·i, restored. A morph entry with no glyph cannot be displayed and may be rejected by the build. · I took the honest reading: the one sign is the suffix ·i, and the verb has no sign at all. Budge supplies [maa] in his transliteration only. morph is now `[{"lemma": "·i", "g": [0]}]`. The reading stays mꜣꜣ·i (the word meant), l stays "[see] · I", and the note now says the verb is restored, has no sign, and that only ·i is analysed.
2. U3 (ln2, w27–w34) psd · n, l, i · **major** · psḏ mwt·k was translated "lighting up your mother", which treats psḏ as transitive and makes it a participle or adverbial form. No such form was named, and nothing is written for it ("taken as describing how he rises"). As written, verb + noun is a sḏm·f with a noun subject. · The note now gives the sḏm·f, "your mother shines", and states Budge's transitive "making bright thy mother" as the alternative that needs an unwritten form. l "shining" → "shines". i → "You appear in glory and rise, and your mother shines; you have appeared as king of the gods."
3. U25 (ln15, w200–w208) sp·f ḫpr · n, l, i · **major** · ḫpr after sp·f was analysed as a noun genitive, "its time of coming into being". A noun with a suffix cannot take a direct genitive after it: that would be sp ḫpr·f. · ḫpr is now read as the stative after a noun subject, a clause of circumstance: "its occasion having come about" / "when its time came". The doubt is kept. l "of-coming-into-being" → "having-come-about". i → "I have seen the abdju-fish when its moment came, …".
4. U30 (ln20, w242–w248) gm·f · n, l, i · **major** · The note said "as it stands, 'it finds'", that the passive needs gm·tw·f, and that "the tw may have been left out". l had "finds · it(?)". This is wrong. The passive sḏm·f takes a suffix pronoun as its subject and need write no ending, so gm·f is a normal passive, "may it be found", and nothing is missing. The active reading fails anyway, because it leaves the verb without an object. · The note now gives the passive sḏm·f. l → "may-be-found · it". The query is removed from i.
5. U33 (ln26, w264–w270) šsp·i · n, l, i · **major** · This is the same error as 4: "may-receive(?)", plus the claim that the passive needs šsp·tw·i. · The note now reads the passive sḏm·f with suffix subject, "may I be received", and states the active "may I receive" (no object written) as the rejected alternative. l → "may-be-received · I". The query is removed from i.
6. U4 (ln3, w35–w42) iry · n · minor · "What the two reeds mark is not clear" left out the obvious grammatical candidate. · Added: in 3ae-inf verbs like iri, the prospective sḏm·f (wish or future) is often written with y (iry·f), which would give "may mother Nut set …". The plain statement is kept, as fitting the description around it.
7. U7 (ln5, w58–w64) ꜥnḫy · n · minor · The two reeds were called "the ending of the participle". ꜥnḫ is a strong triliteral verb, and its participle has no regular -y. · The note now says it is the participle "living", agreeing with bꜣ, and that what the reeds mark is not clear.
8. U10 (ln6, w88–w96) rsy mḥtt imntt iꜣbtt · n · minor · These were called "nisba adjectives describing the gods". Adjectives agreeing with masculine plural nṯrw would be rsyw, mḥtyw, and so on. mḥtt, imntt and iꜣbtt (t t) are the feminine nouns for the regions. · The note now says they name the four quarters and follow nṯrw as direct genitives. The lemmas already treat imntt and iꜣbtt as nouns, and l/i were already right.
9. U10 pꜣwt-nṯrw · n · minor · The "cake-offerings" reading was given without doubt. The loaf also writes pꜣwt "primeval time" (pꜣwty "primeval one"), and "who made mankind and the primeval gods" fits a creator epithet just as well. · Added a sentence saying the choice is not certain. The reading is kept, since it matches the known lemma.
10. U10 tmmw · glyph role, n, say · minor · The reading tmmw (Budge tememu) has two m's, but the owl G17 was coded comp, which would give tmw. · G17 → phon "m". The note now says "the owl for the second m". say "temmu" → "tememu" (rule: e between consonants).
11. U12 (ln8, w109–w117) ꜥḏt · n · minor · The note did not say that V26 also reads ꜥnḏ, or that the morning bark is usually mꜥnḏt. · Added. ꜥḏt is kept as what the signs and Budge give.
12. U22 (ln13, w174–w184) · l · minor · l had "his-state(?)" but i had "his place(?)". · l → "his-place(?)". The note still gives "state" as the alternative.
13. U24 (ln14, w192–w199) sḥtm·n·i · n · minor · I judged the sḏm·n·f run (sḥtm·n·i, mꜣꜣ·n·i ×2, šsp·n·i). The completed reading is right: the n is written consistently four times, and a sḏm·n·f is never a wish. But the note left out the reading that best removes the "odd change of form", namely the circumstantial sḏm·n·f ("when I have destroyed Apep"), tied to the wishes before it. · Added that sentence. l/i are unchanged.
14. U25 ꜣbḏw · n · minor · The note said "The papyrus writes ꜥnḫ-b-ḏw". But S34 is an approximate code for an odd sign in Budge's type, so nothing shows that the papyrus has the ankh. · The note now says that Budge's type gives a sign like the ankh (coded approx) where ꜣb is expected, and that the print cannot show whether the papyrus or only the type has the odd form. The correction to ꜣbḏw is kept: the fish classifier and the context allow only this reading.
15. U25 mꜣꜣ·n·i · n · minor · The "papyrus writes mꜣꜣ·n; read mꜣꜣ·n·i" correction is kept. The note now adds that ·i is often left unwritten in copies of this time, so this is hardly a slip.
16. U28 dgg · n · minor · No form or subject was given for dgg, which has no suffix. · Added: it is taken as a second sḏm·f after di·f, parallel to mꜣꜣ·i, with ·i unwritten.
17. All words with O34 (psd, ꜥwy·s, wn·sn, mꜣꜣ·n·sn, sp·f, s, mr·s, sktt; 8 glyphs) · glyph tr · style · The bolt was transcribed "s" / "·s". The conventions and every published part write the bolt as z in tr (O34 phon "z", suff "·z"). · Changed to z / ·z. Readings keep s, as the published parts do (sp·i).
18. say · style · bꜥḥ "beah" → "bah"; ḥꜥꜥ "heaa" → "haa"; ꜣbḏw "abdju" → "abedju" (the published Abydos is "Abedju"). (tememu: see 10.)

**Counts:** major 5 · minor 11 · style 2 (18 changes).

### Checked and found correct (no change)

- **Split and joined groups and their q.** The draft makes 12 splits and joins: ḥtp-nṯr, ind / ḥr·k, iry / n·k, šsp / tw, ḥpt / tw, pꜣwt-nṯrw, dwꜣ / tw ×2, nḥm·n, mꜣꜣ·n·sn, di·tw / n·i, iry·tw / n·i. Each re-indexes q by the published rule: a split cuts at the boundary, and a join concatenates with "-". Every other q equals the established file's.
- **ln and p.** Each unit's ln is the papyrus line of its first word. Budge's numerals 12, 19, 23 and 26 inside wrt, swtwt, di·tw and ḏꜣ are reported correctly. p is set on U0 (title), U2 (Ani's speech to Ra) and U9 (second speech, to the gods).
- **Rubric.** w0, w2–w6, w9, w18 and w19 are red, as in the established file, and U0, U1, U2 and U9 each say so.
- **The pronoun-object order** (šsp tw mꜣnw, ḥpt tw mꜣꜥt, dwꜣ tw ḥryw / ẖryw) is analysed correctly as verb + dependent pronoun + noun subject. A passive dwꜣ·tw would wrongly make ḥryw the ones adored.
- **The statives** ii·ṯi, ḫꜥ·ṯi (2nd sg.), rdi·w, ḫr, qꜣs (3rd m. sg. after a noun subject); **the participles** wḏꜥw, ddw (imperfective of rdi), ir; **the relative form** mrr·f; **the passives** nis·tw, di·tw, iry·tw (iry·tw correctly shows the y of the 3ae-inf prospective); **ḥr + infinitive** (stwt·f ḥr bꜥḥ) and **m + ḥꜥꜥ**; **the infinitive** with a genitive subject (hrw ḏꜣ nṯr). All are labelled correctly.
- **Names and lemmas against the known list.** wsir, rꜥ, ḥr, ḏḥwty, ꜣny, mꜣꜥ-ḫrw, ind, ·ti, pꜣwt-nṯrw, ḥtp-nṯr, imntt, rsy, mḥtt, m-bꜣḥ, šmsw, wiꜣ, ḏꜣi, sḏm·n·f and sḏm·tw·f all use the known keys. itn uses the known key, with reading iṯn following the spelling, the same practice as psd/psḏ. ity is new, so no key conflicts. Khepri, Tatenen, Horakhty, Manu, Apep and Iah do not occur in the published parts. Their say forms are the settled modern names or follow the rule.
- **No Budge-isms.** l and i contain no "homage", "saith", "thee/thou" or "triumphant". mꜣꜥ-ḫrw is always "true of voice" or "vindication". I found no phrase that looks borrowed from a modern translation.

### Considered and refused

- **U3 nṯrw written with t and plural strokes (nṯrwt) → nṯrw.** Kept. nswt nṯrw "king of the gods" is the fixed epithet, and "king of the goddesses" would make no sense here, so the sense allows only one reading.
- **U9 ḏfꜣw with the pintail (sꜣ) for ꜣ.** Kept. kꜣw ḏfꜣw is a fixed pair. The substitute-sign coding (G39 phon ꜣ) follows the published practice (štꜣw with W24 phon ꜣ).
- **U30 wdb written b-w-d.** Kept. wdb ḫt "reversion of offerings" is a set term, and the order is probably a graphic arrangement of small signs. The m-ḫt "after" alternative is already in the note.
- **U28 iꜥḥ with ꜥ left out.** Kept. The classifier (a god with disk and crescent) settles the word.
- **U24 sḥtm·n·i, U25–U27 mꜣꜣ·n·i, šsp·n·i as wishes ("may I …", Budge).** Refused. Middle Egyptian has no prospective sḏm·n·f, and the n is written four times. See change 13.
- **U24 Q1 inside sḥtm coded det and not read.** Left. No value of the seat fits, and the note says so. Recoding it as an unread phon would claim more than the print shows.
- **U14 mnt "daily" with the arm ꜥ and no m.** Left. The reading does not account for D36, and the note already says so; l/i carry "(?)". No better word fits the signs.
- **U2 Z4 in ii coded det.** Left. The published parts use Z4 det 10 times. phon y (the iy spelling) would be equally defensible, and this is not worth a change.
- **U24 ꜥꜣ "donkey" with an unexplained w; U27 ḥꜣtw with two w's and pḥwyt with a final w not in the reading.** Left. Unread extra signs keep phon with their own value, as in the published parts.
- **U11 iṯy (reading) vs ity (lemma); U10 tꜣ-twnn vs tꜣ-ṯnn.** Left. The reading follows the spelling and the lemma names the word, consistent with psd/psḏ and iṯn/itn.
- **about: "his wife Thuthu" in the vignette.** Left. It is a plain statement about the plate, not translation wording.
- **U1 in "by" for Budge's àn "behold".** Left. This is the title formula (dwꜣ rꜥ … in N), and the note gives the doubt about W25.

### For the glosser (outside this pass)

Several draft lemmas share a key with a known entry of another sense, so the build would fill the wrong gloss unless `__broaden__` adds the new sense:

- ḥpt (known: door-post) — here "embrace"
- wḏꜣ (known: proceed) — here "be sound, prosper" in ꜥnḫ wḏꜣ snb
- tr (known: enclitic particle) — here "time, season" (trwy)
- ꜣbḏw (known: Abydos) — here the abdju-fish
- ḫt (known: thing) — here "wood, board"
- ꜣḫ (known: spirit) — here "glory, effectiveness"
- ꜥ (known: arm) — here "region / state(?)"
- ḫnm — here "join, reach"
- mi (known: "come!") — here the preposition "like"
- s (known: man) — here the unexplained single s; the morph has its own gloss
- mꜣꜥt — here also the goddess Maat
- rsy — here also the noun "the south"
- ·w — new: the 3rd m. sg. ending of the stative

## Pass 2

Edits made by script (scratchpad review2/edit2.py), checks in review2/verify.py and review2/lem.py. After the edits the concatenated glyph sequence (810 signs) still equals source/established/ani-hymn-to-ra.json. Rubric, approx and restored flags match sign by sign. Every morph g-list is non-empty and covers its word's glyphs exactly once. No sign, role, tr or q was changed. Every lemma in units.json is in known-lemmas.json or is a top-level key of gloss.json. gloss.json has no unused keys and no key that duplicates a known lemma. Every `__broaden__` value begins with the known entry, copied whole, followed by " · ".

### Changes

Format: unit/entry · field · severity · what was wrong · what was done.

1. U25 `s` (the lone bolt) / gloss `__broaden__.s` · morph lemma, gloss · **major** · The broaden entry gave `s` "a second word of the same spelling: a lone s of unclear sense". That is a placeholder, not a word of the language. Without it, the part's glossary would list s "man, person" for this sign. · Removed the broaden entry. The morph lemma is now the known `·s` (suffix 'it, its'), which is Budge's reading ("its") and the note's "perhaps". The morph keeps its own gloss: "a single s, not understood here (perhaps the suffix "its")". The reading, l ("s(?)") and the note are unchanged.
2. gloss `ḫft` · **major** · The entry had "Budge: khefti 'when'". Budge prints χeft, and Budge brackets are for names. The entry also ran prepositional and conjunctional uses together. · Changed to "in front of, facing; in accordance with; at the time of, when (preposition; also before a verb form)".
3. gloss `mnt` · **major** · "also thigh (noun f.)" was added from memory and is not secure lexicon. "meaning uncertain here" ties a general gloss to this one line. · Changed to "mnt — daily (adverb; Budge: ment)". The doubt about the signs stays in the U14 note.
4. U22 · l, i, n · minor · l and i had "his place(?) of yesterday". No noun ꜥ 'place, region' is known: that is Budge's guess. ꜥ 'state, condition' is attested. · l "his-state(?)", i "he has come to his state(?) of yesterday". The note now says Budge's 'region' is a sense the word is not known to have, and that 'state' is the reading taken. The query is kept. The gloss `ꜥ` broaden changes to match (13).
5. U10 · l · minor · l gave "southern · northern · western · eastern". Pass 1 rewrote the note to make these the feminine nouns for the quarters, followed by a direct genitive, but l still showed adjectives. · l "of-the-south · the-north · the-west · the-east". i already had this.
6. U0 · n · minor · The note called N27 in ꜣḫt "approximated in Budge's type", but the sign has no approx flag (the flag is on N27 in ḥr-ꜣḫty, U7). · Removed the claim.
7. U5 · n · minor · The note said šsp O42 was "approximated in Budge's type", but it is not flagged approx. · Removed the claim.
8. U12 · n · minor · The note said A53 in irw and V26 in ꜥḏt were "approximated in the type", but neither is flagged. Only the boat P3 is. · Removed both claims. The note on the boat is kept.
9. U10 · n · minor · The note put "(approximated in the type)" on the rushes M22, which are not flagged. The approximate sign is the plumed god A40. · Moved the remark to A40.
10. U24 · n · minor · The note called F9 in ꜣt "approximated", but it is not flagged. Only the packet's UNSURE applies. · Now "(an animal head not clear in the print)".
11. gloss `pḥ` · minor · The second sense "hindquarters, rear, end (noun m.)" came from memory. The standard noun is pḥwy, which is already a known lemma (U27). · Removed. The entry is now "to reach, arrive at, attain (verb)".
12. gloss `·w` · minor · "also the plural ending of nouns and adjectives" is wrong under a lemma for the stative ending. Plural -w is never analysed as a separate morph. · Removed.
13. gloss `__broaden__.ꜥ` · minor · "also region(?), state, condition (noun f.; sense uncertain)" gave Budge's unattested 'region', a gender that is not secure, and a line-bound hedge. · Now known entry + " · a second word of the same spelling: state, condition (noun)".
14. gloss `__broaden__.wḏꜣ` · minor · "to be content, well-disposed" belongs to wḏꜣ-ib, not to wḏꜣ. Also, "be sound" is a separate word, not an extension of "proceed". · Now known entry + " · a second word of the same spelling: to be sound, prosper (verb; ꜥnḫ wḏꜣ snb …)".
15. gloss `__broaden__.ḫt` · minor · ḫt 'wood' was marked noun f. That word is masculine; the feminine is ḫt 'thing'. · "wood, tree, stick, a wooden board (noun m.)".
16. gloss `tꜣ-ṯnn` · minor · "'the Land that rises'" gave an etymology as if certain. The Budge form "Ta-tunen" does not match the packet (Ta - tu - nen) or the U10 note (Ta-tu-nen). · Now "Tatenen, god of the land that first rose out of the waters, worshipped at Memphis (god's name; tꜣ 'land'; Budge: Ta-tu-nen)".
17. gloss `nwt` · minor · "'sky'" was given as the meaning of the name, which is not transparent. · Removed.
18. gloss `iꜣbtt` · minor · The tail "iꜣbty 'eastern'" conflicts with the known lemma iꜣby, which U0 uses. · Removed. The entry is now "the east, the eastern quarter where the sun rises (noun f.)".
19. gloss `ꜥḏt` · minor · "Adjet, the morning bark" presented ꜥḏt as an established name. The note says it is the reading of the signs and that the usual name is mꜥnḏt. The Budge form āṭet is his English: his transliteration is āṭtet. · Now "the sun's bark of the day, the morning bark (boat name; the reading follows the signs: the morning bark is usually named mꜥnḏt, also ꜥnḏt; Budge: āṭtet)".
20. gloss `ḫpri`, `ḥr-ꜣḫty`, `sktt`, `ḥwt-sr` · Budge spelling · minor · These were taken from Budge's English column or partly anglicised (Kheperà, Ḥeru-khuti, Sektet, Ḥet-ser). The convention and the known entries (Àusàr, Àbṭu, Teḥuti) use the transliteration column. · Now χeperà, Ḥeru-χuti, sektet and ḥet ser. ḥwt-sr also gets "at Heliopolis", as in the U18 note.
21. gloss `wdb` · minor · "the turning over of offerings" did not match the units ("reversion of offerings"). · Now "wdb ḫt 'the reversion of offerings', …". The second word "shore, riverbank" is kept as standard lexicon, in the "a second word of the same spelling" format.
22. gloss `ꜣḫt`, `int` · style · The second words were written as "also …" or with redundant wording. · Both now use the "a second word of the same spelling:" format. Their senses (inundation season, valley) are standard and kept.
23. gloss `nyny`, `ḥꜣt`, `iꜥḥ`, `ḥwt-bꜣ`, `__broaden__.rsy` · style · nyny was tied to "raised arms", while this classifier holds the arms forward. iꜥḥ described the classifier of this one writing. ḥwt-bꜣ had "a sacred sanctuary". rsy had a redundant "(noun; rsy 'the south')". ḥꜣt split its senses with "· also". · All tightened. No sense was added or removed.

**Counts:** major 3 · minor 18 · style 2 (23 changes).

### Checked and found correct (no change)

- **The units pass 1 changed.** U3 psḏ (sḏm·f with noun subject), U25 ḫpr (stative after sp·f), U30 gm·f and U33 šsp·i (passive sḏm·f with suffix subject), U28 mꜣꜣ·i (morph on ·i only, restored flag kept), and U10 tmmw (G17 phon m). All are right, and their l, i and n agree.
- **Grammar labels throughout.** These are labelled correctly: stative endings (·ṯi, ·w, unwritten), sḏm·n·f and sḏm·tw·f morphs, the relative form mrr·f, the imperfective participle ddw, the nisbas ḥry, ẖry and iry, the infinitive with a genitive subject, ḥr + infinitive, n + infinitive 'without', and the dual ꜥwy.
- **Second senses kept as standard lexicon:** int 'valley', ꜣḫt 'inundation season', ꜣḫ 'glory, effectiveness', ḥpt 'embrace', tr 'time, season', ꜣbḏw 'abdju-fish', mi 'like', mꜣꜥt the goddess, rꜥ 'sun, day', wdb 'shore', šps 'precious', and ḥꜣt 'beginning'.
- **Unsure items kept.** iꜥḥ 'moon, Iah' and ḥwt-sr are right as entries. ḥꜣt is right; the note gives the doubt about "prow".
- **No Budge-isms and no remembered modern wording** in l or i.

### Considered and refused

- **U2 reading `ind` → inḏ** (the tr has nḏ and the say form is "inedj"). Kept: the published ani-125-address uses reading "ind" with the known lemma "ind".
- **Budge brackets on common nouns** (stwt "satetu", ḥmw "ḥemu", tmmw "tememu", mnt "ment"). Kept: the published entries do the same (ḥpt "ḥeptu", "qebt", "pait").
- **say for ḫꜥ·ṯi "khaatji" next to ḫꜥ·k "khaek".** Left: the rule allows either, and this is not a reading question.
- **ꜥwy·s with the second arm coded det.** Left: it is coded the same way in U4, U16 and U26, and reading the repeated sign as a marker of the dual is a defensible analysis.
