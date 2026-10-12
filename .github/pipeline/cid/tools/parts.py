import json,re
L=json.load(open('lines.json'))
I="Cantar I (Destierro)"; II="Cantar II (Bodas)"; III="Cantar III (Corpes)"
# (tirada_from, start_label or None, tirada_to, end_label or None, name, cantar)
spec=[
(5,None,9,None,"Martín Antolínez supplies the camp; the sand-filled chests are pawned to Raquel and Vidas",I),
(10,None,14,None,"The moneylenders pay; the Cid leaves Burgos for San Pedro de Cardeña",I),
(15,None,17,None,"At Cardeña: Jimena's plea, and Castilians gather to follow the Cid",I),
(18,None,18,None,"The last night at Cardeña: Jimena's prayer, the farewells, the road into exile",I),
(19,None,23,None,"The angel's dream; the border crossed; Castejón surprised and the Henares raided",I),
(24,None,26,None,"Minaya's vow; the spoils sold to the Moors; the march toward the Jalón",I),
(27,None,31,None,"Camp before Alcocer; the town taken by a feigned retreat",I),
(32,None,34,None,"Fáriz and Galve besiege Alcocer; the sally, and Pero Vermúdez charges with the banner",I),
(35,None,39,None,"The battle below Alcocer: Fáriz wounded, Galve routed",I),
(40,None,43,None,"Counting the spoil; Minaya rides to King Alfonso with a gift",I),
(44,None,48,None,"Alcocer sold; camp on the hill by Monreal; the king half-pardons Minaya",I),
(49,None,55,None,"Raids from the hill; Minaya returns with men; the count of Barcelona takes offence",I),
(56,None,59,None,"Battle with the count of Barcelona; Colada won; the captive count refuses food",I),
(60,None,63,None,"The count eats and is set free; the exiles grow rich",I),
(64,None,68,None,"Toward Valencia: Murviedro taken and the Moorish armies beaten",II),
(69,None,74,None,"Raids south of Valencia; the call to arms; the siege and fall of the city",II),
(75,None,77,None,"The king of Seville repulsed; the uncut beard; a second gift for the king",II),
(78,None,82,None,"Jerónimo made bishop; Minaya's embassy wins leave for Jimena; the Infantes take notice",II),
(83,None,83,"1452","Minaya fetches Jimena and the daughters from Cardeña",II),
(83,"1453",83,None,"The Cid's escort and Avengalvón meet the ladies at Medinaceli",II),
(84,None,86,None,"Through Molina to Valencia; the Cid rides Babieca to greet his family",II),
(87,None,90,None,"The ladies look out over Valencia; King Yúsuf lands from Morocco",II),
(91,None,94,None,"Jimena reassured; the battle plan; the bishop asks for the first blows",II),
(95,None,95,None,"The battle against Yúsuf and the great spoil",II),
(96,None,101,None,"Minaya brings the king a gift; royal favour; the Infantes plan the marriages",II),
(102,None,102,None,"The king proposes the marriages and a meeting with the Cid",II),
(103,None,104,"2012","Both sides make ready for the meeting on the Tagus",II),
(104,"2013",104,"2067","The Cid kneels before Alfonso and is pardoned",II),
(104,"2068",104,None,"The king asks the daughters' hands for the Infantes",II),
(105,None,108,None,"Gifts and leave-taking; the Cid tells Jimena of the matches",II),
(109,None,111,None,"Jimena glad, the Cid uneasy; the weddings in Valencia",II),
(112,None,114,None,"The lion breaks loose; the Infantes' fear; King Búcar lands",III),
(115,None,117,None,"Búcar's message; Fernando's cowardice; the bishop opens the battle",III),
(118,None,119,None,"Búcar killed and Tizón won; the victory and the spoils",III),
(120,None,123,None,"The Cid content with his sons-in-law; their boasting and the household's jests",III),
(124,None,125,None,"The Infantes ask to take their wives to Carrión; Jimena's farewell",III),
(126,None,127,None,"Félez Muñoz sent along; Avengalvón learns of the plot and leaves them",III),
(128,None,130,None,"The oak wood of Corpes: the daughters stripped, beaten and abandoned",III),
(131,None,131,None,"Félez Muñoz finds and rescues his cousins",III),
(132,None,133,None,"Minaya brings the daughters home; Muño Gustioz asks the king for justice",III),
(134,None,136,None,"The king summons a court at Toledo; the Cid's vigil at San Servando",III),
(137,None,137,"3126","The Cid dresses for the court and enters it",III),
(137,"3127",137,"3198","The court opens; Colada and Tizón are handed back",III),
(137,"3199",137,None,"The Cid claims the dowry money",III),
(138,None,143,None,"The Cid charges the Infantes with dishonour; Pero Vermúdez challenges Fernando",III),
(144,None,149,"3408","Martín Antolínez and Muño Gustioz challenge; envoys of Navarre and Aragon arrive",III),
(149,"3409",149,None,"The new marriages granted; Minaya's challenge; the combats set; the Cid takes leave",III),
(150,None,150,"3570","Babieca and the king; the champions wait at Carrión",III),
(150,"3571",150,None,"The lists; Pero Vermúdez defeats Fernando",III),
(151,None,152,None,"Martín Antolínez and Muño Gustioz win; the second marriages; the end",III),
]
T=json.load(open('tiradas.json'))
pages={t['tirada']:t['pdf_pages'] for t in T}
def numkey(n):
    m=re.match(r'(\d+)(?:-(\d+))?([a-z]?)',n); return (int(m.group(1)),m.group(3))
ABSENT={99,1043,2432,2459,3663,3679}
parts=[]
for seq,(ta,sa,tb,sb,name,cantar) in enumerate(spec,2):
    sel=[];on=sa is None
    for l in L:
        if l['tir']<ta or l['tir']>tb: continue
        if l['tir']==ta and sa and l['num']==sa: on=True
        if on: sel.append(l)
        if l['tir']==tb and sb and l['num']==sb: break
    verse=[l for l in sel if l['num']!='PROSE']
    nums=[l['num'] for l in verse]
    pid=f"cid-tiradas-{ta:02d}-{tb:02d}"
    if sa or sb:
        st=tb if sb else ta; k=sum(1 for q in parts if q[0]['tiradaSplitOf']==st)
        pid+="abc"[k]
    ints=[numkey(n)[0] for n in nums]
    lo,hi=min(ints),max(ints)
    p={'id':pid,'seq':seq,'cantar':cantar,'tiradas':[ta,tb],'tiradaSplit': bool(sa or sb),'tiradaSplitOf': (tb if sb else ta) if (sa or sb) else None,
       'lines':{'first':nums[0],'last':nums[-1],'min':lo,'max':hi},'lineCount':len(nums),
       'pdfPages':sorted(set(l['pn'] for l in sel)),'printedPages':None,'name':name}
    p['printedPages']=[p_-4 for p_ in p['pdfPages']]
    flags=[]
    if any(l['num']=='PROSE' for l in sel): flags.append(f"contains {sum(1 for l in sel if l['num']=='PROSE')} printed lines of Pidal's italic prose restoration (lost folio) — not verse; decide handling")
    if any(l['ital'] for l in verse): flags.append("wholly italic restored line(s): "+', '.join(l['num'] for l in verse if l['ital']))
    if any(l['over'] for l in verse): flags.append("line numbering unresolved (more printed lines than margin numbers allow): "+', '.join(l['num'] for l in verse if l['over']))
    if nums!=sorted(nums,key=numkey): flags.append("Pidal transposes lines here (print order differs from numeric order)")
    if any(not l['t'] for l in verse): flags.append("no OCR text for: "+', '.join(l['num'] for l in verse if not l['t']))
    gaps=[i for i in range(lo,hi+1) if i in ABSENT]
    if gaps: flags.append("numbers printed nowhere in the verse column (see REPORT): "+', '.join(map(str,gaps)))
    p['flags']=flags
    parts.append((p,sel))
# id: make tirada split ids unique & readable
out={'work':'Cantar de mio Cid','workEn':'The Song of the Cid',
 'edition':"Ramón Menéndez Pidal (ed.), Poema de mio Cid, 2.ª edición corregida (Clásicos Castellanos 24; Madrid: Ediciones de \"La Lectura\", 1923); scan archive.org PoemaDeMioCid2ed (pdfPages = 1-based page index in pidal1923_text.pdf; printed page = pdf page − 4)",
 'note':"seq 1 is the published pilot cid-tiradas-01-04 (lines 1–64). lineCount counts printed verse lines including Pidal's b-lines and wholly italic restored lines; first/last are in print order (Pidal sometimes transposes lines), min/max numeric.",
 'parts':[p for p,_ in parts]}
json.dump(out,open('/home/claude/work/cid/parts.json','w'),ensure_ascii=False,indent=1)
for p,sel in parts:
    with open(f"/home/claude/work/cid/ocr/{p['id']}.txt",'w') as f:
        f.write(f"# {p['id']} — tiradas {p['tiradas'][0]}–{p['tiradas'][1]}, lines {p['lines']['first']}–{p['lines']['last']}, pdf pages {p['pdfPages'][0]}–{p['pdfPages'][-1]}\n")
        f.write("# DRAFT OCR (archive.org text layer), mechanically cleaned. Italics LOST; ç usually read as q/£/(; verify every line against the page image.\n")
        f.write("# Line labels: Pidal's numbers as inferred from margin labels (every 5th) + counting; '[ITALIC LINE]' = wholly italic restored line; 'PROSE' = Pidal's prose restoration of a lost folio.\n")
        cur=None
        for l in sel:
            if l['tir']!=cur:
                cur=l['tir']; f.write(f"## tirada {cur}\n")
            tag=''
            if l['ital']: tag='\t[ITALIC LINE]'
            if l['over']: tag='\t[NUMBER UNCERTAIN]'
            f.write(f"{l['num']}\t{l['t']}{tag}\n")
for p,_ in parts: print(p['seq'],p['id'],p['lines']['first'],p['lines']['last'],p['lineCount'],p['pdfPages'][0],p['pdfPages'][-1],len(p['flags']))
print(sum(p['lineCount'] for p,_ in parts))
