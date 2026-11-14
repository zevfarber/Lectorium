# aeneid-068 (IX.446-529): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Planctus matris. Testudo Volscorum'
PART = "Euryalus's Mother and the Assault on the Camp (IX.446–529)"
TITLE_EN = "Euryalus's Mother and the Assault on the Camp — Aeneid IX.446–529"
ABOUT = ("The poet breaks off to speak to the dead friends in his own voice: if his verse has any power, Nisus and Euryalus "
"will be remembered as long as Rome stands on the Capitol. The Rutulians carry Volcens's body back to their camp and find "
"there the slaughter of the night — Rhamnes drained of blood, Serranus, Numa and many more — and they recognise the spoils "
"Euryalus had taken. At dawn Turnus calls his men to arms, and they march on the Trojan camp with the heads of Nisus and "
"Euryalus fixed on spears; the Trojans on the walls know the faces too well. Rumour flies through the town to Euryalus's "
"mother, the one Trojan woman who would not be left behind in Sicily. Her shuttle falls from her hands; she runs to the "
"walls and the front line and laments aloud: she was not allowed to say goodbye, she could not close his eyes or wrap him in "
"the robe she was weaving, and all that has come back to her of him is his head. She begs the Rutulians or Jupiter to kill "
"her. The Trojans' courage fails at her cries, and at the word of Ilioneus and the weeping Iulus she is carried indoors. Then "
"the trumpet sounds and the assault begins: the Volsci advance under a locked roof of shields to fill the ditches and tear up "
"the rampart; the Trojans, practised in sieges from the long war at Troy, hurl everything they have and finally roll down a "
"huge mass that smashes the shield-roof. Mezentius comes on with fire, Messapus calls for ladders, and the poet calls on "
"Calliope and her sisters to help him tell the slaughter that Turnus made that day. The mother's lament draws on the "
"laments of Hecuba and Andromache for Hector in the Iliad.")

U = [
(446, 'ambo!',
 "Fortunate both!",
 "How fortunate you both are!",
 """A new paragraph in Greenough. The last part ended with Nisus dying on his friend's body (9.444–445); now the poet speaks to the two dead men in his own voice, an apostrophe, something Virgil rarely does in the Aeneid. 'Fortunati', 'fortunate', 'blessed', not in their deaths but in what follows them, the fame that the next lines promise. 'ambo', 'both', the two together. Elision 'Fortunat(i) ambo'."""),
(449, 'habebit.',
 "If anything my songs can do,\nno day ever from remembering time you will take away,\nwhile the house of Aeneas the Capitol's immovable rock\nshall dwell beside, and the empire the Roman father shall hold.",
 "If my verses have any power at all, no day will ever erase you from the remembrance of the ages, so long as the line of Aeneas lives beside the Capitol's rock that nothing moves, and the Roman father holds his sovereign rule.",
 """'Siquid' = 'si quid', 'if (in) anything', 'quid' an adverbial accusative with 'possunt', 'if my songs have any power'; Greenough writes it as one word, as he does 'siqua'. 'nulla dies… eximet', 'no day will take (you) out', with 'memori… aevo', 'from mindful time', the ablative of separation framing 'vos': the ages that remember. 'dum', 'as long as', with the future. 'domus Aeneae', 'the house of Aeneas', his descendants, the Romans, and in particular the Julian family that claimed him. 'Capitoli', genitive of 'Capitolium', the old '-i' for '-ii' that Virgil always uses for nouns in '-ius' and '-ium'. 'immobile saxum', 'the immovable rock', the Capitoline hill with Jupiter's temple, the pledge of Rome's permanence. 'accolet', 'will dwell beside'. 'pater Romanus', 'the Roman father', the head of the Roman state; ancient readers were already unsure whom Virgil meant (the emperor, the senate, Jupiter of the Capitol have all been proposed). 'imperium… habebit', 'will hold the rule'. The poet's promise of undying fame is the reward of the friends who wanted glory (9.195–196). Elision 'Capitol(i) immobile'."""),
(451, 'ferebant.',
 "The victorious Rutulians, of plunder and spoils having taken possession,\nVolcens, lifeless, weeping, into the camp were carrying.",
 "The Rutulians, victorious and masters of the plunder and the spoils, were carrying the lifeless Volcens back to their camp with tears.",
 """A new paragraph in Greenough. 'Victores', 'victors', with a bitter edge: they have won back their own spoils and lost their leader. 'praeda… spoliisque potiti', 'having got possession of the plunder and the spoils', 'potior' with the ablative; 'spolia' are arms stripped from the enemy, here the things Euryalus had taken. 'Volcentem exanimum', 'Volcens lifeless', killed by Nisus at the end of the last part (9.442–443). 'flentes', 'weeping'. 'ferebant', 'were carrying', the imperfect of an action in progress. Elision 'Volcent(em) exanimum'."""),
(454, 'Numaque.',
 "Nor less in the camp was the grief, Rhamnes being found\nbloodless and the chiefs at once, so many, in one slaughter destroyed,\nboth Serranus and Numa.",
 "No less was the grief in the camp when they found Rhamnes drained of blood, and so many of their leading men struck down together in one slaughter, Serranus and Numa among them.",
 """'Nec minor… luctus (erat)', 'nor was the grief less', the verb understood. 'Rhamnete reperto exsangui', ablative absolute, 'Rhamnes being found bloodless', the king and augur killed by Nisus in his sleep (9.324–328). 'primis… peremptis', a second ablative absolute, 'the chiefs having been destroyed', framing 'una tot caede', 'so many in one slaughter'; 'una' agrees with 'caede'. 'Serranoque Numaque', the double '-que… -que' again, 'both Serranus and Numa', in apposition to 'primis'. Serranus was the young gambler (9.335–338); Numa was not named in the raid, so Virgil adds a name to the dead. Elisions 'exsangu(i) et' ('-gu-' is a consonant and a vowel here, 'gw'), 'Numaqu(e) Ingens' (across the stop, into the next sentence)."""),
(456, 'rivos.',
 "A huge crowding to the very\nbodies and the half-dead men, and the place, with warm, fresh\nslaughter, and the full, with foaming blood, streams.",
 "There was a great rush to see the bodies themselves, the men half alive, the ground still warm with fresh slaughter, and the streams brimming with foaming blood.",
 """'Ingens concursus (fit)', 'a huge running-together (takes place)', the verb left out. 'ad ipsa corpora… viros… locum… rivos', four objects of 'ad', the eye moving from the dead to the dying to the ground to the water. 'seminecis… viros', 'half-dead men', accusative plural in '-is'; 'semineces' from 'semi-' + 'nex', 'death'. 'tepida… caede', 'with warm slaughter', framing 'recentem', 'fresh': the place is still warm with the blood just spilt. 'plenos spumanti sanguine rivos', 'streams full with foaming blood'. The Latin Library reads 'pleno spumantis sanguine rivos', 'streams foaming with full (deep) blood': the same picture, with the foaming given to the streams instead of the blood. Elisions 'Numaqu(e) Ingens' (from the line before), 'loc(um) et'."""),
(458, 'receptas.',
 "They recognise the spoils among themselves, and the gleaming helmet\nof Messapus, and the medallions with much sweat recovered.",
 "They pointed out the spoils to one another, among them Messapus's gleaming helmet and the medallions won back with so much sweat.",
 """'Agnoscunt… inter se', 'they recognise among themselves', point them out to one another. 'galeam… nitentem Messapi', 'the shining helmet of Messapus', which Euryalus put on (9.365–366) and whose gleam betrayed him (9.373–374). 'phaleras', 'medallions', Rhamnes's decorations, taken by Euryalus (9.359). 'multo… sudore receptas', 'recovered with much sweat', framing 'phaleras': won back only with the long night's chase and fight. Elisions 'spoli(a) inter', 'Messap(i) et'."""),
(460, 'cubile:',
 "And now, first, with new light was sprinkling the lands,\nof Tithonus the saffron leaving, Aurora, couch:",
 "And now Dawn, rising from the saffron bed of Tithonus, was first scattering her new light over the earth:",
 """A new paragraph in Greenough. These two lines are repeated exactly from 4.584–585, the dawn on which Dido sees Aeneas's fleet gone. 'prima… Aurora', 'Dawn, first', early Dawn, framing the two lines with 'croceum… cubile'. 'novo… lumine', 'with new light', framing 'spargebat', 'was sprinkling'. 'Tithoni', 'of Tithonus', the Trojan prince loved by the Dawn, who won him immortality but not unending youth; Homer has Dawn rise from his bed at the opening of Iliad 11 and Odyssey 5. 'croceum', 'saffron-coloured', the yellow of the early sky, Homer's 'saffron-robed' Dawn. 'linquens', 'leaving'. No elisions."""),
(464, 'iras.',
 "now, the sun poured in, now, things by the light uncovered,\nTurnus to arms the men, in arms surrounded himself,\nrouses, and the bronze-clad lines into battles drives\neach his own, and with various rumours they sharpen their angers.",
 "Now the sun had poured in, now the light had uncovered the world; Turnus, armed himself, roused his men to arms, each leader drove his bronze-clad ranks into battle, and they whetted their anger with every kind of rumour.",
 """'iam… iam', 'now… now', two ablatives absolute, 'the sun having been poured in', 'things having been uncovered by the light'. 'in arma viros… suscitat', 'rouses the men to arms', framing the line and a half; 'armis circumdatus ipse', 'himself surrounded with arms', already armed: he leads by example. 'aeratas… acies', 'bronze-clad lines', the ranks armed in bronze. 'cogit quisque suas', 'each (leader) drives his own (lines)', 'quisque' with a singular verb, then 'acuunt', 'they sharpen', plural, since 'quisque' implies many. The Latin Library reads 'cogunt quisque suos', 'each drives his own (men)', with a plural verb throughout: the same sense, but 'suos' makes the men, not the lines, the object. 'variis… rumoribus', 'with various rumours', what each had heard of the night's work. Elisions 'sol(e) infuso', 'aeratasqu(e) acies', 'variisqu(e) acuunt'."""),
(467, 'Nisi.',
 "Nay, the very (heads), on raised (a pitiful sight) spears,\nthey fix on the points, the heads, and with much shouting follow\nof Euryalus and Nisus.",
 "More than that, they fixed the very heads of Euryalus and Nisus on spears held high (a piteous sight) and followed them with loud cries.",
 """'Quin', 'nay more', 'what is more', adding something worse. 'ipsa… capita… Euryali et Nisi', 'the very heads of Euryalus and Nisus', held back to the end, so that the names come last, in a half-line. 'arrectis… in hastis', 'on upraised spears', framing the parenthesis 'visu miserabile', 'pitiful to see', 'visu' the supine in '-u' (the ablative of respect: 'in the seeing'). 'praefigunt', 'fix on in front', on the spear-points. 'sequuntur', 'follow', march behind the heads with shouts. In Iliad 18.176–177 Hector longs to cut off Patroclus's head and set it on the stakes of the Trojan wall. Line 467 is one of the poem's unfinished half-lines: Virgil died before he could revise the Aeneid, and some sixty lines stand incomplete. Elisions 'ips(a) arrectis', 'miserabil(e) in', 'capit(a) et', 'Euryal(i) et'."""),
(471, 'maesti;',
 "The sons of Aeneas, hardy, of the walls on the left side\nset against them their battle-line, for the right is girded by the river,\nand the huge trenches they hold, and on the high towers\nstand sorrowful;",
 "The hardy Trojans set their line against them on the left side of the walls, since the right was girded by the river; they held the great trenches and stood grieving on the high towers;",
 """'Aeneadae', 'sons of Aeneas', his followers, the Trojans, a patronymic used of a whole people. 'duri', 'hardy', toughened. 'murorum in parte sinistra', 'on the left side of the walls', the side open to attack. 'opposuere' = 'opposuerunt', 'they set opposite', the '-ere' perfect again; 'aciem', 'battle-line'. 'dextera cingitur amni', 'the right (side) is girded by the river', the Tiber, which guards the camp on that side; 'amni', an ablative in '-i'. 'ingentis… fossas', 'the huge trenches', accusative plural in '-is'. 'stant maesti', 'they stand grieving', held over to the next line: they have already seen what the Rutulians carry. Elisions 'muror(um) in', 'opposuer(e) aciem'."""),
(472, 'tabo.',
 "at the same time the faces of the men, fixed on, were moving them,\nknown too well to the wretched men and dripping with black gore.",
 "and all the while the faces of the two men stuck on the spears moved them to grief, faces the poor Trojans knew all too well, running with dark corruption.",
 """'simul', 'at the same time'. 'ora virum praefixa', 'the faces of the men fixed (on the spears)', 'virum' = 'virorum', the old genitive plural (as 'divom'). 'movebant', 'were moving', stirring the Trojans to grief; it can also be taken with the Rutulians as subject ('they kept shaking the faces on their spears'), but the sentence is about the Trojans, and the next line is what they see. 'nota nimis miseris', 'known too well to the wretched (Trojans)'. 'atro… tabo', 'with black gore', framing 'fluentia', 'flowing'; 'tabum' is blood that has begun to rot. No elisions."""),
(475, 'Euryali.',
 "Meanwhile, through the terrified, flitting, winged, city\nthe messenger Rumour rushes, and the mother's glides up to the ears\nof Euryalus.",
 "Meanwhile winged Rumour went flying through the frightened town as a messenger and slipped into the ears of Euryalus's mother.",
 """A new paragraph in Greenough. 'pavidam… per urbem', 'through the frightened town', the Trojan camp, framing 'volitans pennata', 'flitting, winged'. 'nuntia Fama', 'Rumour the messenger', the winged goddess described at length in 4.173–188, who flies by night and spreads truth and lies alike. 'ruit', 'rushes'. 'matrisque… Euryali', 'the mother of Euryalus', her son's name held over to the next line; she is never named in the poem. 'adlabitur auris', 'glides to the ears', 'adlabor' (Greenough's 'adl-' for 'all-'), with the accusative plural 'auris' in '-is'. Elisions 'matrisqu(e) adlabitur', 'Euryal(i) At' (across the stop, into the next sentence)."""),
(476, 'pensa.',
 "But sudden from the wretched woman the warmth her bones left,\nshaken out of her hands were the shuttles, and unrolled the wool-tasks.",
 "At once the warmth of life drained from the poor woman's bones; the shuttle was struck from her hands and the spun wool rolled away.",
 """'At', 'but'. 'subitus… calor', 'sudden(ly) the warmth', the adjective with the force of an adverb, framing 'miserae': the heat of life leaves her at the shock. 'miserae', dative of disadvantage, 'from the wretched woman'. 'ossa reliquit', 'left her bones'. 'excussi (sunt)… radii', 'the shuttles were shaken out', the plural for one shuttle; 'revoluta… pensa', 'the wool unrolled', 'pensum' the weight of wool given out for a day's spinning, here unwinding as it falls. The model is Andromache in Iliad 22.437–448: at her loom in the house, she hears the wailing from the wall, her limbs shake, and the shuttle falls to the ground. Elision 'Euryal(i) At' (from the line before)."""),
(480, 'memor;',
 "Flies out the unhappy woman, and with a womanly wailing,\ntorn as to her hair, the walls, out of her mind, and the battle-lines at a run,\nthe front ones, she seeks, not she of the men, not she of danger\nand of weapons mindful;",
 "Out flew the unhappy woman, and with a woman's shrieks, her hair torn, beside herself, she ran to the walls and the front ranks, thinking nothing of the men there, nothing of danger or of weapons;",
 """'Evolat', 'flies out'. 'infelix', 'unhappy', 'ill-starred', her standing word. 'femineo ululatu', 'with a womanly wailing', the same words as for the wailing in Carthage at Dido's death (4.667); here, as there, there is no elision: the '-o' of 'femineo' stands in hiatus before 'ululatu', and the long howl is heard in the metre. 'scissa comam', 'torn as to her hair', 'comam' the accusative of respect with a participle used like a Greek middle ('having torn her hair'). 'amens', 'out of her mind'. 'muros… atque agmina… prima', 'the walls and the front ranks', where no woman should go. 'non illa… non illa', 'not she… not she', the pronoun repeated with emphasis. 'virum', 'of the men', the old genitive plural; 'pericli', syncopated for 'periculi'; both genitives depend on 'memor', 'mindful'. Elision 'atqu(e) agmina'."""),
(480, 'implet:',
 "the sky then with complaints she fills:",
 "and then she filled the sky with her laments:",
 """'caelum… implet', 'she fills the sky'. 'dehinc', 'then', 'next', here one syllable (the two vowels run together, synizesis), as often in Virgil. 'questibus', 'with complaints', laments. The colon introduces her speech. No elisions."""),
(481, 'aspicio?',
 "“This you, Euryalus, do I behold?",
 "“Euryalus, is this how I must look on you?",
 """The mother's lament (481–497), the only speech by a mourning mother in the poem; it is built on the laments for Hector in Iliad 22 and 24, by his mother Hecuba and his wife Andromache. 'Hunc ego te… aspicio', 'do I see you (as) this', 'hunc' agreeing with 'te' as a predicate: is this — a head on a spear — what you have become? 'Euryale', vocative. Elisions 't(e) Euryale', 'Euryal(e) aspicio' (with 'Eu-' one syllable)."""),
(483, 'crudelis?',
 "You, that\nlate rest of my old age, could you leave alone,\ncruel one?",
 "Could you, the late-won comfort of my old age, leave me alone, cruel boy?",
 """'Tune', 'you?', 'tu' with the question particle '-ne'. 'illa… requies', 'that rest', the comfort of her declining years, framing the line; 'illa' is Greenough's reading, agreeing with 'requies'; the Latin Library has 'ille', agreeing with 'tu', 'are you he who were…', which changes the grammar but not the sense. 'senectae… meae', 'of my old age', 'senecta' a poetic form of 'senectus'; 'sera', 'late', since he was born to her late or because he was to be her rest in her last years. 'potuisti linquere (me) solam', 'were you able to leave (me) alone', 'solam' feminine, so the object is plainly herself. 'crudelis', 'cruel one', vocative, the word Dido uses of Aeneas (4.311): the grieving speak to the dead as if they had chosen to go. Elision 'Tun(e) illa'."""),
(484, 'matri?',
 "Nor you, under such great dangers sent,\nto address for the last time to your wretched was given the chance mother?",
 "And when you were sent into such deadly danger, was your poor mother not even allowed to speak to you a last time?",
 """'Nec… data (est) copia', 'nor was the opportunity given', with the infinitive 'adfari', 'to speak to', Greenough's 'adf-' for 'aff-'. 'te… missum', 'you, sent', framing 'sub tanta pericula', 'under such dangers'. 'extremum', 'for the last time', an adverbial accusative. 'miserae… matri', dative, framing the rest of the line. Euryalus had left without telling her, to spare her (9.287–289). Elisions 'adfar(i) extremum'."""),
(489, 'anilis.',
 "Alas, in a land unknown, to dogs given as prey, to Latin ones,\nand to birds you lie, nor you, your funeral, I your mother\nled forth, or pressed your eyes, or the wounds washed,\nwith a robe covering, which for you nights in haste and days\nI was pressing on, and with the loom cares I was consoling, an old woman's.",
 "Alas, you lie in a strange land, thrown to the dogs and birds of Latium for their prey, and I your mother never led you out to burial, never closed your eyes or washed your wounds, nor covered you with the robe I was hurrying night and day to finish for you, soothing an old woman's cares at the loom.",
 """'terra ignota', 'in an unknown land', ablative of place without a preposition. 'canibus… Latinis alitibusque', 'to the Latin dogs and birds', 'data praeda', 'given as prey': the oldest fear in epic, from the opening lines of the Iliad (1.4–5), where the heroes are left 'a prey for dogs and all the birds'. 'nec te, tua funera, mater produxi', 'nor did I, (your) mother, lead you forth — your funeral', 'produco', to lead out the funeral procession; 'tua funera', 'your funeral', in apposition to 'te', the dead son being himself the funeral (plural for singular). The Latin Library reads 'funere', which makes 'tua… mater' go together, 'nor did I, your mother, lead you out in your funeral'; an older reading, preserved by Servius, took 'funera' as an old feminine noun, 'the woman who leads the funeral', in apposition to 'mater'. All give the same sense: she could perform none of the rites. 'pressive oculos', 'or pressed your eyes (shut)', '-ve' 'or'. 'veste tegens', 'covering (you) with a robe'; 'quam… urgebam', 'which I was pressing on with', 'noctes… diesque', accusatives of duration, framing 'festina', 'in haste'. 'tela', 'with the loom', ablative (not the 'tela', 'weapons', of 493). 'curas… anilis', 'an old woman's cares', accusative plural in '-is'. Andromache in Iliad 22.510–514 speaks of the fine clothes stored in Hector's house that she will burn, since he will never wear them. Elisions 'terr(a) ignota', 'pressiv(e) oculos', 'urgeb(am) et'."""),
(491, 'habet?',
 "Where shall I follow, or what now your limbs and torn-off members\nand body mangled, land holds?",
 "Where am I to follow? What land holds your limbs now, the torn pieces of you, your mangled body?",
 """'Quo sequar', 'where shall I follow', a deliberative subjunctive: she would follow him even to where his body lies. 'quae… tellus', 'what land', framing the whole question. 'artus avolsaque membra', 'limbs and torn-off members', 'avolsa' Greenough's spelling of 'avulsa' (the old '-vol-'); 'funus lacerum', 'the mangled body', 'funus' here the corpse itself. She imagines the headless body torn by the dogs and birds of 485–486. No elisions."""),
(492, 'refers?',
 "This to me of you,\nson, do you bring back?",
 "Is this all of you that you bring home to me, my son?",
 """'Hoc', 'this', the head on the spear. 'mihi de te… refers', 'do you bring back to me of yourself', as if he had come home from his mission. 'nate', 'son', vocative of 'natus'. No elisions."""),
(492, 'secuta?',
 "For this did I by land and sea follow?",
 "Was it for this that I followed you over land and sea?",
 """'Hoc sum… secuta', 'have I followed this', 'hoc' the internal accusative, 'was this the end of my following'. 'terraque marique', 'both by land and by sea', the double '-que'. She alone of the Trojan mothers refused to stay behind in Sicily with Acestes (9.216–218, 9.284–286). No elisions."""),
(494, 'ferro:',
 "Pierce me, if any there is pity, at me all your weapons\nhurl, O Rutulians, me first destroy with the steel:",
 "Run me through, if there is any pity in you; hurl all your spears at me, Rutulians, and cut me down first of all:",
 """She turns to the enemy. 'Figite me', 'pierce me', imperative. 'siqua est pietas', 'if there is any pity', 'siqua' = 'si qua'; 'pietas' is usually duty, here mercy, the feeling that answers duty. 'me… me… me', the pronoun three times. 'conicite', 'hurl', held over. 'primam', 'first', before any of the men. 'absumite ferro', 'consume with the sword'. Elisions 'siqu(a) est', 'm(e) omnia', 'conicit(e) o', 'prim(am) absumite'."""),
(497, 'vitam.”',
 "or you, great father of the gods, have pity, and with your\nhated this thrust down head beneath Tartarus, with your weapon,\nsince otherwise I cannot break off this cruel life.”",
 "or you, great father of the gods, have pity, and with your thunderbolt hurl this hated head of mine down to Tartarus, since in no other way can I cut short this cruel life.”",
 """'magne pater divom', 'great father of the gods', 'divom' = 'divorum', the old genitive plural. 'miserere', 'have pity', imperative of 'misereor'. 'tuo… telo', 'with your weapon', the thunderbolt, framing the line. 'invisum hoc… caput', 'this hated head', hateful to herself and, she feels, to the gods; 'caput' as 'self', but the word recalls her son's head. 'detrude', 'thrust down', 'sub Tartara', 'down to Tartarus', the deepest part of the underworld. 'quando', 'since'. 'crudelem abrumpere vitam', 'to break off cruel life', as Dido would (4.631, 'invisam… abrumpere lucem'). Her speech ends. Elisions 'invis(um) hoc', 'quand(o) aliter', 'crudel(em) abrumpere'."""),
(499, 'gemitus:',
 "By this weeping were shaken their spirits, and sorrowful through all\ngoes a groan:",
 "Their hearts were shaken by her weeping, and a sorrowful groan went through them all:",
 """'Hoc fletu', 'by this weeping', ablative of cause. 'concussi (sunt) animi', 'spirits were shaken'. 'maestus… gemitus', 'a sorrowful groan', framing 'per omnis… it', 'goes through all', 'omnis' accusative plural. 'it', 'goes', a short plain verb set first in the line. Elision 'concuss(i) animi'."""),
(499, 'vires.',
 "grow numb, broken for battles, their strengths.",
 "their strength for battle failed and went numb.",
 """'torpent', 'grow numb', 'are paralysed'. 'infractae ad proelia vires', 'their strength broken for battle', 'infractae', from 'infringo', 'broken off', 'weakened'. The despair of one mother undoes an army before the assault begins. Elision 'infract(ae) ad'."""),
(502, 'reponunt.',
 "Her, kindling the griefs, Idaeus and Actor,\nat the warning of Ilioneus and of the much-weeping Iulus,\nsnatch up, and between their hands under roofs put back.",
 "Since she was setting their grief ablaze, Idaeus and Actor, at the bidding of Ilioneus and of Iulus, who wept bitterly, took her up and carried her in their arms back indoors.",
 """'Illam incendentem luctus', 'her, kindling griefs', the reason she must be taken away. 'Idaeus et Actor', two Trojans, otherwise little known. 'Illionei monitu', 'at the warning of Ilioneus', the senior Trojan who spoke for the castaways at Carthage (1.521) and before Latinus (7.212); 'Illionei', a Greek genitive, its '-ei' run together into one syllable. The name comes from 'Ilion', Troy, and is usually spelt with one 'l' (the Latin Library has 'Ilionei' here); Greenough's double 'l' is kept as printed, and the scansion is the same either way. 'multum lacrimantis Iuli', 'of Iulus much weeping', 'multum' adverbial; 'Iuli' three syllables, 'I-u-li'. He had promised Euryalus that his mother would be as a mother to him (9.297–298). 'corripiunt', 'snatch up'. 'inter manus', 'between their hands', in their arms. 'sub tecta reponunt', 'put (her) back under roofs', indoors. Elisions 'Ill(am) incendentem', 'monit(u) et'."""),
(504, 'increpuit;',
 "But the trumpet a terrible sound far off with its bronze, ringing,\nrang out;",
 "But the trumpet's ringing bronze blared out its fearful note far and wide;",
 """A new paragraph in Greenough. 'At', 'but', turning back to the war. 'terribilem sonitum… increpuit', 'rang out a terrible sound', the accusative of the sound made; 'procul', 'far off', heard far away. 'aere canoro', 'with tuneful bronze', the trumpet named by its metal. The line echoes Ennius's famous 'at tuba terribili sonitu taratantara dixit', 'and the trumpet with terrible sound said taratantara': Virgil keeps the first words and leaves out the noise. No elisions."""),
(504, 'remugit.',
 "follows a shout, and the sky bellows back.",
 "a shout went up behind it, and the sky roared back.",
 """'sequitur clamor', 'a shout follows', the army's answer to the signal. 'caelumque remugit', 'and the sky bellows back', 'remugio', 'low back', like cattle: the echo of the shout. No elisions."""),
(506, 'vallum.',
 "Hasten up, with driven evenly the tortoise, the Volscians,\nand the trenches to fill prepare, and to tear up the rampart.",
 "The Volscians came on fast, moving their tortoise forward in step, and made ready to fill in the trenches and tear down the palisade.",
 """'Adcelerant', 'they hurry up', Greenough's 'adc-' for 'acc-'. 'acta pariter testudine', ablative absolute, 'the tortoise having been driven evenly', moved forward in step; 'testudo', 'tortoise', the Roman formation in which men lock their shields above their heads and at the sides, like a shell. 'Volsci', the Volscians, an Italian people of Turnus's alliance, whose warrior-queen Camilla closed the catalogue in Book 7 (7.803). 'fossas implere', 'to fill the ditches', to make a way to the wall. 'vellere vallum', 'to tear out the rampart', the stakes along the top of the earthwork; the 'v' sounds repeat. No elisions."""),
(509, 'viris.',
 "Seek, a part, an approach, and with ladders to climb the walls,\nwhere thin is the line and light shows through the ring,\nnot so thick with men.",
 "Some looked for a way in and tried to scale the walls with ladders where the defending line was thin and light showed through the ring of men, less closely packed.",
 """'Quaerunt pars', 'a part seek', a collective singular with a plural verb, construction according to the sense; 'quaerunt' takes first a noun ('aditum', 'an approach') and then an infinitive ('ascendere', 'to climb'). 'scalis', 'with ladders'. 'qua', 'where'. 'rara… acies', 'the line is thin'. 'interlucet', 'shows light between', a picture word: gaps in the line of defenders. 'corona', 'garland', 'crown', and so the ring of men round the walls. 'non tam spissa viris', 'not so thick with men', 'viris' ablative. Elisions 'adit(um) et', 'rar(a) est'."""),
(511, 'bello.',
 "Of weapons to pour out in answer\nevery kind the Teucrians, and with hard poles to thrust down,\nused to defending walls in a long war.",
 "Against them the Trojans poured out every kind of missile and thrust them down with stout poles, men long practised in defending walls through a long war.",
 """'effundere… detrudere', historic infinitives, with 'Teucri' as their subject in the nominative: Latin uses the plain infinitive in this way for quick, vivid narrative in place of an imperfect ('they kept pouring… kept thrusting'), and you will meet it again in the battle books. 'Telorum… omne genus', 'every kind of missiles', framing the line-end. 'contra', 'in reply'. 'duris… contis', 'with hard poles', long pikes for pushing ladders and men off the wall. 'adsueti', Greenough's 'ads-' for 'ass-', 'accustomed'; 'longo… bello', 'in a long war', the ten years at Troy. Elisions 'Telor(um) effundere', 'Teucr(i) ac'."""),
(513, 'perrumpere:',
 "Rocks too of deadly they were rolling weight, if in any way\nthey could the covered line break through:",
 "They also rolled down stones of murderous weight, to see whether they could break through that covered line:",
 """'Saxa… volvebant', 'they were rolling rocks', down from the wall. 'infesto… pondere', 'of hostile weight', ablative of description, framing 'volvebant'. 'siqua possent', 'if in any way they might', 'siqua' = 'si qua' again, 'si' with the subjunctive of an attempt ('to see if'), 'qua' adverbial, 'by any way'. 'tectam aciem', 'the covered line', the tortoise. Elisions 'quoqu(e) infesto', 'tect(am) aciem'."""),
(515, 'sufficiunt.',
 "when nevertheless all\nto bear it pleases, beneath the dense tortoise, falls;\nnor now do they hold out.",
 "yet the attackers were content to take every blow beneath their close-packed tortoise. But now they could hold out no longer.",
 """'cum tamen', 'while all the same', with the indicative 'iuvat', setting a fact against the last clause: the stones fall, but the attackers do not mind. 'omnis… casus', 'all falls', 'every blow', accusative plural in '-is', object of 'ferre'. 'iuvat', 'it pleases (them)', impersonal. The Latin Library reads the subjunctive 'iuvet', which makes the 'cum' clause concessive in the ordinary way ('although they were glad…'); the sense is the same. 'subter densa testudine', 'beneath the dense tortoise', 'subter' with the ablative. 'nec iam sufficiunt', 'and now they are not equal (to it)', the attackers can no longer bear up, as 'nam' in the next sentence explains; some take the subject as the Trojans' stones, which are no longer enough. No elisions."""),
(518, 'tegmina.',
 "For where the mass hangs over, huge,\na vast the Teucrians bulk both roll and send tumbling,\nwhich laid low the Rutulians far and wide, and of their arms broke apart\nthe coverings.",
 "For where the great mass of attackers pressed closest, the Trojans rolled and tipped over a huge block of stone, which flattened the Rutulians far and wide and broke apart their roof of shields.",
 """'qua globus imminet ingens', 'where the mass presses close, huge', 'globus' the close-packed knot of men under the tortoise. 'immanem… molem', 'a huge mass', framing 'Teucri', a great stone or a mass of masonry. 'volvuntque ruuntque', 'both roll and send tumbling', the double '-que', 'ruo' used transitively, 'hurl down'. 'stravit', 'laid flat', the perfect of a thing done at a stroke. 'Rutulos', the Volscians, called by the general name of Turnus's army. 'late', 'far and wide'. 'armorum… tegmina', 'the coverings of their arms', the shields locked overhead; 'resolvit', 'loosened', broke the roof apart. Elision 'lat(e) armorumque'."""),
(520, 'certant.',
 "Nor do they care in blind to fight battle\nany longer, the bold Rutulians, but to drive from the rampart\nwith missiles they strive.",
 "The bold Rutulians had no wish to go on fighting blind; instead they struggled to drive the defenders off the rampart with missiles.",
 """'Nec curant… amplius', 'nor do they care any more'. 'caeco… Marte', 'in blind warfare', framing 'contendere', 'to fight', 'Mars' the god used for war itself (metonymy): under the tortoise no one can see the enemy. 'audaces', 'bold', still. 'pellere vallo', 'to drive (the Trojans) from the rampart', 'vallo' ablative of separation. 'missilibus', 'with missiles', anything thrown. 'certant', 'they strive', with the infinitive. Line 520 is another of the unfinished half-lines. No elisions."""),
(522, 'ignis;',
 "In another part, dreadful to see, was shaking an Etruscan\npine and smoke-bearing brings fires Mezentius;",
 "Elsewhere Mezentius, terrible to look on, was brandishing a blazing torch of Etruscan pine and bringing fire and smoke against them;",
 """'Parte alia', 'in another part', elsewhere along the wall. 'horrendus visu', 'dreadful to see', the supine again (as 'visu miserabile', 465). 'quassabat… pinum', 'was shaking a pine', a pine-torch, swung to keep it blazing; 'Etruscam', 'Etruscan', since Mezentius is the exiled king of the Etruscan city of Caere, the 'despiser of the gods' of the catalogue (7.648), driven out by his own people for his cruelty (8.481–495). 'fumiferos… ignis', 'smoke-bearing fires', accusative plural in '-is'. 'infert', 'brings against', the tense moving from imperfect to present. Elisions 'Part(e) alia', 'ali(a) horrendus', 'pin(um) et'."""),
(524, 'poscit.',
 "but Messapus, of horses the tamer, Neptune's offspring,\ntears open the rampart and ladders against the walls demands.",
 "and Messapus, the tamer of horses and the son of Neptune, cut through the palisade and called for ladders to scale the walls.",
 """'at', 'and on the other hand'. Line 523 repeats 7.691 exactly, where Messapus is introduced in the catalogue: 'equum domitor', 'tamer of horses', 'equum' = 'equorum', the old genitive plural, an epithet in Homer's manner ('horse-taming' is Homer's word for Hector and the Trojans); 'Neptunia proles', 'Neptune's offspring', the god of horses as well as of the sea. He has lost his helmet in the night (458). 'rescindit vallum', 'cuts open the rampart'. 'scalas in moenia poscit', 'demands ladders against the walls'. Elision 'vall(um) et'."""),
(527, 'Orco;',
 "You, O Calliope, I pray, breathe upon me singing,\nwhat there then with the sword slaughters, what deaths Turnus\nbrought about, what man each sent down to Orcus;",
 "Calliope, I pray you and your sisters, breathe on me as I sing what carnage Turnus wrought there with the sword that day, what deaths he dealt, which warrior each man sent down to Orcus;",
 """A new paragraph in Greenough. An invocation of the Muses before a stretch of killing, as Homer calls on them before great slaughters (Iliad 11.218–220, 14.508–510). 'Vos, o Calliope', 'you (plural), O Calliope', the chief of the nine Muses addressed with her sisters; Calliope is the Muse of epic. 'adspirate canenti', 'breathe upon (me) singing', 'canenti' dative, 'mihi' understood; Greenough's 'adsp-' for 'asp-'. 'quas… strages, quae funera… ediderit', 'what slaughters, what deaths (Turnus) produced', indirect questions with the perfect subjunctive, depending on the idea of singing; 'edo', 'bring forth', 'cause'. 'quem quisque virum demiserit Orco', 'what man each sent down to Orcus', 'Orco' a dative of the place to which, Orcus the underworld or its god. No elisions."""),
(529, 'potestis.]',
 "and with me the huge borders unroll of the war,\n[for you both remember, goddesses, and can recount.]",
 "and unroll with me the vast scroll of this war to its farthest edges. [For you remember, goddesses, and you can tell it.]",
 """'mecum… evolvite', 'unroll with me', the image of a book-roll unwound to the end; 'ingentis oras… belli', 'the huge edges of the war', its full extent, 'ingentis' accusative plural in '-is'. The ancient commentators say Virgil takes the phrase from Ennius ('quis potis ingentis oras evolvere belli?', 'who can unroll the huge edges of the war?'). Line 529 is bracketed by Greenough as spurious and is kept here inside [ ]: it is copied from 7.645, where it stands before the catalogue of Italians, and is generally thought to have been added here from there; the Latin Library omits it. 'et… et', 'both… and'; 'enim', 'for'; 'meministis', 'you remember', a perfect with present meaning; 'divae', 'goddesses', vocative; 'memorare', 'to tell'. It echoes Homer's invocation before the catalogue of ships, Iliad 2.484–486, 'for you are goddesses, you are present and know all things'. Elisions 'mec(um) ingentis', 'div(ae) et'."""),
]

P = A.part('aeneid-068'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
A.jdump({'title': TITLE, 'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sents}, os.path.join(HERE, 'units.json'))
print(len(sents), 'units')
