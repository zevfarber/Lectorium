import json, re
D='/home/user/Lectorium/.github/pipeline/odyssey/drafts/odyssey-029/'
lines={}; para=set()
for raw in open(D+'packet.md',encoding='utf-8'):
    m=re.match(r'^(¶ |  )(\d{3})  (.*)$',raw.rstrip('\n'))
    if m:
        lines[int(m.group(2))]=m.group(3)
        if m.group(1)=='¶ ': para.add(int(m.group(2)))
assert min(lines)==223 and max(lines)==331 and len(lines)==109

U=[]
def u(start,l,i,n,p=False,mark=None):
    U.append(dict(start=start,l=l,i=i,n=n,p=p,mark=mark))

u((223,None),
 "So he spoke, and they went apart, and told it then to the girl.",
 "So he spoke, and the attendants went a little way off and told it to the girl.",
 "This closes Odysseus's speech from 6.218; ὣς ἔφαθ’ is 'so he spoke', with ἔφαθ’ the elided ἔφατο (imperfect of φημί), its τ turned to θ before the rough breathing of αἱ. αἱ is a pronoun, 'they', the attendants. ἴσαν is the imperfect 3 pl. of εἶμι 'go', and ἀπάνευθεν means 'apart, at a distance'. εἶπον is 'they told' (the thing said is left to be understood), and κούρῃ is the dative with Ionic -ῃ where Attic has κόρῃ, 'to the girl', Nausicaa.",p=True)
u((224,None),
 "But he from the river washed off his skin, heavenly Odysseus,\nthe brine that covered his back and his broad shoulders,\nand from his head he wiped the foam of the unharvested salt-sea.",
 "Heavenly Odysseus washed from his skin, in the river, the brine that covered his back and broad shoulders, and wiped from his head the foam of the sea that yields no harvest.",
 "νίζετο takes two accusatives, the skin (χρόα) and the brine (ἅλμην) washed off it: 'he washed the brine from his skin'. ἥ is the relative 'which', and οἱ is a dative of the person, 'his'. εὐρέας is the uncontracted accusative plural (Attic εὐρεῖς). ἄμπεχεν is ἀμφί + ἔχω with the ἀμφ- reduced before π, 'covered'. δῖος Ὀδυσσεύς is 'heavenly Odysseus'. ἀτρυγέτοιο is a genitive in -οιο, the stock epithet of the sea, and its meaning is not known: 'unharvested' (from ἀ- and τρυγάω, 'gather in') is the traditional guess, with 'unresting' or 'barren' also proposed.")
u((227,None),
 "But when he had washed all, and anointed himself richly,\nand about him put on the clothes that the unwed maiden gave him,",
 "When he had bathed all over and anointed himself richly, and put on the clothes the unwed maiden had given him,",
 "λοέσσατο is the aorist middle of λούω (Attic ἐλούσατο), without augment, and ἄλειψεν the aorist of ἀλείφω 'anoint'; λίπ’ is λίπα, 'richly, with oil'. ἀμφὶ … ἕσσαθ’ is tmesis for ἀμφιέσσατο, 'clothed himself in' (ἕσσαθ’ is elided ἕσσατο, aorist middle of ἕννυμι), with εἵματα 'clothes' as object. ἅ is the relative 'which', οἱ 'to him', and πόρε an unaugmented aorist of πόρω 'gave'. παρθένος ἀδμής is 'the unwed maiden', Nausicaa, whose gift this is (6.214).")
u((229,None),
 "him then Athena, sprung of Zeus, made\ntaller to look upon and thicker, and down from his head\nshe sent curling locks, like the hyacinth flower.",
 "Athena, the daughter sprung from Zeus, made him taller to look at and sturdier, and let curling locks fall from his head, like the hyacinth flower.",
 "τὸν is the pronoun 'him', not the article; τὸν μέν has no matching δέ, and the sentence simply runs on. θῆκεν is an unaugmented aorist of τίθημι, 'made', and Διὸς ἐκγεγαυῖα is the perfect participle of ἐκγίγνομαι, 'having sprung from Zeus'. μείζονα is 'taller', πάσσονα 'thicker, sturdier' (comparative of παχύς), and εἰσιδέειν the uncontracted infinitive 'to look at'. κὰδ … ἧκε is tmesis for κατῆκε, with κὰδ standing for κατά before δ: 'let down'. κάρητος is a genitive of κάρη 'head'. ὑακινθίνῳ ἄνθει is 'the hyacinth flower', a flower whose modern identity is uncertain.")
u((232,None),
 "And as when a man pours gold about silver,\nskilled, one whom Hephaestus taught and Pallas Athena\nevery craft, and graceful works he brings to completion,\nso then on him a grace she poured-down, on head and on shoulders.",
 "As when a skilled man overlays silver with gold, one whom Hephaestus and Pallas Athena have taught every craft, and he brings graceful works to completion, so she shed a grace upon his head and shoulders.",
 "A simile: ὡς δ’ ὅτε is 'as when' and ὣς ἄρα 'so then' answers it. The craftsman (ἴδρις 'skilled') pours gold about silver, that is, gilds it; περιχεύεται is middle. δέδαεν is an aorist of δάω 'teach' with two accusatives, the man and τέχνην παντοίην 'every craft'; Hephaestus is the divine smith and Pallas Athena the patroness of craft. τελείει is the uncontracted present of τελέω 'complete'. κατέχευε … χάριν is 'poured down a grace', the same image as the gold; τῷ is 'on him', and κεφαλῇ τε καὶ ὤμοις is a dative of place.")
u((236,None),
 "He sat down then, going apart, on the shore of the sea,\nglistening in beauty and grace;",
 "Then he went apart and sat down on the sea-shore, glistening with beauty and grace;",
 "ἕζετ’ is elided ἕζετο, 'sat down', and κιών the participle of κίω 'go'. θῖνα is the accusative of θίς 'shore, beach', and ἀπάνευθε 'apart'. κάλλεϊ is the dative of κάλλος with its two vowels kept apart (Attic κάλλει), and χάρισι the dative plural of χάρις; στίλβων 'glistening' is what the grace of the last unit has done to him. The ano teleia ends the unit before the girl's reaction.")
u((237,'θηεῖτο'),
 "and the girl gazed at him.",
 "and the girl looked on in wonder.",
 "θηεῖτο is the imperfect middle of θηέομαι 'gaze at with wonder' (Attic θεάομαι), without the augment. It has no object expressed; the object is Odysseus. κούρη is Ionic for κόρη, 'girl', here Nausicaa.")
u((238,None),
 "Then indeed among the fine-plaited attendants she spoke:",
 "Then she spoke among the fine-plaited attendants:",
 "A speech introduction with the pattern of δή ῥα τότ’ … μετηύδα: ῥα is ἄρα, 'then indeed', and μετηύδα 'spoke among' takes the dative. The unnamed speaker is Nausicaa. ἀμφιπόλοισιν is 'attendants' and ἐυπλοκάμοισι 'fine-plaited', an adjective built on πλόκαμος 'lock, braid'; both are datives plural in -οισι(ν).")
u((239,None),
 "“Hear me, white-armed attendants, that I may say something.",
 "“Hear me, white-armed attendants, so that I may say something.",
 "κλῦτέ is the aorist imperative of κλύω 'hear', with μευ (epic for μου) in the genitive, as verbs of hearing take. ἀμφίπολοι, vocative, is 'attendants', and λευκώλενοι 'white-armed', a stock epithet of women. ὄφρα is 'so that' with the aorist subjunctive εἴπω, and τι 'something'.",p=True,mark="Nausicaa speaks")
u((240,None),
 "Not against the will of all the gods, who hold Olympus,\nwith the godlike Phaeacians does this man mingle;",
 "It is not against the will of all the gods who hold Olympus that this man is coming among the godlike Phaeacians;",
 "οὐ πάντων ἀέκητι θεῶν is 'not against the will of all the gods', a way of saying that some god, at least, has willed it. ἀέκητι takes the genitive. Φαιήκεσσ’ is the dative in -εσσι (elided), governed by ἐπιμίσγεται, 'mixes with, consorts with'. ἀντιθέοισι is 'godlike'. οἳ is the relative 'who', and Ὄλυμπον ἔχουσιν 'hold Olympus'.")
u((242,None),
 "For before, indeed, to me unseemly he seemed to be,\nbut now he is like the gods, who hold the wide sky.",
 "For at first he seemed to me unseemly, but now he is like the gods who hold the wide sky.",
 "δέατ’ is elided δέατο, an epic aorist 'seemed', here with the infinitive εἶναι. ἀεικέλιος is 'unseemly, unsightly'. θεοῖσιν ἔοικε takes the dative, 'is like the gods', and τοί is here the relative 'who' (not the article). οὐρανὸν εὐρύν is 'the wide sky'.")
u((244,None),
 "Would that to me such a man, as husband called, might be\ndwelling here, and that it might please him to remain on this very spot.",
 "If only such a man as this could be called my husband, and live here, and be glad to stay right here.",
 "αἲ γάρ with the optative (εἴη, ἅδοι) opens a wish, 'if only'. κεκλημένος is the perfect middle participle of καλέω, so πόσις κεκλημένος εἴη is 'might be called husband'. ἐμοί is the dative 'to me' (my husband). ναιετάων is the uncontracted present participle of ναιετάω 'dwell'. ἅδοι is the optative of ἁνδάνω 'be pleasing', with οἱ 'to him', and αὐτόθι means 'on the very spot, right here'. The wish is Nausicaa's own, spoken to her maids and never to him.")
u((246,None),
 "But give, attendants, to the stranger both food and drink.”",
 "So give the stranger food and drink, attendants.”",
 "The line repeats 6.209 word for word up to the comma; there the sentence went on to the bathing, which is now done. δότ’ is the elided aorist imperative of δίδωμι 'give', and ξείνῳ the dative of ξεῖνος 'stranger, guest'. βρῶσίν τε πόσιν τε is 'both food and drink', the pair of words that recurs in the next line. With this the speech ends.")
u((247,None),
 "So she spoke, and they then readily heard her and obeyed,\nand beside Odysseus they set both food and drink.",
 "So she spoke, and they listened to her readily and obeyed, and set food and drink beside Odysseus.",
 "ὣς ἔφαθ’ is 'so she spoke' (see 223 for the form), and αἱ δ’ ἄρα is 'and they then', αἱ a pronoun. κλύον and ἐπίθοντο are unaugmented aorists, 'heard' and 'obeyed'; τῆς is the genitive 'her' that κλύον takes. The two verbs together are a stock way of saying that an order was carried out. πὰρ … ἔθεσαν is tmesis for παρέθεσαν, 'set beside', and Ὀδυσσῆι the dative in -ηι of Ὀδυσσεύς.",p=True)
u((249,None),
 "Indeed he drank and ate, much-enduring, heavenly Odysseus,\ngreedily;",
 "Then he drank and ate, much-enduring, heavenly Odysseus, greedily;",
 "ἦ τοι is 'indeed, truly', and ὁ is the pronoun 'he'. ἦσθε is the imperfect of ἔσθω 'eat', paired with πῖνε 'drank' (unaugmented imperfect of πίνω). πολύτλας δῖος Ὀδυσσεύς is the standing name-formula 'much-enduring, heavenly Odysseus'. ἁρπαλέως is 'greedily, eagerly', and the ano teleia holds the reason back for the next unit.")
u((250,'δηρὸν'),
 "for long he had been of food unfed.",
 "for he had gone a long time without tasting food.",
 "δηρόν is 'for a long time', and ἦεν the imperfect of εἰμί (Attic ἦν). ἄπαστος, 'not having tasted', is built on the negative ἀ- and takes the genitive ἐδητύος 'of food', as adjectives of lack do.")
u((251,None),
 "But white-armed Nausicaa devised another thing:",
 "But white-armed Nausicaa thought of something else:",
 "A formula for a mind turning to a new plan: ἄλλ’ is ἄλλο, 'another thing', the object of ἐνόησεν 'thought of, devised'. Here it is filled with Nausicaa's name and her epithet λευκώλενος 'white-armed'. What follows is the plan itself, the journey to the city.",p=True)
u((252,None),
 "The clothes then having folded she laid on the fair wagon,\nand yoked the strong-hoofed mules, and up she stepped herself,\nand urged on Odysseus, and spoke a word, and called him by name:",
 "She folded the clothes and laid them on the fair wagon, yoked the strong-hoofed mules, and stepped up herself; then she urged Odysseus on, and spoke, calling him by name:",
 "τίθει is an unaugmented imperfect of τίθημι, 'was laying'. ἀπήνη is the mule-wagon, and ἡμιόνους 'mules', with κρατερώνυχας 'strong-hoofed' (from κρατερός and ὄνυξ 'claw, hoof'). ἂν δ’ ἔβη is tmesis for ἀνέβη, 'mounted', and αὐτή 'herself'. ἔπος τ’ ἔφατ’ ἔκ τ’ ὀνόμαζεν is the formula 'spoke a word and called him by name'. Ὀδυσῆα has a single σ, the metrical variant of Ὀδυσσῆα.")
u((255,None),
 "“Rouse yourself now, stranger, to go to the city, that I may send you\nto my father’s house, wise-minded, where I say you\nwill come to know all the Phaeacians, as many as are best.",
 "“Get up now, stranger, and go to the city, so that I may send you to the house of my wise-hearted father, where I tell you you will come to know all the best of the Phaeacians.",
 "ὄρσεο is the aorist middle imperative of ὄρνυμι 'rouse yourself, get up'. ἴμεν is the epic infinitive of εἶμι 'go', and πόλινδ’ has the direction suffix -δε, 'to the city'. ὄφρα with the aorist subjunctive πέμψω gives purpose. δαΐφρονος, of Alcinous, is disputed: 'wise-minded' (from δαῆναι 'learn') is followed here, though 'warlike' (δάιος) is the other ancient reading. φημί with the accusative and infinitive is 'I say that you will …', and εἰδησέμεν the future infinitive of οἶδα 'know'. ὅσσοι ἄριστοι is 'as many as are best'.",mark="Nausicaa speaks")
u((258,None),
 "But do just this, and you seem to me not to lack sense:",
 "But do just this, for you seem to me a man not lacking in sense:",
 "ἔρδειν is an infinitive used as an imperative, 'do', and μάλ’ ὧδ’ 'just so'. δοκέεις is the uncontracted δοκεῖς. οὐκ ἀπινύσσειν, 'not to lack sense', is a litotes for 'you are sensible'; ἀπινύσσω is built on ἀ- and the root of πινυτός, the word behind πεπνυμένος.")
u((259,None),
 "So long as we go through the fields and the works of men,\nso long with the attendants after the mules and the wagon\nquickly go;",
 "As long as we are passing the fields and the works of men, go quickly along with the attendants behind the mules and the wagon;",
 "ὄφρ’ ἂν … κ’ … τόφρα is 'as long as … for that long', with the short-vowel subjunctive ἴομεν 'we go'; κ’ is κεν, the same as ἄν. ἔργ’ ἀνθρώπων is 'the works of men', the tilled land. μεθ’ ἡμιόνους καὶ ἄμαξαν is 'after (in the wake of) the mules and the wagon'. ἔρχεσθαι is an infinitive used as an imperative, as ἔρδειν was at 258.")
u((261,'ἐγὼ δ’'),
 "but I the way will lead.",
 "and I will lead the way.",
 "ἐγὼ δ’ is 'but I', set against the attendants who will follow behind. ἡγεμονεύσω is future (or aorist subjunctive) of ἡγεμονεύω 'lead', and ὁδόν is 'the way' as its object.")
u((262,None),
 "But when we set foot on the city, around which is a tower\nhigh, and fair a harbour on either side of the city,\nand narrow the entrance;",
 "But when we come to the city, around which stands a high tower, with a fair harbour on either side of it and a narrow entrance;",
 "ἐπὴν is ἐπεὶ ἄν, and ἐπιβήομεν the aorist subjunctive of ἐπιβαίνω with its vowel stretched (ἐπιβῶμεν), with the genitive πόλιος 'set foot on the city'. ἣν πέρι is 'around which', the preposition placed after its noun. πόλιος and πόληος are two epic genitives of the same word πόλις, and πύργος is 'tower'. εἰσίθμη is 'entrance' and λεπτή 'narrow'. The ἐπήν clause never receives its verb: the description runs on, and she starts afresh at 297.")
u((264,'νῆες'),
 "and the ships, both-sides-curving, along the road\nare drawn up;",
 "and the ships, curved on both sides, are drawn up along the road;",
 "ἀμφιέλισσαι, 'curved on both sides', is an epithet of ships built on ἀμφί and ἑλίσσω 'turn, curve'; the exact sense was not certain in antiquity ('rowed on both sides' is another guess). ὁδόν is an accusative of the way, 'along the road'. εἰρύαται is the 3 pl. perfect passive of ἐρύω 'draw', so 'have been drawn up'.")
u((265,'πᾶσιν'),
 "for to all there is a slip, to each man his own.",
 "for each man has a slip of his own.",
 "ἐπίστιον is glossed 'slip, dock' for a ship, from ἐπί and the root of ἑστία 'hearth'; the sense is only approximately known. πᾶσιν … ἑκάστῳ is 'for all, for each one', the second word narrowing the first.")
u((266,None),
 "And there their meeting-place, around the fair sanctuary of Poseidon,\nwith hauled stones, dug in deep, fitted together.",
 "There, too, is their meeting-place, around the fair sanctuary of Poseidon, fitted together with hauled stones set deep in the earth.",
 "ἔνθα δέ τέ σφ’ is 'and there their …', σφ’ being the elided dative σφι, and τε epic. ἀγορή is the assembly-place. Ποσιδήιον, 'of Poseidon', is a neuter adjective used as a noun, with 'sanctuary' understood. ῥυτοῖσιν λάεσσι is 'with hauled stones' (ῥυτός from ἐρύω 'draw'), and κατωρυχέεσσ’ 'dug down, sunk in the ground' (from κατορύσσω); ἀραρυῖα is the perfect participle of ἀραρίσκω, 'fitted together'. The agreement is with ἀγορή.")
u((268,None),
 "And there they tend the tackle of the black ships,\nthe cables and the sail-cloths, and they sharpen the oars.",
 "There they see to the tackle of the black ships, the cables and the sails, and shave the oars to a point.",
 "ὅπλα is 'gear, tackle', and ἀλέγουσι 'they care for, see to'. νηῶν μελαινάων is 'of the black ships' with the feminine genitive plural in -άων. πείσματα are 'cables', and σπεῖρα 'wrappings, folds', probably the sails or their sail-cloths, though the exact sense is not known. ἀποξύνουσιν is 'they sharpen', and ἐρετμά 'oars'.")
u((270,None),
 "For to the Phaeacians there is no care for bow or quiver,\nbut masts and oars of ships and well-balanced ships,\nin which exulting they cross the grey sea.",
 "For the Phaeacians care nothing for bow or quiver, but for masts and oars and well-balanced ships, glorying in which they cross the grey sea.",
 "μέλει takes a dative of the person and the thing cared for in the nominative: βιός 'bow', φαρέτρη 'quiver', ἱστοί 'masts', ἐρετμά 'oars', νῆες 'ships'. νῆες ἐῖσαι is 'well-balanced ships' (the sense of ἐῖσαι is uncertain). ᾗσιν is a dative feminine plural relative, 'in which', with ἀγαλλόμενοι 'exulting'. περόωσι is the uncontracted περῶσι 'they cross', and πολιὴν θάλασσαν 'the grey sea'.")
u((273,None),
 "Their talk I avoid, the bitter, lest anyone afterwards\nfind fault;",
 "I shun their bitter talk, in case someone should find fault afterwards;",
 "τῶν is 'their', the genitive of the pronoun. ἀλεείνω is 'I avoid, shun', and φῆμιν ἀδευκέα 'bitter talk' (ἀδευκής 'bitter, unkind'). μή with the subjunctive μωμεύῃ is 'lest he find fault' (with me, understood). ὀπίσσω is 'afterwards, later'.")
u((274,'μάλα δ’'),
 "for very overweening are they among the people;",
 "for the people here are very overweening;",
 "μάλα is 'very'. ὑπερφίαλοι is 'overweening, insolent', a word whose formation is unclear; 'overweening' is kept for it, and it is not the word used for ὑπερηνορέοντες, 'overbearing'. κατὰ δῆμον is 'among the people, in the district'.")
u((275,None),
 "and indeed some baser man might thus say, meeting us:",
 "and some baser man who met us might say something like this:",
 "καί νύ is 'and indeed', and εἴπῃσι is the subjunctive in -ῃσι(ν) with the sense 'might say'. κακώτερος is 'baser, of lower sort' and ἀντιβολήσας 'having met (us)'. What follows, down to 284, is the imagined taunt, spoken in the voice of that man.")
u((276,None),
 "‘And who is this that follows Nausicaa, both fair and tall,\nthe stranger?",
 "‘Who is this fine, tall stranger following Nausicaa?",
 "τίς δ’ ὅδε is 'and who is this?'. ἕπεται takes the dative, so Ναυσικάᾳ is 'follows Nausicaa'. καλός τε μέγας τε is 'both fair and tall' (or 'fine and big'), agreeing with ξεῖνος 'stranger'. The Greek question mark ; ends the unit at ξεῖνος.",mark="The imagined taunt")
u((277,'ποῦ δέ'),
 "And where did she find him?",
 "Where did she find him?",
 "μιν is the epic accusative 'him', and εὗρε 'found' has no augment (Attic ηὗρε). The question is asked in the taunter's voice.")
u((277,'πόσις νύ'),
 "A husband, now, to her will he be, to herself.",
 "He is to be her own husband, then.",
 "νυ is 'now, then', with a sneer. οἱ is the dative 'for her', and αὐτῇ 'herself' underlines it: her own, no one else's. ἔσσεται is the epic future of εἰμί (Attic ἔσται).")
u((278,None),
 "Either some wanderer she has taken in from his own ship,\nof men from far-off lands, since none are near;",
 "Either she has taken in some wanderer from his own ship, one of a far-off people, since none live near here;",
 "ἦ … ἤ is 'either … or', the second half at 280. πλαγχθέντα is the aorist passive participle of πλάζω 'driven astray' (compare πλάγχθη in line 2 of the poem). κομίσσατο is the aorist middle of κομίζω 'take in, care for', with doubled σ. ἧς is the possessive 'his own', qualifying νηός; ἀνδρῶν τηλεδαπῶν is 'of men from far-off lands', in the genitive after τινά 'some one'. που is 'perhaps'.")
u((280,None),
 "or for her, praying, some much-prayed-for god has come,\ndescending from heaven, and will hold her all her days.",
 "or some god much prayed to has come down from the sky to her, in answer to her prayer, and will keep her for all her days.",
 "εὐξαμένῃ is the dative of the aorist middle participle of εὔχομαι, 'to her, having prayed'. πολυάρητος is 'much-prayed-for, much-invoked' (from ἀρή 'prayer'). οὐρανόθεν has the suffix -θεν, 'from the sky'. καταβάς is 'having come down'. ἕξει is future of ἔχω, 'will have, will keep', with μιν 'her'; ἤματα πάντα 'all her days'.")
u((282,None),
 "Better, if even herself, having gone about, a husband has found\nfrom elsewhere;",
 "It is better if she has gone out herself and found a husband from elsewhere;",
 "βέλτερον is 'better' with ἐστί understood. καὐτή περ is καὶ αὐτή περ, 'even herself'. ἐποιχομένη is 'going about, going to (seek)', and εὗρεν the aorist 'has found'. ἄλλοθεν is 'from elsewhere'.")
u((283,'ἦ γὰρ'),
 "for she, indeed, these men at least disdains, among the people,\nthe Phaeacians, who woo her, many and good.’",
 "for she scorns these Phaeacians here among the people, who court her, so many and so good.’",
 "ἦ γάρ is 'for truly'. τούσδε γ’ … Φαίηκας is 'these, at least, the Phaeacians', the noun placed last. ἀτιμάζει is 'dishonours, scorns'. τοί is the relative 'who', and μνῶνται 'woo, court' (from μνάομαι). πολέες τε καὶ ἐσθλοί is 'many and good'. The closing mark ’ ends the imagined taunt.")
u((285,None),
 "So they will say, and to me these reproaches would come.",
 "That is what they will say, and it would be a reproach to me.",
 "ὣς is 'so' (accented as the adverb), and ἐρέουσιν the uncontracted future of the verb 'say' (Attic ἐροῦσι). κε with the optative γένοιτο is 'would become', and ὀνείδεα the plural 'reproaches' (Attic ὀνείδη).")
u((286,None),
 "And I am indignant at another too, who such things at least might do,\nwho, against the will of her dear father and mother, they being alive,\nmingles with men, before an open wedding has come.",
 "I would blame any other girl too who did such things, who mingled with men against the will of her dear father and mother, while they live, before a public wedding had come.",
 "νεμεσῶ is 'I am indignant at, I blame', with the dative ἄλλῃ 'another (woman)'. ἥ τις … ῥέζοι is a relative clause with the optative, 'any who should do'. ἀέκητι φίλων … ἐόντων is 'against the will of her dear ones, being (alive)', with φίλων the parents. μίσγηται is the subjunctive of μίσγομαι 'mingle with, consort with', and ἀμφάδιον 'open, public' qualifies γάμον. πρίν γε takes the infinitive ἐλθεῖν 'before … has come'.")
u((289,None),
 "Stranger, and you quickly from me take in the word, so that soonest\nescort and homecoming you may get from my father.",
 "Stranger, quickly now take in my words, so that you may soonest obtain from my father an escort and your homecoming.",
 "ἐμέθεν is 'from me' (epic ἐμέθεν, with the -θεν suffix), and ξυνίει the imperative of συνίημι, 'take in, understand'; ἔπος is the word, or words, she has just said. ὄφρα … τύχῃς is purpose with the aorist subjunctive of τυγχάνω, which takes the genitives πομπῆς 'escort' and νόστοιο 'homecoming'. παρὰ πατρὸς ἐμοῖο is 'from my father'.")
u((291,None),
 "You will find a splendid grove of Athena near the path,\nof poplars;",
 "Near the road you will find a splendid grove of Athena, a grove of poplars;",
 "δήεις is the future of an old verb 'find' (epic 2 sg.). ἀγλαόν is 'splendid', and ἄλσος 'grove'. ἄγχι takes the genitive κελεύθου, 'near the path'. αἰγείρων is the genitive plural of αἴγειρος 'poplar' (the black poplar), 'a grove of poplars'.")
u((292,'ἐν δὲ'),
 "and in it a spring flows, and around it a meadow;",
 "and a spring flows in it, and a meadow lies around;",
 "The verbs are left out in the second half: ἀμφὶ δὲ λειμών is 'and around (it) a meadow'. ἐν δέ is 'and in it', κρήνη 'spring', and νάει the present of νάω 'flow'.")
u((293,None),
 "And there my father’s precinct and his flourishing orchard,\nso far from the city as a man, having shouted, makes himself heard.",
 "There are my father’s precinct and his flourishing orchard, as far from the city as a man’s shout carries.",
 "τέμενος is land cut off and set apart for a king, here 'precinct'; ἀλωή is 'orchard, vineyard, garden', and τεθαλυῖα the perfect participle of θάλλω, 'flourishing'. τόσσον … ὅσσον is 'as far … as'. γέγωνε is a perfect with present sense, 'makes himself heard', and βοήσας 'having shouted'. πτόλιος is again an epic genitive of πόλις.")
u((295,None),
 "There, sitting down, wait for a time, until we\nto the city go and reach my father’s house.",
 "Sit down there and wait a while, until we have come to the city and reached my father’s house.",
 "μεῖναι is the aorist infinitive of μένω 'wait', used as an imperative. εἰς ὅ κεν is 'until', with the subjunctives ἔλθωμεν and ἱκώμεθα (the latter from ἱκνέομαι 'reach'). ἄστυδε has the suffix -δε, 'to the city', and καθεζόμενος is 'sitting down'.")
u((297,None),
 "But when you expect that we have come to the house,\nthen go to the city of the Phaeacians and ask for\nthe house of my father, great-spirited Alcinous.",
 "But when you think we have reached the house, then go into the city of the Phaeacians and ask for the house of my father, great-spirited Alcinous.",
 "ἐπὴν … ἔλπῃ is 'when you expect', the subjunctive of ἔλπομαι. ἡμέας is 'us' (Attic ἡμᾶς), with ἀφῖχθαι, the perfect infinitive of ἀφικνέομαι 'to have arrived'. ποτί is πρός, 'to'. ἴμεν and ἐρέεσθαι (from ἐρέομαι 'ask') are infinitives used as imperatives, as before. μεγαλήτορος is 'great-spirited', the standing epithet of men of high standing.")
u((300,None),
 "Easily known it is, and even a child could lead you,\na small one;",
 "It is easily known, and even a small child could lead you there;",
 "ῥεῖα is 'easily' (Attic ῥᾳδίως), and ἀρίγνωτ’ is ἀρίγνωτα, 'easy to recognise', the neuter plural agreeing with δώματα (299) though ἐστί is singular, as neuter plurals allow. ἂν … ἡγήσαιτο is a potential optative, 'could lead', and πάϊς is παῖς 'child'. νήπιος is 'young, childish'.")
u((301,'οὐ μὲν'),
 "For not at all like to them are the houses of the Phaeacians made,\nsuch a house as is the house of Alcinous\nthe hero.",
 "For the houses of the Phaeacians are nothing like it: such is the house of the hero Alcinous.",
 "ἐοικότα is the perfect participle of ἔοικα, 'be like', with the dative τοῖσι, here 'to those (other houses)'; τέτυκται is the perfect passive of τεύχω 'make', and οὐ … τι 'in no way'. οἷος is 'such as', of the kind of house it is. ἥρωος is a title of honour, 'the hero', for a man of rank.")
u((303,'ἀλλ’ ὁπότ’'),
 "But when the house and the court have hidden you within,\nvery swiftly through the hall to go, until you reach\nmy mother;",
 "But when the house and the courtyard have taken you in, go very quickly through the hall, until you reach my mother;",
 "ὁπότ’ ἄν … κεκύθωσι is 'whenever … have hidden', the perfect subjunctive of κεύθω 'hide, enclose', and αὐλή is the courtyard. διελθέμεν is the epic infinitive of διέρχομαι, used as an imperative. μεγάροιο is a genitive of the way, 'through the hall'. ὄφρ’ ἂν ἵκηαι is 'until you reach' (ἵκηαι = ἵκῃ, subjunctive), and μητέρ’ ἐμήν 'my mother', Arete.")
u((305,'ἡ δ’ ἧσται'),
 "and she sits at the hearth in the firelight,\nturning sea-purple yarn, a wonder to behold,\nleaning against a pillar;",
 "She sits at the hearth in the glow of the fire, twirling sea-purple yarn, a wonder to see, leaning against a pillar;",
 "ἡ is 'she' (a pronoun), and ἧσται the present of ἧμαι 'sit'. ἐσχάρῃ is the hearth, and αὐγῇ 'glow, gleam'. ἠλάκατα is the wool on the distaff or the thread spun from it, and στρωφῶσ’ is 'turning, twirling'; ἁλιπόρφυρα is 'sea-purple' (a dye taken from the sea). θαῦμα ἰδέσθαι is 'a wonder to see', with the aorist middle infinitive. κίονι κεκλιμένη is 'leaning against a pillar'.")
u((307,'δμωαὶ'),
 "and maidservants for her sit behind.",
 "and her maids sit behind her.",
 "δμωαί is Ionic for δμῳαί, 'maidservants'. οἱ is a dative of possession, 'her'. εἵατ’ is elided εἵατο, the epic 3 pl. of ἧμαι, 'they sit' (perfect in form, present in sense).")
u((308,None),
 "And there my father’s throne is leaned toward it,\non which he drinks wine, sitting, like an immortal.",
 "And there my father’s throne leans up against it, and on it he sits and drinks his wine like an immortal.",
 "ποτικέκλιται is the perfect passive of κλίνω, 'has been leaned towards'. αὐτῇ is feminine, so it must mean the hearth or the queen; the Greek does not say which, and the English leaves it as 'it'. τῷ is 'on which', and ὅ γε 'he'. οἰνοποτάζει is 'drinks wine', ἐφήμενος 'sitting on it', and ἀθάνατος ὥς 'like an immortal', with the accent on ὥς because it follows its noun.")
u((310,None),
 "Passing by him, about my mother’s knees your hands\nthrow, that the homecoming day you may see\nrejoicing quickly, even if you are very far off.",
 "Pass him by and throw your hands round my mother’s knees, so that you may see the day of your homecoming with joy, and soon, even if you come from very far away.",
 "τὸν is 'him', the father on his throne. παραμειψάμενος is 'having passed by'. βάλλειν is an infinitive used as an imperative, 'throw'; to clasp the knees is the gesture of a suppliant. ἡμετέρης, 'our', stands for 'my', as the plural does. ἵνα … ἴδηαι is purpose, the aorist subjunctive of ὁράω (ἴδηαι = ἴδῃ), and νόστιμον ἦμαρ 'the day of homecoming'. τηλόθεν is 'from afar'.")
u((313,None),
 "If she, for her part, thinks kindly toward you in her heart,\nhope for you then to see your dear ones and to reach\nyour well-built home and your own fatherland.”",
 "If she is kindly disposed to you in her heart, then there is hope that you will see your dear ones and reach your well-built home and your own native land.”",
 "εἴ κέν … φρονέῃσ’ is a condition with the subjunctive, 'if she should think', and φίλα 'kindly' is an adverb. κείνη is Ionic for ἐκείνη, 'she'. ἐλπωρή is 'hope', with ἐστί understood, and ἰδέειν and ἱκέσθαι are the infinitives. οἶκον ἐυκτίμενον is 'well-built home', and σὴν … πατρίδα γαῖαν 'your own fatherland'. With these words Nausicaa's long speech ends.")
u((316,None),
 "So then having spoken, she lashed with a shining whip\nthe mules;",
 "So she spoke, and lashed the mules with her shining whip;",
 "ὣς ἄρα φωνήσασ’ is 'so then having spoken'. ἵμασεν is the aorist of ἱμάσσω 'lash', and μάστιγι φαεινῇ 'with a shining whip'. The mules are in the accusative ἡμιόνους, and the unit stops at the ano teleia, before αἱ 'they'.",p=True)
u((317,'αἱ δ’ ὦκα'),
 "and they swiftly left the river’s streams.",
 "and they quickly left the river’s streams.",
 "αἱ is feminine, 'they', the mules. λίπον is an unaugmented aorist of λείπω, and ὦκα 'swiftly'. ῥέεθρα is 'streams', the flowing water of the river.")
u((318,None),
 "and they ran well, and well they strode out with their feet;",
 "and they ran well, and well they strode out with their feet;",
 "τρώχων is an unaugmented imperfect of τρώχω 'run', and πλίσσοντο the imperfect of πλίσσομαι, 'step out, stride' (literally 'spread the legs'). ἐὺ μέν … ἐὺ δέ, 'well … and well', repeats the adverb for emphasis, and πόδεσσιν is the dative in -εσσι.")
u((319,None),
 "And she drove right well, so that together they might follow on foot,\nboth the attendants and Odysseus, and with judgment she laid on the lash.",
 "She drove very carefully, so that the attendants and Odysseus could keep up on foot, and she plied the lash with judgment.",
 "ἡνιόχευεν is 'she drove' (from ἡνίοχος 'charioteer', the one who holds the reins), and μάλα 'very'. ὅπως is 'so that', with the optative ἑποίατο (Attic ἕποιντο), 'might follow', and πεζοί 'on foot'. νόῳ is 'with mind, with judgment', and ἐπέβαλλεν 'laid on'. ἱμάσθλην is 'lash', from ἱμάσσω, the noun distinct from μάστιξ 'whip' at 316.")
u((321,None),
 "And the sun set, and they reached the famous grove,\nsacred to Athena, where then sat down heavenly Odysseus.",
 "The sun set, and they reached the famous grove sacred to Athena, where heavenly Odysseus sat down.",
 "δύσετο is the aorist middle of δύω 'sink, set', and ἠέλιος is Ionic for ἥλιος. τοί is the pronoun 'they'. κλυτόν is 'famous', and ἱρόν the Ionic contraction of ἱερόν, 'sacred'; 'the grove sacred to Athena' is the same grove Nausicaa described at 291. ἵν’ is 'where', and ἕζετο 'sat down'.")
u((323,None),
 "Then at once he prayed to the daughter of great Zeus:",
 "Then at once he prayed to the daughter of great Zeus:",
 "ἠρᾶτο is the imperfect of ἀράομαι 'pray', with the dative Διὸς κούρῃ μεγάλοιο, 'to the daughter of great Zeus'; μεγάλοιο is a genitive in -οιο. The unnamed goddess is Athena.")
u((324,None),
 "“Hear me, child of aegis-bearing Zeus, Atrytone;",
 "“Hear me, child of aegis-bearing Zeus, Atrytone.",
 "κλῦθι is the aorist imperative of κλύω 'hear', with μευ the genitive; it is the ordinary opening of a prayer. αἰγιόχοιο is 'aegis-bearing' (the meaning of the second half is disputed, the aegis being the goddess's shield or cloak), and τέκος is 'child'. Ἀτρυτώνη is a cult-title of Athena, traditionally 'the Unwearied' (ἀ- and τρύω), though the formation is irregular and the sense not fully certain.",mark="Odysseus prays")
u((325,None),
 "now at least hear me, since before you never heard me\nas I was wrecked, when the famous earth-shaker was wrecking me.",
 "Hear me now at least, since you never heard me before when I was being wrecked, when the famous earth-shaker was wrecking me.",
 "νῦν δή πέρ is 'now at least'. ἄκουσον is the aorist imperative and ἄκουσας the aorist indicative of ἀκούω, both taking the genitive μευ. ῥαιομένου is the present passive participle of ῥαίω 'shatter, wreck', agreeing with the μευ understood, and ἔρραιε the imperfect 'was wrecking'. κλυτὸς ἐννοσίγαιος is 'the famous earth-shaker', Poseidon, whom he does not name.")
u((327,None),
 "Grant me to come to the Phaeacians as dear and as pitied.”",
 "Grant that I come among the Phaeacians as one welcome and pitied.”",
 "δός is the aorist imperative of δίδωμι 'grant', with the accusative μ’ and the infinitive ἐλθεῖν. The accusatives φίλον 'dear, welcome' and ἐλεεινόν 'to be pitied' agree with μ’: he asks to be received as a friend and to be pitied. The prayer ends here.")
u((328,None),
 "So he spoke, praying, and Pallas Athena heard him.",
 "So he prayed, and Pallas Athena heard him.",
 "The line closes the prayer. εὐχόμενος is 'praying', and τοῦ is the genitive 'him' that ἔκλυε 'heard' takes. Παλλὰς Ἀθήνη is 'Pallas Athena'; the meaning of Παλλάς is disputed.",p=True)
u((329,None),
 "but to him she did not yet appear face to face;",
 "but she did not yet show herself to him face to face;",
 "αὐτῷ is 'to him' (Odysseus), and φαίνετ’ the elided imperfect middle φαίνετο, 'appeared'. ἐναντίη is 'face to face, openly', agreeing with the goddess. οὔ πω is 'not yet'.")
u((329,'αἴδετο'),
 "for she felt reverence for\nher father’s brother;",
 "for she felt reverence for her father’s brother;",
 "αἴδετο is the imperfect of αἰδέομαι 'feel reverence or shame before', and ῥα is ἄρα. πατροκασίγνητον is 'father's brother', that is, Poseidon, the brother of Zeus; the word says what the earlier κλυτὸς ἐννοσίγαιος left unnamed.")
u((330,'ὁ δ’ ἐπιζαφελῶς'),
 "but he furiously raged\nat godlike Odysseus, before he his own land reached.",
 "but he raged furiously against godlike Odysseus, until the man reached his own land.",
 "ὁ is the pronoun 'he', Poseidon. ἐπιζαφελῶς is 'vehemently, furiously', and μενέαινεν 'raged, was angry', with the dative ἀντιθέῳ Ὀδυσῆι, 'against godlike Odysseus'. πάρος with the infinitive ἱκέσθαι is 'until he should reach', and ἣν γαῖαν 'his own land', with ὅς as the possessive. These two lines repeat, from the middle of the first, a line of the poem's opening in Book 1.")

# ---- cut
starts=[]
for s in U:
    ln,mk=s['start']; L=lines[ln]
    off=0 if mk is None else L.index(mk)
    if mk is not None: assert L.count(mk)==1,(ln,mk)
    starts.append((ln,off))
sents=[]
for k,s in enumerate(U):
    a=starts[k]
    b=starts[k+1] if k+1<len(U) else (332,0)
    parts=[]
    ln=a[0]
    while True:
        seg=lines[ln] if ln<332 else ''
        lo=a[1] if ln==a[0] else 0
        hi=b[1] if ln==b[0] else len(seg)
        if ln>b[0] or (ln==b[0] and hi==0): break
        parts.append(seg[lo:hi].strip())
        if ln==b[0]: break
        ln+=1
    t='\n'.join(x for x in parts if x)
    nl=t.count('\n')
    assert s['l'].count('\n')==nl,(a,'l lines',nl,s['l'])
    assert '\n' not in s['i'] and '\n' not in s['n']
    o=dict(t=t,l=s['l'],i=s['i'],n=s['n'],ln=a[0],v=True)
    if s['p']: o['p']=True
    if s['mark']: o['mark']=s['mark']
    # check paragraph flag agrees with Murray
    if a[1]==0: assert (a[0] in para)==bool(s['p']),(a,'para')
    sents.append(o)
out=dict(title="Ἡ ὁδὸς πρὸς τὴν πόλιν",titleEn="The Way to the City — Odyssey 6.223–331",
 part="The Way to the City (6.223–331)",
 about="Odysseus washes the sea-salt from his body in the river, and Athena makes him taller and sturdier, with thick curling hair, so that he sits on the shore glistening, and Nausicaa gazes at him. She tells her attendants that this man comes among the Phaeacians not against the will of the gods, and that she would gladly have such a husband, and has them give him food and drink. She then lays out the plan for the road to the city: he is to follow behind the wagon with the attendants until the city is near, wait in Athena's grove outside it, since she fears the gossip of the common people, and then find the house of her father Alcinous and clasp the knees of her mother. She drives the mules to the grove, where Odysseus prays to Athena to be received as a friend and pitied by the Phaeacians. Athena hears him, but she will not yet appear to him, out of respect for her uncle Poseidon, who still rages against him.",
 sentences=sents)
json.dump(out,open(D+'units.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
# validate
chk=json.load(open(D+'units.json',encoding='utf-8'))
cat=' '.join(x['t'].replace('\n',' ') for x in chk['sentences'])
src=' '.join(lines[k] for k in range(223,332))
assert re.sub(r'\s+',' ',cat)==re.sub(r'\s+',' ',src)
print(len(chk['sentences']),'units OK')
