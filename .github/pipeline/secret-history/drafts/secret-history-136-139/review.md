# Review (pass 1) — secret-history-136-139

Reviewer pass 1. `units.json` edited in place by script (`t`, `ln`, `p` untouched; re-verified: 54 units, 387 words, each consumed exactly once in order, `t` identical to the packet's romanized words for all 54 units, `p: true` on units 0, 23, 38, 45 = the first unit of §136, §137, §138, §139, per-word sum of Ming brackets equals the packet gloss for all 387 words). Every Han quotation in the notes and morph glosses was re-checked mechanically against the unit's packet glosses; the slips found are in the log.

Unit numbers are 0-based positions in `units.json` (unit 0 = §136 `Čiṅgis Qaγan-(n)u aγ̇uruγ …`, unit 23 = first of §137, unit 38 = first of §138, unit 45 = first of §139). "w3" means the fourth word of the unit.

Sources used: conventions, runbook, packet, the model `secret-history-01-06.json`, the published parts (for house renderings), `drafts/secret-history-131-135/` (units, review), the glossary, `known-forms.json`, and Shiratori's text and Ming glosses in `source/` for §§46–49, 122 and 139 only. No modern translation was opened.

## Counts (log entries; a bulk entry covers several places)

| severity | entries |
|---|---|
| major | 1 |
| moderate | 8 |
| minor | 21 |
| trivial | 9 |
| total | 39 |

## Changes

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 12 | morph, l, i, n | major | bolulaγ̇i (Ming 做了) was read as an optative 'let us make' (-γ̇i). The form is bolu- + -laγ̇i, the back-vowel partner of -leġei (büleġei, keġeldüleġei: a past, Ming 來/了), and the Ming glosses this part's hortatives 咱 (morilaja 上馬咱 unit 10, žokilduja 商和咱) and this word 了. As the draft had it the speech's last sentence was a proposal ('let us press on them … and make enemies of them') that nothing in the form or the Ming supports; it also dropped basa 'again' | morph bolula- + -γ̇i → bolu- + -laγ̇i (past; glossary already has bolu-); l 'enemy they also became'; i 'Now, once more leaning on the enemy, they too have become enemies'; note rewritten with the reasoning and the guess ('the enemy' = the Tatars) marked |
| 6, 7, 9, 10, 11, 12 | i, n | moderate | Shiratori's quotation opens at `"Žürkin-(n)e` (unit 6) and closes only at `bolulaγ̇i"` (unit 12); units 6–12 are one speech of Chinggis's. The draft closed the quotation in unit 6 and told 7–8, 10–11 as narration ('they struck', 'he said'), then slipped into 'we gave back' in 9 | unit 6 i leaves the quotation open (house practice: open at the first unit, close at the last); units 9–10 use single marks for the inner speeches; 10 'we said' (keġen has no subject; bida 'we' recurs); notes of 6, 7, 9, 10 say so |
| 11 | i, n | moderate | 'Waiting six days for the Jurkin, they had not come': the participle's subject is 'they', i.e. the Jurkin, so the Jurkin wait for themselves. The accusative Žürkin-i is the object of külčežü, the waiters are unnamed | 'We waited six days for the Jurkin, and they did not come' (the speech is first person); note says the waiters are unnamed and cross-refers to the previous part's iregdeküi |
| 11 | n | minor | 'did not come (and so broke faith)': 'broke faith' is in neither the form nor the Ming (破來了) | removed |
| 20 | i, n | moderate | i 'Let our words be brought home to us' makes the locative üges-tür 'in the words' the subject and man-u (a genitive 'ours') a dative 'to us'; the form has neither. Unit 22 repeats the frame (üġes-tür an-u kürgen) and the draft itself renders it 'in their words' | i 'Let it be brought to pass in our words'; note aligned, points to unit 22 |
| 24 | morph (Žürkin-dür) | moderate | -dür labelled 'against, to' where l and i read 'among' (a- 'were' with a locative) | 'in, among' |
| 29 | l, i, n | moderate | morph and Ming say an-u 'their' (plural, 肝每 'livers'), but l and i gave 'his' and a singular 'liver'; the same oath uses the singular in-ü for the heel-tendon and the life | l 'livers their', i 'if they leave your door, cut out their livers and cast them aside'; note says why (an-u/eliged plural; heilüġešü has no person) |
| about | about | moderate | said the three Jalair men 'give themselves and their sons': only Kügün-Uqa and Chila'un-Gaichi bring (two) sons; Jebke is given to Qasar; no one gives himself. 'The Tatar campaign they failed to join' left the speech out; 'putting aside' of Sacha-Beki and Taichu was unattributed | reworded to what §137 says; §136 mentions the speech and that the two put themselves aside by their own words |
| 14, 15, 24, 31 | morph (Sača-Beki ×2, Čilaγ̇un-Γaiči ×2) | moderate | 'beki a title, chief' and 'Γaiči a title, a cattle-herd?' are outside knowledge; the glossary says of beki 'the meaning of beki is not known from these sources' | 'the sense of beki / Γaiči is not known from these sources' |
| 53 | n, morph (öġer-ün) | moderate | claimed öġer-ün 'elsewhere means other'; the glossary entry for öġer-ün (自己(的)) is 'own, self', so the note contradicted the published parts (and öġere 'otherwise' in unit 35 is a different word) | note and morph say 'own, as in the earlier parts' |
| 38–41 | morph (oldaγsan ×4), n | minor | morph invented a verb olda- 'find, get'; the glossary has ol- (olba [得了]) and the sibling boldaba is read bol- + -da- | ol- + -da- (function unclear) + -γsan; note aligned |
| 25 | morph, l, i, n (köġud(i)-jer(i)-jen) | minor | 'obscure ending (perhaps instrumental)' where the known entry köġüdi already analyses the same pattern (köġüd(i)-jer-en 'with one's own sons', the (i)s Shiratori's); l and i lost the 'with' | split köġü + -d + -jer (instrumental) + -(i)jen; l 'sons-with-own'; i 'coming to an audience with his two sons Muqali and Buqa' |
| 13 | morph (Ködöġe-Aral, Dolγ̇an-Boldaγ), n | minor | 'aral river-meadow', 'perhaps seven hills' and the note's 'Boldaq hills' are not in the Ming (地名 only) | aral 'perhaps island, as in Baljun-Aral'; the rest removed |
| 0 | morph, n (aγ̇uruγ) | minor | 'baggage' is not in the Ming (老小營, camp of the old and young) | removed; 'rear camp' marked as my rendering |
| 53 | morph (emčü) | minor | gloss copied from unit 28 ('so private slave'); the noun here is irgen | removed |
| 47 | morph (-ü- of irgen-ü-ġen) | minor | labelled a mere linking vowel; the phrase is 'from the inside of his own people' (dotorāča), so -ü- is the genitive, with -ġen after it | relabelled genitive, linking vowel kept as an alternative; note adds it |
| 25, 31 | morph (aγ̇ulžažü) | minor | -žü labelled 'back-vowel form'; the printed ending is -žü (pass 1 of the last part relabelled the same kind of slip) | 'front-vowel form; printed -žü after a back-vowel stem' |
| 1, 4 | morph (aγ̇uruγ̇ud) | minor | plural given as -d though the printed word is aγ̇uruγ̇ud (aγ̇uruγ + -ud, as in Dolγ̇an-Boldaγ̇ud in unit 13) | lemma -ud |
| 46 | n | minor | §49 (published) names Ökin-Barqaq's son Qutuγtu-Jürki, this section Sorqatu-Žürki (as §122); the draft did not tell the reader | one sentence: the text does not say whether they are one man |
| 45 | l, morph, n | minor | l 'Ökin-Balaqaq' (Shiratori: Balaqaγ); note said §§43–54 print Barqaγ without saying where or that the Han differs (巴剌 here, 巴舌兒 in §§48–49) | l Ökin-Balaqaγ; note: §§48–49, the Han difference, the eldest-son reason for identification |
| 50, 52 | morph (omoγ ×2) | minor | 'pride' is not in the Ming (勇) | 'daring, courage' |
| 50 | morph (aγ̇ur) | trivial | cites Ming 剛氣 (unit 49's word); this word's gloss is 氣有的(每) | 氣 |
| 39 | n | minor | 'the Besüd are a branch of the Taichi'ud in this telling': the text says only Taičiγ̇ud-un dotora Besüd-ün nutuγ-ača | 'sets the Besüd camp inside the Taichi'ud and says no more' |
| 48 | i | minor | 'skilled with the arrow-thumb' is not what heregei-dür hončitan says (in the thumb, able to shoot); 'lungs full' reordered | 'able to shoot with the thumb, with full lungs' |
| 52 | i | minor | 'the Jurkin of the clan-name' is not English and leaves oboγtu-ji unexplained | 'the clan-holding Jurkin' (reading in the note) |
| 15 | l | minor | 'Behind them' drops the ablative -ča ('from behind'); 'Teletü's' supplies a genitive that is not there; 'having-overtaken' for a -žü converb | 'From-behind them', 'Teletü mouth-at', 'overtaking' |
| 9 | l | minor | 'withdrawing' drops the causative -uγ̇a- that the morph and the known entry carry | 'causing-to-withdraw' |
| 0, 3, 4, 5, 7, 9, 12, 14, 15, 16, 18, 23, 24, 25, 31, 36, 37, 38, 39, 40, 41, 43, 45, 46, 47, 52, 53 | l | minor | conventions: names in `l` are Shiratori's forms; the draft wrote Chinggis Qahan, Sacha, Taichu, Qorijin, Qughurchin, Shikiur, Jalair, Bayan, Chila'un-Gaichi, Jebke, Tüngge, Qashi, Küchü, Kököchü, Shigigen, Taichi'ud, Högelün, Boroqul, Jurkin, Qan, Sorqatu-Jurki | Čiṅgis Qaγan, Sača, Taiču, Qorižin, Quγ̇určin, Šikiγ̇ur, Žalair, Bajan, Čilaγ̇un-Γaiči, Žebke, Tüṅge, Qaši, Küčü, Kököčü, Šigigen, Taičiγ̇ud, Höġelün, Boroγ̇ül (unit 37) / Boroγ̇ul (38, 41), Žürkin / Žurkin as printed in each unit, Qān, Sorqatu-Žürki (English stays in `i`) |
| 9, 16, 18, 21, 22, 52 | l | minor | conventions: converbs as '-ing'; -žu/-žü rendered 'having-…' | 'being-said', 'Seizing', 'Being-told', 'making-known', 'causing-to-know', 'subduing' (-ġed/-uγ̇ad converbs keep 'having-') |
| 13 (w4), 15 (w4), 29 (w3), 35 (w2), 1 (w0), 4 (w1, w2) | morph brackets | minor | Ming brackets counted twice (büküi-dür [有] [有 時] [時]; amasar-a [口 行] [行]; eliged [肝每] [每]; (n)eče [行] [行]; aγ̇uruγ̇ud-tur and qosoruγsad likewise), so the sum did not equal the packet gloss | single bracket per morph; sums re-checked |
| 137 words (see list below) | morph gloss brackets | minor | the whole-word Ming gloss sat on the first morph (qaγan [皇帝 的], bida [咱的], irgen [百姓 行] …); the published house (131-135 pass 1, pass 2) puts the case/plural/possessive/participle marker's Ming (的, 行, 裏, 時, 每, 有的, 麽) on the suffix morph. Verb endings (了, 着, 呵) stay on the stem as in the published parts | split by script, sum per word re-checked against the packet |
| 3 | l | trivial | 'Žürukin-to' where unit 6 has 'Žürkin-by' for the same agent dative | 'by' |
| 8 | i | trivial | müd-kü 'also' in l and in unit 7's i, dropped in this i | 'too' |
| 28 | i, n | trivial | i 'your own slave' against l 'private' and unit 53's 'private people'; note 'of the house' for egüden 'door' | 'private'; 'of the door' |
| 45 | l | trivial | l 'custom' against the note's 'reason' (Ming 理); josun in the published parts is 'the reason thus' in l | 'reason' (i keeps 'account', as 109-114 does) |
| 47 | n | trivial | 'runs on for three units': the sentence runs from unit 47 to teimü in unit 51, five | corrected |
| 15 | n, morph | trivial | 'a pass or opening' for amasar is not in the Ming (口) | removed |
| 12 | n | trivial | cites 咱 without saying where | 'in unit 10' |
| 41 | n | trivial | (addition) the identity of the §138 Boroγ̇ul with §137's rested on the name and frame alone | the Han (孛舌羅兀勒) is identical in both |

### Words whose Ming brackets were split between lemma and suffix (137)

unit:number of words — 0:2, 1:3, 2:1, 3:1, 4:4, 6:1, 7:4, 8:2, 9:1, 10:8, 11:3, 12:4, 13:6, 14:1, 15:3, 16:1, 19:1, 20:2, 21:1, 22:4, 23:1, 24:5, 25:1, 26:2, 27:3, 28:2, 29:4, 31:2, 32:1, 33:3, 35:3, 36:1, 37:5, 38:5, 39:6, 40:5, 41:5, 42:1, 43:5, 45:3, 46:1, 47:4, 48:4, 49:2, 50:3, 52:3, 53:4. (Includes the seven words whose brackets had been counted twice, the four oldaγsan words and bolulaγ̇i; the full list is the diff against the draft.)

## Findings refused (nothing changed, or only flagged)

- **The oaths of §136 (unit 19–22): 'We did not hold to the word we spoke' (ba ese kürbe).** The idiom 'arrive at the word' = 'keep to the word' is the drafter's; the Ming gives only 不曾到了. i commits, but the note says the idiom is uncertain and the morph is literal. Kept; listed under doubts.
- **gebe / gedkün 'cast aside' as execution (units 22, 29, 33, 35).** Only the Ming 撇 and the context (ami in-ü tasulžu gedkün, 'cutting off his life, cast aside') support it; the note for unit 22 says exactly that and the reading is not pushed into i beyond 'cast aside'. Kept.
- **Unit 34 'Raising the wide door, let him give' (örgen egüden ergüžü ögtügei).** No better rendering is derivable from grammar plus Ming 擡着 敎與; the note flags it as a possible ritual figure. Kept.
- **Unit 43 bolγaquju.** The structure bol- + -γa- + -qu + -ju is sound (the causative as in bolγaba, 'made into'; -qu the future participle, as in bolγaqu na žöb; -ju the Ming's 麽, and the known entry for ken-e has the same frame ken-e boldaqu-ju bi 'to whom am I made …?'). i adds 'else' ('to whom else could they be made?') as the force of the rhetorical question; the note already says it is rhetorical and uncertain. Kept.
- **Splitting -teġen of köġüd-teġen (unit 43) into dative -te + reflexive -ġen.** Probably right (compare irgen-ü-ġen), but the known entry köġüd-teġen treats it as a unit and the Ming (每 (自的) 行) does not separate; left as one morph with both Ming marks.
- **Unit 45 i 'The account of these Jurkin people' for josun 理.** l and note say 'reason'; the published parts render josun both ways ('the reason thus' in l, 'the account' in 109-114's i). Only l was aligned.
- **Qabul Qahan in `i` (units 45, 47) for Qabul Qān-u.** The house puts Qān in `i` as 'Qan' (To'oril Qan, Altan Qan) and Qaγan as 'Qahan', but 043-054 already calls this man Qabul Qahan, and the reader will want to recognise him. Kept 'Qahan'; l has Qān. Flagged below.
- **Onan against Onon in `i` (unit 7).** Published parts use 'Onan' throughout except 125-130 ('Onon'); kept 'Onan' with the majority. Flagged.
- **Unit 1 double-object reading (qosoruγsan-i … haran-u qubčan tonožuγ̇ui).** The note already says the Ming leaves it loose; kept.
- **Unit 6 'have done' against büleġei 'was'.** The note states the reading. Kept.
- **Unit 9 'they' as the party who proposed terms.** Note says it is a reading (the same open point as 131-135 unit 16–17). Kept.
- **Unit 10 tere + -ü for Teġün-ü (no -ġün- morph).** Gloss says the stem is teġün-; bida + -n- + -u has a separate -n- but the sources do not give a morph for -ġün-. Kept.
- **Unit 21 'gave them'.** The object of ögbe is unsaid; the note says so; 'them' is mild. Kept.
- **Quotation marks in units 32–35 (inner and outer speeches of Chila'un-Gaichi).** Shiratori's outer quotation runs from `"Altan` (unit 32) to `gedkün"` (unit 35) with inner 'keġen ögbe bi' clauses; the drafter's marks follow the inner clauses. Readable; kept.
- **Unit 47 'so saying' (keġežü after aqa).** The Ming 說着 after 長 reads oddly, as the note says. Kept; doubt.
- **Unit 49 'mouths full' plural for aman düġüreṅ.** Rendering choice; kept.
- **Unit 50 'could' (i) against 'can' (l, unit 51's note).** Narrative tense; kept.
- **Unit 53 l 'his' for in-ü against i 'their'.** The antecedent is the collective Jurkin; either is defensible; kept.
- **Notes that open with the Mongol instead of the lesson.** Refused again, as in 131-135 (restructuring is for the editor).
- **A Boroγ̇ül / Boroγ̇ul spelling split in `i`.** Shiratori's two spellings (units 37, 38, 41) share the same Han; `i` uses one form (Boroqul) as the house does for Boroγ̇ul elsewhere.

## Remaining doubts

1. **Unit 20 (kürge) with units 19, 21, 22.** The oath 'üges-tür man-u kürge' (now 'let it be brought to pass in our words') and the idiom in unit 19 rest on the Ming 敎到 / 到了 alone; unit 22's 'carried out to the letter in their words' agrees with it but proves nothing.
2. **gebe / gedkün / the 'cast aside' penalties** (22, 27, 29, 33, 35): whether the sentence is death, exposure or only putting away; i says 'cast aside'.
3. **Units 34–35** (ergüžü ögtügei 'raising the wide door, let him give') and the oath's second halves: sense uncertain, as the note says.
4. **Unit 43 bolγaquju:** the 'else' is the force of a rhetorical question; the alternative is a plain question 'to whom shall they be made [eyes and ears]?'
5. **Unit 12 bolulaγ̇i:** now a past on the strength of -leġei and the Ming 了; 'leaning on the enemy' = the Tatars is a guess.
6. **Unit 11 iregdebe:** the Ming 破來了 fits neither 'come' nor the passive of iregdeküi (previous part: 'were summoned'); i says 'they did not come'.
7. **§139 body-part idioms (unit 48–50):** helige-dür šülšütü, heregei-dür hončitan, aγ̇ušigi duγ̇uraṅ, žirügetü, aman düġüreṅ are read from the Ming word by word; hončitan, aγ̇ur-, šülšü-, omoγ- stems are all marked uncertain. **žürkimes** is kept as one unanalysed word; the derivation of the clan name from it is the chronicler's, and the note says so.
8. **Unit 45 / 46 Ökin-Balaqaγ = Ökin-Barqaγ:** identified on the eldest-son description (the Han differs); and Sorqatu-Žürki here against Qutuγtu-Jürki in §49 is a discrepancy of the text.
9. **Unit 37 / 38–41 Jebke and Boroγ̇ul:** Jebke as the subject of abčiražü rests on word order; the §137 and §138 boys are one person on name, frame and identical Han (孛舌羅兀勒).
10. **Unit 47:** 'keġežü' after aqa ('so saying') and whether -ü- of irgen-ü-ġen is the genitive.
11. **House spelling in `i`:** Qabul Qahan (recognition) against the Qan rule; Onan against Onon; apostrophes (Chila'un, Kügün-Uqa, Högelün) — for the editor.
12. **For the glosser:** lemmas changed here that the gloss must follow: -ud (aγ̇uruγ̇ud), bolu- + -laγ̇i (bolulaγ̇i), ol- + -da- + -γsan (oldaγsan), -jer (köġudi, jeri), the 'in, among' of Žürkin-dür (unit 24); the novel tokens `jeri` and `köġudi` should be read with the instrumental analysis.

# Pass 2 — secret-history-136-139

Reviewer pass 2. Every one of the 108 `gloss.json` entries was checked against the final `units.json` morph (lemma, meaning, grammar label, Ming bracket against `novel-forms.json`) at every unit where the token occurs. Key set re-checked with `r3lib.tokens`: gloss keys (108, plus an empty `__broaden__`) equal the novel-forms keys; every token of every `t` is in exactly one of novel/known; no keys added or removed. No modern translation opened.

## Counts

| severity | entries |
|---|---|
| major | 0 |
| moderate | 4 |
| minor | 3 |
| trivial | 2 |
| total | 9 |

## Changes

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 12 | gloss `bolulaγ̇i` | moderate | Still the old analysis (bolula- 'make, treat as' + optative -γ̇i 'let us'), contradicting the unit's morph bolu- + -laγ̇i (past) and the note | Rewritten: bolu- 'become, be made' + -laγ̇i, past, uncertain; Ming 做了 kept |
| 38-41 | gloss `oldaγsan` | moderate | Lemma olda-, which the morph (ol- + -da- + -γsan) does not support | Rewritten as ol- + -da- + -γsan, Ming 得了的 kept |
| 25 | gloss `jeri` | moderate | Called 'an obscure ending, perhaps an instrumental'; morph now says -jer instrumental | Rewritten: -jer, instrumental 'with', compare köġüd(i)-jer-en |
| 25 | gloss `köġudi` | minor | Said the bracketed i was a bare 'linking vowel' before the reflexive -jen, while the morph puts (i) with the -jer/-jen pieces | Reworded: köġü + plural -d, with the bracketed (i) as Shiratori's linking vowel; the instrumental sits under `jeri` |
| 1, 4 | gloss `aγ̇uruγ̇ud-tur` | moderate | 'plural -d' where the morph has -ud | Now 'plural -ud (… -ud after γ)' |
| 12, 24 | gloss `žürkin-dür` | minor | Only 'against, to'; unit 24 now has 'in, among' | Entry gives both senses |
| 37 | gloss `žebke-ji` | minor | Bracket [人名 行]; the packet's Ming for this word is 人名 only (and novel-forms says [人名]) | Bracket corrected to [人名] |
| 25 | n | trivial | Note still said 'an obscure -(i)jer(i)- (perhaps an instrumental)' after pass 1 settled on -jer instrumental | Note now says -jer, instrumental 'with', bracketed (i)s Shiratori's |
| 1 etc. | gloss `žürkin` | trivial | 'a spelling of Žürukin' reversed the known entry (Žürukin is the variant) | Reworded |


## Checked, no change
- All other entries agree with the final morphs; Ming brackets equal novel-forms except `žebke-ji` (fixed). `ügesi`, `egüden`, `ködölgeküi-dür`, `bolγaquju`, `ökin-balaqaγ` kept as they are.
- units.json: 54 units unchanged in count; no new remembered English found in the units re-read (12, 24, 25, 38, 1, 4 and the morph-changed words); notes for those units match the morphs.

## Refusals
- None.

## Remaining doubts
- The unit 25 'instrumental' reading of -jer rests on the earlier köġüd(i)-jer-en alone.
- `build`/`validate` were not run (validate refuses before a build).
