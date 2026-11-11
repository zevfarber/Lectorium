import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..')); sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..'))
import aeneid_lib as A
# aeneid-049 draft. Drafted from the Latin and grammar only. t is cut from the edition, never typed.
TITLE = 'Ostia Tiberis. Prodigia Latini'
TITLE_EN = "The Tiber and the Omens of Latium — Aeneid VII.1–106"
PART = "The Tiber and the Omens of Latium (VII.1–106)"
ABOUT = """The second half of the poem begins. Aeneas's old nurse Caieta dies and gives her name to the harbour where she is buried; once her rites are paid, the Trojans sail on by moonlight past the headland of Circe, the daughter of the Sun, where from the enchantress's halls come the roars of lions, boars, bears and wolves, men whom her drugs have turned into beasts. Neptune fills their sails and carries them safely past. At dawn the wind drops, and Aeneas sees from the sea a great wood through which the Tiber, yellow with sand, bursts into the sea among singing birds; he turns his ships into the river with joy. The poet calls on Erato for a new and greater theme: the kings and the state of ancient Latium, and the war that is to come. Latinus, son of Faunus and grandson of Picus, whose line goes back to Saturn, has ruled long in peace; he has no son, only a daughter, Lavinia, now of an age to marry, and many princes seek her, Turnus the handsomest and best-born of them, with the queen eager for the match. But portents stand in the way. A swarm of bees settles on the top of the sacred laurel in the palace, and a seer declares that a foreign man is coming with his army to rule from the citadel; and while Lavinia stands beside her father at the altar her hair catches fire, and she seems to be wrapped in flame and to scatter fire through the palace, a sign of glory for her and of war for her people. Latinus goes to the oracle of his father Faunus in the grove beneath Albunea, sleeps on the fleeces of the sheep he has sacrificed, and hears a voice from the grove: he must not marry his daughter to a Latin, for foreign sons-in-law are coming whose descendants will rule the whole world from the rising to the setting sun. Latinus does not keep the answer to himself, and Rumour has already spread it through the Ausonian cities when the Trojans moor their fleet on the grassy bank of the Tiber."""
U = [
(2, 'dedisti;',
 """You too to our shores, nurse of Aeneas,
undying fame by dying, Caieta, have given;""",
 """You too, Caieta, nurse of Aeneas, gave our shores a fame that will never die when you died here;""",
 """Book VII opens the second half of the poem, the Iliadic half of war in Italy. 'Tu quoque' links Caieta to the companions Book VI left behind in names on the coast, Misenus (6.234) and Palinurus (6.381): she too gives a place its name, Caieta (modern Gaeta), the harbour where Aeneas landed at the very end of Book VI. 'Aeneia nutrix' is 'the Aenean nurse', the adjective doing the work of a genitive, 'Aeneas's nurse'. 'Litoribus nostris' is 'to our shores': the poet speaks as an Italian. 'Aeternam moriens' sets 'eternal' against 'dying' side by side. 'Dedisti' is perfect, 'you have given'; the address in the second person to a dead character (apostrophe) is a mark of feeling."""),
(4, 'signat.',
 """and now guards your honour your resting-place, and your bones a name
in great Hesperia, if that is any glory, mark.""",
 """and now the honour paid you keeps watch over your resting-place, and in great Hesperia a name marks where your bones lie, if there is any glory in that.""",
 """'Servat honos sedem tuus' is 'your honour guards your seat', the place where she lies, 'sedem' the grave. 'Ossaque nomen… signat' is 'and the name marks your bones': the place-name is her epitaph. 'Hesperia', 'the western land', is a Greek name for Italy. 'Siqua est ea gloria' is 'if that is any glory' — a characteristic doubt about what fame can do for the dead; 'siqua' is Greenough's one-word printing of 'si qua', 'if any', 'qua' the indefinite after 'si'. Note the order in 'sedem tuus' and 'ossaque nomen', words of two clauses interleaved."""),
(7, 'relinquit.',
 """But dutiful, the funeral rites duly performed, Aeneas,
the mound of the tomb having been heaped up, after the deep had grown still,
the waters, sets his course with sails and leaves the harbour.""",
 """But Aeneas, ever faithful, when he had paid her funeral rites with due care and raised a mound over her grave, set his course under sail as soon as the deep seas had fallen calm, and left the harbour.""",
 """'Pius' is Aeneas's standing epithet, his sense of duty, shown here in caring for the dead. Two ablatives absolute, 'exsequiis… rite solutis', 'the funeral rites having been duly discharged' ('solvere' of paying what is owed), and 'aggere composito tumuli', 'the mound of the grave-barrow having been heaped up'. 'Quierunt' is 'quieverunt', the shortened perfect, 'had become calm'; 'alta… aequora', 'the deep waters', frames the clause across the line-end. 'Tendit iter velis' is 'directs his way with sails', 'sails on'. The present tense ('tendit', 'relinquit') is the historic present, used throughout the narrative."""),
(9, 'pontus.',
 """Breathe on the breezes into the night, nor the shining his course
Moon denies, glitters beneath the trembling light the sea.""",
 """The breezes blow fair on into the night, and the bright moon does not refuse its light to their course; under its quivering beams the sea gleams.""",
 """'Adspirant' (Greenough's unassimilated spelling of 'aspirant', 'breathe upon', 'blow favourably') — the winds are behind them. 'In noctem' is 'into the night', 'as night comes on'. 'Nec… negat' is litotes, 'nor does she refuse (light)': the moon is bright and full. 'Cursus' is accusative plural, 'their voyage', a poetic plural; 'candida' goes with 'Luna'. 'Splendet… pontus' stands alone without a connective (asyndeton). 'Tremulo sub lumine' is the moon's light shimmering on the water: an often-admired line, the sound of 'splendet tremulo' imitating the trembling."""),
(14, 'telas.',
 """Next are skimmed the shores of Circe's land,
where the rich daughter of the Sun her unapproachable groves
with ceaseless song makes resound, and in her proud halls
burns fragrant cedar to give light in the night,
with the shrill comb running through the fine webs.""",
 """Next they skirt close by the coast of Circe's country, where the wealthy daughter of the Sun makes her forbidden groves ring with her unending song, and in her lofty halls burns sweet-scented cedar to light the night, while her rattling comb runs through the delicate threads of her loom.""",
 """The headland of Circeii (Monte Circeo), on the coast of Latium south of the Tiber, was held to be Circe's home; in Virgil's day it was joined to the mainland, but it had been thought an island. 'Proxima' is predicative, 'close by', 'next'; 'raduntur' is 'are grazed', 'skimmed': they pass close in. Circe is the daughter of the Sun ('Solis filia'). The picture comes from the Odyssey, Book 10, where Odysseus's men find Circe singing in her house as she works at a great loom, and wolves and lions prowl round it — men she has bewitched. 'Inaccessos' is 'not to be approached'. 'Resonat' is used transitively, 'makes the groves ring'. 'Nocturna in lumina' is 'for lights by night', purpose with 'in'. 'Arguto… pectine' is 'with the shrill comb', the weaver's comb or batten that drives the weft home, which clicks and rattles; 'percurrens' is 'running over' the warp."""),
(16, 'rudentum,',
 """From here were heard groans and the rage of lions
the chains refusing and late in the night roaring,""",
 """From there could be heard the growls and fury of lions straining against their chains and roaring late into the night,""",
 """'Exaudiri' is a historic infinitive, used for the main verb of a vivid narrative: 'there were heard'; 'saevire' and 'ululare' in 18 are the same. 'Gemitus iraeque leonum' is 'the groans and wraths of lions', 'irae' the plural of outbursts of rage. 'Recusantum' and 'rudentum' are genitive plural participles agreeing with 'leonum', 'refusing' (fighting against) their chains and 'roaring'. 'Sera sub nocte' is 'in the depth of night', 'late in the night'."""),
(20, 'ferarum.',
 """and bristle-bearing swine and in their stalls bears
to rage, and shapes of great wolves to howl,
whom from the form of men the savage goddess with potent herbs
had clothed, Circe, into the faces and backs of wild beasts.""",
 """and bristly boars and bears penned in their stalls were raging, and the shapes of huge wolves howling: all once men, whom the cruel goddess Circe with her potent herbs had stripped of human form and dressed in the faces and hides of beasts.""",
 """'Saevire' and 'ululare' are historic infinitives, as 'exaudiri' in 15; the subjects 'sues' and 'ursi' and 'formae' are nominative. 'Saetigeri' is 'bristle-bearing', a compound adjective in the old epic manner. 'Praesaepibus' (Greenough's spelling of 'praesepibus') are stalls or pens. 'Formae magnorum luporum' is 'the shapes of great wolves': they look like wolves but are not. 'Quos' covers all the beasts. 'Ex facie hominum' is 'out of the appearance of men'; 'induerat… in voltus ac terga ferarum' is a bold phrase, 'had clothed (them) into the faces and backs of beasts', 'induo' (put on, as a garment) used of transformation. In the Odyssey Circe turned Odysseus's men into swine with a drug in their drink. 'Voltus' is Greenough's old spelling of 'vultus'. 'Dea saeva… Circe' frames the sentence's subject across the line-end."""),
(24, 'vexit.',
 """And lest such monstrous things the dutiful Trojans should suffer,
carried into the harbour, or the dread shores should approach,
Neptune with winds filled their sails, favouring ones,
and gave them flight and past the boiling shallows carried them.""",
 """So that the faithful Trojans might not undergo such monstrous change by putting into that harbour or set foot on that dreadful shore, Neptune filled their sails with following winds, sped their escape and carried them beyond the seething shallows.""",
 """'Quae' is a connecting relative, 'and these', with 'monstra… talia'. 'Ne… paterentur… neu… subirent' is a negative purpose clause, 'so that they should not suffer… nor approach'. 'Pii' again: the Trojans as a whole share their leader's piety, and the gods protect them for it. 'Delati in portus' is 'having been carried into the harbour'. Neptune, who promised Venus a safe voyage to Italy (5.779–815), keeps his word. 'Fugam dedit' is 'gave (them) flight', 'let them escape'. 'Vada fervida' are the 'seething shallows' off the headland, where the sea foams over rocks."""),
(26, 'bigis:',
 """And now was reddening with rays the sea, and from the high air
Aurora in her rosy car was shining saffron-yellow:""",
 """And now the sea was growing red with the sun's first rays, and from high heaven Dawn shone yellow as saffron in her rosy chariot,""",
 """A new paragraph in Greenough. A dawn formula, like Homer's 'rosy-fingered Dawn'. 'Rubescebat' is an inceptive verb (the '-sco' ending), 'began to grow red'; the imperfects set the scene. 'Aethere ab alto' is 'from the lofty sky'. 'Lutea' is 'saffron-coloured', golden-yellow, Homer's 'saffron-robed' Dawn. 'Bigis' is the two-horse chariot ('bigae', plural in form). The colon looks forward to 'cum' in the next line: 'it was dawn… when the winds dropped'."""),
(28, 'tonsae.',
 """when the winds laid themselves down, and all at once settled
every breath, and in the sluggish marble struggle the oar-blades.""",
 """when the winds dropped, every breath of air suddenly fell still, and the oars laboured in the slow, marble-smooth water.""",
 """'Cum' here is 'cum inversum', the 'when' that carries the main event after an imperfect scene-setting clause: 'the dawn was breaking, when…'. 'Posuere' is 'posuerunt', the '-ere' perfect (you'll see this constantly), used intransitively, 'the winds lay down'. 'Omnis… flatus' is 'every breath', the words split across the line. 'In lento… marmore' is 'on the sluggish marble': 'marmor' is the smooth, glittering surface of a calm sea. 'Luctantur… tonsae', 'the oar-blades struggle': with no wind they must row, and the still water seems heavy."""),
(30, 'prospicit.',
 """And here Aeneas a huge out of the water grove
looks out on.""",
 """And at this point Aeneas, looking out from the sea, catches sight of a vast wood.""",
 """'Hic' is 'at this point', of time as well as place. 'Ex aequore', 'from the sea', goes with 'prospicit': Aeneas looks out from the water. 'Ingentem… lucum', 'a huge grove', frames the phrase; 'lucus' is properly a sacred grove, and the woods round the mouth of the Tiber are full of gods. 'Prospicit' is held over to the next line, and the sentence ends there — a strong pause at the beginning of the line."""),
(32, 'prorumpit.',
 """Through this, with its pleasant stream, Tiberinus,
with rapid eddies and with much sand yellow,
into the sea bursts forth.""",
 """Through the middle of it the Tiber, with his lovely stream, yellow with abundant sand, breaks out into the sea in swirling eddies.""",
 """'Hunc inter' is 'between this', 'through it', the preposition put after its noun (anastrophe). 'Tiberinus' is the river and the river-god together; Virgil uses the god's name as the river's. 'Fluvio… amoeno', 'with pleasant stream', is a descriptive ablative. 'Verticibus rapidis' is 'with swift whirlpools'. 'Multa flavus arena', 'yellow with much sand': 'flavus' is the Tiber's stock epithet (Horace's 'flavum Tiberim'), from the silt it carries. 'Arena' is Greenough's spelling of 'harena', 'sand'. Here at last is the river named in Creusa's and the Sibyl's prophecies (2.782, 6.87)."""),
(34, 'volabant.',
 """Various, around and above,
used to the banks birds and to the river's channel,
the sky were soothing with song and through the grove were flying.""",
 """Birds of every kind that haunt the banks and the river's bed were filling the air round about and overhead with their sweet song and flying through the grove.""",
 """'Variae… volucres', 'various birds', frames two lines. 'Circumque supraque' is 'both around and above', the double '-que… -que'. 'Adsuetae' (Greenough's spelling of 'assuetae') takes the datives 'ripis' and 'alveo', 'accustomed to the banks and the riverbed'. 'Alveo' is read as two syllables, the 'e' running into the 'o' (synizesis). 'Aethera' is the Greek accusative of 'aether', 'the air'. 'Mulcebant', 'were soothing', 'charming': the birdsong caresses the air. 'Luco' is a dative of direction with 'volabant', or an ablative of place, 'in the grove'. The peaceful picture is the threshold of a land that will soon be at war."""),
(36, 'opaco.',
 """To turn the course his companions and to the land to direct the prows
he commands, and glad enters the shaded river.""",
 """He orders his comrades to change course and turn their prows to land, and joyfully he enters the shady river.""",
 """The print has 'flectere' with a small letter after the full stop at the end of 34, a misprint for 'Flectere', corrected here: a small letter after a question mark has been kept as Greenough's habit (6.845 'quo'), but after a full stop it is treated as a misprint (as 6.472). t keeps the print, because t must match the pinned source; l and i begin with a capital. 'Imperat' takes the infinitives 'flectere' and 'advertere', a poetic construction for 'imperat ut…', with 'sociis' the dative of the people ordered. 'Advertere proras' is 'turn the prows toward'. 'Laetus' is predicative, 'joyfully': he has reached the goal of seven years' wandering. 'Succedit' takes the dative 'fluvio', 'goes up into the river'; 'opaco', 'shady', because of the overhanging trees."""),
(40, 'pugnae.',
 """Come now, what kings, Erato, what were the times of things,
what in ancient Latium was the state, when the stranger fleet
first the army brought to the Ausonian shores,
I will set forth, and of the first battle I will recall the beginnings.""",
 """Come now, Erato: who the kings were, what the times were, what the state of affairs in ancient Latium when an army from abroad first beached its fleet on Ausonian shores, I will set out, and I will call to mind how the first fighting began.""",
 """A new paragraph in Greenough, and a second invocation, halfway through the poem, like the first at 1.8. 'Nunc age' is 'come now', a formula that rouses attention. Erato is the Muse of love poetry; Apollonius of Rhodes invokes her at the start of the third book of his Argonautica, where Medea falls in love with Jason. Virgil's war will be fought over a bride, Lavinia. 'Qui reges… quae tempora… quis… fuerit status' are indirect questions, all depending on 'expediam', 'I will unfold'; 'fuerit' is the perfect subjunctive they call for. 'Advena… exercitus', 'a stranger army', is the subject of 'appulit', 'brought (its fleet) to land'; 'classem' is the object; 'Ausoniis… oris' is dative. 'Exordia pugnae' is 'the beginnings of the fight'."""),
(41, 'mone.',
 """You the bard, you, goddess, admonish.""",
 """You, goddess, you must prompt your poet.""",
 """The print has 'tu' with a small letter after the full stop at the end of 40, a misprint for 'Tu', corrected here (the sense is the same either way); t keeps the print, because t must match the pinned source; l and i begin with a capital. 'Vatem' is the poet himself, the inspired singer; the Latin word means both prophet and poet. 'Tu… tu' is emphatic repetition (anaphora). 'Mone' is 'remind', 'prompt': the Muse supplies what the poet must tell."""),
(44, 'Hesperiam.',
 """I will tell of horrid wars,
I will tell of battle-lines, and driven by their passions to death kings,
and the Tyrrhenian band, and all under arms compelled
Hesperia.""",
 """I will tell of dreadful wars, I will tell of ranks drawn up for battle and of kings driven by their passions to their deaths, of the Etruscan band, and of all Hesperia forced to take up arms.""",
 """'Dicam… dicam' is anaphora again, the poet setting out his programme. 'Horrida bella' recalls the Sibyl's prophecy, 'bella, horrida bella' (6.86). 'Acies' are battle-lines. 'Actos animis in funera reges' is 'kings driven by their courage (or their passions) into deaths'; 'animis' may be either, and both are true of Turnus and Mezentius. 'Funera' is literally 'funerals', here 'deaths'. 'Tyrrhenam manum' is 'the Etruscan band': Etruscans fight on both sides, under Mezentius for Turnus and under Tarchon for Aeneas. 'Coactam' is 'forced together', 'mustered'; 'Hesperiam', the object, is held to the start of the line for weight, and the sentence stops there."""),
(45, 'moveo.',
 """Greater of things to me is born an order,
greater a work I set in motion.""",
 """A grander sequence of events is opening before me; a greater task I now set in motion.""",
 """'Maior rerum… ordo' is 'a greater order of events', a nobler series of happenings; 'mihi nascitur' is 'is born for me', 'opens before me'. 'Maior… maius' is another anaphora, in two forms of the same comparative. The war in Italy, the Iliadic half of the poem, ranks above the wanderings of the first six books, as war was the highest theme of epic. 'Moveo' is 'I set going', 'I undertake'. The print runs 'moveo.Rex' together with no space after the full stop (only the spacing is wrong; the reading text is unaffected); the unit can still end at the stop, and the next begins mid-line at 'Rex'."""),
(46, 'regebat.',
 """King Latinus the fields and the cities,
now rather old, in long peace, calm ones, ruled.""",
 """King Latinus, now growing old, had governed the countryside and its towns in a long, unbroken peace.""",
 """The print has 'moveo.Rex', with no space after the full stop, a misprint for 'moveo. Rex', corrected here; t keeps the print, because t must match the pinned source, and so this unit begins in the middle of line 45. 'Rex… Latinus' frames the subject; 'placidas', 'peaceful', agrees with 'urbes', and 'arva… et urbes… placidas' frames the object, 'the fields and the quiet cities'. 'Iam senior' is 'now rather old', the comparative without a stated standard. 'Regebat', imperfect, 'had been ruling', 'was ruling', sets the long settled state that the Trojans' arrival will break."""),
(49, 'auctor.',
 """Him by Faunus and the nymph Laurentine Marica begotten
we receive; to Faunus Picus was father, and he as his parent
you, Saturn, names; you of the blood the furthest founder.""",
 """He was the son, so tradition tells us, of Faunus and Marica, a nymph of Laurentum; Faunus's father was Picus, and Picus traced his descent to you, Saturn — you are the first founder of the line.""",
 """'Hunc… genitum (esse)… accipimus' is 'we receive (by tradition) that he was born', accusative and infinitive with a verb of hearing. Faunus is an old Italian god of woods and herdsmen, with an oracle (81 below); Marica was a nymph worshipped at Minturnae on the Liris, here called 'Laurentine', of Laurentum, Latinus's city. 'Fauno Picus pater' is 'to Faunus, Picus (was) father', a dative of possession with 'est' understood. Picus, an old Italian king and woodpecker-god, was turned into a woodpecker by Circe, whose shore the Trojans have just passed (the tale is told in 7.189–191 and by Ovid, Metamorphoses 14). 'Refert' is 'names', 'traces back to'. Saturn, driven from heaven by Jupiter, reigned in Latium in the Golden Age (8.319–325); 'ultimus auctor' is 'the furthest founder', the first ancestor. The poet turns to address Saturn directly (apostrophe), as he did Caieta in line 1."""),
(51, 'est.',
 """A son to him by the fate of the gods and male offspring
none there was, and in its early growth, rising, was snatched away in youth.""",
 """By the will of the gods he had no son, no male issue; the one he had was snatched away in early youth, just as he was coming into his own.""",
 """The print has 'filius' with a small letter after the full stop at the end of 49, a misprint for 'Filius', corrected here; t keeps the print, because t must match the pinned source; l and i begin with a capital. 'Huic' is a dative of possession with 'fuit', 'to him there was no son'. 'Fato divom' is 'by the decree of the gods'; 'divom' is the old genitive plural, 'divorum' (Latin Library 'diuum', the same word in the later spelling). 'Proles… virilis nulla' is 'no male offspring', the 'nulla' held to the next line. 'Primaque oriens erepta iuventa est' is 'and (the offspring), rising, was snatched away in its first youth': a son had been born, but died young. 'Oriens' is 'rising', like a star; 'prima… iuventa', ablative of time, frames the verb; 'erepta… est' is split by 'iuventa'."""),
(53, 'annis.',
 """Alone the house and such great seats was preserving a daughter,
now ripe for a husband, now with full years marriageable.""",
 """A daughter alone was left to keep the family and its great domain, already ripe for a husband, her years full and ready for marriage.""",
 """'Sola… filia' frames the line: one daughter, Lavinia (named at 72), kept the house going and was heir to the throne. 'Tantas… sedes' is 'so great a seat', the realm. 'Servabat' is 'kept', 'preserved', the hope of the line resting on her. 'Matura viro' is 'ripe for a husband', 'viro' a dative; 'plenis… annis', 'with full years', an ablative of respect or cause; 'nubilis' is 'marriageable', from 'nubo'. 'Iam… iam' repeats the point: she is of an age to marry, and so the suitors come."""),
(55, 'Ausonia.',
 """Many her from great Latium and all
Ausonia were seeking.""",
 """Many from the length of Latium and from all Ausonia were seeking her hand.""",
 """'Petebant' is 'were seeking (in marriage)', the regular word for courting. 'Magno e Latio totaque… Ausonia' is 'from great Latium and from all Ausonia', the preposition 'e' shared by both nouns; 'Ausonia' is held to the next line. Ausonia is an old name of a people of central Italy, used in verse for Italy as a whole."""),
(57, 'amore;',
 """Seeks before others, most handsome of all,
Turnus, by grandfathers and great-great-grandfathers powerful, whom the royal wife
to be joined as son-in-law was hastening with wondrous love;""",
 """Before all the others, and the handsomest of them all, Turnus sought her, a man powerful in his long line of ancestors, whom the queen was eager, with a wonderful love, to see joined to the house as her son-in-law;""",
 """'Petit ante alios… omnis' is 'seeks, before the others… of all'; 'omnis' is Greenough's accusative plural (for 'omnes'), with 'pulcherrimus' 'most handsome of all'. Turnus, prince of the Rutulians at Ardea, is the poem's great adversary, its Achilles or Hector; he is named here for the first time. 'Avis atavisque potens' is 'powerful in grandfathers and great-great-grandfathers', of noble descent; the double ending '-is… -is' gives a ringing phrase. 'Regia coniunx' is the queen, Amata, not yet named. 'Adiungi generum' is 'to be joined (as) son-in-law', 'generum' predicative; 'properabat' takes the infinitive, 'was hastening to have him joined'. 'Miro… amore' is 'with an extraordinary love', which will turn to frenzy in this book."""),
(58, 'obstant.',
 """but with various terrors the portents of the gods stand in the way.""",
 """but omens from the gods, frightening in many ways, stand in the way.""",
 """'Portenta deum' is 'portents of the gods', 'deum' = 'deorum', the old genitive plural. 'Variis… terroribus', 'with various terrors', frames the line; the ablative is of manner or means. 'Obstant' is 'stand in the way', 'oppose', the match. The two portents follow: the bees on the laurel (59–70) and the fire in Lavinia's hair (71–80)."""),
(63, 'colonis.',
 """A laurel there was in the middle of the house in the lofty inner rooms,
sacred in its foliage and with awe preserved through many years,
which father having found, when he was founding the first citadel,
himself was said to Phoebus to have consecrated, Latinus,
and the Laurentines from it the name to have given, the settlers.""",
 """In the middle of the palace, deep in the lofty inner rooms, there was a laurel, its leaves held sacred and preserved with reverent fear for many years; father Latinus himself, men said, had found it when he was building his first stronghold, had dedicated it to Phoebus and called his settlers Laurentines after it.""",
 """'Tecti medio in penetralibus altis' is 'in the middle of the house, in its deep inner rooms': the laurel grows in the inner court of the palace, as Priam's did in Troy (2.512–514). 'Sacra comam' is 'sacred as to its leaves', 'comam' an accusative of respect, the Greek construction (you'll see it often with parts of the body: 'accensa comas', 75). 'Metu' is 'religious awe'. 'Quam… inventam' is 'which, found', a participle where English uses a clause: 'which he had found'. 'Cum conderet' is 'when he was founding'. 'Ferebatur… sacrasse… posuisse' is 'was said to have consecrated… and to have given', the personal construction with 'fertur'; 'sacrasse' is 'sacravisse', shortened. The laurel is sacred to Phoebus Apollo. In 'Laurentisque ab ea nomen posuisse colonis', 'Laurentis' is accusative plural ('-is' for '-es'), the name itself in apposition to 'nomen', and 'colonis' is dative: 'gave the settlers the name Laurentes from it (ab ea, the laurel)'. The point is the etymology: Laurentum from 'laurus'."""),
(67, 'pependit.',
 """On its top bees in a dense mass (wonderful to tell),
with a huge whirring through the clear air carried,
settled on the crest, and by their feet through each other linked
a swarm sudden from the leafy bough hung.""",
 """Onto its very top — a marvel to relate — came bees in a thick mass, borne through the clear air with a mighty humming, and settled on the crest; and with their feet locked one into another a swarm suddenly hung from the leafy bough.""",
 """'Huius… summum… apicem' is 'the topmost crest of this (laurel)', the words spread over three lines. 'Mirabile dictu' is 'wonderful to tell', the supine in '-u'. 'Stridore ingenti' is 'with a huge buzzing'. 'Liquidum… aethera' is 'the clear air' (Greek accusative 'aethera'); 'vectae' is 'carried'. 'Obsedere' is 'obsederunt', 'besieged', 'occupied' — a military word that hints at the meaning. Greenough prints 'ex pedibus… nexis', 'from feet linked', so that the swarm 'hung from' its own interlocked feet; the Latin Library has 'et pedibus', 'and, with feet linked, a swarm… hung', which joins the two clauses. The picture hardly differs; with 'ex' the two clauses stand side by side with no connective, with 'et' they are joined. 'Per mutua' is adverbial, 'each into each'. 'Examen' is 'a swarm'. A swarm settling was an omen of strangers arriving to settle, since bees found a new colony when they swarm."""),
(70, 'arce.”',
 """Straightway the seer: “A foreign one we see,” he says,
“arriving, a man, and the same parts seeking a column,
from the same parts, and on the topmost citadel to be lord.”""",
 """At once the seer spoke: “We see a stranger arriving,” he said, “and an army making for the same quarter as the bees, out of the same quarter, and lording it from the top of our citadel.”""",
 """The print has '“Externum cernimus, ”inquit', with the closing mark set against 'inquit', a misprint for '“Externum cernimus,” inquit', corrected here; t keeps the print, because t must match the pinned source; l and i close the quotation before 'inquit'. 'Continuo vates' is 'at once the seer (said)', the verb of speaking left out and then supplied by 'inquit'. 'Externum… adventare virum' is accusative and infinitive after 'cernimus', 'we see a foreign man approaching'; 'adventare' is the frequentative of 'advenio', 'to be on the way'. 'Partis… easdem', 'the same parts', and 'partibus ex isdem', 'from the same parts', are a riddle: the newcomers will come from the quarter the bees came from and make for the same height. 'Isdem' is 'eisdem'. 'Dominarier' is the old present infinitive of the deponent 'dominor', for 'dominari', with the archaic ending '-ier', kept in solemn language: 'to be master'. 'Summa… arce' is 'on the top of the citadel', as the bees on the top of the laurel."""),
(73, 'ignem,',
 """Moreover, with pure torches while she kindles the altars,
and beside her father stands Lavinia the maiden,
she seemed (dreadful!) in her long hair to catch fire,""",
 """Besides this, while the maiden Lavinia was kindling the altars with pure torches, standing at her father's side, she was seen — a horror to tell — to catch fire in her long hair,""",
 """'Adolet… altaria' is 'kindles the altars', 'adoleo' meaning to burn in sacrifice; the subject is Lavinia, held back to the end of the next line, and the present with 'dum' is regular, 'while she kindles'. 'Castis… taedis', 'with pure torches', frames the clause: the purity of the rite makes the omen the more striking. 'Iuxta genitorem adstat' is 'stands beside her father'; 'adstat' is Greenough's spelling of 'astat'. Lavinia is named here for the first time. 'Visa (est)' is 'she was seen', 'she seemed', governing the infinitives 'comprendere' here and 'cremari', 'involvi', 'spargere' in 74–77. 'Nefas', 'unspeakable!', is an exclamation thrown in. 'Comprendere' is the shortened form of 'comprehendere', 'to catch (fire)', with 'longis… crinibus' 'in her long tresses'. The scene recalls the harmless flame on Ascanius's head at Troy (2.682–686), a sign of greatness to come."""),
(77, 'tectis.',
 """[and all her adornment with crackling flame to be burned]
and royal, set alight in her tresses, set alight in her crown
distinguished with jewels; then, smoky, in yellow light
to be wrapped, and through the whole house Vulcan to scatter.""",
 """[and all her finery to burn in crackling flame,] her royal tresses set alight, alight her crown with its jewels, and then, wreathed in smoke and tawny light, to be wrapped in fire and to scatter the fire-god all through the palace.""",
 """Greenough brackets line 74 as spurious, so it stands inside [ ] here; it reads like an addition meant to fill out the picture, and the sentence runs well without it. 'Ornatum' is her dress and ornaments; 'cremari' is 'to be burned'. 'Regalisque accensa comas' is 'set alight in her royal tresses', 'comas' an accusative of respect with the passive participle (as 'sacra comam', 60), and 'regalis' the accusative plural in '-is' agreeing with it; 'accensa… accensa' is anaphora. 'Coronam insignem gemmis' is 'her crown remarkable with jewels'. 'Fumida' is 'smoky'; 'lumine fulvo' is 'in yellow light'. 'Involvi' is 'to be wrapped' in fire. 'Volcanum' is the god of fire for fire itself (metonymy); 'Volcanum spargere' is 'to scatter fire'. 'Totis… tectis' is 'through the whole house'."""),
(78, 'ferri:',
 """That indeed dreadful and wonderful to see was reported:""",
 """This indeed was talked of as a terrible thing and a marvel to behold:""",
 """'Ferri' is a historic infinitive, 'was spoken of', 'was reported'; 'id' is its subject. 'Visu' is the supine, 'to see', 'in the seeing', as 'dictu' in 64. 'Horrendum ac… mirabile' are predicative, 'as dreadful and wonderful'. The colon introduces the explanation."""),
(80, 'bellum.',
 """for they sang that she would be famous in fame and fates,
herself, but for the people a great war it portended.""",
 """for the seers prophesied that she herself would be glorious in renown and destiny, but that for her people the sign foretold a great war.""",
 """'Canebant' has the seers for subject, 'they foretold' ('cano' of prophecy as well as song). 'Fore inlustrem… ipsam' is the accusative and infinitive, 'that she herself would be illustrious' — 'fore' is the future infinitive of 'sum'; 'inlustrem', 'brilliant', plays on the fire in her hair (Greenough's unassimilated spelling of 'illustrem'). 'Fama fatisque' is 'in fame and fortunes'. 'Sed populo magnum portendere bellum' is 'but that it (the omen) portended a great war for the people', the subject of 'portendere' changing to the portent itself. Light around the head was an omen of royalty and glory; smoke and fire spreading through the palace, of war."""),
(84, 'mephitim.',
 """But the king, troubled by the portents, the oracles of Faunus,
his fate-speaking father, approaches, and the groves beneath lofty
consults Albunea, which, greatest of woods, with its sacred
spring resounds, and, dark, breathes out a savage vapour.""",
 """But the king, disturbed by these portents, goes to the oracle of Faunus, his prophetic father, and consults the groves beneath high Albunea, the greatest of forests, which echoes with its holy spring and breathes out from its darkness a deadly sulphurous vapour.""",
 """A new paragraph in Greenough. 'Sollicitus monstris' is 'anxious at the portents', 'monstra' being any sign from the gods. 'Fatidici genitoris', 'fate-speaking father', stands in apposition to 'Fauni'. 'Oracula… adit' is 'goes to the oracle'; the plural 'oracula' is the place of oracles. Albunea is a sulphur spring and grove, with a nymph or Sibyl of the same name; Horace places an Albunea at Tibur, but Virgil seems to set it near Laurentum. 'Sub alta… Albunea', 'beneath lofty Albunea', is ablative. 'Nemorum quae maxima' is 'which, greatest of woods', 'quae' referring to Albunea. 'Sacro fonte sonat' is 'resounds with its holy spring'. 'Mephitim', with the Greek-style accusative in '-im', is a noxious exhalation from the ground, worshipped in Italy as a goddess, Mephitis. 'Opaca' is 'dark', 'shaded'."""),
(86, 'petunt;',
 """From here the Italian peoples and all the Oenotrian land
in doubts answers seek;""",
 """From here the peoples of Italy and the whole Oenotrian country seek responses in time of uncertainty;""",
 """'Hinc' is 'from here', from this oracle. 'Italae gentes' is 'the Italian peoples'; Oenotria, 'the land of wine', is an old Greek name for southern Italy, used for Italy at large. 'Petunt' is plural with the compound subject. 'In dubiis' is 'in doubtful matters', 'in times of uncertainty'. 'Responsa' are the god's answers."""),
(88, 'petivit,',
 """hither gifts the priest
when he has brought, and of slain sheep under the silent night
on the hides spread out has lain down and sleep has sought,""",
 """whenever the priest has brought his gifts here and has lain down in the silent night on the outspread fleeces of slaughtered sheep and courted sleep,""",
 """'Cum tulit… incubuit… petivit' is 'cum' with the perfect indicative in a general statement, 'whenever he has brought…', with the present 'videt' in the main clause (89). The rite is incubation: the priest (or the questioner) sleeps on the skins of the victims in the holy place and receives the god's answer in dreams. 'Huc' is 'hither'. 'Caesarum ovium… pellibus… stratis' is 'on the spread hides of slaughtered sheep'; 'caesarum' is the participle of 'caedo'. 'Sub nocte silenti' is 'in the silent night'. 'Incubuit' takes the dative, 'lay down upon'; 'somnos' is a poetic plural."""),
(91, 'Avernis.',
 """many in wondrous ways images he sees flitting,
and various hears voices, and enjoys of the gods
the converse, and in deepest Avernus addresses Acheron.""",
 """he sees many phantoms fluttering about in wondrous fashion, hears voices of many kinds, enjoys the converse of the gods and speaks with Acheron in the depths of Avernus.""",
 """'Multa… simulacra… volitantia' is 'many phantoms flitting', images of the dream. 'Modis… miris' is 'in wondrous ways', an old phrase found in Lucretius (1.123). 'Fruitur' is deponent and takes the ablative, 'enjoys the conversation', 'conloquio' (Greenough's spelling of 'colloquio'), carried over the line-end. 'Acheronta' is the Greek accusative of Acheron, the river of the underworld, here the powers below; 'adfatur' (for 'affatur') is 'addresses'. 'Imis… Avernis' is 'in deepest Avernus', the plural 'Averni' standing for the lower world, as at 5.732. The questioner talks with the gods above and the dead below."""),
(95, 'velleribus:',
 """Here and then father himself, seeking answers, Latinus
a hundred wool-bearing was sacrificing, duly, two-year sheep,
and on the hide of these propped and on the spread
fleeces he was lying:""",
 """Here, at that time, father Latinus himself, seeking an answer, was sacrificing with due rite a hundred woolly sheep of two years old, and lay propped on their skins, on the fleeces spread out beneath him:""",
 """'Hic et tum' is 'here and at that time'. 'Pater ipse… Latinus' frames the line: the king himself, not a priest, consults his own father. 'Lanigeras… bidentis' frames the next: 'bidentes' are sheep two years old, of an age for sacrifice (the name from the two grown teeth, by the old explanation); 'bidentis' is accusative plural in '-is'. 'Mactabat' is 'was sacrificing', the imperfect of what he was in the act of doing. 'Harum… tergo' is 'on the back (the hide) of these', 'effultus', 'propped', 'supported', taking the ablative; 'stratis… velleribus' is 'on the strewn fleeces', the adjective and noun split across the line. The colon leads to the sudden voice."""),
(95, 'est:',
 """sudden from the deep grove a voice given back was:""",
 """suddenly from deep within the grove came a voice in answer:""",
 """'Subita… vox' is 'a sudden voice'; the adjective stands for the adverb, 'suddenly'. 'Ex alto… luco' is 'from the deep grove', 'altus' of depth as well as height. 'Reddita est' is 'was given back', the regular word for an oracle returning an answer. Faunus speaks to his son."""),
(97, 'paratis:',
 """“Do not seek in marriages your daughter to join, Latin ones,
O my offspring, and in the bridal-chambers do not trust, prepared:""",
 """“Do not seek, O my son, to give your daughter in marriage to a Latin, nor put your faith in the wedding that stands ready;""",
 """'Ne pete' is 'ne' with the imperative, an old and poetic form of prohibition, for 'noli petere'. 'Conubiis… sociare Latinis' is 'to unite (her) in marriage with a Latin'; 'conubiis', 'marriages', a poetic plural, frames the line with 'Latinis'. 'Natam' is 'daughter'. 'O mea progenies', 'O my offspring', is Faunus addressing his son. 'Thalamis… paratis' is 'in the marriage-chamber made ready', that is, the match with Turnus already in hand; 'crede' takes the dative, 'trust'. 'Neu' is 'and do not'."""),
(101, 'videbunt.”',
 """foreign will come sons-in-law, who by their blood our
name to the stars shall bear, and from whose stock descendants
all things beneath their feet, where the Sun, at either running back,
looks on the Ocean, both turned and ruled shall see.”""",
 """sons-in-law will come from abroad, who by mingling their blood with ours shall raise our name to the stars, and from whose stock shall spring descendants who will see the whole world, wherever the Sun on his circuit looks upon Ocean in the east and in the west, turning at their command and governed beneath their feet.”""",
 """'Externi… generi' is 'foreign sons-in-law': the plural is general, 'men from abroad', meaning Aeneas. 'Qui… ferant' is a relative clause of purpose or characteristic, with the subjunctive, 'who are to carry'. 'Sanguine' is 'by their blood', by the union of the two races; 'nostrum nomen' is split over the line-end. 'Quorum a stirpe nepotes' is 'descendants from whose stock', the Romans. 'Omnia sub pedibus… vertique regique videbunt' is 'shall see all things turned and ruled beneath their feet', accusative and passive infinitive after 'videbunt', with the double '-que… -que'; 'verti' is 'to be turned', directed as they will. 'Qua Sol utrumque recurrens aspicit Oceanum' is 'wherever the Sun, running his course and back, looks upon both Oceans', the eastern where he rises and the western where he sets: the whole earth. Faunus's speech ends here."""),
(103, 'Latinus,',
 """These answers of father Faunus and warnings in the silent
night given, not himself with his own mouth holds back Latinus,""",
 """These answers of his father Faunus, the warnings given him in the silence of the night, Latinus did not keep locked in his own lips,""",
 """'Haec responsa… monitusque… datos' is the object, 'these answers and warnings given', with 'silenti nocte' 'in the silent night' split across the line. 'Patris Fauni' is 'of his father Faunus'. 'Non… premit ore' is 'does not press (them) in his mouth', 'does not keep them silent'; 'ipse' is 'he himself': Latinus tells others, and the news spreads. 'Premit' is a historic present."""),
(106, 'classem.',
 """but around far and wide flying, already Rumour through the cities
Ausonian had carried them, when the Laomedontian youth
from the grassy bank of the river moored its fleet.""",
 """but Rumour, flying all about and far and wide, had already carried them through the cities of Ausonia by the time the Trojan warriors moored their fleet to the grassy bank of the river.""",
 """'Fama' is Rumour, the swift goddess of hearsay drawn at full length in Book IV (4.173–188), 'volitans', 'flitting about'. 'Circum late' is 'round about and far and wide'. 'Tulerat… cum… religavit' is a pluperfect followed by 'cum' with the perfect indicative, 'cum inversum': 'Rumour had already carried them… when the Trojans moored'. 'Laomedontia pubes' is 'the Laomedontian youth', the Trojans, named from Laomedon, Priam's father and an early king of Troy. 'Religavit' is 'tied up', 'moored'; 'ab aggere' is 'to the bank' (literally 'from', of the place where the rope is fastened, as Latin says 'ab' of the side from which a thing hangs); 'gramineo ripae… aggere' is 'the grassy mound of the riverbank'. The Trojans have now landed at the place where their city is to be."""),
]
P = A.part('aeneid-049'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
