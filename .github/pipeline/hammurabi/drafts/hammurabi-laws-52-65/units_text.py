# -*- coding: utf-8 -*-
"""The drafter's annotations for hammurabi-laws-52-65, unit by unit. Words are listed in stele order as
(say, morph-spec); make_units.py checks them against the words it cuts from Harper's lines.
morph-spec: 'lemma' (all glyphs) or 'lemma:k|lemma2:k2|lemma3' (k glyphs each, in order; the last takes the rest)."""

TITLE_EN = 'Laws of Hammurabi — §52–65: crops, dikes and orchards (xv 1 – xvi 77)'
PART = 'Laws §52–65 · crops, dikes and orchards (Col. xv 1 – xvi 77)'
ABOUT = ('Fourteen laws on the damage one farmer can do to another’s crop, and on the date-orchard. A tenant whose '
         'field yields nothing is still held to his contract (§52). Then water: a man who lets his dike decay or '
         'leaves his ditch open and floods the fields round about must replace the grain he destroyed — and if he '
         'cannot, he and his goods are sold and the farmers of the district share the price (§53–56). Then sheep: '
         'a shepherd who grazes his flock on a man’s field without leave pays in grain, and more if he does it '
         'after the flocks have been brought in from the fields (§57–58). The last laws turn to orchards: a fine '
         'for felling another man’s tree (§59), and the contract between a landowner and the gardener who plants '
         'his field as a date-orchard or tends one already planted — the four unproductive years, the division of '
         'the fifth, the land left unplanted, the pollination of the palms and the share of the crop (§60–65). '
         'After §65 five columns of the stele were chiselled away in antiquity; the laws that stood there '
         'follow in the next parts from other copies.')

# glosses for lemmas not in an earlier part's glossary (the glosser may refine them)
NEWG = {
    'mārum': 'son; member of a group: DUMU A.GÀR{meš} mārū ugārim “the sons of the irrigated land”, the district’s farmers',
    'enûm': 'to change, alter: ul inni “he shall not alter” (present)',
    'kārum': 'dike, embankment (written KAR; Harper kâru): kāršu “his dike”, ina kārišu “in his dike”',
    'danānum-D': 'D-stem of danānum “to be strong”: to strengthen: dunnunim “to strengthen”, udannin “he strengthened”',
    'pītum': 'opening, breach (in a dike): Harper bi-tum',
    'petûm-N': 'N-stem of petûm: to be opened, to open (itself): ittepti “has opened”, ippetû “(which) was opened”',
    'ugārum': 'the irrigated farmland of a district, the commons (written A.GÀR; Harper ugaru)',
    'wabālum-Š': 'Š-stem of wabālum “to carry”: to make (something) carry off: mê uštābil “he let the water carry off”',
    'ḫalāqum-D': 'D-stem of ḫalāqum “to be lost”: to destroy, cause to be lost: uḫalliqu',
    'bīšum': 'movable property, goods: bīšašu “his goods”',
    'atappum': 'ditch, small canal: atappašu “his ditch”',
    'šiqītum': 'irrigation, watering: ana šiqītim “for irrigation” (Harper ši-ki-tim)',
    'šammū': 'plants, grass, pasture: ana šammī “(to) the plants”',
    'akālum-Š': 'Š-stem of akālum “to eat”: to feed, to let graze: šūkulim “to feed”, uštākil, ušākilu',
    'magārum': 'to agree: itti … imtagar “has come to an agreement with”',
    'eṣēdum': 'to harvest, reap: iṣṣid “he shall harvest”',
    'elēnumma': 'in addition, over and above (Harper e-li-nu-um-ma)',
    '20': 'twenty — two corner-wedges; said ešrā (?)',
    '60': 'sixty — a single vertical wedge (the sexagesimal “one” of the next order, Harper’s LX); said šūši (?)',
    'ištu': 'after, since; from',
    'elûm-up': 'to go up, come up: ītelianim “(the sheep) have come up”',
    'kannum': 'band, tie (?): kannū gamartim, a signal hung at the city gate at the end of the grazing season (sense from context)',
    'gamartum': 'completion, end: kannū gamartim “the bands of completion” (?)',
    'ḫalālum-N': 'N-stem of a verb ḫalālum, “to be hung up” (?): ittaḫlalū — the meaning is inferred from the context',
    'naṣārum': 'to guard, keep watch: inaṣṣar “he shall guard”',
    'iṣum': 'tree, wood: iṣam “a tree”',
    'nakāsum': 'to cut, cut down: ikkis “he cut down”',
    '1/2': 'one half — a horizontal crossed by a vertical (Harper’s ½); said mišil (?) “half (of)”',
    'manûm-syll': 'mina — weight of silver, 60 shekels (about 500 g), here spelled ma-na: 1/2 mana kaspim “half a mina of silver”',
    'šaqālum-pres': 'to weigh out (silver = to pay): išaqqal “he shall pay” (Harper i-ša-ḳal)',
    'nukaribbum': 'gardener, orchard-keeper — written NU.{giš}KIRI₆ “man of the orchard”; Harper leaves it as NU.kirû, later study reads nukaribbum',
    'zaqāpum': 'to plant (trees), set upright: zaqāpim “to plant” (Harper za-ga-bi-im), izqup “he planted”',
    '4-kam': 'four — MU 4{kam}, here a count of years, “four years”, said erbe šanātim (spoken form reconstructed)',
    'ḫamuštum': 'fifth (ordinal): ina ḫamuštim šattim “in the fifth year”',
    'mitḫāriš': 'equally, in equal parts',
    'zittum': 'share, portion (written ḪA.LA; Harper zittu): zittašu “his share”',
    'nasāqum': 'to choose, select: inassaq “he shall choose” (Harper i-na-za-ak)',
    'gamārum-G': 'to finish, complete: lā igmur “he did not finish”',
    'nidītum': 'land left lying, an unplanted patch (from nadûm “to leave”)',
    'ezēbum-G': 'to leave, leave behind: īzib “he left”',
    'libbum-in': 'heart, inside: ana libbi “into (the middle of)”',
    'šakānum-G': 'to set, place: išakkanūšum “they shall place for him”',
    'nadānum-N2': 'N-stem of nadānum: to be given: innadnušum “(which) was given to him”',
    'absinnum': 'furrow, ploughed (seed-)land (written AB.SÍN; Harper abšênu)',
    'šanātum': 'years (plural of šattum): ša šanātim “of the years”',
    'nadûm-N': 'N-stem of nadûm: to be left lying (of land): innadû “(in which) it lay neglected”',
    'epēšum-G': 'to do, make; to work (land): eqlam šipram ippeš “he shall do the work on the field”',
    'ištiat': 'one (feminine of ištēn): ša šattim ištiat “of one year”',
    'rakābum-D': 'D-stem of rakābum “to ride, mount”: to pollinate (date palms): rukkubim “to pollinate”, urakkib',
    'adi-while': 'until, as long as: adi kirâm ṣabtu “as long as he holds the orchard”',
    'ṣabātum-hold': 'to seize, hold: ṣabtu “(as long as) he holds”',
    'šittān': 'two-thirds: šittīn',
    'maṭûm-D': 'D-stem of maṭûm “to be little”: to reduce, diminish: umtaṭṭi “he has reduced” (Harper um-ta-di)',
    'biltum-yield': 'yield (of an orchard), produce: biltam, bilat kirîm “the yield of the orchard”',
}

UNITS = [
 # ---------------------------------------------------------------- §52
 {'from': ('XV', 1), 'to': ('XV', 6), 'ln': 52,
  'l': 'If the-tenant in the-field grain or sesame not has-caused-to-be, his-contracts he-shall-not-change.',
  'i': 'If the tenant did not raise grain or sesame in the field, he may not change his contract.',
  'n': 'The last of the tenant laws (§42–47): a bad crop does not undo the lease. riksātum, the “bindings” you met '
       'in §47, are the terms of the contract; inni is enûm “to change” in the present, and ul inni is a flat '
       'statement of law: “he shall not alter” them — he still owes what he agreed. uštabši is the Š-stem perfect '
       'of bašûm again (§42, §49). Here the grain-sign carries a phonetic complement: the stele writes ŠE-am, the '
       'sign ŠE followed by am to tell you to read šeʾam (Harper prints še-am).',
  'words': [('šumma', 'šumma'), ('irrišum', 'irrišum'),
            ('ina', 'ina'), ('eqlim', 'eqlum'), ('šeʾam', 'šeʾum'),
            ('u', 'u'), ('lū', 'lū'), ('šamaššammam', 'šamaššammū'),
            ('lā', 'lā'), ('uštabši', 'bašûm-Š'),
            ('riksātišu', 'riksātum:4|-šu'),
            ('ul', 'ul'), ('inni', 'enûm')]},
 # ---------------------------------------------------------------- §53
 {'from': ('XV', 7), 'to': ('XV', 15), 'ln': 53,
  'l': 'If a-man for his-dike to-strengthen his-arm let-drop and his-dike not he-strengthened, and in his-dike '
       'a-breach has-opened and the-irrigated-land the-water he-has-let-carry-off,',
  'i': 'If a man neglected to keep his dike strong and did not strengthen it, and a breach opened in his dike and '
       'he let the water carry away the irrigated land,',
  'n': 'The water laws begin. kārum (Harper kâru) is the dike or embankment that holds the water back, written '
       'with the single sign KAR, the TE sign with extra wedges (Harper’s List of Signs no. 147: kar, kâru). '
       'ana kārišu dunnunim is ana with an infinitive, “for the strengthening of his dike”: dunnunum is the D-stem '
       'of danānum “to be strong”, and udannin, in the next clause, its preterite. aḫšu iddi, “he let his arm '
       'drop,” is the idiom for negligence you met at §44. pītum is a breach (Harper bi-tum: the BI sign also '
       'stands for pí), and ittepti the N-stem perfect of petûm, “has opened.” ugārum, written A.GÀR, is the '
       'irrigated land of a district, shared by many farmers; mê uštābil is wabālum “to carry” in the Š-stem '
       'perfect, “he has made the water carry off,” with two objects, the land and the water. The stone is '
       'damaged in XV 8–14: Harper draws the lost signs in outline and brackets them — KAR in line 8, -un-nu- in '
       'line 9, id-di-ma in line 10, the -šu of KAR-šu in lines 11 and 13, -ni-in-ma in line 12, -ip-ti in line 14 '
       '— restored from the phrases repeated around them.',
  'words': [('šumma', 'šumma'), ('awīlum', 'awīlum'),
            ('ana', 'ana'), ('kārišu', 'kārum:1|-šu'),
            ('dunnunim', 'danānum-D'),
            ('aḫšu', 'aḫum:2|-šu'), ('iddīma', 'nadûm:2|-ma'),
            ('kāršu', 'kārum:1|-šu'),
            ('lā', 'lā'), ('udanninma', 'danānum-D:4|-ma'),
            ('ina', 'ina'), ('kārišu', 'kārum:1|-šu'),
            ('pītum', 'pītum'), ('ittepti', 'petûm-N'),
            ('u', 'u'), ('ugāram', 'ugārum'), ('mê', 'mû'), ('uštābil', 'wabālum-Š')]},
 {'from': ('XV', 16), 'to': ('XV', 20),
  'l': 'the-man who in his-dike the-breach was-opened, the-grain which he-caused-to-be-lost shall-replace.',
  'i': 'the man in whose dike the breach opened shall replace the grain he caused to be lost.',
  'n': 'The penalty repeats the case in short as a relative clause: awīlum ša ina kārišu pītum ippetû, “the man '
       'in whose dike the breach was opened” — ippetû (Harper ib-bi-tu-u) is the N-stem preterite of petûm with '
       'the subjunctive -u that every verb in a ša-clause takes. uḫalliqu is ḫalāqum “to be lost” in the D-stem, '
       '“he made (it) be lost,” again subjunctive. iriab is riābum “to replace,” as in §8 and §23. The plate shows the '
       'sign ḪAL in u-ḫal-li-ḳu (Harper’s List of Signs no. 2).',
  'words': [('awīlum', 'awīlum'),
            ('ša', 'ša'), ('ina', 'ina'), ('kārišu', 'kārum:1|-šu'),
            ('pītum', 'pītum'), ('ippetû', 'petûm-N'),
            ('šeʾam', 'šeʾum'), ('ša', 'ša'), ('uḫalliqu', 'ḫalāqum-D'),
            ('iriab', 'riābum')]},
 # ---------------------------------------------------------------- §54
 {'from': ('XV', 21), 'to': ('XV', 26), 'ln': 54,
  'l': 'If grain to-replace not he-is-able, him and his-goods for silver they-shall-give, and',
  'i': 'If he is unable to replace the grain, he and his goods shall be sold for silver, and',
  'n': 'If he cannot pay, the loss falls on his person: he is sold. šuāti is the independent pronoun “him” (the '
       'accusative of šū); bīšum is movable property, “goods.” ana kaspim nadānum, “to give for silver,” is to '
       'sell; the plural inaddinū is the impersonal “they” of the authorities. riābam is the infinitive of riābum, '
       'and lā ileʾʾi “he is not able” is leʾûm, as in §28.',
  'words': [('šumma', 'šumma'), ('šeʾam', 'šeʾum'), ('riābam', 'riābum'),
            ('lā', 'lā'), ('ileʾʾi', 'leʾûm'),
            ('šuāti', 'šuāti'),
            ('u', 'u'), ('bīšašu', 'bīšum:2|-šu'),
            ('ana', 'ana'), ('kaspim', 'kaspum'),
            ('inaddinūma', 'nadānum:5|-ma')]},
 {'from': ('XV', 27), 'to': ('XV', 30),
  'l': 'the-sons of-the-irrigated-land whose grain the-water carried-off shall-divide (it).',
  'i': 'the farmers of the irrigated land whose grain the water carried away shall share the proceeds.',
  'n': 'DUMU A.GÀR{meš}, “the sons of the irrigated land,” are the farmers of the district who share its water: '
       'DUMU “son” (mārum) in its sense “member of a group,” A.GÀR = ugārum, and MEŠ, the plural marker, cut after '
       'the whole phrase — the sign ME with three corner-wedges (Harper’s List of Signs no. 185). Harper prints the '
       'group as one word, mâr+ugarê. mû “water” is plural in Akkadian, so the verb is too: mû ublū, “the water '
       'carried off.” ša šeʾšunu, “whose grain” — ša with a suffix on the noun that follows. The price of the man '
       'and his goods goes to the neighbours he flooded.',
  'words': [('mārū ugārim', 'mārum:1|ugārum'),
            ('ša', 'ša'), ('šeʾšunu', 'šeʾum:1|-šunu'),
            ('mû', 'mû'), ('ublū', 'wabālum'),
            ('izuzzū', 'zâzum')]},
 # ---------------------------------------------------------------- §55
 {'from': ('XV', 31), 'to': ('XV', 36), 'ln': 55,
  'l': 'If a-man his-ditch for irrigation opened, his-arm let-drop and the-field of-his-neighbour the-water '
       'he-has-let-carry-off,',
  'i': 'If a man opened his ditch to irrigate, was careless, and let the water carry away his neighbour’s field,',
  'n': 'Not a burst dike this time but carelessness at the sluice. atappum is a ditch or small canal; ana šiqītim '
       '“for irrigation” (Harper ši-ki-tim, the KI sign for qí); ipte is the preterite of petûm “to open.” '
       'eqel itêšu, “the field of his neighbour”: eqlum stands in the construct, eqel, before the genitive. '
       'mê uštābil as in §53.',
  'words': [('šumma', 'šumma'), ('awīlum', 'awīlum'),
            ('atappašu', 'atappum:3|-šu'),
            ('ana', 'ana'), ('šiqītim', 'šiqītum'), ('ipte', 'petûm'),
            ('aḫšu', 'aḫum:2|-šu'), ('iddīma', 'nadûm:2|-ma'),
            ('eqel', 'eqlum'), ('itêšu', 'itûm:2|-šu'),
            ('mê', 'mû'), ('uštābil', 'wabālum-Š')]},
 {'from': ('XV', 37), 'to': ('XV', 38),
  'l': 'grain like his-neighbour he-shall-measure-out.',
  'i': 'he shall measure out grain equal to his neighbour’s crop.',
  'n': 'The damage is valued by the yield of the land next door, as for the idle tenant of §42–43: kīma itêšu, '
       '“like his neighbour.”',
  'words': [('šeʾam', 'šeʾum'), ('kīma', 'kīma'), ('itêšu', 'itûm:2|-šu'),
            ('imaddad', 'madādum')]},
 # ---------------------------------------------------------------- §56
 {'from': ('XV', 39), 'to': ('XV', 42), 'ln': 56,
  'l': 'If a-man the-water opened and the-works of the-field of-his-neighbour the-water he-has-let-carry-off,',
  'i': 'If a man let the water out and let it carry away the work done on his neighbour’s field,',
  'n': 'mê iptēma, “he opened the water,” let it out onto the land. epšētum (Harper ip-še-tim) are the “works,” '
       'the tilling already done — the field of §49 that was “prepared”: here it is washed out before anything '
       'grows, so there is no crop to compare and the law sets a fixed rate.',
  'words': [('šumma', 'šumma'), ('awīlum', 'awīlum'),
            ('mê', 'mû'), ('iptēma', 'petûm:3|-ma'),
            ('epšētim', 'epšētum'), ('ša', 'ša'), ('eqel', 'eqlum'), ('itêšu', 'itûm:2|-šu'),
            ('mê', 'mû'), ('uštābil', 'wabālum-Š')]},
 {'from': ('XV', 43), 'to': ('XV', 45),
  'l': 'for-10 GAN.E, 10 GUR of-grain he-shall-measure-out.',
  'i': 'he shall measure out ten kor of grain for every ten bur of land.',
  'n': 'The rate of §44: the literal order is “10 GAN.E 10 ŠE.GUR,” and the “for” is supplied. As there, the '
       'signs and the translation follow Harper (ten kor per ten bur); later study of the field-measures reads '
       'the first wedge as “one bur,” ten times the rate.',
  'words': [('ešret', '10'), ('būrim', 'būrum'),
            ('ešret', '10'), ('kur šeʾam', 'šeʾum:1|kurrum'),
            ('imaddad', 'madādum')]},
 # ---------------------------------------------------------------- §57
 {'from': ('XV', 46), 'to': ('XV', 50), 'ln': 57,
  'l': 'If a-shepherd for the-plants the-sheep to-make-eat with the-owner of-the-field not has-agreed, and',
  'i': 'If a shepherd has not come to an agreement with the owner of a field to graze his sheep on its plants,',
  'n': 'The grazing laws. rēʾûm “shepherd” is written PA.LU, two signs read together as SIPA (Harper: rêʾu). '
       'ṣēnū “sheep (and goats), the flock” is written U₈.UDU{ḫi.a}: the ewe-sign U₈, the sheep-sign UDU, and the '
       'plural marker ḪI.A. Harper lists the first sign under the wool-sign SÍG (his no. 190), whose shape it '
       'shares; modern sign lists call it U₈ (§35 wrote the flock with UDU alone). šūkulum is akālum “to eat” '
       'in the Š-stem infinitive, “to make eat, to feed,” and takes two objects: ana šammī ṣēnī šūkulim, “to '
       'feed the plants to the sheep.” imtagar is the perfect of magārum “to agree.”',
  'words': [('šumma', 'šumma'), ('rēʾûm', 'rēʾûm'),
            ('ana', 'ana'), ('šammī', 'šammū'),
            ('ṣēnī', 'ṣēnum'), ('šūkulim', 'akālum-Š'),
            ('itti', 'itti'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('lā', 'lā'), ('imtagarma', 'magārum:4|-ma')]},
 {'from': ('XV', 51), 'to': ('XV', 53),
  'l': 'without the-owner of-the-field the-field the-sheep he-has-made-eat,',
  'i': 'but has grazed his sheep on the field without the owner’s consent,',
  'n': 'balum “without” — here “without (the consent of).” uštākil is the Š-stem perfect of akālum: “he has made '
       'the sheep eat the field,” two accusatives again, eqlam ṣēnī.',
  'words': [('balum', 'balum'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('eqlam', 'eqlum'), ('ṣēnī', 'ṣēnum'),
            ('uštākil', 'akālum-Š')]},
 {'from': ('XV', 54), 'to': ('XV', 55),
  'l': 'the-owner of-the-field his-field shall-harvest;',
  'i': 'the owner of the field shall harvest his field;',
  'n': 'iṣṣid is eṣēdum “to harvest” in the present: the owner brings in whatever the sheep have left.',
  'words': [('bēl', 'bēlum'), ('eqlim', 'eqlum'), ('eqelšu', 'eqlum:2|-šu'),
            ('iṣṣid', 'eṣēdum')]},
 {'from': ('XV', 56), 'to': ('XV', 64),
  'l': 'the-shepherd who without the-owner of-the-field the-field the-sheep made-eat, over-and-above for-10 GAN.E '
       '20 GUR of-grain to the-owner of-the-field he-shall-give.',
  'i': 'and the shepherd who grazed his sheep on the field without the owner’s consent shall give the owner of the '
       'field, over and above, twenty kor of grain for every ten bur.',
  'n': 'ušākilu is the Š-stem preterite of akālum with the subjunctive -u of the ša-clause. elēnumma (Harper '
       'e-li-nu-um-ma) is “in addition, over and above,” the -ma stressing it: the harvest stays with the owner '
       'and the shepherd pays besides. The rate doubles §56’s: twenty kor per ten bur. Twenty is two corner-wedges '
       '(Harper’s XX).',
  'words': [('rēʾûm', 'rēʾûm'), ('ša', 'ša'), ('ina', 'ina'), ('balum', 'balum'),
            ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('eqlam', 'eqlum'), ('ṣēnī', 'ṣēnum'),
            ('ušākilu', 'akālum-Š'),
            ('elēnumma', 'elēnumma'),
            ('ešret', '10'), ('būrim', 'būrum'),
            ('ešrā', '20'), ('kur šeʾam', 'šeʾum:1|kurrum'),
            ('ana', 'ana'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('inaddin', 'nadānum')]},
 # ---------------------------------------------------------------- §58
 {'from': ('XV', 65), 'to': ('XV', 70), 'ln': 58,
  'l': 'If after the-sheep from the-irrigated-land have-come-up (and) the-bands of-completion on the-city-gate '
       'have-been-hung,',
  'i': 'If, after the sheep have come up from the irrigated fields and the signal that grazing is over has been '
       'hung on the city gate,',
  'n': 'A harder case: grazing after the season has closed. ištu “after.” ṣēnū is a feminine plural, and so is its '
       'verb: ītelianim is elûm “to go up” in the perfect, feminine plural ītelâ, with the ventive -nim “hither” — '
       'the flocks have come up from the fields into town. kannū gamartim is literally “the bands of '
       'completion” (kannum “band, tie”; gamartum “end”): something hung at the city gate as a public sign that '
       'the grazing is over. The words are clear, the custom is not; ittaḫlalū looks like the N-stem perfect, '
       'plural, of a verb ḫalālum, “have been hung up,” a meaning inferred from the context. Harper prints '
       'ga ma-ar tim without hyphens; on the plate it is one word, GA-MA-AR-TIM.',
  'words': [('šumma', 'šumma'), ('ištu', 'ištu'), ('ṣēnū', 'ṣēnum'),
            ('ina', 'ina'), ('ugārim', 'ugārum'),
            ('ītelianim', 'elûm-up'),
            ('kannū', 'kannum'), ('gamartim', 'gamartum'),
            ('ina', 'ina'), ('abullim', 'abullum'),
            ('ittaḫlalū', 'ḫalālum-N')]},
 {'from': ('XV', 71), 'to': ('XV', 74),
  'l': 'the-shepherd the-sheep into a-field has-let-loose and the-field the-sheep he-has-made-eat,',
  'i': 'a shepherd turned his sheep loose into a field and grazed them on it,',
  'n': 'ṣēnī ana eqlim iddi: nadûm “to throw” — he turned the flock into the field on purpose, after the fields '
       'were closed.',
  'words': [('rēʾûm', 'rēʾûm'), ('ṣēnī', 'ṣēnum'),
            ('ana', 'ana'), ('eqlim', 'eqlum'), ('iddīma', 'nadûm:2|-ma'),
            ('eqlam', 'eqlum'), ('ṣēnī', 'ṣēnum'),
            ('uštākil', 'akālum-Š')]},
 {'from': ('XV', 75), 'to': ('XVI', 3),
  'l': 'the-shepherd the-field he-made-eat shall-guard and at the-harvest for-10 GAN.E 60 GUR of-grain to '
       'the-owner of-the-field he-shall-measure-out.',
  'i': 'the shepherd shall keep watch over the field he grazed, and at harvest he shall measure out to the owner '
       'of the field sixty kor of grain for every ten bur.',
  'n': 'eqel ušākilu, “the field (that) he grazed,” is a relative clause without ša: the noun stands in the '
       'construct and the verb takes the subjunctive. Harper prints eḳlum, a nominative, but A.ŠÀ shows no case '
       'ending and the grammar asks for the construct. inaṣṣarma, from naṣārum “to guard”: the field is in his '
       'charge until harvest. The penalty is sixty kor per ten bur, three times §57’s. Sixty is one vertical '
       'wedge, the same stroke as “one” at the next sexagesimal place (Harper’s LX). The column changes at the '
       'stele’s line XVI 1.',
  'words': [('rēʾûm', 'rēʾûm'), ('eqel', 'eqlum'), ('ušākilu', 'akālum-Š'),
            ('inaṣṣarma', 'naṣārum:4|-ma'),
            ('ina', 'ina'), ('ebūrim', 'ebūrum'),
            ('ešret', '10'), ('būrim', 'būrum'),
            ('šūši', '60'), ('kur šeʾam', 'šeʾum:1|kurrum'),
            ('ana', 'ana'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('imaddad', 'madādum')]},
 # ---------------------------------------------------------------- §59
 {'from': ('XVI', 4), 'to': ('XVI', 7), 'ln': 59,
  'l': 'If a-man without the-owner of-the-orchard in the-orchard of-a-man a-tree has-cut-down,',
  'i': 'If a man cut down a tree in another man’s orchard without the owner’s consent,',
  'n': 'The orchard laws (§59–65). kirûm is written {giš}KIRI₆, the wood-determinative GIŠ and the garden-sign SAR, '
       'as in §27–41; the orchards here are date-palm groves. kiri awīlim, “the orchard of a man,” has kirûm in '
       'the construct. iṣum “tree” (iṣam, accusative); ikkis is the preterite of nakāsum “to cut.”',
  'words': [('šumma', 'šumma'), ('awīlum', 'awīlum'),
            ('balum', 'balum'), ('bēl', 'bēlum'), ('kirîm', 'kirûm'),
            ('ina', 'ina'), ('kiri', 'kirûm'), ('awīlim', 'awīlum'),
            ('iṣam', 'iṣum'), ('ikkis', 'nakāsum')]},
 {'from': ('XVI', 8), 'to': ('XVI', 9),
  'l': '½ mina of-silver he-shall-weigh-out.',
  'i': 'he shall pay half a mina of silver.',
  'n': 'A fixed fine in silver. The half is one sign, a horizontal crossed by a vertical (Harper’s List of '
       'Numerals: ½); it is written 1/2 here and drawn with the MAŠ sign, “half” — the identification of the '
       'character is ours, Harper gives only the shape. Its Akkadian, mišil “half (of),” is a reconstruction. '
       'ma-na, the mina (sixty shekels, about 500 g): Harper writes it as a plain syllabic word here, where §24 '
       'read the same two signs as the logogram MA.NA. išaqqal is šaqālum “to weigh out,” i.e. to pay; its last '
       'sign is GAL, read qal (Harper ḳal).',
  'words': [('mišil', '1/2'), ('mana', 'manûm-syll'), ('kaspim', 'kaspum'),
            ('išaqqal', 'šaqālum-pres')]},
 # ---------------------------------------------------------------- §60
 {'from': ('XVI', 10), 'to': ('XVI', 12), 'ln': 60,
  'l': 'If a-man a-field as an-orchard to-plant to a-gardener gave,',
  'i': 'If a man gave a field to a gardener to plant as an orchard,',
  'n': 'The gardener, NU.{giš}KIRI₆, is “the man of the orchard” in Sumerian. Harper leaves the word as NU.kirû; '
       'the Akkadian behind it is nukaribbum, read so in later study. zaqāpum is “to plant (upright)” — Harper’s '
       'za-ga-bi-im, with GA for qá and BI for pí, as in e-bi-ši-im for epēšim at §42.',
  'words': [('šumma', 'šumma'), ('awīlum', 'awīlum'),
            ('eqlam', 'eqlum'), ('ana', 'ana'), ('kirîm', 'kirûm'), ('zaqāpim', 'zaqāpum'),
            ('ana', 'ana'), ('nukaribbim', 'nukaribbum'), ('iddin', 'nadānum')]},
 {'from': ('XVI', 13), 'to': ('XVI', 16),
  'l': 'the-gardener the-orchard planted, four years the-orchard he-shall-raise;',
  'i': 'and the gardener planted the orchard, he shall tend the orchard for four years;',
  'n': 'izqup, preterite of zaqāpum, still belongs to the condition; the rule starts with urabba, rabûm “to '
       'grow” in the D-stem, “he shall raise (it)” — the verb used of bringing up a child in §29. MU 4{kam} is '
       'the year-sign, four wedges, and KAM: here a stretch of time, said erbe šanātim “four years” (a '
       'reconstruction), like ana MU 3{kam} at §44. Young palms bear nothing; the gardener carries those years.',
  'words': [('nukaribbum', 'nukaribbum'),
            ('kirâm', 'kirûm'), ('izqup', 'zaqāpum'),
            ('erbe šanātim', 'šattum:1|4-kam'),
            ('kirâm', 'kirûm'), ('urabba', 'rabûm-D')]},
 {'from': ('XVI', 17), 'to': ('XVI', 22),
  'l': 'in the-fifth year the-owner of-the-orchard and the-gardener equally shall-divide;',
  'i': 'in the fifth year the owner of the orchard and the gardener shall divide it equally;',
  'n': 'ḫamuštum, “fifth,” is the ordinal of ḫamšum “five” (compare rebûtim “fourth” at §44). mitḫāriš, '
       '“equally, in equal parts.”',
  'words': [('ina', 'ina'), ('ḫamuštim', 'ḫamuštum'),
            ('šattim', 'šattum'),
            ('bēl', 'bēlum'), ('kirîm', 'kirûm'),
            ('u', 'u'), ('nukaribbum', 'nukaribbum'),
            ('mitḫāriš', 'mitḫāriš'),
            ('izuzzū', 'zâzum')]},
 {'from': ('XVI', 23), 'to': ('XVI', 26),
  'l': 'the-owner of-the-orchard his-share shall-choose and shall-take.',
  'i': 'the owner of the orchard shall choose his share and take it.',
  'n': 'zittum “share” is written ḪA.LA, the Sumerian for “share” (Harper prints the Akkadian, zitti-šu). '
       'inassaqma is nasāqum “to choose” (Harper i-na-za-ak-ma: ZA for sa, AK for aq): the owner picks which half '
       'is his.',
  'words': [('bēl', 'bēlum'), ('kirîm', 'kirûm'),
            ('zittašu', 'zittum:2|-šu'),
            ('inassaqma', 'nasāqum:4|-ma'),
            ('ileqqi', 'leqûm')]},
 # ---------------------------------------------------------------- §61
 {'from': ('XVI', 27), 'to': ('XVI', 30), 'ln': 61,
  'l': 'If the-gardener the-field in planting not finished and an-unplanted-patch left,',
  'i': 'If the gardener did not finish planting the field but left part of it unplanted,',
  'n': 'igmur is gamārum “to finish.” nidītum, from nadûm “to leave lying,” is the patch left bare; īzib, '
       'ezēbum “to leave.”',
  'words': [('šumma', 'šumma'), ('nukaribbum', 'nukaribbum'),
            ('eqlam', 'eqlum'), ('ina', 'ina'), ('zaqāpim', 'zaqāpum'),
            ('lā', 'lā'), ('igmurma', 'gamārum-G:3|-ma'),
            ('nidītam', 'nidītum'), ('īzib', 'ezēbum-G')]},
 {'from': ('XVI', 31), 'to': ('XVI', 33),
  'l': 'the-unplanted-patch into the-middle of-his-share they-shall-place-for-him.',
  'i': 'the unplanted part shall be counted in his share.',
  'n': 'ana libbi zittišu, “into the heart of his share”: the bare patch is reckoned as part of the gardener’s half '
       'of the orchard. išakkanūšum, “they shall place for him” — šakānum with the plural impersonal “they” and '
       'the dative -šum.',
  'words': [('nidītam', 'nidītum'),
            ('ana', 'ana'), ('libbi', 'libbum-in'), ('zittišu', 'zittum:2|-šu'),
            ('išakkanūšum', 'šakānum-G:4|-šu')]},
 # ---------------------------------------------------------------- §62
 {'from': ('XVI', 34), 'to': ('XVI', 36), 'ln': 62,
  'l': 'If the-field which was-given-to-him as an-orchard not he-planted,',
  'i': 'If he did not plant as an orchard the field that was given to him,',
  'n': 'innadnušum is nadānum in the N-stem, “(which) was given to him,” with the subjunctive -u before the '
       'dative suffix.',
  'words': [('šumma', 'šumma'), ('eqlam', 'eqlum'),
            ('ša', 'ša'), ('innadnušum', 'nadānum-N2:4|-šu'),
            ('ana', 'ana'), ('kirîm', 'kirûm'), ('lā', 'lā'), ('izqup', 'zaqāpum')]},
 {'from': ('XVI', 37), 'to': ('XVI', 44),
  'l': 'if (it is) furrow-land, the-yield of-the-field for the-years which it-was-left-lying the-gardener to the-owner '
       'of-the-field like its-neighbour shall-measure-out,',
  'i': 'then, if it is ploughland, the gardener shall measure out to the owner the field’s yield for the years it '
       'lay neglected, at the rate of the neighbouring field,',
  'n': 'A second šumma inside the first: the case divides by the kind of land. AB.SÍN (Harper abšênum) is '
       'absinnum, the furrow — ploughed, sown ground, against the waste land of §63; “if (it is) furrow” is a '
       'verbless clause. The second sign is damaged on the stone and Harper draws part of it in outline; it is '
       'read here as SÍN, a compound of the grain-sign ŠE and the sign NAGA — the identification is uncertain. '
       'bilat eqlim, “the yield of the field,” uses the tribute-sign GÚN as in §45. ša šanātim ša innadû, “of the '
       'years in which it lay neglected”: šanātum is the plural of šattum, and innadû nadûm in the N-stem, '
       'subjunctive.',
  'words': [('šumma', 'šumma'), ('absinnum', 'absinnum'),
            ('bilat', 'biltum'), ('eqlim', 'eqlum'),
            ('ša', 'ša'), ('šanātim', 'šanātum'),
            ('ša', 'ša'), ('innadû', 'nadûm-N'),
            ('nukaribbum', 'nukaribbum'),
            ('ana', 'ana'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('kīma', 'kīma'), ('itêšu', 'itûm:2|-šu'),
            ('imaddad', 'madādum')]},
 {'from': ('XVI', 45), 'to': ('XVI', 47),
  'l': 'and the-field the-work he-shall-do and to the-owner of-the-field he-shall-return.',
  'i': 'and he shall do the work on the field and hand it back to the owner.',
  'n': 'eqlam šipram ippeš, “he shall do the field the work,” two objects. ippeš is the present of epēšum: '
       'Harper’s i-ib-bi-eš writes the first vowel twice and uses BI for pé. In u-ta-a-ar the long vowel of utâr '
       'is spelled out with an extra a. The field goes back worked, as at §43–44.',
  'words': [('u', 'u'), ('eqlam', 'eqlum'), ('šipram', 'šiprum'),
            ('ippešma', 'epēšum-G:4|-ma'),
            ('ana', 'ana'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'), ('utâr', 'târum-D')]},
 # ---------------------------------------------------------------- §63
 {'from': ('XVI', 48), 'to': ('XVI', 52), 'ln': 63,
  'l': 'If the-field (was) waste-land, the-field the-work he-shall-do and to the-owner of-the-field he-shall-return',
  'i': 'If the field was uncleared land, he shall do the work on the field and hand it back to the owner,',
  'n': 'KI.KAL is uncultivated land (§44; Harper’s List of Signs gives KI.KAL, which he reads nidûtum). The stele '
       'has a carver’s slip in XVI 51: it repeats A.ŠÀ “field” where a-na “to” is needed; Harper prints '
       'eḳlu(=a-na), keeping the stone and giving the intended word, as at §47.',
  'words': [('šumma', 'šumma'), ('eqlam', 'eqlum'), ('nidûtam', 'nidûtum'),
            ('eqlam', 'eqlum'), ('šipram', 'šiprum'),
            ('ippešma', 'epēšum-G:4|-ma'),
            ('ana', 'ana'), ('bēl', 'bēlum'), ('eqlim', 'eqlum'),
            ('utâr', 'târum-D')]},
 {'from': ('XVI', 53), 'to': ('XVI', 57),
  'l': 'and for-10 GAN.E 10 GUR of-grain of year one he-shall-measure-out.',
  'i': 'and he shall measure out ten kor of grain for every ten bur, for one year.',
  'n': 'Rent for a single year, ša šattim ištiat, “of one year” — ištiat is the feminine of ištēn “one,” agreeing '
       'with šattum. The rate is the ten-per-ten of §44 and §56.',
  'words': [('u', 'u'), ('ešret', '10'), ('būrim', 'būrum'),
            ('ešret', '10'), ('kur šeʾam', 'šeʾum:1|kurrum'),
            ('ša', 'ša'), ('šattim', 'šattum'),
            ('ištiat', 'ištiat'),
            ('imaddad', 'madādum')]},
 # ---------------------------------------------------------------- §64
 {'from': ('XVI', 58), 'to': ('XVI', 62), 'ln': 64,
  'l': 'If a-man his-orchard to a-gardener for pollinating gave,',
  'i': 'If a man gave his orchard to a gardener to pollinate,',
  'n': 'An orchard already grown. rukkubum is the D-stem infinitive of rakābum “to ride, mount” — the word for '
       'pollinating date palms by hand, setting the male flower on the female tree.',
  'words': [('šumma', 'šumma'), ('awīlum', 'awīlum'),
            ('kirāšu', 'kirûm:2|-šu'),
            ('ana', 'ana'), ('nukaribbim', 'nukaribbum'),
            ('ana', 'ana'), ('rukkubim', 'rakābum-D'),
            ('iddin', 'nadānum')]},
 {'from': ('XVI', 63), 'to': ('XVI', 70),
  'l': 'the-gardener as-long-as the-orchard he-holds, of the-yield of-the-orchard two-thirds to the-owner '
       'of-the-orchard he-shall-give, a-third he himself shall-take.',
  'i': 'as long as he holds the orchard, the gardener shall give the owner two-thirds of its yield and take one '
       'third himself.',
  'n': 'adi kirâm ṣabtu, “as long as he holds the orchard” — ṣabātum “to seize, hold,” subjunctive after adi. '
       'Harper prints kirûm, but the logogram shows no case and the verb wants an object. šittīn is “two-thirds,” '
       'šaluštum “one third” (the widow’s third of §29). šū, “he,” is stressed: he himself.',
  'words': [('nukaribbum', 'nukaribbum'),
            ('adi', 'adi-while'), ('kirâm', 'kirûm'), ('ṣabtu', 'ṣabātum-hold'),
            ('ina', 'ina'), ('bilat', 'biltum-yield'), ('kirîm', 'kirûm'),
            ('šittīn', 'šittān'),
            ('ana', 'ana'), ('bēl', 'bēlum'), ('kirîm', 'kirûm'),
            ('inaddin', 'nadānum'),
            ('šaluštam', 'šaluštum'),
            ('šū', 'šū'), ('ileqqi', 'leqûm')]},
 # ---------------------------------------------------------------- §65
 {'from': ('XVI', 71), 'to': ('XVI', 73), 'ln': 65,
  'l': 'If the-gardener the-orchard not pollinated and the-yield has-made-less,',
  'i': 'If the gardener did not pollinate the orchard and so reduced its yield,',
  'n': 'urakkib is the D-stem preterite of rakābum, “he pollinated.” umtaṭṭi is maṭûm “to be little” in the '
       'D-stem perfect, “he has made less” (Harper um-ta-di, the DI sign for ṭi).',
  'words': [('šumma', 'šumma'), ('nukaribbum', 'nukaribbum'),
            ('kirâm', 'kirûm'), ('lā', 'lā'), ('urakkibma', 'rakābum-D:5|-ma'),
            ('biltam', 'biltum-yield'), ('umtaṭṭi', 'maṭûm-D')]},
 {'from': ('XVI', 74), 'to': ('XVI', 77),
  'l': 'the-gardener the-yield of-the-orchard according-to its-neighbour [shall-measure-out].',
  'i': 'the gardener shall measure out the orchard’s yield at the rate of the neighbouring orchard.',
  'n': 'He makes good the shortfall, judged by the orchard next door. The last line, XVI 77, is lost: its place is '
       'empty on Harper’s plate, and his transliteration restores the whole word in brackets, [i-ma-ad-da-ad], '
       'from the endings of §55 and §62. Below it the stone has been cut away — five columns, the laws Harper '
       'numbers §66–99 — and the code resumes, from other copies, in the next parts.',
  'words': [('nukaribbum', 'nukaribbum'),
            ('bilat', 'biltum-yield'), ('kirîm', 'kirûm'),
            ('ana', 'ana'), ('itêšu', 'itûm:2|-šu'),
            ('imaddad', 'madādum')]},
]
