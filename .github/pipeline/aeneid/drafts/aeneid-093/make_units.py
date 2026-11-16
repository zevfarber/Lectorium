# aeneid-093 (XII.216-310): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Augurium. Foedus ruptum'
PART = "The Omen and the Broken Treaty (XII.216–310)"
TITLE_EN = "The Omen and the Broken Treaty — Aeneid XII.216–310"
ABOUT = ("The treaty has been sworn and the victims killed, but the Rutulians, watching their champion, begin to think the duel unequal: Turnus comes to the altar with silent step and lowered eyes, pale and wasted. "
"His sister Juturna sees the crowd wavering and goes among the ranks in the likeness of Camers, a warrior of famous family, and sows rumours: is it not shameful to let one man die for them all, when the whole enemy army is hardly a match for them, and to sit idle now only to serve proud masters later? "
"The Italians' mood turns; they want war, and pray that the treaty may be undone. "
"Then Juturna sends an omen from the sky: Jupiter's eagle swoops on a flock of shore birds and carries off a swan, until the whole flock turns, darkens the sky and drives it to drop its prey. "
"The augur Tolumnius greets the sign as the answer to his prayers, calls the Italians to arms and hurls the first spear, which kills one of nine Arcadian brothers. "
"The truce collapses into battle. The altars are stripped, Latinus flees with his gods, and the fighting spreads round the very place of the sacrifice: Messapus kills the Etruscan king Aulestes on the altar and calls him a better victim for the gods, Corynaeus sets an enemy's beard alight with a brand from the altar, and the shepherd Alsus splits Podalirius's head with an axe. "
"The breaking of a sworn truce by an arrow, at a goddess's prompting, is Homer's (Iliad IV), and the omen of the eagle has its model in the Iliad too.")

U = [
(217, 'motu;',
 "But indeed to the Rutulians unequal that fight seemed,\nfor a long while now, and with shifting motion their breasts were stirred;",
 "But to the Rutulians the fight had long been seeming unequal, and their hearts were troubled by shifting feelings;",
 "A new paragraph in Greenough: the scene turns back to the watching Italians. 'At vero', 'but indeed', a strong turn. 'videri… misceri', historic infinitives, standing for imperfect indicatives in a quick description (you will meet them often): 'it seemed… they were stirred'. 'Rutulis', dative with 'videri', 'seemed to the Rutulians'. 'inpar' is Greenough's spelling of 'impar'. 'iamdudum', 'for some time now', since the oath began. 'vario… motu', 'with varied motion', feelings pulling now one way, now another. 'pectora', 'breasts', the seat of feeling. Elision 'iamdud(um) et'."),
(218, 'aequis.',
 "then more, as nearer they discern, not with strength equal.",
 "and the more so now, as they see more closely that the two do not meet on equal strength.",
 "'tum magis', 'then (all the) more', with the historic infinitives of the previous line still understood. 'ut propius cernunt', 'as they see more closely', 'ut' with the indicative meaning 'as' or 'when'. 'non viribus aequis', 'not with equal strength', an ablative of manner or description, with 'eos pugnare' or the like understood: the champions are not matched. The Latin Library prints 'aequos', '(them) not equal in strength', which makes the same point by another construction. No elisions."),
(221, 'pallor.',
 "Helps it, with step silent, advancing and the altar\nsuppliantly venerating with lowered eye, Turnus,\nand his wasting cheeks and in his youthful body the pallor.",
 "Turnus himself adds to the feeling, coming forward with silent step and worshipping at the altar like a suppliant with downcast eyes, and so do his wasted cheeks and the pallor of his young body.",
 "'Adiuvat', 'helps', with no object: Turnus helps the feeling along. 'ad-iuvat' has a consonantal i after the prefix, a-dju-vat, the first syllable long. 'incessu tacito', 'with silent gait'. 'suppliciter venerans', 'reverencing like a suppliant'; 'demisso lumine', ablative absolute, 'eye cast down'. The subjects multiply after the verb: 'Turnus', then his cheeks, then his pallor. 'tabentes', 'wasting, pining away' (from 'tabeo'); the Latin Library has 'pubentes', 'downy with youth', which would stress his boyishness rather than his strain, and so changes the picture. 'iuvenali', 'youthful', with consonantal i. Elisions 'gen(ae) et', 'iuvenal(i) in'."),
(224, 'Camerti,',
 "Whom as soon as Juturna, his sister, to grow louder saw,\nthe talk, and of the crowd to waver the faltering hearts,\ninto the midst of the battle-lines, in form likened to Camers,",
 "As soon as his sister Juturna saw the murmuring grow and the faltering hearts of the people begin to waver, she went into the midst of the ranks in the likeness of Camers,",
 "The period runs from 222 to 228; it is cut at the comma. 'Quem', a connecting relative, picking up 'sermonem', 'which talk'; it stands first and its noun follows in the next line. 'simul ac', 'as soon as'. 'Iuturna soror', Turnus's sister, the nymph whom Juno urged to break the treaty (in the last part). 'crebrescere… variare', infinitives after 'vidit'. 'volgi', Greenough's spelling of 'vulgi', 'of the common people'. 'labantia corda', 'tottering hearts'. 'formam adsimulata', 'made like in form', a passive participle with an accusative of the part, the Greek accusative; 'adsimulata' is Greenough's spelling of 'assimulata'. Elisions 'sermon(em) et', 'form(am) adsimulata'."),
(228, 'fatur:',
 "to whom family from forefathers great and the glorious, of a father's,\nname was, of valour, and himself most fierce in arms,\ninto the midst she throws herself, the battle-lines, not unaware of things,\nand rumours sows, various, and such words speaks:",
 "a man of great ancestry, whose father had a famous name for courage, and himself a most fierce fighter; into the midst of the ranks she plunges, knowing well what she is about, sowing rumours of every kind, and speaks these words:",
 "'cui… erat', dative of possession, 'to whom was', 'who had'. 'cui' is one syllable here. 'genus a proavis ingens', 'a great lineage from his ancestors'; 'clarumque paternae nomen… virtutis', 'and the famous name of his father's valour', the adjective and its noun split across the line. Camers appears at 10.562–563 as the son of great-hearted Volcens, the richest landowner of the Ausonians. 'in medias… acies' is repeated from 224 after the parenthesis, taking up the sentence again. 'haud nescia rerum', 'not ignorant of matters', an understatement: she knows exactly what she is doing. 'serit', 'sows', from 'sero'. Elisions 'ips(e) acerrimus', 'ses(e) acies'."),
(230, 'animam?',
 "“Is it not shameful, O Rutulians, for all such men, one\nto put forward as a shield, a life?",
 "“Are you not ashamed, Rutulians, to throw one life into the danger on behalf of all of us, men like us?",
 "Juturna's speech, in the voice of Camers, runs to 237. 'Non pudet', 'does it not shame (you)', impersonal, with the infinitive 'obiectare'. 'pro cunctis talibus', 'on behalf of all (of us), such (as we are)', brave men able to fight for themselves. 'unam… animam', 'one life', framing the clause, set against 'cunctis'. 'obiectare', 'to throw in the way, expose', a frequentative of 'obicio'; the i after the prefix is consonantal, ob-jec-ta-re, so the first syllable is long. Elision 'obiectar(e) animam'."),
(231, 'sumus?',
 "In number, or in strength, equal\nare we not?",
 "Are we not their equals in numbers or in strength?",
 "A double question, '-ne… an', 'whether in number or in strength', here with 'non': 'are we not equal either in number or in strength?' The answer she wants is that the Italians are more than equal, as the next lines show. 'numero… viribus', ablatives of respect, 'in respect of number, of strength'. 'aequi', 'equal', with 'eis', 'to them', understood. Elision 'Numeron(e) an'."),
(232, 'Turno:',
 "Look, all of them, both Trojans and Arcadians, these are,\nand the fated bands, Etruria hostile to Turnus:",
 "Look: these are all they have, Trojans and Arcadians, and the band the fates sent them, Etruria, that hates Turnus:",
 "'En', 'look!', pointing at the enemy line across the field. 'omnes… hi sunt', 'these are all', the whole of their army is in view and it is not large. 'Troes', two syllables, Tro-es; 'Arcades', Evander's men from Pallanteum. 'fatalesque manus', 'and the fated bands', probably the Etruscans, who by the prophecy of Book VIII were waiting for a foreign leader and found him in Aeneas. 'infensa Etruria Turno', 'Etruria hostile to Turnus', who had sheltered the tyrant Mezentius. Elision 'infens(a) Etruria'."),
(233, 'habemus.',
 "scarcely an enemy, if in turn we should meet them, do we have.",
 "if we met them man to man, we should scarcely have one enemy apiece.",
 "'vix hostem… habemus', 'we scarcely have an enemy', that is, scarcely one enemy for each of us: the Italians outnumber them. 'alterni', 'alternately, one against one', each Italian paired with a Trojan. 'si congrediamur', a present subjunctive in a supposed case, 'if we should meet (them)'. The argument is meant to make the single combat look like cowardice, when a general battle would win. Elision 'host(em) alterni'."),
(235, 'feretur:',
 "He indeed to the gods above, at whose altars he devotes himself,\nwill rise up in fame, and living through mouths will be carried:",
 "He, it is true, will rise in fame to the gods above, to whose altars he is devoting himself, and his name will live on men's lips:",
 "'Ille', Turnus. 'quidem', 'indeed', conceding one point before the turn at 'nos'. 'ad superos… succedet fama', 'will mount up to the gods above in fame', his glory rising to heaven. 'quorum se devovet aris', 'at whose altars he devotes himself': in a Roman 'devotio' a commander vowed his own life to the gods for his army's victory, as the Decii did; Juturna presents Turnus as such a sacrifice. 'vivus per ora feretur', 'living, he will be carried through the mouths (of men)', a phrase with a long Roman history. Elision 'quid(em) ad'."),
(237, 'arvis.”',
 "we, our fatherland lost, to masters proud to be obedient\nshall be forced, who now, sluggish, have sat down in the fields.”",
 "we shall lose our country and be forced to obey proud masters, we who now sit idle in the fields.”",
 "Juturna's speech ends here. 'nos', 'we', set hard against 'ille'. 'patria amissa', ablative absolute, 'our country lost'. 'dominis… superbis', dative with 'parere', 'to obey proud masters', the Trojans pictured as conquerors. 'cogemur', 'we shall be compelled'. 'lenti', 'sluggish, idle', the adjective doing the work of an adverb. 'consedimus arvis', 'we have sat down in the fields', watching the duel when they could be fighting; 'arvis' a local ablative without a preposition. Elision 'patri(a) amissa'."),
(239, 'murmur;',
 "By such was kindled the young men's feeling, by words,\nnow more and more, and creeps through the columns a murmur;",
 "Words like these set the young men's minds ablaze more and more, and a murmur crept along the ranks;",
 "'Talibus… dictis', 'by such words', framing the line, the formula that marks the end of a speech. 'incensa est', 'was set on fire'. 'iuvenum sententia', 'the feeling of the young men', the fighting men. 'iam magis atque magis', 'now more and more'. 'serpit', 'creeps', a snake's movement, of a sound spreading low through the crowd. 'agmina', 'columns, ranks'. Prodelision 'incensa (e)st', the 'e' of 'est' lost after the vowel."),
(240, 'Latini.',
 "the Laurentines themselves changed, and the Latins themselves.",
 "even the Laurentines were changed, even the Latins.",
 "A verbless line, 'sunt' understood with 'mutati'. 'ipsi… ipsique', 'even… and even', the repeated pronoun marking the surprise. The Laurentines and the Latins are Latinus's own people, who had wanted peace and the duel; even they now turn against the treaty. Laurentum is Latinus's city. Elision 'mutat(i) ipsique'."),
(243, 'iniquam.',
 "Who for themselves now rest from the fight and for their state safety\nwere hoping, now arms they want and the treaty they pray\nundone, and Turnus's lot they pity, unjust.",
 "Men who had been hoping that they would now have rest from fighting and safety for their fortunes now want arms, pray that the treaty may be undone, and pity Turnus for his unfair lot.",
 "'Qui', 'those who', the antecedent left out. 'sibi… requiem pugnae', 'rest from battle for themselves', 'pugnae' a genitive of separation, 'rest from'. 'rebus… salutem', 'safety for their affairs'. 'sperabant', imperfect, set against 'nunc… volunt'. 'foedus… precantur infectum', 'pray for the treaty (to be) undone', the participle carried over the line-end. 'sortem… iniquam', 'his unfair lot', framing the clause: the single combat. 'requiem', three syllables, re-qui-em. Elision 'infect(um) et'."),
(246, 'fefellit.',
 "To these another, greater thing Juturna joins, and from high\ngives a sign, the sky, than which not more effective any\nhas troubled minds Italian and by its portent deceived.",
 "To this Juturna adds something greater still, and gives a sign from high heaven; none ever did more to confound Italian minds or deceived them more with its marvel.",
 "'His', 'to these (words)'. 'aliud maius', 'something else, greater'. 'maius' scans long in its first syllable, mai-jus. 'adiungit' has a consonantal i after the prefix, ad-jun-git. 'alto… caelo', 'from the high sky', framing the clause. 'quo non praesentius ullum', 'than which none (was) more effective', 'praesens' being the word for power felt on the spot; 'quo' is an ablative of comparison. 'Italas' has its first syllable lengthened, as 'Italia' does in verse. 'monstro', 'by the portent', an omen beyond nature. Elision 'Iuturn(a) adiungit'."),
(250, 'uncis.',
 "For flying in the ruddy upper air, the tawny bird of Jove\nthe shore-birds was harrying and the throng loud-sounding\nof the winged troop, when suddenly gliding down to the waves\na swan, outstanding, with its feet he seizes, shameless, with crooked talons.",
 "For Jove's tawny eagle, flying through the red-glowing sky, was harrying the shore-birds and the whole clamouring flock of winged creatures, when suddenly he swooped down to the water and, ruthless, snatched up a splendid swan in his hooked talons.",
 "'Iovis ales', 'Jupiter's bird', the eagle; 'fulvus', 'tawny'. 'rubra… in aethra', 'in the reddish upper air', 'aethra' a Greek word for the bright sky. 'agitabat', imperfect, the scene running on, until 'cum… rapit', an inverted 'cum' with the historic present: the sudden event comes in the 'when' clause. 'agminis aligeri', 'of the winged column', a high-flown phrase. 'lapsus', 'gliding down'. 'cycnum excellentem', 'a splendid swan', framed against 'improbus', 'shameless, relentless', the eagle. The Iliad has an eagle omen at the wall of the Greek camp (Iliad XII), its bird likewise forced to drop its prey. Elision 'cycn(um) excellentem'."),
(252, 'visu,',
 "Pricked up their spirits the Italians, and all the birds\nturn their flight with clamour, wonderful to see,",
 "The Italians' hearts leapt up; and all the birds, a marvel to see, turned back from flight with a great cry,",
 "The period runs from 251 to 256; it is cut at the comma. 'Adrexere', Greenough's spelling of 'arrexere', = 'arrexerunt', the '-ere' perfect (you will see it constantly), 'they pricked up', as of ears. 'Itali', with its first syllable long in verse, Ī-ta-li. 'convertunt… fugam', 'turn about their flight', they stop fleeing and turn on the eagle. 'clamore', 'with a clamour'. 'mirabile visu', 'wonderful to see', 'visu' the supine in '-u', 'in the seeing'. Elision 'Adrexer(e) animos'."),
(256, 'fugit.',
 "and the sky they darken with wings, and the enemy through the airs\nwith a cloud made they press, until, by force conquered and by the very\nweight, he failed, and the prey from his talons, the bird,\nflung into the river, and deep into the clouds fled.",
 "and darkened the sky with their wings, and, forming a cloud, pressed their enemy hard through the air, until he gave way, overcome by their force and by the very weight of his prize, flung his prey from his talons into the river, and fled away deep into the clouds.",
 "'aethera', Greek accusative of 'aether'; its 'Ae-' is one long syllable. 'hostem', the eagle, now the enemy. 'facta nube', ablative absolute, 'a cloud having been made', the flock massed together. 'donec… defecit', 'until he gave out', 'donec' with the perfect indicative of a fact. 'vi victus et ipso pondere', 'conquered by force and by the very weight', the swan's. 'ales', the eagle again. 'fluvio', 'into the river', a dative of direction. 'proiecit', with consonantal i after the prefix, pro-jecit. 'penitus', 'deep, far within'. Elisions 'aetheraqu(e) obscurant', 'praedamqu(e) ex', 'penitusqu(e) in'."),
(258, 'manus;',
 "Then indeed the augury the Rutulians with a shout greet\nand make ready their hands;",
 "Then the Rutulians hailed the omen with a shout and made their hands ready for the fight;",
 "'Tum vero', 'then indeed', marking the climax of the change of heart. 'augurium', 'the augury', a sign given by birds, which is what the Roman augurs watched for; 'salutant', 'greet', accept the omen as meant for them. 'expediunt manus', 'make their hands ready', for weapons; 'expedio' is 'to free, get ready'. 'expediuntque' scans ex-pe-di-unt-que. Elision 'ver(o) augurium'."),
(259, 'petivi.',
 "and first Tolumnius the augur:\n“This was it, this, with my vows,” he says, “which often I have sought.",
 "and first of all the augur Tolumnius: “This was it, this,” he cried, “the thing I have so often asked for in my prayers.",
 "The print has 'votis, inquit, quod', with 'inquit' inside the quotation, a misprint for 'votis,” inquit, “quod', corrected here: 'inquit' is the narrator's word breaking into the speech, as at 6.46 and 11.464. 'primus… Tolumnius augur', 'Tolumnius the augur first', Turnus named him 'felix Tolumnius' at 11.429; the verb of speaking is left out and 'inquit' supplies it. 'Hoc erat, hoc… quod', 'this was it, this, that': the imperfect of something now recognised as true all along. 'votis', 'with my vows'. 'petivi', 'I have sought'. No elisions."),
(263, 'populat:',
 "I accept and I recognise the gods; me, me as leader, the sword\nseize, O wretched, whom a shameless stranger with war\nterrifies, like feeble birds, and your shores\nby force lays waste:",
 "I accept it, and I know the gods in it. Take up the sword with me, with me as your leader, poor people, whom a shameless foreigner terrifies with war like helpless birds and plunders your coast by force:",
 "'Adcipio adgnoscoque', Greenough's spellings of 'accipio agnoscoque'. 'accipio' is the formal word for accepting an omen as binding on oneself; 'adgnosco deos', 'I recognise the gods', at work in the sign. 'me, me duce', 'with me, me as leader', an ablative absolute, the pronoun doubled in eagerness. 'corripite', 'seize', plural imperative. 'improbus advena', 'the shameless newcomer', Aeneas, read as the eagle. 'invalidas ut aves', 'like weak birds', 'ut' placed after the words it governs. 'litora… populat', 'ravages the shores'. Elisions 'Adcipi(o) adgnoscoque', 'corripit(e) O'."),
(264, 'dabit.',
 "he will seek flight, and far out on the deep\nwill give his sails.",
 "he will take to flight and set his sails far out over the deep.",
 "Tolumnius reads the omen: as the eagle dropped its prey and fled into the clouds, so Aeneas will flee by sea. 'petet… fugam', 'will seek flight'. 'penitus… profundo', 'far off on the deep', 'profundo' the open sea, an ablative of place. 'vela dabit', 'will give sails (to the winds)', the regular phrase for setting sail. No elisions."),
(265, 'raptum.”',
 "You, of one mind, close up your companies,\nand your king, by fighting, defend, snatched from you.”",
 "Close up your ranks with one mind, and by fighting defend the king who has been snatched from you.”",
 "Tolumnius's speech ends here. 'unanimi', 'of one mind', like the flock that turned together. 'densete', 'thicken, close up', from 'denseo', 'catervas', 'companies'. 'regem… raptum', 'the king snatched away', Turnus, taken from them by the treaty as the swan was taken by the eagle; 'vobis' is a dative of separation, 'from you'. 'pugna', 'by fighting', an ablative of means. No elisions."),
(267, 'procurrens:',
 "He spoke, and straight at the opposing enemies a weapon he hurled,\nrunning forward:",
 "With that he ran forward and hurled a spear full at the enemy facing him:",
 "'Dixit', 'he spoke', the regular close of a speech. 'adversos… in hostis', 'against the enemies facing (him)', 'hostis' the '-is' accusative plural that Greenough prints. 'contorsit', 'whirled, hurled', the spear spun as it is thrown. 'procurrens', 'running forward', held back to the next line. The augur, not a soldier, breaks the truce, as Pandarus breaks the truce in Iliad IV with an arrow, urged by Athena in disguise as Juturna is here. No elisions."),
(268, 'secat.',
 "a sound gives the whistling cornel, and the airs,\nsure, it cuts.",
 "the cornel shaft whistles as it flies, and cuts the air unerringly.",
 "'stridula cornus', 'the whistling cornel', the spear named from its wood, the hard cornelian cherry used for shafts. 'sonitum dat', 'gives a sound'. 'certa', 'sure', of the spear's aim, an adjective standing for an adverb: it flies true. 'secat', 'cuts'. 'auras', 'the airs', the plural common in verse. No elisions."),
(269, 'tumultu.',
 "At once this, at once a huge shout, and all\nthe wedges thrown into confusion, and hearts heated by the uproar.",
 "At the same moment a huge shout went up, all the close-packed ranks were thrown into disorder, and hearts were heated by the tumult.",
 "'Simul hoc, simul…', 'at once this, at once…', the cast and the uproar come together; the verbs are left out. 'cunei', 'wedges', the dense blocks of soldiers drawn up in the field; it has three syllables, cu-ne-i. 'turbati', 'thrown into disorder', with 'sunt' understood. 'calefacta', 'heated', from 'calefacio'. 'tumultu', 'by the uproar'. No elisions."),
(272, 'Gylippo,',
 "The spear, flying, where by chance nine most handsome brothers'\nbodies had taken their stand opposite, whom a faithful had borne,\none, so many, to Arcadian, wife Tyrrhenian, Gylippus,",
 "The flying spear, where by chance nine brothers, all of them most handsome, had taken their stand facing it, all born to the Arcadian Gylippus by one faithful Etruscan wife,",
 "The period runs from 270 to 276; it is cut at the comma. 'Hasta volans' is the subject, and its verb waits until 'transadigit' in 276. 'ut forte', 'where by chance'. 'pulcherrima fratrum corpora', 'most handsome bodies of brothers', the body standing for the man, a usage of epic. 'constiterant contra', 'had taken their stand opposite'. 'crearat' = 'creaverat', 'had borne', the syncopated pluperfect. 'una tot', 'one woman, so many sons'. 'coniunx', with consonantal i after the prefix, con-junx. 'Tyrrhena', 'Etruscan'. No elisions."),
(276, 'harena.',
 "one of these, at the middle, where is chafed the sewn, by the belly,\nbelt, and of the sides the joinings the buckle bites,\na youth outstanding in beauty and in shining arms,\nit drives through, through the ribs, and on the tawny sand lays him out.",
 "struck one of them in the middle of the body, where the stitched belt rubs against the belly and the buckle grips the joining at the sides, a young man of outstanding beauty and gleaming armour; it drove right through his ribs and stretched him out on the yellow sand.",
 "'horum unum', 'one of these', object of 'transadigit', with 'iuvenem' in apposition. 'ad medium', 'at the middle (of the body)'. 'teritur qua… alvo balteus', 'where the sewn belt is chafed by the belly'; 'alvo' an ablative. 'balteus' is best read in three syllables, bal-te-us, though two would also scan. 'fibula mordet', 'the buckle bites', clasping the belt's ends. 'transadigit costas', 'drives through the ribs', a compound verb with two accusatives, the man and the part pierced. 'effundit', 'pours out', lays him full length. Greenough prints no comma after 'mordet'. Elisions 'hor(um) unum', 'un(um) ad', 'iuven(em) et', 'fulvaqu(e) effundit'."),
(279, 'ruunt.',
 "But the brothers, a spirited phalanx and fired with grief,\npart, swords they draw with their hands, part the missile iron\nseize, and blindly they rush.",
 "But the brothers, a spirited band, ablaze with grief, some drawing swords, some snatching up javelins, charged blindly forward.",
 "'animosa phalanx accensaque luctu', in apposition to 'fratres', 'a spirited phalanx and inflamed by grief'; 'phalanx', a Greek word for a close battle-line, the eight surviving brothers. 'pars… pars', 'some… others', with plural verbs, since each 'part' is several men. Greenough's comma after the first 'pars' is not needed for the sense, which is 'pars gladios stringunt', 'some draw swords'. 'missile ferrum', 'throwing iron', javelins. 'caeci', 'blind', with rage and grief. No elisions."),
(281, 'armis:',
 "Whom, the columns, against\nrun forward, of the Laurentines; from this side, packed, again pour in like a flood\nthe Trojans and the Agyllines and, with painted arms, the Arcadians:",
 "Against them the Laurentine columns ran forward; from the other side the Trojans, the men of Agylla and the Arcadians with their painted armour flooded in again in close array:",
 "'Quos… contra', 'against whom', the preposition placed after its pronoun, a connecting relative. 'agmina… Laurentum', 'the columns of the Laurentines', 'Laurentum' the old '-um' genitive plural. 'hinc', 'on this side', set against the Italians: the other army. 'densi', 'massed'. 'rursus inundant', 'flood in again', battle pictured as water. 'Agyllini', the men of Agylla, the Etruscan city also called Caere, Mezentius's old capital. 'pictis… armis', 'with painted arms', decorated shields. Elisions 'Laurent(um) hinc', 'Agylliniqu(e) et'."),
(282, 'ferro.',
 "thus all one love holds, to decide by the iron.",
 "so one desire took hold of them all, to settle the matter with the sword.",
 "'sic', 'thus', summing up. 'omnis' is the '-is' accusative plural, 'all (of them)', object of 'habet'; 'amor unus', 'one desire', is the subject. 'decernere ferro', 'to decide with the sword', an infinitive depending on 'amor'. The duel was meant to settle the war by two men; now every man wants to settle it himself. No elisions."),
(285, 'ferunt.',
 "They tore apart the altars; there goes through the whole sky, thick,\na storm of weapons, and an iron rain rushes on,\nand the mixing-bowls and the hearths they carry off.",
 "They pulled the altars to pieces; a thick storm of missiles swept over the whole sky and a rain of iron came pouring down, and they carried off the mixing-bowls and the fire-pans.",
 "'Diripuere', = 'diripuerunt', 'they tore apart', the altars of the treaty, for brands and weapons. 'it toto… caelo', 'goes over the whole sky'. 'turbida… tempestas telorum', 'a thick storm of weapons'. 'ferreus', three syllables, fer-re-us; 'ingruit', 'rushes on, assails'. 'crateras', a Greek accusative plural, 'mixing-bowls', for the wine of the sacrifice; 'focos', the braziers set up at 118. Who carries them off and why is not said: the sacred vessels are taken from the field. Elisions 'Diripuer(e) aras', 'telor(um) ac'."),
(286, 'divos.',
 "Flees Latinus himself,\nthe outraged carrying back, the treaty undone, the gods.",
 "Latinus himself fled, carrying back his outraged gods, the treaty unfulfilled.",
 "'Fugit ipse Latinus', 'Latinus himself flees', the king who swore the oath. 'pulsatos… divos', 'the gods beaten, outraged', framing the line: the gods by whom he swore have been insulted by the breach. 'referens', 'carrying back', the images he brought out for the oath. 'infecto foedere', ablative absolute, 'the treaty unaccomplished'. No elisions."),
(288, 'adsunt.',
 "Bridle others their chariots, or their bodies with a leap\nthrow up onto horses, and with drawn swords are at hand.",
 "Others yoked and bridled their chariots, or leapt up on to their horses, and were there with swords drawn.",
 "'Infrenant… currus', 'they bridle their chariots', the chariot put for its horses. 'alii', 'others'. 'corpora saltu subiciunt in equos', 'with a leap they throw their bodies up onto horses'; 'subicio' here means 'to throw up from below'. 'subiciunt' has a consonantal i after the prefix, its first syllable long: su-bji-ci-unt. 'strictis ensibus', 'with drawn swords'. 'adsunt', 'are at hand'. No elisions."),
(291, 'equo:',
 "Messapus the king, and of a king the emblem bearing,\nthe Tyrrhenian Aulestes, eager to confound the treaty,\nwith his horse facing him, frightens back:",
 "Messapus, eager to throw the treaty into confusion, rode his horse straight at the Etruscan Aulestes, a king who wore the emblem of a king, and drove him back in fright:",
 "Messapus, the tamer of horses, Neptune's son, fights for Turnus. 'regem regisque insigne gerentem', 'a king and wearing the badge of a king': the victim is royal, which makes the next lines worse. 'Tyrrhenum Aulesten', 'the Etruscan Aulestes', with a Greek accusative in '-en'; at 10.207 he led a ship to Aeneas. 'avidus confundere', 'eager to throw into disorder', an infinitive after an adjective, poetic. 'adverso… equo', 'with horse facing (him)', riding at him head-on. 'proterret', 'frightens away'. Elisions 'regisqu(e) insigne', 'Tyrrhen(um) Aulesten'."),
(293, 'umeros.',
 "falls he, drawing back,\nand, wretched, on the set-against, behind him, is rolled, altars,\nonto his head and onto his shoulders.",
 "Aulestes fell as he backed away, and, poor man, was pitched over the altars that stood behind him, on to his head and shoulders.",
 "'ruit ille recedens', 'he falls as he retreats'. 'miser', 'wretched', the narrator's pity. 'oppositis a tergo… aris', 'by the altars set in his way behind him', the altars of the treaty. 'involvitur', 'is rolled over', tumbling backwards. 'in caput inque umeros', 'onto his head and onto his shoulders'. 'umeros' is Greenough's spelling, without the h of 'humeros'. Elisions 'terg(o) involvitur', 'inqu(e) umeros'."),
(295, 'fatur:',
 "But hot he flies at him with his spear,\nMessapus, and with a weapon, him begging much, like a beam,\nfrom above, high on his horse, heavily strikes and thus speaks:",
 "But Messapus, burning for blood, flew at him with his spear, and from high on his horse, as the man pleaded for his life, struck down hard with a shaft like a beam, and spoke these words:",
 "'fervidus', 'fiery, hot', of Messapus's eagerness. 'advolat hasta', 'flies at (him) with spear'. 'telo… trabali', 'with a weapon like a beam', framing the line; a 'trabs' is a timber. 'orantem multa', 'him begging many things', the participle with the man understood as its noun, 'multa' an internal accusative. 'desuper altus equo', 'high on his horse, from above', the rider over the fallen man. 'graviter ferit', 'strikes heavily'. 'atque ita fatur', the regular formula introducing a speech. Elisions 'teloqu(e) orantem', 'atqu(e) ita'."),
(296, 'divis.”',
 "“He has it; this, better, to the great given, a victim, gods.”",
 "“He has it! Here is a better victim for the great gods.”",
 "'Hoc habet', 'he has this', 'he's hit', the cry of the crowd in the Roman arena when a gladiator was wounded. 'haec melior… victima', 'this (is) a better victim', a king slain on the altar in place of the beasts of the treaty, a savage joke. 'magnis… divis', dative, 'to the great gods', framing the second half with 'data', 'given'. No elisions."),
(297, 'membra.',
 "Run together the Italians and strip the warm limbs.",
 "The Italians ran up together and stripped the limbs, still warm.",
 "'Concurrunt', 'run together', from every side. 'Itali', with the first syllable long, as at 251. 'spoliant', 'strip', of armour, the ordinary prize of battle. 'calentia membra', 'the warm limbs', the life only just gone. No elisions."),
(300, 'flammis:',
 "Meeting him, a burnt firebrand Corynaeus from the altar\nseizes, and to Ebusus coming on and bringing a blow\nhe gets in first, at his face, with flames:",
 "Corynaeus, coming to meet him, snatched a charred brand from the altar, and as Ebusus came on, aiming a blow, he was first to thrust the flames into his face:",
 "'Obvius', 'meeting (him)', in his path. 'ambustum torrem', 'a half-burnt brand', from the sacrificial fire. Corynaeus is a Trojan; a Trojan of the name is killed by Asilas at 9.571, and one buries Misenus at 6.228: the names repeat. 'venienti… plagamque ferenti', datives with 'occupat os', 'forestalls the face to him coming and bringing a blow', strikes him in the face first. 'occupat', 'seizes first, forestalls'. 'Ebuso': the Latin Library spells it 'Ebyso'. Elision 'venient(i) Ebuso'."),
(301, 'dedit.',
 "To him the huge beard blazed up\nand a smell of burning, scorched, gave.",
 "His great beard blazed up and gave off a stench of burning.",
 "'olli', the old form of 'illi', 'to him, his', a dative of reference; Virgil uses it for an archaic ring (you will meet it again at 309). 'ingens barba', 'his great beard'. 'reluxit', 'flared up'. 'nidorem', 'a reek', the smell of something burning, here hair and flesh. 'ambusta', 'scorched', with 'barba'. Elisions 'oll(i) ingens', 'nidoremqu(e) ambusta'."),
(303, 'ipsum:',
 "Over him, himself, having followed up,\nthe hair, with his left, of the confused enemy he seizes,\nand pressing in his knee, straining, to the earth pins the man himself:",
 "Following up, Corynaeus himself stood over him, seized his bewildered enemy's hair in his left hand, and pressing down with his knee forced him to the ground:",
 "'Super… secutus', 'having followed up, over (him)'; 'ipse' is Corynaeus. 'caesariem', 'the hair' of the head. 'laeva', 'with his left (hand)', 'manu' understood. 'turbati… hostis', 'of the confounded enemy', framing the line with 'caesariem'. 'inpresso… genu', ablative absolute, 'knee pressed in'; 'inpresso' is Greenough's spelling of 'impresso'. 'nitens', 'straining'. 'terrae adplicat', 'presses (him) to the ground', 'terrae' a dative; 'adplicat' is Greenough's spelling of 'applicat'. Elision 'terr(ae) adplicat'."),
(304, 'ferit.',
 "thus with the stiff, his side, sword he strikes.",
 "and so struck him in the side with his unbending sword.",
 "'sic', 'thus', in that position, holding him down. 'rigido… ense', 'with the stiff sword', framing 'latus', 'the side'. 'ferit', 'strikes'. The killing is told in four plain words after the long build-up; Ebusus is not heard of again. No elisions."),
(306, 'superimminet:',
 "Podalirius over Alsus,\nthe shepherd, and in the first line through the weapons rushing,\nwith sword following, naked, looms:",
 "Podalirius, following with drawn sword, loomed over Alsus, a shepherd, who was rushing through the missiles in the front line:",
 "'Podalirius', a Trojan, its name borrowed from a Greek healer of the Iliad. 'Alsum… ruentem', 'Alsus… rushing', the object of 'superimminet', 'looms over', a double compound of 'immineo'. 'pastorem', 'a shepherd', one of the countrymen fighting for Turnus. 'prima… acie', 'in the front line'. 'per tela', 'through the weapons'. 'ense… nudo', 'with naked sword', framing 'sequens'. Elision 'primaqu(e) acie'."),
(308, 'cruore.',
 "he, with an axe,\nof the man facing him the forehead's middle and the chin, drawn back,\nsplits, and with spattered widely drenches the armour gore.",
 "but the shepherd swung back his axe and split his opponent's forehead down the middle and his chin, and drenched his armour with blood spattered far and wide.",
 "'ille', Alsus, the shepherd, who turns the tables. 'securi… reducta', ablative absolute, 'his axe drawn back', the weapon of a countryman; 'securi' is the ablative of 'securis', framing the next line. 'adversi', 'of the man facing him', Podalirius. 'frontem mediam mentumque', 'the middle of the forehead and the chin'. 'disicit', 'splits apart', Greenough's spelling (the Latin Library 'dissicit'); the i after the prefix is consonantal, so the first syllable is long. 'sparso late… cruore', 'with gore spattered widely', framing the clause. No elisions."),
(310, 'noctem.',
 "On him hard rest, on his eyes, and iron presses\nsleep; into eternal are closed his lights, night.",
 "A hard rest, an iron sleep, weighs down his eyes; his eyes are shut in everlasting night.",
 "'Olli', 'on him', the old 'illi', a dative of reference: Podalirius. 'dura quies… et ferreus… somnus', 'hard rest and iron sleep', death as sleep, the subjects framing a line and a half. 'urget', 'presses on'; Greenough spells it with -g- here, not 'urguet'. 'ferreus', three syllables, fer-re-us. 'in aeternam… noctem', 'into everlasting night', framing the clause. 'lumina', 'lights', the eyes. 'conduntur', 'are laid to rest, shut away'. The two lines repeat 10.745–746, where Greenough has 'clauduntur', 'are closed'. No elisions."),
]

# Speech-mark check exemptions (rule 5b), by closing text of the unit:
#  'petivi.' (259): the print has '“Hoc erat, hoc, votis, inquit, quod saepe petivi.' with 'inquit' inside the
#      quotation; t keeps the print (one opening mark), l and i close the speech before 'inquit' and reopen it
#      after (two opening marks, one closing mark).
EXEMPT = {'petivi.'}
# Long periods are cut at internal commas (222-228 at 224, 251-256 at 252, 270-276 at 272), as build_aeneid.py allows.
OVERLONG = set()
P = A.part('aeneid-093'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
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
