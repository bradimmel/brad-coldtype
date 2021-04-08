from coldtype import *
from coldtype.warping import warp_fn

myFont = Font("../assets/VulfMonoDemo-Light.otf")

@animation((2600,800), timeline=Timeline(900))
def bradleyimmel(f):
    l = f.a.progress(f.i, loops=36, easefn="eeio")
    
    def shift_counters(i, pen):

        if pen.glyphName == "B":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
                .mod_contour(1, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(1, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())
                .mod_contour(2, lambda p: p.scale(1-l.e/3) if l.loop in [0, 1] else p.noop())
                .mod_contour(2, lambda p: p.rotate(l.e*-10) if l.loop in [0, 1] else p.noop())
            )
            
        if pen.glyphName == "r":
            return (pen
                .mod_contour(0, lambda p: p.skew(l.e/-5) if l.loop in [0, 1] else p.noop())
            )

        if pen.glyphName in ["l", "I"]:
            return (pen
                .mod_contour(0, lambda p: (p
                    .scale(1, l.e*.1 + 1)
                    .offset(0, l.e*15)
                    .rotate(l.e%0.01 * 500 * l.e)) if l.loop in [12, 13] else p.noop())
            )

    return (
        (Composer(f.a.r, "Bradley Immel",
        Style(myFont, 200))
        .pens()
        .align(f.a.r)
        .pmap(shift_counters)
        .f(1)
        .phototype(f.a.r, cut=100, cutw=8, fill=(hsl(0.16, 1, 0)))
        )
    )