import threading, time
import thread_event as tev
import event


class Timer_event(threading.Thread):

    def __init__(self, dl_time, event_name, *args):
        super(Timer_event, self).__init__()
        self.dl_time = dl_time
        self.event_name = event_name
        self.args = args

        #setup threading timer to wait the timer_bang
        self.timer = threading.Timer(dl_time, self.timer_bang)
        self.timer.start()

        #set thread for waiting timer
        self.setDaemon(True) #auto close the thread
        self.start() #start waiting thread ( self.run() )


    def __del__(self):
        self.end()


    def timer_bang(self):
#         tev.bang(self.event_name, self.args)
        event.bang(self.event_name , *self.args )

    def run(self):
        while True:
            pass


    def trash(self):
        self.timer.cancel()


    def end(self):
        self.trash()
        print "stop"
