import event

def foo ():
    print("foo1 was invoked")

def foo2 (num):
    print("foo2 is {0}".format(num))


event.add("foo1" , foo)
event.add("foo2" , foo2)
event.bang("foo1")
event.bang("foo2",137) #add arg
