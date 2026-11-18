# Review — ani-125-rubric

## Pass 1

I edited units.json by script (scratchpad review1.py, review1b.py). No sign code, sign order or glyph count changed. After the edits, the concatenated glyph sequence (345 signs) still equals the packet's w0–w98 and source/established/ani-125-rubric.json (checked by script).

Units are numbered by the first word index in the draft (the draft has 100 words, w0–w99, after the drafter's two splits and one join).

### Changes

Format: unit · field · severity · what was wrong · what was done.

1. Unit ln4 (w36–w43) · n, l, i · **major** · The note called n ḫnd·n šꜣi "n + the sḏm·n·f, the usual negative 'has not, has never'". That is the wrong label. With n, the sḏm·n·f states a general or present truth ("does not, cannot"). The past negative is n + sḏm·f, as the address note says ("n with a sḏm·f is the past negative"). · The note now gives the correct label. l "not · has-trodden" → "not · treads". i "on which no pig has trodden" → "on which no pig treads".
2. Unit ln5 (w44–w50) · n, l · **major** · The main reading took irt as a passive "is made", explaining the t as "the t that this verb often shows". The passive sḏm of iri has no t. The t is the regular infinitive ending of this class of verb, and ir + infinitive is the usual way a rubric states its condition. · The note now reads irt as the infinitive with šꜥt tn as its object, and says the English renders it as a passive. l "is-made" → "making". i is unchanged, since the English passive keeps the sense.
3. Unit ln8b (w85–w87) · n, l, i · **major** · nswt-bity was taken as the plural "kings" on the grounds of "the stroke". A single stroke Z1 does not mark a plural, and a single seated king (A43) is written. The plural is Budge's and is not in the signs. · The text is now singular "the king of Upper and Lower Egypt". The note says it may be meant generally and that Budge's "kings" is not shown. l → "the-king-of-Upper-and-Lower-Egypt".
4. Unit ln8b · l, i, n · minor · "ushered in" for stꜣ goes beyond the word ("drag, draw, haul") and sounds like a remembered modern rendering. · l "is-ushered-in" → "is-drawn". i → "He will be drawn along together with …". The note's gloss is now "drag, draw, haul (… hauling a sledge or towing a boat in procession)".
5. Unit ln10 (w95–w99) · i, n · minor · "Truly proven": "proven" is not in šs mꜣꜥ ("truly right"). It is an interpretive, translation-style phrase. · i → "Truly right, a million times." The note no longer says "proven".
6. about · minor · Four problems: (a) "clean clothing" — "clean" is in Naville's parallel (footnote), not in Ani's text; (b) "where no pig has trodden" (see 1); (c) "stand in the king's favour" states as fact a reading the ln6b note leaves untranslated (sšd …?); (d) "proven true a million times" (see 5). · Changed to "clothing", "on which no pig treads", "be near the king among his courtiers" and "'truly right, a million times'".
7. Unit ln1 (w0–w14) · n · minor · On w0, the case for ir rested only on "the usual way for a rubric to name the person". · The note now gives the reason that actually decides it: the name is resumed by the ·f of wnḫ·f, which is the ir + noun … sḏm·f pattern ("as for N, he …"). in + noun would be followed by a participle with no resumptive suffix. It also says plainly that the sign is unidentified and the reading rests on the grammar alone. The reading, roles and l/i are kept. The U7/phon/r coding follows the published practice for a substitute sign (e.g. U28/phon/ḏ in the introduction).
8. Unit ln1 · n · minor · V12 (band of string, which classifies binding and tying) was called "a tied band as classifier of cloth". · Now "a band of string (V12) as classifier".
9. Unit ln3 (w24–w35) · n · minor · ist was described as "reed i, bolt s, t", but the glyph is S29, the folded cloth. · Corrected.
10. Unit ln3 · n · minor · No verb form was given for sš "drawn". · Added: no ending shows the form, and it is taken as the passive participle describing the image.
11. Unit ln8 (w78–w84) · n · minor · sbꜣ was described as "bolt s", but the glyph is S29. · Corrected to the folded cloth.
12. Unit ln8 · n · minor · "He will not be held back" is a future, but the papyrus writes single n (classically the past with sḏm·f; the future negative is nn). The note did not say so. The verb dni was also stated without doubt, although its sign Q2 is unexplained and Budge reads "separated". · Added a sentence on n written for nn, and a sentence that the verb and its sense are not certain.
13. Unit ln8b · n · minor · stꜣ was described as "bolt s", but the glyph is S29. · Corrected.
14. Unit ln9 (w88–w94) · n · minor · gs (Aa13) was called "the half-loaf". Aa13 is an uncertain object (signs-egyptian.json), and the print gives it the same shape as Aa15. · Changed to say this.
15. w36 skr·tw, w79 dni·tw·f, w85 stꜣ·tw·f · glyphs role/tr · minor · The t and w of the sḏm·tw·f were coded `suff` "·t"/"w". tw is not a suffix pronoun, and the published address codes the same morpheme as phon "t", "w" (pr·tw). · Changed to phon "t", "w". The morph lemma sḏm·tw·f is unchanged.
16. w25 ir · glyphs role · style · D4 was `log`. The model (ir·i), the address (ir·n·k) and this part's own w45 irt code D4 as phon "ir". · Changed to phon.

**Counts:** major 3 · minor 12 · style 1 (16 changes).

### Checked and found correct (no change)

- **q for the split and joined groups.** In the published parts, a split cuts Budge's q string at the word boundary and re-indexes each piece, so the joining separator falls away. For example, address reχ-kuà-ten "0:1-2-3:4*5-6:7:8" became "0:1-2-3:4*5" + "0:1:2", and peti trà "0:1-2-3-4" became "0:1-2" + "0-1". A join concatenates the pieces with "-" and shifts the indices: introduction neter + sentrà ("0-1:2:3") became "0-1-2:3:4", and ḥetep "0:1*2" + neter "0-1" became "0:1*2-3-4". The draft follows this exactly:
  - w15 "0-1:2-3-4-5:6" → wdn "0-1:2-3-4" + n·f "0:1"
  - w24 "0-1:2" → ir (none) + n·k "0:1"
  - w39 "0:1:2-3-4" + w40 (none) → ḫnd·n "0:1:2-3-4-5"

  Every other word's q equals the packet's.
- **Rubric flags** match the established file word by word, and the split pieces inherit their flag. Each unit with red words says so.
- **ln values** each match the papyrus line of the unit's first word. "p" is set on the first unit only.
- **Unread or extra signs** (the ṯ in wdn, the t n in msw, the second n in šns, the second ꜣ in šꜣi, the w in dni and stꜣ) keep phon with their own value. The published parts do the same (sgr·n·i w, ḏꜣḏꜣt s), and the notes use "The papyrus writes X; read Y." where a correction is made.

### Considered and refused

- **w0 ir vs Budge's in (àn).** I kept ir. The sign is neither N35 nor D21, so the signs settle nothing. The resumptive ·f of wnḫ·f favours ir + noun. Budge's in + noun would need a participle with no ·f. The doubt is now stated plainly (change 7). I did not add "(?)" to l/i: the sense of the clause does not depend on the particle.
- **w99 sp roles** (O34/Q3 comp, O50 phon). The address codes sp·i as O34 phon, Q3 phon, O50 det, which is a different coding. The draft's coding fits the conventions' definition of `comp` (a consonant repeated from a multiliteral sign) and is not wrong. I left it, and flag it for consistency in pass 2 or at build.
- **w20 r "goose"** (D21 phon + Z1 det + G38). Arguably D21+Z1 is the stroke-marked word sign, and the goose word may be rꜣ. This does not affect sense, and Budge reads re. I left it.
- **w34 F1 phon "ḫnt"** contradicts the note's "no value of the head gives ḫnt". The note already says the reading is kept only after Budge, and "pigment(?)" is marked. I left it: no better reading is supported by the signs.
- **w46 Y1 log "šꜥ".** The word is written without š and ꜥ. The coding follows the published substitute-sign practice, and the note says so. I left it.
- **w67 di·w·f with the dative n missing.** This is not a slip with only one possible reading, so it is not forced into the "The papyrus writes … read …" form. The note already gives the doubt and Budge's agreement. I left it.
- **w60 sšd** with the lemma glossed "(meaning uncertain)" and the word left untranslated in l/i. This is honest as it stands. I left it.
- **ln6 "flourish like Ra"** with "like" unwritten. The note says so, and Budge supplies it too. I left it.
- **ln1 i "shod in white sandals".** This is a natural rendering of ṯbi m tbwt ḥḏty and not an imported phrase. I left it.
- **ln2 snṯr S29** may be the arrowhead sn of the introduction's spelling. The packet's description (triangle at the foot) does not support this, so I made no change.
- **ln1 "m 'with' is the rib-like Aa15 again"**: "again" points back to w7, which the note does not name. This is too slight to change.
- **gloss.json** is outside this pass. For pass 2 / the glosser: šꜥt is "broadened" with "writing", and ḥḏ with "white". Both are probably separate lemmas (šꜥt "document"; ḥḏ "white"), which is a glossary-structure question. "wnn-nfr" say "Wenen-nefer" and i "Wennefer" are consistent with the rule and the gloss.

## Pass 2

I edited units.json and gloss.json by script (scratchpad review2.py). No sign code, sign order or glyph count changed. After the edits, the concatenated glyph sequence (345 signs) still equals the packet's w0–w98. Every morph lemma is a known-lemmas key or a gloss.json key. No gloss.json key is unused. Every `__broaden__` value is the known entry copied whole, followed by " · ". Each word's morph indices cover its glyphs exactly once. Word numbers below are the draft's w0–w99, as in pass 1.

### Changes

Format: unit · field · severity · what was wrong · what was done.

1. Unit ln7 (w66–w77) · l, i, n · **major** · ḫꜣwt was translated "the altars". ḫꜣwt is a feminine singular noun ("altar, offering table", as in its own glossary entry). Only R1 and two t's are written, with no plural strokes. The plural is Budge's ("the tables"), and the signs do not show it, which is the same ground on which pass 1 made nswt-bity singular. The note also explained the t of ꜥꜣt as loose agreement "with the altars", which overlooked that ḫꜣwt is itself feminine. · l "the-altars" → "the-altar". i → "upon the altar of the great god". The note now says ḫꜣwt is feminine, that no plural strokes are written, and what Budge has. It explains the t of ꜥꜣt as agreement with ḫꜣwt or as written by attraction, and gives the reason for translating "great god" (the usual phrase nṯr ꜥꜣ).
2. w99 sp · glyphs role/tr; ln10 n · minor (consistency; pass 1 left this open) · The draft coded the signs O34 comp, Q3 comp, O50 phon "sp". The published address spells the word out twice in the same way and codes it O34 phon "z", Q3 phon "p", with the final sign as `det`: sp·i with O50 det, and sp·i with N5 det. It uses O50 `log` only when the sign stands alone. · Recoded to O34 phon "z", Q3 phon "p", O50 det. The note now reads "bolt s and p, with the threshing floor (which can also write the word alone) as classifier".
3. w34 ḫnty · glyphs role · minor · F1 is coded phon "ḫnt", so the following X1 repeats a t the sign already carries. Coding it phon "t" counted the t twice. The introduction's ḫnty codes the same t as `comp` (W17 phon ḫnt, N35 comp, X1 comp, Z4 phon y). · X1 → comp "t".
4. Unit ln6 (w51–w57) · n · minor · msw: the note said "a stroke for the plural". This contradicts the rule pass 1 applied to nswt-bity, that a single stroke does not mark a plural. · Now reads: "a seated man and woman (the classifier of people) and a stroke; the plural is not otherwise marked".
5. Unit ln6b (w58–w65) · n · minor · šnyw·f "his courtiers" is written with A21, A1, a stroke and ·f, with no plural strokes. The note did not say where the plural comes from. · Added: "No plural strokes are written; the plural is taken from m 'among'."
6. Unit ln5 (w44–w50) · n · minor (honesty) · šꜥt is written Y1 + X1 + Z1, with no š and no ꜥ. The papyrus roll with t and stroke is the regular writing of mḏꜣt "book, papyrus roll", and the note did not mention it. · Added a sentence: mḏꜣt fits the signs at least as well and gives much the same sense, and the reading šꜥt rests on Budge. The reading and the translation are kept, since "writing" covers both.
7. Unit ln1 (w0–w14) · n · minor · "m 'with' is the rib-like Aa15 again": Aa15 is an uncertain object (signs-egyptian.json), not a rib, and "again" pointed back to nothing. A capitalised "What" also followed a semicolon. · Now reads "m 'with', both here and before tpt, is Aa15, an object of uncertain nature that often writes m", and the punctuation is fixed.
8. about · minor · There were two mismatches with the units. (a) "drawn … on clean ground on which no pig treads" ran two clauses together: the picture is drawn on clean ground, and it is then buried(?) in a field on which no pig treads. (b) "he will flourish with his children's children, be near the king" did not match the units. Ln5/ln6 have him and his children's children flourishing, and "near the king" has no word behind it: sšd is left untranslated, and the text has "among his courtiers". · Now reads "drawn in pure pigment on clean ground and buried(?) in a field on which no pig treads", and "he and his children's children will flourish, he will be among the king's courtiers".
9. w51, w53 msw · morph lemma; gloss.json · minor · The glosser's new key "ms — to bear, give birth to (verb); msw 'children'" duplicated the published verb lemma msi (known: "to give birth; (passive) to be born"). Its entry was also pinned to the noun. · The morph lemma is now "msw". The gloss key "ms" is replaced by "msw — children, offspring (noun; plural of ms 'child', from msi 'give birth')".
10. gloss.json `__broaden__` šꜥt, ḥḏ, kꜣ · minor (open item from pass 1) · The homonyms were added as "also …" senses of one word. The published glossaries keep a homonym under the same key and mark it "a second word of the same spelling" (pr "comes forth" / "house"; ḥr "face, upon" / "Horus"; ꜥꜣ "great" / "donkey" / "door"). They never use a distinct key. So the lemma keys in units.json stay as they are. · šꜥt: "· a second word of the same spelling: letter, document, writing (noun)". ḥḏ: "· a second word of the same spelling: white, bright (adjective; verb 'be white, bright'; written with the mace)". This drops "ḥḏt 'white'", which would be read as the White Crown. kꜣ: "· a second word of the same spelling: bull (noun; written with the bull)".
11. gloss.json `__broaden__` sš · minor · The added sense was pinned to this line ("sš 'drawn, written'"). · Now reads "· also to write, draw, paint (verb; written with the scribe's palette)".
12. gloss.json `__broaden__` wꜣḏ, n, m (new) · minor · The units use senses that the known entries lack: wꜣḏ "greens" (a noun; the entry has the adjective and verb only), n "without" before a noun (ln6), and m "among" (ln6b, ln9). · Broadened each: "· also fresh plants, greens, vegetables (noun)"; "· the negative also before a noun, 'without, there being no …'"; "· also 'among' (with a group of people)".
13. gloss.json stꜣ · minor · The entry kept "to usher in", the phrasing pass 1 removed from l/i as a likely remembered rendering. · Now reads "stꜣ — to drag, draw, haul (verb; of hauling a sledge or towing a boat)".
14. gloss.json sḏm·w · minor · "(verb form; written after the verb)" is contradicted by its only occurrence, where the w stands above the arm, before it. · Now reads "the w sometimes written with the passive sḏm, '… is done, … is given' (verb form)".
15. gloss.json ṯbt · minor · "plural ṯbwt, 'a pair of sandals'" confused the plural with the dual. · Now reads "sandal (noun; plural ṯbwt, later written tbwt)".
16. gloss.json sšd · style · The entry "sšd — (meaning uncertain)" had no meaning slot. · Now reads "sšd — a word not identified here (meaning uncertain; Budge: seśeṭ, sic)".
17. gloss.json tpt · style · The meaning slot "the first, finest (of oil)" did not read as a noun gloss. · Now reads "finest oil, oil of the first quality (noun; from tp 'head, first'; reading and sense uncertain)".
18. gloss.json wnn-nfr · style · The entry had no grammar label. Name entries in the published glossary use "(god's name; Budge: …)". · Now reads "Wennefer, 'he who is (always) perfect', a name of Osiris (god's name; Budge: Un-nefer)".

**Counts:** major 1 · minor 14 · style 3 (18 changes).

### Checked again and found correct (no change)

- Every glyph's role and tr against its reading, for all 100 words. The coding agrees with the published parts for wsir, ꜣny, mꜣꜥ-ḫrw (Aa11 phon + P8 log), ꜥntyw, ḥtp/ḥtpt (R4 phon + t, p comp), sm (O34 comp z), ḥr·s (D2 phon + D21 comp + O34 suff ·z), wꜥb (D60 log + N35a det), wnn (E34 phon + N35 comp, the second N35 phon), nswt, nṯr (R8 phon + A40 det), sbꜣ (N14 phon + ꜣ comp + O1 det), imntt, ḥnꜥ, ꜥꜣt and ds. The noncontiguous morph indices (skr in skr·tw) follow published practice (ms·t, gs·fy, mwt·f).
- Grammar labels: n + sḏm·n·f ("cannot/does not", pass 1's correction) is right. irt as the infinitive of the 3ae-inf. verb with its t is right. The geminated wnn·f (future) is right. The sḏm·tw·f passive in skr·tw, dni·tw·f and stꜣ·tw·f is right. nw is the plural genitive, nt the feminine genitive. nty for ntt after a feminine noun is noted.
- say: checked against the published forms for clusters. khenden matches khendek, sekertu matches rekhtu/pertu, hedjty matches pehty/Qedty, imentet is as published, and Wenen-nefer follows the rule for names. All say forms are consistent.
- Rubric flags, ln values and q are unchanged since pass 1. I rechecked the ln and the red/black statements in the notes against the packet: w62 nswt and w64 onward are black, and w63 m is red.

### Considered and refused

- **"finest oil" (ln1 l/i)** is Budge's wording ("the finest oil"), but it is the plain lexical sense of tpt and not a period phrase like "triumphant" or "saith". Alternatives such as "first-quality oil" read worse and teach nothing more. I kept it.
- **Distinct lemma keys for šꜥt "writing" / ḥḏ "white"** (for example šꜥt-2). The published glossaries never do this; see change 10. I kept the same keys, with the published "a second word of the same spelling" wording.
- **šꜥt → mḏꜣt as the reading** (w46). The established Y1 may be the reader's identification of a flat sign that Budge, reading śā, took as the pool N37. The sense is the same either way. The alternative is now stated in the note (change 6), and the reading follows Budge.
- **di·w·f with the passive w written before the arm, ·f "to him"**: pass 1's reasoning stands. The note already gives the doubt.
- **F1 phon "ḫnt"** (w34): pass 1's refusal stands. The substitute-sign coding follows Budge, and the note says that no value of the head gives ḫnt.
- **D2 / F34 coded log + Z1 det here but phon in some published words**: the published parts use both codings for ḥr with its stroke. This part uses log consistently when the stroke follows and phon with the complement r. This is acceptable as it stands.
- **šmsw "followers"** is unmarked for plural, as šnyw is, but šmsw is commonly collective ("retinue"), and m "among" carries the group. I left it.
- **n (single) for future nn in ln8 ("as other copies sometimes do")**: this is a fair general statement about New Kingdom spelling. I left it.
