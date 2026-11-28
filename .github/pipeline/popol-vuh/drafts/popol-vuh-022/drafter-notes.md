# popol-vuh-022: drafter's notes

There are 48 units for 16 paragraphs (714 words). `cut.py` and `make_units.py` are unchanged. `cut.json` has 85 pieces.
`groups.py` merges consecutive pieces within a paragraph, and `units_src.py` holds mt / l / i / n. `make_units.py` takes `t`
only from cut.json, so no `t` was retyped. It prints:
`OK: 48 units, 16 paragraphs, 714 words, longest 31 (U28); paragraph starts at U1, 3, 6, 13, 16, 19, 22, 24, 28, 29, 35, 37, 39, 41, 43, 45`.

Grouping: each question is kept with its answer: U4 (Apa quix pe vi? / Maba quetaon), U7 (naqui chivah? / Yvahil chi ca
yao), U16 (the dog order + “Ve”), and U28 (the lords' request + “Vꜩ bala, at ahau”). U36's answer is in the next
paragraph (U37), so it could not go in the same unit. The couplets and the set of three in U1, the three chi-commands
(U10) and the elahoc / ococ couplet (U47) are each kept whole.

## Checks run
- make_units.py OK (tiling, paragraph starts, one mt per WORD_RE token, the JSON loads).
- I compared every mt by script with every mt of the same manuscript form in published 001–021 (case ignored).
  **Two forms differ from all their published values**, both for a change of person:
  - **xquetamah → xqetamaj** (U5) 'we knew'. The published xketamaj (021) is 'they knew'. Here the orphans speak of
    their own parents (ca chuch, ca cahau). The note says so.
  - **quil → qil** (U28) 'let us see'. The published value is kil 'they see / hold back'. Here chi quil tah is the lords'
    'let us see it'. The note says so.
- **Forms with more than one published value, and the value chosen here by sense:** ca ka (ongoing, U5, U8, U11, U32,
  U34; Ca valih oc = c- + a- 'you'), otherwise qa 'we/our'. cah qaj 'we want' (U8, U11), as in 021. quib qib'
  'ourselves' in ca ca xibih quib (U8), as 007's same phrase. chi chik where its c is shared with a following cut/cu
  (U23, U26, U28, U40), as published. libah chi cut keeps chi, as in 019 and 021. chi before v vach / qui vach is
  kept chi (U16, U17, U27, U40, U42), as 021.33 has it. vcab uq'ab' 'his arms' (U30, racan vcab, as 008). chique chiqe
  'to us (?)' in U35 only. chike elsewhere. cam kam 'death' (U37).
- **New forms (no published mt)** are respelled letter by letter, with nothing restored, except where the word is
  certain:
  - camac → kamaq' (amac, as ramac → ramaq' in 001).
  - aꜩiac → atz'iaq (as 021's atz'iyaq / atz'iiaq; the manuscript's vowels are kept).
  - chutic → ch'utik (the published chuti → ch'uti'; the ending follows the letters).
  - ꜩy → tz'i' (the published ꜩi 'dog').
  - xꜭaztah / xꜭazta / xꜭaztai → xk'astaj / xk'asta / xk'astai (the cuatrillo is written; the endings follow the letters).
  - poꜫoh → poq'oj (the tresillo is written).
  - For the other new forms the toggle only respells qu/c → k/q, v → u/w, h → j, b → b', z → s. Where c/qu has to be
    k or q, the choice follows the sense: quetaon qetaon 'we', chique chiqe, quil qil. cabar is kab'ar by the letters,
    not Brasseur's q'ab'ar, because the manuscript has plain c. xecahic is xekajik by the letters (see question 1).
- README 5b: U13's note opens "The manuscript has xquihquiba, a misprint for xqui tiquiba, corrected here."
- Every item in the establishment log is mentioned in its unit's note. pach and qui pach quib, which Brasseur omits: U1.
  mayo quih: U2. aꜩiac: U2. vachibal and the garbled Brasseur: U2. camac with plain c: U3. xeughaxic: U4. The mark on
  quetaon: U4. naqui chivah? Yvahil, its division and the y: U7. mixxobic: U9. chixah: U10. The marginal 1: U10.
  coh cay tah … vma: U11. quixbetacoc: U12. xquihquiba: U13. ꜩy: U16. caztah against ꜭaztah: U16 and U17. The ending of
  xꜭaztai: U17. zacbizala: U18. xcuꜩinizah with plain c: U21. poꜫoh: U25. The struck na: U28. ri i xahoh: U28.
  xeꜭha chi cu: U28. Xhunahpu: U29 and U36. xcotix: U31. The looped ꜩ of ꜩalic: U31. Ca valih oc: U32. xecha with
  plain ch, and the words missing from Brasseur: U35 and U36. chique: U35. quicotirizai: U38. ivaliqahol: U38.
  qui vholom: U39. quelic: U41. chica-|can: U41. Tocob with plain c: U44. The z of quiz: U45. ta xe culun cut: U46.
  hucaly: U46. elahoc: U47. quechacatahic: U48.

## Open questions for the reviewer
1. **xecahic (U20)**. The log prints it without comment. Brasseur's x-e qatic 'they were (not) burned' is what the
   sense needs. As written, xe cah 'they went down' does not fit. The h may be Ximénez's h-like t (the same hand as the
   5b case xquihquiba in ¶4), and the page should be checked. If it is a t, this is another 5b correction (xecatic).
   As drafted: printed as the log has it, English follows Brasseur, and the toggle is by the letters (xekajik).
2. **Mi / mix 'do not' (U9)**. I read Mi as the prohibitive and mix as mi + ix 'you (pl.)', following Brasseur's m yx.
   Published glossary entries for mi and mix are 'just now' + x-. The glosser should broaden both.
3. **Hunal tah coh i puzu (U36)**. I gave 'one at a time (?)'. 'In the same way (?)' is also possible. Brasseur does not
   have this line.
4. **Who dances and who rejoices** in U22 (que xahouic, nim que quicotic) and U33 (Nim que quicotic). The grammar does
   not say. I followed Brasseur.
5. **maui xuculu, ma pu xurico (U43)**. The prefix xu- would be 'he met / found it'. I followed Brasseur's 'he had not
   been found or taken' and gave 'they had not met him, they had not found him (?)'. This sense needs checking.
6. **xcheque chuvach ꜩalic, que cabar (U31)**. This line is not understood. The English follows Brasseur's note. ꜩalic
   is the 020 word ('grasses (?)' there).
7. **Guesses after Brasseur in ¶1, ¶14 and ¶16**: mocho, xule, quemelah, luc, pach, mayo quih (U1–U2); xaraxoh, chubic,
   xaraxoxinac, cabichal (U41); xucamibeh (U42); balih, xolobachan, culun, hucaly, beyox, elahoc (U45–U47). All are
   marked (?) and the notes say they are guesses.
8. **chi before v vach** after ꜭaztah (U16, U17, U27, U40, U42). It is either chic 'again' or chi 'at'. I kept mt chi,
   as 021.33 does, and did not render it in `i`.

## Known forms used in a new sense (for the glosser's `__broaden__`)
- mi 'do not' (prohibitive, U9)
- mix 'do not, you (pl.)' = mi + ix (U9)
- Ve 'yes, very well' as an answer (U16)
- xul 'lower, bow down' (U47), not 'came'
- tubul 'heaped up (?)' (U46)
- culun 'be found, come upon (?)' (U46)
- quil 'let us see' (qil, U28)
- xquetamah 'we knew' (U5)
- chique 'to us (?)' (U35)
- cam 'death' (noun, U37)
- quelic as que + elic 'they flee (?)' (U41)
- cal 'their children' (U45)
- xcotix 'cut out (?)' (U31)
- ꜩalic in xcheque chuvach ꜩalic (unclear, U31)
- coloba 'set out, hold up (?)' (U25)
- quetaon 'we know (?)' (U4)

## Proposed house renderings (not added to conventions.md)

| K'iche' (MS) | `l` | `i` | avoided |
|---|---|---|---|
| puz, puzu (as published) | sacrifice | sacrifice (cut open) | kill (for puz), immolate |
| ꜭaztah / caztah v vach | come-alive its-face | come back to life (mt k'astaj for both spellings) | be resurrected |
| ꜩy (022) | dog | dog (the published ꜩi, mt tz'i') | — |
| yvahil | your-payment | your payment | reward, wages |
| maihah / maiha | marvel | marvel at (mt maijaj / maija by the letters) | be amazed |
| qui vholom ahau | their-head lord | their chief lord | king |
| al, ꜭahol (rahaual ival i ꜭahol; cal qui ꜭahol) | child, son | your / their children and sons (the note gives Brasseur's 'vassals') | vassals (in `i`) |
| halvachibal quib | change-of-face themselves | changing their own form | metamorphosis |
| Xhunahpu (022, three times) | Xhunahpu | Hunahpu (as 021; the note says the MS has x-) | — |
| at ahau | you lord | lord (as 011, 019) | my lord, Your Majesty |
