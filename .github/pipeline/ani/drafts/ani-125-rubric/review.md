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
