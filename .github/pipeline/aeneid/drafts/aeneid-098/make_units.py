# aeneid-098 (XII.746-842): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Fauni oleaster. Iuno placata'
PART = "Juno Gives Way (XII.746–842)"
TITLE_EN = "Juno Gives Way — Aeneid XII.746–842"
ABOUT = ("Aeneas, still slowed by the arrow-wound in his knee, chases Turnus round the plain like a hound that has a stag penned in by a river, and the banks and the sky ring with the noise. "
"Turnus shouts to the Rutulians for his own sword; Aeneas threatens death to any of them who comes near. "
"Five times they circle and five times run back, and the prize is no trophy of the games but Turnus's life, as it was Hector's when Achilles chased him round Troy in the Iliad. "
"Aeneas's spear has stuck fast in the stump of a wild olive sacred to Faunus, which the Trojans had cut down to clear the field; Turnus prays to Faunus and the Earth to hold it, and the god holds it. "
"While Aeneas strains at it, Juturna, again in the shape of the charioteer Metiscus, runs up and hands her brother his sword, and Venus, angry that the nymph should be allowed so much, pulls the spear free. "
"The two men face each other once more. "
"In heaven Jupiter speaks to Juno, who is watching from a cloud: Aeneas is owed to the sky, she has done all the harm she can, and he forbids her to go further. "
"Juno gives way, and asks one thing that fate does not bind: when the peoples unite, let the Latins keep their name, their language and their dress, and let Troy stay fallen, name and all. "
"Jupiter, smiling, grants it: the Trojans will sink into the Latin people, adding only their rites, and from the mixed race will come a nation that outdoes all others in piety and honours Juno above all. "
"Juno, content, leaves her cloud.")

U = [
(748, 'urget:',
 "Not less Aeneas, although, slowed by the arrow,\nat times his knees hinder him and refuse the running,\npursues, and on the trembling one's foot with foot, hot, presses:",
 "Aeneas kept up the pursuit no less, though now and then his knees, slowed by the arrow-wound, hampered him and would not run, and hot on the heels of the frightened man he pressed him foot to foot:",
 "A new paragraph in Greenough. 'Nec minus', 'no less', for all Turnus's speed. 'Aeneas', Ae- one long syllable. 'tardata sagitta', 'slowed by the arrow', the wound he took when the truce broke (12.319). 'genua', subject of 'impediunt' and 'recusant', here three syllables with the final a elided. 'trepidi', genitive, 'of the panicking man', Turnus; 'pedem pede… urget', 'presses foot with foot', the pursuer's step almost on the fugitive's. 'fervidus', 'hot, eager'. Elision 'genu(a) impediunt'."),
(751, 'instat;',
 "as, shut in, if ever by a river having caught\na stag, or fenced by the fear of the crimson feather,\nthe hunter-hound with running and with barking presses on;",
 "as when a hunting hound has come upon a stag penned in by a river or hemmed by the scare of crimson feathers, and presses it hard, running and baying;",
 "A simile. 'veluti siquando', 'as if ever', 'siquando' Greenough's one word for 'si quando'. 'inclusum… cervum', 'a shut-in stag', the adjective first and the noun held to the next line. 'nanctus', Greenough's spelling of 'nactus', from 'nanciscor', 'come upon'. 'puniceae… formidine pinnae', 'by the scare of the crimson feather': a 'formido' was a cord hung with red feathers stretched round a wood to frighten deer towards the nets (Lewis & Short). 'venator… canis', 'a hunter dog', 'venator' used as an adjective. The model is Iliad XXII, where Achilles chases Hector like a hound after a fawn (from memory). Elision 'cerv(um) aut'."),
(753, 'vias;',
 "he, however, by the snares and by the bank terrified, the high,\na thousand flees and flees back ways;",
 "the stag, terrified by the snares and the steep bank, ran a thousand ways forward and back;",
 "'ille', the stag. 'insidiis', 'by the traps', the feather-line and the nets. 'ripa… alta', 'by the high bank', the river that cuts off its escape. 'mille… vias', 'a thousand ways', an accusative of the path run (cognate accusative) with both verbs. 'fugit refugitque', 'flees and flees back', the doubled verb tracing the doubling back. Elision 'ill(e) autem' and 'aut(em) insidiis'."),
(755, 'est.',
 "but the lively Umbrian\nclings, gaping, now, now he holds, and, like one holding,\nhas snapped with his jaws, and by the bite is cheated, empty.",
 "but the eager Umbrian hound clung close with gaping mouth, all but had him, snapped his jaws as if he held him, and was mocked by a bite on empty air.",
 "'Umber', 'an Umbrian', a breed of hunting dog from Umbria. 'vividus', 'full of life'. 'haeret', 'sticks close'. 'hians', 'gaping', jaws open. 'iam iamque tenet', 'now, now he holds', the present of the thing all but done. 'similisque tenenti', 'like one holding', with a dative. 'increpuit malis', 'has clashed with his jaws', a sudden perfect among presents. 'morsu… elusus inani est', 'is cheated by an empty bite', 'elusus est' split round 'inani'. Elisions 'morsuqu(e) elusus', 'inan(i) est'."),
(757, 'tumultu.',
 "Then truly rises a shout, and the banks and the lake\necho around, and the sky thunders, all, with the uproar.",
 "Then a great shout went up; the banks and the marsh echoed it all round, and the whole sky thundered with the din.",
 "'Tum vero', 'then indeed', marking the high point. 'exoritur', 'arises'. 'ripaeque lacusque', the double '-que… -que', 'both the banks and the lake', the marsh that hems Turnus in (745). 'responsant', 'answer back', echo, a frequentative. 'caelum… omne', 'the whole sky', framing 'tonat'. 'tumultu', 'with uproar', ablative of cause. Elision 'circ(a) et'."),
(759, 'ensem.',
 "He, at once fleeing the Rutulians, at once rebukes all,\nby name each calling, and the known demands sword.",
 "Turnus, even as he fled, berated all the Rutulians, calling each man by name, and clamoured for his own familiar sword.",
 "'Ille', Turnus. 'simul… simul', 'at the same time… at the same time', fleeing and shouting together. 'increpat', 'rebukes'. 'omnis', Greenough's -is accusative plural. 'nomine quemque vocans', 'calling each by name'. 'notum… ensem', 'the familiar sword', his father Daunus's blade forged by Vulcan (12.90–91), left behind that morning when he took Metiscus's by mistake. 'efflagitat', 'demands loudly'. Elision 'notumqu(e) efflagitat'."),
(762, 'instat.',
 "Aeneas death in return and instant threatens\ndestruction, if anyone should approach, and terrifies the trembling,\nthat he will raze the city threatening, and wounded presses on.",
 "Aeneas in his turn threatened death and instant ruin if any man came near, and frightened the trembling Rutulians by vowing to raze their city, pressing on though wounded.",
 "'Aeneas', Ae- one long syllable. 'contra', 'on the other side'. 'mortem… praesensque… exitium', 'death and instant destruction', the second object held over the line-break. 'si quisquam adeat', a present subjunctive, the threat as it is spoken. 'trementis', -is accusative plural, the Rutulians. 'excisurum (esse) urbem', 'that he will raze the city', with 'se' left out. Achilles waves the Greeks back from Hector in the same way in Iliad XXII (from memory). Elisions 'quisqu(am) adeat', 'excisur(um) urbem'."),
(764, 'illuc;',
 "Five circles they complete in running, and as many unweave,\nhither and thither;",
 "Five times round the circuit they ran, and as many times wound it back, this way and that;",
 "'Quinque orbis', 'five circles', 'orbis' the -is accusative plural. 'explent cursu', 'fill out by running'. 'totidem… retexunt', 'unweave as many', the image of a weaver unpicking her web: they run each circuit back the other way. 'huc illuc', 'hither, thither'. Hector runs round Troy three times in Iliad XXII; Virgil makes it five (from memory). No elisions."),
(765, 'certant.',
 "for not light or game-prizes are sought,\nprizes, but of Turnus's life and blood they contend.",
 "it was no trifling prize of the games they were after: they were fighting for the life and blood of Turnus.",
 "'neque enim', 'for not'. 'levia aut ludicra… praemia', 'light or sporting prizes', the adjectives first and the noun held to the next line. 'de vita et sanguine certant', 'they contend about his life and blood'. Homer says it outright in Iliad XXII: they were not running for a sacrificial beast or an ox-hide, the prizes of a foot-race, but for Hector's life (from memory). Elisions 'nequ(e) enim', 'levi(a) aut', 'vit(a) et'."),
(769, 'vestes,',
 "By chance, sacred to Faunus, with leaves a wild olive bitter\nhere had stood, for sailors once a revered wood,\nwhere, saved from the waves, to fix gifts they used\nto the Laurentine god and their vowed to hang garments,",
 "It happened that a wild olive with bitter leaves, sacred to Faunus, had stood here, a tree once held in reverence by sailors, where men saved from the sea used to fasten their offerings to the god of Laurentum and hang up the garments they had vowed;",
 "A new paragraph in Greenough. The period runs to 771; it is split at the comma after 'vestes'. 'Fauno', dative with 'sacer'. Faunus is the Italian woodland god, father of King Latinus (7.47–48). 'foliis… amaris', an ablative of description, 'with bitter leaves'. 'steterat', pluperfect: it had stood, and stands no longer. 'servati ex undis', 'saved from the waves', shipwrecked men; it was custom to hang up the clothes one had escaped in as a thank-offering. 'Laurenti divo', 'the Laurentine god', Faunus of Laurentum. 'votas', 'vowed'. Elisions 'servat(i) ex', 'div(o) et'."),
(771, 'campo.',
 "but the stump the Teucrians, with no distinction, sacred though it was,\nhad cleared away, so that on a clean they might run together, field.",
 "but the Trojans had taken away the stump without regard to its sanctity, so that they could meet in battle on open ground.",
 "'stirpem… sacrum', 'the stump, sacred', the masculine adjective with 'stirps', which is often masculine in verse. 'Teucri', the Trojans, two syllables, Teu-crī. 'nullo discrimine', 'with no distinction', making no difference between holy and common wood. 'sustulerant', pluperfect of 'tollo', 'had removed'. 'puro… campo', 'on a clear plain', framing 'ut possent concurrere'; 'ut' postponed. The sacrilege matters at once: Faunus will take his revenge. Elision 'pur(o) ut'."),
(773, 'tenebat.',
 "Here the spear of Aeneas was standing; hither the force it\nhad carried, fixed, and in the tough root was holding.",
 "Here stood the spear of Aeneas: the force of his throw had carried it to this spot, lodged it, and held it fast in the tough root.",
 "'Aeneae', genitive; Ae- is one long syllable, and 'hasta' elides into it: 'hast(a) Aeneae'. 'stabat', 'stood', upright where it had struck. 'impetus', 'the impetus' of the throw, the subject of both 'detulerat' and 'tenebat'. 'fixam', 'fixed', the spear lodged. 'lenta in radice', 'in the tough, clinging root'; the Latin Library omits 'in', without change of sense. Elisions 'hast(a) Aeneae', 'fix(am) et', 'lent(a) in'."),
(776, 'poterat.',
 "He leaned on it and wished with his hand to wrench out the iron,\nthe Dardanian, and with the weapon to follow him whom to catch by running\nhe was not able.",
 "The son of Dardanus bent over it and tried to wrench the iron out with his hand, to bring down with a weapon the man he could not catch on foot.",
 "'Incubuit', 'leaned over, threw his weight on'. 'convellere ferrum', 'to tear out the iron', the spearhead, for the spear itself. 'Dardanides', 'descendant of Dardanus', a Greek patronymic for Aeneas; Dardanus was the founder of the Trojan line. 'teloque sequi', 'and to pursue with a weapon', to strike from a distance. 'quem… non poterat', 'whom he could not catch by running', the wounded knee again. No elisions."),
(779, 'profanos.”',
 "Then truly, mad with fear, Turnus,\n“Faune, I pray, have pity,” he said, “and you, best, the iron,\nEarth, hold, if I have always tended your honours,\nwhich, on the other side, the Aeneadae by war have made profane.”",
 "Then Turnus, out of his mind with fear: “Faunus, I beg you, pity me,” he cried, “and you, kindest Earth, keep hold of the iron, if I have always kept up the worship due to you both, which the men of Aeneas have defiled with war.”",
 "The print has the whole of 777–779 inside one pair of speech marks with 'inquit' standing within them; this is Greenough's ordinary practice with a parenthetic 'inquit', not a misprint, and l and i set 'he said' apart. 'amens formidine', 'out of his mind with fear'. 'miserere', imperative of 'misereor'. 'optima… terra', 'best Earth', the vocative split by 'ferrum'. 'vestros', 'yours', plural: Faunus and Earth. 'colui… honores', 'I have tended your honours', worship. 'Aeneadae', 'the people of Aeneas', Ae-nĕ-a-dae, with 'contra' elided into it. 'fecere' = 'fecerunt'. Elisions 'ver(o) amens', 'miserer(e) inquit', 'tuqu(e) optima', 'contr(a) Aeneadae'."),
(780, 'vocavit.',
 "He spoke, and the help of the god to not vain vows he called.",
 "So he spoke, and the god's help he called on was not called in vain.",
 "'Dixit', 'he spoke', the regular close of a speech. 'opem… dei… vocavit', 'he called the god's help'. 'non cassa in vota', 'into vows not empty', a litotes: the prayer worked. Virgil says so before he shows it, and the next sentence explains. Elision 'cass(a) in'."),
(783, 'Aeneas.',
 "For long struggling and in the tough stump delayed,\nwith strength none was he able to unclose the bite\nof the oak, Aeneas.",
 "For long Aeneas struggled and lingered over the tough stump, and no strength of his could loosen the wood's grip.",
 "'Namque', 'for', explaining 'non cassa'. 'luctans… moratus', 'struggling… held back', two participles agreeing with 'Aeneas', the subject kept to the end of the sentence. 'lento… in stirpe', masculine 'stirps' again. 'viribus haud ullis', 'with no strength at all'. 'discludere morsus roboris', 'to unclose the bite of the wood', the grip of the root pictured as jaws; 'robur' is hard wood, oak-wood. 'Aeneas', Ae- one long syllable. Elision 'lentoqu(e) in'."),
(785, 'reddit.',
 "While he strains, keen, and presses,\nagain into the charioteer's form changed, Metiscus's,\nruns forward and to her brother the sword the goddess, Daunian, restores.",
 "While he strained and heaved with all his force, the goddess, Daunus's daughter, once more took on the look of the charioteer Metiscus, ran forward, and gave her brother back his sword.",
 "'Dum nititur', 'while he strains', 'dum' with the present. 'rursus… mutata', 'again changed', Juturna, who took Metiscus's shape at 12.468–472. 'aurigae… Metisci', 'of the charioteer Metiscus', framing 'faciem mutata'. 'dea Daunia', 'the Daunian goddess', daughter of Daunus and sister of Turnus, named only at the end. 'ensem… reddit', his own sword. In Iliad XXII Athena gives Achilles back his spear unseen (from memory); here the gift goes to the loser. Elision 'fratriqu(e) ensem'."),
(787, 'revellit.',
 "Which, Venus, to the bold nymph indignant that it was allowed,\napproached and the weapon from the deep root tore out.",
 "Venus, indignant that the bold nymph should be allowed so much, came near and tore the spear out of the deep root.",
 "'Quod', a connecting relative, 'and that': it is the subject of 'licere', 'indignant that this was allowed to the bold nymph'. 'indignata', 'resenting', from the deponent 'indignor'. 'adcessit', Greenough's spelling of 'accessit'. 'alta ab radice', 'from the deep root'. Venus answers Juturna's help, so the two goddesses cancel out and the fight is even again. Elisions 'nymph(ae) indignata', 'telumqu(e) alt(a) ab'."),
(790, 'anheli.',
 "They, aloft, in arms and in spirits restored,\nthis one in the sword trusting, this one fierce and towering with the spear,\nstand up facing, to the contests of Mars breathless.",
 "The two stood tall, their weapons and their courage renewed, one trusting in his sword, the other fierce and towering with his spear, and faced each other for the breathless trial of war.",
 "'Olli', the old form of 'illi', here nominative plural, 'they'. 'sublimes', 'raised high, towering'. 'armis animisque refecti', 'restored in arms and spirits', a chiming pair. 'hic… hic', 'this one… that one', Turnus with the sword, Aeneas with the spear. 'adsistunt contra', 'take their stand facing'. 'certamina Martis anheli', 'the contests of panting Mars', an accusative of what they face; 'anheli', 'breathless', is transferred from the fighters to the god of war. No elisions."),
(792, 'tuentem:',
 "Juno meanwhile the king of all-powerful Olympus\naddresses, from a tawny the fighting cloud watching:",
 "Meanwhile the king of almighty Olympus spoke to Juno, who was watching the fighting from a tawny cloud:",
 "'Iunonem', the object, put first; the subject, 'rex omnipotentis Olympi', Jupiter, follows. 'interea', 'meanwhile', the scene cut to heaven. 'fulva… de nube', 'from a tawny cloud', framing 'pugnas', the line built round what she watches. Juno has watched from the hill now called Alban (12.134). In Iliad XXII Zeus too turns from the chase to talk with a goddess about Hector's fate (from memory). Elision 'Iunon(em) interea'."),
(793, 'coniunx?',
 "“By what way now will the end be, wife?",
 "“Where will it end now, my wife?",
 "Jupiter's speech begins. 'Qua', 'by what way, where', an adverb: 'how will an end come?' The Latin Library prints 'quae', 'what end will there be?', with 'finis' feminine, as it often is in verse; the sense differs a little. 'coniunx', 'wife', con-iunx, the i a consonant. Juno is both his sister and his wife. No elisions."),
(793, 'restat?',
 "What, finally, remains?",
 "What is left to do at last?",
 "'Quid denique restat?', 'what, after all, remains?' The two short questions in one line set the tone: weary, firm, and already sure of the answer. 'denique', 'finally, in the end'. 'restat', 'remains, is left over'. No elisions."),
(795, 'tolli.',
 "Aeneas the Indiges you know yourself, and to know you confess,\nis owed to heaven, and by the fates to the stars is raised.",
 "You know yourself, and admit that you know, that Aeneas is owed to heaven as a god of this land, and that the fates will raise him to the stars.",
 "'Indigetem', 'as Indiges', the title of a native hero made a god: after his death Aeneas was worshipped by the river Numicus as Jupiter Indiges (Livy I, from memory). 'Aenean', a Greek accusative. 'scis ipsa et scire fateris', 'you yourself know and confess that you know'. 'deberi caelo', 'is owed to heaven', and 'tolli', 'is raised', both infinitives of indirect statement. 'fatis', 'by the fates'. Elisions 'Indiget(em) Aenean', the elided syllable falling before Ae-, which is one long syllable; 'ips(a) et', 'fatisqu(e) ad'."),
(796, 'haeres?',
 "What are you building, or with what hope in the cold clouds do you cling?",
 "What are you plotting, or what hope keeps you clinging there in the chill clouds?",
 "'Quid struis', 'what are you building up', scheming. 'qua spe', 'with what hope', ablative. 'gelidis in nubibus haeres', 'do you stick in the cold clouds', a pointed picture: the queen of heaven sitting about in the damp air to watch a fight she cannot win. No elisions."),
(799, 'victis?',
 "By a mortal was it fitting to be violated, with a wound, a god,\nor the sword (for what without you would Juturna avail?)\nsnatched away to be given back to Turnus, and strength to grow for the beaten?",
 "Was it right that one who is to be a god should be hurt by a mortal's wound? Or that the sword taken from Turnus should be handed back to him — for what could Juturna do without you? — and the beaten side find its strength again?",
 "'Mortalin' = 'mortaline', 'mortali' with the question particle '-ne', its e dropped. 'mortali… volnere', 'by a mortal wound', one dealt by a man: the arrow of 12.319. 'divom', Greenough's spelling of 'divum', here accusative singular, 'a god', Aeneas, subject of 'violari'. 'decuit', 'was it fitting', governs all three infinitives: 'violari', 'reddi', 'crescere'. 'ensem… ereptum', 'the sword snatched away'. The parenthesis lays Juturna's help at Juno's door. 'victis', dative, 'for the conquered'. Elision 'Turn(o) et'."),
(803, 'est.',
 "Cease now at last, and by prayers be bent, ours,\n[lest you so great should gnaw, silent, a grief, and to me cares]\n[often from your sweet, sad, mouth should return,]\nit has come to the last.",
 "Stop now, at last, and let my pleas move you [and do not let so great a grief gnaw at you in silence, nor bitter cares so often come back to me from your dear lips]: we have come to the end.",
 "Greenough brackets 801–802 as spurious; they are kept in [ ]. 'Desine', 'stop'. 'inflectere', a passive imperative, 'be bent'. In the bracketed lines 'ni' is the old form of 'ne', 'and let not…', and 'edit' is an old present subjunctive of 'edo', 'eat', = 'edat'; 'curae… tristes… recursent', 'let bitter cares not keep running back to me'. 'ventum ad supremum est', 'it has come to the last', an impersonal passive. Elisions 'precibusqu(e) inflectere', 'vent(um) ad', 'suprem(um) est'."),
(806, 'veto.',
 "On lands to harry or on waves\nthe Trojans you have been able, unspeakable to kindle war,\nto disfigure a house, and with grief to mingle the wedding-songs:\nfurther to attempt I forbid.”",
 "You have had the power to hound the Trojans over land and sea, to light an abominable war, to blight a royal house and mix mourning with marriage-songs: I forbid you to try anything more.”",
 "The print has 'veto. ”Sic', a misprint for 'veto.” Sic', corrected here: Jupiter's speech ends at 'veto'. 'Terris… vel undis', 'on lands or waves', the whole tale since Book I. 'potuisti', 'you have been able', taking four infinitives. 'infandum… bellum', the war Allecto stirred up for Juno in Book VII. 'deformare domum', Latinus's house, shamed by Amata's death. 'luctu miscere hymenaeos', 'to mingle the wedding-songs with grief', Lavinia's marriage. 'veto', 'I forbid'. Elisions 'potuist(i) infandum', 'dom(um) et', 'miscer(e) hymenaeos'."),
(807, 'voltu:',
 "So Jupiter began;\nso the goddess, with lowered, in reply, Saturnian, face:",
 "Thus Jupiter spoke; and thus, with downcast look, the daughter of Saturn answered:",
 "The closing speech mark the print sets before 'Sic' belongs to the end of the previous unit, and is dropped here. 'orsus (est)', 'began', from 'ordior', used of starting to speak. 'sic… sic', 'so… so', the two speakers balanced. 'Saturnia', 'daughter of Saturn', Juno's regular title, held to the end. 'submisso… voltu', 'with lowered face', framing the line; 'voltu' is Greenough's spelling of 'vultu'. The verb of speaking is left out. No elisions."),
(809, 'reliqui;',
 "“That, indeed, because known to me your, great, will,\nJupiter, both Turnus and the earth unwilling I have left;",
 "“It is because I knew that this was your will, great Jupiter, that I have left Turnus and the earth, though against my wish;",
 "Juno's speech begins. 'Ista… tua… voluntas', 'that will of yours', the words spread round the line; 'quia' is postponed. 'nota (est)', 'is known'. 'magne… Iuppiter', the vocative split across the line-break. 'invita', 'unwilling', feminine, agreeing with the speaker. 'reliqui', 'I have left', perfect: she has already withdrawn. Elision 'Turn(um) et'."),
(812, 'Teucros.',
 "nor would you see me on an airy alone now seat\nworthy and unworthy things suffering, but by flames girt, beneath the very\nI should stand battle-line and be dragging into hostile fights the Teucrians.",
 "otherwise you would not see me now sitting alone on a perch of air, bearing whatever befell, deserved or not: I should be standing in the battle-line itself, girt with flames, dragging the Trojans into a fight they would rue.",
 "'videres… starem… traherem', imperfect subjunctives of a present unreal condition, the 'if' clause left to be understood: '(if it were not your will), you would not see…'. 'me aeria', 'me' elided before 'aeria'. 'aeria… sede', 'on an airy seat', framing 'solam nunc'. 'digna indigna pati', 'to suffer worthy, unworthy things', everything, without 'et'. 'flammis cincta', 'ringed with flames'. 'inimica… proelia', 'hostile battles', battles to their cost. 'Teucros', Teu- one syllable. Elisions 'm(e) aeria', 'dign(a) indigna', 'star(em) acie', 'traheremqu(e) inimica', 'inimic(a) in'."),
(815, 'arcum:',
 "Juturna, to her wretched, I admit, to run to the aid of, brother,\nI urged, and for his life greater things to dare I approved,\nnot so that weapons, however, not so that she should strain a bow:",
 "I did urge Juturna, I confess, to go to the help of her unhappy brother, and I allowed her to dare great things to save his life, but not to aim weapons, not to bend a bow:",
 "'Iuturnam… suasi', 'I urged Juturna', with 'succurrere'; 'suadeo' usually takes a dative of the person. 'fateor', 'I confess', a parenthesis. 'misero… fratri', 'her unhappy brother', framing 'fateor, succurrere'. 'probavi', 'I approved'. 'maiora', 'greater things'. 'non ut… contenderet', 'not that she should…', a purpose clause; 'contenderet' goes with both 'tela', 'aim weapons', and 'arcum', 'draw the bow', a zeugma. The arrow that wounded Aeneas came from an unknown hand (12.319–320). No elisions."),
(817, 'divis.',
 "I swear by the Stygian head implacable of the spring,\nthe one dread which to the gods above is assigned.",
 "I swear it by the unappeasable source of the Stygian stream, the one oath that holds the gods above in awe.",
 "'adiuro', 'I swear by', with the accusative; ad-iu-ro, the i a consonant, ad- long. 'Stygii… fontis', 'of the Stygian spring', the river Styx; 'caput', 'head, source'. 'implacabile', 'that cannot be appeased'. An oath by the Styx binds even the gods: Hera swears by it in the Iliad (from memory). 'una superstitio', 'the one object of religious awe', the old sense of 'superstitio'. 'quae reddita (est)', 'which has been assigned'. No elisions."),
(818, 'relinquo.',
 "And now I yield, indeed, and the fights loathing I leave.",
 "And now I give way, truly, and leave the fighting, which I have come to loathe.",
 "'cedo', 'I yield', the word that matters, set early. 'equidem', 'for my part, truly'. 'exosa', 'hating', a participle of 'odi' with active sense, 'having come to hate'. 'pugnas… relinquo', 'I leave the battles'. Juno's anger, which drove the poem from its first lines (I.4), gives way here. Elisions 'ced(o) equidem', 'pugnasqu(e) exosa'."),
(820, 'tuorum:',
 "That you, which by no law of fate is held,\nfor Latium I beseech, for the majesty of your own:",
 "One thing, which no law of fate forbids, I beg of you for Latium's sake and for the honour of your own kin:",
 "'Illud te… obtestor', 'I beseech you this', two accusatives, the person and the thing asked. 'nulla fati quod lege tenetur', 'which is held by no law of fate', so Jupiter is free to grant it. 'pro Latio', 'on behalf of Latium'. 'tuorum', 'of your own (people)': Latinus descends from Saturn, Jupiter's father (7.48–49), so the Latins are Jupiter's kin. Elision 'Lati(o) obtestor'."),
(825, 'vestem.',
 "when now with marriages peace happy, so be it,\nthey shall settle, when now laws and treaties they shall join,\nnot the old, native, name to change the Latins\nnor Trojans to become bid, and Teucrians to be called,\nor their voice to change, the men, or to alter their dress.",
 "when they make peace through happy marriages (so be it), and when they join in laws and treaties, do not command the native Latins to change their ancient name, or to become Trojans and be called Teucrians, or to change their speech or their dress.",
 "'cum… component… iungent', future indicatives, 'when they shall settle… join'. 'conubis', Greenough's spelling of 'conubiis', 'by marriages'. 'esto', 'let it be so', a grudging concession. 'ne… neu… iubeas', 'do not order', the thing she asks. 'indigenas… Latinos', 'the native Latins', framing the line. 'Troas', a Greek accusative plural, Trō-ăs, two syllables. 'Teucros', Teu- one syllable. 'vocem', 'speech, language'. 'vertere vestem', 'change their dress', the Trojan's Phrygian clothes. No elisions."),
(827, 'propago:',
 "Let Latium be, let there be Alban through the ages kings,\nlet there be Roman, strong with Italian valour, offspring:",
 "Let Latium stand; let there be Alban kings through the long ages; let the Roman stock grow mighty on Italian courage:",
 "Three jussive subjunctives: 'Sit… sint… sit', 'let there be'. 'Albani… reges', the kings of Alba Longa, Ascanius's city, the line that leads to Romulus. 'per saecula', 'through the generations'. 'Romana… propago', 'the Roman offshoot', a gardener's word for a layer or slip; 'Itala virtute', ablative, 'by Italian valour'. The future Rome she asks for is Italian, not Trojan. No elisions."),
(828, 'Troia.”',
 "fallen it has, and may you allow it to have fallen with its name, Troy.”",
 "Troy has fallen: then let it be gone for good, and let its name go down with it.”",
 "'occidit, occideritque', 'it has fallen, and… have fallen', the verb repeated for weight. 'sinas', 'may you allow', with the perfect subjunctive 'occiderit' and no 'ut'. 'cum nomine', 'with its name'. 'Troia', last word of the speech. Juno's whole quarrel with the Trojans ends in this one demand, and Roman history answers it: Rome took the Latin name and tongue. No elisions."),
(830, 'proles:',
 "To her, smiling, of men and things the maker:\n“You are the sister of Jove and of Saturn the second offspring:",
 "The creator of men and of the world smiled at her and said: “You are truly Jove's sister, Saturn's other child:",
 "'Olli', the old 'illi', here dative singular, 'to her'. 'subridens', 'smiling', recalls I.254, where Jupiter smiles at Venus in the same words, 'Olli subridens hominum…'. 'repertor', 'the deviser, maker'. The verb of speaking is left out. Jupiter's speech begins. 'Es germana Iovis', 'you are the sister of Jove'. 'altera proles', 'the second child' of Saturn, the other besides Jupiter himself: the storm of anger proves her birth. Elision 'Saturniqu(e) altera'."),
(831, 'fluctus.',
 "of angers such great you roll beneath your breast waves.",
 "such great waves of anger you churn in your breast.",
 "'irarum tantos… fluctus', 'such great waves of angers', the noun held to the end of the line. 'volvis', 'you roll', the sea image. The line may be read with the one before: such wrath is proof of divine birth, and the remark is half rebuke, half admiration. The plural 'irae', as at I.11, means fits of anger. No elisions."),
(833, 'remitto.',
 "But come, and the begun in vain let go fury:\nI give what you wish, and myself, both beaten and willing, I give up.",
 "But come, let go of this rage that you began for nothing: I grant you your wish, and yield, beaten and willing both.",
 "The print has no mark after 'furorem' (832); 'do quod vis' begins a new statement, so it is read as after a colon here. 'Verum age', 'but come'. 'inceptum frustra… furorem', 'the fury begun in vain', framing 'submitte'. 'submitte', 'lower, let down'; the Latin Library spells it 'summitte'. 'do quod vis', 'I give what you want'. 'victusque volensque', the double '-que', 'both conquered and willing'. 'me… remitto', 'I give myself back, give way'. Elision 'ag(e) et'."),
(835, 'erit;',
 "Their speech the Ausonians, ancestral, and customs will keep,\nand as is the name it will be;",
 "The Ausonians will hold on to the tongue their fathers spoke and to their own ways, and their name will remain what it is;",
 "'Ausonii', 'the Ausonians', the Italians, from an old name for Italy. 'sermonem… patrium', 'their fathers' speech', framing 'Ausonii'. 'moresque', 'and their customs'. 'utque est nomen erit', 'and as the name is, (so) it will be': they will still be called Latins. Each of Juno's requests is granted in turn. Elision 'utqu(e) est'."),
(836, 'Teucri.',
 "mingled in body only\nwill settle down the Teucrians.",
 "the Trojans will be merged with them in blood alone, and sink from view among them.",
 "'commixti corpore tantum', 'mingled in body only', by marriage and descent, not in name or language. 'subsident', 'will settle down', 'subsido', of sediment sinking to the bottom: the Trojans vanish into the Latin people. 'Teucri', Teu-crī, two syllables, placed last in the clause. No elisions."),
(837, 'Latinos.',
 "Custom and rites of sacred things\nI will add, and I will make all with one mouth Latins.",
 "Their custom and the rites of their worship I will add, and I will make them all Latins of one tongue.",
 "'Morem ritusque sacrorum', 'the custom and rites of the sacred things', Trojan religion, the Penates and Vesta brought from Troy; this is all the Trojans add. 'adiciam', 'I will add', ad- long, from 'ad-iacio' with the i a consonant. 'omnis', -is accusative plural, 'all'. 'uno ore', 'with one mouth', one language. Elisions 'faciamqu(e) omnis', 'un(o) ore'."),
(840, 'honores.”',
 "Hence the race, with Ausonian mixed which blood will rise,\nabove men, above to go gods in devotion you will see,\nnor will a people any your equally celebrate honours.”",
 "The race that will spring from here, blended with Ausonian blood, you will see outstrip men and outstrip the gods themselves in devotion, and no nation will keep your festivals with equal zeal.”",
 "'Hinc genus… quod… surget', 'the race which will rise from here', the antecedent drawn into the relative clause. 'Ausonio… sanguine', 'with Ausonian blood', framing 'mixtum'. 'supra… supra', 'above… above', the repetition building to the bold claim that Romans will outdo the gods in 'pietas'. 'tuos… honores', 'your honours', worship. At Rome Juno shared the Capitol with Jupiter and Minerva (from memory). Elisions 'supr(a) homines', 'supr(a) ire'."),
(841, 'retorsit.',
 "Nodded to these Juno and, her mind gladdened, turned back.",
 "Juno nodded assent to this, and gladly turned her purpose round.",
 "'Adnuit his', 'she nodded to these things', agreed. 'laetata', 'rejoicing', a participle of 'laetor'. 'mentem… retorsit', 'twisted her mind back', changed her purpose; 'mentem' may also be taken with 'laetata', 'gladdened in mind', an accusative of respect. Elision 'Iun(o) et'."),
(842, 'relinquit.',
 "Meanwhile she departs from the sky and the cloud leaves.",
 "Then she withdrew from the sky and left her cloud behind.",
 "'Interea', 'meanwhile', back to the plain below. 'excedit caelo', 'goes out from the sky', the open air where she sat, ablative of separation without a preposition. 'nubem… relinquit', 'leaves the cloud' from which she had watched (792). The goddess who opened the poem in anger leaves it quietly. Elision 'Intere(a) excedit'."),
]

# Speech-mark check exemptions (rule 5b), by closing text of the unit:
#  'profanos.”' (776-779): the print keeps 'inquit' inside one pair of marks (777); l and i set 'he said' outside
#      the speech, so they carry an extra closing and opening mark; noted (Greenough's practice, not a misprint).
#  'veto.' (803-806): the print has 'veto. ”Sic'; l and i close Jupiter's speech after 'veto'; the note opens
#      'The print has'.
#  'voltu:' (806-807): t opens with the misplaced closing mark; l and i drop it; noted.
#  'remitto.' (832-833): no mark after 'furorem' in the print; l and i read a colon; noted (no mark issue).
EXEMPT = {'profanos.”', 'veto.', 'voltu:'}
OVERLONG = set()
P = A.part('aeneid-098'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']} | {L[0]['n']}
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
