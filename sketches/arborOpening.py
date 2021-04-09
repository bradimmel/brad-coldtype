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
        tu = -25
        )

    # define different sections/speeds
    slowPoints = [150,250]
    fastCloudSpeed = 3
    slowCloudSpeed = .8

    if f.i  < slowPoints[0]/fastCloudSpeed:     # in
        cloudProgress = fastCloudSpeed * f.i
    elif f.i > slowPoints[1]/fastCloudSpeed:    # out
        cloudProgress = slowPoints[0] + ((slowPoints[1] - slowPoints[0]) / fastCloudSpeed) * slowCloudSpeed + (f.i-slowPoints[1]/fastCloudSpeed) * fastCloudSpeed
    else:                                       # middle
        #cloudProgress = (fastCloudSpeed-1)*slowPoints[0]/fastCloudSpeed+f.i
        cloudProgress =  slowPoints[0] + (f.i - slowPoints[0] / fastCloudSpeed) * slowCloudSpeed
    


    eisenach = ((Composer(f.a.r,
        "EISENACH",
        style
        )
        .pens()
        .align(f.a.r)
        .f(eisenachColor)
        .understroke(s=hsl(1, 1, 1), sw=10)
        .skew(-.2)
        .rotate(5)
        .translate(-1000+cloudProgress*6,500+f.i/2)
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
        style
        )
        .pens()
        .align(f.a.r)
        .f(eisenachColor)
        .understroke(s=hsl(1, 1, 1), sw=10)
        .scale(.8)
        .skew(-.2)
        .rotate(5)
        .translate(1100-cloudProgress*6,100-f.i/2)
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

    sunRad  =  200
    sunColor = hsl(0.17 -f.i/7000,1,.85)
    sun = (DATPen()
        .oval(f.a.r.inset(f.a.r.mxx/2-sunRad,f.a.r.mxy/2-sunRad))
        .f(sunColor)
        .translate(300,500)
        .flatten(30)
        .roughen(5)
        
    )

    sky = (DATPen()
        .rect(f.a.r)
        .f(hsl(0.17,1,.78))
        .f(bgColor)
    )

    theArborShadow = theArbor.copy().translate(-8,-5).f(hsl(0.58, 1, .95))
    





    return (
        (sky),

        (sun
        .phototype(f.a.r, cut=150, cutw=8, fill=(sunColor))
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
