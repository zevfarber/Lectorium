import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
toks = json.load(open(os.path.join(HERE, 'toks.json')))

ABOUT = ("The fourth part of text ga, the bardo of the wrathful deities, still on the twelfth day. The list of the "
"twenty-eight Īśvarīs goes on: the six of the south, of the west and of the north, each with her colour, her animal's "
"head and what she holds, and then the four gatekeeper yoginīs with the heads of cuckoo, goat, lion and snake, all coming "
"out from inside the dead person's own brain. All of them, the text says, have dawned of themselves from the energy of the "
"self-arisen body: the peaceful deities dawn from the empty aspect of the body of truth, the wrathful from its clear aspect, "
"and to know the fifty-eight blood-drinkers as the natural radiance of one's own awareness is to become a buddha at once. "
"One who does not recognise them sees them as Lords of Death, faints with terror and wanders in saṃsāra. The deities are as "
"vast as the sky, or as Mount Meru, or at the least as tall as eighteen of one's own bodies stacked up; all that appears "
"dawns as light and bodies, one's own appearance, and to recognise this is perfect buddhahood in a single instant. If one "
"does not, the peaceful ones dawn as the Black Protector and the wrathful ones as Yama, the Lord of Death, King of the "
"Teaching, who comes filling the world, biting his lip, holding his tally-stick, crying 'Strike! Kill!', drinking brains and "
"tearing out hearts. Learning and an aeon of practice are no help without recognition; with it, one key point and one word "
"are enough. The dead person has a body of mind and cannot die; he is the form of emptiness, and emptiness cannot harm "
"emptiness; nothing of all this exists outside his own awareness. The part ends with the call on the yidam: the dead "
"person is to take refuge, remember the Three Jewels and his own yidam, and call on him by name for help.")

U = []
def u(end, l, i, n, p=False, gap=None):
    U.append((end, l, i, n, p, gap))

u(21,
"O child-of-noble-family! South from, Delight yellow, pha-wad(?) head, hand in razor holding, and; Peaceful-One red, sea-monster head, hand in vase holding, and;",
"O child of noble family, from the south: the yellow Delight, with the head of a bat(?), holding a razor in her hand; the red Peaceful One, makara-headed, holding a vase;",
"The six Īśvarīs of the south, after the six of the east at the end of 011. As there, each is named and given her colour, her animal's head and what she holds; the names are translated. dga' ba, 'delight' (dga', 'glad'); the other recension calls this goddess rdo rje, 'Vajra'. pha wad: the first letter is doubtful ([?]): its tick may be a tsheg fused to the letter, which would give pa. No word pha wad is known. It is kept as printed and read, with low confidence, as perhaps for pha wang, 'bat', one letter off; the other recension has phag mgo ma, 'sow-headed'. spu gri, 'razor'. zhi ba, 'peaceful', here a goddess's name. chu srin, 'water monster', the makara, as in 011. bum pa, 'vase'. kyai is printed with two e-signs, as in 011.",
p=True)
u(39,
"Nectar red, scorpion's head, hand in lotus holding, and; Moon red, hawk's head, hand in vajra holding, and;",
"the red Nectar, with the head of a scorpion, holding a lotus; the red Moon, hawk-headed, holding a vajra;",
"bdud rtsi, 'nectar' (Sanskrit amṛta), the drink of immortality. sdig pa, 'scorpion'; sdig pa'i mgo, 'the head of a scorpion', with -'i, 'of'. padma, 'lotus'. zla ba, 'moon'. khra, 'hawk, falcon'. The print has zla ba dmar mo, 'the red Moon', where the other recension has dkar mo, 'white'.")
u(58,
"Club dark-green, fox's head, hand in staff holding, and; Ogress yellow-black, tiger's head, hand in skull-blood holding, and;",
"the dark green Club, fox-headed, holding a staff; the yellow-black Rākṣasī, tiger-headed, holding a skull full of blood;",
"be con, 'club', here a goddess's name. wa'i mgo, 'the head of a fox' (wa, 'fox'). Part 011 read this syllable, on its last page, as spra'i[?], 'monkey's'; that reading is withdrawn: enlarged eight times, the letter is wa, one letter high, as in the other recension. dbyug tho, here and below, is the print's spelling of dbyug to, 'staff', which the other recension has; it also has phyar ba, 'brandishing', for thogs pa, 'holding'. srin mo, 'ogress', Rākṣasī, as in 011; ser nag, 'yellow-black'. stag, 'tiger'. thod khrag, 'skull and blood', a skull full of blood.")
u(76,
"Gods'(?) yogins six own's brain's inside from emerged, then, oneself to dawning come. Them at not fear!",
"These six divine(?) yoginīs come out from inside your own brain and dawn before you. Do not fear them.",
"The sentence that closed the east in 011. lha'i, 'of the gods, divine', stands where the other quarters have their own name (shar gyi in 011, nub kyi and byang gi below); one would expect lho'i, 'of the south', but the other recension also has lha'i, and the print is followed. rnal 'byor, 'yogin', here without the feminine -ma that the other quarters have and the other recension has. The print adds rang gi, 'your own', before klad pa'i, as for the east.")
u(98,
"O child-of-noble-family! West from, Eater red-green, vulture head, hand in club holding, and; Delight red, horse's head, hand in great-trunk(?) holding, and;",
"O child of noble family, from the west: the red-green Eater, vulture-headed, holding a club; the red Delight, horse-headed, holding a great carcass(?);",
"za ba, 'eating, eater' (za, 'to eat'). dmar ljang, 'red-green', where the other recension has ljang nag, 'dark green'. bya rgod, 'vulture'. be con, 'club', here the thing she holds. dga' ba, 'Delight', the name of the first goddess of the south as well. rta, 'horse'. khog chen: khog pa is the trunk of the body, its hollow; khog chen, 'great trunk', is taken as a great carcass, a body without its limbs; the sense is not sure.",
p=True)
u(118,
"Great-Strength red, garuḍa's head, hand in staff holding, and; Ogress yellow, dog's head, hand in vajra razor cutting, and;",
"the red Great Strength, garuḍa-headed, holding a staff; the yellow Rākṣasī, dog-headed, cutting with a vajra razor in her hand;",
"stobs chen, 'great strength' (stobs, 'strength'); dmar mo, 'red', where the other recension has dkar mo, 'white'. khyung, the garuḍa, as in 010. srin mo, 'ogress', a second Rākṣasī after the one of the south; here ser mo, 'yellow', where the other recension has dmar mo, 'red'. khyi, 'dog'. rdo rje spu gri, 'a vajra razor'; gcod pa, 'cutting' (gcod, 'to cut'). The other recension has spu gris, 'with the razor', which makes the instrument plain; the print's spu gri without -s is read the same way.")
u(136,
"Desire red, hoopoe head, hands two arrow-bow drawing, and; Wealth-Guardian green, deer's head, hand in vase holding, and;",
"the red Desire, hoopoe-headed, drawing a bow and arrow with both hands; the green Guardian of Wealth, deer-headed, holding a vase;",
"'dod pa, 'desire'. pu shud, 'hoopoe'. lag gnyis, 'the two hands', where the other recension has lag na, 'in the hand'. The print runs gnyis and mda' together across the line join, here divided. mda' gzhu 'gengs pa, 'drawing the bow and arrow', as of Caurī in 011. nor srung, 'guardian of wealth' (nor, 'wealth'; srung, 'to guard'); ljang khu, 'green', where the other recension has dmar ljang, 'red-green'. sha ba, 'deer'. 'dzin pa, 'holding'.")
u(155,
"West's yoginīs six own's brain's inside from emerged, then, oneself to dawning come. Them at not fear!",
"These six yoginīs of the west come out from inside your own brain and dawn before you. Do not fear them.",
"As for the east in 011. The other recension has klad pa'i nang nas, without rang gi, and 'char ro.")
u(179,
"O child-of-noble-family! North from, Wind-Goddess blue, snake's head, hand in banner waving, and; Woman red, ibex's head, hand in stake(?) holding, and;",
"O child of noble family, from the north: the blue Wind Goddess, snake-headed, waving a banner; the red Woman, ibex-headed, holding a stake(?);",
"rlung lha, 'wind god' (rlung, 'wind'; lha, 'god'), here a goddess. sbrul gyi mgo, 'the head of a snake', where the other recension has spyang ki'i mgo, 'the head of a wolf'; so in the print the north has two snake-headed goddesses, this one and the Water Goddess below. ba dan, 'banner, pennant'; 'phyar ba, 'waving, brandishing'. mi mo, 'woman' (mi, 'person', with -mo). skyin, 'ibex'. gsal shing is taken as a stake or spit of wood (shing, 'wood'); the sense is not sure.",
p=True)
u(198,
"Sow black, pig's head, hand in fang-noose(?) holding, and; Vajra red, crow's head, hand in small-corpse holding, and;",
"the black Sow, Vārāhī, pig-headed, holding a noose of fangs(?); the red Vajra, crow-headed, holding a small corpse;",
"phag mo, 'sow' (phag, 'pig', with -mo), Sanskrit Vārāhī. mche zhags: mche ba is 'fang, tusk' and zhags pa 'noose'; 'a noose of fangs' is taken from the words, and the sense is not sure. The print runs na and mche together at the start of the line after the ornament (109.2), here divided. bsnams pa, 'holding', the respectful word (bsnams, the past stem of snom). rdo rje, 'vajra', here a goddess's name. khwa ta, 'crow'. zhing chung, 'a small corpse' (zhing, 'corpse', as in 011; chung, 'small').")
u(221,
"Great-Nose dark-green, ox's head, hand in club holding and, blood drinking, and; Water-Goddess blue, snake's head, hand in snake-noose holding, and;",
"the dark green Great Nose, ox-headed, holding a club and drinking blood; the blue Water Goddess, snake-headed, holding a noose of snakes;",
"sna chen, 'great nose' (sna, 'nose'), a name that suits an elephant's trunk; the other recension has glang chen mgo, 'elephant-headed', where the print has glang gi mgo, 'the head of an ox' (glang, 'ox, bull'; glang chen, 'great ox', is the elephant). be con thogs shing khrag 'thung ba, 'holding a club and drinking blood' (thogs shing, 'holding, and'; 'thung, 'to drink'); the other recension has bam chen thogs shing thod khrag 'thung ba, 'holding a great corpse and drinking blood from a skull'. chu lha, 'water god', here a goddess. sbrul zhags, 'a noose of snakes'.")
u(240,
"North's yoginīs six own's brain's inside from emerged, then, oneself to dawning come. Them at not fear!",
"These six yoginīs of the north come out from inside your own brain and dawn before you. Do not fear them.",
"As for the west.")
u(255,
"O child-of-noble-family! Gate-women ri(?) yoginīs four, brain's inside from emerged, then, oneself to dawning come.",
"O child of noble family, the four gatekeeper yoginīs come out from inside your brain and dawn before you.",
"sgo ma, 'gate-woman', the female gatekeeper, as in 011: the Īśvarīs too have four at the gates. After sgo ma the print has a syllable ri, doubtful on the image ([?]), which gives no sense and which the other recension lacks; it may be the ra of rnal 'byor, which follows, set twice. It is kept as printed, given in the literal line with a query and left out of the idiomatic line. The print has no ma yengs par nyon cig, 'listen without distraction', which the other recension has after kyai rigs kyi bu.",
p=True)
u(277,
"East from, Vajra Sow, cuckoo head, hand in iron-hook holding, and; south from, Vajra yellow, goat's head, hand in noose holding, and;",
"from the east, Vajra Sow, cuckoo-headed, holding an iron hook; from the south, the yellow Vajra, goat-headed, holding a noose;",
"Each of the four is called rdo rje, 'Vajra', with a colour. In the east the print has phag mo, 'sow', where the other recension has dkar mo, 'white'; phag mo may have been carried over from the Sow of the north (109.1). It is kept, and the goddess is named as printed, Vajra Sow, though she then has no colour and a cuckoo's head. khu byug, 'cuckoo'. lcags kyu, 'iron hook'; zhags pa, 'noose': the hook, noose, chain and bell are those of the four gatekeeper goddesses of the peaceful deities (006). ra, 'goat'; ra'i mgo, 'the head of a goat'.")
u(300,
"West from, Vajra red, lion's head, hand in iron-chain holding, and; north from, Vajra dark-green, snake's head, hand in bell holding, and;",
"from the west, the red Vajra, lion-headed, holding an iron chain; from the north, the dark green Vajra, snake-headed, holding a bell;",
"seng ge, 'lion'; lcags sgrog, 'iron chain'; sbrul, 'snake'; dril bu, 'bell'. The other recension has seng mgo ma and sbrul mgo ma, 'lion-headed one, snake-headed one'.")
u(319,
"Yogin gate-women four also own's brain's inside from emerged, then, oneself to dawning come. Them at not fear!",
"These four gatekeeper yoginīs, too, come out from inside your own brain and dawn before you. Do not fear them.",
"rnal 'byor sgo ma, 'yogin gatekeepers', again without the -ma of rnal 'byor ma, which the other recension has. The other recension has klad pa'i nang nas, without rang gi, and no ma 'jigs shig here.")
u(334,
"Īśvarīs twenty-and-eight, heruka fierce's deities, self-arisen's body's energy from self-dawned are-because, face-knowing do!",
"The twenty-eight Īśvarīs, deities of the fierce heruka, have dawned of themselves from the energy of the self-arisen body: recognise them.",
"The list is closed by naming the twenty-eight together. dbang phyug ma, 'Īśvarī', and nyi shu rtsa brgyad, 'twenty-eight', as in 011. he ru ka drag po'i lha, 'deities of the fierce heruka', the words 011 used of the thirty inside their ring. rang byung gi sku, 'the self-arisen body', the buddha's body that arises of itself; sku'i rtsal las, 'from the energy of the body'. rang shar, 'dawned of itself'. yin pas, 'because (they) are', runs on to the command. The other recension has kyang, 'too', after the number, rang rtsal, 'own energy', and rang shar ba yin pas.",
p=True)
u(347,
"O child-of-noble-family! Body-of-truth empty's aspect from, peaceful's deities-as dawned it-is. Face-knowing do!",
"O child of noble family, it is from the empty aspect of the body of truth that the peaceful deities have dawned. Recognise this.",
"chos sku, 'body of truth' (dharmakāya). stong pa, 'empty'; cha, 'part, aspect'; stong pa'i cha las, 'from the empty aspect'. zhi ba'i lha, 'peaceful deities'; -ru, 'as', after a vowel. shar ba yin no, 'it is (that they) have dawned' (shar, the past of 'char), closes with the sentence-ending -o.",
p=True)
u(358,
"Body-of-truth clear's aspect from, wrath's deities-as dawned it-is. Face-knowing do!",
"It is from the clear aspect of the body of truth that the wrathful deities have dawned. Recognise this.",
"The print has ཆ་ལ་ལས (cha la las), a misprint for ཆ་ལས (cha las), corrected here. The la is set twice, at the end of 110.4 and again at the start of 110.5; cha las stands in the sentence before. gsal ba, 'clear, luminous'; gsal ba'i cha, 'the clear aspect'. The print says chos sku, 'body of truth', a second time, where the sense wants longs sku, 'body of enjoyment' (sambhogakāya), set against the body of truth of the sentence before: from its empty aspect the peaceful deities, from the clear aspect of the body of enjoyment the wrathful ones. The other recension has longs sku. The text and both translations keep chos sku, as printed. khro ba'i lha, 'deities of wrath', where the other recension has khro bo'i, 'of the wrathful ones'.")
u(392,
"Own's brain's inside from, blood-drinkers fifty-and-eight's deity-host emerged, then, dawned dawning's time this-at: whatever dawned all, own's knowing's own-radiance; self-dawned-as knowing, then: that-not-interval, blood-drinker's body with two-as without-ly buddha-becoming-is.",
"At this time, when the host of the fifty-eight blood-drinking deities comes out from inside your own brain and dawns, know that whatever dawns is the natural radiance of your own awareness, dawned of itself; and at that very moment you become a buddha, inseparable from the body of the blood-drinker.",
"lnga bcu rtsa brgyad, 'fifty-eight' (lnga bcu, 'fifty'): all the blood-drinking deities together, the thirty of 011 with the twenty-eight Īśvarīs. shar 'char ba'i dus 'dir, 'at this time of dawning' (dus, 'time'; 'dir, 'at this'): shar, the past of 'char, stands before the present, 'dawned and dawning'; the other recension has rang la 'char ba'i, 'dawning to you'. rang mdangs, 'own radiance, natural glow'. The print closes rang mdangs with ༔ and goes on rang shar bar shes nas, 'knowing (it) as dawned of itself, then'; the other recension has rang mdangs las shar ba shes na, 'if (you) know (it) as dawned from the natural radiance'. de ma thag, 'right upon that' (ma thag, 'no interval'). gnyis su med par, 'without being two'. sangs rgyas pa'o, 'is to become a buddha', with the sentence-ending -o after pa; the other recension has sangs rgyas so.",
p=True)
u(411,
"O child-of-noble-family! Thus face not know if, you, those (plural) at fearing and, dreading-because, again suffering's adding(?)-to go.",
"O child of noble family, if you do not recognise them in this way, you will fear them and dread them, and so go on again to more(?) suffering.",
"de ltar ngo ma shes na, 'if (you) do not recognise (them) so': ma ... na. khyed, 'you', the polite or plural form, where the text mostly has khyod. zhed cing bred pas, 'fearing and dreading, because' (zhed, 'to fear'; bred, 'to be scared'): bred is doubtful on the image ([?]), though it fits the traces and the other recension has it. slar, 'again, back'. sdug bsngal gyi snon mar 'gro go is obscure, and its sense is uncertain. snon is 'to add', and snon ma could be 'an addition', which gives 'go to an addition of suffering', 'go on to more suffering'. The other recension has sdug bsngal gyis non par 'gro'o, 'go oppressed by suffering' (non, 'pressed down'), and the print's words may be a slip for that, as one reader suggests (gyis non par for gyi snon mar). The print writes 'gro go as one syllable, 'grog, with one o-sign over both letters; it is written out here. The sentence closes with the plain stroke ། instead of ༔.",
p=True)
u(432,
"Thus face not know if, blood-drinker's deities all Death-Lords-as seen, then: blood-drinker's deities all at fear. Dread. Be-frightened. Faint.",
"If you do not recognise them so, you will see all the blood-drinking deities as Lords of Death: you will fear all the blood-drinking deities, you will be terrified, you will be frightened, you will faint.",
"gshin rje ru, 'as Lords of Death', as gshin rjer in 010: gshin rje, 'Lord of the Dead', Yama, and the fierce figures of his court; -ru, 'as'. mthong nas, 'having seen'. Four short sentences follow, each a verb with the sentence-ending -o, which repeats the verb's last letter: 'jigs so, 'fear'; dngangs so, 'are terrified' (dngangs is the print's spelling of sngangs, which the other recension has); skrag go, 'are frightened'; brgyal lo, 'faint'. The other recension has lha tshogs thams cad, 'the whole host of deities', where the print has lha thams cad, and lha la, without thams cad.")
u(446,
"Self-appearance demons-into gone, then, saṃsāra-in wander. Not fear, not be-frightened if, saṃsāra-in not wander.",
"Your own appearance turns into demons, and you wander in saṃsāra. If you are neither afraid nor frightened, you will not wander in saṃsāra.",
"bdud, 'demon, Māra', the power that hinders; bdud du song, 'has gone into demons, has turned demon' (song, the past of 'gro, 'to go'; du, 'into'). 'khor bar 'khyams so, 'wanders in saṃsāra', with -r, 'in'. ma zhed ma skrag na, 'if (you) neither fear nor are frightened': ma ... na with two verbs; the other recension has ma zhen, 'if (you) do not cling'. mi 'khyams so: mi, not ma, negates a verb of the present or future.")
u(475,
"O child-of-noble-family! Peaceful and wrathful-ones' bodies those (plural) also: great, as-for, sky with equal; middling, as-for, Meru as-much-as; least even oneself eighteen stacked as-much-as come-because: that at not be-afraid!",
"O child of noble family, the bodies of the peaceful and wrathful deities, too: the largest are as vast as the sky, the middling as large as Mount Meru, and even the smallest come as tall as eighteen of you stacked one on another. Do not be afraid of that.",
"che ba ni ..., 'bring ni ..., tha ma yang ...: 'the large ..., the middling ..., even the least ...'. nam mkha' dang mnyam pa, 'equal to the sky'; the other recension has nam mkha'i mtha', 'the limits of the sky', and 'bring rnams. ri rab, Mount Meru, the mountain at the centre of the world; tsam pa, 'as much as'. rang bco brgyad brtsegs pa tsam, 'as much as eighteen of oneself stacked up' (bco brgyad, 'eighteen'; brtsegs pa, 'piled up'): the print has no lus, 'body', which the other recension has (rang lus), but the sense holds. 'byung bas, 'because (they) come'.",
p=True)
u(481,
"Appearance-existence all, light and body-as dawns.",
"All that appears and exists dawns as light and bodies.",
"snang srid, 'appearance and existence', all that appears and is, the whole world (snang, 'appear'; srid, 'existence'). 'od dang sku ru, 'as light and bodies'; 'char ro, 'dawns'.")
u(502,
"Appearances all light and body-as dawning, that: own's knowing's own-radiance-as face-knowing-because, light and body two-as without-ly dissolving, then, buddha-become.",
"When you recognise all these appearances that dawn as light and bodies as the natural radiance of your own awareness, you dissolve into the light and the bodies without duality and become a buddha.",
"snang ba thams cad ... 'char ba de, 'all the appearances that dawn ..., that': de closes the phrase that is the object of the recognising. ngo shes pas, 'because (you) recognise'. 'od dang sku gnyis su med par thim nas, 'dissolving inseparably into light and bodies'. The other recension has ngo shes nas, rang mdangs rang 'od dang sku ..., 'into (your) own radiance, (your) own light and bodies'; the print has no rang mdangs rang. sangs rgyas so, 'become a buddha', with the sentence-ending -o.")
u(515,
"Son, you, seen-appearances, terror-fright's appearances whatever arisen though: self-appearance-as face-knowing do [ … ]!",
"Son, whatever appearances of terror and fright arise for you in what you see, recognise them as your own appearance [ … ].",
"bu, 'son, child'. mthong snang, 'what is seen, visions' (mthong, 'see'; snang, 'appearance'). gang byung yang, 'whatever has arisen' (byung, the past of 'byung, 'to arise'; yang, 'even, though'). rang snang du, 'as your own appearance', as in 003. Between gyis and shig (112.3) the print has six or seven letters that no reader could read in the scan, even enlarged five times on a straightened copy: the traces look like la, ya, ra, a ja-shaped letter, ga or ba, a letter with the u-sign, and sa, perhaps la yar ja ... bsus or bzhus, possibly a correction cut into the block. They are left out of the text, which reads gyis shig, 'do!', a complete sentence; the other recension has nothing there. The literal and idiomatic lines mark the place with [ … ].",
p=True, gap="p. 112 l. 3: six or seven letters after gyis (unreadable in the scan)")
u(522,
"Clear-light own's own-radiance-as face-knowing do!",
"Recognise them as the clear light's own natural radiance.",
"'od gsal, 'clear light'. rang gi rang mdangs su, 'as its own natural radiance'. The other recension has 'od gsal rang rig rang mdangs su, 'as the clear light, the natural radiance of self-knowing awareness'.")
u(533,
"Thus face know if, now oneself at buddha-becoming at, doubt there-is-not.",
"If you recognise them in this way, there is no doubt that you will become a buddha now, in yourself.",
"da lta, 'now'. rang la, 'in oneself, by oneself'. sangs rgyas pa la the tshom med do, 'there is no doubt about becoming a buddha' (the tshom, 'doubt'; med, 'there is not', with the sentence-ending -o).")
u(546,
"Instant one by perfect-buddha called, that, this-time(?) arising is. Mind in remembering do!",
"What is called 'perfect buddhahood in a single instant' is what comes about this time(?). Keep this in mind.",
"skad cig gcig gis, 'by a single instant'. rdzogs sangs rgyas, 'perfect buddha, complete buddhahood' (rdzogs, 'complete'). bya ba, 'what is called': the other recension has zhes bya ba, with zhes, 'so', closing the name; the print has bya ba alone. sang res: sang is doubtful on the image ([?]); sang res is no known phrase, and the reading is uncertain. The other recension has da res, 'this time, now' (res, 'turn, time'), and the sense is probably that. 'byung ba yin no, 'is what comes about'. yid la dran par gyis shig, 'keep in mind' (yid, 'mind'; dran, 'remember').")
u(564,
"O child-of-noble-family! Oneself's(by?) now face not known, then, frightened, then: peaceful-ones' bodies all, Protector Black's body-as dawn.",
"O child of noble family, if you do not recognise them now and are frightened, all the bodies of the peaceful deities will dawn as the body of the Black Protector.",
"rang gi, 'oneself', stands for rang gis as the subject of the verbs, as kyi for kyis in earlier parts; the other recension has the same. ngo ma shes nas skrag nas, 'having not recognised and being frightened': the print has nas, 'then', where the sense wants a condition, and the other recension has skrag na, 'if frightened'; the idiomatic line reads it so. mgon po nag po, 'the Black Protector', Mahākāla, the great guardian of the teaching (mgon po, 'protector, lord'; nag po, 'black'). sku ru 'char ro, 'dawn as the body (of)'.",
p=True)
u(578,
"Wrathful-ones' bodies all, Lord-of-Death King-of-the-Teaching's body-as dawned, then: self-appearance demons-into gone, then, saṃsāra-in wander.",
"All the bodies of the wrathful deities dawn as the body of Yama, the Lord of Death, King of the Teaching; your own appearance turns into demons, and you wander in saṃsāra.",
"gshin rje chos kyi rgyal po, 'the Lord of Death, King of the Teaching' (chos kyi rgyal po, 'king of the teaching, of dharma'), Yama Dharmarāja, who judges the dead. shar nas, 'having dawned'. 'khyam mo, 'wander', from the form 'khyam, where the print had 'khyams so above; both spellings are in use, and the other recension has 'khyam mo throughout.")
u(598,
"O child-of-noble-family! Self-appearance face not know if: Word, sūtra-tantra all in learned being and, aeon-for dharma done though, awaken not will.",
"O child of noble family, if you do not recognise your own appearance, then even if you are learned in all the Word, the sūtras and the tantras, and practise the teaching for an aeon, you will not become a buddha.",
"bka', 'word, command', the Buddha's word; mdo rgyud, 'sūtras and tantras' (mdo, 'sūtra'; rgyud, 'tantra'). mkhas shing, 'being learned, and'. bskal ba, 'aeon' (Sanskrit kalpa), with -r, 'for'. chos byas kyang, 'even if (you) practise the teaching' (byas, the past of byed, 'to do'). sangs mi rgya'o, 'will not become a buddha': the negative mi stands between the two syllables of the verb sangs rgya, 'to awaken', which takes the sentence-ending -'o.",
p=True)
u(609,
"Self-appearance face know if, key-point one and word one by, buddha-become.",
"If you recognise your own appearance, you become a buddha through a single key point and a single word.",
"gnad, 'key point, vital point'; tshig, 'word'; gcig, 'one'. gis, 'by', after the second, governs both.")
u(622,
"Self-appearance-as face know if, died as-soon-as, reality-itself's between-in, Lord-of-Death King-of-the-Teaching's body dawns.",
"If you [do not] recognise them as your own appearance, then as soon as you have died, the body of Yama, the Lord of Death, King of the Teaching, will dawn in the bardo of reality.",
"As printed, the sentence says 'if you recognise (them) as your own appearance': there is no negative. The context (Yama appears to the one who fails to recognise, as in the sentences before) and the other recension (rang snang ngo ma shes na) need ma, 'not', and the sense is given so; but the image shows no ma, even enlarged seven times. The literal line keeps the print's words; the idiomatic line adds [not] in brackets. shi ma thag tu, 'as soon as (you) have died' (shi, the past of 'chi, 'to die'). chos nyid kyi bar dor, 'in the bardo of reality', where the other recension has chos nyid bar dor, without kyi.",
p=True)
u(641,
"Lord-of-Death King-of-the-Teaching's body: great, as-for, sky with equal; middling, as-for, Meru as-much-as by, world's realm filling, then, comes.",
"The body of the Lord of Death, King of the Teaching, is at its largest as vast as the sky, and at middling as large as Mount Meru, and he comes filling the world.",
"As for the peaceful and wrathful deities above. nam mkha', 'sky': mkha' is doubtful on the image ([?]), and the other recension has nam mkha'i mtha', 'the limits of the sky'. 'bring po, 'the middling', the print's form here for 'bring. tsam gyis, 'with (a size) as much as'. 'jig rten gyi khams, 'world-realm, the world' ('jig rten, 'world'; khams, 'realm'). gang nas, 'filling' (gang, 'full, to fill'). yong ngo, 'comes': yong is doubtful ([?]); its first letter may be 'a, which gives 'ong, the other recension's reading; the print has yong ngo clearly a line below, and yong is a spelling of 'ong, 'to come', so the sense is the same either way.")
u(660,
"That also: upper-teeth-by lower-lip pressed; crystal-eye eye-in having; hair crown-on bound; belly big; neck thin; hand in tally-stick holding;",
"He bites his lower lip with his upper teeth; his eyes are like glass(?); his hair is bound up on the crown of his head; his belly is huge, his neck thin; he holds a tally-stick in his hand;",
"de yang, 'that is', opens the description. ya so, 'upper teeth', with -s, 'by'; ma mchu, 'lower lip'; mnan pa, 'pressing down' (mnan, the past stem of gnon, 'to press'): he bites his lip in rage. mig shel mig tu yod pa, 'having crystal eyes for eyes' (shel, 'crystal, glass'), is taken as glassy, staring eyes; the sense is not sure. skra, 'hair'; spyi bo, 'crown of the head', with -r, 'on'; bcings pa, 'bound' (bcings, the past stem of 'ching, 'to bind'). gsus pa, 'belly'; ske, 'neck'; phra ba, 'thin'. khram shing, 'tally-stick', a notched stick on which deeds are scored: the record by which Yama judges. Each phrase ends in -pa or -ba with ༔, a list of what he is like.")
u(681,
"Mouth from 'strike, kill!''s sound crying; brain drinking; head body tearing-apart; vital-organs-heart pulling-out: such-like's world's realms all filled, then, comes.",
"crying out from his mouth 'Strike! Kill!', drinking brains, tearing heads from bodies, pulling out hearts. Like this he comes, filling every realm of the world.",
"rgyob sod, 'strike! kill!': rgyob is the imperative of rgyag, 'to strike' (past brgyab), and sod the imperative of gsod, 'to kill'; kyi sgra, 'the sound of'; sgrog pa, 'crying out'. klad pa, 'brain'; 'thung ba, 'drinking': 'thung is doubtful on the image ([?]), though the other recension has it. mgo lus phral ba, 'tearing head and body apart', as in 011. don snying, 'organs and heart' (don, a solid organ of the body; snying, 'heart'); 'don pa, 'taking out'. de lta bu'i, 'of that kind' (de lta bu, 'like that'). khengs nas, 'having filled' (khengs, 'to be full'). The print says he comes filling all the world-realms (khams thams cad khengs nas), where the other recension has khams gang nas, 'filling the world', as in the sentence before.")
u(695,
"O child-of-noble-family! Such-like's appearances dawned, then, arisen's time-at: you, fear and fright-to not do!",
"O child of noble family, when such appearances dawn and come before you, do not be afraid or frightened.",
"shar nas byung ba'i tshe, 'at the time when (they) have dawned and arisen'. 'jigs pa dang skrag par ma byed cig, 'do not make fear and fright' (byed, 'to do', with cig, which marks a command; ma, 'not'): par is doubtful on the image ([?]); the other recension has skrag pa.",
p=True)
u(708,
"You-yourself habitual-tendencies' mind's body are-because: killing and chopping happened though, dying-to-be there-is-not.",
"You are a body of mind made of habitual tendencies, so even if you are killed and cut to pieces, you cannot die.",
"yid kyi lus, 'body of mind, mental body', the body of the dead person in the bardo, made of bag chags, 'habitual tendencies', not of flesh. bsad pa, 'killing' (bsad, the past stem of gsod, 'to kill'). btubs pa, 'chopping, cutting to pieces': btubs is the past stem of gtub, 'to cut up', and the other recension has gtub pa. byung yang, 'even if (it) happens'. 'chi rgyu med do, 'there is nothing to die' (rgyu, after a verb, 'what is to be').")
u(717,
"Meaning-in, you emptiness own-form are-because, fear not need.",
"In truth you are the very form of emptiness, so you need not be afraid.",
"don la, 'in truth', as in 011. stong nyid, 'emptiness' (Sanskrit śūnyatā), short for stong pa nyid. rang gzugs, 'own form': gzugs is doubtful on the image ([?]). The other recension has stong pa'i rang gzugs, 'the empty one's own form'. zhed mi dgos so, 'need not fear' (dgos, 'to need'); the other recension has bred sngangs mi dgos, 'need not dread or be terrified'.")
u(730,
"Death-Lords (plural) also own's knowing's own-radiance from dawned are-because, substance-having-as established there-is-not.",
"The Lords of Death, too, have dawned from the natural radiance of your own awareness, so they do not exist as anything substantial.",
"The print has དངོས་པ་ཅན (dngos pa can), a misprint for དངོས་པོ་ཅན (dngos po can), corrected here: the o-sign is missing, and only dngos po can gives sense. The first letter is also doubtful on the image ([?]) and looks more like ga; the other recension has dngos po can. gshin rje rnams, 'the Lords of Death' (rnams, plural). dngos po, 'thing, something real'; can, 'having'; dngos po can du grub pa med do, 'are not established as having substance', do not really exist (grub pa, 'established').")
u(737,
"Emptiness by emptiness at chance not finds.",
"Emptiness can find no way to harm emptiness.",
"stong pa nyid, 'emptiness' (stong pa, 'empty'; nyid, '-ness'). glags, 'an opening, a chance to do harm'; glags mi rnyed, 'finds no way to harm' (rnyed, 'to find'). The other recension has the words in the other order, stong pa nyid la stong nyid kyis, the object before the agent; the sense is the same.")
u(763,
"You-yourself's knowing's own-energy from dawned except: outside-in, peaceful-ones and, wrathful-ones and, blood-drinkers and, head-likenesses and, rainbow-lights and, Lord-of-Death's forms terrifying and-so-on, really established without-ly, decided.",
"Apart from what dawns from the natural energy of your own awareness, it is settled that the peaceful ones, the wrathful ones, the blood-drinkers, the animal heads, the rainbow lights, the terrifying forms of the Lord of Death and all the rest do not really exist outside.",
"rang rtsal, 'own energy', as in 011. ma gtogs, 'except, apart from'; the other recension has ma gtogs pa. phyi rol du, 'outside, in the outer world', where the other recension has phyi rol na. mgo brnyan, 'head-likeness', the animal heads, as in 011. 'ja' 'od, 'rainbow light'. 'jigs 'jigs, 'terrifying', the word doubled. la sogs, 'and so on'. dngos su grub pa med par, 'without being really established'. thag chod do, 'it is decided, settled' (thag, 'cord'; chod, 'cut'), with the sentence-ending -o.")
u(777,
"Thus decided if, terror-fright all own-place-in freed, then, two-as without-ly dissolving, then, buddha becomes.",
"If you are certain of this, all terror and fright are freed in their own place, and you dissolve without duality and become a buddha.",
"thag chod na, 'if (it) is settled', where the other recension has shes na, 'if (you) know'. rang sar grol, 'freed in its own place', freed of itself, with nothing done to it (rang sa, 'own place', with -r). gnyis su med par thim nas sangs rgyas par 'gyur ro, as in 011.")
u(786,
"Thus face know if, as-for: yidam's deity is.",
"If you recognise them in this way, this is your yidam deity.",
"na ni, 'if, then': ni sets off the condition. The other recension has de ltar ma shes na'ang, 'even if (you) do not recognise (them) so, (it) is the yidam deity', which leads into the call on the yidam that follows; the print's reading also makes sense, and it is kept.",
p=True)
u(800,
"'Me, the between's narrow-pass in, meeting for coming is. For-refuge I-go': thinking's devotion longingly please-make!",
"With all your longing, have the devotion that thinks: 'He is coming to meet me in the narrow pass of the bardo; I go to him for refuge.'",
"bdag, 'I, me', the humble word: the dead person speaks. bar do'i 'phrang, 'the narrow pass of the bardo' ('phrang, 'defile, a dangerous narrow way'). bsu ba la, 'to meet, to welcome'. 'byon par 'dug go, 'is coming' ('byon, the respectful verb 'to come, to go'; 'dug after -par, 'is in the act of'), with the sentence-ending -o. skyabs su mchi'o, 'I go for refuge' (mchi, the humble 'go'). snyam pa'i, 'thinking', closes the words of the thought, as in the earlier parts. mos pa, 'devotion'; dung dung, 'intensely, with longing'; mdzod cig, 'please do!', the respectful command.")
u(812,
"Jewels-three after-ly remembering do! You-yourself's yidam whatever is, that, remembering do!",
"Call the Three Jewels to mind. Remember your own yidam, whoever he is.",
"dkon mchog gsum, 'the Three Jewels', the Buddha, the teaching and the community (dkon mchog, 'rare and supreme'). rjes su dran pa, 'to recollect, to call to mind' (rjes su, 'after, following'; dran pa, 'to remember'). gang yin pa de, 'whatever that is'. The other recension has yi dam gyi lha, 'yidam deity'; the print has yi dam alone.")
u(834,
"Name by, whatever emerges(?), call! 'I, the between-in wandered am-because, help to run! Compassion-by hold! Yidam precious!' so called, and, prayer obtain(?)!",
"Call him by name, whatever name comes to you(?): 'I am wandering in the bardo: run to help me! Hold me with your compassion, precious yidam!' Call out so, and pray.",
"mtshan, 'name', the respectful word; mtshan nas bos, 'call by name', as ming nas bos in the formula of the days before. gang thon is uncertain: thon is doubtful on the image ([?]), and gang thon is read 'whatever comes out', whatever name comes to mind (thon, 'to come out'); the other recension has only mtshan nas bos shig. bos cig: bos, the past stem of 'bod, 'to call', here in a command, with cig where shig is usual after -s. bar dor 'khyams nas yod pas, 'because (I) am wandering in the bardo' ('khyams nas yod, 'having wandered, am'). ra mda', 'help, rescue'; ra mda' la rgyug cig, 'run to help!' (rgyug, 'to run'), where the other recension has ra mda' mdzod cig, 'give help!'. thugs rjes bzung zhig, 'hold (me) with compassion!' (bzung, the past stem of 'dzin, 'to hold'; zhig marks a command after -ng); the other recension has zungs shig. rin po che, 'precious'. zhes, 'so', closes the words called. gsol ba thob cig is read, as in the parts before, as a guess for 'pray'. The part ends here; the next begins on the same line, with the call on the lama.")

sents = []
start = 0
for end, l, i, n, p, gap in U:
    w = ' '.join(toks[start:end + 1]).rstrip(' ')
    d = {'w': w, 'l': l, 'i': i, 'n': n}
    if p:
        d['p'] = 1
    if gap:
        d['gap'] = gap
    sents.append(d)
    start = end + 1
assert start == len(toks), (start, len(toks))
out = os.path.join(os.path.dirname(HERE), 'units.json')
json.dump({'about': ABOUT, 'sentences': sents}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(sents))
for k, s in enumerate(sents):
    print(k, s['w'][-30:], '|', s.get('gap', ''))
