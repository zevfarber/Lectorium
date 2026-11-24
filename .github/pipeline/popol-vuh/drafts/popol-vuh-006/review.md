# Review — popol-vuh-006

## Pass 1

Reviewer pass 1, 2026-11-24. I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md (the text and the
establishment log), popol-vuh-001…005.json, popol-vuh-glossary.json, the 005 review, wordre.py, novel-forms.json,
known-forms.json and the draft units.json (58 units). For meaning I used only Brasseur 1861 (OCR lines 20090–20560:
K'iche', French and notes) and the glossary. No modern translation was opened or recalled. I made every edit by script
(json load/dump, ensure_ascii=False, indent=1). No `t` was changed, and no unit was added, removed or moved. gloss.json
was not touched.

I compared every mt with 001–005 by script (MS form → modern form). Five forms differ from a published spelling, and all
five are real homographs that the note explains: `chiquih` chikij 'behind them' (005 chiqij 'behind us'), `cachbilan`
kachb'ilan (005 qachb'ilan 'we accompany'), `quib` qib' 'ourselves' (001–002 kib'), `cuꜭ` quk' 'with us' (001 kuk'),
`cam` kam 'die' (002 k'am 'take'). I also compared roots across forms, which the script does not see, and that found
three real inconsistencies (xunao, the ok 'enter' family, and the qaj 'go down' verb against 003), below. I checked
every cross-reference in the notes against 001–005 and every Brasseur claim against the OCR; two were wrong (units 22
and 53). Every establishment-log item is mentioned in the note of its unit; the one missing (the ß-ligature in `atit`)
was added.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) holds for all 58 units, and the units' `t`, joined in
order, give back the packet's 22 paragraphs exactly, paragraph by paragraph.

Counts: **major 0 · minor 13 · style 12** (25 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 5, 6 | mt, n | minor | `ꜩucubei` → tzukub'ei, `iꜩucubal` → itzukub'al. c stands for /k/ or /q/, and here the choice was against every witness: Brasseur's note derives it from tzukuh 'sustain' (his k = q), and 001 prints ꜩucul 'provider' as tzuqul. | mt tzuqub'ei, itzuqub'al. The note gives the root tzuq, Brasseur's k and 001's tzuqul. No ejective restored. |
| 6 | mt, n | minor | `ivalcual` → iwalkual. The drafter restored ejectives in ik'ow, q'at, k'am and sik'in as certain words, but not here, though alk'wal 'children' is just as certain (Brasseur "Sont-ce vos enfants"). The note's analysis "al … with cual, the children of both parents" said that cual is 'children of both parents'. | mt iwalk'wal. The note now says: alcual 'children', built on al 'a woman's child'; the word is certain, so the toggle restores the ejective. |
| 8, 10, 15 | mt, n | minor | `tocobah` → tokob'aj. Brasseur prints tokobah (k = q) and, in unit 15, togobah (g = ꜫ); the word is the certain toq'ob' 'pity' (chi tocobah nu vach 'pity my face'). tokob'aj matched neither witness nor the modern word. | mt toq'ob'aj ×3. The note to unit 8 gives both of Brasseur's spellings and says that the ejective is restored. |
| 10, 13, 15 | n | minor | "chi before the verb gives a wish or a command" / "chi of command + cunah". These are addressed to the old pair (chivech 'to you (pl.)'), and chi is ch- + i- 'you (pl.)', as Brasseur writes it (ch'y tokobah, ch'y cunah, ch'y togobah). Unit 11 and unit 20 (chivelezah) already said so, so the notes contradicted each other. | Each note now gives ch- (command) + i- 'you (pl.)', with Brasseur's spelling. |
| 13 | n | minor | "varam 'my sleep' (v- 'my' + aram)". nu 'my' stands before it (nu varam), and the root is var 'sleep', the root of the house word vvarabal 'its place to sleep'. | "nu varam 'my sleep': nu 'my' + varam 'sleep', from var 'sleep' (the root of vvarabal …) + -am". |
| 16, 18, 22 | mt, n | minor | `choc` → choq, `xchoc` → xchoq, `xoquic` → xoqik. The verb is ok 'enter', with k: 001–005 give xoc → xok and catoc → katok, and this part gives vcoc → ukok (unit 31). -oq is the suffix (cahoc, acanoc), not this root. | mt chok, xchok, xokik. The note to unit 16 says ok, with k, as xoc → xok in the earlier parts. |
| 22 | n | minor | "vla 'hither', as in the last part". vla does not occur in 005. It is in 003 (xcupin vla, xoc vla). | "as in the third part". |
| 23 | n | minor | xcah → xqaj 'went down' (Brasseur x-kah, his k = q) is right. But 003 gave the same verb kaj (`xcahixic` → xkajixik 'were brought down', `vcahic` → ukajik), and the note did not say so. The script did not catch it because the MS forms differ. | The note says that 003 gave kaj, that the verb is qaj, and that it is qaj throughout this part. See QUESTIONS. |
| 26 | mt, n | minor | `xunao` → xuna'o. 004 gives the same verb, `xca nao` 'we felt', as nao, with no glottal stop (glossary `nao`). Same verb, same sense, two spellings. | mt xunao. The note cites 004's xca nao. That na'o is the modern form of both goes to QUESTIONS. |
| 29 | mt, n | minor | `ahꜭun` → ajkun. The image letter is ꜭ (established by the letter rule), and the toggle respells it k'. The draft respelled vꜫexel by the letter (uq'exel, though the modern word is k'exel), and 005 did the same with vꜭhapa → uch'apa (modern chap). Following the modern word here, and only here, was inconsistent. | mt ajk'un. The note gives the modern ajkun, Brasseur's c (OCR aheun), and the precedent of vꜫexel and vꜭhapa. See QUESTIONS: the owner may prefer the modern word in all three. |
| 46 | n | minor | "The boys fear a strength like Zipacna's, the strength the boys of the last part feared in his father." Hunahpu and Xbalanque never fear Vucub Caquix: they judge his pride evil (005 unit 2, this part's unit 32). The comparison was invented. | "The four hundred fear his strength." |
| 51 | n | minor | "xuchaxic 'he was told': x- + ꜭha 'say' + -x- (passive) + -ic". This left out the u- that is in the form (x-u-cha-x-ic). | "x- + u- + cha 'say' + -x- (passive) + -ic, the u- standing in this passive as in xe vꜭhax 'they were told' in the second part". |
| 53 | n | minor | (1) "ca is taken as the ongoing c-, the 'you' left unwritten". The a of ca may be the 'you', a- (Brasseur C'a ziquin), so it was not shown to be unwritten. (2) "The first sentence is not in Brasseur's French." The French has 'tandis qu'il creusait la terre' (the OCR is damaged), which is part of it. | (1) "c- (ongoing) + a, perhaps a- 'you (one)' (Brasseur C'a ziquin), though with the intransitive ziquin one would expect cat; inferred." (2) "Brasseur's French (damaged in the OCR here) gives of the first sentence only 'while he dug the earth'." |
| 1 | n | style | "so the qu is qui- 'their'". Before a vowel the 3pl possessive is k-, not qui-. | "the qu is k-, the form of qui- 'their' before a vowel". |
| 1 | n | style | The establishment log's ß-ligature in `atit` (all) was not mentioned in any note of this part. | Added: the ti of atit is the ß-ligature, read ti here and throughout. |
| 15 | i | style | "are all loose now". 'all' renders nothing (005 review made the same correction for xa ca chuiu). | "are loose now". |
| 21 | n | style | "xel … with no ending at the clause's end". xel is not at the end of its clause; that is why it has no -ic. | "with no -ic, because more follows in the clause (as xe icou above)". |
| 22 | n | style | zac huluhuh did not mention the same word in the macaw's boast, 004 `nu ꜩam zachuluhuh` (004 l 'gleams', i 'gleams white'). | Added the cross-reference. |
| 24 | n | style | caual: the note did not say that Brasseur prints qual (as he does for 005's vcual), or why the toggle is not kuwal as in 004/005. | Added: there a letter was missing from cuval, and here a letter is different, so the letters are respelled as written. |
| 29 | n | style | xcamouic → k'am, but 005's `xcamou chi la` (the same verb without -ic) was left kamow, and the note did not say so. | Added one sentence. |
| 30 | n | style | "xbanouic …: ban 'do' with -ou- + -ic" left out x-. | "x- + ban 'do' + -ou- + -ic". |
| 48 | n | style | "i sets them in single quotation marks": the reader does not know what `i` is. Ha 'go!' was not set apart from ha 'water' (unit 36). | "the English sets them …"; added "not ha 'water'". |
| 48 | i | style | "‘Go down and take out the earth …’". 'down' came from caha, which the note calls a guess (Brasseur 'tirer'), so 'take out' and 'go down' both had a source. | "‘Go and take out the earth in the pit,’". |
| 56 | n | style | "pala … in the earlier parts". It occurs only in 003 (haruh pala). | "in the third part (haruh pala)". |
| about | — | style | "asks who they are" (he asks where they come from), and "poor old people" ('poor' is not in the text). | "asks where they come from; they say they are old people seeking their living". |

### Refused / left

- **`caual` → kawal (units 24, 29), not 005's kuwal. Kept.** Brasseur prints qual in both places, which supports the drafter's identification with cuval/vcual. But in 005 a letter was *missing* (vcual = cuval without v), and the toggle supplied the known spelling. Here a letter is *different* (a for u). Turning a into u would be emending, not restoring, and the identification is inferred. The note now says all this. **For the owner:** if caual is to be treated as a miswriting of cuval, change mt to kuwal in units 24 and 29 together.
- **Ejectives restored by the drafter: all kept.** `icouic`/`icou` → ik'ow (Brasseur iqou, his q = ꜭ; 'passèrent'). `xquicat` → xkiq'at (Brasseur x-qui gat, g = ꜫ; 'coupé'). `xcamouic` → xk'amowik (Brasseur x-qamouic; 'prit'). `xcam qui naoh` → xk'am (Brasseur x-qam; 'tinrent conseil'). `ziquin`/`ziquih` → sik'in/sik'ij, as 002's ziquinoc/iziquih. Each of these words is certain in its context, and Brasseur agrees. For `xcam qui naoh`, the missing ergative prefix is odd, and the note says so ("no prefix on the verb"), as with xil in unit 3. *For QUESTIONS:* 004's `icouen` → ikowen ('surpass', uncertain) may be the same verb, and may want ik'owen.
- **`coto` family → koto (units 47, 51, 53–55, 57). Kept.** Brasseur reads q (ꜭ) throughout, and the modern verb is k'ot 'dig, gouge'. But 003 printed the same root letter for letter (cotah → kotaj, cotox → kotox, xcotin → xkotin 'gouge'), and the image has plain c. Restoring it here alone would split the root across parts. *For QUESTIONS:* k'ot in 003 and 006 together.
- **`xuchaxic` → xuch'axik, against plain `cha`, `xcha`. Kept.** This follows 005's chuchaxic → chuch'axik (the passive of the house word with plain ch), and the published glossary's cha/xecha → cha/xecha, letter for letter. vchaxic → uchaxik (001, 002) is the one counterexample. The precedent is split, and the drafter followed the nearest one.
- **`vꜫexel` → uq'exel. Kept**, by the letter (Brasseur also has g = ꜫ), and now consistent with ajk'un.
- **xcah read two ways (unit 23 xqaj 'went down', unit 32 xkaj 'they wanted'). Checked and right.** Brasseur has x-kah (k = q) for the first and x-c'ah for the second, and his French has 'tomba' and 'voulurent'.
- **Agent focus -ou- (xcamouic, xbanouic). Checked and right.** The doer stands before the verb in both (ri xa ahꜭun …, Naual atit, naual mama …).
- **`raxcanacoh` (n), against Brasseur raxcauacoh and 004's MS raxcavacoh. Not changed (`t` pinned).** *For the establisher:* recheck n against u/v on i0025. The note respells the letters and calls the word the same as 004's.
- **Unit 9 `vcoxom ve`.** Left. ve is written with v-, where 'his' before a vowel is r- (re, unit 2). Brasseur divides u e 'his teeth'. l gives "teeth" with no possessor, and the note does not analyse the prefix. Nothing more can be said with certainty.
- **Unit 6 l "Not(?)" for the question word Ma.** Left. 004 (unit 7) glosses the question Ma as "Not" in l, and the note explains it.
- **Unit 51 i "we cannot get to the bottom of it".** Left. It is interpretive (l 'not we-find(?)'; Brasseur 'nous n'en pouvons plus'), but the note marks the clause as inferred.
- **Unit 14 `quivbah` → kiub'aj against 005's quivubah → kiwub'aj.** Left. These are different MS spellings, each respelled letter for letter, as the 005 reviews decided.
- **`chaquimah` → chakimaj.** Left, letter for letter. The word is unknown, and Brasseur's k (= q) alone does not settle it.
- **QUESTIONS points:** (1) caual kawal vs kuwal (above). (2) The modern word against the image letter: ajk'un (ajkun), uq'exel (uk'exel), and 005's uch'apa (chap) should be decided together. (3) 003's xcahixic/vcahic were given kaj 'go down'; the verb is qaj (006). (4) 004's xca nao and 006's xunao are both letter for letter; na'o is the modern verb. (5) The k'ot 'dig, gouge' family in 003 and 006 (koto, kotaj, kotox, xkotin). (6) 004's mt for `zachuluhuh` (sachulujuj) reads the c + h of zac|huluhuh as the digraph ch; 006 divides the word and gives saq julujuj. 004's toggle should probably be saqjulujuj. (7) 004's icouen → ikowen may be ik'ow (above).
- **Glosser (pass 2).** Keys must match the final mt: ꜩucubei tzuqub'ei, iꜩucubal itzuqub'al, ivalcual iwalk'wal, tocobah toq'ob'aj, choc chok, xchoc xchok, xoquic xokik, xunao xunao, ahꜭun ajk'un. Known forms in a new sense that may need `__broaden__`: `re` ('his teeth', r- + e), `ve` ('yes'; 'my teeth'), `quib` ('ourselves', qib'), `cuꜭ` ('with us', quk'), `chiquih` ('behind them', chikij), `cachbilan` (kachb'ilan, ongoing), `cam` ('die', kam), `xquicot` ('they dug'), `ha` ('go!'), `cu` (ku, c- + u-), `chi` ('mouth', chi').

## Pass 2

Reviewer pass 2, 2026-11-24 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
packet.md (text and establishment log), units.json as left by pass 1, gloss.json (made by the glosser from the pre-pass-1
draft), pass 1's review, novel-forms.json, known-forms.json, popol-vuh-001…005.json, popol-vuh-glossary.json, the 005
review and wordre.py. For meaning I used only Brasseur 1861 (OCR lines 20090–20560, K'iche', French and notes) and the
glossary; no modern translation was opened or recalled. Every edit was made by script (json load/dump, ensure_ascii=False,
indent=1); no `t` was changed and no unit was added, removed or moved.

Units: I went through all 58 again (grammar labels against forms, K'iche' → l word by word, l ↔ i, couplets, the house
table, uncertainty labels, every establishment-log item, the about). I re-ran the MS-form → mt comparison against 001–005
by script: the only differences are pass 1's five explained homographs (chiquih, cachbilan, quib, cuꜭ, cam). Comparing
roots by hand found one more split: `xutiquiba` (unit 55) had xutikib'a, against tikib'a' in 001 (xchicatiquiba) and 003
(tiquiba) and the glossary. I checked the notes' cross-references against 001–005 (zachuluhuh, quizoc, chi ca coh, recha,
xi quivubah, chuiu/ahe, e cabauil, Vꜭux Cah in 005, In banol vleu, calibal, acanic, nah, quiꜭohe, mucunic, vvbaxic,
xcolo, pala, Vꜩ bala) and the Brasseur claims against the OCR; all held except the one location below (unit 58).

Gloss: I checked all 135 entries and all 17 `__broaden__` values against the text and the final mt, by script and by reading.
Every novel form has an entry and no key is extra. Nine heads were stale against pass 1's mt (the list pass 1 gave) and
one against this pass's change; all now equal the mt of their tokens. Several morphologies were wrong (missing u- in the
three passives of 'say', w- 'my' in varam, a root kok, ka- in xchi). Every `__broaden__` value begins with the glossary
entry verbatim; four broadenings were added for known forms used here in senses the glossary does not cover.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 58 units, the units' `t`, joined in order, give
back the packet's 22 paragraphs exactly, every novel form is keyed in gloss.json, and every gloss head equals the units'
mt for that form.

Counts: **major 0 · minor 24 · style 11** (35 findings; units 5, gloss 30).

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 55 | mt | minor | `xutiquiba` → xutikib'a, but the same verb is tikib'a' in 001 (xchiqatikib'a'), 003 (tiquiba) and the glossary. | mt xutikib'a'; the note says the toggle shows the glottal stop as in the first and third parts. |
| 9 | i | style | "a half of what we have": 'of what we have' renders nothing (Brasseur's parenthesis 'de notre nourriture'). | "and a share, a half, we give to them". |
| 21 | n | style | chi in chi too vloc was not analysed, though every other command in the speech is (Brasseur ch'y too). | Added: chi is ch- + i- 'you (pl.)', as before the other commands. |
| 33 | n | style | xcah 'they wanted': "c- (qui- 'their' before a vowel)" — on a verb the prefix is the ergative 'they', as the part's other notes call it (xquicam, xquicat). | "c- (the form of qui- 'they' before a vowel)". |
| 58 | n | style | "as quiꜭohe 'I am' in the earlier parts": it occurs only in 004. | "in the fourth part". |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| ꜩucubei, iꜩucubal | value | minor | Heads tzukub'ei, itzukub'al and root tzukuj, against the mt tzuqub'ei, itzuqub'al (pass 1: root tzuq). | Heads = mt; root tzuq 'feed, sustain', Brasseur's k = q. |
| ivalcual | value | minor | Head iwalkual; morphology "kual, the children of both parents" (pass 1 removed this from the note). | "iwalk'wal — your (pl.) children; iw- + alk'wal 'children', built on al 'a woman's child'; ejective restored". |
| tocobah | value | minor | Head tokob'aj against mt toq'ob'aj. | toq'ob'aj, from toq'ob' 'pity'; Ximénez leaves the ejective unmarked. |
| choc, xchoc, xoquic | value | minor | Heads choq, xchoq, xoqik and root oq, against mt chok, xchok, xokik (the verb ok, as xoc/catoc in the glossary). | Heads = mt; root ok 'enter'. |
| xunao | value | minor | Head xuna'o and root na', against mt xunao (004's nao). | xunao, na 'feel'; letters respelled, as nao. |
| ahꜭun | value | minor | Head ajkun and "kun" against mt ajk'un. | ajk'un; "the letter respelled as written (modern ajkun)". |
| xutiquiba | value | minor | Head followed the old mt. | xutikib'a', tikib'a' 'plant, begin'. |
| vcalibal | value | minor | "Brasseur reads the first letter as q": he prints u galibal, g = ꜫ. | "Ximénez writes plain c where Brasseur reads ꜫ (his g)". |
| varam | value | minor | "w- 'my' + aram": nu 'my' stands before it; the root is war (as pass 1 corrected in the note). | "waram — sleep; noun, war 'sleep' + -am". |
| xel | value | minor | "with no ending at the end of a clause": the -ik is missing because the clause goes on (pass 1's correction in note 22). | "with no -ik because more follows in the clause". |
| xuchaxic, xuꜭhaxic, xuꜭhax | value | minor | "x- completive + ch'a …" left out the u- that is in the form (pass 1's correction in note 52). | "x- completive + u- + ch'a 'say' + -x- (passive) + -ik" (xuꜭhax without -ik). |
| vcoc | value | minor | "u- 'its' + kok": an invented root. | "taken with ok 'enter', the c not explained (Brasseur x-uq-oc)". |
| caual | value | minor | "precious stones, jewels": jewels is yamanic, the other half of the pair (005 pass 2 corrected the same swap); "the cuval … written with a" stated as fact. | "kawal — precious stones (inferred); perhaps kuwal (cuval) … written with a; the letters respelled as written". |
| xchi | value | minor | "written apart before ka- + verb": in Xchi ca coh the ca is qa- 'we'. | "before the person prefix and the verb". |
| __broaden__ chiquih | value | minor | "chi + ki- 'their' + ij" would give chikiij; before a vowel the prefix is k-. | "chi + k- 'their' (ki- before a vowel) + ij 'back'". |
| __broaden__ ve | value | minor | The glossary's teeth reading is pinned to nay pu ve raxcavacoh; here ve is 'my teeth' (units 14, 16, 18). | Added "we — my teeth; w- 'my' + e 'tooth'". |
| __broaden__ xquicot | new | minor | Glossary "they rejoiced"; here 'they dug' (unit 51). | Added "xkikot — they dug; x- completive + ki- 'they' + kot 'dig'". |
| __broaden__ chi | new | minor | The glossary has 'let' but not the plural command ch- + i- of units 11–16, 21. | Added "chi — ch- (command) + i- 'you (pl.)', before a verb". |
| xcah | value | style | "k- (ki- 'their' …)" on a verb. | "'they'". |
| ivachbilan | value | style | "iw- 'your (pl.)'" on a verb; "the verb of qachb'ilan" pointed to another part's form. | "iw- 'you (pl.)' (i- before a vowel, the ergative) + achb'ilan 'accompany'". |
| canih | value | style | "I beg": the person is not in the word (Oh canih 'we beg'). | "beg, implore (inferred); a word of entreaty, with chiwech, chawech". |
| cunah | value | style | "the root of ajkun 'healer'": that is not the head of ahꜭun. | "the root of ahꜭun 'healer' (modern ajkun)". |
| tahoc | value | style | "(koto tajoq 'dug out')" pinned. | "passive ending -taj + -oq, written apart after a verb (inferred)". |
| __broaden__ cuꜭ | value | style | "ruk' with q- 'our'". | "q- 'our' (qa- before a vowel) + uk' 'company'". |
| __broaden__ pala | new | style | Glossary 'as many as'; here half of a question 'how far' (unit 57). | Added "pala — with janikan, in a question 'how far?' (inferred)". |

### Refused / left

- **Pass 1's decisions kept**: caual kawal (not kuwal); ajk'un and uq'exel by the letter; the coto family koto; xuchaxic xuch'axik
  against plain cha/xcha; ejectives restored in ik'ow, q'at, k'am, sik'in. I found nothing against them; they are owner questions.
- **Unit 41 `Xchin teleh` 'I shall carry'.** Left. in 'I' is the absolutive on a transitive root (one would expect a
  transitive form with v-/nu-); Brasseur reads 'je le porterai'. The note gives the parts correctly; whether teleh is an
  antipassive is not decidable from this text.
- **ba rendered "then" in l (units 11, 14, 17, 18), though the note calls it a particle of urging.** Left: consistent
  across the part, and the note explains it.
- **Unit 15 quivbah kiub'aj vs 005 quivubah kiwub'aj; unit 4 xil with no ergative; unit 46 xcam with no prefix.** Left, as pass 1.
- **Unit 52 i "we cannot get to the bottom of it"** (Brasseur 'nous n'en pouvons plus'). Left, marked inferred in the note.
- **Gloss entries not changed**: every other entry's head, meaning and morphology match the notes; uncertain senses are marked.
- **about**: checked against the units; every event is there and in order. No change.

### Points for QUESTIONS.md

1. Pass 1's seven points stand (caual kawal/kuwal; modern word vs letter for ajk'un, uq'exel, 005's uch'apa; 003's kaj
   → qaj; 004 xca nao / 006 xunao vs na'o; the k'ot family in 003 and 006; 004 sachulujuj → saqjulujuj; 004 ikowen → ik'owen).
2. The glossary entry `xquicot` ('they rejoiced', 001) and 006's 'they dug' share mt xkikot; the toggle cannot tell them
   apart. Fine by the letter rule; noted for the owner.
3. House renderings to copy into conventions.md (confirmed): ahau → the lord; lal ahau → my lord (lal the respectful
   'you'); ahꜭun → a healer; naual atit, naual mama → an old woman of spirit power, an old man of spirit power; omuch
   ꜭaholab → the four hundred boys; Vꜩ bala → Very well; vbac vvach → his eyes (l its-bone his-face); vꜫexel → a replacement.
