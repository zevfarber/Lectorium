# Review — ani-125-address

Drafted in four chunks (a w0–178, b w179–401, c w402–586, d w587–710), merged; reviewed in two halves (units 0–49, 50–100), two passes each. Lead's merge decisions: lemma keys ṯn (2pl dependent) vs tn (fem. demonstrative); nym→nm; wdb→wḏb; ḫw/ḫwi→ḫwi; M6 in tr made phon with t, r as complements in every occurrence; qrt and ꜥꜣ broadened for the door senses; unused entries wnmi, iꜣbi, nym, ḫw dropped.

---
## review-1
# Review — ani-125-address, pass 1, half 1 (units 0–49, Budge lines 2–24)

Input: chunks/review-in-1.json · Output: chunks/review-out-1.json (made by script; signs, glyph order and glyph count unchanged).

## Changes

Format: unit (index in this file) · field · severity · what was wrong · what I did.

1. U0 · n · minor · Aa27 was called "the bent-arm sign nḏ". Aa27 is an uncertain object, perhaps a spindle (sign-entries.json). · Now reads "the sign nḏ (an uncertain object, perhaps a spindle)".
2. U3 · n · minor · sꜥr was described as "bolt s", but the glyph is S29, the folded cloth. · Changed to "the folded cloth s".
3. U4 w2, U7 w5 · glyphs tr · minor · O34 (the bolt) in sp had tr "s". The convention, the published introduction (kꜣw·sn ·z) and the rest of this half write z for the bolt. · tr changed to "z".
4. U25 w6, U29 w12, U34 w2, U36 w2, U37 w3, U38 w3, U40 w3, U44 w3, U46 w2, U48 w3 · glyphs tr · minor · O34 used as a suffix had tr "·s", while U8 and U9 have "·z". · tr changed to "·z" throughout (the readings keep s).
5. U6 · l, i · minor (consistency) · The same clause ḥr-ntt ir·n·i mꜣꜥt was "For I did what is right" here and "because I have done what is right" in U30. · l is now "have-done · I · truth" and i is "For I have done what is right in Egypt."
6. U8 · n · minor · iwty was called "a spelling of no known word … this is a guess". But U29 (line 18) has the same word, D35 + t + vulture for -y + sparrow + strokes, and here the water n stands in for the D35 arms, which also read n. · The note now gives that explanation and calls the reading probable, not certain, citing Budge's àt "without".
7. U8 w8 · morph gloss · minor · The known-lemma gloss for grg is the verb "to speak falsehood", but here the word is a noun. · Added the per-occurrence gloss "falsehood, lie (noun; from grg "tell lies")".
8. U10 w1 · glyphs role/tr · minor · In wi the stroke Z1 was phon "w" and the quail chick G43 was det "", so each sign had the other's value. · Z1 is now det "" (the stroke standing for the 1st-person classifier, as A1 det does in U18's wi) and G43 is phon "w". The note now gives the signs in their order.
9. U10 · l, i · minor · m-ꜥ·tn was rendered "among you". The note itself says "with you, in your hands", and Budge has "by you". · l is now "in-the-hand-of · you" and i is "…the great reckoning that is in your hands."
10. U12 · n · minor · For nn ir·n·i ḫt r·f, only the "there is no one against whom …" reading was given. But the note on line 5 allows nn for n in this copy, which gives "I have not done anything against him" (the god). · Added that alternative. i is unchanged.
11. U14 · n · minor · The note said "the m and the ṯ of rmṯ are not written", but the loaf t is written and stands for ṯ. · Corrected.
12. U14 · n, l, i · minor · ḏdt rmṯ was "what people speak of" (i), "what-said" (l) and "commend" (n). ḏd X means "say X", and the relative form here has no n, so it is not past. · i is now "I have done what people say is right, and what the gods are pleased with.", l is "what-say", and the note reads "what (people) say — that is, what people hold to be right".
13. U15 · n · minor · sḥtp was "bolt s", but the glyph is S29. · Changed to "the folded cloth s".
14. U16 · l, n · minor · The l had "ferry-boat · to · the-boatless", but no n stands before iwy (Budge's w122–w123). · l is now "· (to) ·" and the note says no n is written.
15. U18 · n · minor · The verb form of ḫw was not named. It has no suffix, so it is the imperative (next to nḥm·tn, the sḏm·f). · Added.
16. U19 · n · minor · smi was "bolt s", but the glyph is S29. Also, "The great god is Osiris" was stated flatly, while U3 says "presumably". · Changed to "folded cloth s" and "presumably Osiris".
17. U20 · n · minor · The note said "ink + adjective: 'I am …'". ink takes a noun, so wꜥb is an adjective used as a noun here ("I am one pure of …"). · Label corrected.
18. U22 · l, i · minor (consistency) · The name was "Hepedra" in l and i but ḥpd-rꜣ / say "Heped-ra" in the word. · Now "Heped-ra(?)" throughout.
19. U22 · p · minor · The dead man's first-person speech starts again after the third-person narration of U21 (whose note says so), so this is the first unit of a speech. · p set to true.
20. U25 w2 · glyph role · minor · D53 in m-bꜣḥ was "log" here but "phon" in every other m-bꜣḥ in this half (U5, U9, U19). · Set to phon.
21. U26 · l · style (consistency) · l had "Maat" for the common noun mꜣꜥt, while U5, U9 and U13 have "truth". l now uses "truth" and keeps "Maat" for names (Lord of Maat, pool of Maat). · l is "testify-to · truth".
22. U29 · n · minor · The note said "The 1st person stative can express a wish" without qualification. The optative stative is mostly 2nd person. · Rewritten as "now and then used for a wish (most often in the 2nd person) … taken so here".
23. U29 · n · minor · The verb form of wddyw was not named. The doubled d is the gemination of the imperfective participle of a 3ae-inf. verb. · Added.
24. U30 w0 · morph, say · minor · ḥr-ntt had two lemmas (ḥr + nty) and say "her-entet", which is Budge's vowel. U6 and U22 have one lemma ḥr-ntt and "her-netet", and the note itself calls it one word. · morph is now [ḥr-ntt 0–4], say is "her-netet", and the note reads "ḥr-ntt (as on line 6)".
25. U30 · l · style · Same as item 21: "Maat" → "truth" for the noun. "of-Maat" is kept in the title.
26. U32 · i · style · i read "…that is empty (of it)", but the note says the text does not say what the limb would lack, so "(of it)" picked an antecedent that is not there. · i is now "There is no limb in me that is lacking."
27. U36 · n · minor · The note said in "say" is "used only after a quotation", which U44 contradicts. · Now "normally used only after the words quoted".
28. U44 · n · major · in·k "you said" comes before what is said, against the rule this half itself states for in. This was not acknowledged, and ini "bring" (same signs) is possible. · The note now gives the problem and the alternative "what did you bring them?". The translation stays with Budge's sense, now marked as uncertain.
29. U49 w4 · reading, tr, say, n · major · The word was read wdb with V24 tr "wd". V24 (cord on stick) is wḏ, and the classifier N20 is the tongue of land wḏb, so the signs give wḏb "riverbank, sandbank". Budge's "uteb" with t is his own spelling, and the signs win. · V24 tr is now "wḏ", the reading "wḏb", say "wedjeb", and the note says why. **The lemma key is still "wdb"** (the brief says to keep keys). The caller should rename it to wḏb in lemmas-all / known-lemmas when merging, since this key is plainly misspelt.

## Findings considered and refused

- U10 bꜣby, U39 bꜣq, U41 bꜣt: the second vulture has role "comp". Strictly it is a doubled uniliteral, not a complement of a multiliteral. But it is used consistently for "the doubled vulture, read once", and no other role fits better. Kept.
- U16 mḫnt and U37 nym (D36 tr "ꜥ" not read), and U40 ḥr-ꜥ (G17 tr "m" not read): in the owl-plus-arm ligature one sign is not read. Making it det "" would mislabel it as a classifier, and the notes say which sign is silent. Kept.
- U3, U8, U16 misprint notes put "The text writes X; read Y" in the middle of the note, not at its start. The published introduction does the same (units 28 and 42), and the formula itself is used correctly. Kept.
- Double reeds are given tr "i","i" in some words (nꜣy·k, šdyt, pḥwy, iri) and "y","y" in others (ꜥnḫyw, twy, mꜣꜣyw). This is untidy but does not affect any reading. Not normalised, to keep the edit small; flagged for a later pass.
- U5 ꜥ "hand" between m-bꜣḥ and nb-r-ḏr is left out of i. The note explains it, and l keeps "the-hand". Kept.
- U5 l "Lord-to-the-Limit" vs i "Lord of All": the glossary gives both (the literal name and its sense). Kept.
- U4 iwt: the draft keeps nn as the future and sets out the sḏmt·f and ·tw options with the doubt stated. Kept.
- U12: the nn + noun reading of the first four clauses differs from Budge's verbs. The grammar supports it, and the note says the sense of mtrw·i is uncertain. Kept.
- U13 ib·i: the restored suffix is flagged, and the note says it is restored. Correct.
- U20 ꜥwy: tr order ꜥ,–,y,w against reading ꜥwy follows the print order of Z4 and G43. Kept.
- U21 iy-wy: M18 tr "ii" with Z4 "y" for reading iy. This is the house's established tr for M18. Kept.
- U22 ꜥꜣ "donkey" with D53: I considered noting that it may mark a male animal, but that would be speculation. Kept as "no evident part … taken as a second classifier".
- U31 twri "taken as a stative": the final i might be the dual ending (pḥwy is dual). The note already hedges ("taken as"). Kept.
- U45 nn "these" spelled n + nw + nw + w: this might be the older demonstrative nw, but the meaning is the same. Kept.
- Lemma keys hrw (known "terror"), sḫt ("blaspheme"), ḥmt ("wife"), st ("place"), tꜣ ("be hot") and rd ("foot") are wrong for these words. Each has a correct per-occurrence gloss, which the brief allows. Kept. They are listed here so the caller knows the known-lemma glosses do not cover these occurrences.
- U1 tn has lemma key "ṯn" while its gloss text starts "tn —". This is cosmetic. Kept.
- Budge-isms ("homage", "saith", "thee/thou", "triumphant"): none in l or i. No note calls the writer "Ani's scribe".
- say: every word was checked by rule. The only fixes are items 24 and 29.

## Self-check
- Flattened sign list of review-out-1 equals review-in-1 (1297 glyphs).
- Every morph g-list covers each word's glyphs exactly once, and every q covers its glyphs exactly once (checked by script; 0 failures).

## Counts
- major: 2 (items 28, 29)
- minor: 24 (items 1–20, 22–24, 27; item 4 is counted once although it touches 10 units)
- style: 3 (items 21, 25, 26)
- Total changes: 29 items, across 29 units.

---
## review-2
# Review 2 — ani-125-address, units 50–100 of the draft (review-in-2.json, indices 0–50; Budge ll. 24–47)

Unit indices are within review-in-2.json. Output: review-out-2.json.

## Changes

| unit | field | severity | what was wrong | what I did |
|---|---|---|---|---|
| 27 | n | major | Grammar label: "ḫnd·k ḥr·n im·sn is a relative clause without a relative word". The antecedent rd·ky "your two legs" is defined, so this cannot be a virtual relative clause. ḫnd·k is the relative form, tied back by the resumptive ·sn | Rewrote the sentence: relative form after a defined noun, with the resumptive ·sn in im·sn |
| 29 | reading, say, morph lemma, glyph R14 tr, n | major | The same group (R14 + m + loop classifier) is read **imnt** (lemma imny) on the right lintel in u10, whose note argues that the West sign points to imn, not wnm. Here it was read **wnmi** (lemma wnmi, tr wnm). That is two readings and two lemma keys for one word in the same half | Unified on imn: reading imny, say imeny, lemma imny, R14 tr imn. The note now points back to imnt and gives Budge's unem and the wnmy alternative |
| 16 | morph gloss | major | Lemma key qrt is the known lemma "Qernet, the place the 4th god comes forth from" (opening part), so the glossary would show a place name for a part of a door | Added a per-occurrence gloss: "a part of a door, perhaps the bolt-socket (noun; sense not secure; Budge: qert 'bolt-socket')". **Flag:** the key itself collides with the place name. A separate lemma key for the door word needs a lemmas-all entry, so I left that to the builder |
| 10 | n | minor | "The negation is written with one n this time, not nn; the sense is the same": n sḏm·f is not the future negative | Now: strictly n + sḏm·f is "I do not (cannot) let"; in a refrain it is more likely nn written short, and it is translated as before (l keeps "not · let · I") |
| 49 | n | minor | Self-contradiction: it calls pr·tw "impersonal ('there is a going out')" and then calls ḫrw its subject | pri takes no object, so strictly the form is impersonal ("there is a going out for you"), with ḫrw standing after n·k as what goes out. Budge's passive is still mentioned |
| 30 | reading, say, morph lemma, n | minor (consistency) | "left" was iꜣbi / lemma iꜣbi here but iꜣbt / lemma iꜣby in u12: two glossary entries for one word | reading iꜣby, say iaby, lemma iꜣby. The note now says iꜣby, and its cross-reference now points to imny |
| 8,10,12,14,16,18,20,22 (n-is); 17 (sꜣḥ); 25 (wsḫt, n-is) | glyph tr | minor | S29 (folded cloth) was given tr "z". Conventions keep z for the bolt O34 only, and the published opening has S29 = s | S29 tr set to s in all 10 occurrences |
| 35 | glyph tr | minor | O34 (bolt) in st had tr "s" | tr set to z, as elsewhere in this half and in the published parts |
| 8, 17, 25, 29, 32 (twice) | n | minor | The folded-cloth S29 was described as "bolt s" (n-is ×2, sꜣḥ, wsḫt, bsw, smi) | Changed to "folded cloth s". The real bolts (ds, sš·k, st, ·sn) are untouched |
| 7, 25 | n | minor | The sign inside the O15 hall sign and the classifier of wsḫt (W10) were called "the collar". W10 is the cup (packet: "enclosure containing W10 and X1") | "collar" changed to "cup" |
| 33 | glyph role; n | minor | F32 had role log but tr ẖ, with X1 t written after it, so it is the uniliteral here. The note said "Budge reads it as a different word", but Budge's χat 'reins' is the same ẖt | role phon. Note now reads "(Budge: 'reins', the inner organs)" |
| 37, 41 | glyph role | minor | M6 in tr had role phon, but log in u0, u4 and in half 1 | role log |
| 45 | glyph role | minor | Z9 in sḏt had role phon, but log in u4, u6 and in half 1 | role log |
| 45 | l, i, n, say | minor (consistency) | "Nun" / say "Nenu". The published opening has nw = "Nu" (say Nu, i "from Nu") | l/i use "Nu", say Nu, note "Nu (also called Nun)" |
| 32 | say | minor | n-is said "en-is"; the other 9 occurrences say "enis" | enis |
| 42 | say | minor | wꜥb·kwi said "uabkwi"; u26 and the published parts have "wabkwi" | wabkwi |
| 20 | i; n; morph gloss | minor | i "the keeper of the leaf of this door" rendered the compound iry ꜥꜣ "doorkeeper" literally, unlike u32. The note said ꜥꜣ "door-leaf" has "the same signs as ꜥꜣ 'great'", but only the column is shared. The lemma ꜥꜣ's known gloss is "great; here, hither", with no door sense | i "says the doorkeeper of this door". The note now says only the column is shared and points out that this is the compound iry-ꜥꜣ, printed here as two groups. Added a gloss override "door, door-leaf …" |
| 28 | morph gloss | minor | st had no gloss override, so the glossary would show the known st "place, seat, throne". The other occurrences carry an override | Added "it, them (3rd person dependent pronoun, written s-t)" |
| 7, 24, 31 | morph gloss (·n of rḫ·ṯi·n) | minor | Lemma ·n is glossed as the suffix pronoun, but the u31 note rightly says it is the dependent pronoun after the stative | Gloss override: "us (1st person plural dependent pronoun, object of the stative; same spelling as the suffix ·n)" |
| 43 | l | minor | "(I) · protected · (myself)" gave iw a gloss it does not have, and put "I" out of the word order | "protected · I · (myself) · from · the-hostile-acts …" |
| 43 | n | minor | "The iw before it has no suffix of its own" made the ordinary iw sḏm·n·f look odd | Now: the iw of a statement, with the sḏm·n·f carrying its own subject |
| 26 | n | minor | "(he prints dots under it)": the packet shows Budge's English as empty, not dots. Also, gr as a stative would want ·kwi, which the note did not say | "Budge gives no English for ḥr m ir·f". Added that the bare grt is the reason to keep the particle reading in mind (translation kept with Budge: the A2 classifier supports 'silent') |
| 6 | n | minor | sd "break" with hand d was not explained against the usual sḏ | Added: the verb is usually written sḏ; here the hand d stands for ḏ (reading kept as the signs give it) |
| 15 | n | minor | rn·k (masculine) after a run of feminine ·t was not explained | Added: sꜣtw is a masculine noun |
| 40 | l | minor (consistency) | ꜥꜣ "here" is "here(?)" in the published introduction's ii·n·i ꜥꜣ, which the note cites | l "here(?)" |
| 3 | l | minor | l lacked the "(is)" used in every other "A (is) the name" unit | "giver · of-breath · (is) · name · its" |
| 50 | n | minor | The note gives 'decreed' without saying that Budge's own English is the source | Added: Budge's English has 'Hath decreed it' |
| 8 | n | style | "as in ḏd in" was opaque | "as in the formula ḏd in N 'said by N'" |
| 8–28 | i | style | Quotation style changed mid-half: u0–6 and half 1 use single quotes, u29+ and the published introduction use single quotes with names quoted alone, but u8–28 used double quotes with nested singles | Converted to the house style. Speech frames use single quotes ('…,' says X, '…'). Name answers have the name quoted alone ('Ox of Geb' is your name., as in introduction u40). Plain lines (u24, 26–28) lose their outer quotes, like u31, u34 etc. |
| 18 | n | style | "the flying duckling pꜣ" (G40 is called a "flying duck" in u4) | "flying duck" |

## Considered and refused

- **u2 tr (X1 D21 M6 A2), M6 as det:** half 1 (units 37–38) codes this spelling the same way. Kept.
- **G17+D36 ligature (mi, m, nm, m-m, mk-tw), D36 role phon tr ꜥ while the reading has no ꜥ:** this follows the published introduction (mk: G17 phon m, D36 phon ꜥ). Kept.
- **u11 ḥnk·n·f, G43 tr w though "not read":** the note says so. tr is per glyph and the reading is separate. Kept.
- **u14 second N35 of the doubled n as comp:** the misprint-rule note opens correctly ("The text writes nn for 'of'; read n."). Kept. I could not check Budge's "(sic)" against the packet (it carries no flag), so it is left as the drafter saw it.
- **Joining u20 iry + ꜥꜣ into iry-ꜥꜣ as in u32:** this would mean composing a new q from two established layouts. Not necessary for the sense. Left split, and the note now names the compound.
- **nm (u35, u45; lemma nm) vs nym (half 1 u37):** a cross-half inconsistency of reading and lemma key. I cannot edit half 1. **Flag for the merge:** choose one (nm, with "later nim" in the gloss, fits the signs n-m+ꜥ).
- **ir·k glossed "yourself" in l (u7, u24, u28, u31, u47):** matches published introduction u42 ("pass · yourself"). Kept.
- **u39 "reed-leaf" for M18:** the same wording as introduction u2. Kept.
- **u5 "The numeral of line 27 comes before st":** house phrasing (introduction u25). Kept.
- **U15 sign in qrs, šd, sd, fꜣt, wn "for the arm with a stick" (u11):** matches the introduction's ruling (U15 printed where D40 is expected). Kept.
- **u2 "pw as 'this'" in wꜣs pw n ds:** pw as a demonstrative is defensible, and the note does not overclaim. Kept.
- **u6 n mr "the genitive after the infinitive":** acceptable, and the alternative 'throw' is given. Kept.
- **u21 rn·k after qbt (with t):** the gender of qbt is unknown and the word is doubtful. A remark would add nothing secure. Kept.
- **u23 rnnwtt with two t, one unwritten:** the standard form of the name. Kept.
- **u28 n·i before the dependent st:** the note only describes the order. Kept.
- **u35 W24 tr "w" in wnwt:** a pragmatic split of nw over the hare's n. Kept.
- **u36 "a man known by what he says":** light, but marked within a guessed reading. Kept.
- **u50 l "has-decreed" for a sḏm·f:** past sense is fine, and the unit is flagged doubtful. Kept.
- **u43 twi "later form of the pronoun 'I'":** correct. Kept.
- **u26 grt translated 'silent' (Budge) rather than the particle:** the A2 classifier supports silence. Kept, with the grammar caveat added.
- **Budge-isms / "Ani's scribe":** I grepped l, i and n for thee/thou/thy/saith/homage/triumphant/hath/verily/Ani/scribe. The only hits are the misprint note in u14 and the Budge quotation in u50. Nothing to change.
- **Restorations (u2, u4 sḏt, u9 ·t, u25):** flags and notes agree. Kept.

## Self-check
- The flattened glyph sign list of review-out-2 equals review-in-2 (1211 signs, same order).
- Every morph g-list covers its word's glyphs exactly once, and every q covers its glyphs exactly once (0 failures).

## Counts
- major: 3 (u27 relative form; u29 right-reading/lemma unification; u16 qrt lemma gloss)
- minor: 24 rows (incl. S29 tr ×10 glyphs and "bolt"→"folded cloth" ×6 note phrases, each counted once)
- style: 3

---
## review2-1
# Review 2: ani-125-address, pass 2, half 1 (units 0–49 of the merged draft, Budge lines 2–24)

Input: chunks/review2-in-1.json. Output: chunks/review2-out-1.json, made by script. The signs, the glyph order and the glyph count are unchanged.
Glossary corrections are in chunks/gloss-fix-1.json. gloss.json itself is not touched.
I read the pass-1 logs (review-1.md, review-2.md) and did not reopen the points they refused.

## Changes to the units

Format: unit (index in this file) · field · severity · what was wrong · what I did.

1. U37 w0 · reading, say, n; U40 · n · minor (consistency) · The same signs (N35 G17 D36) are read **nm** / say "nem" in half 2 (u35, u45). The harmonised lemma key and the glossary are also nm, but here the word was read "nym" / "nim". · Changed the reading to nm and say to "nem". The U37 note now opens "nm 'who?'", and the U40 note now says "as in m-ꜥ and nm".
2. U37 w1, U38 w1 · glyph roles · minor · In the particle tr written X1 D21 M6 (+A2), M6 was det "", with t and r as phon. But M6 is the tr sign itself. In U42, U44, U46 and U48 (and in half 2) it stands alone as log "tr" and writes the whole word, so it cannot be a classifier where t and r come before it. · M6 is now phon "tr", and X1 and D21 are now comp. The U37 note now reads "the knotted stalk tr (coded M6), with t and r written before it as its complements". The U38 note now marks the reed i as "(not read)". **Flag for half 2 u2:** it has the same spelling (X1 D21 M6 A2) with M6 as det. Its pass-1 reviewer kept that only to match these two units, so it should get the same change.
3. U18 w3 · morph lemma · minor (consistency) · The verb "protect" had the key **ḫw** here and **ḫwi** in half 2 (u43 ḫw·n·i). That makes two glossary entries ("ḫw — to protect, guard" and "ḫwi — to protect, guard, keep safe") for one verb. · Changed the key to ḫwi. The reading stays ḫw (the imperative). **The gloss.json entry "ḫw" is now used nowhere and should be dropped** when the glossary is assembled.
4. U16 w12 · glyph role · minor · In iwy, Z7 (w) after E9 (iw) was phon. It repeats the w of iw, and the same pattern is comp in iwsw (U27) and iw (U4, U7) in this half. · Role changed to comp.
5. U29 · n · minor · The note said the vulture stands for the ending -y "as in ḫftyw". No spelling of ḫftyw with the vulture is in evidence, so the comparison looks invented. · The note now says "the vulture apparently standing for the ending -y (as in iwty below)". iwty below has the same use, and the note itself describes it.
6. U36, U37, U38, U40 · morph gloss (in·sn) · minor · The override said in "say" is "only after the words quoted". U44 (in·k before what is said) contradicts this, and so does the note in U36 ("normally"). · Changed to "normally after the words quoted". The broadened glossary entry is corrected the same way (see G9).
7. U35 w6 · morph gloss (hrw) · style · The override "day (noun; the sun sign with its stroke)" described this spelling, not the word, and differed from U10's "day (noun)". · Changed to "day (noun)".
8. U21 · i · style · i used double quotes ("Welcome, welcome!"). House style, applied in half 2 and the published introduction, uses single quotes. · Changed to 'Welcome, welcome!'.

## Glossary (gloss.json): every entry for a lemma used in units 0–49 checked

These are the corrections written to chunks/gloss-fix-1.json:

- G1 · ind · minor · The entry said "from i 'O' and nḏ ḥr 'greet the face'", which puts ḥr inside ind. ind is i + nḏ, and ḥr·k is outside it. · Now: "ind — hail! greetings! (interjection; from i 'O' and nḏ 'greet'; ind ḥr·k 'hail to you', literally 'greetings to your face')".
- G2 · m-bꜣḥ · minor · The entry said bꜣḥ is "sometimes written with the phallus sign". The phallus sign is the normal writing of bꜣḥ, and every m-bꜣḥ in this text has it. · Now "written with the phallus sign bꜣḥ".
- G3 · nn (second word) · minor (grammar) · The entry gave the demonstrative as "before its noun: nn tꜣw 'these lands'". In classical Egyptian nn is joined to its noun by the genitive n (nn n X). The bare nn tꜣw of U45 is the later usage, and the entry was also tied to this one line. · Now: "demonstrative pronoun before its noun, in classical Egyptian joined to it by the genitive n, nn n X; in later texts also without it". The first word of the entry is unchanged.
- G4 · t · minor · "(noun; later also written tꜣ)" has no support in this text or in the house material, and is the kind of modern form the brief warns about. · Now "t — bread, loaf (noun)".
- G5 · šn, ḥꜣwt · style · The query was misplaced inside the grammar bracket: "(? verb" and "(? noun". · Now "curse(?) (verb; …)" and "entrails(?) (noun; …)".
- G6 · ḥꜣty · style · "(noun; the forepart of a lion sign)" does not read as a sentence. · Now "(noun; written with the forepart of a lion, ḥꜣt)".
- G7 · wꜣḏ · style/minor · The entry put "(adjective) green, fresh" inside a list that ended "(noun; …)", so it labelled the adjective as a noun. · Now: "papyrus stem; papyrus-shaped column, sceptre or amulet (noun); green, fresh (adjective; verb wꜣḏ 'be green') (Budge: 'tablet')".
- G8 · __broaden__ hrw · minor · The second word was given as "day (noun; plural hrw)". The plural is not hrw. · Now "· a second word of the same spelling: day (noun)". The known entry "hrw — terror, dread" is kept whole.
- G9 · __broaden__ in · minor · The entry said "only after the words quoted: in·k 'you said'", but in·k in U44 comes before the words. · Now "normally after the words quoted: in·sn 'they say', in·k 'you said'". The known entry is kept whole.
- G10 · ḫw · minor · This entry is a duplicate of ḫwi (see change 3). · Drop it. It is not written to gloss-fix-1.json, because the format has no "delete" value.

I checked these entries and found them correct; no change: ipw, ṯn, šꜥt, sꜥr, m-ḫt, sp, nb-r-ḏr, ḥr-ntt, iwty, ẖt, sꜥm, itn, wi, m-ꜥ, bꜣby, bsk, sr, pwy, ip, ḫbnt, ḏw, mtr, hri, ·s, sḥtp, mri, ḥqr, iby, ḥꜣy, mḫnt, iwy, prt-ḫrw, smi, wꜥb, ·tw, wy, sn, sw, sḏm, mdt, twy, miw, ḥpd-rꜣ, wḏꜥ, psš, išd, ẖnw, ẖrt, smtr, iwsw, ꜥḥꜥ, gꜣiw, qꜣ, iꜣt, ꜣtf, nfw, nꜣy, wpwty, wdi, ṯms, sḫpr, idryt, ṯꜣmt, ꜥbw, pḥwy, twr, šdyt, ꜥt, šw, rsy, mḥtt, snḥm, qdty, wnwt, grḥ, snꜥꜥ, swꜣ, nm, tr, tw, pw, ḥꜣyt, bꜣq, ḥr-ꜥ, niwt, bꜣt, pty, ḫnd, msdt, ihhy, fnḫw, bs, sḏt, ṯḥnt, qrs, wḏb, ḫꜣwy.
I also checked the broadened entries used in this half: ḥr, ꜥꜣ, ḫr, nḥm, ḥry-ib, ḥmt, sḫt, rd, tꜣ, st and m. Each keeps its known entry whole, as a script check confirmed for all 14 broadened entries. Every top-level key matches the lemma at the start of its entry, and no top-level key duplicates a known lemma.
I checked every per-occurrence override in this half. The changed ones are items 6 and 7; the rest are correct: grg, ḥr (Horus), hrw (U10), ꜥꜣ ×3, ḫr, nḥm (U29), ḥry-ib, ḥmt, sḫt, rd, nn (U45), tꜣ, st, in·k. Known lemmas used without an override (ḫt, ny, imy, mꜣꜥti, pr, r in ir·tn, ẖry, im, iwi and the others) fit their use here.

## Findings considered and refused

- **šꜥt "from šꜥd 'cut'":** a plausible derivation, not plainly wrong. Kept.
- **ṯꜣmt "cf. the verb ṯꜣm 'to cover, veil'":** I cannot confirm it from the material at hand, but it is not plainly wrong and the entry is hedged with "cf.". Kept.
- **wnwt and swꜣ entries name their usual signs:** these describe the normal spelling of the word, not one line. Kept.
- **qdty, ḥpd-rꜣ entries describe the beings by what this text says of them:** for names known only from this passage, that is the only identification there is, and Budge's spelling is given. Kept.
- **ẖrt (my half, T28 ẖr) and ḫrt (half 2, Aa1 ḫ):** two different words with different signs ("portion, concerns" and "condition"). This is not a duplicate. Kept.
- **U6 tꜣ-mri M6 as det:** the sign is an approximate coding of a "stalk with knot" classifier in a place name, not the tr particle. Kept.
- **U47 bs, where the w (G43) is not read and the note does not say so:** this is a small gap, and bsw is no better supported. Kept.
- **U22 ꜥꜣ "donkey" with D53:** pass 1 refused calling D53 a male-animal classifier, and I do not reopen it.
- **U15 sḥtp·n·i with G43 + Z1 read ·i, and U14/U15/U16/U17 l leaving the untranslated iw out:** both are explained in the notes. l follows the published practice, where iw is "not translated". Kept.
- **U1/U11/U31 ·kwi with Z1 as suff "i", against U10 wi with Z1 as det:** the published introduction (ꜥq·kwi, ḥtp·kwi) has the same split. Kept.
- **Budge-isms and "Ani's scribe":** I grepped l, i and n. The only hit is "scribe's kit" (U34, a sign description). The S29 = s and O34 = z tr and the "folded cloth" / "bolt" wording in the notes all agree with the signs throughout this half.
- **say:** I checked every word against the rule. No changes beyond item 1.

## Self-check
- The flattened glyph sign list of review2-out-1 equals that of review2-in-1 (1297 glyphs, same order).
- Every morph g-list covers its word's glyphs exactly once, and every q covers its glyphs exactly once (checked by script; 0 failures).
- Units changed: 16, 18, 21, 29, 35, 36, 37, 38, 40.

## Counts
- Unit changes: major 0 · minor 6 (items 1–6) · style 2 (items 7, 8)
- Glossary: major 0 · minor 7 (G1, G2, G3, G4, G8, G9, G10) · style 3 (G5, G6, G7)
- Total: major 0 · minor 13 · style 5

---
## review2-2
# Review 2, pass 2 — ani-125-address, units 50–100 of the merged draft (review2-in-2.json, indices 0–50; Budge ll. 24–47)

Unit indices are within review2-in-2.json. Output: review2-out-2.json (made by script). Glossary corrections: gloss-fix-2.json (gloss.json not touched).

## Changes to the units

| unit | field | severity | what was wrong | what I did |
|---|---|---|---|---|
| 0 | reading, say, glyph V24 tr, n | major | The same word as half 1's last unit (line 24) was still read **wdb**, with V24 tr "wd" and say "wedeb". Pass 1 corrected that unit to wḏb because the signs give ḏ, and the lemma key is now wḏb. This copy was missed | Set reading wḏb, say wedjeb, V24 tr wḏ. Added one sentence to the note (Budge's uteb has t, but the signs give ḏ) |
| 22, 24 | reading, say, glyph Z9 tr, morph lemma, n | major | The crossed sticks Z9 with the walking legs were read **sš** "pass", with Z9 tr "sš". Z9 has no value sš. Z9 + D54 is the usual writing of swꜣ "pass (by)", and half 1 reads it so three times (swꜣ·i, swꜣ, swꜣ·n·i) | Set reading swꜣ·k / swꜣ, say sewak / sewa, Z9 tr swꜣ, lemma swꜣ (already in the glossary, "swꜣ ḥr 'pass by'"). The u22 note now gives Budge's seś and the spelled-out sš·k of line 34 as a possible same verb. The threshold's sš·k (u14, O34 + N37) stays sš, as in the published introduction u42 |
| 45 | reading, say, morph (lemma + gloss), glyph W24 role, l, i, n | major | N35 + U19 nw + W24 nw was read **Nu** (lemma nw). This was wrong in three ways. (1) Half 1 (u45, line 23) reads the same spelling, with one more w, as the demonstrative nn "these" before its noun. (2) Budge reads it as a demonstrative too: ennu "that same". (3) The word order "nnw wy" cannot give the i's "the waters of Nu", because a direct genitive would put wy first. The god's classifiers are also missing | Set reading nn, say nen, lemma nn with the gloss override "these, those (demonstrative, before its noun)". l is now "in · these · waters(?)" and i is "…his floor being in these waters(?)?". The note gives the demonstrative reading, Budge's, and the Nu alternative with why it is set aside |
| 45 | n | minor | wnnw "being" had no verb form named | Added: the form is not certain (the w may be the prospective ending), and the clause is taken as circumstantial |
| 43 | morph lemma, n | minor (consistency) | The verb "protect" was keyed **ḫwi** here, but half 1 keys it **ḫw** (u18). That gives two glossary entries for one verb | Lemma set to ḫw. The note now says "ḫw 'protect, guard'". The gloss.json entry ḫwi is now unused and can be dropped |
| 26, 34, 44 | reading, morph, glyph I9 role/tr, n | minor (consistency) | The particle "then" was **irf** (one word, lemma irf) in u2 and u4, but **ir·f** = r + ·f in u26, u34 and u44. The glossary would show the preposition r "to" for these three | All three are now reading irf, lemma irf, I9 role phon, tr f (say iref unchanged). The notes call it the particle irf, "in origin r with ·f" |
| 26 | morph gloss | minor | The interrogative m in ḥr m "why?" had no override, so the glossary would show the preposition m. u39's r m has the override | Added the same override: "what? (interrogative pronoun; r m …)" |
| 43 | morph gloss (hrw) | minor | "day (noun; plural hrw)": the plural of hrw is hrww | "day (noun; plural hrww)" (also fixed in the broadened entry; see below) |
| 7 | n | minor | It called the owl-and-forearm writing of mi "the old m-ꜥ writing". It is the later writing, and u39 of this half says so | "the later m-ꜥ writing" |
| 29 | glyph D53 role | minor (consistency) | m-bꜣḥ had D53 as log. Pass 1 set it to phon in every m-bꜣḥ of half 1 | role phon |
| 29 | n | minor | The Y1 under bꜣḥ was called "unexpected and doubtful in the print", but it is in every m-bꜣḥ of this text (packet line 5: G17 D53 Z1 Y1) | Now: "is written in every m-bꜣḥ of this text (as on line 5)" |
| 29, 30 | glyph R14 / R15 role | minor (consistency) | imny and iꜣby had the West and East emblems as log, but as phon in u10 imnt and u12 iꜣbt. In all four the sign carries a complement | role phon in u29 and u30 |
| 14 | n | minor | sꜣt was glossed "floor, ground" with no word on the lemma sꜣtw, while u15 calls it the masculine sꜣtw. The w was not explained | The note now says this is sꜣtw, masculine, with its w unwritten unless the two strokes stand for it (Budge sati) |
| 40 | n | minor | smit was described as the infinitive "with its feminine t". The t is the ending of the infinitive of verbs whose last consonant is weak (3ae-inf.), not a feminine ending | Relabelled |
| 4 | n | minor | bs was not described. Its quail chick w is not in the reading, and Budge reads besu | Added a sentence: the signs, Budge's besu, and the possibility that the w belongs to the word |
| 1 | l | minor (consistency) | "a-sceptre · it-was": the house l for A pw is "it-is" (half 1 u43 "a-leg · it-is"). The i keeps "It was" | l "a-sceptre · it-is" |
| 7, 10, 12, 16, 19 | say | minor | nt was said "enet". The published introduction (u9) and half 1 (u8, u29) say "net", and so does u30/u43 of this half | "net" |
| 33 | say | minor | ḏꜥr said "djaer". By rule ꜥ → a, and no e is added next to a vowel (as in ꜥq aq, mꜣꜥ maa) | "djar" |
| 43 | say | minor | twi said "tui". w before a vowel stays w (as in ·kwi, wabkwi) | "twi" |
| 4, 5, 28, 35 | morph gloss (st) | style | Two different wordings of the st "it, them" override | Both now match the broadened entry: "it, them (3rd person dependent pronoun, object of a verb, written s-t)" |
| 20 | morph gloss (ꜥꜣ) | style | The override described the signs ("the column ꜥꜣ with the door-leaf as classifier"), which is not a glossary sense | "door, door-leaf (noun; iry-ꜥꜣ "doorkeeper")", as the broadened third sense |

## Glossary corrections (gloss-fix-2.json)

I checked every gloss.json entry (top level and `__broaden__`) for the 140 lemma keys used in this half, along with the known-lemmas entries they rest on. I am correcting these:

| lemma | severity | what was wrong | corrected entry |
|---|---|---|---|
| mꜣw | major | "a title of Thoth, "he of the Two Lands"" gives mꜣw a meaning it does not have. The Two Lands belong to the following tꜣwy, and the word itself is unknown. It also spoke of "the print" (pinned to the line) | "Mau(?), a title of Thoth, in the phrase mꜣw tꜣwy 'the Mau of the Two Lands' (title; reading and sense uncertain; Budge: māau 'recorder')" |
| mi | minor | "imperative of iwi" (mi is a suppletive imperative, not a form of iwi). Also "written m-ꜥ … later spelled with ꜥ" says the same thing twice and contradicts itself | "come! (the imperative that serves the verbs of coming, iwi and ii; in later copies written with the owl m and the forearm ꜥ, as if mꜥ, with the walking legs)" |
| gr | minor | It merged the particle grt into the verb's entry, as if one word ("the same signs also write…") | Verb gr, plus "a second word of nearly the same spelling: the particle grt 'now, moreover, indeed'" |
| wꜣḏ | minor | Grammar labels were misplaced: "(adjective) green, fresh (noun; …)" | Noun senses (noun) · also green, fresh (adjective; verb wꜣḏ 'be green') (Budge: 'tablet') |
| sd | minor | "to break (verb)" did not say that sd is only a writing of the verb sḏ | "(verb; a writing of sḏ 'break', with the hand d for the cobra ḏ)" |
| mr | minor | "Budge reads maa" is a remark about one line, not a sense | "canal, channel, pool (noun)" |
| sꜣḥ | minor | "reading uncertain where it occurs; Budge: saḥ" is pinned to the line. sꜣḥ "toe" is an ordinary word, and the doubt belongs in the note (u17 has it) | "toe (noun)" |
| bsw | minor | "the first element of the name of the right leg" is pinned to the line | "Besu(?), a word not understood, written with a fish classifier; perhaps from bs 'bring in, introduce' (name element; reading and sense uncertain; Budge: besu 'traveller')" |
| pw | minor | The interrogative pw was run in as "also" one sense of the demonstrative | Interrogative split off as "a second word of the same spelling" |
| irf | minor | "(enclitic particle, in questions…)", but u34 and u44 use it after a statement | "mostly in questions, 'what then?', also after a statement or a command" |
| m-bꜣḥ | minor | "sometimes written with the phallus sign": the phallus D53 is the regular sign of bꜣḥ | "written with the phallus sign bꜣḥ" |
| `__broaden__` in | minor | "only after the words quoted": half 1 u44 has in·k before the words, and pass 1 changed that note to "normally" | Known entry kept whole + "· a second word of the same spelling: to say, said (verb; normally after the words quoted: in·sn 'they say', in N 'says N'; in·k 'you said')" |
| `__broaden__` hrw | minor | "day (noun; plural hrw)" | "…(noun; plural hrww)" |
| `__broaden__` ·ti (new) | minor | The known entry says "written ·tw here" (true of the opening part). Every stative ending in this half (u7, u24, u31, u47) is written ·ṯi with the tethering rope, so the glossary would mislead | Known entry kept whole + "· also written ·ṯi, with the tethering rope ṯ and the reed (the older spelling)" |

**For the merge:** the gloss.json entry **ḫwi** is unused after the u43 lemma change (ḫw already covers the verb), so drop it. The entry for **ḫnd** keeps its second sense ("leg, shin"), because half 1 u43 uses the noun.

Entries I checked and found sound (no change): pty, tr, wꜣs, ds, šd, sw, nfw, pꜣ, bs, sḏt, ṯḥnt, m-ḫt, qrs, hꜣtw, ·s, ꜥḫm, tn, nn (now also used for the demonstrative in u45), bnš, n-is, tḫ, bw, ·t, ꜥryt, imny, iꜣby, ḥnk, fꜣt, irp, iwꜣ, gb, wn, mwt, pꜣyt, wḏꜣt, sbk, bꜣḫw, iry, qbt, šw, sꜣ, ḥpt, nḫn, rnnwtt, ḫnd, wꜥb, ḥr-ntt, mnw, wnpt, nbt-ḥwt, smi, tw, iry-ꜥꜣ, siꜣ, ḏꜥr, ẖt, nm, wnwt, ḏḥwty, ḫrt, ḫww, ḫw, šnt, twi, m-m, inb, iꜥrt, wy, sbi, wḏꜣ, t, ḥnqt, sḏm·tw·f, wḏ, wḏb, swꜣ. The broadened entries ḥr, ꜥꜣ, st, m, tꜣ, qrt and rd each keep their known entry whole.

## Considered and refused

- **u45 nnw → Nu was set in pass 1** ("Nun" changed to "Nu" for consistency). That pass fixed the name's form, not the reading. The reading is what I changed, for the reasons above; this does not reopen pass 1's ruling on the god's name.
- **u14 sš·k → swꜣ as well:** O34 + N37 spell s-š, and the published introduction u42 reads the same group as sš. Kept.
- **u11 vs u13, the G43 of ḥnk "not read" in one and read (ḥnkw) in the other:** the two forms differ (sḏm·n·f vs noun), and both notes say what they do. Kept.
- **u35/u36/u45 in written with N35 alone:** the reading is marked as taken, with doubt stated. Kept.
- **u36/u37 W19 tr "m" for a sign whose value is mi:** the sign is an approximation of an unclear type, and the note says the reading is a guess. Kept.
- **u21 rdi·n·f as a relative form without the feminine t to agree with qbt:** the t is often unwritten, and qbt's gender is unknown. Kept.
- **u49 pr·tw "impersonal" with ḫrw after it:** settled in pass 1, and the note is now coherent. Kept.
- **u27 relative form ḫnd·k:** settled in pass 1. Kept.
- **u41 ḫrt (with Aa1) vs gloss ẖrt (with F32):** these are two distinct lemmas, and both glosses are right for their words. Kept.
- **gloss t "later also written tꜣ":** this is a spelling remark, not plainly wrong. Kept.
- **gloss siꜣ, "(verb); Sia, the god of perception" without "a second word" phrasing:** cosmetic. Kept.
- **Budge-isms / "Ani's scribe":** grepped l, i and n for thee/thou/thy/saith/homage/triumphant/hath/verily/scribe/Ani. The only hits are "Nephthys" and the Budge quotation in u50. u9 says "the copyist" (of Budge's source), which is fine. Nothing to change.

## Self-check
- The flattened glyph sign list of review2-out-2 equals that of review2-in-2 (1211 signs, same order; 51 units).
- Every morph g-list covers its word's glyphs exactly once, and every q covers its glyphs exactly once (checked by script, 0 failures).

## Counts
- major: 3 unit changes (u0 wḏb; u22/u24 swꜣ; u45 nn "these") + 1 glossary (mꜣw) = **4**
- minor: 16 unit rows + 13 glossary rows = **29**
- style: **2**
