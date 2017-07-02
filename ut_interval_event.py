import interval_event, event

def beacon():
    print "beacon"

def finish():
    print "interval event was finished."

event.add("/beacon" , beacon)
event.add("/finish" , finish)


timer = interval_event.IntervalEvent("/beacon" , "/finish")
timer.setDaemon(True)
timer.start()

#bang looped events
print "CTRL+C to finish"
timer.set(0.5, 3)

try:
    while True:
        pass
except KeyboardInterrupt :
    print "Test Finished."
