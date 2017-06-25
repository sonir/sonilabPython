import OSC

class slOscSend:
    """ Osc Sender """

    def __init__ (self,adr, port):
        self.ip_adr = adr
        self.port = port
        self.destination = (self.ip_adr, self.port)
        self.adr = "/unset"
        self.val = 137
        self.str = 'IP: '
        self.str += self.ip_adr
        self.str += ' PORT: '
        self.str += str(port)
        print(self.str)


#     def send (self, adr, val):
#         osc = OSC.OSCClient()
#         self.adr = adr
#         self.val = val
#         self.msg = OSC.OSCMessage()
#         self.msg.setAddress(self.adr)
#         self.msg.append(self.val)
#         osc.sendto(self.msg, self.destination)

    def send2arg (self, adr, val1, val2):
        osc = OSC.OSCClient()
        self.adr = adr
        self.val1 = val1
        self.val2 = val2
        self.msg = OSC.OSCMessage()
        self.msg.setAddress(self.adr)
        self.msg.append(self.val1)
        self.msg.append(self.val2)
        osc.sendto(self.msg, self.destination)

    def send (self, adr, *args):
        osc = OSC.OSCClient()
        self.adr = adr
        self.msg = OSC.OSCMessage()
        self.msg.setAddress(self.adr)
        for i in args:
            self.msg.append(i)
        osc.sendto(self.msg, self.destination)
