#8CH GPIO TOGGLE
import RPi.GPIO as GPIO

PIN_A = 3
PIN_B = 5
PIN_C = 7
PIN_D = 11
PIN_E = 13
PIN_F = 15
PIN_G = 19
PIN_H = 21
PIN_I = 23
CH_MAX = 9

class SlGpio :

    try:
        #while True :
        def __init__ (self) :
            print("init")
            self.CH_MAX = CH_MAX
            self.GPIO = GPIO
            self.GPIO.setmode(GPIO.BOARD)
            global PIN_A, PIN_B, PIN_C, PIN_D, PIN_E, PIN_F, PIN_G, PIN_H
            self.ch = [PIN_A, PIN_B, PIN_C, PIN_D, PIN_E, PIN_F, PIN_G, PIN_H]
            self.ch_val = [False, False, False, False, False, False, False, False]

            for var in range(CH_MAX):
                print("The pin {0} was set as OUTPUT".format(self.ch[var]))
                self.GPIO.setup(self.ch[var],GPIO.OUT)


            # self.GPIO.setmode(GPIO.BOARD)
                # self.GPIO.setup(self.pi,GPIO.OUT)

        def set (self, ch, val) :
            if ch >= CH_MAX or ch < 0:
                print("The CH is invalid")
                return False
            else:
                self.ch_val[ch]=val
                return True

        def update(self) :
            for var in range(CH_MAX):
                GPIO.output(self.ch[var],self.ch_val[var])

    except KeyboardInterrupt :
    	GPIO.cleanup()
