# Cantar de mio Cid — conventions (Run 3)

Distilled from the project's `old-spanish-cid-conventions.md` (2026-07-20) and the published pilot
`cid-tiradas-01-04.json` (tiradas 1–4, lines 1–64), the model of shape and register.

## Edition and sources (sole-source rule)
- Text: Ramón Menéndez Pidal, *Poema de mio Cid*, 2.ª edición corregida (Clásicos Castellanos 24, Madrid 1923)
  — public domain. Scan: archive.org `PoemaDeMioCid2ed` (`source/raw/pidal1923_text.pdf`; printed page = PDF
  page − 4). The OCR (`source/raw/pidal1923_djvu.txt`) is never used as text; the mechanically cleaned
  per-part drafts in `source/ocr/` are a starting point only. The structure (152 tiradas, lines 1–3730, every
  margin label and tirada break) was checked by eye on all 236 poem pages on 2026-10-12 (`source/tiradas.json`).
- Lexical aids, PD: Pidal's own notes at the foot of the page, his *Cantar de mio Cid: texto, gramática y
  vocabulario* (1908–11). Modern translations (Hamilton & Perry, Raffel, Harney, Such & Hodgkinson …) are never
  opened.

## The manuscript and honesty
Single manuscript (Vivar codex; colophon "Per Abbat … era de mill e CC XLV", AD 1207). The first folio is
lost; Pidal's prose reconstruction of the opening is not included. Two more folios are lost (after v. 2337 and
after v. 3507): Pidal fills them with italic prose from the chronicles (tiradas 115, 149, 150) — we do NOT
include that prose; the unit where the gap falls says in its note what is lost and that Pidal supplies the sense
from the *Crónica de Veinte Reyes*.

## Orthography (established text)
- Pidal's critical text exactly, inconsistencies included (puorta/puerta, llegaua/tornava, buolto, run-together
  dela), old accentuation (tí, Vío). Pidal does NOT accent "mio" — the OCR does; the image decides.
- Pidal's italics = editorial restorations → [brackets] at letter/word level: entróv[e], su[e], ve[e]r,
  R[o]y (only the o is italic), [Burgos]. A wholly italic (restored) line is printed plain and flagged in its note.
- Quotation marks: one opening “ and one closing ” per speech; Pidal's repeated line-initial quotes dropped.
- No transliteration; no plain-letters toggle needed (ç is readable).

## Sectioning, numbering, segmentation
- Work = Cantar de mio Cid; parts = runs of whole tiradas (≈55–110 lines), a very long tirada split at a strong
  sense break; ids `cid-tiradas-NN-MM` (a/b/c for split tiradas).
- Line numbers are Pidal's, b-numbers included (14b). `ln` = the integer part of the unit's first line (the
  reader computes the range by counting lines, so a range across a b-line reads one high — accepted, as in the
  pilot). Pidal moves lines but keeps their numbers: follow his print order, keep his numbers, and say so in the
  note where it happens. A line with two numbers (1044-5) takes the first in `ln`; the note gives both.
- Verse stays verse: tap-unit = punctuated sense-unit (1–4 lines, never more than 6), lineation kept with "\n",
  `v: true`; `p: true` on the first unit of each tirada. Caesura not marked.
- Pidal's tirada rubrics are editorial: fold a short English version into the first note of each tirada
  ("Tirada 2 (assonance ié-a) — Omens on the road to Burgos").

## Translation and notes
- `l` structurally transparent, keeping the line division of `t` (one `l` line per verse); hyphenate glued
  clitics sparingly (oviéronla "they-had-it", ferídal "a-blow-to-it", nol "not-him"). `i` real English, one
  paragraph, lightly elevated, never childish.
- Recurring patterns (first few times, then a nudge): initial f- for modern h- (fablar, fincar); aver
  'have/hold'; the split conditional (conbidar le ien); enclitic squeeze (nol, gela, tornós, l'an); double
  negative; epic tense-mixing; article + possessive (las sus bocas); a new assonance = a new tirada.
- House renderings: v. 20 "God, what a good vassal — if only he had a good lord!"; Padre spirital "the spiritual Father"; Minaya Albar Fáñez "Minaya Álvar Fáñez" in `i` (Albar kept in `l`); the *en buen ora* formula
  "in a good hour you girded on your sword" (and its variants: "born in a good hour").
- Bavieca (the Çid's horse, first at v. 1573) "Babieca" in `i` (Bavieca kept in `l`), from cid-tiradas-84-86.
- Yúcef, king of Marruecos (first at v. 1621) "Yúsuf" in `i` (Yúcef kept in `l`); Marruecos "Morocco" in `i`, from cid-tiradas-87-90.
- Never bowdlerize.

## Glossary
Shared `cid-glossary.json` (`{work, workEn, language, note, glossary}`), keyed by the reader's tokens (brackets
stripped, lowercased; an apostrophe splits: l'an → `l`, `an`), value "lemma = modern Spanish — meaning
(grammar)" as in the existing entries. 100 % coverage, checked by the validator.

## Pronunciation and audio
Reconstructed twelfth-century Castilian (ç = [ts], z = [dz], intervocalic -s- = [z], x = [ʃ], j/g(e,i) = [ʒ],
initial f- = [f], v distinct from b). `langCode: null`. A voice has not been chosen by the owner; parts
publish without audio until he chooses. Do not build audio.

## Decisions taken while setting up Run 3 (2026-10-12; listed in QUESTIONS.md)
- Lost-folio prose left out, with a note (as the pilot did with the reconstructed opening).
- Pidal's print order followed where he moves lines; his numbers kept.
- Unnumbered wholly italic lines take provisional letters after the preceding number (181b, 181c, …), as the
  pilot did with 14b, and the note says the letter is ours.
- The six numbers printed nowhere (99, 1043, 2432, 2459, 3663, 3679) and the label 2455 printed twice: follow
  the print; the establishing run checks each on the image (Pidal's footnotes may explain) and records it.
- The pilot's `[Roy]` at v. 15 and v. 58 should be `R[o]y` (only the o is italic); left for the owner.
- Álbar/Álvar Albar[oz] "Álvar Álvarez" in `i` (the -oz form kept in `l`), as in 19-23, 35-39, 95-95.
- coronado "tonsured-one" in `l`, "churchman" in `i` (78-82, 83-83b, 95-95); non … cristiano "no one" (Pidal, vv. 29, 1788).
- Per Vermu[doz] "Per Vermudoz" in `i`; co[m]de don Garcia "Count García" (the Garci Ordóñez of v. 1345, said in the note); sant Esidr[e] "Saint Isidore", from cid-tiradas-96-101.
- onor (la onor) "estate" in `l`, "lands and lordship" in `i`, kept distinct from ondra "honour"; vistas "meeting" in `l` and `i`; amor of lord to vassal "favour" in `i`; Roi/Roy Díaz "Ruy Díaz"; Di[da]go e Ferrando "Diego and Fernando"; una grant ora "for a long while" (Pidal 'un gran rato'), from cid-tiradas-102-102.
- Galind Garçiaz / Galín Garcia[z] "Galín García" in `i` (the manuscript form kept in `l`; vv. 443, 740, 1996, 1999); Mont Mayor "Montemayor" (vv. 738, 1992); Tajo "Tajo" in `i` and titles, not "Tagus"; non son en cuenta "past counting" (cf. v. 918); Hyas = hya (ya) + se, from cid-tiradas-103-104a.
- Pidal's circumflex marks two words run together: ên = e + en "and in" (v. 2035), as lâ, lês, mê, âquel; onor of honour shown at a reception (con tan grand onor, v. 2015) "honour", the house "estate" kept for onor held, given or taken; omillarse a uno "bow (to), greet" (Pidal 'saludarle'), from cid-tiradas-104-104b.
- amor of a vassal toward his lord's act (con vuestro amor, v. 2099) "good will" in `i`, the house "favour" kept for a lord's amor to his vassal; the bishop "Don Jerome" in `i` throughout; escuelas "retinues" in `l`, "my household knights" in `i` (Pidal 'mesnadas', vv. 1360, 2072), from cid-tiradas-104-104c.
- Bare buena (or buen[a]) before çinxiestes/çinxo espada or naçió/nasco is the *en buen ora* formula with ora (and sometimes en) unsaid: "(in) a-good (hour)" in `l`, the house formula in `i`, never "a good sword" (v. 2185); A[n]su[o]r Gonçál[v]ez (v. 2172), brother of the Infantes, "Asur González" in `i` (Pidal's form, note to 2172), the manuscript form kept in `l`; manero "proxy" (Pidal 'representante, apoderado'); reyal "quarters" (Pidal 'real, albergue'), from cid-tiradas-105-108.
- sines al "without anything else" (sines, paragogic sin; al 'other thing'), v. 2255; des = de + es (ese) "of that" (cf. en es día, v. 1678), v. 2275; ca non yo "and not I" (ca non, Pidal 'y no que'); rastados "stayed behind" (Pidal 'han quedado', rastar); duraron of time "spent" (Pidal 'emplearon'), from cid-tiradas-109-111.
- mesnadas "household-troops" in `l` ("my men"/"troops" in `i`), kept distinct from escuelas "retinues"; sí vos vala el Criador "so may the Creator help you" in `i`; Ferran[t] / Di[a]g Gonçal[v]ez "Fernando / Diego González" in `i` (manuscript forms in `l`; the poem states no seniority between the Infantes); Búcar "King Búcar", Quarto "Quarto"; enbaídos "shamed" (Pidal 'avergonzados, corridos'); rebata "alarm"/"a fright" (Pidal 'sobresalto, susto'), from cid-tiradas-112-114.
- Paragogic -e in `l`: the English word stays plain (leal[e] "loyal", vagar[e] "leisure"), as in 01-04; brackets in `l` only for restored words or letters with an English counterpart; fera[ve]/sera[ve]/[estave] = ferá/será/está + -ve; auze "good fortune" in `i`; ensayar in Pidal's three senses (2376 'try', 2381 'attack', 2388 refl. 'exert oneself'); don Pero (v. 2340) "Don Pero" in `i`, the same man as Per Vermudoz, from cid-tiradas-115-117.
- Gonçal[v]o, father of the Infantes, "Count Don Gonzalo" in `i` (co[m]de kept in `l`); Valençia kept so in `l`, "Valencia" in `i`; Tizón "Tizón" (the sword), from cid-tiradas-118-119.
- arras "dower" in `l`, "marriage settlement" in `i` (the husband's gift; Pidal 'las villas y tierras que el varón da a la mujer'), kept distinct from axuvar "trousseau" (the bride's parents' gift; vv. 1649, 2571); never "marriage portion"; Grandes son las nuevas "a great stir" in `i` (Pidal 'gran actividad o animación hay', v. 2588); escurrir "escort" in `l`, "see off" in `i` (Pidal 'despiden', vv. 1067, 2590), from cid-tiradas-124-125.
- mandar of gifts "bestow" (Pidal 'ofreció en don', v. 2585), kept distinct from mandar "order"; saludar of kin or lord "kiss" in `i` (Pidal 'las besó', v. 2601); tener armas "play at arms" (Pidal 'jugando las armas', v. 2613); Valençia la clara "Valencia the bright" in `l`, "Valencia the fair" in `i`; Nos before a verb = non + se (vv. 2569, 2617), kept apart from Nos "we"; darvos e = split future (e = he); (sí) vos vala el Criador: valer "help" in `i`, never "keep"; don Elvira as printed, "Doña Elvira" in `i`, from cid-tiradas-124-125.
- escurrir of an escort on the road (vv. 2640, 2652; Pidal 'acompáñelas … hasta Medinaceli') "escort" in `l` and `i`, the house "see off" kept for a farewell; Acáyaz "Governor" (Pidal 'alcaide', as alcáyaz at v. 1502); Medina "Medinaceli", Salón "the Jalón", Arbuxuelo "Arbujuelo", Anssarera "the Ansarera", Santa María d'Alvarrazín "Santa María de Albarracín" in `i`; barragán "valiant man"; ¿O eres … (v. 2618) O = ó 'where', as at v. 102, from cid-tiradas-126-127.
- montes of wild country "woods" (robredo de Corpes, vv. 2698, 2715, 2751, 2757); robredo "oak-wood"; çiclatones "ciclatons" in `l`, "silken tunics" in `i`; pelliçones "fur-robes"; çinchas "girths"; briales "tunics"; varraganas "concubines", kept apart from barragán "valiant man"; imperative + nos with metathesis (cortandos = cortadnos, cf. dándoslas v. 2081, indos v. 832); apocopated imperfect subjunctive in -ás (fincás, assomas); -dor adjectives one form for both genders (duradores, tajadores); place identifications only from Pidal's notes, from cid-tiradas-128-130.
- Félez Muñoz, the Çid's nephew, so in `l` and `i`; Dí[a]g Téllez "Diego Téllez", Álvar Fáñez's man (Pidal's note to 2822 'vasallo o pechero'); don Urraca "Doña Urraca" in `i`; enffurçión/enfurçión "tribute (in kind)" (Pidal's note to 2822; modern infurción); una grand ora "for a long while" kept (v. 2828); coñosçedores "prudent, discerning" (Pidal 'entendido, prudente'), never "grateful"; mal se ensayaron "did an evil deed" (Pidal 'mala proeza hicieron'); recordar "wake, come round"; "my Çid" in `i`, as in 102–130, from cid-tiradas-131-131.
- juntas "assemblies" in `l`, "an assembly" in `i`; vistas / juntas / cortes "a meeting, or an assembly, or a court" (vv. 2914, 2949; Pidal's notes to 2733, 2963); porteros "officers", the king's summoners (Pidal's note to 2963), never "doorkeepers"; San[t] Fagunt "Sahagún", San Çalvador "Oviedo", Santi Yaguo "Santiago" in `i`; Alcoçeva "the Alcoceba", Bado de Rey kept so (Vadorrey in the note), Rio d'amor "Río d'Amor" (Pidal's notes to 2872, 2875, 2876); desonor "dishonour", like desondra, never the house "estate"; de criazón "bred in the household" (Pidal's note to 2919); Merçed heading a petition "Mercy, O king"; dar derecho a "do right by", aver derecho de "have justice of"; Muño Gustioz so in `l` and `i`, from cid-tiradas-132-133.
- Anrric/Arric "Count Enrique" in `i`, Remond "Count Remond", Fróila, Birbón kept so; sín salve Dios = sí + me "so may God save me" (Pidal's note to 3042 'así me salve Dios'); fazer as a stand-in verb (sí fago, v. 3042); e[n]bair "trample on, ill-treat" (Pidal 'atropellar, maltratar'); espaçio "comfort, solace" (Pidal 'solaz, consuelo'); San Serván "San Servando" in `i`; biltarse "humble oneself", from cid-tiradas-134-136.
- el Crespo de Grañón "the Curly-haired of Grañón" in `i` (Pidal: García Ordóñez); Remont (v. 3109) "Count Remond"; desobra "outrage" (Pidal 'demasía, desmán', his "unknown word"); recabdar (v. 3098) "secure", holding Pidal's two senses; escaño "bench", from cid-tiradas-137-137a.
