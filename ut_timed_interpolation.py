import timed_interpolation, sl_metro


metro = sl_metro.Metro(1.0)

lerp = timed_interpolation.TimedInterpolation()
lerp.manual_set(10.0, 0.1, 10.0)
count = 0

tmp = lerp.update()

print "check manual set with starting value , end value and the duration"
while tmp != 0.1:
    if metro.update():
        tmp = lerp.update()
        print tmp

assert lerp.update() == 0.1
print "Finished."


print "check automatic set without st time"
lerp.set(10.0, 10.0)
while tmp != 10.0:
    if metro.update():
        tmp = lerp.update()
        print tmp
print "--"

print "Check direct set with duration 0.0"
lerp.manual_set(13.7, 137.0, 0.0)
assert lerp.update() == 137.0

# print "Check automatic set with duration 0.0"
lerp.set(13.7, 0.0)
assert lerp.update() == 13.7



print "ALL OK"
exit()


