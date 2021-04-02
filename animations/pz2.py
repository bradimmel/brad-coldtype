from coldtype import *
from coldtype.time.midi import MidiReader
import soundfile as sf
from coldtype.warping import warp_fn
from coldtype.time.audio import Wavfile

myFont = Font("assets/Secuela-Italic-v_1_787-TTF-VF.ttf")
drums = MidiReader("demos/pz2/pz2_MIDI_new.mid", duration=750, bpm=82, fps=30)[0]
# wav playing still doesn't work yet
wav = __sibling__("../demos/pz2/pz2_amp.wav")
audio = Wavfile("demos/pz2/pz2_amp.wav")

wSize = 1500


@animation((wSize,wSize), duration=drums.duration, audio=wav)
def pz2(f):
    kick = drums.fv(f.i, [36], [5, 50])
    snare = drums.fv(f.i, [38], [10, 50])
    contract = drums.fv(f.i, [34], [5, 200])
    shifter = drums.fv(f.i-5, [40], [5, 5])
    hat1 = drums.fv(f.i, [42], [10, 10])
    hat2 = drums.fv(f.i, [43], [10, 10])
    hat3 = drums.fv(f.i, [44], [10, 10])
    hat4 = drums.fv(f.i, [45], [10, 10])
    synth1 = drums.fv(f.i, [48], [10, 10])
    synth2 = drums.fv(f.i, [49], [10, 10])
    
    produceZooColor = hsl(0.72, 0.5, .52)
    pzScale = 0

    style = Style(myFont,
        390,
        tu=150-120*contract.ease(),
        )

    amoeba = (Composer(f.a.r,
        "AMOEBA\nVOL.   2",
        #"PRODUCE\nZOO",
        style,
        )
        .pens()
        .align(f.a.r)
        .f(hsl(1, 0.9, 1))
        .pmap(lambda i, p: 
              (p.flatten(3)
                .roughen(amplitude = int(snare.ease()*15))
                  ))
        .rotate(10+f.i/20 - shifter.count*10)
        )

    amoeba2 = amoeba.copy().translate(-20,0)
    amoeba3 = amoeba.copy().translate(-30,0)

    

    def move_O_center(idx,x,y):
        if 240 <= idx <=  434:
            return x+13*kick.ease(), y

    def move_B_centers(idx,x,y):
        if 255 <= idx <=  465:
            return x+13*kick.ease(), y

    def shift_dot(idx,x,y):
        if 0 <= idx <= 1000 :    # all points
            return x+10, y


    amoeba[0][3].map_points(move_O_center)
    amoeba[1][6].map_points(move_O_center)
    amoeba[0][1].map_points(move_B_centers)

    amoeba2[0][3].map_points(move_O_center)
    amoeba2[1][6].map_points(move_O_center)
    amoeba2[0][1].map_points(move_B_centers)

    amoeba3[0][3].map_points(move_O_center)
    amoeba3[1][6].map_points(move_O_center)
    amoeba3[0][1].map_points(move_B_centers)

    amoeba2[1][4].map_points(shift_dot)
    amoeba3[1][4].map_points(shift_dot)


    # background

    zebra = (DATPen().rect(f.a.r).f(hsl(0,0,0)))
    for c in f.a.r.subdivide_with_leading(300, .5, "mxy"):
        zebra += DATPen().rect(c).f(hsl(1, 0, 1))


    # spinning produce zoos

    # override
    secondHalfFrame = 438

    # secondHalfFrame = shifter.note.on
    # print(secondHalfFrame)

    # make produce zoos appear when shifter starts
    if (f.i > secondHalfFrame):
        pzScale = 0.1
    else:
        pzScale = 0

    adjustedFrame = f.i - secondHalfFrame

    pz0 = (Composer(f.a.r,
        "PRODUCE\nZOO",
        style,
        )
        .pens()
        .align(f.a.r)
        .f(produceZooColor)
        .scale(pzScale)
        )

    pz01 = (pz0.copy()
        .translate(10-adjustedFrame/4 ,-600-adjustedFrame/1.5)
        .rotate(adjustedFrame-50)
    )   
    pz02 = (pz0.copy()
        .translate(400-adjustedFrame/2,-350+adjustedFrame/3)
        .rotate(adjustedFrame+10)
    )
    pz03 = (pz0.copy()
        .translate(-300+adjustedFrame/4,-500+adjustedFrame/2)
        .rotate(adjustedFrame+60)
    )
    pz04 = (pz0.copy()
        .translate(600+adjustedFrame/3,-550-adjustedFrame/2)
        .rotate(adjustedFrame-0)
    )
    pz05 = (pz0.copy()
        .translate(-600+adjustedFrame/2,-660+adjustedFrame/4)
        .rotate(adjustedFrame-30)
    )
    pz06 = (pz0.copy()
        .translate(500-adjustedFrame/4,550-adjustedFrame/2)
        .rotate(adjustedFrame+120)
    )
    pz07 = (pz0.copy()
        .translate(-500-adjustedFrame/1.5,660-adjustedFrame/2)
        .rotate(adjustedFrame-120)
    )
    pz08 = (pz0.copy()
        .translate(-200+adjustedFrame/3,450-adjustedFrame/3)
        .rotate(adjustedFrame+75)
    )
    pz09 = (pz0.copy()
        .translate(150-adjustedFrame/4,600+adjustedFrame/3)
        .rotate(adjustedFrame-60)
    )
    pz10 = (pz0.copy()
        .translate(-650+adjustedFrame,350-adjustedFrame/4)
        .rotate(adjustedFrame-200)
    )

    
    

    return DATPens([

        # background
        (zebra
        .scale(4)
        .rotate(-5)
        .translate(f.i*.25,f.i*1)
            ),

        # lil produce zoos
        (pz01
            .understroke(s=produceZooColor, sw=3)
            ),

        (pz02
            .understroke(s=produceZooColor, sw=3)
            ),

        (pz03
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
            ),

        (pz04
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        (pz05
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        (pz06
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        (pz07
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        (pz08
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        (pz09
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        (pz10
            .reversePens()
            .understroke(s=produceZooColor, sw=3)
        ),

        # white
        (amoeba3
            .reversePens()

            .understroke(s=hsl(.95, 1, 1), sw=15)
            .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.7, 1, 1)))
            ),

        # purple
        (amoeba2
            .reversePens()

            .understroke(s=hsl(.95, 1, 1), sw=15)
            .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.7, 1, 0.85)))
            ),
        
        # yellow
        (amoeba
            
            .reversePens()
            .translate(0, 0)

            .understroke(s=hsl(.95, 1, 1), sw=15)
            .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.15, 1, 0.85)))
            )])


def release(passes):
    FFMPEGExport(pz2, passes).gif().write()