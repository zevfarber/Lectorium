# Review — bardo-thodol-006 (pp. 54–62)

## Pass 1

Checked against conventions.md, QUESTIONS.md, runbook.md and ../run3/RUNBOOK.md (Reviewer), packet.md (the pinned print,
its fifteen `# fix:` lines and the establishment log), units.py, hooks.py, the pilot bardo-thodol-001.json, the units of
002–005, 005's review.md and glossary.json. All 45 units were read word by word, from the original to `l` to `i`, and
every grammatical label in the notes was checked against the form; every division was checked against conventions.md
"What the page shows" and against how 001–005 divide the same words (by script over all their `w`). units.json was edited
in place by script (ensure_ascii=False, indent 1, no final newline, as the file was written; a round-trip of the unedited
file was checked to be byte-identical first). Four `w` changes (below), letters kept identical. Letter check (all `w`
joined, ' / ' and spaces removed, against `hooks.letters()` for the part): 45 units, 4773 letters, PASS; verse line counts
w / l / i equal (u. 19: six lines each). hooks.assemble + hooks.validate report no error other than "no glossary entry"
(111, the words the glosser is covering).

### Changes

- u. 20, 38 · w, l, i, n · minor · the name of the northern realm. The draft divided བྱང་ཕྱོགས་ ལས་ རབ་རྫོགས་པའི and rendered "the north-direction from, Fully-Accomplished's realm(-in / from)". But every other realm in this part stands directly after its direction with no particle (u. 34–37: དབུས་ཕྱོགས་ ཐིག་ལེ་བརྡལ་བའི, ཤར་ཕྱོགས་ མངོན་པར་དགའ་བའི, ལྷོ་ཕྱོགས་ དཔལ་ …, ནུབ་ཕྱོགས་ པདྨ་བརྩེགས་པ་ བདེ་བ་ཅན་ གྱི; 005 u. 40 ནུབ་ཕྱོགས་ བདེ་བ་ཅན་ གྱི), the other recension has the same ལས་རབ་རྫོགས་པའི in both places, and las rab rdzogs pa, "fully accomplished action", is a name that goes with Amoghasiddhi's wisdom of accomplishing deeds; "from the north into the realm …" (u. 20) gives a strained sense · w now བྱང་ཕྱོགས་ ལས་རབ་རྫོགས་པའི (both units); `l` "the north-direction, Action-Fully-Accomplished's realm-in / from"; `i` "the northern realm of Fully Accomplished Action"; the note to u. 20 explains the name, why las is read as part of it, and that 005 (rab brtsegs pa after las) took las as "from"; u. 38's note says "Las rab rdzogs pa".
- u. 29 · l, n · minor · drafter's doubt. The note said "How the print's kyi, 'of', fits is not clear" and `l` had "Your before-at". kyi stands where the sense wants kyis, the doer of ngo shes, as the other recension has (khyod kyis gong du), and the print writes gi for gis elsewhere (gcig gi in the pilot; 005 u. 11's yi read as yis the same way) · `l` now "You-of(by?) earlier-at"; the note: gong du "earlier, before this"; kyi read as kyis by the sense, with the other recension and the print's habit. `i` "Before this, if you had recognised" kept.
- u. 5 · n · minor · drafter's doubt (stem). The note said only "sgom … the verb of meditation, here with shig making a command", leaving bsgoms unlabelled. bsgoms is the past stem of sgom (sgom / bsgoms / bsgom / sgoms); the imperative is sgoms, which the print itself has in 002 (u. 46 སྒོམས་ཤིག) and the other recension here · the note now says so, and that with shig the form is read as the command.
- u. 4 · i · minor · "rest in the state of great equanimity where there is nothing to do" made chen po qualify equanimity; in btang snyoms byar med chen po'i ngang it qualifies byar med, as `l` ("nothing-to-do great's state") and the note ("byar med chen po, 'great non-doing'") have it · now "so rest in equanimity, free of attachment and aversion, of near and far, in the great state where there is nothing to do."
- u. 25, 26 · w · style · division. དུས་གཅིག / དུས་ཅིག were joined; 003 u. 33 divides the same words དུས་ གཅིག་ ལ (and the master glossary has དུས, གཅིག, ཅིག) · now དུས་ གཅིག་ ལ, དུས་ ཅིག་ ལ. `l` "at-one-time" kept; the note to u. 26 (cig without its prefix) still holds.
- u. 1, 5, 33, 34, 35, 36, 37, 41, 42 · l · style · 'char du 'ong was "to-dawn come" here, where 003 (u. 31, 44) and 005 (u. 20, 25, 49) give it "dawning come(s)" · now "dawning come(s)" in all nine; the note to u. 1 still marks 'char du against 'char nas.
- u. 2 · i · style · nyams nga ba "awesome" in `i`; 003 u. 30 has "fearsome" in both `l` and `i`, and `l` here has "fearsome" · `i` now "lustrous and fearsome".
- u. 15 · n · style · "where they had bag chags … or sdig sgrib" left out the fourth day, which had yi dwags in this place (005 u. 35) · now names all three, with their days.
- u. 1 · n · style · drafter's doubt (ནཱིར་ཏི་མ). The identification with Nṛtyā rested on the list of eight only · added that nṛti is "dancing", with its ṛ written as a vowel and r; "the letters do not spell it plainly" and "(?)" in `l` kept.

Severity count: major 0 · minor 4 · style 5 (9 change lines).

### Drafter's doubts, adjudicated

1. u. 1 ནཱིར་ཏི་མ as Nṛtyā(?): kept, with the "(?)" in `l` and "taken as" in the note; Gandhā and Nṛtyā are the pair of the
   north in the set of eight, and nīrti is a plausible writing of nṛti (above).
2. u. 2 ལྗང་ལ་འཆར་བ "green and dawning" (`i` "green and radiant"): kept. 'char ba is the house verb "dawn", the note gives
   the days-before 'tsher ba and the other recension; ཉམས་ང་བ "fearsome" as 003 (the `i` brought into line, above).
3. bya ba grub pa'i ye shes "the wisdom that accomplishes deeds" (u. 2, 12, 19, about): built from the grammar (bya ba "deed,
   what is to be done", grub pa "accomplished"), as the note shows; not a stock English name. Kept. The division
   བྱ་བ་ གྲུབ་པའི་ ཡེ་ཤེས follows 005's སོ་སོར་ རྟོགས་བའི་ ཡེ་ཤེས and 004's མེ་ལོང་ ལྟ་བུའི་ ཡེ་ཤེས.
4. u. 5 བསྒོམས་ཤིག: past stem used with shig (above).
5. u. 19 སྐྱོར "the present and imperative stem": right (skyor / bskyor / bskyor / skyor), and "as on the first day, where
   the second to fourth days had bskyor" matches 004 u. 8 (སྐྱོར) and 004 u. 32, 005 u. 11, 39 (བསྐྱོར). skyol in the last
   line is the form of 004 u. 8, 32 and 005 u. 11; nothing to add.
6. u. 22 ཚན་ཆེ "strong": kept as read and as one word (see Refused).
7. u. 23 ཕྱི་ལ་ཁྲིད "led back": kept (see Refused).
8. u. 29 ཁྱོད་ཀྱི་གོང་དུ: resolved by reading kyi as kyis (above).
9. Divisions: all checked against 001–005 (see Checked and confirmed); དུས་གཅིག / དུས་ཅིག split to agree with 003; བྱང་ཕྱོགས་
   ལས་རབ་རྫོགས་པའི joined as a name (above); the rest stand.
10. u. 39 Sanskrit: Vijaya, Yamāntaka, Hayagrīva, Amṛtakuṇḍalin; Aṅkuśā, Pāśā, Śṛṅkhalā (śṛṅkhalā "chain", lcags sgrog),
    Ghaṇṭā — right.
11. u. 40 Indra Śatakratu for dbang po brgya byin and Vemacitra for thag bzang ris: the standard equivalences of these
    Tibetan names (brgya byin renders śatakratu; thag bzang ris, "good woven pattern", renders vemacitra), so they may be
    stated; the sages of the animals and hungry ghosts, with no sure Sanskrit, are rightly given in English.
12. u. 42 forty-two: 5 buddhas + 5 consorts + 8 bodhisattvas + 8 female bodhisattvas + 8 gatekeepers + 6 sages + the All-Good
    pair = 42. Right.
13. u. 37 པདྨ་བརྩེགས་པ: kept as one word and left undecided between second name and description, as the note says.
14. u. 11 no yang na: right; the print has nothing between the instruction to rest and the refuge formula, and the note
    says what the other recension and the fourth day have.

### Checked and confirmed (no change)

- Misprint notes in rule-5b form: u. 26 "The print has སྐོ at the head of p. 59, a misprint for ངོ, corrected here", u. 32
  "The print has ཁྱ་བ, a misprint for བྱ་བ, corrected here", u. 39 "The print has གཞིན་རྗེ, a misprint for གཤིན་རྗེ,
  corrected here", each with its reason and the other recension. The tsheg-only fixes need no note, as in 002–005.
- [?] readings called uncertain: སྒྲིབ་པ (u. 1), དྲག་བོས (u. 19), ཡུན་རིང་ before ༔ (u. 22), ལྷུན་གྱིས (u. 45); the guesses
  gsol ba thob cig / 'di skad du thob cig "(?)" (u. 11, 18), tshan che "is read as" (u. 22), drag pos "fierce-by(?)" (u. 7).
- Kept-as-printed readings from the log noted: bzhog cig (u. 10, with the stems of 'jog), rab rdzogs / rab brtsegs (u. 20),
  zhan yang (u. 21), dus cig (u. 26), the print's b for p (rnam bar, drag bos, grub bas, rim ba), kye beside kyai (u. 43),
  bos (u. 27).
- Other-recension differences of sense from the log, all in the notes: blo dman pa yin na'ang (u. 6), zhen pa spongs (u.
  17), no "listen" after the vocative (u. 27, 31), bag chags kyi dbang (u. 28), rang snang du ma shes pas (u. 30), Shākya seng
  ge (u. 40), snang ba las (u. 42), the realms "are" the quarters of the heart (u. 43), lhun gyis (u. 45).
- Stems and labels: lhung past (u. 16, as 005 after its pass 1); 'ongs past of 'ong (u. 25); shar past of 'char (u. 26);
  bos past and imperative of 'bod (u. 27); zhog imperative of 'jog (u. 4); skyes past of skye (u. 8); na'ang as 'ang after
  a vowel (u. 6); yang after -n as the rule gives, with the print's own kyang after zin (u. 21 — the note is right where
  the log calls yang the irregular form); rgyu after a verb for what is to happen (u. 29); rtsa in numbers (u. 42).
- Metre of the prayer (u. 19): nine syllables in every line after kyai ma (bcom ldan don yod grub bas lam sna drongs = 9;
  yum mchog dam tshig sgrol mas rgyab nas skyor = 9), as the note says.
- Division agrees with conventions.md and 001–005: ཡིན་ ནའང (as 002's ཡིན་ ན), ད་ ཕན་ཆད་དུ (as 003's ཁ་སང་ ཕན་ཆད), གོང་ ལྟར
  (as 002's རིམ་བ་ ལྟར), ཡེ་ཤེས་ བཞི་ སྦྱོར, བྱ་བ་ གྲུབ་པའི, དེ་ དག (as དེ་ རྣམས), ཕྱི་ ལ and ཕྱིར་ ཐོན (as 002's ཕྱིར་ ཐོན་པ),
  ཡེ་ནས (001), ལན་མང་དུ (005), རིམ་བ་ མང་དུ, ཉམས་ང་བ (003), སྐྲག་དངངས (as 005's དངངས་སྐྲག), ཆགས་སྡང (as 005's ཆགས་ཞེན),
  ཉེ་རིང, བཏང་སྙོམས, རང་རྩལ (as རང་མདངས), ལས་འཕྲོ (as ལས་ངན), ལྷན་ཅིག་ཏུ (as གཤིབས་མར, རྩེ་གཅིག་ཏུ), འབྲལ་མེད་དུ (as 005's
  དབྱེར་མེད་དུ), བཞི་བཅུ་རྩ་གཉིས, ལྷུན་གྱིས་གྲུབ་པ (a fixed term, as ཉམས་སུ་མྱོང), ཀུན་ཏུ་བཟང་པོ (004), the names whole.
- House renderings and the formulae of 004–005: the refuge formula, the hook of compassion, "Turn with devotion", the
  path of welcoming, the prayer word for word apart from the day's names, the dissolution formula, the six lights, "the
  dead-one's by-name", child of noble family, face-introduce / point out, knowing / awareness, the between / bardo,
  lustreless / dull, shimmering, body of perfect enjoyment.
- `i` read for remembered wording from the modern translations: none found.

### Refused

- u. 22 · split ཚན་ཆེ as 003 split བཀྲག་ ཆེ་བ and ལྡིར་ ཆེ་བ: there bkrag and ldir are nouns of their own ("lustre",
  "roar"); tshan is not used alone in this sense, and tshan che is the set adjective "strong, intense". Kept as one word.
- རིགས་ལྔ, རིགས་དྲུག joined while ཐུབ་པ་ དྲུག, འོད་ དྲུག, ཕྱོགས་ བཞི are split: "the five families" and "the six kinds" are
  set terms (as ཞི་ཁྲོ or ཕུང་པོ would be), the others plain counts. Kept.
- u. 23 · ཕྱི་ ལ་ ཁྲིད "back-to led", `i` "lead them back": phyi la "outward, behind"; "away" was considered, but "back"
  gives the pull against the light that the sentence describes, and the note gives both. Kept.
- u. 25 · 'ongs pas (past) rendered "come dawning" in `i`: as 005 u. 26 (bros su 'ongs), the past stem in a narration of
  what happens; `l` shows "came". Kept.
- u. 13 · ma bros shig with the imperative stem in a prohibition: the note claims no stem, and the form is the one of
  003–005. Kept.
- u. 41 · `i` lists Samantabhadra and Samantabhadrī, then "the All-Good father and mother, the two of them": the Tibetan
  names them, then sums them up; the `i` follows it. Kept.
- 005 u. 48 (published): its བྱང་ཕྱོགས་ ལས་ རབ་བརྩེགས་པའི took las as "from". If las belongs to the name here, it may there
  too (las rab brtsegs pa, or a slip for las rab rdzogs pa). A published part is not changed from this draft; noted here
  for the owner.

## Pass 2

Second pass: every one of the 84 entries in gloss.json (83 from the glosser, ལས་རབ་རྫོགས་པའི from the orchestrator) and the
two broadenings checked against its word, its use in units.json, the notes, and the master entries of related forms
(stems, case and particle forms, parts, Sanskrit); the master entries of the 254 known forms read against how they are
used here; then all 45 units read again from the original through `l` to `i`, with pass 1's one bold change (ལས in the
northern realm's name) re-examined against 005 u. 48 and both control witnesses in source/raw. Both files were edited by
script (ensure_ascii=False, indent 1, no final newline; a round-trip of each unedited file was checked to be byte-identical
first). `w` is unchanged, so the key set is the same as after pass 1. Key check by script: the gloss.json keys equal
novel-forms.json plus "__broaden__"; every broadening is of a master key used here and begins with the master entry whole
+ " · ". Build: BUILT, 45 units. Validate: PASS, no WARN.

### Changes: gloss.json

- __broaden__ དག · new · minor · the master has only "pure, correct"; here (u. 43, 45) de dag is "those", the plural, as `l` "those (plural)" has · broadened with the plural marker after de.
- __broaden__ ཀྱི · new · minor · the master gives kyi only as "of"; u. 29 reads khyod kyi as khyod kyis 'by' (pass 1), and the entry would contradict the note · broadened, with "perhaps", as the master's གི already says of gi for gis.
- __broaden__ གྲུབ་པ · new · minor · the master has only "established, proved to exist"; in u. 5 phrag dog gi rgyu las grub pa is "formed from", `l` "formed" · broadened with "formed, made; accomplished".
- __broaden__ གྲུབ་པའི · new · minor · the master has "of the established · formed from"; bya ba grub pa'i ye shes (u. 2, 12) is "the wisdom that accomplishes deeds", a sense neither covers · broadened.
- gloss ལྗང · sense · minor · "ljang khu 'light green'": ljang khu is simply "green" (master ལྗང་ཁུ "green"; `l` "light, green" is 'od + ljang khu) · now "ljang khu 'green'".
- gloss ཐག་བཟང་རིས · hedge · minor · "perhaps the king of the demigods, Vemacitra", where the note to u. 40 (adjudicated in pass 1: thag 'weave' + ris 'pattern' renders vema + citra) states it · now "the king of the demigods, Sanskrit Vemacitra".
- gloss ལས་རབ་རྫོགས་པའི · hedge · minor · stated the reading as fact · now "read as the name …; las may also be taken as 'from' …, as it was before rab brtsegs pa'i" (see u. 20 below).
- gloss ཐུབ་པ · general · style · gave only "sage", while the form is first the adjective "able" (master ཐུབ "able") · now "able, capable (thub 'to be able' + -pa) · the sage, the Able One (Sanskrit muni) …".
- gloss གྷནྡྷེ་མ · hedge · style · "perhaps Gandhā": the letters spell gandhe plainly, the form of address of Gandhā, and the note to u. 1 has no doubt (the doubt belongs to ནཱིར་ཏི་མ, which keeps its "perhaps") · "perhaps" removed.
- gloss སྤྲས་པ · stem · style · no stem · now "spras, past of spra 'to adorn', + -pa".
- gloss བཏང་སྙོམས · stem · style · btang now "past of gtong".
- gloss སྦྱོར · stem · style · now "the present stem; past and future sbyar".
- gloss པདྨ་བརྩེགས་པ · stem · style · brtsegs now "past of rtseg", as the master's རབ་བརྩེགས་པའི.
- gloss དབང་པོ་བརྒྱ་བྱིན · stem, Sanskrit · style · byin now "past of sbyin 'give'"; Śatakratu added, as in the note to u. 40.
- gloss ཞིག · grammar · style · "a form of cig" said nothing of when · now "the form of cig after a vowel and after ng, n, m, r, l, '; shig after s".
- gloss ལས་འཕྲོ · general · style · "the good karma … that ties a person to the teaching" pinned the general word to this text's use · now the general sense first, "in this text …" after.
- gloss སྒོ་བ · parts · style · "-ba, one who does" · now "-ba, here 'the one of the gate'".
- gloss རྣམ་པར་རྒྱལ་བ · general · style · "the first of the four" is the order of this list, not a fact of the figure · now "one of the four …, named first in this text".
- __broaden__ ཁྲིད · stem · style · "to lead, guide (khrid)" gave no stem · now "khrid, past and imperative stem of 'khrid 'to lead'".

### Changes: units.json

- u. 20 · n · minor · pass 1's note on Las rab rdzogs pa gave its reasons but not its uncertainty, and said only that 005 "took las as 'from'" · now adds "The reading is the likelier one, not a sure one: las can also be 'from' …"; that the other recension has las rab rdzogs pa'i in 005's place too; that either the print names the realm in two ways or one place is a slip; and that "the two parts read las differently".

Severity count, pass 2: major 0 · minor 8 · style 12 (20 change lines: 14 gloss entries rewritten, 4 broadenings added, 1 broadening reworded; 1 unit note).

### Pass 1's bold change re-examined (u. 20, 38: ལས་རབ་རྫོགས་པའི)

Kept. (1) Every other realm in this part stands directly after its direction with no particle (u. 34–37), and so does the
west in 005 u. 40; with las as "from", u. 38 would run "from the north, from the realm … from (nas)", and u. 20 "having
dissolved, from the north, into the realm", both strained. (2) The other recension has ལས་རབ་རྫོགས་པའི in both places here and
also in 005's place (དེའི་དུས་སུ་བྱང་ཕྱོགས་ལས་རབ་རྫོགས་པའི), and the dzogchengonpa transcription of this print agrees at 60.5.
(3) las rab rdzogs pa, "action fully accomplished", answers to Amoghasiddhi's wisdom, bya ba grub pa'i ye shes. Against it:
las is very often "from", and 005 read it so before rab brtsegs pa, which can stand as a name alone ("Heaped Up"). So the
reading is likely, not certain; the note now says that, and the gloss hedges. 005 is published and is not changed here
(see QUESTIONS.md).

### Checked and confirmed (no change)

- Stem claims in gloss and notes, each checked: bsgoms past of sgom (sgom / bsgoms / bsgom / sgoms), read as the command; bros imperative (and past) of 'bros; bzhog read as zhog, imperative of 'jog ('jog / bzhag / gzhag / zhog); bos past and imperative of 'bod; shar past of 'char; 'ongs past of 'ong; lhung past beside ltung; skyor present and imperative; skyes past of skye.
- Particle forms: na'ang ('ang after a vowel), yang after -n (zhan yang, regular), zin te / yin te (te after n), khrid de / 'phrod de (de after d), cig after g (bzhog cig, bkrag med pa cig), shig after s (bsgoms shig, bros shig), zhig after n (gzhan zhig).
- Hedges kept where the text is uncertain: ནཱིར་ཏི་མ "perhaps Nṛtyā", དྲག་བོས "perhaps for drag pos", ཚན་ཆེ "read so", བཞོག་ཅིག "kept as printed", པདྨ་བརྩེགས་པ "second name or description"; ལྷུན་གྱིས་གྲུབ་པ needs none (the [?] is in the note to u. 45).
- Sanskrit: Vajrapāṇi, Sarvanivaraṇaviṣkambhin, Gandhā (gandhe the feminine form of address), saṃskāra, Vijaya, Yamāntaka, Hayagrīva, Amṛtakuṇḍalin, muni, Śatakratu, Vemacitra, Śākyasiṃha, dharmarāja, kṛtyānuṣṭhānajñāna (note) are right.
- Known forms read against their use here: ལ ("with" after gnyis in u. 1, as 004 u. 16, 40 and 005 u. 21; "whereas" after yin pa in u. 29, within "after a verb: 'and'"), ཅིག, ཏེ, དེ, ཡང, ཟིན་པར, ཡོད་པ, ཕྱིར, ཟེར, མར, སྣང་བ, ཀྱིས (gnyis kyis), གི, གིས ('ong gis) cover their use; only དག, ཀྱི, གྲུབ་པ, གྲུབ་པའི needed broadening (above).
- All 45 units re-read: pass 1's changes are sound; the three misprint notes (u. 26, 32, 39) in rule-5b form; the four [?] readings called uncertain; u. 45's "the next sentence of the print speaks of the size of the forms" agrees with the stored transcription of p. 63 (སྐུ་དེ་དག་ཀྱང་མི་ཆེ་བ). `i` read again for remembered wording: none found.

### Findings considered and refused

- u. 1 · note "'char du 'ong ngo, 'they come to dawn', where the days before had 'char nas 'ong ngo, 'they come dawning'", while `l` has "dawning come" for both (pass 1, for agreement with 003 and 005): the note describes the Tibetan difference, which `l` cannot show without breaking the formula of the earlier parts. Kept.
- u. 22 · `l` "Again," `i` "But" for yang at the head of the sentence: yang there introduces the contrary case; `i` gives the sense, `l` the word. Kept.
- u. 8 · `i` "and you will go toward it" for skyes nas 'ong gis: the same rendering as 004 u. 45. Kept.
- ཆེན་པོའི, སྐྱེས་པས, ཤེས་པས and other entries with a set phrase from this part: phrases showing the form's use, as the master gives, not a line's wording. Kept.
- ཐག་བཟང་རིས "thag 'weave, rope'": thag is "rope, cord" and thag 'dren / thags "weaving"; the gloss gives both and renders the vema of the Sanskrit. Kept.
- 005 u. 48 (published) reads ལས as "from" before རབ་བརྩེགས་པའི: not changed; a QUESTIONS.md entry is proposed to the orchestrator.
