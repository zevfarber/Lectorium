# Review — ani-023-024 (Spells 23 and 24, Plate 15)

## Pass 1

All edits were made by script (`review1_023024.py` in the reviewer's scratchpad). The script asserts each old value before it replaces it: each text replacement must match exactly once, and each glyph's sign, role and tr, each morph list and each say value is checked first. The file is written back with json.dumps(ensure_ascii=False, indent=1). The draft had been written with indent=2, so the whole file is now re-indented. No glyph code was changed or moved, and no word was joined or split. A second script (`check_023024.py`) confirmed these points after the edits:
- the 647 sign codes, joined in order, equal the packet's sequence;
- every morph `g` covers its word's glyphs exactly once;
- every det has an empty `tr`, no other role has an empty `tr`, and every O34 carries z;
- every word's `rubric` flag matches the packet glyph by glyph;
- `restored` stands on exactly the bracketed glyphs the packet describes (r·sn: n and the strokes; nty·f twice: f; m before sgrw; rdi of rdi n·i; the ṯ of ṯsmw; r before šwyt in U13);
- `ln` of each unit is the packet line of its first glyph, and Spell 24 restarts at 1;
- no Budge-ism is in any `l` or `i`;
- the JSON parses.

The joins and splits are re-indexed correctly:
- imt-wrt (U7): `0-1-2` + `0:1-2-3` → `0-1-2-3:4-5-6`;
- nty·f (U15, twice): `0:1*2` + `—` → `0:1*2-3`;
- rdi | n·i (U17): `0:1-2:3` → `0:1` + `0:1`.

Rubric statements were checked against the flags: U0, U1, U6, U9, U10, U13, U14, U15, U16, U17 and U18 say "in red" for exactly the flagged words.

Counts: 2 major, 9 minor, 2 style.

### Changes

- U14 rwd · n · **major** · The note called rwd "the stative, 'are firm'". The stative follows its subject, but rwd stands before ꜥqy·k. · The note now says that rwd, standing first, is the adjective-verb used as predicate ("firm are your …") or the sḏm·f. `l` and `i` were already right.
- U13 · n · **major** · The note said "The second and third versions below have m bw nb nty·f im". The third version (U17) has only ḫr nty·f. · Corrected: the second version has m bw nb nty·f im, and the third has only ḫr nty·f.
- U18 šwyt · morph · minor · The reading was šwyt but the lemma was šwt. In the house glossary šwt is "feather, plume" (ani-017-b), so the word would have been filed under the wrong lemma. · The lemma is now šwyt, with the gloss override kept ("shade, shadow … here with a house-like classifier where the refrain has the sun"). The note now says "šwyt 'shade, shadow', a word of the same letters but different" instead of naming šwt.
- U13 šwyt · n · minor · The note did not say that the refrain's letters šwyt are also the ordinary spelling of 'shade, shadow'. A reader comparing the refrain with the variant in U18 needs to know this. · One sentence added: the sun classifier points to light, the same letters spell šwyt 'shade, shadow', and the variant in U18 is taken that way.
- U16 qmꜣ·tw · glyphs (roles/tr only) + n · minor · The draft had N29 phon q, G1 phon ꜣ, T14 det and G17 phon m, with the throw-stick T14 as a classifier. The house (ani-147-b qmꜣ·n) reads T14 as the sign that writes qmꜣ, with q, ꜣ and m as its complements. · Changed to N29 comp q, G1 comp ꜣ, T14 phon qmꜣ, G17 comp m, and the note rewritten to match. M15, Y1a, t and w are unchanged.
- U6, U7, U14 nt · morph · minor · The draft filed the feminine genitive under the lemma n. The house files it under ny ("written n, fem. nt", ani-017-a). · The lemma is now ny in all three places.
- U6 biꜣ · n · minor · The draft disagreed with Budge's bàat (t not read) without saying why. · Added: biꜣ is masculine, as the n (not nt) of n pt after it shows, so the t is not a feminine ending.
- U14 inn · n · minor · The draft said only "the participle of ini, its n doubled". · Now "the imperfective participle of ini", which doubles the n.
- U3 mḥ, ꜥpr · n · minor · The note gave no form for the two words. · They are now named as statives describing Thoth.
- U13, U15 s · say · minor · `se` → `es`, the house say-form for s 'man' (published parts).
- U1 ḏd·i · n · minor · Ani's Spell 22 opens the same way: a doubtful ḏd, which Budge also renders 'to be said', and which ani-022-072 reads as 'said(?)', perhaps for ḏd mdw. The draft did not mention this. · One sentence added giving that parallel and noting that no sign for mdw is printed here. The reading ḏd·i is kept (see refused).
- U2, U8, U9 · n · style · "the genitive n is not written" → "direct genitive", the house wording (ani-001-a, ani-001-b). Nothing is missing from the text.
- U9 swt · n · style · The note now says the reading as the particle is doubtful.

### The drafter's flagged doubts

- w7 ḏd·i vs Budge 'to be said' (U1). Kept. The signs are I10 D46 M17 Z1, and Budge's t'eṭà also has the reed. Reading the reed as ·i is unusual, since this papyrus writes ·i with the seated man two words later, but it gives a form the signs support. Budge's 'to be said' implies a reading he does not spell out. The note says the reading is not sure and now gives the Spell 22 parallel.
- w12/27 wḥꜥ vs Budge uāu (V12 D36 Z7 U15). Kept. Budge's uāu gives no known verb that fits. wḥꜥ 'loosen' fits the sense and the classifier of cords. The note already says that the value wḥ of the first sign is a guess and that Budge has no ḥ.
- w13/28 nwt 'bonds(?)' and w47 nwt·f. Kept with their queries. The note gives the reading of nt-w as the ending wt with t before w, as uncertain. The lemma nwt is in the house glossary as Nut. Both uses carry gloss overrides, so the glosser needs to add homographs (see below).
- w34 ḫsf·tw. Kept. Reading it as the passive with an unexpressed subject is grammatical, the alternative (ḫsf tw tm 'Atum repels you') is given, and `l` and `i` carry "(?)".
- w36–37 "The papyrus writes wdn·n·f sn·f; read wd·n·f sn." Kept, as justified under the misprints rule. With the context (the bonds turned against those who restrain) the only verb that gives sense is wdi 'cast, shoot', which is also Budge's 'shoots'. wdn 'offer, be heavy' gives none. A doubled n is the commonest slip. The second f after sn: reading it as sn·f 'his brothers' would need the brother sign, and this spelling (O34 N35 Z2) is the pronoun's. No second sensible reading of the stray f exists, so it is left unread, and the note says so. The opening sentence follows the misprints form.
- w44 "papyrus writes ir; read in" (U6). Kept. After a passive with a following noun only the agent 'by' gives sense, as in the parallel in line 1 (wn rꜣ·i in ptḥ). Budge himself transliterates àn, so the slip is in the signs as printed, and the reading is corrected while the glyphs stay.
- w50 biꜣ. Kept (reason added to the note, above).
- w86 psḏt (X6 log psḏ). Kept. It matches the house exactly (ani-017-a, ani-018-introduction).
- w108 bḥnwt (U12). Kept. Taking t before w as the feminine plural follows the same practice as nwt. The sense 'hyenas' rests on Budge and on the dog classifier, which the note says ("not otherwise known in these parts").
- w133 ꜥqy·k. Kept. It is queried in `l` and `i`, and S39 is marked as not identified.
- šwyt / šwt. Lemma corrected and notes improved (above).
- Unit 17 = U16 (w163–177). Corrected qmꜣ (above). The rest is kept: the note says plainly that how the words hang together is not clear, rtw and mwt keep Budge's queries, and `l` follows the signs.
- w183 nty·f as a noun 'him whose it is' (U17). Kept. It is marked uncertain, Budge's 'where it is' is given, and the elliptical sense fits ḫr 'from (a person)'.
- w116 and w143, the versions. The U13 note's claim about the other versions has been corrected (above). U15's dmḏ·n·k with 'you' is right, and its note says the addressee is now the one who gathers.

### Considered and refused

- w139 m written twice (G17 phon + Aa15 comp). Refused: the conventions reserve comp for a multiliteral, but the house writes the same doubled m with Aa15 as comp (imi in ani-017-b and ani-weighing-of-the-heart; imy in ani-018-introduction). Consistency with the published parts wins.
- U17 rdi has the rubric flag, though Budge's overline covers only n·i. Refused: the flag matches the established word (erṭā-nà, rubric), which the house check compares glyph by glyph. The note says exactly what the overline covers.
- U4 i puts "(Twice.)" at the end of the sentence, while U2 puts it after the verb. Refused: in U4 sp sn stands at the end of its clause (wḥꜥ·w nwt sp sn), so the placement follows the Egyptian.
- U5 sn includes the stray f in the lemma sn with tr f. Refused: the stray f is kept as it stands and is not read, and the note explains it. Making it a suffix would claim a reading.
- U8 sꜣḥ and w13/w47 nwt filed under lemmas that the house glosses as "toe" and "Nut". Kept with gloss overrides. For the glosser: these need "a second word of the same spelling" entries under `__broaden__`, not new lemmas.
- nṯrw (R8 log + R8 det det). Refused: the house is mixed (ani-001-a has R8 phon), and log is right for the flag.
- Sekhmet as a name (ani-146-a has sḫmt `sekhemet` 'mighty one', an epithet). Kept: here the seated goddess is the classifier and she is named with ink, so this is the goddess, whose name is settled.
- Budge-isms and remembered modern wording: none found. "Lake of Fire" follows Budge's own Śe-nesert and the house nsrt 'flame, fire'.

### For the glosser and pass 2

- New lemmas: biꜣ, btn, bḥnt, imy-wrt, ipn, isk, mḥyt, ptḥ, rwd, srf, swt (the particle; note that the house's swt elsewhere is Seth, under stẖ), sḫmt, wnš, wḥꜥ, wꜥrt, šwyt (light (?) · a second word of the same spelling: shade, shadow), ḫꜣḫ, ṯsm, ꜥqy, š-nsrt.
- To broaden: nwt (+ bonds (?); + a weapon or tool (?)), sꜣḥ (+ Sah, Orion), ny (check that it covers nt), ḫr (+ 'from', with persons), rd (+ rtw, 'thigh (?)').
- Pass 2 should re-read U5 and U16 as wholes, the two least certain passages.

## Pass 2

Both files were edited by script (`review2_023024.py` in the reviewer's scratchpad). Each old value was asserted before it was replaced. The glosser had worked from the units as they stood before pass 1, so the lemmas were reconciled after the edits. Checks re-run after the edits: the 647 signs equal the packet, morph covers each glyph once, det tr is empty, O34 carries z, and there are no Budge-isms. Every morph lemma in units.json is now a key of known-lemmas.json or of gloss.json, and gloss.json has no unused keys. Every `__broaden__` entry starts with the known entry copied exactly, followed by " · ".

Counts: 1 major, 7 minor, 2 style.

### Changes (gloss.json)
- rwd · **major** · The entry repeated pass 1's error, "stative rwd 'are firm'"; in this text rwd stands before its subject. · It is now "to be firm, hard, strong (verb; a later spelling of rwḏ; Budge: ruṭ)".
- __broaden__ šwt · minor · The lemma is no longer used, since pass 1 filed the word under šwyt. · The entry is removed, and its sense is moved into šwyt as "a second word of the same spelling: shade, shadow".
- __broaden__ sꜣḥ · minor · The entry was missing, so the house gloss "toe" alone would have covered Orion. · Added: known entry · "a second word of the same spelling: Sah, Orion … (god's name; Budge: Saḥu)".
- __broaden__ sgr · minor · The house has sgr only as a verb, but U16 uses the noun sgrw 'silence'. · The noun is added.
- __broaden__ dmḏ · minor · The house sense "unite, join together" does not cover 'gather' in U13, U15 and U17. · 'gather, collect' is added.
- imy-wrt · minor · The glosser gave an invented literal sense, "the one on the great side". · It now reads "the west side, the West; first the starboard side of a boat (also written feminine, imt-wrt; Budge: àmt urt)".
- swt · minor · The glosser invented the sense "'as for … indeed' (?)". · It is now the enclitic particle "but, however", and the entry notes that the same letters write Seth's name, which is filed under stẖ.
- biꜣ · minor · The entry was tied to this passage ("the metal of the opening-of-the-mouth tools") and claimed too much. · It now gives a general sense.
- wḥꜥ, ḫꜣḫ · style · Both entries carried remarks about this passage's sign coding. · The remarks are removed, so the entries are general to the lemma.
- ipn, nwt broaden · style · Both entries were worded for this passage only. · They are reworded to be general to the lemma; nwt's "weapon" sense is marked doubtful.

### Second read of units.json
No further changes. Re-checked and kept:
- U5 and U16 as a whole: their notes say plainly where the sense is unclear.
- U17 `l` "him-whose(-is)-it": it matches the note's reading, and it is marked uncertain.
- U9 `i` "every spell" for ḥkꜣ nb, which `l` gives as "magic · all": the sense is the same.
- U12 rdi … n 'given to': Budge's 'made into' is given in the note.

The other glosses (ptḥ, sḫmt, wꜥrt, wnš, bḥnt, btn, ṯsm, ꜥqy, mḥyt, š-nsrt, isk, srf, and the rd, ḫr and r broadenings) match the text and the house style, and the names carry Budge's spelling.
