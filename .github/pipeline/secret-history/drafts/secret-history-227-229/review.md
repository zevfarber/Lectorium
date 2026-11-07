# Review — secret-history-227-229

## Pass 1

Units are numbered 0–62 in order of appearance in `units.json` (U0 = `Basa Čiṅgis Qaγan žarliγ bolžu`, U28 = §228, U33 = §229). Word indices are those of `packet.md` (0–448).

Mechanical checks run after the edits: `t` of every unit identical to the drafter's (and equal to the packet words of its run of indices); 63 units, 449 `words` entries, indices 0–448 each consumed once; every word has at least one morph; every Ming gloss in `[ ]` equals the packet's (449 of 449); quotation marks in `t` and `l` now agree unit by unit, and `i` carries the same marks plus the one supplied opening mark (U20); `p: true` on U0 (§227), U28 (§228), U33 (§229) and nowhere else; JSON valid. Edits were made in place by script (`/tmp/claude-0/-home-user-Lectorium/4fadb8a1-a117-531e-92d5-ef6520a5577f/scratchpad/review227.py`); the original is kept at `.../scratchpad/units227.orig.json`. No `t` field touched.

### Changes (unit · field · severity · what was wrong · what was done)

#### Major (3)
1. U23, U24 · i, l, n · major · `josutan böġesü` (Ming 理有的每) was rendered "are in the right", which makes those who deserve execution or a beating innocent and turns the rule round; the note's "once their guilt is established" was invented. Now "if there are those who deserve execution, and rightly so" / "…a beating, and rightly so"; the note says the rejected reading and why (Ming 合處斬的 / 合打的). l of U23 "let-us-have-cut-down" (there is no hortative; -ü + -že) → "we have-cut-down-indeed".
2. U43 · l, i, n · major · i made the quiver-bearers "give back their quivers" and the cooks give back their vessels, i.e. accusatives, when the forms are datives (qor-tur, saγ̇urin-dur(i)-jan, saba-dur(i)-jan, "to the quiver / to one's own seat / to one's own dish"). Now "Let the quiver-bearers go back to their quivers, the day guards to their own seats, the cooks to their own cups and dishes, each to his own"; the note explains the datives and says what is still uncertain.
3. U60, U61 · i, l, n · major · "let the night guard keep them" (ab- is "take", not "keep") and the man himself (küġün-i, accusative, twice) dropped from the objects; U60 "shall deal with that man" supplied a verb that is not there. Now U60 "As for the man who has asked the number — the night guard, that man —", U61 "together with the gelding he rode that very day, saddled and bridled, and the clothes he has on, let the night guard take"; the note gives both readings (man taken with his gear / only gear taken) and says `selte` favours the first. l of U61 began "That's that-very day's" (tere kü üdür-ün) → "That indeed day's".

#### Moderate (19)
4. U1, U5, U8, U16, U17, U19, U27, U29, U32, U34, U44, U45, U48, U49, U52, U53, U61 · l · moderate · Shiratori's printed marks are in `t` but were missing from `l` (published 224-226 keeps them in `l`, straight `"`). Marks restored in `l` at the places they stand in `t`; `i` unchanged (curly).
5. U2–U5 · i · moderate · "Buqa is to take one turn: let him enter…" invents "is to take" (nigen kešig has no verb) and doubles the finite verb. Now "Let Buqa enter on duty with one turn, having charge of the guardsmen and putting them in order" (same for the others); U2 note's "the command of one turn" removed, and the note now says nigen kešig has neither ending nor verb.
6. U13, U14, U15 · i, l, n, morph (word 109) · moderate · berkešijen was analysed as berkeši + reflexive -jen, against the glossary's berkešijeġsü (berkešije- "find hard", used in published 224-226 for the same phrase); U13 i had its own "if" and U14 a second condition. Now berkešije- + converb -n, "was finding it hard to go about in our presence"; U13 i is a verb-less qualifier ("Again, the same man, with no sickness of body and without having taken counsel…"), U14 carries the "if"; notes rewritten and the uncertainty said.
7. U9 · morph (word 60), n · moderate · bügüdgežü split as bügü + -d + -ge- + -žü (four invented morphs); the glossary has bügüdge- "to muster, count over" (bügüdgeġesü, stem uncertain). Now bügüdge- + -žü, note says so.
8. U20, U25 · morph (words 149, 175), n · moderate · aqalaγdaba / aqalaba lemma `aqala-`; the glossary (and 224-226 pass 2) analyse aqa + -la-. Now aqa / -la- / (-γda-) / -ba; notes reworded; U25 note says there is no person ending, so "I" is a reading.
9. U21 · n · moderate · note cited Ming 比我 for na-dāča; the packet has 我行 (比我 is the glossary's other reading). Corrected; also the confused sentence on min-u ("set after its noun, here before it") reworded.
10. U26 · n · moderate · note said min-u "stands before its noun"; it follows kešigten-i (end of U25), the genitive set after its noun as the glossary has it. Corrected. i "he lays a hand or a foot on them" → "brings his own hand and foot to bear on them" (kürge- "deliver", γar köl without "or").
11. U29, U30, U31 · i · moderate · "Among those outside, my guardsman ranks above the officers…" detached γadanadus ("outside-ones") from the officers it qualifies; U31 "my guardsmen and the officers of the thousands" supplied a conjunction that is not there (kešigten-dür is a dative, "equals of my guardsmen"). Now U29 "My guardsman is above the officers of the thousands who are outside", U30 likewise, U31 "The thousand-commanders outside, being equals of my guardsmen, on a level with them,".
12. U37 · i, n · moderate · "at sunset" is not in the form or the Ming (光有的行, "while it has light"). Now "while the sun gives light"; the note says dusk is only a guess.
13. U40, U41 · l, i, n · moderate · `kirüġe-dür` (last word of U40) was missing from U40's l and i and appeared in U41's l and i. Moved to U40 ("to-gathering-place" / "at the gathering place"); notes adjusted; U40 note now says that "with us" for the accusative bidan-i is a reading of the sense; U41 note says the ending -šü is as printed.
14. U44 · n · moderate · false label: instrumentals "-γ̇ar after a back vowel, -bar after a consonant-final stem", but josu and qaγ̇uli both end in a vowel. Replaced by "-γ̇ar on josu, -bar on qaγ̇uli; I do not explain the difference of form".
15. U45 · i, n · moderate · "behind the palace, in front of it" for qoinaγ̇un uridaγ̇un (Ming 從後, 從前, "from behind, from in front"); the first barižu was rendered as a finite "they are to seize him" while l has the converb. Now "a man going about the palace from behind, from in front, or crosswise, seizing him,"; the note records the repeated barižu.
16. U46 · i, n · moderate · note called in-ü "the back-vowel companion of an-u" (reversed: in-ü is the front-vowel form); i "spend the night" had no subject. Now "let the night guard, having seized him and passed the night, ask him in the morning for his words".
17. U47 · i, n, morph (word 333) · moderate · "the night guard and the turn are relieved" (kebteġül kešig, Ming 宿衞 班, kešig also "the guard" in the glossary) → "the night-guard shift"; daγ̇ulžu given a lemma of its own: now taγ̇ul- (printed daγ̇ul-, Ming 分付着 identical to taγ̇ulžu).
18. U49 · i · moderate · baiγsad (plural participle, Ming 立了的每) turned into "standing there" as a loose finite clause, "hold the door" for daružu egüden (Ming 壓着, "pressing"). Now "The night guards, lying round the palace at night, pressing on the door, those who have taken their stand,".
19. U50 · l, i, n, morph (word 362) · moderate · i added "take the people", l/i "drive off" for oγ̇orudqun (oγoru- "go off" + polite plural -dqun) as if sure; the Ming of čabčižu is 欲着 (not the glossary's 斬着), unmentioned. Now i "the night guard are to drive off the people who enter at night, smashing their heads and hewing at their shoulders until they fall", l "go-off (you all)"; the note says "drive off" is a guess, that the object is not known, and that 欲 is probably a slip; morph gloss says so.
20. U51, U52 · i, n · moderate · U51 had its own finite "let him speak" and U52 a second, but keleležü is a converb and only keleleġültügei is finite; "a man" for haran keleten (plural, "those having words"). Now U51 "If people with urgent words come at night, speaking to the night guard," U52 "…let them have it told"; l of U52 "let-be-spoken-through" → "let-be-made-to-speak"; U52 note records Ming 邊行 ("at the side") for ümerēče.
21. U56 · n · moderate · note cited Ming 敎行者 for jabutuγai; the packet has 行者︀ (敎 is the glossary's variant). Corrected; i "between the night guard" → "between the night guards".
22. U62 · i, n · moderate · "relying on his standing" supplied an object for itegeltü (Ming 倚仗, nothing named); the note's remark on 悅 now states the Ming reads "pleased" and probably stands for 晩; the note now says there is a full stop, not a question mark, so the question is uncertain.

#### Minor (21)
23. U1 · n · minor · -le- called "be"; now "act as" (as aqalažu in the glossary).
24. U2, U3 · n · minor · "Four near-identical units follow" (it is this unit and three more); "the second name here (Alchidai)" (no such thing).
25. U7, U34 · l (and U34 i) · minor · tuṅγarun is the converb of time (glossary "when proclaiming"); l now "proclaiming-when", U34 i "When proclaiming…".
26. U8 · l · minor · "to-own-own" → "own-to-his-own".
27. U10 · l · minor · "let-exchange" omitted the reciprocal -ldü- → "let-exchange-with-one-another".
28. U11 · l · minor · oγ̇araγsan "missing-ones" (plural) → "having-missed" (singular participle).
29. U18, U19 · i · minor · aldaltan "held at fault"/"penalized" → "liable to a penalty"; U18 "If you have not had it heard" (no "you") → "If they have not made it heard"; U19 note says the attachment of "by the rule of the decree" is open.
30. U22 · i, n · minor · "broken … report it" → "disturbed … tell me" (kündeġe- "stir", žiγa- "tell"); note says "breached" is a reading.
31. U28 · n · minor · note cited Ming 做的 (packet 做) and said §227 opens with the same formula (it has bolžu).
32. U32 · i · minor · ereġüleje is the hortative: "we shall hold … guilty" → "let us hold the thousand-commanders' man guilty" (Ming 千戶每的 plural).
33. U36 · i · minor · "each in his own place" had no source; now "going about by day, in each direction, each to his own post".
34. U39 · l, i, n · minor · saba (Ming 皿) "vessel" beside ajaγa "cup" (Ming 器) → "dish".
35. U48 · l, i, n · minor · l "saying said" for keġebe; i "likewise" for kü (Ming 也) → l "said", i "…hand over to the night guard, and go out", note says kü is left unrendered.
36. U55 · n · minor · "the upper part of the place where the guard stands" stated as fact; now "I read it spatially" (Ming 從上).
37. Words 57, 252, 292, 295 (U8, U36, U43) · morph · minor · separate "(i)" morph and plain -jen/-jan; recent parts (211–217) and the glossary keep it in -(i)jen/-(i)jan. Now two/three morphs per word.
38. Word 5 (U1) · morph · minor · plural given as -d against surface turγaγ̇ud-un; now -ud (as word 244).
39. Words 83, 104, 187, 191, 194, 152, 178, 221, 292, 380 · morph lemma · minor · plain γ where the glossary entries are doloγ̇an, qariγ̇u, sačaγ̇u, saγ̇urin, saγ̇uri; now written as the glossary has them.
40. Words 94, 290 · morph · minor · dative-locative given as -tür after back-vowel stems (nojad-tur, qor-tur) → -tur.
41. Word 254 (naran-u) · morph · minor · genitive lemma -un with surface -u → -u ("the -u form after a stem in n").
42. Words 268, 278, 293 · morph · minor · baγurči → baγ̇urči (glossary's baγ̇určin entry lists baγ̇urči; published parts).
43. Words 272, 339 · morph · minor · taγul- → taγ̇ul- (consistent with word 333).

Counts by severity: critical 0 · major 3 · moderate 19 · minor 21 (43 items; item 4 touches 17 units, 37, 39, 42, 43 several words).

### Findings refused
- Lemma "invention" flagged by the drafter (min-u → bi + -u; na-da, na-dāča → bi + -da / -dāča; bidan-dur / bidan-i → bida + -dur / -i): kept. They match the glossary's own entries (`bi` lists the stems na-, nama-, min-; `na-dāča` is already bi + -dāča; `bidan-dur` is bida + stem extension -n + -dur) and the practice of published 189–224-226 (bi + -u, bi + -dur, bida + -dur). The glossary's whole-token entries `min-u` and `na-da` remain the entries the reader's token lookup will find; the lemma column follows the later parts.
- qorčin as one morph although the glossary reads qor-či-n (uncertain): published parts use one morph; kept.
- kereldüġesü kept as kerel- + -ldü- (glossary head is kereldü-, same analysis in its text).
- turγaγ "day guard": an inference of the glossary (Ming 散班), followed; the note says so.
- U10 "nights" supplied after γurban: already said in the note; kept.
- U9 "should muster" (no modal in the form): the converb chain ends in an optative at U10, so a deontic reading is fair; kept.
- U17 "in every third turn" for γutaγ̇ar γutaγ̇ar: note already calls it my reading; kept.
- U38 "with us" for bidan-dur ("to us"): note gives "to us"; consistent with "in our presence" elsewhere only loosely, left as readable English.
- U33–U34 "Kešig" left unrendered in i: l has it and the note explains the doubled phrase.
- U35 qorčin note "qor + -či + the plural": glossary agrees (-n plural uncertain); kept.
- U41 / U26 -šü as converb or conditional on different words (kelečilešü, beriġedešü): both are tentative in the notes; kept.
- `ln` and `p` beyond the three `p: true` flags: supplied by the build.
- `about` / `titleEn`: checked against the units, no change.

### Remaining doubts
- U23/U24 josutan (rightly so vs. in the right): Ming 理有的每 follows 合處斬的 / 合打的, so "rightly" is the likelier reading, but the form alone does not decide.
- U43 meaning of the "return" (taγ̇araldutuγai, Ming 復) and U50 oγ̇orudqun / "drive off": both stems uncertain; i is a best reading.
- U60–U61: whether the man is taken together with his gear or only the gear is taken.
- U37 γaltaj-a ("while the sun gives light") and U40 kirüġe-dür (Ming 聚馬): unclear.
- U62 ker: question or "how"; žilda (Ming 悅 against 晩).
- U13–U15: berkešijen ažuγ̇u as "was finding it hard" and the conditional chain it finishes.
- New name for conventions.md: Eljigedei (Elžigedei); not yet in the house list.
- For the glossary pass: key `u` (needs "also genitive -u after a stem in n", naran-u), `kešig` (add "the night-guard shift" use at kebteġül kešig), `kirüġe`, `ekid`, `mürü` are new or need broadening; `saγ̇u-` / `saγu-` heads differ inside the glossary itself.

## Pass 2

Read: conventions.md, RUNBOOK §2, packet.md, units.json (after pass 1), gloss.json, novel-forms.json, known-forms.json, the shared glossary. gloss.json was checked entry by entry against the text, the morph lemmas and the Ming glosses (originals kept at `.../scratchpad/gloss227.orig.json`; script `.../scratchpad/gloss_p2.py`). Mechanical checks after the edits: every novel reader token of `t` (98) has a key, plus `saba-duri` (the reader's token of saba-dur(i)-jan; `jan`, `öġer-türi`, `mör-türi`, `saγ̇urin-duri`, `jen` are already in the glossary); no key is already in the glossary or unused; the 8 `__broaden__` entries each begin with the glossary's entry whole + " · "; every entry ends with its Ming gloss in `[ ]` (or, if broadened, carries it); Ming brackets agree with the packet (the three tokens with variant glosses now say so); `t` of all 63 units identical to pass 1; JSON valid; quote marks in `t`, `l`, `i` agree.

### Changes (unit/key · field · severity · what was wrong · what was done)

#### Moderate (6)
1. `ötökülekün-i` · gloss · moderate · invented Ming reading "those who are senior" (the Ming is 爲長的(每)行); lemma ötögü not marked as printed ötökü-. Rewritten with the real Ming and the printed form.
2. `oroqui` · gloss · moderate · muddled grammar ("-qu + -i … accusative-like ending of -qui"). Now participle -qui (the participle -qu with final -i; ending uncertain), "entering".
3. `žailažü` · gloss · moderate · wrong label "front-vowel form" on a back-vowel stem. Now "written -žü although the stem has back vowels" (as conventions, jadažü); head tied to the glossary's žaila-.
4. `ekid`, `baγ̇utala` · gloss + morph (U50, words ekid, baγ̇utala) · moderate · gloss heads disagreed with the glossary (eki "brain, uncertain", baγ̇u- "settle, halt"); morph kept ekid as one morph and baγu-. Gloss heads now eki + plural -d and baγ̇u- "come down, fall"; U50 morph changed to eki + -d and baγ̇u- to match.
5. `süitügei`, `šöjüġed` · gloss · moderate · "to give (rods)?" stated the context as the meaning of the stem, against the Ming 敎導 "instruct". Now "to instruct, discipline?" with the rods reading flagged as inferred.
6. `mököriġülkün` · gloss · moderate · -kün called a bare "participle"; the glossary (mököriġüldekün) has "future participle -kün". Aligned.

#### Minor (19)
7. `kešiġüd-ün`, `kešigtü`, `γadanadus` · gloss · minor · the entry's Ming covered only one of the occurrences' glosses (班每 的; 扈衞 有的 and 護衞; 在外的每). Variants added.
8. `alčidai`, `elžigedei` · gloss · minor · no reader-form of the name (Alchidai, Eljigedei). Added.
9. `mököriġülü-že`, `nišid-že` · gloss · minor · "(we)" / "(him)" pinned to the line. Generalised.
10. `beriġedešü` · gloss · minor · -šü as conditional unexplained; now says the usual conditional is -ġasu/-ġesü and the ending is as printed (Ming 呵).
11. `mudrγa` · gloss · minor · "a slip" asserted; now "probably".
12. `qariγ̇ultuγai` · gloss · minor · "-l- give back" pinned; now verb-maker, perhaps "cause to return" (Ming 敎囘).
13. `miṅγaloγ̇udai` · gloss · minor · -lo- beside -li- unexplained; now tied to miṅγaliγ̇ud.
14. `ereġüleje` · gloss · minor · stem differs from the glossary's ereġül- (ereġülüžü); cross-referred.
15. `jabudal` · gloss · minor · "doing" invented. Removed.
16. `γaltaj-a` · gloss · minor · γal given as "fire, light" as if the glossary's; now fire (Ming 光 "light"), "in the light, while it has light".
17. `kirüġe-dür` · gloss · minor · "gathering" stated as a meaning; now a guess, "gathering place?".
18. `taγ̇araldutuγai` · gloss · minor · -ldu- "each to the other"; now reciprocal / joint.
19. `ketügelčen` · gloss · minor · cross-reference to ketül- (ketülžü) added.
20. `šiṅgegsen-ü` · gloss · minor · "of the having set" → "of (the sun) having set".
21. `degeġün` · gloss · minor · cross-reference deġere added.
22. `emüšügsen` · gloss · minor · printed š noted.

Counts by severity: critical 0 · major 0 · moderate 6 · minor 16 (22 items).

### Findings refused
- Full-token keys such as `naran-u`, `kebteġül-eče`, `kešiġüd-ün` (instead of splitting at the hyphen): kept; the glossary does the same (turγaγ̇ud-un, nojad-ača style keys) and known-forms uses them.
- `miṅγaliγ̇ud` / `miṅγaloγ̇udai` analysis (-li-/-lo-, -ai as genitive): tentative in the entries; no better analysis from the sources.
- `ger-ün` "house" in `l`, "tent" in `i` (U52): both are the glossary's readings of ger; left.
- `kelečilešü` stem keleči- + -le-: kept, entry says stem tentative.
- `josutan` "possessive plural -tan" (not "-tu + -n"): agrees with josutan-i in the glossary.
- `kešig` broaden entry mixes three senses of kešig: legitimate, each tagged with its Ming.

### Remaining doubts
- `taγ̇araldutuγai` (U43): Ming 復 "return"; the stem taγara- is not in the glossary; a stem meaning "part, go separate ways" would also suit "each to his own". Left as uncertain.
- `ekid` as eki + -d, `dalbaru`, `ketügelčen`, `jabudal`, `kirüġe`: all stems or forms guessed from the Ming alone.
- Pass 1 doubts stand: U23/U24 "rightly so", U43, U50 "drive off", U60–U61, U37, U62, U13–U15.
