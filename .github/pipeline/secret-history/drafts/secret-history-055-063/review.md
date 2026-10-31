# Review, pass 1 — secret-history-055-063 (§§55–63)

Reviewer: adversarial pass 1, on `units.json` only (conventions, runbooks, `../run3/RUNBOOK.md` §2, the packet, `novel-forms.json`, `known-forms.json`, the model `secret-history-01-06.json`, the published parts §§7–23, §§24–42 and §§43–54 with their `review.md`, and `secret-history-glossary.json` read; no modern translation opened or recalled; Naka Michiyo not available, not used). `units.json` was edited in place by script; no `t`, word count, word order, `p` flag or schema key was changed. `gloss.json` does not exist yet; pass 2 will check it.

## Totals

| severity | changes |
|---|---|
| major | 0 |
| moderate | 22 |
| minor | 83 |
| trivial | 32 |
| **all** | **137** |

A spelling rule applied across many units (the `bulk` lines) counts as one change. A change to a morph gloss and the note that explains it count separately.

## Method notes

- Every `t` was re-cut from the packet by script (462 packet rows, all consumed once, in order, 90 units; `t` of every unit identical to the draft). `p` flags and keys compared with the draft unit by unit: unchanged.
- Every bracketed Ming gloss in every morph (all 745 morphs) was checked by script against the packet's Ming column (VS16 and spaces ignored): all now substrings of the word's own Ming; the one blank Ming (packet rows 58 and 259, `[no Ming gloss]`) is the published marker. Every 'Ming X' cited inside a morph gloss was checked the same way (a cited-from-elsewhere reading in #25 and a Han variant in #26 corrected), and every Han string in the notes was checked against the packet (three wrong citations corrected: #30, #50, #65).
- Names: every English form in `i`, notes, glosses, `about`, `titleEn` and `part` was checked against the published parts' rules (ž→j, č→ch, ṅ→ng, γ̇→', γ→q, ġ→g, j→y; ö and ü kept; Qaγan = Qahan; -Baγ̇atur = -Ba'atur; peoples as 'the Mongols', 'the Tatars'). The draft broke these rules in some sixty places (see the `bulk` lines).
- The draft's -lüġe / -luγ̇a ('as soon as'): the published glossary has `deġü-lüġe-beġen`, where lüġe is the postposition 'together with'; a participle + lüġe is 'as soon as'. The glosses now say so (tentative); pass 2 should keep the new glossary entries `lüġe` / `luγ̇a` apart from the past narrative -luγ̇a of `aluγ̇a` (which is also the ending of `aisuluγ̇a`, #70 and #73).
- Passes made over each unit: grammatical labels against the form; l word by word against t; l against i for sense and force (converb vs finite verb, conditional vs imperative, active vs passive, supplied words); remembered English; consistency with the published renderings.

## What the drafter's flagged doubts came to

- **§55 (#0–#16).** The three pursuers as the unstated subject of `kürküi-lüġe`: kept, flagged. `busud` (#6): kept as unsettled; i no longer invents 'other men' (now 'unlike faces'). `busu nerete-ji … nereidüjü` (#11): the reading 'take another woman and call her Högelün' kept, now with 'take' flagged as supplied and without the speculation about 'keeping' women. `böġesü` (#8, #10): the drafter made it a command; it is the conditional, now 'if only you have your life'. `ele` with `ker` (#25, #28): the Ming glosses it 般 'sort', not 'indeed'. `γoloγ` (#12): 'carry off' kept, 'save … out of here' removed.
- **§56 (#18–#37).** `dergečežü`: 'clinging' kept as the drafter's guess, now marked where reused (#30). `tolkistala`/`daγ̇uristala` (#29): the clauses are `-tala` ('until, so that') and 'with a great voice' belongs to the weeping, not to the ringing woods; the accusative on `müren-(n)i` is now discussed. `simboli`/`idqaba` (#35): stem uncertain, said so; 'on' removed from i. `teberikü` (#31): address, kept, with 'O' like #32.
- **§57–58 (#38–#48).** `iregseġer` (#38): the reading 'because Ambaqai Qahan had named the two' kept; the Ming's 說來 ('said') is not in i and the note still says so. `qaγ̇uluγa` (#44): 'ditch' (Ming 路渠) against 'road' (§56, 道路): both kept, the difference now stated. `ösül ösün` (#48): doublet kept, hedged.
- **§59 (#49–#55).** `teriġüten` (#49): the Ming here is 等項 'and the like'; 'the other headmen'. `abčiraγsan-dur` (#54): the drafter's passive 'was brought in' lost the accusative and the missing agent; now 'at the bringing of …'. `siγ̇a` (#53): 'knucklebone' marked as outside the sources.
- **§60–§63 (#56–#89).** `Ongiradai` (#68): 'Onggirat' is outside knowledge and gone. The speaker through #75–#88 is De-Sečen, not Yesügei (#80, wrong in the draft's note). `Ambar ele sai üže-ġülümü` (#84): the drafter's guess kept, 'I thought' and 'me' flagged. `aqu ta` (#88): kept as an exclamation, 'you have' removed.

## Changes

Format: unit · field · severity · what was wrong · what was done. Unit numbers (#) count from 0 in `units.json`; word indices (w) count from 0 within the unit.

- #0 · i · **minor** · 'When the three came up' drops the force of -lüġe ('as soon as', as l has it) · 'As soon as'
- #0 · n · **minor** · called the participle -qui although the form is -küi, and left -lüġe as a bare 'clause-linker' · form named correctly; the link to lüġe 'together with' (published) given as the reason for 'as soon as'
- #0 w0 · morph kür- / -küi / -lüġe · **minor** · two morphs (stem + -lüġe) with the participle inside the stem's gloss; -lüġe glossed only 'clause-linker' · three morphs; -lüġe tied to the published postposition 'together with', 'as soon as' after a participle (tentative)
- #1 · i · **minor** · 'and hid' turns the -qui-luγ̇a time-clause into a plain coordinate verb; l has 'hid-as-soon-as' · 'as soon as he was hidden'
- #1 · n · **minor** · -luγ̇a left unexplained · tied to -lüġe
- #1 · n · **minor** · 'the fourth word of a long converb chain' is false: the -luγ̇a word is the seventh word of its unit and the chain began in the unit before · corrected
- #2 · i · **minor** · 'and' joined a main clause to a time-clause that unit 1 now closes with 'as soon as' · 'and' removed
- #2 · n · **moderate** · the note says in-ü is read as 'their', but i says 'pursued him' and the in-ü stands after qoināča, not after γurbaγ̇ula: note and i contradicted each other · note says what i does: 'from behind him'
- #2 · n · **minor** · 'uda- delay, follow': 'follow' is not a meaning the sources give; the note had just said the stem cannot be split off · removed
- #4 · n · **minor** · 'Üžin lady' stated as fact; the Ming glosses only the whole pair as a woman's name · hedged
- #5 · i · **trivial** · 'marked' is not the sense of uqa- 'understand, perceive' (l: 'perceived') · 'perceived'
- #6 · i · **moderate** · 'not the faces of other men' invents 'other men' (busu 'other' + plural d; the words are 'other than faces') and an ordinary-man contrast the form does not state · 'unlike faces', which keeps the riddle
- #6 · n · **minor** · i and note not tied together · stated
- #7 · i · **moderate** · 'There are faces that are reaching' drops the possessive plural -tan ('face-havers'); the note itself reads 'those with faces' · 'ones with faces that reach to your life'
- #7 · n · **minor** · 'men' is not in čiraitan · 'those'
- #8 · i · **moderate** · böġesü is the conditional ('if it be'); i made it a command, 'Only keep your life' · 'If only you have your life' (genitive possessor + 'be' = 'have')
- #8 · n · **moderate** · note defended the imperative as 'a wish: while you live' · condition, with the grammar stated
- #9 · n · **minor** · the last sentence is unintelligible and speculates about 'the pursuers' goods' · rewritten to what the text says
- #10 · i · **moderate** · command 'Only keep your life' for the conditional böġesü (as unit 8) · 'If only you have your life'
- #11 · i · **moderate** · 'give one of them another name' reads busu nerete-ji (accusative: 'one having another name') as 'give a name'; 'of them' is not in the words · 'take one who has another name, and call her Högelün too'; 'take' flagged in the note
- #11 · n · **minor** · 'keep other women', 'rather odd': neither is in the words; the speaker is called 'Čiledü's wife' where the unit names her · said what the grammar and the speaker allow; 'take' flagged
- #12 · i · **moderate** · 'Save your own life; take it out of here' adds 'save' and 'out of here' (the Ming 刁出去 is 'carry off in the mouth, go out') and doubles one verb into two commands · 'carry your own life off'
- #13 · n · **trivial** · inference stated as fact · hedged
- #14 · n · **minor** · 'for a keepsake' is not in the Ming or the words · removed
- #14 · n · **minor** · note says -dču, morph said -čü after a stem naruid- · note and morph agree (naru(i)- + -dču, stem unanalysed)
- #14 w4 · morph naru(i)- · **minor** · stem naruid- + -čü contradicts the note ('a converb in -dču') · lemma naru(i)-, -dču
- #14 w4 · morph -dču · **minor** · -čü contradicts the note · -dču
- #15 · i · **minor** · kürčü ('arriving') was rendered 'came up' and aisuqu-luγ̇a ('as soon as coming') 'arrived': the two verbs were swapped · kürčü 'arrived', aisuqu-luγ̇a 'as soon as they came up'
- #15 · n · **minor** · 'this and §56' omits §62; -luγ̇a unexplained · corrected
- #16 · i · **minor** · qurdun 'swiftly' (Ming 快) dropped · 'swiftly' restored
- #16 · n · **trivial** · 'unit 2' is ambiguous (the reader sees no unit numbers) · named the unit
- #19 · i · **minor** · 'and on and on they chased' is not in the words; -tala 'until' is lost · 'until they had crossed seven hills'
- #20 · i · **minor** · 'then' is not in the words; irežü 'coming' dropped; 'the Brave' for the name's -Baγ̇atur against the published 'Yesügei-Ba'atur' · 'turned back and came'; name as published
- #24 · n · **minor** · variant stated as fact · hedged
- #24 · n · **trivial** · punctuation added to l and i without saying so · said
- #25 · l · **minor** · 'how indeed': the Ming gives ele the sense 般 'sort, manner', not 'indeed' (但) · 'how-like'
- #25 · i · **moderate** · 'are' and 'then' are not in the words (ker ele 'how-like') · removed
- #25 · n · **minor** · ele read 'indeed' against the Ming's 般; 'follows its count' is meaningless · corrected
- #25 w2 · morph ele · **minor** · gloss 'indeed, only' for a word the Ming glosses 般 · sense from the Ming; the other reading kept as the elsewhere-sense
- #26 · n · **minor** · -te 'times: once' asserted as a suffix meaning · hedged
- #26 · n · **trivial** · character not the packet's (丢) · packet's character
- #26 · n · **trivial** · as above · as above
- #26 w3 · morph oγ̇or- · **trivial** · character not the packet's (丟 for 丢) · packet's character
- #27 · n · **minor** · the two words were analysed by different patterns (uruγ-šida, qoina-γšida) · one pattern for both: stem + -γšida
- #27 w1, w3 · morph uruγšida, qoinaγšida · **minor** · uruγšida analysed uruγ + -šida but qoinaγšida qoina + -γšida: two patterns for one ending · both stem + -γšida; the stem uru- marked uncertain
- #28 · l · **minor** · 'how indeed' (see unit 25) · 'how-like'
- #28 · i · **trivial** · 'cried' is not in kēġed 'having said' (l) · 'said'
- #28 · n · **minor** · as unit 25 · as unit 25
- #28 · n · **minor** · 'the long ē stands for the diphthong of keġe-' is unexplained; the morph -ed does not match ergü-ġed (unit 42) · analysis matches ergüġed
- #28 w4 · morph -ġed · **minor** · -ed is not an ending found elsewhere in the part; ergüġed has -ġed · lemma -ġed
- #28 w1 · morph ele · **minor** · gloss 'indeed, only' for a word the Ming glosses 般 · as unit 25
- #29 · l · **minor** · -tala ('until') missing from l, though l has it for dabatala (unit 19) · '-until' added twice
- #29 · i · **moderate** · 'with a great voice' attached to the woods and stream resounding, but daγ̇u-bar belongs to uilažu 'weeping'; the -tala clauses ('so that') were turned into 'as' clauses of time · 'with a great voice' goes with weeping; the -tala clauses follow as the result
- #29 · n · **moderate** · note 'as the river heaved' matches neither -tala nor the accusative; the accusative was not discussed · both readings stated; i keeps the intransitive
- #30 · i · **minor** · 'hurrying along' is not in dergečežü jabužu (the note reads them 'clinging as he went') · 'clinging on as he went'
- #30 · n · **moderate** · the note cites 迓步周 as the Ming gloss and translates it 'walking along': 迓步周 is the Han transcription of jabužu; the Ming is 行著 · right Ming; guess marked
- #31 · i · **trivial** · unit 32 has 'O weeping one' (an address), unit 31 'Embracing one' with no 'O' for the same construction · 'O' added for the pair
- #32 · n · **trivial** · inference stated as fact · hedged
- #34 · n · **minor** · unintelligible parenthesis · removed
- #35 · i · **trivial** · 'on' is not in idqaba (Ming 勸 'urge') · 'on' removed
- #35 · n · **trivial** · inference stated as fact · hedged
- #35 · n · **trivial** · character not the packet's · packet's character
- #37 · i · **minor** · 'home' is not in this unit (ger-türjen is in the unit before) · removed
- #37 · n · **minor** · 'as at the end of other tales in the work' cites usage that is not in the sources · removed
- #38 · l · **trivial** · a colon in l that is not in t and not in i · comma
- #39 · n · **trivial** · plural stated as fact · hedged
- #40 · n · **trivial** · 'in the packet's wording' is process talk, and 教 is not the packet's character (敎) · packet's character, plain gloss
- #44 · i · **moderate** · 'the paths were worn to ruts', 'lay up to': the words say only that it became ditches rib-having and dust knee-having; 'worn' and 'paths' are invented, and 'rib-deep, knee-deep' is a ready-made formula rather than a rebuild · rebuilt from -ta / -te 'having' and the Ming 沒 'reach to'
- #44 · n · **moderate** · note defended the invented 'ruts'; the different Ming of qaγ̇uluγa (unit 34 'road') not mentioned · rewritten
- #48 · n · **trivial** · stated as fact · hedged
- #49 · i · **minor** · 'their chiefs': the Ming 等項 is 'and the like'; the unit's teriġüten is a plural possessive of teriġü 'head' and l has 'chiefs-and-so' · 'the other headmen' (from 等 'and the like' and teriġü 'head')
- #49 · n · **minor** · 'known-forms' is a pipeline file name in a reader's note · plain statement
- #49 w5 · morph teriġü · **minor** · 'head, chief' gives 'chief' as a dictionary meaning; the Ming has 項 · 'chief' marked as a reading
- #49 w5 · morph -ten · **minor** · gloss 'those with heads, and the like' gave the sense of the whole word to the suffix · Ming 等 given to -ten
- #50 · i · **minor** · 'back' is not in ireġesü 'when he came' · removed
- #50 · n · **minor** · the Ming of this word is 懷孕; the note cites the Ming of the published entry · this packet's Ming
- #51 · i · **minor** · 'was at … and at that very time' makes two clauses of büküi-dür 'when being' and repeats the žöb tende 'right there' of the next unit · 'while at …'
- #51 · n · **minor** · 'Deliun hill' and 'Boldaγ is a hill-name' stated as fact; neither is in the sources · said so
- #53 · n · **minor** · 'knucklebone' presented as the meaning of the Ming · origin said
- #53 · n · **trivial** · same sense as adqu- (§63) analysed as a separate stem without a word · cross-reference
- #53 w3 · morph siγ̇a · **minor** · 'knucklebone (Ming 髀石)' gives an outside meaning as the Ming's · said so
- #53 w6 · morph hadqu- · **trivial** · stem not linked to adqu- · linked
- #54 · i · **moderate** · 'was brought in': the verb is active (abčira-γsan) with an accusative object (l: [acc]); the passive makes the Tatar the one brought in by an unnamed agent and hides that there is an agent · 'at the bringing of …', which keeps both the object and the missing agent
- #54 · n · **moderate** · note defended the passive · active stated
- #57 · i · **trivial** · 'also' is not in the words · removed
- #57 · n · **trivial** · stated as fact · hedged
- #57 w4 · morph -bi · **trivial** · 'a variant of -be' stated as fact · hedged
- #58 · n · **minor** · the next unit has no büküi-dür · corrected
- #61 · n · **trivial** · 'title' not in the sources · 'second element'
- #64 · i · **minor** · 'went to' is a verb supplied here although jorčiba stands three units on and unit 66 then says 'set out' again · verb left to unit 66
- #64 · n · **minor** · note defended the supplied verb; 'his' not flagged · flagged
- #64 · n · **trivial** · stated as fact · hedged
- #65 · n · **trivial** · cites 女子 as the Ming of öki; the packet has 女 · packet's Ming
- #68 · i · **moderate** · 'of the Onggirat' gives a people-name that is not in Shiratori's word or the Ming (人氏); the published parts keep 'Uriangqadai' · Shiratori's form kept
- #68 · n · **moderate** · 'the Ongirat people' is outside knowledge stated as fact · hedged, outside knowledge dropped
- #68 w0 · morph Ongiradai · **moderate** · 'a man of the Ongirat people' is outside knowledge · Ming's sense and the published -dai only
- #70 · i · **moderate** · 'at whom are you aiming, that you come?' turns the converb žorižü ('aiming') and the finite verb into two clauses joined by 'that', and gives -laγ̇a a subjunctive force · 'aiming at whom have you come?'
- #70 · n · **trivial** · 'not yet true' stated as a fact of the story · softened
- #70 · n · **minor** · 'an ending I cannot name' although -luγ̇a is a published ending; 'the next unit' is three units on · ending named, hedged
- #70 w4 · morph -laγ̇a · **minor** · 'past ending (uncertain)' for a published ending · named
- #72 · i · **minor** · 'This son of mine's' is clumsy and commits min-u to 'son' without saying so · 'This my son's'; the other reading said in the note
- #72 · n · **minor** · i's choice between two readings not stated · stated
- #73 · n · **minor** · 'back-vowel form' is wrong: both are back-vowel; the difference is a vowel spelling · corrected
- #73 w4 · morph -luγ̇a · **minor** · 'past ending (uncertain)' for a published ending · named
- #74 · n · **minor** · a mark after a colon cannot be a closing quote (the speech of unit 72–73 closed at aisuluγ̇a") · corrected
- #76 · i · **minor** · 'a son indeed': 'indeed' is not in köġün bi · 'he is a son'
- #77 · n · **trivial** · 'last night' for 'this night' unexplained · explained
- #78 · l · **trivial** · a colon in l not in t · comma
- #78 · i · **moderate** · 'In it … in its claws': 'in it' replaces Bi 'I' (dropped), 'claws' is not in adqun · 'I saw' (flagged as supplied), no claws
- #78 · n · **minor** · supply not flagged · flagged
- #80 · i · **minor** · 'the man' presumes a known person (küġün has no article; Ming 人) · 'a man'
- #80 · n · **trivial** · küün is not the token's form · corrected
- #80 · n · **moderate** · the note makes Yesügei the speaker of units 77–88, but he is the addressee: De-Sečen says 'I dreamed' (unit 77, bi) and 'my hand' (min-u) · speaker corrected
- #80 w2 · morph küġün · **trivial** · 'person, man' without the contrast with köġün · contrast added
- #81 · i · **minor** · 'one has only looked at and seen': 'one', 'only' and 'has' are not in the words (no ele here) · words only
- #81 · n · **minor** · '[only]' not in the words · removed
- #82 · i · **minor** · 'has gripped them and brought them, and alighted' makes the two converbs finite verbs · converbs kept
- #82 · n · **trivial** · §59 has abčiraγsan-dur, not the same form; the other abčira- is in §56 · corrected
- #84 · n · **minor** · 'I thought' and 'me' are supplied unflagged · flagged
- #87 · n · **trivial** · 'the -n of the adjective' asserted · hedged
- #88 · i · **minor** · 'you have there' makes 'you' the possessor; aqu is 'there is' and ta is the addressee · 'there is, you!'
- #88 · n · **minor** · 'closing quote mark … by Shiratori's logic' says Shiratori has one; t has none · said that the mark is mine
- #89 · i · **minor** · 'omen' loses the Ming's 吉 'lucky'; 'told' for 吿 'announce' · 'lucky omen', 'announced'
- #89 · n · **minor** · 'the Ming says only omen' contradicts 吉兆 'lucky omen' in the same sentence · corrected
- #89 · n · **minor** · 'it' unflagged; 'as often' is not sourced · flagged
- bulk · morph -lüġe / -luγ̇a (#3 w5, #1 w6, #14 w5, #15 w4) · **minor** · -lüġe / -luγ̇a glossed as a bare 'as soon as, once'; the published glossary has lüġe as the postposition 'together with' (deġü-lüġe-beġen), which is where the sense comes from · glossed as the postposition used after a participle, tentative, with the published entry named
- bulk · morph -te / -ta "times" (#26 w0 w4, #27 w0 w2, #47 w5) · **minor** · -te / -ta 'times: once' stated as a suffix meaning · hedged: probably the dative-locative, 'times' from the Ming's 遍
- bulk · morph Ming brackets · **minor** · the drafter put the whole word's Ming gloss in the bracket of every morph of a multi-morph word (249 words, 532 morphs); a suffix then claims the whole word's Ming · each morph now carries its own bracketed Ming part where the packet's Ming column splits (行 on a dative, 自的 on a reflexive, 著/着 on a converb, 了 on a past, 每 on a plural, 的 on a genitive, 呵 on -lüġe/-luγ̇a, and so on); where the column does not split, the stem keeps the whole-word gloss and the suffix gets 'part of …' as in the published parts; every bracket checked as a substring of the packet's Ming (VS16 and spaces ignored)
- bulk · name: Khan → Qahan · **minor** · i, notes, about, title say 'Khan' for Qaγan; the published parts (§§43–54) have 'Qutula Qahan', 'Ambaqai Qahan' · Qahan (i, n, about)
- bulk · name: Ambaghai → Ambaqai · **minor** · γ is q (published Ambaqai) · respelled (i, n, glosses)
- bulk · name: Hoelun-Ujin → Högelün-Üjin · **minor** · remembered form; the published rule is ž→j, ġ→g (Tödögen, Jegüredei), ö and ü kept (Ödchigin, Yesügei) · Högelün / Högelün-Üjin in i, n, glosses, about, titleEn, part
- bulk · name: Chiledu → Chiledü · **minor** · ü dropped (published Yeke-Chiledü) · respelled
- bulk · name: Yesugei → Yesügei; Yesügei the Brave → Yesügei-Ba'atur · **minor** · ü dropped in six places while kept in fifteen; 'the Brave' where the published i keeps 'Yesügei-Ba'atur' · respelled; glosses give both forms
- bulk · name: Negun-Taishi, Daritai-Odchigin, Temujin(-Uge), Temuge(-Odchigin), Temulun, Chigurku, Kodon-Baraqa · **minor** · ö / ü dropped (published Negün-Taishi, Daritai-Ödchigin, Möngetü) · Negün-Taishi, Daritai-Ödchigin, Temüjin(-Üge), Temüge(-Ödchigin), Temülün, Chigürkü, Ködön-Baraqa
- bulk · name: Qadaan, Taichiud, Qachiun, Olqunuud → Qada'an, Taichi'ud, Qachi'un, Olqunu'ud · **minor** · γ̇ is an apostrophe (published Qara-Qada'an, Taichi'ud, Qachi'u) · respelled
- bulk · name: Jochi → Jüchi; Deliun-Boldaq → Deligün-Boldaq · **minor** · Žüči is Jüchi (published); Deliġün is Deligün (ġ is g, ü kept) · respelled
- bulk · l: γ̇ and ṅ in names · **minor** · l has Qadaγan, Taičiγud, Baγatur, Qačiγun, Olqunuγud (dot lost) and 'Činggis' where Shiratori writes Qadaγ̇an, Taičiγ̇ud, Baγ̇atur, Qačiγ̇un, Olqunuγ̇ud, Čiṅgis (published l keeps the dot and ṅ) · Shiratori's forms restored (10 units)

## Findings refused

- #0 / #14 / #15 the three pursuers, 'she', 'he' supplied as subjects: kept; the reflexive -ban/-jan and the story fix them, and the notes say they are supplied.
- #3 `tergen-dur(i)-jan` 'to his own cart': kept; the Ming 車子自的行 (cart-own-to) agrees.
- #9 'each one is a girl … each one is a lady': kept; `tutun` 'each' (Ming 每) is the drafter's reading and the note says it is uncertain.
- #13 'taking in my scent' for `hünüsčü` 'smelling': kept (trivial); l has 'smelling'.
- #22 / #30 'held fast / clinging' for `dergečežü`: kept as a flagged guess; no better reading in the sources (the Ming's first character is rare).
- #24 'tuft' for `kekül(i)-jen` and 'open country' for `keġer γažar-a`: kept; the note says the first is only a reading.
- #26 / #27 / #47 `nigente`, `γurbanta` as 'once', 'thirteen times': kept; only the -te / -ta analysis was hedged.
- #38 i leaves out the Ming's 說來 ('said') in `iregseġer`: kept; the note states the reading and the doubt about the genitive.
- #41 'The Mongols rejoiced': kept; the note already says the first genitive is the possessor of the joy.
- #46 'rode against the Tatar people': kept as the drafter's sense of `morilaba` + dative; the note says the Ming has only 'got on horse'.
- #48 'vengeance for Ambaqai Qahan': kept as the reading of the genitive.
- #53 'the size of a knucklebone': kept; `tedüi` 'so much, like' and the Ming 般 support 'the size'. Only the source of 'knucklebone' was marked.
- #55 'gave him the name': kept; 'him' is the natural object of `nere ögküi` (the note says so).
- #66 'took Temüjin with him': kept; 'with him' follows `abuγ̇ad` 'having taken'.
- #84 'Surely it shows me something good': kept as the drafter's flagged guess; `ele` 'indeed' and the causative are the only evidence.
- #86 i drops `ele` (Ming 但): kept (trivial); the sense does not change.
- `bolutala` (#44) and `boluγ̇ad` (#45) analysed bol- + -u(γ̇)- : kept, matching the published entry for `abuγ̇ad` (ab- + -uγ̇ad); the published `boluγ̇asu` has `bolu-`, so pass 2 should make the glossary say that the stem is bol-/bolu- in either way.
- `keġe- + -n` split as [道] + [麽] for Ming 麽道, and `-γa-` as [敎]: kept; these are my assignments of the Ming's characters, the only split the column allows, and carry the same hedge as every analysis in the part.
- Whether ġ should be g in names (Högelün, Deligün, Tödögen): rule taken from the §§43–54 review, where it was left open for the owner; I applied it consistently and did not reopen it. The familiar forms (Hö'elün, Qahan's Chinggis) are not used.

## Remaining doubts (for pass 2 and the owner)

- Pass 2 glossary: new entries for `lüġe` / `luγ̇a` (postposition 'together with', after a participle 'as soon as'; keep apart from the past -luγ̇a of `aluγ̇a`, `aisuluγ̇a`, `aisulaγ̇a`); `ele` needs a broadening for 般 ('how-like', after `ker`); `tedüi` ('like, the size of', Ming 般); `qaγ̇uluγa` ('road' and 'ditch'); `teriġüten` (Ming 等項); `tutun`, `qojar` and the -ni/-jan/-jen known entries cover this part's use but should be checked against the new notes.
- #6 / #7 / #11 Čiledü's wife's speech: `busud`, `čiraitan`, `busu nerete-ji … nereidüjü`, still unsettled in sense.
- #29 whether `müren-(n)i … tolkistala` is transitive ('she shook the river') or the river simply heaved.
- #35 `simboli` and `idqaba`: stems unknown.
- #38 `iregseġer`: the Ming's 說來 against 'come'.
- #54 the agent of `abčira-` (Yesügei by context only) and who says the quoted words.
- #68 the clan behind `Ongiradai`; #72 whom `min-u` qualifies.
- #80 who 'the man' is and how the dream telling is framed inside De-Sečen's speech; #84 `üže-ġülümü`; #88 `aqu ta`.
- The names rule (ġ → g, Qaγan → Qahan) and the new spellings of Högelün and Deligün, left open for the owner.


# Review, pass 2 — secret-history-055-063 (§§55–63)

Reviewer: adversarial pass 2, on `units.json` once more and, for the first time, `gloss.json` (written by the Sonnet glosser). Read: conventions, runbooks, `../run3/RUNBOOK.md` §2, packet, `novel-forms.json`, `known-forms.json`, `units.json`, `gloss.json`, `secret-history-glossary.json`, the published §§43–54 with its `gloss.json` and `review.md`. No modern translation opened or recalled. Edits were made in place by script (`gloss.json`, `units.json`); no `t`, word count or order, `p` flag, lemma, morph count or schema key was changed (compared with the pass-1 file by script).

## Totals (pass 2)

| severity | changes |
|---|---|
| major | 0 |
| moderate | 7 |
| minor | 32 |
| trivial | 28 |
| **all** | **67** |

Of these, 42 are to `gloss.json` (34 in the 216 new entries, 8 in the 12 `__broaden__` entries) and 25 to `units.json`. A change to a note and to the morph it explains count separately.

## Method notes

- **Coverage (by script, with the reader's own tokenizer `R.tokens`).** 312 distinct tokens in the `t` of the 90 units; the shared glossary (781 entries) + the 216 new `gloss.json` keys cover all 312, none missing; no new key is unused; no new key is already in the shared glossary (the build would ignore it); no empty value; the 216 new keys equal `novel-forms.json` exactly. A dry run of `H.assemble` + `H.validate` + `common_checks` (nothing written; `r3.py build` itself was not run, because it writes the story, the glossary and `stories.json`) gave 0 errors, 0 warnings, glossary 997 entries, no uncovered token.
- **Every new entry** was set beside every occurrence of its token in `units.json` (word, packet Ming, morph lemmas and glosses): dictionary form is the lemma of the morph that carries it (script check: all 215 entries whose lemma is a morph lemma match; `ni-jen` is the one composite key, intentionally); the closing Ming bracket equals the packet's Ming of the token (VS16 and spaces ignored; the two blank-Ming words `i`, `ösün` carry the published `[no Ming gloss]`); every entry has ' — ' and a grammar label; meanings were set against the Ming, not against memory.
- **The 12 `__broaden__` entries:** each old entry text equals the entry in `secret-history-glossary.json` character for character, then ' · ' and the new reading (script check). Eight had a sentence of one line quoted inside the new reading; those were cut back to the form's own sense.
- **Known forms not broadened:** all 96 known entries were read against their occurrences. Twelve are broadened; the rest cover this part's use. Two borderline cases left alone: `qojar` ('it follows the pair it counts', but unit 25 puts it before its noun, a note on usage, not a sense), and `bi` ('I' and 'is, exists', both already in the entry).
- **Units:** l and i read once more word by word for every unit; every § cross-reference in the notes checked against the packet's § numbers (all correct); every Ming bracket of every morph re-checked as a substring of the packet's Ming (0 mismatches); morphs scanned for repeated or contradictory glosses of the same word (four found, fixed).
- The glosser's habits that needed correcting: **pinning to the line** (story roles, 'on the Onan', 'a Tatar', 'here with ülü', quoted sentences in the broadened entries); **remembered or outside meanings** ('hearth-prince', 'the later Chinggis', 'ankle-bone for games', 'a three-year-old animal', 'kin by birth', 'mother's kin', 'get out of here'); **disagreeing with the published parts** (`törežüġüi`/`keġežüġü` against the published past narrative `kēžüġü`; `monγol` against the published `monγol-i`); and one Ming bracket that carried the 行 of the neighbouring suffix (`de-sečen`). No modern forms were invented in the stems; every stem the glosser marked uncertain was left marked.

## Changes

Format: unit or entry · field · severity · what was wrong · what was done. Entries are named by their glossary key; units by their number from 0.

- gloss · čiledü · **trivial** · entry pinned to the line (a § range and a story role) · rewritten (see gloss.json)
- gloss · höġelün-üžin · **minor** · story role pinned to the line; not a dictionary fact · rewritten (see gloss.json)
- gloss · höġelün · **trivial** · story role pinned to the line · rewritten (see gloss.json)
- gloss · jesügei · **trivial** · story role pinned to the line · rewritten (see gloss.json)
- gloss · busud · **minor** · pinned to a line and to a § number · rewritten (see gloss.json)
- gloss · qubitu · **trivial** · 'on a yellow horse' is this line's rendering, not the form's · rewritten (see gloss.json)
- gloss · uqaba-u · **trivial** · 'you' is supplied from one line · rewritten (see gloss.json)
- gloss · ele · **minor** · entry quoted two other lines (ambar ele, čima-ji ele) and carried no clear particle label; rewritten general, ele named an emphatic particle · rewritten (see gloss.json)
- gloss · γoloγ · **moderate** · 'get out of here' is a remembered gloss that pass 1 had already removed from i; Ming 刁 is 'carry in the mouth' · rewritten (see gloss.json)
- gloss · oluqu · **trivial** · pinned to the line (ülü) · rewritten (see gloss.json)
- gloss · qojar-tur · **minor** · Ming 裏 is 'in'; 'with' is not its sense and the morph says 'with, among' · rewritten (see gloss.json)
- gloss · monγol · **minor** · published monγol-i has 'the Mongols (the Ming glosses 達達 Tatars)'; 'the Ming's word for Mongol and Tatar' says more than the sources show · rewritten (see gloss.json)
- gloss · moṅγol-un · **trivial** · aligned with the published Monγol entries · rewritten (see gloss.json)
- gloss · temüžin · **moderate** · 'the later Chinggis' is outside knowledge, not in these §§ · rewritten (see gloss.json)
- gloss · temüžin-üge · **moderate** · story content pinned to one line and stated as an etymology · rewritten (see gloss.json)
- gloss · ködön-baraγa · **minor** · story role (Tatar) pinned to the line, not a property of the name · rewritten (see gloss.json)
- gloss · žali-buqa · **minor** · story role (Tatar) pinned to the line, not a property of the name · rewritten (see gloss.json)
- gloss · qori-buqa · **minor** · story role (Tatar) pinned to the line, not a property of the name · rewritten (see gloss.json)
- gloss · temüge-ödčigin · **moderate** · 'hearth-prince' is outside knowledge (the published Daritai-Ödčigin and Tödögen-Ödčigin carry no gloss), and 'the youngest' is the line · rewritten (see gloss.json)
- gloss · qačiγ̇un-elči · **trivial** · source of the reading said · rewritten (see gloss.json)
- gloss · siγ̇a-jin · **minor** · 'the ankle-bone for games' is outside knowledge stated as the meaning; 'of a knucklebone' pinned the case to the line · rewritten (see gloss.json)
- gloss · kijad · **trivial** · hedged and tied to the published name · rewritten (see gloss.json)
- gloss · törgüd · **minor** · 'kin by birth' is outside knowledge; the Ming gives only 家 · rewritten (see gloss.json)
- gloss · naγaču-nar-ača · **trivial** · 'mother's kin' is not the Ming's sense · rewritten (see gloss.json)
- gloss · γunan · **minor** · 'a three-year-old animal' is not in the Ming (三歲 only); no grammar label · rewritten (see gloss.json)
- gloss · ölegetei · **trivial** · 'in the cradle' is the line's rendering · rewritten (see gloss.json)
- gloss · ösün · **trivial** · grammar label missing · rewritten (see gloss.json)
- gloss · daγ̇uristala · **trivial** · derivation stated as fact · rewritten (see gloss.json)
- gloss · törežüġüi · **moderate** · split as converb -žü + 'was' against the published past narrative -žüġü (kēžüġü) and against the same word's other morph gloss (u53 'past: was born') · rewritten (see gloss.json)
- gloss · keġežüġü · **minor** · called the ending uncertain 'as with törežüġüi', where the published kēžüġü treats -žüġü as the past narrative · rewritten (see gloss.json)
- gloss · de-sečen · **minor** · bracket carried the 行 that belongs to the following -(n)i, not to the name · rewritten (see gloss.json)
- gloss · deliġün-boldaγ-a · **minor** · pinned to the neighbouring word (Onan-(n)u) in one line · rewritten (see gloss.json)
- gloss · γorqonaγ · **minor** · pinned to the neighbouring word (Onan-(n)u) in one line · rewritten (see gloss.json)
- gloss · qabirγa-ta · **trivial** · 'submerged' overstates; matches the unit's 'reach to' · rewritten (see gloss.json)
- gloss · böġesü (broaden) · **minor** · quoted a whole sentence of one line · rewritten (see gloss.json)
- gloss · ni (broaden) · **minor** · 'in one place' topic-like: two units (§59 and §61) read so; addition kept general · rewritten (see gloss.json)
- gloss · tedüi (broaden) · **minor** · quoted a whole sentence and the one line's 'like a knucklebone' · rewritten (see gloss.json)
- gloss · aqu (broaden) · **minor** · quoted a whole line ('what a dream there is, you') · rewritten (see gloss.json)
- gloss · žöb (broaden) · **trivial** · pinned to the line's repetition (žöb žöb tende) · rewritten (see gloss.json)
- gloss · keġelitei (broaden) · **trivial** · quoted a whole line · rewritten (see gloss.json)
- gloss · teriġüten (broaden) · **minor** · pinned to the line's name (Qori-Buqa) · rewritten (see gloss.json)
- gloss · daγ̇uližu (broaden) · **trivial** · pinned to a line (Tatar-i daγ̇uližu) · rewritten (see gloss.json)
- #47 w5 · morph -ta · **minor** · γurbanta is 'three times' ('once' is the gloss of nigente); the bulk fix of pass 1 copied 'once' here · changed
- #20 w3 · morph Jesügei-Baγ̇atur · **trivial** · respelling by pass 1 left the form twice · changed
- #49 w1 · morph Jesügei-Baγ̇atur · **trivial** · as above · changed
- #57 w0 · morph Temülün · **trivial** · parenthesis repeats the word · changed
- #52 w4 · morph -žüġüi · **moderate** · split as converb + 'was' against the published past narrative -žüġü, and against the morph of the same word in unit 53 · changed
- #53 w7 · morph -žüġüi · **minor** · same word, two different morph glosses (unit 52 / unit 53) · changed
- #70 w5 · morph -žüġü · **trivial** · as the published kēžüġü · changed
- #73 w5 · morph -žüġü · **trivial** · as the published kēžüġü · changed
- #5 · n · **trivial** · an English phrase that arrives ready-made ('taken their measure'), not built from uqa- 'perceive' (l, i) · changed
- #12 · n · **minor** · invented stem meaning 'to pass out' offered in the same breath as 'I cannot name the stem' · changed
- #14 · n · **trivial** · 'down' is in neither l, i nor the Ming 探 · changed
- #20 · n · **minor** · 'has joined the pursuit' is invented: the three of §55 include Yesügei (the next units name his two brothers) · changed
- #22 · n · **minor** · a verb dergeče- 'to cling along' that is in no source, offered as the possible stem · changed
- #28 · n · **minor** · 'indeed' contradicts the note of unit 25 (ele after ker is 般 'sort', not 'indeed') · changed
- #44 · n · **trivial** · 'submerged' overstates; as the glossary entry now says · changed
- #48 · i · **minor** · ösül ösün (l 'enmity') is not in i at all, and n says it 'is translated once' · changed
- #48 · n · **minor** · n claimed a rendering i did not have; the supplied 'yet' was unflagged · changed
- #52 · n · **minor** · 'known-forms' is a pipeline file name in a reader's note (pass 1 removed one such in #49) · changed
- #52 · n · **moderate** · note analysed the ending as converb + 'is', against the published past narrative -žüġü; now as the glossary entry · changed
- #64 · n · **trivial** · 'by birth' is outside knowledge; as the glossary entry now says · changed
- #70 · l · **minor** · 'you' is not in aisulaγ̇a; l is word by word (i has 'have you come') · changed
- #70 · n · **trivial** · inference stated as a fact of the story · changed
- #77 · i · **minor** · 'my' is not in the words (min-u stands in unit 85 only) and unit 70 has plain 'in-law' · changed
- #85 · i · **minor** · as unit 77 · changed
- #78 · n · **trivial** · 'a hawk' is outside knowledge presented as the Ming's · changed

## Findings refused

- `ongiradai` ('a man of the Ongira(?) clan'): kept. It is built from Shiratori's word minus the published `-dai` of `urjaṅqadai` ('a man of the Uriangqai') and the Ming 人氏; the question mark and the note say it is uncertain, and no outside clan name is used.
- `šinqor` 'gyrfalcon': kept in the entry and in i. The Ming 海靑 is the Chinese name of that bird and 'gyrfalcon' is only our English for it; the note now says so. No better English is available from the sources.
- `siγ̇a` 'knucklebone': kept, with the source of the sense stated (outside the sources; the Ming gives only 'thigh-stone'); the first pass had already marked it.
- `elči` 'envoy' and `taiši` 'prince': kept, because the published glossary has `elčin` 'envoy' and `taiši 'prince'`; only `ödčigin` 'hearth-prince', which has no published gloss, was removed.
- `kijad` 'plural of Kiyan': kept (hedged), since the published glossary has `Möngetü-Kijan`.
- `moṅγol-un` / `monγol`: the Ming 達達 'Tatars' for the Mongols is kept as the Ming's reading, as in the published `monγol-i`.
- `jan`, `jen`, `ni` broadened entries list the stems after which the ending was seen (`tergen-dur(i)-`, `γar-tur(i)-`, `kekül(i)-` …): kept; the published `jan` does the same, and these are citations of the form, not sentences.
- `i`/`olu`: `olu- i` read as a stem and an ending written apart (probably 'will get'): kept, flagged uncertain in entry, morph and note; the Ming gives nothing.
- #6 i 'Their faces are unlike faces': 'Their' is not in the words; kept, the note says the unit is unsettled and i keeps the riddle.
- #9 i 'At the cart's front': 'At' supplied for the bare noun; kept, the note says the grammar is `ölžige tutun ökid` and that the word is unknown.
- #13 i 'taking in my scent' for `hünüsčü` 'smelling': kept (trivial), as in pass 1.
- #46 i 'rode against the Tatar people': kept as in pass 1; the note already states that the Ming has only 'got on horse'.
- #47 l 'two-with' against the entry's 'in, among the two': kept; the note says 'with/among' and i's 'against the two' is flagged as a reading.
- #53 i 'At his birth he was born': clumsy but a literal rendering of `töreküi-dür … törežüġüi`; kept.
- #84 i 'Surely' for `ele`: kept as in pass 1 (flagged guess).
- #86 i 'showed me' for `üžegsen ažuγ̇u` ('was seen/shown'): kept; the note says whether the dream showed or the dreamer saw is not settled.

## Remaining doubts (for the owner)

- **The ending -žüġüi** (`törežüġüi`, §59 twice) as the past narrative -žüġü with a final -i: the glossary now says so on the model of the published `kēžüġü`; the analysis is a guess and is marked.
- **-lüġe / -luγ̇a 'as soon as'** (entries `kürküi-lüġe`, `ireküi-lüġe`, `buruqui-luγ̇a`, `abqui-luγ̇a`, `aisuqu-luγ̇a`; the tokens `lüġe` and `luγ̇a` do not occur apart in this part): tentative, derived from the published postposition 'together with'; kept apart from the past narrative -luγ̇a of `aisuluγ̇a`. If the owner has a better source for the sense, five entries and the matching morphs change together.
- **bol- / bolu-**: `bolutala` and `boluγ̇ad` are analysed `bol-` + linking `-u-`; the published `boluγ̇asu` has `bolu-` as the stem. Both entries say the stem is `bol-`; the difference is only one of segmentation and does not change a meaning.
- **Unsettled in sense** (unchanged since pass 1): §55 `busud`, `čiraitan`, `busu nerete-ji … nereidüjü`; §56 `müren-(n)i … tolkistala` (transitive or not), `simboli`/`idqaba`; §57 `iregseġer` against the Ming's 說來; §59 the agent of `abčira-`; §61 the clan behind `Ongiradai`; §63 `üže-ġülümü`, `aqu ta`.
- **Names:** ġ → g and Qaγan → Qahan (Högelün, Deligün), the rule taken from §§43–54, still open for the owner.
- **Entry-level pinning left in the published glossary** (not this part's to change): the published `jan` entry cites `quruγ̇ud(i)-` and others; the new additions follow that style.
