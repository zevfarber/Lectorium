# Review — ani-074-008-002-009-132-010 (Spells 74, 8, 2, 9, 132 and 10, Plate 18)

## Pass 1

Method. Every unit was read word by word against the packet in a merged view (scratchpad `review1/view.py`). The view shows each word's glyphs with role and tr, its morph lemmas, and the packet words it covers, with Budge's transliteration, English, approx / UNSURE flags and the third reader's decisions. House spellings, roles, say forms and renderings were checked by script against all 29 published `ani-*.json` (`review1/house.py`), mainly 043-089-091-092, 044-045-046-050-093, 147-a/b, 017-a…f, 018, 125-address and the model. Morph lemmas were compared with known-lemmas.json. Every complement was checked by script for a multiliteral host sign. No modern translation was opened or recalled. Budge's English was used only as a check on sense.

All edits were made by script (`review1/edit.py`). Before replacing anything, the script asserts that each text replacement matches exactly once and checks each glyph's old sign, role and tr. The file was written back with json.dumps(ensure_ascii=False, indent=1), the draft's own format, with no trailing newline. The pre-edit copy is `review1/units.before.json`. No glyph code was changed, added or moved, and no word was joined or split. After the edits, `review1/check.py` and a comparison with the draft confirmed:
- the 1001 sign codes, joined in order, equal the packet's sequence;
- only 2 glyphs differ from the draft, both in role;
- every `q` indexes its word's glyphs once, and every morph `g` covers them once;
- every det has an empty tr and no other role has one, and every O34 carries z;
- `ln` and `rubric` match the packet, and every glyph marked `restored` lies in a word the packet marks restored (and the reverse);
- there are no `s`/`t` fields and no Budge-ism in `l`, `i` or `about`.

The drafter's emendations were judged against conventions.md ("The scribe's mistakes"):
- U1 i+r read in: accepted. ḏd in N allows only in.
- U18 eye at the head of rwty read rwty: accepted. Budge's own footnote gives the same correction.
- U20 wsir written twice, read once: accepted. Budge marks it (sic).
- U43 rꜣ·f read rꜣ·i: accepted. Budge marks it (sic), and the parallel ꜥrt·i allows only 'my'.
- U23 itf·f "his father" left unemended: accepted. More than one reading is possible, and the note says so (see Refused).

Counts: 0 major, 7 minor, 12 style.

### Changes

- U1 · l, i · **minor** · `l` had "for(?) · Sokar", which reads as "for Sokar", but `i` makes Sokar the one called on, with "(for me?)". `i` also had "Do what you do", an imperative, where `l` and the note have the sḏm·f wish "may-do-you". · l → "for(?)-(me) · Sokar"; i → "May you do your deeds (for me?), Sokar (Twice.),".
- U5 · l, i, n · **minor** · šmt·i was rendered as a sḏm·f, "walk-I", and the note did not explain the t. The note cites Spell 147, where the house reads the same writing (147-b U31) as the infinitive šmt with ·i, "my going". · l → "going-my · weary-am-I"; i → "As I go, I am weary". The note now names the infinitive and gives Budge's 'I walk along'.
- U6 · n · **minor** · Two readings departed from Budge's letters without a reason. ibḥw against his ābeḥ: the note did not say that his ꜥ is not printed. ṯꜣ against his t'a (= ḏꜣ): only his English was given. · Each now gives Budge's letters and why the signs give ibḥ and ṯꜣ.
- U9 wnw · glyph 2 (W24) · **minor** · comp nw. W24 is not purely a complement, because it adds the w that the hare wn lacks. The chick after it is the complement of that w. · → phon nw.
- U11 · n, i · **minor** · The note said "Budge's numeral 3 stands before this line". The numeral 3 stands before itf in U10, and nothing in the packet puts a numeral at ink here. `i` also dropped nn, which `l` renders "this(?)". · The sentence was removed. i → "[I am] that Osiris, this one(?), [who is in] the West."
- U21 imḥt · glyph 2 (Aa15), n · **minor** · comp m, but the owl m before it is a uniliteral sign, so there is no multiliteral sign for Aa15 to complement. The same ruling was made in 043 pass 1 (U10, in·tw). The note did not say that m is written twice against a reading with one m. · → phon m. The note now says the m is written twice, as in Budge's àmmeḥet, and read once.
- U28 · n · **minor** · The note called sꜣ mry itf·f "the title of the priest who buries and serves his father". Nothing in the text or the house supports that claim. It also wrote "it·f" against the reading itf·f. · → "sꜣ mry itf·f … is said of Horus, the son who buried and served his father Osiris."
- U4 · n · style · The note did not explain the w of ꜣḫw, given its singular rendering "the Spirit". · One sentence added: a plural is possible, but no strokes are written and Budge has a singular.
- U9 · n · style · The note called the sign after tp "the kneeling man" and then "the seated man". · Both now read "kneeling man".
- U10 · i · style · `i` had the singular "my ornament" against `l` "ornaments-my", the reading ḫkrw and the house rendering (043 U44). · → "my ornament(s)".
- U10 · n · style · irt was read against Budge's maat with no reason given. · A parenthesis now gives Budge's maat and says that the t and stroke after the plain eye give irt.
- U12 · l · style · `i` has "his day on which(?) he does not exist" with nothing for "on which" in `l`. · l → "day-his · (on-which) · not-does-he …".
- U15 · l · style · "and-living" puts an unwritten "and" in `l` as if it were written. The note says no "and" is written. · → "(and)-living".
- U23 · n · style · The note did not point to the evidence of line 4. · One sentence added: in itf·i the same doubled viper cannot be ·f.
- U25 · n · style · The second viper of itf·i is "not read", but the note did not open with the formula for a doubled sign. · The note now opens "The papyrus writes f twice in itf; read it once."
- U29 · n · style · The chick w in ꜣḫ·kwi was listed without saying that it is not read. · "(not read)" added.
- U31 · n · style · pr was read against Budge's pa-f without comment. · "(Budge: pa-f; the sign is pr)" added.
- U32 · i · style · "with long strides(?)": "long" has nothing behind it in the Egyptian, and `l` has "with · striding(?)". · → "who comes forth striding(?)".
- U40 · i · style · `i` had the singular "his stride(?)" against `l` "strides-his" and the plural reading nmtt·f. · → "at his strides(?)".

### Refused

- **U23 itf·f kept unemended.** Three writings of itf in this spell double the viper:
  - U23 itf·f has no suffix after it;
  - U25 itf·i has Budge's restored ·i after it;
  - U28 itf·f is in sꜣ mry itf·f, where ·f fits.

  So in U23 "his father" (·f) and "my father" (itf written with ff and the suffix left out) are both possible. Under the conventions, more than one reading means the text is translated as it stands and the note says so. The note already did that, and pass 1 added the line 4 evidence.
- **N35 as comp after two M22 in nn / nn·kwi** (U5, U11, U45). Kept. This is the house tagging in every published nn and nni (001-a, 017-a/b/c, 044).
- **U39 ꜥḏ · D46 comp d.** The hand d complements ḏ. Kept: this is the d-for-ḏ spelling the part shows in psd (U3, U17), and the tr shows what the sign carries.
- **U31 rr · V10 tr rr.** The house has V10 phon r in rr (147-a/b, 017-f, 018-b), but in every house case a mouth r follows. Here the loop stands alone, and the note says the second r of the Spell 147 writing is absent, so V10 carries the whole word. Kept.
- **p: true on each ḏd in unit and on U39.** Kept: house (043, 044). U39 is the first unit of the speech of Spell 10, which has no ḏd in.
- **U27 i "on earth"** against `l` "which-is-in · the-earth". Kept: imy tꜣ is rendered in idiomatic English and the sense is the same.
- **U37 mi with water n "not read", without the formula.** Kept. The note says the n may belong to the word, so the slip is not one-way.
- **U19 wꜥw "establish(?)".** The sense comes from Budge's English. Kept: the note says that both the reading and the sense are guesses, and `l`/`i` mark them (?).
- **U42 ꜥpr ḥḥ·f, U45 ḫmt … ḫꜥw·f, U6, U12, U13 tm "come to an end".** All kept: each doubt is stated in the note and marked in `l`/`i`.
- **U22 R7 described as "the small bowl"** (the packet says censer). Kept: R7 is the bowl with smoke, and the description is not wrong.
- **U3/U17 reading psd with lemma psḏ.** Kept: this is the house writing and tagging (hymn-to-ra U3).
- **U12 n wnn·i im** has no form label. Kept: no label is wrong, and the doubt about the sense is stated.

### For the glosser

No lemma was renamed or added. The lemmas used that are not in known-lemmas.json (14):

qrrt, ḥfd, ibḥ, ꜥbꜣ, rwty, wꜥw, imḥt, šfyt, sḥr, rw, sḏf, ꜥḏ, šꜣs, nꜣg.

These known entries are too narrow for this part (`__broaden__`):
- is (known only as "tomb"; here the particle "indeed", U42, U44);
- tm (known only as the negative verb; here also "be complete, come to an end", U13);
- ḫꜥ (known only as the verb; here the noun ḫꜥw "appearings, crowns", U45);
- ḫm (known as "not know"; here read ḫmt, taken as "without (?)", U45, doubtful).

## Pass 2

Method. All 46 units were read again from the start, word by word, in a fresh merged view of units.json and the packet (`review2/view.py`, output `review2/all.txt`). Each word was checked for every glyph's role and tr, its reading against the signs and Budge's letters, its morph, its say form, and its grammar labels. `l` was checked word by word, and `i` against `l`. House roles, readings and say forms were checked by script against the published `ani-*.json`: mk / mk-tw, m-m, mi, rdi(t), wi, sp sn, ir·k, wnw, iꜥḥ, swty / stẖ, ꜣḫ·kwi, "(iw)" and "(twice)" in `l`. Then gloss.json was checked entry by entry against the text and known-lemmas.json. No modern translation was opened or recalled. Budge's English was used only as a check on sense.

Edits were made by script (`review2/edit.py`, `review2/edit2.py`). Before replacing anything, each text replacement was asserted to match exactly once, and each gloss value was asserted equal to its old value. Both files were written back in their own format: json indent 1, ensure_ascii off, no trailing newline. The pre-edit copies are `review2/units.before.json` and `review2/gloss.before.json`. After the edits, `review2/check.py` confirmed:
- the 1001 sign codes, joined in order, equal the packet's sequence;
- glyphs, q and morph are identical to the pass-1 file;
- every q and every morph g covers its word's glyphs once;
- every det has an empty tr and no other role has one;
- every morph lemma is either in known-lemmas.json or a gloss key, and no gloss key is unused;
- every `__broaden__` entry begins with exactly the known entry + " · " and is used in this part.

Counts: 0 major, 5 minor, 7 style (12 changes: 6 in units.json, 6 in gloss.json).

### Changes — units.json

- U0 · n · **minor** · The note called wnt "its infinitive with t" under the lemma wn, a verb of two consonants, whose infinitive takes no t. · The note now says the t is one that the infinitive of a two-consonant verb does not take, so the form (infinitive or noun) is not clear.
- U3 · n · **minor** · The note quoted Budge as "uārt", but the packet prints "uart". · → "(Budge: uart)".
- U5 · n · **minor** · Pass 1 changed `l`/`i` to the infinitive "my going", but the note still opened "šmt·i 'I walk'" and then called it the infinitive. · → "šmt·i 'my going'".
- U0 · n · style · The note called pr the infinitive of pri without saying that the infinitive's t is missing. · ", its t not written" added.
- U19 · n · style · The first sign of wꜥw (coded K1, not that sign) has tr w only because Budge reads u. The note did not say so. · Clause added: "the first sign taking his u only because he reads it so".
- U40 · l · style · `i` has "at his strides(?)" (pass 1), but `l` had "strides-his" with no doubt marked. · → "strides(?)-his".

### Changes — gloss.json

- ḫꜥ · `__broaden__` · **minor** · Pass 1 asked for this entry and the glosser left it out. The known entry has only the verb, and U45 has the noun ḫꜥw. · Added: known entry whole + " · also ḫꜥw, appearings, glorious appearances; crowns (noun m. plural; Budge: χāāu)".
- mwt · `__broaden__` · **minor** · The entry was not needed. The known entry already has "to die (verb; often written mt, without the w; Budge: mit)", which is the U15 word. The added "death, dying (the infinitive …)" only names an infinitive, which the house does not gloss separately (compare prt under pri). It also repeated "Budge: mit". · Removed.
- rr · `__broaden__` · style · The new sense was pinned to this line ("the sense of the verb after rdi 'let'"). · → known entry + " · also to turn about, turn back (verb; Budge: rer, 'to return')".
- nꜣg · style · Pinned to the line ("the parallel with qq 'eat'"). · → "the sense is a guess from Budge".
- rw · style · Pinned to this print ("Budge: no transliteration, only …"). · → "(noun m.; also the lion as a god; written with the recumbent lion; Budge: 'the Lion-god')".
- šfyt · style · No Budge reading, unlike the other new entries. · "Budge: śeft" added.

### Checked and kept

- **Broadenings kept** (each is used in this part and begins exactly with the known entry):
  - is: the particle, U42, U44;
  - bꜣ: the verb "hack open (?)", U39;
  - ir: the noun irt "deeds", U1 irt·k (the known entry has only the verb and particles);
  - rr: "turn back", U31;
  - sꜥḥ: the stative verb, U29;
  - ḫm: ḫmt "without (?)", U45.
- **tm — refused (pass 1's suggestion).** The known entry already has "a second word of the same spelling: to be complete, whole (verb)". U13's "come to an end" is a rendering of that sense in context, so it is not a new sense.
- **New entries.** All 14 (qrrt, ḥfd, ibḥ, ꜥbꜣ, rwty, wꜥw, imḥt, šfyt, sḥr, rw, sḏf, ꜥḏ, šꜣs, nꜣg) have correct grammar labels and mark their doubt. The one place name, imḥt, gives Budge's àmmeḥet. No modern sense is invented: every doubtful sense is marked (?) and attributed to Budge or to the classifier.
- **House checks** (published parts):
  - mk-wi is hyphenated as the house mk-tw;
  - m-m with D36 phon ꜥ is the house tagging;
  - mi with G17 D36 is the house writing;
  - "(iw)" and "(twice)" in `l` are the house form;
  - wnw "Wenu" and iꜥḥ "Iah" match the house;
  - swty under the lemma stẖ matches 043.

### Refused

- **ꜣḫ·kwi (U29): G43 phon w, "not read".** The house ꜣḫ·kwi (one case) has no chick. Here the chick is printed, and the note says it is not read. Kept.
- **U26 ḥsq·i: sḏm·f rendered "have cut out".** The note states that the sḏm·f here is of a deed done, and the sense of the passage requires the past. Kept.
- **U9 / U19 U15 as a classifier of wn.** The packet codes what is printed, the note names the sign, and the house 043 writes wn·w the same way. Kept.
- **part "walking".** This is a general description of Spell 74, not a translation of wnt. Kept.

Totals: 12 changes — 0 major, 5 minor (3 units, 2 gloss), 7 style (3 units, 4 gloss); 4 findings refused; nothing unresolved.
