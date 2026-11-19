# Review — ani-weighing-of-the-heart

## Pass 1

I edited units.json by script (scratchpad review1/edit1.py; checks in review1/verify.py, against a copy of the draft taken before the edits). No sign code, sign order or glyph count changed. After the edits the concatenated glyph sequence (709 signs) still equals source/established/ani-weighing-of-the-heart.json. Every morph g-list is non-empty and covers its word's glyphs exactly once, and every q covers its glyphs once. The rubric, approx and restored flags are unchanged glyph by glyph, and the rubric flags match the established file. Every determinative has an empty tr, and every l has one token per word. I checked each of the 41 units (U0–U40, in draft order) sign by sign against the packet and Budge's transliteration. I checked every grammatical label in the notes, l against the Egyptian, i against l, and say against the rule. I compared names, codings and renderings with the published parts, and lemma keys with known-lemmas.json.

### Changes

Format: unit · field · severity · what was wrong · what was done.

1. U11, U20, U30 pꜣwt · reading, say, glyph tr, lemma, l, i, n · **major** · The draft read the group as pꜣwt, "company, assembly", and glossed it that way. No such word exists. This is Budge's 1895 reading (paut) of the Ennead, psḏt. The loaf X6 writes pꜣwt "loaves, cake-offerings", which cannot be a feminine body of gods that judges and speaks (ꜥꜣt agrees with it in U11). The printed sign, "a circle with a horizontal line across it", is the moon-sign psḏ (N9) as the type renders it. · reading → psḏt, say → pesedjet. X6 stays log; its tr changed pꜣw → psḏ (the code and the approx flags are untouched). Lemma pꜣwt → psḏt. l "the-company" → "the-Ennead". i "company of the gods" → "Ennead of the gods". The U11 note now explains the sign, the reading and Budge's paut, and U20 and U30 point back to it.
2. U16, U37 · n, l, i · **major** · The notes said that "n with the sḏm·n·f is 'did not, has not'". That is the meaning of n + sḏm·f. In the classical language, n + sḏm·n·f says what does not or cannot happen. The published 125-rubric (U3) says exactly this, and the draft's own U17 note gives n + sḏm·f as the past. · Both notes now give the classical sense and add that copies of this time may also use the form for the past. U16: l "could-be-found", i "No wrong of his could be found at all." U37: l "not · speak-I", i "I do not knowingly speak lies."
3. U8 r-gs · n · minor · The note said r-gs "fits the signs as well" as Budge's erma. It does not. The printed sign is Aa15 (m), and gs needs Aa13. · The note now says what is printed, that Budge's erma reads it as printed, and that r-gs takes the sign as the similar Aa13. The papyrus writes r-gs with Aa13 in the rubric of Spell 125. It also says the reading is not sure.
4. U11 · n · minor · The note said that ḏd in ḏḥwty is in red. Only ḏd in is rubric (w71–72); ḏḥwty (w73) is black. · Corrected: "ḏd in in red …; ḏḥwty goes on in black."
5. U13 · i · minor · "In very truth" is Budge's English for m wn mꜣꜥ. · i → "Truly, I have judged the heart of the Osiris."
6. U13 wḏꜥ·n(·i), U27 ii·n(·i), in·n(·i) · reading, say · minor · The unwritten suffix is supported in all three places. Thoth reports in U13 (his speech is headed U11 and goes on with "hear this speech" in U12), and Horus speaks in the first person in U27. The brackets, however, break with the published practice. The hymn to Ra reads mꜣꜣ·n·i, with ·i unwritten, unbracketed, and has the note say so; its morph has no ·i, as here. The say "wedjani" also broke the pattern of wḏꜥ·n "wedjaen" (U30) and ii·n·i "iieni". · Readings → wḏꜥ·n·i, ii·n·i and in·n·i, and say → wedjaeni. The notes keep "the suffix ·i is not written". l keeps "-(I)" to mark the pronoun that is not written.
7. U30 wḏꜥ·n · glyph role (D46) · minor · The draft coded the stray hand phon "d". The reading wḏꜥ has no d, and the note says the hand is not pronounced, so the tr claimed a sound the word lacks. comp does not fit either, because the hand repeats no consonant. · D46 → det, tr "". This is the draft's own treatment of unread signs (W24 and O29 in ḏꜣḏꜣt, R4 in ꜥꜣ). The note now says that the cobra and hand are printed as the familiar pair of ḏd and that the hand is coded as an unread sign.
8. U15, U28 mꜣꜥ · n · minor · The notes called mꜣꜥ in "sp·f mꜣꜥ" and "ib·f mꜣꜥ" "an adjective as predicate". An adjectival predicate stands first, as mꜣꜥ mty does in U22. After its subject, the word is the stative. · Both notes now say "the stative". U15 adds the contrast with U22.
9. U7 · i, n · minor · i "make my name stink(?)" repeated Budge's English ("make to stink"). The note also failed to say that s-ḫ-r is the ordinary spelling of sḫr "overthrow". · i → "Do not make my name foul(?) to the entourage", matching l "make-foul(?)". The note now names sḫr "overthrow, fell" and says that it takes no fish, so the sense is uncertain.
10. U25, U32 · i · minor · "Let there be given to him" is Budge's English (w158–159). · i → "Have offering loaves given to him, …" and "Have bread and beer given to him, …". Both are built from imi + di·tw, "cause that there be given".
11. U40 · l, i, n · minor · l and i had "an Osiris", which is Budge's wording. The published parts render Wsir N as "the Osiris N". · l → "the-Osiris". i → "the Osiris, greatly favoured by the perfect god, …". The note says this is Wsir N with Ani's titles between.
12. U24 · n · minor · The "The papyrus writes … read rdit" sentence stood second, but the conventions want the note to open with it. The note also did not explain n before an infinitive. · I moved the correction sentence to the start. I added that n before an infinitive denies it as a noun ("there is no letting"), and the alternative n rdi·t(w), passive.
13. U25 ꜣḥt · l, i · style · The hymn to Osiris has the same doubtful ꜣḥt mn, and there l and i carry "(?)". Here the note calls the reading doubtful, but l and i did not mark it. · l "a-field(?)", i "a lasting field(?)".
14. U35 imntt, U39 m-ḫt·k, U40 tꜣwy · glyph role · style · R14 was coded log and M3 log. The published parts code imntt with R14 phon imnt, and m-ḫt and ḫt with M3 phon ḫt. The second N16 of tꜣwy was coded log "tꜣ", but published tꜣwy codes it det. · R14 → phon. M3 → phon. Second N16 → det, tr "".
15. U38 snnw · glyph role (second Z1) · style · Of the two strokes of the numeral 2, one was num and the other det. · Second Z1 → num, tr "".
16. U5 ntk · say · style · "entek" put in an initial e that the rule does not give. Published nty is "nety". · say → "netek".
17. U4 · n · style · "after m the verb takes this form, often written with t" makes a general claim. · Now: "takes the form called the negatival complement, here written with t."
18. U9 · l, i · style · l "hearing-your" and i "Good is your hearing" did not match the note, which takes sḏm·k as a sḏm·f subject clause ("good (is it that) you hear"). · l "hear-you", i "How good! It is good that you hear …".
19. U10 · n · style · The note said the gap was "about one group wide". The established gaps entry gives about one and a half groups, with dots beneath. The note also called G41 "the alighting duck pꜣ" without saying that pꜣ is normally the flying duck G40. · Both corrected. The G40/G41 doubt comes from the established reading.

**Counts:** major 2 · minor 10 · style 7 (19 changes).

### Checked and found correct (no change)

- **Joins (5) and splits (4).** Each one is stated in its note, and each q is re-indexed correctly or omitted where it would be a plain left-to-right string (hooks.py).
  - Joins: ḥn + i → ḥn·i (U6); àm + ut → imy-wt (U10); wḏꜥ + n → wḏꜥ·n·i (U13); wḏꜥ + n → wḏꜥ·n (U30); ḏd + n → ḏd·n (U30, across Budge's line 3).
  - Splits: pr / n·k (U6, Budge's numeral 11 inside the group); nfr / wy (U9); di·tw / n·f (U25 and U32).
  - Every join is grammatically required: an n of the sḏm·n·f or of the relative form, a suffix, or a compound title.
  - Every split separates a word from a particle or a dative.
- **The Anubis legend (U10).** The lacuna is the gap after mꜣꜥt in the established file. l "truth-[…]" and i "… what is right […] of the balance" show it in the right place without guessing what is lost. "With the gap, the grammar of the whole is uncertain" says plainly what is doubtful. The "(?)" stays on "give face".
- **ln and p.** Every unit's ln is the established line of its first word. p is on each new speech: U0, U1, U10, U11, U20, U26, U34 and U35.
- **Rubric and restored.** The notes name the red words correctly for U0, U1, U20, U21, U26, U34 and U35 (U11 is corrected above). Budge's brackets are reported in U1 (the woman and man of mwt·i, the ·i of ḫprw·i) and in U34 (n and strokes of ꜣny).
- **Grammar labels.** I checked these and found them right:
  - the negative imperative m with the negatival complement (U2–U4, U7, U8);
  - ntk N, a sentence with no verb;
  - the nisba imy;
  - the participles swḏꜣ, wḏꜥ (after pꜣ), prrt (with the doubled r), iryt (feminine passive used as a noun), mrr and mry·f;
  - the passives gm·n·tw and di·tw;
  - the sḏm·f after imi (wn·i) and after ḏr (wnn·f);
  - the dependent pronoun sw placed before its noun subject;
  - the relative form ḏd·n;
  - n + sḏm·f as the past (U17–U19, U23, U29);
  - the adjectival predicates mꜣꜥ mty (U22) and mty (U31);
  - n + noun "there is no" (U36);
  - the unagreeing wr, nb and pn, each said in its note.
- **Names and say.** These match the published parts: Osiris, Wennefer (Wenen-nefer), Thoth, Horus, Hermopolis / Khemenu, the Osiris, the scribe Ani, mꜣꜥ-ḫrw "true of voice" (Aa11 phon + P8 log, and U1 phon mꜣ D36 phon ꜥ in U40), and lord of the West. Isis, Khnum and Ammit take their settled modern names. Imy-ut, Sekhet-Hetepu and Shenyt follow the rule.

### Considered and refused

- **The bracketed suffixes as such.** The readings are right (see change 6); only the notation was changed. I did not add "The papyrus writes X; read Y" to U13 and U27, because an unwritten ·i is the normal spelling of this period, not a slip.
- **U21 l "ordains(?)-he" against i "… is ordained(?)".** Kept. The note says that the first sign is not clear, that Budge does not read it, and that i gives only the general sense. A closer i would claim more than the signs allow.
- **U12 ḏdt pn (masculine demonstrative with a feminine noun).** Not put under the correction formula. The note states the disagreement, and the sense is not in doubt. It is not a misspelt word.
- **U35 mk with D36 coded det.** Left. The published parts code the arm in mk as phon ꜥ, which also contributes nothing to the reading. det for the unpronounced later spelling is equally defensible.
- **U36 isft, second reed coded comp i.** Left. The note gives the doubt about the sign. Re-coding a sign whose identity is itself uncertain gains nothing.
- **U21 nn: M22 phon n ×2, N35 comp n ×2.** Left. It is the same coding as tꜣ-twnn in the published hymn to Ra.
- **U3 ḏꜣḏꜣt: W24 and O29 coded det, not read.** Left. The 125-introduction reads W24 there as ꜣ, but here both signs are approximate and unidentified, and the note says so.
- **U25 ꜣḥt from O22.** The sign coded is the booth sḥ (Budge's seḥ). The note gives the doubt honestly, and the sense "field" is secure from Budge and the land classifier. Only "(?)" was added (change 13).
- **U5 ḫnmw as the god, not Budge's verb "formeth".** Kept. The reason given in the note is sound.
- **U17 i "food offerings".** This coincides with Budge's English, but it is the plain sense of šbw, not a phrase. Likewise "I have come to you", "like the followers of Horus" (the published hymn to Ra has the same) and "There is no wrong in my body" are what the grammar gives.
- **ḏd in rendered "Said by".** Left. l is "said · by" as in all published parts. The i of the published parts varies ("Words spoken by", "By").
- **U6 ḥn·i, U13 wḏꜥ·n·i with no q after a join.** Left. hooks.py omits q for a plain left-to-right string.
- **U1 restored flags on B1 and A1 of mwt·i.** Left. The word's own unsure note puts both in brackets (the layoutNote mentions only A1).
- **Outside this part:** the published hymn to Ra (U10) reads the same X6 + t + three gods as pꜣwt-nṯrw "the cake-offerings of the gods". In the light of change 1, "who made mankind and the Ennead of the gods of the south, north, west and east" should be reconsidered there. This is for the owner; I did not edit it.

### For the glosser

- Lemma key renamed: **pꜣwt → psḏt** (U11, U20, U30). gloss.json's pꜣwt entry should become "psḏt — the Ennead, the company of nine gods (noun f.; psḏt nṯrw 'the Ennead of the gods'; Budge: paut)".
- No other key was added or renamed.
- ꜥꜣ is used in U40 as the adverb "greatly" (ḥsy ꜥꜣ). The known entry has "(adverb) here, hither" only, so it may need `__broaden__`.

## Pass 2

I edited units.json and gloss.json by script (scratchpad review2/edit2.py; checks in review2/verify.py, against copies of both files taken before the edits). No sign code, sign order or glyph count changed. After the edits the concatenated glyph sequence (709 signs) still equals source/established/ani-weighing-of-the-heart.json. Every morph g-list is non-empty and covers its word's glyphs exactly once, every determinative has an empty tr, and the rubric, approx and restored flags are unchanged glyph by glyph. Every l has one token per word. gloss.json keys now equal the units' lemma keys minus known-lemmas.json (26 entries), and each `__broaden__` value starts with its known entry copied exactly. I read all 41 units again sign by sign against the packet and Budge's transliteration, every grammatical label in the notes, l against the Egyptian, i against l, say against the rule, and codings and names against the six published ani-* parts. I checked every gloss entry against the text and against every use of its lemma in the part, and every known entry used here for senses this part needs that it lacks.

### Changes

Format: unit/key · field · severity · what was wrong · what was done.

1. gloss pꜣwt · key, value · **major** · The entry still glossed pꜣwt "company, cycle (of gods)", a word that does not exist, after pass 1 renamed the lemma to psḏt. The build would have found no entry for psḏt and published a ghost entry. · pꜣwt removed. psḏt added: "psḏt — the Ennead, the company of nine gods (noun f.; psḏt nṯrw 'the Ennead of the gods'; Budge: paut)".
2. gloss sḫr · value · minor · "make foul … perhaps 'make stink'" is Budge's English ("make to stink"). It also contradicted the U7 note, which says the signs ordinarily spell sḫr "overthrow, fell". · "sḫr — to overthrow, fell (causative verb, from ḫr 'fall'); to harm, bring to ruin (?) (sense uncertain)".
3. gloss __broaden__ ꜥꜣ · new · minor · U40 ḥsy ꜥꜣ uses ꜥꜣ as the adverb "greatly". The known entry has only "great" and "here, hither". · Known entry copied whole + " · also greatly, very (adverb, after an adjective or participle: ḥsy ꜥꜣ 'greatly favoured')".
4. gloss __broaden__ imi · new · minor · The known entry is "give! (imperative of rdi)" only. In U25, U32 and U39 imi is "cause, let" before a sḏm·f (imi di·tw, imi wn·i), and the l and i say "cause", "have … given", "let me be". · Known entry + " · also cause, let (before a sḏm·f …)".
5. gloss __broaden__ r · new · minor · The known entry has "to, towards, into, at". Here r·i is "against me" five times (U2–U4, U8) and r·f is "concerning him" (U14, U30). · Known entry + " · also against (of hostility …); concerning, about …".
6. gloss __broaden__ grg · new · minor · The known entry is a verb only ("to speak falsehood"). In U8 and U37 grg is the noun "lies", the object of ḏd. · Known entry + " · also lies, falsehood (noun; ḏd grg 'speak lies')".
7. gloss bṯꜣ · value · minor · "rebel" is not a sense of bṯꜣ. The entry also pinned itself to a line ("bṯꜣ·f 'his wrong'"). · "bṯꜣ — to do wrong, sin (verb); wrong, wrongdoing, crime (noun)".
8. gloss ḫnmw · value · minor · The entry said "Budge reads the word as the verb χnem 'formeth'". That is a remark on one line, and it is not Budge's spelling of a name. The entry also offered an unsupported etymology ("ḫnm 'join, fashion'"). · Both removed: "ḫnmw — Khnum, the ram-headed god who shapes the bodies of the newborn on a potter's wheel (god's name)".
9. gloss ꜣst · value · minor · The entry gave "'seat, throne'" as the meaning of the name, but the name is not transparent. Only its writing uses the seat sign. · "(goddess's name, written with the seat sign; Budge: Àuset)".
10. gloss wpi · value · minor · The entry lacked "judge", the sense this part uses (wp-mꜣꜥt, U11). The example also stood outside the grammar bracket. · "wpi — to open, part, separate; to judge (between) (verb 3ae-inf.; wp mꜣꜥt 'who judges what is right')".
11. U25 · n · minor · The note said that the first sign "may be the pool with lotus flowers that writes ꜣḥ". That sign writes šꜣ, and nothing printed here writes ꜣḥ. · Now: "Budge's seḥ takes the first sign as the booth sḥ, which gives no word for field here; no sign that writes ꜣḥ is clearly printed, and the reading is doubtful."
12. U30 · n · minor · Pass 1's insertion broke the sign list: "like the unread signs in ḏꜣḏꜣt, the stand-like sign wḏꜥ, and the n …" made wḏꜥ and the n into unread signs. · Split into two sentences: "… like the unread signs in ḏꜣḏꜣt. Then come the stand-like sign wḏꜥ and the n of the sḏm·n·f, …".
13. U37 · n · minor · The note still opened "n ḏd·n·i 'I have not said'", the past sense the same note then rejects for the classical language. · Opening gloss → "'I do not say'". The later remark that copies of this time may mean "I have not spoken" stays.
14. U32 pri · reading, say, n · minor · The note calls the word the infinitive "its t unwritten", but the reading was pri. Elsewhere in the part the reading carries unwritten letters (ꜥwt·i, ḥsyw, ḥnqt), and the same infinitive in U25 and U28 is prt. · reading → prt, say → peret, and the note now names prt.
15. gloss __broaden__ wḏꜥ · removed · style · The known entry ("to judge, separate (verb)") already covers every use here. The broadening only restated it with a line-pinned example (wḏꜥ·n 'has judged'). · Removed.
16. gloss rq · value · style · The example was pinned to a line (rq·k 'your hostility'), a stray "(?)" came after the grammar, and "turn aside" is unsupported. · "rq — to oppose, be hostile (verb); opposition, hostility (noun)".
17. gloss ḥn, imy-wt, ntk, snnw · value · style · ḥn: "Budge's guess for a doubtful sign" is about this line. imy-wt: "noun m." for a god's title, and "wrappings" was added. ntk: archaic "thou". snnw: the example stood outside the grammar bracket. · ḥn "(verb; reading and sense uncertain)". imy-wt "(god's epithet; …)", "wrappings" dropped. ntk "you", "masculine singular". snnw example moved inside the bracket.

**Counts:** major 1 · minor 13 · style 3 (17 changes).

**Gloss after this pass:** 26 new entries. 8 broadened keys: m, ḏr, sḫm and sš kept; ꜥꜣ, imi, r and grg added; wḏꜥ dropped.

### Considered and refused

- **R8 coded log in nṯr (U8, U29, U40), nṯrw (U30) and nṯrt (U29), but phon in nṯrw (U11, U20).** Left. A lone R8 writing the whole word is a logogram by the conventions' own definition. The published parts are themselves mixed (phon in most, log in two), so neither choice is an error.
- **U8 r-gs without the opening "The papyrus writes X; read Y".** Left as pass 1 wrote it. It is not settled whether the scribe or Budge's type is at fault, and the note says plainly that the reading is not sure.
- **U9 wy say "uy" (published "wy" for the lake-word wy).** Left. "uy" follows the rule (w → u when no vowel follows). The published form belongs to another lemma.
- **U28 prt as an infinitive after ib·f mꜣꜥ.** Left. A stative of pri would not take t with a masculine subject, and the note's reading ("coming forth") is defensible.
- **Known mꜣꜥ "(adjective)", used here as the stative (U15, U28) and in m wn mꜣꜥ (U13).** Not broadened. The stative belongs to the adjective-verb, and "true, right" covers the sense.
- **Known ḫr "to, near, with (of persons)", rendered "against" (U29), "towards" (U23) and "before" (U40).** Not broadened. These are contextual renderings of the same preposition used of persons.
- **U11 i "who judges what is right for the great Ennead" against l "of".** Kept. The genitive n allows "for", and i is meant to be real English.
- **ini "3ae-inf." and šm "2-lit." in the glossary.** Kept. Both are the standard verb classes.
- **sš __broaden__ adds the noun "writing, record".** Kept. U30 renders sš that way (with doubt), and the known entry has only the verb "write".
- **U21, U6 ḥn·i, U10 gap.** Left as pass 1 found them. Each note already says plainly that the reading is doubtful.
