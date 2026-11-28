import json
J=lambda f: json.load(open(f))['words']
KEYS=('page','plate','chapter','line','signs','q','budge','gloss','rubric','restored','approx','unsure')
DEC=[]
def pick(w): return {k:w[k] for k in KEYS if k in w}
def dec(w, st, decision, why, **kw):
    for k,v in kw.items():
        if v is None: w.pop(k,None)
        else: w[k]=v
    w['approx']=[c for c in w.get('approx',[]) if c in w['signs']]
    if not w['approx']: w.pop('approx')
    w['unsure']=(w.get('unsure','')+' · ' if w.get('unsure') else '')+'Decision (%s): %s'%(decision,why)
    DEC.append(dict(stretch=st, page=w['page'], budge=w['budge'], decision=decision, why=why, signs=w['signs']))
def fromB(w,b):
    for k in ('signs','q','approx'):
        if k in b: w[k]=b[k]
        else: w.pop(k,None)
def stretch(a,b):
    A=[pick(w) for w in J(a)]; B=J(b); assert len(A)==len(B)
    for x,y in zip(A,B):
        for k in ('page','line','plate'): assert x[k]==y[k],(x['budge'],k)
        assert bool(x.get('rubric'))==bool(y.get('rubric'))
        if y.get('unsure') and y['unsure']!=x.get('unsure'): x['unsure']=(x.get('unsure','')+' · ' if x.get('unsure') else '')+'B: '+y['unsure']
        if 'q' not in x and y.get('q') and y['signs']==x['signs']: x['q']=y['q']
    return A,B
def at(A,i,budge):
    assert A[i]['budge'].replace(' ','')==budge.replace(' ',''), (A[i]['budge'],budge); return A[i]
def drop_q(w): w.pop('q',None)

# ---- stretch 1 (p. 135 row 7 - p. 136)
A,B=stretch('A1.json','B1.json')
dec(at(A,11,'sektet'),1,'A',"the boat stands on a base with a cabin and steering oars: P3 approx (boat-on-stand form, as in the other barques here)", approx=['P3'])
w=at(A,15,'āṭet'); w['signs']=['V26','X1','X1','D46','P3']; drop_q(w)
dec(w,1,'A/B',"under V26 X1 X1 the long rounded sign with a knob is the hand D46 (Budge ṭ; B), then the boat on a stand P3 approx (A's boat code)", approx=['V26','P3'])
for i in (18,54):
    dec(at(A,i,'Ani'),1,'A',"Ani kneels with one arm raised, no flail: A1 (zoom 3)")
dec(at(A,33,'ṭā - kuà'),1,'A',"kneeling man with arm raised, no flail: A1")
dec(at(A,37,'χu'),1,'A',"the kneeling figure holds a flail (the small triangle before him): A52")
w=at(A,41,'Ta-sertet'); fromB(w,B[41]); dec(w,1,'B',"two stacked columns: N16 over the low sledge-like sign (U15 approx), then X1 X1 over N25 approx; read column by column")
w=at(A,42,'seqṭeṭ - f'); w['signs']=['O34','Aa28','D46','D46','W24','P3','I9']; drop_q(w)
dec(w,1,'A/B',"after Aa28 two long rounded signs with a knob stacked at the left are hands D46 ×2 (Budge's two ṭ; B); W24 over the boat on a stand at the right, P3 approx (house boat code)", approx=[c for c in ('Aa28','P3') ])
dec(at(A,44,'Seχet - Àaru'),1,'A',"the small cone under X1 is the wedge N21 approx (house: small wedge N21)")
w=at(A,50,'āut'); fromB(w,B[50]); dec(w,1,'B',"under X1 a jar with side lugs: the heart F34 (Budge's 'joy of heart'), not the pot W24")
w=at(A,59,"t'ai - k"); dec(w,1,'A',"the boat on a stand: P3 approx (house boat code)")
w=at(A,60,'bàt'); fromB(w,B[60]); dec(w,1,'B',"X1 over the cup W10 approx over a flat bar with a small tuft: Aa13 approx (house), over Z2; no sky sign")
w=at(A,61,'sensen - k'); fromB(w,B[61]); dec(w,1,'B',"T22 T22 approx, then the flat bar with a small tuft Aa13 approx (house)")
dec(at(A,64,'àritu - nek'),1,'A',"two columns: D4 over D21, then X1 over the coil Z7; phonetic order ir-t-w")
dec(at(A,67,'uàa'),1,'A',"the boat with emblems on a stand: P3 approx (house boat code)")
dec(at(A,70,'āṭet'),1,'A',"the boat on a stand: P3 approx; no hand printed here")
w=at(A,71,'ṭekai - k'); fromB(w,B[71]); dec(w,1,'B',"the long rounded sign with a knob (hand D46) over the jar-stand with a Λ inside W11 approx; Budge prints ṭeḳai with a dot under t and k (zoom 6)", budge='ṭeḳai - k')
dec(at(A,74,'χennu'),1,'A',"the animal belly with legs and tail: F32 approx (Budge χ = ẖ), not the hide F27")
S1=A

# ---- stretch 2 (p. 137)
A,B=stretch('A2.json','B2.json')
dec(at(A,6,'àbṭu'),2,'A',"first sign the upright with a crossbar and flaring top: the Abydos fetish R17 approx (house ruling); the top sign of the pair is the long rounded hand D46 (Budge ṭ), the fish K1 approx")
w=at(A,9,'ṭutu'); w['signs']=['N26','X1','G43','D3']; drop_q(w)
dec(w,2,'A/B',"N26 approx over X1; the small bird with a stub tail is the quail chick G43 (B; Budge's u); then ONE sign, a row of five hanging looped strands, no good code: D3 approx (A), the same as in χeft", approx=['N26','D3'])
w=at(A,26,'qet'); fromB(w,B[26]); dec(w,2,'B',"the seated wrapped figure with a long wig, no arms shown, the same figure as in neb - s: A40 approx")
dec(at(A,34,'χeft'),2,'A',"the row of five hanging looped strands is one sign: D3 approx (as in ṭutu)")
w=at(A,36,'neb - s'); fromB(w,B[36]); dec(w,2,'B',"the seated wrapped figure with a long wig (no beard visible): A40 approx, as in qet; not the woman B1", approx=['A40'])
w=at(A,60,'χu'); fromB(w,B[60]); dec(w,2,'B',"the kneeling figure holds a flail (triangle): A52, as χu on p. 136")
S2=A

W=S1+S2
for w in W:
    if 'approx' in w:
        w['approx']=[c for c in w['approx'] if c in w['signs']]
        if not w['approx']: w.pop('approx')
json.dump(W,open('merged.json','w'),ensure_ascii=False,indent=1)
json.dump(DEC,open('decisions.json','w'),ensure_ascii=False,indent=1)
print(len(W),len(DEC))
