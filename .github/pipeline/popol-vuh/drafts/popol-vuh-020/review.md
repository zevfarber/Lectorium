# popol-vuh-020: review

## Pass 1

I read conventions.md, runbook.md, the Run 3 RUNBOOK §2 "Reviewer", packet.md, establish-log.md, known-forms.json, drafter-notes.md, units.json (59 units), the published 001–019 (mainly 011 and 015–019) and popol-vuh-glossary.json. Brasseur 1861 (OCR lines 25900–26480) was used only to check meaning. No modern translation was opened.

I made the edits with a script (`json.load` → exact-substring replacements, each asserted unique → `json.dump(ensure_ascii=False, indent=1)`). No `t` changed. The script also asserted that every `mt` has exactly as many entries as WORD_RE finds tokens. units_src.py has not been updated to match.

### Checks run
- **mt.** By script, I compared every mt with the mt of the same manuscript form in the published 001–019. Nothing contradicts a published spelling. Where a form has two published values (xcah xkaj/xqaj, cam kam/k'am, xquilo xkilo/xqilo, chi chi/chik/chi', vvb uub'/wub'), the draft picks by sense, and each choice is right in context. I then checked every new form by hand against the letter rule. Each is respelled letter for letter, except where the drafter supplied a mark for a certain word: sotz' family, tz'onoj (as 016), uk'utb'al (as 015 k'utb'al), raq'ab'al (aq'ab' published), xik'ow (as icou ik'ow), k'oje (as 015 coheic), q'equmar, Wuch' (as 001). None of these is a restoration on an uncertain word. One exception is co=k'o in a line not understood (U22), but every published co is k'o, so I kept it.
- **README 5b.** U36 opens "The manuscript has xuhquiba, a misprint for xu tiquiba, corrected here: …". U55 opens "The manuscript has xquihquiba, a misprint for xqui tiquiba, corrected here: …". Both follow the 017 formula. Correct.
- **Establishment log.** Every doubtful word in the log is flagged in a note, with two exceptions that I fixed below (pacaquic U9, cahanican U19). The notes also mention every one of: the struck words (U20), the blot (U9), the looped t, the ß-like ligature, the plain c kept against Brasseur, and the readings kept as written (quꜩ, xcha, chopor, balam ×2, Xecoh, qui qui ꜭux, chiqui, rahal, xbec, Qui pu ca, cut/cat).
- **House renderings.** The draft follows them: Vꜩ bala "Very well"; Heart of Sky; the lords; the boys; Huncame, Vucub Came; vbac vvach "eyes" (U30 `l` corrected below). The chacatah- verbal noun is "brought low", as 019.
- **Couplets.** Couplets stay couplets in `i`: xa bolol, xa ꜩimah; que ꜭha, que ꜭha; xul coloc, xulu culoc; que huminic, que chaninic; chuti chicop, nima chicop (fixed U25); xavi xare … xavi xare (fixed U32).
- **Cross-references in notes** were checked against the published text. They are all correct: 011's Xuxulim Ha, Balami Ha (third house) and Ꜩoꜩi Ha (fourth house); ꜩaꜩ chi teu vpam; the father's head in the tree on the lords' order (011 U19–20); 016 v xambe and ꜩoꜩotic; 017 quixbic and the tiquiba case; 018 tio and varanel; 019 chacala, Mavi quehe and qui chacatahic; 003 xꜫecumaric; 016 coh vꜩin; 010/017 tacol que; and the glossary senses of coh 'put', quel 'hang', xcupix 'caught', he 'go'.
- **Remembered English.** I found none. The only phrase not built from the K'iche' or from Brasseur was U45 "brought it on yourselves", which I replaced.

### Changes (unit · field · severity · what was wrong · what was done)
1. **U27 · i · major.** `i` said "and all of them went off" for ta xe ul he cut conohel, but xe ul is 'they arrived' and `l` has "they-arrived going(?)". The sense was the opposite of `l`. Changed to "and then all of them arrived (?)".
2. **U16 · i · minor.** xqui ya vi quib is plural ('they gave themselves'), and `l` has it plural, but `i` said "one of them gave himself up". Changed to "they gave themselves up (?), one (?) because of one Camazotz", which mirrors hun vi rumal hun. The note's reading of the first hun is kept.
3. **U16 · l · minor.** The note gives vvb as 'his blowgun', but `l` had "in blowgun". Changed to "in his-blowgun".
4. **U18 · i · minor.** In ri hun ꜩam vvb, hun belongs to ꜩam ('one end of the blowgun'), but `i` said "the tip of one blowgun". `i` also added "one of them", which the K'iche' does not have. Changed to "and there they stayed perched (?) at one end of the blowgun". The note's last clause now says the one perched there is not named.
5. **U25 · n · minor.** The note said "ac is not otherwise known in this book". But the peccary is aꜫ (mt aq') in 015 and 016, in the same kind of animal list beside ziz, and Brasseur's 'Sangliers' matches the glossary entry for aꜫ. The note now gives that link (inferred). I kept mt ak; see refused 3.
6. **U30 · l · minor.** xcotix has no plural absolutive, so it is 'it was carved', but `l` had "they-were-carved". `l` also had "his-bones" against the house `l` "its-bone his-face". Changed to "it-was-carved(?) its-bone his-face".
7. **U30 · l · style.** Unknown words in `l` used the modern spelling ("kolok(?)", "kulok(?)"), where published `l` uses the MS form (cayac(?), caxꜩ(?), hina(?)). `l` also gave xulu a "came-down" that the root ul does not have. Changed to "he-came coloc(?), he-came(?) culoc(?)". The guess "came down" stays in `i`, marked.
8. **U9 · l · style.** "pakakik(?)" (modern spelling) changed to "pacaquic(?)", as in 7.
9. **U9 · n · minor.** The log lists pacaquic as a doubtful reading, but the note did not say so. Added "is a doubtful reading and".
10. **U19 · n · minor.** The log lists cahanican as doubtful, but only labalo was flagged. Added "(cahanican is also a doubtful reading)".
11. **U45 · i · minor.** The note says the English follows Brasseur ('Vous avez subi toutes les hontes'), but `i` had "You have brought it on yourselves (?)", which is neither Brasseur nor the K'iche'. Changed to "You have suffered every shame (?)".
12. **U46 · i · minor.** que vꜭhaxic is a plural passive ('they are told'), as `l` and the note have it, but `i` said "they told him". `i` also had "rest … on the ball", against Brasseur's "repose ta tête … du jeu de balle", which the note says it follows. Changed to "“Let the head rest (?) from the ball (?),” they were told." This matches U45's "they were told".
13. **U47 · l · minor.** `l` had "held-up(?)", while `i` and the note have "held themselves back". Changed to "held-back(?)".
14. **U40 · i · minor.** `l` and the note have 'expose yourself' (Brasseur 'Expose-toi'), but `i` said "You must stand alone", a different sense. Changed to "Only put yourself forward, then (?)", with xa 'only'.
15. **U14 · l · minor.** The note gives cahauaxic as c- (ongoing) … 'it is wanted', but `l` had "it-was-wanted". Changed to "it-is-wanted". `i` stays in the past narrative.
16. **U51 · n · minor.** The note did not mention that v coc Xbalanque, set beside v holom Hunahpu in the same sentence, can be the possessive 'Xbalanque's turtle'. Added that reading, and that the English takes Xbalanque as the doer, with Brasseur.
17. **U8 · n · minor.** The note gave "coh 'us'" with its c- unaccounted for (glossary: k- + oj). Changed to "coh 'us' (c- + oh)".
18. **U26 · n · minor.** Same fix for quix: "(c- + ix)".
19. **U5 · i · style.** "the guardians had gone once more" added a pluperfect the K'iche' (xe be chic) does not have. Changed to "They came out again (?), when the guardians went once more to summon them."
20. **U1 · i · style.** chi (= chic 'again') was dropped. Changed to "Then they went in again, into the Cold House" (as 019 "went in again, into Chaim Ha").
21. **U7 · i · style.** Same: "Then they went in again, into the Jaguar House:".
22. **U25 · i · style.** The couplet chuti chicop, nima chicop had been merged into "all the animals small and great". Changed to "all the small animals and the great animals".
23. **U32 · i · style.** The parallel xavi xare … ; xavi xare … had been flattened to "…, and it spoke as well". Changed to "likewise its hair (?) showed itself fine (?); likewise it spoke."
24. **U28 · n · style.** The note said as fact "The story explains why each animal eats what it eats". Changed to "The passage seems to tell why each animal eats what it eats, though the text does not say so."

### Findings refused
1. **U17 ꜩonoh = tz'onoj against U26 xuꜩonoh = xutzonoj.** The two are inconsistent inside the part, but each matches the published mt of that exact form (016 tz'onoj, 008 xutzonoj). Changing either would break consistency with a published part. The better fix is to change 008 to xutz'onoj in a later correction, outside this folder.
2. **U22 co = k'o in a line not understood.** All seven published co are k'o, and the note flags the line. I kept it for consistency.
3. **U25 ac mt.** I did not change it to aq'. The link to aꜫ is inferred, not certain, so by the rule the toggle respells the letters. The note now gives the link.
4. **U20 v nimal 'body'.** 011's xa vnimal was itself read 'the elder', taken as the body, so it is not independent support. The (?) stays.
5. **U39 "he should not play (?)".** qui could be 'their' (mana qui … chaahic 'not their playing'). The note already marks the reading as inferred, and Brasseur's 'de ne pas jouer' supports either. No change.
6. **U35 note "the dawn comes and goes four times".** This is an inference, but it comes directly from cate ta chi queꜫumar chic … cahmul. Kept.
7. **U42 "I will do the rest" / U48 "went to meet it".** Both lean on Brasseur ('je ferai le reste', 'sortit à sa rencontre'), but neither changes the force. Kept.
8. **U30 `i` "its eyes" against the house "his eyes".** The pronoun follows the context: at this point it is the turtle's face. The house `l` was applied (change 6).

### Drafter's open questions
- **zoꜩ: mt sotz' or by the letters? Keep sotz'** (and Kamasotz', Sotz'in Ja, Sotz'i Ja).
  - The manuscript zoꜩ matches sotz' letter for letter except for the unmarked ejective on the plain ligature. That is exactly the case of coꜩih → kotz'i'j (015–019) and ꜩonoh → tz'onoj, whose glossary entry says "the word certain; the manuscript has the plain tz ligature".
  - 011's tzotz is a different form (ꜩoꜩ, ligature at both ends). Its glossary entry gives the reason for respelling by the letters: "the modern form of Ximénez's word is not certain". The same-form consistency rule is therefore not broken.
  - For QUESTIONS.md: whether 011's ꜩoꜩ / Ꜩoꜩi Ha should be brought into line (sotz' read through a ligature-for-z) is a decision for that part, not this one.
  - The glosser needs new entries for zoꜩ, Camazoꜩ, Zoꜩin and Zoꜩi. The ꜩoꜩ entry should not be broadened.
- **pix in `i`: keep the K'iche' word, marked (?)**, as the house does for ꜩite.
  - The two candidate readings (Brasseur's 'glands' of a cornice; modern pix 'tomato') point to different scenes, and the text itself does not decide.
  - Committing `i` to either would state a guess as fact. The notes (U41, U49, U54) already give both readings.
  - `i` prints pix for MS pixc in U41. The note ties them together, so this is acceptable.
  - The log's "the oak" is only in the log's summary, not in the draft. Nothing needs changing.

### Counts (pass 1)
- major: 1
- minor: 15
- style: 8
- total changes: 24 (25 replacements; U30 `l` had two)
- refused: 8
