import math
minimum_val = 0.0001

def get (deg):

    global minimum_val
    deg = int(deg)

    #set 0 is twelve o'clock
    rad = math.radians(deg)
    # print("rad:{}".format(rad))
    x = math.sin(rad) * 1.0
    y = math.cos(rad) * 1.0
    # 1.0 is radius

    #marume
    x = round(x,4)
    y = round(y,4)
    return [x,y]
