# aeneid-088 (XI.648-724): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Camilla bellatrix. Dolus Liguris'
PART = "Camilla in the Thick of Battle (XI.648–724)"
TITLE_EN = "Camilla in the Thick of Battle — Aeneid XI.648–724"
ABOUT = ("The cavalry battle before the walls of Latinus's city has swung back and forth, and now Virgil turns to Camilla, queen of the Volscians, the warrior maiden vowed to Diana. "
"She rides through the slaughter like an Amazon, one breast bared, now showering javelins, now swinging a double axe, the golden bow of Diana on her shoulder, shooting backwards even as she gives ground. "
"Around her ride the companions she chose for herself, Larina, Tulla and Tarpeia, and Virgil compares the band to the Amazons of Thermodon around their queens Hippolyta and Penthesilea. "
"Then, in Homer's manner, he asks his heroine whom she killed first and whom last, and gives the list: Eunaeus, Liris and Pagasus, Amastrus and four more, and Ornytus, an Etruscan hunter who has come to war in a bullock's hide and a wolf's-head cap, and whom she mocks as he dies. "
"She kills the giant Butes from behind and outrides Orsilochus in a circle until she is behind him with her axe. "
"Last comes the son of Aunus, a Ligurian of a people famous for lying, who cannot escape and tries a trick: let her get off her horse and fight him fairly on foot. "
"She does, and he gallops away; she outruns his horse on foot, seizes the reins and kills him, as a hawk takes a dove out of the sky. "
"The passage is Camilla's aristeia, the run of triumph that Homer gives a hero before his death, and the reader, who has heard Diana foretell it, knows hers is near.")

U = [
(649, 'Camilla,',
 """But in the midst of the slaughter exults an Amazon,\none side laid bare for battle, quiver-bearing Camilla,""",
 """But in the thick of the slaughter an Amazon exults, one side of her breast bared for the fight: Camilla with her quiver,""",
 """A new paragraph in Greenough. 'medias inter caedes', the preposition set between adjective and noun, a common poetic order. 'exsultat', 'leaps, revels'. 'Amazon', in apposition: Camilla is not an Amazon but is called one, and the simile at 659 makes good the name. 'unum exserta latus', 'bared as to one side', a passive participle in middle sense with a Greek accusative of respect (like 'tempora nudus' at 489); the Amazons were pictured fighting with one breast uncovered. 'pugnae', dative of purpose, 'for battle'. 'pharetrata', 'wearing a quiver'. Diana has just told Opis of Camilla's childhood and fate (532–596). Elision 'unu(m) exserta'."""),
(652, 'Dianae.',
 """and now, pliant, from her hand scattering javelins, she thickens them,\nnow the stout in her right hand she snatches, unwearied, double axe;\ngolden from her shoulder rings the bow, the arms of Diana.""",
 """now she showers her pliant javelins thick and fast, now, never tiring, she snatches up the stout double axe in her right hand; the golden bow, the weapon of Diana, rings on her shoulder.""",
 """'nunc… nunc', 'now… now': missiles at a distance, then the axe at close quarters. 'lenta… hastilia', 'pliant shafts', framing the phrase; 'spargens… denset', 'scattering, she makes them thick', a shower. 'denset' is from 'denseo', an old second-conjugation form beside 'denso'. 'bipennem', 'two-edged axe', the Amazon's weapon in Greek art. 'indefessa', 'unwearied'. 'arcus et arma Dianae', 'the bow and the arms of Diana', the second phrase explaining the first, with the singular 'sonat'. Camilla is Diana's votary. The bow sounding on the shoulder recalls Apollo's arrows rattling as he came down from Olympus in anger (Iliad I.46, from memory). No elisions."""),
(654, 'arcu.',
 """She even backwards, if ever, driven back, she has withdrawn,\narrows, her bow turned round, fleeing, aims.""",
 """Even when she is driven back and gives ground, she turns her bow and aims her arrows behind her as she flees.""",
 """'in tergum', 'towards the back'. 'siquando', 'if ever', printed as one word (more usually 'si quando'; compare 'siqua' and 'nequid' earlier in the book). The perfect 'recessit' in a general condition with the present 'dirigit': whenever she has given ground, she shoots. 'fugientia', 'fleeing', is transferred from the archer to her arrows. 'converso… arcu', ablative absolute, 'her bow turned round'. The backward shot from horseback was the famous trick of the Parthians, Rome's eastern enemies in Virgil's own day (compare Georgics III.31, from memory). 'dirigit', Greenough's spelling; the Latin Library prints 'derigit', an older spelling of the same verb. Elisions 'Ill(a) etiam', 'etia(m) in'."""),
(658, 'ministras:',
 """But around her, chosen companions, Larina, the maiden,\nand Tulla, and, the bronze-bound brandishing, Tarpeia, axe,\nItalian women, whom herself as a glory for herself the godlike Camilla\nchose, of peace good and of war attendants:""",
 """Around her ride her chosen companions, the maiden Larina, Tulla, and Tarpeia brandishing her bronze-bound axe, daughters of Italy whom godlike Camilla herself picked out to be her glory, good helpers in peace and in war:""",
 """'circum', adverb, 'around (her)', with 'sunt' understood. The names are Italian, even Roman: 'Tulla' recalls King Tullus, 'Tarpeia' the Tarpeian Rock and the girl who, in the Roman story, let the Sabines into the Capitol; 'Larina' may come from the town of Larinum. 'aeratam… securem', 'bronze-fitted axe', framing the line; 'securem' is Greenough's accusative (usually 'securim', as he himself prints at 696). 'Italides', a Greek-style feminine, 'women of Italy'. 'decus sibi', 'as a glory for herself', predicative. 'dia', 'divine', an old epithet from Ennius. 'pacisque… bellique', the double '-que… -que'. Elision 'Tullaqu(e) et'."""),
(663, 'peltis.',
 """such as the Thracian, when the streams of Thermodon\nthey beat and war in painted arms, Amazons,\nwhether around Hippolyta, or when herself, the daughter of Mars, in her chariot\nPenthesilea brings back, and with a great howling uproar\nthe womanly exult, with crescent shields, columns.""",
 """like the Amazons of Thrace when they pound along the streams of Thermodon and make war in their painted armour, around Hippolyta, or when Penthesilea, child of Mars, rides home in her chariot and her hosts of women exult with their crescent shields amid a great tumult of shrieking.""",
 """'quales', 'such as', the simile picking up 'Amazon' (648). The Amazons, a nation of warrior women, lived by the river Thermodon on the south shore of the Black Sea; 'Threiciae', 'Thracian', is loose, for the wild north (four syllables, Thre-i-ci-ae). 'Thermodontis', Greek genitive. 'pulsant', they beat the river, with their horses' hooves. 'bellantur', a rare deponent form of 'bello'. Hippolyta was the queen whose girdle Hercules took; Penthesilea, 'Martia', a daughter of Mars, led the Amazons to Troy and fell to Achilles, and Dido's temple shows her (I.490–493). 'se… refert', returns from battle. 'magno… ululante tumultu', ablative absolute. 'lunatis… peltis', crescent shields. 'exsultant' echoes 648. Elisions 'circu(m) Hippolyten', 'magnoqu(e) ululante', 'femine(a) exsultant'."""),
(665, 'fundis?',
 """Whom with your weapon first, whom last, fierce maiden,\ndo you throw down? Or how many on the ground dying bodies do you pour out?""",
 """Whom first, fierce maiden, whom last do you strike down with your weapon? How many dying bodies do you stretch upon the ground?""",
 """The poet turns and speaks to his heroine, an apostrophe that is a Homeric way of opening a list of kills: 'Then whom first, whom last did you slay, Patroclus?' (Iliad XVI.692–693, from memory). 'aspera virgo', vocative, 'harsh, fierce maiden'. 'deicis… fundis', vivid presents, 'do you bring down… lay low'. 'humi', locative, 'on the ground'. 'morientia corpora', 'dying bodies', the object of 'fundis', literally 'pour out', of bodies sprawled at length. 'Aut', 'or', adds a second and wider question: not only which, but how many. Elision 'postremu(m) aspera'."""),
(667, 'pectus:',
 """Eunaeus, with Clitius as father, first, whose open,\nas he faced her, with long fir-wood she strikes through, breast:""",
 """First Eunaeus, son of Clitius: as he faced her, she drove her long fir-wood shaft clean through his unguarded breast;""",
 """The answer, with the verb taken from the question: 'Eunaeum… primum (deicit)'. 'Clitio… patre', 'with Clitius as father', ablative of origin, a common way to name a warrior's father; the Latin Library spells it 'Clytio'. 'cuius… pectus', 'whose… breast', the relative clause enclosing the rest. 'apertum', 'open', unprotected. 'adversi', genitive agreeing with 'cuius', 'of him facing her'. 'abiete', 'with fir', the wood of her spear-shaft: the i is a consonant, so 'ab-ye-te', three syllables with the first long. 'transverberat', 'strikes clean through'. No elisions."""),
(669, 'versat.',
 """of blood he, vomiting streams, falls, and the bloody\nhe chews ground, and dying in his own wound turns himself.""",
 """he falls, spewing out rivers of blood, bites the bloodied earth, and writhes in his own wound as he dies.""",
 """'sanguinis… rivos', 'streams of blood', framing 'ille vomens'. 'cruentam… humum', the adjective and noun across the line-break. 'mandit humum', 'chews the ground', the Homeric picture of the fallen warrior biting the dust, met already at 418 ('humum ore momordit'). 'suo se in volnere versat', 'turns himself in his own wound', writhes in his blood. 'volnere', Greenough's old spelling of 'vulnere'; he is not consistent, and prints 'vulnus' at 698. 'moriens', 'dying', with the present: the death is drawn out. Elision 's(e) in'."""),
(673, 'ruunt.',
 """Then Liris and Pagasus on top; of whom the one the reins,\nhis horse stabbed from beneath, rolled back, while he gathers, the other\nwhile he comes up and his right hand to the falling one holds out, unarmed,\nheadlong and together they fall.""",
 """Then Liris and Pagasus besides: one had been thrown back as his horse was stabbed from under him and was gathering up the reins, the other was coming up and holding out his unarmed hand to his falling friend, when both together went down headlong.""",
 """'Tum… super', 'then, on top of these', 'super' an adverb, with 'deicit' understood again. 'Lirim', accusative of 'Liris', also the name of a river of Latium. 'quorum alter… alter', 'of whom the one… the other', each with a 'dum'-clause. 'suffosso… equo', ablative absolute, 'his horse stabbed from below'. The Latin Library reads 'suffuso', which would mean something like 'his horse sprawled under him': a real difference of sense, though the picture of the fall is much the same; Greenough's reading is kept. 'revolutus', 'rolled back'. 'labenti', 'to the one slipping', dative. 'inermem', his hand empty of its weapon, held out to help. 'praecipites', plural, 'headlong'. Elision 'quoru(m) alter'."""),
(675, 'Chrominque;',
 """To these she adds Amastrus,\nson of Hippotes, and she pursues, leaning on, from afar, her spear,\nTereus and Harpalycus and Demophoon and Chromis;""",
 """To these she adds Amastrus, son of Hippotes, and, bearing down with her spear from a distance, she hunts down Tereus, Harpalycus, Demophoon and Chromis;""",
 """'His addit', 'to these she adds', with the dative. 'Hippotaden', Greek accusative of the patronymic 'Hippotades', 'son of Hippotes', a name Homer gives to Aeolus; this is some other man. 'incumbens… hasta', 'leaning on her spear', putting her weight behind the throw; 'eminus', 'at a distance', so she throws rather than thrusts. The four names are Greek accusatives: 'Terea' (Tereus), 'Demophoonta' (Demophoon), 'Chromin' (Chromis; the Latin Library spells it 'Chromim'). The string of '-que… -que… et… -que' runs the victims together, a mere roll-call. Elisions 'sequiturqu(e) incumbens', 'Tereaqu(e) Harpalycumque', 'Harpalycumqu(e) et'."""),
(677, 'viri.',
 """and as many as, sent from her hand, she whirled, shafts, the maiden,\nso many Phrygian fell men.""",
 """and for every shaft the maiden sent whirling from her hand, a Phrygian warrior fell.""",
 """'quot… tot', 'as many… so many', correlatives: every throw a kill. 'emissa manu… spicula', 'shafts sent from the hand', here javelins or arrows. 'contorsit', 'whirled, hurled'. 'cecidere' = 'ceciderunt', the old third-person plural perfect in '-ere' (you have seen it many times now). 'Phrygii', 'Phrygian', the Latins' scornful word for the Trojans; many of her victims are in fact Etruscan allies of Aeneas, like Ornytus, who follows. Elision 'quotqu(e) emissa'."""),
(681, 'albis,',
 """Some way off Ornytus, in arms\nunfamiliar and on a horse, a hunter, Iapygian, is borne along,\nwhose hide the broad shoulders, torn from a bullock,\nfor a fighter, covers; the head the huge of the mouth gape\nand the jaws covered of a wolf, with teeth white,""",
 """Some way off rode Ornytus, a hunter, in outlandish gear and mounted on an Apulian horse; a hide stripped from a bullock covered the broad shoulders of this fighter, and his head was cased in the huge gaping mouth and jaws of a wolf, white teeth and all,""",
 """'Procul', 'at a distance', standing out on the field. 'armis ignotis', 'in unfamiliar arms', not a soldier's. 'equo… Iapyge', 'on an Iapygian horse', from Apulia in the heel of Italy, horse-breeding country. 'cui… umeros', 'whose shoulders', dative of reference. 'pugnatori', 'for a fighter', is hard: most take it with 'cui', the shoulders of a man now turned fighter, the hunter's gear gone to war; some join it with 'iuvenco', 'a fighting bullock'. 'oris hiatus et malae… lupi', 'the gape of the mouth and the jaws of a wolf', a wolf-skin cap, such as Dolon wore in the Iliad (X.334, from memory). 'texere' = 'texerunt', 'covered'. Elision 'pugnator(i) operit'."""),
(683, 'est.',
 """and his rustic hands arms a hunting-spear; he himself the troops\nturns about in the midst of, and by his whole head above is.""",
 """and a countryman's hunting-spear armed his hands; he wheeled about in the midst of the squadrons, taller than them all by a whole head.""",
 """'agrestis… manus', accusative plural, 'his countryman's hands'; or 'agrestis' is nominative with 'sparus', 'a rustic spear': Greenough's '-is' plural lets both stand. 'sparus', a short hunting-spear, a peasant's weapon. 'catervis… in mediis', 'in the midst of the troops', the preposition placed after the first word. 'vertitur', 'turns about', passive in middle sense. 'toto vertice supra est', 'is above by his whole head', taller than all: Homer marks Ajax and Agamemnon out the same way (Iliad III.193 and 227, from memory). A big, conspicuous target. Elision 'supr(a) est'."""),
(685, 'fatur:',
 """Him she, caught (nor indeed was it toil, the column being turned),\npierces, and over him these words from a hostile breast speaks:""",
 """She caught him as his troop broke (no hard task), ran him through, and standing over him spoke these words from a heart full of enmity:""",
 """'Hunc… exceptum… traicit', 'she catches him and runs him through', the participle doing the work of a first verb. 'neque enim labor', a parenthesis, 'for it was no toil', with 'erat' understood. 'agmine verso', ablative absolute, 'the column turned', put to flight. 'super', adverb, 'over (him)', though it can mean 'besides'. 'haec… fatur', 'speaks these things', so a speech follows. 'inimico pectore', 'from a hostile breast'. The taunt over a fallen enemy is a Homeric habit, and Virgil gives it to his fighters on both sides. Elision 'ill(a) exceptum'."""),
(686, 'putasti?',
 """“In the woods you, Tyrrhenian, wild beasts were hunting, did you think?""",
 """“Did you think, Etruscan, that you were out in the woods chasing game?""",
 """Camilla's taunt begins. 'Tyrrhene', vocative, 'Tyrrhenian', that is Etruscan: Ornytus is one of the Etruscans who have come to fight for Aeneas. 'Silvis', ablative of place, 'in the woods'. 'te… agitare', accusative and infinitive after 'putasti', 'that you were hunting'. 'putasti' = 'putavisti', a syncopated perfect, very common. 'feras', 'wild beasts': his hunting costume shows that he took war for sport, and he has met the huntress of Diana. No elisions."""),
(688, 'redarguerit.',
 """Has come, which your, the day, with women's arms\nwords should refute.""",
 """The day has come to prove your people's boasts false by a woman's weapons.""",
 """'Advenit… dies', 'the day has come', the subject held back. 'qui… redarguerit', a relative clause of purpose or characteristic, 'such as to refute', in the perfect subjunctive, as if the refutation were already complete. The Latin Library has 'redargueret', imperfect, 'which was to refute': a shade of tense, not a change of meaning. 'vestra… verba', 'your words', plural: the Etruscans' scorn for a woman in arms (their leader Tarchon will soon reproach his men for running from one). 'muliebribus armis', 'with women's arms', instrumental. No elisions."""),
(689, 'Camillae.”',
 """A name, however, not light, of your fathers\nto the shades this you will carry back: by the weapon to have fallen of Camilla.”""",
 """Still, it is no slight fame that you will carry back to the shades of your fathers: that you fell by Camilla's weapon.”""",
 """'Nomen… haud leve', 'a name not light', a distinction, by litotes. 'patrum manibus', 'to the Manes of your fathers', the spirits of the dead below. 'hoc', explained by the infinitive clause 'telo cecidisse Camillae', 'to have fallen by the weapon of Camilla'. 'referes', future, 'you will carry back'. The consolation is cruel and proud at once; Aeneas told the dying Lausus that he fell by the hand of great Aeneas (X.830, from memory). 'patrum', genitive plural, Ornytus's ancestors. The speech ends here. No elisions."""),
(693, 'lacerto,',
 """Next Orsilochus and Butes, the two greatest of the Teucrians\nbodies; but Butes, turned away, with her spear-point she pierced\nthe corslet and the helmet between, where the neck of the seated rider\nshows bright and from the left hangs the shield arm,""",
 """Next Orsilochus and Butes, the two biggest men among the Trojans: Butes she pierced from behind with her spear-point, between corslet and helmet, where the neck of the seated rider shows and the shield hangs from the left arm;""",
 """'Protinus', 'straightway'. The two accusatives wait for a verb that never comes: the sentence breaks off and starts again with 'sed', taking each man in turn, an anacoluthon. 'duo maxima Teucrum corpora', 'the two biggest bodies of the Teucrians', 'Teucrum' the old genitive plural in '-um'. 'Buten', Greek accusative. 'aversum', 'turned away'. 'loricam galeamque inter', 'between corslet and helmet', the preposition after its nouns. 'sedentis', 'of (him) sitting', on horseback. 'lucent', 'gleam', show bare. 'laevo… lacerto', framing 'dependet parma'. Elision 'Orsiloch(um) et'."""),
(695, 'sequentem,',
 """Orsilochus, fleeing and, through a great circle chased,\nshe baffles, inside on the ring, and follows the follower,""",
 """Orsilochus she fled from, and, chased round a wide circle, gave him the slip by wheeling on the inside, and was soon hunting her hunter;""",
 """'Orsilochum… eludit', 'she baffles Orsilochus'. 'fugiens', 'fleeing', a feint. 'magnum… per orbem', 'through a great circle', framing 'agitata', 'driven, chased'. 'gyro interior', 'inside (him) on the ring', cutting the circle tighter until she comes round behind him; 'gyrus' is the ring in which horses were schooled. 'sequiturque sequentem', 'and follows the follower', the same verb twice: the pursuer becomes the pursued. Elisions 'magnumqu(e) agitata', 'gyr(o) interior'."""),
(698, 'cerebro.',
 """then the stout, both through the armour of the man and through the bones, axe,\nhigher rising, to him begging and much praying,\nshe redoubles: the wound with warm wets his face brain.""",
 """then, rising tall, she brought her heavy axe down again and again through the man's armour and through his bones, while he begged and prayed and pleaded: the wound drenched his face with warm brains.""",
 """'validam… securim', 'the stout axe', framing the line; here Greenough prints the usual accusative 'securim' (compare 'securem', 656). 'perque… perque', 'both through… and through'. 'viro', dative of disadvantage, 'on the man'. 'altior exsurgens', 'rising higher', to strike down from above. 'oranti et multa precanti', 'to him begging and praying much', also dative: his pleas count for nothing. 'congeminat', 'doubles, redoubles', blow on blow. 'vulnus… cerebro', 'the wound wets his face with warm brain'; 'vulnus', so spelt here, though 669 had 'volnere'. Elisions 'perqu(e) arma', 'perqu(e) ossa', 'orant(i) et'."""),
(701, 'sinebant.',
 """Fell in with her, and at the sudden sight, terrified, stuck fast\nof the Apennine-dweller the warrior son, Aunus,\nnot of the Ligurians the last, while to deceive the fates allowed.""",
 """Into her path came the warrior son of Aunus, who dwelt on the Apennines, and, terrified by the sudden sight, stood rooted: not the least of the Ligurians, so long as the fates let him cheat.""",
 """'Incidit huic', 'fell upon her', came across her path. The subject is held to the next line, 'bellator filius Auni', 'the warrior son of Aunus', and he is never named. 'Appenninicolae', 'Apennine-dweller', a compound like 'caelicola'. The Ligurians, hill-tribes of the north-west, were proverbial at Rome for cunning and lying; Servius cites Cato on them (from memory). 'haud… extremus', 'not the last', litotes. 'Ligurum', old genitive plural. 'dum… sinebant', 'while the fates allowed (him) to deceive', ironic: they are about to stop allowing it. Elision 'subitoqu(e) aspectu'."""),
(705, 'haec:',
 """And he, when himself by no running now to escape from the fight\nable nor the pressing queen to turn away he sees,\nwith planning to turn over tricks having begun and with cunning,\nbegins these words:""",
 """When he saw that no speed could carry him clear of the fight now, and that he could not turn the queen aside as she pressed upon him, he set to work to devise a trick with craft and cunning, and began:""",
 """'Isque ubi… cernit', 'and he, when he sees', vivid present. 'se… evadere… posse… avertere', accusative and infinitive: 'that he could neither escape… nor turn away'. 'nullo… cursu', 'by no running', his horse's or his own. 'pugnae', dative of separation with 'evadere', 'get clear of the fight'. 'reginam', Camilla, queen of the Volscians. 'consilio… et astu', 'with planning and with cunning', the pair split around the line. 'versare dolos', 'to turn over tricks', 'verso' the frequentative of 'verto'. 'ingressus', 'having begun', with an infinitive. 'incipit haec', 'begins thus', the verb of speaking at its barest. Elisions 'curs(u) evadere', 'nequ(e) instantem', 'regina(m) avertere'."""),
(706, 'equo?',
 """“What so remarkable, if you, a woman, in a strong\ntrust horse?""",
 """“What is so remarkable in it, if you, a woman, put your trust in a strong horse?""",
 """The Ligurian's speech begins, and plays on the very prejudice Camilla has just punished in Ornytus. 'Quid tam egregium', 'what (is) so remarkable', 'est' understood. 'femina', in apposition to the subject of 'fidis': 'you, a woman'. 'forti… equo', 'a strong horse', across the line-break. 'fido', 'trust', takes the dative ('equo'). He means that her victories belong to the horse, not to her, and so he hopes to get her off it. Elision 'ta(m) egregium'."""),
(708, 'fraudem.”',
 """Dismiss your flight and yourself hand to hand on level\nwith me trust ground, and for the fight gird yourself, on foot:\nsoon you will know to whom windy glory brings harm.”""",
 """Send away the horse you run on; trust yourself to meet me hand to hand on level ground and make ready to fight on foot: you will soon learn which of us comes to grief through empty craving for glory.”""",
 """'Dimitte fugam', 'dismiss your flight', send away the horse that lets you escape. 'te… crede', 'trust yourself', with 'comminus', 'at close quarters', and 'aequo… solo', 'on level ground'. 'pugnaeque adcinge pedestri', 'and gird (yourself) for a fight on foot', 'te' understood again; 'adcinge' is Greenough's spelling of 'accinge'. 'iam', 'soon'. 'ventosa… gloria', 'windy glory', empty boasting. 'fraudem', 'harm', the old legal sense of 'fraus', loss or damage; the word is ironic in the mouth of a man whose whole plan is a fraud. 'cui… ferat', indirect question. Elisions 'fug(am) et', 'pugnaequ(e) adcinge'."""),
(711, 'parma.',
 """He spoke; but she, raging, and by sharp inflamed resentment,\nhands her horse to a companion and in equal stands firm arms,\nwith sword, on foot, naked, and with plain, undaunted, shield.""",
 """So he spoke; but she, furious and stung by sharp resentment, handed her horse to one of her companions and stood to face him on equal terms, on foot, fearless, with naked sword and unmarked shield.""",
 """'Dixit', 'he spoke', the closing formula. 'furens… adcensa dolore', 'raging and inflamed with indignation'; 'adcensa' is Greenough's spelling of 'accensa'. 'comiti', one of the companions of 655. 'paribus… in armis', 'in equal arms', on foot like him, as he asked. 'resistit', 'takes her stand'. 'pedes', a noun, 'a foot-soldier', so 'on foot'. 'ense… nudo', 'with naked sword'. 'pura… parma', 'with a plain shield', bearing no device. 'interrita', 'undaunted', has a short final a in the metre, so it is nominative and goes with Camilla, not the shield. Elisions 'acriqu(e) adcensa', 'puraqu(e) interrita'."""),
(714, 'fatigat.',
 """But the youth, to have won by his trick thinking, flies off himself,\nno delay, and with reins turned, in flight, is carried away,\nand the four-footed swift with iron heel he wears out.""",
 """But the young man, thinking his trick had won, was off and away at once himself; he wheeled his reins, galloped off in flight, and drove his swift steed hard with his iron-shod heel.""",
 """'vicisse dolo ratus', 'thinking that he had won by his trick', 'ratus' from 'reor', with a perfect infinitive. 'avolat ipse', 'flies off himself', on the very horse he urged her to give up. 'haud mora', 'no delay', a parenthesis Virgil likes. 'conversis… habenis', ablative absolute, 'with reins turned'. 'fugax', 'in flight'. 'quadrupedem… citum', 'the swift four-footed (one)', his horse; the Latin Library spells it 'quadripedemque'. 'ferrata calce', 'with iron-shod heel', a spur. 'fatigat', 'wears out', drives hard. No elisions."""),
(717, 'Auno,”',
 """“Foolish Ligurian, and in vain in spirit lifted up, proud,\nfor nothing your fathers' you have tried, slippery one, arts,\nnor will trickery you unharmed to deceitful carry home Aunus,”""",
 """“Empty-headed Ligurian, puffed up for nothing with your proud spirit, it is to no purpose you have tried the slippery arts of your fathers, and your trickery will not carry you home unharmed to Aunus, the old deceiver,”""",
 """Camilla's answer, with the verb of speaking put after it ('haec fatur', 718). 'Vane… elate', vocatives, 'foolish… lifted up'; 'animis… superbis', 'in proud spirit', framing. 'patrias… artis', 'your fathers' arts', the Ligurian gift for lying, 'artis' the '-is' accusative plural. 'temptasti' = 'temptavisti', syncopated. 'lubricus', 'slippery'. 'perferet', 'will carry (you) through'. 'fallaci… Auno', dative of goal, 'to deceitful Aunus'. The print closes the speech at the end of 717, after the comma, as it often does: the speech is just these three lines, and the sentence runs on. Elisions 'frustraqu(e) animis', 't(e) incolumem'."""),
(720, 'sumit:',
 """these things speaks the maiden, and on swift, fiery, soles\npasses the horse in running, and, facing him, the reins seized,\nshe engages and penalty from his hostile blood exacts:""",
 """so the maiden spoke, and on her flying feet, quick as fire, she outran the horse, caught the reins, turned to face him, closed with him and took her vengeance from his hated blood:""",
 """'haec fatur virgo', the speech-formula placed after the speech. 'pernicibus… plantis', 'on swift soles', framing 'ignea', 'fiery', of speed and anger together. In Book VII Virgil said Camilla could skim over standing corn without bruising the ears (VII.808–811, from memory). 'transit… cursu', 'passes in running': a girl on foot overtakes a galloping horse. 'frenis… prehensis', ablative absolute, 'the reins seized'. 'adversa', 'face to face'. 'poenas… sumit', 'exacts the penalty', 'inimico ex sanguine', 'from hostile blood'. Elisions 'virg(o) et', 'poenasqu(e) inimico', 'inimic(o) ex'."""),
(724, 'plumae.',
 """as easily as the hawk from a rock, the sacred bird, from high\novertakes on the wing, aloft in a cloud, a dove,\nand seized holds her, and with feet disembowels hooked;\nthen blood and plucked drift down from the sky feathers.""",
 """as easily as a hawk, the holy bird, swooping from a high crag, overtakes on the wing a dove high up in a cloud, seizes and holds her and tears out her entrails with crooked talons, and the blood and the torn feathers come floating down out of the sky.""",
 """'quam facile', 'as easily as', a simile of manner. 'accipiter… sacer ales', 'the hawk, the holy bird', sacred to Apollo; in the Odyssey a hawk is called Apollo's swift messenger (XV.526, from memory). 'saxo… ab alto', framing the phrase. 'sublimem in nube', 'aloft in a cloud'. 'comprensam… tenet', 'holds her seized'. 'pedibus… uncis', 'with hooked feet', talons, framing 'eviscerat', 'disembowels'. 'vulsae… plumae', 'plucked feathers', framing the last line. The model is Achilles chasing Hector like a hawk after a dove (Iliad XXII.139–142, from memory); here the woman is the hawk. Elisions 'facil(e) accipiter', 'sublim(em) in', 'pedibusqu(e) eviscerat'."""),
]

# Speech-mark check exemptions (rule 5b / doubtful marks), by unit ln: none.
# The print's marks are sound: 686-689 (Camilla to Ornytus), 705-708 (the Ligurian), 715-717 (Camilla to the
# Ligurian, closed inside the comma at 717, 'haec fatur virgo' following, as at the archive's other ',”').
EXEMPT = set()
P = A.part('aeneid-088'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
    if t.rstrip('”]')[-1] not in A.TERMINAL + ',': print('ENDING', ln, repr(t[-12:]))
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
