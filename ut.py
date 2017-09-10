import time, sl_metro,delay
import threading
import timer_gate as tg
import event

metro = sl_metro.Metro(1.0)

FOO_GATE_TIME = 0.5
BAR_GATE_TIME = 0.2

invoking_count = 0
invoking_count2 = 0
invoking_count3 = 0

do_test = True

def test_start():
    global do_test
    do_test = True
event.add("/test_start" , test_start)

def test_end():
    global do_test
    do_test = False
event.add("/test_end" , test_end)

def foo(val1):
    global invoking_count
    print "foo: ", val1
    invoking_count += 1
event.add("/foo" , foo)

def bar(val1):
    global invoking_count2
    print "bar: ", val1
    invoking_count2 += 1
event.add("/bar" , bar)

def baz(val1):
    global invoking_count3
    print "baz: ", val1
    invoking_count3 += 1
event.add("/baz" , baz)



tg.set(FOO_GATE_TIME , "/foo")
tg.set(BAR_GATE_TIME , "/bar")
tg.set(2.0 , "/baz")

#Basic Test store of event interval
tmp = tg.seek("/bar")
assert tmp[0] == "/bar"
assert tmp[1] == BAR_GATE_TIME
print "[OK] basic function set() and seek()"

#Test interval update with set()
tg.set(137.0 , "/baz")
tupple = tg.seek("/baz")
assert tupple[1] == 137.0
print "[OK]data update with set()"

#START TEST1
print "---------------------"
print "Star test1 ..."
print "foo() gate opens every" , FOO_GATE_TIME, "ms."
print "bar() gate opens every" , BAR_GATE_TIME, "ms."
time.sleep(2.0)

#set test1 end timer
delay.bang(3600.0, "/test_end")
#execute test 1
while do_test:
    tg.bang("/foo" , 137)
    tg.bang("/bar" , 138)
    if metro.update():
        print "+++"
        print threading.enumerate()

print "--------------"
print "start test2..."
event.bang("/test_start")
#set timer to end the next test
delay.bang(7.0, "/test_end")
#Youcan set event and its interval and bang at once with setbang()
tg.setbang(1.0, "/baz", 139)
while do_test:
    tg.bang("/baz" , 140)

print "--------------"
print "ALL TEST is finished."
