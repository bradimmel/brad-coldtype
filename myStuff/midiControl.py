from coldtype import *
from coldtype.midi.controllers import Generic

@renderable(rstate=1)
def use_midi(r, rs):
    controller = Generic("SV-0 KEYBOARD", rs.midi)
    fader = controller(77, 0.5) # returns a value between 0 and 1
    return (DATPen()
        .oval(r.take(fader, "mdx").square())
        .f(hsl(0.65)))