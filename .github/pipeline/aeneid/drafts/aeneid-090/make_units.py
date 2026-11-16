# aeneid-090 (XI.836-915): t is cut from the edition by A.cut; l, i, n drafted from the Latin.
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import aeneid_lib as A

TITLE = 'Opis ultrix. Fuga ad urbem'
PART = "Opis's Vengeance and the Rout to the Walls (XI.836–915)"
TITLE_EN = "Opis's Vengeance and the Rout to the Walls — Aeneid XI.836–915"
ABOUT = ("Opis, the nymph whom Diana sent down to guard Camilla, has watched the battle from the hills, and now sees her lying dead. "
"She mourns her briefly and swears that the man who wounded her will pay with his life. "
"From the old burial mound of a Laurentine king she finds Arruns, still exulting, calls out to him in mockery, and kills him with a single arrow from Diana's quiver; his comrades leave him dying in the dust, and she flies back to Olympus. "
"With their leader gone, Camilla's horsemen break, and the whole Latin army flees for the city. "
"At the gates there is slaughter: those who reach them first are cut down on the threshold, the defenders shut the gates against their own men, and the women on the walls, remembering Camilla, hurl whatever they can find. "
"Acca brings the news to Turnus, who abandons his ambush in the hills just before Aeneas marches through the pass he was guarding. "
"The two armies come in sight of each other beneath the walls, but the sun is setting, and both sides camp for the night. "
"So ends Book XI.")

U = [
(837, 'pugnas.',
 """But of Trivia the guardian long since on the mountains, Opis,\nhigh sits, on the topmost, and watches, undaunted, the fights.""",
 """But Opis, Trivia's guardian, had long been sitting high on the mountain-tops, watching the battle unafraid.""",
 """A new paragraph in Greenough. 'Triviae custos', 'Trivia's guardian': Trivia, 'of the three ways', is Diana as goddess of crossroads, where she was identified with Hecate. Opis is the nymph Diana sent down to guard Camilla and avenge her (XI.532–596); in Callimachus she is a Hyperborean maiden, a name also given to Artemis herself (from memory). 'iamdudum… sedet', 'has long been sitting', the present with 'iamdudum' for an action still going on. 'alta… summis', 'high… on the topmost (mountains)', the adjective again where English wants an adverb, as 'altus' at 726. 'interrita', 'unterrified', a goddess among the missiles. Elisions 'iamdud(um) in', 'spectatqu(e) interrita'."""),
(840, 'voces:',
 """And as, far off, in the midst of the young men, amid the shouting of them raging,\nshe saw ahead, with grim death punished, Camilla,\nboth she groaned and gave these from her deepest breast words:""",
 """And when, far off amid the shouting of the frenzied warriors, she saw Camilla punished with a grievous death, she groaned and spoke these words from the bottom of her heart:""",
 """'Utque', 'and as', 'ut' of time with the perfect, 'as soon as'. 'furentum', 'of (men) raging', Greenough's old genitive plural of the participle in '-um' for '-ium' (you will see 'defendentum', 'ruentum', 'lacrumantum' later in this part). 'prospexit', 'looked out and saw', from far off. 'multatam', 'punished, fined', from 'multo'; the Latin Library reads 'mulcatam', 'mauled', which makes the death brutal rather than a penalty. 'ingemuitque deditque', the double '-que… -que', 'both… and'. 'imo pectore', 'from the bottom of her breast'. Elisions 'iuven(um) in', 'deditqu(e) has'."""),
(842, 'bello!',
 """“Alas, too much, maiden, too much cruel you have paid\na penalty, the Teucrians having tried to provoke in war!""",
 """“Alas, maiden, too cruel, far too cruel is the penalty you have paid for daring to challenge the Trojans in war!""",
 """Opis's lament opens; it runs to 849. 'nimium… nimium', the repeated word of grief. 'crudele… supplicium', 'a cruel penalty', split across the line-end. 'luisti', 'you have paid', from 'luo', the verb of paying a debt or penalty; 'luet' returns at 849, of Arruns. 'conata', 'having tried', a participle with causal force: this is what she paid for. 'Teucros', 'the Teucrians', Trojans, after their ancestor Teucer; 'eu' is one syllable. 'lacessere bello', 'to provoke with war'. No elisions."""),
(844, 'sagittas.',
 """Nor to you, lonely among the thickets, to have worshipped Diana\nwas any profit, or our on your shoulder to have carried arrows.""",
 """It did you no good to have worshipped Diana alone in the thickets, or to have carried our arrows on your shoulder.""",
 """'Nec… profuit', 'nor did it profit', with two perfect infinitives as subjects, 'coluisse… gessisse', 'to have worshipped… to have carried'. 'tibi desertae', 'to you, lonely', the solitary life of the huntress devoted to Diana (XI.567–584). 'nostras… sagittas', 'our arrows', Diana's and her nymphs': Camilla carried the goddess's own weapons. 'umero', Greenough's spelling of 'humero', 'shoulder'. The Latin Library reads 'pharetras', 'quivers', for 'sagittas', 'arrows', which hardly changes the sense. Elision 'desert(ae) in'."""),
(847, 'inultae.',
 """Not however without honour your queen has left you\nat the very edge now of death, nor this without a name death\namong the nations will be, or the fame will you suffer of one unavenged.""",
 """Yet your queen has not left you without honour, now at the very end of death; your death will not go unnamed among the nations, nor will you bear the name of one who died unavenged.""",
 """'tua… regina', 'your queen', Diana, whose follower Camilla was. 'indecorem', 'without honour', from the rarer third-declension 'indecoris'. 'extrema iam in morte', 'now in death's last moment'. 'sine nomine', 'without a name', unsung. 'per gentis', 'among the peoples', the '-is' accusative plural (you'll see it constantly in this part: 'sonantis', 'instantis', 'orantis', 'hostis'). 'famam… inultae', 'the repute of (one) unavenged', the genitive agreeing with the 'you' implied in 'patieris': you will not be spoken of as unavenged. Diana had promised both things, burial and vengeance (XI.590–594). Elisions 'i(am) in', 'neq(ue) hoc'."""),
(849, 'merita.',
 """For whoever your has violated with a wound body,\nby death will pay, deserved.”""",
 """For whoever has violated your body with a wound will pay for it with the death he has earned.”""",
 """The lament closes here. Greenough's print sets the closing mark after a space, joined to the next word, 'Fuit', as at 827; t keeps the print, and l and i close the speech after 'merita.'. The line repeats Diana's command (XI.591–592), 'quicumque sacrum violarit vulnere corpus': Opis is carrying out her orders. 'tuum… corpus', framing the line. 'violavit', 'has violated', the word for profaning something sacred. 'morte… merita', 'by a deserved death', ablative of price with 'luet', 'will pay'. No elisions."""),
(851, 'tectum:',
 """There was, huge, a mountain beneath high,\nof king Dercennus, of earthen mound, a tomb,\nof the ancient Laurentine, and with dark holm-oak covered:""",
 """At the foot of a high mountain there was the great tomb of Dercennus, an ancient king of the Laurentines, a mound of heaped earth shaded by a dark holm-oak:""",
 """The mark at the head of t belongs to the speech just ended (see the previous unit); l and i carry none. 'Fuit', 'there was', the formula that sets a scene. 'monte sub alto', 'under a high mountain', the preposition placed between adjective and noun. 'Dercenni', Dercennus, an early king of Laurentum, known only from this line. 'terreno ex aggere', 'of an earthen mound', ablative of material. 'bustum', 'tomb', strictly the place where a body was burnt. 'ilice', the holm-oak, the evergreen oak of Italy. Paris shoots Diomedes from behind the grave-pillar of Ilus in the Iliad (XI.369–372, from memory). Elisions 'terren(o) ex', 'opacaqu(e) ilice'."""),
(853, 'alto.',
 """Here the goddess herself first with swift swoop, most beautiful,\nsets, and Arruns from the mound watches, high.""",
 """Here first the goddess, in all her beauty, came to rest after her swift flight, and from the high mound she kept watch on Arruns.""",
 """'hic', 'here', on the tomb. 'primum', 'first', before she does anything else. 'rapido… nisu', 'with a swift effort', the swoop of her flight: she has come down from the mountain. 'se… sistit', 'sets herself, takes her stand'. 'pulcherrima', 'most beautiful', the stock praise of a goddess, here with a chill: beauty and death. 'Arruntem', accusative of 'Arruns'. 'speculatur', 'keeps watch', from a look-out ('specula'). 'tumulo… ab alto', 'from the high mound', framing the line's end. No elisions."""),
(855, 'abis?',
 """When she saw him exulting in his spirits and with vain things swelling,\n“Why, she says, turned aside are you going off?""",
 """When she saw him exulting and swollen with empty pride, “Why, she said, are you slinking off the other way?""",
 """'Ut vidit', 'when she saw', 'ut' of time again. 'laetantem animis', 'rejoicing in spirit', and 'vana tumentem', 'swelling with vain things', a neuter plural used as an adverbial accusative: empty pride. The Latin Library reads 'fulgentem armis', 'gleaming in his armour', which loses the point: Arruns is gloating. Opis's taunt opens; it runs to 857. 'inquit', 'she says', set inside the speech. 'diversus', 'turned another way', away from the fighting, as Arruns has been running since 806. Elision 'laetant(em) animis'."""),
(857, 'praemia.',
 """Here direct your step,\nhere, about-to-die, come, that you may take worthy of Camilla\nrewards.""",
 """This way, turn your steps this way; come here, man about to die, and take the reward that Camilla's death has earned you.""",
 """'Huc… huc', the repeated 'here', a summons. 'dirige', 'direct'; the Latin Library spelling 'derige' is the same word. 'periture', 'you who are going to die', the vocative of the future participle: the address is the sentence. 'capias ut', 'that you may take', 'ut' of purpose set after its verb. 'digna Camillae praemia', 'rewards worthy of Camilla', irony: the prize for killing Camilla is death. No elisions."""),
(857, 'Dianae?”',
 """Are you even by the weapons going to die of Diana?”""",
 """Shall even you have the honour of dying by Diana's arrows?”""",
 """The taunt ends. 'Tune', 'you?', 'tu' with the question particle '-ne', scornful. 'etiam', 'even': even a creature like you. 'moriere', 'you will die', the future in '-re' for '-ris', common in verse. 'telis… Dianae', 'by the weapons of Diana', framing the line. The irony is double: death at the hands of a goddess was a kind of honour (Aeneas tells Lausus his death by Aeneas's hand will console him, X.829–830), and Arruns does not deserve it. Elision 'Tun(e) etiam'."""),
(862, 'papillam.',
 """She spoke, and from her gilded a winged the Thracian arrow\ndrew from her quiver, and with the horn, hostile, she stretched it,\nand drew it far, until, bent, should meet\none another the ends, and with her hands now she touched, level,\nwith the left the edge of the iron, with the right and the string her breast.""",
 """So she spoke, and the Thracian maid drew a winged arrow from her gilded quiver, aimed it in anger along her bow of horn, and pulled it far back, until the curving ends almost met and her hands were level, the left touching the iron point, the right with the bowstring touching her breast.""",
 """'dixit', 'she spoke', closing the speech. 'Threissa', 'the Thracian woman', the Greek form, as Harpalyce at I.316: Thrace was a land of huntresses. 'deprompsit pharetra', the words of Diana's order at XI.590, 'pharetra deprome sagittam'. 'cornu', 'horn', the bow; 'infensa', 'hostile'. 'donec… coirent… tangeret', 'donec' with the subjunctive, 'until… should meet', of a result aimed at. 'capita', 'heads', the bow's two tips. 'laeva aciem ferri, dextra nervoque papillam', the full draw: the left hand at the arrowhead, the right hand with the string at her breast, as Pandarus draws in Iliad IV.123 (from memory). Elisions 'cornuqu(e) infensa', 'capit(a) et', 'laev(a) aciem'."""),
(864, 'ferrum.',
 """At once of the weapon the whirring and the airs sounding\nheard, at the same time, Arruns, and stuck in his body the iron.""",
 """In the same instant Arruns heard the hiss of the arrow and the singing air, and the iron was fixed in his body.""",
 """'Extemplo', 'immediately'. 'stridorem', 'the whirring, shrill hiss'. 'auras… sonantis', 'the sounding airs', with the '-is' accusative plural. 'audiit una', 'heard at the same time', with 'una' an adverb: the hearing and the wound are one moment, as the two clauses joined by '-que' show. Arruns hears death coming, as Camilla did not (801–802). 'haesit… ferrum', 'the iron stuck fast'. Elisions 'un(a) Arruns', 'haesitqu(e) in'."""),
(867, 'Olympum.',
 """Him breathing out and his last groaning\nhis comrades, forgetful, in the unknown of the plains dust leave;\nOpis to the airy on her wings is carried off Olympus.""",
 """His comrades forget him and leave him gasping out his life and groaning his last in the dust of some unknown corner of the plain, while Opis is borne away on her wings to airy Olympus.""",
 """'Illum', put first, 'him': the killer of Camilla. 'exspirantem… gementem', 'breathing out… groaning', both with 'illum'. 'extrema', 'his last (groans)', a neuter plural used as an adverbial accusative. 'obliti', 'forgetting', from 'obliviscor'. 'ignoto camporum in pulvere', 'in the unknown dust of the plains', with the genitive 'camporum' dependent on 'pulvere': no one will know where he fell, the opposite of the 'nomen' promised Camilla (846). 'aetherium… Olympum', framing the line. The two clauses stand side by side without a connective (asyndeton). Elisions 'Ill(um) exspirantem', 'soci(i) atque', 'atqu(e) extrema', 'campor(um) in'."""),
(868, 'Camillae;',
 """First flees, its mistress lost, the light wing of Camilla;""",
 """First to flee, now that their mistress was lost, was Camilla's light-armed squadron;""",
 """A new paragraph in Greenough: the rout. 'Prima fugit', 'first flees', with 'fugit' repeated three times in two lines (868–869): the verb is the paragraph. 'domina amissa', ablative absolute, 'their mistress having been lost'. 'levis ala', 'the light wing', the cavalry squadron, here Camilla's own Volscian horse. Elision 'domin(a) amissa'."""),
(871, 'tendunt.',
 """thrown into confusion flee the Rutulians, flees keen Atinas,\nand the scattered leaders and the deserted companies\nsafe places seek, and on their horses, turned away, toward the walls make.""",
 """the Rutulians flee in confusion, and keen Atinas flees, and the scattered captains and leaderless companies make for safety and, turning their horses, ride for the walls.""",
 """'Rutuli', the Rutulians, Turnus's own people. 'acer Atinas', 'keen Atinas', a Rutulian captain; Virgil names him again in Book XII. 'disiecti', 'scattered', from 'disicio', where the 'i' after the prefix is a consonant (dis-iec-ti). 'desolati', 'abandoned', without their commanders. 'manipli', 'companies', shortened from 'manipuli', the infantry unit, an anachronism from the Roman army. 'tuta', 'safe places', a neuter plural adjective used as a noun. 'aversi', 'turned away', backs to the enemy. Elision 'avers(i) ad'."""),
(875, 'campum.',
 """Nor anyone, the pressing Teucrians and death bringing,\nto withstand is able with weapons or to stand against,\nbut slack they carry back on shoulders drooping their bows,\nand of the four-footed the crumbling with running shakes the hoof plain.""",
 """No one can hold back the Trojans as they press on bringing death, or make a stand against them with weapons; they carry their bows unstrung on drooping shoulders, and the hooves of the galloping horses shake the crumbling plain.""",
 """'instantis Teucros… ferentis', 'the Teucrians pressing on… bringing', with the '-is' accusative plurals. 'sustentare', 'to hold up, withstand'; 'sistere contra', 'to make a stand against (them)'. 'laxos… arcus', 'slack bows', framing the line: the archers have given up. 'quadrupedum… ungula', 'the hoof of the four-footed (beasts)', a collective singular. The last line gallops, mostly in dactyls, and echoes VIII.596 ('quadrupedante putrem sonitu quatit ungula campum'). 'putrem', 'crumbling', the dry, loose earth. The Latin Library spells 'quadripedumque', the same word. Elision 'quisqu(am) instantis'."""),
(878, 'tollunt.',
 """Rolls toward the walls, with murk thick, black,\nthe dust, and from the look-outs, beaten in their breasts, the mothers\na womanly clamour to the stars of the sky raise.""",
 """A cloud of dust rolls toward the walls, thick with black murk, and from the watch-towers the mothers, beating their breasts, raise the cry of women to the stars of heaven.""",
 """'Volvitur… pulvis', 'rolls… the dust', the verb first and the subject held to the next line. 'caligine turbidus atra', 'thick with black murk'. 'e speculis', 'from the look-outs', the towers on the walls. 'percussae pectora', 'struck in respect of their breasts', the Greek accusative (accusative of respect) with a passive participle: they beat their breasts in grief. 'femineum clamorem', 'a womanly shout', the shrill wailing of women, as when Troy fell (II.487–488). 'ad caeli sidera', an epic hyperbole, as at 832–833. Elision 'clamor(em) ad'."""),
(880, 'turba;',
 """Who in their running the gates first burst through, standing open,\nthese the hostile on top, with mingled column, presses the crowd;""",
 """Those who were first to burst at a run through the open gates find the enemy crowd pressing on top of them in a mingled throng;""",
 """'Qui… hos', 'who… these', the relative clause first and the demonstrative picking it up, a common Latin order. 'inrupere', 'burst in', '-ere' for '-erunt', and with the prefix 'in-' unassimilated (Greenough's spelling of 'irrupere'). 'patentis', 'standing open', '-is' accusative plural. 'mixto… agmine', 'in a mingled column', pursuers and pursued pouring in together. 'super', adverb, 'on top'. The same danger faces Troy in Iliad XXI, when Priam orders the gates opened to the fleeing Trojans and Achilles is close behind (from memory). Elision 'prim(i) inrupere'."""),
(883, 'animas.',
 """nor wretched do they escape death, but on the threshold itself,\nwithin their fathers' walls and amid the safe places of their homes,\npierced through they breathe out their lives.""",
 """they do not escape a pitiful death, but on the very threshold, inside the walls of their fathers and among the safe places of their homes, they are run through and breathe out their souls.""",
 """'miseram… mortem', 'wretched death', framing the clause. 'limine in ipso', 'on the very threshold', of the gate. 'moenibus in patriis', 'in their ancestral walls'. 'inter tuta domorum', 'among the safe places of their homes', a neuter plural adjective with a genitive, a favourite turn of Virgil's ('strata viarum'). The three phrases build up: they die where they should have been safe. 'confixi', 'pierced through'. 'exspirant animas', 'breathe out their lives', 'anima' as breath and life. Elisions 'miser(am) effugiunt', 'limin(e) in', 'atqu(e) inter', 'confix(i) exspirant'."""),
(883, 'portas:',
 """Some to shut the gates:""",
 """Some set about shutting the gates:""",
 """'Pars claudere portas', 'a part (begins) to close the gates', a historic infinitive: the infinitive used as a main verb in vivid narrative, with its subject in the nominative (Allen & Greenough treats it under the infinitive). 'Pars' will be picked up by 'pars… pars' at 888–889, other groups of the fleeing. The colon introduces what this means for those still outside. No elisions."""),
(886, 'ruentum.',
 """neither to their comrades to open a way nor into the walls do they dare\nto receive them begging, and there arises a most pitiful slaughter\nof those defending with arms the entrances and onto the arms of those rushing.""",
 """they dare not open a way for their comrades or let them inside the walls, however they plead, and a most pitiful slaughter begins, of men defending the entrances with arms and men rushing onto those arms.""",
 """'nec… nec', 'neither… nor', both infinitives with 'audent', 'they dare'. 'moenibus… accipere', 'to receive within the walls', the ablative of place. 'orantis', 'those begging', a participle used as a noun, '-is' accusative plural. 'miserrima caedes', 'a most pitiable slaughter'. 'defendentum… ruentum', 'of men defending… of men rushing', two genitive plurals in Greenough's old '-um' for '-ium', set at either end of the line: the slaughter is of Latins by Latins. 'aditus', accusative plural, 'the approaches'. Elisions 'accipe(re) orantis', 'defendent(um) armis', 'inqu(e) arma'."""),
(890, 'postis.',
 """Shut out, before the eyes and of their weeping the faces of parents,\nsome into the steep ditches, with the crush pressing,\nroll, with let-loose some, blind and spurred, reins\nram at the gates and the hard with bar door-posts.""",
 """Shut out, before the eyes and faces of their weeping parents, some roll down into the steep ditches as the crush drives them on; others, blind and frantic, gallop with loosened reins and batter like rams at the gates and the door-posts made fast with the bar.""",
 """'Exclusi', 'shut out', masculine plural with 'pars', agreement by sense. 'lacrumantum', Greenough's spelling of 'lacrimantum', 'weeping', with the '-um' genitive plural again. 'pars… pars', 'some… others'. 'praecipitis fossas', 'the steep ditches', '-is' accusative plural. 'urgente ruina', ablative absolute, 'with the crash (of the crowd) pressing'. 'immissis… frenis', 'with reins let go', framing the phrase. 'arietat', 'butts like a ram', from 'aries', the battering-ram; the 'i' is a consonant, so the word has three syllables (ar-ye-tat). 'obice', 'with the bar', ablative with 'duros'; 'postis', accusative plural. Elisions 'exclus(i) ante', 'lacrumantumqu(e) ora', 'caec(a) et'."""),
(895, 'ardent.',
 """The very mothers from the walls, in the utmost contest,\n(shows them true love of country) as they saw Camilla,\nweapons with their hands, trembling, hurl, and with oak hard,\nwith stakes, iron and with poles imitate burnt-hardened,\nheadlong, and to be first to die before the walls they burn.""",
 """The mothers themselves, vying with each other on the walls, hurl weapons with trembling hands (true love of their country shows them the way) as they had seen Camilla do; with hard oak, with stakes and fire-hardened poles, they make do for iron, rushing headlong, burning to be the first to die for their walls.""",
 """'Ipsae… matres', 'the mothers themselves', framing the line. 'summo certamine', 'in the utmost rivalry', vying with each other. 'monstrat amor verus patriae', 'true love of country shows (them)', a parenthesis. 'ut videre Camillam', 'as they had seen Camilla', following her example; 'videre' is '-ere' for '-erunt'. 'robore… stipitibus… sudibus', 'with oak, with stakes, with poles', the ablatives of means: 'ferrum… imitantur', 'they imitate iron', make wood serve for steel. 'obustis', 'burnt at the end', hardened in fire. 'praecipites', 'headlong'. 'mori… ardent', 'burn to die', the infinitive with a verb of desire. Elisions 'patri(ae) ut', 'sudibusqu(e) imitantur'."""),
(897, 'tumultum:',
 """Meanwhile Turnus in the woods most savage fills\na message, and to the young man a huge brings Acca turmoil:""",
 """Meanwhile in the woods the cruellest of news reaches Turnus and fills his mind; Acca brings the young man word of the great disaster:""",
 """A new paragraph in Greenough. 'Turnum… implet nuntius', 'the message fills Turnus', takes possession of him. 'saevissimus', 'most savage', the cruellest news. Turnus has been lying in ambush in a wooded valley, waiting for Aeneas to come over the ridge (XI.511–531). Acca is Camilla's comrade, sent by the dying Camilla with her last message (XI.820–827). 'tumultum', 'uproar, disorder', here the news of the rout. 'iuveni', 'the young man', Turnus, as often. The colon introduces what she tells him. Elisions 'Turn(um) in', 'iuven(i) ingentem'."""),
(900, 'ferri.',
 """destroyed the Volscians' lines, to have fallen Camilla,\nto be rushing on the hostile enemies, and with Mars favourable\nall things to have seized, fear now to the walls to be carried.""",
 """that the Volscian lines are destroyed and Camilla has fallen, that the enemy are pressing on in their fury and with the war going their way have carried all before them, and that panic is already spreading to the walls.""",
 """Indirect statement depending on 'fert', 'she reports': 'deletas (esse) acies', 'cecidisse Camillam', 'ingruere hostis', 'corripuisse', 'metum… ferri', the infinitives piled up without connectives (asyndeton), as a breathless messenger speaks. 'Volscorum', the Volscians, Camilla's people. 'infensos hostis', 'the hostile enemy', '-is' accusative plural. 'Marte secundo', ablative absolute, 'with Mars favourable', Mars for war, a metonymy. 'omnia corripuisse', 'have seized everything'. Elisions 'Volscor(um) acies', 'ingruer(e) infensos', 'i(am) ad'."""),
(902, 'linquit.',
 """He, raging (and the savage of Jove so will drives),\nabandons the beset hills, the woods rough he leaves.""",
 """In his fury (and so the cruel will of Jupiter drives him on) he abandons the hills he was holding and leaves the rough woods.""",
 """'Ille furens', 'he, raging', Turnus. 'et saeva Iovis sic numina pellunt', a parenthesis, 'and so the cruel will of Jove drives (him)': 'numina', 'divine powers', the plural for the god's will. By leaving the ambush Turnus lets Aeneas through the pass, as the next lines show. The Latin Library reads 'poscunt', 'demand', which makes Jupiter's will an order rather than a force pushing him. 'obsessos collis', 'the hills he had beset', where he lay in wait, '-is' accusative plural. 'deserit… linquit', the same act said twice. Elision 'nemor(a) aspera'."""),
(905, 'opaca.',
 """Scarcely from sight had he gone out, and the plain was holding,\nwhen father Aeneas, the passes having entered, open,\nboth overcomes the ridge and from the wood comes out, dark.""",
 """Scarcely had he gone out of sight and reached the plain, when father Aeneas entered the pass, now unguarded, crossed the ridge and came out of the dark forest.""",
 """'Vix… exierat… tenebat, cum…', 'scarcely had he gone… when…', the 'inverted cum': the main event comes in the 'cum' clause. 'pater Aeneas', the title of the founder. 'saltus… apertos', 'the passes, open', now that Turnus has left them unguarded. 'ingressus', 'having entered', may be taken as a finite verb with 'est' left out, so that '-que' on 'exsuperat' joins it to what follows. 'exsuperat iugum', 'surmounts the ridge'. 'silva… opaca', framing the line's end. 'Aeneas' is three syllables, the 'Ae-' one long syllable. Elisions 'conspect(u) exierat', 'silvaqu(e) evadit'."""),
(907, 'absunt;',
 """So both to the walls, swift, with all their\ncolumn are borne, and not by long between each other paces are apart;""",
 """So both of them are hurrying toward the walls with all their columns, and they are not many paces apart;""",
 """'ambo', 'both', Turnus and Aeneas, each at the head of his army. 'rapidi', 'swift', an adjective doing an adverb's work. 'toto… agmine', 'with their whole column', run over the line-end. 'feruntur', 'are borne along', the passive of hurrying movement. 'nec longis inter se passibus absunt', 'and are not apart from each other by long paces', litotes: they are close. The ablative 'passibus' gives the measure of difference. Elision 'amb(o) ad'."""),
(911, 'equorum.',
 """and at the same time as Aeneas the smoking with dust plains\nsaw ahead, far, and the Laurentine columns saw,\nso savage Aeneas recognised Turnus in arms\nand the coming of feet and the snorting heard of horses.""",
 """and as soon as Aeneas looked out and saw the plains smoking with dust far off and saw the Laurentine columns, Turnus too recognised Aeneas in his savage armour and heard the tramp of marching feet and the snorting of horses.""",
 """'simul… et', 'at the same time as… so also', the two sightings set side by side. 'fumantis… campos', 'the plains smoking with dust', '-is' accusative plural. 'Laurentia agmina', 'the Laurentine columns', the Latin army. 'Aenean', the Greek accusative. 'saevum… in armis', 'savage in arms'. 'adgnovit', 'recognised', Greenough's unassimilated spelling of 'agnovit'. 'pedum', 'of feet', of the infantry. 'flatus… equorum', 'the snortings of the horses', framing the line's end. Elisions 'Laurentiaqu(e) agmina', 'saev(um) Aenean'."""),
(914, 'reducat:',
 """And at once they would enter the fights and try the battles,\nif not rosy weary already in the flood Phoebus Iberian\ndipped his horses, and night, the day gliding away, brought back:""",
 """And at once they would have joined battle and tried the issue, had not rosy Phoebus already been bathing his weary horses in the Iberian flood and bringing back the night as the day slipped away:""",
 """An unreal condition, 'ineant… temptent, ni… tinguat… reducat', with present subjunctives where prose would use the imperfect, which makes it vivid: they are on the point of fighting. 'Phoebus', the Sun, driving his chariot into the sea at evening. 'gurgite… Hibero', 'in the Iberian flood', the ocean beyond Spain in the far west, where the sun sets; Hiberus is the Ebro. 'tinguat', Greenough's spelling of 'tingat', 'dips'. 'die labente', ablative absolute, 'as the day slips away'. Night parts the armies in Homer too (Iliad VII.282, VIII.485–486, from memory). Elision 'continuoqu(e) ineant'."""),
(915, 'vallant.',
 """they encamp in their camp before the city, and the walls entrench.""",
 """they pitch camp before the city and entrench themselves by the walls.""",
 """The last line of Book XI. 'considunt castris', 'they settle down in camp', with 'castris' ablative of place. 'ante urbem', 'before the city', Latinus's city. 'moenia vallant', 'fortify the walls with a rampart', 'vallum', the stockade of a camp: both armies dig in, the Trojans their camp, the Latins their walls. The fighting resumes in Book XII, with Turnus's offer to meet Aeneas in single combat. Elision 'urb(em) et'."""),
]

# Speech-mark check exemptions (rule 5b), by unit ln:
#  848: the print closes Opis's lament with a mark set after a space and joined to 'Fuit' ('merita. ”Fuit');
#       t (unit 'Nam quicumque... merita.') lacks the mark, l and i close the speech after 'merita.'.
#  849: the mark stands at the head of t ('”Fuit'); l and i carry none.
EXEMPT = {848, 849}
P = A.part('aeneid-090'); L = A.lines_of(P); paras = {l['n'] for l in L if l['p']}
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
