from coldtype import *
from coldtype.time.nle.premiere import PremiereTimeline
from fontTools.svgLib import SVGPath

json = Path("~/Desktop/brad-coldtype/sketches/media/arbor_01.json").expanduser()
pt = PremiereTimeline(json)

mutator = Font("../assets/Fonts/MutatorSans.ttf")
vulfBlack = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BlackItalic.otf")
vulfBold = Font("../assets/Fonts/Vulf Mono/VulfMonoDemo-BoldItalic.otf")
svg_path = Path("~/Desktop/brad-coldtype/assets/river01.svg").expanduser()
r = Rect(1080,1080)


@animation(r, solo=1,  timeline=pt)
def arborMountains(f):
    
    background = Rect(r).fill(hsl(0.6, 1, 0.9))

    return (
        (background),

    )