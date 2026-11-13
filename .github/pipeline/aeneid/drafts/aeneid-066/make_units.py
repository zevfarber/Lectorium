# aeneid-066 (IX.224-313): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Nisus et Euryalus apud Ascanium'
PART = "Nisus and Euryalus Before the Council (IX.224–313)"
TITLE_EN = "Nisus and Euryalus Before the Council — Aeneid IX.224–313"
ABOUT = ("Night: everything on earth is asleep except the Trojan leaders, who stand armed in council in the middle of "
"the camp, debating what to do and who should carry word to Aeneas. Nisus and Euryalus ask to be heard. Nisus tells them "
"that the Rutulians lie sunk in wine and sleep, that there are gaps in their watch-fires, and that he knows a way out by "
"the gate nearest the sea; let the two of them go, and they will soon be back with Aeneas, and with spoils besides. Old "
"Aletes weeps for joy that the gods have not abandoned Troy after all: the gods and their own good hearts will reward "
"them first, Aeneas and Ascanius after. Ascanius, in command while his father is away, outdoes him. He puts all his hopes "
"in their hands and heaps up gifts — silver cups, tripods, gold, a mixing-bowl that was Dido's, and, once Italy is won, "
"Turnus's own horse and golden armour, twelve women, captives, and the king's land — and takes Euryalus, nearly his own "
"age, as his companion for life. Euryalus asks for one thing only. His mother, who followed him from Troy and would not "
"stay behind in Sicily, does not know he is going, and he cannot bear her tears: let Ascanius look after her. The Trojans "
"weep, and Ascanius, reminded of his own love for his father, swears that she shall be a mother to him and have whatever "
"he has promised her son. They arm: Ascanius gives Euryalus his own sword, Mnestheus gives Nisus a lion-skin, Aletes "
"exchanges helmets with him, and the leaders see them to the gate with prayers. Iulus gives them many messages for his "
"father, but the winds scatter them all into the clouds. Virgil builds the night council and the arming on Iliad 10, "
"where Diomedes and Odysseus go spying among the Trojans, and the gifts on Agamemnon's offer to Achilles in Iliad 9.")

U = [
(225, 'oblita laborum:',
 "All other creatures, throughout the lands, in sleep\nwere loosening their cares, and hearts forgetful of their toils:",
 "Everywhere on earth every other living thing was easing its cares in sleep, its heart forgetting its labours:",
 """A new paragraph in Greenough. Night, and the scene moves from the two friends, who left the gate at the end of the last part to look for the prince (9.223), to the Trojan leaders. 'Cetera… animalia', 'the other living creatures', framing the line; 'omnis', accusative plural with 'terras', Greenough's '-is' (you'll see this constantly). 'somno', 'by sleep', instrumental ablative. 'laxabant curas', 'were loosening their cares', 'et corda oblita laborum', 'and (loosening) hearts forgetful of toil'. A sleeping world set against those who stay awake is an old contrast: it opens Iliad 10, where all the Greeks sleep except Agamemnon, the book in which Diomedes and Odysseus go spying by night, the model of this whole episode. Virgil used it for Dido's sleepless night (4.522–532), and 225 is almost the line printed at 4.528, 'lenibant curas, et corda oblita laborum', which Greenough brackets there as spurious. Elision 'cord(a) oblita'."""),
(228, 'nuntius esset.',
 "but the leaders of the Teucrians, the foremost, and the chosen youth\na council on the highest affairs of the realm were holding,\nwhat they should do, or who now to Aeneas should be messenger.",
 "but the foremost captains of the Trojans and the pick of their young men were holding council on the gravest affairs of the kingdom: what they were to do, and who should now carry word to Aeneas.",
 """'ductores Teucrum primi', 'the first leaders of the Teucrians'; 'Teucrum' = 'Teucrorum', the short genitive plural (as 'divom', 'virum'). There is no 'but' in the Latin: the two clauses are set side by side without a connective (asyndeton), and the contrast does the work. 'delecta iuventus', 'the chosen youth', the picked young warriors. 'consilium… habebant', 'were holding a council', the imperfect of a scene going on. 'summis regni de rebus', 'about the highest matters of the realm', 'de' set between adjective and noun, a common verse order. 'quid facerent quisve… esset', indirect questions in the imperfect subjunctive after a past verb. 'Aeneae… nuntius', 'messenger to Aeneas', who is away up the Tiber with Evander (Book 8). Elision 'prim(i) et'."""),
(230, 'campi medio.',
 "They stand, leaning on long spears, and holding shields,\nof the camp and of the plain in the middle.",
 "They stood leaning on their long spears, shields in hand, in the middle of the open ground of the camp.",
 """'Stant', the vivid present. 'adnixi hastis', 'leaning on their spears', 'hastis' dative (or ablative) with a verb of leaning; 'adnixi' is from 'adnitor', Greenough's spelling of 'annitor'. They hold council standing and armed, ready for an attack at any moment. 'castrorum et campi medio', 'in the middle of the camp and the open ground', 'medio' a noun, 'the middle', ablative of place without a preposition; 'campi' is the clear space inside the rampart. Elisions 'adnix(i) hastis', 'castror(um) et'."""),
(232, 'morae fore.',
 "Then Nisus, and together with him\nEuryalus, at once, eager, to be admitted beg:\na great matter (it is), and worth the delay it will be.",
 "Then Nisus, and Euryalus with him, came in haste and eagerly begged to be let in: it was a matter of weight, they said, and would be well worth the interruption.",
 """'una', 'together', the adverb. 'alacres', 'eager', nominative plural, of both. 'admittier' = 'admitti', 'to be admitted', the old present passive infinitive in '-ier', an archaism Virgil keeps for its antique ring (it belongs to old prayers and laws). 'orant' with the infinitive, 'they beg to be let in'. 'rem magnam (esse), pretiumque morae fore', indirect statement hanging on the idea of saying in 'orant': 'it is a great matter, and will be worth the delay'; 'pretium morae', 'the price of the delay', what repays it. Elision 'confesti(m) alacres'."""),
(233, 'dicere iussit.',
 "First Iulus\nreceived them, excited, and Nisus to speak ordered.",
 "Iulus was the first to welcome them in their excitement, and he told Nisus to speak.",
 """'Primus Iulus', 'Iulus first', before the elders: Ascanius, Aeneas's son, is also called Iulus, the name from which the Julian family claimed descent (1.267–288), and he is in command while his father is away. 'Iulus' has three syllables, I-u-lus. 'trepidos', 'agitated', 'in a flurry', here with eagerness, not fear. 'Nisum dicere iussit', 'ordered Nisus to speak', the elder of the two. No elisions."""),
(236, 'quae ferimus.',
 "Then thus the son of Hyrtacus: “Hear, O, with minds fair,\nmen of Aeneas, and let not by our years be judged these things\nwhich we bring.",
 "Then the son of Hyrtacus spoke: “Hear us with open minds, men of Aeneas, and do not judge what we bring by our years.",
 """Nisus's speech (234–245). 'Hyrtacides', 'son of Hyrtacus', a patronymic in '-ides' (as at 9.177); 'sic (ait)', the verb of speaking left out, as so often. 'mentibus aequis', 'with fair minds', without prejudice. 'Aeneadae', 'sons of Aeneas', his people. 'neve… spectentur', 'and let them not be viewed', a negative jussive subjunctive; 'ab annis', 'from (the standpoint of) our years': they are young, and expect to be doubted. 'quae ferimus', 'what we bring forward', what we propose. Elision 'Audit(e) O'."""),
(237, 'conticuere;',
 "The Rutulians, by sleep and wine loosened,\nhave fallen silent;",
 "The Rutulians, slackened with sleep and wine, have gone quiet;",
 """'somno vinoque soluti', 'loosened by sleep and wine', as the last part showed the Rutulian watch passing the night in drink (9.164–167). 'conticuere' = 'conticuerunt', 'have fallen silent', the perfect in '-ere' for '-erunt' again. Short clauses, set down like a scout's report. No elisions."""),
(238, 'proxuma ponto;',
 "a place for a surprise we have spied ourselves,\nwhich lies open at the fork of the road by the gate that is nearest the sea;",
 "we have seen for ourselves a place to strike unseen, lying open where the road forks by the gate nearest the sea;",
 """'locum insidiis', 'a place for a surprise', 'insidiis' dative of purpose; 'insidiae' is any stealthy attack, not only an ambush lying in wait. 'ipsi', 'we ourselves', as eyewitnesses. 'qui patet', 'which lies open'. 'in bivio portae', 'at the fork of the gate', where the road out of the gate divides. 'quae proxuma (est) ponto', 'which is nearest the sea', 'ponto' dative with 'proxumus'; 'proxuma' is Greenough's old spelling of 'proxima' (as 'maxumus'). Elision 'loc(um) insidiis'."""),
(240, 'erigitur:',
 "the fires are broken off, and black to the stars smoke\nis raised:",
 "there are gaps in their fires, and black smoke rises to the stars:",
 """'interrupti (sunt) ignes', 'the fires are interrupted': the ring of watch-fires round the camp has gaps in it where the guards have fallen asleep and let them die. 'ater… fumus', 'black smoke', framing 'ad sidera': smouldering fires give smoke, not flame, and so less light. Elisions 'interrupt(i) ignes', 'aterqu(e) ad'."""),
(243, 'adfore cernetis.',
 "if the chance you permit (us) to use\nto seek Aeneas and the walls of Pallanteum,\nsoon here with spoils, a great slaughter accomplished,\nus present you will see.",
 "if you let us use our chance to go in search of Aeneas and the walls of Pallanteum, you will soon see us back here with spoils, after cutting a great swathe through the enemy.",
 """'si… permittitis uti', 'if you permit (us) to use', 'fortuna' ablative with 'utor'; the present indicative in a plain condition. 'quaesitum', supine of purpose, 'to seek'. 'Aenean', a Greek accusative. 'moenia Pallantea', 'the walls of Pallanteum', Evander's town on the site of the future Rome; 'Pallantea' is a Greek-style adjective, four syllables, Pal-lan-te-a. 'adfore (nos)… cernetis', 'you will see (us) to be present', 'adfore' the future infinitive of 'adsum', its subject understood. 'ingenti caede peracta', ablative absolute, 'a huge slaughter carried through': Nisus means to kill on the way, as Diomedes and Odysseus kill the sleeping Thracians in Iliad 10. No elisions."""),
(245, 'cognovimus amnem.”',
 "Nor us the way deceives as we go:\nwe have seen in the dim valleys the edge of the city\nby constant hunting, and the whole we have come to know of the river.”",
 "Nor shall we lose our way: hunting there day after day we have caught sight of the outskirts of the city down in the shadowy valleys, and we know the whole course of the river.”",
 """'Nec nos via fallit euntis', 'nor does the road deceive us as we go', 'euntis' accusative plural, agreeing with 'nos'. 'primam… urbem', 'the first (part of) the city', its outskirts, as 'summus mons' is the top of the mountain; 'obscuris… sub vallibus', 'down in the dark valleys', enclosing it. 'venatu adsiduo', 'by constant hunting', ablative of means. 'amnem', the Tiber, the road to Pallanteum. Nisus's speech ends. Elisions 'venat(u) adsiduo', 'adsidu(o) et'."""),
(246, 'maturus Aletes:',
 "Here, with years heavy and of mind ripe, Aletes:",
 "At this Aletes, heavy with years and ripe in judgement, spoke:",
 """'Hic', 'at this point'. 'annis gravis', 'heavy with years'; 'animi maturus', 'ripe of mind', 'animi' a genitive (or old locative) of respect, as in 'aeger animi'. Aletes is one of the elder Trojans, last seen in the storm of Book 1 (1.121). The verb of speaking is left out again. Elision 'atqu(e) animi'."""),
(251, 'ora rigabat.',
 "“Gods of our fathers, under whose power Troy always is,\nnot after all utterly the Teucrians to destroy are you preparing,\nsince such spirits of young men and such sure you have brought forth\nhearts.” So saying, the shoulders and right hands he held\nof both, and his face with tears, and cheeks, was wetting.",
 "“Gods of our fathers, under whose protection Troy has always stood, you do not mean to wipe out the Trojans altogether after all, when you have given our young men such courage and such steadfast hearts.” As he said this he held them both by the shoulders and the right hand, and tears ran down his face and cheeks.",
 """The print has 'pectora. ”Sic', a misprint for 'pectora.” Sic', corrected here: the closing mark is set after the space and joined to the next word (as at 9.117 and 9.221). t keeps the print; since the mark is joined to 'Sic', this unit runs on to the end of the narrative sentence. Aletes's speech is broken off here by the narrative and resumed at 252. 'Di patrii', 'ancestral gods', the gods of Troy. 'sub numine', 'under the divine power', the protection of the gods. 'non tamen', 'not after all', for all our disasters. 'cum… tulistis', 'when you have brought forth', 'cum' with the indicative explaining what proves the point ('in that you have…'). 'talis', accusative plural. 'certa pectora', 'sure hearts', steadfast. 'memorans', 'saying', poetic for 'dicens'. 'voltum… atque ora', 'his face and cheeks', Greenough's 'voltum' for 'vultum'; 'rigabat', 'was wetting': old men and heroes weep freely in epic. Elisions 'Troi(a) est' (or 'Troia 'st'), 'iuven(um) et', 'ambor(um) et', 'atqu(e) ora'."""),
(253, 'solvi?',
 "“What for you, what worthy, men, for deeds of praise such\nrewards could I think can be paid?",
 "“What rewards, men, what rewards worthy of such glorious deeds could I think it possible to pay you?",
 """Aletes speaks again (252–256), so Greenough opens a new mark. 'Quae… quae digna… praemia', 'what, what worthy rewards', the question word doubled in his emotion, and 'praemia' held over to the next line. 'pro laudibus istis', 'for these praiseworthy deeds of yours', 'laudes' the deeds that earn praise, 'iste' of the persons spoken to. 'rear', present subjunctive of 'reor', deliberative, 'am I to think?' 'posse… solvi', 'can be paid', as a debt is paid. No elisions."""),
(256, 'immemor umquam.”',
 "The fairest, first,\nthe gods and your character will give, your own; then the rest will repay\nforthwith dutiful Aeneas and, untouched in years,\nAscanius, of a service so great not unmindful ever.”",
 "The finest reward of all the gods and your own hearts will give you first; then the rest will be repaid without delay by dutiful Aeneas and by Ascanius, who has his whole life before him and will never forget so great a service.”",
 """'Pulcherrima', 'the fairest (rewards)', neuter plural, 'praemia' understood. 'di moresque… vestri', 'the gods and your own character': the first reward of a good deed is the deed itself, and the gods' approval. 'reddet', singular, agreeing with the first of its two subjects. 'actutum', 'forthwith', an old adverb of early Latin verse and comedy. 'pius Aeneas', his standing epithet. 'integer aevi', 'untouched in age', 'aevi' genitive of respect: Ascanius's life is still all before him, so he will be remembering for a long time. 'meriti tanti… non immemor', 'not unmindful of so great a service', the two negatives making a strong positive (litotes). Aletes's speech ends. Elision 'atqu(e) integer'."""),
(260, 'obtestor;',
 "“Nay rather, I you, I whose only safety is in my father brought back,”\ntakes up Ascanius, “by the great, Nisus, Penates\nand Assaracus's Lar and of hoary Vesta the inner shrine\nadjure;",
 "“No, it is I,” Ascanius broke in, “I whose one hope of safety is my father's return, who implore you both, Nisus, by the great Penates, by the household god of Assaracus and the inner shrine of grey-haired Vesta;",
 """Ascanius's speech (257–280). 'Immo', 'nay rather', correcting Aletes: it is not for the Trojans to promise them rewards, it is for him to beg. 'ego vos… obtestor', 'I implore you', subject and object set side by side at the start and the verb held back three lines. 'cui sola salus (est) genitore reducto', 'for whom the only safety (lies in) my father brought back', an ablative absolute standing for a condition. 'excipit', 'takes up (the speech)', 'breaks in'. 'Nise', vocative: he turns to Nisus, who made the proposal, but 'vos' is both. 'penatis', accusative plural in '-is': the Penates, the gods of Troy's hearth that Aeneas carried out of the burning city. 'Assaraci… larem', 'the Lar of Assaracus', the hearth-god of the house of Assaracus, a king of Troy and Aeneas's great-grandfather. 'canae… Vestae', 'of hoary Vesta', the ancient goddess of the hearth, whose undying fire Hector's ghost gave Aeneas to carry away (2.296–297); 'penetralia', her innermost shrine. Elisions 'Imm(o) ego', 'lar(em) et'."""),
(261, 'pono gremiis:',
 "whatever to me of fortune and of trust there is,\nin your laps I place:",
 "whatever fortune, whatever hope I have, I lay in your laps:",
 """'quaecumque… fortuna fidesque est', 'whatever fortune and trust there is to me', the dative of possession (as 'sunt mihi'), the verb singular with the nearer subject. 'fides', here 'confidence', what he can rely on. 'in vestris… gremiis', 'in your laps', enclosing 'pono': to set a thing in someone's lap is to put it wholly into their keeping. Elision 'fidesqu(e) est' (or 'fidesque 'st')."""),
(262, 'triste recepto.',
 "call back my father,\ngive back the sight of him; nothing, he recovered, (is) sad.",
 "bring my father back, let me see him again; with him restored, nothing can grieve us.",
 """'revocate… reddite', two imperatives side by side without a connective (asyndeton), urgent. 'reddite conspectum', 'give back the sight (of him)'. 'nihil illo triste recepto', 'nothing (is) grievous, he having been recovered', an ablative absolute standing for a condition, with 'est' left out. No elisions."""),
(266, 'Sidonia Dido.',
 "Two I will give, wrought in silver and rough with figures,\ncups, which, Arisba conquered, my father took,\nand tripods twin, of gold two great talents,\na mixing-bowl, ancient, which gives Sidonian Dido.",
 "I will give you a pair of cups wrought in silver and rough with figures in relief, which my father took when he conquered Arisba, two matching tripods, two great talents of gold, and an ancient mixing-bowl, the gift of Sidonian Dido.",
 """The gifts are counted out like Agamemnon's offer to Achilles in Iliad 9, which also has tripods and talents of gold, women, and more besides if Troy is taken. 'Bina… pocula', 'cups in a pair', the distributive used for things that go in twos; 'pocula' is held over to the next line. 'argento perfecta', 'finished in silver'; 'aspera signis', 'rough with figures', embossed. 'devicta… Arisba', ablative absolute, 'Arisba having been conquered': a town of the Troad on the Hellespont, which in the Iliad sends men to fight for Troy; no other story of Aeneas taking it survives, and ancient commentators were puzzled by it. 'tripodas' and 'cratera' are Greek accusatives (plural and singular); 'cratera', the great bowl in which wine was mixed with water. 'talenta', the talent, a great weight of metal, here of gold. 'dat', 'gives', present for 'gave': the gift is still Dido's gift. 'Sidonia', 'of Sidon', the Phoenician city from which Dido came. Elisions 'perfect(a) atque', 'crater(a) antiquum'."""),
(270, 'aureus:',
 "But if to take Italy and of the sceptres to be master\nit shall have fallen to (him) as victor, and for the spoil to declare the lot,\nyou have seen on what horse Turnus, in what armour he went,\ngolden:",
 "But if it falls to my father as victor to take Italy, to win its throne and to share out the spoil by lot — you have seen the horse Turnus rode and the armour he went in, all gold:",
 """'Si vero', 'but if', 'vero' marking the step up to greater rewards still. 'contigerit', future perfect, 'shall have fallen (to his lot)'; 'victori', 'to (my father) as victor', dative with 'contingo'. 'sceptris potiri', 'to become master of the sceptres', 'potior' with the ablative; the plural for royal power. 'praedae dicere sortem', 'to declare the lot for the spoil', to divide the booty by lot. 'vidisti quo… equo, quibus… in armis', 'you have seen on what horse, in what arms', questions in the indicative, half exclamation, a loose and lively turn. 'aureus', 'golden', gleaming in gilded armour. In Iliad 10 the Trojan spy Dolon is promised the horses of Achilles; here the Trojan prince promises Turnus's. Elisions 'caper(e) Italiam', 'victor(i) et'."""),
(271, 'praemia, Nise.',
 "that very one, the shield and the crests red,\nI will take out from the lot, already now your rewards, Nisus.",
 "that very horse, the shield and the red-plumed crest, I will set apart before the lots are drawn: from this moment they are yours, Nisus.",
 """'ipsum illum', 'that very one', the horse. 'clipeum cristasque rubentis', 'the shield and the reddening crests', 'rubentis' accusative plural; the plural 'cristae' for the plumes of a single helmet. 'excipiam sorti', 'I will take out from the lot', reserve before the spoil is divided, 'sorti' dative of separation. 'iam nunc', 'even now', the promise as good as paid; 'tua praemia', in apposition. No elisions."""),
(274, 'ipse Latinus.',
 "Besides, twice six my father, the choicest of matrons,\npersons, and captives will give, and to all their own arms,\nover and above these, what of the plain the king himself holds, Latinus.",
 "Besides this, my father will give you twelve women, the choicest of their sex, and captive men, each with his own armour, and on top of all this whatever land King Latinus himself holds.",
 """'bis sex', 'twice six', twelve, a poetic way with numbers. 'lectissima matrum corpora', 'the choicest bodies of matrons', a periphrasis for 'the choicest women'; 'corpora' of persons, as of slaves. 'captivos', captive men; 'suaque omnibus arma', 'and to all of them their own arms', their armour going with them. 'insuper his', 'over and above these'. 'campi quod', 'what of land', 'campi' partitive genitive: the royal domain of Latinus, king of the Latins. Agamemnon's offer in Iliad 9 includes seven women, and twenty Trojan women more if Troy falls. Elision 'suaqu(e) omnibus'."""),
(277, 'casus complector in omnis.',
 "But you, whom my age by nearer laps\nfollows close, boy to be revered, now with my whole heart\nI receive, and as comrade embrace for all chances.",
 "As for you, honoured boy, whose years run only a little ahead of mine, I take you now to my heart with all my soul and embrace you as my companion in every fortune.",
 """Ascanius turns to Euryalus. 'Te vero', 'but you', set first for emphasis, the object of both 'accipio' and 'complector'. 'mea quem… aetas insequitur', 'whom my age follows close', 'spatiis propioribus', 'by nearer laps', a picture from the racecourse ('spatium', a lap of the track): Euryalus is only a little older, close enough to be a friend. 'venerande puer', 'boy to be honoured', the gerundive; Ascanius, a boy himself, honours him for his daring. 'casus… in omnis', 'for all chances', whatever may come; 'omnis' accusative plural. Elision 'accipi(o) et'."""),
(281, 'Euryalus:',
 "No for my affairs without you will be sought glory;\nwhether peace or wars I wage, in you the greatest, of deeds\nand of words, (will be) my trust.” In answer to whom such things speaks\nEuryalus:",
 "No glory shall I seek for my fortunes without you; whether I am at peace or at war, you shall have my fullest trust in all I do and say.” To him Euryalus answered:",
 """The print has 'fides. ”Contra', a misprint for 'fides.” Contra', corrected here: the closing mark is again joined to the next word; t keeps the print, so this unit runs on to 'Euryalus:'. 'meis… rebus', 'for my affairs', dative of advantage. 'quaeretur', 'will be sought'. 'seu… seu', 'whether… or'; 'geram', 'I wage', strictly the verb of war ('bellum gerere'), stretched to cover peace as well. 'tibi… fides (erit)', 'in you will be my trust', 'tibi' dative. 'rerum verborumque', 'of deeds and words', in everything I do and say. Ascanius's speech ends. 'quem contra', 'in answer to whom', 'contra' adverbial; 'talia fatur', 'speaks such things', the regular formula. 'Euryalus' is four syllables, Eu-ry-a-lus, with the Greek 'eu' a single long syllable. No elisions."""),
(283, 'adversa cadat.',
 "“Me no day from such brave venturings\nunlike shall prove; only — fortune, favourable\nor adverse, let it fall.",
 "“No day shall ever prove me unequal to this bold venture; only let fortune fall as it will, kind or cruel.",
 """Euryalus's speech (281–292). 'Me nulla dies… arguerit', 'no day shall prove me', 'arguerit' a future perfect (or a perfect subjunctive, 'would prove'); 'arguo', to show, to convict. 'tam fortibus ausis dissimilem', 'unlike such brave ventures', unequal to them; 'ausis', from 'ausum', a daring deed, dative with 'dissimilem'. 'tantum… cadat', 'only let (fortune) fall', a jussive subjunctive. Here the reading matters. Greenough prints 'aut adversa': 'only let fortune fall favourable or adverse', that is, I answer for my own courage, and the outcome I leave to fortune, whichever way it falls. The Latin Library prints 'haud adversa', the reading most editors prefer: 'only let fortune fall favourable, not adverse', my courage is sure, and my one prayer is for luck. l and i follow Greenough. Elision 'secund(a) aut'."""),
(286, 'regis Acestae.',
 "But you, above all gifts,\none thing I beg: a mother, of Priam's ancient race,\nI have, whom, poor woman, the Ilian land did not hold\nas she went out with me, nor the walls of King Acestes.",
 "But one thing I ask of you, above all gifts. I have a mother, of Priam's ancient line, poor woman, whom neither the land of Troy could hold back from leaving with me, nor the walls of King Acestes.",
 """'te… unum oro', 'I ask you one thing', 'oro' with a double accusative of the person and the thing. 'super omnia dona', 'above all gifts', beyond all you have offered. 'genetrix… est mihi', 'there is to me a mother', the dative of possession again; she is never named. 'Priami de gente vetusta', 'of the ancient stock of Priam', royal blood. 'quam miseram tenuit non… non', 'whom, poor woman, did not hold back… nor', the 'non' repeated (anaphora): not Troy, and not Sicily, where in Book 5 the weary and the women stayed behind in a city for Acestes (5.715–718); Nisus spoke of her in the last part (9.216–218). 'Ilia tellus', 'the land of Ilium', Troy. 'mecum excedentem', 'going out with me'. Elisions 'un(um) oro', 'mec(um) excedentem'."""),
(288, 'linquo:',
 "Her I now, unaware of this, whatever of danger it is,\nand unsaluted, leave:",
 "Now I am leaving her without a word of farewell, knowing nothing of this danger, whatever it may be:",
 """'ignaram huius quodcumque pericli est', 'unaware of this, whatever of danger it is', 'huius' and 'pericli' both hanging on 'ignaram'; 'pericli' = 'periculi', the shortened form usual in verse. 'inque salutatam' = 'insalutatamque', 'and unsaluted', the word split by its '-que' (tmesis), a much-quoted example. 'linquo', 'I leave', the simple verb for 'relinquo', poetic. Elisions 'ignar(am) huius', 'pericl(i) est' (or 'pericli 'st')."""),
(290, 'succurre relictae.',
 "night and your, as witness,\nright hand, that I could not the tears bear of my mother;\nbut you, I beg, console her helpless and come to the aid of her forsaken.",
 "night is my witness, and your right hand, that I could not bear my mother's tears; but you, I beg you, comfort her in her helplessness, and stand by her when she is left alone.",
 """The print has no mark after 'parentis' at the end of 289, a misprint (a stop dropped), corrected here: the 'quod' clause ends with the line, and 'at tu' begins a new clause. The lower-case 'at' suggests the lost mark was a semicolon or colon rather than a full stop, so l and i supply a semicolon. 'nox et tua… dextera (testis est)', 'night and your right hand are witness', 'testis' agreeing with the nearer subject; he is clasping Ascanius's hand. 'quod nequeam', 'that I could not', subjunctive because it is the thing the witnesses are called to vouch for, a kind of indirect statement. 'lacrumas', Greenough's old spelling of 'lacrimas'. 'parentis', 'of my parent', his mother. 'solare', imperative of the deponent 'solor'. 'inopem… relictae', 'helpless… forsaken', the two words saying what he is doing to her. Elisions 'solar(e) inopem', 'inop(em) et'."""),
(293, 'Dardanidae lacrimas;',
 "This let me hope carry, of you: bolder I shall go\ninto all chances.” Struck in mind, gave\nthe Dardanians tears;",
 "Let me take with me this hope in you, and I shall go the more boldly to meet whatever comes.” Their hearts were struck, and the Trojans wept;",
 """The print has 'omnis. ”Percussa', a misprint for 'omnis.” Percussa', corrected here: the third closing mark in this part joined to the word after it; t keeps the print, and the unit runs on to 'lacrimas;'. 'Hanc… spem', 'this hope'; 'sine me… ferre', 'allow me to carry', 'sine' the imperative of 'sino' (not the preposition). 'tui', 'of you', objective genitive, hope resting on you. 'audentior', 'bolder'. 'in casus omnis', 'into all chances', taking up Ascanius's 'casus… in omnis' (277). Euryalus's speech ends. 'Percussa mente', ablative absolute, 'their minds struck'. 'dedere' = 'dederunt'. 'Dardanidae', 'descendants of Dardanus', the Trojans. Elision 'tu(i) audentior'."""),
(294, 'pietatis imago.',
 "before all, handsome Iulus,\nand his mind was grazed by the image of love for a father.",
 "and handsome Iulus above all, for the picture of a son's love for his father touched his heart.",
 """'ante omnis', 'before all', more than any; 'omnis' accusative plural. 'pulcher Iulus', his epithet here and again at 310; 'dedit lacrimas' is understood from the line before. 'strinxit', 'grazed', touched lightly but sharply, like a blade's edge. 'patriae pietatis imago', 'the image of fatherly devotion': most take 'patriae' as 'toward a father', so that Euryalus's love for his mother calls up Ascanius's own love for Aeneas; some take it as 'his father's', Aeneas's famous 'pietas'. Either way his thought goes to Aeneas. Almost the same line returns at 10.824, 'et mentem patriae subiit pietatis imago', when Aeneas looks down at Lausus, killed defending his father. Elisions 'ant(e) omnis', 'atqu(e) animum'."""),
(296, 'omnia coeptis.',
 "Then thus he speaks out:\n“Be pledged things worthy of your mighty undertakings, all.",
 "Then he spoke: “You may count on everything that your great enterprise deserves.",
 """'Tum sic effatur' is a half-line: Virgil died leaving the Aeneid unrevised, and nearly sixty such unfinished lines stand in it. 'effatur', 'speaks out', from the solemn 'effor'. Ascanius's second speech (296–302). 'Sponde', 'pledge', 'be assured of': take it as promised. 'digna… omnia', 'all things worthy', framing the line; 'tuis ingentibus… coeptis', 'your mighty undertakings', ablative with 'digna'; 'coeptum' is a thing begun. No elisions."""),
(299, 'parva manet.',
 "For she will be to me a mother, and the name of Creusa\nalone will be lacking, nor for a birth such the gratitude\nsmall awaits.",
 "For she shall be a mother to me, lacking only the name of Creusa, and no small thanks are owed her for bearing such a son.",
 """'Namque erit ista mihi genetrix', 'for that mother of yours will be a mother to me', 'ista' the pronoun of the person spoken to, 'mihi' dative of possession. 'nomenque Creusae solum defuerit', 'and only the name of Creusa will be missing', 'defuerit' future perfect: Creusa, Ascanius's mother, was lost on the night Troy fell, and her ghost took leave of Aeneas in Book 2 (2.771–789). 'partum… talem', 'such a birth', bearing such a son; 'gratia… parva', 'small gratitude', 'manet', 'awaits', here transitive with 'partum' as its object: no small thanks awaits such a birth. Elision 'Namqu(e) erit'."""),
(300, 'ante solebat:',
 "Whatever chances the deed shall follow,\nby this head I swear, by which my father before was wont:",
 "Whatever the outcome of your deed, I swear by this head of mine, by which my father used to swear:",
 """'Casus… quicumque', 'whatever chances', framing the clause; 'factum sequentur', 'shall follow the deed', 'factum' accusative. 'per caput hoc iuro', 'I swear by this head', his own: to swear by a head was to stake a life on one's word. 'per quod pater ante solebat (iurare)', 'by which my father was wont (to swear) before', the infinitive understood: Aeneas used to swear by his son's life. No elisions."""),
(302, 'generique manebunt.”',
 "what to you I promise, returned, and with affairs prospering,\nthese same to your mother and your family shall remain.”",
 "all I promise you for your return and success shall be kept the same for your mother and your kin.”",
 """'quae… haec eadem', 'what things… these same things', the relative clause set before its antecedent. 'tibi… reduci', 'to you returned', 'reduci' dative of the adjective 'redux'; 'rebusque secundis', ablative absolute, 'and things going well'. 'matrique tuae generique', 'to your mother and your kin', the double '-que… -que'. 'manebunt', 'will remain', stand good even if you do not come back: a promise that looks ahead to the worst. Ascanius's speech ends. No elisions."""),
(305, 'aptarat eburna.',
 "So he speaks, weeping; from his shoulder at once he takes off his sword,\ngilded, which with marvellous art had made Lycaon\nof Cnossos, and handy in a scabbard had fitted, of ivory.",
 "So he spoke, in tears, and with that took from his shoulder his gilded sword, which Lycaon of Cnossos had made with marvellous skill and fitted, easy to draw, in an ivory scabbard.",
 """'inlacrimans', 'weeping', Greenough's 'inl-' for 'ill-'. 'umero… exuit', 'took off from his shoulder': the sword hung from a baldric over the shoulder, and he gives it to Euryalus. 'mira… arte', 'with marvellous art', framing 'quem fecerat'. 'Lycaon Gnosius', 'Lycaon of Cnossos', a Cretan smith otherwise unknown; 'Gnosius' is Greenough's spelling, more familiar as 'Cnosius'. 'habilem', 'handy', easy to draw; 'vagina… eburna', 'in an ivory scabbard', framing 'aptarat' = 'aptaverat', the syncopated pluperfect. The arming follows Iliad 10, where Diomedes and Odysseus are lent weapons before they set out. Elisions 'atqu(e) habilem', 'vagin(a) aptarat'."""),
(307, 'permutat Aletes.',
 "Gives to Nisus Mnestheus a hide, and of a shaggy lion\nthe spoils; his helmet faithful exchanges Aletes.",
 "Mnestheus gave Nisus the hide of a shaggy lion, and loyal Aletes exchanged helmets with him.",
 """'pellem horrentisque leonis exuvias', 'a hide and the spoils of a bristling lion', two nouns for one thing (hendiadys); 'horrentis' genitive singular. 'Mnestheus', two syllables, the Greek 'eu' one sound; he is one of the two captains in charge of the watch (9.171). 'galeam… permutat', 'exchanges his helmet', gives his own and takes Nisus's. 'fidus', 'faithful'. In Iliad 10 Meriones lends Odysseus a bow, a sword and a leather helmet. Elision 'pell(em) horrentisque'."""),
(310, 'prosequitur votis.',
 "At once, armed, they advance; whom, as they go, all\nthe band of the chiefs to the gates, of young and of old,\nescorts with prayers.",
 "Armed, they set out at once, and the whole company of leaders, young and old, went with them to the gates with prayers for their return.",
 """'Protinus', 'straightway'. 'quos… euntis', 'whom, going', 'euntis' accusative plural; 'omnis… manus', 'the whole band', framing 'euntis primorum'. 'iuvenumque senumque', 'of young and old', the double '-que… -que'. 'prosequitur votis', 'escorts with vows', sees them off with prayers for a safe return. Elision 'armat(i) incedunt'."""),
(312, 'mandata dabat portanda:',
 "And also handsome Iulus,\nbeyond his years a spirit and a care bearing manly,\nmany to his father messages was giving to be carried:",
 "Handsome Iulus too, with a man's spirit and a man's concern beyond his years, gave them many messages to carry to his father:",
 """'Nec non et', 'and not not… also', a double negative that adds: 'and also'. 'ante annos', 'before his years', beyond his age. 'animumque… curamque virilem', 'a man's spirit and a man's care', 'virilem' with both. 'multa… mandata', 'many instructions', framing 'patri'; 'dabat portanda', 'was giving to be carried', the gerundive of purpose with 'do'. Elision 'ant(e) annos'."""),
(313, 'inrita donant.',
 "but the breezes\nall tear apart, and to the clouds, unfulfilled, give them.",
 "but the winds tore them all to pieces and gave them to the clouds, to come to nothing.",
 """'aurae… discerpunt', 'the breezes tear apart', the vivid present; 'nubibus… donant', 'make a present of them to the clouds'; 'inrita', 'unaccomplished', Greenough's 'inr-' for 'irr-'. The messages will never reach Aeneas: the two will not get through. The picture is Catullus's, whose Ariadne says of Theseus's promises that the winds of the air tear them all apart, unfulfilled (64.142, 'quae cuncta aerii discerpunt irrita venti'); Virgil uses it again when Apollo grants half of Arruns's prayer and scatters the other half to the winds (11.794–795). No elisions."""),
]

P = A.part('aeneid-066'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
