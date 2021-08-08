from coldtype import *
from fontTools.misc.transform import Transform
from coldtype.time.nle.premiere import PremiereTimeline
from coldtype.warping import warp_fn
import random as pyRandom
import numpy as np
import soundfile as sf
from coldtype.time.audio import Wavfile

json = Path("~/Desktop/brad-coldtype/sketches/media/arborTHBRippedJeans_coldtype.json").expanduser()
pt = PremiereTimeline(json)

mutator = Font("../assets/Fonts/MutatorSans.ttf")
vulfBlack = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BoldItalic.otf")
cheee = Font("../assets/Fonts/Cheee/CheeeDemo-BingBong.otf")
eck = Font("../assets/Fonts/Eckmannpsych/Eckmannpsych-Demo-Large.otf")
blimey = Font("../assets/Fonts/Blimey-V03/VARIABLE/Blimey-VO3-Variable.ttf")
digest = Font("../assets/Fonts/Digestive/DigestiveDemo-Small.otf")
swear = Font("../assets/Fonts/Swear Banner/SwearBannerDemo-Black.otf")
swearItalic = Font("../assets/Fonts/Swear Banner/SwearBannerDemo-BoldItalic.otf")
cheee2 = Font("../assets/Fonts/Cheee/CheeeDemo-Gnat.otf")
pais = Font("../assets/Fonts/paisley-Regular.otf")
banco  = Font("../assets/Fonts/Thrasher/banco.ttf")
topspeed  = Font("../assets/Fonts/Thrasher/top-speed.regular.ttf")
dj  = Font("../assets/Fonts/Thrasher/HANGTHEDJ.ttf")
r = Rect(1080,1920)
audio = Wavfile("../media/Californication Guitar.wav")

@animation(r,  timeline=pt)
def arborTHBRippedJeansINVERSE(f):
    amp = audio.amp(f.i)
    red =  hsl(0,1,0)
    black = hsl(0,1,0.5)
    white = hsl(0,1,1)

    checkerSize = 50
    checkers = (DATPen().rect(f.a.r).f(black))
    for i in range(math.ceil(f.a.r.mxy/checkerSize)):
        for j in range(math.ceil(f.a.r.mxx/checkerSize/2)):
            checkers += DATPen().rect(Rect(checkerSize,checkerSize)).offset(j*checkerSize*2+i%2*checkerSize, i*checkerSize).f(white)

    checkers.pmap(lambda i, p: 
                (p.flatten(3)
                    .nlt(warp_fn(f.i*2, f.i*2,octaves=3,speed=5, mult=40))))

    THB = DPS(pens=[
        (StyledString("THE HOUSE BAND",
            Style(banco,150, tu = -100+f.i/6))
            .pens()
            .align(f.a.r)
            .offset_y(600)
            .f(white)
            .understroke(1,20)
        ),

        (StyledString("THE HOUSE BAND",
            Style(banco,150, tu = -100+f.i/6))
            .pens()
            .align(f.a.r)
            .offset_y(600)
            .f(red)
            .pmap(lambda i, p: 
                (p.flatten(5)
                    .roughen(amplitude = amp*20)
                ))
            .smooth()
        )
    ])

    presents = (StyledString("PRESENTS",
            Style(topspeed,140,tu=-200+f.i*1.3))
            .pens()
            .align(f.a.r)
            .offset_y(400)
            .f(red)
            .understroke(1,20)
        )

    l = f.a.progress(f.i, loops=6, easefn="seio")
    loopNum = 4
    startRipped = -1000
    startJeans =  1000
    loopFrame = 1*(f.i-450/12*(loopNum+1))
    if l.loop < loopNum:
        xRipped = startRipped
        xJeans = startJeans
    elif l.loop == loopNum:
        xRipped = startRipped+l.e*800 +f.i-100
        xJeans = startJeans-l.e*750-f.i+100
    else:
        xRipped = startRipped+800+loopFrame+f.i-100
        xJeans = startJeans-750-loopFrame-f.i+100

    
    RJ = DPS(pens=[
        (StyledString("Ripped",
            Style(dj,130, tu=340))
            .pens()
            .align(f.a.r)
            .offset(xRipped,0)
            .f(1)
            .understroke(1,50)
        ),
        (StyledString("Ripped",
            Style(dj,200))
            .pens()
            .align(f.a.r)
            .offset(xRipped,0)
            .f(red)
            .pmap(lambda i, p: 
                (p.flatten(5)
                    .roughen(amplitude = amp*25)
                ))
            .smooth()
            #.understroke(1,50)
        ),
        (StyledString("Jeans",
            Style(dj,130, tu=360))
            .pens()
            .align(f.a.r)
            .offset(xJeans,-200)
            .f(white)
            .understroke(1,50)
        ),
        (StyledString("Jeans",
            Style(dj,200))
            .pens()
            .align(f.a.r)
            .offset(xJeans,-200)
            .f(red)
            .pmap(lambda i, p: 
                (p.flatten(5)
                    .roughen(amplitude = amp*25)
                ))
            .smooth()
            #.understroke(1,50)
        )
    ])

    l2 = f.a.progress(f.i, loops=6, easefn="seio")
    loopNum2 = 6
    startLive = -1000
    startArbor =  1000
    loopFrame2 = 1*(f.i-450/12*(loopNum2+1))
    if l2.loop < loopNum2:
        xLive = startLive
        xArbor = startArbor
    elif l2.loop == loopNum2:
        xLive = startLive+l2.e*600+f.i-100
        xArbor = startArbor-l2.e*750-f.i+150
    else:
        xLive = startLive+600+loopFrame2+f.i-100
        xArbor = startArbor-750-loopFrame2-f.i+150


    LatA = DPS(pens=[

        (StyledString("Live at",
            Style(topspeed,100))
            .pens()
            .align(f.a.r)
            .offset(xLive,-500)
            .f(red)
            .understroke(1,20)
        ),

        (StyledString("The Arbor",
            Style(topspeed,100))
            .pens()
            .align(f.a.r)
            .offset(xArbor,-600)
            .f(red)
            .understroke(1,20)
        )
    ])


    xDT  = 80
    yDT =  -890
    DT= DPS(pens=[
        (StyledString("06.04.21 8 PM",
            Style(dj,60, tu=510))
            .pens()
            .align(f.a.r)
            .offset(xDT,yDT)
            .f(1)
            .understroke(1,20)
        ),
        (StyledString("06.04.21 8 PM",
            Style(dj,80, tu=220))
            .pens()
            .align(f.a.r)
            .offset(xDT,yDT)
            .f(red)
            #.understroke(1,50)
        ),
    ])

    def T( idx,x, y):
        start = 22
        end =  27
        num = 7
        slope = num*3
        if start < idx < end:
            return x,y-(num*30-170+slope*(idx-start)/(end-start))

    def H( idx,x, y):
        start = 41
        end =  59
        num =  6
        slope = num*3
        if start < idx < end:
            return x,y-(num*30-170+slope*(idx-start)/(end-start))

    # THB[0].map_points(T)
    # THB[1].map_points(H)

    return(
        (checkers),

        (THB),#.phototype(f.a.r,blur=1,cut=100,cutw=100, fill=hsl(0,1,.5)),
        
        (presents),#.phototype(f.a.r,blur=1,cut=150,cutw=130, fill=hsl(0,1,.5)),
        (RJ),
        (LatA),
        (DT),
    )