import math

def get (x1, y1, x2, y2):
    radian = math.atan2(x2-x1, y2-y1)
    deg = math.degrees(radian)
    if deg < 0 :
        deg = 360+deg
    return deg

    # x_diff = x2 - x1
    # y_diff = y2 - y2
    # if x_diff != 0:
    #         theta = y_diff/x_diff
    # else:
    #         theta = 0

    #theta = y_diff/x_diff
    # theta = math.atan2(x_diff, y_diff)


    # return math.atan(theta)
    # return theta
