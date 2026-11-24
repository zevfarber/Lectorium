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
