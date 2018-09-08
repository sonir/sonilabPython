# EVENT HANDLER

events = {}

def add(event_name, func):
    global events
    # events = { event_name:func }
    events[event_name] = func

def bang(event_name,*args):
    global events
    if event_name in events:
        func = events[event_name]
        if args:
            return func(*args)
        else:
            return func() #if noatgs, invoke the func without arg
    else:
        print "--> ERR::event::bang::Unknown event [" , event_name, "] was called. Ignore this invoke."
