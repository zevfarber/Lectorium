# Review — ani-044-045-046-050-093 (Spells 44, 45, 46, 50, 93 and 93 A, Plates 16–17)

## Pass 1

All edits were made by script (`review1.py` in the reviewer's scratchpad `r1/`). Before it replaces anything, the script checks the old value: each text replacement must match exactly once, and each glyph's sign, role and tr is checked first. The file was written back with json.dumps(ensure_ascii=False, indent=1), the draft's own format, and still has no trailing newline. No glyph code was changed or moved. One word was split: nmmt in U24. A second script (`check.py`) confirmed after the edits:
- the 1180 sign codes, joined in order, equal the packet's sequence;
- every morph `g` covers its word's glyphs exactly once, and every `q` indexes its word's glyphs exactly once;
- every det has an empty `tr` and no other role has one; every O34 carries z (·z as a suffix);
- every `ln` is the packet line of the unit's first glyph;
- `rubric` on every word matches the packet's rubric flags;
- `restored` is set only on the bracketed glyphs. Where the packet flags a whole word but only part of it is in brackets, the draft flags only the bracketed signs, which is right: rḫ·i, mꜣꜣ·i, wsir (w86), swḏꜣ·tn | wi, nwd, ꜥm, wšb·sn, im·i (w342). The N35 of n in U24 is restored (packet w138);
- no `s`/`t` fields; no Budge-ism (saith, thee/thou/thy, ye, triumphant, homage, netherworld, verily) in any `l`, `i` or `about`.

Counts: 0 major, 7 minor, 5 style.

### Changes

- U4 wp-wꜣwt · say · **minor** · "Wepwawet" is not the settled say form. · → `Wep-wawet`. The English "Wepwawet" in `i` and `n` follows the house and was kept.
- U22 dwꜣt · say · **minor** · "duat" is not the settled say form. · → `Duat`.
- U6 ipt·i · reading, say, glyph 0 tr, morph, n · **minor** · The draft made up an unknown word ipt with R15 tr "ip", a value that R15 does not have, and translated it "brow" only on Budge's word. But Budge reads the horns wp as àp in this same part (Àp-uat for wp-wꜣwt, line 2). The established description of the first sign is "a tall staff with a forked (two-pronged) top", which is the horns on a staff. The rest of the group (t, stroke, flesh sign) is the spelling of the house's wpt "brow" in Spell 17 (F13 wp, X1, Z1). · reading → wpt·i, say → `wepeti`, R15 tr → `wp`, morph lemma ipt → **wpt** (a known lemma). The note now says the forked top is taken as the horns wp on a staff and that R15 is only the nearest code. It gives Budge's àp = wp and compares Spell 17. The doubt is kept in the note and in `l`/`i` ("brow(?)").
- U9 mkt · glyph 1 role/tr, n · **minor** · The draft emended "mꜥkt → mkt" and kept D36 as phon ꜥ "not read". The house's mkt in Spell 147 (147-a) is written with the same arm, tagged det. The arm is a regular part of the spelling, not a slip, so the "The papyrus writes …; read …" formula does not apply. · D36 → det, tr empty. The formula sentence is removed. The note now says the arm carries no sound here and is a classifier, as in mkt "protection" in Spell 147. It still takes mkt as the infinitive of mki with sw as object, and says the construction is unusual and the reading doubtful.
- U24 nmmt → nmmt | nṯr · words, say, l, i, n · **minor** · The draft took the flag and the seated god after the block as classifiers of nmmt. That pair is how this part writes nṯr "god" (ḥtp-nṯr in U50: R8 log nṯr, A40 det), and a flag is not a classifier of a block. · Split (the word had no q, so none was needed): nmmt = T29 log; nṯr = R8 log nṯr + A40 det, morph nṯr. l → "… the-block · of-the-god", i → "Spell for not going in to the slaughter-block of the god." The note now says Budge prints the flag and god in one group with the block and that they are split off as nṯr in a direct genitive. "nmmt in black" became "nmmt nṯr in black" (packet: w142 not rubric).
- U3, U4, U5 wi · glyph 1 role/tr · **minor** · The draft had the seated man (U3, U4) and the stroke (U5) as phon i. The house tags wi as G43 phon w + A1 det (017-c, 026-030b, 125-address), and the stroke as det (125-address). · → det, tr empty. The notes already call the stroke a stand-in for the seated man, so they need no change.
- U40 · l, i, n · **minor** · `l` left ꜥm untranslated "(ꜥm)" while `i` rendered it "the swallowing". `l` had "shall-fall-you" while `i` had "fall(?)". The "…" in `i` read as a gap in the Egyptian, but nothing is missing (Budge's dotted line is in his English only). · l → "not · shall-fall(?)-you · swallowing(?) · fish · with · doing · goring(?) · to-me", i → "You shall not fall(?) … swallowing(?) fish … with goring(?) done to me." The note adds that the words do not join into a clear sentence and that the dots mark breaks in sense, not missing words.
- U24 nmmt · say · style · "nememet" against the house `nemmet` (2×). · → `nemmet`.
- U30 tꜣwy · glyph 3 role/tr · style · The last Z4 was phon "wy" while the first Z4 was det. The house tags the dual strokes in tꜣwy as det throughout. · → det, tr empty.
- U34, U39, U47, U49 iꜣbt / iꜣbtt · glyph 0 role · style · R15 was tagged log with D58 as complement b. A sign with a phonetic complement is a phonogram, and the house (Hymn to Ra, Address) tags R15 phon iꜣb here. · → phon.
- U36 bby · glyphs 1, 3 tr · style · The reeds were tr i. The house bby (Spell 18) gives them y, as the reading bby does. · → y.
- U46 · n · style · The reading ḥtm puts t before m, but the glyphs give ḥ b m t, and the note did not account for the order. · Added "the t written after the m and read before it".

### The drafter's flagged choices

- **D35 alone = n, D35 + N35 = nn (except n msi nṯrw).** Kept. This matches 029-027-058-059 and 026-030b (D35 phon n + N35 phon n = nn) and the house n with N35 comp n. U10 and U39 say that n with the sḏm·f is taken as the future, and U31 explains n msi as the past passive. The choice is consistent and stated.
- **O34 tr "z", ·s "·z".** House. Every O34 checked.
- **·i before tw** (ḫm·tw·i, ꜥwꜣ·tw·i, iṯ·tw·i, ḏꜣ·tw·i). Kept as writing order. The morph indexes follow the glyphs, and each note says the suffix is read after tw.
- **m nm "again".** Kept. The house nm in Spell 18 is T34 G17 Y1a, exactly as in U0. The F25 alternative (m wḥm) is stated.
- **Joins.** iḫmw-sk (the stray chick is tagged phon w and the note says it is not read, as with the house's unread arm in nm), tp-rꜣ·i, pfy + R3 (unread sign as det, the doubt stated, the feminine nt explained), ḥtp-nṯr (house spellings in 018-b and 026-030b): all kept, with q correct. ipt·i is now wpt·i (above).
- **Splits** n·k, n·i, wi from verbs, rnn·n | wi, imn·n | wi, ṯs·w | n·i, tbw | n·i, swḏꜣ·tn | wi: kept. The q strings were re-derived and are correct. The order rnn·n wi wp-wꜣwt (dependent pronoun before a noun subject) is right and is explained.
- **Emendations.**
  - mꜥkt → mkt is withdrawn (above).
  - ṯsnw·i → ṯsw·i, nwy → pwy and ḥbmt·f → ḥtm·f are kept. Each opens with the formula, and each glyph keeps its own value.
  - nwy → pwy: the next spell writes the same phrase with the stool, so the sense allows one reading.
  - ḥbmt·f: the D58 is described as an approximate code. The t order is now noted.

### Findings refused

- **X6 for psḏt (U27).** One could object that X6 is the loaf pꜣt and that psḏt is written with the moon N9. Not changed: the house writes psḏt with X6 log psḏ in four parts (017-a, Weighing ×3, 018-introduction, 023-024).
- **O50 det in sp·s (U31).** One could ask for O34/Q3 comp and O50 phon sp. Not changed: the house tags sp (s, p, O50) as O34 phon, Q3 phon, O50 det in five parts.
- **wrd → wrḏ** (U16–U18). Not changed: the house lemma is wrd (001-b, 146-a, known-lemmas), spelt with the hand d.
- **V13 tr "iṯ" in iṯ·tw·i (U39), where no walking legs follow.** Not changed. The established description puts the tether "on a small two-legged stand", the V15 ligature, and the house tags V13 phon iṯ with X1 comp ṯ (017-e, 029-027).
- **D36 tr "di" in rdit (U26, U34).** House (029-027, 061-054, Weighing).
- **wi in U29 written with the stroke alone, tagged phon i.** Left as drafted. With no chick written, the stroke is the only sign carrying the word, and tagging it det would leave a word with no sound-bearing sign. The note says the stroke stands for the pronoun.
- **V6 tr "š" in sšd·f, V6 "wꜣ" in ꜥwꜣ·tw·i (U47), P8 "ḫn" in ḫnnw, U7 "ḥn" in ḥnnw, U19 "nw", R3/S38/F44 etc.** Not changed. These are approximate codes for signs the established file could not match, and each tr is the value the note argues the printed sign carries. The notes say so.
- **M22 tr "n" each in nnyw / nnw.** House (M22 phon n ×2 with N35 comp n in six parts).
- **The m in U39 and U40 ("with … with …") as the negative imperative m "do not" (Budge: "not … nor").** Not adopted. The owl alone, without the arm, is the preposition in this papyrus, and the draft translates what stands. The negative reading is no better supported.
- **ḥsq·i "I reap" (U44)** looks like Budge's "I reap". Kept: ḥsq "cut off" said of the fields is the plain sense, and the note says the reaping sense is taken from the context.
- **U8 "My utterance I know."** Kept: the fronted object is in the Egyptian, and the note says the sense is a guess.
- **U26 rdit "it was given(?)".** Kept: the note says it is the infinitive used as a heading, and the doubt is shown in `l` and `i`.
- **say clusters** (`tepehti`, `ikhemu-sek`, `khemtui`, `itjtui` etc.) follow the house practice for suffixes and clusters (ruled in 061-054).

### For the glosser

Lemma renamed: **ipt → wpt** (known: "brow, forehead"). ipt is no longer used. Lemma added to a word: **nṯr** (known) on the new word in U24.

These known entries are too narrow for this part and need `__broaden__`:
- mwt (known only as "mother"; here the verb "die", infinitive mt);
- sk (known "wipe, sweep"; here "perish", in skt and iḫmw-sk);
- smꜣt (known "place of union"; here "hair of the head");
- ḥꜣ (known only as the preposition "behind"; here the noun "nape, back of the head");
- wn (here "hasten", with the walking legs, U23);
- sšd (here "fillet, headband");
- ḥnwt (known "deceit · mistress"; here "horn", dual ḥnwty);
- kꜣ (here the particle "then, so", U46);
- mkt / mki: the draft uses a new lemma mki "protect" for the infinitive mkt. The known noun mkt "protection" stands beside it.


## Pass 2

Edits by script (`r2/edit.py` in the reviewer's scratchpad): each text replacement asserted to match exactly once, each glyph's old sign/role/tr asserted before the change, each gloss entry asserted to start as expected; written back with json.dumps(ensure_ascii=False, indent=1), no trailing newline. Pass 1's `check.py` re-run afterwards: the 1180 sign codes still equal the packet's sequence; morph g, q, det/tr, O34, ln and rubric checks clean (the "restored?" lines are the part-bracketed words pass 1 explains). Lemma check by script: every morph lemma is in known-lemmas.json or gloss.json; no gloss entry for an unused lemma; every `__broaden__` value starts with the known entry copied whole + " · "; no s/t fields.

Counts: 0 major, 13 minor, 5 style.

### Changes — units.json

- U22 · l, i, n · **minor** · "the sun-folk" for ḥnmmt is remembered modern-translation wording, not in any published part. · → "the-Henmemet" / "the Henmemet" (the name, with the note's existing explanation "a class of beings who live in the sun's light").
- U46 bnnwt · glyph 2 (N35) role · **minor** · Second water n tagged comp n, but the reading bnnwt has nn: both water n's carry sound (as rnn in U4). · comp → phon.

### Changes — gloss.json

- ṯst · **minor** · "noun m." for a noun in -t; Budge's English misquoted ("vertebrae" for his "vertebræ"). · → noun f.; 'the vertebræ'.
- ḥnmmt · **minor** · "the sun-folk" (modern-translation wording); "noun f. plural" for a collective. · → "the Henmemet, a class of beings who live in the sun's light (noun f., collective; written with the disc with falling rays; Budge: hamemet)".
- ḫm · **minor** · "used impersonally" misnames the passive ḫm·tw. · → "passive ḫm·tw 'be unknown, be ignored'"; Budge: χem added.
- ·st · **minor** · Pinned to the line ("here after bn"). · → general: "it, they (suffix pronoun of the 3rd person; a writing of ·s with t found in later texts; doubtful)".
- mki · **minor** · Line-specific doubt and Budge's 'verily' (his rendering of this one passage) put into the lemma. · → "to protect, guard (verb; infinitive mkt; Budge: māket)".
- nwd · **minor** · Pinned ("participle, 'which moves'"). · → "to turn, bend, move (?) (verb; reading and sense doubtful; Budge: ennuṭ, 'advancing')".
- db · **minor** · Stray "'goring'" (Budge's English for tbw, not ṭeb) tacked on. · removed; "pierce" added to the sense to match Budge's 'pierce'.
- ḥsq · **minor** · "also used of reaping" stated as fact; it is the context's sense here. · → "perhaps also of cutting grain, reaping (?)"; Budge: ḥesq.
- __broaden__ mwt · **minor** · New sense pinned ("mt·i 'I die'", "often with a small ring", which is this print's approximate N33). · → "to die (verb; often written mt, without the w; Budge: mit)". Old entry copied whole (checked).
- __broaden__ wn · **minor** · New sense pinned ("wn·n·i 'I have hastened'"). · → "(verb of motion, written with the walking legs; doubtful)".
- __broaden__ bꜣby (new) · **minor** · Budge prints Bàbà here; the known entry gives only Baabi / Bebi, so a reader of Budge could not find the name. · old entry + " · Budge also: Bàbà".
- nwḥ · style · Budge's English without his transliteration. · added "Budge: ennuḥti, 'goring'".
- ḥst · style · Budge's transliteration missing. · added "Budge: ḥeset".
- wnwn · style · "reduplicated from wn" is a guess at derivation; Budge missing. · → "(verb, reduplicated; written with the walking legs; the sense is doubtful; Budge: unun, 'travel')".
- bnnt · style · A word not otherwise met, given as certain. · "(?)" added to the sense.
- __broaden__ itm (new) · style · Budge prints Tmu here; the known entry has only Tem. · old entry + " · Budge also: Tmu".

### Findings refused

- **"the Imperishable Stars" (U5, gloss iḫmw-sk).** Kept. It is the Egyptological term of art for these circumpolar stars, not one translator's phrasing, and the note builds it from the grammar ('those who do not know perishing').
- **Two reeds tr i/i where the reading has y (nnyw U26, ḏꜣyt·i U49, ky U41).** Not changed: the house is split (ky i/i ×28, pwy y/y and i/i), and pass 1 changed bby only because each reed there stands alone for y.
- **bnnwt: w written after t.** Not noted: the feminine plural -wt is regularly written t before w.
- **U31 i "who saw at her first occasion"** (l has no "at"), **U19 "Let this be done"** ("this" not written), **U31 "in their forms"** ("their" not written). Small English supplements, not misreadings; left.
- **U50 note quotes Budge's "triumphant with victory".** Kept: it is a marked quotation of Budge as a check, not wording in `l`/`i`.
- **im lemma "im" (U37, U39) beside "m" for im·i (U44, U47, U48).** House practice exactly (im → im; im·f, im·s → m).
- The known entries for ꜣḫ, sr, ḥnn, ꜥm, iṯi, ḏꜣi, mnt, nm, ẖrt-nṯr cover this part's senses; no broaden needed. The glosser's other broaden entries (sk, smꜣt, ḥꜣ, sšd, ḥnwt, kꜣ) were checked and are exact copies with fair new senses; left.
