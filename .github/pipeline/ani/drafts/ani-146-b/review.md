# Review — ani-146-b (Spell 146, pylons 7–10, Plates 11–12)

## Pass 1

All edits were made by script (`review1_146b.py` and `review1b_146b.py` in the reviewer's scratchpad). Each script loads units.json and writes it back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, which is how the drafter's file was written. A second script (`check146b.py`) compared the result with the packet and confirmed these points:
- the 425 sign codes, joined in order, are unchanged and equal the packet's sequence w0…w112. The draft has 114 words: one join and two splits, described below.
- every unit's `ln` is the packet line of its first glyph (pylon-relative, as printed). `"p": true` stands on each pylon's title, its "says" unit and its first speech unit, as in ani-146-a.
- every word's `rubric` flag matches the packet. The tenth ordinal (w93) is black, and the note says so.
- every unjoined, unsplit word's `q` equals the packet's layout. The join and the splits are re-indexed correctly:
  - U4 iry-ꜥꜣ = àri + āāa, `0-1:2-3-4-5:6-7-8:9-10`;
  - U10 n + snḏ from `0:1`, each now a single sign;
  - U24 snḏ `0-1` + n·s `0:1` from `0-1-2:3`.
- every morph `g` list covers each glyph of its word exactly once.
- every det has an empty `tr`, and every role is one of the six.
- no Budge-ism (triumphant, saith, homage, thee/thou, hath, "quieteth", "feeble", "far-reaching", "gainsaid") appears in any `l` or `i`.

Counts: 3 major, 7 minor, 2 style.

### Changes

- U16 w69 (the number) · reading, say, tr, morph, n · major · The reading was the figure "350", but no published part has a digit or a space in a reading; every numeral there is read as its word (sfḫ, ḥḥ, sn), with the first sign of a multi-sign figure carrying the word and the rest empty (ani-147-b sfḫnwt Z2 'sfḫ', Z2 '', Z1 ''; ani-weighing snnw). Each V1 had tr 'šnt' and each V20 tr 'mḏ'. The morph keyed the hundreds to `šnt`, which known-lemmas.json has only as "hostility, harmful acts", so the build would have glossed "350" as hostility. It keyed the fifty to `mḏ` 'ten', but fifty is its own word, dyw · reading `ḫmt-šnt-dyw`, say `khemet-shenet-diu` (by rule; the drafter's "diyu" added a y), tr V1 'ḫmt-šnt', '', '' and V20 'dyw', '', '', '', ''. The morph is now `šnt` [0,1,2] (needs broadening, below) and `dyw` [3–7] (new). The note now gives the number words and says the script almost never spells them out. `l` "350" and `i` "350 rods(?)" are kept, since the figure is the clearest English.
- U15 hrrt · l, i, n · major · The note called hrrt "the feminine participle of hri 'be content'" and the `l`/`i` made it "who contents the heart". hri takes no object (the glossary gives it intransitive, with the relative form hrrt), so a participle of it cannot mean "who contents"; that sense is Budge's "who quieteth" · hrrt is now taken as the relative form, feminine for the pylon, with ib as its subject. `l` "with-whom-is-content(?) · the-heart · of-Mesat(?) · lord-her", `i` "with whom the heart of Mesat(?), her lord, is content(?),". The note keeps the participle reading 'content of heart', the pattern of the other titles, as the alternative, and the unit stays doubtful.
- U10 iwty swꜣ ḥr·s · l, i, n · major · `l` "who-does-not · pass · by-her" and the note's "'one who does not pass by her'" make the title name someone who stays away from the pylon. That is not a title of the pylon, and it does not mean "no one passes". `i` "she whom no one passes" said something else again · `l` "who-not · passes-(one) · by-her · …", `i` "she past whom no one goes, for fear of her terror(?).". The note now says that iwty stands for the pylon, that ·s points back to it, and that no subject is written. It also notes that iwty is not in the feminine (unlike iwtt in U9) and keeps the drafter's reading as the alternative.
- U8 ḫꜣꜥt ḏrt · l, i, n · minor · "swift(?) of hand" is not a sense of ḫꜣꜥ 'throw, cast', the lemma the note itself gives · "hurling(?) · of-hand" / "hurling(?) of hand,". The note now reads "'hurling of hand' (?), a hand that throws".
- U24 ẖnw·s · tr, n · minor · E14 had tr 'ẖ', and the note guessed that the sign was "perhaps a form of the animal's belly, the sign ẖ". The house reads this same animal sign as ẖn in ẖnw (and in mḫnt), with water n as complement (ani-125-address, two cases) · tr 'ẖn'; the note now follows the house and cites it.
- U17 bs · n · minor · The note said bs is "also written with a fish in Spell 17 (bsw)". No Spell 17 part has it: bsw with a fish is in ani-125-address, where it is a name not understood · the note now points there and says that word is not understood either.
- U16 sꜣtt · glyph role/tr · minor · The bolt before the hobble sꜣ (V16) was `phon` 'z', so the reading would have two s's. It repeats the s of sꜣ, like the folded cloth before Aa18 in sꜣrt (ani-146-a U20) · role `comp`, tr 'z'. The note now says "as complement".
- U9 nḏnḏ · n · minor · The note said the small pot is "coded W24, approximate". The packet marks only Aa27 as approximate in w41 · "the small pot nw (W24)".
- U10 swꜣ · n · minor · The note gave "(Budge: seś)" with no reason for differing from him · it now adds that the crossed sticks are the sign swꜣ and that swꜣ ḥr is the idiom 'pass by'.
- U16 šmꜥ · n · minor · The note gave "(Budge: qemāu)" with no reason for reading šmꜥ · it now reads "(Budge: qemāu, his old value for this sign)".
- U17 ṯst · glyph tr · style · The complement bolt had tr 's'. The house writes the bolt as 'z' in tr in every role (O34 comp 'z' ×11 in the published parts, none 's') · 'z'.
- U0 · n · style · The note said the building sign stands "over the house". The packet's q (`0-1-2:3-4-5`) and its description put O16 and O1 side by side (they are stacked only at the eighth and tenth pylons) · "and the house beside it".

### The drafter's flagged choices

- The cardinal 350: changed (above). Grep of all 19 published ani-*.json files found no digit reading. Multi-sign numerals carry the word on their first sign, as in ani-147-b and ani-weighing-of-the-heart.
- D35 as `log` 'iwt' in iwtt (U9) and iwty (U10), and as `phon` 'n' in U24: kept. The house has D35 for iwt both ways: `phon` in ani-017-a and `log` with X1 `comp` in ani-125-address, which is the more recent part and has the same structure as this draft. D35 for the negative n is `phon` 'n' in 82 published cases, and U24's water n as `comp` matches ani-146-a U26.
- The join iry-ꜥꜣ in pylon 7 (U4): kept. Budge's English puts "[is]" under āāa, so he read it as a verb. The signs are the same as in ani-146-a U10's iry-ꜥꜣw·s: the rod-and-lozenge O29 with ꜥ and ꜣ, the hatched O29 and U15 not read, and a person classifier. The house joins these. Here no ·s is written (and no n before it), and the note says so.
- The split n + snḏ (U10): kept. Budge transliterates the group as two words, "en senṭ", and n 'because of' with the noun snḏ is plain grammar.
- The split snḏ + n·s (U24): kept. It encodes the reading 'the one within her does not fear because of her', and the note gives Budge's sḏm·n·f reading snḏ·n·s as possible and the sense as doubtful. Both parses are open, and the drafter chose one and said so.

### Considered and refused

- U3 "The papyrus writes i, b and k; read ikbyt": kept. With the lock of hair and the mourning woman as classifiers, only ikb 'mourn' fits, so the formula is right. The note also says that the transposition may be only a matter of grouping, which is honest.
- U3 mrr·s as a relative form ('whom she loves'): not added. With ikbyt as its antecedent, it gives no clear sense, and the note already marks the line as doubtful.
- U7 ꜥḫm ḏꜣft as "who quenches(?) the burning" against Budge's supplied negative: kept. No negative is written, the note says so, and the line is marked doubtful.
- U9 smꜣmt: I considered reading the owl as a complement of the sickle, which would give smꜣt 'she who slays'. I kept the drafter's reading: Budge reads the extra m (smammet), the note gives participle or noun with a query, and the word is marked doubtful. The plinth Aa11 as `det` "not read" follows the house practice for unread signs (Y1a, W24 in qd in ani-146-a).
- U14 nb where nbt is expected: kept untouched, as conventions require. More than one reading is possible, the signs are translated as they stand, and the note says why.
- U22 sdbḥt: Budge's setebḥ takes X1 as the t/d of the stem, while the draft reads it as the ending, with d and ḥ unwritten. I kept the draft: both are guesses, and the note says the reading is doubtful.
- U22 tnwt with Q2 as `phon` 'tn' for an unidentified sign: kept, since the note gives it as Budge's reading and doubtful. U16 dbn with U30 'd' is kept on the same grounds.
- Two reeds as `phon` 'y' + 'y' with a single y in the reading (iꜣggyt, ikbyt), where ꜣny has 'i' + 'i': kept. The house does both (nrwyt in ani-146-a has 'y' + 'y').
- Names: `say` "Sikty-ef", "Khu-djet-ef", "Ir-su-djes-ef" (hyphen + -ef) follow ani-spell125-opening (Maa-ef, Tutu-ef) and ani-125-introduction (Per-tep-dju-ef). "Sekhen-wer" follows the w-before-a-vowel rule (wered in ani-146-a). Every name note quotes Budge's transliteration as the packet has it.
- U19 ir-sw-ḏs-f "He who made himself by himself" and U25 sḫn-wr "Great Embracer", both without a query: kept. Each name is built from transparent words (iri, sw, ḏs·f; sḫn with the embracing-arms classifier, wr), and conventions ask for the meaning where it is transparent.
- U2 and U17 'the weary one' for bgꜣ: kept. The sense follows the classifier and the known link to bꜣgi, but the glossary entry needs broadening (below).
- The ordinals sfḫnwt, ḫmnnwt, psḏnwt (nwt not written) and mḥt-mḏ: kept. The forms and notes agree with ani-146-a and ani-147-a (ḫmtnwt without the pot). mḥ + number is the regular ordinal from ten upward.
- U1, U6, U13, U21 "says the Osiris (the scribe) Ani (true of voice)": kept. They match ani-146-a U17/U23/U29, and each note states the differences (scribe left out, mꜣꜥ-ḫrw present or absent, no classifier).
- `about`, `titleEn`, `part`: consistent with ani-146-a ("part 2"; "the seventh to the tenth pylon (Plates 11–12)"). The last unit's note says in one sentence what other papyri have after the tenth pylon, as conventions require.

### For the glosser

New lemmas (not in known-lemmas.json), computed by script after this pass (25): iꜣggyt, ikb, ḥꜣp, sikty-f, ḫmnnw, rkḥ, ḏꜣf, spd, pꜥt, ḫꜣꜥ, nḏnḏ, nihy, ḫw-ḏt-f, psḏnw, msꜣt, dyw, dbn, sꜣtt, šmꜥ, qq, ir-sw-ḏs-f, mḏ, nhs, tnwt, sḫn-wr. (`dyw` replaces the draft's use of `mḏ` for fifty. `mḏ` 'ten' is still used in mḥt-mḏ, U20.)

Known entries that do not cover their use here (`__broaden__`):
- šnt — known only as "hostility, harmful acts, strife"; here (U16) a second word of the same spelling: hundred (numeral; ḫmt šnt 'three hundred'; the coil V1).
- ḏrt — known only as "kite"; here (U8) a second word of the same spelling: hand (noun f.; the hand sign with t; Budge: ṭet).
- bs — known only as "flame"; U7 uses that sense, but U17 (with a fish as classifier) needs "perhaps also image, figure of a god (?) (noun; Budge: bes)".
- bgꜣ — known as "failing, harm, fault (?) … weariness"; here (U2, U17) 'the weary one', the dead Osiris (noun used of a person; Budge: beḳa).
- wꜣḏ — known as papyrus stem / green / greens; here (U16) green stone, malachite or felspar (noun; with the stone classifier).
- mḥ — known only as "fill"; here (U20) the ordinal formation mḥ + number, 'the one completing N', mḥt-mḏ 'tenth'.
- ḫt — "wood, tree, stick" covers the sign, but here (U16) the sense is a rod as a measure of length (?). A short addition.
- sdbḥ — known as a verb; here (U22) perhaps a noun 'entreaty' (?), written short. A short addition.

## Pass 2

All edits were made by script (`review2_146b.py` in the reviewer's scratchpad). It loads each file with json and writes it back with json.dumps(ensure_ascii=False, indent=1) and no trailing newline, as the files were. A second script (`check2_146b.py`) then confirmed these points:
- the 425 sign codes, joined in order, equal the packet's sequence w0…w112;
- every morph `g` list covers its word's glyphs exactly once;
- every morph lemma is in known-lemmas.json or is a top-level gloss.json key (25 new lemmas, none missing, none unused, none duplicating a known lemma);
- every `__broaden__` key (8) is in known-lemmas.json, and each value begins with that entry copied whole, then " · ".
Every `say` whose reading occurs in a published ani-*.json was compared with the published form. All agree except šfšft·s (below).

Counts: 1 major, 10 minor, 7 style.

### Changes — units.json

- U16 wꜣḏ · n · minor · "'green stone', malachite or green felspar": nothing in the signs or the text identifies the mineral (the stone classifier says only "stone"). The identification was added from outside · now "'green stone'; which stone is meant is not said."
- U3 ḥꜣpt · n · minor · "taken as the verb after mrr·s" did not name the form, and it left out that the t does not fit · now "taken as the infinitive after mrr·s, 'loves to cover', though the infinitive of a verb of three consonants has no t". The participle alternative that follows is kept.
- U2 bgꜣ · n · minor · "a word related to bꜣgi" stated the link as a fact, while the known gloss gives it with "perhaps" · now "perhaps a writing of bꜣgi 'be weary, slack'".
- U7 ꜥḫm · n · minor · The word was called "a participle" with no mention that a title of the (feminine) pylon would be expected to show t · added "written without the feminine t".
- U23 šfšft·s · say · minor · "shefsheftes" did not match the house form of this word: šfšft·k is "shefshefetek" in ani-017-f, so e is inserted between f and t · "shefshefetes".
- U18 qq · n · style · as for U7: added "written without the feminine t".

### Changes — gloss.json

- `__broaden__` mḥ · major · "forms the ordinals from eleven on: mḥt-mḏ 'tenth'" contradicts its own example and the unit (U20: "the way ordinals above nine are formed") · now "also forms the ordinals from ten upward, mḥ with the number, 'the one that completes N' (participle; mḥt-mḏ 'tenth', feminine; Budge: meḥt met)".
- `__broaden__` wꜣḏ · minor · "green stone, malachite (?)" added a specific that the text does not support, and "as in 'green stone of the South'" tied the entry to U16 · now "also green stone (noun; written with the stone as classifier; Budge: uat')".
- `__broaden__` bgꜣ · minor · "used of the dead Osiris" tied the lemma to this passage's interpretation (U2's note) · now "also the weary one (noun, used of a person; written with the seated man with hanging arms, the classifier of weariness)".
- `__broaden__` ḫt · minor · The measuring rod was entered as "a sixth word", but it is the same word as "wood, tree, stick" (the second word), and "written with the stick sign" is true of that word too · now "also a rod as a measure of length (?) (noun; Budge: χet)".
- `__broaden__` ḏrt · minor · "also hand" made 'hand' a sense of the word 'kite'. They are two words · now "a second word of the same spelling: hand (noun f.; Budge: ṭet)".
- nḏnḏ · grammar · minor · "reduplicated form of nḏ" claimed a base word that no unit gives or supports, and "infinitive nḏnḏ" tied the entry to U9's form · now "(verb; a reduplicated word; Budge: net'net')".
- `__broaden__` šnt · style · "numeral hundred (šnt; …)" did not follow the house wording for a homonym · now "a second word of the same spelling: hundred (numeral; …; ḫmt šnt 'three hundred')".
- ḫmnnw · grammar · style · "the number that gives Hermopolis, ḫmnw, its name" is background, not part of the lemma, and "numeral, ordinal" did not follow the known sfḫnw / ḫmtnw / fdnw pattern · now "eighth (ordinal numeral, from ḫmn 'eight'; feminine ḫmnnwt; Budge: χemennet)". The Hermopolis remark stays in the U5 note.
- psḏnw · grammar · style · now "(ordinal numeral, …)", as for ḫmnnw.
- ḫꜣꜥ · grammar · style · "written with the walking legs" described this one writing (cf. the pass 2 changes to ḥfꜣw in ani-146-a) · removed.
- spd · grammar · style · Budge's form was missing · added "Budge: sepṭet".
- dyw · grammar · style · "the old word" meant nothing · now "(numeral; the script almost never spells it out, writing the figure instead)".

### Considered and refused

- F4 in ḥꜣt (U14) as `phon` 'ḥꜣt' rather than `log`: kept. It is the same coding as ani-146-a U34 and ani-125-address.
- ẖnw·s (U24), E14 'ẖn' + N35 comp + W24 'nw' + G43 comp: kept. It is the same coding as ẖnw in ani-125-address (and as F32 ẖnw in ani-017-d).
- "nedjnedj" with no e between the two halves: kept. It follows the house's reduplicated "khebkhebet" (ani-146-a).
- "Sikty-ef" with no e in kt: kept. The house's "Hentyt-arqyu" is the same.
- U3 "The papyrus writes i, b and k; read ikbyt": kept, for the reason pass 1 gives. Only ikb fits the classifiers.
- U22 nhst 'who rouses' without a query: kept. The doubt of the line is stated at the end of the note, and tnwt and sdbḥt carry the queries.
- U16 ḫmt-šnt-dyw (pass 1): not undone. The morph gives no lemma for ḫmt; the šnt broadening names ḫmt šnt 'three hundred' instead, since one glyph cannot be split between two morphs.
- U15 hrrt, U10 iwty, U4 iry-ꜥꜣ join (pass 1): re-read and kept. The l/i match the parse given, and the doubt is stated.
- Gloss entries left as the glosser wrote them, each checked against its unit notes: iꜣggyt, ikb, ḥꜣp, rkḥ, ḏꜣf, pꜥt, nihy, msꜣt, dbn, sꜣtt, šmꜥ, qq, mḏ, nhs and tnwt; the name entries sikty-f, ḫw-ḏt-f, ir-sw-ḏs-f and sḫn-wr (in ani-146-a's pattern, with Budge's forms as in the packet: Sàkti-f, χu-t'et-f, Àri-su t'esef, Seχen-ur); and the broadenings bs and sdbḥ.
- Every broadening was re-tested for need: each covers a use in a unit that the old entry does not. None was dropped.
