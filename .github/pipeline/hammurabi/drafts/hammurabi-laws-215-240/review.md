# Review — hammurabi-laws-215-240

## Pass 1

Reviewer: strongest model, adversarial. Inputs: RUNBOOK §2, conventions.md, runbook.md (Reviewer), packet.md, units.json, the published parts (glossaries and units, for house renderings), Harper's plates 60–64 (PDF 335–343), his List of Signs (nos. 16, 58, 128, 129, 168, 179, 209 looked up). Backup of the original units.json is outside the repo (scratchpad `rev/units.orig.json`). Edits were made in place by script; every changed field is listed below. `r3.py build` was run only to see errors: the only errors left are the missing-gloss ones (100), as expected.

### How the plate check was done (and its limit)

Plates: Plate 60 (PDF 335) = XXXIV 50–96; 61 (337) = XXXV 1–44; 62 (339) = XXXV 45–94; 63 (341) = XXXV 94–98, XXXVI 1–36; 64 (343) = the rest. (The packet's plate list is one off.) Line numerals checked against the margin numerals (XXXIV 55 at the sixth row of Plate 60, pencilled §214 at XXXIV 51, XXXV 25, 45 …): the running numerals are right.

What I did: read at zoom 5–9 and counted sign-groups row by row for XXXIV 55–58, 65–68, 82, 92–93, XXXV 22–27, 36–42, 55–57, 64–65, 75–77, 80–92, 98, XXXVI 5, 10–15; compared every repeated word (šum-ma, i-na-ad-di-in, KÙ.BABBAR, uš-ta-mi-it …) for identical shapes; read Harper's list entries 128, 168, 179, 209 against the plate. What I did NOT do: identify every wedge of every syllabogram independently of Harper, or read XXXVI 21–37 and XXXVI 63–80 sign by sign (their rows were not counted; only the logograms there, GIŠ.MÁ, MÁ.DU.DU, were checked in other rows). The structure (line division, repeated words, `nl`, numerals) agrees with the plate everywhere I looked; the exceptions are the three open items below.

Mechanical checks (script): every `reading` reconstructs from the glyph `tr` values; all morph indices valid; no ḳ in any field; every sign key exists in signs-cuneiform.json (SHITIM, FOUR included); `ln` and `p` stand on the first unit of each of §215–§240 and nowhere else; unit start lines agree with packet.md (the 19 differences are all logograms or numerals Harper writes as words); Harper's XXXIV numeral drift is noted in the first unit and in `about`; the drift ends at XXXV 1 as the packet says.

### Changes made

Unit numbers are 0-based positions in `sentences` (with col line, § in brackets).

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 43 (XXXV 69, §229) | n | medium | imqutma called a "perfect" of maqātum; im-ku-ut is the preterite imqut (perfect would be imtaqut) | "preterite (imqut)" |
| 54 (XXXV 95, §233) | n | medium | iqtup called a "perfect"; iq-tu-up is preterite-shaped (perfect would be iqtatap) | "has the shape of a preterite … a perfect would be iqtatap" |
| 60 (XXXVI 16, §235) | n, morph lemma | medium | izzapar called an "N present"; iz-za-par has one p, a present would be izzappar; lemma `zapārum` invents a root | note says N-stem preterite shape, root not known; lemma → `izzapar` (form-lemma, as published `ibbûm`, `upaṣ`) |
| 34 (XXXV 43, §227) | l, n, morph lemma | medium | l "has-deceived-and" gives a sense as if read, while the note says the verb is unread; lemma `daʾāṣum` is an invented root | l "has-idāṣ-and" (unread verbs keep their form in l, as the draft does for iqtup, uštēṣbima); note says the sense is not derivable; lemma `idāṣ`. i keeps "deceived (?)" |
| 56, 58 (XXXVI 4, 10, §234–235) | l, morph lemma | medium | l "caulked" for ip-ḫi(-ma), an unread verb, with "caulk" a stock-translation sense that cannot be rebuilt from the grammar; lemma `peḫûm` | l "he-has-ipḫi(-and)"; lemma `ipḫi`; i keeps "caulked (?)" |
| 56 | n | medium | justification "the next laws … the boat's leaking" cites a reading (izzapar) the part itself cannot make | rewritten: not derivable from the form; the sense a boatman's fee seems to need; UNCERTAIN |
| 67 (XXXVI 41, §237) | l, i | medium | l "he-has-loaded-her" and i "has loaded her" for iṣēnši, an unread verb (note says UNCERTAIN); no (?) in i | l "he-has-iṣēn-her"; i "has loaded (?) her" |
| 31 (XXXV 36, §226) | n, say | medium | note states flat that abbuttum is "a distinctive hair-cut or lock of hair" (not in the text, not Harper: published 141-152 gloss it UNCERTAIN, Harper "service, slavery"); say `abbuti` against the note's `abbutti` | note hedged to the 141-152 wording (later dictionaries' sense, hair-style not in the text, UNCERTAIN), construct before wardi; say `abbutti` (units 31 and 35) |
| 49 (XXXV 82, §232) | n | medium | note said only that the first sign "looks like" Harper's ŠÀ (no. 209). The plate (XXXV 82, 90, XXXVI 22) draws the first sign like no. 209 (box, vertical, diagonal) and the second like no. 128; and XXXV 82 has an extra sign (box with bar and long vertical) between ma and the ŠÀ-like sign that neither Harper's text nor the draft has | note states exactly this; extra sign left unkeyed, marked UNCERTAIN/open. Glyph keys NOT changed (see "Open") |
| 39 (XXXV 56, §228) | n | medium | note "the single sign Harper numbers 168". On the plate (XXXV 56, 64, 93) a bar-and-vertical sign stands between ma and the diamond-bearing sign that alone is ŠITIM at XXXV 75 and 98 | note says so; SHITIM called Unicode ŠITA, tentative; extra sign left unkeyed, open |
| 38 (XXXV 52, §227) | i | low | "shall go free" for ūtaššar; house rendering (100-111) is "he shall be released", and l says so | "shall be released" |
| 71 (XXXVI 56, §238) | i | low | "has raised it again": "again" is not in uštēliašši | "has raised it" |
| 64 (XXXVI 32, §236) | i, n | low | i "has lost it" for uḫtalliq, which is "destroyed" in §232 and in l; tebûm "sink" against published "rise" (1-10 ušetbûšuma) unmentioned | i "has destroyed it"; note says why "sink" (the law's sense, uštēliašši "raised" as its opposite) |
| 69 (XXXVI 48, §237) | i | low | same "lost" for uḫtalliq | "has destroyed what was in her" |
| 32, 35 (XXXV 39, 45) | l | low | l "not his-own" gives the sense of še-e-im, which the note marks UNCERTAIN | l "not šēm"; i keeps "not his" |
| 37 (XXXV 50, §227) | n | low | "ḫalālum 'to hang up'" stated flat | "hang" called the usual sense, not shown by the form; UNCERTAIN |
| 77 (XXXVI 72, §240) | n | low | note "ḫalqu 'are lost'"; mimma is singular and l says "is-lost" | "is lost (the stative with the subjunctive -u)" |
| 78 (XXXVI 76, §240) | n | low | note spells mimmāšu, say is mimmâšu | note mimmâšu |
| 75 (XXXVI 67, §240) | n | low | "perhaps a fast and a slow, or one under way and one at moor": guesses for unread words with no basis in the form | removed |
| 28 (XXXV 26, §224) | n | low | idīšu given as certain; the case vowel is the grammar's (accusative would be idāšu) | said so, UNCERTAIN |
| about | about | low | "a gentleman" (stock word; house is "a man"); "tricked", "caulking", "near the eye" stated as known | "a man"; hedged the three |

Counts: high 0, medium 10 rows, low 12 rows (22 rows over 20 units and `about`; 26 changed fields incl. lemma edits).

### Checked and found right (no change)

- Grammar labels, form by form: ubtalliṭ D perfect; īpušma, iptēma preterite; uštamīt Š perfect; uštalim Š perfect; uḫtabbit, uḫtalliq D perfect; ugdallib D perfect, ugallib D preterite; uttebbi D perfect, utebbima D preterite, utebbû with -u; idukkū, inakkisū, iḫallalūšu, udannan present; iddâk N; ippeš present; udanninma D preterite; inaddiššum present + -šum; ušaklilšum Š; īgīma preterite of egûm; īgurma preterite; tebiat stative; ubârma present; imqutu preterite + -u; lā udanninuma subjunctive -u before -ma (not a plural).
- Numerals and fractions against the plate: 10 (corner wedge), 5, 3, 2, 60 (single vertical wedge, XXXVI 5), IGI.6.GAL (IGI + three-over-three + GAL, XXXV 25), 4, 6.
- KÙ.BABBAR: no IM complement on the plate at XXXIV 65 and XXXV 25 (two signs and nothing after); the other lines where Harper prints kaspam/kaspi (XXXIV 93, XXXVI 60) show KÙ + BABBAR with no extra sign I could assign (the group count there is crowded; I kept bare).
- Á-šu (XXXV 27): one sign (box with hatch, chevrons, vertical) + šu; Harper's no. 129 id/it; kept A2.
- ŠU.I (Harper no. 138): two signs at XXXV 41; kept. GIŠ.MÁ, MÁ.DU.DU (no. 58 shows MÁ and two DU): counts agree at XXXVI 4, 10, 5.
- ŠITIM at XXXV 75, 98 is one diamond-bearing sign: kept.
- "I did not shave him knowingly" (i of XXXV 52): "him" kept; it parallels the published §206 "I did not strike him knowingly".
- "a bronze knife" for GÍR.NI: the note already says the kind is unread; kept.
- "If a physician has made a severe wound … on a commoner's slave" (unit 13) carries the verb of the next unit in i; same device as the "If it is a man's slave" units. Kept.
- Numeral drift note, `col`/`line`, `nl`, `ln`/`p`: right.
- Overlap check against distinctive modern renderings (red-flag only, nothing opened): no verbatim run found; "he shall replace the slave with a slave", "that builder shall be killed" and "they shall cut off his hands" are the plain grammar and house forms already in earlier parts.

### Findings refused

- GAR → SHA3 (ŠÀ) as the first sign of ŠA.GA, and GA → GAR: the plate supports it (see unit 49), but eight published parts write GAR + GA for the same word and a change here would show the same logogram two ways in one work. Left; recorded under Open.
- "shall give … one sixth (of a shekel)" (unit 27): the unit is the natural one and the note says it is not written; kept.
- "sinew (?)" for še-ir-ḫa-nam (unit 19): hedged in i and note; joining Harper's two words is explained. Kept.
- "boatman" for MÁ.DU.DU, "strong boat": derivable (malāḫum read from the sign group; dannum).
- uštēṣbima "Š perfect": left as written (the note already calls the root unknown).
- "ina šattimma" "in that very year": the -ma is real; kept.

## Open (not fixed; affects glossary / later check)

1. **XXXV 56, 64, 93 (and possibly 82):** an extra bar-and-vertical sign group between ma and ŠITIM (and between ma and ŠÀ.GA at 82) on the plate, absent from Harper's text and from the draft. I could not identify it (a LÚ-like determinative? a second part of the word?). Needs a human look at Plate 62, rows 56, 64, 82 and Plate 63, row 93. Until then the unit notes say it is unkeyed. Does not block the build; it is a visible sign omitted on four lines.
2. **ŠA.GA keys:** the plate shows ŠÀ-box + gar-shaped sign; all nine parts key GAR + GA (glyph 𒃻𒂵 for a box-and-arrow pair). A global decision (QUESTIONS.md).
3. XXXIV 92 `uḫ-tab-da(=it)` note: I did not recount the signs of this row to the plate (the row is crowded); the note's claim that DA stands where "bi-it" is meant is unchanged and unchecked.
4. The gloss must handle: tebûm "to rise" (1-10) against "sink" here (broaden); form-lemmas `idāṣ`, `izzapar`, `ipḫi`, `iṣēn`, `uštēṣbi` are UNCERTAIN entries; abbuttum (broaden 141-152's entry); gullubum: the verb "to shave" is galābum, D infinitive gullubum; the lemma `gullubum-D` (units 32, 35, 38) named an infinitive as the verb: renamed `galābum-D`, notes at units 32 and 35 corrected (medium, grammar label; 3 morph entries + 2 notes).
5. For QUESTIONS.md: the sign-level reading of XXXVI 21–37 and 63–80 rests on Harper's values plus the repeated-word concordance, not on a wedge-by-wedge reading.

## Pass 2

Reviewer: strongest model, adversarial. Inputs: Pass 1 above, RUNBOOK §2, conventions.md, runbook.md, units.json, gloss.json (Sonnet), the published `hammurabi-*.json` glossaries, linecheck.md, Harper's plates 60–64 (PDF 335–343) and List of Signs (PDF 393–407). Backups of units.json and gloss.json as received are outside the repo (scratchpad `rev2/`). Edits were made in place by script; `r3.py build` then `r3.py validate` were run: **PASS**, one WARN (the 67 linecheck lines, below).

### Changes made

| unit / entry | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| unit 39 (XXXV 56, §228) | n | medium | Pass 1 and the draft said an unidentified "bar-and-vertical sign" stands between ma and ŠITIM, left unkeyed ("open"). There is no extra sign: šum is drawn in TWO parts (an arrowhead + a hatched triangle: see XXXVI 42 bottom tier "šum-šu", XXXVI 80 "-šum", every "šum-ma" row) and ma is the bar-and-vertical sign (the same shape ends every "-ma", e.g. i-bu-uš-ma at XXXIV 58). The line is šum, ma, ŠITIM (one sign, Harper's no. 168, as the plate row 168 of his list shows it). The note therefore told readers of a sign that does not exist | note rewritten: ŠITIM is one sign, the same alone at XXXV 64, 72, 75, 93, 98; šum two shapes, ma the bar-and-vertical sign; nothing unread before the builder's sign |
| unit 49 (XXXV 82, §232) | n | medium | same mistake: "a further sign … stands between ma and the ŠÀ-like sign … unkeyed (UNCERTAIN, open)" | sentence replaced by the true state (šum two-part, ma bar-and-vertical, nothing between ma and ŠA.GA). The remark that the first sign looks like ŠÀ (no. 209) and the second like no. 128 stays, as does the GAR/GA key (see refused) |
| unit 78 (XXXVI 79, §240) | glyph GA `tr`, word `reading`, n | low | glyph `tr` "ga" and reading "ḫal-ga-am" (Harper's g); the house reading of GA as q is `qa₂` and five published parts read this very word ḫal-qa₂-am (conventions: "GA read qa = qa₂") | `tr` qa₂, reading ḫal-qa₂-am; note says Harper prints g, the sign is GA read qa₂. `say` ḫalqam unchanged. The plate sign is the same hatched-comb + arrowhead GA as in ŠA.GA |
| unit 60 (XXXVI 18, §235) | word `say` | low | say "ḫiṭitam" (short i) against lemma ḫiṭītum and the published ḫiṭītam (141-152) | say ḫiṭītam |
| units 63, 77, 78 | glyph `val`, word `say` | low | the first glyph of GIŠ.MÁ-šu carried val "elippušu" while `say` was "elippišu" (63, 77 second, 78) — val and say disagreed; and in XXXVI 72 (unit 77 first GIŠ.MÁ-šu, Harper's elippu-šu, the boat as subject of tebiat) `say` was elippišu against Harper's nominative | val = say = elippišu in 63, 77 (second), 78 (Harper's elippi-šu at XXXVI 28, 73, 79); in 77 (first) say = val = elippušu |
| unit 77 | n | low | note "elippušu, elippišu are GIŠ.MÁ with ŠU" said nothing of which is which | note says elippušu is the subject form (Harper's elippu-šu), elippišu follows ina (Harper's elippi-šu), vowel not written |
| gloss `elippum` | entry | low | forms met did not include elippušu | elippušu (GIŠ.MÁ-šu, Harper's elippu-šu) added |
| gloss `__broaden__` `ḫalāqum-D` | new | low | holder (112-126) had only uḫalliqu; this part has uḫtalliq (perfect) three times (XXXV 83, XXXVI 34, 49) and the glosser did not broaden | holder's text kept whole + " · " + the perfect uḫtalliq with two examples |
| gloss `__broaden__` `egûm` | new | low | holder (112-126) has itēgi(ma), igûma; this part has īgīma (preterite + -ma) at XXXVI 32 and 45 | holder's text kept whole + " · " + īgīma |

Counts: high 0, medium 2, low 7 (9 rows; 8 fields in units.json, 3 in gloss.json). No lemma, grammar label, `l` or `i` needed changing in this pass.

### Task 1 — gloss.json checked against text and grammar

- Every one of the 33 new entries was read against the units that use it (forms, sign spellings, glyph sequence, UNCERTAIN marking). All forms quoted occur in the units; sign claims match the glyphs (e.g. še-e-im = SHE E IM; ZÚ.LUM = KA + LUM; ŠU.I = ŠU + I; IGI.6.GAL); labels are right (uštamīt, uštalim, uḫtabbit, ubtalliṭ perfects; īpušma, imqutma, uttebbi-class forms as the unit notes say; ušaklilšum, uštēliašši carry no tense claim). No invented modern forms, no mis-named grammar found; every UNCERTAIN verb (idāṣ, uštēṣbi, qatāpum, ipḫi, takālum-D, izzapar, naqārum, tebûm-D, iṣēn) is marked in the entry exactly as in its unit note. Lemma names unchanged. No new lemma duplicates one already published.
- All 15 `__broaden__` entries start with the latest published holder's full text (compared by script against the latest of the 18 earlier `hammurabi-*.json` glossaries, in plan order) followed by " · " and the new reading: nothing dropped or garbled (15/15 identical prefix). Two more were added above. `tebûm` ("rise" in 1-10 against "sink" here) is handled in the entry itself and in unit 64's note.
- Forms met in this part but covered only by the general entry (case forms, -šu/-ša/-ši/-šum suffix uses, ṣimmim, qīštišu, ramānišu, dannatam, iriabšum, mimmâšu) were left: the entries are general to the form, as the format asks.

### Task 2 — linecheck.md (67 lines) on the plates

Method (and its limit): each row of Plates 60–64 was cut out at zoom 5–9 and the sign groups counted against the glyph sequence for that stele line; repeated words were compared row against row (the six GÍR.NI UD.KA.BAR rows XXXIV 57, 61, 76, 80, 86, 90 are identical shape for shape; KÙ.BABBAR rows 65, 68, 72, XXXV 8, 11, 16, 25, XXXVI 7 are numeral + GÍN + KÙ + BABBAR with nothing after; GU₄ and ANŠE rows XXXV 18–34; MÁ.DU.DU and GIŠ.MÁ rows throughout XXXVI; the ŠU.I, ŠITIM, É, SAR, ŠÁM-šu rows) and Harper's List entries for 109, 128, 129, 138, 148, 168 were looked at. This is sign-group level: I did NOT identify every wedge of every syllabogram independently of Harper.
Results: all 67 lines confirmed as the same signs Harper prints, written as logograms or numerals where he prints the Akkadian word (his list gives UD.KA.BAR = siparru, IGI+GAL fractions, ŠU.I = gallabu, Á = id/it). The real reading differences found: (a) ḫal-ga-am (q-convention, fixed above); (b) the "extra sign" at XXXV 56, 64, 82, 93 — none, see above; (c) XXXVI 60 numeral row: KÙ BABBAR mi ši il on the upper tier and ŠÁM + ša below, as the unit has it (no extra sign); (d) XXXIV 84: the plate row has ZI with its chevrons and then ma, am, kab, tam and lacks the diamond-cross IM-part that XXXIV 56 and 75 show: Harper's "zi-ma-am" (one m) is what the plate shows, so unit 13's note is right; (e) XXXIV 92: after TAB the plate has ONE box sign (DA) where bi-it is expected, as unit 16's note says (Pass 1 open item 3: now confirmed). Bracketed signs: the plate draws the restored signs in outline exactly where the units bracket them (XXXVI 61 [in], 62 [lum], 63 [i-gur], 64 [ŠE.GUR], 65 [at], 66 [di] [šum], 67 [GIŠ.MÁ], 68 [tim], 69 [uk] [tim]).
Rows XXXVI 21–37 and 63–80 were read in this pass sign group by sign group: no discrepancy with the units, apart from the items above. Rows examined less closely than the rest (counts plausible, not exact): XXXVI 48, 53, 75–77 (crowded, two-tier).

### Task 3 — second look at units.json

- The "unidentified extra sign group" at XXXV 56/64/93/82 (Pass 1, Open 1) was a mis-count: see unit 39 and 49 above. It is therefore NOT to be said in the `about`; nothing added there.
- The ŠA.GA key question stays as Pass 1 left it. On the plate (XXXV 82, 90; XXXVI 22) the first sign has the ŠÀ shape (a box with a vertical and a diagonal) and the second is the same hatched-comb + arrowhead sign that writes ga in ḫal-ga-am (XXXVI 79): so the plate reads ŠÀ + GA, and our keys (GAR, GA) differ in the first sign only; a global decision (QUESTIONS.md), not touched here.
- Nothing else in the 79 units needed changing. Checked again and left: "I did not shave him knowingly" (unit 38, as Pass 1), the units with an unread verb (l keeps the form), the unit-27/30 fractions, ŠU.I, IGI.6.GAL, SAR, Á-šu.

### Findings refused

- GAR → SHA3 for the first sign of ŠA.GA (as Pass 1): eight published parts key it GAR; changing it here shows one logogram two ways in one work.
- Adding a comment to the `about` on the plate signs: no longer applicable (no extra sign).
- Re-keying GÍR.NI or UD.KA.BAR from Harper's shape (the plate shows 7 sign groups i-na-GÍR-NI-UD-KA-BAR in all six rows; consistent with his List 148).
- Splitting "ṣi-ma-am" (unit 13) into ṣi-im-ma-am: the plate lacks the IM part (see (d)).

### Open for the owner / later parts (nothing blocks publication)

1. Earlier parts record "an extra unidentified sign group" at XXVII 34, XXVIII 59 (zi-it-tim) and "more sign groups than the transliteration" at XXVIII 3–5 (QUESTIONS.md, 153-169 and 170-177). In this part the same appearance was produced by two things: šum is a two-shape sign, and ZI is a bar-with-verticals sign followed by chevrons that Harper's List draws as one sign; a re-look at those lines with this in mind may remove them. Not touched (other parts' files).
2. XXXV 97 (igarum iq-tu-up): the row shows more sign groups after É than the five signs of É.GAR₈ + iq-tu-up; IG/UB are multi-shape signs, so this is unresolved, not an error found; unit 54's note already says UNCERTAIN.
3. The sign-level reading of the crowded rows remains at sign-group level (see Task 2).
