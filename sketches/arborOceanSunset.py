from coldtype import *
from coldtype.warping import warp_fn
import random as pyRandom

mutator = Font("../assets/MutatorSans.ttf")
vulfBlack = Font("../assets/VulfMono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/VulfMono/VulfMonoDemo-BoldItalic.otf")
tl = Timeline(800)

r = Rect(1080,1920)
a = DP().rect(r.inset(-100, 850)).offset_y(-250).flatten(10).roughen(350, seed=3)
b = DP().rect(r.inset(-100, 850)).offset_y(-250).flatten(10).roughen(350, seed=1)

rs1 = random_series(0, 100)
sunProgress = 0

starPoints = []
starCount = 100
starSize = 5
for i in range(starCount):
    starPoints.append((pyRandom.randint(0,1080-starSize),(pyRandom.randint(1000,1920-starSize))))

@animation((r), solo=1,  timeline=tl)
def arborOcean(f):
    sunLoop = f.a.progress(f.i/2, loops=16, easefn="qeio")
    global sunProgress
    tideLoop = f.a.progress(f.i/2, loops=6, easefn="ceio")
    # manual reset for render
    if f.i == 0:
        sunProgress = 0
    circleRad = 350
    circle = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-circleRad))
    squiggle = (DATPen().sine(f.a.r.inset(-400,f.a.r.mxy/2-30), 5)).offset_x(-350)
    squiggle2 = (DATPen().sine(f.a.r.inset(-200,f.a.r.mxy/2-30), 3))
    
    CB = (StyledString("Claire Brooks",
        Style(vulfBold, 90, wght=800, wdth=200, tu=0, space=800))
        .pens()
        .f(hsl(1,1,1))
        .distribute_on_path(squiggle, offset=-2.6*f.i+1900)
        .offset(0,600)
        
        .pmap(lambda i, p: 
        (p.flatten(2)
            .nlt(warp_fn(0, f.i*10, mult=10))))
        )

    CBShadow = CB.copy().offset(-4,-6).f(hsl(1,1,1))

    # LIVE AT THE ARBOR
    LatAStyle = Style(vulfBlack, 80, wght=800, wdth=200, tu=400, space=800)
    LatAColor = hsl(.08,1,.75)

    LatA = DATPens()

    LatA += (Composer(f.a.r, "LIVE", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(-350,-660)
    .rotate(10)
    .f(LatAColor)
    )

    LatA += (Composer(f.a.r, "AT", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(100,-660)
    .rotate(-2)
    .f(LatAColor)
    )

    LatA += (Composer(f.a.r, "THE", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(-140,-830)
    .rotate(1)
    .f(LatAColor)
    )

    LatA += (Composer(f.a.r, "ARBOR", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(280,-850)
    .rotate(6)
    .f(LatAColor)
    )

    LatA.offset_y(40)


    for i in range(len(LatA)):
        for j in range(len(LatA[i][0])):
            if j % 2 == 0:
                LatA[i][0][j].offset_y(10)
            else:
                LatA[i][0][j].offset_y(-10)
            
            # j+i stuff is a little silly but gets me good random movement stuff!
            occLoopsSeed = (i+j)*2
            sandTxtLoop = f.a.progress(f.i - (i*10+j*5), loops=32, easefn="ceio")
            LatA[i][0][j].rotate(+rs1[j+i]/10)
            occLoops = [occLoopsSeed,occLoopsSeed+1]
            for k in range(100):     # 100 just to dirtily cover everything
                occLoops.append(occLoopsSeed + k*6)
                occLoops.append(occLoopsSeed + k*6 + 1)
            if sandTxtLoop.loop in occLoops:
                LatA[i][0][j].rotate(sandTxtLoop.e*20)

    # sunset mechanics
    sunsetStart = 200
    sunsetEnd = 400
    skyColor = hsl(0.9, 1, 0.88)
    sunColor = hsl(0.12, 1, 0.8)
    sunY = 80
    oceanColorTop = hsl(0.6 , 1, 0.7)
    oceanColorBottom = hsl(0.53, 1, 0.85)

    if f.i > sunsetStart:
        skyColor = hsl(0.9-(f.i-sunsetStart)/1000, 1, 0.88-(f.i-sunsetStart)/300)
        sunColor = hsl(0.12-(f.i-sunsetStart)/1400, 1, 0.8-(f.i-sunsetStart)/1400)
        sunY = 80-(f.i-sunsetStart)*1.5
        oceanColorTop = hsl(0.6+(f.i-sunsetStart)/1400, 1, 0.7-(f.i-sunsetStart)/900)
        oceanColorBottom = hsl(0.53+(f.i-sunsetStart)/1400, 1, 0.85-(f.i-sunsetStart)/1400)
    if sunsetEnd < f.i < 800:
        skyColor = hsl(0.9-(sunsetEnd-sunsetStart)/1000, 1, 0.88-(sunsetEnd-sunsetStart)/300)
        sunColor = hsl(0.12-(sunsetEnd-sunsetStart)/1400, 1, 0.8-(sunsetEnd-sunsetStart)/1400)
        sunY = 80-(sunsetEnd-sunsetStart)*1.5
        oceanColorTop = hsl(0.6+(sunsetEnd-sunsetStart)/1400, 1, 0.7-(sunsetEnd-sunsetStart)/900)
        oceanColorBottom = hsl(0.53+(sunsetEnd-sunsetStart)/1400, 1, 0.85-(sunsetEnd-sunsetStart)/1400)
    
    
    
    sky = (DATPens().rect(Rect(1080,1920))
    #.f(Gradient.Vertical(Rect(1080,600).offset_y(1000), hsl(0.9 , 1, 0.88), hsl(1, 1, 0.85)))
    .f(skyColor)
    .scale(1.1)
    )

    # stars
    
    stars = DATPens()

    for i in range(starCount):
        starPointx = starPoints[i][0]
        starPointy = starPoints[i][1]
        starRect = Rect([starPointx, starPointy, starSize, starSize])
        stars.append(
            DATPen()
            .rect(starRect)
            #.f(hsl(skyColor.h,0,skyColor.l+(f.i-sunsetEnd)/100))  
            .f(1,1,1)     
            )

    for i in range(len(stars)):

        if f.i < sunsetEnd or (rs1[i]) > f.i-sunsetEnd:
            stars[i].scale(0)
            continue
            
        occLoopsSeed = (i)
        starLoop = f.a.progress(f.i - (i*10), loops=64, easefn="ceio")
        occLoops = [occLoopsSeed,occLoopsSeed+1]
        for k in range(100):     # 100 just to dirtily cover everything
            occLoops.append(math.floor(occLoopsSeed/10) + k*2)
            occLoops.append(math.floor(occLoopsSeed/10) + k*2 + 1)
        if starLoop.loop in occLoops:
            stars[i].scale(.1+starLoop.e)


    tide = tideLoop.e/4 * ((math.floor((tideLoop.loop+2)/2)%4)/4)

    ocean = (DATPens().rect(Rect(1080,600))
    .scale(1.1,1)
    .f(Gradient.Vertical(Rect(1080,600).offset_y(500), oceanColorTop, oceanColorBottom))
    #.f(hsl(0.6 , 1, 0.75))
    .offset_y(400)
    
    # tide

    .scale(1, 1+tide)
    .offset_y(-600*tide/2)
    )
    
    # waterShimmer = (DP.Interpolate([a, b], f.a.progress(f.i, loops=1, easefn="seio").e)
    #         .f(None)
    #         .smooth()
    #         .s(1).sw(1)
    #         .phototype(f.a.r, blur=10, cut=40, cutw=20, fill=(hsl(.6,1,.73)))
    #         )
    
    sun = (DATPens()
        .oval(f.a.r.inset(f.a.r.mxx/2-200,f.a.r.mxy/2-200))
        #.f(Gradient.Vertical(Rect(1080,600).offset_y(800), hsl(0.2 , 1, 0.7), hsl(0, 1, 0.8)))
        .f(sunColor)
        .translate(300,sunY) 
        .pmap(lambda i, p: 
        (p.flatten(2)
            .nlt(warp_fn(f.i*10, f.i*10, mult=2))))
        #.phototype(f.a.r, blur=20, cut=100, cutw=20,  fill=(hsl(.09,1,.83)))
    )


    sand = (DATPens().rect(Rect(1200,500))
    .scale(2,1)
    #.f(Gradient.Vertical(Rect(1080,400), hsl(0.16 , 1, 0.78), hsl(0.16, 1, 0.85)))
    .f(hsl(0.16, 1,  0.82))
    )
    
    ocean.pmap(lambda i, p: 
        (p.flatten(1)
            .nlt(warp_fn(f.i*4, f.i*4, mult=15))))

    # sand.pmap(lambda i, p: 
    #     (p.flatten(1)
    #         .nlt(warp_fn(f.i*4, f.i*4, mult=15))))

    sunReflection = (sun[0].copy()
        .offset(0,-30).skew(-.15).scale(1,.7)
        .f(Gradient.Vertical(Rect(1080,600).offset_y(800), hsl(0.15 , .8, 0.7), hsl(0, 1, 0.8)))
        .reverseDifference(ocean)
        .xor(ocean)
        .offset_y(4)
        .color_phototype(f.a.r, blur=10, cut=120, cutw=45)
    )

    sunTextRadOffset = 18
    sunCirc = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-200 - sunTextRadOffset,f.a.r.mxy/2-200 - sunTextRadOffset)).translate(300,sunY).reverse()
    sunProgress += sunLoop.e

    sunText = (StyledString("Friday 7PM "*20,
        Style(vulfBold, 40, wght=800, wdth=0, tu=0, space=500))
        .fit(sunCirc.length())
        .pens()
        .f(hsl(1,1,1))
        #.distribute_on_path(sunCirc, offset= -1000 + sunProgress * 2)
        .distribute_on_path(sunCirc, offset= f.i - 1000)
        .phototype(f.a.r, blur=2, cut=100, cutw=20,  fill=(hsl(1,1,1)))
        )


    return (
        # beach!
        (sky),
        (stars),
        (sun),
        (sunText),
        
        (sand),
        (LatA),
        (ocean),
        #(sunReflection),
        #(waterShimmer),

        (CBShadow
        .phototype(f.a.r, blur=2, cut=100, cutw=20,  fill=(hsl(1,1,1)))
        ),
        (CB
        .phototype(f.a.r, blur=2, cut=100, cutw=20,  fill=(hsl(.6,1,.82)))
        ),
    )


def release(passes):
    FFMPEGExport(arborOcean, passes).gif().write()