# aeneid-089 (XI.725-835): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Tarcho et Venulus. Mors Camillae'
PART = "Tarchon's Rally and the Death of Camilla (XI.725–835)"
TITLE_EN = "Tarchon's Rally and the Death of Camilla — Aeneid XI.725–835"
ABOUT = ("Camilla's charge has broken the Etruscan horse, and Jupiter, watching from Olympus, stirs their leader Tarchon to rally them. "
"Tarchon rides among his men and shames them: a woman is routing them, and they are slow at nothing but love-making, dances and feasting. "
"Then he charges Venulus, the Latin envoy from Tibur, drags him off his horse and carries him away across his saddle, as an eagle carries off a struggling snake. "
"His men follow. Meanwhile Arruns, an Etruscan whom the fates have marked, stalks Camilla round the field, waiting for his chance. "
"She has fixed her eyes on Chloreus, a priest of Cybele in gorgeous Phrygian armour and gold, and pursues him blindly, eager for the spoils. "
"Arruns prays to Apollo of Mount Soracte, whose worshippers walk on burning coals: let him strike down this plague, and he will go home without glory. "
"Apollo grants half the prayer and lets the winds scatter the rest. The spear flies, unseen by Camilla, and lodges beneath her bared breast; Arruns runs off like a wolf that has killed a shepherd. "
"Dying, Camilla sends her companion Acca with a last message to Turnus, and her life departs in a line that Virgil will use again as the last line of the poem. "
"The battle flares up fiercer than before.")

U = [
(726, 'Olympo:',
 """But not these things with no eyes the sower of men and of gods\nobserving sits, high, on topmost Olympus:""",
 """But the father of men and gods was not watching these things with unheeding eyes as he sat on high on the summit of Olympus:""",
 """A new paragraph in Greenough. 'At non… nullis… oculis', 'not with no eyes', a double negative (litotes): Jupiter watches closely. 'hominum sator atque deorum', 'sower (begetter) of men and of gods', Jupiter, an Ennian title that renders Homer's 'father of men and gods'. 'summo… Olympo', ablative of place, 'on topmost Olympus', framing the line's end with 'altus', 'high', an adjective used where English wants an adverb. Zeus in the Iliad often watches the battle from Ida or Olympus and turns its course. No elisions."""),
(728, 'iras.',
 """the Tyrrhenian, Tarchon, the father into battles savage\nrouses, and with goads not gentle stirs his angers.""",
 """the Father rouses Tarchon the Etruscan to savage battle and spurs his anger with goads that are far from gentle.""",
 """'Tyrrhenum… Tarchonem', 'Tyrrhenian Tarchon': Tarchon is the leader of the Etruscans ('Tyrrheni'), who joined Aeneas in Book VIII and sailed with him in Book X. 'genitor', 'the father', Jupiter. 'in proelia saeva', 'into savage battles', the poetic plural. 'stimulis haud mollibus', 'with goads not soft', litotes again: the goad is the stick that drives oxen. 'incitat iras', 'stirs up his angers', the plural common in verse for a fit of rage. Elision 'Tarchon(em) in'."""),
(731, 'pulsos.',
 """Therefore amid slaughters and the yielding columns Tarchon\nis borne on his horse and with various cries goads the squadrons,\nby name each calling, and restores to battle the routed.""",
 """So Tarchon rides among the slaughter and the giving ranks, goading his squadrons with every kind of cry, calling each man by his name, and brings the routed back into the fight.""",
 """'inter caedes cedentiaque agmina', 'among slaughters and yielding columns', with a play of sound, 'caedes… cedentia'. 'fertur equo', 'is carried on his horse', rides. 'variis… vocibus', 'with various cries', now rebuke, now encouragement. 'alas', 'wings', the cavalry squadrons, as often. 'nomine quemque vocans', 'calling each by name', the commander's way in Homer (Agamemnon in Iliad X.68–69, from memory). 'reficit… pulsos', 'restores those driven back'. Elisions 'Erg(o) inter', 'cedentiaqu(e) agmina', 'variisqu(e) instigat', 'reficitqu(e) in'."""),
(733, 'venit?',
 """“What fear, O never going to feel the smart, O always sluggish\nTyrrhenians, what so great cowardice has come into your spirits?""",
 """“What are you afraid of, Etruscans, you who will never feel the sting of shame, you who are always idle? What is this great cowardice that has come over your hearts?""",
 """Tarchon's speech opens, without a verb of speaking, and runs to 740. 'Quis metus', 'what fear (is this)?', with 'est' left out. 'O numquam dolituri', 'O you who will never feel the pain', a future participle used as a noun: they will never resent their own disgrace. 'inertes', 'sluggish, idle'. 'animis', dative, 'into your spirits'. 'ignavia', 'cowardice, slackness'. The rebuke of men who give ground is Homeric: Agamemnon and Hector both shame their troops so (Iliad IV, V, from memory). Elisions 'dolitur(i) O', 'tant(a) animis'."""),
(734, 'vertit!',
 """A woman, scattered, drives you, and these columns turns!""",
 """A woman is chasing you in all directions and turning ranks like these to flight!""",
 """'Femina', put first with scorn: the point of the whole speech. 'palantis', 'straggling, scattered', the '-is' accusative plural (from 'palor'), with 'vos' understood: 'drives you as you scatter'. 'haec agmina', 'these columns', ours, with a gesture. 'vertit', 'turns', to flight. Elision 'atqu(e) haec'."""),
(735, 'dextris?',
 """To what end the steel, or why these do we carry, weapons useless, in our right hands?""",
 """What is our steel for, and why do we carry these useless weapons in our hands?""",
 """'Quo', 'whither?', here 'to what end?', with 'ferrum' and no verb: 'what is the iron for?'. 'quidve', 'or why', '-ve' 'or' joined to 'quid'. 'inrita', 'useless, ineffective', Greenough's spelling of the familiar 'irrita' (the prefix 'in-' kept unassimilated, as in 'adloquitur' at 821). 'dextris', 'in our right hands', the ablative of place without a preposition. Elisions 'quidv(e) haec', 'tel(a) inrita'."""),
(740, 'altos!”',
 """But not for Venus slow and for nocturnal wars,\nor when the curved has proclaimed the dances, the pipe of Bacchus,\nwait for the feasts and the cups of the full table\n(this your love, this your zeal) until the rites the favourable soothsayer\nannounce, and to the groves calls the victim, fat, deep!”""",
 """You are not slow when it comes to love and the battles of the night, or when the curved pipe calls you to the dances of Bacchus: wait, then, for the banquets and the cups on the laden table (this is your passion, this your one pursuit), until the soothsayer declares the omens good and the fat victim summons you to the depths of the sacred groves!”""",
 """'At non… segnes', 'but (you are) not sluggish', with 'estis' left out: for love they have energy enough. 'in Venerem', 'for Venus', for love-making; 'nocturna… bella', 'night wars', love's battles, a common figure in Latin love poetry. 'curva… tibia Bacchi', 'the curved pipe of Bacchus', the Phrygian pipe with a bent horn at the end, framing the line; 'indixit choros', 'has proclaimed the dances'. 'exspectate', a scornful imperative, 'go and wait for'. 'hic amor, hoc studium', with 'est' understood. 'dum… nuntiet… vocet', 'dum' with the subjunctive, 'until'. The Etruscans were famous both for luxury and for their 'haruspices', who read the entrails of victims; the sacrificial meal follows in the sacred grove. The speech ends at 740. No elisions."""),
(744, 'aufert.',
 """These things having spoken, his horse into the midst, ready to die himself too,\nhe spurs, and at Venulus, facing him, he hurls himself, wild,\nand, torn down from his horse, with his right hand clasps his enemy,\nand, before his own lap, with much force, aroused, he carries him off.""",
 """With these words he spurs his horse into the thick of the fight, ready to die himself as well, and hurls himself in a fury straight at Venulus; he tears his enemy from his horse, grips him in his right arm, and with a mighty effort carries him off in front of him across his saddle.""",
 """'Haec effatus', 'having spoken these things', the deponent 'effor'. 'moriturus et ipse', 'about to die himself too': ready to die, not doomed to; Tarchon survives the book. 'Venulo adversum', 'facing Venulus', 'adversum' an adjective with 'se'. Venulus is the envoy whom the Latins sent to Diomedes in Argyripa to ask for help (VIII.9; his report, XI.242–295); he is from Tibur ('Tiburtum', 757). 'dereptum', 'torn down'. 'gremium ante suum', 'before his own lap', across his horse's withers. 'concitat… concitus', the same verb twice. Elisions 'equ(um) in', 'Venul(o) adversum', 'dereptumqu(e) ab', 'gremi(um) ante'."""),
(746, 'oculos.',
 """Is raised to the sky a shout, and all the Latins\nturned their eyes.""",
 """A shout goes up to the sky, and all the Latins turn their eyes to see.""",
 """'Tollitur in caelum clamor', the Homeric shout that goes up to heaven. 'cunctique Latini', 'and all the Latins'. 'convertere', the shortened third person plural perfect, '-ere' for '-erunt' (you have seen it often: 'tenuere', 'fecere'). The present 'tollitur' then the perfect 'convertere': the shout rises, and at once every eye is turned. Elision 'converter(e) oculos'."""),
(747, 'ferens;',
 """Flies, fiery, over the plain Tarchon\narms and a man carrying;""",
 """Tarchon flies like fire across the plain, carrying the arms and the man;""",
 """'Volat', 'flies', put first for speed. 'igneus', 'fiery', of the rider's heat and speed. 'aequore', 'over the level', ablative of the way: 'aequor' is any flat surface, here the plain. 'arma virumque ferens', 'carrying arms and a man': the poem's first words, 'Arma virumque', used again with a smile, for Tarchon is carrying off a man in armour. No elisions."""),
(749, 'ferat;',
 """then from the top of his own spear\nhe breaks off the iron and searches out the parts exposed,\nwhere a wound deadly he may bring;""",
 """then he breaks off the iron head from the tip of the man's own spear and searches for an open place where he can deal a fatal wound;""",
 """'summa ipsius ab hasta', 'from the top of his own spear', that of Venulus: 'ipsius' points to the captive, not Tarchon. 'ipsius' is scanned with the middle 'i' long, as usual. 'defringit', 'breaks off'. 'partis… apertas', 'the open parts', the '-is' accusative plural: the gaps in the armour. 'rimatur', 'searches out', from 'rima', a crack. 'qua… ferat', 'by which way he may bring', a relative clause of purpose. Elisions 'summ(a) ipsius', 'ferr(um) et'."""),
(750, 'exit.',
 """against him that one resisting\nholds off from his throat the right hand and force with force evades.""",
 """the other fights back, holding the hand away from his throat, and meets force with force to escape it.""",
 """'contra ille repugnans', 'on the other side he (Venulus), fighting back'. 'sustinet a iugulo dextram', 'holds the right hand away from his throat'. 'vim viribus exit', 'escapes force by force': 'exit' is used transitively, 'avoids', as of dodging a weapon in the boxing match of Book V ('tela exit', V.438, from memory). 'vim viribus', two forms of the same noun side by side, a figure Virgil likes. Elisions 'contr(a) ille', 'dextr(am) et'."""),
(755, 'insurgens;',
 """And as, flying high, when, carried off, the tawny a serpent\nbears, eagle, and has entwined her feet and with her talons clung,\nbut wounded the serpent its sinuous coils turns\nand with raised bristles with scales and hisses with its mouth,\ntowering, rearing up;""",
 """And as when a tawny eagle flies high, carrying a snake she has snatched up, her feet wound about it and her talons fast in it, and the wounded serpent writhes its twisting coils, bristles with its scales on end and hisses with its mouth, rearing high;""",
 """A long simile. 'Utque… cum', 'and as when'. 'raptum… draconem', 'a snake carried off'; 'draco' is a snake, not a dragon. 'fulva… aquila', 'the tawny eagle', framing. 'implicuit… haesit', perfects among presents: her grip is already fast. 'saucius at serpens', with 'at', 'but', put second. 'sinuosa volumina', 'winding coils'. 'adrectis… squamis', ablative absolute, 'with scales raised'; the Latin Library spells it 'arrectis'. The model is the omen of Iliad XII.200–207, where an eagle carries a live snake over the Trojans and the snake bites it till it drops it (from memory). Elisions 'aquil(a) implicuitque', 'atqu(e) unguibus', 'adrectisqu(e) horret'."""),
(756, 'alis:',
 """she no less presses with hooked\nthe struggling one, with beak, at the same time the air beats with her wings:""",
 """she presses the struggling creature no less hard with her hooked beak, and all the while beats the air with her wings:""",
 """'illa', the eagle, set against 'serpens'. 'haud minus', 'no less', litotes. 'obunco… rostro', 'with hooked beak', the adjective at the end of one line and the noun in the next, with 'luctantem', 'the struggling one', the snake, between. 'aethera', Greek accusative of 'aether', 'the upper air'. 'verberat alis', 'beats with her wings'. In Homer's version the snake wins; here, as in Tarchon's case, the bird keeps its prey. Elision 'ill(a) haud'."""),
(758, 'ovans.',
 """not otherwise his prey out of the column of the Tiburtines Tarchon\ncarries, exulting.""",
 """even so Tarchon carries off his prey from the ranks of the men of Tibur in triumph.""",
 """'haud aliter', 'not otherwise', the usual turn back from the simile to the story. 'praedam', 'his prey', the word of the hunt. 'Tiburtum', genitive plural of 'Tiburtes', the people of Tibur (Tivoli), with the old short ending '-um'. 'ovans', 'exulting', from 'ovo'; the 'ovatio' was the lesser triumph at Rome, a general entering the city on foot or horseback. Elision 'Tiburt(um) ex'."""),
(759, 'incurrunt.',
 """The leader's example and success having followed,\nthe Maeonians charge in.""",
 """Following their leader's example and his success, the Etruscans charge.""",
 """'Ducis exemplum eventumque', 'the example and the outcome of their leader': they copy what he did and are encouraged by how it went. 'secuti', perfect participle of the deponent 'sequor', with present sense. 'Maeonidae', 'Maeonians', that is Lydians: the Etruscans were believed to have come from Lydia in Asia Minor (Herodotus I.94, from memory), and Virgil calls them so again and again. Elisions 'exempl(um) eventumque', 'Maeonid(ae) incurrunt'."""),
(761, 'temptat.',
 """Then, to the fates owed, Arruns\nthe swift Camilla, with his javelin and with much cunning ahead,\ncircles, and what may be the chance most easy, he tries.""",
 """Then Arruns, whose death was owed to the fates, circles swift Camilla, javelin in hand and well ahead of her in cunning, and tries to find which chance will be the easiest.""",
 """'fatis debitus', 'owed to the fates': his death is fixed. Diana has sworn that whoever wounds Camilla will pay with his blood (XI.591–592), and the reader knows it. Arruns is an Etruscan, one of Tarchon's men. 'velocem… Camillam', framing the line. 'iaculo', 'with his javelin', best taken with 'circuit' (some join it with 'velocem'). 'multa prior arte', 'ahead (of her) in much craft', getting the start by cunning. 'quae sit… facillima', indirect question. 'circuit', 'goes round', two syllables by contraction or three; the metre takes three, 'circuĭt'. Elision 'iacul(o) et'."""),
(763, 'lustrat;',
 """Wherever herself, raging, in the middle of the column has carried, the maiden,\nthere Arruns goes after, and silent her tracks scans;""",
 """Wherever the maiden carried herself in her fury through the midst of the ranks, Arruns followed close and silently traced her tracks;""",
 """'Qua se cumque', 'wherever', the relative 'quacumque' split by 'se' (tmesis, 'cutting', of a compound word). 'qua… hac', 'by which way… by that way', the pattern repeated in the next sentence. 'furens', 'raging', in the fury of her fighting. 'subit', 'comes up behind'. 'tacitus', 'silent', an adjective where English uses an adverb. 'vestigia lustrat', 'scans her footprints', like a hunter. No elisions."""),
(765, 'habenas.',
 """where victorious returns she and her foot from the enemy brings back,\nthere the youth by stealth his swift twists aside reins.""",
 """where she came back victorious and withdrew her step from the foe, there the young man stealthily turned aside his swift reins.""",
 """'victrix', 'victorious', feminine of 'victor'. 'pedemque ex hoste reportat', 'brings her foot back from the enemy', a solemn way of saying she withdraws. 'iuvenis', 'the young man', Arruns. 'furtim', 'by stealth'. 'celeris… habenas', 'swift reins', the '-is' accusative plural: the speed belongs to the horse, but the adjective is given to the reins (transferred epithet). 'detorquet', 'twists aside'. Elision 'pedemqu(e) ex'."""),
(767, 'hastam.',
 """These approaches and now these approaches and the whole he wanders\non every side circuit, and his sure shakes, persistent, spear.""",
 """He tries this approach and now that, wanders round her on every side, and shakes his unerring spear, relentless.""",
 """'Hos aditus iamque hos aditus', 'these approaches and now these', the repetition showing his patient searching. 'pererrat… circuitum', 'wanders over the whole circuit'. 'certam… hastam', 'his sure spear', framing, and 'sure' because the reader knows the end. 'improbus', 'shameless, persistent', a word of blame for a stubborn, unscrupulous effort. 'quatit', 'shakes', poising it for the throw. Elisions 'iamqu(e) hos', 'circuit(um) et'."""),
(771, 'tegebat.',
 """By chance, sacred to Cybelus, Chloreus, and once a priest,\nconspicuous far off, in Phrygian was shining arms,\nand his foaming was driving horse, which a hide with bronze\nin the manner of plumage scales, with gold joined, covered.""",
 """It happened that Chloreus, sacred to Mount Cybelus and once its priest, was shining far and wide in his Phrygian armour and urging on his foaming horse, which was covered with a hide set with bronze scales laid like feathers and fastened with gold.""",
 """'Forte', 'by chance', marks a new figure. 'sacer Cybelo', 'sacred to Cybelus', the mountain in Phrygia that gave Cybele, the Great Mother, her name; Chloreus is her priest, a Trojan. 'olimque sacerdos', 'and once a priest', perhaps in Troy. 'Chloreus', two syllables, 'eu' a Greek diphthong. 'insignis longe', 'conspicuous far off'. 'pellis aënis… squamis… conserta', 'a hide joined with bronze scales', 'in plumam', 'in the manner of feathers'; 'aënis', three syllables (the mark shows the vowels are separate), and 'auro', 'with gold' thread or wire. Elision 'spumantemqu(e) agitabat'."""),
(773, 'cornu;',
 """Himself, with foreign rust-red bright and with purple,\nwas shooting shafts, from a Lycian, Gortynian, horn-bow;""",
 """He himself, bright with foreign dark red and with crimson, was hurling Cretan arrows from a Lycian bow;""",
 """'Ipse', the rider, after the horse. 'peregrina ferrugine… et ostro', 'with foreign rust-colour and purple', two dyes of his clothes: 'ferrugo' is the dark red of iron rust, 'ostrum' the purple of the shellfish. 'spicula… Gortynia', 'Gortynian darts', from Gortyn in Crete, whose archers were famous; 'Lycio… cornu', 'with a Lycian horn', a bow (bows were made of horn) from Lycia, the land of Apollo the archer. The words interlock, 'Lycio Gortynia cornu', and the names gather the archer-lands of the old world. 'torquebat', 'was whirling, hurling'. No elisions."""),
(775, 'cassida;',
 """golden from his shoulders was the bow, and golden to the seer\nthe helmet;""",
 """the bow on his shoulders was golden, and golden the seer's helmet;""",
 """'aureus… arcus et aurea… cassida', 'golden bow and golden helmet', the adjective repeated (anaphora): gold is everything about him. 'ex umeris', 'from his shoulders', hanging there. 'vati', dative of possession, 'to the seer (was)': a priest of Cybele was also a 'vates', a prophet. 'cassida', a rare form of 'cassis', 'helmet', with a Greek-looking first-declension ending. No elisions."""),
(777, 'crurum.',
 """then the saffron cloak and the folds rustling\nof linen with tawny into a knot he had gathered gold,\nembroidered with needle as to his tunics and the barbarian coverings of his legs.""",
 """his saffron cloak and its rustling linen folds he had gathered in a knot with a brooch of yellow gold, and his tunic and his foreign leggings were embroidered with the needle.""",
 """'croceam chlamydemque sinusque crepantis carbaseos', 'saffron cloak and rustling linen folds', with the double '-que… -que', 'both… and'; 'crepantis', '-is' accusative plural, 'crackling, rustling'. 'carbaseos', 'of fine linen'. 'fulvo… auro', 'with tawny gold', a brooch, framing 'in nodum'. 'pictus acu tunicas', 'painted with the needle as to his tunics', embroidered: a passive participle with a Greek accusative of respect, like 'unum exserta latus' at 649. 'barbara tegmina crurum', 'barbarian coverings of the legs', trousers, the mark of the eastern foreigner to a Roman eye. Elision 'fulv(o) in'."""),
(782, 'amore,',
 """Him the maiden, whether that on temples she might fix arms\nTrojan, or that in captured she might parade herself in gold,\na huntress, him alone out of all the contest of the battle\nblind was following, and through the whole, heedless, column\nwith a womanly for booty and for spoils was burning love,""",
 """Him alone, out of all the struggle of the battle, the maiden was following blindly, whether to hang Trojan armour in a temple or to parade herself, a huntress, in captured gold; heedless through the whole host, she burned with a woman's love of booty and of spoils,""",
 """The period runs from 778 to 784; it is cut at the comma. 'Hunc… unum', 'him alone', framing. 'sive ut… sive ut', 'whether in order to… or to', two purpose clauses. 'templis praefigeret arma', 'fix the arms on temples', dedicating spoils to a god. 'Troïa', three syllables. 'venatrix', 'huntress', Diana's follower even here. 'caeca… incauta', 'blind… unwary', the narrator's warning. 'femineo… amore', 'with a womanly love', the poet's own judgement; but men too die for spoils in this poem, Euryalus for a helmet (IX.359–374) and Turnus, at the end, for Pallas's belt. Elisions 'siv(e) ut' twice, 'un(um) ex', 'totumqu(e) incauta', 'praed(ae) et', 'spolior(um) ardebat'."""),
(784, 'precatur:',
 """when a weapon from his ambush, at last, his moment seized,\nhe hurls, and the gods above Arruns thus with his voice prays:""",
 """when at last, seizing his moment, Arruns hurls a spear from his hiding place, and prays aloud to the gods above in these words:""",
 """'cum… concitat', 'when (at last) he hurls', the 'inverted' cum-clause: the main event comes in the clause with 'cum', after the long description, as so often in narrative. 'ex insidiis', 'from ambush'. 'tempore capto', ablative absolute, 'the time seized'. 'superos', 'those above', the gods. 'sic voce precatur', 'prays thus with his voice': the prayer is spoken as the spear flies. Elision 'tel(um) ex'."""),
(788, 'pruna,',
 """“Highest of gods, of holy guardian Soracte, Apollo,\nwhom first we worship, for whom the pine fire on the heap\nis fed, and through the midst, trusting in piety, the fire\nwe worshippers press our steps on the many coal,""",
 """“Apollo, highest of the gods, guardian of holy Soracte, you whom we worship before all others, for whom the fire of pine is fed upon its heap and through whose flames we, your worshippers, trusting in our devotion, tread with our feet on many a glowing coal,""",
 """Arruns's prayer opens; it runs to 793. The period runs from 785 to 790 and is cut at the comma. 'deum', the old genitive plural '-um'. Soracte is the mountain north of Rome, visible from the city; on it, at Apollo's festival, the families called 'Hirpi Sorani' walked barefoot over burning embers unharmed (Pliny the Elder, from memory). 'primi', 'first', before all others. 'pineus ardor', 'the pine blaze'. 'freti pietate', 'relying on our piety', 'fretus' with the ablative. 'multa… pruna', 'on much live coal', collective singular, framing 'premimus vestigia'. A prayer begins, in the old form, by naming the god's titles and services. No elisions."""),
(790, 'omnipotens.',
 """grant, father, this from our to be wiped out disgrace arms,\nall-powerful.""",
 """grant, father, almighty one, that this disgrace be wiped out by our arms.""",
 """The request, after the god's titles. 'da… aboleri', 'grant (this) to be abolished', 'do' with an infinitive, poetic. 'hoc… dedecus', 'this disgrace', the shame of being routed by a woman, Tarchon's point at 734. 'nostris… armis', 'by our arms', or 'from our arms'. 'pater', 'father', a title of any great god. 'omnipotens', 'all-powerful', usually Jupiter's title, is given to Apollo here, held over to the next line and set off by the pause: the prayer flatters. No elisions."""),
(792, 'ferent):',
 """Not the stripped arms or the trophy of the routed\nmaiden, or any spoils do I seek (for me other deeds glory\nwill bring):""",
 """I do not ask for the armour stripped from the routed maiden, nor for a trophy, nor any spoils (other deeds will win me glory):""",
 """'exuvias', 'stripped things', the armour taken off a dead enemy. 'pulsaeve… virginis', 'or of the routed maiden'. 'tropaeum', a trophy, the enemy's arms set up on a post where he was routed. 'mihi cetera… facta ferent', 'other deeds will bring me (glory)': a proud parenthesis. 'laudem', 'praise, glory', put at the end of 791. Arruns does not want what Camilla wants (782); he is willing to be 'inglorius'. Elision 'spoli(a) ulla'."""),
(793, 'urbes.”',
 """let this dread, by my wound, if only plague\nfall, struck, I will return inglorious to my father's cities.”""",
 """only let this dread scourge fall, struck down by my wound, and I will go back to the cities of my fathers without glory.”""",
 """'dum… cadat', 'if only… may fall', 'dum' with the subjunctive in a proviso, 'provided that' (also 'dummodo'). 'haec dira… pestis', 'this dread plague', framing. 'meo… vulnere', 'by a wound from me', the possessive standing for the agent. 'pulsa', 'struck'. 'patrias… urbes', 'my fathers' cities', the accusative of goal without a preposition. 'remeabo', 'I will go back'. 'inglorius', 'without glory'. He will indeed not return. The speech ends at 793. No elisions."""),
(795, 'auras:',
 """Heard him, and of the prayer that should succeed a part,\nPhoebus granted in his mind, a part into the winged scattered breezes:""",
 """Phoebus heard, and in his mind granted that one part of the prayer should succeed, and scattered the other to the flying breezes:""",
 """'Audiit', 'heard', the perfect of 'audio' without the 'v'. 'voti… partem… partem', 'part of the vow… part', the second 'partem' answered by 'dispersit'. 'succedere… dedit', 'granted (it) to succeed', 'do' with the infinitive as at 789. 'mente', 'in his mind', silently. 'volucris… auras', 'the winged breezes', the '-is' accusative plural. The model is Iliad XVI.249–252, where Zeus grants one half of Achilles' prayer for Patroclus and refuses the other (from memory). No elisions."""),
(797, 'oranti;',
 """that he should lay low by sudden, confounded, death Camilla,\nhe nodded assent to him praying;""",
 """he nodded his assent to the man's prayer that he should strike Camilla down, thrown into confusion by sudden death;""",
 """'sterneret ut', 'that he should lay low', with 'ut' put second, an indirect command depending on 'adnuit'. 'subita… morte', 'by sudden death', framing 'turbatam', 'thrown into confusion'. 'adnuit', 'nodded', the god's nod that makes a thing certain. 'oranti', dative, 'to the one praying', the present participle used as a noun. No elisions."""),
(798, 'procellae.',
 """that returning his high fatherland should see him,\nhe did not grant, and into the South Winds the voice turned the blasts.""",
 """that his lofty homeland should see him come home, he did not grant, and the storm-gusts carried his words away on the south winds.""",
 """'reducem ut patria alta videret', 'that his high fatherland should see him returning', 'ut' again postponed; 'patria alta', 'high', perhaps for the hill-towns of Etruria, perhaps just 'noble'. 'reducem', 'brought back', home. 'non dedit', 'did not grant', the bare phrase emphatic. 'Notos', Greek accusative plural of 'Notus', the south wind. 'vertere', '-ere' for '-erunt'. 'procellae', 'gusts'. Elisions 'reduc(em) ut', 'patri(a) alta'."""),
(801, 'Volsci.',
 """Therefore when sent from his hand gave a sound the spear through the air,\nturned their minds, keen, and their eyes carried\nall to the queen the Volscians.""",
 """So when the spear, flung from his hand, sent its whirr through the air, all the Volscians turned their keen attention and their eyes towards their queen.""",
 """'Ergo ut', 'so when'. 'missa manu… hasta', 'the spear sent from his hand', framing the clause. 'sonitum dedit', 'gave a sound', whirred. 'convertere… tulere', the shortened perfects ('-ere' for '-erunt') again, one for the minds and one for the eyes. 'acris', with 'animos', the '-is' accusative plural, 'keen'. 'cuncti… Volsci', 'all the Volscians', Camilla's own people, the subject held to the end. 'reginam', 'the queen', Camilla. Elisions 'converter(e) animos', 'cunct(i) ad'."""),
(804, 'cruorem.',
 """Not at all herself, either of the air\nor of the sound mindful, or of the weapon coming from the sky,\nthe spear, until, under her bared carried home breast,\nlodged, and the maiden's deep drank, driven, blood.""",
 """She alone was not aware of the rush of air, or of the sound, or of the weapon coming down from the sky, until the spear went home under her bare breast, lodged there, and drove deep, drinking her virgin blood.""",
 """'Nihil… memor', 'not at all aware', 'nihil' as an adverb; 'ipsa', 'she herself', set against all her watching people, with 'erat' left out. 'nec… nec… aut', 'neither… nor… or'. 'ab aethere', 'from the upper air', for the spear's long flight. 'donec… haesit', 'until… stuck', the perfect indicative of fact. 'exsertam papillam', 'her bared breast', recalling the Amazon's bare side at 649. 'bibit… cruorem', 'drank the blood': the spear is thirsty, as Homer's spears long to taste flesh (Iliad XXI.70, from memory). 'acta', 'driven'. Elision 'virgineumqu(e) alte'."""),
(806, 'suscipiunt.',
 """Run together, trembling, her companions, and their mistress falling\nthey catch up.""",
 """Her companions run to her in alarm and catch their mistress as she falls.""",
 """'Concurrunt', 'run together', put first. 'trepidae comites', 'her trembling companions', feminine: the band named at 655–656, Larina, Tulla and Tarpeia. 'dominam', 'their mistress', a word of the household. 'ruentem', 'falling', present participle: they catch her as she sinks. 'suscipiunt', 'take up from below, support'. No elisions."""),
(808, 'audet.',
 """Flees before all, terrified, Arruns,\nwith joy and with mingled fear, and no longer any more to his spear\nto trust or to the weapons to oppose himself of the maiden does he dare.""",
 """Arruns, terrified, flees before anyone else, with joy and fear mixed in him, and no longer dares to trust his spear or to face the maiden's weapons.""",
 """'Fugit ante omnis', 'flees before all', first of all, 'omnis' the '-is' accusative plural. 'exterritus', 'terrified', 'ex-' strengthening the verb. 'laetitia mixtoque metu', 'with joy and fear mixed', the ablative: his feeling is both at once. 'nec iam amplius', 'no longer any more'. 'hastae credere', 'to trust his spear', the dative with 'credo'. 'telis occurrere virginis', 'to meet the maiden's weapons', even now that she is dying. Elisions 'ant(e) omnis', 'i(am) amplius'."""),
(813, 'petivit:',
 """And as that one, before the weapons hostile should follow,\nat once into the mountains himself, off the road, has hidden, high,\nthe shepherd killed, the wolf, or a great bullock,\nconscious of his bold deed, and his tail drawing back\nhas tucked, trembling, under his belly, and the woods has sought:""",
 """And as a wolf that has killed a shepherd or a great bullock at once hides himself off the beaten track in the high mountains before hostile spears can follow, knowing his deed was a bold one, drawing back his tail to tuck it quivering beneath his belly, and makes for the woods:""",
 """A simile. 'ille… lupus', 'that wolf', 'ille' as in many similes, almost like the Greek article, 'the well-known kind'. 'prius quam… sequantur', 'before (the weapons) can follow', the subjunctive of anticipation. 'abdidit… subiecit… petivit', perfects of habitual action in a comparison (the 'gnomic' perfect): this is what a wolf does. 'avius', 'off the road', an adjective for an adverb. 'occiso pastore… magnove iuvenco', ablative absolute, 'a shepherd or a great bullock killed'. 'remulcens', 'drawing back'. 'subiecit' with consonantal 'i', sub-je-cit. The model is Iliad XV.586–590, where Antilochus flees like a beast that has killed a dog or a herdsman (from memory). Elisions 'tel(a) inimica', 'continu(o) in', 'ses(e) avius', 'pavitant(em) utero'."""),
(815, 'armis.',
 """not otherwise from their eyes himself, troubled, took away Arruns,\nand content with flight among the midst mingled himself, the arms.""",
 """even so Arruns, in his agitation, took himself out of their sight and, content to escape, lost himself among the armed throng.""",
 """'haud secus', 'not otherwise', the return from the simile. 'ex oculis se… abstulit', 'removed himself from (their) eyes'. 'turbidus', 'disturbed, in turmoil', an adjective for his state. 'contentus fuga', 'content with flight', with the ablative: he wants nothing more, as he said in his prayer. 'mediis se immiscuit armis', 'mingled himself with the midst of the arms', armed men; 'arma' for the soldiers who bear them. Elision 's(e) immiscuit'."""),
(817, 'mucro:',
 """She with her hand, dying, the weapon pulls, but between the bones\nthe iron at the ribs in the deep stands wound point:""",
 """She, dying, tugs at the spear with her hand, but the iron point stands fast among the bones by her ribs in the deep wound:""",
 """'Illa', Camilla, set first: the poem returns to her. 'manu… trahit', 'pulls with her hand', tries to draw it out; the present for vividness. 'ossa… inter', 'between the bones', the preposition after its noun (anastrophe), with 'sed', 'but', put second in its clause. 'ferreus… mucro', 'the iron point', framing the line. 'alto… vulnere', 'in the deep wound'. 'stat', 'stands fast'. No elisions."""),
(819, 'reliquit.',
 """she sinks bloodless, sink, cold in death,\nher eyes, the once rosy colour her face has left.""",
 """she sinks down drained of blood; her eyes sink too, cold in death, and the colour that once glowed in her face is gone.""",
 """'labitur… labuntur', 'she slips… slip', the same verb twice, first of her body, then of her eyes: anaphora without a connective (asyndeton). 'exsanguis', 'bloodless'. 'frigida leto lumina', 'eyes cold with death', 'lumina', 'lights', the poetic word for eyes. 'purpureus… color', 'the bright colour', 'purpureus' in verse often of any glowing hue, here the bloom of life. 'quondam', 'once'. 'ora', 'face', poetic plural. 'reliquit', the perfect: it has left her. No elisions."""),
(822, 'fatur:',
 """Then thus breathing out Acca, of those her own age one,\nshe addresses, faithful before others, who alone to Camilla\n(was the one) with whom to share her cares; and these things so she speaks:""",
 """Then, as she breathed her last, she spoke to Acca, one of the girls of her own age, faithful above all the rest, the only one with whom Camilla used to share her cares; and these were her words:""",
 """'exspirans', 'breathing out', dying. 'ex aequalibus unam', 'one of her equals in age'. 'fidam ante alias', 'faithful before others', agreeing with 'Accam'; the Latin Library reads 'fida', which would go with 'quae', 'who alone was faithful to Camilla', a different construction and a slightly different sense. 'quae sola Camillae, quicum partiri curas', 'who alone (was) to Camilla (one) with whom to share cares', a compressed phrase, 'erat' understood. 'quicum', the old ablative 'qui' for 'qua' with 'cum'. 'haec ita fatur', 'speaks thus'. Elisions 'Acc(am) ex', 'fid(am) ante', 'ant(e) alias', 'atqu(e) haec'."""),
(824, 'circum.',
 """“So far, Acca, sister, I have been able: now the wound bitter\nfinishes me, and with shadows grows black all around.""",
 """“Thus far, Acca, my sister, I have had the strength: now the cruel wound is ending me, and all around me everything grows black with darkness.""",
 """Camilla's last words open; they run to 827. 'Hactenus… potui', 'thus far I have been able', 'I have done what I could'. 'soror', 'sister', in affection: Acca is a comrade, not a sister. 'conficit', 'finishes off', the verb of killing. 'tenebris nigrescunt omnia circum', 'all things around grow black with darkness', the darkness of death that covers the eyes in Homer. 'circum', adverb, 'round about'. No elisions."""),
(825, 'perfer:',
 """Flee away and these to Turnus instructions, the last, carry through:""",
 """Get away from here and carry these last instructions to Turnus:""",
 """'Effuge', 'flee away', 'ex-' strengthening the verb: she is to get out of the fighting and reach Turnus, who lies in ambush in the hills. 'mandata novissima', 'last commands', 'novissimus', 'newest', in the sense 'last'. 'perfer', 'carry through', all the way to him. Elision 'Effug(e) et'."""),
(826, 'urbe.',
 """let him take my place in the battle and keep the Trojans from the city.""",
 """let him take my place in the battle and keep the Trojans away from the city.""",
 """The message itself, in two jussive subjunctives, 'succedat… arceat', 'let him succeed… let him keep off'. 'succedat pugnae', 'come up into the fight', take over her command, with the dative. 'arceat urbe', 'keep from the city', the ablative of separation: Latinus's city, now without its cavalry screen. The message will reach Turnus and draw him out of his ambush, the turning point of the book. Elision 'Troianosqu(e) arceat'."""),
(827, 'vale.',
 """And now farewell.”""",
 """And now, farewell.”""",
 """The last words of Camilla's speech, 'Iamque vale', 'and now farewell', the ordinary leave-taking of Romans at a grave as well as in life. The speech closes here, though the print sets its closing mark after a space, joined to the next word (see the next unit); l and i close the speech after 'vale.'. No elisions."""),
(828, 'fluens.',
 """At the same time with these words she was letting go the reins,\nto the ground not of her own will flowing.""",
 """With these words she let the reins slip from her hands and slid, against her will, to the ground.""",
 """The print has 'vale. Simul' with the closing double mark joined to 'Simul', a misprint for the mark set straight after 'vale.', corrected here; the mark at the head of t belongs to the speech just ended, so l and i carry none. 'Simul his dictis', 'at the same time as these words', the ablative. 'linquebat', 'was leaving', imperfect: the grip slowly loosens. 'non sponte', 'not of her own accord'. 'fluens', 'flowing', of a body slipping helplessly. No elisions."""),
(831, 'umbras.',
 """Then, cold, from her whole\ngradually she loosens herself body, and her drooping neck\nand captured by death she laid down her head, her arms leave her,\nand life with a groan takes flight, chafing, beneath the shades.""",
 """Then, growing cold, she slowly freed herself from all her body, laid down her drooping neck and her head that death had taken, and her weapons slipped from her; and life, crying out against its lot, passed with a groan into the world of shades.""",
 """'frigida… exsolvit se', 'cold, she releases herself', the spirit freeing itself from the limbs. 'lenta… colla', 'pliant, drooping neck', poetic plural. 'captum leto… caput', 'her head taken by death'. 'arma relinquunt', 'her arms leave her'; the Latin Library reads 'relinquens', 'leaving her arms', which makes Camilla let them go, not the arms desert her. 'indignata', 'resenting', unwilling to leave a young body before its time. This line returns, word for word, as the last line of the poem, of Turnus's death (XII.952). No elisions."""),
(833, 'sidera:',
 """Then indeed, immense, rising strikes the golden shout\nstars:""",
 """Then a vast shout rises and strikes the golden stars:""",
 """'Tum vero', 'then indeed', marks the turn. 'immensus… clamor', 'a boundless shout', framing the line, with 'surgens', 'rising', between. 'ferit aurea… sidera', 'strikes the golden stars', a hyperbole of epic noise; Ennius has similar shouts reaching the sky. The shout is both grief and rage. No elisions."""),
(835, 'alae.',
 """with fallen Camilla the battle grows more savage,\nthey charge in, close packed, at once the whole force of the Teucrians,\nand the Tyrrhenian leaders and Evander's Arcadian squadrons.""",
 """with Camilla fallen the fighting grows fiercer, and the whole host of the Trojans charges in, massed together, with the Etruscan chiefs and Evander's Arcadian squadrons.""",
 """'deiecta… Camilla', ablative absolute, 'Camilla having been thrown down'. 'crudescit', 'grows raw, grows savage', an inceptive verb ('-sco', 'begins to be'). 'incurrunt… omnis copia', a singular subject with a plural verb, because the host is many men (agreement by sense); 'densi', plural for the same reason. 'Teucrum', genitive plural in '-um', 'of the Teucrians', Trojans; 'eu' one syllable. 'Tyrrheni… duces', the Etruscan leaders. 'Evandri… Arcades alae', the cavalry of Evander's Arcadians, Pallas's people. Elision 'Evandriqu(e) Arcades'."""),
]

# Speech-mark check exemptions (rule 5b), by unit ln:
#  827: the print closes Camilla's speech with a mark set after a space and joined to 'Simul' ('vale. ”Simul');
#       t (unit 'Iamque vale.') lacks the mark, l and i close the speech after 'vale.'.
#  827 (second unit, also ln 827): the mark stands at the head of t ('”Simul'); l and i carry none.
# Both units start on 827, so the one entry covers both.
EXEMPT = {827}
P = A.part('aeneid-089'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
