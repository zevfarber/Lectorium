import json,re,os,string
from number import labtext,parse
P=json.load(open('P.json'))
corr=json.load(open('corr.json'))
seq=[]; tir=1
for p in P:
    for b in p['bands']:
        if b['k']=='tnum': tir+=1; seq.append({'k':'T','pn':p['pn'],'y':b['y0'],'tir':tir})
        elif b['k']=='verse':
            lt=labtext(p,b) if b['lab'] else None
            seq.append({'k':'V','pn':p['pn'],'y':b['y0'],'lab':lt,'words':b['words'],'x0':b['x0'],'le':p['le'],'h':b['h']})
V=[s for s in seq if s['k']=='V']
for i,s in enumerate(V): s['idx']=i
def val(v):
    m=re.match(r'^(\d+)(?:-(\d+))?([a-z]?)$',v)
    a=m.group(1)
    if m.group(2): a=a[:len(a)-len(m.group(2))]+m.group(2)
    return int(a),m.group(3)
# pass 1: anchors
cur=0
for s in V:
    c=corr.get(str(s['idx']))
    s['anchor']=None; s['kind']=''
    if c in ('PROSE','I'): s['kind']=c; continue
    if c=='NL': continue
    if c: s['anchor']=c; cur=val(c)[0]; continue
    if s['lab'] is not None:
        n,suf=parse(s['lab']); e=cur+1
        snap=5*round(e/5)
        if n is not None and not suf and abs(n-e)<=3 and n%5==0: s['anchor']=str(n)
        elif not re.search(r'[0-9A-Za-z]',s['lab']):
            if e%5==0: s['anchor']=str(e)
            else: s['flag']='ignored-empty'; cur+=1; continue
        elif abs(snap-e)<=2: s['anchor']=str(snap); s['flag']='snapped'
        else: s['flag']='unreadable label'; continue
        cur=val(s['anchor'])[0]
    else: cur+=1
# pass 2: assign by intervals
anchors=[i for i,s in enumerate(V) if s['anchor']]
irregular=[]
def assign(lo,hi,a,b):
    # V[lo..hi-1] between anchor value a (tuple) and b (tuple or None)
    bands=[V[k] for k in range(lo,hi)]
    normal=[x for x in bands if x['kind']=='']
    start=a[0]
    if b is None: need=len(normal)
    else: need=b[0]-a[0]-1+(1 if b[1] else 0)
    if b is not None and b[0]<a[0]: need=len(normal)  # relocation backwards
    if b is not None and need<0: need=len(normal)
    n=start; extra_letter={}
    cnt=0; lastnum=a
    for x in bands:
        if x['kind']=='PROSE': x['num']='PROSE'; continue
        if x['kind']=='I':
            base=lastnum; L=extra_letter.get(base,1 if not base[1] else string.ascii_lowercase.index(base[1])+1)
            extra_letter[base]=L+1
            x['num']=f"{base[0]}{string.ascii_lowercase[L]}"; x['ital']=True; continue
        cnt+=1
        if cnt<=need or b is None or b[0]<=a[0]:
            n+=1; x['num']=str(n); lastnum=(n,'')
        else:
            base=(n,'') ; L=extra_letter.get(base,1); extra_letter[base]=L+1
            x['num']=f"{n}{string.ascii_lowercase[L]}"; x['over']=True
    if b is not None and b[0]>a[0]:
        if len(normal)!=need: irregular.append((V[lo-1]['idx'] if lo>0 else -1, a, b, len(normal), need))
prev=None; prevv=(0,'')
for ai in anchors+[len(V)]:
    lo=(prev+1) if prev is not None else 0
    b=val(V[ai]['anchor']) if ai<len(V) else None
    assign(lo,ai,prevv,b)
    if ai<len(V):
        V[ai]['num']=V[ai]['anchor']; prev=ai; prevv=val(V[ai]['anchor'])
json.dump(seq,open('prov.json','w'),ensure_ascii=False)
json.dump(irregular,open('irregular.json','w'))
if __name__=='__main__':
    print('irregular intervals',len(irregular))
    for r in irregular: print(r)
    print([ (s['idx'],s['pn'],s['lab']) for s in V if s.get('flag')=='unreadable label'])
