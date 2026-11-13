#!/usr/bin/env python3
"""Builds azatiwada-phoenician.json — the Phoenician version of the Karatepe inscription,
copy A (the lower gate), complete: columns I–IV. Lines A I 1–16 were the pilot (2026-11-12); the rest
is in units_rest.py. Run from the repository root:  python3 .github/pipeline/azatiwada-phoenician/build.py

Letters: authored in Hebrew square letters (no final forms), exactly as the source witness
prints them, then converted letter for letter to the Phoenician block (U+10900–10915).
Checks: every word has a glossary entry and every entry is used; the concatenated letters equal the
witness's copy A, every line, apart from the readings listed in EMEND (bracketed restorations and
half-bracketed damaged letters are read as printed, the brackets dropped).
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from units_rest import REST, GLOSS, UPDATE

HERE = os.path.dirname(os.path.abspath(__file__))
HEB = 'אבגדהוזחטיכלמנסעפצקרשת'
PHX = ''.join(chr(0x10900 + i) for i in range(22))
FINALS = 'ךםןףץ'
assert not any(f in HEB for f in FINALS)
def phx(s): return ''.join(PHX[HEB.index(c)] if c in HEB else c for c in s)

# The witness's lines A I 1–16 (DEAPS, OSU, "Phoe. Class 2026" edition of KAI 26 A), with
# the hyphens/dashes it uses to show where a stone line break falls inside a word removed.
WITNESS = json.load(open(os.path.join(HERE, 'source', 'deaps-kai26.json'), encoding='utf-8'))

# Readings where the pilot departs from the witness: (line, witness word, printed word, why)
EMEND = [(('i', 16), 'אזתונ', 'אזתוד', "the witness prints ʾztwn, a slip: the name is ʾztwd everywhere else"),
         (('i', 1), 'עבר', 'עבד',
          "the witness prints ʿbr; ʿbd 'servant' is the reading the Luwian parallel requires "
          "('servant of Tarhunzas'), and r and d are near-identical letters on this stone")]

U = []   # units: ln, heb, tr, l, i, n, par (Luwian clause numbers)
def unit(ln, heb, tr, l, i=None, n=None, par=None, p=False):
    U.append(dict(ln=ln, heb=heb, tr=tr, l=l, i=i, n=n, par=par, p=p))

unit('I 1', 'אנכ אזתוד הברכ בעל עבד בעל',
     'ʾanōkī ʾAzitiwadda habbarūk Baʿl, ʿebed Baʿl',
     'I (am) Azatiwada, the-blessed of-Baal, servant of-Baal,',
     'I am Azatiwada, blessed of Baal, servant of Baal,',
     "No verb 'am': Phoenician, like Hebrew, sets a name beside 'I' and lets the sentence stand. "
     "אנכ is Hebrew אנכי, written without its final vowel letter — Phoenician spells only consonants, "
     "even at the end of a word. Baal here is the god the Luwian calls Tarhunzas, the storm god. "
     "The source we follow prints ʿbr in the last word; we read ʿbd, 'servant', which the Luwian "
     "('servant of Tarhunzas') requires — on this stone r and d are almost the same letter.",
     par=[1], p=True)
unit('I 2', 'אש אדר אורכ מלכ דננימ',
     'ʾiš ʾiddir ʾAwarik milk Dānunīm',
     'whom made-mighty Awariku, king of-the-Danunians.',
     'whom Awariku, king of the Danunians, raised to power.',
     "אש is the relative 'who, whom, which' — Hebrew אשר without its last letter. The verb comes "
     "before its subject, the usual order. מלכ 'king' was pronounced milk, judging from how Greek and "
     "Latin writers spelled Phoenician names. The Danunians are the people of Adana, the kingdom the "
     "Luwian calls Hiyawa.",
     par=[2])
unit('I 3', 'פעלנ בעל לדננימ לאב ולאמ',
     'paʿalanī Baʿl la-Dānunīm la-ʾab wa-la-ʾimm',
     'Made-me Baal for-the-Danunians into-a-father and-into-a-mother.',
     'Baal made me a father and a mother to the Danunians.',
     "פעל 'do, make' is Phoenician's everyday verb where Hebrew uses עשה; the נ on the end is 'me'. "
     "ל… ל: 'make someone into something'. The Luwian says 'mother and father', in the other order.",
     par=[3], p=True)
unit('I 3', 'יחו אנכ אית דננימ',
     'yaḥwō ʾanōkī ʾiyyat Dānunīm',
     'Gave-life I the-Danunians.',
     'I gave the Danunians life.',
     "You'll see this constantly: a bare verb form (the infinitive) followed by אנכ 'I' is this "
     "text's way of saying 'I did it' — the whole boast is told in this pattern. אית marks the object, "
     "like Hebrew את.",
     par=[4])
unit('I 4', 'ירחב אנכ ארצ עמק אדנ לממצא שמש ועד מבאי',
     'yarḥeb ʾanōkī ʾarṣ ʿimq ʾAdana la-mimṣaʾ šamš wa-ʿad mabōʾiyu',
     'Widened I the-land of-the-Plain of-Adana from-the-going-out of-the-sun and-as-far-as its-coming-in.',
     'I widened the land of the plain of Adana from sunrise to sunset.',
     "The sun 'goes out' in the east and 'comes in' in the west, as in Hebrew ממזרח שמש עד מבואו. "
     "The י on מבאי means 'its' here, not 'my' — see line 11. The Plain of Adana is the Cilician plain "
     "around the modern city of Adana.",
     par=[5])
unit('I 5', 'וכנ בימתי כל נעמ לדננימ ושבע ומנעמ',
     'wa-kūn ba-yamūtiya kull nuʿm la-Dānunīm wa-šabʿ wa-manʿam',
     'And-there-was in-my-days every good for-the-Danunians, and-plenty and-delight.',
     'In my days the Danunians had every good thing, plenty and comfort.',
     "כנ, from the root kwn, is Phoenician's 'be', where Hebrew uses היה. ימת 'days' has the plural "
     "ending -ōt, as in poetic Hebrew ימות.",
     par=[6], p=True)
unit('I 6', 'ומלא אנכ עקרת פער',
     'wa-millōʾ ʾanōkī ʿaqarōt Paʿar',
     'And-filled I the-storehouses of-Paʿar.',
     'I filled the granaries of Paʿar.',
     "עקרת is a rare word; the Luwian has 'granaries' at this point, which fixes the sense. פער is a "
     "place, the Luwian Pahar.",
     par=[7])
unit('I 6', 'ופעל אנכ סס על סס ומגנ על מגנ ומחנת על מחנת בעבר בעל ואלמ',
     'wa-paʿōl ʾanōkī sūs ʿal sūs wa-magen ʿal magen wa-maḥanet ʿal maḥanet ba-ʿabūr Baʿl wa-ʾilīm',
     'And-made I horse upon horse and-shield upon shield and-camp upon camp, for-the-sake-of Baal and-the-gods.',
     'I piled up horse on horse, shield on shield, army on army, by the grace of Baal and the gods.',
     "The Phoenician runs horse, shield, army; the Luwian horse, army, shield. מחנת is Hebrew מחנה, a "
     "camp and the army in it. בעבר is Hebrew בעבור 'for the sake of'. 'By the grace of Baal and the "
     "gods' has no counterpart in the Luwian here; in the Phoenician it returns as a refrain.",
     par=[8, 9, 10])
unit('I 8', 'ושברת מלצמ',
     'wa-šibbartī malīṣīm',
     'And-I-broke the-scoffers,',
     'I broke the insolent,',
     "A change of form: שברת is an ordinary past tense with the ending ת 'I', in place of the "
     "infinitive-plus-אנכ pattern. מלצמ is uncertain — 'scoffers' or 'the insolent', from the root of "
     "Hebrew לץ. The Luwian clause is just as uncertain, so the two versions cannot settle each other here.",
     par=[11])
unit('I 9', 'ותרק אנכ כל הרע אש כנ בארצ',
     'wa-tarōq ʾanōkī kull ha-raʿ ʾiš kūn ba-ʾarṣ',
     'and-cleared-out I all the-evil that was in-the-land.',
     'and I cleared away all the evil that was in the land.',
     "The root of תרק is uncertain; the sense 'cleared out' is safe because the Luwian says 'drove out "
     "of the land'.",
     par=[12, 13])
unit('I 9', 'ויטנא אנכ בת אדני בנעמ',
     'wa-yaṭnōʾ ʾanōkī bēt ʾadōnī ba-nuʿm',
     'And-set-up I the-house of-my-lord in-goodness,',
     'I established my lord’s house in prosperity,',
     "יטנא is the causative (Phoenician makes it with י where Hebrew uses ה) of a root meaning 'raise'. "
     "בת is 'house', Hebrew בית: Phoenician writes the contracted vowel without its י. 'My lord' is "
     "Awariku.",
     par=[14], p=True)
unit('I 10', 'ופעל אנכ לשרש אדני נעמ',
     'wa-paʿōl ʾanōkī la-šurš ʾadōnī nuʿm',
     'and-did I for-the-root of-my-lord good,',
     'and I did good to my lord’s line,',
     "שרש 'root' means descendants, as in Hebrew שרש ישי.",
     par=[15])
unit('I 11', 'וישב אנכ על כסא אבי',
     'wa-yašōb ʾanōkī ʿal kissiʾ ʾabīyu',
     'and-seated I (him) on the-throne of-his-father.',
     'and I set him on his father’s throne.',
     "A false friend for Hebrew readers: אבי here is 'his father', not 'my father'. After a noun ending "
     "in the genitive vowel -i, Phoenician writes 'his' as י (-yu). ישב is the causative, 'make sit' "
     "(Hebrew הושיב).",
     par=[16])
unit('I 11', 'ושת אנכ שלמ את כל מלכ',
     'wa-šōt ʾanōkī šalōm ʾitt kull milk',
     'And-made I peace with every king.',
     'I made peace with every king,',
     "שת 'put, make' is Hebrew שית; את is here the preposition 'with'. This clause is lost from both "
     "copies of the Luwian (§17); only the Phoenician keeps it.",
     par=[17])
unit('I 12', 'ואפ באבת פעלנ כל מלכ בצדקי בחכמתי ובנעמ לבי',
     'wa-ʾap ba-ʾabūt paʿalūnī kull milk ba-ṣidqī ba-ḥokmatī wa-ba-nuʿm libbī',
     'And-also in-fatherhood made-me every king, because-of-my-righteousness, because-of-my-wisdom, and-because-of-the-goodness of-my-heart.',
     'and every king even treated me as a father, for my justice, my wisdom and the goodness of my heart.',
     "Here the final י is 'my' (ṣidqī, ḥokmatī, libbī), against 'his' in אבי (line 11): the letter is "
     "the same, and the vowel before it decides. The Luwian of this clause is broken; its gaps are "
     "restored from this Phoenician sentence.",
     par=[18])
unit('I 13', 'ובנ אנכ חמית עזת בכל קצית על גבלמ',
     'wa-banō ʾanōkī ḥōmiyōt ʿazzōt ba-kull qaṣayōt ʿal gabūlīm',
     'And-built I walls strong at-all the-ends, on the-borders,',
     'I built strong walls at all the far ends, on the frontiers,',
     "חמית 'walls' is Hebrew חומות; קצית 'ends, edges' is Hebrew קצות; גבלמ 'borders' is Hebrew גבולים.",
     par=[19], p=True)
unit('I 14', 'במקממ באש כנ אשמ רעמ בעל אגדדמ',
     'ba-maqōmīm ba-ʾiš kūn ʾišīm raʿīm baʿlē ʾagdūdīm',
     'in-places in-which were men bad, masters of-bands,',
     'in places where there had been bad men, leaders of gangs,',
     "באש is ב 'in' plus the relative אש: 'in which'. אשמ is 'men' (Hebrew אנשים). בעל here is the "
     "ordinary noun, 'master, owner' — the same word as the god's name. אגדדמ: 'bands, troops', the "
     "root of Hebrew גדוד.",
     par=[20])
unit('I 15', 'אש בל אש עבד כנ לבת מפש',
     'ʾiš bal ʾiš ʿabd kūn la-bēt Mopš',
     'who — not a-man (of them) a-servant was to-the-house of-Mopsos.',
     'not one of whom had ever been subject to the house of Mopsos.',
     "בל 'not' is the negative of Hebrew poetry (בל ימוט). מפש is Mopsos, the seer whom Greek legend "
     "makes the founder of cities in Cilicia; the Luwian calls him Muksas. This is one of the few places "
     "where a figure of Greek myth turns up in a contemporary inscription.",
     par=[21])

for (ln, heb, tr, l, i, n, par) in REST:
    unit(ln, heb, tr, l, i, n, par=par, p=True)

# glossary: Hebrew-letter word form -> entry
G = {
 'אנכ': "ʾanōkī — I (independent pronoun; Hebrew אנכי)",
 'אזתוד': "ʾAzitiwadda — Azatiwada, ruler under Awariku and builder of the fortress at Karatepe; a Luwian name, perhaps 'beloved of the Sun' (Luwian Azzattiwadas)",
 'הברכ': "ha- + barūk — the blessed (one); article ה + passive participle of brk 'bless' (Hebrew ברוך)",
 'בעל': "baʿl — Baal, the storm god (the Luwian Tarhunzas); as a common noun, 'master, owner' (בעל אגדדמ 'masters of bands')",
 'עבד': "ʿabd — servant (Hebrew עבד)",
 'אש': "ʾiš — relative pronoun: who, whom, which, that (Hebrew אשר)",
 'אדר': "ʾiddir — made mighty, raised to power (D-stem of ʾdr 'mighty'; Hebrew אדיר)",
 'אורכ': "ʾAwarik — Awariku, king of the Danunians and Azatiwada's overlord (Luwian Awarikus)",
 'מלכ': "milk — king (Hebrew מלך)",
 'דננימ': "Dānunīm — the Danunians, the people of Adana (Luwian Hiyawa)",
 'פעלנ': "paʿal + -nī — (he/they) made me; pʿl 'do, make' (Phoenician's word for Hebrew עשה) + suffix -n 'me'",
 'לדננימ': "la- + Dānunīm — for/to the Danunians",
 'לאב': "la- + ʾab — into a father, as a father (Hebrew אב)",
 'ולאמ': "wa- + la- + ʾimm — and into a mother (Hebrew אם)",
 'יחו': "yaḥwō — I gave life to, made flourish (causative infinitive of ḥwy 'live'); with אנכ = 'I gave life'",
 'אית': "ʾiyyat — object marker, not translated (Hebrew את)",
 'ירחב': "yarḥeb — widened, enlarged (causative infinitive of rḥb 'be wide'; Hebrew הרחיב)",
 'ארצ': "ʾarṣ — land (Hebrew ארץ)",
 'עמק': "ʿimq — plain, valley (Hebrew עמק); עמק אדנ 'the Plain of Adana'",
 'אדנ': "ʾAdana — Adana, city and kingdom in the Cilician plain",
 'לממצא': "la- + mimṣaʾ — from the going-out, the rising (of the sun) (root yṣʾ 'go out'; Hebrew מוצא)",
 'שמש': "šamš — sun (Hebrew שמש)",
 'ועד': "wa- + ʿad — and as far as, until (Hebrew עד)",
 'מבאי': "mabōʾ + -iyu — its coming-in, its setting (root bwʾ 'come'; Hebrew מבוא) + 'its'",
 'וכנ': "wa- + kūn — and there was (infinitive of kwn 'be', Phoenician's verb for Hebrew היה)",
 'בימתי': "ba- + yamūt + -iya — in my days (plural of ym 'day', with the ending -ōt; Hebrew ימות)",
 'כל': "kull — all, every (Hebrew כל)",
 'נעמ': "nuʿm — good, goodness, prosperity (Hebrew נעם)",
 'ושבע': "wa- + šabʿ — and plenty, satiety (Hebrew שבע)",
 'ומנעמ': "wa- + manʿam — and delight, comfort (root nʿm; Hebrew מנעמים)",
 'ומלא': "wa- + millōʾ — and (I) filled (D-stem infinitive of mlʾ; Hebrew מילא)",
 'עקרת': "ʿaqarōt — storehouses, granaries (plural; a rare word, its sense fixed by the Luwian)",
 'פער': "Paʿar — a town or district of Adana (Luwian Pahar)",
 'ופעל': "wa- + paʿōl — and (I) made, did (infinitive of pʿl 'do, make')",
 'סס': "sūs — horse (Hebrew סוס)",
 'על': "ʿal — upon, on (Hebrew על)",
 'ומגנ': "wa- + magen — and shield (Hebrew מגן)",
 'מגנ': "magen — shield (Hebrew מגן)",
 'ומחנת': "wa- + maḥanet — and camp, army (Hebrew מחנה)",
 'מחנת': "maḥanet — camp, army (Hebrew מחנה)",
 'בעבר': "ba-ʿabūr — for the sake of, by the grace of (Hebrew בעבור)",
 'ואלמ': "wa- + ʾilīm — and the gods (plural of ʾl 'god'; Hebrew אלים)",
 'ושברת': "wa- + šibbartī — and I broke, shattered (past tense, ending -tī 'I'; Hebrew שברתי)",
 'מלצמ': "malīṣīm — scoffers, the insolent (meaning uncertain; root of Hebrew לץ)",
 'ותרק': "wa- + tarōq — and (I) cleared out, purged (root uncertain; sense fixed by the Luwian)",
 'הרע': "ha- + raʿ — the evil (Hebrew הרע)",
 'כנ': "kūn — was, were (infinitive of kwn 'be')",
 'בארצ': "ba- + ʾarṣ — in the land (Hebrew בארץ)",
 'ויטנא': "wa- + yaṭnōʾ — and (I) set up, established (causative infinitive of ṭnʾ 'raise')",
 'בת': "bēt — house, household, dynasty (Hebrew בית)",
 'אדני': "ʾadōnī — my lord (Hebrew אדני); here Awariku",
 'בנעמ': "ba- + nuʿm — in goodness, in prosperity",
 'לשרש': "la- + šurš — for the root, i.e. the descendants (Hebrew שרש)",
 'וישב': "wa- + yašōb — and (I) seated, set (causative infinitive of yšb 'sit'; Hebrew הושיב)",
 'כסא': "kissiʾ — throne (Hebrew כסא)",
 'אבי': "ʾabīyu — his father (ʾab 'father' + -y 'his' after the genitive vowel; not 'my father')",
 'ושת': "wa- + šōt — and (I) put, made (infinitive of šyt; Hebrew שית)",
 'שלמ': "šalōm — peace (Hebrew שלום)",
 'את': "ʾitt — with (preposition; Hebrew את 'with')",
 'ואפ': "wa- + ʾap — and also, and even (Hebrew אף)",
 'באבת': "ba- + ʾabūt — in fatherhood, as a father (abstract noun from ʾab 'father')",
 'בצדקי': "ba- + ṣidq + -ī — because of my righteousness, my justice (Hebrew צדק)",
 'בחכמתי': "ba- + ḥokmat + -ī — because of my wisdom (Hebrew חכמה)",
 'ובנעמ': "wa- + ba- + nuʿm — and because of the goodness",
 'לבי': "libb + -ī — my heart (Hebrew לבי)",
 'ובנ': "wa- + banō — and (I) built (infinitive of bny 'build'; Hebrew בנה)",
 'חמית': "ḥōmiyōt — walls, fortifications (Hebrew חומות)",
 'עזת': "ʿazzōt — strong (feminine plural of ʿz; Hebrew עזות)",
 'בכל': "ba- + kull — in all, at every",
 'קצית': "qaṣayōt — ends, edges, far reaches (Hebrew קצות)",
 'גבלמ': "gabūlīm — borders, frontiers (Hebrew גבולים)",
 'במקממ': "ba- + maqōmīm — in places (Hebrew מקומות)",
 'באש': "ba- + ʾiš — in which, where (ב 'in' + relative אש)",
 'אשמ': "ʾišīm — men (plural of ʾš 'man'; Hebrew אנשים)",
 'רעמ': "raʿīm — bad, evil (plural; Hebrew רעים)",
 'אגדדמ': "ʾagdūdīm — bands, troops of raiders (Hebrew גדודים)",
 'בל': "bal — not (the negative of Hebrew poetry, בל)",
 'לבת': "la- + bēt — to the house (dynasty) of",
 'מפש': "Mopš — Mopsos, legendary founder of the ruling house of Adana (Luwian Muksas; Greek Μόψος)",
}

for k, v in GLOSS.items():
    if k in G and G[k] != v: sys.exit('glossary clash: ' + k)
    G[k] = v
G.update(UPDATE)

# Luwian clause -> the Luwian story that holds it (the pilot, then Run 3's three parts)
def luwian_id(c):
    c = int(re.match(r'\d+', str(c)).group())
    return ('azatiwada-luwian' if c <= 21 else 'azatiwada-22-37' if c <= 37
            else 'azatiwada-38-58' if c <= 58 else 'azatiwada-59-75')

def main():
    out_units, gl = [], {}
    used = set()
    for k, u in enumerate(U):
        words = u['heb'].split()
        for w in words:
            if w not in G: sys.exit('no glossary entry: ' + w)
            used.add(w)
        su = {'ln': u['ln'], 't': phx(u['heb']), 'tr': u['tr'], 'l': u['l']}
        if u['i'] and u['i'] != u['l']: su['i'] = u['i']
        if u['n']: su['n'] = u['n']
        if u['p']: su['p'] = True
        if u['par']:
            lns = [int(re.match(r'\d+', str(c)).group()) for c in u['par']]
            lns = sorted(set(lns), key=lns.index)
            su['par'] = {'id': luwian_id(lns[0]), 'ln': lns, 'clause': True}
        out_units.append(su)
    unused = set(G) - used
    if unused: sys.exit('unused glossary entries: ' + ' '.join(sorted(unused)))
    for w in used: gl[phx(w)] = G[w]

    # witness check: A I 1–16 up to מפש, line-break hyphens removed, emendations applied
    wl = [x for x in WITNESS if x['side'] == 'a']
    wtoks = []
    for x in wl:
        for w in x['words']:
            w = re.sub(r'[-–⸢⸣\[\]]', '', w)
            for (where, a, b, _) in EMEND:
                if (x['col'], int(x['line'])) == where and w == a: w = b
            wtoks.append(w)
    ours = ' '.join(u['heb'] for u in U).split()
    if ours != wtoks:
        for a, b in zip(ours, wtoks):
            if a != b: sys.exit('witness mismatch: ours %s vs witness %s' % (a, b))
        sys.exit('witness length mismatch %d vs %d' % (len(ours), len(wtoks)))

    story = {
      'id': 'azatiwada-phoenician',
      'title': '𐤀𐤆𐤕𐤅𐤃',
      'titleEn': 'The Azatiwada Inscription (Karatepe), Phoenician',
      'work': '𐤀𐤆𐤕𐤅𐤃',
      'workEn': 'The Azatiwada Inscription (Karatepe), Phoenician',
      'part': 'Copy A, the lower gate · columns I–IV',
      'language': 'Phoenician',
      'langCode': None,
      'script': 'phoenician',
      'rtl': True,
      'trStyle': 'line',
      'numbering': 'colline',
      'provisional': True,
      'draftNote': 'The letters follow one published reading of the stone and are still to be checked against photographs; two readings (I 1, I 16) depart from it, as the notes there say.',
      'parallel': {'label': 'Luwian'},
      'about': ("Around 700 BCE Azatiwada, a governor under the king of Adana in Cilicia, built a fortress "
                "on a hill above the Ceyhan river and carved his account of his deeds on its gates in two "
                "languages: the local Luwian, in Anatolian hieroglyphs, and Phoenician, the language of "
                "trade and diplomacy along the coast. This is the Phoenician. It is the longest Phoenician "
                "inscription ever found, and close kin to biblical Hebrew — a Hebrew reader will recognize "
                "most of its words. The same text in Luwian is in the library too: each section here links "
                "to its twin."),
      'source': ("KARATEPE, Phoenician version, copy A (the lower gate), columns I–IV, complete (KAI 26 A; "
                 "Gibson, Textbook of Syrian Semitic Inscriptions III no. 15). Found in 1946–47, so no "
                 "edition before 1930 exists; following the policy adopted for the Luwian, the sequence of "
                 "letters on the stone is treated as a fact, taken from the reading published by DEAPS "
                 "(Digital Editions of Aramaic and Phoenician Sources, Ohio State University; 'Phoe. Class "
                 "2026' edition, following Gibson 1988), and still to be checked against photographs. Two "
                 "departures, in I 1 and I 16, are explained in their notes; letters the source restores in "
                 "damaged places (III 1–2) are printed, and the note says so. The two other copies (C, on the "
                 "statue of the god; B, fragments) are not printed; where C differs in substance, a note says "
                 "so. Line numbers give the column and the stone line where each section begins; words the stone breaks over a line end are printed whole. The stone "
                 "leaves no spaces between words; the spaces here follow the editions. Vocalization (the "
                 "line under the letters) is reconstructed — Phoenician wrote no vowels — after the "
                 "conventions of the standard grammars, and applied consistently; the actual vowels are "
                 "unknown in many words. The Hebrew-letters switch shows the same consonants in the square "
                 "script. Translations are made fresh from the Phoenician; no modern translation was "
                 "consulted. Font: Noto Sans Phoenician (OFL)."),
      'sentences': out_units,
      'glossary': gl,
    }
    # reverse links: each Luwian clause -> the Phoenician unit holding its parallel
    lw = json.load(open('azatiwada-luwian.json', encoding='utf-8'))
    back = {}
    for k, u in enumerate(U):
        for c in (u['par'] or []):
            back.setdefault(int(re.match(r'\d+', str(c)).group()), {'ln': u['ln'], 'u': k})
    lw['parallel'] = {'id': 'azatiwada-phoenician', 'label': 'Phoenician'}
    for x in lw['sentences']:
        if x.get('ln') in back:
            x['par'] = {'id': 'azatiwada-phoenician', 'ln': [back[x['ln']]['ln']], 'u': back[x['ln']]['u']}
    # the same map for Run 3's later Luwian parts (their build reads it)
    with open(os.path.join(os.path.dirname(HERE), 'azatiwada', 'phoenician-parallels.json'), 'w', encoding='utf-8') as f:
        json.dump({str(k): v for k, v in sorted(back.items())}, f, ensure_ascii=False, indent=1)
    with open('azatiwada-luwian.json', 'w', encoding='utf-8') as f:
        json.dump(lw, f, ensure_ascii=False, indent=1)
    with open('azatiwada-phoenician.json', 'w', encoding='utf-8') as f:
        json.dump(story, f, ensure_ascii=False, indent=1)
    print('units', len(out_units), 'words', len(ours), 'glossary', len(gl))

if __name__ == '__main__':
    main()
