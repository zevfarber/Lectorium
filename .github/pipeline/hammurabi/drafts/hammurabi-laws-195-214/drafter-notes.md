# Drafter notes — hammurabi-laws-195-214 (XXXIII 41 – XXXIV 54)

units.json: 45 units, 208 words, 107 stele lines covering Harper's lines 1:1 (script check against the packet: every packet line used once and in order, every unit starts at the next stele line; no nl at glyph level was needed — no word breaks across stele lines). `p`/`ln` on the first unit of each law only (195 XXXIII 41, 196 XXXIII 45, 197 XXXIII 50, 198 XXXIII 54, 199 XXXIII 60, 200 XXXIII 66, 201 XXXIII 71, 202 XXXIII 75, 203 XXXIII 82, 204 XXXIII 88, 205 XXXIII 92, 206 XXXIV 4, 207 XXXIV 14, 208 XXXIV 20, 209 XXXIV 23, 210 XXXIV 31, 211 XXXIV 35, 212 XXXIV 41, 213 XXXIV 45, 214 XXXIV 51). Units cross a column only at §205 (XXXIII 92–93 + XXXIV 1). The words were built by script from a spelling table (`/tmp/.../scratchpad/b/lib.py, words.py, units.py`, not retyped per unit); `reading` is generated from the glyphs' `tr`, so every reading reconstructs; every sign key exists; every non-determinative glyph index is in a morph entry; no dotted k anywhere. `python3 ../run3/r3.py validate` says "not built yet" (I did not build, publish or commit); the line check against Harper (ratio < 0.8) lists only the 19 lines where Harper writes the Akkadian word for a logogram or numeral (rit-tê-šu, I ma-na kaspim, ½/⅓, X/V/II šiḳil kaspim, mârat, mâra-zu, zinništum ši, amtum, the {mašak}ḳinazi alpim line) — each confirmed on the plate (below). I ran `git status` once (read-only) to see what the sign tool had touched; nothing else of git.

## Plates read
Plate 56 (PDF 327) only for orientation (col. XXXII/XXXIII, nothing of this part); Plate 57 (329, XXXIII 41–54 on the right column), Plate 58 (331, XXXIII 54–93 and XXXIV 1–3), Plate 59 (333, XXXIV 4–49), Plate 60 (335, XXXIV 49/50–54). Rendered at zoom 3 overview, 5–10 on crops. Harper's List of Signs (PDF 383–409, odd pages carry the table) was read for the stele forms of: UM (no. 65, with the rittu entry), muškēnu (no. 34), ner/NER.SE.GA/NER.PAD.DU (no. 170), GUD (no. 109), ḳinazu (no. 153), ŠÁM (no. 83), su/mašku (no. 5), ah (no. 156), az (no. 63), šu (no. 138), me (no. 184).

Honest limit (as in 185–194): I did not identify every syllabogram wedge by wedge. I compared sign-group counts with Harper's transliteration on the plate for XXXIII 41–81 and 88–93 and XXXIV 1–20 and 49–54 (they agree wherever I counted; clusters are sometimes over-counted by one at a line's start, the same way on parallel lines); XXXIV 21–48 I checked only at overview level (row positions, tier structure, margin numerals), not cluster by cluster. The lines with logograms or unusual groups were read sign by sign. Harper's printed value was followed wherever the plate showed nothing against it. Row mapping checked by the margin numerals (5, 10 … 95 on Plate 60, 30–45 on Plate 59) and by the pencilled law numbers on the plates (196 at XXXIII 45, 197 at 50, 199 at 60, 200 at 66, 201 at 71, 202 at 75 etc.).

### Sign-level findings
- **MAŠ.EN.KAK** (XXXIII 54 tier 2, 56 tier 2, 72, 88, 89, XXXIV 20, 35 tier 2): three signs, cross-shaped MAŠ, bar-and-box EN, triangle KAK, no complement (Harper's list no. 34 muškēnu shows the same four pieces). Bare.
- **NER.PAD.DU** (XXXIII 50, 52, 56, 62): three signs, GÌR/ner (diamond + box + triangle, Harper no. 170, keyed KISH as in 185–194 NER.SE.GA), PAD (fan-and-hook, new sign), DU (box and vertical, Harper no. 89); -šu added at 52 (4 clusters). Bare at 50, 56, 62.
- **warad** (XXXIII 60 tier 2, 62 tier 2, 92): ARAD alone, the dotted triangle (Harper no. 16 wardu); no complement.
- **šîmi-šu** (XXXIII 64 tier 2): ŠÁM (the long left-hand sign with the hatched inside, Harper no. 83) + ŠU; two clusters, not three.
- **ŠU.ŠI** (XXXIII 81): DISH, ŠU (box), IGI (arrowhead and bar, Harper no. 172 ši) — so ŠU.ŠI is written ŠU + IGI (ŠI), not ŠU + SI. The line is DISH ŠU IGI IM MAḪ ḪA AZ (7 clusters).
- **{mašak}ḳinazi alpim** (XXXIII 80): Harper normalizes to two words; the plate is I NA {SU} + three signs (a sprout/star, a cross, the box-and-triangle AZ — Harper's list no. 153 ḳinazu is exactly these three together) + GUD (bars + triangle, no. 109, one sign). So: `i-na {mašak}qi₂-na-az GU₄`. The det is the SU sign (box with hatched inside; Harper no. 5 su, mašku). No -im written on alpim.
- **½** (XXXIV 18, 43): the first cluster is the cross-shaped MAŠ (same shape as in MAŠ.EN.KAK) — the numeral ½ is that sign. Keyed MASH, role num, tr "1/2".
- **⅓** (XXXIII 73, XXXIV 21, 53): THIRD, as in earlier parts.
- **kaspim** everywhere: KU3 UD IM (six clusters in "I ma-na kaspim"): KÙ.BABBAR-im with the -im complement written (checked at XXXIII 58). ma-na is two sign-groups (MA, NA), written in syllables here (Harper lower case).
- **DUMU** (XXXIII 41, 46, 82, 83, XXXIV 17, 20, 93): the DUMU sign alone, no complement (line 41 has the same cluster count as line 17 where Harper writes mâr). DUMU.SAL at XXXIV 24, 35 (mârat) and with ZU at 33 (mâra-zu).
- **GEME₂** (XXXIV 45, 51): SAL + KUR, as in earlier parts; **SAL** alone for zinništum (XXXIV 31, 41).
- **A.ZU** (XXXIV 13): A and ZU, two clusters, bare.
- **uš-ta-dí-ši** (XXXIV 27): four clusters, USH TA DI IGI; `dí` has no separate sign; written di. Compare uš-ta-ad-di-ši (38, 48): five clusters.
- **XXXIV 54 i-ṣ̌a-ḳal**: the plate shows the ordinary I ŠA GAL, three clusters (like XXXIV 50). Harper's caron-and-dot is a printing blemish.
- **XXXIV 4–13**: first rows have two tiers on the plate (4, 5, 13, 14 tier 2 etc.); the {b} marks of the packet fall where the plate has a second tier.
- **maḫāṣum in -zi-**: Harper's ma-ḫa-zi-šu / ma-ḫa-zi-im (XXXIV 14, 36): the ZI sign is a spelling of ṣi (maḫāṣišu, maḫāṣim); keyed ZI, tr ṣi (as the ṣi of ṣi-iḫ-ra-am). am-ḫa-zu (XXXIV 11) is amḫaṣ-šu, ZU = -ssu, as elsewhere.

## Signs added
- **PAD** = 𒉻 (CUNEIFORM SIGN PAD), the middle sign of NER.PAD.DU. Identification by shape against Harper's list no. 170; the entry says so. `signs.py check`: in sync.
Not added: ME for the second sign of rit-tê-šu; SU for {mašak}; MASH for ½; GEME₂ via SAL+KUR; THIRD existing.

## Uncertain readings (all marked in the notes)
1. **rit-tê-šu** (XXXIII 43): the plate shows three clusters: a UM-like box, a vertical-and-bar sign, ŠU. Harper's list no. 65 gives UM + a vertical-and-bar sign as "rittu"; Harper normalizes rit-tê-šu. I key UM + ME (the vertical-and-bar sign looks like his no. 184 me, not his no. 146 te). Both identification and number ("hands", Harper's -ê plural/dual, vs a single hand) UNCERTAIN. Reading `UM.ME-šu`, say rittēšu.
2. **ḫapādum-D / uḫappadū** (XXXIII 49) and **ḫabātum-D / uḫtabbit** (XXXIII 47, 55, 61): the sense "destroy / put out" comes from the law (the talion pair), not from the verbs; ḫapādum is not met elsewhere. English "has destroyed … they shall put out his eye".
3. **eṣemtum** for NER.PAD.DU: the Sumerogram "bone"; the Akkadian ending (eṣemti, eṣemtašu) is supplied, none is written.
4. **lētum** "cheek" (XXXIII 76, 83, 89, 93): dictionary sense (Delitzsch), not derivable from the grammar here.
5. **qinazum** "whip" and the hide determinative; **ŠU.ŠI** = šūši "sixty" with the thing counted not written (strokes supplied in the English only as "times").
6. **risbatum** "brawl" (XXXIV 5), **idû** (XXXIV 10, parsed as an infinitive of edûm after ina), **ṣimmum** "wound": the zi-im-ma-am / ṣi-im-ma-am difference (Harper XXXIV 7 zi, XXXV 21 ṣi; read ṣi throughout).
7. **mēḫrum** "equal" in mēḫrišu (XXXIII 68), ša elīšu rabû "greater than he", ša kīma šuāti "like him": from the forms, fine, but the talion hinge on them.
8. The spoken forms of numbers (ešeret, ḫamšat, šalšāt, šinā, mišil, ištēn) are reconstructed; ⅓ is only the nearest Unicode sign.
9. **tulê-type plurals**: none this time; **idukkū** is the active plural "they shall kill", not an N-stem passive (the house `iddâk` is for the N-stem).
10. Syllabograms not re-checked wedge by wedge: u/TIM/DIM (TIM used throughout, as in 153–194), SU/ŠU/ZU in i-na-ak-ki-su (Harper su, kept SU), BU read pu (pu-uḫ-ri-im), AH read iḫ/uḫ (AH tr follows Harper: uḫ-tab-bi-it, me-iḫ-ri-šu).

## Proposed house renderings (for conventions.md)
Talion formulas, from the grammar alone:
- `īn mār awīlim uḫtabbit … īnšu uḫappadū` "has destroyed the eye of a man's son … they shall put out his eye"
- `eṣemti awīlim ištebir … eṣemtašu išebbirū` "has broken a man's bone … they shall break his bone"
- `šinni awīlim mēḫrišu ittadi … šinnašu inaddû` "has knocked out the tooth of a man of his own rank … they shall knock out his tooth"
- `mār awīlim` "a man's son" (a member of the awīlum class; l "a-man's-son"); `awīlum` "a man" unchanged; `warad awīlim` "a man's slave"; `muškēnim` "of a commoner"
- `rittēšu inakkisū` "they shall cut off his hands" (number UNCERTAIN); `uznašu inakkisū` "they shall cut off his ear"
- `mišil šīmišu išaqqal` "he shall pay half of his price"; `1 mana kaspim išaqqal` "he shall pay one mina of silver" (išaqqal "he shall pay (lit. weigh out)")
- `lēt awīlim … imtaḫaṣ` "has struck the cheek of …" (lētum "cheek", UNCERTAIN); `ša elīšu rabû` "who is greater than he"; `ša kīma šuāti` "who is like himself"
- `ina puḫrim ina qinazi alpim 1 šūši immaḫḫaṣ` "he shall be struck sixty times in the assembly with an ox-hide whip"
- `ina risbatim imtaḫaṣma ṣimmam ištakanšu` "has struck (him) in a brawl and has set a wound on him"; `ina idû lā amḫassu itamma` "shall swear, 'I did not strike him knowingly'"; `asâm ippal` "he shall pay the physician" (A.ZU)
- `ina maḫāṣišu imtūt` "has died from his blow"; `ša libbiša uštaddīši` "has made her lose what is in her womb"; `ana ša libbiša` "for what was in her womb"
- `mārassu idukkū` "they shall kill his daughter"
Spellings: awīlam, ṣimmam, mārassu, amḫassu, uštaddīši, išebbirū, inaddû, qinazi.

## Law numbers and line numbers
Harper's §-headings in col. XXXIV (§206–§214 in this part) are one line behind his running line numerals; I followed the running numerals (the plate's margin numbers 5, 10 … agree) and said so in the §206 note. Law boundaries are Harper's headings; the pencilled §-numbers on the plates agree with them from §196 on (§208 pencilled at XXXIV 20, §209 at 23, §214 at 51).

## For the glosser
New lemmas (not in earlier glossaries): asûm (A.ZU, "physician"), elī ("over, above": elīšu), eṣemtum (NER.PAD.DU "bone"), lētum ("cheek", UNCERTAIN), maḫāṣum-N (immaḫḫaṣ "he shall be struck"), mēḫrum ("equal"), qinazum ("whip", UNCERTAIN), risbatum ("brawl", UNCERTAIN), rittum (UM.ME, "hand(s)", UNCERTAIN), tamûm ("to swear"), uznum ("ear"), šebērum ("to break"), šinnum ("tooth"), šūši (ŠU.ŠI "sixty"), ḫabātum-D (uḫtabbit "has destroyed", UNCERTAIN beyond that), ḫapādum-D (uḫappadū "put out", UNCERTAIN), ṣimmum ("wound").
Broaden (the old entry does not cover this part's use): maḫāṣum (infinitive maḫāṣišu/maḫāṣim; amḫaṣ 1st sg; imtaḫaṣ), nadûm (ittadi/inaddû of a tooth: "knock out"), nakāsum (hands, ear), īnum (īn construct), edûm (infinitive after ina, idû), apālum (asâm ippal "pay the physician"), mâtum (imtūt), nadûm-Š (uštaddīši "made her drop"; the old entry is "strip of"), šīmum (šīmišu "price" of a slave, old entry "purchase price"), šaqālum, alpum (alpim = GU₄ bare, "of an ox"), wardum (warad construct), awīlum (awīlam accusative, awīlim after a construct, mār awīlim), muškēnum (nominative and genitive), mārum/mārtum (mār, mārat construct, mārassu), zinništum, amtum (amat construct), libbum (ša libbiša "what is in her womb"), kaspum, manûm (ma-na in syllables), šiqlum, mišlum, puḫrum, ša, u, lū ("u lū" = "or"), kīma, šuāti, šū, šī (ši alone, XXXIV 41), 1/2 (MAŠ, new numeral reading), 10/5/2/1 (numerals with šiqlum), šumma.

## For QUESTIONS.md
- §195 "hands" vs "hand", and the second sign of UM.ME (rittu): needs an eye on the autograph and Harper's sign list no. 65 beyond my reading.
- Whether to rename the PAD sign gloss if a later reviewer finds a better Unicode match.
- Whether ŠU.ŠI should be glossed "sixty (strokes)" rather than leaving the strokes unwritten.
