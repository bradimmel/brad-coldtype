from coldtype import *
from coldtype.warping import warp_fn

cheee = Font("../assets/Fonts/Cheee/CheeeDemo-Pickles.otf")
eck = Font("../assets/Fonts/Eckmannpsych/Eckmannpsych-Demo-Large.otf")

@animation((1080,1920), duration=450)
def eisenachPoster01(f):
    l = f.a.progress(f.i/2, loops = 3, easefn="eeio")
    if l.loop == 0:
        forwardLoop = l.e
    else:
        forwardLoop = 1
    style = Style(cheee,
        240,
        tu=-10,
        ro=1,
        r=1,
        capHeight=600+forwardLoop*400,
        #kp={"T/Y":-25}
        )

    text = (Composer(f.a.r,
        "eisenach\nlive\nat\nthe\narbor\nfriday\n8PM",
        style,
        #leading=math.floor(10+kick.ease()*10)
        )
        .pens()
        #.reversePens()
        .align(f.a.r)
        .offset(forwardLoop*60,40)
        .f(1)
        .understroke(0,sw=20)
        .skew(-forwardLoop/8)
        .explode()
        )

    for i in range(len(text)):
        text[i].pmap(lambda i, p: 
            (p.flatten(3)
                .nlt(warp_fn(f.i*(1+i%3/2), f.i*(1+i%3/2), mult=15+(i%3/2))))
                .rotate(forwardLoop*360)
                )

        #text[i].f(hsl(1+(f.i+5*i)%10/100,.9,.85))


    return (
        (DP(Rect(f.a.r)).f(hsl(.6,1,.9))),
        (text
        .phototype(f.a.r, cut=130, cutw=8, blur=5, fill=(hsl(forwardLoop*.15, 1, .87)))
        ),
        )

def release(passes):
    FFMPEGExport(eisenachPoster01, passes).gif().write()