import json, re
from collections import Counter
J=lambda f: json.load(open(f))['words']
KEYS=('page','plate','chapter','line','signs','q','budge','gloss','rubric','restored','approx','unsure')
DEC=[]; DIFF=[]
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
        for k in ('page','line','plate'):
            if x[k]!=y[k]: DIFF.append((a,x['budge'],k,x[k],y[k]))
        if bool(x.get('rubric'))!=bool(y.get('rubric')) or bool(x.get('restored'))!=bool(y.get('restored')): DIFF.append((a,x['budge'],'flags'))
        if y.get('unsure') and y['unsure']!=x.get('unsure'): x['unsure']=(x.get('unsure','')+' · ' if x.get('unsure') else '')+'B: '+y['unsure']
        if 'q' not in x and y.get('q') and y['signs']==x['signs']: x['q']=y['q']
    return A,B
def at(A,i,budge):
    assert A[i]['budge'].replace(' ','')==budge.replace(' ',''), (A[i]['budge'],budge); return A[i]

# ---- stretch 1 (p. 131 row 9 - p. 132)
A,B=stretch('A1.json','B1.json')
dec(at(A,0,'à'),1,'A',"standing man with one arm raised forward, the other down: A26 approx")
dec(at(A,5,'ḥetep'),1,'A',"only the loaf on a mat R4 is printed (zoom 5); no X1 Q3 under it")
for i in (23,66,69):
    w=at(A,i,A[i]['budge']); dec(w,1,'B',"Budge prints mā with a macron", budge=B[i]['budge'])
w=at(A,30,'màśeru'); fromB(w,B[30]); dec(w,1,'B',"the same sign as in māśeru p. 134 (three of four readers P1 approx): a flat boat-like body with a post at its right end, a stick across it and a curved stroke under it, no separate legs; no good code; Budge prints māśeru", budge='māśeru', approx=['P1','N2'])
dec(at(A,31,'hru'),1,'A',"Budge prints hru with no dot (zoom 3)")
dec(at(A,32,'reṭiu'),1,'A',"under D21 the flat hand D46 (Budge ṭ); the looped cord after the bird is the bowstring T12 approx (rwḏ), not F51")
dec(at(A,44,'àmmu - k'),1,'A',"the flat bar after the reed is the im-sign Aa13 approx (Budge àm), not the arm D36")
w=at(A,48,'maa - entu'); fromB(w,B[48]); dec(w,1,'B',"house order: eye D4 first, sickle U1 second")
w=at(A,51,'set'); fromB(w,B[51]); dec(w,1,'B',"three stacked bands with hill-shaped tops, each N25 approx; no water")
dec(at(A,55,'sàp - tu'),1,'A',"the lying loop with crossed ends: the cord V6 approx (F51 possible)")
dec(at(A,67,'màtet'),1,'A',"last sign the flat bar with a small tuft: Aa13 approx (house)")
S1=A

# ---- stretch 2 (p. 133 - p. 134 top)
A,B=stretch('A2.json','B2.json')
w=at(A,1,'àri - nef'); dec(w,2,'B',"Budge spaces the hyphen: àri - nef", budge='àri - nef')
dec(at(A,5,'hru'),2,'A',"Budge prints hru with no dot (zoom 2.5)")
w=at(A,8,'uau - θà'); fromB(w,B[8]); dec(w,2,'B',"the θ sign is a crossbar with a knob or loop at each end and a pendant (balance-like, U38 approx; no good code) over D54; the narrow rounded upright after it U33 approx, then one reed")
for i in (18,24):
    w=at(A,i,'qam - nek'); fromB(w,B[i]); dec(w,2,'B',"first sign the flat block with spines at its sloping left end: the crocodile-skin sign I6 approx (km)")
dec(at(A,19,'unnut'),2,'A',"phonetic order E34 N35 W24 X1 N14 N5 (W24 and the star stand over N35 and X1)")
w=at(A,21,'màtet'); fromB(w,B[21]); dec(w,2,'B',"last sign the flat bar with a small tuft: Aa13 approx (house)")
dec(at(A,22,'mesmes - nek'),2,'A',"two stacked groups, each a long open rectangle with a slanted left end (N36 approx; no good code) over the bolt O34: read N36 O34 N36 O34")
w=at(A,26,'entā - k'); fromB(w,B[26]); dec(w,2,'B',"the low flat sign with an upright tab U15 (house, even where Budge reads ā); the bar with a tuft Aa13 approx")
dec(at(A,27,"ḥet' - ta"),2,'A',"the mace and cobra printed as one ligature: T3 I10 approx (Budge ḥet' needs the ḏ)")
for i,b in ((30,'rā - k'),(32,'Rā'),(53,'χāā - k'),(55,'seāāa'),(59,'ḥāu - k'),(64,'Rā'),(84,'ḥenā - sen')):
    w=at(A,i,b); keep=w['signs']
    fromB(w,B[i]); dec(w,2,'B',"the low flat sign with an upright tab U15 (house, even where Budge reads ā)")
w=at(A,60,'messu'); fromB(w,B[60]); dec(w,2,'B',"third sign a tall stem with a tuft at its foot: the sedge M23 approx (sw)")
w=at(A,75,'ḥesiu'); fromB(w,B[75]); dec(w,2,'B',"the bolt O34 stands over the two reeds (O34 first); the partly hidden figure coded A1 (A2 possible)")
S2=A

# ---- stretch 3 (Plate XXI, pp. 134-135)
A,B=stretch('A3.json','B3.json')
w=at(A,4,'Nut'); fromB(w,B[4]); dec(w,3,'B',"the type prints the crossed circle O49, not the pot W24: code what is printed")
dec(at(A,7,'unemi'),3,'A',"first sign the flower on a stem M42 approx (Budge un); R14 (west) possible in shape")
for i,b in ((10,'àau'),(19,'ṭua - tu'),(36,'àau - nek')):
    w=at(A,i,b); fromB(w,B[i]); dec(w,3,'B',"the figure raises both arms upward: A28 approx (as in stretch 2), not A30")
w=at(A,27,'àt'); fromB(w,B[27]); dec(w,3,'B',"first sign the flat bar with a raised bump: Aa13 approx (no exact code)")
w=at(A,28,'beḳai'); fromB(w,B[28]); dec(w,3,'B',"the trapezoid for Budge's ḳ: W11 approx (house)")
for i in (40,50,53):
    w=at(A,i,A[i]['budge']); fromB(w,B[i]); dec(w,3,'B',"the upright with a knob head is the mace T3 (ḥḏ), before the cobra I10")
dec(at(A,63,"t'at'at"),3,'A',"only a bar with three ticks over X1 and strokes is printed: Aa8 approx (not the house t'at'at group)")
dec(at(A,72,'uθesu'),3,'A',"the post with a hooked top and slanting foot: the support U39 approx (wṯs)")
dec(at(A,75,'ḥu'),3,'A',"lower sign the flat bar with a small tuft: Aa13 approx (as in màtet)")
S3=A

out=S1+S2+S3
for w in out:
    w['chapter']='XV'
    if w.get('q'):
        idx=sorted(int(x) for x in re.findall(r'\d+',w['q']))
        if idx!=list(range(len(w['signs']))): w.pop('q')
json.dump(out,open('merged.json','w'),ensure_ascii=False,indent=1)
json.dump({'decider':'run lead (routine model) from crops at zoom 2.5–5','decisions':DEC},open('decisions.json','w'),ensure_ascii=False,indent=1)
print(len(out),len(S1),len(S2),len(S3),'rubric',sum(1 for w in out if w.get('rubric')),'restored',sum(1 for w in out if w.get('restored')),'approx',sum(1 for w in out if w.get('approx')),'unsure',sum(1 for w in out if w.get('unsure')),'dec',len(DEC),Counter(d['decision'] for d in DEC))
print('DIFF',DIFF)
print([ (w['budge'],w['signs']) for w in out if '?' in w['signs']])
# afterwards (run lead): grouping parentheses in q removed (the pin check does not take them); a q whose order
# was reversed by the parentheses (maa, p. 134) was dropped.
