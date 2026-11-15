# aeneid-080 (X.689-790): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Mezentii pugna. Mors Orodis'
PART = "Mezentius in Battle (X.689–790)"
TITLE_EN = "Mezentius in Battle — Aeneid X.689–790"
ABOUT = ("With Turnus carried off the field, Jupiter rouses Mezentius, the exiled Etruscan tyrant who scorns the gods, to take his place. "
"The Etruscans he once ruled hurl themselves at him with all their hatred, and he stands like a sea-cliff under a storm, cutting men down. "
"They dare not close with him, but bay at him from a distance like hunters round a cornered boar, while he falls on them like a starving lion on a deer. "
"He kills the Greek Acron, a bridegroom who never married, and then Orodes, whom he will not strike from behind; dying, Orodes warns him that his own death is near, "
"and Mezentius answers that Jupiter can see to that. The slaughter spreads on both sides while the gods look on in pity, and Mezentius strides "
"across the plain huge as the giant Orion. Aeneas comes against him. Mezentius prays to his own right hand and spear and vows Aeneas's armour to his son Lausus; "
"his spear glances off and kills Antores, a Greek who once followed Hercules, who dies remembering Argos. Aeneas's spear pierces Mezentius's shield and wounds him in the groin, "
"and as Aeneas draws his sword, Lausus sees his father bleeding and weeps. The similes of the rock, the boar and the lion all have models in the Iliad.")

U = [
(690, 'ovantis.',
 """But meanwhile, at Jupiter's promptings, Mezentius, blazing,\nsucceeds to the fight and attacks the Teucrians, exulting.""",
 """Meanwhile, at Jupiter's prompting, Mezentius took up the fight, blazing with fury, and fell upon the triumphant Trojans.""",
 """A new paragraph in Greenough. Turnus has just been swept away to Ardea, and Jupiter sends Mezentius in his place. Mezentius is the Etruscan tyrant whom his own people drove out for his cruelty (VIII.481–495) and Virgil's 'contemptor divum', 'scorner of the gods' (VII.648): now he fights at a god's prompting without knowing it. 'Iovis… monitis', 'at Jupiter's warnings', ablative of cause. 'succedit pugnae', 'comes up to the fight', takes over the place Turnus left; the dative with a compound verb. 'ovantis', accusative plural in '-is', 'rejoicing', the Trojans exulting at Turnus's flight. Elision 'Teucrosqu(e) invadit'."""),
(692, 'instant.',
 """There rush together the Tyrrhenian lines, and with all their hatreds, against one,\none man, and with weapons crowding, they press on.""",
 """The Etruscan ranks charged together, and against one man, one alone, they pressed with all their hatred and a hail of weapons.""",
 """'Tyrrhenae acies', the Etruscan lines, the men of Caere who expelled Mezentius and now fight for Aeneas: this is personal. 'omnibus… odiis… telisque frequentibus', 'with all their hatreds and thick weapons', the ablatives wrapped round 'uni, / uni… viro', 'against one man', dative with 'instant'. The repetition of 'uni' across the line-end, a figure called anadiplosis, makes the whole army against a single man. 'frequentibus', 'crowded, thick'. Elisions 'Tyrrhena(e) acies', 'atqu(e) omnibus', 'un(i) odiisque'."""),
(697, 'fugacem,',
 """He, like a cliff which juts out into the vast sea,\nfacing the fury of the winds and exposed to the deep,\nall the force and threats bears through, of both sky and sea,\nitself unmoved remaining, the offspring of Dolichaon, Hebrus,\nhe lays low on the ground, with him Latagus and Palmus the runaway,""",
 """He, like a crag that runs out into the open sea, meeting the rage of the winds and exposed to the waves, enduring all the violence and menace of sky and sea while it stands unmoved itself, struck Hebrus, Dolichaon's son, to the ground, and with him Latagus and Palmus, who tried to run,""",
 """The rock that stands firm against wind and sea is an Iliad simile (15.618–621, the Greeks holding against Hector), and Virgil used it in Book VII for Latinus resisting his people (VII.586–590). Here it fits one man under the whole Etruscan attack. 'velut', 'just as'; 'quae prodit', 'which juts out'. 'obvia', 'in the way of', with the dative. 'expostaque', the shortened verse form 'expostus' for 'expositus'. 'perfert', 'endures to the end'. 'ipsa immota manens', feminine, still the rock, before the sentence turns back to Mezentius with 'sternit humi', 'lays low on the ground', 'humi' a locative. 'prolem Dolichaonis', 'the offspring of Dolichaon'. The long sentence runs on, so this unit ends at a comma. Elisions 'cunct(am) atque', 'ips(a) immota'."""),
(701, 'cristas.',
 """but Latagus with a stone and a huge fragment of a mountain\nhe catches in the mouth and the face turned towards him; Palmus, his knee-tendon\ncut, rolling helpless he lets lie, and the arms to Lausus\nhe gives, to have on his shoulders and to fix the crest on his head.""",
 """but Latagus he caught full in the mouth and face with a stone, a huge fragment of a mountain, and Palmus he hamstrung and left writhing helpless on the ground, and gave his armour to Lausus to wear on his shoulders and his crest to set upon his head.""",
 """'sed', taking the two men in turn. 'saxo atque ingenti fragmine montis', one weapon named twice, 'a stone, a huge fragment of mountain', hendiadys; heroes in Homer throw boulders no two men of today could lift. 'occupat', 'catches first', strikes before he can act. 'os faciemque adversam', 'mouth and face turned to him'. 'poplite… succiso', ablative absolute, 'his knee-sinew cut'. 'volvi segnem sinit', 'lets him roll, helpless': he does not bother to kill a runaway. 'Lauso', Lausus, Mezentius's son, a young man Virgil has praised (VII.649–654); he will matter at the end of this part. 'donat habere… figere', infinitives of purpose after 'donat', a poetic construction. Elisions 'sax(o) atqu(e) ingenti', 'faciemqu(e) adversam', 'haber(e) umeris'."""),
(705, 'creat:',
 """Nor did he spare Euanthes the Phrygian, and Paris's Mimas,\nhis age-mate and companion, whom in one night Theano\ninto the light for his father Amycus gave, and with a torch pregnant\nthe Cisseian queen brings forth Paris:""",
 """And Euanthes the Phrygian too, and Mimas, Paris's companion and of an age with him, whom Theano bore to his father Amycus on the same night that the daughter of Cisseus, the queen, pregnant with a firebrand, gave birth to Paris:""",
 """'Nec non', 'and not not', so 'and also', with 'sternit' understood from 697. 'Paridis… Mimanta / aequalem comitemque', 'Mimas, Paris's age-mate and companion'. 'una… nocte', 'on one (and the same) night'. 'in lucem… dedit', 'gave into the light', bore. This Theano, wife of Amycus, is perhaps not Homer's Theano, Antenor's wife. 'Cisseis regina', Hecuba: Virgil makes her daughter of Cisseus, as Euripides does; Homer makes her daughter of Dymas (Iliad 16.718, perhaps). Before Paris was born she dreamed she was carrying a firebrand ('face praegnans'), a sign that he would burn Troy. 'Parin', Greek accusative. 'creat', a vivid present beside 'dedit'. Elisions 'comitemqu(e) una', 'genitor(i) Amyco'."""),
(706, 'Mimanta.',
 """in his father's city\nhe lies; the unknowing one the Laurentine shore holds, Mimas.""",
 """Paris lies in the city of his fathers; Mimas, a stranger to it, lies on the Laurentine shore.""",
 """The two boys born on one night end far apart. 'urbe paterna / occubat', 'lies (dead) in his ancestral city': the subject is Paris, from the line before, buried at Troy. The Latin Library prints 'Parim; Paris urbe paterna', naming Paris again as subject of 'occubat'; the sense is the same, but Greenough's 'creat' leaves the subject to be supplied. 'ignarum… Mimanta', 'Mimas, not knowing (it)', a stranger to the land he dies in; the adjective and the name frame the line. 'Laurens… ora', 'the Laurentine coast', near Latinus's city. No elisions."""),
(711, 'armos,',
 """And as that boar, by the bite of the dogs from the high mountains\ndriven, whom Vesulus the pine-bearing for many years\nhas sheltered, or for many the Laurentine marsh, in the forest\nfed on reeds, after it has come among the nets,\nhas stopped, and snorted, fierce, and bristled his shoulders,""",
 """And as the boar driven by the dogs' teeth down from the high mountains, the boar that pine-clad Vesulus has sheltered many years, or the Laurentine marsh, feeding in the forest of reeds, once he is caught among the nets, stops short, snorts in his fury and bristles his shoulders,""",
 """A hunting simile: a boar at bay among nets and hunters, which recalls Iliad 11.414–420, Odysseus surrounded like a boar by hounds and young men (the lines perhaps). 'ille… aper', 'that boar', the familiar one of hunting stories. 'Vesulus', Monte Viso in the Alps, where the Po rises. 'multosve', 'or many (years)'. 'silva… harundinea', 'in a reed forest', the marsh. 'pastus', 'having grazed', from the deponent 'pascor'; the Latin Library prints 'pascit', 'the marsh feeds him', a different construction with the same picture. 'ventum est', impersonal passive, 'it has been come', he has come. 'armos', 'shoulders', accusative of respect. The sentence runs on, so this unit ends at a comma. Elisions 'postqu(am) inter', 'ventum (e)st'."""),
(718, 'hastas.',
 """and no one has the courage to rage and nearer to approach,\nbut with javelins and with safe, from afar, shouts they press him;\nhe however, unafraid, delays towards all sides,\nwith his teeth gnashing, and from his back shakes off the spears;""",
 """and no man has the courage to vent his anger on him and come closer, but they harry him with javelins and with shouts from a safe distance, while he, unafraid, holds off, turning to face every side, gnashes his teeth, and shakes the spears from his back;""",
 """The print has a full stop after 'hastas', with 'haud' following in lower case, a misprint for a lighter stop, corrected here: the simile runs on into 'haud aliter'. Greenough prints 717–718 ('ille autem… hastas') here, between 713 and 714, keeping the boar inside the simile; most editions put them after 716. This edition keeps his order. 'nec cuiquam… virtus', 'nor is there courage to anyone', dative of possession. 'irasci propiusque accedere', infinitives with 'virtus', 'courage to rage and come nearer'. 'tutis… procul clamoribus', 'safe shouts from afar'. 'partis… in omnis', accusative plural in '-is', 'towards all sides'. Elisions 'cuiqu(am) irasci', 'propiusqu(e) accedere', 'ill(e) aut(em) impavidus'."""),
(716, 'lacessunt:',
 """not otherwise, those to whom there is Mezentius for just anger,\nnot one has the heart with drawn steel to close;\nwith missiles from afar and with vast shouting they provoke him:""",
 """just so, of all those who had just cause to hate Mezentius, not one had the heart to close with him sword in hand; they goaded him from a distance with missiles and with a great clamour:""",
 """'haud aliter', 'not otherwise', the regular way of turning from a simile to the thing it describes. 'iustae quibus est Mezentius irae', 'to whom Mezentius is for just anger', the double dative: 'quibus', of the persons, and 'irae', of purpose, 'an object of just anger'; the relative clause comes before its antecedent, the 'ulli' of the next line. 'non ulli est animus', 'there is not to anyone the heart', dative of possession again. 'stricto… ferro', 'with drawn steel'. The colon leads into the story of Acron as an example. Elisions 'ulli (e)st', 'long(e) et'."""),
(720, 'hymenaeos.',
 """There had come from the ancient lands of Corythus Acron,\na Greek man, his unfinished wedding leaving, a fugitive.""",
 """There had come from the ancient lands of Corythus a man named Acron, a Greek, an exile who had left his wedding unfinished.""",
 """'Corythi de finibus', 'from the territory of Corythus', an Etruscan town, traditionally Cortona, named after its founder Corythus (see III.170). 'Graius homo', 'a Greek man', one of several Greeks in Italy in this book. 'infectos… hymenaeos', 'the unfinished wedding', the marriage not yet completed; 'hymenaeus' is the wedding song and so the wedding. 'profugus', 'an exile', with no reason given. The pathos of the bridegroom who dies is an Iliad pattern: Iphidamas in Iliad 11.221–247 left his bride after the wedding (the lines perhaps). Elision 'hom(o) infectos'."""),
(722, 'ostro:',
 """Him when, throwing into confusion from afar the middle ranks, he saw,\ncrimson with plumes and with the purple of his promised wife:""",
 """When Mezentius saw him far off, spreading havoc through the middle of the lines, scarlet with his plumes and with the purple his betrothed had given him,""",
 """'Hunc', Acron, the object of 'vidit'; the subject is Mezentius, whose main verb does not come until 'ruit' in 729, after the simile. 'miscentem… media agmina', 'throwing the middle ranks into confusion'. 'longe', 'far off', with 'vidit'. 'purpureum', 'crimson', with two ablatives: 'pennis', the plumes of his crest, and 'pactae coniugis ostro', 'with the purple of the promised wife', a cloak she dyed or wove for him. 'ostrum', the purple dye of the murex shellfish. Elision 'medi(a) agmina'."""),
(725, 'cervum,',
 """an unfed lion, as often through the deep lairs ranging\n(for mad hunger urges him), if by chance a fleeing\nhas spied she-goat, or rising to his horns a stag,""",
 """as a hungry lion, prowling as he often does through deep cattle-folds (for mad hunger drives him), if by chance he catches sight of a timid goat or a stag lifting its antlers,""",
 """A lion simile, modelled on Iliad 3.23–28, where Menelaus sees Paris and rejoices like a hungry lion that finds a stag or wild goat. 'impastus', 'unfed'. 'ceu', 'as', an old word of comparison, put late. 'stabula alta', 'deep stalls', the folds where cattle are penned. 'suadet enim vesana fames', a parenthesis. 'si forte… conspexit', 'if by chance he has spied', the perfect used of what happens again and again. 'fugacem… capream', 'a quick-to-run roe' (strictly a wild she-goat or roe deer), the adjective at the line-end. 'surgentem in cornua', 'rising into horns', the stag's antlers rearing up. The sentence runs on. Elisions 'stabul(a) alta', 'capre(am) aut', 'surgent(em) in'."""),
(729, 'hostis.',
 """he rejoices, gaping hugely, and his mane has raised, and he clings\nto the entrails, crouching over them; there bathes his cruel, foul,\njaws the gore,\nso rushes among the thick enemies, eager, Mezentius.""",
 """he rejoices, gaping monstrously, raises his mane, and fastens on the entrails, crouching over them, while the foul blood washes his ruthless jaws: just so Mezentius rushed eagerly into the thick of the enemy.""",
 """'hians immane', 'gaping hugely', 'immane' a neuter adjective used as an adverb. 'arrexit', a perfect like 'conspexit', of habit. 'super accumbens', 'lying over it'; the Latin Library has 'incumbens', 'leaning on it', much the same. 'lavit', 'washes', from the older 'lavo, lavere' of the third conjugation. 'inproba… ora', 'the shameless mouth', the adjective and noun split; 'taeter… cruor', 'foul gore'. 'ora cruor,' is a half-line, one of the lines Virgil left unfinished when he died; after it the grammar does not close the simile but jumps to 'sic ruit', which picks up 'Hunc ubi… vidit' of 722. 'hostis', accusative plural in '-is'. Elision 'comasqu(e) arrexit'."""),
(731, 'cruentat.',
 """Laid low is unhappy Acron, and with his heels the black\nearth he beats, breathing out his life, and the broken weapons he bloodies.""",
 """Down went the unhappy Acron, beating the dark earth with his heels as he breathed his last, and staining the broken spears with his blood.""",
 """'Sternitur', 'is laid low', the passive put first as the result of the charge. 'infelix', 'unfortunate', a word Virgil uses of those whose death he pities; he will say the same of Antores at 781. 'calcibus… tundit humum', 'beats the ground with his heels', the death-throes. 'atram… humum', the adjective at the end of one line and the noun in the next. 'expirans', Greenough's spelling here of 'exspirans' (he prints 'exspirans' at 739). 'infracta… tela', 'the broken spears', those broken in him or around him. Elision 'hum(um) expirans'."""),
(733, 'volnus:',
 """And he likewise Orodes, as he fled, did not deign\nto lay low, nor with a thrown spear-point to give a blind wound:""",
 """And Orodes too, as he fled, Mezentius did not deign to strike down or to wound unseen with a thrown spear:""",
 """'idem', 'the same man', Mezentius, now shown at his best. 'haud est dignatus', 'he did not think it worthy', the deponent 'dignor' with an infinitive. 'fugientem… Oroden', 'Orodes fleeing', the Greek accusative in '-en'. 'iacta… cuspide', 'with a thrown point', ablative of means. 'caecum… volnus', 'a blind wound', one struck from behind, where the victim cannot see it coming. 'volnus', Greenough's spelling of 'vulnus'. Elisions 'Atqu(e) idem', 'fugient(em) haud'."""),
(735, 'armis.',
 """facing him, he runs to meet him, and himself to the man, man,\nhe brought together, not by stealth the better, but by brave arms.""",
 """he ran round to meet him face to face and closed with him man to man, proving himself the better not by a trick but by strength of arms.""",
 """'obvius adversoque', 'in the way and facing him', the same idea twice: he runs round in front of Orodes to fight him from the front. 'seque viro vir / contulit', 'and brought himself, a man to a man', the two forms of 'vir' set side by side for single combat. 'haud furto melior', 'better not by stealth', 'furtum', 'theft', so any underhand trick; 'fortibus armis', ablative of means, 'by brave arms'. Even the tyrant has a code. Elision 'adversoqu(e) occurrit'."""),
(737, 'Orodes.”',
 """Then over the fallen man, with foot planted, leaning on his spear too:\n“A part of the war not to be scorned, men, lies here: tall Orodes.”""",
 """Then, setting his foot on the fallen man and leaning on his spear, he said: “There lies tall Orodes, my men, no small part of this war.”""",
 """'super abiectum', 'over the man thrown down'. 'posito pede', ablative absolute, 'foot set', on the body, as a warrior plants his foot to draw out his spear (compare Patroclus at Iliad 16.503, perhaps). 'nixus et hasta', 'and leaning on his spear', the 'et' placed late. The verb of speaking is left out. 'Pars belli haud temnenda', 'a part of the war not to be despised', the gerundive of 'temno': Mezentius praises his victim, to praise himself. 'altus', 'tall'. Elision 'bell(i) haud'."""),
(738, 'secuti.',
 """His comrades shout together, a joyful paean taking up.""",
 """His comrades raised a shout, taking up a joyful song of victory.""",
 """'Conclamant', 'they shout all together'. 'paeana', Greek accusative singular of 'paean', a song of triumph, originally a hymn to Apollo the Healer; Achilles' men sing one after Hector falls (Iliad 22.391–394, perhaps). 'secuti', 'following', taking up their leader's boast. No elisions."""),
(741, 'tenebis.”',
 """He, however, breathing out his life: “Not with me, whoever you are, unavenged,\nvictor, nor for long will you rejoice: you too fates\nlook out for, equal ones, and the same fields soon you will hold.”""",
 """But he, breathing his last, answered: “Whoever you are, conqueror, I shall not go unavenged, and you will not exult for long: a like fate is watching for you too, and soon you will lie in these same fields.”""",
 """The dying man's prophecy is Homeric: Patroclus warns Hector (Iliad 16.851–854), and Hector warns Achilles (22.358–360). 'Non me… inulto', ablative absolute, 'with me not avenged'; 'nec longum laetabere', 'nor will you rejoice for long', 'longum' adverbial, 'laetabere' the second-person future in '-re'. 'quicumque es', 'whoever you are': he does not know who has killed him. 'fata… paria', 'equal fates', the adjective held over. 'prospectant', 'look out for, await'. 'eadem… arva', 'the same fields', this battlefield, where Mezentius will die in this book. Elisions 'Ill(e) aut(em) exspirans', 'quicumqu(e) es', 'pari(a) atqu(e) eadem'."""),
(744, 'viderit.',
 """At which, smiling, with anger mixed, Mezentius:\n“Now die. But of me the father of gods and king of men\nwill see.”""",
 """At this Mezentius smiled, but with anger in his smile: “Die now. As for me, the father of gods and king of men will see to that.”""",
 """'Ad quae', 'at which (words)', a connecting relative; the Latin Library has 'ad quem', 'to whom', a little different but the same scene. The verb of speaking is again left out. 'subridens mixta… ira', 'smiling, with anger mixed in', ablative absolute. 'Ast', an old and poetic form of 'at', 'but'. 'divom', old genitive plural. 'de me… viderit', 'about me let him see', the perfect subjunctive used as a jussive, 'let him look to it': the formula 'divom pater atque hominum rex' is Homer's 'father of men and gods'. Mezentius echoes Achilles' reply to the dying Hector (Iliad 22.365–366), but with a sneer. On the closing speech mark, see the next unit. Elisions 'morer(e) ast', 'atqu(e) hominum'."""),
(746, 'noctem.',
 """Saying this, he drew the spear out of the body:\non him a hard rest weighs, on his eyes, and an iron\nsleep; into eternal night his eyes are closed.""",
 """With these words he drew the spear from the body. Hard rest and iron sleep pressed down upon his eyes, and their light closed in everlasting night.""",
 """The print has 'viderit. ”Hoc', with the closing speech mark joined to the next word, a misprint for 'viderit.” Hoc', corrected here: the speech ends with 'viderit'. 'Hoc dicens', 'saying this'. 'eduxit corpore telum', 'drew the spear from the body', 'corpore' ablative of separation. 'olli', old form of 'illi', dative, 'on him', Orodes. 'dura quies… ferreus… somnus', 'hard rest and iron sleep', death; Homer has 'bronze sleep' for a warrior's death (Iliad 11.241, perhaps). 'lumina', 'lights', his eyes. Virgil uses these two lines again in XII.309–310. No elisions."""),
(751, 'peditem.',
 """Caedicus Alcathous cuts down, Sacrator Hydaspes,\nand Parthenius Rapo, and, very hard in his strength, Orses,\nMessapus Cronius and Lycaonian Erichaetes,\nthe one, from the fall of his unbridled horse, lying on the ground,\nthe other on foot.""",
 """Caedicus cut down Alcathous, Sacrator Hydaspes, Rapo cut down Parthenius and Orses, a man of iron strength, and Messapus Cronius and Erichaetes, son of Lycaon, the one lying on the ground, thrown when his unbridled horse stumbled, the other on foot.""",
 """A new paragraph in Greenough: the battle widens into a catalogue of killings, in the manner of the Iliad. One verb, 'obtruncat', 'cuts down', serves for all four killers, each with his victims in the accusative. 'praedurum viribus', 'very hard in strength'. 'Lycaonium', 'son of Lycaon', an adjective of descent. 'illum… hunc', 'the former… the latter', Cronius and Erichaetes. 'infrenis equi lapsu', 'by the fall of his bridle-less horse', a horse ridden without a bridle, as the Numidians rode (IV.41). Messapus fights for Turnus; most of the others are named only here. Elisions 'Alcatho(um) obtruncat', 'Rap(o) et', 'Lycaoniumqu(e) Erichaeten', 'ill(um) infrenis'."""),
(753, 'deicit;',
 """On foot also the Lycian had come forward, Agis,\nwhom, however, not lacking in the courage of his forefathers, Valerus\nthrows down;""",
 """On foot too the Lycian Agis had come forward, but Valerus, who did not lack his forefathers' courage, threw him down;""",
 """'Pedes', 'on foot', picking up 'peditem' just before. 'Lycius… Agis', from Lycia in Asia Minor, a Trojan ally as in the Iliad. 'quem… deicit', 'whom… throws down', the relative clause carrying the main action. 'haud expers… virtutis avitae', 'not without a share in his grandfathers' courage', 'expers' with the genitive. 'Valerus' has a Roman sound: the Valerii were a great Roman family, and Virgil may be giving them an ancestor. No elisions."""),
(754, 'sagitta.',
 """but Thronius Salius, and Salius Nealces\nby ambush, with a javelin and an arrow deceiving from afar.""",
 """and Salius killed Thronius, and Nealces Salius, by stealth, with a javelin and an arrow that struck unseen from far away.""",
 """The verb is again understood, 'deicit' from the line before. 'Salius', killer and then killed, the name repeated in chiasmus, 'Thronium Salius Saliumque Nealces'. 'insidiis', 'by ambush', explained by what follows: perhaps 'iaculo' goes with Salius's kill and 'longe fallente sagitta', 'with an arrow deceiving from afar', with Nealces', the arrow from an unseen archer being the ambush. 'fallente', 'escaping notice', the root sense of 'fallo'. Elision 'iacul(o) et'."""),
(757, 'illis.',
 """Now heavy grief was Mavors making equal, and mutual\ndeaths: they were cutting down alike and alike falling,\nvictors and vanquished, nor to these was flight known, nor to those.""",
 """And now Mars was dealing out heavy grief and mutual slaughter in equal measure: victors and vanquished alike were killing and alike were falling, and neither side knew what it was to run.""",
 """A new paragraph in Greenough. 'aequabat', 'was making equal', with two objects, 'luctus' (accusative plural) and 'mutua… funera', 'mutual deaths', split across the line-end. 'Mavors', the old, poetic name of Mars. 'caedebant pariter pariterque ruebant', 'they cut down alike and alike fell', the repeated 'pariter' in chiasmus; 'victores victique', both at once, the same men winning and losing. 'neque his… neque illis', 'neither to these… nor to those', datives of possession. Elisions 'nequ(e) his', 'nequ(e) illis'."""),
(761, 'saevit.',
 """The gods in Jupiter's halls pity the anger, the vain,\nof both, and that such great toils for mortals should be:\nhere Venus, there opposite watches Saturnian Juno;\npale Tisiphone in the midst of the thousands rages.""",
 """In Jupiter's halls the gods pitied the useless anger of both sides and the thought that mortals should suffer such toil: on this side Venus watched, on that, facing her, Juno, Saturn's daughter, while pale Tisiphone raged among the thousands.""",
 """'Iovis in tectis', 'in Jupiter's house'. 'iram… inanem / amborum', 'the empty anger of both', fruitless because fate has settled the end; the adjective held over the line-end. 'tantos… esse labores', accusative and infinitive after 'miserantur', 'that there are such great toils for mortals'. 'hinc… hinc contra', 'on this side… on that, opposite', the two goddesses watching their own sides. 'Saturnia', Saturn's daughter, Juno. 'Tisiphone', one of the three Furies, here the spirit of slaughter itself, as Strife rages in the Iliad. Elisions 'ambor(um) et', 'medi(a) inter'."""),
(763, 'campo.',
 """But truly, a huge spear shaking, Mezentius\nwild strides onto the field.""",
 """But Mezentius, shaking his enormous spear, strode wildly out over the plain.""",
 """'At vero', 'but indeed', bringing the camera back to Mezentius. 'ingentem… hastam', the adjective and noun framing the line. 'quatiens', 'shaking, brandishing'. 'turbidus', 'stormy, wild', the man as a storm. 'ingreditur', 'strides on', a verb of stately advance. 'campo', 'on the plain', a local ablative without a preposition. Elision 'ver(o) ingentem'."""),
(767, 'condit:',
 """As great as Orion,\nwhen on foot he walks through the greatest of mid Nereus's\npools, cutting a way, with his shoulder he towers above the waves,\nor from the mountain-tops bringing back an aged ash\nboth walks on the ground and hides his head among the clouds:""",
 """He was as huge as Orion when he strides on foot through the vast pools of the midmost sea, cleaving his way, his shoulders rising clear of the waves, or when, carrying home an ancient ash-tree from the mountain heights, he walks upon the ground and hides his head among the clouds:""",
 """'Quam magnus Orion… talis', 'as great as Orion… such', the two halves of the comparison. Orion was the giant hunter of myth, son of Neptune, who gave him, the story ran, the power to walk through the sea; in the Odyssey he still hunts in the underworld (11.572–575, perhaps). 'pedes', 'on foot', wading. 'medii… Nerei', 'of mid Nereus', the old sea-god standing for the sea; 'Nerei', a Greek genitive in two syllables. 'maxima… stagna', 'the greatest pools', the deep sea. 'umero', 'with his shoulder'. 'annosam… ornum', 'an aged mountain-ash'. 'ingrediturque solo et caput inter nubila condit' is the same line as IV.177, of Rumour, and recalls Strife in Iliad 4.443. Elision 'sol(o) et'."""),
(768, 'armis.',
 """such, himself, with vast arms, Mezentius carries forward.""",
 """so huge was Mezentius as he advanced in his massive armour.""",
 """'talis', 'such', completing 'Quam magnus'. 'se… infert', 'carries himself forward', advances. 'vastis… armis', 'with vast arms', ablative of manner; the adjective and noun frame the verb and the name. His name falls in the same place at the close of both the lion simile (729) and this one, keeping him at the centre of the battle. No elisions."""),
(770, 'parat.',
 """Against him Aeneas, having spied him in the long line,\nprepares to go to meet him.""",
 """Aeneas, catching sight of him along the far-stretching line, made ready to go out against him.""",
 """A new paragraph in Greenough: the duel begins. 'Huic contra', 'against him', 'huic' a dative with 'obvius', 'in his way'. 'speculatus', 'having spied out', a deponent participle in active sense. 'in agmine longo', 'in the long line', along the battle front. 'obvius ire', 'to go in his path', to meet him. Aeneas had been looking for Turnus on the field; he finds Mezentius instead. Elision 'contr(a) Aeneas'."""),
(771, 'stat;',
 """Remains unterrified he,\nthe enemy, great-hearted, awaiting, and with his own bulk stands;""",
 """Mezentius stood his ground, unterrified, waiting for his great-hearted enemy, and stood firm in all his massive bulk;""",
 """'Manet', 'stays', put first. 'imperterritus', 'utterly unafraid', a long compound filling the space before the line-end. 'hostem magnanimum', 'the great-hearted enemy', Aeneas; Mezentius is generous in calling him so. 'opperiens', 'waiting for'. 'mole sua stat', 'stands by his own bulk', fixed like the rock of 693. 'stat', a monosyllable at the line-end, gives a heavy close. Elision 'magnanim(um) opperiens'."""),
(776, 'Aeneae.',
 """and with his eyes the distance having measured, as much as enough for a spear:\n“My right hand, my god, and the weapon which, to be hurled, I poise,\nnow be present! I vow, from the pirate's body torn,\nclad in his spoils, you yourself, Lausus, a trophy\nover Aeneas.”""",
 """Measuring with his eye the distance a spear could carry, he said: “My right hand, which is my god, and the weapon I poise to throw, be with me now! I vow that you yourself, Lausus, dressed in the spoils stripped from that pirate's body, shall be my trophy over Aeneas.”""",
 """'oculis spatium emensus', 'having measured the space with his eyes', the deponent 'emetior'. 'quantum satis hastae', 'as much as (is) enough for a spear'. The verb of speaking is left out. 'Dextra mihi deus', 'my right hand (is) my god': the scorner of gods prays to his own hand and spear, 'adsint', 'may they be present', the word used in prayers to gods. 'libro', 'I poise, balance'. 'Voveo… te… tropaeum', 'I vow you as a trophy', the language of a vow to a god; a trophy was a post dressed in captured armour, and Lausus himself, in Aeneas's armour, will be one. 'praedonis', 'the robber's', Aeneas, the foreign raider. 'Aeneae', genitive, 'of (victory over) Aeneas'. On the closing speech mark, see the next unit. Elisions 'atqu(e) oculis', 'spati(um) emensus'."""),
(777, 'iecit;',
 """He spoke, and the hissing from far off spear\nhe threw;""",
 """With that he hurled his whistling spear from far off;""",
 """The print has 'Aeneae. ”Dixit', with the closing speech mark joined to the next word, a misprint for 'Aeneae.” Dixit', corrected here: the speech ends with 'Aeneae'. 'Dixit', 'he spoke', the speech closed with a single word. 'stridentem… hastam', 'the hissing spear', framing 'eminus', 'from a distance'. 'iecit', 'threw', held over the line-end and stopped hard by the semicolon. Elision 'stridentemqu(e) eminus'."""),
(780, 'urbe.',
 """but it, flying, from the shield was struck away, and far off\nnoble Antores between side and groin it pierces,\nHercules's companion Antores, who, sent from Argos,\nhad attached himself to Evander and in an Italian city had settled.""",
 """but in its flight it glanced off the shield and, some way off, struck the noble Antores between the side and the groin: Antores, once the companion of Hercules, who had come from Argos, attached himself to Evander and settled in an Italian city.""",
 """'illa', the spear. 'clipeo est excussa', 'was struck off from the shield', ablative of separation: it glances off Aeneas's shield. 'procul', 'at a distance'. 'latus inter et ilia', 'between the side and the groin', the preposition between its two nouns. 'figit', 'pierces', a vivid present. 'Antoren', Greek accusative, the name repeated, a figure that brings a victim close. Hercules had come to Evander's settlement on the site of Rome and killed Cacus (VIII.185–275); Antores, from Argos, stayed behind. 'Itala… urbe', Pallanteum, Evander's town. Elisions 'clipeo (e)st', 'egregi(um) Antoren', 'Euandr(o) atqu(e) Itala'."""),
(782, 'Argos;',
 """Laid low is the unhappy man by a wound meant for another, and the sky\nhe looks at, and, dying, his sweet Argos remembers;""",
 """The unhappy man fell, by a wound meant for another, and looked up at the sky, and as he died remembered his sweet Argos.""",
 """One of the most quoted lines in the poem. 'Sternitur infelix', the same opening as Acron's death at 730. 'alieno volnere', 'by another's wound', the blow intended for Aeneas. 781 is a hypermetric line, with a syllable too many: the '-que' of 'caelumque' is elided into 'aspicit' at the start of 782. 'dulcis… Argos', accusative plural, from the plural form 'Argi', 'Argos' (so 'ab Argis' at 779), with 'dulcis' the '-is' accusative plural; 'reminiscor' takes the accusative here. 'caelum aspicit', the dying man's look upward. Elision 'caelumqu(e) aspicit', across the line-end."""),
(786, 'pertulit.',
 """Then dutiful Aeneas throws his spear: it through the round,\nhollow with triple bronze, through the linen layers and through three\nbulls' woven work passes, and low it settled\nin the groin, but its force did not carry through.""",
 """Then dutiful Aeneas threw his spear: it passed through the hollow round of the shield with its three layers of bronze, through the layers of linen and the work woven of three bulls' hides, and lodged low in the groin, but its force was spent.""",
 """'pius Aeneas', his standing epithet, set against the scorner of the gods. 'per orbem / aere cavum triplici', 'through the round, hollow with triple bronze', Mezentius's shield. 'linea terga', 'linen backs', layers of linen. 'tribus… tauris intextum opus', 'the work woven with three bulls', layers of three ox-hides, the adjective and noun split. 'transit', perhaps the contracted perfect of 'transeo' for 'transiit' (the Latin Library's reading), or a present. 'ima… sedit / inguine', 'settled low in the groin'. 'viris', accusative plural, 'vires', 'its strength': it did not carry its full force through. Homer's spears pierce shields layer by layer in the same way (Iliad 7.245–248, perhaps). No elisions."""),
(788, 'instat.',
 """Swiftly his sword\nAeneas, at the sight of the Tyrrhenian's blood glad,\nsnatches from his thigh, and on the trembling man, hot, presses.""",
 """Quickly Aeneas, glad to see the Etruscan's blood, snatched his sword from his thigh and pressed hard on his shaken foe.""",
 """'Ocius', 'more swiftly', the comparative used for 'very swiftly', 'at once'. 'viso Tyrrheni sanguine', ablative absolute, 'the Etruscan's blood having been seen'. 'laetus', 'glad': Aeneas is not always gentle in this book. 'eripit a femine', 'snatches from the thigh', drawing his sword from where it hung at his side; 'femine' is from 'femur', which has a second stem 'femin-'. 'trepidanti', dative with 'instat', 'presses on the man in alarm'. 'fervidus', 'hot, ardent', an adjective doing the work of an adverb. Elision 'femin(e) et'."""),
(790, 'volutae.',
 """He groaned deeply, for love of his dear father,\nwhen he saw, Lausus, and tears over his face rolled.""",
 """Lausus groaned deeply for love of his dear father when he saw it, and the tears rolled down his face.""",
 """'Ingemuit', 'he groaned', put first; the subject, 'Lausus', is held back until the next line, so the reader feels the groan before knowing whose it is. 'cari… genitoris amore', 'from love of his dear father', ablative of cause, with 'genitor' the poetic word for father. 'ut vidit', 'when he saw', 'ut' temporal with the indicative. 'volutae', with 'sunt' understood, 'rolled'. Lausus, the son Mezentius vowed to dress in Aeneas's armour, is about to step in to save him. No elisions."""),
]

PAIRS = {742: 744, 772: 776}
P = A.part('aeneid-080'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units')
