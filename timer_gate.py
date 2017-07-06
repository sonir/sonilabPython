from collections import deque
import delay
import event as ev

DEFAULT_FLG = True

LENGTH = 99
queue = deque([] , maxlen=LENGTH)

def set(ms, adr):
    obj = seek(adr)
    if obj == None:
        # when it is new one, add new gate
        global queue
        param = ( adr , ms, DEFAULT_FLG )
        queue.append(param)
    else:
        #it is existing one, update the new ms
        update_with_true(ms,adr)

def seek(adr):
    global queue
    for param in queue:
        if param[0] == adr:
            return param
    #if could not find .. return none
    return None

def update(ms, adr, flg):
    global queue
    count = 0
    for param in queue:
        if param[0] == adr:
            queue[count] = (adr, ms, flg)
            return True
        count += 1
    #if could not find .. return none
    print "timer_gate :: not found " , adr
    return False


def update_with_true(ms, adr):
    update(ms, adr, True)
ev.add("/update_with_true", update_with_true)


def update_with_false(ms, adr):
    update(ms, adr, False)
ev.add("/update_with_false", update_with_false)


def bang(adr, *args):
    obj = seek(adr) #get stored data
    ms = obj[1]
    state = obj[2]
    if state:
        ev.bang(adr, *args)
        ev.bang("/update_with_false", ms, adr)
        delay.bang(ms, "/update_with_true" , ms, adr)
    else:
        return False

def setbang(ms, adr, *args):
    set(ms, adr)
    bang(adr, *args)
