import thread_event as tev
import event
import sl_metro


metro = sl_metro.Metro(1.0)
metro2 = sl_metro.Metro(1.0)
metro3 = sl_metro.Metro(1.5)


# Make callback functions
def foo():
    while True:
        if metro3.update():
            print "    [foo()::EVENT LOOP]:"

def bar(val1, val2):
    while True:
        if metro2.update():
            print "    [bar()::EVENT LOOP]:" , val1 , " , " , val2


# Connect events and callbacks
event.add("/foo" , foo)
event.add("/bar" , bar)


tev.bang("/foo")
tev.bang("/bar" , 137, 1.38)
while True:
    if metro.update() :
        print "[MAIN LOOP]"
