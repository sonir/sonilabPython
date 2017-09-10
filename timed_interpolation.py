
import time
class TimedInterpolation :

    def __init__ (self):
        self.st = 0.0
        self.ed = 0.0
        self.diff = 0.0
        self.now = 0.0

        self.duration = 0.0
        self.time_st = 0.0
        self.time_ed = 0.0
        self.time_diff = 0.0
        self.time_now = 0.0
        self.ellapse = 0.0

        self.end_flg = False


    def manual_set(self, st, ed, sec):
        self.st = st
        self.ed = ed
        self.duration = sec
        self.diff = ed-st
        self.time_st = time.time()
        self.time_ed = self.time_st + self.duration

        self.end_flg = False

    def set(self, val, sec):
        self.manual_set(self.now, val, sec)


    def update(self):

        if self.end_flg == True:
            return self.ed

        self.time_now = time.time()
        self.ellapse = self.time_now - self.time_st
        self.now = self.st + ( self.diff * ( self.ellapse / self.duration ) )
        if self.ellapse > self.duration:
            self.now = self.ed
            self.end_flg = True
        return self.now
