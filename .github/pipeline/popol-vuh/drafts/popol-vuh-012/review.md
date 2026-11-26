# Review — popol-vuh-012

## Pass 1

Reviewer pass 1, 2026-11-26. I read conventions.md (all of it, with the house renderings table and "The modern-letters
toggle"), runbook.md (the Reviewer paragraph), ../run3/RUNBOOK.md §2 (Reviewer), QUESTIONS.md, packet.md (the 20
established paragraphs and the establishment log), known-forms.json / novel-forms.json, wordre.py, popol-vuh-001…011.json,
popol-vuh-glossary.json, the 011 review (as the model of this file) and the draft units.json (83 units). For meaning I
used only Brasseur 1861 (OCR lines 22680–23260: K'iche', French and notes; also his introduction at 9026–9062 on Xquiq
and the Cendrier, his note on Cuchumaquiq at 21802 and the zakitok note at 22445) and the published parts and glossary.
I opened no modern translation and recalled none. Every edit was made by script (json load/dump, ensure_ascii=False,
indent=1). No `t` was changed, one `mt` word was changed (unit 62), and no unit was added, removed or moved. Unit
numbers are 0-based; ¶ numbers are the packet's paragraphs.

**mt against the published parts.** By script I compared every mt with 001–011 (MS form → modern form, lowercased).
No known form takes an mt that 001–011 never gave it. Forms with more than one published mt fit their sense here: chi
is chik only where it stands for chic (units 20, 35, 81) and chi elsewhere; ca is ka (ongoing, 'you') or qa 'we' (48,
53); cab is q'ab' 'hand' (never kab' 'two'); oc is oq after acan / apan and ok 'enter' (28); cam is kam 'die' (8) and
k'am 'take' (49), with cama kama (43, 51), the known take-verb split (QUESTIONS 007–009); cat is kat 'you' (27, 54) and
k'at 'burn' (59, as 010); cuꜭ kuk' 'with them'; quech kech 'theirs'; xe is xe' only as 'bottom' (72); cah qaj 'we want'
(54, as 007). The only mt changed is `cac` 'red' (unit 62, below). The 100-odd forms not in 001–011 were checked letter
by letter (ꜩ tz, ꜫ q', ꜭ k', ꜭh ch', v u/w, z s, h j, b b', c/qu k or q): every letter is respelled, and the marks
supplied are all on certain words (Xkik', ukik'el, kik' 'blood'; umi'al; q'ab'taq; chuch'axik from the house chuꜭhaxic,
as 005's chuchaxic), with the vowels Ximénez wrote (umeal, waqaqib').

**The drafter's flagged points, ruled one by one:**
1. ¶5 `ri vholom Hunahpu` (unit 11): kept as written, i "the head of Hunahpu". This is the table's Hunhunahpu-as-written
   pattern of 005 turned round, and it is applied the same way: print the MS, the English follows it, the note says so.
   The note did say so, but in a tangled sentence ("the head is that of Hunhunahpu, the father …"). Rewritten to say
   plainly that the MS has Hunahpu where the head is Hunhunahpu's, that the text itself names Hunhunahpu in ¶7 and ¶13,
   and that Brasseur prints Hunhun-Ahpu here.
2. ¶11 `cololeh` (unit 43) and ¶14 `ꜩololeh` (unit 49), both 'return' (inferred): kept. Brasseur reads chi qu'y
   cololeh 'soyez de retour' and x-chi qu y tzololeh 'vous retournerez', so both rest on him; the notes cross-refer and
   say the plain-c form may be the same word. mt by the letters (kololej, tzololej).
3. Red and fire sharing mt q'aq': `ꜫaꜫ` is written with tresillos in both senses, so q'aq' is forced by the letters
   (as 010's ꜫaꜫa q'aq'a), and the notes (61, 64, 65) say the modern red is kaq. Kept. But `cac` 'red' with plain c
   (unit 62) had been given q'aq' too: that supplies two ejectives that the certain word does not have. Changed (below).
4. ¶15 `ꜭha cut` without x (unit 60) and ¶13 `Queque` (unit 47): kept as printed, mt ch'a and Keke by the letters; both
   notes say what the MS has and what is presumed (completive not written; a slip for quehe), with Brasseur.
5. The 'you' markers: ¶4 (units 7–8) qui read 'I' with Brasseur's ma-qu'i ('mourrai-je'); ¶13 quinicamizah c- + in +
   i- (Brasseur qu'in y camizah) and maui qui puz with c- + i- ('vous ne me sacrifierez point'); ¶14 iꜭux plural 'your'
   to the maiden. Each is marked inferred and matches Brasseur; his note on iꜭux ('votre mis au pluriel pour ton … ce
   mode respectueux') is real (OCR 22985–22995). Kept.

**The drafter's departures:** `vmial` umi'al (unit 25): kept; the vowel i is in the MS, so only the glottal stop of the
certain word mi'al is supplied, and the note sets it against umeal. `Xquic` Xkik': kept; kik' 'blood' is certain and
Brasseur's notes give quiq 'sang'. `vacaquib` waqaqib': kept; Brasseur vakakib (his k = q) and the known waqib' both
give q, and the extra syllable is kept as written. `cac` 'red' q'aq': changed to kaq. `xcopcot` 'gashed': changed to
Brasseur's 'became renowned (?)'; the cut reading had no source behind it and is the kind of fully formed English the
conventions treat as suspect.

**Establishment log.** Every doubtful reading, letter decision and division is mentioned in its unit's note (quinaoh,
bixic, ca cha ca nu tao, xbec, the t–i ligature of tiquil and the cross, Hiiaa, the divisions of ¶4, Hunahpu, ri a vi qui
cab, the overwritten pa and cu, xare,tal, the blot on ve qui nim ahau, vtiohil, vmial, Cat acan, Cat oc, hun hunahpu,
xbiyx, cu biyh, puzo, ahchoce, quinicamizah, xaqui, Queque, ꜩacuixtah and the blot on xchi, vꜩaquic, ca cah ta na bec,
holomax with its blot, ꜭha without x, Catepuch, iiꜩ, chuchaxic, locox, Xca beba / naba, yaix, xuchuieh, turur, chi
luu, xe quiz, e uabai, a?anoc, the blot after chuv, and the plain c of co chic, co cha pam, cac che, quz, ruc, cab).
One note misplaced the marginal annotation (unit 5); corrected.

**Brasseur attributions.** Checked against the OCR. Three did not hold and were corrected (units 1, 27, 28); two French
quotations were given as English and are now quoted (5, 58).

Afterwards: the JSON parses; 83 units; every `t` equals the draft's; len(mt) == len(WORD_RE.findall(t)) for all 83; the
units' `t`, joined in order with a space, give back the packet's 20 paragraphs exactly; the only mt difference from the
draft is unit 62 word 13 of 14 (q'aq' → kaq).

Counts: **major 0 · minor 9 · style 11** (20 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 62 | mt, n | minor | `cac` in cac che 'red tree' (plain c) had mt q'aq'. That supplies two ejectives the certain word does not have: the modern red is kaq (as the notes of 61 and 64 say), and Brasseur's cak (k = q) spells kaq. The 004/008 precedent of plain-c cac → q'aq' was for *fire*, whose certain word is q'aq'. | mt kaq (no mark supplied, only the k/q choice per word). Note: kaq is the modern word the letters spell, Brasseur agrees; ꜫaꜫ with tresillos stays q'aq' by the letters. |
| 64 | l, i, n | minor | `xcopcot` rendered 'it was cut, gashed (?)' against the only source (Brasseur: 'tandis que l'arbre devenait célèbre à cause de la jeune fille'), on the drafter's reasoning that sap is drawn from a tree. No published part or glossary entry has the root. Also `l` glossed chi in colom chi pa zel as 'now'. | l "when it-became-renowned(?) the tree because-of maiden", "set(?) (chi) in bowl"; i "and the tree became renowned (?) because of the maiden"; the note gives Brasseur's French, says the form has no person prefix and that a passive 'cut' would fit the grammar but has no support. |
| 1 | n | minor | Xquic: "x-, the feminine or diminutive prefix … 'Little Blood'". Neither 'diminutive' nor 'Little Blood' is in Brasseur; his note says the prefix x (ix) makes a woman's name, and his introduction gives 'la Femme-Sang ou la Gomme-Noire'. | Rewritten from his note and introduction, French quoted; 'Little Blood' removed. |
| 27 | n | minor | "Xibalba is below, and the maiden is to go up to the world of people (Brasseur's note)". His note only glosses 'sur la face de la terre' and wonders whether the scene was in a cave or underground. | The inference is ours (from acan 'go up'); his note is reported as it is. |
| 28 | n | minor | "the head speaks for both brothers, as Brasseur notes". His note asks instead whether Vucub Hunahpu reappears as the representative of the priestly order; it is his French text that has 'la tête de Hunhun-Ahpu et de Vukub-Hunahpu'. | Both stated correctly. |
| 5 | n | minor | The marginal note was placed "at the foot of the page"; the log puts it at the left of 0040 l.38–40. 'the Ash-heap' was given as Brasseur's words. | "at the left of the column a few lines below (a cross and a few words)"; Brasseur 'le Cendrier'. |
| 14 | n | minor | 'right hand' for a vi qui cab follows 008 (inferred there), but the note did not say that Brasseur reads vi here as 'tip' ('étends seulement le bout de ta main'). | Added; 008's reading kept. |
| 54 | n | minor | "ca cah is taken as c- + ca- 'we' + ah" does not match the letters (that would be ca caah) or the mt (ka qaj). | "ca is the ongoing c- with its vowel, and cah c- 'we' (before a vowel) + ah 'want' … (toggle ka qaj)". |
| about | — | minor | "a tree, still called the Chuh Q'aq' Che": the text has only chuꜭhaxic 'it is called'. | "a tree, called the Chuh Q'aq' Che". |
| 11 | n | style | Flag 1: the Hunahpu-for-Hunhunahpu sentence was tangled ("Hunahpu, not Hunhunahpu as Brasseur prints: the head is that of Hunhunahpu, the father, but …"). | Says plainly: the MS has Hunahpu though the head is Hunhunahpu's (as ¶7 and ¶13 name it; Brasseur Hunhun-Ahpu); printed as written, as in 005; the English follows the MS. |
| 4 | i | style | "Its fruit must truly be sweet": 'must' is Brasseur's 'doivent être', not in quiꜩih quz vvach. 'go' (a guess, per the note) had no mark. | "Shall I not go (?) and see … Truly its fruit is sweet, they say, so I hear". |
| 12 | i | style | "Do you still want it?": 'still' is Brasseur's 'toujours'; l and n have 'Not you-want?' / 'do you not want it?'. | "Do you not want it?" |
| 17 | i | style | "spat out its spittle with force": a guess (the note), unmarked. | "with force (?)". |
| 25 | i | style | "the daughter and the son": vmial, vꜭahol are 'his daughter, his son' (l). | "his daughter and his son simply remain". |
| 28 | i | style | "Trust in my word": 'my' is Brasseur's ('ma parole'); the K'iche' is pa ꜩih 'in (the) word', and the reading is inferred. | "Trust the word (?)". |
| 45 | n | style | "zamahel 'messengers' (house of the last parts)": garbled; zamahel is not in the house table. | "as in the last parts". |
| 56 | n | style | l has "you-bear(?)", but the note did not say where 'you' comes from. | Added: the 'you (pl.)' of Brasseur's ch'y (chi + i-), not written here. |
| 58 | n | style | Brasseur's rendering given in our English. | Quoted in French: 'le sang seul passe contrat pour lui-même'. |
| 61 | n | style | "the last part's ꜫaꜫa 'red'": the form is in 010, not 011. | "an earlier part's". |
| 80 | i | style | "onto the face of the earth": chuvi is 'on top of', not chuvach 'on the face of'. | "onto the earth". |

### Refused / left

- **Flagged points 1, 2, 4, 5**: kept as drafted (reasons above); only point 1's wording was changed.
- **ꜫaꜫ 'red' q'aq'** (61, 64, 65, ꜫaꜫluhluh): kept by the letters; the 'red'/'fire' clash belongs to QUESTIONS 010 point 2.
- **vmial umi'al, Xquic Xkik', vacaquib waqaqib'**: kept (above).
- **ahchoce ajchoke** (39) and **Chec Chek** (42): Brasseur writes k (= q) in both, and his note ties ec to ekah 'carry'.
  Kept with k under 007's rule (q only where the note ties the word to a known q word in the published parts; neither
  is tied).
- **cucaam kukaam** (44): the note derives it from cam 'take' (k'am), but the derivation is only inferred, so the
  letters are respelled and nothing restored. Kept.
- **vchac 'its flesh (?)' uchak** (20): kept with Brasseur ('plus de chair'); the note lays out the other two vchac words.
- **Unit 8 i "Surely I shall not die … if I pick just one?"**: the ma … tah wish as an anxious question follows Brasseur's
  question and the couplet is kept. Kept.
- **Unit 32 i "six months had passed"** without (?): xzacat is a guess, but the sense is fixed by vacaquib ic and ¶10.
  Kept.
- **Unit 80 'she' went up** where Brasseur has the owls 'montant en grand nombre': xu (x- + v-) is singular, and quia
  'many' is only inferred; the i is marked (?). Kept; the about's "the owls lead the maiden up" fits both.
- **Unit 0 chi left unrendered**, mt chi: kept; the note says it may be chic.
- **ahuchan / ahuꜭhan** two mts (ajuchan, ajuch'an): kept, each by its letters, the modern word unknown.
- **Couplets**: ma qui cam tah / ma qui zach tah (8), nu chub, nu caxah (19), the two couplets of 24, vmial, vꜭahol
  (25), qui tiquem / qui chelem (44), the two cate lines (57), xa quic, xa holomax (58), vva vꜫexevach (69), turur rih /
  ꜫaꜫluhluh rih (74) are all kept as pairs in `i`. No change.
- **Names in `l` in MS spelling** (Vvcub Hunahpu, Vvcub Came) and Tucur 'the owls' in `i`: kept, as in 010–011.

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. **Red with plain c**: `cac` 'red' is now kaq (the modern word, no mark supplied), while ꜫaꜫ 'red' with tresillos is
   q'aq' by the letters, the same as 'fire'. Decide with 010 point 2 whether the tresillo spelling of 'red' should
   ever give kaq (that would replace a letter, the 011 point 2 kind of case).
2. **xcopcot**: now 'became renowned (?)' with Brasseur; the drafter's 'was cut, gashed' is grammatically possible
   but has no source.
3. **Hunahpu for Hunhunahpu** (¶5) is the mirror case of 005's table row; the owner may want the table row widened to
   "either name as written".
4. **vi qui cab 'right hand'** (008, here ¶5 twice) against Brasseur's 'le bout de ta main' here; the 'right' reading
   rests on 008's pairing with mox 'left'.
5. **ahchoce, Chec**: Brasseur's k (= q) not followed (007 rule); if ekah 'carry' (modern eqaj) is accepted as certain,
   Chec → Cheq.
6. **For the glosser**: known forms used in a new sense here need broadening: `cac` (kaq 'red', plain c), `xcul` (xkul
   'it ran, flowed', inferred, against 'it was smeared'), `vchac` ('its flesh', guess), `chi` (chi + i- 'you (pl.)' in
   chi chih, chi puzu), `vi` (wi in vvi qui cab), `raih` (raij with nu- 'I': the r belongs to the stem), `cah` (qaj 'we
   want'), `zaquitoc` (published as the torch's name; here the flint knife, Brasseur 'un couteau de silex').
