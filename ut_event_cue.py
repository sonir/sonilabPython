import event_cue, event

#Event cue uses deque. It is thread safe. You can control event with it.

def first(args):
    print "first()" , args[0], "," , args[1], ",", args[2]
event.add("/first",first)

def second(str):
    print str
event.add("/second" , second)

evcue = event_cue.EventCue()
args = []
args.append(1)
args.append('ehehe')
args.append(0.2)
evcue.add("/first", args)


mystr = "ahaha!"
args2=[]
args2.append(mystr)
evcue.add("/second", args2)

evcue.dump()
print ("OK")
