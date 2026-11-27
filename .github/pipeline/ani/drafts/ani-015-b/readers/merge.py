import json, re
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
def fromB(w,b,keys=('signs','q','approx')):
    for k in keys:
        if k in b: w[k]=b[k]
        else: w.pop(k,None)
def addB(w, b):
    if b.get('unsure') and b['unsure']!=w.get('unsure'): w['unsure']=(w.get('unsure','')+' · ' if w.get('unsure') else '')+'B: '+b['unsure']
    if 'q' not in w and b.get('q') and b['signs']==w['signs']: w['q']=b['q']
def align(A,B):
    import difflib
    ka=[(w['page'],w['budge'].replace(' ','')) for w in A]; kb=[(w['page'],w['budge'].replace(' ','')) for w in B]
    m={}
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,ka,kb,autojunk=False).get_opcodes():
        if op=='equal':
            for i,j in zip(range(i1,i2),range(j1,j2)): m[i]=j
    return m
def bw(A,B,m,budge,page,n=0):
    i=find(A,budge,page,n); return A[i], B[m[i]]

# ---- stretch 1 (A1 base: splits ànet' | ḥrà - k as Budge spaces them)
A=[pick(w) for w in J('A1.json')]; B=J('B1.json'); m=align(A,B)
for i,j in m.items():
    if B[j]['signs']==A[i]['signs']: addB(A[i],B[j])
n=sum(1 for w in A if w['budge']=="ànet'")
for k in range(n):
    i=[x for x,w in enumerate(A) if w['budge']=="ànet'"][k]
    dec(A[i],1,'A',"Budge spaces ànet' | ḥrà - k as two transliteration groups under one overline: two words (as mer | Ṭes Ṭes in ani-015-a)")
i=find(A,'χabes',127); dec(A[i],1,'B',"first sign a tall stem with a curled top on a flared base: M12 approx (lotus-like); Q7 (brazier) does not fit; doubtful", signs=['M12']+A[i]['signs'][1:], approx=['M12'])
i=find(A,'χer-āba',127); dec(A[i],1,'A',"no low flat sign is printed between N29 and O49")
w,b=bw(A,B,m,'śeta',127); fromB(w,b); dec(w,1,'B',"first sign the long hatched rectangle: N37 (š, house), not the bolt")
w,b=bw(A,B,m,'peṭ',127); dec(w,1,'own',"Q3, the bar with turned-down ends (N1 approx) over the flat hand D46 (Budge ṭ), then D54; whether D54 belongs here or to nemmat is unclear (spacing favours peṭ)", signs=['Q3','N1','D46','D54'], approx=['N1'])
w,b=bw(A,B,m,'ba',127); fromB(w,b); dec(w,1,'B',"the small bowl with wisps before the ram is the incense bowl R7 (house: R7 coded before the ba-sign); the ram E10")
for k in range(2):
    pg=[127,128][k]; w,b=bw(A,B,m,'Ṭeṭṭu',pg); fromB(w,b); dec(w,1,'B',"the flat sign over the chick is the hand D46 (Budge dotted ṭ), not the cobra")
w,b=bw(A,B,m,'urert',127); dec(w,1,'A',"the crown with a curl set on a basket, one sign: S4 approx (red crown on basket)")
w,b=bw(A,B,m,'temt - f',128); dec(w,1,'A',"the sledge with upturned end U15 (tm), no jackal head")
w,b=bw(A,B,m,'atet - f',128); fromB(w,b); dec(w,1,'B',"animal head with open jaws: the leopard head F9 approx (ꜣt), not the lion forepart")
w,b=bw(A,B,m,'Na - àreṭ - f',128); fromB(w,b); dec(w,1,'B',"under D21 the flat hand D46 (Budge ṭ); then the looped sign with splayed legs T12 approx; O1 approx as printed")
w,b=bw(A,B,m,'Àbṭu',128); fromB(w,b); dec(w,1,'B',"the flat sign over the coil is the hand D46 (Budge ṭ)")
w=A[find(A,'tepḥet - f',128)]; dec(w,1,'A',"no dot is visible under the first t of Budge's transliteration at zoom 6")
w,b=bw(A,B,m,'χat - f',128); fromB(w,b); dec(w,1,'B',"the fish K4 stands on top, X1 and an oval (Aa2 approx) under it")
w,b=bw(A,B,m,'suten net',128); fromB(w,b); dec(w,1,'B',"M23 with X1 under it, then the bee L2 with X1 under it: M23 X1 L2 X1")
S1=A

# ---- stretch 2
A=[pick(w) for w in J('A2.json')]; B=J('B2.json'); m=align(A,B)
for i,j in m.items():
    if B[j]['signs']==A[i]['signs']: addB(A[i],B[j])
i=find(A,'āq',129); dec(A[i],2,'A',"two upright strokes as one sign Z4A (house), then the tall slanted sign Aa28 approx")
i=find(A,'àmu - χet - f',129); dec(A[i],2,'A',"the seated figure has a long wig: A40 approx")
w=A[find(A,'àten',129)]; dec(w,2,'B',"Budge prints àṭen with a dotted ṭ (zoom 6)", budge='àṭen')
w,b=bw(A,B,m,'Māāṭet',130); fromB(w,b); dec(w,2,'B',"the crossed-curves sign is the netting needle V26 approx, as the house codes āṭet (hymn to Ra, ani-015-a)")
w,b=bw(A,B,m,'àbeχ - f',130); fromB(w,b); dec(w,2,'B',"kneeling man carrying a load on his head: A9 approx")
w,b=bw(A,B,m,'taiu',130); fromB(w,b); dec(w,2,'B',"two rows, each N16 followed by N21: N16 N21 N16 N21")
i=find(A,'suten',130); dec(A[i],2,'A',"a seated long-wigged figure is printed after N35: A40")
i=find(A,'qemāt - s',130); dec(A[i],2,'A',"the low flat sign U15 crosses the foot of M26; X1 over a tilted oval (H8 approx); then I12 O34")
i=find(A,'meḥt - s',130); dec(A[i],2,'A',"M16, X1 over the tilted oval (H8 approx), I12, O34 — as qemāt - s")
i=find(A,'àpt - k',130); dec(A[i],2,'A',"Budge prints àpt with a dotted à")
S2=A

# ---- stretch 3
A=[pick(w) for w in J('A3.json')]; B=J('B3.json'); m=align(A,B)
for i,j in m.items():
    if B[j]['signs']==A[i]['signs']: addB(A[i],B[j])
w=A[find(A,'sesunneṭ',131)]; b=B[find(B,'sesunnet',131)]; fromB(w,b); dec(w,3,'B',"the long rounded sign with a tab at its right X4 approx over a slab on three legs with a small Y on it (T28 approx; the strokes Z2 may be its legs); all doubtful")
w=A[find(A,'maaau',131)]; dec(w,3,'A/B',"signs as A (eye D4 then sickle U1, house order); Budge prints maau", budge='maau')
i=find(A,'maa',131); dec(A[i],3,'A',"house order D4 U1")
i=find(A,'hru',131); dec(A[i],3,'A',"Budge prints hru with no dot (zoom 6)")
w=A[find(A,'ṭeḳa',131)]; b=B[find(B,'ṭeka',131)]; fromB(w,b); dec(w,3,'B',"same long rounded sign as in sesunneṭ (X4 approx) over a trapezoid stand Q7 approx; Budge prints ṭeka, undotted k", budge='ṭeka')
w,b=bw(A,B,m,'śepses - nek',131); dec(w,3,'own',"the noble seated on a chair A51 approx (B); after Y1a a single dashed stroke Z1 (A)", signs=['A51']+w['signs'][1:], approx=['A51'])
S3=A

out=S1+S2+S3
for w in out:
    w['chapter']='XV'
    if w.get('q'):
        idx=sorted(int(x) for x in re.findall(r'\d+',w['q']))
        if idx!=list(range(len(w['signs']))): w.pop('q')
json.dump(out,open('merged.json','w'),ensure_ascii=False,indent=1)
json.dump({'decider':'run lead (routine model) from crops at zoom 2.5–6','decisions':DEC},open('decisions.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(out),len(S1),len(S2),len(S3),'rubric',sum(1 for w in out if w.get('rubric')),'approx',sum(1 for w in out if w.get('approx')),'unsure',sum(1 for w in out if w.get('unsure')),'dec',len(DEC),Counter(d['decision'] for d in DEC))
