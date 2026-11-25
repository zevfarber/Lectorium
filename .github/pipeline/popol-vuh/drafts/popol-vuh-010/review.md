# Review — popol-vuh-010

## Pass 1

Reviewer pass 1, 2026-11-25. I read conventions.md (the rules, the house renderings table and the modern-letters
toggle), runbook.md ("ACTION draft" and the Reviewer paragraph), ../run3/RUNBOOK.md §2, QUESTIONS.md, packet.md (the
established text and the establishment log), popol-vuh-001…009.json, popol-vuh-glossary.json, wordre.py, the 009
review and the draft units.json (76 units). For meaning I used only Brasseur 1861 (OCR lines 21900–22560: K'iche',
French and notes; ch. II "CAPAH CHI TZIH") and the published parts and glossary. I opened no modern translation and
recalled none. Every edit was made by script (json load/dump, ensure_ascii=False, indent=1). No `t` and no `mt` was
changed, and no unit was added, removed or moved. Unit numbers are 0-based, as in the draft's array.

I compared every mt with 001–009 by script (MS form → modern form, lowercased). Two forms differ from a published mt,
and both are deliberate departures that the notes explain: `cochoch` qochoch 'our home' (unit 33; 002 has kochoch
'their home', and unit 25 here keeps kochoch for 'their home'), and `cat` k'at 'burn' (unit 57; 002–009's cat is kat
'you (sg.)', a different word). The forms with more than one published mt (qui, que, ca, chi, cu, cuꜭ, vi, xe, cam)
each fit their sense here: cuꜭ is quk' 'with us' in units 2 and 4 and kuk' 'with them' in 5, 68 and 69, as Brasseur's
own note on uq distinguishes (kuq 'with us', cuq 'with them'); vi is wi' 'top' only in pu vi ha (unit 30), as 003/007;
chi is chi' 'mouth' in units 6 and 38 and chik where it stands for chic (units 12, 38, 39). I then compared the roots of
the new forms with the published mt by script: tacal/tacatoh/tacol/itaca (taq), cahic (qaj), ecouic (ekowik, 007) for
eco, cucah (quk'aj) for xcucah, xquiz (xk'is) for quiz, quizic, caam (k'a'm) for ꜩeen tze'n, libah, huzu(c), nai,
achbilan, bizonic, maihah, choconic, taquen, ꜩihon, chaah, tem, vxic, labe, puz and yaol. All agree with the published
letters. The roots check found two notes that did not match their published parts: puz (unit 64) and yaol (unit 69).

I checked every grammatical label, `l` word by word against the K'iche', `l` against `i`, the couplets, the house table
and every Brasseur claim against the OCR. Every doubtful reading, letter decision and word division in the
establishment log is mentioned in its unit's note: the blots (units 4, 60), heitaca, ixrahpopachih, qui quic, Que calem,
Ahalcana, cohiuoiobeh, xa et culic, iꜭux ivatit, mi xbizonic, hal ha / Nuzivan Cul, chi a / quiqui, ꜫaꜫa, quinicamo /
in, xeghacatah, xeghacovic, taqueh, ahamche, vvach, xahixchiha, xq̄cam, coloquic, hucul, huzuc, equiꜩiha, çaquiric,
chiquizic, xha, the t-i ligature of tihobal, quia molah, the plain z of ziban and xqui zac against Xꜩac, the q-shaped
qux, and ꜭohul. None was missing.

The drafter's restored ejectives and glottal stops, judged one by one:
- `caztah` k'astaj. Kept: Brasseur has qaztah (q = ꜭ), and the root ꜭaz 'live' (ꜭazlem) is known.
- `mecoh` meq'oj. Kept: Brasseur has megoh (g = ꜫ), and his 'réchauffez' fits meq' 'warm'. The note marks the reading
  inferred, as 009 did for ketz'ab'al.
- `catanalah` k'atanalaj, `cat`/`xcat` k'at / xk'at. Kept: Brasseur has qatanalah and qat ('pierre incandescente',
  'ils se brûlaient'). The burn word is known.
- `zic`/`izic` sik', isik'. Kept: Brasseur has ziq, his note makes it tobacco and the cigar, and the word is known.
- `quizic` k'isik, `quiz` k'is. Kept: Brasseur has qiziq and qiz, and 006–008 publish xquiz as xk'is.
- `queca` q'eqa. Kept: it is the black of four colour words, the root of queꜫum q'equm (house table), and Brasseur
  has geka. The first letter is not in doubt.
- `ꜩe` tze', `ꜩeen` tze'n. Kept: only the glottal stop is supplied, and the tz stays plain. In ꜩeen the double e is
  Ximénez's own mark for the glottal stop, as in 001's caam k'a'm.
- `quic` kik', `quiqui` kik'i, `quiquib` kik'ib'. Kept: they match 009 and the glossary (Brasseur quiq, quiqi, quiqib).
- Left letter for letter by the drafter, and kept so: ꜫaꜫa q'aq'a and caꜫ kaq' (the tresillo is written, though
  modern 'red' is kaq), eco eko (Brasseur eqo), quzquz kuskus, quihila kijila, caza kasa, cala kala, ꜭhacatah ch'akataj
  beside chacatah chakataj, ziban siban, ꜩuan tzuan, culic kulik, calem kalem, chab chab', vxic uxik.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 76 units, and the units' `t`, joined in order
with a space, give back the packet's 18 paragraphs exactly.

Counts: **major 0 · minor 9 · style 12** (21 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 1 | n | minor | It said that he "is read with Brasseur as a form of the verb 'go' whose 'we' form is the Ho na of ¶6". Brasseur's note says something more specific: he stands for ho-e, the third person plural of the subjunctive ('that they go'), though his French has 'allez, vous'. | The note gives his analysis. It keeps the doubt about whose 'go' this is, and points to Ho na (¶6) and hix (¶15). |
| 2 | n | minor | "opon is to arrive at a place away from the speaker …, so the summons is spoken from Xibalba's side." The argument runs backwards. A journey to Xibalba called opon 'arrive there' is spoken from away from Xibalba, by the messengers at the ball court. | "the words are framed for the messengers to say at the ball court, of a journey there, to Xibalba, while the lords' own wish in the next lines uses vl 'come here' (inferred)". |
| 26 | n | minor | "as Brasseur's note gives its forms (hin 'let me go', ho 'let us go')". His note (at ¶1) names the verb Ho 'aller' and gives hin (ho-in), hat (ho-at) and he (ho-e). It does not give a form 'let us go'. The note also missed that Brasseur divides k'ulic, his k standing for q. | The note quotes his forms exactly and marks 'we' as inferred. It adds that his k'-ulic would be q- 'our' + vl + -ic 'our arrival', which suits his 'notre voyage sera inutile' (inferred). The mt stays kulik, letter for letter. |
| 30, 37 | l, n | minor | "pu is pa 'in' (Brasseur's note)". Brasseur's note (at ¶8, pu beal) says pu stands for pa u, contracted p'u, 'dans le'. That is, pa + v- 'its', which the l lines did not show. | l "in-its top house", "in-its road". Both notes give his words. Unit 30's note also points to the glossary's pu chi'. |
| 32 | i | minor | "You are only to play the flute and sing". The l says make-music, and the note links ꜩuan to zu 'flute' only as an inference, against the letter (tz ligature, not z). Brasseur has 'faites de la musique'. | "You are only to make music and sing". |
| 51 | n | minor | It did not say that Brasseur's French renders xqui chac 'qu'ils venaient de jouer' (whom they had just tricked). That is another reading of the verb the English gives as 'beaten'. | Added. 'beaten' is now said to follow his note on chacomahic (inferred). |
| 64 | n | minor | "puz, the word of sacrifice in earlier parts". Its only published use is 001:43, where puz is paired with naual as a word of power. 001's note and the glossary call its sense uncertain, "often connected with sacrifice". | "puz, the word set beside naual in the first part, where its sense is uncertain and often connected with sacrifice". |
| 66 | n | minor | "Brasseur says the whole verse is very hard to translate". His note 'Tout ce verset est d'une traduction fort difficile' belongs to the laughter verse (unit 60, 'menaçaient d'être frappés d'apoplexie (1)'), where note 60 already cites it. His note at this sentence is the one on cha / chah / chaah. | The misattribution is removed. The note now says that his note here is on the play of cha, chah and chaah. |
| 68, 69, 71 | i | minor | 68 said "their torches were brought in to them: a single torch". This contradicts itself. The K'iche' xa hun chi chah 'only one torch' is singular, and so are xqui quiz ri chah (unit 74) and the i of 74 "the torch". Units 69 and 71 had "their torches". | 68 "Then their torch was brought in to them: a single torch …". 69 "the bearer of their torch and their cigars". 71 "They were to light their torch, and each his cigar". |
| 5 | n | style | The first ca is "left unexplained". The note did not say that Brasseur prints ka for both (his k = q), that is, ca- 'we' twice ('que nous vivifiions nos visages'). | Added. The mt stays ka, since the reading is uncertain. |
| 6 | n | style | "The marvelling is surely ironic." This is an interpretation stated as certain. | "perhaps ironic (inferred)". |
| 10 | n | style | "(his note: cha is the word, the arrow …)". Brasseur has no note on Chabi. The note quoted is his note on cha at the torch (¶17). | "(his note on cha at the torch, ¶17: …; his French 'Flèche-de-Hibou')". |
| 23, 53 | l | style | Vꜩ bala was l "Good indeed". The house table gives l "good bala", and 008 has "Good bala". | l "Good bala". |
| 25 | n | style | "only the grandmother Xmucane is left". To the speakers she is their mother (qui chuch), as the next line says. | "only their mother Xmucane, the grandmother of Hunbaꜩ and Hunchouen, is left". |
| 33 | n | style | It did not mention that Brasseur himself writes k'ochoch here (his k = q, 'our') against c'ochoch 'their' in unit 25, which supports the qochoch departure. It also glossed his u qux vv'atit as "'her heart'", while his French is 'le cœur de votre aïeule'. | Both added or corrected. |
| 39 | n | style | "(Brasseur eqo, 'they passed')". The toggle question turns on his q (= ꜭ), and he writes iqo / iqou for icou, but the note did not say so. | Added. eco stays eko, letter for letter. |
| 44 | n | style | "The colour words take -a." zaqui takes -i. | "ꜫaꜫa, queca and ꜫana take -a, zaqui -i." |
| 58 | n | style | "culibal 'their seat'". 'their' is qui, which is not part of culibal. Brasseur's OCR vacamaric (against yacamaric) was not mentioned. | "culibal 'seat'". Added "(Brasseur's OCR has vacamaric)". |
| 62 | n | style | "(Brasseur 'the Gloomy House')": a loose gloss of his 'la Maison Ténébreuse'. | Quoted as he has it. |
| 68 | n | style | "uꜭ 'with' comes four times in this sentence". There are three in this unit. Brasseur's count of four includes the cuꜭ of the next sentence (unit 69), which his note quotes. | "four times here, three in this sentence and the cuꜭ of the next". |
| 69 | n | style | yaol "(as in the last part; inferred)". 009 reads yaol as 'given' (glossary: "given, giving"), not 'giver'. | "(the form of the last part's yaol, read there 'given'; inferred)". |

### Refused / left

- **The restored ejectives and glottal stops** (k'astaj, meq'oj, k'atanalaj, k'at, sik', k'isik, q'eqa, tze'/tze'n,
  kik'): all kept, for the reasons given above.
- **`cochoch` qochoch (unit 33) and `cat` k'at (unit 57)** against the published kochoch and kat: kept. Both are other
  words or senses, and the notes say so. Brasseur supports both letters (k'ochoch, qat).
- **`Ahalcana` Ajalq'ana / "Ahalq'ana" (unit 17)** against the plain c of the MS: kept. It is the same lord as 009's
  Ahalꜫana, Brasseur has g in both, and the note says the letter differs.
- **The owls' names translated in `i`** (Arrow Owl, One-Leg Owl, Macaw Owl, Head Owl) while Vucub Caquix and Huracan
  stay K'iche': kept. The text itself explains each name in the next two sentences, Brasseur translates them the same
  way (Flèche-de-Hibou, Une-Jambe-de-Hibou, l'Ara-Hibou, la Tête-de-Hibou), and the note gives the reason. For
  QUESTIONS (below).
- **`poy`, `aham che` split** ("an effigy … a figure of carved wood", unit 48) against the house rendering "the
  effigies carved of wood": kept. Here they are two figures, greeted one by one as Huncame and Vucub Came (unit 49).
- **Unit 68 "a single torch"** against Brasseur's 'à chacun d'eux son écharde': kept. The K'iche' says xa hun chi chah
  'only one torch', and the sentences after it keep the singular.
- **Unit 5's first ca** (mt ka) against Brasseur's ka (= qa): kept letter for letter. The form is unclear, and the note
  now gives both readings.
- **Unit 20 "Truly indeed"** for quiꜩih bala: kept. The house table fixes only Vꜩ bala.
- **Unit 28 `toc`**: Brasseur's OCR seems to read `Que pe ca cha-cut` without toc. The OCR line is poor, and the MS is
  the text, so nothing was added.
- **Unit 14 `e cu tacal` 'alighted'** against Brasseur's 'porteurs de leur message': kept, with 005's tacal (glossary
  'set, come to rest').
- **`chuꜭhaxic` l "it-is-called" (unit 15)** against the house table's "it-is-said": kept, on the precedent of 001 and
  009 pass 2.
- **Names in `l` in MS spelling** (Vvcub Came, Vvcub Hunahpu, Hunbaꜩ): kept, as in 009.
- **The about**: checked against the units. Every event is there, in order. No change.

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. **Drafter's proposed renderings, not added to the house table meanwhile:** the four owls translated as epithets
   (Arrow Owl, One-Leg Owl, Macaw Owl, Head Owl; mt keeps the K'iche'); Queꜫuma Ha 'the Dark House'; rahpop achih
   'captains of the warriors' (after Brasseur's 'capitaine des gardes'); Nim Xob Carchah kept as a name; tem 'bench'.
2. **The written tresillo in a known word without the ejective:** ꜫaꜫa 'red' (modern kaq) is given q'aq'a, letter for
   letter, while queca 'black' is given q'eqa, restored. The conventions allow restoring but say nothing about a
   written ejective that the modern word lacks. caꜫ (unit 12) is the same case.
3. **The chac / chacatah family:** Brasseur writes k (= q) throughout (chakatah, chakomahic, chak). The mt follows 009
   (chak, chakataj). The one ꜭhacatah (unit 46) gives ch'akataj. Decide together with 009 question 2 and modern ch'ak.
4. **eco eko against icou ik'ow:** Brasseur writes q (= ꜭ) in both (eqo, iqou). If they are one verb, eco should be
   ek'o.
5. **The 'go' verb (he, ho, hix):** Brasseur makes he ho-e 'that they go'. The glosser needs entries for all three.
6. **For the glosser:** vxic 'wings' (units 11–12) broadens 004's uncertain entry; tem 'bench' broadens 'holding';
   pu 'in its' (pa + u, Brasseur) broadens 'in, at'; yaol here is the agent 'bearer', against the entry's 'given'.

## Pass 2

Reviewer pass 2, 2026-11-25 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
QUESTIONS.md, packet.md (text and establishment log), popol-vuh-001…009.json, popol-vuh-glossary.json, wordre.py, the
009 review (its pass 2), pass 1 above, units.json as pass 1 left it, gloss.json, novel-forms.json and known-forms.json.
For meaning I used only Brasseur 1861 (OCR lines 21900–22560, and 17567 / 34317 for Cavizimah) and the glossary. I
opened no modern translation and recalled none. Every edit was made by script (json load/dump, ensure_ascii=False,
indent=1). No `t` was changed, and no unit was added, removed or moved. Unit numbers are 0-based.

Units: I went through all 76 again: grammar labels against forms, K'iche' → l word by word, l ↔ i, couplets, the house
table, uncertainty labels, the establishment-log items (all covered, as pass 1 found) and the about. I re-checked every
Brasseur claim in the notes against the OCR; all hold except the Cavizimah gloss (unit 39), which was shortened. I re-ran
the MS form → mt comparison against 001–009 (same two deliberate departures as pass 1: qochoch, k'at) and then a letter
check on every mt (no v, z, c or non-ch h left; one b' per MS b; one j per MS h outside ch/ꜭh). That check found two
respelling slips pass 1 missed: `Cahulhut` → Kajulhut (an h left unrespelled) and `ziban` → siban (b without its ').

Gloss: I checked all 119 entries and every `__broaden__` value against the units and the final mt, by script and by
reading. Keys equal novel-forms.json exactly; every head equals the units' mt (compared lowercased); every broadening
begins with the current glossary entry verbatim + " · ". I then compared every known form's use in 010 with its glossary
entry (185 forms). Pass 1's four requests were open: the glosser broadened `tem` only, and not `vxic`, `pu` or `yaol`.
The same check found six more known forms used in a sense the glossary lacks: `cha`, `zac`, `bala`, `choc`, `huracan`,
`mi`, plus `cul` in a name. Several entries carried Sonnet errors: a false Brasseur attribution (`ho`), the claim pass 1
had already removed from unit 64 (`puzu`), an invented form (`ajtzib'` in `ziban`), an invented root (`wal` in `valehic`),
a wrong morphology (`toc` 'let them'), and person markers that belong to other words (`humuhub`, `oponic`).

Afterwards: the JSON parses; len(mt) == len(WORD_RE.findall(t)) for all 76 units; the units' `t`, joined in order, give
back the packet's 18 paragraphs exactly, and each paragraph is tiled by whole units; gloss keys == novel-forms keys
(+ `__broaden__`), every head matches the mt, every broadening prefix checks. Final gloss: 119 novel forms, 19 broadened.

Counts: **major 0 · minor 19 · style 15** (34 findings: units 7 (minor 4, style 3); gloss 27 (minor 15, style 12)).

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 70 | mt | minor | `Cahulhut` was given Kajulhut: the second h was left unrespelled (h → j). | Kajuljut. Gloss head changed with it. |
| 32 | mt, n | minor | `ziban` was given siban: the b was not respelled b' (the rule respells every b; cf. ajtz'ib'enai). | mt sib'an; the note's "(siban)" → "(sib'an)". Gloss head changed with it. |
| 62 | n | minor | "oponic 'they arrived there', with -ic at the end of the clause". It is not clause-final: pa Queꜫuma Ha follows. | "xe oponic 'they arrived there': opon + -ic, here kept before the place phrase pa Queꜫuma Ha." |
| about | — | minor | "sent to the Dark House with a lit torch and a lit cigar each": after pass 1 made unit 68 "a single torch … each one's cigar", the about still gave each brother a torch. Also "Xmucane weeps" states Brasseur's French as the text's, where unit 34 marks quzquz 'grief' a guess. | "with a single lit torch and a lit cigar each"; "Xmucane is overcome with grief". |
| 32 | n | style | "four verbs in -an": coton ends in -on. | "four verbs in -an (coton in -on)". |
| 64 | n | style | "que 'them' + ca- 'we'": que is c- + e 'them' (the same relabelling 009 pass 2 made). | "que, c- (ongoing) + e 'them', + ca- 'we'". |
| 39 | n | style | Cavizimah "'adorned calabash tree'": Brasseur (OCR 34317) has 'calebassier orné ou armé'. | Quoted in full: "adorned or armed calabash tree". |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| ho | value | minor | "(ho 'let us go', after Brasseur)": Brasseur gives no such form (pass 1 corrected the same claim in unit 26); 'we' is inferred, unmarked. Head capitalised (Jo). | "jo — (inferred) we go, let us go; the verb 'go' (Brasseur names it Ho 'aller', with hin …, he …); the person 'we' is inferred". |
| toc | value | minor | "(inferred) let them": toc is the end of petoc written apart (pet + -oc), not a word 'let them' (unit 28's note). | "toq — the end of petoq 'come' written apart …: the t of pet + -oq". |
| puzu | value | minor | "puz, the word of sacrifice in earlier parts": the claim pass 1 removed from unit 64; the glossary's pus is 'sacred power (exact sense uncertain); often connected with sacrifice'. | Brought into line with unit 64. |
| ziban | value | minor | "the tzib' … of ajtzib'": no such entry; the word is tz'ib' of ajtz'ib'enai (unit 32). Head siban. | "sib'an — … the tz'ib' 'write, paint' of ajtz'ib'enai, but written with the plain z …". |
| ꜩuan | value | minor | "make music, play the flute; … tzu 'flute'": pass 1 removed 'flute' from i as an inference; the flute word is su (ajsu), not tzu. | "make music; … perhaps the su 'flute' of ajsu, though written with the tz ligature". |
| valehic | value | minor | "from wal 'rise' + -ej + -ik": an invented root; the note gives only 'rise up' (inferred) after Brasseur. | "(inferred) rising up, getting up; not otherwise known, after Brasseur ('voulant se lever')". |
| quiqui | value | minor | Not marked doubtful, though the note and the log call the reading (qui qui joined) doubtful. | Doubtful reading stated; Brasseur's chi quiqi-a given. |
| cahulhut | value | minor | Head Kajulhut (see unit 70). | kajuljut. |
| __broaden__ vxic | new | minor | Glossary: 'becoming' / '(uncertain) finery … or perhaps xik' wing; paired with vpuvac'. Units 11–12 read 'its wings'. Pass 1 asked; not supplied. | Added "uxik — (inferred) its wings; u- + xik 'wing' (modern xik'), after Brasseur ('des ailes') …". |
| __broaden__ pu | new | minor | Glossary: 'also' / 'in, at'. Units 30, 37 read pu as pa + u- 'in its' (Brasseur's note). Pass 1 asked; not supplied. | Added "pu — in its, in the; pa 'in' + u- 'its' contracted …". |
| __broaden__ yaol | new | minor | Glossary: '(inferred) given, giving'. Unit 69 reads the agent 'giver, bearer'. Pass 1 asked; not supplied. | Added "yaol — (inferred) giver, bearer …". |
| __broaden__ cha | new | minor | Glossary: 'say' / 'at your'. Unit 65 reads cha 'flint (?)', arrow point (Brasseur's note). | Added "cha — (guess) arrow point, flint …". |
| __broaden__ zac | new | minor | Glossary: 'white, light' / 'white dice'. Unit 16 reads xqui zac … qui ꜩih 'they made clear their word', a verb. | Added "saq — (inferred) make clear, speak out …". |
| __broaden__ huracan | new | minor | Glossary: the Heart of Sky's name only. Units 10–11 use it as the owl's name 'One-Leg', which the text itself explains. | Added "Juraqan — One-Leg, in Juraqan Tukur 'One-Leg Owl' …". |
| __broaden__ mi | new | minor | Glossary: 'now, just now'. Unit 35 l reads mi xbizonic 'do-not(?) grieve'. | Added "mi — (inferred) do not, before a verb …; the form is not clear". |
| oponic | value | style | "they arrived there": 'they' is xe; and the clause-final -ic label (unit 62) does not fit. | "arrived there; opon + -ik, the ending of an intransitive verb". |
| culibal | value | style | "from a root 'sit'": no root named or known. | "a noun of place in -ib'al, after Brasseur ('siège')". |
| calem | value | style | "(perhaps c- + e 'they' + a verb)": that describes que, not calem; the doubtful letter not said. | Doubtful reading (looped l) stated; left out of the English. |
| humuhub | value | style | "they roared": 'they' is xe. | "roar with laughter, burst out laughing; after Brasseur ('éclataient de rire')". |
| ꜫaꜫa | value | style | "the letters of kaq 'red' respelled with the tresillo": kaq has no tresillo; unmarked as inferred. | "(inferred) red; a colour word in -a, written with two tresillos (Brasseur caka, 'rouge') …". |
| eco | value | style | "the verb of ik'ow" stated as fact; the unrestored ejective unexplained. | "taken as the verb of ekowik and of ik'ow …; the ejective not restored". |
| culic | value | style | Brasseur's k'ulic 'our arrival' option (unit 26) missing. | Added. |
| tucur, quzquz, xyaic, cala | head | style | Heads capitalised (Tukur, Kuskus, Xyaik, Kala) from a sentence-initial mt; glossary heads of common words are lower case (e.g. k'atek'ut). | Lower-cased. |
| __broaden__ tem | value | style | The glosser's "taken as a noun 'seat', not 'holding'" argues with the old entry and omits Brasseur. | "tem — (inferred) bench, seat; noun (qa tem 'our bench'), after Brasseur ('siège d'honneur'); tem is the modern word for a bench". |
| __broaden__ bala | new | style | Glossary covers only Vꜩ bala; units 20 read quiꜩih bala 'truly indeed'. | Added "b'ala — (inferred) indeed; strengthens the word before it". |
| __broaden__ choc | new | style | Glossary: 'let it enter; ch- (wish)'. Unit 34 is narrative ('it enters, came over'). | Added "chok — it enters, comes over (in narrative, not a wish) …". |
| __broaden__ cul | new | style | The name Nuzivan Cul: the glossary's kul senses are 'it comes', 'coat', 'throat (in chi kul)'. | Added "Kul — (inferred) throat, gorge, in the name of the ravine Nusiwan Kul (Brasseur 'ma ravine de gorge')". |

### Refused / left

- **The glosser's other broadenings are kept**: ꜩihon 'lit', quic 'rubber', que qe 'us', cochoch qochoch, cat k'at, cah
  qaj, a 'river', na 'first'. Each is a sense the entry lacks and the units use.
- **No broadening** for ꜩac (Xꜩac qui ꜩih 'their word fell' is under 'fall'), oc 'already' (under 'yet, still', as 009
  pass 2), chi 'for' in chi varabal (under 'at, in, to'), yao 'given' in xha yao (under 'give'), vtuquel 'only'
  (under 'by itself, alone'), chaah 'game' (under 'play', as 009 pass 2), hal (under 'change').
- **Unit 9 xe vꜭhaxic**: the note analyses vꜭhaxic without naming v-; left, as the glossary entry gives u- and 009 does
  the same.
- **Unit 21 l "We then (cu)"** for Oh na cu: the 'then' stands for na; left.
- **Unit 2 opon**: Brasseur's text has `Qu'yx apon kuq`; the MS (established) has opon and the note's reading does not
  depend on the vowel. Left; for the establisher (below).
- **Pass 1's decisions all stand**: the restored ejectives, qochoch / k'at, the owl names translated in i, the split of
  poy / aham che, the single torch, Ahalq'ana, "it-is-called" for chuꜭhaxic. I re-checked each against the OCR.
- **The house table**: Vꜩ bala, poy / aham che, queꜫum, ahau, chuꜭhaxic, Hunhunahpu as written: all as pass 1 left them.

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. Pass 1's six points stand; its point 6 (the glosser's broadenings) is now done (vxic, tem, pu, yaol).
2. **For the establisher** (Brasseur differs and the establishment log is silent; the MS is the text): ¶1 `Quix opon cuꜭ`
   (Brasseur apon); ¶16 `rumal vi queꜩabal` (Brasseur rumal ri qu'etzabal, no vi); ¶3 `xe vlic, e cu tacal` (Brasseur
   x-e ulic cu takal, no e). Worth a look at the image when 010 is revisited.
3. No new house rendering in this pass.
