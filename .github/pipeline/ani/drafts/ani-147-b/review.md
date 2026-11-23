# Review — ani-147-b (Spell 147, gates 4–7, Plates 11–12)

## Pass 1

All edits were made by script (`review1.py` in the reviewer's scratchpad). The script loads the JSON and writes it back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, which matches the drafter's file byte for byte. Afterwards a script compared the result with the packet and confirmed these points:
- the 756 sign codes, joined in order, are unchanged from before the edits and equal the established sequence;
- every unit's `ln` is the packet line of its first glyph;
- every word's `rubric` flag matches the packet;
- every unjoined word's `q` equals the packet's layout, and the 7 joins (U1, U12, U14, U23, U28, U31, U37) are re-indexed correctly;
- every morph `g` list covers each glyph index of its word exactly once;
- every det has an empty `tr`;
- the 8 restored glyphs are exactly the ones Budge brackets (w29 viper, w59 n, the four signs of irt n, the seventh stroke, the second ·k), and each note says so.

No genitive `n` is keyed to the negative: every "of" is `ny`, and every dative or prepositional n (n·f, n·k, n·i, n ḏt, n wsir) is `n`. No Budge-ism ("triumphant", "saith", "hall", "homage", thee/thou/hath, "victory", "avenger", "herald") appears in any `l` or `i`.

Counts: 0 major, 6 minor, 4 style.

### Changes

- U35 · l, i, n · minor · `l` had "going · the-Osiris" and `i` had a finite verb, "the Osiris Ani goes with you". The note itself calls šmt an infinitive with Ani as its subject, and line 7 (U31) has the same construction, wꜣt šmt·i "the way of my going", as a direct genitive · `l` is now "has-been-made · the-way · of-going · of-the-Osiris · Ani · with-you · in · […]" and `i` "The way has been made for the going of the Osiris Ani with you in […]". The note now names the two direct genitives, gives the parallel with line 7, and gives Budge's finite reading.
- U6 · n · minor · "Budge's numeral 8 stands before it" (imw·f). The packet puts numeral 8 inside the word, between the owl G17 and w G43 · corrected.
- U12 · n · minor · "(Budge: Ānkh-f-em-fent)" quoted Budge's English spelling. House practice since 147-a pass 2 is to quote his transliteration (packet: ānχ - f · em · fent) · now "(Budge: ānχ-f-em-fent)". All other Budge forms quoted in the notes were checked against the packet and are correct.
- U20 w92 `imy·tn` · say · minor · "imytjen". The tj rule is for ṯ, and the suffix ·tn has t (house: ḥnꜥ·tn henaten, m·tn meten, ḏd·tn djedten) · "imyten".
- U35 w157 `ḥnꜥ·tn` · say · minor · "henatjen" disagreed with the published "henaten" (ani-001-b, ×5) · "henaten".
- U25 · n · minor · "This unit opens the sixth gate, at the head of Plate 12". Plate 12 begins inside the fifth gate's speech (U21: Budge's heading falls between imyt and nṯrw) · now "the first wholly on Plate 12 (the fifth gate's speech already runs over onto it)".
- U30 · i · style · sp sn was written out as a doubled sentence. The house renders it "(Twice.)" (weighing-of-the-heart: "My heart of my mother! (Twice.)") · now "I have come today! (Twice.)".
- U17 w81 `iwnw` · glyph W24 role · style · `comp`. W24 adds the final w and is not a pure repeat; the published parts mark it `phon` (ani-001-a, ani-001-b, ani-017-a, ani-125-address, ani-hymn-to-osiris; comp only in ani-017-f) · `phon`.
- U37 · n · style · "(Budge begins his second group with them, 'Ma-')" suggested that U15 + t are his "Ma" · now "(Budge's second group begins with them; his Maṭenu takes its m from the owl that follows)".
- U0 · n · style · the fourth gate's heading is the only one of the seven not in red (packet: w0–w1 carry no rubric flag; gates 1–3 and 5–7 do), and the note did not say so · one clause added.

### Considered and refused

- U8 w37 `in·n·i·f` (two suffixes on one verb, which is not a possible form): kept. The I9 stands after the seated man, so no n is free to make it n·f. The note says that the regular object would be sw and that the ·f may be a slip, and Budge also has "him". Splitting the viper off as its own word would not explain it any better.
- U19 "The papyrus writes p, g, ꜣ and s; read psg": kept. The classifier D26 (spitting) allows only this word, which is already house lemma psg. A metathesis plus a stray ꜣ is the kind of slip the formula is for.
- U23 `i` "in his vindication" where `l` has "in · vindication": kept. The possessive is English idiom for m mꜣꜥ-ḫrw said of the one protected, and it adds no claim the note does not make.
- U48 `ir·n·k` as a statement, against Budge's "Make thou": kept. The signs give the sḏm·n·f, and the note says that a request would need another form.
- U32 ḫmt "who devises(?)" against Budge's "without": kept. It is marked doubtful, the note gives Budge's view and the reason (the D35 arms), and ḫmt is the house lemma from the third gate.
- U37 X1 in the name with role `det` and empty tr (a sign not read): kept. It has the same status as the house's unread U15, and the note says that both are not read. No reading of U15 + t is supported.
- U38 the first Aa11 as `det` (perhaps the plinth written twice): kept, stated in the note.
- U2 watcher written without ·s (`sꜣwty`, `l` "the-watcher"): correct per the packet (no O34 printed).
- U16 `imyt` "which are in" as a feminine nisba after the dual ꜥrty, and U21 the same spelling as the preposition imytw "among": kept. Each fits its own syntax (after a noun, and between ink iꜣw and nṯrw), and each note says how the signs are taken.
- U43 `is·k` keyed to lemma `ist`: kept. The known entry is the particle, and the note calls is a short form.
- U5, U16 and U43 renderings that resemble Budge's English ("the son of", "jaw bones" → "the two jaws", "Only One" → "O sole one"): built from the grammar; not Budge-isms.
- `p` flags on both the "said by" unit and the first speech unit of each gate: these follow ani-147-a (its U4/U5, U25/U26, U35/U36).
- ꜥbw "purification" (U22) where ani-001-b and ani-017-b have ꜥbt "offering" for Budge's āb/ābet: kept. The note gives both readings and marks the choice as doubtful, and no t is written.

### For the glosser

New lemmas (not in known-lemmas.json): bgꜣsw, db-ḥr-khꜣ-ḫft, diwnw, dmḏ, fdnw, fnḏ, imytw, in-ḥr, itk-tꜣw-khꜣq-ḫrw, min, nsp, qs, sfḫnw, sisnw, srs-tp, sḫm-m-dnw-sn, šꜣbw, ḥkꜣw, ḫsf-ḥr-ꜥšꜣ-ḫrw, ḫsf-ḫmiw, ḫsf-ꜣd, ꜣds-ḥr, ꜥnḫ-f-m-fnṯw, ꜥrt, ꜥꜣ-mꜣꜥ-ḫrw. None was added or renamed in this pass. In the name glosses, quote Budge's transliteration (ānχ-f-em-fent, χesef-ḥrà-āśt-χeru, Ṭeb-ḥrà-keha-χeft …), not his English.

Known entries whose sense here is different, so the build would show the wrong gloss unless they are broadened (`__broaden__`):
- psd — known only as "to move (?) (verb …)"; here "back, backbone" (noun).
- sꜣq — known only as "robbery, theft"; here "to gather, collect (limbs)" (verb).
- imw — known only as "flame, burning (?)"; here imw·f "his company (?)", the beings around a god (noun pl.; Budge: àmmu, 'divine companions'; doubtful).
- iꜣw — known only as "praise, adoration"; here "old man, the aged one" (noun; with the bent man leaning on a stick).
- sꜥḥ — known as "noble, dignitary"; here also "the noble body, mummy" (sꜥḥ·f).
- ꜥšꜣ — known as an adjective; here used as a noun, "multitude, the many (parts)" (ꜥšꜣ·f).

## Pass 2

All edits were made by script (`review2.py` in the reviewer's scratchpad). It uses json.dumps(ensure_ascii=False, indent=1) and writes no trailing newline, which matches both files as found. Afterwards a script confirmed these points:
- the 756 sign codes, joined in order, are unchanged and equal the packet's sequence (and HEAD's);
- every morph lemma in units.json is in known-lemmas.json or gloss.json;
- no gloss entry is unused, and none duplicates a known lemma;
- every entry begins "lemma — ";
- every `__broaden__` value begins with its known-lemmas.json entry copied whole, then " · ".

Every Budge form quoted in gloss.json and in the notes (45 in the notes, 22 in the glossary) was compared with the packet's transliteration character by character. All are correct. The names in `l`/`i` agree with the glossary (all 12), and every `say` that also occurs in ani-147-a matches it.

Counts: 0 major, 5 minor, 7 style.

### Changes — gloss.json

- sfḫnw · meaning · minor · "feminine sfḫnwt, the t often not written". The second clause generalised from this one spelling, the seventh gate's heading, and does not belong in a lemma entry · now "feminine sfḫnwt", the same as ḫmtnw in ani-147-a.
- bgꜣsw · meaning · minor · "the guilty (?), failing ones". "Failing ones" was a sense invented from a guessed etymology · now "the guilty (?)", with the etymology kept as "perhaps".
- dmḏ · grammar · style · "the reading rests on Budge's ṭemt" pinned the entry to this part's sign doubt, which the U17/U24 notes already give, and it repeated "Budge: ṭemt" · now "to unite, join together (verb; Budge: ṭemt)".
- qs · grammar · style · gender missing · "noun m.".
- `__broaden__` ꜥšꜣ · style · the new sense gave "ꜥšꜣ·f 'its many (parts)'" and "many parts" as senses of the lemma · now "multitude, the many (noun; with a suffix, 'its many (parts)'; Budge: āśt)".
- `__broaden__` sšd · style · the new sense included "'bind up' a thing bound with a band", which is reasoning about this one occurrence · now "to bind up, bandage (?) (verb; a guess; Budge: seśeṭ, 'bandaged')".
- `__broaden__` psd · style · gender missing on the new noun sense · "noun m.".

### Changes — units.json

- U26 w118 `itk-tꜣw-khꜣq-ḫrw` · glyph 3 (X1) role · minor · the role was `phon` "t" before U30 `phon` "tꜣ", which would read ttꜣ. Everywhere else in the part, a sign that announces a multiliteral is `comp` (U6 reed before M1, U31 q and ꜣ before T14, U3 and U24 s before F36 and Aa18) · `comp`.
- U10 · n · minor · swꜣ·i disagrees with Budge's seś-à, and the note did not give his reading · "(Budge: seś-à, taking the sign as sš)", as ani-147-a does.
- U37 · n · minor · the note called ·sn "'their'" but then rendered "cutting them down". On an infinitive the suffix here is the object · "the suffix ·sn 'them', the object of the infinitive".
- U43 · n · style · Sektet was called "the bark in which the sun crosses the sky", which does not match the known gloss ("the evening bark of the sun") · aligned.
- U40 · n · style · "as at the earlier gates" did not mention that sš and mꜣꜥ-ḫrw are left out here · added.

### Considered and refused

- Name glosses that say which gate each demon belongs to ("the doorkeeper of the fourth gate of Spell 147"): kept. This is the house pattern for names (ani-147-a, pass 2), and it is not a line-pinned sense.
- bgꜣsw / U7: the derivation from bgꜣ is kept as "perhaps", because the unit note gives the same hedge. Nothing in the packet confirms or refutes it.
- Lemma keys `db-ḥr-khꜣ-ḫft` and `itk-tꜣw-khꜣq-ḫrw`, with "kh" for k + h: kept. They are Leiden letters (V31 k, O4 h), not the digraph, and they match the morph lemmas.
- `ḥkꜣw` keyed as written rather than as ḥkꜣ: kept. It matches units.json, and the gloss gives "magic, spells".
- ḫsf-ḫmiw and ꜥnḫ-f-m-fnṯw meanings not marked "(?)": kept. Both are built from transparent, known words, and the signs support them (the toppled-wall classifier, the worm).
- `__broaden__` ꜥšꜣ (is it needed?): kept. The known entry is only an adjective, and here the word is a noun with a suffix.
- No broadening for wꜥ ("O sole one"), nḏ (participle "protector"), sꜣwty ("watcher"), mꜣꜥ-ḫrw (U23 noun), ir (U35 passive), sp/sn, ḫr ("before"), wꜥb (stative): the known entries cover these uses.
- U19 `l` "cuts(?)" against `i` "wounds(?)": kept. Both fall inside the gloss "cut, wound (?)", and the English is better for the change.
- U2 "as at the second gate, but no ·s": checked against ani-147-a U23 (rn sꜣwty·s). The comparison is with the writing of sꜣwty, so it is kept.
- U34 "left untranslated at the second gate": correct (ani-147-a U30 is in the second gate).
- Roles and `tr` in every word were re-checked against the readings. No other faults were found, and the pass 1 items were not reopened.
