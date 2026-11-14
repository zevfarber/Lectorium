# aeneid-074 (X.185-275): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Duces Etrusci. Nympharum nuntius'
PART = "The Ship-Nymphs and the Blazing Shield (X.185–275)"
TITLE_EN = "The Ship-Nymphs and the Blazing Shield — Aeneid X.185–275"
ABOUT = ("The catalogue of the Etruscan captains ends. Cinyras leads the Ligurians, and Cupavo wears swan's feathers on his "
"helmet in memory of his father Cycnus, who mourned Phaethon until he was changed into a swan; Ocnus brings men from "
"Mantua, the city he named after his mother, the prophetess Manto, and Virgil pays his own birthplace a tribute; "
"Aulestes rides in the Triton. Thirty ships in all sail to the help of Troy. At midnight Aeneas, too anxious to sleep, "
"is steering his own ship when a band of sea-nymphs meets him: they are his Trojan fleet, which Cybele changed into "
"nymphs when Turnus tried to burn it. Cymodocea, the most eloquent of them, tells him that Ascanius is besieged and "
"that Turnus means to block the Arcadian and Etruscan horsemen, urges him to arm at dawn and take up Vulcan's shield, "
"and drives his ship on faster than an arrow. Aeneas prays to Cybele. At daybreak he comes in sight of the camp and "
"raises the blazing shield. The Trojans on the walls cheer like cranes, the Rutulians see the sea covered with ships, "
"and fire pours from Aeneas's helmet and shield like a blood-red comet or the Dog Star rising.")

U = [
(188, 'paternae.',
 """Nor would I pass you by, of the Ligurians leader bravest in war,\nCinyras, nor you, with few companions, Cupavo,\nfrom whose crest rise swan's feathers,\nthe reproach, Love, of you, and the badge of his father's form.""",
 """Nor would I pass you by, Cinyras, bravest in war of the Ligurian chiefs, nor you, Cupavo, with your few companions, from whose crest rise the feathers of a swan, a reproach to you, Love, and the emblem of his father's shape.""",
 """A new paragraph in Greenough. 'Non ego te… transierim', 'I would not pass you over', a potential perfect subjunctive and an apostrophe, the poet turning to address the heroes. 'Cinyre', vocative; the Latin Library prints 'Cunare', and the name differs between editions. 'comitate', vocative of the participle of the deponent 'comitor', used passively, 'accompanied by few'. 'olorinae… pennae', 'swan's feathers', framing the line. 'crimen, Amor, vestrum', 'your reproach, Love', 'vestrum' plural, as if Love and his fellow love-gods were addressed: the plumes recall a love that ended in a swan. 'formae… paternae', 'of his father's shape', explained in the next lines. Elisions 'Cinyr(e) et', 'formaequ(e) insigne'."""),
(193, 'sequentem.',
 """For they say that, in grief for Phaethon beloved, Cycnus,\namid the poplar leaves and the shade of his sisters,\nwhile he sings and with the Muse consoles his sad love,\nwhitening, in soft plumage, drew on old age,\nleaving the earth and the stars with his voice pursuing.""",
 """For they tell how Cycnus, mourning his beloved Phaethon, sang among the poplar leaves in the shade of Phaethon's sisters, consoling his sad love with music, until he drew on a white old age of soft plumage, and left the earth, pursuing the stars with his song.""",
 """'ferunt', 'they say', with the accusative and infinitive 'Cycnum… duxisse'. Phaethon, son of the Sun, lost control of his father's chariot and was struck down by Jupiter's thunderbolt into the river Eridanus (the Po); his sisters, weeping for him, were turned into poplars, hence 'umbram sororum', 'the shade of his sisters'. Cycnus, a Ligurian king who loved him, mourned in song until he became a swan ('cycnus' is Greek for 'swan'); Ovid tells the story later (Metamorphoses 2.367–380). 'Musa', ablative, 'with song'. 'canentem', 'growing white' (from 'caneo'), plays on 'canit', 'sings'. 'duxisse senectam', 'drew out an old age'. 'Phaethontis', four syllables. No elisions."""),
(195, 'promovet:',
 """The son, accompanying with his fleet bands of his own age,\nthe huge Centaur with oars drives forward:""",
 """His son, sailing with a fleet of companions his own age, drives the huge Centaur forward with his oars:""",
 """'Filius', Cupavo, son of Cycnus. 'aequalis… catervas', 'bands of his own age', accusative plural in '-is', object of 'comitatus', the participle of the deponent 'comitor' used actively, 'accompanying'. 'classe', 'with a fleet', ablative. 'Centaurum', the ship, named for its figurehead, a Centaur, half man and half horse; Sergestus's ship in the boat-race of Book V bore the same name (V.122). 'remis', 'with oars', ablative of means. 'promovet', 'moves forward'. No elisions."""),
(197, 'carina.',
 """it\nlooms over the water, and a rock at the waves, huge, threatens,\ntowering, and with long keel furrows the seas deep.""",
 """the Centaur leans over the water and, towering high, threatens the waves with a huge rock, and ploughs the deep seas with its long keel.""",
 """'ille', the Centaur, figurehead and ship at once: the carved creature leans out over the waves brandishing a boulder, as Centaurs fought with rocks and tree-trunks, while the vessel it stands for cuts the sea. 'instat aquae', 'presses on the water', dative. 'saxum… immane', 'a huge rock', framing 'undis', dative with 'minatur': literally 'threatens a rock to the waves'. 'arduus', 'towering'. 'sulcat', 'furrows', the keel ploughing the sea, a farming word. Elisions 'saxumqu(e) undis', 'mari(a) alta'."""),
(201, 'avis;',
 """He too a column rouses from his native shores, Ocnus,\nof prophetic Manto and of the Tuscan river the son,\nwho walls and his mother's name gave to you, Mantua,\nMantua, rich in ancestors;""",
 """Ocnus too stirs up a column from his native shores, son of the prophetess Manto and the Tuscan river, he who gave you your walls, Mantua, and his mother's name, Mantua rich in ancestry;""",
 """A new paragraph in Greenough. 'Ille… Ocnus', 'that Ocnus', the name held back. 'ciet', 'rouses', 'calls out'. 'Mantus', Greek genitive of 'Manto', a prophetess ('fatidicae', 'fate-telling'), in Greek legend the daughter of the Theban seer Tiresias. 'Tusci… amnis', 'the Tuscan river', the Tiber, as the river-god father. 'qui muros matrisque… nomen', 'who gave you walls and his mother's name': Mantua was named after Manto. Mantua was Virgil's own city, and the apostrophe 'tibi, Mantua', with the name repeated at the head of the next line, is the poet's tribute to it. 'dives avis', 'rich in ancestors', ablative of respect. Elision 'Ill(e) etiam'."""),
(203, 'vires.',
 """but not one race to all:\na race to her threefold, peoples under each race four,\nshe herself the head to the peoples, from Tuscan blood her strength.""",
 """but not all her people are of one stock: she has three races, under each race four peoples, and she herself is head of them all, drawing her strength from Tuscan blood.""",
 """Mantua's mixed origins. 'non genus omnibus unum', 'not one stock for all', dative of possession. 'gens illi triplex', 'she has a threefold race', three peoples, with four communities under each ('populi… quaterni', distributive, 'four apiece'), and Mantua the head of all twelve. 'Tusco de sanguine vires', 'from Tuscan blood (comes her) strength': the Etruscan element rules. Which three races are meant Virgil does not say, and ancient commentators could only guess. Verbs are left out throughout, in the clipped style of a catalogue. No elisions."""),
(206, 'pinu.',
 """From here too five hundred against himself Mezentius arms,\nwhom, with father Benacus, veiled in reed grey-green,\nMincius in hostile pine was leading to the seas.""",
 """From here too Mezentius arms five hundred men against himself, whom Mincius, son of father Benacus, veiled in grey-green reeds, was leading to the sea in a hostile ship of pine.""",
 """'Hinc', from Mantua. 'in se… armat', 'arms against himself': Mezentius's cruelty has made these men his enemies, so it is he, in effect, who arms them. 'quos… Mincius… ducebat', the ship Mincius, named for the river that flows out of Lake Benacus (Garda) past Mantua; its figurehead is the river-god crowned with reeds, as rivers were pictured. 'patre Benaco', 'with Benacus for father', ablative of origin. 'velatus harundine glauca', 'veiled with grey-green reed'. 'infesta… pinu', 'in hostile pine', the ship, 'pinu' ablative. No elisions."""),
(208, 'verso.',
 """Goes heavy Aulestes, and with hundredfold timber the wave\nlashes, rising up; foam the shallows, the marble turned.""",
 """On goes mighty Aulestes, rising to the stroke and lashing the waves with a hundred oars, and the waters foam as their marble surface is churned.""",
 """'It gravis Aulestes', 'weighty Aulestes goes', the verb first, a strong opening; 'gravis', heavy, formidable. 'centena arbore', 'with hundredfold timber', a hundred oars, the singular 'arbor' for the wood of them all. 'adsurgens', 'rising up', the rowers standing to the stroke or the ship heaving forward; Greenough's spelling of 'assurgens'. 'marmore verso', ablative absolute, 'the marble turned up': the calm sea gleams like marble. 'vada', 'shallows', here simply 'waters'. Aulestes will die in Book XII (290). Elision 'centenaqu(e) arbore'."""),
(212, 'unda.',
 """Him carries a monstrous Triton, with his blue conch\nterrifying the straits, whose, as far as the flanks, shaggy, as he swims,\nfront a man displays, in a sea-beast ends his belly:\nfoaming under the half-beast breast murmurs the wave.""",
 """He is carried by a monstrous Triton, who terrifies the seas with his blue conch; as he swims, his shaggy front shows a man down to the flanks, but his belly ends in a sea-beast, and the foaming wave murmurs under his half-brute breast.""",
 """'Hunc vehit… Triton', 'a Triton carries him', the ship's name and figurehead: Triton, Neptune's merman herald, who blows a shell trumpet to rouse or calm the sea. 'caerula concha', 'with sea-blue conch', ablative of means. 'cui… nanti', 'to whom as he swims', dative of reference. 'laterum tenus', 'as far as the flanks', 'tenus' following its genitive. 'hispida frons hominem praefert', 'his shaggy front shows a man'. 'in pristim desinit alvus', 'his belly ends in a sea-monster', 'pristis' a whale or shark, accusative in '-im'; a ship called Pristis raced in Book V (116). 'semifero', 'half-wild'. 'cui' is one syllable. No elisions."""),
(214, 'secabant.',
 """So many chosen chieftains in thrice ten ships were going\nto the aid of Troy, and the fields of salt the bronzes were cutting.""",
 """So many chosen chieftains were sailing in thirty ships to the aid of Troy, cutting the plains of salt with their bronze-clad prows.""",
 """A new paragraph in Greenough, a single summing-up couplet that closes the catalogue. 'ter denis navibus', 'in thrice ten ships', a distributive numeral used for a plain number, as poets do. 'subsidio Troiae', 'for a help to Troy', dative of purpose, Troy meaning the Trojans and their camp. 'campos salis', 'the plains of salt', the sea. 'aera', nominative plural of 'aes', 'the bronzes', the bronze-sheathed prows, as a fresh subject; the Latin Library prints 'aere', 'with bronze', keeping the chiefs as subject, to much the same sense. Elision 'Troi(ae) et'."""),
(216, 'Olympum:',
 """And now the day from heaven had withdrawn, and kindly, with her chariot\nnight-wandering, Phoebe was striking mid-Olympus:""",
 """And now day had departed from the sky, and kindly Phoebe, in her night-wandering chariot, was treading the middle of heaven:""",
 """A new paragraph in Greenough. The story returns to Aeneas at sea, where line 147 left him at midnight. 'concesserat', 'had withdrawn', 'given place'. 'Phoebe', the Moon, sister of Phoebus the Sun, driving her own chariot across the sky. 'curru noctivago', 'with night-wandering chariot', a poetic compound adjective, the pair split over the line end. 'pulsabat', 'was beating', as hooves strike the ground. 'medium… Olympum', 'mid-heaven', 'Olympus' for the sky: it is midnight. No elisions."""),
(218, 'ministrat.',
 """Aeneas (for not to his limbs gives care any rest)\nhimself sitting both the helm steers and to the sails attends.""",
 """Aeneas, for anxiety allows his limbs no rest, sits at the helm himself, steering and tending the sails.""",
 """'neque enim', 'for… not', a parenthesis giving the reason: the leader keeps watch while his men sleep, as he took the helm himself when Palinurus was lost at the end of Book V (867–868). 'cura', 'care', 'anxiety', the subject of 'dat'. 'clavumque… velisque', 'both… and', the double '-que'. 'clavum regit', 'steers the tiller'. 'velis ministrat', 'attends to the sails', 'ministro' with the dative, working the ropes. Elision 'nequ(e) enim'."""),
(223, 'prorae.',
 """And to him in mid-course a band, look, of his own\ncomes to meet, of companions: nymphs, whom kindly Cybebe\ndivine power to have of the sea, and nymphs from ships to be,\nhad bidden, were swimming side by side and the waves were cutting,\nas many as before bronze-clad prows had stood at the shore.""",
 """And see, in the middle of his course a company of his own comrades comes to meet him: the nymphs whom kindly Cybebe had bidden to hold divinity in the sea and to be nymphs instead of ships were swimming abreast and cutting through the waves, as many as the bronze prows that once stood moored along the shore.""",
 """'chorus… suarum comitum', 'a band of his own companions', feminine: they are his ships. In Book IX (77–122) Turnus tried to burn the Trojan fleet, and Cybele, from whose sacred pines on Ida it was built, had the ships turned into sea-nymphs, as Jupiter had promised her. 'Cybebe', another form of 'Cybele', the Phrygian Great Mother. 'numen habere maris', 'to have divinity of the sea', and 'nymphas e navibus esse', 'to be nymphs (made) out of ships', infinitives with 'iusserat'. 'innabant', 'swam on'. Line 223 repeats IX.121 word for word. Elisions 'Atqu(e) illi', 'medi(o) in', 'nymphasqu(e) e'."""),
(228, 'adloquitur:',
 """They recognise from afar their king and circle him with dances,\nof whom she who of speaking was most skilled, Cymodocea,\nbehind following, with her right hand the stern holds, and herself with her back\nrises out, and with her left in the silent waves paddles beneath,\nthen thus, him unknowing, she addresses:""",
 """They know their king from far off and circle him in dances; and the most gifted speaker among them, Cymodocea, following behind, takes hold of the stern with her right hand, lifts her back out of the water, and paddles beneath the silent waves with her left; then she speaks to him, unaware as he is:""",
 """'lustrant choreis', 'circle (him) with dances', 'lustro' 'go round', as in a rite; 'choreis', a Greek word, 'choral dances'. 'quarum quae… Cymodocea', 'of whom (she) who (was) most skilled in speaking, Cymodocea', the name coming last. 'fandi', genitive of the gerund with 'doctissima'. Cymodocea, 'wave-receiver' in Greek, is a Nereid in Homer's list (Iliad 18.39) and in Neptune's train in Book V (826, 'Cymodoceque'). 'pone', 'behind', an adverb. 'subremigat', 'rows beneath', paddling with her hand. 'ignarum', 'unknowing': he does not yet know who they are. Elision 'ignar(um) adloquitur'."""),
(229, 'Aenea?',
 """“Are you awake, of gods the offspring,\nAeneas?""",
 """“Are you awake, Aeneas, child of the gods?""",
 """Cymodocea's speech begins. 'Vigilasne', 'are you awake?', '-ne' marking the question. 'deum gens', 'race of the gods', in apposition to 'Aenea', the Greek vocative: Aeneas is the son of Venus. 'deum' = 'deorum', the old genitive plural. Servius says the words recall a ritual formula with which the Vestal Virgins roused the king of sacrifices, 'vigilasne, rex? vigila'. No elisions."""),
(229, 'rudentis.',
 """Wake, and to the sails let loose the sheets.""",
 """Wake, and let the sheets run free to the sails.""",
 """'Vigila', imperative, 'wake', taking up 'vigilasne'. 'velis immitte rudentis', 'let go the ropes to the sails', pay out the sheets so that the sails take the full wind: make all speed. 'rudentis', accusative plural in '-is', 'ropes'. 'immitte', 'send in', 'let go'. Elision 'Vigil(a) et'."""),
(231, 'tua.',
 """We are they, of Ida the pines from the sacred summit,\nnow nymphs of the sea, your fleet.""",
 """It is we, the pines from the sacred summit of Ida, now nymphs of the sea: your fleet.""",
 """'Nos sumus', 'it is we', the plain announcement. 'Idaeae… pinus', 'Idaean pines', framing the line: the fleet was built from pines of Mount Ida above Troy, sacred to Cybele (IX.80–92). 'pelagi', 'of the sea'. 'classis tua', 'your fleet', the climax at the end of the clause, in apposition to 'nos'. No elisions."""),
(234, 'quaerimus.',
 """The treacherous, when us\nheadlong with sword the Rutulian and with flame was pressing,\nwe broke, unwilling, your bonds, and you over the sea\nwe seek.""",
 """When the treacherous Rutulian was driving us headlong with sword and fire, we broke your moorings, though it was against our will, and now we seek you across the sea.""",
 """'Perfidus… Rutulus', Turnus, 'the Rutulian', named by his people. 'ut', 'when', with the imperfect 'premebat', 'was pressing'. 'praecipitis', 'headlong', accusative plural in '-is' agreeing with 'nos'. 'ferro… flammaque', 'with sword and flame'. 'invitae', 'unwilling', feminine: loyal ships would not leave their master's moorings of their own accord. 'tua vincula', 'your bonds', the cables that tied them to the bank (IX.118). 'teque', 'and you', object of 'quaerimus', held back over the line end. No elisions."""),
(235, 'undis.',
 """This form the Mother, pitying, remade,\nand granted us to be goddesses and our life to pass beneath the waves.""",
 """The Mother took pity on us and refashioned us in this form, and granted us to be goddesses and live out our lives beneath the waves.""",
 """'Genetrix', 'the Mother', Cybele, Mother of the Gods, so called in IX.82 and IX.117. 'Hanc… faciem… refecit', 'remade (us into) this shape'; 'miserata', 'having pitied (us)'. 'dedit esse… agitare', 'granted to be… to pass', the infinitive with 'do', a poetic construction. 'aevum agitare', 'to spend a lifetime'. The nymphs are immortal now, as Jupiter promised (IX.101–103). Elision 'aevumqu(e) agitare'."""),
(237, 'Latinos.',
 """But the boy Ascanius by wall and by trenches is held\namid weapons in the midst and the Latins bristling with war.""",
 """But the boy Ascanius is shut in by rampart and trench, in the midst of weapons and of Latins bristling with war.""",
 """'At', 'but', turning to the news. 'puer Ascanius', Aeneas's young son, left in the besieged camp. 'muro fossisque tenetur', 'is held by wall and trenches', penned inside. 'tela inter media', 'amid the weapons in the midst', the preposition set after its noun. 'horrentis Marte', 'bristling with war', 'Mars' standing for war; 'horrentis' is accusative plural in '-is' with 'Latinos'. Elisions 'tel(a) inter', 'medi(a) atque'."""),
(239, 'eques:',
 """Already the appointed places hold, with the brave mingled Etruscan,\nthe Arcadian horseman:""",
 """The Arcadian cavalry, joined with the brave Etruscans, already hold their appointed positions:""",
 """'Arcas eques', 'the Arcadian horseman', a collective singular for the cavalry of Evander's people, who went by land while Aeneas sailed; 'forti… Etrusco', likewise collective, 'the brave Etruscan', dative with 'permixtus', 'mingled with'. 'tenent', plural by the sense, with the singular subject. 'loca iussa', 'the ordered places', the positions assigned them. 'Iam', 'already'. The subject is held to the end, after the verb and the participle phrase. No elisions."""),
(240, 'Turno.',
 """in the middle against them to set his squadrons,\nlest to the camp they join, fixed is the resolve for Turnus.""",
 """Turnus is fixed in his resolve to set his squadrons between them and the camp, so that they cannot join it.""",
 """'certast' = 'certa est', the verb leaning on the word before, a form Greenough prints; the Latin Library has 'certa est'. 'sententia Turno', 'the resolve (is) to Turnus', dative of possession: 'Turnus's resolve is fixed'. 'opponere', infinitive explaining 'sententia'. 'medias… turmas', 'his squadrons in the middle', between the horsemen and the camp. 'illis', dative, 'against them'. 'ne castris iungant', 'lest they join (themselves) to the camp', 'castris' dative. No elisions."""),
(243, 'auro.',
 """Up, come, and with Dawn coming your allies to be called\nfirst to arms bid, and the shield take, which gave you himself,\nunconquerable, the Fire-lord, and its rims encircled with gold.""",
 """Up, come, and as soon as Dawn arrives, be the first to have your allies called to arms, and take up the unconquerable shield which the Lord of Fire himself gave you and rimmed with gold.""",
 """'Surge age', 'rise, come', 'age' an interjection. 'Aurora… veniente', ablative absolute, 'with Dawn arriving'. 'socios… vocari… iube', 'order the allies to be called', the passive infinitive with 'iubeo'. 'primus', 'first', before Turnus can strike. 'clipeum… quem dedit ipse… Ignipotens', 'the shield which the Fire-lord himself gave', Vulcan's shield of Book VIII, engraved with the future of Rome; 'Ignipotens', 'lord of fire', as at VIII.414 and 710. 'oras ambiit auro', 'went round its rims with gold'. Elisions 'Surg(e) age', 'ag(e) et', 'iub(e) et', 'invict(um) Ignipotens', 'atqu(e) oras'."""),
(245, 'acervos.”',
 """Tomorrow's light, if my words not vain you think,\nof huge Rutulian slaughter will look upon the heaps.”""",
 """Tomorrow's light, if you do not think my words idle, will look upon great heaps of slaughtered Rutulians.”""",
 """The speech ends. 'Crastina lux', 'tomorrow's light', personified as a witness. 'putaris' = 'putaveris', future perfect, 'if you shall not have thought', a shortened form. 'inrita', Greenough's spelling of 'irrita', 'vain', 'unfulfilled'. 'ingentis… acervos', 'huge heaps', framing 'Rutulae… caedis', 'of Rutulian slaughter'; 'ingentis' is accusative plural in '-is'. 'spectabit', 'will look upon'. No elisions."""),
(247, 'puppim:',
 """She had spoken, and with her right hand, departing, pushed the high,\nnot ignorant of the way, stern:""",
 """She had spoken, and as she left him, knowing well how it was done, she gave the tall ship a push with her right hand:""",
 """'Dixerat', 'she had spoken', the regular formula closing a speech. 'discedens', 'going away'. 'altam… puppim', 'the high stern', for the ship, framing 'haud ignara modi', 'not unaware of the way', litotes: once a ship herself, she knows how a ship is best driven. 'impulit', 'pushed', 'drove on'. 'dextra', ablative, 'with her right hand', which was holding the stern (226). No elisions."""),
(248, 'sagitta.',
 """flies it through the waves\nswifter both than a javelin and than an arrow equalling the winds.""",
 """the ship flies through the waves, swifter than a javelin or an arrow that matches the wind.""",
 """'fugit illa', 'it flies', the ship. 'ocior', 'swifter', a comparative with no positive in common use, with ablatives of comparison 'iaculo' and 'sagitta'. 'et… et', 'both… and'. 'ventos aequante sagitta', 'than an arrow equalling the winds'. The speed is the nymph's doing, a sign of divine help. Elision 'iacul(o) et'."""),
(249, 'cursus.',
 """Then the others speed their courses.""",
 """Then the others quicken their course.""",
 """'Inde', 'then', 'after that'. 'aliae', feminine, the other ships, nymphs as they now are. 'celerant cursus', 'speed their courses', 'celero' used transitively, as poets use it. A short sentence: the whole fleet surges on behind the leader. Elision 'Ind(e) aliae'."""),
(250, 'tollit.',
 """Is amazed, unknowing, himself\nthe Trojan son of Anchises; his spirits yet with the omen he lifts.""",
 """The Trojan son of Anchises is himself amazed, not understanding; yet he takes heart from the omen.""",
 """'Stupet', 'is astounded', put first. 'inscius', 'unknowing', not understanding what has happened. 'Tros Anchisiades', 'the Trojan, son of Anchises', a solemn Homeric naming with a Greek patronymic. 'animos… tollit', 'raises his spirits'. 'omine', 'with the omen', ablative of cause: the nymphs and their news are a sign of heaven's favour. 'tamen', 'yet', even without understanding. No elisions."""),
(251, 'precatur:',
 """Then briefly, above looking up at the vault, he prays:""",
 """Then he looks up at the vault of heaven and prays briefly:""",
 """'breviter', 'briefly'. 'super adspectans convexa', 'looking up at the vault', 'super' an adverb, 'above'; 'convexa', neuter plural, 'the curved vault' of the sky; 'adspectans' is Greenough's spelling of 'aspectans'. The Latin Library prints 'supera aspectans convexa', 'looking at the vault above', to the same sense. 'precatur', 'prays'. No elisions."""),
(255, 'secundo.”',
 """“Kindly mother of Ida, of the gods, to whom Dindymus is dear,\nand towered cities, and to the reins the yoked lions,\nyou to me now of the fight be leader, you duly bring near\nthe omen, and the Phrygians attend, with foot, goddess, favouring.”""",
 """“Kindly Mother of the gods, Lady of Ida, who love Dindymus and towered cities and the lions yoked in pairs to your reins, be now my leader in battle, bring this omen duly to fulfilment, and stand by the Phrygians, goddess, with your favouring step.”""",
 """Aeneas's prayer to Cybele. 'parens… deum', 'mother of the gods', 'deum' = 'deorum'; 'Idaea', 'of Ida'. 'cui… cordi', 'to whom (is) for a heart', a double dative, 'who holds dear'. 'Dindyma', Mount Dindymus in Phrygia, her sanctuary (as at IX.618). 'turrigeraeque urbis', 'towered cities': she wears a crown of towers as guardian of cities; 'urbis' is nominative here, an old plural form; the Latin Library prints 'urbes'. 'biiugi… leones', 'lions yoked in pairs', who draw her chariot. 'propinques', 'bring near', subjunctive of wish, like 'adsis'. 'pede… secundo', 'with favouring foot'. Elisions 'turrigeraequ(e) urbis', 'biiugiqu(e) ad', 'Phrygibusqu(e) adsis'."""),
(256, 'effatus.',
 """So much he spoke.""",
 """That was all he said.""",
 """'Tantum effatus', 'only so much (having) spoken', with 'est' left out; 'effor', 'speak out', is a solemn word used of prayers and prophecies. The short clause closes the prayer as briefly as 'breviter' promised. Elision 'Tant(um) effatus'."""),
(257, 'fugarat:',
 """And meanwhile, rolled round again, was reddening,\nwith light now full grown, the day, and night had routed:""",
 """And meanwhile the day, come round once more, was reddening with light now full, and had put the night to flight:""",
 """'interea', 'meanwhile', while Aeneas prayed. 'revoluta', 'rolled round again', the day returning in its cycle. 'rubebat', 'was reddening' with the dawn; the Latin Library prints 'ruebat', 'was rushing on', a reading that changes the picture from colour to speed. 'matura… luce', 'with ripened light', ablative. 'fugarat' = 'fugaverat', 'had routed', a contracted pluperfect, the night chased off like an enemy. No elisions."""),
(259, 'se.',
 """first to his comrades he proclaims, the standards they should follow\nand their spirits fit to arms and for battle make themselves ready.""",
 """first he gives orders to his comrades to follow the standards, to steel their spirits for arms, and to make ready for the fight.""",
 """'principio', 'first of all'. 'edicit', 'proclaims', a commander's order. 'signa sequantur… aptent… parent', subjunctives of indirect command without 'ut', 'that they follow… fit… prepare'. 'animos aptent armis', 'fit their spirits to arms', with alliteration. 'pugnae', dative, 'for battle'. 'parent se', the monosyllable ending the line, an unusual and abrupt rhythm. Elision 'atqu(e) animos'."""),
(262, 'ardentem.',
 """And now in view the Teucrians he has, and his own camp,\nstanding on the high stern; when the shield then with his left\nhe lifted, blazing.""",
 """And now he has the Trojans and his own camp in sight as he stands on the lofty stern, and then he raised the blazing shield high in his left hand.""",
 """'Iamque… habet', 'and now he has… in view'. 'stans celsa in puppi', 'standing on the high stern', the very words used of Augustus leading the fleet at Actium on the shield of Book VIII (680): lifting that shield, Aeneas takes the pose of his descendant. 'cum deinde… extulit', 'when then he raised', the 'inverted cum' that brings in the main event after 'iamque'. 'deinde', two syllables here. 'sinistra', 'with his left hand', the shield-arm. 'ardentem', 'blazing', in the light. Elisions 'Iamqu(e) in', 'cels(a) in'."""),
(264, 'iaciunt:',
 """A shout to the stars raise\nthe Dardanians from the walls; hope added rouses their wrath;\nweapons by hand they hurl:""",
 """The Dardanians on the walls raise a shout to the stars; fresh hope rouses their fury, and they hurl their spears:""",
 """'Dardanidae', 'the Dardanians', the Trojans in the camp, who see the shield and know their leader has come back. 'ad sidera', 'to the stars', a common epic exaggeration. 'spes addita', 'hope added', new hope on top of their courage. 'suscitat iras', 'rouses their wrath'. 'tela manu iaciunt', 'they throw weapons by hand', a new burst of fighting from the ramparts. Three clauses with no connectives (asyndeton) give the sudden surge. Elisions 'Clamor(em) ad', 'Dardanid(ae) e'."""),
(266, 'secundo.',
 """such as under clouds black\nStrymonian give signals cranes and through the aether swim\nwith a noise, and flee the south winds with clamour glad.""",
 """just as Strymonian cranes give their signals under black clouds, swim through the air with a rushing sound, and flee before the south winds with joyful cries.""",
 """The simile: 'quales', 'such as', 'just as'. 'Strymoniae… grues', 'Strymonian cranes', from the Strymon, a river of Thrace famous for them. Homer compares the Trojans marching out to battle with clamouring cranes (Iliad 3.3–7); here the cranes' cries are the shouts from the walls. 'dant signa', 'give signals', calling to one another. 'tranant', 'swim across', of flight through the air. 'notos', 'the south winds', bringers of storm. 'clamore secundo', 'with glad clamour'. Elision 'atqu(e) aethera'."""),
(269, 'aequor.',
 """But to the Rutulian king and the leaders these things marvellous seemed,\nthe Ausonian, until, turned to the shores, the ships\nthey look back at, and the whole sea gliding in with fleets.""",
 """But to the Rutulian king and the Ausonian leaders all this seemed a wonder, until they looked behind them and saw ships turned toward the shore and the whole sea gliding in with fleets.""",
 """'videri', the historic infinitive, standing for a main verb in vivid narrative, 'seemed'. 'Rutulo regi', Turnus. 'ducibus… Ausoniis', 'the Ausonian leaders', noun and adjective split by the line end. 'donec… respiciunt', 'until they look back', the present in a narrative 'donec' clause. 'versas ad litora puppes', 'ships turned toward the shore', coming in to land behind them. 'adlabi', 'is gliding towards', Greenough's spelling of 'allabi'; 'totum… aequor… classibus', 'the whole sea with fleets': the sea itself seems to sail in. Elisions 'ducibusqu(e) ea', 'totumqu(e) adlabi'."""),
(271, 'ignes:',
 """Blazes the peak on his head, and from the plumes, from the top, a flame\npours, and vast the boss spews, golden, fires:""",
 """The peak of his helmet blazes on his head, flame streams from the top of his crest, and the golden boss of his shield spews out great fires:""",
 """'apex', the peak of the helmet, where the crest is set; 'capiti', dative, 'on his head'. 'cristis… a vertice', 'from the plumes, from the top'. 'funditur', 'is poured'. 'umbo', the boss of the shield. 'vomit… ignes', 'spews fires': the helmet was 'flammas vomentem', 'spewing flames', when Venus brought the arms in Book VIII (620). In Homer Athena kindles fire from Diomedes' helmet and shield as he goes into battle (Iliad 5.4–7). Elision 'cristisqu(e) a'."""),
(275, 'caelum.',
 """not otherwise than when in the clear night comets\nblood-red mournfully glow, or the Sirian blaze,\nthat one, thirst and diseases bringing to sick mortals,\nrises and saddens with ill-omened light the sky.""",
 """even as, on a clear night, comets glow blood-red and baleful, or the blaze of Sirius, that brings thirst and sickness to suffering mortals, rises and darkens the sky with its sinister light.""",
 """The simile: 'non secus ac', 'not otherwise than', 'just as'. 'siquando', 'if ever', 'whenever', Greenough's single word for 'si quando'. 'liquida… nocte', 'on a clear night'. Comets were held to portend war and disaster. 'sanguinei… rubent', 'glow blood-red'; 'lugubre', neuter used as an adverb, 'mournfully'. 'Sirius ardor', 'the Sirian blaze', the Dog Star, which rises in the heat of high summer, the season of drought and fever ('sitim morbosque'). Homer likens Achilles, as Priam sees him coming, to this star, a sign of evil (Iliad 22.26–31). 'laevo', 'left', 'ill-omened'. 'contristat', 'saddens', 'darkens'. No elisions."""),
]

P = A.part('aeneid-074'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
        if t.count(mk) != l.count(mk): print('MARK l', ln, mk)
        if mk in '“”' and t.count(mk) != i.count(mk): print('MARK i', ln, mk)
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units')
