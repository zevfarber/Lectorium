# Review (pass 1) — hammurabi-laws-170-177

Reviewer: strongest model, adversarial. units.json edited in place by script (backup of the draft kept in the scratchpad, not in the repository). 32 units, 385 words, unchanged in count; no glyph sign key added, none removed (`signs.py check`: in sync). `t` is not a field of units.json (the build makes it), so nothing was retyped. Unit numbers below are 0-based positions in `sentences`, with the unit's first stele line.

## Counts
Changes: 26 entries (high 0, medium 8, low 18); the about rewrite is one of the medium ones. Findings refused or confirmed unchanged: see the second and third sections.

## What was checked on the plate (Plates 46–52, PDF 307–319, rendered at zoom 3 and cropped at zoom 6–10)
Line division: all 204 stele lines compared by script against the pinned transliteration (reading, per line, with the logograms normalised): the only differences are the logogram lines Harper writes as Akkadian (DUMU{meš} for mârê, GEME₂ for amtum, É for bît/bîtam/bîtim, SAL for zinništum/zinništim, ARAD for warad/wardim, KÙ.BABBAR for kaspim, DUMU.SAL for mârat, DUMU.UŠ/TUR.UŠ). `reading` reconstructs from the glyph `tr` for every word; every glyph index is covered by exactly one morph entry; every sign key exists.

Rows examined on the plate (sign-group count and shape against the same sign elsewhere on the plates, and against Plate 25 for ḪA.LA-šu):
- TIM vs DIM: keys TIM and DIM carry the same Unicode character (𒁴), so the choice is invisible in the built text; TIM kept (as 153-169). On the plate the tail of ḫi-ir-tim (XXVIII 54), du-tim (XXIX 67), u-ni-a-tim (XXX 50), ṣi-iḫ-ḫi-ru-tim (XXX 48) and zi-it-tim (XXVIII 59) is one and the same group (a diamond with a small box, then a long wedge), so TIM is consistent everywhere it is written.
- É vs É-tim at XXX 25 and 32: bare É confirmed. After the nested-corner É the row has ŠA (box of three lines + X-diamond), NI, IM and nothing else; both rows are identical. Bare É also confirmed at XXVIII 53 (second tier), XXIX 12, 25, 81 (bîtam: É then I-BU-ŠU), XXX 47.
- KÙ.BABBAR: bare (KÙ, BABBAR, no -im) at XXIX 2 and XXX 51; KÙ.BABBAR-šu at XXX 57 (five groups: I NA KÙ BABBAR ŠU, no -i).
- ARAD: bare at XXIX 58, 64 (be-el ARAD), XXX 5 and XXX 17 (two-tier rows: mi-iš-lam above; BE, EL, ARAD below, nothing after ARAD). The wardim/warad `say` stays a reading of the bare sign.
- DUMU.SAL (XXIX 60, 66, 71, 88; XXX 8, 20): DUMU then SAL (kite with long horizontal) then a-wi-lim, as the draft has it. DUMU.UŠ at XXVIII 58: DUMU, UŠ, DUMU, then the ḫi-ir-tim tail as at 54; confirmed.
- NU.MU.SU at XXX 22 and 55: three signs, nothing after SU; confirmed.
- GEME₂: bare. XXVIII 45 is identical, row for row, to the first tier of XXVIII 64 (which the drafter confirmed bare): A NA DUMU ME ESH ŠA SAL KUR. XXVIII 70 ends in KUR with no further sign. XXVIII 41, 74, 77 were judged by sign-group count only.
- ša/ta at XXVIII 75: the second sign is the same sign as the TA of iš-ta-ka-an (XXIX 30); TA is right, the draft's glyph stays. (The form itself stays flagged, see below.)
- MU at XXIX 10: the row has seven signs, U2 ŠA LA MU | ŠI IM MA (the two tiers), so the extra MU is on the plate and the seven glyphs stay.
- a-ba (XXVIII 53, 69): the sign after A is BA, distinct from the BI of a-bi-ša (XXIX 37); Harper's a-ba stands.
- SAL bare at XXX 43 (zinništim): after SAL the next group is ŠU; no TIM.
- ZI-IT-TIM at XXVIII 59: NOT ḪA.LA-šu (compared with Plate 25, XVI 24, where ḪA is a cross-like sign, LA a box with a hook, and the row ends in ŠU; XXVIII 59 ends in the TIM tail, not ŠU). ZI and IT match the ṣi-it of XXIX 13. One chevron-pair group between ZI and IT is not accounted for by the spelling; kept as Harper reads, now flagged UNCERTAIN in the note (see changes).

Not done: every syllabogram of every row was not identified independently at stroke level. For rows not named above I confirmed sign-group counts and the position of every logogram; the syllabic spellings follow Harper (whose normalised word the plates support wherever I looked) and the sign keys of the published parts for the same spelling, which I re-derived by script (same spelling gives the same key in 100-111 … 153-169). Harper's printed dots (XXVIII 84 ụ, 88 ṇ, XXIX 65 ṇ) were taken as type dirt as the packet says; I did not inspect them on the plate.

## Changes (unit · field · severity · what was wrong · what was done)
| unit | field | severity | what was wrong, what was done |
|---|---|---|---|
| U2 (XXVIII 50) | words[9].say | low | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U2 (XXVIII 50) | words[12].say | low | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U5 (XXVIII 66) | words[9].say | low | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U6 (XXVIII 73) | words[5].say | low | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U11 (XXIX 16) | words[10].say | low | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U16 (XXIX 47) | words[1].say | medium | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U17 (XXIX 51) | words[8].say | low | DUMU{meš} as nominative-plural subject said mārī (oblique); nominative mārū (in U16 it must agree with nominative maḫrūtum/warkūtum) |
| U2 (XXVIII 50) | n | low | note followed the say change |
| U2 (XXVIII 50) | n | low | note followed the say change |
| U2 (XXVIII 50) | n | low | added one sentence saying why the subject plural is mārū (first occurrence) |
| U6 (XXVIII 73) | n | low | note followed the say change |
| U11 (XXIX 16) | n | low | note followed the say change |
| U16 (XXIX 47) | n | medium | note followed the say change |
| U17 (XXIX 51) | n | low | note followed the say change |
| U22 (XXIX 80) | n | low | bišam -> bīšam (published gap-a/100-111/141-152 bi-ša-am = bīšam, lemma bīšum) |
| U22 (XXIX 80) | n | low | lemma spelling follows the existing glossary lemma bīšum |
| U22 (XXIX 80) | words say/morph lemma | medium | say bišam / lemma bišum (a new lemma) -> bīšam / bīšum, the lemma already in the glossary (gap-a: bīšašu); avoids a duplicate glossary entry |
| U11 (XXIX 16) | l | medium | l said "decide" while i and the house rendering (153-169 §168, iparrasūma) say investigate |
| U11 (XXIX 16) | n | low | note matched l/i |
| U28 (XXX 31) | l | medium | l said "decide" while i and the house rendering say investigate |
| U28 (XXX 31) | n | low | note matched l/i |
| U4 (XXVIII 62) | i | low | "But if ... , in his lifetime," moved the lifetime phrase to the end against the word order of l and turned u šumma into a contrast; now "And if the father, in his lifetime, has not said ..." |
| U15 (XXIX 41) | i | medium | "after that, that woman has died" read warka as an adverb and doubled "woman"; warka governs the clause (l: "after that-woman has-died") |
| U15 (XXIX 41) | n | medium | note glossed warka "afterwards" against l/i ("after that woman has died") |
| U3 (XXVIII 58) | n | low | added the honest UNCERTAIN on the zi-it-tim row (plate shows ZI, IT and the TIM tail, and no ŠU, so it is not ḪA.LA-šu as at §60; one extra sign-group between ZI and IT is unexplained) |
| about | about | medium | the old about put the widow’s dowry/marriage-gift/home/for-life under §172 (they are §171, with the estate passing to her sons), made "takes an heir’s share if no marriage-gift was ever given" part of §171’s grant, said "first husband" without the (?) the notes carry, and "record the property" for what the law says as investigate + leave a tablet; "each was read from the plate" now true only after review: reworded "checked on the plate" |

## Findings refused or confirmed unchanged (with reason)
- TIM vs DIM key: refused as a change; same glyph, same sound; precedent 153-169 uses TIM.
- É, ARAD, KÙ.BABBAR, NU.MU.SU, SAL, DUMU.SAL bare vs complemented: no change needed; plate confirms the draft (above).
- XXVIII 75 `iš-ta-ak-ka-an` normalised to `iššakkan`: kept (flagged UNCERTAIN in the note); the plate has TA, so the spelling is Harper's and the normalisation is the drafter's reading of the passive; I have no better form and the sense (release shall be set) is certain from §117's pattern.
- `iddinušim`, `ūlidušum`, `imtanūšunūti`, `iḫuzuši` (short -u), `ṣiḫḫirū`, `ḫāwirīšama` (?), `arnam immidū`, `uzaḫḫamūši`, `ikkal` as "have the use of", `DUMU.UŠ` as heir: all already marked UNCERTAIN/(?) in the notes and in `i`; no better reading exists in the allowed sources; left.
- `i` begins U1 with "and" where the Akkadian has none (asyndeton): refused; English needs the coordinator and `l` shows the plain order. Likewise "But" at U6.
- U3 `i` "take it": kept; the note already says what is chosen is not stated.
- `u-ša-la-mu-ši-im-ma` seven glyphs / say ušallamšimma: kept (the plate has the MU).
- ZI tr "ṣi" at XXIX 13 (ṣi-it-tam) vs "zi" at 59: kept, each as Harper prints it, as in 127-140 / 153-169.
- `ina zittim` at 59: not changed to ḪA.LA (plate excludes it).
- Units' `ln`/`p` placement (170, 171, 172, 173, 174, 175, 176, 177 carry ln and p; §172A and §176A carry neither, as §133A): correct; no change. Column crossing of U8 (XXVIII 88 into XXIX) is allowed in the laws.
- q not ḳ: no ḳ anywhere in units.json. No verbatim-overlap red flag against any recalled modern rendering: the `i` lines are built from the grammar (several are deliberately awkward, e.g. "lay claim against ... for slavery").

## Still uncertain (for the second pass / the owner)
- XXVIII 59 zi-it-tim: one unexplained sign-group on the plate.
- GEME₂ at XXVIII 41, 74, 77 not individually dissected; syllabograms not identified at stroke level (see "Not done").
- The nominative/oblique choice for DUMU{meš} (mārū / mārī) is grammar, not the plate; the published parts use mārī almost everywhere, so a project-wide decision is wanted (the glosser should note that mārum has both forms).
- The §172 protasis/apodosis division and the sense of emēdum arnam (the sons "are in the wrong") rest on Harper's glossary only.
- Glosser: the draft's 12 new lemmas are now 11 (bīšum already exists, gap-a: "movable property, goods": broaden with "bīšam iršû, Harper BISU" if wanted).

# Review (pass 2) — hammurabi-laws-170-177

Second adversarial pass: every gloss.json entry against units.json and against the glossaries of the published parts (all fourteen, prologue to 153-169, by script); the notes' grammar labels, l/i, house renderings re-read for every unit.

## Changes
| where | severity | what was wrong, what was done |
|---|---|---|
| gloss.json `bišum` | medium | a duplicate of the existing lemma `bīšum` (units already use bīšum since pass 1); entry dropped. The new-lemma list is now exactly the 11 absent from earlier glossaries: almattum, bultum, emēdum, emēdum-N, gadum, nudunnûm, panûm, unūtum, wardūtum, warkûm, zaḫāmum-D |
| units U31 morph | medium | lemma `šâmum-buy` (not in any glossary, so a spurious new lemma and no gloss); the published parts (26-41, gap-a) use lemma `šâmum` ("to buy: ištām, išammu"); changed |
| gloss.json `__broaden__` warkatum, erēbum, ragāmum, šakānum, leqûm | high (build rule) | the glosser's "old entry" was not the latest holder's text (older or paraphrased bases), so the entries did not begin with the old entry whole; rebuilt by script as latest published entry + ' · ' + new reading (checked by script: every broaden begins with latest holder's text + ' · ') |
| `__broaden__` walādum, alākum | low | nothing new: ittalad, ūlidušum, ūlissum, ittalku, ittalak are all already in the latest entries; both broadenings dropped |
| `__broaden__` mutum | low | new part repeated mussa/mut (already in old); now only mutiša panîm / warkîm |
| `__broaden__` rabûm-D, maḫrûm, ḫīrtum | low | trimmed to the new reading; "feminine plural, nominative" for maḫrūtum removed (see warkûm) |
| gloss.json nudunnûm | low | stray "also the noun of the same word in the dowry laws" removed |
| gloss.json warkûm | medium | warkūtum called "plural feminine, nominative"; the note and gloss now say only "plural in -ūtum" (the agreement with mārū is not claimed) |
| U27 `mārīša` -> `mārūša` | medium | DUMU{meš}-ša is the subject of ṣiḫḫirū ("whose children are small"); pass 1 had missed it; now nominative like the other subject plurals; note says so |
| U16 note | medium | pass 1 left "mārī maḫrūtum u warkūtum" in the note against the changed say (mārū); corrected, and "agreeing with the nominative" replaced by a neutral statement about the -ūtum forms |

## Checked and left
- Remaining mārī in units are accusative objects (ūlissum, ittalad, lā ittalad), or after a preposition or in the genitive (ana, itti, mār-, ša … almattim); mārūa (U1, U4) is the quoted nominative "my sons".
- Lemmas -ia, paqādum, šubtum already have glossary entries (1-10, litany): no new entries needed.
- Glosses of the 11 new lemmas read against the text: forms, spellings, case labels agree with the units (bultišu, wardūtim, nudunnam/nu-du-un-na-am, uzaḫḫamūši, immidū, innemdū, warkîm/warkūtum, gadum, almattum/almattim, panîm, unīātim/unūt). The uncertainties are marked UNCERTAIN as in the notes. Wording of mutum, ḫīrtum, warkatum additions now follows the house format.
- l <-> i, remembered English, house renderings (mut libbiša iḫḫazzi, ītelli, itâr, ina ša … lā īšu, ana šīmtim ittalku, ṭuppam ušezzibūšunūti) re-read for every unit: consistent with conventions.md and the earlier parts; no further change.
- Refused: no change to ṣiḫḫirū/ṣeḫrum (kept UNCERTAIN); no change to the i of U1 "and" (as pass 1).

## Decision: mārū vs mārī
The premise (earlier parts "mostly write mārī even for subjects") is not borne out by the published text: mārī is used there for accusative/oblique plurals (ša mārī ūlidušum, mārī ūlissum, ana mārī), and the SUBJECT plural is written nominative: 127-140 "mārū warki abišunu illakū", 141-152 "mārūša ul ibaqqarūši", 153-169 "mārū ana ummātim ul izuzzū" (and 52-65 "mārū ugārim"); the 153-169 glossary entry for mārum already says "mārū (DUMU{meš}) 'sons' as subject" and "mārūša … nominative plural". So mārū for subjects is the latest published practice and correct `say`; kept, and extended to U27. No clash with glossary lemmas (lemma is mārum; forms are listed inside the entry). Note for QUESTIONS.md in questions-draft.md.
