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
