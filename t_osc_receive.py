import sq_osc_receive, observer

obs = observer.Observer()
osc = sq_osc_receive.SqOscReceive(54321,obs)

try:
    while True:
        pass

except KeyboardInterrupt :
    osc.terminate()
