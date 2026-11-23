# Review — bardo-thodol-013 (pp. 115–121)

**units.json is now the master.** It was edited in place by script. The drafter's scratch build013.py is stale and must
not be re-run, because it would overwrite these edits.

## Pass 1

**Sources checked against.** conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md (the pinned print with its 12
`# fix:` lines), establish-log.md, the pilot (units.py, ../../../bardo-thodol-001.json), the published parts 002–012
(searched by script: w, l, i and n), 012's review, glossary.json, and the other recension (source/raw/bowiki-other-recension.txt),
used as a control witness only. No modern translation was opened. The 118.1 line (སྒྲ་རུ་མི་ལྡང) was checked on n119.jpg at ×4.

**Reading.** All 29 units and the about were read word by word: original → `l` → `i`.

**Stems and endings.** The labels in the notes were checked against the forms. These stems were checked:
- btang / gtong; spangs / spong; bsgral / sgrol (future with du gsol, as 004); skyol / skyel; phyungs, the imperative of 'byin
- shog / 'ong; 'brang / 'brangs; bskyab / skyob; byas / byed; bstan / ston; bsgom, the future of sgom; bya / byed
- bcang / 'chang; shi / 'chi; bsags / gsog; skyes / skye; bltas / lta; drangs / 'dren; gtad / gtod; babs / 'bab; zhus / zhu

These endings and particles were checked: ces after -g; zhing after a vowel and after -ng; shing after -s; yi after a vowel;
ru after a vowel; -pas; -bas; the sentence-ending -o (do, to, ro, so, -'o); 'am as its own syllable; and zhig after -ng.
All the labels are right. One point was left unsaid: ma with the past stem in a prohibition (u. 0). It has been added.

**Marks, misprints and fixes.**
- The 21 `[?]` marks of the log are each called doubtful in their unit:
  - u. 0: zhig
  - u. 2: spangs
  - u. 3: shugs, nga
  - u. 6: pas
  - u. 11: pas, 'og
  - u. 12: spyir
  - u. 13: 'ong
  - u. 15: do, khro'i
  - u. 16: gson
  - u. 19: byas
  - u. 22: klog
  - u. 23: byang ba, 'phrad, shong
  - u. 26: bdar
  - u. 27: su rya
  - u. 28: pa, dras
- The three misprints (u. 3, u. 6, u. 14) open their notes with the rule-5b sentence.
- The other nine fixes are each named in their unit:
  - five tshegs: u. 1, 14, 15, 18, 24
  - four contractions: u. 6 'char, u. 13 'ong ngo, u. 25 rdzogs so, u. 28 zhus so
- `v` is set on u. 2–7: 24 lines, line count equal in w / l / i. The `p` flags fall at sensible breaks.

**House renderings.** These were checked:
- bar do: "the between" in `l`, "bardo" in `i`
- ngo sprod: "face-introduction" / "pointing-out"
- 'od gsal: "clear light"
- chos nyid: "reality-itself" / "reality"
- khrag 'thung: "blood-drinker"
- ngo shes: "face-know" / "recognise"
- longs sku: as in 006

rig pa in `l` was "awareness" twice, where every published part has "knowing" (fixed below). The cross-references were checked,
and all hold:
- 003: mos ba gyis la, 'jigs snang, rang snang
- 004: the yi read as yis, bsgral du gsol
- 006: longs sku, zhes bya ba yin
- 008: tshogs kyi read as kyis, tshogs (ma) bsags
- 009: med pa'i thabs med, de'i phyir, srid pa'i bar do, thos pa tsam gyis, bskyed rdzogs
- 012: ma gtogs, the call formula
- 002 u. 36 / u. 49 for lam gyis

**Word division.** This was checked by script against the glossary keys and the `w` of 001–012. Each run of 2–3 words was joined
and looked up, and each word was split and looked up. The published parts put -du / -tu / -su on their word everywhere
(ནང་དུ, ཐོག་ཏུ, plus about 80 other forms), and the glossary has ལམ་གྱིས "in a flash" as one word. Five places in 013 broke
this rule (below).

**Edit and checks.** units.json was edited by script (ensure_ascii=False, indent 1, no final newline). The round trip was
checked to be identical first. Letter check: all `w` joined, with spaces and ' / ' removed, against hooks.letters() for
the part. Result: 29 units, 3291 letters, EQUAL.

### Changes

- u. 13 · w / l / n · minor · ལམ་ གྱིས was divided as two words, but `l` and the note read it as "in a flash". The glossary
  has ལམ་གྱིས as one word for that sense, as the pilot and 002 u. 36 divide it; ལམ་ གྱིས as two words is 002 u. 49's "by the
  path" · Now ལམ་གྱིས. The note says it is written as one word, and that read as two it could be "by the path".
- u. 14, 19, 20, 28 · w / l · minor · རིག་ཐོག་ ཏུ, རྣ་ལམ་ དུ, ནང་ དུ, དྲུང་ དུ had -tu / -du as free words, against the
  convention (fused endings stay on the word) and every published part (ནང་དུ 011 u. 26; ཐོག་ཏུ 002, 005, 006) · Now
  རིག་ཐོག་ཏུ, རྣ་ལམ་དུ, ནང་དུ, དྲུང་དུ, with `l` hyphened to match: "knowing-top-on", "ear-path-in", "inside-in", "presence-in".
- u. 27 · n · minor · `l` read de'i gu ru literally as "His guru", while `i` read "from him … to Guru Sūryacandra". The note
  did not say why the two differ. Taken literally, Sūryacandra would be Chos rje Gling pa's teacher, against babs, "came down",
  and rim par · The note now says that the idiomatic line reads de'i as des, "from him" (the other recension's reading), and
  gu ru as the title. `l` kept literal.
- u. 15 · l / n · minor · `l` had "the between in" for las, which the note itself explains as "from, out of" · `l` now
  "the between from". The note adds that the other recension has la.
- u. 0 · n · minor · stem. ma btang zhig is a prohibition with the past stem, and the note did not say that a prohibition
  usually takes the present stem · Added "a prohibition usually has the present stem (ma gtong zhig), and the print has the past".
- u. 17 · n · minor · "dus gsum du … here most likely the three sessions of the day, not past, present and future" was
  asserted without support · Now gives both senses: the periods of the day seem meant with ma chag par, "but this is not sure".
- u. 3 · n · minor · recension notes were vague ("words this line differently"). The note now says what the other recension
  has:
  - gcig par for gcig pur;
  - the 8-syllable third line, set against the other recension's nine-syllable sangs rgyas rnams kyis thugs rjes shugs
    phyungs nas, which bears on the drafter's metre flag.

  It also says why 'jigs nga stays one word (a two-syllable word with a doubtful second syllable).
- u. 10 · n · minor · "the other recension words the opening differently" was vague · Now gives the reading: des ni, "by that"
  (the prayer as the means), with ni added after las 'phro.
- u. 22 · n · minor · "gson dus su … where the other recension differs" was vague · Now gives gson po'i dus su (the print's
  own wording in u. 14–16) and de'i phyir na.
- u. 21 · n · minor · "bar dor rig pa … where the other recension differs" was vague · Now gives bar do'i rig pa.
- u. 16 · n · minor · "places them differently" was vague · Now says where khyad par (du) and shin tu stand in each recension.
- u. 28 · n · minor · "spells the name differently" was vague · Now gives ga ga dharma pa mu dras. "no closing dedication, as
  the other recension does" read the wrong way round · Now "where the other recension has one (beginning 'di bris dge bas …)".
- u. 7 · i / n · minor · `i` read "the elements of the five elements", where `l` and the note have "realms" · `i` now "the
  realms of the five elements". The note adds that sgra ru may stand for dgra ru, "as enemies" (dgra ru ldang, "rise up as an
  enemy"), which fits ldang and the other recension's sdang. The image was checked ×4: it plainly has སྒྲ. Nothing is changed in
  `w`, and `i` keeps "sound(?)".
- u. 5 · n · style · The note now says that the other recension has lha yis (supporting yi read as yis) and dbang gis.
- u. 6 · n · style · The note now says that the other recension has bskyab, which confirms the drafter's skyab = bskyab, and
  gives the paradigm skyob / bskyabs / bskyab / skyobs.
- u. 6 · i · style · "When I suffer the karma of my habitual tendencies" dropped sdug bsngal, the object of myong · Now "When I
  undergo the suffering of the karma of my habitual tendencies".
- u. 16 · i · style · The yang of gson po'i dus su yang was untranslated · Now "while one is alive too".
- u. 13 · l · style · bem rig was "matter-awareness" in `l`; the house rendering of rig pa in `l` is "knowing" · Now
  "matter-knowing".
- u. 26 · n · style · The note now gives the other recension's ri bo ri lha bran gyis gar byed pa. That reading suggests that
  ri lha, "mountain god", may belong together, giving "like the mountain god's servants(?) making a dance". `w` division
  (རི་ ལྷ་ བྲན་) and `i` are kept, with the uncertainty.

Severity count: major 0 · minor 13 · style 6 (19 change lines). The four division fixes of u. 14/19/20/28 count as one line.

### Refused

- u. 3 metre (drafter's flag): the corrected third line has 8 syllables. The doubled rgyas is a pinned `# fix:`, and the log
  calls it certain. The other recension's nine-syllable line differs in three places (kyis, rjes, nas), so the print has not
  simply lost one syllable that could be restored. The fix stays, and the note now gives the other recension's line.
- u. 3 'jigs nga as one word (drafter's flag): kept. nga is not a free word. The syllable stands where the second syllable of
  'jigs snang / 'jigs pa should be, and the note gives both candidates.
- u. 0 ཐུགས་རྗེས་ མ་ བཏང་ཞིག་ གྱིས་ ལ (drafter's flag): division and reading kept. They are consistent with 012's
  བཟུང་ཞིག / བོས་ཅིག and with the free gyis ("do!") of the other recension's ma gtang gyis la. The note was made fuller (see
  above).
- u. 6 skyab tu gsol as bskyab (drafter's flag): right. The other recension has bskyab; note only (above).
- u. 13 lam gyis "in a flash" (drafter's flag): kept as the reading. chos nyid … 'ong ngo with an adverb fits, and the
  other recension agrees on the words. Only the division was changed.
- u. 5 yig drug (drafter's flag): the note says that the text does not name the mantra, and that it is usually
  Avalokiteśvara's. This is fair, so it was kept. The colophon rule ("only what the text says") applies to the colophon
  notes, not to this one.
- u. 26 ལྷ་ བྲན་ གར་ བྱེད་པ (drafter's flag): the division was kept as four free words. Neither ri lha nor lha bran is
  certain, and a join would claim more than the text shows. The note now gives the alternative.
- u. 27 de'i gu ru (drafter's flag): de'i was not emended to des in `w` or `l`, because the print is followed (conventions).
  The note was rewritten (above).
- u. 17 dus gsum du as one word (drafter's flag): kept, as a fixed phrase with fused -du, like dus su.
- u. 16 de bas na note "(de, 'that'; bas, 'by'; na, 'then')": bas is better called "than/from" (ba + -s) in this set phrase.
  The meaning given, "therefore", is right, so it was kept. The glosser should not copy "by".
- u. 24 `i` "simply by not letting wrong views arise": "letting" adds a little agency to ma skyes pa, but the sense ("only by
  wrong views not arising") holds. Kept.
- u. 23 `l` "If met if": clumsy, but it is the house treatment of gal te … na in `l`. Kept.
- u. 12 `i` "many are somewhat confused": a fair reading of bag re 'khrul ba mang bas. Kept.
- `i`: no English that reads as remembered rather than built from the words was found.
- about: accurate to the part. Kept.

## Pass 2

Second pass. Each of the 111 entries in gloss.json was checked against the word and its use in units.json (w / l / i / n),
against the verb stems and against the master entries of related forms (དབྱིངས་ཕྱུག་མ, ནམ་མཁའི་དབྱིངས་ཕྱུག་མ, བཟུང་ཞིག, རིག་པ,
བསྟན་པ, བབ, ཞུས, བསགས་པ). Stems checked and right: btang / gtong (with bzung zhig as precedent for past stem + zhig), spangs /
spong, phyungs / 'byin ('byin / phyung / dbyung / phyungs), 'brang / 'brangs, bskyab / skyob (skyab tu), bcang / 'chang,
bstan / ston, byas / byed, shi / 'chi, bsags / gsog, bltas / lta, babs / 'bab, drangs / 'dren, zhus / zhu, sel (present), ldang
(present). Case endings checked: -tu after -g / -b, -du after -m / -n / -l, -su after -s, -ru after a vowel, -bar / -par,
-pas / -bas, -'i. Coverage by script: novel-forms.json has 111 keys, all in gloss.json, none empty, no extra keys; every word of
units.json (punctuation stripped) is in glossary.json or gloss.json. The 210 known forms were read against their uses here;
two master entries fail this part's use (གཏད, སྐུ་གཟུགས, below); the rest cover it (ཀྱི read as kyis, ལས 'from', འདིར 'at this',
ཡང 'again', དེ 'he', ཐོབ 'having gained', ཅིག in lan cig, གནས 'place', ཡོད་པས after nas as in 012).

Then all 29 units and the about were read again, original → `l` → `i`, with pass 1's changes. Rule-5b sentences open the notes
of u. 3, 6, 14; the 21 `[?]` places are each called doubtful in their unit; rig pa is "knowing" in `l` (u. 14, 21; bem rig
u. 13); house renderings hold. No `w` was changed. Letter check (all `w` joined, ' / ' and spaces removed, against
hooks.letters() for the part): 29 units, 3291 letters, EQUAL. gloss.json and units.json were edited by script
(ensure_ascii=False, indent 1, no final newline; round trip byte-identical checked first).

### Changes: gloss.json

- gloss ཤོག · stem · minor · "(shog, the imperative of 'to come')" did not name the verb · now "shog, the imperative of 'ong 'to
  come', 'come!'; after a verb it closes a wish".
- gloss དབྱིངས་ཕྱུག · sense · minor · "phyug 'rich, lady'": phyug is 'rich'; 'mistress' belongs to phyug ma, as the master
  entries དབྱིངས་ཕྱུག་མ and ནམ་མཁའི་དབྱིངས་ཕྱུག་མ say. "the consort goddesses in the daily prayers" was pinned to the text ·
  now "(dbyings 'expanse' + phyug 'rich', as in phyug ma 'rich one, mistress'; short for dbyings phyug ma): the name of a consort
  goddess, and of the female deities as a host".
- gloss འམ · wording · minor · "written as its own syllable after a final" presented the print's spelling as the rule (after
  gsum the particle is usually mam) · now "usually joined to the word or matched to its final, gsum mam, but also written as its
  own syllable".
- gloss གྷ་གྷ་དྷརྨ་པ་མུ་དྲས · form / doubt · minor · "the print has dras with -s" neither glossed the -s nor marked the doubtful
  form · now "(gha gha dharma pa mu dra + -s 'by'); as printed, uncertain (the other recension has ga ga dharma pa mu dras)".
- gloss སྒམ་པོ་བདར · doubt · minor · "a mountain's name; bdar is doubtful" (the text calls it the place whose mountain it is) ·
  now "as printed, uncertain: Sgam po bdar, a place name (the other recension has sgam po gdar)".
- gloss བྲན · wording · style · "as printed, uncertain in the phrase of the colophon" pinned a line's doubt to a clear word · now
  "servant, slave (bran)"; the note (u. 26) and `l` "servants(?)" keep the doubt.
- gloss སྒྲ་རུ · wording · style · "as printed, uncertain where it may stand for dgra ru" read as of u. 7 only (u. 5 has the plain
  sense) · now "where 'sound' gives no sense, perhaps for dgra ru 'as enemies' (uncertain)".
- gloss བསྟན་ཏོ · ending · style · -to after -n not explained (the rule gives -no) · now "the sentence-ending -to, the form after
  bstan, from its old spelling bstand".
- gloss ཆག་པར · stem · style · "chag 'to break'" unnamed stem, transitive gloss · now "chag, past of 'chag 'be broken, break off'".
- gloss བེམ་རིག, རིག་ཐོག་ཏུ · house · style · rig pa glossed "awareness" only; master རིག་པ and the house `l` have "knowing" · now
  "rig pa 'knowing, awareness'" (bem rig "matter and knowing").
- gloss འབྱུང་ལྔའི · wording · style · "'byung 'element'" · now "'byung, short for 'byung ba 'element'".
- gloss དེད · wording · style · "ded, from 'ded" vague · now "ded, taken as a noun from 'ded 'to drive, to chase'".

### Changes: __broaden__ (master entries)

- གཏད · sense · minor · master "aimed, directed, placed toward (past of gtod)" does not cover u. 27 bka' dang lung gtad,
  "entrusted" · added " · handed over, entrusted (gtad, past of gtod): bka' dang lung gtad 'entrusted the word and the
  transmission'".
- སྐུ་གཟུགས · sense · minor · master "image of a deity, a statue or painting" does not cover u. 4 (the forms in which the deities
  appear in the bardo) · added " · bodily form, the form in which a deity appears (sku 'body', respectful, + gzugs 'form')".

### Changes: units.json

- u. 16 · n · minor · de bas na explained "(bas, 'by')", as flagged in pass 1; bas here is the ending of comparison, 'than, from'
  · now "(de, 'that'; bas, 'than, from', the ending of comparison; na, 'then'): 'from that, then'".
- u. 5 · l · style · "all six-syllables' sound-into": the Tibetan yig drug sgra ru has no 'of' · now "all six-syllable sound-into".
- u. 7 · n · style · "'byung lnga'i khams, 'the elements of the five elements'" was left when pass 1 changed `i` to "realms" · now
  "'the realms of the five elements' (khams, 'realm, element')".

Severity count: major 0 · minor 8 · style 9 (17 change lines; grouped entries counted as one line each).

### Refused

- gloss བཏང་ཞིག "let go!" with the past stem btang: kept. It matches master བཟུང་ཞིག (past stem + zhig as a command); the
  note (u. 0) says a prohibition usually has the present stem.
- gloss ཕྱུངས, སྐྱབ་ཏུ, བཅང་བར, འབྲང: paradigms checked; right.
- gloss ཚོར་བས "by hearing": kept beside "by perceiving"; tshor is used of taking in by the senses, hearing included.
- gloss ཉི་ཟླ་སངས་རྒྱས, ཀརྨ་གླིང་པས, ཆོས་རྗེ་གླིང་པ: names lead with the name, as the master's names do (ཕྲ་མེན, བརྒྱ་བྱིན); the
  family links given are the colophon's own.
- __broaden__ འོང་ངོ "will come" for u. 13 "comes": not needed; 'ong 'come' is in the entry, and the present reading is the
  ordinary range of the form.
- __broaden__ ཡོད་པས for 'khyams nas yod pas: not needed; 012 used the master entry for the same phrase, and the note explains it.
- u. 24 `i` "by not letting wrong views arise": kept, as in pass 1.
- `w`: no division changed; no key changed.
