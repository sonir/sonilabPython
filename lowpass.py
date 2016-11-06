from collections import deque

class Lowpass :

    def __init__ (self, length):
        self.len = length
        self.min_val = 0.005
        self.queue = deque([])
        self.ans = 0.0

        # make list with 0
        for var in range(0,self.len):
            self.queue.append(0.0)

    def run(self,val):
        self.update(val)
        # self.print_all()
        self.ans = self.calc_ave()
        # self.ans = self.min_check(self.ans)
        return self.ans

    def update(self, val):
        self.queue.popleft()
        self.queue.append(val)

    def calc_ave(self):
        self.total = 0
        for var in self.queue:
            self.total = self.total + var
        val = self.total / len(self.queue)
        return val

    def min_check(self, val):
        if val <= self.queue:
            return 0
        else:
            return val

    def print_all(self):
        for var in self.queue:
            print var
