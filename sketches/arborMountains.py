from coldtype import *
from fontTools.misc.transform import Transform
from coldtype.time.nle.premiere import PremiereTimeline
from coldtype.warping import warp_fn
from fontTools.svgLib import SVGPath
import random as pyRandom

json = Path("~/Desktop/brad-coldtype/sketches/media/arborMountains_coldtype.json").expanduser()
pt = PremiereTimeline(json) #.retime_for_symbol("a")

mutator = Font("../assets/Fonts/MutatorSans.ttf")
vulfBlack = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BoldItalic.otf")
svg_path = Path("~/Desktop/brad-coldtype/assets/river01.svg").expanduser()
r = Rect(1080,1920)

rs1 = random_series(0, 100)

starPoints = []
starCount = 200
starSize = 3
for i in range(starCount):
    starPoints.append((pyRandom.randint(0,1080-starSize),(pyRandom.randint(1000,1920-starSize))))


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
        .offset(-200+f.i/6,horizon)
        .f(hsl(.1,.3,.5))
    )
    mountain02 = (mountain.copy()
        .offset(500-f.i/8,horizon)
        .f(hsl(.1,.3,.4))
    )

    # stars
    
    # stars = DATPens()

    # for i in range(starCount):
    #     starPointx = starPoints[i][0]
    #     starPointy = starPoints[i][1]
    #     starRect = Rect([starPointx, starPointy, starSize, starSize])
    #     stars.append(
    #         DATPen()
    #         .rect(starRect) 
    #         .f(1,1,1)     
    #         )

    # twinkle

    # for i in range(len(stars)):

    #     occLoopsSeed = (i%4)*2
    #     starLoop = f.a.progress(f.i - (rs1[i]), loops=18, easefn="ceio")
    #     occLoops = [occLoopsSeed,occLoopsSeed+1]
    #     for k in range(10):     # dirtily cover everything
    #         occLoops.append(math.floor(occLoopsSeed) + k*2)
    #         occLoops.append(math.floor(occLoopsSeed) + k*2 + 1)
    #     if starLoop.loop in occLoops:
    #         stars[i].scale(1-(starLoop.e)/1.8)


    # constellations
    rickPath = (StyledString("Rick", 
    Style(vulfBold, 140, wght=80, wdth=200, tu=0, space=800))
    .pen()
    .align(r)
    )

    vandivierPath = (StyledString("Vandivier", 
    Style(vulfBold, 140, wght=80, wdth=200, tu=0, space=800))
    .pen()
    .align(r)
    )

    
    rickStars = (StyledString("."*150, 
    Style(vulfBold, 15, wdth=0, tu=400, space=500))
    #.fit(rickPath.length())
    .pens()
    .distribute_on_path(rickPath, offset=10)
    .f(1)
    .offset(-280-f.i/8,700 - f.i/40)
    .rotate(10)
    )

    vandivierStars = (StyledString("."*350, 
    Style(vulfBold, 15, wdth=1, tu=400, space=500))
    #.fit(starWordPath.length())
    .pens()
    .distribute_on_path(vandivierPath, offset=10)
    .f(1)
    .offset(25+f.i/8,590+f.i/40)
    .rotate(10)
    )

    wordStars = DPS(pens=[rickStars, vandivierStars])

    # twinkle
    for i in range(len(wordStars)):
        for j in range(len(wordStars[i])):
            #wordStars[i].scale(min(1, (f.i-rs1[i])/30))
            occLoopsSeed = (i%4)*2
            starLoop = f.a.progress(f.i - rs1[j], loops=18, easefn="ceio")
            occLoops = [occLoopsSeed,occLoopsSeed+1]
            for k in range(10):     # dirtily cover everything
                occLoops.append(math.floor(occLoopsSeed) + k*2)
                occLoops.append(math.floor(occLoopsSeed) + k*2 + 1)
            if starLoop.loop in occLoops:
                wordStars[i][j].scale(1-(starLoop.e)/3.8)




    # moon

    moonRad = 200
    moon = (DATPen()
        .oval(f.a.r.inset(f.a.r.mxx/2-moonRad,f.a.r.mxy/2-moonRad))
        .f(hsl(.18,0,.85))
        #.translate(300,500)
        .translate(300,300)
    )
    sky = DATPen().rect(r).f(hsl(.7,1,.2))
    landscape = DATPen().rect(Rect(1080,800)).f(hsl(.35,.5,.7))

    moonTextRadOffset = 18
    moonCirc = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-moonRad - moonTextRadOffset,f.a.r.mxy/2-moonRad - moonTextRadOffset)).translate(300,300).reverse()

    moonText = (StyledString("and friends",
        Style(vulfBold, 30, wght=800, wdth=0, tu=0, space=500))
        .fit(moonCirc.length())
        .pens()
        .f(hsl(1,1,1))
        #.distribute_on_path(moonCirc, offset= -1000 + sunProgress * 2)
        .distribute_on_path(moonCirc, offset= f.i*3 - 160)
        #.phototype(f.a.r, blur=2, cut=100, cutw=20,  fill=(hsl(1,1,1)))
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
    # riverNums = [
    #     [30,600,1,0], 
    #     [20,550,1.5,-30], 
    #     [15,700,1.2,20]]
    # for i in range(len(riverNums)):
    #     riverStreams += (
    #         (river(riverNums[i][0])
    #         .distribute_on_path(riverPath, offset=riverNums[i][1]+f.i*riverNums[i][2])
    #         .offset_x(riverNums[i][3] * (pt.end-f.i)/pt.end)    # converge/narrow
            
    #         )
    #     )


    LatA = (Composer(f.a.r, "LIVE   AT \nTHE ARBOR", style = Style(vulfBlack, 150))
        .pens()
        .align(f.a.r)
        #.understroke(s=hsl(1, 1, 1), sw=10)
        .scale(.6,1.5)
        .skew(-.2)
        .rotate(5)
        .offset(0,-600)
        .pmap(lambda i, p: 
            (p.flatten(3)
                .nlt(warp_fn(100, 5, mult=80))))
        .pmap(lambda i, p: 
            (p.flatten(3)
                .nlt(warp_fn(f.i*10, f.i*10, mult=10))))
                )
    
    return (
        (sky),
        (landscape),
        #(stars),
        (wordStars),
        (moon),
        (moonText),
        (mountain01),
        (mountain02),
        #(riverStreams),
        #(riverPath),
        #(letterTestPath),
        (LatA),


    )