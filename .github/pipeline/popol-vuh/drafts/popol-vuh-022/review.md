# popol-vuh-022: review

## Pass 1

I read conventions.md, runbook.md (Reviewer), the Run 3 RUNBOOK §2 "Reviewer", packet.md (pinned text and establishment log), drafter-notes.md, units.json (48 units), the published 001–021 (mainly 001, 003, 005, 007, 010, 012, 014–021), popol-vuh-glossary.json and 021's review.md. Brasseur 1861 (OCR lines 26994–27360) was used only to check meaning. I looked at page image i0070 (cropped with Pillow) for U20 `xecahic`. No modern translation was opened or recalled.

I made the edits with a script (`json.load` → exact-substring replacements, each asserted unique → `json.dump(ensure_ascii=False, indent=1)`). The script asserted that no `t` and no `mt` changed, and that every `mt` still has exactly as many entries as WORD_RE finds tokens. units_src.py has not been updated to match.

### Checks run
- **mt.** By script, I compared every mt with all published mt values of the same manuscript form in 001–021. Only two values differ from every published value: xquetamah → xqetamaj (U5) and quil → qil (U28). Both are justified by a change of person ('we'), and both notes say so. Where a form has more than one published value (ca, chi, cah, quib, que, cuꜭ, quih, vcab, cam, chique, oc, ha, cu, vi, xe), each choice fits its sense: chiqe 'to us' (U35) has a published precedent; cam kam 'death' (U37); vcab uq'ab' as 008. huzu stays jusuk, as in every published case, even though the c is not written (glossary: the c is shared). I checked the 50-odd new forms against the letter rule by hand. Marks are supplied only for certain words: kamaq' (as ramaq'), atz'iaq (as 021), ch'utik (chuti), tz'i' (ꜩi 'dog'), k'astaj/k'asta/k'astai (cuatrillo written), poq'oj (tresillo written), aq'anoq (published). Uncertain words (mocho, xule, quemelah, luc, pach, mayo, kij, uma, pulik, sakb'isala, xekajik, kab'ar, xperepoxik, xkole, xcheke, tzalik, xaraxoj, chub'ik, xukamib'ej, xelaj, b'alij, xolob'achan, jukaly, b'eyox, elajoq) are respelled by the letters, with nothing restored.
- **README 5b.** U13's note opens "The manuscript has xquihquiba, a misprint for xqui tiquiba, corrected here.", which is the required form and matches 017/020.
- **Establishment log.** Every item is mentioned in its unit's note, as the drafter's list says. I checked each one: qui pach quib (U1), mayo quih (U2), chiaꜩiac (U2), vachibal (U2), camac (U3), xeughaxic (U4), the mark on quetaon (U4), naquichivah yvahil (U7), mixxobic (U9), chixah and the marginal 1 (U10), coh caytah … vma (U11), quixbetacoc (U12), xquihquiba (U13), ꜩy (U16), caztah/ꜭaztah (U16–17), xꜭaztai (U17), zacbizala (U18), xcuꜩinizah (U21), poꜫoh (U25), the struck na, ixahoh and chicu (U28), Xhunahpu (U29, U36), xcotix and ꜩalic (U31), cava-|lihoc (U32), xecha and the words missing from Brasseur (U35–36), chique (U35), quicotirizai and ivaliqahol (U38), qui vholom (U39), quelic and chica-|can (U41), Tocob (U44), quiz (U45), culun and hucaly (U46), elahoc (U47), quechacatahic (U48).
- **House renderings.** Vꜩ bala "Very well" (U6, U24, U28, U37); ahau / at ahau "lord"; meba "poor men"; xahoh / xahol "the dance / the dancers"; the dance names kept; Huncame, Vucub Came. chacatah- "brought low" (014, 019, 020) was not followed in U48 (change 10).
- **Cross-references in notes** checked against the published text: 018 Apa quix ix pe vi; 007 ca ca xibih quib and tocob nu vach; 016 poroh; 012 coloba; 006 acanoc; 008 racan vcab and tubul ('giving way, tottering', glossary); 007 xeculun; 019 zanic; 003 cahizabal, cacan, culu/rico; 012 xe quiz; 020 xcotix, ꜩalic, halvachibal; 019 Quehe cut qui chacatahic; 015 -ou- ('the ending that names the doers', the published label, which is right for the agent-focus que banouic after are); 021 catic and the dance glosses. The cabichal citation (U41) was wrong (change 7).
- **Couplets.** Kept in `i`: qui chuch, qui cahau (U3, U5); the two xꜩonox lines (U3); Mi xibih ivib, mix xobic (U9); the three chi-commands (U10); qui bix, qui xahoh (U13); chi camizah … chi puzu (U23); racan vcab (U30); v rainic, v malinic (U35); maui xuculu, ma pu xurico (U43); pa nima zivan / pa nima xolobachan (U45); xe ul elahoc, xe ul pu ococ (U47); xa maihabal, xa pu qui halvachibal (U48, restored by change 10).
- **Remembered English.** None found. "Have pity on me" is 007's; "Get up!" is built from valih; the bowing words, the drunk lords, 'vassals' and the ants come from Brasseur and are marked.

### Changes (unit · field · severity · what was wrong · what was done)
1. **U41 · l, i, n · major.** qui cabichal was rendered 'their companions (?)' and called "the obscure pair-word of 005". It is published as 'the two of them' in 014, 020 and 021 (glossary second sense), and Brasseur's 'deux à deux' agrees. `l` "their-companions(?)" → "the-two-of-them"; `i` "and their companions (?) split open too (?)" → "the two of them split open too (?)"; the note now cites 014/020/021. Also kept xa 'only' in `i` ("it was done only to bring them low") and in the note.
2. **U11 · l, n · minor.** `l` had "it-wants" and the note "'our heart wants this'", but cah is 'we want' (c- + ah), mt qaj, as the unit before. 'It wants' would be rah. `l` → "we-want"; the note says so. `i` keeps Brasseur's sense for the whole line, marked (?).
3. **U43 · l, i, n · minor.** *(Open question 5.)* `l` and `i` had 'they met him, they found him', but xu- is x- + v-, a single doer. `l` → "not he-met-him(?), not also he-found-him(?)"; `i` → "no one had met him, no one had found him (?)", which keeps Brasseur's sense with an unnamed single doer; the note says this.
4. **U46 · l, n · minor.** vla was glossed 'came'. The glossary has it only as 'hither' (with verbs of coming), mt ula. `l` "came" → "hither"; the note now takes hucaly as the verb of coming (a guess) and vla as 'hither'.
5. **U16 · i, n · minor.** `i` had "Very well" for Ve, the house rendering of Vꜩ bala, against `l` "Yes" and the published "Yes" for “Ve,” in 006, 012, 016, 017 and 020. `i` → "Yes"; the note no longer calls this a new use of 'if' (the glossary already has 'yes').
6. **U9 · n · minor.** The note said "In earlier parts mix was mi + x-, 'just now'", but 010, 014 and 015 have Mi xbizonic 'do not grieve', with Brasseur's m'yx division. The note now cites them.
7. **U20 · l, n · minor.** *(Open question 1.)* `l` "they-xecahic(?)" did not show the reading `i` takes. → "they-were-burned(?)". The note now reports the page check (below).
8. **U7 · n · minor.** chivah was analysed "ch- + i- 'you (pl.)' + ah", leaving the v unexplained. → "ch- + iv- 'you (pl.)' (the form before a vowel) + ah".
9. **about · style.** "defeated" → "brought low" (house), and "children and vassals" → "children and sons" (the drafter's own proposed rendering avoids 'vassals' in English).
10. **U48 · i · minor.** `i` had "were defeated" (Brasseur's 'vaincus') against the house "brought low" for chacatah- (014, 019, 020), and merged the xa … xa pu pair into "by wonders alone, and by changing their own form". → "This is how the lords of Xibalba were brought low: only by wonders, only by changing their own form, did the boys do it."
11. **U1 · i · style.** "bowed themselves low" and "bent themselves down" render guesses (quemelah, luc) without the (?) that `l` and the note give them. Marked.
12. **U40 · n · style.** "the dancers have revived … each other": only Hunahpu was revived, and the house was restored, not revived. → "have brought back the dog, the house, the man and Hunahpu".

### Findings refused
1. **U34 que banouic "-ou-, the ending that names the doers".** This is the published label (015, glossary), and it fits the agent-focus after are ('it is they who do it'). Kept.
2. **U32 Ca valih oc "c- + a- 'you'".** One would expect cat for 'you' with an intransitive verb, but the glossary already has ka = k- + a- 'you' (ma ka jisaj). Kept.
3. **U29 `i` "sacrificed each other" against `l` "themselves".** quib covers both, Brasseur has 'l'un par l'autre', and 021.33 has the same. Kept.
4. **U21 huzu mt jusuk although no final c is written.** Every published huzu is jusuk, and the glossary explains the shared c. The same form keeps the same mt. Kept.
5. **U22 `i` "as the two went on dancing, the lords rejoiced greatly".** The pair que xahouic / nim que quicotic is rendered as two clauses with their own verbs; who is the subject is open (open question 4), and the note says so. Kept.
6. **U18 chu "'it', ch- + v-".** Loose (ch- is the mood prefix, v- the person), but not wrong. Kept.
7. **The drafter's `__broaden__` list.** Ve 'yes' and mix/mi 'do not' are already in the glossary, so the glosser needs no broadening for them (noted for pass 2).

### Drafter's open questions (decisions)
1. **xecahic (U20).** I looked at i0070. The letter after `xeca` is a tall stroke drawn as a loop, with a shoulder running into the next letter. It has the same shape as the h-like t of `ta` that opens the line above (`ta xquiporoh cut`), and also as the h of `poroh`. The hand does not separate the two letters here. The sense allows only 'they were not burned' (Brasseur x-e qatic; 021's xe catic 'they were burned'), so the letter may be t. The note now says this and calls it a doubtful reading. `t` is pinned and was not changed. mt stays xekajik by the letters. *For the orchestrator:* this is a candidate README 5b correction (xecatic), like xquihquiba. It would need a re-pin, which is not the reviewer's job. It may be worth a line in QUESTIONS.md.
2. **Mi / mix (U9).** Agreed: mi is the prohibitive, and mix is mi + ix. The published 010/014/015 already read it so, and the glossary already has both senses, so there is no broadening.
3. **Hunal tah (U36).** Keep 'one at a time (?)', with the note's alternative 'in the same way'. It is hun + -al beside huhunal (U30). Nothing in the line decides it.
4. **Who dances and who rejoices (U22, U33).** Keep as drafted, after Brasseur. The notes say that the grammar does not decide.
5. **maui xuculu, ma pu xurico (U43).** xu- is a single doer, so 'they' is wrong. Decided as change 3: 'no one had met him, no one had found him (?)'.
6. **xcheque chuvach ꜩalic, que cabar (U31).** Keep, as a guess after Brasseur's word-for-word note. mt kab'ar by the letters is right: the manuscript has plain c, and the word is uncertain.
7. **Guesses after Brasseur (¶1, ¶14, ¶16).** All are marked, and their notes say they are guesses. Only U1 `i` lacked marks (change 11).
8. **chi before v vach.** Keep mt chi, unrendered, as 021.33.

### Proposed house renderings (drafter-notes.md): view
I endorse all ten as proposed: puz/puzu 'sacrifice'; ꜭaztah/caztah v vach 'come back to life' (mt k'astaj for both spellings); ꜩy 'dog' (mt tz'i', as ꜩi); yvahil 'your payment'; maihah/maiha 'marvel at' (mt maijaj/maija); qui vholom ahau 'their chief lord'; al, ꜭahol 'children and sons' (Brasseur's 'vassals' only in notes); halvachibal quib 'changing their own form'; Xhunahpu → Hunahpu in `i` (the note gives the x-); at ahau 'lord'. One condition: the table should also record **qui cabichal 'the two of them'** (already published in 014/020/021, see change 1). It should also repeat that **chacatah-** is 'brought low', never 'defeated' (change 10).

### Counts (pass 1)
- major: 1
- minor: 8
- style: 3
- total changes: 12 (21 field edits, counting the about's 2)
- refused: 7

## Pass 2

I checked all 60 novel entries and the 8 `__broaden__` entries in gloss.json (written before pass 1) against the current units.json (mt, `l`/`i`/`n` after the pass-1 changes), novel-forms.json and popol-vuh-glossary.json, by script and by hand. I edited gloss.json by script (load, asserted replacements, `json.dump(ensure_ascii=False, indent=1)`). After the edits the script asserted two things: every entry's modern form equals an mt the text uses for that token (case ignored), and every broadening begins with the published entry copied whole plus " · ". I then re-read units.json end to end. Units changed in pass 2: none. No `t` or `mt` changed.

### Checks run
- **Keys.** All 60 novel-forms.json keys are present. No entry is extra, and none is already in the glossary.
- **Modern forms.** Every one equals the mt (hunal's junal is the lowercased Junal of a sentence start, the glossary's practice).
- **Broadening prefixes.** All 8 are exact. Their new readings agree with the units: xul 'bow down', tubul 'heaped up', quil qil, xquetamah xqetamaj, cam 'death', xcotix 'cut out', ꜩalic, coloba.
- **Broadenings needed after pass 1.** cah 'we want' (qaj), vla 'hither', qui cabichal 'the two of them', xu (x- + u-), chique 'to us', Ve 'yes', and mi/mix 'do not' are already covered by the published entries, so none is added. xuculu, quih, rumal and tac were not covered (changes 9–12).
- **Other known forms** used in this part were checked against their glossary senses: na 'feel' (xu na rib), coh, ca, chi, que 'them', ya, cacan, zachic, huzu, ive, ahilan, raih, nao, quiz, banouic, xahouic, xꜭha/xecha, bala, tah, la, e, chu. All are covered.

### Changes (item · severity · what was wrong · what was done)
1. **quemelah · minor.** The entry had invented morphology, "k- 'they' + root + -aj (?)". The 'they' is the separate xqui, and nothing shows a prefix inside the word. Removed; the entry now says it is respelled by the letters.
2. **chivah · minor.** "ch- + i- 'you (pl.)'" left the w unexplained. → "ch- + iw- 'you (pl.)' (the form before a vowel) + aj" (as pass-1 change 8 in U7).
3. **xꜭaztah · minor.** The second sense, "with the ergative xqui- 'they' … revived (him)", is wrong for this form. Every xꜭaztah in the part is intransitive (U18, U27, U33, U40), and the transitive use is xqui ꜭaztah, the separate token ꜭaztah (U42). Replaced with the example xk'astaj u wach 'he (it) came back to life'.
4. **xecahic · minor.** The entry put "(not)" into the word's sense (the negation is maui) and gave "(?)" for what the unit marks as inferred. Rewritten. It now gives the letters' reading (xe + kaj 'go down' + -ik), the doubtful t (xecatic, the katik of 021, Brasseur), and the page check of pass 1.
5. **xurico · minor.** The entry said "here read 'was found'", which pass 1 changed to 'no one had found him' with a single unnamed doer. Rewritten to match U43, with the morphology x- + u- + riq + -o.
6. **hucaly · minor.** The entry glossed it as "ants". The ants are zanic. The units (after pass 1, U46) take hucaly as the verb of the ants' coming. Rewritten: "(guess) came upon, of the ants".
7. **huyubal · style.** The entry was pinned to 'their' ("qui- 'their' before it"). Made general, with the example.
8. **xucamibeh · style.** The entry said "he was put to death" against its own active morphology (u- 'he'). Changed to "(guess) put to death", with the morphology unchanged.
9. **__broaden__ xuculu · minor (added).** The glossary has only "unknown word" (002's exclamation). Here (U43) it is x- + u- + kul 'meet' + -u, the culu of 003, 'met him'. Added, with the U43 reading.
10. **__broaden__ quih · minor (added).** The glossary's 'juice', 'sun/day' and 'day' senses do not cover chi mayo quih (U2), which is unclear. Added as unclear, after Brasseur (guess).
11. **__broaden__ rumal · style (added).** U12 takes rumal as 'after that' (inferred, Brasseur 'après cela'), which the glossary's 'by, because of' does not cover. Added.
12. **__broaden__ tac · style (added).** U12's unrendered tac after the verb is neither the plural marker nor 'send'. Added as an unclear particle.

### Refused
1. **Glossing Ve, mi and mix as broadenings,** which the drafter's list had asked for. They are already in the glossary (pass 1, refused 7).
2. **cabichal, cah, vla, xu, chique: no new broadening.** The published senses ('the two of them', 'we want', 'hither', x- + u-, 'to us') already cover the pass-1 readings.
3. **ꜩy keeps "(003, 004)".** This cites where the published form is, not the line it glosses here. Kept.
4. **The other entries were left as written:** mocho, xule, luc, pach, mayo, aꜩiac, vachibal, camac, quetaon, chutic, yvahil, xahon, vochoch, ivetaam, vma, pulic, cayel, ꜩy, xꜭaztai, zacbizala, pulinac, xcuꜩinizah, quicotic, poꜫoh, maiha, xꜭazta, xpuz, xperepoxic, xcole, aponoc, xcheque, cabar, xahouilabic, valih, rainic, malinic, hunal, quicotirizai, ival, xchap, quelic, xaraxoh, chubic, xaraxoxinac, xelah, cal, balih, xolobachan, culun, beyox, elahoc, ococ, and the 8 submitted broadenings. In each one the mt, sense, (?)/inferred/guess mark and morphology agree with the current units.

### Re-read of units.json
I found nothing further. In particular I checked: libah chi cut keeps mt chi while Xe vꜭhax chi cut / Caminac chi cut have chik, as the drafter decided with 019/021; U12 "After that" (inferred, noted); U38 couplet ival i ꜭahol kept; U47 couplet kept.

### Counts (pass 2)
- major: 0
- minor: 8 (6 entry corrections + 2 added broadenings)
- style: 4
- total changes: 12 (8 entries rewritten, 4 broadenings added, 0 units changed)
- refused: 4

### Counts (both passes)
- major: 1
- minor: 16
- style: 7
- total changes: 24
- refused: 11
