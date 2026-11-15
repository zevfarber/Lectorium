# aeneid-076 (X.362-438): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Pallantis virtus. Halaesus et Lausus'
PART = "Pallas Rallies the Arcadians (X.362–438)"
TITLE_EN = "Pallas Rallies the Arcadians — Aeneid X.362–438"
ABOUT = ("On another part of the field, where a mountain torrent has left the ground strewn with boulders and uprooted trees, "
"the Arcadian cavalry have had to leave their horses, and, unused to fighting on foot, they turn and run from the Latins. "
"Pallas, Evander's young son, shames and pleads with them: the enemy are mortal men like themselves, the sea is at their "
"backs, and the only road home runs through the thickest of the enemy. Then he leads the way and kills man after man: "
"Lagus as he wrenches up a rock, Hisbo who rushes him in fury, Anchemolus who had defiled his stepmother's bed, and the "
"twin sons of Daucus, whom even their parents could not tell apart until Pallas made them different. His men take heart "
"and close up behind him, as scattered fires a shepherd sets merge into one line of flame. On the Italian side Halaesus, "
"whose prophet father had once hidden him in the woods to cheat his fate, cuts down Pallas's men, until Pallas prays to "
"Father Tiber and kills him with a spear. Lausus, son of Mezentius, steadies the Italians, and the two armies lock together, "
"Pallas on one side, Lausus on the other, two young men of rare beauty, neither of whom will ever see home again. Jupiter "
"does not let them meet: each is to die at the hands of a greater enemy.")

U = [
(363, 'ripis,',
 """But on the other side, where boulders rolling far and wide\nhad driven a torrent, and trees torn from the banks,""",
 """But on another part of the field, where a torrent had sent boulders rolling far and wide, and trees torn from its banks,""",
 """A new paragraph in Greenough. 'At', 'but', turns the story from Aeneas's landing to another part of the battle. 'parte ex alia', 'from another side', the preposition placed between adjective and noun, as often in verse. 'qua', 'where'. 'saxa rotantia', 'rolling rocks'; 'impulerat torrens', 'a torrent had driven (them)', pluperfect: the flood has gone and left its wreckage. 'arbusta diruta ripis', 'trees torn from the banks', 'ripis' an ablative of separation. The Latin Library has 'intulerat', 'had carried in', to almost the same sense. Elision 'part(e) ex'."""),
(368, 'amaris:',
 """the Arcadians, unused to bringing on battle-lines on foot,\nwhen Pallas saw them give their backs to pursuing Latium\n(since the rugged nature of the place had persuaded them to let go\ntheir horses), the one thing that is left in needy straits,\nnow with prayer, now with words bitter he kindles their courage:""",
 """when Pallas saw his Arcadians, who were not used to fighting on foot, turning their backs to the pursuing Latins (the rough ground had made them leave their horses), he did the one thing left in such straits, and fired their courage, now with entreaty, now with bitter words:""",
 """Pallas, Evander's young son, was put in Aeneas's charge in Book VIII with Evander's Arcadian horsemen. 'Arcadas', Greek accusative plural. 'insuetos… inferre', 'unused to bringing on', with the infinitive; 'acies… pedestris', 'battle on foot', accusative plural in '-is'. 'ut vidit', 'when he saw', 'ut' with the perfect indicative. 'Latio… sequaci', 'to pursuing Latium', the land for its people; 'dare terga', 'to give their backs', to run. In the parenthesis 'quis' is the old dative plural of the relative (= 'quibus'), 'to whom', and 'quando' means 'since'. The Latin Library has 'aquis': 'the nature of the place, rough with water', with no relative. 'unum quod… restat', 'the one thing that remains', in apposition to what follows. Elision 'virtut(em) accendit'."""),
(369, 'socii?',
 """“Where are you fleeing, comrades?""",
 """“Where are you running, my comrades?""",
 """Pallas's speech begins with a rebuke. 'Quo', 'to where?', 'whither?'. 'socii', vocative. The whole speech is modelled on Ajax's appeal to the Greeks at the ships in the Iliad: is there a walled city behind us to fall back on? we are far from home with the sea at our backs; our safety lies in our hands (Iliad 15.733–741). No elisions."""),
(372, 'pedibus.',
 """By yourselves and your brave deeds,\nby your leader Evander's name and the wars he fought out,\nand my hope, which now rises to rival my father's glory,\ndo not trust your feet.""",
 """By yourselves and your brave deeds, by the name of your leader Evander and the wars he fought and won, by my own hope, which now rises to match my father's fame, do not trust to your feet.""",
 """The print has 'Opemque', a misprint for 'spemque', corrected here. 'Opem' cannot open a hexameter, since its first syllable is short ('ŏpis'), and Greenough capitalises only at a stop or for a name; 'spemque', which the Latin Library prints, scans. 'Per… per', 'by…', the form of earnest entreaty. 'devicta bella', 'wars fought to a finish', from 'devinco'. 'patriae… aemula laudi', 'rivalling my father's glory', 'patriae' the adjective 'paternal', 'laudi' dative with 'aemula'; 'subit', 'rises, comes up'. 'fidite ne pedibus' = 'ne fidite', a prohibition with 'ne' and the imperative, a poetic and old-fashioned turn (prose says 'nolite fidere'); 'pedibus' is dative with 'fido'. Trusting their feet means running away, a gibe at horsemen now on foot. No elisions."""),
(373, 'via.',
 """With steel must be burst through the enemy\nthe way.""",
 """Our road runs through the enemy, and it must be cut open with the sword.""",
 """'rumpenda est via', a gerundive of obligation: 'a way is to be burst open', 'a way must be broken'. 'ferro', ablative of means, 'with the sword'. 'per hostis', accusative plural in '-is'. The line break throws 'est via' to the head of the next line, short and emphatic. No elisions."""),
(374, 'reposcit.',
 """Where that mass of men, thickest, presses,\nthere you and Pallas your leader your lofty homeland demands back.""",
 """Where that knot of men presses thickest, that is the way our proud homeland calls you back, and Pallas your leader with you.""",
 """'Qua… hac', 'by which way… by this way'. 'globus', 'a ball', a dense knot of soldiers; 'densissimus', 'thickest'. 'virum' = 'virorum', the old genitive plural you have met often. 'Pallanta', Greek accusative of 'Pallas': he names himself, as their commander. 'patria alta', 'your lofty homeland', Evander's town Pallanteum on the Palatine hill, the future site of Rome (Book VIII). 'reposcit', 'demands back': the road home lies straight through the enemy. Elision 'patri(a) alta'."""),
(376, 'manusque.',
 """No divine powers press us; by a mortal we are pressed, by an enemy,\nmortals; as many to us are both lives and hands.""",
 """No gods bear down on us; we are mortals hard pressed by a mortal enemy, and we have as many lives and as many hands as they have.""",
 """'Numina', 'divine powers', gods. 'mortali… hoste mortales', one word set against itself across the line in two forms (polyptoton): mortals pressed by mortals. 'urgemur' picks up 'urget' in the line before. 'totidem nobis', 'we have as many', a dative of possession with 'sunt' understood; 'totidem', 'as many' as the enemy. '-que… -que', 'both… and'. In the Iliad Agenor steadies himself to face Achilles with the same thought: his flesh too can be pierced, he has one life, and men call him mortal (Iliad 21.568–570). Elision 'mortal(i) urgemur'."""),
(378, 'petemus?”',
 """Look, with a great barrier of sea the deep shuts us in;\nthere fails now land for flight: the open sea, or Troy, shall we make for?”""",
 """Look, the deep has shut us in behind with a great barrier of sea, and there is no more land to run across: are we to head for the open sea, or for Troy?”""",
 """'maris magna… obice', 'with a great bar of sea'; 'obex' is a bolt or barrier. The Arcadians have the coast behind them. 'deest', 'is lacking', its 'de-' and 'est' run together as one syllable (synizesis). 'fugae', dative, 'for flight'. 'pelagus Troiamne', a double question with '-ne' on the second word: 'the sea, or Troy?'. 'Troy' is probably the Trojans' camp, the new Troy which the enemy is blockading, though the old city across the sea fits the irony too: either way there is nowhere to run. The Latin Library has 'petamus', a deliberative subjunctive, 'are we to make for'; Greenough's future, 'shall we make for', is plainer. The speech ends. No elisions."""),
(379, 'hostis.',
 """This he says, and in their midst into the dense bursts the enemy.""",
 """So he spoke, and burst into the thick of the enemy.""",
 """'Haec ait', 'this he says', the regular formula that closes a speech. 'medius', an adjective where English uses a phrase: 'in the middle', 'into their midst'. 'densos… in hostis', 'into the packed enemy', 'hostis' accusative plural in '-is'. 'prorumpit', 'bursts forward'. He does at once what he urged, cutting his way where the enemy is thickest (373). No elisions."""),
(381, 'Lagus.',
 """In his way first, by the fates drawn on unjust,\nis Lagus.""",
 """The first to cross his path, drawn on by cruel fate, was Lagus.""",
 """'Obvius… fit', 'becomes in the way', meets him; 'huic', dative with 'obvius', is one syllable. 'fatis… iniquis', 'by unkind fates', ablative of cause. The name is held over to the next line and closes the sentence. Lagus, like most of the men killed in these battle-lists, is known only from this line: Virgil, like Homer, gives each victim a name. No elisions."""),
(384, 'haerentem.',
 """Him, while a rock of great weight he tears up,\nwith a whirled spear he pierces, where divisions to the ribs\nthrough the middle the spine was giving, and the spear he tugs back\nsticking in the bones.""",
 """As Lagus was wrenching up a heavy rock, Pallas hurled his spear and pierced him where the spine runs down the middle and parts the ribs, and dragged the spear back out from where it clung in the bones.""",
 """'Hunc', object of 'figit'. 'dum… vellit', 'while he is tearing up'; 'magno… pondere', ablative of quality, 'of great weight': Homer's heroes, too, often snatch up a stone to throw. 'intorto… telo', 'with a whirled spear', thrown with a twist. 'discrimina costis… dabat', 'gave divisions to the ribs', 'costis' dative: the spine runs between the ribs of either side, so Lagus, stooping, is struck in the back. 'receptat', a frequentative form of 'recipio', 'tugs back' with effort, since the point sticks 'ossibus haerentem', 'clinging in the bones'. No elisions."""),
(385, 'sperans:',
 """Him not standing over does Hisbo catch first,\nthough he indeed this was hoping:""",
 """Hisbo did not take Pallas by surprise as he stood over the body, though that was what he hoped:""",
 """'Quem', the connecting relative, Pallas (= 'et eum'). 'super', 'above', an adverb: Pallas standing over Lagus while he frees his spear. 'occupat', 'catches first', strikes before the other can act. 'ille quidem hoc sperans', 'he indeed hoping this': Hisbo meant to catch Pallas while his weapon was stuck. The colon introduces why he failed. Elision 'quid(em) hoc'."""),
(387, 'recondit.',
 """for Pallas, as he rushed on, first,\nwhile he raged, off his guard at the cruel death of his comrade,\ncatches and his sword in the swollen lung buries.""",
 """for Pallas was ready first: as Hisbo charged, raging and careless at his comrade's cruel death, Pallas met him and buried his sword in his swelling lung.""",
 """'ante', 'first', before Hisbo could strike. 'ruentem… incautum', 'rushing, off his guard', both describing Hisbo. 'dum furit', 'while he rages'. 'crudeli morte sodalis', 'at the cruel death of his comrade', ablative of cause: Hisbo was Lagus's friend. 'excipit', 'catches, meets', the word for a hunter taking a charging beast on his weapon. 'tumido… pulmone', 'the swelling lung', swollen with his fury and his panting. 'recondit', 'buries', 'hides away'. Elisions 'atqu(e) ensem', 'tumid(o) in'."""),
(389, 'novercae.',
 """Next Sthenius he attacks, and of Rhoetus from the race ancient\nAnchemolus, who dared the chamber to defile of his stepmother.""",
 """Next he went for Sthenius, and for Anchemolus, of the ancient line of Rhoetus, who had dared to defile his stepmother's bed.""",
 """'Hinc', 'next'. 'Rhoeti de gente vetusta', 'of the ancient race of Rhoetus'. The old commentators tell the story: Rhoetus, a king of the Marsi, took a second wife, his son Anchemolus seduced her, and he fled his father's anger to Daunus, Turnus's father, which is why he fights here for Turnus. 'thalamos', 'the bedchamber', the plural standing for the marriage bed. 'ausum', perfect participle of 'audeo', 'having dared'. 'incestare', 'to pollute, defile'. 'novercae', 'stepmother'. Elision 'aus(um) incestare'."""),
(392, 'error;',
 """You too, twins, on the Rutulian fell fields,\nDaucian Larides and Thymber, most alike offspring,\nnot told apart by your own and to your parents a welcome mistake;""",
 """You too fell on Rutulian fields, twin sons of Daucus, Larides and Thymber, so alike that your own family could not tell you apart, a confusion that delighted your parents;""",
 """The poet turns to address the twins (apostrophe), as he does with victims he pities. 'gemini', 'twins'. 'Daucia… proles', 'Daucian offspring', the sons of Daucus, an adjective from the father's name doing the work of a genitive. 'Laride', vocative of 'Larides'; 'Thymber', nominative standing for the vocative, as poets allow. 'simillima', 'most alike'. 'indiscreta suis', 'indistinguishable to their own people', 'suis' dative. 'gratus… parentibus error', 'a mistake pleasing to the parents', in apposition to the whole: the mix-ups were a family joke. Greenough's 'agris' is 'arvis' in the Latin Library, to the same sense. No elisions."""),
(393, 'Pallas:',
 """but now harsh gave to you distinctions Pallas:""",
 """but now Pallas gave you a cruel way to be told apart:""",
 """'dura… discrimina', 'harsh distinctions', framing the line: a grim play on the twins' likeness, since Pallas makes them different by the way he maims each of them. 'discrimina' was used at 382 of the parting of the ribs by the spine. 'dedit', perfect, 'gave'; 'vobis', dative. No elisions."""),
(394, 'ensis;',
 """for from you, Thymber, your head Evander's took off sword;""",
 """for Evander's sword struck off your head, Thymber;""",
 """'tibi', a dative of separation with 'abstulit', 'took away from you'. 'Thymbre', vocative. 'Evandrius… ensis', 'the Evandrian sword', Evander's own sword in his son's hand, the adjective from the name used as with 'Daucia proles' just before. 'caput', 'head'. No elisions."""),
(396, 'retractant.',
 """you, cut off, as its own, Larides, your right hand seeks,\nand half-alive twitch the fingers and the steel grasp again.""",
 """your severed right hand, Larides, seeks you as its master, and the half-alive fingers twitch and clutch again at the sword.""",
 """'te… suum', 'you, its own': the hand looks for its owner. 'decisa', 'cut off'. 'dextera', the fuller form of 'dextra'. 'semianimes', 'half-alive', four syllables, the 'i' of 'semi-' sounded as a consonant (y). 'micant', 'flicker, twitch'. 'retractant', 'handle again', the fingers still trying to grip the sword. Ennius had already written 'semianimesque micant oculi', 'and the half-alive eyes twitch', of a severed head (Annals, quoted by the ancient commentators); Virgil reuses his line-opening. No elisions."""),
(398, 'hostis.',
 """The Arcadians, fired by the warning and watching the glorious\ndeeds of the man, mingled grief and shame arm against the enemy.""",
 """The Arcadians were fired by his rebuke and by the sight of his glorious deeds, and grief and shame together armed them against the enemy.""",
 """'Arcadas', Greek accusative plural, object of 'armat'. 'accensos monitu', 'kindled by his warning', the speech at 369–378. 'tuentis', accusative plural in '-is', agreeing with 'Arcadas': 'as they watch'. 'praeclara… facta viri', 'the man's glorious deeds', split across the line. 'mixtus dolor et pudor', 'grief and shame mixed', two subjects felt as one, with a singular adjective and verb. 'in hostis', 'against the enemy'. Elision 'monit(u) et'."""),
(400, 'traicit.',
 """Then Pallas, as on his two-horse car fleeing Rhoeteus went past,\npierces him through.""",
 """Then, as Rhoeteus fled past in his two-horse chariot, Pallas ran him through.""",
 """'biiugis', ablative of 'biiugi', 'a pair-horse chariot' (from 'bis' and 'iugum'), three syllables, the second 'i' a consonant. 'fugientem Rhoetea', 'Rhoeteus as he flees', 'Rhoetea' a Greek accusative. 'praeter', an adverb, 'past', ending the line. 'traicit' (= 'transicit', from 'trans' and 'iacio'), 'pierces through', held to the next line and stopped short. No elisions."""),
(400, 'Ilo;',
 """This space and so much of delay there was to Ilus;""",
 """That was all the respite and delay that Ilus won;""",
 """'Hoc spatium tantumque morae', 'this interval and so much of delay', 'morae' a partitive genitive with 'tantum'. 'Ilo', dative of possession: Ilus had only this much respite. The next lines explain: the spear that killed Rhoeteus had been meant for Ilus, who lived only because Rhoeteus got in its way, and only for a moment. No elisions."""),
(404, 'arva.',
 """For at Ilus from afar his strong he had aimed spear,\nwhich, coming between, Rhoeteus intercepts, noblest Teuthras,\nyou fleeing and your brother Tyres, and from the chariot rolled\nbeats, half-alive, with his heels the Rutulians' fields.""",
 """For Pallas had aimed his strong spear at Ilus from a distance, and Rhoeteus, coming between, caught it as he fled from you, noble Teuthras, and from your brother Tyres; rolled from his chariot, he drummed his heels, half-dead, on the Rutulians' fields.""",
 """'Ilo', dative of direction, 'at Ilus'. 'direxerat', pluperfect: the spear was already in the air (the Latin Library spells it 'derexerat'). 'medius… intercipit', 'in between, he intercepts'. 'optime Teuthra', vocative: the poet turns to address an Arcadian, from whom, with his brother 'Tyren' (Greek accusative of 'Tyres'), Rhoeteus was fleeing. 'Rhoeteus' has 'eu' as one syllable. 'curru volutus', 'rolled from the chariot', 'curru' ablative of separation. 'caedit… calcibus arva', 'strikes the ground with his heels', his death-throes; 'semianimis' as at 396. 'Rutulorum… arva', the Rutulians' own soil. No elisions."""),
(409, 'ovantis:',
 """And as, at his wish, the winds in summer having risen,\nscattered fires into the woods sends a shepherd,\nthe parts between suddenly seized, there spreads out, one,\nbristling over the broad plains, the battle-line of Vulcan;\nhe, sitting as victor, looks down on the flames exulting:""",
 """And as in summer, when the winds he hoped for have risen, a shepherd sets fires at scattered points in the woods, and suddenly the gaps between catch, and a single bristling line of fire stretches across the wide plains, while he sits looking down like a victor on the exulting flames:""",
 """The simile. 'optato', ablative used as an adverb, 'as he wished'; 'ventis… coortis', ablative absolute, 'the winds having risen'. 'dispersa… incendia', 'scattered fires', set at several points; 'immittit silvis', 'sends into the woods', dative with a compound verb. Shepherds burned off scrub to bring up fresh pasture. 'correptis… mediis', ablative absolute, 'the spaces between being caught'. 'acies Volcania', 'Vulcan's battle-line', the fire-front pictured as an army, the god's name standing for fire. 'ovantis', accusative plural in '-is', 'exulting', as soldiers cheer at a triumph. The scattered fires that join in one line are Pallas's men, rallied. Homer likens a hero's onslaught to fire racing through a wood (Iliad 11.155–157; 20.490–492). Elision 'dispers(a) immittit'."""),
(411, 'Palla.',
 """not otherwise of your comrades the valour comes together, all, into one\nand helps you, Pallas.""",
 """just so the courage of all your comrades gathered into one and came to your aid, Pallas.""",
 """'non aliter', 'not otherwise', closes the simile. 'socium' = 'sociorum', the old genitive plural. 'coit… in unum', 'comes together into one', as the scattered fires merged into a single front. 'omnis', nominative singular with 'virtus', 'all the valour'. 'Palla', Greek vocative of 'Pallas': the poet turns to address him, as he addresses those he pities, a quiet hint of what is coming. No elisions."""),
(412, 'arma.',
 """But in wars keen Halaesus\nheads against those facing him, and himself into his own gathers armour.""",
 """But Halaesus, fierce in war, pressed forward against them, gathering himself behind his shield.""",
 """Halaesus was introduced at 352 in the last part; in the catalogue of Book VII he is a follower of Agamemnon's line who settled in Italy. 'bellis acer', 'keen in wars', ablative of respect. 'tendit in adversos', 'makes for those facing him'. 'se… in sua conligit arma', 'gathers himself into his arms', crouches behind his shield ready to strike; 'conligit' is Greenough's spelling of 'colligit', which the Latin Library prints. Elision 'sequ(e) in'."""),
(416, 'cruento.',
 """He slaughters Ladon and Pheres and Demodocus;\nfrom Strymonius the right hand with flashing he tears sword,\nraised against his throat; with a stone he strikes the face of Thoas,\nand the bones scattered, mingled with brain bloody.""",
 """He slew Ladon, Pheres and Demodocus; with his flashing sword he lopped off the right hand of Strymonius as it was raised against his throat; he struck Thoas in the face with a stone and scattered his bones, mixed with blood and brains.""",
 """'Hic', 'he', Halaesus. 'mactat', 'slaughters', properly a word of sacrifice. 'Ladona', 'Phereta', Greek accusatives; '-que… -que' joins the three names. 'Strymonio', dative of separation, 'from Strymonius'. 'deripit', 'tears away'. 'elatam in iugulum', 'raised against the throat', Halaesus's throat: Strymonius was about to strike. 'ora', 'face', plural for singular. 'dispersit', a perfect among presents, the instant result. 'cerebro… cruento', 'with bloody brain', ablative with 'permixta'. Several names are Homeric: Thoas, and Demodocus, the Phaeacian bard of the Odyssey. Elision 'elat(am) in'."""),
(417, 'Halaesum:',
 """Singing the fates, in the woods his father had hidden Halaesus:""",
 """His father, who could foretell the fates, had hidden Halaesus away in the woods;""",
 """'Fata canens', 'singing the fates', prophesying: his father was a seer who foresaw that the boy would die in war. 'silvis', ablative of place, 'in the woods'. 'celarat' = 'celaverat', the shortened pluperfect. Homer's seer Merops of Percote likewise tried to keep his two sons from the war, and they went and died (Iliad 2.831–834; 11.329–332). No elisions."""),
(420, 'Evandri.',
 """when the old man in death his whitening eyes released,\nlaid hand on him the Fates, and to the weapons devoted him\nof Evander.""",
 """but when the old man's eyes, grown white with age, were closed in death, the Fates laid their hand on Halaesus and devoted him to the weapons of Evander.""",
 """'ut', 'when', with the perfect. 'senior', 'the old man'. 'leto', ablative, 'in death'. 'canentia lumina', 'whitening eyes', from 'caneo', 'to be grey or white': dim with age, a play on 'canens', 'singing', in the line before. 'solvit', 'released'. 'iniecere' = 'iniecerunt', with consonantal 'i' after the prefix. 'manum inicere', 'to lay a hand on', a Roman legal phrase for seizing what one claims as one's own. 'Parcae', the Fates. 'sacrarunt' = 'sacraverunt', 'consecrated', marked him as a victim. 'Evandri' is held to the next line: the weapons are those of Evander's son. No elisions."""),
(420, 'precatus:',
 """Him thus Pallas attacks, having first prayed:""",
 """Before he attacked him, Pallas prayed in these words:""",
 """'Quem', connecting relative, 'and him' (= 'et eum'), Halaesus. 'petit', 'attacks', 'aims at'. 'ante precatus', 'having first prayed', the perfect participle of the deponent 'precor' with 'ante' as an adverb. 'sic', 'thus', points to the prayer that follows. No elisions."""),
(422, 'Halaesi.',
 """“Grant now, father Tiber, to the steel which, to throw, I poise,\nfortune and a way through the breast of hard Halaesus.""",
 """“Grant now, Father Tiber, to the steel I balance for the throw, good fortune and a path through the breast of hard Halaesus.""",
 """Pallas prays to the river Tiber, god of the land, on whose bank Evander's town stands; Tiberinus appeared to Aeneas in Book VIII. 'Thybri', vocative of 'Thybris', the Greek-style form of the river's name. 'ferro', dative, 'to the steel', the spear's point. 'quod missile libro', 'which I poise as a missile', 'libro' to balance a weapon before throwing it, 'missile' predicative. 'fortunam atque viam', 'success and a passage'. 'duri', 'hard', unyielding. Elision 'fortun(am) atque'."""),
(423, 'habebit.”',
 """These arms and spoils of the man your oak will have.”""",
 """Your oak shall bear the arms and spoils of the man.”""",
 """The vow: if the god grants success, Pallas will hang Halaesus's armour on an oak by the river, sacred to the god, as victors dedicated spoils on a tree as a trophy. 'exuviae', 'spoils', what is stripped from the body. 'tua quercus', 'your oak', the tree on the Tiber's bank. The thought of spoils is ironic: later in this book Turnus will strip the sword-belt from Pallas's own body. Elision 'arm(a) exuviasque'. The speech ends."""),
(424, 'deus:',
 """Heard those words the god:""",
 """The god heard his prayer:""",
 """'Audiit' = 'audivit', the perfect with its 'v' dropped. 'illa', 'those things', the words of the prayer, neuter plural. 'deus', the Tiber. The answer comes at once, in the half-line before the colon; not every prayer in the poem is granted, and Pallas's next one, to Hercules, will not be. No elisions."""),
(425, 'inermum.',
 """while he shields Imaon, Halaesus\nto the Arcadian, ill-starred, spear gives his breast unprotected.""",
 """for while Halaesus was covering Imaon, the luckless man laid his unguarded breast open to the Arcadian spear.""",
 """'dum texit', 'while he shields', present of 'tego'. 'Imaona', Greek accusative of 'Imaon', one of his comrades. 'Arcadio… telo', 'to the Arcadian spear', Pallas's, dative. 'infelix', 'ill-starred'. 'inermum', 'unarmed, unprotected', a by-form of 'inermis'. In shielding a friend Halaesus exposes himself, and the fate laid on him at 419 is fulfilled. Elisions 'Imaon(a) Halaesus', 'Arcadi(o) infelix'."""),
(427, 'agmina:',
 """But not, by the slaughter of so great a man, terrified does Lausus,\na huge part of the war, suffer the columns to be:""",
 """But Lausus, a mighty part of the war himself, would not let the ranks lose heart at the death of so great a man:""",
 """Lausus is the son of the Etruscan exile Mezentius, Turnus's ally; in the catalogue of Book VII he is second in beauty only to Turnus. 'perterrita… sinit agmina', 'does not let the columns (be) terrified', the participle predicative with 'sinit'; 'non' goes with 'sinit'. 'caede viri tanta', 'by the slaughter of so great a man', ablative of cause, Halaesus's death. 'pars ingens belli', 'a huge part of the war', in apposition: a mainstay of his side. No elisions."""),
(428, 'moramque.',
 """first Abas,\nset against him, he kills, of the fight both the knot and the stay.""",
 """First he killed Abas, who stood in his way, the knot on which the fighting had snagged and stood still.""",
 """'primus', 'first', an adjective where English uses an adverb. 'Abantem', accusative of 'Abas', an Etruscan captain from the catalogue of Aeneas's allies earlier in this book. 'oppositum', 'set against him'. 'interimit', 'kills'. 'pugnae nodumque moramque', 'both knot and delay of the fight', in apposition: Abas was the point where the battle was tied up and held back, the man the enemy could not get past. '-que… -que'. Elision 'opposit(um) interimit'."""),
(430, 'Teucri.',
 """Laid low is Arcadia's offspring, laid low the Etruscans,\nand you, O by the Greeks undestroyed bodies, Teucrians.""",
 """Down go the sons of Arcadia, down go the Etruscans, and you too, Trojans, whose bodies the Greeks could not destroy.""",
 """'Sternitur… sternuntur', the same verb opening each clause (anaphora), singular with 'proles', plural with 'Etrusci'. 'Arcadiae proles', 'the offspring of Arcadia', Pallas's men. 'Etrusci', Tarchon's allies. Then the poet addresses the Trojans themselves. 'Grais imperdita corpora', 'bodies not destroyed by the Greeks', 'Grais' a dative of agent with the participle; 'imperdita' appears to be Virgil's own coinage. They survived the sack of Troy only to die here. 'Teucri', 'Teucrians', with 'eu' one syllable. No elisions."""),
(431, 'aequis.',
 """The columns clash, with leaders and strength equal.""",
 """The armies came together, matched in their leaders and in their strength.""",
 """'concurrunt', 'run together', the word for armies meeting. 'ducibus… et viribus aequis', ablative of manner, 'with leaders and strength equal', 'aequis' going with both nouns. The leaders who balance each other are Pallas and Lausus, as the next lines show. Elision 'ducibusqu(e) et'."""),
(433, 'sinit.',
 """The rearmost pack the lines tight, nor does the crowd to be moved\nweapons and hands allow.""",
 """The rear ranks press the lines together, and the crush is too thick for anyone to move a weapon or a hand.""",
 """'Extremi', 'the hindmost', the rear ranks pushing forward. 'addensent', 'make thick', a rare verb, from 'addenseo'. 'acies', accusative plural, 'the lines'. 'turba', 'the crush', subject of 'sinit'. 'tela manusque moveri', 'weapons and hands to be moved', accusative and infinitive after 'sinit', with 'nec' going with the verb. Compare the press at the close of the last part, foot against foot (361). Elision 'Extrem(i) addensent'."""),
(434, 'aetas:',
 """On this side Pallas presses and drives on,\non that side, facing him, Lausus, nor much differs their age:""",
 """On one side Pallas pushes forward and drives on, on the other Lausus stands against him, and there is little difference in their years:""",
 """'Hinc… hinc', 'on this side… on that side'. 'instat et urget', two nearly synonymous verbs for steady pressure, understood again with 'Lausus'. 'contra', 'facing', 'opposite'. 'nec multum discrepat aetas', 'nor does their age differ much': both are young men, and both are sons fighting in the sight of armies led by or allied with their fathers. No elisions."""),
(436, 'reditus.',
 """outstanding in beauty, but to whom Fortune had denied\ninto their homeland returns.""",
 """both of outstanding beauty, but Fortune had denied them any return to their homeland.""",
 """'egregii forma', 'outstanding in form', ablative of respect, 'egregii' nominative plural. 'quis' = 'quibus', the old dative plural of the relative, as at 366: 'to whom'. 'Fortuna', capitalised as the goddess. 'negarat' = 'negaverat', the shortened pluperfect. 'reditus', accusative plural, 'returns', one for each. The poet tells us their deaths before they happen: both will fall in this book. No elisions."""),
(437, 'Olympi:',
 """Them to clash, however, did not allow\nwith each other the ruler of great Olympus:""",
 """Yet the ruler of great Olympus did not let the two of them meet each other in combat:""",
 """'Ipsos', 'the two themselves', set first for emphasis. 'concurrere passus haud', 'did not allow to clash', 'passus' (est) from the deponent 'patior', with the accusative and infinitive. 'tamen', 'however'. 'inter se', 'with each other'. 'magni regnator Olympi', 'the ruler of great Olympus', Jupiter, held back to the end of the line. No elisions."""),
(438, 'hoste.',
 """soon them their own fates await under a greater enemy.""",
 """soon each of them was to meet his own death at the hands of a greater enemy.""",
 """'mox', 'soon'. 'sua fata', 'their own fates', each his own. 'manent', 'await'. 'maiore sub hoste', 'under a greater foe', 'sub' with the ablative, at his hands: Pallas will die by Turnus, and Lausus by Aeneas, later in this book. The part ends on that forecast. No elisions."""),
]

# Misprint (rule 5b): 10.371 'Opemque' for 'spemque' is a wrong word, not a displaced mark; t keeps the print,
# l/i read 'spemque', the note of unit 369-372 opens with the rule-5b sentence. No pair handling needed.
PAIRS = {}
P = A.part('aeneid-076'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
