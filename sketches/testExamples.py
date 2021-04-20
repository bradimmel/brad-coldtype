from coldtype import *

co = Font("../assets/MutatorSans.ttf")

@renderable((1000, 1000))
def text_on_a_path_fit(r):
    circle = DATPen().oval(r.inset(250)).reverse()
    dps = (StyledString("COLDTYPE COLDTYPE COLDTYPE ", # <-- note the trailing space
        Style(co, 200, wdth=1, tu=100, space=500))
        .fit(circle.length()) # <-- the fit & length methods
        .pens()
        .distribute_on_path(circle)
        .f(Gradient.H(circle.bounds(), hsl(0.5, s=0.6), hsl(0.85, s=0.6))))
    return dps