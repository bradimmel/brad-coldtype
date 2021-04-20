from coldtype import *
from coldtype.warping import warp_fn

mutator = Font("../assets/MutatorSans.ttf")
vulfBlack = Font("../assets/VulfMono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/VulfMono/VulfMonoDemo-BoldItalic.otf")
tl = Timeline(900)

rs1 = random_series(0, 100)

@animation((1080,1920), timeline=tl)
def arbor01(f):

    circleRad = 350
    circle = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-circleRad))
    squiggle = (DATPen().sine(f.a.r.inset(-400,f.a.r.mxy/2-30), 5)).offset_x(-350)
    squiggle2 = (DATPen().sine(f.a.r.inset(-200,f.a.r.mxy/2-30), 3))
    #circle.rotate(-f.i*2)
    
    CB = (StyledString("Claire Brooks",
        Style(vulfBlack, 90, wght=800, wdth=200, tu=0, space=800))
        #.fit(squiggle.length())
        .pens()
        .f(hsl(.6,1,.9))
        #.pmap(lambda i, p: p.f(hsl(1,1,1)))
        .distribute_on_path(squiggle, offset=3*f.i-100)
        .offset(0,600)

        # .pmap(lambda i, p: 
        # (p.flatten(2)
        #     .nlt(warp_fn(0, f.i*10, mult=10))))
        )

    

    CBShadow = CB.copy().offset(-4,-6).f(hsl(1,1,1))

    # LIVE AT THE ARBOR
    LatAStyle = Style(vulfBlack, 80, wght=800, wdth=200, tu=400, space=800)

    LatA = DATPens()

    LatA += (Composer(f.a.r, "LIVE", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(-350,-660)
    .rotate(10)
    )

    LatA += (Composer(f.a.r, "AT", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(100,-660)
    .rotate(-2)
    )

    LatA += (Composer(f.a.r, "THE", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(-140,-830)
    .rotate(1)
    )

    LatA += (Composer(f.a.r, "ARBOR", LatAStyle)
    .pens()
    .align(f.a.r)
    .offset(280,-850)
    .rotate(6)
    )


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
            for k in range(30):     # 100 just to dirtily cover everything
                occLoops.append(occLoopsSeed + k*6)
                occLoops.append(occLoopsSeed + k*6 + 1)
            if sandTxtLoop.loop in occLoops:
                LatA[i][0][j].rotate(sandTxtLoop.e*20)

    
    
    sky = DATPens().rect(Rect(1080,1920)).f(hsl(.9,1,.88))
    ocean = DATPens().rect(Rect(1080,600)).f(hsl(.6,1,.7)).scale(1.1,1).offset_y(400)
    sun = (DATPens()
        .oval(f.a.r.inset(f.a.r.mxx/2-200,f.a.r.mxy/2-200))
        .f(hsl(1,1,1))
        .translate(300,80) 
        # .pmap(lambda i, p: 
        # (p.flatten(2)
        #     .nlt(warp_fn(f.i*10, f.i*10, mult=2))))
        .phototype(f.a.r, blur=20, cut=100, cutw=20,  fill=(hsl(.09,1,.83)))
    )

    sand = DATPens().rect(Rect(1080,500)).f(hsl(.18,1,.85))
    
    ocean.pmap(lambda i, p: 
        (p.flatten(1)
            .nlt(warp_fn(f.i*4, f.i*4, mult=15))))


    sunTextOffset = 18
    sunCirc = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-200 - sunTextOffset,f.a.r.mxy/2-200 - sunTextOffset)).translate(300,80).reverse()
    sunText = (StyledString("Friday 7PM "*20,
        Style(vulfBold, 40, wght=800, wdth=0, tu=0, space=500))
        .fit(sunCirc.length())
        .pens()
        .f(hsl(1,1,1))
        .distribute_on_path(sunCirc, offset=3*f.i-2000)
        )


    return (
        # beach!
        (sky),
        (sun),
        (sunText),
        (sand),
        (ocean),

        (CBShadow),
        (CB),
        (LatA)
        )