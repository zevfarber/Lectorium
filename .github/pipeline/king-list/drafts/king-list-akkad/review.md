## Pass 1

### What I read

- Pipeline files:
  - run3/RUNBOOK.md (the Reviewer section)
  - conventions.md, runbook.md
  - packet.md, drafter-notes.md and units.json
- For house practice:
  - the pilot king-list-antediluvian.json
  - the glossaries and units of all published king-list-*.json, especially akshak-kish-iv-uruk-iii
  - the review of that part
- Langdon pp. 17–18 (langdon1923_0022–0023.jpg): the transliteration, the translation and fns. 1–15 and 1–3.
- Plates, at 2–8× zoom:
  - Pl. III (0044): Col. VI 29–48.
  - Pl. IV (0045): Col. VII 1–14.
  - For comparison: Pl. I II 9–10 (KA, GI₄) and Pl. II III 4 (SAG) and III 18 (ab-ba-ni).

### How the edits were made and checked

Edits were made by script (scratchpad reviewer/rev1.py): load, modify, dump with indent=1 and ensure_ascii=False. No cuneiform was retyped; one sign key changed, SAG → KA.

Checks:
- Every morph `g` covers its word's glyphs exactly once (asserted).
- `r3.py build` → BUILT, 15 units.
- `validate` → **PASS**. Two WARNs:
  - The unit 0 note is still long, now 1861 chars, down from 2450. It covers six prism lines.
  - linecheck VI 33, confirmed below.
- `signs.py check` → in sync.
- Afterwards stories.json was checked out and king-list-akkad.json deleted. `git status` shows only units.json changed.
- gloss.json and new-lemmas.json were not touched.

### Changes

- **VI 33 · words (sagi glyph 0), morph gloss, n, about · major**
  - What was wrong: the drafter replaced Langdon's KA with SAG "from the drawing", comparing the sign only with the KA of II 10.
    - The first sign of VI 33 is a small pointed head (a large corner-wedge) with one upright and a slanting wedge below. It has no inner strokes.
    - It is unlike KA on this copy: in II 9 and II 10 KA is a box filled with strokes.
    - It is equally unlike SAG on this copy: in III 4, ḫur-saĝ, SAG is a box with diagonals and uprights.
    - So the copy does not support replacing the sign. Langdon drew the copy and reads KA, and conventions say his reading is the base. This is the same reasoning as the long Gimil in VI 9 of the last part.
  - What was done:
    - Glyph 0 is KA again (log, tr sagi). The word is still read sagi as one word, as sib → sipa.
    - The note and the morph gloss now say that the drawn form is unlike the usual KA (and unlike SAG) and that the identification is uncertain.
    - The SAG claim was removed from `about`. The uncertainty is now flagged there.
- **VI 33 · morph (Ur-Zababa) · minor**
  - What was wrong: the stray upright marked "sic!" had its own lemma, "(sic)". House practice (ur-i-awan; VI 17 x-mu-ti) puts a visible unread sign inside the name's morph, and a "(sic)" glossary entry is not a word.
  - What was done:
    - The DISH glyph (punct, tr "(sic)") stays and is now covered by the `ur-{d}za-ba₄-ba₄` morph (g 0,2,3,4,5).
    - The "(sic)" lemma was removed.
    - The broadening of the Ur-Zababa gloss now mentions the wedge.
- **VI 31 · n · minor**
  - What was wrong: the note was 2450 chars, and it was rewritten for the KA change anyway.
  - What was done: it was tightened to 1861 chars. All the sign information and Langdon's footnotes are kept.
- **VI 31 · l · style**
  - What was wrong: the reading is `lu₂(?)`, but `l` "the-man-who" carried no query.
  - What was done: it is now "the-man(?)-who".
- **VI 37, VI 39, VI 43, VI 46, VII 9 · l · style**
  - What was wrong: house `l` style puts " — " before the reign after "son of X" (ur-i-awan IV 26, uruk-i V 25, akshak VI 3 and VI 12). The draft had a comma.
  - What was done: the comma is now " — ".
- **VII 11 (VII 12 total) · n · minor**
  - What was wrong: "197, which their figures do yield (55 + … + 15)" presented Langdon's arithmetic as ours, and it did not cite the variants.
  - What was done: it is now attributed to Langdon's fn. 3, with P. 2 Rev. III 2 and S. Rev. 8. The sum was rechecked and is 197.
- **na-ra-am-{d}suen · morph gloss (VI 43, VI 47) · minor**
  - What was wrong: "the god's name and the following line are largely restored" was pinned to one line, and it was wrong for VI 47, where the whole name is restored.
  - What was done: it now reads "the god's name, and in its second mention the whole name, are in a break and restored by Langdon".

**Counts: 1 major, 4 minor, 2 style.**

### Drafter's contested calls: verdicts

- **VI 33 sagi vs ka-šu-duĝ:** refused as SAG, kept as Langdon's KA (see Changes). The reading sagi as one word is accepted.
- **VI 33 "(sic)" wedge: confirmed.**
  - The copy has UR, AN, ZA, then a single upright with a tiny "sic" printed beside it, then MUŠ₃ MUŠ₃.
  - It is shipped as DISH (punct, "(sic)") inside the name's morph.
  - Langdon's transliteration ignores it.
- **VI 34 a-de₃ (sic) and lu₂(?): confirmed.**
  - The copy has 8 signs: LUGAL | A, with "sic!" printed after it | NE (a crossed box) | a sign with a "?" drawn inside it | A GA NE KI.
  - Langdon's "A-ga-de (ki)" for the first Agade is not on the copy. The plate is followed.
  - The query sign is LU₂-like. lu₂(?) follows Langdon's galu, and the house has the precedent en-nun-dara₃(?).
- **VI 31–32, the name split: accepted.**
  - VI 31 is A GA NE + ŠAR RU KI IN. ŠAR is the same box of corner-wedges as the SAR of nu-giš-šar (VI 32) and ŠAR in VI 37 and VI 41.
  - VI 32 is NI (dotted damage outline), LU (a gridded box), BA, NI. It is not the AB BA NI of III 18.
  - Langdon's one-name reading is kept and flagged as uncertain.
- **VII 2, extra visible signs: accepted as Langdon's one gí, flagged.** The group (a box with uprights, uprights, a slanting wedge) resembles the GI₄ of II 10 (dug₄-ga-gi₄-ib) closely enough.
- **VII 6 [4]: confirmed.** The hatching ends at mid-line. Only LUGAL is drawn, and there is no figure. Langdon gives no "(?)", so the 4 is shipped bracketed.
- **VII 9 [šu-dur-ulₓ]: accepted.**
  - KIB is the sign key (GIŠ crossing GIŠ, 𒄒).
  - Langdon marks ū̄l as an unusual value. He takes it "after Scheil, probable reading of KIB as ul" (fn. 1).
  - ul is not a standard value of KIB, so ulₓ is the honest notation, and readings follow the sign.
  - The Gimil rule is followed: restored, so ŠU (log), as in VI 1 and VI 3 of the last part.
  - DUR = GU₂×KAK (𒄙) is acceptable for the plain value dur, and the name is wholly restored.
- **VII 8 [mu] and the 21 trace; VI 42 [ni-ag]: confirmed** on the plate.
- **Numerals: house practice is followed.**
  - The count-of-kings lemmas are the value: "4" as in ur-i-awan IV 3, and "11" as "12" in uruk-i III 35 and "23" in kish-i II 42. **"11" is correct.**
  - Years are u/diš/geš clusters: 56 = FIVE U + SIX DISH, 9 = NINE DISH, 15, 21 = U U + DISH, 3 = THREE DISH, 181 = THREE GESH2 + DISH. These match the plate (VI 36 <<<+6 wedges, VII 12 three tall uprights + one).
- **VI 45 and VI 48:** Langdon's "38 (?)" and "24 (?)" are LACUNA glyphs, not signs. Correct.
- **Totals:** reported, not corrected.
  - The surviving reigns make 56+9+15+3+21+15 = 119.
  - 181 − 119 = 62 = 38 + 24, Langdon's reckoning in fn. 3.

### The drafter's claim about the published VI 30 (assessed; nothing edited)

**I agree that the published reading is doubtful.**
- On this plate NE is the crossed box alone:
  - In VI 34 (twice) it is followed directly by LU₂ and by KI.
  - In VII 13 it is followed by the pointed lozenge KI.
  - In VI 31 it is followed by ŠAR.
- VI 30 draws A, GA, the crossed box, a box of corner-wedges, then the lozenge KI, EŠ₂, BA and DU. That is 8 signs where Langdon has 7.
- The box of corner-wedges is drawn exactly like ŠAR/SAR (VI 31, 32, 37, 41). The published part merges it into a "two-part NE". That merge is not supported by the three other writings of NE in this stretch.
- VI 30 most likely has an extra sign that looks like SAR between a-ga-de₃ and KI. It might be a scribal slip, but that is not certain.
- For the owner (QUESTIONS.md) at publication. The published part is not changed by this run.

### Plate vs Langdon

- VI 31: A GA NE · ŠAR RU KI IN. There is no KI after Agade, as Langdon.
- VI 32: NI LU BA NI · NU GIŠ SAR. NI and LU are inside a damage outline.
- VI 33: KA(?) ŠU DUG · UR AN ZA DIŠ("sic") MUŠ₃ MUŠ₃. **Langdon omits the DIŠ.**
- VI 34: LUGAL A("sic!") NE · LU₂(?) · A GA NE KI. **Langdon prints A-ga-de (ki) for the first.**
- VI 35–41: as Langdon.
- VI 42: MU, 15, then hatching with traces. **Langdon prints ni-ag unbracketed.**
- VI 43–48: as Langdon's brackets. In VI 43 the AM is at the edge of the break and there is a trace at the far right.
- VII 1: as Langdon.
- VII 2: the visible group is read as gí (Langdon).
- VII 3–5: only LUGAL is visible.
- VII 6: **no figure drawn** (Langdon prints 4).
- VII 7: IB AK.
- VII 8: **MU in the break** (Langdon unbracketed). 21, with the first u a trace.
- VII 9: dumu DU DU KID.
- VII 10: 15, NI, AK.
- VII 11: u + diš, LUGAL.
- VII 12: MU BI, 3 geš + 1, IB AK.
- VII 13: A GA NE KI GIŠ KU BA AN SIG₃.
- VII 14: NAM LUGAL BI UNUG KI EŠ₂ BA DU.
- linecheck: VI 33 only. It is confirmed: sagi = Langdon's ka-šu-duĝ (KA ŠU DUG), the (sic) wedge, and za-ba₄-ba₄ = his Il-ba-ba by sign.

### Uncertain readings (flagged in the notes)

- The first sign of sagi (VI 33).
- -ì-lu-ba-ni (VI 32).
- lu₂(?) (VI 34).
- gí (VII 2).
- ulₓ and the whole of Shu-Durul (VII 9, restored).
- Langdon's [4] (VII 6).

### Lemma changes for gloss.json

- **`(sic)` removed.** The glyph is now inside the `ur-{d}za-ba₄-ba₄` morph. gloss.json and new-lemmas.json should drop "(sic)".
- The `ur-{d}za-ba₄-ba₄` broadening in gloss.json should say: "· also the king whose cup-bearer Sargon was, where the name is clear on the copy but has a stray upright wedge after ZA, marked 'sic!' and not read". The current text, "where the first sign, UR, is clear …", is acceptable but omits the wedge.
- **`sagi` (string unchanged), gloss must change.** The gloss.json text says "written SAG.ŠU.DUG … the first sign is taken as SAG". It should read: "cup-bearer, a court office — read as one word, sagi; the signs are Langdon's KA.ŠU.DUG (his ka-šu-duĝ); the first sign as drawn on the copy is unlike its usual KA, and its identification is uncertain".
- For pass 2: the gloss.json `du-du` entry says the name is "in a break on this prism". That is true of VII 8 but not of VII 9, where DU DU KID is clear. It should say "partly restored" or similar.

### For the owner and signs.py (not done)

- The DUG entry added to signs-cuneiform.json gives the value "in sagi (SAG.ŠU.DUG)". With the KA reading kept, this should be "KA.ŠU.DUG" (Langdon). It is left as it is, per instructions.
- VI 30 (published): an extra SAR-like sign. See above.

## Pass 2

### What I checked

- gloss.json: 19 entries plus `__broaden__` for e-lu-lu, ur-{d}za-ba₄-ba₄ and a-ga-de₃. I checked them against units.json, the plates, Langdon pp. 17–18 (fns.) and the published glossaries.
- units.json: re-read end to end.

### How the edits were made and checked

Edits were made by script (scratchpad reviewer/rev2.py): load, modify, dump with indent=1 and ensure_ascii=False, keeping each file's trailing newline.

Checks afterwards:
- Each broadening starts with the published entry, copied exactly, followed by " · ".
- The lemma sets match: new-lemmas.json keys = gloss.json keys (without `__broaden__`) = the units.json lemmas that are in no published glossary. There are 18.
- Every broadened lemma is used in units.json.
- Build → BUILT, 15 units, 48 glossary entries, no "(sic)".
- `validate` → **PASS**. It gives the same two WARNs as pass 1:
  - unit 0 n is 1861 chars, which is acceptable for a six-line entry;
  - linecheck VI 33, confirmed in pass 1.
- `signs.py check` → in sync.
- Afterwards stories.json was checked out and king-list-akkad.json removed. The build wrote no other file. `git status` shows only gloss.json, new-lemmas.json and units.json in drafts/king-list-akkad/.

### Changes — gloss.json / new-lemmas.json

- **(sic) · major**
  - What was wrong: the lemma was removed from units.json in pass 1, so the entry would have shipped a non-word.
  - What was done: deleted from gloss.json and new-lemmas.json.
- **sagi · major**
  - What was wrong: the entry said "written SAG.ŠU.DUG … taken as SAG from the copy", which is against the pass-1 decision.
  - What was done: it is now "read as one word, sagi; the signs are Langdon's KA.ŠU.DUG …; the first sign … unlike its usual KA, … uncertain".
- **ur-{d}za-ba₄-ba₄ (broaden) · minor**
  - What was wrong: the added text "where the first sign, UR, is clear on the copy (the break is not there)" left out the stray wedge now inside this lemma's morph.
  - What was done: the old entry is kept exactly, followed by " · also the king whose cup-bearer Sargon was, where the name is clear on the copy but has a stray upright wedge after ZA, marked 'sic!' and not read".
- **du-du · minor**
  - What was wrong: "where it stands the name is in a break on this prism" is false where the name stands after dumu, clear as DU DU KID.
  - What was done: it now says that on this prism the name is restored where his own reign is given and is clear where his son is named.
- **na-ra-am-{d}suen · minor**
  - What was wrong: "where it stands the god's name is lost" did not cover the second mention, where the whole name is restored.
  - What was done: it now matches the pass-1 morph text.
- **new-lemmas.json draftGloss · style**
  - What was wrong: the drafts were stale.
  - What was done: each is now set to the final gloss.json text.

### Changes — units.json

- **about · minor**
  - What was wrong: "then his sons Rimush and Manishtishu, Naram-Suen and Shargalisharri" made all four Sargon's sons. The prism makes Naram-Suen the son of Manishtishu (VI 44) and Shargalisharri the son of Naram-Suen (VI 47, restored).
  - What was done: it now reads "… Manishtishu's son Naram-Suen, and Naram-Suen's son Shargalisharri".
- **morph glosses · style**
  - What was wrong: the morph glosses were not aligned with the shipped glossary text.
  - What was done: sagi, du-du, na-ra-am-{d}suen and the three broadened lemmas now have the same text as gloss.json. The wording of a-ga-de₃ and e-lu-lu follows the glosser ("also a king of Agade", "… at the head of the dynasty").

**Counts (pass 2): 2 major, 4 minor, 2 style.**

### Entries checked and kept

- šar-ru-ki-in-i₃-lu-ba-ni and šar-ru-ki-in: the signs and Langdon's form are right. "Sargon" is given as the English name, and the uncertainty is kept.
- nu-{ĝeš}kiri₆: GIŠ.SAR = kiri₆ by sign. nu is given as a profession-forming element, which is a fair, general description.
- ri-mu-uš.
- ri-mu-šu-uš: the last two signs are swapped against Langdon's ri-mu-uš-šu, as stated.
- ma-ni-iš-ti-iš-šu: Ma-ni-iš-te-šu is in Legrain No. 1, the Nippur text (fns. 4, 7).
- šeš-gal.
- šar-ga-li₂-šar-ri: restored from L. No. 1 VII 15 (fn. 9).
- a-ba and nu: the grammar is right. a-ba-am₃ is the interrogative + copula, and nu is the negator before a noun.
- i-gi₄-gi₄, i-mi, na-ni: the variants are as fns. 12–13.
- šu-dur-ulₓ: KIB read ul after Scheil (fn. 1), restored.
- 11: house practice for a count of kings (cf. "12", "23").
- e-lu-lu and a-ga-de₃: each broadening keeps the published entry exactly and is general.

No invented modern forms or misnamed grammar were found.

### Re-read of units.json

Nothing else was found. I rechecked every footnote attribution (fns. 1–15, 1–3), every sum (119, 62 = 38 + 24, 197), the eleven names for "11 lugal", the brackets, the `l`/`i` pairs and the house formulas.

### For QUESTIONS.md / conventions.md at publication

1. **VI 30 (published part):** the copy draws a SAR-like box of corner-wedges between NE and KI. Elsewhere in VI 31–VII 13 NE is the crossed box alone, so the published "two-part NE" is doubtful. The published part was not changed.
2. **VI 33:** the first sign of sagi is Langdon's KA, but as drawn it matches neither KA nor SAG on the copy. It is flagged as uncertain, and the owner may want a check against a sign list.
3. **signs-cuneiform.json DUG:** the value text says "in sagi (SAG.ŠU.DUG)" and should become KA.ŠU.DUG. It was not changed, per instructions; it needs signs.py or an owner edit.
4. **New house renderings for conventions.md:**
   - an unread "sic!" wedge goes inside the name's morph (DISH, punct, tr "(sic)"), with no lemma of its own;
   - a count of kings takes the value as its lemma ("11");
   - " — " before the reign after "son of X" also applies to "elder-brother of X, son of Y";
   - KIB = ulₓ after Langdon/Scheil.
