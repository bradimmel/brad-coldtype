from coldtype import *
import random
from coldtype.warping import warp_fn

mutator = Font("../assets/MutatorSans.ttf")
vulf =  Font("../assets/VulfMonoDemo-Italic.otf")
duration = 400

rs1 = random_series(0, 1000)

@animation((1080,1920), timeline=Timeline(duration))
def arborOpening(f):
    loopNum = 16
    l = f.a.progress(f.i, loops=loopNum, easefn="ceio")
    l2 = f.a.progress(f.i, loops = loopNum, easefn="seio")
    #loopLength = duration/(2*loopNum)

    eisenachColor = hsl(0.1, 1, 1)
    bgColor = hsl(0.58, 1, .9)
    style = Style(mutator,
        200,
        r=1,
        ro=1,
        wdth=10,
        wght=400,
        tu = -25
        )

    # define different sections/speeds
    slowPoints = [150,280]
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
        .translate(-100)#+cloudProgress*6,500+f.i/2)
        # .pmap(lambda i, p:
        #     p.attr(skp = dict(
        #         PathEffect=skia.DiscretePathEffect.Make(20, l.e*10+2, random.randint(0,100))
        #     )))
        
        # .pmap(lambda i, p: 
        #       (p.flatten(10)
        #         .roughen(amplitude = int(3))
        #           ))
        )
        )

    # a = eisenach.pmap(lambda i, p: 
    #         (p.flatten(10)
    #         .roughen(10, seed=1)
    #         ))

    a = eisenach.copy().pen().flatten(10).roughen(20, seed=rs1[l.loop])
    b = eisenach.copy().pen().flatten(10).roughen(20, seed=rs1[l.loop+1])

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
        #.flatten(30)
        #.roughen(5)
        
    )

    sunA = sun.copy().flatten(30).roughen(20, seed=1)
    sunB = sun.copy().flatten(30).roughen(20, seed=10)

    sky = (DATPen()
        .rect(f.a.r)
        .f(hsl(0.17,1,.78))
        .f(bgColor)
    )

    theArborShadow = theArbor.copy().translate(-8,-5).f(hsl(0.58, 1, .95))
    


    # looping text
    loopStart = 4
    midSpace = 0
    if  l.loop in [loopStart, loopStart+1, loopStart+2, loopStart+3]:
        infoTracking = -60+l.e*100
        infoSize = .8
        midSpace = l.e*500
    else:
        infoTracking = -60
        midSpace = 0

    infoStyle = Style(mutator,
        200,
        r=1,
        ro=1,
        wdth=400,  
        wght=900,
        tu = infoTracking,
        kp={"Y/F":1000-midSpace}
    )

    dateAndTime = (StyledString(
    "THURSDAYFIVE PM",  
    infoStyle)
    .pens()
    .align(f.a.r)
    .scale(.5)
    .translate(0, -800)
    #.pmap(shift_counters)
    .scale(.8,1)
    .f(hsl(.9,1,1))
    #.s(1).sw(7).f(None)
    .skew(.1)
    .pmap(lambda i, p: 
            (p.flatten(3)
                .nlt(warp_fn(f.i*5, f.i*5, mult=20))))
    )

    


    
    for i in range(len(dateAndTime)):
        if l.loop in [loopStart,loopStart+2]:
            dateAndTime[i].rotate((l.e+l.loop)*90).scale((-l.e+2)/2)
        elif l.loop in [loopStart+1,loopStart+3]:
            dateAndTime[i].rotate((1-l.e+l.loop)*90).scale((-l.e+2)/2)




    return (
        (sky),

        # (sun
        # .phototype(f.a.r, cut=150, cutw=8, fill=(sunColor))
        # ),

        # new sun
        (DP
        
        #.phototype(f.a.r, cut=150, cutw=8, fill=(eisenachColor))
        .Interpolate([sunA, sunB], l2.e)
            .f(1)
            .smooth()
            .phototype(f.a.r, blur=20, cut=100, cutw=20,  fill=sunColor)
        ),

        # (eisenachShadow
        # .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.58, 1, .95)))
        # ),

        (theArborShadow
        .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.58, 1, .95)))
        ),


        # new eisenach
        (DP
        .Interpolate([a, b], l2.e)
            .f(1)
            #.smooth()
            .phototype(f.a.r, blur=5, cut=100, cutw=20)
        ),
        

        (theArbor
        
        .phototype(f.a.r, cut=150, cutw=8, fill=(eisenachColor))
        ),

        (dateAndTime
        
        .phototype(f.a.r, cut=180, cutw=8, fill=(hsl(.7,1,1)))
        
        )

        

        

    )
