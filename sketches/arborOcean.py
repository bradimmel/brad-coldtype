from coldtype import *
from coldtype.warping import warp_fn

mutator = Font("../assets/MutatorSans.ttf")
tl = Timeline(900)
@animation((1080,1920), timeline=tl)
def arbor01(f):
    circleRad = 350
    circle = DATPen().oval(f.a.r.inset(f.a.r.mxx/2-circleRad))
    squiggle = (DATPen().sine(f.a.r.inset(-200,f.a.r.mxy/2-30), 4)
    .offset(-0,400))
    squiggle2 = (DATPen().sine(f.a.r.inset(-200,f.a.r.mxy/2-30), 3)
    .offset(-0,0))
    #circle.rotate(-f.i*2)
    
    CB = (StyledString("REBECCA CHRISTENSEN",
        Style(mutator, 80, wght=800, wdth=200, tu=0, space=800))
        #.fit(squiggle.length())
        .pens()
        #.pmap(lambda i, p: p.f(hsl(1,1,1)))
        .distribute_on_path(squiggle, offset=3*f.i-800)
        )

    LatA = (StyledString("LIVE AT THE ARBOR",
        Style(mutator, 80, wght=800, wdth=200, tu=0, space=800))
        #.fit(squiggle.length())
        .pens()
        #.pmap(lambda i, p: p.f(hsl(1,1,1)))
        .distribute_on_path(squiggle2, offset=-3*f.i+1300)
        )

    sky = DATPens().rect(Rect(1080,1920)).f(hsl(.9,1,.85))
    ocean = DATPens().rect(Rect(1080,600)).f(hsl(.6,1,.7)).scale(1.1,1).offset_y(400)

    sun = (DATPens()
        .oval(f.a.r.inset(f.a.r.mxx/2-200,f.a.r.mxy/2-200))
        .f(hsl(.13,1,.8))
        #.translate(300,500)
        .translate(300,80) 
        .pmap(lambda i, p: 
        (p.flatten(2)
            .nlt(warp_fn(f.i*10, f.i*10, mult=2))))

    )

    sand = DATPens().rect(Rect(1080,500)).f(hsl(.18,1,.85))
    
    ocean.pmap(lambda i, p: 
        (p.flatten(3)
            .nlt(warp_fn(f.i*10, f.i*10, mult=30))))


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

        
        (CB),
        (LatA)
        )