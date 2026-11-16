# aeneid-086 (XI.445-531): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Turnus ad arma. Camilla'
PART = "Turnus to Arms; Camilla's Offer (XI.445–531)"
TITLE_EN = "Turnus to Arms; Camilla's Offer — Aeneid XI.445–531"
ABOUT = ("While Latinus's council is still quarrelling, a messenger bursts in: Aeneas has broken camp, and the Trojans and their Etruscan allies are marching down from the Tiber across the plain. "
"The city is thrown into uproar, the young men shouting for arms, the elders weeping and wavering, a din Virgil compares to birds settling in a grove or swans crying on the marshes of the Po. "
"Turnus seizes his moment with a sneer (let them sit and praise peace while the enemy overruns the kingdom) and hurries out, giving orders as he goes to Volusus, Messapus and Coras. "
"Latinus abandons his plan and blames himself for not having taken Aeneas as son-in-law; the Latins man the walls, dig trenches and haul up stones, and matrons and boys stand along the ramparts. "
"The queen goes up with the matrons and Lavinia to the temple of Pallas and they pray, as the Trojan women once prayed to Athena in the Iliad, for the Phrygian robber to fall before their gates. "
"Turnus arms and runs down from the citadel in his gold and bronze, like a stallion breaking loose for the pastures and the river. "
"At the gates Camilla, queen of the Volscians, leaps from her horse and offers to meet the Trojan and Etruscan cavalry alone. "
"Turnus gives her command of the horse, with Messapus, and tells her his own plan: Aeneas is crossing the hills by a mountain track, and Turnus will ambush him in a wooded defile. "
"Virgil describes the valley and the hidden plateau above it, and Turnus goes and takes up his position there.")

U = [
(446, 'movebat:',
 """They were these things among themselves on doubtful matters debating,\ncontending; his camp Aeneas and his battle-line was moving:""",
 """So they argued among themselves, contending over a question that hung in the balance; and all the while Aeneas was moving his camp and his line of battle:""",
 """A new paragraph in Greenough. 'Illi', Latinus and his council, still at the quarrel of the last part. 'haec… agebant', 'were debating these things'; 'dubiis de rebus', 'in a doubtful state of affairs', a crisis whose outcome is unclear. The two clauses stand side by side with no connective (asyndeton): the effect is 'while they talked, Aeneas marched'. 'castra movere', the regular Roman phrase for breaking camp to march. The imperfects set the scene for the sudden present of 448. Elisions 'Ill(i) haec', 'castr(a) Aeneas'."""),
(450, 'campis.',
 """a messenger, amid huge uproar, through the royal halls,\nlook, rushes, and with great terrors fills the city:\nthe Teucrians, drawn up in battle-line, from the Tiber river,\nand the Tyrrhenian band over all the plains are coming down.""",
 """and look, a messenger comes running through the palace amid a great uproar and fills the city with alarm: the Trojans, he reports, are coming down from the Tiber in battle order, and the Etruscan force with them, across the whole breadth of the plain.""",
 """'ecce', 'look!', and the vivid presents 'ruit… implet' break into the imperfects. 'ingenti… tumultu', framing the line, ablative of attendant circumstance. The accusative and infinitive 'Teucros… descendere' depends on the idea of reporting contained in 'nuntius'; no verb of saying is expressed. 'Tiberino a flumine', from the Trojan camp near the Tiber's mouth. 'Tyrrhenam manum', the Etruscan allies who joined Aeneas under Tarchon in Book X. 'totis… campis', 'over all the plains', local ablative. Elisions 'magnisqu(e) urbem', 'Tiberin(o) a'."""),
(452, 'irae.',
 """At once disturbed were their minds, and shaken the common people's\nhearts, and roused by goads not gentle their angers.""",
 """At once their spirits were thrown into confusion, the hearts of the common people were shaken, and their anger was roused by goads that were anything but gentle.""",
 """No verb: 'sunt' is understood with all three participles, an ellipsis natural in quick narrative. 'vulgi', the common people, as opposed to the council. 'adrectae', Greenough's spelling with the prefix left unassimilated (the familiar form is 'arrectae'), from 'arrigo', 'raise up', of anger 'pricked up' like a beast's ears. You will meet these 'ad-' spellings all through this part: 'adrepto', 'adceperit', 'adsciverit', 'adcinxerat', 'adcommoda'. 'stimulis haud mollibus', 'by goads not soft', litotes for sharp ones. Elisions 'turbat(i) animi', 'pector(a) et'."""),
(454, 'patres.',
 """For arms with the hand, alarmed, they call; roars 'arms!' the youth;\nweep, sorrowing, and mutter the fathers.""",
 """In their alarm they reach out and clamour for weapons, the young men roar for war, while the elders weep in sorrow and mutter their doubts.""",
 """'Arma… arma', anaphora, the word repeated at each half of the line. 'manu poscunt', 'demand with the hand', with gestures as well as voices. 'trepidi', 'in a flurry, alarmed'. 'fremit arma', 'roars arms', an internal accusative: the shout is the word itself (Turnus himself 'arma amens fremit' at VII.460, from memory). 'patres', the elders and councillors, who 'mussant', 'mutter', unable to decide: young against old. The three clauses run without connectives, quickening the pace. No elisions."""),
(458, 'cycni.',
 """Here on every side a clamour,\nwith varied discord, great, raises itself into the airs,\nnot otherwise than when in a deep grove by chance the flocks\nof birds have settled, or on the fish-filled river Padusa\ngive out sound the hoarse swans through the talkative pools.""",
 """Then on every side a great clamour of discordant voices rises into the air, just as when flocks of birds happen to settle in a deep grove, or hoarse swans send their cries over the chattering pools of the Padusa, rich in fish.""",
 """'Hic', 'at this point'. 'dissensu vario', 'with varied disagreement', ablative of manner. The simile is introduced by 'haud secus atque… cum', 'not otherwise than when'. 'consedere' = 'consederunt', the perfect in '-ere' (you will see this constantly). 'piscosove amne Padusae', '-ve', 'or'; the Padusa was a channel of the Po delta near Ravenna, famous for swans. 'stagna loquacia', 'chattering pools', the birds' noise given to the water. Homeric model: the Greek host pouring onto the plain like geese, cranes and long-necked swans by the Cayster (Iliad II.459–466, from memory). Elisions 'atqu(e) alto', 'alt(o) in', 'conseder(e) avium', 'piscosov(e) amne'."""),
(462, 'altis.',
 """“Oh yes,” says Turnus, seizing the moment, “citizens,\ncall a council and, sitting there, praise peace:\nthey with arms on the kingdom are rushing.” No more having spoken\nhe snatched himself up and swiftly carried himself out of the high halls.""",
 """“Oh yes, citizens,” said Turnus, seizing his moment, “call your council and sit there praising peace: they are rushing on the kingdom in arms.” Without another word he sprang up and hurried out of the lofty palace.""",
 """The print encloses the whole of 459, 'ait' and 'Turnus' included, in marks, opens a second time before 'cogite', and joins the closing mark to 'Nec' at 461: misprints for a speech that runs 'Immo… O cives… ruunt.' with 'ait… adrepto tempore, Turnus' outside it, corrected here. 'Immo', 'nay rather', bitterly ironic: by all means keep talking. 'adrepto tempore', ablative absolute, 'the moment seized'. 'cogite… laudate', mocking imperatives; 'sedentes', 'sitting', the posture of a council that talks while others act. 'illi', the enemy; 'in regna', poetic plural. 'corripuit sese', 'snatched himself up'. Elisions 'Imm(o) ait', 'concili(um) et', 'ill(i) armis', 'ses(e) et'."""),
(464, 'Rutulos.',
 """“You, Volusus, the Volscians' companies to arm give order,\nand lead out,” he says, “the Rutulians too.""",
 """“Volusus,” he said, “give orders for the Volscian companies to arm, and lead out the Rutulians as well.""",
 """The print sets a second opening mark before 'duc' at the start of 464, a misprint, since Turnus's speech is already running from 463; corrected here, with 'he says' set outside the marks. 'Voluse', vocative of Volusus, a Volscian captain. 'armari… edice maniplos', 'proclaim that the companies be armed', accusative and passive infinitive. The Latin Library's 'maniplis' (dative, 'give the companies orders to arm') changes the construction, hardly the sense. 'maniplos', syncopated 'manipulos', the only form that fits the verse. 'et Rutulos', 'the Rutulians too', 'et' meaning 'also'. Elision 'Volus(e) armari'."""),
(467, 'arma.”',
 """The cavalry, Messapus, in arms,\nand with your brother, Coras, over the broad plains spread out.\nPart, the approaches of the city let it secure and the towers occupy;\nthe rest, where I shall have ordered, with me let the band carry arms.”""",
 """Messapus, and you, Coras, with your brother, deploy the cavalry in arms across the broad plains. Let one part hold the approaches to the city and man the towers; let the rest of the force carry the attack with me wherever I give the word.”""",
 """'Messapus… Coras… diffundite', nominatives with a plural imperative, the nominative doing duty for the vocative, common in verse. 'Equitem', collective singular, 'the cavalry'. Coras and his brother Catillus, Argive founders of Tibur, appeared in the catalogue of Book VII (from memory, about 670–677). 'firmet… capessat', jussive subjunctives agreeing with 'Pars'; the Latin Library's plural 'firment… capessant' (agreement by sense) changes nothing in meaning. 'turris', '-is' accusative plural. 'qua iusso' = 'qua iussero', 'where I shall have ordered', an old future perfect in '-so', surviving in Virgil's day in archaic and legal language (compare 'faxo'). 'inferat arma', 'carry the attack'. No elisions."""),
(468, 'urbe.',
 """At once onto the walls through the whole city there is running everywhere.""",
 """At once there is a rush to the walls from every quarter of the city.""",
 """'Ilicet', 'at once'; it was originally 'ire licet', 'you may go', the formula that dismissed a Roman court or assembly, and that origin suits the moment, since the council is breaking up. 'discurritur', impersonal passive, 'there is running in all directions': the action without the actors, a favourite device for crowds. 'tota… urbe', local ablative without 'in'. No elisions."""),
(472, 'urbi.',
 """His plan, himself, the father, and his great undertakings Latinus\nabandons, and, by the gloomy time troubled, puts them off,\nand much he accuses himself, who did not receive of his own accord\nDardanian Aeneas and adopt him as son-in-law for the city.""",
 """Father Latinus himself abandons his plan and his great design and, shaken by this grim hour, puts it off, and he blames himself again and again for not having welcomed Dardanian Aeneas of his own free will and taken him into the city as his son-in-law.""",
 """'Consilium… et magna incepta', his peace proposal and the embassy with gifts (302–335). The Latin Library has 'concilium', 'he leaves the council', which changes the sense: there the meeting breaks up; here the plan is given up, and 'differt', 'puts off', suits a plan. 'pater', a title of respect for the king. 'multa se incusat', 'accuses himself much', 'multa' an internal accusative. 'qui non adceperit', causal relative with the subjunctive, 'since he had not received'; 'adceperit… adsciverit' are Greenough's spellings of 'acceperit… asciverit'. 'ultro', 'unasked'. 'Aenean', Greek accusative. 'urbi', 'for the city'. Elisions 'Consili(um) ipse', 'magn(a) incepta', 's(e) incusat', 'Dardani(um) Aenean', 'generumqu(e) adsciverit'."""),
(474, 'subvectant.',
 """Dig before the gates some, or rocks and stakes\ncarry up.""",
 """Some dig trenches before the gates, others bring up stones and stakes.""",
 """'Praefodiunt… portas', 'dig in front of the gates', a rare compound taking the accusative of the thing dug before. 'alii… aut', 'some… or (others)': 'aut' stands where we expect a second 'alii'. 'sudes', sharpened stakes for the defence. 'subvectant', frequentative of 'subveho', 'keep carrying up', the repeated loads. The narrative runs on in vivid presents. No elisions."""),
(475, 'bucina.',
 """For war gives the signal, hoarse, the bloody one,\nthe horn.""",
 """The hoarse horn sounds the bloody signal for battle.""",
 """'Bello', dative, 'for war'. 'cruentum' agrees with 'signum': the signal is 'bloody' because it begins the bloodshed, a transferred epithet. 'rauca… bucina', the adjective in mid-line and the noun held over to the first word of the next: you wait to hear what instrument it is. The 'bucina' was the curved horn of the Roman camp that sounded the watches; Virgil gives the Latins Roman equipment. No elisions."""),
(476, 'omnis.',
 """Then the walls with a varied ringed garland\nthe matrons and boys: calls the final toil all.""",
 """Then matrons and boys ringed the walls in a motley circle: this last, desperate labour calls on everyone.""",
 """'cinxere' = 'cinxerunt'. 'varia… corona', 'with a varied ring', 'corona' the regular military word for a ring of men round a wall, here a mixed one. 'matronae puerique', the subject held back to the next line. 'labor ultimus', 'the final toil', the crisis that leaves no one out. 'omnis', '-is' accusative plural, 'all'. No elisions."""),
(480, 'decoros.',
 """And also to the temple and to the highest citadel of Pallas\nis carried up, with a great throng of matrons, the queen,\ngifts bearing, and beside her as companion Lavinia the maiden,\nthe cause of so great an evil, her eyes cast down, her lovely ones.""",
 """The queen too, attended by a great throng of matrons, rides up to the temple of Pallas on the summit of the citadel, bearing gifts, and beside her goes the maiden Lavinia, the cause of all this disaster, her lovely eyes lowered.""",
 """'Nec non', 'and also', two negatives making a strong positive. 'subvehitur', 'is carried up', in a carriage, as Roman matrons rode to festivals. 'regina', Amata, Latinus's queen. 'magna matrum… caterva', ablative of attendant circumstance. Homeric model: Hecuba and the Trojan women carry a robe up to Athena's temple on the citadel and pray to her (Iliad VI.286–311, from memory). 'causa mali tanti', the same words the Sibyl used of a foreign bride (VI.93, from memory). 'oculos deiecta decoros', 'cast down as to her lovely eyes', a participle in middle sense with an accusative, on the Greek model. Elisions 'summasqu(e) ad', 'tant(i) oculos'."""),
(482, 'voces:',
 """Go up the matrons and the temple with incense fill with smoke,\nand mournful from the high threshold pour out voices:""",
 """The matrons enter, fill the temple with the smoke of incense, and from the lofty threshold pour out their mournful prayers:""",
 """'Succedunt', 'go up to, enter'. 'ture vaporant', 'fill with incense-smoke', 'tus, turis', frankincense. 'alto… de limine', 'from the high threshold': the temple stands at the top of the citadel, and prayers were often spoken at the door before the image. 'maestas… voces', the adjective and noun framing the line. The vivid presents continue. No elisions."""),
(485, 'altis.”',
 """“Mighty in arms, guardian of war, Tritonian maiden,\nbreak with your hand the spear of the Phrygian robber, and himself\nheadlong lay low on the ground and stretch him out beneath the high gates.”""",
 """“Mighty in arms, mistress of war, Tritonian maiden, break with your own hand the spear of the Phrygian robber, throw him headlong to the earth and lay him out dead beneath our lofty gates.”""",
 """A prayer in hymn style: titles first ('Armipotens', 'praeses belli', 'Tritonia virgo'), then the requests. 'Tritonia', Minerva (Athena), named from Lake Triton in Libya, her birthplace in one story. 'Phrygii praedonis', 'the Phrygian bandit': Aeneas cast as a second Paris, come to carry off a bride. 'effunde', 'pour out', of a body sprawled in death. The model is Theano's prayer in Iliad VI.305–310 (from memory): break the spear of Diomedes and let him fall before the Scaean gates; Athena refused, and the reader suspects Minerva will too. Elision 'portisqu(e) effunde'."""),
(486, 'Turnus.',
 """Girds himself, raging, eagerly for battles, Turnus.""",
 """Turnus himself, in a fury, arms for battle in eager haste.""",
 """Narrative resumes after the matrons' prayer. 'Cingitur', passive in middle sense, 'girds himself', 'arms'. 'ipse', in contrast with the women at their prayers. 'furens', the word that follows Turnus through these books. 'certatim', usually 'in rivalry', of several people vying; of one man it means 'with all eagerness', as if racing the rest. 'in proelia', poetic plural. The subject is held to the last word of the line. Elision 'certati(m) in'."""),
(491, 'hostem:',
 """And now indeed, the ruddy breastplate having put on, with bronze\nhe bristled scales, and his calves he had enclosed in gold,\nhis temples bare as yet, and to his side he had girded his sword,\nand he gleamed, from the high running down, golden, citadel,\nand exults in spirit, and in hope already seizes in advance the enemy:""",
 """And now he had put on his ruddy breastplate and bristled with scales of bronze, he had sheathed his legs in gold, his head still bare, and had belted his sword to his side, and he flashed all golden as he ran down from the high citadel, exulting in his heart and in his hopes already closing with the enemy:""",
 """'Iamque adeo', 'and now indeed'. 'thoraca', Greek accusative of 'thorax', object of 'indutus', 'having put on', a passive participle in middle sense. 'aenis… squamis', 'with bronze scales', scale-armour; 'horrebat', 'bristled'. 'suras… auro', golden greaves. 'tempora nudus', 'bare as to the temples', Greek accusative of respect: no helmet yet. 'adcinxerat', Greenough's 'accinxerat'. 'aureus', 'golden', said of the man himself. The tenses move from pluperfect to imperfect to the vivid present 'exsultat… praecipit'; 'praecipit hostem', 'grasps the enemy in advance', in imagination. Elisions 'Iamqu(e) adeo', 'thorac(a) indutus', 'surasqu(e) incluserat', 'lateriqu(e) adcinxerat', 'fulgebatqu(e) alta', 'exsultatqu(e) animis'."""),
(493, 'aperto',
 """just as when, his tethers broken, flees the stalls\nat last free a horse, and of the plain having gained possession, the open one,""",
 """just as a horse, when he has snapped his halter and bolted from the stable, free at last and master of the open plain,""",
 """Greenough prints the simile as one six-line period with no stop inside it, so it is divided here, without a mark, where the horse reaches the plain and the two alternatives ('aut… aut') begin. 'qualis', 'such as', answering Turnus. 'praesaepia', Greenough's spelling of 'praesepia', 'stalls'. 'vinclis' = 'vinculis', syncopated like 'maniplos'. 'potitus', 'having got possession of', 'potior' with the ablative ('campo… aperto'). Homeric model: Paris running down from Troy's citadel in shining armour, compared to a stall-fed horse breaking loose for the river and the mares (Iliad VI.506–511, repeated of Hector at XV.263–268; from memory). Elision 'ub(i) abruptis'."""),
(497, 'armos.',
 """either he to the pastures and the herds makes of mares,\nor, used to water, to be bathed in the familiar river,\nleaps out, and with neck raised snorts on high,\nrunning riot, and play his manes over neck, over shoulders.""",
 """makes either for the pastures and the herds of mares, or, used to bathing in the waters of a river he knows, darts out and neighs with his neck held high, revelling, while his mane tosses over his neck and shoulders.""",
 """'ille', a redundant pronoun picking up the subject, a Homeric touch. 'armenta… equarum', 'herds of mares'. 'adsuetus aquae perfundi', 'used to being bathed in water', 'aquae' probably dative with 'adsuetus', the passive infinitive in middle sense. 'emicat', 'flashes out'. 'adrectis… cervicibus', Greenough's 'arrectis', 'with neck raised'. 'luxurians', 'running riot'. 'per colla, per armos', the repeated preposition swinging like the mane. The horse is Turnus's pride and freedom; that Homer gave this simile to Paris is a sign not in his favour. Elision 'ill(e) in'."""),
(501, 'fatur:',
 """Meeting him, with the Volscians' column accompanying, Camilla\nruns up, and at the gates from her horse the queen, right under them,\nleapt down, whom the whole troop, imitating, having left\nto the ground slid down their horses; then such things she speaks:""",
 """To meet him came Camilla with her Volscian column at her side, and right under the gates the queen leapt down from her horse; her whole troop followed her lead, left their horses and slid to the ground; then she spoke these words:""",
 """'Obvia cui', connecting relative, 'meeting him', 'obvia' predicative with 'occurrit'. Camilla, the Volscian warrior maiden, closed the catalogue of Italian forces at the end of Book VII; she is 'regina', queen of her people. 'portis… sub ipsis', 'right under the gates'. 'quam… imitata', 'imitating whom', the connecting relative again. 'relictis… equis', ablative absolute. 'defluxit', 'flowed down', a smooth dismount; to dismount was a mark of respect to a commander. 'talia fatur', the stock formula before a speech. Elisions 'Volscor(um) acie', 'portisqu(e) ab'."""),
(504, 'contra.',
 """“Turnus, if to the brave rightly there is any confidence in self,\nI dare, and the sons of Aeneas I promise to meet, their squadron,\nand alone the Tyrrhenian horsemen to go facing, against them.""",
 """“Turnus, if the brave may rightly have some confidence in themselves, I dare it, and I promise to meet the squadron of Aeneas's men, and to ride out alone against the Etruscan horsemen.""",
 """'sui… fiducia', 'confidence in oneself', objective genitive; 'forti', dative of possession, 'to a brave person', a general statement that Camilla applies to herself. 'merito', 'deservedly'. 'siqua', printed as one word ('si qua'). 'Aeneadum', old genitive plural in '-um', 'of the sons of Aeneas', the Trojans. 'turmae', a cavalry squadron, dative with 'occurrere'. 'sola… obvia', feminine: Camilla speaks as a woman and as a captain. 'ire obvia contra', 'go to meet them, against them', a full, emphatic phrase. Elisions 'siqu(a) est', 'aude(o) et', 'promitt(o) occurrere', 'ir(e) obvia'."""),
(506, 'serva.”',
 """Me allow first with my hand to try the dangers of war;\nyou on foot by the walls stand fast and the defences guard.”""",
 """Let me be the first to put my hand to the hazards of war, while you stay on foot by the walls and keep the defences safe.”""",
 """'Me sine… temptare', 'allow me to try': 'sine' is the imperative of 'sino', 'allow', not the preposition. 'prima', feminine again, 'the first'. 'pedes', 'on foot', nominative singular of 'pedes, peditis', 'foot-soldier', not the plural of 'pes': her cavalry will meet theirs while Turnus fights as infantry at the walls. 'subsiste', 'stand fast, stay behind'. Elision 'subsist(e) et'."""),
(507, 'fixus:',
 """Turnus to this, his eyes on the awe-inspiring maiden fixed:""",
 """Turnus answered, his eyes fastened on the formidable maiden:""",
 """Ellipsis of the verb of speaking: 'Turnus ad haec', supply 'respondit', as often. 'oculos… fixus', 'fixed as to his eyes', the accusative with a passive participle in middle sense, like 'oculos deiecta' at 480. 'horrenda', gerundive used as an adjective, 'to be shuddered at', 'awe-inspiring': Camilla is fearsome, not merely beautiful. Elision 'horrend(a) in'."""),
(509, 'parem?',
 """“O glory of Italy, maiden, what thanks to speak\nor what to return can I provide?""",
 """“Maiden, glory of Italy, what thanks can I find to speak, or what to repay?""",
 """'decus Italiae', 'the glory of Italy', in apposition to 'virgo'. 'grates dicere… referre', 'to say thanks… to return them': the Roman distinction between thanking in words and repaying in kind ('gratias agere', 'gratiam referre'); 'grates' is the solemn word, used of thanks to gods. 'parem', deliberative subjunctive, 'what am I to provide?'. 'quasve', '-ve', 'or'. No elisions."""),
(510, 'laborem.',
 """But now, since above all things is\nthat spirit of yours, with me share the toil.""",
 """But now, since that spirit of yours rises above everything, share the labour with me.""",
 """'est omnia quando iste animus supra': in prose order 'quando iste animus est supra omnia', 'since that courage of yours is above all things'; both 'quando' and 'supra' come after their words (anastrophe). 'iste', 'that of yours', the demonstrative of the second person. 'partire', imperative of the deponent 'partior', 'divide, share'. Turnus accepts her offer, but on his own terms. Elision 'ist(e) animus'."""),
(514, 'urbem.',
 """Aeneas, as rumour and the sent bring back assurance,\nthe scouts, of horsemen the light, the shameless one, arms\nhas sent ahead, to shake the plains; himself, the steep of the mountain\nthrough the lonely places, by the ridge crossing over, approaches toward the city.""",
 """Aeneas, as rumour and the scouts we sent out confirm, has cunningly sent his light cavalry ahead to scour the plains, while he himself, crossing the high ground by a lonely ridge, is coming on towards the city.""",
 """'ut fama fidem missique reportant exploratores', 'as rumour and the scouts sent out bring back confirmation', 'fidem reportant' with two subjects. 'improbus', 'shameless, unscrupulous', Turnus's word for an enemy's cunning. 'equitum levia… arma', 'the light arms of horsemen', for the light cavalry itself. 'quaterent campos', purpose without 'ut', 'to shake (scour) the plains'. 'ardua montis per deserta', 'through the steep, deserted places of the mountain', neuter plural adjectives used as nouns. 'iugo superans', 'passing over by the ridge'. Elisions 'levi(a) improbus', 'ips(e) ardua'."""),
(516, 'fauces.',
 """A stealth of war I prepare in the hollow track of the wood,\nso that the two-way, with armed soldiery, I may beset, pass.""",
 """I am preparing a stratagem of war on the winding track through the forest, to hold both ends of the pass with armed men.""",
 """'Furta… belli', 'thefts of war', a stratagem, an ambush; 'furtum' is anything done by stealth. 'convexo in tramite', 'on the hollow, curving path'. 'ut… obsidam', purpose clause. 'bivias… fauces', 'two-way jaws', a defile with an entrance at either end; 'fauces', 'throat', is the regular word for a narrow pass. 'armato… milite', collective singular, 'with armed soldiery'. Elisions 'convex(o) in', 'armat(o) obsidam'."""),
(519, 'curam.”',
 """You the Tyrrhenian horseman, with standards brought together, receive;\nwith you keen Messapus will be, and the Latin squadrons,\nand Tiburtus' band; of a leader you too take on the charge.”""",
 """You must take on the Etruscan cavalry in close battle; with you will be fierce Messapus, the Latin squadrons and the troop from Tibur: you too must shoulder a general's command.”""",
 """'conlatis… signis', 'with standards brought together', in pitched battle; 'conlatis' is Greenough's unassimilated 'collatis'. 'excipe', 'receive, take the shock of'. 'Tyrrhenum equitem', collective singular again. 'Tiburti… manus', 'the band of Tiburtus', founder of Tibur and brother of Coras and Catillus: the men of Tibur. 'ducis… curam', 'the charge of a commander'; 'et tu', 'you too', since Turnus commands elsewhere. Turnus gives Camilla the cavalry command while he takes the ambush for himself. Elisions 'Tyrrhen(um) equitem', 'tec(um) acer'."""),
(521, 'hostem.',
 """Thus he speaks, and with like words Messapus to battle\nurges, and the allied leaders, and proceeds against the enemy.""",
 """So he spoke, and with like words urged Messapus and the allied captains to battle, and set out against the enemy.""",
 """'Sic ait', the closing formula. 'paribus… dictis', 'with like words', framing 'Messapum in proelia'. 'socios… duces', the allied captains, Coras and Catillus among them. 'hortatur', deponent, 'urges on'. 'pergit in hostem', 'goes on against the enemy', though he is going to lie in wait rather than attack. Elision 'Messap(um) in'."""),
(525, 'maligni.',
 """There is, with a curving bend, a valley, suited to stratagem\nand to the tricks of arms, which, with dense leaves dark,\npresses on both sides a flank, where a thin path leads\nand narrow jaws bring you, and approaches grudging.""",
 """There is a valley with a curving bend, made for stratagems and the wiles of war, hemmed in on either side by a slope dark with thick foliage; a faint path leads into it, through a narrow gorge and a forbidding entrance.""",
 """'Est… valles', 'there is a valley', the formula that opens a description of a place (compare 'Est in secessu longo locus', I.159). 'valles', an old nominative of 'vallis'. 'adcommoda', Greenough's spelling of 'accommoda', 'suited', with the datives 'fraudi… dolis'. 'quam… urget… latus', 'which a dark flank presses', 'utrimque', 'on both sides'. 'quo', 'to which', relative adverb. 'ferunt', 'lead', with no object expressed. 'maligni', 'grudging, niggardly', of an entrance that gives little room. Elision 'curv(o) anfractu'."""),
(529, 'saxa.',
 """Above it, among look-outs and on the highest top of the mountain,\na plain unknown lies, and safe retreats,\nwhether on right and left you wish to meet the fight\nor to press on from the ridges and huge to roll rocks.""",
 """Above it, among the look-out points on the mountain's very summit, lies a hidden tableland, a safe place of retreat, whether you choose to meet the battle from right or left, or to bear down from the ridges and roll huge boulders on the enemy.""",
 """'Hanc super', anastrophe, 'above this (valley)'. 'in speculis', 'on the look-outs', high points for watching. 'planities ignota', 'level ground unknown', to the enemy. 'tuti… receptus', 'safe retreats', poetic plural, nominative. 'seu… velis… sive', 'whether you wish… or', the generalising 'you', 'one'. 'occurrere pugnae', 'to meet the fight', dative. 'instare iugis', 'to press on from the ridges' or 'to take one's stand on the ridges'; either way the attack comes from above. Elision 'siv(e) instare'."""),
(531, 'iniquis.',
 """Hither the young man by a known tract of roads is carried\nand seized the place and in the woods sat down, the treacherous ones.""",
 """Here the young warrior hurried by a route he knew well, seized the position and settled in ambush among the treacherous woods.""",
 """'Huc', 'to this place'. 'iuvenis', Turnus, still a young man. 'nota… regione viarum', 'by a known tract of roads', ablative of the way by which. 'fertur', 'is carried, hurries', passive in middle sense. 'arripuit… insedit', perfects after the present: done at once. 'silvis… iniquis', 'woods unfair', unfavourable to an enemy, a place of ambush. 'insedit', 'sat down in, occupied'. The next part turns from Turnus to Diana and the story of Camilla. Elision 'loc(um) et'."""),
]

# Speech-mark check exemptions (rule 5b), by unit ln:
#  459: the print encloses all of 459 ('ait' and 'Turnus' included) in marks, reopens before 'cogite' (460) and
#       joins the closing mark to 'Nec' (461 ”Nec); l and i open the speech at 'Immo', set 'he says, Turnus,
#       seizing the moment' outside the marks, and close it after 'ruunt.'.
#  463: the print sets a second opening mark before 'duc' (464) inside a speech already running; l and i set
#       'he says' outside the marks instead.
EXEMPT = {459, 463}
# Ending-check exemption, by unit ln:
#  492: the horse simile 492-497 is one six-line period with no stop inside it (only 'luxurians,' in 497);
#       it is split after 'aperto' (493), where the two 'aut' alternatives begin, so that no unit runs past five lines.
NOSTOP = {492}
P = A.part('aeneid-086'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
cuts = A.cut(P, [(u[0], u[1]) for u in U])
sents = []; prev_end_line = None
for (t, ln), (_, _t, l, i, n) in zip(cuts, U):
    u = {'t': t, 'l': l, 'i': i, 'n': n}
    if prev_end_line != ln and ln in paras: u['p'] = True
    u['v'] = True; u['ln'] = ln; sents.append(u)
    prev_end_line = ln + t.count('\n')
    if t.count('\n') != l.count('\n'): print('LINE COUNT', ln, repr(t[:30]), t.count('\n'), l.count('\n'))
    if t.count('\n') > 4: print('TOO LONG', ln)
    if '\n' in i: print('NEWLINE IN i', ln)
    if t.rstrip('”]')[-1] not in A.TERMINAL + ',' and ln not in NOSTOP: print('ENDING', ln, repr(t[-12:]))
    nw = len(n.split())
    if nw > 139 or nw < 15: print('NOTE LENGTH', ln, nw)
    for mk in '“”[]':
        if t.count(mk) != l.count(mk) and ln not in EXEMPT: print('MARK l', ln, mk)
        if mk in '“”' and t.count(mk) != i.count(mk) and ln not in EXEMPT: print('MARK i', ln, mk)
    if '“' in n or '”' in n: print('DOUBLE MARK IN n', ln)
covered = sorted({ln + k for (t, ln) in cuts for k in range(t.count('\n') + 1)})
if covered != [l['n'] for l in L]: print('COVERAGE', covered)
joined = '\n'.join(l['t'] for l in L)
rebuilt = ''.join(t + ('\n' if (k + 1 < len(cuts) and cuts[k + 1][1] != ln + t.count('\n')) else ' ' if k + 1 < len(cuts) else '') for k, (t, ln) in enumerate(cuts))
if rebuilt != joined: print('JOIN MISMATCH')
if A.sha(L) != P.get('sha256', A.sha(L)): print('SHA MISMATCH')
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units;', len(covered), 'lines covered')
