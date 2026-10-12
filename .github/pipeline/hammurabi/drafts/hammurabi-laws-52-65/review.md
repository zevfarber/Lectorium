# Review — hammurabi-laws-52-65

## Pass 1

Scope: all 33 units (§52–65), stele XV 1 – XVI 77, checked against Harper's plates XXII–XXVI (PDF 259, 261, 263, 265, 267), his List of Signs (PDF 383, 403, 405, 409), the packet, conventions.md, and the published parts (renderings, lemmas and notation; hammurabi-laws-42-51 as the model). units.json edited in place by script (load → modify → dump, ensure_ascii=False, indent=1). Pre-review copy kept in the reviewer's scratchpad.

### Mechanical checks (all pass)
- Line division: units cover 155 stele lines, XV 1–78 and XVI 1–77, each once and in order. Every unit's col/line is its first line. Every nl flag falls on Harper's line breaks. Harper's raised {b} marks a second sub-row of the same stele line (seen on the plate at XV 15, 41, 65, 68; XVI 11, 12, 32, 36, 47, 72), so the unit correctly has no nl there.
- ln/p: these appear only on the first unit of each of the 14 laws. The inner šumma of §62 (unit 25) correctly has neither.
- `reading` rebuilds from the glyph `tr` for every word. Every multi-sign Sumerogram has its val on the first glyph and "" on the others.
- Sign keys: all are present in signs-cuneiform.json (HAL, U8 = LAHSHU, NAGA, UZ3, BURU14 included). The numerals 20 and 4 use `u` with valid Unicode names.

### Changes made

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 7 (§56) | words[3] ip-te-ma · morph | minor | petûm claimed all 3 glyphs; -ma had g: [] | petûm g [0,1], -ma g [2] |
| 9 (§57) | words[10] im-ta-gar-ma · morph | minor | the same fault (magārum [0–3], -ma []) | magārum [0,1,2], -ma [3] |
| 22 (§61) | words[6] ig-mur-ma · morph | minor | the same fault (gamārum [0–2], -ma []) | gamārum [0,1], -ma [2] |
| 13 (§58) | i-te-li-a-nim · say, gloss; n | minor | `ītelianim` had no length mark on the fem. pl. -ā- before the ventive | say `īteliānim`; gloss and note updated; note's bare form given as ītelia (ītelâ) |
| 13 (§58) | i | style | "the signal that grazing is over" replaced the Akkadian noun (kannū "bands") with an interpretation | "the bands that mark the end of grazing have been hung up at the city gate" |
| 17 (§59) | i | minor | "he shall pay" — the house rendering of išaqqal is "weigh out" (§24 in hammurabi-laws-11-25), and l already says he-shall-weigh-out | "he shall weigh out half a mina of silver." |
| 20 (§60) | n | minor | "ḫamuštum … is the ordinal of ḫamšum 'five'": ḫamšum is itself the ordinal; ḫamuštum is its feminine | "is the feminine of the ordinal ḫamšum, agreeing with šattum" |
| 25 (§62) | l | style | "for the-years" read sense into ša šanātim | "of the-years" |
| 25 (§62) | ša-na-tim · morph lemma | minor | the lemma was `šanātum`, a plural form; the house lemma is the dictionary form | lemma `šattum` (with the published gloss) |
| 28 (§63) | iš-ti-a-at · morph lemma | minor | the lemma was `ištiat`, a feminine form; `ištēn` is already in the published glossary | lemma `ištēn` (with the published gloss) |
| 27 (§63) | n | minor | said Harper's List of Signs gives KI.KAL "which he reads nidûtum". Sign no. 177 (PDF 409) has only the group KI.KAL under KI, with no reading | "read nidûtum as at §44 (Harper's List of Signs enters the group KI.KAL under KI, no. 177; later dictionaries read it kankallum)" |
| 30 (§64) | n | minor | overclaimed: "Harper prints kirûm, but … the verb wants an object". ṣabtu is a stative, which can be intransitive ("the orchard is held") or transitive, so Harper's nominative is grammatical | the note now gives both readings and says we take kirâm as the object of the gardener's holding |
| 32 (§65) | n | minor | XVI 77: "its place is empty on Harper's plate". In fact the plate (PDF 267) ends the column at line 76 and draws no row 77. The note also stated as fact that Harper restored "from the endings of §55 and §62" | now says the plate draws nothing and the column ends at 76; the restored word is "the verb that closes the parallel §55 and §62"; added that the cuneiform shown is Harper's restoration, not a reading of the stone |
| 32 (§65) | i | minor | i showed the restored verb as if it were attested (l had brackets) | "the gardener [shall measure out] …" |
| 1 (§53) | n | style | "restored from the phrases repeated around them" stated Harper's method as fact | "Harper's restorations, supported by the same words repeated in the lines around them" |
| about | — | style | "five columns … were chiselled away" was stated as fact; it is Harper's count (his editorial line after XVI 77) | "After §65 the stele was chiselled smooth in antiquity — five columns by Harper's count;" |

Counts: major 0 · minor 12 · style 4.

### Considered and refused

- **XV 75 `eqel`** (Harper eḳlum): kept. In "rēʾûm eqel ušākilu inaṣṣar" the field is the object of inaṣṣar and the head of an asyndetic relative clause (verb in the subjunctive). That calls for the construct, eqel. The plate shows A.ŠÀ with no complement, so nothing contradicts it. The note explains this honestly.
- **XVI 64 `kirâm`** (Harper kirûm): the say is kept. It is grammatical, and it fits the subject nukaribbum. Only the note's overclaim was fixed (see above).
- **Part name "crops, dikes and orchards"** (plan.md: "Crops, debts and the date-orchard"): accepted. §52–65 has no debt law; the debt laws are §48–51, already published. The name covers §52 (crop), §53–56 (dikes and ditches) and §59–65 (orchards). The grazing laws §57–58 fall under "crops" (damage to the crop). The coordinator should update plan.md.
- **MEŠ written as two glyphs ME + ESH** (unit 4, DUMU A.GÀR{meš}): not changed. Harper's List of Signs no. 185 (PDF 409) has MEŠ as one sign, and Unicode has it as one character: CUNEIFORM SIGN MESH, U+1238C. signs-cuneiform.json has no MESH key, and I may not add signs. The two-glyph spelling looks right on screen and reads correctly as {meš}. → coordinator (see below).
- **§59 ma-na written as syllables (phon)** where §24 has the logogram MA.NA (log): not changed. Harper's transliteration differs at the two places (ma-na here, MA.NA at §24), the base is Harper line by line, and the note states the difference plainly.
- **XVI 51 A.ŠÀ(=a-na)**, with val "ana" on the A glyph and the correction written into the ŠÀ tr: kept. It follows the house precedent for carver's slips, il-lu(=ḳu)-u in §47.
- **XVI 77 drawn as cuneiform at all.** I considered replacing it with a gap word: no copy preserves the line, and the conventions say losses are "shown as gaps, never reconstructed". signs-cuneiform.json has no LACUNA pseudo-sign, and Harper's bracketed restoration is part of the base transliteration, so I kept the signs and made the note and the i say plainly that they are a restoration. → coordinator decision (below).
- **ṣēnī / ṣēnū** (OB plural) vs `ṣēnē` in §35 of hammurabi-laws-26-41: kept the draft's OB forms. The published `ṣēnē` follows Harper's late spelling. That is an inconsistency in the earlier part, and it is reported, not changed.
- **ḳ in tr** (u-ḫal-li-ḳu, iz-ḳu-up, i-li-ḳi, i-ša-ḳal): kept. It is the notation of the latest published parts (26-41 and 42-51 use ḳ).
- **AB.SÍN as AB + SHE(tr SÍN) + NAGA(tr "")**: kept. It follows the precedent of GEME₂ = SAL + KUR(tr ""). On the plate the second sign is partly outlined: a star-like head plus a cross-hatched outline. The note and the NAGA sign entry both say the identification is uncertain.
- **½ as MAŠ**: kept. On the plate it is a horizontal crossed by a vertical, and the note says the identification is ours.
- **Verbatim-overlap check.** I checked against the modern renderings I recognise, without opening any of them. The only shared wording is forced by the Akkadian structure: "grain or sesame in the field … change his contract" in §52, and "the man in whose dike the breach opened shall replace the grain" in §53, which is awīlum ša ina kārišu pītum ippetû šeʾam … iriab and uses the house verb "replace" from §23. There is no distinctive borrowed phrase. I made one rewording for other reasons: §58 "the bands that mark the end of grazing". The renderings of šumma awīlum ("If a man"), imaddad ("measure out") and bēl eqlim ("the owner of the field") match the house.
- **Everything else**: I checked each sign of every line on the plates. The logograms A.ŠÀ, ŠE (with -am only at XV 2), A.GÀR, KAR, KÙ.BABBAR, DUMU…MEŠ, SIPA (PA.LU), U₈.UDU.ḪI.A, KÁ.GAL, BURU₁₄, GAN₂.E, ŠE.GUR, {giš}KIRI₆, NU.{giš}KIRI₆, MU 4{kam}, ḪA.LA, GÚN, AB.SÍN and KI.KAL all stand where the draft has them. The numerals match: 10, 20 (two U), 60 (one vertical), ½. So do the outlined restorations in XV 8–14 and the ḪAL sign in XV 19 (Harper's no. 2, the crossed form, not ḪAR no. 159). The notes' sign-list references are right (no. 2 ḫal, 147 kar/kâru, 185 meš, 190 SÍG with ṣênê spelled U₈.UDU.ḪI.A) and so are the cross-references (§28 ileʾʾi, §29 urabbāšu and the third, §42 e-bi-ši-im, §44 KI.KAL and aḫšu iddi, §45 GÚN, §47 riksātum and the carver's slip, §49 uštabši and eqel epšētim). Every grammatical label in the notes was checked against the form; apart from the fixes above, they are correct.

### For the coordinator
1. **Earlier part, real error — ḫal written with the HAR key (hammurabi-laws-1-10 §9 and hammurabi-laws-11-25).** The drafter's remark is correct. Six glyphs have tr "ḫal" with sign HAR: in 1-10 unit 19 (ḫal-qu, ḫal-ga-am), and in 11-25 units 6, 8, 14, 15 (ḫal-qa₂-am). Harper's List of Signs gives ḫal only under no. 2, the crossed ḪAL form; no. 159 is ḫar, mur. On plate X (PDF 235), VII 1b ḫal-qu clearly shows the crossed ḪAL sign. All six should be sign HAL (CUNEIFORM SIGN HAL, now in signs-cuneiform.json). I did not edit them.
2. **Earlier part, real error — the flock in §35 (hammurabi-laws-26-41 unit 15).** The drafter's remark is correct. On plate XVIII (PDF 251), XI 67 reads Ù · U₈ · UDU · ḪI · A, five signs, the same U₈ form as XV 48/52/58/65/71/73. The published word is "UDU{ḫi.a}" = LU HI A, which leaves out U₈. It should be U₈.UDU{ḫi.a} (U8 + LU + HI + A), and the note "ṣênê is the flock-word over the sheep-sign LU" needs adjusting. I did not edit it.
3. **MESH sign**: please add `MESH` → 'CUNEIFORM SIGN MESH' (U+1238C; Harper no. 185) to signs-cuneiform.json. Then in unit 4 the {meš} glyphs ME + ESH (det) can become one glyph MESH (det).
4. **XVI 77**: decide whether a line with no surviving signs (Harper's plate stops at 76) should show Harper's restored cuneiform, as it does now, or a LACUNA gap unit word. The second option needs the LACUNA pseudo-sign from runbook.md.
5. **plan.md**: rename the part to "crops, dikes and orchards" (no debt laws in §52–65).
6. **Minor, published 42-51 §44 note**: it says Harper's sign list gives KI.KAL "as nidûtum". Sign no. 177 shows only the group, so the reading must come from elsewhere in Harper (his glossary or translation). Low priority.

## Pass 2

Scope: gloss.json (38 new entries and 25 `__broaden__` entries as delivered), checked against units.json (every form cited must occur in this part's `say`) and against the merged published glossary as the build computes it (`r3lib.merged_inline_glossary`, parts in reading order, later parts overriding). Also a re-check of units.json after the coordinator renamed ṣēnum to ṣēnū, and a further read of every l/i/n. Edits were made by script. Pre-pass copies of both files are in the reviewer's scratchpad.

Note on the build: `cun.fill_words` takes a word's tap-gloss from its own `morph.gloss` in units.json first, and uses the glossary only as a fallback. Per-word glosses in units.json are therefore reader-facing, and I checked them too.

### Changes made

| unit / entry | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| gloss `__broaden__`: ina, -šu, ana, wabālum, bēlum, nadānum, elûm, libbum, šakānum | value | major | Nine broaden values did not start with the published entry the build actually merges. The glosser had prefixed a different part's text (e.g. the litany or prologue `ina` "in, within", or elûm without the §35 "forfeit" sense that 26-41 published). The build replaces the whole entry with the broaden value, so §35's elûm sense, the 42-51 bēlum text, and others would have been lost from the glossary | Every broaden is rebuilt as the merged published entry, exactly, + " · " + addition. All 28 verified by script |
| gloss `__broaden__`: eqlum, petûm, balum, šattum, rabûm-D, târum-D, kaspum, manûm, šaqālum, gamārum, ezēbum, nadānum-N, epēšum, adi, ṣabātum, biltum, enûm | value | style | Many additions restated the base meaning (manûm repeated the whole mina definition; šaqālum, gamārum, ezēbum, epēšum, ṣabātum, biltum, libbum, šakānum and nadānum-N restated "to weigh out / to finish / to leave / …") | Additions cut down to the new forms or sense only, e.g. manûm "· spelled in syllables, ma-na, at §59 …", šaqālum "· išaqqal (present) “he shall weigh out”" (the house verb) |
| gloss `__broaden__` šattum | value | minor | Did not cover the syllabic plural šanātim (ša-na-tim, XVI 39), now that šanātum is folded into šattum | "· šattim (genitive); plural šanātim “years” (ša šanātim “of the years”); MU 4{kam}, said erbe šanātim “four years”" |
| gloss `__broaden__` adi, ṣabātum | value | minor | ṣabtu was labelled "(stative, 3rd person) “he holds”" without its subjunctive, and the alternative reading was hidden | Labelled the stative with the subjunctive -u after adi; ṣabātum also gives Harper's reading ("as long as the orchard is held") |
| gloss `__broaden__` (added) mārum, šuāti, nadûm | value | minor | The published mārum entry is "son (DUMU) — here: a minor, not yet able to sell", which is wrong for mārū ugārim. šuāti ("that, the aforesaid") does not cover its use as the pronoun "him". nadûm did not cover turning a flock loose | Broadens added: mārum "member of a group: mārū ugārim …"; šuāti "as the independent pronoun “him” …"; nadûm "of a flock: ṣēnī ana eqlim iddi …" |
| gloss rakābum-D (+ units unit 31 per-word gloss) | value | major | "urakkibma (present, with -ma) “he shall pollinate”" was wrong. lā urakkibma (XVI 72) is the D preterite in a protasis, "he did not pollinate"; the D present would be urakkab | Corrected to "urakkib(ma) (preterite): lā urakkib “he did not pollinate”". The unit 31 and 29 per-word glosses now use the same text |
| gloss akālum-Š | value | minor | "ušākilu … “(whom) he grazed”" misread both clauses: §57 has rēʾûm ša … ušākilu, "(the shepherd) who grazed"; §58 has eqel ušākilu, "the field he grazed". uštākil was glossed "he has fed" | "ušākilu (preterite, subjunctive -u) “(who) grazed; (the field) he grazed”", and uštākil "he has grazed (the sheep on the field)" |
| gloss ištu | value | minor | It cited ītelianim. Since pass 1 the `say` is īteliānim, so the cited form no longer occurred in the part | Now cites īteliānim |
| gloss nukaribbum, absinnum | value | minor | The honesty caveats in the notes were missing from the glossary: nukaribbum is a later-study reading (Harper NU.kirû), and the reading of AB.SÍN's second sign is uncertain | Short parentheses added to both |
| units: 6 ṣēnū words (units 9, 10, 12, 13, 14) | morph gloss; U8 glyph val | minor | After the lemma rename, the per-word gloss was still the §35 text "ṣēnē over the sheep-sign LU", which is wrong here because the writing is U₈.UDU{ḫi.a}. The glyph val was still ṣēnum | The per-word gloss is now the gloss.json ṣēnū entry, and val is "ṣēnū" |

Counts (pass 2): major 2 · minor 7 · style 1.

### Checked and refused (no change)
- **New entries checked and correct as they stand:** kārum, danānum-D, pītum, petûm-N (ittepti perfect; ippetû preterite with subjunctive), ugārum, wabālum-Š (uštābil perfect), ḫalāqum-D, bīšum, atappum, šiqītum, šammū, magārum (imtagar perfect), eṣēdum (iṣṣid present), elēnumma, 20, 60, kannum (?), gamartum, ḫalālum-N (? and the inference is stated), naṣārum, iṣum, nakāsum, 1/2 (mišil marked ?), zaqāpum, 4-kam, ḫamuštum (feminine ordinal), mitḫāriš, zittum, nasāqum, nidītum, nadûm-N (innadû preterite with subjunctive), šittān (šittīn oblique), maṭûm-D (umtaṭṭi perfect), ṣēnū. Every form these entries cite occurs in this part's `say`, and every grammatical label is right.
- **ištēn:** its published entry, "one: šattam ištiatma “one year only”", already cites the feminine ištiat, so no broaden is needed.
- **Coverage:** every lemma used in units.json now has a published entry or a gloss.json entry, and no gloss.json entry is unused.
- **l/i/n:** a full re-read of units.json after the lemma change found nothing further. The notes' "ṣēnū is a feminine plural" (§57/§58) now agrees with the lemma.

### For the coordinator
1. **ṣēnum / ṣēnū split:** in the merged glossary the build uses, `ṣēnum` is not the prologue's "evil". hammurabi-laws-26-41, which comes later in reading order, overrides it with "sheep, the flock: ṣēnē over the sheep-sign LU". The same word for "flock" will therefore sit under two lemmas: ṣēnum in §35, ṣēnū here. Your rename is kept. For QUESTIONS.md: when §35 is corrected (it is missing U₈, see Pass 1), move it to ṣēnū as well. The prologue's "evil" homonym also deserves its own key.
2. **The broaden mechanism is fragile:** the glosser's base text came from a different part than the one the merge keeps. Future glossers should copy the base from `merged_inline_glossary`, not from any one published file.
