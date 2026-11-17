# aeneid-097 (XII.650-745): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Turnus redit. Ensis fractus'
PART = "Turnus Comes Back to Fight (XII.650–745)"
TITLE_EN = "Turnus Comes Back to Fight — Aeneid XII.650–745"
ABOUT = ("Turnus has only just sworn to go down to the dead with his honour whole when Saces rides up, an arrow-wound in his face, with news from the city: Aeneas is threatening to raze it, torches are flying on to the roofs, Latinus cannot decide whom to have for a son-in-law, and the queen has died by her own hand, while Messapus and Atinas hold the gates alone. "
"Turnus stands stunned, shame, grief, love and valour seething together in him, until he sees a tower he built himself go up in flames. "
"He tells his sister that fate has won, leaps from the chariot and rushes through the fighting like a boulder torn from a mountain, and at the walls he calls on both armies to stand back: the treaty is his to pay for, and his sword will settle it. "
"Aeneas leaves the siege exulting, towering like Athos, Eryx or the Apennines, and every eye on both sides turns to the two men. "
"They charge and clash like two bulls fighting for the herd, while Jupiter holds up his scales and lays their fates in them, as Zeus does for Achilles and Hector in the Iliad. "
"Turnus rises for a great blow, and his sword breaks: in his haste that morning he had taken his charioteer's blade instead of his father's, and against armour forged by Vulcan it shatters like ice. "
"He runs, and the Trojans ring him round with the marsh on one side and the walls on the other.")

U = [
(650, 'erat:',
 "Scarcely these things had he spoken:",
 "He had hardly finished speaking:",
 "A new paragraph in Greenough. 'Vix ea fatus erat', 'scarcely had he said these things', the pluperfect of the deponent 'for', 'speak', a stock formula for news that breaks in on a speech. The speaker is Turnus, who has just resolved to go down to the dead with his honour intact (646–649). No elisions."),
(652, 'Turnum:',
 "through the midst, flies, look, of the enemy,\ncarried on a foaming horse, Saces, by an arrow, in front,\nwounded in the face, and rushes, imploring by name, Turnus:",
 "see, through the thick of the enemy Saces came flying on a foaming horse, wounded full in the face by an arrow, and rushed up calling Turnus by name:",
 "'medios… per hostis', 'through the midst of the enemy', the preposition set between adjective and noun; 'hostis', Greenough's -is accusative plural. 'ecce', 'look!', putting the reader on the spot. 'vectus equo spumante', 'carried on a foaming horse', ridden hard. Saces appears only here. 'adversa… ora', an accusative of respect with 'saucius', 'wounded in the face, in front', the Greek construction; 'adversa' marks a wound taken facing the enemy, not in flight. 'nomine', 'by name', the urgent address. Elision 'ruitqu(e) implorans'."),
(653, 'tuorum.',
 "“Turnus, in you the last safety: pity your own.",
 "“Turnus, our last hope of safety is in you: have pity on your people.",
 "Saces's speech begins. 'in te suprema salus', 'in you (is) the last safety', 'est' understood. 'miserere', the imperative of the deponent 'misereor', 'pity', which takes a genitive, here 'tuorum', 'your own people'. The words open a report built to shame Turnus into returning. Elision 'Turn(e) in'."),
(655, 'daturum;',
 "Thunders Aeneas in arms, and the highest he threatens\nhe will throw down, the citadels of the Italians, and to destruction give;",
 "Aeneas is thundering in arms and threatens to throw down the highest citadels of Italy and give them over to destruction;",
 "'Fulminat', 'hurls lightning', a word that sets Aeneas beside Jupiter. 'minatur deiecturum… daturum', 'threatens (that he) will throw down… will give', future infinitives with 'esse' and the subject 'se' both left out. 'summas… arces', the adjective and noun split across the line. 'Italum' = 'Italorum', the old genitive plural. 'exscidio', 'to destruction', a dative of goal; 'exscidium' is Greenough's spelling, 'excidium' the familiar one. Elisions 'deiectur(um) arces', 'Ital(um) exscidioque'."),
(656, 'volant.',
 "and now torches to the roofs fly.",
 "already torches are flying on to the roofs.",
 "'iamque', 'and already'. 'faces… volant', 'torches fly', the burning ordered at 573 now under way. 'ad tecta', 'to the roofs', the houses of Latinus's city. Saces's sentences are short and breathless, a messenger's report. No elisions."),
(657, 'referunt;',
 "On you the faces of the Latins,\non you their eyes they turn;",
 "To you the Latins turn their faces, to you their eyes;",
 "'In te… in te', 'on you… on you', the repetition (anaphora) pressing the charge home. 'ora… oculos referunt', 'they turn back their faces and eyes', as people look to the one man who can save them. 'Latini' here is the plural, the Latin people, set against 'rex ipse Latinus' in the next clause. Elisions 'In t(e) ora', 'in t(e) oculos'."),
(658, 'flectat.',
 "mutters the king himself, Latinus,\nwhom as sons-in-law to call, or to what treaty himself to bend.",
 "King Latinus himself hesitates and mutters, unsure whom to call his son-in-law, which compact to turn to.",
 "'mussat', 'mutters, hesitates in silence', a rare and expressive verb; it comes back at 718 for heifers wondering which bull will rule. 'quos generos vocet… quae… ad foedera flectat', indirect deliberative questions with the subjunctive, 'whom he should call…, to which treaty he should turn'. 'generos', plural for singular, Aeneas or Turnus. 'sese… flectat', 'bend himself'. Elision 'ses(e) ad'."),
(660, 'fugit.',
 "Besides, the queen, of you most faithful, by her right hand\nhas fallen, her own, and the light in terror has fled.",
 "Besides, the queen, who was your most faithful friend, has fallen by her own hand; in her terror she has fled the light.",
 "'Praeterea', 'besides', the worst news held back to the end. 'regina', Amata, whose death was told at 595–603. 'tui fidissima', 'most faithful to you', 'tui' an objective genitive. 'dextra… sua', 'by her own right hand', framing 'occidit ipsa'. 'lucem… fugit', 'fled the light', died. 'exterrita', 'terrified', her panic at the assault. Elision 'lucemqu(e) exterrita'."),
(662, 'aciem.',
 "Alone before the gates Messapus and fierce Atinas\nhold up the battle-line.",
 "Only Messapus and fierce Atinas are holding the line before the gates.",
 "'Soli', 'alone', placed first for emphasis. Messapus, son of Neptune and tamer of horses, has led a contingent since VII.691; Atinas is a Rutulian chief, last seen in the rout of Book XI ('fugit acer Atinas', 11.869). 'sustentant aciem', 'prop up the battle-line', keep it from giving way. The Latin Library prints 'acies', the plural; the sense is the same. No elisions."),
(664, 'ferrea:',
 "Around these on both sides the phalanxes\nstand dense, and with drawn sword-points a crop bristles,\nof iron:",
 "On both sides of them the enemy ranks stand massed, and a harvest of iron bristles with drawn blades:",
 "'Circum hos', 'around these two'. 'utrimque', 'on both sides'. 'phalanges', a Greek word for close-ordered ranks. 'strictis… mucronibus', 'with drawn points', an ablative framing the line. 'seges… ferrea', 'an iron crop', the adjective held over to the next line for effect: a field of standing grain made of swords. 'horret', 'bristles', the word for grain standing stiff. Elision 'Circ(um) hos'."),
(664, 'versas.”',
 "you your chariot on the deserted grass wheel.”",
 "and you are wheeling your chariot on empty grass.”",
 "'tu', emphatic and set against all that has gone before: everyone else is fighting for the city, and you…. 'deserto in gramine', 'on the deserted grass', far from the battle, where Juturna has kept him. 'versas', 'you keep turning', the frequentative of 'verto', of idle circling. The speech ends here, on a reproach. Elision 'desert(o) in'."),
(666, 'stetit.',
 "Stunned was, by the varied confused image of things,\nTurnus, and with a gaze silent stood.",
 "Turnus was struck dumb, bewildered by the shifting picture of what was happening, and stood staring in silence.",
 "'Obstipuit', 'was stunned', the perfect of a sudden state, placed first with its subject held back to the next line. 'varia… imagine rerum', 'by the many-sided picture of events', the adjective and noun framing 'confusus'. 'obtutu tacito', 'with a silent gaze', 'obtutus' a fixed look. 'stetit', 'stood still'. No elisions."),
(668, 'virtus.',
 "Seethes, huge,\nin one heart, shame, and with grief mixed madness,\nand by furies driven love, and conscious valour.",
 "In that one heart a great shame seethed, and madness mingled with grief, and love driven by furies, and valour that knew its own worth.",
 "'Aestuat', 'boils, seethes', of the sea or a fire, put first; the four subjects follow, 'pudor', 'insania', 'amor', 'virtus'. 'uno in corde', 'in one heart', all at once. 'mixto… luctu', an ablative absolute or of attendant circumstance, 'grief mingled with it'. 'amor', his love for Lavinia, or love of glory: commentators differ. 'conscia virtus', 'valour conscious of itself'. The same words are used of Mezentius at 10.870–872, where Greenough brackets the last line. Elisions 'un(o) in', 'mixtoqu(e) insania'."),
(671, 'urbem.',
 "As soon as were shaken off the shadows, and light was restored to his mind,\nthe burning of his eyes orbs to the walls he twisted,\nwild, and from the wheels to the great looked back city.",
 "As soon as the darkness had cleared and the light come back to his mind, he turned his blazing eyes wildly on the walls, and from his chariot looked back at the great city.",
 "'Ut primum', 'as soon as'. 'discussae (sunt) umbrae… reddita (est)', 'the shadows were shaken off… light was restored', the auxiliaries left out. 'ardentis oculorum orbes', 'the burning orbs of his eyes', 'ardentis' the -is accusative plural; the Latin Library's 'orbis' is only another form. 'torsit', 'twisted', a violent turn. 'turbidus', 'wild, distraught'. 'eque' = 'e' + '-que'; 'rotis', 'the wheels', the chariot. 'magnam… ad urbem', the preposition late. Elisions 'discuss(ae) umbrae', 'umbr(ae) et', 'oculor(um) orbes'."),
(675, 'altos.',
 "But look, with flames among the storeys rolling,\nto the sky surged a whirl and was gripping a tower,\na tower which with joined beams he had raised himself,\nand had set wheels beneath, and had laid gangways high.",
 "And look: a whirling column of fire, rolling up through the floors, was surging to the sky and had hold of a tower, the very tower he had raised himself of close-joined timbers, setting wheels beneath it and laying high gangways across.",
 "'Ecce autem', 'but look', the eye drawn to something new. 'flammis… volutus', 'rolled with flames'. 'tabulata', 'storeys, floors' of a wooden tower. 'undabat', 'was surging like a wave'. 'vortex', 'a whirl', Greenough's spelling; the Latin Library prints the later 'vertex', the same word. 'turrim… turrim', the word repeated at the line-break to fix the eye on it. 'compactis trabibus', 'with fastened beams'. 'eduxerat… subdiderat… instraverat', three pluperfects, the work he had done. 'pontis', gangways for crossing to the walls, -is accusative. Elisions 'Ecc(e) autem', 'cael(um) undabat', 'qu(am) eduxerat', 'pontisqu(e) instraverat'."),
(676, 'morari;',
 "“Now, now the fates, sister, prevail; stop delaying;",
 "“Now, sister, now the fates have the upper hand; stop holding me back;",
 "Turnus speaks to Juturna, whose disguise as his charioteer he saw through at 632. 'Iam iam', 'now, now', the doubling of urgency. 'fata… superant', 'the fates are winning'. 'absiste morari', 'cease to delay (me)', the infinitive with 'absisto'. The speech is short, as the moment demands. No elisions."),
(677, 'sequamur.',
 "where the god and where harsh calls Fortune, let us follow.",
 "where god and cruel Fortune call, let us follow.",
 "'quo… et quo', 'where… and where'. 'deus', 'the god', any god, unnamed. 'dura… Fortuna', framing the verb 'vocat', which agrees with the nearer subject. 'sequamur', a hortatory subjunctive, 'let us follow'; the plural may include Juturna or be the plural of resolve. No elisions."),
(680, 'amplius.',
 "It is fixed to join hand with Aeneas, it is fixed whatever of bitter there is\nin death to endure; nor me unseemly, sister, will you see\nany more.",
 "My mind is made up: I will meet Aeneas hand to hand, and bear whatever bitterness there is in death; you will not see me disgraced any longer, sister.",
 "'Stat', 'it stands (fixed)', impersonal, 'it is resolved', with the infinitives 'conferre' and 'pati'; repeated for firmness. 'conferre manum', 'to join hands', to fight hand to hand. 'Aeneae', dative, three syllables. 'quidquid acerbi est', 'whatever of bitterness there is', a partitive genitive. 'indecorem', 'unseemly, dishonoured'. 'germana', 'sister', a fuller word than 'soror'. 'amplius', 'any longer', run over into the next line for weight. Elisions 'man(um) Aeneae', 'acerb(i) est', 'm(e) indecorem'."),
(680, 'furorem.”',
 "This, I beg, allow me to rage, before, this madness.”",
 "Let me, I beg you, rage out this madness first.”",
 "'Hunc… furorem', 'this madness', the cognate accusative with 'furere', the verb and its own noun set side by side ('rage this rage'). 'oro', 'I pray', parenthetic. 'sine', the imperative of 'sino', 'allow', with the infinitive. 'ante', an adverb, 'first', before the end comes. Turnus calls his own resolve madness and embraces it. The speech ends here. Elision 'furer(e) ante'."),
(683, 'rumpit.',
 "He spoke, and from the chariot gave a leap, swiftly, to the fields,\nand through the enemy, through weapons rushes, and his sorrowful sister\nleaves, and with swift running the middle of the columns bursts.",
 "With that he sprang swiftly from the chariot to the ground, and dashed through the enemy, through their weapons, leaving his grieving sister behind, and burst at full speed through the middle of the ranks.",
 "'Dixit et', 'he spoke and', a formula of transition. 'saltum dedit', 'gave a leap', leapt. 'ocius', 'quickly', a comparative used for the positive. 'arvis', 'to the fields', a dative of direction, poetic. 'per hostis, per tela', the repeated preposition for speed; 'hostis' the -is accusative plural. 'maestam… sororem… deserit', 'abandons his sorrowing sister'. 'media agmina rumpit', 'bursts the middle of the columns'. The tenses move from perfect to historic present. Elision 'medi(a) agmina'."),
(686, 'vetustas;',
 "And as from a mountain's a rock top headlong\nwhen it rushes, torn away by the wind, or a turbid rainstorm\nhas washed it out, or with years loosened it, creeping beneath, old age;",
 "And as when a rock comes crashing headlong from a mountain-top, torn loose by the wind, or because a muddy rainstorm has washed it free, or the slow work of the years has crept beneath and loosened it;",
 "A simile for Turnus's rush. 'veluti… cum', 'as when'. 'montis… de vertice', 'from the top of a mountain', the genitive placed first. 'praeceps', 'headlong'. 'avulsum vento', 'torn off by the wind'. 'seu… aut', 'or else… or', alternative causes. 'proluit', 'has washed away'. 'annis… sublapsa vetustas', 'age gliding beneath with the years', time undermining it unseen. The model is Iliad XIII, where Hector charges like a boulder loosed from a cliff by a winter torrent (cited from memory). No elisions."),
(689, 'secum:',
 "it is carried into the steep with great momentum, the mountain, relentless,\nand leaps from the ground, woods, herds and men\nrolling along with it:",
 "down the sheer slope the relentless mass is borne with tremendous force, bounding off the ground and sweeping woods, herds and men along with it:",
 "'fertur', 'is carried, plunges', a passive with a middle sense. 'in abruptum', 'into the steep', a neuter adjective used as a noun. 'magno… actu', 'with great impetus'. 'mons', 'mountain', the rock now called a mountain, hyperbole. 'improbus', 'shameless, relentless', a word for anything that knows no limits. 'exsultat solo', 'bounds from the ground', 'solo' an ablative of separation. 'silvas armenta virosque', a list with one '-que'. 'involvens', 'rolling up'. No elisions."),
(692, 'ore:',
 "through the scattered columns Turnus\nthus to the city rushes, to the walls, where most with poured\nblood the earth is wet and hiss with spear-shafts the airs,\nand signals with his hand and with a great at once begins voice:",
 "so Turnus rushed through the broken ranks to the city walls, where the ground was most drenched with spilt blood and the air was whistling with spears, and he signalled with his hand and at the same time began to shout aloud:",
 "'sic', 'so', answers 'veluti' of 684: the simile applied. 'disiecta per agmina', 'through the scattered columns', the preposition after the adjective. 'urbis… ad muros', 'to the walls of the city'. 'ubi plurima… terra madet', 'where the earth is wettest', 'plurima' with 'terra', 'the ground in most places'. 'fuso sanguine', 'with poured blood'. 'stridunt… aurae', 'the air hisses'. 'significat manu', 'signals with his hand', for silence. 'magno… ore', 'with a great voice'. Elisions 'striduntqu(e) hastilibus', 'man(u) et'."),
(693, 'Latini;',
 "“Spare now, Rutulians, and you, your weapons hold back, Latins;",
 "“Hold off now, Rutulians, and you, Latins, keep back your weapons;",
 "'Parcite', 'spare', here 'refrain, hold off', addressed to his own men. 'Rutuli… Latini', both peoples named, one at each end of the line. 'inhibete', 'check, hold back'. 'vos' marks the second address. Elisions 'Rutul(i) et', 'tel(a) inhibete'."),
(695, 'ferro.”',
 "whatever is the Fortune, mine it is: me more rightly alone\nfor you the treaty to pay for and to decide with the sword.”",
 "whatever fortune is coming, it is mine: it is more right that I alone should pay for the broken treaty on your behalf and settle it with the sword.”",
 "'quaecumque est Fortuna, mea est', 'whatever Fortune there is, it is mine': he claims the outcome, good or ill. 'verius', 'more just', with 'est' understood: 'it is more right that I…', followed by the accusative 'me… unum' and the infinitives. 'pro vobis', 'on your behalf'. 'foedus luere', 'to atone for the treaty', to pay the penalty for its breaking. 'decernere ferro', 'to decide with the sword'. The speech ends here. Elisions 'quaecumqu(e) est', 'me(a) est', 'luer(e) et'."),
(696, 'dedere.',
 "Withdrew all, in the middle, and room gave.",
 "Everyone between them drew back and left a space.",
 "'Discessere' = 'discesserunt', 'they withdrew', and 'dedere' = 'dederunt', 'they gave', the -ere perfect you have seen throughout. 'medii', 'those in the middle', the troops between Turnus and the walls. 'spatium', 'room', the ground for single combat. Elision 'Discesser(e) omnes'."),
(700, 'armis;',
 "But father Aeneas, having heard the name of Turnus,\nleaves both the walls and the highest leaves the citadels,\nand hurls aside delays all, works all breaks off,\nwith joy exulting, and terribly thunders in his arms;",
 "But father Aeneas, hearing the name of Turnus, left the walls, left the high towers, cut short every delay and broke off all the siege-works, leaping for joy and making his armour ring with a fearful thunder;",
 "A new paragraph in Greenough. 'audito nomine Turni', an ablative absolute, 'the name of Turnus having been heard'. 'deserit… deserit', repeated, as Turnus 'deserted' his sister at 683. 'praecipitat moras', 'throws delays headlong', cuts them short. 'omnis', -is accusative plural. 'opera', 'works', the siege engines and assault. 'laetitia exsultans', 'leaping for joy'. 'horrendum', an adverbial neuter, 'terribly'. 'intonat armis', 'thunders with his arms'. Elisions 'oper(a) omnia', 'laetiti(a) exsultans', 'horrendumqu(e) intonat'."),
(703, 'auras.',
 "as great as Athos, or as great as Eryx, or himself, when with quivering\nholm-oaks he roars, as great, and exults, with snowy\ntop lifting himself, father Apennine, to the airs.",
 "huge as Athos, or as Eryx, or as father Apennine himself when he roars with his quivering holm-oaks and exults in lifting his snowy crown to the sky.",
 "A comparison of size. 'quantus… quantus… quantus', 'as great as', three mountains: Athos in northern Greece, Eryx in western Sicily (where Venus had a temple and Anchises was buried, Book V), and the Apennines, Italy's spine, called 'pater' as a god. 'coruscis… ilicibus', 'with quivering holm-oaks', framing 'cum fremit', the forest roaring in the wind. 'nivali vertice', 'with snowy summit'. 'Appenninus' is Greenough's spelling of 'Apenninus'. Homer likens Hector to a snowy mountain in Iliad XIII (from memory). Elision 's(e) attollens'."),
(707, 'umeris.',
 "Now indeed both the Rutulians eagerly and the Trojans and all\nturned their eyes, the Italians, both those who the high held\nwalls and those who the lowest were battering with the ram, walls,\nand their arms laid down from their shoulders.",
 "And now Rutulians and Trojans and all the Italians vied with one another to turn their eyes towards them, both those who held the high walls and those who were pounding the foot of the walls with the ram, and they set down the arms from their shoulders.",
 "'Iam vero', 'and now indeed'. 'et… et… et', 'both… and… and'. 'certatim', 'eagerly, vying', each straining to see. 'convertere' = 'converterunt'. 'omnes… Itali', split across the line. 'quique… quique', 'both those who… and those who', defenders on the walls and attackers at their base. 'ariete', 'with the ram', three syllables, the i read as a consonant. 'deposuere' = 'deposuerunt'. 'umeris', Greenough's spelling of 'humeris', an ablative of separation. Elisions 'ver(o) et', 'certat(im) et', 'converter(e) oculos', 'quiqu(e) alta', 'quiqu(e) imos', 'deposuer(e) umeris'."),
(709, 'ferro.',
 "Is amazed Latinus himself\nthat huge, born in different parts of the world,\nhave come together and decide by the sword, men.",
 "Latinus himself was astonished that two giants, born in opposite quarters of the world, had met to settle the matter with the sword.",
 "'Stupet', 'is amazed', with an accusative and infinitive, 'that the men have met'. 'ingentis… viros', 'huge men', framing two lines, 'ingentis' the -is accusative plural. 'genitos diversis partibus orbis', 'born in different parts of the world', Asia and Italy. 'coiisse', perfect infinitive of 'coeo', 'come together'. 'cernere', the old sense, 'to decide', as in 'decernere' at 695. No elisions."),
(712, 'sonoro.',
 "And they, as with empty level lay open the fields,\nwith swift charge, having thrown from afar their spears,\nrush into Mars with shields and bronze resounding.",
 "And the two of them, as soon as the plain lay open and clear, ran swiftly forward, hurled their spears from a distance, and closed in battle with shields and ringing bronze.",
 "'illi', the two champions. 'ut', 'as soon as', with the perfect 'patuerunt'. 'vacuo… aequore', 'with an empty level', the ground cleared. 'procursu rapido', 'with a swift charge'. 'coniectis eminus hastis', an ablative absolute, 'spears thrown from afar', the Homeric order of a duel: spears first, then swords. 'invadunt Martem', 'they rush into Mars', 'Mars' standing for battle. 'aere sonoro', 'sounding bronze'. Elisions 'Atqu(e) illi', 'ill(i) ut', 'atqu(e) aere'."),
(713, 'tellus;',
 "Gives a groan the earth;",
 "The earth groaned;",
 "'Dat gemitum', 'gives a groan', a periphrasis for 'gemit'. 'tellus', 'the earth', under the weight of the charge and the blows. Homer has the earth groaning beneath advancing armies (Iliad II, from memory). The short clause, ending at the semicolon, is the moment of impact. No elisions."),
(714, 'congeminant:',
 "then thick with swords blows\nthey redouble:",
 "then they rained blow after blow with their swords:",
 "'tum', 'then', after the spears. 'crebros… ictus', 'frequent blows', framing 'ensibus', 'with swords'. 'congeminant', 'redouble', a rare word, 'twin together', strokes coming in pairs and series. The verb is held over to the next line. No elisions."),
(714, 'unum.',
 "chance and valour are mingled into one.",
 "chance and courage blended into one.",
 "'fors et virtus', 'luck and courage', the two forces that decide a fight. 'miscentur in unum', 'are mixed into one', impossible to tell apart. The Latin Library prints the singular 'miscetur', agreeing with the nearer subject; the sense is the same. No elisions."),
(717, 'incurrunt;',
 "And as on huge Sila or on the top of Taburnus\nwhen two, turned into hostile battle, bulls\nwith brows charge;",
 "And as on great Sila or high on Taburnus, when two bulls lower their foreheads and charge into hostile battle;",
 "A second simile, the duel as a bullfight. 'velut… cum', 'as when'. 'ingenti Sila', a great forest in Bruttium, the toe of Italy; 'summo… Taburno', 'on the top of Taburnus', a mountain in Samnium; '-ve', 'or'. 'conversis… frontibus', 'with brows turned', lowered against each other, framing the line. 'inimica in proelia', 'into hostile battle'. Virgil describes a fight of bulls at length in Georgics III (cited from memory). Elision 'inimic(a) in'."),
(719, 'sequantur;',
 "frightened have withdrawn the herdsmen,\nstands the herd all with fear mute, and wonder the heifers\nwho the grove will rule, whom all the herds will follow;",
 "the frightened herdsmen have drawn back, the whole herd stands dumb with fear, and the heifers murmur among themselves, wondering who will be lord of the woodland, whom all the cattle will follow;",
 "'pavidi… magistri', 'the frightened masters', the herdsmen. 'cessere' = 'cesserunt', 'have withdrawn'. 'metu mutum', 'dumb with fear'. 'mussant', 'murmur, wonder', the verb used of Latinus at 657: the heifers wait, like the king, to know who will have them. 'quis… imperitet, quem… sequantur', indirect questions with the subjunctive. 'nemori', dative with 'imperitet', 'rule over the grove'. Elision 'nemor(i) imperitet'."),
(722, 'lavant;',
 "they among themselves with much force wounds exchange,\nand horns, straining, drive in, and with blood abundant\nnecks and shoulders bathe;",
 "the two of them deal wound for wound with great force, butting hard and driving their horns home, and bathe their necks and shoulders in streams of blood;",
 "'illi', the bulls. 'inter sese… volnera miscent', 'mingle wounds among themselves', give and take wounds; 'volnera' is Greenough's spelling of 'vulnera'. 'multa vi', 'with much force'. 'obnixi', 'straining against each other', the participle of 'obnitor'. 'infigunt', 'drive in'. 'sanguine largo', 'with plentiful blood'. 'armos', 'shoulders', of animals. Elisions 'ill(i) inter', 'cornuaqu(e) obnixi', 'obnix(i) infigunt'."),
(722, 'remugit:',
 "with groaning the grove all bellows back:",
 "the whole wood bellows back with their groans:",
 "'gemitu', 'with the groaning', of the bulls. 'nemus omne', 'the whole grove'. 'remugit', 're-bellows', echoes their bellowing, a verb made for cattle. The colon turns to the application of the simile. No elisions."),
(724, 'complet.',
 "not otherwise Trojan Aeneas and the Daunian hero\nrun together with shields; a huge crash the sky fills.",
 "just so did Trojan Aeneas and the Daunian hero clash with their shields; a mighty crash filled the heavens.",
 "The print has alitur, a misprint for aliter, corrected here: 'alitur', 'is nourished', does not construe, and the Latin Library prints 'aliter'. 'non aliter', 'not otherwise', the regular close of a simile. 'Tros', 'the Trojan', a Greek nominative. 'Daunius heros', 'the Daunian hero', Turnus, son of Daunus. 'concurrunt clipeis', 'run together with shields'. 'aethera', the Greek accusative of 'aether'. No elisions."),
(727, 'letum;',
 "Jupiter himself two, balanced the tongue, scales\nholds up, and the fates places in them, differing, of the two,\nwhom the struggle should doom, and with what weight death should sink.",
 "Jupiter himself held up a pair of scales with the beam level and laid in them the differing fates of the two men, to see which of them the ordeal would condemn, and which side death would weigh down.",
 "'duas… lances', 'two pans', a pair of scales, framing the line. 'aequato examine', an ablative absolute, 'the tongue being balanced', the needle at the centre of the beam. 'fata… diversa duorum', 'the different fates of the two'. 'quem damnet… quo vergat', indirect questions of purpose, 'to see whom… which way'. 'labor', 'the struggle'. 'quo… pondere', 'with which weight'. The scene is Homer's: Zeus weighs the fates of Achilles and Hector in Iliad XXII, and Hector's sinks (from memory). The print ends the line with a semicolon but begins 728 with a capital; it is read here as the end of a sentence. Elision 'fat(a) imponit'."),
(730, 'ferit:',
 "Darts out here, thinking it safe, and with his whole body\nrises Turnus to his high-lifted sword,\nand strikes:",
 "At this, Turnus sprang forward, thinking it safe, rose with his whole body to the sword he held high above him, and struck:",
 "'Emicat', 'springs out, flashes forth'. 'hic', 'at this point'. 'impune putans', 'thinking (to do it) with impunity', that he could strike without risk. 'corpore toto', 'with his whole body'. 'alte sublatum… in ensem', 'onto the sword raised high', framing the line; 'consurgit… in ensem', he rises into the blow, putting his weight behind it. 'ferit', 'strikes', held to the next line. No elisions."),
(731, 'acies.',
 "cry out the Trojans and the alarmed Latins,\nand roused are both of them the battle-lines.",
 "Trojans and anxious Latins cried out, and both armies were on edge.",
 "'exclamant', 'shout out', at the blow. 'trepidi… Latini', 'the anxious Latins', who fear for Turnus. 'arrectae (sunt)', 'are raised up', on tiptoe with suspense, the auxiliary left out. 'amborum acies', 'the battle-lines of both'. Elisions 'arrectaequ(e) amborum', 'ambor(um) acies'."),
(733, 'subeat.',
 "But the treacherous sword\nbreaks, and in mid-stroke, burning, it deserts him,\nunless flight to his aid should come.",
 "But the treacherous blade snapped and left him, all on fire, at the very height of the blow, defenceless unless flight could come to his rescue.",
 "'perfidus ensis', 'the faithless sword', given the character of a traitor. 'frangitur', 'is broken'. 'in medio… ictu', 'in the middle of the stroke', framing the line. 'ardentem', 'him burning', Turnus in his eagerness. 'deserit… ni… subeat', a mixed condition: the indicative states as already true what would follow, 'it leaves him (helpless)', and the present subjunctive gives the escape, 'unless flight should come'. 'subsidio', a dative of purpose, 'for help'. Elision 'medioqu(e) ardentem'."),
(734, 'inermem.',
 "He flees swifter than the east wind,\nwhen the hilt, unknown, and his right hand he saw, unarmed.",
 "He ran faster than the east wind, as soon as he saw the hilt that was not his own and his right hand bare.",
 "'Fugit', 'he flees', Turnus. 'ocior euro', 'swifter than Eurus', the east wind, an ablative of comparison; 'eu' one syllable, as in 'Teucri'. 'ut', 'when, as soon as', with the perfect 'aspexit'. 'capulum ignotum', 'the strange hilt', a sword he did not know. 'dextram… inermem', 'his right hand unarmed', framing the line. Elisions 'capul(um) ignotum', 'dextramqu(e) aspexit'."),
(737, 'Metisci.',
 "The story is that headlong, when for the first battles his yoked\nhe was mounting horses, his father's blade left behind,\nwhile he hurried, the steel of his charioteer he snatched, Metiscus.",
 "The story goes that when he was mounting behind his team for the first fighting, in his headlong haste he left his father's blade behind and snatched up the sword of Metiscus his charioteer.",
 "'Fama est', 'the story is', with an accusative and infinitive, 'that (he) snatched'; the subject 'eum' is left out and 'praecipitem', 'headlong', agrees with it. 'prima in proelia', 'for the first fighting' of the day. 'iunctos… equos', 'the yoked horses'. 'patrio mucrone relicto', an ablative absolute, 'his father's blade left behind', the sword Vulcan made for Daunus (12.90–91). 'dum trepidat', 'while he hurries', 'dum' with the present. 'aurigae… Metisci', 'of the charioteer Metiscus', whom Juturna threw from the chariot at 468–470. Elisions 'Fam(a) est', 'prim(a) in', 'ferr(um) aurigae'."),
(739, 'suffecit:',
 "And that, a long time, while gave their backs, straggling, the Teucrians,\nwas enough:",
 "And that served him well enough for a long time, as long as the Trojans were scattering in flight:",
 "'Idque', 'and that', the borrowed sword. 'diu… suffecit', 'was sufficient for a long time'. 'dum terga dabant', 'while they were giving their backs', 'terga dare' the idiom for running away; 'dum' with the imperfect, 'all the while'. 'palantia', 'straggling, scattered', with 'terga'. 'Teucri', the Trojans, eu one syllable. No elisions."),
(741, 'dissiluit;',
 "after it came to the arms of the god, Vulcanian,\nthe mortal blade, like ice brittle, at the stroke\nflew apart;",
 "once it came up against the armour made by the god Vulcan, the mortal blade shattered at the blow like brittle ice;",
 "'postquam… ventumst', 'after it was come', an impersonal passive, 'ventumst' Greenough's printing of 'ventum est'. 'arma dei… Volcania', 'the god's Vulcanian arms', the armour Vulcan made for Aeneas in Book VIII. 'mortalis mucro', 'the mortal blade', alliterating against the divine armour. 'glacies ceu futilis', 'like brittle ice', 'ceu' 'as, like' postponed; 'futilis', 'brittle', the Latin Library's 'futtilis' only a spelling. 'dissiluit', 'leapt apart'. Elisions 'postqu(am) arma', 'de(i) ad'."),
(741, 'harena.',
 "tawny gleam the fragments on the sand.",
 "the pieces lay glinting on the yellow sand.",
 "'fulva… harena', 'on the tawny sand', a locative ablative framing the clause. 'resplendent', 'shine back', catch the light. 'fragmina', 'fragments', a poetic word. The line gives one still picture after the shock of the break. Elision 'fragmin(a) harena'."),
(745, 'cingunt.',
 "So, out of his mind, different in flight he seeks parts of the plain, Turnus,\nand now hither, now thither, uncertain he weaves circles;\nfor on all sides with a dense the Teucrians have shut him in, ring,\nand here a vast marsh, here steep walls hem him in.",
 "So Turnus, beside himself, made for one part of the plain after another in his flight, weaving aimless circles this way and that; for the Trojans had closed him in on every side in a tight ring, and he was hemmed in by a wide marsh on one side and high walls on the other.",
 "The print has no stop after 'orbes' (743); 'enim' begins a new clause, so l and i pause there. 'amens', 'out of his mind'. 'diversa… aequora', 'different stretches of the plain', framing the line. 'fuga', ablative, 'in flight'. 'nunc huc, inde huc', 'now this way, then that way'. 'incertos implicat orbes', 'weaves uncertain circles'. 'inclusere' = 'incluserunt'. 'densa… corona', 'with a thick ring', of men. 'hinc… hinc', 'on one side… on the other'. The chase recalls Achilles chasing Hector round Troy in Iliad XXII (from memory). Elisions 'Erg(o) amens', 'ind(e) huc', 'undiqu(e) enim', 'Teucr(i) inclusere', 'atqu(e) hinc'."),
]

# Speech-mark check exemptions (rule 5b), by closing text of the unit: none needed.
#  'complet.' (723-724): t keeps the print's 'alitur'; l and i read 'aliter' (rule 5b); the note opens 'The print has'.
#  'letum;' (727): the print's semicolon before capital 'Emicat' (728) is read as a full stop in l and i; noted.
#  'cingunt.' (742-745): no stop after 'orbes' (743) in the print; l and i pause there; noted. The unit cannot end at
#      'orbes' (no mark), so 742-745 stay one four-line unit.
EXEMPT = set()
OVERLONG = set()
P = A.part('aeneid-097'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
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
