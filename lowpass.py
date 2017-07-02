#deque is faster more than list
from collections import deque

class Lowpass :

    def __init__ (self, length):
        self.len = length
        self.min_val = 0.005
        self.queue = deque([] , maxlen=length)
        self.current = 0.0

        # make list with 0
        for var in range(0,self.len):
            self.queue.append(0.0)

    def run(self,val):
        self.update(val)
        # self.print_all()
        self.current = self.calc_ave()
        self.current = self.min_check(self.current)
        return self.current

    def update(self, val):
        # self.queue.popleft()
        self.queue.append(val)

    def calc_ave(self):
        self.total = 0
        for var in self.queue:
            self.total = self.total + var
        val = self.total / len(self.queue)
        return val

    def min_check(self, val):
        if val <= self.min_val:
            return 0
        else:
            return val

    def print_all(self):
        for var in self.queue:
            print var

    def reset(self):
        self.queue.clear()
        current = 0.0
        for var in range(0,self.len):
            self.queue.append(0.0)
