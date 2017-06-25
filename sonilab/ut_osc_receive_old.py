import sl_osc_receive, observer

obs = observer.Observer()
osc = sl_osc_receive.SlOscReceive(54321,obs)

try:
    while True:
        pass

except KeyboardInterrupt :
    osc.terminate()
