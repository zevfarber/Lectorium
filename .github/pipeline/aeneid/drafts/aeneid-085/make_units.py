# aeneid-085 (XI.336-444): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Drances et Turnus. Altercatio'
PART = "The Quarrel of Drances and Turnus (XI.336–444)"
TITLE_EN = "The Quarrel of Drances and Turnus — Aeneid XI.336–444"
ABOUT = ("Latinus has proposed peace with the Trojans, and the first to rise in his council is Drances, an old enemy of Turnus: rich, eloquent, influential in faction, of noble birth on his mother's side, and no fighter. "
"He backs the king's offer and asks him to add one more gift, his daughter Lavinia as bride for Aeneas, and then turns on Turnus by name. "
"Turnus's ill-starred leadership, he says, has cost the Latins their best captains and filled the city with mourning; there is no safety in war; let Turnus give up his claim and go, or, if he wants the princess and the palace so badly, let him face Aeneas alone, for Aeneas is calling him out. "
"Turnus blazes up. "
"Drances, he answers, is always bold in words while the walls keep the enemy away; let him show his valour in the field, where the Trojans are near enough. "
"Turnus recalls his own deeds, Pallas and the Arcadians killed, Pandarus and Bitias cut down inside the Trojan camp, and mocks Drances' terror of a twice-defeated people. "
"Then he turns to Latinus: if all hope is gone, let them beg for peace; but the Latins still have men, allies, Messapus, Tolumnius, Camilla and her horsemen, and fortune has often turned. "
"And if Aeneas wants him alone, Turnus will meet him, even if he proves a second Achilles in armour made by Vulcan; he has devoted his life to his people and his king. "
"The debate is Virgil's version of a Roman senate-house quarrel, and Drances, the clever civilian who goads a soldier, echoes Homer's Thersites and Polydamas while being neither.")

U = [
(339, 'auctor,',
 """Then Drances, the same hostile one, whom the glory of Turnus\nwith sidelong envy and with goads was driving bitter,\nlavish of wealth and in tongue better, but cold for war\nhis right hand, in counsels held a not futile adviser,""",
 """Then Drances rose, hostile as ever, a man whom the glory of Turnus spurred on with the bitter goads of a jealous, sidelong envy; lavish with his wealth and better with his tongue, though his sword-hand was cold in war, he was held to be no worthless counsellor,""",
 """A new paragraph in Greenough. 'idem infensus', 'the same man, hostile', the Drances who spoke against Turnus at the truce (122–131). 'obliqua invidia', 'with envy looking askance'; 'stimulis… amaris', 'with bitter goads', framing the line-end. 'largus opum', 'generous of wealth', genitive with an adjective; 'lingua melior', 'better in tongue', ablative of respect. 'frigida bello dextera', the right hand that should strike is 'cold' in war. 'habitus', 'considered'; 'consiliis', dative or ablative, 'in debate'. The main verb waits until 342 ('surgit'). Elisions 'ide(m) infensus', 'obliqu(a) invidia', 'op(um) et'."""),
(342, 'iras:',
 """in sedition powerful (birth to him from his mother proud\nnobility gave, uncertain from his father he bore),\nrises and with these weighs down words and heaps up angers:""",
 """powerful in faction (his mother's high rank gave him proud descent; his father's he brought with him uncertain), he rose, and with these words loaded and heaped up the anger:""",
 """'seditione potens', 'powerful in civil strife', able to sway a crowd, a Roman type. The parenthesis gives his birth: 'genus… superbum… nobilitas dabat', 'nobility on the mother's side gave him proud birth'; 'incertum de patre ferebat', 'from his father he carried (a birth) uncertain', the noun 'genus' understood: his father was obscure, or unknown (Servius takes it either way). 'onerat… aggerat iras', 'loads and piles up the angers', the metaphor of building a rampart (agger) of hatred against Turnus. 'surgit', vivid present, as speakers rose in the Roman senate. Elision 'atqu(e) aggerat'."""),
(345, 'mussant.',
 """“A matter to no one obscure and not of our voice needing\nyou consult on, O good king: all themselves to know confess\nwhat the fortune of the people brings, but to say they mutter.""",
 """“You ask our counsel, good king, on a matter that is dark to no one and has no need of any word from us: all confess they know what the fortune of the people portends, but they only mutter and dare not say it.""",
 """Drances' speech begins. 'Rem… consulis', 'you consult (us) on a matter', 'consulo' with the accusative of the thing asked about. 'nulli obscuram', 'unclear to nobody'; 'nostrae… vocis egentem', 'needing our voice', 'egeo' with the genitive. 'O bone rex', a respectful vocative. 'quid fortuna ferat populi', indirect question, 'what the fortune of the people brings': ruin, if the war goes on. 'mussant', 'they mutter, hesitate to speak', from fear of Turnus; Drances casts himself as the one brave enough to speak out. Elision 'null(i) obscuram'."""),
(350, 'luctu,',
 """Let him give freedom of speaking and the blusterings let him remit,\non account of whose auspices ill-omened and character perverse\n(I will say it indeed, though arms to me and death he threaten)\nthe lights so many to have fallen of leaders and the whole we see\nto have sunk the city in grief,""",
 """Let him grant us freedom to speak and abate his blustering pride, the man under whose ill-starred leadership and perverse ways (yes, I will say it, though he threaten me with arms and death) we see so many of our leaders, the lights of our people, fallen, and the whole city sunk in grief,""",
 """Turnus is not named: 'Det… remittat', jussive subjunctives, 'let him give… let him abate', with the antecedent of 'cuius' left as 'he'. 'flatus', 'blasts, puffs', of his arrogance. 'ob auspicium infaustum', 'because of his unlucky auspices': a Roman general fought under his own auspices, so defeat was his. 'mores… sinistros', 'perverse character', 'sinister', 'left', the unlucky side. 'lumina… ducum', 'the lights of leaders', a bold metaphor. 'cecidisse… consedisse', accusative and infinitive after 'videmus'. Elisions 'auspici(um) infaustum', 'dic(am) equidem'."""),
(351, 'armis.',
 """while the Trojan he assails\ncamp, in flight trusting, and heaven he terrifies with arms.""",
 """while he makes his attempt on the Trojan camp, trusting to flight, and frightens heaven with the clash of arms.""",
 """'dum… temptat', 'while he assails', the present with 'dum'. 'Troia… castra', the Trojan camp, the adjective and noun across the line-break. 'fugae fidens', 'trusting in flight', a sneer: Turnus escaped from inside the camp only by leaping into the Tiber (IX.815–818). 'caelum territat armis', 'he frightens the sky with arms', all noise and no result; the frequentative 'territat' adds to the scorn. No elisions."""),
(356, 'iungas.',
 """One thing also to those gifts, which very many to be sent\nto the Dardanians and to be promised you order, one thing, best of kings,\nmay you add, and not you anyone's violence conquer,\nbut that your daughter to an outstanding son-in-law and worthy marriage\nyou give, father, and this peace with an eternal treaty bind.""",
 """To those gifts, so many, that you order to be sent and promised to the Dardanians, add one thing more, best of kings, one thing, and let no man's violence overcome you: give your daughter, father, to a son-in-law of distinction in a worthy marriage, and bind this peace with an everlasting treaty.""",
 """'Unum… unum', the repetition holds back what the gift is. 'donis istis', dative with 'adicias', 'add to those gifts', the ones Latinus proposed (333–334). 'adicias', potential or jussive subjunctive; its first syllable is long, as if 'adiicias'. 'nec te ullius violentia vincat', 'and let not anyone's violence defeat you', meaning Turnus's. 'quin… des… iungas', 'from giving… and binding', 'quin' after the idea of prevention. 'egregio genero', Aeneas, unnamed. 'hymenaeis', Greek, 'marriage', a four-syllable line-end. Elisions 'Un(um) etiam', 'un(um) optime', 't(e) ullius', 'nat(am) egregio', 'dignisqu(e) hymenaeis', 'pac(em) hanc'."""),
(359, 'remittat.',
 """But if so great holds minds and breasts terror,\nhimself let us beseech, and favour let us beg from himself:\nlet him yield, his own right to the king and country let him give up.""",
 """But if such terror holds our minds and hearts, let us beseech the man himself and beg the favour of him in person: let him give way and surrender his own claim to the king and to his country.""",
 """'Quod si', 'but if'. 'tantus… terror', framing the line. 'ipsum… ab ipso', 'the man himself… from the man himself', heavy irony: if Turnus is so feared, the council must plead with him as with a lord. 'obtestemur… oremus', hortatory subjunctives, 'let us beseech… let us beg'. 'cedat… remittat', jussive, 'let him yield… give back'. 'ius proprium', 'his own right', his claim to Lavinia's hand, which only he can surrender. Elision 'veniamqu(e) oremus'."""),
(361, 'malorum?',
 """Why the wretched so often into open dangers citizens\ndo you throw forward, O for Latium the head and cause of these evils?""",
 """Why do you fling our unhappy citizens so often into open danger, you, the source and cause of all these evils for Latium?""",
 """Now Drances turns and speaks to Turnus directly, an abrupt address (apostrophe). 'miseros… cives', framing the line. 'in aperta pericula', 'into dangers in the open', 'proicis', 'you throw forth', as if they were things to be thrown away. 'caput… et causa', 'head and cause', the alliteration sharpening the charge; 'caput', 'fountain-head, origin'. 'Latio', dative of disadvantage. Elision 'hor(um) et'."""),
(363, 'pignus.',
 """No safety in war: peace you we ask, all,\nTurnus, together with peace's sole inviolable pledge.""",
 """There is no safety in war: we all ask you for peace, Turnus, and with it the one pledge that can keep a peace unbroken.""",
 """'Nulla salus bello', 'no safety in war', a short, quotable verdict; Turnus will throw these exact words back at 399. 'pacem te poscimus', 'posco' with two accusatives, the thing and the person asked. 'Turne', vocative, held to the start of the next line. 'pacis… inviolabile pignus', 'the inviolable pledge of peace', Lavinia, whose marriage to Aeneas would bind the treaty; she is not named. Elision 'solu(m) inviolabile'."""),
(365, 'venio.',
 """First I, hateful whom you to yourself imagine, and to be so\nI do not care, see, a suppliant I come.""",
 """I am the first, I whom you picture as your enemy (and I do not mind if I am), see, I come to you as a suppliant.""",
 """'Primus ego', 'I first', taking the lead. 'invisum quem tu tibi fingis', 'whom you imagine (as) hateful to you'. 'et esse nil moror', 'and I care nothing about being so', 'moror' here 'pay heed to', with an infinitive. 'en', 'look', drawing attention to the gesture. 'supplex', the suppliant's humility is false and the insult is real. Elision 'eg(o) invisum'."""),
(366, 'abi.',
 """Pity your own,\nput away your proud spirits and, beaten, go.""",
 """Take pity on your own people, lay aside your pride, admit you are beaten, and go.""",
 """'Miserere', imperative of the deponent 'misereor', with the genitive 'tuorum', 'your people'. 'pone animos', 'put down your spirits', the plural 'animi' meaning pride, arrogance. 'pulsus abi', 'go, beaten', the participle doing the work of a clause: admit defeat and leave. Turnus will pick up 'pulsus' with fury at 392. Elision 'pon(e) animos'."""),
(367, 'agros.',
 """Enough funerals, routed,\nwe have seen, and huge we have laid waste the fields.""",
 """We have been routed and seen enough deaths, and laid waste wide lands.""",
 """'Sat', short for 'satis', 'enough', with the genitive understood or simply adverbial. 'funera', 'deaths, funerals'. 'fusi', 'routed', nominative plural agreeing with the 'we' of 'vidimus'. 'ingentis… agros', 'huge fields', '-is' accusative plural, the adjective set before 'et': the word order is 'et ingentis desolavimus agros'. 'desolavimus', 'we have emptied', by the war. No elisions."""),
(370, 'hostem.',
 """Or if fame moves you, if so much in your breast strength\nyou conceive, and if so much a dowry palace to heart is,\ndare and, facing, trusting, carry your breast against the enemy.""",
 """Or if glory stirs you, if you feel such strength in your heart, if a palace that comes as a dowry is so dear to you, then be bold and carry your breast confidently against the enemy who faces you.""",
 """Three conditions, 'si… si… si', each sharper than the last. 'fama', 'reputation, glory'. 'concipis', 'you conceive', as if strength were a passion. 'dotalis regia', 'a palace for a dowry', Latinus's kingdom coming with Lavinia; Drances says Turnus wants the throne, not the girl. 'cordi est', 'is to the heart', 'is dear', the predicative dative. 'aude', 'dare'; 'adversum… in hostem', 'against the enemy opposite'. Elisions 's(i) adeo', 'cord(i) est', 'aud(e) atque', 'atqu(e) adversum'."""),
(373, 'campis.',
 """No doubt so that to Turnus may fall a royal wife,\nwe, souls cheap, an unburied and unwept crowd,\nmust be strewn on the plains.""",
 """No doubt, so that Turnus may win a royal bride, we, lives of no account, a crowd unburied and unwept, must be strewn across the plains.""",
 """'Scilicet', 'of course', bitterly ironic, as often. 'ut… contingat', purpose clause, 'so that (a royal wife) may fall to Turnus'. 'nos… sternamur', 'we are to be laid low', a jussive or indignant subjunctive. 'animae viles', 'cheap souls'. 'inhumata infletaque', 'unburied and unwept', the worst fate in the ancient world: the unburied could not cross the Styx (VI.325–330). The Latins have just been burying their dead under truce (182–224). Elision 'inhumat(a) infletaque'."""),
(375, 'vocat.”',
 """You too, if any you have strength,\nif of your father's Mars something you have, him look at, facing,\nwho calls.”""",
 """You too, if there is any strength in you, if you have anything of your father's war-like spirit, look him in the face — the man who calls you out.”""",
 """'siqua tibi vis', 'if (you have) any strength', 'siqua' printed as one word ('si qua'), 'tibi' dative of possession. 'patrii quid Martis', 'anything of your father's Mars', partitive genitive: Mars for warlike spirit, 'patrii', as Turnus's father Daunus was a fighter. 'illum… qui vocat', Aeneas, who said he would rather have met Turnus in single combat (115–118). 'contra', adverb, 'face to face'. 'qui vocat.' is one of Virgil's unfinished half-lines; the speech ends with it, abruptly. Elision 'ill(um) aspice'."""),
(376, 'Turni;',
 """At such words blazed up the violence of Turnus;""",
 """At such words Turnus's fierce temper flared;""",
 """A new paragraph in Greenough. 'exarsit', 'flared up', the image of fire, the regular word for sudden anger. 'violentia Turni', 'the violence of Turnus', the abstract noun as subject, picking up Drances' 'ullius violentia' (354): the speech provokes the very thing it complained of. 'violentia' is Turnus's word through the last books (XII.9, 45). No elisions."""),
(380, 'ades.',
 """he gives a groan and breaks out these from the bottom of his breast words:\n“Abundant indeed, Drances, always to you the supply of speaking\nthen, when wars hands demand; and when the fathers are called,\nfirst you are present.""",
 """he groaned, and these words burst from the depths of his breast: “You always have a full flow of words indeed, Drances, just when war calls for hands; and when the elders are summoned, you are the first to arrive.""",
 """'dat gemitum', 'gives a groan'. 'rumpit… voces', 'bursts out words', as if the words broke through. Turnus's speech begins. 'Larga… copia fandi', 'an abundant supply of speaking', 'fandi' the gerund. 'Drance', Greek vocative. 'tum, cum…', 'just when', the irony in the timing. 'patribus vocatis', ablative absolute, 'the fathers (elders) having been summoned', Roman senators. The Latin Library places 'semper' before 'Drance'; the sense is unchanged. Elision 'rumpitqu(e) has'."""),
(382, 'fossae.',
 """But not to be filled is the senate-house with words,\nwhich safely to you big fly, while keeps apart the enemy\nthe rampart of walls and do not overflow with blood the ditches.""",
 """But the council-chamber is not to be filled with words, words that fly big and safe from your mouth while the rampart of the walls holds back the enemy and the trenches are not yet brimming with blood.""",
 """'non replenda est', 'is not to be filled', the gerundive of obligation. 'curia', the Roman senate-house, a deliberate anachronism. 'quae… volant', 'which fly', words as winged things (Homer's 'winged words'). 'tuto', adverb, 'in safety'; 'magna', 'big', boastful. 'dum distinet hostem agger', 'while the rampart keeps off the enemy'; 'nec inundant… fossae', 'and the ditches are not flooding', 'dum' governing both. Elision 'replend(a) est'."""),
(386, 'agros.',
 """So thunder in eloquence, your habit, and me of fear\naccuse, you, Drances, since so many of slaughter heaps\nof Teucrians your right hand has made and everywhere with trophies\nyou mark the fields.""",
 """So go on, thunder with your eloquence, as you always do, and accuse me of cowardice, you, Drances, since your right hand has made such heaps of slaughtered Trojans, and you set up trophies all over the fields.""",
 """Bitter irony throughout. 'Proinde', 'so then', two syllables by synizesis. 'tona', 'thunder', of a loud orator. 'solitum tibi', 'a thing usual to you', in apposition to the whole command. 'timoris argue', 'accuse of fear', the genitive of the charge, a legal idiom. 'tot stragis acervos', 'so many heaps of slaughter'. 'insignis', second person singular of 'insignio', 'you mark, make conspicuous', not the adjective. 'tropaeis', trophies were enemy armour hung on a stake, as Aeneas did at the start of the book (XI.5–11). Elision 'ton(a) eloquio'."""),
(388, 'muros.',
 """What may achieve lively valour,\nyou may test; and not far, of course, the enemy\nare to be sought by us: they stand around on every side the walls.""",
 """What living valour can achieve, you are free to find out; and certainly we need not go far to look for the enemy: they are all round our walls.""",
 """'Possit quid vivida virtus', an indirect question, 'what lively valour can do', the object of 'experiare'. 'experiare licet', 'you may test', 'licet' with the subjunctive, 'experiare' an alternative form of 'experiaris'. 'scilicet', 'obviously', here dry rather than bitter. 'quaerendi nobis', 'must be sought by us', the gerundive with dative of agent. 'circumstant… muros', the Trojans are camped close by. No elisions."""),
(389, 'cessas?',
 """We go against the facing: why do you hang back?""",
 """Let us go out against them: why do you hang back?""",
 """'Imus', 'we are going', the present used for an immediate future, almost 'let us go'. 'in adversos', 'against those facing (us)', the enemy, the adjective standing as a noun. 'quid cessas?', 'why do you delay?', to Drances, who has not moved. The short clauses imitate a man already on his feet. No elisions."""),
(391, 'erit?',
 """Or to you will Mars in a windy\ntongue and in feet fleeing those\nalways be?""",
 """Or will your warfare always be in that windy tongue of yours and those feet so quick to run?""",
 """'An', introducing a second, scornful question. 'Mavors', an archaic and poetic form of 'Mars', the god for war-making itself. 'tibi', dative of possession, 'will your Mars be'. 'ventosa in lingua', 'in a windy tongue', all air. 'pedibus… fugacibus istis', 'in those runaway feet of yours', 'iste' contemptuous, 'that… of yours'. 'semper erit?' is one of Virgil's unfinished half-lines, here falling, as at 375, at a sharp break in the speech. Elision 'ventos(a) in'."""),
(392, 'ego?',
 """Beaten, I?""",
 """Beaten, am I?""",
 """Turnus seizes on Drances' word 'pulsus abi' (366), 'go, beaten', and throws it back as a question with no verb, 'beaten, I?', the indignation in the bare words. The next unit asks whether anyone could fairly call him so. No elisions within these words; 'ego' elides into 'Aut', across the question mark."""),
(395, 'armis?',
 """Or anyone justly, most foul one, beaten\nwill accuse, who swollen to grow with Ilian the Tiber\nblood, and of Evander the whole with the stock will see\nto have fallen the house and stripped the Arcadians of arms?""",
 """Or will anyone, you foulest of men, have the right to call me beaten, when he sees the Tiber rising swollen with Trojan blood, and the whole house of Evander fallen with all its line, and the Arcadians stripped of their arms?""",
 """'merito', 'deservedly', 'justly'. 'foedissime', 'most foul', vocative to Drances. 'pulsum arguet', 'will charge (me as) beaten'. 'qui… videbit', 'who will see', with three accusative and infinitive clauses: the Tiber growing swollen with Trojan blood ('Iliaco… sanguine' framing), Evander's house fallen 'with its stock', since Turnus killed Pallas, his only son (X.479–489), and the Arcadians 'stripped of their arms'. 'Arcadas', Greek accusative plural. Elisions 'eg(o) aut', 'puls(um) arguet', 'sanguin(e) et', 'dom(um) atque', 'atqu(e) exutos'."""),
(398, 'saeptus.',
 """Not so me tested Bitias and Pandarus huge\nand those whom a thousand in a day, victor, under Tartarus I sent,\nshut in by walls and by the hostile rampart hemmed.""",
 """That is not how I seemed to Bitias and huge Pandarus, or to the thousand I sent down to Tartarus in a single day of victory, though I was shut inside the walls and hemmed in by the enemy's rampart.""",
 """'Haud ita me experti (sunt)', 'not so did they find me'. In Book IX Turnus burst into the Trojan camp when the giant brothers Pandarus and Bitias threw the gate open; he killed Bitias, then Pandarus, and many more before he escaped into the Tiber (IX.672–818). 'mille', a round figure for 'countless'. 'die', 'in one day', ablative of time. 'inclusus… saeptus', 'shut in… hemmed', the danger he fought through. Elisions 'm(e) experti', 'hostiliqu(e) aggere'."""),
(399, 'bello.',
 """‘No safety in war.’""",
 """‘There is no safety in war,’ you say.""",
 """The print has an opening double mark before 'Nulla' and no closing mark anywhere; Turnus is quoting Drances' words of 362 back at him, and the reading text marks just those three words as a quotation within his speech. 'Nulla salus bello', 'no safety in war', said with scorn. Turnus answers the slogan in the next unit. No elisions."""),
(400, 'tuis.',
 """To the head sing such things, madman,\nof the Dardanian and to your own affairs.""",
 """Chant such things, madman, against the head of the Dardanian and for your own fortunes.""",
 """'Capiti… Dardanio', 'to the Dardanian head', Aeneas's, split across the line-break. 'cane', 'sing, prophesy', 'cano' used of oracles and spells: prophesy such doom for Aeneas, not for us. 'rebusque tuis', 'and to your own affairs', your own party, since Drances is suspected of favouring the Trojans. 'demens', 'madman', the insults grow. No elisions."""),
(402, 'Latini.',
 """So all things with great\ndo not cease to throw into confusion with fear and to extol the strength\nof a race twice conquered, on the other hand to press down the arms of Latinus.""",
 """So go on, never stop throwing everything into turmoil with your terrors, praising up the strength of a people twice beaten, and running down the arms of Latinus.""",
 """'ne cessa', 'do not stop', the poetic negative imperative with 'ne', instead of prose 'noli'. 'omnia magno… metu', 'all things with great fear', framing. 'extollere vires gentis bis victae', 'to exalt the strength of a twice-conquered people': Troy fell twice, to Hercules in Laomedon's time and to the Greeks. 'contra premere', 'by contrast to belittle', 'arma Latini', the king's side. Elisions 'Proind(e) omnia', 'met(u) atque', 'atqu(e) extollere', 'premer(e) arma'."""),
(405, 'undas.',
 """Now even the Myrmidons' chiefs at Phrygian arms tremble,\nnow even the son of Tydeus and Larissaean Achilles,\nand the river from the Adriatic backwards flees, Aufidus, the waves.""",
 """Now, no doubt, the chiefs of the Myrmidons quake at Trojan arms, now Tydeus's son and Achilles of Larissa quake too, and the river Aufidus runs backward in flight from the Adriatic waves.""",
 """Sarcasm: if Drances is right, the world is upside down. 'Nunc et', 'now even'. The Myrmidons were Achilles' men; 'Phrygia arma', the Trojans'. 'Tydides', 'son of Tydeus', Diomedes, who has just refused to fight Aeneas (225–295). 'Larissaeus', from Larissa in Thessaly, Achilles' country. 'amnis… Aufidus', a river of Apulia, Diomedes' new home, flowing into the Adriatic; a river running back to its source is a proverbial impossibility. Elision 'Phrygi(a) arma'."""),
(407, 'acerbat.',
 """Or when himself afraid against my abuse he pretends,\nthe crime of a schemer, and with fear the charge makes bitter.""",
 """Or then, when the scheming villain pretends to be frightened of my railing, and by his fear makes the accusation sharper.""",
 """A loose, angry construction: 'Vel cum', 'or (look) when', a fresh example of Drances' tricks, with no main clause. 'se pavidum… fingit', 'pretends himself afraid', as Drances did at 348 ('licet arma mihi mortemque minetur'). 'contra mea iurgia', 'in the face of my abuse'. 'artificis scelus', 'the villain of a trickster', 'scelus' 'crime' used of a person, an abusive idiom of comedy. 'formidine crimen acerbat', 'he sharpens the charge with his fear': pretending to fear Turnus makes Turnus look a tyrant. No elisions."""),
(409, 'isto.',
 """Never a soul such by this right hand, cease to be troubled,\nwill you lose: let it dwell with you and be in that breast.""",
 """Never will you lose such a soul as yours by this right hand of mine (put away your alarm): let it live on with you and stay in that breast of yours.""",
 """'animam talem', 'such a soul', with contempt: a soul not worth the taking. 'dextra hac', 'by this right hand', ablative of means. 'absiste moveri', 'cease to be disturbed', a mocking parenthesis. 'amittes', 'you will lose', the future, held to the next line. 'habitet… sit', jussive subjunctives: let it stay where it belongs. 'pectore in isto', 'in that breast of yours', 'iste' again contemptuous. Elisions 'Numqu(am) animam', 'dextr(a) hac', 'pector(e) in'."""),
(410, 'revertor.',
 """Now to you and your great, father, proposals I return.""",
 """Now, father, I come back to you and to your weighty proposals.""",
 """Turnus turns from Drances to Latinus. 'pater', 'father', a respectful address to the king, who is also the father of his promised bride. 'tua magna… consulta', 'your great proposals', the land and ships offered to the Trojans (316–334), the adjective and noun around the vocative. 'revertor', deponent, 'I return'. Elision 't(e) et'."""),
(414, 'inertis.',
 """If no further hope in our you place arms,\nif so deserted we are and, once the column turned,\nutterly we have fallen and Fortune has no return? —\nlet us beg for peace and hands let us stretch out helpless.""",
 """If you place no further hope in our arms, if we are so forsaken and utterly lost because our line broke once, and Fortune has no way back? — then let us pray for peace and hold out our hands, defenceless.""",
 """The print sets a question mark after 'regressum' and goes on with a small 'oremus'. This is not a clear misprint: Greenough lets the three 'si'-clauses rise to an indignant question before the answer, so it is kept as printed, and the reading text marks the turn with a dash. 'ultra', 'any longer'. 'semel agmine verso', ablative absolute, 'the line once turned', one defeat. 'neque habet Fortuna regressum', 'and Fortune has no way back'. 'oremus… tendamus', hortatory subjunctives. 'dextras… inertis', 'hands without weapons', the suppliant's gesture. Elision 'nequ(e) habet'."""),
(415, 'adesset!',
 """And yet, O, if anything of our usual valour were present!""",
 """And yet, oh, if only there were anything left of our old courage!""",
 """'Quamquam', 'and yet', correcting what has just been said: Turnus cannot bring himself to accept surrender. 'O si… adesset', a wish for the present that cannot be fulfilled, the imperfect subjunctive. 'quicquam… virtutis', 'anything of valour', the partitive genitive. 'solitae', 'accustomed', the courage the Latins used to have. No elisions."""),
(418, 'momordit.',
 """That man to me before others both fortunate in his toils\nand outstanding in spirit, who, so that not anything such he should see,\nfell dying and the ground once with his mouth bit.""",
 """In my eyes that man is blessed in his labours beyond all others, and noblest in spirit, who fell dying, once and for all biting the earth, rather than see such a thing.""",
 """'mihi', 'to me', 'in my judgement', the ethic dative. 'fortunatus laborum', 'fortunate in his toils', a genitive of respect after the Greek model; 'egregius animi', 'outstanding in spirit', 'animi' an old locative-genitive. 'nequid tale videret', a purpose clause, 'so as not to see any such thing', printed as one word ('ne quid'). 'humum… ore momordit', 'bit the ground with his mouth', the Homeric picture of a warrior falling face down (Iliad II.418, from memory). Elisions 'mih(i) ante', 'ant(e) alios', 'egregiusqu(e) animi'."""),
(423, 'tempestas:',
 """But if both resources to us and still untouched youth\nand for help Italian cities and peoples remain,\nbut if even for the Trojans with much glory has come\nblood, there are for them their own deaths, and equal over all\nthe storm:""",
 """But if we still have resources and young men untouched by war, and cities and peoples of Italy remain to help us, and if the Trojans too have won their glory at the cost of much blood (they have their own dead, and the same storm has passed over all):""",
 """'Sin', 'but if', the other side of 411: two 'sin' clauses balance the earlier 'si' clauses. 'opes nobis… supersunt', 'resources remain to us', dative of possession. 'auxilio', 'for help', dative of purpose. 'cum multo… sanguine', 'with much blood', framing 'gloria venit'. 'sunt illis sua funera', 'they have their own deaths', 'illis', dative of possession. 'parque per omnis tempestas', 'and the storm (went) equally through all', the verb left out; 'omnis', '-is' accusative plural. Elision 'auxilioqu(e) urbes'."""),
(424, 'deficimus?',
 """why, inglorious, on the threshold first\ndo we fail?""",
 """why do we lose heart so shamefully on the very threshold?""",
 """The question answers the long 'sin' clauses. 'indecores', 'without honour', an adjective used for the manner, 'shamefully'. 'in limine primo', 'at the first threshold', at the beginning of the struggle, as if they were turning back at the door. 'deficimus', 'we fail, lose heart', held over to the next line for weight. No elisions."""),
(424, 'artus?',
 """Why before the trumpet trembling seizes our limbs?""",
 """Why does trembling seize our limbs before the trumpet has even sounded?""",
 """A second 'cur', in parallel, an anaphora. 'ante tubam', 'before the trumpet', before the signal for battle has been given. 'tremor occupat artus', 'trembling takes hold of our limbs', the physical sign of fear, a phrase of epic. Turnus turns the charge of cowardice back on the whole council. No elisions."""),
(427, 'locavit.',
 """Many things the day and with varied (turns) the toil of changeable time\nhas brought back to better, many, alternately revisiting,\nhas mocked and on the solid again Fortune has set.""",
 """Many a time the passing days and the shifting toil of changing time have turned things for the better; Fortune comes back by turns to many she has mocked and sets them again on firm ground.""",
 """The print has 'variisque', which is hard to construe; the Latin Library reads 'variique', 'and the toil of varied, changeable time'. The print is kept, read as 'with its varied turns'; either way the sense is the same. 'Multa', neuter plural object, 'many things'. 'dies', feminine here, 'time, the passing of days'. 'rettulit in melius', 'brought back to better'. 'alterna revisens', 'revisiting by turns'. 'lusit', 'made sport of'. 'in solido', 'on solid ground', the opposite of Fortune's wheel. No elisions."""),
(431, 'agris.',
 """Not will be for help to us the Aetolian and Arpi:\nbut Messapus will, and fortunate Tolumnius, and those whom\nso many peoples have sent, leaders, nor small will follow\nglory the chosen from Latium and the Laurentine fields.""",
 """The Aetolian and his Arpi will be no help to us: but Messapus will, and lucky Tolumnius, and the leaders sent by so many peoples, and no small glory will attend the chosen men of Latium and the fields of Laurentum.""",
 """'erit auxilio nobis', 'will be for a help to us', the double dative, singular with two subjects. 'Aetolus', Diomedes, called Aetolian after his father's country (as at 239); 'Arpi', the city he founded in Apulia. Messapus led a contingent in VII.691–705; Tolumnius is the augur who will break the truce at XII.258. 'misere' = 'miserunt', the perfect in '-ere'. 'delectos', 'the chosen men', the picked forces. 'Laurentibus agris', of Laurentum, Latinus's city. Elision 'Lati(o) et'."""),
(433, 'catervas.',
 """There is also from the Volscians' outstanding race Camilla,\na column driving of horsemen and flowering with bronze troops.""",
 """We have Camilla too, of the noble race of the Volscians, leading a column of horse and squadrons gleaming with bronze.""",
 """'Est et', 'there is also', the name kept to the end of the line. Camilla, the warrior maiden of the Volsci, closed the catalogue of Italian forces in VII.803–817 and will have her great scenes later in this book. 'agmen agens', 'driving a column', the noun and verb from the same root. 'florentis aere catervas', 'troops flowering with bronze', bright armour pictured as blossom; 'florentis', '-is' accusative plural. No elisions."""),
(437, 'recusem.',
 """But if me alone the Teucrians into combat call,\nand this pleases, and so much the common good I stand in the way of,\nnot so much these, hating them, hands Victory has fled,\nthat for so great anything a hope to attempt I should refuse.""",
 """But if the Trojans challenge me alone to combat, and you are content with that, and I am so great an obstacle to the common good, Victory has not so hated and fled these hands of mine that I would refuse any venture for so great a prize.""",
 """Turnus answers Drances' challenge (373–375). 'me solum… poscunt', 'demand me alone'. 'idque placet', 'and that is agreed', by the council. 'tantum… obsto', 'I stand so much in the way', with the dative 'bonis communibus'. 'exosa', perfect participle of the deponent 'exosus', 'having hated', active in sense. 'non adeo… ut… recusem', a result clause, 'not so far… that I should refuse'. 'pro spe', 'for (so great) a hope'. Victoria is a goddess here, as at Rome. Elisions 'Teucr(i) in', 'ade(o) has'."""),
(440, 'licet.',
 """I will go with spirit against him, even if great he should play Achilles\nand made by Vulcan's hands equal should put on arms,\nhe, though he may.""",
 """I will go against him boldly, even if he should prove a great Achilles and put on armour like his, made by the hands of Vulcan.""",
 """'Ibo animis contra', 'I will go against (him) with courage', 'animis' plural for spirit. 'vel… licet', 'even though', 'licet' with the subjunctive, held to the end of the sentence. 'praestet', 'show himself as, equal'. Achilles' armour was made by Hephaestus (Iliad XVIII, from memory); Aeneas's by Vulcan at Venus's request (VIII.608–731), which Turnus has not yet faced. 'paria', 'matching (Achilles')'. 'ille', Aeneas, unnamed, held back for emphasis. Elision 'Ib(o) animis'."""),
(442, 'devovi.',
 """To you this life and to my father-in-law Latinus\nI, Turnus, not to any of the men of old in valour second,\nhave devoted.""",
 """To you and to Latinus, my father-in-law, I, Turnus, second to none of the heroes of old in valour, have vowed this life of mine.""",
 """The print has an opening double mark before 'devovi', a stray mark, since no new speech begins here; it is left out of the reading text. 'Vobis… soceroque Latino', datives, 'to you and to my father-in-law'; 'socer' anticipates the marriage. 'Turnus ego', the proud name. 'devovi', 'I have devoted', the Roman 'devotio', in which a general vowed his life to the gods below in exchange for victory, as the Decii did. Elisions 'anim(am) hanc', 'eg(o) haud'."""),
(444, 'tollat.”',
 """Me alone Aeneas calls: and let him call, I pray,\nand not Drances rather, whether this is the anger of the gods,\nwith death atone, or whether it is valour and glory, carry it off.”""",
 """Aeneas calls on me alone: then let him call, I pray, and let it not be Drances rather than I who, if this is the anger of the gods, pays for it with his death, or, if it is valour and glory, carries off the prize.”""",
 """'Solum', 'me alone', the object of 'vocat'. 'et vocet oro', 'and let him call, I pray', 'oro' standing alone with the subjunctive. 'nec Drances potius… luat… tollat', 'and let Drances not rather (than I)… atone or… take (the glory)'. The two 'sive' clauses cover both outcomes: if the gods are angry, Turnus will pay with his life; if there is glory to win, it will be his. 'morte luat', 'atone with death'. Elisions 'Solu(m) Aeneas', 'siv(e) est' twice."""),
]

# Speech-mark check exemptions (rule 5b / doubtful marks), by unit ln:
#  399: the print opens a quotation at 'Nulla salus bello' (Turnus quoting Drances, 362) and never closes it;
#       l and i mark just those three words with single marks, so the double-mark counts differ.
#  440: the print sets a stray opening mark before 'devovi' (442) with no speech beginning; l and i omit it.
EXEMPT = {399, 440}
P = A.part('aeneid-085'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
