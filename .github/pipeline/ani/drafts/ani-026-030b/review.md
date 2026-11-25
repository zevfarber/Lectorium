# Review — ani-026-030b (Spells 26 and 30B, Plate 15)

## Pass 1

All edits were made by script (`review1_026.py` in the reviewer's scratchpad). The script asserts each old value before replacing it: each text replacement must match exactly once, and each glyph tr, lemma, l, i and q is checked first. The file was written back with json.dumps(ensure_ascii=False, indent=1), the draft's own indent, without a trailing newline as before. No glyph code was changed or moved. One join was made (U9, srwd + n). A second script (`check_026.py`) confirmed after the edits:
- the 617 sign codes, joined in order, equal the packet's sequence;
- every morph `g` covers its word's glyphs exactly once;
- every det has an empty `tr`, no other role has an empty `tr`, and every non-suffix O34 carries z;
- every word's `rubric` flag matches the packet glyph by glyph (U0 rꜣ n rdit ib n; U14 rꜣ n tm rdit ḫsf·tw ib n, ḫr·f m ẖrt-nṯr; U15 ḏd·f), and the notes say "in red" for exactly these;
- `restored` stands on exactly the bracketed glyphs of the packet (A1 of im·i; r; ḥr with its stroke; A1 of ḫprw·i), and the notes say so;
- `ln` of each unit is the packet line of its first glyph (Spell 30B restarts at 1);
- no Budge-ism ("saith", "triumphant", "homage", "thy/thee", his name forms) in any `l` or `i`.

Joins and splits, re-indexed: iw | n·i (U2, U5) `0-1-2:3` → `0-1` + `0:1`; wn | n·i (U6) and sšw | n·i (U7); dwn | wi (U10) `0:1-2:3-4-5` → `0:1-2:3` + `0-1`; irw | wḏ·n·i (U11); ḥtp + nṯr → ḥtp-nṯr (U14) `0:1*2` + `0-1` → `0:1*2-3-4`; pr | n·k (U20) `0:1:2-3:4` → `0:1:2` + `0:1`; and in this pass srwd + n → srwd·n (U9) `0-1:2-3-4-5` + `—` → `0-1:2-3-4-5-6`. All are stated in the notes.

Counts: 1 major, 10 minor, 2 style.

### Changes

- U9 srwd·n · words (join), l, i, n, say · **major** · The draft took the lone water n after srwd as in 'by' with its reed unwritten, and srwd as an infinitive with an agent. That supplies a sign the papyrus does not have, when the signs as they stand give a regular form: srwd·n inpw mꜣsty·i is verb, n, noun subject, object, the sḏm·n·f. The `i` ("so that they lift me up") also did not match the `l` ("may-raise-up · for-me"): r·i is 'for me', not an object. · n joined to srwd as srwd·n (morph srwd [0–5] + sḏm·n·f [6]; N35 phon n; say `seruden`; q re-indexed). `l` "has-made-firm · Anubis · knees-my · raised · for-me"; `i` "Anubis has made my knees firm, raised up(?) for me." The note gives the join, the sḏm·n·f, and the (i)n reading as the alternative and why it is weaker.
- U9 ṯsw · n · minor · The note called ṯsw "the prospective, its subject (the knees) not written". The prospective sḏm·f does not normally drop its subject. · Taken as the stative of ṯs after the noun it describes ("raised up"), its w the ending; still marked uncertain.
- part · minor · "the heart not opposing" did not render the Spell 30B title as the draft itself translates it (and 023-024's part name follows the spell titles). · "Spells 26 and 30B — giving the heart; not letting the heart be turned back (Plate 15)".
- U5 sḫr, U7 sšw, U9 srwd·n and ṯsw, U21 sḫnš · glyphs (tr only) · minor · The bolt O34 had tr `s`. The house (conventions; every published part, 202 + 13 cases) gives the bolt tr `z`, with s in reading and say. · tr → `z` in all five; readings and say unchanged.
- U3 ꜥmw·i · n · minor · "ꜥm …, which sounds much the same" over-claims: i and ꜥ are different consonants. · Now "with the reed sound i written where the arm ꜥ is meant", and the note adds that the signs are left as they stand. The reading ꜥmw·i(?) is kept (see refused).
- U8 irty·i · n · minor · The note disagreed with Budge's maa without saying why. · Added: a pair of eye signs with a suffix is the ordinary writing of the dual noun, and Budge's own English is "my two eyes".
- U8 šdntt · n · minor · The note said "the second t belonging to its ending", which makes the first t part of the stem, while the lemma is šdn. · Now "one t being its ending … the other t is not explained". Lemma šdn kept.
- U13 ḫni·tw · morph · minor · The reading is ḫni (as the signs stand) and the rendering is from ḫnr 'restrain, shut in', but the lemma was ḫni. The glosser would have glossed ḫni (a different verb) under a rendering that belongs to ḫnr. · Lemma → ḫnr; the note says the word is filed as a writing of ḫnr. Reading kept as ḫni·tw, uncertainty kept.
- U14 tm rdit · n · minor · "tm … with the infinitive rdit after it" was the wrong form. tm is itself the infinitive after rꜣ n, and the verb after tm takes the negatival complement. The house (weighing scene, irt after m) calls a t-written form there "the negatival complement, written with t". · Note rewritten to match.
- U17 ḏꜣḏꜣt · n · minor · The eared ring (W24) and the barred sign (N1) were listed as if they were ordinary classifiers. They are unexplained, as the weighing-scene note says of the same place. · Added "The ring and the barred sign are not explained, and they are not read."
- U3 šꜥt · (for the glosser) · minor · The known glossary entry šꜥt is "slaughter … · letter, document". Built as it stands, the word glossed 'cakes' here would show "slaughter". · No edit to units.json. The glosser should put šꜥt under `__broaden__`: the known entry whole + " · a third word of the same spelling: a kind of cake or loaf (noun f.; with the grain classifier; Budge: śetā)".
- U13 · l · style · `l` had "[from]" and "[at]" for the words Budge restores. Published parts do not bracket restored words in `l` (the brackets there mark gaps, "[…]"); the note says they are restored. · Brackets removed.
- U21 rmṯ · n · style · The note did not say the m is unwritten. · "its m not written" added.

### The drafter's flagged doubts

- w25 ꜥmw·i (Z11, tr im) read as ꜥm 'eat'. Kept, with the wording fixed above. As written, im(w) gives no known verb, and the A2 classifier asks for a verb of eating. ꜥm is the nearest word that fits the signs. The glyph keeps its value im, as the house does when a reading departs from a sign (023-024 "ir; read in", D21 tr r). Because the reading is a guess, the note does not open with the scribe-error formula. Instead it says plainly, with a query in `l` and `i`, that the signs give im.
- w104 ḫni·tw as ḫnr. Kept as a guess, marked uncertain. Only the lemma was fixed (above). The context (the ba kept from the corpse) and Budge's 'imprisoned' agree with ḫnr, and nothing in the signs supports another sense.
- w76 dwn + wi. Kept. G43 + A1 is the house writing of wi (ani-017-c, ani-125-address). A pronoun object before a noun subject is regular. The note gives dwn·i as the alternative.
- w135 ḫr n·f → ḫr·f. Kept. The note opens with the formula, the glyphs are unchanged, and N35 keeps phon n, as in 023-024's wdn·n·f. No sensible reading keeps the n. The whole word carries the rubric flag, and the note says that Budge's overline starts over the n.
- w71 lone n as (i)n. Changed (major, above).
- w62 ꜥrty·f. Kept. The second X1 as comp t and the final Z4 as the dual strokes after a suffix (morph ·f [7, 8]) match the known entry for ·f.
- w85 ḥwt-kꜣ-ptḥ with R8. Kept. The flag after Ptah's name is left unread and called a possible god classifier, and the note says so. The model's ḥwt-kꜣ-ptḥ has the same reading and say.
- w7 n·f in the title. Kept. Taking the second n as the genitive and n·f as 'to him' gives a clean title, and the note gives Budge's alternative.
- w174 ḥn·n. Kept. The note says that both the sign (U6 approximate) and the sense are uncertain and points to the weighing-scene copy. The lemma ḥn is the house entry "to hasten (?)".

### Findings refused

- U4 ḫnt·k, Z4 as det "not read": the strokes could write the y of the infinitive ḫntyt. Not changed: the draft's reading is defensible, and nothing turns on it.
- U1/U15 etc. ḥꜣty, F4 phon (weighing has log): both roles are used in published parts (ani-125-address phon). Not changed.
- U15 sp sn unhyphenated: ani-023-024 (the latest part) writes "sp sn"/`sep sen`, the weighing scene "sp-sn". Left as the latest part has it.
- U6 ꜥꜣwy say `aawy` (w before y): matches the house `awyi` for ꜥwy·i. Not changed.
- U12 the D36 "classifier" of the second sḫm·i: it might be the forceful arm D40 in Budge's type. Codes are established, and the note already calls it another form of the classifier. Not changed.
