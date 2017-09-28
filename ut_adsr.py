import adsr

#attack, decay and release are tuple with target value and duration
adsr = adsr.Adsr((0.95,4.0),(0.25, 5.0), 4.0,(0.0, 4.0))


#Start ADSR
adsr.bang()

while True:

    tmp = "INIT"
    if adsr.count == 1:
        tmp = "ATTACK"
    if adsr.count == 2:
        tmp = "DECAY"
    if adsr.count == 3:
        tmp = "SUSTAIN"
    if adsr.count == 4:
        tmp = "RELEASE"

    print adsr.update() , " : ", tmp


    #Repeat Bang
    if adsr.count == -1:
        adsr.bang()

