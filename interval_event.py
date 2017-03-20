import threading, time, datetime
import event

class IntervalEvent(threading.Thread):

    def __init__(self, event_name, end_event):
        super(IntervalEvent, self).__init__()
        self.event_name = event_name
        self.end_event = end_event
        self.times = 0
        self.cycle = True
        self.interrupt = False
        self.doing = False


    def set(self, interval, times):
        self.interval = interval
        self.times = times
        if self.doing == True:
            self.interrupt = True


    def run(self):
            while(self.cycle):
                for i in range(self.times):
                    self.doing = True
                    #if set new param, break now repeat
                    if self.interrupt == True:
                        self.interrupt = False
                        self.doing = False
                        event.bang(self.end_event)
                        break
                    #bang event
                    event.bang(self.event_name)
                    time.sleep(self.interval)
                    # Finalize process
                    if i == (self.times-1):
                        if self.end_event != None:
                            event.bang(self.end_event)
                        self.times = 0
                        self.doing = False


    def stop(self):
        event.bang(self.end_event)
        self.cycle = False
        self.interrupt = True


    def test(self):
        event.bang(self.event_name)
