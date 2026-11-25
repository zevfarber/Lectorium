# Review — ani-018-b (Spell 18, the tribunals, sections F–J and the closing rubric, Plate 14)

## Pass 1

All edits were made by script (`review1_018b.py` in the reviewer's scratchpad). The script loads units.json and asserts that each old value is present (each text replacement must match exactly once, and each glyph's sign, role and tr are checked before the change). It writes the file back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline. No glyph code was retyped, and no word was joined or split. A second script (`check_018b.py`) confirmed these points after the edits:
- the 1130 sign codes, joined in order, equal the sequence in `source/established/ani-018-b.json`;
- every word's `rubric` flag matches the established file glyph by glyph;
- `ln` of every unit is the established line of its first glyph. Budge's numerals restart at 1 in each of sections F–J;
- every morph `g` list covers its word's glyphs exactly once. Every role is one of the six, every det has an empty `tr`, every other role has a `tr`, and every O34 has 'z';
- `q` is unchanged on every word that keeps Budge's grouping. The five joins are re-indexed correctly:
  - ḥtp-nṯr (U2, U24): `0:1*2` + `0-1` → `0:1*2-3-4`;
  - mnty·sn (U3): `0-1:2-3-4-5` + `0-1:2` → `0-1:2-3-4-5-6-7:8`;
  - ir·n·sn (U9): `—` + `—` + `0:1:2` → `0-1-2:3:4`;
  - ꜥḥꜥ·n·sn (U10): `—` + `—` + `0:1:2` → `0-1-2-3:4:5`;
- no Budge-ism (saith, triumphant, homage, thee/thou/thy, hath, divine chiefs, fiends, vindicate) is in any `l` or `i`.

Red writing, checked against the established flags. These units say "in red":
- the section openings: ir ḏꜣḏꜣt ꜥꜣt imyt + the place (U0, U4, U9, U16, U21);
- the "ir …" explanations: ir sipt mnty·sn (U5) and ir grḥ pwy n sštꜣ irw (U17);
- i at the head of each refrain (U1, U6, U13, U18, U23);
- the whole closing rubric from ḏd·tw (U27–U30).

U0 and U4 also say what is black. `p` stands on the five openings, the five refrains and the start of the rubric (U27), as in ani-018-a.

House renderings checked:
- smꜣꜥ-ḫrw "make(s) true of voice" and mꜣꜥ-ḫrw "true of voice", with the object moved after the verb when the epithet follows (U7, U19, U24), as ani-018-a does;
- ḏꜣḏꜣt "tribunal";
- "the accounting scribe of the god's offerings of all the gods" (ani-001-b, ani-022-072). ḥtp-nṯr is joined, as the house writes it;
- the names: Wepwawet (ani-001-b), Rosetau / `Ra-setjau`, En-iarered-ef, Babi, Wennefer, "the Lord to the Limit", Busiris / `Djedu`, Abydos / `Abedju`.

Counts: 2 major, 5 minor, 3 style.

### Changes

- U28 wḏꜣ pw ir·n·f · l, i, n · major · The draft took wḏꜣ as an adjective and read "sound is what he has done": `i` "what he has done upon earth is sound(?)". That misreads a set construction. An infinitive + pw + the relative form ir·n·f ("what he did was to go") simply states the action, and adverbials such as tp tꜣ go with the infinitive. The labels for ir·n·f (relative form of the past) were right, but the sense was not. The rubric means that the man prospers upon earth, not that his past deeds are judged sound · `l` "prospering(?) · it-is · what-has-done-he · upon · earth", `i` "…, he prospers(?) upon earth." The note now names the construction, gives the literal "prospering is what he has done", keeps Budge's 'it makes him strong' for comparison, and gives the other sense of wḏꜣ ('proceed, go on', against which the roll and the absence of the walking legs argue). It still says the reading is doubtful.
- U5 ḫnr·tw · glyph roles/tr, n · major · The drafter gave the U15-coded sign `phon` 'ḫnr' ("the sign ḫnr itself, an enclosure"), made ḫ and n its complements and made the reed a `det`. Nothing supports a ḫnr phonogram. The sign is coded U15 (the sledge tm in this house, and otherwise the house's "low hooked sign" classifier). Spell 1 (ani-001-a U12) writes ḫnr ḫ n r with U15 as a classifier, and a reed as a determinative is no role at all. Budge's χenà also has the reed and no r. The fix: Aa1 `phon` 'ḫ', N35 `phon` 'n', M17 `phon` 'i', U15 `det` ''. The reading ḫnr·tw is kept, with its query, because Budge's 'imprisonment', the classifier and the sense all point to it. The note now says plainly that no r is written, that the reed stands where r is expected, and that the enclosure-like sign suits ḫnr as a classifier but is not shown to write it. It names the passive sḏm·tw·f.
- U28 ḫr · glyph tr · minor · T28 had `tr` 'ḫr'. The butcher's block writes ẖr (the sign glossary and the note itself say so). The glyph shows the sign's value, and the reading gives the word meant · T28 `tr` 'ẖr'. The reading ḫr and the note's "which writes ẖr … taken as the particle ḫr" are kept.
- U29 rr · glyph role/tr, n · minor · V10 was `det`, and the note said "only one r is written, and the reading is doubtful". Every published writing of rr (ani-017-f U7, ani-147-a U11/U13, ani-147-b U42/U44) is V10 `phon` 'r' + D21 'r' + D54 `det`, which is exactly this spelling, so both r's are written · V10 `phon` 'r'. The note now says the word is spelled as in Spells 17 and 147, where the ring writes the first r. The "doubtful" is dropped. The known entry still carries its own (?).
- U8, U20 smꜣꜥ-ḫrw · n · minor · "the infinitive after n" was wrong: no n stands before smꜣꜥ-ḫrw. It is a second noun after the n of grḥ pwy n … · "the infinitive, a second noun after the same n 'of'".
- U12 · n · minor · "It was the gods of Busiris, after their inspecting, who allowed the slaughter" asserted a reading of a passage that `l` and `i` mark as doubtful. sipt n imyw ḏdw can equally be the inspecting *of* them · "Perhaps the gods of Busiris, by their inspecting, allowed the slaughter; the text does not say so."
- U4 isdnw · n · minor · The house already has a god of the judgement named beside Thoth: Isdes, isds (ani-017-c U20, M17 S29 D46 + s). The draft did not mention it · added: "The name is close to that of Isdes (isds), a god of the judgement whom Spell 17 names beside Thoth, and it may be the same god, but the spelling differs." The reading isdnw and the name Isdenu are kept, because the signs write n + nw, not s.
- U27 · i · style · `l` "being-pure(?)" and the note ("said of the one who recites") did not match `i` "said in purity(?)" · `i` "If this spell is said by one who is pure(?), …".
- U28 šdd·w · morph · style · The classifier U15 stood in the sḏm·w morph. A classifier belongs to the verb stem, and the house splits morphs non-contiguously for this (ani-017-c U12 ḏdw: ḏd [0,1,3,4], sḏm·w [2]) · šd [0,1,2,4], sḏm·w [3].
- U29 pr·f · say · style · "perief". The house says pr·f "peref" (3 occurrences) · "peref".

### The drafter's flagged doubts

- mnty·sn 'condemned(?)' (U3, U5): kept with its query. The join is right, and its q is re-indexed correctly. The reading follows the signs, and the note says the word is not known in these parts. 'Condemned' is the drafter's own, not Budge's 'annihilated'. The ꜣ read as in ḫftyw follows the house.
- wpwt / wpt (U2, U4): kept. The infinitive of wpi 'judge (between)' suits the crossed-sticks classifier (as in ani-001-b wp), and the note says that the w is an extra writing. The alternative wpwt 'message, errand' (ani-125-address wpwtyw 'messengers') does not fit "the tribunal of the … of the dead".
- ḫnr·tw: changed (above).
- iwt with D54 first (U9): kept. Only iwt fits, and the note says what is printed. It is not put under the misprints formula: Budge's īut implies the legs-with-reed sign M18, so the difference may lie in the print and not in the scribe's hand. The note does not blame the scribe.
- ꜥwt (U9): kept. The crook S39 writes ꜥwt, with w and t as complements and the hide as classifier.
- n ḏri·n·tw (U11): kept with its queries. The negative n sḏm·n·tw·f 'could not be …' is the right label. A verb ḏr 'put an end to, stop' needs a broadened gloss (below).
- rdi·n·tw with the stray w (U12): kept. The w is unread and the note says so. D36 for the hand that gives is the house's (ani-001-b U17, ani-017-a U27).
- sštꜣ with W10 (U15, U17): kept as an unread classifier, and the note says the sign is unidentified.
- qrs (U17): kept as the verb 'bury' after ḥr. The house writes the verb with these signs too (ani-125-address U49 qrs·n·i, Q6 U15).
- ḏrww 'side(?)' (U17): kept with its query.
- mnt 'thigh(?)' (U17): kept. The lemma collides with the known entry mnt 'daily' (below).
- The rubric:
  - wꜥb: kept (`i` aligned, above).
  - twt: kept. Budge's supplied '[and he maketh]' is reported, and nothing is supplied in `l`.
  - ḫr on T28: tr changed (above).
  - šdd·w with V6: the `tr` 'šd' on V6 is kept. The note says that the cord stands where the water-skin šd is expected and that the reading rests on the sense. V6's own value šs would give no word here.
  - wḏꜣ pw ir·n·f: changed (above).
  - rr: changed (above).
  - šs mꜣꜥt: kept. The known entry šs already carries "meaning uncertain".

### Considered and refused

- U0 wp-wꜣwt `say` "Wep-wawet" against `i` "Wepwawet": kept. Compound names are hyphenated in `say`, and `i` uses the settled name (as ani-001-b does).
- U16 bby read with lemma bꜣby, not under the misprints formula: kept. Bby is a writing of the name, not a slip that the sense allows only one way. The note says the vulture is not written.
- U17 ḫpš 'foreleg': kept. The F23 classifier is the ox's foreleg, and the house (ani-017-c U21) has "Foreleg" for the same spelling.
- U20 ꜥwy·fy "the suffix made dual to agree with the arms": kept. The extra strokes after ·f follow a dual noun, and the reading shows them.
- U27 `i` "after mooring": kept. It is real English, and the note and the known gloss of mni explain it as the end of life's voyage.
- U29 `i` "goes round him": kept. It is literal, and 'encircle' is in the note.
- U9 ir·n·sn as a circumstantial "when they had made": kept. It is the sḏm·n·f after pw, and the join is correctly re-indexed.
- `titleEn` without "and the rubric": kept. `part` names the rubric, and ani-018-a's `titleEn` has the same shape.

### For the glosser and pass 2

Lemmas used in units.json that are NOT in known-lemmas.json (9):
- `isdn` (Isdenu; Budge: Àsṭennu; perhaps the same god as Isdes);
- `itrty` (the Two Shrines, the national shrines of Upper and Lower Egypt; Budge: àterti);
- `mnty` (condemned (?); sense uncertain; Budge: menta);
- `nḏm` (to be sweet, pleasant; nḏm ib 'glad');
- `sft` (to slaughter, butcher);
- `sštꜣ` (to hide, make secret; causative of štꜣ);
- `wp-wꜣwt` (Wepwawet, 'Opener of the Ways'; Budge: Àp-uat);
- `ḏrw` (side, flank (?); Budge: t'eruu, 'heel');
- `ꜥwt` (small cattle, flocks, goats and sheep; Budge: āut).

Known lemmas whose entry is too narrow for this part (for `__broaden__`):
- `mnt`: only 'daily (adverb)'. U17 has mnt 'thigh, leg (?)' (noun f.; with the leg classifier; Budge: ment, 'leg'), which needs "· a second word of the same spelling".
- `ḏr`: only 'limit, border' and 'since'. U11 has ḏri 'put an end to, stop (?)' (verb; Budge: t'erà).
- `ḫr`: only the verb 'fall' and the preposition. U28 has the particle ḫr, which brings in a further case or a consequence (here written with T28 ẖr).
- `bꜣby`: add "also written bby, without ꜣ (Budge: Bebi)".
- `ḫnr`: add the passive ḫnr·tw '(things) are shut away (?)' only if pass 2 thinks the entry needs it; the general sense 'shut in' covers it.

## Pass 2

All edits were made by script (`review2_018b.py` in the reviewer's scratchpad). The script asserts each old value: entries must match exactly, text replacements must match exactly once, and glyphs are checked by sign, role and tr. It writes units.json and gloss.json with json.dumps(ensure_ascii=False, indent=1) and no trailing newline. No glyph code was touched. After the edits, pass 1's checker (`check_018b.py`) confirmed the same points as before: the 1130 signs are in order, the rubric flags and `ln` match, morph coverage is exact, det/tr are correct, `q` is unchanged outside the five joins (which are correct), and there are no Budge-isms. A further check of gloss.json confirmed:
- every morph lemma is in known-lemmas.json or in gloss.json (none missing, none unused);
- every new entry starts "lemma — ";
- every `__broaden__` value starts with the known entry verbatim, followed by " · ".

The coordinator asked about three entries:
- itrty: the reading in the units (i t r t y with two shrine classifiers) is the usual spelling of 'the Two Shrines', so the entry and U22's note agree. Budge's 'two regions' is kept only as his rendering.
- isdn: now matches the pass-1 note on U4.
- the ḥr broadening ('with', of the cause of a feeling: ḥtp ḥr·s): kept. It is exactly U22's use.

Counts: 0 major, 4 minor, 8 style.

### Changes

- gloss `·f` (broaden) and U20 ꜥwy·fy · gloss, reading, say, glyph role, n · minor · The glosser called ·fy "the dual form" of ·f, "agreeing with a dual noun". The U20 note said the same ("the suffix made dual to agree with the arms"), and pass 1 refused to change it. That was wrong: Egyptian has no dual of the 3rd masculine singular suffix. The two strokes after ·f are the dual strokes of ꜥwy written again, and they are not read. The house writes this word ꜥwy·f (ani-017-f U6). The fix:
  - reading `ꜥwy·f`, say `awyef`, the last Z4 `det` '' (still in the ·f morph);
  - the note now says that the strokes are repeated and not read, and that the suffix is still ·f 'his';
  - broaden: "· after a dual noun sometimes followed by the two strokes of the dual, which are not read (ꜥwy·f 'his two arms')".
- gloss `ḫr` (broaden) · minor · "a third word of the same spelling" was wrong, because the particle is a different word and is here not written the same way. "not translated" and "written with the block ẖr" described this line only, not the lemma · "· a third word: the particle ḫr, which brings in a further case or a consequence (?) (particle; sometimes written ẖr)".
- U10, U25 ꜥ after m-bꜣḥ · morph gloss · minor · Without its own gloss, the build would show 'arm, hand' for a sign that the notes leave unexplained and `l` shows as "(ꜥ)" · added an occurrence gloss: "ꜥ — the arm sign, written after m-bꜣḥ 'in the presence of'; not explained, perhaps part of a fuller writing of the preposition (?)".
- gloss `iry` (broaden, new) · minor · U26 irt·f and U29 iry·f use iry as an adjective 'belonging to', with a feminine irt. The known entry gives only the noun 'one who belongs to, keeper of' · added "· also as an adjective, 'belonging to, pertaining to' (feminine irt; irt·f 'which belongs to him')".
- gloss `isdn` · style · "who with Thoth, Osiris and Anubis sits in the court" was tied to this line · "a god of the tribunal that judges the dead; perhaps a form of the name of Isdes (?)", as the U4 note now says.
- gloss `itrty` · style · the spelling detail "written with two shrines as classifier" was cut. The label is now "noun f., dual".
- gloss `mnty` · style · "written with the captive that classes people with enemies" was made general: "with the classifier of enemies".
- gloss `nḏm` · style · "glad" and "of the heart" are not senses of nḏm itself · "to be sweet, pleasant (verb; nḏm ib 'glad of heart'; …)".
- gloss `sštꜣ` · style · added "causative of štꜣ 'be secret'", as the house labels causatives.
- gloss `wp-wꜣwt` · style · "who goes before Osiris" went beyond these parts · "a jackal god".
- gloss `ḏrw` · style · "taken from ḏr" stated an etymology as fact · "side, flank (?) (noun; perhaps from ḏr 'limit, end'; …)".
- gloss `mnt`, `ḏr` (broaden) · style:
  - mnt: "written with a leg sign" becomes "with the leg as classifier";
  - ḏr: the doubled hedge ("(?)" + "sense uncertain") and the invented derivation are replaced by "· also ḏri 'to put an end to, stop' (?) (verb; Budge: t'erà)".

### Second read of units.json

I made a full second read: `l` word by word, `i` against `l`, the grammar in every note, and consistency with the pass-1 edits. Nothing else needed changing:
- U5 (ḫnr·tw), U28 (ẖr, wḏꜣ pw ir·n·f, šdd·w morph) and U29 (rr) agree in their glyphs, notes, `l` and `i`.
- U8 and U20 now hang the infinitive on the one genitive n.
- U27 `i` agrees with "being-pure(?)".
- The rubric statements still stand on U27–U30.

Refused:
- U11 hꜣy is given no grammatical label: kept. Both a participle and a stative are possible, and the note does not claim either.
- U9 `i` "the form" against `l` "forms-their": kept as the English idiom for iri ḫprw m.
- gloss `šs` with V33: no broadening is needed. The known entry is general, and the sign is described in the U30 note.
- gloss `ꜥwt`, `sft`, `bꜣby` (broaden), `ḥr` (broaden): kept as written.
