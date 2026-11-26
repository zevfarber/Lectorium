# Review — ani-061-054 (Spells 61 and 54, Plate 15)

## Pass 1

All edits were made by script (`review1_061.py` in the reviewer's scratchpad). The script asserts each old value before it replaces it: each text replacement must match exactly once, and each glyph's sign and old tr, each lemma, reading and say is checked first. The file was written back with json.dumps(ensure_ascii=False, indent=1), the draft's own indent, without a trailing newline as before. No glyph code was changed or moved, and no join or split was added. The draft's two joins were checked and kept: utā + aāb → wḏꜥ-ꜣꜥb (`0-1:2-3-4` + `0-1*2-3:4-5` → `0-1:2-3-4-5-6*7-8:9-10`), and r + tn → r·tn (`—` + `0:1:2` → `0-1:2:3`). Both q strings are offset correctly and both notes state the join. A second script (`check_061.py`) confirmed after the edits:
- the 283 sign codes, joined in order, equal the packet's sequence;
- every morph `g` covers its word's glyphs exactly once;
- every det has an empty `tr` and no other role has one; every O34 carries z (·z as a suffix);
- no Budge-ism ("saith", "thee/thou/thy", "triumphant", "homage", "Utcha", "Seb", "Set", "Àusàr") appears in any `l` or `i`.

Checked by hand against the packet:
- **rubric**: rꜣ n tm rdit nḥm·tw, m-ꜥ·f, both ḏd in, and rꜣ n rdit nfw m. The notes say "in red" for these in U0, U1, U3 and U4.
- **restored**: the A1 of nḫt·i, the A40 of wḏꜥ-ꜣꜥb and the whole of pḥty. All three notes say so.
- **ln / p**: every `ln` is the packet line of the unit's first glyph, and Spell 54 restarts at 1. `p` is set on the two titles and the two speeches.

Counts: 0 major, 7 minor, 6 style.

### Changes

- U0 mꜥ·f (w7) · reading, say, morph, n · **minor** · The draft read mꜥ·f, said `maef`, filed it under the lemma m, and called it "the preposition m written with the arm". The house reads this group as the compound preposition m-ꜥ (ani-017-d, -f, 125-address, 147-a; say `em-a`; lemma m-ꜥ, already known). The say also broke the rule: after ꜥ → a, no e is added. · Reading `m-ꜥ·f`, say `em-af`, morph m-ꜥ [0,1] + ·f. The note now says "the compound preposition m-ꜥ 'from (the hand of)', m 'in' with ꜥ 'hand', here written with Aa15 for the owl". The red-ink sentence was updated to match.
- U6 ꜥnḫ·s (w51) · glyph 3 tr · **minor** · The bolt used as the suffix ·s had tr `·s`. In the published parts the bolt suffix is `·z` in every part except ani-017-f and the weighing scene (about 90 cases, including the two latest parts, 022-072 and 023-024). It is `z` everywhere as a non-suffix. · tr → `·z`; reading and say unchanged.
- U9 ḏfꜣw (w71) · glyph 2 tr, n · **minor** · The pintail duck G39, written where the vulture is expected, had been given the meant value `ꜣ`. Meanwhile the vulture in ḫsbḏ, in the same unit and under the same correction, kept its own value. The latest house precedents (023-024 "ir; read in", D21 tr r; 026-030b ꜥmw·i, Z11 tr im) give the sign its own value and let `reading` carry the correction. · tr → `sꜣ` (G39's house value, ani `sꜣ` log ×3). The opening now states the formula plainly: "The papyrus writes ḏfsꜣ and ḫsbꜣ; read ḏfꜣw and ḫsbḏ." It then says what stands where, that the signs keep their own values, and that the classifiers (bread; the grains of a mineral) allow no other words. The ḏfꜣw sentence now says "the duck (for ꜣ)".
- U7 lone n (w60) · morph · **minor** · The lemma was n. The known entry n is the negative and the preposition 'to, for', and neither is what the note offers. The note's only explanation is the genitive. Built as it stands, the glossary would have shown "not". · Lemma → ny (known: the genitive adjective, written n). The note already says the word is untranslated and doubtful.
- U6 nḫt·i (w52) · n · **minor** · The note said the classifier U15 stands "where the arm with a stick is usual". That reads as though another sign stood in its place. In the house, the low hooked U15 of Budge's type *is* the printed arm with a stick, the classifier of force (001-a, 125-address, 026-030b). The note also left out the strongest support for its own correction: that classifier belongs to nḫt, and nḫḫ 'grow old' takes the bent old man. · Reworded: "printed for the arm with a stick, the classifier of force that nḫt takes (as sḫm in Spell 61)". The nḫḫ sentence now ends "…without the t, and is classified with the bent old man; the t and the classifier of force speak for nḫt".
- U2 sḫm (w23) · n · **minor** · The drafter's reading without ·f is right, but the note gave only half the evidence ("no viper is printed"). The last sign is not a stray: it is the regular classifier of sḫm, written the same way in Spell 30B's sḫm·i (S42 G17 U15 A1). · Added: "the sign printed for the arm with a stick, the classifier of force: sḫm·i 'I have power' in Spell 30B is written the same way."
- U9 nḏm (w68) · n · **minor** · "here used as a noun" did not name the form. nḏm is an adjective-verb, and what stands here is the adjective used as a noun. · "here the adjective used as a noun, 'the sweet one'". The `l` "sweet-one" and the `i` stand.
- U5 wpt (w46) · n · style · The two classifiers were listed without saying what they classify, and the note did not point to the published copy of the same group. · Added: Z9 is "the classifier of parting and crossing", and the group is "the same group as wpt 'the judging' in Spell 18" (ani-018-b: F13 Q3 Z9 A2). That copy also supports the note's own remark that the man with hand to mouth suits wpi 'judge'.
- U8 ꜣt (w63) · n · style · The note did not say what the sun classifies. It also did not square the head-as-sound reading with Spell 147, where the same hippopotamus head is the classifier after t and ꜣ. · Now "the sun (N5), the classifier of time". Added: "In Spell 147 the same head follows t and ꜣ as a classifier; here no ꜣ is written, and the head carries the sound."
- U8 bkꜣ·n·i (w62) · n · style · "With the sun the word is bkꜣ 'morning, become light'" stated the identification as fact, though the note ends "The reading is uncertain". · "With the sun as classifier the word would be bkꜣ 'morning, grow light'".
- U8 wr pḥty · n · style · "an adjective with the noun it refers to" misdescribes the construction. pḥty is not the noun that wr describes. It is the noun that says in what respect: "great of strength". · "an adjective followed by the noun that says in what respect".
- U7 · l · style · `[n]` for the untranslated water n. In `l` the published parts put untranslated words in round brackets, "(iw)", "(n)" ×5, and keep square brackets for gaps "[…]". This unit's neighbour U5 has "(iw)". · "(n)".
- U9 · n · style · The misprints sentence spelled the written forms as "ḏ-f with …", "ḫ-s-b with …" rather than as the X of "The papyrus writes X; read Y". · Merged into the minor change to ḏfꜣw above.

### The drafter's flagged choices

- **w23 sḫm without ·f, against Budge's seχem-f.** Kept, and the note was strengthened (above). The last sign is the printed classifier of force, the one sḫm·i carries in Spell 30B, and no viper is printed. Budge's ·f is not in his own type. "let my flood (be) mighty" (rdi + object + stative) is a sound way to construe the clause without a suffix. The note says that the subject 'it' and the clause structure are uncertain, and it gives rdy n·f 'to whom … was given' as the alternative.
- **w21 rdy·n·f.** Kept. D36 takes tr `d` here where the house rdi has `di`, because the two reeds write the y out. That is consistent within the word: the reading has a single y, and each reed has tr y, as in the house twy. Labelling it the sḏm·n·f is right for the signs (N35 phon n, morph sḏm·n·f). The note also offers the participle split.
- **w46 wpt from the horns F13, against Budge's àpt.** Kept. F13 writes wp, and Budge reads the same horns àpt in Spell 17 (the noun wpt 'brow', known lemma). Spell 18 has the same four signs as wpt 'judging' (lemma wpi), so the A2 classifier is house-attested for wpi. Taking the word as the relative form of wpi, feminine after st, fits the signs, and the note marks the sense "not certain" with the alternative 'parted from the earth'. Reading it as the noun wpt 'brow' ("this great place, the brow of Geb") was considered and not adopted: it leaves r tꜣ hanging and the A2 unexplained.
- **w20 ꜣgꜣb, lemma ꜣgb.** Kept. Budge also reads two vultures (aḳab). The note does not pretend to explain the second one, and the reading keeps what stands, as 026-030b did with ḫni under ḫnr. This is not a case for the misprints formula: the sense would not change.
- **w62 bkꜣ·n·i "dawned(?)".** Kept, softened (above). The doubt is marked in `l`, in `i` and in the note. The note sets the pregnancy sense against the sun classifier and calls Budge's 'destroyed (?)' his guess. Nothing is overclaimed.
- **w63 E25 as the hippopotamus head for ꜣt.** Kept, with the Spell 147 comparison added (above). The established code E25 is approximate. The packet describes a head and forepart, not a whole animal. With no ꜣ written, the head has to carry the sound, and the known lemma ꜣt 'moment' and the sun classifier agree.
- **w71/w73 ḏfꜣw and ḫsbḏ (U9).** Kept as corrections. Is ḫsbḏ really a single-reading slip, given Aa1 O34 D58 G1 N33 Z2? Yes. ḫ-s-b with the grains of a mineral and plural strokes gives no other word: no ḫsbꜣ is known, and ḥsb 'count' has ḥ and a different classifier. Budge himself understood it as lapis ('the blue'), and the parallel imy ḏfꜣw … imy ḫsbḏ wants a noun of substance. The rule allows the correction, the glyphs are untouched, and G1 keeps tr ꜣ. ḏfꜣw likewise: the bread classifier allows only 'provisions'. Its G39 tr was corrected (above).
- **w52 nḫḫt → nḫt.** Kept, argued better (above). The t and the classifier of force decide between nḫt and nḫḫ. The second Aa1 keeps phon ḫ, as the house keeps a doubled sign's value (023-024 wdn·n·f).
- **w68 nḏm as a noun.** Kept as a nominalised adjective (relabelled above). Budge's 'makest pleasant' would need snḏm, which is known and is not written, and the note says so.
- **w40 ngg-wr with G38 as wr.** Kept. Budge's type shows the wr bird of w64 and this one as near twins: the packet codes w64 G36 "could be goose G38". With D21 under it, the bird is read wr. The note says that the bird is printed as a goose and why it is still read wr. Taking G38 as the classifier of ngg, with wr written by r alone, would give a writing of wr that is not known.
- **w57 wḏꜥ-ꜣꜥb.** Kept. The join, the re-indexed q, the restored A40 and the "(?)" in `i` are right. The say `Wedja-aab` follows the house wḏꜥ `wedja`. The name is said to be not understood. Budge's "Utcha" is not used.

### Findings refused

- say `nehemtu` (nḥm·tw), `khesbedj` (ḫsbḏ) and `pehty` (pḥty): strictly, the rule wants an e between consonants (`nehemetu`, `khesebedj`, `pehety`). Not changed: the house has rḫ·tw `rekhtu` ×3 (against `rekhetu` ×1 and ḫsf·tw `khesefetu`), ḫsbd `khesbed` (hymn to Osiris) and pḥty `pehty` (125-introduction). The draft follows the majority house forms. A house-wide say pass, if wanted, is a question for the owner.
- "the Great Cackler" (ngg-wr) is also Budge's English. Not changed: it is the transparent meaning of the name, ngg 'cackle' + wr 'great', and the conventions ask for the meaning of a transparent name. There is no other honest English for it.
- U1 `i` "It is I" for ink pw: it might be taken as "I am he" (Budge). Not changed: the note explains ink pw as a sentence on its own, and "It is I" is built from the grammar.
- U5 r tꜣ "to the earth" (Budge "upon earth"): kept. wpi … r gives direction, and the note offers 'parted from'.
- U9 `i` "who are among the provisions" against `l` "who-is-in": not changed. The relative agrees with the vocative "you" in English, and "among" for imy before a plural noun of goods is a fair rendering.
- U9 pr·f "the sḏm·f … after the noun it describes": this could be called a virtual relative clause. Not changed: the description is accurate, and it is the register of the published notes.
- U0 nḥm·tw "the passive sḏm·tw·f after rdi": correct as a label for the tw-passive subjunctive after rdi. Not changed.
- U4 ink pw / footnote mentions, U2 and U9 Appendix sentences: these match the packet's skipped list (Chapters LX–LXII with another copy of LXI, LXIII A/B; LV and LVI). Not changed.

### For the glosser

Lemmas used in morph that are not in known-lemmas.json: ꜣgb, ngg-wr, nḫt, ssn, wḏꜥ-ꜣꜥb, bkꜣ. Known entries to watch:
- nḏm is glossed as the verb only. This part uses the adjective as a noun, 'the sweet one'. A broadening is suggested: "· also as an adjective used as a noun, 'the sweet one' (nḏm tꜣwy 'the sweet one of the Two Lands')".
- sš already has 'nest', and wpi already has 'judge' (so the A2 classifier is covered). m-ꜥ, ny, ꜣt, ḏfꜣw, ḫsbḏ and sꜣw all cover this part as they stand.

## Pass 2

gloss.json was edited by script (`review2_061.py` in the reviewer's scratchpad), and units.json by a second script (`review2u_061.py`). Each old value is asserted before it is replaced. The draft's indent=1 and its trailing-newline state are kept for both files. Checks after the edits:
- every morph lemma in units.json is a key of known-lemmas.json or of gloss.json;
- gloss.json has no unused keys, and its one `__broaden__` entry (nḏm) is for a lemma that is known and used;
- that entry starts with the known entry copied exactly, character for character, followed by " · " (asserted by script);
- `check_061.py`, re-run, passes: the 283 signs equal the packet, morph covers each glyph once, det tr is empty and no other tr is, O34 carries z / ·z, and there are no Budge-isms in `l` / `i`.

units.json was re-read as a whole, as a fresh adversarial pass after the pass-1 edits. The notes, readings, `l` and `i` agree with each other. The pass-1 relabels (m-ꜥ, ny, the classifier of force, nḏm as a nominalised adjective) read consistently in every unit that mentions them. One overclaim was found (below).

Counts: 0 major, 3 minor, 2 style.

### Changes (gloss.json)

- wḏꜥ-ꜣꜥb · **minor** · "a being addressed by name" is an invented sense. The text has ink wḏꜥ-ꜣꜥb, "I am W.": the speaker takes the name for himself, and no one is addressed. "Budge: Utā-aāb" was a hyphenated form Budge never prints: he prints two groups, utā and aāb, and his English is 'Utcha-aāb'. "not understood (?)" hedged twice. · "Wedja-aab, a name the speaker takes for himself, not understood (name; the first part perhaps wḏꜥ 'judge, separate', the second, ꜣꜥb, not known; Budge: Utcha-aāb)". The say form Wedja-aab is kept: it is the units' `say` and follows the house wḏꜥ `wedja`, with ꜣ ꜥ → a.
- ngg-wr · **minor** · The entry was tied to this line ("whose egg the speaker claims to be"). It gave Budge's spelling as "Neḳeḳ-ur" with a hyphen, but Budge prints "Neḳeḳ ur" with a space under one group (packet w40). House entries quote Budge as he prints him: his hyphens are kept where he has them (Qem-ur, ānχ-f-em-fent) and none are added. The entry also lacked the say form that house name entries begin with (Kem-ur, Ankh-ef-em-fenetju). · "Negeg-wer, 'the Great Cackler', a goose god of the beginning of things (god's name; from ngg 'cackle' and wr 'great'; Budge: Neḳeḳ ur)".
- bkꜣ · **minor** · "sense uncertain here" tied the entry to this line, and the second word was folded into the first's brackets. Budge's reading was given as English only. · "to grow light, dawn (?) (verb; with the sun as classifier; Budge: beka, 'destroy (?)') · a second word of the same spelling: to be pregnant (verb)", in the house format for words of the same spelling. The doubt stays as (?).
- nḫt · style · "not to be confused with nḫḫ 'grow old'" is advice about this line, and "Budge: neχeχt" is his reading of the scribe's doubled ḫ, not a spelling of the word. "verb 3-lit." is not the house form, which is "verb" in all but three entries. · "to be strong, mighty (verb; written with the arm with a stick, the classifier of force)". The misprint and Budge's reading are already in the note.

### Changes (units.json)

- U7 ꜣꜥb · n · style · "the cup and the mat suggest an offering vessel" claimed too much: both classifiers are approximate codes (W10, R4), and the word is unknown. · "its two classifiers, both approximate, may point to a vessel or an offering, but that is a guess."

### Checked and kept

- ꜣgb, "written with three lines of water": correct. The packet's sign is N35A, the three water lines, and this entry does not mention the canal N36 (in this part the canal is in itrw, not in ꜣgb). The units note for ꜣgꜣb also says "three lines of water (N35A)". "noun m." and "Budge: aḳab 'the water floods'" quote the packet exactly. Not changed.
- ssn: "to breathe, smell", with the nose as classifier and Budge's sesen 'smell', is correct and general. "verb 3-lit." is correct for s-s-n and is left; this is a style point only.
- nḏm (`__broaden__`): the old part is the known entry exactly. The new part, "also the adjective used as a noun, 'the sweet one'", is what U9 now says. Kept.
- No entry carries a Budge-ism in its meaning part; Budge's forms appear only in the "(Budge: …)" slot.
