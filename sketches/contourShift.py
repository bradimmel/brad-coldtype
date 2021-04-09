from coldtype import *
from coldtype.warping import warp_fn

myFont = Font("../assets/VulfMonoDemo-Italic.otf")
duration = 450
@animation((2000,300), timeline=Timeline(duration))
def bradleyimmel(f):
    loopNum = 18
    l = f.a.progress(f.i, loops=loopNum, easefn="eeio")
    l_speedy = f.a.progress(2*f.i, loops=loopNum, easefn="eeio")
    l_speedy_sin = f.a.progress(2*f.i%duration, loops=loopNum, easefn="ceio")


    myTracking = 0
    fontSize = 200
    if l.loop in [24,25]:
        myTracking = -l_speedy_sin.e*50
        #fontSize += l.e*10

    style = Style(myFont,
        fontSize,
        tu=myTracking,
        kp={"y/I":700}
        )

    bimmel = (Composer(f.a.r, 
        "BradleyImmel",
        style)
        .pens()
        .align(f.a.r)
        )
    
    if l.loop in [24,25]:
        bimmel.scale(1, 1 - l.e*.1)

    def shift_counters(i, pen):

        if pen.glyphName == "B":
            return (pen
                .mod_contour(2, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
                .mod_contour(1, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(1, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())
                .mod_contour(0, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(0, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())
            )
            
        if pen.glyphName == "r":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
            )

        if pen.glyphName == "a":
            return (pen
                .mod_contour(1, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
                .mod_contour(0, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(0, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())
            )

        if pen.glyphName == "d":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
                .mod_contour(1, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(1, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())
            )

        if pen.glyphName == "l":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())

                .mod_contour(0, lambda p: (p
                .scale(1, l.e*.1 + 1)
                .offset(0, l.e*15)
                .rotate(l.e%0.01 * 500 * l.e)) if l.loop in [8, 9] else p.noop())
            )
        
        if pen.glyphName == "e":
            return (pen
                .mod_contour(1, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
                .mod_contour(0, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(0, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())            )

        if pen.glyphName == "y":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
            )

        if pen.glyphName == "I":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())

                .mod_contour(0, lambda p: (p
                .scale(1, l.e*.1 + 1)
                .offset(0, l.e*15)
                .rotate(l.e%0.01 * 500 * l.e)) if l.loop in [8, 9] else p.noop())
            )

        if pen.glyphName == "m":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
            )



    def move_r_top( idx,x, y):
        if 36 <= idx <= 52 and l.loop in [14]:
            return x, y + l_speedy.e*12
        else:
            return x, y

    def move_d_top( idx,x, y):
        if (36 <= idx <= 52 or 0 <= idx <= 2) and l.loop in [15]:
            return x, y + l_speedy.e*12
        else:
            return x, y

    bimmel[0][1].map_points(move_r_top)

    bimmel[0][3].map_points(move_d_top)
    def move_y_top( idx,x, y):
        if 50 <= idx <= 66 and l.loop in [16]:
            return x, y + l_speedy.e*8
        elif 35 <= idx <= 41 and l.loop in [17]:
            return x, y + l_speedy.e*8
        else:
            return x, y

    bimmel[0][6].map_points(move_y_top)
    


    return (
        (bimmel
        .pmap(shift_counters)
        .f(0)
        #.phototype(f.a.r, cut=150, cutw=40, fill=(hsl(0.16, 1, 0)))
        )
    )

def release(passes):
    FFMPEGExport(bradleyimmel, passes).gif().write()