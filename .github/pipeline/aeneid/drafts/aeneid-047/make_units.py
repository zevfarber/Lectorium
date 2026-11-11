import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..')); sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..'))
import aeneid_lib as A
# aeneid-047 draft. Drafted from the Latin and grammar only. t is cut from the edition, never typed.
TITLE = 'Lethe. Animae. Reges Albani. Augustus'
TITLE_EN = "The Souls by Lethe and the Pageant of Rome — Aeneid VI.703–800"
PART = "The Souls by Lethe and the Pageant of Rome (VI.703–800)"
ABOUT = """In a secluded valley of Elysium Aeneas sees a grove and the river Lethe, with countless nations of souls flitting about it and humming like bees in a summer meadow among the flowers and lilies. He shudders and asks what the river is and who the crowds on its banks are. Anchises tells him that these are souls for whom fate has other bodies in store, who drink at Lethe a long forgetfulness, and that he has long wanted to show him this line of their descendants, so that Aeneas may rejoice with him the more at having found Italy. Aeneas asks in wonder whether any soul could really want to return to the sluggish body, and Anchises explains. A spirit within feeds the sky, the earth, the sea, the moon and the stars, and a mind spread through the whole universe moves it; from it come men, beasts, birds and the creatures of the sea. The seeds of life in them are fiery and of heavenly origin, except so far as the body clogs and dulls them; from the body come fear and desire, grief and joy, and souls shut in its dark prison cannot see the open sky. Even after death the taints of the body do not wholly leave them, and so they are punished and purged, some hung out to the winds, some washed beneath a flood, some burnt clean by fire; each suffers his own lot, and only a few remain in Elysium, until time has removed the stain and left the soul pure fire. After a thousand years a god calls them in a throng to Lethe, so that, remembering nothing, they may wish to return to bodies. Anchises then leads Aeneas and the Sibyl to a mound from which they can watch the souls as they come, and begins to show him his descendants. First is Silvius, the son Lavinia will bear him late in life and bring up in the woods, the first of the kings of Alba Longa; then Procas, Capys, Numitor and Silvius Aeneas, young men wearing the civic crown of oak, who will found the towns of Latium, now nameless places. Then comes Romulus, son of Mars and of Ilia, with the double crest on his helmet: under his auspices Rome will make her empire as wide as the earth, enclose seven hills within one wall, and rejoice in her sons as the tower-crowned Mother of the Gods rejoices in hers. Anchises bids Aeneas look at his Romans: here is Caesar and the whole progeny of Iulus, and here is the man so often promised, Augustus Caesar, offspring of a god, who will found a golden age again in Latium, where Saturn once ruled, and carry Roman rule beyond the Garamantes and the Indians, to a land beyond the paths of the sun, while the Caspian kingdoms, the land by Lake Maeotis and the mouths of the Nile already tremble at the oracles of his coming."""
U = [
(705, 'amnem.',
 """Meanwhile sees Aeneas in a valley drawn back
a grove set apart and thickets rustling with woods,
and the Lethean — which swims past the peaceful homes — river.""",
 """Meanwhile, far back in a recess of the valley, Aeneas catches sight of a grove shut off by itself, of undergrowth whispering in the wood, and of the stream of Lethe flowing along before those quiet homes.""",
 """A new paragraph in Greenough. 'Videt' is the historic present, used throughout this narrative. 'Valle reducta' is 'a valley drawn back', a retired, secluded valley. 'Virgulta sonantia silvis' is 'thickets rustling with woods'; the Latin Library prints 'silvae', 'the rustling thickets of the wood', which many editors read: the sense is barely changed. 'Lethaeumque… amnem' frames the relative clause, river held to the end of the line. 'Praenatat' is 'swims before', 'flows past'. Lethe, Greek 'forgetting', is the river of oblivion; its model is the myth of Er at the end of Plato's Republic, where the souls about to be born again drink from the river of Unmindfulness on the plain of Lethe."""),
(706, 'volabant;',
 """Around this numberless races and peoples were flitting;""",
 """Round it, flitting this way and that, were peoples and nations past counting;""",
 """'Hunc circum' puts the preposition after its noun (anastrophe), common in verse. 'Gentes populique' is 'nations and peoples', a pairing for a whole world of souls. 'Volabant' is 'were flying', the imperfect of a scene going on, and prepares the bee simile that follows: the souls are light and winged, like insects."""),
(709, 'campus.',
 """and — as in meadows when bees in calm summer
on flowers settle various, and the white around
lilies pour themselves — hums all with murmur the plain.""",
 """and — as when, in a meadow under the clear summer sky, bees alight on blossoms of many hues and crowd thickly round the white lilies — the whole plain is loud with their humming.""",
 """Greenough sets the simile off with dashes, breaking the sentence 'ac… strepit omnis murmure campus' in two. 'Velut… ubi' is 'as when'; the Latin Library's 'veluti' is the same word. 'Insidunt' takes the dative 'floribus… variis', 'settle on many-coloured flowers'. 'Candida circum lilia' is another anastrophe, 'around the white lilies', and 'funduntur' is a middle, 'pour themselves', 'swarm'. Homer compares the Greek host pouring out to assembly to bees about spring flowers (Iliad 2.87–90), and Virgil used bees for the Carthaginians at work (1.430–436); bees were also sometimes thought of as souls in Greek belief, which suits this place. 'Strepit… murmure' is 'hums with a murmur'."""),
(712, 'ripas.',
 """He shudders at the sudden sight, and the causes asks,
unknowing Aeneas, what those rivers are out there,
or what men with so great a column have filled the banks.""",
 """Aeneas shudders at the sudden sight and, not understanding, asks the reason: what river is that further on, and who are all these men that fill its banks in so great a company?""",
 """'Horrescit' is an inceptive verb ('-sco'), 'begins to shudder'. 'Visu subito' is 'at the sudden sight', an ablative of cause. 'Inscius' is 'not knowing', and the subject 'Aeneas' is held back to 711. Two indirect questions hang on 'requirit', so their verbs are subjunctive: 'quae sint ea flumina' and 'quive viri… complerint'. 'Flumina' is a poetic plural for the one river; 'porro' is 'out there', 'further on'. '-ve' is 'or'. 'Complerint' is 'compleverint', the syncopated perfect subjunctive. 'Tanto… agmine' is 'with so great a column', the military word for a moving crowd."""),
(715, 'potant.',
 """Then father Anchises: “Souls, to whom second by fate
bodies are owed, at Lethe's river's wave
the care-free waters and long forgetfulness drink.""",
 """Then his father Anchises: “These are souls for whom fate has other bodies in store; at the stream of Lethe they are drinking water that takes away all care, and drinking a long oblivion.""",
 """A new paragraph in Greenough, and Anchises's speech opens. 'Tum pater Anchises' leaves out the verb of speaking, as so often. 'Animae' is 'souls', with 'sunt' understood ('(These are) souls'). 'Quibus altera… corpora debentur' is 'to whom other bodies are owed', the dative with 'debentur', 'fato' 'by fate'. This is the doctrine of rebirth into new bodies, taught by Pythagoras and by Plato. 'Securos latices' is 'care-free waters': the waters are called free of care because they free the drinker of it, a transferred epithet. 'Oblivia' is a poetic plural, 'forgetfulness'."""),
(718, 'reperta.”',
 """[These indeed to tell of to you and to show face to face,]
long since this offspring I desire to count over of my line,
so that the more with me you may rejoice, Italy found.”""",
 """I have long wanted [to tell you of these and show them to you face to face,] to count over this offspring of my line, so that you may share my joy the more at Italy found at last.”""",
 """Greenough brackets line 716 as spurious, so it stands inside [ ]: read with it, 'has' (these souls) is the object of 'memorare' and 'ostendere', and the three infinitives all hang on 'cupio', which crowds the sentence; without it, 717 reads plainly on its own. 'Coram' is 'face to face', 'in person'. 'Iampridem… cupio' is the present with 'iampridem', 'I have long been wanting', of something begun in the past and still going on. 'Prolem… meorum' is 'the offspring of my own', the line of descendants. 'Quo magis… laetere' is a purpose clause with a comparative, so 'quo' replaces 'ut'; 'laetere' is 'laeteris', the second-person '-re' ending. 'Italia… reperta' is 'at Italy found', the ablative with 'laetor', the noun and participle together standing for 'the finding of Italy'. The closing mark ends Anchises's answer."""),
(721, 'corpora?',
 """“O father, is it then that some up to the sky from here go must be thought,
aloft, souls, and again to slow return
bodies?""",
 """“Father, are we truly to think that some souls rise from here to the sky, lifted on high, and go back once more into the slow weight of bodies?""",
 """Aeneas's question opens without a verb of speaking. 'Anne' is 'an', introducing a question that expects surprise or disbelief. 'Putandum est' is the impersonal gerundive, 'it must be thought', followed by the accusative and infinitive 'aliquas… ire… animas'. 'Sublimis' is 'sublimes', the '-is' accusative plural, 'aloft'. 'Ad caelum' here means the sky of the living world, not heaven. 'Tarda' is 'slow', 'heavy': the body weighs the soul down, the theme of Anchises's reply."""),
(721, 'cupido?”',
 """What so dire desire of the light have the wretched?”""",
 """Why do the poor souls crave the light with so terrible a longing?”""",
 """'Lucis' is an objective genitive, 'desire for the light', life in the upper world. 'Miseris' is a dative of possession, 'have the wretched', with 'est' understood. 'Cupido' is feminine here, so 'dira'; the same phrase, 'tam dira cupido', is used in Georgics 1.37. The closing mark ends Aeneas's question."""),
(723, 'pandit.',
 """“I will tell you indeed, nor you in suspense, son, will I hold,”
takes up Anchises, and in order each thing unfolds.""",
 """“I will explain, my son, and not leave you hanging in doubt,” Anchises answers, and lays out each matter in its turn.""",
 """The speech is one line long, so it opens and closes in 722, and the narrative goes on in 723. 'Equidem' is 'indeed', 'for my part'. 'Suspensum… tenebo' is 'I will (not) hold you in suspense', 'suspensum' 'hung up', 'kept waiting'. 'Suscipit' is 'takes up (the talk)', 'replies'. 'Ordine singula pandit' is 'unfolds the particulars in order', and so he does: from the soul of the universe down to the fate of each human soul."""),
(727, 'miscet.',
 """“First, the sky and the lands and the plains of water
and the shining globe of the Moon and the Titan's stars
a breath within nourishes, and, poured through the limbs,
mind drives the whole bulk and with the great body mixes itself.""",
 """“To begin: the sky and the earth, the watery plains, the shining globe of the Moon and the Titan's stars draw their nourishment from a spirit inside them, and a mind, poured into every limb, keeps the whole bulk astir and blends itself with that vast body.""",
 """A new paragraph, and Anchises's long explanation opens. It joins Stoic teaching about a divine spirit or mind spread through the whole universe to the Pythagorean and Platonic doctrine of rebirth, in language often borrowed from Lucretius, who often opens an argument with 'principio', 'in the first place'. The objects come first and the verb 'alit', 'nourishes', waits until 726. 'Campos… liquentis' is 'the liquid plains', the sea, with the '-is' accusative plural. 'Titania astra' is 'the Titan's stars', usually taken of the sun (itself called Titan, as the son of the Titan Hyperion) together with the other stars. 'Spiritus' is 'breath', 'spirit'; 'mens' is 'mind'. 'Infusa per artus' is 'poured through the limbs': the universe is pictured as one great living body. 'Molem' is 'mass', 'bulk'."""),
(729, 'pontus.',
 """Thence the race of men and of beasts, and the lives of flying things,
and the monsters which beneath its marble surface the sea bears.""",
 """From it spring the race of men and of beasts, the life of all that flies, and the strange shapes the sea carries beneath its plain of polished marble.""",
 """'Inde' is 'from this (source)', the verb ('come', 'are') left out. 'Pecudum' is 'of cattle', beasts in general. 'Volantum' is 'volantium', the participle used as a noun, 'of flying things', with the shortened genitive plural. 'Marmoreo… aequore' is 'under the marble surface', the sea's calm shining like polished marble. 'Monstra' are the sea's strange creatures, not necessarily monsters. Land, air and water: all living things share the one spirit."""),
(732, 'membra.',
 """Fiery is to them the vigour and heavenly the origin,
to those seeds, so far as harmful bodies do not slow them
and earthly joints do not blunt them, and limbs that must die.""",
 """In these seeds there is a vigour of fire, and their birth is from heaven, so far as harmful bodies do not slow them down, nor earthly joints and dying limbs blunt their edge.""",
 """'Ollis' is the archaic form of 'illis', from old epic (Ennius), here a dative of possession, 'to them belongs'; 'seminibus', 'to (those) seeds', stands in apposition to it in the next line. The 'seeds' are the particles of the world-spirit in every living thing. 'Igneus… vigor' is 'fiery vigour': for the Stoics the divine spirit was a kind of fire. 'Quantum non… tardant' is 'in so far as… do not slow', the 'non' carrying on to 'hebetant'. 'Moribunda' is 'doomed to die'. The body as a clog on the soul is Plato's thought (Phaedo)."""),
(734, 'caeco.',
 """Hence they fear and desire, grieve and rejoice, nor the airs
see clearly, shut in darkness and a blind prison.""",
 """From this come their fears and desires, their griefs and their joys; and shut up in darkness, in a prison without light, they cannot look out and see the open air.""",
 """'Hinc' is 'from this', the body. The four verbs name the four passions of Stoic teaching, fear, desire, grief and pleasure, set in two pairs. 'Dispiciunt' is 'see through', 'see clearly out'; 'auras' is 'the airs', the bright sky. 'Clausae' agrees with 'animae' understood: the subject has passed from 'they' (men) to their souls. 'Carcere caeco' is 'in a blind prison', the body as the soul's prison, again a Platonic picture."""),
(738, 'miris.',
 """Nay even when with the last light life has left them,
not, however, every evil from the wretches nor utterly all
the bodily plagues depart, and deep within it must be
that many things long grown together in wondrous ways become ingrained.""",
 """And more: even when life has left them with the last light of day, the unhappy souls are still not rid of every ill, not wholly free of all the body's corruptions, and much that has long grown into them must, in strange ways, sink deep and take root.""",
 """'Quin et' is 'nay, even', a step further. 'Supremo… lumine' is 'with the last light', the day of death; 'reliquit' (perfect) has 'eas', 'them', understood. 'Omne malum' and 'omnes… pestes' are the subjects of 'excedunt', 'go out'; 'miseris' is a dative of separation, 'from the wretched (souls)'. 'Corporeae excedunt' elides. 'Necesse est' takes the infinitive 'inolescere', 'to grow in', with 'multa… concreta' as its subject, 'many things grown hard together'. 'Modis… miris' is 'in wondrous ways', a phrase Lucretius likes."""),
(740, 'expendunt:',
 """Therefore they are schooled with punishments, and of old wrongs
the penalties they pay out:""",
 """So they are put to work by penalties, and pay out in torment for ancient wrongs:""",
 """'Exercentur' is 'are exercised', 'are kept at work', 'harried'. 'Supplicia expendunt' is 'pay out the penalties', 'expendo' first meaning 'weigh out' (money, in the old way). The punishment here is a cleansing that ends, not the everlasting punishment of Tartarus described in the previous part."""),
(741, 'ventos;',
 """some are spread out, empty,
hung up to the winds;""",
 """some are stretched out, insubstantial, and hung in the winds;""",
 """'Aliae… aliis' (740–741) is 'some… for others', dividing the souls. 'Panduntur' is 'are spread out', 'inanes' 'empty', 'unsubstantial', and 'suspensae ad ventos' 'hung up to the winds': the cleansing by air. Three elements purify, air, water and fire; what is purged is the earthly part."""),
(742, 'igni;',
 """for others under a vast whirlpool
the ingrained crime is washed out, or burnt out with fire;""",
 """for others, the ingrained sin is rinsed away under a great swirl of water, or burnt out of them by fire;""",
 """'Aliis' is a dative of reference, 'for others'. 'Infectum' is 'dyed in', 'ingrained', from 'inficio', a word from dyeing: the crime is a stain. 'Eluitur' 'is washed out', 'exuritur' 'is burned out', two compounds of 'ex-' side by side. 'Igni' is the ablative, 'with fire'."""),
(743, 'Manes;',
 """each we suffer our own Manes;""",
 """every one of us endures the ghostly lot that is his own;""",
 """A famous hard phrase. 'Manes' are the spirits of the dead; here it seems to mean the lot that each soul must bear after death for what it was in life, its own ghostly fate. 'Quisque', 'each', stands in apposition to the 'we' of 'patimur': Anchises suddenly speaks in the first person plural, including himself among the souls. The Latin Library's 'manis' is only another spelling of the accusative plural."""),
(744, 'tenemus;',
 """thence through wide
we are sent Elysium, and we few hold the joyful fields;""",
 """after that we are sent out through the wide spaces of Elysium, and only a handful of us remain in possession of these glad meadows;""",
 """'Exinde' is 'after that'. 'Per amplum… Elysium' is 'through wide Elysium', with a hyperbaton across the line end; 'mittimur' is 'we are sent'. 'Pauci laeta arva tenemus' is 'we few hold the happy fields': a few souls, Anchises among them, stay in Elysium and are not reborn. The order of the stages in 743–751 is a famous puzzle. One reading takes 'donec' (745) with the few: they stay in Elysium until time has left them pure fire, and are not reborn; another takes 'pauci… tenemus' as an aside, and 'donec' with the cleansing of the rest, who then go to Lethe (748)."""),
(747, 'ignem.',
 """until long time, the circle of time completed,
has taken away the hardened stain, and pure leaves
the ethereal sense and the fire of unmixed air.""",
 """until length of days, once time has run its full circle, has lifted out the stain hardened in them, and leaves clean the sense that belongs to the upper sky and the fire of unmixed air.""",
 """'Donec' is 'until', here with the indicative. 'Longa dies' is 'long time': 'dies' is feminine in this sense, a stretch of time. 'Perfecto temporis orbe' is an ablative absolute, 'the circle of time having been completed'. 'Concretam… labem' is 'the stain grown hard', picking up 'concreta' in 738. 'Exemit' is the perfect, 'has taken out'. 'Aetherium sensum' is 'the ethereal sense', the soul's power of perceiving, made of heaven's fire. 'Auraï' is Greenough's archaic genitive singular in '-āī' for 'aurae', which Lucretius uses often; the diaeresis marks the ending as two syllables, so the word scans au-rā-ī. 'Simplicis' is 'unmixed', 'pure'."""),
(751, 'reverti.”',
 """These all, when a thousand years the wheel they have rolled through,
to the Lethean river the god calls forth in a great column,
that, to be sure, unremembering they may see again the vaults above,
and begin into bodies to be willing to return.”""",
 """And when these have rolled the wheel round for a thousand years, a god summons them all in a vast company to the Lethe stream, so that, their memory wiped clean, they may look once more on the curving sky above and start to want to go back into bodies.”""",
 """'Volvere' is 'volverunt', the '-ere' perfect again, 'they have rolled'. 'Rotam' is 'the wheel' of time, the cycle of a thousand years; in Plato's myth of Er the soul's journey between lives lasts a thousand years. 'Deus' is 'a god', unnamed. 'Scilicet' is 'of course', 'you see': this is why they drink Lethe. 'Ut… revisant… incipiant' is a purpose clause. 'Immemores' is 'unremembering'. 'Supera… convexa' is 'the vaults above', the sky of the upper world. 'Velle reverti' is 'to want to return': this answers Aeneas's question at 721. The closing mark ends the speech."""),
(755, 'vultus.',
 """Anchises had spoken, and his son and with him the Sibyl
into the middle of the gatherings draws and the murmuring crowd,
and a mound he takes, whence all in a long line he might
facing him review, and learn the faces of those coming.""",
 """Anchises had done speaking. He led his son, and the Sibyl with him, into the thick of the assembled crowds and their murmur, and climbed a knoll from which he could review them all in their long column as they faced him, and pick out the features of each newcomer.""",
 """A new paragraph in Greenough. 'Dixerat' is the pluperfect, 'had spoken', the usual way of closing a speech and moving on. 'Natumque unaque Sibyllam' is 'his son and, with him, the Sibyl', 'una' the adverb 'together'. 'Conventus' is accusative plural, 'gatherings'. 'Unde… possit… legere' is a relative clause of purpose, 'from where he could review'; the Latin Library's 'posset' follows the past sense instead of the historic present 'trahit', with no change of meaning. 'Legere' is 'to read off', 'to review', as a general reviews troops; 'adversos' is 'facing (him)'. 'Venientum' is 'venientium', 'of those coming'. So begins the pageant of Roman heroes, a counterpart of Odysseus's catalogue of famous shades (Odyssey 11), and like a Roman funeral, where the masks of a family's ancestors were carried in procession."""),
(759, 'docebo.',
 """“Now come, the Dardan offspring what glory hereafter will follow,
what descendants await from the Italian race,
illustrious souls and destined to go into our name,
I will set out in words, and teach you your fates.""",
 """“Come now: the glory that is to follow the Dardan line in after times, the descendants who wait for us from Italian blood, bright souls who will pass into our name — these I will set forth for you in words, and make your destiny known to you.""",
 """A new paragraph, and Anchises's second speech opens; it runs on past the end of this part. 'Nunc age' is 'come now', a call to attention. Two indirect questions, 'quae… gloria… sequatur' and 'qui maneant… nepotes', hang on 'expediam'; 'deinde' is 'hereafter'. 'Dardaniam prolem' is the Trojan line, from Dardanus, the founder of the house. 'Itala de gente' looks to the marriage with Lavinia. 'Inlustris' is 'illustres', the '-is' accusative plural, in apposition to the descendants. 'In nomen ituras' is 'that will go into our name', inherit it. 'Expediam dictis' is 'I will unfold in words'. 'Docebo' takes two accusatives, 'te' and 'fata'."""),
(762, 'surget,',
 """He, you see, the youth who leans on a pure spear,
holds by lot the nearest places of the light; first to the airs
of heaven, mixed with Italian blood, he will rise,""",
 """That youth — you see him? — who rests his weight on a spear without a point has drawn the station closest to the daylight; he will be the first to rise into the upper air with Italian blood mingled in him,""",
 """The sentence runs to 766 and is divided here at a comma. 'Ille, vides,… iuvenis' is 'that youth, you see', with 'vides' put in as an aside. 'Pura… hasta' is 'a pure spear', a spear without an iron head; the hasta pura was a Roman military honour, and Servius takes it here as the prize for a first victory. 'Nititur' takes the ablative, 'leans on'. 'Proxuma' is Greenough's older spelling of 'proxima', like 'maxumus'; 'proxuma… lucis loca' is 'the places nearest the light': he will be the next to be born. 'Sorte' is 'by lot'. 'Italo commixtus sanguine' is 'mixed with Italian blood', as the son of Aeneas and the Latin princess Lavinia."""),
(766, 'Alba.',
 """Silvius, an Alban name, your last-born offspring,
whom to you, long-lived, late, Lavinia your wife
will rear in the woods, a king and of kings the parent,
from whom our race in Long Alba will hold sway.""",
 """Silvius, a name of Alba, the child of your last years, whom, late in your long life, your wife Lavinia will bring up for you in the forests: a king, and sire of kings, from whom our race will hold dominion in Alba Longa.""",
 """The print has 'silvius', a misprint for 'Silvius', corrected here: the name stands at the head of the line, in apposition to 'ille' (760), and Greenough prints it with a capital at 769; t keeps the print, because t must match the pinned source; l and i give the reading. 'Albanum nomen' is 'an Alban name', because all the later kings of Alba bore it. 'Postuma' is 'last-born'; the ancient commentators took it as 'born after his father's death', which sits awkwardly with 'tibi longaevo serum', 'late-born to you in your old age'. 'Educet silvis' is 'will bring up in the woods', the source of the name, from 'silva'. 'Regem regumque parentem' is 'a king and father of kings'. 'Unde' is 'from whom'; 'Longa… Alba' frames the clause, Alba Longa, the city founded by Ascanius."""),
(770, 'Albam.',
 """Next him is Procas, glory of the Trojan race,
and Capys, and Numitor, and he who you in name will give back,
Silvius Aeneas, equally in piety or in arms
outstanding, if ever to rule he receives Alba.""",
 """Close beside him is Procas, the glory of the Trojan nation, and Capys, and Numitor, and the one who will restore your name to the world, Silvius Aeneas, as eminent for his piety as for his feats of arms — if ever he is allowed to take up the rule of Alba.""",
 """A new paragraph in Greenough. 'Proxumus' is 'proximus' again, with the old spelling. Procas, Capys and Numitor are kings of Alba Longa, not named in the order of Livy's list (1.3), where Aeneas Silvius is the second king and Procas the father of Numitor; Numitor was the grandfather of Romulus. 'Qui te nomine reddet' is 'who will give you back in name', by bearing the name Aeneas. 'Pietate vel armis' is 'in piety or in arms', 'vel' here hardly more than 'and', with 'pariter', 'alike'. 'Si umquam… acceperit' is a future perfect: the ancient commentator Servius has a story that a guardian kept the throne from him until late in life."""),
(771, 'iuvenes!',
 """What young men!""",
 """What young men they are!""",
 """'Qui' is the interrogative adjective used in an exclamation, 'what (fine) young men!'"""),
(772, 'quercu!',
 """How great, look, the strength they display,
and shaded they wear their temples with the civic oak!""",
 """See how much strength they make a show of, and how they wear their temples shaded with the oak of the civic crown!""",
 """'Aspice', 'look', is put in as an aside, like 'vides' at 760. 'Vires' is 'strength' (the Latin Library's 'viris' is another spelling of the plural). 'Umbrata… tempora' is an accusative, 'their shaded temples', with 'gerunt', 'they wear'. 'Civili quercu' is 'with the civic oak', the 'corona civica', the oak-leaf crown given to a soldier who saved a citizen's life; the senate voted one to Augustus in 27 BC. Virgil gives it, out of its time, to these ancient kings, perhaps as saviours of their people and founders of towns."""),
(775, 'Coramque.',
 """These for you Nomentum and Gabii and the city of Fidena,
these will set on the hills the Collatine citadels,
Pometii and the Fort of Inuus and Bola and Cora.""",
 """These will found for you Nomentum and Gabii and the town of Fidenae, these will set the towers of Collatia on the hills, and Pometii, and the Fort of Inuus, and Bola and Cora.""",
 """'Tibi' is the ethical dative, 'for you', 'you will see'. 'Hi… hi' is anaphora, 'these… these'. 'Imponent montibus arces' is 'will set citadels on the hills', and the verb serves for all the towns. These are old towns of Latium, some held to be Alban colonies; by Virgil's day several were small or deserted. 'Fidenam' is a singular for the usual plural Fidenae; 'Collatinas… arces' is Collatia; 'Pometios' is Suessa Pometia; 'Castrum Inui' is 'the fort of Inuus', a country god likened to Pan. The doubled '-que… -que' in 775 runs the list on."""),
(776, 'terrae.',
 """These then will be names; now they are lands without a name.""",
 """In that age these will be famous names; today they are stretches of country that no one has named.""",
 """'Haec' (these places) is the subject, with 'nomina' the predicate: they will then be names, that is, names of note. The line plays on 'nomina… nomine', with 'tum' and 'nunc' set against each other: in Anchises's present, Latium is still wild land; the towns are to come."""),
(779, 'educet.',
 """Nay, to his grandfather as companion himself the son of Mavors will add,
Romulus, whom of the blood of Assaracus Ilia his mother
will rear.""",
 """More: a child of Mars, Romulus, will attach himself to his grandfather as a companion, he whom Ilia, a mother sprung from the blood of Assaracus, will rear.""",
 """A new paragraph in Greenough. 'Quin et' is 'nay more'. 'Avo comitem sese… addet' is 'will add himself as a companion to his grandfather', Numitor, whom Romulus restored to the throne of Alba. 'Mavortius' is 'son of Mavors', the old form of 'Mars' (the Latin Library spells it 'Mauvortius'). 'Assaraci… sanguinis' is a genitive of description with 'Ilia', 'of the blood of Assaracus': Assaracus was the grandfather of Anchises, so Romulus is Trojan on his mother's side too. Ilia is Rhea Silvia, the Vestal who bore Romulus and Remus to Mars; her name here points to Ilium. 'Educet' is 'will bring forth', 'rear'."""),
(780, 'honore?',
 """Do you see how twin on his head stand the crests,
and the father himself with his own honour of the gods already marks him?""",
 """Do you see the twin crests standing on his helmet, and how his father himself already marks him out with his own sign of godhead?""",
 """'Viden' is 'videsne', 'do you see?', with the final 's' dropped before '-ne', as in everyday speech and comedy. 'Ut' is 'how', introducing an indirect question in the indicative, an older and livelier usage than the subjunctive. 'Geminae… cristae' are 'twin crests', a helmet with a double plume, usually taken as a mark of Mars. 'Pater ipse' may be Mars, his father, marking him with his own emblem, or Jupiter, 'the father of the gods', if 'superum' is taken with 'pater'; taken with 'honore', 'superum' (= 'superorum') makes it 'the honour of the gods', a sign that Romulus will himself become a god, as Quirinus."""),
(784, 'virum:',
 """Look, under his auspices, son, that renowned Rome
her empire to the lands, her spirits to Olympus will make equal,
and seven, one city, for herself with a wall will enclose citadels,
blessed in an offspring of men:""",
 """Behold, my son: by his auspices that famous Rome will make her dominion match the lands of the world and her courage match Olympus, and, one city, will throw a single wall around seven strongholds, fortunate in her progeny of men:""",
 """'En' is 'look!'. 'Huius… auspiciis' is 'under his auspices', the omen of the birds by which Romulus founded the city, and the right of a Roman commander to take the auspices. 'Incluta' is 'famous', Greenough's spelling of 'inclita'. 'Imperium terris, animos aequabit Olympo' is one verb with two pairs: 'aequo' takes the dative, 'will make her power equal to the earth, her spirit to Olympus'. 'Septem… arces' are the seven hills of Rome; 'una' is 'one', the single city, set against 'septem'. 'Prole virum' is 'in her offspring of men', 'virum' being 'virorum', the old genitive plural."""),
(787, 'tenentes.',
 """as the Berecyntian mother
rides in her chariot, tower-crowned, through the Phrygian cities,
glad in her birth of gods, embracing a hundred grandsons,
all heaven-dwellers, all holding the heights above.""",
 """just as the Berecyntian Mother rides in her car through the towns of Phrygia, a crown of turrets on her head, delighted with the gods she has given birth to, clasping a hundred descendants, all of them denizens of the sky, all of them possessors of the lofty realms above.""",
 """A simile: Rome among her sons is like Cybele, the Great Mother of the gods, called 'Berecyntian' from Mount Berecyntus in Phrygia. She wore a crown of towers, the city-wall crown, and rode in a chariot drawn by lions; Lucretius describes her procession in his second book (from 2.600). Her cult, from Phrygia near Troy, was brought to Rome in 204 BC, so she is a Trojan goddess too. 'Laeta deum partu' is 'glad in her offspring of gods', 'deum' being 'deorum'. 'Complexa' is 'having embraced', 'holding in her arms'. 'Omnes… omnes' is anaphora; 'caelicolas' is 'heaven-dwellers', and 'supera alta' 'the lofty heights above'."""),
(789, 'tuos.',
 """Hither both now turn your eyes, look at this race
and your Romans.""",
 """Bend both your gazes this way now: look at this nation, the Romans who are yours.""",
 """A new paragraph in Greenough, and Anchises leaps from the founding of Rome to Virgil's own day. 'Geminas… acies' is 'your twin eyes', 'acies' being 'sight', 'the eye'. 'Flecte' and 'aspice' are imperatives. 'Romanos… tuos' is 'your Romans': they are Aeneas's descendants and his people."""),
(790, 'axem.',
 """Here is Caesar and all of Iulus
the offspring, destined to come under the great axis of the sky.""",
 """Here stands Caesar, and the whole progeny of Iulus that is destined to rise into the light beneath the great pole of heaven.""",
 """'Hic' is 'here'. 'Caesar' is probably Julius Caesar, with the whole Julian house after him (some take it of Augustus, named in 792); the Julii claimed descent from Iulus, Aeneas's son (1.288). 'Iuli' scans as three syllables, I-u-li. 'Ventura' is 'about to come', the future participle; 'magnum caeli… sub axem' is 'beneath the great axis of the sky', into the world of the living."""),
(795, 'imperium:',
 """This man, this is he, whom you hear promised to you rather often,
Augustus Caesar, offspring of the Deified, who golden will found
ages once more in Latium, through the fields ruled
by Saturn of old, and beyond both Garamantes and Indians
will push forward the empire:""",
 """This is the man, yes, this is he, whom you hear pledged to you again and again: Augustus Caesar, offspring of a god, who will found anew in Latium an age of gold, across the countryside that Saturn ruled in times long past, and push the bounds of empire beyond the Garamantes and the Indians:""",
 """'Hic vir, hic est' repeats 'hic' for emphasis: 'this is the man, this is he'. 'Tibi… promitti' is an accusative and infinitive with 'audis'; 'saepius' is 'often', the comparative used loosely, as at 695. 'Augustus' was the title given to Octavian in 27 BC. 'Divi genus' is 'offspring of the Deified': Julius Caesar, his adoptive father, was declared a god in 42 BC. 'Qui' is held back to 793, and governs both 'condet' and 'proferet'. 'Aurea… saecula' is 'golden ages', the golden age of Saturn, who once ruled in Latium (as told at 8.319–325; compare the Fourth Eclogue). 'Regnata… Saturno' is 'reigned over by Saturn', an intransitive verb used in the passive. 'Super… Garamantas et Indos' is 'beyond the Garamantes and Indians': L. Cornelius Balbus triumphed over the Garamantes of the Sahara in 19 BC, and Indian embassies came to Augustus."""),
(797, 'aptum.',
 """lies outside the stars a land,
outside the paths of the year and of the sun, where sky-bearing Atlas
the axis on his shoulder turns, fitted with burning stars.""",
 """there is a country lying beyond the constellations, beyond the roads of the year and of the sun, where Atlas the sky-bearer turns on his shoulder the axle of heaven, studded with blazing stars.""",
 """'Iacet… tellus' is 'there lies a land', said without a connecting word: the empire will reach it. 'Extra sidera' is 'outside the constellations', meaning the signs of the zodiac, through which the sun travels in the year; 'anni solisque vias' says the same thing again. So the land lies far to the south, beyond the sun's track. 'Caelifer' is 'sky-bearing', a compound adjective. Line 797 is repeated from 4.482 (where Greenough prints 'humero'). 'Aptum' is 'fitted', 'set', with the ablative 'stellis ardentibus'."""),
(800, 'Nili.',
 """At his coming even now both the Caspian kingdoms
at the oracles of the gods shudder and the Maeotic land,
and of the sevenfold Nile the alarmed mouths are in turmoil.""",
 """Against his coming the realms of the Caspian and the land by Lake Maeotis are already bristling with dread at the answers of the gods, and the sevenfold Nile is thrown into confusion at all its frightened mouths.""",
 """'Huius in adventum' is 'against his coming', 'in' with the accusative of a time looked forward to. 'Et… et' is 'both… and'. 'Caspia regna' are the realms around the Caspian Sea, towards Parthia; 'Maeotia tellus' is the land by Lake Maeotis (the Sea of Azov), the Scythians' country. 'Responsis… divom' is 'at the replies of the gods', oracles foretelling his conquests; 'divom' is 'divorum', the old genitive plural ('divum' in the Latin Library). 'Septemgemini' is 'sevenfold', for the seven mouths of the Nile; Egypt was taken by Octavian in 30 BC. 'Turbant' is intransitive, 'are in confusion', and 'trepida' 'alarmed'. Anchises's speech goes on into the next part."""),
]
P = A.part('aeneid-047'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units')
