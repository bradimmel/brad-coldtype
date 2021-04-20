from coldtype import *

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
    
    squigglyTxt = (StyledString("LIVE AT THE ARBOR",
        Style(mutator, 80, wght=800, wdth=200, tu=0, space=800))
        #.fit(squiggle.length())
        .pens()
        #.pmap(lambda i, p: p.f(hsl(1,1,1)))
        )

    squigglyTxt1 = squigglyTxt.copy().distribute_on_path(squiggle, offset=3*f.i-800)

    squigglyTxt2 = squigglyTxt.copy().distribute_on_path(squiggle2, offset=-3*f.i+1300)


    return (
        (DATPen().rect(f.a.r).f(hsl(.9,1,.9))),
        
        (squigglyTxt1),
        (squigglyTxt2)
        )