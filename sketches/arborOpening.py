from coldtype import *
import random

myFont = Font("../assets/MutatorSans.ttf")
duration = 400


@animation((1080,1920), timeline=Timeline(duration))
def arborOpening(f):
    loopNum = 4
    l = f.a.progress(f.i, loops=loopNum, easefn="seio")
    

    eisenachColor = hsl(0.1, 1, 1)
    bgColor = hsl(0.58, 1, .9)
    style = Style(myFont,
        200,
        ro=1,
        r=1,
        wdth=10,
        wght=400,
        tu = -10
        )

    eisenach = ((Composer(f.a.r,
        "EISENACH",
        style,
        )
        .pens()
        .align(f.a.r)
        .f(eisenachColor)
        .understroke(s=hsl(1, 1, 1), sw=10)
        .skew(-.2)
        .rotate(5)
        .translate(-1000+f.i*6,500+f.i/2)
        # .pmap(lambda i, p:
        #     p.attr(skp = dict(
        #         PathEffect=skia.DiscretePathEffect.Make(20, l.e*10+2, random.randint(0,100))
        #     )))
        .pmap(lambda i, p: 
              (p.flatten(10)
                .roughen(amplitude = int(3))
                  ))
        )
        )

    eisenachShadow = eisenach.copy().translate(-8,-5).f(hsl(0.58, 1, .95))

    theArbor = ((Composer(f.a.r,
        "AT\n     THE ARBOR",
        style,
        )
        .pens()
        .align(f.a.r)
        .f(eisenachColor)
        .understroke(s=hsl(1, 1, 1), sw=10)
        .skew(-.2)
        .rotate(5)
        .translate(1200-f.i*6,100-f.i/2)
        # .pmap(lambda i, p:
        #     p.attr(skp = dict(
        #         PathEffect=skia.DiscretePathEffect.Make(20, l.e*10+2, random.randint(0,100))
        #     )))
        .pmap(lambda i, p: 
              (p.flatten(10)
                .roughen(amplitude = int(3))
                  ))
        )
    )
    
    theArborShadow = theArbor.copy().translate(-8,-5).f(hsl(0.58, 1, .95))
    return (
        (DATPen()
        .rect(f.a.r)
        .f(hsl(0.17,1,.78))
        .f(bgColor)
        ),

        (eisenachShadow
        .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.58, 1, .95)))
        ),

        (theArborShadow
        .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.58, 1, .95)))
        ),

        (eisenach
        
        .phototype(f.a.r, cut=150, cutw=8, fill=(eisenachColor))
        ),

        (theArbor
        
        .phototype(f.a.r, cut=150, cutw=8, fill=(eisenachColor))
        )

        

    )
