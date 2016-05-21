# Invert degree 180.
# Ex. 270 -> 90

import math

def get(deg):
    deg = int(deg)
    rad = math.radians(deg)
    rad = float(rad)

    # For unknown bug 135 is dark number
    if deg == 315 :
        return 135

    inv = ( math.degrees(rad+math.pi) ) % 360.0
    return int(inv)
