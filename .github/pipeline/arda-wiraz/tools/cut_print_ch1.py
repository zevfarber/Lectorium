# Cuts Haug's printed Pahlavi for chapter 1 into word images, one list per unit.
# Needs the page images n104..n109 (archive.org .../page/nNNN_w1500.jpg) and blocks_all.json /
# blocks104.json (line + word-shape boxes found from white space) in the working folder given as argv[1].
# NUM = where the print's sentence numbers sit (line, shape counted from the right); DROP = rings and ornaments.
from PIL import Image
import numpy as np, json, os, sys
from scipy import ndimage
SRC=sys.argv[1]; HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT=os.path.abspath(os.path.join(HERE,'..','..','..'))
ALL=json.load(open(os.path.join(SRC,'blocks_all.json'))); ALL={int(k):v for k,v in ALL.items()}
NUM={104:{(0,0):1,(1,5):2,(2,8):3,(4,0):4,(5,11):5,(6,3):6},
     105:{(0,0):7,(2,4):8,(4,6):9,(6,5):10,(7,9):11,(9,0):12},
     106:{(0,4):13,(1,4):14,(2,0):15,(3,8):16,(5,10):17,(7,0):18,(8,0):19,(8,10):20},
     107:{(0,9):21,(1,5):22,(2,4):23,(2,9):24,(3,7):25,(4,6):26,(6,5):27,(8,0):28},
     108:{(0,8):29,(2,1):30,(3,0):31,(3,8):32,(5,0):33,(5,9):34,(6,9):35,(7,4):36,(8,4):37,(8,12):38},
     109:{(0,7):39,(1,4):40,(2,7):41,(3,5):42,(4,2):43}}
DROP={104:{(2,7),(6,12)},105:{(4,5),(6,4),(8,4)},106:{(0,3),(3,7),(5,9),(7,11)},107:{(0,8),(7,3)},108:{(0,7),(4,11),(7,3)},109:{(3,4),(5,10)}}
LAST={104:6,105:9,106:8,107:8,108:8,109:5}
starts=[1,2,3,5,7,8,9,10,12,13,15,16,17,18,19,21,22,24,25,27,28,29,30,31,33,34,36,38,40,42]
def unit_of(s): return max(i for i,st in enumerate(starts) if st<=s)+1
seq={}; cur=None; seen=[]
for n in range(104,110):
    for li,L in enumerate(ALL[n]['lines'][:LAST[n]+1]):
        for j,b in enumerate(L['blocks']):
            if (li,j) in NUM[n]: cur=NUM[n][(li,j)]; seen.append(cur); continue
            if (li,j) in DROP[n]: continue
            seq.setdefault(unit_of(cur),[]).append((n,L['base'],b))
assert seen==list(range(1,44)),seen
B=json.load(open(os.path.join(SRC,'blocks104.json'))); tb=list(reversed(B['lines'][0]['blocks']))[:3]
seq[0]=[(104,838,b) for b in tb]
out=os.path.join(ROOT,'img','arda-wiraz','001'); os.makedirs(out,exist_ok=True)
for f in os.listdir(out): os.remove(os.path.join(out,f))
pages={n:np.array(Image.open(os.path.join(SRC,f'n{n}.jpg')).convert('L')).astype(float) for n in range(104,110)}
res={}; tot=0
for u in range(31):
    files=[]
    for (n,base,b) in seq[u]:
        a=pages[n]; x0=ALL[n]['x0']; top,bot=base-74,base+54
        c=a[top:bot, x0+b[0]-4:x0+b[1]+5]
        alpha=np.clip((165-c)/85,0,1); alpha[alpha<0.25]=0
        lab,k=ndimage.label(alpha>0)
        for q in range(1,k+1):
            m=lab==q; ys=np.where(m)[0]
            if (ys.min()==0 or ys.max()==alpha.shape[0]-1) and (ys.max()-ys.min())<34: alpha[m]=0
            elif m.sum()<6: alpha[m]=0
        if alpha.sum()<20: continue
        rgba=np.zeros(c.shape+(4,),'uint8'); rgba[...,3]=(alpha*255).astype('uint8'); rgba[...,:3]=30
        img=Image.fromarray(rgba,'RGBA'); img=img.resize((max(1,img.size[0]*2//3),img.size[1]*2//3),Image.LANCZOS)
        arr=np.array(img); arr[...,3]=(np.round(arr[...,3]/255*7)/7*255).astype('uint8'); arr[...,:3]=30
        fn=f'u{u:02d}-{len(files):02d}.png'; Image.fromarray(arr,'RGBA').save(os.path.join(out,fn),optimize=True)
        tot+=os.path.getsize(os.path.join(out,fn)); files.append({'f':fn,'w':arr.shape[1],'h':arr.shape[0]})
    res[u]=files
json.dump(res,open(os.path.join(HERE,'print-sample.json'),'w'),indent=0)
print('files',sum(len(v) for v in res.values()),'bytes',tot)
