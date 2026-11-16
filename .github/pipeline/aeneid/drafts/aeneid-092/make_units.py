# aeneid-092 (XII.107-215): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Foedus. Iuturna'
PART = "Juturna and the Treaty (XII.107–215)"
TITLE_EN = "Juturna and the Treaty — Aeneid XII.107–215"
ABOUT = ("The morning of the duel. Aeneas, armed in the arms his mother gave him, comforts his men and the anxious Iulus and sends word to Latinus that he accepts the terms. "
"At dawn both sides measure out a field beneath the walls of the city and build altars of turf; the armies march out, plant their spears and lean their shields against them, while the women, the unarmed crowd and the old men fill the towers and rooftops to watch. "
"From the Alban Mount, still nameless, Juno looks down and speaks to Turnus's sister Juturna, a nymph of springs and rivers whom Jupiter made immortal: she herself can do no more for Turnus and cannot bear to watch, but Juturna may dare what she will to save him and break the treaty. "
"Then the kings come out in procession, Latinus crowned with the rays of his ancestor the Sun, Turnus behind white horses, Aeneas with his starry shield and Ascanius beside him, and a priest brings the victims. "
"Aeneas swears by the gods of earth, sea and sky to the terms on both sides: if Turnus wins, the Trojans will withdraw to Evander's city; if Aeneas wins, Trojans and Italians will be joined as equals under Latinus's rule, and Lavinia will give her name to the new city. "
"Latinus swears by the same powers, by Janus and the gods below, and by his sceptre, as Achilles swore in the Iliad, that the peace will never be broken. "
"The part ends with the victims slaughtered on the altars; the whole ceremony is modelled on the oath before the duel of Paris and Menelaus in Iliad III, a truce that a goddess saw broken.")

ADVISORY = {
 "lede": "In a few words Juno recalls that Jupiter took Juturna's maidenhood and gave her rule over pools and rivers in return (140–141), and speaks of the other Latin women who went to his bed (143–144).",
 "more": "Nothing is described. The act is named in a single phrase, 'erepta pro virginitate', 'in return for her maidenhood taken from her', inside a parenthesis about how the nymph came by her honours, and Juno mentions the other women only to say that she favoured Juturna above them. Juturna returns to it herself, bitterly, near the end of the book. The text is presented unaltered, and the translations and notes render what the Latin says at the force it says it."
}

U = [
(109, 'bellum,',
 "Nor less meanwhile, in his mother's arms fierce,\nAeneas whets his Mars and rouses himself with anger,\nglad that, a treaty being offered, the war is being settled,",
 "Meanwhile Aeneas, no less fierce in the armour his mother gave him, whets his warlike spirit and stirs himself to anger, glad that the war is to be settled by the treaty offered,",
 "A new paragraph in Greenough; the scene turns to the Trojan camp. The period runs from 107 to 112; it is cut at the comma. 'Nec minus', 'no less' than Turnus, whose arming ended the last part. 'maternis… in armis', the armour Venus had Vulcan make for him (Book VIII). 'saevos' is Greenough's old spelling of 'saevus' (-os after v, as in 'divom'). 'Aeneas': Ae- is one long syllable. 'acuit Martem', 'whets his Mars', his fighting spirit. 'oblato… foedere', ablative absolute, 'a treaty being offered'; 'componi… bellum', accusative and infinitive after 'gaudens', 'that the war is being settled'. Elision 'Mart(em) et'."),
(112, 'leges.',
 "then his comrades, and sorrowing Iulus' fear, he comforts,\nteaching the fates, and to King Latinus bids an answer\nsure men carry back, and state the terms of peace.",
 "and then he comforts his companions and the fears of grieving Iulus, telling them what the fates decree, and bids men carry a firm answer back to King Latinus and set out the terms of peace.",
 "'tum', 'then', the next thing Aeneas does. 'socios… metum… Iuli', two objects of 'solatur', 'comforts', a deponent; 'maesti', 'sorrowing', goes with Iulus, his son. 'Iuli' has three syllables here, I-u-li. 'fata docens', 'teaching the fates', explaining what fate has promised. 'iubet… viros… referre', 'orders men to carry back', with 'regi… Latino' a dative. 'responsa… certa', 'a sure answer', accepting Turnus's challenge. 'pacis… leges', 'the terms of peace', the conditions sworn at 183–194. No elisions."),
(115, 'efflant:',
 "The next, barely, the highest was sprinkling with light, the mountains,\nday, risen, when first from the deep flood lift themselves\nthe Sun's horses and the light from raised nostrils breathe out:",
 "The next day, newly risen, was just scattering its light over the mountain-tops, at the hour when the horses of the Sun first lift themselves out of the deep sea and breathe daylight from their raised nostrils:",
 "A new paragraph in Greenough: the dawn of the day of the duel. 'Postera… orta dies', 'the following day, having risen', its words framing two lines; 'dies' is feminine here, as often of a fixed day. 'summos… montis', '-is' accusative plural, 'the tops of the mountains'. 'cum primum', 'as soon as'. 'alto… gurgite', 'from the deep flood', the Ocean, out of which the Sun's team climbs each morning. 'solis equi', the horses that draw the Sun's chariot. 'lucem… efflant', 'breathe out light', the daylight streaming from their nostrils. Elisions 'prim(um) alto', 'lucemqu(e) elatis'."),
(119, 'gramineas.',
 "the field for the contest under the walls of the great city\nhaving measured out, both the Rutulian men and the Teucrians were preparing,\nand in the middle hearths, and for the gods they share, altars\nof turf.",
 "The Rutulians and the Teucrians had measured out a field for the contest beneath the walls of the great city, and were making ready fire-pans in the middle and altars of turf for the gods both peoples worship.",
 "'campum… dimensi', 'having measured out the field', a deponent participle with active sense, its object far ahead of it. 'Rutulique… Teucrique', double '-que', 'both Rutulians and Teucrians'; in 'Teucri' the eu is one syllable. 'focos', 'hearths', portable braziers for the sacrificial fire. 'dis communibus', 'for the gods in common', those both sides honour. 'aras gramineas', 'altars of turf', the plain altar of the open field; the adjective runs over into the next line. Elision 'camp(um) ad'."),
(120, 'vincti.',
 "Others both spring-water and fire were bringing,\nclad in the limus and with vervain bound as to their temples.",
 "Others brought spring water and fire, dressed in the sacrificial apron, their brows bound with holy sprays.",
 "'fontemque ignemque', double '-que', 'both a spring and fire', 'fontem' standing for its water: water and fire are the two elements of purification. 'velati limo', 'clothed in the limus', an apron bordered with purple worn by attendants at a sacrifice (Servius; L&S 'limus'). 'verbena', sacred foliage plucked for rites; the fetial priests who struck Roman treaties carried it. 'tempora vincti', 'bound as to their temples', the passive participle with an accusative of the part (the Greek 'middle' use). Elisions 'fontemqu(e) ignemque', 'lim(o) et'."),
(122, 'portis.',
 "Forth comes the legion of the Ausonians, and, javelin-armed, from the full\ncolumns pour themselves, gates.",
 "The Ausonian army marches out, and its columns, armed with javelins, stream from the crowded gates.",
 "'Procedit', placed first: the march begins. 'legio', a Roman word for an army, here the Latin host. 'Ausonidum', 'of the Ausonians', the old '-um' genitive plural; Ausonia is a poetic name for Italy. 'pilata… agmina', 'columns armed with the pilum', the heavy Roman javelin (others take 'pilata' as 'close-packed'). 'plenis… portis', 'from the full gates', ablative of separation, its words parted across the line. 'se fundunt', 'pour themselves out', like water. Elision 'legi(o) Ausonidum'."),
(125, 'vocet;',
 "From here the Trojan whole\nand Tyrrhene rushes, with varied arms, army,\nno otherwise equipped with iron than if harsh, of Mars,\nbattle were calling;",
 "From this side the whole army, Trojan and Tuscan, surges out in its varied arms, equipped with steel exactly as if the harsh battle of Mars were summoning them;",
 "'Hinc', 'from this side', the Trojan camp. 'Troïus', with the diaeresis marking three syllables, Tro-i-us. 'omnis… exercitus', 'the whole army', framing a line and a half; 'Tyrrhenus', 'Tuscan', the Etruscan allies who came to Aeneas in Book X. 'ruit', 'rushes', of a mass in motion. 'haud secus… quam si… vocet', 'not otherwise than if… were calling', a comparison with the subjunctive. 'instructi', plural by sense after the collective 'exercitus'. Elision 's(i) aspera'."),
(128, 'proles.',
 "and also in the midst of the thousands the very\nleaders flit about, with gold and with purple handsome,\nboth Mnestheus, of Assaracus' race, and brave Asilas\nand Messapus, tamer of horses, Neptune's offspring.",
 "and in the midst of the thousands the captains themselves dart to and fro, splendid in gold and purple: Mnestheus of the line of Assaracus, brave Asilas, and Messapus the horse-tamer, son of Neptune.",
 "'nec non', 'and also', two negatives making a strong positive. 'volitant', 'flit about', a frequentative of 'volo', 'fly', as the leaders ride along their lines. 'auro… ostroque decori', 'handsome in gold and purple'; the Latin Library prints 'superbi', 'proud', for 'decori'. 'genus Assaraci', 'offspring of Assaracus', an early king of Troy and Aeneas's ancestor. 'equum domitor', 'tamer of horses', 'equum' the old '-um' genitive plural; the epithet is Homer's. 'Neptunia proles', Messapus is Neptune's son. Mnestheus and Asilas fight for Aeneas, Messapus for Turnus: the leaders of both sides. No elisions."),
(130, 'reclinant.',
 "And when, the signal given, into his own space each had withdrawn,\nthey fix in the ground their spears and lean back their shields.",
 "When the signal was given and each man had drawn back to his own ground, they planted their spears in the earth and leaned their shields against them.",
 "'Ut', with the indicative 'recessit', 'when', of time. 'dato signo', ablative absolute, 'the signal having been given'. 'spatia in sua', 'into their own spaces', the ground allotted to each side. 'quisque', singular, followed by the plural 'defigunt' by sense. 'defigunt tellure hastas', 'they fix their spears in the ground', 'tellure' an ablative of place: arms grounded, the sign of a truce. 'reclinant', 'lean back', setting the shields against the planted spears. Elisions 'spati(a) in', 'tellur(e) hastas'."),
(133, 'adstant.',
 "Then, poured out with eagerness, the mothers and the crowd, unarmed,\nand the feeble old men the towers and the roofs of the houses\nbeset; others at the lofty gates stand.",
 "Then the mothers, streaming out in their eagerness, the unarmed common folk and the frail old men crowded the towers and the rooftops, and others stood at the high gates.",
 "'studio effusae', 'poured out by eagerness', the women streaming from their houses to watch. 'volgus' is Greenough's spelling of 'vulgus'; 'inermum', 'unarmed', from 'inermus', a by-form of 'inermis'. 'turris', '-is' accusative plural, 'towers'. 'obsedere' = 'obsederunt', the poetic 3rd-plural perfect, 'took possession of', a siege word used of spectators. 'adstant' is Greenough's spelling of 'astant'. The watchers on the walls recall the old men of Troy watching from the gate-tower in Iliad III. Elisions 'studi(o) effusae', 'obseder(e) alii'."),
(137, 'Latini.',
 "But Juno, from the summit which now is called Alban —\nthen neither name nor honour nor glory was there to the mount —\nlooking forth from the hill, gazed on the field and both\nthe lines of Laurentines and Trojans and the city of Latinus.",
 "But Juno, looking out from the summit now called the Alban Mount — in those days the hill had no name, no honour, no renown — was watching the field below, the two armies, Laurentine and Trojan, and the city of Latinus.",
 "A new paragraph in Greenough. 'e summo… tumulo', 'from the top of the hill', its words far apart. 'qui nunc Albanus habetur', 'which is now held (to be) Alban': the Alban Mount above Alba Longa, where the Latins later kept a yearly festival to Jupiter. 'monti', dative of possession with 'erat': 'the mountain had then neither name nor honour nor glory'. 'aspectabat', a frequentative, 'kept gazing at'. 'Laurentum Troumque', genitive plurals, 'of the Laurentines and of the Trojans'; 'Troum', from 'Tros', has two syllables, Tro-um. Elisions 'Iun(o) e', 'camp(um) aspectabat', 'Troumqu(e) acies'."),
(141, 'sacravit):',
 "At once Turnus's thus she addressed sister,\ngoddess to goddess, who over pools and rivers sounding\npresides (this to her the king of the air on high\nJupiter, for her maidenhood snatched away, hallowed as an honour):",
 "At once, goddess to goddess, she spoke to Turnus's sister, who rules over pools and sounding rivers (an honour that Jupiter, high king of heaven, conferred on her in return for the maidenhood he had taken from her):",
 "'adfata est', Greenough's spelling of 'affata est', 'addressed', from the deponent 'adfor'. 'sororem', Juturna, named only at 146. 'diva deam', 'goddess (spoke to) goddess', two forms of the word set side by side. 'stagnis… fluminibusque', datives with 'praesidet', 'presides over'. 'hunc… honorem', 'this honour', her power over waters. 'erepta pro virginitate', 'in return for her maidenhood snatched away': Jupiter had violated her and paid her with immortality. Her spring, the Lacus Iuturnae, was in the Roman Forum. 'rex aetheris altus', 'high king of the upper air'. No elisions."),
(145, 'locarim:',
 "“Nymph, glory of rivers, most pleasing to my heart,\nyou know how you alone, above all the Latin women who\nof great-hearted Jove the unwelcome bed have climbed,\nI have preferred, and gladly in a part of heaven have placed:",
 "“Nymph, glory of the rivers, dearest of all to my heart, you know how I have favoured you alone above all the Latin women who have climbed into great-souled Jupiter's unwelcome bed, and how gladly I have given you a place in heaven:",
 "Juno's speech opens; it runs to 153. 'decus fluviorum', 'glory of the rivers', in apposition. 'animo… nostro', dative with 'gratissima', 'nostro' the royal plural. 'scis ut', 'you know how', an indirect question with the subjunctives 'praetulerim… locarim'; 'locarim' = 'locaverim', a syncopated perfect. 'te… unam', 'you alone'. 'quaecumque Latinae… ascendere', 'whatever Latin women climbed', 'ascendere' = 'ascenderunt'. 'ingratum… cubile', 'the unwelcome bed', hateful to the wronged wife who speaks. 'lubens' is Greenough's spelling of 'libens'. 'caeli… in parte', 'in a share of heaven', her immortality. Elisions 'fluvior(um) animo', 'ingrat(um) ascendere'."),
(146, 'dolorem.',
 "learn your — lest you blame me — Juturna, grief.",
 "now learn, Juturna, of the grief that is coming to you, so that you may not lay the blame on me.",
 "'disce… dolorem', 'learn your grief', the sorrow about to fall on you, your brother's death; the two words stand at either end of the line, with the purpose clause and her name between. 'ne me incuses', 'so that you may not blame me', a negative purpose clause: Juno wants it known that she did all she could. 'Iuturna', named at last: a Roman goddess of springs, here made Turnus's sister. Elision 'm(e) incuses'."),
(148, 'texi:',
 "Where Fortune seemed to allow and the Fates were permitting\nthings to go well for Latium, Turnus and your walls I sheltered:",
 "As long as Fortune seemed to allow it and the Fates permitted Latium's cause to prosper, I shielded Turnus and your city's walls:",
 "'Qua', 'in so far as', the limit of what was allowed. 'visa est… pati', 'seemed to permit', and 'Parcae… sinebant', 'the Fates were allowing', both govern 'cedere res Latio', 'that affairs should turn out (well) for Latium'; 'cedere' here is 'to turn out, succeed' (L&S). The Parcae are the three Fates. 'tua moenia', 'your walls', Ardea, the city of Turnus and his sister. 'texi', 'I covered, protected', from 'tego'. Elisions 'vis(a) est', 'Turn(um) et'."),
(150, 'propinquat.',
 "now the young man with unequal fates I see clash,\nand the Fates' day and a hostile force draws near.",
 "Now I see the young man going into battle with a destiny no match for his foe's, and the day the Fates have set and a hostile power are close upon him.",
 "'iuvenem… concurrere', accusative and infinitive after 'video', 'I see the young man meeting (in fight)'. 'imparibus… fatis', 'with unequal fates', ablative of attendant circumstance: his destiny is no match for Aeneas's. 'Parcarum dies', 'the day of the Fates', his appointed day of death. 'vis inimica', 'the hostile power', Aeneas and the will of heaven behind him. The singular 'propinquat' serves both subjects. Elision 'iuven(em) imparibus'."),
(151, 'possum.',
 "Not the fight, this, to look on with my eyes, not the treaty can I.",
 "I cannot bear to look upon this fight, nor upon this treaty.",
 "'Non… non', the negative repeated with each object (anaphora). 'pugnam… hanc', 'this fight', the words parted. 'aspicere… possum', 'I can look upon', taking both objects; 'oculis', 'with my eyes', adds weight. Juno cannot bear to watch the duel that will end Turnus, nor the treaty that will end her war. Elisions 'pugn(am) aspicere', 'aspicer(e) hanc'."),
(153, 'decet.',
 "You, for your brother, if anything more effective you dare,\ngo on: it is fitting.",
 "If you dare anything more effective for your brother, go on: it becomes you.",
 "'Tu', emphatic: what Juno will not do openly, the sister may. 'pro germano', 'on behalf of your brother', 'germanus' being a full brother. 'siquid', printed by Greenough as one word, = 'si quid', 'if anything'. 'praesentius', 'more immediate, more effective', 'praesens' being the word for a god's help felt on the spot. 'perge', 'go on, proceed'. 'decet', 'it is fitting', a sister's part. No elisions."),
(153, 'sequentur.”',
 "Perhaps the wretched better things will follow.”",
 "It may be that better things are in store for the unhappy.”",
 "'Forsan', 'perhaps', a poetic form of 'fortasse'. 'miseros… sequentur', 'will follow the wretched': better fortune may yet come to those now in misery. After what Juno has just said of the fatal day, it sounds more like a spur than a hope. The speech ends here. No elisions."),
(155, 'honestum.',
 "Barely these words, when tears from her eyes Juturna poured\nand three times and four times with her hand her breast struck, comely.",
 "She had scarcely finished when Juturna poured tears from her eyes and beat her lovely breast with her hand three and four times over.",
 "'Vix ea (dixerat), cum', 'scarcely (had she said) these things, when', the verb of speaking left out. 'cum… profudit', 'cum' with the indicative after 'vix': the main event comes in the cum-clause (the 'inverted' cum). 'oculis', 'from her eyes', ablative of separation; the Latin Library has the present 'profundit'. 'terque quaterque', 'three and four times', the phrase of I.94. 'honestum', 'comely, fair', the beauty of the breast she strikes. Beating the breast is the gesture of mourning. No elisions."),
(156, 'Iuno:',
 "“Not for tears this time,” says Saturnian Juno:",
 "“This is no time for tears,” said Saturnian Juno.",
 "The print has 'tempus, ”ait', a misprint for 'tempus,” ait', corrected here: the closing mark is set after the space and joined to the next word, as elsewhere in this edition. 'Non lacrumis hoc tempus (est)', 'this is not a time for tears', 'lacrumis' (Greenough's spelling of 'lacrimis') a dative of purpose. 'ait', 'says', breaks into the speech. 'Saturnia', 'daughter of Saturn', Juno's standing epithet. No elisions."),
(158, 'foedus:',
 "“Hurry, and your brother, if there is any way, snatch from death,\nor do you stir up war and shake loose the framed treaty:",
 "“Make haste, and snatch your brother from death if there is any way, or else stir up war yourself and strike down the treaty they have framed:",
 "Juno's words resume after 'ait'; they run to 159. 'Adcelera' is Greenough's spelling of 'accelera', 'hurry', keeping the prefix 'ad-' unassimilated. 'siquis modus (est)', 'if there is any way'. 'eripe morti', 'snatch from death', 'morti' a dative of separation. 'bella cie', 'stir up war', 'cie' the imperative of 'cieo'. 'conceptum… foedus', 'the treaty framed', 'concipere' being the word for putting a formula into set words (Turnus's 'concipe foedus', 13). 'excute', 'knock out, shake off'. Elisions 'Adceler(a) et', 'conceptumqu(e) excute'."),
(159, 'audendi.',
 "the backer, I, of the daring.”",
 "I take the daring upon myself.”",
 "The print has 'audendi. ”Sic', a misprint for 'audendi.” Sic', corrected here: the mark closing Juno's speech is joined to the next word, so t keeps the print and l and i close the speech after 'audendi.'. 'auctor ego (sum) audendi', 'I am the author of the daring', 'audendi' the genitive of the gerund. An 'auctor' stands as guarantor for what another does: the responsibility, and the blame, will be Juno's. Elision 'eg(o) audendi'."),
(160, 'mentis.',
 "Thus having urged her on, she left her\nuncertain and troubled by the sad wound of her mind.",
 "With these words of encouragement she left her, wavering, and shaken by the grievous wound in her heart.",
 "The print has 'audendi. ”Sic', a misprint for 'audendi.” Sic', corrected here; the mark at the head of t belongs to the speech just ended, so l and i carry none. 'exhortata', a deponent participle, 'having urged (her) on'. 'incertam', 'undecided', with 'eam' understood. 'tristi… volnere mentis', 'by a sad wound of the mind', grief pictured as a wound; 'volnere' is Greenough's spelling of 'vulnere'. Elision 'incert(am) et'."),
(164, 'specimen;',
 "Meanwhile the kings — in vast state Latinus\nin a four-horse chariot rides, whose temples around\ngilded twice six rays, shining, encircle,\nof the Sun, his grandsire, the token;",
 "Meanwhile the kings come out: Latinus rides in great state in a four-horse chariot, twelve gilded rays ringing his shining brows, the emblem of his grandsire the Sun;",
 "A new paragraph in Greenough. 'reges', 'the kings', is the subject of 'procedunt' at 169; the sentence breaks off to describe each of them. 'ingenti mole', 'with vast mass', in great pomp and with a great train. 'quadriiugo', 'four-yoked'; the second i is a consonant, so the word has four syllables, qua-dri-iu-go. 'cui tempora circum', 'around whose temples', 'circum' after its noun. 'bis sex radii', 'twice six rays', a radiate crown. 'Solis avi specimen', 'token of his grandfather the Sun': in Hesiod Latinus is a son of Circe, the Sun's daughter, though Virgil in Book VII makes him a son of Faunus (from memory). No elisions."),
(165, 'ferro;',
 "in a white pair goes Turnus,\ntwo in his hand, with broad iron, brandishing spear-shafts;",
 "Turnus drives behind a pair of white horses, brandishing in his hand two spears with broad iron heads;",
 "'bigis… in albis', 'in a white pair', 'bigae' being a two-horse chariot and 'albis' its white horses, the team of 12.83–84. 'bina… hastilia', 'two spears', 'bini' the distributive numeral used of things that go in pairs; Homer's heroes often carry two spears. 'lato… ferro', ablative of description, 'with broad iron (heads)'. 'crispans', 'brandishing', making them quiver. No elisions."),
(169, 'castris,',
 "on this side father Aeneas, of the Roman stock the source,\nblazing with starry shield and heavenly arms,\nand beside him Ascanius, of great Rome the second hope,\ncome forth from the camp,",
 "and from the other side father Aeneas, the source of the Roman race, ablaze with his starry shield and heavenly armour, and beside him Ascanius, the second hope of great Rome, come out from the camp,",
 "The sentence begun at 166 runs to 171; it is cut at the comma. 'hinc', 'on this side', the Trojan camp, answering Latinus and Turnus. 'Romanae stirpis origo', 'source of the Roman stock', in apposition. 'sidereo… clipeo', 'with starry shield', the shield Vulcan made in Book VIII, with Rome's future worked on it; 'caelestibus armis', arms made in heaven. 'iuxta', 'close by', an adverb. 'spes altera', 'the second hope', after his father. 'procedunt castris', 'come forth from the camp', 'castris' an ablative of separation: at last the verb of 'reges' (161). Elisions 'clipe(o) et', 'iuxt(a) Ascanius'."),
(171, 'aris.',
 "and in pure raiment a priest\nof a bristly sow the young and an unshorn two-year ewe\nbrought, and moved the beasts up to the blazing altars.",
 "and a priest in spotless robes brought the young of a bristly sow and an unshorn ewe of two years, and led the beasts up to the burning altars.",
 "'pura in veste', 'in pure raiment', white and unstained, as a sacrifice requires. 'sacerdos', the priest, subject of both verbs. 'saetigeri fetum suis', 'the young of a bristly sow', a piglet: Roman treaties were struck over a pig (Livy I.24, from memory). 'intonsam bidentem', 'an unshorn ewe', 'bidens' a sheep of the age fit for sacrifice (L&S: having two prominent teeth). 'adtulit' is Greenough's spelling of 'attulit'; 'admovit… pecus', 'moved the beasts up', 'pecus' collective. Elision 'puraqu(e) in'."),
(174, 'libant.',
 "They, toward the rising, having turned their eyes, sun,\ngive meal from their hands, salted, and the brows with the knife,\nthe tops, mark of the beasts, and from bowls pour on the altars.",
 "Turning their eyes toward the rising sun, they scatter salted meal from their hands, mark the victims with the knife on the crown of the head, and pour libations on the altars from shallow bowls.",
 "'Illi', the kings. 'conversi lumina', 'turned as to their eyes', a passive participle with an accusative of the part (the Greek 'middle' use): they face east to pray. 'fruges… salsas', 'salted grain', the meal sprinkled on a victim's head. 'tempora… summa notant', 'they mark the tops of the temples', clipping hair from between the horns as a first offering. 'pateris', broad shallow bowls for pouring. 'altaria libant', 'pour libations on the altars'. The rite follows the oath-sacrifice before the duel of Paris and Menelaus in Iliad III. Elision 'Ill(i) ad'."),
(175, 'precatur:',
 "Then dutiful Aeneas, his sword drawn, thus prays:",
 "Then dutiful Aeneas drew his sword and prayed in these words:",
 "'pius Aeneas', his standing epithet, apt at a sacred rite. 'stricto… ense', ablative absolute, 'his sword having been drawn', part of the solemnity of the oath he is about to swear. 'precatur', 'prays', a deponent. The colon introduces his prayer, which is also an oath. No elisions."),
(180, 'torques;',
 "“Be now the Sun witness, and this Earth, to me calling,\nfor whose sake such great toils I have had strength to endure,\nand the almighty father, and you, Saturnian consort,\nnow kinder, now, goddess, I pray, and you, renowned Mavors,\nwho all wars, father, beneath your sway turn;",
 "“Now let the Sun be my witness as I call upon him, and this Land, for whose sake I have had the strength to bear such labours, and the almighty Father, and you, Saturnian consort — kinder now, goddess, kinder now, I pray — and you, glorious Mavors, father, who turn every war beneath your power;",
 "Aeneas's prayer and oath open; they run to 194. 'Esto', future imperative of 'sum', 'be (my) witness', the solemn form; 'mihi vocanti', 'to me as I call'. 'haec… Terra', 'this Land', Italy. 'quam propter', 'on account of which', the preposition after its noun. 'Saturnia coniunx', Juno; 'iam melior', 'now kinder', a prayer that her anger is at last spent. In 'coniunx' the i is a consonant. 'Mavors', an old name of Mars. 'torques', 'turn, wield', as one steers. The list follows Agamemnon's oath in Iliad III: Zeus, the Sun, rivers, Earth, the powers below. Elision 'tuqu(e) inclute'."),
(182, 'ponto:',
 "and springs and rivers I call, and whatever of the high air\nsanctity, and what in the blue sea are powers:",
 "and I call on the springs and rivers, on every holy presence of the high heavens, and on the divinities that dwell in the dark-blue sea:",
 "'fontisque fluviosque', double '-que', 'both springs and rivers'; 'fontis', '-is' accusative plural. 'quaeque… religio', 'and whatever sanctity (there is) of the high heaven', 'religio' here the divine presence that inspires awe, standing for the gods themselves. 'quae caeruleo sunt numina ponto', 'whatever powers are in the blue sea', 'ponto' an ablative of place. The colon leads into the terms of the oath. Elisions 'quaequ(e) aetheris', 'religi(o) et'."),
(186, 'lacessent,',
 "if by chance victory falls to Ausonian Turnus,\nit is agreed that the conquered withdraw to Evander's city,\nIulus will quit the fields, nor afterwards any arms, rebelling,\nwill the Aeneadae bring back or with iron harass these realms,",
 "if victory should chance to fall to Ausonian Turnus, it is agreed that the defeated shall withdraw to Evander's city; Iulus shall give up these lands, and never hereafter shall the people of Aeneas take up arms again in revolt or attack this kingdom with the sword,",
 "The terms of the oath, first if Turnus wins. The period runs from 183 to 190; it is cut at the comma. 'cesserit… si', 'if (victory) shall have fallen', future perfect; 'fors', 'by chance', used as an adverb. 'convenit', 'it is agreed', the word of a contract. 'Evandri… urbem', Pallanteum, on the site of Rome. 'cedet… agris', 'will withdraw from the land'. 'rebelles', 'renewing war', its root sense. 'Aeneadae', 'the people of Aeneas'; Ae- is one syllable. 'ferrove', 'or with the sword', '-ve' = 'vel'. Elisions 'disceder(e) ad', 'arm(a) ulla', 'ferrov(e) haec'."),
(190, 'peto:',
 "but if Victory nods our Mars to us\n(as rather I think, and rather may the gods confirm by their power),\nI will not bid the Italians obey the Teucrians,\nnor for myself do I seek a kingdom:",
 "but if Victory grants the battle to us (as I rather believe, and may the gods rather make it so by their power), I will not command the Italians to be subject to the Teucrians, nor do I seek a kingdom for myself:",
 "The other outcome, if Aeneas wins. 'sin', 'but if'. 'adnuerit… Martem', 'shall have nodded the battle to us', granted it with a nod, as gods grant prayers; 'nostrum… Martem', 'our Mars', the fight as ours. 'Victoria', the goddess Victory. 'ut potius reor', 'as I rather think'; 'firment', a subjunctive of wish, 'may (the gods) confirm it'. 'non ego nec… nec', the negatives piled up. 'Teucris', dative with 'parere', 'obey'; eu is one syllable. 'regna', poetic plural, 'a kingdom'. Elision 'nostr(um) adnuerit'."),
(191, 'mittant.',
 "on equal terms both\nunconquered nations into everlasting treaty let them commit themselves.",
 "Let both nations, unconquered, bind themselves on equal terms in an everlasting covenant.",
 "'paribus… legibus', 'on equal terms', ablative of manner. 'ambae… gentes', 'both peoples', framing; 'invictae', 'unconquered': neither will be a subject nation. 'se… mittant', jussive subjunctive, 'let them send themselves' into the treaty. This is Virgil's picture of Rome's beginnings: Trojans and Italians joined as equals, not conquerors and conquered. Elision 'aetern(a) in'."),
(192, 'dabo;',
 "Rites and gods I will give;",
 "I will give them my sacred rites and my gods;",
 "'Sacra deosque', 'the rites and the gods', the Penates and the worship Aeneas carried out of Troy (I.6, 'inferretque deos Latio'). What the Trojans bring to the union is religion; the Latins keep their arms and their rule. 'dabo', 'I will grant'. No elisions."),
(193, 'socer;',
 "my father-in-law, his arms, Latinus, let him keep,\nhis rule, accustomed, my father-in-law;",
 "let Latinus, my father-in-law, keep his arms; let my father-in-law keep the sovereignty that is his by right;",
 "'habeto', future imperative, 'let him have', the language of law and treaty. 'socer… socer', 'father-in-law', repeated: Aeneas presses the bond the marriage to Lavinia will make. 'imperium sollemne', 'his established authority', 'sollemnis' meaning customary, hallowed by long use. The one verb 'habeto' serves both clauses. No elisions."),
(194, 'nomen.”',
 "for me walls the Teucrians\nwill set up, and to the city will give Lavinia her name.”",
 "the Teucrians shall build walls for me, and Lavinia shall give the city her name.”",
 "'mihi', 'for me', a dative of advantage. 'Teucri', with eu one syllable. 'constituent', 'will establish'. 'urbi… dabit… nomen', 'will give the city a name': Lavinium, the first Trojan city in Italy, called after Lavinia (compare 'Lavinia… litora', I.2). The prayer and oath end here. No elisions."),
(196, 'dextram:',
 "Thus first Aeneas; follows thus then Latinus,\nlooking up at the sky, and stretches to the stars his right hand:",
 "So Aeneas spoke first, and Latinus followed in the same way, looking up to the sky and stretching his right hand toward the stars:",
 "'Sic prior Aeneas (dixit)', the verb of speaking left out. 'deinde' is two syllables here, dein-de, the ei run together. 'suspiciens', 'looking up at', from 'sub' and 'specio'. 'tendit… dextram', the raised right hand of one taking an oath. Elision 'tenditqu(e) ad'."),
(199, 'Ditis;',
 "“These same things, Aeneas, by earth, sea, stars I swear,\nand Latona's twofold offspring and two-fronted Janus,\nand the power of the gods below and of harsh Dis the shrines;",
 "“To these same terms I swear, Aeneas, by earth, by sea, by the stars, by Latona's two children and two-faced Janus, by the might of the gods below and the shrines of pitiless Dis;",
 "Latinus's oath opens; it runs to 211. 'Haec eadem… iuro', 'I swear these same things', the terms Aeneas has set out. 'terram mare sidera', accusatives of what one swears by, listed without connectives (asyndeton). 'Aenea', the Greek vocative; Ae- is one long syllable. 'Latonae genus duplex', 'Latona's twofold offspring', Apollo and Diana. 'Ianum bifrontem', Janus, the two-faced god of gateways and beginnings, an Italian god sworn by an Italian king. 'deum', the old genitive plural. 'Ditis', Dis, lord of the dead. Elisions 'ead(em) Aenea', 'de(um) infernam', 'infern(am) et'."),
(200, 'sancit.',
 "may hear these things the Father, who treaties with the thunderbolt hallows.",
 "May the Father hear this, who seals treaties with his thunderbolt.",
 "'audiat', a subjunctive of wish, 'may he hear'. 'genitor', 'the Father', Jupiter. 'foedera fulmine sancit', 'makes treaties sacred with the thunderbolt': Jupiter strikes down the oath-breaker, and at Rome the fetial priest struck the treaty pig with a flint in his name (Livy I.24, from memory). The f-sounds weigh on the line. No elisions."),
(201, 'testor:',
 "I touch the altars; the fires between and the powers I call to witness:",
 "I lay my hand on the altars, and I call to witness the fires between us and the gods:",
 "'Tango aras', 'I touch the altars', the gesture of one who swears. 'medios ignis', 'the fires in the middle', the altar flames standing between the two parties; 'ignis', '-is' accusative plural. 'testor', 'I call to witness', a deponent. Elision 'Tang(o) aras'."),
(203, 'cadent;',
 "no day this peace for the Italians nor the treaty will break,\nhowever things fall out;",
 "no day shall break this peace for the Italians, or this treaty, however things may fall;",
 "'nulla dies', 'no day', no time to come. 'Italis', 'for the Italians', a dative of reference. 'quo res cumque cadent' = 'quocumque res cadent', 'in whatever way things fall out'; the word is split by 'res', a figure called tmesis, 'cutting'. The future 'cadent' covers the duel: whoever wins, the peace will hold. Elision 'pac(em) hanc'."),
(205, 'solvat;',
 "nor me any force, willing,\nshall turn aside, not if it pour the earth into the waves,\nmingling them in flood, and melt heaven into Tartarus;",
 "no force shall make me turn from it of my own will, not even if it should pour the earth into the waves, mingling all in a flood, and melt heaven down into Tartarus;",
 "'me… volentem', 'me willing': no force shall turn me aside so that I consent to it. 'avertet', 'shall turn away'. 'non, si…', 'not (even) if', with the subjunctives 'effundat… solvat', a case imagined; their subject is still 'vis', 'that force'. 'diluvio miscens', 'confounding (them) in a deluge'. 'caelum… in Tartara solvat', 'should dissolve heaven into Tartarus', the whole order of the world collapsing. Elisions 'tellur(em) effundat', 'caelumqu(e) in'."),
(207, 'umbras,',
 "as this sceptre” (for in his right hand a sceptre, as it chanced, he was bearing)\n“never with light leafage will put forth shoots or shade,",
 "just as this sceptre” — for he happened to be holding his sceptre in his right hand — “will never again put out light leaves or shoots or give shade,",
 "The print has 'hoc ”(dextra', a misprint for 'hoc” (dextra', corrected here: the closing mark is joined to the next word, as elsewhere in this edition. The period runs from 206 to 211; it is cut at the comma. 'ut', 'as (surely as)': the oath stands as fixed as the sceptre will stay dead. Latinus echoes Achilles' oath by his sceptre in Iliad I, which will never put out leaves again. The parenthesis 'dextra… gerebat' is the poet's, stepping into Latinus's words; 'nam' comes late in its clause. 'fronde levi', 'with light foliage'. 'virgulta', 'shoots'. Elision 'sceptr(um) hoc'."),
(211, 'Latinis.”',
 "since once in the woods from the lowest stock cut off\nit lacks its mother and has laid down to the iron its leaves and arms,\nonce a tree, now a craftsman's hand in comely bronze\nhas cased it and given it to the Latin fathers to bear.”",
 "now that it has once been cut in the forest from the foot of its trunk and has lost its mother, and has shed its leaves and branches to the axe; once a tree, now a craftsman's hand has sheathed it in fine bronze and given it to the elders of Latium to bear.”",
 "The print has 'gesture gestare', a misprint for 'gestare', corrected here: 'gesture' is not Latin and breaks the metre, and the Latin Library lacks it. 'cum semel', 'since once', with the indicatives 'caret… posuit'. 'imo de stirpe', 'from the bottom of the stock', 'stirps' masculine here ('imo'). 'recisum', 'cut off'. 'matre', 'its mother', the parent tree. 'comas et bracchia', 'its hair and arms', leaves and branches, the tree pictured as a body. 'ferro', 'by the axe'. 'olim arbos', 'once a tree', 'arbos' the old form of 'arbor'. 'patribus… Latinis', the elders of Latium; 'gestare', 'to carry', the sceptre of office. The oath ends here. No elisions."),
(213, 'procerum.',
 "With such, between themselves, they were confirming the treaty, words,\nin the sight, in the midst, of the chiefs.",
 "With such words they confirmed the treaty between them, in full view of the assembled chiefs.",
 "'Talibus… dictis', 'with such words', framing the line, the formula that closes speeches. 'inter se', 'with one another'. 'firmabant', imperfect, the ceremony still in progress. 'conspectu in medio procerum', 'in the midst of the sight of the chiefs', in full view of the leading men of both sides, so the oath has its witnesses. Elision 'conspect(u) in'."),
(215, 'aras.',
 "Then, duly consecrated,\ninto the flame they cut the throats of the beasts, and the entrails from them living\ntear out, and heap with loaded platters the altars.",
 "Then over the flames they cut the throats of the duly consecrated victims, tear out the entrails while the beasts still live, and pile the altars high with laden platters.",
 "'rite sacratas… pecudes', 'the victims duly consecrated', its words framing a line. 'in flammam iugulant', 'they cut their throats into the flame', so the blood falls on the fire. 'viscera vivis eripiunt', 'tear the entrails from them (still) living', 'vivis' a dative of separation. 'oneratis lancibus', 'with loaded dishes', the 'lanx' a broad platter for offerings. 'cumulant… aras', 'heap the altars'. The ceremony is complete; the next part shows how it is broken. Elision 'cumulantqu(e) oneratis'."),
]

# Speech-mark check exemptions (rule 5b), by closing text of the unit:
#  'audendi.' (159): the print closes Juno's speech with a mark joined to 'Sic' ('audendi. ”Sic');
#      t lacks the mark, l and i close the speech after 'audendi.'.
#  'mentis.' (159-160): the mark stands at the head of t ('”Sic'); l and i carry none.
EXEMPT = {'audendi.', 'mentis.'}
# Long periods are cut at internal commas (107-112 at 109, 166-171 at 169, 183-190 at 186, 206-211 at 207), as build_aeneid.py allows.
OVERLONG = set()
P = A.part('aeneid-092'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
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
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'advisory': ADVISORY, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units;', len(covered), 'lines covered')
