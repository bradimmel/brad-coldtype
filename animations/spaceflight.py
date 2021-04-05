from coldtype import *
from coldtype.time.midi import MidiReader
import soundfile as sf
from coldtype.warping import warp_fn
from coldtype.time.audio import Wavfile
import random as pyRandom
import math

myFont = Font("assets/Secuela-Italic-v_1_787-TTF-VF.ttf")
drums = MidiReader("demos/pz2/pz2_MIDI_new.mid", duration=100, bpm=82, fps=30)[0]
# wav playing still doesn't work yet
wav = __sibling__("../demos/pz2/pz2_amp.wav")
audio = Wavfile("demos/pz2/pz2_amp.wav")

wSize = 1500


@animation((wSize,wSize), duration=drums.duration, audio=wav)
def spaceflight(f):
    # kick = drums.fv(f.i, [36], [5, 50])
    
    amp = audio.amp(f.i)

    starSize = 5
    starCount = 100
    starWarpSpeedSize = amp*100
    focalPoint = (f.a.r.mxx/2,f.a.r.mxy/2)
    deadSpotRad = 200
    stars = DATPens()
    for i in range(starCount):
        starRect = Rect([pyRandom.randint(0,f.a.r.mxy-starSize), pyRandom.randint(0,f.a.r.mxx-starSize), starSize, starSize+starWarpSpeedSize])
        # todo: replace box w circle
        if (starRect.x-focalPoint[0]) == 0 or (-deadSpotRad < (starRect.x-focalPoint[0]) < deadSpotRad and -deadSpotRad < (starRect.y-focalPoint[1]) < deadSpotRad):
            continue
        starOrient = math.degrees(math.atan((starRect.y-focalPoint[1])/(starRect.x-focalPoint[0])))-90

        stars.append(
            DATPen()
            .rect(starRect)
            .f(hsl(1,1,1))
            .rotate(starOrient)
        )


    return DATPens([
        # background
        (DATPen()
            .rect(f.a.r)
            .fill(hsl(0, 0, 0))),   # black


        (stars)
    ])
