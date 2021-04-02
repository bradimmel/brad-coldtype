from coldtype import *
from coldtype.time.midi import MidiReader
from coldtype.warping import warp_fn

obvs = Font("assets/Secuela-Italic-v_1_787-TTF-VF.ttf")
drums = MidiReader("demos/coldtypeDrums01.mid", duration=190, bpm=82, fps=30)[0]
#drums = MidiReader("assets/808.mid", duration=120, bpm=120, fps=30)[0]
logos = DefconFont("assets/logos.ufo")
wav = __sibling__("demos/coldtypeDrums01.wav")
#wav = Path("assets/808.wav")

@animation(duration=drums.duration, audio=wav)
def drummachine(f):
    kick = drums.fv(f.i, [36], [5, 50])
    snare2 = drums.fv(f.i, [37], [15, 75])
    snare3 = drums.fv(f.i, [39], [5, 5])
    hat = drums.fv(f.i, [42], [10, 10])

    style = Style(obvs,
        390,
        tu=-10+0*snare2.ease(),
        wdth=1-snare2.ease()*0,
        ro=1,
        r=1,
        #kp={"T/Y":-25}
        )

    pens = (Composer(f.a.r,
        "CANTA\nLOUPE",
        style,
        #leading=math.floor(10+kick.ease()*10)
        )
        .pens()
        .align(f.a.r)
        .f(hsl(1, 0.9, 1))
        )

    snare = drums.fv(f.i, [38], [10, 40])
    se = snare.ease()

    if snare.count%2 == 1: # the first snare hit
        pens[0].translate(-10*se, 0)
        pens[1].translate(10*se, 0)
        #pens[0].ffg("L").rotate(se*-30)
    else: # second snare
        pens[0].translate(10*se, 0)
        pens[1].translate(-10*se, 0)
        #(pens[1]
        #    .ffg("P")
        #    .mod_contour(0, lambda c:
        #        c.rotate(se*30)))

    def move_A2_bar( idx,x, y):
        if idx in [2,3,16,17]:
            return x, y-10*snare3.ease()

    pens[0].map_points(move_A2_bar)

    def move_A1_bar( idx,x, y):
        if idx in [2,3,16,17]:
            return x, y-5*snare2.ease()

    pens[0][3].map_points(move_A1_bar)

    def move_T_top( idx,x, y):
        if hat.count%2 == 0 and 6 <= idx <= 7:
            return x+10*hat.ease(), y

        elif hat.count%2 == 1 and 0 <= idx <= 1:
            return x-10*hat.ease(), y

    pens[0].ffg("T").map_points(move_T_top)

    def move_O_center( idx,x, y):
        if 21 <= idx <= 40:
            return x+8*kick.ease(), y

    pens[1].ffg("O").map_points(move_O_center)

    #(pens[1]
    #     .ffg("P")
    #     .mod_contour(1, lambda c:
    #         c.rotate(snare3.ease()*-30)))

    # if kick.count%2 == 1:
    #     line = 0
    #     glyph = "O"
    # else:
    #     line = 1
    #     glyph = "T"

    # (pens[line]
    #     .ffg(glyph)
    #     .scale(1+0.1*kick.ease()))

    #if (hat.count%3) == 1:
        # (pens[0]
        #     .ffg("O")
        #     .mod_contour(1, 
        #         lambda c: (c
        #             .translate(10*hat.ease(), 10*hat.ease())
        #             .rotate(hat.ease()*10))))

    #elif (hat.count%3) == 2:
        # (pens[0]
        #     .ffg("D")
        #     .mod_contour(1,
        #         lambda c: (c
        #             .translate(10*hat.ease(), 10*hat.ease())
        #             .rotate(hat.ease()*10))))




    #fp = f.a.progress(f.i, easefn="linear").e
    #ghz_logo = (DATPen()
        #.svg("assets/cantaloupe.svg")
        #.scale(0.2)
        #.align(f.a.r, y="mny")
        #.translate(0,100)
        #.nonlinear_transform(warp_fn(speed=fp*3, rz=3, mult=10))
        #.skew(snare2.ease()*.1))

    return DATPens([
        (DATPen()
            .rect(f.a.r)
            .fill(hsl(0.07, 0.9, 0.7))),
        #ghz_logo.f(hsl(0.9, 0.55, 0.5)),
        (pens
            
            .reversePens()
            .translate(0, 100)
            #.pmap(lambda i, p: 
            #  (p.flatten(3)
            #      .nlt(warp_fn(f.i*10, f.i*10, mult=300))))
            .understroke(s=hsl(.95, 1, 1), sw=15)
              .phototype(f.a.r, cut=150, cutw=8, fill=(hsl(0.16, 1, 0.83)))
            )])

def release(passes):
    FFMPEGExport(drummachine, passes).gif().write()