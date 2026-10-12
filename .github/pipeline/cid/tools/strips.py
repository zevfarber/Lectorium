import pymupdf, json, sys
from PIL import Image, ImageDraw, ImageFont
d=pymupdf.open('/home/claude/lectorium/.github/pipeline/cid/source/raw/pidal1923_text.pdf')
P={p['pn']:p for p in json.load(open('P.json'))}
seq=json.load(open('prov.json'))
idx={(s['pn'],s['y']):s for s in seq}
try: font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',20)
except: font=ImageFont.load_default()
def strip(pn,W=270,scale=1.0):
    p=P[pn]; le=p['le'] or 200
    x0=le-110; x1=le+W-110
    top=p['top']-5; bot=(p['bot'] or 1640)
    pix=d[pn-1].get_pixmap(matrix=pymupdf.Matrix(scale,scale),clip=pymupdf.Rect(x0,top,x1,bot))
    im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    canvas=Image.new('RGB',(pix.width+150,pix.height+30),'white')
    canvas.paste(im,(0,30))
    dr=ImageDraw.Draw(canvas)
    dr.text((5,2),f'p{pn}',fill=(0,0,255),font=font)
    for b in p['bands']:
        yy=(b['y0']-top)*scale+30
        if b['k']=='verse':
            s=idx.get((pn,b['y0']))
            dr.text((pix.width+3,yy),f"{s['idx']}:{s['num']}",fill=(220,0,0),font=font)
        elif b['k']=='tnum':
            s=idx.get((pn,b['y0'])); dr.text((pix.width+3,yy),f"T{s['tir']}",fill=(0,150,0),font=font)
    return canvas
def sheet(pns,out):
    ims=[strip(pn) for pn in pns]
    W=sum(i.width for i in ims)+10*len(ims); H=max(i.height for i in ims)
    S=Image.new('RGB',(W,H),'white'); x=0
    for i in ims: S.paste(i,(x,0)); x+=i.width+10
    S.save(out)
if __name__=='__main__':
    pns=list(map(int,sys.argv[2:])); sheet(pns,sys.argv[1])
