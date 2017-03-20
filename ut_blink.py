import blink

val = 0
print "1"
val = blink.run(val)
assert val == 1
print "2"
val = blink.run(val)
assert val == 0
print "3"
val = blink.run(val)
assert val == 1
print "4"
val = blink.run(val)
assert val == 0
print "5"
print "OK"
