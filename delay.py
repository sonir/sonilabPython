from collections import deque
import timer_event, threading

LENGTH = 99
queue = deque([] , maxlen=LENGTH)

def bang(del_time, event_name,*args):
    global queue
    tm = timer_event.Timer_event(del_time, event_name, *args)
    queue.append(tm)

def waiting():
    while True:
        pass

def release():
    queue.clear()
    pass


my_thread = threading.Thread(target=waiting, name="waiting")
my_thread.setDaemon(True)
my_thread.start()
