# EVENT HANDLER

events = {}

def add(event_name, func):
    global events
    # events = { event_name:func }
    events[event_name] = func

def bang(event_name,*args):
    global events
    func = events[event_name]
    if args:
        return func(*args)
    else:
        return func() #if noatgs, invoke the func without arg
