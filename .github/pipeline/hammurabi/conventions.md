# Laws of Hammurabi — conventions (Run 3)

Distilled from the project's `akkadian-hammurabi-conventions.md` (decided 2026-07-17), the display decision
of 2026-10-11 (`hammurabi-signs-display`), the owner's completion plan of 2026-10-11, and the five published
parts (`hammurabi-prologue`, `-litany`, `-laws-1-10`, `-laws-11-25`, `-laws-26-41`), which are the model of
shape, notation and register. Where this file and the published parts disagree, follow the latest published
part (`hammurabi-laws-26-41`) and record the difference in QUESTIONS.md.

## The owner's decisions for finishing the code (2026-10-11)
- Finished in full, prologue to epilogue, nothing skipped: "the kind of text people use for references."
- The stele's erased section (≈§66–99, chiselled off in antiquity, almost certainly when the Elamites took the
  stele to Susa) is filled from the ancient duplicate tablets, preferring public-domain (pre-1930) editions.
- Every passage taken from a tablet other than the stele is MARKED: the unit names its witness (`w`, `ref`)
  and its note says, in plain words, which tablet the words come from ("From a fragment of a second copy of
  the code found at Susa (Scheil's Fragment I, col. II) — the stele itself is erased here.").
- Losses no surviving copy preserves are shown as gaps, never reconstructed.
- Fallback where no PD edition of a needed duplicate exists: the Aqhat rule (attested signs are facts; any
  edition's signs, never its restorations or translation). No such edition is in the repository, so in
  practice such a law is a gap unit, listed in QUESTIONS.md.

## Source and the sole-source rule
- Stele: R. F. Harper, *The Code of Hammurabi, King of Babylon* (Chicago 1904) — transliteration (pinned,
  `source/hammurabi-harper1904-source.json`, §42 → end, transcribed twice from page images 2026-10-11) and
  autograph plates (`source/harper1904-cornell.pdf`; plate index `source/harper-plates.json`; Plate N on
  PDF page 217 + 2(N−1); Harper's List of Signs on PDF pages 381–411).
- Gap witnesses (`source/witnesses/`): Kohler & Ungnad, *Hammurabi's Gesetz* II (1909) pp. 33–37 (syllabic
  transliteration of the gap laws with the tablet for each stretch; Anhang pp. 180–182 lists the duplicates);
  Ungnad, *Keilschrifttexte der Gesetze Hammurapis* (1909) (autographs of the duplicates); Poebel, *PBS V*
  (1914) no. 93, Plates XXXIX–XL (the Nippur tablet); Cuq, *Les nouveaux fragments du Code de Hammourabi*
  (1918) (Scheil's reading of that tablet). Kohler–Ungnad vols. III–V are translation/commentary — sense only.
- Lexical aids, public domain: Delitzsch, *Assyrisches Handwörterbuch* (1896); Muss-Arnolt, *Concise
  Dictionary* (1905); Harper's own glossary and List of Signs.
- Modern resources (eBL, Oracc, Roth, Borger's MZL) may be consulted silently as **sign-identity checks only**,
  never for wording. Modern translations (Roth, Richardson, Van De Mieroop, King) are never opened.
- Readings are 1904-vintage and honestly so. Where Harper's reading is superseded, keep Harper as the base
  and flag the modern understanding in the note. Notation is normalized (below).

## Data model (every unit)
`{t, l, i, n, ln, p?, col, line, words[]}`. `t` is BUILT from the words (glyphs joined; a space between
words; "\n" at every new stele line). `ln` = the law number (`numbering: "clause"` → § chips); in the
epilogue parts `ln` = the stele line number (`numbering: "line"`). `col`/`line` = the unit's first stele
line (Harper's column numeral in capitals, as in the source, e.g. "XIII", 17). Units never cross a column
in the epilogue; in the laws a long law spans several units.

Word: `{reading, say, glyphs[], morph[], nl?}`. Glyph (drafter writes): `{sign, role, tr, val?, nl?, u?}`:
- `sign` = the key in `signs-cuneiform.json` (the build copies its character). A sign not yet there is added
  with `python3 ../run3/signs.py add cuneiform KEY 'CUNEIFORM SIGN NAME' '{...}'` — the name must be the real
  Unicode name (š is spelled SH: SHA, SHU, MASH; see the gotchas below).
- `role`: `phon` syllabogram · `log` Sumerogram (carries `val`, its Akkadian value in context; `tr` = the CAPS
  citation form, e.g. A.ŠÀ written as two glyphs A + ŠÀ with tr "A" and "ŠÀ") · `det` determinative (tr "",
  superscript in academic mode, silent in readable) · `comp` phonetic complement · `num` numeral.
- `nl: true` on the first word (or the first glyph, if a word breaks across lines) of each new stele line
  after the unit's first.
- `u`: only for a numeral whose character varies with its count — the exact Unicode name.
`reading` = the academic per-sign transliteration, hyphen-joined, determinatives in braces (`{d}`), modern
subscript indices (`ša₃`, `ṣi₂`), Sumerograms CAPS with dots; it reconstructs from the glyphs' `tr`.
`say` = readable normalized Old Babylonian: macrons for long vowels, circumflex for contraction, mimation kept
(`awīlum`, `mātim`). Numbers: Arabic in `reading`/`tr` (a-du 12-šu, ITI 6{kam}); `say` spells them out
(šinšerīšu, šinā šiqil); the morph gloss marks a reconstructed spoken number "(?)".
`morph`: `[{lemma, gloss, g:[glyph indices]}]`; the part's `glossary` is keyed by lemma (built from
gloss.json + earlier parts' glossaries).

## Lessons already learned (keep them)
- q, never ḳ (owner, 2026-10-12): every reader-facing field — glyph `tr`, `reading`, `say`, `l`, `i`, notes,
  glosses — writes q, including when a note cites Harper's own spelling (Harper's eḳlam is cited as eqlam).
  Glyph values follow the modern indices: KI read qi = `qi₂`, KU read qu = `qu₂`, GA read qa = `qa₂`, IG = `iq`,
  AK = `aq`. Harper's ḳ survives only in the pinned source and the packet.
- Write Sumerograms as glyph `tr` from the start — never slices of the Akkadian word (A.ŠÀ, not "e"+"qil").
- `a-du` is said `adu` (Harper Plate IX, col. vi 21 shows DU, not DI); the note says it is a variant of adi.
- KÙ is KU3, not KU. KAR (TE-gunû), ITI fall back to Noto glyph shapes — that is accepted.
- Unicode-name gotchas: AM = "GUD TIMES KUR", AḪ = "HI TIMES NUN", Ù = "IGI DIB", UL = "U GUD", IA = "I A",
  ŠUM = TAG, tam = UD, it = A2, EŠ = "U U U", AR = "IGI RI", AZ = "PIRIG TIMES ZA", ḪAR = "HI TIMES ASH2",
  BIL = "NE SHESHIG", SUḪUŠ = "DU SHESHIG", KAR = "TE GUNU", ENGUR = "LAGAB TIMES HAL", 50 = "FIVE U".
- Harper's carver's-slip notes are kept with his correction in the note (il-te-di(=ḳi), i-pa-ad-da-ri(=ar)-šu).
- Harper's provisional spots (in the source apparatus): XLII 5–9 and XLIII 70–74 (one line-divider too few);
  XXXIV line numerals one ahead of his §-headings from §206 to §221 (follow the running numerals, note it);
  XXXVIII 31–36 a lacuna in Harper (a gap unit).

## Translation and notes
- `l` structurally transparent (hyphen-glued where it shows structure: "his-going was-ordered"); `i` real
  English, plain legal register ("If a man …"), never archaizing. The code's formula stays fixed:
  `šumma awīlum` = "If a man" (l: "If a-man").
- House renderings (fixed before drafting, from the grammar): "the black-headed people" (ṣalmāt qaqqadim);
  "so that the strong might not wrong the weak" (dannum enšam ana lā ḫabālim); "to make justice appear in the
  land" (mīšaram ina mātim ana šūpîm); `iddâk` "he shall be killed"; `ilkum` "the fief-duty"; the talion
  laws (§196–200), the most quoted lines of the code, are rendered from the grammar alone, and the drafter
  records the chosen wording as a new house rendering.
- Notes lead with what the reader needs to read the words; flag first occurrences of recurring patterns
  (šumma-protasis + apodosis; the N-stem passive; the -ma clause chain; Sumerograms read in Akkadian) then nudge.
- Never bowdlerize (the drowning, the impaling, the cut-off hand).

## Honesty (reader-facing)
Sign identifications, values, normalization and pronunciation are scholarly conventions; Old Babylonian is the
best-understood Akkadian, and the notes say so; where a reading is Harper's and superseded, say both.
In the gap parts the `about` says plainly that the stele is erased here and these laws come from other ancient
copies, named, some broken.

## Pronunciation and audio
Conventional reconstructed Old Babylonian. Audio is LIVE for this work (German carrier voice de-DE-Neural2-D,
chosen by the owner 2026-10-11, "for now"); `audio.yml` voices every new `hammurabi-` part on push
(BUILD_ON_PUSH), within the $10/month budget. The run does nothing about audio.

## Copyright safeguards
Sole-source rule above; the house renderings above; a verbatim-overlap red-flag check at review against any
distinctive modern rendering the reviewer recognises (never opened as a source).

## Decisions taken while setting up Run 3 (2026-10-12; in QUESTIONS.md too)
- Parts: the code's subject blocks, cut at law boundaries to ≈100–230 stele lines (21 parts, see plan.md).
- The gap is two parts: gap-a (house-and-neighbour laws, Ungnad's §66–≈78, from Scheil's Susa fragments and the
  Assyrian copies) and gap-b (merchant-and-loan laws, from the Nippur tablet PBS V 93 with Cuq/Scheil's reading).
  Establishing gap-a establishes both. Ungnad's approximate numbers ("§ cca. 71") become `ln: 71` and the
  note says the number is approximate.

## House renderings added by hammurabi-laws-42-51 (2026-10-12)
`bēl eqlim` "the owner of the field"; `bēl ḫubullim` "the creditor"; `ṭuppašu uraṭṭab` "he shall soak his tablet" (the debt tablet is wetted, cancelling it); `ana pî ṣimdat šarrim` "according to the king's schedule"; `{d}IM irtaḫiṣ` "the storm-god Adad flooded". `uštabši` is a Š-stem perfect (lemma `bašûm-Š`).

## House renderings added by hammurabi-gap-a (2026-10-12)
`ša pî ṭuppišu` "according to his tablet"; `bēl kirîm` "the owner of the orchard"; `tamkārum šū ul immagar` "that merchant shall not agree"; `bīt ilkim` "a house that carries fief-duty"; `ina mimma ša iddinu ītelli` "he forfeits whatever he gave"; `bītum ana bēlīšu itâr` "the house returns to its owner"; `ina ūmīšu lā malûtim` "before his days are full"; `tabal` "take away!" (lemma tabālum). Spellings `ītelli`, `īšu`.

## House renderings added by hammurabi-gap-b (2026-10-13)
Laws 89–100 numbered as approximate (Cuq's articles 90–97, 'article 100' = 99, 'article 101' opening = 100). Spellings of leqûm in q (ilqi, ilteqēma); upaṣ, NER, GIŠ.BAR left untranslated and marked uncertain; `ša ḫubullam ilqû` rendered from grammar (see units).

## House renderings added by hammurabi-laws-100-111 (2026-10-13)
`šamallûm` "agent"; `sābītum` (ŠAL.GEŠ.TIN.NA) "tavern-keeper", `bīt karānim` "tavern"; `kanīkum` "sealed receipt"; `ina abnim rabîtim` "by the heavy weight"; `tamkāršu ittakir` "he disowned his merchant"; `nīš ilim izakkar` "he shall swear the oath of the god"; `nikkazzum` "the account"; `maḫīr šikarim` "the rate of beer"; `ṣarrūtum` "criminals"; `ana dibtim` "on credit (?)"; adi 3-šu / 6-šu "three / six times"; `ūtaššar` "he shall be released" (Dt of wašārum, not D); `isaddar` "he shall write out" (sadārum). ŠAL.NIN.AN is read `ugbabtum`, always marked uncertain, never nadītum (§127, §178–179 follow). MAL.GE.A = gagûm (GE keyed GI4), uncertain. Harper's dotted headings (ḲÂPU, ḲALÛ, TADMIḲTU, BITIḲTU) are written q even when cited. DAM.GÀR is two sign-groups on the plate. Broaden bases come from the latest published holder, by script. Laws 100 opens in gap-b; this part's first unit (XVII 1–7) is the tail and carries no ln/p.

## House renderings added by hammurabi-laws-112-126 (2026-10-13)
`bēl šibultim` "the owner of the consignment"; `ina balum bēl šeʾim` "without the owner of the grain"; `nibūtum` "hostage (for debt)", `bīt nēbīša` "the distrainer's house"; `ina šīmātīša imtūt` "she died a natural death"; ⅓ MA.NA "one-third of a mina" (spoken `šalšāt` reconstructed, marked (?)); `eḫiltum awīlam iṣbassuma` "a debt has seized a man"; `ana kiššātim ittandin` "he handed over into service"; MU 3{kam} `šalāš šanātim` "three years"; `andurāršunu iššakkan` "their release shall be set"; `ana našpakūtim` "for storage" (lemma našpakūtum); `ibbûm ittabši` "an accident has happened" (uncertain); `ana gamrim` "altogether"; Á našpakim "the hire of the bin" (A₂, not A.ENGUR); `ana 1 ŠE.GUR.E 5 SÌLA ŠE` "five qa of grain for each kor"; `ukallam` "he shall show" (kalāmum-D); `dīnum šū rugummâm ul īšu` "that case has no claim"; `ina pilšim ulu ina nabalkattim` "through a breach or a crossing-over (?)"; `itti šarrāqānišu ileqqi` "from his thief he shall take"; §126 `babtum` "the one he accused" (uncertain; Harper "loss, defects"), `ubâršuma` "he shall prove it against him" (uncertain). The subjunctive -u before dative -šu(m) is short (`innadnušum`, `ūlidušum`), long only for a plural -ū. -kam is written with the KAM sign (Plate 15, X 35).

## House renderings added by hammurabi-laws-127-140 (2026-10-13)
`mutum` "husband" (short u; mūtum is "death"): mutiša, mussa; `ugbabtum` in §127 is NIN.AN alone (no ŠAL), uncertain; `zittum` "share" (Harper ṣi-it-tam); `{šal}šugītum` uncertain; `pagrum` (XXII 14) is only Harper's restoration, marked uncertain; GE in šu-gi₄-tim is GI4. §133A (Harper's heading) has no ln/p: chips run 127–140.

## House renderings added by hammurabi-laws-141-152 (2026-10-13)
`zikiltam izakkil` "plays the fool" (Harper's sense, uncertain); `ezibša iqtabi` "says 'I divorce her'" (ezēbum = "divorce" throughout); `ḫarrānša uzubbûša` "her journey (?), her divorce payment"; `ana wuṣîm panīša ištakan` "set her face to go out"; `bēlissa` "her mistress" (bēltum); `abbuttam išakkanši` "puts the slave-mark (?) on her"; `uštamaḫḫar/uštatamḫir` "make herself equal"; `laʾbum` "a sickness"; `aššum … lā ṣabātiša` "so that the creditor may not seize her"; `kilallašunu` "both of them"; `tamkāram ippalū` "they shall pay the merchant"; permissive present rendered "may" where §144 `ul iḫḫaz` shows the contrast. Spellings `ūldu`, `īzibšim`, `ušamṭa`, `iṣabbatū`. Logograms without complement are bare (SAL, GEME₂, É, KÙ.BABBAR); `{b}` marks a sub-row within one stele line.

## House renderings added by hammurabi-laws-153-169 (2026-10-14)
`iḫīrma` (ḫiārum) "has chosen (a bride)"; `kallātam` "bride" (É.GI₄.A, three signs, no ending); `biblum` "present" (betrothal gift, distinct from `tirḫatum`); `bēl aššatim` "the man entitled to the wife" (be-el, not EN); `ibrum` "friend"; `uktarriṣṣu` "has slandered him" (karāṣum-D, uncertain); `lamādum` "has had intercourse with" (l "has-known"); `nasāḫum` "cast out", `innassaḫ` "shall be cast out", `ablūtum` "sonship"; `ālam ušeṣṣûšu` "they shall drive him out of the city"; `ina gašīšim šakānum` "set on a stake" (impale); `iqallû` "burn"; `ikassûšuma ana mê inaddûši` "bind him and throw him into the water" (-ši printed on the plate, uncertain); `itabbal` "he shall take away"; `itbalam` = preterite of tabālum + ventive; `aḫāzum` "take (a wife)"; `mut libbiša iḫḫazzi` "the husband of her heart shall take her"; `aḫḫū` (lemma aḫum-brother), `inūma aḫḫū izuzzū` "when the brothers divide"; `ibbablušum` (short u before -šum); `uštašannâma` "he shall double it" (uncertain); `rabītišu` "his senior one" (father's chief wife ?); `ša īnšu maḫru` "the son he favours (?)"; `panīšu ubbalū` "they shall overlook it (?)"; `adi šinīšu` "a second time"; `kasap tirḫatim` (construct). Spellings `ušeṣṣûšu`, `ūlissum`, `aššassu`, `mussa`. Signs: ZUM (u-li-zum, uncertain, possibly two signs); UG (𒊌, Harper 62) for ug-dar-ri-zu and iš-ru-uq, not IG; -kam in ku-nu-kam is KAM; conjunction `ù` is U3; DUMU.SAL, SAL bare; TUR at XXVII 38 is only the nearest key.

## House renderings added by hammurabi-laws-170-177 (2026-10-14)
`ḫīrtašu` / `mārī ḫīrtim` "his wife" / "the sons of the wife" (ḫīrtum as the free wife against the slave-woman amtum); `mārūa iqtabi` "has said 'my sons'" (DUMU{meš}-u-a); `imtanūšunūti` "has counted them (with)"; `ana šīmtim ittalku` "after (he) has gone to his fate" (as before); `DUMU.UŠ` aplum "the heir"; `ina zittim inassaqma ileqqi` "shall choose from the share and take it"; `andurār … iššakkan` "the release … shall be established"; `ana wardūtim ul iraggumū` "shall not lay claim … for slavery"; `nudunnam` "marriage-gift", `šeriqtum` "dowry"; `ušallamšimma` "has made good to her"; `adi balṭat ikkal` "as long as she lives she shall have the use of it" (uncertain); `kīma aplim ištēn` "like one heir"; `aššum … šūṣîm` "in order to make (her) go out"; `arnam immidū` "(the sons) are in the wrong"; `mut libbiša iḫḫazzi` "the husband of her heart shall take her" (as 127-140); `warad ekallim` "a slave of the palace", `warad muškēnim` "a slave of a commoner"; `bēl wardim` "the slave's owner"; `ana šinīšu izuzzūma` "they shall divide into two parts"; `mišlam … ileqqi` "shall take one half"; `ṭuppam ušezzibūšunūti` "have them leave a tablet" (as §151); `ana unūt … išammu ina kaspišu ītelli` "the buyer … forfeits his silver"; `makkūr ana bēlišu itâr` "the property shall return to its owner". Spellings: `ūlissum`, `ūlidušum`, `iddinušim`, `iddiššim`, `išṭurušim`, `uṣṣi`, `wuṣîm`, `abiša`, `bēlišu`, `ileqqēma`, `inūma`. Plural -ū kept long in `inaddinū`, `īpušū`, `iršû`, `inaṣṣarū`, `urabbû` (couple as subject). §172A and §176A (Harper's own headings) carry no ln/p, as §133A.
Subject plurals of DUMU{meš} are said mārū, oblique mārī (as earlier parts). XXVIII 59 zi-it-tim has an unexplained extra sign-group (kept as Harper).


## House renderings added by hammurabi-laws-178-184 (2026-10-14)
`ša abūša šeriqtam išruqušim` "to whom her father has given a dowry" (the -šim looks back to the woman); `warkassa ēma elīša ṭābu nadānam` "to give her estate to whomever it pleases her"; `mala libbiša` "as much as her heart wants"; `lā ušamziši` / `uštamziši` "has not let her have" / "has let her have" (verb UNCERTAIN); `kīma emūq zittiša` "in proportion to her share"; `kīma emūq bīt abim` "in proportion to the means (lit. strength) of her father's house"; ŠE.BA, Ì.BA, SIG.BA "grain, oil and wool rations" (left unread); `libbaša uṭabbū` "they shall content her" (lit. make her heart good); `ana errišim ša elīša ṭābu inaddinma irrissa ittanaššiši` "she shall give (them) to a tenant who is pleasing to her, and her tenant shall keep supporting her"; `adi balṭat ikkal` "as long as she lives she shall have the use of it" (as 170-177); `šaniam ul uppal` "nor use them to pay another (?)" (UNCERTAIN); `ablūssa ša aḫḫīšama` "her heirs are her brothers alone"; `ana ilim iššīma` "has dedicated (lit. lifted) to a god" (UNCERTAIN); `IGI.3.GAL ablūtiša` "one third of her heir's share" (šalšat, (?)); `ilkam ul illak` "she shall not perform the fief-duty"; `aššat Marduk ša Bābilim` "a wife of Marduk of Babylon"; `zittam kīma aplim ištēn izzazma` "she shall take a share like one heir, and"; `ul izzaz` "she shall have no share"; `aḫḫūša ul ibaqqarūši` "her brothers shall not make any claim against her". Spellings: išruqušim, išruqšim, išṭurušim, išṭuršim(ma), inaddinūšimma, ittadnūšimma, uṭabbū, uṭṭibbū, ileqqūma, ibaqqarūši, iddišši, išarraqūšima, inaddinūši, irrissa, ablūssa, ablūtiša, aḫḫūša, aḫḫīšama, zinništum/zinništim. Priestess classes are left as the signs they are written with where no reading is certain (NU.PAR, SAL, zikrum, kallātim): the notes say so each time.
(Class lemma `zikrum-class`; the reviewer revised `l` of `ikkal` to the literal "she-shall-eat"; ileqqûma, eliša, `šim` = Harper's ŠIM sign (key SHIM).)

## House renderings added by hammurabi-laws-185-194 (2026-10-14)
`ṣeḫram ina mêšu ana mārūtim ilqēma urtabbišu` "has taken a young child as his son while he was in his waters (a newborn?) and has raised him" (ina mêšu UNCERTAIN); `tarbītum šī ul ibbaqqar` "no claim shall be made on that foster-child"; `ana bīt abišu itâr` "shall go back to his father's house"; `mūzaz ekallim` "one who stands in the palace's service"; `mār ummiānim` "a craftsman (lit. a son of a craftsman)", UM.MI.A with no ending; `ana tarbītim ilqēma` "has taken (a son) as a foster-child"; `šipir qātīšu uštāḫissu` "has taught him the work of his hands" (aḫāzum-Š; the -ssu is z of the stem + šu, spelled ZU); `itti mārīšu lā imtanûšu` "has not counted him among his sons"; `bīssu ipuš` "has set up a house of his own (made his house)", written É-ba(=zu): the plate shows BA where ZU is meant; `ana tarbītim nasāḫim panam ištakan` "has set his face to cast out the foster-child"; `rīqūssu ul ittallak` "shall not go away empty-handed (?)" (rīqūtum + -šu, UNCERTAIN); `šalšat ablūtišu` "one third of his heir's share"; `ul abī atta, ul ummī atti iqtabi` "'You are not my father; you are not my mother,' he has said"; `lišānšu inakkisū` "they shall cut off his tongue"; `īnšu inassaḫū` "they shall pluck out his eye"; `uwaddīma` "has identified (?)" and `iṣīrma` "has turned away from (?)", both UNCERTAIN; `mušēniqtum` "wet-nurse" (Š-participle of enēqum, built from the form); `ina qāt mušēniqtim imtūt` "has died in the wet-nurse's care (lit. hand)"; `irtakas` "has taken on (lit. bound)" (UNCERTAIN); `ukannūšima` "they shall convict her, and"; `tulêša inakkisū` "they shall cut off her breast" (tulê is a plural form, rendered singular, noted). NER.SE.GA and the zikrum class are left unread (signs KIŠ, ŠE (UNCERTAIN, Harper no. 76), GA). Spellings: ilqûšu, ilqûšuma, urabbûšu, imtanûšu, murabbīšu, murabbītišu, murabbīssu, uštāḫissu, bīssu, inakkisū, inassaḫū, rīqūssu. Urabbi is the preterite of rabûm-D (present urabba, perfect urtabbi). Signs added: EME (𒅴, KA TIMES ME, Harper no. 13, lišānu); UBUR (𒉮, NUNUZ AB2 TIMES ASHGAB, Harper no. 105 tulû; identification TENTATIVE). The ṣi of ṣi-iḫ-ra-am (Harper no. 72) is keyed ZI, the only ṣi key.

## House renderings added by hammurabi-laws-195-214 (2026-10-14)
Talion (§196–200), rendered from the grammar: `īn mār awīlim uḫtabbit … īnšu uḫappadū` "has destroyed the eye of a man's son … they shall destroy his eye" (both verbs UNCERTAIN, ḫabātum-D and ḫapādum-D); `eṣemti awīlim ištebir … eṣemtašu išebbirū` "has broken a man's bone … they shall break his bone" (NER.PAD.DU = eṣemtum, ending supplied); `šinni awīlim mēḫrišu ittadi … šinnašu inaddû` "has knocked out the tooth of a man of his own rank … they shall knock out his tooth"; `mārassu idukkū` "they shall kill his daughter"; `ina puḫrim ina qinazi alpim 1 šūši immaḫḫaṣ` "he shall be struck sixty times in the assembly with an ox-hide whip" (qinazum split UNCERTAIN). KÙ.BABBAR is written without an IM complement (plate); i-du-uk-ku uses UG; PAD (𒉻) added. Spellings `abašu`, `elišu`, `ešret` as earlier parts. §206 on: running line numerals, not Harper's §-headings.

## House renderings added by hammurabi-laws-215-240 (2026-10-14)
`asûm` "the physician" (A.ZU); `gallābum` "the barber" (ŠU.I); `bānûm` "the builder" (ŠITIM); `malaḫum` "the boatman" (MÁ.LAḪ₄); `elippum` "boat" (GIŠ.MÁ); `ūtaššar` "be released"; `uḫtalliq` "destroyed"; `rebūt`/`šuššat` reconstructed spoken numbers marked (?). Signs FOUR, SHITIM added. See units' notes for the unread boat-law verbs.

## House renderings added by hammurabi-laws-241-257 (2026-10-15)
`alpam … ana nibūtim itebbi` "has taken an ox as a hostage-pledge"; `ana šattim I īgur` "hired for a year"; `iriab` "he shall replace"; `ūtaššar` "go free" (as §103); `ina ṣērim` "in the open country"; `ikkib-` / `ikkipma` "gored" (nakāpum); `kaspam mišil šīmišu inaddin` "he shall pay half its price"; `nīš ilim izakkarma` "swears the oath of the god"; `dīnum šū rugummâm ul īšu` as earlier. Unread kept bare: GU₄.DA.UR.RA, GU₄.LID.UD.SAG, ŠÀ.GAL, AK.ŠU. Numerals: šalāšat, erbet, samānat, ešret (reconstructed, (?)). Sign EIGHT added.

## House renderings added by hammurabi-laws-258-277 (2026-10-15)
`īgur` "has hired" (preterite in the protasis, as 241-257); `Á-šu` / `Á-ša` `idīšu` / `idīša` "its hire" / "her hire" (of the thing hired), `idi` "the hire of" before a trade name; `ŠÀ.GUD` unread (an ox-driver (?)); `GIŠ.APIN` `epinnam` "plough" (Harper's List no. 108), `GIŠ.APIN.TUK.KIN` and `GIŠ.GAN.UR` unread (two farm implements); `NA.KAD` `nāqidam` "herdsman" (NA + KAD, Harper's glossary); `ana LID.GUD.ZUN u ṣênê rīm īgur` "hired to pasture cattle and sheep" (ri-im = `rēʾîm`, lemma `rêʾûm-pasture`, UNCERTAIN); `ša innadnušum` "that was given to him"; `uḫtalliq` "has destroyed (lost)", i "has lost"; `alpam kīma alpim … iriab` "he shall replace ox for ox"; the animal logograms GU₄ and UDU are bare (no -am written); `idīšu … ḫarratim maḫir` "has received his wage … (a damaged phrase)" — the middle is damaged, `ḫarratim` is not read and nothing is claimed for it; `libbašu ṭāb` "his heart is good" = "he is satisfied"; `uṣṣaḫḫir` "has diminished" (ṣeḫērum-D, UNCERTAIN; Harper's glossary also lists an intransitive stem), `umtaṭṭi` "has reduced" (maṭûm-D); `ana pî riksātīšu` "according to his contract" (KA = pûm "mouth"); `talittam u biltam inaddin` "he shall give the young and the yield"; `uṣarrirma` "has been dishonest (?)", `šimtam uttakkir` "has changed the mark (?)", `ana kaspim ittadin` "has sold for silver"; `adu ešrīšu ša išriqu` "up to tenfold of what he stole" (i: "up to ten times what he stole"); `ù lu` written as two words, ù (lemma `u`) + lu (lemma `lū`) "or" — never `ulu` (the plate has the Ù sign, as in 241-257; 112-126 and 127-140 have one word `ulu`, see QUESTIONS); `lipit ilim` "a stroke of the god" = "a plague (?)" (Harper's glossary: liptu "stroke, visitation"); `ubbamma` "he shall clear himself, and" (UNCERTAIN); `miqitti tarbaṣim` "the loss of the pen" (the KI of mi-qi₂-it-ti is read qi), `tarbaṣum` is spelled tar-ba-ṣi-im; `rēʾûm igûma … kazzatam uštabši` "the herdsman was careless and has brought about a harm (?)" (`igûma` as 112-126, `say` igûma); `kazzatum` "a harm (?)" and `ḫiditum` "loss (?)" UNCERTAIN (Harper's glossary: kazzatu "injury", ḫitîtu "blame, reproach, disaster, loss"), kaz written ka + az; the verb `ušallamma` "he shall make good, and" stands at the head of the next unit (XXXVIII 86), not in the §267 unit; `ana dīāšim` "for threshing"; `lalâm` (LÁ + AM) unread, "a small animal (?)" (Harper's glossary "small animal, goat (?)"); `ṣumbam` "wagon" (GIŠ.MAR.GÍD.DA, GÍD keyed LAL, tentative), `murteddīša` "its driver", `ṣumbamma ana ramānīša` "the wagon alone, by itself"; `ina ūmim ištēn` "per day" (UD + 1 + KAM; ūmum is masculine, so ištēn, whereas `ina šattim ištēt` "in a year" keeps the feminine form of 241-257); `{lu₂}NAGAR` `agram` "a hireling" (as 26-41), NAGAR alone `nangarim` "of a carpenter" (Harper's own normalization, two lemmas for one sign); `adi taktida šattim` "until the end (?) of the year" (taktida unread); `maḫirtam` unread "a kind of boat (?)" (as §234–239); the {lu₂} trade names GAB.A, KAD, GUL, GA(?), SA, AT.KIT left unread; `ŠE` = "grain (še)" in the plain English `i` for the small silver weight ("six grains of silver"), the note keeps the technical word; numerals reconstructed as spoken forms, all (?): šeššet, ḫamšat, šalāšat (as 241-257; 215-240 has šalāš), erbet, samānat, ešrā, ešret, ištēn, ištēt, erbâ, šalāš šūšī, šinā u mišil, šuššat (IGI.6.GAL), with the feminine form before ŠE and GÍN; the 4 of the SA law (XXXIX 38) is bracketed, the plate being hatched there. Gap units: §262 at XXXVIII 30 (`a-na` + LACUNA); the lacuna XXXVIII 31–36 is not printed by Harper, so it has no unit of its own (the validator matches units to Harper's lines) and §263 starts at 37. Signs added: APIN, TUK, KIN, GUL, KAD (KAD₂, tentative).

## House renderings added by hammurabi-laws-278-282 (2026-10-15)
`bennī … elīšu imtaqut` "the bennu-sickness has fallen on him" (disease unknown; -ī unexplained); `warḫušu lā imlāma` "his month is not yet full"; `ana nādinānišu utārma` "he shall give him back to his seller"; `baqrī irtaši` "claims have arisen against him (?)" (AK = aq, ba-aq-ri); `nādinānšu baqrī ippal` "his seller shall answer the claims"; `ina māt nukurtim` "in a hostile country"; `mārū mātim` "natives of the country" (l "sons-of the-land"), `mārū mātim šanītim` "natives of another country"; `utēddi` "has identified (?)"; `lū warassu lū amassu` "whether his male slave or his female slave" (ARAD-zu, GEME₂-zu); `ina maḫar ilim kaspam išqulu iqabbima` "shall declare, before the god, the silver he paid" (i-qa₂-ab-bi-ma); `ipaq` "shall take back (?)" (lemma pâqum, UNCERTAIN); `ul bēlī atta` "You are not my master"; `kīma warassu ukānšuma` "he shall prove him to be his slave"; `uznašu inakkis` "he shall cut off his ear"; "a male or a female slave" as §118. ù lu is two words. wardum/amtum/KÙ.BABBAR stand bare on the plate. §278–282 end the numbered laws; the epilogue (col. XL) follows.

## House renderings added by hammurabi-epilogue-1 (2026-10-15)
`aḫī ul addi` "I did not let my arm drop (I was never idle)" (as `aḫšu iddi`); AN alone as subject is `Anum`; `rēʾûm mušallimum` "the shepherd, the protector"; Š perfects are labelled by their stem (`uštapṣiršināti` paṣārum-Š, `uštaktitma` katātum-Š); `ay` + preterite "may (it) not"; `iršiā` (3rd fem. pl.); Zarpanitum is one sign (Harper 183), shown as ZA with tr Zar, TENTATIVE; -mi opens the quotation at XLI 20, `liqbīma` introduces it at XLI 40; `danītam` "firmly (?)"; `ṣāt ūmi` "the future of days"; `matīma`; li- precatives "let/may". Signs ALAN (ṣalmum) and SIG4 (libittum) are tentative; TUKUL keyed to TUK (Harper 187).

## House renderings added by hammurabi-epilogue-2 (2026-10-15)
`ṣalmāt qaqqadišu` "his black-headed people"; `narûm šū likallimšuma` "let that stele show them to him"; `šar mīšarim` "king of justice"; `dīnšina lidīn / purussāšina liprus` "let him judge their case, decide their decisions"; `ina mātišu raggam u ṣēnam lissuḫ` "let him uproot the wicked and the evil one from his land"; `šīr nišīšu liṭīb` "let him bring well-being to his people"; `ḫaṭṭašu lirrik` "lengthen his scepter"; `irrit ilī` "the curse of the gods" (NI.NI); `palê tanēḫim` "a reign of sighing"; `ana šīmtim lišīmšum` "decree for him as his fate"; `ilum rabûm abu ilī` "the great god, father of the gods". `litēršu` recurs in later epilogue parts — render the same way. `a-di-nu` is read adīnu (diānum) here.
