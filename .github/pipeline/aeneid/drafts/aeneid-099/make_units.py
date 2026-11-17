# aeneid-099 (XII.843-952): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Dira. Mors Turni'
PART = "The Death of Turnus (XII.843–952)"
TITLE_EN = "The Death of Turnus — Aeneid XII.843–952"
ABOUT = ("Jupiter, at peace with Juno, turns to Juturna. "
"He sends down one of the Dirae, the twin Dread Ones who wait beside his throne, and she drops to earth like a poisoned arrow, shrinks into the shape of the owl that sings at night on tombs, and flits screeching before Turnus's face and beats at his shield; his limbs go numb and his voice sticks in his throat. "
"Juturna knows the sound of those wings. She tears her hair, asks bitterly why Jupiter gave her a life that cannot end when it keeps her from dying with her brother, and sinks into her river. "
"Aeneas taunts Turnus to stand and fight; Turnus answers that it is not Aeneas he fears but the gods and Jupiter, and heaves an ancient boundary-stone that twelve men of today could hardly lift. "
"But, as in a dream where the legs will not run, his strength fails him and the stone falls short. "
"Aeneas's spear, louder than a siege engine's stone or a thunderbolt, pierces the rim of his shield and his thigh, and Turnus falls to his knees. "
"He admits defeat, gives up Lavinia, and asks Aeneas, for the sake of his own father Anchises, to pity old Daunus and send him or his body home. "
"Aeneas hesitates and is half won over, until he sees on Turnus's shoulder the belt he stripped from the dead Pallas. "
"Burning with fury, he cries that it is Pallas who makes this sacrifice, and buries his sword in Turnus's breast; and Turnus's life, bitter at its going, flies down among the shades. "
"The poem ends there.")
ADVISORY = {
 "lede": "In her lament for her brother, Juturna asks whether this is what Jupiter gives her in return for her maidenhood (878), the act the poem named earlier in this book (140–141).",
 "more": "Nothing is described. The act is named in a single phrase, 'pro virginitate', 'in return for my maidenhood', inside a bitter question about the immortality she was given, which now keeps her from dying with Turnus. The text is presented unaltered, and the translations and notes render what the Latin says at the force it says it."
}

U = [
(844, 'armis.',
 "These things done, another thing the father with himself turns over,\nand Juturna prepares from her brother to send away, from the arms.",
 "This settled, the Father turned over another plan in his mind, and made ready to draw Juturna away from her brother's side in the fighting.",
 "A new paragraph in Greenough. 'His actis', ablative absolute, 'these things having been done': the bargain with Juno just struck. 'genitor', 'the father', Jupiter. 'secum ipse volutat', 'he himself rolls over with himself', ponders, the verb picturing thought turning round. 'Iuturnam', Turnus's sister, the nymph who has kept him alive by driving his chariot. 'dimittere ab armis', 'to send away from the arms', from the fighting at her brother's side. Elisions 'secu(m) ipse', 'dimitter(e) ab'."),
(848, 'alas.',
 "There are said to be twin plagues, by surname the Dirae,\nwhom, and Tartarean Megaera, Night the unseasonable\nin one and the same bore birth, and with equal bound them\nof serpents coils, and wind-swift added wings.",
 "There are two plagues, it is said, called the Dread Ones, whom Night at her darkest bore at a single birth together with Megaera of Tartarus, binding all three alike in coils of snakes and giving them wings swift as the wind.",
 "'Dicuntur', 'are said', Virgil keeping his distance from the tale. 'geminae pestes', 'twin plagues'. 'cognomine Dirae', 'by name the Dirae', 'the Dread Ones', a Roman name for the Furies; with 'Megaeram' they make three, the other two (Allecto and Tisiphone) unnamed here. 'Tartaream', of Tartarus, the pit of the underworld. 'Nox intempesta', 'unseasonable Night', the dead of night, a time unfit for any business; Aeschylus too makes the Furies daughters of Night (from memory). 'paribus… serpentum spiris', 'with like coils of snakes', framing 'revinxit'. 'ventosas', 'windy', swift. Elisions 'un(o) eodemque', with the 'eo' of 'eodem' run together into one syllable (synizesis), and 'ventosasqu(e) addidit'."),
(852, 'urbes.',
 "These by Jove's throne and on the threshold of the savage king\nattend, and sharpen fear for sick mortals,\nwhenever death horrific and diseases the king of gods\ncontrives, or with war terrifies deserving cities.",
 "They wait beside the throne of Jove, on the threshold of the stern king, and whet the fears of suffering mankind whenever the king of the gods sets dreadful death and disease in motion, or terrifies with war the cities that have earned it.",
 "'Hae', the two Dirae. 'ad solium… in limine', 'at the throne… on the threshold', posted like attendants. 'saevi… regis', 'the stern king', Jupiter in his angry aspect. 'adparent', Greenough's spelling of 'apparent', 'appear, attend'; 'apparitor' was the Roman word for an official's attendant. 'aegris', 'sick, wretched'. 'siquando', Greenough's one word for 'si quando', 'whenever'. 'deum', the old genitive plural, = 'deorum', 'of the gods', as with 'superum' and 'divom' (by now a familiar pattern). 'molitur', 'sets in motion' something huge. 'meritas', 'deserving' it. Elisions 'saeviqu(e) in', 'let(um) horrificum'."),
(854, 'iussit.',
 "Of these one, swift, sent down from the highest ether\nJupiter, and as an omen to meet Juturna ordered.",
 "Jupiter sent one of them, swift, down from the height of heaven, and ordered her to meet Juturna as a sign.",
 "'Harum unam', 'one of these', partitive genitive. 'celerem', 'swift', with 'unam'. 'demisit', 'sent down'. 'ab aethere summo', 'from the topmost ether', the bright upper air where the gods live. 'in omen', 'for an omen', expressing purpose: the Dira's coming is itself the sign of what Jupiter has decided. 'occurrere', 'to run to meet', with the dative 'Iuturnae'. Elisions 'Har(um) unam', 'inqu(e) omen', 'Iuturn(ae) occurrere'."),
(855, 'fertur.',
 "She flies, and in a swift to earth whirlwind is borne.",
 "Away she flew, carried down to earth on a swift whirlwind.",
 "'Illa', the Dira. 'volat', 'flies', the present of quick narrative. 'celeri… turbine', 'in a swift whirlwind', the adjective and noun framing 'ad terram'. 'fertur', 'is carried', a passive that suits a power riding on the storm rather than beating her own way down. Elision 'celeriqu(e) ad'."),
(859, 'umbras:',
 "Not otherwise than by the string through a cloud driven an arrow,\nwhich, armed with the gall of savage poison, a Parthian,\na Parthian or a Cydonian, a weapon past healing, has shot,\nhissing, and the swift, unseen, it leaps across, shadows:",
 "Just as an arrow sped from the bowstring through a cloud, an arrow tipped with deadly poison's gall that some Parthian, Parthian or Cretan, has let fly, a shaft no remedy can cure, whirs as it passes unseen through the fleeting shadows:",
 "A simile. 'Non secus ac', 'not otherwise than', 'just as'. 'nervo… impulsa', 'driven by the string'. 'armatam… quam', 'which, armed', the relative set after its first word. 'saevi… felle veneni', 'with the gall of cruel poison'. The Parthians beyond the Euphrates and the Cydonians of Crete were the famous archers of Virgil's world; 'Parthus' is repeated as if the poet corrected himself. 'telum immedicabile', 'a weapon beyond cure', in apposition. 'celeris… umbras', 'swift shadows', 'celeris' the -is accusative plural. 'incognita', 'unseen', with 'sagitta'. Elisions 'nub(em) impulsa', 'tel(um) immedicabile'."),
(860, 'petivit.',
 "such the daughter of Night bore herself and sought the lands.",
 "so the child of Night sped on her way and made for the earth.",
 "'talis', 'such', closing the simile. 'se… tulit', 'carried herself', went. 'sata Nocte', 'sprung from Night', 'sata' the participle of 'sero', 'sow', with an ablative of origin: the Dira named by her mother. 'terras… petivit', 'made for the lands'. The simile has stressed speed, sound and invisibility: a death that cannot be seen coming or cured. No elisions."),
(864, 'umbras,',
 "After the battle-lines she sees, the Ilian, and the columns of Turnus,\nof a bird, small, into the sudden gathered shape,\nwhich at times on tombs or on rooftops deserted\nby night sitting, late sings, ill-boding, through the shadows,",
 "When she saw the Trojan lines and Turnus's columns, she shrank suddenly into the shape of the little bird that sits at night on tombs or empty rooftops and sings its late, ill-omened song through the dark;",
 "'Postquam… videt', 'after she sees', 'postquam' with a present. 'Iliacas', 'of Ilium', Trojan. 'alitis… parvae', 'of a small bird', genitive with 'figuram'. 'conlecta', Greenough's spelling of 'collecta', 'drawn together, shrunk'. 'subitam', 'sudden', transferred to the shape. 'quondam', here 'at times'. 'bustis', 'tombs', places where the dead were burned. 'serum', 'late', an adverbial accusative with 'canit'. 'importuna', 'ill-boding'. The bird is the owl, the bird of bad omen at Rome. The period runs on to 866 and is split at the comma. Elisions 'Postqu(am) acies', 'atqu(e) agmina', 'quond(am) in'."),
(866, 'alis.',
 "into this changed, form, before Turnus's face the plague\nflies to and back sounding, and the shield beats with her wings.",
 "changed into this shape, the plague flitted back and forth before Turnus's face, screeching, and beat against his shield with her wings.",
 "'hanc… in faciem', 'into this shape', framing 'versa'. 'pestis', 'the plague', the Dira, subject. 'ob ora', 'before his face', 'ora' plural for one face. 'fertque refertque', 'carries herself and carries herself back', the double '-que… -que' tracing the to-and-fro. 'sonans', 'screeching'. 'everberat', 'beats at', the prefix 'e-' of thoroughness. Elisions 'vers(a) in', 'clipeumqu(e) everberat'."),
(868, 'haesit.',
 "For him the limbs a strange loosened, with dread, numbness,\nand raised with horror his hair, and his voice in his throat stuck.",
 "A strange numbness of dread unstrung his limbs; his hair stood up in horror, and the voice stuck in his throat.",
 "'Olli', the old form of 'illi', here dative, 'for him', the person affected: 'loosened his limbs'. 'novus', 'new, unknown'. 'formidine', 'with dread', ablative of cause. 'adrectae… comae', 'hair raised', Greenough's spelling of 'arrectae'. 'vox faucibus haesit', 'the voice stuck in the jaws', the words Aeneas used of himself at the sight of Creusa's ghost (2.774, from memory). The bravest man in Italy now feels what he made others feel. Elisions 'adrectaequ(e) horrore', 'com(ae) et'."),
(871, 'pugnis:',
 "But from afar when the Dira's whirring she recognised and wings,\nunhappy, her loosened hair tears Juturna,\nwith nails her face, the sister, disfiguring, and her breast with fists:",
 "But when unhappy Juturna, far off, knew the whirr of the Dira's wings, she tore her loosened hair, and as a sister will, she marred her face with her nails and beat her breast with her fists:",
 "'ut', 'when', with the perfect. 'stridorem… et alas', 'the whirring and the wings', one thing as two. 'adgnovit', Greenough's spelling of 'agnovit', 'recognised': a goddess knows what this messenger means. 'crinis… solutos', 'loosened hair', 'crinis' the -is accusative plural; mourning women let their hair down. 'soror', 'as a sister'. 'foedans', 'befouling', disfiguring, with two objects, 'ora' and 'pectora', each with its own instrument: the gestures of a funeral, made before the death. Elision 'stridor(em) adgnovit'."),
(872, 'iuvare?',
 "“What now you your, Turnus, sister can help?",
 "“What help can your sister give you now, Turnus?",
 "Juturna's lament begins, spoken to her brother, who cannot hear it. 'Quid', 'in what', an adverbial accusative with 'iuvare': 'how can she help you?' 'tua… germana', 'your sister', 'germana' a full sister, of the same parents. 'nunc', 'now', against all the help she gave before: she drove his chariot and brought him his sword (12.785). No elisions."),
(873, 'mihi?',
 "Or what now for hard me remains?",
 "Or what is left now for me, hard as my lot is?",
 "'durae… mihi', 'for me, hard', the adjective agreeing with 'mihi', feminine: Juturna hard-fated, or hard of heart to live on while he dies; the Latin holds both. 'superat', 'is left over', with the dative. 'iam', 'any longer'. Short questions follow one another fast, the rhythm of grief. No elisions."),
(874, 'monstro?',
 "By what for you the light\nart could I prolong? Such can I set myself against, a monster?",
 "By what craft can I keep you in the daylight? Can I stand against such a monster as this?",
 "'Qua… arte', 'by what skill', framing the line-break. 'tibi lucem… morer', 'delay the light for you', keep you alive; 'morer' is a deliberative subjunctive. 'Talin' = 'taline', 'tali' with the question particle '-ne', its e dropped: 'to such a…?', dative with 'opponere'. 'monstro', 'portent, monster', the Dira, a creature sent by Jupiter, which no nymph can face. Elision 'm(e) opponere'."),
(875, 'acies.',
 "Now, now I leave the battle-lines.",
 "Now, yes, now I leave the field.",
 "'Iam iam', 'now, now', the doubling of urgency, as with the hound that 'iam iamque tenet' (12.754). 'linquo', 'I leave', present: she goes as she says it. 'acies', 'the battle-lines'. Short and flat after the questions: she has understood. Elision 'linqu(o) acies'."),
(878, 'Iovis.',
 "Do not me terrify, fearing,\nobscene birds: of wings the beatings I know\nand the deadly sound, nor do they deceive me, the commands proud\nof great-souled Jove.",
 "Do not terrify me, ill-omened birds; I am frightened already. I know the beat of your wings and the deadly sound, and I do not mistake the haughty orders of great-hearted Jove.",
 "'Ne… terrete', 'do not terrify', 'ne' with the imperative, an old and poetic form of prohibition. 'timentem', 'me fearing', already afraid. 'obscenae volucres', 'ill-omened birds', plural, though there is one: she addresses the kind. In augury 'obscenus' means 'of evil omen'. 'alarum verbera', 'the beatings of the wings'. 'nec fallunt', 'nor do they escape me', I read them rightly. 'iussa superba', 'proud commands'. 'magnanimi', 'great-souled', a stock epithet of the king of gods, here turned bitter. No elisions."),
(878, 'reponit?',
 "These things, for my maidenhood, does he pay back?",
 "Is this what he pays me for my maidenhood?",
 "Juturna turns to what Jupiter took from her, named once before in this book (12.140–141, 'erepta pro virginitate', in return for her maidenhood taken from her). 'Haec', 'these things', her brother's death and her own helplessness. 'pro virginitate', 'in return for my maidenhood'. 'reponit', 'gives back, repays', as one pays back what is owed. The question is bitter: the gifts she was paid with are what now hurt her. No elisions."),
(879, 'aeternam?',
 "For what did he give life eternal?",
 "Why did he give me a life without end?",
 "'Quo', 'to what end, for what', an adverb asking purpose. 'vitam… aeternam', 'eternal life', her immortality, the other part of Jupiter's payment with her rule over pools and rivers (12.139–141). 'dedit', 'he gave'. The gift is now a curse: she cannot follow her brother into death. No elisions."),
(881, 'umbras!',
 "Why of death taken away is\nthe condition? I could end such great griefs\nnow surely, and with my wretched brother as companion go through the shades!",
 "Why has the lot of death been taken from me? Then at least I could put an end to this great grief now, and go with my poor brother through the shades!",
 "'ademptast' = 'adempta est', 'has been taken away', the e of 'est' dropped and the word joined to the one before (prodelision), as in speech. 'mortis… condicio', 'the condition of death', the terms on which mortals live. 'Possem', 'I could', an imperfect subjunctive of a thing now impossible: 'I would be able (if I were mortal)'. 'certe', 'at least'. 'comes', 'as companion'. 'per umbras', 'through the shades', among the dead. Elision 'cert(e) et'."),
(882, 'ego?',
 "Immortal I?",
 "Immortal, am I?",
 "'Immortalis ego?', 'I, immortal?', with 'sum' left out: a question of indignant disbelief, turning the word for her privilege against herself. The line runs on without pause, 'ego' eliding into 'Aut' across the question mark; elision across a break in sense is common in Virgil's speeches. Elision 'eg(o) Aut'."),
(884, 'imos?”',
 "Or anything to me sweet of my own\nwithout you, brother, will be? O what enough deep will gape,\nearth, for me, and to the Shades a goddess will send down, the lowest?”",
 "Or will anything of mine be sweet to me without you, brother? Oh, what earth will gape deep enough for me, and send a goddess down to the Shades below?”",
 "'quicquam… meorum', 'anything of my own'. 'te sine', 'without you', the preposition after its noun. 'O quae… terra', 'O what earth', an exclamation. 'satis ima', 'deep enough'. 'dehiscet… demittet', futures, 'what earth will gape?', as if asking where one could be found; the Latin Library prints subjunctives, 'dehiscat… demittat', 'could gape… could send', a wish more than a question. 'Manis… imos', 'the lowest Shades', 'Manis' the -is accusative plural of 'Manes', the spirits of the dead. 'deam', 'a goddess', the word that bars her way. No elisions."),
(886, 'alto.',
 "So much having spoken, her head with grey-green she covered, mantle,\nmuch groaning, and herself in the river the goddess hid, deep.",
 "So much she said, and covered her head with her sea-grey mantle, and with many a groan the goddess hid herself in the depths of her river.",
 "'Tantum effata', 'having spoken so much', 'effata' from 'effor'. 'glauco… amictu', 'with a grey-green cloak', the colour of water, framing 'contexit'; covering the head is a gesture of grief. 'multa gemens', 'groaning many things', an adverbial accusative. 'fluvio… alto', 'in the deep river', her own stream, for she is a river-nymph (12.139–140). 'se… condidit', 'hid herself'. Juturna does not appear again. Elision 'Tant(um) effata'."),
(888, 'fatur:',
 "Aeneas presses on against him, and his spear brandishes,\nhuge, tree-like, and from his savage heart thus speaks:",
 "Aeneas pressed on to meet him, shaking his great spear, huge as a tree, and spoke from a fierce heart:",
 "A new paragraph in Greenough. 'instat contra', 'presses on in front, against him'. 'coruscat', 'brandishes, makes flash', the spear shaken till it gleams. 'ingens arboreum', 'huge, tree-like', two adjectives held over to the next line, the spear the size of a sapling. 'saevo… pectore', 'from a savage breast', ablative of source. 'sic… fatur', 'speaks thus'. 'Aeneas', Ae- one long syllable. Elision 'arbore(um) et'."),
(889, 'retractas?',
 "“What now further delay is there? Or why now, Turnus, do you draw back?",
 "“What is the delay now? Why are you still holding back, Turnus?",
 "Aeneas's taunt begins. 'deinde', 'next, after this', here two syllables, 'dein-de', its e and i run together (synizesis): 'what further delay is there now?' 'mora est', 'is there delay'. 'retractas', 'do you draw back', a frequentative, hanging back again and again. Turnus has his sword back and still does not close. Elision 'mor(a) est'."),
(890, 'armis.',
 "Not by running, with savage it must be fought hand to hand arms.",
 "This is no race: the contest must be fought hand to hand, with cruel weapons.",
 "'Non cursu', 'not by running', against the chase of 746–790. 'certandum est', 'it must be contended', the impersonal gerundive of obligation. 'comminus', 'hand to hand', at close quarters, as against 'eminus', 'from far'. 'saevis… armis', 'with savage arms', framing the rest of the line. Elision 'certand(um) est'."),
(893, 'terra.”',
 "Turn yourself into all, you, shapes, and gather whatever\neither in courage or in craft you are strong; choose the steep, with wings,\nstars to follow, or shut in the hollow yourself to hide earth.”",
 "Change yourself into every shape you like, call up whatever you have of courage or of cunning: pray to soar on wings to the high stars, or to shut yourself away in the hollow earth.”",
 "'Verte… tete in… facies', 'turn yourself into shapes', like Proteus, the shape-changing sea-god; 'tete' is a doubled, emphatic 'te'. 'omnis', the -is accusative plural with 'facies'. 'contrahe', 'gather up'. 'sive animis sive arte', 'whether in spirit or in skill'. 'vales', 'you are strong'. 'opta', 'wish, pray'. 'ardua… astra', 'the steep stars', framing 'pennis sequi'. 'clausum', 'shut in', with 'te'. The Latin Library has 'clausumque', 'and', for 'clausumve', 'or', joining the two escapes rather than offering a choice. Elisions 'Vert(e) omnis', 'tet(e) in', 'siv(e) animis', 'siv(e) arte', 'opt(a) ardua'."),
(895, 'hostis.”',
 "He, his head shaking, “Not me your hot frighten\nwords, fierce one: the gods frighten me, and Jupiter my enemy.”",
 "Turnus shook his head: “Your hot words do not frighten me, savage: it is the gods that frighten me, and Jupiter my enemy.”",
 "'Ille', Turnus. 'caput quassans', 'shaking his head', with the verb of speaking left out. 'fervida… dicta', 'hot words', split across the line. 'ferox', 'fierce one', a vocative thrown back at Aeneas. 'di me terrent', 'the gods frighten me', 'terrent' and 'me' turned round from the first clause. 'Iuppiter hostis', 'Jupiter as enemy': Turnus has understood the Dira. It is his most clear-sighted moment. No elisions."),
(898, 'arvis.',
 "Nor more having spoken, a rock he looks around and sees, huge,\na rock ancient, huge, which on the plain by chance was lying,\na boundary for the land set, that a quarrel it might settle for the fields.",
 "Without another word he looked round and saw a huge stone, an ancient, enormous stone that happened to lie on the plain, set there as a landmark to settle disputes over fields.",
 "'Nec plura effatus', 'not having spoken more'. 'circumspicit', 'looks round and spies'. 'saxum… ingens' comes back as 'saxum antiquum ingens': the repetition heaves the stone up. 'forte', 'by chance'. 'limes… positus', 'set as a boundary', in apposition. 'litem ut discerneret', 'so that it might decide a dispute', a purpose clause with 'ut' postponed; to move a boundary-stone was sacrilege at Rome. In Iliad XXI Athena throws at Ares a stone that men of old had set as a field's boundary (from memory). Elisions 'plur(a) effatus', 'sax(um) antiquum', 'antiqu(um) ingens', 'lit(em) ut'."),
(900, 'tellus:',
 "Scarcely it would picked twice-six on their neck take up,\nsuch as now of men produces bodies the earth:",
 "Twelve picked men could hardly have taken it up on their shoulders, men with such bodies as the earth brings forth today:",
 "'Vix… subirent', 'could scarcely go under it', bear it, a potential subjunctive. 'illud', the stone; the Latin Library prints 'illum', masculine, which would take up 'limes', the boundary-mark, with the same sense. 'lecti bis sex', 'twelve picked men', 'bis sex', 'twice six'. 'cervice', 'with the neck', the shoulders. 'qualia… corpora', 'such bodies as'. Homer's heroes too lift stones that two men 'such as mortals are now' could not lift (Iliad V and XII, from memory). No elisions."),
(902, 'heros.',
 "he, in his hand snatched up, trembling, was hurling it at the enemy,\nrising higher and with running roused, the hero.",
 "the hero snatched it up in a shaking hand and hurled it at his enemy, rising to his full height and putting a run behind it.",
 "'ille', Turnus. 'manu… trepida', 'with trembling hand', framing 'raptum'; 'raptum', 'snatched up', the stone. 'torquebat', 'was hurling', an imperfect of an action that will fail. 'altior insurgens', 'rising higher', up on his toes. 'cursu concitus', 'roused by running', with a run-up. 'heros', 'the hero', held to the end of the sentence: Turnus is still given the name. No elisions."),
(905, 'sanguis.',
 "But neither himself running nor does he know going,\nor lifting his hands, or the rock immense moving;\nhis knees totter, cold has congealed with chill the blood.",
 "But he did not know himself as he ran or as he went, as he raised his hands or moved the enormous stone: his knees gave way, and his blood thickened, frozen with cold.",
 "'neque… nec… cognoscit', 'he does not recognise', with four participles: 'se currentem… euntem… tollentem… moventem', 'himself running, going, lifting, moving'. He does not feel like himself. 'manus', 'hands'; the Latin Library has 'manu', 'with his hand', taking 'tollentem' with the stone. 'genua', here two syllables, 'gen-wa', the u a consonant, which makes the first syllable long. 'labant', 'totter'. 'concrevit', 'has thickened', set solid. Elision 'saxumv(e) immane'."),
(907, 'ictum.',
 "Then the stone itself of the man, through the empty void rolled,\nneither the distance crossed whole, nor carried home the blow.",
 "Then the man's stone, whirled through the empty air, neither covered the whole distance nor drove home its blow.",
 "'lapis ipse viri', 'the man's very stone': the stone, like the man, fails. 'vacuum per inane', 'through the empty void', a doubled emptiness. 'volutus', 'rolled', tumbling. 'nec spatium evasit totum', 'did not get across the whole space'. 'neque pertulit ictum', 'nor carried the blow through', did not strike home. Elision 'spati(um) evasit'."),
(912, 'sequuntur:',
 "And as in dreams, when our eyes, languid, has pressed\nby night rest, in vain eager to stretch out our runnings\nwe seem to wish, and in the midst of efforts, sick,\nwe sink down; not the tongue has power, not in the body the familiar\nsuffices strength, nor voice nor words follow:",
 "And as in dreams, when the drowsy quiet of night has weighed down our eyes, we seem to strain in vain to run on and on, and in the middle of the effort we sink down helpless; the tongue will not work, the body's familiar strength fails, and neither voice nor words will come:",
 "A simile. 'oculos… pressit… quies', 'rest has pressed our eyes', 'languida… nocte quies', 'languid rest at night'. 'nequiquam', 'in vain'. 'avidos… cursus', 'eager runnings', 'extendere', 'to stretch out'. 'velle videmur', 'we seem to wish', the dreamer's will. 'aegri', 'weak, sick'. 'succidimus', 'we collapse'. 'notae… vires', 'familiar strength'. 'sufficiunt', 'hold out'. Virgil takes the dream from Iliad XXII, where Achilles cannot catch Hector nor Hector escape, as in a dream (from memory). Elision 'nequiqu(am) avidos'."),
(914, 'negat.',
 "so to Turnus, wherever a way by courage he sought,\nsuccess the goddess, the dread, denies.",
 "so wherever Turnus tried to force a way by courage, the dread goddess refused him success.",
 "'sic', 'so', answering 'velut'. 'Turno', dative with 'negat'. 'quacumque', 'by whatever way'. 'virtute', 'by valour'. 'successum', 'success'. 'dea dira', 'the dread goddess', the Dira, her name (845) turned into an adjective. The simile and its point together make defeat a failure of the body against the will: it will not obey. No elisions."),
(915, 'varii.',
 "Then in his breast the feelings\nare turned, various.",
 "Then his heart was in turmoil, his thoughts shifting this way and that.",
 "'pectore', 'in his breast', the seat of feeling. 'sensus… varii', 'shifting feelings', the subject, with the adjective held to the end. 'vertuntur', 'are turned, churn', a passive with a middle sense. The short sentence opens Turnus's mind; the next shows what passes through it. No elisions."),
(918, 'sororem.',
 "The Rutulians he gazes at and the city,\nand hesitates with fear, and death to be near he trembles;\nnor where he may snatch himself, nor with what force strive at the enemy,\nnor his chariot anywhere he sees, nor his charioteer sister.",
 "He looked to the Rutulians and the city, he faltered in fear and trembled at the death bearing down on him; he could see no way of escape, no strength to go at his enemy, and nowhere his chariot or the sister who drove it.",
 "'aspectat', 'keeps looking at', a frequentative. 'cunctatur… metu', 'hesitates for fear'. 'letum… instare tremescit', 'trembles that death is near', an accusative and infinitive after a verb of fearing. 'nec quo se eripiat', 'nor where to snatch himself away', an indirect deliberative question, like 'qua vi tendat', 'with what force to strive', both depending on 'videt'. 'aurigam… sororem', 'his charioteer sister', Juturna, gone. Elisions 'letumqu(e) instare', 's(e) eripiat'."),
(921, 'intorquet.',
 "At him hesitating the spear Aeneas, the fateful, brandishes,\nhaving drawn his chance with his eyes, and with body whole\nfrom afar hurls it.",
 "As Turnus hesitated, Aeneas shook his fateful spear, chose his chance with his eye, and threw from a distance with the whole weight of his body.",
 "A new paragraph in Greenough. 'Cunctanti', 'at him hesitating', a dative, Turnus. 'telum… fatale', 'the fateful spear', carrying his fate. 'sortitus fortunam oculis', 'having drawn his luck with the eyes', picking spot and moment as one draws lots. 'corpore toto', 'with the whole body'. 'eminus', 'from far'. 'intorquet', 'hurls with a twist'. 'Aeneas', Ae- one long syllable. Elisions 'tel(um) Aeneas', 'fortun(am) oculis'."),
(923, 'crepitus.',
 "Hurled from a wall- never\nengine so do stones roar, nor from the thunderbolt such\nburst crashes.",
 "Never do stones hurled from a siege engine roar so loud, nor do such crashes burst from a thunderbolt.",
 "Two comparisons in the negative: the spear is louder than both. 'Murali… tormento', 'by a wall-engine', a catapult used against city walls, the noun held across the line-break. 'concita', 'hurled', with 'saxa'. 'sic… fremunt', 'so roar'. 'nec fulmine tanti dissultant crepitus', 'nor do such great crashes leap out from the lightning', 'fulmine' an ablative of source. 'dissultant', 'leap apart', burst. No elisions."),
(925, 'orbes.',
 "It flies, like a black whirlwind,\ndeath dire the spear bearing, and the edges opens\nof the breastplate and of the shield the outermost, sevenfold, circles.",
 "On flew the spear like a black whirlwind, carrying dreadful death, and laid open the rim of the breastplate and the outer circles of the sevenfold shield.",
 "'Volat… hasta', 'the spear flies', the subject held back. 'atri turbinis instar', 'like a black whirlwind', 'instar', 'the likeness of', with a genitive. 'exitium dirum… ferens', 'bringing dire destruction'; 'dirum' recalls the Dira. 'oras… recludit', 'unseals the edges', the lower rim of the corslet. 'clipei… septemplicis', 'of the sevenfold shield', seven layers of hide, like Ajax's in the Iliad (from memory). 'orbes', 'circles', the layers. Elisions 'dir(um) hasta', 'loric(ae) et', 'clipe(i) extremos'."),
(926, 'femur.',
 "Through the middle, hissing, it passes the thigh.",
 "With a hiss it went clean through the middle of his thigh.",
 "'Per medium… femur', 'through the middle of the thigh', framing 'stridens transit'. 'stridens', 'whirring', the sound of the arrow in the simile (859) and of the Dira's wings (869). A wound in the thigh brings Turnus down without killing him, so that the last scene can be a plea. No elisions."),
(927, 'Turnus.',
 "Falls, struck,\nhuge, to the earth, with doubled knee, Turnus.",
 "Struck, huge Turnus fell to the ground, his knee bent double under him.",
 "'Incidit', 'falls down'. 'ictus', 'struck', the participle of 'icio'. 'ingens', 'huge', Turnus's great stature, used of him again and again. 'duplicato poplite', 'with knee doubled', an ablative absolute; 'poples' is properly the back of the knee. 'Turnus', the subject, kept to the very end, so the sentence falls with him. No elisions."),
(929, 'remittunt.',
 "Rise together with a groan the Rutulians, and the whole bellows back\nmountain around, and the voice far and wide the groves high send back.",
 "The Rutulians sprang up with a groan, the whole hillside round about bellowed back, and the tall woods far and wide returned the sound.",
 "'Consurgunt', 'rise up together', the watching Rutulians starting to their feet. 'gemitu', 'with a groan'. 'remugit', 'bellows back', of a sound that echoes like the lowing of cattle. 'mons… circum', 'the mountain round about'. 'vocem… remittunt', 'send back the voice', echo. 'late', 'far and wide'. 'nemora alta', 'the lofty woods'. Elisions 'circ(um) et', 'nemor(a) alta'."),
(931, 'inquit:',
 "He, humble and suppliant, his eyes and his right hand, praying,\nstretching out, “Truly I have deserved it, nor do I beg it off,” he says:",
 "Humbled, a suppliant, he raised his eyes and stretched out his right hand in entreaty. “I have earned this, truly, and I make no plea against it,” he said:",
 "The print has 'deprecor, ”inquit', a misprint for 'deprecor,” inquit', corrected here: the mark closes Turnus's first words, not 'inquit'. 'humilis supplexque', 'low and suppliant'; the Latin Library omits '-que', 'humbled as a suppliant', with little change. 'oculos dextramque… protendens', 'stretching out eyes and right hand', one verb for both. 'Equidem merui', 'I have deserved it'. 'nec deprecor', 'and I do not pray it away', ask to escape my fate. Elisions 'Ill(e) humilis', 'supplexqu(e) oculos'."),
(932, 'tua.',
 "“use your lot.",
 "“Make use of your fortune.",
 "Turnus's speech resumes after 'inquit'. 'utere', the imperative of 'utor', which takes the ablative: 'sorte tua', 'your lot', what chance has given you. Turnus grants the victor's right to kill, and in the next words asks him not to use it. No elisions."),
(936, 'meis.',
 "If of a wretched you any, parent,\ncare can touch, I beg (there was also to you such\nAnchises, a father), on Daunus have pity, his old age,\nand me, or, if my body robbed of the light you prefer,\ngive back to my own.",
 "If any thought for an unhappy parent can touch you (you too had such a father in Anchises), I beg you, have pity on Daunus in his old age, and give me back to my people, or, if you would rather, my body robbed of the light.",
 "'Miseri… parentis… cura', 'care for a wretched parent', spread over two lines. 'siqua', Greenough's one word for 'si qua', 'if any'. 'fuit et tibi talis Anchises', 'you too had such an Anchises', a parenthesis that turns Aeneas's own devotion to his father on him. 'Dauni', Turnus's father; 'miserere', the imperative, takes the genitive 'senectae'. 'me seu corpus… mavis', 'me, or, if you prefer, my body'. 'spoliatum lumine', 'stripped of the light', dead. Hector asks Achilles to give his body back to his parents in Iliad XXII, and Priam begs by the memory of Achilles' father in XXIV (from memory). No elisions."),
(937, 'coniunx:',
 "You have conquered, and the conquered stretching out his palms\nthe Ausonians have seen; yours is Lavinia as wife:",
 "You have won, and the Italians have seen me beaten and holding out my hands; Lavinia is yours to marry:",
 "'Vicisti', 'you have won', the perfect of a thing done. 'victum tendere palmas', 'the beaten man stretching out his palms', an accusative and infinitive after 'videre'; outstretched hands are the suppliant's gesture. 'Ausonii', the Ausonians, an old name for the Italians. 'videre' = 'viderunt'. 'tua est Lavinia coniunx', 'Lavinia is yours as wife': the prize the war was fought for, given up in five words. Elisions 'Vicist(i) et', 'tu(a) est'."),
(938, 'odiis.',
 "further do not stretch your hatreds.”",
 "do not carry your hatred any further.”",
 "The print has 'odiis. ”Stetit', a misprint for 'odiis.” Stetit', corrected here: Turnus's speech ends at 'odiis', so l and i close it there while t keeps the print. 'ulterius', 'further'. 'ne tende', 'do not stretch', a poetic prohibition with 'ne' and the imperative. 'odiis', 'in your hatreds', ablative. The verb picks up 'tendere palmas' just before: he has stretched out his hands; Aeneas should not stretch out his hate. Elision 'tend(e) odiis'."),
(939, 'repressit;',
 "Stood, fierce in his arms,\nAeneas, rolling his eyes, and his right hand held back;",
 "Aeneas stood there, fierce in his armour, his eyes moving restlessly, and held back his right hand;",
 "The print has 'odiis. ”Stetit', a misprint for 'odiis.” Stetit'; the mark at the head of t belongs to the speech just ended, so l and i carry none. 'Stetit', 'stood', placed first: he stops. 'acer in armis', 'keen in arms'. 'volvens oculos', 'rolling his eyes', looking this way and that, undecided. 'dextram… repressit', 'held back his right hand', the sword hand. 'Aeneas', Ae- one long syllable. No elisions."),
(944, 'gerebat.',
 "and now, now more and more him hesitating to bend the speech\nhad begun, when ill-starred on the shoulder high appeared\nthe baldric, and gleamed with its known studs the belt\nof Pallas the boy, whom, overcome, with a wound Turnus\nhad laid low, and on his shoulders the enemy's emblem was wearing.",
 "and Turnus's words were beginning to sway him more and more as he hesitated, when high on Turnus's shoulder there came into view the ill-fated baldric, and the belt of young Pallas flashed with its familiar studs; Turnus had overcome the boy and struck him down with a wound, and now wore on his shoulders the badge he had taken from his enemy.",
 "'iam iamque magis', 'now, now more', as the plea works. 'cunctantem', 'him hesitating', Aeneas, the object of 'flectere'. 'sermo', 'the speech', subject of 'coeperat'. 'cum… apparuit', 'when there appeared', 'cum' with the indicative of a sudden turn ('cum inversum'). 'infelix… balteus', 'the unlucky baldric', framing the line. 'notis… bullis', 'with the familiar studs'. 'cingula', 'belt', a poetic plural. Turnus stripped it from the dead Pallas in Book X, and the poet said then that the day would come when he wished it untouched (X.495–505, from memory). 'volnere', Greenough's spelling of 'vulnere'. 'inimicum insigne', 'the enemy's emblem'. Elisions 'c(um) apparuit', 'atqu(e) umeris', 'inimic(um) insigne'."),
(947, 'terribilis,',
 "He, after with his eyes the reminders of savage grief\nand the spoils he drank in, set on fire by furies and with anger\nterrible,",
 "Aeneas, once his eyes had drunk in the spoils, those reminders of a cruel grief, ablaze with fury and terrible in his anger,",
 "'Ille', Aeneas. 'postquam… hausit', 'after he drank in', 'haurio' of taking something in through the eyes. 'saevi monimenta doloris', 'the reminders of cruel grief', in apposition to 'exuvias', 'the spoils'. 'monimenta', Greenough's spelling of 'monumenta'. 'furiis accensus', 'set on fire by furies', by madness; the word recalls the Furies of 845. 'ira terribilis', 'terrible in anger', the adjective held over the line-break. The sentence runs through the speech to 951. Elisions 'Ill(e) oculis', 'exuviasqu(e) hausit'."),
(948, 'mihi?',
 "“You, from here, clothed in the spoils of my own,\nare you to be snatched from me?",
 "“You, dressed in the spoils of one of mine, are you to be snatched out of my hands?",
 "Aeneas's last words begin. 'Tune', 'you?', 'tu' with '-ne'. 'hinc', 'from here'. 'spoliis indute meorum', 'clothed in the spoils of my own', a vocative participle; 'induo' in the passive takes the thing put on in the ablative or accusative. 'meorum', 'of my own people', Pallas, his ward. 'eripiare' = 'eripiaris', 'are you to be snatched away', a present subjunctive in an indignant question. No elisions."),
(949, 'sumit,”',
 "Pallas you with this wound, Pallas\nsacrifices, and the penalty from your guilty blood exacts,”",
 "It is Pallas who deals you this wound, Pallas who offers you up as a victim and takes the penalty out of your guilty blood,”",
 "'Pallas… Pallas', the name doubled across the line-break: the dead boy is made the killer. 'hoc volnere', 'with this wound', the blow given as he speaks; 'volnere' is Greenough's spelling. 'immolat', 'sacrifices', properly 'sprinkles the victim with sacred meal': the death is an offering to the dead, as Aeneas took captives alive to sacrifice at Pallas's pyre (10.517–520, from memory). 'poenam… sumit', 'exacts the penalty'. 'scelerato ex sanguine', 'from blood stained by crime'. Elisions 't(e) hoc', the monosyllable 'te' elided, and 'scelerat(o) ex'."),
(951, 'fervidus.',
 "this saying, the sword into his facing, under, breast he buries,\nhot.",
 "and as he said it he buried his sword deep in the breast that faced him, in a blaze of fury.",
 "'hoc dicens', 'saying this', the participle that closes the speech; the sentence begun at 945 ends here. 'ferrum… condit', 'buries the iron', the verb of hiding used of Juturna's plunge into her river (886). 'adverso sub pectore', 'beneath the breast turned towards him', facing him. 'fervidus', 'hot, burning', alone at the head of the line, the last word the poem gives to Aeneas. Elision 'ferr(um) adverso'."),
(952, 'umbras.',
 "But for him are loosened with cold the limbs,\nand life with a groan takes flight, chafing, down under the shades.",
 "But Turnus's limbs went slack and cold, and life, bitter at its going, took flight with a groan down among the shades.",
 "'Ast', an old and solemn 'at', 'but'. 'illi', 'for him', Turnus, a dative of the person affected. 'solvuntur frigore membra', 'the limbs are loosened with cold', the words used of Aeneas's terror in the storm (I.92, from memory), now of death. The last line returns word for word from XI.831, where it closed Camilla's death, and here it ends the poem. 'fugit', the present, with short u. 'indignata', 'resenting', unwilling to go. 'sub umbras', 'down to the shades', of motion. No elisions."),
]

# Speech-mark check exemptions (rule 5b), by closing text of the unit:
#  'odiis.' (938): the print has 'odiis. ”Stetit'; l and i close Turnus's speech after 'odiis'; the note opens
#      'The print has'.
#  'repressit;' (938-939): t opens with the misplaced closing mark; l and i drop it; noted.
#  'inquit:' (930-931): the print has 'deprecor, ”inquit'; mark counts agree, only the spacing is wrong; noted.
EXEMPT = {'odiis.', 'repressit;'}
OVERLONG = set()
P = A.part('aeneid-099'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
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
