import pymupdf, numpy as np, json, sys
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
R=json.load(open('rules.json'))
def region(pn):
    rl=R[str(pn)]
    top=rl[0][1] if rl and rl[0][0]<300 else 230
    bot=None
    for r in rl:
        if r[0]>top+20: bot=r[0]; break
    if bot is None: bot=1640
    return top,bot
def bands(pn):
    p=d[pn-1]; pix=p.get_pixmap(colorspace=pymupdf.csGRAY)
    a=np.frombuffer(pix.samples,dtype=np.uint8).reshape(pix.height,pix.width)
    top,bot=region(pn)
    sub=a[top+6:bot-4, 60:1130]<140
    prof=sub.sum(1)
    on=prof>3
    res=[];y=0;n=len(on)
    while y<n:
        if on[y]:
            s=y
            while y<n and on[y]: y+=1
            e=y
            cols=np.where(sub[s:e].sum(0)>0)[0]
            res.append({'y0':s+top+6,'y1':e+top+6,'x0':int(cols[0])+60,'x1':int(cols[-1])+60,'ink':int(sub[s:e].sum())})
        else: y+=1
    # merge bands separated by tiny gaps (accents, descenders)
    m=[]
    for b in res:
        if m and b['y0']-m[-1]['y1']<=4:
            m[-1]['y1']=b['y1']; m[-1]['x0']=min(m[-1]['x0'],b['x0']); m[-1]['x1']=max(m[-1]['x1'],b['x1']); m[-1]['ink']+=b['ink']
        else: m.append(b)
    return [b for b in m if b['ink']>30]
if __name__=='__main__':
    for pn in map(int,sys.argv[1:]):
        print('== ',pn,region(pn))
        for b in bands(pn): print(b['y0'],b['y1'],b['y1']-b['y0'],b['x0'],b['x1'],b['ink'])
