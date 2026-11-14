# aeneid-075 (X.276-361): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Tarchonis naufragium. Pugna in litore'
PART = "The Landing and the Battle on the Shore (X.276–361)"
TITLE_EN = "The Landing and the Battle on the Shore — Aeneid X.276–361"
ABOUT = ("Turnus does not lose heart at the sight of the fleet. He means to hold the beach before the enemy can land, "
"and he rouses his men: the fight they prayed for has come, hand to hand; let them think of wives, homes and the glory "
"of their fathers, and catch the Trojans at the water's edge while their footing is still unsteady, for Fortune helps "
"those who dare. Aeneas lands his men by gangways over the sterns; some jump into the shallows, some climb down the oars. "
"The Etruscan Tarchon looks for a stretch of open water and orders his crews to drive their ships straight onto the "
"enemy's land, careless if his own ship breaks up. All the other keels run aground unharmed; his sticks on a sandbar, "
"rocks there, and breaks apart, throwing his men into the surf. Turnus brings his whole army down to the shore and the "
"trumpets sound. Aeneas strikes first and kills man after man: Theron, Lichas who was cut from his dead mother's womb, "
"the sons of Hercules' comrade Melampus, the boaster Pharus. The seven sons of Phorcus save the young Cydon by drawing "
"his attack, and Venus turns their spears aside; Aeneas calls for the spears he once threw at the Greeks and kills two of "
"the brothers, while a third only grazes Achates. On the Italian side Clausus of Cures kills Dryops and six Thracians, "
"Halaesus and Messapus bring up their troops, and the two armies push each other back and forth on the very threshold "
"of Italy, evenly matched, like winds fighting in the sky, foot against foot and man against man.")

U = [
(277, 'terra.',
 """Yet not did bold Turnus's confidence give way,\nto seize the shores first and to drive the comers from the land.""",
 """Yet bold Turnus did not lose his confidence that he could take the shore first and drive the newcomers from the land.""",
 """A new paragraph in Greenough. 'Haud… cessit', 'did not give way', with 'fiducia', 'confidence', as subject and 'audaci Turno' a dative of possession: 'bold Turnus's confidence did not yield'. The infinitives 'praecipere' and 'pellere' say what he was confident of: 'praecipere litora', 'to seize the shore before them', and 'pellere terra', 'to drive from the land', 'terra' an ablative of separation. 'venientis', accusative plural in '-is', 'those coming', the landing force. The line is almost the same as IX.126, where Turnus faced the Trojan ships before they became nymphs. Elision 'praecipir(e) et'."""),
(279, 'dextra;',
 """[unbidden their spirits he raises with words and rebukes them unbidden]\n“What with prayers you have longed for is here, to break through with the right hand;""",
 """[Unprompted he lifts their spirits with his words, and unprompted he taunts them on:] “What you prayed for is here: the chance to break their ranks with your own right hands;""",
 """Line 278 is printed in square brackets: Greenough marks it as spurious. It repeats IX.127 word for word, and editors suspect it was brought in from there; it is kept here as printed, and the English keeps it in brackets. 'ultro… ultro', 'of his own accord', framing the line. Then Turnus's speech begins. 'Quod votis optastis', 'what you have longed for in your prayers'; 'optastis' = 'optavistis', the shortened perfect. 'adest', 'is at hand'. 'perfringere dextra', 'to break through with the right hand', an infinitive explaining 'quod': what they prayed for was a chance to fight at close quarters. Elisions 'ultr(o) animos', 'atqu(e) increpat'."""),
(280, 'viris.',
 """in their hands is Mars himself, for men.""",
 """the god of war himself is in the hands of men.""",
 """'Mars' stands for battle itself, the god's name used for his sphere, a figure (metonymy) you will meet constantly in epic. 'in manibus… viris', 'in the hands for men', 'viris' a dative of reference: the fighting is now within reach of their hands, and 'viri' carries the sense 'real men', men who can use them. The verb 'est' is understood. No elisions."""),
(282, 'laudes.',
 """Now of his wife be\neach man, his own, and of his home mindful; now the great call back\ndeeds, the glories of your fathers.""",
 """Now let every man remember his wife and his home; now call to mind the great deeds and glories of your fathers.""",
 """'esto' and 'referto' are future imperatives, the solemn form of command used in laws and formal orders: 'let each man be…', 'call back'. 'coniugis… suae tectique memor', 'mindful of his own wife and home', genitives with 'memor': they fight for their homes against invaders. 'referto' may mean 'recall' the great deeds or 'repeat, renew' them; either fits. 'patrum laudes', 'the glories of their fathers', in apposition to 'magna facta'. Hector rallies the Trojans in the same way in the Iliad, telling them that a man who dies for his country leaves wife and children safe (Iliad 15.494–499). No elisions."""),
(283, 'prima.',
 """Unbidden let us run to meet them at the wave,\nwhile they are flustered, and of the landed totter the first footsteps.""",
 """Let us strike first and meet them at the water's edge, while they are in confusion and their first steps on land are unsteady.""",
 """'occurramus', hortatory subjunctive, 'let us run to meet them'; 'ultro', 'without waiting', taking the attack to the enemy. 'ad undam', 'at the water'. 'dum trepidi', 'while (they are) flustered', the verb left out. 'egressis… vestigia prima', 'the first footsteps for the landed', 'egressis' a dative of reference ('for those who have stepped ashore') doing the work of a genitive. 'labant', 'totter'. Elisions 'Ultr(o) occurramus', 'trepid(i) egressisque'."""),
(286, 'muros.',
 """Those who dare, Fortune helps,”\nthis he says, and with himself turns over whom to lead against them\nor to whom the besieged he could entrust, the walls.""",
 """Fortune lends her help to those who dare,” he says, and turns over in his mind whom he can lead against the landing, and to whom he can entrust the walls he is besieging.""",
 """Line 284 is a half-line, one of the many unfinished lines (more than fifty) left in the poem at Virgil's death; the speech stops on it. 'Audentis Fortuna iuvat', 'Fortune helps the daring', was already a proverb in Latin: Terence has 'fortis fortuna adiuvat' (Phormio 203). 'Audentis' is accusative plural in '-is', Greenough's spelling for 'audentes'. 'haec ait', 'so he speaks'. 'secum versat', 'turns over with himself', ponders. 'quos… vel quibus… possit', indirect questions: whom he can lead against the landing, or to whom he can entrust the walls 'obsessos', 'under siege', the Trojan camp his men are blockading. 'concredere', 'to hand over in trust'. No elisions."""),
(288, 'exponit.',
 """Meanwhile Aeneas his comrades from the sterns high\nby gangways puts ashore.""",
 """Meanwhile Aeneas lands his comrades from the high sterns by gangways.""",
 """A new paragraph in Greenough. 'de puppibus altis', 'from the high sterns': ancient ships came in stern first to the shore, so men landed over the stern. 'pontibus', 'by bridges', gangplanks let down onto the beach, ablative of means. 'exponit', 'sets out', the regular word for putting troops ashore. Aeneas's landing is orderly; Tarchon's, which follows, is not. 'Aeneas' scans with 'Ae-' as one long syllable. Elision 'Intere(a) Aeneas'."""),
(290, 'alii.',
 """Many to watch the backward runs\nof the slackening sea and to the shallows to trust themselves with a leap,\nby the oars others.""",
 """Many watch for the ebb of the spent wave and trust themselves to the shallows with a leap; others climb down by the oars.""",
 """'servare… credere', historic infinitives, used in quick narrative in place of a main verb: 'many were watching… and trusting'. 'recursus languentis pelagi', 'the running-back of the weakening sea', the moment a spent wave draws back and the water is shallowest; 'languentis' is genitive singular. 'brevibus', 'the shallows', the adjective used as a noun (the 'brevia', shoals), dative with 'se credere'. 'saltu', 'with a leap'. 'per remos alii', 'others by the oars', the verb left out: they slide down the oars into the water. Elision 'pelag(i) et'."""),
(293, 'precatur:',
 """Having scanned the shores, Tarchon,\nwhere shallows he does not expect, nor broken murmurs back the wave,\nbut the sea unobstructed with growing tide glides in,\nturns suddenly his prow and his comrades entreats:""",
 """Tarchon, having scanned the shore for a place where he expects no shoals and no broken wave murmurs back, but the open sea glides in unchecked on a rising tide, suddenly turns his prow to land and calls on his comrades:""",
 """Tarchon is the Etruscan leader who has joined Aeneas with his fleet (Book VIII, and earlier in this book). 'Speculatus', 'having looked out', the perfect participle of the deponent 'speculor'. 'qua', 'where'. 'vada non sperat', 'he expects no shallows'; 'sperare' here means simply 'expect'. 'fracta remurmurat unda', 'the broken wave murmurs back', surf breaking on a reef. 'mare inoffensum', 'the sea without obstruction', 'adlabitur' (Greenough's spelling of 'allabitur') 'glides in', 'crescenti aestu', 'on a swelling tide'. 'advertit… proram', 'turns his prow (to land)'. The Latin Library reads 'proras', 'the prows', which makes Tarchon turn the whole fleet; Greenough's singular has him lead with his own ship. Elisions 'mar(e) inoffensum', 'crescent(i) adlabitur'."""),
(296, 'carina.',
 """“Now, O chosen band, on the strong bend to the oars;\nlift, carry the ships; the hostile split with your beaks,\nthis land, and a furrow for herself let press the keel itself.""",
 """“Now, my chosen band, bend to your strong oars; lift the ships, drive them on; split this hostile land with your beaks, and let each keel plough a furrow for itself.""",
 """Tarchon's speech. 'incumbite remis', 'lean on the oars', dative with a compound verb; 'validis… remis' frames the verb. 'tollite, ferte', 'lift, carry', imperatives piled up without 'and' (asyndeton). 'rostris', 'with the beaks', the bronze rams at the prow. 'inimicam… hanc terram', 'this enemy land', split across the line end. 'sulcum… premat', 'let it press a furrow', a jussive subjunctive: the keel as a ploughshare and the beach as a field. 'sibi', 'for itself'. No elisions."""),
(298, 'semel.',
 """To shatter, nor in such a mooring my ship do I refuse,\nthe land once grasped.”""",
 """Nor do I shrink from wrecking my ship in such a berth, once we have laid hold of the land.”""",
 """The print has 'semel. ”Quae', a misprint for 'semel.” Quae', corrected here. The closing speech mark has slipped onto the next word; since the cut can only fall where the printed characters allow, the stray mark begins the next unit's text, and the speech is closed here in the English. 'Frangere… puppim… nec… recuso', 'nor do I refuse to break the ship', 'puppis' (stern) standing for the whole ship. 'tali statione', 'in such an anchorage', ironic: a beach rammed at speed is no harbour. 'arrepta tellure semel', ablative absolute, 'the land once seized'. No elisions."""),
(302, 'Tarchon.',
 """Which such words after\nhad spoken Tarchon, his comrades rose to the oar-blades\nand the foaming ships onto the fields drove Latin,\nuntil the beaks hold dry ground and settled the keels,\nall unharmed — but not your ship, Tarchon.""",
 """When Tarchon had spoken so, his comrades rose to their oars and drove the foaming ships onto the Latin fields, until the beaks held dry ground and every keel came to rest unharmed — but not your ship, Tarchon.""",
 """The closing speech mark printed at the head of this unit belongs to Tarchon's speech (see the note before). 'Quae talia postquam effatus (est)', 'after he had spoken such words', a connecting relative, 'quae' = 'et ea'. 'consurgere… inferre', historic infinitives, 'they rose… and drove'. 'tonsis', 'to the oar-blades', a poetic word for oars. 'spumantis', accusative plural in '-is'. 'donec… tenent… sedere', 'until the beaks hold dry land and the keels have settled'; 'sedere' = 'sederunt'. 'innocuae', 'unharmed'. 'sed non puppis tua, Tarchon', the poet turns to address his character (apostrophe), with a touch of irony: the man who ordered the landing is the one wrecked. Elision 'sicc(um) et'."""),
(307, 'relabens.',
 """For, dashed upon the shallows, on a ridge while it hangs uneven,\nswaying, held up long, and the waves it wearies,\nit breaks up, and its men in mid waves puts out,\nwhom fragments of oars and floating thwarts\nhamper, and drags back their foot at once the wave slipping back.""",
 """For, struck on the shoals, while she hung on a treacherous ridge, rocking, held up a long while and wearying the waves, she broke apart and spilled her men into the midst of the water, where broken oars and floating benches hampered them, and the backwash dragged their feet from under them.""",
 """'inflicta vadis', 'dashed upon the shallows', dative with a compound participle. 'dorso… iniquo', 'on an uneven ridge', a sandbar. 'anceps', 'swaying both ways', balanced on the bar. 'fluctus fatigat', 'wears out the waves', which beat on her in vain, a bold reversal of the usual picture. 'solvitur', 'she comes apart'. 'exponit', the word used for Aeneas's orderly landing at line 288, now grimly reused: the wreck puts its men ashore in mid-sea. 'quos', the men, object of 'impediunt'. 'transtra', the rowing benches. 'pedem', 'their footing', singular for plural (the Latin Library has 'pedes', to the same sense). 'unda relabens', 'the wave sliding back', the undertow. Elision 'Namqu(e) inflicta'."""),
(310, 'canunt.',
 """Nor Turnus does sluggish delay hold back, but he sweeps, fierce,\nthe whole line against the Teucrians and facing them on the shore sets it.\nThe signals sound.""",
 """Nor does Turnus hang back in idle delay: fiercely he sweeps his whole army against the Trojans and plants it facing them on the shore. The trumpets sound.""",
 """A new paragraph in Greenough. 'segnis… mora', 'sluggish delay', the delay itself called lazy. 'rapit… totam aciem', 'snatches up his whole battle-line', carries it off at speed. 'in Teucros', 'against the Teucrians', the Trojans, named from Teucer, an ancestor of their kings; the 'eu' of 'Teucros' is one syllable. 'contra… sistit', 'halts (it) opposite'. 'Signa canunt', 'the signals sound', the calls of the horn that open battle. Elisions 'tot(am) aciem', 'aci(em) in', 'contr(a) in'."""),
(313, 'petit:',
 """First the squadrons attacked rustic\nAeneas — an omen of the fight — and laid low the Latins,\nTheron being slain, who, of men the greatest, unprovoked\nAeneas attacks:""",
 """Aeneas was the first to fall on the country troops, an omen of the battle, and he laid the Latins low by killing Theron, the mightiest of them all, who had come at Aeneas unprovoked:""",
 """'Primus… Aeneas', the subject held over to the next line. 'turmas… agrestis', 'the rustic squadrons', the farmer-levies of Latium, accusative plural in '-is'. 'omen pugnae', 'an omen of the battle', in apposition to Aeneas: his first stroke foretells how the day will go. 'occiso Therone', ablative absolute, 'Theron slain'. 'virum', genitive plural = 'virorum' (the old form you have met often), with 'maximus', 'greatest of men'. 'ultro', 'unprovoked', taking the attack to him. 'Aenean', Greek accusative; 'petit', present after a perfect, a shift into vivid narrative. No elisions."""),
(314, 'apertum.',
 """him with the sword through the bronze stitchings,\nthrough the tunic rough with gold, in the side he drains, laid open.""",
 """he drove his sword through the bronze-linked mail and the tunic stiff with gold, and drank from the side he laid open.""",
 """'huic', dative of disadvantage, 'for him', where English says 'his': 'he pierces his side'; 'huic' is one syllable. 'aerea suta', 'bronze stitchings', armour of bronze plates sewn or linked together. 'squalentem auro', 'rough, crusted with gold'. 'haurit', literally 'drains', 'drinks': the sword draws blood as one draws water, a bold use of the word. 'latus… apertum', 'the side laid open'. Elisions 'perqu(e) aerea', 'squalent(em) auro'."""),
(317, 'parvo?',
 """Then Lichas he strikes, cut out, his mother already dead,\nand to you, Phoebus, sacred: the hazards to escape of the steel,\nto what end was it granted the little one?""",
 """Next he strikes Lichas, who was cut from his mother's body after she had died, and was dedicated to you, Phoebus: what good did it do him to escape the knife as an infant?""",
 """'Lichan', Greek accusative of 'Lichas'. 'exsectum… matre perempta', 'cut out, his mother already dead', ablative absolute: born by the operation later called Caesarean. Such children were said to be sacred to Apollo ('Phoebe', vocative: the poet turns to address the god), the god of healing, whose son Asclepius was himself cut from his dead mother's body. 'casus… ferri', 'the hazards of the steel', the surgeon's blade. 'quo', 'to what end?'. 'parvo', 'to him as a little one', dative with 'licuit'. The irony is plain: he escaped the knife at birth only to die by the sword. No elisions."""),
(319, 'Leto:',
 """Nor far off, Cisseus the hardy\nand huge Gyas, laying low the ranks with the club,\nhe cast down to Death:""",
 """Not far off, he sent hardy Cisseus and huge Gyas, who had been felling whole ranks with their clubs, down to death:""",
 """'Cissea', 'Gyan', Greek accusatives of 'Cisseus' and 'Gyas'. 'sternentis agmina clava', 'laying low the columns with the club', 'sternentis' accusative plural in '-is', agreeing with both brothers. They fight with the club of Hercules, their father's old leader, as the next lines explain. 'deiecit Leto', 'cast down to Death', a dative of direction; Greenough's capital makes 'Letum' Death personified. 'deiecit', with consonantal 'i' after the prefix. No elisions."""),
(322, 'praebuit.',
 """not at all them Hercules' arms\nnor strong helped hands, nor their father Melampus,\nof Alcides the comrade, as long as heavy the earth toils\nprovided.""",
 """nothing availed them, not the arms of Hercules, not their strong hands, not their father Melampus, the comrade of Hercules for as long as the earth supplied him with heavy labours.""",
 """'nihil', adverbial accusative, 'not at all'. 'iuvere' = 'iuverunt', with three subjects: 'Herculis arma', the hero's own kind of weapons; 'validae manus'; and 'genitor Melampus', their father. 'Alcidae', 'of Alcides', a name of Hercules from his grandfather Alcaeus. 'usque… dum', 'all the while that'. 'gravis… labores', 'heavy labours', accusative plural in '-is': the Labours laid on Hercules while he lived on earth, before he was taken up among the gods. The verb of the clause, 'praebuit', is held to the next line, and the sentence stops on it. No elisions."""),
(323, 'ore.',
 """Look — for Pharus, while words he hurls idle,\nwhirling a javelin, as he shouts he fixes it in the mouth.""",
 """See: as Pharus was hurling his idle boasts, Aeneas spun a javelin and planted it in his shouting mouth.""",
 """'Ecce', 'look!', calling the reader in as a witness. 'Pharo… clamanti', datives of disadvantage: 'he fixes it in the mouth for Pharus as he shouts', that is, in his mouth. 'voces… inertis', 'idle words', empty taunts, 'inertis' accusative plural in '-is'. 'intorquens', 'hurling with a twist'. 'sistit', 'brings to a stop', plants. The boaster is struck in the very mouth he boasts with. No elisions."""),
(327, 'iaceres,',
 """You too, golden with first down on his cheeks,\nwhile you follow Clytius, unhappy one, your new delight, Cydon,\nby the Dardan laid low right hand, free of care for the loves\nwhich of young men were always yours, pitiable one, would be lying,""",
 """You too, Cydon, luckless lover, as you followed Clytius, your new delight, whose cheeks were golden with their first down, would have lain struck down by the Dardan's hand, past caring for the loves of young men that were always yours, a sight to pity,""",
 """The poet turns to address Cydon (apostrophe). 'flaventem prima lanugine malas', 'growing golden on his cheeks with first down', 'malas' a Greek accusative of respect, 'as to his cheeks': Clytius is a youth whose beard is just coming. 'nova gaudia', 'your new joy', in apposition to 'Clytium'. 'Dardania… dextra', 'by the Dardan (Trojan) right hand', Aeneas's. 'securus amorum', 'free from care for your loves', genitive with 'securus': death would end them. 'qui… erant', 'which were always yours', 'tibi' dative of possession. 'miserande', vocative, 'pitiable one'. 'iaceres', imperfect subjunctive, 'you would be lying dead', the main clause of an unreal condition whose 'if not' comes next. Elision 'Clyti(um) infelix'."""),
(330, 'coniciunt;',
 """had not of brothers a packed band met him, of Phorcus\nthe offspring, seven in number, and seven spears\nthey hurl;""",
 """had not a close-packed band of brothers met him, the sons of Phorcus, seven in number; and they hurl seven spears;""",
 """'ni… foret obvia', 'had not (a band) been in the way', the 'if not' clause of the unreal condition: Cydon is saved because the brothers draw Aeneas's attack. 'foret' = 'esset'. 'stipata', 'crowded together'. 'Phorci progenies', 'the offspring of Phorcus', in apposition. 'septena', a distributive numeral, 'seven', one spear from each brother, the distributive standing for the plain number as poets use it. 'coniciunt', plural, with the brothers as the sense-subject. No elisions."""),
(332, 'Venus.',
 """some from helmet and shield rebound\nharmless; turned aside some, as they grazed his body,\nkindly Venus.""",
 """some glance harmlessly off his helmet and shield; others, as they grazed his body, kindly Venus turned aside.""",
 """'partim… partim', 'some… others', adverbs used as if they were pronouns. 'resultant inrita', 'leap back, useless', 'inrita' (Greenough's 'inr-' for 'irr-') agreeing with the spears. 'stringentia corpus', 'grazing his body', just touching it. 'alma Venus', 'nurturing Venus', Aeneas's mother. In the Iliad Aphrodite carries Aeneas out of danger when Diomedes wounds him (Iliad 5.311–318), and gods often turn a missile from a favourite, as Athena turns Pandarus's arrow from Menelaus (Iliad 4.127–133). No elisions."""),
(332, 'Achaten:',
 """The faithful one Aeneas addresses, Achates:""",
 """Aeneas turns to his faithful Achates:""",
 """'Fidum… Achaten', the standing epithet of Achates, Aeneas's constant companion, 'fidus Achates' throughout the poem; 'Achaten' is a Greek accusative. 'adfatur', 'addresses', Greenough's spelling of 'affatur'. The verb of speaking is followed by a colon and the speech. Elision 'Fid(um) Aeneas'."""),
(335, 'campis.',
 """“Hand up weapons to me: not one my right hand in vain\nwill have hurled at the Rutulians, of those that stood in the bodies of the Greeks\non the Ilian plains.”""",
 """“Hand me spears: not one of those that stood fixed in Greek bodies on the plains of Troy shall my right hand hurl in vain against the Rutulians.”""",
 """The print has 'campis. ”Tum', a misprint for 'campis.” Tum', corrected here. The closing speech mark has slipped onto the next word, so, as at line 298, it begins the next unit's text, and the speech is closed here in the English. 'Suggere', 'supply', 'hand up'. 'non ullum… torserit', 'will not have hurled any', the future perfect of confident assertion. 'steterunt quae', 'which stood (fixed)', the relative clause after its sense; in 'steterunt' the 'e' before '-runt' is short, an old scansion. 'Graium' = 'Graiorum', the old genitive plural. These are the spears that once stuck in Greek bodies at Troy. Elision 'qu(ae) in'."""),
(336, 'iacit:',
 """Then a great he snatches spear\nand hurls:""",
 """Then he snatched up a great spear and threw:""",
 """The closing speech mark at the head of this unit belongs to Aeneas's words to Achates (see the note before). 'corripit', 'snatches up', and 'iacit', 'throws', two presents in quick succession, the second carried over to the next line and stopped short by the colon: the throw is as sudden as the words. No elisions."""),
(337, 'rumpit.',
 """it, flying, of the shield pierces the bronze\nof Maeon, and the breastplate together with the breast bursts.""",
 """In flight it pierced the bronze of Maeon's shield and burst through his breastplate and his breast together.""",
 """'illa volans', 'it, flying', the spear. 'clipei… aera', 'the bronzes of the shield', its bronze layers ('aera' is neuter plural of 'aes'). 'Maeonis', genitive of 'Maeon', the first of the seven brothers to fall. 'thoraca', Greek accusative of 'thorax', 'breastplate'. 'simul cum pectore', 'along with the chest'. 'transverberat', 'strikes right through'; 'rumpit', 'bursts'. No elisions."""),
(339, 'dextra:',
 """To him his brother comes up, Alcanor, and his brother falling\nholds up with his right hand:""",
 """His brother Alcanor came to his side and held him up with his right hand as he fell:""",
 """'Huic… subit', 'comes up to him', dative with a compound verb; 'subit' also suggests coming up beneath him, to bear him up. 'frater… fratremque', the same word in two cases across the line, stressing the bond between them (polyptoton). 'ruentem', 'collapsing'. 'Huic' is one syllable. No elisions."""),
(341, 'pependit.',
 """his arm transfixed, the hurled\nspear flies straight on and keeps, bloody, its course,\nand the right arm from the shoulder by its sinews, dying, hung.""",
 """the spear, driven through his arm, flew straight on, keeping its bloody course, and his right arm hung dying from the shoulder by its sinews.""",
 """'traiecto… lacerto', ablative absolute, 'his upper arm pierced through'. 'missa… hasta', 'the spear sent' (by Aeneas). 'protinus', 'straight on'. 'servat… tenorem', 'keeps its course', unchecked by the arm it has passed through. 'dextera', 'the right arm', the whole limb, the fuller spelling of 'dextra' above; 'moribunda', 'dying', said of the arm itself. 'nervis', 'by the sinews', ablative. Elision 'dexteraqu(e) ex'."""),
(344, 'Achatae.',
 """Then Numitor, the javelin from his brother's body snatched,\nat Aeneas aimed; but not also to pierce in return\nwas it allowed, and of great the thigh he grazed Achates.""",
 """Then Numitor, snatching the javelin from his brother's body, aimed it at Aeneas; but he was not allowed to strike him in return, and only grazed the thigh of mighty Achates.""",
 """'iaculo… rapto', ablative absolute, 'the javelin snatched', the very spear that killed Maeon. 'Aenean', Greek accusative; 'petiit', perfect, 'aimed at'. 'sed non et figere contra est licitum', 'but it was not granted (him) to pierce in return as well': Aeneas is protected. 'licitum est', impersonal. 'magni… Achatae', 'of great Achates', the Greek genitive in '-ae'; 'perstrinxit', 'grazed'. No elisions."""),
(349, 'cruorem.',
 """Here, from Cures, trusting in his youthful body, Clausus\narrives, and with rigid spear strikes Dryops from afar,\nunder the chin heavily pressed, and at once of him speaking\nthe voice and the life takes, the throat pierced through; but he\nwith his forehead strikes the earth and thick vomits from his mouth gore.""",
 """Now Clausus of Cures, trusting in his young strength, came up and struck Dryops from a distance with his stiff spear, driven hard in under the chin, and as Dryops spoke it took his voice and his life together through the pierced throat; and he struck the ground with his forehead and vomited thick blood from his mouth.""",
 """'Curibus', 'from Cures', ablative of origin, the Sabine town; Clausus led the Sabines in the catalogue of Book VII, where Virgil makes him the founder of the Roman Claudian clan. 'primaevo corpore', 'in his youthful body', ablative with 'fidens'. 'eminus', 'at a distance'. 'pressa', 'driven home'. 'pariterque… vocem animamque rapit', 'snatches voice and life together', two objects under one verb: he dies in mid-word. 'loquentis', 'of him as he spoke'. 'at ille', 'but he', a change of subject. 'fronte ferit terram', 'strikes the earth with his forehead', falling head first. Elisions 'voc(em) animamque', 'guttur(e) at', 'terr(am) et'."""),
(352, 'casus.',
 """Three Thracians too, of Boreas's race the highest,\nand three, whom Idas their father and their native Ismara send,\nby various fates he lays low.""",
 """Three Thracians as well, of the lofty line of Boreas, and three whom their father Idas and their homeland Ismara had sent, he laid low, each by a different death.""",
 """The subject is still Clausus. 'Threicios', 'Thracian', with the 'ei' as two syllables. 'Boreae de gente suprema', 'from the lofty race of Boreas', the North Wind, whose home was Thrace. 'Tres… et tris', Greenough prints both forms of the accusative side by side (the Latin Library has 'tris' for both). 'Idas', here a Thracian father of three of Aeneas's allies. 'Ismara', neuter plural, a mountain and town in Thrace. 'per varios casus', 'by various fates', each killed a different way. Elision 'patri(a) Ismara'."""),
(354, 'equis.',
 """Runs up Halaesus\nand the Auruncan bands; comes up too Neptune's offspring,\ndistinguished Messapus for his horses.""",
 """Halaesus ran up with the Auruncan bands, and Neptune's son came on as well, Messapus, famous for his horses.""",
 """'Accurrit Halaesus', the verb first: help arrives for the Italians. Halaesus appears in the catalogue of Book VII as a follower of Agamemnon's line who settled in Italy; 'Auruncae manus', 'the Auruncan bands', a people of southern Latium. 'subit et', 'comes up too', 'et' meaning 'also'. 'Neptunia proles', 'Neptune's offspring', Messapus, introduced in Book VII as Neptune's son, a tamer of horses whom neither fire nor steel could bring down. 'insignis… equis', 'distinguished for his horses', ablative of respect. No elisions."""),
(356, 'Ausoniae.',
 """To drive out they strive,\nnow these, now those; it is fought on the threshold itself\nof Ausonia.""",
 """Now one side, now the other, strains to drive the enemy out; the struggle is on the very threshold of Ausonia.""",
 """'Expellere tendunt', 'they strive to drive out', 'tendo' with the infinitive. 'nunc hi, nunc illi', 'now these, now those', the battle swaying back and forth. 'certatur', impersonal passive, 'there is fighting', the action told without naming any fighter. 'limine in ipso Ausoniae', 'on the very threshold of Ausonia', the beach as the doorway of Italy; 'Ausonia' is a poetic name for Italy. Elision 'limin(e) in'."""),
(359, 'contra:',
 """In the great, at strife, sky winds\nbattles as when raise with spirits and strength equal;\nnot they themselves to each other, not the clouds, not the sea gives way;\ndoubtful the fight long, stand straining all things against each other:""",
 """As when, in the vast sky, warring winds raise battle against one another with equal spirit and equal strength, and neither they themselves nor the clouds nor the sea will give ground, the fight hangs long in doubt, and everything stands locked in resistance:""",
 """The simile. 'ceu', 'as', postponed into the second line. 'magno… aethere', 'in the great upper air', framing 'discordes… venti', 'warring winds'. 'proelia tollunt', 'raise battles'. 'animis et viribus aequis', 'with equal spirit and strength', ablative of manner. 'non… cedit', the verb singular, taken with each subject in turn: 'neither the winds themselves give way to each other, nor the clouds, nor the sea'. 'anceps pugna diu', 'the fight (is) long doubtful', the verb left out. 'obnixa', 'straining against', from 'obnitor'. Perhaps modelled on Homer's simile of the east and south winds contending in a mountain glen (Iliad 16.765–769). Elisions 'ips(i) inter', 'obnix(a) omnia'."""),
(361, 'vir.',
 """not otherwise the Trojan lines and the lines Latin\nclash; clings to foot foot, and close to man man.""",
 """just so the Trojan and the Latin ranks clash together; foot is locked against foot, and man pressed close on man.""",
 """'haud aliter', 'not otherwise', closes the simile. 'acies aciesque', the word doubled to set the two armies face to face. 'haeret pede pes', 'foot sticks to foot', and 'densus viro vir', 'man packed close on man': each noun set beside itself in another case, so the words press together like the fighters. Homer has the same figure for a close-locked line, shield on shield, helmet on helmet, man on man (Iliad 13.130–131, 16.215). The line ends on a single-syllable word, 'vir', a rare and jarring close. Elision 'Troian(ae) acies'."""),
]

# Misprints (rule 5b): the stray ” of 298 and 335 sits at the head of the next unit's t; l/i close the speech
# on the earlier unit. Mark counts are checked over each pair instead of unit by unit.
PAIRS = {297: 298, 333: 335}
P = A.part('aeneid-075'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
