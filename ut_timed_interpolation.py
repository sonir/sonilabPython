import timed_interpolation, sl_metro


metro = sl_metro.Metro(1.0)

lerp = timed_interpolation.TimedInterpolation()
lerp.manual_set(10.0, 0.0, 10.0)
count = 0
while True:
    if metro.update():
        tmp = lerp.update()
        print tmp
        if tmp == 0.0:
            metro.set(1.0)
            lerp.set(10.0, 10.0)
        if tmp == 10:
            print "OK"
            exit()
