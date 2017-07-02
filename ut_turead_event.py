import thread_event as tev
import event, tuple_tool, sl_metro

metro = sl_metro.Metro(1.0)
metro2 = sl_metro.Metro(1.0)


def foo():
    while True:
        if metro2.update():
            print "    [EVENT LOOP]"


def bar(val1):
    print "--------------------------------------"
    print "::::: bar was invoked :: " , val1
    print "--------------------------------------"

event.add("/foo" , foo)
event.add("/bar" , bar)


tev.bang("/bar" , "ehehe", 137)
tev.bang("/foo")

while True:
    if metro.update():
        print "[MAIN LOOP]"
