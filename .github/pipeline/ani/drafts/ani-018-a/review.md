# Review — ani-018-a (Spell 18, the tribunals, sections A–E, Plate 13)

## Pass 1

All edits were made by script (`review1_018a.py` in the reviewer's scratchpad). The script loads units.json, asserts that each old value is present (exactly once for text), changes it, and writes the file back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, as the drafter wrote it. No glyph code was retyped: joins and splits copy the existing glyph objects. A second script (`check_018a.py`) then confirmed these points:
- the 929 sign codes, joined in order, equal the sequence in `source/established/ani-018-a.json`.
- every word's `rubric` flag matches the established file glyph by glyph. No word is restored.
- the red writing is: ir ḏꜣḏꜣt ꜥꜣt imyt + the place in each section opening (U0, U5, U11, U16, U21); ir sꜣyw sbiw (U1); ir sꜥḥꜥ ḏd m ḏdw (U6); ir grḥ pwy n ḫt ḫꜣwt ḥb (U12); ir sꜥḥꜥ ꜥꜣw n (U17); and i at the head of each refrain (U2, U8, U13, U18, U22). Every one of these units says "in red", and U0 and U17 also say what is black.
- every morph `g` list covers its word's glyphs exactly once. Every role is one of the six, every det has an empty `tr`, every other role has a `tr`, and every O34 has 'z'.
- every word that is not joined or split keeps the packet's `q`. The one join and the two splits are re-indexed:
  - ḥr-ḫnty-irty (U11): `—` + `0-1:2*3-4-5:6-7` → `0-1-2:3*4-5-6:7-8`;
  - iḏbw + rḫty (U19): `0*1*2:3*4*5-6-7:8*9-10:11` → `0*1*2:3*4*5` + `0-1:2*3-4:5`;
  - iḏbw + rḫty (U21): `0*1*2-3-4*5:6` → `0*1*2` + `0-1*2:3`.
- `ln` of every unit is the established line (Budge's section-relative numeral) of its first glyph. The numerals restart at 1 in each of sections A–E.
- `"p": true` stands on the five section openings and on the five refrains (the address to Thoth, a speech), and nowhere else. This is now consistent across the sections (see U12 below).
- no Budge-ism (saith, triumphant, homage, thee/thou/thy, hath, divine chiefs, fiends) is in any `l` or `i`. After the changes below, "vindicate" is no longer used for smꜣꜥ-ḫrw anywhere.

Counts: 3 major, 10 minor, 4 style.

### Changes

- U2, U8, U13, U18, U22 (refrain) and U3, U9, U14, U19, U23 (its second half), `about`, U2 n, U3 n · l, i, n · major · The draft rendered smꜣꜥ-ḫrw as "vindicate". The published Spell 1 parts render it "make true of voice". ani-001-b has `l` "who-make(s)-true-of-voice · Osiris · against · enemies-his" twice. ani-001-a's `l` still says "who-vindicate(s)", but its `i` says "who make(s) Osiris true of voice against his enemies" both times, and so does every published `i`. The fix:
  - `l`: "who-makes-true-of-voice" in the refrain, and the imperative "make-true-of-voice" in the second half.
  - `i`: "O Thoth, who makes Osiris true of voice against his enemies,". The second half reads "make the Osiris Ani true of voice against …" (U3, U14). Where the epithet mꜣꜥ-ḫrw follows the name, the object is moved after the verb so that the two "true of voice" do not run together: "make true of voice the Osiris Ani, true of voice, against …" (U9, U19, U23).
  - U2 n: the phrase "is kept literal, as in Spell 1", replacing "it is rendered 'vindicate'".
  - U3 n: "the imperative, 'make true of voice!'".
  - `about`: "asking Thoth, who made Osiris true of voice …, to make Ani true of voice before the next tribunal".
  - The one remaining "vindication" (U19 n) is the noun sense of mꜣꜥ-ḫrw that the known entry gives, and it is kept.
- U19 w204 and U21 w221 (the place of section E) · reading, say, glyph roles/tr, morph, q (split), l, i, n, `about` · major · The draft read tꜣw-rḫyt 'the lands of the common folk'(?). It took the slanting wedges for "the land sign tꜣ", but the land sign is N16. The established code is N21, the tongue of land iḏb 'bank', and the house reads exactly this sign that way: ani-001-b U2 has iḏbwy 'the Two Banks(?)', N21 `log` 'iḏb' with the canal N23. In U19 the established file describes "three slanting wedges over three bench-like signs", not the draft's "six wedges". That is the same bank-over-canal group, written three times for a plural. The rest of the group is r ḫ t y, in that order. It cannot be rḫyt 'common folk', which is in any case written with the lapwing (known entry). The plants-on-a-base classifier (M20, the reed field) suits a riverbank. ani-001-b U2 also has a place after the Two Banks, rḫtt 'Rekhtet', in a passage about the mourners of Osiris. Here the night of this tribunal is Isis's mourning for Osiris (U20). So the fix is:
  - each word is split into iḏbw (N21 `log` 'iḏb' + N21s `det`; lemma iḏb; say idjebu) and rḫty (r ḫ t y `phon`, M20 and O49 `det`; lemma rḫtt; say Rekhty);
  - `l` "the-Banks(?) · of-Rekhty(?)", `i` "the Banks(?) of Rekhty(?)";
  - U19 n now explains the sign, gives Budge's Taiu(?)-reχit, and says that 'Banks' is a fair reading of the signs while the name and its identification with Rekhtet are not sure.
  - U21: the papyrus writes only t, y and the classifiers. The refrain just before gives the full spelling, so the misprints formula applies: the note now opens "The papyrus writes ty for the name; read rḫty …".
  - `about`: "the Banks of Rekhty, a place not identified".
- U12 w119 ḫꜣwt · morph, l, i, n · major · The draft translated "the things of the altar(?)" and set Budge's 'night' aside. That breaks the spell's own structure. Each "ir …" unit takes up the night named at the end of the section before: U6 takes up U4 (sꜥḥꜥ ḏd m ḏdw), and U17 takes up U15 (sꜥḥꜥ ꜥꜣw n ḥr). The night at the end of section B is grḥ n ḫt ḫꜣwy m sḫm (U10). U12's "ir grḥ pwy n ḫt ḫꜣwt" is that same night, so the word is ḫꜣwy 'night' written with t and without the sky. The draft's note even saw the parallel, but read it backwards · lemma `ḫꜣwy`; the reading stays `ḫꜣwt`, as written. `l` "of-the-night(?)", `i` "the things of the night(?) of the festival(?)". The note gives the parallel and keeps 'altar' (as in the introduction) as the other possible reading, so the reading is marked as doubtful.
- U11 w106–107 ḥr + ḫnty-irty · reading, say, q (join), morph, l, n · minor · The draft kept Budge's two groups and put the lemma ḥr-ḫnty-irty on the second group only, so the glossary would gloss "Khenty-irty" as "Horus-Khenty-irty" and ḥr would be glossed separately. The published ani-017-c U26 has the name as one word (G5 `log` … D4 `log` 'ir', D4 `det`) · joined as ḥr-ḫnty-irty, say "Horus-Khenty-irty", one morph [0–8]; `l` "Horus-Khenty-irty". The note says that the groups are joined. R22 stays `det` and unread, as the note explains.
- U12 · p · minor · `"p": true` stood on this "ir grḥ …" unit, but not on the other three "ir …" explanation units (U1, U6, U17). Spell 17's published "as for …" units carry no p · removed. The p is now on the section openings and the refrains only.
- U0 n and `about` · n · minor · The note on the passage left out said the address to Thoth was "not on Ani's papyrus as Budge prints it" and that Ani's text "opens in the middle of the spell". Budge prints it in brackets precisely because it is not Ani's · now: "Before this, Budge prints in square brackets a passage that Ani's papyrus does not have, supplied (his note) from Naville's edition of other papyri: the opening of the spell, an address to Thoth, who makes Osiris true of voice, and the start of the section on the tribunal in Heliopolis. It is left out, so Ani's text begins with the explanation of that tribunal." The `about` had the same hedge ("as Budge prints it") · now "that Ani's papyrus does not have (Budge supplies it from Naville's edition)".
- U3 · n · minor · The note put Budge's footnote (Var. m-bꜣḥ) on this m. The footnote mark is on the m of the next refrain (p. 76 n. 2, packet w90, U9), and U9 cites it correctly · U3 now says "at the same word in the next refrain Budge's footnote gives a variant m-bꜣḥ".
- U1 · l, i, n · minor · `l` "in · again(?)" and `i` "a second time(?)" did not agree, and "in" made the literal line opaque · `l` "(m) · again(?)", `i` "when he was beaten(?) again(?)". The note adds that m is left untranslated and that this nm is not the interrogative 'who?' (the only nm in known-lemmas).
- U5 · l, i · minor · nḏ-ḥr itf was "protector · of-the-father". The house has "who-protects · father-his" / "who protects his father" (ani-017-b U2, ani-017-c U31), and the note itself calls it a participle · `l` "who-protects · the-father", `i` "and Horus, who protects the father."
- U10 · l, i, n · minor · ḫt ḫꜣwy was "the things of the evening". The published ani-125-address U49 has the same phrase as "things of the night", and Budge has 'night' · `l` "of-the-night", `i` "the things of the night". The note now glosses ḫꜣwy 'night, evening' and cites the Spell 125 parallel.
- U19 · l · minor · `i` had "for him(?)" but `l` had "for-him" with no query, although the note calls it doubtful · `l` "for-him(?)".
- U7 · n · minor · mrw 'bandages' was asserted, but the drafter listed it as doubtful, and the word is not otherwise known in these parts · one sentence added: "The word is not met elsewhere in these parts, and its sense rests on the classifier and on Budge." `l` and `i` are kept without a query, since the cord classifier, mr 'bind' and Budge all agree.
- U17 · n · minor · "Seth seems to tell his own followers to set up pillars, perhaps against Horus" went beyond the text · now "the text does not say whose followers they are, or what 'it' is."
- U7 iw·sn, U17 r·s, U20 sn·s · glyph tr · style · O34 as a suffix had '·s'. The house writes the bolt '·z' (87 published occurrences against 8; ani-017-a r·s) · '·z'.
- U0 w4 iwnw · glyph role/tr · style · W24 was `comp` 'n'. The house (ani-001-a) has `phon` 'nw', and the note itself says "the pot nw" · `phon` 'nw'.
- U6 · n · style · "In Spell 1 Ani guards … the shoulder of Osiris" · "the left shoulder", as ani-001-b U9 has it.
- U12 · l, n · style · ḥḏ tꜣ "the brightening of the earth" · "of the land", as the house renders tꜣ in ḥḏ tꜣ (ani-hymn-to-ra U22, "the land grows bright").

### The drafter's flagged doubts

- sꜣyw (U1): kept as sꜣw 'guard' (infinitive) without a query. The sign value sꜣ agrees with Budge, and the captive classifier suits "keeping the rebels in custody". The two reeds are not explained by an infinitive, but the note describes them. Neither Budge's 'fettering' nor 'guarding' is a different word.
- ḥtm·n·tw with U33 (U1): kept. The note already says the tall sign is not identified. The passive sḏm·n·tw·f is the right label, and Budge's noun "the destruction" leaves the n·tw unexplained.
- m nm qn·tw·f (U1): kept as doubtful (`l`/`i` aligned, above). The draft's rejection of Budge's active "he wrought evil" is right: tw + suffix is passive.
- mrw (U7): hedged in the note (above).
- ḫnty-irty with R22 unread (U11): the word is joined (above). R22 is still unread. Budge's àn is reported, and nothing better can be asserted.
- ḫꜣwt (U12): changed (above).
- ḥb from W3/N5 (U12): kept with its query. The rubric runs to the end of ḥb, which supports taking it with the heading. How it joins the words before it is still unclear, as the note says.
- Pe/Dep with t (U14, U16): kept without a query. The t is the feminine ending of the place names, and the note says the usual names are Pe and Dep.
- ꜥꜣw 'pillars(?)' (U15, U17): kept with its query. The alternative iwnw is mentioned in the note.
- smn·tw (U15): kept, and no query is needed. The passive sḏm·tw with the dative n·f before the noun subject iwꜥt is the regular order.
- iwꜥt (U15): kept, and no query is needed. The t and the roll of abstracts point to 'inheritance', as the note says.
- r·s (U17): kept, with the note's statement that the referent is unknown.
- mꜣꜥ-ḫrw n·f (U19): kept as doubtful. A query was added to `l` (above).
- tꜣw-rḫyt(?) (U19, U21): changed to iḏbw rḫty (above).
- rs·ti (U20): kept. The 3rd feminine singular stative ending written tw, after the subject ꜣst, is right.
- tnw (U24): kept with its query, and the alternative 'number, count' is in the note. The lemma ṯni needs broadening (below).
- ihꜣbw (U24): kept with its query.
- tni (U24): kept. S39 is a classifier and the note says it is approximate. "Thinis" in `i` and "Teni" in `say` follow the house practice for places (Djedu / Busiris, Abedju / Abydos).

### Considered and refused

- U15 `i` "the inheritance of the property of his father" against `l` "in · the-property": kept. m here is 'in (the matter of)', and English "of" carries it. A literal "inheritance in the property" is not idiomatic.
- U24 `i` "the coming of jubilation(?)" against `l` "the-coming-into-being": kept as idiomatic English for ḫpr. The sense is not lost.
- U7 `l` "they" rather than "(iw)-they": kept. The note says that iw is not translated, and the house is not uniform here.
- U3 doubled ꜣny: kept as drafted. The note opens with the formula ("The papyrus writes ꜣny twice …; read it once"), mentions Budge's "(sic)", and `l` marks the second as "(Ani)".
- U20 "The papyrus writes kꜣbyt; read iꜣkbyt": kept. After irt with the mourning lock, only 'lament' makes sense, and ani-001-b spells the word in full.
- U12 reading field: it keeps `ḫꜣwt`, as the signs are written, although the lemma is now ḫꜣwy. The word meant is not certain enough for the misprints formula.
- U4, U6, U17: ḏd 'djed pillar' with lemma `ḏd` is kept. The glossary needs a second sense (below).
- U2 ḫftyw·f "(an old spelling, not read)" with G1 `phon` 'ꜣ': kept. The tr shows the sign's value, and the reading follows the house (ani-001-a has the same roles).
- `say` "nef" for n·f against "enef" in some parts: kept, since both forms are in published use. "Horus-Khenty-irty" is taken from ani-017-c.
- U0 and U24 note lengths: kept. Each is long because it reads every sign of a unit that has many new words, and neither carries background beyond a sentence. The refrain notes after U2 are already short.
- U9: adding Budge's Nebseni footnote (p. 76 n. 1): not done. It does not show that Ani's text is garbled, so conventions leave it out.

### For the glosser and pass 2

Lemmas used in units.json that are NOT in known-lemmas.json (16): `dp` (Dep, place name; Budge: Ṭept), `hꜣkr` (Haker, a night festival of Osiris, here with the god classifier; Budge: Haker), `ihꜣbw` (jubilation, rejoicing (?); Budge: àhabu), `iwꜥt` (inheritance, noun f.; cf. iwꜥ 'heir'; Budge: āuāt), `mrw` (bandages (?); Budge: meru), `mt` (to die; mtw 'the dead'), `p` (Pe, place name, here written pt; Budge: Pet), `qn` (to beat, overpower (?), with crossed sticks; Budge: qen), `rs` (to be awake, keep watch), `smn` (to make firm, establish; causative of mn), `sḏr` (to lie down, spend the night), `sꜥḥꜥ` (to set up, erect; causative of ꜥḥꜥ), `tfnwt` (Tefnut; Budge: Tefnut), `tni` (Teni, Thinis; Budge: Teni), `ḥtm` (to destroy; to perish), `ꜥꜣw` (pillars, columns (?); Budge: āāiui).

Known lemmas whose entry is too narrow for this part (for `__broaden__`):
- `ḏd`: only 'say'. U4 and U6 have the djed pillar ("· a second word of the same spelling: the djed pillar, emblem of Osiris (noun m.)").
- `nm`: only 'who?'. U1 has m nm 'again, a second time (?)' (Budge 'the second time').
- `iꜣkb`: iꜣkbyt is only 'wailing woman'. U20 has iꜣkbyt 'lament, mourning' (noun f.).
- `ṯni`: 'be distinguished; ṯnw greatness'. U24 has tnw, written with t, 'separating, setting apart (?)' (Budge: tennu).
- `rḫtt`: add "also written rḫty; iḏbw rḫty 'the Banks of Rekhty' (Budge: Taiu(?)-reχit)".
- `iḏb`: add the plural iḏbw 'the Banks' (written with N21 three times).
- `sꜣw` (to guard): the entry says "written with the herdsman with his stick". U1 writes it with the sign sꜣ and a captive classifier ('guarding, keeping in custody'; Budge: saiu, 'fettering').
- `m`: add 'before, in the presence of' (U3 etc.; Budge's variant m-bꜣḥ).
- `·ti`: the 3rd feminine singular is given only as "written ·ṯi". U20 writes it ·tw (rs·ti).
- `ḫꜣwy`: add "also written ḫꜣwt, with t" (U12), if pass 2 keeps that reading.
