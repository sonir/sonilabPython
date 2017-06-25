import interval_event, event, time
import sys

def foo():
    print ("foo")

event.add("/foo" , foo)

def foo2():
    print "end event"

event.add("/foo2" , foo2)

# set callback event and event for end
ie = interval_event.IntervalEvent("/foo" , "/foo2")

try:
    ie.setDaemon(True)
    ie.start()
    ie.test()
    ie.test()
    ie.set(0.5, 10)
    time.sleep(2)
    ie.set (0.05, 10)
    time.sleep(2)
    # Do finalize to avoid error in RPI
    ie.stop()
    sys.exit()

except KeyboardInterrupt:
    print "ED"
    ie.cycle = False
    sys.exit()
