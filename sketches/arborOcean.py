from coldtype import *
from coldtype.warping import warp_fn

mutator = Font("../assets/MutatorSans.ttf")
vulf = Font("../assets/VulfMono/VulfMonoDemo-BlackItalic.otf")
tl = Timeline(900)

rs1 = random_series(0, 100)

@animation((1080,1920), timeline=tl)
def arbor01(f):
    l = f.a.progress(f.i, loops=32, easefn="ceio")


    circleRad = 350
    circle = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-circleRad))
    squiggle = (DATPen().sine(f.a.r.inset(-200,f.a.r.mxy/2-30), 4))
    squiggle2 = (DATPen().sine(f.a.r.inset(-200,f.a.r.mxy/2-30), 3))
    #circle.rotate(-f.i*2)
    
    CB = (StyledString("Claire Brooks",
        Style(vulf, 90, wght=800, wdth=200, tu=0, space=800))
        #.fit(squiggle.length())
        .pens()
        .f(hsl(.6,1,.9))
        #.pmap(lambda i, p: p.f(hsl(1,1,1)))
        .distribute_on_path(squiggle, offset=3*f.i-800)
        .offset(-0,600)
        )

    CBShadow = CB.copy().offset(-4,-6).f(hsl(1,1,1))

    # LIVE AT THE ARBOR
    LatAStyle = Style(vulf, 80, wght=800, wdth=200, tu=400, space=800)

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
            LatA[i][0][j].rotate(f.a.progress(f.i - (i*10+j*5), loops=32, easefn="ceio").e*10+rs1[j+i]/10)

    
    
    sky = DATPens().rect(Rect(1080,1920)).f(hsl(.9,1,.88))
    ocean = DATPens().rect(Rect(1080,600)).f(hsl(.6,1,.7)).scale(1.1,1).offset_y(400)

    sun = (DATPens()
        .oval(f.a.r.inset(f.a.r.mxx/2-200,f.a.r.mxy/2-200))
        .f(hsl(1,1,1))
        #.translate(300,500)
        .translate(300,80) 
        .pmap(lambda i, p: 
        (p.flatten(2)
            .nlt(warp_fn(f.i*10, f.i*10, mult=2))))
        .phototype(f.a.r, blur=20, cut=100, cutw=20,  fill=(hsl(.09,1,.8)))
    )

    sand = DATPens().rect(Rect(1080,500)).f(hsl(.18,1,.85))
    
    ocean.pmap(lambda i, p: 
        (p.flatten(1)
            .nlt(warp_fn(f.i*10, f.i*10, mult=15))))


    # beach[1].f(hsl(.9,1,.85))
    # beach[2].f(hsl(.5,1,.8))
    # beach[3].f(hsl(.18,1,.85))
    # beach[4].f(hsl(.18,1,.85))
    # beach.scale(1,1.5).offset_y(-100)
    # beach.pmap(lambda i, p: 
    #         (p.flatten(3)
    #             .nlt(warp_fn(f.i*10, f.i*10, mult=30))))

    return (
        # beach!
        (sky),
        (sun),
        (sand),
        (ocean),

        (CBShadow),
        (CB),
        (LatA)
        )