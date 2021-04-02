from coldtype import *
import noise


df = "assets/Secuela-Italic-v_1_787-TTF-VF.ttf"

t = Timeline(180, storyboard=[0])



def style_a(f, hit):
    dps:DATPens = StyledString("Bradley Immel", Style(df, 200+30*(1-hit), wdth=0, ro=1, t=-10*(1-hit))).pens().align(f.a.r)
    def alter(idx, p):
        fr = p.getFrame()
        rng = 10+45*hit
        factor = 0.5
        x_seed = (f.i+idx)*factor
        fs = (200-rng)+noise.pnoise1(x_seed, repeat=int(t.duration*factor))*rng
        def move_O_center(idx, x, y):
            if 19 <= idx <= 40:
                return x+fs/90, y+fs/90
        dps[0].map_points(move_O_center)
        if p.glyphName != "space":
            return StyledString(p.glyphName, Style(df, 120, wdth=1, ro=1)).fit(fr.w).pens().align(fr)[0]
        else:
            return DATPen()

    
    #return dps
    return dps.map(alter)

    

@animation(rect=(1200,300), timeline=t)
def render(f):
    return DATPens([
        DATPen().rect(f.a.r).f(0),
        style_a(f, 1).f(1)
    ])