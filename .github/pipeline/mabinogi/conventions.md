# Pedeir Keinc y Mabinogi (the Four Branches) — conventions (Run 3)

Distilled from the project's `welsh-mabinogion-conventions.md` and `mabinogion-pilot-2026-09-27.md`, and the
published pilot `mabinogi-001.json` (Pwyll and Arawn exchange kingdoms), the model of shape and register.

## Edition of record
J. Gwenogvryn Evans, *The White Book Mabinogion* (Pwllheli 1907) — a diplomatic transcription of NLW Peniarth 4
(the White Book of Rhydderch, c. 1350); public domain; chosen by the owner over the Red Book (2026-09-27).
Scan `source/raw/evans1907.pdf` (archive.org `whitebookofmabin00evan`); the Four Branches are Evans cols 1–111
(Pwyll 1–38, Branwen 38–61, Manawydan 61–81, Math 81–111), PDF pp. 33–88; column c is on PDF page (c+65)//2,
odd columns left. All present and legible (checked 2026-10-12). No Red Book substitution in the Four Branches.
The archive.org OCR misreads Evans's special sorts wholesale; per-part OCR drafts, the second witness and the
disagreement worklists are in `source/drafts/`. The second witness (cy.wikisource, Williams-shaped) is a
comparison only, never the edition, never adopted without the image — it has its own typos and unbracketed Red
Book wording. Third witness for White Book defects: Rhŷs & Evans 1905 (Red Book text), `source/raw/rhys-evans1905_*`.
Later editions (Ifor Williams 1930 onward) are in copyright and are not the edition.

## What the text looks like
- Manuscript spelling kept: `k` for /k/, `u`/`v` for /v/, `w` for the 6-shaped w, `y` for /ɨ/ and /ə/, `d` for
  /d/ and /ð/, final -t -c -p for /d g b/, `ss`/`s` for long s, `ll` and `rh` as written. Evans's dotted ẏ printed
  plain y; his underlinings not reproduced.
- Word division and punctuation are ours: proclitics separated (a oed, a doeth, ym penn); fused forms with an
  apostrophe (a'y, y'r, o'r, i'th, a'm, a'th, y'm, ni'th, o'y) — the reader splits them and glosses each half.
  Speech in “ ”. Capitals: sentence starts and proper names only.
- Manuscript defects shown, not mended: a word the sense requires that the White Book omits is supplied from the
  Red Book and the note says so; phrases Williams supplied that the sense does not need are not supplied; a
  readable scribal slip stays and is glossed under the intended word.

## Sectioning and segmentation
The four branches are the manifest `group` ("First Branch: Pwyll" …); parts are the tale's own episodes,
`mabinogi-NNN` in order across all four branches, with `seq`. Prose; tap-unit = the sentence, cut at a full stop
or question mark; a speech and its `heb ef` tag are one unit; never cut at a comma unless a sentence would run
past about forty words. `p: true` on the first unit of each paragraph (ours: a change of scene or of
speaker-exchange). The units' `t`, joined, reproduce the established text character for character. No `tr`, no `v`.

## The two English layers
- `l` follows the Welsh order as far as English can bear it and shows the machinery: the abnormal sentence
  ("Pwyll … a oed" → "Pwyll … it-was-that was"), `sef` ("that-is"), the gwneuthur periphrasis ("rising he-did"),
  the verbal noun for a finite verb ("and coming to Glyn Cuch"), `heb ef` "said he". Hyphenate sparingly.
- `i` real English prose, lightly old-fashioned ("it came to pass" allowed), courtly and dry, never childish;
  `i` on every unit.
- A repeated formula gets the same English every time. Proper names in English take the modern Welsh forms:
  Pwyll, Arawn, Hafgan, Dyfed, Arberth, Glyn Cuch, Annwfn, Rhiannon, Pryderi, Branwen, Bendigeidfran, Manawydan,
  Gwydion, Aranrhod, Lleu, Blodeuedd …

## House renderings (fixed before drafting)
| Welsh | `l` | `i` | avoided |
|---|---|---|---|
| Pwyll Pendeuic Dyuet | Pwyll Prince of-Dyfed | Pwyll, Prince of Dyfed | Lord of Dyved |
| A threigylgweith | And one-time | And once | One day |
| Annwuyn | Annwfn | Annwfn | the Otherworld, Hell, Hades |
| Penn Annwuyn | Head of-Annwfn | Head of Annwfn | Chief of Annwn |
| erchwys | pack | pack | hounds (that is cwn) |
| unben / unbenn | chieftain | chieftain | lord, sir, prince |
| ansyberwyt | un-courtesy | discourtesy | rudeness |
| anryded | rank | rank | honour, dignity |
| kerennyd | friendship | friendship | goodwill |
| kedymdeithas | fellowship | fellowship | companionship |
| kyuoeth | realm | realm | kingdom, dominions |
| gormes | oppression | oppression | scourge, plague |
| y rof i a Duw | between me and God | between me and God | by God |
| Ie | Yes | Yes | Aye, Well |
| heb ef / heb ynteu / heb hitheu | said he / said he-for-his-part / said she-for-her-part | he said / he said / she said | — |
| Duw a dalo itt | God may-he-repay to-you | may God repay you | God reward thee |
| Sef … | That-is … | (dropped) | This is what … |
| a oruc / a wnaeth | he-did | folded into the verb | he proceeded to |
| gwreic | wife / woman | same | lady |
| llys | court | court | palace, hall |
| gwyrda | noblemen | noblemen | nobles, magnates |
| teulu | household-troop | warband | household, retinue |
| cantref | cantref | cantref | hundred, cantrev |
| pryt … ac ansawd | form and appearance | form and appearance | shape and semblance |
| dyrnaut | blow | blow | stroke |
| digrifwch | amusement | pleasure | mirth, diversion |
| carueidrwyd | affection | affection | dalliance |
| meuyl im | shame to-me | shame on me | woe is me |
| Oy a Duw | Oh God | Oh God | Alas |

## Notes and Middle Welsh for the reader
What a tutor would point at; flag on first occurrence in a part, then nudge: the abnormal sentence; verbal-noun
narrative closed by a oruc / a wnaeth; sef; mutations written as they sound, with the base word named
(y wlat ← gwlat; a chanu ← kanu); the five jobs of y; old spellings (u = v, k = c, -t = -d, d = dd); vanished verb
forms (imperfect subjunctive -ei/-ssei, pluperfect -ssei, impersonal -it/-wyt, 3 sg. preterite -wys/-awd);
conjugated prepositions (arnaw, idaw, ganthaw …). Quote Welsh bare, English glosses in single quotes. A note says
plainly where the text has a supplied word or a manuscript slip. Words whose meaning is disputed are said to be.

## Glossary
Work-level `mabinogi-glossary.json` — a flat object `{form: entry}`. Keys: lowercased forms exactly as the
reader tokenizes them (mutated forms; apostrophe halves `a`, `y`, `r`, `th`, `m`). Entry: `lemma (modern) —
meaning; grammar; mutation and its cause`, the dictionary form as GPC lemmatises it. 100 % coverage (validator).
Sonnet invents modern forms and misnames mutations — the reviewer budgets a real check of every entry.

## Sole-source rule and aids
Draft from the established text plus, from knowledge, Strachan *Introduction to Early Welsh* (1909),
Morris-Jones *A Welsh Grammar* (1913), Silvan Evans *Dictionary* (1887–1906); GPC may be consulted for meanings
(the owner's ruling: a dictionary entry is a meaning, not a rendering). Modern English Mabinogion translations
(Jones & Jones, Gantz, Ford, Davies, Bollard, Parker) are never consulted; Lady Charlotte Guest (1849) stays
closed too. If an English phrase arrives fully formed, rebuild it from the Welsh.

## Pronunciation and audio
Convention (stated in the source line): the manuscript spelling read with the sounds of Welsh c. 1300. A voice
has not been chosen by the owner (a pilot clip job exists, unheard); parts publish without audio. Do not build audio.

## Decisions taken while setting up Run 3 (2026-10-12; in QUESTIONS.md)
- Parts: 13 more episodes, 002–014 (see plan.md); 012 is short (1,142 words) because the tale's seam is there.
- Word division and punctuation: the pilot's established text in practice follows the second witness's
  punctuation; continue the pilot's practice (it is the published model) — the owner may rule otherwise.
- Col. 16 (part 002): Evans prints a blank in "Arglwyd heb [ ] allu"; the sense needs "nyt oes" (Red Book "heb ef
  nyt oes allu") — supply "nyt oes" only, with a note. Col. 14: "na thygyei idaw idaw" — a scribal repetition,
  printed as written, with a note.
- mabinogi-001's source line says "columns 1–13"; the part ends in col. 12 — corrected at setup.
