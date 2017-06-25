# if you want to use this library from outside of sonilab folder, should import as follows,
# from sonilab import sl_metro, sl_osc_send, osc_receive, event
# enjoy !!

import sl_metro, sl_osc_send, osc_receive, event

metro = sl_metro.Metro(1.0)
sender = sl_osc_send.slOscSend("127.0.0.1" , 57137)
receiver = osc_receive.OscReceive(57137)


def osc_received (vals):
    print "OSC RECEIVED :: arg[0] = " + str(vals[0]) + " | arg[1] = "  + str(vals[1])

event.add("/test" , osc_received)
receiver.setup("/foo")


try :
    while True:
        if metro.update():
            print "OK"
            sender.send("/test", 137, 1.37)

except KeyboardInterrupt :
    receiver.terminate()
