import time

class Metro :
    def __init__ (self, interval) :
        #Interval is Sec (1.0=1sec)
        # self.interval = interval
        # self.reset()
        self.set(interval)

    def update_ellapse (self) :
        self.ed = time.time()
        self.ellapse = (self.ed - self.st)

    def reset(self) :
        self.st = time.time()
        self.ed = time.time()
        self.ellapse = 0

    def update (self) :
        self.update_ellapse()
        if self.ellapse > self.interval :
            self.reset()
            return True
        else:
            pass
            return False

    def set(self, interval):
        self.interval = interval
        self.reset()
