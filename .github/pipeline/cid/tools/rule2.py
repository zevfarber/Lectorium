import pymupdf,numpy as np,json
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
R=json.load(open('rules.json'))
out={}
for pn in range(127,363):
    rl=R[str(pn)]
    if not rl: out[pn]=None; continue
    p=d[pn-1]; pix=p.get_pixmap(colorspace=pymupdf.csGRAY)
    a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width)<140
    res=[]
    for r in rl:
        blk=a[r[0]:r[1]+1].any(0)
        xs=np.where(blk)[0]
        # longest run with gaps<=6
        runs=[];cs=xs[0];pr=xs[0]
        for x in xs[1:]:
            if x-pr>6: runs.append((cs,pr)); cs=x
            pr=x
        runs.append((cs,pr))
        L=max(runs,key=lambda t:t[1]-t[0])
        res.append((r[0],int(L[0]),int(L[1])))
    out[pn]=res
json.dump(out,open('rules2.json','w'))
P={p['pn']:p for p in json.load(open('P.json'))}
for pn in range(127,363,7): print(pn,P[pn]['le'],out[pn])
