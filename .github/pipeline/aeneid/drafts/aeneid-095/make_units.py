# aeneid-095 (XII.441-553): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Aeneas in proelium redit'
PART = "Aeneas Returns to the Battle (XII.441–553)"
TITLE_EN = "Aeneas Returns to the Battle — Aeneid XII.441–553"
ABOUT = ("Healed, Aeneas marches out of the camp with Antheus, Mnestheus and the whole army behind him, and the Italians shudder as the column bears down on them like a storm-cloud coming in from the sea. "
"The Trojans cut down the first of the enemy, among them the augur Tolumnius, who threw the spear that broke the truce, and the Rutulians run. "
"Aeneas will fight no one but Turnus and hunts for him alone through the dust; but Juturna, Turnus's sister, throws his charioteer Metiscus from the chariot, takes his shape, and drives her brother this way and that across the field like a swallow darting through a great house, never letting him come to grips. "
"When Messapus's spear strikes the crest from Aeneas's helmet, his patience breaks: calling Jupiter and the altars of the broken treaty to witness, he gives his anger free rein. "
"The poet asks what god could tell the slaughter that follows, and why Jupiter willed such a clash between peoples destined for lasting peace. "
"Aeneas and Turnus sweep through the battle like fires in a dry wood or torrents off the mountains, each killing in turn, Turnus hanging the heads of two brothers from his chariot, until every contingent on both sides is drawn into one vast struggle. "
"The Homeric pattern is plain throughout: lists of single kills, the poet's appeal for help to tell them, and his address to the fallen.")

U = [
(442, 'quatiens;',
 "These words when he had given, through the gates he bore himself out, huge,\na monstrous spear in his hand shaking;",
 "With these words he strode out through the gates, a towering figure, brandishing a huge spear;",
 "A new paragraph in Greenough: Aeneas, healed, goes out to battle. 'Haec ubi dicta dedit', 'when he had given these words', the regular formula for the end of a speech. 'portis', ablative of the way by which, 'through the gates'. 'sese extulit', 'carried himself out', a grander 'went out'. 'ingens', 'huge', of the hero's stature, the adjective with the force of an adverb: he looms. 'telum immane', 'a monstrous weapon'. 'quatiens', 'shaking', brandishing. Elisions 'ses(e) extulit', 'tel(um) immane'."),
(444, 'castris:',
 "at once, in a dense column,\nboth Antheus and Mnestheus rush, and the whole, the camp left behind,\nthrong streams out:",
 "with him, in a close-packed column, Antheus and Mnestheus rush out, and the whole host leaves the camp and streams after them:",
 "'simul', 'at the same time', with him. 'agmine denso', 'in a dense column', ablative of manner. 'Antheusque Mnestheusque', 'both Antheus and Mnestheus', the double '-que'; in both names 'eu' is a Greek diphthong, one syllable, An-theus, Mnes-theus. Mnestheus is the Trojan captain who raced in the boat contest of Book V. 'omnis… turba', 'the whole crowd', 'omnis' nominative singular; 'relictis… castris', ablative absolute, 'the camp left behind', split across the line. 'fluit', 'flows', a crowd moving like water. No elisions."),
(445, 'tellus.',
 "then with blinding dust the plain\nis churned, and with the beat of feet trembles the roused earth.",
 "then the plain is lost in a blinding cloud of dust, and the ground, roused by the tramp of feet, quakes.",
 "'caeco pulvere', 'with blind dust', dust that blinds, the active sense of 'caecus'. 'miscetur', 'is mixed up, thrown into turmoil'. 'pulsu pedum', 'with the beat of feet', the phrase used of Mars's horses at 334–335. 'tremit excita tellus', 'the roused earth trembles', 'excita' from 'excio', 'stir up'; the subject is held to the end of the line. No elisions."),
(448, 'tremor:',
 "Saw them from the facing rampart coming Turnus,\nsaw them the Ausonians, and cold through the deepest ran\nbones a trembling:",
 "Turnus saw them coming from the rampart opposite, the Ausonians saw them, and a cold shudder ran through to the marrow of their bones:",
 "'Vidit… videre', 'saw… saw', the verb repeated at the head of two lines; 'videre' = 'viderunt'. 'ab adverso… aggere', 'from the opposite mound', the Trojan rampart facing them. 'venientis', Greenough's -is accusative plural, '(them) coming'. 'Ausonii', the Italians, from Ausonia, a poetic name for Italy. 'gelidus… tremor', 'a cold trembling', framing two lines; 'per ima… ossa', 'through the lowest bones', to the marrow: fear felt as cold, a Homeric turn. Elision 'vider(e) Ausonii'."),
(449, 'refugit.',
 "first, before all the Latins, Juturna\nheard and knew the sound, and, struck with trembling, shrank back.",
 "Juturna, before any of the Latins, heard the sound and knew it, and shrank back in terror.",
 "'prima ante omnis… Latinos', 'first before all the Latins', 'omnis' the -is accusative plural. Juturna is Turnus's sister, a nymph of springs to whom Jupiter gave immortality, as told earlier in this book; Juno has set her to save her brother. 'Iuturna', the I consonantal, Yu-tur-na. 'audiit', the uncontracted perfect of 'audio'; 'adgnovit', Greenough's spelling of 'agnovit'. 'sonum', the noise of the advancing Trojans, and with it the news that Aeneas is back. 'tremefacta', 'made to tremble'. 'refugit', 'fled back, recoiled'. Elisions 'prim(a) ante', 'ant(e) omnis', 'son(um) et'."),
(450, 'aperto.',
 "He flies, and over the open plain sweeps on his black column.",
 "Aeneas flies on, sweeping his dark column across the open plain.",
 "'Ille', Aeneas. 'volat', 'flies', of speed. 'campo… aperto', 'over the open plain', ablative of the way, framing the rest of the line. 'atrum… agmen', 'the black column', dark with armour and dust. 'rapit', 'snatches, sweeps along', the leader carrying his men with him. Elision 'campoqu(e) atrum'."),
(452, 'medium;',
 "As when towards the lands, the sky breaking, a storm-cloud\ngoes across the middle of the sea;",
 "As when a storm-cloud, the weather bursting, moves landward across the open sea;",
 "A simile, 'Qualis… talis' (456): Aeneas's army is like a storm-cloud coming in from the sea. 'Qualis ubi', 'such as when'. 'ad terras', 'towards the lands'. 'abrupto sidere', ablative absolute, 'the sky broken', 'sidus' here meaning weather or season, as often: the storm bursts. 'nimbus', 'a rain-cloud, storm-cloud'. 'it mare per medium', 'goes through the middle of the sea', the preposition set after its first word. The model, from memory, is the goatherd in Iliad IV who sees a black cloud coming over the sea and drives his flock into a cave. Elision 'ub(i) ad'."),
(454, 'late;',
 "for the wretched, alas, foreknowing far off,\nshudder the hearts of the farmers; it will bring downfall\nto the trees and havoc to the crops, it will overthrow all things far and wide;",
 "far off the hearts of the poor farmers, alas, know what is coming and shudder: it will bring the trees crashing down, lay the crops flat, and wreck everything far and wide;",
 "'miseris… agricolis', 'for the wretched farmers', a dative of reference going with 'corda', 'the hearts of the farmers', framing the clause. 'heu', the poet's own sigh. 'praescia longe', 'foreknowing from afar'. 'horrescunt', 'begin to shudder', an inceptive. 'dabit ille ruinas', 'it will give ruins', 'ille' the cloud; the futures give the farmers' own fears. 'stragem… satis', 'havoc to the sown crops', 'satis' from 'sata', 'things sown'. 'ruet omnia late', 'it will overthrow everything far and wide', 'ruo' here transitive. Elision 'cord(a) agricolis'."),
(455, 'venti:',
 "ahead fly, and the sound carry to the shores, the winds:",
 "the winds fly before it and carry its roar to the shore:",
 "'ante volant', 'fly ahead', the winds that run before a squall. 'sonitum… ferunt ad litora', 'carry the sound to the shores', so that the storm is heard before it arrives, as the Trojan advance was heard at 449. 'venti', the subject, held to the end. No elisions."),
(458, 'adglomerant.',
 "such, against the facing foes, the Rhoetean leader\nhis column drives; densely, in wedges closed, each one himself\nthey mass together.",
 "Just so the Trojan captain drives his column against the enemy before him, and each man packs close into the wedge-shaped ranks, massing together.",
 "'talis', answering 'Qualis' in 451. 'in adversos… hostis', 'against the enemies opposite', -is accusative plural. 'ductor Rhoeteius', 'the Rhoetean leader', Aeneas, from Rhoeteum, a headland near Troy, so simply 'Trojan'. 'agmen agit', 'drives the column'. 'densi… se quisque… adglomerant', 'packed close, each one, they mass themselves together', 'quisque' in apposition to a plural verb, the sense running from 'each' to 'all'. 'cuneis… coactis', 'with wedges formed', ablative absolute; a 'cuneus' is a wedge-shaped column for breaking a line. 'adglomerant', Greenough's spelling of 'agglomerant'. No elisions."),
(460, 'Gyas;',
 "Thymbraeus with his sword strikes heavy Osiris,\nMnestheus Archetius, Achates cuts down Epulo,\nand Gyas Ufens;",
 "Thymbraeus strikes down the massive Osiris with his sword, Mnestheus kills Archetius, Achates cuts down Epulo, and Gyas Ufens;",
 "A catalogue of single kills in the Homeric manner, each Trojan with his man. 'Ferit ense', 'strikes with the sword'. 'gravem… Osirim', 'heavy Osiris', the Greek accusative in -im, a Rutulian with an Egyptian god's name. 'Archetium', the verb carried over from 'ferit'. 'obtruncat', 'cuts down'. Achates is Aeneas's faithful companion, Gyas a captain from the boat race of Book V; Ufens led the Aequi in the catalogue of Book VII. 'Mnestheus', the eu one syllable again. Elision 'Epulon(em) obtruncat'."),
(461, 'hostis.',
 "falls the very man, Tolumnius the augur,\nthe first who against the facing foes his spear had hurled.",
 "Tolumnius the augur himself falls, the man who had been the first to hurl a spear at the enemy facing him.",
 "'cadit ipse', 'falls himself', 'ipse' marking him out: Tolumnius is the augur who read a false omen earlier in this book and threw the first spear, breaking the truce. 'primus… qui torserat', 'who had been the first to hurl', the relative held back. 'in adversos… hostis', -is accusative, framing the line as at 456. 'torserat', pluperfect of 'torqueo', 'twist, whirl, hurl'. The breaker of the treaty is the first to pay. No elisions."),
(463, 'agros.',
 "Is raised to the sky a shout, and, turned in their turn,\nin dusty flight the Rutulians give their backs across the fields.",
 "A shout rises to the sky, and now it is the Rutulians who turn and run, showing their backs across the fields in a cloud of dust.",
 "'Tollitur in caelum clamor', 'a shout is raised to heaven', a formula of battle. 'versi… vicissim', 'turned in their turn': before, the Trojans had fled from Turnus; now the Rutulians run. 'pulverulenta fuga', 'in dusty flight', ablative of manner. 'dant terga', 'give their backs', turn and flee, a stock phrase. 'Rutuli', Turnus's people. No elisions."),
(466, 'insequitur:',
 "He himself neither the turned-away deigns to lay low for Death\nnor those meeting him on equal foot nor those bearing weapons\ndoes he pursue:",
 "Aeneas himself does not stoop to lay low the men who turn and run, nor does he go after those who stand to meet him on equal terms or who carry spears against him:",
 "'Ipse', Aeneas, intent on one man. 'neque… nec… nec', 'neither… nor… nor'. 'aversos', 'turned away', those running. 'dignatur sternere Morti', 'deigns to lay low for Death', 'Morti' a dative, Death as a person, as 'Leto' at 328. 'pede… aequo', 'on equal foot', on level terms, hand to hand; 'congressos', 'those who have engaged'. 'tela ferentis', 'those bearing weapons', -is accusative. 'insequitur', 'pursues', placed late to govern the last two. Elision 'nequ(e) aversos'."),
(467, 'poscit.',
 "Turnus alone in the dense murk\nhe tracks, scanning; him alone to combat he demands.",
 "Turnus alone he searches for through the thick gloom, scanning every side; Turnus alone he challenges to fight.",
 "'solum… solum', 'him alone… him alone', the repetition marking a single purpose: the treaty made the war a duel. 'densa in caligine', 'in the thick murk', the dust of battle, the preposition between adjective and noun. 'vestigat', 'tracks', a hunting word. 'lustrans', 'scanning, surveying'. 'in certamina poscit', 'calls to combat', the plural for the single duel. Elisions 'dens(a) in', 'sol(um) in'."),
(470, 'relinquit:',
 "By this, shaken with fear in her mind, Juturna the warrior-maid\nthe charioteer of Turnus, from amid the reins, Metiscus,\nshakes out, and far off, slipped from the pole, leaves him:",
 "Shaken to the heart by this fear, Juturna, the warrior maid, tips Turnus's charioteer Metiscus out from among the reins and leaves him lying far behind, fallen from the chariot-pole:",
 "'Hoc… metu', 'by this fear', of the duel. 'concussa… mentem', 'shaken in mind', 'mentem' an accusative of the part affected. 'virago', 'warrior-maid', a woman of a man's spirit. 'aurigam Turni… Metiscum', framing the line, 'Turnus's charioteer Metiscus'. 'media inter lora', 'from the midst of the reins'. 'excutit', 'shakes out, throws'. 'lapsum temone', 'slipped from the pole', the shaft between the horses. The model is Athena thrusting Sthenelus out of Diomedes' chariot and taking the reins herself in Iliad V. Elision 'medi(a) inter'."),
(472, 'Metisci.',
 "she herself takes his place, and with her hands the rippling guides reins,\nall things wearing, both the voice and body and arms of Metiscus.",
 "She takes his place herself and guides the rippling reins with her own hands, assuming everything of Metiscus, his voice, his body and his armour.",
 "'ipsa subit', 'she herself goes under', steps into his place. 'undantis… habenas', 'the waving reins', -is accusative, rippling as they run loose. 'flectit', 'bends, steers'. 'cuncta gerens', 'wearing everything', explained by 'vocemque et corpus et arma', 'both voice and body and armour', '-que… et… et' in a run of three: a god's disguise is complete. Elisions 'manibusqu(e) undantis', 'vocemqu(e) et'."),
(475, 'escas,',
 "Black, as when through a rich master's great house\nflits, and on wings the lofty halls ranges, a swallow,\nscraps of food gathering and for her chattering nests morsels,",
 "As when a black swallow flits through the great house of some wealthy lord and wings her way round the lofty halls, gathering tiny scraps and food for her chattering nestlings,",
 "A second simile, closed by 'similis' at 477: Juturna darting about in the chariot is like a swallow. 'Nigra… hirundo', 'a black swallow', framing two lines. 'velut… cum', 'as when'. 'domini… divitis aedes', 'the house of a rich master'. 'pervolat', 'flies through'. 'pennis', 'with wings'. 'alta atria', 'high halls', the atrium of a great Roman house, open to the sky in the middle. 'pabula parva legens', 'gathering small food'. 'nidis… loquacibus', 'for the chattering nests', the nest put for the young in it. The simile is Virgil's own, small and domestic against the din of battle. Elision 'alt(a) atria'."),
(477, 'sonat:',
 "and now in the empty colonnades, now round the damp\npools it sounds:",
 "and her cry rings now in the empty colonnades, now round the standing pools:",
 "'nunc… nunc', 'now… now', the bird darting from place to place. 'porticibus vacuis', 'in the empty colonnades', ablative of place. 'umida circum stagna', 'round the wet pools', the preposition set after its first word; perhaps the rain-pool in the open middle of the atrium. 'sonat', 'sounds', with her twittering. No elisions."),
(480, 'longe.',
 "like her, through the midst of the enemy Juturna\nis borne by the horses, and flying in the swift chariot goes round everything,\nand now here her brother, and now here, she displays, exulting,\nand to join hands does not allow; she flies off the track, far.",
 "just so Juturna is carried by the horses through the thick of the enemy, flying everywhere in the swift chariot; now here, now there she shows her brother in triumph, but never lets him close with the foe, and wheels away far off the track.",
 "'similis', 'like (her)', closing the simile. 'medios… per hostis', 'through the midst of the enemy', -is accusative plural. 'fertur equis', 'is borne by the horses'. 'obit omnia', 'goes round everything', visits every part of the field. 'iamque hic… iamque hic', 'now here… now here'. 'germanum', 'her brother', Turnus. 'ostentat ovantem', 'shows (him) exulting', keeping up his credit without risking him. 'conferre manum', 'to join hand', to fight at close quarters. 'avia', 'pathless places', neuter plural accusative: 'off the track'. Elisions 'iamqu(e) hic' twice."),
(483, 'vocat.',
 "No less Aeneas the twisting circles follows, to meet him,\nand tracks the man, and through the scattered columns with great\nvoice calls.",
 "No less does Aeneas follow every winding turn to cut him off, track the man down, and call him with a great voice through the broken ranks.",
 "'Haud minus', 'no less', litotes. 'tortos… orbes', 'the twisted circles', the winding course of the chariot. 'legit', 'gathers, follows', as one follows a path. 'obvius', 'to meet (him)', trying to head him off. 'vestigat', as at 467. 'virum', Turnus. 'disiecta per agmina', 'through the scattered columns'; in 'disiecta' the i after the prefix is consonantal, dis-yec-ta. 'magna voce vocat', 'calls with a great voice', the noun split from its adjective over the line, and 'voce vocat' a play of sound. 'Aeneas', Ae- one long syllable. Elision 'vir(um) et'."),
(485, 'retorsit.',
 "As often as his eyes he cast on the enemy\nand the wing-footed flight with his running tried, of the horses,\nturned away so often the chariot Juturna twisted back.",
 "Every time he turned his eyes on his enemy and tried to match the flight of the wing-footed horses with his own speed, Juturna wheeled the chariot round and away.",
 "'Quotiens… totiens', 'as often as… so often', the correlatives. 'oculos coniecit in hostem', 'cast his eyes on the enemy'; in 'coniecit' the i is consonantal, con-ye-cit. 'alipedum… equorum', 'of the wing-footed horses', framing the line, 'alipes' a compound of the high style. 'cursu temptavit', 'tried with running', tried to overtake on foot. 'aversos… currus', 'the chariot turned away', the plural for one chariot, and proleptic: she twists it so that it is turned away. 'retorsit', from 'retorqueo'. No elisions."),
(486, 'agat?',
 "Alas, what is he to do?",
 "Alas, what can he do?",
 "'quid agat?', 'what is he to do?', a deliberative question in the subjunctive: the poet enters into Aeneas's mind and asks it for him. 'Heu', the narrator's own cry of sympathy, as at 452. Such questions bring the narrative close to inner speech. No elisions."),
(487, 'curae.',
 "On a shifting tide in vain he tosses,\nand divided call his mind to opposite courses, cares.",
 "In vain he is tossed on a shifting tide, as conflicting cares pull his mind first one way and then the other.",
 "'Vario… aestu', 'on a changing tide', framing the half-line; 'fluctuat', 'tosses like a wave', the sea-image for an unsettled mind used of Aeneas and of Dido before. 'nequiquam', 'in vain'. 'diversae… curae', 'divided cares', framing the line. 'vocant animum in contraria', 'call his mind to opposite courses': whether to keep the treaty and hunt Turnus alone, or to fight whoever comes. Elision 'anim(um) in'."),
(490, 'ictu.',
 "At him Messapus, since in his left hand two, as it happened, he carried,\npliant, as he ran light, shafts tipped with iron,\nof these one, whirling it, he aims with sure stroke.",
 "Messapus, who as it happened was carrying two pliant, iron-tipped spears in his left hand as he ran lightly forward, whirls one of them and aims it at him with a sure throw.",
 "'Huic', 'at him', dative with 'dirigit'; 'Huic' is one syllable. Messapus, son of Neptune and tamer of horses, is a leading Latin captain. 'uti', the old form of 'ut', here explaining: 'since he was carrying'. 'laeva', 'in the left hand', 'manu' understood. 'lenta… hastilia', 'pliant shafts', framing the line; 'praefixa… ferro', 'tipped with iron'. 'levis cursu', 'light in running'. 'horum unum', 'one of these'. 'contorquens', 'whirling'. 'certo… ictu', 'with sure stroke'. 'dirigit', 'aims'. Elisions 'praefix(a) hastilia', 'hor(um) unum'."),
(493, 'cristas.',
 "Stopped Aeneas, and gathered himself into his arms,\nsinking on his knee; yet the peak, speeding, the topmost,\nthe spear carried off, and the top shook from his head, the crests.",
 "Aeneas stopped short and drew himself together behind his shield, dropping on one knee; even so the spear in its rush carried away the peak of his helmet and struck the crest from its top.",
 "'Substitit', 'stopped'. 'se collegit in arma', 'gathered himself into his arms', crouching behind his shield. 'poplite subsidens', 'sinking on the knee', 'poples' the back of the knee. 'apicem… summum', 'the topmost peak' of the helmet, framing. 'incita', 'driven, at speed', with 'hasta'. 'tulit', 'carried off'. 'summas… cristas', 'the top crests', the plume, the plural for one crest. 'excussit vertice', 'shook from the top'. A near miss, and the second attack on Aeneas outside the treaty. 'Aeneas', Ae- one long syllable. Elision 'summasqu(e) excussit'."),
(494, 'irae;',
 "Then indeed rise up his wraths;",
 "Then at last his anger rises;",
 "'Tum vero', 'then indeed', the strong marker of a turning-point. 'adsurgunt irae', 'angers rise up', 'adsurgunt' Greenough's spelling of 'assurgunt'; the plural for surges of rage. Until now Aeneas has held back, hunting only Turnus; the second treacherous attack releases him. Elisions 'ver(o) adsurgunt', and 'ir(ae) insidiisque', running across the semicolon into the next unit."),
(495, 'referri,',
 "and by treacheries driven,\nwhen he saw turned aside the horses and the chariot carried back,",
 "and, driven to it by treachery, when he saw the horses and the chariot turned aside and carried away from him,",
 "'insidiis… subactus', 'driven by treacheries', both the spear thrown in time of truce and Juturna's evasions; 'subactus' means 'forced, compelled' rather than 'defeated'. 'ubi sensit', 'when he perceived', with the accusative and infinitive 'equos currumque referri', 'that the horses and chariot were being carried back'. 'diversos', 'turned aside', with 'equos'. The comma leaves the main verb to the next unit. No further elisions beyond 'ir(ae) insidiisque', noted with 494."),
(499, 'habenas.',
 "much calling to witness Jupiter and the altars of the broken treaty,\nnow at last he attacks their midst, and with Mars favouring,\nterrible, savage, with no distinction, slaughter\nhe rouses, and of his wraths all lets loose the reins.",
 "he calls again and again on Jupiter and on the altars of the violated treaty to bear witness, and now at last he charges into the thick of them and, terrible with the war-god on his side, stirs up savage slaughter that spares no one, and gives his anger free rein.",
 "'multa… testatus', 'calling much to witness', 'multa' an inner accusative, 'often, earnestly'. 'Iovem et laesi… foederis aras', 'Jupiter and the altars of the injured treaty', the altars at which the oath was sworn; Jupiter guards oaths. 'iam tandem', 'now at last'. 'invadit medios', 'charges into the midst'. 'Marte secundo', ablative absolute, 'Mars favouring'. 'nullo discrimine', 'with no distinction', killing whoever comes. 'saevam… caedem', framing. 'irarumque omnis effundit habenas', 'and lets loose all the reins of his angers', -is accusative plural; a charioteer's image, after Juturna's driving. Elisions 'Iov(em) et', 'tand(em) invadit', 'irarumqu(e) omnis'."),
(503, 'expediat?',
 "Who for me now so many bitter things — what god? — who in song the slaughters\nvarious, and the death of captains, whom over the whole plain\nin turn now Turnus drives, now the Trojan hero,\ncould unfold?",
 "What god could now set out for me in song so much bitterness, such varied slaughter, the deaths of the captains whom Turnus and the Trojan hero drive in turn across the whole plain?",
 "A new paragraph in Greenough: the poet's own appeal, without speech marks. 'Quis… deus… expediat?', 'what god could set out?', a potential subjunctive, the verb held to the start of the fourth line; 'quis' repeated. 'mihi', 'for me'. 'tot acerba', 'so many bitter things'. 'carmine', 'in song'. 'caedes diversas', 'the varied slaughter', the plural for many killings. 'obitum… ducum', 'the death of captains'. 'aequore toto', 'over the whole plain', 'aequor' of level land. 'inque vicem', 'and in turn'. 'Troius heros', Aeneas; 'Troius' has three syllables. The model, from memory, is Iliad XII, where Homer says it would be hard for him to tell all of it as a god could. No elisions."),
(504, 'futuras?',
 "Was it your pleasure that with so great a commotion should clash,\nJupiter, peoples in eternal peace destined to be?",
 "Was it your will, Jupiter, that nations destined to live in everlasting peace should clash in so great an upheaval?",
 "'Tanton' = 'tantone', 'with so great…?', the question particle '-ne' cut to '-n'. 'placuit', 'did it please (you)'. 'concurrere', 'to clash', with the accusative subject 'gentis… futuras'. 'tanto… motu', 'with such great commotion', ablative of manner. 'gentis', -is accusative plural, 'the peoples', Trojans and Italians. 'aeterna… in pace futuras', 'destined to be in eternal peace': the two peoples will become one, as Jupiter grants Juno at the end of this book. A rare direct protest by the poet to the god. No elisions."),
(508, 'ensem.',
 "Aeneas the Rutulian Sucro — that fight first, as they rushed,\nhalted in their place the Teucrians — him not long delaying\ncatches in the side and, where death is swiftest, the cruel\nsword drives through his ribs and the lattice of his chest.",
 "Aeneas meets the Rutulian Sucro (his was the first fight that brought the Trojans' charge to a stand) and, since he holds him only briefly, catches him in the side and, where death comes quickest, drives his cruel sword through the ribs that wall the chest.",
 "'Rutulum Sucronem', the object, held until 'excipit' in 507. 'ea prima… pugna', 'that fight (was) the first (which)', a parenthesis: Sucro's stand first halted the charging Trojans ('ruentis… Teucros', -is accusative plural). 'loco statuit', 'stopped in place'. 'haud multa morantem', '(him) delaying not much', not holding Aeneas long. 'excipit in latus', 'takes (him) on the side'. 'qua fata celerrima', 'where fates (are) swiftest'. 'crudum… ensem', 'the cruel sword', framing. 'transadigit', 'drives through', with a double accusative, 'costas et cratis pectoris', 'ribs and the wickerwork of the chest', 'cratis' the -is accusative plural. 'Aeneas', Ae- one long syllable. Elision 'Sucron(em) ea'."),
(512, 'portat.',
 "Turnus, thrown from his horse Amycus and his brother Diores,\nmeeting them on foot, this one as he came with the long spear-point,\nthis one with the sword he strikes, and from his chariot the cut-off of the two\nhangs heads, and dripping with blood carries them.",
 "Turnus, on foot, meets Amycus, thrown from his horse, and his brother Diores; one he strikes with his long spear as he comes on, the other with his sword, then cuts off both their heads, hangs them from his chariot and carries them, dripping with blood.",
 "'equo deiectum', 'thrown from his horse', with 'Amycum'; in 'deiectum' the i after the prefix is consonantal, de-yec-tum. 'Dioren', Greek accusative of 'Diores', perhaps the Diores of the foot-race in Book V. 'congressus pedes', 'meeting (them) on foot', 'pedes' nominative: Turnus fights them dismounted. 'hunc… hunc', 'this one… that one'. 'cuspide longa', 'with the long spear-point'. 'mucrone', 'with the sword-point'. 'curru… suspendit', 'hangs from the chariot'; 'abscisa… capita', 'the cut-off heads'. 'rorantia sanguine', 'dripping with blood'. A trophy of savage epic warfare, like the heads of Nisus and Euryalus paraded on spears in Book IX. Elisions 'deiect(um) Amycum', 'curruqu(e) abscisa', 'capit(a) et'."),
(515, 'Peridiae,',
 "That one, Talos and Tanais to death and brave Cethegus,\nthree in one encounter, sends, and gloomy Onites,\nan Echionian name, and the offspring of a mother, Peridia,",
 "Aeneas sends Talos and Tanais and brave Cethegus to their deaths, three in a single encounter, and gloomy Onites, of Echion's line and born of Peridia,",
 "'Ille… hic' (516), 'the one… the other', here Aeneas and Turnus in turn: Aeneas kills Rutulians, Turnus the Trojans and their allies. 'neci… mittit', 'sends to death', 'nex' violent death. 'Talon', 'Tanaim', Greek accusatives. 'tris', the -is accusative of 'tres'. 'Cethegum', the name of a Roman family, the Cornelii Cethegi, given to an early Italian. 'maestum', 'gloomy', the doomed man's look. 'nomen Echionium', 'Echionian in name', of the line of Echion, one of the men sprung from the dragon's teeth who helped Cadmus found Thebes. 'matris… genus Peridiae', 'the offspring of his mother Peridia', in apposition. Elision 'congress(u) et'."),
(517, 'Menoeten,',
 "this one, brothers sent from Lycia and Apollo's fields,\nand the young man who hated, in vain, wars, Menoetes,",
 "Turnus kills two brothers sent from Lycia and the fields of Apollo, and young Menoetes, who loathed war, though it did him no good,",
 "'hic', Turnus. 'fratres Lycia missos', 'brothers sent from Lycia', 'Lycia' ablative of the place from which; 'neci… mittit' carries over from 513. 'Apollinis agris', 'Apollo's fields', Lycia again, where Apollo had an oracle at Patara; the Lycians were Troy's allies in Homer. 'iuvenem exosum… bella', 'a youth who hated wars', 'exosus' a participle with active sense. 'nequiquam', 'in vain': his hatred of war did not save him. 'Menoeten', Greek accusative. Elision 'iuven(em) exosum'."),
(520, 'serebat.',
 "an Arcadian, whose, round the streams of fish-filled Lerna,\ncraft had been, and a poor home, nor known to him the powerful's\nfavours, and on hired land his father used to sow.",
 "an Arcadian, who had plied his trade round the streams of Lerna, where fish abound; his home was poor, he knew nothing of the great and their favours, and his father sowed rented ground.",
 "'Arcada', Greek accusative of 'Arcas', 'an Arcadian', one of Evander's men. 'piscosae… Lernae', 'of fish-filled Lerna', the marsh near Argos where Hercules killed the Hydra, close to the Arcadian border. 'cui… ars fuerat', 'whose craft had been', a dative of possession, presumably fishing. 'pauper… domus', 'a poor home', with 'fuerat' again. 'nec nota potentum munera', 'and the favours of the powerful (were) not known (to him)', the Roman world of patrons and clients. 'conducta… tellure', 'on hired land', framing, ablative of place. 'serebat', 'used to sow', imperfect of custom. 'cui', one syllable. No elisions."),
(522, 'lauro,',
 "And as, let loose from different sides, fires\ninto a dry wood and thickets crackling with laurel,",
 "And as fires set at different points race into a parched forest and thickets of crackling laurel,",
 "A double simile, fire and flood, for the two heroes sweeping through the battle, closed by 'non segnius' at 525. 'velut', 'as'; the verb for the fires is left out, the sense being 'rush'. 'immissi… ignes', 'fires let loose', framing the line. 'diversis partibus', 'from different sides', as the two men come at the field from opposite sides. 'arentem in silvam', 'into a dry wood'. 'virgulta sonantia lauro', 'thickets crackling with laurel', laurel being known for crackling as it burns. Homer compares a hero to fire in a wood and to a river in winter flood in Iliad XI, from memory. Elisions 'arent(em) in', 'silv(am) et'."),
(525, 'iter:',
 "or when, in swift descent from the mountains high,\ngive out their roar foaming rivers and into the seas run,\neach its own having ravaged path:",
 "or as foaming rivers rush roaring down from the high mountains and run to the sea, each laying waste its own path:",
 "'aut ubi', 'or when'. 'decursu rapido', 'in swift downward course'. 'dant sonitum', 'give sound', roar. 'spumosi amnes', 'foaming rivers'. 'in aequora currunt', 'run into the seas', the plural for the sea. 'quisque suum populatus iter', 'each having laid waste its own course', 'quisque' in apposition to the plural 'amnes', as at 457; 'populatus' a deponent participle, active in sense. Elision 'spumos(i) amnes'."),
(526, 'proelia;',
 "not more sluggishly the two,\nAeneas and Turnus, rush through the battles;",
 "with no less fury do the two of them, Aeneas and Turnus, sweep through the battle;",
 "'non segnius', 'not more sluggishly', a litotes for 'just as fiercely', closing the simile. 'ambo… ruunt', 'both rush', with 'Aeneas Turnusque' in apposition; 'Aeneas', Ae- one long syllable. 'per proelia', 'through the battles', the plural for the many fights across the field. No elisions."),
(528, 'itur.',
 "now, now\nseethes wrath within, are bursting, not knowing how to be beaten,\nthe breasts, now with all strength into wounds the going is.",
 "now, now anger surges within them, hearts that cannot learn defeat are near to bursting, now with all their might they go about the work of wounding.",
 "'nunc nunc', 'now, now', doubled at the line's end for urgency, then picked up by 'nunc' in 528. 'fluctuat ira intus', 'rage tosses within', the sea-image of 486 again. 'rumpuntur… pectora', 'breasts burst', with fury. 'nescia vinci', 'not knowing (how) to be beaten', an infinitive with an adjective. 'in volnera… itur', 'it is gone into wounds', an impersonal passive, 'they go to wound'; 'volnera' is Greenough's spelling of 'vulnera'. 'totis… viribus', 'with all their strength'. Elision 'ir(a) intus'."),
(532, 'solo:',
 "Murranus he, sounding out his forebears and of his grandsires the ancient\nnames, and his whole line traced down through Latin kings,\nheadlong with a rock and with the whirl of a huge stone\nhurls out and pours on the ground:",
 "Murranus, who was forever sounding out the ancient names of his forebears and grandsires and his whole lineage traced down through the Latin kings, Aeneas hurls headlong from his chariot with a rock, the whirling blow of a huge stone, and stretches him on the ground:",
 "'hic', here Aeneas. 'atavos… sonantem', 'sounding (his) forebears', boasting them aloud; an 'atavus' is properly a great-great-great-grandfather. 'avorum', 'of grandfathers', the full genitive. 'per reges… actum genus omne Latinos', 'his whole race carried down through Latin kings', 'actum' with 'genus'. 'scopulo… turbine saxi', 'with a crag… with the whirl of a stone', one missile described twice. 'praecipitem', 'headlong'. 'excutit effunditque solo', 'knocks out and pours on the ground', from his chariot. Elisions 'Murran(um) hic', 'avor(um) antiqua', 'regesqu(e) actum', 'scopul(o) atque', 'atqu(e) ingentis', and 'sol(o) hunc' across the colon."),
(534, 'equorum.',
 "him, the reins and yokes beneath,\nthe wheels rolled forward, and with frequent beat above, the hoof,\ndriven, of horses unmindful of their master, tramples him.",
 "and the wheels roll him under the reins and yokes, while the hooves of his own horses, forgetting their master, trample him from above with thudding blows.",
 "'hunc… provolvere rotae', 'the wheels rolled him forward', 'provolvere' = 'provolverunt'. 'lora et iuga subter', 'beneath reins and yokes', the preposition after its nouns: he is tangled under his own team. 'crebro… pulsu', 'with frequent beat'. 'super', 'above', an adverb. 'ungula… incita', 'the driven hoof', the singular for all the hooves. 'nec domini memorum… equorum', 'of horses unmindful of their master', 'memor' with the genitive, framing the last line. 'proculcat', 'tramples down'. Elisions 'sol(o) hunc', where h does not prevent elision, and 'lor(a) et'."),
(536, 'torquet:',
 "He, at Hyllus, rushing and in spirit monstrously raging,\nruns to meet him, and his spear at the gilded temples hurls:",
 "Turnus goes to meet Hyllus as he charges in, raging with monstrous fury, and hurls his spear at his gilded temples:",
 "'Ille', now Turnus. 'ruenti Hyllo… frementi', 'Hyllus rushing… raging', datives with 'occurrit', 'runs to meet'. 'animis', 'in spirit', the plural of passion. 'immane', neuter used as an adverb, 'monstrously', like 'miserabile' at 338. 'aurata ad tempora', 'at the gilded temples', the gold of the helmet over the temples; the preposition between adjective and noun. Elisions 'ruent(i) Hyllo', 'Hyll(o) animisque', 'animisqu(e) immane', 'telumqu(e) aurata', 'aurat(a) ad'."),
(537, 'cerebro.',
 "for him, through the helmet, with the brain pierced, stood the spear.",
 "the spear passed through his helmet and stood fast, lodged in his brain.",
 "'olli', the old form of 'illi', dative, 'for him', a dative of reference; Virgil keeps it from early Latin poetry, Ennius above all, for a solemn effect. 'per galeam', 'through the helmet'. 'fixo… cerebro', ablative absolute, 'with the brain transfixed', framing the clause. 'stetit hasta', 'the spear stood', upright in the wound. No elisions."),
(539, 'Turno.',
 "Nor did your right hand you, bravest of the Greeks, Cretheus,\nsnatch away from Turnus.",
 "Nor did your own right hand, Cretheus, bravest of the Greeks, save you from Turnus.",
 "The poet turns to address the dead, an apostrophe in the Homeric manner. 'Dextera nec tua te… eripuit', 'nor did your right hand snatch you away', 'tua te' set side by side. 'Graium', the old genitive plural, 'of the Greeks', two syllables, Grai-um; Cretheus is one of Evander's Arcadians, Greeks by descent. 'Cretheu', Greek vocative, the eu one syllable. 'Turno', dative of separation, 'from Turnus'. No elisions."),
(540, 'sui:',
 "Nor did the gods shelter Cupencus,\nwhen Aeneas came, his own:",
 "Nor, when Aeneas came at him, did his own gods protect Cupencus:",
 "'texere' = 'texerunt', from 'tego', 'cover, protect'. 'di… sui', 'his own gods', framing the clause: Cupencus is a priest, and Servius, from memory, says 'cupencus' was a Sabine word for priest, so his gods might have been expected to guard him. 'Aenea veniente', ablative absolute, 'Aeneas coming', 'Aenea' the ablative, with long final a; Ae- one long syllable. No elisions."),
(541, 'aerei.',
 "he gave, meeting it, to the steel\nhis breast, nor did the poor man the delay of his shield of bronze avail.",
 "he met the blade with his chest, and the bronze shield that held it back a moment did the poor man no good.",
 "'dedit obvia ferro pectora', 'he gave his breast to meet the steel', 'obvia' with 'pectora', the plural for one chest; 'ferro', 'the iron', the weapon. 'misero', dative with 'profuit', 'did (not) help the wretched man'. 'clipei mora… aerei', 'the delay of his bronze shield', framing: it slowed the blow but did not stop it. 'clipei', three syllables; 'aerei', 'of bronze', has its vowels run together (synizesis) so that the line scans. No elisions."),
(543, 'tergo.',
 "You too the Laurentine saw, Aeolus, plains\nmeet death and far and wide the earth cover with your back.",
 "You too, Aeolus, the Laurentine plains saw going down to death and stretching your length over the ground.",
 "Another apostrophe, the poet addressing the dying, as Homer addresses Patroclus and Menelaus. 'Te… Aeole', vocative, Ae- one long syllable; this Aeolus is a Trojan, not the king of the winds in Book I. 'Laurentes… campi', 'the Laurentine plains', framing the line, the fields round Laurentum, Latinus's city. 'oppetere', 'to meet (death)', 'mortem' understood. 'late… consternere tergo', 'to strew the ground far and wide with your back', a big man falling full length. Elision 'oppeter(e) et'."),
(546, 'metae:',
 "You fall, whom the Argive could not phalanxes\nlay low, nor of Priam's kingdom the overthrower, Achilles;\nhere for you of death were the turning-posts:",
 "You fall, whom neither the Argive phalanxes nor Achilles, destroyer of Priam's kingdom, could lay low; here was the goal set for your death:",
 "'Occidis', 'you fall', the present for vividness. 'Argivae… phalanges', 'the Argive phalanxes', framing, the Greeks at Troy. 'potuere' = 'potuerunt'. 'Priami regnorum eversor', 'overthrower of Priam's realm', 'regna' plural for a single kingdom. 'mortis… metae', 'the turning-posts of death', 'meta' the post at the end of a racecourse, here the end of life's course. 'erant', 'were (all along)', the imperfect of what was fated. Elision 'regnor(um) eversor'."),
(547, 'sepulchrum.',
 "a home, lofty, under Ida,\nat Lyrnesus a home lofty, in Laurentine soil a tomb.",
 "your lofty home was beneath Ida, your lofty home at Lyrnesus; your tomb is in Laurentine soil.",
 "'domus alta… domus alta', 'a high house… a high house', the repetition setting his great home against his grave, the verb left out. 'sub Ida', 'under Ida', the mountain above Troy. 'Lyrnesi', locative, 'at Lyrnesus', a town of the Troad sacked by Achilles, where he took Briseis; so Aeolus had once survived Achilles. 'solo Laurente', 'in Laurentine soil', 'Laurens' an adjective. 'sepulchrum', Greenough's spelling of 'sepulcrum'. No elisions."),
(552, 'vi:',
 "Wholly indeed turned are the lines, and all the Latins,\nall the Dardanians, Mnestheus and keen Serestus\nand Messapus, of horses the tamer, and brave Asilas\nand the Tuscans' phalanx and Evander's Arcadian squadrons,\neach for himself, the men, strive with the utmost force of their strength:",
 "The whole battle-lines are now turned on each other, all the Latins and all the Dardanians, Mnestheus and keen Serestus, Messapus the horse-tamer and brave Asilas, the Tuscan phalanx and Evander's Arcadian squadrons; every man of them strives for himself with all the strength he has:",
 "'Totae… conversae acies', 'whole battle-lines turned', 'sunt' understood: the whole armies are now engaged, not only the two leaders. 'adeo', 'indeed', stressing 'totae'. 'Dardanidae', 'descendants of Dardanus', the Trojans. 'equum domitor', 'tamer of horses', 'equum' the old genitive plural, Messapus's standing title. 'Tuscorum… phalanx', the Etruscans; 'Evandri… Arcades alae', 'Evander's Arcadian squadrons'. 'pro se quisque viri', 'the men, each for himself', 'quisque' with a plural verb. 'summa… opum vi', 'with the utmost force of their resources', the line ending on a monosyllable, an old-fashioned rhythm; the line is said, from memory, to come from Ennius. 'Mnestheus', eu one syllable. Elisions 'Tot(ae) adeo', 'convers(ae) acies', 'Evandriqu(e) Arcades'."),
(553, 'tendunt.',
 "no delay, no rest; in a vast contest they strain.",
 "there is no pause and no rest; they strain against each other in one vast struggle.",
 "'nec mora nec requies', 'neither delay nor rest', a phrase without a verb. 'vasto certamine', 'in a vast contest', ablative of manner. 'tendunt', 'they strain, strive', taking up 'nituntur' in 552. The next paragraph turns to Venus, who puts it into Aeneas's mind to attack the city itself. No elisions."),
]

# Speech-mark check exemptions (rule 5b), by closing text of the unit: none needed (the part has no speech marks).
#  'Turno.' (538-539): the print has no comma after the vocative 'Cretheu' (538); l and i supply it, and the
#      note says so. Reported for the source under rule 5.
EXEMPT = set()
# Long periods: 494-499 cut after 'irae;' (494) and at the comma after 'referri' (495); 513-520 at the commas
# after 'Peridiae' (515) and 'Menoeten' (517); 521-528 at the comma after 'lauro' (522); 548-552 is five lines.
OVERLONG = set()
P = A.part('aeneid-095'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
cuts = A.cut(P, [(u[0], u[1]) for u in U])
sents = []; prev_end_line = None
for (t, ln), (_, tail, l, i, n) in zip(cuts, U):
    u = {'t': t, 'l': l, 'i': i, 'n': n}
    if prev_end_line != ln and ln in paras: u['p'] = True
    u['v'] = True; u['ln'] = ln; sents.append(u)
    prev_end_line = ln + t.count('\n')
    if t.count('\n') != l.count('\n'): print('LINE COUNT', ln, repr(t[:30]), t.count('\n'), l.count('\n'))
    if t.count('\n') > 4: print('TOO LONG' + (' (known, uncuttable)' if ln in OVERLONG else ''), ln, t.count('\n') + 1, 'lines')
    if '\n' in i: print('NEWLINE IN i', ln)
    if t.rstrip('”]')[-1] not in A.TERMINAL + ',': print('ENDING', ln, repr(t[-12:]))
    nw = len(n.split())
    if nw > 139 or nw < 15: print('NOTE LENGTH', ln, nw)
    for mk in '“”[]':
        if t.count(mk) != l.count(mk) and tail not in EXEMPT: print('MARK l', ln, mk)
        if mk in '“”' and t.count(mk) != i.count(mk) and tail not in EXEMPT: print('MARK i', ln, mk)
    if '“' in n or '”' in n:
        if tail not in EXEMPT and 'The print has' not in n: print('DOUBLE MARK IN n', ln)
covered = sorted({ln + k for (t, ln) in cuts for k in range(t.count('\n') + 1)})
if covered != [l['n'] for l in L]: print('COVERAGE', covered)
joined = '\n'.join(l['t'] for l in L)
rebuilt = ''.join(t + ('\n' if (k + 1 < len(cuts) and cuts[k + 1][1] != ln + t.count('\n')) else ' ' if k + 1 < len(cuts) else '') for k, (t, ln) in enumerate(cuts))
if rebuilt != joined: print('JOIN MISMATCH')
if A.sha(L) != P.get('sha256', A.sha(L)): print('SHA MISMATCH')
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units;', len(covered), 'lines covered')
