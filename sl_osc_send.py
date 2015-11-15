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


    def send (self, adr, val):
        osc = OSC.OSCClient()
        self.adr = adr
        self.val = val
        self.msg = OSC.OSCMessage()
        self.msg.setAddress(self.adr)
        self.msg.append(self.val)
        osc.sendto(self.msg, self.destination)
