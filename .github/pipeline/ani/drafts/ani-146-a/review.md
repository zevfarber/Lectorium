# Review — ani-146-a (Spell 146, pylons 1–6, Plate 11)

## Pass 1

All edits were made by script (`review1_146a.py` in the reviewer's scratchpad). The script loads the JSON and writes it back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, which matches the drafter's file. A second script (`check146a.py`) compared the result with the packet and confirmed these points:
- the 632 sign codes, joined in order, are unchanged and equal the packet's sequence;
- every unit's `ln` is the packet line of its first glyph (pylon-relative, as printed), and `"p": true` stands on each pylon's title, its "said by" unit and its first speech unit, as in ani-147-a;
- every word's `rubric` flag matches the packet;
- every unjoined word's `q` equals the packet's layout, and the 3 joins (U5 iry-ꜥꜣ·s, U10 iry-ꜥꜣw·s, U15 iry-ꜥꜣ·s, each Budge's àri + āa-s) are re-indexed correctly;
- every morph `g` list covers each glyph of its word exactly once;
- every det has an empty `tr`;
- the restored glyphs are exactly the ones Budge brackets (w43 X1, w48 X1, w58 X1, w82 D21, w168 Z1, all eight signs of w172 θennu), and each note says so. w176 urṭ-[àb] has brackets only in the transliteration and is rightly not flagged.

Every genitive "of" written n/nt/nw is keyed `ny`; every negative D35 is `n`; the dative n (U4, U25) is `n`. No Budge-ism (triumphant, saith, homage, thee/thou, hath) appears in any `l` or `i`. `say` forms checked against the house (·tw·s → -tues as in ir·tw·s "irtues"; ordinals as in ani-147-a/b).

Counts: 2 major, 2 minor, 2 style.

### Changes

- U3 w18 `srt` · n, l, i · major · The note opened "The papyrus writes r, n and t …; read srt", the formula for a slip the sense allows only one way. The reading is Budge's footnote emendation ("Read [s over r] t A2 sert"): it adds a sign and drops another, and Budge himself prints only dots in his text line. That is a guess, not a forced correction, and the `l`/`i` gave "who-foretells" without a query · The note now says what stands (r over n over t, with the man with hand to mouth, which gives no known word), gives Budge's footnote as an emendation followed only with a query, and says the reading is doubtful. `l` "who-foretells(?)", `i` "who foretells(?) words". The reading `srt` and the signs are unchanged.
- U24 w130 · reading, say, morph lemma, n, l, i · major · The note corrected r-š-i-t + nose to šrt 'nose' ("with r and š changed round"). The signs as they stand give rš 'rejoice', which takes the nose D19 as its regular classifier, so the sense does not allow only one reading, and the conventions say to translate what stands. ḥꜣw 'breath' rested only on Budge's 'nostrils' · reading `šrt` → `ršit`, say `sheret` → `reshit`, lemma `šrt` → `rš`; `l` "fire · lady · of-abundance(?) · of-joy(?)", `i` "Fire, lady of abundance(?) of joy(?),". The note gives the reading as it stands, ḥꜣw as perhaps 'excess, abundance' (?), Budge's reśàt / 'breath' and the metathesis šrt as the alternative, and says both words and the sense are doubtful.
- U20 · n · minor · "(Budge: āu)" against the reading iwt, with no reason given · now "(Budge: āu; no arm ꜥ is written, and the young animal is the sign iw)".
- U31 · n · minor · "(Budge: āu-s, 'her breadth')" against ꜣw·s 'her length', with no reason given · now adds "his ā is not in the signs, and the sign is ꜣw".
- U31 · l · style · "is-known-(one)" mixed the passive and the impersonal. The house renders the sḏm·tw·f of rḫ as "is-known" (ani-022-072) · "not · is-known · length-her · breadth-her".
- U10 · l · style · "(it-is)" put the written pw in parentheses, which the house keeps for unwritten words; pw is always "it-is" (ani-017-a/b, ani-125-address) · "Mes-Ptah · it-is".

### The drafter's "The papyrus writes X; read Y" corrections

- w18 srt (U3): withdrawn as a correction (above); kept as a queried reading.
- w130 šrt (U24): withdrawn (above); the signs are read as they stand.
- w73 second mꜣꜥ-ḫrw (U12): kept. A dittography across Budge's numeral 6 and the blank he records ("[⅜ in. blank]", confirmed in both readers' files), marked (sic) by Budge; no other reading of a doubled epithet is possible.
- w157 hmhmt (U30): kept. m-h-ꜣ-h-t gives no word as it stands; after ꜥꜣt 'great (of)' only hmhmt 'roaring, war-cry' fits, and Budge reads the same (hemhat, 'shoutings'). The note names both changes (the owl set first, ꜣ for the second m).
- w166 šꜣꜥ (U32): kept. After n gm·n·tw qd … m, 'since the beginning' is the sense, and Budge marks the s (sic). šꜣs 'travel' would need the walking legs, not the roll.
- w176 wrd-ib (U34): kept. The epithet is written correctly at the fourth pylon (U19), Budge marks the face (sic) and transliterates urṭ-[àb]; wrd-ḥr is not a known name.

### Considered and refused

- U9 `l` "above · person · every" for r bw nb, where bw is 'place': kept. bw nb here carries the man and woman classifiers, and the note explains bw and the idiom 'everyone'.
- U32 `i` "Her like" where qd has no ·s: kept. The possessive is the English for a likeness of the pylon spoken of, and it adds no claim the note does not make (cf. ani-147-b pass 1, U23).
- U34 `l` "before" for the two words ẖr ḥꜣt: kept. It is a compound preposition, and the note gives both parts and both senses (in front of / earlier than).
- U25 the analysis of n hꜣ n sdbḥ·tw·s and U26 "while his head is (on him)(?)": kept. Both are marked doubtful and give the alternatives (sdbḥ 'equip'; ·s for ·f); a reading of the n after hꜣ as the sḏm·n·f was weighed and gives no clearer sense.
- U4 wꜣy 'the one gone far' against Budge's 'destruction', and U14 smrt 'companion' against his 'beloved': kept; the signs support them (walking legs; s + mr), and each note gives Budge's view and says the word is doubtful.
- U2 sbtyw read as plural with two strokes and plural strokes (Z4 could mark a dual 'the two walls'): kept; the plural strokes Z2 follow.
- U12 in "says" with no ḏd: correct per the packet (w69 has its own overline and no t'et), and the note says so.
- U19 wrd and ib as two words, U34 wrd-ib as one: both follow Budge's groups (urṭ / àb vs urṭ-[àb]); the l/i rendering "the Weary of Heart" matches ani-001-b ("the-Weary · of-heart").
- Names (Neruyt, Mes-Ptah, Sebaq, Negau, Hentyt-arqyu, Sematy): each note quotes Budge's transliteration exactly as the packet has it and marks the meaning doubtful.
- Pylon 1 sbḫt tower vs pylons 2–6 L-shaped frieze sign, all coded O16: the U0 and U6 notes describe each as printed.

### For the glosser

Lemma key changed in this pass: `šrt` → `rš` (U24 w130; reading ršit 'joy' (?), the verb rš 'rejoice'). The key `šrt` is no longer used.

New lemmas (not in known-lemmas.json): hmhmt, ms-ptḥ, ngꜣw, nrwyt, rš, sbty, sbꜣq, sdbḥ, smr, smꜣty, snk, stꜣw, sꜣr, ḥfꜣw, ḥntyt-ꜥrqyw, ḫbḫbt, ṯni.

Known entries whose sense here is different, so the build would show the wrong gloss unless they are broadened (`__broaden__`):
- sr — known only as "official, magistrate"; here (U3) the verb sr 'foretell, make known', srt (?) 'who foretells' (doubtful; Budge's footnote: sert).
- ḥnwt — known only as "deceit, wrongdoing"; here (U8, U18) ḥnwt 'mistress (of)', a second word of the same spelling (noun f.; the cup W10).
- ḫt — known as thing / wood / stairway / rear; here (U24) ḫt 'fire, flame' (noun; with the flame classifier; Budge: χet).
- ḥꜣw — known only as "nakedness"; here (U24) perhaps ḥꜣw 'excess, abundance' (?) (noun; Budge renders 'breath').
- qd — known only as "to build"; here (U32) the noun qd 'form, likeness' (Budge: qeṭ, 'the like').
- ꜣw and wsḫ — known as verbs/adjectives 'be long', 'be broad'; here (U31) as nouns 'length', 'breadth' with ·s. A short addition each.
