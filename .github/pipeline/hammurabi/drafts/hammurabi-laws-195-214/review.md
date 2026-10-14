# Review — hammurabi-laws-195-214

## Pass 1

Reviewer: strongest model, adversarial. Inputs: RUNBOOK §2, runbook.md, conventions.md, packet.md, drafter-notes.md, units.json, the five published-part glossaries/units (consistency), Harper's autograph plates 56–60 (PDF 327, 329, 331, 333, 335) and his List of Signs (PDF 383–411). Original units.json is backed up outside the repo (scratchpad `rev/units.orig.json`). Edits were made in place by script; every changed field is listed below.

### How the plate check was done (and its limit)

I cut every stele line of this part out of the plates (rows located from the printed rules and checked against Harper's margin numerals 5, 10 … 95 and the pencilled § numbers 195–214) and read them at zoom 6–7: all 107 lines, XXXIII 41–93 and XXXIV 1–54. Method:

1. Row mapping: every one of the 107 rows is the line the unit says (confirmed by the repeated words: the nine `i-ša-qal` rows, the five `im-ta-ḫa-aṣ` rows, etc. land on the same line numbers; the line division of units.json equals Harper's, 107 of 107, script-checked against packet.md; the only sign-level differences from Harper's transliteration are the logograms, ṣ for his z, and his `ṣ̌a`, all accounted for).
2. Concordance: every repeated word was set side by side (šum-ma, a-wi-lum/lim/lam, DUMU, uḫ-tab-bi-it ×3, iš-te-bi-ir ×3, li-e-it ×4, im-ta-ḫa-aṣ(-ma) ×8, im-tu-ut ×7, ša li-ib-bi-ša ×4, uš-ta-(a)d-di-ši ×3, the eleven silver lines, the numerals). Every set is the same signs row for row; no unit spells a repeated word differently from its plate.
3. Sign identity against Harper's List of Signs (stele-form column): ZI (his no. 41, cross + chevrons) is what stands in zi-im-ma-am and ma-ḫa-zi-; ŠÁM (no. 83); UM (65); ME-shape (184); NER.PAD.DU (170, three signs); GU₄ (109); ŠI/IGI (172); DI (175, the same diamond in uš-ta-dí-ši and uš-ta-ad-di-ši, so Harper's acute is only a print mark); GISH (108); AZ (63); the A, PI, LIM, MA, šum, SAL, KUR, DUMU, ARAD shapes (204, 149, 172, 132, 60, —, —, 70, 16).
4. What I did NOT do: identify every wedge of every syllabogram independently of Harper. Where the plate shows nothing against Harper's printed value I followed it, and the concordance (identical rows for identical words) is the check on that. Findings below are the places where the plate does contradict the draft.

### Changes made

| unit (col line, ln) | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| U8 (XXXIII 58) | words, n | high | `KÙ.BABBAR-im`: a third glyph IM (role comp) that is not on the plate. After the numeral and ma-na the row has exactly two signs, KÙ (hook-and-box) and BABBAR (arrowhead with its small wedge) — Harper's own no. 179 kaspu is those two signs. The drafter notes say "-im checked at XXXIII 58": it is not there. conventions.md: a logogram without complement is bare (`KÙ.BABBAR`) | removed the IM glyph, reading `KÙ.BABBAR`, morph g [0,1]; note says plainly that only the two signs are written and -im is the grammar's |
| U15 (XXXIII 73) | words | high | same: IM complement not on the plate (row 73) | same fix |
| U19 (XXXIII 86) | words | high | same (row 86) | same fix |
| U21 (XXXIII 91) | words | high | same (row 91: `10 GÍN KÙ BABBAR i ša qal`, nothing between BABBAR and the I of išaqqal) | same fix |
| U29 (XXXIV 17) | words | high | same (XXXIV 18) | same fix |
| U30 (XXXIV 20) | words | high | same (XXXIV 21) | same fix |
| U33 (XXXIV 28) | words | high | same (XXXIV 28) | same fix |
| U37 (XXXIV 39) | words | high | same (XXXIV 39) | same fix |
| U39 (XXXIV 43) | words | high | same (XXXIV 43) | same fix |
| U42 (XXXIV 49) | words | high | same (XXXIV 49) | same fix |
| U44 (XXXIV 53) | words | high | same (XXXIV 53) | same fix |
| U35 (XXXIV 33, §210) | words, n | medium | `i-du-uk-ku`: the third sign is keyed IG (𒅅, Harper no. 40 ik/ig/GAL). The plate shows the box-and-triangle sign (the same shape as the AZ of im-ta-ḫa-aṣ, XXXIV 25), which is Harper's no. 62 ug/uk (drawn like no. 63 az), not the box-and-bar of GAL in i-ša-qal | sign IG → UG (tr uk kept); note names Harper no. 62. (Published 11-25 and 112-126 key IG for this same word; see QUESTIONS) |
| U3 (XXXIII 48, §196) | l, i, n | medium | "they-shall-put-out / they shall put out his eye": "put out" is not derived from the grammar (the drafter itself says the verb ḫapādum is unattested and its sense taken from the law) and is the stock English of the famous translations; the talion lines must be rebuilt from grammar alone | l "his-eye they-shall-destroy.", i "they shall destroy his eye.", note says the Akkadian has two different verbs (ḫabātum-D, ḫapādum-D) and that "destroy" stands for both because the grammar cannot tell them apart; house-rendering sentence corrected |
| U2 (XXXIII 45, §196) | n | medium | "plain meaning 'to rob': 'has ruined, destroyed'", "UNCERTAIN beyond 'destroyed'" — "destroyed" is itself not derivable (D-stem of a verb of robbing); the uncertainty was drawn one word too late | note now says "destroyed" is taken from the sense of the law, not the grammar; UNCERTAIN as a word |
| U17 (XXXIII 79, §202) | n | medium | {mašak} + `qi-na-az`: Harper's List no. 153 (qinazu) draws these three pieces as ONE sign; the plate's first two pieces (sprout, cross) are not the ordinary KI (diamond with wedge, ak-ki-su) or NA (bow-tie diamond, i-na) of the same plate. The note said the list "draws the same three" and presented the syllabic split as fact | note now states that Harper lists it as one sign, that the first two pieces are not the plain KI and NA, and that the split qi₂-na-az (keys kept) is a reconstruction, UNCERTAIN |
| U25 (XXXIV 7) | n | medium | "ṣimmam is ṣimmum 'wound'" stated flat (the drafter's own list calls it uncertain); also -šu in ištakanšu glossed "on him" with no word that it is the dative -šu(m) written without m | sense marked Harper's, UNCERTAIN, not derivable from the grammar; -šu(m) dative, m not written |
| U40 (XXXIV 45, §213) | l | medium | "If a-slave-woman of-a-man has-struck-and": no subject word in the sentence and no "he-", so l reads as the slave-woman striking (i says "he has struck"); elsewhere subject-less verbs carry "he-" (U4, U6, U14, U25) | l "If a-slave-woman of-a-man he-has-struck-and" |
| U11 (XXXIII 64, §199) | i, n | low | i "half of his price": "his" reads as the offender's; the -šu is the slave's. Note said ŠÁM is drawn "as a long wedge with three signs in it" (no. 83 is one long sign with hatched strokes) | i "he shall pay half of the slave’s price."; note corrected |
| U21 (XXXIII 91) | words (say), n | low | `ešeret`; published 42-51 / 52-65 say `ešret` for 10 before the counted noun, and latest-published wins | say ešret; note rewritten (construct, as the 10 GAN.E) |
| U33 (XXXIV 28) | words (say), n | low | same | same |
| U0 (XXXIII 41, §195) | words (say), n | low | `abāšu`; published 185-194 `abašu` (house spelling keeps the vowel before the suffix short) | say abašu, note |
| U16 (XXXIII 75, §202) | words (say), n | low | `elīšu`; published 1-10, 42-51, 141-152 `elišu` | say elišu, note |
| U16 (XXXIII 75) | n | low | "so Delitzsch's lētu, 'cheek, jaw'" — an attribution I cannot verify and not derivable from the grammar | "the dictionary sense 'cheek, jaw'; UNCERTAIN, not derivable from the grammar" |
| U17 (XXXIII 79) | n | low | "puḫrum, the same word as in the prologue": the word is in §5 (laws-1-10), not the prologue; "Delitzsch's 'whip, thong'" unverifiable attribution; one ḳ in a note (Harper's "ḳinazu") against the q rule | "as in §5"; "dictionary sense"; qinazu |
| U1 (XXXIII 43, §195) | n | low | "the code's way of saying 'the court shall have it done'" asserts a sense the form does not give | "an impersonal 'they': the code does not say who does it" |
| U1 (XXXIII 43) | n | low | the identification of the second rittu sign was asserted from memory of the list | note records what the plate and the list show: a vertical with a horizontal tail = no. 184 me, no. 181 lal drawn alike, and Harper's rittu entry shows UM + the same shape (identification stays UNCERTAIN) |
| U28 (XXXIV 14, §207) | n | low | "he swears again": "again" is not in the form (itammama is itamma + -ma) | "the same oath as in §206" |
| U44 (XXXIV 53) | n | low | Harper's "iṣ̌aḳal" cited with ḳ (q rule, conventions "including when a note cites Harper") | iṣ̌aqal |
| about | about | low | "loses his hands (§195)" asserts the plural the drafter itself marks UNCERTAIN | "has his hand cut off (§195; whether one hand or two is uncertain)" |
| about | about | low | closing list of uncertain words named only "the verb of the second eye clause" and omitted the whip group | "the two verbs of the eye clause … the sign group for 'whip'" |

Counts (rows above): high 11, medium 6, low 13 — 30 changed rows over 22 units (the 11 kaspim words and the U35 sign are the only glyph changes; the rest are notes, l/i, `say` and `about`).

Open, NOT fixed here (outside units.json; must be fixed before `R3 build`): **high** — the new sign PAD in `signs-cuneiform.json`, and its embedded copy in `index.html` / `reader.html`, has the glyph U+0080 (a control character) instead of 𒉻 (U+1227B CUNEIFORM SIGN PAD, which `unicodedata.lookup` returns). Every NER.PAD.DU (units U4, U5, U7, U10) would print a broken character. Repair it with `signs.py` (remove the entry in all three places and re-add it by Unicode name, or whatever the tool permits) and run `signs.py check`.

### Checked and found right (no change)

- Line division, col/line of every unit, `nl` flags, `ln`/`p` on the first unit of each law (§195–214; Harper's running numerals, headings one behind from §206 — the plate's margin numerals and the pencilled § numbers 207 at XXXIV 14, 208 at 20, 209 at 23, 210 at 31, 211 at 35, 212 at 41, 213 at 45, 214 at 51 agree with the running numerals).
- Numbers/amounts in §§198–214, each against the plate: 1 mina (XXXIII 58, 86: one upright wedge); ⅓ mina (XXXIII 73, XXXIV 21, 53: two uprights over a bar); ½ mina (XXXIV 18, 43: the cross); 10 shekels (XXXIII 91, XXXIV 28: the corner wedge); 5 (XXXIV 39: five wedges in two groups); 2 (XXXIV 49: two uprights); 60 (XXXIII 81: wedge + ŠU + ŠI, the ŠI being the arrowhead-and-bar of Harper's no. 172, so ŠU.ŠI, not ŠU.SI). The statement of each law's penalty in l, i, n and about matches.
- Reading reconstructs from the glyphs' tr for every word (script); every glyph in a morph entry; every sign key exists (PAD's glyph aside).
- No ḳ left in any field (the two that were there are fixed above).
- ZI = Harper's no. 41 on the plate in zi-im-ma-am, ma-ḫa-zi-šu, ma-ḫa-zi-im; reading ṣi follows ṣimmum / maḫāṣum as in published 112-126 (kept).
- MAŠ for ½, THIRD for ⅓, IA5 for 5, MIN for 2, U for 10, DISH for 1: shapes agree.
- Grammar labels checked form by form: imtaḫaṣ perfect (infixed -ta-), imḫaṣ preterite; inakkisū, išebbirū, uḫappadū, idukkū present plural; inaddû = inaddi + -ū; immaḫḫaṣ N present; išaqqal present; uštaddīši Š perfect + -ši; ištebir perfect of šebērum; ittadi perfect of nadûm; itamma / itammama; rabû stative with the subjunctive -u after ša; maḫāṣišu / maḫāṣim infinitives; amḫassu = amḫaṣ + -šu (ss, ZU); mārassu = mārt + -šu. All fine as written.
- l ↔ i force for every unit, apart from the rows above: the pairs agree in tense, person, number and structure.

### Findings refused

- **"knocked out" for ittadi / inaddû (U12–U14), kept.** nadûm is "to cast, throw"; for a tooth "knock out" is the natural English for "cast out" and the note already says the verb is certain and the idiom is the law's; l keeps the literal "cast-out". Not a remembered formula in the way "put out his eye" was (that one the drafter itself could not tie to the grammar).
- **"an eye for an eye" in titleEn / part name, kept**: it is the plan's name for the block (packet.md title), a label not a rendering; the text's i never uses it.
- **AH key for uḫ (uḫ-tab-bi-it, pu-uḫ-ri-im) kept**: Harper draws uh (no. 151) and ah/ih (no. 156) differently, but the published parts key all of them AH (pu-uḫ-ri-im, nu-uḫ-ši-im, tu-uḫ-di-im) and the glossary gives AH the value uḫ. Consistency over a sign split I cannot settle from 1904 drawings.
- **ME for the second sign of rittu kept** (UNCERTAIN as marked): the plate and no. 184 agree; so does no. 181 lal, which I now say in the note. Not decidable from the autograph.
- **ZI read ṣi where Harper prints zi kept**: Harper's own XXXV 21 prints ṣi-im-ma-am for the same word; published 112-126 keys ZI = ṣi in ma-ḫa-ṣi-im.
- **uštaddīši (long ī before -ši) kept**: the published parts write short before -ši (lā ušamziši), but this form is a III-weak Š perfect where the long vowel is the stem's; the written da-/ad-di-ši does not decide it. Not changed; mentioned in QUESTIONS only for house-style consistency.
- **Plural "hands" vs "hand" (U1)**: i keeps "his hands" with the UNCERTAIN note (Harper's -ê is an oblique dual); the about now says "hand" is open. The plate gives only UM + ME-shape + ŠU, no number.
- **idû as infinitive of edûm, risbatum "brawl", lētum "cheek"**: all three are Harper's/dictionary senses, already flagged UNCERTAIN in the notes; no better reading from the grammar.
- **Law boundaries and ln for §208 as p: true although the sentence continues §207's pattern**: Harper's heading and the pencilled 208 on the plate (XXXIV 20) both mark it; kept.

### For QUESTIONS.md

1. KÙ.BABBAR-im: the published parts 1-10, 127-140, 153-169 write `KÙ.BABBAR-im` with an IM glyph; in this part all eleven silver lines on plates 57–60 have only KÙ + BABBAR. Someone should check those earlier plates for the IM complement (and for UG vs IG in `i-du-uk-ku`, published 11-25 and 112-126 as IG, here the plate shows UG/AZ shape).
2. House spelling of the vowel before a pronominal suffix is short in the published parts (abašu, elišu, bēlišu); the grammar would give abāšu, elīšu. Followed the published short forms here; a global decision is open.
3. `ešret` (construct) vs `ešeret` for 10 before šiqlum: followed the published `ešret`.
4. Harper's no. 153 (qinazu) is one sign in his list; the split into KI NA AZ is a reconstruction (U17).
5. rittu: UM + ME-or-LAL-shaped sign, hand or hands: unresolved (U1).
6. The sign PAD glyph is U+0080 in signs-cuneiform.json, index.html, reader.html: repair before build.
7. The two verbs ḫabātum-D / ḫapādum-D of the eye talion are both rendered "destroy"; if a later part or an owner decision gives ḫapādum a sense, §196 should be revised.

## Pass 2

Reviewer: strongest model, adversarial, second pass (units.json + gloss.json + linecheck + pass-1 changes). Backups outside the repo (scratchpad `p2/units.orig.json`, `p2/gloss.orig.json`). Edits by script; rebuilt; `validate` prints PASS; `signs.py check`: in sync.

### Sign PAD
PAD in `signs-cuneiform.json` is 𒉻 U+1227B (checked by code point), and the same character is in `index.html` and `reader.html`; the pass-1 U+0080 problem is gone. No action.

### Linecheck (18 lines), plate spot-checks
Plate 57 (PDF 329) XXXIII 43 and plate 59 (PDF 333) XXXIV 26–45 re-read at zoom 5–6 (row structure, numeral shapes, the five-wedge numeral at 39); the rest rest on pass 1's 107-line reading. Classification of the 18 lines:
- **Pure logogram or numeral differences (Harper writes the Akkadian word or a Roman numeral/fraction):** the eleven silver lines (XXXIII 58, 73, 86, 91; XXXIV 18, 21, 28, 39, 43, 49, 53: I / ⅓ / X / ½ / V / II + ma-na kaspim against our numeral + ma-na + KÙ.BABBAR); XXXIV 24 (mârat = DUMU.SAL), 31 and 41 (zinništum = SAL), 51 (amtum = GEME₂); XXXIV 33 (mâra-zu = DUMU.SAL-zu).
- **Not only a logogram difference, a real reading difference from Harper:** XXXIII 43 (Harper's syllabic rit-tê-šu against our UM.ME-šu: the plate shows UM-box, vertical-and-tail, ŠU, three clusters, so the sign count agrees but the identification of the middle sign is ours and UNCERTAIN, already in the note) and XXXIII 80 (Harper's ḳinazi alpim: besides GU₄ = alpim, our qi₂-na-az splits Harper's single no. 153 into three keys, a reconstruction already marked UNCERTAIN in the note).
No line needs a change.

### Changes made (units.json)

| unit (col line, ln) | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| U28 (XXXIV 14, §207) | i, n | medium | “If he has died from his blow, he shall swear” — the same “he” is the victim (imtūt) and the striker (itammama); the reader cannot tell who dies | i “If the man has died from his blow, he shall swear, and”; note says the subject of imtūt is the man struck and is not written |
| U29 (XXXIV 17) | i | low | “if the dead man was a man’s son”: “the dead man” is not in the Akkadian and the next unit says “If he was a commoner’s son” | “if he was a man’s son” (parallel with U30) |
| U12 (XXXIII 66, §200) | i, n | medium | “a man of his own rank” for awīlim mēḫrišu (“a man, his equal”): not built from the grammar and the stock English of older translations; the talion lines are to be rebuilt from grammar | i “a man who is his equal”; house-rendering sentence in the note changed to match |
| U34 (XXXIV 31, §210) | l | low | l “If that woman” reverses the Akkadian order (zinništum šī); U38, U43 keep the order (“If woman that”) | l “If woman that has-died,” |
| U36 (XXXIV 35, §211) | l | low | no subject at all in this sentence, but l has no “he-” (pass 1 added “he-” to U40 for the same reason) | “he-has-made-her-drop” |
| U37 (XXXIV 39) | n | low | note says the numeral 5 is “five wedges in one sign”; pass 1 and the plate show two groups | “five wedges in two groups” |
| U0 (XXXIII 41) | n | low | “§195–200 are the talion laws (repaid in kind)”: §198–199 are silver fines | “the laws of the hand, the eye, the bone and the tooth (repaid in kind between equals, in silver otherwise)” |

### Changes made (gloss.json)

All 17 new lemmas were checked against the forms in units.json and the notes; all 7 broaden entries are the old entry whole (from the latest published holder, by script: nadûm-Š and šīmum from 100-111, nadûm from 153-169, maḫāṣum from 112-126, nakāsum from 185-194, edûm from 127-140, libbum from 178-184) + " · " + the new reading. No invented modern forms. Grammar labels agree with the forms (D perfect uḫtabbit, D present uḫappadū, N present immaḫḫaṣ, construct šinni/lēt, present išebbirū/inakkisū, perfect ištebir/imtaḫaṣ).

| entry | severity | what was wrong | what was done |
|---|---|---|---|
| rittum | medium | “Harper normalizes rit-tê-šu, an oblique plural or dual ending” names a grammar the note (and Harper) does not give | “an ending -ê whose grammar is not clear to me”; number and second sign stay UNCERTAIN |
| uznum | low | “uznašu (u-zu-un-šu, accusative + -šu)”: the spelling has no vowel between un and šu, so “accusative” is Harper's normalization, not the spelling | said so in the entry |
| edûm (broaden) | low | gloss “knowingly I did not strike him” can be read as “I did strike him, unknowingly” (word order) | “in knowing, I did not strike him”, i.e. “I did not strike him knowingly” |
| mārtum (broaden, added) | low | mārat (DUMU.SAL, construct, nominative/accusative) is a new form of the lemma, not in the old entry (which has mārtim, mārassu) | old entry whole + " · mārat (DUMU.SAL, no ending written) construct “daughter of” …" |
| amtum (broaden, added) | low | amat (GEME₂, construct) likewise absent from the old entry | old entry whole + " · amat (GEME₂ …) construct “slave-woman of” …" |

### Findings refused

- **ittadi / inaddû “knock out” (pass 1 refused; I agree it stays).** nadûm “cast, throw” + šinnum has no English that is not an idiom; l keeps “cast-out”. Recorded in QUESTIONS as a rendering a later owner decision may revisit.
- **titleEn / part “an eye for an eye”.** The plan's name for the block, a label, not a rendering; no unit uses it.
- **“ox-hide whip” (U17).** The hide determinative is on qinazi and alpim “of an ox” follows, so “ox-hide whip” combines both written facts; the note says which is which.
- **“who is like himself” (U18).** Reflexive English is a little off, but “who is like him” is as ambiguous; the note carries the sense. Left.
- **uštaddīši long ī (pass 1 kept).** Agreed: III-weak stem + -ši contracts (as iddīšu). But 100-111's entry (the same stem, uštaddišu) is short; the entry now carries both spellings. In QUESTIONS.
- **lū, ina, kīma, šuāti, alpum, šakānum not broadened.** The old entries (“or”, “in, from … (by means of)”, “like, as”, “him”, “ox”, “to set”) already cover this part's use.
- **ŠÁM = šīmum, UM.ME, ma-na in syllables (not MA.NA as in 112-140).** All follow the plate and Harper's lower-case ma-na; 52-65 and 153-169 also spell ma-na. Not changed.
- **Title/part column numerals lower-case** matches the published parts (xxxii 31 …).

Counts for Pass 2: high 0, medium 3 (U28, U12, rittum), low 9 (U29, U34, U36, U37, U0, uznum, edûm, mārtum, amtum). 12 changes. Combined with pass 1 (high 11, medium 6, low 13): high 11, medium 9, low 22.

### For QUESTIONS.md (pass 2)
1. uštaddīši (this part) against uštaddišu (100-111, same III-weak Š perfect + suffix): long or short vowel before -ši/-šu; global decision on the house spelling.
2. “knocked out” for ittadi/inaddû of a tooth, a stock-English idiom for “cast out”; revisit when the nadûm entry is reviewed as a whole.
3. i-du-uk-ku: UG here, IG in 11-25 and 112-126 (pass-1 item 1, confirmed still open).
4. XXXIII 80: Harper's single sign no. 153 ḳinazu against our three keys KI NA AZ, and XXXIII 43 UM.ME against Harper's rit-tê-šu: both reading differences, not logograms.
5. The ⅓ and ½ signs, the spoken šūši (“1 ŠU.ŠI” = sixty, the thing counted not written).
