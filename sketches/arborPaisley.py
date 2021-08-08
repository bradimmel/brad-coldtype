from coldtype import *
from fontTools.misc.transform import Transform
from coldtype.time.nle.premiere import PremiereTimeline
from coldtype.warping import warp_fn
import random as pyRandom
import numpy as np
import soundfile as sf
from coldtype.time.audio import Wavfile

json = Path("~/Desktop/brad-coldtype/sketches/media/arborPaisley_coldtype.json").expanduser()
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
audio = Wavfile("../media/Rich Girl Guitar.wav")

r = Rect(1080,1080)

paisleySpacer = 250
paisleyPos = []
paisleyCount = 22
paisleyPos = []
paisleyMove = []
for i in range(paisleyCount):
    paisleyPos.append((0,0,0))
for i in range(paisleyCount):
    valid = False
    while not valid:
        xPos = pyRandom.randint(0,1080)
        yPos = pyRandom.randint(0,1920)
        paisleyMove.append((pyRandom.randint(-50,50),pyRandom.randint(-50,50),pyRandom.randint(-10,10)))
        rotPos = pyRandom.randint(0,360)
        for k in range(paisleyCount):
            x,y,rot = paisleyPos[k]
            dist = math.sqrt(math.pow(xPos-x,2) + math.pow(yPos-y,2))
            if dist < paisleySpacer:
                valid = False
                break
            else:
                valid = True

    paisleyPos[i] = (xPos, yPos, rotPos)




@animation(r,  timeline=pt)
def arborPaisley(f):
    amp = audio.amp(f.i)

    def introBlur(startFrame):
        return (max(1,3-(f.i-startFrame-100)/100))

    starts = [0, 30, 100, 130, 130]
    positions = [500, 300, 50, -150, -330]
    # positions = [800, 600, 100, -120, -560]
    drift = 1/20
    textColorPhoto = hsl(0.7,1,0.2)


    text = DPS(pens=[
        (StyledString("THE HOUSE BAND",
            Style(swear,120, tu = 40))
            .pens()
            .align(f.a.r)
            .pmap(lambda i, p: 
                (p.flatten(3)
                    .nlt(warp_fn(f.i*2, f.i*2,octaves=3,speed=5, mult=15))))
        ),

        (StyledString("presents",
            Style(swearItalic,100, tu = 40))
            .pens()
            .align(f.a.r)
            .pmap(lambda i, p: 
                (p.flatten(3)
                    .nlt(warp_fn(f.i*2, f.i*2,octaves=3,speed=5, mult=15))))
        ),

        (StyledString("PAISLEY",
            Style(blimey,400, wght=800, tu = -40, kp={"P/A":-30, "I/S":-20, "S/L":-15}))
            .pens()
            .align(f.a.r)
            .pmap(lambda i, p: 
                (p.flatten(3)
                    .nlt(warp_fn(f.i*2, f.i*2,octaves=3,speed=5, mult=15))))
        ),

        (StyledString("Live at the Arbor ",
            Style(swearItalic,60, tu = 550))
            .pens()
            .align(f.a.r)
            .skew(.2)
            .pmap(lambda i, p: 
                (p.flatten(3)
                    .nlt(warp_fn(f.i*2, f.i*2,octaves=3,speed=5, mult=15))))
        ),

        (Composer(f.a.r, "Cameron  Most                                                        7.30\n THB                                                                                                    8.00",
            Style(swear,80, wght=800, tu = -40, kp={"P/A":-30, "I/S":-20, "S/L":-15}), leading=40)
            .pens()
            .align(f.a.r)
            .pmap(lambda i, p: 
                (p.flatten(3)
                    .nlt(warp_fn(f.i*2, f.i*2,octaves=3,speed=5, mult=15))))
        ),

    ]
    )




    
    loops = []
    for i in range(len(text)):
        loops.append(f.a.progress(f.i-starts[i], loops=1, easefn="ceio"))
        if loops[i].loop != 0:
            loops[i].e = 1
        (text[i]
        .f((f.i-starts[i]-100)/100)
        .offset(0, positions[i]-loops[i].e*100-(f.i-starts[i])*drift)
        )
    
        PAISLEYCopies = DPS()

    # for i in range(5):
    #     PAISLEYCopies.append(
    #         (text[2].copy()
    #         #.scale(1 + .03*i,1+.05*i)
    #         .offset(-10*i,-10*i)
    #         )
    #     )
        
    # PAISLEYCopies.reversePens()

    # photoPAISLEY = DPS()
    # colors = [hsl(0.7,1,0.8), hsl(0.7,1,0.7), hsl(0.7,1,0.6), hsl(0.7,1,0.5), hsl(0.7,1,0.4), ]
    # for i in range(len(PAISLEYCopies)):
    #     photoPAISLEY.append(PAISLEYCopies[i].phototype(f.a.r,blur=introBlur(starts[2]+i*10),cut=max(300-(f.i-(starts[5]+i*10)), 200),cutw=max(100-(f.i-(starts[5]+i*10)), 200), fill=colors[i])),


    photoText = DPS()
    for i in range(len(text)):
        photoText.append(text[i].phototype(f.a.r,blur=introBlur(starts[i]),cut=100,cutw=100, fill=textColorPhoto))



    paisleyColor = hsl(.14,1,.9)

    paisley =  (StyledString("A",
            Style(pais,600, tu = 40))
            .pens()
            .f(hsl(.14-amp/8,1,.9-amp/4))
            .offset(0,0)
        )

    paisleys = DPS()
    for i in range (len(paisleyPos)):
        paisleys.append((paisley.copy()
            .offset(paisleyPos[i][0], paisleyPos[i][1])
            .rotate(paisleyPos[i][2] + paisleyMove[i][2]*f.i/15)
            .offset(paisleyMove[i][0]*f.i/100,paisleyMove[i][1]*f.i/100))
            .scale(1+amp*1.2)
            )

    return(
        (DP(f.a.r).f(hsl(.08,.4,.85))),
        (paisleys),
        (photoText),
        
        
    )