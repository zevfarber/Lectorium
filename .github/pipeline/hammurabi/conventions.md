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
