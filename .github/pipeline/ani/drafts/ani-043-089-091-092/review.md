# Review — ani-043-089-091-092 (Spells 43, 89, 91 and 92, Plates 17–18)

## Pass 1

Method. Every unit was read against the packet word by word through a merged view (scratchpad `r1/view.py`): each word's glyphs with role and tr, its morph lemmas, and the packet words it covers with Budge's transliteration, English and flags. The approximate codes the packet flags were compared by script with what each note says (`r1/approx.py`). House spellings, roles, say forms and renderings were checked against all published `ani-*.json`, mainly 044-045-046-050-093, 026-030b, 029-027-058-059, 017-a…f, 018-b, 125-address and the model. No modern translation was opened or recalled.

All edits were made by script (`r1/edit.py`). Before it replaces anything, the script checks the old value: each text replacement must match exactly once, and each glyph's sign, role and tr is checked first. The file was written back with json.dumps(ensure_ascii=False, indent=1), the draft's own format, and still has no trailing newline. No glyph code was changed or moved, and no word was joined or split. After the edits, `check.py` and a comparison with the draft confirmed:
- the 1550 sign codes, joined in order, equal the packet's sequence;
- only 4 glyphs differ from the draft, all in role or tr;
- every `q` indexes its word's glyphs once, and every morph `g` covers them once;
- every det has an empty tr and no other role has one, and every O34 carries z;
- `ln`, `rubric` and `restored` match the packet;
- there are no `s`/`t` fields and no Budge-ism in `l`, `i` or `about`.

Counts: 0 major, 19 minor, 6 style.

### Changes

- U0 · n · **minor** · šꜥd after rdit was called "the sḏm·f with tp s as its subject". An active sḏm·f would make the head the one that cuts. · Now the passive sḏm, with one sentence on why.
- U1 · n · **minor** · The note opened "The papyrus writes n; read in". The house treats in written with water n alone as a writing, not a slip (125-address U85), so the formula does not apply. · The ꜣny dittography formula now opens the note. in is described as written without its reed, as in the Address.
- U2 · n · **minor** · The note said the sḏm·n·f rdi·n·f would have "no subject", but ·f would be its subject. M3 and D54 are approximate in the packet and the note did not say so. The low hooked U15, which recurs throughout the part with no letter in Budge, was given as a plain classifier. · The argument is corrected: ·f would refer to no one named before it. M3 and D54 are now marked approximate. One sentence now says the value of U15 is not clear.
- U5 rnp·kwi · glyph 3 (M17) · **minor** · comp i, but no multiliteral sign in the word carries i (M4 is det). · → phon i.
- U10 in·tw · glyph 1 (N35) · **minor** · comp n, but a single water n is not a multiliteral sign. · → phon n. The formula nn·tw → in·tw is kept (see Refused).
- U14 nw · glyph 0 (N35), n · **minor** · Water n was phon before U19 nw. In 044 the house tags N35 as comp n before U19 (nwd, nwḥ). The note claimed "as the house writes nw elsewhere" and did not say why it departs from Budge's ennu. · N35 → comp n. The note now cites nwd/nwḥ, gives Budge's ennu, and notes that in Spell 17 the same group writes nn 'these', which gives no sentence here.
- U15 · i · **minor** · `l` has the sḏm·n·f "have-let-you" but `i` had the future "you shall let". · i → "(then) you have let(?)". The note already says the form is doubtful.
- U17 · l, n · **minor** · `i` had "bring (it) to the sky(?)" with no "to" in `l`. N1 in ḥrt is approximate and the note did not say so. · l → "(to)-the-sky(?)". The note now says no preposition is written and that N1 is approximate.
- U19 · i · **minor** · `i` had a gap, "your …(?)", where `l` translates ꜥqꜣ·tn. · → "your straightness(?)".
- U22 · l, i · **minor** · sp sn was rendered as a repeated word in both `l` and `i`. The house has "(twice)" in `l` and "(Twice.)" in `i` (023-024, 026-030b). `i` also took Budge's "where he was" for ẖr·f against `l`'s "under-him(?)". · l → "in · peace · (twice)". i → "to his place(?) of yesterday, in peace (Twice.) to the West."
- U24 · l · **minor** · `l` had the present "perishes-it · is-destroyed-it", against `i` and the note (the future negative). · → "shall-perish-it · shall-be-destroyed-it".
- U28 nst·f · glyph 0 tr, n · **minor** · The note opened "The papyrus writes ẖrt·f; read nst·f". But T28 is an approximate code for a sign the type prints like ẖr, and the packet decision says a seat sign is meant. The doubt is in the coding of the shape, so the one-way-slip formula does not apply. T28 also kept tr ẖr while the word is read nst. · tr → ns, the value the note argues, as with the other approximate codes. The formula is removed. The note now gives the shape, Budge's nest, the stock phrase ḫꜥ ḥr nst, and says the reading rests on these.
- U32 · n · **minor** · The note said "all of it in red except ẖrt-nṯr", but ꜣḫ (w292) is black in the packet. sbꜣ is read against Budge's sebχet with no reason given. · → "except ꜣḫ and ẖrt-nṯr, which are black". The note now says why sbꜣ is read (the gates sbꜣw of the West in Spell 30B), that the single sign could also write sbḫt (Spell 146), and that the reading is uncertain.
- U33 · n · **minor** · šwt is read against Budge's χaibit (ḫꜣybt) with no reason given. · One sentence added: the sunshade with t can write either word, and šwt is taken.
- U44 · i · **minor** · `i` made smn a main verb ("the Eye of Horus makes firm"). `l` and the note have the participle "which makes firm". · → "(it is) the Eye of Horus that makes firm …".
- U47 · l · **minor** · `l` had the indicative "is-opened" while `i` and the note make it a wish ("Let the way be opened … that it may see"). · → "let-be-opened".
- U50 · l, i, n · **minor** · n irt·sn was explained as the sḏmt·f "not yet done" and then translated as a future wish, which the form does not give. · Translated as it stands: l "have-(yet)-done-they", i "They have not yet done evil to me." The note says Budge's wish is not what the form gives.
- U54 · n · **minor** · The note said the eye-before-seat writing of wsir is "as in the House of Osiris in Spell 125", a parallel that does not hold. It is the ordinary writing (017, 018 and many other parts). · → "the order of the usual writing in Spells 17 and 18".
- U56 · l, i · **minor** · The tenses did not match: `l` had "is-shut-in" for nn + sḏm·tw·f, and `i` had "will go forth" for iw·f pr·f. · l → "shall-be-shut-in(?)". i → "he goes forth by day, and his ba shall not be shut in(?)", as in U32's "he becomes".
- U12 · i · style · "unions" is Budge's word, while `l` has "joinings(?)". · → "thousands of joinings(?)".
- U34 · n · style · sš was given as "(Budge: ān)" with no reason. The ·ṯi of wn·ṯi was called "the older spelling of ·ti, for the feminine". The ·ṯi spelling belongs to the second person. · The note now says Budge reads the sign ān, an old value, and that his 'scribe' agrees. ·ṯi is now described as written as for the second person and taken as the third person feminine ·ti.
- U36 · n · style · The participle reading of sšd after feminine irt did not mention the missing t. · One clause added: a feminine participle would have t, so the form is doubtful.
- U42 · n · style · The stray f is not read but the note did not open with the formula (cf. ꜣny in U1). · "The papyrus writes f after bꜣ·i; read without it." added at the opening.
- U46, U47, U53 · n · style · The notes did not say that these signs are approximate in the packet: A47, Y1 and S35 (U46), N35A (U47), G36 (U53). · "(coded …, approximate)" added at each.
- U56 · n · style · The closing sentence said all four spells ask to "go out by day" for the head too. · Rewritten: Spell 43 keeps the head on the body, and the other three let the ba and shadow go out and come back.

### Refused

- **ẖrt-nṯr "the necropolis"** (U0, U7, U26, U32). Kept. 26 of the 27 published units render it "the necropolis" in `l` and `i`; only the Hymn to Osiris has "the realm of the dead" in `i`.
- **U56 p:true** (black "ir rḫ rꜣ pn …"). Kept. The house puts p:true on every "if this spell is known" closing: 022-072 U14, 029-027 U37 and 044 U20. The voice also changes there from Ani's first person. The note says the words are black and does not call them a rubric.
- **Formulas kept as genuine one-way slips:**
  - ꜣny twice (U1);
  - nn·tw → in·tw (U10): nn is no verb, and only ini fits;
  - nfmy → nfꜣy (U11): the same phrase in line 7 has ꜣ;
  - ꜣmm-f-tn (U19): the reading "he grasps you" breaks the parallel;
  - sḥk → sk and ḥbtm → ḥtm (U24): house precedent ḥbmt·f in 044;
  - n-mn → smn (U44): smnt in line 2;
  - m-nw → m-ẖnw (U47).
- **ḫni·tw read as ḫnr** (U26, U32, U46, U54, U56). Kept. This is the 026-030b house solution, and its doubt is stated.
- **·tw tagged suff with lemma ·tw.** Kept: it is the practice of the latest parts (029-027, 061-054, 044).
- **say -kwi** (tjeskwi, maakwi, hemeskwi) against 044's khakui. Kept: it is the majority house form (017, 018, 022, 125).
- **say "Innitu"** for innytw. By rule it would be "Inenitu". Kept: it is a name of unclear make-up, matching the English used in `l`/`i`, and the note says so.
- **ḥḥ read with lemma nḥḥ** (U6). Kept: 001-a has the same writing and tagging.
- **dd = D37 D37** (U28). Kept: house (017-f).
- **U21** isw rdit·tn: `l` has "your-letting", `i` has "you are to let". Kept: it is a fair English rendering of the infinitive with a suffix subject after isw.
- **U49/U54** šwt rendered as "the shadows" (of the dead). Kept as a collective.
- **U53** "Budge … gives 'among' under em". Kept: reader B in the packet says Budge's 'among' is set under em/χenti and given to em.
- **U8** O21 as a classifier written before O22. U21 ḫpd with F51 inside the word. Both kept: the doubt is stated and the signs are as established.
- **U13** iw·f with a bare infinitive taken as the future. U36 "binds(?)". U43 iw as "comes(?)". U45 iḫḫw "light(?)". U51 isby. U52 sm·sn·tw. U55. All kept: each doubt is stated in `l`/`i` and in the note.

### For the glosser

No lemma was renamed or added. The lemmas used that are not in known-lemmas.json (24):

rnpi, innytw, pḥrr, wḏfꜣ, nfꜣ, ḫꜣ, ḥrt, ꜣmm, mꜥt, isw, ḫpd, nbw, ꜥꜣt, bꜣw, ḥwt-ḥr, is, wnt, ḫtm, ḫkr, pḏ, nmtt, mdw, iḫḫw, nḏr.

These known entries are too narrow for this part (`__broaden__`):
- dmi (known "town"; here the verb "touch, join, be joined to" and the noun "joining", U7, U12);
- šwt (known "feather, plume"; here "shadow", U33, U46, U47, U49, U54);
- nw (known only "Nu"; here the verb "look, see", U14);
- ·ti (known as the 2nd person stative ending; here also the 3rd person feminine, wn·ṯi and ḫtm·ṯi, U34–U35);
- iꜣbtt (known as the noun "the east"; here the adjective "eastern", U22).
