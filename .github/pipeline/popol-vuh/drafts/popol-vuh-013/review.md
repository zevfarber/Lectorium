# Review — popol-vuh-013

## Pass 1

Reviewer pass 1, 2026-11-26. I read conventions.md (all of it, with the house renderings table and "The modern-letters
toggle"), runbook.md (ACTION draft, Reviewer), ../run3/RUNBOOK.md §2 (Reviewer), packet.md (the 14 established
paragraphs and the establishment log), known-forms.json / novel-forms.json, wordre.py, popol-vuh-001…012.json (by script
for every mt, and by hand at 003, 005–012 where the notes cite them), popol-vuh-glossary.json, the 012 review (as the
model of this file) and the draft units.json (33 units). For meaning I used only Brasseur 1861 (OCR lines 23160–23445:
K'iche', French and his notes (1) Xtoh/Xganil/Xcacou, tziya and (2) chicop). I opened no modern translation and recalled
none. Every edit was made by script (json load/dump, ensure_ascii=False, indent=1, as drafted). No `t` and no `mt` was
changed, and no unit was added, removed or moved. Unit numbers are 0-based; ¶ numbers are the packet's paragraphs.

**Checks run afterwards.** The JSON parses; 33 units; every `t` and every `mt` is identical to the draft's;
len(mt) == len(WORD_RE.findall(t)) in all 33 units; the units' `t`, taken in order, rebuild each of the packet's 14
paragraphs exactly (joined with a space), with no unit crossing a paragraph and no couplet split (Ta hul val oc, ta hul
tacal oc; ha cama … ha hacha; xavi xere … xavi cu xere; in macol, in ꜭazbol; quetal, qui ꜩihel puch all stay in one
unit).

**mt against the published parts.** By script every MS word was set against its mt in 001–012 (lowercased form → mt).
Every known form takes an mt that 001–012 gave it in the same sense; the only differences are case (Lal, Chajal, Anim,
Xoponik, Xu, arek'ut) and `vvi` (below). The 50-odd new forms were checked letter by letter (ꜩ tz, ꜭ k', ꜭh ch', v u/w,
z s, h j, b b', c/qu k or q). Marks are supplied only on certain words (alk'wal as 009's ralk'walaj, k'aslik, uk'u'x,
q'alaj, chuxe', usik'ixik as 007's xsik'inik, jutaq'ij, and wi' 'head, top' as 010's pu vi ha and the published chuwi');
everything uncertain is respelled (ukatb'al, kakal, jokam, wachelaam, kalab'a, xkaxinik, kaw, b'ok, samiy, rekan, xekan,
Kila, tziya, chichu, nare, ibare, alib').

**The drafter's flagged points, ruled one by one:**
1. `vvi` → uwi' (unit 21): kept. 012's uwi (glossary: "part of the word for the right hand, vi qui cab") is another
   word; here vvi is 'its top', the vi 'head, top' that 010 already gave wi' and that every published chuvi gives as
   chuwi'.
2. `hutaquih` → jutaq'ij (unit 9): kept. The day word q'ij is certain, Brasseur writes hutagih (his g = ꜫ), and the note
   says the c and ꜫ run together.
3. `huvi`, `vcavi`, `roxvi` → juwi', ukawi', roxwi' (units 17, 29): kept. The analysis jun / ka / ox + wi' rests on the
   text's own count (one, second, third) and on Brasseur's hyphenation u ca-vi r'ox-vi; the root wi' is certain, so its
   glottal stop is supplied as in chuwi'. The notes say huvi is 'one head' and the reading of the plant is Brasseur's.
4. `chivi` → chiwi (unit 17): kept, by the letters; the note says chi + vi is inferred.
5. `Ta hul val oc` → jul, wal (unit 19): kept by the letters. hul = ul 'come' is a guess; the note says the letters are
   those of jul 'hollow' and that what val means is not known, and gives the doubtful reading and Brasseur's va uloc
   (his шос is the OCR of uloc, as in his `a qam шос` for a cam vloc).
6. `cat` 'net' → kat (units 13, 18, 22, 23, 25, 29): kept, but see QUESTIONS point 1. Ximénez writes plain c, Brasseur
   cat; the toggle supplies no ejective it is not sure of.
7. `cabix` kab'ix (¶8, unit 15) against qab'ix (¶13, unit 26): kept. Brasseur himself distinguishes them: c'abix (his c
   = k) in ¶8 and k'abix (his k = q) in ¶13; the grandmother's 'our field' fits her speech, and 010's cochoch is both
   kochoch and qochoch.
8. `cam` kam 'die' (unit 11, Xe cam vi val) against k'am 'take' (units 18, 21, 26): kept, the published split.

**The drafter's two choices the brief asked me to decide:**
- *vchuch Hunbaꜩ, Hunchouen* 'the mother of …' (units 0, 1): kept. Earlier parts make Xmucane their grandmother
  (009: Xpiyacoc and Xmucane are the parents of Hunhunahpu; 009 also: the boys' own mother is dead; 010: ivatit 'your
  grandmother', qui chuch Xmucane of Hunhunahpu's mother). The manuscript nonetheless says vchuch, and Brasseur keeps
  'la mère' with the note 'La mère apparemment pour l'aïeule' (OCR verified). The house practice for the text's own
  slips (Hunhunahpu-as-written in 005, Hunahpu-as-written in 012) is: print it, let the English follow it, say so in the
  note. The unit 0 note says so plainly and the about says "the grandmother … (the text calls her their mother)".
- *alib* as 'daughter-in-law' (¶2, ¶6, ¶7, ¶14) and 'mother-in-law' (¶4 Lal valib, unit 8): kept. The evidence is in the
  text: Xquic says in alib la 'I am your alib' (¶2, ¶4), then Lal valib 'you are my alib' (¶4), with v- 'my' and lal the
  respectful 'you', both in her own speech; the old woman then says at valib 'you are my alib' (¶6, ¶7, ¶14). The word
  is used from both sides, and Brasseur renders it 'votre belle-fille' and then 'Vous êtes ma belle-mère' (both in the
  OCR). The `l` of ¶4 is 'my-in-law', the `i` 'my mother-in-law', and the note marks the two-sided sense inferred.

**`chi` → chik in Ꜭo chi pa ri val** (unit 4): kept. 007 printed ꜭo chi vi as chi, but 011 (ꜭo chi vi ri vholom) and
012 (ꜭo chi ral) give chik, and the glossary's chik 'any more (ꜭo chi vi …); chic with its c not written' covers it.

**Brasseur attributions.** Every one was checked against the OCR (23160–23445) and all hold: 'était chez elle', 'La mère
apparemment pour l'aïeule', the omission of vbi. Ta xul cut ri ixoc Xquic, x-qol-oc, 'peu s'en fallait …', 'ó ma dame et
mère', 'votre belle-fille', 'la fille adoptive de votre seigneurie', 'où sont mes fils?', 'leurs deux descendants, les
signes de leur parole', 'ne les vois-tu donc pas ?', 'Sors d'ici, va-t'en!', the garbled ve ауа, Xerela, x-qo nare,
'Croyez-moi véritablement …', '(l'épouse)', 'les voici portés vivants', u gatbal, 'la sentence … plus illustres', 'Vous
êtes ma belle-mère', yv'ila, chi log, 'leur image chérie', cakal, 'se mirent en colère', tzibanic, qotonic, 'ils
employaient tout le jour', hutagih, 'la consolation de la vieille', ca v'ah, 'c'est ton adultère', the unreadable Заро /
ирнен, x-e Cam vi v'al, 'Ce n'est que trop vrai …', uh'at bala, 'Va donc', 'pour ceux qui mangent', 'moissonne',
'filet', c'abix, 'le chemin avait été ouvert et nettoyé par eux', takeh, chiri, u ca-vi r'ox-vi, havi, 'une seule gerbe
sortant encore son image', 'se brisa', 'Malheureuse pécheresse', qazbol, qam, 'le Gardien des aliments', 'afin d'obtenir
qu'il en rapportât', the note on Xtoh / Xganil / Xcacou (toh the ninth day sign, 'pluie, averse'; gan 'jaune',
maturity, harvests; cacou 'cacao'), Xganil in his K'iche' and Xcanil in his French, the tziya note ('cuire le maïs avec
de la cendre ou de la potasse'), qu'echa twice, tzamiy / u tzamiyal, 'les barbes et l'extrémité de la gerbe', 'les
arracha doucement', 'sans déraciner la gerbe', 'les arrangea …', 'remplir un grand filet', x-ekan, the chicop note
('Ximenez traduit par animal; nous avons cru que le mot barbare convenait davantage'), u coc, r'ekan, 'comme leur
fardeau (ordinaire)', aumal, galaba, 'aurais-tu donc ruiné (mon champ)', k'abix, 'Je vais y voir à l'instant', r'ila,
u qolibal, 'l'endroit où avait été placé le filet', 'C'est là véritablement un signe', vienauinakchie, 'celles des
sages que tu portes'. One paraphrase ('three goddesses') is now quoted (unit 20).

**Establishment log.** Every doubtful reading, letter decision and division is in its unit's note (the omitted clause in
Brasseur, xꜭol oc, ve a vila, Cat pe vi with the raised mark, xꜭo nare, ivila, loc, the overwritten l of cacal, ca uah
with u, ꜭo cha pam, ꜭaxtoꜭ, the blot on vi of Xe cam vi, the tag xꜭha chicut ri atit at a line start, the division of
¶7 and veeh, quecha / queꜭha, xcha cut, zibanic and zamiy with plain z, huvi with its raised mark and MS u, the blot on
Chahal, Ta hul val oc, chi cau with u, the struck letter before cat, xucut ha, auumal, xe a calaba, rila, chi rochoch,
ri e ꜭo ri vi, the plain c of vcatbal, cotonic, cat, Xcanil, xecan, recan, vcoc, vcolibal, cabix, Catepuch, and the
part's end at Ximénez's heading). Two were missing and are added: the blot over vi in ꜭo vi cabix (unit 15) and the
split spellings hunhun ahpu / hun hunahpu (unit 6).

Counts: **major 0 · minor 4 · style 10** (14 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 5 | n | minor | ve a vila was analysed as "a- 'you' + vila, with v before the vowel, + il 'see' + -a": it names vila (which in ¶13 and elsewhere is v- 'I' + il + -a) and then breaks it again, so the reader cannot tell whose v it is. | "a v-, the 'your, you' a- with v before a vowel (written apart here), + il 'see' + -a". |
| 11 | n | minor | "xma 'there was not'" as the label of xma in Xma ca uah vi at ta valib, where it negates 'I want': there is no existential here. | "xma, the negative (elsewhere 'there was not', as xma ꜭo in ¶9)". |
| 15 | n | minor | The log's blot over vi in ꜭo vi (0044 l.21) was not mentioned; the log says the notes must. | Added "(a blot lies over vi; read with Brasseur's qo vi)". |
| 6 | n | minor | The log's split spellings of the name (MS hunhun ahpu, then hun hunahpu) were not mentioned. | Added: the manuscript writes the name apart in both places; printed Hunhunahpu as everywhere. |
| 11 | n | style | ca uah "c- (ongoing) + v- 'I'" leaves the a of ca unaccounted for. | "ca, the ongoing c- with its vowel, + v- 'I' …" (012's wording). |
| 12 | n | style | ca nu biyh, ca nu tao "c- + nu-": same gap. | "ca (the ongoing c- with its vowel) + nu- 'I'"; "ca + nu- 'I'". |
| 4 | n | style | cat 'you (one)', "c- + at" without saying what c- is. | "c- (ongoing) + at 'you'". |
| 5 | i | style | "Go back where you came from!" for cat pe vi 'you come from there' is Brasseur's sense ('Sors d'ici'), inferred in the note, unmarked in i. | "Go back where you came from (?); out, away with you!" |
| 8 | i | style | "the dear (?) face of what I carry": vcaam has v- 'its/her', not nu- 'my'; 'I' is Brasseur's ('ceux que je porte'). Unit 7 already says "what is carried". | "the dear (?) face of what is carried". |
| 13 | i | style | "fetch food for those who eat (?)" dropped the possessor of quecha 'their food' (l has their-food). | "fetch their food, for those who eat (?)". |
| 17 | i | style | "it bore its fruit" for vachelaam, which the note calls a guess. | "it bore its fruit (?)". |
| 32 | i | style | "what you will do, you and those who are there": 'you and' and the future are not in Chi vil chi na a banoh, ri e ꜭo … | "what you do, and those who are there (?), who are wise already (?)". |
| 20 | n | style | "three goddesses of food and plenty" given as Brasseur's words in our English. | Quoted: 'trois divinités qui présidaient à la nourriture, à l'abondance', each a goddess. |
| about | — | style | "The grandmother hurries to the field": the K'iche' has xbe 'she went'; anim 'quickly' is on her way home (¶14). | "goes to the field … hurries home, and takes it as the sign". |

### Refused / left

- **Flagged points 1–8 and the two decisions above**: kept, for the reasons given.
- **cat 'net' as k'at**: not restored. The modern net word is probably k'at, but the letters are plain c, Brasseur prints
  cat (his c = k), and conventions restore only where certain. Sent to QUESTIONS.
- **echa 'food'** without a final glottal stop, **xecan / recan** with k (Brasseur k = q), **Vhat** Ujat, **hocam**,
  **cacal**, **cau**: respelled by the letters, nothing restored; the meanings are inferred or guessed and the notes say
  so. xecan / recan follow 012's rule for ahchoce (q only where tied to a certain q word).
- **quecha kecha / queꜭha kech'a**: two mts for one word, each by its letters, as 012's ajuchan / ajuch'an. Kept.
- **alcual 'al + ꜭahol made one word'** stated without "inferred": kept; it is 009's published analysis (ralcualah) and
  the modern alk'wal is certain.
- **Unit 0 i "Now they were there, the mother of …"**: the plural e with a singular noun is awkward English but mirrors
  the K'iche', and the note explains it (inferred: the household). Kept.
- **Unit 7 i "make their own sentence (?) shine (?)"**: odd, but both doubtful words are marked and the note says the
  English is a guess along Brasseur's lines. Kept.
- **ꜭaxtoꜭ 'deceiver'** (unit 11): kept; 005 glossed it 'demon, deceiver' and the note marks this sense inferred.
- **Unit 23 'animals'** for chicop where Brasseur prefers 'barbares': kept, following Ximénez's 'animal' (reported by
  Brasseur's own note) and every published chicop.
- **Hunchouen with u** though the MS letter is v-shaped here: kept, as 009–012; the note says so.

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. **cat 'net'**: mt kat by the letters (the same letters as kat 'you'); if the owner accepts k'at 'net' as certain, six
   tokens in units 13, 18, 22, 23, 25, 29 change to k'at.
2. **vchuch Hunbaꜩ, Hunchouen**: rendered 'the mother of' as written, the third text-slip of this kind (005, 012); the
   table row for "as written" could be widened to cover kin terms too.
3. **For the glosser**: known forms used in a new sense here need broadening: `hal` (jal 'ear of maize', inferred; the
   published entry is 'change'), `hul` (jul, guess 'come', in ta hul), `cat` (kat 'carrying net'), `vvi` (uwi' 'its
   top'), `loc` (lok 'dear (?)', after Brasseur's 'chérie'), `xquiz` (xk'is of the heart, 'failed'), `val` (wal, meaning
   unknown in ta hul val oc), `i` (iw- 'you (pl.)' as ergative in i vila; the published entry is the possessive only),
   `xpetic` ('she came'), `ya` ('put, set' in qui ya).

## Pass 2

Reviewer pass 2 (adversarial), 2026-11-26. I read conventions.md (with the house table and "The modern-letters toggle"),
runbook.md, ../run3/RUNBOOK.md §2, packet.md with the establishment log, known-forms.json / novel-forms.json, wordre.py,
popol-vuh-glossary.json, popol-vuh-001…012.json (by script for every form a note cites as "as in an earlier part"), the
012 review's Pass 2, and pass 1 above with units.json and gloss.json as it left them. For meaning I used only Brasseur
1861 (OCR 23160–23445, K'iche', French and notes) and the published files; I opened no modern translation and recalled
none. Every edit was made by script (json load/dump, ensure_ascii=False, indent=1). No `t` or `mt` was changed, no unit
added, removed or moved; none of pass 1's rulings was undone.

**Fresh pass on units.json.** All 33 units again: grammar labels against the forms, K'iche' → `l` word by word, `l` ↔
`i`, remembered English, couplets (Ta hul … ta hul; ha cama … ha hacha; in macol, in ꜭazbol; xavi xere … xavi cu xere;
quetal, qui ꜩihel puch; xa zu, xa bix … xa zibanic, xa pu cotonic — all kept as pairs in `i`), house renderings (Vꜩ
bala 'Very well', lal the respectful 'you', capoh 'maiden', names kept). Every "as in an earlier part" was checked in the
published JSON: 012 vhoxbal / nu hoxbal, co cha pam, xbec, ca bixic, ca nu tao, vila, xqui chaquih 'they dried it';
010 xqui taqueh ri be, ivatit, cochoch qochoch; 009 ahzu ajsu, ahbix, ahꜩibenai, ahcot ajkot, ralcualah, xcaminac oc,
yaqueic; 007 xziquinic xsik'inik; 006 vcoc, vcolbal, ha cama; 005–007 ꜭaxtoꜭ; 004 cube; 003 xa loc. All hold. Every
Brasseur attribution was rechecked against the OCR and holds (the French quotations are his words). Two small fixes.

**gloss.json.** By script: 55 novel forms, 55 entries, no extras; every entry's modern form equals the unit's mt for that
token (cabix carries both kab'ix and qab'ix, as its two mts); every `__broaden__` starts with the published entry
exactly, then " · ". Each value was read against the final notes: 8 entries corrected, 7 broadenings added; the 7 the
glosser wrote (hal, hul, cat, vvi, loc, i, xe) are correct and kept.

Afterwards: both files parse; 33 units; len(mt) == WORD_RE count in every unit; the units' `t`, joined with a space,
rebuild the packet's 14 paragraphs exactly; novel-forms keys == gloss keys; every modern form == mt; every broadening
begins with its published entry.

Counts (pass 2): **major 0 · minor 10 · style 5** (15 rows).

### Changes

| unit / entry | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 7 | i | style | "What is carried here is alive" made e ꜭazlic singular; e is the plural ('they are living'; l "they alive"; Brasseur 'les voici portés vivants'). | "Here they are, carried, and alive: Hunhunahpu and Vucub Hunahpu are not dead; …". |
| 0 | n | style | "in 010 the brothers left them to keep 'your grandmother' warm": "the brothers" could be read as Hunbatz and Hunchouen themselves. | "in 010 Hunhunahpu and Vucub Hunahpu, leaving for Xibalba, told the two to keep 'your grandmother' warm". |
| gloss `ꜩiya` | value | minor | Gave Brasseur's note as 'préparer le maïs avec la cendre', which is not his wording. | His note's words 'cuire le maïs avec de la cendre ou de la potasse' and his rendering 'vous qui préparez le maïs avec la cendre'. |
| gloss `alib` | value | minor | Only 'daughter-in-law', though the entry itself says the word is used from both sides and ¶4 Lal valib is 'my mother-in-law' (unit 8). | "daughter-in-law; also mother-in-law: …, said from either side (inferred)". |
| gloss `valib` | value | minor | Only 'my daughter-in-law'; Lal valib (unit 8) is Xquic's 'my mother-in-law'. | Adds "also my mother-in-law, said by the son's wife (inferred)". |
| gloss `chivi` | value | minor | Analysed as chi + wi' 'head', the word of huvi/vcavi; the note's chi + vi is the ꜭo chi vi 'is there any more' pattern, vi the particle of place. "at all" is in no note. | "chi 'any more' (chik with its c not written) + wi, the particle that points back to a place … as in k'o chi wi". |
| gloss `xtoh` | value | minor | "'rain', a goddess of food" compressed Brasseur's note; he makes Xtoh the goddess of rain and of the earth's fruitfulness, one of three of food and plenty. | Rewritten with his words ('les auteurs traduisent par le mot pluie, averse'), the ninth day sign, inferred. |
| broaden `yaqueic` | added | minor | Pass 1 asked; missing. The published entry is 'bearing, ways'; here (unit 2) it is taken as 'come forth, be born'. | Added as a guess, with Brasseur's 'peu s'en fallait pour la naissance'. |
| broaden `chaquih` | added | minor | Published entry 'dry' / 'dry (something)'; here (unit 9) qui chaquih is taken as 'they spent (the day)'. | Added as a guess, with Brasseur's 'ils employaient tout le jour'. |
| broaden `ya` | added | minor | Pass 1 asked; missing. The published entry is 'give' (and 'river'); qui ya (unit 24) and 012's chi ya chuvi ꜫaꜫ are 'put, set'. | Added "put, set; the 'give' verb used of placing a thing". |
| broaden `val` | added | minor | Pass 1 asked; missing. The published entry 'my child' does not cover ta hul val oc (unit 19), where the note says the meaning is unknown. | Added "(unclear) in ta hul val oc, a doubtful reading; what it means there is not known". |
| broaden `vila` | added | minor | ve a vila (unit 5) is a- 'you' + w- (rest of aw-) + il + -a, and i vila (unit 8) is not a command; the published entry has only the command after chi and 'I see it'. | Added both uses, inferred. |
| broaden `pa` | added | style | The published question-particle sense is pinned "after mi"; here it follows ma (Ma pa xe camic) and ꜭo chi (Ꜭo chi pa ri val), as in 008/012's ma pa. | Added "question particle after other words too: ma pa …, ꜭo chi pa …". |
| broaden `xpetic` | added | style | Pass 1 asked. The published entry reads "(you) came"; unit 24 Ta xpetic is 'she came'. | Added "he came, she came; the same form of a third person". |
| gloss `ꜭazbol`, `recan`, `rila` | value | style | ꜭazbol mixed spellings ("k'az 'debt'"); recan was not marked inferred though its sense rests on the inferred ecan of xecan; rila was pinned to 'she'. | ꜭazbol: "ꜭaz 'debt' + -bol; not the ꜭaz 'live' of ꜭazlic"; recan: "(inferred) her load, his load, its burden; r- 'her, his, its'"; rila: "he sees it, she sees it". |

### Refused / left

- **Broaden `xquiz`** (pass 1 point 3): not added. The published "it finished, they finished; k'is 'end, be finished'"
  covers both uses here (xquiz cut vꜭux 'her heart came to an end', xquiz a cam 'have you finished taking'); 'failed' is
  the English of the line, not a new sense.
- **Unit 8 i "So you shall see"**: kept. Quehe cut i vila ta has no future mark, but neither does it have a command form;
  Brasseur's 'voyez' is one reading, the English one other, and the l shows the bare form.
- **Unit 26 i "Have you laid it waste (?)"** for xe 'them': kept; English "it" for the field's plants, l keeps 'them'.
- **Unit 32 i "I shall see yet"** for chi vil (optative): kept; Brasseur 'je verrai', and the l shows "That I-see".
- **gloss `xecan` "the toggle keeps k"**: kept; it explains the mt, as 012's entries do.
- **gloss `boc` "(guess)"** where the note says inferred: kept; the gloss is less confident than the note, never more.
- **Published entries `vcaam` ("carried by him"), `xbec` ("he went"), `petic` ("coming", verbal noun)**: cover these uses
  closely enough; not broadened.

### For QUESTIONS.md (pass 2; nothing blocked)

1. Pass 1's three points stand (cat 'net' as k'at; vchuch 'mother' for the grandmother; the glosser broadenings, now done).
2. **alib** is now glossed both ways ('daughter-in-law', 'mother-in-law'); if the owner wants a house rendering, the
   proposal is alib 'daughter-in-law' / valib 'my mother-in-law' only where Xquic says it of the grandmother (¶4).
3. No new house renderings proposed beyond pass 1's; Chahal Echa 'the Guardian of Food' and Xtoh, Xcanil, Xcacau kept as
   names could go into the table if they recur.
