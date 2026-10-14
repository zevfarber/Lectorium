# Drafter notes — hammurabi-laws-170-177 (XXVIII 38 – XXX 60)

units.json: 32 units, 385 words, 204 stele lines, covering Harper's lines 1:1 (checked by script: every unit's first line and the running line count match the pinned transliteration; `reading` reconstructs from the glyph `tr`; every sign key exists; `signs.py check` = in sync; a dry assemble + validate with an empty gloss gives no error other than "lemma has no gloss" for the 12 new lemmas below, and the usual WARN of 37 linecheck lines).

## How far the plate was read (honest limit)
Plates 46–52 (PDF 307–319) were rendered and viewed. Line division and the Sumerogram lines were checked by sign-group count; shapes were confirmed for the lines listed in "plate-confirmed" below. I did NOT identify every syllabogram independently: syllabic words follow Harper's transliteration and the sign keys of the published parts for the same spelling (script-built from the precedent), so the reviewer must still read every sign. Where a Sumerogram's complement was not decidable at this zoom I followed the published parts' "bare logogram" practice (É, GEME₂, KÙ.BABBAR, SAL, ARAD, É.GAL without complement).
- plate-confirmed: XXVIII 40/42 (DUMU ME ESH U LI ZUM), 41 (U3, SAL+KUR, ZU), 47 (DUMU ME ESH U A | IG TA BI; sub-row break after U, same at 65), 54 (DUMU ME ESH ḪI IR TIM), 55 (U3 DUMU ME ESH SAL KUR, no -tim), 64 (GEME₂ bare, ul-du-šum on the second sub-row), 53 (É bare on the second sub-row), 58 area, XXIX 57 (second sub-row = É GAL), XXIX 59 MAŠ.EN.KAK (three spaced signs), 58 U3 LU ARAD, row-length/sub-row structure of the lines Harper marks {b}.
- NOT resolved on the plate (reviewer please decide): `tim` TIM vs DIM everywhere (I used TIM throughout, as 153-169 does for šīmtim, ḫīrtim etc.); É bare vs É-tim at XXX 25, 32 (bîtim) — bare chosen; KÙ.BABBAR bare vs -im at XXIX 2, XXX 51; ARAD bare vs ARAD-im in `bēl wardim` (XXIX 64, XXX 5, 17); GEME₂ bare at XXVIII 45, 64, 70, 74, 77 (checked at 55, 64 only); `ša`/`ta` in XXVIII 75 (see below); MU in XXIX 10 (see below); ZI-IT-TIM at XXVIII 59 (could be ḪA.LA as at §60 — I kept Harper's syllabic spelling).

## Uncertain readings (all flagged UNCERTAIN or (?) in the notes)
- XXVIII 75 `iš-ta-ak-ka-an`: Harper's reading (glossary I, 2). Kept in `reading`, with TA; `say` normalized to the N present `iššakkan` (passive "shall be established", as §105/§117, which are written iš-ša-ak-ka-an). If the plate shows ŠA the glyph should change to SHA.
- XXIX 10 `u-ša-la-mu-ši-im-ma`: Harper has an extra MU (his glossary: u-sa-la-mu-si-im). `say` ušallamšimma (as §138/§149/§156). Seven glyphs kept as Harper prints.
- XXVIII 44/63 `bu-ul-ti-šu`: bultišu (Harper BULTU), modern bulṭu; TI glyph tr "ti".
- XXVIII 58 `DUMU.UŠ` = aplum "heir" (Harper TUR.UŠ, ablu); heir vs eldest son.
- XXVIII 49 `imtanūšunūti` (manûm "to count"): vowels of the form.
- XXVIII 46/64 `ūlidušum`, XXVIII 40 `ūlissum` (ZUM complex sign, as §167).
- XXVIII 88–XXIX 1 `ikkal` "she shall eat" read as "have the use of"; XXIX 4 `warkassa` "her estate" (§171) vs "her case" (§172).
- XXIX 18 `uzaḫḫamūši` (zaḫāmum D, Harper "to scheme"); XXIX 23 `arnam immidū` ("the sons are in the wrong", Harper emēdu I,1 "to be in the wrong"); the whole §172 protasis/apodosis division rests on that reading.
- XXIX 55 `ḫāwirīšama` = first husband (?) (the "(?)" is in `i`).
- XXIX 73 `iḫuzuši`: short -u (house rule) is only a guess (could be iḫuzūši).
- XXX 24 `ṣiḫḫirū` (plural of ṣeḫrum?), XXX 46 `ušezzibūšunūti` "have them leave a tablet" (as §151 uštēzib), XXX 22 NU.MU.SU = almattum "widow".
- XXIX 64 etc. `be-el` + ARAD: ending not decided (see above). Harper's printed dots (XXIX 65 ṇ) ignored.
- Sub-row marker {b} is not recorded anywhere in the output (as in 141-152/153-169).

## New signs
None added (`signs.py check`: in sync).

## New lemmas (glosser needs entries)
bultum (BULTU "life-time"), wardūtum "slavery", nudunnûm "marriage-gift" (Harper NUDUNNU), zaḫāmum-D "to scheme", emēdum (arnam emēdum "to be in the wrong"), emēdum-N "to be joined" (Harper IV,1), warkûm "later, subsequent" (warkîm, warkūtum), gadum "together with" (Harper GADU), bišum "property" (Harper BISU), almattum "widow" (NU.MU.SU), panûm "former" (panîm), unūtum "household goods" (Harper UNUTU).
Broaden candidates: `mutum` ("husband"), `ḫīrtum` (here the legal wife as against the slave-woman), `warkatum` (warkassa "her case"/"her estate"; warkat "the estate of"), `aplum` (also DUMU.UŠ), `ḫāwirum`, `rabûm-D` (here "to bring up"), `ezēbum-Š` (here "have them leave a tablet"), `erēbum`, `leqûm`.

## New house renderings proposed (for conventions.md)
`ḫīrtašu` / `mārī ḫīrtim` "his wife" / "the sons of the wife" (ḫīrtum as the free wife against the slave-woman amtum); `mārūa iqtabi` "has said 'my sons'" (DUMU{meš}-u-a); `imtanūšunūti` "has counted them (with)"; `ana šīmtim ittalku` "after (he) has gone to his fate" (as before); `DUMU.UŠ` aplum "the heir"; `ina zittim inassaqma ileqqi` "shall choose from the share and take it"; `andurār … iššakkan` "the release … shall be established"; `ana wardūtim ul iraggumū` "shall not lay claim … for slavery"; `nudunnam` "marriage-gift", `šeriqtum` "dowry"; `ušallamšimma` "has made good to her"; `adi balṭat ikkal` "as long as she lives she shall have the use of it" (uncertain); `kīma aplim ištēn` "like one heir"; `aššum … šūṣîm` "in order to make (her) go out"; `arnam immidū` "(the sons) are in the wrong"; `mut libbiša iḫḫazzi` "the husband of her heart shall take her" (as 127-140); `warad ekallim` "a slave of the palace", `warad muškēnim` "a slave of a commoner"; `bēl wardim` "the slave's owner"; `ana šinīšu izuzzūma` "they shall divide into two parts"; `mišlam … ileqqi` "shall take one half"; `ṭuppam ušezzibūšunūti` "have them leave a tablet" (as §151); `ana unūt … išammu ina kaspišu ītelli` "the buyer … forfeits his silver"; `makkūr ana bēlišu itâr` "the property shall return to its owner". Spellings: `ūlissum`, `ūlidušum`, `iddinušim`, `iddiššim`, `išṭurušim`, `uṣṣi`, `wuṣîm`, `abiša`, `bēlišu`, `ileqqēma`, `inūma`. Plural -ū kept long in `inaddinū`, `īpušū`, `iršû`, `inaṣṣarū`, `urabbû` (couple as subject). §172A and §176A (Harper's own headings) carry no ln/p, as §133A.

## Expected linecheck lines (37; all logogram lines Harper writes as Akkadian)
XXVIII 40, 41, 42, 45, 54, 55, 58, 64, 70, 74, 76, 77; XXIX 2, 5, 16(fixed: šumma added), 22, 24, 27, 34, 41, 60, 62, 65, 66, 71, 77, 81, 88; XXX 8, 20, 23, 39, 43, 47, 51, 55, 57 — each is DUMU{meš}/DUMU.SAL/GEME₂/SAL/É/KÙ.BABBAR written as Akkadian by Harper; to be confirmed on the plate by the reviewer.
