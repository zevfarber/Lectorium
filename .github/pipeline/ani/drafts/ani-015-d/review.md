# Review — ani-015-d

## Pass 1

Units are numbered from 0 in the order of `sentences`. I checked all 26 units and 155 packet words against the packet, conventions.md, the model and the published parts. Every word was also compared by script with every published word (all `ani-*.json`) that has the same sign sequence. The only differences were ḥr (D2 Z1) coded phon here where the house has log 60 times to 12, and the say of n·i. Both are changed below. I did not change any sign code or the order of the signs. After editing, all of these checks pass:
- the JSON loads;
- the concatenated sign sequence equals the packet's (557 glyphs);
- morph `g` covers every glyph of every word exactly once;
- every `q` indexes its word's glyphs exactly;
- there are no `s`/`t` fields;
- every det has an empty tr, and no other role does;
- the `ln` of every unit matches the line of its first packet word.

The only rubric word in the packet is w56 (pr·k). It is flagged, and U9's note says it is red. The packet has no restorations. Every join and split is stated in its note:
- joins: ḥr-ntt, mꜣꜣ·n·sn, ḥtp-nṯr, and (new, see below) sk·n;
- splits: di·k | wi, ir·tw | n·k, ḥsq | n·i, ṯsw | n·f.

I re-indexed `q` on each of them and checked it by script.

### Changes
- U20, U21 · words (unit boundary), reading, say, morph, q, l, i, n · major · Three problems:
  - The same words stand in the first part of the spell (ani-015-a U20: sktt sk·n·s pḥ sw, "the Sektet-bark has hauled(?) and reaches him"). There sk·n is a sḏm·n·f and pḥ sw is "(it) reaches him". The draft instead read sk n sktt as "the towing of the Sektet-bark", a noun phrase standing for a clause.
  - The draft took sw as "it, the bark", but sktt is feminine and sw is masculine.
  - The draft made qdt rꜥ the subject of pḥ. That breaks a sentence that needs no verb: qdt rꜥ m ḥꜥꜥwy is built like U24's nṯrw nbw m ḥꜥꜥw, and Budge also reads two clauses here.

  What was done:
  - sk + n are joined into sk·n (say seken; morph sk [0–3], sḏm·n·f [4–5]; N35 tr n; q "0-1-2-3-4:5").
  - pḥ and sw move from U21 to U20.
  - U20 now reads l "has-hauled(?) · Sektet-bark · reaches · him", i "the Sektet-bark has hauled(?) and reaches him;". Its note cites 015-a, gives sk n sktt "one hauls for the Sektet-bark" as the other possibility, says that sw cannot be the bark, and calls the sense of sk uncertain.
  - U21 (still ln 46) is now qdt rꜥ m ḥꜥꜥwy: l "crew(?) · (of)-Ra · in · rejoicing", i "the crew(?) of Ra are in rejoicing." Its note labels the sentence as having no verb.
- U0 · n · minor · The note opened "The papyrus writes n-r-w-i-w …; read nrw". Writing nrw sign by sign without the vulture is a spelling, not a slip. The formula belongs only to slips corrected in the reading (conventions, "The scribe's mistakes"). · The formula is removed. The note now says nrw is spelled out sign by sign and that the i and the second w are not read.
- U24 · n · minor · Same misuse: "The papyrus writes n-t-r-w without the flag; read nṯrw". Writing nṯr phonetically with t for ṯ is a spelling. · Now "nṯrw 'gods' is spelled out here without the flag: …".
- U1 · n · minor · wr·f was labelled "an adjectival sentence with the suffix as subject". An adjectival sentence takes the dependent pronoun (wr sw); with a suffix, wr·f is the sḏm·f of the adjective-verb. · The label is corrected and wr sw is given for contrast.
- U7 · n · minor · wḏ was called "a passive form after its subject". The passive sḏm·f comes before its subject. A verb form after a noun subject after ḥr-ntt is the stative (ntt + noun + stative). · Now "the stative after its subject sꜣ, the usual pattern after ḥr-ntt".
- U7 · n · minor · sqdd·f was called "a sḏm·f of wish with the last consonant doubled". The geminated form of a 3ae-inf verb is not the form of a wish, and the previous part writes the Sektet-bark sqdt with the same two hands. · The note now says it is taken as a wish like ḫnm·f, that the doubled hand may be only a spelling (it cites sqdt) or the geminated form, and that the form is doubtful. The reading sqdd·f is kept.
- U7 (also `about`, `part`) · l, i · minor · "sail into the Field of Reeds": the preposition is m 'in', not r. · Now "in" in l, i, about and part.
- U5 · n · minor · Budge's one group ṭā-kuà can be read as the stative di·kwi, "I am placed among the revered ones". The k + seated-man writing of ·kwi is house (nn·kwi in ani-074…). The note gave only the split, though both readings fit the signs. · The split di·k | wi is kept, since mk-wi with A1 alone as wi is attested in the published parts. The note now gives di·kwi as the other reading and calls the split doubtful.
- U10 · glyph role/tr, n · minor · In biꜣ, X1 was coded det with an empty tr. t is a sound sign. House practice codes an unread phonogram as phon and says it is not read. · X1 is now phon t. The note says "with t (not read in biꜣ)".
- U16 · n, l · minor · The note read "m sp·f 'at its time'", but no m is written: the packet has àbṭu then sep-f, and Budge's [in] is in his English only. l had "at" as if it were a word. · The note now says no preposition is written and that the noun is used as an adverb. l is now "(at)-time · its".
- U17 · n · minor · ḏwt ḫr had no form label. · Added: taken as the content of the wish, the verb with its ending unwritten. A stative would show t after the feminine subject.
- U18 · n · minor · ḥsq, translated "It is cut off", had no form label. · Added: "taken as a passive with no subject written". The note already gives the sḏm·n·f alternative, and it stays.
- U19 · n · minor · wnn rꜥ had no form label. In this string of promises the sḏm·f of wnn usually looks to the future. · Added the label, the note that the form is often future ('Ra will be'), and that the present tense is a choice. i is unchanged.
- U22 · n · minor · sḫr, "is felled", had no form label. · Added "taken as a passive sḏm·f … with its subject ḫfty 'the enemy' after it".
- U25 · n, l, i · minor · The note treated in as "says N", exactly as at line 39. Here, though, the promises it closes speak to Ani as "you", so "says N" is harder, and l/i showed no doubt. · The note now says this and calls the reading doubtful. l is "says(?)", i "So says(?) the Osiris, …".
- U0 · l · style · i had "far(?)" but l had "far". · l is now "far(?)".
- U3 · l · style · l rendered r as "in". The Egyptian is r. · l is now "at". i keeps "in the West" as English.
- U4 · n · style · The note did not say why the word order is odd. · Added: after mk the subject normally comes first (mk isft ḥꜣ·k).
- U7 · l, i, n · style · "joy of heart" is Budge's English word for word. It is not literal (the note itself says 'length of heart'). · Now "gladness-of-heart" / "with gladness of heart". The house renders ib … ꜣw 'glad' (015-a).
- U15 · n · style · The past-tense mꜣꜣ·n·k among future promises was left unremarked. · Added that the past tense is kept as written.
- U23 · i · style · "with Thoth and Maat on either side of him" made Thoth and Maat Horus's companions. They are further objects of "you have seen". · Now "and Thoth and Maat on either side of him".
- U15, U23 (×2) · glyph role · style · In ḥr (D2 Z1) the face was coded phon. The house codes it log 60 times to 12, and 015-b codes it log 12 out of 12. · Changed to log. ḥr-ntt keeps D2 phon, as in 017-c and 017-d.
- U18 · say · style · n·i was "eni". The published parts have "ni" (015-b, twice). · Now "ni".
- U11 · say · style · ir·tw was "iretu". The published parts have "irtu" (017-d, 044…). · Now "irtu".
- U12 · say · style · nis·tw·k was "nistuk". By the rule (e between consonants), and following ms·tw·f "mesetuef", it should be "nisetuk". · Now "nisetuk".
- about · style · "Horus with Thoth and Maat in the bark": the text does not say "in the bark". · Now "at his sides".

### Refused
- U0 ḥrw st·f r isftyw, read as ḥri 'be far': the signs (ḥr, r, w, U15) allow it. The note already calls it doubtful and gives Budge's 'fortifying', and i has (?). I considered ḥry st·f 'who is upon his seat', but there is no y and r isftyw is left hanging. Kept.
- U0 isftyw, G1 phon ꜣ (not read): this is the house coding of the same ending in ḫftyw·k (015-c). Kept. (The bird may be the buzzard tyw, G4, in the original, but the code is the established reader's.)
- U1 ꜥḏt, X1 coded comp t and D46 comp d: the same coding as 015-a's ꜥḏt and 015-b's mꜥnḏt. Kept.
- U1 wr·f ꜣw "great is he and long(?)": doubtful, and the note says so. Kept.
- U4 mk ḥꜣ·k isft, with no verb: I tested reading the owl and arm as imi 'put!' (the imperative of rdi), which would supply Budge's verb. But then the k after it stands alone, and ḥꜣ·k has its own k. The draft's reading is kept and called doubtful. D36 in mk / m-m / mfkꜣt stays phon ꜥ (not read): the house codes the arm both ways (det in 147-a and the weighing, phon ꜥ in 125-introduction and 074).
- U5 di·k | wi: kept, with the stative as the alternative (see Changes). The house writes mk-wi with A1 log wi (074).
- U6 tꜣ-ḏsr with U15 coded where D45 is expected: no "papyrus writes" formula. The issue is the code, not a slip. Throughout these plates U15 is the house's code for the flat arm (read ꜥ), and D45 is an arm with a wand. The note says this and that the reading rests on Budge. Kept.
- U7 ḥr-ntt written with Z4 (n, t, two strokes): 017-c and 017-d have the identical spelling and coding. The note's "as elsewhere on this papyrus" holds. Kept. sꜣ on an Aa17 approximation: the note says it rests on an uncertain sign, and l/i carry (?). Kept.
- U8 and U25 in as "says N" rather than Budge's vocative "O": the call is i (015-c U0, written with A26), and in after a speech naming the speaker is the known use. U8 is kept as is. U25 is now marked (?) (see Changes).
- U10 biꜣ 'firmament' with ꜣ unwritten and no sky sign; snsn 'keep company with' (the known entry is only 'smell, breathe'); sbꜣw 'stars' (the known sbꜣ is only 'door'): the readings are right and the occurrence glosses separate the senses. The glosser must `__broaden__` snsn and sbꜣ. Kept.
- U15 bꜥbꜥt: a new lemma, its sense doubtful, and the note and i say so. Kept.
- U17 ḫpr ḏwt ḫr … ḫft sr·n·f: the gap is reported exactly as Budge prints it, with nothing restored, and the whole sentence is called doubtful. sr·n·f is correctly a sḏm·n·f (Budge's ser-nef). Kept.
- U18 split of ḥsq | n·i and ṯsw | n·f: Budge's one-group ḥeseq-nà could be the sḏm·n·f ḥsq·n·i 'I have cut off'. The note gives that reading, and the sentence is called doubtful. ṯsw n·f "of him", rather than the dative "for him", is a choice the note explains. Kept. (Open question for pass 2 and the glosser: the lemma is ṯst, noun f., but the written form ṯsw shows no t.)
- U20 sk read from a V28 code: the house coding (015-a). Kept.
- U21 qdt 'crew(?)': doubtful, and l/i carry (?). Kept.
- U22 nbt-ꜥnḫ: the name is translated where it is transparent, and the note does not guess the goddess. nḏm on V28: the house coding (015-a U5). Kept.
- U23 nfrw left as "the neferu(?)": Budge's own '(?)' and the unidentified sign justify leaving it. Note for the glosser: the lemma key nfrw is the known 'beauty'. The occurrence gloss calls this "a word not understood", so either it gets a lemma key of its own or nfrw is broadened. Kept for pass 2.
- U24 iw labelled a participle after mꜣꜣ + object: the stative would also fit, but the participle is the known gloss's own use (iwi). Kept.
- p: only U9 has it, where the red section begins. U8 and U25 are say-lines without p, as in 015-b and 015-c. Kept.
- Budge-isms: none in l/i after the "joy of heart" change. I checked thee/thou/thy/saith/homage/triumph/glorious/victorious/behold/shining ones/netherworld/venerated/sailors/look out/make glorious/set in order. "Power of the powers", "Praises are made for you", "her heart is glad" and "to make the hearts of the spirits live" agree with Budge only because they are the literal words. House renderings agree with the published parts: "the Osiris (the scribe) Ani", "true of voice", the Sektet-bark / Adjet-bark, the Disk, the necropolis, the Sacred Land, the Field of Reeds, and the says Seketet / Adjet / Ta-djeser / Sekhet-Iaru / Nebet-…

## Pass 2

I re-read all 26 units afresh (numbered as in Pass 1) and checked every gloss.json entry against the text, the grammar and the packet's Budge spellings. Every word was compared by script with all published words that have the same sign sequence (reading, roles, tr) and the same reading (say). The only house difference is int (U15): the one published int codes the first fish det, while this part codes it phon in with i and n as complements. Both are defensible, so it is kept. Sign codes and order are untouched. After editing, these checks pass by script:
- both files load;
- the sign sequence equals the packet's (557 glyphs);
- morph `g` covers every glyph once;
- every `q` indexes its word exactly. Unchanged words carry the packet's q. The joined words (ḥr-ntt, sk·n, mꜣꜣ·n·sn, ḥtp-nṯr) and the split ones were re-derived and match;
- no det has a tr, and no other role has an empty one;
- there are no `s`/`t` fields;
- every `ln` matches its first word's line.

The gloss keys equal the lemmas used minus the known-lemmas keys (11: ḥri, isfty, imꜣḫy, sqdi, ꜣwt-ib, ḥknw, bꜥbꜥt, dm, qdt, nbt-ꜥnḫ, sꜥnḫ). The sk·n restructure added no lemma, since sk and sḏm·n·f are both known. Every `__broaden__` key is a known lemma that the units use, and each value begins with the known entry copied by script + " · ".

### Changes — units.json
- U0 · n · minor · ḥrw st·f had no form label · Added: taken as a participle with its noun after it, 'far of seat', the same pattern as ꜥꜣ nrw.
- U0 · n · style · "isftyw … is i, the tall sign is as in isft (coded …)" did not parse, and "the vulture, as in the plural ḫftyw" did not say what the vulture does · Now "i, the tall sign is (coded Y1a, approximate, as in isft), s, f, t and the vulture standing for the plural ending, as in ḫftyw".
- U0 · n · style · Added that Spell 17 (017-f) also writes nrw without the vulture. This is the evidence that the spelling is attested (see Refused, (a)).
- U8 · n · minor · The note did not mention that in Spells 18 and 146 the say-line in N stands *before* the words it introduces. A reader could take U8 as opening the promises · Added that sentence, and the reason it is taken as closing here: the words after it speak to Ani as 'you'.
- U11, U12 · l · style · "made · one · for" and "called · one · you" are not in the house's form for the sḏm·tw·f. 015-a has stꜣ·tw as "is-towed" · Now "is-made · for · you · praises …" and "is-called · you · in …".
- U17 · n · minor · "the verb with its ending unwritten (a stative would show t after a feminine subject)" contradicted itself · Now: the form of ḫr is not clear, since a stative after the feminine ḏwt would usually show its ending t, which is not written.
- U18 · n · minor · Two problems. ṯsw has the lemma ṯst (noun f.), but nothing said why there is no t (pass-1 open question). dmw was "a passive form" with no name · Added "the plural of ṯst 'vertebra' with the t of the feminine not written". dmw is now "a passive sḏm·f, with the w the passive sometimes shows". The reading ṯsw is kept as written, and the lemma stays ṯst (the house lemma for the noun, 044 U27).
- U21 · n · style · The note did not say that qdt 'crew' is not the usual word · Added: the usual word for a boat's crew is sqdw (from sqdi), with an s that is not written here.
- U24 · i · minor · i "when they see Ra" did not match l "have-seen · they", the sḏm·n·f the note names. U15 keeps the past tense as written · Now "when they have seen Ra coming in peace".
- about · style · "Horus with Thoth and Maat at his sides" is the reading Pass 1 removed from U23's i (Thoth and Maat are further objects of 'you have seen') · Now "and Horus, and Thoth and Maat at his sides".

### Changes — gloss.json
- ḥri · minor · Budge's 'fortifying' belongs to a different reading of this one passage, not to the lemma. "(?)" and "sense doubtful" described this occurrence, not the verb, which is well attested · Now "to be far, distant, keep away (from: r) (verb; Budge: ḥeru)". The doubt stays in U0's l/i/n.
- isfty, imꜣḫy, ꜣwt-ib, ḥknw, sꜥnḫ · style · Each carried Budge's English for this passage ('wicked devils', 'the venerated beings', 'joy of heart', 'praises') · Cut to "Budge: <spelling>". ḥknw "plural in sense; written with the man with hand to mouth" described this writing · Now "praise, hymns of praise (noun m.; from ḥkn 'praise')". ꜣwt-ib now gives ꜣwt 'length' explicitly. sꜥnḫ "causative verb, transitive" is now in the house form "(verb; causative of ꜥnḫ 'live')".
- sqdi · minor · "sqdd·f 'he sails'" was pinned to the line, and its 'he sails' contradicts U7's wish 'may he sail' · Now "(verb 3ae-inf.; geminated stem sqdd; Budge: seqṭeṭ)". The geminated stem is kept as a general pointer.
- dm · minor · Three problems: "(?)", "sense doubtful" and "written with the knife as classifier" described this passage; 'let be cut asunder' is Budge's English here; the verb 'be sharp, pierce' is not doubtful · Now "to be sharp; to pierce, cut (verb; Budge: ṭemu)".
- nbt-ꜥnḫ · minor · Two problems: Budge's spelling was given as his English "Nebt-ānkh", where the packet's transliteration is Nebt - ānχ; and "a goddess (?)" doubted what the cobra classifier shows · Now "'Lady of Life', a name or title of a goddess (god's name f.; …; Budge: Nebt-ānχ)".
- bꜥbꜥt, qdt · style · Tidied to "sense doubtful, taken from Budge: …". These two keep Budge's English (see Refused).
- __broaden__ ꜥ · minor · "side, in the dual ꜥwy·f 'his two sides' (ḥr ꜥwy·f 'at his two sides')" was pinned to U23 and reproduced the line. The known ꜥ entry (dual ꜥwy 'the two arms') and ·f entry ("ꜥwy·f 'his two arms'") already cover the word, and l has "two-arms" · Removed.
- __broaden__ nfrw · minor · This resolves the pass-1 open question. The house has no numbered or "(?)" lemma keys (none among the 1041 known): homonyms share one key, joined by "a second word of the same spelling" (sr, ḥꜣ, sš …). The build fills each morph gloss from the occurrence gloss first, and the occurrence gloss on U23 already gives this word's sense. So the right shape is a broaden, not a new key. The old text "in ḥr nfrw 'at the nfrw' … perhaps 'look-out' (?) (Budge: 'the place of look out')" was pinned to the line and was Budge's English · Now "· a second word of the same spelling, not understood: perhaps a place in the sun's bark (?) (noun; Budge: neferu, with a query)".
- __broaden__ snsn · minor · The added sense carried an invented derivation ("the sense 'be joined' from the 'smell, kiss' of sn, 'touch, mingle'") · Now "· also to join, keep company with, associate with (verb; with m or m-m 'among'; Budge: sensen)".
- __broaden__ biꜣ · style · "Budge: bàt, 'the sky'; the ꜣ is not written" described this writing · Now "· also the firmament, the sky thought of as a vault of metal (noun m.; Budge: bàt)".
- __broaden__ sbꜣ · style · The star was given as a sense of 'door' · Now "· a second word of the same spelling: star (noun m.; written with the star sign; plural sbꜣw)".

### Refused
- (a) Restoring "The papyrus writes X; read Y" for nrw (U0) and nṯrw (U24). Pass 1 was right. Neither word is missing a sound:
  - n-r-w writes every consonant of nrw. The vulture G14 is its classifier (146-b codes it det), and 017-f writes nrw r-n-w with no vulture and no formula.
  - n-t-r-w writes every consonant of nṯrw, with t for ṯ as d stands for ḏ in this part's ḏḥwty.

  These are phonetic spellings, not slips. The house keeps the formula for a missing or wrong sound sign (015-b nḫn written ḫ-n; 015-a qꜣs/ḥsq out of order; 015-c ḏfḏfsꜣ for ḏfꜣw). Where only an expected logogram or classifier is absent, the house says so in plain words ("spelled out", "is not written": 015-a dwꜣw and ḥr-ꜣḫty, 015-b ind, 017-b iꜥrwt).
- (b) Pass 1's U20/U21 restructure is kept. sk·n sktt pḥ sw is the noun-subject form of 015-a's sktt sk·n·s pḥ sw (same coding of sk: S29 comp, V28 phon sk, V31 comp, U15 det). sw is the object of pḥ, and qdt rꜥ m ḥꜥꜥwy parallels U24. Re-indexed q 0-1-2-3-4:5, ln 45 / 46 and the l-order were checked by script.
- (c) U8 and U25 in as 'says N', not Budge's vocative 'O'. The house renders in + N as 'says / said by N' in every published part (018-introduction, 146-a/b, 029…, 044…), and the call 'O' is i (015-c U0). U8 stays unqueried in l/i. Its note gives the doubt, and it closes a prayer in which Ani speaks of himself as 'he'. U25 keeps "says(?)" because the 2nd-person promises before it make 'says' harder.
- bꜥbꜥt and qdt keep Budge's English in the gloss. The sense of each rests on Budge alone, and the house keeps his English for such words (015-c pass 2: msms "Budge: mesmes, 'count'"; wṯs; known sk "Budge's 'toweth'").
- ṯsw: no `__broaden__` of ṯst and no new key. The plural writing is explained in U18's note. The house gives the noun the key ṯst (044) and keeps ṯs for the verb (015-c, 026, 125-introduction, 146-b).
- int (U15) coding: see above. Kept.
- sbꜣw N14 log (the house codes it phon, but in words with house or door classifiers, where the star writes the sounds of sbꜣ 'door'). For 'star' with stroke and classifier, log is the conventions' role. Kept.
- imꜣḫyw F39 log with complement ḫ: the house codes imꜣḫ so (F39 log twice). Kept.
- Occurrence glosses on biꜣ, snsn, sbꜣ and nfrw are kept. They pick this word's sense out of a multi-sense entry, as the build expects.
- All other pass-1 decisions and refusals were re-examined and stand: ḥri, di·k | wi vs di·kwi, mk ḥꜣ·k isft, sqdd·f, sꜣ on Aa17, ḥsq | n·i, the in in U8, nfrw left untranslated, and iw as a participle. Budge-isms: none in l/i (re-checked thee/thou/saith/homage/triumph/glorious/shining/venerated/netherworld/look out/sailors/joy of heart). Says agree with the house wherever the reading is published.
