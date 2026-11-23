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

## Pass 2

All edits were made by script (`review2_146a.py` in the reviewer's scratchpad). It uses json.dumps(ensure_ascii=False, indent=1) and keeps each file's ending as found (no trailing newline). Afterwards scripts confirmed these points:
- the 632 sign codes are unchanged and equal the packet's sequence, and all the pass 1 structural checks still hold (`check146a.py`);
- every morph lemma in units.json is in known-lemmas.json or gloss.json (17 new, none missing);
- no gloss entry is unused, and none duplicates a known lemma;
- every entry begins "lemma — ";
- every `__broaden__` value (8) begins with its known-lemmas.json entry copied whole, then " · ";
- every Budge form in the glossary was checked against the packet's transliteration (Neruit, Mes-Ptaḥ, Sebaq, Neḳau, Ḥentet-Ārqiu, Semati, reśàt, smert, senk, setau, sart, ḥefu, χebχebet, θennu, sert, ḥent, χet, ḥau, qeṭ, tememet).

Counts: 0 major, 9 minor, 9 style.

### Changes — gloss.json

- ms-ptḥ, ngꜣw, nrwyt, sbꜣq, smꜣty, ḥntyt-ꜥrqyw · grammar · style · "(name of a doorkeeper; …)" did not match the house wording for these demons in ani-147-a/b · now "(name of a gatekeeper demon; …)", in the published order: name, meaning (?), office, part, then the grammar.
- ngꜣw · grammar · minor · "from the word for the long-horned bull, which takes the bull as classifier" copied the unit's reasoning about this spelling · now "spelled as ngꜣw 'long-horned bull', with the bull as classifier; doubtful".
- sbꜣq · grammar · style · "the arrow sign is not understood" described this one writing · now "the reading rests on a sign not identified", the wording of srs-ḥr in ani-147-a.
- nrwyt · grammar · style · "doubtful" was missing, though the note gives the meaning with a query · added.
- rš · whole · minor · The entry mixed this passage's form "ršit", a stray "rš," and Budge's other reading of this passage ("Budge instead reads … 'the nostrils'") · now "to rejoice, be glad (verb; written with the nose as classifier); joy (noun f.; Budge: reśàt)".
- smr · whole · minor · "(?)", "doubtful" and "Budge reads … 'beloved'" belonged to the reading of U14, not to the lemma, which is certain · now "companion, 'Friend', a courtier's title (noun m.; feminine smrt; a word built on mri 'love'; Budge: smert)". The doubt stays in the U14 note.
- snk · grammar · minor · "not otherwise known in these parts" was a remark about the part · removed; "the sense is doubtful" kept.
- ḫbḫbt · grammar · minor · the same "not otherwise known in these parts" · removed.
- stꜣw · grammar · style · "noun pl." was not stated in the note (the plural strokes may be only classifiers) · "noun".
- sꜣr · whole · minor · "sꜣrt, the one in need (?) (feminine participle used as a noun …)" pinned the lemma to U20, and "Budge: 'the needy'" quoted his English, not his transliteration · now "want, need; to be in need (?) (noun and verb; doubtful; Budge: sart)".
- ḥfꜣw · grammar · style · "written with the snake sign alone" described this one writing · now "(noun m.; Budge: ḥefu)".
- ṯni · whole · minor · "written with t for ṯ in places" described U9's spelling; "exaltation" and "ṯnwt … participles" were senses and forms not given in the notes; "'how great'" quoted Budge's English · now "to be distinguished, raised above (verb); ṯnw, greatness (?) (noun; Budge: θennu)".
- `__broaden__` sr · minor · "participle feminine srt 'who foretells' (?); doubtful" pinned the new sense to U3 · now "a second word of the same spelling: to foretell, make known (verb; Budge: sert)".
- `__broaden__` ḥnwt · style · the new sense lacked the house phrase "a second word of the same spelling" and Budge's form · added (Budge: ḥent).
- `__broaden__` ḫt · minor · "noun f." was not stated in the notes, and "'Flame'" quoted his English · now "a fifth word: fire, flame (noun; written with the flame as classifier; Budge: χet)".
- `__broaden__` ḥꜣw · minor · "Budge instead renders 'breath'" argued this passage · now "a second word of the same spelling: excess, abundance (?) (noun; Budge: ḥau)".
- `__broaden__` qd · style · "the like" and "'the like'" repeated Budge's English · now "form, likeness (noun m.; Budge: qeṭ)", with "a second word of the same spelling".
- `__broaden__` tmmw · style · "feminine collective form tmmt, 'mankind' (noun f. …)" restated the sense · now "also written tmmt, as a feminine collective (Budge: tememet)".

### Changes — units.json

None. In a fresh pass over every unit, including those not touched in pass 1, I re-read every role and `tr` against its reading, every `l` against the Egyptian word order, every `i` against its `l`, and every grammatical label. No fault was found.

### Considered and refused

- hmhmt "the shout of battle": kept. The U30 note supports it ("the battle cry of a fierce goddess").
- sbty "noun m.; plural sbtyw": kept. The gender is the lemma's own, and the plural is the form in the text (U2).
- sdbḥ, both senses ("entreat (?)", "provide for, equip"), and the causative of dbḥ: kept. The U25 note gives both senses and the derivation.
- smꜣty "from smꜣ 'unite', or … 'slay'", and ḥntyt-ꜥrqyw "ꜥrq 'bind, swear' (?)": kept. Each is in its note, with the query.
- The ꜣw and wsḫ broadenings: kept as the glosser wrote them. Each begins with the known entry whole, and the senses are those of U31.
- Name glosses that name the pylon and the spell: kept. This is the published house pattern ("the doorkeeper of the first gate of Spell 147").
- U24 l/i "abundance(?) of joy(?)" (pass 1): re-examined and kept. The note gives both readings and says that both are doubtful.
- U26 "while his head is (on him)(?)" and U25 sdbḥ·tw·s: re-examined. Both are marked doubtful and give the alternatives, and no better parse is supported.
- U12, the second mꜣꜥ-ḫrw with ordinary roles (phon/log): kept. The glyphs record what the papyrus has, and the note marks the second writing as not read.
