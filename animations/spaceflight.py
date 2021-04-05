from coldtype import *
from coldtype.time.midi import MidiReader
import soundfile as sf
from coldtype.warping import warp_fn
from coldtype.time.audio import Wavfile
import random as pyRandom
import math

# todo: change font
myFont = Font("assets/Secuela-Italic-v_1_787-TTF-VF.ttf")
drums = MidiReader("demos/pz2/pz2_MIDI_new.mid", duration=100, bpm=82, fps=30)[0]
# wav playing still doesn't work yet
wav = __sibling__("../demos/pz2/pz2_amp.wav")
audio = Wavfile("demos/pz2/pz2_amp.wav")

wSize = 1500
starCount = 100
starPoints = []
starSize = 5
for i in range(starCount):
    starPoints.append((pyRandom.randint(0,wSize-starSize),(pyRandom.randint(0,wSize-starSize))))
    
@animation((wSize,wSize), duration=drums.duration, audio=wav)
def spaceflight(f):
    # kick = drums.fv(f.i, [36], [5, 50])
    
    ################
    # stars
    ################
    global starCount
    global starSize

    # todo: interpolate/smooth
    amp = audio.amp(f.i)
    starWarpSpeedSize = amp*200
    focalPoint = (f.a.r.mxx/2,f.a.r.mxy/2)
    # should probably just define as a Rect eventually?
    deadSpotRadx = 300
    deadSpotRady = 100
    stars = DATPens()

    for i in range(starCount):
        starPointx = starPoints[i][0]
        starPointy = starPoints[i][1]
        starRect = Rect([starPointx, starPointy, starSize, starSize+starWarpSpeedSize])

        # todo: replace box w circle
        # divide by 0 safety and deadspot logic
        if (starPointx-focalPoint[0]) == 0 or (-deadSpotRadx < (starPointx-focalPoint[0]) < deadSpotRadx and -deadSpotRady < (starPointy-focalPoint[1]) < deadSpotRady):
            continue

        relativePos = [(starPointx-focalPoint[0]), (starPointy-focalPoint[1])]

        # todo: better math with tan to get accurate sign?
        if relativePos[0] <= 0:
            starOrient = math.degrees(math.atan(relativePos[1]/relativePos[0]))+90
        else:
            starOrient = math.degrees(math.atan(relativePos[1]/relativePos[0]))-90
        
        stars.append(
            DATPen()
            .rect(starRect)
            .f(hsl(1,1,1))
            .rotate(starOrient, point = Point(starPointx, starPointy))      # makes it grow only outward 
        )

    ################
    # text
    ################

    style = Style(myFont,
        100,
        tu=150,
        )

    myText = (Composer(f.a.r,
        "SPACEFLIGHT",
        style,
        )
        .pens()
        .align(f.a.r)
        .f(hsl(.3, 1, .5))
        )

    return DATPens([
        # background
        (DATPen()
            .rect(f.a.r)
            .fill(hsl(0, 0, 0))),   # black


        (stars),

        (myText)
    ])
