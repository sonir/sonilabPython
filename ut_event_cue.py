import event_cue, event

#Event cue uses deque. It is thread safe. You can control event with it.

def first(val1, str1, val2):
    print val1, str1, val2
event.add("/first",first)

def second(str1):
    print str1
event.add("/second" , second)

evcue = event_cue.EventCue()
evcue.add("/first", 1, 'ehehe', 0.2)


mystr = "ahaha!"
evcue.add("/second", mystr)

evcue.dump()
print ("OK")
