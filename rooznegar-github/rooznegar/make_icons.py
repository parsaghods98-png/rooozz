import os, math
from PIL import Image, ImageDraw
for d in ('www','assets'): os.makedirs(d, exist_ok=True)
S=2048
def bg(n):
    im=Image.new('RGB',(n,n)); px=im.load()
    for y in range(n):
        for x in range(n):
            t=(x*.4+y*.6)/n
            a,b,u=((67,56,202),(124,58,237),t/.55) if t<.55 else ((124,58,237),(219,39,119),(t-.55)/.45)
            px[x,y]=tuple(int(a[i]+(b[i]-a[i])*u) for i in range(3))
    return im
def glyph(n):
    im=Image.new('RGBA',(n,n),(0,0,0,0)); d=ImageDraw.Draw(im); w=(255,255,255,255); c=n/2
    for k in range(12):
        a=math.radians(k*30)
        d.line([(c+n*.31*math.cos(a),c+n*.31*math.sin(a)),(c+n*.38*math.cos(a),c+n*.38*math.sin(a))],fill=(255,255,255,200),width=int(n*.022))
    d.ellipse([c-n*.25,c-n*.25,c+n*.25,c+n*.25],outline=w,width=int(n*.045))
    d.line([(n*.4,n*.51),(n*.47,n*.59),(n*.62,n*.4)],fill=w,width=int(n*.06),joint='curve')
    for p in [(n*.4,n*.51),(n*.62,n*.4)]:
        r=n*.03; d.ellipse([p[0]-r,p[1]-r,p[0]+r,p[1]+r],fill=w)
    return im
b=bg(S); g=glyph(S)
full=b.convert('RGBA'); full.alpha_composite(g)
full.resize((1024,1024),Image.LANCZOS).convert('RGB').save('assets/icon-only.png')
b.resize((1024,1024),Image.LANCZOS).save('assets/icon-background.png')
fg=Image.new('RGBA',(1024,1024),(0,0,0,0)); sm=g.resize((676,676),Image.LANCZOS); fg.paste(sm,(174,174),sm); fg.save('assets/icon-foreground.png')
for n in (192,512): full.resize((n,n),Image.LANCZOS).convert('RGB').save('www/icon-%d.png'%n)
