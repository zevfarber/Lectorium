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
