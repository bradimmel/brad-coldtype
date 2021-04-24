from coldtype import *
from fontTools.misc.transform import Transform
from coldtype.time.nle.premiere import PremiereTimeline
from coldtype.warping import warp_fn
from fontTools.svgLib import SVGPath

json = Path("~/Desktop/brad-coldtype/sketches/media/arborMountains_coldtype.json").expanduser()
pt = PremiereTimeline(json) #.retime_for_symbol("a")

mutator = Font("../assets/MutatorSans.ttf")
vulfBlack = Font("../assets/VulfMono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/VulfMono/VulfMonoDemo-BoldItalic.otf")
svg_path = Path("~/Desktop/brad-coldtype/assets/river01.svg").expanduser()
r = Rect(1080,1920)

@animation(r, solo=1,  timeline=pt)
def arborMountains(f):
    
    svgp = SVGPath.fromstring(svg_path.read_text(), transform=Transform())
    riverPath = DP()
    svgp.draw(riverPath)
    riverPath.s(0).sw(1).f(None).align(r).scale(1.8).offset_y(-600)

    riverStreams = DATPens()

    mountain = (DP()
        .polygon(3, Rect(1000,1000))
        .scale(1.3,1)
        )

    horizon = 500
    mountain01 = (mountain.copy()
        .offset(-200+f.i/8,horizon)
        .f(hsl(.1,.3,.5))
    )
    mountain02 = (mountain.copy()
        .offset(500-f.i/10,horizon)
        .f(hsl(.1,.3,.4))
    )

    moonRad = 200
    moon = (DATPen()
        .oval(f.a.r.inset(f.a.r.mxx/2-moonRad,f.a.r.mxy/2-moonRad))
        .f(hsl(.18,0,.85))
        #.translate(300,500)
        .translate(300,300)
    )
    sky = DATPen().rect(r).f(hsl(.7,1,.2))
    landscape = DATPen().rect(Rect(1080,800)).f(hsl(.35,.5,.7))

    letterTestPath = (StyledString("T", 
    Style(mutator, 1000, wght=80, wdth=200, tu=0, space=800))
    .pen()
    .align(r)
    )

    letterTest = (StyledString("."*10, 
    Style(vulfBold, 80, wdth=1, tu=100, space=500))
    .fit(letterTestPath.length())
    .pens()
    .distribute_on_path(letterTestPath, offset=10)
    .f(1)
    )





    def river(fntSize):
        thisRiver = ((StyledString("Friday 8PM",
        Style(vulfBold, fntSize, wght=800, wdth=200, tu=0, space=800))
        .pens()
        .f(hsl(.6,1,.7))
        
        # .pmap(lambda i, p: 
        # (p.flatten(2)
        #     .nlt(warp_fn(0, f.i*10, mult=10))))
        )) 
        return thisRiver

    # fntSize, offsetOnPath, speed, offset_x
    riverNums = [
        [30,600,1,0], 
        [20,550,1.5,-30], 
        [15,700,1.2,20]]
    for i in range(len(riverNums)):
        riverStreams += (
            (river(riverNums[i][0])
            .distribute_on_path(riverPath, offset=riverNums[i][1]+f.i*riverNums[i][2])
            .offset_x(riverNums[i][3] * (pt.end-f.i)/pt.end)    # converge/narrow
            
            )
        )
    
    return (
        (sky),
        (landscape),
        (moon),
        (mountain01),
        (mountain02),
        (riverStreams),
        (riverPath),
        (letterTestPath),
        (letterTest),

    )