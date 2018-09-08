# for latest https://github.com/ptone/pyosc
from OSC import OSCClient, OSCMessage
# for old version (0.3.5) https://pypi.org/project/pyOSC/#files
# import OSC

class slOscSend:
    """ Osc Sender """

    def __init__ (self,adr, port):
        self.ip_adr = adr
        self.port = port
        self.destination = (self.ip_adr, self.port)
#         self.client = OSC.OSCClient()
        self.client = OSCClient()
        self.client.connect(self.destination)
        self.adr = "/unset"
        self.str = 'IP: '
        self.str += self.ip_adr
        self.str += ' PORT: '
        self.str += str(port)
        print(self.str)



    def send (self, adr, *args):
        self.adr = adr
#         msg = OSC.OSCMessage()
        msg = OSCMessage()
        msg.setAddress(self.adr)
        for i in args:
            msg.append(i)
        try:
            self.client.send(msg)
        except:
          print ">>> ERR :: Could not connect to ", self.ip_adr, ":", self.port
#          osc.sendto(self.msg, self.destination)
