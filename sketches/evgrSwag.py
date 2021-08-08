from coldtype import *
from coldtype.warping import warp_fn

mutator = Font("../assets/MutatorSans.ttf")
secu = Font("../assets/Secuela-Italic-v_1_787-TTF-VF.ttf")
blimey = Font("../assets/Blimey-V03/VARIABLE/Blimey-VO3-Variable.ttf")
tl = Timeline(800)

@renderable()
def evgr(r):
    EVGRmain = (StyledString("EVGR", 
    Style(secu, 300, wght=800, wdth = 500, tu=300, ))#kp={"V/G":-80}))
    .pens()
    .align(r)
    .f(hsl(1,1,1))
    )

    EVGRthin = (StyledString("EVGR", 
    Style(secu, 300, wght=600, wdth = 500, tu=320, ))#kp={"V/G":-80}))
    .pens()
    .align(r)
    .offset(0,0)
    .f(hsl(1,1,1))
    )

    zebra = DP()
    for c in r.subdivide_with_leading(50, 35, "mxy"):
        zebra += DATPen().rect(c).f(1,1,1)
    zebra.pmap(lambda i, p: 
        (p.flatten(2)
            .nlt(warp_fn(0, 0, mult=120))))



    EVGRtilt = (StyledString("EVGR", 
    Style(mutator, 300, wght=500, wdth = 500, tu=-150, kp={"V/G":-80}))
    .pen()
    .align(r)
    .offset(25,-30)
    #.skew(.2)
    .f(None)
    .s(0).sw(10)
    )


    return(
        (DP(Rect(r)).f(hsl(.07,.28,.77))),
        # (EVGRmain
        # .implode()
        # .xor(EVGRmain.copy().offset(-15,15))
        # .phototype(r, blur=2, cut=100, cutw=20,  fill=(hsl(1,1,1)))
        # ),
        (zebra
        .implode().reverseDifference(EVGRmain).f(1)
        #.xor(EVGRthin)
        .phototype(r, blur=0, cut=140, cutw=50,  fill=(hsl(1,1,1)))
        ),
        (EVGRmain
        .f(None))
        
    )
