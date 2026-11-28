# popol-vuh-021: review

## Pass 1

I read conventions.md, runbook.md (Reviewer), the Run 3 RUNBOOK §2 "Reviewer", packet.md, establish-log.md, known-forms.json, novel-forms.json, drafter-notes.md, units.json (47 units), the published 001–020 (mainly 002, 010, 012, 017–020) and popol-vuh-glossary.json. Brasseur 1861 (OCR lines 26540–27000) was used only to check meaning. No modern translation was opened or recalled. gloss.json was not touched.

I made the edits with a script (`json.load` → exact-substring replacements, each asserted unique → `json.dump(ensure_ascii=False, indent=1)`). No `t` changed (asserted). The script also asserted that every `mt` has exactly as many entries as WORD_RE finds tokens. units_src.py has not been updated to match.

### Checks run
- **mt.** By script, I compared every mt with the mt of the same manuscript form in the published 001–020. The only value not published for its form is xecah → xeqaj (U26), which is right: 'they went down', and the note separates it from the 'foot of the sky' word. Where a form has two published values (ca qa/ka, chi chi/chik/chi', cah qaj/kaj, xcah xqaj/xkaj, cam kam/k'am, cuꜭ kuk'/quk', oc oq/ok, que ke/qe, quech kech/qech, quih kij/q'ij, cab q'ab'/kab', xac xak/xaq), each choice fits its sense, except U5 que (change 1). I checked the new forms against the letter rule by hand. Marks are supplied only for certain words: etz'anem (as 017), atz'iyaq, k'astaj and k'utun (as published), q'ijin (written with the tresillo). Uncertain words (chojim, choj, jonel, kucha, tix, kajim, chaom, kua and the five dance names) are respelled by the letters. Qui ia → Ki ya follows the published ia = ya; see refused 3.
- **Establishment log.** Every doubtful reading and every letter decided against Brasseur is flagged in a note: honel; the blot after chicop; nicvachi-nel; caquinuc; the blotted mixoh; ch-oc; the q-shaped ꜭux; tacoh; Vue; catoc against gat-oc; xchi|cuchah; Ma vꜩ lo; ꜭaztah against caztah; cahim; cuchiqueic; cutunizah/cutun; achbilai que; ca quiy; queta-am; chivi/tana; the f-like t; ꜫihin; aꜩiyac/aꜩiiac; the marginal ?; pu quih and cul qui cu; Chiꜩic/Chitic; the garbled Brasseur at libah; v xenacahic; the q-shaped cuz (twice); xqhao; chi cah; quiiꜩel; gocam curaih naypu; ca cah; cax/cacrail; mach cay. README 5b: none.
- **House renderings.** Vꜩ bala "Very well" (U18); vbac vvach "eyes", with `l` "its-bone our-face" (U42); ahau "lord"; chohim abah "heated stone" (as 018); chacatah- "brought low" (as 019); the boys; Huncame, Vucub Came. All are followed.
- **Couplets.** Couplets stay couplets in `i`: the heading (U1); maui xe camic / maui xe chacatahic (U2); chuti huyub, nima huyub (U14); tacal qui yuyub, tacal qui xulcab (U23); que ca maihah tah, que ca cayih ta puch (U38). chuvi ra, chuvi cax (U46) had been merged; see change 9.
- **Cross-references in notes** were checked against the published text: nicvachinel 002/009; halahoh 002; racan ha 007 and a 'water' 010; hupulic 007; cuz 008; achbilai and the caztah … cuꜭ line 010; quia 010/012; caxcol rail 014; hoc and quixbic 017; chohim abah, mich and chacbal 018; chaco 019; hebel and ꜩaꜩ chi 020. U2's caxcol rail is cited as 014, which is right. U13's "in 017 'cleared'" matches the glossary.
- **Remembered English.** I found none. The phrasings that are not built from the K'iche' come from Brasseur, and the notes say so (fish-men, the sweet drink, the eyes in mockery).

### Changes (unit · field · severity · what was wrong · what was done)
1. **U5 · mt, l, n · minor.** The note called que "the plural absolutive", which it cannot be after a noun. It also gave 'them' as the only reading by the letters, while `i` had 'us'. Ximénez's qu writes q as well as k. The glossary already has "qe — us (the object after an agent noun, camol qe 'taker of us')" from 010, and Brasseur's ke (his k = plain q) is qe. mt ke → qe; `l` "of-them(?)" → "of-us"; the note was rewritten to give qe 'us' after an instrument noun, with 010's camol que, Brasseur, the person of chi ca ꜭux, and the ke 'them' alternative. `i` ("their means of killing us (?)") is kept. *This decides the drafter's open point: 'us'.*
2. **U7 · l, i, n · minor.** The note gave quix ul as "'they come to you': c- + ix 'you (pl.)' + ul". But ix is the subject of the intransitive ul: 'you come'. With ꜩonobex the phrase is 'you come to be asked'. `l` "If you they-come to-ask(?)" → "If you-come to-be-asked(?)". `i` "if they come to ask you about our death" → "if you come to be questioned (?) about our death". The note's label was corrected.
3. **U4 · i · minor.** `l` has rumal ri … twice ('about our death …, about the not-yet-having-died'), but `i` turned the second into "since we have not yet died". That made a cause out of a second topic of the question. Changed to "and about how we have not yet died, not yet been brought low".
4. **U30 · i, n · minor.** *(Drafter's open point: hala.)* I keep the drafter's reading, hala as the stem of halahoh 'different' (002). Brasseur's 'peu de chose' is given in the note. But `i` "all kinds (?) of things" added an 'all' that `l` ("different(?)") does not have. The note also misquoted 002's halahoh as 'each its own way', which is 002's `i`; 002's note has 'different, of many kinds'. The repeated xa 'only' before the dances was dropped in `i`. `i` now reads "they did different things (?): they only danced the Puhuy dance, the Cux dance, only the Yboy; they only danced the Xtzul, only the Chitzic, as well." The note now quotes 002 correctly and says that the English keeps xa.
5. **U31 · n · minor.** *(Drafter's open point: Qui ia.)* The reading quia 'many' stands. But the note gave a morphology, "ꜭiy 'many' + -a", that no published part or note supports. 010 and 012 have quia 'many' (inferred, toggle kia). The note now cites them, and says that the toggle respells the two words as written, ia as the published ia (ya).
6. **U44 · n · minor.** *(Drafter's open point: cuꜭ 'with us' against 010's 'with them'.)* The difference is justified, and mt quk' is kept. In 010 the faces are ca vach 'our faces', so the other party is 'them'. Here they are qui vach 'their faces', the fellow poor men's, so the other party is the speakers, 'us'. The c writes either k or q. The note said only that "the letters also allow 'with them', as 010". It now gives the person contrast as the reason. 010 does not need to change.
7. **U39 · l · minor.** `l` "was-spoken" disagreed with the note, which has xꜭhao 'spoke it' (ꜭha + -o, active), and with `i` "gave them". Changed to "spoke-it".
8. **U29 · n · style.** The note said "the modern atz'yaq, with the tz' supplied", but mt is atz'iyaq, which keeps Ximénez's i. The note now says that the toggle gives atz'iyaq, with the tz' supplied and the other letters kept.
9. **U46 · i · style.** The couplet chuvi ra, chuvi cax had been merged into "over the harm and the pain". Changed to "over the harm, over the pain".
10. **U12 · n · style.** que was labelled "ca- ongoing + e". The prefix before the vowel is c- (as the note's own quecha in U11 says). Changed to "c- ongoing + e 'they'".

### Findings refused
1. **U14 `l` "when it-is-shown" for ta chi cutunizah.** The note gives the morphology -iz 'make' + -ah, which is active, so 'make appear'. `i` has active "you will bring out". But no person prefix is written, so a passive-like 'when it is made to appear' is not excluded. `i` and the note agree, and `l` marks no person, so I kept it.
2. **U44 cam = kam by the letters, although `l` takes it as 'take'.** The word is a guess ('take part (?)', after Brasseur's qam). By the rule, an uncertain word is respelled and nothing is restored. The note says so. Kept.
3. **U31 ia → ya, though the sense here is not 'give'.** The published ia is ya (i for y) in every case. Keeping the same form's toggle is the rule, and the note now says so (change 5). The alternative, ia letter for letter, would be the first such value. Kept.
4. **U23 `i` drops chi (= chic) in "Then all Xibalba rejoiced".** "Then" carries cut, and an "again" would suggest an earlier rejoicing in this scene. Not changed.
5. **U20 `i` "over it" in "fly (?) four times over it".** It is not in the K'iche'. It comes from Brasseur's 'volons-y', it is attached to a marked guess, and the scene (the oven) requires it. Kept.
6. **U7 catoc 'be burned' against Brasseur's ꜫat- 'be condemned'.** The letters allow either, since Ximénez leaves ejectives unmarked. The oven setting favours 'burn', and the note gives both. Kept.
7. **U25 "Just as the boys had said".** This makes xavi xare explicit, as Brasseur's '(qu'ils l'avaient annoncé)' does. The sense is not changed. Kept.

### Drafter's open questions (decisions)
- **que cumal (U5):** 'us', with mt qe (change 1).
- **cuꜭ (U44):** 'with us', mt quk'. The difference from 010's 'with them' is justified by the person of the faces, and the note now says so (change 6). 010 is not changed.
- **Qui ia (U31):** quia 'many' (inferred, as 010/012). Toggle Ki ya, as the published ia (change 5).
- **hala (U30):** 'different (?)', from halahoh. Brasseur's 'peu de chose' is in the note, and xa 'only' is now kept in `i` (change 4).

### Counts (pass 1)
- major: 0
- minor: 7
- style: 3
- total changes: 10 (15 field edits)
- refused: 7
