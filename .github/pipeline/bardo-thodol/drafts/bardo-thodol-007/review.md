# Review — bardo-thodol-007 (pp. 63–72)

## Pass 1

Checked against conventions.md, QUESTIONS.md, runbook.md and ../run3/RUNBOOK.md (Reviewer), packet.md (the pinned print,
its 23 `# fix:` lines and the establishment log), the reader logs in readings/, units.py, hooks.py, the pilot
bardo-thodol-001.json, the units of 002–006, 006's review.md, glossary.json, and both control witnesses in source/raw/
(the passage is at dzogchengonpa-kha.txt ll. 262–308 and in the other recension from ཀྱེ་རིགས་ཀྱི་བུ་སྐུ་དེ་དག་མི་ཆེ་བ to
…མཛད་པ་ཞིག་འཆར་དུ་འོང་ངོ). All 41 units were read word by word, from the original to `l` to `i`. Every grammatical label in
the notes was checked against the form, and every other-recension claim in the notes against the stored text. Every division
was checked against conventions.md "What the page shows" and against how 001–006 divide the same words, by script over all
their `w`. Unit numbers are 1-based, as in the drafter's list.
units.json was edited in place by script (ensure_ascii=False, indent 1, no final newline, as the file was written; a
round-trip of the unedited file was checked to be byte-identical first). No `w` was changed. Letter check (all `w` joined,
' / ' and spaces removed, against `hooks.letters()` for the part): 41 units, 5079 letters, PASS. Verse line counts w / l / i
are equal (u. 30: seven lines each). hooks.assemble + hooks.validate report no error other than "no glossary entry" (156:
the glosser has not run yet), and no WARN.

### Changes

- u. 17 · l, i, n · minor · drafter's doubt 7. `l` had "Those (plural)-of(?)", and the note read the print's kyi as if it were the
  other recension's ni ("these are what is called"). kyi reads plainly as it stands: de rnams kyi ye shes bzhi sbyor gyi snang
  ba is "the vision of the four wisdoms joined of those", the five families from whose hearts the lights came (u. 4) · `l`
  now "Those (plural)'s wisdoms four joined's appearance"; `i` "this is called the vision of their four wisdoms joined; it is
  what is called the path …"; the note gives kyi as 'of', and ni in the other recension, with the sense close either way. The
  sentence "The text does not explain the name: the four lights … are a path by which one passes into Vajrasattva" said
  first that there is no explanation and then gave one. It now reads "…; perhaps the four lights, joined, are a path that leads
  within Vajrasattva".
- u. 20 · l, i, n · minor · drafter's doubt 8. 'gyur ba med par yid ches was taken as "trust unwaveringly". But -par / -r before
  yid ches regularly marks what is trusted ("trust that it is so"), and the other recension says this outright: lam 'gyur ba
  med pa yin par yid ches · `l` now "path change without-as trust having"; `i` "you will trust that the path of reality,
  wholly pure, does not change"; the note gives this reading, with the other recension, and keeps "trust unwaveringly" as
  the other possible reading.
- u. 28 · n · minor · stem. "byon, the respectful verb 'to come', with one form for every tense" is wrong: the verb is 'byon
  (present and future) / byon (past and imperative). The other recension's 'byon par 'dug gi shows the present · the note
  now reads "byon, the past (and imperative) stem of 'byon", and the other recension's reading is marked "with the present
  stem". Also, "'od zer gyis … marks them as those who come" put the ergative on the intransitive byon. gyis marks the
  light-rays as the doers of 'dzin pa, "holding" · now "marks them as the doers of 'dzin pa, 'holding': it is the light-rays
  that hold, and that have come".
- u. 31 · n · minor · drafter's doubt 10. The note ended "The form without -s is kept as printed", which implies an irregular
  form. sangs rgya'o is regular: rgya is the present stem of sangs rgya ba, sangs rgyas the past (and the noun "buddha") · the
  note now gives the stem and says that the other recension has the past, sangs rgyas so. The establish log's "(kept)" is
  right: nothing was to be corrected.
- u. 36, 40, about · l, i, n · minor · drafter's doubt 14. mkha' spyod was "Sky-Going" in `l` and "Sky-Goers" in `i`. In u. 41,
  mkha' 'gro ma is "sky-goer-woman" in `l` and "she who goes in the sky" in the note. So two different Tibetan words had the
  same English in one part · mkha' spyod is now "Sky-Faring" (`l` "Sky-Faring's realm", `i` "the pure Sky-Faring realm", "the
  Sky-Faring realm"; spyod "to move about, to enjoy" is kept in the note, Sanskrit khecara), with a note that it is not the
  same word as mkha' 'gro ma. The about and u. 40's quotation of the other recension follow.
- u. 2 · i · minor · drafter's doubt 3. "These forms come in pairs, five and five, filling the whole space" added "the whole
  space", which the text does not say. khyab pa is "pervaded, taken up throughout" by the pairs, as `l` and the note have it ·
  now "These forms, too, are pairs throughout, five and five, and each group of five has a rim made of clusters of the five
  lights:". 'od lnga'i is "of the five lights", as `l`, not "of five colours".
- u. 3 · l · style · sems dpa' / sems ma were "heroes" / "heroines" in `l`, where 004 u. 16, 40, 005 u. 21 and 006 u. 1 have
  "bodhisattva" / "female-bodhisattvas" (and the note and `i` here say bodhisattvas) · now "family's bodhisattvas",
  "family's female-bodhisattvas".
- u. 10 · l · style · "discerning's wisdom" dropped so sor, which 005 u. 22 gives as "individually discerning's wisdom" · now
  "individually-discerning's wisdom". `i` "the discerning wisdom" is 005's and stays.
- u. 21, 27 · i · style · each continues an `i` that ends in a comma (u. 20) or in "So" (u. 26), but began with a capital
  ("Awareness", "Do not act so") · now lowercase, as u. 7, 11, 14 and 37 are.
- u. 22 · n · style · 'ong te has te where the rule gives ste after -ng. This is the print's habit (QUESTIONS.md, 002), and the
  only irregular one of the part's te/ste/de; the note did not say so · one clause added.
- u. 30 · l, n · style · drafter's doubt 9. Line 5 ma dag rigs drug 'od lam bsgral du gsol has no las, and `l` showed no doubt ·
  `l` now "light-paths (from?) freeing I-pray". The note's "bsgral, the future stem of sgrol" now reads "past and future
  stem (sgrol / bsgral / bsgral / sgrol), future with du gsol and past in bsgral nas", since the next line has the past.
- u. 38 · n · style · "and `i` leaves the word out" put pipeline jargon in a note for readers · now "the translation leaves the word
  out".
- u. 41 · n · style · drafter's doubt 14. "Lord of the Lotus Dance" takes padma with gar. The name parses just as well as padma +
  gar gyi dbang phyug, "Lotus, Lord of Dance" · the rendering is kept, and the note now gives the other parse.
- about · style · "The best, the middling and all the rest are freed so". The print has no rab, "the best" (u. 31 says so),
  and its third group is thams cad, "all" · now "Those who make it are freed, the middling by fierce devotion, and all through
  its power".

Severity count: major 0 · minor 6 · style 8 (14 change lines).

### Drafter's doubts, adjudicated

1. u. 4 མེ་རེ་རེ: kept, joined as the doubled-sound word of 003 u. 31 ("shimmering"). The reader log confirms that the image
   plainly has མེ (×7). The other recension has only རེ་རེ. A stray མེ in front of re re "one by one" is the other way to read
   it. The note gives both readings and says that it cannot tell which is right; `l` has "(?)". `i` uses "shimmering" without
   a hedge, which is acceptable with the note.
2. u. 4 སྦ་ཐག་དྲིལ་བ "a cord of cane, twisted": kept as a guess, which the note says it is ("the likeness is not sure in
   either"). sba "cane", thag "cord" and dril "rolled, wound" are each sound. The other recension's བ་ཐག་སྦྲེལ་བ is given.
3. u. 2 ལྔ་ལྔའི་ཟུང / ཁྱབ་པ: the reading "pairs of five and five" is kept, and the note says that the sense is not sure. "Filling
   the whole space" was removed from `i` (above). The other recension's brgyan pa is in the note.
4. Divisions. Checked by script against 001–006:
   - བཅས་ཏེ as 001 u. 17 and 005 u. 44.
   - ཆགས་སུ as བྲོས་སུ (004–006).
   - ལྔ་རུ as ས་རུ (004–006).
   - བསྐྱལ་དུ as བསྒྲལ་དུ.
   - སྟེང་དུ as མདུན་དུ, དུས་སུ, ཞིང་ཁམས་སུ.
   - འཁྱམས་དུ as the fused la-don.
   - འོ་རྒྱལ་ལོ one word: the fused -lo stays on its word, as ཕྱག་འཚལ་ལོ in the pilot. 003's འོ་བརྒྱལ་ ནས differs only in that
     nas is a free particle.
   - ཆ་མཉམ་པ, བཞུགས་ཚུལ, གདན་ཁྲི, རང་རང, ལྔ་ལྔའི / ལྔ་ལྔས, ལྔ་ཚན, ཁ་སྦུབ་པ, ཙམ་པ (as the pilot's ཙམ་དུ), ཤས་ཆེ་བ (as 006's ཚན་ཆེ),
     བླ་ན་མེད་པ, བདེ་བར་གཤེགས་པའི (a title, as བཅོམ་ལྡན་འདས), པདྨ་གར་གྱི་དབང་ཕྱུག (names whole, as 006), ཡུམ་ཆེན: all stand.
   - The splits ཆ་ འཛིན་པའི (a verb with its object), མི་ རྟོག་བའི (as མི་ སྣང, མ་ བྱེད), གཉིས་སུ་ མེད་པར (as ཡེ་ནས་ མེད་པ),
     འགའ་ ཞིག (as གཞན་ ཞིག), གང་ ཞེ་ ན (as ཡིན་ ན), བྱོན་པར་ འདུག་ གིས (as 002 u. 17 འོང་བར་ འདུག་ གིས): all stand.
   - རང་ ངོ་སྤྲད་པ (u. 38) beside རང་ངོ་ ཤེས (u. 32, as the pilot's u. 31): both stand. In u. 32 rang ngo, "one's own face", is
     the object of shes. In u. 38 ngo sprad is the house's one word everywhere, and rang is the doubtful word (5).
5. u. 38 རང "self(?)": kept, with "(?)" in `l`. The note gives the other recension's yang and says that the sense is
   uncertain. The translation leaves the word out (the note's wording now says this without jargon).
6. u. 22 གཅིག "together, at once": kept, with "as-one(?)" and "the sense is not sure". The stored other recension has neither
   drug kyang nor gcig, as the note says. (Reader B's log quotes a dus gcig tu from some other place. The note follows the
   stored text, which is right.)
7. u. 17 དེ་རྣམས་ཀྱི: kyi is now read as "of" (above). ཁོང་གསེང / ཁོང་སེང "inner hollow": kept. Reader B also takes khong seng
   as the usual form, and the two spellings in the print are noted in both places.
8. u. 20 འགྱུར་བ་མེད་པར with ཡིད་ཆེས: now read as the content of the trust (above).
9. u. 30: line 5 without ལས, read as "free me from" and now marked "(from?)" in `l` (above). ཡུམ་ཆེན "great mothers": right,
   the five consorts. yis is "by" after a vowel. Seven lines: counted, each nine syllables after kye ma (dug lnga drag pos
   'khor bar 'khyams pa'i tshe = 9 … dag pa'i zhing mchog lnga ru bskyal du gsol = 9). w / l / i have seven lines each.
10. u. 31 སངས་རྒྱའོ: the stem is now given (present; above). The print lacks རབ, and the note says so and what follows from it.
11. u. 28 བྱོན་པར་འདུག་གིས: the reading "have come, and so" stands, with 'dug after a verb as in 002 u. 17–18 and gis "so,
    since" as 002's note. The stem of byon is corrected (above).
12. Stems:
    - blangs, past of len (len / blangs / blang / longs): right.
    - bkag, past of 'gog ('gog / bkag / dgag / khog): right.
    - bsgral: past and future of sgrol. The label is completed (above).
    - bskyal, past and future of skyel (skyel / bskyal / bskyal / skyol): right.
    - skyor, present and imperative: right, as 004 u. 8 and 006 u. 19.
    - skyes, past of skye: right.
    - shar, past of 'char: right.
    - 'ongs, past of 'ong: right.
    - bos, past and imperative of 'bod ('bod / bos / bod / bos): right.
    - zhe as the form zhes takes before na (ce na / zhe na / she na by the final of the word before; gang ends in -ng): right.
    - 'khyams du: the rule gives su after -s. The note says so, and that the other recension also writes du: right.
    - Not on the list but checked: brgyan past of rgyan; zhog imperative of 'jog; the prohibition ma byed cig with the present
      stem; drongs (prayer) as in 004.
13. The establish log's "The other recension breaks off into another passage at 65.3" is wrong. Reader A searched for so sor
    rtogs pa'i ye shes dmar and found its first occurrence, which belongs to the fourth day (Amitābha's own day; the text that
    follows there is the hungry-ghost light, as the log says). The second occurrence is the passage of this part. It has the red
    drop (byi ru'i phor ba, gting mdangs), …rang bzhin gyis thig le lnga lngas brgyan pa, de'i mtha' dbus med pa…, and de rnams
    kyang khyod rang gi snying ka dang 'brel mar 'char du 'ong ngo, then runs on unbroken with the rest of p. 66 onward. So
    65.3–5 has a comparison. The drafter's notes to u. 10–12 (byi ru, gting mdangs, rang bzhin gyis, 'brel mar) quote it
    correctly. The establish log is not this review's file to change; see QUESTIONS below.
14. Renderings:
    - "knowledge-holder" for rig 'dzin (vidyādhara): kept. rig here is "knowledge" (vidyā), not the house rig pa "awareness",
      and the note explains it.
    - "Sky-Goers" for mkha' spyod: changed to "Sky-Faring" (above).
    - "Lord of the Lotus Dance": kept, with the other parse in the note (above).
    - "knowledge-holder of full ripening" (rnam par smin pa, vipāka): kept.
    - "discerning wisdom" (005 u. 22) and "wisdom of sameness" (005): right in `i`. `l` brought into line with 005 (above).

### Checked and confirmed (no change)

- No `# fix:` in this part corrects a misprint: 17 are line-join tshegs, 2 mid-line tshegs and 4 contractions. So no rule-5b
  note is required. The contractions are each named once anyway: ཐཾས (u. 15), རྒྱལོ (u. 25), ཐམ (u. 35), པལ (u. 36), ཚོགྶ
  (u. 36), མཁའགྲོ (u. 41), and the -གས sign at the end of རྫོགས (u. 3, confirmed in read_A-log).
- Uncertain readings are called uncertain:
  - 63.3 རྫོགས[?] (u. 3: "not sure on the image … rjogs, no word"). This is accurate to read_A-log, which reads a ར over a
    three-bar ཇ/ཛ.
  - 68.3 བས[?] (u. 25: "the letter is not sure on the image").
  - me re re (u. 4), du kha (u. 23, "the reading is uncertain"), mdun pa (u. 29), the line 5 sense (u. 30), gcig (u. 22),
    lnga lnga'i zung (u. 2), sba thag (u. 4), rang (u. 38).
- The kept readings of the log are all noted: དུ་ཁ, མེ, མདུན་པ, ཐམས་ཅད་ཀྱང against ཐ་མས་ཀྱང (u. 33: "possible, not sure"),
  མི་རྟོག་བའི, ཡིན་བས, དག་བ, ཁོང་གསེང / ཁོང་སེང, མཚེར / འཚེར, ཀྱེ beside ཀྱཻ, སངས་རྒྱའོ and འཛིགས.
- The other-recension claims in the notes were checked against the stored text, one by one. All are accurate: cha lugs, brgyan
  pa, tshom bu, dus gcig, 'ong ngo, ba thag sbrel ba, re re, dang por, nang du, no cig, mthing ka without 'od dang ldan pa and
  dper na, byi ru, gting mdangs, rang bzhin gyis, 'brel mar, shar ba / 'ong ba, rnam par mi rtog pa'i, lhod, ni, rdo rje sems
  dpa'i, khyod kyis ngo sprod kyi don, med pa yin par, dmyal ba'i, dud ka, 'ong ngo, ma byed cig, mi dmigs pa'i, pas, 'o brgyal
  lo, gdam ngag gi, 'jigs, chags tu, mdzod la, 'dun pa, yum mchog rigs lnga'i yum gyis, bar do rigs drug, rab, gnyis med du,
  sangs rgyas so, tha mas kyang, skye sgo, gsar bar, 'gro ba shas che ba zhig, 'khyams du, zhing khams nas, 'od lam gyis, yang,
  'bod, 'od khra bo shar du, thim pa'i dkyil 'khor gyi dbus su, gar mdzad cing, lta stangs.
- 004's treatment of du kha (u. 19, 21, 27) is followed in u. 23.
- Particles: yis after a vowel, ru after a vowel, -go after -g, -bo after -b, -ngo after -ng, -'am on lta bu.
- The house renderings are kept:
  - child of noble family
  - face-introduce / point out
  - knowing / awareness
  - the between / bardo
  - body of perfect enjoyment
  - lustreless / dull
  - shimmering
  - "dawning come(s)" for 'char du 'ong
  - the refuge formula, the prayer frame, and smon lam 'di skad du thob cig as the guess of 006.
- `i` was read for wording remembered from the modern translations. None was found.

### Refused

- u. 38 · join རང་ངོ་ སྤྲད་པ, to match u. 32's རང་ངོ་: ngo sprad is one word in every part, and the doubt here is rang / yang.
  Splitting ngo sprad would also break the house "face-introduce". Kept.
- ཡུམ་ཆེན joined while 004–006 split ཡུམ་ མཆོག: yum chen (mo), "great mother", is a lexical term, and yum chen lnga is a set
  ("the five great mothers"). Here mchog in yum mchog is an epithet added to yum. Kept.
- u. 5, 26, 41 · cig after a vowel (snam bu cig, med pa cig, mdzad pa cig) where the rule gives zhig: the notes make no rule
  claim, and the other recension has zhig in u. 41. QUESTIONS.md (002) already records the print's cig where the rule wants
  another form (ཉོན་ཅིག after n), and this is the same habit. Kept without a note.
- u. 4 · `i` "shimmering" without a hedge: `i` carries no question marks in the published parts, and the note states the doubt.
  Kept.
- u. 41 · `i` "he holds a curved knife and a skull full of blood": 'dzin cing could belong to the consort, but the chain runs
  on to mdzad pa cig, whose subject is the knowledge-holder. Kept.
- u. 17 · "the usual spelling is khong seng": Reader B's log says the same, and the print has both. Kept.
- u. 33 · follow the other recension's tha mas kyang: the print is followed (conventions.md), and the note gives the other
  reading and why it fits. Kept.
