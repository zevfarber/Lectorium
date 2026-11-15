# aeneid-077 (X.439-509): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Pallantis mors. Balteus'
PART = "The Death of Pallas (X.439–509)"
TITLE_EN = "The Death of Pallas — Aeneid X.439–509"
ABOUT = ("Turnus's sister warns him to go to the help of Lausus, and he drives his chariot through the battle. He orders his "
"men off the field: Pallas is his, and his alone, and he wishes Evander were there to watch. Pallas, undaunted, answers that "
"he will be praised either for the richest spoils or for a glorious death, and that his father can bear either outcome. "
"Turnus leaps down and comes on like a lion charging a bull. Pallas prays to Hercules, once his father's guest, to help "
"him win; Hercules hears him and weeps, knowing he can do nothing, and Jupiter consoles his son: every man's day is fixed, "
"and the work of courage is to lengthen one's name by deeds. Pallas's spear only grazes Turnus; Turnus's goes through "
"shield, corselet and chest. Standing over the body, Turnus sends Pallas back to Evander dead, grants him a grave, and "
"strips off his heavy sword-belt, engraved with the murder of the bridegrooms on their wedding night. The poet breaks in: "
"the day will come when Turnus will wish he had never touched Pallas, and will hate that belt. The Arcadians carry Pallas "
"home on his shield, a great grief to his father and a great glory, given to war and taken by it on the same first day.")

U = [
(440, 'agmen.',
 """Meanwhile his sister, kindly, warns to go to the aid of Lausus\nTurnus, who in his winged chariot the middle cuts of the column.""",
 """Meanwhile his gentle sister warned Turnus to go to the help of Lausus, and he cut through the middle of the battle in his flying chariot.""",
 """A new paragraph in Greenough. 'soror alma', 'his kindly sister', is the nymph Juturna, who is only named later and plays a large part in Book XII. 'monet succedere', 'warns (him) to come up', with the infinitive; 'succedere Lauso', 'to relieve Lausus', dative with a compound verb: Lausus is fighting Pallas (last part). 'volucri curru', 'in his winged chariot', ablative of means. 'medium… agmen', 'the middle of the column', the adjective where English uses a noun. 'secat', 'cuts'. Jupiter has just said that Pallas and Lausus will fall to greater enemies (438): here the first of those enemies arrives. No elisions."""),
(443, 'adesset.”',
 """When he saw his comrades: “Time to cease from the fight;\nalone I against Pallas am borne, to me alone Pallas\nis owed; I could wish his father himself were here to watch.”""",
 """When he reached his comrades, he cried, “It is time to leave off fighting; I go against Pallas alone; Pallas is owed to me and no one else; I only wish his father were here himself to see it.”""",
 """'Ut vidit', 'when he saw', 'ut' with the perfect indicative. 'Tempus (est) desistere', 'it is time to cease'; 'pugnae', dative with 'desisto', a poetic construction. 'in Pallanta feror', 'I am borne against Pallas', the passive in a middle sense, 'I rush'; 'Pallanta' is the Greek accusative. 'solus… soli', the same word twice (polyptoton): Turnus claims the kill as his right. 'cuperem… adesset', 'I could wish (that) he were present', a potential subjunctive with a wish-clause without 'ut'; 'parens… spectator', 'his father as onlooker', Evander. The wish is cruel, and the reader remembers it when the poet turns to the grieving father at the end of the part. Elisions 'eg(o) in', 'cuper(em) ipse'."""),
(444, 'iusso.',
 """This he says, and his comrades withdrew from the plain as ordered.""",
 """So he spoke, and his comrades drew back from the field as they were told.""",
 """'Haec ait', the formula that closes a speech, as you have seen many times. 'cesserunt', 'withdrew', a perfect after the present 'ait'. 'aequore iusso', 'from the plain ordered', ablative of separation: the ground they were ordered to leave, the participle carrying the command (literally 'the ordered plain'). 'aequor', properly any level surface, sea or plain, is often the open battlefield in these books. No elisions."""),
(448, 'tyranni:',
 """But at the Rutulians' withdrawal the young man then, at the commands haughty\nmarvelling, stands amazed at Turnus, and over the body huge\nhis eyes he rolls, and goes over from afar all with fierce gaze,\nand with such words goes against the words of the tyrant:""",
 """But the young man, amazed at the Rutulians' withdrawal and at that haughty order, stood staring at Turnus, ran his eyes over that huge frame, surveyed every part of him from a distance with a fierce look, and answered the tyrant's words with these:""",
 """'At' turns to Pallas. 'Rutulum abscessu', 'at the withdrawal of the Rutulians', 'Rutulum' = 'Rutulorum', the old genitive plural. 'iuvenis', Pallas. 'iussa superba miratus', 'wondering at the proud commands'. 'stupet in Turno', 'is struck dumb at Turnus'. 'corpus… per ingens lumina volvit', 'rolls his eyes over the huge body', the preposition set between adjective and noun. 'obit', 'goes round', looks over; 'truci… visu', 'with a fierce gaze'. 'it contra dicta', 'goes against the words', answers them. 'tyranni', 'the tyrant's': 'tyrannus' is a Greek word for a king, with a hostile edge in Pallas's mouth. Elision 'Rutul(um) abscessu'."""),
(451, 'minas.',
 """“Either for spoils I, now seized, shall be praised, the richest,\nor for a death renowned: to either lot my father is equal.\nAway with threats.”""",
 """“I shall be praised either for winning the richest spoils or for a glorious death: my father can bear either fate. Enough of your threats.”""",
 """The print has 'minas. ”Fatus', a misprint for 'minas.” Fatus', corrected here. The closing speech mark has slipped onto the next word; since the cut can only fall where the printed characters allow, the stray mark begins the next unit's text, and the speech is closed here in the English. 'spoliis… raptis… opimis', 'for spoils taken, the richest', ablative of cause; 'spolia opima' were properly the armour a Roman commander stripped from an enemy commander he had killed himself. 'leto insigni', 'for a famous death'. 'sorti… aequus utrique', 'equal to either lot': the answer to Turnus's wish (443). 'Tolle minas', 'take away your threats'. Elisions 'let(o) insigni', 'utriqu(e) est'."""),
(451, 'aequor.',
 """Having spoken, into the middle he advances of the plain.""",
 """With that he strode out into the middle of the field.""",
 """The closing speech mark printed at the head of this unit belongs to Pallas's speech (see the note before). 'Fatus', 'having spoken', the perfect participle of the deponent 'for', used with present sense. 'medium… in aequor', 'into the middle of the plain', the open ground the Rutulians have cleared. 'procedit', 'goes forward'. No elisions."""),
(452, 'sanguis.',
 """Cold for the Arcadians gathers into their hearts the blood.""",
 """The blood ran cold and gathered about the hearts of the Arcadians.""",
 """'Frigidus… sanguis', 'the cold blood', framing the line: fear was thought to draw the blood inward and chill it. 'Arcadibus', dative of reference, 'for the Arcadians', where English uses a possessive. 'coit', 'comes together, curdles'. 'praecordia', 'the parts about the heart'. They fear for Pallas as he walks out alone to meet Turnus. No elisions."""),
(454, 'comminus;',
 """Down leapt Turnus from his two-horse car, on foot he prepares to go\nhand to hand;""",
 """Turnus leapt down from his chariot and made ready to meet him on foot, at close quarters;""",
 """'Desiluit', 'leapt down', perfect, the quick act, then 'apparat', present. 'biiugis', 'from the pair-horse chariot', ablative of separation, three syllables with the second 'i' a consonant, as at 400 in the last part. 'pedes', nominative singular of 'pedes, peditis', 'a man on foot', not 'pedes', 'feet'. 'comminus', 'at close quarters', held over to the next line. No elisions."""),
(456, 'imago.',
 """and as a lion, when from a watch-place high he has seen\nstanding far off on the plains, pondering battle, a bull,\nflies at him: not other is the look of Turnus coming.""",
 """and as a lion that has seen from a high lookout a bull standing far off on the plain, brooding on battle, comes flying at it, just so did Turnus look as he came on.""",
 """The simile. 'utque leo', 'and as a lion'; 'specula… ab alta', 'from a high watch-point'. 'cum vidit', 'when he has seen', with the accusative and infinitive 'stare… taurum'. 'meditantem in proelia', 'thinking on battles', the bull too is ready to fight. 'advolat', 'flies at', stopped by the colon. 'haud alia', 'not otherwise', closes the simile; 'imago', 'the appearance'. When Patroclus kills Sarpedon in the Iliad, Homer compares him to a lion falling on a bull in a herd (Iliad 16.487–489); Sarpedon will be named in this part. Elisions 'meditant(em) in', 'ali(a) est'."""),
(459, 'fatur:',
 """Him when within reach of a thrown he believed would be spear,\nto go first Pallas, if any chance might help him having dared\nwith strength unequal, and to the great sky thus he speaks:""",
 """When Pallas judged that Turnus would be within a spear's throw, he moved first, hoping that chance might somehow help a man who had dared with unequal strength, and spoke thus to the vast sky:""",
 """'Hunc', Turnus. 'ubi… credidit', 'when he believed'; 'contiguum… fore', 'would be within reach', with 'missae… hastae', dative, 'of a thrown spear'. 'ire prior Pallas', 'Pallas goes first', a historic infinitive in place of a main verb. 'siqua' = 'si qua', 'if in any way', Greenough printing it as one word: 'if chance should help him'; the subjunctive 'adiuvet' gives Pallas's hope. 'ausum', 'having dared', him who dared. 'viribus imparibus', 'with unequal strength', ablative: he knows he is overmatched. 'aethera', Greek accusative. Elisions 'magnumqu(e) ita', 'it(a) ad'."""),
(461, 'adsis.',
 """“By my father's guest-welcome and the tables, which as a stranger you came to,\nI pray you, Alcides, to my undertakings great be present.""",
 """“By the welcome my father gave you, by the table you came to as a stranger, I pray you, Hercules, stand by me in this great venture.""",
 """Pallas prays to Hercules, called 'Alcides', 'descendant of Alcaeus', his grandfather. In Book VIII Evander tells how Hercules came to his settlement, killed the monster Cacus and was welcomed and honoured there; hence 'patris hospitium et mensas', 'my father's hospitality and tables'. 'advena', 'as a newcomer'. 'adisti' = 'adiisti', 'you came to'. 'te precor… adsis', 'I pray you to be present', the subjunctive without 'ut' after a verb of asking; 'adsis' is Greenough's spelling of 'assis'. 'coeptis ingentibus', dative, 'to my great enterprise'. Elisions 'hospiti(um) et', 'adven(a) adisti'."""),
(463, 'Turni.”',
 """Let him see me from himself, half-dead, tear the arms bloody,\nand me as victor let them bear, the dying eyes of Turnus.”""",
 """Let Turnus see me strip the bloody armour from him as he lies half-dead, and let his dying eyes endure the sight of me as victor.”""",
 """'Cernat', 'let him see', a jussive subjunctive, as is 'ferant'. 'semineci sibi', 'from himself half-dead', a dative of separation with 'rapere': 'semineci' is from 'semineci-s', 'half-dead'. 'arma cruenta', 'the bloody armour'. 'victorem… ferant', 'let them bear me as victor', endure the sight of me. 'morientia lumina', 'dying eyes'. Pallas wishes on Turnus exactly what is about to happen to himself, armour and all. The speech ends. Elision 'raper(e) arma'."""),
(465, 'inanis.',
 """Heard Alcides the youth, and a great beneath the deepest\nheart he holds down groan, and tears pours out useless.""",
 """Hercules heard the young man; deep in his heart he held back a heavy groan, and shed tears that could do no good.""",
 """'Audiit' = 'audivit', the perfect without its 'v'. 'magnum… gemitum', 'a great groan', framing the next line and a half. 'sub imo corde premit', 'presses down beneath the bottom of his heart', as Aeneas 'premit altum corde dolorem' at I.209. 'lacrimas… inanis', 'useless tears', accusative plural in '-is': he can do nothing for Pallas against fate. In the Iliad Zeus, unable to save his son Sarpedon, sheds tears of blood (Iliad 16.459–461); Virgil divides the scene between Hercules, who weeps, and Jupiter, who explains. Elision 'lacrimasqu(e) effundit'."""),
(466, 'amicis:',
 """Then the Father his son with words addresses friendly:""",
 """Then the Father spoke to his son with words of comfort:""",
 """'Genitor', 'the Father', Jupiter, capitalised as a name; Hercules is his son by Alcmena. 'natum', 'his son'. 'dictis… amicis', 'with friendly words', ablative of means, framing the verb. 'adfatur', 'addresses', Greenough's spelling of 'affatur'. The colon introduces the speech. No elisions."""),
(469, 'opus.',
 """“Stands for each his own day, short and beyond repair the time\nfor all is of life: but fame to extend by deeds,\nthis is of valour the work.""",
 """“Every man has his appointed day; for all men the span of life is short, and once gone it can never be restored; but to make one's name outlast one by what one does, that is what courage is for.""",
 """'Stat', 'stands fixed', set first: the day of death cannot be moved. 'sua cuique', 'to each his own', the reflexive referring to 'cuique'. 'dies', here feminine, as often when it means a fixed day. 'inreparabile', 'that cannot be got back', Greenough's spelling of 'irreparabile'. 'omnibus est vitae', 'is for all, of life'. 'famam extendere factis', 'to extend fame by deeds', the infinitive phrase the subject, taken up by 'hoc'. 'virtutis opus', 'the task of manhood', 'virtus' being the courage and worth of a man. Elisions 'brev(e) et', 'fam(am) extendere'."""),
(471, 'progenies.',
 """Troy beneath the walls high\nso many sons fell of gods; nay, there fell along with them\nSarpedon, my offspring.""",
 """Beneath the high walls of Troy so many sons of gods fell; why, my own child Sarpedon fell with them.""",
 """'Troiae sub moenibus altis', 'under the high walls of Troy'. 'nati… deum', 'sons of gods', 'deum' = 'deorum', the old genitive plural. 'cecidere' = 'ceciderunt'. 'quin', 'nay, more'. 'una', an adverb, 'together', 'along with them'. Sarpedon, king of the Lycians and son of Zeus, was killed by Patroclus; Zeus wished to save him and was talked out of it by Hera, since gods' sons too must die (Iliad 16.431–461). 'mea progenies', 'my offspring', held back to the end. No elisions."""),
(472, 'aevi.”',
 """Even his own Turnus\nfates call, and the goal of his given he has reached, of life.”""",
 """Turnus too is called by his own fate, and has come to the turning-post of his allotted time.”""",
 """'Etiam', 'even, also', Turnus too. 'sua… fata', 'his own fates', split across the line. 'metas… dati… aevi', 'the turning-posts of his given lifetime': the 'metae' marked the end of a chariot course, and so the end of anything. 'pervenit ad', 'arrives at', present tense: he is already near it. Jupiter's speech, like the poet's forecast at 438, looks far ahead: Turnus will die at Aeneas's hands at the poem's close. The speech ends. No elisions."""),
(473, 'arvis.',
 """Thus he speaks, and his eyes from the Rutulians' fields turns away.""",
 """So he spoke, and turned his eyes away from the fields of the Rutulians.""",
 """'Sic ait', closing the speech. 'reicit', Greenough's spelling of 'reiicit' ('re' + 'iacio'), three syllables with the first long, 'casts back'. 'oculos… reicit arvis', 'turns his eyes away from the fields', 'arvis' taken as an ablative of separation: Jupiter will not watch what follows. Some take 'arvis' as dative and the line to mean that he turns his eyes back to the battlefield; the sense of turning away fits his grief better. Elision 'atqu(e) oculos'."""),
(475, 'ensem.',
 """But Pallas with great strength hurls his spear\nand from the scabbard hollow the flashing snatches sword.""",
 """Then Pallas hurled his spear with all his strength and snatched his flashing sword from its hollow scabbard.""",
 """'magnis… viribus', 'with great strength', framing the verb, ablative of manner. 'emittit', 'sends out', launches. 'vagina… cava', 'from the hollow scabbard', ablative of separation, joined by '-que'. 'deripit', 'snatches off', the same verb Halaesus used of a hand at 415. He throws and draws in one motion, ready to close in. No elisions."""),
(478, 'Turni.',
 """It, flying, where of the shoulder rise the coverings top,\nfalls, and a way through the shield's edges having toiled out,\nat last even grazed from the great body of Turnus.""",
 """The spear flew and struck where the top of the shoulder-armour rises, forced its way through the rim of the shield, and in the end did no more than graze Turnus's mighty body.""",
 """'Illa', the spear. 'umeri surgunt qua tegmina summa', 'where the topmost coverings of the shoulder rise', in prose order 'qua summa tegmina umeri surgunt'. 'incidit', 'falls on'. 'viam… molita', 'having laboured out a way', the perfect participle of the deponent 'molior'. 'clipei… per oras', 'through the rims of the shield'. 'tandem etiam… strinxit', 'at last even grazed', a scratch for all that effort; the object is left out (some skin, a little blood). 'magno… de corpore Turni', 'from the great body of Turnus', his size stressed again. Elision 'tand(em) etiam'."""),
(480, 'fatur:',
 """Then Turnus with iron, tipped, the oak with sharp\nat Pallas, long poising, hurls, and thus he speaks:""",
 """Then Turnus, after long poising his oaken spear with its sharp iron point, hurled it at Pallas and said:""",
 """'Hic', 'at this', 'then'. 'robur', 'oak', the oaken shaft; 'ferro praefixum… acuto', 'tipped in front with sharp iron'. The words interlock: 'ferro… acuto' frames 'praefixum robur'. 'in Pallanta', 'at Pallas', Greek accusative. 'diu librans', 'long balancing': Turnus takes his time, where Pallas threw at once. 'iacit… fatur', two presents joined by 'atque'. Elision 'atqu(e) ita'."""),
(481, 'telum.”',
 """“Look whether more be ours piercing the spear.”""",
 """“See now whether my spear is not the better at piercing.”""",
 """'Adspice', Greenough's spelling of 'aspice', 'look'. 'num… sit', 'whether it is', an indirect question: a taunt, since Pallas's spear only grazed. 'mage' = 'magis', 'more', an old form kept in verse. 'nostrum', 'our', the plural for 'my'. 'penetrabile', here active, 'piercing', though the word usually means 'that can be pierced'. The words are spoken as the spear flies. No elisions."""),
(485, 'ingens.',
 """He had spoken; but the shield, so many layers of iron, so many of bronze,\nwhich hide so many times goes round, wrapped about, of bull,\nwith quivering the point in the middle pierces through stroke,\nand of the corselet the hindrances and the breast perforates huge.""",
 """He had spoken; and the quivering point struck the shield in the middle and drove straight through it, for all its layers of iron and bronze and the bull's hide wrapped round it fold upon fold, then pierced the barrier of the corselet and the great chest.""",
 """'Dixerat', 'he had spoken', the pluperfect that so often closes a speech. 'tot ferri terga, tot aeris', 'so many backs of iron, so many of bronze', in apposition to 'clipeum': 'terga', properly 'hides', is used of the layers of a shield. 'quem pellis… obeat', 'which bull's hide goes round', the subjunctive giving the clause the force of 'though'. 'vibranti… ictu', 'with a quivering stroke', framing the line. 'loricae… moras', 'the delays of the corselet', what should have stopped the spear. In the Iliad Hector's spear goes through six of the seven layers of Ajax's shield and stops at the last (Iliad 7.245–248); nothing stops Turnus's. No elisions."""),
(486, 'telum:',
 """He snatches the warm, in vain, from the wound weapon:""",
 """Pallas tore the warm spear from the wound, but it was no use:""",
 """'Ille', Pallas. 'calidum… telum', 'the warm weapon', framing the line, warm with his blood. 'frustra', 'in vain'. 'de volnere', 'from the wound', Greenough's 'volnus' for 'vulnus' (the old spelling, as in 'divom'). The colon introduces why it was useless. No elisions."""),
(487, 'sequuntur.',
 """by one and the same way blood and life follow.""",
 """his blood and his life came out together by the same road.""",
 """'una eademque via', 'by one and the same way', ablative of the route. 'sanguis animusque', 'blood and life', 'animus' here the breath of life; '-que' joins them. 'sequuntur', 'follow': they follow the spear out of the wound. Elision 'un(a) eademque'."""),
(489, 'cruento.',
 """He falls forward onto the wound, a sound over him his arms gave,\nand the earth hostile, dying, he seeks with mouth bloody.""",
 """He fell forward onto his wound, his armour clashed over him, and in death he struck the enemy's earth with a bloody mouth.""",
 """'Corruit in volnus', 'he falls headlong on his wound'. 'sonitum super arma dedere', 'his arms gave a sound over him', Homer's formula for a fallen warrior, 'and his armour rang upon him' (Iliad 4.504 and often). 'dedere' = 'dederunt'. 'terram hostilem… petit ore cruento', 'seeks the enemy's earth with bloody mouth', another Homeric picture, men who 'bite the earth' as they fall (Iliad 2.418; 11.749); 'hostilem' adds that Pallas dies on the enemy's ground, far from home. Elision 'terr(am) hostilem'."""),
(492, 'Euandro;',
 """Over whom Turnus standing,\n“Arcadians, these, he says, mindful my words carry back\nto Evander;""",
 """Turnus stood over him and said, “Arcadians, remember these words of mine and take them back to Evander:""",
 """Line 490 is a half-line, one of the many unfinished lines (more than fifty) left in the poem at Virgil's death, as 284 earlier in this book. 'Quem', the connecting relative, 'him', Pallas. 'super adsistens', 'standing over', 'adsistens' Greenough's spelling of 'assistens'. Greenough prints 'inquit' inside the speech marks, as is his habit; it is not part of what Turnus says. 'memores… referte', 'carry back, remembering'. 'Euandro', Greenough's spelling here of Evander's name (Greek 'Euandros'), dative. No elisions."""),
(492, 'remitto.',
 """such as he deserved, Pallas I send back.""",
 """I send him back his Pallas, in the state he deserved.""",
 """'qualem meruit', 'such as he deserved', Evander the subject: Turnus sends the son back dead, the reward he says Evander has earned by taking Aeneas's side. 'Pallanta', Greek accusative. 'remitto', 'I send back', the present for the immediate future. The words are spoken to Pallas's own men. No elisions."""),
(494, 'largior.',
 """Whatever honour of a tomb, whatever comfort of burying there is,\nI grant freely.""",
 """Whatever honour lies in a tomb, whatever comfort there is in burial, I give him freely.""",
 """'Quisquis honos tumuli', 'whatever honour (there is) of a tomb'. 'quidquid solamen humandi est', 'whatever comfort of burying there is', 'humandi' a gerund in the genitive. 'largior', 'I bestow generously', a deponent, held over to the next line and stopped short. Turnus lets the Arcadians take the body home for burial, which Homer's heroes did not always grant, but he keeps the belt. Elision 'humand(i) est'."""),
(495, 'hospitia.',
 """Not for him will stand, the Aeneian, at little\nwelcome.”""",
 """His welcome to Aeneas will cost him dear.”""",
 """The print has 'hospitia. ”Et', a misprint for 'hospitia.” Et', corrected here. The closing speech mark has slipped onto the next word, so, as at line 451, it begins the next unit's text, and the speech is closed here in the English. 'Haud… stabunt… parvo', 'will not stand at a small price', 'stare' with the ablative of price meaning 'to cost'. 'illi', Evander. 'Aeneia hospitia', 'the Aeneian guest-friendship', his alliance with Aeneas; 'Aeneia', four syllables, is the adjective from 'Aeneas'. Elision 'hospiti(a) et', across the stop."""),
(499, 'auro;',
 """And with left he pressed foot, such things having said,\nthe lifeless one, tearing away the huge weight of the belt\nand the crime stamped on it, on one night of wedlock\nslaughtered a band of young men foully and the bridal chambers bloody,\nwhich Clonus son of Eurytus in much had engraved gold;""",
 """With these words he set his left foot on the lifeless body and tore away the heavy sword-belt with the crime embossed on it, a band of young bridegrooms foully murdered on a single wedding night and their chambers drenched in blood, which Clonus, son of Eurytus, had engraved in rich gold;""",
 """The closing speech mark at the head of this unit belongs to Turnus's speech (see the note before). 'laevo pressit pede', 'pressed with his left foot', to hold the body down while he pulls, as Patroclus sets his heel on Sarpedon to draw out his spear (Iliad 16.503–504). 'exanimem', 'the lifeless (body)'. 'baltei', 'of the belt', two syllables (synizesis): the 'balteus' carried the sword. 'impressum nefas', 'the impious deed embossed': the fifty daughters of Danaus, married against their will to their cousins the sons of Aegyptus, killed their husbands on the wedding night. 'caesa manus… thalamique cruenti', in apposition to 'nefas'. 'Clonus Eurytides', a craftsman known only here. No elisions."""),
(500, 'potitus.',
 """in which now Turnus exults, spoil, and rejoices having won it.""",
 """and now Turnus exults in this spoil and glories in having won it.""",
 """'quo… spolio', 'in which spoil', the relative attracted into agreement with the noun it introduces; ablative with 'ovat' and with 'potitus'. 'ovat', 'exults', as a general does at an ovation, the lesser triumph. 'potitus', 'having got possession of', from the deponent 'potior', which takes the ablative. 'nunc', 'now', set against the time to come in the next lines. Pallas had hoped to strip Turnus (462); it is Turnus who strips Pallas. No elisions."""),
(502, 'secundis!',
 """Ignorant, the mind of men, of fate and of lot to come,\nand of keeping measure, by circumstances lifted up favourable!""",
 """How blind the minds of men are to fate and to what lies ahead, and how unable to keep within bounds when good fortune raises them high!""",
 """The poet speaks in his own voice. 'Nescia', 'not knowing', with genitives, 'fati sortisque futurae', 'of fate and of the lot to come', and then with an infinitive, 'servare modum', 'how to keep measure'. 'mens hominum', 'the mind of men', singular for all. 'sublata', 'lifted up', perfect participle of 'tollo'. 'rebus… secundis', 'by favourable things', ablative, prosperity. When Hector puts on the armour he stripped from Patroclus, Zeus pities him in the same spirit, for he has no thought of the death that is near (Iliad 17.198–208). No elisions."""),
(505, 'oderit.',
 """For Turnus a time will be, when at a great price he will wish bought\nuntouched Pallas, and when those spoils and the day\nhe will hate.""",
 """A time will come for Turnus when he would give a great price to have left Pallas untouched, when he will hate those spoils and this day.""",
 """'Turno tempus erit', 'there will be a time for Turnus', dative of possession. 'magno… emptum', 'bought at a great price', ablative of price: he will wish he could buy back the deed, 'intactum Pallanta', Pallas unharmed. 'optaverit… oderit', future perfects; 'odi', 'I hate', has only perfect forms, with present meaning, so 'oderit' is simply 'he will hate'. 'ista', 'those', with a note of scorn. At the poem's end Aeneas sees this belt on Turnus's shoulder and kills him for it (XII.940–952). Elisions 'c(um) optaverit', 'Pallant(a) et', 'spoli(a) ista'."""),
(506, 'frequentes.',
 """But his comrades with much groaning and tears\nlaid on a shield carry back Pallas, thronging.""",
 """But his comrades, crowding round, with loud lament and many tears, laid Pallas on his shield and carried him back.""",
 """'At' turns from Turnus to the Arcadians. 'multo gemitu lacrimisque', 'with much groaning and tears', ablative of manner. 'impositum scuto', 'placed on a shield', 'scuto' dative with the compound participle: a warrior's shield served as his bier. 'referunt', 'carry back'. 'frequentes', 'in crowds', all of them together. No elisions."""),
(509, 'acervos.',
 """O grief and glory great, you who will return to your father!\nThis first day gave you to war, this same takes you away,\nwhile yet huge of Rutulians you leave heaps.""",
 """O you who will go home to your father, his great grief and his great glory! This day, your first, gave you to war, and this same day takes you away, though you leave behind you great heaps of Rutulian dead.""",
 """The poet turns to address Pallas (apostrophe), as he did at 411. 'dolor atque decus magnum', 'grief and great glory', in alliteration, nominatives in exclamation; 'rediture', future participle in the vocative, 'you who are to return'. 'parenti', dative, Evander. Greenough prints no comma after 'parenti'; the sense is the same. 'haec… haec eadem', 'this… this same', the repetition (anaphora) setting the gift and the loss side by side. 'cum tamen', 'while all the same'; 'ingentis… acervos', accusative plural in '-is'. Elision 'eade(m) aufert'."""),
]

# Misprints (rule 5b): 10.451 'minas. ”Fatus' and 10.495 'hospitia. ”Et' print the closing speech mark joined to the
# next word. t keeps the print; the unit ending at 'minas.' / 'hospitia.' closes the speech in l and i; the stray ”
# begins the next unit's t, whose l and i carry no mark. Mark balance is checked over each pair, as in aeneid-075.
PAIRS = {449: 451, 494: 495}
P = A.part('aeneid-077'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
