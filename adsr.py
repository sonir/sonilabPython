import timed_interpolation
ADSR_PHASE_COUNT = 4

class Adsr:
    #attack, decay and release are tuple with target value and duration
    def __init__(self, attack, decay, sustain, release):
        self.lerp = timed_interpolation.TimedInterpolation()
        self.set_params(attack, decay, sustain,release)
        self.reset()



    def set_params(self, attack, decay, sustain, release):
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        self.count = -1



    def reset(self):
        tmp = self.lerp.current
        self.lerp.manual_set(tmp, tmp, 0.0)
        self.lerp.end_flg = True
        self.count = (-1)



    def set_phase(self):
        if self.count == 1:
            self.lerp.set(self.attack[0], self.attack[1])
        elif self.count == 2:
            self.lerp.set(self.decay[0], self.decay[1])
        elif self.count == 3:
            self.lerp.set(self.decay[0], self.sustain)
        elif self.count == 4:
            self.lerp.set(self.release[0], self.release[1])
        else:
            print "ERR :: ADSR :: UNKNOWN PHASE"




    def bang(self):
        self.count = 0



    def update(self):
        # rest until bang
        if self.count == (-1):
            return

        #check now phase finished
        if self.lerp.end_flg == True:
            self.count += 1 #automatically count 0 is shifted to 1
            self.set_phase()
        #All phase finished, rest
        if self.count > ADSR_PHASE_COUNT:
            self.reset()

        return self.lerp.update_exponential()




