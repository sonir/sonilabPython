import sl_gpio2, time

try:
    gpio = sl_gpio2.SlGpio()
    gpio.set(7, True)
    assert(gpio.ch_val[7]==True)
    print("set val is OK")

    assert(gpio.set(7, True)==True)
    assert(gpio.set(8, True)==False)
    assert(gpio.set(-1, True)==False)
    print("CH Test is OK")

    counter = 0
    print("start: loop...")
    while True :
        for var in range(gpio.CH_MAX):
            val = False
            if var == counter:
                val = True
            gpio.set(var,val)
        gpio.update()
        counter = counter + 1
        if counter >= gpio.CH_MAX:
            counter = 0
        time.sleep(0.2)

except KeyboardInterrupt :
	GPIO.cleanup()
