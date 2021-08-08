from coldtype import *
from fontTools.misc.transform import Transform
from coldtype.time.nle.premiere import PremiereTimeline
from coldtype.warping import warp_fn

json = Path("~/Desktop/brad-coldtype/sketches/media/arborJazz_coldtype.json").expanduser()
pt = PremiereTimeline(json)

mutator = Font("../assets/Fonts/MutatorSans.ttf")
vulfBlack = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BoldItalic.otf")
cheee = Font("../assets/Fonts/Cheee/CheeeDemo-BingBong.otf")
eck = Font("../assets/Fonts/Eckmannpsych/Eckmannpsych-Demo-Large.otf")
blimey = Font("../assets/Fonts/Blimey-V03/VARIABLE/Blimey-VO3-Variable.ttf")
digest = Font("../assets/Fonts/Digestive/DigestiveDemo-Small.otf")
swear = Font("../assets/Fonts/Swear Banner/SwearBannerDemo-Black.otf")
cheee2 = Font("../assets/Fonts/Cheee/CheeeDemo-Gnat.otf")

r = Rect(1080,1920)


@animation((1080,1920),  timeline=pt)
def arborJazz(f):
    lineLoops = []
    letterLoops = []
    y_motions = []
    for i in range(6):
        
        lineLoops.append(f.a.progress(f.i/2-2*i, loops=4, easefn="ceio"))
        if lineLoops[i].loop == 0:
            y_motions.append(lineLoops[i].e*1600)
        elif lineLoops[i].loop in [1,2]:
            y_motions.append(1*1600)
        elif lineLoops[i].loop == 3:
            y_motions.append((2-lineLoops[i].e)*1600)

    startPoint = -1500
    y_disp = 120

    textColor = 1
    grad = Gradient.Vertical(f.a.r, hsl(.99,1,.76), hsl(0.05, 1, 0.76))
    #hsl(.18,1,.93)



    text = (DPS(pens=[

    (StyledString("JAZZMANIA",Style(swear,150, tu = 40)).pens()
    .align(f.a.r)
    .offset_y(startPoint+40 + y_disp*2 + y_motions[0])
    .f(textColor)
    ),

    (StyledString("FEATURING",Style(cheee2,100, tu = 220)).pens()
    .align(f.a.r)
    .offset(0,startPoint+30 + y_disp + y_motions[1])
    .f(textColor)
    ),
    
    (StyledString("RICK VANDIVIER",Style(eck,150, tu = 0)).pens()
    .align(f.a.r)
    .offset(0,startPoint+15 + y_motions[2])
    .f(textColor)
    ),
    
    (StyledString("AND   FRIENDS",Style(cheee,84, tu=400)).pens()
    .align(f.a.r)
    .offset(0,startPoint-y_disp + y_motions[3])
    .f(textColor)
    ),

    (StyledString("LIVE AT THE ARBOR",Style(blimey,84, tu=260, wght=500)).pens()
    .align(f.a.r)
    .offset(0,startPoint-2*y_disp + y_motions[4])
    .f(textColor)
    ),

    (StyledString("FRIDAY 8PM",Style(digest,80, tu=430,)).pens()
    .align(f.a.r)
    .offset(0,startPoint-3*y_disp + y_motions[5])
    .f(textColor)
    ),

    ]
    )
    .pmap(lambda i, p: 
            (p.flatten(3)
                .nlt(warp_fn(f.i*2, f.i*2, mult=10))))
    )
    return(
        (DP(f.a.r).f(grad)),
        (text).scale(1,1.5).phototype(f.a.r,blur=2,cut=60,cutw=60,fill = hsl(.14,1,.86)),
    )