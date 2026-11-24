# Review — popol-vuh-007

## Pass 1

Reviewer pass 1, 2026-11-24. I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md (the text and the
establishment log), popol-vuh-001…006.json, popol-vuh-glossary.json, wordre.py, the 006 review and the draft units.json
(55 units). For meaning I used only Brasseur 1861 (OCR lines 20470–20960: K'iche', French and notes) and the glossary.
I opened no modern translation and recalled none. Every edit was made by script (json load/dump, ensure_ascii=False,
indent=1). No `t` was changed, and no unit was added, removed or moved. gloss.json was not touched.

I compared every mt with 001–006 by script (MS form → modern form). The only difference is `cah` (unit 48), which is qaj
'we want' here and kaj 'sky' in 001; the note explains it, and it agrees with 006's xcah → xkaj 'they wanted'. I also
compared roots across forms by hand, which the script cannot do. That found four splits: the bite verb (003/004 ti'o),
chi + cut (always chik in 002–006), taca/zacbal against Brasseur's k and the words the notes tie them to, and rixcac
against the drafter's own restorations. I checked every cross-reference to an earlier part and every Brasseur claim
against the OCR. Two Brasseur claims were wrong (unit 37 'claws', unit 36 'arches of greenery'), and one cross-reference
did not hold (unit 13 taquentah). Every establishment-log item is mentioned in the note of its unit.

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 55 units, and the units' `t`, joined in order,
give back the packet's 18 paragraphs exactly, paragraph by paragraph.

Counts: **major 0 · minor 13 · style 11** (24 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 15, 17 | mt, n | minor | `cucah` → qukaj. Brasseur prints k'uqah (his q = ꜭ) and translates 'boire', and the verb is the certain uk' 'drink' (ta cucah ri ca qui 'when we drink our drink'). The drafter restored ejectives on the same grounds in xecabar and chacab, so this one was inconsistent. | mt quk'aj ×2. The note gives q- + uk' + -ah, Brasseur's spelling, and says that the ejective is restored. |
| 20, 22, 23 | mt, n | minor | `rixcac` → rixkak, letter for letter. The word ('his nails', in a couplet with 'hair', Brasseur r'ixgag, 'ongles') is as certain as q'ab'ar or aq'ab', which the drafter restored. | mt rixk'aq ×3, the modern word. The note says that the word is certain and cites xecabar and chacab. Brasseur's g in the first consonant goes to QUESTIONS. |
| 29, 30, 37, 51 | mt, n | minor | `chi` in xꜭha chi cut, Are chi cut, pahac chi cut → chi. In 002–006 every chi + cut/cu that stands for chic gives chik (2:5, 2:29, 4:11, 5:8, 6:45 …), and the `l` here reads it as 'again/now'. Brasseur writes chicut each time. | mt chik in all four. The notes say that chi is chic, its c shared with cut. |
| 33 | mt, n | minor | `taca` → taka. The note follows Brasseur's division chi tak a 'by the rivers' (his k = q): this is taq, the plural word, which this part itself gives as taq (unit 36 pa tac). | mt taqa. The note says why. |
| 29 | mt, n | minor | `zacbal` → sakb'al. The note derives the word from zac 'white' (saq in 001, 005, 006), and Brasseur prints zakbal (k = q). Both witnesses say q. This is the 006 rule (ꜩucubei → tzuqub'ei): a choice against every witness is changed. | mt saqb'al. The note says why. |
| 45, 53 | mt, n | minor | `vtio` → utio and `tionic` → tionik. The bite verb has the glottal stop in 003 (xtio → xti'o) and 004 (itio → iti'o, catio → qati'o). | mt uti'o and ti'onik. The notes cite the earlier parts. |
| 36 | i | minor | "the head(?) of the ec plant". The note (and Brasseur, 'une tête d'ek') says that vvach is the crab's head, made of ec. The `i` made it the plant's head. | "For its head they used ec, the ec that grows all through the forests." |
| 50 | i, n | minor | "Will you not come along, boys?" The guess had no source, and the note set it against the only witness, Brasseur's 'Où donc se trouve-t-elle?'. | i "Where is it, then, boys?" The note says that this follows Brasseur and is a guess. |
| 7 | n | minor | "chi 'again' (chic, its c shared with the next word)". The next words are vi and vla, so no c is shared. | The note now says that chi is taken as chic without its c and may be the preposition, inferred. |
| 37 | n, i | minor | "Brasseur 'the great claws'". He has 'les grandes pattes' / 'les petites pattes' (legs). `i` also carried (?) four times. | n "the great legs (les grandes pattes)". i "That became the crab's legs, and pahac its small legs; and they put on a shell of stone for the crab's face and its back." |
| 13 | n | minor | "taquen 'keep on, follow', the verb of taquentah in the third part". 003 reads taquentah as 'be sent' (taq 'send'), so the note contradicted the published part. | "(inferred, after Brasseur); the same letters begin taquentah in the third part, taken there as 'be sent'." |
| 54 | n | minor | pacalic 'face up' was given as plain fact. Brasseur reads both pacalic and hupulic as stooping ('rasant la terre', 'en te baissant'), and the note did not say so. | Added that the sense is inferred from the pair, with Brasseur's French. |
| about | — | minor | "calls up … that he is still digging" (he asks them to come and take away the earth, for he has gone far down), and "drag their great tree to the edge" ('to the edge' is not in the text). | Both corrected. |
| 12 | n, i | style | vꜩin was glossed 'succeed' here, 'come to an end' in unit 21 (the same verb, as that note says), and 'be finished' in 006 (chuꜩinoc). "how well we have done with him" can mean 'finished with him'. | n "vꜩin 'be finished, come right' (vꜩ 'good' + -in …)". i "how well we have dealt with him". |
| 7, 49 | i | style | "(?)" in `i` (sheltered(?), echoing(?)). No published `i` has one, because the notes carry the doubt. In 49, "straight" renders nothing. | "sheltering". "a great mountain that echoes …; you will just come out there". |
| 6 | i | style | "only the sound of it comes down to me". The note says that the rendering follows Brasseur ('le son en est répercuté'), but 'comes down to me' is not his and not in the words. | "only its sound is echoed, like one echo, two echoes". |
| 9, 11 | l | style | chu racuh / xuracuh vchi was "cries-out(?)" in `l`. 005 and 006 give the literal "he-scraped(?) his-mouth" in `l` and leave 'cried out' to `i`. | "he-scrapes(?)", "he-scraped(?)". |
| 13 | i | style | "it would have been the end of us!" The note itself says that the words leave this unsaid (Brasseur's parenthesis 'de nous'). | "it would have been all over!" |
| 46 | i | style | "We would not go now". 'now' is Brasseur's 'maintenant'. The note gives on as 'perhaps'. | "We would not go to catch it". |
| 48 | n | style | "(not cah 'sky'; and the k- 'they' of xcah 'they wanted' in the last part)" was garbled. | "(not cah 'sky'; the same verb as xcah 'they wanted' in the last part, there with k- 'they')". |
| 29 | n | style | The toggle's ch'umilal was not explained. | "(toggle ch'umil, as in the fourth part)". |
| 33 | n | style | ꜩucuh 'seek' (tzukuj) stands beside 001's ꜩucul and 006's ꜩucubei (tzuq 'feed'), and the note did not say that it is a different root. | Added one sentence. |
| 36 | n | style | "used in arches of greenery". Brasseur has 'arcs de triomphe'. | "used to deck triumphal arches". |
| 25 | n | style | "(as xticaric)" did not say where. | "in the last part". |

### Refused / left

- **The drafter's restored ejectives: all kept.** `xecabar`/`cabarinac` → q'ab'ar: Brasseur has gabar (g = ꜫ) and 'ivres', so the word is certain. `chacab` → chaq'ab': aq'ab' is in the conventions' list, Brasseur has ch'agab, and 003 restored acabal → aq'ab'al the same way. `caholab` → k'ajolab': the plain c is a slip in a certain word, and the note says so. `ꜩiquin` → tz'ikin, as 001/002's ꜯiquin. `tocoba`/`tocob` → toq'ob', as 006. `chumilal` → ch'umilal, as 004. `xuꜫat` → q'at: the establisher chose the letter ꜫ, so nothing is restored. The ziquin family → sik'-, as 002 and 006.
- **Letter for letter: kept.** `cot`/`coto` → kot/koto, as 006 (QUESTIONS 006 (4)). `qux` → kux (Brasseur also c; 'gnaw' inferred). `zcaquin` → skakin (Brasseur the same). `ecouic` → ekowik: the identification with ik'ow is inferred, so nothing is restored. `ec`, `pec`, `mac`, `xtubuquih`, `Laquiba` keep k where Brasseur has k (= q) or q (= ꜭ). These words are unknown, and 006 decided (chaquimah) that Brasseur's letter alone does not settle such a word. See QUESTIONS.
- **`recah` → reqaj: kept.** Brasseur has r'ekah (k = q), and 'carry on the back' fits. **`chuꜩucuh`/`ꜩucuh` → tzukuj 'seek': kept** against Brasseur's tzukuh (k = q). His own French has 'en cherchant' (unit 34) and 'que je cherche' (unit 41), and the k-word 'seek' fits all three places. The note now separates it from tzuq.
- **`quilo`, `cucah`, `ca`, `caxol` as q- 'we': checked and right** (Brasseur k'ilo, k'uqah, ka, kaxol).
- **`xchax` → xch'ax: kept**, as 006's xuchaxic/xuꜭhax (QUESTIONS 006 (5)).
- **Unit 54, `ca xibih rib` read as the crab taking fright, against Brasseur's 'nous nous prîmes de peur': kept.** rib is the 3rd-person reflexive, and the verb has no ca- 'we'. Compare unit 45, `ca ca xibih quib` 'we frighten ourselves', with both. The reading also completes the pair: face down, it bites; face up, it takes fright. The note gives Brasseur's reading.
- **Unit 12 `i`: kept** apart from the two small changes above. "it has come right" is built from vꜩin.
- **Unit 31, the subject of `xchac`: checked.** Zipacna, beaten 'by them' (cumal). Brasseur has 'quand il fut vaincu'.
- **`Moꜩ` as "Motz" in `i`: kept.** Names respell ꜩ as tz (Q'ucumatz, Camalotz), and the about adds 'the Pleiades' with Brasseur.
- **Unit 3 `icama` → ikama: kept**, as 005/006's cama → kama, which the note cites. See QUESTIONS for the split with 006's xquicam → xk'am.
- **Unit 32 `i` "the boys' hearts" beside "the four hundred boys".** Left. The text has the same doubling (caholab … omuch chi ꜭaholab), and the note names Hunahpu and Xbalanque.
- **Unit 54 `i` "we came within a little of catching it".** Left: it is idiomatic and follows the words.
- **For the glosser / pass 2:** the keys must match the final mt: cucah quk'aj, rixcac rixk'aq, zacbal saqb'al, taca taqa, vtio uti'o, tionic ti'onik. `chi` 'again' (chic) as chik before cut is already the published practice (glossary chi → chik broaden if missing).

### For QUESTIONS.md

1. **Brasseur's k (= q) in words not otherwise known.** In 007, a word is given q where the note ties it to a known q word (saqb'al, taqa, reqaj, as 006's tzuqub'ei). Words not otherwise known keep k (ek, pek, xtub'ukij, Lakib'a, as 006's chakimaj). A house rule would settle it. Meanwhile, the rule just stated.
2. **The modern word or Brasseur's letter when an ejective is restored.** rixcac → rixk'aq follows the modern word ixk'aq, where Brasseur's gag (ꜫ…ꜫ) would give ixq'aq'. Decide together with the 006 question about ajk'un, uq'exel and uch'apa.
3. **The 'take' verb is split.** 005 and 006 (cama → kama) and 007 (icama → ikama) keep k, while 006's xcam, xquicam and xcamouic give k'am. These should be decided together.
4. **tzukuj 'seek' against tzuq 'feed'.** 007's ꜩucuh is tzukuj, while 001's ꜩucul and 006's ꜩucubei are tzuq. Brasseur writes tzukuh for both, so his k does not separate them.
5. **pacalic / hupulic.** 007 reads them as 'face up' and 'face down', against Brasseur's 'stooping' for both. 008 continues the episode (Brasseur pagal curi tap x-akanic, pagalic c'akanic) and should keep the same reading.

## Pass 2

Reviewer pass 2, 2026-11-24 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
packet.md (text and establishment log), popol-vuh-001…006.json, popol-vuh-glossary.json, wordre.py, the 006 review (its
pass 2), units.json as left by pass 1, pass 1's review, gloss.json (written by the glosser from the pre-pass-1 draft),
novel-forms.json and known-forms.json. For meaning I used only Brasseur 1861 (OCR lines 20470–20960, K'iche', French and
notes) and the glossary; no modern translation was opened or recalled. Every edit was made by script (json load/dump,
ensure_ascii=False, indent=1); no `t` was changed and no unit was added, removed or moved. Unit numbers are 1-based, as in
pass 1.

Units: I went through all 55 again (grammar labels against forms, K'iche' → l word by word, l ↔ i, couplets, the house
table, uncertainty labels, the establishment-log items, the about) and re-checked the Brasseur claims against the OCR
(all now hold). I re-ran the MS-form → mt comparison against 001–006 by script: the only difference is `cah` qaj (unit
48), explained. Every `chi` + `cut` gives chik; but pass 1's chi → chik edit in unit 51 also changed the *first* chi of
the unit (`ꜩiquin chi be tah ivvbah`, 'birds that you may go and shoot', Brasseur chi be-tah), which is the plain chi
'that'.

Gloss: I checked all 139 entries and every `__broaden__` value against the text and the final mt, by script and by
reading. Keys equal novel-forms.json exactly. Seven heads did not equal the mt: the six pass 1 listed, and `ya` (river
head ya' against mt ya). The chi → chik change touches no key (chi is a known form; the glossary already has chik). Every
`__broaden__` value began with the glossary entry verbatim; one of the glosser's (nu) cited a form (ta'o) that is not the
mt. I compared each of the 143 known forms' uses in 007 with its glossary entry and added seven broadenings the glosser
missed. `__broaden__` now holds 14 keys (7 from the glosser, 7 added).

Afterwards the JSON parses, len(mt) == len(WORD_RE.findall(t)) for all 55 units, the units' `t` joined give back the
packet's 18 paragraphs exactly, gloss keys == novel-forms keys (+ `__broaden__`), every gloss head equals the units' mt
for that form, and every `__broaden__` value starts with the current glossary entry + " · ".

Counts: **major 0 · minor 27 · style 14** (41 findings; units 3, gloss 38).

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 51 | mt, n | minor | mt chik for the first chi (`ꜩiquin chi be tah ivvbah`), which is 'that' before the verb (l 'that go', Brasseur chi be-tah); pass 1's chi → chik change caught it along with xꜭha chi cut. | mt chi; the note now says which chi is which. |
| 15, 17 | l | style | "we-drink(?)": the note (since pass 1) calls the verb certain and the toggle restores the ejective. | "we-drink". |
| 22 | n | style | "iv- 'you (pl.)' (i- before a vowel)" read as if i- were the prevocalic form. | "(the form of i- before a vowel)". |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| cucah | value | minor | Head qukaj, "ukaj … (inferred)" against mt quk'aj and the note (certain verb uk'). | "quk'aj — we drink; q- + uk' 'drink' + -aj; the ejective restored (Brasseur k'uqah)". |
| rixcac | value | minor | Head rixkak against mt rixk'aq. | rixk'aq; Ximénez's plain c, the modern word in the toggle. |
| zacbal | value | minor | Head sakb'al, root sak, against mt saqb'al. | saqb'al, saq 'white, clear' (Brasseur zakbal, k = q). |
| taca | value | minor | Head taka against mt taqa; Brasseur's division not given. | taqa; Brasseur's tak a, taq the plural word. |
| vtio | value | minor | Head utio, ti, against mt uti'o (as xti'o, iti'o, qati'o). | uti'o, ti' 'bite'. |
| tionic | value | minor | Head tionik against mt ti'onik. | ti'onik, ti' 'bite' + -on- + -ik. |
| ya | value | minor | River head ya', against mt ya (the note: the toggle respells the letters). | "ya — river, water (inferred, after Brasseur); the letters respelled as written". |
| icama | value | minor | "kama, a verb of taking not otherwise known": the glossary has cama 'take' (005/006). | "kama 'take', the verb of k'am, its letters respelled as written". |
| taquen | value | minor | "the verb of taqentaj in an earlier part": 003 reads taquentah as 'be sent' (pass 1 corrected the same in note 13). | "(inferred, after Brasseur); the same letters begin taqentaj, read 'be sent' in an earlier part". |
| quicot | value | minor | "ki- 'they' + kot 'rejoice'": the root is kikot 'be glad' (glossary xquicot); 'they' is in que. | "verb root kikot 'be glad', as in xkikot 'they rejoiced'". |
| ecouic | value | minor | "e 'they' + ik'ow + -ik": 'they' is que; the note takes ecouic as a variant of icouic. | "passing (inferred); taken as the verb of ikowik 'pass' (ik'ow), respelled as written". |
| vxul | value | minor | "its claws … ('the great claws')": Brasseur has les grandes pattes (pass 1's correction in note 37). | "its great legs (inferred) … ('les grandes pattes')". |
| ꜭazlic | value | minor | Root "k'asl": the glossary's root is k'as (k'aslem = k'as + -lem). | "k'as 'live' + -lik, of one root with k'aslem". |
| vila | value | minor | "ch- (command) + iw- …": ch- is not in the form (it is in chi). | "after chi (ch- + i-): w-, the rest of iw- before a vowel, + il + -a". |
| cabih | value | minor | "ka- 'two' with a day word": morphology invented, not in the notes. | Dropped; adds 'the second day' (unit 19). |
| xuracuh | value | minor | "he cried out" stated plainly; the note and glossary racuh mark the scrape idiom inferred. | "he scraped (inferred) … with uchi' 'his mouth' taken as 'he cried out'". |
| pacalic | value | minor | "face up" with no hedge; the note says inferred from the pair, against Brasseur's 'stooping'. | "(inferred) … (Brasseur reads both as stooping)". |
| mac | value | minor | "perhaps a second plant name": invented; the note says only 'not otherwise known'. | "not otherwise known; printed as written, beside ek, a plant". |
| __broaden__ nu | value | minor | Example "ka nu ta'o", against mt tao. | "ka nu tao". |
| __broaden__ ca | new | minor | Glossary has qa/ka (ongoing, uncertain); here ca = cab 'second' (unit 2, chu ca) and an unexplained particle (units 6, 22, 26 ×2, 44, 55). | Added "ka — second (inferred) … · ka — (unclear) a particle before a verb or a word of state, left unrendered". |
| __broaden__ apanoc | new | minor | Glossary "later, in time (guess)"; here 'away, over there' (unit 11, xcah apanoc ri che). | Added "apanoq — away, over there; apan 'go there' + -oq, after a verb of motion". |
| __broaden__ xe | new | minor | Glossary has 'they' and xe' 'root' pinned to the title line; here xe' 'the foot, the bottom of' (xe che, xe zivan, xe nima huyub). | Added "xe' — the foot, the bottom of (a tree, a mountain, a ravine)". |
| __broaden__ xuꜩin | new | minor | Glossary 'it succeeded, came right'; here 'is he finished?' (unit 21; the note: 'come to an end'). | Added "xutzin — it was finished, came to an end". |
| __broaden__ na | new | minor | Glossary 'now, then; still'; here qui na 'their feeling' (unit 26). | Added "na — feeling, sense (inferred); na 'feel', the root of nao". |
| __broaden__ vcoc | new | minor | Glossary 'its going in' (006); here the crab's shell / the false crab (units 37, 38). | Added "ukok — its shell (guess), the false crab … (Brasseur 'tortue')". |
| __broaden__ cat | new | minor | Glossary 'you (one) shall'; here ongoing (cat be 'you are going', cat bec, cat el, cat oc). | Added "kat — you (one), of what is going on; k- 'ongoing' + at". |
| petoc, chul | value | style | "the plural 'you' of kix carried over from the word before": pinned to the line. | General wording (after kix / a command before it). |
| rachac | value | style | The entry covered only unit 3; in unit 37 (rachac tap) the note says it is not clear. | Added "elsewhere not clear". |
| tao | value | style | "I hear it": the person is in nu-, not the form. | "hear it … (ka nu tao 'I hear it')". |
| quilo | value | style | "we shall see": 'shall' is from chi. | "we see (it)". |
| bec | value | style | "b'e + -k"; the note has -ec. | "b'e 'go' with -ek (inferred)". |
| apan | value | style | "go there; verb, as in apanoq 'later, in time'": tied to the glossary's guess, and the use is adverbial. | "over there, away; taken as apan 'go there', the root of apanoq". |
| xcoh | value | style | "we shall (return)": the verb in brackets is another word. | "we shall". |
| caholab | value | style | "a second spelling": the note calls the plain c a slip in a certain word. | Says so. |
| __broaden__ qui | value | style | Last reading not in the format (meaning; morphology). | "ki — how, so (inferred); a word of degree before utz 'good'". |
| __broaden__ tana | value | style | Pinned to chi qa tana. | "tana — listen, wait (guess); a verb after chi qa 'let us' …". |
| __broaden__ cah | value | style | Pinned to ma b'a chi qaj. | "… as xkaj 'they wanted'". |

### Refused / left

- **Glosser's seven broadenings kept** (qui drink/degree, oc -oq, pa question, nu ergative 'I', tana, cah 'we want', chire
  'at his teeth'): each is a sense the glossary entry does not have.
- **No broadening for** `pu` (the note's 'also'? is the glossary sense; 'in' is a bare guess), `vbi` as 'its sound' (a
  guess in one line; `l` keeps 'its-name'), `xuxic` 'it became' (same sense; the person is not in the form), `chiquech`
  'from among them' (the relational chi covers 'to, from'), `ꜭahol` 'boy' in address, `vvach` as the crab's head (face →
  head inferred, `l` keeps 'its-face'), `la` in `re la` (the glossary's 'unexplained particle' covers it), `xꜭha` 'it is
  said' (the same verb used impersonally).
- **Unit 20 `l` "their carrying(?)" against the note's 'they carrying'**: left; qui is ambiguous (possessor or ergative)
  before a participle-like form, and the (?) holds the doubt.
- **Unit 40 `i` "they asked Zipacna" for xchax 'he was told'**: left; the words spoken are a question.
- **Pass 1's mt decisions** (ejectives restored in quk'aj, rixk'aq, q'ab'ar, chaq'ab', tz'ikin, toq'ob'; letter for letter
  in ek, pek, mak, xtub'ukij, Lakib'a, kot/koto, ekowik, kux, skakin): I found nothing against them.
- **The about**: checked against the units; every event is there, in order. No change.

### For QUESTIONS.md

1. Pass 1's five points stand (Brasseur's k in unknown words; modern word vs Brasseur's letter for restored ejectives,
   rixk'aq; the 'take' verb kama/k'am; tzukuj vs tzuq; pacalic/hupulic for 008).
2. **`ya` 'river' (unit 39) is printed ya**, letter for letter, while ha in this part (racan ha, unit 49) is ja' 'water'.
   Brasseur gives 'rivière' for ya. Whether ya is a separate word, or ha written with y, is for the owner; meanwhile the
   toggle respells the letters.
3. **`vcoc`** is 'its going in' in 006 and 'its shell' (guess, Brasseur 'tortue') here, with one mt ukok. Fine by the letter
   rule, but 008 (Brasseur x-uq-oc, u coc) should settle which reading carries on.
4. No new house rendering in this part.
