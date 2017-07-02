import delay, event, sl_metro

#Finishing flag
finished = False

#metro
metro = sl_metro.Metro(0.1)

#Make call back functions for timer involing
def foo():
    global finished
    print "[He]"

def bar(*args):
    print "[is]" , " , " , args[0] , " , " , args[1] , " , " , args[2]
    assert args[0] == 1
    assert args[1] == 0.3
    assert args[2] == 0.07

def bar2(val1, val2, val3):
    print "[foolish.]" , " , " , val1 , " , " , val2 , " , " , val3
    assert val1 == 1
    assert val2 == 0.3
    assert val3 == 0.07

#set the callbacks as event
event.add("/foo", foo)
event.add("/bar" , bar)
event.add("/bar2" , bar2)

#set timer
delay.add(1.0, "/foo")
delay.add(2.0, "/bar", 1, 0.3, 0.07)
delay.add(3.0, "/bar2", 1, 0.3, 0.07)

count = 0
while count < 50:
    if metro.update():
        count = count + 1
        print count
    pass

print "TEST is finished."
