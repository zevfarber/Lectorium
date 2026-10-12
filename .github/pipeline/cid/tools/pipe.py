import pymupdf, numpy as np, json, re
from collections import Counter
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
R=json.load(open('rules.json'))
R2=json.load(open('rules2.json'))
BOT_OVERRIDE={235:1160}
def img(pn):
    p=d[pn-1]; pix=p.get_pixmap(colorspace=pymupdf.csGRAY)
    return np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width)<140
def segment(dark,y0,y1):
    sub=dark[y0:y1,60:1130]; on=sub.sum(1)>3
    res=[];y=0;n=len(on)
    while y<n:
        if on[y]:
            s=y
            while y<n and on[y]: y+=1
            res.append([s,y])
        else: y+=1
    m=[]
    for s,e in res:
        if m and s-m[-1][1]<=4: m[-1][1]=e
        else: m.append([s,e])
    m2=[]
    prof=sub.sum(1)
    for s_,e_ in m:
        h=e_-s_
        k=round((h+14)/46) if h>50 else 1
        if k<=1: m2.append([s_,e_]); continue
        cuts=[s_]
        for j in range(1,k):
            c=s_+round(j*h/k); lo,hi=c-10,c+10
            cc=min(range(lo,hi),key=lambda r:prof[r]); cuts.append(cc)
        cuts.append(e_)
        for a_,b_ in zip(cuts,cuts[1:]): m2.append([a_,b_])
    m=m2
    B=[]
    for s,e in m:
        blk=sub[s:e]; colsum=blk.sum(0); ink=int(blk.sum())
        if ink<60: continue
        core=np.where(colsum>=2)[0]
        if len(core)==0: continue
        runs=[]; st=core[0]; pr=core[0]
        for c in core[1:]:
            if c-pr>40: runs.append((int(st)+60,int(pr)+60)); st=c
            pr=c
        runs.append((int(st)+60,int(pr)+60))
        big=[r for r in runs if r[1]-r[0]>=10]
        if big: runs=big
        B.append({'y0':s+y0,'y1':e+y0,'h':e-s,'ink':ink,'runs':runs,'x0':runs[0][0],'x1':runs[-1][1]})
    return B
def process(pn):
    dark=img(pn); rl=R[str(pn)]
    top=rl[0][1]+6 if rl and rl[0][0]<300 else 225
    bot=None
    for r in rl:
        if r[0]>top+20: bot=r[0]-3; break
    B=segment(dark,top,bot or 1640)
    if bot is None:
        # footnote fallback: footer (Digitized by Google) removal and spacing-based note detection
        B=[b for b in B if b['y0']<1640]
        # find first index from which all following band pitches < 38 and h<=27, at least 2 bands
        while B and B[-1]['ink']<1000: B.pop()
        for i,b in enumerate(B):
            if b['h']<=18 and b['x1']-b['x0']>500: B=B[:i]; break
        cut=None
        for i in range(1,len(B)-1):
            tail=B[i:]
            if all((tail[j+1]['y0']-tail[j]['y0']<40) or tail[j]['h']>45 for j in range(len(tail)-1)):
                cut=i; break
        if cut: B=B[:cut]
        if pn in BOT_OVERRIDE: B=[b for b in B if b['y0']<BOT_OVERRIDE[pn]]
    xs=[b['x0'] for b in B if b['h']>=28 and b['ink']>2500]
    if not xs: return {'pn':pn,'le':None,'bands':[] ,'top':top,'bot':bot}
    cands=[l for (y,l,r) in R2.get(str(pn)) or [] if r-l>700]
    c=Counter(int(x)//8 for x in xs)
    if cands:
        best=None
        for x in sorted(set(xs)):
            pass
        # cluster centers: x values with count, choose cluster within 20 of a cand having most members
        scores=[]
        for cand in cands:
            mem=[x for x in xs if abs(x-cand)<=18]
            scores.append((len(mem),cand,mem))
        scores.sort(reverse=True)
        mem=scores[0][2]
        le=int(min(sorted(mem)[:max(1,len(mem)//4)][-1], np.median(mem))) if mem else scores[0][1]
    else:
        m=c.most_common(1)[0][0]*8
        near=[x for x in xs if m-12<=x<=m+20]
        le=int(np.percentile(near,25))
    out=[]
    for b in B:
        corew=sum(r[1]-r[0] for r in b['runs'])
        k='verse'
        if corew<130 and b['ink']<1800 and b['x0']>le+150 and b['h']>=18: k='tnum'
        elif out and out[-1]['k']=='tnum' and (b['h']<=29 or b['h']>=45) and not (b['x0']<le-14): k='rub'
        elif out and out[-1]['k']=='rub' and b['y0']-out[-1]['y1']<20: k='rub'
        elif b['ink']<300: k='speck'
        elif b['x0']>le+200 and b['ink']<3000: k='turn'
        elif b['x0']>le+90: k='center'
        if k in('center','turn') and out and out[-1]['k'] in ('tnum','rub') and b['y0']-out[-1]['y1']<60: k='rub'
        b['k']=k; b['lab']= (k=='verse' and b['x0']<le-14)
        out.append(b)
    # attach OCR words
    words=d[pn-1].get_text('words')
    for b in out:
        ws=[w for w in words if b['y0']-4 <= (w[1]+w[3])/2 <= b['y1']+4]
        ws.sort(key=lambda w:w[0])
        b['words']=[(round(w[0]),round(w[2]),w[4]) for w in ws]
    return {'pn':pn,'le':le,'bands':out,'top':top,'bot':bot}
if __name__=='__main__':
    P=[process(pn) for pn in range(127,363)]
    json.dump(P,open('P.json','w'),ensure_ascii=False)
    print(Counter(b['k'] for p in P for b in p['bands']))
    for p in P:
        for b in p['bands']:
            if b['k'] in ('center','turn'): print(p['pn'],b['k'],b['y0'],b['h'],b['x0'],b['ink'],' '.join(w[2] for w in b['words'])[:60])
