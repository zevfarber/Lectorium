import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..')); sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..'))
import aeneid_lib as A
# aeneid-052 draft. Drafted from the Latin and grammar only. t is cut from the edition, never typed.
TITLE = 'Iuno irata. Allecto. Amata'
TITLE_EN = "Juno Summons Allecto — Aeneid VII.286–372"
PART = "Juno Summons Allecto (VII.286–372)"
ABOUT = """Juno, returning through the air from Argos, sees far off the Trojans glad and settled in Latium, building houses and trusting the land, their ships abandoned. Stung, she pours out her anger. The Trojans could not be killed at Sigeum, could not be held captive when captured, were not burned when Troy burned; she hounded them over every sea, spent the powers of sky and sea, set the Syrtes, Scylla and Charybdis against them, and now they rest in the Tiber, unafraid of the sea or of her. Mars destroyed the Lapiths and Jupiter gave Calydon to Diana's anger for far less; she, the great wife of Jove, is beaten by Aeneas. If the gods above will not help her she will rouse the underworld. She cannot keep Aeneas from the kingdom or from Lavinia, but she can delay it all and destroy both peoples: the bride's dowry will be Trojan and Rutulian blood, Bellona will attend the wedding, and Venus's son will be a second Paris, a firebrand for the new Troy. She comes down to earth and calls up from the dark the Fury Allecto, hated by Pluto and her own sisters, and charges her to wreck the peace and set the young men clamouring for war. Allecto goes first to Latinus's palace, where Queen Amata is already fretting over the Trojans' coming and the marriage of Turnus. The Fury throws one of her snakes into the queen's breast; it glides unfelt over her body, becomes her necklace and the ribbon of her headdress, and breathes its venom into her. Before the madness has taken hold, Amata pleads with Latinus, still gently and in tears: will he give their daughter to an exile who will sail off with her as Paris sailed off with Helen, and break his word to their kinsman Turnus? If the oracle wants a foreign son-in-law, every land outside their rule is foreign, and Turnus, descended from Inachus and Acrisius, comes from the heart of Greece."""
U = [
(289, 'Pachyno.',
 """But look: from Inachian Argos was bringing herself back
the savage consort of Jove, and, borne along, was holding to the airs,
and glad Aeneas and the fleet, from the upper sky, far off,
the Dardanian fleet, all the way from Sicilian Pachynus, she spied.""",
 """But now Jove's fierce consort was on her way back from Argos, the city of Inachus, riding through the air, when from high in the sky, as far off as Pachynus in Sicily, she caught sight of Aeneas in his gladness and the Dardanian fleet.""",
 """A new paragraph in Greenough. 'Ecce autem', 'but look', turns the story sharply, a favourite epic transition. 'Inachiis… ab Argis': Argos, a plural noun in Latin ('Argi'), is 'Inachian' from Inachus, river-god and first king there; it was Juno's own city, 'dear' to her (1.24). 'Sese referebat', 'was carrying herself back', 'was returning'. 'Invecta', 'borne along' (in her chariot), and 'auras… tenebat', 'was holding her way through the air'. 'Aenean' is a Greek accusative. 'Ab usque Pachyno', 'all the way from Pachynus', the south-eastern cape of Sicily (3.699), puts 'ab' before 'usque', the reverse of the usual 'usque ab'. Virgil does not explain how she sees Latium from so far: the distance shows a goddess's sight. 'Prospexit' is perfect after the imperfects: the sudden act against the background."""),
(291, 'dolore.',
 """building now their houses she sees them, now trusting the land,
having deserted their ships: she stood, transfixed with sharp pain.""",
 """She sees them already at work on houses, already trusting the land, their ships left behind; and she stood still, transfixed by bitter pain.""",
 """Three infinitives depend on 'videt', 'she sees', in accusative and infinitive with the subject ('eos', 'them') left out; the asyndeton and the repeated 'iam… iam' give her view in quick strokes. 'Moliri' is deponent, 'to build with effort', 'to set about building'. 'Fidere' takes the dative 'terrae', 'to trust the land'. 'Deseruisse' is perfect: the ships are already left behind, a settler's act. 'Stetit… fixa' is 'stood fixed', 'transfixed', with 'acri… dolore', 'with sharp pain', framing 'fixa'. Juno's 'dolor', resentment, is the word of the poem's opening ('quidve dolens', 1.9; 'saevique dolores', 1.25)."""),
(292, 'dicta:',
 """Then, shaking her head, these from her breast she pours out, words:""",
 """Then, shaking her head, she poured out these words from her heart:""",
 """'Quassans caput', 'shaking her head', in anger; 'quasso' is the frequentative of 'quatio', 'shake again and again'. 'Haec… dicta' goes round 'effundit pectore', 'she pours out from her breast': the words come in a rush. 'Effundit' is a historic present. Her first speech in the poem, also a soliloquy, was introduced with the verb of speaking left out, 'haec secum' (1.37); the speech that follows (293–322) deliberately recalls that one."""),
(294, 'Phrygum !',
 """“Alas, the hated stock, and to our fates opposed
the fates of the Phrygians!""",
 """“Oh, that hated breed, and the destiny of the Phrygians, set against my own destiny!""",
 """The print has 'fata Phrygum ! Num', with a space before the exclamation mark, a misprint for 'fata Phrygum! Num', corrected here; t keeps the print, because t must match the pinned source. Juno's speech opens (293–322). 'Stirpem' and 'fata' are accusatives of exclamation after 'heu', 'alas for…'. 'Invisam', 'hated', recalls 'genus invisum' among her grievances at 1.28. 'Fatis… nostris' is dative with 'contraria', 'opposed to our fates'; 'nostris' is the plural for the singular, 'my'. Setting 'fatis' against 'fata' states her problem in two words: Troy's destiny runs against hers. 'Phrygum' is the genitive plural of 'Phryges', 'Phrygians', a common name for the Trojans and often a contemptuous one."""),
(296, 'viros ?',
 """Could they on the Sigean plains fall?
could they, captured, be captured? did, set on fire, burn up
Troy its men?""",
 """Could they be killed on the plains of Sigeum? Once captured, could they be held captive? When Troy was set ablaze, did it burn up its men?""",
 """The print has 'Troia viros ? Medias', with a space before the question mark, a misprint for 'Troia viros? Medias', corrected here; t keeps the print, because t must match the pinned source. Three questions with 'num' expect the answer 'no', and that answer is the scandal: they could not be destroyed. 'Sigeis… campis', 'on the Sigean plains', the Trojan plain by the headland of Sigeum (compare 'Sigea… freta', 2.312). 'Occumbere', 'to fall', 'to meet death'. 'Potuere' is '-ere' for '-erunt' (so 'invenere' next). 'Capti… capi' plays on one verb: taken, they would not stay taken. Virgil is echoing Ennius's Annales, as Macrobius reports the lines: 'nec cum capta capi nec cum combusta cremari', 'neither to be taken when taken nor burned when burned'. 'Incensa… Troia', 'Troy set on fire', is spread over the line-end."""),
(297, 'viam.',
 """Through the midst of battle lines and the midst of fires
they found a way.""",
 """Through the thick of the fighting and through the heart of the flames they found a way out.""",
 """'Per' governs both 'acies' and 'ignis', though it stands only before the second; 'ignis' is the '-is' accusative plural. 'Medias… medios', 'the middle of', is the Latin idiom: 'medius' agrees with its noun where English says 'the midst of', and the repetition (anaphora) presses the point. 'Invenere' is '-ere' for '-erunt'. The sentence is short and flat after the three questions: the plain fact. Aeneas's escape through the burning city, with the gods opening the way, is the story of Book II."""),
(298, 'quievi.',
 """But, I suppose, my divine powers at last
lie weary, with hatreds, or glutted I have rested.""",
 """But no doubt my divine power has at last grown weary and lies idle, or I have had my fill of hatred and given up.""",
 """'Credo', 'I suppose', 'no doubt', set in parenthesis, is ironic: she means the opposite. 'Numina' is her divine will and power, the plural used for the singular, as often in verse. 'Odiis', 'with hatreds', can go with 'fessa', 'tired out by hatred', or with 'exsaturata', 'glutted with hatred', or with both. The subject shifts from 'numina' ('iacent', 'lie') to Juno herself ('quievi', 'I have rested'), and 'exsaturata', a perfect participle, agrees with that 'I'. Venus had called Juno's heart 'nec exsaturabile', 'never to be glutted' (5.781); Juno's sarcasm proves her right."""),
(300, 'ponto !',
 """Why, even, from their fatherland driven out, hostile, through the waves
I dared to follow them, and against the fugitives over the whole sea to set myself!""",
 """Why, when they were driven from their homeland I even dared to hunt them over the waves, and to bar the fugitives' way across the whole sea!""",
 """The print has 'opponere ponto !', with a space before the exclamation mark, a misprint for 'opponere ponto!', corrected here; t keeps the print, because t must match the pinned source. 'Quin etiam', 'why, even', 'what is more', caps the argument. 'Ausa' is 'ausa (sum)', 'I dared', with the auxiliary left out; 'audeo' is semi-deponent, active in sense with a passive-form perfect. 'Excussos', 'shaken out', 'driven out', agrees with the understood object 'eos'; 'patria' is ablative of separation, 'from their fatherland'. 'Infesta', 'hostile', agrees with Juno. 'Profugis' is dative with 'opponere', 'to set myself against the fugitives'. 'Toto… ponto', 'over the whole sea', is ablative of place without 'in', usual with 'totus'. Aeneas was 'fato profugus' in the poem's second line (1.2)."""),
(301, 'marisque.',
 """Spent against the Teucrians are the forces of both sky and sea.""",
 """The forces of sky and sea alike have been used up against the Trojans.""",
 """'Absumptae (sunt)', 'have been used up', with the verb 'to be' left out, as often. 'In Teucros' is 'against the Teucrians', 'in' with the accusative of hostility. 'Caelique marisque', 'both of sky and of sea', with double '-que', sums up what she has spent: the storm she raised through Aeolus in Book I, and the burning of the ships she brought about through Iris in Book V (5.606). 'Teucri', 'Teucrians', from Teucer, an early king of the Troad, is one of Virgil's commonest names for the Trojans. The line is a single flat statement between two outbursts."""),
(303, 'profuit?',
 """What the Syrtes or Scylla to me, what huge Charybdis
has profited?""",
 """What good to me were the Syrtes or Scylla, what good the vast gulf of Charybdis?""",
 """'Quid… profuit' is 'what good did (it) do', 'quid' an internal (adverbial) accusative with 'prosum', and 'mihi' dative, 'to me'. The verb is singular and is understood with each subject in turn; 'quid' is repeated (anaphora). The Syrtes are the shoals off the North African coast, onto which the storm of Book I drove ships (1.111). Scylla and Charybdis, the monster and the whirlpool of the Straits of Messina, are the dangers Helenus warned Aeneas against (3.420–432); the Trojans rowed clear of Charybdis (3.558–560). Juno counts them all as her weapons, and none served."""),
(304, 'mei.',
 """In the longed-for they bury themselves, the Tiber's bed,
unconcerned with the sea and with me.""",
 """They lie snug in the bed of the Tiber they longed for, with no more fear of the sea or of me.""",
 """'Conduntur' is passive in form with a reflexive sense, 'they hide themselves', 'they settle in'. 'Optato… alveo', 'in the longed-for bed', is ablative of place without a preposition, and goes round 'conduntur Thybridis'. 'Thybris' is a poetic, Greek-looking name for the Tiber. 'Securi', 'free from care', takes the genitive: 'pelagi', 'about the sea', and 'mei', the genitive of 'ego', 'about me'. Ranking herself beside the sea as one more danger now past is the bitterest touch."""),
(307, 'merentem?',
 """Mars to destroy the race
huge of the Lapiths had the power; gave over to the wrath
himself the father of gods ancient Calydon of Diana —
what crime so great, on the Lapiths' part or Calydon's, deserving?""",
 """Mars could destroy the mighty race of the Lapiths; the father of the gods himself gave ancient Calydon over to Diana's anger — and what crime so great had the Lapiths or Calydon committed to deserve it?""",
 """Two precedents. 'Valuit', 'had the power', takes the infinitive 'perdere'; 'Lapithum' is the old genitive plural in '-um'. The Lapiths of Thessaly fought the Centaurs at the wedding of their king Pirithous; Servius says Mars, left out of the invitations, stirred the fight. Calydon in Aetolia suffered when King Oeneus forgot Diana in his sacrifices and she sent the great boar. 'Concessit in iras… Dianae', 'gave (it) up to Diana's wrath'; 'deum' is genitive plural with 'genitor', Jupiter. 'Calydona' is a Greek accusative. 'Quod scelus… tantum… merentem', 'deserving (for) what crime so great?'. Greenough prints 'Lapithis', which can be construed only loosely, as a dative 'on the Lapiths' part'; the Latin Library prints 'Lapithas', accusative beside 'Calydona' with 'merentem'. The sense is the same, and the print is kept."""),
(310, 'Aenea.',
 """But I, the great consort of Jove, who nothing to leave undared
have brought myself, unhappy, who myself to every shift have turned,
am beaten by Aeneas.""",
 """But I, the great wife of Jupiter, who in my misery have left nothing undared, who have turned my hand to every device — I am beaten by Aeneas.""",
 """'Ast' is an old form of 'at', 'but', kept for solemn speech. The opening echoes Juno's first soliloquy, 'Ast ego, quae divom incedo regina, Iovisque / et soror et coniunx' (1.46–47): the same outrage, now at the voyage's end. 'Quae potui… quae… verti' are relative clauses with first-person verbs, agreeing with 'ego'. 'Potui', 'I have been able', 'I could bring myself', takes 'linquere'; 'inausum', 'undared', is predicative: 'to leave nothing undared'. 'Infelix', 'unhappy (that I am)', agrees with the 'I'. 'Memet' is 'me' strengthened with '-met'. 'In omnia verti', 'I have turned myself to every means'. 'Aenea' is the ablative of 'Aeneas', with 'ab' of the agent. After two long relative clauses, 'vincor ab Aenea' falls short and hard at the start of the line."""),
(311, 'est:',
 """But if my divine powers are not
great enough, I would not hesitate, for my part, to call on whatever anywhere exists:""",
 """And if my own divinity is not great enough, I for one will not shrink from calling on any power there is, wherever it may be:""",
 """'Quod si', 'but if', 'now if': 'quod' is the connective often used before 'si'. 'Dubitem haud' is a potential subjunctive, 'I would not hesitate'; 'haud' set after its verb is unusual and puts weight on the refusal. 'Equidem', 'for my part', 'I for one', goes with a first-person verb, as usual. 'Quod usquam est', 'whatever exists anywhere', is the object of 'implorare', 'to call on for help'; it is deliberately vague, and the next line says where she means. 'Numina' is again the plural for her divine power (297). The colon looks forward: what follows explains this line."""),
(312, 'movebo.',
 """to sway if I am unable those above, Acheron I shall set moving.""",
 """If I can bring no god above round to my side, I shall rouse the world of the dead.""",
 """Juno's most quoted line. 'Flectere', 'to bend', 'to sway', is the word for winning a god over by prayer; 'nequeo', 'I am unable', takes the infinitive. 'Superos', 'those above', the gods of heaven, stands against 'Acheronta', the Greek accusative of 'Acheron', a river of the underworld standing for the powers below. 'Movebo' is future, 'I will set in motion', 'I will stir up'. The order puts the condition first and keeps the threat for the end of the line. The line explains what follows: she will not appeal to Olympus but call a Fury up from the dark (323–326). Freud set the line as the motto of his Interpretation of Dreams (1900)."""),
(314, 'coniunx:',
 """It will not be granted — so be it — to bar him from the Latin kingdom,
and fixed by the fates stands Lavinia as his wife:""",
 """I shall not be allowed — very well — to keep him from the throne of Latium, and by the fates' decree Lavinia stays his bride, past changing:""",
 """Juno concedes what she cannot change. 'Non dabitur' is impersonal, 'it will not be granted (to me)', with the infinitive 'prohibere', 'to keep (him) from', as its subject; 'regnis… Latinis', 'from the Latin kingdom' (plural for singular), is ablative of separation and frames the clause. 'Esto', the future imperative of 'sum', 'so be it', is a grudging concession. 'Immota', 'unmoved', 'fixed', with 'fatis', 'by the fates'; 'manet', 'remains'. 'Lavinia coniunx', 'Lavinia as his wife', with 'coniunx' predicative. Lavinia is Latinus's only child (7.52), promised by Faunus's oracle to a son-in-law from abroad (7.96–98)."""),
(316, 'regum.',
 """but to drag it out and to add delays to such great matters is allowed,
but it is allowed to root out the peoples of both kings.""",
 """but I may still drag it out and put delays in the way of such great events; I may still destroy the peoples of both kings.""",
 """'At… at', 'yet… yet', in anaphora, set what she can do against what she cannot. 'Licet' is impersonal, 'it is allowed', with infinitives as its subject: 'trahere', 'to drag out', 'to protract', and 'moras… addere', 'to add delays', with 'tantis… rebus' dative after 'addere'. 'Exscindere', 'to cut out', 'to destroy root and branch', is a strong word, used of cities and peoples. 'Amborum… regum', 'of both kings', Latinus and Aeneas: the war is to fall on both nations. In two lines Juno sets out the plot of the poem's second half."""),
(317, 'suorum:',
 """At this price let son-in-law and father-in-law come together, the price of their own:""",
 """Let son-in-law and father-in-law join hands, then, at this price, paid by their own people:""",
 """'Coeant' is a jussive subjunctive, 'let them come together', in alliance. 'Hac… mercede', 'at this price', is ablative of price, and 'suorum', 'of their own (people)', depends on it: the price is their subjects' lives. 'Gener atque socer' are Aeneas and Latinus. The pair carried a Roman memory: Caesar and Pompey were father-in-law and son-in-law before civil war, and Anchises calls them 'socer' and 'gener' at 6.830–831."""),
(319, 'pronuba.',
 """with blood Trojan and Rutulian you will be dowered, maiden,
and Bellona awaits you as bride's attendant.""",
 """Your dowry, girl, will be Trojan and Rutulian blood, and Bellona waits to attend you as bride.""",
 """Juno turns to address Lavinia, who is not present (apostrophe). 'Dotabere' is the second person singular future passive of 'doto', 'endow', with '-re' for '-ris': 'you will be dowered'; 'sanguine' is ablative of means. The Rutulians are Turnus's people, of Ardea (7.409–411). 'Manet' is 'awaits', with 'te' as object. Bellona is the Roman goddess of war. A 'pronuba' was the married woman who attended the bride and joined the couple's hands; Juno, goddess of marriage, was herself 'pronuba' at Dido's union (4.166). Here she hands the office to war."""),
(322, 'taedae.”',
 """Nor with a torch only
Cisseus's daughter, pregnant, gave birth to marriage fires;
nay, the same to Venus is her own offspring, a second Paris,
and deadly once more, for a Pergamum reborn, the torches.”""",
 """Nor was Hecuba the only one to carry a firebrand in her womb and give birth to marriage fires; no, Venus has the same in her own son, a second Paris, and once more there will be torches of death for a Troy risen again.”""",
 """The print has no mark after 'iugalis', a misprint for 'iugalis;' (the sense needs a stop before 'quin'), corrected here; t keeps the print, because t must match the pinned source. 'Cisseis', a Greek patronymic, 'daughter of Cisseus', is Hecuba, Priam's queen, who when carrying Paris dreamed she gave birth to a firebrand (compare 10.704–705); 'face praegnans', 'pregnant with a torch'. 'Tantum', 'only', goes with 'Cisseis'. 'Enixa (est)', 'gave birth to', from the deponent 'enitor'; 'ignis… iugalis' is '-is' accusative plural, 'marriage fires': Paris, whose marriage burned Troy. 'Quin', 'nay rather'. 'Idem… partus suus', 'her own offspring (is) the same', with 'Veneri' dative: Aeneas. 'Recidiva… Pergama', 'Pergamum risen again', the new Troy. 'Taedae', pine torches, serve weddings and funerals alike. Juno's speech ends."""),
(323, 'petivit:',
 """These words when she had uttered, the earth, dread, she sought:""",
 """When she had said this, the dread goddess made for the earth:""",
 """The print has 'Horrenda', with a capital, a misprint for 'horrenda', corrected here; t keeps the print, because t must match the pinned source. A new paragraph in Greenough. 'Haec ubi dicta dedit', 'when she had given (uttered) these words', is a regular epic formula for closing a speech. 'Horrenda' is the gerundive used as an adjective, 'to be dreaded', 'dread', and stands for the goddess herself. 'Terras… petivit', 'made for the earth': she comes down from the sky to call up help from below. After her first speech she went in the same way to Aeolus (1.50–52); this time the help comes from the underworld."""),
(326, 'cordi.',
 """grief-bringing Allecto from the seat of the dread goddesses
and from the infernal darkness she calls up, to whom grim wars
and angers and ambushes and harmful charges are dear to the heart.""",
 """she calls up Allecto, bringer of grief, from the home of the dread goddesses and the darkness of the underworld, Allecto whose heart's delight is grim war, rage, treachery and harmful slander.""",
 """'Allecto', a Greek name in '-o', has the same form for nominative and accusative; here it is accusative, the object of 'ciet', 'summons', 'calls up'. She is one of the three Furies, Greek Erinyes, with Tisiphone (6.571) and Megaera (12.846); her name was taken to mean 'the unresting'. 'Dirarum… dearum', 'of the dread goddesses', the Furies, called 'Dirae' (12.845). 'Luctificam', 'grief-making', is a compound adjective in the old epic style. 'Infernis… tenebris', 'from the darkness below', goes with 'ab sede'. 'Cui… cordi (sunt)' is a double dative, 'to whom (they are) for a heart', 'dear to her'. 'Iraeque insidiaeque et' piles her pleasures up (polysyndeton). 'Crimina' here are accusations, quarrels."""),
(329, 'colubris.',
 """Hates her even the father himself, Pluto, hate her the sisters
of Tartarus, the monster: into so many faces she turns herself,
so savage her looks, with so many, black, she sprouts, snakes.""",
 """Father Pluto himself hates the monster, her own sisters in Tartarus hate her: she changes into so many shapes, her looks are so savage, she bristles black with so many snakes.""",
 """'Odit… odere' (anaphora), 'hates… hate'; 'odere' is '-ere' for '-erunt', and 'odi' is a perfect with present meaning. 'Et' is 'even'. 'Pater Pluton', 'father Pluto', king of the underworld; 'pater' is a title of honour for a god, not a claim that he begot her (she is 'sata Nocte', 331). 'Pluton' is the Greek nominative. 'Sorores… Tartareae' are the other Furies; Tartarus is the underworld's prison of the damned. 'Monstrum', the object of both verbs, is held back to the next line. 'Tot… tam… tot' build the description. 'Ora' are faces, shapes. 'Pullulat… colubris', 'she sprouts with snakes', ablative of means; 'atra', 'black', agrees with her."""),
(330, 'fatur:',
 """Her Juno with these words whets, and such things says:""",
 """Juno sharpens her for the work with these words, speaking thus:""",
 """'Quam' is a connecting relative, 'her', standing for 'eam' at the start of a sentence. 'Acuit', 'whets', 'sharpens', as a blade is sharpened, is present here like 'fatur': Allecto's rage is to be given an edge. 'His… verbis' and 'talia fatur' say the same thing twice, a common epic doubling. 'Fatur' is from the deponent 'for, fari', 'speak', used mainly in verse."""),
(334, 'finis.',
 """“This give me as my own, maiden sprung from Night, as a labour,
this service, that my honour, or, broken, my
fame may not give way from its place, nor by marriages to win round Latinus
the sons of Aeneas be able, or to occupy the Italian borders.""",
 """“Maiden born of Night, take on this labour for me alone, this one service, so that my honour and good name are not broken and forced to give ground, and the sons of Aeneas cannot win Latinus round with a marriage or take hold of the land of Italy.""",
 """Juno's speech to Allecto opens (331–340). 'Proprium', 'as my own', 'for me alone': a task done for Juno and no other. 'Virgo sata Nocte', 'maiden sprung from Night', 'sata' perfect participle of 'sero', 'sow', 'beget', with 'Nocte' ablative of origin; Night is the Furies' mother (12.846). 'Ne… cedat… neu… possint' is a negative purpose clause, 'so that… may not', with 'neu' continuing it. 'Honos' is the older form of 'honor'; 'noster' is the plural for 'my'. 'Infracta', 'broken', agrees with 'fama'; '-ve', 'or'. 'Cedat loco', 'give ground', a soldier's phrase. 'Conubiis', 'by marriages', plural for one marriage, ablative of means; 'ambire', 'to go round', to canvass and win over, as a candidate does voters. 'Aeneadae', the sons of Aeneas, his people. 'Finis' is the '-is' accusative plural."""),
(338, 'artes.',
 """You can like-minded arm for battles brothers
and with hatreds overturn houses, you lashes into homes
and funeral torches can bring, to you are names a thousand,
a thousand arts of harming.""",
 """You can arm brothers who are of one heart and send them into battle, and overturn households with hatred; you can bring the lash and the funeral torch under men's roofs; you have a thousand names, a thousand ways of doing harm.""",
 """'Tu… tu… tibi', anaphora of the second person, is the style of a hymn listing a god's powers: Juno flatters as she commands. 'Unanimos', 'of one mind', makes the brothers' quarrel the worse; the Theban brothers Eteocles and Polynices are the famous case. 'In proelia', 'for battles'. 'Odiis', ablative of means, 'with hatreds'; 'versare', 'to overturn', 'to wreck'. 'Tectis' is dative with the compound 'inferre', 'to bring into homes'; 'verbera' are 'lashes', the Fury's whip, and 'funereas… faces' the torches of funerals. All the infinitives depend on 'potes'. 'Tibi nomina mille' is a dative of possession, 'you have a thousand names' ('sunt' understood), and 'mille… artes' continues it. 'Nocendi', genitive of the gerund, 'of harming'."""),
(340, 'inventus.”',
 """Your fertile shake out breast,
scatter the settled peace, sow the charges of war:
arms let them want and demand at once and seize, the young men.”""",
 """Shake out the schemes your teeming heart holds, shatter the peace they have made, sow grievances that will end in war; let the young men want weapons, call for them and seize them, all at once.”""",
 """The print has 'inventus', a misprint for 'iuventus', 'the young men', corrected here; t keeps the print, because t must match the pinned source ('n' for 'u' is a common slip, and 'inventus', 'found', makes no sense here). 'Fecundum… pectus', 'your teeming breast', rich in evil; 'concute', 'shake out', as one shakes out a fold of a garment for what it holds. 'Disice' is Greenough's spelling of 'disiice', 'scatter', 'shatter'. 'Compositam', 'settled', 'agreed'. 'Sere' is the imperative of 'sero', 'sow'; 'crimina belli', 'charges that lead to war', pretexts. 'Velit poscatque… rapiatque' are jussive subjunctives, 'let (them) want… demand… seize', in rising order, with the collective 'iuventus' as subject; 'simul', 'at once'. Juno's speech ends."""),
(345, 'coquebant.',
 """Thereupon, with Gorgon venoms steeped, Allecto
first Latium and of the Laurentine ruler the dwelling
lofty seeks, and has beset the silent threshold of Amata,
whom, over the coming of the Teucrians and Turnus's marriage,
burning, a woman's cares and angers were seething.""",
 """Then Allecto, steeped in Gorgon poisons, makes first for Latium and the lofty palace of the Laurentine king, and takes her post at the silent threshold of Amata, who was already burning, fretted by a woman's anxieties and resentments over the coming of the Trojans and the matter of Turnus's marriage.""",
 """A new paragraph in Greenough. 'Exin' is a shortened form of 'exinde', 'thereupon'. 'Gorgoneis… venenis', 'with Gorgon poisons', ablative with 'infecta', 'steeped', 'tainted': the Gorgons had snakes for hair, and Allecto carries the same venom. 'Laurentis… tyranni' is genitive singular, 'of the Laurentine ruler', Latinus, whose city is Laurentum; 'tyrannus' is the Greek word for a ruler, with no bad sense (as at 266). 'Tecta… celsa', 'the lofty dwelling', spans the line-end. 'Obsedit', 'she has beset', a perfect among presents. 'Quam… ardentem', 'her, burning', is the object of 'coquebant'; 'super' with the ablative, 'about', 'over'. 'Teucrum' is the old genitive plural. 'Coquebant', 'were cooking', 'kept her seething', is a homely metaphor. Amata had been eager for Turnus as son-in-law (7.56–57)."""),
(348, 'omnem.',
 """At her the goddess, from her dark-blue locks, one snake
hurls, and into her bosom, to her inmost heart, slips it,
so that, maddened by this monster, she may throw her house into turmoil, all of it.""",
 """At her the goddess flings one snake from her dark tresses and slips it into the folds of her dress, down to her inmost heart, so that the creature may drive her wild and she may throw the whole palace into turmoil.""",
 """'Huic', 'at her', is dative with 'conicit', 'throws'. 'Caeruleis… de crinibus', 'from her dark locks', goes round 'unum'; 'caeruleus' is dark blue, or simply dark, the colour of snakes and of the underworld. 'Sinum' is the fold of the dress over the breast. 'Intuma' is Greenough's older spelling of 'intima', 'innermost', like 'maxumus'; in 'praecordia ad intuma', 'to her inmost heart', 'ad' stands between noun and adjective. 'Quo… monstro', 'by which monster', makes a relative clause of purpose with the subjunctive 'permisceat', 'so that by it she may throw into confusion'. 'Furibunda', 'raging', agrees with Amata. 'Domum… omnem', 'the whole house', is split across the verb."""),
(351, 'animam:',
 """It, between her clothes and smooth breast having glided,
rolls on, with no touch, and escapes the raging woman's notice,
breathing into her its viper's breath:""",
 """Gliding between her clothes and her smooth breast, it coils on without a touch that she can feel and goes unnoticed as her frenzy grows, breathing its viper's breath into her:""",
 """'Ille', 'it', is the snake ('anguis' is masculine here, as 'unum' showed). 'Lapsus' is the perfect participle of the deponent 'labor', 'having glided'. 'Levia' is from 'levis' with a long e, 'smooth', not 'levis' with a short e, 'light'. 'Volvitur', 'rolls', 'winds', is passive in form with a reflexive sense. 'Attactu nullo', 'with no touch', ablative of manner: she does not feel it. 'Fallit', 'escapes the notice of'; 'furentem', 'her, raging', looks ahead: the madness is already at work, and she does not know its cause. 'Vipeream… animam', 'viper's breath'; 'inspirans', 'breathing into (her)'. The colon introduces the snake's transformations."""),
(353, 'errat.',
 """becomes the twisted, on her neck,
gold the huge serpent, becomes of the long fillet the ribbon,
and binds her hair, and over her limbs, slippery, it wanders.""",
 """the huge serpent becomes the twisted gold collar at her throat, becomes the ribbon of her long headband, wreathes itself through her hair, and slides, slippery, over her limbs.""",
 """'Fit… fit' (anaphora): the snake 'becomes' the queen's ornaments. 'Tortile… aurum', 'twisted gold', is a torque or necklace, with 'collo', 'on her neck'. 'Coluber', 'serpent', is the subject, and 'ingens' agrees with it. 'Taenia', a Greek word, is a band or ribbon, here the hanging end of the 'vitta', the woollen fillet worn in a married woman's hair; 'longae… vittae' is genitive. 'Innectit', 'binds', 'twines into'. 'Membris', 'over her limbs'; 'lubricus', 'slippery', gives the snake's motion. The ornaments of a queen and matron are the snake's disguise, which is why she does not notice it."""),
(358, 'hymenaeis:',
 """And while the first infection, with moist venom slipped in,
pervades her senses and in her bones twines fire,
and not yet her mind in her whole breast has caught the flame,
rather gently and in the accustomed way of mothers she spoke,
much over her daughter weeping and the Phrygian marriage:""",
 """While the first infection, creeping in with its moist poison, was working through her senses and twining fire into her bones, and before her mind had caught the flame through all her heart, she spoke gently enough, as mothers do, weeping much over her daughter and the Phrygian marriage:""",
 """'Dum… pertemptat… implicat', 'while (it) pervades… twines', is 'dum' with the present for continuing action; 'necdum… percepit', 'and not yet has (her mind) taken in'. 'Lues', 'plague', 'infection'; 'sublapsa', 'having slipped in under', with 'udo… veneno', 'with its moist poison', framing it. 'Ossibus', 'in her bones', goes with 'implicat'. 'Mollius', 'rather gently', is the comparative meaning 'somewhat'; 'et' joins it to 'solito matrum de more', 'in the usual way of mothers', 'solito' agreeing with 'more'. 'Locuta est' is the perfect of the deponent 'loquor'. 'Multa… lacrimans', 'weeping much', 'multa' an internal (adverbial) accusative. 'Super nata', 'over her daughter', 'super' with the ablative; the Latin Library prints 'natae', 'over her daughter's Phrygian marriage', and the sense hardly changes. 'Hymenaeis' is the Greek word for marriage."""),
(360, 'tuique ?',
 """“To exiles is she given, to be led home as bride, Lavinia, to Teucrians,
O father, and have you no pity for your daughter and yourself?""",
 """“Is Lavinia to be handed over as a bride to Trojan exiles, father? Have you no pity for your daughter, or for yourself?""",
 """The print has 'gnataeque tuique ?', with a space before the question mark, a misprint for 'gnataeque tuique?', corrected here; t keeps the print, because t must match the pinned source. Amata's speech opens (359–372). '-ne' on the first word makes it a question, and putting 'exsulibus' first stresses her contempt: exiles, men without a country. 'Datur ducenda', 'is given to be led', is the gerundive of purpose with 'do'; 'ducere (uxorem)', 'to lead (a wife) home', is the regular term for a man marrying. 'Genitor', 'father', is Latinus as Lavinia's father. 'Miseret' is impersonal: the one who feels pity is accusative ('te'), and the objects of pity genitive ('gnatae', 'tui'). 'Gnatae' is Greenough's older spelling of 'natae'; 'tui' is the genitive of 'tu'."""),
(362, 'praedo?',
 """Nor for the mother have you pity, whom at the first north wind will leave
the faithless one, seeking the deep, with the maiden carried off, the robber?""",
 """Or for her mother, whom this faithless pirate will leave behind at the first north wind, making for the open sea with the girl he has stolen?""",
 """'Nec matris miseret (te)', 'nor do you pity the mother', 'matris' genitive as before; Amata means herself. 'Primo aquilone', 'at the first north wind', ablative of time: as soon as a wind offers he will sail off with his prize. 'Perfidus… praedo', 'the faithless robber', frames the line; Dido called Aeneas 'perfide' (4.305, 4.366), and the same charge now comes from another queen. 'Alta petens', 'seeking the deep', the open sea. 'Abducta virgine' is an ablative absolute, 'the maiden having been carried off'. The fear is groundless: Aeneas has come to stay, as 290–291 showed."""),
(364, 'urbes ?',
 """Or is it not so that the Phrygian made his way into Lacedaemon, the shepherd,
and Ledaean Helen to the Trojan cities carried off?""",
 """Was it not just so that the Phrygian shepherd found his way into Sparta and carried Helen, Leda's daughter, off to the cities of Troy?""",
 """The print has 'ad urbes ? Quid', with a space before the question mark, a misprint for 'ad urbes? Quid', corrected here; t keeps the print, because t must match the pinned source. 'An', 'or', puts a question that backs the last one with a known case, expecting 'yes'; the Latin Library prints 'At', 'but', and the sense barely changes. 'Phrygius… pastor', 'the Phrygian shepherd', is Paris, brought up among the herdsmen of Mount Ida, who came to Sparta as Menelaus's guest. 'Lacedaemona' is a Greek accusative, the goal of 'penetrat', 'makes his way into'; 'penetrat' is a historic present beside the perfect 'vexit'. 'Ledaeam… Helenam', 'Helen, daughter of Leda'. Without knowing it, Amata repeats Juno's 'Paris alter' (321)."""),
(366, 'Turno?',
 """What of your sacred faith, what of your old care for your own,
and of the right hand so many times given to your kinsman Turnus?""",
 """What has become of your solemn word, of your old concern for your own family, of the hand you have pledged so often to Turnus, your kinsman?""",
 """'Quid', 'what (of)', with the verb left out: 'what has become of'. 'Sancta fides', 'sacred good faith', a promise sworn. 'Cura… tuorum', 'care for your own', has an objective genitive. 'Data dextera', 'the right hand given', the hand clasped in pledge; 'totiens', 'so often'. 'Consanguineo', 'of the same blood', 'kinsman'; Servius makes Turnus's mother Venilia (10.76) the sister of Amata, so that Turnus is her nephew. The narrative said only that Amata wanted Turnus as son-in-law and that portents stood in the way (7.56–58); here she claims that Latinus had pledged himself too."""),
(370, 'divos.',
 """If a son-in-law from a foreign race is sought for the Latins,
and this is settled, and the commands of Faunus, your father, press you,
every land, for my part, that, free, from our sceptre
stands apart, I judge foreign, and that the gods mean so.""",
 """If a son-in-law for the Latins must be sought from a foreign people, and that is fixed, and the commands of your father Faunus weigh on you, then I hold that every land standing free and apart from our rule is foreign, and that this is what the gods mean.""",
 """Amata turns the oracle's words against it. Faunus, Latinus's father (7.47–48), had foretold 'externi… generi', 'sons-in-law from abroad' (7.98). 'Si… petitur', 'if… is sought', a simple condition, granting the fact for argument's sake. 'Latinis' is dative, 'for the Latins'. 'Sedet', 'is settled', 'is fixed'; 'premunt', 'press', 'weigh on'. 'Fauni… parentis', 'of Faunus your father', goes round 'premunt te iussa'. The main clause is accusative and infinitive after 'reor', 'I think', with 'esse' understood: 'omnem… terram… externam (esse)', 'that every land is foreign'. 'Quae libera… dissidet', 'which stands apart, free', with 'sceptris… nostris', 'from our sceptre' (plural for singular). 'Et sic dicere divos', 'and that the gods mean this'. The quibble makes Turnus's Ardea 'foreign' enough."""),
(372, 'Mycenae.”',
 """And Turnus has, if of his house the first origin is traced back,
Inachus and Acrisius as fathers, and midmost Mycenae.”""",
 """And Turnus too, if you trace his house back to its first beginnings, has Inachus and Acrisius for forefathers, and Mycenae, the heart of Greece.”""",
 """'Turno' is a dative of possession with 'sunt' understood, 'Turnus has'. 'Si… repetatur', 'if it should be traced back', has the present subjunctive of a 'should… would' condition. 'Prima… origo', 'first origin', goes round 'domus repetatur'. 'Patres', 'forefathers'. Inachus was the first king of Argos (286, 'Inachiis… ab Argis'), Acrisius a later king there, the father of Danae; Virgil tells at 409–411 how Danae founded Ardea, Turnus's city, with settlers from Acrisius's people. 'Mediae… Mycenae', 'Mycenae in the middle (of Greece)', the heart of the Greek world; 'Mycenae' is a plural name. So Turnus is Greek by descent, as 'foreign' as Aeneas. Amata's speech ends."""),
]
P = A.part('aeneid-052'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
