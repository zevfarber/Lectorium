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

## Pass 2

I re-read units.json after the pass-1 changes and found nothing further to change. I checked:
- the about paragraph against the revised U16, U18 and U27;
- notes against the published glossary senses: tiyic, chuꜩinic, rah, chopon, cat, coh, vila, quecha;
- house renderings, couplets, and `(?)` marks between `l` and `i`.

Units changed in pass 2: none.

Then I checked all 100 novel entries and the 4 `__broaden__` entries in gloss.json against units.json (mt, `l`/`i`/`n`) and against popol-vuh-glossary.json, by script and by hand:
- Every key is a lowercased token of the text, and none is already in the glossary.
- Every modern form equals the draft's mt. The only differences were capitals from a sentence start (xtane, cahanican, acaroc), and lowercase there follows the glossary's practice.
- Every broadening begins with the old entry whole, then " · ".
- I kept zoꜩ = sotz' and pix/pixc kept in K'iche' with (?), as decided in pass 1.

I edited gloss.json by script (load, replace, `json.dump(ensure_ascii=False, indent=1)`), with the broadening prefixes asserted.

### Changes (item · severity · wrong · done)
1. **pacaquic · minor.** The entry gave "ke 'they (ongoing)' + pakakik" as the morphology of the single word pacaquic, and it omitted the doubtful reading. Rewritten as "(doubtful reading, guess) fall upon … verb in -ik".
2. **buhuhic · minor.** The entry glossed it "taking counsel", which belongs to ꜩonoh … naoh, not to this word. It also gave the morphology as que + the word. Rewritten as "(guess) whirring, making a great noise … verb in -ik".
3. **queꜫumar · minor.** The entry ended "; ke 'then'", which is nonsense for this form. Rewritten as q'equm + -ar.
4. **ꜭohic · minor.** The morphology was "k'o + -jik". Corrected to k'oj (as k'oje) + -ik.
5. **ꜭoleta · minor.** The morphology included kat 'you shall', which is a separate token. Corrected to k'ol + -eta, with (?) kept.
6. **cactarin · minor.** The entry had "kak 'red'", against the draft's mt kaq for cac 'red' (U36) and the glossary's kaq 'red'. Corrected to cac (kaq).
7. **xulu · minor.** The entry had "(?) came down". After the pass-1 change to U30 `l`, xulu is only 'came, arrived' (ul), and the "down" guess belongs to culoc. Rewritten as "(doubtful reading) came, arrived".
8. **yecoub · minor.** The entry had "held up, held back". After the pass-1 change to U47 `l`, only "hold back" stands. Rewritten as "(guess) hold back …", noting the plain c kept.
9. **ac · minor.** Brought into line with the pass-1 U25 note: perhaps aꜫ 'peccary' written with plain c. The "aq/ak' both possible" clause was dropped. mt ak is kept, respelled by the letters.
10. **mucum · minor.** The entry said "doubtful", but the reading is not doubtful; only the sense is inferred. Changed to "(inferred)", with Brasseur's French added.
11. **cahanican · minor.** The doubtful reading from the establishment log was missing. Added.
12. **ꜩucu · minor.** The doubtful reading from the establishment log was missing. Added.
13. **coxcotic · minor.** The sense is inferred in the U50 note but was unmarked in the entry. Added "(inferred)" and the looped t.
14. **catic · minor.** The entry was pinned to the line ("were burned … in xe katik"), and the sense was not marked as inferred. Made general: "(inferred) burn, be burned; k'at with plain c + -ik".
15. **xeꜩacou · minor.** The -ow ending was left unnamed. Added "the ending that names the doers (after Are)", as in the glossary's banouic, and marked the sense (inferred).
16. **teuh · minor.** The modern form was lowercase "tewj", but the word occurs only in the name, where mt is "Tewj". The morphology "+ ha 'house'" was wrong for the single token. Rewritten.
17. **ꜩah · style.** The entry was pinned to the line. Made general, marked (doubtful reading, guess).
18. **quꜩ · style.** "Not otherwise known" missed what U4's note gives (qu + ligature, Brasseur c'utz = ca vꜩ). Rewritten.
19. **camizabal · style.** The entry ended "ki- 'their' before it", which describes the line, not the form. Moved into an example.
20. **hebel · style.** "respelled with the sense after the draft" was meaningless. Rewritten.
21. **cohe · style.** "k'o 'be' + -je, plain c" is now "ꜭohe 'be' written with plain c, the k' restored as in coheic".
22. **huchatic, ama, chacuca · style.** These had sentence-start capitals in the modern form though none is a name. Lowercased (one change, three entries), following the glossary's practice.
23. **__broaden__ tiyic · minor (added).** The glossary has "were eaten (uncertain)"; here (U16) the word is 'were bitten'. Added, with the old entry kept whole.
24. **__broaden__ chuꜩinic · minor (added).** The glossary has "it will come right, it can be"; here (U15) the word is 'it is finished, comes to an end' (inferred). Added.
25. **__broaden__ nimal · minor (added).** The glossary has only 'greatness'; here (U20) the word is Hunahpu's body (inferred, Brasseur 'le corps'). Added.
26. **__broaden__ qui · minor (added).** The glossary had no entry for qui 'sweet, glad' (U10 qui qui ꜭux, Brasseur quiy) or for the unclear question particle (U11 Apa qui, U20 Qui cu are). Added both readings.

### Refused
1. **cahanican, xtane, acaroc: lowercase against the capitalised mt.** The capitals come only from the sentence start. The glossary lowercases such words (e.g. catecut k'atek'ut).
2. **vuch broadening.** The new reading ("the animal, standing alone") overlaps the old 'opossum'. It is kept because the old entry is tied to the name and the mt here is lowercase wuch'.
3. **No broadening added for cul, cama, he, coh, tio, cac, xcah, chi, ꜩam, rah, chopon, vꜭhaxic, xquilo or co.** The glossary already covers this part's senses of all of them.
4. **The remaining entries were left as written:** zacbocom, ochoch, cuꜩ, mamai, xzach, vꜩinic, bolol, ꜩimah, cahauaxic, zoꜩin, zoꜩ, camazoꜩ, chaquiꜩam, chopor, vcutbal, quiliꜩ, xtane, zilobic, chacal, cahanic, labalo, ril, cupul, zilabic, zoz, quixbih, acaroc, yayan, colana, xare, racabal, cumar, ꜩalic, canohoc, tiz, cubulcutih, chuꜩam, halvachibal, xcotix, coloc, culoc, zoꜩi, atan, chuuc, xecah, xaquinuchic, xuchux, xaquinic, xaquin, raxaꜩinic, chux, baquitila, chayecuh, avib, pixc, avuꜭ, xpixabaxic, colan, chacoyan, yan, caxou, tanenic, xicou, canab, pix, ocotal, chaninic, camixtah, xtiquixtah, cuba, colem, xcacatah, pucabin, zaquiram, zaquilal, rahal, and the coc/quel/xcupix broadenings. In each one the mt, sense, (?) mark and morphology agree with the draft.

### Build and validate
- `python3 ../run3/r3.py build popol-vuh popol-vuh-020` reported "BUILT popol-vuh-020: 59 units → popol-vuh-020.json", with no WARN lines.
- `python3 ../run3/r3.py validate popol-vuh popol-vuh-020` reported PASS.
- The build wrote popol-vuh-020.json and updated popol-vuh-glossary.json and stories.json. Nothing was published or committed.

### Counts (pass 2)
- major: 0
- minor: 20 (16 entry corrections + 4 added broadenings)
- style: 6
- total changes: 26 (24 entries rewritten in gloss.json, 4 broadenings added, 0 units changed)
- refused: 4

### Counts (both passes)
- major: 1
- minor: 35
- style: 14
- total changes: 50
- refused: 12
