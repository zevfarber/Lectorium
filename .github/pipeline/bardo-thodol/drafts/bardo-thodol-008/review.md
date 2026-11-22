# Review — bardo-thodol-008 (pp. 72–79)

## Pass 1

Checked against conventions.md, QUESTIONS.md, runbook.md and ../run3/RUNBOOK.md (Reviewer), packet.md (the pinned print,
its 18 `# fix:` lines and the establishment log), hooks.py, tib.py, units.py (the pilot), the units of 002–007, 007's
review.md, glossary.json, and both control witnesses in source/raw/. The passage is at dzogchengonpa-kha.txt ll. 308–344, and
in the other recension from དཀྱིལ་འཁོར་དེའི་ཤར་ནས་ས་ལ་གནས་པའི to …ཐོས་གྲོལ་ཆེན་མོ་ལགས་སོ, where it runs on into the wrathful
deities. All 31 units were read word by word, from the original to `l` to `i`. Every grammatical label in the notes was
checked against the form, and every other-recension claim in the notes against the stored text. Every division was checked
against conventions.md "What the page shows" and against how 001–007 divide the same words, by script over all their `w`
(each multi-syllable word of 008 searched as a syllable string in 001–007, and each pair of adjacent 008 words searched as one
word there). Unit numbers are 1-based.

units.json was edited in place by script (ensure_ascii=False, indent 1, no final newline, as the file was written; a
round-trip of the unedited file was checked to be byte-identical first). The letters of `w` are unchanged; one word was
re-divided (u. 26). Letter check (all `w` joined, ' / ' and spaces removed, against `hooks.letters()` for the part, loaded as
r3.py loads it): 31 units, 3825 letters, PASS. Verse line counts w / l / i are equal (u. 26: eight lines each).
hooks.assemble + hooks.validate with an empty part glossary: no error other than "no glossary entry" (136, the glosser has
not run yet), and no WARN.

### Changes

- u. 9 · n · minor · stem. "bcad is the future stem of gcod" is wrong. The verb is gcod / bcad / gcad / chod, so bcad is the
  past stem (the master glossary's བཅད says so) · now "bcad is the past stem of gcod (gcod / bcad / gcad / chod)", and the note
  adds that the future gcad would be expected before du, and that the other recension also has bcad du.
- u. 23 · n · minor · stem. "bsags, the past stem of sogs" named the imperative as the verb. The verb is gsog / bsags / bsag /
  sogs, as the master glossary's བསགས་པའི has it · now "the past stem of gsog, 'to gather': gsog / bsags / bsag / sogs".
- u. 5 · n · minor · fact. "as the print itself writes it four lines below": dbag is on 74.1 and dpag on 74.4, which is three
  lines below (checked by script on the established file; the establish log says 74.4) · now "three lines below".
- u. 13 · n · minor · fact. "the word stands rightly in the line above and three times on the next page": dud 'gro'i is on 75.4
  and, on p. 76, only on 76.4 and 76.5 (by script; the log names 75.4, 76.4 and 76.5) · now "twice on the next page".
- u. 30 · i · minor · drafter's doubt 16. "…is the Great Liberation through Hearing. It is finished." supplied a copula that the
  print does not have. That is the other recension's lags so. The print's sentence has one verb, thal lo, with thos grol chen
  mo in apposition to what is listed, as `l` has it · now "All that stands above, the recognition of the clear light …
  and the pointing-out of the peaceful bardo of reality, the Great Liberation through Hearing, is finished."
- u. 26 · w · style · drafter's doubt 18. ཡུམ་མཆོག was joined. 004–007 split ཡུམ་ མཆོག seven times, and 007's review refused to
  join it (mchog is an epithet added to yum, unlike the lexical yum chen) · re-divided ཡུམ་ མཆོག (letters unchanged).
- u. 26 · l · style · lines 1 and 5 had "Knowledge-holders' deity-hosts" and "knowledge-holders' host's(?)". The apostrophe
  shows a genitive where the Tibetan has none (rig 'dzin lha tshogs, dpa' bo rig 'dzin tshogs). In this part, u. 27 has the
  same words as "knowledge-holder deity-hosts", and u. 24 has "knowledge-holders' deity-host" for rig 'dzin gyi lha tshogs ·
  now "Knowledge-holder deity-hosts (plural) also" and "heroes, knowledge-holders, host's(?) the-way lead!".
- u. 26 · n · style · "as the print elsewhere writes gi for gis (002)". The instance is the pilot's gcig gi (conventions.md;
  005's note cites it), not 002 · now "(gcig gi in the pilot), and 005 read yi as yis in its prayer".
- u. 30 · l · style · "the dying-point's between" for 'chi kha'i bar do, where the pilot (001 u. 19) has "Death-point's
  between" · now "death-point's between".
- u. 1 · n · style · drafter's doubt 1. "With full ripening, power over life, the great seal and spontaneous presence below,
  these are names of the stages a knowledge-holder reaches" claimed all five names as a known set. The usual list is four:
  full ripening, power over life, the great seal and spontaneous presence. Dwelling on the Levels is the fifth here · now
  "Four of the five names … are elsewhere the usual list of the stages a knowledge-holder reaches; Dwelling on the Levels,
  the fifth here, is read with them, and the text itself does not explain the names."
- u. 3 · n · style · "The words are those of the east, with red for white and mkha' 'gro ma for mkha' 'gro" left out the
  third difference. The east has 'khril zhing and the west 'khril ba · added.
- u. 7 · n · style · drafter's doubt 5. The reading of 'dir as ldir has a parallel the note did not use. The print has 'dir
  btsam du in 003 (u. 33), taken there as ldir ba tsam du · one clause added.
- u. 10 · n · style · "The print has ཀྱཻ." said nothing about why · now "The print has ཀྱཻ, the other recension ཀྱེ." (checked).
- u. 17 · n · style · "rang is said four times" listed three (rang snang, rang du, rang ngo) · khyod rang added.
- u. 21 · n · style · "parts 003 and 007 had mdun pa, so the m is the print's habit" overstated the evidence. By script, the
  print has 'dun pa in 002, 004, 005 and 006 (seven times) and mdun pa in 003 and 007 · now "it had mdun pa in 003 and 007 too
  (beside 'dun pa in 002 and 004–006), so the m is one of its spellings".
- u. 22 · n · style · "byon, the respectful 'come'" without its stem; 007's review settled the label · now "byon, the past
  stem of 'byon", and the other recension's 'byon par is marked "with the present stem".
- u. 25 · n · style · drafter's doubt 12. khon nas is a guess either way. khong nas, "from within, from the heart", is as
  near to the print as kho na nas, and it fits gsol · added as another possible reading. `i` still follows the other
  recension's kho nar, as the note says.

Severity count: major 0 · minor 5 · style 12 (17 change lines).

### Drafter's doubts, adjudicated

1. u. 1 ས་ལ་གནས་པའི རིག་འཛིན "Dwelling on the Levels": kept. sa in a list of knowledge-holder stages is the bhūmi, and the
   note gives "on the Earth" as the plain sense of the words. The claim about the names is narrowed to the usual four (above).
2. u. 5 ཀྱི་རོལ་དུ "round them": kept, with "side-at(?)" in `l`. rol is "side" (phyi rol, nang rol, pha rol), so "on their
   side" is a fair reading of the print. The note gives the other recension's ཕྱི་རིམ་དུ (checked) and says the sense is about
   the same, which is true.
3. u. 5 རིགས་བཞི, གནས་གསུམ, གནས་བཅུ unexplained: right. The text does not explain them, and the note says so rather than
   supplying a list from outside. གནས་གསུམ་ མཁའ་འགྲོ has no genitive in the print ("places three sky-goers" in `l` is right).
   The other recension has gnas gsum gyi, which changes nothing. གིང untranslated: kept. It is a class name with no English
   equivalent, and the note describes it. It stands untranslated in the about as well.
4. u. 6 ཞིང་ལྤགས, མི་གསུར: kept as hedged guesses. `l` has "corpse-skin(?)", and the notes say "the sense is not sure" and "taken
   so". Each part (lpags "skin", gsur "burnt offering", dud pa "smoke") is sound.
5. u. 7 ཙམ་ འདིར་བ་ འོང read as ldir: kept, with "booming(?)" in `l`. The other recension has ཙམ་དུ་ལྡིར་ནས (checked). The
   print spelled the same verb 'dir in 003 (u. 33); the note now says so (above).
6. u. 10 ཁྲ་ཤིག་ཤིག་པ, མེར་མེར་བ, ཕྱམ་ཕྱམ་པ: kept as approximate senses, which the note says they are. The stray གཅིག: kept, "one(?)"
   in `l`, left out of `i`. The other recension has ཕྱམ་ཕྱམ་པ་ཞིག་གསལ་ལ (checked), so gcig is the print's indefinite, written
   after the ༔ instead of before it, as the note says.
7. u. 10 མཚོན་སྐུད = tshon skud: kept. The other recension has ཚོན་སྐུད་བསྒྲིལ་བ (checked), and "weapon-thread" gives no sense.
8. u. 16 བསོ་སྒྲ: kept, "bso-sound" in `l`, with "the sense is not sure" in the note. The other recension also has བསོ་སྒྲ, so it is
   not a misprint of this print. `i` gives one English word ("a din, a roar") for two cries, which is acceptable with the
   note. སྒྲ་གྲགས one word: kept. sgra grags "sound, noise" is a lexical compound. No earlier part has it (003's སྒྲ་ དག་ ལ is a
   different reading).
9. u. 17 རིག་པའི་ རང་དུ: kept. The print's words give sense ("as awareness's own"), and the note gives the other recension's
   rang rtsal du (checked) and the possibility that rtsal dropped.
10. u. 19 བཀོལ་གཅོད: kept as "worked and slaughtered", from bkol "put to work" and gcod "cut". The note gives the other
    recension's bkol spyod (checked).
11. u. 23: ཁྱེད་རྣམས་མཁྱེན: kept. mkhyen is the respectful "know", and the other recension's re mkhyen is noted (checked).
    ད་ ཞག་ ཕན་ཆད་དུ: kept, with the reading marked unsure. da zhag is not attested as one word in 001–007 (ད་ལྟ is), so the
    split stands. ཕན་ཆད is joined as 001–007 join it. ཅིག་ གི: a genitive after -g, right. བཟུང་ཅིག: the note correctly calls
    bzung the past stem of 'dzin used where the imperative zung is expected, with the other recension's zungs (checked).
12. u. 25 ཁོན་ནས: kept as printed, translated after the other recension's ཁོ་ནར (checked). The alternative khong nas was added
    (above).
13. u. 21, 25 མདུན་ བརྩེ་གཅིག་ཏུ: the division stands. It matches 005–007's འདུན་པ་ / མདུན་པ་ རྩེ་གཅིག་ཏུ, and མདུན stands for mdun
    pa. The claim about the print's habit was narrowed (above).
14. u. 26 line 5 ཚོགས་ཀྱི as kyis: kept. `l` has "host's(?)", and `i` and the note read it as "by", after the parallel
    ཚོགས་ཀྱིས of line 6 and the other recension's རྣམས་ཀྱིས (checked). The note gives the reading as printed. Its cross-reference
    was corrected (above).
15. u. 28 དགེ་བའི་བཤེས་གཉེན་གྱི་རིགས: kept as hedged ("the phrase is short and the sense is not sure"). rigs "kind, class" with
    thams cad is plain. The about's "all who have had a spiritual friend" follows the note's reading.
16. u. 30 ཐལ་ལོ "it is finished": kept in `l` with "(?)". thal "to pass through, to have gone by" with -lo gives a closing
    verb. `i` was rid of the other recension's copula (above). u. 31, the threefold seal: the note is hedged ("said to mark
    it…; its meaning is explained in more than one way") and is kept.
17. u. 31 ཨྠྀི: letters "ithi" (tib.py LETTERS) and said "iti" (OVERRIDE) are both right by their own systems. The letters
    line is Wylie, and the second i stands for the reversed gi-gu on ཐ. The say line is THL, where tha is said t. The note
    explains both and gives Sanskrit iti. No change.
18. New divisions, checked by script against 001–007:
    - བཅད་དུ, དྲང་དུ as 007's བསྒྲལ་དུ, བསྐྱལ་དུ.
    - འགུལ་འགུལ་དུ as འཆར་དུ (26×).
    - སྐྱེ་བར as གྲོལ་བར.
    - རང་དུ as ཡེ་ཤེས་སུ.
    - དེ་རུ as ས་རུ, ལྔ་རུ.
    - ཤ་སྟག་གོ, ཐལ་ལོ: fused endings, as ཕྱག་འཚལ་ལོ, ཡོད་དོ, ངེས་སོ.
    - ཨ་ཙ་མ་ར: one interjection.
    - ཁྲོ་འཛུམ: one compound, as the joined ཁ་དོག-type pairs. ལྔ་ལྡན: one compound.
    - ཆོས་སྐྱོང་བའི: chos skyong is a lexical compound.
    - ཐད་ སྙིང་ཀར: thad stands alone here, while 004–006 have the one word ཐད་ཀར in snying gi thad kar. སྙིང་ཀར as ཐུགས་ཀར.
    - ད་ ཞག: as 11.
    - ངོ་ འཕྲོད split, as in 001–003 (10×).
    - Only ཡུམ་མཆོག departed from practice, and it was re-divided (above). The script found no other word of 008 divided
      differently in 001–007, except རང་ངོ (joined 2×, split 1× before; the pilot joins it) and སྐྲག་དངངས. 006 u. 28 joins
      སྐྲག་དངངས, and 005–006 join དངངས་སྐྲག. 003 u. 14 splits it only because འཇིགས་ སྐྲག་ དངངས་ གསུམ counts the three words
      as three. The joined forms stand.

### Checked and confirmed (no change)

- The five misprint notes open "The print has X, a misprint for Y, corrected here.": དབག → དཔག and མཁའ་གྲོ → མཁའ་འགྲོ (u. 5),
  དུད་འགྲེའི → དུད་འགྲོའི (u. 13), བདེ་གཤིགས → བདེ་གཤེགས (u. 23), ཚོཌ → ཚོགས (u. 24). The contractions are named: དེ་ཙན (u. 14), རང་སྒྲའབྲུག
  (u. 15), ལྕགྶ (u. 24), and the mid-line tsheg of ལྗང་ཁུསྐུ (u. 4). The other ten fixes are line-join tshegs and need no note.
- The five [?] readings are all in the notes: མདོག (u. 2), མི (u. 6), བྱེད (u. 8), བཅས (u. 16), ཚོཌ (u. 24). So are the log's
  kept-as-printed items: ཀྱི་རོལ་དུ (u. 5), ཙམ་འདིར་བ་འོང (u. 7), མདུན་བརྩེ་གཅིག (u. 21, 25), ཨ་ཙ་མ་ར (u. 23), ཁོན་ནས (u. 25),
  ལྡན་བ and གཅིག for ཅིག (u. 2), ཨྠྀི and རྒྱ་རྒྱ་རྒྱ (u. 31), and དང༔ without a tsheg (u. 30). Also noted: the witness's slips mdag
  (u. 2), a tsa ma re (u. 23), sku for kyu (u. 24), and the skipped dpa' bo dang (u. 5). All were checked in
  dzogchengonpa-kha.txt.
- Other-recension claims, checked one by one in the stored text. All are accurate:
  - u. 1–5: lta stangs ×4; phyi rim du; srung ma; bla re; khengs par phyed༔ shig shig.
  - u. 6–12: tsam du ldir nas 'ong ngo; phyed and bsu bar; ye shes 'od kha dog lnga; tshon skud; phyam phyam pa zhig; snying
    gi thad kar; lta mi bzod pa; zhig kyang; 'char du 'ong.
  - u. 14–20: the ༔ after ma skrag cig; 'od kyi nang nas, no dus gcig la, and 'ong; sgra drag; sgra drag po'i drag sngags; ma
    skrag cig added; rang rtsal du; lhung; bkol spyod; thon pa'i dus; gyis la.
  - u. 21–24: 'dun pa rtse gcig tu; 'di rnams and 'byon par; re mkhyen; bde bar gshegs pa; thugs rje'i 'od zer gyis; a tsa
    ma; nga 'di man chad du; ma gtong zhig; zungs shig.
  - u. 25–30: kho nar; drangs; rnams kyis; kye ma; thams cad kyang; kyang; ngo sprad pa twice and bar dor; lags so, and the
    running on into the wrathful deities.
- Stems and labels:
  - skyes, past of skye; btab, past of 'debs; bzung, past of 'dzin, imperative zung(s); btang, past of gtong.
  - drang, future of 'dren, beside past drangs and imperative drongs; bsgral, past of sgrol; skyol, imperative of skyel.
  - Particles: ru after a vowel, -go after -g, gi after -g.
  - All right (bcad and bsags corrected above).
- House renderings: "the between" / "bardo"; "child of noble family"; "knowledge-holder"; "Sky-Faring" and "sky-goer" kept
  apart; "face-introduce" / "pointing-out" for ngo sprad, and the face "meeting" for the intransitive ngo 'phrod, as the pilot
  u. 21; "clear light"; "reality" for chos (nyid); "knowing" / "awareness"; "dawning comes"; "lustreless" / "dull"; the prayer
  frame and the guess for smon lam 'di skad du thob cig.
- `i` was read for wording remembered from the modern translations. None was found.

### Refused

- u. 30 · `i` follow the other recension's lags so: the print is followed (conventions.md), and the note gives the other
  reading. Kept.
- u. 16 · `l` "Sound loud" for sgra grags, against the note's "sound, noise": grags "to resound" read as an attribute is
  within the word's range, and `i` "Loud" agrees. Kept.
- u. 21 · `i` "and think:", which has no word in the clause: it anticipates snyam pa'i, which closes the thought in u. 25. Without
  it, the quoted thought would have no frame in English. Kept.
- u. 11 · note that rigs 'dzin is a kept spelling not listed in the establish log: the note already says it is the print's
  spelling, here only. Kept.
- u. 2 · cig written gcig: the note says this is the print's spelling, as the log does. No rule claim. Kept.
- u. 6 / u. 8 · phyed glossed "half" in one note and "half, to open" in the other: both describe the other recension's word,
  whose sense is unclear there. Kept.
- about · no change. Its readings follow the notes (Dwelling on the Levels, ging, the spiritual friend), and it does not use
  the copula changed in u. 30's `i`.

### For QUESTIONS.md (open decisions for the owner)

- The five knowledge-holders' names (u. 1–4, about): sa la gnas pa is rendered "Dwelling on the Levels" (sa = bhūmi). If
  "Dwelling on the Earth" is preferred, u. 1, the about and the glossary entry change together.
- ཐལ་ལོ (u. 30) as "it is finished" and the threefold seal རྒྱ་རྒྱ་རྒྱ (u. 31): both closings are read by sense, and a reader of
  treasure literature should confirm them.
- ཨྠྀི letters "ithi" against said "iti" (tib.py LETTERS / OVERRIDE, added by the drafter): consistent with the house systems.
  To show "iti" in the letters line too, change tib.py's LETTERS.

## Pass 2

Second pass: every one of the 110 entries in gloss.json and its 7 broadenings checked against the word, its use in units.json
(w / l / i / n) and the master entries of related forms (stems, particle forms, Sanskrit); the master entries of the 199 known
forms of this part read by script against the units where each occurs; then all 31 units read again from the original through
`l` to `i`, with every cross-reference in the notes to earlier parts checked by script against their units. Both files were
edited by script (ensure_ascii=False, indent 1, no final newline; a round-trip of each unedited file was checked to be
byte-identical first). `w` is unchanged. Key check by script: the gloss.json keys equal the part's words not in the master
glossary (110 of 309), none unused, none already in the master; every broadening is of a master key used here and begins with
the master entry whole + " · ". Letter check: 31 units, 3825 letters, PASS (sha256 of the pinned source matches).
hooks.assemble + hooks.validate in memory with gloss.json merged as `r3.py build` merges it (validate reading the glossary as
it would be written; nothing written): no error, no WARN; no "no glossary entry" left. `r3.py build` was not run, because it
writes the story, glossary.json and stories.json.

### Changes: gloss.json

- gloss དཔའ་བོ · Sanskrit · minor · "hero (dpa' bo; Sanskrit ḍāka)": dpa' bo renders vīra; ḍāka is the male mkha' 'gro · now
  "hero (dpa' bo; Sanskrit vīra): in the tantras the male companions of the sky-goer women".
- gloss དཔའ་མོ · Sanskrit · minor · "heroine (… Sanskrit ḍākinī)": ḍākinī is mkha' 'gro ma (the glossary's own entry), not
  dpa' mo · now "heroine (dpa' mo, the feminine of dpa' bo 'hero'): in the tantras a female companion of the sky-goers".
- gloss ཁེངས་པ · stem · style · "filling, being filled" without the verb's class · now "filled, full (khengs pa, the
  intransitive 'to be full'; the transitive 'to fill' is 'gengs)".
- gloss བཀོལ་གཅོད · stem · style · bkol given as a bare verb · now "bkol, past of 'khol 'to put to work'".
- gloss འདས་པ · stem · style · no stem · now "'das, the past stem of 'da' 'to pass beyond', + -pa".
- gloss བཏང་ཅིག · stem · style · added "the imperative stem proper is thong" (gtong / btang / gtang / thong), as བཟུང་ཅིག names zung.
- gloss བཟུང · stem / general · style · "in bzung cig it stands as 'hold!'" spoke of another key (བཟུང་ཅིག) and a line · now the
  four stems "'dzin / bzung / gzung / zung" and the example only.
- gloss སྒྲིལ་མ · parts · style · "(sgril ma)" gave no parts · now "sgril 'to roll, to wind' + -ma".
- gloss ཁོན · sense · style · khon is itself a word ("grudge, resentment"); the entry now says so and that it gives no sense here,
  beside the two slips it already proposed.
- gloss མཁའ་འགྲོ · general · style · "written here without the feminine -ma" pinned to a line (the form is also in u. 5 and
  u. 22) · now "also written mkha' 'gro ma, with the feminine -ma".
- gloss རིགས་འཛིན · general · style · "here only" pinned the entry to this part · removed.
- gloss ཁྱེད · sense · style · "you (khyed)" did not say it is the politer and plural word (the master's ཁྱེད་རང "the more polite
  'you'") · added.
- gloss དེ་རུ · grammar · style · "-ru 'to', the form of -r after a vowel" implied -r itself is not after a vowel · now "-ru 'to',
  a form of the particle la used, like -r, after a vowel".
- gloss ཐོད་རྔ · wording · style · "two-faced drum" · now "double-headed drum".

### Changes: units.json

- u. 5 · n · minor · "dpa' bo and dpa' mo … (Sanskrit ḍāka, ḍākinī)": as the gloss above · now "(dpa' bo, Sanskrit vīra), in the
  tantras the male and female companions of the sky-goers".
- u. 7 · n · minor · fact. "ldir, which the print has twice on the next page": u. 7 is on 74.5; ldir ba and ldir stand only on
  p. 76 (u. 15–16), by script on the established file · now "twice two pages on (76), spelt ldir".
- u. 10 · n · style · fact. "gsal la dwangs pa, bkrag la nyam nga ba … as in 007": 007 has bkrag la nyam nga ba'i only; gsal la
  dwangs pa is in 004–006 (by script) · now "as on the days before (gsal la dwangs pa in 004–006, bkrag la nyam nga ba'i in 007)".
- u. 15 · n · style · fact. "chos kyi rang sgra … as in 003": 003 has chos nyid kyi rang sgra (twice) · now "as chos nyid kyi
  rang sgra in 003".
- u. 6 · n · style · "a small two-faced drum" · now "double-headed", as the gloss.

Severity count, pass 2: major 0 · minor 4 · style 15 (19 change lines: 14 on gloss.json, 5 on units.json; no broadening added).

### Checked and confirmed (no change)

- Stems and labels in gloss and notes, each checked: bcad past of gcod (gcod / bcad / gcad / chod); bsags past of gsog
  (gsog / bsags / bsag / sogs); bzung past of 'dzin and zung its imperative; btang past of gtong, with the present after ma in the
  other recension's ma gtong zhig; drang future, drangs past, drongs imperative of 'dren; bsgral past (and future) of sgrol;
  skyol imperative of skyel (skyel / bskyal / bskyal / skyol); byon past of 'byon; btab past of 'debs; skyes past of skye; byed
  present (past byas); skye present in skye bar; mdzad and mkhyen respectful; gi / gis after -g; ru after a vowel; -go after -g;
  -lo after -l; the future before purposive du (u. 9 note).
- The seven glosser broadenings are needed and begin with the master entry verbatim: ཤར "east" (u. 1–4 directions); ས bhūmi
  (u. 1, hedged in the note); ཆོས "reality" (u. 15, house rendering); ཚོགས "accumulation" (u. 23); གསོལ "wear" (u. 5); ཆད་པ
  "punishment" (u. 9); ཙམ "as much as" (u. 7, 15).
- Hedges kept where the notes mark doubt: ཞིང་ལྤགས, མི་གསུར, འདིར་བ, ཁྲ་ཤིག་ཤིག་པ, མེར་མེར་བ, ཕྱམ་ཕྱམ་པ, བསོ་སྒྲ, བཀོལ་གཅོད, མདུན,
  བརྩེ་གཅིག་ཏུ, ཁོན, ཐལ་ལོ, མཚོན་སྐུད, ཨ་ཙ་མ་ར; the master's ཐོབ་ཅིག and འདིར (the 003 guess) as used here.
- Known forms read against their use here: ཚེ (life in u. 2, time in u. 26), གནས (place), གཅིག (one, a), ཅིག, གི, གིས, ཀྱི (the
  master's "perhaps … for kyis" covers u. 26 line 5), ཀྱིས, ཀྱང, ཡང (even, though), ལ ('and' between qualities in u. 10, 16, after
  gtod in u. 21, 25), ཞིང (clause particle in u. 1–4), མ, མི, ཟིན་པ (caught), སྟོང (thousand), ལྡིར, དེ (after ngo 'phrod in u. 28),
  རིགས (families, kinds), ངོ / འཕྲོད split. All cover their use; no further broadening is needed.
- All 31 units re-read: pass 1's changes are sound (bcad and bsags stems, u. 30 `i` without the copula, ཡུམ་ མཆོག, the hedged
  line 5 of the prayer, death-point's between). Cross-references checked by script: 007 has byon par 'dug gis (u. 22), chags su
  'ong bas (u. 13), bag chags dbyings su dag pa (u. 10); bsu ba la 'ong in 004–007 (u. 8); zug nas 'ong in 003–006 (u. 11).
  Verse line 1 and 5 of the prayer have nine syllables after kyai ma, as the note says. `i` read again for remembered
  wording: none found.

### Findings considered and refused

- u. 9 · `l` "punishment cutting come" for chad pa bcad du 'ong, against a purposive "to-cut": 007 renders bsgral du gsol
  "freeing I-pray" in `l`; the note gives "to impose". Kept for consistency.
- u. 27 · ces after skyol (-l, where the rule gives zhes): it opens a new unit after ༔, the usual place of ces in this print, and
  no note claims a rule. Kept.
- gloss ཆོས་སྐྱོང་བའི "of those who protect the teaching" against the adjectival use in u. 5 ("dharma-protecting's guardians"):
  both readings are inside the entry ("of those who protect" = "protecting"), and pass 1 settled the division. Kept.
- gloss རོལ་དུ, གནས་པའི, ཉི་ཤུ་རྩ་བཞིའི and others with an example from this part: the master entries carry examples in the same
  way; none is pinned to a single line's reading beyond the example. Kept.
- gloss དཔེ་བྱད, དུར་ཁྲོད without Sanskrit: not required by the entry format. Kept.
