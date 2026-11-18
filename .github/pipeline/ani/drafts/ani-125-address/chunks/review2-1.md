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
