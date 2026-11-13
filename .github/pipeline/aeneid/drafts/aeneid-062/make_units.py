# aeneid-062 (VIII.520-607): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Arma in nubibus. Profectio Pallantis'
PART = "The Sign in the Sky and the Departure of Pallas (VIII.520–607)"
TITLE_EN = "The Sign in the Sky and the Departure of Pallas — Aeneid VIII.520–607"
ABOUT = ("Evander has just offered Aeneas the command of the Etruscan army and his own son Pallas as his companion, and "
"Aeneas and his friend Achates sit with their eyes on the ground, turning over the hard road ahead, when Venus sends a sign "
"out of a clear sky: a flash of lightning, a crash as if the world were falling, the blare of an Etruscan trumpet, and, "
"high in the cloudless air, armour glowing red and clashing like thunder. The others are dumbfounded; Aeneas knows the sound. "
"His mother promised to send this sign if war broke out, and to bring him arms made by Vulcan through the air. He tells "
"Evander not to ask what it means: heaven is calling him, and he foresees the slaughter of the Latins and the shields, "
"helmets and bodies the Tiber will roll down to the sea. He rekindles the altar fires of the day before and sacrifices with "
"Evander, then goes back to his ships, picks the best of his men to ride with him, and sends the rest downstream to take "
"the news to his son Ascanius. Horses are given to the Trojans who are bound for Etruria, and a special one for Aeneas, "
"covered in a lion's skin with gilded claws. As word spreads through the little town, the mothers pray twice as hard. "
"Evander clings to his son's hand and weeps. If only he were young again, he says, as he was when he killed King Erulus, "
"who had three lives and had to be killed three times; then he would not be parted from his son, and Mezentius would never "
"have done so much killing on his border. He prays to Jupiter that he may live to see Pallas come home, and, if some "
"disaster is coming, that he may die now, while hope is still possible and the boy is still in his arms; and he collapses "
"and is carried indoors by his servants. The horsemen ride out through the open gates, Aeneas and Achates at their head "
"and Pallas in the middle of the column, shining like the morning star rising out of the Ocean, while the mothers watch "
"from the walls as the dust cloud and the flashing bronze move off. They take the shortest way through the scrub to an "
"ancient grove near the river of Caere, sacred to Silvanus, where Tarchon and the Etruscans are camped, and there they rest "
"their horses and themselves.")

U = [
(523, 'aperto.',
 "Scarcely those things had he spoken, and fixed their faces they kept,\nAeneas son of Anchises and faithful Achates,\nand many hard things with their own sad heart were pondering,\nhad not a sign from the sky Cytherea given, open.",
 "Hardly had he finished speaking, and Aeneas, son of Anchises, and faithful Achates sat with their eyes fixed on the ground, turning over many hard things in their troubled hearts, and would have gone on doing so, had not the goddess of Cythera given a sign out of the open sky.",
 """A new paragraph in Greenough. 'Vix ea fatus erat', 'scarcely had he said these things', the deponent 'for'. 'defixi ora tenebant', 'they kept their faces fixed', downcast, the participle predicative. 'Anchisiades', 'son of Anchises', a Greek patronymic. 'putabant', 'were thinking over', the old sense of 'puto', 'reckon'. 'ni… dedisset', 'had not… given': the 'ni' clause hangs on an unstated 'and they would have gone on', an epic way of saying that something broke in on a scene; the imperfect indicative before it is the action interrupted. 'Cytherea', Venus, from Cythera, the island where she came ashore from the sea. 'caelo… aperto', 'from the open sky', framing the line: thunder out of a clear sky was a portent. Elision 'defixiqu(e) ora'."""),
(526, 'clangor.',
 "For unforeseen, hurled from the upper air, a flash\nwith a sound came, and to crash down all things seemed suddenly,\nand a Tyrrhenian of the trumpet to bellow through the air blare.",
 "For without warning a flash of lightning darted from the heavens with a roar, everything seemed suddenly to be falling in ruin, and the blare of an Etruscan trumpet bellowed through the sky.",
 """'Namque', 'for', explaining the sign. 'inproviso', 'unexpectedly', adverb (Greenough's spelling of 'improviso', the prefix not assimilated). 'vibratus ab aethere fulgor', 'a flash hurled from the upper air'. 'visa (sunt)', 'seemed', with two infinitives: 'ruere omnia', 'that everything was crashing down', and 'mugire… clangor', 'that a blare was bellowing'. 'Tyrrhenus… tubae… clangor', 'the Tyrrhenian clangour of a trumpet', framing the line: the Etruscans were credited with inventing the war trumpet, and the sign fits the Etruscan war ahead. 'mugire', 'to low, bellow', of cattle. 'aethera', Greek accusative of 'aether'. Elisions 'Namqu(e) inproviso', 'ruer(e) omnia'."""),
(529, 'tonare.',
 "They look up; again and again a crash resounds huge:\narms among a cloud, in a region of the sky serene,\nthrough the clear air to glow red they see, and struck to thunder.",
 "They look up, and again and again a huge crash rings out: in a calm quarter of the sky, inside a cloud, they see armour glowing red through the clear air and thundering as it clashes.",
 """'Suspiciunt', 'they look up', 'sub' + 'specio'. 'iterum atque iterum', 'again and again'. 'increpat', 'rattles', 'crashes'. The colon opens what they see. 'arma… vident… rutilare… et… tonare', 'they see arms glow red and thunder', accusative and infinitive after a verb of seeing. 'inter nubem', 'within a cloud', the cloud that carries the gods' gifts. 'caeli regione serena', 'in a serene region of the sky', ablative of place. 'per sudum', 'through the clear sky', 'sudum' a neuter adjective used as a noun, 'fair weather'. 'pulsa', 'struck', the pieces of armour clashing against each other. Elisions 'iter(um) atque', 'atqu(e) iterum', 'arm(a) inter'."""),
(531, 'parentis.',
 "Were astounded in their minds the others, but the Trojan hero\nrecognised the sound and of his divine mother the promises.",
 "The others were struck dumb with amazement, but the Trojan hero knew the sound, and recognised the promise his goddess mother had made.",
 """'Obstipuere' = 'obstipuerunt', 'they were dumbfounded', the '-ere' perfect (as always). 'animis', 'in their minds', ablative of respect. 'Troius heros', Aeneas. 'agnovit… promissa', 'recognised the promises': he hears the sound and sees in it what was promised. The promise has not been shown in the poem: we learn of it only here, from what Aeneas says next. 'divae… parentis', 'of his goddess mother', framing 'promissa'. Elisions 'Obstipuer(e) animis', 'sonit(um) et'."""),
(533, 'Olympo.',
 "Then he speaks: “No, truly, my host, do not indeed ask\nwhat outcome the portents bring: I am summoned by Olympus.",
 "Then he spoke: “No, my host, do not ask, I beg you, what these portents mean for the future: it is I who am called for by heaven.",
 """Aeneas's speech opens. 'memorat', 'he speaks', 'recounts'. 'Ne… ne quaere', 'do not ask', 'ne' with the imperative, a poetic form of prohibition (prose uses 'noli quaerere'); the repeated 'ne' and 'vero… profecto', 'truly… indeed', make it urgent. 'hospes', 'host', Evander; the word means both host and guest. 'quem casum portenta ferant', 'what event the portents bring', indirect question, subjunctive. 'ego poscor Olympo', 'I am demanded by Olympus', 'Olympo' ablative (or dative) of the source of the summons: the sign is for him. Elision 'ver(o) hospes'."""),
(536, 'auxilio.',
 "This sign foretold she would send, the goddess my mother,\nif war should break out, and Vulcanian arms through the airs\nwould bring for aid.",
 "My goddess mother foretold that she would send this sign if war broke upon us, and would bring me arms made by Vulcan through the air to help me.",
 """'cecinit', 'sang', 'foretold', prophecy being chanted. 'missuram (esse)', 'that she would send', and 'laturam (esse)', 'that she would bring', future infinitives with the subject 'se' left out, as often in verse. 'diva creatrix', 'the goddess who bore me'. 'si… ingrueret', 'if war should come rushing on', subjunctive in reported speech. 'Volcania… arma', 'Vulcanian arms', the shield and armour forged in the last part. 'auxilio', 'for help', dative of purpose. 536 is a half-line, two words long: one of the lines Virgil left unfinished at his death, which the poem keeps as they are. Elisions 'bell(um) ingrueret', 'Volcaniaqu(e) arma', 'latur(am) auxilio'."""),
(537, 'instant;',
 "Alas, what great slaughters on the wretched Laurentines are pressing;",
 "Ah, what slaughter is hanging over the wretched Laurentines;",
 """'Heu quantae… caedes', 'alas, how great slaughters', an exclamation; the plural for many killings. 'miseris… Laurentibus', 'the wretched Laurentines', the people of Latinus's city Laurentum, dative with 'instant', 'press upon', 'are close at hand'. The pity is real: the Latins are his destined people. No elisions."""),
(538, 'dabis;',
 "what penalty to me, Turnus, you will pay;",
 "what a price you will pay me, Turnus;",
 """'quas poenas… dabis', 'what penalties you will give', i.e. 'pay': 'poenas dare', 'to pay the penalty', 'be punished'. 'mihi', 'to me', dative. 'Turne', vocative, an apostrophe to the absent enemy. The prophecy is fulfilled in the poem's last lines. No elisions."""),
(540, 'pater!',
 "how many under the waves\nshields of men and helmets and brave bodies you will roll,\nFather Thybris!",
 "how many shields of warriors, how many helmets and the bodies of brave men you will roll beneath your waters, Father Tiber!",
 """'quam multa… scuta… galeasque… corpora', 'how many shields and helmets and bodies'. The line 539 repeats 1.101, 'scuta virum galeasque et fortia corpora volvit', from Aeneas's first speech in the storm, where he wished he had died at Troy among the dead the Simois rolled down: the despairing memory now becomes a threat. Behind both is Achilles choking the Scamander with corpses (Iliad 21, from memory). 'virum' = 'virorum'. 'volves', 'you will roll'. 'Thybri', vocative of the Greek form 'Thybris', the Tiber as a river-god, 'pater'. Elision 'galeasqu(e) et'."""),
(540, 'rumpant.”',
 "Let them demand battle-lines and the treaties break.”",
 "Let them call for war, and break their treaties!”",
 """'Poscant… rumpant', 'let them demand… let them break', jussive subjunctives, bitter and defiant: let the Latins have the war they ask for. 'acies', 'battle-lines', 'battle'. 'foedera rumpant', the alliance Latinus offered Aeneas in Book 7, now overthrown by the war Juno and Allecto stirred up. Aeneas's speech ends, and Greenough closes the mark. No elisions."""),
(544, 'adit:',
 "These when spoken he had uttered, from the seat he raises himself high,\nand first, by Herculean fires the slumbering altars\nhe rouses, and the yesterday's Lar and the small Penates\njoyful approaches:",
 "When he had said this, he rose from his lofty seat, and first he roused the altar fires of Hercules that had sunk to embers, and gladly approached the household god he had worshipped the day before and Evander's humble Penates:",
 """A new paragraph in Greenough. 'Haec ubi dicta dedit', 'when he had given these words', a set formula of epic. 'solio… ab alto', 'from the high seat', framing 'se tollit'. 'Herculeis sopitas ignibus aras', 'the altars slumbering with Herculean fires', the altars of yesterday's festival of Hercules (8.102 ff.), where the fire has died to embers; 'excitat', 'he wakes', 'rekindles'. 'hesternum… larem', 'yesterday's Lar', the household god Evander honoured the day before; 'Lar' and 'penates' are the gods of the home. 'parvos', 'humble', in keeping with Evander's poor house. 'penatis', accusative plural in '-is' (Greenough's '-is', as always). 'laetus', 'glad', at the sign. Elision 'prim(um) Herculeis'."""),
(545, 'iuventus.',
 "they sacrifice chosen in the custom two-year sheep,\nEvander equally, equally the Trojan youth.",
 "and Evander and the young Trojans alike sacrificed sheep chosen according to custom.",
 """'mactant', 'they sacrifice', plural with the two subjects 'Euandrus' and 'iuventus'; The Latin Library prints 'mactat', the singular agreeing with the nearer subject, a small difference of sense. 'lectas de more bidentis', 'two-year-old sheep chosen by custom', 'bidens', 'having two (teeth)', a sheep old enough to show its two permanent incisors, the age for sacrifice; '-is' accusative plural. 'pariter, pariter', 'alike… alike', the repetition binding the two peoples in one act. 'Euandrus', Greenough's Greek spelling, three syllables, E-van-drus. No elisions."""),
(546, 'revisit.',
 "Afterwards from here to the ships he steps and his comrades revisits.",
 "Then he went down to the ships and saw his companions again.",
 """'Post hinc', 'afterwards, from here', two adverbs together. 'ad navis', 'to the ships', '-is' accusative plural. 'graditur', 'he walks', deponent. 'revisit', 'goes back to see', his men left with the ships at Pallanteum. No elisions."""),
(548, 'legit;',
 "Of whom from the number, who themselves into wars should follow,\nthose excelling in valour he picks;",
 "From among them he chose the bravest to follow him into war;",
 """'Quorum', 'of whom', the connecting relative ('and of them'). 'de numero', 'from the number'. 'qui sese in bella sequantur', 'to follow him into wars', a relative clause of purpose with the subjunctive. 'praestantis virtute', 'outstanding in courage', '-is' accusative plural, object of 'legit', 'he chooses'. Elision 'ses(e) in'."""),
(550, 'patrisque.',
 "the remaining part, downward\nis carried on the water and lazily with the favouring stream flows down,\nas messengers to come to Ascanius both of events and of his father.",
 "the rest drifted down the river, borne idly on the current, to bring Ascanius news of what had happened and of his father.",
 """'pars cetera', 'the rest'. 'prona… aqua', 'on the downward-sloping water', i.e. downstream to the Tiber's mouth, where the Trojan camp is. 'fertur', 'is carried'. 'segnis', 'lazily', adjective for adverb: they need not row. 'secundo… amni', 'with the following stream', 'secundus' from 'sequor'. 'nuntia ventura', 'to come as messengers', future participle of purpose, neuter plural agreeing loosely with 'pars'. 'rerumque patrisque', 'both of events and of his father', the double '-que'. Elision 'ventur(a) Ascanio'."""),
(551, 'arva;',
 "Horses are given to the Teucrians to Tyrrhenian heading fields;",
 "Horses were given to the Trojans who were bound for the lands of Etruria;",
 """'Dantur', 'are given', by Evander. 'Teucris', 'to the Teucrians', the Trojans, from Teucer, an ancestral king; 'Teucr-' has the diphthong 'eu', one syllable. 'Tyrrhena petentibus arva', 'heading for Tyrrhenian fields', Etruria, the participle agreeing with 'Teucris'. No elisions."""),
(553, 'aureis.',
 "they lead a choice one for Aeneas, which a tawny lion's\npelt covers wholly, gleaming with claws golden.",
 "for Aeneas they led out a horse picked out of the common lot, wholly covered by a tawny lion's skin that glittered with gilded claws.",
 """'exsortem', 'out of the lot', a horse not shared out by lot but set apart as a special gift; 'equum' is understood. 'Aeneae', dative, 'for Aeneas'. 'fulva leonis pellis', 'a tawny lion's pelt', split across the lines. 'obit totum', 'covers it entirely', 'obeo' in its sense 'go round', 'envelop'. 'praefulgens unguibus aureis', 'shining with golden claws', the claws gilded; 'aureis' is two syllables, 'au-reis', by synizesis. A lion skin is a hero's gear, the mark of Hercules, whose festival the book has just told. Elision 'exsort(em) Aeneae'."""),
(555, 'regis.',
 "Rumour flies, suddenly spread through the small city,\nthat swiftly go horsemen to the shores of the Tyrrhenian king.",
 "A rumour flew at once through the little town that horsemen were riding fast for the shores of the Etruscan king.",
 """A new paragraph in Greenough. 'Fama volat', 'Rumour flies', an epic commonplace, and Rumour is a winged goddess at 4.173 ff. 'volgata', Greenough's spelling of 'vulgata', 'spread abroad'. 'parvam… per urbem', 'through the small city', framing the participle: Pallanteum is a village. 'ire equites', accusative and infinitive giving the rumour's content. 'ocius', 'more swiftly', the comparative for 'with speed'. 'ad litora regis', 'to the shores of the king', of Tarchon; The Latin Library prints 'limina', 'the king's threshold', his court, a change of picture rather than of the event. Elisions 'ir(e) equites', 'Tyrrhen(i) ad'."""),
(557, 'imago.',
 "Vows from fear the mothers double, and nearer to the danger\ngoes the fear, and greater of Mars now appears the image.",
 "The mothers doubled their prayers in their fear; dread came closer as the danger grew, and the shape of war now loomed larger before them.",
 """The print has 'vota', lowercase after the full stop that ends 555, a misprint for 'Vota', corrected here; t keeps the print, because t must match the pinned source; l and i begin with a capital. 'vota… duplicant', 'they double their vows', prayers and promised offerings for the riders' return. 'metu', 'out of fear', ablative of cause. 'propius periclo it timor', 'fear goes nearer to the danger': fear grows as the danger comes close. 'periclo' = 'periculo', the old short form, dative with 'propius'. 'Martis… imago', 'the image of Mars', of war, now plainly in view. Elision 'i(am) apparet'."""),
(559, 'fatur:',
 "Then father Evander, the right hand having clasped of him going,\nclings, unsated, weeping, and such things speaks:",
 "Then Evander, the father, clasping the hand of his departing son, clung to him, unable to have his fill of tears, and spoke these words:",
 """The print has 'tum', lowercase after the full stop that ends 557, a misprint for 'Tum', corrected here; t keeps the print, because t must match the pinned source; l and i begin with a capital. 'pater Evandrus', 'father Evander', father here in the plain sense. Greenough prints 'Evandrus' here and 'Euandrus' at 545; the spelling varies, the name is the same. 'dextram complexus euntis', 'having clasped the right hand of (his son) going', 'euntis', genitive singular of the participle of 'eo', the son left to be understood. 'haeret', 'clings'. 'inexpletus lacrimans', 'insatiate, weeping', unable to weep enough. 'talia fatur', 'speaks such things', the formula that brings on a speech. No elisions."""),
(563, 'misi,',
 "“O if for me past should bring back Jupiter the years,\n(such as I was when the front line under Praeneste itself\nI laid low, and of shields burned, a victor, the heaps,\nand the king with this, Erulus, right hand down to Tartarus I sent,",
 "“O, if only Jupiter would bring back to me the years that are gone (the man I was when, beneath the very walls of Praeneste, I cut down the front rank of the enemy, burned the piles of their shields in victory, and with this right hand sent King Erulus down to Tartarus,",
 """A comma-ended unit: Evander's first sentence runs to 571 and is split at its commas. 'O… si referat', 'O, if (Jupiter) should bring back', a wish with the present subjunctive; the sentence turns at 568 into a contrary-to-fact statement. Nestor in Homer looks back the same way to the deeds of his youth, wishing he were young as then (Iliad 7 and 11, from memory). 'qualis eram', 'such as I was'; the print opens a bracket here, and the clause it encloses runs to 567 (see there). 'Praeneste sub ipsa', 'under Praeneste itself', a Latin town in the hills east of Rome, here feminine ('ipsa'), though usually neuter. 'scutorum… acervos', 'heaps of shields', captured arms burned as an offering. 'Erulum', King Erulus, known only from this story. 'Tartara', neuter plural, the underworld. Elisions 'prim(am) aciem', 'scutorumqu(e) incendi', 'reg(em) hac'."""),
(565, 'dederat;',
 "to whom at birth three lives Feronia his mother\n(horrible to say) had given;",
 "to whom at his birth his mother Feronia had given three lives (dreadful to tell);",
 """'nascenti cui', 'to whom being born', 'cui' one syllable. 'tris animas', 'three lives', 'tris' the old accusative plural of 'tres'. 'Feronia', an old Italian goddess, honoured in groves at Soracte and Tarracina; that Erulus was her son is told only here. A many-lived monster recalls Geryon, the three-bodied giant Hercules killed. 'horrendum dictu', 'horrible to tell', the supine in '-u', ablative of respect, a set phrase in epic; Greenough brackets it himself. No elisions."""),
(566, 'erat;',
 "three suits of arms to be wielded,\nthree times by Death he had to be laid low;",
 "three times he had to take up arms, three times be laid low in death;",
 """'terna arma movenda (erant)', 'three sets of arms had to be wielded', the gerundive of obligation; 'terni', distributive, 'three each', 'three sets'. 'ter Leto sternendus erat', 'three times he had to be laid low by Death', again the gerundive with 'erat'. 'Leto', dative of agent, Death personified, a solemn old word for 'mors'. The repetition 'terna… ter' marks the three fights. Elision 'tern(a) arma'."""),
(567, 'armis:',
 "from whom then however all\ntook away this right hand the lives, and of as many arms stripped him):",
 "and yet this right hand took every one of those lives from him, and stripped him of as many suits of armour):",
 """The print has 'armis:' with no closing bracket, though it opened one at 561 ('(qualis eram') and never closes it (the bracket in 565 is a separate, closed one), a misprint for 'armis):', corrected here; t keeps the print, because t must match the pinned source. The clause from 561 to here is the parenthesis, and the main sentence resumes at 'non ego' (568); no other place for the bracket fits the sense. 'cui… abstulit', 'took away from whom', 'cui' dative of separation. 'tunc tamen', 'then, nonetheless', in spite of his three lives. 'omnis… animas', 'all his lives', '-is' accusative plural. 'totidem exuit armis', 'stripped him of as many sets of arms', ablative of separation. Elisions 'dextr(a) et', 'totid(em) exuit'."""),
(571, 'urbem.',
 "not I now from your sweet embrace would be torn anywhere,\nson, your, nor on his neighbouring ever would Mezentius,\nthis head insulting, so many with the sword cruel have dealt\ndeaths, of so many citizens bereaved the city.",
 "I would not now be torn from your sweet embrace, my son, nor would Mezentius ever have mocked me, his neighbour, and dealt out so many cruel deaths by the sword, and robbed this city of so many of its citizens.",
 """The main clause, resuming after the bracket. 'non… divellerer', 'I would not be torn away', imperfect subjunctive of a present unreal condition; 'dedisset', 'viduasset', pluperfects for the past. 'dulci amplexu… tuo', 'from your sweet embrace', split by 'divellerer usquam' and the vocative 'nate'. 'finitimo huic capiti insultans', 'insulting this neighbouring head', 'caput', 'head', for the person: Evander himself, whom Mezentius scorned across the border. 'tot ferro saeva… funera', 'so many cruel deaths by the sword'. 'viduasset' = 'viduavisset', 'bereaved', 'widowed'. 'urbem' is most naturally Pallanteum; some take it as Mezentius's own city. Elisions 'dulc(i) amplexu', 'capit(i) insultans'."""),
(574, 'preces.',
 "But you, O gods above, and of the gods you, greatest ruler,\nJupiter, an Arcadian, I beg, pity king,\nand a father's hear prayers.",
 "But you, O gods above, and you, Jupiter, mightiest ruler of the gods, take pity, I beg you, on an Arcadian king, and listen to a father's prayers.",
 """'At', 'but', turning from regret to prayer. 'superi', 'gods above', vocative. 'divom tu maxume rector', 'you, greatest ruler of gods', 'divom' = 'divorum', 'maxume' Greenough's old spelling of 'maxime'. 'miserescite', 'take pity', with the genitive 'Arcadii… regis', 'on the Arcadian king', Evander speaking of himself in the third person. 'quaeso', 'I beg', parenthetic. 'patrias… preces', 'a father's prayers', the adjective doing the work of a genitive. Elision 'super(i) et'."""),
(577, 'laborem.',
 "If your divine powers\nunharmed Pallas for me, if the fates keep in store,\nif I am to see him, I live, and to come together into one:\nlife I pray for; I endure any to last out toil.",
 "If your divine will and the fates are keeping Pallas safe for me, if I am to see him again and meet him once more, I pray for life; I can bear to endure any hardship.",
 """'Si… reservant… si… vivo', 'if (they) are keeping… if I live', simple conditions with the indicative. 'numina vestra… fata', 'your divine powers… the fates', the two subjects of 'reservant'. 'incolumem Pallanta', 'Pallas safe', 'Pallanta' Greek accusative. 'si visurus eum vivo', 'if I am living to see him', the future participle of what is destined. 'venturus in unum', 'about to come into one (place)', to meet again. The colon then gives the apodosis: 'vitam oro', 'I ask for life'. 'patior… durare', 'I submit to enduring', 'I can endure'. 'quemvis… laborem', 'any toil whatever', framing 'durare'. Elisions 'viv(o) et', 'vit(am) oro'."""),
(578, 'minaris:',
 "But if some unspeakable misfortune, Fortune, you threaten:",
 "But if, Fortune, you are threatening some unspeakable blow:",
 """'Sin', 'but if', the second of two contrasted conditions. 'infandum casum', 'an unspeakable fall', a disaster too dreadful to name: Pallas's death. 'Fortuna', vocative, the goddess of chance now addressed directly. 'minaris', 'you threaten', deponent. The colon introduces the wish that answers it. Elision 'aliqu(em) infandum'."""),
(579, 'vitam,',
 "now, O now, may it be allowed the cruel to break off life,",
 "now, O now, may I be allowed to break off this cruel life,",
 """A comma-ended unit: the sentence runs to 583. 'nunc O nunc', 'now, O now', the urgent repetition (The Latin Library has the words in another order, with the same sense). 'liceat', 'may it be permitted', a wish with the present subjunctive. 'crudelem abrumpere vitam', 'to break off (my) cruel life', the life made cruel by what it would have to witness. Elision 'crudel(em) abrumpere'."""),
(584, 'fundebat:',
 "while the cares are undecided, while the hope uncertain of the future,\nwhile you, dear boy, my late and only joy,\nin my embrace I hold, and that no heavier news my ears\nshould wound.” These words the father at the parting last\npoured out:",
 "while my fears are still unsettled, while hope of the future is uncertain, while I still hold you in my arms, dear boy, my late-born and my only joy, so that no heavier news may wound my ears.” These were the words the father poured out at their last parting:",
 """The print has 'volneret. ”Haec', with a space before the closing mark and none after it, a misprint for 'volneret.” Haec', corrected here; t keeps the print, because t must match the pinned source. Because the mark is joined to 'Haec', this unit also carries 'Haec genitor… fundebat', as at 7.560, 8.404 and 8.443. 'dum… dum… dum', 'while… while… while', the anaphora of a man clinging to the moment. 'curae ambiguae', 'cares undecided': his fear may yet prove groundless. 'mea sera et sola voluptas', 'my late and only joy', a child of his old age. 'neu… volneret', 'and lest… wound', a negative purpose continuing 'liceat'; 'volneret', Greenough's 'vulneret'. Evander's speech ends. 'digressu… supremo', 'at the last parting', and it proves the last. Elisions 'cur(ae) ambiguae', 'ser(a) et'."""),
(584, 'ferebant.',
 "the servants him, collapsed, into the house were carrying.",
 "his servants carried him indoors, fainting.",
 """'famuli', 'servants'. 'conlapsum', 'having collapsed', from 'conlabor' (Greenough's spelling of 'collapsum', the prefix unassimilated), the object of 'ferebant'; 'eum' is understood. 'in tecta', 'into the house', 'tecta', 'roofs', for the building. The imperfect leaves the scene unfinished as the narrative moves on. Elision 'conlaps(um) in'."""),
(588, 'armis:',
 "And now indeed had gone out by the gates the cavalry, opened,\nAeneas among the first and faithful Achates,\nthen other of Troy chiefs; himself, of the column Pallas\nin the middle, in his cloak and painted conspicuous in arms:",
 "And now the cavalry had ridden out through the open gates, Aeneas and faithful Achates among the first, then the other princes of Troy, and Pallas himself in the middle of the column, conspicuous in his cloak and his ornamented armour:",
 """A new paragraph in Greenough. 'Iamque adeo', 'and now indeed', marking the decisive moment. 'exierat', pluperfect: by the time we look, they are out. 'portis… apertis', 'by the opened gates', framing 'equitatus', 'the cavalry'. 'proceres', 'chiefs', 'princes'. 'ipse… Pallas', 'Pallas himself', framing 'agmine', with 'agmine… in medio', 'in the middle of the column'; The Latin Library prints 'it', 'goes', for 'in' (most likely 'it medio', 'goes in the middle'), supplying a verb, with the same picture. 'chlamyde', 'in a cloak', the Greek short military mantle. 'pictis… in armis', 'in painted arms', worked with colour or inlay. 'conspectus', 'conspicuous'. Elisions 'Iamqu(e) adeo', 'ade(o) exierat', 'ind(e) alii', 'ips(e) agmine', 'chlamyd(e) et'."""),
(591, 'resolvit.',
 "such as when, of Ocean drenched with the wave, Lucifer,\nwhom Venus beyond the others of the stars loves, the fires,\nhas raised his face sacred to the sky and the darkness dissolved.",
 "like the Morning Star, when, wet from the waters of Ocean, the star Venus loves above all the other fires of heaven lifts his holy face into the sky and scatters the darkness.",
 """'qualis ubi', 'such as when', a simile. 'Lucifer', 'Light-bringer', the morning star, the planet of Venus: so 'quem Venus… diligit', 'whom Venus loves', 'ante alios astrorum… ignis', 'beyond the other fires of the stars', '-is' accusative plural. 'Oceani perfusus… unda', 'drenched in the wave of Ocean': the stars were thought to rise from the river Ocean round the earth. 'extulit', 'has raised', the gnomic perfect of a simile. 'os sacrum', 'his holy face'. 'resolvit', 'dissolves'. Homer compares Achilles' gleaming spear to the evening star and Diomedes' armour to a star new-bathed in Ocean (Iliad 22 and 5, from memory); a bright star in a simile there often warns of death. Elisions 'ub(i) Oceani', 'ant(e) alios'."""),
(593, 'catervas.',
 "Stand fearful on the walls the mothers and with eyes follow\nthe dusty cloud and gleaming with bronze the squadrons.",
 "The mothers stood fearful on the walls and followed with their eyes the cloud of dust and the troops flashing with bronze.",
 """'Stant pavidae… matres', 'the frightened mothers stand', the women who doubled their prayers (556). 'in muris', 'on the walls'. 'oculis… sequuntur', 'they follow with their eyes', as the column moves off. 'pulveream nubem', 'the dusty cloud', the dust raised by the horses. 'fulgentis aere catervas', 'the troops shining with bronze', '-is' accusative plural. Elision 'pavid(ae) in'."""),
(595, 'tendunt;',
 "They, through the thickets, where nearest the end of the roads,\narmed make their way;",
 "Under arms they pressed on through the scrub by the shortest road to their goal;",
 """'Olli', archaic for 'illi', 'they', a form Virgil uses for an old-fashioned ring (you have met it before). 'per dumos', 'through the thickets'. 'qua proxuma meta viarum (est)', 'where the goal of the ways is nearest', i.e. by the shortest route; 'proxuma' is Greenough's old spelling of 'proxima', and 'meta' is the turning-post or end-point. 'armati tendunt', 'they press on, armed'. No elisions."""),
(596, 'campum.',
 "goes the shout, and, a column having been formed,\nwith four-footed sound shakes the crumbling plain the hoof.",
 "a shout goes up; they form a column, and the gallop of hooves hammers the loose, dry earth.",
 """'it clamor', 'the shout goes', rises. 'agmine facto', 'a column having been made', ablative absolute: they fall into line of march. 596 is one of the most famous sound-lines in Latin: five dactyls and the final foot, the run of short syllables beating like a gallop. 'quadrupedante… sonitu', 'with a four-footed sound', the sound of four hooves; 'quadrupedans', 'galloping', from 'quadrupes'. 'putrem… campum', 'the crumbling plain', powdery, broken up. 'ungula', 'the hoof', singular for all the hooves. 'quatit', 'shakes'. Virgil rings a variation on the same line at 11.875 (from memory), and the effect goes back to Ennius (from memory). No elisions."""),
(598, 'sacer;',
 "There is a vast cool grove near the Caerite river,\nby the religion of the fathers widely sacred;",
 "There is a great, cool grove near the river of Caere, held sacred far and wide by the religion of our forefathers;",
 """'Est ingens… lucus', 'there is a great grove', the formula that opens a description of a place ('est locus…'). 'gelidum', 'cold', 'cool' with shade. 'lucus', a sacred grove. 'Caeritis amnem', 'the river of Caere', 'Caeritis' genitive of 'Caere', the Etruscan city also called Agylla (8.479), Mezentius's old city, near the coast north of Rome; the stream is a small one by the town. 'religione patrum', 'by the religious awe of the fathers', ablative of cause. 'late sacer', 'sacred far and wide', revered throughout the region. No elisions."""),
(599, 'cingunt.',
 "on all sides hills\nhave shut it in, hollow, and with black fir the grove encircle.",
 "on every side hollow hills enclose it, and ring the wood with dark fir.",
 """'undique', 'on all sides'. 'colles… cavi', 'hollow hills', curving round like a bowl. 'inclusere' = 'incluserunt', 'have shut in', the '-ere' perfect. 'nigra… abiete', 'with black fir', framing 'nemus', 'the grove', a second word for the same wood; 'abiete' is three syllables in verse, not four, 'ab-ye-te', the i a consonant. 'cingunt', 'surround'. Elision 'cav(i) et'."""),
(602, 'Latinos:',
 "To Silvanus the story is the ancient sacred made Pelasgians,\nof fields and of the flock the god, both grove and day,\nwho first the borders once held Latin:",
 "The story is that the ancient Pelasgians, who long ago were the first to hold the lands of Latium, dedicated both the grove and a festival day to Silvanus, god of the fields and the flocks:",
 """'fama est', 'the story is', with accusative and infinitive: 'veteres sacrasse Pelasgos', 'that the ancient Pelasgians consecrated'. 'sacrasse' = 'sacravisse', the shortened perfect infinitive. 'Silvano', dative, Silvanus, the Italian god of woods and wild land, here of fields and herds as well: 'arvorum pecorisque deo', in apposition. 'lucumque diemque', 'both the grove and a day', a feast day, the double '-que'. 'Pelasgos', the Pelasgians, the old name for the pre-Greek peoples of Greece, believed to have wandered into Italy too: 'qui primi… habuere', 'who first held', 'habuere' = 'habuerunt'. 'finis… Latinos', 'the Latin borders', '-is' accusative plural. Elisions 'fam(a) est', 'aliquand(o) habuere'."""),
(605, 'arvis.',
 "not far from here Tarchon and the Tyrrhenians safe were holding\na camp by its position, and from a lofty all hill to be seen\nnow could the legion, and in broad was encamped in the fields.",
 "not far from there Tarchon and the Etruscans held a camp made safe by the lie of the land, and from a high hill the whole of their army could now be seen, its tents spread out across the wide fields.",
 """'haud procul hinc', 'not far from here'. 'Tarcho', a Latin form of the nominative 'Tarchon', the Etruscan leader (8.506). 'tuta… castra locis', 'a camp safe by its position', 'locis', ablative of cause, the natural strength of the ground. 'celso… de colle', 'from a high hill', framing 'omnis', which agrees with 'legio': 'omnis… legio', 'the whole army', 'legio' used loosely of the Etruscan host. 'videri… poterat', 'could be seen'. 'tendebat', 'was encamped', 'tendere' (tentoria), 'to pitch tents'. 'latis… in arvis', 'in the broad fields', framing 'tendebat'. Elisions 'Tarch(o) et', 'celsoqu(e) omnis', 'legi(o) et'."""),
(607, 'curant.',
 "Hither father Aeneas and for war the chosen youth\ncome up, and weary both horses and bodies tend.",
 "Here father Aeneas and his young men chosen for war came up, and, tired out, they cared for their horses and for themselves.",
 """'Huc', 'hither'. 'pater Aeneas', the formal title, father of his people. 'bello lecta iuventus', 'the youth chosen for war', 'bello' dative of purpose. 'succedunt', 'come up', 'approach', the present for vivid narrative. 'fessi', 'tired', after the ride. 'et equos et corpora curant', 'tend both horses and bodies', 'corpora curare', 'to look after one's body', to eat and rest; the double 'et'. The arrival sets up Venus's gift in the next part. Elision 'fessiqu(e) et'."""),
]

P = A.part('aeneid-062'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
