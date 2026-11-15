# aeneid-078 (X.510-605): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Aeneae furor. Inferiae'
PART = "The Rage of Aeneas (X.510–605)"
TITLE_EN = "The Rage of Aeneas — Aeneid X.510–605"
ABOUT = ("A surer messenger than rumour reaches Aeneas: his men are close to destruction. With Pallas and Evander before his "
"eyes, and the table and the handclasp of friendship he was given in Evander's city, he cuts a lane through the battle looking "
"for Turnus, and takes eight young men alive to be sacrificed at Pallas's pyre, as Achilles did for Patroclus. Then he kills "
"everyone in his path and refuses every plea: Mago, who clasps his knees and offers buried silver and gold as ransom; a priest "
"of Apollo and Diana, slaughtered like a victim; Anxur, who had promised himself a long old age; Tarquitus, son of Faunus, "
"whose head he strikes off as he begs, leaving the body to the birds and the fish; and the brothers Lucagus and Liger, who "
"charge him in a chariot, the one boasting, the other begging. Likened to the hundred-handed giant Aegaeon fighting Jupiter, "
"he rages across the plain like a flood or a black whirlwind, until at last Ascanius and the besieged Trojans break out of "
"their camp. Virgil models these scenes closely on the rage of Achilles after the death of Patroclus in the Iliad.")

U = [
(512, 'Teucris.',
 """And now no rumour of so great a disaster, but a surer messenger\nflies to Aeneas: by a slender margin from death\nare his men; the routed Teucrians it is time to help.""",
 """No longer is it only rumour of the disaster, but a surer messenger who speeds to Aeneas: his men are a hair's breadth from death, and it is time to help the routed Trojans.""",
 """A new paragraph in Greenough. The poem returns to Aeneas, who has been fighting elsewhere while Turnus killed Pallas. 'Nec iam fama… sed certior auctor', 'no longer a rumour… but a surer informant': an 'auctor' is the person who vouches for a report. 'advolat Aeneae', 'flies to Aeneas', dative with a compound verb. What the messenger reports follows as reported speech, accusative and infinitive with the verb of saying understood: 'esse suos', 'that his men are', and 'tempus (esse) succurrere', 'that it is time to help'. 'tenui discrimine leti', 'by a thin margin of death', ablative of measure: a 'discrimen' is the dividing line. 'versis… Teucris', 'the turned Teucrians', in flight; dative with 'succurrere'. No elisions."""),
(515, 'quaerens.',
 """All the nearest he reaps with the sword, and through the broad column\nblazing he drives a path with the steel, you, Turnus, proud\nwith new slaughter, seeking.""",
 """He mows down everything nearest him with the sword and, blazing with anger, cuts a wide lane through the enemy ranks with the steel, looking for you, Turnus, proud of your fresh kill.""",
 """'Proxima quaeque', 'all the nearest', the neuter plural of 'quisque' with a superlative, 'each nearest thing'. 'metit', 'reaps', the harvest picture for slaughter. 'limitem agit', 'drives a path': a 'limes' is the boundary track between fields, so he cuts a lane through the ranks. 'ferro', 'with the steel', the sword again. 'te, Turne', the poet turns to address Turnus directly (apostrophe), as he addressed Pallas at the end of the last part. 'superbum caede nova', 'proud with the fresh slaughter', the killing of Pallas. 'quaerens', held to the end: everything Aeneas does here is a search for one man. Elision 'limit(em) agit'."""),
(517, 'datae.',
 """Pallas, Evander, before his very\neyes all are, the tables to which as a stranger first\nhe then came, and the right hands given.""",
 """Pallas, Evander, everything is before his eyes: the table to which he first came as a stranger, and the right hands pledged in friendship.""",
 """'in ipsis… oculis', 'in his very eyes', the adjective and noun set apart across the line. 'Euander', Greenough's spelling of Evander (Greek 'Euandros'), as in the last part. 'omnia sunt', 'all things are', and then the list in apposition. 'mensae', 'the tables', plural for singular: Evander's feast, at which Aeneas arrived in Book VIII. 'advena', 'as a newcomer'. 'tunc', 'then', that first time. 'dextrae datae', 'right hands given', the clasp that seals an alliance between guest-friends. Aeneas brought Pallas to the war, and Evander gave the boy into his keeping. No elisions."""),
(520, 'flammas.',
 """Born of Sulmo,\nfour young men here, as many whom Ufens rears,\nliving he seizes, to sacrifice them as offerings to the shades\nand with captive blood to drench the pyre's flames.""",
 """Here he takes alive four young men, sons of Sulmo, and as many reared by the Ufens, to offer up as a sacrifice to the dead and to drench the flames of the pyre with captives' blood.""",
 """Aeneas takes prisoners for human sacrifice at Pallas's funeral, as Achilles takes twelve Trojan youths alive from the river to kill at Patroclus's pyre (Iliad 21.26–32, 23.175–176); the sacrifice is carried out in Book XI. 'Sulmone creatos', 'born of Sulmo', ablative of origin: Sulmo may be their father (a Rutulian Sulmo dies in Book IX) or a town. 'quos educat Ufens', 'whom the Ufens rears', a river of Latium, the present tense for their home country. 'viventis', 'living', accusative plural in '-is'. 'inferias', 'as offerings to the dead', in apposition. 'quos immolet… perfundat', a relative clause of purpose with the subjunctive, 'to sacrifice… to drench'. No elisions."""),
(521, 'hastam.',
 """Then at Mago from afar his hostile spear he had aimed.""",
 """Next, from a distance, he had levelled his deadly spear at Mago.""",
 """'Inde', 'next'. 'Mago', dative, 'at Mago', with 'contenderat', 'had aimed': 'contendere hastam' is to strain and hurl a spear at a mark. The pluperfect jumps straight to the result, the spear already on its way, and the next line picks up the action from there; you will see the same quick pluperfect at 546. 'infensam', 'hostile', the weapon given the feeling of the man who throws it. No elisions."""),
(523, 'supplex:',
 """He with cunning ducks under, and quivering flies over the spear,\nand the knees embracing speaks such words, a suppliant:""",
 """Mago cleverly ducked under it, and the spear flew quivering over him; then he clasped Aeneas's knees and pleaded with him thus:""",
 """'Ille', Mago. 'astu subit', 'goes under by cunning', ducks. 'tremibunda supervolat hasta', 'the spear flies over, quivering', its subject held to the end of the line. 'genua amplectens', 'clasping (his) knees': the suppliant's gesture, which in Homer puts the one who makes it under the protection of Zeus. 'effatur talia', 'utters such things'. 'supplex', 'as a suppliant', an adjective where English uses a phrase. Mago's plea is modelled on the Trojans who beg for their lives in the Iliad and offer ransom: Adrastus to Menelaus (Iliad 6.45–50) and Lycaon to Achilles (Iliad 21.64–96). Elisions 'Ill(e) astu', 'genu(a) amplectens'."""),
(525, 'patrique.',
 """“By your father's shades and the hopes of rising Iulus\nI beg you, this life spare for son and for father.""",
 """“By the spirit of your father, by the hopes you have in Iulus as he grows to manhood, I beg you, spare this life of mine for my son and my father.""",
 """'Per patrios manis', 'by your father's shades', Anchises, who died in Sicily; 'manis' is accusative plural in '-is', and 'manes', the spirits of the dead, is always plural. 'spes surgentis Iuli', 'the hopes of rising Iulus', the hopes Aeneas has in his growing son; Palinurus begged Aeneas in the underworld with the same words (VI.364). 'Iuli' is three syllables, I-u-li. 'te precor… serves', 'I beg you, save', the subjunctive without 'ut' after a verb of asking. 'nato… patri', datives, Mago's own son and father, set against the father and son he invokes in Aeneas. No elisions."""),
(528, 'mihi.',
 """There is a house, lofty; there lie deep buried talents\nof chased silver; there are of gold weights, worked\nand unworked, to me.""",
 """I have a lofty house, with talents of embossed silver buried deep in it, and masses of gold, both wrought and unwrought.""",
 """Mago offers ransom, the regular bargain on a Homeric battlefield. 'Est domus alta… mihi', 'there is to me', the dative of possession, with 'mihi' held to the end of the list. 'penitus defossa', 'buried deep', hidden treasure. 'talenta', 'talents', a Greek weight, here of precious metal. 'caelati argenti', 'of chased silver', silver plate engraved or embossed. 'pondera', 'weights', masses of bullion. 'facti infectique', 'worked and unworked', gold made into vessels and gold in the raw; 'infectus' here is simply 'not made'. Elision 'caelat(i) argenti'."""),
(529, 'tanta.”',
 """Not on this the victory of the Teucrians\nturns, nor will one life make differences so great.”""",
 """The Trojans' victory does not hang on me; a single life will not make so great a difference.”""",
 """'hic', 'here', on this one man. 'victoria Teucrum', 'the victory of the Teucrians', 'Teucrum' = 'Teucrorum', the old genitive plural. 'vertitur', 'turns', hinges. 'anima una', 'one life', the subject of 'dabit'. 'discrimina tanta', 'such great differences', plural for singular: the word that meant 'margin' at 511 here means a deciding difference. Mago argues that sparing him costs the Trojans nothing. The speech ends. Elision 'anim(a) una'."""),
(530, 'Dixerat.',
 """He had spoken.""",
 """So he spoke.""",
 """'Dixerat', 'he had spoken', the pluperfect that so often closes a speech in Virgil: the speech is over and done before the next action begins. Aeneas's answer, which follows, is short and final. No elisions."""),
(530, 'reddit:',
 """Aeneas in reply to him such words returns:""",
 """And Aeneas answered him in these words:""",
 """'contra', 'in reply', an adverb. 'cui', 'to him', a connecting relative put late in its clause: 'and to him'. 'talia reddit', 'gives back such things', answers; 'reddere' is an ordinary epic verb for a reply. Mago spoke for six lines; Aeneas answers in four. No elisions."""),
(532, 'tuis.',
 """“Of silver and gold which you recount, the many talents,\nfor your sons spare them.""",
 """“All those talents of silver and gold you speak of, keep them for your sons.""",
 """'quae multa talenta… memoras', 'the many talents which you mention': the noun is drawn into the relative clause, and the clause comes first, standing as the object of the main verb. 'Argenti atque auri', genitives with 'talenta'. 'parce', 'be sparing (of them)', 'parco' in its sense of 'keep, save'; 'natis… tuis', 'for your sons', dative of advantage. Aeneas turns Mago's own words back on him: Mago asked to be spared for his son (525), and it is the gold that is spared for the sons. Elisions 'Argent(i) atque', 'atqu(e) auri'."""),
(533, 'perempto.',
 """War's bargainings Turnus\ndid away with, those, before me, already then when Pallas was slain.""",
 """Turnus did away with such trading in war before ever I did, the moment he killed Pallas.""",
 """'Belli commercia… ista', 'those dealings of war', ransom and the exchange of prisoners; 'ista', 'those (you speak of)', with contempt. 'sustulit', 'removed, abolished', perfect of 'tollo'. 'prior', 'first', before Aeneas: Turnus set the rule. 'iam tum Pallante perempto', 'already then, when Pallas was slain', an ablative absolute; 'peremptus' is from 'perimo', 'destroy'. Achilles answers Lycaon in the same way: before Patroclus died he spared Trojans and sold them, but now no one will escape (Iliad 21.99–105). No elisions."""),
(534, 'Iulus.”',
 """This my father Anchises' shades, this feels Iulus.”""",
 """That is the judgment of my father Anchises' spirit, and that is the judgment of Iulus.”""",
 """'Hoc… sentit', 'this (is what)… feels', 'thinks, judges': 'sentio' is to hold an opinion. The singular verb serves both subjects, 'manes' and 'Iulus', with 'hoc' repeated before each (anaphora). Mago begged by Anchises and Iulus (524); Aeneas answers that they themselves would show him no mercy. 'patris Anchisae', 'of father Anchises', the noun in apposition to the name. The speech ends. No elisions."""),
(536, 'ensem.',
 """Thus having spoken, the helmet with his left he holds, and, bent back\nthe neck of the pleading man, to the hilt drives the sword.""",
 """With that he gripped Mago's helmet in his left hand, bent his neck back as he still begged, and drove the sword in up to the hilt.""",
 """'Sic fatus', 'having so spoken', the deponent participle with present sense. 'laeva', 'with the left (hand)'. 'reflexa cervice orantis', 'the neck of the man praying bent back', an ablative absolute; 'orantis', genitive of the present participle, 'of the one begging': he is still pleading when he dies. 'capulo tenus', 'as far as the hilt', 'tenus' put after its ablative, as it always is. 'applicat', 'drives home'. Elision 'cervic(e) orantis'."""),
(539, 'armis.',
 """Not far off Haemon's son, of Phoebus and Trivia the priest,\nwhose temples the headband with sacred ribbon bound,\nall gleaming in robe and in distinguished arms.""",
 """Not far off was the son of Haemon, priest of Phoebus and of Trivia, his temples bound with the priest's headband and its sacred ribbon, all gleaming in his robe and his splendid armour.""",
 """No verb: 'erat' is understood. 'Haemonides', 'son of Haemon', a Greek patronymic in '-ides' and the priest's only name. 'Phoebi Triviaeque', Apollo and Diana; 'Trivia', 'goddess of the three ways', is Diana as Hecate of the crossroads. The 'infula' was a band of wool worn on the head by priests, and by victims led to sacrifice; the 'vitta' was its ribbon. 'cui… tempora', 'whose temples', dative of reference. 'conlucens', Greenough's spelling of 'collucens', 'shining all over'. 'insignibus armis', 'distinguished arms'; The Latin Library reads 'insignibus albis', 'white insignia', the priest's white trappings, not his armour. Elisions 'vest(e) atque', 'atqu(e) insignibus'."""),
(541, 'tegit;',
 """Him, having met him, he drives over the plain, and, fallen, standing over him\nsacrifices, and with huge shade covers;""",
 """Aeneas closed with him and drove him across the field, then, standing over him where he fell, slaughtered him like a victim and wrapped him in vast darkness;""",
 """'Quem', the connecting relative, 'him'. 'congressus', 'having engaged', from the deponent 'congredior'. 'agit campo', 'drives (him) over the plain'. 'lapsum… superstans', 'standing over (him) fallen'. 'immolat', 'sacrifices', the word for killing a victim at the altar, used of a priest who wears a victim's headband; it echoes 'immolet' at 519. 'ingenti umbra tegit', 'covers with huge shadow', either the darkness of death or the shadow of the giant figure standing over him; both have been held. Elision 'ingentiqu(e) umbra'."""),
(542, 'tropaeum.',
 """the arms Serestus\ngathered carries back on his shoulders, for you, king Gradivus, a trophy.""",
 """Serestus gathered up his armour and carried it off on his shoulders, a trophy for you, Lord Gradivus.""",
 """'arma… lecta refert', 'carries back the arms, gathered', a participle and a verb where English uses two verbs. 'umeris', 'on his shoulders'. Serestus is one of Aeneas's captains. 'tibi, rex Gradive', the poet addresses Mars by 'Gradivus', an old Roman title of the war god. 'tropaeum', 'a trophy', in apposition to 'arma': a victor hung an enemy's armour on a post or a tree as an offering to the god, as Aeneas does with Mezentius's at the start of Book XI. No elisions."""),
(545, 'furit.',
 """Renew the battle lines, of Vulcan's stock born,\nCaeculus, and coming from the mountains of the Marsi Umbro:\nthe Dardanian against them rages.""",
 """Caeculus, born of Vulcan's stock, and Umbro, come from the mountains of the Marsi, rallied the lines; the Dardan hero raged against them.""",
 """'Instaurant acies', 'they renew the battle lines', the plural verb before its two subjects. Both are Italian allies of Turnus from the catalogue in Book VII: Caeculus, son of Vulcan and founder of Praeneste, and Umbro, a Marsian priest who could charm snakes. 'Volcani', Greenough's spelling of Vulcan's name. 'stirpe creatus', 'born of the stock', ablative of origin, as 'Sulmone creatos' at 517. 'Dardanides', 'the Dardanian', Aeneas, descendant of Dardanus, founder of Troy's royal line; the patronymic stands alone as a title. 'contra', an adverb, 'against (them)'. No elisions."""),
(546, 'orbem;',
 """Of Anxur with the sword the left arm\nand the whole of his shield with the steel he had struck off, the round;""",
 """With his sword he had struck off Anxur's left arm, and the whole round of his shield with it;""",
 """'Anxuris… sinistram', 'Anxur's left (hand)', the arm that carried the shield. 'deiecerat', 'had struck off', the quick pluperfect again (see 521): the blow has fallen before we are told of it. 'deiecerat' has the consonantal 'i' after the prefix: de-ie-ce-rat. 'totum clipei… orbem', 'the whole circle of the shield', framing the line. 'ense… ferro', 'with the sword… with the steel', the same weapon named twice, once for each object. No elisions."""),
(549, 'annos:',
 """he had said something great, and force would be present to his word\nhad believed, and to the sky his spirit perhaps was raising,\nand grey hairs for himself and long years had promised:""",
 """he had uttered some great boast and believed his words would have power behind them, and perhaps he was lifting his heart up to heaven and had promised himself grey hair and long years:""",
 """The poet looks back at Anxur a moment before the blow. 'dixerat… aliquid magnum', 'had said something big', a boast. 'vimque adfore verbo crediderat', 'and had believed that force would attend his word', accusative and infinitive; 'adfore', Greenough's spelling of 'affore', the future infinitive of 'adsum'. Perhaps a spell or a vow is meant, a word with power in it. 'caelo… animum… ferebat', 'was carrying his spirit to the sky', was full of confidence. 'canitiem', 'grey hair', old age. 'fortasse', 'perhaps': the narrator does not claim to know. Elisions 'ill(e) aliquid', 'vimqu(e) adfore', 'caeloqu(e) animum', 'sib(i) et'."""),
(552, 'obtulit.',
 """Tarquitus, exulting, against him in gleaming arms,\nwhom to forest-dwelling Faunus the nymph Dryope had borne,\nin his way, to the blazing one, put himself.""",
 """Tarquitus, exulting in his shining armour, whom the nymph Dryope had borne to Faunus of the woods, threw himself in the way of the blazing Aeneas.""",
 """'exultans', Greenough's spelling of 'exsultans', 'leaping, exulting'. 'contra', 'facing him', an adverb. 'silvicolae Fauno', 'to woodland-dwelling Faunus', dative: Faunus, an old Italian god of the countryside, is also the father of king Latinus (Book VII). 'Dryope', the nymph's name, from the Greek for oak. 'crearat' = 'creaverat', the shortened pluperfect. 'obvius ardenti sese obtulit', 'put himself in the way of the burning one', 'ardenti' Aeneas, dative with 'obvius'; 'sese' is a strengthened 'se'. Elision 'ses(e) obtulit'."""),
(553, 'hasta;',
 """He, drawn back,\nthe corselet and the shield's huge weight pins with his spear;""",
 """Aeneas drew back his spear and drove it through the corselet and the heavy mass of the shield, pinning them together;""",
 """'Ille', Aeneas, the subject changing with the pronoun, as often in these battle scenes. 'reducta… hasta', 'with spear drawn back', an ablative framing the line and a half: he draws it back to throw. 'loricam', 'the corselet', body armour. 'clipei ingens onus', 'the huge burden of the shield'. 'impedit', 'entangles, hampers': the spear goes through shield and corselet together and pins them, so that Tarquitus cannot use his arm. Elision 'clipeiqu(e) ingens'."""),
(556, 'fatur:',
 """then the head of him begging in vain and much preparing\nto say he strikes down to the earth, and the trunk, warm,\nrolling forward, over it these words with hostile breast he speaks:""",
 """then, as Tarquitus begged in vain and made ready to say much more, Aeneas struck his head to the ground, rolled the warm trunk forward, and spoke over it in his hatred:""",
 """'orantis… parantis', genitive participles with 'caput', 'the head of one praying… preparing': he is cut off mid-plea. 'nequiquam', 'in vain'. 'multa… dicere', 'to say many things', the infinitive held over to the next line, as his words are never spoken. 'deturbat terrae', 'knocks down to the earth', 'terrae' a dative of direction, poetic for 'in terram'. 'truncum… tepentem', 'the warm trunk', the body still warm. 'super haec… fatur', 'speaks these things over (it)'. 'inimico pectore', 'with a hostile breast'. Elision 'nequiqu(am) et'."""),
(557, 'iace.',
 """“There now, fearsome one, lie.""",
 """“Lie there now, you terror of the field.""",
 """The taunt over a fallen enemy is a Homeric habit, and what follows is modelled on Achilles' words over Lycaon (Iliad 21.122–127). 'Istic', 'there, where you are', the adverb that goes with the second person. 'metuende', the vocative of the gerundive, 'you who must be feared', in mockery. 'iace', imperative, 'lie'. No elisions."""),
(558, 'sepulchro:',
 """Not you your excellent mother\nwill lay in the ground, nor with the ancestral tomb load your limbs:""",
 """No loving mother will lay you in the earth or weigh your limbs down with your fathers' tomb:""",
 """'optima mater', 'your excellent mother', the nymph Dryope, with some irony. 'condet humi', 'will put away in the ground', 'humi' a locative, 'on the ground'. 'patrio… sepulchro', 'with the ancestral tomb', the family grave; 'sepulchro', Greenough's spelling of 'sepulcro'. 'onerabit membra', 'will load your limbs', a heavy tomb on the body, which is the honour denied. To lie unburied was among the worst fates in the ancient world: in Book VI an unburied shade cannot cross the Styx. Elisions 't(e) optima', 'patrioqu(e) onerabit'."""),
(560, 'lambent.”',
 """to the birds you will be left, the wild, or, in the flood sunk,\nthe wave will bear you, and fishes unfed your wounds will lick.”""",
 """you will be left to the birds of prey, or the current will sink you and carry you off, and hungry fish will lick your wounds.”""",
 """'linquere' = 'linqueris', 'you will be left', the future passive with the ending '-re' for '-ris', common in verse. 'alitibus… feris', 'to the wild birds', dative. 'gurgite mersum', 'sunk in the flood', the river or the sea near the field; 'mersum' agrees with 'te' understood. 'impasti', 'unfed', hungry. 'volnera', Greenough's spelling of 'vulnera'. Achilles throws Lycaon into the river with much the same words: no mother will lay him on a bier, and fish will lick the blood from his wound (Iliad 21.122–127). The speech ends. Elision 'piscesqu(e) impasti'."""),
(564, 'Amyclis.',
 """Straightway Antaeus and Lucas, the front ranks of Turnus,\nhe pursues, and brave Numa and tawny Camers,\nof great-hearted Volcens born, who richest in land\nwas of the Ausonians and reigned over silent Amyclae.""",
 """At once he went after Antaeus and Lucas, foremost in Turnus's ranks, and brave Numa and fair-haired Camers, son of great-hearted Volcens, who had been the richest landholder among the Ausonians and reigned in silent Amyclae.""",
 """'prima agmina Turni', 'the front ranks of Turnus', in apposition to the two names. 'persequitur', 'hunts down'. 'fulvum', 'tawny', golden-haired. 'magnanimo Volcente satum', 'sprung from great-hearted Volcens', ablative of origin with 'satus', 'sown, begotten'. 'ditissimus agri', 'richest in land', genitive with the adjective. 'Ausonidum', 'of the Ausonians', Italians, the old genitive plural again. 'tacitis… Amyclis', 'silent Amyclae', a town on the coast of Latium: the old story is that, tired of false alarms, its people forbade all talk of enemies, and so were taken unawares. A Camers appears alive again in Book XII; Virgil left such details unrevised at his death. Elisions 'Antae(um) et', 'prim(a) agmina', 'Ausonid(um) et'."""),
(568, 'enses:',
 """As Aegaeon, to whom a hundred arms, they say,\nand a hundred hands, and from fifty mouths fire\nand breasts blazed, when against Jove's thunderbolts\nwith so many equal shields he clashed, so many swords drew:""",
 """Like Aegaeon, who, they say, had a hundred arms and a hundred hands, with fire blazing from fifty mouths and fifty breasts, when against the thunderbolts of Jupiter he clashed as many matching shields and drew as many swords:""",
 """The simile. 'Aegaeon qualis', 'such as Aegaeon (was)', 'qualis' answered by 'sic' in the next unit. Aegaeon is the hundred-handed giant whom, Homer says, the gods call Briareus and men Aegaeon (Iliad 1.401–404); in Homer he comes to the help of Zeus, but Virgil follows a version in which he fought against Jupiter. 'centum cui bracchia dicunt', 'to whom they say (there were) a hundred arms', dative of possession in reported speech. 'centenas', distributive, 'a hundred each'. 'ignem… arsisse', 'fire blazed', accusative and infinitive with 'dicunt'. 'quinquaginta oribus pectoribusque', 'from fifty mouths and breasts', ablative. 'streperet… stringeret', subjunctives with 'cum'. Elisions 'quinquagint(a) oribus', 'pectoribusqu(e) arsisse'."""),
(570, 'mucro.',
 """so over the whole plain Aeneas rages, victor,\nonce it had grown warm, his blade.""",
 """so Aeneas raged in victory over the whole field, once his blade had grown warm with blood.""",
 """'sic' answers 'qualis': one man fighting like a hundred. 'desaevit', 'rages to the full', 'de-' strengthening the verb. 'toto… in aequore', 'over the whole plain', the open field. 'victor', 'as victor', in apposition. 'ut semel', 'when once', as soon as. 'intepuit', 'grew warm', an inceptive verb from 'tepeo', with the blood of the first kill. 'mucro', 'the point', the sword. Elision 'tot(o) Aeneas'."""),
(571, 'tendit.',
 """Nay, look, against Niphaeus's\nfour-yoked horses and their facing breasts he makes.""",
 """And now, see, he makes straight for the four-horse chariot of Niphaeus and the horses' breasts as they come on.""",
 """'Quin ecce', 'nay, look', 'quin' marking a step further. 'Niphaei', genitive, with 'equos'. 'quadriiugis in equos', 'against the four-yoked horses', a four-horse chariot; 'quadriiugis' has the consonantal 'i' written double, as 'biiugis' (575). 'adversa pectora', 'the breasts facing (him)', the horses'. 'tendit', 'directs his course'. No elisions."""),
(574, 'currus.',
 """And they, him from afar striding and dreadful things roaring,\nwhen they saw, by fear turned and backward rushing\nboth pour out their master and snatch to the shore the chariot.""",
 """But the horses, when they saw him striding at them from far off with a terrible roar, wheeled round in fear and bolted, threw out their master, and dragged the chariot away to the shore.""",
 """'illi', the horses. 'longe gradientem', 'striding long', with great steps. 'dira frementem', 'roaring dreadful things', the neuter plural used as an adverb. 'ut videre', 'when they saw', 'videre' = 'viderunt', as so often. 'versi… retroque ruentes', participles, 'turned and rushing back'; then 'effunduntque… rapiuntque', the double '-que… -que', 'both… and', joining the two main verbs. 'effundunt ducem', 'pour out their master', fling him from the car. 'currus', 'the chariot', poetic plural. Elisions 'Atqu(e) illi', 'gradient(em) et', 'rapiuntqu(e) ad'."""),
(576, 'Liger;',
 """Meanwhile with two-yoked team carries himself Lucagus, white,\ninto the midst, and his brother Liger;""",
 """Meanwhile Lucagus drove his pair of white horses into the thick of the fight, and his brother Liger with him;""",
 """'biiugis… albis', 'with a white two-horse team', ablative, framing the line; 'biiugis' has the doubled consonantal 'i', as at 571. 'infert se', 'carries himself in', charges. 'in medios', 'into the midst (of the enemy)'. 'fraterque Liger', the second subject added after the verb, so the singular 'infert' agrees with the first. Two brothers in one chariot, one to drive and one to fight, are a common pair in the Iliad. No elisions."""),
(577, 'ensem.',
 """but the brother with the reins\nturns the horses, his drawn sword whirls, fierce, Lucagus.""",
 """his brother handled the reins and wheeled the horses, while Lucagus, eager for the fight, whirled his drawn sword.""",
 """'frater', Liger, the driver. 'habenis flectit equos', 'turns the horses with the reins'. 'strictum… ensem', 'the drawn sword', framing the second half of the line. 'rotat', 'whirls round', brandishes. 'acer', 'keen, fierce', an adjective where English might use an adverb. The two halves of the line set the brothers' tasks side by side with no conjunction between them (asyndeton). No elisions."""),
(578, 'furentis:',
 """Not did bear Aeneas them with so great heat raging:""",
 """Aeneas would not endure their frenzied onset:""",
 """'Haud tulit', 'did not bear', did not put up with. 'tanto fervore furentis', 'raging with such fire', the alliteration of 'f' carrying the heat; 'furentis' is accusative plural in '-is', the two brothers. The colon looks forward to what he does about it. No elisions."""),
(579, 'hasta.',
 """he rushed in, and with spear levelled huge appeared.""",
 """he charged, and loomed up huge before them with his spear levelled.""",
 """'inruit', Greenough's spelling of 'irruit', 'rushed in'. 'adversa… hasta', 'with spear turned toward them', ablative, levelled at the enemy. 'ingens apparuit', 'appeared huge', a predicate adjective: Aeneas's great stature in battle, as in the Aegaeon simile. Elision 'adversaqu(e) ingens'."""),
(583, 'terris.',
 """To him Liger:\n“Not Diomedes' horses nor the chariot you see of Achilles\nnor the plains of Phrygia: now of war the end and of life\non these lands will be given.”""",
 """Liger shouted at him, “These are not the horses of Diomedes you see, nor the chariot of Achilles, nor the plains of Phrygia: here, on this soil, you will meet the end of the war and of your life.”""",
 """The print has 'terris. ”Vesano', a misprint for 'terris.” Vesano', corrected here. As at 451 in the last part, the stray mark begins the next unit's text, and the speech is closed here in the English. Line 580 is a half-line, one of the many unfinished lines (more than fifty) left in the poem at Virgil's death, as 490 in the last part. 'Cui Liger', 'to him Liger (said)', the verb of speaking left out. Liger sneers at Aeneas's escapes at Troy: Diomedes wounded him and took his horses, and Poseidon carried him away from Achilles (Iliad 5.297–327, 20.288–340). 'belli finis et aevi', 'an end of war and of life'. No elisions."""),
(584, 'Ligeri.',
 """Mad, such words far and wide\nfly from Liger.""",
 """Such were the words that flew far and wide from Liger in his madness.""",
 """The closing speech mark printed at the head of this unit belongs to Liger's speech (see the note before). 'Vesano… Ligeri', 'from mad Liger', a dative of reference with 'volant', the adjective and the name framing the clause. 'vesanus', 'out of his mind', from the negative 've-' and 'sanus'. 'late… volant', 'fly far and wide', like Homer's winged words. The poet calls the boast madness before the answer comes. No elisions."""),
(585, 'hostem.',
 """But not likewise the Trojan hero\nwords prepares in reply: his javelin, for, he hurls at the enemy.""",
 """But the Trojan hero did not make ready words in answer: instead he hurled his javelin at his enemy.""",
 """'non et', 'not also', not in his turn. 'Troïus', printed by Greenough with the diaeresis: three syllables, Tro-i-us. 'dicta parat contra', 'prepares words in reply', 'contra' an adverb. 'iaculum nam torquet', 'for he hurls a javelin', with 'nam' put second in its clause, a poetic order. 'torquet', 'whirls, hurls'. The Latin Library has 'hostis', accusative plural, 'at the enemies', both brothers; Greenough's 'hostem' is singular, aimed at Lucagus. No elisions."""),
(589, 'inguen:',
 """Lucagus, as, leaning forward, bending to the blows, with his weapon\nhe prompted the pair, while, his foot thrust forward, the left,\nhe readies himself for the fight, goes in through the rims, the spear, the lowest,\nof his gleaming shield, then the left groin pierces:""",
 """As Lucagus, bent forward over the horses, was urging on the pair with his sword, his left foot planted forward to ready himself for the fight, the spear went in under the bottom rim of his shining shield and pierced his left groin:""",
 """'Lucagus ut', 'as Lucagus', the subject put before 'ut', with the perfect 'admonuit'. 'pronus pendens in verbera', 'leaning forward, hanging over to the blows', bent to lash the horses. 'telo', 'with his weapon': he has no whip and uses his sword. 'biiugos', 'the two-yoked (horses)', the team. 'proiecto… pede laevo', an ablative absolute, 'his left foot thrust forward', 'proiecto' with the consonantal 'i' after the prefix. 'dum… aptet', 'while he fits himself', the subjunctive giving his purpose. 'oras… per imas', 'through the lowest edges'. 'inguen', 'the groin'. No elisions."""),
(590, 'arvis.',
 """flung from the chariot, dying, he rolls on the fields.""",
 """hurled from the chariot, he rolled dying across the field.""",
 """'excussus curru', 'shaken out of the chariot', 'curru' an ablative of separation. 'moribundus', 'dying', an adjective in '-bundus' for an action under way. 'volvitur arvis', 'is rolled over the fields', the passive in a middle sense, 'rolls'; 'arvis' is an ablative of place without a preposition. No elisions."""),
(591, 'amaris:',
 """Him dutiful Aeneas with words addresses bitter:""",
 """Over him dutiful Aeneas spoke these bitter words:""",
 """'Quem', the connecting relative, 'him'. 'pius Aeneas', the hero's standing epithet: his duty to Pallas and Evander is what drives him now, and Virgil sets the word beside one of his harshest speeches. 'dictis… amaris', 'with bitter words', framing the verb. 'adfatur', Greenough's spelling of 'affatur', 'addresses'. No elisions."""),
(594, 'deseris.',
 """“Lucagus, no sluggish flight of horses your chariot\nbetrayed, nor did empty shadows turn it from the enemy:\nyou yourself, leaping from the wheels, the yoke desert.”""",
 """“Lucagus, it was no cowardly bolting of your horses that betrayed your chariot, no empty phantoms that turned it from the enemy: it is you who leap from the wheels and abandon the team.”""",
 """The print has 'deseris. ”Haec', a misprint for 'deseris.” Haec', corrected here. As at 583, the stray mark begins the next unit's text, and the speech is closed here in the English. Aeneas mocks with what happened to Niphaeus just before (572–574), whose horses bolted in fear. 'fuga segnis equorum', 'the cowardly flight of horses'. 'vanae… umbrae', 'empty shadows', phantoms that scare horses. 'vertere' = 'verterunt', with 'currus' understood as object. 'rotis saliens', 'leaping from the wheels', ablative of separation: a sneer, since Lucagus was struck down and fell. 'iuga deseris', 'you desert the yoke'. Elision 'verter(e) ex'."""),
(595, 'biiugos;',
 """These words thus having spoken,\nhe seized the pair;""",
 """With these words he laid hold of the horses;""",
 """The closing speech mark printed at the head of this unit belongs to Aeneas's speech (see the note before). 'Haec ita fatus', 'having spoken these words so', the closing formula. 'arripuit biiugos', 'snatched the pair', took hold of the team by the bridles, so that the chariot is stopped and Liger, the driver, is left helpless in it. No elisions."""),
(596, 'eodem:',
 """the brother was stretching out helpless\nhis palms, unhappy, from the chariot slipped down, the same:""",
 """his brother, poor wretch, slipping down from the same chariot, held out his helpless hands:""",
 """'frater', Liger, who was boasting a moment before. 'tendebat… palmas', 'was stretching out his palms', the suppliant's gesture; the imperfect sets the scene for what follows. 'inertis', accusative plural in '-is' with 'palmas', 'unarmed, helpless'. 'infelix', 'unlucky', with 'frater'. 'curru delapsus eodem', 'slid down from the same chariot', the one his brother had just been thrown from. No elisions."""),
(598, 'precantis.”',
 """“By yourself, by those who you such begot, your parents,\nman of Troy, allow this life, and pity one who prays.”""",
 """“By your own self, by the parents who made you the man you are, Trojan, let me keep this life, and take pity on one who begs you.”""",
 """'Per te, per qui te… parentes', 'by you, by the parents who (bore) you', the antecedent 'parentes' taken into the relative clause and put at its end. 'talem', 'such', so great a man: Liger flatters the man he mocked. 'genuere' = 'genuerunt'. 'vir Troiane', 'man of Troy', vocative. 'sine hanc animam', 'allow (me) this life', 'sine' the imperative of 'sino', 'allow'. 'miserere precantis', 'pity the one praying', 'misereor' with the genitive. Mago's plea opened in the same way, with 'per' (524). The speech ends. Elisions 'sin(e) hanc', 'anim(am) et'."""),
(600, 'dabas.',
 """To him pleading more, Aeneas: “Not such things a while ago\nas words were you giving.""",
 """He would have pleaded further, but Aeneas answered, “Those were not the words you were uttering a moment ago.""",
 """'Pluribus oranti', 'to him pleading with more (words)', a dative with the verb of speaking left out: Liger is still begging, or about to beg further, when Aeneas cuts him short. 'Haud talia… dicta dabas', 'you were not giving such words', 'dare dicta' a poetic phrase for speaking, the imperfect for what Liger kept saying. 'dudum', 'a little while ago', his taunt at 581–583. Elision 'orant(i) Aeneas'."""),
(600, 'frater.”',
 """Die, and your brother do not desert, a brother.”""",
 """Die, and do not be a brother who deserts his brother.”""",
 """'Morere', imperative of the deponent 'morior', 'die'. 'ne desere', 'do not desert', 'ne' with the imperative, an old and poetic prohibition (prose would say 'noli deserere'). 'fratrem… frater', the same word at either end of the clause: Aeneas turns a brother's loyalty into the reason for killing him, answering the taunt with the charge of desertion he made against Lucagus. The scorn is deliberate: grief for Pallas has driven Aeneas past mercy. Elision 'Morer(e) et'."""),
(601, 'recludit.',
 """Then the hiding-places of the life, the breast, with his point he opens.""",
 """Then with the point of his sword he laid open the breast, where the life lay hidden.""",
 """'latebras animae', 'the hiding-places of the life', in apposition to 'pectus': the life was thought to lodge in the chest. 'mucrone', 'with the point'. 'recludit', 'opens up', unlocks, the opposite of 'claudo', 'shut'. A single line, without comment, for the last death in this run of killings. No elisions."""),
(604, 'furens.',
 """Such deaths across the plains dealt the leader,\nthe Dardanian, of a torrent's water or of a black whirlwind\nin the manner raging.""",
 """Such were the deaths the Dardan leader dealt across the plain, raging like a flood of water or a black whirlwind.""",
 """'Talia… funera', 'such deaths', the poet sums up. 'edebat', 'was producing, dealing out', the imperfect for the continuing action. 'ductor Dardanius', 'the Dardanian leader', Aeneas. 'torrentis aquae vel turbinis atri more', 'in the manner of a torrent of water or of a black whirlwind', 'more', ablative of 'mos', with genitives, a common way of making a short comparison; 'torrentis' is genitive singular here, not an accusative plural. No elisions."""),
(605, 'iuventus.',
 """At last burst out and the camp leave\nAscanius the boy and the besieged-in-vain youth.""",
 """At last the boy Ascanius and the young men, besieged to no purpose, broke out and left the camp.""",
 """'Tandem', 'at last': the Trojan camp has been under siege by Turnus since Book IX, while Aeneas was away gathering allies. 'erumpunt… relinquunt', the verbs first, the subjects held to the last line. 'Ascanius puer', 'the boy Ascanius', Aeneas's son, also called Iulus (524, 534). 'nequiquam obsessa iuventus', 'the youth besieged in vain', a collective singular, the Trojan fighting men: the siege has failed. Elisions 'Tand(em) erumpunt', 'nequiqu(am) obsessa'."""),
]

# Misprints (rule 5b): 10.583 'terris. ”Vesano' and 10.594 'deseris. ”Haec' print the closing speech mark joined to the
# next word. t keeps the print; the unit ending at 'terris.' / 'deseris.' closes the speech in l and i; the stray ”
# begins the next unit's t, whose l and i carry no mark. Mark balance is checked over each pair, as in aeneid-077.
PAIRS = {580: 583, 592: 594}
P = A.part('aeneid-078'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
        if t.count(mk) != l.count(mk) and ln not in PAIRS and ln not in PAIRS.values(): print('MARK l', ln, mk)
        if mk in '“”' and t.count(mk) != i.count(mk) and ln not in PAIRS and ln not in PAIRS.values(): print('MARK i', ln, mk)
for a, b in PAIRS.items():
    pair = [s for s in sents if s['ln'] in (a, b)]
    if len(pair) != 2 or not pair[1]['t'].startswith('”'): print('PAIR SHAPE', a, [s['t'][:12] for s in pair])
    for mk in '“”':
        if sum(s['t'].count(mk) for s in pair) != sum(s['l'].count(mk) for s in pair): print('PAIR MARK l', a, mk)
        if sum(s['t'].count(mk) for s in pair) != sum(s['i'].count(mk) for s in pair): print('PAIR MARK i', a, mk)
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units')
