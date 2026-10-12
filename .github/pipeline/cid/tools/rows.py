import pymupdf, json, sys
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
R=json.load(open('rules.json'))
def rows(pn):
    p=d[pn-1]; rl=R[str(pn)]
    top=rl[0][1] if rl and rl[0][0]<300 else 230
    bot=None
    for r in rl:
        if r[0]>top+20: bot=r[0]; break
    if bot is None: bot=1640
    words=p.get_text('words')
    ws=[w for w in words if (w[1]+w[3])/2>top and (w[1]+w[3])/2<bot]
    ws.sort(key=lambda w:(w[1]+w[3])/2)
    rs=[]
    for w in ws:
        yc=(w[1]+w[3])/2
        if rs and abs(yc-rs[-1]['yc'])<14:
            rs[-1]['w'].append(w); n=len(rs[-1]['w']); rs[-1]['yc']=(rs[-1]['yc']*(n-1)+yc)/n
        else: rs.append({'yc':yc,'w':[w]})
    out=[]
    for r in rs:
        r['w'].sort(key=lambda w:w[0])
        x0=r['w'][0][0]; h=max(w[3]-w[1] for w in r['w'])
        out.append({'y':round(r['yc']),'x0':round(x0),'x1':round(max(w[2] for w in r['w'])),'h':round(h),'words':[(round(w[0]),w[4]) for w in r['w']]})
    return out,top,bot
if __name__=='__main__':
    for pn in map(int,sys.argv[1:]):
        o,t,b=rows(pn); print('== page',pn,t,b)
        for r in o: print(r['y'],r['x0'],r['x1'],r['h'],' '.join(f"{w}" for x,w in r['words']))
