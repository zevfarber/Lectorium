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
