# Review — ani-029-027-058-059 (Spells 29, 27, 58 and 59, Plates 15–16)

## Pass 1

All edits were made by script (`review1.py` in the reviewer's scratchpad `r1/`). The script asserts each old value before it replaces it: every text replacement must match exactly once, and each glyph's sign, role and tr and each moved word's reading are checked first. The file was written back with json.dumps(ensure_ascii=False, indent=1), the draft's own format, keeping its trailing-newline state. The diff touches only the changed lines. No glyph code was changed or moved, and no join or split was added. One block of five words was moved from one unit to the next (U13 → U14). A second script (`check.py`) confirmed after the edits:
- the 975 sign codes, joined in order, equal the packet's sequence;
- every morph `g` covers its word's glyphs exactly once;
- every det has an empty `tr` and no other role has one; every O34 carries z (·z as a suffix);
- every `ln` is the packet line of the unit's first glyph;
- `rubric` on every word matches the packet's rubric flags (w0–4, w8, w11–12, w49–53, w57, w60–61, w161–168, w245–253, w256–263, w265–266);
- no Budge-ism ("saith", thee/thou/thy, "triumphant", "homage", "ye", "netherworld", Amenta, Unnu, Mesqen, Àusàr) appears in any `l` or `i`.

Checked by hand:
- **restored**: the packet flags w134 àb-f as restored, but its own description says that only the viper is in brackets. The draft flags only the I9 of ib·f. That is right and was kept. The restored [ni] (w175) is flagged on both its glyphs. The notes of U17 and U24 say "restored".
- **red ink**: every unit with rubric words says "in red". The notes also say correctly where the red stops: ḏd in is black in Spell 58 (U23), and ẖrt-nṯr is black after each title.
- **p**: set on the four titles, the four "said by" units, the rubric of Spell 58, and each change of speaker in Spell 58 (U23, U24, U26–U28).
- **q** of every join and split was re-derived from the packet. All are right: r·i, n·tn, nm, im·tn, ngg-wr; di·tw|n·k, mꜣꜥ-ḫrw|n·f, sḏm|n·f, wn|n·i, qrs·k|tw, rdy·tn|n·i, di·t|n·i.
- **cross-references** checked against the published files: ḥꜣ·k in Spell 17 (017-f); wpwtyw with Z9 in the Address; sḫm·i with D36 as classifier, wn with O31 U15, ib·i n·i and ḥꜣty·i, all in Spell 26 (026-030b, units 1, 6 and 12 belong to Spell 26); rqy·k and the heart as witness in Spell 30B; ind-ḥr·k in Spell 147; nm tr tw, nm and mḫnt with the owl-arm ligature in the Address; msqt in Spell 17; sꜣq with Aa18 in Spell 147; ssn with water n and sꜣw·n·i in Spell 54; šns in the rubric of Spell 125. All are correct except "the opening hymn" (below).

Counts: 0 major, 6 minor, 5 style.

### Changes

- U13 / U14 · words, l, i, n · **minor** · The draft ended U13 with ib n wsir ꜣny mꜣꜥ-ḫrw, as an apposition hanging after the sentence ("His heart is pleasing(?) to the gods, the heart of the Osiris Ani, true of voice."). It then left n·f in U14 with no subject ("It is his"). The draft's own parallel, ib·i n·i "my heart is mine" in Spell 26, has its noun subject before n + suffix, and so does this line: ib n wsir ꜣny mꜣꜥ-ḫrw n·f, "the heart of the Osiris Ani, true of voice, is his". · The five words were moved to the head of U14 (ln stays 4). U13 now reads l "pleasing(?) · heart-his · to · the-gods", i "His heart is pleasing(?) to the gods.", and the note drops its last two sentences. U14 now reads l "the-heart · of · the-Osiris · Ani · true-of-voice · to-him · has-power-he · over-it", i "The heart of the Osiris Ani, true of voice, is his; he has power over it." The note opens with ib n wsir ꜣny and mꜣꜥ-ḫrw and calls n·f "the predicate of a sentence without a verb, with ib n wsir ꜣny as its subject".
- U20 · l, n · **minor** · The note said "m ẖrt-nṯr as in the title", and `l` had "in · the-necropolis". No m is written: the unit's last word is ẖrt-nṯr (w146), and Budge supplies "[in]". · l → "(in)-the-necropolis". The note now says "ẖrt-nṯr as in the title, but here without m 'in', which is not written (Budge supplies '[in]')".
- U7 · n · **minor** · The note claimed that read as a sḏm·n·f "the t would be unexplained". That is true only of Budge's "you have done". The relative form irt·n·tn "what you have done", feminine as a neuter, explains the t, and it is exactly the analysis the draft itself gives irt·n·f in U15. · The alternative was added: "read as one word, the relative form irt·n·tn 'what you have done' … it is explained, as in irt·n·f in line 4, and that reading is as possible". The reading irt n·tn, which the drafter flagged as doubtful, is kept.
- U4 ḫndw (w35) · glyph 3 role, n · **minor** · The chick was tagged `comp` (a complement of the mountain ḏw). The note, however, makes it the w of a participle, which is a sound of its own and not a repeat. With the mountain standing for d, it cannot be a complement of it anyway. · Role → `phon` (tr w unchanged). The note now says "the w being the plural ending of a participle, not a complement of the mountain".
- U34 smt · l, i, n · **minor** · `l` and `i` rendered smt as "going(?)", but the note says the word is not known and its second sign is not identified. Nothing in the signs or the note supports "going". Budge's "making straight for" is his guess. · l → "(smt) · straight · …", i → "'(Smt?) Straight' is the name of the rudder." This is the house treatment of an unknown word, as with nqfywt in U6 and stwt in U35. The note says the word "is left untranslated", and its last sentence now reads "ꜥqꜣ seems to say so; what smt adds is not known."
- U35 stwt · n · **minor** · The note says that stwt "is not known", but stwt is a known lemma ("rays, beams of light, esp. of the sun"). Built as it stands, the glossary would show the reader "rays" under a word the note calls unknown. · Added: "The stwt 'rays' of the published parts is spelt the same, but light does not take this classifier, and the word here is not known". Lemma kept (see "For the glosser").
- U8 ḥḥ · n · style · "as in the opening hymn": the opening hymn (the Hymn to Ra, Plate 1) has no ḥḥ for nḥḥ. The V28 N5 V28 writing read nḥḥ is in the Hymn to Osiris and in Spell 1 (001-a). · Changed to "as in the hymn to Osiris and in Spell 1".
- U38 · n · style · This correction is given in Spell 58 (U22) and was only nudged here ("ssn is again written sst … read ssn as there"). Spell 59 has its own title, and a reader may begin there. The conventions say that the note on a correction opens with the formula. · The note now opens "The papyrus writes sst; read ssn, as in Spell 58." The later sentence now gives the reason briefly: "Here the t stands above the nose; the nose and the air allow only ssn 'breathe'."
- U44 · n · style · Same: the correction was not stated as the formula. · The note now opens "The papyrus writes sst·s and sst·i; read ssn·s and ssn·i, as in the title." The following sentence was reworded so that it does not repeat the correction.
- U21 · l · style · `i` marks "the place(?)" as doubtful, as the note does, but `l` did not. · "the-place(?)".
- U36 psy · l, i · style · The note says psy is "not known otherwise; the reading is doubtful", but `l` / `i` gave "a loaf" without a query, unlike "a portion(?)" beside it. · "a-loaf(?)" / "a loaf(?)".

### The drafter's flagged choices

- **Joins r·i, n·tn, nm, im·tn, ngg-wr.** All kept. Each q is right, and each note says the join was made.
  - r·i: Budge's (sic) stands on the r, and the note gives ḥtpt·i as the alternative.
  - nm: [ni] + mꜣ. The Z4 is a det with empty tr, and the arm is phon ꜥ but not read, as in the house nm of the Address.
  - ngg-wr: here G38 is the classifier and G36 writes wr. That differs from Spell 54, where G38 was read wr, but here a second bird is printed, and the note says so.
- **Splits di·tw|n·k, mꜣꜥ-ḫrw|n·f, sḏm|n·f, wn|n·i, qrs·k|tw, rdy·tn|n·i, di·t|n·i.** All kept.
  - The q strings were re-derived and are correct.
  - The labels are right: the passive sḏm·tw·f after nn; n·f as the predicate (now with its subject, above); sḏm n "listen to" with a noun subject; wn as the imperative; qrs·k tw with suffix subject and dependent-pronoun object; rdy·tn and di·t as wishes.
  - rdy·tn takes D36 tr `d` with two y, the house treatment from 061-054.
- **Corrections.**
  - ḥm·tw → nḥm·tw (U0), msqn → msqt (U29) and n → mw (U40): kept. Each opens with the formula, the glyph keeps its own tr, and the sense allows one reading (the Spell 61 title; msqt in Spell 17; mw in both titles).
  - Aa11 for Aa15 in sḏm·k (U20): kept. Aa11 keeps phon mꜣꜥ, following the house example of "ir; read in" with D21 tr r. The established reading (Decision B) makes the sign the closed plinth.
  - ssn written sst: kept, and the formula was added to U38 and U44 (above).
- **tmt for the bolt group (U4).** Kept as doubtful. The O34 and N35 keep their own tr, the note says they are not explained, and `l` / `i` carry "(?)". tm "be complete" is in the known entry.
- **ḫndw with the mountain.** Kept as doubtful. The N26 keeps its own value ḏw, and the note says it stands for d. The chick's role was corrected (above).
- **ḥr + infinitive (U4).** Kept. ḫr "fall" is intransitive, so the suffix on the infinitive is its subject. Leaving ḥr as "(ḥr)" in `l` is acceptable, because the note explains the construction.
- **iṯ as a passive sḏm·f after rdi (U5).** Kept. It matches nḥm·tw in Spell 29, and the note gives the active alternative.
- **nqfywt.** Kept untranslated. Budge's bracketed words are named as his supplement.
- **irt n·tn.** Kept, with the relative alternative added (above).
- **ẖryw "who hold(?)".** Kept. The nisba of ẖr is labelled correctly, and the "carrying" sense is marked with (?) in both `l` and `i`.
- **hb·f as hꜣb.** Kept. The known entry hꜣb has "to send" as its second word, so the build's gloss will fit. "sends(?)" carries the doubt.
- **mꜣt.** Kept as doubtful, now in a shorter unit (above).
- **sḫm with the owl-arm ligature, arm as det.** Kept. This is the house treatment: in Spell 26, sḫm·i is S42 G17 D36(det) A1.
- **irt·n·f as a relative (U15).** Kept. The label is right, and the note gives both the heart and the owner as possible subjects, as well as the participle with n·f.
- **st vs smyt (U21).** Kept. The known entry st already has the sense "with the hill-country sign, the desert hills, the necropolis (?)".
- **tnw "where?" (U25).** Kept as doubtful. The two unexplained signs are said to be unexplained.
- **gm-ḥrw.** Kept: two lemmas (gmi, ḥr) in a name phrase, and Budge's supplied words are named.
- **psy with O1.** Kept. O1 keeps tr pr, and the doubt is now shown in `l` / `i` (above).
- **dni.** Kept. The known entry has "share, portion (?)" as its second word.
- **nšy as nšny.** Kept. The known nšny "storm, raging" fits, and the hair-rage reading is marked doubtful.
- **smt, stwt, swn unknown.** smt is now untranslated (above). The note on stwt now faces the known stwt (above). swn is kept, said to be not known.
- **mhr "jug".** Kept. The note says the reed is not explained.
- **mrty.** Kept. The dual and the classifiers are described, and "what the name means is not certain".

### Findings refused

- **X1 in iṯ, tr `ṯ`** (U5, U6, U9). One could ask for `t`, under the ruling that a sign keeps its own value. Not changed, because the house is split: the Hymn to Osiris has iṯ with X1 phon t, but iṯ·n·f has X1 comp ṯ. t for ṯ is regular New Kingdom spelling, not a slip, and the note says "t, written for ṯ".
- **F32 tr `ḫ` in mḫnt·i** (U31) and **U28 tr `ḏ` in ḏdt** (U10, U12). Not changed. The house gives F32 ḫ where the belly writes ḫ (m-ḫt, ḫt, bꜣḫw) and U28 ḏ in ḏdt/ḏdw (×11).
- **D36 phon ꜥ where the arm is not read** (nm, mḫnt·i, mhr, mḏꜣbt). Not changed: it is the house tagging of nm and mḫnt in the Address. The notes say the arm is not read.
- **tmt (U0, U5) against the house reading tm** (061-054, 026-030b). Not changed. Here a second t is written after the owl, which the published parts did not have, and the note says Spell 61 lacks it.
- **wḏ with the hand d as complement of ḏ** (U20). Not changed: the sign keeps its own value, as the ruling asks.
- **say clusters** (`khendu`, `nehemtu`) follow the majority house forms, as ruled in 061-054.
- **U2 "of the living" against Budge's "which liveth".** Kept. The note argues it from the people classifier in the next line.
- **U1 "Back, you messenger of every god!"** Built from ḥꜣ·k (preposition + suffix, the turning-back cry, as in 017-f). It is not Budge's "Turn thou back".
- **U28's account of Merty as serpent goddesses.** It reads from the eyes, the cobra and the dual, and the note says what the name means is not certain. Kept.
- **U41 "Wenu (Hermopolis)".** Hermopolis is not in the conventions' list of settled names, but `i` keeps the Egyptian name and only glosses it, and the note gives Budge's Unnu and the house Khemenu. Kept.

### For the glosser

Lemmas used in morph that are not in known-lemmas.json: nqfywt, mꜣt, tnw, mrty, rwi, srt, mḏꜣbt, smt, ꜥqꜣ, mitt, swn, mhr, irtt, psy, nht, wnw. Known entries that do not cover this part's use (broaden):
- **stwt**: only "rays". Here it is an unknown word with the mummy classifier. Suggest: "· a second word of the same spelling, with the mummy-shaped classifier, not known (Budge gives no English)".
- **wsr**: only "power, strong". Here wsrw "oars". Suggest: "· a second word of the same spelling: oar (noun; plural wsrw, with the wood classifier; Budge: useru)".
- **in**: the particle in iw opening a question ("is it that …?") is not covered.
- **ḫnd**: the participle "striding (?)" is covered by the verb.
- **ẖry**: the sense "who hold (?)" is a guess, marked in the note, and needs no broadening.

## Pass 2

gloss.json and units.json were edited by one script (`review2.py` in the reviewer's scratchpad `r1/`). It asserts each old value before replacing it and keeps both files' indent=1 and trailing-newline state. Checks after the edits:
- every morph lemma in units.json is in known-lemmas.json or gloss.json;
- no gloss.json entry or `__broaden__` key is for a lemma no longer used (smt is still a word in U34, untranslated, so its entry stays, corrected);
- every broadening starts with the known entry copied whole, then " · " (asserted by script for all five);
- no entry contains "here", "this line" or a line number;
- `check.py`, re-run, passes: the 975 signs equal the packet, morph covers each glyph once, det tr is empty, O34 carries z / ·z, the ln and rubric flags match, and there are no Budge-isms in `l` / `i`.

Budge's spellings were checked against the packet transliterations.

Counts: 0 major, 7 minor, 5 style.

### Changes (gloss.json)

- nqfywt · **minor** · The entry was tied to the line ("a word in the address to the takers of hearts") and offered "noun or participle" as a grammar it cannot know. · "nqfywt — a word not known; perhaps of seizing or striking, from its classifier of force (?) (Budge: neqefiut, 'stealers')".
- tnw · **minor** · "where?, what? (?)" took Budge's 'what?' into the meaning. tnw is 'where?'; the doubt about this occurrence belongs in the unit note, which already gives it. · "tnw — where? (interrogative adverb; Budge: ten, 'what?')".
- mrty · **minor** · "a pair of goddesses shown with eyes and a rearing cobra" turned the classifiers into a description of images. The identification was also stated without doubt. · "Merty, a pair of goddesses (?) (god's name, dual; written with two eyes and the rearing cobra; the meaning of the name is not certain; Budge: Merti)".
- rwi · **minor** · "sḏm·f as a command, 'may you depart'" pinned the entry to U29. "rua" is not Budge's spelling; the packet has ruà. · "rwi — to go away, depart (from: r) (verb; Budge: ruà, 'separate')".
- smt · **minor** · The entry was out of step with pass 1. "perhaps 'going' (?)" kept the sense that was removed from U34 because nothing supports it. · "smt — not known (word of doubtful reading; Budge: semet, 'making straight for')".
- mhr · **minor** · The Budge spelling was wrong: "māḥeru" for the packet's māḥerà. · Corrected; the rest kept.
- ẖry (`__broaden__`) · **minor** · "here taken as 'who hold…'" pinned the broadening to the line. · The known entry is kept whole, followed by " · also, perhaps, who holds, has in keeping (?) (plural ẖryw; Budge: χeri, 'possessors of')".
- ꜥqꜣ · style · "the word for a true course or plumb-line" is a claim without support in the text or the known entries. "true" was added to the meaning. · "ꜥqꜣ — straight, exact (adjective; Budge: āqa, 'the middle')".
- mitt · style · The Budge spelling was "matet"; the packet has màtet. "adverb / noun f." was set in the house form. · "(adverb; noun f.; Budge: màtet)".
- wsr (`__broaden__`) · style · "a second word of the same spelling: wsrw 'oar'" gave the plural form as if it were the lemma. · "· a second word of the same spelling: oar (noun m.; plural wsrw, written with the wood classifier; Budge: useru)".

### Changes (units.json)

- U41 · n · style · "the published parts also call it Khemenu" suggested that the parts call *Wenu* Khemenu. Khemenu is another name, ḫmnw, for the same city. · "the published parts name the same city by its other name, Khemenu (ḫmnw)."
- U44 · n · style · The pass-1 rewording left an ellipsis that is hard to read: "and ssn·i 'I breathe' the seated man". · "… has the seated man."

### Checked and kept

- stwt (`__broaden__`): "a second word of the same spelling: meaning uncertain (?), written with a mummy-shaped classifier of images, perhaps from twt 'image'". This agrees with pass 1: U35's note says the known stwt 'rays' does *not* fit here. The coordinator's message read pass 1 the other way, but pass 1 did not say the word here is "rays". The prefix is exact. Kept.
- tm (`__broaden__`): "also tmt 'all, all of them' (?) (from tm 'to be complete'; Budge: temt)". This matches U4 and is marked doubtful. Kept.
- in (`__broaden__`): the interrogative in iw. The prefix is exact. Kept.
- mꜣt, srt, mḏꜣbt, swn and psy are each marked doubtful (?), with Budge's spelling as the packet prints it. irtt and nht are general and right; the Budge part is optional for words that are not names. Kept.
- wnw: "Wenu, Hermopolis, city of Thoth … (place name; …; Budge: Unnu)". This is general and uses the packet's spelling. Kept.
- The fresh read of units.json found nothing else wrong in roles, tr, labels or `l` ↔ `i`. U13 and U14 read consistently after the pass-1 move, and the ssn formula now stands in U22, U38 and U44.
