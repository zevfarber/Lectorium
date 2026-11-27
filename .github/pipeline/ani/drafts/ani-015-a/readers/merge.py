import json
J=lambda f: json.load(open(f))['words']
KEYS=('page','plate','chapter','line','signs','q','budge','gloss','rubric','restored','approx','unsure')
DEC=[]
def pick(w): return {k:w[k] for k in KEYS if k in w}
def find(W, budge, page, n=0):
    hits=[i for i,w in enumerate(W) if w['budge']==budge and w['page']==page]
    return hits[n]
def dec(w, st, decision, why, **kw):
    for k,v in kw.items():
        if v is None: w.pop(k,None)
        else: w[k]=v
    w['approx']=[c for c in w.get('approx',[]) if c in w['signs']]
    if not w['approx']: w.pop('approx')
    w['unsure']=(w.get('unsure','')+' · ' if w.get('unsure') else '')+'Decision (%s): %s'%(decision,why)
    DEC.append(dict(stretch=st, page=w['page'], budge=w['budge'], decision=decision, why=why, signs=w['signs']))
def addB(w, b):
    if b.get('unsure') and b['unsure']!=w.get('unsure'): w['unsure']=(w.get('unsure','')+' · ' if w.get('unsure') else '')+'B: '+b['unsure']
    if 'q' not in w and b.get('q') and b['signs']==w['signs']: w['q']=b['q']

# ---- stretch 1
A=[pick(w) for w in J('A1.json')]; B=J('B1.json')
bi={}  # align by order: equal length except Ḥeru χuti (B 1 word) and mer|Ṭes Ṭes (B 2 words)
j=0
for i,w in enumerate(A):
    if w['budge']=='χuti' and w['page']==123: continue
    bi[i]=j; j+=1
    if w['budge']=='mer Ṭes Ṭes': j+=1
for i,w in enumerate(A):
    if i in bi and B[bi[i]]['signs']==w['signs']: addB(w,B[bi[i]])
i=find(A,'Ani',123); dec(A[i],1,'B',"Ani's det is the kneeling man with one open hand raised before the face, no flail: A1", signs=A[i]['signs'][:5]+['A1'])
i=find(A,'neferu - k',123); dec(A[i],1,'B',"Budge prints neferu-k without spaces", budge='neferu-k')
i=find(A,'maa - à',123); dec(A[i],1,'B',"Budge prints maa-à without spaces; two eyes, no sickle", budge='maa-à')
i=find(A,'āṭtet',123); dec(A[i],1,'own',"first sign the crossed lens shape = netting needle V26 approx, as the house codes āṭet (hymn to Ra) and āṭ (Spell 9); under it the flat hand D46 (Budge ṭ)", signs=['V26','D46','X1','X1','P3'], approx=['V26','P3'])
for pg in (123,124):
    b='nemà - [k]' if pg==123 else 'nemà - k'
    i=find(A,b,pg); s=['O38' if c=='O1' else c for c in A[i]['signs']]
    dec(A[i],1,'B',"the open ⊔⊓ meander-like sign is no house: O38 approx (corner) nearer than O1", signs=s, approx=['T34','O38'])
i=find(A,'χefta - k',123); dec(A[i],1,'A/B',"kneeling enemy with arm raised A13 approx (house, Spell 18); the small circle stands above the strokes: N33 Z2 (B's order)", signs=['Aa1','I9','X1','G1','A13','N33','Z2','V31'], approx=['A13','N33'])
i=find(A,'ḥennu - nek',123); dec(A[i],1,'A/B',"Budge prints h without a dot (hennu); the kneeling figure has both arms raised: A4 approx", budge='hennu - nek')
i=find(A,'àuχemu',123); dec(A[i],1,'A',"after the owl a cross-like sign on a base with three strokes: the negation arms D35 approx (not R22)", approx=['D35'])
i=find(A,'àterti',124); A[i]['unsure']=(A[i].get('unsure','')+' · ' if A[i].get('unsure') else '')+"Budge prints 'àterti (?)' and his English in braces '{the two halves of the sky,}'"
# split mer Ṭes Ṭes as Budge spaces it (B)
i=find(A,'mer Ṭes Ṭes',124); base=A[i]; b1,b2=B[bi[i]],B[bi[i]+1]
w1=dict(pick(b1)); w2=dict(pick(b2))
for w in (w1,w2): w['plate']=base['plate']; w['line']=base['line']; w['chapter']='XV'
dec(w1,1,'B',"Budge spaces mer | Ṭes Ṭes as separate groups: two words")
A[i:i+1]=[w1,w2]
i=find(A,'Sebàu',124); dec(A[i],1,'B',"the Y-forked upright has no good code; Aa26 approx as B (S43 has no fork); doubtful", signs=['Aa26','N33','Z2'], approx=['Aa26','N33'])
S1=A

# ---- stretch 2
A=[pick(w) for w in J('A2.json')]
i=find(A,'seḳer',125); A[i]['unsure']=(A[i].get('unsure','')+' · ' if A[i].get('unsure') else '')+'Decision (A): Budge prints ḳ with the dot'
DEC.append(dict(stretch=2,page=125,budge='seḳer',decision='A',why='dotted ḳ printed',signs=A[i]['signs']))
i=find(A,'ṭu',125); dec(A[i],2,'A',"N26 over O31 with a short stroke, then a tall dashed stroke: Z1 Z1")
i=find(A,'peḥreru',125); dec(A[i],2,'A',"the man carries a stick over his shoulder: A33 approx; Budge prints '(?)' after peḥreru")
i=find(A,'nub - nef',125); dec(A[i],2,'B',"a foot/leg stands under the collar's stand: S12 D58 (b complement), then the looped flat sign U15; one word as Budge hyphenates", signs=['S12','D58','U15','N35','I9'], approx=['S12','D58'], q=None)
i=find(A,'nept',125); dec(A[i],2,'A',"the small hourglass-like sign has no exact code: N23 approx (B left it unread)")
i=find(A,'seqa - tu',125); dec(A[i],2,'A',"the long flat bar with a small tuft on top is not Y1: Aa13 approx")
i=find(A,'ḥesb',125); dec(A[i],2,'A',"oval with band Aa2 approx over the flat bar with a tuft Aa13 approx")
i=find(A,'ḥru',125); dec(A[i],2,'B',"Budge prints hru with an undotted h", budge='hru')
i=find(A,'mer',125); dec(A[i],2,'A',"the angled hoe U6 (nes's top sign is the tongue F20, drawn alike)")
S2=A

# ---- stretch 3
A=[pick(w) for w in J('A3.json')]; B=J('B3.json')
j=0
for i,w in enumerate(A):
    if w['budge']=='χuti': continue
    b=B[j]; j+=1
    if b['signs']==w['signs']: addB(w,b)
i=find(A,'Àbṭu',126); dec(A[i],3,'B',"the Abydos fetish (wig on a pole with plumes), no ankh: R17 approx", signs=['R17','O49'], approx=['R17'])
i=find(A,'meri - f',126); dec(A[i],3,'B',"flared bar over a stroke = the canal N36, not the hoe", signs=['N36','Z1','I9'], approx=None)
i=find(A,'Ani',126); dec(A[i],3,'A',"Ani squats with knee raised and a flail at the shoulder: A52")
i=find(A,'ṭuau',126); dec(A[i],3,'A',"long-corded loop V4 approx; the figure raises both arms: A28 approx")
i=find(A,'Ḥeru',126); bw=pick(B[16]); bw['line']=A[i]['line']
dec(bw,3,'B',"Budge prints 'Ḥeru - χuti' with his hyphen: one word")
A[i:i+2]=[bw]
i=find(A,'Ḥet-ka-Ptaḥ',126); dec(A[i],3,'A',"coded in print order inside the enclosure")
i=find(A,'sem',126); dec(A[i],3,'B',"the sšm sign (blade on a support with hooked end) T32 approx; doubtful", signs=['O34','T32','G17','D54'], approx=['T32'])
i=find(A,'χu - sen - tu',126); dec(A[i],3,'B',"under the hatched disc a bent arm D41 approx; the knotted upright T3 approx; both doubtful", signs=['Aa1','D41','G43','T3','O34','N35','Z2','X1','G43'], approx=['D41','T3'])
i=find(A,"seḥet' - k",126); dec(A[i],3,'B',"a cobra (Budge t') over the disc with rays: I10 N8", signs=['S29','T3','I10','N8','V31'], approx=['N8'])
i=find(A,'smu',126); dec(A[i],3,'A',"the arched sign with a fringe of beads is the collar S12")
for b in ('maa - nek','maa-sen'):
    i=find(A,b,126); s=A[i]['signs']; k=s.index('U1'); s=s[:k]+[s[k+1],'U1']+s[k+2:] if s[k+1]=='D4' else s
    dec(A[i],3,'B',"eye with the sickle over it coded D4 U1 (house order)", signs=s)
i=find(A,'meḥu',126); dec(A[i],3,'B',"scroll-like bar pierced by a stem with a triangle: V22 approx (mḥ), not the sail", signs=['V22','G43','Z1'], approx=['V22'])
S3=A

out=S1+S2+S3
for w in out:
    w['chapter']='XV'
    if w.get('q'):
        import re
        idx=sorted(int(x) for x in re.findall(r'\d+',w['q']))
        if idx!=list(range(len(w['signs']))): w.pop('q')
json.dump(out,open('merged.json','w'),ensure_ascii=False,indent=1)
json.dump({'decider':'run lead (routine model) from crops at zoom 3–7','decisions':DEC},open('decisions.json','w'),ensure_ascii=False,indent=1)
print(len(out),len(S1),len(S2),len(S3),'rubric',sum(1 for w in out if w.get('rubric')),'approx',sum(1 for w in out if w.get('approx')),'unsure',sum(1 for w in out if w.get('unsure')),'dec',len(DEC))
