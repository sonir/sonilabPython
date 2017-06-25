import osc_receive, event
receiver = osc_receive.OscReceive(54321)


def foo(vals):
  for val in vals:
    print val

event.add("/foo",foo)
receiver.setup("/foo")


try:
    while True:
        pass

except KeyboardInterrupt :
    receiver.terminate()
