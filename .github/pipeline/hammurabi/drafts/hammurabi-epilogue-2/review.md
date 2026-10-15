# Review (pass 1) — hammurabi-epilogue-2 (Col. XLI 75 – XLII 97)

Reviewer: adversarial pass 1. Edited `units.json` in place by script (json load/modify/dump, `ensure_ascii=False`, indent 1; the untouched file round-trips byte-identically). `python3 ../run3/signs.py check`: in sync (no sign added or changed). Nothing committed, built or published; no file touched but `units.json` and this one.

## Counts

Edits (one entry per field changed): **31** — high 1, medium 14, low 16. Several entries are one finding touching `l`/`i`/note/`say` together (distinct findings: about 20).

Plus one **high** finding that is not an edit to `units.json` and that blocks the validator (see "Line division", F1 below): the pinned source has no stele line XLII 9, the plate does.

## What I did on the plates

Method: Harper’s plates 75–78 (PDF pp. 365, 367, 369, 371) rendered at zoom 6–12 with `page.py` and my own crops; every ruled row from XLI 75 to XLII 97 (and the first row of XLII 98) viewed; rows counted against Harper’s numerals; Harper’s List of Signs (PDF pp. 383–411) read for the signs named below; Harper’s printed transliteration page (PDF p. 122 = his p. 102) viewed; Harper’s glossary (PDF pp. 168–212, text layer) searched for every entry the notes cite; Harper’s Index of Sumerograms (p. 212) for PA.TE.SI. The validator cannot run before the build, so I reproduced its line check by script.

**Confirmed on the plate:**
- **Line division, the whole part.** Rows from XLI 75 to XLII 97 match the units’ lines one for one; the markers 80, 85, 90, 95 (XLI), 100, and 5, 10, 15, 20, 25, 30 (XLII), 35 … 75 (XLII) fall on the rows the division gives them; sub-rows (the “{b}” ends of lines) sit exactly where the notes say: XLI 77, 79; XLII 1, 2, 4, 6, 17, 18, 36, 44, 52, 54, 59, 63, 70, 74 (and XLI 104/105, below). The next row after our last line, XLII 98, begins with the star of {d}EN.KI, so the part boundary is right.
- **XLII 5–10 (flagged).** Plate 76, left column: rows 5 i-gul-ma · 6 di-ni la u-ša-az-zi-iq (with a sub-row) · 7 a-wa-ti-ia · 8 la uš-te-pi-el · 9 u-zu-ra-ti-ia · 10 la u-na-ki-ir — six rows for lines 5–10. Row 7 is, sign for sign, the row of XLII 29 (a-wa-ti-ia); row 8 is the row of XLII 30 (uš-te-pi-el) with one extra sign (LA) in front; row 9 begins with the same hatched box and ZU as XLII 31 (u-zu-ra-ti-ia). Harper’s own glossary cites uš-te-pi-el at xlii 8 and 30 and uṣurtu (u-zu-ra-ti-ia) at xlii 9 and 31. The drafter’s division is right; Harper’s print (a-wa-ti-ia la uš-te-pi-el as one line) is the one that is a divider short.
- **XLI 103–105 (flagged).** Rows 103 (e-la a-na la-ḫa) and then one ruled box with two half-height rows: ZI-IM.RI.GA (four large signs) above, a-na im-ki-im below. Harper’s printed page prints the numeral 105 immediately before a-na im-ki-im, right after “ZI-IM. / RI.GA”, so ZI-IM.RI.GA is 104 and the box holds lines 104 and 105. Confirmed, and now said in the note.
- **XLII 79–80 (flagged).** Row 79 (i-na pî-šu kab-tim) and row 80 (li-iq-bi: three signs with wide gaps) are two ruled rows; the numeral 80 sits on the second. Nothing to change but the note’s wording (the “faint scan” remark was the transcriber’s, not Harper’s).
- **Sumerograms and the odd signs**: the star AN + UD for Šamaš (XLI 97, XLII 14; List no. 148 has the group); LUGAL (XLI 96, XLII 13, 40); EN (XLII 41; List no. 49); DINGIR, the star alone (XLII 45); PA.TE.SI (XLII 42: PA, TE, SI; Index of Sumerograms “PA.TE.SI, 42, 42”); NI.NI = ilī at XLII 25 and 46 (two big triangles; List no. 99 “ili”; Harper’s glossary lists NI.NI at 42, 25 and 46); GIŠ.PA (XLII 14, 50; List no. 108 “ḫattu”); BAL (XLII 47, 64: three pieces, as List no. 7 “palû”); ME.LAM (XLII 48: ME + LAM; List no. 184 “melammu”); URU (XLII 73; List no. 85); KA (XLII 79, 95); É.KUR (XLII 84; List “E.KUR”); AMA (XLII 82: the box with a star inside; List no. 102 “ummu”); NIN (XLII 81, 85: the diamond with a triangle in it); KID (XLII 53, 81, 89, 95: the same hatched box in all four); {d}EN.LÍL = star + EN + KID (XLII 53, 89, 95; List no. 49 “Bêl” is exactly this group); GIR2 in na-piš-ti-šu (XLII 93: List no. 134 “kir, piš”, the 𒄈 sign); GUL (XLI 79, XLII 5: ◁ + hatched box; List no. 164 “gul, kul”); DUR (XLII 26: List no. 53 “dur”); IN (XLI 81 etc.: chevrons + big triangle; List no. 73); DI (the diamond with a hook; List no. 175).
- **Line check, aligned.** The drafter’s division has 128 written lines against Harper’s 127 (the missing 9). With Harper’s line 9 inserted by hand, the validator’s own ratio test flags 11 lines under 0.75: XLI 97 (šaUTU…), XLII 14, 40, 41, 45, 50, 73, 81, 82, 85, 95 — every one a logogram Harper writes as the Akkadian word (Šamaš, šarrum, bêlum, ilum, ḫaṭṭi, ali, Bêlit, ummum, bêltum, Bêl) and every one confirmed on the plate as above. (Unaligned, the validator’s own list is meaningless after XLII 9; do not read it.)

**Not done:** every syllabogram of all 128 lines was not matched shape by shape against the List of Signs. I counted sign groups per row and compared recurring signs across rows (the same words recur: a-wa-ti-ia, uš-te-pi-el, u-zu-ra-ti-ia, ša i-na na-ru-ia aš-tu-ru, mi-ša-ri-im, LI, KI, ZU, NI.NI, KID …) and they agree; where a sign is built of several pieces (LI = chevrons + hatch + a bow; TAG šum; IN; ME.LAM; BAL; NIN) group counts are only approximate. No reading was changed on the plate’s evidence alone. Sign values were not re-derived from Unicode shape; the keys are the glossary’s, already used in published parts (the only new (sign, tr) pairs are GUL gul, DUR2 dur, BAL BALA, AMA AMA, GIR2 piš, all checked above). `reading` was rebuilt from the glyphs’ `tr` by script for all 32 units: no mismatch. Every unit’s morph indices were checked for coverage of the glyphs: two broken words found and fixed (below).

## Line division — finding F1 (high, for the lead; no change made to `units.json`)

The drafter’s division is plate-true and agrees with Harper’s numerals from XLII 10 on, but it has one stele line (XLII 9, u-zu-ra-ti-ia) that the pinned source `source/hammurabi-harper1904-source.json` does not have: the source runs XLII 7 “a-wa-ti-ia la uš-te-pi-el”, 8 “u-zu-ra-ti-ia”, 10 “la u-na-ki-ir”. The validator zips the units’ lines with the source’s lines (`parts.json`: from 2486 to 2612, 127 lines), so as drafted it will report “units cover 128 stele lines, the part has 127” and “unit 14: starts at XLII 11, but the next stele line is XLII 12” (and so on to unit 31). I could not and did not touch the source, `parts.json` or `hooks.py`. Options, for the lead: (a) amend the pinned source (split line 7, insert line 9, `lines` 128, new sha256 in `parts.json`; the later epilogue parts then shift by one in `from`/`to`); (b) special-case XLII 5–9 in the validator; (c) if nothing may change, fold the part back to Harper’s own division: put awâtīya + lā uštepiel on one written line (7) and u-zu-ra-ti-ia on line 8, so unit 13 has four lines (6, 7, 8, 10) — then the validator passes, the notes (which already describe the plate) must be reworded, and the display shows a divider where the stone has none. I recommend (a). The same applies to XLIII 70–74, which the conventions already list as a provisional spot.

## Changes

Unit numbers are 0-based positions in `units.json`, with the stele line.

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| #2 (xli 80) | n | medium | Note said the word at xli 68 “is addinu (nadānum)” as if settled and did not say that Harper’s glossary files all three occurrences (41,69; 41,81; 42,27) under dânum; the two parts disagree and the reader was not told. | replaced |
| #5 (xli 88) | l | medium | `l`/`i` gave “decisions” (plural) for pu-ru-za-ši-na, but Harper’s glossary enters pu-ru-za-ši-na (41,89) beside pu-ru-za-am (§6), the accusative singular purussâm (published `say` purussâm in laws 1-10); it is the singular with a suffix, parallel to the singular dīnšina in the line before. | their-case let-him-judge, their-decisions let-him-decide. -> their-case let-him-judge, their-decision let-him-decide. |
| #5 (xli 88) | i | medium | Follows `l`: singular “decision”, as dīnšina is singular. | let him judge their case, let him decide their decisions. -> let him judge their case, let him decide their decision. |
| #5 (xli 88) | n | medium | Label error: “in the plural, purussā-”. The form is the accusative singular + suffix (Harper’s glossary, §6 parallel). | replaced |
| #5 (xli 88) | words[2].say | medium | purussāšina (macron) is not the house spelling of the accusative singular of purussûm (laws 1-10 has purussâm). | purussāšina -> purussâšina |
| #8 (xli 95) | l | low | `l` “has-given” suggests a perfect; išrukušum is the preterite išruk(u) + šum (the note and `i` say “gave”). | Hammurabi, king of-justice, to-whom Shamash truths has-given, I(-am). -> Hammurabi, king of-justice, to-whom Shamash truths gave, I(-am). |
| #8 (xli 95) | n | low | The note called kīnātim the plural of kīnum “firm”, but the lemma (and the litany) is kittum; row reference widened to 96–98 though the star is in row 97. | replaced |
| #10 (xli 103) | n | low | Line division for 104/105 rested on the plate alone; Harper’s own numerals support it (checked on his printed page, p. 102). | replaced |
| #11 (xlii 1) | n | low | Harper’s reading is superseded in the lexicon (tanittum “praise”); the house rule is to keep Harper as base and flag the modern understanding. | replaced |
| #14 (xlii 11) | n | medium | Unsupported grammar claim (“the OB D precative would be lurrik”) that the same text contradicts (lilemmin, lišappiḫaššum, lišaškin are all li- + D/Š); it also cast doubt on a form Harper lists as arāku II,1. | replaced |
| #16 (xlii 18) | n | low | Plate fact missing: row 19 is partly drawn in outline (damage), as the reader of the plate would see. | replaced |
| #17 (xlii 22) | n | low | irrit/irrītim inconsistency in one noun; sign evidence added. | replaced |
| #17 (xlii 22) | words[4].say | low | irrit (short) against irrītīya/irrītim (long) for one noun; the construct keeps the long ī as kibīt does in epilogue-1. | irrit -> irrīt |
| #19 (xlii 33) | l | low | “has-had-take” is not a gloss of the Š of aḫāzum; “made take” is. | my-name inscribed he-has-erased-and, his-name he-has-written-out; because-of those curses another-indeed he-has-had-take, -> my-name inscribed he-has-erased-and, his-name he-has-written-out; because-of those curses another-indeed he-has-made-take, |
| #19 (xlii 33) | i | medium | “has had someone else take it up” supplied an object (“it”) and a phrase (“take up”) the grammar does not give; rebuilt: aššum … šaniamma uštaḫiz = “because of those curses, another one, he has made take”. The note already says the sense is the drafter’s inference. | has erased my inscribed name and written out his own name; and because of those curses has had someone else take it up (?), -> has erased my inscribed name and written out his own name; and because of those curses has made another one take (it) (?), |
| #19 (xlii 33) | words[8].morph | medium | šaniamma: lemma šanûm covered glyphs 0-2 and -ma covered glyph 3 (AM); MA (glyph 4) belonged to nothing, so the form was mis-segmented in the word display. | šanûm g [0,1,2] -> [0,1,2,3]; -ma g [3] -> [4] |
| #20 (xlii 39) | l | low | `l` “ruler” against `i` “governor” for patesi. | that-man, whether king or lord or ruler or any-person who a-name is-called, -> that-man, whether king or lord or governor or any-person who a-name is-called, |
| #21 (xlii 45) | words[5].say | high | `say` palê dropped the suffix -ya (BALA-ia = palêya, “my reign”, as the note says); the spoken line would lose a syllable and the sense “my”. | palê -> palêya |
| #23 (xlii 53) | n | low | kibissu (short) against kibīssa at xlii 83 and kibīt in epilogue-1: one noun, one vowel length. | replaced |
| #23 (xlii 53) | n | low | Evidence from Harper’s glossary and list added to the Ellil naming. | replaced |
| #23 (xlii 53) | words[5].say | low | kibissu -> kibīssu, as kibīssa (xlii 83) and kibīt (epilogue-1). | kibissu -> kibīssu |
| #25 (xlii 64) | i | medium | “death at the glance of an eye” put in a preposition (“at”) that the construct chain mūt nīṭil īnim does not contain (“death of a glance of the eye”); the note says it is kept literal and the force UNCERTAIN, so `i` must not interpret. `l` was already literal. | A reign of sighing, few days, years of famine, darkness without light, death at the glance of an eye — -> A reign of sighing, few days, years of famine, darkness without light, death of a glance of the eye (?) — |
| #27 (xlii 73) | n | medium | False statement about the source: Harper’s glossary lists šu-bi-lam (42,75) under abalu III,1 “to bring, to take away, to transport”. | replaced |
| #27 (xlii 73) | n | medium | Note said lā šubšâm is “the usual way to say a thing is not to exist” — an unsupported idiom that drops the causative Š. | replaced |
| #27 (xlii 73) | i | medium | “not exist” lost the Š-stem’s causative force (šubšâm = “to cause to be”, lā šubšâm “not to bring into being”). | the ruin of his city, the scattering of his people, the carrying off (?) of his kingship, and that his name and his memory not exist in the land — -> the ruin of his city, the scattering of his people, the carrying off (?) of his kingship, and that his name and his memory not be brought into being in the land — |
| #28 (xlii 79) | n | low | The transcriber’s remark about a faint scan was worded as if it were Harper’s own divider habit; the plate settles it (checked). | replaced |
| #29 (xlii 81) | n | medium | Note said Harper “gives only Bêlit” and called the NIN.LÍL reading tentative; Harper’s glossary enters BELIT [NIN.LIL] at xlii 81. | replaced |
| about | about | low | The plate shows the signs whole; the stretch is unread because Harper gives bare signs, not because the stone is damaged. | replaced |
| about | about | low | The curses are wishes (li- precatives), not statements; “gods” for two gods and a goddess. | replaced |
| about | about | low | The Ellil group is Harper’s own (list no. 49, glossary); only the name Bēlit is a convention. | replaced |
| #30 (xlii 87) | words[7].morph | medium | awāssu: lemma awātum covered glyph 0 only and -šu covered glyph 1 (WA), leaving ZU (glyph 2) unassigned; the suffix is the ss written with ZU, so awātum = A+PI, -šu = ZU. | awātum g [0] -> [0,1]; -šu g [1] -> [2] |

## Verdicts on the drafter’s flagged lemma decisions

- **adīnu = diānum, not addinu (XLI 81, XLII 27).** Kept. Harper’s glossary enters a-di-nu at 41, 69 / 41, 81 / 42, 27 under DANU “to judge, to determine, to decide” (the same entry holds i-di-in, li-di-in, a-di-in); dīn adīnu is then verb and cognate noun, as dīnam idīn (§5); one d in a-di-nu cannot decide, but the grouping does. The published epilogue-1 read the same word at xli 68 as addinu (nadānum); the English is the same (“the verdicts that I gave”), and this part now says so in the note. **For the lead:** epilogue-1’s lemma at that line (`nadānum`) and note are inconsistent with this part; the pass-2 reviewer / owner should decide whether to change the published part (not touched here), and QUESTIONS.md should carry it.
- **qâlum (liqūlma XLI 79, iqūlma XLII 5, 22).** Kept. Harper has ḲALU I,1 “to give attention to: i-gul 42, 5, 22; li-gul 41, 79”; the plate sign is the ◁ + hatched box of List no. 164 (gul, kul); the root and vowels are not settled and the note says UNCERTAIN.
- **bêlum-Š (uštepiel XLII 8, 30).** Kept, uncertain. Harper’s glossary: BELU III,1 “to overrule: us-te-pi-el, 42, 8, 30”. The spelling uš-te-pi-el is unexplained: in XLII 6–10 it stands among preterites (ušazziq, unakkir), in XLII 27–32 among perfects (uptassis, uttakkir), so no tense is asserted. The lemma name looks like bēlum “lord”: the glosser must say in the entry that it is not the noun.
- **lirrik (XLII 15).** Kept as arākum-D (Harper ARIKU II,1 “to prolong: li-ir-ri-ik 42, 15”). The note’s remark that the OB precative “would be lurrik” was dropped (see table): this text writes li- before every D and Š stem.
- **lirʾi (XLII 17).** Kept as rêʾûm “to pasture” (lemma `rêʾûm-pasture`), uncertain. Harper has ARU II,1 “to carry, to rule: li-ri 42, 17; li-ru-su 44, 23” (a different verb); “shepherd his people in justice” fits the litany’s shepherd, but the spelling li-ri (no second vowel or sign for the ʾ) is unexplained; flagged in the note.
- **Bēlit and NIN.LÍL (XLII 81).** Kept: `say`/lemma Bēlit (Harper’s reading), glyphs star + NIN + KID. The note was wrong that Harper “gives only Bêlit”: his glossary has BELIT [NIN.LIL], goddess, consort of Bel, 42, 81 (and BEL [EN.LIL] at 42, 53, 89, 95). Note corrected; modern name Ninlil mentioned there. NIN here (XLII 81, 85) is a diamond with a triangle inside; I found no separate NIN entry in Harper’s List of Signs (List no. 31 “šir” is a related shape), so NIN stays the glossary key used for NIN.AN in the laws.
- **na-piš-ti-šu with GIR2 (XLII 93).** Confirmed: List no. 134 “kir, piš”; the plate sign is the same (a ▤ + ⋖ shape); the key GIR2 with tr piš is right.

## Findings refused or left as drafted (with the reason)

- **#28 `i` “may he speak all this”**: the “all this” supplies an object that liqbi does not have; left, because the note says exactly this (the verb carries the whole list from xlii 73) and English needs an object. Pass 2 may prefer “may he say it”.
- **#10 `i` “Except [for la-ḫa ZI-IM.RI.GA, which I cannot read]; for the wise (?) …”**: left. Peiser’s footnote is quoted, Harper gives bare signs, ēla “except” is a spelling guess and is marked as one; im-ki-im keeps Harper’s spelling and his “(?)”. Harper’s glossary enters im-kum “wise” (4, 7) and then IM-KI-IM (?) separately at 41, 105, so “imqim” is the drafter’s suggestion, not Harper’s, and the note says so.
- **#11 tanādātim / šuṣâ**: left with Harper’s “might” as the base; the lexicon’s tanittum was only added as a flag (table).
- **p flags**: only XLI 75, XLII 2, XLII 18 carry `p`. A reader might want one at XLI 95 (the king names himself) and at XLII 53, 81 (a new deity); left, since the epilogue convention is “only at a new paragraph of sense” and that is a taste call.
- **tēšī (XLII 59, `say`)**: the case ending of tēšûm in the construct is unknown; Harper’s te-ši is all there is; macron left.
- **purussê (XLI 82, `say`)**: kept as the oblique plural, as epilogue-1 has it at XLI 70; Harper’s glossary lists it with pu-ru-zi-im and pu-ru-za-am (singulars), so singular is possible; the English “decisions of the land” (plural) and “verdict” (singular) in the same sentence are the part before’s choice.
- **AS for two shapes**: the plate has the single-wedge aš (List no. 1; aš-ṭuru XLI 79, XLII 4, 21, aš-šum XLII 36, li-ša-aš-ki-in XLII 97) and the three-bar aš (List no. 131; na-aš-qa₂ XLI 99, na-aš-pu-uḫ XLII 74). The house keys both to AS (epilogue-1 does the same at na-aš-qa₂); left.
- **`iṣūtim` “few”**: Harper has only “small”; “few” fits the context and the usual sense; left.
- **ilum (XLII 45) = the AN sign, god not named**: left as the drafter’s note says (title “great god, father of the gods” suggests Anum, flagged as inference).
- **litēršu (XLII 49)**: left UNCERTAIN as drafted; Harper files li-te-ir(-šu) under TARU II,1 “to return, restore” (42, 49; 43, 4, 80, 89; 44, 1, 44, 46). The same verb recurs through the next epilogue parts: whatever is chosen here must be kept there.
- **Hammurabi “king of justice” rendering, “the black-headed people”, “the fief-duty” etc.**: all match conventions.md house renderings; nothing to change.

## Disclosure (sole-source rule)

No modern translation was opened. While probing the PDF text layer I printed the first 80 characters of PDF pp. 118–135 in one command, and a later search printed a snippet of p. 119; they showed fragments of **Harper’s own 1904 English translation** of this and neighbouring passages (the first words of its rendering of the “if that man” clause, of the Bêl curse, of the later curses, and a phrase of the prologue). I did not use them, and none of my edits to `i` follows them (the edits are rebuilt from the grammar: “their decision”, “made another one take”, “death of a glance of the eye (?)”, “not be brought into being”). Harper’s glossary (pp. 168–212) was used for the entries named in the notes and in this review; Harper’s List of Signs for sign identities. The tanittum remark in #11 is from my memory of the standard lexicon and is labelled as such in the note.

## Points for the glosser and pass 2

- New lemmas: qâlum, kibsum, ṣalmum-black, ela, laḫa, ZI.IM.RI.GA, tanādātum, bêlum-Š (not the noun bēlum), arākum-D, irritum (construct irrīt), mašûm, adārum, pasāsum-D, pašāṭum, patesi, awīlūtum, palûm (BALA; palêya), arārum, šâmum-D, rabûm-Š, tēšûm, šabûm-D, raḫlum, tanēḫum, iṣûm, ḫušaḫḫum, ekletum, mūtum (death, not mutum “husband”), nīṭilum, sapāḫum-N, Bēlit, kabātum, šipṭum, lemēnum-D, lapātum-Š, tabākum, šakānum-Š. Check each against the text; Sonnet invents forms.
- Broaden: `diānum` (adīnu in dīn adīnu), `purussûm` (accusative singular + suffix, purussâšina; oblique purussê / genitive purussîm), `kittum` (plural kīnātim), `Enlil` (say Ellil; sign group star + EN + KID, Harper’s Bêl), `emqum` (im-ki-im, imqim (?)), `ilum` (DINGIR alone, and NI.NI = ilī), `bēltum` (NIN), `egirrûm` (igirrīya, “my igirrû”), `kibītum` (kibīssu, kibīssa, ssu/ssa written ZU/ZA), `rêʾûm-pasture` (lirʾi, precative), `wabālum-Š` (šūbilam — Harper does enter it, abalu III,1), `bašûm-Š` (šubšâm), `nasāḫum` (lissuḫ), `ḫaṭṭum` (GIŠ.PA), `ūmum` (UD = ūmī), `qātum` (qāssu).
- The line-count problem F1 above will stop `R3 build`/`validate`; the units are right, the source is a line short.
- No `{b}` sub-row marking exists in the units (as in epilogue-1); the notes say where sub-rows are.
- XLII 19 is partly drawn in outline on the plate (damage); XLII 53/89/95 (Ellil) and 81 (Bēlit) share one KID sign; XLII 25 and 46 share NI.NI.


---

# Review (pass 2) — hammurabi-epilogue-2 (Col. XLI 75 – XLII 97)

Reviewer: adversarial pass 2, on the strongest model. Edited `units.json` and `gloss.json` in place by script (json load/modify/dump, `ensure_ascii=False`, indent 1; both files round-trip byte-identically before the edit and keep their no-trailing-newline state). `python3 ../run3/signs.py check`: in sync (no sign added or changed). Nothing committed, built or published; no file touched but `units.json`, `gloss.json` and this one. Not reopened: the XLII 6 division (unit 13 follows Harper's four lines 6, 7, 8, 10; its note says the plate has five rows).

## Counts

Entries (one per field or glossary entry changed): **49** — high 0, medium 15, low 34.
- `units.json`: 23 (medium 7, low 16).
- `gloss.json`: 26 (medium 8, low 18): 7 plain entries corrected, 4 `__broaden__` entries corrected, 15 `__broaden__` entries added (the glosser had broadened 18 lemmas and missed 15 more whose latest published entry does not cover this part’s use).

## What I checked

- **Text pass.** Every note's grammar label read against the form, original → `l` word by word, `l` ↔ `i`, consistency with epilogue-1 (re-read in full: xl 79–80, xli 12, 62, 68, 73 and the rest of the cross-references the notes make) and with the litany/prologue; q-not-ḳ (no ḳ/Ḳ anywhere in either file); NFC; `say` against `reading` for all 243 words; glyph coverage by morph for every word (no gaps); `col`/`line`/`ln` of every unit against the pinned source (all 127 stele lines consumed one for one; with the XLII 6 unit as it now stands, the validator's zip of units and source lines agrees).
- **Source line compare.** Readings line by line against the pinned transliteration, with the unit lines zipped to the 127 source lines: the only differences are the logograms and determinatives Harper writes as the Akkadian word (listed by the validator) plus ga→qa₂, ḳ→q, `{b}`/`{1}` markers, and ù for Harper's u. No other difference.
- **Harper's glossary** (PDF text layer pp. 167–214, searched form by form): every form in the part was looked up; every "Harper's X n,m" claim in the notes and in gloss.json was compared with the entry. Confirmed: kibsu, ṣalmu, taṣimtu, ḲALU, DANU (a-di-nu 41,69 / 41,81 / 42,27; li-di-in 41,88), PURUSSU (pu-ru-za-ši-na 41,89, pu-ru-zi-im 42,88, pu-ru-zi-e), PARASU, ARIKU II,1, ARU II,1, IRRITU, MASU I,1, ADARU, PASASU II,2, PASATU I,1, AWILUTU, NABU I,1, BELU III,1, USURTU (41,73; 42,9, 31), ILU/NI.NI (42,25, 46), MELAMMU, SAMU I,1/II,1, KIBITU (42,55, 83), RABU III,1, TARU II,1 (li-te-ir-su 42,49), ARARU I,1, SABARU I,1, TESU, ŠABU II,1, SAPAHU II,1 / IV,1, SUBTU, ISU, SUSAHU, EKLITU, NITLU, MUTU, TANEHU, TANATU, ASU III,1 (su-sa-a 42,1), BASU III,1 (su-ub-sa-a-am 42,78), ABALU III,1 (su-bi-lam 42,75), SAKANU III,1 (li-sa-as-ki-in 42,97), LAPATU III,1, LIMENU II,1, DAMAKU II,1, KABATU I,1, SIPTU, ZIKRU, all as the notes say except the findings below.
- **Gloss bases.** All 33 `__broaden__` bases (18 original + 15 added) checked by script against the latest published holder in reading order (`publishedBefore` prologue, litany, laws 1–10, 11–25, 26–41; then parts.json order, gap-a and gap-b after laws-52-65): each new text is the old entry whole + " · " + the addition. Reproduced `merged_inline_glossary` order; all 37 new lemmas have a top-level entry, none is missing or superfluous. diānum (laws 1–10), kittum and emqum (litany) have their base outside parts.json: right by the `publishedBefore` order.
- **Plates.** Beyond pass 1: rows of plate 75 (XLI 75–80), plate 77 left (XLII 35–39) and right (XLII 56–60) viewed at zoom 5–6 against the sign counts; plates 76 and 77 viewed whole. Nothing contradicts a reading; but I could not match individual syllabograms reliably by eye at that size, so this is a consistency check on sign-group counts and recurring words (a-wa-ti-ia, uš-te-pi-el, u-zu-ra-ti-ia, šum-ma a-wi-lum šu-u, ša i-na na-ru-ia aš-tu-ru, NI.NI, KID, LI), not a shape-by-shape proof. Harper's own print (ra-be-tum, ik-li-it, na-wa-ri-im, šu-ub-ša-a-am, i-me-eš-ma) agrees with the units wherever Harper's glossary headword spells differently (ra-bi-tum, ek-li-it, nu-wu-ri-im, su-ub-sa-a-am).

## Changes — `units.json`

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| about | about | low | Said the three lines 7, 8, 9 are separate on the plate, but the text now follows Harper's four lines; a reader of the text would not know. | Added: the text keeps his division (7 both words on one written line, 8, then 10). |
| #10 (xli 103) | n | low | "imqim" is not a form of emqum (genitive emqim); the litany spells im-qum and says emqum. | emqim, with the litany cross-reference and IM = em. |
| #11 (xlii 1) | n | medium | Misnamed grammar: "tanādātim, the plural of tanittum" — tanādātum is its own word (the lexicon remark is from memory and labelled so). | "later dictionaries have a word tanādātum “praise, glory”, which the spelling would also fit". |
| #13 (xlii 6) | n | low | "ay ušazziq, xli 73": that word is on xli 74 (source line 74; Harper's glossary u-sa-zi-ik 41,74). | xli 74. |
| #13 (xlii 6) | n | low | "five lines are numbered between 5 and 10": between 5 and 10 there are four numerals; the five lines are 6–10. | "lines 6 to 10 are five lines, but only four pieces of text are printed for them". |
| #17 (xlii 22) | n | medium | "the e is his normalization" is false (Harper prints i-me-eš in text and glossary) and hides that imēš is not the regular preterite of mašûm (imši). | Said so; form marked UNCERTAIN. |
| #19 (xlii 33) | n | medium | Attributed to Harper "sadaru I,2" for ištadar: Harper files is-ta-dar (42,35) and i-sa-ad-dar under ŠATARU "to write" (I,2). The sadārum of laws 100–111 rests on a SA sign this word does not have; šaṭārum is also the verb of ašṭuru and of šaṭram just before. | Note rebuilt: perfect of šaṭārum, Harper's grouping, DAR read dar as in išaddar (ištaṭar named as the grammatical form), sadārum explained. |
| #19 | words[ištadar].morph.lemma | medium | Lemma sadārum, see above. | sadārum -> šaṭārum (`say` ištadar kept: house policy dar, as išaddar in laws 26–41). |
| #19 | n | low | “his own name he has written out” followed the sadārum reading. | “… he has written”. |
| #19 | l | low | “he-has-written-out”. | he-has-written. |
| #19 | i | low | “written out his own name”. | written his own name. |
| #19 | n | low | šināti glossed “these”; `l` and `i` say “those” (šināti is the oblique 3rd fem. pl. pronoun used as “those”). | “those”, in two places of the note. |
| #21 (xlii 45) | words[abu].say | medium | `say` abum (with mimation) for a-bu before a genitive (abu ilī); Harper lists a-bu (42,46) separately from a-bu-um; the spoken line should have the construct. | abum -> abu. |
| #21 | n | low | "abu is abum" without saying it is the form before a genitive. | added. |
| #22 (xlii 50) | n | low | "where the same man was to have it lengthened": xlii 14 is the obedient man, here it is the cursed man. | "the obedient man". |
| #24 (xlii 59) | i | low | “cannot be put down” is an idiom Harper's “to control” (and `l` “to-be-controlled”) does not give. | “cannot be controlled (?)”. |
| #24 | n | low | lišappiḫaššum parsed li- + D + -šum, dropping the ventive -am (the m assimilates: -aš-šum). | added. |
| #25 (xlii 64) | n | low | Said “iklit” while `say` and the glossary have eklit. | eklit. |
| #25 | n | low | “all in the accusative”: the construct forms (palê, mūt, nīṭil …) show no case. | “all objects of lišīmšum (most of the endings show no case)”. |
| #27 (xlii 73) | i | medium | “memory” renders zikrum, which `l` has as “mention” and Harper as “name, vow”; “memory” is the remembered curse formula, not the word. | “his name and mention of him”. |
| #27 | n | medium | Quoted Harper as saying sapahu IV,1 is “to be dispersed”: Harper gives no sense at IV,1; the entry is “to disperse, to drive out” (II,1). | Rewritten without the quote. |
| #28 (xlii 79) | i | low | “may he speak all this” supplies an object in plain type (pass 1 left it as a possible change). | “may he say (all this) …”: supplied words in brackets. |
| #29 (xlii 81) | n | low | “Harper’s ra-bi-tum”: his glossary has it, his print and the unit have ra-be-tum. | both said. |

## Changes — `gloss.json`

| entry | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| irritum | entry | low | “because of these curses”: `l`/`i` say “those”. | those. |
| mašûm | entry | low | “preterite” stated flatly for imēš (see #17). | UNCERTAIN, regular form imši. |
| tēšûm | entry | medium | “uproar” invented (Harper: “revolt”). | removed. |
| šabûm-D | entry | low | Stem not named. | “D-stem of Harper’s šabu (II,1 …)”. |
| sapāḫum-N | entry | medium | Quoted Harper as “to be dispersed” (no such sense at IV,1). | Harper lists na-aš-pu-uḫ under “to disperse, to drive out”. |
| tabākum | entry | low | “Harper’s tabaku”: his headword is the noun TABKU “pouring out”. | said. |
| ṣalmum-black | entry | low | Example was the prologue's phrase, not this part's. | ṣalmāt qaqqadišu, with the prologue's ṣalmāt qaqqadim in brackets. |
| emqum (broaden) | appended | medium | “imqim” as the genitive of emqum. | emqim, litany cross-reference. |
| purussûm (broaden) | appended | medium | Spellings pu-ru-us-se-e / “genitive” not those of this part (pu-ru-zi-e, pu-ru-zi-im); purussê called neither case nor number. | spellings corrected, “oblique plural” / “genitive”. |
| bašûm-Š (broaden) | appended | medium | Spelling su-ub-sa-a-am (Harper's glossary) instead of the text's šu-ub-ša-a-am; the Š infinitive glossed passively (“not to be brought into being”). | spelling corrected, Harper's form in brackets; active gloss. |
| târum-D (broaden) | appended | low | Example “litēršu šarrūtam” is not a line of this text. | melam šarrūtim litēršu. |
| ṣēnum (broaden, added) | appended | medium | The latest holder (laws 258–277) has only “sheep, the flock”; the prologue's “evil (one)” was overwritten, and ṣi-nam here is the evil one. | “ṣēnam … ‘evil (one)’, a different noun from ṣēnum ‘sheep’”. |
| nawārum (broaden, added) | appended | medium | Entry is the verb; nawārim here is a noun “of light”. | added, Harper's namaru II,1 noted, UNCERTAIN in form. |
| šaṭārum (broaden, added) | appended | medium | Needed for the lemma change at #19. | ištadar added. |
| nišū, šū, nakārum-D, ešērum, ṭâbum-D, qabûm, šebērum, sapāḫum-D, waṣûm-Š, abum, awātum, mātum (broaden, added) | appended | low (12 entries) | The latest entry does not carry the forms this part has: nišīšu “his people” (entry: “his household”), šināti, uttakkaru, lištēšir, liṭīb, liqbi, lišbir, lišappiḫaššum, šuṣâ, abu, awâtim/awâtīya/awâtūa/awāssu, mātassu/mātišu. | One true addition each, from the text and Harper's glossary. |

## Findings refused or left as drafted

- **XLI 80 (#2) `l` “I-judged” against `i` “gave”.** Left: `i` is epilogue-1's wording for the same clause (xli 68, “which I gave”); the note says both readings give the same English; changing `i` would split the two parts.
- **XLI 93 (#7) and XLII 16 (#15) `i` “and” where the Akkadian has none.** Left: English list conjunction on the last wish, the practice of epilogue-1 (xli 53, 59); `l` shows the asyndeton.
- **purussê (XLI 82) number.** Left as pass 1: oblique plural, as epilogue-1; Harper lists it with singulars; the glossary entry now only says “oblique plural” where this part's spelling is concerned.
- **mašûm / imēšma, uštepiel, lirʾi, ḫušaḫḫum, iṣūtim “few”, ilum = DINGIR, litēršu.** Left with the pass-1 verdicts; where a form is irregular the note and entry now say UNCERTAIN.
- **kīnātim under kittum.** Left: Harper has KINATU “justice” and KITTU separately; the litany's lemma is kittum and the note says so.
- **Plate shape-by-shape.** Not done for every syllabogram (see above); the rows I did not look at rest on pass 1's counts and on Harper's print.
- **ZI.IM.RI.GA, la-ḫa, ela.** Left unread, as drafted.

## Points for the lead

- Epilogue-1 (published) reads xli 68 `a-di-nu` as addinu (nadānum); this part reads it diānum (Harper's DANU lists all three places). Still not reconciled; pass 1 asked for a QUESTIONS.md line.
- The glossary homonym ṣēnum (prologue “evil (one)” against later “sheep”): the broaden entry restores both for this part; any later part that uses ṣi-nam would hit the same overwrite.
- Build and validator were not run; `lemma` `sadārum` is no longer used in this part (šaṭārum), so the `sadārum` entry is untouched in earlier parts.

## Disclosure (sole-source rule)

No modern translation was opened or recalled for any edit. Used: Harper's glossary text layer (PDF pp. 167–214), his plates 75–77, his print (the pinned source) and epilogue-1 and the earlier published parts of this work. The tanādātum remark in #11 is still from memory of the lexicon, labelled as such in the note.
