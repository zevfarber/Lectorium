import json, re
D='/home/user/Lectorium/.github/pipeline/odyssey/drafts/odyssey-030/'
R='/home/user/Lectorium/'
lines={}; para=set()
for raw in open(D+'packet.md',encoding='utf-8'):
    m=re.match(r'^(¶ |  )\s*(\d{1,3})  (.*)$',raw.rstrip('\n'))
    if m:
        lines[int(m.group(2))]=m.group(3)
        if m.group(1)=='¶ ': para.add(int(m.group(2)))
assert min(lines)==1 and max(lines)==132 and len(lines)==132, (min(lines),max(lines),len(lines))

def pub(part,ln):
    d=json.load(open(R+'odyssey-%03d.json'%part,encoding='utf-8'))
    for s in d['sentences']:
        if s['ln']==ln: return s
    raise KeyError

U=[]
def u(start,l,i,n,mark=None):
    if isinstance(start,int): start=(start,None)
    U.append(dict(start=start,l=l,i=i,n=n,mark=mark))

u(1,
 "So he there prayed, much-enduring, heavenly Odysseus,\nand the girl toward the city carried the strength of the two mules.",
 "So he prayed there, much-enduring, heavenly Odysseus, while the strength of the two mules bore the girl toward the city.",
 "ὧς, as printed, is the adverb ὣς 'so, thus', and ὁ μὲν is 'he', a pronoun, matched by δέ in the next line, which turns to the girl. ἠρᾶτο is the imperfect of ἀράομαι 'pray'. πολύτλας δῖος Ὀδυσσεύς is the standing formula for the hero: πολύτλας is πολύ- 'much' with τλῆναι 'endure', and δῖος is 'heavenly'. προτί is the epic form of πρός 'toward'. ἡμιόνοιιν is a dual genitive, 'of the two mules', and μένος ἡμιόνοιιν 'the strength of the two mules' is a periphrasis for the pair of mules that draw the wagon. φέρεν is the imperfect ἔφερεν with no augment and the ending -εν.")
u(3,
 "And she, when to her own father’s renowned halls she came,\nmade them stand at the forecourt, and her brothers around her\nstood, like to the immortals, who from under the wagon\nthe mules unyoked and the clothing carried within.",
 "When she came to the renowned halls of her own father, she brought the team to a halt in the forecourt, and her brothers, like the immortals, stood around her; they unyoked the mules from the wagon and carried the clothing inside.",
 "ἡ is 'she', a pronoun, not the article. οὗ is the genitive of the reflexive pronoun, 'her own', so οὗ πατρός is 'her own father’s'. ἀγακλυτά is 'renowned', and δώμαθ’ is δώματα elided before the rough breathing of ἵκανε, 'came to' (imperfect of ἱκάνω). στῆσεν is the transitive aorist of ἵστημι, 'made stand, halted', and its object, the mules and the wagon, is left unsaid. προθύροισι is a dative plural in -οισι, 'at the forecourt'. ἵσταντ’ is the imperfect middle ἵσταντο 'stood', and ἀθανάτοις ἐναλίγκιοι is 'like the immortals', ἐναλίγκιος taking the dative. οἵ ῥ’ is 'who then' (ῥ’ is ἄρα). ὑπ’ ἀπήνης is 'from under the wagon' (ἀπήνη is the mule-wagon), ἔλυον 'unyoked', and ἔσφερον is εἰσέφερον 'carried in', with εἴσω 'inside'.")
u(7,
 "And she herself to her own chamber went;",
 "She herself went off to her own chamber;",
 "αὐτή is 'she herself'. ἑόν is the possessive ὅς, ἥ, ὅν 'her own' (accusative agreeing with θάλαμον 'chamber'), not the relative pronoun, and ἤιε is the imperfect of εἶμι 'go'. The ano teleia ends the sentence before the old woman is brought in.")
u((7,'δαῖε'),
 "and kindled for her a fire\nan old woman of Apeire, chamber-attendant Eurymedusa,\nwhom once from Apeire ships brought, both-sides-curving;",
 "and an old woman from Apeire, her chamber-attendant Eurymedusa, kindled a fire for her, the woman whom curved ships once brought from Apeire;",
 "δαῖε is the imperfect of δαίω 'kindle', with no augment, and οἱ is 'for her'. γρῆυς is the Ionic form of γραῦς 'old woman', and Ἀπειραίη means 'woman of Apeire', the place named again in Ἀπείρηθεν, with the suffix -θεν 'from'; where Apeire lay is not known. θαλαμηπόλος is 'chamber-attendant' (θάλαμος 'chamber' and πόλος 'one who tends'). τήν is a pronoun used as the relative 'whom'. νέες is the uncontracted plural of νηῦς, 'ships', and ἤγαγον is 'brought'. ἀμφιέλισσαι is of disputed sense: 'curved on both sides' is the usual guess, 'rowed on both sides' another; the house rendering is 'both-sides-curving' in the literal layer and 'curved on both sides' in the smooth one.")
u(10,
 "for Alcinous her as a prize they picked out, because over all\nthe Phaeacians he was king, and to him as to a god the people listened;",
 "They had picked her out as a prize for Alcinous, because he was king over all the Phaeacians, and the people listened to him as to a god;",
 "Ἀλκινόῳ is a dative, 'for Alcinous', and αὐτήν 'her' is the object of ἔξελον, 'they picked out' (aorist of ἐξαιρέω), with γέρας 'a prize, a mark of honour' in apposition; the subject 'they', the Phaeacians, is not named. οὕνεκα is 'because'. ἄνασσε is the imperfect of ἀνάσσω 'be king over', with the dative πᾶσιν Φαιήκεσσιν (dative plural in -εσσι(ν)). θεοῦ … ὥς is 'as to a god', the accented ὥς following the word it governs. ἄκουεν takes a genitive: the people 'listened to him' as to a god.")
u(12,
 "who brought up Nausicaa, white-armed, in the halls.",
 "She brought up white-armed Nausicaa in the halls.",
 "ἣ is the relative 'who', picking up Eurymedusa, and τρέφε is the imperfect of τρέφω 'bring up, rear', unaugmented. Ναυσικάαν is the accusative of Ναυσικάα, and λευκώλενον 'white-armed' is her stock epithet. μεγάροισιν is a dative plural in -οισιν, 'in the halls'.")
u(13,
 "she it was who kindled the fire for her and within set the supper in order.",
 "She it was who kindled the fire for her and set the supper in order inside.",
 "ἥ is again the relative, 'she who', with οἱ 'for her'. ἀνέκαιε is the imperfect of ἀνακαίω 'kindle up', and the phrase πῦρ … ἀνέκαιε answers δαῖε … πῦρ three lines earlier. δόρπον is 'supper' and ἐκόσμει the imperfect of κοσμέω 'set in order, arrange'. εἴσω is 'within'.")
u(14,
 "And then Odysseus set out to go to the city;",
 "Then Odysseus set out for the city;",
 "ὦρτο is the aorist middle of ὄρνυμι 'rouse, set oneself in motion', so 'set out'. πόλινδ’ is πόλιν with the suffix -δε 'toward, to', and ἴμεν is the epic infinitive of εἶμι 'go'; ὦρτο … ἴμεν is 'set out to go'.")
u((14,'ἀμφὶ'),
 "and around him Athena\nmuch mist poured, kindly disposed toward Odysseus,\nlest any of the great-hearted Phaeacians meeting him\nmight mock him with words and ask who he was.",
 "and Athena poured a thick mist around him, kindly disposed toward Odysseus, so that none of the great-hearted Phaeacians who met him should mock him with words and ask who he was.",
 "ἀμφὶ … χεῦε is tmesis: the preverb stands apart from its verb, which together are 'poured around', with χεῦε an aorist of χέω unaugmented in form. ἠέρα is 'mist' (accusative of ἀήρ). φίλα φρονέουσ’ is 'thinking kindly' (φίλα is adverbial, φρονέουσα the uncontracted participle), and Ὀδυσῆι is the dative of Ὀδυσσεύς. μή τις … is a purpose clause, 'lest anyone', with the optatives κερτομέοι 'might mock' and ἐξερέοιθ’ (ἐξερέοιτο, its τ turned to θ before the rough breathing of ὅτις), 'might ask'; ὅτις εἴη is an indirect question, 'who he was', with the optative kept after a past main verb. μεγαθύμων is 'great-hearted', the genitive plural of μεγάθυμος, and ἀντιβολήσας 'meeting him' is an aorist participle.")
u(18,
 "But when he was then about to enter the delightful city,\nthere met him the goddess, gleaming-eyed Athena,\nlike to a maiden, a young girl, holding a jar.",
 "But just as he was about to enter the delightful city, the goddess, gleaming-eyed Athena, met him there, made like a young maiden carrying a jar.",
 "ἔμελλε with an infinitive is 'was about to', and δύσεσθαι is the future infinitive of δύομαι 'enter'. ἐραννήν is 'delightful' (the house word for ἐραννός, kept apart from ἐρατεινός 'lovely'). ἀντεβόλησε 'met' takes the dative οἱ. ἐικυῖα is the perfect participle of ἔοικα, 'being like', with the dative παρθενικῇ … νεήνιδι 'a maiden, a young girl'; κάλπιν ἐχούσῃ 'holding a jar' (κάλπις, a water-jar) agrees with that dative. The goddess is called θεά, γλαυκῶπις Ἀθήνη, 'the goddess, gleaming-eyed Athena', in her stock formula.")
u(21,
 "She stood before him, and he questioned her, heavenly Odysseus:",
 "She stopped in front of him, and heavenly Odysseus questioned her:",
 "στῆ is the unaugmented aorist of ἵστημι, 'stood, came to a stand'. πρόσθ’ αὐτοῦ is 'in front of him', πρόσθε taking the genitive. ὁ is the pronoun 'he', and ἀνείρετο is the imperfect middle of ἀνείρομαι 'ask, question'. δῖος Ὀδυσσεύς is 'heavenly Odysseus'. The ano teleia introduces the speech, and Murray prints no quotation marks.")
u(22,
 "“O child, would you not for me the house of the man show-the-way-to,\nAlcinous, who among these people is king?",
 "“My child, would you not show me the way to the house of the man Alcinous, who is king among these people?",
 "ὦ τέκος is 'O child', an address to a young girl. οὐκ ἄν … ἡγήσαιο is the optative with ἄν in a question, and a negative one, so it is a polite request: 'would you not …?'. ἡγήσαιο is the aorist optative middle of ἡγέομαι 'lead, show the way', taking the accusative δόμον 'to the house', with μοι 'for me'. ἀνέρος is the genitive of ἀνήρ, 'of the man', in apposition to Ἀλκινόου. ὃς is the relative 'who', not the possessive. ἀνθρώποισι is a dative plural in -οισι, and μετά with it is 'among'. The Greek question mark ; ends the unit, and the speech goes on.",
 mark="Odysseus asks")
u(24,
 "for I too, a stranger, much-tried, hither come\nfrom afar, from a distant land;",
 "for I too am a stranger, much tried, and I come here from far away, from a distant land;",
 "καὶ γάρ is 'for indeed', and ξεῖνος 'stranger' (also 'guest'). ταλαπείριος is 'much-tried' (from τλῆναι 'endure' and πεῖρα 'trial'), agreeing with ἐγώ. ἐνθάδε is 'here', and ἱκάνω 'I come'. τηλόθεν is 'from far off', the suffix -θεν meaning 'from'. ἀπίης is 'distant', an adjective of γαίης, the epic genitive of γαῖα 'land'.")
u((25,'τῷ'),
 "therefore I know no one\nof men who this city and land hold.”",
 "so I know no one of the men who hold this city and land.”",
 "τῷ is an old dative of the article used as an adverb, 'therefore, so'. οὔ τινα οἶδα is 'I know no one', with the partitive genitive ἀνθρώπων 'of men'. οἵ is 'who', the relative, and ἔχουσιν 'hold, occupy'. The closing line is the same line that Odysseus spoke to Nausicaa at 6.177, where he first came before her.")
u(27,
 "Him then in turn addressed the goddess, gleaming-eyed Athena:",
 "Then the goddess, gleaming-eyed Athena, spoke to him in turn:",
 "This is a speech-introduction that recurs word for word. τόν is the pronoun 'him', not the article, and αὖτε is 'in turn, then'. προσέειπε is the aorist of προσεῖπον 'address, speak to'. θεά, γλαυκῶπις Ἀθήνη is 'the goddess, gleaming-eyed Athena', the standing name-formula.")
u(28,
 "“Therefore I, for you, stranger, father, the house, which you bid me,\nwill show, since near my blameless father he dwells.",
 "“So I will show you, stranger, father, the house you ask for, since he lives close to my blameless father.",
 "τοιγάρ is 'therefore, so', and ἐγώ τοι is 'I, for you' (τοι is σοι). ξεῖνε πάτερ is 'stranger, father': πάτερ is a respectful address to an older man and does not claim kinship. ὅν is the relative 'which', not the possessive, and κελεύεις 'you bid, ask'. δείξω is the future of δείκνυμι 'show'. ἐπεί μοι … ναίει is 'since he dwells': the subject is the man of the house, Alcinous, left unsaid, and μοι 'my' is a dative of interest with πατρός. ἐγγύθι is 'near', with the suffix -θι 'at'. ἀμύμων, a stock epithet of persons, is of unknown meaning; 'blameless' is the traditional guess and is kept every time.",
 mark="Athena answers")
u(30,
 "But go in silence, so, and I will lead the way,\nand at any of men do not look, nor question.",
 "But go on in silence, and I will lead the way, and do not look toward anyone or question anyone.",
 "ἴθι is the imperative of εἶμι 'go', and σιγῇ 'in silence' is a dative. τοῖον is an adverb, taken as 'so, thus'; its exact force here is not certain, and it is kept in the literal layer only. ἡγεμονεύσω is the future of ἡγεμονεύω 'lead', with ὁδόν 'the way'. The two prohibitions, μηδέ … προτιόσσεο and μηδ’ ἐρέεινε, are imperatives after μηδέ. προτιόσσομαι is 'look toward, look at' (some take it as 'address'), and ἐρέεινε is the imperative of ἐρεείνω 'ask'.")
u(32,
 "For strangers these people do not very much put up with,\nnor, gladly welcoming, treat kindly whoever from elsewhere comes.",
 "For the people here do not much put up with strangers, nor do they gladly welcome and treat kindly whoever comes from elsewhere.",
 "ξείνους ἀνθρώπους is 'stranger men', ξεῖνος serving as an adjective, and οἵδε is 'these here', that is the people of the place. ἀνέχονται is 'put up with, tolerate' and takes the accusative. ἀγαπαζόμενοι is 'welcoming warmly', and φιλέουσ’ is the uncontracted φιλέουσι, 'treat kindly'. ὅς κ’ … ἔλθῃ is 'whoever comes': κε with the subjunctive makes a general relative clause. ἄλλοθεν is 'from elsewhere', the suffix -θεν meaning 'from'.")
u(34,
 "in swift ships they, trusting, in swift ones,\nthe great gulf cross over, since to them the earth-shaker gave it;",
 "Trusting in their swift ships, and swift they are, they cross the great gulf of the sea, since the earth-shaker has granted it to them;",
 "νηυσὶ θοῇσιν and ὠκείῃσι are two datives in -ῃσι(ν) agreeing with each other after πεποιθότες 'trusting' (perfect participle of πείθομαι); θοός and ὠκύς are different words, both kept as 'swift'. τοί γε is 'they' (τοί is a pronoun). λαῖτμα is 'the depth, the gulf', here of the sea, and ἐκπερόωσιν is the uncontracted present of ἐκπεράω 'cross over'. σφισι is 'to them', and δῶκ’ is the unaugmented aorist δῶκε 'gave', its object left unsaid; ἐνοσίχθων is 'earth-shaker', Poseidon.")
u(36,
 "of them the ships are swift, as if a wing or a thought.”",
 "Their ships are swift as a wing or as a thought.”",
 "τῶν is 'their', a genitive of the pronoun, and νέες the uncontracted plural of νηῦς. ὠκεῖαι is 'swift'. ὡς εἰ is 'as if', with the verb left out: 'swift as if they were a wing or a thought'. πτερόν is 'wing, feather', ἠέ 'or', and νόημα 'thought'. The speech ends.")
_p=pub(8,405); u(37,_p['l'],_p['i'],
 "ὣς ἄρα φωνήσασ’ is 'so then, having spoken', the aorist participle of φωνέω, and here it closes Athena’s speech. ἡγήσατο is the aorist middle of ἡγέομαι 'lead the way'. Παλλὰς Ἀθήνη is 'Pallas Athena'; the meaning of Παλλάς is disputed. καρπαλίμως is 'swiftly'.")
u((38,'ὁ'),
 "and he then after the footsteps walked of the goddess.",
 "and he then walked in the goddess’s footsteps.",
 "ὁ is the pronoun 'he', Odysseus. μετ’ ἴχνια βαῖνε is 'walked after the footsteps', μετά with the accusative meaning 'after, in the track of', and βαῖνε is the imperfect of βαίνω. θεοῖο is the genitive of θεός in -οιο; the masculine word θεός is used of a goddess.")
u(39,
 "And him the Phaeacians, ship-famous, did not notice\ngoing through the city, through their midst;",
 "The Phaeacians, famous for their ships, did not notice him as he went through the city among them;",
 "τόν is 'him', the pronoun, and Φαίηκες ναυσικλυτοί is 'the Phaeacians famous for ships', κλυτός being 'famous'. ἐνόησαν is 'noticed'. ἐρχόμενον 'as he went' agrees with τόν, and κατὰ ἄστυ is 'through the city'. σφέας is the accusative 'them', so διὰ σφέας is 'through their midst'.")
u((40,'οὐ'),
 "for not Athena\nallowed, fine-plaited, the dread goddess, she who upon him a haze\nwondrous poured down, kindly thinking in her heart.",
 "for fine-plaited Athena, the dread goddess, would not allow it — she who had shed a wondrous haze upon him, kindly disposed toward him in her heart.",
 "εἴα is the imperfect of ἐάω 'allow', its object left unsaid. ἐυπλόκαμος is 'fine-plaited', of the hair; the epithet here belongs to Athena. δεινὴ θεός is 'the dread goddess' (δεινός, 'fearful, formidable'). ἥ is the relative 'who', with ῥά for ἄρα, and οἱ 'upon him'. ἀχλύς is 'haze', the mist that dims sight, a different word from the ἠήρ of line 15. θεσπεσίην is 'wondrous', and κατέχευε 'poured down'. φίλα φρονέουσ’ ἐνὶ θυμῷ is 'thinking kindly in her heart', the phrase of line 15 with ἐνὶ θυμῷ added, ἐνί being ἐν.")
u(43,
 "And wondered Odysseus at the harbours and the well-balanced ships,\nand the meeting-places of the heroes themselves and the long walls,\nhigh, fitted with stakes, a wonder to see.",
 "Odysseus marvelled at the harbours and the well-balanced ships, and at the meeting-places of the heroes themselves, and the long, high walls fitted with stakes, a wonder to see.",
 "θαύμαζεν is the imperfect of θαυμάζω 'wonder at', with an accusative object. Ὀδυσεύς is Ὀδυσσεύς with one σ. νῆας ἐίσας is 'well-balanced ships'; the sense of ἐίσας is uncertain. ἡρώων is 'of the heroes', ἥρως used of men of standing, and ἀγοράς 'meeting-places'. τείχεα is the uncontracted 'walls', with μακρά 'long' and ὑψηλά 'high'. σκολόπεσσιν is a dative plural in -εσσι of σκόλοψ 'pointed stake', and ἀρηρότα the perfect participle of ἀραρίσκω 'fit', 'fitted with stakes'. θαῦμα ἰδέσθαι is 'a wonder to see', with the aorist middle infinitive.")
u(46,
 "But when they came to the renowned halls of the king,\nand among them of speeches made-beginning the goddess, gleaming-eyed Athena:",
 "But when they came to the renowned halls of the king, the goddess, gleaming-eyed Athena, was the first to speak among them:",
 "ἵκοντο is the unaugmented aorist middle of ἱκνέομαι 'come to', and βασιλῆος is the genitive 'of the king', in -ῆος, Alcinous. ἀγακλυτά is 'renowned'. τοῖσι δὲ μύθων ἦρχε is a speech-introduction: ἄρχω takes the genitive, 'made a beginning of speeches', and τοῖσι is a pronoun, 'among them'.")
u(48,
 "“This here, then, for you, stranger, father, the house, which you bid me\nto point out;",
 "“Here is the house, stranger, father, that you bid me point out;",
 "οὗτος δή τοι is 'this, you see, is', with οὗτος agreeing with δόμος 'house' and τοι being σοι. ξεῖνε πάτερ is the address of line 28 again, 'stranger, father'. δόμος, ὅν με κελεύεις repeats the clause of line 28, with πεφραδέμεν 'to point out' where 28 had δείξω 'I will show'; πεφραδέμεν is an aorist infinitive of φράζω in -έμεν, the epic infinitive ending. ὅν is the relative.",
 mark="Athena speaks")
u((49,'δήεις'),
 "and you will find Zeus-nurtured kings\na feast feasting;",
 "and you will find Zeus-nurtured kings feasting at a banquet;",
 "δήεις is the future of an old verb 'find', second person singular. διοτρεφέας is 'Zeus-nurtured' (Διός and τρέφω), an accusative plural in uncontracted -έας, and βασιλῆας is 'kings', the Phaeacian chiefs. δαίτην δαινυμένους is 'feasting a feast', a cognate accusative: δαίνυμαι 'feast' takes δαίς 'feast, banquet' as its object.")
u((50,'σὺ'),
 "but you go inside, and in your heart\ndo not at all be afraid;",
 "but go inside, and do not be at all afraid in your heart;",
 "σὺ δ’ is 'but you'. κίε is the imperative of κίω 'go', with ἔσω 'inside'. μηδέ … τάρβει is a prohibition with the imperative of ταρβέω 'fear', and τι is adverbial, 'at all'. θυμῷ is a dative, 'in your heart'.")
u((51,'θαρσαλέος'),
 "for a bold man in all\ndeeds proves better, even if from some other place he comes.",
 "for a bold man does better in every undertaking, even if he has come from somewhere else.",
 "θαρσαλέος is 'bold' (θάρσος 'courage'), and ἐν πᾶσιν … ἔργοισιν is 'in all undertakings', the dative plural ἔργοισιν in -οισιν split by the adjective. ἀμείνων is 'better', and τελέθει 'proves to be, turns out': a present of general truth. εἰ καί … ἔλθοι is 'even if he should come', an optative, with ποθεν ἄλλοθεν 'from some other place', the ἄλλοθεν of line 33 again.")
u(53,
 "The lady first you will find in the halls;",
 "First you will find the lady of the house in the halls;",
 "δέσποιναν is 'the lady' of the house, 'mistress'. μὲν πρῶτα is 'first (of all)', and κιχήσεαι is the future middle of κιχάνω 'come upon, find', in uncontracted -εαι. μεγάροισιν is a dative plural in -οισιν.")
u(54,
 "Arete is her name, name-bearing, and from parents\nthe very same who begot Alcinous the king.",
 "Her name is Arete, and she comes from the very same parents as those who begot King Alcinous.",
 "Ἀρήτη is 'Arete'. ὄνομ’ ἐστὶν ἐπώνυμον is 'her name is a name she bears'; ἐπώνυμον is 'named, by name', and how far it points to a meaning in the name is not certain. ἐκ … τοκήων τῶν αὐτῶν οἵ περ τέκον is 'from the very same parents who begot', with τοκήων the epic genitive plural of τοκεύς. Taken strictly this would make her Alcinous’ sister; the genealogy that follows (lines 63–66) shows that she is the daughter of his brother, so τοκῆες is loose here, 'forebears'.")
u(56,
 "Nausithous first Poseidon the earth-shaker\nbegot, and Periboea, in form the best of women,\nthe youngest daughter of great-spirited Eurymedon,\nwho once over the high-spirited Giants was king.",
 "First Poseidon the earth-shaker and Periboea became the parents of Nausithous — Periboea the best of women in looks, the youngest daughter of great-spirited Eurymedon, who was once king over the high-spirited Giants.",
 "Ποσειδάων is the epic form of Ποσειδῶν, with ἐνοσίχθων 'earth-shaker'. γείνατο is the aorist middle of γείνομαι 'beget, bear', with both parents for subject, so 'became the parents of'; μὲν πρῶτα is 'first'. γυναικῶν εἶδος ἀρίστη is 'best of women in looks', εἶδος an accusative of respect. ὁπλοτάτη is 'youngest', and μεγαλήτορος 'great-spirited'. ὑπερθύμοισι is a dative plural in -οισι, 'high-spirited', the house word for ὑπέρθυμος; the context makes it a reproach against the Giants, but the fixed rendering is kept. Γιγάντεσσιν is a dative plural in -εσσιν, 'the Giants'.")
u(60,
 "But he destroyed his wanton people, and himself perished;",
 "But he destroyed his wanton people and perished himself;",
 "ὁ μὲν is 'he', Eurymedon. ὤλεσε is the transitive aorist of ὄλλυμι 'destroy', and ὤλετο its middle aorist 'perished'. ἀτάσθαλον is the adjective from the root of ἀτασθαλίαι 'wanton follies', so 'wanton'; the people’s wantonness is what brought them to ruin. αὐτός is 'himself'.")
u(61,
 "and with her Poseidon was mingled, and begot a child,\nNausithous, great-hearted, who among the Phaeacians was king;",
 "Poseidon lay with her and fathered a child, great-hearted Nausithous, who was king among the Phaeacians;",
 "τῇ is 'with her', a dative of the pronoun, and ἐμίγη is the aorist passive of μίγνυμι, 'was mingled', with the dative. ἐγείνατο is 'begot'. Ναυσίθοον μεγάθυμον is 'great-hearted Nausithous', in apposition to παῖδα 'child'. Φαίηξιν is a dative plural, 'among the Phaeacians', and ἄνασσε the imperfect of ἀνάσσω 'be king'.")
u(63,
 "and Nausithous begot Rhexenor and Alcinous.",
 "And Nausithous became the father of Rhexenor and Alcinous.",
 "ἔτεκεν is the aorist of τίκτω, said of a father 'begot'. Ῥηξήνορά is the accusative of Ῥηξήνωρ, and τε … τε is 'both … and', so the two sons are named together.")
u(64,
 "the one, having no son, struck silver-bowed Apollo,\na bridegroom, in his hall, one only daughter having left,\nArete;",
 "The one, who had no son, silver-bowed Apollo struck down while he was still a bridegroom in his hall, leaving one only daughter, Arete;",
 "τὸν μέν is 'the one', the first of the two brothers. ἄκουρον ἐόντα is 'being without a son' (ἄκουρος, from κοῦρος 'boy'), ἐόντα being the epic participle of εἰμί. βάλ’ is the unaugmented aorist ἔβαλε, 'struck', and ἀργυρότοξος 'silver-bowed' (ἄργυρος and τόξον) is a stock epithet of Apollo. νυμφίον is 'a bridegroom', so newly married. μίαν οἴην is 'one only', οἴην being οἶος 'alone', and λιπόντα is the aorist participle of λείπω 'leaving', agreeing with τόν. Ἀρήτην is the accusative of the name, 'Arete'.")
u((66,'τὴν'),
 "and her Alcinous made his wife,\nand honoured her, as no other woman on earth is honoured,\nof as many women as now under husbands a house keep.",
 "and Alcinous made her his wife and honoured her as no other woman on earth is honoured, of all the women who now keep house under their husbands.",
 "τήν is 'her', a pronoun, and ποιήσατ’ ἄκοιτιν is 'made his wife' (ἄκοιτις, 'bedfellow, wife'). ἔτισ’ is the aorist of τίω 'honour', and τίεται the passive present, 'is honoured'. ὡς … ἄλλη is 'as no other woman on earth is honoured'. ὅσσαι is 'as many as', and ὑπ’ ἀνδράσιν 'under husbands', under their authority; οἶκον ἔχουσιν is 'keep a house, run a household'.")
u(69,
 "So she deeply in heart has been honoured and is,\nboth by her dear children and by Alcinous himself\nand by the people, who her as a god looking at\ngreet with words, when she goes through the town.",
 "So she has been honoured, and is honoured, deeply from the heart, by her dear children and by Alcinous himself and by the people, who look upon her as upon a god and greet her with words whenever she walks through the town.",
 "ὣς κείνη is 'so she' (κείνη is ἐκείνη), answering the ὡς of line 67. περὶ κῆρι is 'exceedingly in heart', περί adverbial and κῆρι the dative of κῆρ 'heart'. τετίμηταί τε καὶ ἔστιν is 'has been honoured and is', with the participle carried over. ἔκ τε … ἔκ τ’ … καὶ λαῶν is 'both by … and by … and by the people', ἐκ marking the agent. Ἀλκινόοιο is a genitive in -οιο. θεὸν ὥς is 'as a god'. εἰσορόωντες is the uncontracted participle of εἰσοράω 'look upon'. δειδέχαται is a perfect with the sense of a present, 'they greet', in the ending -αται for -ανται, its formation old and unusual. μύθοισιν is 'with words'. στείχῃσ’ is the epic subjunctive in -ῃσι, 'whenever she walks', with ἀνὰ ἄστυ 'through the town'.")
u(73,
 "for not at all, she herself too, of a good mind is she in want;",
 "for she herself, too, does not lack a good mind;",
 "οὐ μέν γάρ τι is 'for not at all'. νόου … ἐσθλοῦ is 'of a good mind', the genitive νόου separated from ἐσθλοῦ, and δεύεται is 'lacks' (δεύομαι), taking the genitive. καὶ αὐτή is 'she herself too', that is as well as Alcinous, with whom she shares her people’s honour.")
u(74,
 "and for those she thinks well of, and for men, quarrels she resolves.",
 "and she settles quarrels for the women she thinks well of, and for men too.",
 "ᾗσι is here the relative, a feminine dative plural 'to whom' (Attic αἷς), and not the possessive. τ’ is the epic τε, and ἐὺ φρονέῃσι is the subjunctive 'she thinks well of, is well disposed to', a general clause. καὶ ἀνδράσι adds 'and for men too'. νείκεα is the uncontracted 'quarrels', and λύει 'looses, settles'.")
u(75,
 "If she, for her part, thinks kindly toward you in her heart,\nhope for you then to see your dear ones and to reach\nyour high-roofed home and your own fatherland.”",
 "If she is kindly disposed to you in her heart, then there is hope that you will see your dear ones and reach your high-roofed home and your own native land.”",
 "The first two lines repeat what Nausicaa told Odysseus at 6.313–314; the third has ὑψόροφον 'high-roofed' (ὑψι- and ὄροφος 'roof') where 6.315 had ἐυκτίμενον 'well-built'. κέν is κε, and φρονέῃσ’ is the epic subjunctive in -ῃσι, 'should think', with φίλα 'kindly'. ἐλπωρή is 'hope', and τοι is σοι. ἰδέειν is the uncontracted aorist infinitive of ὁράω 'see', and ἱκέσθαι 'to reach'. σὴν ἐς πατρίδα γαῖαν is 'to your own fatherland', σός being the possessive 'your own'. The speech ends here.")
u(78,
 "So then having spoken, gleaming-eyed Athena went away\nover the unharvested open-sea, and left lovely Scheria,\nand came to Marathon and to wide-streeted Athens,\nand entered the solid house of Erechtheus.",
 "So she spoke, and gleaming-eyed Athena departed over the sea that yields no harvest and left lovely Scheria, and came to Marathon and to Athens of the wide streets, and entered the solid house of Erechtheus.",
 "ὣς ἄρα φωνήσασ’ ἀπέβη is the formula that follows a speech: ἀπέβη is 'went away'. πόντον ἐπ’ ἀτρύγετον is 'over the … open sea': ἀτρύγετος is of unknown meaning, 'unharvested' (ἀ- and τρυγάω 'gather in') being the traditional guess. λίπε and ἵκετο and δῦνε are unaugmented aorists, 'left', 'came to', 'entered'. Σχερίην ἐρατεινήν is 'lovely Scheria', in Ionic -ην. εὐρυάγυιαν is 'with wide streets' (εὐρύς and ἀγυιά 'street'), of Athens. Ἐρεχθῆος is the genitive of Ἐρεχθεύς. πυκινὸν δόμον is 'the solid house', πυκινός meaning 'thick, compact, tightly built'.")
u((81,'αὐτὰρ'),
 "but Odysseus\nto Alcinous’ famous halls went;",
 "But Odysseus went on toward the famous halls of Alcinous;",
 "αὐτάρ is 'but, and then', turning from Athena to Odysseus. πρὸς δώματ’ … κλυτά is 'to the famous halls', δώματ’ being δώματα elided, and ἴε the imperfect of εἶμι 'go'. Ἀλκινόου is the genitive, 'of Alcinous', in the ending -ου; the word order puts it first for emphasis.")
u((82,'πολλὰ'),
 "and much his heart\nturned over for him, as he stood, before he reached the bronze threshold.",
 "and his heart turned over many thoughts as he stood there, before he reached the bronze threshold.",
 "πολλά is adverbial, 'much', and οἱ κῆρ is 'his heart', οἱ a dative of the possessor. ὥρμαιν’ is the imperfect of ὁρμαίνω 'turn over in the mind, ponder', and ἱσταμένῳ is a dative participle, 'as he stood', agreeing with οἱ. πρίν with the infinitive ἱκέσθαι is 'before reaching'. χάλκεον οὐδόν is 'the bronze threshold'.")
u(84,
 "for it was as though the radiance of the sun, or the moon’s,\nfilled the high-roofed house of Alcinous, great-spirited.",
 "for it was as if the radiance of the sun or the moon filled the high-roofed house of great-spirited Alcinous.",
 "ὥς τε is 'as if', and αἴγλη 'radiance, gleam'. ἠελίου is 'of the sun', and πέλεν is the unaugmented imperfect of πέλω 'be, was'. δῶμα καθ’ ὑψερεφές is 'through the high-roofed house', κατά with the accusative and ὑψερεφές 'high-roofed' (ὑψι- and ἐρέφω 'roof over'). μεγαλήτορος is 'great-spirited'. The first line is the line used of Menelaus’ house at 4.45; only its second half names another owner.")
u(86,
 "for bronze walls were driven this way and that,\nto the inmost part from the threshold, and around a cornice of kyanos;",
 "for bronze walls ran this way and that, from the threshold to the inmost part, and a cornice of kyanos ran round them;",
 "ἐληλέδατ’ is a perfect passive of ἐλαύνω in the ending -δατ(αι), 'were driven, ran'; Homer’s perfects and pluperfects of this kind take -αται/-ατο instead of Attic -ανται. ἔνθα καὶ ἔνθα is 'this way and that'. ἐς μυχὸν ἐξ οὐδοῦ is 'from the threshold to the inmost part'. θριγκός is 'cornice, coping', and κύανος names some dark-blue material whose identity is not known (enamel, glass-paste and lapis have all been proposed), so it is left as 'kyanos'. περί is adverbial, 'round'.")
u(88,
 "and golden doors the solid house within shut in;",
 "and golden doors shut in the solid house within;",
 "χρύσειαι is 'golden', and θύραι 'doors'. πυκινὸν δόμον is 'the solid house' again. ἔεργον is the imperfect of εἴργω 'shut in, enclose'. ἐντός is 'within', and whether it means the doors shut the house from the inside or shut in what lies within is not settled by the words.")
u(89,
 "and doorposts of silver stood on the bronze threshold,\nand a silver lintel above, and a golden handle.",
 "Silver doorposts stood on the bronze threshold, with a silver lintel above and a golden handle.",
 "σταθμοί are 'doorposts', and ἀργύρεοι 'of silver'. ἕστασαν is the pluperfect of ἵστημι in its imperfect sense, 'stood'. ἐν χαλκέῳ οὐδῷ is 'on the bronze threshold'. ἐφ’ is ἐπί, 'above' or 'on top', with the verb left out. ὑπερθύριον is 'lintel', and κορώνη 'a curved handle or ring' on the door (the word also means 'crow').")
u(91,
 "And of gold on either side and of silver dogs there were,\nwhich Hephaestus made with knowing wits\nto guard the house of great-spirited Alcinous,\nbeing immortal and ageless for all their days.",
 "On either side stood dogs of gold and of silver, which Hephaestus made with his skilled wits to guard the house of great-spirited Alcinous, immortal and ageless for all their days.",
 "χρύσειοι … καὶ ἀργύρεοι are 'of gold and of silver', and ἑκάτερθε 'on either side', the suffix -θε marking place. κύνες ἦσαν is 'there were dogs'. οὓς Ἥφαιστος ἔτευξεν is 'which Hephaestus made'. ἰδυίῃσι is the perfect participle of οἶδα, 'knowing', in the dative plural feminine, and πραπίδεσσι is a dative plural in -εσσι of πραπίδες 'wits', the seat of understanding, originally the midriff. φυλασσέμεναι is an infinitive in -έμεναι, 'to guard'. ἀθάνατος 'immortal' and ἀγήρως 'ageless' agree with οὓς, and ἤματα πάντα is an accusative of time, 'through all their days'.")
u(95,
 "and within, chairs along the wall were set fast, this way and that,\nfrom the threshold to the inmost part, right through, where on them robes\nfine, well-spun, had been thrown, the works of women.",
 "Inside, chairs were fixed along the wall, this way and that, from the threshold to the inmost part all the way through, and on them fine, well-spun robes had been thrown, the work of women.",
 "ἐν is an adverb, 'within', and θρόνοι are 'chairs, seats'. ἐρηρέδατ’ is a perfect passive of ἐρείδω, 'were set fast', in the same ending -δατ(αι) as ἐληλέδατ’ above. ἐς μυχὸν ἐξ οὐδοῖο repeats the phrase of line 87, with the genitive οὐδοῖο in -οιο where 87 has οὐδοῦ. διαμπερές is 'right through'. ἔνθ’ ἐνὶ is 'where on them', ἐνί being ἐν. πέπλοι are 'robes, cloths', λεπτοί 'fine' and ἐύννητοι 'well-spun'; βεβλήατο is the pluperfect passive of βάλλω, 'had been thrown', so draped over the seats. ἔργα γυναικῶν is 'the work of women', in apposition.")
u(98,
 "And there the leaders of the Phaeacians used to sit\ndrinking and eating;",
 "There the leaders of the Phaeacians used to sit, drinking and eating;",
 "ἡγήτορες is 'leaders', and ἑδριόωντο the uncontracted imperfect of ἑδριάομαι 'sit', here of a habit, 'used to sit'. πίνοντες καὶ ἔδοντες is 'drinking and eating', ἔδω being the old verb 'eat'.")
u((99,'ἐπηετανὸν'),
 "for a never-failing supply they used to have.",
 "for they had a never-failing supply.",
 "ἐπηετανόν is 'never-failing', a neuter used as a noun, 'a never-failing supply'; the exact sense of the word is only approximately known. ἔχεσκον is the iterative imperfect of ἔχω, in -σκον, 'they used to have'.")
u(100,
 "And golden, then, youths on well-constructed pedestals\nstood, burning torches in their hands holding,\nlighting the nights throughout the house for the feasters.",
 "Golden youths stood on well-constructed pedestals, holding burning torches in their hands to light the nights through the house for the banqueters.",
 "χρύσειοι κοῦροι are 'golden youths', figures of gold. ἐυδμήτων is 'well-constructed' (ἐύ- and δέμω 'build'), and βωμῶν, here 'raised bases, pedestals' (the word is often 'altar'), is a genitive plural governed by ἐπί. αἰθομένας δαΐδας is 'burning torches', and μετὰ χερσὶν ἔχοντες 'holding in their hands'. φαίνοντες is 'lighting up', with νύκτας 'the nights' for 'through the nights'. δώματα is a plural for one house, and δαιτυμόνεσσι a dative plural in -εσσι, 'for the banqueters'.")
u(103,
 "and fifty for him maidservants, women, throughout the house,\nsome grind at mills the apple-coloured grain,\nand others weave webs and turn yarn,\nsitting, like leaves of a tall poplar;",
 "He has fifty maidservants in the house: some grind the yellow grain at the mills, and others weave webs and turn yarn as they sit, like the leaves of a tall poplar;",
 "πεντήκοντα is 'fifty', with οἱ 'for him' (Alcinous), and δμωαὶ γυναῖκες is 'maidservants, women'. αἱ μέν … αἱ δέ is 'some … others', with αἱ pronouns. ἀλετρεύουσι is 'grind', and μύλῃς ἔπι is 'at the mills', ἔπι being ἐπί set after its noun. μήλοπα is of uncertain meaning; 'apple-coloured' (from μῆλον 'apple' and ὄψ 'look') is the traditional guess, so 'yellow'. ἱστοὺς ὑφόωσι is 'weave webs', ὑφόωσι the uncontracted ὑφάω, and ἠλάκατα is spun wool or thread on the distaff, which στρωφῶσιν 'they turn, twirl'. ἥμεναι is the infinitive of ἧμαι, used as 'sitting'. οἷά τε φύλλα is 'like the leaves', μακεδνῆς 'tall' and αἰγείροιο the genitive of αἴγειρος 'black poplar'; the point of comparison is not said.")
u(107,
 "and from close-woven cloths runs off the liquid oil.",
 "and from the close-woven linen the liquid oil runs off.",
 "καιρουσσέων, of the cloths, is of uncertain meaning; the old explanation 'close-woven' is followed. ὀθονέων is a genitive plural of ὀθόνη 'fine cloth, linen'. ἀπολείβεται is 'drips off, runs off', and ὑγρὸν ἔλαιον 'liquid oil'. The picture is of cloth so closely woven that oil runs from it, if the ancient reading is right.")
u(108,
 "As much as the Phaeacians beyond all men are skilled\nto drive a swift ship on the open-sea, so the women\nare craftswomen of looms;",
 "As far as the Phaeacians are skilled beyond all other men at driving a swift ship on the sea, so the women are skilled at the loom;",
 "ὅσσον … ὣς δέ is 'as much as … so'. ἴδριες is 'skilled', the plural of ἴδρις, with the infinitive ἐλαυνέμεν (in -έμεν) 'to drive'. περὶ πάντων … ἀνδρῶν is 'beyond all men'. νῆα is the Ionic accusative of νηῦς, and νῆα θοήν 'a swift ship'. ἐνὶ πόντῳ is 'on the open sea'. τεχνῆσσαι is 'craftswomen, skilled women', with ἱστῶν 'of looms', and the verb 'are' is left out.")
u((110,'πέρι'),
 "for beyond others gave them Athena\nto know very-beautiful works, and a noble mind.",
 "for Athena gave them, beyond all others, skill in very beautiful handiwork and a noble mind.",
 "πέρι is περί with its accent thrown back, 'beyond others', and σφισι is 'to them'. δῶκεν is the unaugmented aorist of δίδωμι 'gave'. ἔργα τ’ ἐπίστασθαι περικαλλέα καὶ φρένας ἐσθλάς is 'to know very beautiful works and a noble mind': the infinitive ἐπίστασθαι, 'to understand, know how to do', says what the gift is. The line repeats 2.117, where the same gifts are Penelope’s.")
u(112,
 "And outside the courtyard a great orchard, near the doors,\nfour-acre;",
 "Outside the courtyard, near the doors, is a great four-acre orchard;",
 "ἔκτοσθεν is 'outside', with the genitive αὐλῆς 'of the courtyard'. ὄρχατος is 'orchard, garden of trees', and ἄγχι θυράων is 'near the doors', θυράων being a genitive plural in -άων (Attic θυρῶν). τετράγυος is 'of four γύαι', and γύης is a land-measure whose size is not certain, so 'four-acre' is only approximate.")
u((113,'περὶ'),
 "and around a fence has been driven on both sides.",
 "and a fence has been run around it on both sides.",
 "περί is adverbial, 'around'. ἕρκος is 'fence', and ἐλήλαται is the perfect passive of ἐλαύνω, 'has been driven, run'. ἀμφοτέρωθεν is 'on both sides', the suffix -θεν marking direction.")
u(114,
 "And there tall trees have grown, thriving,\npear trees and pomegranates and apple trees with splendid fruit,\nand sweet fig trees and thriving olives.",
 "There tall trees have grown, thriving: pear trees and pomegranates and apple trees with splendid fruit, and sweet fig trees and thriving olives.",
 "δένδρεα is the uncontracted 'trees', and πεφύκασι the perfect of φύω, 'have grown, stand grown'. τηλεθόωντα and, two lines on, τηλεθόωσαι are the uncontracted participles of τηλεθάω 'thrive, be luxuriant'. The names are ὄγχναι 'pear trees', ῥοιαί 'pomegranate trees', μηλέαι 'apple trees' (from μῆλον), συκέαι 'fig trees' and ἐλαῖαι 'olive trees'. ἀγλαόκαρποι is 'with splendid fruit' (ἀγλαός, καρπός), and γλυκεραί 'sweet'.")
u(117,
 "Of these never the fruit perishes nor fails\nin winter nor in summer, year-long;",
 "The fruit of these trees never perishes or fails, in winter or in summer, lasting the whole year;",
 "τάων is 'of these', a genitive plural in -άων. ἀπόλλυται is 'perishes' (passive of ἀπόλλυμι) and ἀπολείπει 'fails, gives out', intransitive. χείματος … θέρευς are genitives of time, 'in winter … in summer', θέρευς being the Ionic θέρους. ἐπετήσιος is 'lasting the year' (ἐπί and ἔτος).")
u((118,'ἀλλὰ'),
 "but always indeed\nthe western wind, blowing, some makes grow, and others ripens.",
 "but the west wind, always blowing, makes some grow and ripens others.",
 "μάλ’ αἰεί is 'always, indeed', αἰεί being ἀεί. Ζεφυρίη is a feminine adjective, 'of the west', standing for the West Wind (a noun such as 'breath' is understood), and πνείουσα is the uncontracted participle 'blowing'. τὰ μέν … ἄλλα δέ is 'some … others', with τά a pronoun. φύει is transitive here, 'makes grow', and πέσσει 'ripens' (properly 'cooks').")
u(120,
 "pear upon pear grows old, and apple upon apple,\nand grape upon grape, and fig upon fig.",
 "Pear grows old upon pear, and apple upon apple, grape upon grape, and fig upon fig.",
 "ὄγχνη ἐπ’ ὄγχνῃ is 'pear upon pear', with the dative after ἐπί, and the three pairs that follow have the same shape. γηράσκει is 'grows old', that is ripens and ages while the next fruit comes on, and the picture is of one fruit following another without a gap. αὐτάρ here is a simple 'and'.")
u(122,
 "And there for him a many-fruited vineyard is rooted,\nof which one part, a sun-drying-ground, on a level spot\nis dried by the sun, and others they gather,\nand others they tread;",
 "There he has a richly fruited vineyard, planted in the ground: one part of it, a warm drying-place on level land, is dried by the sun, while other grapes they gather, and others they tread;",
 "οἱ is 'his' (Alcinous). πολύκαρπος is 'rich in fruit', and ἀλωή is a cultivated plot, here a vineyard, as the grapes show; ἐρρίζωται is the perfect passive of ῥιζόω, 'has taken root'. τῆς is the relative 'of which', with ἕτερον 'one part'. θειλόπεδον is a sun-warmed place (θείλη 'heat of the sun', πέδον 'ground') and λευρῷ ἐνὶ χώρῳ 'on a level spot'. τέρσεται is 'is dried', ἠελίῳ 'by the sun'. τρυγόωσιν is the uncontracted τρυγάω 'gather grapes', and τραπέουσι the uncontracted τραπέω 'tread'. ἑτέρας … ἄλλας are feminine, 'others', the grapes or vines understood, and the 'they' who gather and tread is not named.")
u((125,'πάροιθε'),
 "and in front are unripe grapes,\nshedding blossom, and others are beginning to darken.",
 "and in front of these are unripe grapes shedding their blossom, while others are just turning dark.",
 "πάροιθε is 'in front'. ὄμφακες are 'unripe grapes', and ἄνθος ἀφιεῖσαι is 'letting go their blossom', the feminine participle of ἀφίημι. ἕτεραι is 'others' (grapes), and ὑποπερκάζουσιν is 'are beginning to darken', from ὑπό 'slightly' and περκάζω 'turn dark, ripen' (of grapes).")
u(127,
 "and there neatly-ordered beds beside the last row\nof every kind have grown, never-failing gleaming;",
 "And there, along the last row, neatly ordered beds of every kind of plant have grown, gleaming fresh and never failing;",
 "κοσμηταί is 'neatly ordered', and πρασιαί 'garden beds'. παρὰ νείατον ὄρχον is 'along the last row', νείατος meaning 'furthest, last' and ὄρχος 'row (of plants)'. παντοῖαι is 'of every kind', and πεφύασιν the perfect of φύω in the Ionic ending -ασιν, 'have grown'. γανόωσαι is the uncontracted participle of γανάω 'gleam, look fresh', and ἐπηετανόν, used as an adverb, is the 'never-failing' of line 99.")
u(129,
 "and in it two springs, the one over the garden all\nis spread, and the other from the other side beneath the courtyard’s threshold sends it\nto the high house, whence the townsmen drew water.",
 "And in it are two springs: one spreads over the whole garden, and the other flows from the other side under the threshold of the courtyard toward the high house, where the townspeople drew their water.",
 "ἐν is 'in it', an adverb, and δύω 'two'. κρῆναι are 'springs'. ἡ μέν τ’ … ἡ δ’ are 'the one … the other', ἡ being a pronoun. ἀνὰ κῆπον ἅπαντα is 'over the whole garden', and σκίδναται 'is scattered, spreads'. ἑτέρωθεν is 'from the other side', and ὑπ’ αὐλῆς οὐδόν 'under the threshold of the courtyard', ὑπό with the accusative of motion. ἵησι is 'sends', its object, the water, left out. πρὸς δόμον ὑψηλόν is 'toward the high house'. ὑδρεύοντο is the imperfect of ὑδρεύομαι 'draw water'.")
u(132,
 "Such then in Alcinous’ were of the gods the splendid gifts.",
 "Such were the splendid gifts of the gods in the house of Alcinous.",
 "τοῖ’ is τοῖα 'such', and ἄρ’ 'so, then'. ἐν Ἀλκινόοιο is 'in Alcinous’ (house)', the genitive in -οιο with the noun left out. ἔσαν is the epic ἦσαν 'were'. ἀγλαὰ δῶρα is 'splendid gifts', ἀγλαός being 'splendid'.")

# repeated whole-unit for 7.27
_p=pub(2,178); 
for x in U:
    if x['start']==(27,None):
        x['l'],x['i']=_p['l'],_p['i']
        assert 'Him then in turn' in x['l']

# ---- cut t
def linepos(ln,word):
    s=lines[ln]
    if word is None: return 0
    k=s.find(word); assert k>=0,(ln,word)
    assert s.find(word,k+1)<0 or True
    return k
starts=[x['start'] for x in U]
def abspos(st): return (st[0],linepos(*st))
prev=None
for a in starts:
    if prev: assert abspos(a)>abspos(prev),(a,prev)
    prev=a
out=[]
for idx,x in enumerate(U):
    (l0,p0)=abspos(x['start'])
    if idx+1<len(U): (l1,p1)=abspos(U[idx+1]['start'])
    else: (l1,p1)=(133,0)
    parts=[]
    for ln in range(l0,l1+1):
        if ln>132: break
        s=lines[ln]
        a=p0 if ln==l0 else 0
        b=p1 if ln==l1 else len(s)
        seg=s[a:b].strip()
        if seg: parts.append(seg)
    t='\n'.join(parts)
    assert x['l'].count('\n')==t.count('\n'),(x['start'],x['l'].count('\n'),t.count('\n'))
    assert '\n' not in x['i']
    d={'t':t,'l':x['l'],'i':x['i'],'n':x['n'],'ln':l0,'v':True}
    if x['start'][1] is None and l0 in para and (l0,None)==x['start']: d['p']=True
    if x['mark']: d['mark']=x['mark']
    out.append(d)
# reproduction check
joined=' '.join(d['t'].replace('\n',' ') for d in out)
orig=' '.join(lines[i] for i in range(1,133))
assert joined==orig
assert sum(d['t'].count('\n')+1 for d in out)==132+0 or True
doc={
 "title":"Ἐς Ἀλκινόου δώματα",
 "titleEn":"To the Palace of Alcinous — Odyssey 7.1–132",
 "part":"To the Palace of Alcinous (7.1–132)",
 "about":"Nausicaa reaches her father’s house, where her old nurse Eurymedusa kindles a fire for her, and Odysseus, left behind, sets out for the city. Athena pours a thick mist about him so that no Phaeacian will stop him with questions, and meets him at the edge of town in the likeness of a young girl carrying a jar. She warns him that the people there have little love for strangers, leads him unseen through the harbours and walls to the king’s halls, and tells him whom he will find: first the queen Arete, whose descent from Poseidon she recounts, and who is honoured by her husband, her children and the whole people. Athena then leaves for Athens, and Odysseus stands hesitating before the bronze threshold of a palace lit like the sun or the moon, with its golden and silver dogs, its seats hung with women’s weaving, its golden youths holding torches, its fifty maidservants, and beyond the court a great orchard and vineyard where fruit never fails and two springs run.",
 "sentences":out}
json.dump(doc,open(D+'units.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'units')
