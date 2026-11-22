# Review — bardo-thodol-009 (pp. 81–90)

## Pass 1

Checked against conventions.md, QUESTIONS.md, runbook.md and ../run3/RUNBOOK.md (Reviewer), packet.md (the pinned print,
its 23 `# fix:` lines and the establishment log), the three reader logs in readings/, hooks.py, tib.py, units.py (the pilot),
the published units of 001–008, 008's review.md, glossary.json, and the other recension in source/raw/bowiki-other-recension.txt
(text ga has no transcription of this print, so dzogchengonpa-kha.txt does not apply). The passage runs in the other recension
from ད་ནི་ཁྲོ་བོའི་བར་དོར་འཆར་ཚུལ་བསྟན་པར་བྱ་སྟེ to …ངན་སོང་དུ་འགྲོ་བ་མི་སྲིད་དོ, and from there on into འདི་དང་བཏགས་གྲོལ་གཉིས, where part 010 begins.
All 33 units and the about were read word by word, from the original to `l` to `i`. Every grammatical label in the notes was
checked against the form and the verb's stems. Every other-recension claim was checked against the stored text. Every division
was checked against conventions.md "What the page shows" and against how 001–008 divide the same words. This was done by
script over all their `w`: each multi-syllable word of 009 was searched as one word and as a run of words, and each pair of
adjacent 009 words was searched as one word. Renderings were compared with 001–008 by script. Unit numbers are 1-based.

units.json was edited in place by script (ensure_ascii=False, indent 1, no final newline, as the file was written). A
round-trip of the unedited file was checked to be byte-identical first. The letters of `w` are unchanged. Two places were
re-divided (u. 15, u. 30). Letter check (all `w` joined, ' / ' and spaces removed, against `hooks.letters()` for the part,
loaded as r3.py loads it; the source sha256 matches parts.json): 33 units, 4093 letters, PASS. hooks.assemble + hooks.validate
were run in memory with an empty part glossary. They gave no error other than "no glossary entry" (180; the glosser has not
run yet) and no WARN. No units are verse.

### Changes

- u. 4 · n · minor · fact. "The print writes la ma as one sign at the line end (ལམ)" is wrong. ཅིག་ལམ་འཕྲོད stands in mid-line on
  82.2; the line ends at གཅིག་ལ · now "in mid-line".
- u. 10 · n · minor · other recension. "The other recension has grol bar yang sla" is wrong. It has གྲོལ་བ་ཡང་སླ་སྟེ (checked) ·
  now "grol ba yang sla, 'freedom, too, is easy'".
- u. 16 · n · minor · stem. The note called sgoms pa "the print's spelling of bsgoms pa" but did not say what the form is.
  The verb is sgom / bsgoms / bsgom / sgoms, so sgoms is the imperative, written where the past is meant · now gives the four
  stems, the other recension's bsgoms pa, and the print's own bsgoms pa on 88.2 (u. 24).
- u. 18 · n · minor · fact. "the print joins shong and dang with no tsheg between them" contradicts the pinned text, which has
  ཤོང་དང. Reader B read a fused tsheg there and kept it, as the establish log says. What the print really lacks is the other
  recension's pa (མ་ཤོང་པ་དང) · now "the print has ma shong dang, without the pa of the other recension's ma shong pa dang (the
  tsheg after shong is fused into the headline)".
- u. 24 · n · minor · fact. "The print writes the -gs of dgos as one sign (དགོྶ)": dgos ends in -s. The sign is ས subjoined to
  the go (U+0FB6) · now "the final -s of dgos as a letter set below the go".
- u. 28 · n · minor · stem. "klog … stands for the more usual klag" turned the stems round. klog is the present stem of the
  standard verb (klog / bklags / bklag / klogs). The pilot has the same ཀློག་པར་བྱའོ (001 u. 13; master glossary ཀློག "to read
  aloud"). The other recension's ཀླག looks like the future bklag without its prefix · now "klog, 'to read (aloud)', the present stem, as in
  the pilot (klog par bya), where the other recension has klag".
- u. 31 · n · minor · other recension and grammar (drafter's doubt 89.4). (a) "The print adds this second group … the other
  recension has only the three" is wrong. The other recension has སྤྲུལ་སྐུ་ཐོབ་པ་དང་གནས་མཐོ་རུས་སུ་སྐྱེས་ཏེ (checked), so it has the
  birth in the high realms too. There it is the same people who are born there, and the print gives that birth to "others".
  (b) The other recension has གནས "abodes" exactly where the print's doubtful ཀ[?]ས[?] stands, after a clear གཞན་དག. This
  candidate was missing from the note. (c) "kas is taken as the -s that marks who is born" gave an agentive ending to the
  intransitive skye without remark · now (b) is offered as a possible reading ("others are born in the high abodes"), (c) is
  said plainly, and (a) is corrected. `l` keeps "by(?)" and `i` reads the same either way.
- u. 30 · w · style · drafter's doubt (division). ལོངས་སྤྱོད་ རྫོགས་པའི་ སྐུ was split into three. 004–007 join
  ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ(ར / རུ) as one word five times (by script; the master glossary has those keys), and the pilot joins
  ལོངས་སྤྱོད་རྫོགས་སྐུ. It is the lexical name of a body of a buddha, beside the joined ཆོས་སྐུ and སྤྲུལ་སྐུ of u. 28–31 ·
  re-divided ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ (letters unchanged).
- u. 30 · l, n · style · "enjoyment perfect's body" · now "body-of-perfect-enjoyment", as 004–007 ("as-the-body-of-perfect-
  enjoyment"). The note now says "one word as in 004–007; the pilot's homage has the short form longs spyod rdzogs sku".
- u. 15 · w · style · སྔར་འདྲིས was joined. 006 u. 23 (སྔར་ འདྲིས་ མེད་པའི) and 007 u. 19 (སྔར་ འདྲིས་པའི་ མི, the same simile) split
  it. sngar is the adverb "before", as in u. 19 here (སྔར་ མ་ མཐོང་བ) · re-divided སྔར་ འདྲིས་ ཀྱི (letters unchanged). The note
  says so.
- u. 10, 28, 29, 30, 31 · l · style · "recognition caught" for ngos zin. 003 (u. 20) and 006 (u. 21) have "recognition seized"
  · now "recognition seized" throughout.
- u. 4 · n · style · the misprint note for de ya → de la did not use the strongest evidence. The other recension has
  དེ་རྣམས་ལ (checked) · added.
- u. 4 · n · style · the note explained cig la ma 'phrod as ngo 'phrod without saying that the print has no ngo. The other
  recension has ངོ་མ་འཕྲོད and ངོ་འཕྲོད (checked) · added.
- u. 4 · n · style · "'byung ngo, with the sentence-ending -o repeated after -ng" · now "written ngo after -ng".
- u. 7 · n · style · "The other recension has bsun ma 'das, which differs" · now gives the whole phrase, རིག་འཛིན་མཁའ་འགྲོའི་བསུན་མ་འདས་པའི་འོག་ཏུ,
  without lha tshogs kyi (checked).
- u. 9 · n · style · drafter's doubt 84.2. The note did not give the other recension, which differs here in wording. It has
  མི་ཐོབ་པར་བརྒྱལ་ཏེ༔ དེ་ཁོ་ར་ཁོར་ཡུག་ཏུ་འོང་སྟེ (checked) · added, with "the print has neither par nor te de kho ra".
- u. 13 · i · style · `l` and the note have 'khyams pa yod do "there are (those) who wander", but `i` said flatly that the
  abbots and teachers "wander in saṃsāra" · now "and some of them wander in saṃsāra".
- u. 14 · n · style · "(into-bad-destinies in the literal line, as in 002)": this unit's `l` has "bad-destinies' abyss". 002's
  "into-bad-destinies" renders ngan song du · now "('bad-destinies' in the literal line, as in 002)".
- u. 15 · n · style · "gsang sngags … (Sanskrit mantra)" · now "Sanskrit guhyamantra" (gsang "secret" + sngags "mantra").
- u. 15 · n · style · the note said nothing of ཐ་མ་ཅིག, where cig stands after a vowel and the rule gives zhig, as the other
  recension has (ཐ་མའི་ཐ་མ་ཞིག, checked). The print's ཅིག habit is in QUESTIONS (002) · one clause added.
- u. 20 · n · style · shi ram "the print's spelling of sha ri ram" did not give the other recension, which has ཤར་རི་རམ
  (checked) · added.
- u. 32 · n · style · drafter's doubt 90.1. The note's alternative (the first two names read as one) did not say that the other
  recension has the ༔ after the first chos (མ་སྒོམ་པར་སངས་རྒྱས་པའི་ཆོས༔, checked), which supports two names · added.
- about · style · "others attain the three bodies in the three bardos or are born in the higher realms" gave all three bodies
  to "others", while the dharmakāya in the bardo of death belongs to the great meditators of the sentence before. The print's
  "others" (gzhan dag) are only those born in the higher realms · now "those who recognise in the bardo of reality or of
  becoming attain the other two bodies, and others are born in the higher realms".

Severity count: major 0 · minor 7 · style 16 (23 change lines).

### Drafter's doubts, adjudicated

1. 89.4 གཞན་ དག་ ཀས: kept as printed and marked uncertain. The note was wrong about the other recension and is corrected. It
   now offers གནས as a candidate for the crushed letters, beside the reader's ཀྱང, and says that an agentive on skye is
   irregular (above). The division གཞན་ དག་ ཀས stands: gzhan dag is "others" with the plural dag, as de dag is split in 001–008,
   and the doubtful syllable is best left as its own word.
2. 89.5 ཆགས་ ལ་ སྤྱོད་པའི: kept. ཆགས is clear to reader C at ×5 (ཆ, ག, ས), so it is no misreading of the witness's bare ལ. "formed(?)"
   in `l` and the note's "the sense of chags la here is not sure" are right. `i` follows the sense without chags and says
   nothing the print contradicts. chags "take shape" with la "and" (a clause link after a verb) is the likeliest reading. The
   division is sound (ཆགས་ ལ: la is a free particle).
3. 88.4 སྒྲ་ ཟེར་ དང: kept. ཟེར is a gap filled from the other recension's སྒྲ་དང་ཟེར་དང, and both `l` "rays(?)" and the note ("very
   doubtful") say so. The print has no dang after sgra. Taking rol mor sgra as "the sound of music" is the only reading that
   gives sense, and the note says why the ར for འ is not corrected. The stray tsheg fix (ད་ང → དང) is named.
4. 83.1 འཕྲི་བ་ ལ་ མེད: kept, with "at(?)" in `l` and "translated as if absent" in the note. The la is marked [?], and the other
   recension's ཟད་ཅིང་འཕྲི་བ་མེད་པས (checked) has no la. A locative "in lessening there is none" would give the same sense, so the
   note's treatment loses nothing.
5. 83.4 གནས་ བསྒྱུར་ དེ: kept. bsgyur is the past stem of sgyur (sgyur / bsgyur / bsgyur / sgyur). The note rightly says that
   the clause link after -r is te by rule and offers "that" as the other reading. The other recension's གནས་འགྱུར་ནས (checked) is
   given in the note.
6. 84.2 བརྒྱལ་བ་ ཁོར་ཡུག་ཏུ: the misprint fix (བབ) is named and hedged ("fairly but not wholly sure"). The reading "swoon upon swoon"
   is marked as taken from the words. The other recension's different wording is now added (above).
7. 90.1: སངས[?] is called blotted, and sangs rgyas is not in doubt. གསང་ལམ against the other recension's གསེབ་ལམ is given. The
   double reading of the first two names is kept and supported (above).
8. ལོངས་སྤྱོད་ རྫོགས་པའི་ སྐུ: re-divided as one word, as 004–007 have it (above). The pilot's ལོངས་སྤྱོད་རྫོགས་སྐུ is the short form
   of the same word and is also one word.

### Division, checked by script against 001–008

- Same as before: ངོ་སྤྲད (joined); ངོ་ འཕྲོད, ངོས་ ཟིན, ངོ་ ཤེས (split); འཇིགས་ སྐྲག་ དངངས་ གསུམ (split as in 003 u. 14 before gsum, which
  counts three words; 008's review settled this); ཐ་མའི་ ཡང་ ཐ་མ (007 u. 35); གཉིས་སུ་ མེད་པར (007 u. 31); ཡིན་ ནའང (006 u. 6); ཞེ་ ན
  (007 u. 22); ཡན་ཆད (008 u. 30); སྐྱེ་བོ་ ཐ་མལ་པ (002 u. 46); ཡི་དམ་ གྱི་ ལྷ (007 u. 3); ལས་འཕྲོ (006 u. 21); སྡིག་པོ་ཆེ (002, 005);
  ཕྱག་རྒྱ་ཆེན་པོ (002); དཔག་ཏུ་མེད་པར (as དཔག་ཏུ་མེད་པ, 001, 008); ཉམས་སུ་བླང(ས) (as the pilot's ཉམས་སུ་བླངས); ཉམས་ལེན (002); ལྔ་བཅུ་རྩ་བརྒྱད
  (as བཞི་བཅུ་རྩ་གཉིས, 006); འཇའ་འོད beside འཇའ་ དང་ འོད (004); དག་པ་ མཁའ་སྤྱོད (007, 008); ཐོས་གྲོལ་ ཆེན་མོ, ཆོས་ཉིད་ བར་དོ (001–008).
- New words, sound as lexical compounds or fused endings: ཁྲག་འཐུང, ཁྲོ་བོའི, འཆར་ཚུལ, མ་རིག, འཁྲུལ་འཁོར, ལྷུན་སྟུག, སྡིག་སྒྲིབ, ཁོར་ཡུག་ཏུ,
  རང་དབང, གསང་སྔགས(་པ), མཚན་ཉིད(་པ), སྐུ་གཟུགས, མཆོད་བསྟོད, གཤེ་སྐུར, སྡང་སེམས, ལོག་ལྟ, སྤྱོད་ལམ, བྱིན་རླབས, བསྐྱེད་རྫོགས, གདན་དྲངས་པར,
  རྫོགས་ཆེན་པ, སྒོམ་ཆེན, རྫོགས་སངས་རྒྱས་པའི, གསང་ལམ, མ་ཐག་ཏུ, མ་ཁད་དུ, སྣ་རེ, ཅིས་ཀྱང, དེ་ལྟར་རོ, ཕྱིར་རོ, སྡུག་བསྔལ་ལོ.
- Departures from earlier practice: only སྔར་འདྲིས and the three-word ལོངས་སྤྱོད་ རྫོགས་པའི་ སྐུ. Both were re-divided (above). The script
  found no other word of 009 divided differently in 001–008.

### Checked and confirmed (no change)

- The three misprint notes open "The print has X, a misprint for Y, corrected here.": དེ་ཡ → དེ་ལ (u. 4), བརྒྱལ་བབཁོར → བརྒྱལ་བ་ཁོར
  (u. 9), ནམ་མཁར → ནམ་མཁའ (u. 26). Each gives the degree of certainty the establish log gives. The contractions are named: ལམ
  (u. 4), རྣམྶ (u. 18), དགོྶ (u. 24), རྟག|སུ (u. 26). So are the tsheg fixes: བར་དོའཆར (u. 1, 2), ལའཕྲོད (u. 4), འཛིནམཁའ (u. 7),
  འདིནིཁྲོ (u. 8), ཐོབབརྒྱལ (u. 9), པའིགནད (u. 16), རིངསྲེལ (u. 17), དེའིཕྱིར (u. 20), ཡིནཏེ (u. 21), ཟེར་ད་ང (u. 26), དམཚིག (u. 27),
  འགྱུརབས (u. 28), པརསངས and པའིཆོས (u. 32). ཀསམཐོ (u. 31) is the one line-join tsheg left without a note, which is not needed.
- The print has 14 [?] marks (by script on the established file; the establish log's heading says 17, but it lists the same 14).
  All are called uncertain in the notes: ངོ, ཐོབ (u. 4), དུ, ལ (u. 5), འཛིན (u. 7), དེས (u. 19), པ(ས) (u. 20), རྟག (u. 26), ཟེར (u. 26),
  འདིར (u. 30), ཀ, ས (u. 31), ཆགས (u. 31), སངས (u. 32). The log's kept-as-printed items are in the notes: རོལ་མོར (u. 26), ཤི་རམ
  (u. 20), གཡང་ལ (u. 14), རིང་སྲེལ (u. 17), སྒོམས (u. 16), ཤོང་དང (u. 18, corrected above), and the ༔ set apart after སྟུག and རིང (u. 5).
- Other-recension claims, checked one by one in the stored text. Apart from u. 10 and u. 31 (corrected above), all are
  accurate:
  - u. 5: འབྱུང for byung; no la in འཕྲི་བ་མེད.
  - u. 6: ངོ་སྤྲད་ཅིང.
  - u. 7: བསུན་མ་འདས; གནས་འགྱུར་ནས; འོང་ངོ༔ ད་ནི … འདིར.
  - u. 15: the sentence worded differently: ལྟ་བུར, ཡིན་པ་ངོ་ཤེས་པས.
  - u. 19: དེའི་རྐྱེན.
  - u. 20: དེས for de'i phyir.
  - u. 26: རོལ་མོའི; སྒྲ་དང་ཟེར་དང.
  - u. 28: ཐོས་གྲོལ་ཆེན་མོ་འདི་ཀླག.
  - u. 30: བར་དོར.
  - u. 32: གསེབ་ལམ.
- Stems and labels:
  - Verbs: bya, future of byed (byed / byas / bya / byos); bstan, past of ston; sprad, past of sprod; byung, past of 'byung;
    bsgyur, past of sgyur; bsgrims, past of sgrim; song, past of 'gro; btab, past of 'debs; blang, future of len
    (len / blangs / blang / longs); bzlas, past of zlo; drangs, past of 'dren; bsgom, future in ma bsgom par; byon, past of
    'byon, beside present mi 'byon; grongs, the respectful "die".
  - Negation: mi with the present (mi thob), ma with the past (ma mdzes, ma 'phrod).
  - Particles: de after -d (yod de); ste after a vowel (bya ste); te after -r expected (u. 7, said so); ru after a vowel
    (dka' ru); -'o after a vowel, -ngo, -lo, -ro, -bo, -no, -do after their finals; na'ang = na yang.
  - Sanskrit: heruka, vinaya, samaya, śarīra. All right (sgoms, klog and kas corrected above).
- House renderings: "the between" / "bardo"; "face-introduce" / "pointed out" for ngo sprad, the face "meeting" for ngo 'phrod;
  "clear light"; "reality itself" / "reality"; "body of truth"; "knowledge-holder"; "Sky-Faring" kept apart from "sky-goer";
  "knowing" / "awareness"; "death-point's between" (as 008's review settled); "emanation-body"; "deity-host"; "human-world";
  "karmic-residue"; "Hearing-Liberation Great" / "Great Liberation through Hearing"; "is-here" for bzhugs so (as the pilot's
  title).
- `i` was read for wording remembered from the modern translations. None was found.

### Refused

- u. 8 · note "dngangs is the print's spelling of sngangs": dngangs is itself a standard spelling, so "the print's spelling"
  overstates. But the master glossary's དངངས and དངངས་སྐྲག say the same, and 003–008 follow it. Changing it here alone would make
  the parts disagree. Kept, and listed for the owner below.
- u. 33 · 'dis "with the -s that marks the doer" before the intransitive sleb: the instrumental "by this" is within the range
  of -s, and `i` ("whom it has reached") gives the sense either way. Kept.
- u. 7 · `i` "the fifty-eight … wrathful deities come", with no verb in that clause: the fifty-eight are the subject of
  'char du 'ong in the next clause, and `i` must give them a verb. Kept.
- u. 16 · mngon rtogs glossed "(sādhana)" rather than the word's Sanskrit, abhisamaya: the note explains it as the text that
  describes a deity for meditation, which is what sādhana means here. Kept.
- u. 22 · "ma, the 'not' of the past" with the adjectival mdzes: the past sense ("was not seemly") is what `i` gives, and u. 21
  has mi mdzes pa for the present. Kept.
- u. 3 · "parts 003 to 008" for the seven days: 003 opens the bardo of reality and its first day, and 008 closes the seventh
  (checked in the abouts). Kept.

### For QUESTIONS.md (open decisions for the owner)

- 89.4 གཞན་དག་ཀ[?]ས[?]: the other recension has གནས at this point. A better image of n90 might show the crushed letters as གནས
  ("others are born in the high abodes") rather than ཀས or ཀྱང. The note now gives all three.
- དངངས "the print's spelling of sngangs" (master glossary, 003–009 notes): dngangs is a standard spelling in its own right. To
  change it, edit the master entries and leave the published notes, or bring them into line together.
- The establish log's count of [?] marks (17) does not match the 14 marks in the pinned file. The log is left as written, a
  record of that firing.

## Pass 2

Second pass. Each of the 141 entries in gloss.json and its 2 broadenings was checked against the word and its use in
units.json (w / l / i / n), against the master entries of related forms (stems, particle forms, Sanskrit), and against
glossary.json style. The master entries of the 204 known forms used in this part were read by script against the units where
each occurs, to find uses they do not cover. Then all 33 units were read again from the original through `l` to `i`, with
pass 1's changes. Both files were edited by script (ensure_ascii=False, indent 1, no final newline). A round-trip of each
unedited file was checked to be byte-identical first. `w` is unchanged.

Key check by script: the gloss.json keys equal the part's words not in the master glossary (141 of 345). None is unused and
none is already in the master. Every broadening (2 from the glosser, 6 added here) is of a master key used in this part, and
each begins with the master entry whole + " · ". Letter check: 33 units, 4093 letters, PASS (sha256 of the pinned source
matches). hooks.assemble + hooks.validate were run in memory, with gloss.json merged as `r3.py build` merges it (validate
reading the glossary as it would be written; nothing written). Result: no error, no WARN, and no "no glossary entry" left.
`r3.py build` was not run.

### Changes: gloss.json

- gloss ཀས · sense · minor · "the draft takes it as 'and others'" was pinned to the draft and wrong about it: the draft reads
  -s as the doer's ending, hedged · now "a doubtful reading of this print (ka + -s?) after gzhan dag 'others': perhaps for kyang
  'too', or for gnas 'abodes' …; the sense is not sure", matching pass 1's u. 31 ruling.
- gloss ཐོས་པ · stem · minor · "thos, past of nyan 'hear'": thos "to hear" is a verb of its own (nyan "listen" has past mnyan) ·
  now "(thos 'to hear' + -pa)".
- gloss སྒོམས་པ · stem · minor · "(sgom + -pa; the print spells it sgoms)" · now "sgoms, in form the imperative of sgom (sgom /
  bsgoms / bsgom / sgoms), written for the past bsgoms", as the u. 16 note.
- gloss བསྒོམ་པའི, བསྒོམ་པར · stem · minor · given as "sgom pa + …", which hid the stem · now "bsgom, the future stem of sgom".
- gloss ཕྱེད་པའི · stem · minor · "phyed, a form of phye 'to divide'" did not say what phye is · now "a spelling of phye, the past
  stem of 'byed 'to open, to separate'", with bye brag phyed as the example.
- gloss འབྱུང་བར · sense · minor · example "'byung bar 'gyur 'is sure to appear'" put the sense of cis kyang into the verb · now
  "'will come to arise'".
- gloss ཤ་སྟག · sense · minor · "without exception, certainly …, an intensifier": sha stag is "nothing but, all of them", not
  "certainly" · now "nothing but, all without exception (sha stag), set after what it covers".
- gloss འོག་ཏུ · wording · minor · the example "welcome has passed 'og tu" mixed English into the Tibetan · now "X 'das pa'i
  'og tu 'after X has passed'".
- gloss དོད་པ · sense · style · guess removed. dod pa "to stick out, protrude" is the ordinary verb of 'bur du dod pa (as the u. 16
  note has it) · now "standing out, projecting (dod 'to stick out, protrude' + -pa) …".
- gloss ལོངས · sense · style · "the sense is taken from the context" removed. longs "leisure, opportunity" is a word in its own
  right (yengs longs med) · now with that example, and its other use as the imperative of len.
- gloss ལྷུན་སྟུག · parts · style · "(lhun stug)" gave no parts · now "lhun 'mass, bulk' + stug 'thick', as in stug po; also
  written lhun 'thug".
- gloss འཁྲུལ་འཁོར · sense · style · "wheel of delusion" left out the word's own sense, "machine, turning device" · now has both,
  as the u. 5 note.
- gloss stems added where the glosser left them out:
  - བསྒྲིམས: past of sgrim, sgrim / bsgrims / bsgrim / sgrims.
  - བཟླས་པ: past of zlo, zlo / bzlas / bzla / zlos.
  - ཉམས་སུ་བླང: future of len, len / blangs / blang / longs.
  - ཉམས་སུ་བླངས་པ: blangs, past of len; it had been given as past of the compound.
  - ཁྲག་འཐུང: 'thung present, past 'thungs; also Sanskrit heruka.
  - འབྱོན: present, past byon.
  - འགྱུར: present and future, past gyur.
  - བསྒྱུར: past and future of sgyur.
  - བསྟན་པར: bstan, past and future of ston.
  - འདས་པའི: past of 'da'.
  - བཤད་པའི: past of 'chad.
  - གདན་དྲངས་པར: drangs, past of 'dren; gdan "seat".
  All are style changes.
- gloss parts, Sanskrit and wording · style:
  - ལྔ་བཅུ་རྩ་བརྒྱད: rtsa is the joining word, not part of "and eight".
  - མ་ཐག་ཏུ: ma + thag "distance" + -tu.
  - ཐ་ན: tha "end" + na.
  - ཅིས་ཀྱང: ci + -s + kyang.
  - བྱིན་རླབས: byin + rlabs.
  - གསང་སྔགས: guhyamantra.
  - མ་རིག: avidyā.
  - གདུང: the respectful word for bones.
  - གཡང: usually g.yang sa.
  - ཤི་རམ: apparently a spelling of sha ri ram.
  - རོལ་མོར: "in play" dropped; "perhaps written for rol mo'i", as the u. 26 note.
  - ཁོར་ཡུག་ཏུ: "again and again" given as the sense of a recurring state, not as the word's meaning.
- __broaden__ · added (style), each as master entry + " · " + new reading, for known words whose master entry did not cover this
  part's use:
  - ཆགས: "to come into being, to take shape … the sense is not sure" (u. 31).
  - བྱེ་བྲག: "distinction, difference: bye brag phyed" (u. 32).
  - དག: "plural marker after nouns too" (u. 28, 31).
  - མ་ཁད་དུ: "on the point of, just before" (u. 25). The master entry has only "as soon as", against the u. 25 note.
  - ལ: "from, of, with verbs of fleeing and fearing" (u. 14).
  - ཚན་ཆེ: "great in number, prevailing" (u. 6).

### Changes: units.json

- u. 10 · n · style · "ngos zin, 'the face is caught'" after pass 1 made `l` "recognition seized" · now "'the face is seized'".

Severity count, pass 2: major 0 · minor 8 · style 14 (22 change lines: 21 on gloss.json, including the 6 new broadenings as one
line; 1 on units.json).

### Checked and confirmed (no change)

- The glosser's two broadenings are needed and begin with the master entry verbatim:
  - ཕྱིར "because, for the sake of" (u. 11, 20, 27, 32).
  - གནས "state, condition" (u. 7, gnas bsgyur).
- Stems and labels in gloss entries, each checked:
  - Past stems: bris, past of 'bri; btab, past of 'debs; byas, past of byed; shar, past of 'char; song, past of 'gro; skyes,
    past of skye; byon, the respectful past of 'byon.
  - Other forms: 'dul, present; skye, present in skye ba; grongs, respectful "died".
  - Particles: -ru after a vowel (dka' ru); -lo, -ro, -'o endings.
- Known forms read against their use here:
  - Covered as they stand: ཟེར ("ray", u. 26); ཀློག (u. 28); ཐོབ་པ (u. 4, 21); ཡང ("even", u. 14); ཅིག ("a", u. 10, 15); སྐུ; མཐོང;
    བཞིན་དུ; ཞེ; ན; ཏེ; དེ ("after a verb: 'and then'", u. 7 bsgyur de); འདིར (here, u. 12–30); མར; ཙམ་དུ; གཅིག.
  - Covered by the glossary's own wording: དངངས (left as in pass 1).
- Sense hedges kept where the notes mark doubt: ཀས, ཆགས, རོལ་མོར, ཤི་རམ, ཁོར་ཡུག་ཏུ.
- All 33 units re-read. Pass 1's changes are sound:
  - The two re-divisions.
  - "recognition seized".
  - The u. 31 note with gnas.
  - The stems of sgoms and klog.
  - The about.
  No further change to `l`, `i` or the notes beyond u. 10 above. `i` was read again for remembered wording, and none was found.

### Findings considered and refused

- gloss བསྟན་པར, འབྱོན, འཛིན-type entries with an example from this part (bstan par bya, mi 'byon): the master entries carry
  examples the same way, and none is pinned to a single line's reading. Kept.
- gloss སྐུ་གཟུགས "image of a deity, a statue or painting" against u. 22, where sku gzugs are forms among the relics: an image of a
  deity is what the word means, and the note explains the use there. Kept.
- gloss ཤོང "to fit, to find room (shong 'to be able to hold')": both senses are the one verb (blor ma shong "did not fit in the
  mind"). Kept.
- gloss བརྒྱལ་བ with brgyal as a bare verb: brgyal ba "to faint" has no distinct stems in common use. Kept.
