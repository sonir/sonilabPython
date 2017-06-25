# import sl_metro
import random

class SlBlinkPattern:

    def __init__(self, interval):
        # self.metro = sl_metro.Metro( (interval*0.1) )
        self.list1 = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.list1_interval = 0.2
        self.list2 = [1, 0, 1, 0, 1, 0, 0]
        self.list2_interval = 0.5
        self.list3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.list3_interval = 2
        self.count = -1

    def bang(self) :
        self.count = 0 #flg for start step
        dice = random.randint(1,3)
        if dice==1:
            self.list = self.list1
            return self.list1_interval
        elif dice==2:
            self.list = self.list2
            return self.list2_interval
        elif dice==3:
            self.list = self.list3
            return self.list3_interval
        else:
            print("unknown case in SlBlinkPattern.bang")
            sys.exit(0)



    def reset(self):
        self.bang_flg = False
        self.rotation = 0
        self.now = 0

    def update (self) :

        if self.count == -1:
            return 0

        if self.count >= len(self.list):
            self.count = -1
            return 0

        self.count += 1
        flg = self.list[self.count-1]
        return flg
