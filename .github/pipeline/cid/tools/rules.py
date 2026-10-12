import pymupdf, numpy as np, json
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
def rules(pn):
    p=d[pn-1]; pix=p.get_pixmap(colorspace=pymupdf.csGRAY)
    a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width)
    dark=(a<120)
    out=[]
    for y in range(a.shape[0]):
        row=dark[y]
        # longest run
        if row.sum()<400: continue
        r=np.diff(np.concatenate([[0],row.astype(int),[0]]))
        s=np.where(r==1)[0]; e=np.where(r==-1)[0]
        L=(e-s).max()
        if L>400: out.append((y,int(L),int(s[(e-s).argmax()])))
    # collapse
    res=[]
    for y,L,x in out:
        if res and y-res[-1][1]<=3: res[-1][1]=y; res[-1][2]=max(res[-1][2],L)
        else: res.append([y,y,L,x])
    return res
if __name__=='__main__':
    allr={}
    for pn in range(127,363):
        allr[pn]=rules(pn); 
    json.dump(allr,open('rules.json','w'))
    for pn in range(127,140): print(pn,allr[pn])
