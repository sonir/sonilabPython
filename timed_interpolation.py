
import time
class TimedInterpolation :

    def __init__ (self):
        self.st = 0.0
        self.ed = 0.0
        self.diff = 0.0
        self.current = 0.0

        self.duration = 0.0
        self.time_st = 0.0
        self.time_ed = 0.0
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
        self.manual_set(self.current, val, sec)


    def update(self):

        if self.end_flg == True or self.duration == 0.0:
            self.current = self.ed
            return self.current
        else:
            self.time_now = time.time()
            self.ellapse = self.time_now - self.time_st
            self.current = self.st + ( self.diff * ( self.ellapse / self.duration ) )
            if self.ellapse > self.duration:
                self.current = self.ed
                self.end_flg = True
            return self.current


    def update_exponential(self):

        if self.end_flg == True or self.duration == 0.0:
            self.current = self.ed
            return self.current
        else:
            self.time_now = time.time()
            self.ellapse = self.time_now - self.time_st
            self.current = self.st + ( self.diff * ( (self.ellapse / self.duration)*(self.ellapse / self.duration) ) )
            if self.ellapse > self.duration:
                self.current = self.ed
                self.end_flg = True
            return self.current


    def print_params(self):
        print "duration: " , self.duration
        print "time_st: " , self.time_st
        print "time_ed: " , self.time_ed
        print "time_now" , self.time_now
        print "ellapse: " , self.ellapse
        print "st: " , self.st
        print "ed: " , self.ed
        print "diff: " , self.diff
        print "current: " , self.current


