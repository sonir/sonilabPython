import sl_metro

metro = sl_metro.Metro(1.0)

blinker = False
count = 0

while(1):
    #global metro
    if metro.update() :
        count=count+1
        if count>=10:
            metro.set(0.5)
        blinker = ~blinker
        if blinker:
            print("OK")
        else:
            print("NULL")

        # pass#print(1)
