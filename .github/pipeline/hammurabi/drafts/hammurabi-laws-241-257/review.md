# Review — hammurabi-laws-241-257

## Pass 1

Reviewer: strongest model, adversarial. Inputs: conventions.md, runbook.md (Reviewer), ../run3/RUNBOOK.md §2, packet.md, units.json, the published parts 215–240, 195–214, 185–194 and the other published parts' glossaries (for house renderings), Harper's plates 63–68 (PDF 341–351) and his List of Signs (nos. 5, 25, 48, 50, 54, 61, 65, 68, 79, 80, 91, 109, 129, 150, 158, 162, 169, 170, 172 looked up). No modern translation opened or recalled as a source; Delitzsch / Muss-Arnolt were not open in this pass (decisions on zu-ga-am and the unread words rest on grammar and on Harper's own List of Signs). Backup of the original units.json is outside the repo (scratchpad `rev/units.orig.json`). Edits were made in place by the script `scratchpad/rev/patch1.py` (it applies the changes below to the drafter's file and writes `rev/log1.json`); no sign was added; `signs.py check` says "in sync". `r3.py build` was run only to see errors: the only errors left are the missing-gloss ones (28 lemmas, the glosser's job).

### How the plate check was done (and its limit)

Plate map: Plate 63 (PDF 341) ends with XXXVI 81; Plate 65 (PDF 345) = XXXVI 82–91 and XXXVII 1–38; Plate 66 (347) = XXXVII 39–84; Plate 67 (349) = XXXVII 85–101 and XXXVIII 1–6 (the packet's plate list is one off at the start: XXXVI 81 is on PDF 343, not 341; 343 holds XXXVI 38–81). Row boundaries were found by script, then each row cut out at zoom 6–9.

What I did: counted sign-groups row by row and compared them with the glyph sequence for XXXVI 82, 84, 86, 87, 89; XXXVII 1–2, 4–5, 7, 11, 15, 19–20, 23, 24–25, 29, 31–32, 34, 37, 44, 47, 52–54, 60–61, 64, 67, 82, 86, 96–99; XXXVIII 1 and 3. Compared Harper's List of Signs entries with the plate for every unusual logogram: Á (129) at XXXVI 87 and 89; ANŠE (91) at XXXVII 2 (one sign: box + triangle); SU "flesh" (80) at XXXVII 32; NER (170), IGI (172), UM.ME "rittu" (65), DUMU "mâru" (70), ŠÀ.GAL (150), AK.ŠU (48), SA/pasuttu (50), GUD.DA.UR.RA / GUD.LID.UD.SAG (109), AM (79: the GUD shape with a cross in the triangle), IB "ib, ip" (186), GAN.E (51), ŠE.GUR (142), MU (25: box-and-cross sign, its second form carries a small ⟨ tail). Checked every alpam/alpim/alpum: GU₄ + AM (a compact AM beside GU₄) at XXXVII 2 and 11 (first alpam) and 19 (first alpam); GU₄ + um at XXXVII 44 (alpum) and 60; GU₄ alone at XXXVI 82 and XXXVII 7, 12, 15, 20, 23, 29, 37, 52 and the second alpim of 11 and 19 — all as the drafter has them. Checked the line order LID/GUD at XXXVII 99: the plate has LID, GUD, ZUN (Harper prints GUD.LID.ZUN) — the drafter's order is right.
What I did NOT do: identify every wedge of every syllabogram independently of Harper. The syllabic words were checked at sign-group level (count and place of the clusters), and the specific words the lead listed were each looked at: zu-ga-am (ZU, GA, AM — the last sign is the triangle with the cross: AM), ik-ki-ib-ma (four signs: IG, KI, IB, MA; the plate IB is Harper's ib/ip), ba-ab-ta-šu (four groups), ip-ki-zum (only the layout of the two-tier row), bi-ḫa-zu (five groups), id-du-uk-šu (six signs: UR, MAḪ, Á, DU, UG, ŠU), UR.MAḪ (two signs, UR and MAḪ), AK.ŠU (AK, one small flared vertical for ŠU, i, GUR). The line division was checked by script: every unit's `nl` breaks give exactly Harper's lines (the one apparent difference, XXXVIII 3 "{kam}", is the superscript counted as a word in the packet).

Mechanical checks (script): every `reading` reconstructs from the glyph `tr` values; all morph indices valid; no ḳ in any field; `ln` and `p` stand on the first unit of each of §241–§257 and nowhere else (17 laws, 17 pairs); unit start lines agree with packet.md; sign keys all resolve (the build passes the sign check).

### Changes made

Unit numbers are 0-based positions in `sentences` (with col line and law in brackets).

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 2 (XXXVI 85–86, §242) | words[3], n | **high** | šattim was MU + TIM (complement). On the plate (XXXVI 86) MU is followed directly by the single vertical wedge (the numeral 1), then i and GUR: no TIM. The note even counted "two signs, not three" to support it | MU alone (log, val šattim), as the published `MU 3{kam}`; note rewritten |
| 37 (XXXVIII 2–3, §257) | words[3], n | **high** | same: `MU-tim`; the plate (XXXVIII 3) is i, na, MU, the vertical 1, KAM | MU alone; note rewritten |
| 1, 12, 14, 23, 24 (§241, 247, 248, 251, 252) | words, n | medium | KÙ.BABBAR-i / KÙ.BABBAR-im with a complement sign. The rows at XXXVI 84, XXXVII 25, 34, 64, 67 show KÙ and BABBAR and nothing after (counted at zoom 8–9: 5 groups at 64 and 67, 7 at 34, 8 at 84). This is also what the earlier parts found (215–240: "numeral + GÍN + KÙ + BABBAR with nothing after"; Harper's kaspim / kaspi is his normalization) | bare KÙ.BABBAR, `say` kept (kaspim, kaspi), val moved to KÙ as in the published parts; three notes corrected |
| 4 (XXXVI 89, §243) | words[1], l, n | medium | the compound was GU₄.UD.LID.SAG (Harper's transliteration). On the plate the diamond (LID) follows GU₄ and UD is third; Harper's own List of Signs (no. 109) prints GUD.LID.UD.SAG. The note also said the verb "finishes both" §242 and §243 | glyph order, reading, `say`, lemma, l and note: GU₄.LID.UD.SAG; note says Harper's transliteration differs from his list and the plate; the verb statement hedged |
| 13 (XXXVII 32, §248) | words[11], n | medium | `ZU.SA-šu`: wrong signs, wrong order, and a note saying the plate has "two clusters" keyed by shape. Harper's List of Signs no. 50 prints pasuttu as SA + a second sign; the plate row (SU, then SA, then a small diamond-in-triangle with a long tail, then šu) agrees. ZU is not there | `SA.x-šu`: SA (log), x (second sign unidentified; key UL only as the nearest shape; tr "x"), šu; note rewritten; word stays UNCERTAIN |
| 13 | l, i, n | medium | ittasak glossed "torn out" / "throw, tear out": nasākum is "to throw, cast"; "torn out" is a guess the l presented as the word | l "has-thrown(?)"; i "torn off (?)"; note says "tear off" is a guess |
| 26 (XXXVII 74, §253) | n | medium | `iqīpšu` called the "perfect" of qiāpum; iqīp-šu is a preterite (a perfect would be iqtīp) | "preterite" |
| 30 (XXXVII 85, §254) | n | medium | `utenniš` called the D-stem "perfect"; it is the D preterite (perfect: uttenniš) | "preterite" |
| 10 (XXXVII 19, §246) | n | medium | "a hurt foot or neck": "neck" for labiānu is established nowhere (the word is unread) | "labiānu" |
| 17 (XXXVII 44–47, §250) | n | medium | zu-ga-am: the note said the signs "also read su-qa₂-am" as if ZU = su were a plain value. Decided from grammar: an accusative -am, then ina alākišu, so a word for the way the ox went; zu = su (z for s) + ga = qa₂ gives sūqam "street", the only word I can build, but the z-spelling is not confirmed; a zuq- word (zuqtum "peak") would show a t, which is not written | sūqam kept, marked UNCERTAIN, the assumption (z for s) and the rejected alternative stated in the note; l/i unchanged ("the-street(?)", "(?)") |
| 4 | words[2] | low | `3` said šalāš before a masculine noun (kur) while the same law's 4 is erbet: Akkadian 3–10 take the opposite gender's form (šalāšat with kur). The published 215–240 says šalāš before šiqil, a house inconsistency | said šalāšat (?); see QUESTIONS |
| 3 (XXXVI 87) | n, l, i | low | note: the compound has "five signs" and "the plate shows one more cluster in this row than Harper's five": there are four signs after Á and the plate row has exactly Harper's five groups (Á, GUD, DA, UR, RA). l "of-the-GU₄…" put an article in; i "which I cannot read" inside the English | note, l, i rewritten ("?", "unread") |
| 0 (XXXVI 81, §241) | l, i | low | l "for hostage-taking" invented a noun; i "seized … as a pledge" where the house word for ittebi is "distrained" (§114–115) | l "as-a-hostage"; i "has distrained an ox as a hostage (a pledge for debt)" |
| 2 | i | low | "(an animal)" stated an inference | "(an animal?)" |
| 4 | i | low | "which I cannot read" inside i | "(another kind of hired ox?; unread)" |
| 5 (XXXVII 1–4, §244) | n | low | tense of iddūkšu not stated | "as read, the preterite of dâkum + -šu" |
| 6 (XXXVII 5) | i | low | "the loss is its owner's alone" sits close to a remembered idiom; the text is only "to its owner only" | "the loss is for its owner alone"; note still says "the loss" is supplied |
| 8, 10 (§245, §246) | i | low | "he shall give … an ox like the ox" dropped iriab "he shall replace" (house: riābum "to replace") | "he shall replace the ox for its owner with an ox like it" |
| 9 (XXXVII 14–18, §246) | l, i, n | low | šēpīšu is a plural/dual form (cf. qarnīšu "horns") but l and i said "its foot" | l "its-feet"; i "foot (or feet)"; note states the form and that the number is UNCERTAIN |
| 15 (§249) | n | low | "lightning or sudden death" was a guess | "a death with no human cause" |
| 19 (XXXVII 52–53, §251) | n | low | did not say that the spelling at XXXVII 53 has A where the next line has PU (na-ak-ka-a… / na-ak-ka-pu-u), which makes nakkāpamma shakier | added |
| 20 (XXXVII 54, §251) | i, n | low | i "fault" is neither Harper's "loss, defects" nor the glossary's babtum; note did not give the tense of ušēdišumma or mark "kīma nakkapû" as uncertain | i "defect (?)"; note: Š preterite, no subject named, "kīma nakkapû" UNCERTAIN |
| 23 (§251) | n | low | "no one is named to receive it" said twice | once |
| 27 (XXXVII 75, §253) | l | low | l "he-has-put-in-his-charge" is a paraphrase of ipqissum (paqādum) | l "he-has-committed-to-him" |
| 31 (XXXVII 86, §254) | l, i, n | low | "restore" / "make good" for iriab; the house word is "replace" (riābum) | "replace" throughout |
| 32 (XXXVII 88–90, §255) | l | low | l "he-has-hired-out" is the sense of ittadin, not the word | l "he-has-given" (i keeps "hired out") |
| 33 (§255) | i | low | "for every ten bur" put a supplied word in as if written (the plate has no ana here; §58 etc. write ana 10 GAN.E) | "(for) every ten bur" |
| 25 (§253) | n | low | "ana pāni X izuzzum = to attend to X" stated as a known idiom | "literally 'to stand before his field', taken as 'to be in charge of it': a reading from the sense, UNCERTAIN" |
| 36 (§257) | n | low | — | added that Harper lists AK.ŠU under AK (his sign no. 48) |
| 37 | words[4] | low | lemma `1` for 1{kam}; the published `MU 3{kam}` uses `3-kam` | lemma `1-kam` |
| 9, 21, 26, 30, 31, 35 | morph lemma | low | lemmas that invent a root or a nominative from one form: šarāmum, mašārum, tânum, aldāʾum, labiānum (house practice in 215–240: form-lemma, as `izzapar`, `idāṣ`, `ibbûm`) | ušarrim, imtanaššar, tâna, aldāʾam, labiān |
| about | about | low | "dragged about the field by the cattle" (ina liātim is "with/by"; the unit says "with") | "with the cattle" |

Counts: 33 findings — high 2, medium 8, low 23 (59 field edits; the KÙ.BABBAR finding touches five units, the MU finding two).

### Findings considered and refused (no change)

- **GU₄-am at XXXVII 2, 11, 19 (the small ornate sign after GU₄).** The drafter's AM stands: the row has one more sign-group than GU₄ alone would give, and the group is the compact AM (the GUD shape with a cross in the triangle, Harper no. 79; the same sign closes zu-ga-am at XXXVII 44 and na-ak-ka-a[m] at 53). Not changed.
- **ANŠE alone at XXXVII 2.** Harper's no. 91 is one sign (box + triangle); no -am follows on the plate. Not changed.
- **NER, IGI, DUMU, UM.ME, SU, ŠÀ.GAL, AK.ŠU, Á, UR.MAḪ, GUD.DA.UR.RA.** Each agrees with Harper's List of Signs and the plate (see above). Not changed (the only corrections are the ones in the table: the drafter's GUD.DA.UR.RA is right; its note was wrong about an extra cluster).
- **ik-ki-ib-ma: keep tr ib, say ikkipma.** IB carries both ib and ip (Harper no. 186); the reading line keeps Harper's ib and the `say` gives the verb nakāpum (the litany has munakkip). Not changed.
- **iddūkšu (XXXVII 4).** Six signs, preterite + -šu is the best reading; the doubled d stays unexplained. Not changed, UNCERTAIN as flagged.
- **ana bēlišuma = "only/alone" (§244).** The emphatic -ma is the best parse. Not changed (only the English `i` was made plainer).
- **babtum / ušēdišumma (§251).** Both readings are in the note; kept. The glossary entry for babtum (141–152) is already hedged.
- **aldāʾum, tâna, labiānu, pasuttu, ŠÀ.GAL, AK.ŠU, pīḫassu, imtanaššarūšu.** Kept unread / uncertain as the drafter has them; I cannot do better from the grammar. The `i` carries "(?)" in each.
- **ittasak = "nasākum" (not nasāqum).** Kept; the note says AK could also be aq.
- **Numerals `ištēt` for 1 with šattum, `samānat` for 8, `ešret` before būrim.** Spoken forms reconstructed (?), as in the published parts. Not changed (but see QUESTIONS for šalāš / šalāšat).
- **Numerals as role `num` against the published `log`.** The build accepts `num`; not changed.
- **The wording of the hired-ox and field-steward laws against remembered English.** §242–243 (hire by name, "to its owner"), §245–246 and §253–256 were checked sentence by sentence against the grammar; no phrase recalled as a published translation was found. The nearest to a remembered idiom (§244 "the loss is its owner's alone") was changed above; "(for) every ten bur" is forced by the numbers (the rate of §58). The §253–255 renderings ("to take charge of", "has bound him to cultivate", "has weakened the cattle", "they shall convict that man") are built from stand-before / rakāsum-D / enēšum-D / kânum-D and flagged where they rest on a guess.

### For the glosser (pass 2 will check)

New lemmas: GU₄.DA.UR.RA, GU₄.LID.UD.SAG, nēšum, mēgūtum, šēpum, labiān, qarnum, zibbatum, pasuttum (SA + x: say so), nasākum, sūqum (UNCERTAIN), nakkāpum, edûm-Š, ušarrim, sanāqum, aldāʾam, ŠÀ.GAL, enēšum-D, tâna, pīḫatum (UNCERTAIN), imtanaššar, AK.ŠU, the numerals 4 and 8, `1-kam`. Broaden: kaspum (the house entry already covers bare KÙ.BABBAR), šattum (MU alone), 3 (šalāšat before a masculine noun).

### Open for pass 2

- Re-read the notes of units 13, 17, 20 after the glosser's entries (pasuttum, sūqum, babtum).
- Decide, once glosses exist, whether `x` (unidentified second sign of pasuttu) should become a real sign key.

## Pass 2

Reviewer: strongest model, adversarial. Inputs: conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md, units.json (after pass 1), gloss.json, review.md (pass 1), the published parts' glossaries (latest holder of every `__broaden__` key found by script over the 19 published parts) and the published sentences of 100-111, 215-240 (consistency of sign keys, `say` and lemma per reading, compared by script: every difference listed in this part is a deliberate one, see below). Plates 65, 66, 67 (PDF 345, 347, 349) re-rendered at zoom 3–14; Harper's List of Signs nos. 48, 49, 50 (PDF 389). No modern translation opened. Patch script: scratchpad `p2/patch2.py` (originals saved as `p2/units.p2orig.json`, `p2/gloss.p2orig.json`). `build` succeeds; `validate` prints PASS; `signs.py check` says "in sync"; no sign added.

### (A) Pass-1 edits re-verified on the plates

- MU alone at XXXVI 86 (šattim, then the one vertical wedge, then i, gur) and at XXXVIII 3 (i, na, MU, the wedge, KAM): confirmed, no TIM.
- Bare KÙ.BABBAR: the silver rows read as KÙ + BABBAR with no following sign wherever looked at again (XXXVI 84, XXXVII 25, 34); consistent with the 195-214 / 215-240 finding. Not changed.
- GU₄.LID.UD.SAG at XXXVI 89 (diamond second): confirmed; GU₄.DA.UR.RA at XXXVI 87: five groups as Harper.
- XXXVII 32 (pasuttu): NOT confirmed, see the first row of the table.
- Row 33 (it-ta-sa-ak) shows the corner sign as `sa` and the fan-with-tail as `ak` (Harper's List nos. 50 and 48), which is how the unit has it.
- Not looked at again, pass 1 stands: the syllabic rows pass 1 listed (counted by group, not wedge by wedge); XXXVII 64 and 67 (the plate rows are crowded; accepted from pass 1's counts at zoom 8–9).
- Label/consistency check against the published parts (script, reading by reading): same glyph keys and `say` everywhere except (a) the numerals 1, 3, 10, 60 written role `num` where 112-126 has `num` and 195-240 have `log` (the build accepts both); (b) `3` said šalāšat where 215-240 says šalāš (below); (c) Á with val `idi` where 112-126 has `idum` (all later parts use idi); (d) `alap` / `eqelšu` vs `eqlišu`, `qātišu` vs `qātīšu` (different forms, correctly different). `ūtaššar` is rendered "go free" in `i` as in §103 of 100-111 and "he-shall-be-released" in `l` as in 215-240; the note names it Dt of wašārum. Fine.

### (B) Changes

| unit / entry | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 13 (XXXVII 32, §248) | words[11] glyphs, reading, n | medium | pass 1 put the glyphs in the order SA, x. The plate row (zoom 12) reads: ù, lu, SU, a triangle with a small diamond and a tail wedge, the three-line corner sign (= SA, Harper no. 50, the same shape as `sa` in the next row), šu. Harper's List prints the compound as SA then the triangle sign, but the plate decides | glyphs reordered x, SA, šu; tr of the unknown sign `X` (CAPS, so the validator no longer WARNs about "x"); reading `X.SA-šu`; note says the plate and the List differ in order and that the order is unsettled; gloss `pasuttum` says the triangle sign comes first on the plate |
| 18 (§250) | n | medium | "īšu … with the relative-subjunctive -u, here at the end of a clause": wrong label. `ul īšu` is a main clause; īšu is the plain "he has" (subjunctive would be īšû) | note rewritten |
| 5 (§244) | n; gloss dâkum | medium | iddūkšu called a preterite with "the doubled d unexplained" (UNCERTAIN). The doubled d is explained by the perfect: -ta- infix after the root's d, middle ʾ contracted (iddūk), and the perfect is the protasis tense of the whole part (ittebi, ištebir, uḫtabbit …) | read as perfect + -šu, still marked UNCERTAIN in form; the idukkū comparison kept; gloss entry `dâkum` (broaden) changed the same way |
| 21 (§251) | n; gloss ušarrim, sanāqum | medium | the note and entry presented a verb "šarāmum" "to cut back, trim" as a lexical fact (pass 1 had already removed it from the lemma only); "dictionary sense" for sanāqum, though no dictionary was open in either pass | "a verb whose root I cannot fix"; the sense is from the context alone; "dictionary" removed; "(šarāmum?)" in the note → "(ušarrim?)" |
| 31 (§254) | n; gloss marārum | low | imrirū "preterite plural with the relative -u": the plural -ū IS the subjunctive here, and a preterite beside present imarrar would be imrurū, not imrirū | note and broaden text say so; still UNCERTAIN |
| 26, 30, about | l, i, n, about | low | `aldāʾum` (a nominative nobody has seen) used as the English word although the form on the stele is accusative aldāʾam and the lemma is aldāʾam | `aldāʾam` throughout (units 26, 30, about) |
| about | about | low | "must give an ox like the ox": the house verb for iriab is "replace" | "must replace the ox with an ox like it" |
| gloss labiān | text | low | "a part of an ox" stated as fact, "its labiānu" (invented nominative) | "probably a part of the animal (it stands beside the foot), only the context"; "its labiān-" |
| gloss qarnum | text | low | "qarnum as a body part of an animal" (empty) | cut |
| gloss pasuttum | text | low | "SA + a second sign", "of its pasuttu" | two signs described (corner sign SA, triangle sign unidentified, triangle first on the plate); "its pasuttu" |
| gloss imtanaššar | text | low | "a Gtn present of a verb mašārum (?)" presented the root as known | "a verb whose root I take as mašārum, a guess" |
| gloss 1-kam | text | low | KAM called "a complement"; the glyph is the raised {kam} (role det) | "followed by the sign KAM, written raised" |
| gloss aldāʾam | text | low | said "aldāʾum … left as aldāʾum" | "aldāʾam … left unread" |
| gloss `__broaden__` ina | text | low | `ina liātim` "with (or by) the cattle" (§256) is not covered by the published entry | broadened: base (from 215-240) + " · “with, by”, of company or means (UNCERTAIN): ina liātim …" |

Counts: 17 findings (units 6 + gloss 11; some touch both): high 0, medium 4 (units 13, 18, 5, 21) plus 2 gloss counterparts of those (dâkum, ušarrim), low 11.

### (B) Every gloss entry checked

New lemmas (28 incl. numerals): GU₄.DA.UR.RA, 4, GU₄.LID.UD.SAG, nēšum, mēgūtum, šēpum, qarnum, zibbatum, nasākum, sūqum, nakkāpum, edûm-Š, ŠÀ.GAL, enēšum-D, tâna, AK.ŠU, 8, 1-kam — kept as written (Sumerograms stated as unread; each UNCERTAIN word carries the flag; no modern form invented that I could find; enšum is in the prologue glossary); changed as in the table: labiān, pasuttum, ušarrim, sanāqum, aldāʾam, imtanaššar, pīḫatum (kept, "root not clear" stays), 1-kam. nēšum: "labbum is also lion" is hedged ("the signs do not choose"). sūqum: kept with the z-for-s caveat. mēgūtum, zibbatum: ordinary words, readings from the form, kept.

`__broaden__` (27 keys): every old entry is whole at the start (script check: all 27 begin with the latest holder's text + " · ", holder found by publication order: 215-240 for alpum, idum, agārum, dâkum, maḫāṣum, nakāsum, 1, 3, -šum, lū, bēlum, kaspum; 195-214 for šebērum, apālum; 185-194 for pānum, izuzzum, qātum, eqlum; litany for nakāpum, šīrum, zērum; 100-111 qiāpum; 170-177 paqādum; 42-51 erēšum, marārum; 141-152 rakāsum-D; 11-25 šarāqum). Each new reading checked against the unit it serves: alpum, idum, agārum, nakāpum, maḫāṣum, nakāsum, šebērum, šīrum, 1, 3, -šum, lū, pānum, izuzzum, qiāpum, paqādum, erēšum, rakāsum-D, šarāqum, qātum, zērum, eqlum, bēlum, kaspum, apālum: correct and not over-claimed. Changed: dâkum, marārum (table). Added: ina. The entry `3` says šalāšat (?) before a masculine noun: right (see QUESTIONS). Entries for lemmas not broadened but used with a new form (šattum with MU alone, nibūtum, ilum, babtum, ṣērum, wašārum) were read against the text and cover it.

### Findings considered and refused

- **šalāš (215-240) vs šalāšat (here).** Kept šalāšat: 3–10 take the opposite gender's form, ešret / erbet / samānat in this part follow the same rule; 215-240 has šalāš before šiqil (masculine) which is the odd one (published, not touched). QUESTIONS.
- **ūtaššar.** Already the house form ("be released" / "go free" as §103); nothing to change.
- **GU₄ + AM (units 5, 8, 10).** Plate and pass 1 agree; not changed. **ANŠE alone**, **NER**, **IGI**, **UM.ME**, **DUMU as TUR key** (as published): not changed.
- **zu-ga-am = sūqam.** Kept UNCERTAIN as pass 1 left it.
- **ina eqlim šuāti, imaddad, ukannūšuma, uštabši, ittadin, uštamīt, imtūt, ištebir, ittakis, uḫtabbit:** tense labels checked against the forms (perfect: -ta- infix), all right.
- **numerals as role `num`.** Build accepts it; not changed.
- **ŠÀ.GAL "fodder (?)", pīḫassu "what he owes (?)", tâna, aldāʾam, AK.ŠU:** already flagged and hedged in `i`; left.

### For QUESTIONS.md

- 241-257: pasuttu (XXXVII 32) read X.SA on the plate order, Harper's List prints SA first; the triangle sign is keyed UL only as nearest. šalāš (215-240, šalāš šiqil kaspim) vs šalāšat/erbet/samānat (here): gender-opposite numerals; 215-240 is the odd one out. iddūkšu now read as perfect. Unread/uncertain: GU₄.DA.UR.RA, GU₄.LID.UD.SAG, labiān, aldāʾam, tâna, pīḫatum, ŠÀ.GAL, AK.ŠU, ušarrim, usanniq, imtanaššar, zu-ga-am, ittasak. Plate checks in this part were by group count and shape for syllabic rows; the pass-1 list stands.
