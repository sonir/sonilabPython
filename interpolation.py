
class Interpolation :

    def __init__ (self):
        self.st = 0.0
        self.ed = 0.0
        self.now = 0.0
        self.step = 0
        self.step_count = 0


    def set(self, st, ed, step):
        self.st = st
        self.ed = ed
        self.step =step
        self.step_count = 0


    def update(self):
        if self.step_count >= self.step:
            return self.now
        else:
            self.step_count += 1
            self.now = self.st + ( ((self.ed-self.st)/self.step) * self.step_count );
            return self.now
