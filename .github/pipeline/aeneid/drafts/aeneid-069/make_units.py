# aeneid-069 (IX.530-620): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Turris eversa. Numani probra'
PART = "The Falling Tower and the Taunts of Numanus (IX.530–620)"
TITLE_EN = "The Falling Tower and the Taunts of Numanus — Aeneid IX.530–620"
ABOUT = ("The assault on the Trojan camp goes on. A tall wooden tower, joined to the wall by gangways, is the "
"Italians' chief target; Turnus throws a blazing torch into its side, the fire takes hold, and as the defenders crowd "
"away from the flames their weight brings the whole tower down. Only two men escape the wreck. Young Helenor, a king's "
"son by a slave-woman, carrying a plain white shield, finds himself among thousands of enemies and charges to his death "
"like a beast leaping onto the hunters' spears; the swift Lycus reaches the wall and is clutching for his friends' "
"hands when Turnus catches him, taunts him, and tears him down with part of the wall, as an eagle carries off a hare "
"or a wolf a lamb. A list of killings follows on both sides, ending with the splendid son of Arcens, brought up in "
"Sicily, whose head Mezentius splits with a sling-stone. Then, for the first time in war, young Ascanius bends his "
"bow. His target is Numanus Remulus, newly married to Turnus's younger sister, who is striding before the lines "
"shouting insults: the Trojans are twice-conquered Phrygians hiding behind walls, while the Italians are a hard race "
"who dip their babies in icy rivers, hunt as boys, plough and fight as men, and wear helmets over their grey hair; "
"the Trojans, with their saffron and purple, sleeves and bonneted caps, are women, and should go back to the drums "
"and pipes of Cybele and leave war to men. The part ends with the taunt; the arrow comes in the next.")

U = [
(534, 'fenestras.',
 "A tower there was, of vast height to look up to, and with gangways high,\nwell placed in its position, which with utmost strength all\nthe Italians to storm and with utmost force of means to overthrow\nwere striving; the Trojans in return to defend it with stones\nand through the hollow loopholes, crowded, weapons to hurl.",
 "There was a tower of towering height, joined to the walls by lofty gangways and placed where it most counted; all the Italians were straining with all their might to storm it and to bring it down with every means they had, while the Trojans fought back, defending it with stones and, packed close together, hurling their spears through its open loopholes.",
 """A new paragraph in Greenough. 'vasto suspectu', 'of vast looking-up', an ablative of description: its height as measured by the upward gaze. 'pontibus', 'bridges', the gangways joining the wooden tower to the wall. 'opportuna loco', 'well placed in position'. 'expugnare… evertere' depend on 'certabant', 'were striving'; 'Troes contra (certabant) defendere… intorquere', the verb understood for the Trojans too. 'summis… viribus… summaque… opum vi', 'with utmost strength and utmost force of resources', the repetition giving the effort. 'densi', 'crowded', with the Trojans. 'fenestras', 'windows', here loopholes. The storming of a wall goes back to Iliad 12, where the Trojans assault the Greek rampart. Elisions 'suspect(u) et', 'expugnar(e) Itali', 'summaqu(e) evertere', 'everter(e) opum', 'tel(a) intorquere'."""),
(537, 'adesis.',
 "First a blazing hurled torch Turnus\nand the flame fixed to its side, which in fullest force with the wind\nseized the planks and to the posts clung, eaten through.",
 "Turnus was the first to hurl a blazing torch and lodge the fire in the tower's side; whipped up by the wind it caught the planking in a mass of flame and clung to the posts as it ate them through.",
 """'Princeps', 'first', an adjective with the force of an adverb. 'lampada', 'torch', a Greek accusative singular of 'lampas'. 'adfixit lateri', 'fixed to the side', Greenough's 'adf-' for 'aff-', with the dative. 'quae plurima', 'which (flame), in great mass', 'plurima' with the force of an adverb, 'in fullest force'; 'vento', 'with the wind', ablative of means. 'tabulas', 'planks'. 'postibus… adesis', 'to the eaten posts', dative with 'haesit', 'clung'; 'adesis' from 'adedo', 'eat into', the beams already gnawed by the fire it clings to. Elision 'flamm(am) adfixit'."""),
(539, 'fugam.',
 "Thrown into confusion, they panic within, and in vain from the evils\nwant escape.",
 "Inside, the men were thrown into confusion and panic, wanting to escape the disaster and finding no way.",
 """'trepidare… velle', historic infinitives (as 'effundere', 511): the plain infinitive used for an imperfect in quick narrative, with 'turbati', 'thrown into confusion', as subject. 'frustra', 'in vain'. 'malorum… fugam', 'flight from the evils', 'malorum' an objective genitive, the thing fled from. Elision 'trepidar(e) intus'."""),
(541, 'fragore.',
 "While they mass themselves and back they sink\ninto the part which from the plague is free, then with the weight the tower\nfell headlong suddenly, and the sky thunders all with the crash.",
 "As they crowded together and fell back to the side the fire had not reached, the tower, under that sudden weight, came crashing down, and the whole sky thundered with the noise.",
 """'Dum… glomerant… residunt', 'while they mass themselves and sink back', 'dum' with the present in narrative. 'in partem quae peste caret', 'into the part which is free from the plague', 'peste' the fire, ablative with 'caret'. 'tum', 'then', picking up the 'dum' clause. 'pondere', 'with the weight', of all the men crowding onto one side, which overbalances the tower. 'procubuit subito', 'fell forward suddenly', the perfect of a single instant; 'tonat', 'thunders', the present, of the noise that follows. 'caelum… omne', 'the whole sky', framing 'tonat'. Elision 'subit(o) et'."""),
(544, 'veniunt.',
 "Half-dead to the ground, with the huge mass following,\nboth pierced with their own weapons and in the chests by hard\nrun through timber, they come.",
 "Half-dead they came to the ground with the huge mass crashing after them, pierced by their own weapons, their chests run through by splintered beams.",
 """'Semineces', 'half-dead', from 'semi-' + 'nex', 'death'. 'immani mole secuta', ablative absolute, 'the huge mass having followed', 'secuta' a deponent participle with active meaning: the wreckage falls on them. 'confixi… transfossi', 'pierced… run through', 'suis telis', 'by their own weapons', the spears they were holding. 'pectora', 'as to their chests', an accusative of respect with a passive participle (the Greek construction), framed with 'duro… ligno', 'with the hard wood'. 'veniunt', 'they come', held back to the end of the sentence. Elision 'terr(am) immani'."""),
(545, 'elapsi.',
 "Scarcely only Helenor\nand Lycus escaped.",
 "Barely two escaped, Helenor and Lycus.",
 """'Vix unus Helenor et Lycus', 'scarcely Helenor alone and Lycus', 'unus' adding 'only', 'just'; the two names are the only survivors. 'elapsi (sunt)', 'slipped out', the plural verb with two subjects, 'sunt' left out. No elisions."""),
(548, 'alba;',
 "Of whom the young Helenor,\nwhom to the Maeonian king the slave Licymnia secretly\nhad borne, and in forbidden to Troy had sent arms,\nwith a sword light, bare, and with a shield inglorious, white;",
 "Of the two, young Helenor, whom the slave-woman Licymnia had borne in secret to the king of Maeonia and sent to Troy in arms he had no right to bear, was lightly armed with a bare sword and carried a plain white shield that had won no glory;",
 """'Quorum', 'of whom', the connecting relative. 'primaevus', 'in his first youth'. 'Maeonio regi', 'to the Maeonian king', Maeonia being Lydia in Asia Minor, the king unnamed. 'serva Licymnia', 'the slave Licymnia'. 'sustulerat', 'had borne', 'tollo' used of giving birth. 'vetitis… armis', 'in forbidden arms', framing the line: perhaps because a slave's son had no right to serve. 'ense… nudo', 'with a bare sword', i.e. no spear; 'levis', 'light(-armed)'. 'parma… alba', 'with a white shield', blank, with no device; 'inglorius', 'without glory', since he has done nothing yet to put on it. The sentence breaks off: Helenor is picked up again by 'isque' (549). Elisions 'vetitisqu(e) ad', 'parmaqu(e) inglorius'."""),
(550, 'Latinas:',
 "and he, when himself of Turnus amid the thousands he saw,\non this side lines and on that side lines standing near, Latin ones:",
 "and when he saw himself among Turnus's thousands, Latin ranks standing on this side and Latin ranks on that,",
 """'isque', 'and he', resuming Helenor after the clauses about his birth: the sentence begun at 545 is started again (anacoluthon). 'se… vidit', 'he saw himself (to be)', with 'acies… adstare', 'that lines stood near', accusative and infinitive after 'vidit'. 'Turni media inter milia', 'amid the thousands of Turnus', 'inter' set after its adjective. 'hinc… atque hinc', 'on this side and on that', with 'acies' repeated. 'adstare', Greenough's 'ads-' for 'ast-'. 'Latinas', 'Latin', for all Turnus's Italians. The colon leads into the simile. Elisions 'isqu(e) ubi', 'medi(a) inter', 'atqu(e) hinc'."""),
(555, 'tendit.',
 "as a wild beast which, by the dense of hunters fenced in ring,\nagainst the weapons rages and herself, not unaware, on death\nflings and with a leap above the hunting spears is carried,\nnot otherwise the youth, into the midst, about to die, of the enemy\nrushes in and, where weapons he sees thickest, makes his way.",
 "as a wild beast, hemmed in by a close ring of hunters, rages against their spears and, knowing well what she does, throws herself on death and leaps up onto the hunting spears, so the young man, sure to die, charged into the thick of the enemy and made for the place where he saw the weapons thickest.",
 """'ut fera… haud aliter iuvenis', 'as a wild beast… not otherwise the youth', the simile and its application. 'densa… corona', 'by a dense ring', framing 'venantum saepta', 'fenced in by the hunters'; 'venantum', the shorter genitive plural of the participle ('venantium'). 'haud nescia', 'not unaware', understatement for 'knowing well' (litotes). 'morti… inicit', 'flings onto death', the dative with a verb compounded with 'in-'; 'inicit' has a hidden consonantal i ('in-yicit'). 'supra venabula fertur', 'is carried above the spears', leaps onto them. 'moriturus', 'about to die', the future participle. Homer compares Hector among the Greeks to a lion or boar whose own courage kills it (Iliad 12.41–48). Elision 'sesequ(e) haud'."""),
(558, 'dextras.',
 "But with his feet far better, Lycus, between both the enemy\nand between the arms, in flight the walls makes for, and the high strives\nto grasp top with his hand and of his comrades to touch the right hands.",
 "But Lycus, far faster on his feet, ran through the enemy and through their weapons, reached the wall, and was struggling to catch hold of its top and reach his comrades' outstretched hands.",
 """'pedibus… melior', 'better with his feet', ablative of respect. 'inter et hostis inter et arma', 'between both the enemy and the weapons', the preposition repeated and 'et' set after it; 'hostis', accusative plural in '-is'. 'fuga', 'in flight', ablative. 'muros tenet', 'makes for the walls', 'teneo' of holding a course. 'certat prendere… attingere', 'strives to grasp… to touch'. 'alta… tecta', 'the high top' of the wall, framing 'certat'. 'socium', 'of the comrades', the old genitive plural in '-um' = 'sociorum'. 'dextras', 'right hands', reaching down to pull him up. Elision 'sociumqu(e) attingere'."""),
(560, 'victor:',
 "Him Turnus, alike with running and spear following,\nupbraids with these words, the victor:",
 "Turnus, who had kept up with him both on foot and with his spear, taunted him in triumph:",
 """'Quem', 'him', the connecting relative. 'pariter cursu teloque', 'equally with running and spear', keeping pace with him and keeping him within his spear's reach. 'secutus', 'having followed'. 'increpat', 'upbraids', 'taunts'. 'his', 'with these (words)', ablative. 'victor', 'as victor', already sure of him. The colon introduces the speech. No elisions."""),
(562, 'revellit.',
 "“Our, to escape, madman,\ndid you hope you could, hands?” At once he seizes the man himself\nhanging, and with a great of the wall part tears him away.",
 "“Madman, did you really hope you could get away from these hands of ours?” With that he seized Lycus where he hung and tore him down along with a great piece of the wall.",
 """The print has 'manus? ”Simul', a misprint for 'manus?” Simul', corrected here; so this unit also carries the narrative to its stop. 'Nostrasne… manus', 'our hands?', '-ne' the question particle, framing the question. 'evadere', 'escape', with a direct object. 'sperasti' = 'speravisti', the shortened perfect. 'demens', 'madman', vocative. 'Simul', 'at the same moment'. 'adripit', Greenough's 'adr-' for 'arr-', 'seizes'. 'ipsum pendentem', 'the man himself as he hung', clinging to the top of the wall. 'magna muri cum parte', 'with a great part of the wall', 'cum' set inside its phrase. 'revellit', 'tears away'. Elisions 'Nostrasn(e) evadere', 'pendent(em) et'."""),
(566, 'lupus.',
 "As when either a hare or of gleaming body a swan\nhas carried up, seeking the heights, in its feet Jove's armour-bearer, curved,\nor, sought by its mother with many bleatings, a lamb\nthe wolf of Mars from the stalls has snatched.",
 "So Jove's armour-bearer, the eagle, soaring to the heights, carries off a hare or a white-bodied swan in its hooked talons, or the wolf of Mars snatches from the fold a lamb its mother looks for with long bleating.",
 """'Qualis ubi', 'such as when', a simile with its main clause ('such was Turnus') left to be understood. 'Iovis armiger', 'Jove's armour-bearer', the eagle, which carries his thunderbolts. 'pedibus… uncis', 'in curved feet', 'talons', framing the line. 'sustulit… rapuit', perfects of what happens again and again (the 'gnomic' perfect of similes). 'candenti corpore', 'of gleaming body', ablative of description. 'Martius… lupus', 'the wolf of Mars', the animal sacred to the war-god, father of Romulus. 'matri', dative of the agent with the participle 'quaesitum'; 'balatibus', 'bleatings'. In Iliad 22.308–310 Hector swoops on Achilles like an eagle seizing a lamb or a hare. Elisions 'ub(i) aut', 'lepor(em) aut', 'quaesit(um) aut'."""),
(567, 'tollitur:',
 "On all sides a shout\nis raised:",
 "On every side a shout went up:",
 """'Undique', 'from all sides'. 'clamor tollitur', 'a shout is raised', the Rutulians cheering Turnus's feat and pressing the attack. No elisions."""),
(567, 'complent;',
 "they attack, and the ditches with mound-earth fill;",
 "they charged, and filled the ditches with earth and rubble;",
 """The print has 'agere', a misprint for 'aggere', corrected here: 'agere' ('to drive') gives no sense and does not scan; Greenough prints 'aggere' everywhere else (9.43, 9.769), and the Latin Library has 'aggere'. 'invadunt', 'they attack', 'go in'. 'fossas… complent', 'they fill the ditches', the trenches round the camp, as the Volscians had planned (506). 'aggere', 'with a mound', the heaped earth and rubble used to build up a causeway to the wall, ablative of means. No elisions."""),
(568, 'iactant.',
 "blazing torches others at the roof-tops hurl.",
 "others hurled blazing brands up onto the rooftops.",
 """'ardentis taedas', 'blazing torches', accusative plural in '-is'; 'taeda', pine-wood, then a torch made of it. 'alii', 'others', the second group after those filling the ditches. 'ad fastigia', 'at the tops', the roof-ridges of the buildings and towers inside the wall. Elision 'ali(i) ad'."""),
(572, 'sagitta,',
 "Ilioneus with a rock and a huge fragment of mountain\nLucetius, coming up to the gate and fires carrying,\nEmathion Liger, Corynaeus lays low Asilas,\nthe one with the javelin good, the other with the far-deceiving arrow,",
 "Ilioneus felled Lucetius with a rock, a huge piece broken from a mountain, as he crept up to the gate carrying fire; Liger felled Emathion, and Asilas Corynaeus, the first a fine hand with the javelin, the second with the arrow that strikes unseen from far off;",
 """A list of killings in Homer's manner, one verb, 'sternit', 'lays low', serving every pair (569–576); the long sentence is divided here at a comma. 'saxo atque ingenti fragmine montis', 'with a rock and a huge fragment of a mountain', two names for one weapon. 'portae subeuntem', 'coming up to the gate', the dative with 'subeo'. 'ignis', accusative plural in '-is'. 'Emathiona', a Greek accusative. 'hic… hic', 'this one… that one', Liger and Asilas in order. 'longe fallente', 'deceiving from far', unseen until it hits. Which side Liger and Asilas fight on is not said; a Liger fights for Turnus in Book 10 (10.576), and a Trojan Corynaeus is alive at 12.298, a loose end of the unrevised poem. Elisions 'sax(o) atque', 'atqu(e) ingenti'."""),
(576, 'Capys.',
 "Ortygius Caeneus, the victor Caeneus Turnus,\nTurnus Itys and Clonius, Dioxippus and Promolus\nand Sagaris and, on the high standing before the towers, Idas,\nPrivernus Capys.",
 "Caeneus felled Ortygius, and Turnus Caeneus, the victor; Turnus killed Itys and Clonius, Dioxippus, Promolus and Sagaris, and Idas as he stood out in front of the high towers; and Capys killed Privernus.",
 """The list goes on, 'sternit' (571) still the verb. 'Ortygium Caeneus, victorem Caenea Turnus', the killer becomes the killed in the next breath; 'Caenea', 'Ityn', 'Idan' are Greek accusatives. Caeneus shares his name with the Caeneus of myth, born a woman and made a man, seen among the dead at 6.448. 'Turnus… Turnus', the name repeated at the line's end and start, as his kills pile up. 'summis… pro turribus', 'in front of the high towers', on the Trojan side; 'stantem', 'standing'. Capys, a Trojan companion of Aeneas (1.183), is the founder of Capua in 10.145. Elision 'Sagar(im) et'."""),
(577, 'strinxerat:',
 "Him first the light spear of Themillas\nhad grazed:",
 "Themillas's light spear had grazed Privernus first:",
 """'Hunc', 'him', Privernus. 'primo', 'at first', before Capys's arrow. 'levis hasta Themillae', 'the light spear of Themillas', 'Themillae' the genitive of a first-declension masculine name. 'strinxerat', 'had grazed', from 'stringo', the pluperfect for what came before. The colon leads into what Privernus did next. No elisions."""),
(578, 'tulit;',
 "he his hand, flung away his shield, madly,\nto the wound carried;",
 "and he, like a fool, threw down his shield and put his hand up to the wound;",
 """'ille', 'he', Privernus. 'proiecto tegmine', ablative absolute, 'his covering having been thrown away', 'tegmen' the shield; in 'proiecto' the 'i' is a consonant. 'demens', 'out of his mind', 'madly', an adjective doing the work of an adverb. 'ad volnus tulit', 'carried to the wound', 'volnus' Greenough's old spelling of 'vulnus'. No elisions."""),
(580, 'rupit.',
 "so on its wings, gliding up, an arrow,\nand to the left was pinned side the hand, and hidden within,\nthe breathing-ways of life with a deadly wound it burst.",
 "so an arrow came gliding on its wings, his hand was pinned to his left side, and the arrowhead, buried inside, tore open the passages of his breath with a deadly wound.",
 """'ergo', 'therefore', because he had dropped his shield. 'alis adlapsa sagitta (est)', 'an arrow glided up on its wings', Greenough's 'adl-' for 'all-', 'est' supplied from the next clause; the arrow is Capys's. 'laevo… lateri', 'to the left side', dative, framing 'infixa est'. 'manus', 'the hand', the subject: the arrow pins the hand he had raised to his side. The Latin Library has 'alte' and no 'manus' ('was fixed deep in his left side'), which makes the arrow the subject throughout. 'abdita… intus', 'hidden within', the arrow again, subject of 'rupit'. 'spiramenta animae', 'the breathing-passages of life', the lungs. Elisions 'laev(o) infixa', 'infix(a) est', 'abditaqu(e) intus', 'spirament(a) animae'."""),
(585, 'Palici:',
 "There stood in splendid the son of Arcens arms,\nembroidered with the needle as to his cloak and in rust-red bright, Spanish,\noutstanding in looks; his father had sent him, Arcens,\nreared in the Mother's grove, the Symaethian around\nstreams, where rich and easily appeased is the altar of Palicus:",
 "There stood the son of Arcens in splendid armour, his cloak embroidered with the needle and bright with Spanish crimson, a youth of striking beauty; his father Arcens had sent him to war, brought up in the Mother's grove beside the waters of Symaethus, where the altar of Palicus stands, rich with offerings and quick to be appeased:",
 """'egregiis… armis', 'in splendid arms', framing the line; the son is never named. 'pictus acu chlamydem', 'embroidered (painted with the needle) as to his cloak', the accusative of the thing with a passive participle, as 'pectora' (543). 'ferrugine… Hibera', 'with Spanish rust-colour', a dark red dye. 'eductum', 'brought up'. 'Matris luco', 'in the grove of the Mother', Greenough's reading; which mother is not said. The Latin Library has 'Martis', 'of Mars', which changes the grove's god. 'Symaethia… flumina', the streams of the Symaethus near Etna in Sicily. 'pinguis… et placabilis ara Palici', 'the rich and easily appeased altar of Palicus', one of the Palici, twin gods of Sicily; 'pinguis', rich with sacrifices. Elisions 'chlamyd(em) et', 'ub(i) et'."""),
(589, 'harena.',
 "the whirring sling, laying aside his spears, Mezentius\nhimself three times with drawn-in round his head drove thong,\nand the middle of him facing, with melted, the temples, lead,\nsplit, and at full length stretched him out on much sand.",
 "Mezentius laid down his spears, whirled the whistling sling three times round his head with the strap drawn tight, and split the youth's forehead clean between the temples with the molten lead, and stretched him out full length across the sand.",
 """'positis… hastis', ablative absolute, 'his spears having been laid aside'. 'stridentem fundam', 'the whirring sling', framing the line. 'ter… circum caput egit', 'three times drove (it) round his head', whirled it; 'adducta… habena', ablative absolute, 'with the thong drawn tight'. 'media… tempora', 'the middle of his temples', framing the line, 'adversi', 'of him facing'. 'liquefacto… plumbo', 'with the melted lead', the leaden sling-bullet, which the ancients believed could melt with the speed of its flight. 'diffidit', 'split apart', perfect of 'diffindo'. 'multa… harena', 'on much sand', so large is the body stretched out. 'porrectum', 'stretched out'. Mezentius is the exiled Etruscan tyrant who was bringing fire at 521–522. Elisions 'medi(a) adversi', 'porrect(um) extendit'."""),
(594, 'habebat.',
 "Then for the first time in war his swift aimed arrow,\nit is said, before accustomed to frighten wild beasts, fleeing ones,\nAscanius, and brave by his hand laid low Numanus,\nto whom Remulus as surname was, and of Turnus the younger\nsister, lately in marriage joined, he had to wife.",
 "Then for the first time in war, they say, Ascanius, who had used before only to frighten the timid beasts of the wild, aimed his swift arrow, and with his own hand he brought down brave Numanus, whose surname was Remulus, a man lately joined in marriage to Turnus's younger sister.",
 """A new paragraph in Greenough. 'dicitur… intendisse… fudisse', 'is said to have aimed… to have laid low', the personal construction with the infinitive, 'Ascanius' its subject; the poet tells it as tradition. 'bello', 'in war', unlike the hunt of Silvia's stag (7.496–499). 'solitus', 'having been accustomed', the perfect participle of 'soleo'. 'fugaces', 'fleeing', 'timid'. 'manu', 'with his hand', by his own act. 'cui Remulo cognomen erat', 'to whom the surname was Remulus', the dative of possession with the name drawn into the dative. 'Turnique minorem germanam', 'Turnus's younger sister'. 'thalamo sociatus', 'joined by the marriage-chamber', 'married'. The killing is anticipated here; it comes after his speech. Elision 'celer(em) intendisse'."""),
(597, 'ferebat:',
 "He before the first line things fit and unfit for telling\nshouting, and swollen in his heart with his new royalty,\nwas going, and huge himself with clamour bore along:",
 "Out in front of the first line he went, shouting things fit and unfit to repeat, his heart swollen with pride in his new royal connection, and making himself out a giant with his noise:",
 """'Is', 'he', Numanus. 'primam ante aciem', 'before the first line', 'ante' set after its adjective. 'digna atque indigna relatu', 'things worthy and unworthy in the telling', 'relatu' the supine in '-u' (as 'visu', 465). 'vociferans', 'shouting'. 'tumidus… praecordia', 'swollen as to his heart', the accusative of respect again. 'novo… regno', 'with new royalty', his recent marriage into Turnus's royal house. 'ingentem sese… ferebat', 'was carrying himself huge', swaggering. The colon introduces the speech. Elisions 'prim(am) ante', 'dign(a) atque', 'atqu(e) indigna'."""),
(599, 'muros?',
 "“Does it not shame, by siege a second time and rampart to be hemmed,\ntwice-captured Phrygians, and before death to stretch walls?",
 "“Are you not ashamed, you Phrygians taken twice already, to be shut in again by a siege and a palisade, and to hold up walls between yourselves and death?",
 """Numanus's taunt (598–620) sets Italian hardness against Trojan softness, a contrast Romans liked to draw. 'Non pudet', 'does it not shame (you)', impersonal, with the infinitives 'teneri… praetendere'. 'obsidione… valloque', 'by siege and rampart'. 'bis capti Phryges', 'twice-captured Phrygians', vocative: Troy was taken by Hercules, when Laomedon cheated him, and then by the Greeks; 'Phryges', 'Phrygians', is a sneer, the Trojans as soft Asiatics. 'morti praetendere muros', 'to stretch walls in front of death', the dative: walls as a screen against dying. Elision 'obsidion(e) iterum'."""),
(600, 'poscunt!',
 "Look who our for themselves by war marriages demand!",
 "See who these are, who come to claim our brides by war!",
 """'En', 'look!', pointing. 'qui… poscunt', '(here are the men) who demand', the antecedent understood. 'nostra… conubia', 'our marriages', framing the line: Lavinia, promised to Turnus, whose sister Numanus has married. 'sibi', 'for themselves'. 'bello', 'by war'. No elisions."""),
(602, 'Ulixes:',
 "What god to Italy, what madness of yours drove you?\nNot here are the sons of Atreus, nor of speaking the contriver, Ulysses:",
 "What god, what madness drove you to Italy? Here you will find no sons of Atreus, no Ulysses, that inventor of tales:",
 """The print has no mark after 'adegit' before the capital 'Non', a misprint for 'adegit?', corrected here. 'Quis deus… quae… dementia', 'what god, what madness', two subjects with one singular verb, 'adegit', 'drove'. 'Italiam', 'to Italy', accusative of the place to which, without a preposition. 'Atridae', 'the sons of Atreus', Agamemnon and Menelaus. 'fandi fictor', 'the fashioner of speaking', 'fandi' the genitive of the gerund of 'for', 'speak': Ulysses, the master of lies who devised the wooden horse. Numanus means the Greeks could beat the Trojans only by trickery. Elision 'dementi(a) adegit'."""),
(606, 'cornu.',
 "A hard from the root race, our sons to the rivers first\nwe carry down, and with savage frost harden and with the waters;\nthe hunt they watch over as boys, and the forests weary;\nto turn is their game horses, and arrows to shoot from the horn.",
 "We are a hard race from the root: our newborn sons we first carry down to the rivers and toughen them in the cruel ice and water; as boys they are up all night for the hunt and tire out the forests; their sport is wheeling horses and shooting arrows from the bow.",
 """'durum a stirpe genus', 'a race hard from the stock', in apposition to 'we'. 'natos… deferimus', 'we carry our sons down', newborn, 'primum', 'first of all'. 'saevo… gelu… et undis', 'with savage frost and waters', framing 'duramus', 'we harden'. 'venatu invigilant', 'they keep watch over the hunt', 'venatu' an old dative ('venatui') with 'invigilo'. 'silvas fatigant', 'they weary the forests', by hunting through them. 'ludus (est)', 'their game is', with the infinitives 'flectere… tendere' as subject. 'spicula', 'arrows'; 'cornu', 'from the horn', the bow, made of horn. Elisions 'dur(um) a', 'venat(u) invigilant'."""),
(608, 'bello.',
 "But enduring of toil and to little accustomed, our youth\neither with hoes the earth tames or shakes towns in war.",
 "Our young men, patient of hard work and used to little, either break the soil with the hoe or shake towns with war.",
 """'patiens operum', 'enduring of toils', 'patiens' with the genitive, as an adjective. 'parvo… adsueta', 'accustomed to little', dative, Greenough's 'ads-' for 'ass-'. 'iuventus', 'youth', the young men collectively. 'aut… aut', 'either… or': farming and war, the two Roman virtues. 'rastris', 'with hoes', heavy rakes for breaking clods. 'domat', 'tames'. 'quatit oppida bello', 'shakes towns with war'. Elision 'parvoqu(e) adsueta'."""),
(610, 'hasta;',
 "All our lifetime by iron is worn, and with reversed of bullocks\nthe backs we weary, spear;",
 "Our whole life is spent with iron in our hands: we goad the backs of our bullocks with the butt-end of a spear;",
 """'Omne aevum ferro teritur', 'every age is worn away with iron', the whole of life, young and old, spent with weapons or tools. 'versa… hasta', 'with spear reversed', framing the line and a half: they drive their oxen with the butt of the spear, never putting it down. 'iuvencum', 'of bullocks', the old genitive plural ('iuvencorum'); its 'i' is a consonant, so 'versaque' does not elide into it. 'terga fatigamus', 'we weary the backs'. Elision 'Omn(e) aevum'."""),
(611, 'vigorem:',
 "nor slow old age\nweakens the strengths of our spirit, or changes the vigour:",
 "nor does slow old age weaken the strength of our spirit or alter its vigour:",
 """'nec… -que', 'neither… nor'. 'tarda senectus', 'slow old age', slow-moving, or slow to come. 'debilitat', 'weakens'. 'vires animi', 'the strength of the spirit'; 'vires' Greenough's spelling, 'viris' the Latin Library's, the same word. 'vigorem', 'vigour'. No elisions."""),
(613, 'rapto.',
 "our white hair with the helmet we press, and always fresh\nto carry home pleases plunder, and to live on what is seized.",
 "we press the helmet on our grey hair, and it is always our joy to bring home fresh plunder and to live by what we take.",
 """'canitiem', 'whiteness', the white hair of age. 'galea premimus', 'we press with the helmet'. 'recentis… praedas', 'fresh plunder', framing 'comportare iuvat', 'it pleases to carry together'; 'recentis' accusative plural in '-is'. 'vivere rapto', 'to live on what is seized', 'rapto' the neuter participle used as a noun, ablative of means. Raiding was an honourable trade in early Italy as in Homer's Greece. No elisions."""),
(616, 'mitrae.',
 "You have robes embroidered with saffron and gleaming purple,\nidleness is to your hearts, it pleases to indulge in dances,\nand your tunics have sleeves and ribbons your caps.",
 "You wear clothes embroidered with saffron and shining purple; your hearts are set on idleness, you love to give yourselves up to dances, and your tunics have sleeves and your bonnets ribbons.",
 """'Vobis… vestis (est)', 'to you is clothing', the dative of possession, 'est' understood. 'picta croco', 'embroidered with saffron', yellow. 'fulgenti murice', 'with gleaming purple', the dye from the murex shellfish. 'desidiae cordi (est)', 'idleness is to your heart', 'cordi' a predicative dative, 'dear to you'. 'indulgere choreis', 'to give yourselves to dances', the dative. 'et… et', the first 'et' linking the clause, the second joining 'tunicae' and 'mitrae' as subjects of 'habent'; 'manicas', 'sleeves', to Romans a mark of softness. 'redimicula', 'ribbons', tying the 'mitra', the Phrygian bonnet, under the chin. Elision 'croc(o) et'."""),
(618, 'cantum!',
 "O truly Phrygian women, for not Phrygian men, go over high\nDindymus, where to the accustomed the double-mouthed gives the pipe music!",
 "Phrygian women, that is what you truly are, not Phrygian men! Go off over high Dindymus, where the double pipe plays the music you know so well!",
 """'O vere Phrygiae', 'O truly Phrygian women', the feminine; 'neque enim Phryges', 'for (you are) not Phrygian men'. The insult goes back to Thersites in Iliad 2.235, calling the Greeks 'Achaean women, no longer Achaean men'. 'ite', 'go', imperative. 'alta Dindyma', 'lofty Dindymus', a neuter plural name, a mountain in Phrygia sacred to Cybele. 'adsuetis', 'to those accustomed', dative. 'biforem… cantum', 'two-mouthed music', framing the clause: the Phrygian double pipe, one reed for each hand, used in Cybele's rites. Elisions 'nequ(e) enim', 'Dindym(a) ubi'."""),
(620, 'ferro.”',
 "Drums you and the boxwood call, Berecyntian, of the Mother,\nthe Idaean; leave arms to men and give way to the steel.”",
 "The drums and the Berecyntian flute of the Idaean Mother are calling you; leave weapons to men and give way to the sword.”",
 """The print has no mark after 'Idaeae' before 'sinite', a misprint for a stop (a semicolon is read here), corrected here. 'Tympana… buxusque… Berecyntia', 'drums and Berecyntian boxwood', the flute made of boxwood, with one singular verb, 'vocat'. Berecyntus is a mountain in Phrygia sacred to Cybele. 'Matris Idaeae', 'of the Idaean Mother', Cybele, worshipped on Mount Ida near Troy, whose rites, with drums and pipes, were performed by eunuch priests; hence the sneer. 'sinite arma viris', 'leave arms to men', 'viris' dative. 'cedite ferro', 'yield to the steel'. Numanus's speech ends; Ascanius answers with an arrow in the next part. Elision 'sinit(e) arma'."""),
]

P = A.part('aeneid-069'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units')
