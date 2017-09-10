import timed_interpolation, sl_metro


metro = sl_metro.Metro(1.0)

lerp = timed_interpolation.TimedInterpolation()
lerp.set(0.0, 1.0, 5.0)
count = 0
while True:
    if metro.update():
        tmp = lerp.update()
        print tmp
        if tmp == 1.0:
            metro.set(0.1)
            lerp.set(0.0, -0.1, 4.0)
        if tmp == (-0.1):
            metro.set(0.011)
            lerp.set(0.0, 10000.0, 2.0)
