# Review — popol-vuh-009

## Pass 1

Reviewer pass 1, 2026-11-25. I read conventions.md (the rules, the house renderings table and the modern-letters
toggle), runbook.md ("ACTION draft" and the Reviewer paragraph), ../run3/RUNBOOK.md §2, packet.md (the established text
and the establishment log), QUESTIONS.md, popol-vuh-001…008.json, popol-vuh-glossary.json, wordre.py, the 008 review
and the draft units.json (43 units). For meaning I used only Brasseur 1861 (OCR lines 21320–21990: K'iche', French and
notes) and the published parts. I opened no modern translation and recalled none. Every edit was made by script (json
load/dump, ensure_ascii=False, indent=1). No `t` was changed, and no unit was added, removed or moved. Unit numbers are
0-based, as in the draft's array.

I compared every mt with 001–008 by script (MS form → modern form, lowercased). Two forms differ from a published mt,
both deliberate departures: `chacab` chakab' (007 chaq'ab') and `cuc` kuk (001 q'uq'). Both are kept (see Refused). The
forms with more than one published mt (ca, chi, cu, vi, oc, que, quib, xe, cam, cah, ha, chique, cumal) each fit their
sense here. I then compared the roots of the new forms with the published mt (taq/taca, cotob, tocob, cat/catol, alcual,
cutun, puvac, raih, caubal, vcul, eꜩ, camou). That check found the `camouic` mismatch with 006 and the `queꜩabal` /
006 `eꜩeyah` split (below). I checked every grammatical label, `l` word by word against the K'iche', `l` against `i`,
the couplets, the house table and the name spellings. Every cross-reference to an earlier part was checked by script,
and every Brasseur claim against the OCR. Every doubtful reading, letter decision and supralinear word in the
establishment log is now mentioned in its unit's note. Two were missing before this pass: the joined `hun baꜩ, hun
chouen` and `hun came`.

The drafter's departures that were checked:
- `xquicutu` xkik'utu. Kept: 001 has uk'utunisaxik and 008 has xk'utun, and Brasseur has q (= ꜭ).
- `ralcualah` ralk'walaj. Kept: 006 has iwalk'wal.
- `quic` kik'. Kept: the word is certain.
- `catol` q'atol. Kept: 006 has xkiq'at, and Brasseur has g.
- `Ahaltocob` Ajaltoq'ob'. Kept: 006 has toq'ob'aj, 007 has toq'ob', and Brasseur has g.
- `ꜫana`, `Chuꜫanal`, `Ahalꜫana` q'-. Kept: the tresillo is in the MS, and 008 has ꜫan q'an.
- `pachcab` pachq'ab'. Kept: 008 has vcab uq'ab', and Brasseur has g.
- `ahꜩibenai` ajtz'ib'enai. Kept: 001 has xchiqatz'ib'aj.
- `queꜩabal` ketz'ab'al. Kept, but see the questions below.
- `cuxic` quxik. Kept: Brasseur has k'uxic, and 008 has qumal.
- `tacoc` taqoq. Kept: 007 has taqa, and Brasseur has tak-oc.
- `qui ꜩih` qi tzij. Kept: it follows the published quiꜩih qitzij, and the note says so.
- `vve` we. Changed to uwe.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 43 units, and the units' `t`, joined in order,
give back the packet's 15 paragraphs exactly.

Counts: **major 0 · minor 12 · style 6** (18 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 7, 11, 12, 17, 42 | mt, n | minor | `Hunbaꜩ` was Junb'atz with a plain tz. The reason given was that the MS has the plain ligature. But the same part restores tz' in ajtz'ib'enai and ketz'ab'al against the plain ligature, and 005 gave Ꜩiz Tz'iis. The day name and the word b'atz' 'thread, monkey' are certain. | mt Junb'atz' (6 tokens). Note 7 says why. |
| 7 | n | minor | "chouen is a day name of unclear meaning", and the two names were called "two of the twenty days". Brasseur's note gives batz as the 11th day of the K'iche' count and chouen as the 11th day of the Maya (Yucatec) count. | The note gives Brasseur's note. It says the two may be the same day in two languages (inferred). |
| 4, 7 | n | minor | Note 4 said "Brasseur notes that here it seems to stand for both brothers". That note of his belongs to `e caib xe ralcualah` (unit 7: 'ces Hunhun-Ahpu étaient deux'). At unit 4 his French is 'Leur nom à chacun est Ahpu'. | Note 4 now quotes his French. Note 7 now gives his other reading of e caib, against the drafter's 'two sons'. |
| 24 | l, i, n | minor | `l` made quic the subject ("the blood it-sickens person"), but `i` made it the object ("to sicken people's blood"). The note also had Brasseur read Xiquiripat as xic 'hawk' + ripat. In fact he glosses the whole name 'hotte volante'. 'épervier' is his gloss for Xic in unit 34. | l "that-it-sickens". i "their office was the blood, that it should make people sick." The note now gives Brasseur's glosses as they are and labels ch- + u- 'it' (the blood, taken as subject). |
| 29 | mt, l, i, n | minor | `camouic` was labelled "'dying': cam 'die' … as 005's xcamou". 005 reads xcamou as possibly 'take', and 006's xcamouic is k'am 'take' (xk'amowik). Brasseur prints qamouic (q = ꜭ) and renders it 'un squelette à prendre'. The draft's own `i` already said "taken up". | mt k'amowik (as 006). l "at taking(?)". i "there was only bare bone to take up". The note now gives the reading and Brasseur's letter. |
| 32 | mt, n | minor | `vve` → we drops a letter, and the word is not certain enough for that. Brasseur divides it u ve (uve tzamez). Ximénez's vv is elsewhere uw/wu (vvach uwach, vvcub wuqub'). | mt uwe (letter for letter). The note gives Brasseur's division. |
| 32 | n | minor | It did not say that Brasseur renders `hupul oc` 'tomber la bouche en l'air' (mouth upward). That is the opposite of the 'face down' that 007/008 adopted. The question is open in QUESTIONS (007 5, 008 1). | Added. The English keeps the 007/008 reading. |
| 39 | l, i, n | minor | "yoke(s)" for `bate`. Nothing in the K'iche' or in Brasseur ('anneaux') gives it, and it reads as remembered English. "face-ring(?)" / "face rings" for vachzot is grounded nowhere either (the note itself says "headgear or face-pieces"). | l "ring(?)", "face-piece(?)". i "their rings … their headdresses and face-pieces". The note says bate = ring (Brasseur 'anneaux'; guess). |
| 39 | n | minor | It did not say that Brasseur's French makes queꜩabal the lords' wish 'to hold up to scorn' (livrer au mépris) the brothers and their gear. That is another reading of the word that the toggle restores as etz'ab'al. | Added. 'gear for play' is marked inferred. |
| 20 | n | minor | "from taꜫ 'send for'". The tresillo spells q' (taq'), but mt taqoq, 007's taqa and Brasseur's tak-oc (k = q) all have plain q. | "from taq 'send, send for' (Brasseur tak-oc, his k standing for q)". |
| 21 | n | minor | "as 008's pa qui vi". 008 has no pa qui vi. The phrase is in 003 (3:27) and 007 (7:26). | "as pa qui vi in 003 and 007". |
| 7, 18 | n | minor | The establishment log's joined names `hun baꜩ, hun chouen` and `hun came` were not mentioned (only `vvcub hun ahpu` was, in unit 6). | Added "(MS hun baꜩ, hun chouen, joined as in earlier parts)" and "(MS hun came, joined as Huncame)". |
| 6 | n | style | "Brasseur's note takes 'in the night' as 'before the dawn'". He has 'avant la marche de leur soleil (de leur calendrier, de leurs institutions)'. | Paraphrased exactly. |
| 17 | n | style | "in a line Brasseur's OCR partly lost". The OCR has `x-caminak ca cut qui`, moved to another line, not lost. | "Brasseur too has x-caminak ca cut (the OCR displaces it to another line)". |
| 36 | n | style | cozih: Brasseur's g (gozih) was not mentioned, though the toggle respells the c. | Added. |
| 38 | n | style | It did not mention 001's `xqui cuch qui ꜩih, qui naoh` 'they joined their word, their thought', the same gathering of naoh. cuc may be that verb. | Added as inferred. mt stays kuk. |
| 40 | n | style | biye was glossed "(bin 'walk, go')". bin is 'walk', and 'go' is be. | "(perhaps be 'go', or bin 'walk'; Brasseur 'leur voyage')". |
| 24 | n | style | "chu yabih 'he sickens'": with quic as subject, the u- is 'it'. | Relabelled (part of the row above). |

### Refused / left

- **`chacab` chakab' (unit 2) against 007's chaq'ab' 'by night'.** Kept. Here Brasseur has xa chakab 'seulement une
  partie' (k = q), where in 007 he has ch'agab. The pairing with nicah 'half' supports 'a part'. The word is uncertain, so
  the letters are respelled. The note names 007's reading. Raised for QUESTIONS.
- **`cuc` kuk (unit 38) against 001's cuc q'uq' 'quetzal feathers'.** Kept. It is a different word. Brasseur has c'uq, and
  the note now points to 001's cuch.
- **`qui ꜩih` qi tzij (unit 29).** Kept. It follows the published quiꜩih qitzij (004–008), and Brasseur prints quitzih.
  This is the only `qui` in 001–009 with mt qi; the note explains it. The glosser should broaden `qui`.
- **Restored ejectives kept**, for the reasons in the method paragraph: xkik'utu, ralk'walaj, kik', q'atol, Ajaltoq'ob',
  q'ana / Chuq'anal / Ajalq'ana, pachq'ab', ajtz'ib'enai, ketz'ab'al.
- **Letter for letter kept:** chak (unit 20, modern ch'ak 'win' not shown), tokota, kosij, ukulel, kul (unit 36: 008's vcul
  is uqul 'neck', but here the sense 'throat' is Brasseur's guess), tzuun, b'ate, yachwach, wachsot, ajkot (with 006's
  koto), Wok, Kuchumakik, Xikiripat.
- **`Vcub` Wuqub' (unit 13).** Kept. The word is certain, and the note says that the MS has one v.
- **Names in `l` in MS spelling** (Vvcub Hunahpu, Hunbaꜩ, Ahalꜫana): kept, on the precedent of 007's `Moꜩ` in `l`.
  Vucub Caquix's "Seven Macaw" comes from the house table and is not extended to Vvcub Hunahpu.
- **Unit 7 `e caib xe ralcualah` "two were born to him"**: kept. xe- (3pl absolutive) with r- (3sg ergative) fits 'he had
  them as children' better than Brasseur's 'these Hunhun-Ahpu were two'. Both readings are now in the note.
- **Unit 14 `cacab` "two by two"** against Brasseur's 'tous les deux jours': kept. The note gives both.
- **Unit 32 `vve ꜩamez` covered by "wherever"** in `i`: kept, because the note says so (Brasseur 'avec la trahison').
- **The about**: checked against the units. Every event is there, in order. No change.
- **For the glosser / pass 2:** `hunbaꜩ` is Junb'atz'. `camouic` is k'amowik 'taking' (inferred). `vve` is uwe. `bate` is
  'ring (guess)', not yoke. `qui` needs a broadening (qi, in qi tzij). `tacoc` comes from taq, not taq'. `chacab` needs a
  broadening ('a part', inferred, chakab').

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. **tz' against the plain ligature.** Hunbaꜩ is now Junb'atz', with ajtz'ib'enai, ketz'ab'al and 005's Tz'iis: the
   known word decides. 006's `eꜩeyah` 'playing' was given etzeyaj with a plain tz. If it is etz' 'play', as queꜩabal
   ketz'ab'al is here, 006 should be revised together with it.
2. **`chacab`**: chaq'ab' 'by night' in 007 and chakab' 'a part' in 009. These are the same letters read two ways, and
   Brasseur's letters differ too (ch'agab / chakab).
3. **`vve`** (unit 32) is uwe, letter for letter (Brasseur uve). The drafter proposed we ('if'). This is the same question
   as 008's vv after ca/qui (wu) against 005's vvb (uub').
4. **The 'take' verb** (QUESTIONS 007 3, 008 3): `chi camouic` is now k'amowik, with 006's xcamouic and Brasseur's q.
   005's xcamou is still kamow.
5. **hupul / pacal** (QUESTIONS 007 5, 008 1): in unit 32 Brasseur renders hupul-oc 'la bouche en l'air' (face up), which
   is opposite to the 'face down' of 007/008. The English keeps 007/008's reading. The owner should decide the reading of
   hupul for 007–009 together.
6. **`cuc` (unit 38) against 001's `cuch`** in the same phrase with naoh. Respelled kuk. It may be the same verb.
7. **`cul` 'throat' (unit 36) kul against 008's vcul uqul 'neck'.** Both are left as they are. Decide them together if
   they are one word.
8. **`bate`**: "yoke" was removed as not grounded. If the owner has a source for the ball-game sense, the note can say
   so.
9. No new house rendering in this part.

## Pass 2

Reviewer pass 2, 2026-11-25 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
packet.md (text and establishment log), QUESTIONS.md, popol-vuh-001…008.json, popol-vuh-glossary.json, wordre.py, the
008 review (its pass 2), units.json as left by pass 1, pass 1's review, gloss.json, novel-forms.json and
known-forms.json. For meaning I used only Brasseur 1861 (OCR lines 21320–21990: K'iche', French and notes) and the
glossary. I opened no modern translation and recalled none. Every edit was made by script (json load/dump,
ensure_ascii=False, indent=1). No `t` was changed, and no unit was added, removed or moved. Unit numbers are 0-based.

Units: I went through all 43 again: grammar labels against forms, K'iche' → l word by word, l ↔ i, couplets, the house
table, uncertainty labels, every establishment-log item (all are covered) and the about (no change). I re-checked every
Brasseur claim in the notes against the OCR. One was wrong: unit 34's 'strap', which is not in Brasseur. One attribution
was misleading: unit 14's hom. I re-ran the MS form → mt comparison against 001–008 by script. It gives the same three
deliberate differences as pass 1 (chacab, qui ꜩih, cuc). I also compared roots by script. This found 001's `camuhibal`
qamujib'al 'our place of shade' (muh 'shade'), which bears on xcacamuh 'veil'. I added it as an inference and kept the
mt, since the morph division is unclear. The same check found that 006's `vcotobahic`, which pass 1's note tied to
cotobax 'be punished', is 'its digging' there.

Gloss: I checked all 105 entries and every `__broaden__` value against the units and the final mt, by script and by
reading. Keys equal novel-forms.json exactly. Every head equals the units' mt for its form (compared lowercased). Every
broadening begins with the current glossary entry verbatim + " · ". I compared each known form's use in 009 with its
glossary entry. Four broadenings were missing: `chacab`, which pass 1 asked for and the glosser did not supply,
`vlaquel`, `chirih` and `chuvi`. `patan` lacked its 'load' sense. None was unneeded.

Afterwards the JSON parses, and len(mt) == len(WORD_RE.findall(t)) for all 43 units. The units' `t`, joined, give back
the packet's 15 paragraphs exactly. Gloss keys == novel-forms keys (+ `__broaden__`), and every head and broadening
prefix checks. Final gloss: 105 novel forms, 16 broadened.

Counts: **major 0 · minor 14 · style 14** (28 findings: units 11 (minor 4, style 7); gloss 17 (minor 10, style 7)).
Gloss: 13 values fixed (11 entries, 2 broadenings), 4 broadenings added, 0 dropped.

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 34 | n | minor | "Brasseur takes … Patan as a carrying basket and its strap". He has 'hotte qui sert à porter des fardeaux', with no strap. He goes on to say that office, charge and tribute are often the same word, so the link to the duty is his own, not ours. | The note now gives his words: a basket for carrying loads, from which come 'office, charge and tribute'. |
| 14 | n | minor | "hom is the ball court (Brasseur's note), a walled alley … hips, not the hands": this attributes to Brasseur what his note does not say. His note gives Nahuatl tlachco and calls the place a temple. | The note says what Brasseur says, and the cultural fact stands unattributed. |
| 38 | n | minor | "cotobax may be the cotobah of 006 (vcotobahic)". In 006 vcotobahic is 'its digging' (coto 'dig'), so the note implied a sense link that 006 does not support. | "cotobax has the letters of 006's vcotobahic, read there as 'its digging'; whether they are one verb is not known." |
| 13 | n | minor | "(hun + taꜫ + ꜫih)": taꜫ spells taq' with the tresillo, but the word is taq 'each' (glossary: jun + taq + q'ij). This is the same slip pass 1 fixed in unit 20. | "(hun 'one' + tac 'each' + ꜫih 'day')". |
| 1 | n | style | "camuh, a verb not otherwise known": 001's camuhibal 'our place of shade' (ca- + muh 'shade') shares the letters, which fits Brasseur's 'veil'. | Added as inferred. mt stays xqakamuj, since the division is unclear. |
| 15 | l | style | l "He-came-here" against the note's "chul 'he comes here'" and i "would come". | "He-comes-here". |
| 17 | n | style | xe yaluh rested on Brasseur's French alone. His note on Xbaquiyalo gives yaloh 'séparer, retenir, demeurer'. | Added. |
| 20 | n | style | "que 'them' + ca- 'we'": que is c- (ongoing) + e 'them', as the note says of que two units earlier. | Relabelled. |
| 23 | l | style | l "giving(?)", where the note says the agent form 'giver' is "here taken as 'given'" and i has "given them". | "given(?)". |
| 26 | n | style | Brasseur has `chi pe puh rakan`, without chirih. This was not mentioned, though the note cites his letters for the next words. | Added. |
| 42 | n | style | ca chuvi chic 'later' was called inferred, without its basis. Brasseur has 'ensuite de cela'. | Added. |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| ꜩiyah | value | minor | "the phrase it ends": ꜩiyah begins `ꜩiyah bac xu pan …`. | "in tziyaj b'aq 'bare bone (?)', read after Brasseur's 'only a skeleton' (guess)". |
| hom | value | minor | "struck with the hips … (Brasseur's note)": the same false attribution as unit 14. | "the walled alley of the ball game (Brasseur: the hall of the ball game, Nahuatl tlachco)". |
| culvachih | value | minor | No hedge, though note 32 marks the pair inferred, after Brasseur. | "(inferred) … after Brasseur". |
| hupul | value | minor | "face down" stated plainly, though note 32 says that Brasseur here reads 'mouth upward' and that the English keeps 007/008's reading (inferred; QUESTIONS 007 5, 008 1). | "(inferred) … (Brasseur here reads hupul-oc 'mouth upward', the opposite)". |
| cotobax | value | minor | "perhaps the verb of ukotob'ahik": that word is 'its digging'. | "the letters of ukotob'ajik 'its digging', but whether one verb is not known". |
| __broaden__ patan | value | minor | "a carrying basket and its strap": Brasseur has no strap. The sense 'load' (huhun chi patan 'each a load', note 36) was missing. | Brasseur's 'hotte … whence office, charge, tribute', plus "patan — (inferred) load, burden carried". |
| __broaden__ chacab | new | minor | The glossary has only chaq'ab' 'at night'. In unit 2 the units give chakab' 'a part' (Brasseur xa chakab 'seulement une partie'). Pass 1 asked for this broadening, and the glosser did not supply it. | Added "chakab' — (inferred) a part, a portion …". |
| __broaden__ vlaquel | new | minor | The glossary has "(uncertain) 'set itself, level itself'" (001). Here the units read 'alone, unmarried' (Brasseur 'célibataire'). | Added "ulaqel — (inferred) alone, unmarried …". |
| __broaden__ chirih | new | minor | The glossary has 'behind it'. Unit 26 reads chirih vvach 'on his face'. | Added "chirij — (inferred) on, over (the surface of) …". |
| __broaden__ chuvi | new | minor | The glossary has 'on top of'. Unit 42 reads ca chuvi chic 'later on', in time. | Added "chuwi' — (inferred) after, later (of time) …; after Brasseur ('ensuite de cela')". |
| xcacamuh | value | style | It lacked the possible muh 'shade' link (unit 1). | Added "(inferred)". |
| yaqueic | value | style | "their bearing": 'their' is qui, which is not in the form. | "bearing, ways". |
| culelaah | value | style | "they face each other": 'they' is qui, and 'each other' is quib. | "face (each other), with kib' 'one another'". |
| cuchmaihic | value | style | "they gathered": 'they' is que, which is not in the form. | "gathering, coming together". |
| telelaon | value | style | "they carry": 'they' is qui. | "carry on the shoulder, bear as a load". |
| yaluh | value | style | "stayed long" was given without Brasseur's yaloh. | "stay long, remain" + his yaloh. |
| __broaden__ que | value | style | "ke 'them' + qa- 'we'": it misdescribes que, which is k- + e. | "ke — k- 'ongoing' + e 'them', the object before a transitive verb …". |

### Refused / left

- **The glosser's other broadenings are kept.** They are qui (qi tzij), cab ('the two of them'), pa (after naqi), chire
  ('because'), chul (narrative), cul ('throat'), cuc ('gather'), zac ('white dice'), nim ('respect') and hunhunahpu (the
  father). Each is a sense the entry lacks and the units use. In `pa`, the existing reading is limited to 'after mi', so
  the naqi pa use is not covered by it.
- **No broadening for** `ca` in `ca cut` / `ca chuvi chic`. These are left unrendered, and the entry's "(unclear) a
  particle … left unrendered" covers them. `oc` 'already' (unit 42) falls under 'yet, still'. `holom` 'skull' falls under
  'head'. `chaah` as a noun 'the ball game' (unit 13) falls under 'play (perhaps at ball)'. `cahau` 'parents' (unit 5) is
  the English of i, not a sense of the word.
- **l "it-is-called" for chuꜭhaxic (units 26, 35)** against the house table's "it-is-said": kept. The pilot itself uses
  both (001:7, 001:24).
- **`chamiy` mt chamiy (letter for letter).** The staff word may be modern ch'amiy, but Brasseur too writes chamiy
  without his apostrophe. It is left as it is. See question 2 below.
- **Pass 1's decisions all stand.** These are chacab chakab', qui ꜩih qi tzij, cuc kuk, camouic k'amowik, vve uwe,
  Junb'atz', the restored ejectives, and the letter-for-letter forms. I re-checked each against the OCR and 001–008.
- **Unit 7 "as in 005"** sits after nabeal … vcabal. Only vcabal is in 005, and the sentence reads as referring to it.
  Left.
- **The about**: re-checked against the units. No change.

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. Pass 1's nine points stand.
2. **`chamiy` 'staff'** (Chamiabac, rahchami, cahchamiyal) is respelled without the ejective, following the letter and
   Brasseur. If the modern word ch'amiy decides, the four forms and the names change together. This is the same question
   as rixk'aq and aq'an (007 2, 008 4).
3. **`xcacamuh`**: x- + ca- + camuh, or x- + ca- + ca- + muh 'shade' (001's camuhibal qamujib'al)? Meanwhile mt is
   xqakamuj and the link is noted as inferred. If muh is the root, 001's q- and 009's k- for the same ca- should agree.
4. No new house rendering in this part.
