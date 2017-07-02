import threading, event
import tuple_tool as tt

def bang(event_name, *args):
    tuple1 = tt.make(event_name)
    merged_tuple = tt.merge(tuple1, args)

    my_thread = threading.Thread(target=invoke_event, name="th", args=merged_tuple)
    my_thread.setDaemon(True)
    my_thread.start()


def invoke_event(*args):
    print "invoked"
    ev_name = tt.get_top(args)
    splited = tt.split(args, 1)
    striped_args = splited[1]
    if striped_args:
        event.bang(ev_name, *striped_args)
    else:
        event.bang(ev_name)
