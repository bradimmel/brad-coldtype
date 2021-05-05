from coldtype import *
from coldtype.time.midi import MidiReader
import random as pyRandom
from coldtype.warping import warp_fn
from coldtype.time.nle.premiere import PremiereTimeline

mutator = Font("../assets/MutatorSans.ttf")
blimey = Font("../assets/Blimey-V03/VARIABLE/Blimey-VO3-Variable.ttf")
json = Path("~/Desktop/brad-coldtype/sketches/media/arborPlanets_coldtype.json").expanduser()
pt = PremiereTimeline(json)
drums = MidiReader("../media/Arbor/space drums.mid", duration=931, bpm=99, fps=30)[0]

rs1 = random_series(0, 1000, seed=10)

starPoints = []
starXs = random_series(0,1080, seed=2)
starYs = random_series(0,1920, seed=1)
starCount = 200
starSize = 5
for i in range(starCount):
    starPoints.append((starXs[i],starYs[i]))


 
@animation((1080,1920), timeline=pt)
def arborPlanets(f):
    loopNum = 4
    l = f.a.progress(f.i/4, loops=loopNum, easefn="ceio")
    l2 = f.a.progress((f.i-50)/4, loops = loopNum-1, easefn="seio")
    #loopLength = duration/(2*loopNum)

    kick = drums.fv(f.i, [24], [5, 20])
    snare = drums.fv(f.i, [25], [5, 20] )

    maiyaColor = hsl(0.1, 1, 1)
    bgColor = hsl(0.58, 1, .07)
    blimeyStyle = Style(blimey,
        100,
        r=1,
        ro=1,
        wght=100,
        tu = 250,
        )

    stars = DATPens()

    for i in range(starCount):
        starPointx = starPoints[i][0]
        starPointy = starPoints[i][1]
        starRect = Rect([starPointx, starPointy, starSize, starSize])
        stars.append(
            DATPen()
            .oval(starRect) 
            .f(1,1,1)     
            )

    # twinkle
    for i in range(len(stars)):

        occLoopsSeed = (i%4)
        starLoop = f.a.progress(f.i + (rs1[i]), loops=18, easefn="ceio")
        occLoops = [occLoopsSeed,occLoopsSeed+1]
        for k in range(10):     # dirtily cover everything
            occLoops.append(occLoopsSeed + k*2)
            occLoops.append(occLoopsSeed + k*2 + 1)
        if starLoop.loop in occLoops:
            stars[i].scale(1-(starLoop.e)/1.8)


    sunRad  =  100
    sun = (DATPen()
        .oval(f.a.r.inset(f.a.r.mxx/2-sunRad,f.a.r.mxy/2-sunRad))
        .f(1)
        #.translate(300,500)
        .translate(0,0)
        .phototype(f.a.r, cut=100, cutw=100, blur=2, fill=(hsl(.16,1,.8)))

    )

    orbit = DP().oval(Rect(500,500)).reverse().align(f.a.r).s(1).sw(.3).f(None)

    orbit01 = orbit.copy().scale(.9).skew(.4)
    orbit02 = orbit.copy().scale(1.4).skew(.5)
    orbit03 = orbit.copy().scale(1.8).skew(.6)
    
    orbit01.scale(1+snare.ease()/10)
    sun.scale(1+kick.ease()/15)

    if l.loop == 0:
        maiyaScale = l.e
        maiyaRotate = 360*l.e-150
    else:
        maiyaScale = 1
        maiyaRotate = -150

    if l2.loop == 0:
        shaScale = l2.e
        shaRotate = 360*l2.e-200
    else:
        shaScale = 1
        shaRotate = -200

    maiya = ((StyledString(
        "MAIYA & JAKE",
        blimeyStyle
        )
        .pens()
        .f(1)
        .align(f.a.r)
        .translate(-200,600)
        .explode()
        .scale(maiyaScale)
        .rotate(maiyaRotate+f.i/4)
        )
        )
    

    sha = ((StyledString(
        "Harry Sha",
        blimeyStyle
        )
        .pens()
        .f(1)
        .align(f.a.r)
        .translate(200,-500)
        .explode()
        .scale(shaScale)
        .rotate(shaRotate+f.i/4)
        )
        )

    # text worm
    for i in range(len(maiya)):
        wormLoop = f.a.progress(f.i-i*6, loops = 12, easefn="seio")
        if math.floor(wormLoop.loop/2) %4 == 2 and wormLoop.loop > 5:
            maiya[len(maiya)-1-i].translate(-30*wormLoop.e*math.sin((maiyaRotate+f.i/4)*2*math.pi/360),30*wormLoop.e*math.cos((maiyaRotate+f.i/4)*2*math.pi/360))
    for i in range(len(sha)):
        wormLoop = f.a.progress(f.i-i*6, loops = 12, easefn="seio")
        if math.floor(wormLoop.loop/2) %4 == 0 and wormLoop.loop > 10:
            sha[len(sha)-1-i].translate(-30*wormLoop.e*math.sin((shaRotate+f.i/4)*2*math.pi/360),30*wormLoop.e*math.cos((shaRotate+f.i/4)*2*math.pi/360))



    ufos = DPS()
    # start point, color vals, x/y speeds, rotate speed,
    ufoSpecs = [ 
        [[-500,-500], [.4,.8,.18,.8], [1, 0.5], [1/6]],
        [[-700,600], [.6,.8,.8,.7], [.8, -0.5], [1/4]],
        [[500,900], [.4,.8,.18,.8], [-0.5, -0.5], [1/8]],
        [[500,-300], [.6,.8,.8,.7], [-0.1, -0.5], [1/4]],
        [[100,200], [.7,.8,.4,.8], [-0.8, -0.5], [1/3]],
        [[-200,700], [.1,.8,.9,.8], [0.1, 0.2], [1/2]],

        [[-1000,-500], [.4,.8,.18,.8], [1, 0.5], [1/6]],
        [[-1400,300], [.6,.8,.8,.7], [1, 0.5], [1/4]],
        [[300,-600], [.4,.8,.18,.8], [-0.5, -0.5], [1/8]],
        [[-900,300], [.6,.8,.8,.7], [0.5, 0.2], [1/4]],
        [[-100,-800], [.7,.8,.4,.8], [-0.2, -0.1], [1/3]],
        [[1000,700], [.1,.8,.9,.8], [-0.1, 0.2], [1/2]],
        ]

    for i in range(len(ufoSpecs)):
        ufo = DPS()

        ufo += (DP().oval(Rect(50,50)).align(f.a.r).offset_y(15).f(hsl(ufoSpecs[i][1][0],1,ufoSpecs[i][1][1])))    
        ufo += (DP().oval(Rect(100,30)).align(f.a.r).f(hsl(ufoSpecs[i][1][2],1,ufoSpecs[i][1][3])))
        ufo.offset(ufoSpecs[i][0][0]+f.i*ufoSpecs[i][2][0], ufoSpecs[i][0][1]+f.i*ufoSpecs[i][2][1]).rotate(i*50 + f.i*ufoSpecs[i][3][0])
        ufos += ufo


    sky = (DATPen()
        .rect(f.a.r)
        .f(bgColor)
    )



    # looping text
    loopStart = 14
    if  l.loop in [loopStart, loopStart+1, loopStart+2, loopStart+3]:
        infoTracking = -60+l.e*100
        infoSize = .8
        midSpace = l.e*500
    else:
        infoTracking = -60
        midSpace = 0

    infoStyle = Style(mutator,
        40,
        r=1,
        ro=1,
        wdth=400,  
        wght=900,
        tu = infoTracking,
    )

    meteorSpeed = 1

    dateAndTime = (StyledString(
    "FRIDAY      EIGHT PM",  
    infoStyle)
    .pens()
    #.translate(0, -800)
    #.pmap(shift_counters)
    .f(hsl(.9,1,1))
    #.s(1).sw(7).f(None)
    .distributeOnPath(orbit01, offset = meteorSpeed*f.i)
    # .pmap(lambda i, p: 
    #         (p.flatten(3)
    #             .nlt(warp_fn(f.i*5, f.i*5, mult=20))))
    )



    LatA = (StyledString(
        "LIVE AT THE ARBOR",  
        infoStyle)
        .pens()
        #.translate(0, -800)
        #.pmap(shift_counters)
        .f(hsl(.9,1,1))
        #.s(1).sw(7).f(None)
        .distributeOnPath(orbit01.rotate(180), offset = meteorSpeed*f.i)
        # .pmap(lambda i, p: 
        #         (p.flatten(3)
        #             .nlt(warp_fn(f.i*5, f.i*5, mult=20))))
        )

    date = (StyledString("05.07.21",
        Style(blimey, 80, wght=500, wdth=0, tu=0, space=500))
        .pens()
        .offset(840,50)
        .f(hsl(1,1,1))
        .pmap(lambda i, p: 
            (p.flatten(3)
                .nlt(warp_fn(f.i*5, f.i*5, mult=10))))
        .phototype(f.a.r, blur=2, cut=100, cutw=20,  fill=(hsl(.16,1,.8)))
        
        # psych mode
        #.phototype(f.a.r, blur=2, cut=100, cutw=20,  fill=(hsl((100+f.i)/50,1,.7)))
        )

    # psych mode
    # for i in range(len(LatA)):
    #     LatA[i].rotate((f.i*5))
    # for i in range(len(dateAndTime)):
    #     dateAndTime[i].rotate((f.i*5))



    return (
        (sky),

        (stars),
        (sun),
        #(ufos),

        (maiya
        
        .phototype(f.a.r, cut=100, cutw=100, blur=1, fill=(hsl(.1,1,.7)))

        # psych mode
        #.phototype(f.a.r, cut=100, cutw=100, blur=1, fill=(hsl(f.i/50,1,.7)))
        ),

        (sha
        .phototype(f.a.r, cut=100, cutw=100, blur=1, fill=(hsl(.1,1,.7)))
        
        # psych mode
        #.phototype(f.a.r, cut=100, cutw=100, blur=1, fill=(hsl((210+f.i)/50,1,.7)))
        ),

        #(orbit01),
        #(orbit02),
        #(orbit03),
        

        (dateAndTime
        
        .phototype(f.a.r, cut=190, cutw=20, blur=3, fill=(hsl(.7,1,1)))
        
        ),

        (LatA
        
        .phototype(f.a.r, cut=190, cutw=20, blur=3, fill=(hsl(.7,1,1)))
        
        ),
        (date),

        

        

    )

def release(passes):
    FFMPEGExport(arborClouds, passes).gif().write()
