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
