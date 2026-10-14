# Drafter notes — hammurabi-laws-185-194 (XXXII 31 – XXXIII 40)

units.json: 34 units, 197 words, 106 stele lines covering Harper's lines 1:1 (checked by script against the packet: every packet line used exactly once and in order; the split word XXXII 94/95 carries a glyph-level `nl`; every phonetic word's `reading` reconstructs from its glyphs' `tr`; every sign key exists in signs-cuneiform.json; every non-determinative glyph index is in a morph entry; no dotted k anywhere). `p`/`ln` on the first unit of §185–194 only (185 XXXII 31, 186 XXXII 39, 187 XXXII 50, 188 XXXII 54, 189 XXXII 60, 190 XXXII 65, 191 XXXII 75, 192 XXXII 96, 193 XXXIII 10, 194 XXXIII 23). The words were built by script from a hand-checked spelling table (one entry per Harper word, `gen.py`/`words.py` in the session scratchpad, not retyped per unit). I did not run build, validate or publish and did not commit. The sign glossary change (below) touched signs-cuneiform.json, index.html, reader.html through signs.py.

## How far the plates were read
Plates 54–58 (PDF 323–331) were rendered. Harper's List of Signs (PDF 383–411, his stele forms in the third column) was read page by page and used as the sign-shape reference. The plate was compared line by line at zoom 5–12 for the lines below; for the remaining ordinary syllabic lines (the great majority) the match is by sign-group count and by distinctive shapes (the TUR bracket, the É nested corners, the MU barred box, the AM lattice, KIŠ, the chevron stacks), not every wedge. Honest limit: I could not independently identify every syllabogram on the plate; Harper's printed value was followed wherever the plate showed nothing against it. Checked sign by sign against Harper's list:
- XXXII 50, 96, XXXIII 10 NER.SE.GA: three signs, KIŠ (his no. 170 ner, the diamond-and-long-triangle sign), the tall chevron "tree" (no. 76, se) and GA (no. 118). DUMU is his no. 70.
- XXXII 51 êkallim is É.GAL with NO complement (two signs, É and GAL); Harper's normalized -lim is not written.
- XXXII 52, XXXIII 1, 11 zinništi is the single sign SAL; the zi of zi-ik-ru-um is his no. 41 (barred wedge + chevron stack).
- XXXII 54 mâr ummânim is DUMU + UM.MI.A (UM, MI, A): three signs, no ending; Harper's own list no. 70 has the group mâr-ummâni.
- XXXII 55, 32, 37 (XXXIII) mâram is DUMU alone.
- XXXII 48, 63, 73, XXXIII 12, 19 "bît" and 93 "bîtim" are the bare sign É (the nested corner), no tim.
- XXXII 80 bí-zu is É + a box sign that I key ZU (see open item 3).
- XXXII 92 i-na eqlim kirêm: the line shows about seven clusters; I follow Harper (A.ŠÀ-lim, {giš}KIRI₆) without having confirmed the complements.
- XXXIII 8 lišâni-šu is two clusters: his no. 13 (lišânu, EME) + ŠU. XXXIII 39 tulê-ša is two clusters: his no. 105 (tulû, three parts joined) + ŠA.
- XXXIII 6: tier 1 u-ul a-bi, tier 2 at-ta, confirmed against a font rendering of U₂ UL A BI / AD TA. XXXIII 7 stands on two tiers (u-ul um-mi at- / ti iq-ta-bi?), see open item 7.
- The conjunction "u" is the ù sign (arrowhead + barred box, U3) in every case, as in all published parts; the U₂ sign appears in u-ul, u-ra-ab-bu-šu, u-wi-id-di-ma, u-ka-an-nu-ši-ma and šu-u.

## Signs added
- EME = 𒅴 (CUNEIFORM SIGN KA TIMES ME), Harper's list no. 13 lišânu, for XXXIII 8 lišānšu.
- UBUR = 𒉮 (CUNEIFORM SIGN NUNUZ AB2 TIMES ASHGAB), Harper's list no. 105 tulû, for XXXIII 39 tulêša. The Unicode identification with Harper's no. 105 is TENTATIVE (modern UBUR has no Unicode name of its own); the sign entry says so. If the reviewer knows better, change the key's character with signs.py.
`python3 ../run3/signs.py check`: in sync.

## Unresolved plate items (reviewer please look)
1. NER.SE.GA, second sign: Harper's no. 76 "se" (tall chevron tree) is not his no. 142 "še" (the horizontal chevron bundle used in ŠE.BA); I key it SHE (ŠE), the nearest house key, in the glyph with tr "SE". UNCERTAIN; it could be ZI in the modern list. First sign: his no. 170 ner = KISH key as in the earlier parts (the font glyph matches the plate shape).
2. ṣi in ṣi-iḫ-ra-am (XXXII 32, 40, 66, 76): the plate sign is a wedge with a barred box (Harper's no. 72 "ṣi"), not the chevron-stack no. 41 "zi" used in zi-ik-ru-um. Both are keyed ZI as in the earlier parts (precedent ṣi-iḫ-ra-am is ZI AH RA AM); possibly ṣi here is a different sign (ZA-like). Same word is spelled the same in the published part.
3. XXXII 80 bí-zu and the -zu elsewhere: the box sign after É on the plate has an arrowhead inside (closer to Harper's no. 3 ba than his no. 4 zu, which has bars). I key ZU because the grammar needs bīssu "his house" (-ssu); precedent: bi-za, ṣi-ba-zu. Same question at XXXIII 17 mu-ra-bi-zu and XXXII 85 ri-qu₂-zu.
4. XXXII 85 Harper prints tal-ku-zu. The signs are RI KU ZU; I read ri-qu₂-zu = rīqūssu "empty-handed" (UNCERTAIN, see conventions note below). The reviewer should confirm the RI sign on the plate (Harper's no. 43 ri/Nanâ).
5. Final su/šu: XXXIII 9 and 40 inakkisū (Harper prints su, not šu; kept as SU key), XXXIII 38 ir-ku-šu (Harper šu; SHU key; read irkusu). The plate does not distinguish SU/ŠU/ZU cleanly at this scale.
6. XXXII 80 uš (ISH vs USH): kept USH with Harper's uš. i-bu-uš is said ipuš (BU read pu; the house list has BU = bu, pu).
7. XXXIII 6–7: both lines are two-tier on the plate; in line 7 tier 1 seems to end with AD (at), while Harper puts the {b} before at-ti. It does not change the words or the line division.
8. XXXII 94/95: the word inaddiššum is split across two stele lines; the second part iš-šum is on 95 and the TAG (šum) sign was keyed as in the earlier parts.
9. u / TIM / DIM distinctions were not re-checked sign by sign (TIM used throughout, as in 153–184).
10. XXXII 79 u-ra-ab-bu-u-šu: the extra U₂ sign is as Harper prints; kept as written.

## New lemmas (glosser needs entries)
ummiānum (UM.MI.A "craftsman"), tarbītum "foster-child, what is raised" (rabûm-D noun), mārūtum "sonship", NER.SE.GA (untranslated Sumerogram, UNCERTAIN), ḫiāṭum (UNCERTAIN, iḫīaṭ "seeks out"), rēqum "empty" (rīqūssu, UNCERTAIN), edûm-D (uwaddi "makes known, identifies", UNCERTAIN), ṣiārum (iṣīr, root UNCERTAIN, "turn away from (?)"), rakāsum (G stem, irtakas, irkusu "bind"), mušēniqtum "wet-nurse" (Š-participle of enēqum, built from the form), lišānum "tongue" (EME), tulûm "breast" (tulê), atta "you" (masc.; atti fem.).
Broaden candidates (existing lemma does not cover this use): zikrum-class (also §187, §192–193 "mār zinništim zikrum"), izuzzum (mūzaz "one who stands"), ekallum (É.GAL with no complement), baqārum-N (ibbaqqar with AK-GAR), rabûm-D (murabbīšu / murabbītīšu / murabbīssu participle, "the one who raises him"), aḫāzum-Š (uštāḫissu "has taught him", the -ssu = ZU), šiprum (šipir qātīšu "the work of his hands"), epēšum (ipuš "he made", bīssu ipuš), nasāḫum (inassaḫū "they shall pluck out", the eye), nakāsum (inakkisū "they shall cut off", tongue and breast), kânum-D (ukannūšima "they shall convict her"), manûm-count (imtanûšu "he has counted him"), šanûm (šaniamma), qātum (qāt "in the hand of"), mārum (mārašu "his son", mār X "a member of the class X", DUMU{meš}-šu), alākum (ittalak/ittallak "he shall go (away)"), balum (balum abišu "without his father"), aššum (aššum + subjunctive "because"), īnum (īnšu "his eye").

## House renderings chosen (for conventions.md)
`ṣeḫram ina mêšu ana mārūtim ilqēma urtabbišu` "has taken a young child as his son while he was still in his waters (a newborn?) and has raised him" (ina mêšu UNCERTAIN); `tarbītum šī ul ibbaqqar` "no claim shall be made on that foster-child"; `ana bīt abišu itâr` "shall go back to his father's house"; `mūzaz ekallim` "one who stands in the palace's service"; `mār ummiānim` "a craftsman (lit. a son of a craftsman)"; `ana tarbītim ilqēma` "has taken (a son) as a foster-child"; `šipir qātīšu uštāḫissu` "has taught him the work of his hands" (aḫāzum-Š, -ssu in ZU); `itti mārīšu lā imtanûšu` "has not counted him among his sons"; `bīssu ipuš` "has set up a house of his own (made his house)"; `ana tarbītim nasāḫim panam ištakan` "has set his face to cast out the foster-child"; `rīqūssu ul ittallak` "shall not go away empty-handed (?)"; `šalšat ablūtišu` "one third of his heir's share" (as 178–184); `ul abī atta, ul ummī atti iqtabi` "'You are not my father; you are not my mother,' he has said"; `lišānšu inakkisū` "they shall cut off his tongue"; `īnšu inassaḫū` "they shall pluck out his eye"; `uwaddīma` "has identified (?)" and `iṣīrma` "has turned away from (?)" both UNCERTAIN; `mušēniqtum` "wet-nurse"; `ina qāt mušēniqtim imtūt` "has died in the wet-nurse's care (lit. hand)"; `irtakas` "has taken on (lit. bound herself to)" (UNCERTAIN); `ukannūšima` "they shall convict her, and"; `tulêša inakkisū` "they shall cut off her breast" (plural form tulê, rendered singular, noted). Spellings: ilqûšu, ilqûšuma, urabbûšu, imtanûšu, murabbīšu, murabbītīšu, murabbīssu, uštāḫissu, bīssu, inakkisū, inassaḫū, rīqūssu.

## Open questions / how some readings were reached
- ḫiāṭum "to look out for, seek" (iḫīaṭ) and the subject of iḫīaṭ (the child or the man): UNCERTAIN; I give the child as subject in the English and say the other reading is possible. No modern translation was opened.
- rīqūssu: Harper's tal-ku-zu made no sense to me; reading the same signs RI KU ZU as ri-qu₂-zu gave rēqum "empty" at once. I record honestly that the word arrived as a recognition (the root is in Delitzsch's dictionary), then was checked only against the grammar (ZU = -ssu as in bīssu, mutatis mutandis for the adverb) and the context (the next lines give the foster-son one third of his share). Marked UNCERTAIN in the English line and in the note.
- iṣīrma: no root identified (hollow verb ṣiārum? ṣarārum "deceive"?); the sense follows the sequence (finds father's house, turns from foster-parents, goes there). UNCERTAIN.
- uwaddīma: D-stem of edûm taken for "to point out, identify". UNCERTAIN.
- NER.SE.GA and zikrum class: left unread, UNCERTAIN, as in §178–184.
- mušēniqtum "wet-nurse" is derived from the form (Š-participle of enēqum "to suck"); not met in the earlier parts.
- §191's `ittalak` as an order "he shall go away" and §193's as a perfect "has gone": same spelling, different function.
- tulê: plural form; I give "her breast" in the English; reviewer may prefer "breasts".
- The law numbers: Harper's headings 185–194 only; no unnumbered unit in this part.
