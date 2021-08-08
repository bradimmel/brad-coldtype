from coldtype import *
from coldtype.time.nle.premiere import PremiereTimeline

fnt = Font.Cacheable("../assets/VulfMono/VulfMonoDemo-BlackItalic.otf")
json = Path("~/Desktop/brad-coldtype/sketches/media/helloWorld_coldtype.json").expanduser()
pt = PremiereTimeline(json) #.retime_for_symbol("a")

@animation((1920, 1080), timeline=pt, bg=0)
def test(f):
    print(pt[0].current(f.i))
    return (StyledString(pt[0].current(f.i).text,
        Style(fnt, 250))
        .pen()
        .align(f.a.r)
        .f(hsl(.1,1,.5)))