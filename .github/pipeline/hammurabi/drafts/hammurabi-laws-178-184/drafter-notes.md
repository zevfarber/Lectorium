# Drafter notes — hammurabi-laws-178-184 (XXX 61 – XXXII 30)

units.json: 28 units, 282 words, 158 stele lines covering Harper's lines 1:1 (checked by script: every unit's first line and the running line count match the packet; every packet line is used exactly once; each word's `reading` reconstructs from its glyphs' `tr` once determinatives are stripped; every sign key exists in signs-cuneiform.json; every glyph index appears in exactly one morph entry; Harper's dotted k nowhere). Words were built by script from a hand-checked spelling table (one entry per Harper word), not retyped per unit. I did not run build/validate/publish.

## How far the plate was read
Plates 52–55 (PDF 319, 321, 323, 325) were rendered at zoom 6–10 and EVERY row of XXX 61 – XXXII 30 was viewed and compared with the expected sign-group sequence, with Harper's List of Signs (PDF 383–411) as the shape reference. Checked sign by sign (shapes matched to the list): all logogram lines and the lines with sub-rows; for the ordinary syllabic lines the match is by sign-group count and by the distinctive shapes (ŠA, A, BU, AZ, UG, ZI, TU/LI fans, RU curl, SAL diamond-with-tail, AN star, KAM, KÁ, É, GAL, IGI) rather than every wedge. Found on the plate and different from Harper's normalized word:
- XXXI 14 kaspim is KÙ.BABBAR with no -im written (A NA KÙ BABBAR, 4 signs).
- XXXI 13 "i-kal" is NI (read ì) + KAL: ì-kal; later lines (57, 73) write i-ik-ka-al.
- XXXI 52, 69, 87, XXXII 13 ŠA.GA (GAR GA) É a-ba, as Harper prints; the sign-group counts agree.
- XXXI 44, 77, XXXII 3, 16 mārtišu is DUMU.SAL-šu (TUR, SAL, ŠU), not DUMU-ti-šu as at §38–39.
- XXXI 45 kallâtim is SAL + É + GI₄ + A (four signs); XXXI 61 qadištam is SAL + NU + GIG (three signs); XXXI 62 NU.PAR is NU + a gap + one more sign (PAR).
- XXXI 78, 93 "aššat Marduk" is SAL + {d}AMAR.UTU (the SAL bare); XXXI 79 Bābilim is KÁ.DINGIR.RA + KI.
- XXXII 3, 17 šugītim is ŠU GI₄ TIM only: no raised SAL on the plate (Harper prints none either).
- XXX 82, 89 and XXXII 26 e-mu-uq, and all iš-ru-uq-ši-im lines: the "uq" is the UG sign (box with a long wedge), not IG; ku-nu-uk-kam (XXXII 8) has UG read uk.
- XXXI 42 ag-ga is AK + GA (read aq-qa₂), as at §141–152 the single qa₂.

## Plate items NOT resolved (reviewer please look)
1. XXXI 48 iš-[ru]-uq-ši-im: Harper brackets RU, and the plate shows no curl-shaped RU after the IŠ sign (the same word at XXXI 65, 81 and XXXII 5 has it). I kept the glyph RU with tr "[ru]" (precedent: "ni]" in 127-140) and say so in the note; if the reviewer prefers, drop the glyph and bracket instead.
2. XXX 92 (sub-row of it-ta-ad-nu-ši-im-ma): the plate shows three sign-groups after AD (a cross-like sign, a diamond-and-fan sign, MA) where Harper's nu-ši-im-ma needs four signs. I kept Harper's NU IGI IM MA. Possibly ši-im is one sign here, as -šim at XXX 85 and XXXII 19.
3. XXX 85 i-na-ad-di-nu-šim-ma and XXXII 19 iš-ru-uq-šim: Harper writes šim in one piece and the plate shows ONE sign of the TAG (šum) shape; I used TAG with tr "šim" (not "šum"), so the reading keeps Harper's šim. TAG has no šim value in the glossary; question in questions-draft.md.
4. XXXI 62 NU.PAR: the second sign (PAR) stands apart from NU on the plate; I used the BAR sign (𒁇) with tr PAR, not compared with Harper's list of signs (his entry for NU.PAR is no. 35); UNCERTAIN.
5. XXX 61 / XXXI 20: Harper's NIN.AN {b}ŠAL(?) — on the plate (XXX 61) SAL is the sub-row sign; at XXXI 20 it is on the same line. The two signs I call NIN and AN: the top row of XXX 61 shows more wedge-groups than TAG MA NIN AN need; I did not resolve whether NIN is one sign or two. 127-140's NIN + AN kept.
6. XXXI 62 "ù lu": the ù sign (Ù, IGI.DIB) is drawn as an arrow-head + box; I read it as U3 as in the earlier parts.
7. TIM vs DIM (all -tim words): TIM used throughout, as 153-177; not distinguished on the plate.
8. ŠU vs ZU (box with horizontal strokes) in DUMU.SAL-šu: I followed Harper (ŠU); 153-169 wrote DUMU.SAL-zu for mārassu. The two signs look alike on the plate.
9. uṭ-ṭi-ib-bu (XXXI 2) and u-ṭa-ab-bu (XXX 87): uṭ = UD, ṭi = DI, ṭa = DA are the values by precedent; the shapes fit but are not independent identifications. ṭ-values of DA/DI/UD/TI are modern conventions.
10. XXX 61/XXXI 20 ŠAL(?): treated as SAL; which class of woman it names is not decided (see questions).

## Signs added
GIG (𒍼, CUNEIFORM SIGN GIG; Harper's list no. 171, gig, with NU.GIG = qadištum). `signs.py check`: in sync. No other sign was added (BAR, KAL, KAM, UG, AS, USH, SIG, THREE, NIN, SAL already present).

## New lemmas (glosser needs entries)
ēma "wherever", mazûm-Š (ušamziši, uštamziši; UNCERTAIN verb, "let her have"), emūqum "strength", šalšum "a third" (IGI.3.GAL), qadištum, NU.PAR (untranslated), SAL-sign (Harper ŠAL(?); untranslated), ŠE.BA, Ì.BA, SIG.BA (untranslated rations), zikrum-priestess (not the prologue's zikrum "name"), šarāqum-give (išruq, išarraqū; kept apart from šarāqum "to steal"), ṭâbum-D (uṭabbū, uṭṭibbū; the glossary entry ṭâbum already mentions the D-stem).
Broaden candidates: ugbabtum (here NIN.AN + SAL), zinništum, kunukkum, kallatum (here a class of woman, UNCERTAIN), aššatum (SAL = aššat, "wife of Marduk"), ilkum ("ilkam alākum"), izuzzum ("take a share", ul izzaz), akālum (ì-kal), našûm (Gtn ittanaššiši; iššīma "dedicated"), baqārum, irrišum (irrissa "her tenant"), apālum (uppal, UNCERTAIN), ablūtum (ablūssa, ablūtiša "heirship"), warkatum ("estate"), aplum (ab-lim "of an heir" in kīma aplim ištēn), šaṭārum, zittum (ṣi-it-tam = zittam).

## House renderings chosen (for conventions.md)
`ša abūša šeriqtam išruqušim` "to whom her father has given a dowry" (the -šim looks back to the woman); `warkassa ēma elīša ṭābu nadānam` "to give her estate to whomever it pleases her"; `mala libbiša` "as much as her heart wants"; `lā ušamziši` / `uštamziši` "has not let her have" / "has let her have" (verb UNCERTAIN); `kīma emūq zittiša` "in proportion to her share"; `kīma emūq bīt abim` "in proportion to the means (lit. strength) of her father's house"; ŠE.BA, Ì.BA, SIG.BA "grain, oil and wool rations" (left unread); `libbaša uṭabbū` "they shall content her" (lit. make her heart good); `ana errišim ša elīša ṭābu inaddinma irrissa ittanaššiši` "she shall give (them) to a tenant who is pleasing to her, and her tenant shall keep supporting her"; `adi balṭat ikkal` "as long as she lives she shall have the use of it" (as 170-177); `šaniam ul uppal` "nor use them to pay another (?)" (UNCERTAIN); `ablūssa ša aḫḫīšama` "her heirs are her brothers alone"; `ana ilim iššīma` "has dedicated (lit. lifted) to a god" (UNCERTAIN); `IGI.3.GAL ablūtiša` "one third of her heir's share" (šalšat, (?)); `ilkam ul illak` "she shall not perform the fief-duty"; `aššat Marduk ša Bābilim` "a wife of Marduk of Babylon"; `zittam kīma aplim ištēn izzazma` "she shall take a share like one heir, and"; `ul izzaz` "she shall have no share"; `aḫḫūša ul ibaqqarūši` "her brothers shall not make any claim against her". Spellings: išruqušim, išruqšim, išṭurušim, išṭuršim(ma), inaddinūšimma, ittadnūšimma, uṭabbū, uṭṭibbū, ileqqūma, ibaqqarūši, iddišši, išarraqūšima, inaddinūši, irrissa, ablūssa, ablūtiša, aḫḫūša, aḫḫīšama, zinništum/zinništim. Priestess classes are left as the signs they are written with where no reading is certain (NU.PAR, SAL, zikrum, kallātim): the notes say so each time.
§-chips: every law starts with p and ln (178–184); no Harper-only heading in this part, so no unnumbered unit.

## Expected linecheck lines (logogram lines Harper writes as Akkadian; all confirmed on the plate above)
XXX 62, 79; XXXI 3, 9, 14, 21, 44, 45, 46, 61, 77, 78, 79, 93; XXXII 3, 16.
